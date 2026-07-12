# 15. Regression II: GLMs and Classification

> **Spine.** Pick the response's generative story, wire its natural parameter through a linear predictor, and you have a GLM — cross-entropy training *is* categorical-GLM maximum likelihood, and any proper prior cures separation.
> **Which line?** Line 1 (choose the joint: the response's exponential-family story) feeding line 3 (predict by *marginalizing* the coefficient posterior, not plugging the mode) — the module's sharpest lesson lives on line 3.
> **Promise.** After this module you can build a GLM for any exponential-family response, explain why the logistic MLE diverges on separable data (and why weight decay is the proper prior that fixes it), and turn a coefficient posterior into a *calibrated* class probability in closed form — integrating, not plugging.
> **Prereqs.** Modules 04 (likelihood→loss dictionary, the exponential-family table, the censoring seed $S(c)$), 05 (conjugacy / Gaussian machinery behind the prior), 10 (`rw_metropolis` pattern), 13 (Laplace = MAP + Hessian), 14 (the Bayesian linear model this generalizes). **Runtime.** ~65 s (includes JAX import + JIT + NUTS).
> **Sources.** ISLP ch. 4, 11; booklet ch. 8, 11; MacKay *ITILA* (moderated outputs) by concept; Ng–Jordan 2002 (generative vs discriminative) by concept, softened.

Module 14 gave the response a Normal story: $y \sim \mathcal N(x^\top\beta, \sigma^2)$, identity link, conjugate everything. But most responses are not Gaussian. A click is Bernoulli, a count of arrivals is Poisson, a time-to-failure is Exponential or Weibull. A **generalized linear model** keeps the one good idea — a *linear predictor* $\eta = x^\top\beta$ — and swaps the Gaussian for whatever exponential-family story the response actually tells, connecting the two through a **link** $g$ that maps the mean onto the linear scale: $g(\mathbb E[y\mid x]) = x^\top\beta$. That is the whole recipe. Everything below is consequences.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "15-glms-classification"          # this module's figure dir
FIG = Path("figures") / SLUG
FIG.mkdir(parents=True, exist_ok=True)
SEED = 0
rng = np.random.default_rng(SEED)

plt.rcParams.update({
    "figure.figsize": (7, 4), "figure.dpi": 110, "savefig.dpi": 150,
    "savefig.bbox": "tight", "axes.grid": True, "grid.alpha": 0.3,
    "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 11,
})

def save(fig, name):
    out = FIG / f"{name}.png"
    fig.savefig(out)
    plt.close(fig)
    print(f"[fig] {out}")
```

## 15.1 The GLM recipe: one table, three members

Module 04's exponential-family table already did the hard part. Each response family has a **natural parameter** $\eta$ — the coordinate in which the log-density is linear in the sufficient statistic. A GLM declares that natural parameter to be a linear function of the covariates. The link that lands you *on* the natural parameter is the **canonical link**; it is the one that makes the sufficient statistic $\sum_i x_i y_i$ and gives the tidiest math, though any monotone link is legal.

| response story | mean $\mu = \mathbb E[y\mid x]$ | canonical link $g(\mu)=\eta$ | inverse link $\mu = g^{-1}(\eta)$ | this is |
|---|---|---|---|---|
| Normal($\mu,\sigma^2$) | $\mu\in\mathbb R$ | identity $\mu$ | $\eta$ | linear regression (M14) |
| Bernoulli($\mu$) | $\mu\in(0,1)$ | logit $\log\frac{\mu}{1-\mu}$ | $\sigma(\eta)=\frac1{1+e^{-\eta}}$ | logistic regression |
| Poisson($\mu$) | $\mu>0$ | log $\log\mu$ | $e^{\eta}$ | log-linear / count regression |

The links are exactly the natural-parameter columns of module 04's table — logit for Bernoulli, $\log$ for Poisson — read as functions of the mean. Fitting a GLM by maximum likelihood *is* minimizing the negative log-likelihood, which by module 04's likelihood→loss dictionary is a named loss: Bernoulli NLL is binary cross-entropy, Poisson NLL is the Poisson deviance. So "train a classifier with cross-entropy" and "fit a Bernoulli GLM by ML" are the same sentence in two dialects. Verify the identity numerically: `sklearn`'s logistic regression (cross-entropy, unpenalized) and a hand-rolled cross-entropy minimizer land on the same coefficients.

```python
from scipy.optimize import minimize
from sklearn.linear_model import LogisticRegression

g1 = np.random.default_rng(0)
n = 400
X = np.column_stack([np.ones(n), g1.normal(0, 1, n), g1.normal(0, 1, n)])
beta_true = np.array([0.4, 1.5, -0.8])
y = g1.binomial(1, 1 / (1 + np.exp(-X @ beta_true)))

# sklearn: C=inf turns off the L2 penalty -> pure cross-entropy MLE.
sk = LogisticRegression(C=np.inf, solver="lbfgs", max_iter=2000).fit(X[:, 1:], y)
coef_sklearn = np.concatenate([sk.intercept_, sk.coef_.ravel()])

# hand-rolled: minimize mean binary cross-entropy = Bernoulli NLL.
def bce(b):
    z = X @ b
    return np.mean(np.logaddexp(0, z) - y * z)      # stable -log Bernoulli(sigma(z))
hand = minimize(bce, np.zeros(3), method="BFGS").x

print("sklearn coef :", np.round(coef_sklearn, 4))
print("hand-CE coef :", np.round(hand, 4))
print(f"max|diff| = {np.max(np.abs(coef_sklearn - hand)):.2e}")
```

The two agree to `1.13e-04` (optimizer tolerance): cross-entropy training and Bernoulli-GLM maximum likelihood are the same optimization. The fitted slopes `1.7105` and `-0.7317` sit near the truth $(1.5,-0.8)$; the intercept `0.4737` near $0.4$. Nothing here is new statistics — it is module 04's log loss with a linear predictor bolted on.

## 15.2 Separation: the MLE's silent divergence

Here is where the maximum-likelihood story breaks, and the break is instructive.

**Setup.** Two clouds of points, one per class, that a straight line can perfectly separate. Fit unpenalized logistic regression.

**Predict.** Commit before running. *What does the MLE do to the weight vector $\hat w$ on perfectly separable data?* The naive picture: the optimizer finds the best separating line and reports finite coefficients, like any other fit. (The intuition being used: "maximum likelihood always returns a finite estimate at the peak of the likelihood.")

```python
import warnings
from sklearn.linear_model import LogisticRegression

gs = np.random.default_rng(1)
Xa = gs.normal([-2, 0], 1.0, size=(20, 2))       # class 0
Xb = gs.normal([2, 0], 1.0, size=(20, 2))        # class 1
Xsep = np.vstack([Xa, Xb]); ysep = np.r_[np.zeros(20), np.ones(20)]
Xd = np.column_stack([np.ones(40), Xsep])
print(f"linearly separable? gap along x0 = {Xb[:,0].min() - Xa[:,0].max():.3f} > 0")

def mean_ce(b):
    z = Xd @ b
    return np.mean(np.logaddexp(0, z) - ysep * z)

# March the MLE's L2 penalty toward zero (prior variance -> infinity): ||w|| blows up.
print("  prior var (C)   ||w||")
with warnings.catch_warnings():
    warnings.simplefilter("ignore")            # separable data => lbfgs won't 'converge'
    for C in [1, 10, 100, 1000, np.inf]:
        m = LogisticRegression(C=C, solver="lbfgs", max_iter=10000).fit(Xsep, ysep)
        w = np.r_[m.intercept_, m.coef_.ravel()]
        print(f"    {C:>8g}    {np.linalg.norm(w):6.3f}")
        if C == np.inf:
            w_dir = w / np.linalg.norm(w)      # the separating direction

# Loss along that direction as ||w|| grows: it decreases forever, no finite minimizer.
print("  ||w||    mean cross-entropy along the separating direction")
for t in [1, 2, 4, 8, 16, 32]:
    print(f"    {t:>3}     {mean_ce(t * w_dir):.5f}")
```

The weight norm does not settle — it grows without bound as the penalty relaxes: `1.944` at $C=1$, `8.124` at $C=100$, `17.955` with the penalty fully off, and it would keep climbing if the optimizer let it. The reason is in the second table: mean cross-entropy along the separating direction falls monotonically — `0.20116`, `0.08344`, `0.02956`, `0.00619`, `0.00031`, `0.00000` — toward zero as $\|w\|\to\infty$, with **no finite minimizer**. On separable data the likelihood is maximized only in the limit of infinite confidence: the model wants to predict every training point with probability exactly 0 or 1, and it can only approach that by sending $\|w\|\to\infty$. The naive picture fails because the likelihood surface has no interior peak — its supremum sits at the boundary of parameter space.

```python
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
th = np.linspace(0.2, 40, 200)
ax[0].plot(th, [mean_ce(t * w_dir) for t in th], color="C1", lw=2)
ax[0].set_xlabel(r"$\|w\|$ along the separating direction")
ax[0].set_ylabel("mean cross-entropy (training)")
ax[0].set_title("MLE loss has no finite minimizer:\nit falls to 0 as $\\|w\\|\\to\\infty$")
# right: the data and a few separating lines of growing steepness
for t, c in [(1, "C0"), (4, "C2"), (16, "C3")]:
    b = t * w_dir
    xs = np.linspace(-5, 5, 100)
    ax[1].plot(xs, -(b[0] + b[1]*xs)/b[2], color=c, lw=1.5, label=f"$\\|w\\|={t}$")
ax[1].scatter(*Xa.T, c="C0", s=25, label="class 0")
ax[1].scatter(*Xb.T, c="C3", s=25, marker="^", label="class 1")
ax[1].set_xlabel("$x_0$"); ax[1].set_ylabel("$x_1$"); ax[1].set_ylim(-4, 4)
ax[1].set_title("same boundary, steeper and steeper"); ax[1].legend(fontsize=8)
save(fig, "separation")
```

![Left: mean cross-entropy versus weight norm, a curve that decays monotonically toward zero with no interior minimum. Right: the two point clouds with three separating lines of increasing steepness that share essentially the same location but represent ever-larger weight norms.](figures/15-glms-classification/separation.png)

The cure is generative. A proper Gaussian prior $\beta \sim \mathcal N(0, \tau^2 I)$ adds $\frac1{2\tau^2}\|\beta\|^2$ to the negative log-posterior — exactly the L2 / weight-decay term — and now the objective is $\|w\|^2$-penalized cross-entropy, which is strictly convex and *has* a finite minimizer for any finite $\tau^2$. In the table, that is the $C<\infty$ rows: $C=1/(n\lambda)$ is the prior variance in disguise, and every finite $C$ returns a finite $\|\hat w\|$. This is the generative answer to "why does weight decay help": it is not a numerical trick, it is the statement that you do not actually believe the separating margin is infinitely sharp. Any prior that assigns positive density to finite coefficients and vanishing density to $\|\beta\|=\infty$ regularizes the divergence away. Deep networks on separable batches have the same pathology (the logits of a correctly-classified point can always be scaled up to cut its loss); weight decay is the same prior, wearing the same costume.

## 15.3 Bayesian logistic regression three ways

Unlike the Beta-Binomial, the logistic posterior has no closed form — the Bernoulli likelihood times a Gaussian prior is not conjugate. So this is the first model where we must *approximate or sample*, and it is the perfect place to check that our three tools from Part III agree. Take a modest, non-separable dataset ($n=50$, two features plus intercept) and a weak prior $\beta \sim \mathcal N(0, 3^2 I)$, and fit the coefficient posterior three ways.

**Route 1 — Laplace (module 13's machinery).** Find the MAP by minimizing the negative log-posterior, then set $\Sigma = H^{-1}$ where $H = X^\top W X + \tau^{-2}I$ is the negative Hessian at the mode, $W=\mathrm{diag}(p_i(1-p_i))$. One optimization, one Hessian, a Gaussian.

**Route 2 — Metropolis–Hastings (module 10's `rw_metropolis`).** The same random-walk sampler, promoted to $d=3$: propose $\beta' = \beta + \text{step}\cdot Z$, accept in log space with ratio $\log p(\beta') - \log p(\beta)$. Only the log-posterior is needed, up to a constant.

```python
g3 = np.random.default_rng(2)
n = 50
Xa3, Xb3 = g3.normal(0, 1.2, n), g3.normal(0, 1.2, n)
Xc = np.column_stack([np.ones(n), Xa3, Xb3]); d = 3
beta3 = np.array([0.5, 1.2, -0.9])
yc = g3.binomial(1, 1 / (1 + np.exp(-Xc @ beta3)))
tau = 3.0

def neg_log_post(b):
    z = Xc @ b
    log_lik = np.sum(yc * z - np.logaddexp(0, z))
    return -(log_lik - 0.5 * np.sum(b**2) / tau**2)        # + Gaussian-prior penalty

# Route 1: Laplace = MAP + curvature (module 13).
b_map = minimize(neg_log_post, np.zeros(d), method="BFGS").x
p = 1 / (1 + np.exp(-Xc @ b_map))
H = (Xc.T * (p * (1 - p))) @ Xc + np.eye(d) / tau**2        # negative Hessian at the mode
Sigma = np.linalg.inv(H)
sd_lap = np.sqrt(np.diag(Sigma))
print("Laplace  mean:", np.round(b_map, 3), " sd:", np.round(sd_lap, 3))

# Route 2: random-walk Metropolis (module 10's pattern, promoted to d=3).
def rw_metropolis(log_p, x0, step, n_draws, gen):
    x, lx = x0.copy(), log_p(x0); chain = np.empty((n_draws, len(x0))); acc = 0
    for t in range(n_draws):
        xp = x + step * gen.standard_normal(len(x0))
        lp = log_p(xp)
        if np.log(gen.random()) < lp - lx:
            x, lx, acc = xp, lp, acc + 1
        chain[t] = x
    return chain, acc / n_draws

g_mh = np.random.default_rng(10)
chain, acc = rw_metropolis(lambda b: -neg_log_post(b), b_map.copy(),
                           2.0 * sd_lap.mean(), 60_000, g_mh)
chain = chain[5000:]
print(f"MH (acc={acc:.3f}) mean:", np.round(chain.mean(0), 3),
      " sd:", np.round(chain.std(0), 3))
```

**Route 3 — NUTS (NumPyro, the course PPL).** The same model handed to the gradient-based sampler, using the idioms from `tools/ppl_idioms.py`.

```python
import jax
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS

def logreg(X, y=None):
    b = numpyro.sample("b", dist.Normal(0.0, tau).expand([X.shape[1]]))
    numpyro.sample("y", dist.Bernoulli(logits=X @ b), obs=y)

mcmc = MCMC(NUTS(logreg), num_warmup=600, num_samples=800, num_chains=2,
            chain_method="sequential", progress_bar=False)
mcmc.run(jax.random.PRNGKey(0), X=np.asarray(Xc), y=np.asarray(yc).astype(float))
b_nuts = np.asarray(mcmc.get_samples()["b"])
print("NUTS     mean:", np.round(b_nuts.mean(0), 3),
      " sd:", np.round(b_nuts.std(0), 3))
print(f"max|mean| Laplace-vs-NUTS = {np.max(np.abs(b_map - b_nuts.mean(0))):.3f}"
      f"   MH-vs-NUTS = {np.max(np.abs(chain.mean(0) - b_nuts.mean(0))):.3f}")

fig, ax = plt.subplots(1, 3, figsize=(12, 3.4))
names = [r"$\beta_0$ (intercept)", r"$\beta_1$", r"$\beta_2$"]
for j in range(3):
    ax[j].hist(chain[:, j], bins=50, density=True, alpha=0.4, color="C0", label="MH")
    ax[j].hist(b_nuts[:, j], bins=50, density=True, alpha=0.4, color="C2", label="NUTS")
    gg = np.linspace(*ax[j].get_xlim(), 200)
    ax[j].plot(gg, stats.norm(b_map[j], sd_lap[j]).pdf(gg), "C1", lw=2, label="Laplace")
    ax[j].set_title(names[j]); ax[j].set_yticks([])
ax[0].legend(fontsize=8)
fig.suptitle("Three routes to the same logistic posterior (n=50)")
save(fig, "three-ways")
```

![Three panels, one per coefficient, each overlaying the Metropolis histogram, the NUTS histogram, and the Laplace Gaussian curve; the two sampled histograms sit on top of each other and the Laplace curve tracks them with a slight leftward shift on the steepest coefficient.](figures/15-glms-classification/three-ways.png)

The two *exact* samplers are indistinguishable — MH and NUTS posterior means differ by at most `0.028` across all three coefficients, well inside Monte Carlo error, and their standard deviations agree to two digits (`0.331`, `0.314`, `0.373` from NUTS). Laplace tracks them but its center sits `0.100` short of the posterior mean *in magnitude* on the steepest coefficient (mode $-0.803$ vs mean $-0.903$ for $\beta_2$: closer to zero): the $n=50$ posterior is skewed with its heavier tail pointing *away* from zero, and Laplace reports the *mode*, which for a skewed density is not the mean. That gap is small here and it is also a preview — the difference between "where the posterior peaks" and "what the posterior averages to" is precisely what the next section is about.

## 15.4 Integrate, don't plug: calibrated probabilities in closed form

You have a coefficient posterior. A new $x_\star$ arrives. What is $P(y_\star=1\mid x_\star, \text{data})$? Line 3 of the spine is unambiguous — prediction is *marginalization*:
$$P(y_\star=1\mid x_\star) = \int \sigma(x_\star^\top\beta)\, p(\beta\mid \text{data})\, d\beta,$$
the posterior-averaged sigmoid, **not** the plug-in $\sigma(x_\star^\top\hat\beta)$ that evaluates the sigmoid at a single $\beta$. Because $\sigma$ is curved, the average of the sigmoid is not the sigmoid of the average (Jensen), and the two differ in a specific, correctable direction.

MacKay's **moderated approximation** gives the integral in closed form. Approximate the posterior as $\mathcal N(\mu,\Sigma)$; then $a = x_\star^\top\beta$ is Gaussian with mean $m=x_\star^\top\mu$ and variance $s^2 = x_\star^\top\Sigma x_\star$, and the probit-matched Gaussian integral of a logistic yields
$$P(y_\star=1\mid x_\star) \;\approx\; \sigma\!\left(\frac{m}{\sqrt{1 + \tfrac{\pi}{8}s^2}}\right).$$
The denominator $\sqrt{1+\tfrac\pi8 s^2}$ shrinks the logit toward zero — toward $p=0.5$ — by an amount set by the *predictive variance* $s^2$. Check it against brute-force Monte Carlo integration over the Laplace posterior from §15.3 — and before the scan below runs, commit to a prediction: *where along a slice of input space is the plug-in-vs-integrated gap largest — at the decision boundary, where class uncertainty peaks, or somewhere else?* (The intuition being used: "corrections for uncertainty matter most where the model is most uncertain, i.e. at $p=0.5$.")

```python
def plug_in(x):  return 1 / (1 + np.exp(-x @ b_map))
def mackay(x):
    m, s2 = x @ b_map, x @ Sigma @ x
    return 1 / (1 + np.exp(-m / np.sqrt(1 + np.pi / 8 * s2)))
g_mc = np.random.default_rng(7)
draws = g_mc.multivariate_normal(b_map, Sigma, 300_000)
def mc_integrate(x): return np.mean(1 / (1 + np.exp(-draws @ x)))

x_bnd = np.array([1.0, -b_map[0] / b_map[1], 0.0])       # a point on the m=0 boundary
x_conf = np.array([1.0, 2.5, 0.0])                       # a confident point
for name, x in [("boundary", x_bnd), ("confident", x_conf)]:
    print(f"{name:9s}: plug-in={plug_in(x):.4f}  MacKay={mackay(x):.4f}  "
          f"MC={mc_integrate(x):.4f}")

# Where is the plug-in/integrated gap largest? Scan a slice; then shrink it with n.
x1s = np.linspace(-3, 3, 121)
gap = [abs(plug_in(np.array([1., t, 0.])) - mackay(np.array([1., t, 0.]))) for t in x1s]
i = int(np.argmax(gap))
print(f"n=50 : max|plug-in - MacKay| = {gap[i]:.4f} at plug-in p = "
      f"{plug_in(np.array([1., x1s[i], 0.])):.3f}")
```

If you predicted "at the boundary," you were caught by exactly the intuition named above. At the decision **boundary** ($m=0$) all three agree at `0.5000` — the gap is *exactly zero* there, because shrinking a zero logit toward zero changes nothing. Move to a **confident** point and they part: plug-in says `0.8259`, but the honest integrated probability is `0.7988` (Monte Carlo) — and MacKay's closed form nails it at `0.8005`, matching the expensive integral without drawing a sample. The plug-in is **overconfident**: it reports the probability you would assign if you knew $\beta$ exactly, ignoring that you do not. Scanning the slice, the gap peaks at `0.0332` at a fairly confident prediction (plug-in $p\approx$ `0.854`): class uncertainty and *parameter* uncertainty are different things, and the correction is largest not where the class is uncertain but where the plug-in is confident while the posterior is still wide.

The size of the correction is $s^2 = x_\star^\top\Sigma x_\star$, the epistemic variance — which shrinks as data accumulates. Refit at $n=500$ and the whole gap collapses.

```python
gL = np.random.default_rng(2)
nL = 500
XL = np.column_stack([np.ones(nL), gL.normal(0, 1.2, nL), gL.normal(0, 1.2, nL)])
yL = gL.binomial(1, 1 / (1 + np.exp(-XL @ beta3)))
def nlp_L(b):
    z = XL @ b
    return -(np.sum(yL * z - np.logaddexp(0, z)) - 0.5 * np.sum(b**2) / tau**2)
bL = minimize(nlp_L, np.zeros(d), method="BFGS").x
pL = 1 / (1 + np.exp(-XL @ bL))
SigL = np.linalg.inv((XL.T * (pL * (1 - pL))) @ XL + np.eye(d) / tau**2)
def pl_L(x): return 1 / (1 + np.exp(-x @ bL))
def mk_L(x):
    m, s2 = x @ bL, x @ SigL @ x
    return 1 / (1 + np.exp(-m / np.sqrt(1 + np.pi / 8 * s2)))
gapL = max(abs(pl_L(np.array([1., t, 0.])) - mk_L(np.array([1., t, 0.]))) for t in x1s)
print(f"n=500: max|plug-in - MacKay| = {gapL:.4f}")

fig, ax = plt.subplots(figsize=(7, 4))
xg = np.linspace(-4, 4, 200)
ax.plot(xg, [plug_in(np.array([1., t, 0.])) for t in xg], "C1--", lw=2, label=r"plug-in $\sigma(x^\top\hat\beta)$")
ax.plot(xg, [mackay(np.array([1., t, 0.])) for t in xg], "C0", lw=2, label="MacKay (integrated)")
ax.plot(xg, [mc_integrate(np.array([1., t, 0.])) for t in xg], "k:", lw=1.5, label="Monte Carlo")
ax.axhline(0.5, color="gray", lw=0.8); ax.set_xlabel(r"$x_1$ (at $x_2=0$)")
ax.set_ylabel(r"$P(y=1\mid x)$"); ax.legend(fontsize=9)
ax.set_title("Plug-in is overconfident; integrating pulls probabilities toward 0.5")
save(fig, "moderation")
```

![A slice of predicted probability versus x1. The plug-in dashed curve is steeper, reaching more extreme probabilities; the integrated MacKay curve and the Monte Carlo dotted curve lie on top of each other, less steep, everywhere pulled toward 0.5 except at the crossing point where all three meet.](figures/15-glms-classification/moderation.png)

At $n=500$ the maximum gap is `0.0034` — an order of magnitude smaller than at $n=50$. "Integrate, don't plug" is a small correction when data are plentiful and a large one when they are scarce; MacKay's one-line formula buys the correction for free. The plug-in is the $s^2\to0$ limit — the answer of a model that has stopped admitting it could be wrong.

## 15.5 Calibration: does the honest probability keep its promise?

A classifier is **calibrated** if, among the cases it calls 70%, about 70% are positives. The plug-in's overconfidence should show up as *miscalibration* — it will call things 95% that are only 90%. Measure it with a **reliability diagram** (bin predictions, plot bin-mean prediction against bin-mean outcome; calibration is the diagonal) and its scalar summary, the expected calibration error (ECE) — first met in module 01, where an overconfident forecaster inflated ECE roughly 13× over an honest one; here the same diagnostic, built into a reusable `ece()` harness, grades a classifier's plug-in against its marginalized probabilities. To beat down the noise, pool predictions over 300 small training sets ($n=40$, where overconfidence bites) and a fresh test point each.

```python
def fit_laplace(Xt, yt, tau=3.0):
    dd = Xt.shape[1]
    def nlp(b):
        z = Xt @ b
        return -(np.sum(yt * z - np.logaddexp(0, z)) - 0.5 * np.sum(b**2) / tau**2)
    b = minimize(nlp, np.zeros(dd), method="BFGS").x
    p = 1 / (1 + np.exp(-Xt @ b))
    return b, np.linalg.inv((Xt.T * (p * (1 - p))) @ Xt + np.eye(dd) / tau**2)

def make(n_, gen):
    Xx = np.column_stack([np.ones(n_), gen.normal(0, 1.2, n_), gen.normal(0, 1.2, n_)])
    return Xx, gen.binomial(1, 1 / (1 + np.exp(-Xx @ beta3)))

def ece(p, y, n_bins=10):
    edges = np.linspace(0, 1, n_bins + 1); e = 0.0
    for i in range(n_bins):
        m = (p >= edges[i]) & (p < edges[i + 1])
        if m.sum():
            e += m.mean() * abs(y[m].mean() - p[m].mean())
    return e

P_plug, P_int, Y = [], [], []
for r in range(300):
    gg = np.random.default_rng(r)
    Xt, yt = make(40, gg); b, S = fit_laplace(Xt, yt)
    Xe, ye = make(50, gg)
    m = Xe @ b; s2 = np.einsum("ij,jk,ik->i", Xe, S, Xe)
    P_plug.append(1 / (1 + np.exp(-m)))
    P_int.append(1 / (1 + np.exp(-m / np.sqrt(1 + np.pi / 8 * s2))))
    Y.append(ye)
P_plug, P_int, Y = map(np.concatenate, (P_plug, P_int, Y))
print(f"ECE integrated = {ece(P_int, Y):.4f}   ECE plug-in = {ece(P_plug, Y):.4f}")
hi_p, hi_i = P_plug >= 0.9, P_int >= 0.9
print(f"cases called >=0.90:  plug-in predicts {P_plug[hi_p].mean():.3f}, "
      f"actual {Y[hi_p].mean():.3f}   |   integrated predicts {P_int[hi_i].mean():.3f}, "
      f"actual {Y[hi_i].mean():.3f}")

fig, ax = plt.subplots(figsize=(5.2, 5))
edges = np.linspace(0, 1, 11); ctr = (edges[:-1] + edges[1:]) / 2
for p, lab, c, mk in [(P_plug, "plug-in", "C1", "s"), (P_int, "integrated", "C0", "o")]:
    yb = [Y[(p >= edges[i]) & (p < edges[i+1])].mean() if ((p >= edges[i]) & (p < edges[i+1])).sum() else np.nan
          for i in range(10)]
    ax.plot(ctr, yb, mk + "-", color=c, label=lab)
ax.plot([0, 1], [0, 1], "k--", lw=1, label="perfect")
ax.set_xlabel("predicted probability"); ax.set_ylabel("observed frequency")
ax.set_title("Reliability: plug-in bows below the diagonal (overconfident)")
ax.legend(fontsize=9); save(fig, "calibration")
```

![A reliability diagram. The integrated curve hugs the diagonal; the plug-in curve bows below it in the high-probability region, meaning cases it calls very likely are positive less often than promised.](figures/15-glms-classification/calibration.png)

The integrated predictor's ECE is `0.0207`; the plug-in's is `0.0401`, roughly twice as miscalibrated. The failure is concrete: among the cases the plug-in calls at least 90% likely, it predicts an average of `0.959` but only `0.915` are actually positive — a four-point overconfidence gap. The integrated predictor, having pulled those probabilities toward 0.5 by exactly the predictive-variance correction, predicts `0.944` against an actual `0.923`. A well-specified Bayesian model that *marginalizes* is calibrated almost by construction; the same model that *plugs in the mode* is not. This reliability harness returns in module 25 to audit deep ensembles and temperature scaling.

## 15.6 Generative vs discriminative: a race, softened

Logistic regression is **discriminative** — it models $p(y\mid x)$ directly. Its generative cousin, **naive Bayes**, models $p(x\mid y)\,p(y)$ (Gaussian class-conditionals with the "naive" assumption that features are independent given the class) and turns the crank of Bayes' rule to get $p(y\mid x)$. When the class-conditionals are Gaussian with equal covariance, *both* imply a linear decision boundary — so which should you use?

The folklore (Ng & Jordan 2002) is that naive Bayes, with its stronger assumptions, converges to its best error with *fewer* samples, while logistic regression has an *equal-or-lower asymptotic* error. That is a claim about two curves, and it is easy to overstate, so measure it directly — under a **well-specified** naive-Bayes world (features truly conditionally independent) and a **misspecified** one (features correlated within class, which naive Bayes wrongly ignores).

```python
from sklearn.naive_bayes import GaussianNB

def error_curves(well_specified, d=8, reps=50, ns=(20, 40, 80, 160, 320, 640)):
    if well_specified:
        mean_diff = 0.9 * np.ones(d); Cov = np.eye(d)          # NB assumption holds
    else:
        mean_diff = np.zeros(d); mean_diff[0] = 1.6            # signal in one feature
        Cov = 0.25 * np.eye(d) + 0.75 * np.ones((d, d))        # correlated: NB ignores it
    m0, m1 = -mean_diff / 2, mean_diff / 2
    nb_err, lr_err = [], []
    for n_ in ns:
        e_nb, e_lr = [], []
        for r in range(reps):
            gg = np.random.default_rng(2000 + r)
            def draw(nn):
                lab = (gg.random(nn) < 0.5).astype(int); Xx = np.zeros((nn, d))
                Xx[lab == 0] = gg.multivariate_normal(m0, Cov, (lab == 0).sum())
                Xx[lab == 1] = gg.multivariate_normal(m1, Cov, (lab == 1).sum())
                return Xx, lab
            Xt, yt = draw(n_); Xe, ye = draw(3000)
            e_nb.append(1 - GaussianNB().fit(Xt, yt).score(Xe, ye))
            e_lr.append(1 - LogisticRegression(max_iter=800).fit(Xt, yt).score(Xe, ye))
        nb_err.append(np.mean(e_nb)); lr_err.append(np.mean(e_lr))
    return np.array(ns), np.round(nb_err, 3), np.round(lr_err, 3)

ns, nbW, lrW = error_curves(True)
_,  nbM, lrM = error_curves(False)
print("well-specified  NB:", nbW, " LR:", lrW)
print("misspecified    NB:", nbM, " LR:", lrM)

fig, ax = plt.subplots(1, 2, figsize=(11, 4), sharey=False)
for a, (nb, lr, ttl) in zip(ax, [(nbW, lrW, "well-specified NB world"),
                                  (nbM, lrM, "misspecified NB world")]):
    a.plot(ns, nb, "C0o-", label="naive Bayes")
    a.plot(ns, lr, "C1s-", label="logistic")
    a.set_xscale("log"); a.set_xlabel("training size n"); a.set_ylabel("test error")
    a.set_title(ttl); a.legend(fontsize=9)
fig.suptitle("Generative reaches its asymptote fast; discriminative's asymptote is equal-or-lower")
save(fig, "gen-vs-disc")
```

![Two panels of test error versus log training size. Left (well-specified): the naive-Bayes and logistic curves descend together to the same floor near 0.10. Right (misspecified): naive Bayes flattens early at about 0.20 while logistic keeps descending to about 0.07, ending well below it.](figures/15-glms-classification/gen-vs-disc.png)

Read the numbers. In the **well-specified** world both methods converge to the same floor — naive Bayes `0.104`, logistic `0.105` at $n=640$: when the generative model is *true*, its extra assumptions cost nothing asymptotically. Note that even here NB never *leads* at small $n$ in this regime (at $n=20$ it trails, `0.191` vs `0.16` — its $2d$ per-class means and variances are themselves noisy estimates); the famed "generative is sample-efficient" beat shows up instead as the *speed* of convergence in the right panel. In the **misspecified** world the story separates: naive Bayes races to its (biased) plateau — `0.229`, `0.217`, `0.215`, `0.204` — nearly asymptotic by $n=160$ while logistic is still descending, because NB's false independence assumption caps how well it can ever do; logistic keeps improving to `0.069`, a far lower asymptote, because it never assumed independence and can learn to discount the correlated noise. The honest claim is exactly the softened one: **the gap shrinks (well-specified) and can reverse (misspecification favors the discriminative model)** — but there is no guaranteed crossover, and at any fixed $n$ the ranking depends on the problem. Naive Bayes buys sample-efficiency with a modeling assumption; when that assumption is false, the bill comes due at the asymptote.

## 15.7 Survival regression: conditioning on exactly what you observed

Module 04 planted the seed: an observation known only as $Y>c$ contributes the survival function $S(c)=P(Y>c)$ to the likelihood, not a density. Survival regression cashes that seed. Model a lifetime as Exponential with a covariate-dependent rate through a log link, $\lambda_i = \exp(x_i^\top\beta)$ (the Poisson row's link, now on a hazard), and let each unit be either observed to fail at time $t_i$ (contributes the density $\lambda_i e^{-\lambda_i t_i}$) or still alive at the censoring time $c$ (contributes $S(c)=e^{-\lambda_i c}$). The log-likelihood just sums the right contribution per unit:
$$\ell(\beta) = \sum_{i:\ \text{failed}} \big(\log\lambda_i - \lambda_i t_i\big) \;+\; \sum_{i:\ \text{censored}} \big(-\lambda_i c\big).$$
**Setup.** $n=1000$ units, true log-hazard $\log\lambda = 0.2 + 0.6x$, study ends at $c=1$ — about 30% of units are still alive at the end. The tempting shortcut: drop the censored rows and fit only the observed failures.

**Predict.** Commit to a *direction and rough size* before running. Dropping 30% of rows loses information, so the estimates get noisier — but do they get *biased*? If so, which way: does the fitted hazard $\lambda(x)$ come out too high or too low, and does the slope on $x$ steepen or flatten? (The intuition being used: "deleting rows costs variance, not bias — missing data just means less data.")

```python
gsv = np.random.default_rng(5)
n = 1000
xc = gsv.normal(0, 1, n); Xs = np.column_stack([np.ones(n), xc])
beta_surv = np.array([0.2, 0.6])                      # true log-rate coefficients
lam = np.exp(Xs @ beta_surv)
T = gsv.exponential(1 / lam)                          # true lifetimes
c = 1.0
obs = np.minimum(T, c); failed = (T <= c).astype(float)
print(f"censored fraction = {1 - failed.mean():.3f}")

def nll_censored(b):                                  # correct: survivors contribute S(c)
    z = Xs @ b; lam_ = np.exp(z)
    return -np.sum(failed * (z - lam_ * obs) + (1 - failed) * (-lam_ * obs))
b_correct = minimize(nll_censored, np.zeros(2), method="BFGS").x

keep = failed == 1                                    # WRONG: drop the censored rows
def nll_dropped(b):
    z = Xs[keep] @ b; lam_ = np.exp(z)
    return -np.sum(z - lam_ * obs[keep])
b_dropped = minimize(nll_dropped, np.zeros(2), method="BFGS").x

print("true beta      :", beta_surv)
print("censored MLE   :", np.round(b_correct, 4), " (conditions on Y>c for survivors)")
print("drop-censored  :", np.round(b_dropped, 4), " (biased: discards survivor info)")

fig, ax = plt.subplots(figsize=(7, 4))
xg = np.linspace(-2.5, 2.5, 100)
ax.plot(xg, np.exp(b_correct[0] + b_correct[1]*xg), "C0", lw=2, label="censored MLE")
ax.plot(xg, np.exp(b_dropped[0] + b_dropped[1]*xg), "C1--", lw=2, label="drop-censored")
ax.plot(xg, np.exp(beta_surv[0] + beta_surv[1]*xg), "k:", lw=1.5, label="truth")
ax.set_xlabel("covariate x"); ax.set_ylabel(r"fitted hazard $\lambda(x)=e^{x^\top\beta}$")
ax.set_title("Dropping censored rows inflates the baseline and flattens the slope")
ax.legend(fontsize=9); save(fig, "survival")
```

![Fitted hazard versus covariate. The censored-MLE curve tracks the truth; the drop-censored curve sits well above it and rises more slowly, both baseline inflated and slope flattened.](figures/15-glms-classification/survival.png)

**Reconcile.** With `0.305` of the units censored, the correct likelihood recovers `[0.2174 0.554 ]` against the truth $(0.2, 0.6)$. Dropping the censored rows returns `[0.9727 0.1628]` — the intercept nearly quintuples and the slope collapses toward zero. The "less data, more noise" intuition fails because the deletion is not random: rows go missing *because* their lifetimes are long, so the deletion mechanism is informative (module 11's MNAR, wearing a survival costume). Deleting survivors conditions on "failed before $c$" — a different event from what you observed — and preferentially removes the low-hazard units, dragging the fitted hazard up and washing out its dependence on $x$. The mechanism is line 2 of the spine: inference is conditioning *on exactly what you observed*, and for a survivor what you observed is $Y>c$, not a failure and not nothing. The same $S(c)$ term generalizes immediately to Weibull (add a shape parameter, so the hazard can rise or fall with age) and to interval- or left-censoring (each contributes the probability of its own observation event) — same recipe, richer stories.

**Ordinal responses**, one more link away, use the **cumulative-link** (ordered-logit) model: a single latent linear predictor $x^\top\beta$ with a set of ordered cut-points $\alpha_1<\cdots<\alpha_{K-1}$, so $P(y\le k) = \sigma(\alpha_k - x^\top\beta)$ — the logistic link applied to *cumulative* categories. It is the natural model for Likert-scale and rating data, and it is the last member of the recipe we will name.

## Bridge — cross-entropy, weight decay, and calibration are one model

Three staples of a deep-learning pipeline are three faces of this module's GLM. **Cross-entropy loss** is the Bernoulli/categorical NLL (§15.1) — training a softmax classifier by cross-entropy *is* fitting a categorical GLM by maximum likelihood, the linear predictor now the network's final layer. **Weight decay** is the Gaussian prior that cures separation (§15.2): the same $\frac1{2\tau^2}\|\beta\|^2$ penalty, the generative statement that infinite-margin confidence is not credible. And the **overconfidence of a plug-in softmax** (§15.4–15.5) is why trained networks are famously miscalibrated: they report $\sigma(x^\top\hat\beta)$ at a point estimate and never integrate over what they do not know about their weights. The Bayesian reading tells you the *direction* of the fix — average over the posterior, or approximate the averaging (MacKay, deep ensembles, temperature scaling) — and module 25 cashes exactly this ledger.

## Pitfalls

- **Fitting unpenalized logistic regression on separable (or near-separable) data.** The coefficients diverge and the "converged" values you get are an artifact of the optimizer's tolerance, not a maximum. Symptom: enormous weights, probabilities pinned at 0/1. Fix: any proper prior (L2 / a finite `C`), which is weight decay by another name.
- **Reporting $\sigma(x^\top\hat\beta)$ as *the* probability.** The plug-in ignores coefficient uncertainty and is systematically overconfident, worst at small $n$ and off-support. Integrate (MacKay's $\sqrt{1+\tfrac\pi8 s^2}$ costs one line) or you will ship miscalibrated confidence.
- **Dropping censored observations in survival / time-to-event data.** Survivors carry information ($Y>c$); deleting them conditions on the wrong event and biases the hazard (intercept up, slope flat, as above). Write the $S(c)$ term.
- **Forgetting the offset in rate/count models.** When exposure varies across units, the response is a *rate*, not a count; omit $\log(\text{exposure})$ and the coefficients absorb exposure differences (Exercise 15.3).
- **Believing naive Bayes always loses.** It reaches its asymptote fast and, when its assumptions hold, matches logistic throughout. It loses *asymptotically only under misspecification* — no universal crossover.

## Exercises

**Exercise 15.1 — Separation and the weight-decay cure (ML/DL bridge).**
*Setup:* The separable data of §15.2. You fit logistic regression with a Gaussian prior $\beta\sim\mathcal N(0,\tau^2 I)$, i.e. `LogisticRegression(C=...)` with $C\propto\tau^2$, and slide $\tau^2$ from small to enormous.
*Predict:* As $\tau^2\to\infty$ (penalty $\to 0$), does $\|\hat\beta\|$ approach a finite limit, or diverge? Commit to one.
*Reason:* The intuition to test: "more prior variance just means a less-regularized but still finite fit" — the same intuition a practitioner has about turning weight decay down.
*Run:*
```python
gs = np.random.default_rng(1)
Xa = gs.normal([-2, 0], 1.0, size=(20, 2)); Xb = gs.normal([2, 0], 1.0, size=(20, 2))
Xsep = np.vstack([Xa, Xb]); ysep = np.r_[np.zeros(20), np.ones(20)]
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    for C in [1, 100, 1e4, 1e6, 1e8]:
        m = LogisticRegression(C=C, solver="lbfgs", max_iter=20000).fit(Xsep, ysep)
        print(f"tau^2 ~ C={C:>8g}:  ||w|| = {np.linalg.norm(np.r_[m.intercept_, m.coef_.ravel()]):.2f}")
```
<details><summary>Reconcile</summary>

$\|\hat\beta\|$ *diverges* — it grows without bound as $C\to\infty$, because on separable data the unpenalized likelihood has no finite maximizer (§15.2). One reading trap: the printed norms appear to plateau near `17.95` at large $C$ — that plateau is lbfgs hitting its stopping tolerance, not a finite optimum. §15.2's second table is the proof: the cross-entropy is still falling (`0.00031` at $\|w\|=16$, `0.00000` only in the limit), so a more patient optimizer would keep climbing. The naive intuition fails: a finite prior variance keeps the fit finite, but the limit $\tau^2\to\infty$ (no prior) is singular, not "just less regularized." This is the exact mechanism behind weight decay in deep nets: on data a network can fit perfectly, the cross-entropy loss keeps rewarding larger logits, so the weights only stop growing because a proper prior (weight decay) tells them to. Turning weight decay to zero on separable data does not give you a slightly-different model; it gives you a divergent one whose apparent coefficients are set by your optimizer's patience.
</details>

**Exercise 15.2 — Does integrating move the decision? (surprising).**
*Setup:* Using the §15.3 posterior ($b\_map$, $\Sigma$), you classify test points by thresholding the predicted probability at 0.5. You compare the plug-in decision $\sigma(x^\top\hat\beta)>0.5$ with the integrated (MacKay-moderated) decision.
*Predict:* Over many test points, on what fraction do the plug-in and integrated classifiers *disagree* about the class at threshold 0.5? Guess a number.
*Reason:* The intuition being tested: "integrating changes the probabilities, so it must move the decision boundary and flip some labels."
*Run:*
```python
gt = np.random.default_rng(31)
Xtest = np.column_stack([np.ones(4000), gt.normal(0, 1.5, 4000), gt.normal(0, 1.5, 4000)])
p_plug = 1 / (1 + np.exp(-Xtest @ b_map))
m = Xtest @ b_map; s2 = np.einsum("ij,jk,ik->i", Xtest, Sigma, Xtest)
p_int = 1 / (1 + np.exp(-m / np.sqrt(1 + np.pi / 8 * s2)))
print("decisions differ on:", np.mean((p_plug > 0.5) != (p_int > 0.5)), "of test points")
print("but mean |p_plug - p_int| =", round(np.abs(p_plug - p_int).mean(), 4))
```
<details><summary>Reconcile</summary>

They disagree on **exactly zero** points. MacKay's moderation divides the logit $m=x^\top\hat\beta$ by a strictly positive number $\sqrt{1+\tfrac\pi8 s^2}$, which cannot change its sign — so $\sigma(\cdot)>0.5 \iff m>0$ for both, and the $p=0.5$ contour is *identical*. Integrating changes every probability (mean shift is nonzero) but never the 0.5-threshold decision. The surprise reorganizes the intuition: probabilities and decisions are different objects (module 06). If your loss is symmetric and your threshold is 0.5, calibration is irrelevant to the decision; the moment the threshold moves off 0.5 — asymmetric costs, the cancer-screening threshold of module 22 — the moderated probability and the plug-in *do* decide differently, and only the integrated one is priced correctly.
</details>

**Exercise 15.3 — Poisson regression with an offset (rates with exposure).**
*Setup:* You model claim counts $y_i$ over exposure windows of differing length $E_i$ (person-years). The true rate is $\mu_i=\exp(\beta_0+\beta_1 x_i)$ per unit exposure, so $y_i\sim\mathrm{Poisson}(E_i\mu_i)$ and $\log\mathbb E[y_i]=\log E_i + \beta_0+\beta_1 x_i$: the $\log E_i$ enters as a fixed **offset** (a coefficient pinned to 1). In your data, longer-exposure units also tend to have larger $x$ ($\log E_i = 0.6\,x_i + \text{noise}$).
*Predict:* If you *ignore* the offset and regress counts on $x$, will the estimated $\hat\beta_1$ be about right, biased high, or biased low, relative to the truth $\beta_1=0.5$?
*Reason:* The intuition to test: "an offset is a minor bookkeeping detail; the slope on $x$ should come out roughly the same."
*Run:*
```python
gp = np.random.default_rng(21); n = 2000
x = gp.normal(0, 1, n); logE = 0.6 * x + gp.normal(0, 0.8, n)
mu = np.exp(0.1 + 0.5 * x); ycount = gp.poisson(np.exp(logE) * mu)
Xp = np.column_stack([np.ones(n), x])
def nll(b, off): eta = Xp @ b + off; return -np.sum(ycount * eta - np.exp(eta))
b_off = minimize(nll, np.zeros(2), args=(logE,),        method="BFGS").x   # correct
b_no  = minimize(nll, np.zeros(2), args=(np.zeros(n),), method="BFGS").x   # ignores exposure
print("true beta1 = 0.5 | with offset:", np.round(b_off, 3), " no offset:", np.round(b_no, 3))
```
<details><summary>Reconcile</summary>

Ignoring the offset biases $\hat\beta_1$ *high*: the with-offset fit recovers a slope near `0.5`, while the no-offset fit inflates it toward `1.1`. Because exposure is correlated with $x$ ($\log E = 0.6x+\varepsilon$), a model with no offset has only one way to explain why high-$x$ units show more events — crank up the $x$ slope — so $\beta_1$ absorbs the exposure effect it was not allowed to name. The offset is not bookkeeping; it is the difference between modeling a *rate* and modeling a *count*. This is the same failure as omitting a confounder from a regression (module 24): a variable that belongs in the linear predictor, left out, reappears inside the coefficient of whatever it correlates with.
</details>

**Exercise 15.4 — How much censoring can the likelihood take? (surprising).**
*Setup:* The survival model of §15.7, same $n=1000$ units and same true lifetimes, but now sweep the study length: $c=4$ (light censoring, ~3%), $c=1$ (the module's ~30%), and $c=0.25$ (brutal: ~70% of units still alive at study end). Fit both estimators at each $c$.
*Predict:* At 70% censoring, only ~300 failures are observed and 700 rows are "incomplete." Commit: does the *correct* censored MLE's slope estimate fall apart too (say, off by more than half), or does it stay near the truth $\beta_1=0.6$? And which way does the drop-censored slope move as censoring grows?
*Reason:* The intuition to test: "with 70% of the outcomes unobserved, no method can estimate well — garbage in, garbage out."
*Run:*
```python
for c_end in [4.0, 1.0, 0.25]:
    obs_c = np.minimum(T, c_end); fail_c = (T <= c_end).astype(float)
    def nll_c(b):
        z = Xs @ b; l_ = np.exp(z)
        return -np.sum(fail_c * (z - l_ * obs_c) + (1 - fail_c) * (-l_ * obs_c))
    bC = minimize(nll_c, np.zeros(2), method="BFGS").x
    kp = fail_c == 1
    def nll_d(b):
        z = Xs[kp] @ b; l_ = np.exp(z)
        return -np.sum(z - l_ * obs_c[kp])
    bD = minimize(nll_d, np.zeros(2), method="BFGS").x
    print(f"c={c_end:<4}: censored {1 - fail_c.mean():.3f}   "
          f"S(c)-MLE {np.round(bC, 4)}   drop {np.round(bD, 4)}")
```
<details><summary>Reconcile</summary>

The correct likelihood barely notices: its slope reads `0.5497` at 3% censoring, `0.554` at 30%, and still `0.5335` at 70% — within noise of the truth 0.6 even when seven in ten lifetimes were never observed to end. The drop-censored fit degrades monotonically and catastrophically: slope `0.447` → `0.1628` → `0.0969`, intercept `0.298` → `0.9727` → `2.1631` (the fitted baseline hazard ends up $e^{2.16}\approx 8.7$, versus the true $e^{0.2}\approx 1.2$). "Garbage in, garbage out" misdiagnoses the input: a censored row is not garbage — $Y>c$ is a genuine, correctly-priced observation whose likelihood contribution $S(c)=e^{-\lambda c}$ pushes the rate *down* exactly as hard as the data warrant. Censoring costs the correct likelihood some efficiency (fewer effective events, wider posterior), never consistency. The bias belongs entirely to the *deletion*, and it grows with the censoring rate because deletion selects ever more aggressively on the outcome. Compression: partial observations are not damaged observations; write the probability of exactly what you saw and the likelihood machinery does the rest.
</details>

## Takeaways

- A **GLM** = an exponential-family response + a linear predictor + a link onto the natural parameter. Bernoulli→logit (logistic), Poisson→log, Normal→identity are the same recipe with different response stories (module 04's table).
- **Cross-entropy training is Bernoulli/categorical GLM maximum likelihood**; MSE is Gaussian GLM ML. Choosing a loss is choosing a response distribution.
- On **linearly separable** data the logistic MLE **diverges** ($\|\hat w\|\to\infty$, loss $\to0$ with no finite minimizer). Any proper Gaussian prior gives a finite MAP — this is the generative meaning of **weight decay**.
- Bayesian logistic regression has **no closed form**; Laplace (MAP + Hessian), from-scratch Metropolis, and NUTS agree — the two exact samplers to Monte Carlo error, Laplace to within its mode-vs-mean skew.
- **Integrate, don't plug:** the honest class probability is $\int\sigma(x^\top\beta)p(\beta\mid\text{data})d\beta$, not $\sigma(x^\top\hat\beta)$. MacKay's $\sigma\!\big(m/\sqrt{1+\tfrac\pi8 s^2}\big)$ gives it in closed form; the plug-in is overconfident, worst at small $n$ and off-support, and it is **miscalibrated** where the integrated predictor is not.
- **Generative vs discriminative** is a race, not a law: naive Bayes reaches its asymptote fast and matches logistic when well-specified; logistic has equal-or-lower asymptotic error and wins under misspecification. The gap shrinks and can reverse — no guaranteed crossover.
- **Survival regression** conditions on exactly what you observed: a survivor contributes $S(c)$, not a density. Dropping censored rows biases the hazard; the $S(c)$ term is the fix, and it generalizes to Weibull and interval censoring.

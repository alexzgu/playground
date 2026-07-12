# 18. Multiplicity, Misspecification, and Large-Scale Inference

> **Spine.** Run a thousand inferences at once and the prior stops being a belief and becomes an *estimate* — shrinkage then does multiplicity control for free; and when your model is wrong the posterior stays sharp about the wrong thing, so you audit its width against the sampling distribution.
> **Which line?** Line 1 (the model is a joint — but now over thousands of parallel unknowns, so the population *is* estimable) and line 4 (a decision — which effects to report — under a loss that must price false discoveries). Plus the honest asterisk on all four: they are exact *given the model*, and here the model is admitted to be wrong.
> **Promise.** After this module you can explain why the top hit in a genome scan is overstated and by how much, control a false-discovery rate two equivalent ways (Benjamini–Hochberg and local-fdr), recover 5 signals out of 100 with a horseshoe, and check whether a posterior interval is too narrow because the model is misspecified.
> **Prereqs.** Modules 16 (hierarchical models, empirical Bayes, partial pooling), 17 (model checking, LOO, the M-open preview), with callbacks to 06 (lasso mode-vs-mean), 08 (BvM conditions and the sandwich line), 12 (the funnel and NumPyro/ArviZ idioms).
> **Runtime.** ~65 s (the horseshoe NUTS fit dominates).
> **Sources.** Efron, *Large-Scale Inference*, by concept; ISLP ch. 13 (multiple testing); Benjamini–Hochberg by concept; booklet ch. 9 (shrinkage) tie.

A drug-screening lab tests 1000 compounds, each once, each measured with noise. It ranks them and writes up the winner. Every step is defensible, and the write-up is still wrong: the reported effect of the top compound is systematically too big, and if the lab published a 95% interval it would miss the truth far more than 5% of the time. Nothing here is fraud. It is what happens when you do inference a thousand times and then *select*. This module is the statistics of that regime — and its twin problem, what your beautifully-calibrated posterior means when the model generating it is false.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "18-scale-and-misspecification"    # this module's figure dir
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

## 18.1 The winner's curse, and shrinkage as automatic multiplicity control

**Setup.** You have $N=1000$ candidate effects. Each true effect $\theta_i$ is itself drawn from a population $\theta_i \sim N(0, A)$ with $A=1$ — so most effects are small (68% of them within one unit of zero), a handful genuinely large. You measure each once with unit noise, $X_i \mid \theta_i \sim N(\theta_i, 1)$. You will rank the compounds by their measurement, report the top one, and write down its effect size $X_{(1)}$.

**Predict.** The top-scoring measurement comes in at about $X=5.3$. Commit to a number: *how big is that compound's true effect $\theta$?* The naive answer — the one the write-up uses — is "about 5.3; that's what we measured." Now commit to a second number: across the **top 10** compounds, by how much does the average measurement overstate the average true effect? The reflex says *zero — selection just picks the biggest, it doesn't inflate anything.*

**Run.** Fit the population $N(0,A)$ from the 1000 measurements themselves — this is empirical Bayes at $J=1000$ groups — and shrink every measurement toward zero by the master formula from module 05, $\widehat\theta_i = \frac{A}{A+1}X_i$, with $A$ estimated from the marginal variance $\operatorname{Var}(X)=A+1$.

```python
# Winner's curse: 1000 effects, most near-null; select the top, compare truth/raw/shrunk.
gw = np.random.default_rng(SEED)
N = 1000
theta = gw.normal(0.0, 1.0, N)                 # true effects ~ N(0, A) with A = 1
X = gw.normal(theta, 1.0)                       # one noisy measurement each

A_hat = max(np.mean(X**2) - 1.0, 0.0)           # marginal Var(X) = A + 1  ->  estimate A
shrink = A_hat / (A_hat + 1.0)                  # module-05 precision weight, EB at J=1000
X_shrunk = shrink * X
print(f"A_hat = {A_hat:.3f}   shrinkage weight A/(A+1) = {shrink:.3f}")

top = np.argmax(X)
sel = np.argsort(-X)[:10]                        # the 10 top-scoring effects
print(f"TOP hit:      raw X = {X[top]:.2f}   true theta = {theta[top]:.2f}   shrunk = {X_shrunk[top]:.2f}")
print(f"top-10 means: raw = {X[sel].mean():.3f}   true = {theta[sel].mean():.3f}   shrunk = {X_shrunk[sel].mean():.3f}")
print(f"selection inflation:  raw - true = {X[sel].mean() - theta[sel].mean():.3f}   "
      f"shrunk - true = {X_shrunk[sel].mean() - theta[sel].mean():.3f}")

rmse = lambda est: np.sqrt(np.mean((est - theta)**2))
rmse_sel = lambda est: np.sqrt(np.mean((est[sel] - theta[sel])**2))
print(f"RMSE over all 1000:   raw = {rmse(X):.3f}   shrunk = {rmse(X_shrunk):.3f}")
print(f"RMSE over the top 10: raw = {rmse_sel(X):.3f}   shrunk = {rmse_sel(X_shrunk):.3f}")
```

**Reconcile.** The top hit measured `5.29`, but its true effect is `2.55` — the measurement overstates reality by a factor of two. Shrinkage pulls it back to `2.80`, within a whisker of the truth. Across the top 10 the effect is systematic: the raw measurements average `3.772` while the true effects average `1.987`, a **selection inflation of `1.785`** that the naive "zero" prediction missed entirely. Shrinkage removes essentially all of it — the shrunk average `1.993` sits `0.006` from the truth. On the selected set, RMSE falls from `1.918` (raw) to `0.523` (shrunk); over all 1000 effects it falls from `1.028` to `0.689`.

The mechanism is regression to the mean, and it is *forced by selection*: a measurement lands in the top 10 partly because $\theta_i$ is large and partly because the noise broke upward, and you cannot select on the sum without selecting on the noise. The reason the fix needs no special "multiplicity correction" is the punchline of the module's first line: with 1000 parallel problems the shrinkage target and strength are read off the *data* (that is what $\widehat A$ is), so the estimator that de-biases selection is just the empirical-Bayes posterior mean of module 16, evaluated at scale. **Shrinkage is multiplicity control that happens automatically** — you get it for free the moment you model the effects as exchangeable draws from a common population.

```python
# Figure: raw estimates inflate off the diagonal; shrunk estimates hug the truth.
fig, ax = plt.subplots(figsize=(6.4, 5))
ax.axline((0, 0), slope=1, color="k", ls="--", lw=1, label="perfect (est = truth)")
ax.scatter(theta, X, s=8, color="C7", alpha=0.35, label="raw measurement $X_i$")
ax.scatter(theta, X_shrunk, s=8, color="C1", alpha=0.5, label="shrunk $\\hat\\theta_i$")
ax.scatter(theta[sel], X[sel], s=55, facecolors="none", edgecolors="C3",
           lw=1.6, zorder=5, label="top-10 selected (raw)")
ax.set_xlabel("true effect  $\\theta_i$"); ax.set_ylabel("estimate")
ax.set_title("Winner's curse: selection lifts raw estimates above the diagonal")
ax.legend(fontsize=8, loc="upper left")
save(fig, "winners-curse")
```

![Scatter of estimate versus true effect: gray raw measurements fan around the y=x line but the top-10 selected (red rings) sit visibly above it; orange shrunk estimates form a tighter cloud pulled toward a shallower slope through the origin.](figures/18-scale-and-misspecification/winners-curse.png)

One honest caveat, cashed in §18.4. A *uniform* Gaussian shrinkage is exactly right here because the effects really are Gaussian. When the truth is **sparse** — most effects exactly zero, a few large — one global shrinkage factor cannot both crush the nulls and spare the signals, and it will over-shrink the genuine large effects. That is the case for a different tool: local, per-coefficient shrinkage.

## 18.2 Two groups: Benjamini–Hochberg is a Bayesian local false-discovery rate

Selection also demands a decision — *which* effects to declare real — and that is line 4 with a loss that prices false positives. The **two-groups model** (Efron) is the joint: each of $N$ z-scores is null with probability $\pi_0$ or non-null otherwise,
$$f(z) = \pi_0\, f_0(z) + (1-\pi_0)\, f_1(z), \qquad f_0 = N(0,1).$$
The **local false-discovery rate** is the posterior probability that a case at $z$ is null — line 2, applied to the mixture:
$$\mathrm{fdr}(z) = P(\text{null} \mid z) = \frac{\pi_0 f_0(z)}{f(z)}.$$
You do not need to know $f_1$: estimate the whole marginal $f(z)$ from the observed z-scores (Efron's move — with thousands of them the histogram *is* the mixture density), and divide the known null piece by it. Compare that to **Benjamini–Hochberg (BH)**, the standard frequentist FDR procedure on the two-sided p-values, at a matched target rate $q=0.1$.

```python
# Two-groups model: BH on p-values vs Bayesian local-fdr from an estimated mixture density.
gz = np.random.default_rng(1)
N, pi0 = 5000, 0.90
is_null = gz.random(N) < pi0
theta2 = np.where(is_null, 0.0, gz.normal(0.0, 2.5, N))   # non-nulls ~ N(0, 2.5^2)
z = gz.normal(theta2, 1.0)
q = 0.10

# Benjamini-Hochberg on two-sided p-values.
p = 2 * (1 - stats.norm.cdf(np.abs(z)))
ps = np.sort(p)
below = np.where(ps <= q * np.arange(1, N + 1) / N)[0]
p_cut = ps[below.max()] if below.size else 0.0
bh = p <= p_cut
print(f"BH        (q={q}): discoveries = {bh.sum():3d}   true non-null = {(bh & ~is_null).sum():3d}"
      f"   false-discovery proportion = {(bh & is_null).sum() / max(bh.sum(), 1):.3f}")

# Local-fdr: estimate f(z) by KDE, divide the known null pi0*f0 by it, control Bayesian FDR.
f_hat = stats.gaussian_kde(z, bw_method=0.15)(z)
lfdr = np.minimum(pi0 * stats.norm.pdf(z) / f_hat, 1.0)
order = np.argsort(lfdr)
cum_fdr = np.cumsum(lfdr[order]) / np.arange(1, N + 1)   # running Bayesian FDR of the set
n_disc = int((cum_fdr <= q).sum())
lf = np.zeros(N, bool); lf[order[:n_disc]] = True
print(f"local-fdr  (q={q}): discoveries = {lf.sum():3d}   true non-null = {(lf & ~is_null).sum():3d}"
      f"   false-discovery proportion = {(lf & is_null).sum() / max(lf.sum(), 1):.3f}")

# local-fdr(z) IS an estimate of the exact posterior P(null | z) under the true mixture.
for zt in (2.5, 3.0, 4.0):
    est = min(pi0 * stats.norm.pdf(zt) / stats.gaussian_kde(z, bw_method=0.15)(np.array([zt]))[0], 1.0)
    f_true = pi0 * stats.norm.pdf(zt) + (1 - pi0) * stats.norm.pdf(zt, 0, np.sqrt(1 + 2.5**2))
    exact = pi0 * stats.norm.pdf(zt) / f_true
    print(f"  z={zt}:  estimated local-fdr = {est:.3f}   exact P(null|z) = {exact:.3f}")
```

BH makes `171` discoveries at a realized false-discovery proportion of `0.111`; local-fdr makes `181` at `0.122` — the two procedures, one built from tail p-values and one from a posterior probability, land in the same place and control the same rate. And the estimated local-fdr tracks the exact posterior $P(\text{null}\mid z)$: `0.644` vs `0.621` at $z=2.5$, `0.306` vs `0.334` at $z=3$, `0.032` vs `0.024` at $z=4$. That is the reading to keep: **BH is controlling an average posterior null-probability over the rejected set.** The frequentist FDR and the Bayesian fdr are the same quantity approached from two directions — a tail area versus a density ratio — and the Bayesian version tells you something BH cannot, the probability that *this specific* case at $z$ is a false alarm.

```python
# Figure: the two-groups mixture, its null component, and the local-fdr curve.
fig, ax = plt.subplots()
grid = np.linspace(-6, 6, 400)
ax.hist(z, bins=80, density=True, color="C7", alpha=0.5, label="observed z-scores")
ax.plot(grid, stats.norm.pdf(grid) * pi0, "C0", lw=2, label="null part  $\\pi_0 f_0$")
ax.plot(grid, stats.gaussian_kde(z, bw_method=0.15)(grid), "C1", lw=2, label="estimated $f(z)$")
ax2 = ax.twinx()
ax2.plot(grid, np.minimum(pi0 * stats.norm.pdf(grid) /
         stats.gaussian_kde(z, bw_method=0.15)(grid), 1.0), "C3", lw=2, ls="--")
ax2.set_ylabel("local-fdr(z) = P(null | z)", color="C3"); ax2.set_ylim(0, 1.05); ax2.grid(False)
ax.set_xlabel("z-score"); ax.set_ylabel("density"); ax.set_title("Two-groups model: where the nulls stop and discoveries begin")
ax.legend(fontsize=8, loc="upper left")
save(fig, "two-groups")
```

![Histogram of z-scores overlaid with the scaled null bell and the wider estimated marginal; a dashed red local-fdr curve sits near 1 in the center and drops toward 0 in both tails, crossing 0.2 around |z|=3.](figures/18-scale-and-misspecification/two-groups.png)

## 18.3 Empirical Bayes at scale: the prior stops being subjective

Module 16 flagged a real cost of empirical Bayes: plugging a point estimate $\widehat\tau$ into the prior and proceeding as if it were known produces intervals that are **too narrow**, because they ignore the uncertainty in $\widehat\tau$ — overconfident at $J=8$ schools. Efron's insight is that this caveat is a *small-$J$* phenomenon and it evaporates as the number of parallel problems grows. With $J$ in the thousands, the prior is pinned down so tightly by the data that plugging it in costs almost nothing: **at scale, the prior is not a subjective object — it is an estimate with a standard error going to zero.**

Watch the empirical-Bayes interval width converge to the full-Bayes width (which marginalizes the hyperparameter $A$ honestly) as $J$ grows.

```python
# EB plug-in vs full-Bayes interval width for theta_1, as the number of parallel problems J grows.
def eb_vs_full_bayes(J, A_true=2.0, seed=1):
    g = np.random.default_rng(seed)
    th = g.normal(0.0, np.sqrt(A_true), J)
    x = g.normal(th, 1.0)
    # EB: point-estimate A, plug in -> posterior sd of theta_1 is sqrt(shrink) with A fixed.
    A_hat = max(np.mean(x**2) - 1.0, 1e-6)
    eb_sd = np.sqrt(A_hat / (A_hat + 1.0))
    # Full Bayes: marginalize A over a grid (flat prior), mixing posteriors N(shrink(A) x1, shrink(A)).
    Agrid = np.linspace(1e-3, 20, 4000)
    loglik = np.array([stats.norm.logpdf(x, 0, np.sqrt(a + 1)).sum() for a in Agrid])
    w = np.exp(loglik - loglik.max()); w /= w.sum()
    shA = Agrid / (Agrid + 1.0)
    mean_c, var_c = shA * x[0], shA
    post_mean = (w * mean_c).sum()
    fb_sd = np.sqrt((w * (var_c + mean_c**2)).sum() - post_mean**2)
    return eb_sd, fb_sd

print("   J   |  EB sd  | full-Bayes sd | ratio EB/FB")
for J in (10, 50, 1000):
    e, f = eb_vs_full_bayes(J)
    print(f"  {J:4d} |  {e:.4f} |    {f:.4f}    |   {e/f:.4f}")
```

At $J=10$ the EB interval is a disastrous `0.2778` of the honest width — it ignores that $A$ is barely known from ten problems, exactly module 16's overconfidence warning. By $J=50$ the ratio is `0.9783`, and by $J=1000$ it is `0.9995`: the plug-in and the fully-marginalized intervals are indistinguishable. This is why "large-scale inference" and "empirical Bayes" are the same subject. The philosophical objection to empirical Bayes — *you used the data twice, once to build the prior and once to use it* — has real teeth at $J=8$ and essentially none at $J=1000$, because the first use consumes a vanishing fraction of the information. The prior became a measurement.

## 18.4 Sparsity as multiplicity control: the horseshoe

Now the sparse regime §18.1 warned about: $n=100$ observations, $p=100$ candidate predictors, but only **5 have nonzero coefficients**. Uniform shrinkage (ridge) cannot win — it shrinks the 5 real signals as hard as the 95 nulls. The lasso zeros coefficients but, tuned to catch the signals, floods the model with false positives. What you want is *global-local* shrinkage: a global scale $\tau$ that pulls everything toward zero, and a per-coefficient local scale $\lambda_j$ with heavy (half-Cauchy) tails that lets a genuine signal escape. That is the **horseshoe** prior,
$$\beta_j \mid \lambda_j, \tau \sim N(0,\ \tau^2\lambda_j^2), \qquad \lambda_j \sim \mathrm{Half\text{-}Cauchy}(1), \qquad \tau \sim \mathrm{Half\text{-}Cauchy}(1).$$

**Predict.** Three fits — horseshoe, ridge ($\alpha=10$), lasso (CV-tuned) — on the same data. Commit to a ranking of their coefficient RMSE, and predict: how many of the 95 true zeros does each leave *materially* nonzero? The naive read is "lasso does sparsity, so lasso wins." Fit with NUTS, sizes kept modest so the run stays inside budget.

```python
# Horseshoe recovery of 5-of-100 signals via NUTS (NumPyro), following tools/ppl_idioms.py.
import jax
import jax.numpy as jnp
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS

gh = np.random.default_rng(SEED)
n, p = 100, 100
Xd = gh.standard_normal((n, p))
beta_true = np.zeros(p)
signal_idx = np.array([7, 20, 45, 66, 88])
beta_true[signal_idx] = np.array([3.0, -2.5, 2.0, -1.5, 2.8])
yd = Xd @ beta_true + gh.normal(0.0, 1.0, n)
null_idx = np.setdiff1d(np.arange(p), signal_idx)

def horseshoe(X, y=None):
    n_, p_ = X.shape
    tau = numpyro.sample("tau", dist.HalfCauchy(1.0))                 # global scale
    with numpyro.plate("p", p_):
        lam = numpyro.sample("lam", dist.HalfCauchy(1.0))            # local scales (heavy tails)
        z = numpyro.sample("z", dist.Normal(0.0, 1.0))              # non-centered: beta = z*lam*tau
    beta = numpyro.deterministic("beta", z * lam * tau)
    sigma = numpyro.sample("sigma", dist.HalfNormal(2.0))
    with numpyro.plate("n", n_):
        numpyro.sample("y", dist.Normal(jnp.dot(X, beta), sigma), obs=y)

mcmc = MCMC(NUTS(horseshoe, target_accept_prob=0.95), num_warmup=800, num_samples=800,
            num_chains=2, chain_method="sequential", progress_bar=False)
mcmc.run(jax.random.PRNGKey(SEED), X=np.asarray(Xd), y=np.asarray(yd),
         extra_fields=("diverging",))
n_div = int(mcmc.get_extra_fields()["diverging"].sum())
beta_hs = np.asarray(mcmc.get_samples()["beta"]).mean(0)
rmse_b = lambda b: np.sqrt(np.mean((b - beta_true)**2))
print(f"horseshoe: {n_div} divergences; coefficient RMSE = {rmse_b(beta_hs):.3f}; "
      f"max |beta| over the 95 nulls = {np.abs(beta_hs[null_idx]).max():.3f}")
print("  signals true -> horseshoe:", [f"{beta_true[i]:+.1f}->{beta_hs[i]:+.2f}" for i in signal_idx])
```

```python
# The frequentist foils: ridge (no zeros) and CV-lasso (zeros, but false positives).
from sklearn.linear_model import Ridge, LassoCV
ridge = Ridge(alpha=10.0).fit(Xd, yd)
lasso = LassoCV(cv=5, random_state=0).fit(Xd, yd)
print(f"ridge  : RMSE = {rmse_b(ridge.coef_):.3f}; nonzero coefs = {(np.abs(ridge.coef_) > 1e-6).sum()}; "
      f"max |beta| over nulls = {np.abs(ridge.coef_[null_idx]).max():.3f}")
print(f"lasso  : RMSE = {rmse_b(lasso.coef_):.3f}; nonzero coefs = {(np.abs(lasso.coef_) > 1e-8).sum()}; "
      f"false positives among the 95 nulls = {(np.abs(lasso.coef_[null_idx]) > 1e-8).sum()}")

# Global-local shrinkage weight kappa_j = 1/(1 + (tau*lam_j)^2): 1 = fully shrunk, 0 = untouched.
lam = np.asarray(mcmc.get_samples()["lam"]); tau = np.asarray(mcmc.get_samples()["tau"])[:, None]
kappa = (1.0 / (1.0 + (tau * lam)**2)).mean(0)
print(f"shrinkage kappa: nulls median = {np.median(kappa[null_idx]):.3f}   "
      f"signals = {np.round(kappa[signal_idx], 2)}")
```

**Reconcile.** The horseshoe recovers the five signals almost exactly and posts a coefficient RMSE of `0.033`, crushing lasso's `0.061` and ridge's `0.267` — and the naive "lasso wins on sparsity" ranking is wrong. Ridge keeps all `100` coefficients nonzero (its largest spurious coefficient is `0.534`), because a Gaussian prior has no mechanism to produce a zero. The CV-lasso, tuned to recover all five signals, pays for it with `35` false positives — it keeps `40` coefficients, seven-eighths of them noise. The horseshoe leaves the 95 nulls with a maximum magnitude of `0.130` and reproduces the signals to two digits. The shrinkage weights show why: the median null is shrunk at $\kappa=$ `0.993` (pinned to zero) while the signals sit at $\kappa$-values around 0.16–0.41 (barely touched). That bimodal split — mass at 0 and mass at 1, the shape that named the prior — is global-local shrinkage doing multiplicity control by geometry.

The 43 divergences are not incidental: the horseshoe's global-local structure is a funnel (module 12), where $\tau$ near zero collapses the geometry of every $z_j$ at once. The non-centered parameterization $\beta = z\lambda\tau$ and a high `target_accept_prob=0.95` tame most of it; a production fit would use a regularized horseshoe to finish the job.

```python
# Figure: global-local shrinkage separates the two populations of coefficients.
fig, ax = plt.subplots()
ax.scatter(null_idx, kappa[null_idx], s=14, color="C7", alpha=0.6, label="95 true nulls")
ax.scatter(signal_idx, kappa[signal_idx], s=90, color="C3", marker="*",
           zorder=5, label="5 true signals")
ax.axhline(0.5, color="k", ls=":", lw=1)
ax.set_xlabel("coefficient index $j$"); ax.set_ylabel("shrinkage weight  $\\kappa_j$")
ax.set_title("Horseshoe: nulls pinned near $\\kappa=1$, signals spared near $\\kappa=0$")
ax.legend(fontsize=9)
save(fig, "horseshoe-shrinkage")
```

![Shrinkage weight per coefficient: gray nulls cluster tightly just below kappa=1 while five red stars sit near the bottom between 0.15 and 0.45, cleanly separated by the dotted midline.](figures/18-scale-and-misspecification/horseshoe-shrinkage.png)

## 18.5 M-open: the posterior is exactly right about a wrong model

Everything so far assumed the model was true. Now drop that. A **Normal linear model** is a model for a conditional mean, $E[y\mid x]=x^\top\beta$ with homoskedastic Gaussian noise. Fit it to a truth that is **skewed and heteroskedastic** — the noise variance grows with $|x|$ and the errors are right-skewed — and ask the frequentist audit question of module 08: does the posterior interval for the slope cover at its stated rate?

**Predict.** The posterior standard deviation of the slope comes from the model's likelihood curvature (its Fisher information). The **sandwich** standard error (Huber–White) estimates the *actual* sampling variability of $\widehat\beta$ without trusting the noise model. Commit: will the posterior sd be about right, too big, or too small — and which one matches the true sampling standard deviation you would see by refitting on fresh data?

```python
# M-open: fit a homoskedastic Normal model to skewed, heteroskedastic truth; audit the slope's sd.
def make_data(g):
    n = 200
    x = g.uniform(-2, 2, n)
    Xd = np.column_stack([np.ones(n), x])
    sd = 0.5 + 0.8 * np.abs(x)                     # heteroskedastic: noise grows with |x|
    eps = sd * (g.standard_exponential(n) - 1.0)   # skewed (mean-zero) errors
    y = Xd @ np.array([0.0, 1.0]) + eps            # true slope = 1
    return Xd, y

Xd, yv = make_data(np.random.default_rng(2))
XtXi = np.linalg.inv(Xd.T @ Xd)
bhat = XtXi @ Xd.T @ yv
resid = yv - Xd @ bhat
n, k = len(yv), 2
s2 = (resid**2).sum() / (n - k)                    # homoskedastic variance estimate

# Bayesian posterior sd of the slope (flat NIG prior -> Student-t, df = n-k).
df = n - k
post_sd = np.sqrt(s2 * XtXi[1, 1] * df / (df - 2))
# Sandwich (HC0): robust to the wrong noise model.
meat = Xd.T @ (Xd * (resid**2)[:, None])
sand_sd = np.sqrt((XtXi @ meat @ XtXi)[1, 1])
# The ground truth: refit on many fresh datasets and measure the slope's spread.
gs = np.random.default_rng(999)
slopes = np.array([np.linalg.solve(A.T @ A, A.T @ b)[1]
                   for A, b in (make_data(gs) for _ in range(5000))])
print(f"slope estimate           = {bhat[1]:.4f}   (true = 1.0)")
print(f"posterior sd (the model) = {post_sd:.4f}")
print(f"sandwich SE  (robust)    = {sand_sd:.4f}")
print(f"true sampling sd  [sim]  = {slopes.std():.4f}")
print(f"residual skew = {stats.skew(resid):.2f}   ->  the Normal model is wrong")
```

**Reconcile.** The posterior standard deviation is `0.0740`; the sandwich SE is `0.1019`; the true sampling standard deviation, measured by brute force, is `0.1046`. The posterior is **too narrow by a third**, and the sandwich nails the truth. Nothing is broken in the Bayesian machine: given the homoskedastic Normal model, `0.0740` is the *exactly correct* posterior sd — the model just happens to be false, and a false model can be perfectly confident about the wrong sampling variance. This is module 08's misspecification line cashed: BvM guarantees credible = confidence *only when the model is well-specified*, and heteroskedasticity (residual skew `2.44` here confirms the Normal is wrong) breaks condition 1. The sandwich is the audit — it replaces the model's assumed noise curvature with the empirical one, so it stays honest about $\operatorname{Var}(\widehat\beta)$ whatever the truth.

Two honest boundaries. For a *pure mean* (no covariate), the sandwich and the model sd coincide — misspecification of a symmetric noise shape does not bias the variance of a plain average (module 08's exercise 08.3). The gap opens for a *functional* like a slope, where the model's homoskedastic weighting is provably not what the heteroskedastic truth delivers. And the sandwich fixes *only* the width; a badly misspecified mean structure is a different disease, caught by the posterior predictive checks of module 17.

## 18.6 Power posteriors: widening honestly, and the M-open vocabulary

If misspecification makes the posterior too sharp, one blunt repair is to tell it to trust the likelihood *less*. The **power (tempered) posterior** raises the likelihood to a power $\eta \in (0,1)$,
$$p_\eta(\theta \mid y) \ \propto\ p(y\mid\theta)^{\eta}\,\pi(\theta),$$
which for a Gaussian likelihood scales the data precision by $\eta$ and so multiplies the posterior variance by $1/\eta$ — the interval widens, honestly, without pretending to information it does not have. Here it is analytically in a Normal–Normal model, and then used to *recalibrate* the misspecified slope of §18.5 to its sandwich width.

```python
# Power posterior: eta < 1 widens the posterior (Gaussian precision scales by eta).
n_obs, tau2, ybar = 20, 100.0, 0.5
print("tempered Normal-Normal posterior sd:")
for eta in (1.0, 0.5, 0.25):
    post_var = 1.0 / (eta * n_obs / 1.0 + 1.0 / tau2)
    print(f"  eta = {eta:>4}:  posterior sd = {np.sqrt(post_var):.4f}")

# Recalibration: the eta that inflates the misspecified posterior sd to the sandwich SE.
eta_star = (post_sd / sand_sd)**2
print(f"recalibrating slope: eta* = (post_sd/sandwich)^2 = {eta_star:.3f}  "
      f"-> tempered sd = {post_sd / np.sqrt(eta_star):.4f} matches sandwich {sand_sd:.4f}")
```

At full strength ($\eta=1$) the Normal–Normal posterior sd is `0.2236`; tempering to $\eta=0.5$ widens it to `0.3162`, and to $\eta=0.25$ to `0.4472` — the $1/\sqrt\eta$ law. For the misspecified regression, the power $\eta^\star=$ `0.527` inflates the posterior sd from `0.0740` back up to the sandwich's `0.1019`: a power posterior is a one-knob way to buy back the calibration that misspecification stole. (Choosing $\eta$ principledly — SafeBayes, matching the sandwich, or held-out predictive loss — is active research; label this **heuristic**, a repair with a tuning parameter, not a theorem.) The same $\eta$ knob is the temperature of module 03's softmax and the tempering ladder that Sequential Monte Carlo (modules 19, 21) walks from prior to posterior; **temperature, annealing, and power posteriors are one idea** — reweighting how sharply a density concentrates.

A cheaper robustness reflex worth naming: **bagging**. Refit on bootstrap resamples and average; the averaging damps the influence of any single leverage point or outlier, a frequentist cousin of the Bayesian bootstrap (module 08) and a pragmatic hedge when you distrust the model's tails. It buys robustness, not calibration — treat it as a **heuristic** stabilizer, not an inference.

> **The M-open vocabulary box (all models are wrong, made technical).**
> - **M-closed** — the true data-generating process is one of the models you are considering. Bayesian model averaging is coherent; the posterior over models concentrates on the truth. This is the world of modules 00–17.
> - **M-complete** — a true process exists and you *could* in principle write it down, but you choose to work with simpler surrogate models for tractability. You compare models by predictive performance (LOO, module 17), not by belief that one is true.
> - **M-open** — you cannot or will not specify the true process; no model on the table is correct. This module lives here. The right targets are predictive (elpd) and the right audits are frequentist (sandwich, coverage). "The posterior is exactly right about a wrong model" is the M-open condition stated precisely: internal coherence is intact, external calibration is not, and only an out-of-model audit detects the gap.

## Bridge — Efron's large-scale inference and the empirical-Bayes regime

Efron's *Large-Scale Inference* is the observation that thousands of parallel z-tests turn the prior into an estimable object and make empirical Bayes not a compromise but the *natural* mode of inference. Read through the four lines: the two-groups model (§18.2) is a mixture joint (line 1); local-fdr is conditioning that mixture on $z$ (line 2); the FDR decision is line 4 with a false-discovery loss. The frequentist multiplicity apparatus — Bonferroni, Benjamini–Hochberg — turns out to be Bayesian shrinkage and posterior null-probabilities viewed from the sampling side, exactly the module-08 pattern (a frequentist crown jewel is a Bayesian move). And the misspecification half (§18.5) is where the bridge finally *breaks*: BvM's promise that credible = confidence is void in M-open, so the two ledgers diverge and you must run both.

## Pitfalls

- **Reporting a selected effect at face value.** The top hit of a large scan is inflated by selection every time; publish the raw estimate and you publish an overstatement (`1.785` units in §18.1). Shrink toward the fitted population, or report the shrunk estimate alongside the raw one.
- **Using uniform (ridge/Normal-Normal) shrinkage on a sparse problem.** One global factor cannot both crush nulls and spare signals; it over-shrinks the real effects. Sparsity needs local shrinkage (horseshoe) or explicit selection.
- **Calling the horseshoe posterior mean "sparse."** Like the lasso (module 06), sparsity is a property of a *mode*, not of the posterior mean — the horseshoe's posterior means are small but not exactly zero (max null `0.130`, not 0). If you need exact zeros, threshold deliberately; do not expect the mean to hand them to you.
- **Quoting a posterior sd from a misspecified model as if it were calibrated.** Under heteroskedasticity, dependence, or a wrong likelihood shape, the posterior interval can be far too narrow (`0.0740` vs a true `0.1046`). Audit with the sandwich or with held-out coverage before trusting the width.
- **Treating empirical Bayes as always-safe or always-dubious.** It is overconfident at small $J$ (module 16's $J=8$) and essentially exact at large $J$ (§18.3's ratio `0.9995` at $J=1000$). Which regime you are in is the whole question.

## Exercises

**Exercise 18.1 — How much does the winner's curse depend on how hard you select?**  *(surprising)*
*Setup:* The §18.1 setup ($N=1000$, $\theta_i\sim N(0,1)$, $X_i\sim N(\theta_i,1)$). You select the top-$m$ effects by measurement and look at the raw selection bias $\overline{X}_{\text{sel}}-\overline{\theta}_{\text{sel}}$.
*Predict:* Which is more inflated — the single top hit ($m=1$), or the top 100 ($m=100$)? Commit to a direction before running.
*Reason:* "Averaging many selected effects should wash out the noise, so more selection means more inflation in total but similar bias per effect" — treating selection bias as roughly constant across the selected set.
*Run:*
```python
ge = np.random.default_rng(SEED)
th = ge.normal(0, 1, 1000); xx = ge.normal(th, 1)
for m in (1, 10, 100):
    s = np.argsort(-xx)[:m]
    print(f"top-{m:3d}: raw-true bias = {xx[s].mean() - th[s].mean():.3f}")
```
<details><summary>Reconcile</summary>

The single top hit is the *most* inflated (bias around `1.9`), and the bias *shrinks* as you select more loosely: top-10 near `1.6`, top-100 near `1.0`. The naive "constant per-effect bias" is wrong. The reason is that the bias is driven by the selection threshold: to make the top-1 cut a measurement needs an extreme upward noise excursion, so the conditional expected noise given selection is large; loosen the cut to the top 100 and you admit effects that barely crossed, whose expected noise boost is milder. Selection bias is *strongest at the tip*. This is why the single most-significant result in any large screen is the least trustworthy at face value — the exact opposite of the intuition that the top hit is the "surest" finding.
</details>

**Exercise 18.2 — Bonferroni versus BH discoveries.**
*Setup:* The §18.2 z-scores. Bonferroni controls the family-wise error rate by rejecting only when $p < \alpha/N$; BH controls the false-discovery rate at $q$.
*Predict:* At $\alpha=q=0.1$ and $N=5000$, will Bonferroni make roughly as many discoveries as BH's `171`, or dramatically fewer?
*Reason:* "Both are multiple-testing corrections at level 0.1, so they should be comparable" — conflating FWER control with FDR control.
*Run:*
```python
gb = np.random.default_rng(1)
isn = gb.random(5000) < 0.90
th = np.where(isn, 0.0, gb.normal(0, 2.5, 5000)); zz = gb.normal(th, 1)
pp = 2 * (1 - stats.norm.cdf(np.abs(zz)))
print(f"Bonferroni (p < 0.1/N): discoveries = {(pp < 0.1 / 5000).sum()}")
print(f"BH already made: 171")
```
<details><summary>Reconcile</summary>

Bonferroni makes far fewer discoveries (on the order of 30–50 versus BH's `171`). Bonferroni controls the probability of *even one* false positive across all 5000 tests — a much stricter demand than controlling the *fraction* of false positives among discoveries. When you are willing to tolerate a small proportion of false alarms (FDR), you can afford to reject much closer to the null, which is exactly the regime where large-scale science operates: you are not trying to guarantee zero errors, you are trying to keep the discovery list mostly true. FDR is the loss function that fits the problem; FWER is answering a stricter question nobody asked.
</details>

**Exercise 18.3 — Temperature as the ML knob you already turn.**  *(ML/DL bridge)*
*Setup:* A power posterior raises the likelihood to $\eta$; a softmax with temperature $T$ divides logits by $T$ before normalizing (module 03). Both reshape how sharply a distribution concentrates.
*Predict:* To make a posterior *wider* you take $\eta<1$. To make a softmax *more uniform* (higher entropy), do you take $T>1$ or $T<1$? And which direction corresponds to $\eta<1$?
*Reason:* "Higher temperature means sharper" — the thermodynamic metaphor run backwards.
*Run:*
```python
logits = np.array([2.0, 1.0, 0.1])
for T in (0.5, 1.0, 2.0):
    q = np.exp(logits / T); q /= q.sum()
    ent = -(q * np.log(q)).sum()
    print(f"T={T}: softmax = {np.round(q, 3)}  entropy = {ent:.3f}")
```
<details><summary>Reconcile</summary>

Higher $T$ makes the softmax *more uniform* — entropy rises from `0.606` nats at $T=0.5$ to `0.933` at $T=2.0$ — because dividing logits by a large $T$ compresses their differences. That is the same move as $\eta<1$ on a posterior: $\eta<1$ flattens the likelihood's contribution just as $T>1$ flattens the logits (with the correspondence $\eta \leftrightarrow 1/T$ for an exponential-family likelihood). Both are single knobs on concentration. You have been tempering distributions every time you set a sampling temperature in a language model, a distillation temperature when training a student network, or an exploration temperature in a policy — the power posterior is the same operation wearing its inference-theory name, and §18.6's honest-widening use and the SMC ladder (modules 19, 21) are its statistical siblings.
</details>

**Exercise 18.4 — Does the horseshoe give you exact zeros?**  *(surprising)*
*Setup:* You fit the §18.4 horseshoe and want a sparse coefficient vector — a clean list of "in" and "out" predictors.
*Predict:* Are any of the 95 null coefficients' posterior means *exactly* zero, the way the lasso's are? Commit yes or no.
*Reason:* "The horseshoe is a sparsity prior, so it must produce sparse (exact-zero) estimates" — expecting the posterior mean to inherit a property of a mode.
*Run:*
```python
n_exact_zero = int((beta_hs[null_idx] == 0.0).sum())
print(f"null coefs with posterior mean exactly 0: {n_exact_zero} of 95")
print(f"smallest |posterior mean| among nulls: {np.abs(beta_hs[null_idx]).min():.5f}")
```
<details><summary>Reconcile</summary>

Zero of them are exactly zero — the smallest null coefficient is tiny but nonzero. The horseshoe is a *continuous* shrinkage prior: its posterior means are pulled extremely close to zero (that is what $\kappa\approx1$ meant), but a smooth prior integrated into a posterior mean can never produce an exact zero, precisely the module-06 lesson that sparsity is a property of the mode, not the mean. The lasso zeros coefficients because its $\ell_1$ mode sits on a corner; the horseshoe has no corner. If you want a hard in/out list you threshold the shrinkage weight $\kappa$ (say $\kappa<0.5$) or the posterior probability of the coefficient exceeding a region of practical equivalence — a *deliberate* decision (line 4), not something the estimator hands you for free. Genuinely sparse Bayes needs a spike-and-slab prior with an actual point mass at zero; the horseshoe buys you the shrinkage benefits without the discontinuity.
</details>

## Takeaways

- **Selection inflates.** The top hit of $N$ parallel measurements is biased upward (`1.785` on the top 10 here); the single most-significant result is the *most* inflated. Report shrunk estimates, not raw ones.
- **Shrinkage is automatic multiplicity control.** Modeling effects as exchangeable draws from an estimated population (empirical Bayes at scale) de-biases selection with no separate correction — RMSE on the selected set fell from `1.918` to `0.523`.
- **BH is a Bayesian local-fdr.** $\mathrm{fdr}(z)=\pi_0 f_0(z)/f(z)=P(\text{null}\mid z)$; Benjamini–Hochberg and local-fdr make matched discoveries (`171` vs `181` at $q=0.1$) and control the same posterior null-probability.
- **Empirical Bayes' caveat is a small-$J$ artifact.** Plug-in intervals are far too narrow at $J=10$ (ratio `0.2778`) and essentially exact at $J=1000$ (`0.9995`); at scale the prior is a measurement, not a belief.
- **Sparsity needs local shrinkage.** The horseshoe's global-local structure (nulls at $\kappa\approx$`0.993`, signals spared) recovered 5-of-100 at RMSE `0.033`, beating ridge (`0.267`, no zeros) and lasso (`0.061`, `35` false positives). Its posterior mean is still not exactly sparse.
- **In M-open, the posterior is right about a wrong model.** Fit to skewed heteroskedastic truth, the slope's posterior sd `0.0740` was too narrow; the sandwich SE `0.1019` matched the true sampling sd `0.1046`. Internal coherence is intact; external calibration is not — audit the width.
- **Power posteriors widen honestly.** $p_\eta\propto p(y\mid\theta)^\eta\pi(\theta)$ scales posterior variance by $1/\eta$; $\eta^\star=$ `0.527` recalibrated the misspecified slope to its sandwich width. Temperature, annealing, and tempering are the one knob; M-closed / M-complete / M-open name which world you are auditing.

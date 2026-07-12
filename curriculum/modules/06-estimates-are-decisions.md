# 06. Estimates and Intervals Are Decisions

> **Spine.** A point estimate and an interval are not summaries you read off a posterior — they are *answers to a loss function*, and what you condition on determines what your guarantee actually means.
> **Which line?** Line 4 (a decision minimizes posterior expected loss). Everything here is line 4 applied to two special "decisions": report a number, report a set.
> **Promise.** After this module you can derive which posterior summary a given loss demands, price an asymmetric decision as a quantile, and explain — with a picture — why a 50%-coverage interval can be *certain* on the data you actually saw.
> **Prereqs.** Modules 00 (four lines), 02 (conditioning), 04 (likelihood, sufficiency, **ancillarity**), 05 (conjugate posteriors, the posterior predictive, the precision-weighted mean).
> **Runtime.** ~11 s.
> **Sources.** C-B §7.3.4 (loss-function optimality, Bayes rules), §9.1–9.3 (coverage, credible vs. confidence sets, Example 9.2.18); booklet ch. 8 (credible/HPD intervals); the two-point uniform after Welch (1939) and Berger–Wolpert by concept; Jaynes (1976) and Cox (1958) by concept.

The four lines (module 00): **a model is a joint $p(\text{unknowns},\text{knowns})$; inference is conditioning; prediction is marginalization; a decision minimizes posterior expected loss.** The first three lines hand you a whole distribution — the posterior $p(\theta\mid y)$ and the predictive $p(\tilde y\mid y)$. But a colleague asks "so what's your estimate of $\theta$?" and a regulator asks "give me an interval." Collapsing a distribution to a number or a set *throws information away*, and the only principled way to throw information away is to say what the collapse is *for*. That "for" is a loss function, and line 4 does the rest: the mean, the median, the mode, every quantile, ridge, lasso — and the interval, whose guarantee means exactly what your conditioning makes it mean.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "06-estimates-are-decisions"       # this module's figure dir
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

## 06.1 The loss picks the estimator

**Definition (C-B §7.3.4).** A **loss** $L(\theta, a)$ is what it costs to report the action $a$ when the truth is $\theta$. Having observed $y$, the **posterior expected loss** of $a$ is
$$\rho(a) = \mathbb{E}_{\theta\mid y}\big[L(\theta, a)\big] = \int L(\theta, a)\,p(\theta\mid y)\,d\theta,$$
and the **Bayes estimate** is $\hat a = \arg\min_a \rho(a)$. This is line 4, verbatim: minimize expected loss under the posterior. C-B (7.3.19) proves this $a$ also minimizes the *Bayes risk* $\int R(\theta,\delta)\pi(\theta)\,d\theta$ — pointwise minimization of posterior expected loss and global minimization of average frequentist risk are the *same* $\hat a$. So a Bayes estimate is not "the Bayesian's number"; it is the optimal number under a stated loss, full stop.

**Setup.** Module 05's conjugate machinery has handed you a $\text{Gamma}(2,1)$ posterior for a rate $\theta$ (shape $2$, rate $1$; scipy `gamma(a=2, scale=1)`) — a deliberately *skewed* posterior. A colleague asks for *your one number* for $\theta$.

**Predict.** Commit to that number now — and to whether the question even has a unique answer. The reflex being tested is "the estimate is where the posterior is centered/peaked," as if 'center' were one place.

**Run.** Three losses, three estimators — and the derivations are three lines each:

- **Squared-error loss** $L=(\theta-a)^2$: $\rho'(a) = \mathbb{E}[-2(\theta-a)] = 0 \Rightarrow a = \mathbb{E}[\theta\mid y]$. **The posterior mean.**
- **Absolute-error loss** $L=|\theta-a|$: $\rho'(a) = P(\theta<a) - P(\theta>a) = 0 \Rightarrow a = \text{median}$. **The posterior median.**
- **0–1 loss** $L=\mathbf 1\{|\theta-a|>\varepsilon\}$ as $\varepsilon\downarrow 0$: $\rho(a) \approx 1 - 2\varepsilon\,p(a\mid y)$ is minimized where the density is largest. **The posterior mode (MAP).**

```python
# One skewed posterior, three losses -> three different point estimates.
post = stats.gamma(a=2, scale=1)                 # Gamma(2,1): shape 2, rate 1
g = np.linspace(1e-4, 40, 160_000)               # fine grid, wide enough to hold the tail
dg = g[1] - g[0]
dens = post.pdf(g)

mean_hat   = post.mean()                          # squared-error Bayes estimate
median_hat = post.median()                        # absolute-error Bayes estimate
mode_hat   = (2 - 1) / 1.0                         # (alpha-1)/rate for Gamma; 0-1 loss

# posterior expected loss of each action, evaluated by quadrature on the grid
def exp_sq(a):  return np.sum((g - a)**2      * dens) * dg
def exp_abs(a): return np.sum(np.abs(g - a)   * dens) * dg
print(f"posterior mean   (L2 -> mean)   = {mean_hat:.4f}   E[L2] = {exp_sq(mean_hat):.4f}")
print(f"posterior median (L1 -> median) = {median_hat:.4f}   E[L1] = {exp_abs(median_hat):.4f}")
print(f"posterior mode   (0-1 -> mode)  = {mode_hat:.4f}   density p(mode) = {post.pdf(mode_hat):.4f}")
# each estimate is optimal ONLY for its own loss:
print(f"cross-check: E[L2] at the median = {exp_sq(median_hat):.4f} > {exp_sq(mean_hat):.4f} (mean wins L2)")
print(f"cross-check: E[L1] at the mean   = {exp_abs(mean_hat):.4f} > {exp_abs(median_hat):.4f} (median wins L1)")

fig, ax = plt.subplots()
ax.plot(g, dens, color="C7", lw=1.5, label="posterior  Gamma(2,1)")
for a_hat, name, col in [(mode_hat, "mode (0–1)", "C0"),
                         (median_hat, "median (L1)", "C1"),
                         (mean_hat, "mean (L2)", "C2")]:
    ax.axvline(a_hat, color=col, lw=2, label=f"{name} = {a_hat:.2f}")
ax.set_xlim(0, 8)
ax.set_xlabel("θ"); ax.set_ylabel("posterior density")
ax.set_title("One skewed posterior, three losses, three estimates")
ax.legend()
save(fig, "loss-picks-estimator")
```

![Gamma(2,1) posterior with three vertical lines: mode at 1.0, median at 1.68, mean at 2.0, spread left-to-right along the skew.](figures/06-estimates-are-decisions/loss-picks-estimator.png)

**Reconcile.** Whatever single number you committed to, it was at best a third of an answer: the three estimates are `1.0000`, `1.6783`, `2.0000` — mode, median, mean, marching rightward in exactly that order because the $\text{Gamma}(2,1)$ posterior is right-skewed. "Your one number" was an ill-posed request; there are three defensible answers, and the loss function is what disambiguates them. On a *symmetric* posterior they would coincide (that is why the Normal lets you be sloppy: mean = median = mode), and the moment the posterior is skewed the choice of loss becomes a real decision. The cross-checks confirm optimality is loss-specific: the mean's expected *squared* loss `2.0000` — which is the posterior variance, exactly $2$ for Gamma(2,1), since $\mathbb E[(\theta-\mathbb E\theta)^2] = \mathrm{Var}[\theta\mid y]$ — beats the median's `2.1035`; the median's expected *absolute* loss `1.0517` beats the mean's `1.0827`. "Which point estimate is best?" is not a well-posed question until you name $L$.

> **Bridge — C-B Table 7.3.1.** Casella & Berger tabulate exactly this for a Binomial: under a uniform prior, $y$-of-$10$ successes gives a squared-error Bayes estimate $(y+1)/12$ and an absolute-error one (the posterior median) that differ at every $y$ except $y=5$ where the Beta posterior is symmetric. Same lesson, conjugate flavor: **the posterior mean is the answer to squared-error loss, not "the estimate."**

## 06.2 Asymmetric loss makes estimates into quantiles

Squared and absolute loss are symmetric: over- and under-shooting cost the same. Real decisions are lopsided. A retailer stocking a perishable good loses more per unit when she runs *out* (a lost sale, an angry customer) than when she over-orders (a markdown). This is the **newsvendor**, and it is line 4 on the *posterior predictive* $p(\tilde y\mid y)$ from module 05 — because the thing you are matching is *future demand*, not a parameter.

**Predict.** Your posterior predictive for demand has mean $10$, and a stockout costs three times a markdown. Commit to an order quantity before the derivation. (The reflex: "order the expected demand — about 10, maybe a bit more to be safe.")

Let underage (too little) cost $c_u$ per unit and overage (too much) cost $c_o$ per unit. Order $q$; demand $\tilde y$ is random with predictive CDF $F$. Expected cost is $\mathbb{E}[c_u(\tilde y - q)_+ + c_o(q - \tilde y)_+]$, and
$$\frac{d}{dq}\,\mathbb{E}[\text{cost}] = -c_u\,P(\tilde y > q) + c_o\,P(\tilde y \le q) = (c_u+c_o)F(q) - c_u = 0 \;\Longrightarrow\; F(q^\star) = \frac{c_u}{c_u + c_o}.$$
The optimal order is a **quantile of the predictive**, at the *critical fractile* $c_u/(c_u+c_o)$ — emphatically **not** the predictive mean. With underage three times as costly as overage, you stock the $0.75$-quantile.

```python
# Newsvendor: underage 3x overage -> order the 0.75-quantile of the PREDICTIVE.
# Predictive from a Gamma-Poisson (module 05): lambda | y ~ Gamma(20, rate 2),
# so future demand ~ NegBinom -> overdispersed counts. (r, p) parameterization:
r_nb, p_nb = 20.0, 2.0 / (2.0 + 1.0)              # Gamma(a=20, rate=2) -> NB(r=20, p=2/3)
pred = stats.nbinom(r_nb, p_nb)
c_u, c_o = 3.0, 1.0
crit = c_u / (c_u + c_o)
q_star   = pred.ppf(crit)                          # optimal order = 0.75-quantile
q_meanby = pred.ppf(0.5)                           # what "order the median" would say
print(f"critical fractile c_u/(c_u+c_o) = {crit:.2f}")
print(f"predictive mean demand          = {pred.mean():.2f}")
print(f"optimal order q* (0.75-quantile)= {q_star:.0f}   (median would say {q_meanby:.0f})")

# verify by brute force: expected cost is minimized at q*
qs = np.arange(0, 30)
draws = pred.rvs(size=400_000, random_state=rng)
cost = np.array([np.mean(c_u*np.maximum(draws-q,0) + c_o*np.maximum(q-draws,0)) for q in qs])
print(f"argmin of simulated expected cost = {qs[cost.argmin()]:.0f}  (matches q*)")
```

**Reconcile.** If you committed to "about 10," you understocked: ordering the predictive **mean** (`10.00`) systematically eats 3-to-1 stockout losses, and "a bit more to be safe" is doing the right thing for an unquantified reason. The loss-optimal order is `12` — the $0.75$-quantile, two units above the mean, with the safety margin *derived* rather than guessed — and the brute-force expected-cost minimizer agrees. The general object here is the **pinball (quantile) loss** $\rho_\tau(u) = u\,(\tau - \mathbf 1\{u<0\})$: its posterior-predictive minimizer is exactly the $\tau$-quantile (same one-line derivative as above, with $\tau$ in place of the fractile). Minimizing pinball loss over a *conditional* predictive $p(\tilde y \mid x)$ is **quantile regression** — the same object you may have trained a gradient-boosted model on, now read as a Bayes rule under an asymmetric loss.

## 06.3 MAP is penalized MLE — and the mode is not the mean

Take the 0–1-loss estimate — the posterior **mode** — and read it in log space:
$$\hat\theta_{\text{MAP}} = \arg\max_\theta\;\big[\log p(y\mid\theta) + \log p(\theta)\big] = \arg\min_\theta\;\big[\underbrace{-\log p(y\mid\theta)}_{\text{loss}} + \underbrace{(-\log p(\theta))}_{\text{penalty}}\big].$$
**The prior is a penalty; the MAP is penalized maximum likelihood.** Two priors on regression coefficients give the two regularizers every ML practitioner knows:

- **Gaussian prior** $\beta\sim N(0,\tau^2 I)$: $-\log p(\beta) = \|\beta\|_2^2/(2\tau^2) + \text{const}$ — this is **ridge**, with penalty $\lambda = \sigma^2/\tau^2$. And because a Gaussian likelihood $\times$ Gaussian prior gives a *Gaussian* posterior, whose mode equals its mean, **ridge is simultaneously the MAP and the posterior mean** here (module 05's precision-weighted mean).
- **Laplace prior** $\beta\sim\text{Laplace}(0,b)$: $-\log p(\beta) = \|\beta\|_1/b + \text{const}$ — this is **lasso**, with penalty $\lambda = \sigma^2/b$. The $\ell_1$ penalty has a corner at $0$, so the MAP produces **exact zeros**: a genuine variable selector.

```python
# Ridge == Gaussian-prior MAP == posterior mean (they coincide for Gaussians).
sigma2, tau2 = 1.0, 4.0                            # noise var, prior var
y_obs = np.array([2.3])                            # one observation, y = theta + noise
lam_ridge = sigma2 / tau2
post_mean = (y_obs.sum()/sigma2) / (1/tau2 + len(y_obs)/sigma2)  # module 05 precision-weighted mean
ridge_est = y_obs.sum() / (len(y_obs) + lam_ridge)               # argmin ||y-theta||^2 + lam*theta^2
print(f"ridge penalty lambda = sigma^2/tau^2 = {lam_ridge:.2f}")
print(f"ridge MAP = {ridge_est:.6f}   posterior mean = {post_mean:.6f}   "
      f"max|diff| = {abs(ridge_est-post_mean):.1e}")
```

Ridge and the posterior mean agree to `0.0e+00` — machine zero — because for a Gaussian the mode *is* the mean. Now the honest part, and the reason this module refuses to call the lasso "sparse Bayes":

```python
# Lasso 1-D: Laplace-prior MAP soft-thresholds to EXACT zero;
#            the Laplace-prior posterior MEAN is smooth and never zero.
b = 1.0                                            # Laplace scale; threshold = sigma^2/b = 1
thr = sigma2 / b
def lasso_map(z):  return np.sign(z) * max(abs(z) - thr, 0.0)   # soft-threshold
def lap_post_mean(z):                              # E[theta | z] under Laplace prior
    t = np.linspace(-25, 25, 200_001)
    w = np.exp(-(z - t)**2/(2*sigma2) - np.abs(t)/b)
    return np.trapezoid(t*w, t) / np.trapezoid(w, t)

for z in (0.3, 0.8):                               # both BELOW the threshold: MAP zeros out
    print(f"observed z={z}:  lasso MAP = {lasso_map(z):.4f}   "
          f"posterior mean = {lap_post_mean(z):.4f}")

# a picture of the estimators as functions of the data z
zz = np.linspace(-3, 3, 400)
fig, ax = plt.subplots()
ax.plot(zz, [lasso_map(z) for z in zz], color="C0", lw=2, label="lasso MAP (mode) — has a flat zero")
ax.plot(zz, [lap_post_mean(z) for z in zz], color="C1", lw=2, label="Laplace posterior mean — never zero")
ax.plot(zz, zz, color="k", ls=":", lw=1, label="identity (no shrinkage)")
ax.axhline(0, color="grey", lw=0.8); ax.axvspan(-thr, thr, color="C0", alpha=0.08)
ax.set_xlabel("observed z"); ax.set_ylabel("estimate of θ")
ax.set_title("Lasso = a MODE with exact zeros; the posterior MEAN is never sparse")
ax.legend(fontsize=9)
save(fig, "lasso-mode-vs-mean")
```

![Two curves versus the data z: the lasso MAP is flat at zero inside a dead-zone then rises with unit slope; the Laplace posterior mean is a smooth S that passes through the origin without ever being exactly zero.](figures/06-estimates-are-decisions/lasso-mode-vs-mean.png)

At $z=0.3$ and $z=0.8$ the lasso MAP is `0.0000` — exactly, twice — while the Laplace-prior posterior *mean* is `0.1432` and `0.3945`, small but strictly nonzero. **Sparsity is a property of the mode, not of the posterior.** The lasso zeros a coefficient because the $\ell_1$ penalty's corner parks the *mode* on the axis; average over the same posterior instead and the coefficient is shrunk-but-alive. This is not a bug in either object — it is the §06.1 lesson biting hard: mode and mean answer *different losses*, and on a corner-having, skewed posterior they disagree qualitatively, not just numerically. (Forward pointers: module 07 formalizes these priors and the "flat in what?" question; module 14 makes the $\lambda \leftrightarrow \tau^2$ correspondence exact for regression and revisits sparsity with the horseshoe in module 18.)

## 06.4 Two intervals, two meanings

Point estimates were line 4 with $\mathcal A = \Theta$. Intervals are line 4 with $\mathcal A$ = *sets*, and here two traditions genuinely diverge — not into right and wrong, but into answers to two different questions.

- A **credible interval** $C(y)$ satisfies $P(\theta\in C(y)\mid y) = 1-\alpha$: a statement about $\theta$ *given the data you hold*. It is read off the posterior (booklet ch. 8: equal-tailed, or the shortest/HPD interval). The randomness is in $\theta$; the data are fixed at what you saw.
- A **confidence interval** $[L(Y), U(Y)]$ satisfies $P_\theta\big(\theta\in[L(Y),U(Y)]\big) \ge 1-\alpha$ **for every $\theta$** (C-B Def. 9.1.4–9.1.5): a statement about the *procedure*, over hypothetical repetitions. The randomness is in $Y$; $\theta$ is fixed and unknown.

C-B state the trap plainly in the remark after Definition 9.1.4: the probability statement $P_\theta(\theta\in[L(X),U(X)])$, which *looks* like a statement about a random $\theta$, refers to the randomness of the data $X$ — read it as $P_\theta(L(X)\le\theta,\ U(X)\ge\theta)$, a statement about a random interval. The confidence guarantee is about how often that *random interval* would trap a *fixed* $\theta$ if you reran the experiment forever. It is a pre-data promise about a machine that manufactures intervals — correct, useful, and answering a question about the machine, not about your dataset. The next section shows exactly what that distinction can cost, and what conditioning buys back.

## 06.5 The two-point uniform: a 50% interval that is sometimes certain  ⟵ centerpiece

**Setup.** Two observations $X_1, X_2 \sim U(\theta-\tfrac12,\ \theta+\tfrac12)$, iid. You do not know $\theta$; you report the interval between the two points, $[\,X_{(1)}, X_{(2)}\,]$ (min to max). It is a *valid 50% confidence interval*: its coverage is exactly $\tfrac12$ for every $\theta$. Two points, each equally likely to fall on either side of $\theta$, straddle $\theta$ (one below, one above) exactly when they disagree in sign — probability $\tfrac12$. (This is the Welch / Berger–Wolpert example.)

**Predict.** You run it once and observe that the two points are far apart: their gap $R = |X_1 - X_2| = 0.9$. *Commit to a number:* given that you saw $R=0.9$, what is your confidence that this particular interval contains $\theta$? The interval is labeled "50%," and the near-universal reflex — the one worth catching yourself in — is **"50%, that's what the interval is."** Hold onto that 50%.

**Run.** Two facts collide. First, the marginal coverage really is $\tfrac12$. Second, $R = |X_1-X_2|$ is an **ancillary statistic** (module 04): its distribution does not depend on $\theta$ — sliding $\theta$ slides both points together and leaves their gap untouched — so $R$ says nothing about *where* $\theta$ is, but everything about *how good this interval is*. Condition on it. Fix $\theta=0$ (WLOG); the points lie in $(-\tfrac12,\tfrac12)$ with gap $r$. The interval $[X_{(1)}, X_{(2)}]$ has width $r$ and covers $0$ iff the points straddle it. Given $r$, the lower point $X_{(1)}$ is uniform on $[-\tfrac12,\ \tfrac12 - r]$ (length $1-r$); it straddles $0$ iff $X_{(1)}\in[-r, 0]$.

- **If $r < \tfrac12$:** the straddling set $[-r,0]$ (length $r$) sits entirely inside the allowed $[-\tfrac12, \tfrac12-r]$, so the conditional coverage is $\dfrac{r}{1-r}$.
- **If $r \ge \tfrac12$:** the allowed range $[-\tfrac12,\tfrac12-r]$ sits entirely inside $[-r,0]$, so **every** admissible placement straddles $0$ — coverage $= 1$. The interval is *certain*.

$$\boxed{\;\mathrm{Cov}(\theta \mid R=r) = \begin{cases} \dfrac{r}{1-r}, & r < \tfrac12,\\[4pt] 1, & r \ge \tfrac12.\end{cases}\;}$$

```python
# Two-point uniform. Annotated picture, staged predict-first, then the geometry
# verified by simulation. theta = 0 without loss of generality.
def two_point(n):
    X = rng.uniform(-0.5, 0.5, size=(n, 2))
    lo, hi = X.min(1), X.max(1)
    return lo, hi, hi - lo                          # interval endpoints and gap R

# --- annotated picture: a handful of realized intervals, colored by R regime ---
lo, hi, R = two_point(14)
order = np.argsort(R)
fig, ax = plt.subplots(figsize=(7, 4.4))
for row, k in enumerate(order):
    certain = R[k] >= 0.5
    covers = (lo[k] <= 0) and (hi[k] >= 0)
    col = "C2" if certain else "C1"                  # green = certain regime, orange = coin-flip
    ax.plot([lo[k], hi[k]], [row, row], color=col, lw=4, solid_capstyle="round")
    mark = "covers θ" if covers else "MISSES θ"
    ax.text(hi[k] + 0.03, row, f"R={R[k]:.2f}  ({mark})", va="center", fontsize=8,
            color="black" if covers else "C3")
ax.axvline(0, color="k", ls="--", lw=1.3)
ax.text(0.01, -1.1, "θ = 0", fontsize=9)
ax.set_yticks([]); ax.set_xlim(-0.75, 1.15); ax.set_ylim(-1.6, 14)
ax.set_xlabel("value")
ax.set_title("Each interval is a '50%' CI — but R tells you which are certain (green) vs coin-flip (orange)")
save(fig, "two-point-intervals")

print(f"predict-first: you saw R=0.90 -> naive answer 50%; geometry says coverage = 1 (certain)")

# --- marginal coverage over many replicates: exactly 1/2 ---
lo, hi, R = two_point(4_000_000)
cover = (lo <= 0) & (hi >= 0)
print(f"marginal coverage over all R = {cover.mean():.3f}   (exactly 0.500)")
```

![Fourteen horizontal interval bars sorted by gap R; long green bars (R>=0.5) at the top, all crossing the dashed theta=0 line and labeled 'covers'; short orange bars below, a mix of covers and misses.](figures/06-estimates-are-decisions/two-point-intervals.png)

Averaged over all $R$, coverage is `0.500` — the confidence claim is honest. But look at the picture: **every green bar covers $\theta$**, because once the two points are more than $\tfrac12$ apart they *must* straddle any $\theta$ they surround. When you saw $R=0.9$, the correct post-data confidence is not $50\%$ — it is $100\%$. And when $R$ is small the interval is *worse* than a coin flip ($r=0.2 \Rightarrow$ coverage $0.25$). The $50\%$ is an average over situations you are no longer in. Overlay the exact geometry on the simulation:

```python
# Conditional coverage vs r: exact r/(1-r) capped at 1, with simulation overlaid.
lo, hi, R = two_point(8_000_000)
cover = (lo <= 0) & (hi >= 0)
edges = np.linspace(0, 1, 41); ctr = 0.5*(edges[:-1]+edges[1:])
emp = np.array([cover[(R>=edges[i])&(R<edges[i+1])].mean() for i in range(len(ctr))])
exact = np.where(ctr < 0.5, ctr/(1-ctr), 1.0)

# a few printed checkpoints (numbers contract)
for r0 in (0.10, 0.20, 0.30, 0.90):
    m = np.abs(R - r0) < 0.01
    print(f"R≈{r0:.2f}: simulated coverage {cover[m].mean():.3f}   "
          f"exact {r0/(1-r0) if r0<0.5 else 1.0:.3f}")

fig, ax = plt.subplots()
ax.plot(ctr, exact, color="C0", lw=2.5, label="exact  Cov(θ|R=r) = r/(1−r), then 1")
ax.plot(ctr, emp, "o", color="C3", ms=4, label="simulation (binned)")
ax.axhline(0.5, color="grey", ls="--", lw=1, label="marginal 'confidence' = 0.5")
ax.axvline(0.5, color="k", ls=":", lw=1)
ax.set_xlabel("observed gap  R = |X₁ − X₂|"); ax.set_ylabel("coverage of the 50% interval")
ax.set_title("The '50%' is an average; conditionally the interval ranges from coin-flip to certain")
ax.legend(fontsize=9)
save(fig, "two-point-coverage")
```

![Coverage versus R: a curve rising from 0 along r/(1-r), reaching 1 at R=0.5 and staying flat at 1; red simulation dots lie on the curve; a dashed horizontal line at 0.5 marks the marginal confidence the curve crosses only at one point.](figures/06-estimates-are-decisions/two-point-coverage.png)

The simulated conditional coverages land on the exact curve — `0.111`, `0.250`, `0.429`, `1.000` at $R\approx 0.10, 0.20, 0.30, 0.90$, matching $r/(1-r)$ (then $1$) at every checkpoint. **The confidence interval is not wrong** — $50\%$ is the correct long-run frequency of the *procedure*. It is answering "how often does this machine trap $\theta$?" when you asked "should I believe *this* interval?" The Bayesian credible interval, which conditions on all of the data (including $R$), gives coverage that *tracks* $R$ automatically, because conditioning on the ancillary is not optional for it — it is what conditioning *means*.

> **Conditionality & ancillarity (module 04 callback).** An **ancillary** statistic has a $\theta$-free distribution; by itself it carries no information about $\theta$ (module 04: for $N(\theta,1)$, the residuals $x_i-\bar x$ are ancillary and, by Basu, independent of $\bar x$). The **conditionality principle** says: *condition on the ancillary you observed.* Here $R$ is ancillary — it cannot help you locate $\theta$ — yet it tells you exactly how sharp your interval is, so ignoring it (as the unconditional $50\%$ does) throws away decision-relevant information. Module 04 met ancillarity as a curiosity; this is where it earns its keep. The two-instruments exercise below is the same lesson stripped to its bones.

## 06.6 The precise sense in which Bayesian intervals are calibrated

Does the credible interval have a *frequency* guarantee at all, or only a within-model one? It has one — but averaged over the prior, not pointwise, and this is exactly right.

**Theorem (prior-averaged coverage).** Let $\theta\sim\pi$ and $Y\mid\theta\sim p(\cdot\mid\theta)$, and let $C(Y)$ be any $1-\alpha$ posterior credible set. Then the coverage, averaged over the prior, is exactly $1-\alpha$:
$$\int \mathrm{Cov}(\theta)\,\pi(\theta)\,d\theta = \mathbb{E}_\theta\,\mathbb{E}_{Y\mid\theta}\big[\mathbf 1\{\theta\in C(Y)\}\big] = \mathbb{E}_Y\,\underbrace{\mathbb{E}_{\theta\mid Y}\big[\mathbf 1\{\theta\in C(Y)\}\big]}_{=\,1-\alpha\ \text{by construction}} = 1-\alpha.$$
The middle step is just Fubini — swap the order of the two expectations over the joint $\pi(\theta)p(y\mid\theta)$ — and the inner expectation is $1-\alpha$ *for every* $y$ because that is what "credible set" means. So a credible interval is calibrated **on average over data drawn from your own model**. Pointwise, at a fixed $\theta$, coverage is free to vary, and it does. Take the conjugate Normal–Normal from module 05: one observation $Y\mid\theta\sim N(\theta,1)$, prior $\theta\sim N(0,\tau^2)$ with $\tau=2$; the $95\%$ credible interval is $\hat\theta \pm 1.96\sqrt{v}$ with posterior mean $\hat\theta = \tau^2 Y/(\tau^2+1)$ and variance $v = \tau^2/(\tau^2+1)$.

**Predict** before running: at $\theta=4$ — two prior-SDs into the tail — is the pointwise coverage of the 95% credible interval *above* or *below* 0.95? (The comfortable guess: "above; shrinkage helps everywhere.")

```python
# Prior-averaged coverage = 1-alpha exactly (Fubini); pointwise coverage varies;
# a misspecified prior degrades it gracefully. Normal-Normal, one obs, sigma^2=1.
tau, sig = 2.0, 1.0
z = 1.96
v = tau**2 / (tau**2 + sig**2)                      # posterior variance
def credible(y):                                     # 95% credible interval endpoints
    m = (tau**2 * y) / (tau**2 + sig**2)
    return m - z*np.sqrt(v), m + z*np.sqrt(v)
def coverage_at(theta, n=400_000):                   # frequentist coverage at fixed theta
    y = rng.normal(theta, sig, size=n)
    lo, hi = credible(y)
    return ((lo <= theta) & (theta <= hi)).mean()

# (1) prior-averaged: draw theta ~ TRUE prior N(0, tau^2), then y | theta
th = rng.normal(0.0, tau, size=3_000_000)
y  = rng.normal(th, sig)
lo, hi = credible(y)
print(f"prior-averaged coverage (true prior)   = {((lo<=th)&(th<=hi)).mean():.4f}   (theorem: 0.9500)")
# (2) pointwise, two values of theta
print(f"pointwise coverage at θ=0              = {coverage_at(0.0):.4f}")
print(f"pointwise coverage at θ=4              = {coverage_at(4.0):.4f}")
# (3) misspecified prior: truth is more diffuse (tau_true=5) than the model's tau=2
th_true = rng.normal(0.0, 5.0, size=3_000_000)
y2 = rng.normal(th_true, sig)
lo2, hi2 = credible(y2)
print(f"prior-averaged coverage (MISSPEC τ=5)  = {((lo2<=th_true)&(th_true<=hi2)).mean():.4f}")

# figure: pointwise coverage curve vs theta, with the prior-averaged line
tg = np.linspace(-8, 8, 41)
cov_curve = np.array([coverage_at(t, n=200_000) for t in tg])
fig, ax = plt.subplots()
ax.plot(tg, cov_curve, color="C1", lw=2, label="pointwise coverage  Cov(θ)")
ax.axhline(0.95, color="C0", lw=2, ls="--", label="prior-averaged = 0.95 (exact)")
ax.axvline(0, color="grey", lw=0.8)
ax.set_xlabel("true θ"); ax.set_ylabel("frequentist coverage of the 95% credible interval")
ax.set_title("Credible intervals: calibrated ON AVERAGE over the prior, not at every θ")
ax.legend(fontsize=9)
save(fig, "prior-averaged-coverage")
```

![Coverage versus true theta: a hump peaking above 0.95 near theta=0 and sloping down toward the tails, crossing a dashed horizontal line at 0.95; the curve is above 0.95 where the prior concentrates and dips below it far from zero.](figures/06-estimates-are-decisions/prior-averaged-coverage.png)

Three regimes, three numbers. Under the true prior, prior-averaged coverage is `0.9501` — the theorem's exact $0.95$, up to Monte-Carlo error. Pointwise, if you guessed "shrinkage helps everywhere," the tail catches you: coverage is *above* nominal near the prior's center (`0.9715` at $\theta=0$, where shrinkage toward $0$ helps) and *below* nominal in the tail (`0.8827` at $\theta=4$, where the same shrinkage pulls the interval *away* from the truth — shrinkage is a bet on the prior, and it pays where the prior is right). C-B Example 9.2.18 works this pointwise computation analytically and shows the coverage can even $\to 0$ in extreme parameter configurations. And when the prior is **misspecified** — the world is more spread out ($\tau_{\text{true}}=5$) than the model assumed ($\tau=2$) — the *averaged* guarantee degrades *gracefully* to `0.8288`, not catastrophically. This is the honest statement of "Bayesian intervals are calibrated": exactly $1-\alpha$ when the prior is right, robust-ish when it is close, and the audit that catches a bad prior is precisely this coverage check. Module 08's Bernstein–von Mises theorem is the large-$n$ endgame: as data accumulate, the likelihood dominates the prior, pointwise coverage flattens to $1-\alpha$ for *all* $\theta$, and credible and confidence intervals fuse — the distinction dramatized in §06.5 quietly evaporates.

## Bridge — decisions are everywhere in your ML stack

Every one of these moves is something an ML practitioner already does, un-named:
- **Choosing a loss chooses a summary.** Train with MSE and your model targets the conditional *mean*; train with MAE it targets the *median*; train with pinball loss it targets a *quantile* — literally the §06.1–06.2 result, which is why quantile regression and probabilistic forecasting exist.
- **Regularization is a prior; the fitted weights are a MAP.** Weight decay is a Gaussian prior, $\ell_1$ is Laplace (§06.3, cashed out for deep nets in module 25). "Tune $\lambda$ by cross-validation" is estimating a prior variance (module 14).
- **A classifier threshold is a Bayes rule.** Acting when $p(\text{positive}\mid x)$ exceeds $c_{\text{FP}}/(c_{\text{FP}}+c_{\text{FN}})$ is the newsvendor fractile wearing a confusion matrix; $0.5$ is optimal only under symmetric costs (module 22).
- **Conformal prediction** gives *marginal* coverage under exchangeability and no conditional guarantee — the §06.5 lesson, made into a modern tool (module 26).

## Pitfalls

- **Reporting the posterior mean by reflex.** The mean is the answer to squared-error loss and nothing else. On a skewed posterior (variances, rates, counts, anything log-scaled) the median or mode may be the decision you actually want; on a *bimodal* posterior the mean can sit in a valley of near-zero density — a value the posterior considers *implausible*.
- **Calling the lasso "sparse Bayes."** The lasso point estimate is a *mode*; the Laplace-prior posterior *mean* is never exactly zero (§06.3). If you want both honest uncertainty and sparsity, you need a different prior (spike-and-slab, horseshoe — module 18), not the lasso's mode.
- **Reading a confidence interval as a post-data probability.** "$\theta$ has a 95% chance of being in $[L,U]$" is a *credible*-interval statement. The confidence guarantee is about the procedure over repetitions; conditionally, as §06.5 shows, a valid $50\%$ interval can be certain or a coin-flip. That is a feature of a pre-data guarantee, not a defect.
- **Ignoring ancillaries / recognizable subsets.** When an ancillary statistic (like $R$) sharpens or degrades your interval, unconditional coverage averages over situations you are not in. Condition on what you actually observed.
- **Expecting pointwise Bayesian coverage.** Credible intervals are calibrated *averaged over the prior* (§06.6), not at every fixed $\theta$. If you need coverage at a specific $\theta$, that is a frequentist question — ask it, and audit.

## Exercises

**Exercise 06.1 — The two instruments (conditionality).**  *(surprising)*
*Setup:* You measure a quantity $\theta$ with one of two instruments, chosen by a fair coin *you can see*. Instrument A is precise: $Y\sim N(\theta, 1)$. Instrument B is crude: $Y\sim N(\theta, 100)$. You used A, and got a reading. A colleague builds a confidence interval by *averaging over the coin* — treating "which instrument" as random and reporting an interval calibrated across both.
*Predict:* Your reading came from the precise instrument A. Should the width of your reported interval depend on *which instrument you used*, or is the coin-averaged interval fine?
*Reason:* "Unbiased/valid coverage is good enough" — the reflex that a procedure with correct average coverage needs no further conditioning.
*Run:*
```python
sigA, sigB = 1.0, 10.0                              # SDs (var 1 and 100)
# Coverage of the naive 95% interval that uses the AVERAGE variance, when you actually used A.
var_avg = 0.5*sigA**2 + 0.5*sigB**2                 # coin-averaged variance
half = 1.96*np.sqrt(var_avg)                        # fixed half-width, ignores which instrument
yA = rng.normal(0.0, sigA, size=1_000_000)          # truth theta=0, instrument A used
print(f"coin-averaged half-width = {half:.2f}")
print(f"conditional coverage GIVEN A used = {(np.abs(yA) <= half).mean():.4f}  (nominal 0.95)")
print(f"proper A-interval half-width = {1.96*sigA:.2f}  ({half/(1.96*sigA):.1f}x narrower)")
```
<details><summary>Reconcile</summary>

The coin-averaged interval has half-width `13.93` and, *given you used A*, covers `1.0000` of the time — a nominal "95%" interval that is really 100% conditional, and absurdly wide (`7.1`× the `1.96` it should be). "Which instrument" is **ancillary** (its distribution — the coin — doesn't depend on $\theta$), yet it determines your precision entirely. The conditionality principle (Cox 1958): condition on the experiment you actually ran. Averaging over the coin answers "how wide must an interval be to work across both instruments?" — a question about a machine you are not using. Same structure as §06.5's $R$: an ancillary that carries no location information but all of the sharpness information.
</details>

**Exercise 06.2 — Jaynes's truncated exponential (a CI that excludes the possible).**  *(surprising)*
*Setup:* Lifetimes exceed a known guarantee time $\theta$: $Y_i\sim \theta + \text{Exp}(1)$, i.e. density $e^{-(y-\theta)}$ for $y\ge\theta$. You observe $n=3$ values. A textbook $90\%$ confidence interval for $\theta$ is built from the pivot $\bar Y - \theta$ (whose distribution, $\tfrac13\text{Gamma}(3,1)$, is $\theta$-free): $C = [\bar y - c_2,\ \bar y - c_1]$ with $c_i = \tfrac13\,G^{-1}(1-\alpha_i)$ quantiles of the pivot, split $\alpha_1=\alpha_2=0.05$.
*Predict:* Every observation satisfies $y_i \ge \theta$, so **$\theta \le \min_i y_i$** is a logical certainty. Can the $90\%$ confidence interval place $\theta$ *above* the smallest observation — i.e. assert something the data have already ruled out?
*Reason:* "A $90\%$ CI contains the plausible values of $\theta$" — the habit of reading a confidence set as a plausibility set.
*Run:*
```python
# One dataset where the mean-based 90% CI lies ABOVE min(y): impossible values.
y = np.array([9.0, 9.1, 12.0])                      # theta must be <= 9.0
ybar, ymin = y.mean(), y.min()
# equal-tailed pivotal CI from (ybar - theta) ~ Gamma(n,1)/n shifted; endpoints:
n = len(y)
lo = ybar - stats.gamma(n, scale=1).ppf(0.95)/n     # upper pivot quantile -> lower theta
hi = ybar - stats.gamma(n, scale=1).ppf(0.05)/n     # lower pivot quantile -> higher theta
print(f"min(y) = {ymin:.2f}  (theta is IMPOSSIBLE above this)")
print(f"90% confidence interval for theta = [{lo:.2f}, {hi:.2f}]")
print(f"does the CI exceed min(y)?  upper end {hi:.2f} > {ymin:.2f}: {hi > ymin}")
```
<details><summary>Reconcile</summary>

The interval's upper end is `9.76`, above `min(y) = 9.00`, so the "$90\%$" confidence interval asserts values of $\theta$ that the likelihood assigns *zero probability* — every such $\theta$ contradicts an observed $y_i \ge \theta$. The CI is still a valid confidence procedure (it traps $\theta$ $90\%$ of the time over repetitions), but it is a statement about the procedure, not about $\theta$: it does not know that $\min_i y_i$ is an ancillary-flavored hard bound the data hand you for free. The likelihood is $\propto e^{-\sum(y_i-\theta)}\mathbf 1\{\theta\le\min y_i\}$, so any posterior sits entirely below `9.00` — it cannot exclude the possible, because conditioning multiplies by an indicator the CI ignores. Jaynes's point exactly: post-data, condition on what the data prove.
</details>

**Exercise 06.3 — Order more, or less?**  *(ML/ops bridge)*
*Setup:* Demand for a perishable is predicted by the posterior predictive $\tilde y\sim\text{NegBinom}$ with mean $10$ from §06.2. Yesterday overage got expensive: markdowns now cost the *same* as a stockout, $c_u = c_o$.
*Predict:* With underage and overage now equally costly (was $3{:}1$), does the optimal order rise, fall, or stay at $12$? Commit to a direction.
*Reason:* "Costs went up on the overage side, so order more to be safe" — conflating which cost changed with which way the fractile moves.
*Run:*
```python
pred = stats.nbinom(20.0, 2.0/3.0)                   # same predictive as 06.2
for (cu, co) in [(3.0, 1.0), (1.0, 1.0)]:
    frac = cu/(cu+co)
    print(f"c_u:c_o = {cu:.0f}:{co:.0f} -> fractile {frac:.2f} -> order {pred.ppf(frac):.0f}")
```
<details><summary>Reconcile</summary>

The order **falls**, from `12` to `10`, the median. Making overage *relatively* more expensive lowers the critical fractile from $0.75$ to $0.50$, so you stock less. The naive "costs went up, order more" reasoning tracks the wrong thing: only the *ratio* $c_u/(c_u+c_o)$ matters, and raising $c_o$ (relative to $c_u$) pushes the fractile — and the order — down. At $c_u=c_o$ the fractile is $0.50$, so the optimal order is always the **median** — which here happens to equal the predictive mean `10.00` because this NB predictive is nearly symmetric, not by rule; on a more skewed predictive the two part ways, exactly as in §06.1. Same mechanism as a cost-sensitive classifier threshold (module 22).
</details>

**Exercise 06.4 — Why your lasso zeros a coefficient your posterior keeps.**  *(ML bridge, surprising)*
*Setup:* One standardized coefficient, data summarized by $z=0.5$; Laplace prior with scale $b=1$ (so the soft-threshold is $\sigma^2/b = 1$), Gaussian likelihood with $\sigma=1$.
*Predict:* The lasso reports this coefficient as exactly $0$ (it is below threshold). Is the *posterior mean* also essentially $0$ (say $<0.02$), or materially nonzero?
*Reason:* "The lasso and the Bayesian Laplace prior are the same model, so they give the same answer" — conflating the mode with the mean.
*Run:*
```python
z, b, s2 = 0.5, 1.0, 1.0
lasso = np.sign(z)*max(abs(z) - s2/b, 0.0)          # soft-threshold -> exact 0
t = np.linspace(-25, 25, 200_001)
w = np.exp(-(z - t)**2/(2*s2) - np.abs(t)/b)
post_mean = np.trapezoid(t*w, t) / np.trapezoid(w, t)
print(f"lasso MAP (mode) = {lasso:.4f}   posterior mean = {post_mean:.4f}")
```
<details><summary>Reconcile</summary>

The lasso MAP is `0.0000`; the posterior mean is `0.2410` — not a rounding whisker off zero, a quarter of the way to the raw signal. Same prior, same likelihood, same *posterior* — but the mode sits on the $\ell_1$ corner at $0$ while the mean integrates the whole (asymmetric, one-sided-shifted) posterior and lands well away from it. Sparsity is a fact about *where the peak is*, and peaks are fragile: the posterior still puts substantial mass on nonzero $\theta$. If a downstream decision averages over coefficients (prediction, model averaging) it sees `0.2410`, not `0`. This is why "Bayesian lasso" point-and-click sparsity is a category error, and why genuinely sparse Bayesian inference needs spike-and-slab or horseshoe priors (module 18).
</details>

**Exercise 06.5 — Equal-tailed or HPD? A set is a decision too.**  *(surprising)*
*Setup:* Report a $90\%$ credible interval for the skewed $\text{Gamma}(2,1)$ posterior of §06.1. The default recipe is **equal-tailed**: $[\,\text{ppf}(0.05),\ \text{ppf}(0.95)\,]$, leaving $5\%$ in each tail. The alternative is the **HPD** (highest-posterior-density) interval — the *shortest* interval holding $90\%$ (booklet ch. 8), whose endpoints sit at equal density.
*Predict:* Two things. (a) Is the equal-tailed interval the shortest $90\%$ interval, or is the HPD meaningfully shorter? (b) Can the equal-tailed interval *exclude* a value of $\theta$ that is **more probable** (higher posterior density) than values it *includes*?
*Reason:* "An equal-tailed interval is the standard credible interval, so it must contain the most-plausible region" — treating the reporting convention as automatically the highest-density set.
*Run:*
```python
from scipy.optimize import minimize_scalar
P = stats.gamma(a=2, scale=1)
et = (P.ppf(0.05), P.ppf(0.95))                     # equal-tailed 90%
def width(l): return P.ppf(P.cdf(l) + 0.90) - l     # width of a 90% interval starting at l
l = minimize_scalar(width, bounds=(1e-6, P.ppf(0.10)), method="bounded").x
hpd = (l, P.ppf(P.cdf(l) + 0.90))                   # HPD 90%
print(f"equal-tailed: [{et[0]:.4f}, {et[1]:.4f}]  length {et[1]-et[0]:.4f}")
print(f"HPD:          [{hpd[0]:.4f}, {hpd[1]:.4f}]  length {hpd[1]-hpd[0]:.4f}")
print(f"density at equal-tailed ends: lo {P.pdf(et[0]):.4f}  hi {P.pdf(et[1]):.4f}")
print(f"density just OUTSIDE the lower ET end (θ=0.15): {P.pdf(0.15):.4f}")
```
<details><summary>Reconcile</summary>

(a) The HPD interval `[0.0838, 3.9321]` has length `3.8483`, about $12\%$ shorter than the equal-tailed `[0.3554, 4.7439]` (length `4.3885`) — for a set-valued decision under a "shorter is better" loss, equal-tailed is *not* optimal on a skewed posterior. (b) Yes: the equal-tailed interval's endpoints have wildly unequal density — `0.2491` at the low end versus `0.0413` at the high end. It *includes* a whole upper region at density below `0.0413`, while *excluding* points just below its lower endpoint — density `0.1291` at $\theta=0.15$, three times more probable than the upper endpoint it keeps. The equal-tailed convention chops equal *probability* off each tail, not equal *plausibility*, so on a skew it trades away short high-density mass near $0$ for a long low-density tail. Which to report is itself a decision (equal-tailed is transformation-friendly and trivial from MCMC draws; HPD is shortest but can be a union for multimodal posteriors) — there is no default that is free of a loss.
</details>

## Takeaways

- A point estimate is **line 4 with $\mathcal A=\Theta$**: minimize posterior expected loss. Squared error → **mean**, absolute error → **median**, 0–1 → **mode**; on a skewed posterior these are three different numbers (`2.0000`, `1.6783`, `1.0000` for Gamma(2,1)).
- **Asymmetric loss → a quantile of the posterior predictive.** Newsvendor with underage:overage $= c_u{:}c_o$ orders the $c_u/(c_u+c_o)$-fractile; pinball loss gives any quantile; that is what quantile regression optimizes.
- **MAP = penalized MLE**: Gaussian prior = ridge (= posterior mean here, to machine precision), Laplace prior = lasso. But **sparsity is a property of the mode, not the posterior** — the Laplace posterior *mean* is never exactly zero (`0.1432`, `0.3945`).
- A **credible** interval is a post-data statement about $\theta$; a **confidence** interval is a pre-data guarantee about a procedure. Both are correct; they answer different questions.
- The **two-point uniform**: a valid `0.500` confidence interval whose conditional coverage is $r/(1-r)$ then $1$ — coin-flip when the ancillary gap $R$ is small, **certain** when $R\ge\tfrac12$. Condition on what you saw.
- **Prior-averaged coverage $= 1-\alpha$ exactly** (Fubini): credible intervals are calibrated *averaged over the prior* (`0.9501`), vary pointwise (`0.9715` at $\theta=0$, `0.8827` at $\theta=4$), and degrade gracefully under a wrong prior (`0.8288`). BvM (module 08) makes credible ≈ confidence as $n\to\infty$.
- The transferable reflex: **name the loss, then read the estimate off it; name what you condition on, then read the guarantee off that.**

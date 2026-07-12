# 16. Hierarchical Models: the Crown Jewel

> **Spine.** Partial pooling is a precision-weighted blend of a group's own data and the population — module 05's master shrinkage formula applied at a *second* level, James–Stein made adaptive — and it beats both no-pooling and complete-pooling out of sample.
> **Which line?** Line 1, mostly: the trick is *building the joint* with a shared prior whose parameters are themselves unknown, so that conditioning (line 2) makes the groups inform each other. Prediction (line 3) is where the payoff is measured.
> **Promise.** After this module you can build a hierarchical model, read every group estimate as a shrinkage weight you can compute by hand, sample it without funnel divergences, and say precisely when empirical Bayes is safe and when it lies about its own uncertainty.
> **Prereqs.** Modules 05 (master shrinkage formula, Normal–Normal), 08 (James–Stein = empirical Bayes), 12 (the funnel + non-centering reflex).
> **Runtime.** ~47 s measured (four NUTS fits — eight-schools centered/non-centered plus a half-Normal refit, and the radon model — dominate; JIT compile included).
> **Sources.** Booklet ch. 7 (hierarchical), ch. 9 (small-area estimation & benchmarking); Efron–Morris and Gelman–Hill by concept; C-B §7.2 (Normal–Normal) as the engine.

Eight schools ran a coaching program for the SAT. Each reported a treatment effect $y_j$ (points) and a standard error $\sigma_j$ — the effects range from `28` points down to `-3`, and school A's `28` looks like a triumph. The question that organizes this whole module: **how much should you believe school A's 28?** Not at all (it is one noisy number)? Completely (it is that school's own data)? Or somewhere in between — and if in between, *exactly* where?

That "exactly where" is a weight you can compute by hand. It is module 05's precision-weighted average, wearing one more layer.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "16-hierarchical"                 # this module's figure dir
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

## 16.1 Three models on one axis — the shrinkage picture

The eight schools, verbatim from Rubin's 1981 analysis (the canonical hierarchical dataset):

```python
y8 = np.array([28., 8., -3., 7., -1., 1., 18., 12.])   # estimated effects (points)
s8 = np.array([15., 10., 16., 11.,  9., 11., 10., 18.])  # their standard errors
J = len(y8)
labels = list("ABCDEFGH")

# No pooling: each school stands alone. theta_j = y_j, uncertainty sigma_j.
# Complete pooling: one common effect mu, precision-weighted mean of the y_j.
prec = 1.0 / s8**2
mu_cp = np.sum(y8 * prec) / np.sum(prec)          # M05 master formula, one level
se_cp = np.sqrt(1.0 / np.sum(prec))
print(f"no pooling:       theta_j = y_j, ranging {y8.min():.0f} to {y8.max():.0f}")
print(f"complete pooling: mu = {mu_cp:.2f} +/- {se_cp:.2f}  (all schools identical)")
```

Two extreme stories. **No pooling** treats the eight effects as eight unrelated quantities: school A's estimate is `28`, full stop, standard error `15`. **Complete pooling** declares the coaching effect identical everywhere and averages the eight noisy readings into one number, `mu = 7.69` — a precision-weighted mean, exactly module 05's formula with the schools as pseudo-observations of a common $\mu$. No-pooling ignores that the schools are similar; complete-pooling denies they differ at all. Both are obviously wrong, in opposite directions.

**Partial pooling** is the model that sits between them, and it is built by making the *story* explicit. Each school has its own true effect $\theta_j$, but the eight $\theta_j$ are themselves draws from a common population:
$$
y_j \mid \theta_j \sim N(\theta_j,\ \sigma_j^2), \qquad
\theta_j \mid \mu, \tau \sim N(\mu,\ \tau^2), \qquad
\mu \sim N(0, 10^2),\ \ \tau \sim \text{Half-Cauchy}(5).
$$
This is a *joint* distribution over everything unknown — the eight $\theta_j$, the population mean $\mu$, and the population spread $\tau$ (line 1). The hyperparameter $\tau$ is the whole ballgame: $\tau\to\infty$ recovers no-pooling (the schools tell us nothing about each other), $\tau\to0$ recovers complete-pooling (they are identical). We do not fix $\tau$ — we let the data condition on it (line 2). Fit it with NUTS, non-centered from the start (§16.2 explains why non-centering is mandatory, not optional):

```python
import jax
import jax.numpy as jnp
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
from numpyro.infer.reparam import LocScaleReparam
from numpyro.handlers import reparam
numpyro.set_platform("cpu")

def make_schools(tau_prior):
    """Eight-schools model; tau_prior selects the hyperprior on the population sd."""
    def model(sigma, y=None):
        mu = numpyro.sample("mu", dist.Normal(0., 10.))
        if tau_prior == "cauchy":
            tau = numpyro.sample("tau", dist.HalfCauchy(5.))
        else:
            tau = numpyro.sample("tau", dist.HalfNormal(5.))
        with numpyro.plate("J", len(sigma)):
            theta = numpyro.sample("theta", dist.Normal(mu, tau))   # the hierarchy
            numpyro.sample("y", dist.Normal(theta, sigma), obs=y)
    return model

def fit_schools(tau_prior, noncentered=True, seed=SEED, warmup=800, samples=1000):
    model = make_schools(tau_prior)
    if noncentered:                                   # M12's reflex: flatten the funnel
        model = reparam(model, config={"theta": LocScaleReparam(0)})
    mcmc = MCMC(NUTS(model), num_warmup=warmup, num_samples=samples,
                num_chains=2, chain_method="sequential", progress_bar=False)
    mcmc.run(jax.random.PRNGKey(seed), sigma=s8, y=y8,
             extra_fields=("diverging",))
    return mcmc

mcmc_pp = fit_schools("cauchy", noncentered=True)
post = mcmc_pp.get_samples()
theta_pp = np.asarray(post["theta"])                  # (n_draws, J)
theta_mean = theta_pp.mean(axis=0)
tau_draws = np.asarray(post["tau"])
mu_mean = float(np.asarray(post["mu"]).mean())
print(f"tau posterior: median {np.median(tau_draws):.2f}, mean {tau_draws.mean():.2f}, "
      f"90% CI [{np.percentile(tau_draws,5):.2f}, {np.percentile(tau_draws,95):.2f}]")
print(f"population mean mu posterior mean = {mu_mean:.2f}")
for j in range(J):
    print(f"  school {labels[j]}: y={y8[j]:5.1f}  ->  theta_hat={theta_mean[j]:5.2f}")
```

School A's `28` becomes a posterior mean of `8.23` — pulled almost all the way down to the population mean of `6.49`, because a lone effect measured with standard error `15` carries little precision against seven siblings clustered near `8`. School C's `-3` is pulled *up*. Everyone moves toward the middle, and the noisiest (largest $\sigma_j$) move most. Put all three models on one axis and the story is a picture:

```python
order = np.argsort(y8)
fig, ax = plt.subplots(figsize=(7.5, 4.2))
xs = np.arange(J)
ax.axhline(mu_cp, color="k", ls="--", lw=1.5, label=f"complete pooling = {mu_cp:.1f}")
ax.errorbar(xs - 0.12, y8[order], yerr=s8[order], fmt="o", color="C0",
            capsize=3, label="no pooling  ($y_j \\pm \\sigma_j$)")
ax.plot(xs + 0.12, theta_mean[order], "s", color="C1", ms=8,
        label="partial pooling (posterior mean)")
for k, j in enumerate(order):                          # the shrinkage arrows
    ax.plot([k - 0.12, k + 0.12], [y8[j], theta_mean[j]], color="C1", alpha=0.4)
ax.set_xticks(xs); ax.set_xticklabels([labels[j] for j in order])
ax.set_xlabel("school (sorted by raw effect)"); ax.set_ylabel("treatment effect (points)")
ax.set_title("Partial pooling shrinks each school toward the population — noisiest moves most")
ax.legend(fontsize=9, loc="upper left")
save(fig, "shrinkage")
```

![Eight schools on one axis: no-pooling estimates with error bars fanned from −3 to 28, complete pooling a flat dashed line near 8, and partial-pooling squares pulled inward toward that line, the outermost schools moving farthest.](figures/16-hierarchical/shrinkage.png)

That collapse of the fan toward the population line is *the* hierarchical picture. It is exactly the shrinkage plot the booklet draws for small-area estimation (ch. 9): the raw $\bar y_i$ (booklet's "direct estimator") pulled toward the synthetic estimate $\hat\theta$ (the population fit), each point landing at a composite of the two. Nobody chose the amount of shrinkage; $\tau$ did, by conditioning.

### The $\tau$ prior: half-Cauchy vs half-Normal

With only $J=8$ groups, the data barely constrain the population spread $\tau$ — its posterior has a long right tail and its lower end is pinned near zero. So the hyperprior on $\tau$ is a modeling choice that *shows*, and the two standard defaults deserve a look (module 07's sensitivity discipline, now at the top of the hierarchy):

```python
mcmc_hn = fit_schools("normal", noncentered=True)     # Half-Normal(5) on tau instead
tau_hn = np.asarray(mcmc_hn.get_samples()["tau"])
theta_hn = np.asarray(mcmc_hn.get_samples()["theta"]).mean(axis=0)
print(f"Half-Cauchy(5): tau median {np.median(tau_draws):.2f}, "
      f"95th pct {np.percentile(tau_draws,95):.2f}, school-A theta {theta_mean[0]:.2f}")
print(f"Half-Normal(5): tau median {np.median(tau_hn):.2f}, "
      f"95th pct {np.percentile(tau_hn,95):.2f}, school-A theta {theta_hn[0]:.2f}")
```

The half-Cauchy allows a heavier upper tail for $\tau$ (95th percentile `10.45` vs `8.01`), so it pools slightly *less* on average. But look at what actually matters — the school-A effect moves only from `8.23` to `7.67`, about half a point on a 28-point estimate. **The sensitivity is real in $\tau$ and negligible in the $\theta_j$**: the group estimates are robust to the hyperprior even when the hyperparameter is not. Half-Cauchy is the common default (weakly informative, lets $\tau$ be large if the data insist); half-Normal is a touch more conservative. Neither is "noninformative" — recall from module 07 that the improper $\pi(\tau)\propto 1/\tau$ gives an *improper posterior* here (the booklet flags exactly this variance-component trap in ch. 15). A proper weakly-informative prior on $\tau$ is not optional bureaucracy; it is what makes the model well-posed.

## 16.2 The funnel returns

Module 12 warned you: the eight-schools model *is* Neal's funnel wearing data. Where $\tau$ is small, the $\theta_j$ are crushed into a needle-thin neck around $\mu$; where $\tau$ is large they spread out. A single leapfrog step size cannot survive both regions — the exact stability cliff of module 12, hit locally at the neck. We fit non-centered above without comment. Now pay the demonstration.

**Setup.** Fit the identical model two ways: **centered** (sample $\theta_j\sim N(\mu,\tau)$ directly) and **non-centered** (sample $z_j\sim N(0,1)$ and set $\theta_j=\mu+\tau z_j$, via `LocScaleReparam` — the same handler from module 12).

**Predict.** Both parameterizations describe the identical posterior. Commit before running: does the change of coordinates matter, and if so, how many divergences does the centered version throw — a handful, or dozens? The tempting intuition, again: "NUTS adapts its step size; two coordinate systems for one distribution should sample about the same."

```python
mcmc_c = mcmc_pp                                              # 16.1's fit was non-centered
mcmc_cen = fit_schools("cauchy", noncentered=False, seed=SEED)  # centered version
ndiv_nc = int(mcmc_c.get_extra_fields()["diverging"].sum())
ndiv_cen = int(mcmc_cen.get_extra_fields()["diverging"].sum())
# how deep into the neck does each chain reach? (smallest tau explored)
tau_reach_cen = float(np.asarray(mcmc_cen.get_samples()["tau"]).min())
tau_reach_nc = float(np.asarray(mcmc_c.get_samples()["tau"]).min())
print(f"CENTERED:     divergences = {ndiv_cen:3d};  min tau reached = {tau_reach_cen:.3f}")
print(f"NON-CENTERED: divergences = {ndiv_nc:3d};  min tau reached = {tau_reach_nc:.3f}")
```

**Reconcile.** The centered chain logs `86` divergences — not a handful, dozens — and cannot descend into the neck: its smallest explored $\tau$ bottoms out at `0.723`, because the neck's curvature blows up as $\tau\to0$ and no single adapted step size survives both the wide mouth and the deep neck. The non-centered chain logs `0` divergences and reaches down to $\tau=$ `0.004`, two orders of magnitude deeper. This is module 12's funnel result (there: 13 divergences collapsing to 0 on the bare funnel) reproduced on a real model — same mechanism, same fix, same reparameterization handler. The divergences are not noise to delete; they are the sampler reporting a region it could not survive. Reparameterize, do not discard.

```python
# The funnel made visible: log(tau) against school-A's theta, centered run.
tc = np.asarray(mcmc_cen.get_samples()["tau"])
thc = np.asarray(mcmc_cen.get_samples()["theta"])[:, 0]
dvc = np.asarray(mcmc_cen.get_extra_fields()["diverging"])
fig, ax = plt.subplots(figsize=(6.8, 4))
ax.scatter(thc[dvc == 0], np.log(tc[dvc == 0]), s=6, alpha=0.3, color="C0", label="draws")
ax.scatter(thc[dvc == 1], np.log(tc[dvc == 1]), marker="x", s=40, color="C3",
           label=f"divergence ({ndiv_cen})")
ax.set_xlabel(r"school-A effect $\theta_A$"); ax.set_ylabel(r"$\log \tau$")
ax.set_title("Centered eight-schools: divergences pile up at the funnel neck (small $\\tau$)")
ax.legend(fontsize=9)
save(fig, "funnel")
```

![Scatter of log tau against theta_A for the centered chain; points form a funnel narrowing downward, and red crosses marking divergences cluster along the lower edge where log tau is most negative.](figures/16-hierarchical/funnel.png)

## 16.3 The partial-pooling weight is module 05's formula, one level up

Here is the arithmetic that demystifies "borrowing strength." Condition on the hyperparameters $\mu$ and $\tau$ for a moment. Then each school is a Normal–Normal problem: a prior $\theta_j\sim N(\mu,\tau^2)$ and one observation $y_j\sim N(\theta_j,\sigma_j^2)$. Module 05's master formula gives the posterior mean immediately — a precision-weighted average of the data and the prior:
$$
\mathbb{E}[\theta_j\mid y_j,\mu,\tau] \;=\; w_j\, y_j + (1-w_j)\,\mu,
\qquad
\boxed{\,w_j = \frac{1/\sigma_j^2}{\,1/\sigma_j^2 + 1/\tau^2\,}\,}.
$$
The weight $w_j$ is the school's own precision divided by the total precision — **exactly module 05's shrinkage weight, now with the population variance $\tau^2$ playing the role of the prior variance.** No pooling is $w_j=1$ ($\tau=\infty$: trust your own data); complete pooling is $w_j=0$ ($\tau=0$: trust the population). Partial pooling is whatever $w_j$ the estimated $\tau$ implies. Borrowing strength, made arithmetic:

```python
tau_hat = np.median(tau_draws)                 # plug in the posterior median of tau
w = (1/s8**2) / (1/s8**2 + 1/tau_hat**2)       # M05 precision weight, second level
approx = w * y8 + (1 - w) * mu_mean            # closed-form shrinkage vs the NUTS mean
print(f"tau_hat = {tau_hat:.2f}")
for j in range(J):
    print(f"  school {labels[j]}: w_j={w[j]:.2f}  closed-form {approx[j]:5.2f}  "
          f"NUTS {theta_mean[j]:5.2f}")
```

The closed-form blend (using a single plug-in $\tau$) lands within about a point of the full NUTS posterior mean for every school — the residual gap (largest for extreme schools like A) is precisely the effect of *marginalizing* $\tau$ rather than fixing it, which §16.5 makes into the whole story of empirical Bayes. Notice the weights: school B ($\sigma=10$) keeps $w=$ `0.07` of its own signal, school H ($\sigma=18$, noisiest) keeps only `0.02` and is dragged hardest toward the population. **The shrinkage is heavier exactly where the data are weaker** — the booklet's rule from ch. 9 stated as a fraction: a homogeneous or large-sample cluster barely pools; a noisy or tiny one leans on the ensemble.

This is also the James–Stein estimator you met in module 08, now *adaptive*. James–Stein shrank $d$ unrelated Gaussian means toward zero with a fixed data-estimated factor $\widehat B=(d-2)/\lVert X\rVert^2$; that is empirical Bayes under a $N(0,\tau^2)$ prior with a **point mass hyperprior fixing the population mean at 0**. The hierarchical model here lets the data choose the shrinkage target $\mu$ *and* the amount $\tau$, per-group weighted by each $\sigma_j$. Same move — "admissibility forced frequentists to invent a posterior mean" — with the training wheels off. (No re-derivation; see module 08 for the JS = EB algebra.)

## 16.4 Which end of the spectrum predicts best? — the bake-off

The shrinkage picture is pretty, but the claim that earns hierarchical models their crown is **predictive**: partial pooling generalizes to held-out data better than either extreme. Let us settle it by simulation across many datasets — and, per the feasibility mandate, using only the closed-form conjugate update inside the loop (no MCMC per replication).

**Setup.** Simulate $R$ replications of a $J$-group world. Each group has a true effect $\theta_j\sim N(0,\tau_{\text{true}}^2)$; we see a noisy training reading $y_j\sim N(\theta_j,\sigma^2)$ and must predict an independent held-out reading $\tilde y_j\sim N(\theta_j,\sigma^2)$ from the *same* group. Slide a pooling weight $\lambda$ from 0 (complete pooling: predict every group with the grand mean $\bar y$) to 1 (no pooling: predict group $j$ with its own $y_j$), estimator $\hat\theta_j(\lambda)=\bar y + \lambda(y_j-\bar y)$. Score each $\lambda$ by held-out mean squared error.

**Predict.** Which $\lambda$ minimizes held-out MSE? The naive answer, and name the intuition: *no pooling* ($\lambda=1$) — "to predict a group's future, use that group's own data; borrowing from other groups can only contaminate it with their differences." Commit to that before running.

**Reason:** the unbiasedness reflex — each $y_j$ is an unbiased estimate of its own $\theta_j$, so surely it is the best predictor of that group.

```python
rng_bo = np.random.default_rng(SEED + 1)
Jb, R, sig, tau_true = 6, 4000, 1.0, 1.0
theta = rng_bo.normal(0., tau_true, size=(R, Jb))       # true group effects
ytr = theta + rng_bo.normal(0., sig, size=(R, Jb))      # training reading
yte = theta + rng_bo.normal(0., sig, size=(R, Jb))      # held-out reading
ybar = ytr.mean(axis=1, keepdims=True)

lams = np.linspace(0, 1, 41)
mse = np.array([np.mean((yte - (ybar + lam * (ytr - ybar)))**2) for lam in lams])
lam_star = lams[mse.argmin()]

# Adaptive partial pooling: estimate tau^2 per replication, then the CONJUGATE
# Normal-Normal weight w = tau2/(tau2+sig2) -- module 05's update, inside the loop.
S = ((ytr - ybar)**2).sum(axis=1, keepdims=True)
tau2_hat = np.maximum(S / (Jb - 1) - sig**2, 0.0)       # method-of-moments tau^2
w_bo = tau2_hat / (tau2_hat + sig**2)                   # per-replication shrinkage
est_pp = ybar + w_bo * (ytr - ybar)                     # = w*y_j + (1-w)*ybar
mse_pp = float(np.mean((yte - est_pp)**2))

print(f"held-out MSE  no pooling (lam=1):       {mse[-1]:.3f}")
print(f"held-out MSE  complete pooling (lam=0): {mse[0]:.3f}")
print(f"held-out MSE  best fixed lambda={lam_star:.2f}:     {mse.min():.3f}")
print(f"held-out MSE  adaptive partial pooling: {mse_pp:.3f}")
```

**Reconcile.** No pooling scores `2.019`, complete pooling `1.978` — and **both lose** to partial pooling at `1.691`. The unbiasedness intuition misses the bias–variance trade: $y_j$ is unbiased for $\theta_j$ but *noisy* (variance $\sigma^2$), and shrinking it toward the population trades a little bias for a large variance cut, lowering expected prediction error. The best fixed weight is $\lambda^\star=$ `0.50` (exactly $\tau^2/(\tau^2+\sigma^2)=0.5$, the population signal-to-total-precision ratio, MSE `1.588`), and the *adaptive* estimator — which estimated $\tau^2$ from each dataset of only $J=6$ readings and applied the conjugate weight, knowing nothing about the truth — comes within 7% of that oracle while beating both extremes by a wide margin. Partial pooling is not a compromise you settle for; it is the predictively optimal point, found automatically.

```python
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(lams, mse, color="C0", lw=2)
ax.scatter([0, 1], [mse[0], mse[-1]], color="C3", zorder=5,
           label="the two extremes (both worse)")
ax.axhline(mse_pp, color="C1", ls="--", lw=1.5,
           label=f"adaptive partial pooling = {mse_pp:.3f}")
ax.annotate(f"best $\\lambda$={lam_star:.2f}", (lam_star, mse.min()),
            textcoords="offset points", xytext=(0, 12), ha="center")
ax.set_xlabel(r"pooling weight $\lambda$  (0 = complete pool, 1 = no pool)")
ax.set_ylabel("held-out MSE"); ax.set_title("The predictive sweet spot is in the interior")
ax.legend(fontsize=9)
save(fig, "bakeoff")
```

![Held-out MSE as a U-shaped curve against the pooling weight lambda, minimized near lambda 0.5, with both endpoints marked as higher, and a dashed line showing the adaptive partial-pooling estimator sitting at the minimum.](figures/16-hierarchical/bakeoff.png)

## 16.5 Empirical Bayes vs full Bayes: the interval that lies

Section 16.3 plugged in a single $\tau$ and got the right posterior *means*. That is empirical Bayes: estimate the prior's hyperparameters (here $\tau$, via the marginal likelihood $y_j\sim N(\mu,\sigma_j^2+\tau^2)$), then treat them as known. It is fast, it needs no MCMC, and its point estimates are excellent. It has one flaw, and at $J=8$ the flaw is loud: **it point-estimates the prior, then forgets it was estimated**, so its uncertainty is too small.

```python
from scipy.optimize import minimize

def neg_marg_ll(params):                     # marginal loglik, theta_j integrated out
    mu, log_tau = params
    v = s8**2 + np.exp(2 * log_tau)          # y_j ~ N(mu, sigma_j^2 + tau^2)
    return 0.5 * np.sum(np.log(2 * np.pi * v) + (y8 - mu)**2 / v)

opt = minimize(neg_marg_ll, x0=[8.0, np.log(5.0)], method="Nelder-Mead")
mu_eb, tau_eb = opt.x[0], np.exp(opt.x[1])
if tau_eb < 1e-3:                            # marginal likelihood peaks at the boundary
    var_eb = np.full(J, 1.0 / np.sum(1/s8**2))   # tau=0 -> all theta_j = mu (complete pool)
else:
    var_eb = 1.0 / (1/s8**2 + 1/tau_eb**2)
width_eb = 2 * 1.96 * np.sqrt(var_eb)        # 95% interval width, tau treated as known

# Full Bayes: tau marginalized (the NUTS posterior from 16.1)
lo = np.percentile(theta_pp, 2.5, axis=0)
hi = np.percentile(theta_pp, 97.5, axis=0)
width_fb = hi - lo
print(f"empirical Bayes: tau_hat = {tau_eb:.2f} (marginal MLE, boundary)")
print(f"mean 95% interval width  EB = {width_eb.mean():.2f}   full Bayes = {width_fb.mean():.2f}")
print(f"EB intervals are {100*(1 - width_eb.mean()/width_fb.mean()):.0f}% too narrow on average")
```

The marginal MLE does something dramatic: it hits the boundary, $\hat\tau=$ `0.00`. The eight effects scatter *less* between schools than their own standard errors would produce even if all schools were identical, so the marginal likelihood for $\tau$ peaks at exactly zero — empirical Bayes concludes *complete pooling*, hands every school the same estimate, and hands every school the complete-pool interval. Those 95% intervals average `15.96` points wide, against `21.89` for the full-Bayes intervals that marginalize $\tau$ — **empirical Bayes intervals are `27`% too narrow.** The missing width is the uncertainty in $\tau$ itself: the full-Bayes posterior for $\tau$ (median 2.80, 95th percentile above 10) says the data *cannot rule out* substantial between-school variation, and that spread inflates every interval. Empirical Bayes conditions on one $\hat\tau$ — here a boundary estimate that is almost certainly not the truth — and pretends it was handed down from heaven.

The lesson is a scale rule, not a verdict. **Empirical Bayes is point-estimating the prior; it is fine when the prior is estimated from *many* groups and overconfident when it is estimated from few.** At $J=8$ the hyperparameter uncertainty is a large fraction of the total and EB lies about it. At $J=$ thousands — the large-scale regime of module 18 — the marginal pins $\tau$ down tightly, the plug-in error vanishes, and empirical Bayes becomes not just acceptable but the *right* tool (Efron's large-scale inference). The eight schools is precisely the small-$J$ corner where you must marginalize.

## 16.6 A worked application: radon with a county-level predictor

Eight schools has group-level summaries. Real hierarchical data are raw observations nested in groups, often with predictors at *both* levels — the canonical example being radon measurements in homes nested in counties, with a county-level uranium reading (Gelman–Hill). We synthesize a radon-style dataset: many counties, most with a handful of homes and a few with many, a home-level predictor (floor: basement vs. first floor), and a county-level predictor (soil uranium).

```python
import pandas as pd

rng_r = np.random.default_rng(SEED + 2)
n_cty = 40
u = rng_r.normal(0., 1., size=n_cty)                    # county-level uranium (standardized)
n_homes = rng_r.integers(1, 30, size=n_cty)             # unequal sample sizes -- the point
g0, g1, beta, tau_c, sig_y = 1.3, 0.7, -0.6, 0.50, 0.75
eta = rng_r.normal(0., tau_c, size=n_cty)               # county deviations from the trend
alpha = g0 + g1 * u + eta                               # county intercept = trend + deviation

rows = []
for c in range(n_cty):
    floor = rng_r.integers(0, 2, size=n_homes[c])       # 0 basement, 1 first floor
    y = alpha[c] + beta * floor + rng_r.normal(0., sig_y, size=n_homes[c])
    for f, yy in zip(floor, y):
        rows.append((c, u[c], f, yy))
df = pd.DataFrame(rows, columns=["county", "u", "floor", "y"])
print(f"radon dataset: {len(df)} homes in {n_cty} counties; "
      f"sizes {n_homes.min()}-{n_homes.max()} homes/county")
print(df.head(3).to_string(index=False))
```

The Bayesian model puts a hierarchy on the county intercepts, with the county deviation $\eta_c$ (not the whole intercept) shrunk toward zero around the uranium regression line — a *varying-intercept* model with a group-level predictor:

```python
cidx = df["county"].to_numpy()
u_arr, floor_arr, y_arr = df["u"].to_numpy(), df["floor"].to_numpy(), df["y"].to_numpy()

def radon_model(cidx, u, floor, N_c, y=None):
    g0 = numpyro.sample("g0", dist.Normal(0., 5.))
    g1 = numpyro.sample("g1", dist.Normal(0., 5.))
    b = numpyro.sample("b", dist.Normal(0., 5.))
    tau = numpyro.sample("tau", dist.HalfNormal(1.))
    sigma_y = numpyro.sample("sigma_y", dist.HalfNormal(1.))
    with numpyro.plate("counties", N_c):
        eta = numpyro.sample("eta", dist.Normal(0., tau))     # county deviation
    mu = g0 + g1 * u + eta[cidx] + b * floor
    with numpyro.plate("obs", len(y) if y is not None else len(floor)):
        numpyro.sample("y", dist.Normal(mu, sigma_y), obs=y)

radon_nc = reparam(radon_model, config={"eta": LocScaleReparam(0)})  # non-center, again
mcmc_r = MCMC(NUTS(radon_nc), num_warmup=700, num_samples=800, num_chains=2,
              chain_method="sequential", progress_bar=False)
mcmc_r.run(jax.random.PRNGKey(SEED), cidx=cidx, u=u_arr, floor=floor_arr,
           N_c=n_cty, y=y_arr, extra_fields=("diverging",))
rp = mcmc_r.get_samples()
eta_bayes = np.asarray(rp["eta"]).mean(axis=0)
print(f"radon fit: {int(mcmc_r.get_extra_fields()['diverging'].sum())} divergences; "
      f"g1(uranium) post mean {np.asarray(rp['g1']).mean():.2f} (true {g1}), "
      f"floor {np.asarray(rp['b']).mean():.2f} (true {beta})")
```

The non-centered fit recovers the uranium slope (posterior mean `0.69`, true 0.7) and the floor effect (`-0.68`, true −0.6), with `0` divergences. The hierarchical structure does its work most visibly on the *small* counties: a county with two homes has an unstable raw intercept, and partial pooling drags it toward the uranium regression line, while a county with 25 homes keeps its own estimate. Plot the shrinkage of the county deviations against sample size:

```python
# No-pooling county deviation = mean residual from the fixed-effects trend, per county.
resid = y_arr - (g0 + g1 * u_arr[cidx] + beta * floor_arr)   # around the true trend
eta_nopool = np.array([resid[cidx == c].mean() for c in range(n_cty)])

fig, ax = plt.subplots(figsize=(7, 4))
ax.axhline(0, color="k", ls="--", lw=1, label="uranium regression line ($\\eta=0$)")
for c in range(n_cty):
    ax.plot([n_homes[c], n_homes[c]], [eta_nopool[c], eta_bayes[c]], color="C1", alpha=0.3)
ax.scatter(n_homes, eta_nopool, s=18, color="C0", label="no pooling (county mean residual)")
ax.scatter(n_homes, eta_bayes, s=18, color="C1", label="partial pooling (posterior mean)")
ax.set_xlabel("homes in county"); ax.set_ylabel(r"county deviation $\eta_c$")
ax.set_title("Small counties shrink hardest toward the population trend")
ax.legend(fontsize=9)
save(fig, "radon")
```

![County deviations plotted against county sample size; no-pooling estimates scatter widely for small counties and partial-pooling estimates pull them toward zero, the pull shrinking as sample size grows so large counties barely move.](figures/16-hierarchical/radon.png)

### Mixed-effects models are this, renamed

A frequentist would fit this with a *linear mixed-effects model*: fixed effects for floor and uranium, a random intercept by county. The random-effects "BLUP" (best linear unbiased predictor) of each county deviation is — up to the plug-in-vs-marginalize gap of §16.5 — the same shrinkage estimate. Fit it with `statsmodels` and compare:

```python
import statsmodels.formula.api as smf
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    md = smf.mixedlm("y ~ floor + u", df, groups=df["county"], re_formula="~1")
    mdf = md.fit(method="lbfgs")
re = mdf.random_effects
eta_mixed = np.array([re[c]["Group"] for c in range(n_cty)])
sample_cty = np.argsort(n_homes)[[0, 1, 20, -2, -1]]          # a few small and large
print("county  n_homes   MixedLM eta   Bayes eta")
for c in sample_cty:
    print(f"  {c:3d}    {n_homes[c]:5d}    {eta_mixed[c]:9.3f}   {eta_bayes[c]:8.3f}")
print(f"corr(MixedLM eta, Bayes eta) across counties = "
      f"{np.corrcoef(eta_mixed, eta_bayes)[0,1]:.3f}")
```

The county deviations from `MixedLM` and from the Bayesian posterior means agree to the third decimal — correlation `1.000` across the 40 counties. **"Random effects" is partial pooling with a different vocabulary and a plug-in $\tau$**: the mixed model maximizes the same marginal likelihood to get $\hat\tau$, then computes the same precision-weighted shrinkage. The Bayesian version marginalizes $\tau$ instead (so its intervals are honestly wider at small $J$, per §16.5), but the point estimates are the same object. Small-area estimation, benchmarking (the booklet's ch. 9 requirement that small-area estimates aggregate to a reliable total), varying-intercept models, and "random effects" are four names for the one hierarchy.

## Bridge — booklet ch. 9, small-area estimation

The booklet's ch. 9 is this module in survey-statistics dress. Its "direct estimator" $\bar y_i$ is our no-pooling $y_j$; its "synthetic estimator" $\hat\theta$ is the population fit; its "composite" or "shrinkage" estimator $E(\mu_i\mid y)$ is our partial-pooling posterior mean $w_j y_j + (1-w_j)\hat\theta$, with the identical weight $\lambda_i = \delta^2/(\delta^2+\sigma_i^2/n_i)$ — module 05's precision ratio, term for term. The booklet's rule ("a homogeneous or large cluster needs no pooling; a heterogeneous or tiny one should borrow from the ensemble") is our $w_j$ read off the $\sigma_j$. Its **benchmarking** requirement — that small-area estimates sum to a more-precise overall total — is a constraint we have not imposed but easily could, and it is the practitioner's guard against a mis-specified population model quietly biasing every group. The through-line to module 08 is exact: the booklet's borrowing-strength picture and Efron–Morris's James–Stein baseball are the same estimator, and module 18 will push $J$ from 8 to thousands, at which point empirical Bayes stops lying and shrinkage becomes automatic multiplicity control.

## Pitfalls

- **Fitting the centered parameterization and ignoring the divergences.** Every hierarchical model is a funnel. The centered version diverges at the neck (small $\tau$) and silently biases $\tau$ upward — the chain never visits the strong-pooling region it couldn't integrate through. Non-center with `LocScaleReparam` by reflex; only revert to centered for data-*rich* groups (module 12's caveat).
- **Reporting empirical-Bayes intervals at small $J$.** Plug-in $\hat\tau$ gives good means but intervals that are systematically too narrow — here `27`% too narrow at $J=8$ — because it ignores its own uncertainty about the prior. Marginalize $\tau$ (full Bayes) when groups are few; EB is safe only at scale.
- **An improper prior on $\tau$.** $\pi(\tau)\propto 1/\tau$ (or a flat prior on $\tau$ pushed to the boundary) yields an improper posterior — the booklet's ch. 15 variance-component trap. Use a proper weakly-informative half-Normal or half-Cauchy; with few groups it *matters*, and "let the data decide" is not available when the data barely constrain $\tau$.
- **Concluding "no group effect" from a small $\hat\tau$.** With few groups the marginal likelihood for $\tau$ often peaks at or near zero even when $\tau>0$ — the eight schools' marginal MLE is exactly `0.00`; a point estimate $\hat\tau\approx0$ is not evidence that the groups are identical, only that the data cannot rule it out. The posterior for $\tau$ has a long tail — report it, do not collapse it.
- **Pooling across groups that aren't exchangeable.** Partial pooling assumes the $\theta_j$ are draws from one population (exchangeable given the group-level predictors). If a group is categorically different, shrinking it toward the others imports bias, not strength — add a group-level covariate that explains the difference, or model the heterogeneity, rather than pooling blindly.

## Exercises

**Exercise 16.1 — How far does school A move?**  *(surprising)*
*Setup:* School A reported $y_A=28$ with $\sigma_A=15$. Suppose you were told the population spread is exactly $\tau=10$ and the population mean is $\mu=8$.
*Predict:* Where does school A's posterior mean land — near 28 (its own data), near 8 (the population), or where? Commit to a number.
*Reason:* The "28 is school A's own measurement, so its estimate should stay close to 28" intuition — trusting a single noisy reading over the ensemble.
*Run:*
```python
sig_A, tau_ex, mu_ex = 15.0, 10.0, 8.0
w_A = (1/sig_A**2) / (1/sig_A**2 + 1/tau_ex**2)
print(f"w_A = {w_A:.3f}, posterior mean = {w_A*28 + (1-w_A)*mu_ex:.2f}")
```
<details><summary>Reconcile</summary>

The weight is $w_A=$ `0.308` and the posterior mean is `14.15` — school A is pulled *more than halfway* from 28 down to the population mean of 8, landing near 14. A standard error of 15 is larger than the population spread of 10, so the precision ratio $w_A=(1/225)/(1/225+1/100)=0.31$ keeps less than a third of the raw signal. The single noisy reading loses to the ensemble because the ensemble is, in precision terms, the stronger evidence about where school A's true effect plausibly sits. This is why the marquee 28 evaporates: it was never 28 points of *signal*, it was 28 points of signal-plus-15-points-of-noise, and the hierarchy knows the difference. The naive intuition over-weights the group's own data exactly when that data is least precise.
</details>

**Exercise 16.2 — When does partial pooling stop mattering?**
*Setup:* The bake-off used $\tau_{\text{true}}=1$, $\sigma=1$, so the optimal shrinkage was $\lambda^\star=0.5$. Now make the groups genuinely different: $\tau_{\text{true}}=4$ with $\sigma=1$.
*Predict:* Does the optimal pooling weight move toward no-pooling ($\lambda=1$) or complete-pooling ($\lambda=0$), and roughly to what value?
*Reason:* Testing whether you have internalized $\lambda^\star=\tau^2/(\tau^2+\sigma^2)$ rather than memorizing "0.5."
*Run:*
```python
rng_e = np.random.default_rng(7)
Jb, R, sig, tt = 6, 4000, 1.0, 4.0
th = rng_e.normal(0, tt, (R, Jb)); ytr = th + rng_e.normal(0, sig, (R, Jb))
yte = th + rng_e.normal(0, sig, (R, Jb)); yb = ytr.mean(1, keepdims=True)
lg = np.linspace(0, 1, 41)
m = np.array([np.mean((yte - (yb + L*(ytr-yb)))**2) for L in lg])
print(f"best lambda = {lg[m.argmin()]:.2f}   (tau^2/(tau^2+sig^2) = {tt**2/(tt**2+sig**2):.2f})")
```
<details><summary>Reconcile</summary>

The optimal weight jumps to `0.95`, essentially no-pooling, matching $\tau^2/(\tau^2+\sigma^2)=16/17=$ `0.94`. When the groups are truly spread far apart relative to the measurement noise, borrowing strength from the population buys almost nothing — each group's own reading is already precise *relative to how much groups differ*, so shrinkage would only import bias. Partial pooling adapts to this automatically: the estimated $\tau^2$ comes back large, the weight comes back near 1, and the hierarchical model gracefully *becomes* no-pooling. The crown jewel is not "always shrink hard"; it is "shrink by exactly the precision ratio, whatever that turns out to be" — which at one extreme is no pooling and at the other is complete pooling.
</details>

**Exercise 16.3 — Empirical Bayes as your network's shrinkage layer.**  *(ML/DL bridge)*
*Setup:* A deep net produces per-user embeddings; a downstream head must predict a scalar for each of $J$ users from a handful of noisy interactions each. You consider two designs: (a) fit each user independently (no pooling), (b) shrink every user's estimate toward a learned global mean by a shared factor estimated from all users (empirical Bayes / a learned prior). This is §16.4's bake-off wearing a neural-net hat.
*Predict:* At $J=50$ users with $\sigma=1$ and true between-user spread $\tau=1$, how much held-out MSE does the EB shrinkage layer save over the independent heads, as a percentage?
*Reason:* The "more parameters (independent per-user heads) = more expressive = better" reflex from deep learning — testing whether you see shrinkage as regularization that *improves generalization*, not as underfitting.
*Run:*
```python
rng_x = np.random.default_rng(11)
J, R, sig, tt = 50, 2000, 1.0, 1.0
th = rng_x.normal(0, tt, (R, J)); ytr = th + rng_x.normal(0, sig, (R, J))
yte = th + rng_x.normal(0, sig, (R, J)); yb = ytr.mean(1, keepdims=True)
mse_indep = np.mean((yte - ytr)**2)
S = ((ytr - yb)**2).sum(1, keepdims=True)
w = np.maximum(S/(J-1) - sig**2, 0) / (np.maximum(S/(J-1) - sig**2, 0) + sig**2)
mse_eb = np.mean((yte - (yb + w*(ytr - yb)))**2)
print(f"independent {mse_indep:.3f}  EB-shrunk {mse_eb:.3f}  "
      f"saving {100*(1-mse_eb/mse_indep):.0f}%")
```
<details><summary>Reconcile</summary>

The independent heads score `1.987` held-out MSE; the empirical-Bayes shrinkage layer scores `1.519`, a `24`% reduction — and at $J=50$ the estimated shrinkage is nearly optimal because $\tau$ is pinned down by 50 users, so unlike the $J=8$ schools there is *no* interval penalty to worry about (§16.5's scale rule). This is exactly why "add a per-user bias term regularized toward a global prior" beats "give every user a free independent parameter": the shared prior is a learned regularizer, and estimating its strength from the whole population is empirical Bayes. Weight decay (module 06's Gaussian-prior MAP) is the fixed-strength version of this; a hierarchical prior with a learned $\tau$ is the *adaptive* version — the same crown-jewel move that beat both extremes in the bake-off, now recognizable as a design pattern you have probably already used without the name.
</details>

**Exercise 16.4 — Does the funnel care about the number of groups?**
*Setup:* The centered eight-schools model diverged at the neck. You might guess the funnel is an artifact of having only 8 groups and would disappear with more.
*Predict:* Refit the centered model on a *synthetic* 30-school dataset (drawn from the same population). Do the divergences go away, stay, or get worse?
*Reason:* The "more data fixes pathologies" reflex — testing whether you understand the funnel as a *geometry* problem, not a sample-size problem.
*Run:*
```python
rng_f = np.random.default_rng(3)
Js = 30; sig_s = rng_f.uniform(9, 18, Js)
y_s = rng_f.normal(8 + rng_f.normal(0, 5, Js), sig_s)     # true tau ~ 5
def big(sigma, y=None):
    mu = numpyro.sample("mu", dist.Normal(0., 10.))
    tau = numpyro.sample("tau", dist.HalfCauchy(5.))
    with numpyro.plate("J", len(sigma)):
        theta = numpyro.sample("theta", dist.Normal(mu, tau))
        numpyro.sample("y", dist.Normal(theta, sigma), obs=y)
mc = MCMC(NUTS(big), num_warmup=600, num_samples=600, num_chains=2,
          chain_method="sequential", progress_bar=False)
mc.run(jax.random.PRNGKey(0), sigma=sig_s, y=y_s, extra_fields=("diverging",))
print(f"centered 30-school divergences = {int(mc.get_extra_fields()['diverging'].sum())}")
```
<details><summary>Reconcile</summary>

The centered 30-school model still diverges (`8` divergences) — more groups do *not* fix the funnel. The neck exists because of the $\theta_j$–$\tau$ geometry (each $\theta_j$'s conditional scale is $\tau$, so all $J$ coordinates pinch simultaneously as $\tau\to0$); adding groups adds dimensions to the neck rather than widening it. What fixes the funnel is the coordinate change (non-centering), full stop, at any $J$. The compression: divergences are a diagnosis of *curvature*, and curvature is a property of the parameterization, not of the amount of data. When you see them in a hierarchical model, reach for `LocScaleReparam` before you reach for more data.
</details>

## Takeaways

- **Partial pooling is a precision-weighted blend.** Each group estimate is $w_j y_j + (1-w_j)\mu$ with $w_j = (1/\sigma_j^2)/(1/\sigma_j^2 + 1/\tau^2)$ — module 05's master shrinkage formula at a second level. No pooling is $\tau=\infty$ ($w_j=1$), complete pooling is $\tau=0$ ($w_j=0$); the hierarchy estimates $\tau$ and lands in between, shrinking noisiest groups hardest.
- **It wins out of sample.** In the bake-off, no pooling (`2.019`) and complete pooling (`1.978`) both lost to adaptive partial pooling (`1.691`); the optimal fixed weight was $\lambda^\star=\tau^2/(\tau^2+\sigma^2)$, found automatically by estimating $\tau$. Shrinkage trades a little bias for a large variance cut.
- **James–Stein, made adaptive.** Partial pooling *is* James–Stein (module 08) with the shrinkage target $\mu$ and amount $\tau$ estimated from the data and weighted per-group by $\sigma_j$ — "admissibility forced frequentists to invent a posterior mean," now with the population parameters free.
- **Every hierarchical model is a funnel.** Fit non-centered (`LocScaleReparam`) by default: the centered eight-schools throws `86` divergences and cannot reach small $\tau$ (stuck at `0.723`), the non-centered version throws `0` and reaches `0.004` — module 12's reflex, on a real model, at any number of groups.
- **Empirical Bayes point-estimates the prior.** The eight-schools marginal MLE is $\hat\tau=$ `0.00` (a boundary estimate), and the plug-in intervals come out `27`% too narrow, because EB ignores its uncertainty about $\tau$. Marginalize $\tau$ when groups are few; empirical Bayes is safe and right at scale (module 18), overconfident at $J=8$.
- **"Random effects" is this, renamed.** A mixed-effects model maximizes the same marginal likelihood for $\hat\tau$ and computes the same shrinkage (correlation `1.000` with the Bayesian county deviations); small-area estimation, varying intercepts, and hierarchical priors are one idea in four vocabularies.
- **The $\tau$ prior matters when groups are few.** With $J=8$ the data barely constrain $\tau$, so use a proper weakly-informative half-Cauchy or half-Normal (not $1/\tau$, which is improper here); the $\theta_j$ are robust to the choice even when $\tau$ is not.

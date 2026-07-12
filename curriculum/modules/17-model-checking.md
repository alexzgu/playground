# 17. Model Checking and Comparison  [SIGNATURE S5]

> **Spine.** A model must be able to predict its own data — that is the posterior predictive check; and the evidence a model assigns to the data carries a built-in Occam factor, so complexity control falls out of integration rather than a penalty you tune.
> **Which line?** Line 3 turned into an audit. Prediction is $p(\tilde y\mid y)=\int p(\tilde y\mid\theta)\,p(\theta\mid y)\,d\theta$; a *check* asks whether the data you already have looks like a draw from it, and the *evidence* $p(y)=\int p(y\mid\theta)\,p(\theta)\,d\theta$ is that same integral run before any conditioning — the prior predictive density of the data.
> **Promise.** After this module you can audit a fitted model against its own predictions, score competing models by exact or approximate evidence and understand why integration penalizes flexibility for free, and read a small p-value and a Bayes factor that *disagree* without being confused about which one lied.
> **Prereqs.** Modules 02 (the `condition` engine's denominator = evidence), 03 (entropy/cross-entropy/KL, codelength), 05 (conjugate evidence and predictive distributions); the Bayesian linear model and hierarchical/GLM fits of modules 14–16 by concept. **Runtime.** ~35 s measured on a quiet box (two NUTS fits + JIT dominate; load-dependent on the 2-CPU codespace).
> **Sources.** Booklet ch. 8, 12; BDA3 ch. 6–7 by concept; ISLP ch. 5 (cross-validation).

## 17.1 The two questions

Module 02 built a one-line inference engine and flagged the number it threw away: `condition(prior, likelihood, obs)` divides the observed column by its sum, and that sum is the *evidence* $p(o)=\sum_h p(h)\,p(o\mid h)$. We used it as a normalizer and promised it would come back to grade models. It comes back now. There are exactly two questions you can ask of a fitted model, and this module is one apparatus for each:

1. **Is this model adequate at all?** Can it reproduce the data it was fit on? This is the *posterior predictive check* (PPC) — an internal-consistency audit, run against a single model, needing no rival.
2. **Which of these models is better?** Given two or more candidates, how should the data adjudicate? This is *comparison* — by evidence (exact when you can integrate), by leave-one-out predictive accuracy (LOO/WAIC, when you can only sample), or by a Bayes factor (evidence ratio), each with its own failure mode.

The first question is not a special case of the second. A model can win every comparison in a bad field and still fail its PPC; a model can pass its PPC and still be beaten. Keep them separate.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "17-model-checking"          # this module's figure dir
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

## 17.2 Can the model predict its own data? The posterior predictive check

The posterior predictive check is one idea: after fitting, simulate replicated datasets $y^{\text{rep}}$ from the posterior predictive $p(y^{\text{rep}}\mid y)=\int p(y^{\text{rep}}\mid\theta)\,p(\theta\mid y)\,d\theta$, pick a *test statistic* $T(\cdot)$ that probes the feature you doubt, and ask where the observed $T(y)$ falls in the distribution of $T(y^{\text{rep}})$. If the data you actually have would be a surprising draw from the model that was fit to it, the model is internally inconsistent — it cannot predict itself.

The canonical failure is a Poisson likelihood on overdispersed counts. The Poisson insists variance equals mean; count data in the wild — accidents per district, hits per page, reads per gene — almost always has variance well above the mean. We generate counts from a Negative Binomial with mean 10 and a variance-to-mean ratio of 3, then fit a Poisson.

**Setup.** Sixty counts, true mean 10, true variance ≈ 30. Fit the Poisson conjugately: a $\mathrm{Gamma}(\alpha_0,\beta_0)$ prior on the rate $\lambda$ (β is the rate) gives a $\mathrm{Gamma}(\alpha_0+\sum y,\ \beta_0+n)$ posterior — module 05's Gamma-Poisson machine. The test statistic is the dispersion $T=\mathrm{Var}/\mathrm{mean}$, which the Poisson pins at 1 in expectation.

**Predict.** The Poisson posterior will nail the *mean* of these counts — the conjugate update centers $\lambda$ near the sample mean. So commit: will the posterior predictive check on the dispersion statistic notice anything wrong? Where will $T(y)\approx 3$ land in the replicated $T(y^{\text{rep}})$ distribution — comfortably inside, at the edge, or off the chart?

**Reason.** The naive intuition: "the model fit the data — the mean matches, the fit looks fine, so the check should pass." That intuition conflates *fitting the mean* with *reproducing the data*.

```python
# overdispersed counts: Negative-Binomial, mean 10, Var/mean = 3  (=> r=5, p=1/3)
r_true, mu_true = 5, 10.0
p_nb = r_true / (r_true + mu_true)
n_ct = 60
gen = np.random.default_rng(SEED)
y_ct = gen.negative_binomial(r_true, p_nb, size=n_ct).astype(float)
dispersion = lambda d, ax=-1: d.var(axis=ax) / d.mean(axis=ax)
T_obs = float(dispersion(y_ct))
print(f"counts: mean {y_ct.mean():.3f}, var {y_ct.var():.3f}, T_obs = Var/mean = {T_obs:.3f}")

# Poisson fit, conjugate Gamma-Poisson (weak prior); draw lambda, then replicate
a0, b0 = 1.0, 0.1
an, bn = a0 + y_ct.sum(), b0 + n_ct
S = 4000
lam_post = gen.gamma(an, 1.0 / bn, size=S)                 # posterior lambda draws
yrep_pois = gen.poisson(lam_post[:, None], size=(S, n_ct)) # one dataset per draw
T_pois = dispersion(yrep_pois)
p_pois = float(np.mean(T_pois >= T_obs))
print(f"Poisson posterior lambda mean {lam_post.mean():.3f} (data mean {y_ct.mean():.3f})")
print(f"Poisson PPC: p = P(T_rep >= T_obs) = {p_pois:.4f}; "
      f"replicated T in [{T_pois.min():.2f}, {T_pois.max():.2f}]")
```

**Run + Reconcile.** The Poisson posterior mean for $\lambda$ is `10.240`, essentially the sample mean `10.233` — the fit is, by that measure, perfect. And it fails anyway. The observed dispersion `3.278` sits so far beyond the replicated distribution — every one of the 4,000 replicated datasets has $T^{\text{rep}}$ below about `1.69` — that the posterior predictive p-value is `0.0000`. The Poisson *cannot* manufacture variance beyond its mean, so no setting of $\lambda$, and no averaging over the posterior of $\lambda$, produces data as dispersed as what we saw. Fitting the mean bought nothing; the check reads the feature the model gets wrong. This is the whole value of a PPC: it catches the mismatch the point estimate hides.

Now the fix. Replace the Poisson with a Negative Binomial (a Gamma-Poisson mixture — module 05's overdispersion predictive), fit it with NUTS, and re-run the identical check. We copy the NumPyro/ArviZ idioms verbatim from `tools/ppl_idioms.py`.

```python
import jax
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS, Predictive

def nb_model(N, y=None):
    mu = numpyro.sample("mu", dist.LogNormal(2.0, 1.0))       # positive mean
    conc = numpyro.sample("conc", dist.Exponential(0.5))      # dispersion (conc->inf = Poisson)
    with numpyro.plate("N", N):
        numpyro.sample("y", dist.NegativeBinomial2(mu, conc), obs=y)

mcmc_nb = MCMC(NUTS(nb_model), num_warmup=500, num_samples=500, num_chains=2,
               chain_method="sequential", progress_bar=False)
mcmc_nb.run(jax.random.PRNGKey(SEED), N=n_ct, y=y_ct)
post_nb = mcmc_nb.get_samples()
yrep_nb = np.asarray(Predictive(nb_model, posterior_samples=post_nb)(
    jax.random.PRNGKey(1), N=n_ct)["y"])
T_nb = dispersion(yrep_nb)
p_nb_ppc = float(np.mean(T_nb >= T_obs))
print(f"NB fit: mu {float(post_nb['mu'].mean()):.2f}, conc {float(post_nb['conc'].mean()):.2f}")
print(f"NB PPC: p = {p_nb_ppc:.3f}; replicated T median {np.median(T_nb):.2f}")
```

The Negative Binomial estimates a mean of `10.28` and a finite concentration `3.92` (had the data been truly Poisson, the concentration would have run off to infinity). Its replicated dispersion now brackets the observed value: the PPC p-value is `0.611`, and `3.278` sits near the middle of the replicated $T$ distribution. The check passes — not because we proved the model true, but because we failed to catch it lying.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 3.8), sharey=True)
for ax, Trep, p, name in [(ax1, T_pois, p_pois, "Poisson"),
                          (ax2, T_nb, p_nb_ppc, "Negative Binomial")]:
    ax.hist(Trep, bins=40, color="C1", alpha=0.8,
            label="replicated $T(y^{rep})$")
    ax.axvline(T_obs, color="black", ls="--", lw=2, label=f"$T(y)={T_obs:.2f}$")
    ax.set_xlabel("dispersion  Var/mean")
    ax.set_title(f"{name}  (PPC $p={p:.3f}$)")
    ax.legend(fontsize=9)
ax1.set_ylabel("replicated datasets")
save(fig, "ppc_dispersion")
```

![Two posterior predictive check histograms of the dispersion statistic Var/mean. Left, the Poisson fit: all 4000 replicated datasets cluster near 1, and the observed value 3.28 (dashed line) lies far to the right, off the chart, p=0.000. Right, the Negative Binomial fit: replicated dispersions spread around 3, and the observed value sits near the center, p=0.61.](figures/17-model-checking/ppc_dispersion.png)

**A PPC is a self-consistency audit, not a hypothesis test.** The posterior predictive p-value is not calibrated to a null: the data are used twice (once to fit, once to check), so under a *correct* model it does not have a $\mathrm{Uniform}(0,1)$ distribution — it is conservative, concentrated toward $0.5$. A PPC p near $0.5$ therefore does not certify the model; a PPC p near $0$ or $1$ is a genuine alarm. Read it as "the model cannot reproduce this feature of the data," never as "the model is rejected at level $\alpha$." And it only ever audits the feature your statistic measures: a second statistic — say the fraction of counts above 20, a tail probe — could catch a different defect the dispersion misses (Exercise 17.1). Choose test statistics that target the failures you fear.

## 17.3 Occam for free: evidence peaks where complexity should  [S5]

Now comparison. The cleanest setting is polynomial regression, where we can integrate the evidence *exactly* and watch it do something training error never does.

**Setup.** Data are generated from a degree-3 polynomial on $[-1,1]$ with moderate noise. We fit polynomials of degree $1$ through $9$. Each fit is a Bayesian linear model $y=\Phi\beta+\varepsilon$ with a *proper* Gaussian coefficient prior $\beta\sim N(0,\tau^2 I)$, known noise variance $\sigma^2$, and $\Phi$ the Legendre design matrix (orthogonal columns — numerically stable, no other magic). For this conjugate linear model the evidence is available in closed form. Marginalizing $\beta$ out of $N(y;\Phi\beta,\sigma^2 I)\,N(\beta;0,\tau^2 I)$ leaves a Gaussian in $y$:

$$p(y\mid\text{degree }d)=\int p(y\mid\beta)\,p(\beta)\,d\beta = N\!\big(y;\ 0,\ \underbrace{\sigma^2 I+\tau^2\Phi\Phi^{\top}}_{C_d}\big).$$

This is the *prior predictive density of the data* — line 3 evaluated before any conditioning — and it is exactly module 02's discarded denominator, now for a continuous parameter and a whole dataset. Its logarithm splits into two terms plus a constant shared by every model:

$$\log p(y\mid d)=\underbrace{-\tfrac12\,y^{\top}C_d^{-1}y}_{\text{data fit}}\ \underbrace{-\tfrac12\log|C_d|}_{\text{Occam term}}\ -\ \tfrac{n}{2}\log 2\pi.$$

**Predict.** As the degree climbs from 1 to 9, the training mean squared error — how well the fitted curve passes through the points — can only fall: more parameters fit the noise better. So here is the question every practitioner faces without a validation set: **the training error only goes down, so how would you ever recover the true degree 3?** Commit to what the *evidence* $\log p(y\mid d)$ does as $d$ grows — monotone up (tracking fit), monotone down, or something else?

**Reason.** The naive intuition is the one that makes people reach for cross-validation or an information criterion: "likelihood-type scores reward fit, fit improves with complexity, so evidence must climb with degree — you need an external penalty to stop it." That intuition forgets the second term.

```python
from numpy.polynomial import legendre

def design(x, d):                       # Legendre basis, columns 0..d
    return np.vstack([legendre.Legendre.basis(k)(x) for k in range(d + 1)]).T

def log_evidence(y, Phi, sigma2, tau2):
    """Exact conjugate-linear-model log marginal likelihood, split fit + Occam."""
    n = len(y)
    C = sigma2 * np.eye(n) + tau2 * (Phi @ Phi.T)     # marginal covariance of y
    _, logdet = np.linalg.slogdet(C)
    fit = -0.5 * (y @ np.linalg.solve(C, y))          # -1/2 y' C^{-1} y
    occam = -0.5 * logdet                             # -1/2 log|C|  (the penalty)
    return fit + occam - 0.5 * n * np.log(2 * np.pi), fit, occam

n_poly, sigma = 30, 0.5
sigma2, tau2 = sigma**2, 1.0
true_c = np.array([0.0, 1.0, 0.0, 1.2])               # degree-3 truth (Legendre coeffs)
degrees = range(1, 10)
gen = np.random.default_rng(SEED + 7)

R = 40                                                # average over datasets: single-set peaks are noisy
ev = {d: [] for d in degrees}
mse = {d: [] for d in degrees}
for _ in range(R):
    x = gen.uniform(-1, 1, n_poly)
    y = design(x, 3) @ true_c + gen.normal(0, sigma, n_poly)
    for d in degrees:
        Phi = design(x, d)
        ev[d].append(log_evidence(y, Phi, sigma2, tau2)[0])
        beta = np.linalg.solve(Phi.T @ Phi + (sigma2 / tau2) * np.eye(d + 1), Phi.T @ y)
        mse[d].append(np.mean((y - Phi @ beta)**2))    # posterior-mean (ridge) train MSE
mean_ev = {d: np.mean(ev[d]) for d in degrees}
mean_mse = {d: np.mean(mse[d]) for d in degrees}
best = max(mean_ev, key=mean_ev.get)
for d in degrees:
    print(f"degree {d}: mean log-evidence {mean_ev[d]:7.2f} | mean train MSE {mean_mse[d]:.4f}")
print(f"evidence peaks at degree {best}; train MSE at deg 1 -> 9: "
      f"{mean_mse[1]:.4f} -> {mean_mse[9]:.4f} (monotone down)")
```

**Run + Reconcile.** The evidence does *not* track fit. Averaged over 40 datasets it climbs from degree 1 to a sharp maximum at **degree 3** — the truth — and then falls monotonically. Meanwhile the training MSE does exactly what you predicted, sliding from `0.4200` at degree 1 down to `0.1656` at degree 9, never once rising. Two scores computed from the same fits point in opposite directions past degree 3. The evidence recovered the generating degree with no held-out data, no cross-validation, no AIC/BIC penalty bolted on.

Why? The decomposition. Look at one dataset across three degrees:

```python
x = gen.uniform(-1, 1, n_poly)
y = design(x, 3) @ true_c + gen.normal(0, sigma, n_poly)
for d in (1, 3, 9):
    le, fit, occam = log_evidence(y, design(x, d), sigma2, tau2)
    print(f"  degree {d}: log-ev {le:7.2f} = fit {fit:7.2f} + Occam {occam:6.2f}")
```

The fit term $-\tfrac12 y^{\top}C_d^{-1}y$ improves (rises toward zero) as degree grows — more flexibility, better Mahalanobis fit — but almost all of that gain is *banked by degree 3*; beyond it the curve is already flexible enough and extra degrees add little. The Occam term $-\tfrac12\log|C_d|$ tells the other half: every added degree enlarges $|C_d|$ (a higher-degree prior predictive spreads its mass over more possible datasets), so $-\tfrac12\log|C_d|$ keeps *shrinking*, subtracting more from the evidence at every step. That is the Occam factor, and it is not a penalty anyone chose: **a more flexible model spreads its prior predictive mass thinner, so it assigns less density to any particular dataset it does fit.** A model that can predict everything predicts nothing well. Integration — not regularization — does the accounting. Degree 3 is where the marginal gain in fit last outruns the marginal complexity cost.

```python
fig, ax1 = plt.subplots()
ax1.plot(list(degrees), [mean_ev[d] for d in degrees], "o-", color="C1",
         label="log-evidence (exact)")
ax1.axvline(3, color="black", ls=":", lw=1)
ax1.set_xlabel("polynomial degree"); ax1.set_ylabel("mean log-evidence", color="C1")
ax1.tick_params(axis="y", labelcolor="C1")
ax2 = ax1.twinx(); ax2.grid(False)
ax2.plot(list(degrees), [mean_mse[d] for d in degrees], "s--", color="C0",
         label="train MSE")
ax2.set_ylabel("mean training MSE", color="C0"); ax2.tick_params(axis="y", labelcolor="C0")
ax1.set_title("Evidence peaks at the true degree (3); training error just keeps falling")
save(fig, "occam_evidence")
```

![Log-evidence and training MSE versus polynomial degree, averaged over 40 datasets from a degree-3 truth. The evidence curve rises to a clear maximum at degree 3 and then declines; the training-MSE curve, on the opposite axis, falls monotonically across all degrees. The two curves diverge past degree 3.](figures/17-model-checking/occam_evidence.png)

This is signature experience S5: **complexity control is a consequence of integrating out parameters, not an extra ingredient.** AIC, BIC, and the "$-k$ parameters" penalties of information criteria are all approximations to this integral (BIC is the leading Laplace approximation to $-2\log$ evidence; module 13's Laplace machinery is the derivation). The regularized-regression, bias-variance, and validation-curve stories of modules 14–15 are this same trade-off viewed without the integral. And the connection to module 03 is literal: $-\log p(y)$ is a *codelength*. The evidence is the probability a model assigns to the data, so $-\log_2 p(y)$ is the number of bits to transmit the data using that model as the code — the **minimum description length**. Choosing the model with the highest evidence is choosing the shortest description of the data, model included. Occam's razor is a lossless-compression theorem.

## 17.4 When you can only sample: LOO, WAIC, and cross-validation

Exact evidence needs a tractable integral. For the models you actually fit with NUTS — hierarchical models, GLMs, anything from modules 15–16 — you have posterior *draws*, not a closed form, and the evidence integral is both hard to estimate and notoriously sensitive to the prior (§17.5 is that warning). The robust alternative scores a model by its *out-of-sample predictive accuracy*: the expected log pointwise predictive density on new data, estimated by leave-one-out cross-validation,

$$\mathrm{elpd}_{\text{LOO}}=\sum_{i=1}^{n}\log p(y_i\mid y_{-i}),\qquad p(y_i\mid y_{-i})=\int p(y_i\mid\theta)\,p(\theta\mid y_{-i})\,d\theta.$$

Refitting the model $n$ times (drop each point, recompute the posterior) is the honest but expensive way. **PSIS-LOO** — Pareto-smoothed importance sampling LOO (Vehtari–Gelman–Gabry) — estimates all $n$ leave-one-out predictive densities from a *single* fit, importance-reweighting the full posterior to approximate each $p(\theta\mid y_{-i})$; the importance weights are module 09's, and their Pareto-tail diagnostic $\hat k$ is the same silent-failure alarm. **WAIC** is a closely related sample-based estimate from the same log-likelihood array. We check PSIS-LOO against brute force on a model small enough to refit exactly.

```python
from numpyro.infer import log_likelihood as np_loglik
import arviz as az
import xarray as xr

n_loo = 25
gen = np.random.default_rng(SEED + 3)
y_loo = gen.normal(0.5, 1.0, size=n_loo)

def normal_model(N, y=None):
    mu = numpyro.sample("mu", dist.Normal(0.0, 10.0))
    sigma = numpyro.sample("sigma", dist.HalfNormal(5.0))
    with numpyro.plate("N", N):
        numpyro.sample("y", dist.Normal(mu, sigma), obs=y)

mcmc_l = MCMC(NUTS(normal_model), num_warmup=500, num_samples=500, num_chains=2,
              chain_method="sequential", progress_bar=False)
mcmc_l.run(jax.random.PRNGKey(SEED), N=n_loo, y=y_loo)

# idioms-file route: compute log-lik in numpyro, cast to NUMPY, attach for az.loo
idata = az.from_numpyro(mcmc_l)
ll = np.asarray(np_loglik(normal_model, mcmc_l.get_samples(), N=n_loo, y=y_loo)["y"])
idata["log_likelihood"] = xr.Dataset(
    {"y": (("chain", "draw", "y_dim"), ll.reshape(2, 500, n_loo))})
loo = az.loo(idata)
print(f"PSIS-LOO elpd = {float(loo['elpd']):.2f}  (p_loo = {float(loo['p']):.2f})")

# WAIC by hand from the same log-lik array (arviz 1.x dropped az.waic):
#   lppd_i = log mean_s p(y_i|theta_s);  p_waic_i = Var_s log p(y_i|theta_s)
from scipy.special import logsumexp
ll_flat = ll.reshape(-1, n_loo)                       # (draws, points)
lppd = logsumexp(ll_flat, axis=0) - np.log(ll_flat.shape[0])
p_waic = ll_flat.var(axis=0)
elpd_waic = float((lppd - p_waic).sum())
print(f"WAIC     elpd = {elpd_waic:.2f}  (p_waic = {p_waic.sum():.2f})")
```

Now the exact brute-force LOO and 10-fold CV, both in closed form because a Normal model with a weak Normal-Inverse-Gamma prior has a Student-t posterior predictive (module 05):

```python
def nig_post(ys, m0=0.0, k0=0.01, a0=0.01, b0=0.01):
    n = len(ys); yb = ys.mean()
    kn = k0 + n; mn = (k0 * m0 + n * yb) / kn
    an = a0 + n / 2
    bn = b0 + 0.5 * np.sum((ys - yb)**2) + 0.5 * k0 * n * (yb - m0)**2 / kn
    return mn, kn, an, bn

def log_pred(y_new, ys):                      # Student-t predictive density (M05)
    mn, kn, an, bn = nig_post(ys)
    scale = np.sqrt(bn * (kn + 1) / (an * kn))
    return stats.t.logpdf(y_new, df=2 * an, loc=mn, scale=scale)

elpd_bf = sum(log_pred(y_loo[i], np.delete(y_loo, i)) for i in range(n_loo))  # exact LOO
K = 10
folds = np.array_split(gen.permutation(n_loo), K)
elpd_cv = sum(log_pred(y_loo[f], y_loo[np.setdiff1d(np.arange(n_loo), f)]).sum()
              for f in folds)
print(f"brute-force LOO elpd = {elpd_bf:.2f}   (exact, n={n_loo} refits)")
print(f"10-fold CV      elpd = {elpd_cv:.2f}")
```

PSIS-LOO reports `-41.76`, brute-force exact LOO `-41.94`, and 10-fold CV `-41.63` — agreement to within a few tenths of a nat across the whole dataset, and PSIS bought it from one fit instead of 25. WAIC lands at `-41.66`, essentially on top of PSIS-LOO. The effective number of parameters `p_loo = 2.69` sits just above the true 2 (mean and variance) — small-sample noise in a sample-size-corrected count of the things the data had to estimate.

When does LOO beat evidence, and when the reverse? Evidence answers "which model would have predicted this dataset a priori" — it is the right score when you believe one of your candidates is *true* (the **M-closed** setting) and you trust your priors, and it is exact and prior-sensitive. LOO answers "which model predicts a held-out point best" — it is the right score when all your models are wrong and you only want the best predictor (the **M-open** setting, module 18's theme), it is robust to vague priors, but it is noisier and can be unstable when a single point dominates (a high $\hat k$). Neither is universally correct; they answer different questions, and knowing which question you are in is the skill.

## 17.5 Small p, large Bayes factor: the Lindley disagreement

A **Bayes factor** is a ratio of evidences, $\mathrm{BF}_{01}=p(y\mid H_0)/p(y\mid H_1)$ — the posterior-odds update between two models (module 02's likelihood ratio, now with the parameters integrated out). It inherits the Occam factor, and that inheritance produces the single most misunderstood result in statistics.

**Setup.** A large study: $n=10^4$ observations, known $\sigma=1$, sample mean $\bar x=0.0258$ (printed below). Test $H_0:\theta=0$ against $H_1:\theta\sim N(0,\tau^2)$. The classical z-test gives $z=\bar x\sqrt n/\sigma$; the Bayes factor for a point null versus a Normal alternative is a clean two-Gaussian ratio (write $s^2=\sigma^2/n$ for the variance of $\bar x$):

$$\mathrm{BF}_{01}=\frac{N(\bar x;0,s^2)}{N(\bar x;0,s^2+\tau^2)}=\sqrt{\frac{s^2+\tau^2}{s^2}}\ \exp\!\Big(-\tfrac12\bar x^2\big(\tfrac1{s^2}-\tfrac1{s^2+\tau^2}\big)\Big).$$

**Predict.** The z-test will call this "significant" ($p\approx 0.01$). Commit: what does $\mathrm{BF}_{01}$ say as the alternative's prior width $\tau$ widens from $0.5$ to $5$ — does the Bayes factor also favor $H_1$ (agreeing with the p-value), stay flat, or move toward $H_0$?

**Reason.** The intuition to be broken: "a significant p-value and a Bayes factor are two dialects for the same evidence — they must agree in direction." They are not, and this is where they visibly split.

```python
sig, N, xbar = 1.0, 10_000, 0.0258
s2 = sig**2 / N
z = xbar / np.sqrt(s2)
p_two = 2 * (1 - stats.norm.cdf(abs(z)))
print(f"xbar = {xbar:.4f},  z = {z:.3f},  two-sided p = {p_two:.4f}")
taus = np.array([0.5, 1.0, 2.0, 5.0])
BF01 = np.sqrt((s2 + taus**2) / s2) * np.exp(-0.5 * xbar**2 * (1/s2 - 1/(s2 + taus**2)))
for t, bf in zip(taus, BF01):
    print(f"  tau = {t:>3}:  BF01 = {bf:5.2f}  (evidence for H0 over H1)")
```

**Run + Reconcile.** The p-value is `0.0099` — "significant," reject $H_0$. The Bayes factor points the *other way and gets more emphatic the vaguer the alternative*: $\mathrm{BF}_{01}=`1.80`$ at $\tau=0.5$ rising to `17.93` at $\tau=5$ — from mild to nearly 18-to-1 odds *for* the null. This is **Lindley's paradox**. The dissection: a diffuse alternative spreads its prior over a wide range of effect sizes, most of them much larger than the tiny $\bar x=0.0258$ actually observed. Under $H_1$ the data are surprising — the alternative "expected" a big effect and got a tiny one — so $H_1$ pays a steep Occam tax for its flexibility (the $\sqrt{(s^2+\tau^2)/s^2}$ factor, which grows with $\tau$). The point null, predicting exactly the small deviation that occurred, is not penalized. The p-value only asks "is $\bar x$ far from 0 relative to its standard error?" ($z=2.58$, yes); the Bayes factor asks "which model predicted this dataset better?" and a vague $H_1$ predicted it *worse* than the sharp $H_0$.

The honest caveat is right there in the table: $\mathrm{BF}_{01}$ runs from `1.80` to `17.93` — a tenfold swing — driven entirely by $\tau$, a prior input the data never sees. Under a point-null Bayes factor the alternative's prior width does not wash out with $n$; it sets the Occam tax directly. This prior-sensitivity is why point-null Bayes factors demand a defensible, not a "vague," alternative — and why we revisit the machinery in module 26. As $\tau\to\infty$ the factor favors $H_0$ without bound regardless of the data (Exercise 17.3): an infinitely vague alternative is infinitely penalized. The frequentist p-value and the Bayesian factor are not two roads to one verdict here; they answer different questions, and on large-$n$, small-effect data they answer them differently.

## 17.6 What a p-value is worth: calibration and replication

The last audit turns the tool on itself. Under a true null a p-value is $\mathrm{Uniform}(0,1)$ by construction — that is what "calibrated" means and what a PPC p-value notably is *not*. Under a real effect the distribution shifts toward 0, and the fraction below $0.05$ is the test's power. Simulating both, and then one uncomfortable consequence for replication:

```python
gen = np.random.default_rng(SEED + 11)
M = 40_000
z0 = gen.normal(0.0, 1.0, M)                      # H0 true: test statistic ~ N(0,1)
p0 = 2 * (1 - stats.norm.cdf(np.abs(z0)))
print(f"under H0: P(p<0.05) = {np.mean(p0 < 0.05):.4f} (=alpha), mean p = {p0.mean():.3f} (uniform)")
for eff in (1.0, 2.0, 3.0):                        # true noncentrality (effect / SE)
    pe = 2 * (1 - stats.norm.cdf(np.abs(gen.normal(eff, 1.0, M))))
    print(f"  true effect {eff} SE: power P(p<0.05) = {np.mean(pe < 0.05):.3f}, "
          f"median p = {np.median(pe):.4f}")

# a study reports p = 0.049 (z = 1.97). If that observed effect equalled the truth,
# what is the chance an identical-size replication also reaches p < 0.05?
z_obs = stats.norm.ppf(1 - 0.049 / 2)
rep = gen.normal(z_obs, 1.0, M)
print(f"z at p=0.049 is {z_obs:.3f}; replication P(p<0.05) if true effect = observed "
      f"= {np.mean(2*(1-stats.norm.cdf(np.abs(rep))) < 0.05):.3f}")
```

Under the null the p-value is flat: `0.0488` of simulations fall below 0.05, mean `0.501`. Under a two-standard-error effect the test has just `0.514` power and a median p of `0.0457` — a real, moderate effect produces a *coin-flip* significant result and p-values scattered all across $(0,1)$. And the replication punchline: a first study that squeaks in at $p=0.049$ corresponds to a test statistic of `1.969`; even in the optimistic world where the true effect *equals* that observed estimate (ignoring the winner's-curse inflation of module 18), an identical replication reaches $p<0.05$ only `0.499` of the time. A just-significant result is, at best, a coin flip to replicate. The p-value near the threshold is not weak because p-values are bad; it is weak because $p=0.049$ carries almost no information — the likelihood is nearly flat between $H_0$ and the estimate. This is the same lesson the Bayes factor taught in §17.5, read off the sampling distribution instead of the evidence.

```python
fig, ax = plt.subplots()
ax.hist(p0, bins=40, density=True, color="C0", alpha=0.6, label="under $H_0$ (uniform)")
ax.hist(2*(1-stats.norm.cdf(np.abs(gen.normal(2.0, 1.0, M)))), bins=40, density=True,
        color="C1", alpha=0.6, label="under real effect (2 SE)")
ax.axvline(0.05, color="black", ls="--", lw=1.5, label="$p=0.05$")
ax.set_xlabel("p-value"); ax.set_ylabel("density"); ax.set_xlim(0, 1)
ax.set_title("p is uniform under $H_0$; a real effect only tilts it — power is 0.52 here")
ax.legend(fontsize=9)
save(fig, "pvalue_calibration")
```

![Two overlaid histograms of p-values. Under H0 the p-values are flat across [0,1] (uniform). Under a real two-standard-error effect the distribution tilts toward zero but still spreads across the whole interval, with only about half its mass below the dashed p=0.05 line.](figures/17-model-checking/pvalue_calibration.png)

## Bridge — the discarded denominator, cashed in three currencies

Module 02's `condition` engine threw away the column sum $p(o)=\sum_h p(h)p(o\mid h)$ and named it evidence. Everything in §17.3–17.5 is that number for richer models: the polynomial evidence $N(y;0,\sigma^2 I+\tau^2\Phi\Phi^\top)$ is $p(o)$ with a continuous $\theta$ integrated out instead of a finite sum; the Bayes factor is a ratio of two such denominators; and the codelength reading $-\log p(y)$ ties it to module 03's cross-entropy and KL — the model that assigns the data the fewest bits wins, which is why cross-entropy training (module 15) and evidence maximization are the same objective seen at two scales. Module 05's conjugate predictive supplied the closed forms (Student-t for LOO, Gamma-Poisson for the Negative Binomial). And for the ML reader: PSIS-LOO is a principled cross-validation, WAIC an information criterion, and evidence maximization is what an ML practitioner approximates every time they tune a regularizer on a validation curve — module 20's Gaussian-process marginal likelihood is this exact Occam mechanism selecting a length scale.

## Pitfalls

- **Reading a PPC p-value as a significance test.** The data are used twice, so it is not calibrated to $\mathrm{Uniform}(0,1)$ — it is conservative. A PPC p near $0.5$ does not validate the model; only an extreme value (near 0 or 1) is informative, and only about the statistic you chose. Pick statistics that probe the failure you fear (overdispersion, zeros, tails, autocorrelation).
- **Trusting a single-dataset evidence peak.** Evidence at one dataset is noisy; the clean S5 peak needed averaging over datasets (or a high-SNR signal). Report the score's variability, not one number.
- **Quoting a Bayes factor without its prior-sensitivity.** A point-null $\mathrm{BF}$ moves an order of magnitude as the alternative's prior width changes (`1.80` to `17.93` here), and that sensitivity never washes out with $n$. Always report the $\mathrm{BF}$ across a range of defensible priors, or don't report it.
- **Confusing "significant" with "large" or "replicable."** At $n=10^4$ a p-value of `0.0099` accompanied an effect of `0.0258`; a just-significant result replicates about half the time even under optimistic assumptions. Significance is a statement about signal-to-noise, not about effect size or evidence for the alternative.
- **Selecting by evidence when you are M-open.** If none of your models is remotely true, the highest-evidence model can still predict badly; LOO/stacking targets predictive accuracy directly. Match the tool to whether you believe a candidate is true.

## Exercises

**Exercise 17.1 — The check that passes on the wrong statistic.**
*Setup:* The overdispersed counts of §17.2, refit with the *Poisson* model. Instead of the dispersion $\mathrm{Var}/\mathrm{mean}$, check the model with the test statistic $T=\text{sample mean}$.
*Predict:* Will the Poisson PPC on the mean statistic fail (p near 0 or 1) as it did on dispersion, or pass (p near 0.5)?
*Reason:* A PPC only audits the feature its statistic measures; the Poisson was fit to match the mean.
*Run:*
```python
T_mean_obs = y_ct.mean()
T_mean_rep = yrep_pois.mean(axis=1)
p_mean = np.mean(T_mean_rep >= T_mean_obs)
print(f"Poisson PPC on the MEAN: p = {p_mean:.3f}  (dispersion PPC was {p_pois:.3f})")
```
<details><summary>Reconcile</summary>

The mean-statistic PPC passes comfortably (p near 0.5), while the same fitted model failed the dispersion check at `0.0000`. Nothing about the model changed — only the lens. The conjugate Poisson fit centers $\lambda$ on the sample mean, so of course replicated datasets reproduce the mean; the model's flaw is entirely in the second moment, invisible to a first-moment probe. The lesson generalizes past this example: a PPC is only as sharp as the discrepancy you point it at, and a model can pass any number of checks while failing the one that matters. Choose test statistics that target the failure mode you actually worry about — for counts, dispersion and zero-inflation; for regression, residual autocorrelation and tail behavior — not the quantities you already fit.
</details>

**Exercise 17.2 — Evidence, LOO, and the validation curve (ML bridge).**
*Setup:* You train a model and read two numbers: training loss (monotone down in capacity) and validation loss (U-shaped). You have just seen evidence (peaks at the true degree) and $\mathrm{elpd}_{\text{LOO}}$ (out-of-sample predictive density).
*Predict:* Which pairs up with which? Is the ML "validation loss" curve closer in spirit to the *evidence* or to $-\mathrm{elpd}_{\text{LOO}}$, and does the training loss correspond to either?
*Reason:* Evidence is a prior-predictive score (before seeing data); LOO is a held-out predictive score (after fitting on the rest) — one of those is exactly what a validation set estimates.
*Run:*
```python
# reuse the polynomial machinery: compare -evidence and an exact LOO-style score by degree
gen2 = np.random.default_rng(SEED + 99)
x = gen2.uniform(-1, 1, n_poly); y = design(x, 3) @ true_c + gen2.normal(0, sigma, n_poly)
for d in (1, 3, 9):
    Phi = design(x, d)
    neg_ev = -log_evidence(y, Phi, sigma2, tau2)[0]
    # crude LOO: leave-one-out ridge predictive log-density, summed
    loo_d = 0.0
    for i in range(n_poly):
        tr = np.delete(np.arange(n_poly), i)
        A = Phi[tr].T @ Phi[tr] + (sigma2/tau2)*np.eye(d+1)
        b = np.linalg.solve(A, Phi[tr].T @ y[tr])
        loo_d += stats.norm.logpdf(y[i], Phi[i] @ b, sigma)
    print(f"degree {d}: -log evidence {neg_ev:7.2f} | -elpd_LOO {-loo_d:7.2f}")
```
<details><summary>Reconcile</summary>

Both $-\log$ evidence and $-\mathrm{elpd}_{\text{LOO}}$ are U-shaped in degree with their minimum at 3 — they are the two principled cousins of the ML validation curve, while the *training* loss (the ridge MSE that fell monotonically) corresponds to neither: it is the in-sample fit that overfitting inflates. The tightest analogy is validation-loss $\leftrightarrow -\mathrm{elpd}_{\text{LOO}}$: both hold out data and score prediction on it, and $k$-fold cross-validation is literally what an ML practitioner runs. Evidence gets to the same answer by a different route — it scores the model *before* conditioning, integrating over the prior — which is why it can be computed with no held-out split at all but pays with prior-sensitivity. The unification worth keeping: "tune the hyperparameter on a validation set," "maximize the marginal likelihood," and "pick the shortest codelength" are three implementations of one idea, complexity control by predictive accuracy.
</details>

**Exercise 17.3 — Lindley to the limit.**
*Setup:* The §17.5 Bayes factor with $\bar x=0.0258$, $n=10^4$, $\sigma=1$, but now sweep the alternative's prior width $\tau$ up toward very large values.
*Predict:* As $\tau\to\infty$ (an ever-vaguer alternative), does $\mathrm{BF}_{01}$ approach a finite limit, settle at 1, or grow without bound in favor of $H_0$?
*Reason:* The Occam-tax factor $\sqrt{(s^2+\tau^2)/s^2}$ grows with $\tau$ while the exponential term saturates — one wins.
*Run:*
```python
for t in (5, 20, 100, 1000):
    bf = np.sqrt((s2 + t**2)/s2) * np.exp(-0.5*xbar**2*(1/s2 - 1/(s2 + t**2)))
    print(f"tau = {t:>5}:  BF01 = {bf:8.1f}")
```
<details><summary>Reconcile</summary>

$\mathrm{BF}_{01}$ grows without bound: the wider the alternative, the more decisively the Bayes factor favors the null, *regardless of the data*. The exponential term converges to a constant $\exp(-z^2/2)$ as $\tau\to\infty$, but the $\sqrt{(s^2+\tau^2)/s^2}\approx\tau/s$ prefactor diverges linearly. So you can make the evidence for $H_0$ arbitrarily strong by choosing a vague enough alternative — a genuinely alarming sensitivity, and the reason "let the prior be uninformative" is a *trap* for point-null Bayes factors specifically (it is harmless for estimation, where the prior washes out — module 07). The resolution is not to abandon Bayes factors but to refuse vague alternatives: the prior on the effect under $H_1$ is a real modeling commitment about what effect sizes are plausible, and pretending indifference by sending $\tau\to\infty$ smuggles in the strongest possible bias toward the null. Module 26 returns to this with the calibrated-Bayes stance.
</details>

## Takeaways

- **A posterior predictive check asks whether a model can reproduce its own data.** Simulate replicated datasets, compare a targeted test statistic $T(y)$ to $T(y^{\text{rep}})$; the Poisson-on-overdispersed-counts check fails at dispersion (p `0.0000`) while the Negative Binomial passes (p `0.611`). It is a self-consistency audit, *not* a calibrated hypothesis test — the data are used twice.
- **Evidence is the prior predictive density of the data**, $p(y)=\int p(y\mid\theta)p(\theta)d\theta$ — module 02's discarded denominator — and it carries a built-in Occam factor: log-evidence peaks at the true polynomial degree (3) while training error falls monotonically (`0.4200`→`0.1656`). Complexity control is a consequence of integration, not a separate penalty. [S5]
- **$-\log p(y)$ is a codelength.** Maximum evidence = minimum description length = shortest data-plus-model encoding; the Occam razor is a compression theorem, and AIC/BIC are its approximations.
- **When you can only sample, score predictive accuracy.** PSIS-LOO (`-41.76`) matches exact brute-force LOO (`-41.94`) and 10-fold CV (`-41.63`) from a single fit; WAIC agrees (`-41.66`). Evidence suits M-closed problems, LOO/stacking suits M-open.
- **A Bayes factor can favor $H_0$ while the p-value rejects it — Lindley's paradox.** At $n=10^4$, $\bar x=0.0258$ ($p=`0.0099`$), $\mathrm{BF}_{01}$ runs `1.80`→`17.93` as the alternative widens $\tau=0.5$→$5$, and diverges as $\tau\to\infty$. A diffuse alternative pays an Occam tax the point null does not; the prior width never washes out.
- **A p-value is calibrated ($\mathrm{Uniform}$) under $H_0$ and only tilted under a real effect** — a 2-SE effect gives power `0.514` and median p `0.0457`. A just-significant $p=0.049$ replicates about `0.499` of the time even optimistically: significance is signal-to-noise, not evidence for the alternative or a promise of replication.
- **Model checking and model comparison are different questions.** One model against itself (PPC) versus models against each other (evidence / LOO / BF); a model can pass one and fail the other. Run both.

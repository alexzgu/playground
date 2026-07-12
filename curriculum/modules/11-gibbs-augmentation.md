# 11. Gibbs Sampling and Data Augmentation

> **Spine.** Sample one full conditional at a time; posterior correlation is the enemy, and augmentation invents the latents that restore conjugacy.
> **Which line?** Line 2 (inference = conditioning), industrialized. When the *joint* posterior is intractable but every *full conditional* $p(\theta_i\mid\theta_{-i},y)$ is a known distribution, you condition on one block at a time and cycle — a Markov chain whose stationary law is the exact posterior.
> **Promise.** After this module you can derive a model's full conditionals, build a Gibbs sampler and *audit it for correctness* against a known exact posterior, quantify the correlation that cripples mixing (for a bivariate-normal Gibbs the lag-1 autocorrelation is $\rho^2$, exactly), and use latent-variable augmentation — missing data included, as latents you failed to record — to make probit, missing-data, and mixture problems conjugate one block at a time.
> **Prereqs.** Modules 00 (four lines), 04 (likelihood, `nig_post`, sufficiency), 05 (conjugate library, the NIG posterior, the Gaussian conditioning toolkit), 09–10 (Monte Carlo, Markov chains and Metropolis–Hastings — Gibbs is a special case).
> **Runtime.** ~15 s.
> **Sources.** Booklet ch. 10 (Gibbs), 11 (data augmentation, Rao-Blackwell), 13 (mixtures/latent); C-B §4.4 (conditional and marginal distributions); Albert–Chib (1993) by concept; Rubin, *Multiple Imputation* by concept.

The four lines (module 00): **a model is a joint $p(\text{unknowns},\text{knowns})$; inference is conditioning; prediction is marginalization; a decision minimizes posterior expected loss.** Module 05 conditioned in closed form when prior and likelihood were conjugate. Module 10 built a Metropolis–Hastings chain for when they are not. Gibbs sampling is the sweet spot between them: the *joint* posterior $p(\theta\mid y)$ has no closed form, yet each parameter's *full conditional* — its distribution given the data and **all the other parameters** — is a tidy conjugate update you already know how to make. You never solve the hard joint problem; you solve a sequence of easy one-block problems and let the Markov chain stitch them into joint samples.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "11-gibbs-augmentation"          # this module's figure dir
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

# Inverse-Gamma sampling WITHOUT scipy's slow per-call .rvs: if X ~ IG(a, b)
# (course convention: scipy invgamma(a=a, scale=b)) then 1/X ~ Gamma(shape=a,
# rate=b), and numpy's gamma takes scale = 1/rate. This is the workhorse draw
# for every variance parameter below — vectorized and ~100x faster in a loop.
def rinvgamma(a, b, rng, size=None):
    return 1.0 / rng.gamma(a, 1.0 / b, size=size)
```

## 11.1 Gibbs is Metropolis–Hastings that never rejects

The algorithm is one line. To sample the joint $p(\theta_1,\dots,\theta_d\mid y)$, cycle through the components; to update $\theta_i$, draw it from its **full conditional** holding everyone else fixed:
$$\theta_i^{(t+1)} \sim p\big(\theta_i \,\big|\, \theta_1^{(t+1)},\dots,\theta_{i-1}^{(t+1)},\,\theta_{i+1}^{(t)},\dots,\theta_d^{(t)},\, y\big).$$
One full sweep over all $d$ components is one Gibbs iteration. Why does cycling through conditionals target the *joint*? Because a Gibbs update is a Metropolis–Hastings move (module 10) whose proposal *is* the full conditional — and that proposal is accepted with probability exactly 1.

**Derivation.** Propose $\theta_i' \sim q(\theta_i'\mid\theta) = p(\theta_i'\mid\theta_{-i})$ (the full conditional), leaving $\theta_{-i}$ fixed. The MH acceptance ratio is
$$\alpha = \frac{p(\theta_i',\theta_{-i})\,q(\theta_i\mid\theta')}{p(\theta_i,\theta_{-i})\,q(\theta_i'\mid\theta)}
= \frac{p(\theta_i'\mid\theta_{-i})\,p(\theta_{-i})\;p(\theta_i\mid\theta_{-i})}{p(\theta_i\mid\theta_{-i})\,p(\theta_{-i})\;p(\theta_i'\mid\theta_{-i})} = 1,$$
using $p(\theta_i,\theta_{-i}) = p(\theta_i\mid\theta_{-i})\,p(\theta_{-i})$ and that the reverse proposal $q(\theta_i\mid\theta') = p(\theta_i\mid\theta_{-i})$ shares the unchanged $\theta_{-i}$. Every factor cancels. **Gibbs is the MH sampler you get for free when you can sample the conditionals: no step size to tune, no rejections, but also no ability to move two correlated components at once — the flaw that §11.4 turns into the module's cautionary tale.** Check the algebra numerically on a bivariate normal, where the conditional is a Gaussian:

```python
# Bivariate normal target N(0, [[1,rho],[rho,1]]). Verify a Gibbs proposal
# (draw x' from x|y, the full conditional) has MH acceptance ratio exactly 1.
rho_chk = 0.8
def log_joint(x, y, r=rho_chk):
    return -0.5 * (x*x - 2*r*x*y + y*y) / (1 - r*r)
def cond_x(xv, yv, r=rho_chk):                     # x | y ~ N(rho*y, 1-rho^2)
    return stats.norm(r*yv, np.sqrt(1 - r*r)).pdf(xv)

x, y = 0.3, -0.5
xp = rng.normal(rho_chk*y, np.sqrt(1 - rho_chk**2))     # proposal from the full conditional
ratio = (np.exp(log_joint(xp, y)) * cond_x(x, y)) / (np.exp(log_joint(x, y)) * cond_x(xp, y))
print(f"MH acceptance ratio for a Gibbs proposal = {ratio:.10f}")
```

The ratio prints `1.0000000000`: a Gibbs move is a proposal so perfectly matched to the target that rejection never helps. Detailed balance (module 10) holds componentwise, so the joint posterior is the stationary distribution.

## 11.2 The workhorse, and its built-in correctness audit

Take the estimand you have carried since module 04: $y_1,\dots,y_n \sim N(\mu,\sigma^2)$ with **both** parameters unknown. Module 05 solved this in closed form with the Normal–Inverse-Gamma (NIG) conjugate prior, giving the exact posterior tuple `nig_post(data)` returns: $\mu\mid y \sim t$, $\sigma^2\mid y \sim \mathrm{IG}$. We will now solve it a *second* way, by Gibbs, and use module 05's exact answer as an **agreement audit** — the empirical correctness check built into the module.

The NIG prior is $\mu\mid\sigma^2 \sim N(\mu_0,\ \sigma^2/\kappa_0)$ and $\sigma^2 \sim \mathrm{IG}(a_0,b_0)$. Two full conditionals fall out by keeping one parameter fixed and reading off the kernel of the other.

*Conditional for $\mu$ (fix $\sigma^2$).* With $\sigma^2$ known this is exactly module 05's Normal–Normal update (prior variance $\sigma^2/\kappa_0$, data variance $\sigma^2/n$): precisions add, mean is precision-weighted,
$$\mu \mid \sigma^2, y \;\sim\; N\!\left(\frac{\kappa_0\mu_0 + n\bar y}{\kappa_0+n},\ \frac{\sigma^2}{\kappa_0+n}\right).$$

*Conditional for $\sigma^2$ (fix $\mu$).* Collect every factor of $\sigma^2$ in $p(y\mid\mu,\sigma^2)\,p(\mu\mid\sigma^2)\,p(\sigma^2)$ — that is $n$ likelihood terms, one prior term on $\mu$, and the $\mathrm{IG}(a_0,b_0)$ — and the exponent and rate read straight off an inverse-gamma kernel:
$$\sigma^2 \mid \mu, y \;\sim\; \mathrm{IG}\!\left(a_0 + \tfrac{n+1}{2},\ \; b_0 + \tfrac12\textstyle\sum_i (y_i-\mu)^2 + \tfrac{\kappa_0}{2}(\mu-\mu_0)^2\right).$$

Cycle these two draws and you have a sampler. **Predict — honestly.** This demo is an audit, not a trap: agreement is the *expected* outcome, and there is no naive intuition to catch. The commitment worth making is the acceptance criterion — will both Kolmogorov–Smirnov $p$-values (Gibbs marginals against module 05's exact CDFs) clear 0.05? A pass is the deliverable; a systematically tiny $p$-value means a bug in a full conditional. Run it, and overlay the marginals on module 05's exact $t$ and $\mathrm{IG}$.

```python
# Normal(mu, sigma^2), both unknown. Gibbs vs module 05's EXACT NIG posterior.
rng2 = np.random.default_rng(11)
mu0, k0, a0, b0 = 0.0, 1.0, 1.0, 1.0                 # weak NIG prior (nig_post defaults)
n = 40
data = rng2.normal(5.0, 2.0, size=n)                 # truth mu=5, sigma^2=4
xbar = data.mean()

def nig_post(data, mu0=0.0, k0=1.0, a0=1.0, b0=1.0):     # copied from modules 04/05
    n = len(data); xbar = data.mean(); S = ((data - xbar)**2).sum()
    kn = k0 + n
    mn = (k0*mu0 + n*xbar) / kn
    an = a0 + n/2
    bn = b0 + 0.5*S + (k0*n*(xbar - mu0)**2) / (2*kn)
    return kn, mn, an, bn

kn, mn, an, bn = nig_post(data)                      # the exact answer, from module 05
t_scale = np.sqrt(bn / (an*kn))                      # mu | y ~ t_{2an}(mn, t_scale)
print(f"exact NIG posterior:  kn={kn:.0f}  mn={mn:.4f}  an={an:.0f}  bn={bn:.4f}")
print(f"exact marginals:  mu ~ t_df={2*an:.0f}(loc={mn:.4f})   E[sigma^2]={bn/(an-1):.4f}")

# --- Gibbs sampler: alternate the two full conditionals ---
M, burn = 20000, 2000
mu_s = np.empty(M); s2_s = np.empty(M)
mu_mean = (k0*mu0 + n*xbar) / (k0 + n)               # mu-conditional mean is constant here
a_cond  = a0 + (n + 1)/2                              # sigma^2-conditional shape is constant
mu_c, s2_c = xbar, data.var()
for t in range(M):
    mu_c = rng2.normal(mu_mean, np.sqrt(s2_c / (k0 + n)))                 # mu | sigma^2, y
    b_cond = b0 + 0.5*np.sum((data - mu_c)**2) + 0.5*k0*(mu_c - mu0)**2   # sigma^2 | mu, y
    s2_c = rinvgamma(a_cond, b_cond, rng2)
    mu_s[t], s2_s[t] = mu_c, s2_c
mu_s, s2_s = mu_s[burn:], s2_s[burn:]

print(f"Gibbs  E[mu]={mu_s.mean():.4f} (exact {mn:.4f})   E[sigma^2]={s2_s.mean():.4f} (exact {bn/(an-1):.4f})")
print(f"Gibbs sd[mu]={mu_s.std():.4f}   exact t sd={stats.t(2*an, mn, t_scale).std():.4f}")
ks_mu = stats.kstest(mu_s, stats.t(2*an, mn, t_scale).cdf)               # agreement audit
ks_s2 = stats.kstest(s2_s, stats.invgamma(a=an, scale=bn).cdf)
print(f"KS  mu   vs exact t : stat={ks_mu.statistic:.4f}  p={ks_mu.pvalue:.3f}")
print(f"KS sigma^2 vs exact IG: stat={ks_s2.statistic:.4f}  p={ks_s2.pvalue:.3f}")
```

```python
# Figure: the agreement audit -- Gibbs histograms under the exact NIG marginals.
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
mg = np.linspace(mu_s.min(), mu_s.max(), 300)
ax[0].hist(mu_s, bins=80, density=True, color="C7", alpha=0.55, label="Gibbs draws")
ax[0].plot(mg, stats.t(2*an, mn, t_scale).pdf(mg), color="C1", lw=2,
           label=f"exact $t_{{{2*an:.0f}}}$ (module 05)")
ax[0].set_xlabel(r"$\mu$"); ax[0].set_ylabel("density")
ax[0].set_title("Gibbs $\\mu$-marginal = exact Student-$t$"); ax[0].legend()
sg = np.linspace(s2_s.min(), s2_s.max(), 300)
ax[1].hist(s2_s, bins=80, density=True, color="C7", alpha=0.55, label="Gibbs draws")
ax[1].plot(sg, stats.invgamma(a=an, scale=bn).pdf(sg), color="C1", lw=2,
           label="exact $\\mathrm{IG}(a_n,b_n)$ (module 05)")
ax[1].set_xlabel(r"$\sigma^2$"); ax[1].set_ylabel("density")
ax[1].set_title("Gibbs $\\sigma^2$-marginal = exact Inverse-Gamma"); ax[1].legend()
fig.suptitle("Agreement audit: a Gibbs sampler reproduces module 05's closed-form posterior")
save(fig, "agreement-audit")
```

![Two panels. Left: histogram of Gibbs mu-draws with the exact Student-t density riding exactly on top. Right: histogram of Gibbs sigma^2-draws under the exact Inverse-Gamma density, matching in location, width and right skew.](figures/11-gibbs-augmentation/agreement-audit.png)

The Gibbs posterior means are `4.7179` for $\mu$ and `3.4945` for $\sigma^2$, against the exact `4.7184` and `3.4862`; the Gibbs posterior sd of $\mu$ is `0.2935` against the exact $t$-marginal's `0.2916`. The audit is the two Kolmogorov–Smirnov tests comparing each full Gibbs marginal to module 05's exact CDF: statistics `0.0053` (against $t_{42}$, $p=$ `0.688`) and `0.0082` (against $\mathrm{IG}$, $p=$ `0.175`). Both $p$-values are large — the draws are indistinguishable from the closed form. **This is the pattern to internalize: whenever a Gibbs sampler has a conjugate special case, use it to audit the sampler before trusting it on the hard problem where no closed form exists.** The exact answer is not a competitor to the sampler; it is the sampler's unit test — an empirical audit, not a proof. One honesty note on the test itself: KS $p$-values are calibrated for *independent* draws, and MCMC output is autocorrelated. The audit is trustworthy here only because this particular chain mixes near-perfectly (Exercise 11.2 measures its lag-1 autocorrelation at `0.0015` — essentially zero); on a slowly-mixing chain, thin to near-independence or pool multiple chains before reading a KS $p$-value, or it will reject a *correct* sampler.

## 11.3 Bayesian linear regression, one block at a time

The two-block move scales straight to regression, the model behind half the course. With $y = X\beta + \varepsilon$, $\varepsilon\sim N(0,\sigma^2 I)$, priors $\beta\sim N(0,\tau^2 I)$ and $\sigma^2\sim\mathrm{IG}(a_0,b_0)$, the joint posterior over $(\beta,\sigma^2)$ has no clean form — but each conditional is one we own:

- $\beta \mid \sigma^2, y \sim N(m, V)$ with $V = \big(X^\top X/\sigma^2 + I/\tau^2\big)^{-1}$, $m = V X^\top y/\sigma^2$ — module 05's Gaussian conditioning with a Gaussian prior (this is *ridge as a posterior*, module 14's spine, here as one Gibbs block).
- $\sigma^2 \mid \beta, y \sim \mathrm{IG}\big(a_0 + n/2,\ b_0 + \tfrac12\lVert y - X\beta\rVert^2\big)$ — an inverse-gamma read off the residual sum of squares.

Alternate them; recover known coefficients from synthetic data.

```python
# Bayesian linear regression by Gibbs: alternate beta | sigma^2 and sigma^2 | beta.
rng3 = np.random.default_rng(3)
n_reg, p = 150, 3
X = rng3.normal(size=(n_reg, p)); X[:, 0] = 1.0            # intercept column
beta_true = np.array([2.0, -1.5, 0.8]); sig2_true = 1.5
y = X @ beta_true + rng3.normal(0, np.sqrt(sig2_true), size=n_reg)
tau2, a0r, b0r = 100.0, 1.0, 1.0                            # vague prior on beta
XtX, Xty = X.T @ X, X.T @ y

Mr, burnr = 6000, 1000
beta_c, s2_c = np.zeros(p), 1.0
bd = np.empty((Mr, p)); s2d = np.empty(Mr)
for t in range(Mr):
    V = np.linalg.inv(XtX / s2_c + np.eye(p) / tau2)       # beta | sigma^2, y
    m = V @ (Xty / s2_c)
    beta_c = m + np.linalg.cholesky(V) @ rng3.normal(size=p)
    resid = y - X @ beta_c
    s2_c = rinvgamma(a0r + n_reg/2, b0r + 0.5*resid @ resid, rng3)   # sigma^2 | beta, y
    bd[t], s2d[t] = beta_c, s2_c
bd, s2d = bd[burnr:], s2d[burnr:]

ols = np.linalg.solve(XtX, Xty)                            # frequentist cross-check
for j in range(p):
    print(f"beta[{j}]: true={beta_true[j]:+.3f}  Gibbs={bd[:, j].mean():+.4f} "
          f"(sd {bd[:, j].std():.4f})  OLS={ols[j]:+.4f}")
print(f"sigma^2: true={sig2_true:.3f}  Gibbs posterior mean={s2d.mean():.4f}")
```

```python
fig, ax = plt.subplots(1, 3, figsize=(13, 3.6))
for j in range(p):
    ax[j].hist(bd[:, j], bins=70, density=True, color="C7", alpha=0.6)
    ax[j].axvline(beta_true[j], color="k", ls="--", lw=1.5, label="truth")
    ax[j].axvline(bd[:, j].mean(), color="C1", lw=1.5, label="posterior mean")
    ax[j].set_title(f"$\\beta_{j}$"); ax[j].set_xlabel("value")
ax[0].set_ylabel("density"); ax[0].legend(fontsize=9)
fig.suptitle("Gibbs regression: posteriors concentrate on the true coefficients")
save(fig, "regression-recovery")
```

![Three histograms of the coefficient posteriors, each a tight bell straddling the dashed true value, with the posterior mean marked.](figures/11-gibbs-augmentation/regression-recovery.png)

The posteriors concentrate where they should: $\beta_0$ posterior mean `2.1743` (truth 2.0), $\beta_1$ `-1.5846` (truth $-1.5$), $\beta_2$ `0.8982` (truth 0.8), each within one-to-two posterior sds of the truth, and the noise variance recovers to `1.4073` (truth 1.5). The tell that the sampler is right, not just plausible: the Gibbs posterior means match ordinary least squares — `2.1749`, `-1.5865`, `0.8989` — to the third decimal, because with a vague prior the posterior mean *is* the OLS solution. Same "two routes agree" audit as §11.2, now against a frequentist estimator instead of a conjugate formula.

## 11.4 The enemy is correlation: lag-1 autocorrelation is $\rho^2$, exactly

Gibbs never rejects — so what could go wrong? It can only move one coordinate at a time, along the axes. When the posterior is *correlated*, axis-aligned steps are tiny, and the chain crawls. Make this precise on the cleanest case: target $(X,Y)\sim N\!\big(0,\ [[1,\rho],[\rho,1]]\big)$, whose conditionals are $X\mid Y \sim N(\rho Y,\,1-\rho^2)$ and $Y\mid X \sim N(\rho X,\,1-\rho^2)$.

**Setup.** Run the two-step Gibbs sweep and track the $X$-coordinate across sweeps. How correlated are successive $X$ values?

**Predict.** At $\rho=0.99$ the two variables are nearly collinear. Commit to a number: the lag-1 autocorrelation of the $X$-chain — is it around $0.99$, and how much does it degrade the effective sample size versus independent draws: 2×, 10×, or worse?

**Reason.** The naive intuition reads the *target* correlation $\rho$ as the *chain* correlation. But one Gibbs sweep passes through the intermediate $Y$ update, and each conditioning step contracts toward the diagonal by a factor $\rho$, so the per-sweep memory compounds.

**Run — the three-line contraction.** Over one sweep, $Y_{t+1}\mid X_t$ has mean $\rho X_t$, then $X_{t+1}\mid Y_{t+1}$ has mean $\rho Y_{t+1}$. Chaining the conditional expectations,
$$\mathbb{E}[X_{t+1}\mid X_t] = \rho\,\mathbb{E}[Y_{t+1}\mid X_t] = \rho\cdot\rho X_t = \rho^2 X_t.$$
So the $X$-chain is an AR(1) process with autoregressive coefficient $\rho^2$, and since $\mathrm{Var}[X]=1$ its **lag-1 autocorrelation equals $\rho^2$ exactly.** For an AR(1) with coefficient $\phi=\rho^2$, the integrated autocorrelation time is $(1+\phi)/(1-\phi)$, so the effective-sample-size fraction is
$$\frac{\mathrm{ESS}}{M} = \frac{1-\phi}{1+\phi} = \frac{1-\rho^2}{1+\rho^2}.$$

```python
# Bivariate-normal Gibbs at several rho. Measure lag-1 autocorr and ESS fraction.
def gibbs_bvn(rho, N, rng):
    xs = np.empty(N); ys = np.empty(N); x = y = 0.0; sd = np.sqrt(1 - rho*rho)
    for t in range(N):
        x = rng.normal(rho*y, sd)      # x | y
        y = rng.normal(rho*x, sd)      # y | x
        xs[t], ys[t] = x, y
    return xs, ys

def autocorr_fft(x):                   # normalized autocorrelation via FFT
    x = np.asarray(x, float) - np.mean(x); n = len(x)
    f = np.fft.rfft(x, 2*n); ac = np.fft.irfft(f*np.conj(f))[:n]
    return ac / ac[0]

def ess_ips(x, maxlag=4000):           # Geyer initial-positive-sequence ESS
    ac = autocorr_fft(x); maxlag = min(maxlag, len(ac) - 2); s = 0.0
    for k in range(1, maxlag, 2):
        pair = ac[k] + ac[k+1]
        if pair <= 0: break
        s += pair
    return len(x) / (1 + 2*s)

rng4 = np.random.default_rng(7)
essfrac = {}
for rho in (0.9, 0.99):
    xs, _ = gibbs_bvn(rho, 120000, rng4)
    lag1 = autocorr_fft(xs)[1]; ef = ess_ips(xs) / len(xs); essfrac[rho] = ef
    print(f"rho={rho}:  rho^2={rho**2:.4f}   measured lag-1 autocorr={lag1:.4f}   "
          f"ESS/M={ef:.4f}  (theory (1-r2)/(1+r2)={(1-rho**2)/(1+rho**2):.4f})")

# Blocked Gibbs at rho=0.99: draw (X,Y) JOINTLY -> independent samples.
xs99, _ = gibbs_bvn(0.99, 120000, rng4)
ess_single = ess_ips(xs99)
joint = rng4.multivariate_normal([0, 0], [[1, 0.99], [0.99, 1]], size=120000)
ess_block = ess_ips(joint[:, 0])
print(f"rho=0.99  single-site ESS/M={ess_single/120000:.4f}   "
      f"blocked ESS/M={ess_block/120000:.4f}   ratio={ess_block/ess_single:.1f}x")
```

```python
# Figure: the zigzag (why it crawls) + the ESS-collapse law.
rng_zig = np.random.default_rng(70)
rho_z, sd_z = 0.99, np.sqrt(1 - 0.99**2)
px, py = [0.0], [2.6]; x, yv = 0.0, 2.6               # start off the diagonal
for _ in range(45):
    x = rng_zig.normal(rho_z*yv, sd_z); px.append(x); py.append(yv)   # horizontal move
    yv = rng_zig.normal(rho_z*x, sd_z); px.append(x); py.append(yv)   # vertical move

fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
gx = np.linspace(-3.5, 3.5, 120)
GX, GY = np.meshgrid(gx, gx)
Q = (GX**2 - 2*rho_z*GX*GY + GY**2) / (1 - rho_z**2)
ax[0].contour(GX, GY, np.exp(-0.5*Q), levels=6, colors="C0", alpha=0.5)
ax[0].plot(px, py, "-o", color="C3", lw=0.8, ms=2.5)
ax[0].set_xlabel("X"); ax[0].set_ylabel("Y")
ax[0].set_title(r"Gibbs zigzag at $\rho=0.99$: tiny axis-aligned steps")
rr = np.linspace(0, 0.995, 200)
ax[1].plot(rr, (1 - rr**2)/(1 + rr**2), color="C0", lw=2, label=r"theory $(1-\rho^2)/(1+\rho^2)$")
ax[1].plot([0.9, 0.99], [essfrac[0.9], essfrac[0.99]], "o", color="C3", ms=9, label="measured")
ax[1].set_yscale("log"); ax[1].set_xlabel(r"target correlation $\rho$")
ax[1].set_ylabel("ESS / iterations")
ax[1].set_title("Effective sample size collapses as $\\rho \\to 1$"); ax[1].legend()
save(fig, "gibbs-zigzag")
```

![Left: contours of a near-degenerate bivariate normal with a Gibbs path making small horizontal-then-vertical steps trapped along the diagonal ridge. Right: ESS/iterations on a log axis crashing from about 0.1 to 0.01 as rho goes 0.9 to 0.99, the two measured points sitting on the theory curve.](figures/11-gibbs-augmentation/gibbs-zigzag.png)

**Reconcile.** The measured lag-1 autocorrelations are `0.8117` at $\rho=0.9$ and `0.9801` at $\rho=0.99$ — sitting on $\rho^2 = 0.81$ and $0.9801$ to the third decimal, not on $\rho$. If you predicted "$\approx 0.99$" you were off in the right direction but for the wrong reason; the contraction squares it. The damage is in the ESS fraction: `0.1014` at $\rho=0.9$ but only `0.0101` at $\rho=0.99$ — matching the law $(1-\rho^2)/(1+\rho^2)\approx$ `0.0100`. **At $\rho=0.99$ you need on the order of 100 Gibbs iterations to buy one independent draw**, a 10× further collapse from $\rho=0.9$, not 2×. The fix is to stop moving one coordinate at a time: **blocked Gibbs** updates correlated components jointly. Here the whole target is one Gaussian block, so drawing $(X,Y)$ together gives independent samples — ESS/iterations jumps from `0.0111` (a fresh, independent run of the $\rho=0.99$ chain — Monte-Carlo noise around the `0.0101` above) to `1.0000`, a `89.7`× improvement. When you cannot block (the conditionals of the joint are intractable), this ESS collapse is exactly the wall that motivates Hamiltonian Monte Carlo in module 12: gradients let a sampler move *along* the ridge instead of ricocheting across it.

## 11.5 Data augmentation I: Albert–Chib probit

Now the module's second theme. Some models are not conjugate as written but become conjugate once you **augment** them with a well-chosen latent variable — you invent the missing piece of the generative story that, had you observed it, would make every conditional easy. The archetype is probit classification. With $y_i\in\{0,1\}$ and $P(y_i=1)=\Phi(x_i^\top\beta)$, the likelihood $\prod_i \Phi(x_i^\top\beta)^{y_i}(1-\Phi(x_i^\top\beta))^{1-y_i}$ is not conjugate to any prior on $\beta$. Albert and Chib (1993) noticed the probit's own generative story hands you the latent: a probit is a **thresholded Gaussian**. Introduce
$$z_i = x_i^\top\beta + \varepsilon_i,\quad \varepsilon_i\sim N(0,1),\qquad y_i = \mathbb{1}[z_i > 0],$$
which reproduces $P(y_i=1)=P(z_i>0)=\Phi(x_i^\top\beta)$ exactly. Condition on the latent $z$ and the model is *linear-Gaussian in $\beta$* — a regression with known unit variance. The two conditionals:

- $z_i \mid \beta, y_i \sim$ **truncated normal**: $N(x_i^\top\beta, 1)$ restricted to $(0,\infty)$ if $y_i=1$, to $(-\infty,0)$ if $y_i=0$ (the density is $\propto N(z_i;x_i^\top\beta,1)$ times the indicator that $z_i$ has the sign $y_i$ demands).
- $\beta \mid z \sim N(m, V)$ with $V=(X^\top X + I/\tau^2)^{-1}$, $m = V X^\top z$ — module 05's Gaussian conditioning with the latent $z$ as the response.

Sample truncated normals by the inverse-CDF trick (no rejection): for $N(m,1)$ on $(0,\infty)$, draw $u\sim U(0,1)$ and return $m + \Phi^{-1}\!\big(\Phi(-m) + u(1-\Phi(-m))\big)$.

```python
from scipy.special import ndtr, ndtri            # standard-normal CDF and its inverse
rng5 = np.random.default_rng(5)
n_pr, p_pr = 2000, 3
Xp = rng5.normal(size=(n_pr, p_pr)); Xp[:, 0] = 1.0
beta_pr_true = np.array([0.4, 1.2, -0.8])
ypr = ((Xp @ beta_pr_true + rng5.normal(size=n_pr)) > 0).astype(float)   # true probit data
print(f"class-1 rate = {ypr.mean():.3f}")

tau2p = 100.0
Vb = np.linalg.inv(Xp.T @ Xp + np.eye(p_pr) / tau2p); Lb = np.linalg.cholesky(Vb)

def rtruncnorm(mean, rng, positive):             # N(mean,1) truncated by sign, vectorized
    u = rng.uniform(size=mean.shape)
    lo = np.where(positive, ndtr(-mean), 0.0)
    hi = np.where(positive, 1.0, ndtr(-mean))
    return mean + ndtri(np.clip(lo + u*(hi - lo), 1e-12, 1 - 1e-12))

Mp, burnp = 4000, 1000
beta_c = np.zeros(p_pr); pd = np.empty((Mp, p_pr))
for t in range(Mp):
    z = rtruncnorm(Xp @ beta_c, rng5, ypr > 0.5)         # z | beta, y  (augmentation step)
    beta_c = Vb @ (Xp.T @ z) + Lb @ rng5.normal(size=p_pr)   # beta | z   (conjugate step)
    pd[t] = beta_c
pd = pd[burnp:]
for j in range(p_pr):
    print(f"beta[{j}]: true={beta_pr_true[j]:+.3f}  posterior mean={pd[:, j].mean():+.4f} "
          f"(sd {pd[:, j].std():.4f})")
```

```python
fig, ax = plt.subplots()
for j, c in zip(range(p_pr), ("C0", "C1", "C2")):
    ax.hist(pd[:, j], bins=60, density=True, color=c, alpha=0.5, label=f"$\\beta_{j}$ posterior")
    ax.axvline(beta_pr_true[j], color=c, ls="--", lw=1.5)
ax.set_xlabel("coefficient value"); ax.set_ylabel("density")
ax.set_title("Albert–Chib probit: augmented Gibbs recovers the true coefficients")
ax.legend()
save(fig, "probit-recovery")
```

![Three overlaid coefficient posteriors, each a bell centered on its dashed true value at 0.4, 1.2 and -0.8.](figures/11-gibbs-augmentation/probit-recovery.png)

On 2000 synthetic points with a `0.605` class-1 rate, the augmented sampler recovers the coefficients cleanly: posterior means `0.4524`, `1.1937`, `-0.8533` against truths $0.4$, $1.2$, $-0.8$, each within one-to-two posterior sds. Notice what augmentation bought: neither conditional required a Metropolis step or a tuning parameter — a non-conjugate classification model became two exact conjugate draws by conditioning on a latent we never observe. **Logistic** regression admits the same trick with a different latent: the Pólya–Gamma augmentation (Polson–Scott–Windle 2013) makes the logistic likelihood conditionally Gaussian in $\beta$ — mentioned here, and the reason Bayesian logistic regression can be Gibbs-sampled at all; module 15 fits logistic models by NUTS instead.

## 11.6 Missing data are just more latents

**Setup.** The augmentation insight has a striking corollary: if a value you *meant* to observe is missing, treat it as a latent variable and impute it inside the Gibbs loop, exactly like the probit's $z$. Take bivariate normal data $(Y_1,Y_2)\sim N(0,\Sigma)$ with correlation $0.7$, and delete $Y_2$ whenever $Y_1 > 0.3$ — a value is missing for reasons that depend only on what you *did* observe ($Y_1$). This is **Missing At Random (MAR)**.

**Predict.** You want $\mathbb{E}[Y_2]$, whose truth is $0$. The obvious move is complete-case analysis: average the $Y_2$ you actually have. Commit to a direction — is the complete-case mean unbiased, or does the MAR deletion push it, and which way?

**Reason.** "The data I kept are still real measurements, so their average estimates the mean" — the intuition that deleting rows only costs precision, not correctness. It ignores that deletion *selected on $Y_1$*, and $Y_1$ is correlated with $Y_2$.

**Run.** Impute the missing $Y_2$ inside Gibbs: draw each from its conditional $Y_2\mid Y_1$ (module 05's Gaussian conditioning again), then update $\mu$ given the completed data. We fix $\Sigma$ at its true value to isolate the selection-bias mechanism; a full sampler would add an inverse-Wishart block for $\Sigma$ — one more full conditional, same pattern. Compare to complete-case.

```python
rng6 = np.random.default_rng(6)
N_m, rho_m = 400, 0.7
Sig = np.array([[1.0, rho_m], [rho_m, 1.0]])
Yfull = rng6.multivariate_normal([0, 0], Sig, size=N_m)
mask = Yfull[:, 0] > 0.3                                   # MAR: missing Y2 where Y1 is large
print(f"missing fraction = {mask.mean():.3f}")
print(f"complete-case  E[Y2] = {Yfull[~mask, 1].mean():.4f}   (full-data {Yfull[:, 1].mean():.4f})")

# Impute-within-Gibbs: missing Y2 are latents; alternate impute <-> update mu.
Mm, burnm = 4000, 1000
mu_e = np.zeros(2); Y = Yfull.copy(); md = np.empty((Mm, 2))
cvar = Sig[1, 1] - Sig[1, 0]**2 / Sig[0, 0]               # Var(Y2 | Y1), constant
for t in range(Mm):
    cmean = mu_e[1] + Sig[1, 0]/Sig[0, 0]*(Y[mask, 0] - mu_e[0])   # E[Y2 | Y1] per missing row
    Y[mask, 1] = rng6.normal(cmean, np.sqrt(cvar))                 # impute the latents
    mu_e = rng6.multivariate_normal(Y.mean(0), Sig / N_m)          # mu | completed data
    md[t] = mu_e
md = md[burnm:]
print(f"impute-within-Gibbs  E[mu2] = {md[:, 1].mean():.4f}   E[mu1] = {md[:, 0].mean():.4f}")

# Multiple imputation = repeated posterior draws of the missing entries.
imp_means = []
for i in range(20):
    for _ in range(50):                                   # thin between completed datasets
        cmean = mu_e[1] + Sig[1, 0]/Sig[0, 0]*(Y[mask, 0] - mu_e[0])
        Y[mask, 1] = rng6.normal(cmean, np.sqrt(cvar))
        mu_e = rng6.multivariate_normal(Y.mean(0), Sig / N_m)
    imp_means.append(Y[:, 1].mean())                      # one completed dataset's Y2 mean
print(f"multiple imputation: between-imputation sd of the Y2 mean = {np.std(imp_means):.4f}")
```

```python
fig, ax = plt.subplots()
obs2 = Yfull[~mask, 1]
ax.hist(obs2, bins=30, density=True, color="C0", alpha=0.55, label="observed $Y_2$ (complete-case)")
ax.hist(Y[mask, 1], bins=30, density=True, color="C3", alpha=0.55, label="imputed $Y_2$ (one draw)")
ax.axvline(obs2.mean(), color="C0", lw=2); ax.axvline(0.0, color="k", ls="--", lw=1.5, label="true mean 0")
ax.axvline(md[:, 1].mean(), color="C1", lw=2, label="imputed posterior mean")
ax.set_xlabel(r"$Y_2$"); ax.set_ylabel("density")
ax.set_title("MAR deletion biases complete-case; imputing the latents removes it")
ax.legend(fontsize=9)
save(fig, "missing-data")
```

![Two histograms of Y2: the observed complete-case values shifted left with mean near -0.4, and the imputed missing values shifted right, so the combined posterior mean sits back at zero.](figures/11-gibbs-augmentation/missing-data.png)

**Reconcile.** Complete-case analysis gives $\mathbb{E}[Y_2]=$ `-0.3959`, badly biased below the truth $0$ (the full data would have given `-0.0036`), because deleting rows with large $Y_1$ preferentially deletes rows with large $Y_2$ — the survivors skew low. Imputing the missing $Y_2$ from $Y_2\mid Y_1$ inside Gibbs restores it: $\mathbb{E}[\mu_2]=$ `0.0149`, essentially the truth. The imputed values (red in the figure) sit exactly where the deleted ones would have, because the conditional $Y_2\mid Y_1$ knows how $Y_2$ tracks the large-$Y_1$ rows that were dropped. **This is line 2 doing the work missingness tried to hide.** The last print makes the "multiple" in *multiple imputation* concrete: each pass through the loop yields a *different* completed dataset — a fresh posterior draw of the missing block — and their spread (between-imputation sd of the $Y_2$ mean = `0.0285`) is precisely the extra uncertainty from not having observed those values, which Rubin's rules add to the within-imputation variance. Multiple imputation is nothing but *keeping several of the Gibbs completions instead of one.*

**When can you ignore the missingness mechanism?** Write the joint of data $Y$ and the missingness indicators $M$: $p(Y,M\mid\theta,\psi) = p(Y\mid\theta)\,p(M\mid Y,\psi)$. You are allowed to drop the $p(M\mid Y,\psi)$ factor — to *not model why data are missing* — exactly when it does not depend on the unobserved values (and $\theta,\psi$ are distinct). That is **ignorability**, and it lines up with three names:

- **MCAR** (missing completely at random): $M \perp Y$ — deletion is a coin flip; even complete-case is unbiased.
- **MAR**: $M$ depends only on *observed* $Y$ — as above; complete-case is biased but the mechanism still drops out of the likelihood, so imputing from the model is valid *without* modeling $M$.
- **MNAR** (missing not at random): $M$ depends on the *missing* values themselves (e.g. large incomes are the ones hidden) — the factor does **not** drop out, ignorable methods are biased, and you must model the missingness mechanism explicitly.

The demo was MAR: deletion depended on $Y_1$, which we see, so the impute-within-Gibbs recovered the truth without ever modeling *why* the holes appeared. Module 24 cashes this in for causal inference, where a potential outcome $Y(1)$ for an untreated unit is precisely an MAR-style missing value, imputed the same way.

## 11.7 Rao-Blackwellization: throw away the last coin flip

**Setup.** A Gibbs run estimates $\mathbb{E}[\sigma^2\mid y]$ from the model of §11.2 by averaging the raw draws $\tfrac1M\sum_t \sigma^2_{(t)}$. But at each step you *drew* $\sigma^2_{(t)}$ from a known conditional $\mathrm{IG}(a_{\text{cond}}, b_{\text{cond}}(\mu_{(t)}))$ whose mean $b_{\text{cond}}/(a_{\text{cond}}-1)$ you can write down. Averaging that conditional mean instead of the raw draw is the **Rao-Blackwellized** estimator.

**Predict.** Both estimators are unbiased for $\mathbb{E}[\sigma^2\mid y]$. Averaging the conditional mean replaces the final inverse-gamma draw with its expectation — how much does that shrink the estimator's variance across independent chains: a few percent, 2×, or much more?

**Reason.** "The raw draws already average out the last step's noise over $M$ iterations, so integrating it analytically is a rounding-error improvement." The Rao–Blackwell theorem (module 06's conditioning-reduces-variance, in Monte Carlo clothing) says otherwise: $\mathrm{Var}[g(\sigma^2)] = \mathbb{E}[\mathrm{Var}[g\mid\mu]] + \mathrm{Var}[\mathbb{E}(g\mid\mu)]$, and the conditional-mean estimator keeps only the second, smaller term.

**Run.**

```python
# Rao-Blackwell: average E[sigma^2 | mu] (a known IG mean) instead of raw sigma^2 draws.
mu0, k0, a0, b0 = 0.0, 1.0, 1.0, 1.0
def gibbs_raw_vs_rb(data, seed, M=3000, burn=500):
    r = np.random.default_rng(seed); n = len(data); xbar = data.mean()
    mu_mean = (k0*mu0 + n*xbar) / (k0 + n); a_c = a0 + (n + 1)/2
    mu_c, s2_c = xbar, data.var(); raw, rb = [], []
    for t in range(M):
        mu_c = r.normal(mu_mean, np.sqrt(s2_c / (k0 + n)))
        b_c = b0 + 0.5*np.sum((data - mu_c)**2) + 0.5*k0*(mu_c - mu0)**2
        s2_c = 1.0 / r.gamma(a_c, 1.0 / b_c)
        if t >= burn:
            raw.append(s2_c)               # raw draw
            rb.append(b_c / (a_c - 1))      # E[sigma^2 | mu_(t)] -- conditional mean
    return np.mean(raw), np.mean(rb)

raws, rbs = [], []
for rep in range(30):                       # 30 independent chains; compare estimator spread
    ra, rb = gibbs_raw_vs_rb(data, 2000 + rep); raws.append(ra); rbs.append(rb)
raws, rbs = np.array(raws), np.array(rbs)
print(f"raw estimator: sd across chains = {raws.std():.5f}")
print(f"RB  estimator: sd across chains = {rbs.std():.5f}")
print(f"variance-reduction factor = {raws.var()/rbs.var():.1f}x")
```

**Reconcile.** Across 30 independent chains the raw estimator's standard deviation is `0.01509`, the Rao-Blackwellized one's `0.00197` — a `58.8`× variance reduction, for free, from code you already wrote. The intuition that the last draw is "already averaged out" misses that the raw draw carries *all* of $\mathrm{Var}[\sigma^2\mid\mu]$ into every term, while the conditional mean has integrated it away analytically; only the smaller cross-$\mu$ variation survives. The booklet (ch. 11) makes the same point: when a conditional expectation is available in closed form, average *it*, not the sample. The one caveat: Rao-Blackwellization helps most when the conditioned-out quantity carries a lot of the noise (as $\sigma^2$'s inverse-gamma draw does here); when the conditional is already nearly a point mass, the gain is small.

## Bridge — augmentation is the E-step and the latent code

The move in §§11.5–11.6 — *invent a latent that makes the conditional easy, then integrate or average over it* — is one of the most reused ideas in the course, wearing three costumes.

- **EM's E-step (module 13).** Expectation–Maximization handles the same latent-variable models by taking the *expectation* over the latent's conditional $p(z\mid x,\theta)$ instead of *sampling* it. Gibbs draws $z^{(t)}\sim p(z\mid x,\theta)$; EM computes $\mathbb{E}[z\mid x,\theta]$. Stochastic augmentation and deterministic augmentation are the same decomposition — module 13 shows EM is Gibbs with the sampling step replaced by its mean, and both are coordinate moves on the same objective.
- **The VAE's latent code (module 25).** A variational autoencoder posits $x$ generated from a latent $z$, and *learns* an approximate conditional $q_\phi(z\mid x)$ to stand in for the intractable $p(z\mid x)$ — amortized augmentation, where a neural network replaces the closed-form full conditional. The probit's $z_i$ and the VAE's code are the same object: an unobserved cause you reconstruct to make the likelihood tractable.
- **Mixtures (module 19).** A cluster label is a latent you augment with; conditional on labels, a mixture is just per-group conjugate updates — Gibbs for mixtures is §11.5's pattern with a categorical latent instead of a Gaussian one.

The unifying sentence: **whenever a model is hard because you are marginalizing over something, put that something back in as a variable and condition on it.** Gibbs samples it, EM averages it, VI approximates it — three answers to one question.

## Pitfalls

- **Trusting a Gibbs sampler you never audited.** The §11.2 discipline is not optional ceremony: derive a conjugate special case, run it, and overlay the exact posterior (KS $p=$ `0.688` there). A sign error in a full conditional produces a chain that mixes beautifully and targets the *wrong* distribution — the trace looks perfect and the answer is wrong. An unaudited sampler is an unverified claim.
- **Reading mixing off the target correlation.** The chain's lag-1 autocorrelation is $\rho^2$, not $\rho$ (§11.4). High posterior correlation is the single most common cause of a Gibbs sampler that "runs" but produces almost no information; always report ESS, not iteration count, and block or reparameterize correlated components.
- **Deriving a full conditional by dropping the wrong terms.** The conditional for $\theta_i$ is proportional to the *joint* with every other variable held fixed — you keep every factor that contains $\theta_i$, including prior-coupling terms (the $\tfrac{\kappa_0}{2}(\mu-\mu_0)^2$ in §11.2's $\sigma^2$ conditional is easy to forget). Drop a coupling term and you have a different model.
- **Complete-case analysis under MAR.** Deleting incomplete rows is unbiased only under MCAR; under MAR it silently biases estimates (`-0.3959` vs the truth $0$ in §11.6). "Just drop the missing rows" is a modeling decision, usually the wrong one.
- **Forgetting MNAR breaks ignorability.** Impute-within-Gibbs is valid under MAR because the missingness mechanism drops out of the likelihood. If data are missing *because of their own value* (MNAR), no amount of imputing from the observed-data model fixes the bias — you must model the mechanism, and even then identification is fragile.

## Exercises

**Exercise 11.1 — Predict the mixing before you run it.**
*Setup:* You Gibbs-sample the bivariate normal of §11.4 at $\rho=0.95$ for $M=40{,}000$ iterations and want roughly 500 effective samples of $X$.
*Predict:* Will $M=40{,}000$ iterations deliver 500 effective draws, and roughly how many effective draws do you actually get?
*Reason:* The habit of treating iteration count as sample size — "40,000 draws is plenty for 500."
*Run:*
```python
rng_ex = np.random.default_rng(21)
xs, _ = gibbs_bvn(0.95, 40000, rng_ex)
print(f"lag-1 autocorr = {autocorr_fft(xs)[1]:.4f}  (rho^2 = {0.95**2:.4f})")
print(f"ESS = {ess_ips(xs):.0f}  (theory M*(1-r2)/(1+r2) = {40000*(1-0.95**2)/(1+0.95**2):.0f})")
```
<details><summary>Reconcile</summary>

The lag-1 autocorrelation is about `0.9057` ($=\rho^2=$ `0.9025`, not $0.95$), and the effective sample size is roughly `1585` — somewhat below the AR(1) theory value $M(1-\rho^2)/(1+\rho^2)\approx$ `2050` (the initial-positive-sequence estimator is deliberately conservative at high autocorrelation). So 40,000 iterations *do* clear 500 effective draws here, but the ESS fraction is only about 4%: you paid for 40,000 and received ~1585. The lesson is not the specific number but the ratio — at $\rho=0.95$, roughly 25 iterations per independent draw. Push to $\rho=0.99$ and the same 40,000 iterations would give only ~400 effective draws. Iteration count is a currency with an exchange rate set by $\rho^2$; always quote ESS.
</details>

**Exercise 11.2 — Does a stronger prior speed up mixing?**  *(surprising)*
*Setup:* In the §11.2 Normal model, a colleague argues that a *tighter* prior on $\mu$ (larger $\kappa_0$) will make the two Gibbs conditionals less coupled and so mix faster.
*Predict:* Does raising $\kappa_0$ from 1 to 50 noticeably lower the lag-1 autocorrelation of the $\sigma^2$-chain?
*Reason:* "Tighter prior ⇒ pins $\mu$ ⇒ less back-and-forth between the two conditionals."
*Run:*
```python
for k0_try in (1.0, 50.0):
    r = np.random.default_rng(4); n = len(data); xbar = data.mean()
    mm = (k0_try*0.0 + n*xbar)/(k0_try + n); a_c = 1.0 + (n+1)/2
    mu_c, s2_c = xbar, data.var(); s2chain = []
    for t in range(6000):
        mu_c = r.normal(mm, np.sqrt(s2_c/(k0_try + n)))
        b_c = 1.0 + 0.5*np.sum((data-mu_c)**2) + 0.5*k0_try*(mu_c-0.0)**2
        s2_c = 1.0/r.gamma(a_c, 1.0/b_c); s2chain.append(s2_c)
    print(f"kappa0={k0_try:>4}: sigma^2 lag-1 autocorr = {autocorr_fft(np.array(s2chain[500:]))[1]:.4f}")
```
<details><summary>Reconcile</summary>

Both give a lag-1 autocorrelation near `0.0015` — essentially zero, and essentially unchanged. This Gibbs sampler already mixes almost perfectly regardless of $\kappa_0$, because $\mu$ and $\sigma^2$ are only weakly coupled in the NIG posterior (the $\mu$-conditional's *mean* doesn't even depend on $\sigma^2$ — only its scale does). The intuition confused *prior strength* with *posterior correlation between parameters*; it is the latter that governs mixing, and here it is already tiny. Contrast §11.4, where the coupling is $\rho=0.99$ by construction and no prior tweak helps — only blocking does. Mixing is about the geometry of the joint posterior, not the sharpness of any one prior.
</details>

**Exercise 11.3 — Imputation vs. dropping rows under MAR.**  *(ML bridge: missing features)*
*Setup:* You have the §11.6 bivariate-normal data with $Y_2$ MAR-deleted, and you want to *predict* $Y_2$ from $Y_1$ on the deleted rows (a missing-feature imputation task familiar from ML pipelines). Compare the mean of the *observed* $Y_2$ (mean-imputation, the sklearn `SimpleImputer` default) against the model-based conditional mean $\mathbb{E}[Y_2\mid Y_1]$ on the deleted rows.
*Predict:* On the deleted rows (all with $Y_1>0.3$), will mean-imputation or conditional imputation be closer to the true deleted $Y_2$ values?
*Reason:* "Filling with the column mean is a fine default" — the ML reflex that imputation is a preprocessing detail.
*Run:*
```python
true_missing = Yfull[mask, 1]
mean_imp = np.full(mask.sum(), Yfull[~mask, 1].mean())          # column-mean imputation
cond_imp = 0.0 + Sig[1,0]/Sig[0,0]*(Yfull[mask, 0] - 0.0)       # E[Y2 | Y1]
print(f"mean-imputation RMSE       = {np.sqrt(np.mean((true_missing - mean_imp)**2)):.4f}")
print(f"conditional-imputation RMSE = {np.sqrt(np.mean((true_missing - cond_imp)**2)):.4f}")
```
<details><summary>Reconcile</summary>

Mean-imputation RMSE is about `1.3281`; conditional imputation is about `0.7093`, nearly halving the error — and worse, mean-imputation is *biased low* on exactly these rows, because the deleted rows have large $Y_1$ and hence (via $\rho=0.7$) large $Y_2$, which the column mean cannot know. Filling with the marginal mean throws away the correlation that carries all the information about the missing entries; the conditional mean is the whole point of the Gibbs imputation step. This is why naive `SimpleImputer(strategy="mean")` degrades a downstream model under MAR: it injects a systematic bias that a conditional (or iterative/`IterativeImputer`) scheme avoids — the same distinction as complete-case vs. impute-within-Gibbs, now measured as prediction error.
</details>

**Exercise 11.4 — Why the probit latent must be truncated.**
*Setup:* In the Albert–Chib sampler, suppose you (wrongly) drew $z_i$ from the *untruncated* $N(x_i^\top\beta,1)$ instead of the sign-truncated version.
*Predict:* Would the sampler still recover $\beta$, converge to some *wrong-but-fixed* $\beta$, or fail to use $y$ at all?
*Reason:* "The latent is Gaussian either way; truncation is a minor correction."
*Run:*
```python
rng_bad = np.random.default_rng(9); beta_c = np.zeros(p_pr); acc = []
for t in range(2000):
    z = Xp @ beta_c + rng_bad.normal(size=n_pr)              # NO truncation: ignores y!
    beta_c = Vb @ (Xp.T @ z) + Lb @ rng_bad.normal(size=p_pr)
    if t >= 500: acc.append(beta_c.copy())
print(f"untruncated posterior means = {np.round(np.mean(acc, 0), 3)}  (true {beta_pr_true})")
```
<details><summary>Reconcile</summary>

The untruncated sampler returns posterior means `-0.844`, `0.77`, `-0.997` — unrelated to the truth $[0.4, 1.2, -0.8]$ (the intercept even flips sign). Look at the two update lines: neither $z$ nor $\beta$ ever references `ypr`. Dropping the truncation deletes the *only* place the labels $y$ enter the sampler, so the chain's output is **completely independent of the data** — it would print these same three numbers for any labels whatsoever. Substituting the $z$-draw into the $\beta$-update gives $\beta_{t+1}\approx (X^\top X+I/\tau^2)^{-1}X^\top X\,\beta_t + \text{noise}\approx\beta_t+\text{noise}$: a prior-tethered AR(1) (contraction eigenvalues just below 1) that settles into a stationary law around the prior mean, carrying no information from $y$ — not a posterior. The truncation to the sign of $y_i$ is not a correction to the augmentation — it *is* the likelihood, the entire mechanism by which the observed classes inform $\beta$. Augmentation works because the latent's conditional encodes the data; strip that and you have an elaborate way to sample noise.
</details>

## Takeaways

- **Gibbs = MH with acceptance 1** (proven; ratio prints `1.0000000000`): sample each full conditional in turn, and the chain targets the exact joint posterior — no step size, no rejections, but only axis-aligned moves.
- **Always audit against a known exact answer.** The Normal$(\mu,\sigma^2)$ Gibbs marginals match module 05's closed-form $t$ and $\mathrm{IG}$ (KS $p=$ `0.688`, `0.175`); Bayesian regression by Gibbs matches OLS to three decimals. A conjugate special case is your sampler's unit test.
- **Correlation is the enemy, quantified.** For the bivariate-normal Gibbs the lag-1 autocorrelation is $\rho^2$ *exactly* (`0.8117` at $\rho=0.9$, `0.9801` at $\rho=0.99$), and the ESS fraction is $(1-\rho^2)/(1+\rho^2)$ — collapsing to `0.0101` at $\rho=0.99$, ~100 iterations per independent draw. Blocking correlated components fixes it (`89.7`× ESS gain here); when you can't block, this is what motivates HMC (module 12).
- **Augmentation invents latents that restore conjugacy.** Albert–Chib probit = threshold a latent Gaussian, then two exact conjugate draws (coefficients recovered to `0.4524`, `1.1937`, `-0.8533`); Pólya–Gamma does the same for logistic.
- **Missing data are just more latents.** Impute-within-Gibbs under MAR removes the complete-case bias (`-0.3959` → `0.0149`); multiple imputation = keeping several posterior completions; MCAR/MAR/MNAR name whether the missingness mechanism drops out of the likelihood (ignorability). Potential outcomes as missing data returns in module 24.
- **Rao-Blackwellize:** average a closed-form conditional mean instead of the raw draw — here a `58.8`× variance reduction for free (booklet ch. 11).
- **One idea, three costumes:** augmentation is EM's E-step (average the latent, module 13) and the VAE's latent code (amortize it, module 25). Whenever marginalizing is hard, put the variable back and condition on it.

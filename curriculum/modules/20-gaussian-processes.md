# 20. Gaussian Processes: Priors over Functions

> **Spine.** A Gaussian process is Bayesian linear regression pushed to infinitely many basis functions; the kernel *is* the covariance of a prior over functions, and the marginal likelihood tunes that kernel with a built-in Occam factor.
> **Which line?** Lines 2 and 3, in function space. The posterior over functions is *one Gaussian conditioning step* (module 05's `gaussian_condition`), and the predictive band is the marginalization that collapses at your data and flares away from it.
> **Promise.** After this module you can write an exact GP regressor in ~20 lines, read a kernel as a smoothness assumption you can *draw*, tune its hyperparameters by marginal likelihood (and see the Occam term punish an overfit lengthscale), recognize the GP posterior mean as kernel ridge regression, and run a Bayesian-optimization loop — plus place three modern ideas (NNGP, inducing points, BART) on the map.
> **Prereqs.** Modules 05 (the Gaussian conditioning toolkit `gaussian_condition`, the precision-weighted mean), 14 (regression as a prior over functions — its finite basis expansion is this module's §1 at finite $M$), 17 (the evidence = fit + complexity decomposition — ML-II is that decomposition in function space).
> **Runtime.** ~14 s.
> **Sources.** Rasmussen & Williams, *Gaussian Processes for Machine Learning*, by concept; ISLP ch. 7; booklet ch. 14 (nonparametric Bayes) framing.

Module 14 fit a curve by choosing $M$ basis functions $\phi_1,\dots,\phi_M$, putting a Gaussian prior on their weights, and conditioning — a prior over functions, drawn as a fan of lines that collapsed onto the data. The obvious question it left open: **why choose $M$ at all?** Let $M\to\infty$ — cover the input space with infinitely many basis functions — and the weight-space bookkeeping becomes intractable, but a miracle intervenes. Every prediction depends on the weights *only* through the $n\times n$ matrix of inner products $\phi(x_i)^\top\Sigma_w\,\phi(x_j)$. Name that matrix the **kernel** and you never touch the weights again. The four lines (module 00): **a model is a joint $p(\text{unknowns},\text{knowns})$; inference is conditioning; prediction is marginalization; a decision minimizes posterior expected loss** — here the unknown is the *entire function* $f$, the kernel is its prior covariance, and conditioning on data is one Schur complement.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "20-gaussian-processes"          # this module's figure dir
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

## 20.1 Two routes to the same prediction, then the infinite limit  [LEAD]

Take module 14's model with a concrete basis: $M=8$ Gaussian bumps $\phi_j(x)=\exp\!\big(-(x-c_j)^2/2h^2\big)$, weights $\beta\sim N(0,\sigma_w^2 I)$, noise $\sigma_n^2$. There are **two** ways to predict at a test input.

- **Weight space** (module 14's machinery): condition on $\beta$, get its Gaussian posterior, push it through $\phi(x_*)$. Cost scales with $M$.
- **Function space** (the kernel trick): define $k(x,x')=\phi(x)^\top\Sigma_w\,\phi(x')$, an $n\times n$ Gram matrix, and never mention $\beta$. Cost scales with $n$.

These are the same model written in two coordinate systems, so they *must* agree — but seeing the agreement at machine precision is the point, because it licenses throwing the weights away.

**Predict.** Same model, two computations. Before running: will the predictive mean and variance differ between the routes — never (identical to rounding), by a little (different linear algebra accumulates error), or noticeably?

**Reason.** The naive worry is that "kernelizing" is an approximation — a trick that trades accuracy for speed. Name that intuition: it treats the kernel form as a *different, cheaper model*. It is not; it is the *same* model.

```python
# One 1-D regression dataset.
n = 12
x = np.sort(rng.uniform(-2.0, 2.0, size=n))
f_true = lambda t: np.sin(1.5*t)
sigma_n = 0.2
y = f_true(x) + rng.normal(0, sigma_n, size=n)
sigma_n2 = sigma_n**2

# Finite Gaussian-bump basis: 8 bumps, weights beta ~ N(0, sigma_w^2 I).
M, h, sw2 = 8, 0.5, 1.0
centers = np.linspace(-2.5, 2.5, M)
def phi(t):
    t = np.atleast_1d(t)
    return np.exp(-0.5*(t[:, None] - centers[None, :])**2 / h**2)   # (len(t), M)
xstar = np.linspace(-3.0, 3.0, 60)

# ROUTE A -- weight space (module 14 blr): posterior over beta, then push through phi.
Phi = phi(x); Sigma_w = sw2*np.eye(M)
Sig_beta = np.linalg.inv(Phi.T @ Phi / sigma_n2 + np.linalg.inv(Sigma_w))
mu_beta  = Sig_beta @ (Phi.T @ y / sigma_n2)
Phis = phi(xstar)
mean_w = Phis @ mu_beta                                   # predictive mean of the latent f*
var_w  = np.einsum("ij,jk,ik->i", Phis, Sig_beta, Phis)  # predictive variance of f*

# ROUTE B -- function space: k(x,x') = phi(x)^T Sigma_w phi(x'), never mention beta.
kfun = lambda ta, tb: phi(ta) @ Sigma_w @ phi(tb).T
K   = kfun(x, x); Ks = kfun(x, xstar); Kss = kfun(xstar, xstar)
Kyi = np.linalg.inv(K + sigma_n2*np.eye(n))
mean_k = Ks.T @ (Kyi @ y)
var_k  = np.diag(Kss) - np.einsum("ij,jk,ik->i", Ks.T, Kyi, Ks.T)

print(f"two routes: max|mean_w - mean_k| = {np.max(np.abs(mean_w-mean_k)):.2e}")
print(f"two routes: max|var_w  - var_k | = {np.max(np.abs(var_w-var_k)):.2e}")
```

**Reconcile.** The two routes agree to `1.14e-14` on the mean and `9.16e-15` on the variance — machine precision. The kernel form is not an approximation to weight-space regression; it *is* weight-space regression, re-expressed so the weights never appear. That matters because the function-space cost is $O(n^3)$ regardless of $M$ — so we can now send $M\to\infty$ for free.

**The infinite limit.** Let the bumps proliferate: place $M$ of them at spacing $\Delta c$, give each weight variance $\sigma_w^2=A\,\Delta c$, and let $\Delta c\to 0$. The kernel becomes a Riemann sum converging to an integral,
$$k(x,x') = A\!\int\! \exp\!\Big(\!-\tfrac{(x-c)^2}{2h^2}\Big)\exp\!\Big(\!-\tfrac{(x'-c)^2}{2h^2}\Big)dc = A\,h\sqrt\pi\,\exp\!\Big(\!-\tfrac{(x-x')^2}{4h^2}\Big),$$
which is the **squared-exponential** (RBF) kernel $\eta^2\exp(-(x-x')^2/2\ell^2)$ with $\ell=\sqrt2\,h$ and $\eta^2=A\,h\sqrt\pi$. Infinitely many localized bumps *is* a smoothness prior with a single lengthscale. Verify the limit numerically — the finite sum converges to the closed-form RBF as $M$ grows:

```python
def krbf(ta, tb, eta2, ell):
    d2 = (np.atleast_1d(ta)[:, None] - np.atleast_1d(tb)[None, :])**2
    return eta2*np.exp(-0.5*d2/ell**2)

hb, A = 0.4, 1.0
ell_lim, eta2_lim = np.sqrt(2)*hb, A*hb*np.sqrt(np.pi)
pa = np.array([0.0, 0.3, 0.5, 1.0, -0.7]); pb = np.array([0.0, 0.0, 0.2, -0.4, 0.5])
target = np.array([krbf(a, b, eta2_lim, ell_lim)[0, 0] for a, b in zip(pa, pb)])
print(f"limit kernel: ell = {ell_lim:.4f}, eta2 = {eta2_lim:.4f}")
shapes = {}
for Mlim in (10, 40, 160):
    c = np.linspace(-6, 6, Mlim); dc = c[1]-c[0]
    phil = lambda t: np.exp(-0.5*(np.atleast_1d(t)[:, None] - c[None, :])**2 / hb**2)
    km = np.array([A*dc*(phil(a) @ phil(b).T)[0, 0] for a, b in zip(pa, pb)])
    print(f"  M={Mlim:4d}: max|k_M - k_RBF| = {np.max(np.abs(km-target)):.3e}")
    xr = np.linspace(-3, 3, 200)
    shapes[Mlim] = A*dc*(phil(xr) @ phil(np.array([0.0])).T).ravel()

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(xstar, mean_w, color="C0", lw=6, alpha=0.4, label="weight space (route A)")
axes[0].plot(xstar, mean_k, color="C1", lw=1.5, ls="--", label="function space (route B)")
axes[0].fill_between(xstar, mean_k-1.96*np.sqrt(var_k), mean_k+1.96*np.sqrt(var_k),
                     color="C1", alpha=0.15)
axes[0].plot(x, y, "ko", ms=5, label="data")
axes[0].set_title("Same prediction, two computations"); axes[0].set_xlabel("x"); axes[0].set_ylabel("y")
axes[0].legend(fontsize=9)
xr = np.linspace(-3, 3, 200)
for Mlim, col in zip((10, 40, 160), ("C3", "C2", "C0")):
    axes[1].plot(xr, shapes[Mlim], color=col, lw=1.3, label=f"finite sum, M={Mlim}")
axes[1].plot(xr, krbf(xr, np.array([0.0]), eta2_lim, ell_lim).ravel(),
             "k--", lw=2, label="RBF limit")
axes[1].set_title(r"Bumps $\to$ squared-exponential as $M\to\infty$")
axes[1].set_xlabel("x - x'"); axes[1].set_ylabel("k(x, x')"); axes[1].legend(fontsize=9)
save(fig, "two-routes-and-limit")
```

![Left: a GP regression fit where the thick weight-space mean and the dashed function-space mean lie exactly on top of each other, through twelve data points, with a shaded band. Right: the finite Gaussian-bump kernel k(x,x') plotted against separation, bumpy at M=10, and by M=160 lying exactly on the smooth dashed RBF-limit curve.](figures/20-gaussian-processes/two-routes-and-limit.png)

The finite sum closes on the RBF kernel fast: max deviation `5.432e-01` at $M=10$, `8.087e-08` at $M=40$, and `1.110e-16` — machine zero — by $M=160$ (limit constants $\ell=$ `0.5657`, $\eta^2=$ `0.7090`). The left panel is the whole idea in one image: the two routes are *indistinguishable*, so the moment you work in function space, the number of basis functions stops being a knob you turn — it went to infinity, and all that survives is the kernel. **A Gaussian process is the $M\to\infty$ limit of module 14, and the kernel is what it left behind.** Formally: $f$ is a GP with mean $0$ and covariance $k$ if every finite collection $(f(x_1),\dots,f(x_m))$ is jointly Gaussian with covariance $[k(x_i,x_j)]$ — a distribution over functions, specified entirely by $k$.

## 20.2 The kernel gallery: what a smoothness assumption looks like

The kernel encodes every prior belief about the function *before any data*: how wiggly, how periodic, how far correlations reach. The fastest way to understand a kernel is to **draw from the prior it defines** — sample $f\sim N(0,\,K(X,X))$ on a dense grid and look. Four workhorses:

- **RBF** (squared-exponential) $\eta^2\exp(-r^2/2\ell^2)$: infinitely differentiable, very smooth; $\ell$ sets the wiggle scale.
- **Matérn-3/2** $\eta^2(1+\sqrt3\,r/\ell)\exp(-\sqrt3\,r/\ell)$: only once differentiable — rougher, more realistic for physical signals.
- **Periodic** $\eta^2\exp(-2\sin^2(\pi r/p)/\ell^2)$: draws repeat with period $p$.
- **Linear** $\sigma_b^2+\sigma_v^2\,x\,x'$: draws are straight lines — Bayesian linear regression is a GP too.

```python
def sqd(ta, tb):
    ta = np.atleast_1d(ta); tb = np.atleast_1d(tb)
    return (ta[:, None] - tb[None, :])**2
def k_rbf(ta, tb, eta2=1.0, ell=1.0):      return eta2*np.exp(-0.5*sqd(ta, tb)/ell**2)
def k_matern32(ta, tb, eta2=1.0, ell=1.0):
    s = np.sqrt(3*sqd(ta, tb) + 1e-18)/ell; return eta2*(1+s)*np.exp(-s)
def k_periodic(ta, tb, eta2=1.0, ell=1.0, p=1.0):
    r = np.sqrt(sqd(ta, tb) + 1e-18);       return eta2*np.exp(-2*np.sin(np.pi*r/p)**2/ell**2)
def k_linear(ta, tb, sb2=0.2, sv2=1.0):
    ta = np.atleast_1d(ta); tb = np.atleast_1d(tb); return sb2 + sv2*np.outer(ta, tb)

def prior_draws(kern, xg, n_draws, gen, jitter=1e-8):
    K = kern(xg, xg) + jitter*np.eye(len(xg))       # jitter: keep Cholesky positive-definite
    L = np.linalg.cholesky(K)
    return (L @ gen.normal(size=(len(xg), n_draws))).T

xg = np.linspace(-4, 4, 240)
gen = np.random.default_rng(1)
fig, axes = plt.subplots(2, 2, figsize=(11, 6.5), sharex=True)
# RBF at two lengthscales -> hyperparameters morph the draws
for ell, col in [(1.0, "C0"), (0.3, "C3")]:
    for f in prior_draws(lambda a, b: k_rbf(a, b, 1.0, ell), xg, 3, gen):
        axes[0, 0].plot(xg, f, color=col, alpha=0.7, lw=1)
axes[0, 0].set_title(r"RBF: $\ell=1$ (blue, smooth) vs $\ell=0.3$ (red, wiggly)")
for f in prior_draws(lambda a, b: k_matern32(a, b, 1.0, 1.0), xg, 4, gen):
    axes[0, 1].plot(xg, f, color="C1", alpha=0.8, lw=1)
axes[0, 1].set_title(r"Matern-3/2, $\ell=1$: rougher (once differentiable)")
for f in prior_draws(lambda a, b: k_periodic(a, b, 1.0, 1.0, 2.0), xg, 4, gen):
    axes[1, 0].plot(xg, f, color="C2", alpha=0.8, lw=1)
axes[1, 0].set_title(r"Periodic, $p=2$: draws repeat")
for f in prior_draws(lambda a, b: k_linear(a, b, 0.2, 1.0), xg, 6, gen):
    axes[1, 1].plot(xg, f, color="C4", alpha=0.7, lw=1)
axes[1, 1].set_title("Linear: draws are straight lines")
for ax in axes.ravel(): ax.set_xlabel("x"); ax.set_ylabel("f(x)")
save(fig, "kernel-gallery")
print("kernel gallery: 3-6 prior draws per kernel drawn")
```

![Four panels of prior function samples. Top-left RBF: three smooth blue curves (long lengthscale) and three fast-wiggling red curves (short lengthscale). Top-right Matern-3/2: jagged, once-differentiable curves. Bottom-left periodic: curves that repeat with period 2. Bottom-right linear: straight lines of assorted slopes and intercepts through the origin region.](figures/20-gaussian-processes/kernel-gallery.png)

Each panel *is* a prior — the set of functions the model considers plausible before seeing data. The RBF panel shows the single most important knob: shrink the lengthscale $\ell$ and the same kernel family goes from lazily smooth (blue) to frantically wiggly (red). Matérn-3/2 draws are visibly rougher than RBF at the same $\ell$ — the finite differentiability shows. The periodic draws repeat exactly; the linear draws are lines. **Choosing a kernel is choosing what "a reasonable function" means** — and §20.4 will let the *data* choose the hyperparameters for you.

## 20.3 The exact GP posterior in twenty lines (module 05, verbatim)

Conditioning is where the GP earns the four-line framing. Stack the latent test values $f_*=f(X_*)$ and the observed data $y=f(X)+\varepsilon$ into one joint Gaussian,
$$\begin{bmatrix} f_* \\ y \end{bmatrix} \sim N\!\left(0,\ \begin{bmatrix} K_{**} & K_{*n} \\ K_{n*} & K_{nn}+\sigma_n^2 I \end{bmatrix}\right),$$
and the posterior $p(f_*\mid y)$ is **exactly module 05's `gaussian_condition`** — the MVN block formula $\mu_{1|2}=\Sigma_{12}\Sigma_{22}^{-1}x_2$, $\Sigma_{1|2}=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$, the same Schur complement that powered modules 14 and (next) 21. No new inference machinery — a GP regressor is that one function called on a covariance matrix built from the kernel.

**Predict.** We will fit two GPs to the same six points: one **noiseless** ($\sigma_n^2\to0$, the function passes through the data) and one **noisy** ($\sigma_n=0.15$). Before running: at a *noiseless* training input, how wide is the 95% posterior band — as wide as the prior ($\pm1.96$), about half that, or essentially zero?

**Reason.** The tempting answer carries the regression reflex "there is always uncertainty at a data point." Name it — it forgets that a *noiseless* observation pins $f$ to a known value, so conditioning leaves nothing to be uncertain about there.

```python
def gaussian_condition(mu, Sigma, idx1, idx2, x2):     # verbatim from module 05
    S11 = Sigma[np.ix_(idx1, idx1)]; S12 = Sigma[np.ix_(idx1, idx2)]
    S22 = Sigma[np.ix_(idx2, idx2)]; S21 = Sigma[np.ix_(idx2, idx1)]
    cond_mean = mu[idx1] + S12 @ np.linalg.solve(S22, x2 - mu[idx2])
    cond_cov  = S11 - S12 @ np.linalg.solve(S22, S21)
    return cond_mean, cond_cov

def gp_posterior(Xtr, ytr, Xte, kern, sn2, jitter=1e-8):
    """Exact zero-mean GP posterior over f(Xte). Reuses module 05's gaussian_condition."""
    nte, ntr = len(Xte), len(Xtr)
    allx = np.concatenate([Xte, Xtr])
    Sig = kern(allx, allx)                    # joint prior covariance of [f_te, f_tr]
    Sig[nte:, nte:] += sn2*np.eye(ntr)        # observation noise on the training block only
    Sig += jitter*np.eye(nte+ntr)             # 1e-8 I: numerical PD insurance (see Pitfalls)
    m, cov = gaussian_condition(np.zeros(nte+ntr), Sig,
                                list(range(nte)), list(range(nte, nte+ntr)), ytr)
    return m, np.diag(cov)

xt = np.array([-2.0, -1.3, -0.6, 0.2, 1.0, 1.7])
yt = np.sin(1.5*xt)
xgp = np.linspace(-3.2, 3.2, 120)
kern = lambda a, b: k_rbf(a, b, 1.0, 0.7)

m_free, v_free = gp_posterior(xt, yt, xgp, kern, 1e-6)        # (nearly) noiseless
m_noise, v_noise = gp_posterior(xt, yt, xgp, kern, 0.15**2)   # noisy
_, v_at_train = gp_posterior(xt, yt, xt, kern, 1e-6)          # variance AT the data (noiseless)
print(f"noiseless: max posterior var at a training point = {v_at_train.max():.2e}")
print(f"noiseless: posterior var far off-support (x=3.2)  = {v_free[-1]:.4f}   (prior var = 1.0)")
print(f"noisy:     mean posterior var at the training inputs = "
      f"{gp_posterior(xt, yt, xt, kern, 0.15**2)[1].mean():.4f}")

fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
for ax, m, v, title in [(axes[0], m_free, v_free, "Noiseless: mean interpolates, band pinches to 0"),
                        (axes[1], m_noise, v_noise, r"Noisy ($\sigma_n=0.15$): mean smooths")]:
    sd = np.sqrt(np.maximum(v, 0))
    ax.fill_between(xgp, m-1.96*sd, m+1.96*sd, color="C0", alpha=0.2, label="95% posterior")
    ax.plot(xgp, m, color="C1", lw=2, label="posterior mean")
    ax.plot(xgp, np.sin(1.5*xgp), "k:", lw=1, label="truth")
    ax.plot(xt, yt, "ko", ms=6, label="data")
    ax.set_title(title, fontsize=10); ax.set_xlabel("x"); ax.legend(fontsize=8, loc="lower center")
axes[0].set_ylabel("f(x)"); axes[0].set_ylim(-2.6, 2.6)
save(fig, "gp-posterior")
```

![Two GP posterior panels over six data points. Left, noiseless: the mean curve passes exactly through every point and the blue band pinches to zero width at each one, ballooning between and beyond them. Right, noisy: the mean is a smoother curve that no longer hits every point exactly, and the band retains a floor width even at the data.](figures/20-gaussian-processes/gp-posterior.png)

**Reconcile.** At a noiseless training input the posterior variance is `1.02e-06` — numerically zero: it equals the assumed noise floor $\sigma_n^2=10^{-6}$ (the jitter, $10^{-8}$, sits two orders of magnitude below and only guarantees positive-definiteness). A noiseless observation *is* the function value there, so conditioning removes all uncertainty: the band pinches to a point and the mean interpolates. This is module 14's trumpet taken to its extreme — the epistemic term vanishes where the data pin $f$, and grows away from them. Off-support at $x=3.2$ the posterior variance climbs back to `0.9834`, essentially the prior variance $1.0$: with no nearby data the GP reverts to its prior (mean $0$, full width) — the honest statement "I have no idea out here," which no point predictor makes. The noisy fit tells the complementary story: with $\sigma_n=0.15$ the mean no longer interpolates (it need not explain the noise), and the variance at the inputs is `0.0213`, a floor rather than zero — you learned $f$ up to the noise, not exactly. **Interpolation vs smoothing is one dial: the noise level $\sigma_n^2$.**

## 20.4 ML-II: the marginal likelihood tunes the kernel, Occam included

Where do $\ell$, $\eta^2$, $\sigma_n^2$ come from? The same place module 14's $\tau^2$ and module 17's model index came from: **maximize the marginal likelihood** (type-II maximum likelihood, "ML-II"), integrating the entire function $f$ out. For a GP the evidence is closed-form,
$$\log p(y\mid\theta)=\underbrace{-\tfrac12\,y^\top K_y^{-1}y}_{\text{data fit}}\ \underbrace{-\tfrac12\log|K_y|}_{\text{complexity}}\ -\ \tfrac n2\log 2\pi,\qquad K_y=K_\theta+\sigma_n^2 I,$$
the **identical fit + complexity decomposition** as module 17's polynomial evidence — now with the kernel's continuous hyperparameters in place of a discrete degree. The complexity term $-\tfrac12\log|K_y|$ depends only on the inputs and the kernel, not on the targets: a wiggly small-$\ell$ kernel treats every point as independent, inflating $|K_y|$'s effective volume and paying a penalty.

**Predict.** Consider a lengthscale so tiny the GP mean can wiggle through *every* training point — a near-perfect interpolant, training error ~0. Does the marginal likelihood *reward* that overfit lengthscale (better fit ⇒ higher evidence), or punish it?

**Reason.** The naive intuition is module 17's exactly: "likelihood-type scores reward fit; the tiny lengthscale fits best; so evidence must prefer it — you'd need a separate penalty to stop it." It forgets the $-\tfrac12\log|K_y|$ term integrates $f$ out and prices flexibility automatically.

```python
def log_marglik(Xtr, ytr, kern, sn2, jitter=1e-8):
    K = kern(Xtr, Xtr) + (sn2+jitter)*np.eye(len(Xtr))
    L = np.linalg.cholesky(K)
    a = np.linalg.solve(L.T, np.linalg.solve(L, ytr))
    fit = -0.5*ytr @ a                          # -1/2 y' Ky^{-1} y
    complexity = -np.sum(np.log(np.diag(L)))    # -1/2 log|Ky|  (the Occam term)
    return fit + complexity - 0.5*len(ytr)*np.log(2*np.pi), fit, complexity

rng2 = np.random.default_rng(3)
nml = 25
xml = np.sort(rng2.uniform(-3, 3, nml))
yml = np.sin(1.2*xml) + 0.3*xml + rng2.normal(0, 0.2, nml); yml = yml - yml.mean()
sn2_ml = 0.2**2
ells = np.linspace(0.05, 3.0, 80)
curve = np.array([log_marglik(xml, yml, lambda a, b: k_rbf(a, b, 1.0, e), sn2_ml) for e in ells])
lml, fitc, compc = curve[:, 0], curve[:, 1], curve[:, 2]
best_ell = ells[np.argmax(lml)]
print(f"ML-II: best lengthscale = {best_ell:.3f}, log-evidence = {lml.max():.3f}")
for e in (0.05, best_ell, 2.5):
    lm, ft, cp = log_marglik(xml, yml, lambda a, b: k_rbf(a, b, 1.0, e), sn2_ml)
    print(f"  ell={e:5.3f}: log-ev {lm:8.3f} = fit {ft:8.3f} + complexity {cp:7.3f}")

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(ells, lml, color="C1", lw=2, label="log-evidence")
axes[0].plot(ells, fitc, color="C0", lw=1.5, ls="--", label="data fit")
axes[0].plot(ells, compc, color="C3", lw=1.5, ls=":", label="complexity term")
axes[0].axvline(best_ell, color="k", lw=1, alpha=0.6)
axes[0].set_title("Evidence = fit + complexity (module 17, function space)")
axes[0].set_xlabel(r"lengthscale $\ell$"); axes[0].set_ylabel("nats"); axes[0].legend(fontsize=8)
xfit = np.linspace(-3.3, 3.3, 200)
for e, col, lab in [(0.05, "C3", r"overfit $\ell=0.05$"), (best_ell, "C1", f"ML-II ell={best_ell:.2f}")]:
    m, _ = gp_posterior(xml, yml, xfit, lambda a, b: k_rbf(a, b, 1.0, e), sn2_ml)
    axes[1].plot(xfit, m, color=col, lw=2, label=lab)
axes[1].plot(xml, yml, "ko", ms=4, label="data")
axes[1].set_title("The overfit-lengthscale foil"); axes[1].set_xlabel("x"); axes[1].legend(fontsize=8)
save(fig, "ml-ii-occam")
```

![Left: log-evidence, data-fit, and complexity terms versus lengthscale. The data-fit term is highest (least negative) at tiny lengthscale and falls as ell grows; the complexity term rises with ell; their sum, the evidence, peaks at an intermediate lengthscale near 1.6. Right: the overfit GP mean at ell=0.05 spikes to each data point and slumps to zero between them, while the ML-II mean is a smooth curve tracking the data.](figures/20-gaussian-processes/ml-ii-occam.png)

**Reconcile.** The evidence peaks at $\ell=$ `1.581` (log-evidence `-6.573`) and *punishes* the tiny lengthscale. Read the decomposition: at $\ell=0.05$ the data-fit term is the best of the three (`-12.412` — the wiggly mean nearly interpolates), yet the complexity term collapses to `2.748`, and the total evidence craters to `-32.637`. At the ML-II optimum the fit is slightly worse (`-13.392`) but the complexity term is `29.792`, and the total wins at `-6.573`. Over-smoothing loses the other way: at $\ell=2.5$ the fit is far worse (`-24.903`) and the evidence is `-15.778`. The right panel shows the foil — the $\ell=0.05$ mean spikes to each point and reverts to $0$ between them (a classic overfit), while the ML-II mean is a clean smooth curve. This is signature experience S5, module 17, in function space: **complexity control is a consequence of integrating out the function, not an extra penalty you add.** (In practice you maximize the log-evidence over $(\ell,\eta^2,\sigma_n^2)$ jointly by gradient ascent; sklearn's `GaussianProcessRegressor` does exactly this.)

## 20.5 The GP posterior mean is kernel ridge regression

The frequentist special case, one more time. Kernel ridge regression (KRR) solves $\min_f \sum_i(y_i-f(x_i))^2+\lambda\|f\|_{\mathcal H}^2$ in the kernel's reproducing-kernel Hilbert space, with the representer-theorem solution $\hat f(x_*)=k_{*n}(K+\lambda I)^{-1}y$. Set $\lambda=\sigma_n^2$ and that is **exactly** the GP posterior *mean* $\mu_*=k_{*n}(K+\sigma_n^2 I)^{-1}y$. Same vector — the ridge penalty $\lambda$ is the noise variance, and the RKHS norm is the GP prior (module 06's MAP-is-penalized-MLE, module 14's ridge-is-a-Gaussian-prior, now in function space).

```python
from sklearn.kernel_ridge import KernelRidge
ellk, lam = 0.7, 0.1
krr = KernelRidge(alpha=lam, kernel="rbf", gamma=1.0/(2*ellk**2)).fit(xml[:, None], yml)
pred_krr = krr.predict(xgp[:, None])
m_gp, _ = gp_posterior(xml, yml, xgp, lambda a, b: k_rbf(a, b, 1.0, ellk), lam)
print(f"GP posterior mean vs kernel ridge: max|diff| = {np.max(np.abs(m_gp-pred_krr)):.2e}")
```

The two agree to `8.02e-09` — the GP posterior mean and sklearn's KernelRidge are the *same estimator*. The distinction is not the point prediction; it is that the GP also hands you the posterior *variance* (§20.3's band), which KRR discards. **KRR, support-vector regression's cousin, and the "kernel trick" you already knew are the mean of a Bayesian posterior over functions** — the frequentist keeps the mean and drops the uncertainty, exactly as in every prior module.

## 20.6 Teaser: Bayesian optimization finds an optimum in ~8 evaluations

If evaluating $f$ is expensive (a hyperparameter sweep, a lab experiment, a drug assay), you cannot grid-search. **Bayesian optimization** fits a GP to the evaluations so far, then uses the posterior to choose the next query by maximizing **expected improvement** (EI) — the expected amount by which a new point beats the best value seen, $\mathrm{EI}(x)=\mathbb E[\max(f_{\text{best}}-f(x),0)]$, which has a closed form under the Gaussian posterior. EI automatically balances exploiting low-mean regions against exploring high-variance ones.

```python
def forrester(x): return (6*x-2)**2 * np.sin(12*x-4)      # standard 1-D BO test; min near 0.757
grid = np.linspace(0, 1, 500)
true_min, true_x = forrester(grid).min(), grid[np.argmin(forrester(grid))]
print(f"BayesOpt target: true min f = {true_min:.4f} at x = {true_x:.4f}")

def expected_improvement(mu, sd, fbest, xi=0.01):
    sd = np.maximum(sd, 1e-9)
    z = (fbest - mu - xi)/sd
    return (fbest - mu - xi)*stats.norm.cdf(z) + sd*stats.norm.pdf(z)   # EI, closed form

Xev = np.array([0.0, 0.5, 1.0]); Yev = forrester(Xev)     # 3 initial evaluations
for _ in range(5):                                        # 5 EI steps -> 8 evaluations total
    yc = (Yev - Yev.mean())/(Yev.std() + 1e-9)            # standardize for a unit-scale GP
    m, v = gp_posterior(Xev, yc, grid, lambda a, b: k_rbf(a, b, 1.0, 0.15), 1e-6)
    xnext = grid[np.argmax(expected_improvement(m, np.sqrt(v), yc.min()))]
    Xev = np.append(Xev, xnext); Yev = np.append(Yev, forrester(xnext))
    print(f"  eval {len(Yev)}: query x={xnext:.3f}  best-so-far f={Yev.min():.4f}")
print(f"best after {len(Yev)} evaluations: {Yev.min():.4f} at x = {Xev[np.argmin(Yev)]:.4f}")

yc = (Yev - Yev.mean())/(Yev.std() + 1e-9)
m, v = gp_posterior(Xev, yc, grid, lambda a, b: k_rbf(a, b, 1.0, 0.15), 1e-6)
m_orig = m*(Yev.std()+1e-9) + Yev.mean(); sd = np.sqrt(np.maximum(v, 0))*(Yev.std()+1e-9)
fig, ax = plt.subplots()
ax.plot(grid, forrester(grid), "k:", lw=1.5, label="true f (hidden)")
ax.fill_between(grid, m_orig-1.96*sd, m_orig+1.96*sd, color="C0", alpha=0.2, label="GP 95%")
ax.plot(grid, m_orig, color="C1", lw=2, label="GP mean")
ax.scatter(Xev[:3], Yev[:3], c="k", s=45, zorder=5, label="initial evals")
ax.scatter(Xev[3:], Yev[3:], c="C3", s=60, zorder=5, label="EI-chosen evals")
ax.scatter([true_x], [true_min], marker="*", c="C2", s=220, zorder=6, label="true optimum")
ax.set_title("Bayesian optimization: 8 evaluations to the optimum")
ax.set_xlabel("x"); ax.set_ylabel("f(x)"); ax.legend(fontsize=8, loc="upper center")
save(fig, "bayesopt")
```

![A GP surrogate over the Forrester function on [0,1]. Three black initial points and five red EI-chosen points; the red points cluster tightly around the deep minimum near x=0.76, where a green star marks the true optimum. The GP mean tracks the true dotted curve closely near the sampled region, with a wide band on the unexplored left.](figures/20-gaussian-processes/bayesopt.png)

Starting from three evaluations at $x\in\{0,0.5,1\}$, EI walks straight downhill: the best-so-far improves `0.0001` → `-0.7280` → `-3.1595` → `-5.5911` → `-6.0207`, reaching the grid optimum `-6.0207` at $x=$ `0.7575` (true min `-6.0207` at `0.7575`) in **8 evaluations total** — no gradients, no grid search, just "fit a GP, ask where improvement is most expected, repeat." This is the M23 bridge: *acquisition functions turn a posterior over functions into a sequential decision* — line 4, driven by the GP of lines 2–3. It is how modern hyperparameter tuners (and many AutoML systems) work.

## 20.7 Teaser: wide neural networks are Gaussian processes (NNGP)

A one-hidden-layer network $f(x)=\sum_{j=1}^{H} v_j\,\tanh(w_j x + b_j)$ with random iid weights defines a *distribution over functions* — a prior. Neal (1996) observed that as the width $H\to\infty$, with output weights scaled $\mathrm{Var}[v_j]=\sigma_v^2/H$, this prior converges to a **Gaussian process**: $f(x)$ is a sum of $H$ iid terms, so the central limit theorem makes any finite set of function values jointly Gaussian. The random network's function-space prior *is* a GP, with a kernel computable from the activation.

**Predict.** As we widen the hidden layer $H=1\to10\to1000$, the marginal distribution of $f(x_0)$ across random networks approaches a Gaussian. Commit: does the *excess kurtosis* of $f(x_0)$ (0 for a Gaussian) shrink monotonically toward 0, and does the two-point correlation $\mathrm{corr}(f(x_0),f(x_1))$ keep drifting or lock onto a limit?

**Reason.** The naive intuition is that "a bigger network is a more complex, more flexible prior" — expecting the distribution to get *wilder* with width. The CLT says the opposite for the *marginals*: more units means more Gaussian, with a *fixed* covariance.

```python
def net_samples(width, xpts, nnets, gen, sw2=4.0, sb2=1.0, sv2=1.0):
    """nnets random 1-hidden-layer tanh nets, evaluated at xpts. Var(v_j)=sv2/width."""
    w = gen.normal(0, np.sqrt(sw2), (nnets, width))
    b = gen.normal(0, np.sqrt(sb2), (nnets, width))
    v = gen.normal(0, np.sqrt(sv2/width), (nnets, width))
    H = np.tanh(xpts[None, None, :]*w[:, :, None] + b[:, :, None])   # (nnets, width, npts)
    return np.einsum("nw,nwp->np", v, H)                            # (nnets, npts)

gen7 = np.random.default_rng(5)
pts = np.array([0.5, 1.5])
print("NNGP width sweep, f evaluated at x0=0.5 and x1=1.5:")
draws_by_width = {}
for width in (1, 10, 1000):
    S = net_samples(width, pts, 8000, gen7)
    draws_by_width[width] = S
    print(f"  H={width:4d}: sd(f(x0)) = {S[:, 0].std():.3f}   "
          f"excess kurtosis = {stats.kurtosis(S[:, 0]):+.3f}   "
          f"corr(f0,f1) = {np.corrcoef(S[:, 0], S[:, 1])[0, 1]:.3f}")

gridx = np.linspace(-3, 3, 120)
fig, axes = plt.subplots(1, 3, figsize=(12, 3.6), sharey=True)
for ax, width in zip(axes, (1, 10, 1000)):
    F = net_samples(width, gridx, 12, gen7)
    for f in F: ax.plot(gridx, f, lw=1, alpha=0.7)
    ax.set_title(f"width H = {width}"); ax.set_xlabel("x")
axes[0].set_ylabel("f(x)")
fig.suptitle("Random 1-hidden-layer nets: function-space prior approaches a GP as H grows", y=1.02)
save(fig, "nngp")
```

![Three panels of random-network function draws. Width 1: a dozen simple tanh-shaped step curves, visibly non-Gaussian and low-variety. Width 10: more varied, more wiggly curves. Width 1000: a rich family of smooth curves that look like draws from a stationary Gaussian process.](figures/20-gaussian-processes/nngp.png)

**Reconcile.** The excess kurtosis of $f(x_0)$ collapses monotonically toward the Gaussian value $0$: `1.179` at $H=1$, `0.247` at $H=10$, `0.107` at $H=1000$ — the marginals Gaussianize exactly as the CLT predicts. Meanwhile the standard deviation barely moves (`0.720` → `0.722`) and the two-point correlation *locks on* — `0.835` at $H=1$, `0.842` at $H=1000$ — it does **not** keep drifting, because the limiting covariance is fixed by the activation, independent of width. The panels tell the same story visually: width-1 nets are crude and repetitive, width-1000 draws look like GP samples. **A wide network's prior over functions is a GP** — the foundation of the "neural tangent kernel" and NNGP literature, and a bridge you will use again in module 25. (An infinitely wide network is Bayesian-linear in its last-layer features — module 14's setup, with the features learned rather than fixed.)

## 20.8 The cost of exactness, and two neighbors on the map

The GP posterior, evidence, and predictive all require solving with $K_y=K+\sigma_n^2I$, an $n\times n$ matrix. Cholesky is $O(n^3)$ time and $O(n^2)$ memory — fine at the $n\le200$ of this module, painful at $n=10^4$, impossible at $n=10^6$.

```python
print("exact-GP cost scales as n^3 (Cholesky of the n x n kernel matrix):")
for nn in (100, 200, 400, 800):
    print(f"  n={nn:4d}: relative cost (n/100)^3 = {(nn/100)**3:6.1f}x")
```

Doubling $n$ multiplies the cost `8.0`-fold; going from $n=100$ to $n=800$ is a `512.0`× jump. Two escapes, both worth knowing by name:

- **Sparse / inducing-point GPs** summarize the data through $m\ll n$ pseudo-inputs, dropping cost to $O(nm^2)$ (Snelson–Ghahramani FITC; Titsias's variational SVGP). The variational version *is* module 13's ELBO applied to a GP — approximate the exact posterior with a cheaper one and bound the evidence.
- **BART** (Bayesian Additive Regression Trees) is another prior over functions — a sum of regularized trees whose piecewise-constant jumps handle the discontinuities a smooth kernel cannot (module-26 reading-map entry).

The unifying idea outlasts the algebra: **a kernel, a wide network, and a tree ensemble are three ways to write a prior over functions**, and in every case inference is conditioning and prediction is marginalization — the same two lines.

## Bridge — kernel ridge, ISLP ch. 7, and the finite-basis limit

ISLP teaches splines and local regression as flexible curve-fitters, and kernels via the support-vector machine. This module supplies the joint distribution underneath all of them. A smoothing spline *is* the posterior mean of a GP with a particular kernel; the SVM/KRR predictor is the GP posterior mean (§20.5, machine-precision `8.02e-09`); a wide neural net's prior is a GP (§20.7). The through-line back to module 14 is literal: that module's basis expansion with $M$ features is this module at finite $M$, and sending $M\to\infty$ (§20.1, agreement `1.14e-14`) is what produced the kernel. "How many basis functions, how many knots, how wide a layer?" all dissolve into "which kernel, with what hyperparameters?" — and §20.4's marginal likelihood answers that with module 17's Occam factor rather than a validation set. The catch, exactly as in modules 07 and 14: a convenient kernel (RBF, for its smooth closed form) is not automatically a *defensible* one — the off-support band is only as trustworthy as the stationarity and smoothness the kernel assumes.

## Pitfalls

- **A non-positive-definite kernel matrix.** Rounding can make $K$ numerically indefinite, and Cholesky then fails. The idiom is to add a tiny **jitter** $10^{-8} I$ before factoring (used in every block above): it is a negligible extra noise variance that guarantees positive-definiteness. If you still get failures, your lengthscale is tiny relative to point spacing (near-duplicate rows) — increase jitter or $\ell$.
- **Confusing the latent-function band with the predictive band.** $\mathrm{Var}[f_*\mid y]$ (what §20.3 plots) excludes observation noise; a band for a *new observation* $\tilde y_*$ adds $\sigma_n^2$. Report the one your question asks for — calibration checks need the predictive band.
- **Extrapolating a stationary kernel.** An RBF GP reverts to the prior mean (usually 0) within a couple of lengthscales of the data (Exercise 20.3), so its extrapolations are confidently mean-reverting. If your function trends or oscillates, encode it (linear or periodic kernel) — the RBF will not invent structure it was not told about.
- **Forgetting to optimize $\sigma_n^2$.** Fixing the noise too low forces near-interpolation (overfit, wiggly mean); too high over-smooths. The marginal likelihood tunes it jointly with $\ell$ and $\eta^2$ — let it (§20.4).
- **Running exact GPs at scale.** Beyond a few thousand points the $O(n^3)$ cost bites; reach for inducing-point or variational GPs (§20.8) rather than waiting on a dense Cholesky.

## Exercises

**Exercise 20.1 — Which kernel can extrapolate a sine?**  *(surprising)*
*Setup:* Train a GP on 20 points of $\sin(x)$ over $[0,4\pi]$, then predict on the *future* interval $[4\pi,6\pi]$ — pure extrapolation. Compare an RBF kernel ($\ell=1$) against a periodic kernel (period $2\pi$).
*Predict:* Both kernels fit the training data perfectly. Will their extrapolation RMSE onto the true continuation be about equal, or will one crush the other?
*Reason:* "A good in-sample fit implies a good forecast" — the intuition that interpolation quality transfers to extrapolation.
*Run:*
```python
xtr = np.linspace(0, 4*np.pi, 20); ytr = np.sin(xtr)
xext = np.linspace(4*np.pi, 6*np.pi, 40); truth = np.sin(xext)
m_per, _ = gp_posterior(xtr, ytr, xext, lambda a, b: k_periodic(a, b, 1.0, 1.0, 2*np.pi), 1e-4)
m_rbf, _ = gp_posterior(xtr, ytr, xext, lambda a, b: k_rbf(a, b, 1.0, 1.0), 1e-4)
print(f"extrapolation RMSE: periodic = {np.sqrt(np.mean((m_per-truth)**2)):.4f}  "
      f"rbf = {np.sqrt(np.mean((m_rbf-truth)**2)):.4f}")
```
<details><summary>Reconcile</summary>

The periodic kernel extrapolates with RMSE `0.0000` — perfect — while the RBF manages only `0.6010`, near the amplitude of the signal it is trying to predict. Both fit the training data identically well, but they encode different *priors*: the periodic kernel knows the function repeats and continues the pattern; the RBF knows only "smooth, correlations decay over $\ell=1$," so beyond a lengthscale past the data it reverts to the prior mean $0$ and forecasts flatline. The lesson is the module's spine: **a GP's forecast is its prior speaking where the data are silent.** Good interpolation is no evidence of good extrapolation — that is governed entirely by the kernel's assumptions, which you chose.
</details>

**Exercise 20.2 — Noise level is the regularizer.**  *(ML bridge)*
*Setup:* Fit the §20.3 data with RBF ($\ell=0.7$) at three assumed noise levels $\sigma_n^2\in\{10^{-6},0.05,0.5\}$, and measure how far the posterior mean sits from the training targets, $\max_i|\,\mu(x_i)-y_i|$.
*Predict:* As $\sigma_n^2$ grows from $10^{-6}$ to $0.5$, does the mean stay pinned to the data (a GP always interpolates), or pull away?
*Reason:* "The GP is defined by its kernel; the noise is a detail" — treating $\sigma_n^2$ as cosmetic.
*Run:*
```python
for sn2 in (1e-6, 0.05, 0.5):
    m, _ = gp_posterior(xt, yt, xt, lambda a, b: k_rbf(a, b, 1.0, 0.7), sn2)
    print(f"sigma_n^2={sn2:7.5f}: max|mean - y| at training points = {np.max(np.abs(m-yt)):.4f}")
```
<details><summary>Reconcile</summary>

The mean pulls away from the data as noise grows: max residual `0.0000` (interpolation) → `0.0480` → `0.2888`. $\sigma_n^2$ is precisely the ridge penalty $\lambda$ of §20.5 — larger $\lambda$ = stronger regularization = a smoother mean that does not chase every point. This is the *same* knob as weight decay in a neural net and $\alpha$ in ridge regression (module 14): "assumed observation noise," "regularization strength," and "prior-vs-likelihood balance" are three names for one dial. Turning noise to zero recovers hard interpolation (and overfitting if the true function is noisy); the marginal likelihood exists to set it for you.
</details>

**Exercise 20.3 — How far until the GP forgets the data?**  *(surprising)*
*Setup:* One data point at $x=0$ with $f(0)=1$, RBF kernel $\ell=0.7$, nearly noiseless. Evaluate the posterior standard deviation at distances $d\cdot\ell$ for $d\in\{0,1,2,3,5\}$ (prior sd is $1$).
*Predict:* How many lengthscales from the data before the posterior sd is back to ~99% of the prior width — about 1, 3, or 10?
*Reason:* "Correlation decays gently, so the data should inform predictions many lengthscales out."
*Run:*
```python
for d in (0, 1, 2, 3, 5):
    _, v = gp_posterior(np.array([0.0]), np.array([1.0]), np.array([d*0.7]),
                        lambda a, b: k_rbf(a, b, 1.0, 0.7), 1e-6)
    print(f"d={d}*ell: posterior sd = {np.sqrt(v[0]):.4f}   (prior sd = 1.0)")
```
<details><summary>Reconcile</summary>

Posterior sd climbs `0.0010` (at the point) → `0.7951` (1$\ell$) → `0.9908` (2$\ell$) → `0.9999` (3$\ell$) → `1.0000` (5$\ell$). The data's reach is astonishingly short: by **two lengthscales** the GP has essentially forgotten the observation and reverted to the prior. The RBF correlation $\exp(-d^2/2)$ falls off *super*-exponentially, so "the correlation decays gently" is wrong — it decays like a Gaussian tail, and information is local. This is exactly why the §20.3 band balloons so fast off-support and why RBF extrapolation (Exercise 20.1) is hopeless: the lengthscale is not a mild preference, it is a hard horizon.
</details>

**Exercise 20.4 — Compute the NNGP kernel from the activation.**  *(ML bridge, surprising)*
*Setup:* §20.7 claimed the infinite-width kernel is "computable from the activation." Close that claim: the limiting covariance is $K(x,x')=\sigma_v^2\,\mathbb E_{w,b}[\tanh(wx+b)\tanh(wx'+b)]$ with $w\sim N(0,4)$, $b\sim N(0,1)$ — a 2-D integral over a *single unit's* weights, computable by Gauss–Hermite quadrature (no closed form for tanh, but quadrature is exact to machine precision here). Evaluate the analytic correlation between $f(0.5)$ and $f(1.5)$, then compare each empirical width's correlation to it.
*Predict:* Rank the widths $H\in\{1,10,1000\}$ by how close their empirical correlation lands to the analytic infinite-width value. Surely $H=1000$ (nearly infinite) is closest and $H=1$ (one neuron!) is farthest?
*Reason:* "Convergence to the limit is monotone in width — closer to $\infty$, closer to the limit kernel." That is true for the *shape* of the distribution; is it true for the covariance?
*Run:*
```python
def nngp_k(xa, xb, sw2=4.0, sb2=1.0, sv2=1.0, npts=80):
    """Infinite-width kernel K(xa,xb) = sv2 * E[tanh(w*xa+b) tanh(w*xb+b)] by Gauss-Hermite."""
    z, wq = np.polynomial.hermite_e.hermegauss(npts)     # E[g(Z)], Z ~ N(0,1)
    wq = wq / np.sqrt(2*np.pi)
    W, B = np.meshgrid(np.sqrt(sw2)*z, np.sqrt(sb2)*z, indexing="ij")
    wt = np.outer(wq, wq)
    return sv2*np.sum(np.tanh(W*xa + B)*np.tanh(W*xb + B)*wt)

k00, k11, k01 = nngp_k(0.5, 0.5), nngp_k(1.5, 1.5), nngp_k(0.5, 1.5)
corr_inf = k01/np.sqrt(k00*k11)
print(f"analytic infinite-width kernel: corr = {corr_inf:.4f}   sd(f(x0)) = {np.sqrt(k00):.4f}")
for width in (1, 10, 1000):
    S = net_samples(width, np.array([0.5, 1.5]), 8000, np.random.default_rng(5))
    cc = np.corrcoef(S[:, 0], S[:, 1])[0, 1]
    print(f"H={width:4d}: empirical corr = {cc:.4f}   |gap to analytic| = {abs(cc-corr_inf):.4f}")
```
<details><summary>Reconcile</summary>

The quadrature gives corr $=$ `0.8374` (and sd `0.7211`, matching §20.7's ~0.72). The ranking prediction fails: $H=1$ lands *closest* (gap `0.0021`), beating $H=1000$ (gap `0.0045`), with $H=10$ farthest (`0.0051`). The miss is that second moments do not converge with width — they are **exact at every width**: $f$ is a sum of $H$ iid units with output variance $\sigma_v^2/H$, so $\mathrm{Cov}[f(x),f(x')]=H\cdot\frac{\sigma_v^2}{H}\,\mathbb E[\tanh(wx+b)\tanh(wx'+b)]$ — the $H$ cancels. Every observed gap is pure Monte-Carlo noise (8,000 nets), so the "ranking" is a coin toss. What the CLT limit actually delivers is *Gaussianity of the shape* (the kurtosis collapse of §20.7), not the covariance, which one neuron already owns. This is why the NNGP kernel can be computed from a single unit's activation — and why an analytic kernel stands in for an infinitely wide Bayesian network (module 25).
</details>

## Takeaways

- **A GP is module 14 at $M=\infty$.** Weight-space basis regression and the kernel form give identical predictions (`1.14e-14`); sending the number of basis functions to infinity leaves only the kernel $k(x,x')=\phi(x)^\top\Sigma_w\phi(x')$, which for Gaussian bumps is the squared-exponential.
- **The kernel is a prior over functions you can draw.** RBF = very smooth, Matérn = rougher, periodic = repeating, linear = straight lines; the lengthscale $\ell$ is the wiggle scale, and choosing a kernel is choosing what "a plausible function" means.
- **The posterior is one Gaussian conditioning step.** `gaussian_condition` (module 05) on the joint of $(f_*,y)$ gives the exact posterior mean and band in ~20 lines; the band pinches to zero at noiseless data (`1.02e-06`) and reverts to the prior off-support (`0.9834`).
- **Interpolation vs smoothing is the single dial $\sigma_n^2$**, which is also the ridge penalty $\lambda$ — the GP posterior mean equals kernel ridge regression to machine precision (`8.02e-09`).
- **The marginal likelihood tunes the kernel with Occam built in.** Evidence = fit + complexity (module 17, function space); it peaks at a sensible lengthscale (`1.581`) and punishes an overfit tiny lengthscale despite its better training fit — no validation set required.
- **A posterior over functions powers decisions and rhymes with deep learning.** Expected improvement finds a 1-D optimum in 8 evaluations (`-6.0207`); a wide 1-hidden-layer network's prior converges to a GP (excess kurtosis `1.179`→`0.107`, correlation locked at `0.842`).
- **Exactness costs $O(n^3)$** (`512.0`× from $n=100$ to $800$); inducing-point/variational GPs and tree-based BART are the standard escapes — three priors over functions, one inference.

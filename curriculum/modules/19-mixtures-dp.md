# 19. Latent Structure: Mixtures and the Dirichlet Process

> **Spine.** Cluster labels are unknowns like any other — marginalize them; EM's point labels hide the uncertainty that Gibbs reveals, and a Dirichlet process lets the number of clusters grow with the data.
> **Which line?** Line 2 (condition on data to get a posterior over *labels and parameters*) and line 3 (predict by marginalizing the labels away). A mixture is a joint over `(data, hidden label, parameters)`; everything else is bookkeeping.
> **Promise.** After this module you can fit a Gaussian mixture two ways (EM and Gibbs) and say exactly what EM throws away, diagnose and repair label switching, cross a bimodal barrier with parallel tempering, and let a Dirichlet-process mixture infer the number of clusters instead of fixing it.
> **Prereqs.** Modules 05 (conjugacy, MVN toolkit), 11 (Gibbs, augmentation, agreement audits), 13 (EM as ELBO ascent — its *minimal* known-variance mixture; the full GMM is ours), 10 (the bimodal-trap chain, tempering promised), 01 (Pólya urn), 07 (nonidentifiability by symmetry). **Runtime.** ~15 s.
> **Sources.** Booklet ch. 13–14 + the stick-breaking insert; Neal (2000) "Markov chain sampling methods for DP mixture models" by concept.

A mixture model is the shortest interesting sentence in the four-line language. The joint is

$$p(x, z, \theta) = \underbrace{p(\theta)}_{\text{prior}}\;\underbrace{\pi_{z}}_{\text{label } z\sim\text{Categorical}(\pi)}\;\underbrace{p(x\mid \theta_{z})}_{\text{component }z\text{ emits }x},$$

with $z\in\{1,\dots,K\}$ a hidden **label** saying which component generated $x$. You never see $z$. That is the entire complication and the entire opportunity: clustering is *inference about the labels*, density estimation is *prediction with the labels marginalized away*, and the number of clusters $K$ is itself just another unknown you can put a prior on. This module walks that ladder — from a fixed-$K$ Gaussian mixture fit two ways, through the symmetry pathology the mixture likelihood always carries, to a Dirichlet process that refuses to fix $K$ at all.

## 19.1 A Gaussian mixture two ways: EM's point labels, Gibbs's label distributions

Module 13 built the *minimal* EM: a two-component 1-D mixture with known, equal variances and equal weights — bare enough to expose EM as coordinate ascent on the ELBO. We now cash the full object it deferred: a **2-D Gaussian mixture with unknown weights, means, and covariances**, fit by full EM and by a conjugate Gibbs sampler, so we can watch what each says about the one question a clustering is really asked — *which points belong where, and how sure are we?*

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import digamma

SLUG = "19-mixtures-dp"
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

The data: two moderately separated 2-D Gaussian blobs, deliberately close enough that a *band* of points along the perpendicular bisector is genuinely ambiguous. That band is where EM and Gibbs will part company.

```python
# 19.1 -- generate a 2-component 2-D Gaussian mixture with real overlap
n = 250
true_pi = np.array([0.55, 0.45])
true_mu = np.array([[0.0, 0.0], [2.6, 2.6]])
true_cov = np.array([[[1.0, 0.4], [0.4, 1.0]],
                     [[1.0, -0.3], [-0.3, 1.0]]])
z_true = (rng.random(n) > true_pi[0]).astype(int)
X = np.array([rng.multivariate_normal(true_mu[k], true_cov[k]) for k in z_true])
print(f"n={n}, component sizes = {np.bincount(z_true)}")
```

**Full EM.** The E-step forms responsibilities $r_{ik}=p(z_i{=}k\mid x_i,\theta)\propto \pi_k\,\mathcal N(x_i;\mu_k,\Sigma_k)$; the M-step sets each $\pi_k,\mu_k,\Sigma_k$ to the responsibility-weighted maximum-likelihood values. This is exactly module 13's two-step dance, now with weights and full covariances free. The incomplete-data log-likelihood climbs monotonically (the E-step re-tightens the ELBO to it at every sweep).

```python
# 19.1 -- full EM for a K-component 2-D GMM (unknown pi, mu, Sigma)
def em_gmm(X, K, rng, iters=100, tol=1e-6):
    n, d = X.shape
    # init: random points as means, global covariance, uniform weights
    mu = X[rng.choice(n, K, replace=False)].copy()
    Sig = np.array([np.cov(X.T)] * K)
    pi = np.full(K, 1.0 / K)
    ll_trace = []
    for _ in range(iters):
        # E-step: responsibilities and incomplete-data log-likelihood
        logr = np.stack([np.log(pi[k]) +
                         stats.multivariate_normal(mu[k], Sig[k]).logpdf(X)
                         for k in range(K)], axis=1)          # (n, K)
        ll = np.logaddexp.reduce(logr, axis=1)                # log p(x_i)
        ll_trace.append(ll.sum())
        r = np.exp(logr - ll[:, None])                        # (n, K)
        # M-step: weighted MLE
        Nk = r.sum(0)
        pi = Nk / n
        mu = (r.T @ X) / Nk[:, None]
        for k in range(K):
            dX = X - mu[k]
            Sig[k] = (r[:, k, None, None] * (dX[:, :, None] * dX[:, None, :])).sum(0) / Nk[k]
        if len(ll_trace) > 1 and ll_trace[-1] - ll_trace[-2] < tol:
            break
    return pi, mu, Sig, r, np.array(ll_trace)

pi_em, mu_em, Sig_em, r_em, ll_em = em_gmm(X, 2, rng)
mono = bool(np.all(np.diff(ll_em) >= -1e-8))
print(f"EM: {len(ll_em)} iters, log-lik {ll_em[0]:.2f} -> {ll_em[-1]:.2f}, monotone {mono}")
# canonical order: component with smaller x-mean is 'cluster 0'
o_em = np.argsort(mu_em[:, 0])
resp_lo_em = r_em[:, o_em[0]]                                 # P(point in the low cluster), EM plug-in
print(f"EM means (ordered) = {np.round(mu_em[o_em, 0], 2)}, {np.round(mu_em[o_em, 1], 2)}")
```

**Conjugate Gibbs.** Same model, but now every unknown is sampled from its full conditional (module 11's recipe). The conjugate prior for a Gaussian component is Normal–Inverse-Wishart: $\Sigma_k\sim\mathrm{IW}(\nu_0,\Psi_0)$, $\mu_k\mid\Sigma_k\sim\mathcal N(m_0,\Sigma_k/\kappa_0)$; the weights get a Dirichlet, $\pi\sim\mathrm{Dir}(a_0\mathbf 1)$. Given the labels the component updates are conjugate; given the parameters the labels are a categorical draw. We add one extra move — a global relabeling swap — to expose the symmetry of §19.2; ignore it for now.

```python
# 19.1 -- conjugate Gibbs for the same GMM (Normal-Inverse-Wishart + Dirichlet)
def gibbs_gmm(X, K, rng, n_sweeps=1500, p_swap=0.02):
    n, d = X.shape
    m0, kappa0, nu0 = X.mean(0), 0.1, d + 2
    Psi0 = np.cov(X.T) * (nu0 - d - 1)                        # so E[Sigma] = cov(X)
    a0 = 1.0
    z = rng.integers(0, K, size=n)
    mu_tr = np.zeros((n_sweeps, K, d))
    z_tr = np.zeros((n_sweeps, n), dtype=np.int8)
    for t in range(n_sweeps):
        counts = np.bincount(z, minlength=K)
        pi = rng.dirichlet(a0 + counts)
        mu = np.zeros((K, d)); Sig = np.zeros((K, d, d))
        for k in range(K):
            Xk = X[z == k]; nk = len(Xk)
            if nk == 0:                                       # empty: draw from prior
                Sig[k] = stats.invwishart(df=nu0, scale=Psi0).rvs(random_state=rng)
                mu[k] = rng.multivariate_normal(m0, Sig[k] / kappa0)
                continue
            xbar = Xk.mean(0); kn = kappa0 + nk; nun = nu0 + nk
            mn = (kappa0 * m0 + nk * xbar) / kn
            S = (Xk - xbar).T @ (Xk - xbar)
            dm = (xbar - m0)[:, None]
            Psin = Psi0 + S + (kappa0 * nk / kn) * (dm @ dm.T)
            Sig[k] = stats.invwishart(df=nun, scale=Psin).rvs(random_state=rng)
            mu[k] = rng.multivariate_normal(mn, Sig[k] / kn)
        # global label-swap move (K=2): posterior is invariant, so it always "fits"
        if K == 2 and rng.random() < p_swap:
            mu, Sig, pi = mu[::-1].copy(), Sig[::-1].copy(), pi[::-1].copy()
            z = 1 - z
        # sample labels z_i ~ Categorical(responsibilities)
        logp = np.stack([np.log(pi[k]) +
                         stats.multivariate_normal(mu[k], Sig[k]).logpdf(X)
                         for k in range(K)], axis=1)
        logp -= logp.max(1, keepdims=True)
        P = np.exp(logp); P /= P.sum(1, keepdims=True)
        z = (np.cumsum(P, 1) > rng.random(n)[:, None]).argmax(1)
        mu_tr[t], z_tr[t] = mu, z
    return mu_tr, z_tr

mu_tr, z_tr = gibbs_gmm(X, 2, rng)
burn = 500
# relabel each post-burn sweep by mean-x ordering, then average the labels
prob_lo_gibbs = np.zeros(n)
for t in range(burn, mu_tr.shape[0]):
    lo = np.argsort(mu_tr[t][:, 0])[0]                        # which raw label is the low cluster
    prob_lo_gibbs += (z_tr[t] == lo)
prob_lo_gibbs /= (mu_tr.shape[0] - burn)
print(f"Gibbs post-burn sweeps = {mu_tr.shape[0] - burn}")
```

Now the beat the panel calls the emotional core.

**Predict.** Call a point "uncertain" if its probability of belonging to the low cluster lands in $[0.1, 0.9]$ — neither method is willing to commit. EM reports one responsibility per point (a plug-in at the fitted $\hat\theta$); Gibbs reports a posterior label probability that has *also* averaged over where the boundary might be. Commit now: will the two methods flag roughly the **same** number of uncertain points, or will one flag noticeably more? The naive read — "both see the same overlapping blobs, so the ambiguous band is the same band" — says roughly equal.

*Reason:* the naive intuition treats the decision boundary as a fixed line and label uncertainty as purely aleatoric (the blobs overlap), forgetting that the boundary's *location* is itself uncertain.

```python
# 19.1 -- how many points does each method call genuinely uncertain?
unc_em = int(((resp_lo_em > 0.1) & (resp_lo_em < 0.9)).sum())
unc_gibbs = int(((prob_lo_gibbs > 0.1) & (prob_lo_gibbs < 0.9)).sum())
print(f"uncertain points (label prob in [0.1,0.9]):  EM {unc_em}   Gibbs {unc_gibbs}")
# a point EM is 'sure' about but Gibbs is not
gap = np.abs(resp_lo_em - prob_lo_gibbs)
i = int(gap.argmax())
print(f"widest-disagreement point: EM P(lo)={resp_lo_em[i]:.3f}  Gibbs P(lo)={prob_lo_gibbs[i]:.3f}")
```

**Reconcile.** Gibbs flags `38` uncertain points to EM's `24` — more than half again as many. EM's boundary is a knife-edge: responsibilities flip from ~1 to ~0 across a razor-thin strip because they are evaluated at a *single* fitted boundary. Gibbs samples the boundary too; every plausible position smears the ambiguous strip wider, so more points inherit a genuinely split label. At the single worst-disagreement point EM is `0.916` sure of the low cluster while Gibbs gives it only `0.837` — EM's confidence is partly an artifact of conditioning on one $\hat\theta$ as if it were the truth. This is module 05's predictive-vs-plug-in lesson wearing a clustering costume: **the plug-in throws away epistemic uncertainty, and here the discarded uncertainty is exactly "where is the boundary."** The uncertainty map makes it visible.

```python
# 19.1 -- figure: EM's crisp responsibilities vs Gibbs's smeared label posterior
fig, ax = plt.subplots(1, 2, figsize=(11, 4.4), sharex=True, sharey=True)
for a, prob, ttl in [(ax[0], resp_lo_em, "EM: plug-in responsibility (one $\\hat\\theta$)"),
                     (ax[1], prob_lo_gibbs, "Gibbs: posterior label probability")]:
    sc = a.scatter(X[:, 0], X[:, 1], c=prob, cmap="coolwarm", vmin=0, vmax=1,
                   s=28, edgecolor="k", linewidth=0.3)
    band = (prob > 0.1) & (prob < 0.9)
    a.scatter(X[band, 0], X[band, 1], s=90, facecolor="none",
              edgecolor="k", linewidth=1.2, label=f"uncertain ({band.sum()})")
    a.set(title=ttl, xlabel="$x_1$"); a.legend(loc="upper left")
ax[0].set_ylabel("$x_2$")
fig.colorbar(sc, ax=ax, label="P(low cluster)", shrink=0.85)
save(fig, "gmm_uncertainty")
```

![Two scatter panels of the same 250 points colored by probability of belonging to the low cluster. Left (EM): color flips abruptly across a thin diagonal band, few circled uncertain points. Right (Gibbs): the color transition is a visibly wider gradient with more circled uncertain points along the boundary.](figures/19-mixtures-dp/gmm_uncertainty.png)

The two panels agree on the confident points and disagree on the boundary — precisely where a downstream decision (which customer segment? which cell type?) is most likely to matter. EM is not *wrong*; it answers a narrower question ("given the best-fit clustering, which side?") than the one clustering is usually asked ("could this point plausibly be the other type?").

## 19.2 Label switching: the symmetry the mixture likelihood cannot break

The Gibbs sampler above hid a scandal. The mixture likelihood is exactly invariant under permuting the component labels: relabel "cluster 0 $\leftrightarrow$ cluster 1" together with their parameters and the joint density is unchanged. So the posterior has $K!$ identical modes, and no amount of data breaks the tie — this is module 07's **nonidentifiability by symmetry**, the cleanest instance in the course. A sampler that mixes *correctly* must visit all $K!$ labelings; when it does, any per-component summary (the trace of $\mu_1$) becomes meaningless, because "$\mu_1$" is not a well-defined quantity.

Our sampler carried a global label-swap move for exactly this reason: it exposes the switching that a sticky single-chain Gibbs would silently hide. Left raw, the component-mean traces jump between the two labelings.

**Predict.** Before looking at the traces: average the raw $\mu_1$ ($x$-coordinate) trace over the whole run, the way you would summarize any MCMC output. What number comes out — near the low mean $0$, near the high mean $2.6$, or near the midpoint $1.3$? And is that number a parameter of anything? The naive intuition: "a trace mean estimates its parameter."

```python
# 19.2 -- label switching: raw traces swap; ordering constraint fixes them
raw0, raw1 = mu_tr[:, 0, 0], mu_tr[:, 1, 0]                  # x-mean of raw components 0 and 1
n_swaps = int((np.sign(raw0 - raw1)[1:] != np.sign(raw0 - raw1)[:-1]).sum())
print(f"naive time-average of raw mu_1 trace = {raw0[burn:].mean():.2f}"
      f"   (true means: 0.0 and 2.6)")
# post-hoc relabel by ordering: force component means to be increasing in x each sweep
srt = np.sort(mu_tr[:, :, 0], axis=1)
lo_fixed, hi_fixed = srt[:, 0], srt[:, 1]
print(f"raw traces cross labels {n_swaps} times in {mu_tr.shape[0]} sweeps")
print(f"ordered means settle at  low {lo_fixed[burn:].mean():.2f}  high {hi_fixed[burn:].mean():.2f}"
      f"  (truth 0.0 and 2.6)")

fig, ax = plt.subplots(1, 2, figsize=(11, 3.8), sharey=True)
ax[0].plot(raw0, lw=0.6, color="C0", label="raw comp 0")
ax[0].plot(raw1, lw=0.6, color="C1", label="raw comp 1")
ax[0].set(title="Raw label traces: $\\mu$ swaps between modes",
          xlabel="Gibbs sweep", ylabel="component mean ($x_1$)")
ax[0].legend(loc="center right")
ax[1].plot(lo_fixed, lw=0.6, color="C2", label="ordered: low")
ax[1].plot(hi_fixed, lw=0.6, color="C3", label="ordered: high")
ax[1].set(title="Ordering constraint $\\mu^{(1)}_1<\\mu^{(2)}_1$ removes it",
          xlabel="Gibbs sweep")
ax[1].legend(loc="center right")
save(fig, "label_switching")
```

![Left: two overlapping traces that repeatedly jump past each other between roughly 0 and 2.6, so neither is a stable estimate of a single mean. Right: after sorting components by x-mean each sweep, two clean well-separated bands near 0 and 2.6.](figures/19-mixtures-dp/label_switching.png)

**Reconcile.** The naive time-average lands at `1.70` — near *neither* true mean. It is a blend of the two, weighted by how long this particular run happened to spend in each labeling (the raw traces cross `27` times), and in the long run — as the swap move equalizes time across the two labelings — it converges to the meaningless midpoint $\approx1.3$. Either way it estimates *nothing*: the "trace mean estimates its parameter" reflex fails because there is no parameter — the labeling is not identified, so the functional you averaged is not invariant under the posterior's symmetry. The fix is an **identifiability constraint**: pick a canonical labeling and enforce it. The simplest is an ordering constraint — relabel every sweep so the component means increase in the first coordinate — after which the "low" and "high" means settle cleanly at `-0.01` and `2.56`, recovering the truth. (Ordering constraints can bias estimates when components genuinely overlap in the ordered coordinate; the more robust industrial tool is post-hoc **relabeling algorithms** that permute each draw to best match a reference labeling, e.g. Stephens' method — same idea, less arbitrary anchor.) This is why §19.1's uncertainty map relabeled by ordering before averaging: without it, every point's label probability would collapse to `0.5` by symmetry, and the map would be blank.

> **Label switching is not a bug to be silenced but a symmetry to be quotiented.** The posterior really does have $K!$ equivalent modes; a well-mixing sampler really should visit them; you restore meaning by choosing a representative from each equivalence class, not by hoping the sampler stays stuck (a stuck sampler is *under*-exploring — it looks stable and is wrong).

## 19.3 When the barrier is real: parallel tempering

Label switching is a benign multimodality — the modes are copies. Mixtures also produce *malign* multimodality, where genuinely different explanations of the data are separated by a valley of low posterior density, and a random-walk sampler cannot cross it. Module 10 planted a chain in an equal mixture of $\mathcal N(-5,1)$ and $\mathcal N(+5,1)$ and watched it declare, with perfect internal consistency, that one mode held all the mass: `0` crossings in 40,000 iterations. It promised the fix here. This is it.

**Parallel tempering** runs a ladder of *flattened* replicas of the target, $p_\beta(x)\propto p(x)^{\beta}$ with inverse temperatures $1=\beta_1>\beta_2>\dots>\beta_M>0$. The cold chain ($\beta=1$) samples the true posterior; hot chains ($\beta$ small) see a nearly flat landscape and stride across barriers freely. Periodically, adjacent chains propose to **swap** states, accepted with a Metropolis probability that keeps every chain stationary. A mode discovered by a hot chain migrates down the ladder into the cold chain — the cold chain crosses the barrier not by walking over it but by *trading places* with a chain that never saw it. Temperature is the same knob as module 18's power posterior and module 10's simulated annealing; here we run the whole ladder at once instead of cooling one chain.

```python
# 19.3 -- parallel tempering on a two-well target; plain chain vs tempered ladder
def two_well_logp(x):                                        # equal mix of N(-5,1), N(5,1)
    c = -np.log(2) - 0.5 * np.log(2 * np.pi)
    return np.logaddexp(c - 0.5 * (x + 5) ** 2, c - 0.5 * (x - 5) ** 2)

def run_pt(temps, rng, n_steps=20000, step=1.0):
    beta = 1.0 / np.asarray(temps, float)
    K = len(temps)
    x = np.full(K, -5.0)                                     # all start in the LEFT well
    lp = two_well_logp(x)
    cold = np.zeros(n_steps); n_acc = n_prop = 0
    for t in range(n_steps):
        prop = x + rng.normal(0, step, K)                   # within-temperature RW-MH
        lpp = two_well_logp(prop)
        acc = np.log(rng.random(K)) < beta * (lpp - lp)
        x = np.where(acc, prop, x); lp = np.where(acc, lpp, lp)
        if K > 1:                                           # one adjacent swap proposal
            j = rng.integers(0, K - 1); n_prop += 1
            d = (beta[j] - beta[j + 1]) * (lp[j + 1] - lp[j])
            if np.log(rng.random()) < d:
                x[[j, j+1]] = x[[j+1, j]]; lp[[j, j+1]] = lp[[j+1, j]]; n_acc += 1
        cold[t] = x[0]
    swap_rate = n_acc / n_prop if n_prop else 0.0
    return cold, swap_rate

plain, _ = run_pt([1.0], rng)                               # single cold chain, no ladder
tempered, srate = run_pt([1.0, 2.0, 4.0, 8.0], rng)        # 4-rung ladder
def frac_right(c): return float((c > 0).mean())
print(f"plain single chain : P(x>0) = {frac_right(plain):.3f}  (truth 0.5)")
print(f"tempered cold chain: P(x>0) = {frac_right(tempered):.3f}  swap accept {srate:.2f}")
```

**Predict.** Both chains start in the *left* well. The plain chain estimates $P(x>0)$; commit to its value before reading on. Naive intuition ("it's a valid MCMC sampler, it will eventually mix") says $\approx 0.5$.

**Reconcile.** The plain chain returns $P(x>0)=$ `0.000` — trapped in the left well for all 20,000 steps, exactly module 10's failure, because the RW step tuned to explore one well (width 1) cannot leap a gap of 10. The tempered cold chain returns `0.532`, essentially the truth, with swaps accepted `0.79` of the time — often enough to ferry the right mode down from the hot rungs. Same cold target, same random-walk proposal; the only addition is a ladder of hotter replicas and a swap move, and the barrier that was impassable becomes routine.

```python
# 19.3 -- figure: the cold marginal, trapped vs tempered
fig, ax = plt.subplots(1, 2, figsize=(11, 3.8))
grid = np.linspace(-9, 9, 400)
dens = np.exp(two_well_logp(grid))
for a, c, ttl in [(ax[0], plain, "Plain chain: trapped in the left well"),
                  (ax[1], tempered, "Tempered ladder: both wells visited")]:
    a.hist(c, bins=60, density=True, color="C0", alpha=0.6)
    a.plot(grid, dens, "k--", lw=1.5, label="target")
    a.set(title=ttl, xlabel="$x$", ylabel="density"); a.legend()
save(fig, "tempering")
```

![Left: a histogram of the plain cold chain piled entirely on the left mode near -4, with the true two-humped target dashed over it — the right hump is empty. Right: the tempered cold chain's histogram fills both humps, matching the target.](figures/19-mixtures-dp/tempering.png)

The mixing-time story is spectral (module 10): the barrier drives the second eigenvalue of the transition kernel toward 1 and the relaxation time toward infinity, *exponentially* in the barrier height. Tempering does not lower the barrier; it opens a fast lane around it. The same idea, walked sequentially from prior ($\beta\to0$) to posterior ($\beta=1$), is Sequential Monte Carlo (modules 18, 21).

## 19.4 The Chinese restaurant process: letting $K$ grow

So far $K$ was fixed. But how many clusters *are* there? Fixing $K$ and comparing by evidence (module 17) is one answer; the nonparametric answer is to let $K$ grow with the data. The generative device is the **Chinese restaurant process (CRP)**, and it is module 01's Pólya urn with an escape hatch for new colors.

Customers enter a restaurant with infinitely many tables. Customer $i$ sits at an occupied table with probability proportional to how many already sit there, and at a *new* table with probability proportional to a concentration $\alpha>0$:

$$P(\text{customer }i\text{ joins table }c) = \frac{n_c}{\alpha + i - 1}, \qquad P(\text{new table}) = \frac{\alpha}{\alpha + i - 1}.$$

Occupied tables get more attractive as they fill — "rich get richer," the Pólya-urn reinforcement of module 01 — while $\alpha$ leaks a steady trickle of new tables. A remarkable simplification falls out for the count $K_n$ of occupied tables: whether customer $i$ opens a new table depends *only on $i$*, not on the seating so far, with probability $\alpha/(\alpha+i-1)$. So

$$K_n = \sum_{i=1}^{n} B_i, \qquad B_i \sim \mathrm{Bernoulli}\!\Big(\tfrac{\alpha}{\alpha+i-1}\Big)\ \text{independent}.$$

A sum of independent Bernoullis: its mean is a closed form, and — the panel's sev-1 correction — that closed form is a **digamma**, not a logarithm:

$$\mathbb E[K_n] = \sum_{i=1}^{n}\frac{\alpha}{\alpha+i-1} = \alpha\big[\psi(\alpha+n)-\psi(\alpha)\big].$$

```python
# 19.4 -- CRP table counts are a sum of INDEPENDENT Bernoulli(alpha/(alpha+i-1))
N, reps = 500, 2000
ns = np.arange(1, N + 1)
fig, ax = plt.subplots(figsize=(7.2, 4.4))
for a, col in [(1.0, "C0"), (2.0, "C1"), (5.0, "C2")]:
    p_new = a / (a + ns - 1)                                 # P(customer i opens a new table)
    Bern = rng.random((reps, N)) < p_new
    Kn_sim = np.cumsum(Bern, axis=1).mean(0)                 # simulated E[K_n]
    EK_exact = a * (digamma(a + ns) - digamma(a))            # exact digamma curve
    EK_asymp = a * np.log1p(ns / a)                          # asymptotic alpha*ln(1+n/alpha)
    ax.plot(ns, Kn_sim, col, lw=1.2, alpha=0.7,
            label=f"$\\alpha={a:.0f}$ simulated")
    ax.plot(ns, EK_exact, "k", lw=1.0)
    ax.plot(ns, EK_asymp, col, ls=":", lw=1.0)
    print(f"alpha={a:.0f}: E[K_500] exact {EK_exact[-1]:.3f}  sim {Kn_sim[-1]:.3f}  "
          f"asymp a*ln(1+n/a) {EK_asymp[-1]:.3f}  crude a*ln n {a*np.log(N):.2f}  "
          f"max|sim-exact| {np.abs(Kn_sim-EK_exact).max():.3f}")
ax.set(xlabel="customers $n$", ylabel="expected occupied tables $E[K_n]$",
       title="CRP growth: exact digamma (black) vs simulation vs asymptote (dotted)")
ax.legend()
save(fig, "crp_growth")
```

![Three rising curves for alpha 1, 2, 5; simulated means sit exactly on the solid black digamma curves, while the dotted asymptotic curves run slightly below each, closing the gap as n grows.](figures/19-mixtures-dp/crp_growth.png)

Before reading the gap off the figure, commit to a direction: does the popular shorthand $\alpha\log n$ *over*- or *under*-count clusters at $n=500$? (Ex 19.2 presses the same misconception from the $\alpha$ side.) The simulated means land on the exact digamma curves to within Monte Carlo noise (max gap `0.161` over all $n$), and the number of clusters grows like $\log n$: at $\alpha=1$, $\mathbb E[K_{500}]=$ `6.793` (which is exactly the harmonic number $H_{500}$, since $\alpha=1$ makes $\psi(1+n)-\psi(1)=H_n$); at $\alpha=5$, `23.587`. The dotted curves are the asymptotic form $\alpha\ln(1+n/\alpha)$, which runs below the truth and only closes the gap as $n$ grows — the popular shorthand "$\mathbb E[K_n]\approx\alpha\log n$" is the *further* $n\gg\alpha$ limit of that, and at finite $n$ it misses in a direction that *depends on $\alpha$* (the trap in the Predict: there is no fixed direction): at $\alpha=1$ it undercounts (`6.21` vs the exact `6.793`), while at $\alpha=5$ it overcounts badly (`31.07` vs `23.587`), because dropping the $+1$ inside $\ln(1+n/\alpha)$ and the digamma corrections trade places as $\alpha$ grows. Two consequences worth carrying: clusters accumulate slowly, so a DP is a *parsimonious* prior on $K$; and $\alpha$ is a genuine dial on granularity, not a nuisance.

The CRP inherits **exchangeability** from the Pólya urn (module 01): the probability of a seating configuration depends only on the *table sizes*, not the order customers arrived. Two sequences that induce the same partition of $\{1,\dots,n\}$ have identical probability.

```python
# 19.4 -- CRP partitions are exchangeable: probability depends only on cluster sizes
def crp_seq_logprob(labels, alpha):
    counts = {}; logp = 0.0
    for i, c in enumerate(labels):
        denom = alpha + i                                    # alpha + (i) since i is 0-based
        logp += np.log(alpha / denom) if c not in counts else np.log(counts[c] / denom)
        counts[c] = counts.get(c, 0) + 1
    return logp
a = 2.0
# "1,1,2" -> partition {{0,1},{2}};  "1,2,1" -> {{0,2},{1}}: same sizes (2,1)
p_A = crp_seq_logprob([0, 0, 1], a)
p_B = crp_seq_logprob([0, 1, 0], a)
print(f"CRP log-prob of two size-(2,1) partitions: {p_A:.6f} vs {p_B:.6f}  "
      f"equal={np.isclose(p_A, p_B)}")
```

Both orderings score `-1.791759` — same partition type, same probability. That order-invariance is the whole reason the CRP defines a coherent prior on clusterings: by de Finetti (module 01) an exchangeable sequence is a mixture over an underlying random measure, and here that measure is the Dirichlet process.

## 19.5 Stick-breaking and a Dirichlet-process mixture that chooses $K$

The CRP describes the *labels*; the **Dirichlet process** $\mathrm{DP}(\alpha, G_0)$ describes the *random distribution* they are drawn from — a distribution over distributions, discrete with probability one, with base measure $G_0$ and concentration $\alpha$ (booklet ch. 14). Its most computable face is **stick-breaking** (Sethuraman 1994; the booklet's stick-breaking insert): break a unit stick at a $\mathrm{Beta}(1,\alpha)$ fraction, keep the piece as the first weight, recurse on the remainder.

$$\omega_j = \gamma_j\prod_{i<j}(1-\gamma_i),\qquad \gamma_j\stackrel{iid}{\sim}\mathrm{Beta}(1,\alpha),\qquad \sum_j\omega_j = 1.$$

The weights decay geometrically in expectation, $\mathbb E[\omega_j]=\frac{1}{1+\alpha}\big(\frac{\alpha}{1+\alpha}\big)^{j-1}$, so a handful of components carry almost all the mass — the source of the DP's parsimony.

```python
# 19.5 -- stick-breaking weights: geometric decay, sum to one
def stick_break(alpha, L, rng):
    v = rng.beta(1.0, alpha, size=L); v[-1] = 1.0            # truncate: last stick takes the rest
    return v * np.concatenate([[1.0], np.cumprod(1 - v[:-1])])
L = 20
for a in (1.0, 5.0):
    W = np.array([stick_break(a, L, rng) for _ in range(4000)])
    eff = np.exp(-(W * np.log(W + 1e-300)).sum(1)).mean()    # mean exp-entropy = "effective #"
    print(f"alpha={a:.0f}: E[w_1..3] = {np.round(W.mean(0)[:3], 3)}  "
          f"(geom pred {np.round([(1/(1+a))*(a/(1+a))**j for j in range(3)], 3)})  "
          f"effective components {eff:.1f}")

fig, ax = plt.subplots(figsize=(7.2, 3.6))
for a, col in [(1.0, "C0"), (5.0, "C1")]:
    ax.bar(np.arange(L) + (0.2 if a == 5 else -0.2), stick_break(a, L, rng),
           width=0.4, color=col, label=f"$\\alpha={a:.0f}$")
ax.set(xlabel="component index $j$", ylabel="weight $\\omega_j$",
       title="Stick-breaking: small $\\alpha$ concentrates mass on few sticks")
ax.legend()
save(fig, "stick_breaking")
```

![Bar chart of the first twenty stick-breaking weights for alpha 1 and alpha 5; alpha=1 dumps most weight on the first two or three sticks, alpha=5 spreads a smaller weight across many more.](figures/19-mixtures-dp/stick_breaking.png)

The empirical means match the geometric prediction, and the "effective number of components" (exponentiated weight entropy) is `3.0` at $\alpha=1$ versus `9.4` at $\alpha=5$ — $\alpha$ tunes how many sticks matter. A **Dirichlet-process mixture** attaches a Gaussian to each stick, $x\mid z\sim\mathcal N(\mu_z,\sigma_z^2)$ with $(\mu_z,\sigma_z^2)\sim G_0$, and lets the data decide how many sticks light up. We fit the truncated version (Ishwaran–Zarepour: cap at $L$ sticks, exact as $L\to\infty$) by the blocked Gibbs sampler the booklet's insert derives, whose one non-obvious full conditional is the stick weight

$$\gamma_j\mid\cdot\ \sim\ \mathrm{Beta}\big(1 + n_j,\ \alpha + \textstyle\sum_{\ell>j} n_\ell\big),$$

with $n_j$ the number of points currently at component $j$ — Beta–Bernoulli conjugacy on the sticks. (If you hold the handwritten insert: this is the $\delta_1=0$ — DP, not Pitman–Yor — special case of its two-parameter stick weight $\mathrm{Beta}(1-\delta_1+e_p,\ \tfrac{\delta_2}{1-\delta_2}+(p-1)\delta_1+f_p)$, with $e_p\leftrightarrow n_j$, $f_p\leftrightarrow\sum_{\ell>j}n_\ell$, and $\tfrac{\delta_2}{1-\delta_2}\leftrightarrow\alpha$.) The test data is galaxy-velocity-like: several well-separated 1-D clumps, the classic setting where "how many clusters?" has no clean answer and the point is to let the posterior spread over $K$.

```python
# 19.5 -- truncated DP-mixture (stick-breaking blocked Gibbs) on galaxy-like 1-D data
true_locs = np.array([10.0, 18.0, 23.0, 32.0])
true_wts = np.array([0.2, 0.35, 0.3, 0.15])
true_sd = np.array([0.5, 0.8, 0.7, 0.5])
m = len(true_locs)
comp = rng.choice(m, size=150, p=true_wts)
y = rng.normal(true_locs[comp], true_sd[comp])
print(f"galaxy-like data: n={len(y)}, {m} true clusters at {true_locs}")

def dp_mixture_gibbs(y, L, alpha, rng, n_sweeps=1500, burn=500):
    n = len(y)
    m0, kappa0, a0, b0 = y.mean(), 0.05, 2.0, 0.5 * y.var()  # Normal-InvGamma base G0
    z = rng.integers(0, min(L, 4), size=n)
    K_tr = np.zeros(n_sweeps, dtype=int)
    for t in range(n_sweeps):
        counts = np.bincount(z, minlength=L)
        sum_gt = counts[::-1].cumsum()[::-1] - counts        # sum_{l>j} n_l
        v = rng.beta(1 + counts, alpha + sum_gt); v[-1] = 1.0
        w = v * np.concatenate([[1.0], np.cumprod(1 - v[:-1])])
        mu = np.empty(L); s2 = np.empty(L)
        for j in range(L):
            yj = y[z == j]; nj = len(yj)
            if nj == 0:                                      # empty stick: draw G0 from prior
                s2[j] = 1.0 / rng.gamma(a0, 1 / b0)
                mu[j] = rng.normal(m0, np.sqrt(s2[j] / kappa0)); continue
            kn = kappa0 + nj; mn = (kappa0 * m0 + yj.sum()) / kn
            an = a0 + nj / 2
            bn = b0 + 0.5 * ((yj - yj.mean()) ** 2).sum() + 0.5 * kappa0 * nj / kn * (yj.mean() - m0) ** 2
            s2[j] = 1.0 / rng.gamma(an, 1 / bn)              # InvGamma via reciprocal-Gamma (M11)
            mu[j] = rng.normal(mn, np.sqrt(s2[j] / kn))
        logN = -0.5 * np.log(2 * np.pi * s2) - 0.5 * (y[:, None] - mu) ** 2 / s2
        logp = np.log(w + 1e-300) + logN
        logp -= logp.max(1, keepdims=True)
        P = np.exp(logp); P /= P.sum(1, keepdims=True)
        z = (np.cumsum(P, 1) > rng.random(n)[:, None]).argmax(1)
        K_tr[t] = len(np.unique(z))
    return K_tr[burn:]

K_post = dp_mixture_gibbs(y, L=15, alpha=1.0, rng=rng)
vals, cnts = np.unique(K_post, return_counts=True)
pmf = cnts / cnts.sum()
print("posterior over #occupied clusters K:")
for k, pk in zip(vals, pmf):
    print(f"  K={k}: {pk:.3f}")
print(f"posterior mode K = {vals[pmf.argmax()]}, mean K = {K_post.mean():.2f}  (truth {m})")
```

**Predict.** We truncated at $L=15$ sticks but generated from `4` clusters. Where does the posterior over the number of *occupied* clusters land — pinned at 15 (it can use all the sticks), at 4, or smeared? Naive intuition ("more capacity is used greedily," the overfitting reflex from maximum likelihood) says it drifts up toward the truncation.

**Reconcile.** The posterior concentrates at $K=$ `4` (mode, probability `0.482`) with mean `4.76` — it uses the sticks it needs and leaves the rest empty, because the stick-breaking prior charges an Occam-style price (module 17) for every occupied component through the geometrically decaying weights. The extra sticks are not overfit; they sit unused with near-zero weight, available if the data demanded them. That is the whole pitch of nonparametric Bayes: **you do not choose $K$, you put a prior over it and read the posterior** — "the data chooses." It never drops below `4` (the four clumps are too separated to merge) but hedges *upward*, placing real probability on 5 and 6 — the honest admission that a couple of the clumps could each be split.

```python
# 19.5 -- figure: the data, and the posterior it induces over K
fig, ax = plt.subplots(1, 2, figsize=(11, 3.8))
ax[0].hist(y, bins=30, color="C0", alpha=0.7)
for loc in true_locs:
    ax[0].axvline(loc, color="k", ls="--", lw=1)
ax[0].set(title="Galaxy-like velocities (4 true clumps, dashed)",
          xlabel="velocity", ylabel="count")
ax[1].bar(vals, pmf, color="C1")
ax[1].axvline(m, color="k", ls="--", lw=1, label="truth")
ax[1].set(title="Posterior over #occupied clusters (L=15 sticks)",
          xlabel="K", ylabel="P(K | data)"); ax[1].legend()
save(fig, "dp_posterior_k")
```

![Left: a 1-D histogram with four separated humps, dashed lines at the true centers. Right: a bar chart of the posterior over K peaking sharply at 4 with smaller bars at 5 and 6 and essentially nothing near the truncation at 15.](figures/19-mixtures-dp/dp_posterior_k.png)

## Bridge — mixtures are the pattern behind half of modern ML

A mixture is "observed data + a discrete latent that indexes structure + parameters." Swap what the latent indexes and you get a zoo of famous models:

| Model | Latent $z$ | What marginalizing $z$ buys |
|---|---|---|
| Gaussian mixture / clustering (this module) | which component emitted $x_i$ | soft cluster membership, density estimate |
| **Hidden Markov model** | a *sequence* of states with Markov transitions | filtering/smoothing (module 21 is a continuous-state cousin) |
| **Topic models (LDA)** | which topic emitted each word | document–topic and topic–word distributions |
| **Mixture of experts / VAE** | a code $z$ (discrete or continuous) selecting a decoder path | amortized posterior $q(z\mid x)$, module 13's ELBO (module 25) |

The through-line is module 11's augmentation lesson stated at scale: **the discrete label is not a nuisance, it is the modeling device.** EM (module 13) point-estimates it, Gibbs (module 11) samples it, variational methods (module 13) approximate its posterior, and a DP lets its *range* be unknown. The HMM adds Markov dependence between labels; LDA adds a per-document prior over label proportions; the VAE makes the label continuous and amortizes its posterior with a neural network. Every one is the joint at the top of this module with one axis relabeled.

## Pitfalls

- **Reporting EM responsibilities as if they were posterior label probabilities.** They are plug-ins at $\hat\theta$; they omit "where is the boundary" (§19.1). Fine for a point prediction, misleading as a confidence.
- **Averaging per-component traces without fixing label switching.** A well-mixed mixture sampler visits all $K!$ labelings; $\overline{\mu_1}$ then estimates a nonexistent parameter (usually the data midpoint). Impose an ordering constraint or relabel post hoc (§19.2).
- **Trusting a single mixture chain that looks stable.** Stability can mean *stuck* — one mode of a malign multimodality, or one labeling of a benign one. Run multiple chains from dispersed starts; use tempering when barriers are real (§19.3).
- **Quoting $\mathbb E[K_n]\approx\alpha\log n$ at finite $n$.** That is a double limit; the exact mean is $\alpha[\psi(\alpha+n)-\psi(\alpha)]$, and the shorthand's error at finite $n$ has no fixed sign — it undercounts at small $\alpha$ and badly overcounts at larger $\alpha$ (§19.4).
- **Misreading the DP as "infinitely many clusters" — or as $\alpha$-free.** The prior is discrete and parsimonious (only $O(\alpha\log n)$ sticks occupied; the truncation $L$ is a computational cap, not a belief about $K$), and $\alpha$ is a real hyperparameter setting the granularity — the booklet puts a prior $\pi(\alpha)\propto(1+\alpha)^{-2}$ on it and samples it too (§19.5).

## Exercises

**Exercise 19.1 — Zero-inflated Poisson by augmentation.**
*Setup:* You count support tickets per customer. Many customers file zero tickets — some because they are genuinely low-volume Poisson users, others because they will *never* file (a structural zero: churned, or never onboarded). A plain Poisson cannot make both kinds of zero. The zero-inflated Poisson (ZIP) is a two-component mixture: with probability $\pi$ a customer is a structural zero ($y=0$ for sure), else $y\sim\mathrm{Poisson}(\lambda)$. We simulate $\pi=0.4$, $\lambda=3$.
*Predict:* Fit a *plain* Poisson (ignore the inflation) by matching its mean to the sample mean. Will its $\hat\lambda$ land above 3, at 3, or below 3? Commit before running.
*Reason:* the naive intuition is "the MLE of a Poisson mean is just the sample average, and averages are unbiased" — which forgets that the extra structural zeros drag the average below the true rate of the Poisson component.
*Run:* augment with a latent structural-zero indicator $s_i$ (this is module 11's data augmentation — invent the latent that restores conjugacy) and Gibbs-sample $(\pi,\lambda)$.
```python
# ZIP: mixture of a point mass at 0 (prob pi) and Poisson(lambda)
n_z = 1500
pi_t, lam_t = 0.4, 3.0
struct = rng.random(n_z) < pi_t
y_zip = np.where(struct, 0, rng.poisson(lam_t, n_z))
plain_lambda = y_zip.mean()                                  # plain-Poisson MLE = sample mean

s = np.zeros(n_z, dtype=bool)                                # latent: is this a structural zero?
pi_s, lam_s = 0.5, 1.0
draws = []
for _ in range(1500):
    is0 = y_zip == 0
    p_struct = pi_s / (pi_s + (1 - pi_s) * np.exp(-lam_s))   # P(structural | y=0)
    s = is0 & (rng.random(n_z) < p_struct)                   # y>0 can't be structural
    pi_s = rng.beta(1 + s.sum(), 1 + (~s).sum())             # Beta conjugate on the indicator
    pois = y_zip[~s]                                         # the genuine-Poisson customers
    lam_s = rng.gamma(1 + pois.sum(), 1 / (1 + len(pois)))   # Gamma conjugate on the rate
    draws.append((pi_s, lam_s))
draws = np.array(draws[500:])
print(f"plain-Poisson lambda_hat = {plain_lambda:.3f}  (biased low)")
print(f"ZIP posterior: pi = {draws[:,0].mean():.3f}, lambda = {draws[:,1].mean():.3f}"
      f"  (truth 0.4, 3.0)")
```
<details><summary>Reconcile</summary>

The plain Poisson returns $\hat\lambda=$ `1.769`, far below the true rate of 3, because 40% of the data are structural zeros that the single Poisson has to absorb by lowering its mean. The ZIP, by inventing the indicator $s_i$ and marginalizing it via Gibbs, recovers $\pi=$ `0.413` and $\lambda=$ `3.019`. The augmentation is module 11 exactly: conditional on $s$, $\pi$ has a Beta full conditional and $\lambda$ a Gamma one; the only subtlety is that a *positive* count is never a structural zero, so $s_i$ can be 1 only where $y_i=0$. The lesson: when zeros (or any observations) arrive from two mechanisms, model the mechanism as a latent — the "biased" plain estimate was never wrong, it was answering a mis-specified model's question.
</details>

**Exercise 19.2 — Does the concentration change how fast clusters appear?**
*Setup:* Two Chinese restaurants, $\alpha=1$ and $\alpha=3$, both filling to $n=200$ customers.
*Predict:* The ratio $\mathbb E[K_{200}^{(\alpha=3)}]/\mathbb E[K_{200}^{(\alpha=1)}]$ — is it about 3 (proportional to $\alpha$), less than 3, or more than 3?
*Reason:* the naive intuition is "new tables open at rate proportional to $\alpha$, so triple $\alpha$ should triple the tables."
*Run:*
```python
nn = np.arange(1, 201)
EK = lambda a: a * (digamma(a + 200) - digamma(a))
print(f"E[K] at alpha=1: {EK(1):.2f}, alpha=3: {EK(3):.2f}, ratio {EK(3)/EK(1):.2f}")
```
<details><summary>Reconcile</summary>

The ratio is `2.24`, not 3. Tripling $\alpha$ less-than-triples the clusters, because the *new-table* probability $\alpha/(\alpha+i-1)$ is not linear in $\alpha$ — at larger $\alpha$ each new table also enlarges the denominator, so the marginal return on concentration diminishes. Concretely $\mathbb E[K_{200}]$ moves from `5.88` to `13.16`. The digamma is not decoration: the "proportional to $\alpha$" reflex overpredicts, and the gap grows with $\alpha$. This is the same reason $\alpha\log n$ misleads — the cluster count is a saturating, not linear, function of its inputs.
</details>

**Exercise 19.3 — Why the swap move rescues the cold chain (ML/DL connection).**
*Setup:* Parallel tempering (§19.3) is the statistical twin of techniques you may have met as *replica exchange* in molecular dynamics and as the intuition behind *temperature* in annealed sampling for energy-based models. Re-run the ladder but vary the top temperature.
*Predict:* Shrink the ladder to $[1.0, 1.3]$ (a timid top temperature). Will the cold chain still cross to the right well as reliably as the $[1,2,4,8]$ ladder did?
*Reason:* the naive intuition is "any ladder with a swap move mixes — the swap is what matters, not how hot the top gets."
*Run:*
```python
timid, sr_t = run_pt([1.0, 1.3], rng)
wide, sr_w = run_pt([1.0, 2.0, 4.0, 8.0], rng)
print(f"timid ladder [1,1.3]:   P(x>0)={ (timid>0).mean():.3f}  swap accept {sr_t:.2f}")
print(f"wide ladder [1,2,4,8]:  P(x>0)={ (wide>0).mean():.3f}  swap accept {sr_w:.2f}")
```
<details><summary>Reconcile</summary>

The timid ladder gives $P(x>0)=$ `0.013` — still trapped — even though its swap-acceptance is *higher* (`0.92`) than the wide ladder's `0.79`. High swap acceptance is worthless if the hottest rung is still too cold to cross the barrier itself: swapping only ferries a mode that *some* rung has already found, and $\beta=1/1.3$ flattens the two-well target far too little to let its chain leap the gap of 10. The wide ladder's hot rung ($\beta=1/8$) sees an almost flat landscape, crosses freely, and hands the discovery down. The design lesson mirrors learning-rate schedules: the top temperature must be hot enough to *escape*, and the rungs spaced so neighbors overlap enough to *swap* — both, not either.
</details>

**Exercise 19.4 — What EM hides at the boundary.**
*Setup:* Take the §19.1 fit. EM gave every point a single responsibility; Gibbs gave a posterior label probability.
*Predict:* Among the points EM is *very* sure about (responsibility for its top cluster $>0.95$), what fraction does Gibbs *also* place above 0.95 for the same cluster — nearly all (say $>0.95$), or noticeably fewer?
*Reason:* the naive intuition is "if the best-fit model is confident, the full posterior should be too — confidence is a property of the data, not the method."
*Run:*
```python
top_em = np.maximum(resp_lo_em, 1 - resp_lo_em)             # EM's confidence in its top label
top_gb = np.maximum(prob_lo_gibbs, 1 - prob_lo_gibbs)
sure = top_em > 0.95
agree = (top_gb[sure] > 0.95).mean()
print(f"EM 'very sure' points: {sure.sum()}/{n}; Gibbs also >0.95 on {agree:.2f} of them")
```
<details><summary>Reconcile</summary>

EM is very sure about `205` of the 250 points, but Gibbs stays above 0.95 on only `0.97` of those — a few percent of EM's "certain" points get downgraded once parameter uncertainty is folded in. Confidence is *not* purely a property of the data: it depends on whether you condition on one $\hat\theta$ (EM) or integrate over $p(\theta\mid\text{data})$ (Gibbs). The gap is modest here because the clusters are fairly separated; with heavier overlap or fewer points it widens, and EM's crispness becomes actively misleading. This is module 05's plug-in-vs-predictive gap, localized to the labels.
</details>

## Takeaways

- **A mixture is a joint over `(data, hidden label, parameters)`.** Clustering is conditioning on the labels; density estimation is marginalizing them; the number of clusters is one more unknown you can put a prior on.
- **EM gives point labels, Gibbs gives label distributions.** EM's responsibilities are plug-ins at $\hat\theta$; Gibbs also averages over where the boundary is, so it flags more genuinely-uncertain points (`38` vs `24` here). At the boundary, EM's crispness is partly an artifact.
- **The mixture likelihood is permutation-symmetric, so the posterior has $K!$ identical modes.** A correct sampler visits them all (label switching), which makes per-component summaries meaningless; fix it with an ordering constraint or post-hoc relabeling, never by hoping the chain stays stuck.
- **Parallel tempering crosses real barriers.** A ladder of flattened replicas plus swap moves lets a cold chain trade places with a hot one that already found the far mode — the fix module 10 promised. The top rung must be hot enough to escape, not just present.
- **CRP cluster counts grow like $\log n$, exactly $\mathbb E[K_n]=\alpha[\psi(\alpha+n)-\psi(\alpha)]$.** The "$\alpha\log n$" shorthand errs at finite $n$ in an $\alpha$-dependent direction (under at $\alpha=1$, badly over at $\alpha=5$). $K_n$ is a sum of independent Bernoullis; the CRP is exchangeable (module 01's Pólya urn).
- **A Dirichlet-process mixture lets the data choose $K$.** Stick-breaking weights decay geometrically, so only $O(\alpha\log n)$ components are occupied; truncate at $L$ sticks for computation and read the posterior over occupied clusters — here it peaks at the true `4` despite $L=15$.
- **Mixtures are the skeleton of HMMs, topic models, and VAEs.** Relabel the latent — sequence of Markov states, per-word topic, continuous code — and the same joint reappears. The discrete label is the modeling device, not a nuisance.

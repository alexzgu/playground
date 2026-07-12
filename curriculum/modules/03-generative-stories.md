# 03. Distributions Are Generative Stories

> **Spine.** A distribution is a compiled generative story; you pick a family by matching its mechanism, and you price a wrong match in bits (KL).
> **Which line?** Line 1 — *a model is a joint distribution* — every factor of that joint is a distribution you choose. This module is how to choose, and how to measure a bad choice. (One line-3 cameo: prediction is marginalization, when we collapse the process onto a sub-window.)
> **Promise.** After this module you can pick a distribution from its generating mechanism instead of its silhouette, predict when the CLT will rescue an average and when it will detonate, and quantify the cost of the wrong family in bits.
> **Prereqs.** Modules 00 (four lines, notation, rate/variance conventions), 02 (conditioning). **Runtime.** ~21 s.
> **Sources.** C-B ch. 3 (families), Thm 3.8.1 (Poisson process), Ex 2.2.4 & 5.2.10 (Cauchy), §3.4 (exponential families — deferred to M04); booklet ch. 3 §3.1 (Monte Carlo).

Conventions used throughout (module 00 states them once; restated here because modules are standalone): `Exp(λ)` has **rate** λ (mean 1/λ), scipy `expon(scale=1/λ)`; `Gamma(k, λ)` has shape k and **rate** λ, scipy `gamma(a=k, scale=1/λ)`; `N(μ, σ²)`'s second argument is the **variance**; `KL(p ‖ q) = E_p[log p − log q]`.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "03-generative-stories"          # this module's figure dir
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

## 03.1 A distribution is a compiled generative story

Photons from a faint star hit a detector; requests hit a web server; mutations land along a chromosome. You do not control *when* any single event happens — only the average **rate** λ. Write down the mechanism and the distribution falls out; you never have to remember which named family goes with which picture.

Here is the whole mechanism for events arriving in time, in two moves. Fix a horizon T and a rate λ. **How many** events occur in [0, T]? A count, `N ~ Poisson(λT)`. **Where** does each land? Independently, uniformly on [0, T]; sort them into arrival times 0 < S₁ < S₂ < ⋯ < S_N < T. That is it — "Poisson count, then uniform order statistics" is a complete recipe for a homogeneous Poisson process. (C-B Thm 3.8.1 characterizes the *same* object by its postulates: independent increments, rate proportional to interval length, no simultaneous arrivals. The order-statistics recipe is that theorem run as a simulator.)

**Predict before reading on.** You placed the points as structurelessly as possible — uniform, given the count. Commit: what is the distribution of the *gaps* between consecutive arrivals? Most people reason "flat placement, flat gaps" and say roughly uniform.

Flat placement does not give flat gaps. Three quantities you might measure each turn out to have a named law, none of which you put in by hand:

- **Gaps.** The inter-arrival times S_{i+1} − S_i are iid `Exp(λ)`. *(Theorem; C-B §3.3 / Thm 3.8.1 — the interval to the next arrival is memoryless.)*
- **Waits.** The k-th arrival time S_k = (sum of k gaps) is `Gamma(k, λ)`. *(Theorem — a sum of k iid Exp(λ) is Gamma(k, λ).)*
- **Counts.** The number of arrivals in any sub-window [0, s] is `Poisson(λs)`.

That last one is line 3 of the course spine wearing work clothes. The sub-window count is a *marginal* of the full process: `p(N_{[0,s]} = m) = Σ_N p(N_{[0,s]} = m | N) p(N)` — *prediction is marginalization* — and the Poisson-count-times-uniform-placement algebra collapses the sum to `Poisson(λs)`. We verify all three faces against scipy with a Kolmogorov–Smirnov statistic (0 = perfect match):

```python
# 03.1 -- one process, three faces. Build via Poisson count + uniform order statistics.
lam, T = 2.0, 30.0                 # rate (events / unit time), horizon; E[N] = lam*T = 60
R = 20000                          # independent replicate processes
counts = rng.poisson(lam * T, size=R)

gaps = []                          # inter-arrival gaps S_{i+1}-S_i     -> should be Exp(lam)
waits = {1: [], 2: [], 3: [], 5: []}   # k-th arrival time S_k          -> should be Gamma(k, lam)
sub_s = 5.0                        # a sub-window [0, sub_s]
subcount = np.empty(R, dtype=int)  # count in the sub-window            -> should be Poisson(lam*s)

for r, N in enumerate(counts):
    if N == 0:
        subcount[r] = 0
        continue
    S = np.sort(rng.uniform(0.0, T, size=N))       # given N: N iid Uniform(0,T), ordered
    subcount[r] = int(np.count_nonzero(S <= sub_s))
    if N >= 2:
        gaps.append(np.diff(S))                     # internal gaps only (both ends are events)
    for k in waits:
        if N >= k:
            waits[k].append(S[k - 1])
gaps = np.concatenate(gaps)

# scipy convention traps: Exp(rate lam) -> expon(scale=1/lam); Gamma(shape k, rate lam) -> gamma(a=k, scale=1/lam)
ks_gap = stats.kstest(gaps, stats.expon(scale=1 / lam).cdf).statistic
print(f"gaps ~ Exp(lam):        KS = {ks_gap:.4f}   ({gaps.size} gaps pooled)")
for k in waits:
    Sk = np.asarray(waits[k])
    ks_k = stats.kstest(Sk, stats.gamma(a=k, scale=1 / lam).cdf).statistic
    print(f"S_{k} ~ Gamma({k}, lam):   KS = {ks_k:.4f}   mean {Sk.mean():.3f} vs {k / lam:.3f}")
print(f"count[0,{sub_s:.0f}] ~ Poisson({lam * sub_s:.0f}): mean {subcount.mean():.3f}, var {subcount.var():.3f}")
```

The gaps match `Exp(λ)` to `0.0062` (KS), and the k-th waits match `Gamma(k, λ)` with sample means landing on k/λ: `0.501`, `1.003`, `1.499`, `2.506` against 0.5, 1.0, 1.5, 2.5. The sub-window count has mean `9.986` and variance `10.087` — the Poisson signature *mean ≈ variance ≈ λs = 10*. If you predicted uniform-ish gaps, here is why that missed: "no pattern" applies to *where each point lands*, not to *distances between neighbors* — a uniform scatter clumps, so tiny gaps are the most common gap of all and the gap density piles up at 0 and decays exponentially (upper-right panel below). You placed points as structurelessly as possible, and exponential, gamma, and Poisson laws crystallized out. Match the mechanism and the family is not a choice; it is a consequence.

```python
# figure: the construction and its three faces
fig, ax = plt.subplots(2, 2, figsize=(11, 7))

S_demo = np.sort(rng.uniform(0, T, rng.poisson(lam * T)))     # one small realization to look at
ax[0, 0].eventplot(S_demo, lineoffsets=0.5, linelengths=0.6, color="C0")
ax[0, 0].step(np.r_[0, S_demo, T], np.r_[0, np.arange(1, S_demo.size + 1), S_demo.size],
              where="post", color="C3", lw=1.5, label="cumulative count")
ax[0, 0].set(title="One realization: N~Poisson(λT) points, placed uniformly",
             xlabel="time", ylabel="count", xlim=(0, T)); ax[0, 0].legend(loc="upper left")

xg = np.linspace(0, 4, 200)
ax[0, 1].hist(gaps, bins=60, density=True, color="C0", alpha=0.5)
ax[0, 1].plot(xg, stats.expon(scale=1 / lam).pdf(xg), "k--", lw=2, label="Exp(λ) pdf")
ax[0, 1].set(title="Gaps are Exponential(λ)", xlabel="gap S$_{i+1}$−S$_i$", ylabel="density",
             xlim=(0, 4)); ax[0, 1].legend()

xw = np.linspace(0, 6, 200)
for k in waits:
    ax[1, 0].hist(np.asarray(waits[k]), bins=60, density=True, alpha=0.35)
    ax[1, 0].plot(xw, stats.gamma(a=k, scale=1 / lam).pdf(xw), lw=2, label=f"Gamma({k}, λ)")
ax[1, 0].set(title="k-th waits are Gamma(k, λ)", xlabel="arrival time S$_k$", ylabel="density",
             xlim=(0, 6)); ax[1, 0].legend(fontsize=9)

mvals = np.arange(0, subcount.max() + 1)
ax[1, 1].hist(subcount, bins=np.arange(-0.5, subcount.max() + 1.5), density=True,
              color="C0", alpha=0.5)
ax[1, 1].plot(mvals, stats.poisson(lam * sub_s).pmf(mvals), "ko", ms=5, label="Poisson(λs) pmf")
ax[1, 1].set(title="Sub-window counts are Poisson(λs)", xlabel="count in [0, 5]", ylabel="prob")
ax[1, 1].legend()
fig.tight_layout()
save(fig, "poisson_process")
```

![A Poisson process built from a Poisson count plus uniform order statistics, and its three emergent faces: Exponential gaps, Gamma waits, Poisson sub-window counts, each overlaid on its scipy density.](figures/03-generative-stories/poisson_process.png)

## 03.2 The averaging story: when it works, and when it detonates

Why is the Normal everywhere? Not because nature prefers bell curves, but because of a *story*. Add up many independent contributions, none dominating, each with finite variance, and the standardized sum converges to `N(0, 1)` no matter what the pieces looked like — the Central Limit Theorem (C-B §5.5). The Normal is the "sum of many small finite-variance shocks" distribution, and the Law of Large Numbers is its running-average shadow: the sample mean of iid finite-variance draws converges to the population mean. The left panel below shows it for `Exp(1)` draws (mean 1): six running means, all reeling in to 1.

That story has a precondition — *finite variance* — and it is worth being caught assuming it. Here is the trap, staged predict-first.

**Setup.** A `Cauchy(0, 1)` variable is what you get from the tangent of a uniform angle, or from the ratio of two independent `N(0, 1)`s (C-B Ex 4.3.6). Its density `1/(π(1+x²))` is symmetric, bell-ish, centered at 0 — it looks like a slightly heavy Normal. You draw Cauchy(0,1) values one at a time and track the running mean X̄ₙ.

**Predict.** As n climbs to 2×10⁵, where does X̄ₙ go — and does the *spread* of X̄ₙ across replicates shrink like 1/√n? Commit to a number and a direction.

**Reason (name the intuition).** The Law of Large Numbers: a sample mean converges to the population mean, tightening like 1/√n; the density is symmetric about 0, so X̄ₙ → 0 with vanishing spread.

**Run.**

```python
# 03.2 -- averaging: Exp(1) (finite variance) vs Cauchy(0,1) (no mean)
def running_mean(x):
    return np.cumsum(x) / np.arange(1, x.size + 1)

def iqr(a):
    q1, q3 = np.percentile(a, [25, 75])
    return q3 - q1

n_show, reps_show = 200_000, 6
finite = np.array([running_mean(rng.exponential(1.0, n_show)) for _ in range(reps_show)])
cauchy = np.array([running_mean(rng.standard_cauchy(n_show)) for _ in range(reps_show)])

# The distribution of X-bar_n itself, summarized by its IQR (a scale that survives heavy tails):
for n in (10, 1000, 100_000):
    Rr = 3000 if n <= 1000 else 800
    xbar = np.array([rng.standard_cauchy(n).mean() for _ in range(Rr)])
    print(f"Cauchy sample mean: n={n:>6}  IQR(X-bar) = {iqr(xbar):.3f}   (theory: 2.000 at every n)")
```

The running means never settle — they drift, then a single outsized draw yanks the whole running average sideways, and it never recovers. And the spread does not shrink: the IQR of the sample-mean distribution is `2.026` at n=10, `2.017` at n=1000, `1.931` at n=10⁵ — fluctuating around 2 at every n. Contrast the LLN, where that spread would fall like 1/√n toward 0.

**Reconcile.** The LLN's hypothesis is that a mean *exists*. The Cauchy's does not: `∫ x/(π(1+x²)) dx` diverges (C-B Ex 2.2.4), so there is no number for X̄ₙ to converge to. Worse:

> **Theorem (C-B Ex 5.2.10).** If X₁, …, Xₙ are iid `Cauchy(0, 1)`, then X̄ₙ is *itself* `Cauchy(0, 1)`. Averaging a million draws returns you exactly one Cauchy draw.

Two lines of proof: the Cauchy characteristic function is φ(t) = e^{−|t|}, so φ_{X̄}(t) = φ(t/n)ⁿ = e^{−n·|t/n|} = e^{−|t|} — unchanged by n. The empirical IQR ≈ 2 at every n *is* this theorem, because the `Cauchy(0,1)` IQR is exactly 2 (its CDF is ½ + arctan(x)/π, so the quartiles sit at ±1). More data does not concentrate an estimator that has no target.

The Cauchy is not a lone monster; it is one end of a gradient. For the Student-t with ν degrees of freedom the variance is ν/(ν−2), finite only when ν > 2 (C-B; t₁ *is* the Cauchy), so the CLT holds for ν > 2 and fails at ν ≤ 2. When variance is infinite the sum story does not vanish — it converges to a *stable law* (the generalized CLT), of which both the Normal and the Cauchy are members. (And a different question — the limit of the *maximum* rather than the sum — has its own family, the extreme-value / GEV distributions; one sentence is all it gets here.)

```python
# figure: averaging tames finite variance but not the Cauchy; the tail gallery behind it
fig, ax = plt.subplots(1, 3, figsize=(13, 4))
nn = np.arange(1, n_show + 1)
for i in range(reps_show):
    ax[0].plot(nn, finite[i], lw=0.8)
ax[0].axhline(1.0, color="k", ls="--", lw=1.5, label="E[X]=1")
ax[0].set(title="Exp(1): running means converge (finite var)", xlabel="n", ylabel="running mean",
          xscale="log", ylim=(0.5, 1.6)); ax[0].legend()
for i in range(reps_show):
    ax[1].plot(nn, cauchy[i], lw=0.8)
ax[1].axhline(0.0, color="k", ls="--", lw=1.5)
ax[1].set(title="Cauchy(0,1): running means never settle", xlabel="n", ylabel="running mean",
          xscale="log", ylim=(-15, 15))
xx = np.linspace(-6, 6, 400)
ax[2].plot(xx, stats.norm.pdf(xx), label="Normal(0,1)")
ax[2].plot(xx, stats.t(df=3).pdf(xx), label="t₃ (var=3)")
ax[2].plot(xx, 1 / (np.pi * (1 + xx**2)), "k-", label="Cauchy (no mean)")
ax[2].set(title="Heavy-tail gallery (log scale)", xlabel="x", ylabel="density",
          yscale="log", ylim=(1e-3, 1)); ax[2].legend(fontsize=9)
fig.tight_layout()
save(fig, "clt_cauchy")
```

![Left: running means of Exp(1) draws converging to 1. Center: running means of Cauchy draws wandering without limit. Right: log-scale densities of Normal, t3, and Cauchy showing the tail thickness that decides whether averaging works.](figures/03-generative-stories/clt_cauchy.png)

## 03.3 Measuring story mismatch in bits

To choose *between* stories you need a ruler for how wrong a story is. The ruler is bits, and it is the same object that will reappear as a training loss (M15), a variational objective (M13), and a model score (M17). Define it once, carefully. (Base-2 logs give **bits**; natural logs give **nats**; always state the base.)

- **Surprise** of a single outcome under model q is `−log q(x)`: rare outcomes are surprising, certain ones cost nothing.
- **Entropy** `H(p) = E_{X~p}[−log p(X)] = −Σ p log p` is your *expected* surprise when the world runs on p and you know it — the irreducible uncertainty.
- **Cross-entropy** `H(p, q) = E_{X~p}[−log q(X)]` is your expected surprise when the world runs on p but you *model* it as q.
- **KL divergence** `KL(p ‖ q) = H(p, q) − H(p) = E_{X~p}[log p(X)/q(X)]` is the *excess* surprise — the bits you waste by believing q instead of the true p.

Worked in coins:

```python
# 03.3 -- entropy, cross-entropy, KL in bits (log base 2)
def entropy_bits(p):
    p = np.asarray(p, float); p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))

def cross_entropy_bits(p, q):
    p, q = np.asarray(p, float), np.asarray(q, float)
    return float(-np.sum(p * np.log2(q)))

def kl_bits(p, q):
    p, q = np.asarray(p, float), np.asarray(q, float); m = p > 0
    return float(np.sum(p[m] * np.log2(p[m] / q[m])))

biased, fairmodel = [0.9, 0.1], [0.5, 0.5]
print(f"H(fair coin)         = {entropy_bits([0.5, 0.5]):.3f} bits   (max for 2 outcomes)")
print(f"H(biased 0.9 coin)   = {entropy_bits(biased):.3f} bits   (rarely surprised)")
print(f"H(p=biased, q=fair)  = {cross_entropy_bits(biased, fairmodel):.3f} bits   (cross-entropy)")
print(f"KL(biased || fair)   = {kl_bits(biased, fairmodel):.3f} bits")
print(f"KL(fair || biased)   = {kl_bits(fairmodel, biased):.3f} bits   (asymmetry: KL is not a distance)")
print(f"check  H + KL = Xent : {entropy_bits(biased) + kl_bits(biased, fairmodel):.3f} bits")
```

A fair coin carries `1.000` bit; a 0.9-biased coin only `0.469` bits, because you can usually guess it. If the world is the 0.9 coin but you insist it is fair, your expected surprise is the cross-entropy `1.000` bit, of which `0.531` bits is pure waste — that is `KL(biased ‖ fair)`, and `0.469 + 0.531 = 1.000` confirms `cross-entropy = entropy + KL`.

> **Theorem (KL ≥ 0; Gibbs' inequality).** `KL(p ‖ q) = E_p[−log(q/p)] ≥ −log E_p[q/p] = −log Σ_x p(x)·q(x)/p(x) = −log Σ_x q(x) = −log 1 = 0`, using Jensen's inequality on the convex function −log; equality iff q = p. So cross-entropy is never below entropy — you can never be *less* surprised by modeling the wrong distribution.

KL is not symmetric: `KL(fair ‖ biased) = 0.737` bits ≠ `0.531`. The direction you minimize is a modeling decision with consequences (mode-covering vs. mode-seeking; M13). Three forward threads make this the course's information backbone:

- Training a classifier by **cross-entropy loss** minimizes `H(p_data, q_θ)` over θ — which is `KL(p_data ‖ q_θ)` up to the constant `H(p_data)` — so cross-entropy training *is* maximum likelihood (M15).
- **Variational inference** maximizes the ELBO = log-evidence − `KL(q ‖ posterior)`; the same divergence, now steering an approximation onto the posterior (M13).
- **Held-out scoring** (WAIC, M17) is expected log predictive density — negative cross-entropy on future data — the honest, out-of-sample version of a likelihood.

```python
# figure: entropy of a coin, and cross-entropy = entropy + KL
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
pp = np.linspace(1e-4, 1 - 1e-4, 400)
Hp = -(pp * np.log2(pp) + (1 - pp) * np.log2(1 - pp))
ax[0].plot(pp, Hp, color="C0")
ax[0].plot([0.5, 0.9], [1.0, entropy_bits(biased)], "ko")
ax[0].annotate("fair: 1.000", (0.5, 1.0), textcoords="offset points", xytext=(0, -16), ha="center")
ax[0].annotate("0.9 coin: 0.469", (0.9, entropy_bits(biased)), textcoords="offset points",
               xytext=(-8, 8), ha="right")
ax[0].set(title="Entropy of a Bernoulli(p) coin", xlabel="p = P(heads)", ylabel="H(p) [bits]")

qq = np.linspace(0.02, 0.98, 400)
Xe = -(0.9 * np.log2(qq) + 0.1 * np.log2(1 - qq))       # H(biased, q=[q,1-q]) vs q
ax[1].plot(qq, Xe, color="C3", label="cross-entropy H(p, q)")
ax[1].axhline(entropy_bits(biased), color="k", ls="--", label="entropy H(p) = 0.469")
ax[1].axvline(0.9, color="C0", ls=":", label="q = p (truth)")
ax[1].annotate("", xy=(0.5, 1.0), xytext=(0.5, entropy_bits(biased)),
               arrowprops=dict(arrowstyle="<->"))
ax[1].text(0.52, 0.72, "KL = 0.531", fontsize=9)
ax[1].set(title="Cross-entropy is minimized at the truth", xlabel="model q = P(heads)",
          ylabel="bits", ylim=(0, 2.2)); ax[1].legend(fontsize=8)
fig.tight_layout()
save(fig, "information")
```

![Left: the concave Bernoulli entropy curve peaking at 1 bit for a fair coin, with the fair and 0.9-biased coins marked. Right: cross-entropy H(p,q) as the model q varies, bottoming out at the entropy H(p) exactly when q equals the true p; the gap above that floor is the KL divergence.](figures/03-generative-stories/information.png)

## 03.4 The least-committal story: maximum entropy

Sometimes you know a *constraint* — a support, a mean, maybe a variance — and nothing else, yet you must still name a distribution. Which one smuggles in the fewest unstated assumptions? The one with the **most entropy** consistent with what you know. Maximum entropy is the least-committal story: it spreads probability as evenly as the constraints permit and adds no structure you cannot defend.

The derivation has exactly two real steps (calculus of variations; details are arithmetic). Maximize `H(p) = −∫ p log p` subject to normalization `∫ p = 1` and moment constraints `∫ p(x) T_k(x) dx = μ_k`. **Step 1:** form the Lagrangian and take its functional derivative in p(x), which gives `−log p(x) − 1 − λ₀ + Σ_k λ_k T_k(x) = 0` (sign choice on the λ_k is a convention; each multiplier absorbs its constraint's sign). **Step 2:** solve for p:

$$p(x) \;\propto\; \exp\!\Big(\textstyle\sum_k \lambda_k\, T_k(x)\Big).$$

The max-entropy distribution is always an *exponential of a linear combination of the constrained statistics*; the multipliers λ_k are pinned down by the constraints. Two specializations:

- **Support [0, ∞), fixed mean μ.** The only statistic is T = x, so `p(x) ∝ e^{λx}`, normalizable on [0, ∞) only for λ < 0; normalizing gives the `Exp(1/μ)` density. *The least-committal story for a positive quantity with a known average is the Exponential.*
- **Support ℝ, fixed mean and variance.** Statistics x and x² give `p(x) ∝ exp(λ₁x + λ₂x²)` — a quadratic in the exponent, i.e. a Gaussian — and matching the two moments yields `N(μ, σ²)`. *The least-committal story for a real quantity with a known center and spread is the Normal.* (So the Normal earns its ubiquity twice: once as the CLT limit, once as max-entropy under mean and variance.)

To check this numerically without hand-assuming the answer's parameters, grid the support and solve the (convex) dual for the multipliers, then compare to the textbook family. The honest test: discretize a target, read off *only* the moment(s) it is supposed to be pinned by, hand max-entropy those, and see whether it reconstructs the whole density.

```python
# 03.4 -- max-entropy on a grid via the convex dual of the variational problem
from scipy import optimize
from scipy.special import logsumexp

def maxent_on_grid(x, features, targets):
    """Max-entropy p on grid x with E[feature_j] = target_j.
    Derivation gives p_i ∝ exp(theta·T_i); solve the convex dual for theta."""
    Tm = np.vstack(features)                     # (m constraints, n grid points)
    b = np.asarray(targets, float)
    def p_of(theta):
        z = theta @ Tm
        return np.exp(z - logsumexp(z))          # normalized, numerically stable
    def dual(theta):                             # convex; its minimizer matches the moments
        return logsumexp(theta @ Tm) - theta @ b
    def dual_grad(theta):
        return Tm @ p_of(theta) - b
    sol = optimize.minimize(dual, np.zeros(len(features)), jac=dual_grad,
                            method="BFGS", options={"gtol": 1e-12})
    return p_of(sol.x)

def kl_nats(p, q):
    p, q = np.clip(p, 1e-300, None), np.clip(q, 1e-300, None)
    return float(np.sum(p * np.log(p / q)))

xg = np.linspace(0, 20, 81)                                     # support >= 0
exp_target = stats.expon(scale=2.0).pdf(xg); exp_target /= exp_target.sum()   # Exp(rate 1/2)
p_exp = maxent_on_grid(xg, [xg], [exp_target @ xg])            # constrain ONLY the mean
print(f"max-ent[support>=0, mean fixed]   vs Exponential: KL = {kl_nats(p_exp, exp_target):.1e} nats")

xn = np.linspace(-8, 8, 121)                                   # support R
norm_target = stats.norm(0, 1).pdf(xn); norm_target /= norm_target.sum()
p_norm = maxent_on_grid(xn, [xn, xn**2], [norm_target @ xn, norm_target @ xn**2])  # mean & variance
print(f"max-ent[support R, mean+var fixed] vs Normal:     KL = {kl_nats(p_norm, norm_target):.1e} nats")
```

Given only a mean, max-entropy rebuilds the entire Exponential to `1.3e-16` nats of KL; given a mean and a variance, it rebuilds the entire Normal to `1.5e-16` nats. Max-entropy does not *approximate* these families — under the matching constraints it *is* them. Which constraints, though, is everything: hand max-entropy a nonnegative-*integer* support and only a mean, and you do **not** get the Poisson (Exercise 03.3). The Poisson came from the process story of §03.1, not from a mean constraint — two different roads build two different families for "counts at rate 3."

```python
# figure: max-entropy points reconstruct the target densities
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(xg, exp_target, "k--", lw=2, label="Exp(λ), discretized")
ax[0].plot(xg, p_exp, "C0o", ms=3, label="max-ent (mean only)")
ax[0].set(title="Support ≥ 0, fixed mean → Exponential", xlabel="x", ylabel="grid prob"); ax[0].legend()
ax[1].plot(xn, norm_target, "k--", lw=2, label="Normal(0,1), discretized")
ax[1].plot(xn, p_norm, "C0o", ms=3, label="max-ent (mean+var)")
ax[1].set(title="Support ℝ, fixed mean+var → Normal", xlabel="x", ylabel="grid prob"); ax[1].legend()
fig.tight_layout()
save(fig, "maxent")
```

![Grid max-entropy solutions (dots) landing exactly on the discretized Exponential (left, mean constraint) and Normal (right, mean and variance constraints), confirming that maximum entropy under those moments reconstructs the whole family.](figures/03-generative-stories/maxent.png)

## Bridge — softmax is max-entropy, and where these families are cataloged

**ML bridge (softmax and temperature).** A network's final layer turns K scores (logits) `s₁, …, s_K` into a distribution over classes. Which distribution? Max-entropy again. Constrain a categorical so that the expected score matches the logits; the max-entropy solution from §03.4 is `p_k ∝ exp(λ s_k)` — softmax. The **temperature** T in `p_k ∝ exp(s_k / T)` is the reciprocal of the Lagrange multiplier: how tightly the score constraint binds. T → 0 pins all mass on the top score (argmax, zero entropy); T → ∞ ignores the constraint (uniform, maximum entropy log₂K). Sliding T slides along the max-entropy family from "certain" to "clueless."

```python
# 03.5 -- softmax IS max-entropy over classes; temperature = Lagrange multiplier
logits = np.array([2.0, 1.0, 0.5, -0.5, -1.0])
def softmax(s, temp):
    z = s / temp; z -= z.max()
    e = np.exp(z); return e / e.sum()
for tmp in (0.5, 1.0, 2.0):
    p = softmax(logits, tmp)
    print(f"softmax @ T={tmp:<3}: entropy {entropy_bits(p):.3f} bits, top prob {p.max():.3f}")
print(f"uniform (T->inf):  entropy {np.log2(logits.size):.3f} bits")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
width, xk = 0.25, np.arange(logits.size)
for j, tmp in enumerate((0.5, 1.0, 2.0)):
    ax[0].bar(xk + (j - 1) * width, softmax(logits, tmp), width, label=f"T={tmp}")
ax[0].axhline(1 / logits.size, color="k", ls="--", lw=1, label="uniform")
ax[0].set(title="Softmax sharpens as T→0, flattens as T→∞", xlabel="class", ylabel="prob")
ax[0].legend(fontsize=8)
Ts = np.linspace(0.1, 20, 200)
ax[1].plot(Ts, [entropy_bits(softmax(logits, t)) for t in Ts], color="C3")
ax[1].axhline(np.log2(logits.size), color="k", ls="--", label="log₂K (uniform)")
ax[1].set(title="Entropy climbs with temperature", xlabel="temperature T", ylabel="entropy [bits]")
ax[1].legend(fontsize=9)
fig.tight_layout()
save(fig, "softmax_temperature")
```

Entropy climbs `0.822 → 1.670 → 2.125` bits as T goes 0.5 → 1 → 2, heading for the uniform ceiling `2.322` bits = log₂5. This is the identical knob behind LLM sampling temperature (M25) and tempered posteriors (M18): temperature is a max-entropy dial.

![Left: softmax class probabilities for fixed logits at temperatures 0.5, 1, 2, sharpening toward argmax as T falls and flattening toward uniform as T rises. Right: softmax entropy increasing monotonically with temperature toward the uniform ceiling log2 K.](figures/03-generative-stories/softmax_temperature.png)

**Catalog bridge (C-B, booklet).** C-B ch. 3 presents these families as a catalog of formulas; we have instead *derived the catalog* from mechanisms (§03.1) and constraints (§03.4), which is why you can reconstruct any entry without memorizing it. And every "verify" above was a Monte Carlo integral — a sample average standing in for an expectation (booklet ch. 3 §3.1) — carrying a √M error bar we leave implicit here and make rigorous in module 09.

One last pattern, deliberately left for next module. The Exponential, Normal, Poisson, Bernoulli, and the softmax/categorical each wrote themselves as `exp(a linear function of some summary of x)`. That shared algebraic skeleton is the **exponential family**, and it is the engine of module 04.

## Pitfalls

- **Shape-matching instead of mechanism-matching.** A histogram that "looks bell-shaped" is not a license to use a Normal for a bounded proportion or a small count. Ask what *generated* the data, then read off the family.
- **Assuming the LLN/CLT always rescues an average.** Infinite variance (heavy tails) or strong dependence breaks both. A running mean that refuses to stabilize as data pours in is a *tail* problem, not a sample-size problem — reach for medians and quantiles (Exercise 03.2). "n is large" is not the hypothesis; "variance is finite" is.
- **Reading KL as a distance.** It is asymmetric (`0.531` vs `0.737` above) and diverges when q puts near-zero mass where p does not. Which direction you minimize decides mode-covering vs. mode-seeking behavior (M13).
- **Forgetting max-entropy is least-committal *given your constraints*.** It launders your assumptions into a distribution; wrong constraints yield a confidently wrong model. The judgment lives in *what* you constrain, not in the entropy step.
- **Mixing bits and nats.** A cross-entropy loss in code is in nats (natural log); a fair coin is ln 2 ≈ 0.693 nats = 1 bit. State the base or your numbers drift by a factor of ln 2.

## Exercises

**Exercise 03.1 — Superposition and thinning.**
*Setup:* Server A is hit at rate λ_A = 3/s and server B at λ_B = 5/s, independently, both Poisson, over a 100 s window. You merge the two access logs into one stream; separately, you subsample A by keeping each event with probability 0.2.
*Predict:* Give the rate **and family** of (i) the merged stream and (ii) the thinned A-stream. Does the Poisson family survive each operation?
*Reason:* The intuition "rates add / rates scale" is about means — but a mean is not a family.
*Run:*
```python
lamA, lamB, Twin, reps = 3.0, 5.0, 100.0, 20000
A = rng.poisson(lamA * Twin, reps)
B = rng.poisson(lamB * Twin, reps)
merged, thinnedA = A + B, rng.binomial(A, 0.2)
print(f"merged:   rate {merged.mean()/Twin:.3f}, var/mean {merged.var()/merged.mean():.3f} (Poisson=1)")
print(f"thinned A: rate {thinnedA.mean()/Twin:.3f}, var/mean {thinnedA.var()/thinnedA.mean():.3f}")
```
<details><summary>Reconcile</summary>

Merging gives `Poisson(λ_A + λ_B) = Poisson(8)` (superposition) and thinning gives `Poisson(0.2·3) = Poisson(0.6)` (thinning) — both **stay Poisson**, confirmed by rates landing on `7.998` and `0.600` with var/mean ≈ 1 (`0.997` merged, `0.994` thinned). The family is *closed* under superposition and independent thinning, which is precisely why the Poisson turns up so often: any pile-up of many independent rare-event streams, or any randomly-sampled subset of one, is again Poisson. This closure is the discrete cousin of the CLT — a robustness property of the mechanism, not a coincidence of shape.
</details>

**Exercise 03.2 — The Cauchy's median keeps the promise its mean breaks.**
*Setup:* The same `Cauchy(0, 1)` as §03.2. Now track the running **median** instead of the mean.
*Predict:* Does the sample median converge as n → ∞? To what, and at what rate?
*Reason:* "The LLN failed for the mean, so estimating the Cauchy's center from data is hopeless."
*Run:*
```python
for n in (10, 1000, 100_000):
    Rr = 3000 if n <= 1000 else 800
    med = np.array([np.median(rng.standard_cauchy(n)) for _ in range(Rr)])
    print(f"Cauchy median: n={n:>6}  IQR(median) = {iqr(med):.4f}")
```
<details><summary>Reconcile</summary>

The median converges to 0 (the Cauchy's true median; C-B §3.3) and its IQR collapses like 1/√n: `0.6597 → 0.0673 → 0.0069`, roughly a 10× tightening per 100× in n. The mean failed not because Cauchy data is uninformative about location, but because the *mean* is the wrong summary for a heavy tail — one giant draw hijacks it, and there is no population mean underwriting it anyway. A quantile-based estimator ignores the tail's magnitude and stays consistent and efficient. Lesson: match the estimator to the tail, not to habit. The naive "no mean ⇒ can't estimate the center" is simply wrong.
</details>

**Exercise 03.3 — Max-entropy for counts is Geometric, not Poisson.**
*Setup:* A nonnegative-integer quantity (defects per widget) is known only through its mean, 3. You reach for a distribution over {0, 1, 2, …}.
*Predict:* The maximum-entropy distribution with mean 3 — is it `Poisson(3)`?
*Reason:* "Counts with a known rate ⇒ Poisson." (You just saw the Poisson built for exactly this setting in §03.1.)
*Run:*
```python
kk = np.arange(41).astype(float)
pois = stats.poisson(3.0).pmf(kk); pois /= pois.sum()
p_me = maxent_on_grid(kk, [kk], [pois @ kk])                 # max-ent on {0..40} with mean 3
r = (pois @ kk) / (1 + pois @ kk)
geom = (1 - r) * r**kk; geom /= geom.sum()                   # Geometric with the same mean
print(f"max-ent(counts, mean 3) vs Geometric: KL = {kl_nats(p_me, geom):.1e} nats")
print(f"max-ent(counts, mean 3) vs Poisson:   KL = {kl_nats(p_me, pois):.3f} nats")
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(kk - 0.2, p_me, 0.4, label="max-ent (mean only) = Geometric")
ax.bar(kk + 0.2, pois, 0.4, label="Poisson(3)")
ax.set(title="Same mean, different family", xlabel="count", ylabel="prob", xlim=(-0.5, 15))
ax.legend(); save(fig, "maxent_counts")
```
<details><summary>Reconcile</summary>

Max-entropy under a mean constraint is `p_k ∝ e^{λk}` — a **Geometric** (`KL = 4.0e-09` nats, i.e. identical), *not* the Poisson (`KL = 0.651` nats apart). The Poisson is not the least-committal count distribution with a given mean; it is the max-entropy count distribution under the *process* constraints (independent increments), which is far more information than "the average is 3." The Geometric, front-loaded on 0 with a fat geometric tail, is what "only the mean" actually buys you (below). This is §03.1 and §03.4 colliding: "counts at rate 3" names two different families depending on which knowledge you genuinely hold. Choosing a distribution is choosing what you claim to know.

![Two distributions with identical mean 3: the maximum-entropy solution under a mean-only constraint (Geometric, front-loaded on 0) versus Poisson(3) (concentrated near its mean). Same mean, different family.](figures/03-generative-stories/maxent_counts.png)
</details>

**Exercise 03.4 — The cross-entropy loss floor is the label entropy (ML bridge).**
*Setup:* A classifier is trained with cross-entropy loss. At some input the label is genuinely stochastic — its true conditional distribution over three classes is p = [0.7, 0.2, 0.1] (irreducible aleatoric noise; the input does not determine the class).
*Predict:* As training approaches perfection, what cross-entropy loss (in nats) does it approach at this input — 0?
*Reason:* "A well-trained model drives cross-entropy loss to zero."
*Run:*
```python
p_labels = np.array([0.7, 0.2, 0.1])
def xent_nats(p, q): return float(-np.sum(p * np.log(q)))
print(f"min cross-entropy (q=p)      = {xent_nats(p_labels, p_labels):.3f} nats")
print(f"cross-entropy at q=uniform   = {xent_nats(p_labels, np.full(3, 1/3)):.3f} nats")
print(f"label entropy H(p) (nats)    = {-np.sum(p_labels*np.log(p_labels)):.3f} nats")
```
<details><summary>Reconcile</summary>

The best attainable loss is `0.802` nats, not 0 — it equals the label entropy `H(p)`, reached exactly when the model outputs q = p (the KL term vanishes; the entropy floor remains). Cross-entropy = entropy + KL, and training can only kill the KL part; the entropy of the labels is the Bayes error floor, the reason a validation-loss curve plateaus *above* zero on any task with genuine label noise. A model reporting loss below `0.802` here is memorizing noise, not learning. Predicting the floor is exactly the §03.3 identity applied to your loss function — cross-entropy training is KL-minimization onto the label distribution (M15).
</details>

## Takeaways

- A distribution is a generative mechanism; pick the family by matching the mechanism, not the histogram's silhouette. Poisson-count + uniform placement *is* the Poisson process, and Exponential gaps, Gamma waits, and Poisson counts fall out of it.
- The Normal is the "sum of many small finite-variance shocks" story (CLT) — and, independently, the max-entropy story under a fixed mean and variance.
- The CLT/LLN needs finite variance. The Cauchy has no mean; its sample mean is Cauchy at *every* n (IQR ≈ 2, no shrinkage). A non-stabilizing average is a tail problem, not a sample-size problem.
- Surprise is −log p; entropy is expected surprise; cross-entropy is expected surprise under the wrong model; `KL(p ‖ q) = cross-entropy − entropy ≥ 0` is the bits wasted, asymmetric and unbounded.
- The same KL is the training loss (M15), the variational objective (M13), and the predictive score (M17) — learn it once here.
- Maximum entropy is the least-committal distribution consistent with stated constraints: support+mean → Exponential, mean+variance → Normal, mean-on-ℕ → Geometric (not Poisson).
- Softmax is max-entropy over classes; temperature is the Lagrange multiplier (T→0 argmax, T→∞ uniform). These stories share one algebraic skeleton — the exponential family — which is module 04.

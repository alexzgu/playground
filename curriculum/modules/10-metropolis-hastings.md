# 10. Metropolis–Hastings from Scratch

> **Spine.** Thirty lines that provably target the posterior — detailed balance builds the sampler — but the diagnostics that certify it are *necessary, not sufficient*, so you report ESS, not draw count.
> **Which line?** Line 2, mechanized. When the posterior $p(\theta\mid y)$ has no closed form and its normalizing constant is unknown, Metropolis–Hastings conditions anyway, using only ratios of the unnormalized density.
> **Promise.** After this module you can write a random-walk sampler for any unnormalized target, tune its step size by the 0.234 rule and know *why* that number, compute ESS / split-$\hat R$ by hand, and recognize the two ways diagnostics lie — a chain trapped in one mode, and a stuck chain that a single-chain check calls "converged."
> **Prereqs.** Module 09 (Monte Carlo: samples as lingua franca, MCSE, the ESS idea for weighted draws), 05 (the Beta-Binomial posterior we sample), 04 (the likelihood we multiply by a prior). Markov chains are built here from scratch — no prior chain theory assumed.
> **Runtime.** ~65 s (the §10.3 acceptance-vs-ESS sweep is ~27 s of it).
> **Sources.** Booklet ch. 11 (MH), ch. 15 (MCMC diagnostics); Levin–Peres *Markov Chains and Mixing Times* ch. 3–5, 12 (spectral gap, mixing) by concept; Roberts–Gelman–Gilks (1997) for the 0.234 optimum; Vehtari et al. (2021) for rank-normalized $\hat R$.

Module 09 gave you a rule: any expectation is a sample average with a $1/\sqrt M$ error bar. It also gave you a catch — to average over the posterior you need *draws from* the posterior, and rejection or importance sampling collapses the moment the target is even mildly awkward or more than a handful of dimensions. Here is the escape. You do not need to sample the posterior directly, and you do not need its normalizing constant. You need only to *compare* two candidate values: is $\theta'$ more probable than $\theta$, and by what ratio? A Markov chain that makes those comparisons correctly will spend time in each region of parameter space in exact proportion to the posterior — and $p(\theta\mid y)/p(\theta^{\star}\mid y)$ cancels the intractable evidence $p(y)$ entirely. That cancellation is the whole trick, and it is what makes Bayesian computation possible at all.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "10-metropolis-hastings"          # this module's figure dir
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

## 10.1 Just enough Markov chains

A Markov chain on a state space is a rule for stepping from the current state $\theta$ to a next state $\theta'$, using a **transition kernel** $P(\theta,\theta')$ — the probability (density) of landing at $\theta'$ given you are at $\theta$. The chain forgets its past: where it goes next depends only on where it is now. A distribution $\pi$ is **stationary** for $P$ if running one step of the chain leaves it unchanged:
$$\pi P = \pi, \qquad\text{i.e.}\qquad \sum_{\theta}\pi(\theta)\,P(\theta,\theta')=\pi(\theta') \ \ \forall\,\theta'.$$
Stationarity is what we want: if the chain's marginal is ever $\pi$, it stays $\pi$ forever, and (under **ergodicity** — the chain is irreducible, so it can reach every region, and aperiodic, so it does not cycle deterministically) the marginal *converges* to $\pi$ from any start, and time-averages along a single trajectory converge to $\pi$-expectations. That last sentence is the ergodic theorem, the Markov-chain analogue of the law of large numbers; we take it on faith here (Levin–Peres ch. 4) and *verify it numerically* at every turn.

Checking $\pi P=\pi$ directly means summing over all of state space — exactly the intractable sum we are trying to avoid. The way out is a *local* sufficient condition. Say $P$ satisfies **detailed balance** with respect to $\pi$ if
$$\pi(\theta)\,P(\theta,\theta') \;=\; \pi(\theta')\,P(\theta',\theta)\qquad\text{for all }\theta,\theta'.$$
Read it as a flow-balance statement: at equilibrium, the probability mass flowing $\theta\to\theta'$ equals the mass flowing back $\theta'\to\theta$. A chain obeying detailed balance is called **reversible**. The payoff is a six-line proof that reversibility *implies* stationarity — a pairwise, checkable condition delivering the global one:
$$
(\pi P)(\theta') = \sum_{\theta}\pi(\theta)P(\theta,\theta')
\overset{\text{DB}}{=} \sum_{\theta}\pi(\theta')P(\theta',\theta)
= \pi(\theta')\sum_{\theta}P(\theta',\theta)
= \pi(\theta')\cdot 1 = \pi(\theta').
$$
Line by line: expand the definition of $\pi P$; swap each summand using detailed balance; pull the constant $\pi(\theta')$ out; the remaining sum is over all destinations from $\theta'$, which is $1$. Done. **Detailed balance is sufficient but not necessary for stationarity** — plenty of stationary chains are not reversible (a deterministic 3-cycle with the uniform stationary law is the standard counterexample; we build it below). Non-reversible chains can even mix *faster*. But reversibility is the property we know how to *engineer*, and Metropolis–Hastings is the engine.

**The Metropolis–Hastings kernel.** Pick any **proposal** $q(\theta'\mid\theta)$ you can sample from — say a Gaussian centered at the current state. From $\theta$, draw a candidate $\theta'\sim q(\cdot\mid\theta)$ and **accept** it with probability
$$\alpha(\theta,\theta') = \min\!\left(1,\ \frac{\pi(\theta')\,q(\theta\mid\theta')}{\pi(\theta)\,q(\theta'\mid\theta)}\right).$$
If accepted, move to $\theta'$; otherwise stay at $\theta$ (and record $\theta$ again). Two things to notice. First, $\pi$ appears only as the *ratio* $\pi(\theta')/\pi(\theta)$, so any unnormalized $\tilde\pi\propto\pi$ gives the identical rule — the evidence $p(y)$ cancels. Second, for a **symmetric** proposal ($q(\theta'\mid\theta)=q(\theta\mid\theta')$, e.g. a Gaussian random walk) the $q$'s cancel too and you are left with the original Metropolis rule $\alpha=\min(1,\ \pi(\theta')/\pi(\theta))$: always accept uphill moves, accept downhill moves with probability equal to the density ratio. That is the whole algorithm.

Why does it target $\pi$? Because the accept/reject step is *designed* to enforce detailed balance. For $\theta\ne\theta'$ the kernel is $P(\theta,\theta')=q(\theta'\mid\theta)\alpha(\theta,\theta')$, and
$$\pi(\theta)\,q(\theta'\mid\theta)\,\alpha(\theta,\theta')
=\min\!\big(\pi(\theta)q(\theta'\mid\theta),\ \pi(\theta')q(\theta\mid\theta')\big),$$
which is symmetric under swapping $\theta\leftrightarrow\theta'$ — that is detailed balance, and by the six-line lemma $\pi$ is stationary. Let us watch it hold on a chain small enough to write the whole kernel down.

```python
# A 3-state target and the Metropolis kernel that reverses w.r.t. it.
pi = np.array([0.2, 0.5, 0.3])                 # unnormalized is fine; this sums to 1
# Symmetric proposal: from state i, propose each *other* state w.p. 1/2.
# Metropolis acceptance for a symmetric proposal is min(1, pi_j/pi_i).
P = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        if i != j:
            P[i, j] = 0.5 * min(1.0, pi[j] / pi[i])
    P[i, i] = 1.0 - P[i].sum()                  # stay-probability absorbs rejections
print("transition matrix P (rows sum to 1):")
print(np.round(P, 4))

flow = pi[:, None] * P                          # flow[i,j] = pi_i P_ij
print(f"detailed balance  max|flow - flow.T|  = {np.abs(flow - flow.T).max():.2e}")
print(f"stationarity      max|pi P - pi|      = {np.abs(pi @ P - pi).max():.2e}")
eig = np.sort(np.linalg.eigvals(P.T).real)[::-1]
print(f"eigenvalues of P: {np.round(eig, 4)}   (leading = 1, gap = {1 - eig[1]:.4f})")

# 'sufficient, not necessary': a deterministic 3-cycle is stationary for the
# uniform law but flagrantly non-reversible.
Cyc = np.array([[0., 1, 0], [0, 0, 1], [1, 0, 0]])
u = np.full(3, 1/3)
flow_c = u[:, None] * Cyc
print(f"\n3-cycle:  max|uP - u| = {np.abs(u @ Cyc - u).max():.2e}  (stationary)"
      f"   max|flow - flow.T| = {np.abs(flow_c - flow_c.T).max():.3f}  (NOT reversible)")
```

Detailed balance holds to machine precision (`0.00e+00`), so $\pi=(0.2,0.5,0.3)$ is stationary to machine precision, and the leading eigenvalue of $P$ is exactly $1$ with the rest inside the unit circle — the spectral fact §10.7 turns into a mixing rate. The 3-cycle confirms the "sufficient, not necessary" clause: it holds the uniform law stationary (`0.00e+00`) while violating detailed balance by a full `0.333` — mass flows around the cycle one way only. Reversibility is a design choice, not a law of nature.

## 10.2 Thirty lines that target the posterior

Now the real thing. In module 05 the Beta-Binomial posterior was a closed form; here we pretend we only know the *unnormalized* posterior — prior times likelihood — and recover it by sampling. Take a $\mathrm{Beta}(1,1)$ prior and $k=6$ successes in $n=20$ trials. The posterior is $\mathrm{Beta}(7,15)$ (we keep the exact answer only to grade the sampler). A random-walk Metropolis sampler is thirty lines, most of them bookkeeping.

```python
# Target: unnormalized log-posterior of a Beta(1,1) prior + Binomial(20, .) with k=6.
# log p(theta | y) = (a-1) log theta + (b-1) log(1-theta) + const, a=7, b=15.
a_post, b_post = 7, 15
exact_post = stats.beta(a_post, b_post)

def log_target(theta):
    if theta <= 0.0 or theta >= 1.0:
        return -np.inf                          # prior support is (0, 1)
    return (a_post - 1) * np.log(theta) + (b_post - 1) * np.log1p(-theta)

def rw_metropolis(log_p, x0, step, n_draws, gen):
    """Random-walk Metropolis. Returns (chain, acceptance_rate)."""
    x, lx = x0, log_p(x0)
    chain = np.empty(n_draws)
    accepts = 0
    for t in range(n_draws):
        x_prop = x + step * gen.standard_normal()          # symmetric Gaussian step
        lp = log_p(x_prop)
        if np.log(gen.random()) < lp - lx:                 # accept w.p. min(1, ratio)
            x, lx, accepts = x_prop, lp, accepts + 1        # ...in log space
        chain[t] = x                                        # record even on reject
    return chain, accepts / n_draws

g_bb = np.random.default_rng(SEED + 1)
chain, acc = rw_metropolis(log_target, 0.3, 0.1, 40_000, g_bb)
chain = chain[2000:]                                        # discard warm-up
print(f"acceptance rate = {acc:.3f}")
print(f"posterior mean:  MH = {chain.mean():.4f}   exact = {exact_post.mean():.4f}")
print("  quantile      MH      exact")
for q in (0.05, 0.25, 0.50, 0.75, 0.95):
    print(f"    {q:.2f}      {np.quantile(chain, q):.4f}  {exact_post.ppf(q):.4f}")

fig, ax = plt.subplots(1, 2, figsize=(11, 3.6))
ax[0].plot(chain[:1500], lw=0.6, color="C0")
ax[0].set_xlabel("iteration"); ax[0].set_ylabel(r"$\theta$")
ax[0].set_title("trace: a healthy random walk (first 1500 draws)")
th = np.linspace(0, 1, 400)
ax[1].hist(chain, bins=60, density=True, color="C0", alpha=0.5, label="MH draws")
ax[1].plot(th, exact_post.pdf(th), "k--", lw=2, label="exact Beta(7,15)")
ax[1].set_xlabel(r"$\theta$"); ax[1].set_ylabel("density")
ax[1].set_title("MH histogram vs exact posterior"); ax[1].legend(fontsize=9)
save(fig, "beta-binomial-mh")
```

The sampler never once used the number $\mathrm{Beta}(7,15)$; it saw only `log_target`, a prior-times-likelihood it could evaluate up to an additive constant. Yet the quantiles land on the exact posterior to within about a thousandth — the $5\%$ quantile is `0.1688` against the truth `0.1682`, the median `0.3116` against `0.3126`, the $95\%$ quantile `0.4864` against `0.4874` — and the mean is `0.3177` versus `0.3182`. Thirty lines, no conjugacy required. The two lines that matter are `np.log(gen.random()) < lp - lx` (accept in log space, so tiny densities do not underflow) and `chain[t] = x` inside *both* branches (a rejected move still produces a draw — the current state, repeated).

![Left: a fuzzy-caterpillar trace of theta wandering around 0.3. Right: the MH histogram sitting exactly under the exact Beta(7,15) density.](figures/10-metropolis-hastings/beta-binomial-mh.png)

The trace is the "fuzzy caterpillar" you want to see — no trends, no sticking, rapid back-and-forth around the posterior mean. The histogram lies under the exact density. But that visual health is *cheap*; §10.4 and §10.6 show two chains that look healthy and are lying. First, the tuning knob.

## 10.3 Tuning: why the magic number is 0.234

The one free parameter is the step size. Too small and the chain crawls, accepting almost every tiny move but taking forever to cross the posterior; too large and almost every proposal overshoots into low density and is rejected, so the chain sits still. Both extremes waste draws. The right metric is not acceptance itself but **effective sample size** — module 09's currency: $M$ correlated draws are worth $\mathrm{ESS}=M/\big(1+2\sum_{k\ge1}\rho_k\big)\le M$ independent ones, where $\rho_k$ is the lag-$k$ autocorrelation. We want the step size that *maximizes ESS per iteration*.

**Setup.** Two targets. A one-dimensional standard normal, and — the case that matters — a $d=50$ product of independent standard normals, $\pi(\theta)=\prod_{i=1}^{50}\mathcal N(\theta_i;0,1)$, the canonical stand-in for a moderate-dimensional posterior. Sweep the proposal scale, record acceptance rate and average per-coordinate ESS.

**Predict.** Commit to a number. *What acceptance rate maximizes ESS?* The naive instinct says "you want your proposals to be accepted, so aim high — 80%, 90%." A more sophisticated guess splits the difference at 50%. Write down your guess for the $d=50$ target before running. (The naive intuition: a rejected proposal is a wasted draw, so minimize rejections.)

```python
def acf_fft(x):                                  # autocovariance via FFT (fast, exact)
    x = x - x.mean(); n = len(x)
    f = np.fft.rfft(x, n=2 * n)
    acov = np.fft.irfft(f * np.conj(f))[:n].real / n
    return acov

def ess_1d(x):
    n = len(x); acov = acf_fft(x)
    if acov[0] <= 0:                             # constant chain: no information
        return 1.0
    rho = acov / acov[0]
    tau = 1.0                                     # integrated autocorrelation time
    for k in range(1, n):
        if rho[k] < 0:                            # truncate at first negative (Geyer)
            break
        tau += 2 * rho[k]
    return n / tau

def rw_metropolis_nd(d, step, n_draws, gen):
    x = np.zeros(d); lx = -0.5 * x @ x
    chain = np.empty((n_draws, d)); accepts = 0
    for t in range(n_draws):
        xp = x + step * gen.standard_normal(d)   # isotropic Gaussian proposal
        lp = -0.5 * xp @ xp                       # log N(0, I_d) up to constant
        if np.log(gen.random()) < lp - lx:
            x, lx, accepts = xp, lp, accepts + 1
        chain[t] = x
    return chain, accepts / n_draws

def sweep(d, steps, n_draws, burn, seed):
    gen = np.random.default_rng(seed); rows = []
    for s in steps:
        ch, ar = rw_metropolis_nd(d, s, n_draws, gen); ch = ch[burn:]
        ess = float(np.mean([ess_1d(ch[:, j]) for j in range(d)]))
        rows.append((s, ar, ess))
    return rows

d = 50
opt_step = 2.38 / np.sqrt(d)                      # Roberts-Gelman-Gilks scaling
steps50 = np.array([0.15, 0.20, 0.25, 0.30, opt_step, 0.40, 0.50, 0.65, 0.85])
rows50 = sweep(d, steps50, 20_000, 4000, SEED + 2)
print(f"d = 50 product target   (theory: step 2.38/sqrt(d) = {opt_step:.3f})")
print("   step   accept    ESS")
for s, ar, ess in rows50:
    print(f"  {s:.3f}   {ar:.3f}   {ess:6.1f}")
peak50 = max(rows50, key=lambda r: r[2])
print(f"  -> ESS peaks at acceptance = {peak50[1]:.3f}, step = {peak50[0]:.3f}")

steps1 = np.array([1.0, 1.5, 2.0, 2.4, 2.8, 3.4, 4.2, 5.5, 7.5])
rows1 = sweep(1, steps1, 30_000, 4000, SEED + 3)
peak1 = max(rows1, key=lambda r: r[2])
print(f"d = 1  standard normal:  ESS peaks at acceptance = {peak1[1]:.3f}, "
      f"step = {peak1[0]:.2f}")
print(f"asymptotic optima -> 1-D: 0.44   high-d product: 0.234")

fig, ax = plt.subplots(figsize=(7.2, 4.2))
ar50 = [r[1] for r in rows50]; es50 = [r[2] / peak50[2] for r in rows50]
ar1  = [r[1] for r in rows1];  es1  = [r[2] / peak1[2]  for r in rows1]
ax.plot(ar50, es50, "o-", color="C0", label="d = 50 product target")
ax.plot(ar1,  es1,  "s--", color="C1", label="d = 1 standard normal")
ax.axvline(0.234, color="C0", lw=1, ls=":"); ax.axvline(0.44, color="C1", lw=1, ls=":")
ax.text(0.234, 0.35, " 0.234", color="C0", fontsize=9)
ax.text(0.44, 0.25, " 0.44", color="C1", fontsize=9)
ax.set_xlabel("acceptance rate"); ax.set_ylabel("ESS / peak ESS")
ax.set_title("Efficiency vs acceptance: the optimum drops with dimension")
ax.legend(fontsize=9)
save(fig, "acceptance-sweep")
```

**Run and reconcile.** For the $d=50$ target, ESS peaks at acceptance `0.240` — near neither 90% nor 50%, but close to the theoretical `0.234`, hit at step `0.337` $=2.38/\sqrt{50}$. Around that peak the curve is *flat*: acceptance from `0.292` (step 0.30) down to `0.161` (step 0.40) all deliver essentially peak ESS, so the practical target is a broad band, not a knife's edge. The naive "accept everything" instinct is badly wrong — at acceptance `0.598` (step 0.15) ESS is `63.4`, only about 58% of the peak `110.0`, because the chain, though rarely rejected, moves in steps too timid to decorrelate.

The `0.234` is not folklore. **Theorem** (Roberts, Gelman & Gilks 1997, asymptotic): for a target that is a product of $d$ i.i.d. smooth one-dimensional densities, as $d\to\infty$ the random-walk proposal scale that maximizes efficiency is $2.38/\sqrt d$, and the acceptance rate there converges to `0.234`. The scope words are load-bearing: it is an *asymptotic-in-$d$, product-target* result, derived via a diffusion limit. In genuinely low dimension the optimum is different — our one-dimensional sweep peaks at acceptance `0.439`, matching the known 1-D optimum near `0.44`, not 0.234. Real posteriors are neither i.i.d. products nor infinite-dimensional, so read `0.234` as a *design target you aim near*, not a convergence test you must pass; anything in the rough 15–40% band on a moderate-dimensional problem is doing fine. (For gradient-based samplers the analogous optimum is higher, ≈0.651 for HMC — module 12.)

![Two curves of normalized ESS against acceptance rate; the d=50 curve peaks near 0.234, the d=1 curve peaks near 0.44, both broad and flat around their maxima.](figures/10-metropolis-hastings/acceptance-sweep.png)

The two peaks sitting at different acceptance rates *is* the lesson: the efficient acceptance rate falls as dimension rises, because in high dimension a random step is almost surely uphill-in-some-coordinates and downhill-in-others, so even a well-scaled proposal is usually a net loss and must be small. Report ESS, tune toward the band, and never trust a single acceptance number without knowing the dimension it came from.

## 10.4 When one chain lies: the bimodal trap

Every diagnostic so far certified a chain that *was* fine. Now a chain that is not. Consider a bimodal target — an equal mixture of $\mathcal N(-5,1)$ and $\mathcal N(+5,1)$. The two modes are ten standard deviations apart, separated by a valley of near-zero density. This is a caricature of a real hazard: multimodal posteriors arise from mixture models (module 19), label-switching symmetries, and weakly-identified parameters.

**Setup.** Run the §10.2 random-walk sampler on this target, well-tuned for *local* exploration (step 1.0, giving a healthy ~70% acceptance), started in the left mode at $\theta=-5$.

**Predict.** *Will one chain, run for 40,000 iterations, find both modes?* The naive intuition — "MCMC is ergodic, and 40,000 steps is a lot; given enough time it explores everything" — says yes, the histogram will show two equal humps. Commit.

```python
def log_bimodal(x, sep=5.0):                     # 0.5 N(-sep,1) + 0.5 N(+sep,1)
    a, b = -0.5 * (x + sep)**2, -0.5 * (x - sep)**2
    m = max(a, b)
    return m + np.log(0.5 * np.exp(a - m) + 0.5 * np.exp(b - m))

g_bim = np.random.default_rng(SEED + 5)
bim, acc_bim = rw_metropolis(log_bimodal, -5.0, 1.0, 40_000, g_bim)
bim = bim[2000:]
crossings = int(np.sum(np.abs(np.diff(np.sign(bim))) > 0))
print(f"step 1.0 (local-optimal):  acceptance {acc_bim:.3f}, "
      f"mode crossings {crossings}, P(theta > 0) = {np.mean(bim > 0):.4f}  (truth 0.5)")

g_big = np.random.default_rng(SEED + 6)
big, acc_big = rw_metropolis(log_bimodal, -5.0, 10.0, 40_000, g_big)
big = big[2000:]
cross_big = int(np.sum(np.abs(np.diff(np.sign(big))) > 0))
print(f"step 10  (mode-spanning):  acceptance {acc_big:.3f}, "
      f"mode crossings {cross_big}, P(theta > 0) = {np.mean(big > 0):.4f}")

fig, ax = plt.subplots(1, 2, figsize=(11, 3.6))
ax[0].plot(bim[:6000], lw=0.6, color="C3")
ax[0].axhline(0, color="k", lw=0.8, ls=":")
ax[0].set_xlabel("iteration"); ax[0].set_ylabel(r"$\theta$")
ax[0].set_title("trapped: step 1.0 never leaves the left mode")
grid = np.linspace(-9, 9, 400)
dens = np.array([np.exp(log_bimodal(z)) for z in grid]); dens /= np.trapezoid(dens, grid)
ax[1].hist(bim, bins=60, density=True, color="C3", alpha=0.5, label="MH draws")
ax[1].plot(grid, dens, "k--", lw=2, label="true bimodal target")
ax[1].set_xlabel(r"$\theta$"); ax[1].set_ylabel("density")
ax[1].set_title("half the posterior is invisible"); ax[1].legend(fontsize=9)
save(fig, "bimodal-trap")
```

**Reconcile.** The well-tuned chain crosses between modes exactly `0` times in 40,000 iterations and estimates $P(\theta>0)=$ `0.0000` — it declares the right mode has *zero* posterior mass, when the truth is $0.5$. The chain is not broken; it is doing precisely what detailed balance promises, sampling the mode it is in. The problem is time: to cross the valley by a random walk it must string together many low-density proposals in a row, and the probability of that is exponentially small in the barrier height. Ergodicity is an asymptotic guarantee, and "asymptotic" here means longer than any run you will do.

You might think the fix is a bigger step. It half-works *in one dimension*: step 10 spans the gap, logging `2798` crossings and recovering $P(\theta>0)=$ `0.5026`. But look at the cost — acceptance has crashed to `0.200`, because a step tuned to leap between modes wildly overshoots *within* a mode. And this rescue is a one-dimensional illusion: in higher dimension, or with modes farther apart, no single step size both spans the barrier and explores a mode, and the multimodal problem becomes genuinely hard. The real fixes change the dynamics — **parallel tempering** runs a ladder of flattened targets so a hot chain can hop barriers and pass the moves down (demonstrated in module 19); the mode-hopping caveat is the first thing to remember when a posterior might be multimodal.

![Left: the trace pinned near -5, never crossing zero. Right: the MH histogram covers only the left hump while the true target has two equal humps.](figures/10-metropolis-hastings/bimodal-trap.png)

The trace looks *stationary* — flat, stable, no trend. That is exactly why a single chain cannot be trusted: local stationarity is indistinguishable from global convergence when you only ever see one basin. The cure is to run several chains from dispersed starts and compare them, which is what the rest of the module builds.

## 10.5 Diagnostics you compute by hand

Return to the well-behaved Beta-Binomial target and run it *properly*: **four chains** from **overdispersed starting points**, so that agreement between them is evidence, not coincidence. Three diagnostics, each computed from scratch, then cross-checked against ArviZ.

```python
def run_chains(log_p, inits, step, n_draws, seed):
    gen = np.random.default_rng(seed)
    return np.array([rw_metropolis(log_p, x0, step, n_draws, gen)[0] for x0 in inits])

chains = run_chains(log_target, [0.10, 0.25, 0.40, 0.55], 0.1, 4000, SEED + 10)
M, N = chains.size, chains.shape[1]              # total draws, per-chain length
print(f"4 chains x {N} draws = {M} total;  overall mean {chains.mean():.4f} "
      f"(exact {exact_post.mean():.4f})")
```

**Trace and ACF.** The trace should show four caterpillars overlapping in the same band; the autocorrelation function should decay to zero within a few dozen lags. A slow-decaying ACF is the signature of a chain that shuffles rather than jumps.

```python
fig, ax = plt.subplots(1, 2, figsize=(11, 3.6))
for j in range(4):
    ax[0].plot(chains[j, :800], lw=0.6, alpha=0.8)
ax[0].set_xlabel("iteration"); ax[0].set_ylabel(r"$\theta$")
ax[0].set_title("four overdispersed chains mix into one band")
lags = np.arange(41)
mean_acf = np.mean([acf_fft(chains[j]) / acf_fft(chains[j])[0] for j in range(4)], axis=0)
ax[1].bar(lags, mean_acf[:41], color="C0", width=0.8)
ax[1].axhline(0, color="k", lw=0.8)
ax[1].set_xlabel("lag $k$"); ax[1].set_ylabel(r"$\rho_k$")
ax[1].set_title("autocorrelation decays by ~lag 30")
save(fig, "diagnostics")
```

![Left: four colored traces all wandering in the same 0.15-0.5 band. Right: an autocorrelation bar chart decaying from 1 to near zero by lag 30.](figures/10-metropolis-hastings/diagnostics.png)

**ESS, multi-chain.** The single-chain formula generalizes: pool the between-chain variance $B$ and within-chain variance $W$ into $\widehat{\mathrm{var}}^+=\frac{N-1}{N}W+\frac1N B$, estimate the combined autocorrelation $\rho_k=1-(W-\overline{\text{acov}}_k)/\widehat{\mathrm{var}}^+$ from the average within-chain autocovariance, and truncate the sum. **Split-$\hat R$.** Split each chain in half (to catch *within*-chain trends), giving $2m$ half-chains, and compare between-half to within-half variance: $\hat R=\sqrt{\widehat{\mathrm{var}}^+/W}$. At convergence the chains are interchangeable, $B\to0$, and $\hat R\to1$; the standard threshold is $\hat R<1.01$.

```python
def ess_multichain(C):
    m, n = C.shape
    W = C.var(axis=1, ddof=1).mean()
    B = n * C.mean(axis=1).var(ddof=1)
    var_plus = (n - 1) / n * W + B / n
    avg_acov = np.mean([acf_fft(C[j]) for j in range(m)], axis=0)
    rho = 1.0 - (W - avg_acov) / var_plus         # rho[0] = 1 by construction
    tau, k = 1.0, 1
    while k + 1 < n:                              # Geyer initial positive pairs
        pair = rho[k] + rho[k + 1]
        if pair < 0:
            break
        tau += 2 * pair; k += 2
    return m * n / tau

def split_rhat(C):
    m, n = C.shape; h = n // 2
    S = np.vstack([C[:, :h], C[:, h:2 * h]])      # 2m half-chains
    W = S.var(axis=1, ddof=1).mean()
    B = h * S.mean(axis=1).var(ddof=1)
    var_plus = (h - 1) / h * W + B / h
    return np.sqrt(var_plus / W)

def rank_normalize(C):                            # Vehtari et al. 2021 transform
    r = stats.rankdata(C.ravel())
    z = stats.norm.ppf((r - 3/8) / (r.size - 1/4))
    return z.reshape(C.shape)

ess_raw   = ess_multichain(chains)
ess_bulk  = ess_multichain(rank_normalize(chains))    # ArviZ's default 'bulk' ESS
rhat_plain = split_rhat(chains)
rhat_rank  = split_rhat(rank_normalize(chains))       # ArviZ's default rank-R-hat
print(f"HAND:  ESS(raw) = {ess_raw:.1f}   ESS(rank/bulk) = {ess_bulk:.1f}   "
      f"of M = {M}")
print(f"HAND:  split-Rhat (plain) = {rhat_plain:.4f}   (rank-normalized) = {rhat_rank:.4f}")
```

By hand, the bulk ESS is `2304.9` out of `16000` draws — the sixteen thousand correlated draws are worth about twenty-three hundred independent ones, an efficiency near $0.14$. **This is the number to report.** Quoting "16,000 draws" would overstate your Monte Carlo precision by roughly $\sqrt{16000/2300}\approx2.6\times$. Split-$\hat R$ is `1.0014` (rank-normalized), comfortably under 1.01.

Now cross-check against ArviZ — and mind the version trap. **ArviZ 1.x defaults to *rank-normalized* split-$\hat R$ and *bulk* ESS** (Vehtari et al. 2021), which first replace each draw by the normal score of its rank across all chains. This makes the diagnostics robust to heavy tails and invariant to reparameterization, but it means a naive by-hand $\hat R$ on the raw draws will *not* match ArviZ's default — you must rank-normalize first, which is why we computed both. ArviZ's `az.ess` and `az.rhat` accept a raw `(chain, draw)` array directly.

```python
import arviz as az
print(f"ArviZ: az.ess  = {float(az.ess(chains)):.1f}   (matches hand rank/bulk)")
print(f"ArviZ: az.rhat = {float(az.rhat(chains)):.4f}   (matches hand rank-normalized)")
```

ArviZ reports ESS `2313.4` and $\hat R$ `1.0014`. Our hand-rolled *rank-normalized* versions (`2304.9` and `1.0014`) match to well under a percent — the residual gap is only a difference in the autocorrelation-truncation rule. On this well-mixed, light-tailed target the transform barely matters: plain $\hat R$ is `1.0013`, one part in $10^4$ from the rank version. The choice bites when chains are heavy-tailed or badly mixed — in §10.6 the same two statistics read `5.5422` (plain) versus `1.7365` (rank) on the same draws, both alarming but wildly different numbers. The lesson: your diagnostics library made a modeling choice on your behalf — know which one, so you compare like with like.

## 10.6 The fooling example: a stuck chain that "passes"

The bimodal trap of §10.4 was caught the instant we looked at the histogram. Here is the more insidious failure: a chain whose *single-chain* diagnostics — the ones a hurried analyst actually checks — all say "converged," while the chain has sampled nothing.

**Setup.** The bimodal target again, but now watch what a per-chain audit reports. Take one chain started at $\theta=-5$, run 4000 draws, and compute *its own* split-$\hat R$ (splitting the single chain in half) and its ESS. Then run four chains from $\{-5,-5,+5,+5\}$ and compute the multi-chain $\hat R$.

**Predict.** *Do the single-chain diagnostics flag the problem?* The intuition being tested: "split-$\hat R$ near 1 and a few hundred ESS mean the chain converged." Guess the single-chain $\hat R$ and the four-chain $\hat R$ before running.

```python
foolers = run_chains(log_bimodal, [-5.0, -5.0, 5.0, 5.0], 1.0, 4000, SEED + 11)
c0 = foolers[0:1]                                  # one chain, stuck in the left mode
print(f"per-chain mode crossings: "
      f"{[int(np.sum(np.abs(np.diff(np.sign(c)))>0)) for c in foolers]}")
print(f"per-chain means: {np.round(foolers.mean(axis=1), 2)}")
print("\nSINGLE-CHAIN AUDIT (chain 0 only):")
print(f"  split-Rhat = {float(split_rhat(c0)):.4f}   ('converged', < 1.01)")
print(f"  az.ess     = {float(az.ess(c0)):.1f}   ('plenty of effective draws')")
print(f"  its own P(theta > 0) = {np.mean(c0 > 0):.4f}")
print("\nFOUR-CHAIN AUDIT:")
print(f"  az.rhat = {float(az.rhat(foolers)):.4f}   (plain {float(split_rhat(foolers)):.4f})")
print(f"  az.ess  = {float(az.ess(foolers)):.1f}")

fig, ax = plt.subplots(figsize=(7.2, 3.6))
for j in range(4):
    ax.plot(foolers[j, :1500], lw=0.7, alpha=0.85,
            label=f"chain {j} (start {[-5,-5,5,5][j]:+d})")
ax.axhline(0, color="k", lw=0.8, ls=":")
ax.set_xlabel("iteration"); ax.set_ylabel(r"$\theta$")
ax.set_title(r"Four chains, two answers: split-$\hat R$ = 1.74 catches what one chain hides")
ax.legend(fontsize=8, ncol=2)
save(fig, "fooling-example")
```

**Reconcile.** Chain 0 is stuck in the left mode — `0` crossings, its own $P(\theta>0)=$ `0.0000` — yet its single-chain split-$\hat R$ is `1.0028` (well under 1.01) and its ESS is `573.6`. Every diagnostic you can compute *from one chain* certifies convergence, because within its basin the chain genuinely is stationary: both halves look identical, so split-$\hat R$ sees nothing wrong. The problem is invisible until chains that explored *different* basins are compared. The four-chain $\hat R$ is `1.7365` — a five-alarm fire, since two chains sit at $-5$ and two at $+5$, so between-chain variance dwarfs within-chain variance. The multi-chain ESS collapses to `6.1`: four chains of four thousand draws are worth six independent samples, because they represent only two distinct answers.

![Four traces splitting into two flat groups, two pinned near -5 and two near +5, none ever crossing zero.](figures/10-metropolis-hastings/fooling-example.png)

This is the case for the discipline the field converged on: **always run multiple chains from overdispersed starts, and read $\hat R$ before anything else.** A single chain's clean diagnostics are necessary for convergence but nowhere near sufficient — they cannot see a mode the chain never visited. Diagnostics detect *non*-convergence; they never prove convergence.

## 10.7 Mixing is a spectral gap

Why do some chains decorrelate in ten steps and others in ten thousand? The answer is spectral. A reversible transition matrix $P$ has real eigenvalues $1=\lambda_1>\lambda_2\ge\cdots\ge\lambda_n>-1$; the leading eigenvector is $\pi$ (stationarity), and the **second-largest eigenvalue** $\lambda_2$ governs how fast everything else decays. The gap $1-\lambda_2$ is the **spectral gap**, and its reciprocal is the **relaxation time** $t_{\mathrm{rel}}=1/(1-\lambda_2)$ — the number of steps to shrink a perturbation by a factor $e$ (Levin–Peres ch. 12). A large gap means fast mixing; a gap near zero — as when two modes are joined by a thin bridge — means the relaxation time, and with it the autocorrelation time, blows up.

**Setup.** The smallest chain that shows it: two states with $P=\begin{psmallmatrix}0.95&0.05\\0.15&0.85\end{psmallmatrix}$ — a mildly sticky switch, nothing exotic. We will simulate a long trajectory, measure the autocorrelation of the state indicator, and only then compute the spectrum.

**Predict.** *How fast does the autocorrelation of the state indicator decay?* If you think "a two-state chain is trivial — it decorrelates in a step or two," commit to a number for the lag-1 autocorrelation and for the lag at which the ACF first drops below one half, before running anything.

```python
a, b = 0.05, 0.15
P2 = np.array([[1 - a, a], [b, 1 - b]])

g_sp = np.random.default_rng(SEED + 7)
Nsp = 200_000; s = 0; ind = np.empty(Nsp)
for t in range(Nsp):
    ind[t] = (s == 0)                             # indicator of state 0
    s = 0 if g_sp.random() < P2[s, 0] else 1
rho_meas = (acf_fft(ind) / acf_fft(ind)[0])
print(f"measured rho[1..5] = {np.round(rho_meas[1:6], 4)}")

# Now the spectral explanation, computed only after the measurement:
lam2 = np.sort(np.linalg.eigvals(P2).real)[::-1][1]
t_rel = 1.0 / (1.0 - lam2)
pi2 = np.array([b / (a + b), a / (a + b)])        # stationary law
tau_int_theory = (1 + lam2) / (1 - lam2)          # AR(1)-type integrated autocorr
print(f"theory   lam2^k    = {np.round(lam2**np.arange(1, 6), 4)}")
print(f"lambda_2 = {lam2:.3f}   relaxation time 1/(1-lambda_2) = {t_rel:.2f}")
print(f"empirical pi_0 = {ind.mean():.4f}  (theory {pi2[0]:.4f})"
      f"   integrated autocorr time (1+l)/(1-l) = {tau_int_theory:.2f}")

fig, ax = plt.subplots(figsize=(7.2, 3.8))
kk = np.arange(0, 26)
ax.plot(kk, rho_meas[:26], "o", color="C0", ms=4, label="measured ACF")
ax.plot(kk, lam2**kk, "-", color="C3", lw=2, label=r"$\lambda_2^{\,k}$ (spectral prediction)")
ax.axvline(t_rel, color="k", lw=1, ls=":")
ax.text(t_rel + 0.3, 0.8, r"$t_{\mathrm{rel}}=1/(1-\lambda_2)=5$", fontsize=9)
ax.set_xlabel("lag $k$"); ax.set_ylabel("autocorrelation")
ax.set_title("Mixing is a spectral gap: ACF decays as the second eigenvalue")
ax.legend(fontsize=9)
save(fig, "spectral-gap")
```

**Reconcile.** The measured autocorrelation is `0.8023` at lag 1, `0.6447` at lag 2, `0.518` at lag 3 — nowhere near "decorrelated in a step or two," and the ACF does not fall below one half until lag 4. The explanation is the spectrum: for a two-state chain the second eigenvalue is $\lambda_2=1-a-b=1-0.05-0.15=$ `0.800` exactly, and the measured ACF tracks $\lambda_2^k=0.8,0.64,0.512,\dots$ almost perfectly. The chain's memory decays geometrically at rate $\lambda_2$, with relaxation time $t_{\mathrm{rel}}=1/(1-\lambda_2)=$ `5.00` steps and an integrated autocorrelation time of $(1+\lambda_2)/(1-\lambda_2)=$ `9.00` — each draw is worth about a ninth of an independent one. The empirical stationary frequency is `0.7516`, matching $\pi_0=0.75$.

![Measured autocorrelation points falling exactly on the curve lambda_2^k = 0.8^k, with a dotted line at the relaxation time of 5 lags.](figures/10-metropolis-hastings/spectral-gap.png)

The measured ACF lies on the $\lambda_2^k$ curve, and the relaxation time marks where it has decayed to about $1/e$. This is the theory beneath every diagnostic in this module: **mixing is the spectral gap; the ACF, ESS, and $\hat R$ are all empirical probes of $1-\lambda_2$.** A multimodal posterior has an exponentially small gap (the thin bridge is a near-eigenvector at $\lambda_2\approx1$), which is *why* §10.4's chain took forever — the relaxation time was astronomically large. In continuous state spaces the same story holds with the eigenvalues of the transition *operator* (Levin–Peres ch. 12, by concept); we cannot diagonalize a million-dimensional operator, which is exactly why we fall back on ESS and $\hat R$ to detect a small gap indirectly.

## Bridge — simulated annealing, the optimizer cousin

Metropolis–Hastings has a twin in optimization. To *maximize* an objective $f(\theta)$ rather than sample a posterior, run Metropolis on the tempered target $\pi_T(\theta)\propto\exp(f(\theta)/T)$ and slowly lower the **temperature** $T$. At high $T$ the target is nearly flat and the chain roams freely, crossing barriers (the §10.4 escape, bought with heat); as $T\to0$ the distribution concentrates on the global maximizer, and the chain settles there. This is **simulated annealing** — Metropolis–Hastings with a cooling schedule. *Predict:* we plant the walker in the *shallower* of two wells — does cooling rescue it into the global minimum, or freeze it where it started?

```python
def U(x):                                          # a double well; global min near -2
    return 0.5 * x**4 - 4 * x**2 + 0.3 * x
grid = np.linspace(-3, 3, 6001)
x_star = grid[np.argmin(U(grid))]
print(f"global min near x = {x_star:.3f} (U = {U(x_star):.3f}); "
      f"local well at +2 has U(+2) = {U(2.0):.3f}")

g_an = np.random.default_rng(SEED + 8)
x, best, bestU = 2.0, 2.0, U(2.0)                  # START in the WRONG (local) well
for T in np.geomspace(3.0, 0.02, 4000):            # cooling schedule
    xp = x + 0.5 * g_an.standard_normal()
    if np.log(g_an.random()) < -(U(xp) - U(x)) / T:   # Metropolis on exp(-U/T)
        x = xp
    if U(x) < bestU:
        best, bestU = x, U(x)
print(f"annealed from the +2 well -> best x = {best:.3f}, U = {bestU:.3f}")
```

Started deliberately in the shallower well at $+2$ (where $U=$ `-7.400`), the annealer escapes over the barrier while $T$ is high and converges to the global minimizer near $x=$ `-2.019` with $U=$ `-8.603`. Same accept/reject step, same detailed-balance machinery — only the target is deliberately deformed and cooled. Bayesian sampling and global optimization are the same algorithm read at two temperatures, and this is the seed of module 19's **parallel tempering** (run several temperatures at once and swap) and a cousin of the SGD-as-sampling view in module 12.

## Pitfalls

- **Reporting draw count instead of ESS.** Sixteen thousand autocorrelated draws with ESS `2304.9` carry the Monte Carlo precision of about twenty-three hundred independent ones. Quote ESS (and, from module 09, the MCSE $s/\sqrt{\mathrm{ESS}}$); the raw draw count flatters your error bars by the square root of the autocorrelation factor.
- **Trusting a single chain.** A trapped chain (§10.4, §10.6) is *locally* stationary and passes every within-chain check — clean trace, low single-chain $\hat R$, healthy ESS — while missing entire modes. Run $\ge4$ chains from overdispersed starts and read multi-chain split-$\hat R$ first, always.
- **Chasing 100% acceptance.** High acceptance usually means a step size too small to decorrelate: the §10.3 chain at 60% acceptance had half the peak ESS. Tune toward the 15–40% band on moderate-dimensional problems (≈0.234 asymptotically), not toward 1.
- **Applying 0.234 out of scope.** It is an asymptotic, i.i.d.-product-target, random-walk result. In one dimension the optimum is ≈`0.44`; for HMC it is ≈0.651; for a strongly correlated or low-dimensional posterior it is only a rough guide. It is a design target, never a convergence test.
- **Reading a by-hand $\hat R$ against ArviZ's default and panicking at the mismatch.** ArviZ 1.x rank-normalizes; your plain $\hat R$ will differ. Rank-normalize before comparing, or expect a benign gap.
- **Believing a healthy trace proves convergence.** Diagnostics are necessary, not sufficient: they detect non-convergence (a small spectral gap) but can never certify that the chain has seen everything it needs to. The bridge you never crossed leaves no trace.

## Exercises

**Exercise 10.1 — The evidence never appears.**
*Setup:* You sample a posterior $p(\theta\mid y)\propto p(y\mid\theta)\,p(\theta)$ with Metropolis, evaluating `log_target` as log-likelihood + log-prior, *omitting* the evidence $\log p(y)$ entirely. A colleague insists your draws are biased because you "forgot to normalize."
*Predict:* Will adding a constant $\log p(y)$ (any constant) to `log_target` change a single accepted/rejected decision, hence the draws?
*Reason:* The intuition that "an unnormalized density is not a real distribution, so sampling it must be wrong" — the thing that makes MCMC feel like cheating.
*Run:*
```python
g1 = np.random.default_rng(SEED + 20)
g2 = np.random.default_rng(SEED + 20)              # SAME seed -> same proposals/uniforms
base, _  = rw_metropolis(log_target, 0.3, 0.1, 8000, g1)
shift = 12.7                                        # a made-up 'log evidence'
shifted, _ = rw_metropolis(lambda t: log_target(t) + shift, 0.3, 0.1, 8000, g2)
print(f"max|difference| between the two chains = {np.abs(base - shifted).max():.2e}")
```
<details><summary>Reconcile</summary>

The two chains are byte-identical: `max|difference| = 0.00e+00`. The acceptance test compares `log(u) < lp_prop - lp_current`, and any additive constant cancels exactly in that difference — not one accept/reject decision changes. Your colleague is wrong; "unnormalized" is not "incorrect." The flip side is worth keeping: because the sampler never touches $p(y)$, it also cannot *estimate* $p(y)$ — the evidence for model comparison in module 17 needs a different device. (Exercise 10.4 shows the same cancellation from the detailed-balance side, and where it appears in ML.)
</details>

**Exercise 10.2 — Guess the effective sample size.**  *(surprising)*
*Setup:* Two random-walk samplers on the same standard-normal target, each producing $M=20{,}000$ draws. Sampler A uses step 0.3 (acceptance ≈ 0.91); sampler B uses step 2.4 (acceptance ≈ 0.44).
*Predict:* Rank the two by ESS. Many reach for A — "91% acceptance means it almost never wastes a proposal, so it must be more efficient." Commit to a rank and a rough ESS ratio.
*Reason:* Equating acceptance rate with efficiency — the belief that a rejected proposal is the only kind of waste.
*Run:*
```python
gA = np.random.default_rng(SEED + 21); gB = np.random.default_rng(SEED + 22)
cA, arA = rw_metropolis_nd(1, 0.3, 20_000, gA)
cB, arB = rw_metropolis_nd(1, 2.4, 20_000, gB)
print(f"A: acceptance {arA:.3f}, ESS {ess_1d(cA[3000:, 0]):.0f}")
print(f"B: acceptance {arB:.3f}, ESS {ess_1d(cB[3000:, 0]):.0f}")
```
<details><summary>Reconcile</summary>

Sampler B — the one that *rejects more than half* its proposals — wins by an order of magnitude in ESS. A's near-total acceptance is a symptom, not a virtue: its steps are so timid that consecutive draws are almost identical, so its autocorrelation time is enormous and its ESS tiny. B accepts less but *moves* when it does, decorrelating in a handful of steps. The waste that matters is not rejection; it is failure to move. This is the §10.3 lesson made personal: efficiency is ESS per iteration, and it is maximized well away from full acceptance. The same trap recurs in optimization — a tiny learning rate "accepts" every gradient step and converges glacially.
</details>

**Exercise 10.3 — How far apart before the chain gives up?**
*Setup:* The bimodal target $\tfrac12\mathcal N(-s,1)+\tfrac12\mathcal N(+s,1)$ with a well-tuned local step (1.0), varying the separation $s$. At $s=5$ (§10.4) a 40,000-step chain crossed zero times.
*Predict:* At which separation does a single chain still cross freely — $s=1$? $s=2$? $s=3$? Predict the crossing count at each before running.
*Reason:* Linear intuition — "twice the distance, half the crossings" — applied to a barrier whose cost is exponential.
*Run:*
```python
for s in (1.0, 2.0, 3.0):
    gg = np.random.default_rng(SEED + 30 + int(s))
    ch, _ = rw_metropolis(lambda x: log_bimodal(x, s), -s, 1.0, 40_000, gg)
    ch = ch[2000:]
    print(f"sep {s:.0f}: crossings {int(np.sum(np.abs(np.diff(np.sign(ch)))>0)):5d}, "
          f"P(theta>0) = {np.mean(ch>0):.3f}")
```
<details><summary>Reconcile</summary>

The crossing count does not halve; it *collapses* super-exponentially. At $s=1$ the modes overlap and the chain crosses thousands of times ($P(\theta>0)\approx0.5$, healthy); at $s=2$ it still crosses a couple thousand times, roughly balanced; by $s=3$ crossings have fallen some thirty-fold to a few hundred and the mass estimate already skews (0.55), and §10.4's $s=5$ gave exactly zero. The valley between modes has depth $\propto s^2$ (the log-density at the midpoint falls quadratically), and the random-walk crossing rate falls like $e^{-\Theta(s^2)}$. This is the spectral gap of §10.7 shrinking toward zero: a small increase in separation is an exponential increase in relaxation time. It is why "just run it longer" fails for multimodal posteriors and why tempering (module 19) exists.
</details>

**Exercise 10.4 — Detailed balance by construction.**  *(ML/DL bridge)*
*Setup:* You have an unnormalized target $\tilde\pi$ on 4 states and *any* symmetric proposal. You suspect a bug: does your Metropolis kernel really reverse with respect to $\tilde\pi$, even though your code never sees the normalized $\pi$?
*Predict:* Build the full $4\times4$ Metropolis kernel from $\tilde\pi=(3,1,4,1)$ (unnormalized) with the uniform "propose any other state" proposal. Will detailed balance hold with respect to the *normalized* $\pi=\tilde\pi/9$ to machine precision?
*Reason:* The worry that using unnormalized $\tilde\pi$ in the acceptance ratio "leaks" a constant into the kernel and breaks reversibility.
*Run:*
```python
pit = np.array([3., 1., 4., 1.]); pin = pit / pit.sum()
K = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        if i != j:
            K[i, j] = (1/3) * min(1.0, pit[j] / pit[i])    # symmetric propose 1/3 each
    K[i, i] = 1 - K[i].sum()
flow = pin[:, None] * K
print(f"max|pi K - pi|          = {np.abs(pin @ K - pin).max():.2e}")
print(f"max|flow - flow.T| (DB) = {np.abs(flow - flow.T).max():.2e}")
```
<details><summary>Reconcile</summary>

Both are zero to machine precision: the kernel reverses with respect to the normalized $\pi$ despite the code only ever touching ratios $\tilde\pi_j/\tilde\pi_i=\pi_j/\pi_i$. Detailed balance is a statement about *flows*, $\pi_i K_{ij}=\pi_j K_{ji}$, and the acceptance rule sets $\pi_i K_{ij}=\tfrac13\min(\pi_i,\pi_j)$, symmetric in $(i,j)$ by construction — the normalizer divides out of both sides. This is the discrete twin of Exercise 10.1 and the mechanism behind every energy-based model in ML: a Boltzmann/energy model $p(\theta)\propto e^{-E(\theta)}$ is sampled by MCMC using only *energy differences* $E(\theta')-E(\theta)$, never the partition function $Z=\sum e^{-E}$ — the same intractable constant, dodged the same way. Contrastive divergence and Langevin samplers for such models are this exercise at scale.
</details>

## Takeaways

- **The whole algorithm is a ratio test.** Propose, then accept with probability $\min(1,\ \tilde\pi(\theta')q(\theta\mid\theta')/[\tilde\pi(\theta)q(\theta'\mid\theta)])$. Only ratios of the *unnormalized* target appear, so the intractable evidence $p(y)$ cancels — that cancellation is what makes Bayesian computation possible.
- **Detailed balance builds correctness; ergodicity delivers it in the limit.** $\pi(\theta)P(\theta,\theta')=\pi(\theta')P(\theta',\theta)$ implies stationarity in six lines (sufficient, not necessary). Metropolis–Hastings is engineered to satisfy it for any target you can evaluate up to a constant.
- **Report ESS, not draw count.** $M$ correlated draws are worth $\mathrm{ESS}=M/(1+2\sum_k\rho_k)$ independent ones; here 16,000 draws bought ESS ≈ 2300. The raw count overstates precision by the square root of the autocorrelation factor.
- **Tune toward ≈0.234, but know the scope.** The 0.234 optimum is asymptotic for i.i.d.-product targets under a random walk; the 1-D optimum is ≈0.44, HMC's is ≈0.651. Aim for the 15–40% band and maximize ESS, not acceptance.
- **Diagnostics are necessary, never sufficient.** A single chain trapped in one mode passes every within-chain check while missing half the posterior. Run ≥4 overdispersed chains and read multi-chain split-$\hat R$ (rank-normalized in ArviZ 1.x) before trusting anything.
- **Mixing is a spectral gap.** The relaxation time is $1/(1-\lambda_2)$; the ACF decays as $\lambda_2^k$. Multimodality drives $\lambda_2\to1$ and the gap to zero, which is why barriers are fatal and why ESS/$\hat R$ exist to detect the collapse indirectly.
- **Sampling and optimization are one algorithm at two temperatures.** Simulated annealing is Metropolis on $\pi^{1/T}$ with $T\to0$; tempering (module 19) exploits the same lever to cross barriers.

# P1. The Algebra of Densities

> **Spine.** A density is an algebraic object you factor into `kernel(θ) · (stuff free of θ)`; conjugate Bayes is *entirely* this factoring — drop the constant, name the kernel, read off the parameters, never integrate.
> **Which line?** The machinery of line 2 (conditioning). `posterior ∝ likelihood × prior` is *executed* by density algebra; without these reflexes every "clearly the posterior is Beta" is a wall.
> **Promise.** After this you can look at $\theta^{9}(1-\theta)^{3}\cdot(\text{junk})$ and say "Beta(10,4), mean 0.7143" in one breath — and know exactly which constant you just discarded and why you were allowed to.
> **Prereqs.** P0 (diagnostic). Uses only numpy/scipy. **Runtime.** ~2 s.
> **Sources.** C-B §3.3 (kernel recognition), §7.2 (conjugacy); booklet ch. 3–5, 8; walls quoted from course modules 01/04/05/10/11 and EXAM.

This is a drill room, not a chapter. Six reflexes, each staged the same way: the **reflex** (what an expert fires without thinking), **the wall** (a real line from the course where the skill is used silently — cited `module:line`), **the fix** (a runnable installer), **a drill** (predict, then run). The reflexes are ordered GATE-first: the first three block whole topics until you own them.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import betaln, gammaln, gamma as Gamma_fn

SLUG = "P1-density-algebra"
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

## P1.1 ∝ in which variable? (GATE)

**Reflex.** Every `∝` silently carries a subscript naming the *one* variable it holds fixed-vs-free. Anything that is not that variable is a constant and gets absorbed — no matter how much data it contains.

**The wall.** Module 04 compares two experiments that produced the same 9-of-12 heads and writes their likelihoods $L_F(\theta)=\binom{12}{9}\theta^9(1-\theta)^3$, $L_S(\theta)=\binom{11}{9}\theta^9(1-\theta)^3$, then: *"The binomial coefficients differ, but they are constants in $\theta$. As functions of $\theta$ the two likelihoods are **proportional**"* (`modules/04-likelihood.md:233`). The student objects that $\binom{12}{9}$ "has data in it, it's not a constant" — and refuses to drop it. Same objection stalls `p(θ|x) ∝ p(x|θ)p(θ)` at every appearance (`modules/04-likelihood.md:10`, `modules/05-conjugate-updating.md:10`, `modules/10-metropolis-hastings.md:60`).

**The fix.** The proportionality in `p(θ|x)` is *in θ*; the data `x` are frozen numbers. So $\binom{12}{9}=220$ is a (big) constant and vanishes on normalization; $\theta^{9}$ stays. Multiplying a likelihood by any θ-free factor cannot move the posterior:

```python
grid = np.linspace(1e-6, 1 - 1e-6, 4000)
kernel = grid**9 * (1 - grid)**3                 # the part that depends on θ
def normalize(u, g):                              # turn any kernel into a density on grid g
    return u / np.trapezoid(u, g)
post_F = normalize(220.0 * kernel, grid)          # C(12,9) = 220 out front
post_S = normalize(165.0 * kernel, grid)          # C(11,9) = 165 out front — different constant
print(f"C(12,9)/C(11,9) = {220/165:.4f}   (the constant we dropped)")
print(f"max|post_F − post_S| = {np.max(np.abs(post_F - post_S)):.2e}   (identical posteriors)")
```

The two coefficients differ by a factor of `1.3333`, yet the normalized posteriors agree to `1.33e-15` (floating-point dust): the constant divided out. That is the whole content of "the likelihood principle" reduced to one line of arithmetic.

**Drill P1.1 — the data-loaded constant.**
*Setup:* You observe $x=3$ from Poisson($\theta$), so $p(x\mid\theta)=\theta^{3}e^{-\theta}/3!$. A classmate writes the likelihood-in-θ as $\theta^{3}e^{-\theta}/6$ and insists the $1/6$ must be kept "because 6 came from the data."
*Predict:* Does keeping vs dropping the $1/3!$ change the *posterior* under any prior? Yes / No.
*Reason:* You are trusting the rule "constants free of the proportionality variable drop." The trap is that $1/3!$ *looks* data-derived.
*Run:*
```python
th = np.linspace(1e-6, 12, 4000)
prior = stats.gamma(a=2, scale=1/1).pdf(th)       # Gamma(2, rate 1) prior on θ
with_const    = normalize((th**3 * np.exp(-th) / 6) * prior, th)
without_const = normalize((th**3 * np.exp(-th))     * prior, th)
print(f"max|with − without| = {np.max(np.abs(with_const - without_const)):.2e}")
```
<details><summary>Reconcile</summary>

`max|with − without| = 1.11e-16` (machine epsilon). The $1/3!$ is a fixed number *once $x=3$ is observed* — the observation froze it. "Depends on the data" is not the test; "depends on the proportionality variable θ" is. This is exactly why MCMC never needs the evidence $p(y)$: it too is a θ-free constant (`modules/10-metropolis-hastings.md:60`).
</details>

## P1.2 Spot the kernel (GATE) — the marquee

**Reflex.** Given a messy density, instantly split it into `kernel(θ) · (θ-free stuff)`, recognize the kernel as a named family, and read off its parameters — *without computing any integral*. The kernel alone determines the distribution; the normalizer is bookkeeping you look up, never derive.

**The wall.** This is *the* move the sources make without slowing down — Casella–Berger even define the word mid-computation: *"We now recognize the integrand in (2.3.5) as the kernel of another gamma pdf. (The kernel of a function is the main part of the function, the part that remains when constants are disregarded.)"* (`curriculum_material/casella_berger/Ch1to5.txt:1442`) — the definition and the reflex in one breath, an entire integral skipped. The booklet proves a credible-interval property with the immortal *"**Proof.** Straightforward."* (`curriculum_material/bayesian_booklet/ch08-bayesian-inference.md:119`). Module 05 does the Beta read-off in one line: $\theta^{(a+s)-1}(1-\theta)^{(b+f)-1}=\mathrm{Beta}(a+s,\ b+f)$ (`modules/05-conjugate-updating.md:130`); module 04 sets `Lg = grid**9 * (1 - grid)**3` and calls it a Beta kernel (`modules/04-likelihood.md:256`).

**The fix.** Cover the normalizer with your thumb and match what's left against six shapes: $\theta^{\alpha-1}(1-\theta)^{\beta-1}\to$ Beta; $x^{\alpha-1}e^{-\beta x}\to$ Gamma(shape α, **rate** β); $e^{-(x-\mu)^2/2\sigma^2}\to$ Normal; $\lambda^x/x!\to$ Poisson; $\lambda^k e^{-\lambda}\to$ Gamma-in-λ; and on the simplex $\prod_k \theta_k^{\alpha_k-1}\to$ Dirichlet(α) — the multivariate Beta, *add 1 to each exponent* (its conjugate-to-Multinomial update just adds category counts, `modules/05-conjugate-updating.md:280`). Then read off parameters and *verify against the named density*, the #1 habit in the whole course:

```python
# θ^9 (1−θ)^3 → Beta(10, 4): add 1 to each exponent. Mean = 10/14.
beta_kernel = grid**9 * (1 - grid)**3
match_beta  = np.max(np.abs(normalize(beta_kernel, grid) - stats.beta(10, 4).pdf(grid)))
# x^2 e^{−5x} → Gamma(shape 3, rate 5): mean = 3/5 = 0.6.
xg = np.linspace(1e-6, 12, 4000)
match_gam = np.max(np.abs(normalize(xg**2 * np.exp(-5*xg), xg) - stats.gamma(a=3, scale=1/5).pdf(xg)))
print(f"Beta(10,4): mean 10/14 = {10/14:.4f},  kernel vs pdf agree to {match_beta:.1e}")
print(f"Gamma(3, rate 5): mean 3/5 = {3/5:.4f},  kernel vs pdf agree to {match_gam:.1e}")
```

The normalized kernel and the scipy pdf agree to `3.1e-13` and `4.1e-10` (grid-discretization only). So the posterior in the wall is Beta(10,4) with mean `0.7143` — read off, not integrated. Plotted, the hand-built kernel and the library density are the *same curve*:

```python
fig, ax = plt.subplots()
ax.fill_between(grid, normalize(beta_kernel, grid), color="C0", alpha=0.35, label="normalize(θ⁹(1−θ)³)")
ax.plot(grid, stats.beta(10, 4).pdf(grid), "C1--", lw=2, label="scipy Beta(10,4)")
ax.axvline(10/14, color="k", ls=":", lw=1, label="mean 0.7143")
ax.set_xlabel("θ"); ax.set_ylabel("density"); ax.set_title("The kernel alone fixes the distribution")
ax.legend()
save(fig, "kernel-readoff")
```

![Normalizing the bare kernel θ⁹(1−θ)³ reproduces scipy's Beta(10,4) exactly; the two curves coincide.](figures/P1-density-algebra/kernel-readoff.png)

**Drill P1.2 — the λ trap.**
*Setup:* A single Poisson observation gives $p(x\mid\lambda)=\lambda^{x}e^{-\lambda}/x!$. You now treat this *as a function of $\lambda$* (data $x$ fixed) to build a likelihood.
*Predict:* Viewed in $\lambda$, is the kernel $\lambda^{x}e^{-\lambda}$ a Poisson kernel or a Gamma kernel? What is the implied "distribution shape" over λ for $x=4$?
*Reason:* The formula "looks Poisson." The trap is that *which variable is free* changes the family the shape belongs to.
*Run:*
```python
lam = np.linspace(1e-6, 20, 4000)
shape_in_lambda = normalize(lam**4 * np.exp(-lam), lam)     # x = 4, free variable is λ
gamma_5_1 = stats.gamma(a=5, scale=1/1).pdf(lam)            # Gamma(shape 5, rate 1)
print(f"kernel λ⁴e^−λ vs Gamma(5,1): agree to {np.max(np.abs(shape_in_lambda - gamma_5_1)):.1e}")
```
<details><summary>Reconcile</summary>

Agreement `3.3e-06`: $\lambda^{4}e^{-\lambda}$ is the **Gamma(shape 5, rate 1)** kernel, not Poisson. Same symbols, different free variable, different family — this is why a Gamma prior is conjugate to a Poisson likelihood (their kernels are the same shape in λ, so the product is again Gamma). Reading the exponent of λ as "shape − 1" gives shape 5; the $e^{-\lambda}$ gives rate 1. Missing this is the single most common conjugacy stumble.
</details>

## P1.3 Product → sum, and posterior updating = adding sufficient statistics

**Reflex.** An iid product $\prod_i p(x_i\mid\theta)$ collapses by two laws — $\prod e^{a_i}=e^{\sum a_i}$ and $\prod c=c^n$ — so exponents add and the sufficient statistics ($\sum x_i$, $\sum x_i^2$, $n$) fall out. Conjugate updating is then *literally* "add the data's sufficient statistics to the prior's."

**The wall.** The EXAM does a Gamma–Poisson fit in one line, `an, bn = a0 + y1.sum(), b0 + n1` (`EXAM.md:106`): posterior shape = prior shape + $\sum y$, posterior rate = prior rate + $n$. No derivation — the reader is expected to see the likelihood kernel $\lambda^{\sum y}e^{-n\lambda}$ slot into the Gamma prior. Same silent move in module 05's Beta read-off (`modules/05-conjugate-updating.md:130`).

**The fix.** Derive the collapse for Poisson, then *verify the closed-form update against a brute-force grid posterior* — guilty until it reproduces a known answer:

```python
y = rng.poisson(3.0, size=40)                      # 40 iid Poisson draws, true λ = 3
a0, b0 = 2.0, 1.0                                  # Gamma(2, rate 1) prior on λ
an, bn = a0 + y.sum(), b0 + len(y)                 # conjugate update: add Σy and n
lam = np.linspace(1e-6, 8, 6000)
brute = normalize(lam**y.sum() * np.exp(-len(y)*lam) * stats.gamma(a0, scale=1/b0).pdf(lam), lam)
closed = stats.gamma(an, scale=1/bn).pdf(lam)
print(f"suff stats: Σy = {y.sum()}, n = {len(y)}  →  posterior Gamma({an:.0f}, {bn:.0f})")
print(f"closed-form vs brute-force grid posterior: agree to {np.max(np.abs(closed - brute)):.1e}")
```

The dataset of 40 numbers entered the posterior through exactly two of them, $\sum y=$ `126` and $n=40$; the closed form Gamma(`128`, `41`) matches the grid posterior to `3.2e-13`. That compression — 40 numbers → 2 — *is* sufficiency, appearing for free from the product-to-sum collapse.

**Drill P1.3 — order and batching (the ML connection).**
*Setup:* A logistic-regression-style online learner sees a stream of Bernoulli outcomes and keeps a running count $(k,n)$ as its state (`modules/25-deep-learning-lenses.md:203` uses `csum = np.cumsum(bits, 1)` for exactly this). You will feed the *same* 10 outcomes in two different orders, updating a Beta(1,1) prior.
*Predict:* Do the two orderings give the same final posterior? Does one batch update equal ten sequential updates?
*Reason:* Intuition from SGD says order matters (path-dependence). The trap: exact Bayesian updating is not SGD.
*Run:*
```python
bits = np.array([1,0,1,1,0,1,0,0,1,1])
def beta_from(seq):                                # add successes to a, failures to b
    return 1 + seq.sum(), 1 + (len(seq) - seq.sum())
a_fwd = beta_from(bits); a_rev = beta_from(bits[::-1]); a_shuf = beta_from(rng.permutation(bits))
clean = lambda t: tuple(int(v) for v in t)
print(f"forward {clean(a_fwd)}, reversed {clean(a_rev)}, shuffled {clean(a_shuf)}")
```
<details><summary>Reconcile</summary>

All three are `(7, 5)`. Because the likelihood is a *product*, multiplication commutes: sequential = batch = any permutation (`modules/05-conjugate-updating.md:487`). The state $(k,n)$ is a lossless sufficient statistic, so the learner can forget the raw stream. This is the opposite of SGD, whose order-dependence comes from *approximate*, non-commuting gradient steps — the exact posterior has no such path-dependence.
</details>

## P1.4 Complete the square in the exponent (scalar)

**Reflex.** When two Gaussian exponents multiply, gather the $x^2$ and $x$ coefficients, use $ax^2-2bx = a(x-b/a)^2 - b^2/a$, read off mean $b/a$ and variance $1/a$, and sweep the leftover $-b^2/a$ into `∝`.

**The wall.** Module 05 forms the Normal–Normal posterior and writes: *"the log-posterior is a sum of two quadratics in θ; completing the square (expand, collect the θ² and θ terms, and read off the Gaussian) gives"* the precision-addition formula (`modules/05-conjugate-updating.md:174`). The words "expand, collect, read off" are the entire derivation; the algebra is left to your hands. Same move powers the Kalman update (`modules/21-state-space.md:21`) and the ridge/Gaussian-prior MAP (`modules/25-deep-learning-lenses.md:69`).

**The fix.** Multiply two unit-variance Gaussians centered at 0 and 4. Collect: exponent $=-\tfrac12(x^2+(x-4)^2)=-\tfrac12(2x^2-8x)+c$, so $a=2$, $b=4$, mean $=b/a=2$, variance $=1/a=0.5$. Verify by normalizing the product numerically:

```python
xg = np.linspace(-6, 10, 8000)
prod = normalize(np.exp(-xg**2/2) * np.exp(-(xg-4)**2/2), xg)  # N(0,1) × N(4,1), unnormalized
m = np.trapezoid(xg*prod, xg); v = np.trapezoid((xg-m)**2*prod, xg)
print(f"completed square → mean b/a = {4/2:.4f}, var 1/a = {1/2:.4f}")
print(f"numerical product posterior → mean {m:.4f}, var {v:.4f}")
```

The pencil answer (mean `2.0000`, var `0.5000`) matches the numerical product (mean `2.0000`, var `0.5000`). Two precisions of 1 added to give precision 2 (variance 0.5); the mean is the precision-weighted average $(1\cdot0 + 1\cdot4)/2 = 2$. That is P3's master pattern, and here it is nothing but "collect the quadratic."

**Drill P1.4 — the precision-weighted mean.**
*Setup:* Prior $\theta\sim N(0,1)$; you observe $n=4$ iid points with mean $\bar y = 3$, known noise variance $\sigma^2=4$.
*Predict:* Is the posterior mean closer to 0 or to 3? Give a number before running. (Naive averaging of "0 and 3" says 1.5.)
*Reason:* You are tempted to average the two centers equally. The trap: they carry different precisions.
*Run:*
```python
m0, t2, n4, ybar, s2 = 0.0, 1.0, 4, 3.0, 4.0
prec = 1/t2 + n4/s2                                # prior precision + data precision
mean_post = (m0/t2 + n4*ybar/s2) / prec
print(f"posterior precision = {prec:.4f}, variance = {1/prec:.4f}, mean = {mean_post:.4f}")
prec1 = 1/t2 + n4/1.0                               # same data but σ² = 1 (sharper likelihood)
print(f"if σ²=1: precision = {prec1:.4f}, mean = {(m0/t2 + n4*ybar/1.0)/prec1:.4f}")
```
<details><summary>Reconcile</summary>

Posterior mean `1.5000`, precision `2.0000`. Here the naive 1.5 happens to be *right* — but only because prior precision $1/1=1$ equals data precision $4/4=1$. Change $\sigma^2$ to 1 and the data precision becomes 4, dragging the mean to `2.4000` (precision `5.0000`). The lesson: never average centers; average *precisions*, then weight. The equal-weight intuition is a coincidence of matched precisions, not a law.
</details>

## P1.5 The sum-of-squares decomposition

**Reflex.** $\sum_i(x_i-\mu)^2 = \underbrace{n(\bar x-\mu)^2}_{\text{shift}} + \underbrace{\sum_i(x_i-\bar x)^2}_{\text{scatter }S}$ — the cross term vanishes because $\sum(x_i-\bar x)=0$. So any quadratic-in-μ splits into "distance of μ from $\bar x$" plus a μ-free constant.

**The wall.** Module 04's NIG helper computes `S = ((data - xbar)**2).sum()  # S = Σx² − nx̄²` and feeds it to the variance posterior (`modules/04-likelihood.md:111`). The EXAM's Normal–Inverse-Gamma scale update is the decomposition's prior-shift variant, `bn4 = b0n + 0.5*Sxx + 0.5*k0*n4/kn*(ybar4 - m0)**2` (`EXAM.md:284`): within-data scatter *plus* a shrink-toward-prior term. Without the identity it is an unmotivated string of symbols.

**The fix.** Verify the split for arbitrary data and arbitrary μ, then assemble the NIG rate $b_n = b_0 + \tfrac12 S + \tfrac12\cdot\tfrac{\kappa_0 n}{\kappa_n}(\bar x - m_0)^2$:

```python
x = rng.normal(5, 2, size=30); xbar = x.mean(); mu = 1.3
lhs = np.sum((x - mu)**2)
S   = np.sum((x - xbar)**2)                        # μ-free scatter
rhs = len(x)*(xbar - mu)**2 + S                    # shift + scatter
print(f"Σ(x−μ)²      = {lhs:.4f}")
print(f"n(x̄−μ)² + S  = {rhs:.4f}   (difference {abs(lhs-rhs):.1e})")
k0, m0, b0 = 1.0, 0.0, 3.0; kn = k0 + len(x)       # prior-shift (NIG) variant, EXAM:284
b_n = b0 + 0.5*S + 0.5*k0*len(x)/kn*(xbar - m0)**2
print(f"NIG rate b_n = {b_n:.4f}  = prior {b0} + ½·scatter + ½·shrink-to-prior")
```

The two forms of $\sum(x_i-\mu)^2$ agree to `2.3e-13` — machine precision, since it is an identity, not an approximation. The scatter $S$ is what survives when μ is free; the shift term is how far your chosen center sits from $\bar x$.

**Drill P1.5 — where does the sum of squares bottom out?**
*Setup:* You will minimize $g(\mu)=\sum_i(x_i-\mu)^2$ over μ for the 30-point sample above.
*Predict:* At which μ is $g$ minimized, and what is the minimum value — in terms of quantities you already printed?
*Reason:* You know least squares picks the mean; the second part tests whether you see the *minimum value* is the scatter $S$.
*Run:*
```python
mus = np.linspace(xbar - 3, xbar + 3, 4001)
g = ((x[:,None] - mus[None,:])**2).sum(0)
print(f"argmin μ = {mus[g.argmin()]:.4f} (x̄ = {xbar:.4f}),  min g = {g.min():.4f} (S = {S:.4f})")
```
<details><summary>Reconcile</summary>

Minimizer `5.0081` = $\bar x$, minimum value `116.2375` = $S$. The decomposition makes this instant: $g(\mu)=n(\bar x-\mu)^2+S$ is a parabola in μ with vertex at $\bar x$ and floor $S$. So $\bar x$ is the least-squares point *by algebra*, and the residual sum of squares $S$ is the irreducible scatter no location can remove. Every OLS normal equation and every NIG variance posterior rides on this one line.
</details>

## P1.6 Gamma/Beta-function fluency

**Reflex.** $\Gamma(n)=(n-1)!$, $\Gamma(\tfrac12)=\sqrt\pi$; $B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$; and $\int(\text{kernel of a known density})=1/(\text{its constant})$, so a marginal likelihood is a *ratio of Beta (or Gamma) functions* — computed in logs via `betaln`/`gammaln`, never as factorials.

**The wall.** Module 01 evaluates a Beta-Binomial marginal as `np.exp(betaln(a + k, b + n - k) - betaln(a, b))` (`modules/01-probability-as-logic.md:251`); the EXAM's exact log-evidence is `gammaln(n+1) − gammaln(k+1) − gammaln(n−k+1) + betaln(a0p+k, b0p+n−k) − betaln(a0p, b0p)` (`EXAM.md:226`). Both assume you see the evidence $\int_0^1 \binom{n}{k}\theta^{a+k-1}(1-\theta)^{b+n-k-1}\,d\theta$ as "the Beta kernel integrates to its own normalizer $B(a+k,b+n-k)$."

**The fix.** Compute a Beta-Binomial evidence two ways — the betaln formula and a brute-force integral of likelihood×prior — and confirm they agree; then show why logs are mandatory:

```python
k, n, a0, b0 = 6, 10, 2.0, 3.0
from scipy.special import comb
log_ev = np.log(comb(n, k)) + betaln(a0 + k, b0 + n - k) - betaln(a0, b0)
evidence_betaln = np.exp(log_ev)
th = np.linspace(1e-9, 1 - 1e-9, 200000)          # ∫ p(k|θ) p(θ) dθ, done numerically
integrand = comb(n, k) * th**k * (1-th)**(n-k) * stats.beta(a0, b0).pdf(th)
evidence_int = np.trapezoid(integrand, th)
print(f"B(a,b) = Γ(a)Γ(b)/Γ(a+b) check: {np.exp(betaln(2,3)):.6f} vs {Gamma_fn(2)*Gamma_fn(3)/Gamma_fn(5):.6f}")
print(f"evidence via betaln = {evidence_betaln:.6f},  via ∫ = {evidence_int:.6f}")
print(f"Γ(1/2) = {Gamma_fn(0.5):.6f},  √π = {np.sqrt(np.pi):.6f}")
```

The Beta-function identity checks (`0.083333` both ways), and the evidence agrees to six digits: `0.104895` from the ratio of Beta functions, `0.104895` from the integral. The two-Beta-function ratio *is* the integral — you never integrated.

**Drill P1.6 — why `betaln`, not `Beta`.**
*Setup:* You need the normalizer $B(500,500)$ for a Beta(500,500) posterior (an easy sample size).
*Predict:* Will `Gamma(500)*Gamma(500)/Gamma(1000)` return a usable number in float64? What does `betaln` give?
*Reason:* You expect "just compute the three gammas." The trap: each $\Gamma(500)$ overflows float64 (max $\approx 10^{308}$) long before the ratio is taken.
*Run:*
```python
with np.errstate(over="ignore", invalid="ignore"):
    naive = Gamma_fn(500) * Gamma_fn(500) / Gamma_fn(1000)   # Γ(500) overflows float64
stable = np.exp(betaln(500, 500))
print(f"naive Γ·Γ/Γ = {naive},   betaln route = {stable:.3e}")
```
<details><summary>Reconcile</summary>

The naive route prints `nan` (or `inf/inf`): $\Gamma(500)\approx10^{1131}$ overflows float64's $\approx10^{308}$ ceiling, so even the *ratio* $\infty/\infty$ is undefined. `betaln` computes $\log B$ by summing `gammaln` values — all modest numbers — then exponentiates once, giving `1.480e-302`, a real (tiny) density normalizer. This is P7's "live in the log domain" reflex previewed: any product of large factorials or Gamma values must be assembled in logs, or float64 eats it before you finish.
</details>

## Where the course uses this

Each reflex, and the exact walls it removes (verified `module:line`, mined from `research/`):

| Reflex | Removes the wall at |
|---|---|
| ∝ in which variable | `04:10`, `04:233`, `05:10`, `10:60`, `14:179`, `15:155`, `EXAM:174` |
| Spot the kernel | `03:281`, `04:47`, `04:256`, `05:130`, `05:280`, `07:190`, `11:83`, `11:86`, `19:76` |
| Product → sum / add sufficient statistics | `04:47`, `05:130`, `05:487`, `25:203`, `26:80`, `EXAM:106` |
| Complete the square (scalar) | `05:174`, `19:428`, `21:21`, `23:374`, `25:69` |
| Sum-of-squares decomposition | `04:111`, `11:86`, `17:275`, `19:127`, `26:80`, `EXAM:284` |
| Gamma/Beta-function fluency | `01:251`, `05:335`, `07:190`, `EXAM:226` |

The matrix versions — completing the square in $\beta$, quadratic forms $x^\top\Sigma^{-1}x$, Cholesky over `inv` — live in **P6**; the log-domain and parameterization-trap craft that Drill P1.6 previews lives in **P7**.

## Pitfalls

- **Dropping a θ-dependent factor "because it looks constant."** The test is dependence on the *proportionality variable*, not on the data. $\binom{n}{k}$ drops in θ; $\theta^k$ never does.
- **Keeping a data-loaded constant "because it has data in it."** Once the data are observed, $1/x!$, $\binom{n}{k}$, and $p(y)$ are all frozen numbers — they cannot bend the posterior.
- **Integrating to normalize when you could read off.** If the kernel is one of the five families, you already know the constant; reaching for `quad` signals you missed the kernel.
- **Reading $\lambda^k e^{-\lambda}$ as Poisson when λ is the free variable.** Same symbols, different family — it is a Gamma kernel in λ. This is the conjugacy stumble behind half of "why is the prior a Gamma?"
- **Assembling normalizers as raw Gamma/factorials.** $\Gamma(500)$ overflows; always go through `betaln`/`gammaln` and exponentiate last.
- **Averaging two centers with equal weight.** The precision-weighted mean equals the naive average *only* when precisions match — a coincidence, not a rule.

## Takeaways

- A density is `kernel · (θ-free stuff)`; the kernel alone fixes the distribution, and `∝` always carries a hidden "in which variable."
- Match a bare kernel to one of six shapes (Beta, Gamma, Normal, Poisson, Gamma-in-λ, Dirichlet on the simplex) and read parameters off the exponents — no integral.
- iid products collapse: exponents add, sufficient statistics ($\sum x$, $\sum x^2$, $n$) fall out, and conjugate updating *is* adding those statistics to the prior's.
- Two Gaussian exponents multiply by completing the square: precisions add, the mean is their precision-weighted average.
- $\sum(x_i-\mu)^2 = n(\bar x-\mu)^2 + \sum(x_i-\bar x)^2$ — the vertex is $\bar x$, the floor is the scatter $S$; every least-squares and NIG variance update rides on it.
- A marginal likelihood is a ratio of Beta/Gamma functions ($\int\text{kernel}=1/\text{constant}$); compute it in logs via `betaln`, never as factorials.
- Verify every read-off against the named density or a brute-force grid — guilty until it reproduces a known answer.
</content>
</invoke>

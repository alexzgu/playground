# P5. Bounds, tails, and approximations

> **Spine.** A bound's direction is set by one sign (the second derivative), a tail's tightness by how much you know (Markov → Chebyshev → Ville), and a "≈ Gaussian" always comes from a second-order Taylor expansion — memorize the mechanisms, not the results.
> **Which line?** Support skills for all four lines: Jensen underwrites every ELBO and assurance (prediction/decision), the tail family bounds error rates (audit), Taylor-to-2nd-order builds Laplace and the delta method (conditioning when the integral is intractable).
> **Promise.** After this module you can call the direction of a Jensen bound before looking it up, predict multiple-looks Type-I inflation from a union bound *before* simulating, and derive the Laplace/delta-method Gaussian from a curvature.
> **Prereqs.** P0; leans on P2 (expectation) and P3 (curvature = precision). **Runtime.** ~7 s.
> **Sources.** Bridges to modules 03/13 (ELBO, Laplace), 22/23 (regret, optional stopping), C-B §3.6 (Chebyshev), booklet ch. 3 (Laplace). Wall quotes cite `module:line` from the mining files.

A "clearly the ELBO is a lower bound," a "roughly 4× at ten looks," a "for large $n$ this is Gaussian" — each is a one-line move an expert makes without slowing down, and each has a mechanical trigger. This module installs the triggers. Every skill is staged **Reflex** (the automatic move) → **The wall** (a real course line that silently uses it) → **The fix** (runnable); the GATEs and the marquee add a committed **Predict**, and the end-exercises drill the rest.

## P5.1 Which way does Jensen go?  *(GATE)*

**Reflex.** For a **convex** $g$ ($g''>0$), $\mathbb{E}[g(X)]\ge g(\mathbb{E}[X])$; for **concave** ($g''<0$), the inequality flips. You never memorize the direction — you read it off the second-derivative sign. Anchor pair: $x^2$ (convex, $\mathbb{E}[X^2]\ge\mathbb{E}[X]^2$, always true) and $\log$ (concave, $\mathbb{E}[\log X]\le\log\mathbb{E}[X]$).

**The wall.** Three course results are *the same convexity check*, and reading them wrong stalls whole sections:
- ELBO: "By Jensen's inequality, `log E_q[p/q] ≥ E_q[log p/q]`, giving the ELBO as a lower bound" (`13:54`). $\log$ concave ⇒ the average of the log sits *below* the log of the average ⇒ ELBO is a **lower** bound, so maximizing it is safe.
- Assurance: "Averaging a concave function pulls you below its value at the mean (Jensen)" (`23:154`) — assurance $=\mathbb{E}_\delta[\text{power}(\delta)]<\text{power}(\mathbb{E}[\delta])$ on the concave shoulder of the S-curve.
- EIG: "`H(E_θ[p(y)]) − E_θ[H(p(y))]` ≥ 0" (`23:412`) — expected information gain is Jensen on the concave entropy $H$, which is *why* it can never be negative.

**The fix.** Feed four functions through one loop; the arrow that comes out is dictated entirely by the sign of $g''$.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "P5-bounds-approximations"
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

```python
# Jensen's direction is the sign of g''. X ~ Gamma(2,1), so E[X] = 2 exactly.
X = rng.gamma(shape=2.0, scale=1.0, size=2_000_000)
mX = X.mean()
for name, g, sign in [("x**2   (convex)", lambda x: x**2, "+"),
                      ("1/x    (convex)", lambda x: 1.0 / x, "+"),
                      ("log x  (concave)", np.log, "-"),
                      ("sqrt x (concave)", np.sqrt, "-")]:
    lhs = g(X).mean()     # E[g(X)]
    rhs = g(mX)           # g(E[X])
    arrow = ">=" if lhs > rhs else "<="
    print(f"{name:16s} g''{sign}:  E[g(X)]={lhs:8.4f} {arrow} g(E[X])={rhs:8.4f}")
```

The two convex rows print `>=`, the two concave rows `<=` — the arrow tracks the sign column, nothing else. Note the `1/x` row: `E[1/X]` prints around `1.0008` while `1/E[X]` is `0.5000`, the exact P2 reciprocal trap, now seen as a *special case of Jensen* (reciprocal is convex on $(0,\infty)$). The mechanical rule — **second-derivative sign → inequality direction** — settles ELBO, assurance, and EIG with no further thought.

**Drill.**
*Predict:* Is $\mathbb{E}[\sqrt{X}]$ larger or smaller than $\sqrt{\mathbb{E}[X]}$?
*Reason:* $\sqrt{\cdot}$ has $g''=-\tfrac14 x^{-3/2}<0$, so it is concave.
*Run:* the `sqrt x` row above. *Reconcile:* concave ⇒ `<=`; the printed `E[√X]` sits below `√E[X]`. A plug-in estimate $\sqrt{\hat\mu}$ therefore *overstates* $\mathbb{E}[\sqrt X]$ — the same bias that makes `E[σ(a)] ≠ σ(E[a])` a real error in module 15's logistic mean (`15:240`).

## P5.2 Markov, Chebyshev, Ville — one family

**Reflex.** Every tail bound is one engine, **$P(Z\ge a)\le \mathbb{E}[Z]/a$ for $Z\ge 0$**, fed a different nonnegative $Z$. Markov feeds it $|X|$ (mean only, weak). Chebyshev feeds it $(X-\mu)^2$ (variance, $1/k^2$). Chernoff feeds it $e^{tX}$ (MGF, exponential). Ville is the same inequality for the *running maximum* of a nonnegative martingale. Climb the ladder as you know more; each rung buys tightness for an assumption.

**The wall.** "Ville's inequality caps ... `P(sup_n BF10 ≥ k) ≤ 1/k`" (`23:316`). A Bayes factor under a true null is a nonnegative martingale with mean 1, so Markov-for-martingales bounds the chance of *ever* manufacturing strong evidence against a true null — the anti-p-hacking guarantee.

**The fix.** Bound $P(|X|\ge 3)$ for $X\sim N(0,1)$ three ways, then watch Ville hold in simulation.

```python
k = 3.0
E_absX = np.sqrt(2 / np.pi)                # E|X| for a standard normal
markov = E_absX / k                        # Markov on |X|
cheb   = 1.0 / k**2                        # Chebyshev: (X-mu)^2, gives 1/k^2
chern  = np.exp(-k**2 / 2)                 # Chernoff / sub-Gaussian tail
truth  = 2 * stats.norm.sf(k)             # exact P(|X| >= 3)
print(f"P(|X|>=3):  Markov {markov:.4f} >= Chebyshev {cheb:.4f} "
      f">= Chernoff {chern:.4f} >= truth {truth:.5f}")
```

The bounds nest: Markov `0.2660` ≥ Chebyshev `0.1111` ≥ Chernoff `0.0111` ≥ the truth `0.00270`, each rung tighter because it uses more of the distribution. Now Ville, on the exact BF martingale from module 23 — this doubles as a *verify-against-known-value* check (the course reports `0.0598`).

```python
# Ville: BF10 under a true null is a nonnegative martingale with mean 1.
g = np.random.default_rng(0)
reps, N, tau2 = 20000, 1000, 1.0
y = g.normal(0.0, 1.0, (reps, N))          # true null: mu = 0
S1 = np.cumsum(y, axis=1); ns = np.arange(1, N + 1)
logBF = 0.5 * (tau2 * S1**2 / (1 + ns * tau2) - np.log(1 + ns * tau2))
supBF = np.exp(logBF).max(axis=1)          # running maximum over all looks
print(f"P(sup BF10 >= 10 | H0) = {(supBF >= 10).mean():.4f}   (Ville bound 1/10 = 0.1000)")
```

The simulated `0.0598` sits under the Ville ceiling `0.1000`: you cannot peek your way to fake evidence against a true null. Same engine, four costumes.

## P5.3 The union bound — multiple-looks Type-I inflation  *(MARQUEE)*

**Reflex.** $P\!\left(\bigcup_i A_i\right)\le\sum_i P(A_i)$ — your default first bound when chances pile up, loose but *always valid, no independence needed*. When you test the same null at $k$ interim looks, "reject at some look" is a union of $k$ events each of size $\alpha$, so the family-wise error is at most $k\alpha$.

**The wall.** "every look is another chance to cross the line" (`23:250`); "'ever cross 1.96' is a much larger event than 'cross at one fixed look'" (`EXAM:180`).

**Setup.** A true null ($\theta=0.5$ coin), up to $k$ equally spaced interim looks out to $N=1000$; reject if the two-sided $z$ ever exceeds 1.96.

**Predict.** The union bound says the ten-look Type-I rate is *at most* $10\times 0.05 = 0.50$. Is the *simulated* rate at ten looks about (a) still 0.05, (b) ~0.10, (c) ~0.20, or (d) ~0.35? Commit before running.

*Reason:* the naive reflex says "each test is 5%, so it stays 5%" — that treats the looks as one event. The union bound already tells you the ceiling is 10× higher; the truth is between the single-look floor and that ceiling.

```python
g = np.random.default_rng(0)
reps, N = 20000, 1000
ns = np.arange(1, N + 1, dtype=np.float32)
cum = np.cumsum(g.random((reps, N)) < 0.5, axis=1, dtype=np.float32)   # Bernoulli(0.5)
zstat = np.abs(cum / ns - 0.5) / np.sqrt(0.25 / ns)                    # running |z|
del cum
zc = stats.norm.ppf(0.975)                                            # 1.96, two-sided 5%

def typeI(k):
    looks = np.linspace(N / k, N, k).astype(int)
    return float((zstat[:, looks - 1] > zc).any(axis=1).mean())

t1, t10 = typeI(1), typeI(10)
t_cont = float((zstat[:, 9:] > zc).any(axis=1).mean())   # a look after every trial
print(f"single look        : {t1:.4f}   (union bound  1*0.05 = 0.05)")
print(f"ten looks          : {t10:.4f}   (union bound 10*0.05 = 0.50)")
print(f"continuous monitor : {t_cont:.4f}")
```

**Reconcile.** Single look `0.0522` — nominal, as it must be. Ten looks `0.2044`: roughly a fourfold inflation, comfortably *under* the union bound `0.50` (the bound is valid but loose, because the ten events overlap heavily — a chain that crosses early tends to cross again). Continuous monitoring gives `0.4664`, and by the law of the iterated logarithm this climbs toward 1 as $N\to\infty$: peek forever at a true null and you are *guaranteed* to reject it. The lesson the union bound teaches before any simulation: **a $p<0.05$ is meaningless without the number of looks attached.** The naive "each test is 5% so the whole thing is 5%" collapses a union into a single event.

## P5.4 Triangle inequality in its working forms

**Reflex.** $|a+b|\le|a|+|b|$, and its everyday consequences: "within $\varepsilon$ of $A$, and $A$ within $\delta$ of $B$ ⇒ within $\varepsilon+\delta$ of $B$," and any *distance* (Euclidean, total variation) obeys $d(P,R)\le d(P,Q)+d(Q,R)$. You reach for it to chain approximations and to bound a two-step error by the sum of the steps.

**The wall.** "the total-variation gap shrinks ... the classic O(1/√n)" (`EXAM:219`) states the Bernstein–von Mises *rate*; the triangle itself lives in its **proof**, which bounds $\mathrm{TV}(\text{posterior},N)\le\mathrm{TV}(\text{posterior},N_1)+\mathrm{TV}(N_1,N)$ through an intermediate Gaussian $N_1$ — the cited homework line only summarizes that result.

**The fix.** Total variation between Bernoullis is $\mathrm{TV}=|p-q|$; check the triangle on three of them.

```python
tv = lambda p, q: abs(p - q)                 # TV distance between Bernoulli(p), Bernoulli(q)
P, Q, R = 0.2, 0.5, 0.9
print(f"TV(P,R)={tv(P, R):.2f}  <=  TV(P,Q)+TV(Q,R)={tv(P, Q) + tv(Q, R):.2f}")
```

Here `0.70 <= 0.70` with equality — $Q$ lies "on the segment" between $P$ and $R$, the collinear case where the triangle is tight. Move $Q$ off that line (say $Q=0.1$) and the right side strictly exceeds the left: the detour costs you. Chaining approximations is exactly this — each hop adds, so you keep the hops few and small.

## P5.5 The $1/\sqrt{n}$ reflex

**Reflex.** The standard error of a mean is $\sigma/\sqrt{n}$: **quadruple the data, halve the error.** A *difference* of two means has SE $\sqrt{2\sigma^2/n}$. A Monte-Carlo estimate over $M$ draws has error $\propto 1/\sqrt{M}$, so cutting it 10× costs $100\times$ the draws. When $n=100$, a mean is good to about $\pm 10\%$ of a standard deviation.

**The wall.** "`se = np.sqrt(2 * sd_obs ** 2 / n_plan)` — SE of the difference in means" (`EXAM:669`); "precision improves only as √M: 10× costs 100×" (`09:79`).

**The fix.**

```python
g = np.random.default_rng(1)
sigma = 3.0
for n in (25, 100, 400):
    xbar = g.normal(0.0, sigma, size=(20000, n)).mean(axis=1)
    print(f"n={n:3d}:  SD[xbar]={xbar.std():.4f}   sigma/sqrt(n)={sigma / np.sqrt(n):.4f}")
n = 100
diff = g.normal(0, sigma, (20000, n)).mean(1) - g.normal(0, sigma, (20000, n)).mean(1)
print(f"difference of two means (n={n}): SD={diff.std():.4f}  sqrt(2*sigma^2/n)={np.sqrt(2 * sigma**2 / n):.4f}")
```

The three SDs halve as $n$ quadruples (`0.6018`, `0.3006`, `0.1492`), tracking $\sigma/\sqrt n$. The difference has SD `0.4219`, matching $\sqrt{2\sigma^2/n}=$ `0.4243` — the extra $\sqrt2$ that a paired-vs-two-sample confusion silently drops.

## P5.6 Taylor to second order — where Laplace and the delta method come from  *(GATE)*

**Reflex.** Every "for large $n$, approximately Gaussian" is a **second-order Taylor expansion of a log-density at its mode**. Two moves do all the work: (1) at a mode the first-derivative term vanishes, so the expansion *starts* at the quadratic; (2) $\exp(-\tfrac12 a(\theta-\hat\theta)^2)$ is a Gaussian kernel with variance $1/a$. Hence Laplace: variance $=1/(\text{negative curvature at the mode})$ — the P3 identity *curvature = precision*. The delta method is the same tool one order down: $\mathrm{Var}[g(X)]\approx g'(\mu)^2\,\mathrm{Var}[X]$.

**The wall.** "second-order Taylor expansion of log p(θ|x) around its peak" ⇒ "`Σ⁻¹ = −∇²log p`" (`13:123`); the central-difference Hessian `H = (neg_log_g(phi_star + h) - 2*neg_log_g(phi_star) + neg_log_g(phi_star - h)) / h**2` (`EXAM:239`).

**The fix — Laplace from curvature.** Approximate a Gamma(3,1) posterior near its mode.

```python
# log p(theta) = 2 log theta - theta + c  (Gamma shape 3).  Mode: 2/theta - 1 = 0 -> 2.
th_star = 2.0
curv = 2.0 / th_star**2                     # -d2/dtheta2 log p = 2/theta^2 at the mode
lap_var = 1.0 / curv                        # Laplace variance = 1 / curvature
print(f"mode={th_star:.1f}  curvature={curv:.4f}  Laplace ~ N({th_star:.1f}, {lap_var:.1f})")
print(f"true Gamma(3,1): mean=3.0 var=3.0   (crude at shape 3, exact-in-form, sharpens with n)")
```

Laplace reports `N(2.0, 2.0)`: it centers on the *mode* (2), not the mean (3), and gets the scale from one second derivative. **The fix — you rarely have that derivative in closed form.** The central second difference recovers it:

```python
neg_log_p = lambda th: -(2 * np.log(th) - th)     # -log kernel
h = 1e-4
H_num = (neg_log_p(th_star + h) - 2 * neg_log_p(th_star) + neg_log_p(th_star - h)) / h**2
print(f"central-difference Hessian = {H_num:.4f}   vs analytic curvature {curv:.4f}")
```

`0.5000` either way — three function evaluations replace a hand derivation, which is exactly how module 13's Laplace evidence is computed. **The fix — delta method and the small-$x$ reflexes.**

```python
g = np.random.default_rng(2)
Xs = g.normal(10.0, 1.0, 1_000_000)          # X ~ N(10, 1);  g(X) = log X, g'(10)=0.1
print(f"Var[log X]:  delta {0.1**2 * 1.0:.4f}   simulated {np.log(Xs).var():.4f}")
m = 1000                                      # log(1+x) ~ x  =>  (1+1/m)^m -> e
print(f"(1+1/m)^m at m={m}: {(1 + 1/m)**m:.4f}   e = {np.e:.4f}")
```

The delta method nails $\mathrm{Var}[\log X]$: predicted `0.0100`, simulated `0.0103`. And $\log(1+x)\approx x$ turns $(1+1/m)^m$ into $\exp(m\cdot\tfrac1m)=e$: printed `2.7169` against `2.7183`. The reflexes $e^x\approx 1+x$ and $\log(1+x)\approx x-\tfrac{x^2}{2}$ linearize log-likelihood ratios on sight.

## P5.7 Growth-rate literacy

**Reflex.** Rank the shapes on sight: $\log t \ll \sqrt t \ll t$. UCB regret grows like $\log t$; a well-tuned bandit like $\sqrt t$; $\varepsilon$-greedy with *constant* $\varepsilon$ suffers **linear** regret (it never stops exploring). The law of the iterated logarithm's $\sqrt{2t\log\log t}$ is barely above $\sqrt t$ — the $\log\log$ grows so slowly it is almost a constant.

**The wall.** "regret grows linearly ... while others flatten toward logarithmic" (`22:251`); "by the law of the iterated logarithm this diverges toward 1" (`23:289`).

**The fix.**

```python
t = np.arange(16, 10001)          # start past e^e so log(log(t)) > 0 (the LIL term)
fig, ax = plt.subplots()
ax.plot(t, np.log(t), label="log t  (UCB regret)")
ax.plot(t, np.sqrt(t), label="sqrt t")
ax.plot(t, np.sqrt(2 * t * np.log(np.log(t))), label="sqrt(2 t loglog t)  (LIL)")
ax.plot(t, 0.02 * t, label="0.02 t  (eps-greedy, const eps)")
ax.set(xlabel="steps t", ylabel="cumulative regret",
       title="Growth rates: log t << sqrt t << linear t")
ax.legend()
save(fig, "growth_rates")
print(f"at t=1e4:  log t={np.log(1e4):.2f}   sqrt t={np.sqrt(1e4):.2f}   0.02 t={0.02 * 1e4:.2f}")
```

![Cumulative regret vs steps for four growth rates on a linear axis: log t stays near the floor, sqrt t and the LIL curve rise slowly and nearly together, constant-eps linear regret shoots up.](figures/P5-bounds-approximations/growth_rates.png)

At $t=10^4$: $\log t=$ `9.21`, $\sqrt t=$ `100.00`, linear $=$ `200.00` — an order of magnitude separates each rung. The figure's punchline: the constant-$\varepsilon$ line escapes the frame while the log curve hugs the floor. *Which asymptotic order* a procedure lives in decides the whole ranking; the constants are a rounding error next to it.

## Pitfalls

- **Guessing Jensen's direction from the result you want.** Always read $g''$. Convex up (bowl) ⇒ $\mathbb{E}[g]\ge g(\mathbb{E})$; concave down (dome) ⇒ flipped. The ELBO is a *lower* bound precisely because $\log$ is a dome.
- **Treating a union bound as an equality.** $k\alpha$ is a *ceiling*, often loose (0.50 vs the simulated 0.20 at ten looks) because the events overlap. It is still the right first move — and it never needs independence.
- **Dropping the $\sqrt2$ in a difference of means.** Two independent means give SE $\sqrt{2\sigma^2/n}$, not $\sigma/\sqrt n$. Halving MC error costs $4\times$, not $2\times$, the draws.
- **Confusing the Laplace mode with the mean.** Laplace centers on the *mode*; for a skewed posterior that is not the mean (Gamma(3,1): mode 2, mean 3). It sharpens as $n$ grows (BvM).
- **Keeping too few or too many Taylor terms.** A *mean* correction needs first order; a *variance* needs the first-order term of the deviation ($g'(\mu)^2\mathrm{Var}$). The mode expansion needs second order because the first-order term is zero there.

## Exercises

**Exercise P5.1 — The reciprocal's revenge.**
*Setup:* Server latency $X\sim\text{Gamma}(2,1)$ (shape 2, rate 1, mean 2). You care about *throughput* $1/X$ and estimate it by $1/\bar X$ from a large sample.
*Predict:* Is $\mathbb{E}[1/X]$ above or below $1/\mathbb{E}[X]=0.5$, and by roughly how much?
*Reason:* $1/x$ is convex, so Jensen points one way; the size of the gap is the surprise.
*Run:* read the `1/x` row of the P5.1 fix.
<details><summary>Reconcile</summary>

$\mathbb{E}[1/X]$ prints ≈ `1.0008` — *double* the plug-in `0.5000`. Analytically $\mathbb{E}[1/X]=1/(\text{shape}-1)=1$ for a Gamma. Convexity guarantees $\mathbb{E}[1/X]\ge 1/\mathbb{E}[X]$; here the gap is 100%, not a rounding error, because $1/x$ curves hard near 0 where a Gamma(2,1) still has mass. Plug-in throughput is not just biased — it is off by a factor of two. This is the P2 trap re-derived as a one-line Jensen consequence.
</details>

**Exercise P5.2 — Predict the peeking penalty at 5 looks.**
*Setup:* Same optional-stopping simulation as the marquee, but $k=5$ equally spaced looks.
*Predict:* The union bound caps five-look Type-I at $5\times0.05=0.25$. Will the *simulated* rate be closer to 0.10, 0.16, or the 0.25 ceiling?
*Reason:* the ten-look rate (0.20) was well under its 0.50 ceiling because looks overlap; five looks overlap too.
*Run:*
```python
print(f"five looks: {typeI(5):.4f}   (union bound 5*0.05 = 0.25)")
```
<details><summary>Reconcile</summary>

Five looks give `0.1457` — again far under the `0.25` union ceiling, and between the single-look 0.05 and the ten-look 0.20. The bound scales linearly in $k$; the truth grows *sublinearly* because each new look is highly correlated with the last. The union bound is the right predictor of the *shape* (more looks ⇒ more inflation, unbounded) even though it overstates the *level*.
</details>

**Exercise P5.3 — Delta method on a sigmoid (ML connection).**
*Setup:* A logit $a\sim N(0,\,0.5^2)$; you report the probability $\sigma(a)=1/(1+e^{-a})$. The plug-in is $\sigma(\mathbb{E}[a])=\sigma(0)=0.5$.
*Predict:* Is $\mathbb{E}[\sigma(a)]$ above, below, or exactly 0.5? And what does the delta method give for $\mathrm{Var}[\sigma(a)]$?
*Reason:* $\sigma$ is convex for $a<0$ and concave for $a>0$; at the symmetric point $a=0$ the two curvatures cancel — a case where Jensen has *no* net direction.
*Run:*
```python
gg = np.random.default_rng(7)
a = gg.normal(0.0, 0.5, 1_000_000)
sa = 1 / (1 + np.exp(-a))
sig0 = 0.5; dsig = sig0 * (1 - sig0)                 # sigma'(0) = 0.25
print(f"E[sigma(a)]={sa.mean():.4f} (plug-in 0.5000)  Var: delta {dsig**2 * 0.25:.5f} sim {sa.var():.5f}")
```
<details><summary>Reconcile</summary>

$\mathbb{E}[\sigma(a)]$ prints ≈ `0.5000` — the mean is *unbiased* here because $\sigma$ is antisymmetric about $a=0$, so the convex and concave halves cancel exactly. Jensen's direction only bites off-center (as in module 15's `E[σ(a)] ≠ σ(E[a])` when the logit mean is nonzero). The variance, though, is real: delta gives `0.01562`, simulation `0.01395` — the linear term $\sigma'(0)^2\mathrm{Var}[a]$ captures the spread even where the mean shift is zero. Lesson: first-order (variance) and Jensen (mean-shift) are *separate* corrections; one can vanish while the other does not.
</details>

## Where the course uses this

| Skill | Reflex | Course walls (`module:line`) |
|---|---|---|
| Jensen direction (2nd-deriv sign) | convex ⇒ E[g]≥g(E); concave flips | ELBO `13:54`, `03:234`; assurance `23:154`; EIG `23:412`; sigmoid mean `15:240`; WAIC gap `17:262` |
| Markov/Chebyshev/Ville family | one engine $P(Z\ge a)\le \mathbb{E}Z/a$ | Ville BF cap `23:316`, verify `23:327`; two-sided tail `18:120`; ESS weight-variance `21:337` |
| Union bound | $P(\cup A_i)\le\sum P(A_i)$, loose but valid | multiple-looks Type-I `23:265`, `EXAM:180`; UCB radius `22:220` |
| Triangle / TV chaining | $d(P,R)\le d(P,Q)+d(Q,R)$ | BvM TV gap `EXAM:219`, `EXAM:257` |
| $1/\sqrt n$ reasoning | quadruple data, halve error; diff has $\sqrt{2\sigma^2/n}$ | SE of difference `EXAM:669`; MC error `09:79`; width shrink `04:71`; SE of mean `17:302` |
| Taylor to 2nd order | mode ⇒ quadratic ⇒ Gaussian; delta = 1st order | Laplace `13:123`, `13:127`; central-diff Hessian `EXAM:239`; Laplace evidence `EXAM:240`; delta method `Ch1to5:4766` |
| Growth-rate literacy | $\log t\ll\sqrt t\ll t$; LIL $\sqrt{2t\log\log t}$ | regret shapes `22:251`, `22:266`; LIL `23:289`, `23:288` |

## Takeaways

- **Jensen's direction is a sign, not a memory.** Convex ($g''>0$): $\mathbb{E}[g]\ge g(\mathbb{E})$. Concave: flipped. ELBO is a lower bound because $\log$ is concave; assurance $<$ power and EIG $\ge 0$ for the same reason.
- **Markov, Chebyshev, Chernoff, Ville are one inequality** — $P(Z\ge a)\le\mathbb{E}[Z]/a$ — fed a nonnegative variable, a squared deviation, an MGF, or a martingale's running max. More assumptions buy a tighter rung.
- **The union bound is your first, always-valid, independence-free ceiling.** It predicted multiple-looks inflation ($\le 0.50$ at ten looks) before any simulation; the truth (0.20) is lower only because the events overlap.
- **$1/\sqrt n$ is the default rate.** SE of a mean $=\sigma/\sqrt n$; of a difference $=\sqrt{2\sigma^2/n}$; MC error $\propto 1/\sqrt M$, so 10× precision costs 100× draws.
- **Every "≈ Gaussian" is a second-order Taylor expansion at a mode**, with variance = 1/curvature (Laplace); the delta method is the same tool at first order; when you lack the derivative, the central second difference recovers the Hessian in three evaluations.
- **Asymptotic order beats constants.** $\log t\ll\sqrt t\ll t$ decides which bandit wins; the LIL's $\sqrt{2t\log\log t}$ is why continuous peeking eventually rejects any true null.

# P2. Expectation as a Tool

> **Spine.** $\mathbb{E}[\cdot]$ is a linear operator you *push around* — through sums (no independence needed), into and out of conditioning, and against a density via LOTUS — but it never passes through a nonlinear $g$; and the single most common move in the whole course is reading a probability as `mean(boolean_array)`.
> **Which line?** Lines 3 and 4: every posterior-predictive integral and every expected-loss decision is an $\mathbb{E}$ you estimate as a mean of an array.
> **Promise.** After this you read `np.mean(tB > tA)`, `x.var(axis=0)`, and `np.mean(np.maximum(tA - tB, 0.0))` as fluent statements about expectations, not opaque numpy — and you never again cancel an $\mathbb{E}$ through a reciprocal or a `max`.
> **Prereqs.** P1 (density algebra) helps but is not required. **Runtime.** ~4 s.
> **Sources.** `research/expert-symbolic.md` area (ii); walls from course modules 00, 05, 08, 15, 16, 17, 18, 22.

Students treat $\mathbb{E}[\cdot]$ as "the average — a number you compute at the end." Experts treat it as an operator with three reflexes: it is **linear** (splits any sum, correlated or not), it **commutes with conditioning** (the tower rule), and it is **the integral of $g$ against a density** (LOTUS) — which is why a Monte-Carlo mean estimates it and why it does *not* pass through a nonlinear function.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "P2-expectation-operator"         # this module's figure dir
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

## P2.1 The marquee identity: $P(A) = \mathbb{E}[\mathbf{1}\{A\}] = $ `mean(boolean_array)`

**Reflex.** Any probability is the expectation of an indicator, and any expectation of an indicator over draws is the *mean of a boolean array*. The instant you can write an event as a condition on samples, its probability is `.mean()` of that condition — no combinatorics, no joint distribution.

$$P(A) = \mathbb{E}\big[\mathbf{1}\{A\}\big], \qquad \mathbf{1}\{A\} = \texttt{(condition).astype(int)}, \qquad \widehat{P(A)} = \texttt{condition.mean()}.$$

**The wall.** This is the most-used unstated identity in the course — 22 silent uses in modules 00–13, 26 in 14–26. It wears a dozen costumes and never announces itself:

> `cover = ((lo <= theta0) & (theta0 <= hi)).mean()`  — module 08:343 (frequentist coverage)
> `p_B_beats_A = np.mean(tB > tA)`  — module 22:105 (which arm is better)
> `empirical acceptance = accept.mean()`  — module 09:293 (rejection-sampler acceptance)
> `np.mean(p0 < 0.05)`  — module 17:335 (Type-I error by simulation)

Coverage frequency, posterior probability, acceptance rate, Type-I error, PPC p-value, bandit lock-in probability — **all the same line**: build a boolean, take its mean. A reader who does not see the identity reads four unrelated tricks; a reader who does sees one.

**The fix.** One array, three questions, three means of booleans — each is a probability.

```python
z = rng.standard_normal(200_000)
p_tail  = (z > 1.96).mean()               # P(Z > 1.96)      indicator mean
p_band  = (np.abs(z) < 1).mean()          # P(|Z| < 1)       indicator mean
# joint posterior draws from module 05's A/B test (Beta(42,960) vs Beta(58,944))
tA = rng.beta(42, 960, 200_000)
tB = rng.beta(58, 944, 200_000)
p_B_better = (tB > tA).mean()             # P(theta_B > theta_A) over the JOINT
print(f"P(Z>1.96)        = {p_tail:.4f}   (analytic 0.0250)")
print(f"P(|Z|<1)         = {p_band:.4f}   (analytic 0.6827)")
print(f"P(theta_B>theta_A) = {p_B_better:.4f}")
```

Prints `P(Z>1.96) = 0.0251`, `P(|Z|<1) = 0.6820`, and `P(theta_B>theta_A) = 0.9503`. The last one is module 05's headline result reproduced in a single `.mean()` of a boolean built from *paired* draws — nothing about the two arms being dependent under the joint changes the recipe.

**Drill P2.1 — expected fixed points.**
*Setup:* Shuffle $n$ cards labeled $1..n$; a "fixed point" is a card landing in its own slot. Let $I_j = \mathbf{1}\{\text{card } j \text{ fixed}\}$, so the count is $\sum_j I_j$.
*Predict:* The expected number of fixed points for $n=5$, and for $n=500$. More cards, more chances to collide — does the expectation grow with $n$?
*Reason:* "More slots, more coincidences" — the naive additive-opportunity intuition.
*Run:*
```python
def mean_fixed(n, reps=20_000):
    perms = np.array([rng.permutation(n) for _ in range(reps)])
    return (perms == np.arange(n)).sum(1).mean()   # sum of indicators, then mean
print(f"E[#fixed] n=5   : {mean_fixed(5):.3f}")
print(f"E[#fixed] n=500 : {mean_fixed(500):.3f}")
```
<details><summary>Reconcile</summary>

Both print $\approx$ `1.000` (`1.008` and `1.000` here). By linearity — which needs no independence, and the $I_j$ are dependent — $\mathbb{E}[\sum_j I_j] = \sum_j P(I_j=1) = \sum_j \tfrac{1}{n} = 1$ for *every* $n$. The extra slots exactly cancel the smaller per-slot probability. The identity $P(A)=\mathbb{E}[\mathbf{1}\{A\}]$ turned a nasty derangement-counting problem into a one-line sum. This is the engine behind "expected occupancy," "effective number of clusters" (module 19:306), and every expected count in the course.
</details>

## P2.2 Linearity splits any sum — dependence is irrelevant

**Reflex.** $\mathbb{E}[aX + bY + c] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y] + c$, *always*. You split expectations of sums without a glance at whether the terms are independent. (What *does* need independence is factoring a **product**: $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$ only when $X\perp Y$.)

**The wall.** Cumulative regret in the bandit tournament is a sum of *dependent* per-pull gaps — each pull's arm depends on all previous rewards — yet the course sums their expectations term by term:

> `inst[t] = np.mean(best_rate - rates[arm]); ... np.cumsum(inst)`  — module 22:225

That `cumsum` is $\mathbb{E}[\sum_t \Delta_t] = \sum_t \mathbb{E}[\Delta_t]$ with no independence assumption anywhere. The same move powers the average treatment effect: $\text{ATE} = \mathbb{E}[Y_1 - Y_0] = \mathbb{E}[Y_1] - \mathbb{E}[Y_0]$, valid even though a unit's treated and control potential outcomes are as correlated as can be.

**The fix.** Take the maximally-dependent case $Y=X$ and watch linearity survive while product-factoring dies.

```python
X = rng.integers(0, 2, 500_000).astype(float)     # Bernoulli(0.5)
Y = X.copy()                                       # perfectly dependent: Y = X
lin_gap = (X + Y).mean() - (X.mean() + Y.mean())   # linearity: must be ~0
prod_gap = (X * Y).mean() - X.mean() * Y.mean()    # factoring: must FAIL
# ATE with strongly correlated potential outcomes
Y0 = rng.normal(10, 2, 500_000)
Y1 = Y0 + rng.normal(3, 0.5, 500_000)              # per-unit effect ~ N(3, .25)
ate_paired = (Y1 - Y0).mean()                      # mean of differences
ate_split  = Y1.mean() - Y0.mean()                 # difference of means
print(f"linearity gap E[X+Y]-(E[X]+E[Y]) = {lin_gap:.2e}")
print(f"product gap   E[XY]-E[X]E[Y]     = {prod_gap:.4f}  (=Var X, NOT 0)")
print(f"ATE mean-of-diffs = {ate_paired:.4f} , diff-of-means = {ate_split:.4f}")
```

Prints `linearity gap = 0.00e+00`, `product gap = 0.2500` (exactly $\text{Var}(X)=\tfrac14$), and the two ATE routes agreeing at `3.0009` / `3.0009`. Sums are free; products cost you an independence assumption. Forgetting which is which is how people "need to model the dependence first" when they simply do not.

## P2.3 LOTUS: $\mathbb{E}[g(\theta)]$ is the mean of `g(draws)`

**Reflex.** To get $\mathbb{E}[g(\theta)]$ you integrate $g$ against $\theta$'s density — the Law Of The Unconscious Statistician — and with posterior *draws* that integral is estimated by `g(draws).mean()`. This is line 3 of the course (prediction = marginalization) whenever the integral has no closed form.

$$\mathbb{E}_{\theta\mid y}[g(\theta)] = \int g(\theta)\,p(\theta\mid y)\,d\theta \;\approx\; \frac{1}{S}\sum_{s=1}^{S} g(\theta^{(s)}), \qquad \theta^{(s)} \sim p(\theta\mid y).$$

**The wall.** The Bayesian logistic prediction integrates the sigmoid over the posterior — and the course writes it as one `np.mean`:

> `def mc_integrate(x): return np.mean(1 / (1 + np.exp(-draws @ x)))`  — module 15:253

That is $\int \sigma(x^\top\beta)\,p(\beta\mid \text{data})\,d\beta$, the honest posterior-predictive probability, done as the mean of $g(\beta^{(s)})$ over draws. When the draws come from the *wrong* distribution, you reweight — the **self-normalized** estimator $\hat{\mathbb{E}}_p[g] = \sum_s w_s\,g(\theta^{(s)}) / \sum_s w_s$ with $w_s = p(\theta^{(s)})/q(\theta^{(s)})$ — which the course uses for importance sampling and posterior-mean-by-quadrature (module 06:162).

**The fix.** Estimate $\mathbb{E}[\theta^2]$ under a Beta posterior two ways (analytic vs. MC mean of `draws**2`), then recover the *same* expectation from the *wrong* proposal via self-normalized weights.

```python
a, b = 58, 944                                     # module 05's arm-B posterior
draws = rng.beta(a, b, 300_000)
m = a / (a + b)                                     # E[theta]
v = a * b / ((a + b)**2 * (a + b + 1))              # Var[theta]
Esq_analytic = v + m**2                             # E[theta^2] = Var + mean^2 (LOTUS)
Esq_mc = (draws**2).mean()                          # mean of g(draws), g(t)=t^2
# self-normalized IS: target p = Gamma(2,1), proposal q = Exp(scale 2); estimate E_p[X]=2
xq = rng.exponential(scale=2.0, size=300_000)       # draws from the WRONG law q
w  = stats.gamma(a=2, scale=1).pdf(xq) / stats.expon(scale=2).pdf(xq)
E_p_x = np.sum(w * xq) / np.sum(w)                   # self-normalized weighted mean
print(f"E[theta^2] analytic = {Esq_analytic:.6f}")
print(f"E[theta^2] MC-mean  = {Esq_mc:.6f}")
print(f"E_p[X] via wrong-proposal weights = {E_p_x:.4f}  (truth 2.0)")
```

Analytic and MC agree at `0.003405` / `0.003403`, and the self-normalized estimate recovers `2.0022` from draws taken from the *wrong* distribution — though those self-normalized weights are *consistent but slightly biased* ($O(1/M)$ bias, real only at small $M$ or with heavy weights). That printed agreement is the point: `g(draws).mean()` is not an approximation you tolerate but the definition of the integral you wanted.

## P2.4 The tower rule, executed — not recited

**Reflex.** $\mathbb{E}[X] = \mathbb{E}\big[\mathbb{E}[X\mid Y]\big]$: condition on the convenient variable, take the *inner* expectation (treating $Y$ as a known constant, so anything not random in $X$ pulls out front), then average over $Y$. Reach for it the instant a model is defined hierarchically ("$X$ given $\lambda$ is Poisson, and $\lambda$ is random").

**The wall.** The eight-schools posterior mean differs from the plug-in blend precisely because the tower rule averages over the hyperparameter instead of fixing it:

> "the residual gap ... is precisely the effect of *marginalizing* $\tau$ rather than fixing it"  — module 16:220

Read as $\mathbb{E}[\theta_j] = \mathbb{E}_\tau\big[\mathbb{E}[\theta_j\mid\tau]\big]$: the two-layer average, not the inner layer at a point estimate. Most write-ups recite the slogan and then cannot execute it; the fix is to *run* both layers.

**The fix.** Poisson–Gamma by hand and by simulation. $X\mid\lambda \sim \text{Poisson}(\lambda)$, $\lambda\sim\text{Gamma}(2,1)$ (shape 2, rate 1, mean 2). Then $\mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X\mid\lambda]] = \mathbb{E}[\lambda] = 2$ — no sum over $x$ needed, just plug the inner mean $\mathbb{E}[X\mid\lambda]=\lambda$ and average.

```python
lam = rng.gamma(shape=2.0, scale=1.0, size=1_000_000)   # rate 1 -> scale 1; mean 2
X   = rng.poisson(lam)                                   # two-stage: draw lambda, then X
inner_then_outer = lam.mean()          # E[E[X|lam]] = E[lam], the tower shortcut
brute_force      = X.mean()            # the full E[X], as a check
print(f"tower  E[E[X|lam]] = E[lam] = {inner_then_outer:.4f}")
print(f"brute  E[X]                = {brute_force:.4f}")
```

Both print $\approx$ `2.00` (`2.0003` and `2.0004`). The tower rule bought the answer from the inner mean alone; the brute-force column merely confirms it. Keep `lam` and `X` around — the variance of this same two-stage draw is the next skill.

## P2.5 Law of total variance: the overdispersion engine

**Reflex.** Variance decomposes across a conditioning variable:

$$\text{Var}(X) = \underbrace{\mathbb{E}\big[\text{Var}(X\mid Y)\big]}_{\text{within / aleatoric}} + \underbrace{\text{Var}\big(\mathbb{E}[X\mid Y]\big)}_{\text{between / epistemic}}.$$

Total = average of the within-group variances **plus** the variance of the group means. This is *the* mechanism for overdispersion (a mixture is wider than any of its components) and for splitting predictive uncertainty into noise you can't reduce and knowledge you can.

**The wall.** Two course lines are this identity in disguise:

> `p_waic = ll_flat.var(axis=0)`  — module 17:263 (WAIC's effective-parameter penalty is the *between-draw* variance of the log-likelihood)
> `A_hat = max(np.mean(X**2) - 1.0, 0.0)`  — module 18:56 (empirical Bayes recovers the between-group variance as **total minus noise**: $\text{Var}[X]=A+1 \Rightarrow \hat A = \text{total} - 1$, clamped by `max(·,0)` since a variance estimate can't go negative when the total dips below the noise floor)

The second is the whole between-group estimation trick: you never observe the group means directly, so you get their variance by subtracting the known within-group noise from the total. That is $\text{Var}(\mathbb{E}[X\mid Y]) = \text{Var}(X) - \mathbb{E}[\text{Var}(X\mid Y)]$ solved for the between term.

**The fix.** Decompose the Poisson–Gamma variance from P2.4. Within: $\text{Var}(X\mid\lambda)=\lambda$, so $\mathbb{E}[\text{Var}(X\mid\lambda)]=\mathbb{E}[\lambda]=2$. Between: $\mathbb{E}[X\mid\lambda]=\lambda$, so $\text{Var}(\mathbb{E}[X\mid\lambda])=\text{Var}(\lambda)=2$. Total $=4$ — **twice** a plain Poisson's variance-equals-mean of 2. That excess is overdispersion.

```python
within  = lam.mean()               # E[Var(X|lam)] = E[lam]
between = lam.var()                # Var(E[X|lam]) = Var(lam)
total_decomp = within + between    # law of total variance
total_direct = X.var()             # the actual Var(X), as a check
overdisp = total_direct - X.mean() # excess over a Poisson (where Var=mean)
print(f"within  E[Var(X|lam)] = {within:.4f}")
print(f"between Var(E[X|lam]) = {between:.4f}")
print(f"total  = within+between = {total_decomp:.4f}   direct Var(X) = {total_direct:.4f}")
print(f"overdispersion Var(X)-E[X] = {overdisp:.4f}  (a pure Poisson would give 0)")
```

Within `2.00`, between `2.00`, total `4.0040` matching the direct `Var(X) = 4.0056`, and the overdispersion `2.00` is exactly the between-group variance. A Poisson mixed over a random rate is *always* wider than a Poisson — and the law of total variance says by exactly how much. This is why count data "always looks overdispersed": there is a latent rate you didn't condition on.

## P2.6 The trap: $\mathbb{E}[g(X)] \neq g(\mathbb{E}[X])$

**Reflex.** Expectation passes through a function *only if the function is linear*. For any curved $g$ you must integrate $g$ against the density (P2.3); you never substitute $\mathbb{E}[X]$ into $g$. And for convex $g$ you know the direction of the error — Jensen: $\mathbb{E}[g(X)]\ge g(\mathbb{E}[X])$ (P5's skill; here we just *feel* its size).

**The wall (the 81×-regret reveal).** The A/B decision's expected regret is $\mathbb{E}[\max(\theta_A-\theta_B,\,0)]$ — a max *inside* the expectation — and collapsing it to $\max(\mathbb{E}[\theta_A]-\mathbb{E}[\theta_B],\,0)$ throws the entire story away:

> `loss_ship_B = np.mean(np.maximum(tA - tB, 0.0))`  — module 05:374 / 22:106
> "a probability weighs *worlds*, a loss weighs *worlds × stakes* ... the regret ratio is `81`×, not the anchored 19-to-1"  — module 22:114

The naive read prices the decision by the *probability* $P(\theta_B>\theta_A)\approx0.95$ — 19-to-1 odds. The correct read prices it by the *expected max*, and gets $81\times$: being wrong in the 5% of worlds where A wins is nearly free (the arms are tied there), while shipping A when B is better forfeits a full point of conversion. The max cannot be pulled out of the expectation.

**Marquee — predict then reveal.** Before any code: $X\sim\text{Gamma}(2,1)$ (shape 2, rate 1), so $\mathbb{E}[X]=2$ and $1/\mathbb{E}[X]=0.5$. **Commit to a number for $\mathbb{E}[1/X]$.** Naive pass-through says $0.5$. Is it?

```python
alpha, beta = 2.0, 1.0                              # Gamma shape, RATE (scipy scale=1/rate)
EX = alpha / beta                                   # = 2
inv_EX = 1 / EX                                     # 1/E[X] = 0.5
E_invX_analytic = beta / (alpha - 1)                # E[1/X] = beta/(alpha-1) = 1  (>1/E[X])
g = rng.gamma(shape=alpha, scale=1/beta, size=2_000_000)
mc = 1 / g                                          # 1/X: Var[1/X] = infinite at alpha=2
batch = mc.reshape(20_000, -1).mean(1)             # 20k modest samples of 100 draws each
print(f"1/E[X]                 = {inv_EX:.4f}")
print(f"E[1/X] analytic        = {E_invX_analytic:.4f}   (factor {E_invX_analytic/inv_EX:.1f}x larger)")
print(f"E[1/X] MC (2e6 draws)  = {mc.mean():.4f}")
print(f"  single largest 1/X draw     = {mc.max():.0f}  ({mc.max()/mc.mean():.0f}x the mean)")
print(f"  worst of 20k size-100 batch = {batch.max():.2f}  (truth 1.0) <- one rare draw dominates it")
```

$\mathbb{E}[1/X] = $ `1.0000`, a full **`2.0`× larger** than the pass-through guess `0.5000`: the reciprocal is convex, so Jensen pushes the true value *up*, and the small-$X$ draws where $1/X$ explodes do the lifting. Those same draws hide a second hazard: at $\alpha=2$ the variance of $1/X$ is *infinite*. The mean over two million draws looks accurate, but that calm is a mirage — the single largest draw is `1138` (`1140`× the mean), and one of 20,000 size-100 batches lands at `12.42`. With no finite variance there is no trustworthy $1/\sqrt{M}$ error bar. Two lessons: nonlinear $g$ breaks pass-through, *and* the tool you'd use to measure the break has no honest error bar here.

![Distribution of 1/X for X~Gamma(2,1): the right tail drags E[1/X] far above 1/E[X].](figures/P2-expectation-operator/jensen_gap.png)

```python
fig, ax = plt.subplots()
ax.hist(mc[mc < 6], bins=120, density=True, color="C0", alpha=0.75)
ax.axvline(inv_EX, color="black", ls="--", lw=2, label=f"1/E[X] = {inv_EX:.2f} (naive)")
ax.axvline(E_invX_analytic, color="C3", lw=2, label=f"E[1/X] = {E_invX_analytic:.2f} (truth)")
ax.set(xlabel="1/X", ylabel="density",
       title="A convex transform: the heavy right tail lifts E[1/X] above 1/E[X]")
ax.legend()
save(fig, "jensen_gap")
```

The figure makes the mechanism visible: the bulk of $1/X$ sits below `0.5`, but a long right tail reaches far past `1`, and expectation is a *balance point* — that thin heavy tail is what $1/\mathbb{E}[X]$ cannot see. The same shape, in decision units:

```python
tA = rng.beta(42, 960, 1_000_000)                  # module 05 posteriors, joint draws
tB = rng.beta(58, 944, 1_000_000)
loss_ship_B = np.mean(np.maximum(tA - tB, 0.0))    # regret if you ship B and A was better
loss_ship_A = np.mean(np.maximum(tB - tA, 0.0))    # regret if you ship A and B was better
p_B_better  = np.mean(tB > tA)                      # the PROBABILITY (line 2)
print(f"P(B>A) = {p_B_better:.4f}  -> naive odds ratio {p_B_better/(1-p_B_better):.0f}:1")
print(f"regret ratio ship-A : ship-B = {loss_ship_A/loss_ship_B:.0f}x  (the DECISION, line 4)")
```

Prints `P(B>A) = 0.9507`, naive odds `19:1`, but regret ratio `81`× — the canonical reveal: $\mathbb{E}[\max(\cdot,0)]\neq\max(\mathbb{E}[\cdot],0)$, and that four-fold gap is line 4 refusing to collapse into line 2.

## Bridge — where this becomes the four lines

Line 3 (prediction) *is* LOTUS: $p(\tilde y\mid y)=\mathbb{E}_{\theta\mid y}[p(\tilde y\mid\theta)]$, computed as `p(y_new | draws).mean()` (module 15:253, 17:262). Line 4 (decision) *is* an expected loss $\mathbb{E}_{\theta\mid y}[L(a,\theta)]$, computed as `L(a, draws).mean()` and minimized over $a$ (module 22) — and P2.6 is why you average the loss over draws instead of plugging in a point estimate. The tower rule and law of total variance split predictive uncertainty into aleatoric and epistemic pieces (module 05) and let empirical Bayes recover a between-group variance it never directly observes (module 18). Every one is the operator $\mathbb{E}$ pushed around by the three reflexes above.

## Pitfalls

- **Collapsing $\mathbb{E}[g(\theta)]$ to $g(\mathbb{E}[\theta])$ for a curved $g$.** The plug-in prediction $\sigma(x^\top\hat\beta)$ is *not* $\mathbb{E}[\sigma(x^\top\beta)]$; the averaged probability is pulled toward $0.5$ (module 15:240). Same disease as $1/\mathbb{E}[X]$, same cure: average $g$ over draws.
- **Adding an independence assumption to split a sum.** Linearity never needs it. Conversely, *dropping* an independence check when factoring a product ($\mathbb{E}[XY]$) or when writing $\text{Var}(X+Y)=\text{Var}X+\text{Var}Y$ (the $2\text{Cov}$ term!) — that is where dependence actually bites.
- **Trusting a Monte-Carlo mean of a heavy-tailed transform.** $\mathbb{E}[1/X]$ at $\alpha=2$, importance weights with a too-light proposal, ratio estimators — the sample mean can have infinite variance. Print a batch-to-batch spread or an effective sample size before believing it.
- **Reciting the tower rule without executing it.** "$\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Y]]$" is useless until you pick the $Y$ to condition on and actually collapse the inner layer. Practice on hierarchical models until the two-stage simulation is automatic.
- **Reading a decision off a probability.** $P(B>A)=0.95$ does not mean the regret ratio is 19:1. A probability weighs worlds; a loss weighs worlds × stakes.

## Exercises

**Exercise P2.1 — the sigmoid you can't pull out (ML connection).**
*Setup:* A Bayesian logistic model gives a posterior on the logit $a = x^\top\beta$ that is $a\sim N(0, s^2)$ for a test point (so the *linear predictor* is centered at 0). You want the predicted class probability $\mathbb{E}[\sigma(a)]$ where $\sigma$ is the logistic sigmoid.
*Predict:* At $s=0$ the answer is $\sigma(0)=0.5$. As posterior uncertainty $s$ grows to $4$, does the predicted probability move *up*, *down*, or *stay at 0.5*?
*Reason:* Plug-in intuition: "the mean logit is 0, so the probability is $\sigma(0)=0.5$ regardless of $s$."
*Run:*
```python
for s in [0.0, 1.0, 4.0]:
    a = rng.normal(0.0, s, 500_000)
    print(f"s={s}:  E[sigma(a)] = {(1/(1+np.exp(-a))).mean():.4f}   sigma(E[a])=0.5")
```
<details><summary>Reconcile</summary>

All three print $\approx$ `0.5000`. Here the naive guess is *right* — but for a subtle reason: $\sigma$ is symmetric about the point $(0, 0.5)$, and a symmetric $a$ makes the convex-below-0 and concave-above-0 regions cancel *exactly*. Shift the center off zero (try $a\sim N(2, s^2)$) and the cancellation breaks: $\mathbb{E}[\sigma(a)]$ is pulled toward $0.5$, below $\sigma(2)=0.88$, and *more* so as $s$ grows. The lesson: $\mathbb{E}[g(X)]=g(\mathbb{E}[X])$ can hold by symmetry at one special point and fail everywhere else — which is exactly why the course insists on averaging $\sigma$ over the posterior (module 15:240, 15:253) instead of plugging in $\hat\beta$. Ship the plug-in and you ship overconfident probabilities everywhere the logit is not centered at 0.
</details>

**Exercise P2.2 — bigger spread, bigger Jensen gap.**
*Setup:* $X$ is uniform on the two-point set $\{1, 2\}$, and separately on $\{1, 10\}$. Both are "average about the middle," but the spreads differ.
*Predict:* Rank the gap $\mathbb{E}[1/X] - 1/\mathbb{E}[X]$ for the two sets. Is the $\{1,10\}$ gap a little bigger, or *much* bigger?
*Reason:* "Both are just two points; the gap should be similar."
*Run:*
```python
for pts in ([1, 2], [1, 10]):
    x = np.array(pts, float)
    print(f"{pts}: E[1/X]={np.mean(1/x):.4f}  1/E[X]={1/np.mean(x):.4f}  gap={np.mean(1/x)-1/np.mean(x):.4f}")
```
<details><summary>Reconcile</summary>

$\{1,2\}$: gap `0.0833` (`0.75` vs `0.6667`). $\{1,10\}$: gap `0.3682` (`0.55` vs `0.1818`) — over **four times** larger. Jensen's gap scales with the *spread* of $X$ (to second order it is $\tfrac12 g''(\mu)\text{Var}(X)$; here $g''(x)=2/x^3>0$). A tiny bit of spread gives a tiny bias; heavy spread gives a bias that dwarfs the naive answer. This is the harmonic-mean / inverse-variance-weighting trap in miniature (expert-symbolic area ii): the more uncertain $X$ is, the more $\mathbb{E}[1/X]$ exceeds $1/\mathbb{E}[X]$, and the more a plug-in reciprocal misleads.
</details>

**Exercise P2.3 — overdispersion you can't wish away.**
*Setup:* You model daily counts as Poisson, but the true rate varies day to day: $\lambda\sim\text{Gamma}(3, 1)$ (mean 3), and $X\mid\lambda\sim\text{Poisson}(\lambda)$. A colleague fits a plain Poisson and reports $\text{Var}(X)=\mathbb{E}[X]=3$.
*Predict:* Is the true $\text{Var}(X)$ equal to 3, or larger? By how much?
*Reason:* "It's Poisson counts, so variance equals the mean."
*Run:*
```python
lam3 = rng.gamma(3, 1, 1_000_000); X3 = rng.poisson(lam3)
print(f"E[X]={X3.mean():.3f}  Var(X)={X3.var():.3f}  within=E[lam]={lam3.mean():.3f}  between=Var(lam)={lam3.var():.3f}")
```
<details><summary>Reconcile</summary>

$\mathbb{E}[X]=$ `2.997` but $\text{Var}(X)=$ `6.002` — *double* the mean. Law of total variance: $\text{Var}(X)=\mathbb{E}[\lambda]+\text{Var}(\lambda)=3+3=6$. The plain-Poisson fit understates the variance by exactly the between-day variance of the rate. This is why real count data (clicks, defects, disease cases) almost always looks overdispersed: there is a latent rate you didn't condition on, and the law of total variance tells you the missing variance is precisely $\text{Var}(\mathbb{E}[X\mid\lambda])$. The fix is a negative-binomial / Gamma-Poisson model, which is this exact mixture (module 03, 18).
</details>

**Exercise P2.4 — coverage is a mean of a boolean.**
*Setup:* You build a 90% posterior credible interval for a parameter, then simulate 40,000 fresh datasets to check its *frequentist* coverage: the fraction of intervals that contain the true value.
*Predict:* Before coding, in one phrase, what is "coverage"? Write it as a numpy expression.
*Reason:* Forces the marquee identity into muscle memory.
*Run:*
```python
theta0 = 1.3
lo = theta0 + rng.normal(-0.9, 0.55, 40_000)       # pretend interval endpoints...
hi = theta0 + rng.normal(+0.9, 0.55, 40_000)       # ...straddling theta0 ~90% of the time
coverage = ((lo <= theta0) & (theta0 <= hi)).mean() # P(covered) = mean of a boolean
print(f"coverage = {coverage:.4f}")
```
<details><summary>Reconcile</summary>

`coverage = 0.9003` — the *mean of a boolean array*, nothing more. This is module 08:343 verbatim. Coverage, acceptance rate, Type-I error, PPC p-value, $P(B>A)$, cluster lock-in — every one is `(condition).mean()`, an estimate of $\mathbb{E}[\mathbf{1}\{A\}]=P(A)$. Once you read every such line as "probability = mean of an indicator," roughly 48 otherwise-cryptic lines across the course become the same sentence.
</details>

## Takeaways

- **$P(A)=\mathbb{E}[\mathbf{1}\{A\}]$**, and its estimate is `(condition).mean()` — the single most-used identity in the course (~48 silent uses). Coverage, acceptance, p-values, lock-in are all this one line.
- **Linearity splits any sum**, dependent or not; **factoring a product** ($\mathbb{E}[XY]$) and **variance of a sum** (the $2\text{Cov}$ term) are where independence actually matters.
- **LOTUS:** $\mathbb{E}[g(\theta)] = \int g\,p \approx$ `g(draws).mean()` — this *is* line 3 (prediction) and line 4 (expected loss). The self-normalized weighted mean recovers it from the wrong proposal.
- **Tower rule, executed:** $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Y]]$ — pick the conditioner, collapse the inner mean, average out. Recital is not execution.
- **Law of total variance:** total = $\mathbb{E}[\text{within}]+\text{Var}[\text{between}]$ = aleatoric + epistemic; it is the overdispersion engine and the "between = total − noise" trick of empirical Bayes.
- **$\mathbb{E}[g(X)]\neq g(\mathbb{E}[X])$** for curved $g$: $\mathbb{E}[1/X]=1$ is $2\times$ the naive $1/\mathbb{E}[X]=0.5$; $\mathbb{E}[\max(\Delta,0)]$ drives the $81\times$ regret, not the $19{:}1$ probability. A probability weighs worlds; a loss weighs worlds × stakes.

## Where the course uses this

| Skill | Course walls (module:line) |
|---|---|
| $P(A)=\mathbb{E}[\mathbf{1}\{A\}]=$ `mean(bool)` | 00:112 (joint = product); 08:343 (coverage); 09:293 (acceptance); 17:335 (Type-I error); 22:105 (P(B>A)) |
| Linearity across dependent terms | 22:225 (cumulative regret via `cumsum`); 19:306 ($\mathbb{E}[K_n]=\sum$ Bernoulli); 20:506 (covariance sum, H cancels) |
| LOTUS / Monte-Carlo mean $\approx\mathbb{E}[g]$ | 15:253 (`mean(sigmoid(draws@x))`); 06:162 (self-normalized posterior mean); 17:262 (predictive density); 22:106 (expected regret) |
| Tower rule executed | 01:137 ($\mathbb{E}[X_iX_j]=\mathbb{E}[\Theta^2]$); 16:220 (marginalize $\tau$); 22:135 (nested EVPI) |
| Law of total variance | 17:263 (`p_waic = ll.var(0)`); 18:56 (`A_hat = mean(X**2)-1`, between = total − noise); 05 (aleatoric + epistemic split) |
| $\mathbb{E}[g(X)]\neq g(\mathbb{E}[X])$ | 05:374 / 22:106 (`mean(max(tA-tB,0))`, 81× regret); 22:114 (worlds × stakes); 15:240 ($\mathbb{E}[\sigma]\neq\sigma(\mathbb{E})$) |

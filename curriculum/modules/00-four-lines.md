# 00. The Four-Line Course

> **Spine.** The whole subject is four lines; every named procedure is a special case, an approximation, or an audit of them.
> **Which line?** All four — this module states them and runs each at least once.
> **Promise.** You can take any statistical or ML procedure and say which of the four lines it implements, and why.
> **Prereqs.** None. **Runtime.** ~3 s.
> **Sources.** Booklet ch. 1–2; C-B §1.2–1.3; ISLP §6.2.

Here is the entire course, compressed:

1. **A model is a joint distribution** $p(\text{unknowns}, \text{knowns})$.
2. **Inference is conditioning:** the posterior $p(\text{unknowns} \mid \text{knowns})$.
3. **Prediction is marginalization:** $p(\text{new} \mid \text{knowns}) = \int p(\text{new} \mid \text{unknowns})\,p(\text{unknowns} \mid \text{knowns})$.
4. **A decision minimizes posterior expected loss:** the action $a$ minimizing $\mathbb{E}_{\text{unknowns}\mid\text{knowns}}[\,L(a, \text{unknowns})\,]$.

That is not a philosophy; it is a recipe. The rest of the course executes it when the integrals are hard, and shows that the tools you already use — MLE, ridge, dropout, A/B tests — are the recipe in different clothes. We open by catching one in the act.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "00-four-lines"                   # this module's figure dir
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

## 00.1 You were already doing this

Ridge regression is what you reach for with more features than data. Fit `sklearn.linear_model.Ridge(alpha=10)` on $n = 50$ rows, $p = 200$ features: a penalized least-squares fit, nothing Bayesian in sight.

**Predict.** *Intuition:* "ridge is an optimizer; a posterior mean is an integral — different objects." I claim the ridge coefficients equal, to machine precision, both the linear-algebra solution $(X^\top X + 10 I)^{-1} X^\top y$ *and* the **posterior mean** of $\beta$ under $y = X\beta + \varepsilon$, $\varepsilon \sim N(0, \sigma^2 I)$, prior $\beta \sim N(0, (\sigma^2/10) I)$. Agree to 3 digits? 8? Not at all?

```python
n, p = 50, 200
X = rng.standard_normal((n, p))
beta_true = 0.3 * rng.standard_normal(p)
sigma = 1.5
y = X @ beta_true + rng.normal(0, sigma, n)
alpha = 10.0

# Route A: the optimizer (no intercept, so it matches the raw normal equations)
from sklearn.linear_model import Ridge
ridge = Ridge(alpha=alpha, fit_intercept=False).fit(X, y).coef_

# Route B: linear algebra, (X'X + alpha I)^{-1} X'y
normal_eq = np.linalg.solve(X.T @ X + alpha * np.eye(p), X.T @ y)

# Route C: the Bayesian posterior mean under beta ~ N(0, tau^2 I).
# Posterior precision = X'X/sigma^2 + I/tau^2 ; mean solves it against X'y/sigma^2.
# With tau^2 = sigma^2 / alpha, the sigma^2 cancels and alpha = sigma^2/tau^2.
tau2 = sigma**2 / alpha
precision = X.T @ X / sigma**2 + np.eye(p) / tau2
post_mean = np.linalg.solve(precision, X.T @ y / sigma**2)

m = max(np.max(np.abs(ridge - normal_eq)),
        np.max(np.abs(ridge - post_mean)),
        np.max(np.abs(normal_eq - post_mean)))
print(f"max|diff| across all three routes = {m:.1e}")
print(f"all three agree to < 1e-10? {bool(m < 1e-10)}")

fig, ax = plt.subplots(figsize=(4.2, 4.2))
ax.scatter(post_mean, ridge, s=12, alpha=0.6)
lim = 1.05 * np.abs(np.concatenate([ridge, post_mean])).max()
ax.plot([-lim, lim], [-lim, lim], "k--", lw=1, label="y = x")
ax.set_xlabel("posterior mean  (Bayes)")
ax.set_ylabel("Ridge(alpha=10) coef  (sklearn)")
ax.set_title("Three routes, one answer")
ax.legend(loc="upper left")
save(fig, "ridge_equals_posterior")
```

**Reconcile.** The routes agree to `1e-10` — `max|diff|` prints around $4\times10^{-15}$, rounding error. They are the same computation: minimizing $\|y - X\beta\|^2 + \alpha\|\beta\|^2$ *is* finding the mode (here also the mean) of a Gaussian posterior with prior variance $\sigma^2/\alpha$. The penalty $\alpha = \sigma^2/\tau^2$ is a prior-to-data precision ratio; "regularize more" means "use a tighter prior." Every point lands on $y = x$.

![Ridge coefficients vs. the Bayesian posterior mean: all 200 points lie on y=x — the same vector to machine precision.](figures/00-four-lines/ridge_equals_posterior.png)

Same pattern all course: you keep your tools and are shown the joint each silently assumed. Lines 1 and 2 were already there.

## 00.2 Four lines, one patient

A test for a rare disease has sensitivity `0.99` (catches 99% of cases) and specificity `0.95` (clears 95% of the healthy); prevalence is `0.001`. Your patient tests positive — all four lines fit on one page.

**Line 1 — the model is a joint.** The unknown is disease status $D \in \{0,1\}$, the knowns are test results; the joint $p(D, T)$ = prior $\times$ likelihood, with $p(D)$ from prevalence and $p(T \mid D)$ from sensitivity/specificity.

**Line 2 — inference is conditioning.** The patient is positive, so condition:
$$\text{PPV} = p(D{=}1 \mid T_1{=}{+}) = \frac{p(+ \mid D)\,p(D)}{p(+ \mid D)\,p(D) + p(+ \mid \bar D)\,p(\bar D)}.$$

**Predict.** *Intuition:* "99% accurate, so a positive means ~99% disease." Commit to a number first.

```python
sens, spec, prev = 0.99, 0.95, 0.001
print(f"sensitivity {sens}, specificity {spec}, prevalence {prev}")
p_pos_D    = sens * prev              # P(+, D)
p_pos_notD = (1 - spec) * (1 - prev)  # P(+, not D)
PPV = p_pos_D / (p_pos_D + p_pos_notD)
print(f"P(+, D)     = {p_pos_D:.5f}")
print(f"P(+, not D) = {p_pos_notD:.5f}")
print(f"PPV = P(D | one positive) = {PPV:.4f}")

# Odds form (this is all of Bayes' rule): posterior odds = prior odds x LR+
prior_odds = prev / (1 - prev)
LR_pos = sens / (1 - spec)
print(f"prior odds {prior_odds:.4f} x LR+ {LR_pos:.1f} = posterior odds {prior_odds*LR_pos:.4f}")
```

**Reconcile.** The PPV is `0.0194` — under 2%. A positive multiplies your *odds* by the likelihood ratio $\text{LR}^+ = 0.99/0.05 = 19.8$, but 19.8 times a tiny prior odds is still tiny. The test is informative (belief moved 20-fold) yet the patient is almost certainly healthy — "how worried should I be?" is answered by conditioning, not accuracy.

**Line 3 — prediction is marginalization.** What will a second (conditionally independent) test say? Marginalize disease status against the posterior we just built: $p(T_2 \mid T_1{=}{+}) = \sum_{d} p(T_2 \mid D{=}d)\,p(D{=}d \mid T_1{=}{+})$.

**Line 4 — a decision minimizes expected loss.** Fix a cost matrix (a common currency of harm): missing a real case costs 1000, over-treating the healthy costs 10, a retest costs 5 before we decide again.

**Predict.** *Intuition:* "the patient is over 98% likely healthy — surely *no-treat*." Rank treat now / never treat / retest first by expected loss before running.

```python
# Loss(action, state): columns are (D, not D).
L = {"treat":    np.array([0.0,  10.0]),    # over-treat the healthy: 10
     "no-treat": np.array([1000.0, 0.0])}   # miss a real case: 1000
post = np.array([PPV, 1 - PPV])
E_treat    = post @ L["treat"]
E_notreat  = post @ L["no-treat"]

# Retest strategy: pay c, observe T2, then take the cheaper action.
c_retest, LR_neg = 5.0, (1 - sens) / spec
def ppv_after(prev_odds, factor):
    o = prev_odds * factor
    return o / (1 + o)
odds1 = prior_odds * LR_pos
PPV_pp = ppv_after(odds1, LR_pos)   # after a 2nd positive
PPV_pn = ppv_after(odds1, LR_neg)   # after a 2nd negative
p_T2pos = PPV * sens + (1 - PPV) * (1 - spec)          # line 3: predictive
best_after = lambda ppv: min(np.array([ppv, 1-ppv]) @ L["treat"],
                             np.array([ppv, 1-ppv]) @ L["no-treat"])
E_retest = c_retest + p_T2pos * best_after(PPV_pp) + (1 - p_T2pos) * best_after(PPV_pn)

print(f"P(2nd test +) = {p_T2pos:.4f};  PPV after ++ = {PPV_pp:.4f}")
print(f"E[loss | treat now]    = {E_treat:.3f}")
print(f"E[loss | no-treat now] = {E_notreat:.3f}")
print(f"E[loss | retest first] = {E_retest:.4f}")
best = min([("treat", E_treat), ("no-treat", E_notreat), ("retest", E_retest)],
           key=lambda t: t[1])
print(f"optimal action = {best[0]}")
```

**Reconcile.** The favorite loses twice. Never treating — 98% safe! — costs `19.435`, because the rare miss costs 1000; treating everyone costs `9.806`. And paying 5 to retest beats both at `5.6846`: a `0.0683`-probable second positive pushes the PPV to `0.2818` (act), a likely second negative all but clears the patient (don't). Same posterior throughout — the loss function alone picked the winner. That is line 4; module 22 prices "buy more data" as expected value of information.

![Belief in disease: prior 0.001 → one positive 0.0194 → two positives 0.2818. A single positive barely dents a rare-disease prior.](figures/00-four-lines/medical_belief.png)

```python
fig, ax = plt.subplots(figsize=(6, 3.2))
stages = ["prior", "1 positive", "2 positives"]
vals = [prev, PPV, PPV_pp]
ax.bar(stages, vals, color=["C0", "C1", "C1"])
for i, v in enumerate(vals):
    ax.text(i, v + 0.006, f"{v:.4f}", ha="center", fontsize=10)
ax.set_ylabel("P(disease)")
ax.set_ylim(0, 0.32)
ax.set_title("A positive test barely moves a rare-disease belief")
save(fig, "medical_belief")
```

## 00.3 A bet you should turn down

You flip a coin 10 times, see 7 heads. Under a flat prior $\theta \sim \text{Beta}(1,1)$ the posterior is $\text{Beta}(8,4)$, mean $8/12 = 0.6667$; the MLE is $\hat\theta = 7/10 = 0.7$. A bookie offers a bet on the *next* flip: pay `0.68`, receive `1` if heads. You accept when your believed win-probability beats the price.

**Predict.** *Intuition:* "the MLE `0.7` is my best estimate, and `0.7 > 0.68`, so this is a `+0.02` edge — take it." Over many replays, does the plug-in bettor profit or lose?

```python
bet = np.random.default_rng(SEED)   # explicitly seeded local generator
a, b = 8, 4
post_mean = a / (a + b)             # posterior predictive P(next head)
mle, price = 7 / 10, 0.68
print(f"posterior Beta({a},{b}) mean = {post_mean:.4f}   MLE = {mle:.1f}   price = {price:.2f}")
print(f"plug-in bettor's believed edge  = {mle - price:.4f}")
print(f"predictive edge (the truth)      = {post_mean - price:.4f}")

# Replay: draw theta from the posterior, then the next flip ~ Bernoulli(theta).
# Averaging over theta IS the posterior predictive (line 3), so E[win] = post_mean.
N = 1_000_000
theta = bet.beta(a, b, N)
win = (bet.random(N) < theta).astype(float)
profit = win - price
print(f"simulated P(next head)          = {win.mean():.4f}")
print(f"simulated mean profit (plug-in) = {profit.mean():.4f}")
print(f"total over {N:,} $1 bets = ${profit.sum():+,.0f}")
```

**Reconcile.** The plug-in bettor is down `-13,235` dollars over a million $1 bets — `-0.0132` per bet, a rounding error per flip, a fortune in aggregate. The MLE `0.7` answers "which single $\theta$ best explains the 10 flips"; the bet asks "probability the *next* flip is heads?", whose honest answer marginalizes over everything unknown about $\theta$ — the posterior predictive, the posterior *mean* `0.6667`, not the likelihood mode. The bookie priced at `0.68`, inside the gap between plug-in optimism (`0.7`) and predictive honesty (`0.6667`), and harvested exactly that gap. A point estimate discards your uncertainty, and someone can charge you for it — which is why line 3 is an integral. Module 05 formalizes it as the rule of succession.

![The Beta(8,4) posterior: the MLE 0.7 sits right of the predictive mean 0.6667, and the bet price 0.68 falls in between — so the plug-in bettor accepts a losing bet.](figures/00-four-lines/coin_bet.png)

```python
fig, ax = plt.subplots(figsize=(6.5, 3.6))
th = np.linspace(0, 1, 400)
ax.plot(th, stats.beta(a, b).pdf(th), color="C1", label="posterior Beta(8,4)")
ax.axvline(post_mean, color="C1", ls="-",  lw=1.5, label=f"posterior mean {post_mean:.4f} (predictive)")
ax.axvline(mle,       color="k",  ls="--", lw=1.5, label=f"MLE {mle:.1f}")
ax.axvline(price,     color="C3", ls=":",  lw=2.0, label=f"bet price {price:.2f}")
ax.set_xlabel(r"$\theta$ = P(heads)")
ax.set_ylabel("posterior density")
ax.set_title("The bet lives in the gap between plug-in and predictive")
ax.legend(fontsize=8, loc="upper left")
save(fig, "coin_bet")
```

## 00.4 Which line is your favorite method?

Every procedure below is one of the four lines, an approximation to one, or an audit tool. Commit to an answer for each — *model, conditioning, prediction, decision,* or *audit* — before the reveal:

> MLE · ridge / weight decay · lasso · cross-validation · confidence interval · p-value · bootstrap · Kalman filter · k-means · dropout · deep ensembles · cross-entropy loss · A/B test · conformal prediction

<details><summary>Reveal the lines</summary>

| Procedure | Line | Why |
|---|---|---|
| MLE | 2 | posterior mode under a flat prior |
| Ridge / weight decay | 1→2 | Gaussian prior, then its MAP/mean (§00.1) |
| Lasso | 1→2 | Laplace prior, then its sparse MAP mode |
| Cross-validation | 3, audit | estimates out-of-sample predictive loss |
| Confidence interval | 2 | frequentist cousin of the credible interval |
| p-value | audit | tail-area check of a model under a null |
| Bootstrap | 2 | resampling ≈ an implicit posterior |
| Kalman filter | 3 then 2 | predict = marginalize, update = condition |
| k-means | 2 | hard-assignment limit of Gaussian-mixture EM |
| Dropout (test time) | 3 | averaging stochastic passes ≈ predictive |
| Deep ensembles | 3 | model averaging ≈ multi-modal posterior |
| Cross-entropy loss | 1 | categorical NLL; minimizing it = MLE |
| A/B test | 4 | ship the arm minimizing expected loss |
| Conformal prediction | 3, audit | predictive coverage under exchangeability |

Not every method is a *pure* line — Kalman is two in a loop, and the audit tools are frequentist checks *on* a Bayesian object. The four lines are the coordinate system; the methods are points in it. Modules 08, 17, and 26 build this table out with running code.

</details>

## 00.5 Notation, conventions, and running the code

Every symbol is defined at first use in each module. The course-wide conventions, stated once and never re-litigated:

| Object | Notation | Convention |
|---|---|---|
| Density / pmf | $p(\cdot)$ | generic; subscripts only when ambiguous |
| Event probability | $P(\cdot)$ | |
| Unknowns / parameters | $\theta, \phi, \lambda, \mu, \sigma^2$ | **anything unknown to you is a random variable** |
| Observed data | $y$ (response), $x$ (covariates, conditioned on) | dataset $D = \{(x_i, y_i)\}_{i=1}^n$ |
| Future data | $\tilde y$ | posterior predictive $p(\tilde y \mid y)$ |
| Normal | $N(\mu, \sigma^2)$ | **second argument is the VARIANCE**, not the SD |
| Gamma | $\text{Gamma}(\alpha, \beta)$ | **$\beta$ is the RATE**; `scipy.stats.gamma(a=α, scale=1/β)` |
| Exponential | $\text{Exp}(\lambda)$ | rate; `scipy.stats.expon(scale=1/λ)` |
| Inverse-Gamma | $\text{IG}(\alpha, \beta)$ | `scipy.stats.invgamma(a=α, scale=β)` |
| Student-t | $t_\nu(\mu, \sigma^2)$ | location–scale; `scipy.stats.t(df=ν, loc=μ, scale=σ)` |
| Beta, Binomial, Poisson, Dirichlet, Multinomial | standard | |
| KL divergence | $\text{KL}(q \,\|\, p)$ | $\mathbb{E}_q[\log q - \log p] \ge 0$ |
| Expectation / variance | $\mathbb{E}[\cdot], \text{Var}[\cdot], \text{Cov}[\cdot,\cdot]$ | subscript the measure when unclear: $\mathbb{E}_{\theta\mid y}[\cdot]$ |
| Proportional to | $\propto$ | drop constants not involving the target variable |

**Two conventions worth shouting** (they cause the most silent bugs): $N(\mu, \sigma^2)$ takes the **variance**, but `scipy.stats.norm` and `rng.normal` take the **SD** — $N(0, 4)$ is `rng.normal(0, 2)`. And $\text{Gamma}(\alpha, \beta)$, $\text{Exp}(\lambda)$ are **rates** while SciPy uses **scale = 1/rate**. Where a call hits either trap, the code comments it.

**Running the module code.** Every module's ```python``` blocks run top-to-bottom in one namespace (cwd `curriculum/`) via the harness:

```
python tools/run_module.py modules/00-four-lines.md --check-determinism
```

Block 1 is always the setup block above (it seeds `rng`, sets a headless backend, defines `save`). The harness runs the blocks, checks two runs give byte-identical output (determinism), and verifies every backtick-quoted prose number was actually printed. Figures go via `save(fig, name)` into `figures/00-four-lines/`; ```python no-run``` blocks are skipped illustrations.

**Assumed background.** Undergraduate probability and calculus — joint/marginal/conditional densities, expectation and variance, change-of-variables (Jacobian), basic combinatorics — are trusted and recapped only in passing; if a step feels too fast, Casella–Berger ch. 1–2 are the patch. Python (numpy/scipy/matplotlib) is assumed; **there is no R anywhere in this course** — the booklet's R code is absorbed for its statistics only.

## Bridge — what the four lines compress

The booklet's "five steps" (ch. 2) are lines 1–4 plus a model-check we make runnable in module 17. Casella–Berger §1.2–1.3 develops Bayes' rule as the ratio-of-joints identity $p(A\mid B) = p(A,B)/p(B)$; line 2 is that identity with "unknowns" for $A$, "data" for $B$. ISLP §6.2 presents ridge as a bias–variance knob; §00.1 showed the knob is a prior variance. Throughout, the operative split is not Bayesian-versus-frequentist tribes but bookkeeping: **which quantities you treat as random (unknown to you) versus fixed (known, or conditioned on)** — frequentist tools reappear as special cases, approximations, or audits.

## Pitfalls

- **Confusing accuracy with the posterior.** A "99% accurate" test gave a 2% PPV; the base rate is half of Bayes' rule, and ignoring it is line 2 done wrong.
- **Plugging a point estimate in where an integral belongs.** The MLE gives the "best single $\theta$"; prediction needs the posterior predictive, which averages over $\theta$ — the coin bet made the loss literal.
- **Reporting a posterior as if it were a decision.** A posterior is an input to line 4; without a loss function "what should I do?" has no answer. One PPV justified treat, no-treat, *or* retest, on costs alone.
- **Reading "noninformative" as "no choice."** A flat prior is still a modeling choice (module 07), and "just regularization" hides the Gaussian prior you committed to.
- **Parameterization traps.** $N(\mu,\sigma^2)$ is variance; SciPy wants SD. $\text{Gamma}$/$\text{Exp}$ here are rates; SciPy wants scale. These cause more bugs than any theorem.

## Exercises

**Exercise 00.1 — Weight decay is a prior with a dial.**
*Setup:* §00.1's ridge `alpha=10` matched the posterior mean under $\beta \sim N(0, (\sigma^2/\alpha) I)$; deep-learning weight decay is the same $\ell_2$ penalty.
*Predict:* As `alpha` climbs `1` → `1000`, does the implied prior widen or narrow, and does $\|\hat\beta\|$ grow or shrink?
*Reason:* "Regularization strength ↔ prior variance."
*Run:*
```python
for al in [1.0, 10.0, 100.0, 1000.0]:
    co = Ridge(alpha=al, fit_intercept=False).fit(X, y).coef_
    print(f"alpha={al:7.1f}  implied tau^2 = sigma^2/alpha = {sigma**2/al:.5f}"
          f"   ||beta|| = {np.linalg.norm(co):.4f}")
```
<details><summary>Reconcile</summary>

Bigger `alpha` = a *narrower* prior ($\tau^2 = \sigma^2/\alpha$ shrinks from `2.25000` to `0.00225`) and a smaller norm (`2.5110` → `0.3521`). Weight decay is not a training trick; it is the precision of a mean-zero Gaussian prior on the weights, its "decay rate" the inverse prior variance. Module 06 derives the MAP identity.
</details>

**Exercise 00.2 — The base rate strikes back.**
*Setup:* Same test, but the disease is ten times more common: prevalence `0.01`.
*Predict:* PPV was `0.0194` at prevalence `0.001`. At ten times the prevalence, is it about ten times bigger (≈ 0.19)?
*Reason:* "Posterior probability scales with the prior."
*Run:*
```python
ppvs = {}
for prev2 in [0.001, 0.01]:
    ppv = sens * prev2 / (sens * prev2 + (1 - spec) * (1 - prev2))
    odds = (prev2 / (1 - prev2)) * (sens / (1 - spec))
    ppvs[prev2] = ppv
    print(f"prevalence {prev2}: PPV = {ppv:.4f}   posterior odds = {odds:.4f}")
print(f"PPV ratio {ppvs[0.01] / ppvs[0.001]:.1f}x for a 10x prevalence change")
```
<details><summary>Reconcile</summary>

The PPV goes `0.0194` → `0.1667`: `8.6`×, not 10×, and still only ~17%. What scales (almost) linearly is the *odds*, not the probability — Bayes' rule is linear in odds ($\text{odds}_{\text{post}} = \text{odds}_{\text{prior}} \times \text{LR}$), and the map $o/(1+o)$ compresses the top end. Even a good test, on a 1-in-100 condition, leaves a positive patient more likely healthy than sick — screening programs live and die by this arithmetic.
</details>

**Exercise 00.3 — Sequential equals batch (an online-learning identity).**
*Setup:* The same 10 flips (7 heads), two ways: all at once, or streamed one at a time updating the Beta posterior after each — the online-learning pattern.
*Predict:* Does folding flips in one at a time (from `Beta(1,1)`), in scrambled order, give a different posterior than the batch update?
*Reason:* "Sequential updates might be order-sensitive — SGD is."
*Run:*
```python
flips = np.array([1, 1, 0, 1, 1, 1, 0, 1, 0, 1])  # 7 heads, some order
online = np.array([1, 1])                          # (a, b) for Beta(1,1)
for f in rng.permutation(flips):                   # scramble the arrival order
    online = online + np.array([f, 1 - f])
batch = np.array([1 + flips.sum(), 1 + len(flips) - flips.sum()])
print(f"streamed (shuffled order): Beta{tuple(int(v) for v in online)}")
print(f"batch (all at once):       Beta{tuple(int(v) for v in batch)}")
```
<details><summary>Reconcile</summary>

Both give `Beta(8, 4)`, regardless of order. Conditioning is associative and order-free: $p(\theta \mid y_1, y_2) \propto p(y_2 \mid \theta)\,p(y_1 \mid \theta)\,p(\theta)$, and multiplication commutes. Unlike an SGD pass — order- and step-size-dependent because it only *approximates* — exact updating depends only on the data seen, not the schedule. Module 02 shows the identity in general; module 21 turns streaming updates into the Kalman filter.
</details>

## Takeaways

- **The four lines are the whole course:** model = joint, inference = conditioning, prediction = marginalization, decision = minimize expected loss. Make them reflex.
- **Your existing tools are special cases.** Ridge is a Gaussian-prior posterior mean; MLE a flat-prior mode; cross-entropy a likelihood. The course reinterprets, it does not replace.
- **Accuracy ≠ posterior.** A 99%-accurate test can give a 2% PPV; the base rate is the other half of line 2.
- **Never plug a point estimate into a prediction.** The predictive integrates over your uncertainty; collapsing it to the MLE is a bet you can be charged for.
- **A posterior is not a decision.** It is an input to line 4; the same belief can justify opposite actions under different costs.
- **Anything unknown is a random variable** — the one bookkeeping rule the whole course runs on.

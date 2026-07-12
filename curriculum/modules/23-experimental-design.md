# 23. Experimental Design

> **Spine.** The design fixes the likelihood you get to condition on — randomization buys ignorability (the likelihood you wrote is the likelihood you got), and information can be priced before you spend a dollar collecting it.
> **Which line?** Upstream of line 2. Every earlier module took the data as given and conditioned; this one chooses *which joint distribution you will end up conditioning on*. Design is the one lever that acts before the likelihood exists.
> **Promise.** After this module you can say why a Bayesian still randomizes, tell power from assurance and compute both, survive the optional-stopping minefield with four claims kept straight, read a factorial experiment as a regression, and choose the next measurement by expected information gain.
> **Prereqs.** Modules 04 (the likelihood principle and its design-stage scope box — the ~4×-at-10-looks number promised there is proved here), 07 (priors, prior-predictive simulation), and the decision frame (utility → action, EVSI/preposterior). Callbacks to 01 (exchangeability = the permutation null), 05 (conjugate Gaussian update), 17 (the foregone-conclusion Bayes-factor caveat).
> **Runtime.** ~7 s measured (all numpy/scipy; conjugate updates inside every simulation loop, no MCMC — the whole optional-stopping lab is vectorized).
> **Sources.** Montgomery, *Design and Analysis of Experiments* 8e, ch. 1–6, 9 (the 2³ nitride-etch example is Montgomery's Example 6.1, reproduced exactly); booklet ch. 6–7; Lindley (information-theoretic design) by concept; Berger–Wolpert on the likelihood principle by concept.

## 23.1 Why a Bayesian still randomizes

Module 04 settled that a Bayesian's *post-data* inference ignores the stopping rule: identical likelihood, identical posterior, whatever your intentions. The over-reading is "then design does not matter to me." It matters enormously — one step earlier. Design does not change how you condition; it changes *what joint distribution you condition inside*. The likelihood you write down assumes a data-generating story, and randomization is the cheapest way to make that story true. Here is the trap, staged as the module's first reveal.

**Setup.** A binary treatment $T$, an outcome $Y$, and a lurking variable $U$ (call it baseline severity) that raises $Y$ on its own. The true causal effect of treatment is $\tau = 2$. You will fit the *same* model to two datasets — a plain linear regression of $Y$ on an intercept and $T$, with $U$ never measured, never in the model:
$$Y_i = \beta_0 + \beta_T\,T_i + \varepsilon_i,\qquad \varepsilon_i\sim N(0,\sigma^2),$$
and read the posterior for $\beta_T$. In dataset **C** the treatment was assigned by severity — sicker patients ($U$ high) were more likely to be treated. In dataset **R** the treatment was assigned by a coin. Same generative code for $Y$ given $(T,U)$; same analysis model; two ways of choosing who got $T$.

**Predict.** Same model, two data collections — *will the posterior know?* Commit: is $\beta_T$'s posterior (i) wrong in **C**, right in **R**; (ii) wrong in both (the model omits $U$ either way); or (iii) right in both, because the likelihood is deaf to intentions (the module-04 lesson)?

*Reason:* the tempting answer is (iii) — module 04 hammered "the posterior only sees the likelihood." The subtlety module 04 flagged in its scope box is that the *design* determines *which* likelihood is the true one.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "23-experimental-design"          # this module's figure dir
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
# Conjugate Gaussian-prior linear model with an EB plug-in for sigma^2:
# posterior for beta is Normal (STYLE: N(mu, VARIANCE)); no MCMC anywhere.
def blr(X, y, tau2=100.0):
    """Posterior mean/cov for beta ~ N(0, tau2 I), y ~ N(X beta, sigma2 I).
    sigma2 estimated once from the OLS residual (empirical-Bayes plug-in)."""
    b_ols, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ b_ols
    s2 = resid @ resid / (len(y) - X.shape[1])
    p = X.shape[1]
    Sn = np.linalg.inv(np.eye(p) / tau2 + X.T @ X / s2)   # posterior covariance
    mn = Sn @ (X.T @ y / s2)                               # posterior mean
    return mn, Sn, s2

TAU, GAMMA, ALPHA = 2.0, 3.0, 1.0     # true causal effect, U->Y, intercept
n = 800
g = np.random.default_rng(1)          # dedicated stream for a stable demo
U = g.normal(0, 1, n)                 # unmeasured baseline severity

# C: confounded assignment — sicker (high U) more likely treated.
pT = 1 / (1 + np.exp(-1.5 * U))
Tc = (g.random(n) < pT).astype(float)
Yc = ALPHA + TAU * Tc + GAMMA * U + g.normal(0, 1, n)

# R: randomized assignment — a coin, independent of U.
Tr = (g.random(n) < 0.5).astype(float)
Yr = ALPHA + TAU * Tr + GAMMA * U + g.normal(0, 1, n)

mc, Sc, _ = blr(np.column_stack([np.ones(n), Tc]), Yc)   # fit ignores U
mr, Sr, _ = blr(np.column_stack([np.ones(n), Tr]), Yr)
mo, So, _ = blr(np.column_stack([np.ones(n), Tc, U]), Yc) # oracle: adjust for U

print(f"true causal effect      : {TAU:.3f}")
print(f"confounded  beta_T post : {mc[1]:.3f} +/- {np.sqrt(Sc[1,1]):.3f}")
print(f"randomized  beta_T post : {mr[1]:.3f} +/- {np.sqrt(Sr[1,1]):.3f}")
print(f"confounded + adjust U   : {mo[1]:.3f} +/- {np.sqrt(So[1,1]):.3f}")

fig, ax = plt.subplots()
grid = np.linspace(0, 7, 400)
ax.plot(grid, stats.norm(mc[1], np.sqrt(Sc[1,1])).pdf(grid), color="C1",
        lw=2, label=f"confounded  ({mc[1]:.2f})")
ax.plot(grid, stats.norm(mr[1], np.sqrt(Sr[1,1])).pdf(grid), color="C0",
        lw=2, label=f"randomized  ({mr[1]:.2f})")
ax.axvline(TAU, color="black", ls="--", lw=1.4, label="true effect = 2")
ax.set_xlabel(r"treatment effect $\beta_T$ (same model, two designs)")
ax.set_ylabel("posterior density")
ax.set_title("Confidently wrong vs quietly right — the design, not the model, decides")
ax.legend()
save(fig, "confounded_vs_randomized")
```

![Posterior for the treatment effect under two designs: the confounded fit is a narrow spike at 5.3 (confidently wrong), the randomized fit sits on the true value 2.](figures/23-experimental-design/confounded_vs_randomized.png)

**Reconcile.** The answer is (i), and the sharp part is *how* wrong the confounded posterior is: $\beta_T = `5.288`\pm`0.187`$ — a posterior sitting seventeen standard deviations from the truth of 2, and tighter the more data you pour in. The randomized fit lands at $`2.010`\pm`0.224`$, covering the truth. Adjusting the confounded data for $U$ recovers $`2.135`$ — but you had that option only because you *measured* $U$; randomization neutralizes the confounders you never thought to measure.

Module 04 was right: the posterior is deaf to intentions and sees only the likelihood. But *which* likelihood is correct is a fact about the world, set by the design. In dataset C the true joint is $p(Y\mid T,U)\,p(T\mid U)\,p(U)$; regressing $Y$ on $T$ alone writes down $p(Y\mid T)$, which is a *different* distribution — its slope absorbs the severity gradient. Randomization forces $T \perp U$, so $p(Y\mid T)$ under the design equals the causal $p(Y\mid \mathrm{do}(T))$, and the model you wrote is the model you got. This is **ignorability**: the assignment mechanism is independent of the potential outcomes given what you conditioned on. Slogan: *the likelihood you wrote is the likelihood you got.* The formal machinery — potential outcomes, backdoor adjustment, what to do when you cannot randomize — is module 24; here the lesson is only that a Bayesian's indifference to *stopping* rules does not extend to *assignment* rules, because assignment writes the joint.

## 23.2 Power answers a $\theta$ you don't know; assurance averages over what you believe

You are sizing a two-arm experiment: $n$ per group, outcomes $N(\mu,\sigma^2)$ with $\sigma=1$ known, testing $H_0:\delta=0$ (no difference in means) two-sided at $\alpha=0.05$. The classical question is **power**: fix an effect size $\delta$, and ask how often you would reject. With $n$ per arm the test statistic has non-centrality $\delta\sqrt{n/2}/\sigma$, so
$$\text{power}(\delta) = \Phi\!\big(\delta\sqrt{n/2}/\sigma - z_{0.975}\big) + \Phi\!\big(-\delta\sqrt{n/2}/\sigma - z_{0.975}\big).$$
Choose $n=63$ so that power at the design point $\delta=0.5$ is about 80% — the textbook target.

But $\delta=0.5$ is a number you *do not know*; it is the effect you are running the experiment to learn. A Bayesian carries a prior over it, $\delta\sim N(0.5,0.2^2)$ say (centered where the classical analyst planted their point, but honest that it could be smaller or larger). **Assurance** is the prior-averaged power — the preposterior probability that the experiment will "work":
$$\text{assurance} = \int \text{power}(\delta)\,\pi(\delta)\,d\delta = \mathbb{E}_{\pi}[\text{power}(\delta)].$$

**Predict.** You designed for 80% power at $\delta=0.5$. Your prior is centered *exactly* at 0.5. Is your assurance (a) also ≈0.80, since the prior mean is the design point; (b) higher; or (c) lower?

*Reason:* the naive intuition is that averaging over a prior centered at the design point returns the design-point power — "the center is the average." Power is not linear in $\delta$, so that intuition is about to break.

```python
z = stats.norm.ppf(0.975)
sigma = 1.0

def power(delta, n):                       # two-sided two-sample z-test power
    ncp = delta * np.sqrt(n / 2) / sigma
    return stats.norm.cdf(ncp - z) + stats.norm.cdf(-ncp - z)

n_per = 63
gd = np.linspace(-0.5, 1.5, 4001)          # quadrature grid over the unknown delta
prior = stats.norm(0.5, 0.2).pdf(gd); prior /= prior.sum()
assurance = float(np.sum(prior * power(gd, n_per)))
pt_point = float(power(0.5, n_per))
print(f"power at the design point delta=0.5 : {pt_point:.4f}")
print(f"assurance (prior N(0.5, 0.2^2))     : {assurance:.4f}")

fig, ax = plt.subplots()
dd = np.linspace(-0.2, 1.4, 400)
ax.plot(dd, power(dd, n_per), color="C0", lw=2, label="power($\\delta$)")
ax.axvline(0.5, color="black", ls="--", lw=1, label="design point 0.5")
ax.axhline(pt_point, color="C0", ls=":", lw=1)
ax.axhline(assurance, color="C3", lw=1.6, label=f"assurance {assurance:.2f}")
ax2 = ax.twinx()
ax2.fill_between(gd, stats.norm(0.5, 0.2).pdf(gd), color="C1", alpha=0.2)
ax2.set_ylabel("prior density on $\\delta$", color="C1"); ax2.grid(False)
ax.set_xlabel("true effect size $\\delta$"); ax.set_ylabel("probability of rejecting $H_0$")
ax.set_title("Power is a point; assurance averages it against your prior")
ax.legend(loc="center right")
save(fig, "power_vs_assurance")
```

![The power curve (concave over plausible effects) with the prior on δ overlaid; assurance is the prior-weighted average, sitting below the design-point power.](figures/23-experimental-design/power_vs_assurance.png)

**Reconcile.** Assurance is `0.7140`, well below the `0.8013` power at the design point — answer (c). The prior is symmetric about 0.5, but the power curve is *concave over the bulk of this prior's support* (globally it is S-shaped — convex near $\delta=0$ — but at $n=63$ the non-centrality already exceeds the critical value across the prior's mass, which is Φ's concave region): it climbs steeply and flattens toward 1. Averaging a concave function pulls you below its value at the mean (Jensen, the inequality that made KL non-negative in module 03) — prior mass on effects smaller than 0.5 costs more power than the equal mass above buys back. Power answers "if the effect were exactly this, how often would I win?"; assurance answers the question you can act on — "given everything I believe, how often will this experiment win?" A reviewer who asks for 80% power is pricing certainty at a $\delta$ nobody has; assurance is the number you can act on, and it is almost always lower.

## 23.3 The optional-stopping lab: four claims, kept apart

This is the module's centerpiece, and it is where careers' worth of confusion lives. "Peeking at the data as it arrives and stopping when you like" does four *different* things to four *different* quantities. Collapsing them is the classic error. Keep them separate.

Setup for all four: a stream of Bernoulli($\theta$) trials (think conversions), analyzed with a Beta(1,1) prior, and — for the frequentist comparisons — the two-sided $z$-test of $H_0:\theta=0.5$ at $\alpha=0.05$.

**Predict — the four-way split.** Before any code, commit to four verdicts for a rule that peeks after every observation and stops when it likes:
(a) does the **posterior** change vs. a fixed-$n$ experiment landing on the same counts?
(b) does the Bayesian credible interval's **prior-averaged coverage** (drawn $\theta$, does the interval catch it?) stay at 95%, or degrade?
(c) does the frequentist **Type-I rate** stay at 5%, and by how much does it inflate at 10 looks / under continuous monitoring?
(d) does **selective reporting** — publish only the experiments that reached significance — leave anyone's intervals calibrated?

*Reason:* the folklore is "peeking breaks everything" (over-pessimistic about a,b) fused with "Bayesians are immune to peeking" (over-optimistic about d). Both halves are wrong. The four claims dissociate.

### (a) The posterior is unchanged — likelihood identity

Let $x_{1:n}$ be the observed bits and let the stopping time $\tau$ be any rule adapted to the data (it may look at everything seen so far, but not the future or $\theta$). The probability of the realized sequence is
$$p(x_{1:n},\ \tau=n\mid\theta) = \Big[\textstyle\prod_i \theta^{x_i}(1-\theta)^{1-x_i}\Big]\cdot \mathbf{1}\{\text{the rule stops here}\} = \theta^{s}(1-\theta)^{n-s}\cdot(\text{factor free of }\theta),$$
because whether the rule fires is a deterministic function of the *already-observed* bits — it contributes no $\theta$. So the likelihood is $\propto\theta^s(1-\theta)^{n-s}$, exactly as if $n$ had been fixed in advance, and the posterior is $\text{Beta}(1+s,\,1+n-s)$ either way.

```python
# Two genuinely different routes to the stopped-stream posterior:
#   route 1 — walk the stream bit by bit, multiplying in each Bernoulli term
#             AND the stopping rule's continue/stop decisions, on a theta grid;
#   route 2 — the closed-form Beta(1+s, 1+n-s) that pretends n was fixed.
g = np.random.default_rng(4)
theta_true = 0.4
stream = (g.random(500) < theta_true).astype(int)
s_cum = np.cumsum(stream); n_ax = np.arange(1, 501)
# rule: stop the first time the running 95% CI excludes 0.5 (or at n=500)
lo = stats.beta.ppf(0.025, 1 + s_cum, 1 + n_ax - s_cum)
hi = stats.beta.ppf(0.975, 1 + s_cum, 1 + n_ax - s_cum)
fired = np.where((lo > 0.5) | (hi < 0.5))[0]
stop = int(fired[0] + 1) if len(fired) else 500
s = int(s_cum[stop - 1])

# route 1: sequential accumulation. At each step the rule's decision (continue
# until `stop`, stop at `stop`) multiplies the likelihood by an indicator that
# depends only on the bits so far — a CONSTANT in theta, so it cancels in the
# normalization. We keep it explicit to show exactly where it drops out.
tgrid = np.linspace(0.001, 0.999, 999)
log_lik = np.zeros_like(tgrid)
for i in range(stop):
    x = stream[i]
    log_lik += np.log(tgrid) if x else np.log(1 - tgrid)
    # stopping-rule factor: 1{rule says continue} (i < stop-1) or 1{rule says
    # stop} (i == stop-1) — either way identically 1 on the realized path and
    # free of theta:  log(1) = 0 added to every grid point.
post_grid = np.exp(log_lik - log_lik.max())
post_grid /= np.trapezoid(post_grid, tgrid)               # flat Beta(1,1) prior

# route 2: closed form, blind to the stopping rule
post_beta = stats.beta.pdf(tgrid, 1 + s, 1 + stop - s)

print(f"stopped at n={stop}, s={s} successes")
print(f"posterior mean: sequential grid {np.trapezoid(tgrid*post_grid, tgrid):.6f}"
      f" vs Beta({1+s},{1+stop-s}) {(1+s)/(2+stop):.6f}")
print(f"max |density difference| between the two routes: "
      f"{np.max(np.abs(post_grid - post_beta)):.2e}")
```

The two routes agree: posterior means `0.250000` and `0.250000`, max density gap `1.00e-08` (trapezoid-vs-exact normalization at the grid resolution — tighten the grid and it shrinks). Route 1 marched through the data *with the stopping rule in the product* and watched every one of its factors contribute $\log 1 = 0$; route 2 never heard of the rule. Claim (a): **stopping rules leave the posterior untouched.** This is module 04's likelihood principle, now verified for adaptive stopping.

### (b) Prior-averaged calibration survives too — the posterior is a martingale

Claim (a) is about one dataset. Claim (b) is the stronger, more surprising fact: *aggregate* calibration is also preserved. Draw $\theta$ from the prior, generate data, peek and stop aggressively, report the 95% credible interval — over the whole prior-averaged process, does the interval catch $\theta$ 95% of the time? The theorem says yes, for *any* data-adapted stopping rule, because $P(\theta\in\text{CI}\mid\text{data})=0.95$ holds *for every dataset* by construction of a credible interval, and the stopping time is a function of the data — conditioning on the stopped data already fixes it. (Equivalently: the posterior is a martingale in the data filtration; optional stopping does not move its prior-averaged calibration.) We simulate a Normal-Normal version — $\theta\sim N(0,1)$, $y_i\sim N(\theta,1)$, stop the moment the 95% interval excludes 0 — because it is fully conjugate and vectorizes.

```python
# Prior-averaged credible-interval coverage under AGGRESSIVE optional stopping.
g = np.random.default_rng(0)
reps, maxN, tau0 = 20000, 200, 1.0
theta = g.normal(0, tau0, reps)
y = g.normal(theta[:, None], 1.0, (reps, maxN))
cs = np.cumsum(y, axis=1); ns = np.arange(1, maxN + 1)
prec = 1 / tau0**2 + ns                      # posterior precision (sigma^2 = 1)
m = (cs) / prec                              # posterior mean at every n (vectorized)
sd = np.sqrt(1 / prec)
excl0 = np.abs(m) > z * sd                    # 95% CI excludes 0  -> stop
first = np.where(excl0.any(1), excl0.argmax(1), maxN - 1)   # stop index (else maxN)
mm = m[np.arange(reps), first]; ss = sd[first]   # sd depends only on n
cover_stop = np.mean((mm - z * ss <= theta) & (theta <= mm + z * ss))
# fixed-n baseline at n = maxN
prec_f = 1 / tau0**2 + maxN
mf = cs[:, -1] / prec_f; sdf = np.sqrt(1 / prec_f)
cover_fixed = np.mean((mf - z * sdf <= theta) & (theta <= mf + z * sdf))
print(f"mean stopping time under the aggressive rule : {first.mean() + 1:.1f}")
print(f"Bayesian coverage, aggressive stopping       : {cover_stop:.4f}")
print(f"Bayesian coverage, fixed n=200 (baseline)    : {cover_fixed:.4f}")
```

Coverage under aggressive stopping is `0.9494`, indistinguishable from the fixed-$n$ baseline `0.9502` and from the nominal 0.95 — despite a mean stopping time of `29.4` and a rule explicitly engineered to chase significance. Claim (b): **prior-averaged Bayesian coverage is immune to optional stopping.** This is the deepest of the four; hold onto it, because (d) will show its precise limit.

### (c) The frequentist Type-I rate inflates — and you must always state the number of looks

The frequentist guarantee is *unconditional*: "over hypothetical repetitions of this design, I reject a true null 5% of the time." Peeking changes the design — every look is another chance to cross the line — so the guarantee, honestly recomputed, is worse. Simulate under a true null $\theta=0.5$ and reject if *any* look is significant.

**Predict.** Ten equally spaced looks up to $N=1000$: is the Type-I rate about (a) 0.05 still, (b) ~0.10, (c) ~0.20, (d) ~0.35? And under *continuous* monitoring (a look after every trial to $N=1000$)?

```python
g = np.random.default_rng(0)
reps, N = 20000, 1000
ns = np.arange(1, N + 1, dtype=np.float32)
# z-statistic at every cumulative n, in float32 to keep the (reps x N) array light
cum = np.cumsum(g.random((reps, N)) < 0.5, axis=1, dtype=np.float32)
zstat = np.abs(cum / ns - 0.5) / np.sqrt(0.25 / ns)
del cum

def typeI_at_looks(k):
    looks = np.linspace(N / k, N, k).astype(int)
    return float((zstat[:, looks - 1] > z).any(axis=1).mean())

t1  = typeI_at_looks(1)
t10 = typeI_at_looks(10)                       # ten equally-spaced interim looks to N=1000
t_cont = float((zstat[:, 9:] > z).any(axis=1).mean())   # continuous: peek every step from n=10
print(f"Type-I,  1 look  (= fixed n=1000): {t1:.4f}")
print(f"Type-I, 10 looks                 : {t10:.4f}  (inflation {t10/0.05:.1f}x)")
print(f"Type-I, continuous to N=1000     : {t_cont:.4f}  (inflation {t_cont/0.05:.1f}x)")

fig, ax = plt.subplots()
ks = [1, 2, 3, 5, 10, 20, 50]
rates = [typeI_at_looks(k) for k in ks]
ax.plot(ks, rates, "o-", color="C1", label="actual Type-I rate")
ax.axhline(0.05, color="black", ls="--", lw=1, label="nominal 0.05")
ax.axhline(t_cont, color="C3", ls=":", lw=1.4, label=f"continuous → {t_cont:.2f}")
ax.set_xscale("log"); ax.set_xlabel("number of interim looks (log scale)")
ax.set_ylabel("P(reject true null at some look)")
ax.set_title("Every peek is another coin flip against a true null")
ax.legend()
save(fig, "type_I_inflation")
```

![Type-I error against number of interim looks (log x-axis): 5% at one look, ~20% at ten, ~47% under continuous monitoring.](figures/23-experimental-design/type_I_inflation.png)

**Reconcile.** One look gives `0.0522` — the nominal 5%, as it must. Ten looks give `0.2044`, a `4.1`× inflation — this is the number module 04's scope box promised ("roughly 4× at ~10 interim looks"), now cashed. Continuous monitoring to $N=1000$ gives `0.4664`, a `9.3`× inflation, and by the law of the iterated logarithm this diverges toward 1 as $N\to\infty$: peek often enough at a true null and you are *guaranteed* to reject it eventually. The moral is not "frequentist tests are broken" — the number is the correct answer to "how often does *this peeking procedure* reject a true null." The moral is that **the number is meaningless without the number of looks attached.** A $p<0.05$ from a pre-registered single analysis and a $p<0.05$ from the fifth of ten peeks are different measurements wearing the same label.

Note the sharp contrast with (a) and (b): the *same* peeking that leaves the Bayesian posterior and its coverage untouched inflates the frequentist error rate ninefold. Nothing contradicts — they measure different things. The posterior is a statement about $\theta$ given the data you have; the Type-I rate is a statement about a procedure over data you don't.

### (d) Selective reporting breaks calibration for everyone

Here the tables turn on the Bayesian. Optional stopping was safe because the stopping rule was a function of the data you kept. **Selective reporting** — running many experiments and publishing only the "significant" ones — conditions on an event that is informative about $\theta$, and *that* breaks calibration, in both paradigms, whenever your analysis prior is not the true effect distribution. Model a realistic world: 90% of tested effects are truly null, the rest are real; analysts use a diffuse (flat) prior, so their credible interval coincides with the frequentist confidence interval. Publish a study only if that interval excludes 0.

```python
g = np.random.default_rng(0)
reps, n_study, sigma = 200000, 25, 1.0
is_null = g.random(reps) < 0.90                         # spike-and-slab truth
theta = np.where(is_null, 0.0, g.normal(0, 2.0, reps))  # 90% nulls, 10% real
ybar = g.normal(theta, sigma / np.sqrt(n_study))
se = sigma / np.sqrt(n_study)
lo, hi = ybar - z * se, ybar + z * se                   # flat-prior CI == freq CI
cover = (lo <= theta) & (theta <= hi)
published = np.abs(ybar) > z * se                        # "significant" -> published
print(f"coverage, ALL studies           : {cover.mean():.4f}")
print(f"coverage, PUBLISHED only         : {cover[published].mean():.4f}"
      f"   ({published.sum()} of {reps} published)")
print(f"published mean |estimate|        : {np.abs(ybar[published]).mean():.3f}"
      f"  vs mean |true effect| {np.abs(theta[published]).mean():.3f}")
```

Across all studies coverage is a healthy `0.9503`; among the *published* ones it collapses to `0.6197`, with published estimates averaging `1.378` in magnitude against a true `1.202` — the winner's curse (module 18) made visible. The confidence interval and the flat-prior credible interval are the same interval here, so **both paradigms fail together**: selecting on significance selects the lucky-large estimates, whose intervals miss the truth. This is the honest boundary of claim (b): prior-averaged coverage survives stopping rules that depend on the *data* but fails the moment the reporting filter carries information about $\theta$ that your prior did not anticipate. A Bayesian whose prior *matched* the 90%-null truth would be protected (their posterior shrinks the noise back toward 0 — module 18's job); a diffuse-prior Bayesian is as exposed as the frequentist. Calibration is a property of the *model plus the reporting process*, not of the paradigm.

**The honest Bayesian caveat — foregone conclusions for Bayes factors.** Estimation is robust to stopping (claims a, b); *testing a point null* has one residual sensitivity worth naming. Under a true null, the Bayes factor $\mathrm{BF}_{10}$ for $H_1:\mu\sim N(0,\tau^2)$ against $H_0:\mu=0$ is a nonnegative martingale with mean 1, so Ville's inequality caps the chance of ever manufacturing strong evidence against a true null: $P(\sup_n \mathrm{BF}_{10}\ge k)\le 1/k$.

```python
g = np.random.default_rng(0)
reps, N, tau2 = 20000, 1000, 1.0
y = g.normal(0.0, 1.0, (reps, N))                # true null mu = 0
S1 = np.cumsum(y, axis=1); S2 = np.cumsum(y * y, axis=1); ns = np.arange(1, N + 1)
del y
# log Bayes factor at every n; BF10 = m1/m0, closed form for a Gaussian point-null test
logBF = 0.5 * (tau2 * S1**2 / (1 + ns*tau2) - np.log(1 + ns*tau2))
supBF = np.exp(logBF).max(axis=1)
print(f"P(sup_n BF10 >= 10 | H0 true) = {(supBF >= 10).mean():.4f}  (Ville bound 1/10 = 0.1000)")
```

The simulated probability is `0.0598`, safely under the `0.1000` bound: you *cannot* peek your way to fake evidence against a true null. The caveat is the mirror image, and it is the module-17 Lindley point wearing a design hat: the *magnitude* of $\mathrm{BF}_{01}$ (evidence *for* the null) grows without bound as the alternative $\tau\to\infty$, so with a diffuse enough $H_1$ you can drive $\mathrm{BF}_{01}$ over any threshold and "conclude" the null even when a small real effect exists — a foregone conclusion baked into the prior width, not the data. The Bayes factor's honesty is only as good as the alternative you were willing to specify (module 17). Estimation posteriors have no such knob; point-null tests do.

## 23.4 The 2³ factorial: effects are contrasts are regression coefficients

Montgomery's Example 6.1: a $2^3$ factorial to develop a nitride-etch process, three factors each at two levels — $A$ = electrode gap, $B$ = C₂F₆ gas flow, $C$ = RF power — replicated twice, response = etch rate (Å/min). Eight treatment combinations, 16 runs. The classical analysis computes an *effect* for each factor and interaction as a contrast of the cell means; the Bayesian analysis fits a regression on the $\pm1$-coded design. **They are the same computation.** Code each factor as $\mp1$ (low/high), build the design matrix with all interaction columns (products of main-effect columns), and the regression coefficient on a coded column is exactly half the Montgomery "effect" (half, because the coded variable moves two units, $-1\to+1$, per unit of effect).

```python
# Montgomery Example 6.1 nitride-etch data (Table 6.4), two replicates per cell.
cells = {"(1)": [550, 604], "a": [669, 650], "b": [633, 601], "ab": [642, 635],
         "c": [1037, 1052], "ac": [749, 868], "bc": [1075, 1063], "abc": [729, 860]}
order = ["(1)", "a", "b", "ab", "c", "ac", "bc", "abc"]
def coded(nm):
    A = 1 if "a" in nm else -1
    B = 1 if "b" in nm else -1
    C = 1 if "c" in nm else -1
    return (A, B, C) if nm != "(1)" else (-1, -1, -1)
rows, y = [], []
for nm in order:
    A, B, C = coded(nm)
    for val in cells[nm]:
        rows.append([1, A, B, C, A*B, A*C, B*C, A*B*C]); y.append(val)
X = np.array(rows, float); y = np.array(y, float)
labels = ["I", "A", "B", "C", "AB", "AC", "BC", "ABC"]

beta_ols, *_ = np.linalg.lstsq(X, y, rcond=None)   # regression coefficients
effects = 2 * beta_ols                             # Montgomery "effect" = 2 x coef
for lab, ef in zip(labels, effects):
    print(f"  {lab:>3}: effect {ef:+9.4f}")
print(f"Montgomery's headline effects -> A (gap) {effects[1]:.3f}, "
      f"C (power) {effects[3]:.3f}, AC {effects[5]:.3f}")
```

The regression reproduces Montgomery's published effects to the digit: $A=`-101.6250`$, $C=`306.1250`$, and the gap–power interaction $AC=`-153.6250`$ dominate; $B$, $AB$, $BC$, $ABC$ are noise-sized. That the estimates are *exactly* the textbook contrasts is not luck — with an orthogonal $\pm1$ design, $X^\top X$ is diagonal, so each least-squares coefficient is an independent contrast, and least squares, method-of-moments, and the flat-prior posterior mean all coincide. The interaction reading: $AC=-153.6$ means the effect of power depends on the gap (and vice versa) — you cannot optimize the two knobs independently, which is precisely what a one-factor-at-a-time search would have missed.

**Effect sparsity as a prior.** The engineering folklore that "only a few effects are real" (Montgomery's *sparsity-of-effects principle*) is a *prior*: most coefficients are noise. A *single* Normal prior cannot express it — one scale would shrink every effect by the same factor and so cannot be simultaneously tight for the null effects and loose for the real ones. A **spike-and-slab** prior can: each effect is either noise (a narrow spike at zero, scale ≈ the coefficient's own standard error) or real (a diffuse slab). The posterior assigns each effect an *inclusion probability* — $P(\text{slab})$, the chance it is real — and shrinks it toward zero in proportion to how much it looks like noise. Because the design is orthogonal, each effect's likelihood is an independent Gaussian, so the whole thing is a closed-form two-component conjugate update, no MCMC.

```python
resid = y - X @ beta_ols
s2 = resid @ resid / (len(y) - X.shape[1])          # replicate-based noise variance
v = s2 / np.diag(X.T @ X)                            # per-coef likelihood variance (diagonal design)
tau0 = np.sqrt(v[1])                                 # spike: scale of a noise effect
tau1, w = 80.0, 0.5   # slab on the order of the real effects (coef ~50-150); P(real) = 1-w

def sparse_shrink(bhat, vj):                         # 2-component Gaussian-mixture posterior
    m0 = tau0**2 / (tau0**2 + vj) * bhat             # posterior mean | spike
    m1 = tau1**2 / (tau1**2 + vj) * bhat             # posterior mean | slab
    l0 = w * stats.norm.pdf(bhat, 0, np.sqrt(tau0**2 + vj))
    l1 = (1 - w) * stats.norm.pdf(bhat, 0, np.sqrt(tau1**2 + vj))
    p_slab = l1 / (l0 + l1)                          # posterior inclusion probability
    return (1 - p_slab) * m0 + p_slab * m1, p_slab

beta_shrunk = np.zeros(8); p_slab = np.zeros(8)
print("effect      raw     shrunk   P(real)")
for i in range(1, 8):
    beta_shrunk[i], p_slab[i] = sparse_shrink(beta_ols[i], v[i])
    print(f"  {labels[i]:>3}: {2*beta_ols[i]:+9.3f} {2*beta_shrunk[i]:+9.3f}   {p_slab[i]:.3f}")

fig, ax = plt.subplots()
idx = np.arange(1, 8)
ax.bar(idx - 0.18, 2*beta_ols[1:], 0.36, color="C1", label="raw effect")
ax.bar(idx + 0.18, 2*beta_shrunk[1:], 0.36, color="C0", label="shrunk (spike-and-slab)")
for k, i in enumerate(idx):
    ax.annotate(f"{p_slab[i]:.2f}", (i, 2*beta_ols[i]), ha="center",
                va="bottom" if beta_ols[i] > 0 else "top", fontsize=8)
ax.axhline(0, color="black", lw=0.8)
ax.set_xticks(idx); ax.set_xticklabels(labels[1:])
ax.set_ylabel("effect (Å/min)")
ax.set_title("Effect sparsity as a prior: inclusion probabilities (labels) select A, C, AC")
ax.legend()
save(fig, "factorial_effects")
```

![Raw vs spike-and-slab-shrunk effects for the 2³ etch experiment; inclusion probabilities (bar labels) select A, C, and AC and shrink the rest.](figures/23-experimental-design/factorial_effects.png)

The inclusion probabilities do the model selection: $A$, $C$, $AC$ come back at $P(\text{real}) = `0.943`,\ `1.000`,\ `1.000`$ and barely shrink, while $B$, $AB$, $BC$, $ABC$ sit at $`0.175`$–$`0.213`$ and are pulled hard toward zero (the $AB$ effect roughly halves, `-24.875` → `-14.967`). The slab scale 80 was set to the order of the real coefficients (≈50–150 on the coef scale); vary it a few-fold and the individual probabilities wobble, but the *ordering* — A, C, AC in, the rest out — is what's robust, and it is the decision the prior is there to make. This is the same partial-pooling arithmetic as module 16 — but with a heavy-tailed (mixture) prior instead of one Gaussian scale, it delivers genuine sparsity rather than uniform softening. The continuous, exact-zeros-in-the-mode cousin is the horseshoe (module 18); the spike-and-slab makes the logic legible in closed form on an orthogonal design.

## 23.5 Pricing information before you buy it

Design chooses *where to measure*, and measurements are worth different amounts. Two ways to price "worth" — expected information gain (nonlinear models) and D-optimality (linear) — are the same idea from two sides.

**Expected information gain.** You are running a logistic dose–response, $p(y{=}1\mid d)=\sigma(a+bd)$, and after a small pilot you hold a posterior over $(a,b)$. Where should the *next* dose go? The Bayesian-optimal design maximizes the expected reduction in posterior entropy, equivalently the mutual information between the parameters and the not-yet-seen outcome at design $d$:
$$\text{EIG}(d) = H\!\big(\mathbb{E}_\theta[p(y\mid d,\theta)]\big) - \mathbb{E}_\theta\big[H(p(y\mid d,\theta))\big],$$
with $H$ the binary entropy. Both terms are exact quadratures over a grid representing the posterior — no MCMC. The first term is the outcome uncertainty you *have*; the second is the uncertainty that would *remain* if you knew $\theta$; their difference is what the observation teaches you.

**Predict.** Your pilot has localized the dose–response reasonably well. Does EIG want the next dose (a) at the extreme high end (biggest response), (b) at the extreme low end (cleanest control), or (c) somewhere in the middle, near where the outcome is a coin flip?

```python
from scipy.special import expit
ag = np.linspace(-4, 4, 81); bg = np.linspace(0.05, 4, 80)
A2, B2 = np.meshgrid(ag, bg, indexing="ij")
logW = stats.norm(0, 2).logpdf(A2) + stats.norm(1, 0.8).logpdf(B2)   # broad prior
g = np.random.default_rng(0)
a_true, b_true = -1.0, 1.5
pilot_d = np.array([-2., -1., 0., 1., 2.])
pilot_y = (g.random(len(pilot_d)) < expit(a_true + b_true * pilot_d)).astype(int)
for d, yy in zip(pilot_d, pilot_y):                 # conjugate-free grid Bayes update
    p = expit(A2 + B2 * d)
    logW += np.log(np.where(yy == 1, p, 1 - p))
W = np.exp(logW - logW.max()); W /= W.sum()

def Hb(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return -(p * np.log(p) + (1 - p) * np.log(1 - p))

doses = np.linspace(-4, 4, 33)
eig = np.array([float(Hb((W * expit(A2 + B2 * d)).sum()) - (W * Hb(expit(A2 + B2 * d))).sum())
                for d in doses])
best = doses[eig.argmax()]
ed50 = -(W * A2).sum() / (W * B2).sum()
print(f"posterior-mean ED50 (dose with p=0.5): {ed50:.3f}")
print(f"EIG-optimal next dose               : {best:.3f}  (EIG {eig.max():.4f} nats)")
print(f"EIG at the extremes d=-4 / d=+4     : {eig[0]:.4f} / {eig[-1]:.4f} nats")

fig, ax = plt.subplots()
ax.plot(doses, eig, "o-", color="C0", label="EIG(d)")
ax.axvline(best, color="C3", ls="--", lw=1.4, label=f"best dose {best:.2f}")
ax.axvline(ed50, color="black", ls=":", lw=1, label=f"posterior ED50 {ed50:.2f}")
ax.set_xlabel("candidate dose $d$"); ax.set_ylabel("expected information gain (nats)")
ax.set_title("Measure where you're most uncertain — EIG peaks near the ED50")
ax.legend()
save(fig, "eig_dose")
```

![Expected information gain against candidate dose: it peaks near the posterior ED50 and is near-zero at the saturating extremes.](figures/23-experimental-design/eig_dose.png)

**Reconcile.** Answer (c): EIG peaks at dose `-0.750`, in the same uncertain-middle region as the posterior ED50 of `-0.373` (a 0.38 gap — about a grid cell and a half; the EIG surface is flat near its top) — where your model puts $p\approx0.5$ and the outcome is most uncertain. The extremes are nearly worthless (`0.0544` and `0.0313` nats) because you are already sure what happens there — a subject at a saturating dose almost certainly responds, teaching you nothing about the parameters. *Information lives where uncertainty lives.* This is the acquisition-function logic behind Bayesian optimization and active learning: don't sample where you already know the answer.

**D-optimality — the linear-model special case.** For a linear model with a flat prior, the posterior covariance is $\sigma^2(X^\top X)^{-1}$, so "most informative design" = "smallest posterior-covariance determinant" = "largest $\det(X^\top X)$". This criterion is called **D-optimality**, and it makes the factorial-vs-OFAT argument quantitative. Compare a $2^2$ factorial (all four corners) against one-factor-at-a-time (a baseline, move $x_1$, move $x_2$, replicate the baseline) — same four runs each, main-effects model.

```python
def dets(X):
    return np.linalg.det(X.T @ X)
factorial = np.array([[1, -1, -1], [1, 1, -1], [1, -1, 1], [1, 1, 1]], float)
ofat = np.array([[1, -1, -1], [1, 1, -1], [1, -1, 1], [1, -1, -1]], float)
df, do = dets(factorial), dets(ofat)
cov_ratio = np.linalg.det(np.linalg.inv(ofat.T @ ofat)) / np.linalg.det(np.linalg.inv(factorial.T @ factorial))
print(f"det(XtX): factorial {df:.1f}, OFAT {do:.1f}, ratio {df/do:.3f}")
print(f"posterior-covariance det ratio (OFAT / factorial): {cov_ratio:.3f}")
```

The factorial's $\det(X^\top X)=`64.0`$ against OFAT's `32.0` — a ratio of `2.000`, and the posterior-covariance determinant is correspondingly `2.000`× larger for OFAT. Same number of runs, twice the volume of parameter uncertainty from the one-at-a-time plan, and OFAT cannot see the $AC$ interaction that dominated the etch process at all. The factorial is D-optimal because its columns are orthogonal — the design analogue of the diagonal $X^\top X$ that made the effects independent contrasts in §23.4.

## 23.6 The design justifies the test — randomization inference

Module 01 promised that *exchangeability under the null is the entire assumption* behind a permutation test, and that the demo lived here. Cash it. You ran a two-group experiment with $n=15$ per arm and randomized assignment. Under the sharp null "treatment does nothing," the label attached to each unit is arbitrary — the randomization made the two groups exchangeable, so every relabeling of the observed responses was *equally likely to have been the one you saw*. That is not an assumption about normal distributions; it is a fact about how you assigned treatment. The permutation null distribution of the mean difference is built by enumerating (here, sampling) relabelings, and the $p$-value is the fraction at least as extreme as observed.

```python
g = np.random.default_rng(2)
nA = nB = 15
A = g.normal(20.0, 2.0, nA); B = g.normal(22.0, 2.0, nB)     # true shift +2
obs = B.mean() - A.mean()
pool = np.concatenate([A, B]); Ntot = len(pool)
nperm = 20000
idx = np.array([g.permutation(Ntot) for _ in range(nperm)])
perm = pool[idx[:, nA:]].mean(1) - pool[idx[:, :nA]].mean(1)
p_perm = float((np.abs(perm) >= abs(obs)).mean())
_, p_t = stats.ttest_ind(B, A)
print(f"observed difference in means : {obs:.3f}")
print(f"permutation p-value          : {p_perm:.4f}  (nperm={nperm})")
print(f"two-sample t-test p-value    : {p_t:.4f}")

fig, ax = plt.subplots()
ax.hist(perm, bins=50, density=True, color="C0", alpha=0.6, label="permutation null")
ax.axvline(obs, color="C3", lw=2, label=f"observed {obs:.2f}")
ax.axvline(-obs, color="C3", lw=2, ls="--")
ax.set_xlabel("mean difference under relabeling"); ax.set_ylabel("density")
ax.set_title("The design builds the null: relabelings you could equally have seen")
ax.legend()
save(fig, "permutation_null")
```

![The permutation null distribution of the mean difference, built from relabelings; the observed difference sits far in the tail (p ≈ 0.031).](figures/23-experimental-design/permutation_null.png)

The permutation $p$-value is `0.0311`, essentially identical to the $t$-test's `0.0313`. When the normal-theory assumptions happen to hold the two agree — but the permutation test *never needed them*. It needs only exchangeability under the null, and randomization *manufactured* that exchangeability. This closes the module's loop: the design that bought ignorability in §23.1 is the same design that licenses the test here. **The design justifies the test** — reference distributions come from how you collected the data, not from a distributional article of faith.

## Bridge — Montgomery, the booklet, and the decision frame

Montgomery's classical DOE machinery is, line by line, Bayesian conditioning on a well-chosen joint: effects are flat-prior posterior means, effect sparsity is a shrinkage prior (§23.4), optimal designs minimize posterior-covariance determinants (§23.5), and Lindley's information-theoretic program (booklet ch. 6–7) supplies the EIG criterion that generalizes D-optimality to nonlinear models. The module is the design-stage half of the decision frame: module 22 asked "given this posterior, what should I do?"; this one asks "given what I might learn, what should I measure?" — the same expectation, over data you don't yet have.

## Pitfalls

- **Believing that "Bayesians can ignore the stopping rule" means "design doesn't matter."** The likelihood principle governs *post-data inference*; it says nothing about which likelihood is *true*, and that is set by the assignment mechanism (§23.1) and priced by the design criterion (§23.5). Randomization is not a frequentist ritual — it is what makes your written-down likelihood the real one.
- **Quoting a Type-I rate without the number of looks.** "$p<0.05$" from a single pre-registered analysis and from the fifth of ten peeks are different measurements (`0.05` vs an effective `0.2044`). Always state the monitoring plan; a $p$-value inherits its meaning from the design's sample space.
- **Confusing optional stopping with selective reporting.** Stopping when *you* like leaves the Bayesian posterior and its coverage intact (§23.3a,b); publishing only *significant* studies breaks calibration for everyone (§23.3d). The first conditions on data you keep; the second conditions on an event that is informative about $\theta$.
- **Designing for power at a point you don't know.** Power at the "expected" effect systematically overstates your chance of success because power is concave over plausible effects; report assurance (§23.2).
- **One-factor-at-a-time optimization.** OFAT wastes half the information of a factorial of the same size (D-ratio `2.000`, §23.5) and is *blind to interactions* — it would never have found the gap–power coupling that dominated Montgomery's etch process.
- **Treating a diffuse alternative as "objective" in a Bayes-factor test.** The evidence *for* a null scales with the alternative's width (Lindley, module 17); with a vague enough $H_1$ you can foregone-conclude the null. Estimation has no such knob — prefer it when you can.

## Exercises

**Exercise 23.1 — The peek that doesn't cost you (predict-then-run).**
*Setup:* Rerun the §23.3b coverage simulation, but make the stopping rule even greedier: stop the instant the 95% credible interval excludes 0 *or* at $n=30$ (a hard budget), whichever comes first.
*Predict:* Will prior-averaged coverage (a) fall clearly below 0.95 because the budget forces you to stop early on inconclusive runs, or (b) stay at ≈0.95?
*Reason:* the intuition "early stopping on noise must hurt coverage" — the same intuition that (correctly) predicts frequentist inflation.
*Run:*
```python
g = np.random.default_rng(1)
reps = 40000; theta = g.normal(0, 1, reps)
y = g.normal(theta[:, None], 1.0, (reps, 30)); cs = np.cumsum(y, 1); ns = np.arange(1, 31)
prec = 1 + ns; m = cs / prec; sd = np.sqrt(1 / prec)
excl = np.abs(m) > stats.norm.ppf(0.975) * sd
first = np.where(excl.any(1), excl.argmax(1), 29)
mm = m[np.arange(reps), first]; ss = sd[first]
cov = np.mean((mm - 1.96 * ss <= theta) & (theta <= mm + 1.96 * ss))
print(f"coverage under greedy stop with hard budget 30: {cov:.4f}")
```
<details><summary>Reconcile</summary>

Coverage stays at nominal: `0.9514`. The budget and the greedy rule are both functions of the *data* — they never peek at $\theta$ — so conditioning on "the interval you finally reported" still leaves $P(\theta\in\text{CI}\mid\text{data})=0.95$ for every realized dataset, and the average over datasets is 0.95. This is claim (b) again: the martingale property of the posterior does not care *when* you stop, only that the rule is adapted to the data. The frequentist intuition "early stopping on noise hurts" is right about the *Type-I rate* (an average over hypothetical repetitions) and wrong about *credible-interval coverage* (a statement conditioned on the data you have). Two different guarantees; the peek breaks one and not the other.
</details>

**Exercise 23.2 — Assurance and the null-effect prior (predict-then-run).**
*Setup:* Keep the §23.2 design ($n=63$ per arm, 80% power at $\delta=0.5$) but now your prior admits a real chance the treatment does nothing: $\delta=0$ with probability 0.3, else $\delta\sim N(0.5,0.2^2)$.
*Predict:* Rank from smallest to largest: (i) assurance under this spike-and-slab prior, (ii) assurance under the pure $N(0.5,0.2^2)$ prior (`0.7140`), (iii) power at 0.5 (`0.8013`).
*Reason:* averaging power against a prior that includes the null.
*Run:*
```python
gd = np.linspace(-0.5, 1.5, 4001); w = stats.norm(0.5, 0.2).pdf(gd); w /= w.sum()
n_per = 63
assur_spike = 0.3 * power(0.0, n_per) + 0.7 * float(np.sum(w * power(gd, n_per)))
print(f"power@0.5 {power(0.5,n_per):.4f} | slab assurance {float(np.sum(w*power(gd,n_per))):.4f} "
      f"| spike-slab assurance {assur_spike:.4f}")
```
<details><summary>Reconcile</summary>

The ranking is (i) spike-slab `0.5148` < (ii) slab `0.7140` < (iii) point power `0.8013`. Putting 30% mass on a true null drags assurance down hard, because power at $\delta=0$ is just the Type-I rate `0.05` — a study run on a null effect "succeeds" only by false positive. Assurance mercilessly exposes the cost of the possibility that there is nothing to find, which point-power hides by assuming the effect is real and exactly 0.5. This is why assurance, not power, is the number to bring to a go/no-go decision: it prices the risk that the experiment is chasing a ghost.
</details>

**Exercise 23.3 — Active learning is EIG (ML connection, predict-then-run).**
*Setup:* In the §23.5 dose problem, a colleague proposes always sampling the dose whose predicted response is closest to a coin flip ($p=0.5$), i.e. the current posterior-mean ED50 — a pure "uncertainty sampling" heuristic from active learning. Compare that dose's EIG to the true EIG-optimal dose.
*Predict:* Will uncertainty sampling (a) match the EIG optimum almost exactly, (b) be noticeably worse, or (c) be catastrophically worse?
*Reason:* uncertainty sampling targets outcome uncertainty $H(\mathbb{E}_\theta[p])$; EIG targets *reducible* uncertainty $H(\mathbb{E}_\theta[p]) - \mathbb{E}_\theta[H(p)]$.
*Run:*
```python
d_us = ed50                                   # uncertainty sampling: dose at posterior ED50
eig_us = float(Hb((W * expit(A2 + B2 * d_us)).sum()) - (W * Hb(expit(A2 + B2 * d_us))).sum())
print(f"EIG at uncertainty-sampling dose {d_us:.3f}: {eig_us:.4f} nats")
print(f"EIG at EIG-optimal dose         {best:.3f}: {eig.max():.4f} nats")
```
<details><summary>Reconcile</summary>

They nearly coincide (EIG `0.1065` vs `0.1078` nats at doses `-0.373` and `-0.750`) — answer (a), *in this problem*. When the posterior over $(a,b)$ is fairly concentrated, the two terms in EIG track each other and "sample where the outcome is uncertain" is a good proxy for "sample where you'll learn most." But the equivalence is not a theorem: outcome entropy also spikes where you are ignorant of $\theta$ yet the observation would be uninformative (e.g. a dose where *no* setting of $\theta$ predicts the outcome well). EIG subtracts off exactly that irreducible part. Uncertainty sampling is the cheap heuristic; EIG is the quantity it is approximating — the same relationship as MAP to full posterior, or a plug-in acquisition to the real value of information.
</details>

**Exercise 23.4 — Reading an interaction (predict-then-run).**
*Setup:* In Montgomery's etch data, the $AC$ (gap × power) effect is `-153.6250`. You want high etch rate. You have found that high power ($C=+1$) raises the rate strongly.
*Predict:* To *maximize* etch rate, should you set the gap $A$ to its high level ($+1$) or low level ($-1$) — and does the answer depend on the power level?
*Reason:* main effects read in isolation vs. main effects plus interaction.
*Run:*
```python
def predict_rate(A, C):        # B set to 0; use fitted coefs
    xb = beta_ols[0] + beta_ols[1]*A + beta_ols[3]*C + beta_ols[5]*A*C
    return xb
for A in (-1, 1):
    for C in (-1, 1):
        print(f"  gap A={A:+d}, power C={C:+d}: predicted rate {predict_rate(A, C):.1f}")
```
<details><summary>Reconcile</summary>

Set the gap *low* ($A=-1$) and power *high* ($C=+1$): that corner gives the top predicted rate. The main effect of $A$ is negative (`-101.625`, low gap already helps), but the real story is the interaction — at high power the gain from lowering the gap is amplified by the $-153.6$ $AC$ term, because $A\cdot C = (-1)(+1) = -1$ multiplies the negative coefficient into a positive contribution. A one-factor-at-a-time study that fixed power at its low level while tuning the gap would have measured a *weaker* gap effect and completely missed that gap and power must be set jointly. Interactions are why you run factorials: the best setting of one knob depends on the others, and only a crossed design can see it.
</details>

## Takeaways

- **Design writes the likelihood; inference only reads it.** A Bayesian is indifferent to *stopping* rules but not to *assignment* rules — randomization buys ignorability, "the likelihood you wrote is the likelihood you got," and a confounded fit is confidently wrong (`5.288` vs a true `2`) while the randomized fit is right (`2.010`).
- **Power is a point; assurance is the average.** Because power is concave over plausible effects, assurance (`0.7140`) sits below point-power (`0.8013`) even with a prior centered on the design point — and collapses further if the null is possible. Report assurance for go/no-go.
- **Optional stopping: four claims, four verdicts.** (a) the posterior is unchanged (likelihood identity); (b) prior-averaged coverage survives (`0.9494`, martingale); (c) frequentist Type-I inflates — `0.2044` at 10 looks (≈4×), `0.4664` under continuous monitoring (≈9×), diverging by the LIL; (d) *selective reporting* breaks calibration for everyone (published coverage `0.6197`). Always state the number of looks.
- **The Bayes-factor caveat.** Ville's bound stops you manufacturing evidence *against* a true null ($P(\sup\mathrm{BF}_{10}\ge10)=`0.0598`\le0.1$), but a diffuse alternative lets you foregone-conclude *for* the null (Lindley, module 17). Estimation posteriors have no such knob.
- **Factorial effects are regression coefficients.** On a $\pm1$-coded orthogonal design the least-squares coefficient is exactly half Montgomery's contrast ($A=`-101.6250`$, $C=`306.1250`$, $AC=`-153.6250`$); effect sparsity is a shrinkage prior; interactions are why one-factor-at-a-time fails.
- **Information has a price you can compute first.** EIG picks the measurement where uncertainty is *reducible* (the dose near the ED50, `-0.750`); D-optimality (max $\det X^\top X$) is its flat-prior linear special case — the $2^2$ factorial beats OFAT by a determinant ratio of `2.000`.
- **The design justifies the test.** Randomization manufactures exchangeability under the null, which is the *entire* content of a permutation test (p `0.0311`, matching the $t$-test's `0.0313` when normality happens to hold, but assuming none of it).
</content>
</invoke>

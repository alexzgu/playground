# 26. One Theory, Two Audits

> **Spine.** One calculus — a joint distribution plus conditioning — answers every question in the course; two audit cultures — post-data belief and pre-data procedure guarantees — check the answer, and the working statistician runs both.
> **Which line?** All four, in retrospect: this module is where you read the whole course back as a single sentence and learn where its two audits agree and where they split.
> **Promise.** You can take any procedure — one you were taught, or one you meet next year — and place it: which of the four lines it implements, what approximation it makes, and which audit will catch it when it lies.
> **Prereqs.** Everything. **Runtime.** ~29 s.
> **Sources.** The whole course; Rubin/Little (calibrated Bayes) and Vovk et al. (conformal) by concept; the reading map in §26.5.

The course was one claim, twenty-six times:

1. **A model is a joint distribution** $p(\text{unknowns}, \text{knowns})$.
2. **Inference is conditioning:** $p(\text{unknowns} \mid \text{knowns})$.
3. **Prediction is marginalization:** $p(\text{new} \mid \text{knowns}) = \int p(\text{new}\mid\text{unknowns})\,p(\text{unknowns}\mid\text{knowns})$.
4. **A decision minimizes posterior expected loss.**

Everything else — MLE, ridge, the Kalman filter, dropout, conformal — was a special case, an approximation, or an *audit* of these four lines. The last skill is knowing there are exactly two ways to check a probabilistic claim, and using both.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "26-capstone"                     # this module's figure dir
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

## 26.1 The ledger: six times the two audits split

The two audits are **the posterior** (post-data belief, conditioned on what you saw) and **the sampling distribution** (procedure behavior over datasets you might have seen). Bernstein–von Mises (M08) says that in the well-specified, fixed-dimension, large-$n$ interior case they agree — a weak-prior 95% credible set has `0.9499` frequentist coverage. The hardest lessons live where they *disagree*. Every ledger row is a claim, the module where you ran it, and the number you saw.

```python
# The ledger, echoed with the canonical numbers each module printed.
rows = [
    ("nuisance: marginalize vs profile", "26 (below)", "t cov 0.95 vs plug-in 0.89"),
    ("stopping rule: posterior invariant", "M23", "seq-vs-closed gap 1.00e-08"),
    ("stopping rule: martingale coverage", "M23", "0.9494 under aggressive stopping"),
    ("stopping rule: frequentist Type-I", "M23", "0.0522 -> 0.2044 at 10 looks"),
    ("conditional coverage (2-pt uniform)", "M06", "marginal 0.500, cond 1.000 at R=0.9"),
    ("Lindley: p rejects, BF favors H0", "M17", "p=0.0099, BF01 1.80 -> 17.93"),
    ("misspecification: width is wrong", "M18", "post sd 0.0739, sandwich 0.1019, true 0.1046"),
    ("calibration: ECE audit", "M15", "0.0207 calibrated vs 0.0401 plug-in"),
]
w = max(len(r[0]) for r in rows)
print("BvM baseline: weak-prior 95% credible set covers 0.9499 frequentially (M08)")
for claim, mod, num in rows:
    print(f"{claim:<{w}}  [{mod:<10}]  {num}")
```

Two mechanisms bear spelling out. **Stopping rules (M23):** $\theta$-independent stopping cancels in the likelihood (M04), so the posterior (sequential vs closed-form gap `1.00e-08`) and its prior-averaged coverage (`0.9494`) are untouched, while the frequentist Type-I error explodes to `0.2044` at ten looks. **Lindley (M17):** the diffuse alternative pays an Occam tax $p$ cannot see — $\mathrm{BF}_{01}$ climbs from `1.80` to `17.93` *for* the null the test rejects at $p=$ `0.0099`. The other rows the ledger carries itself: conditional coverage is $r/(1-r)$ for $r<\tfrac12$ and capped at 1 above — a certain `1.000` at $R=0.9$ (M06); the misspecified posterior's sd `0.0739` vs the sandwich audit's `0.1019` and the true `0.1046` — right about a wrong model (M18); calibrated ECE `0.0207` vs overconfident plug-in `0.0401` (M15). The constant pattern: the posterior is what to believe; the sampling distribution is how to check it.

The first row is this module's one new computation.

**Setup.** $n=6$ draws, mean $\mu$ and variance $\sigma^2$ both unknown — the NIG world of M05 under $\pi(\mu,\sigma^2)\propto 1/\sigma^2$. You want a 95% interval for $\mu$; $\sigma^2$ is a **nuisance** you cannot ignore. Two moves: *marginalize* it (integrate $\sigma^2$ out — line 3 — turning $\mu\mid y$ into a Student-$t_{n-1}$), or *profile/plug in* (fix $\hat\sigma^2$ and treat $\mu\mid y$ as Normal with $\sigma^2$ "known").

**Predict.** *Intuition:* "$n=6$ estimates $\sigma^2$ fine; plugging in should barely differ, both covering 95%." How much wider is the honest $t$, and does the plug-in Normal still cover 95%?

```python
# Reference NIG posterior:  sigma^2 | y ~ IG((n-1)/2, S/2),  mu | sigma^2,y ~ N(xbar, sigma^2/n).
def ref_nig(y):
    n = len(y); xbar = y.mean(); S = ((y - xbar) ** 2).sum()
    return n, xbar, (n - 1) / 2, S / 2       # kn, mn, an, bn

y = rng.normal(10.0, 3.0, size=6)            # one small sample; sigma unknown
kn, mn, an, bn = ref_nig(y)

# ROUTE 1 -- marginalize sigma^2:  mu | y ~ t_{2an}(mn, bn/(an*kn)).  (module 05's NIG->t)
df = 2 * an
scale = np.sqrt(bn / (an * kn))
lo_t, hi_t = stats.t(df, mn, scale).ppf([0.025, 0.975])

# ROUTE 2 -- profile / plug-in:  fix sigma^2 = s^2, then mu | y ~ N(mn, s^2/kn).
s2 = ((y - mn) ** 2).sum() / (kn - 1)        # unbiased sigma^2 estimate
sd = np.sqrt(s2 / kn)
lo_n, hi_n = stats.norm(mn, sd).ppf([0.025, 0.975])

print(f"df = {df:.0f},  center mn = {mn:.3f}")
print(f"marginalize sigma^2 (Student-t):   [{lo_t:.3f}, {hi_t:.3f}]  width {hi_t-lo_t:.3f}")
print(f"profile sigma^2 (plug-in Normal):  [{lo_n:.3f}, {hi_n:.3f}]  width {hi_n-lo_n:.3f}")
print(f"width ratio t / Normal = {(hi_t-lo_t)/(hi_n-lo_n):.3f}")

# Which interval keeps its 95% promise? Replay the experiment (the frequentist audit).
rc = np.random.default_rng(999)
T = 20000
ct = cn = 0
for _ in range(T):
    d = rc.normal(10.0, 3.0, size=6)
    k2, m2, a2, b2 = ref_nig(d)
    lt, ht = stats.t(2*a2, m2, np.sqrt(b2/(a2*k2))).ppf([0.025, 0.975])
    s2d = ((d - m2)**2).sum() / (k2 - 1)
    ln, hn = stats.norm(m2, np.sqrt(s2d/k2)).ppf([0.025, 0.975])
    ct += lt <= 10.0 <= ht
    cn += ln <= 10.0 <= hn
print(f"coverage over {T} replays: marginalized-t {ct/T:.4f}   plug-in-Normal {cn/T:.4f}")

xg = np.linspace(mn - 4, mn + 4, 400)
fig, ax = plt.subplots()
ax.plot(xg, stats.t(df, mn, scale).pdf(xg), color="C1", lw=2, label="marginalize $\\sigma^2$ ($t_5$)")
ax.plot(xg, stats.norm(mn, sd).pdf(xg), color="C3", ls="--", lw=2, label="profile $\\hat\\sigma^2$ (Normal)")
ax.axvspan(lo_t, hi_t, color="C1", alpha=0.10)
ax.axvspan(lo_n, hi_n, color="C3", alpha=0.12)
ax.set_xlabel(r"$\mu$"); ax.set_ylabel("posterior density of the mean")
ax.set_title("Nuisance $\\sigma^2$: integrating it out is wider — and honest")
ax.legend()
save(fig, "marginalize-vs-profile")
```

**Reconcile.** The honest $t$ interval is `1.312`× *wider* (width `2.548` vs `1.943`); over 20,000 replays the plug-in covers only `0.8942`, not 0.95, while the marginalized $t$ holds `0.9508`. The mistake in "$n=6$ pins $\sigma^2$" is that with 5 degrees of freedom the uncertainty *in $\sigma^2$* feeds first-order into the uncertainty in $\mu$, and profiling discards it. This is the "$z$ vs $t$" rule you were handed years ago, now a theorem about integrating out a nuisance (line 3).

![Marginalizing the nuisance variance gives the wider Student-t; the plug-in Normal is narrower and under-covers.](figures/26-capstone/marginalize-vs-profile.png)

## 26.2 The ML zoo, audited

**Fill both blank columns, row by row, before opening the reveal.** *Reading* = the joint-plus-conditioning the procedure implements or approximates; *status* = **theorem** (exact identity), **approx** (bounded approximation), **heuristic** (rhymes with Bayes, no derivation), or **none**. The test only works if you are caught being wrong.

| Procedure | Your reading | Your status |
|---|---|---|
| OLS | | |
| Ridge | | |
| Lasso | | |
| Horseshoe | | |
| Logistic regression | | |
| SVM (hinge loss) | | |
| Decision tree | | |
| Random forest | | |
| Gradient boosting | | |
| BART | | |
| k-means | | |
| PCA / PPCA | | |
| Gaussian process | | |
| Kalman filter | | |
| MC-dropout | | |
| Deep ensembles | | |
| VAE | | |
| Diffusion model | | |
| Conformal prediction | | |
| Bootstrap | | |

<details><summary>Reveal — the audited table</summary>

| Procedure | Bayesian reading | Status | What it buys |
|---|---|---|---|
| OLS | posterior mean under Gaussian noise, flat prior | **theorem** | predictive $t$ intervals free (M14) |
| Ridge | posterior mean, $\beta\sim N(0,\sigma^2/\lambda I)$, $\lambda=\sigma^2/\tau^2$ | **theorem** | $\lambda$ is a learnable variance (M14) |
| Lasso | posterior **mode** under a Laplace prior | **theorem** (mode only) | mode is sparse, mean never is (M06) |
| Horseshoe | global–local shrinkage; posterior over which effects are real | **theorem** | multiplicity control free (M18) |
| Logistic reg. | Bernoulli-GLM MLE; Gaussian-prior MAP = weight decay | **theorem** | proper prior cures separation (M15) |
| SVM (hinge) | hinge is **not** a log-likelihood | **none** | max-margin is a rule, not a posterior |
| Decision tree | greedy partition, no coherent joint | **heuristic** | a point estimate of nothing |
| Random forest | bagged trees; resampling variance reduction | **heuristic** | disagreement = rough epistemic proxy |
| Grad. boosting | stagewise additive functional GD | **none/heuristic** | strong predictor, no posterior |
| BART | sum-of-trees with regularizing prior | **theorem** | the honest RF/boosting sibling |
| k-means | hard-EM limit of a spherical GMM ($\sigma\to 0$) | **approx** | soft GMM restores labels (M19) |
| PCA / PPCA | MLE of a linear-Gaussian latent model | **theorem** | gives PCA a likelihood |
| Gaussian process | Bayesian linear regression at $\infty$ basis functions | **theorem** | posterior over functions (M20) |
| Kalman filter | Normal-Normal update: predict=marginalize, update=condition | **theorem** | the gain *is* the shrinkage weight (M21) |
| MC-dropout | variational approx to a net posterior | **heuristic** | cheap; opaque $q$-family (M25) |
| Deep ensembles | samples from a multimodal weight posterior | **heuristic** (evidence) | best deep uncertainty in practice (M25) |
| VAE | amortized VI; ELBO with an inference net | **approx** | M13's ELBO with a neural $q$ (M25) |
| Diffusion | latent chain + score-following reverse SDE | **theorem** (process) | noising *is* a joint; score is approx (M25) |
| Conformal | finite-sample marginal coverage, exchangeability | **theorem** (model-free) | coverage with no likelihood — §26.3 |
| Bootstrap | posterior under Dirichlet(1,…,1) weights | **approx** | an implicit posterior (M08) |

The status column is the transferable skill: identities to lean on (ridge, Kalman, GP, logistic, PPCA, BART), approximations with a known failure mode (k-means, VAE, bootstrap), folklore that only *rhymes* with Bayes (dropout, ensembles, forests), and one — the SVM hinge loss — with **no** clean likelihood reading.
</details>

## 26.3 Conformal prediction, precisely

Conformal prediction is the odd entry: a useful uncertainty guarantee using *no* Bayesian machinery — the sampling-distribution audit at its limit. Every word is load-bearing. Split-conformal, given a fitted model and a held-out calibration set, produces a prediction set with **finite-sample, distribution-free, marginal coverage under exchangeability**: $P(Y_{n+1}\in C(X_{n+1}))\ge 1-\alpha$ for any distribution, any model, at any $n$.

**Finite-sample** — holds at $n=20$, no asymptotics. **Distribution-free** — no likelihood, no prior; the model can be arbitrarily wrong (it just yields wider sets). **Marginal** — averaged over calibration and test point, *not* conditional on $X_{n+1}=x$. **Exchangeability** is the entire assumption — M01's quiet train/test hypothesis, now load-bearing: calibration and test residuals are exchangeable, so a calibration quantile bounds the test residual.

Three consequences. **No conditional guarantee** — distribution-free conditional coverage is provably impossible (M06's marginal-vs-conditional split, model-free): 90% on average, never 90% *for this $x$*. **Breaks under shift** — void the moment train and test stop being exchangeable. **A model-free audit, not a model** — it wraps any predictor, a Bayesian posterior included. Build with the four lines; certify with conformal.

## 26.4 Bridge — the calibrated-Bayes stance

Rubin and Little's *calibrated Bayes* is not a compromise but a division of labor. **Bayesian for inference:** write the joint, condition, marginalize, decide — the posterior is the only object that coherently fuses prior structure, hierarchical borrowing, and every scrap of data. **Frequentist for evaluation:** audit that procedure with coverage, posterior predictive checks, reliability diagrams, sandwich variances, conformal wrappers. A model that fails its frequentist audit is wrong; a procedure with no generative story says nothing about *this* dataset. Run both.

| Problem X | Reach for Y (inference) | Audit with Z |
|---|---|---|
| Small-$n$ estimation with nuisances | full posterior, marginalize nuisances (M05/M26) | prior-averaged coverage; $t$-vs-plug-in gap (M06/M26) |
| A/B or ship decision | posterior expected loss; Thompson if sequential (M22) | Type-I under your stopping rule; EVSI vs cost (M23) |
| Thousands of parallel effects | hierarchical / empirical-Bayes shrinkage (M16/M18) | local-fdr ≈ P(null); BH at matched FDR (M18) |
| Black-box predictor, need uncertainty | Bayesian layer, deep ensemble, or GP (M20/M25) | reliability diagram + ECE; conformal set (M15/M26) |
| Causal question | potential-outcomes joint; identify before fitting (M24) | randomization / permutation; confounding sensitivity (M23) |

## 26.5 The reading map

What to read each source *for*.

- **Gelman et al., BDA3** — the center of gravity: ch. 5 (hierarchical, M16), 6–7 (model checking, M17), 11–13 (MCMC/variational, M10–M13).
- **MacKay, *ITILA*** — the *bits* view: Occam-as-evidence (M17; the GP marginal-likelihood razor, M20), the information backbone of M03, superb MCMC intuition. Free online.
- **Murphy, *PML1/PML2*** — the encyclopedic reference: PML1 for the GLM/mixture core (M14–M19), PML2 for GPs/VI/deep generative (M13/M20/M25).
- **Rasmussen & Williams, *GPML*** — the GP bible (M20): kernels, marginal likelihood, ML-II. Free online.
- **Särkkä, *Bayesian Filtering and Smoothing*** — state space as recursive Bayes (M21).
- **Efron, *Large-Scale Inference*** — empirical Bayes at scale (M18): two-groups, local fdr, when a prior stops being subjective.
- **Efron & Hastie, *CASI*** — the bridge itself: how frequentist, Bayesian, and predictive ideas relate — this module in book form.
- **Casella & Berger** — the rigor anchor, second pass: ch. 6 (likelihood principle, M04), 7 (estimation/loss, M05–M06), 8 (testing, M17), 10 (asymptotics/BvM, M08).
- **MA 556 booklet** — superseded but foundational: ch. 3–5 (conjugate), 9 (hierarchical), 10–11 (Gibbs/MH), 13–14 + stick-breaking insert (nonparametric), HMC/Stan insert (M12).
- **ISLP** ch. 3/6, 4/11, 5, 13; **Montgomery** ch. 1–6 (design, M23); **MCMT** ch. 3–5, 12 (mixing, M10); **Lawler** ch. 2–5 (SDEs behind Langevin/diffusion, M12/M25).

## Pitfalls

- **Posterior without the audit.** A coherent posterior over a misspecified model is coherently wrong; run the frequentist check (M18 sandwich, M15 calibration).
- **Audit without the posterior.** A $p$-value or coverage number grades a procedure, not a belief about *this* dataset.
- **Profiling a nuisance.** Plugging in $\hat\sigma^2$, $\hat\tau^2$, or $\hat\lambda$ as if known under-covers (§26.1; the small-$J$ EB trap, M16).
- **Trusting conformal under shift.** Its guarantee is exchangeability-only; drift voids it silently.
- **Mislabeling a heuristic as a theorem.** Calling a dropout or forest spread a "posterior" imports a guarantee that isn't there.

## Exercises

**Exercise 26.1 — Which audit catches it?** *Setup:* a colleague monitors an A/B test, stops the moment $p<0.05$, and reports both a 95% credible interval and the $p$-value. *Predict:* which number is trustworthy, which is corrupted by the stopping rule? *Reason:* the intuition tested is "peeking breaks everything." *Run:* re-read the M23 ledger rows.
<details><summary>Reconcile</summary>

The credible interval is fine; the $p$-value is not. Stopping cancels in the likelihood, so the posterior and its prior-averaged coverage `0.9494` are untouched, while Type-I inflates to `0.2044`. Peeking breaks the sampling-distribution audit specifically — it conditions on the *design*, which the peeking changed (the likelihood principle, M04).
</details>

**Exercise 26.2 — Rank the deep-learning readings.** *Setup:* weight decay, cross-entropy, deep ensembles, MC-dropout. *Predict:* rank these four by how firm their Bayesian reading is (theorem → heuristic). *Reason:* does "sounds Bayesian" track "is Bayesian"? *Run:* compare against §26.2's reveal and M25.
<details><summary>Reconcile</summary>

Weight decay = Gaussian-prior MAP and cross-entropy = categorical MLE are **theorems**; deep ensembles and MC-dropout are **heuristics** with no clean derivation. The surprise: the two *training* tricks that feel like pure optimization have the firmer reading, while the *uncertainty* methods advertising Bayesian intent are the folklore. Intent does not track rigor.
</details>

**Exercise 26.3 — Marginalize a second nuisance.** *Setup:* the §26.1 demo integrated out $\sigma^2$. Suppose you fix $\sigma^2$ at the plug-in but use the Student-$t$ quantile anyway. *Predict:* does that recover 95% coverage? *Reason:* "the fix is just fatter tails." *Run:* replace the Normal quantiles with `stats.t(df, mn, sd).ppf(...)` and re-check coverage.
<details><summary>Reconcile</summary>

Yes — coverage returns to ~0.95: under the reference prior $s^2/n = b_n/(a_n\kappa_n)$ exactly, so $t$ quantiles reconstruct the marginal interval. It was never about the quantile table but about propagating $\sigma^2$'s uncertainty into $\mu$ — the $t$ *is* the marginalization, compiled.
</details>

## Takeaways

- The whole course is four lines: model = joint, inference = conditioning, prediction = marginalization, decision = expected loss. Every method is a special case, approximation, or audit of them.
- Two audits, only two: the **posterior** (post-data belief) and the **sampling distribution** (pre-data guarantee). BvM makes them agree in the nice case; the ledger is where they split.
- Marginalize nuisances, don't profile: integrating out $\sigma^2$ gave `0.95` coverage where plugging in gave `0.89`.
- The status column — **theorem / approx / heuristic / none** — is the transferable skill: ridge, GPs, Kalman are theorems; k-means and the bootstrap approximations; deep ensembles heuristics; the SVM hinge loss has no honest likelihood reading.
- Conformal gives finite-sample, distribution-free, **marginal** coverage under exchangeability — no conditional guarantee; void under shift.
- The stance is **calibrated Bayes**: Bayesian for inference, frequentist for evaluation — run both.

You began able to *run* MLE, ridge, cross-entropy, dropout, and an A/B test. You can now say what each one *is* — the joint it assumes, the line it implements, the approximation it makes — and name the audit that catches it when it lies. Given a method you have never seen, you can sort it into theorem / approximation / heuristic / none, read off its implied prior, and decide whether to marginalize or profile its nuisances. That is the difference between using statistics and doing it.

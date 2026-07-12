# Math referee review — modules/15-glms-classification.md

**Verdict: APPROVE** (0 sev-1, 0 sev-2, 3 sev-3). Harness green, deterministic, every
load-bearing number independently reproduced, spec deviation ruled justified.

## Harness / determinism
- `python tools/run_module.py modules/15-glms-classification.md --check-determinism`
  → exit 0, **PASS**, byte-identical second run (no NON-DETERMINISTIC warning),
  no numbers-contract warning, no banned-pattern warning. 14 runnable blocks
  (11 exposition + 3 exercise-Run), 3946 prose words (in 2500–5000), 6 figures
  all referenced and discussed.
- Runtime is CPU-contention-bound on the 2-CPU box: 61 s with 3 competing
  determinism runs, 167 s with 7. Well under the 300 s cap regardless.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | header line 6 | `**Runtime.** ~34 s`. Could not reproduce; lightest-contention isolated-ish run measured **61 s** (block 6 NUTS alone ~15–27 s + ~10–15 s JAX import/JIT). 34 s is at the optimistic edge; prompt-writer expected ~67 s. | Re-measure on an unloaded box and state the representative value (~35–65 s), or note "compute-only, warm JAX." Non-blocking. |
| 3 | §15.3, line 229 | "its mean sits up to `0.100` low on the steepest coefficient." For β₂ the Laplace mode is −0.803 vs posterior mean −0.903 — i.e. *less negative* (higher in signed value, **lower in magnitude**). "low" is sign-ambiguous. The mode-vs-mean **skew explanation is correct** (logistic-coeff posterior has the heavier tail away from 0, so mode is pulled toward 0). | Reword: "its mode sits `0.100` short of the mean in magnitude (closer to 0), because the n=50 posterior is skewed away from zero." |
| 3 | §15.6, line 407–409 | Well-specified panel does **not** exhibit NB's small-n sample-efficiency lead: NB≥LR at *every* n (n=20: NB `0.191` vs LR `0.160`). Prose is careful — it only claims "competitive throughout" / "reaches its asymptote fast," never that NB wins early — so no false statement, but the classic Ng–Jordan "generative wins early" beat is muted/invisible in the left panel. | Optional: pick a well-specified regime where NB visibly leads at small n, or add half a sentence noting the sample-efficiency edge is the *misspecified* panel's fast plateau, not a small-n win here. |

## Deviation ruling (spec item 4: "gap largest near the boundary") — **JUSTIFIED / APPROVED**

The spec's phrase is *mathematically false* for the plug-in-vs-integrated gap, and the
author correctly overturned it and staged the correction as the predict-first catch.

- **Claim verified independently and analytically.** MacKay moderation is
  σ(m/√(1+πs²/8)) with κ(s²)=1/√(1+πs²/8)>0. Since the denominator is strictly
  positive, σ(m/κ)=0.5 ⟺ m/κ=0 ⟺ **m=0** ⟺ σ(m)=0.5. Confirmed numerically:
  at m=0, p=0.500000 for s²∈{0,0.5,5,100}. So (a) the sign of the logit — hence the
  0.5 decision — **can never flip** (also nailed by Exercise 15.2: "disagree on exactly
  zero points", printed `0.0`), and (b) the |plug-in − integrated| gap is **exactly 0
  at the boundary**, rising to a peak at plug-in p≈`0.854` (module) and decaying again
  as m→∞. "Largest near the boundary" is precisely wrong; the module's version is the
  rigorous truth.
- **Honors the rigor intent.** BRIEF quality-bar #1 (rigor behind intuition) and
  STYLE §1 (catch the reader being wrong) are *better* served by the correct statement
  staged as a surprise ("the catch — it peaks *not* at the boundary…") than by
  parroting an incorrect spec sentence. The "at small n" half of the spec item *is*
  honored (n=50 gap `0.0332` → n=500 gap `0.0034`, order-of-magnitude collapse), as is
  "quantified vs MC vs plug-in." **Ruling: the reframing is a correct-and-superior
  deviation, not a defect.**

## Independent recomputations (all reproduce the module to quoted precision)

| quantity | module | independent | ✓ |
|---|---|---|---|
| MacKay κ(s²)=1/√(1+πs²/8) & MC integral of σ over N(m,s²) | 0.8005 vs MC 0.7988 | MC tracks MacKay across (m,s²) grid | ✓ |
| sklearn ≡ hand-CE | max|diff| `1.13e-04`; coefs 0.4737/1.7105/−0.7317 | identical | ✓ |
| C=np.inf sound? | (deprecation workaround) | == `penalty=None` to `0.0e+00`; raises **no** Future/Deprecation warning | ✓ sound |
| separation ‖w‖ sweep | 1.944→8.124→17.955; CE 0.20116→0.00000 | infimum 0, no finite minimizer confirmed | ✓ |
| three-way overlay | MH-vs-NUTS `0.028`, Laplace mode-shift `0.100`, NUTS sd 0.331/0.314/0.373 | reproduced | ✓ |
| ECE | integrated `0.0207` vs plug-in `0.0401`; ≥0.90 bin 0.959/0.915 | reproduced | ✓ |
| NB vs LR | well-spec 0.104/0.105 (tie); misspec NB→0.204 plateau, LR→0.069 | reproduced; softened claim (gap shrinks/can reverse, no guaranteed crossover) respected | ✓ |
| survival | truth [0.2,0.6]; censored MLE `[0.2174,0.554]`; drop `[0.9727,0.1628]`; censored frac `0.305` | reproduced. Param order [intercept,slope]. S(c)=e^{−λc} correctly enters via obs=c for censored (`(1−failed)·(−λ·obs)`); density logλ−λt for failures. Bias direction correct: dropping low-hazard survivors ⇒ intercept up (~5×), slope flat. | ✓ |
| Poisson offset | slope 0.5→1.1 | with-offset `0.512`, no-offset `1.108`; inflation = 0.5+0.6 (logE=0.6x) exactly | ✓ |

## Other checks
- **NumPyro idioms** (§15.3): numpy arrays passed to `mcmc.run` (idiom RULE ✓);
  `MCMC(NUTS(...), num_warmup, num_samples, num_chains=2, chain_method="sequential",
  progress_bar=False)`, `PRNGKey`, `get_samples()` all match `tools/ppl_idioms.py`.
  `dist.Normal(0.,tau).expand([d])` + `dist.Bernoulli(logits=X@b), obs=y` is valid;
  no `plate` on the obs site, which is fine because `Predictive` is never called here
  (the plate rule in the idiom file is scoped to predictive generation). Not a defect.
- **Warning suppression** (§15.2, Ex 15.1): `catch_warnings`+`simplefilter("ignore")`
  is narrowly scoped to the separable-data `LogisticRegression` loop, justified by the
  inline comment (lbfgs ConvergenceWarning is the *pedagogical point*). Narrow ✓.
- **Notation §3**: N(0,τ²I) uses variance convention (τ=3 ⇒ var 9) ✓; Exp rate via
  `rng.exponential(1/λ)` ✓; λ=exp(xᵀβ) hazard ✓. No R anywhere ✓.
- **Citations**: MacKay ITILA, Ng–Jordan 2002, ISLP ch.4/11, booklet ch.8/11 — all
  by concept, none fabricated. ✓
- **SPINE-INDEX consistency**: M04 (likelihood→loss dictionary, censoring seed S(c)),
  M13 (Laplace = MAP+Hessian), M10 (`rw_metropolis`), M05, M14 all cited accurately;
  forward promises to M22 (p>1/11 cancer threshold), M24 (confounder), M25 (harness,
  ensembles, temp scaling) land on real index entries. ✓
- **Numbers-contract spot-check** (≥6): 26/26 prose backtick numbers confirmed in
  printed output (`1.13e-04`, `1.944`, `8.124`, `17.955`, `0.8259`, `0.7988`, `0.8005`,
  `0.0332`, `0.854`, `0.0034`, `0.0207`, `0.0401`, `0.959`, `0.915`, `0.104`, `0.204`,
  `0.069`, `0.2174`, `0.9727`, `0.028`, `0.100`, `0.331`, …). Harness's own contract
  check also clean.

## Required checklist
- [x] Determinism re-run PASS, zero warnings, exit 0
- [x] Spec items 1–8 all present (recipe table; separation+prior cure; three-way agree;
      integrate-don't-plug + MacKay vs MC vs plug-in, small-n; calibration/ECE harness;
      gen-vs-disc softened, well+misspec curves; survival S(c) + drop-censored bias;
      ordinal cumulative-link mention + Poisson-offset exercise)
- [x] Deviation adjudicated: **JUSTIFIED** — corrects an incorrect spec sentence,
      honors rigor, staged as predict-first catch; "at small n" half honored
- [x] All §3 math recomputed independently — no discrepancies
- [x] NumPyro idioms match ppl_idioms.py; C=np.inf sound (no silent change); warning
      suppression narrow and justified
- [x] Citations honest; notation respected; SPINE-INDEX callbacks accurate
- [x] Numbers contract ≥6 spot-checked (26/26)

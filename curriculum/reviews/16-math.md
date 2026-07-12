# Referee report — modules/16-hierarchical.md (math verification)

**Verdict: APPROVE.** The crown jewel earns the name. Determinism clean, numbers-contract
clean, all 8 Required items present and correct, both spec deviations justified (author's
sharper story is right where it diverges from the spec's soft language). Only cosmetic nits.

## Harness re-run
- `python tools/run_module.py modules/16-hierarchical.md --check-determinism` → **exit 0**,
  `PASS in 95.3s (4307 prose words, 19 blocks, 4 figs referenced)`, **zero WARNING lines**.
  Zero warnings means the runner's built-in numbers-contract check (prose backtick-numbers ⊆
  printed output) and the byte-identical determinism check both passed.
- Runtime 95.3s single-run on this contended box vs header's "~40–65 s" — see F2. Well under
  the 300s cap.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | §16.6, "Mixed-effects models are this" para (~L408) | "agree to the **third decimal** — correlation `1.000`" overstates pointwise agreement. The printed sample shows 2nd-decimal gaps (county 14: MixedLM `0.434` vs Bayes `0.453`, Δ=0.019; county 19: `0.381` vs `0.391`). `corr=1.000` measures *linear* agreement (rounded from ≥0.9995), which is genuine, but the values track each other, they don't match to 3 decimals. | Replace "agree to the third decimal" with "track each other almost exactly (correlation `1.000`)" or "agree to within ~0.02". The small systematic offset is exactly the marginalize-vs-plug-in-τ gap §16.5 discusses — could even name it. |
| 3 | header `> **Runtime.**` | Claims "~40–65 s measured"; measured 95.3s here. The clause "load-dependent" hedges it and we are explicitly on a contended box, so defensible — but a reader on a similar 2-CPU box sees ~95s, outside the stated band. | Widen to "~40–95 s, load-dependent" or note "up to ~95s under CPU contention". |
| 3 | §16.2 Reconcile (L178) + Takeaways (L510) | "τ stuck at `0.723`" — 0.723 is the *minimum τ explored* by the centered chain (its exploration floor), not a fixed point; the chain still ranges above it. Adjacent text "cannot descend into the neck / cannot reach small τ" makes the meaning clear, so it reads fine in context, but "stuck at 0.723" in isolation (esp. the takeaway bullet) could be misread as τ pinned there. | Optional: "can't push τ below `0.723`" / "floors out at `0.723`" is marginally more precise than "stuck at". Not blocking. |

No sev-1 or sev-2 findings.

## Required checklist (8 items)

1. **Eight schools complete + 3-models-on-one-axis + τ posterior + half-Cauchy/half-Normal sensitivity** — ✅ y/σ verbatim correct; no-pool/complete-pool/partial-pool on one axis (shrinkage.png); τ median 2.80 printed; half-Cauchy 95th `10.45` vs half-Normal `8.01`, school-A `8.23`→`7.67`, with the sharp "sensitivity real in τ, negligible in θ_j" reading. ✅
2. **Funnel returns (M12 callback), counts printed** — centered `86` div / min-τ `0.723`; non-centered `0` / `0.004`. Explicit M12 callback ("there: 13→0"), consistent with SPINE-INDEX M12 numbers. ✅
3. **Bake-off, predict-first, conjugate-in-loop (no MCMC/replication)** — ✅ MoM τ̂² + Normal–Normal weight inside the loop; predict-then-reconcile staged; `2.019`/`1.978`/`1.691`. ✅
4. **wⱼ derived = M05 master formula, one level up** — boxed `wⱼ=(1/σⱼ²)/(1/σⱼ²+1/τ²)`; correctly framed as M05 with τ² as prior variance. ✅
5. **Radon-style synthetic (counties, varying intercepts, group-level predictor), pandas; batting = mention only** — ✅ 590 homes/40 counties, uranium + floor predictors, pandas DataFrame; batting appears only in the JS callback as a phrase. ✅
6. **EB vs FB, interval widths too narrow at small J, printed** — EB widths `15.96` vs FB `21.89`, "`27`% too narrow"; "EB point-estimates the prior; fine at scale, overconfident at J=8" stated verbatim in spirit. ✅
7. **James–Stein CALLBACK, no re-derivation** — ✅ "(No re-derivation; see module 08 for the JS = EB algebra.)"; frames JS = EB with point-mass hyperprior at μ=0. Callback-only, does not re-derive. ✅
8. **MixedLM vs Bayesian side-by-side, printed; "random effects" renamed; benchmarking/small-area (ch.9)** — ✅ statsmodels MixedLM η vs Bayes η table + corr `1.000`; Bridge maps direct/synthetic/composite/benchmarking to booklet ch.9. ✅

### Deviation rulings

- **(a) EB τ̂ = 0 exactly (boundary), not "small" plug-in.** **JUSTIFIED — author is correct.**
  Independently maximized the eight-schools marginal likelihood Πⱼ N(yⱼ; μ, σⱼ²+τ²) over (μ,τ≥0)
  (μ profiled analytically at each τ on a 4000-point grid): argmin negloglik at **τ=0.0000**, and
  negloglik is **monotonically increasing** from τ=0 (29.6742 at τ=0 → 29.6774 at 0.5 → 29.7734
  at 2.8). The classic data really do scatter *less* between schools than their own σⱼ imply, so
  the marginal MLE sits exactly on the boundary. The spec's "τ̂ plug-in" language was soft; the
  author's sharper "EB concludes complete pooling and hands every school the complete-pool
  interval" is the truth and is pedagogically superior. The boundary handling (var_eb =
  1/Σ(1/σⱼ²) = complete-pool variance) is the correct EB-at-τ=0 interval.
- **(b) radon τ_c=0.50 to avoid MixedLM singularity.** **REASONABLE.** With sig_y=0.75 this gives a
  moderate ICC that keeps MixedLM's variance component off the zero boundary (avoiding a singular
  REML fit) while leaving the hierarchy visibly at work on small counties. Honest data-generation
  choice, disclosed in code; fit recovered g1=`0.69`(true 0.7), floor=`-0.68`(true −0.6), 0 div.

## Independent recomputations (all confirm the module)

- **EB marginal MLE**: grid maximization → τ̂=0.0000 (boundary), negloglik monotone from 0. ✅ (F above)
- **Complete pooling**: μ_cp = 7.6856 → `7.69`, se = 4.0719 → `4.07`. ✅
- **Partial-pooling weights** (τ̂=2.80): w_B(σ=10)=0.073→`0.07`, w_H(σ=18)=0.024→`0.02`,
  matches M05 precision form. Closed-form school-A = 0.034·28+0.966·6.49 = `7.22`. ✅
- **Eight-schools posterior** via my own independent griddy-Gibbs (integrating μ, sampling τ from
  HalfCauchy(5) posterior, then μ, θ): τ median **2.70** (module 2.80), mean 3.54 (3.71), μ **6.52**
  (6.49), θ_A **8.12** (8.23), FB mean 95% width **21.42** (21.89). Same regime, close agreement —
  NUTS values authoritative. ✅
- **EB interval width**: 2·1.96·√(1/Σ(1/σⱼ²)) = `15.96`; 1−15.96/21.89 = 0.271 → `27`% too narrow. ✅
- **Bake-off seed robustness** (spot-checked seeds 1,2,3,4,5,42,100, module uses SEED+1=1):
  adaptive partial pooling beats **both** extremes on **all 7 seeds** (partial ≈1.66–1.69 vs
  no-pool ≈1.96–2.02, complete-pool ≈1.98–2.00). **Generic win, not seed-lucky.** ✅
- **λ⋆ = τ²/(τ²+σ²)**: analytically minimized E[(θ−λy)²]=(1−λ)²τ²+λ²σ² → λ⋆=τ²/(τ²+σ²)=0.5;
  Ex 16.2 τ=4 → 16/17=`0.94`, grid `0.95`. ✅
- **Adaptive within 7% of oracle**: (1.691−1.588)/1.588 = 6.5% ≤ 7%. ✅

## Consistency / idioms / citations / notation

- **M05 master formula**: SPINE-INDEX gives "(κ/(κ+n))·prior + (n/(κ+n))·MLE"; module's precision
  form wⱼ=(1/σⱼ²)/(1/σⱼ²+1/τ²) is the same object, explicitly labeled M05, τ² as prior variance.
  **No re-derivation of JS** (callback-only, per spec item 7). No shrinkage arithmetic contradicts M05/M08. ✅
- **M12 funnel numbers**: module's "13 divergences → 0 on the bare funnel" matches SPINE-INDEX M12
  key numbers ("funnel divergences 13→0"). ✅
- **M18 cross-reference**: M18 L201 cites "module 16's 0.73 at J=8"; module 16's `27`% too narrow ⇒
  width ratio 15.96/21.89 = 0.729 ≈ 0.73. Internally consistent; the J=8→10→50→1000 trend
  (0.73→0.87→0.98→1.00) is monotone as claimed. ✅
- **NumPyro idioms**: reparam(model, {"theta": LocScaleReparam(0)}), MCMC(NUTS(·),
  chain_method="sequential", progress_bar=False), extra_fields=("diverging",),
  get_extra_fields()["diverging"].sum() — all copy ppl_idioms.py (incl. the 8-schools noncentered
  idiom). Obs passed as numpy arrays. reparam toggle (`noncentered=True/False`) correct. ✅
- **Notation §3**: math uses N(·, VARIANCE) throughout; code correctly passes SD to dist.Normal
  (dist.Normal(theta, sigma) with σ_j = sd; dist.Normal(0.,10.) for μ~N(0,10²)). No variance/sd
  trap. HalfCauchy(5)/HalfNormal(5) match prose. ✅
- **Citations (booklet ch. 9)**: opened `curriculum_material/bayesian_booklet/ch09-hierarchical-models.md`.
  §9.2 "Small Area Estimation" contains verbatim the claimed vocabulary — "direct estimator" ȳ_i,
  "synthetic estimator" θ̂, "composite/shrinkage estimator" E(μ_i|y), "borrowing of strength",
  and the weight **λ_i = δ²/(δ²+σ_i²/n_i)** (L218) — exactly the module's Bridge claim. §9.3
  "Benchmarking" backs the benchmarking/aggregate-to-total claim. ch. 7 (§7.1–7.2) covers
  hierarchical Bayesian models. **All citations verified against the source.** ✅

## Structure / STYLE spot-check
- Skeleton complete (Spine/Which line/Promise/Prereqs/Runtime/Sources; §16.1–16.6; Bridge;
  Pitfalls ×5; Exercises ×4 predict-then-run; Takeaways ×7 ≤ cap). 15 exposition blocks ≤ 16 cap
  (+4 exercise Run blocks). 4 figures, all discussed with real captions. ≥1 surprising exercise
  (16.1, 16.4), ≥1 ML/DL bridge (16.3). Predict-then-reveal staged in §16.2 and §16.4 demos. ✅

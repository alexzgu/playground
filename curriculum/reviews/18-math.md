# Referee report — modules/18-scale-and-misspecification.md (math verification)

Verdict: **REVISE** (1 × sev-2, 6 × sev-3; no sev-1). All prose numbers reproduce
exactly; all three author deviations are mathematically justified. The one sev-2 is
a robustness/honesty issue on a headline demo number, not a math error.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| **2** | §18.3, EB/FB table, "disastrous `0.2778`" | The J=10 ratio `0.2778` is a **single-dataset outlier**, not generic J=10 behavior. The demo hardcodes `seed=1`, whose 10-point sample yields `A_hat=0.033` — a near-boundary marginal-variance estimate (the M16 τ̂=0 phenomenon). Across seeds 0–11 the J=10 ratio ranges **0.002 – 0.978** (mean `0.79`, mode `~0.95`); for *typical* J=10 draws EB is within a few % of FB. Presenting `0.2778` as "the" J=10 width and calling it "disastrous… exactly module 16's overconfidence warning" overstates a cherry draw, and the magnitude clashes with M16's own `0.73` (27% too narrow) at J=8. | MC-average the ratio over many datasets per J (report mean ratio, which still rises 0.79→0.98→~1.0 and makes the real point), **or** add one sentence: "this particular 10-problem sample landed near the variance boundary (A_hat=0.03) — the small-J boundary risk of M16; typical J=10 samples are milder." The J=50 (`0.9783`) and J=1000 (`0.9995`) points are robust and carry the argument. |
| 3 | §18.6, "scales the data precision by η and so multiplies the posterior variance by 1/η" | The `1/η` variance law is **exact only for a flat/absent prior on θ**. The Normal–Normal *demo* uses a proper prior (`tau2=100`), so `1/√η` is approximate: printed `0.4468` vs exact-law `0.4472` at η=0.25. (The §18.5 regression recalibration *is* exact — flat prior there.) | State the flat-prior scope for the "×1/η" claim, or note the tiny prior-induced deviation in the Normal–Normal numbers. |
| 3 | §18.5, "misspecification of a symmetric noise shape does not bias the variance of a plain average (module 08's exercise 08.3)" | Imprecise attribution. An intercept-only OLS has sandwich variance ≡ model variance **regardless of noise shape** (skew *or* heteroskedasticity) — because a plain average carries no covariate-weighting for heteroskedasticity to distort. It is *not* symmetry that protects the mean; 08.3's symmetric-Laplace is a different mechanism. Verified: for a pure mean the coincidence holds even under the skewed heteroskedastic truth of §18.5. | Reword: the mean is robust because it has no covariate-weighting to misprice, whereas a slope does. Keep the 08.3 pointer but drop "symmetric" as the operative reason. |
| 3 | §18.6, η* recalibration | A single **global** η scales *every* parameter's variance by 1/η, so η*=0.526 buys back the *slope's* width but simultaneously mis-scales the intercept (and any other functional) — it cannot match all sandwich SEs at once. Implied by "one-knob" but not stated. | Add a half-sentence: η matches one functional's width; it is a global temperature, not per-parameter calibration. |
| 3 | §18.4, ridge vs lasso | `ridge = Ridge(alpha=10)` is a fixed, untuned penalty while `lasso = LassoCV`. A tuned RidgeCV would lower `0.267`. The qualitative claim (ridge produces no zeros) is α-independent, so the beat survives, but the head-to-head RMSE is a slightly unfair comparison. | Either CV-tune ridge too, or note that ridge's RMSE is illustrative and its *no-zeros* property (not its RMSE) is the load-bearing point. |
| 3 | §18.2, "the estimated local-fdr tracks the exact posterior" | The KDE estimate (bw=0.15) runs systematically **~12% low** vs the exact mixture posterior (`0.547` vs `0.621`; `0.296` vs `0.334`; `0.019` vs `0.024`) — tail over-smoothing. "Tracks" is generous. Both numbers are shown honestly and FDR is still controlled (bias → slightly more discoveries, realized FDP 0.069 < 0.10). | Optional: note the estimate is biased low in the tails (finite-sample KDE), so local-fdr slightly over-rejects — still within the q target. |
| 3 | Header, "Runtime. ~68 s" | Verify against measured harness time (earlier run was killed at 280 s only under 4-way CPU contention). Cosmetic — confirm the number. | Update to the measured single-run time. |

## Deviation rulings (adjudicated)

- **(a) dense N(0,1) effects instead of the spec's 95%-null sparse — ACCEPT.**
  Verified the overshoot claim independently. Under sparse truth (95% null, signals
  N(0,σ), σ∈{2.5,3,4}) the marginal-variance EB estimate is small (`A_hat≈0.2–0.6`,
  shrink 0.17–0.38), so uniform shrinkage **over-corrects** the selected set: raw–true
  bias stays positive (`+1.39/+1.13/+0.46`) but shrunk–true goes strongly **negative**
  (`−1.18/−1.50/−2.30`). The clean dense beat — shrunk lands `0.006` from truth — is
  destroyed; shrinkage would understate more than raw overstates. The author's
  "uniform shrinkage overshoots on the selected set under sparse truth, muddying the
  beat" is mathematically correct, and the horseshoe §18.4 is the right home for the
  sparse case. The §18.1 caveat ("over-shrink the genuine large effects", cashed §18.4)
  is honest.

- **(b) π₀=0.90, N=5000 vs spec's 0.95/1000 — ACCEPT (reasonable).**
  0.90/5000 gives ~500 non-nulls and 5000 z-scores → a stable KDE and stable discovery
  counts (BH `166`/FDP `0.060`, local-fdr `174`/FDP `0.069`, both < q=0.1). The spec's
  0.95/1000 (~50 non-nulls) would make the tail KDE and discovery counts noisy, muddying
  the "same place, same rate" beat. All spec requirements met (matched FDR, discoveries
  printed, fdr≈P(null|z)). Minor: the module does not explicitly flag it deviates from a
  canonical 0.95/1000 — not required.

- **(c) η* recalibration linking tempering to the sandwich — ACCEPT (sound).**
  η*=(post_sd/sand_sd)² is the correct solution of post_var/η = sand_var; since tempering
  a flat-prior Gaussian likelihood scales the posterior variance by exactly 1/η, the
  construction is exact and reproduces `0.1019` to 4 dp. Honestly labeled **heuristic**.
  Sole caveat is the global-vs-per-parameter point (finding 5 above).

## Recomputation list (independent, all reproduced to printed precision)

- **18.1 EB de-biasing:** A_hat `1.121`, shrink `0.528` = A/(A+1) = 1−1/(A+1) ✓ (semantics
  correct); top `5.29`/`2.55`/`2.80`; top-10 raw `3.772`/true `1.987`/shrunk `1.993`;
  inflation `1.785`, shrunk residual `0.006`; RMSE sel `1.918`→`0.523`, all `1.023`→`0.689`. ✓
- **18.2 two-groups:** BH `166`/FDP `0.060`; local-fdr `174`/FDP `0.069` — comparable
  quantities, both FDR-controlled < 0.1 ✓; exact vs est `0.547/0.621`, `0.296/0.334`,
  `0.019/0.024` (est biased ~12% low, finding 6). KDE-density-ratio construction sound.
  Bonferroni `59` (Ex 18.2). ✓
- **18.3 EB/FB:** `0.2778`/`0.9783`/`0.9995` reproduce (FB mixture-variance formula
  E[var_c]+Var[mean_c] is correct); grid-upper-bound insensitive (0.2778→0.2789 for
  [0,20]→[0,100]); **but seed-sensitive** (finding 1). Direction matches M16 (EB narrower);
  magnitude does not (0.28 vs 0.73).
- **18.4 horseshoe:** RMSE `0.033` vs ridge `0.267` (100 nonzero, max null `0.534`) vs
  lasso `0.061` (40 nonzero, `35` FP among 95 nulls); `43` divergences; κ null median
  `0.993`, signals `[0.16 0.21 0.29 0.41 0.17]`, max null |β| `0.130`; signals to 2 digits.
  Comparison fair on *coefficient RMSE against the same β_true*; lasso via `LassoCV(cv=5)`,
  ridge via fixed `alpha=10` (finding 4). **43 divergences do not invalidate the RMSE
  claim** — they concentrate at small τ (the region avoided is *stronger* shrinkage), so if
  anything nulls are under-shrunk, yet max null is already `0.130`; signals are recovered
  cleanly and the beat (horseshoe ≪ lasso ≪ ridge) is robust. The regularized-horseshoe
  pointer is an honest, sufficient caveat. ✓
- **18.5 sandwich:** post_sd `0.0739` = √(s²·(X'X)⁻¹₁₁·df/(df−2)) (Student-t, df=198,
  inflation ≈1.005 negligible) ✓; HC0 sandwich `0.1019` = √[(X'X)⁻¹ X'diag(r²)X (X'X)⁻¹]₁₁ ✓;
  true sampling sd `0.1046` from 5000 refits (legit ground truth; HC0 `0.1019` slightly low
  — known finite-sample HC0 bias, immaterial at n=200) ✓; skew `2.44` ✓; "too narrow by a
  third" = 29% ✓.
- **18.6 power posterior:** Normal–Normal sd `0.2236`/`0.3161`/`0.4468` (1/√η approximate
  under the proper prior, finding 2); η* `0.526`, tempered `0.1019` matches sandwich by
  construction. ✓
- **Exercises:** 18.1 bias `2.742`/`1.785`/`1.317` (top-1 most inflated — correct, verified);
  18.3 entropy `0.454`→`1.026`; 18.4 `0`-of-95 exact zeros, smallest `0.00001`. ✓

## Required checklist

- [x] **Determinism harness** — PASS, zero warnings (see RETURN line for confirmed status).
- [x] **Numbers contract** — spot-checked >20 prose backtick-numbers against printed output
  (committed log tools/logs/18-…out.txt + independent recompute); all match to precision.
- [x] **Deviations (a),(b),(c)** — all ruled ACCEPT (see rulings above); (a) overshoot claim
  independently verified.
- [x] **EB de-biasing semantics** — shrinkage estimator is (1−1/(Â+1))·X = Â/(Â+1)·X = EB
  posterior mean; correct.
- [x] **NumPyro idioms** — manual non-centered horseshoe (β=z·λ·τ, z~N(0,1) in plate), valid
  and equivalent to LocScaleReparam; `target_accept_prob=0.95`, `extra_fields=("diverging",)`,
  numpy obs arrays, `PRNGKey(SEED)`, 2 chains sequential — all match tools/ppl_idioms.py.
- [x] **Citations** — Efron LSI / BH / booklet ch.9 by concept; ISLP ch.13 = "Multiple
  Testing" (correct); no fabricated page numbers.
- [x] **Notation §3** — N(·,·) second-arg-variance respected throughout; Half-Cauchy/Half-Normal
  standard; z~N(0,1); β_j~N(0,τ²λ_j²) variance. Consistent.
- [x] **M-closed/M-complete/M-open box** — matches the standard Bernardo–Smith categories;
  accurate.
- [x] **Skeleton/STYLE** — spine header complete; §§18.1–18.6 + Bridge + Pitfalls(5) +
  Exercises(4, predict-then-run, ≥1 surprising, ≥1 ML/DL bridge) + Takeaways(7). Compliant.

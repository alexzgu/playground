# Referee report — modules/00-four-lines.md (mathematics + spec)

**Verdict: APPROVE (with 2 sev-2 nits worth fixing before lock).**
Harness: `PASS in 3.4s`, zero warnings; determinism OK; `max|diff| = 4.5e-15`. All marquee
numbers recomputed independently and match the printed/quoted precision. No mathematical error found.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 2 | §00.5 notation table (L254–268) | SYLLABUS item 5 demands the STYLE §3 table **verbatim**. Module drops the row `Beta, Binomial, Poisson, Dirichlet, Multinomial \| standard` and drops `Cov[·,·]` from the Expectation row (and the "(conditioned on)" gloss on x). Beta/Binomial are used all over this very module. | Restore the missing `Beta, Binomial, …` row and re-add `Cov[·,·]`. 30-second edit. |
| 2 | §00.2 line-4 decision (L131–161) | The module's most counterintuitive result — *retest* is optimal (`5.6846`), beating treat-now (`9.806`) — is revealed with **no captured Predict**. STYLE §1: "a surprise shown without a captured prediction is a defect." (The PPV got a Predict; the decision winner did not.) | Add one line before the decision block: "**Predict.** Which is cheapest — treat now, never treat, or pay 5 to retest?" |
| 3 | §00.4 table | 14 rows vs SYLLABUS "fifteen-procedure". Author merged ridge/weight-decay. **Defensible on merit** — they are the identical ℓ2 penalty and all 15 named procedures still appear (ridge+weight-decay share one row). No fix required. | none |
| 3 | §00.4 bootstrap row | "resampling ≈ an implicit posterior" is practitioner folklore (Bayesian bootstrap). The `≈` softens it acceptably at orientation; STYLE honesty labels relaxed here. | optional: append "(heuristic)". |
| 3 | Bridge (L282) | "the booklet's 'five steps' … are lines 1–4 plus a model-check" is a slightly loose paraphrase (booklet step 5 = "substantial conclusions" is folded in). Verified booklet ch02 L189–196 — characterization is fair. | none |

## Required checklist (SYLLABUS 00-four-lines)
1. Ridge = normal-eq = posterior-mean, `max|diff|` at machine precision — **PASS** (§00.1; 4.5e-15).
2. Medical test, joint→condition→PPV `0.0194`, cost-matrix treat/retest decision — **PASS** (§00.2).
3. Coin losing-bet, Beta(8,4) mean `0.6667`, price between plug-in 0.7 and predictive 2/3, sim θ~posterior, mean profit `-0.0132` < 0 — **PASS** (§00.3).
4. Procedure table → "which line?", predict-then-reveal (blank list, then answers in `<details>`) — **PASS on merit** (14 rows, see sev-3).
5. Notation table + variance/rate conventions + how-to-run — **PARTIAL** (sev-2: not verbatim).

## Independent recomputations (all match module)
- **Ridge≡posterior identity is EXACT for all inputs, not just the chosen numbers.** Posterior mean `(X'X/σ² + I/τ²)⁻¹X'y/σ²` = `(X'X + (σ²/τ²)I)⁻¹X'y`; σ² cancels identically; with `τ²=σ²/α` the shrinkage is exactly `α=σ²/τ²`. Algebra in prose (L69–72, L92) is correct. Holds ∀ X,y,σ²,α. ✓
- **PPV pipeline:** PPV=0.019434… → `0.0194` ✓; LR⁺=19.8 ✓; PPV after ++ =0.281832… → `0.2818` ✓; P(T2+)=0.068268… → `0.0683` ✓.
- **Decision losses from stated matrix** (treat=[0,10], no-treat=[1000,0], c=5): E_treat=9.80565→`9.806`, E_notreat=19.4346→`19.435`, E_retest=5.68463→`5.6846`, argmin=retest ✓.
- **Coin/bet:** Beta(1,1)+7H3T=Beta(8,4) ✓; predictive P(heads)=8/12=2/3 ✓; payout pay 0.68/receive 1-if-heads ⇒ E[profit]=P(heads)−0.68; under predictive =0.6667−0.68=**−0.0133** (analytic), MC `-0.0132` within noise ✓; fair price would be 0.6667, so bet is overpriced and predictive bettor correctly declines (edge −0.0133<0), plug-in accepts on false +0.02 edge. Payout arithmetic watertight. ✓
- **Table spot-check (5):** MLE=flat-prior mode ✓; conformal "predictive coverage under exchangeability" honest per M26 (no conditional-coverage overclaim) ✓; k-means=hard-EM limit, line 2 defensible ✓; dropout≈MC predictive ✓; Kalman predict=marginalize/update=condition ✓.
- **Exercises:** 00.1 τ² 2.25→0.00225, ‖β‖ 2.5110→0.3521 ✓; 00.2 PPV 0.0194→0.1667 = 8.6× (odds ~10×) ✓; 00.3 streamed=batch=Beta(8,4) ✓.
- **Citations:** booklet "five steps" verified ch02 L189; C-B §1.2–1.3 (conditioning/Bayes) and ISLP §6.2 (ridge) consistent. No fabrication.

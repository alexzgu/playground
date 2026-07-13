# EXAM.md — mathematical-statistics referee review

**Verdict: REVISE** (1 severity-2 fix blocking; remainder minor). Harness clean.

Determinism: `python tools/run_module.py EXAM.md --check-determinism` → **PASS in 4.3s**, zero
warnings, 20 blocks, 5 figs referenced, byte-identical across runs.

## Findings table

| sev | problem | issue | concrete fix |
|---|---|---|---|
| 2 | P11 | Prose: collider "drags the estimate to `0.495` — **further from the truth than doing nothing**." False for the printed DGP: unadjusted `3.569` is `1.569` from truth 2.0; collider `0.495` is `1.505` from truth. The collider estimate is marginally **closer** to truth than the unadjusted one. This also mis-answers the Predict's own "rank by closeness" question (true rank: {U} 0.009 < {U,C} 1.505 < nothing 1.569 — so {U,C} is *2nd best*, better than doing nothing). | Reword to "further from the truth than adjusting for **U alone** — 'control for everything' backfires," and drop the "than doing nothing" comparison. OR retune the U→Y / U→T coefficients so unadjusted bias < collider bias (matching canon module 24: unadj 2.924 / collider 0.504, where collider genuinely overshoots past unadjusted). |
| 3 | P5 | Module 03 is only lightly leveraged — the problem is ~95% module 09 (IS, Kong ESS, tail rule); 03 contributes only the conceptual "t₃'s 2nd moment lives in the tails." Weakest integrative pairing of the 12, but genuine (heavy-tail mechanism is load-bearing). | Optional: add one line tying the failure to module 03's heavy-tail-gallery moment claim, or accept as-is. |
| 3 | P5 | Predict says "At M=1000 the ESS fraction looks respectable (over 30%)" but the actual printed value is `0.8866` (88.7%). Technically true (88>30) but undersells; echoes canon's 34.7%/62.65% which the exam's rng state no longer reproduces. | Soften to "looks healthy (near 90%)" so the Predict matches the printed number. |
| 3 | P1 | Decision (e) computes E[excess] from `lam_draw` = the Gamma–Poisson posterior on λ, i.e. the *Poisson* model's posterior, after the model was "fixed" to NB. The decision (keep, 2.321 < 4) is robust and pedagogy holds, but the coupling between the NB fix and the λ used for the decision is loose. | Optional: note that the per-shift rate λ is shared between the Poisson and NB parametrizations (NB = Gamma-mixed Poisson), so re-using `lam_draw` is legitimate. |
| 3 | P8 | "punishing Occam term" describes the wiggly kernel's occam = `7.29`, which is *positive* and only punishing *relative to* the ML-II occam `33.77` (this sign convention makes higher-occam = simpler = rewarded). Directional claims (wiggly higher fit −6.70 vs −9.55; lower evidence −26.98 vs −3.35) are all correct. | Optional: clarify "punishing *relative to* the optimal kernel's Occam reward" to avoid the absolute-sign confusion. |

## Per-problem verdict

- **P1** PASS — well-posed; PPC 0.0000→NB 0.4373; NB r̂=2.32 (moment fit correct); decision keep (2.321<4) determinate.
- **P2** PASS — 0.073/0.033/0.7143 all canon-exact (module 04); peeker Type-I 0.0642→0.2059 (≈4×) correct.
- **P3** PASS — exact logZ −2.1903/−5.0734 reproduced independently; TV 0.0262→0.0082 (3.2×); O(1/√n) honestly hedged for small-n.
- **P4** PASS — KS 0.269/0.911 pass; lag-1 0.9786≈ρ²0.9801; ESS/M 0.0115≈AR(1) 0.0100 (~10/1000).
- **P5** PASS (sev-3 notes) — variance genuinely infinite (∫p²/q diverges: x⁻⁸exp(x²/2)); estimate stuck ≤1.831, ESS/M collapses 0.89→0.16.
- **P6** PASS — JS 1.93 vs MLE 9.96 vs JS⁺ 1.22; partial 1.614 wins; τ̂²=0 in 15.2% ≈ P(χ²₇<3.5)=0.165 (verified).
- **P7** PASS — ridge≡post 1.7e-15; trumpet min 0.813 at center, 1.018 extrapolating; t-slope 0.5435 resists (OLS 0.7502, +42%).
- **P8** PASS (sev-3 note) — wiggly evidence −26.98 ≪ ML-II −3.35; higher fit / lower evidence directionally correct.
- **P9** PASS — reveal gain 0.75; KF≡conjugate |diff|=0.0 exactly; **golden ratio verified**: q=r=1 ⇒ P²+P−1=0 ⇒ P=K=0.618 exactly (independently recomputed).
- **P10** PASS — power 0.7383 > assurance 0.6547 (Jensen on concave shoulder, verified); EVSI 0.0002 < EVPI 0.0013 < cost 0.05 ⇒ don't run.
- **P11** REVISE — collider bias correct (0.495) and worse than {U}, but "further than doing nothing" is false (1.505<1.569); IPW ESS 6.8% correct.
- **P12** PASS — width ratio 1.312 = t₅/z (recomputed 1.3115); coverage 0.9494 vs 0.8912; conformal 0.8887; six-line table correct.

## Recomputation list (independent)

- P9 Riccati: solved P²+P−1=0 → P=(√5−1)/2=0.618, K=(P+1)/(P+2)=0.618. **Golden ratio exact.** ✓
- P12: t₅(.975)/z(.975)=2.571/1.96=**1.3115** ≈ printed 1.312. ✓
- P11: |3.569−2|=1.569, |2.009−2|=0.009, |0.495−2|=**1.505** — collider is *closer* than unadjusted. ✗ (prose defect)
- P3: exact Beta-Binomial logZ = −2.1903 (n=10), −5.0734 (n=200). ✓ matches print.
- P2: binom.sf(8,12,.5)=**0.073**, nbinom.sf(8,3,.5)=**0.033**. ✓ canon (module 04).
- P6: P(τ̂²=0) = P(χ²₇ < 3.5) = **0.165** ≈ printed 15.2%. ✓
- P10: se=√(2/150)=0.1155, power(0.3)=Φ(0.638)=0.738. ✓
- P1: E[max(λ−3,0)]·2 with λ~Gamma(168,40.5) mean 4.148 → ≈2.30 ≈ printed 2.321. ✓

## Numbers-contract spot-check (≥10 verified, all prose backticks ⊆ printed)

2.787, 0.0000, 2.32 (P1); 0.073, 0.033, 0.7143, 0.0642, 0.2059 (P2); 0.0262, 0.0082 (P3);
0.269/0.911, 0.9786, 0.9801, 0.0115 (P4); 1.455/1.831, 0.8866/0.1555 (P5); 9.96/1.93/1.22,
15.2% (P6); 1.7e-15, 0.813/0.849/1.018, 0.5276/0.7502/0.5435 (P7); −26.98/−3.35, 0.117 (P8);
0.75, 0.618, 0.722/1.006 (P9); 0.7383/0.6547, 0.0013/0.0002 (P10); 3.569/2.009/0.495, 6.8% (P11);
5.283/4.028/1.312, 0.9494/0.8912, 0.8887 (P12). All match.

## Integrative check (both modules genuinely required)

All 12 compose ≥2 modules with distinct tools; none is a relabel. P5 (03+09) is the thinnest
pairing but the heavy-tail mechanism is load-bearing. "Draws on" attributions all accurate;
canon-attributed numbers (0.073/0.033, 0.7143, 0.75, 1.312) all match SPINE-INDEX. Staging
(Setup/Predict/Task/Solution) consistent; 5 figures resolve and are each captioned/discussed.
Genuinely surprising answers (≥5): P2 peeker 20%, P5 estimate never reaches 3, P6 JS + τ̂²=0,
P10 don't-run-the-study, P11 more-control-more-bias, P9 golden ratio.

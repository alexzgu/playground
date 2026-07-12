# 09-monte-carlo — Mathematical Referee Review

**Verdict: REVISE** (1 sev-2 blocking, 2 sev-3). Harness PASS in 25.3s, determinism two-run compare clean, zero warnings, numbers-contract grep clean. The two headline deviations are adjudicated **in the author's favor**; the single blocking defect is a factor-of-10 arithmetic error + a false attribution in one exercise reconcile.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| **2** | Ex 09.3 reconcile (~L412) | `1.8^{20}\approx 12{,}700` is wrong by 10×: 1.8²⁰ = **127,482**. Worse, the parenthetical claims the *all-1* trajectory "hoards … here 17.5%" — but P(all-1)=0.5²⁰=9.5e-7, so **zero** all-1 trajectories occur in N=10⁴ (verified). The trajectory actually holding 17.5% has **18 of 20** favored actions, weight **≈1,574**. The number quoted, the trajectory identified, and the causal claim are all inaccurate. | Rewrite: "the dominant trajectory (here 18 of 20 target-favored actions, weight ≈ 1,570) hoards 17.5% of the total; the theoretical worst case, all-1, would weigh 1.8²⁰ ≈ 127,000." Pedagogy (multiplicative blow-up, one trajectory dominates) is correct and survives the fix. |
| 3 | Header `Sources` (L8) | "ch. 5 §§5.9–5.11 (importance sampling, rejection, quadrature)". In the source, §5.7–5.8 are rejection/squeeze-envelope and quadrature sits earlier (~§5.6); §§5.9–5.11 are MC-integration / importance-sampling / proposal-choice. Rejection and quadrature are **not** in the cited range. | Cite "ch. 5 §§5.6–5.11" (or §§5.7–5.11) so rejection (§5.7–5.8) and quadrature are actually covered. |
| 3 | §09.2 (L130) | "measured RMS errors track the theoretical to two figures" — true at M=10³ (0.05226 vs 0.05193) and M=10⁵ (0.00539 vs 0.00519), but M=10⁴ is 0.01824 vs 0.01642 (~11%, one figure) and M=100 is ~9% off. The load-bearing ratio (9.69) is solid. | Soften to "track the theoretical scaling within the sampling noise of a 200-rep RMS," or drop "to two figures." |

## Deviation rulings

**(D1) Strengthened IS-failure demo — APPROVE.** Verified independently:
- **(a) Infinite variance is real.** E_q[w]=∫t₃=1 (finite) but E_q[w²]=∫t₃(x)²/φ(x)dx diverges — integrand grows like x⁻⁸·e^{x²/2} (numerically: 12.0 at x=5, 1.3e15 at x=10, 1.1e24 at x=12). So Var(w)=∞. "ESS looks fine but is meaningless" is the technically correct lesson.
- **(b) Numbers semantically match prose.** Single-run ESS 34,698 = 34.7% of M "passes"; SNIS E[θ²]=1.693 vs truth 3 → (3−1.693)/3 = 43.6% ≈ the claimed "44% low"; max weight 0.29%; median ESS/M collapse 62.65→44.38→27.76→12.27% (10³→10⁶) exactly as printed. Robust alarm (ESS/M ↓ with M) is the right and pedagogically superior diagnostic.
- **(c) Tail rule stated correctly:** proposal tails ≥ target tails; "sample from the fat distribution to learn about the thin one." Safe-direction control (t₃ proposal, bounded weights, median ESS ~92% flat, E[θ²]→1.00) confirms it.

**(D2) Booklet "ESS ≥ n" — APPROVE author's "name-collision," OVERRULE the earlier "misprint" panel and the SYLLABUS item-5 wording.** Source ch04 L116–141 derives ESS = Var_N/Var_I · n = **σ²/δ² + n ≥ n** as the *prior-augmented sample size* ("the prior is worth σ²/δ² observations"), with the booklet's own ✔-Verified annotations confirming the algebra. This is a correctly-derived, legitimately different quantity that merely shares the acronym with Monte-Carlo effective sample size — **not a misprint.** The author's characterization is fair to the source, more accurate than the syllabus's literal "misprint" instruction, and the module's framing (L202–203) honestly distinguishes the two and ties σ²/δ² to M05's κ. **Recommend the orchestrator amend SYLLABUS 09 item-5 "misprint" → "name-collision."**

## Required checklist (8 items)

1. Samples as lingua franca (mean/interval/tail/transform) — **PASS** (§09.1; E[odds] 2.6657 vs 8/(4−1)=2.6667 ✓).
2. MCSE=s/√M over 1,000 reps (0.00294 vs 0.00292 vs exact 0.00292) + E[√|Z|] MC-vs-quadrature (quadrature value **printed**, 0.822179) + π-darts ∝1/√M (ratio 9.69) — **PASS** (sev-3 wording only).
3. IS success P(Z>4)=3.167e-5, naive prints 0, shifted-proposal nails it, both SEs printed — **PASS** (84× SE reduction verified: naive SE 1.78e-5 / IS SE ~2.1e-7 = 84.7×).
4. IS failure, predict-first ESS guess, N(0,1)→t₃, weight histogram + max-share + ESS collapse — **PASS** (marquee; D1 approved).
5. ESS correct formula, three routes agree (all 34,698); booklet flag — **PASS** on formula (Cauchy–Schwarz ESS≤M ✓, M/(1+cv²) algebra ✓, 1/Σw̄² ✓); booklet flag adjudicated in D2.
6. Rejection w/ acceptance accounting (C=2.4576, 1/C=0.4069 emp 0.4068, E[trials]=C) — **PASS**.
7. Rejection-ABC, ε-sweep vs exact Beta(16,36), neighborhood framing, neural-SBI (M25) pointer — **PASS** (sd 0.1314→0.0871→0.0653 vs exact 0.0634 ✓).
8. Bridges: MC-dropout (heuristic-labeled ✓, M25) + off-policy=IS (RL) — **PASS** on framing; the RL bridge's *exercise* carries the sev-2.

## Independent recomputation list (all confirmed unless noted)

- E[√|Z|]: closed form 2^{1/4}Γ(3/4)/√π = **0.822179** = printed quadrature ✓
- P(Z>4) = 3.167e-05 ✓; needed-M for 10% rel MCSE = (1−p)/(0.01p) = 3,157,339 ✓
- IS SE reduction: 1.78e-5 / 2.1e-7 = **84.7×** ✓
- Weight 2nd moment ∫t₃²/φ **diverges** (infinite variance confirmed) ✓
- Kong ESS three-route algebra ✓; ESS≤M ✓
- d-ball d=10: π⁵/(2¹⁰·Γ(6)) = 0.002490 → 1/402 ✓ (d=20 → 4.06e7 ✓)
- Rejection C=Beta(2,5) pdf(0.2)=2.4576, 1/C=0.4069 ✓; E[trials]=C ✓
- Beta(16,36) sd = 0.0634 ✓; E[odds] a/(b−1)=8/3=2.6667 ✓
- Antithetic reduction = 1/(1+ρ): monotone e^Z → ρ<0 → 1.57×; even Z² → ρ=+1 → 0.50× (doubles). Monotonicity condition stated correctly ✓
- **1.8²⁰ = 127,482 ≠ 12,700** (sev-2) ✗; observed max-weight trajectory = 18/20 ones, weight ~1,574, not all-1 (sev-2) ✗
- Numbers-contract spot check (>6): 0.6663/0.8868/[0.4345,0.8649]/2.6657/0.00294/0.822179/3.148e-05/34,698/2.4576/0.3077/3,157,339/0.002490/7.9/1.57 all match printed ✓
- Citations: ch3 §3.1 (SLLN + MCSE=s/√M) ✓; ch5 IS §5.10 ✓, rejection §5.7 / envelope §5.8 (range mislabel, sev-3); SPINE-INDEX M02→M09 MCSE promise honored ✓; notation §3 (N=variance, t₃ Var=3) respected ✓

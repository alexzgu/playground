# Math review — modules/04-likelihood.md [SIGNATURE S3]

Reviewer: mathematical-statistics referee. Date: 2026-07-12.
Basis: BRIEF.md; STYLE.md §3/§4/§6/§8 (honesty-label rule as relaxed: literal Theorem/Empirical
tags optional when the warrant is adjacent; only Heuristic/Open must be tagged); SYLLABUS.md
§04-likelihood (binding, with the author's intentional sharpening of the Pitman–Koopman gloss
judged on correctness, not spec-verbatim); C-B `Ch1to5.txt` / `Ch6to10.txt`; booklet ch. 2.

**Verdict: REVISE (minor).** No severity-1 findings. The mathematics is correct throughout —
every number I recomputed independently matched. Three severity-2 items (one internally
inconsistent Takeaway bullet, one unsupported numeric claim, one silent scipy convention trap)
and nine severity-3 polish items. All fixes are one line each; S3 itself is flawless.

## Harness

- `python tools/run_module.py modules/04-likelihood.md --check-determinism`: **exit 0, PASS in
  ~3 s, zero warnings** (stderr captured and grepped; determinism diff clean; numbers-contract
  grep clean; no legacy `np.random.*`; no `plt.show`). 3,770 prose words (within 2,500–5,000);
  16 runnable blocks; 3 figures, all referenced and discussed; block 1 is the exact STYLE §4
  setup block with `SLUG = "04-likelihood"`; runtime header "~4 s" matches measurement.

## Findings

| Sev | Location | Issue | Concrete fix |
|---|---|---|---|
| 2 | Takeaways, bullet 3 | "**Exponential families** are the families with fixed-dimensional sufficient statistics" drops the fixed-support proviso that §04.3 itself just established — the module's own U(0,θ) foil (1-dim sufficient stat `max xᵢ`, not an exponential family) falsifies the bullet as stated. The retention layer contradicts the body's sharpened Pitman–Koopman point. | "Among families with **fixed support**, exponential families are exactly the ones with fixed-dimensional sufficient statistics; U(0,θ) escapes only by moving θ into the support." |
| 2 | §04.5 scope box | "yet it can inflate a frequentist Type-I rate **fourfold**" — a specific numeric claim that is neither printed by any block nor cited (STYLE §4.3, §6). The true inflation depends on the stopping rule and is unbounded under indefinite peeking; "fourfold" corresponds to some unstated design. | "yet it can inflate a frequentist Type-I rate severely — without bound as peeking continues (simulated in module 23)." |
| 2 | block 8, L215–216 | `stats.nbinom(3, 0.5)` is correct **only because θ₀ = 0.5**. scipy's `nbinom(n, p)` counts failures before the n-th *success* with success prob p; here the stopping event (tail) has prob 1−θ, so the general call is `nbinom(3, 1-theta)`. Verified: at θ=0.6 the module-style call gives 0.0059 where the correct tail is 0.1189. STYLE §3 requires convention traps be commented inline (as done for Gamma rate/scale). | Inline comment: `# scipy nbinom counts heads(=failures) before the 3rd tail(=success, prob 1−θ); equals nbinom(3, θ) only because θ=0.5 here`. |
| 3 | Header, Sources | "C-B §6.2 (sufficiency, ancillarity, likelihood principle)" — the LP is C-B **§6.3** (the body cites §6.3 correctly). | "C-B §6.2 (sufficiency, ancillarity), §6.3 (likelihood principle), §3.4 (exponential families)". |
| 3 | §04.6, Basu | Module states Basu for "a complete sufficient statistic"; the cited C-B 6.2.24 reads "complete **and minimal** sufficient". The module's version is the standard one and is correct (minimality is not needed for the proof), but it silently diverges from the wording of the source it cites. | Add "(C-B 6.2.24 states it with 'minimal' added; the hypothesis isn't needed)". |
| 3 | §04.3, Pitman–Koopman | Labeled "(Theorem, cited)" but no citation is actually given anywhere (the Sources line doesn't cover it; it is not in C-B). Also the classical theorem needs smoothness regularity beyond fixed support. | Cite by concept — "Pitman (1936), Koopman (1936), Darmois (1935); see Lehmann–Casella *TPE* by concept" — and add "under smoothness conditions" before "exactly". |
| 3 | §04.5 scope box | Callback "Exercise 04.4-style logic" is broken: Ex 04.4 is the Fisher-normal-vs-Beta interval exercise and says nothing about stopping rules (STYLE §8.6: callbacks point at real content). | "…does not bias a Bayesian's posterior (the §04.5 proportional-likelihood logic, proved in module 23)". |
| 3 | Pitfalls, bullet 2 | "the differing min/max of A and B suddenly matter" — the maxima are **equal** (both 12); only the minima differ (1 vs 2). | "the differing minima (1 vs 2) and raw values of A and B suddenly matter". |
| 3 | §04.4, last ¶ | Jeffreys prior called "the **unique prior invariant** to reparameterization" — imprecise and not a theorem as stated: it is the *construction rule* π ∝ √I that is equivariant (any fixed prior transforms by a Jacobian; uniqueness claims need careful framing). | "the prior whose construction rule is invariant to reparameterization (module 07 makes this precise)". |
| 3 | Ex 04.3, Reconcile | "it is *not* a useful sufficient statistic here" — Σxᵢ is not sufficient **at all** for the Cauchy location family; "useful" implies it is a (useless) sufficient statistic. | "it is not sufficient at all — and not even a useful summary". |
| 3 | Ex 04.1, Reconcile | "ten times the data gives √10 times the **precision**" — module 05 will define precision = 1/variance, under which the factor is 10, not √10; here "precision" means sd/width. (Also the measured sd ratio is 2.97, not √10 = 3.16 — the "≈" carries it, but the gap is the prior's pseudo-counts.) | "√10 times *narrower* (posterior sd)"; optionally note the 2.97 vs 3.16 gap is the Beta(1,1) pseudo-data. |
| 3 | §04.5 LP box | "two premises most statisticians already accept" — the *formal* sufficiency/conditionality principles used in Birnbaum's proof (and the proof itself) are contested (Mayo 2014, Evans); the informal versions are what's widely accepted. | "two premises that are individually widely accepted (the formal versions, and Birnbaum's proof, have their critics)". |

## Required-items checklist (SYLLABUS §04, 9 items)

1. **Likelihood as evidence summary, growing-n plot** — PASS. §04.1, prefixes n = 5/20/100 of one
   stream; "data's fingerprint" language present; figure `likelihood-growing.png` discussed.
2. **Sufficiency: factorization stated/used; Σx shuffle test; (Σx, Σx²) collision printed** —
   PASS. Thm 6.2.6 stated correctly (matches source verbatim in substance); shuffle test
   conditions on Σx = 3 of 8 at two θ; collision datasets share (6, 45, 427) exactly and the NIG
   tuple prints identically.
3. **Exp families: form, 4-row table, cumulants with ONE Poisson check; Pitman–Koopman** — PASS.
   All four table rows verified analytically (Bernoulli logit/x; Poisson log λ/x; Normal
   (μ/σ², −1/(2σ²))/(x, x²); Gamma-rate (α−1, −β)/(log x, x)). Poisson check 3.7000 vs
   3.7001/3.6944 printed. P–K statement as sharpened is **correct** (U(0,θ) as support-condition
   violator, Cauchy as the fixed-support price) — see sev-3 on the missing citation and the
   sev-2 on the Takeaway that un-sharpens it.
4. **Fisher information** — PASS. Definition, E[score] = 0 and Var = I(θ) simulated at the TRUE
   θ = 0.3 (score evaluated at the generating θ — the logic is right); I = 1/(θ(1−θ)) derivation
   correct; curvature figure; M07/M08 pointers present.
5. **S3 staged** — PASS, and it is the best section of the module. Predict-first with the naive
   "yes" named and held; 0.073 vs 0.033 with hand-computation cross-check printed (STYLE §6
   two-route rule); proportional likelihoods with constant ratio 4.0; shared Beta(10,4) overlay;
   "significant"/"not significant" verdict split stated.
6. **LP stated + honest design-stage scope note** — PASS. LP matches C-B §6.3 statement;
   Birnbaum 6.3.6 correctly invoked; the "p-value is a correct answer to a different question"
   framing satisfies the brief's no-tribalism clause; scope box present (two sev-2/3 nits above).
7. **Censored-likelihood seed** — PASS. S(c) contribution written correctly; 0.5376 = 5/9.3
   verified analytically (score equation 5/λ = Σy + c); naive 6/9.3 = 0.6452; M15 pointer.
8. **Ancillarity anchor (Basu instance)** — PASS. x̄ ⊥ residuals simulated (−0.0026, −0.0020);
   logic correct (x̄ complete sufficient for θ with σ = 1 known; residuals ancillary); M06 pointer.
9. **ML bridge box** — PASS. Dictionary table; MLE = ERM under log loss; all three minimizers
   recovered numerically; GLM deferred to M15.

## Independent recomputations (all matched)

- Binomial p-value: P(X≥9 | 12, ½) = (220+66+12+1)/4096 = **299/4096 = 0.072998** → `0.073`. ✓
- Neg-binomial p-value: P(≥9 heads before 3rd tail) = 1 − Σₖ₌₀⁸ C(k+2,2)(½)^{k+3} = **67/2048 =
  0.032715** → `0.033`; cross-validated via the equivalent event "3rd tail on flip ≥ 12"
  (identical fraction) and via scipy. Tail event correctly defined; observed X = 9 included. ✓
- Proportionality: C(12,9)/C(11,9) = 220/55 = **4.0**, constant in θ (checked 0.2/0.5/0.8). ✓
- Posterior: Beta(1,1) prior (stated) + 9 succ/3 fail → **Beta(10,4)**; mean 10/14 = **0.7143**;
  mode 9/12 = 0.75 = shared MLE. ✓
- Poisson cumulants: A(η) = e^η ⇒ A′ = A″ = λ = 3.7 exactly; sim 3.7001/3.6944 plausible at 2·10⁵. ✓
- Fisher info: 1/(0.3·0.7) = **4.7619**; observed info 10/(0.4·0.6) = **41.7**, 200/0.21 =
  **952.4** = 200·I(0.3); −ℓ″(θ̂) = n/(θ̂(1−θ̂)) rederived. Score sim at true θ — correct design. ✓
- Censored MLE: λ̂ = 5/9.3 = **0.5376** (likelihood with e^{−λc} term written and maximized
  correctly; analytic solution matches optimizer); naive 6/9.3 = **0.6452**. ✓
- Sufficiency collision: A, B both (Σx, Σx²) = (45, 427); NIG by hand: κₙ = 7, μₙ = 45/7 =
  **6.4286**, αₙ = 4, βₙ = 1 + 89.5/2 + 6·56.25/14 = **69.8571** (S = 427 − 6·7.5² = 89.5). ✓
- Shuffle test: 1/C(8,3) = **0.0179**; max deviations 0.0009/0.0014 consistent with kept-sample
  sizes (~101k at θ=0.3, ~50k at θ=0.6). ✓
- Basu demo: independence exact by Basu; sim correlations at 2·10⁵ are noise-level. ✓
- Exercises: Beta(10,4)/Beta(91,31) sds **0.1166/0.0393**, mean **0.7459** = 91/122; Ex 04.4
  Wald ±1.96·√(0.21/100) → **[0.210, 0.390]** vs Beta(31,71) **[0.219, 0.396]** (flat prior ⇒
  Beta(31,71) correct). ✓
- C-B Thm 3.4.2 reduces in canonical coordinates (wᵢ = ηᵢ, log c = −A) to A′ = E[T], A″ = Var[T]
  — the module's gloss is exact. ✓

## Citations checked against sources

Thm 6.2.6 ✓ (statement matches), Ex 6.2.3 ✓, Ex 6.2.9 ✓, Thm 6.2.10 ✓, Def 6.2.16 ✓,
Thm 6.2.24 ✓ (wording nit above), Def 6.3.1 ✓, LP ✓, Thm 6.3.6 (Birnbaum) ✓ — all in
`curriculum_material/casella_berger/Ch6to10.txt`; Thm 3.4.2 ✓ in `Ch1to5.txt`; booklet
`ch02-lecture-two.md` **§2.6 Likelihood Principle** ✓; Lindley–Phillips 9-of-12 attribution
by concept ✓ (correct provenance); Berger–Wolpert by concept ✓. Pitman–Koopman: no citation
given (sev-3). No R anywhere. Notation table respected (θ unknown, y data, N(μ,σ²) variance
convention untouched, ∝ used correctly).

## Numbers-contract semantic spot-check (≥6 required; 14 checked)

`0.600/0.500/0.510` (MLEs, matched to correct n) ✓; `0.0179/0.0009/0.0014` (θ-labels match
printed lines) ✓; `45/427/6.4286/69.8571` ✓; `3.7000/3.7001/3.6944` ✓; `4.7619/0.0007/4.7632`
(sim vs exact roles correct) ✓; `41.7/952.4` ✓; `0.073/0.033` (verdict sides of 0.05 correct) ✓;
`4.0/0.7143/0.75` ✓; `0.5376/0.6452` (correct vs naive roles correct) ✓; `-0.0026/-0.0020` ✓;
`0.3416/2.0267/2.0179/2.0178` ✓; `0.1166/0.0393/0.7459` ✓; `0.3175` (both roles: CE argmin and
0-1 loss value — coincide because the always-0 predictor's error *is* the sample frequency) ✓;
`[0.210, 0.390]/[0.219, 0.396]` ✓. No semantic mismatches found.

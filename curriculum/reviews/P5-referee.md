# P5-bounds-approximations — combined referee (math + pedagogy)

**Target:** `prereqs/P5-bounds-approximations.md`
**Verdict:** APPROVE (0 sev-1, 0 sev-2, 4 sev-3)
**Determinism:** `python tools/run_module.py prereqs/P5-bounds-approximations.md --check-determinism` → PASS in ~4–14 s, **zero warnings**, byte-identical second run. 2731 prose words (in 1,800–3,200), 11 exposition + 2 exercise blocks (≤14), 1 figure, runtime well under 60 s.

## Findings

| sev | location | issue | fix |
|---|---|---|---|
| 3 | P5.3 wall, `23:265` | The quoted "Type-I over multiple looks = P(union of rejections); every peek is another chance" is the **mining file's editorial gloss** (mined-14-26.md:287 note column), not a verbatim course line. `23:265` in the current module is code; the nearest matching prose ("every look is another chance to cross the line") sits at `23:250`. Faithful to the mining record and traceable, but presented in quotes as if a course line. | Either cite `23:250` and quote the real prose, or mark the union clause as a paraphrase. |
| 3 | P5.4 wall, `EXAM:219` | The quote is real ("the total-variation gap shrinks … the classic O(1/√n)") but the source **states the O(1/√n) TV rate directly**; it does not itself chain a triangle inequality. So it is a weak illustration of the *triangle* skill — the triangle framing is the author's, not the cited line's. | Keep, but add a half-sentence noting the triangle appears in the BvM *proof* (TV(post,N) ≤ TV(post,N₁)+TV(N₁,N)), which the cited homework line only summarizes. |
| 3 | intro L9 + §§P5.2/P5.4/P5.5/P5.7 | Intro promises "Every skill is staged Reflex → wall → fix → **Drill**"; only P5.1 has a labeled Drill and P5.3 (marquee) a Predict. Tail-family, triangle, 1/√n, and growth get **no committed-prediction drill**. House-consistent (P2/P3/P4/P6 also relax it), but under-delivers the module's own framing. | Add a one-line predict-then-run Drill to at least the 1/√n and tail-family sections, or soften the intro to "GATEs and the marquee are drilled; end-exercises drill the rest." |
| 3 | Takeaways L305; Pitfalls L243 | "assurance < power … for the same reason" is stated flatly; the honest scope (power is S-shaped, concave *only on the upper shoulder*) is carried correctly in the P5.1 wall ("on the concave shoulder of the S-curve") and in M23 itself, but the compressed takeaway drops it. | Add "(on the power curve's concave shoulder)" to the takeaway so the reflex isn't installed as unconditional. |

No sev-1/sev-2. The ELBO wall (`13:54`) is a light faithful paraphrase of the real Jensen line — acceptable.

## Math hat — checklist

- [x] Determinism PASS, zero warnings, byte-identical reruns.
- [x] **Jensen sign-rule correct:** convex g''>0 ⇒ E[g]≥g(E); concave flips. Anchor pair (x² / log) right; 1/x convex, sqrt concave; E[1/X]=1/(α−1)=1 for Gamma(2,1) printed `1.0008` vs `0.5000`.
- [x] **Three walls correctly attributed:** ELBO lower bound via log-concavity (`13:54`); assurance<power via concave shoulder — **honestly scoped** ("on the concave shoulder of the S-curve", `23:154`); EIG≥0 via entropy concavity (`23:412`). All three are one convexity check.
- [x] **Markov→Chebyshev→Chernoff→Ville one engine:** P(Z≥a)≤E[Z]/a; Chebyshev = Markov on (X−μ)² ⇒ 1/k²; Chernoff via e^{tX}. Nesting `0.2660 ≥ 0.1111 ≥ 0.0111 ≥ 0.00270` valid (note: e^{−k²/2} is a legitimate *two-sided* bound since 2Φ(−k) ≤ e^{−k²/2}). **Martingale condition stated**, not just "nonneg variable": "BF₁₀ under a true null is a nonnegative martingale with mean 1."
- [x] **Union marquee:** 10×0.05 = 0.50 ceiling computed on the *nominal* α (correct); M23 canon reproduced **exactly** — single `0.0522`, ten `0.2044`, continuous `0.4664`, Ville `0.0598 ≤ 0.1000`. Bound-vs-truth gap (0.50 vs 0.20) explained by **dependence/overlap** of looks; LIL divergence-to-1 noted correctly.
- [x] **Taylor section:** Laplace = mode(2)+curvature(0.5)⇒N(2,2), honestly distinguished from the mean(3); delta Var[g]≈g'(μ)²Var (Var[log X] `0.0100`/`0.0103`; sigmoid `0.01562`/`0.01395`); central-difference Hessian `H=(f(θ+h)−2f(θ)+f(θ−h))/h²` = `0.5000` (`EXAM:239`, verbatim); log(1+x)≈x ⇒ (1+1/m)^m→e `2.7169`/`2.7183`. Growth/LIL √(2t log log t) name-drop level, figure starts at t=16 (past e^e) — not overclaimed.
- [x] **Six+ wall quotes spot-checked at cited lines:** `13:54` ✓(paraphrase), `13:123` ✓verbatim, `23:154` ✓verbatim, `23:316` ✓verbatim, `23:412` ✓formula, `15:240` ✓verbatim, `22:251` ✓, `23:289` ✓verbatim; EXAM `180/219/239/669` all verbatim in EXAM.md and mining.

## Pedagogy hat — checklist

- [x] Drill-room format present: Reflex/Wall/Fix on all 7 skills; closing "Where the course uses this" cross-ref table with skill→reflex→module:line walls.
- [~] Drill per skill: only P5.1 labeled Drill + marquee Predict; 4 skills undrilled (sev-3 above; house-consistent).
- [x] **Marquee genuinely predict-first:** P5.3 Setup → Predict (commit a/b/c/d) → Reason (names the naive "each test is 5%") → Run → Reconcile (why 0.20 < 0.50 ceiling). Reader is caught wrong.
- [x] Exercises follow STYLE §5: P5.1 (reciprocal, surprising 2× gap), P5.2 (5-look penalty), P5.3 (sigmoid delta — the ML connection, and a genuine surprise: mean unbiased at a=0 while variance is real). Solutions in `<details>`.
- [x] Length/blocks/runtime within prereq bounds; local seeded generators used (STYLE §4.2 compliant).
- [x] Fluff scan: opens with concrete "clearly the ELBO is a lower bound" instances, no throat-clearing; every figure discussed.
- [x] Reads as reflex-installation: each section names the automatic move and its mechanical trigger (second-derivative sign, one engine, kα ceiling, curvature=precision).

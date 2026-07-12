# Pedagogy Review — 05-conjugate-updating.md (SIGNATURE S2)

**Verdict: REVISE** (one sev-2 defect, otherwise exemplary). Reviewer lens: does S2 match the
panel's worked exemplar, do the four mandates land, is every marquee surprise *captured* before
the reveal, and is it fluff-free at length.

## Findings

| Sev | Location | Issue | Concrete fix |
|---|---|---|---|
| 2 | §05.7 A/B test | Marquee line-4 demo with its own figure, but **no staged `Predict`**. STYLE §1: "A surprise shown without a captured prediction is a defect." The reveal *is* a surprise — `P(B>A)=0.9510` yet expected regret differs by ~2 orders of magnitude (`0.000199` vs `0.016134`) because the 5% of worlds where A wins cost almost nothing. The reader is never caught assuming "P(B>A)≈0.95 ⇒ obviously ship B, and by a comfortable margin." Audit item 5 explicitly lists the A/B decision as predict-before-reveal. | Insert a `**Predict.**` before the code: "Given `P(B>A)≈0.95`, is shipping B obvious? Commit to the *ratio* of ship-A's expected regret to ship-B's — 2×, 10×, or 100×?" Add a one-line `**Reason.**` naming the intuition being repaired ("a high win-probability = a clear-cut, high-margin decision"). Then let the ~80× reveal land. |
| 3 | Takeaways, S2 bullet (line 532) | Recurrence list is trimmed to "rule of succession and add-α" — the **trumpet / regression forward-pointer is dropped** from the one place built for week-later recall, even though 05.1 states all three. | Append "and M14's regression trumpet" so the takeaway carries the full recurrence triple the exemplar mandates. |
| 3 | §05.6 (line ~317) | The first widening reveal — Beta-Binomial predictive var `4.69` vs plug-in `2.34` — is show-then-tell (no `Predict`). Mitigated: the marquee coverage reveal right after *is* predict-first, and Exercise 05.2 predicts the SD ratio. So this is a polish item, not a defect. | Optional: a half-line "before running, guess the variance ratio" — or leave it and rely on Ex 05.2. No action strictly required. |
| 3 | §05.1 header, "why the MLE lies" | Header tone leans mildly sensational/tribal against BRIEF's non-tribalism mandate; the body is scrupulously even-handed (MLE = certainty-from-a-point artifact, not "frequentists wrong"), so the risk is cosmetic. | Optional soften to "why the MLE overreaches" / "why 100% is the wrong answer." Low priority — the reconcile already carries the fair framing. |
| 3 | §05.1 (line 80) | Callback "Laplace's rule of succession (module 00's coin: 6/7)" asserts a specific number sourced to another module. | Verify module 00 actually prints 6/7 for that coin so the cross-reference stays honest (out of this module's numbers-contract scope, but a broken callback is a defect under STYLE §8.6). |

## What passes (verified against exemplar + mandates)

- **S2 vs exemplar (§4):** faithful, arguably improved. Setup (2-of-2, Beta(1,1)) ✓; Predict commits to
  *both* posterior mean and posterior-predictive, names the naive intuition ("most guts say ≈1.0") ✓;
  Reason names the trusted intuition (trusting the point estimate) ✓; Run prints `0.75`/`0.75` ✓;
  Reconcile gives the pseudo-count reading ("3 effective successes and 1 effective failure"), the
  uniform-prior-isn't-no-information reading, the spine ("prior pseudo-data + real data … the whole
  module"), and the compression ("most overconfident exactly when you have least data") ✓. All three
  recurrences present in-prose: rule of succession, add-α (§05.5), M14 trumpet ✓.
- **Two-full-plus-compressed mandate:** exactly two full derivations (§05.3 Beta-Binomial, §05.4
  Normal-Normal); the other three live in one compressed "same move, new algebra" table (§05.5) with a
  single predictive twist each. Does **not** sprawl into five derivations. ✓
- **Master shrinkage as spine:** stated in the header, derived as a convex combination (§05.3),
  re-derived in precision form (§05.4), and foreshadowed as ridge / Kalman gain / partial pooling in
  §05.4, the Bridge, and Takeaways. Landed as THE spine. ✓
- **Gaussian toolkit (§05.8):** motivated ("the engine behind three later modules," named: M14/M20/M21),
  derived once, verified against brute-force sampling, kept tight. Not dry. ✓
- **Predict-before-reveal coverage:** predictive-wider — Ex 05.2 (predict SD ratio) ✓; plug-in coverage
  undershoot — §05.6 Predict ✓; add-α trap — Ex 05.3 predict-first, genuinely surprising ✓;
  **A/B decision — MISSING (sev-2 above)**.
- **Skeleton/fluff/figures/exercises:** all 12 sections present (spine block, 8 numbered, Bridge,
  Pitfalls, Exercises, Takeaways). Fluff scan: clean — no throat-clearing; the few rhetorical lines
  ("what honesty costs", "a posterior is not a deliverable") are load-bearing, not padding. 7 figures,
  all saved, all referenced, all discussed, titles state takeaways (STYLE §7). 4 exercises in full
  Setup/Predict/Reason/Run/Reconcile form; ≥1 surprising (05.2, 05.3), ≥1 ML bridge (05.3). ✓
- **Length/load:** 3,971 prose words (in 2,500–5,000); 16 runnable blocks (at the 16 ceiling); the
  strict-widening rigor caveat ("here, never always") is present. Dense but sequenced well
  (hook → why → two full → compressed → predictive → decision → infrastructure). Non-tribal throughout.

## Learner's-eye summary (5 lines)

1. The 2-of-2 opener genuinely caught me: I wrote ≈1.0 and the Beta(3,1) → 0.75 reveal reorganized how I read every small-n estimate after it.
2. "The prior is worth κ observations" plus the precision-weighted average is the one thing I could reproduce cold a week later — it's repeated in exactly the right places (Beta, Normal, Bridge, Takeaways).
3. The compressed three-pair table made the fourth and fifth derivations feel free; I never felt lectured, and the add-α language-model exercise stung in a way I'll remember.
4. The A/B section is the one place I coasted — I already "knew" B ships, so the loss asymmetry washed over me instead of hitting; a Predict line would have made it bite like S2 did.
5. §05.8 could have been dry infrastructure but the "powers three later modules" framing and the brute-force agreement made it feel earned, not homework.

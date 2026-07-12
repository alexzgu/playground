# 09-monte-carlo — Pedagogy Review

Verdict: **REVISE** (two sev-2 fixes; module is otherwise strong and ships-ready after them).

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 2 | §09.4 Reconcile + Pitfalls bullet 2 + Takeaway 4 | "ESS **falls as M grows**" is literally false and sits in the module's emotional core. Printed sweep is a *fraction* (median ESS/M): 62.65%→12.27%. But absolute ESS **rises** 626→4,438→27,760→122,700. A sharp learner (the one this arc is built to impress) who reconstructs absolute ESS from the printed % sees it climbing and loses trust in the punchline. | Say "the ESS **fraction** collapses" / "ESS grows *sublinearly*" everywhere the tell is stated. Keep the healthy-estimator contrast as "healthy ESS grows *linearly*, so ESS/M holds flat; here ESS/M collapses toward zero." One-word discipline (fraction) throughout §09.4, the pitfall, and the takeaway. |
| 2 | Whole module | 18 runnable python blocks vs the §2 cap of 16. Driven by good practice (figure blocks split from compute), but the number is over. | Merge the two figure blocks that consume only their immediate predecessor's variables: (a) fold `# figure: the 1/sqrt(M) convergence wall` into the `# 09.2 -- pi by darts` block (it uses only `grid, rms`); (b) fold `# figure: ABC posterior tightening` into the `# 09.6` ABC block (it uses only `abc_keep`, `exact_post`). 18→16, zero narrative loss. Leave the `is_weights` figure separate (it legitimately reuses the sweep across a section boundary). |
| 3 | §09.4 Predict beat | The predict question offers two naive reads ("~80,000" vs "a handful"); the actual 34.7% sits *between* them, so neither camp is cleanly "caught" on the number itself — the real catch is that 35k coexists with a 44%-wrong answer. The staging works but the surprise is one level indirect. | Tiny tightening: after "Commit to a number," add a half-line making the trap explicit — "whatever number you pick, notice you are about to treat it as a safety certificate." Sharpens why *both* camps lose. Optional. |
| 3 | §09.4 safe-direction claim | Prose: median ESS "holds flat near `92.1`%". Log drifts 92.10→91.97. Fine as written, but "near 92.1% at every scale" slightly overstates flatness. | Acceptable; if touched, "near 92% at every scale" is cleaner. |
| 3 | §09.1 | "reproduces the exact posterior mean 0.6663 (exact 0.6667)" — calling the MC value "the exact" is loose phrasing. | "recovers the exact posterior mean to `0.6663` (exact `0.6667`)". Cosmetic. |

## Audit results (what passed)

- **Spine:** Organized tightly around it. §09.1 samples-as-lingua-franca → §09.2 error-bar-is-the-result → §09.3/4 IS success→silent-failure. "Report the MCSE" recurs in §09.2, Pitfalls, and Takeaway 2 — it reaches reflex level. PASS.
- **IS-failure arc:** Lands as genuinely disturbing. The single-run ESS (34.7%, max-weight 0.29%) *passing* while the answer is 44% wrong is the "diagnostics can lie" gut-punch, and "just shipped a badly biased number" earns it. Escalation works→fails silently→median-ESS decay is well paced; the added median-decay sophistication does NOT muddy the simpler lesson — it *is* the lesson (one run's ESS is itself random). Only defect is the fraction/absolute wording above.
- **Predict-before-reveal (all three genuine):** rare-event naive MC (predict 10–11/12 within 10%, actual 2/12 — captured, surprising); guess-the-ESS (committed number before run); ABC sweep (committed "still >1 in 5 at ε=0.02?" → no, 1 in 17). All staged per §1, all caught the reader. PASS.
- **M05 callback:** Concrete — Beta(1,1)→7/10 heads→Beta(8,4), exact mean 8/12, named "module 05's coin." PASS.
- **Fluff:** None found. Every opener is a claim/situation; no throat-clearing.
- **Figures (3):** sqrtM_wall, is_weights, abc — all referenced AND discussed (slope −½ wall; weight-histogram + collapse; ε-tightening). Titles state takeaways. PASS.
- **Skeleton:** All six header lines, sections, Bridge, Pitfalls, Exercises, Takeaways present. PASS.
- **Exercises (4, §5 format):** 09.1 (surprising: 3.2M draws vs "10⁵ almost enough"), 09.2 (surprising+ML: 1-in-402 vs "1-in-3", ties to typical set M12), 09.3 (ML: off-policy ESS→7.9, real RL), 09.4 (surprising: antithetic *doubles* variance on an even g). Surprises genuine, ML bridges real, every Reconcile explains the WHY (mechanism, not just the number). PASS.
- **Numbers contract:** Spot-checked ~45 prose backtick numbers against the run log — all present and precision-matched. PASS.
- **Length/voice/tribalism/bridges:** 4,370 words (in band). Voice dense and dry. No paradigm tribalism. MC-dropout and off-policy bridge boxes are one paragraph each, blockquoted, MC-dropout correctly labeled **heuristic** — sized as bridges, not detours. PASS.

## Learner's-eye summary (5 lines)

1. I finish able to state the spine cold: every posterior summary is a `mean()` over draws, and the MCSE is the claim, not decoration — that reflex is installed.
2. The §09.4 gut-punch (ESS "looks fine" at 35% while the answer is 44% wrong) genuinely reorganized my trust in diagnostics; it's the best thing in the module.
3. But if I reconstruct absolute ESS from the printed fractions and see it *rising*, the "ESS falls" line briefly makes me doubt the author — fix the wording and the punch is clean.
4. The three predict beats actually caught me (2/12, not 10/12; 1-in-17, not 1-in-5), which is why the lessons stuck rather than washed over.
5. Nothing felt like filler and every number I checked was real; my only friction is block sprawl, which I never noticed as a reader — only as a spec-checker.

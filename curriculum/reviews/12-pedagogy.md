# Pedagogy review — modules/12-hmc.md  [SIGNATURE S1]

Reviewer verdict: **APPROVE** (with one structural flag for the orchestrator and two cheap staging upgrades). Judged to the S1 bar — the signature lands.

## Findings

| Sev | Location | Issue | Concrete fix |
|---|---|---|---|
| **Moderate** (structural) | Whole module; block 10 (`print("optimal acceptance: RW-Metropolis = 0.234 vs HMC = 0.651")`, line 276) | **Runnable-block cap exceeded: 17 runnable + 1 no-run.** STYLE §2 caps runnable blocks at 16. The no-run PyMC block is correctly exempt, so the count is genuinely 17. Not a pedagogy defect but a contract breach the harness gate will notice. | Merge the one-line block 10 into the preceding stability-cliff block (block 9) — the `0.234 vs 0.651` print belongs with the paragraph that introduces the asymmetry anyway. Drops to 16 with zero content loss. Flagged for orchestrator per instructions; recommend the merge over claiming a no-run exemption (the exemption doesn't apply — 17 are runnable). |
| **Moderate** | §12.5, funnel (lines 283–314) | **Marquee demo shown without a captured prediction.** The prose ("the centering … manufactures exactly the varying-curvature trap") and the code comment ("the centered parameterization diverges at the neck") both reveal the outcome *before* the run. STYLE §1: "A surprise shown without a captured prediction is a defect." The centered-fails/non-centered-works reversal is exactly the "model talking back" moment that should catch the reader. | Add a one-line Predict before the centered run: *"Predict: run both parameterizations. Which chain reaches the bottom of the neck (large negative v), and which throws divergences? Commit before running."* Then let the `13` vs `0` and `-1.97` vs `-10.01` be the reveal. Cheap; converts the payoff figure into a genuine predict-then-reveal. |
| Minor | §12.4, stability cliff (line 252, "Watch it.") | The 2.00-vs-2.01 cliff is staged as "Watch it" — vivid, but not an explicit captured prediction for the marquee reveal. Partially covered by Ex 12.1, which *does* predict a cliff shift. | Optional: prepend "before running, commit — does 2.01 degrade gracefully or catastrophically?" The derived threshold ε_crit=2/ω already functions as the theory-prediction, so this is an enhancement, not a defect. The line "A divergence is not a mysterious warning; it is this exact mechanism firing" lands hard — keep verbatim. |
| Minor | Exercises (3 shipped) | Three is the STYLE §5 minimum. Both required flavors are present and excellent (12.2 genuinely surprising `0.000000`; 12.3 ML/DL SGD-temperature bridge). But the module's single most practical takeaway — non-centering — has no exercise; its predict-then-run currently lives only inside the §12.5 narrative. | Consider a 4th exercise: predict divergence counts for a *shallow* funnel (σ_v=1 vs 3) before/after non-centering — reinforces "match parameterization to where the information is" (Pitfall 3). Not blocking; 3 high-compression exercises is defensible given length/block pressure. |
| Nit | Line 63 | "Not one of the twenty thousand thousand-dimensional draws" reads as a stumble ("thousand thousand-dimensional"). | Reword: "Not one of the 20,000 draws in 1000 dimensions lands within half that radius". |
| Nit | §12.5 Reconcile (line 324) | The geometry explanation is strong ("benign, roughly-spherical bowl") but never explicitly frames the divergence flags as *the model reporting its own pathology*. | One clause: "The divergences are the model telling you its geometry is unsurvivable at this step size — read them, don't delete them." (Pitfall 2 already says the latter; a callback here would close the loop.) |

## Audit resolutions (for the record)

- **S1 staging (item 1): PASS to the highest bar.** The naive "mass at the mode" answer is explicitly captured and named (plug-in-at-MAP / init-at-mode / Laplace) with "Commit to that answer. It is wrong" *before* the code reveal. The Reconcile connects the shock to BOTH consequences — line 85 names plug-in-at-the-mode failure *and* random-walk failure ("that is the wall module 10's Metropolis sampler hits, and we can measure exactly how fast") — so §12.1 motivates the entire module, not just the donut. This is the strongest part of the module.
- **Arc (item 2): builds, does not fragment.** Every section ends by motivating the next (measure the wall → RW death → "the fix is to stop proposing blind steps" → hard ceiling → funnel → practice). Continuous, not a topic list.
- **PPL box (item 5): PASS.** Four names, each tied to a *role* (why NumPyro here, PyMC-for-orientation, Stan read-only, ArviZ diagnostics), PyMC correctly `no-run` labeled. Informative, not a product survey.
- **Numbers contract: PASS.** All 25+ prose backtick-numbers verified ⊆ printed log output at matching precision (31.61, 0.71, 500, 0.239, d^-0.94, 2492, 0.981, 0.910, 2.00, 2.01, 0.651, 13, 0, -1.97, -10.01, 1.0174, 1.1376, 0.2567, ...).
- **Figures (5): all referenced with real captions AND discussed in prose.** typical-set, rwm-decay, leapfrog-trajectory, energy-error, funnel. No orphans.
- **Math spot-checks: correct.** ε_crit=2/ω (harmonic-oscillator leapfrog eigenvalue), O(ε²) energy error, SGLD stationary var 1/(1−ε/4) (AR(1) algebra confirmed), tempered var = T/(1−ε/4) ≈ 0.256 = tempering to N(0,T). Notation (variance-second-arg) consistent throughout; **no R anywhere**.
- **SGLD (item 6): correctly sized as a teaser** — one section, one block, explicit module-25 forward pointer, framed as the HMC→SGD bridge.
- **Length: 3,730 prose words** — comfortably inside the 2,500–5,000 band. Voice is exemplary ("The mode is in a desert.", "it does not shuffle, it *arcs*.").

## Learner's-eye summary (5 lines)

1. I was asked where the mass of a 1000-D Gaussian lives, said "the mode," and got caught — hard — that reorganized everything downstream.
2. I now understand *viscerally* why RW-Metropolis dies (measured 1/d power law, 2492 steps per draw) and why gradients+momentum are the escape, not a trick.
3. Leapfrog-from-scratch plus the O(ε²) and ε_crit=2/ω checks made "a divergence is the stability cliff firing" feel mechanical, not mystical.
4. The funnel would have hit harder if I'd been forced to *guess* which parameterization dies before seeing 13-vs-0 — I was told the answer first.
5. I could reproduce the typical-set argument, the divergence mechanism, and non-centering from memory a week from now — the compression is real.

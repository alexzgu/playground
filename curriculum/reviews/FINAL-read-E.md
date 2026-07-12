# FINAL fresh-read E — modules 17, 18, 19, 20, 21, 23, 24, 26

Hunt target: silent code bugs (wrong indexing that runs but computes the wrong thing) and
prose-figure/caption mismatches, plus typos / garbled markdown / flow breaks.

Method: read every module in full; opened all 33 PNGs and compared against captions, alt-text,
and Reconcile prose; cross-checked every quoted number against `tools/logs/<slug>.out.txt`;
re-ran the one suspicious computation (module 21 tracking ellipses) from source to confirm.

## Findings

| sev | module:line | issue | fix |
|---|---|---|---|
| 1 | 21-state-space:132, 199, 201 | **Prose-figure mismatch + wrong Reconcile.** §21.2 Predict asks whether the 2σ position ellipses are elongated along/across motion; naive intuition = "isotropic R ⇒ a circle." The Reconcile asserts "the circles the isotropic-R intuition predicted are **not** what the figure shows … the ellipses tilt along the direction of motion … more uncertain ahead than across," and the caption/alt-text say the ellipses "shrink and orient along the direction of travel." But the position-covariance block `P[:2,:2]` is **exactly isotropic** at every step (re-ran: eigenvalue axis-ratio = 1.000 for all t). The x- and y-subsystems are decoupled and identical (F, Q, R, and initial `P=10·I` are all axis-symmetric), so `P[0,0]=P[1,1]`, `P[0,1]=0` always. The figure correctly shows **circles**; the naive intuition is right and the whole beat resolves to the wrong answer. | The code/figure are correct — fix the prose. Either (a) rewrite Predict/Reconcile/caption to say the ellipses are circles *because* the two axes are symmetric (velocity coupling inflates position uncertainty equally in x and y, so no elongation), which is itself a clean lesson; or (b) break the symmetry so elongation actually appears (e.g. anisotropic process noise, or plot the along/cross-track error of a curved single-axis track) and keep the current narrative. |
| 2 | 23-experimental-design:601-602 | **Revision scar tissue / broken markdown.** Two stray closing tags `</content>` and `</invoke>` at the very end of the file (leftover from a tool-call wrapper). They render as literal text after the last takeaway. | Delete lines 601-602 (`</content>` and `</invoke>`). File should end after the "The design justifies the test" takeaway. |
| 3 | 23-experimental-design:154 | **Minor over-claim in Reconcile justification.** "at n=63 the non-centrality already exceeds the critical value **across the prior's mass**, which is Φ's concave region." The power curve is concave only for δ > z/√(n/2) ≈ 0.35; the prior N(0.5,0.2²) puts ~22% of its mass below 0.35 (the convex/steep region). The headline conclusion (assurance 0.714 < power 0.801 by Jensen) is correct and robust — the concave bulk dominates — but "across the prior's mass" is imprecise. | Soften to "across most of the prior's mass" or "over the bulk of the prior's support (δ ≳ 0.35)". |

## Per-module verdict

- **17 model-checking** — CLEAN. 3/3 figures match; all quoted numbers (PPC p 0.000/0.611, evidence peak deg 3, PSIS/WAIC/LOO, Lindley BF 1.80→17.93, power 0.514, replication 0.499) match log.
- **18 scale-and-misspecification** — CLEAN. 3/3 figures match; winner's-curse, local-fdr (166 vs 174), EB width ratios, horseshoe (RMSE 0.033, κ split), sandwich (0.0739/0.1019/0.1046), η*=0.526 all match log. (File is git-modified vs HEAD but prose matches the tracked log.)
- **19 mixtures-dp** — CLEAN. 6/6 figures match; EM/Gibbs uncertain counts (24 vs 38), label-switching midpoint 1.70, tempering 0.000/0.532, CRP digamma vs α ln n, stick-breaking, DP posterior K=4 all match log.
- **20 gaussian-processes** — CLEAN. 6/6 figures match; two-routes 1.14e-14, RBF limit, noiseless/noisy band, ML-II peak ℓ=1.581, KRR 8.02e-09, BayesOpt −6.0207, NNGP kurtosis collapse & corr lock all match log.
- **21 state-space** — **ONE SEV-1** (tracking-2d ellipses above). Everything else clean: kalman-1d, ar2-posterior, ou-filter, pf-ess figures match; all numbers match log.
- **23 experimental-design** — **SEV-2 stray tags + SEV-3 minor**. All 6 figures match captions; every number matches log (confounded 5.288, assurance 0.714, Type-I 0.2044/0.4664, Ville 0.0598, factorial effects, EIG −0.750, permutation 0.0311).
- **24 causal** — CLEAN. 6/6 figures match; ATE 1.9987, Simpson −0.1428/+0.1013, collider partial −0.503, confounder-vs-collider 2.001/0.504, IPW trio & ESS collapse 16.4%, two-DGP [0.3,0.2,0.2,0.3] all match log.
- **26 capstone** — CLEAN. Ledger cross-references consistent with source modules; marginalize-vs-profile (t width 2.548 vs 1.943, coverage 0.9508 vs 0.8942) matches log; figure matches.

## Counts
- Sev 1: 1  (module 21 tracking ellipses — false "elongated along motion" claim; figure shows circles)
- Sev 2: 1  (module 23 stray `</content></invoke>` tags)
- Sev 3: 1  (module 23 "across the prior's mass" imprecision)

No silent indexing/broadcasting bugs found in any module's figure-generating code (checked fancy
indexing, axis args, suffix-sum in DP Gibbs, IPW/pcorr, GP einsum quadratic forms, KF covariance
blocks). The one figure that looks wrong (tracking-2d) has *correct* code — the defect is the prose
describing it.

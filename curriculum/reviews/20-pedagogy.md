# Pedagogy review — 20-gaussian-processes.md

**Verdict: REVISE (minor).** Content-complete, arc lands, numbers contract clean (every backtick number ⊆ harness log), all 7 syllabus requirements present, all 4 predict-before-reveal demos genuinely staged. Two medium fixes and two low ones stand between this and APPROVE; none touch the math or the spine.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| **med** | §20.3 Reconcile, "the posterior variance is `1.02e-06` — numerically zero (it equals the jitter)" | Wrong attribution. The block runs with `sn2=1e-6` and `jitter=1e-8` (100× smaller). The floor `1.02e-06` is set by the **assumed noise variance** `1e-6`, not the jitter. A careful learner is told the wrong quantity sets the residual — a bad warrant in a module whose whole §20.3 thesis is "the noise level is the dial." | Change parenthetical to "(it equals the assumed noise variance `1e-6`)". Optionally add: the jitter `1e-8` sits an order of magnitude below and only guarantees PD-ness. |
| **med** | Exercise 20.4 vs §20.7 Reconcile | Surprise pre-spoiled. §20.7 already reveals "the two-point correlation *locks on* — `0.835` … `0.842` … it does **not** keep drifting." Ex 20.4 then asks the reader to *predict* whether corr "shifts by a comparably large amount, or barely moves" and reveals `0.832`→`0.842` — the identical fact, same widths, same `net_samples` call. Per STYLE §1 the reader cannot be "caught being wrong" about something the body already told them; the predict-then-run contract is hollow here. | Repurpose 20.4 to a genuinely open question, e.g. compute the *analytic* NNGP kernel corr from the tanh activation and match it to the empirical `0.842` (closes the "kernel computable from the activation" claim in §20.7), or vary the activation/prior-scale and predict the correlation's direction. Keep it the ML-bridge exercise. |
| low | §20.8 BART bullet | Syllabus item 8 specifies "BART **mention** ('another prior over functions — trees')"; here it runs to ~3 sentences (kernel-vs-jumps contrast + discontinuity/high-dim claim + reading-map). Mild scope creep for a stated one-line teaser. | Trim to one sentence; the "sum of piecewise-constant jumps handles discontinuities" clause can stay as the single differentiator. |
| low | §20.7 NNGP scope | Syllabus calls NNGP a *teaser, one figure* — figure count is honored (1), but the section is a full signature-grade Predict→Run→Reconcile plus a dedicated exercise, heavier than "teaser." Not a defect (the audit itself requests predict-before-reveal on the NNGP sweep), but combined with the 20.4 redundancy it's over-invested relative to BayesOpt. Fixing 20.4 absorbs most of this. | No action beyond the 20.4 fix; optionally tighten §20.7 prose by one paragraph. |

## What passes (verified, not assumed)

- **Demystification arc:** intro names the kernel *as bookkeeping* ("the n×n matrix of inner products … name that matrix the kernel and you never touch the weights again") **before** any mystique; §20.1's two-routes check (`1.14e-14`) then *proves* the bookkeeping is exact, and the ∞-limit (`5.432e-01`→`1.110e-16`) lands "a GP is module 14 at M=∞" as the payoff. Kernel arrives as leftover, never as magic. Strong.
- **Kernel gallery §20.2:** four kernels drawn AND discussed individually (RBF lengthscale morph highlighted as "the single most important knob," Matérn roughness, periodic repeat, linear lines) — not a grid dump; visual-intuition mandate met.
- **ML-II foil §20.4:** Occam made *felt* — at `ℓ=0.05` the fit term is best (`-12.412`) yet evidence craters (`-32.637`); at the ML-II optimum fit is worse (`-13.392`) but evidence wins (`-6.573`). "Fit better, evidence worse" is explicit; tagged S5/M17 in function space. Decomposition signs are internally consistent (small ℓ → near-identity Gram → large |K_y| → biggest complexity penalty).
- **Collapse / off-support §20.3:** staged Predict→Run→Reconcile; band pinches to `1.02e-06` at data, reverts to `0.9834` (prior) off-support; noisy-vs-noiseless narrated as one dial.
- **Predict-before-reveal:** two-routes, collapse, ML-II foil, NNGP sweep all have Setup→Predict→Reason(named intuition)→Reconcile.
- **Exercises (4):** 20.1 periodic-extrapolation surprise genuine (`0.0000` vs `0.6010`); 20.3 two-lengthscale surprise genuine (super-exponential forgetting, `0.9908` by 2ℓ); ≥1 ML bridge present. Only 20.4's surprise is compromised (above).
- **Callbacks real:** `gaussian_condition` is byte-identical to module 05 (docstring aside); M14 "finite basis at M" and M17 "evidence = fit + complexity" are load-bearing, not decorative.
- **Skeleton/figures/length/voice:** header block complete; 6 figures all referenced and discussed; 10 exposition + 4 exercise blocks; ~4,323 words (in band); no throat-clearing; 7 takeaways.

## Learner's-eye summary (5 lines)

1. I came in thinking a GP was mystical; §20.1 killed that in one image — it's module 14 with the weights integrated away, and the two routes agreeing at `1e-14` made me believe the kernel is bookkeeping, not magic.
2. The gallery finally showed me what a "smoothness assumption" *looks* like — I can now read RBF-vs-Matérn-vs-periodic off a picture and I understand lengthscale as a wiggle dial.
3. The ML-II section caught me: I predicted the tiny lengthscale would win on evidence (it fit best) and it lost hard — I felt Occam instead of being told about it.
4. One snag: §20.3 told me the residual "equals the jitter" when it plainly equals the noise variance I set — a five-second stumble in the one section arguing that noise is the dial.
5. Exercise 20.4 asked me to guess something §20.7 had already spoiled two pages up, so I couldn't be surprised; every other exercise reorganized an intuition, this one just repeated one.

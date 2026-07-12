# FINAL-read-D — fresh-reader proofread (modules 09, 10, 11, 13, 14, 15)

Hunt target: silent code bugs (wrong-but-plausible numbers), prose↔figure mismatches, typos/garbled LaTeX, flow/Predict-Reconcile breaks.
Method: read every line; cross-checked every printed value in prose against `tools/logs/*.out.txt`; opened every PNG in `figures/<slug>/` against caption + alt-text + discussion; re-derived the fancy-indexing / einsum / Hessian ops by shape and intent.

Headline: **no severity-1 silent code bug found** in these six modules. Every printed quantity matches its log, and every quadratic-form / weighted-Hessian / fancy-index computation (`einsum("ij,jk,ik->i", ...)`, `(X.T * w) @ X`, `Y[mask,1]`, `p[:,0]**2+p[:,1]**2<=1`) computes what the prose claims. Findings below are figure-rendering / alt-text mismatches.

| sev | module:line | issue | fix |
|---|---|---|---|
| 2 | 15-glms-classification.md:128-137, 140 (separation.png, right panel) | The loop plots three "separating lines" at `t = 1, 4, 16` via `-(b[0]+b[1]*xs)/b[2]` with `b = t*w_dir`. The scalar `t` cancels exactly in that ratio, so all three boundary lines are **mathematically identical** and overplot — only the last (red, ‖w‖=16) is visible. The legend advertises three lines and the alt-text describes "three separating lines of increasing steepness," but the rendered figure shows one line, and boundary *steepness* (the thing meant to grow) is invisible in an x0–x1 boundary plot. | Either drop to a single boundary line and rewrite caption/alt-text to "the boundary is fixed; only the sigmoid's sharpness perpendicular to it grows" (the actually-true point, already in the title "same boundary"), or visualize steepness by coloring the region with `σ(t·w_dir·x)` at each t so the sharpening transition is actually shown. |
| 3 | 15-glms-classification.md:227 (three-ways.png alt-text) | Alt-text says Laplace "tracks them with a slight **leftward** shift on the steepest coefficient." For β2 (negative), Laplace mode −0.803 is *closer to zero* than the mean −0.903, i.e. shifted **rightward/toward zero** — as the body text at line 229 correctly states ("closer to zero"). Alt-text direction is wrong. | Change "leftward shift" → "rightward shift (toward zero)" to match body text and figure. |
| 3 | 15-glms-classification.md:404 (gen-vs-disc.png) | Log-scale x-axis (n = 20,40,80,160,320,640) renders overlapping minor-tick labels ("2×10³×10⁶×10¹…") that are garbled/unreadable on both panels. Data and trend are correct; only tick labels collide. | Set explicit ticks: `a.set_xticks(ns); a.set_xticklabels(ns)` and `a.minorticks_off()`. |
| 3 | 09-monte-carlo.md:262-271, 274 (is_weights.png) | The two subplots use full-width titles set via `ax[k].set_title`; the left title ("Failure: normalized weights span orders of magnitude") and right title ("Median ESS fraction collapses…") **overlap in the center**, rendering both partly unreadable where they collide. Marquee-section figure. | Shorten both titles, or wrap (`\n`), or reduce `fontsize` / add `fig.subplots_adjust(wspace=...)` so the two titles do not collide. |

## Per-module verdict

- **09-monte-carlo** — CLEAN on content; all values match log; abc/sqrtM_wall figures correct. 1 finding: overlapping subplot titles on is_weights.png (sev 3).
- **10-metropolis-hastings** — CLEAN. Every printed number (0.234 sweep, bimodal 0/2798 crossings, fooling R̂ 1.7365/ESS 6.1, spectral λ2=0.8) matches log; 4 figures match captions. 0 findings.
- **11-gibbs-augmentation** — CLEAN. Gibbs=MH ratio, KS p-values, ρ² law, probit/missing-data/RB numbers all match; 5 figures correct (imputed posterior mean ≈0 sits on true-mean line as described). 0 findings.
- **13-laplace-em-vi** — CLEAN. ELBO identity, logit-Laplace KL (0.0264/0.0022), 1−ρ² law, CAVI-NIG sd ratio 0.8944, SVI/NUTS 0.700 ratio, all exercises match log; 6 figures correct. 0 findings.
- **14-bayesian-regression** — CLEAN. Trumpet decomposition, ridge=posterior identity, CV/EB corr 0.795, Student-t multipliers (1.076/1.011/1.125), robust-t weights, all match; 5 figures correct. 0 findings.
- **15-glms-classification** — content CLEAN (every value across all sections + 4 exercises matches log; einsum Hessians and offset/censoring likelihoods all correct). 3 figure/alt-text findings (1 sev-2, 2 sev-3).

Counts: sev-1 = 0, sev-2 = 1, sev-3 = 3.

Worst finding: **15:separation.png** — code intends three lines of "increasing steepness" but the boundary formula is scale-invariant, so all three coincide and only one renders; the legend and alt-text promise three that the reader cannot see. The one thing that IS true ("same boundary") is already in the title, so the fix is to align caption/legend with what the plot can actually show, or to render the sigmoid sharpening explicitly.

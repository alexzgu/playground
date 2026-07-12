# FINAL fresh-read C — modules 00, 01, 03, 04, 05, 06, 08

Scope: hunt for silent code bugs (wrong indexing/axis/broadcasting that runs but computes the
wrong thing), prose-figure mismatches, typos/garbled LaTeX, flow breaks, Reconcile-vs-Predict
drift, and self-resolving exercise solutions. Every ```python``` block was cross-checked against
its harness log in `tools/logs/*.out.txt`, and every PNG in `figures/<slug>/` was opened and
compared to its caption + surrounding prose.

Headline: **no silent code bugs found (sev 1 = 0).** All backtick numbers match the logs; all
figures match intent. One real rendering defect (sev 2) and three minor caption/visual
imprecisions (sev 3).

| sev | module:line | issue | fix |
|---|---|---|---|
| 2 | 00-four-lines:206 | Unescaped `$1` in prose ("over a million **$1** bets"). The line then holds 5 `$` (odd): the stray `$` pairs with the following `$\theta$` spans, so a MathJax/KaTeX renderer typesets "1 bets — … which single " as inline math — garbling the reconcile paragraph of the coin-bet centerpiece. The course convention escapes literal dollars (cf. 01:16, 01:20 use `\$1`); module 00 has zero escaped `$`. | Escape as `\$1 bets` (and audit for any other literal `$` in prose). |
| 3 | 01-probability-as-logic:117 | calibration.png caption: "the overconfident forecaster **bows below** it." The orange curve actually crosses the diagonal at 0.5 — it sits *above* the diagonal for stated prob < 0.5 and *below* for > 0.5 (correct overconfidence S-shape). "Bows below" describes only the right half. | Reword, e.g. "bows away from the diagonal — above it for low probabilities, below for high." |
| 3 | 08-frequentist-bridge:73 | mle-asymptotics.png: the density histogram is visibly taller (peak ≈1.4) than the overlaid Gaussian (peak ≈1.09) because the Poisson sample-mean support (spacing 1/30) aliases against 60 bins → alternating tall/short bars. Caption says "the two coincide"; text honestly reports KS=0.0256, but a fresh reader sees a mismatch. | Optional: align bins to the 1/30 lattice (or bins=30), or soften caption to note discreteness. |
| 3 | 08-frequentist-bridge:216,221 | bvm-convergence.png middle panel (n=50) shows the posterior (~0.76) and MLE sampling law (~1.0) clearly *separated* under a "…fuses with…" title and a "TV=0.145" label — but that TV is the *centered* TV (computed on `post-post.mean()`), while the plot is uncentered; the offset is that dataset's low MLE. Explained in the body text, but the panel-vs-title tension can confuse. | Optional: add a one-line panel note ("centered TV") or center the plotted curves. |

## Per-module verdict

- **00-four-lines** — CLEAN except the sev-2 `$1` rendering bug (206). Numbers, 3 figures, all exercises verified against log.
- **01-probability-as-logic** — CLEAN; one sev-3 caption wording (117). de Finetti trio, Dutch book, Pólya-urn↔Beta-Binomial (1e-17), exercises all match.
- **03-generative-stories** — CLEAN. Poisson-process 4 faces, Cauchy IQR≈2, KL asymmetry, maxent→Exp/Normal/Geometric, softmax all verified.
- **04-likelihood** — CLEAN. S3 two-labs p=0.073/0.033 with shared Beta(10,4), sufficiency-collision (Σx=45, Σx²=427), nbinom convention trap handled correctly, censoring, Basu independence all match.
- **05-conjugate-updating** — CLEAN. Shrinkage slide, NIG→t_22 predictive, add-α, A/B regret ratio 81×, Gaussian block conditioning all verified; nbinom(r=a, p=b/(b+1)) parameterization correct.
- **06-estimates-are-decisions** — CLEAN. loss→estimator, newsvendor fractile, lasso-mode-vs-mean (0.2410 vs 0), two-point uniform γ(r), prior-averaged coverage all verified; no exercise resolves its own Predict.
- **08-frequentist-bridge** — CLEAN code; two sev-3 figure/caption notes (73, 216). Stein dominance, JS=empirical-Bayes B̂=(d-2)/‖X‖², BvM TV 0.167→0.017, Neyman-Scott σ²/2, complete-class risk set all verified.

**Worst finding:** 00-four-lines:206 — an unescaped `$1` in the flagship module's coin-bet
reconcile makes the surrounding prose render as broken inline math (sev 2). Everything else is
cosmetic.

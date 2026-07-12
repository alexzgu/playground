# FINAL fresh-read (Read A) — modules 02, 12, 22

Cold full-text proofread for the last class of defect the structured referees miss:
what an attentive reader notices reading every word in order and comparing prose to the rendered PNGs.
Line numbers are approximate.

| sev | module:line | issue | fix |
|---|---|---|---|
| 2 | 12:217 | Figure alt-text says the leapfrog trajectory sweeps "to the far side — a single proposal covering the whole support," but in `leapfrog-trajectory.png` the trajectory makes a there-and-back U-turn: the end star (red, ~(-1.85,-1.3)) lands right next to the start square (-2,-2), not on the far side. The endpoint contradicts the caption. (The body words "arcs" / "long coherent glide" are fine; only the "to the far side" endpoint claim is wrong.) | Reword to e.g. "sweeping in a long curved arc across the distribution and back — one proposal traversing the whole support," or pick a shorter trajectory whose end actually lands across the ridge. |
| 3 | 12:83 | Typical-set alt-text: "each is a narrow bump centered on √d (dotted line)." In `typical-set.png` the d=1 (blue) curve is a half-normal decaying monotonically from 0 — it is NOT a bump and its peak (0) is not at √1=1; the dotted line sits to its right. Only d≥10 are bumps centered near √d. | Qualify: "each (for d≥10) is a narrow bump centered on √d; at d=1 it is a half-normal pressed against 0." |
| 3 | 02:77,124 | Predict offers anchors "one in ten thousand / thousand / hundred" and Reason says "before prevalence reaches a percent"; the true crossover is 0.048 (~1 in 21, i.e. ~5%), above every offered option. The Reconcile only rebuts readers who "guessed a fraction of a percent," so a reader who picked the offered "one in a hundred" (1%, not a fraction of a percent) is not explicitly addressed. | Either add "one in twenty?" to the options, or change the Reconcile to "if you guessed a percent or less" so it covers the largest offered anchor. |
| 3 | 22:83 | "a whisker below a threshold the naive rule placed 5.5× further out" — the 5.5× factor is 0.5/p\* (naive vs Bayes threshold), not a distance relative to the 8% patient; the phrase reads as if 0.5 is 5.5× beyond 0.08. Mildly confusing on a careful read. | Reword to "5.5× above the Bayes threshold" (consistent with the same sentence earlier in the paragraph) rather than "further out" relative to the patient. |

## Notes (checked, NOT defects)

- All numeric claims recomputed and match: 02 (PPV 0.0194, LR 19.8, crossover 0.048, 3 positives→0.886, tank mean 78.66/UMVU 71/closed 78.67, RMSE crossing ~1075, prosecutor 0.5/0.0909, spam 0.3913); 12 (‖θ‖ 31.61, d/2=500 nats, RW slope −0.94→2492 iters, energy exponent 2.00, ε_crit=2, funnel 13 vs 0 divergences, ULA variance 1/(1−ε/4), tempered 0.2567); 22 (p\*=1/11, regret ratio 81×, EVPI 200.2, lead 1.64σ, n\*=4000, bandit 19.6<99.7<212.4, Ex22.1 0.937, Ex22.4 EVPI 0.27).
- All `<details>` blocks open and close; every Reconcile resolves its own Predict.
- No doubled words; all `$` delimiters balance (even parity per file); no broken bold/math.
- Other figures faithfully match their prose (ppv, logodds, tank_posterior, tank_risk, rwm-decay, energy-error, funnel, threshold, evsi, bandit-regret).
- 12:326 "the neck's curvature grows like e^{−v/2}" is consistent with the module's own use of curvature = frequency ω (ω=1/σ_x=e^{−v/2}); not a defect.

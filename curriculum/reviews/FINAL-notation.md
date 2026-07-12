# FINAL — course-wide notation & convention audit

Auditor sweep of `modules/[0-2]*.md` (all 27) against STYLE.md §1–§3. Grep-driven,
then judged. Verdict: **FINDINGS** — 1 meaning-changing, 1 reader-visible drift,
3 cosmetic. No banned openers, no unlabeled heuristic claims, distribution
conventions clean.

## Findings

| sev | module:location | issue | concrete fix |
|---|---|---|---|
| **1** | 06:205, 06:261, 06:282, 06:319 | `$\mathrm{Cov}(\theta\mid R=r)$` and `$\mathrm{Cov}(\theta)$` (and plot labels "Cov(θ\|R=r)", "coverage Cov(θ)") use **`Cov` to abbreviate *coverage***, colliding head-on with the reserved operator `Cov[·,·]` = covariance (STYLE §3). A reader carrying the notation table parses `Cov(θ\|R=r)=r/(1−r)` as a covariance. | Rename the coverage function throughout module 06 to a non-reserved symbol — e.g. `$\mathrm{cvg}(\theta\mid R=r)$`, `$\gamma(r)$`, or spell it "coverage(·)". Update the two boxed/display formulas (205, 282), the two plot-label strings (261, 319), and the figure caption if it echoes the symbol. |
| **2** | 05:301, 06:205/282, 08:77, 09:199/436, 11:423/452, 14:43, 18:47/327, 20:361/369/506 | `Var`/`Cov` operators rendered with **parentheses** instead of the mandated brackets `Var[·]`, `Cov[·,·]` (STYLE §3; module 01 was corrected to brackets). Course-wide the bracket form dominates (`Var[` 19×, `Cov[` 9×) but paren forms persist (`Var(` 8×, `Cov(` 7×) in 8 modules — `\mathrm{Var}_\theta(W)`, `\mathrm{Cov}(W,\text{score})`, `\mathrm{Cov}(\beta)`, `\operatorname{Var}(X)`, `\mathrm{Cov}(f(x),f(x'))`, etc. `E[·]` itself is uniformly bracketed. | Convert the paren operator calls to brackets for uniformity, e.g. `\mathrm{Var}_\theta[W]`, `\mathrm{Cov}[W,\text{score}]`, `\operatorname{Var}[X]`. (Leave `\mathrm{Corr}(·,·)` — Corr is not in the table, but match its sibling if desired.) Purely typographic; no numbers change. |
| **3** | 08:3, 08:12, 08:258 | "crown jewel" appears **3× inside module 08** (spine + §intro "their crown jewel is our shrinkage" + §8.5). Course-wide the motif is deliberate and load-bearing (02→08→16→18, 6 total, module 16 correctly holds it to 1 = the title), but the in-module triple is repetitive. | Keep the spine and one in-body use; drop or reword the third (258's "a well-specified model's crown jewel" can become "…is precisely BvM calibration"). |
| **3** | 25/26 (audit tables), 00 (four-lines reveal) | `<details>` summary label is `Reconcile` in 104 exercise blocks but two blocks use `Reveal the lines` / `Reveal — the audited table`. | Intentional (these are commit-then-reveal *tables*, not exercise reconciles). No change needed unless strict uniformity is wanted; if so, keep "Reveal" for tables and document the two-label convention. |
| **3** | 25:77/81/346 (vs 14/15) | Regression-weight symbol drifts `β` (14, 15 — 37×/49×) → `w` (25, for network weights). Distinction is principled (linear coefficients vs net weights) and 25 correctly reverts to `β` for the ridge surrogate (346), but `w` is introduced without an explicit "here `w` = network weights" note. | Add a half-sentence at 25's first `w` use ("network weights `w`, the neural analogue of §14's `β`") so the drift is acknowledged, not silent. |

## Verified consistent (clean checklist)

- **Banned openers** — none. No "In this module", "Before we begin", "It is important to note" anywhere.
- **"it can be shown" without warrant** — none.
- **N(μ, σ²) = variance** — uniform. Module 07's `N(0,10)` priors explicitly annotated "prior SD =√10≈3.16"; 07's `N(2,0.5²)` and derived `N(0,0.2000)` all treat arg 2 as variance. The scipy-takes-SD trap is flagged in 00 (table note) and 03 (restated).
- **Gamma(α,β) rate; Exp(λ) rate; IG(α,β)** — rate convention held course-wide, with the mandatory inline scipy-convention comments present at 00 (table), 03:80, 05:255 ("course convention, STYLE §3"), 06:59, 11:41. rng.gamma calls (08, 17, 19, 21) comment their scale=1/rate usage.
- **Student-t `t_ν(μ, σ²)` location–scale** — uniform (00 table, 05:251/258, 11, 13:377, 14:314), scipy `t(df=ν, loc=μ, scale=σ)` used correctly.
- **Beta / Binomial / Poisson / Dirichlet** — standard throughout.
- **KL(·‖·) direction + ‖ symbol** — consistent. 03 defines `KL(p‖q)=E_p[log p−log q]`; 13 (`KL(q‖p)`, what VI minimizes) and 25 (VAE `KL(q‖p(z))`) comply; ‖ used everywhere, never `||` in prose.
- **E[·] bracket style** — uniform (the paren drift is Var/Cov only).
- **∝ / ∝-drop-constants** — used symbolically, consistent.
- **Symbols θ (unknowns), y (response), x (covariates), ỹ (predictive), D (dataset)** — consistent; β for GLM/linear coefficients uniform in 14/15 (only the 25 `w` note above).
- **Honesty labels** — all mandated tags present and correctly placed: dropout≈VI **Heuristic** (25:368), MC-dropout **Heuristic** (25:394), in-context learning **Open** (25:191/244/398/500), cold posteriors **Open** (25:370/400), deep ensembles **Heuristic** (25:81/187/393), BH≡local-fdr **Empirical** (18:146, takeaway 18:445), early-stopping/label-smoothing **Heuristic** (25:77), overparameterization **Open** (25:346). No unlabeled heuristic claim found. de-finetti-class **Theorem** tags used (06:281, 10:233).
- **bits vs nats** — 03 defines the base convention ("Base-2 → bits; natural → nats; always state the base") and flags the mixing pitfall (03:383). Compliant downstream: 13 labels ELBO/KL in **nats**, 17 codelength in **bits**, 23 EIG in **nats**, 18/25 KL in nats. Every entropy/KL/ELBO number states its base.
- **Header front-matter** — all 27 modules carry Spine / Which line? / Promise / Prereqs+Runtime / Sources, uniform.
- **Figure captions** — all take-away-stating and prose-discussed; no bare topic-only or unreferenced captions found.
- **`<details>` exercise solutions** — uniformly `<summary>Reconcile</summary>` (104×); two intentional `Reveal` table variants (see finding).

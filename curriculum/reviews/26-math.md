# Math review — modules/26-capstone.md (CAPSTONE)

Reviewer: mathematical-statistics referee. Date: 2026-07-12.
Basis: BRIEF.md; STYLE.md §3/§4/§6/§8; SYLLABUS.md §26-capstone (binding); SPINE-INDEX.md
in full (every ledger echo cross-checked against the canonical SPINE value for its module);
source library at `curriculum_material/` (booklet, C-B).

**Verdict: REVISE (one sev-1 canon-drift, else clean).** The new mathematics is exactly
right — the reference-NIG demo reproduces the classical Student-t interval to machine precision,
and every recomputed number matched. The ML-zoo status labels are all defensible and the
conformal wording is rigorous. The single blocking issue is a numbers-contract provenance error:
the M18 "sandwich" echo quotes the *true* sd (`0.1046`) under the sandwich label; the sandwich SE
M18 actually printed is `0.1019`. In a synthesis module whose whole job is faithful cross-module
echoing, that is a sev-1.

## Harness

- `python tools/run_module.py modules/26-capstone.md --check-determinism`: **exit 0, PASS in
  29.2 s, zero warnings**, two runs byte-identical. 2498 prose words (within the 1,500–2,500
  capstone exception, at the ceiling), 3 runnable blocks, 1 figure referenced and discussed.
  Block 1 is the exact STYLE §4 setup block with `SLUG = "26-capstone"`. Randomness only through
  `rng` and an explicitly-seeded local `rc = default_rng(999)` — determinism-safe.
- Runtime header says "~45 s"; harness measured **29.2 s** (block 3 = 27.8 s, the coverage
  replay). Overstated but conservative and well under the 120 s target.

## Findings

| Sev | Location | Issue | Concrete fix |
|---|---|---|---|
| 1 | §26.1 ledger block (L60) + prose (L69) | M18 echo reads "post sd `0.0739` vs **sandwich** `0.1046`", and prose: "the sandwich says `0.1046`". Per SPINE-INDEX M18 the sandwich SE is **`0.1019`**; `0.1046` is the **true** sampling sd. The row title is "misspecification: width is wrong" and M18's audit tool (M08's sandwich line cashed) is the *sandwich* estimator — so attributing the true sd to the sandwich is a false provenance statement in the numbers-contract. The pedagogical point (posterior too narrow) survives either way, but the label is wrong. | Either keep the value and relabel — "post sd `0.0739` vs **true sd** `0.1046`" (prose: "…while the truth is `0.1046` — the sandwich estimates it at `0.1019`") — or swap to the sandwich value `0.1019`. Prefer naming both: "posterior `0.0739` vs sandwich `0.1019` (true `0.1046`)". |
| 3 | §26.1 prose (L69) | "conditional on the ancillary spacing its coverage is $r/(1-r)$ — a certain `1.000` once $R\ge 0.9$". The formula $r/(1-r)$ is the $r<\tfrac12$ branch (at $r=0.9$ it gives 9, not 1); coverage is the capped "$=1$ for $r\ge\tfrac12$" branch. As written a careful reader gets $r/(1-r)=9$. | "$= r/(1-r)$ for $r<\tfrac12$ and capped at 1 above — a certain `1.000` at $R=0.9$." (M06 SPINE states it with the cap.) |
| 3 | §26.1 Reconcile (L127) | "The plug-in interval is `1.312`× narrower" — loose: the ratio is $t/\text{plug-in}=1.312$, i.e. the $t$ is 1.312× *wider*; the plug-in is 0.762× as wide. | "the plug-in interval is narrower by the factor `1.312` ($t$ is 1.312× wider)". |
| 3 | Header, Runtime | "~45 s" vs measured 29.2 s. | Update to "~30 s". |
| 3 | STYLE §2 skeleton / cross-cutting apparatus | No explicit `## Bridge` header (apparatus asks ≥1/module). The module is bridge-saturated (ledger, reading map, calibrated-Bayes) so the content requirement is met, but the labeled section is absent. | Optional: label §26.4 or the reading map as the Bridge, or add a one-line note. Acceptable to leave for a capstone. |
| 3 | Ex 26.1 / 26.2 | "*Run:*" steps are "re-read the M23 ledger rows" / "compare against §26.2's reveal" — no runnable code, unlike STYLE §5's mandated code Run. Ex 26.3 has genuine runnable code. | Acceptable deviation for a minimal-code synthesis module; optionally add a 2-line print recomputing the quoted numbers so the Run is executable. |

## Deviation rulings (requested)

- **(a) ~45 s runtime, minimal-code module, coverage replay load-bearing — FAIR.** Measured
  29.2 s (< 120 s target). The 20,000-replay loop is not padding: it *is* the Reconcile, printing
  `0.8942` (plug-in) vs `0.9508` (t) that settle the predict-then-verify. It could be vectorized
  (per-iteration scipy object construction is the cost) to cut ~28 s, but that is polish, not a
  defect. **Approved.**
- **(b) echo-print recap block for cross-module numbers — ACCEPTABLE mechanism, but it is exactly
  what let the sev-1 through.** For a synthesis module the numbers-contract (STYLE §4.3) can only
  be met by echoing string literals from prior modules — legitimate. The cost is that literal
  accuracy is now the whole game, and one literal (`0.1046` mislabeled "sandwich") drifted. Keep
  the mechanism; fix the literal.
- **(c) reference NIG prior (κ=n, m=x̄, a=(n−1)/2, b=S/2) yields the classical t interval exactly
  — CORRECT, verified independently.** With this prior μ|y ~ t_{n−1}(x̄, scale²) where
  scale² = b_n/(a_nκ_n) = [S/2]/[((n−1)/2)·n] = S/((n−1)n) = (s/√n)² with s²=S/(n−1). So the
  marginal-t scale equals the plug-in Normal sd **to machine precision** (I reproduced
  `scale == sd = 0.49566…`), and the width ratio is *purely* the quantile ratio
  t_{0.975,5}/z_{0.975} = 2.5706/1.9600 = **1.3115 → 1.312**. df = 2a_n = n−1 = 5 exactly. The
  "z-vs-t isolation" claim is clean and true.

## Recomputation list (all independently reproduced)

- t₅/z quantile ratio = **1.3115** → module `1.312` ✓; widths **2.548 / 1.943** ✓.
- plug-in coverage analytic = 2·F_{t5}(1.96)−1 = **0.8927** ≈ MC **0.8942** ✓; marginal-t MC
  **0.9508** ✓ (both reproduced byte-for-byte from the module's seeds).
- scale_t == sd_plugin = 0.495656… (Route-1/Route-2 differ *only* in the quantile) ✓.
- Reference-NIG marginal = classical t interval (scale² = S/((n−1)n)) ✓.
- SPINE echoes verified canon: M23 `1.00e-08`, `0.9494`, `0.0522→0.2044@10` ✓; M06 `0.500`,
  cond `1.000@R=0.9` ✓; M17 `p=0.0099`, `BF01 1.80→17.93` ✓; M15 ECE `0.0207/0.0401`
  (0.0207=calibrated, 0.0401=plug-in — correct) ✓; M08 `0.9499` ✓; M18 `0.0739` ✓ but
  `0.1046` mislabeled "sandwich" (canon sandwich = `0.1019`) ✗ → the sev-1.
- ML-zoo: 20 rows (spec ~20, exact match to SYLLABUS list). Status labels all defensible —
  OLS/ridge/lasso(mode)/horseshoe/logistic/GP/Kalman/PPCA/BART = theorem; k-means (hard-EM
  σ→0), VAE (ELBO bound), bootstrap (Dirichlet) = approx; RF/dropout/ensembles/tree = heuristic;
  boosting = none/heuristic; SVM hinge = none (no proper log-likelihood — fair). No overclaim.
- Conformal wording: finite-sample ✓, distribution-free ✓, **marginal** (contrasted with
  conditional) ✓, exchangeability (M01 callback) ✓, "distribution-free conditional coverage
  provably impossible" ✓ (Vovk/Lei–Wasserman/Barber), breaks under shift ✓, P(Y∈C)≥1−α ✓.
- Reading map spot-check: booklet ch03–05/09/10/11/13/14 + `insert-bda-hmc-stan.md` all exist;
  C-B ch. 6 (LP)/7/8/10 correct; BDA3 ch. 5/6–7/11–13 sensible. ✓
- Fill-in-first mechanics: the 20-procedure blockquote precedes the `<details>` reveal table;
  the "commit (a) reading and (b) status" instruction is stated before the answers — genuine
  commit-before-reveal (not a literal blank-column table, but the mechanic holds). ✓

## Required-items checklist (SYLLABUS §26)

1. Ledger, every row → a module the learner RAN (nuisance-26 / stopping×3-M23 / cond-cov-M06 /
   Lindley-M17 / misspec-M18 / calibration-M15): **present** — one new NIG demo as the only new
   code. ⚠ M18 row mislabeled (sev-1).
2. ML-zoo ~20-row audit table, fill-in-first: **present, 20 rows**, labels defensible. ✓
3. Conformal precisely (finite-sample / distribution-free / marginal / exchangeability / no
   conditional / breaks under shift): **present and rigorous**. ✓
4. Calibrated-Bayes stance + working decision-guide table: **present**, rows honest and point to
   real modules. ✓
5. Annotated reading map with "read for" notes: **present**, citations verified. ✓
- Skeleton: Spine block ✓, Pitfalls (5) ✓, Exercises (3, ≥1 surprising = 26.2, ≥1 ML = 26.2) ✓,
  Takeaways (6 ≤7) ✓. Bridge header absent (sev-3). Length exception honored (2498 ≤ 2500).

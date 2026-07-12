# Math review — modules/01-probability-as-logic.md

Reviewer: mathematical-statistics referee. Harness: `python tools/run_module.py modules/01-probability-as-logic.md --check-determinism` → exit 0, **PASS in 4.8–5.1 s** (well under 120 s target), 9 runnable blocks, 3719 prose words, **zero warnings**, determinism confirmed (byte-identical second run).

**Verdict: REVISE** (0 sev-1, 3 sev-2, 5 sev-3). The mathematics that is on the page is correct — every identity recomputed independently checks out — but two rigor overclaims and one dangling forward-reference need fixing.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 2 | §01.1, "Coherence *is* the axioms" (para after Dutch-book code) | Overclaim. The Dutch-book argument forces only **finite** additivity; countable additivity — explicitly listed as one of "the identical Kolmogorov axioms" two paragraphs earlier — is *not* delivered by sure-loss avoidance (a Dutch book against a countably-additivity violator needs an infinite book). The very source cited, C-B ch. 1 (`Ch1to5.txt` §1.2.1, "Axiom 3 … is rejected by a school of statisticians led by deFinetti (1972), who chooses to replace this axiom with the Axiom of Finite Additivity"), says de Finetti himself rejected countable additivity. As written the module's central §01.1 claim is stronger than the theorem behind it. | Add one scoping sentence: the finite Dutch book pins down finite additivity; countable additivity is an extra regularity assumption (which de Finetti resisted — see the note in C-B §1.2.1). |
| 2 | §01.2 intro ("…except the mixture-impossibility fact in (b), which we *derive*") + demos (a)/(b) | Advertised derivation never appears. The load-bearing identity Cov(Xᵢ,Xⱼ) = Var(E[Xᵢ\|Θ]) = Var(Θ) is *asserted* ("The general fact behind the number…") and verified numerically, but the conceptual step — law of total covariance, with conditional independence killing E[Cov(Xᵢ,Xⱼ\|Θ)] — is elided. STYLE §6: "never elide the conceptual step." The identity is what makes (b)'s impossibility argument a proof. | Two lines suffice: E[XᵢXⱼ] = E[E[XᵢXⱼ\|Θ]] = E[E[Xᵢ\|Θ]E[Xⱼ\|Θ]] = E[Θ²] (conditional independence), so Cov = E[Θ²] − E[Θ]² = Var(Θ). Insert at the "general fact" sentence in (a). |
| 2 | Exercise 01.3 reconcile, "The fix (module 21's forward-chaining / blocked CV)" | Dangling forward-reference. SYLLABUS module 21 is state-space (Kalman/AR/particle filters); it contains no CV content, and `forward-chain`/`blocked CV` appears **nowhere** in SYLLABUS.md. The callback points at content no module is specced to deliver (STYLE §8 gate 6: callbacks point at real content). | Either repoint (M26's exchangeability-based conformal audit is the specced landing spot) or get the syllabus owner to add blocked CV to M21's Required list. |
| 3 | §01.2(a) reconcile, "Var(Θ) = `0.05`, which is exactly the covariance we measured" | Semantic slip in the numbers contract. The printed `Var(theta) = Cov(Xi,Xj) = 0.05` is the **analytic** Beta(2,2) variance (`varT`), not a measurement; the *measured* covariance (≈ 0.210 × 0.25 ≈ 0.052) is never printed. Grep passes, semantics don't. | Print the empirical covariance (`np.cov(X[:,0],X[:,1])[0,1]`) and quote both, or reword to "…which matches the covariance we measured (`0.052`)". |
| 3 | Header, "**Runtime.** 3 s (measured)" | Harness measures 4.8–5.1 s (block 1 imports = 2.1 s of it). Both trivially under budget, but the header claims a measurement it doesn't match. | Change to "5 s (measured)". |
| 3 | §01.3, last sentence ("two coherent observers who agree on the exchangeable model cannot disagree about which prior is in play — only about which G they each started from") | Self-contradictory as written: the prior *is* G, so the sentence says they can't disagree about the prior, only about the prior. The uniqueness content (the joint law determines the likelihood/prior split uniquely) is garbled. | Reword: "the exchangeable joint determines G uniquely — there is no freedom in how to split it into likelihood and prior; observers who disagree about the prior are disagreeing about the joint itself." |
| 3 | Exercise 01.3 reconcile, "the honest error against an unrelated point is `5.07`" | `5.07` is the error of the *copy-an-unrelated-point* predictor (theory 2σ² = 5.56); an honest predictor with no neighbors available predicts the stationary mean and gets σ² ≈ 2.78. "Nearly fivefold optimistic bias" is an artifact of the copy convention (an apples-to-apples contrast, but mislabeled as "honest error"). | Reword: "the same copy-predictor applied to an unrelated point scores `5.07`" and note the copy-vs-copy comparison isolates the leakage; the qualitative lesson survives. |
| 3 | throughout (Var(Θ), Cov(Xᵢ, Xⱼ)) | STYLE §3 notation table specifies square brackets: E[·], Var[·], Cov[·, ·]. Module uses parentheses for Var/Cov (it is the first module to use them, so it sets the precedent). E[·] usage is compliant. | Harmonize: either switch to Var[·]/Cov[·,·] or amend the STYLE table to parentheses course-wide before module 05 needs them. |

## Required-item checklist (SYLLABUS §01-probability-as-logic)

| # | Required item | Verdict |
|---|---|---|
| 1 | Two readings as evaluation modes; Dutch book with explicit guaranteed-loss payoff table | **Delivered fully.** Markdown table + printed table; arithmetic verified (all columns −0.20). Slightly longer than the specced "tight box" but the de Finetti trio does carry the module as intended. Rigor caveat = finding sev-2 #1. |
| 2 | Calibration as frequency-matching, simulated forecaster tallies | **Delivered fully.** Honest vs overconfident forecaster, binned reliability diagram, ECE `0.007` vs `0.089` printed. |
| 3a | Beta(2,2)→Bernoulli: positive corr printed, fan of running frequencies, histogram of limits = Beta(2,2) | **Delivered fully.** Corr `0.210` (theory `0.2`) printed; 60-replicate fan on log-x; terminal-frequency histogram vs Beta(2,2) pdf overlay; P(1,1)=`0.304` vs 0.25 bonus. |
| 3b | Without replacement: negative correlation printed; no mixture can do that; infinite exchangeability needed | **Delivered fully.** Corr `-0.116` vs exact −1/9 printed; impossibility argued via Cov=Var(Θ)≥0 (derivation gap = sev-2 #2); extendability point made; −1/(N−1) vs N figure. |
| 3c | Pólya urn ≡ Beta-Binomial predictive, matching sequence probabilities printed; seeds CRP in M19 | **Delivered fully.** Four sequences, both routes printed to 6 d.p., max gap 5.6e-17; M19/CRP pointer present. |
| 4 | de Finetti representation theorem stated precisely, Theorem label, cited, simulated not proved | **Delivered fully.** Infinite exchangeability stated loudly; a.s. limit + unique mixing G; binary scope honestly flagged; Hewitt–Savage attribution correct; simulated in (a), falsified-at-finite-n in (b). |
| 5 | Permutation-null paragraph, demo deferred to M23 | **Delivered fully.** One paragraph in §01.4; M23 pointer matches SYLLABUS M23 item 6 ("M01's exchangeability cashed"). |
| B | Bridges: C-B ch. 1 axioms; "random = unknown to you"; ML train/test exchangeability | **Delivered fully.** All three present; conformal/M26 pointer matches SYLLABUS M26 item 3. One dangling pointer (M21 blocked CV) = sev-2 #3. |
| S | Sources: booklet ch. 1–2; C-B ch. 1 | **Delivered; all citations verified** (see below). |

Skeleton/contract compliance: header block complete; 3719 prose words (in 2,500–5,000); 9 runnable blocks (4–10); 3 figures, all referenced with real captions and discussed; Pitfalls ×5; Exercises ×3 in predict-then-run format with one genuinely surprising (01.1) and one ML-connected (01.3); Takeaways ×7; block 1 is the exact STYLE setup block with SLUG changed; randomness only via `rng`; no `plt.show`, no legacy `np.random.*`; numbers-contract grep clean.

## Citations verified against sources

- **C-B Definition 1.2.4** = Kolmogorov axioms (nonneg, P(S)=1, countable additivity): `curriculum_material/casella_berger/Ch1to5.txt` §1.2.1 "Axiomatic Foundations" — confirmed verbatim.
- **C-B Exercise 5.4**: exchangeable-but-not-iid, Xᵢ|P ~ iid Bernoulli(P), P ~ uniform(0,1), with de Finetti characterization note — confirmed (module's "with a Beta prior" generalization is honestly flagged as such).
- **Booklet ch. 1 §1.3 "coherent"**: "A scientist is called incoherent if he violates any of the axioms" — confirmed (`ch01-lecture-one.md`).
- **Booklet "page 2" Kolmogorov axioms**: confirmed (`ch01-lecture-one.md`, PDF p.7 = booklet p.2).
- **Booklet §2.3 exchangeability** = permutation invariance of the joint density: confirmed (`ch02-lecture-two.md`), including "equi-correlated" phrasing the module reuses.
- **Booklet §2.5 de Finetti** (mixture of iid; Example (1) is exactly the Beta-Bernoulli/Beta-Binomial marginal): confirmed.
- **Booklet "note after Example 3"** = "The mixing distribution is unique": confirmed, exactly there.
- **Booklet §2.7.1 empirical view of probability**: confirmed.
- de Finetti (1937), Hewitt–Savage (1955), Cox: by-concept, exempt; attributions are historically correct.
- Module-00 callbacks: line-1/line-3 quotations match module 00's four lines verbatim; the "losing plug-in bet in module 00's coin demo" exists (plug-in bettor mean profit −0.0132).

## Independently recomputed (fresh code, different seeds / exact arithmetic)

| claim | independent result | module | match |
|---|---|---|---|
| Var(Beta(2,2)) = Cov(Xᵢ,Xⱼ) | 0.0500 analytic; identity re-derived via law of total covariance | `0.05` | ✓ |
| Corr(Xᵢ,Xⱼ) = Var(Θ)/0.25 | 0.2000 | theory `0.2`, empirical `0.210` (R=4000, MC sd ≈ 0.016) | ✓ |
| P(X₁=1,X₂=1) = E[Θ²] | 0.3000 | empirical `0.304` | ✓ |
| WOR N=10, K=5: Cov = (K/N)((K−1)/(N−1)) − (K/N)² | −1/36 = −0.027778 exact | `-0.0278`, empirical `-0.0289` | ✓ |
| WOR Corr = −1/(N−1) | −1/9; N=4: −0.3333; N=200: −0.0050 | `-0.1111`, `-0.3333`, `-0.0050` | ✓ |
| Pólya ≡ Beta-Binomial, a=2, b=3 | exact rational arithmetic (Fractions): identical for all 4 sequences, e.g. [1,1,1] = 4/35 = 0.114286 | `0.114286`, `0.085714`, gap `5.6e-17` | ✓ exact |
| Rule of succession | 6/7 = 0.8571; 51/52 = 0.9808 | `0.8571`, `0.9808` | ✓ |
| Dutch-book columns | all outcomes net −0.20 | `-0.20` / loss `0.2` | ✓ |
| Overconfidence map 0.5+1.6(p−0.5) at p=0.75 | 0.90 | "says 0.9 when they mean 0.75" | ✓ |
| Terminal-freq variance at n=1500 | Var(Θ) + E[Θ(1−Θ)]/n = 0.05013 | `0.0503` | ✓ |
| AR(1) φ=0.8: neighbor-copy MSE 2σ²(1−φ) | 1.111 | `1.09` | ✓ (MC + non-stationary start) |
| AR(1) unrelated-copy MSE 2σ² | 5.556 | `5.07` | ✓ within MC noise (but see sev-3 "honest error" wording) |
| Harness | exit 0, PASS 4.8–5.1 s, zero warnings, deterministic | header says 3 s | runtime header = sev-3 |

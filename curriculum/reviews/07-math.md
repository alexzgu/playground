# Math review — modules/07-priors.md

Reviewer: mathematical-statistics referee. Date: 2026-07-12.
Basis: BRIEF.md; STYLE.md §3/§4/§6/§8 (honesty labels: Theorem/Empirical optional when the
warrant is adjacent; Heuristic/Open mandatory); SYLLABUS.md §07-priors (binding, incl. the
multiparameter-Jeffreys rigor note); modules/SPINE-INDEX.md (Wave-1 canon);
`curriculum_material/bayesian_booklet/ch15-mcmc-difficulties.md` (opened and read).

**Verdict: REVISE (minor).** No severity-1 findings. Every derivation and every number I
recomputed independently matched — the Jeffreys two-route invariance argument is set up and
executed correctly (Jacobians on both legs), the Haldane divergence demo genuinely exhibits
the −log ε signature, the washout-exception numbers are exactly reproducible from the stated
priors, and the load-bearing booklet ch. 15 quotes are verbatim. One severity-2 item (a
binding STYLE length-contract violation: 19 runnable blocks vs the 4–16 range) and five
severity-3 polish items, all with one-line fixes.

## Harness

- `python tools/run_module.py modules/07-priors.md --check-determinism`: **exit 0, PASS in
  6.1–6.7 s, zero warnings**, run twice by me (determinism clean). 3,912 prose words (within
  2,500–5,000); 6 figures, all referenced with real captions and discussed; block 1 is the
  exact STYLE §4 setup block with `SLUG = "07-priors"`; randomness only through `rng`; no
  `plt.show`, no legacy `np.random.*`; runtime header "~7 s" matches measurement.
- **19 runnable blocks** — exceeds STYLE §2's "4–16 runnable blocks" (see sev-2 below). Every
  other shipped module is ≤16 (max: 04, 05, 08 at 16).

## Findings

| Sev | Location | Issue | Concrete fix |
|---|---|---|---|
| 2 | whole module (harness: "19 runnable blocks") | STYLE §2 sets a binding length contract of 4–16 runnable blocks; the module has 19. All content fits comfortably — this is packaging, not mis-scoping. | Merge three compute+figure pairs, e.g. §07.2 blocks 5+6 (basketball compute + histogram), §07.4 blocks 8+9 (route 1 + route 2 — they share one narrative check), §07.5 blocks 11+12 (kernel integrals + log-plot). 19 → 16. |
| 3 | §07.1, para after block 2 | "a spread of `0.3000`, as wide as the priors themselves" — the five prior means span 0.2–0.8 (spread 0.6), so the posterior fan is *half* as wide as the prior disagreement, not "as wide". The printed number is right; the prose comparison is off by 2×. | "a spread of `0.3000` — half the 0.6 spread of the prior means (0.2 to 0.8), so the data have only begun to close the disagreement." |
| 3 | Header, Sources | "Booklet ch. 5–7 (prior elicitation, conjugate families)" mischaracterizes the source: ch. 5 is regression, ch. 6 is Monte Carlo/numerical integration (zero occurrences of "prior"), ch. 7 is testing/model choice/hierarchical. STYLE §6: cite local sources only as verified. The SYLLABUS-mandated ch. 15 citation, by contrast, is verified verbatim (see below). | "Booklet ch. 5, 7 (normal-model conjugate posteriors, model choice) and ch. 15 (variance-component priors; wording verified)" — or drop the parenthetical gloss. |
| 3 | Ex 07.3, Run print + Reconcile | "the Haldane limit, whose posterior mean is the degenerate `1.0000`" — with 2 successes / 0 failures the Haldane posterior kernel θ(1−θ)^{−1} is itself **improper** (the module's own §07.5 result: Beta(s,f) proper iff s,f>0), so it has no mean; 1.0 is the ε→0 limit of Beta(2+ε, ε) posterior means. The exercise blurs the distinction §07.5 just taught. | "the strict Haldane posterior is improper here (all-successes — §07.5); the limit of Beta(ε,ε)-prior posteriors has mean → `1.0000`, the degenerate plug-in answer." |
| 3 | §07.2, `prior_predictive` (block 4) | The `rng=rng` parameter is dead: the function never uses it — `prior_sampler`/`sim_data` close over the global `rng`. A reader passing a fresh generator would silently get the global stream. (Similarly `post_means` in block 2 is built and never read.) | Drop the `rng` parameter (or thread it: `prior_sampler(M, rng)`), and delete the unused `post_means` dict. |
| 3 | §07.3, last para | Flat-log-odds "corresponds … to π(θ) ∝ θ^{−1}(1−θ)^{−1}, which piles all its mass at 0 and 1" — an improper prior has no unit mass to pile; the spikes are non-integrable. Loose wording for the object §07.5 then treats carefully. | "which has non-integrable spikes at 0 and 1 — the improper **Haldane** prior of §07.5." |

## Required-items checklist (SYLLABUS §07, 7 items)

1. **Sensitivity fan lead, 5 priors × n ∈ {10, 10⁴}, both fans plotted** — PASS. §07.1 leads the
   module; five defensible priors; conjugate updates; spread `0.3000` vs `0.0006` both printed;
   two-panel figure; the ML skeptic addressed first, as ordered. Predict-then-reconcile staged.
2. **Prior predictive checks + basketball N(0.5, 10²) with printed tail masses + reusable
   harness** — PASS. `prior_predictive` harness; P(outside [0,1]) = `0.9601` printed and exact
   (recomputed: 2·Φ(−0.05) = 0.96012); all-or-nothing tail `0.9653` vs `0.0238` printed and
   consistent with analytic Beta-Binomial (2·6/506 = 0.0237 for Beta(2,2)).
3. **Flat isn't flat, transform histogram** — PASS. Uniform-θ → logistic density on ψ, sampled
   histogram + analytic overlay; "flat in what?" question posed; both directions run (flat-ψ →
   Haldane).
4. **Jeffreys two ways + invariance through log-odds + multiparameter scope + Bernardo
   pointer** — PASS. √I ∝ θ^{−1/2}(1−θ)^{−1/2} = Beta(½,½) with numeric check `7.11e-15`;
   invariance verified by genuine two-route computation (`5.64e-12`); scope line states
   "often not recommended as-is" with the Jeffreys-preferred independence prior, correctly
   parameterized (π(μ,σ²) ∝ 1/σ² ⟺ π(μ,σ) ∝ 1/σ); reference priors described correctly
   (asymptotic mutual-information maximization; reduce to Jeffreys in 1-d) and cited by concept.
   Matches the SYLLABUS rigor note exactly.
5. **Improper priors: Haldane all-successes divergence + booklet ch. 15 1/σ trap** — PASS.
   Posterior ∝ θ^{n−1}(1−θ)^{−1} derived (Beta(s,f) proper iff s,f>0 — correct); integral
   sequence 1.8644/6.3823/10.9866 genuinely demonstrates log-divergence; safe-vs-not rule stated.
   Booklet quotes verified **verbatim** (see Citations).
6. **Washout exception y = θ₁+θ₂ + faces-of-nonidentifiability + DL pointer** — PASS. Sum
   concentrates (`0.0100` ≈ σ/√n), θ₁ stays prior-width (`2.2361` = √5 exactly — the module's
   "one-time constant-factor drop" explanation is the correct conditional-variance argument:
   Var(θ₁ | θ₁+θ₂) = 10 − 100/20 = 5); ridge figure; structural/symmetry/weak-likelihood
   taxonomy with M19/M25 pointers.
7. **Regularization = implicit prior, softened tone; weakly-informative defaults as stability
   engineering** — PASS. λ ↔ σ²/λ correspondence correct (λ‖β‖² = −2σ² log N(0, σ²/λ) + const;
   MAP = mean for the Gaussian case, correctly noted); explicitly non-polemical ("not a claim
   that deep learning is secretly Bayesian"); dropout/early-stopping tagged as heuristics.

Apparatus: Bridge section present (§07.7); 5 Pitfalls; 4 exercises in STYLE §5 format with
one tagged surprising (07.3) and one ML bridge (07.2); 6 Takeaways.

## Independent recomputations (all matched)

- **Jeffreys normalization:** Beta(½,½).pdf(θ)·√(θ(1−θ)) = 1/π at every θ ⇒ √I kernel *is* the
  Beta(½,½) kernel with normalizer B(½,½) = π. Scaled max|diff| `7.11e-15` reproduced. ✓
- **Invariance as WRITTEN:** dθ/dψ = θ(1−θ) ⇒ I_ψ = I_θ(dθ/dψ)² = θ(1−θ) — module's formula
  correct. Route B: lik·√(θ(1−θ)) is the ψ-space posterior; back-transform multiplies by
  |dψ/dθ| = 1/(θ(1−θ)) — code divides by θ(1−θ), correct direction. Algebra: result ∝
  θ^{s−1/2}(1−θ)^{n−s−1/2} = Beta(7.5, 3.5) = route A exactly; numeric `5.64e-12` reproduced.
  The two-route posterior identity is precisely what Jeffreys invariance asserts (π_J transforms
  by the Jacobian), and the contrast "a flat prior does not" is correct. ✓
- **Flat-isn't-flat:** induced density e^ψ/(1+e^ψ)²; p(0) = 0.2500, p(3) = 0.0452, ratio 5.53 —
  reproduced; prose reads it as a density ratio ("5.53-fold preference for even odds"),
  semantically right. ✓
- **Haldane divergence:** ∫₀^{1−ε} θ⁹/(1−θ) dθ = 1.8644 / 6.3823 / 10.9866 at ε = 10⁻²/10⁻⁴/10⁻⁶
  (quad, reproduced); increments 4.518, 4.604 vs ln 100 = 4.605 — "about 4.6 per two decades" is
  honest (first increment pre-asymptotic, covered by "about"). ✓
- **Washout demo:** Λₙ = (n/σ²)𝟙𝟙ᵀ + I/10; analytic sd(θ₁) = 2.2416 (n=10), 2.2361 (n=10⁴) →
  √5 limit; sd(θ₁+θ₂) = 0.3154 / 0.0100; prior sd √10 = 3.1623. All five printed numbers
  reproduced from the stated priors; "moved by about five thousandths" = 0.0055 ✓.
- **Basketball tails:** Φ(−0.05·1) with sd 10: P(<0) = P(>1) = 0.4801, sum 0.9601 exact;
  MC tails 0.9653/0.0238 consistent with clip-mass 0.9601 + interior contribution and with
  analytic Beta(2,2)-Binomial 0.0237. ✓
- **Sensitivity fan:** conjugate means at (3,7): 0.2500 (pessimist) to 0.5500 (optimist),
  spread 0.3000; at (3000,7000): 0.2999–0.3005, spread 0.0006 — reproduced analytically;
  pseudo-observation weight (a+b)/(a+b+n) and the 1/n decay claim check out. ✓
- **Multiparameter scope algebra:** joint Jeffreys for N(μ,σ) is ∝ 1/σ² (√det diag(1/σ², 2/σ²));
  the independence prior π(μ,σ) ∝ 1/σ transforms to π(μ,σ²) ∝ 1/σ² — module's statement correct
  in its chosen parameterization. ✓
- **§07.5 equivalence:** π(σ) ∝ 1/σ ⟺ π(σ²) ∝ 1/σ² (Jacobian 1/(2σ)). ✓
- **Ridge bridge:** σ²/λ = 0.2000 at (1, 5); Ex 07.2 prior sds √(4/λ) = 6.3246 / 2.0000 / 0.2000. ✓
- **Ex 07.1:** Beta(1,16) mean 1/17 = 0.0588, sf(0.1) = 0.1853; Beta(0.5,15.5) mean 1/32 =
  0.0312, sf(0.1) = 0.0730; Haldane Beta(0,15) improper at 0 (limit of Beta(ε,15+ε) → point mass
  at 0) — module's characterization consistent. ✓
- **Ex 07.3:** Beta(3,1) mean 0.7500; Beta(2.5,0.5) mean 0.8333; Haldane limit mean → 1
  (see sev-3 on wording). ✓
- **Ex 07.4:** Λ₀ = diag(4, 0.1), n = 10⁴: sd(θ₁) = 0.4939, sd(θ₂) = 0.4940 — reproduced;
  the θ₂ = sum − θ₁ propagation argument is correct. ✓

## Citations checked against sources

- **Booklet ch. 15** (`ch15-mcmc-difficulties.md`, opened): "the prior π(σ) ∝ 1/σ is no good
  (Gelman, BA 2006)" — p. 167 of the transcription, **verbatim** ✓; "Priors like π(σ²) ∝ 1/σ²
  create difficulties deep down in a hierarchical model (Gelman, BA 2006)" — p. 168,
  **verbatim** ✓. Both appear in the hierarchical scale-prior context the module claims, both
  attributed to Gelman BA 2006 in the source (the Gelman cite itself is by-concept, exempt),
  and the booklet's recommended alternatives (half-Cauchy / shrinkage priors) match the
  module's "half-Cauchy or half-Normal" fix. The module's characterization is accurate.
- Booklet ch. 5–7 Sources gloss: **mismatch** (sev-3 above).
- BDA3 ch. 2–3, Jeffreys, Bernardo: by concept, exempt; descriptions accurate.
- SPINE-INDEX callbacks: M04 Fisher info I(θ) = 1/(θ(1−θ)) for Bernoulli — canonical (SPINE 04:
  I(0.3) = 4.7619, "Jeffreys ∝ √I (M07)" promise) ✓; M00 ridge-verified-to-machine-precision
  (SPINE 00: 4.5e-15) ✓; M02 conditioning ✓. M05 pseudo-trials reading and rule-of-succession
  0.75, M06 MAP = penalized MLE: SPINE-INDEX not yet updated past Wave 1, checked against
  SYLLABUS M05 item 3–4 / M06 item 3 — exact matches ✓. Forward pointers (M14/M16/M18/M19/
  M24/M25) all point at real SYLLABUS content ✓. No R anywhere. Notation table respected
  (N(·,·) variance convention used consistently: N(0.5,10²), N(0,10) with sd √10, N(2,0.5²)).

## Numbers-contract semantic spot-check (≥6 required; 12 checked)

`0.2500..0.5500`/`0.3000`/`0.0006` (fan spreads, n-labels correct) ✓; `0.9601` (impossible-mass
role) ✓; `0.9653`/`0.0238` (absurd/sensible roles correct) ✓; `0.2500`/`0.0452`/`5.53` (density
values and ratio) ✓; `7.11e-15`/`5.64e-12` (scaled-kernel match; two-route posterior gap) ✓;
`1.8644`/`6.3823`/`10.9866` (ε-labels match printed lines) ✓; `0.0100`/`2.2361`/`2.2416`/
`3.1623` (sum vs θ₁ vs prior roles all correct) ✓; `0.2000` (prior variance, not sd) ✓;
`0.0588`/`0.0312` (uniform/Jeffreys means) ✓; `6.3246`/`2.0000`/`0.2000` (λ-ordering correct) ✓;
`0.7500`/`0.8333`/`1.0000` (flat/Jeffreys/Haldane-limit roles) ✓; `0.4939`/`0.4940` (θ₁/θ₂) ✓.
No semantic mismatches. The one prose-comparison defect ("as wide as the priors") is logged
as sev-3 — the quoted number itself is correct.

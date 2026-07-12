# Math review — 08-frequentist-bridge.md  [SIGNATURE S4]

**Referee verdict: APPROVE.** Harness PASS in 5.0 s, zero warnings, determinism confirmed
(`--check-determinism`). All 9 Required items present and correct. Both author deviations
adjudicated as ACCEPTABLE. Zero sev-1, zero sev-2 findings. Four sev-3 polish notes below —
none blocking.

## Findings table

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | §08.4 BvM demo (L191–223) | The code centers the posterior at *its own* mean (`post - post.mean()`) and the MLE law at its own mean, then compares. This faithfully demonstrates the **shape/width** half of BvM but not the **location** half stated in the box ("posterior *centered at the MLE*"). The demo never shows post-mean → MLE. Honestly labeled in the comment, so not a defect, but a reader could miss that the centering agreement is also part of the theorem. | Add one sentence after L223: note that the posterior mean and MLE also coincide to leading order (their gap is O(1/n)), so centering at either is asymptotically the same choice — the demo isolates the shape claim on purpose. |
| 3 | §08.2 vs dominance sweep | The quantity "JS⁺ total risk at d=10, θ=0" is quoted twice from two independent MC runs: `1.25` (L118, R=40 000) and `1.28` (L149, R=20 000, sweep). Same theoretical value (~1.26), two estimates — reads as a small inconsistency. | Either reuse the §08.2 value in the sweep's first point, or add a half-clause ("MC noise; cf. `1.25` above") so the reader isn't tripped. |
| 3 | bootstrap figure caption (L331) | Caption says "centered on the sample mean 1.64"; the block prints `1.644`. Not backticked, so not a numbers-contract violation, but the truncation is gratuitous. | Write `1.644` (or `≈1.64`) in the caption. |
| 3 | spine (L3), §08 intro (L12), takeaway (L428) | "their crown jewel is our shrinkage" appears 3×. It is *earned* (JS = EB posterior mean is proven, not asserted) and the intro explicitly disclaims "gotcha," so it stays inside the BRIEF's non-tribalism rule. Borderline on the final takeaway, which ends the module on the triumphal note rather than the reconciliation note the body works hard to build. | Optional: let the final bullet close on the audit-reconciliation framing already in L347 ("one calculus, two ledgers") and demote the slogan to a subordinate clause. |

## Required checklist (9 items — all PASS)

1. **Sampling dist + MLE asymptotics overlay** — §08.1 Poisson: sim sd `0.3653` vs √(λ/n) `0.3651`, KS `0.0256`. ✓
2. **CRLB + proviso + U(0,θ) foil + one numerical check + biased-beats-bound note** — §08.1: bound `0.05000` vs Var `0.04997`; U(0,θ) support clause cited (C-B Ex 7.3.13); biased-escape stated. ✓
3. **S4 staged** — §08.2: three unrelated quantities, predict-first ("obviously not"), d=10 MSE `9.98`/`1.99`/`1.25`, dominance sweep, collapse d=1/2, crossover at d=3. ✓
4. **JS = empirical Bayes + punchline** — §08.3: derivation from θᵢ~N(0,τ²), B̂=(d-2)/‖X‖², verified; punchline "admissibility forced frequentists to invent a posterior mean" present verbatim. ✓
5. **BvM: posterior-on-MLE-law overlay, TV at n∈{5,50,500}, conditions explicit, breakdown gallery** — §08.4: TV `0.1668`→`0.1446`→`0.0165`; 4-condition box matches SYLLABUS list exactly; boundary (U(0,θ)), Neyman-Scott (σ²/2), nonidentifiability (M07), misspecification (sandwich, M18) all present. ✓
6. **Risk-set 2-point Θ, Bayes trace boundary, complete-class stated no proof, "special case is a theorem"** — §08.5. ✓
7. **Bootstrap classical vs Bayesian (Dirichlet(1,…,1)), "implicit posterior"** — §08.6: `[1.340,1.980]` vs `[1.357,1.992]`. ✓
8. **Coverage audit, weak prior ≈95%, ties to M06** — §08.6: `0.9499`; correctly distinguishes M06's *prior-averaged* exact 1−α from *pointwise* coverage here. ✓
9. **Minimax exercise, flat risk, crossing, minimax = Bayes vs least-favorable** — Ex 08.1: flat `0.0144`, crossings near 0.18/0.82, Beta(√n/2,√n/2) least-favorable prior. ✓

### Deviation rulings

- **(a) BvM on exponential-rate/Gamma instead of Normal — ACCEPT.** The author's argument is
  *correct*: for Normal-Normal (known variance) the posterior variance is σ²/n and the MLE's
  sampling variance is also σ²/n, so once centered the two laws are the *same* Gaussian at every
  n — TV≈0 identically, nothing converges, no pedagogy. The exponential-rate model gives a
  genuinely right-skewed Gamma posterior (skew `0.886` at n=5 → `0.095` at n=500) whose fusion
  with the MLE law you can *watch*. Both distributions are constructed correctly: posterior
  Gamma(a₀+n, b₀+S) via `rng.gamma(a₀+n, 1/(b₀+S))` (rate parameterization, matches the module's
  Gamma-rate convention); MLE sampling law n/Gamma(n, rate=λ₀) since Σy~Gamma(n,rate). The TV is
  computed against the **simulated MLE sampling distribution** (not the analytic N(θ̂, I⁻¹/n)) —
  a *stronger* demonstration than comparing to the Gaussian, and legitimate since BvM's claim is
  precisely posterior ≈ sampling-law-of-MLE. Faithful. (Note: spec item 5 does not mandate
  Normal, so this is an in-spec authoring choice, not a true deviation.)
- **(b) 3 exercises — ACCEPT.** STYLE §5 / skeleton allows 3–6. The three cover the mandated
  minimax estimator (08.1), the mandated "surprising" slot (08.2, dimension collapse), and the
  mandated ML/DL bridge (08.3, misspecified coverage = OOD overconfidence). All quotas met.

## Independent recomputation list (all reproduced from scratch, not merely re-read)

- **MLE risk pair** (§08.5): exact Σₓ pmf(x;θ)(x/2−θ)² = **(0.105, 0.105)** = θ(1−θ)/n. ✓ matches.
- **Bayes rule p=0.5** (§08.5): posterior means (0.362, 0.5, 0.638) → risk (0.029, 0.029). ✓ Confirms MLE is *dominated* here → inadmissible even in this toy (Bayes rule beats it at both θ).
- **Minimax flat risk** (Ex 08.1): (X+√n/2)/(n+√n) has constant risk (n/4)/(n+√n)² = **0.01443** at n=10; algebra confirms the n−4a²=0 condition forcing a=√n/2 and killing the θ-dependence. ✓
- **Neyman-Scott** (§08.4): σ̂²_MLE = (1/4N)Σ(Xᵢ−Yᵢ)², E = ½·2σ² = **σ²/2**. Derived independently; matches print `0.4988`→`0.5000`. ✓
- **JS = EB identity** (§08.3): ‖X‖²~(1+τ²)χ²_d and E[1/χ²_d]=1/(d−2) ⇒ E[(d−2)/‖X‖²] = 1/(1+τ²) = B, exactly. Analytic `0.6667/0.5000/0.2500` match sims `0.6654/0.4994/0.2503`. Unbiasedness claim is correct *in the marginal (EB) sense* — the wording is fine. ✓
- **Normal-Normal BvM claim** (deviation a): post var = MLE-samp var = σ²/n ⇒ centered TV≈0 ∀n. Author's justification for switching to Gamma is mathematically sound. ✓
- **Stein dimension logic**: d=2 ⇒ (d−2)=0 ⇒ JS≡MLE (no dominance); d=3 ⇒ shrinkage engages (`1.62` vs `3.01`=d). Crossover-at-d=3 semantics correct; JS⁺ risk vector all < d=10. ✓
- **Cramér-Rao** (§08.1): 1/(nI)=σ²/n=1/20=`0.05000` vs Var `0.04997`. ✓
- **Coverage** (§08.6): pv=1/(25+1/100)≈0.03998, pm≈0.9996·ȳ; ȳ~N(θ,1/25) exact ⇒ coverage `0.9499`≈nominal. Framing consistent with M06 (prior-averaged exact 1−α theorem, L276–277) — no contradiction. ✓

## Citations / notation / consistency

- **C-B anchors verified in source:** Theorem 7.3.9 (Cramér-Rao, Ch6to10.txt L579), Example 7.3.13 (scale uniform / U(0,θ) support failure, L624–635), Theorem 10.1.12 (asymptotic efficiency of MLEs, L2966). All three cited correctly. §7.3 (risk/Bayes rules) and §10.1 (MLE asymptotics) anchors accurate. Efron-Morris and booklet ch. 9 cited by concept/preview (allowed). No fabricated page numbers. No R-leak.
- **Notation §3:** N(·,·)=variance, Gamma(α,β)=rate — both honored, including the scipy Gamma trap commented inline (L206). ✓
- **Numbers-contract spot-check (12 checked, all ⊆ printed output):** `0.3653`,`0.3651`,`0.0256`,`0.05000`,`0.04997`,`9.98`/`1.99`/`1.25`,`0.1668`/`0.0165`,`0.4988`/`0.5000`,`(0.105,0.105)`,`(0.029,0.029)`,`0.9499`,`0.0144`. Exercise reconciles (`0.000`/`1.997`/`3.590`, `0.94925`/`0.946`) also match. ✓
- **SPINE-INDEX consistency:** M04 Fisher/asymptotics forward-promise ("θ̂ ~ N(θ,1/nI) and BvM") cashed in §08.1/§08.4; M06 coverage callback (prior-averaged 1−α) honored without contradiction; M07 unidentifiability washout (θ₁+θ₂ concentrates, θ₁ keeps prior width) faithfully referenced in §08.4. ✓
- **Non-tribalism:** complete-class stated with the correct hedge "Bayes rules **and their limits**" / figure title "(limits of) Bayes rules" (L293, L302) — the limit clause is present and load-bearing, not dropped. Module treats CRLB, BvM, Stein, complete-class as serious theorems and honestly flags genuine disagreements (Neyman-Scott, misspecification, boundary). Stays inside the BRIEF's no-tribalism rule; only the thrice-repeated slogan is worth softening (sev-3 above).

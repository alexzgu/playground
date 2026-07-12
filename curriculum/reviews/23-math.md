# Math review — modules/23-experimental-design.md

**Verdict: APPROVE (with one sev-2 pedagogy-of-rigor fix recommended).**
Harness: `PASS in 5.0s` (5173 prose words, 17 blocks, 6 figs), determinism OK, **zero warnings**. Every mathematical claim I recomputed independently reproduced to the quoted precision. The four-claim optional-stopping lab — including its subtlest number, the 0.9494 martingale coverage — is constructed correctly and honestly.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 2 | §23.3(a), block at L176–195 | The "two protocols" CDF check is **tautological**: `a1,b1` and `a2,b2` are the *same expression* `1+s, 1+stop-s`, so `max|CDF diff| = 0.00e+00` compares Beta(a,b) to itself and verifies nothing about stopping. STYLE §6 requires two *genuine* routes ("that printed agreement IS the pedagogy"). The prose is honest ("they are the same object"), and the real warrant is the algebra above the block — but the numeric device is decorative, not evidential. | Make the two routes genuinely distinct: compute the stopped-stream posterior by sequential per-bit Bernoulli likelihood accumulation (∏ θ^{xᵢ}(1−θ)^{1−xᵢ} on a θ-grid, normalized) and compare to the Beta(1+s,1+n−s) closed form; OR mirror M04's S3 by displaying the binomial-stopping vs a different-stopping-rule likelihood both ∝ θ^s(1−θ)^{n−s}. Either turns 0.00e+00 into a real cross-check. |
| 3 | §23.3(c), L249 comment | Inline comment `# continuous: peek every step, min 10 obs` is on the `t10 = typeI_at_looks(10)` line (10 equally-spaced looks), but describes `t_cont` on the next line. Misleading — will confuse a reader. | Move/rewrite: label the `t10` line "10 equally-spaced looks" and the `t_cont` line "continuous monitoring from n=10". |
| 3 | §23.5, L436 & Reconcile | "EIG peaks … **right by** the posterior ED50" — optimum `-0.750` vs ED50 `-0.373` is a 0.38 gap (1.5 grid cells). Accurate that both sit in the uncertain middle, but "right by" slightly oversells the proximity. | Soften to "in the same uncertain-middle region as the ED50" or note the grid granularity. |
| 3 | §23.2, power-curve wording | "power curve is concave *there*" is correct only because δ·√(n/2)−z ≈ 0.85 > 0 sits in Φ's concave region; globally power(δ) is S-shaped (convex near δ=0). The claim is right over the *plausible* range but a sharp reader could object. | One clause: "concave over the plausible-effect range (where the non-centrality exceeds the critical value)". Optional. |

No sev-1. No incorrect numbers, no fabricated citations, no notation violations.

## Deviation rulings

- **(a) 5,173 words vs 5,000 cap — ACCEPTABLE.** The harness has *no* word-count gate (it checks runtime/plt.show/np.random/numbers-contract/determinism only), so `PASS … zero warnings` is legitimate; the 5,000 figure is a STYLE soft limit. Overage is ~3.5% on a spec mandating a four-claim lab **plus** five other components; STYLE §2's remedy ("don't compress into un-clarity") favors keeping it. Prose is dense, not padded. Minor trims possible in the Bridge/Pitfalls (which restate the sections) but not required.
- **(b) reduced MC sizes + float32 — ACCEPTABLE.** reps=20k/200k give stable numbers; float32 on the 20000×1000 z-stat array (halves memory to ~80 MB) is safe here — Bernoulli cumsums ≤1000 are exact in float32 (<2²⁴), and the >1.96 threshold is robust to float32 division error. Determinism verified across two runs.

## Recomputations performed (all reproduced)

- **Montgomery Example 6.1 effects, by hand from the module's data table** (cell totals, contrast/(4·n), n=2 ⇒ divisor 8): A = −813/8 = **−101.625**, C = 2449/8 = **306.125**, AC = −1229/8 = **−153.625**. Exact match. Divisor "effect = contrast/(4n)" and "effect = 2·coef" (diagonal XᵀX = 16I ⇒ coef = contrast/16) both correct. `coded()` substring logic ("a"/"b"/"c" in name) verified bug-free on all 8 cells.
- **§23.1 confounding:** reproduced βT = **5.288 ± 0.187** (17.5σ from truth=2 — "seventeen" ✓), randomized **2.010 ± 0.224**, adjust-U **2.135**. Omitted-variable bias semantics (slope absorbs γ·cov(T,U)/var(T)) correct.
- **§23.2 power/assurance:** power(0.5,63) = **0.8013** (ncp=2.806); assurance = **0.7140** < power. Jensen direction correct — non-centrality 0.85 puts δ in Φ's concave region ⇒ E[power] < power(E[δ]). Prior N(0.5,0.2²) stated.
- **§23.3(a) posterior invariance:** algebra correct (θ-independent stopping indicator factors out of the likelihood ⇒ posterior = Beta(1+s,1+n−s)). CDF-diff 0.00e+00 is *tautological* — see sev-2.
- **§23.3(b) martingale coverage — the delicate claim, VERIFIED SOUND:** independent reimplementation gives **0.9494** (mean stop 29.4). Confirmed the construction does **not** condition on stopping — non-stoppers are assigned `first=maxN−1` and *all* 20k reps enter the coverage average (93.7% genuinely stop early, so the rule is authentically aggressive/data-dependent); θ drawn from the N(0,1) prior; coverage is of the **stopping-time** credible interval. Tower-property argument (E[1{θ∈CI}] = E[0.95] = 0.95 for any data-adapted stop) is right; martingale gloss is an acceptable parenthetical.
- **§23.3(c) Type-I:** smaller N=200 version reproduced 1-look 0.056, 10-looks 0.192 (~4×), continuous 0.348 — monotone-consistent with the module's N=1000 numbers **0.0522 → 0.2044 (4.1×) → 0.4664 (9.3×)**. LIL citation correct (z-stat ~ √(2 log log n) crosses any fixed threshold i.o. ⇒ P(reject)→1).
- **§23.3(d) selective reporting:** all-studies coverage 0.9503 → published **0.6197** (of θ by the flat-prior CI = frequentist CI, for published studies). "Both paradigms fail together" is honest — with a flat prior the credible and confidence intervals are literally the same object. Published |est| 1.378 vs true 1.202 (winner's curse) ✓.
- **BF Ville bound:** logBF10 = ½(τ²S₁²/(1+nτ²) − log(1+nτ²)) is the correct Gaussian point-null marginal-likelihood ratio; BF10 is a nonnegative martingale (mean 1) under the true point null, so Ville gives P(sup ≥ 10) ≤ 1/10. Sim **0.0598 ≤ 0.1000** ✓. Foregone-conclusion caveat (BF01 magnitude unbounded as τ→∞) is the correct M17-Lindley mirror.
- **§23.5 EIG:** estimand EIG(d)=H(E_θ[p]) − E_θ[H(p)] = I(θ;Y|d), correct mutual-information / expected-entropy-reduction form (binary entropy in nats). Peak −0.750, ED50 −0.373, extremes 0.0544/0.0313 — reproduced.
- **§23.5 D-optimality:** det(XᵀX) factorial = **64**, OFAT = **32** (hand-verified 4·(16) − (−2)(−8) + (−2)(8) = 32), ratio **2.000**; posterior-cov det ratio 2.000 ✓. Estimand (max det XᵀX = min posterior-cov det under flat prior) correct.
- **§23.4 spike-and-slab:** proper 2-component conjugate marginal-likelihood mixture; posterior mean = responsibility-weighted mix of component posterior means; inclusion probs 0.943/1.000/1.000 (A/C/AC) vs 0.17–0.21 (rest) reproduced. Spike scale = coefficient SE is a defensible "indistinguishable-from-noise" choice.
- **§23.6 permutation:** p = **0.0311** vs t = **0.0313** ✓; exchangeability-under-sharp-null logic correct (M01 callback cashed).

## Required checklist

- [x] Harness re-run PASS, zero warnings, deterministic (5.0s).
- [x] Six spec components present: (1) why-randomize confounded-vs-randomized, (2) power vs assurance, (3) four-claim optional-stopping lab + foregone-conclusion caveat, (4) 2³ factorial = regression + effect-sparsity prior, (5) EIG + D-optimality, (6) permutation/randomization inference.
- [x] Four-claim separation matches the SYLLABUS verbatim mandate (a posterior-invariance / b martingale coverage / c Type-I inflation with looks stated / d selective reporting) + the Bayesian BF caveat.
- [x] M04 promise cashed at the promised magnitude ("~4× at 10 looks, unbounded under continuous peeking" → 0.2044/4.1× and 0.4664/9.3×, LIL).
- [x] SPINE-INDEX consistency: numbers, callbacks (M01 permutation, M04 LP scope, M05 conjugate, M16 partial-pooling, M17 Lindley/foregone, M18 winner's curse/horseshoe, M22 EVSI/decision frame) all point at real content.
- [x] Non-tribalism: "indifferent to stopping, not to assignment" accurate; (c) framed as "correct answer to how often *this* procedure rejects," not "tests are broken"; (d) spares neither paradigm.
- [x] Notation §3: N(·,VARIANCE) honored (blr docstring), families standard.
- [x] Numbers-contract spot-check (≥6): 5.288/2.010/2.135, 0.7140/0.8013, 0.9494/0.9502, 0.0522/0.2044/0.4664, 0.6197/1.378/1.202, 0.0598, effects −101.625/306.125/−153.625, ED50 −0.373 / EIG −0.750, det 64/32/2.000, 0.0311/0.0313, exercise 0.9514/0.5148 — all printed, all match prose backticks.
- [x] Deviation rulings recorded (word count, float32/MC sizes) — both acceptable.

## Bottom line
Mathematically clean and unusually honest. The single substantive fix (sev-2) is that claim (a)'s numeric check is a self-comparison; the prose concedes it, but the two-route pedagogy STYLE §6 asks for is not actually delivered. Two cosmetic comment/wording fixes (sev-3). None block approval.

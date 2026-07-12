# Math review — modules/10-metropolis-hastings.md

**Verdict: APPROVE (with 2 sev-2 merge items; mathematics is clean).**
Referee: math. Harness re-run `--check-determinism`: **PASS in 64.7 s, exit 0, zero warnings**, byte-identical two-run output. Safety: content is benign (MCMC theory + simulated annealing + EBM bridge); no unsafe material despite the classifier gap during authoring.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 2 | header + whole-module | **Block count 21 > STYLE §2 cap of 16 runnable blocks** (harness confirms "21 runnable blocks"). Overage is driven by the encouraged figure/compute split (6 figure blocks). Flag for merge per instructions. | Merge each figure block into its preceding compute block (e.g. §10.2 trace-fig into the sampler block, §10.3 sweep-fig into the sweep block). That lands ~15 blocks with zero content loss. Or obtain an explicit cap waiver at merge time. |
| 2 | header L7 `> **Runtime.** ~40 s.` | Measured runtime is **~65 s** (harness "PASS in 64.7 s"; block-time sum ≈64.5 s, block 5 sweep alone 27.2 s). STYLE skeleton requires the *measured* value; ~40 s understates it ~60%. | Change to `~65 s` (still far under the 120 s target / 300 s cap). |
| 3 | §10.5 L379 | The "mysterious mismatch" framing for plain-vs-rank R̂ is overstated *for this well-behaved target*: plain `1.0013` vs rank `1.0014` differ by 1e-4 — negligible. The genuine rank-vs-plain divergence is carried by the fooling example (`1.7365` vs plain `5.5422`). | Soften: note that here the two agree to 1e-4 because the chains are well-mixed, and forward-reference §10.6 where rank-normalization actually changes the verdict. |
| 3 | §10.3 L220 | "barely half the peak `110.0`" for ESS `63.4` — that is 0.576, slightly *more* than half. | Reword to "about 58% of the peak" or "little more than half". |

No sev-1 findings. Every derivation, tag, and numeric claim I independently recomputed holds.

## Required checklist

- [x] **Determinism / harness:** `--check-determinism` PASS, exit 0, two runs byte-identical, no warnings, 64.7 s.
- [x] **Numbers contract (spot-check ≥6, did 11+):** §10.2 quantiles 0.1688/0.3116/0.4864 & mean 0.3177 vs exact; §10.3 acc 0.240/step 0.337/peak 110.0/0.598→63.4/1-D 0.439; §10.4 crossings 0 & P 0.0000, step-10 2798/0.5026/acc 0.200; §10.5 ESS 2304.9, R̂ 1.0014, az 2313.4/1.0014, plain 1.0013; §10.6 1.0028/573.6/1.7365/6.1; §10.7 0.8023/0.6447/0.518/9.00/0.7516; bridge −7.400/−2.019/−8.603; Ex 0.00e+00, A/B 401/4012, sep 6650/2050/220. **All match printed output.**
- [x] **Spec compliance (SYLLABUS "10-metropolis-hastings"):** all 8 required items present — Markov-chain primer + 6-line DB⇒stationarity + sufficient-not-necessary 3-cycle + numeric DB on 3-state ✓; 30-line RW-MH on Beta-Binomial with quantile match ✓; d=50 sweep with 0.234@2.38/√d AND 1-D 0.44 both printed, scope stated ✓; bimodal mode-hopping predict-first + tempering→M19 ✓; hand ESS = M/(1+2Σρ)/split-R̂/rank-normalized note ✓; fooling example ✓; 2-state spectral-gap 1/(1−λ₂) vs ACF ✓; simulated-annealing bridge ✓. Skeleton (Spine/Which-line/Promise/Prereqs/Runtime/Sources, Bridge, Pitfalls, 4 exercises, ≤7 Takeaways) all present; 4843 prose words (in 2500–5000 band).
- [x] **Citations:** booklet ch. 11 (opened — MH, detailed balance, symmetric-proposal reduction, RW proposal) and ch. 15 (opened — MCMC difficulties/diagnostics) genuinely cover the cited material; MCMT ch. 3–5/12, RGG 1997, Vehtari 2021 cited by concept, none fabricated.
- [x] **Notation §3:** N(μ,σ²)=variance respected (N(±5,1), log_bimodal uses −½(x∓s)²); scipy `stats` idioms; no R anywhere.
- [x] **Setup block (§4.1):** verbatim template, only SLUG changed; SEED=0, rng defined; randomness only through seeded generators; figures only via `save()`; all 6 figures referenced and discussed.
- [x] **SPINE-INDEX consistency:** Beta(1,1)+6/20 → Beta(7,15) matches the M05 conjugate convention (1+k, 1+n−k); prereqs 04/05/09 consistent.

## Independent recomputation list (verified, not merely read)

1. **DB ⇒ stationarity proof (as written):** valid line-by-line for the discrete sum; the swap step uses DB correctly, the row-sum→1 close is right.
2. **3-cycle counterexample genuinely stationary & non-reversible:** u=(⅓,⅓,⅓), uP=u (column sums ⅓) — stationary; flow asymmetry = ⅓ (one-way circulation) — not reversible. Both confirmed (harness `0.00e+00` / `0.333`). It is a *genuine* stationary non-reversible chain.
3. **MH acceptance ratio + symmetric reduction:** α=min(1, π(θ′)q/π(θ)q); π(θ)q(θ′|θ)α = min(π(θ)q(θ′|θ), π(θ′)q(θ|θ′)) symmetric ⇒ DB. Correct; matches booklet ch. 11's verified margin.
4. **d=50 optimum:** 2.38/√50 = 0.3366 ≈ 0.337; ESS peak (110.0) sits at step 0.337 / acc 0.240 in the swept grid — measured correctly; 0.234 scope stated precisely (asymptotic-in-d, i.i.d.-product, diffusion limit); 1-D 0.439 ≈ known 0.44; HMC 0.651 forward ref correct.
5. **ESS semantics (the flagged 2304.9 vs 2313.4):** confirmed `az.ess` default = **method='bulk' (rank-normalized)** and `az.rhat` default = **method='rank'** in ArviZ 1.2.0. Hand rank/bulk ESS (rank_normalize → ess_multichain, no split, Geyer initial-positive-pairs) is **like-with-like** with az.ess bulk; the 0.37% gap is the autocorr-truncation rule, **not coincidental**. Raw ESS 2260.7 is the honest plain-ESS foil.
6. **Rank-normalized split-R̂ by hand truly rank-normalizes:** `rank_normalize` uses Blom scores z=Φ⁻¹((r−3/8)/(n−¼)) over the pooled M draws — the Vehtari transform. Ranking the unsplit chains then split_rhat splits *once* into 2000-length halves with identical membership to az's split-then-rank pool ⇒ identical result; module's printed `1.0014 == 1.0014` confirms empirically.
7. **Fooling example fair:** starts {−5,−5,+5,+5}, each chain locally stationary in its basin; single-chain split-R̂=1.0028 (both halves same mode) passes while 4-chain R̂=1.7365 (rank) / 5.5422 (plain) fires and ESS→6.1 (two distinct answers). Construction is honest, not rigged.
8. **Spectral-gap demo:** λ₂ = 1−a−b = 1−0.05−0.15 = 0.8 exact; τ_int=(1+λ₂)/(1−λ₂)=9.00 exact (2-state indicator is AR(1) with corr λ₂). Printed ρ[1,2,3]=0.8023/0.6447/0.518 are k=1,2,3 vs λ₂^k=0.8/0.64/0.512; deviations 0.002–0.006 are within ~1–1.3 lag-SE (≈0.005 at N=2·10⁵) — within MC error, "almost exactly" fair.
9. **Bimodal rescue lesson correct:** step 10 buys 2798 crossings and P=0.5026 but crashes acceptance to 0.200 and is explicitly framed as a *1-D illusion* (no single scale spans barrier and explores mode in higher-d) — larger steps trade acceptance for crossing, not a free lunch. Stated correctly.
10. **Evidence-cancels exercise:** additive constant cancels in `lp_prop − lp_current`; with shared seed the two chains are byte-identical (`0.00e+00`) — exact, not approximate. EBM bridge (Ex 10.4) sound: sample e^{−E} via energy differences, Z dodged like p(y); DB verified to machine precision on the 4-state kernel.

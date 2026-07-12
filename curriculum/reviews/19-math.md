# Math review — 19-mixtures-dp.md

Referee: mathematical-statistics verification pass. Verdict: **APPROVE** (0 sev-1, 0 sev-2, 2 sev-3).

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | L191 fig alt-text (`gmm_uncertainty`) | Caption says "the same **200** points" but `n=250` (L53, printed `n=250`). | Change "200 points" → "250 points" in the alt text. |
| 3 | L6 header `**Runtime.** ~9 s` | Harness wall-clock is 15.5 s (determinism run). If 9 s is code-only that is plausible, but the gap is large; STYLE §2 wants the *measured* figure. | Re-measure code runtime and set the header to it (still far under the 300 s cap either way). |

Nothing rises to sev-1 or sev-2. All flagged-risk items below checked out clean.

## Determinism / harness
- `python tools/run_module.py modules/19-mixtures-dp.md --check-determinism` → **PASS in 15.5 s, zero warnings**, 18 blocks, 6 figs, 4338 prose words (in the 2,500–5,000 band).

## Deviation rulings
- **(a) Hand-written numpy Gibbs throughout instead of NumPyro — APPROVED, STYLE-compliant.** STYLE §4.7 forbids PyMC *sampling* and forbids un-smoke-tested NumPyro idioms; it does **not** mandate NumPyro per module. Hand-rolled conjugate/blocked Gibbs is the same idiom M11 uses, mirrors the booklet's ch.14 §14.2 / insert samplers, and sidesteps NumPyro's discrete-latent enumeration machinery (which is exactly the un-smoke-tested surface the rule guards). Author's reasoning is sound. Runtime 15.5 s ≪ budget.
- **(b) Tempering wells at ±5 matching M10 — APPROVED, callback exact.** M10 (L241–281) uses an equal mix of N(−5,1)/N(+5,1), step 1.0, 40,000 iters, **0 crossings, P(θ>0)=0.0000**. M19 L234 quotes "N(−5,1) and N(+5,1) … 0 crossings in 40,000 iterations" — verbatim-accurate attribution. M19's own demo runs 20,000 steps (plain P=0.000) and does not misattribute.

## Recomputation list (all independently verified)
- **E[Kₙ] = α[ψ(α+n)−ψ(α)]** — derivation correct: Σᵢ₌₁ⁿ α/(α+i−1) = α Σⱼ₌₀ⁿ⁻¹ 1/(α+j) = α[ψ(α+n)−ψ(α)] via the standard digamma identity. Printed 6.793 / 11.590 / 23.587 at α=1/2/5, n=500 — reproduced to the printed precision.
- **Harmonic-number claim** — H₅₀₀ = 6.79282… → 6.793, and at α=1, ψ(1+n)−ψ(1)=Hₙ. Correct.
- **crude α·ln n at α=5** = 5·ln 500 = 31.073 → `31.07`; **asymptote** α·ln(1+n/α)=5·ln 101 = 23.076 → `23.076`, correctly below exact 23.587. ✓
- **CRP new-table indicators independent — VERIFIED TRUE (the flagged subtle point).** P(Bᵢ=1 | full seating history)=α/(α+i−1) for *every* history (denominator is always α+i−1, numerator always α, independent of the partition of the i−1 seated). A conditional probability constant in the past ⟹ Bᵢ ⊥ past ⟹ mutual independence by induction. The module's warrant ("depends only on i, not on the seating so far") is exactly this argument, and the code simulates independent Bernoullis matching the exact digamma to max gap `0.161`. Not a defect — a correctly-handled trap.
- **Ex 19.2** — EK(1)=5.8780→`5.88`, EK(3)=13.1639→`13.16`, ratio 2.2395→`2.24` (not 3). Digamma arithmetic correct; the sub-linear-in-α explanation is right.
- **CRP exchangeability** — both orderings score −1.791759 (reproduced). Order-invariance ⟹ de Finetti ⟹ DP framing is sound.
- **Stick-breaking** E[ωⱼ]=(1/(1+α))(α/(1+α))ʲ⁻¹ — reproduced: α=1 → [0.5,0.25,0.125], α=5 → [0.167,0.139,0.116]. Matches booklet ch.14 verified note (L493). Effective-# 3.0 / 9.4 consistent.
- **Stick-breaking full conditional** γⱼ|· ~ Beta(1+nⱼ, α+Σ_{ℓ>j}nₗ) — **matches the source.** It is the DP specialization (δ₁=0, δ₂/(1−δ₂)=α) of the handwritten insert's Pitman–Yor form Beta(1−δ₁+eₚ, δ₂/(1−δ₂)+(p−1)δ₁+fₚ) (ch.14 p.157/161), and is *literally* the typeset §14.2 blocked-Gibbs step 2 Beta(aⱼ,bⱼ), aⱼ=1+ΣI(dᵢ=j), bⱼ=α+ΣI(dᵢ>j) (ch.14 p.159). Faithful, correct specialization. `sum_gt` code (`counts[::-1].cumsum()[::-1]-counts`) correctly = Σ_{ℓ>j}nₗ.
- **EM** — full-GMM E-step (responsibilities via logsumexp) and M-step (responsibility-weighted MLE for π,μ,Σ) are **MLE-EM** (no prior term), bookkeeping internally consistent; log-lik −924.31→−829.88 monotone. Correctly framed as M13's minimal known-variance EM cashed to the full object (dedup honored; M13's minimal example not re-taught).
- **Gibbs NIW conjugacy** — κₙ=κ₀+n, νₙ=ν₀+n, mₙ=(κ₀m₀+nx̄)/κₙ, Ψₙ=Ψ₀+S+(κ₀n/κₙ)(x̄−m₀)(x̄−m₀)ᵀ, Ψ₀=cov(X)(ν₀−d−1)=cov(X) so E[Σ]=cov(X) with ν₀−d−1=1. All standard and correct; Dir(a₀+counts) weights conjugate. DP-mixture NIG updates (an=a₀+nⱼ/2, bn with the κ₀nⱼ/κₙ correction term) correct; InvGamma via reciprocal-Gamma correct.
- **Label switching** — global relabel is an exact posterior symmetry, so unconditional acceptance is the right MH move (accept prob 1). 27 crossings reproduced. Ordering-constraint **bias caveat present** (L228: overlap bias + Stephens'-method pointer). Ordering canonicalization makes §19.1's label probabilities swap-invariant, so the artificial swap does not contaminate the 24-vs-38 comparison.
- **Tempering swap** — code `d=(β_j−β_{j+1})(lp[j+1]−lp[j])`, accept if log u < d, with `lp`=untempered log p. This equals log of min(1,[π_i(x_j)π_j(x_i)]/[π_i(x_i)π_j(x_j)]) with π_i∝p^{β_i} — matches the standard replica-exchange ratio exactly. Within-temp MH uses β·(lpp−lp), correct for target p^β. Trapped-plain-chain claim (P=0.000) and tempered recovery (0.532, swap 0.79) sound.
- **Truncated-DP fit** — L=15 truncation flagged as computational cap "exact as L→∞" (Ishwaran–Zarepour), pitfall L484 reinforces. Posterior over K = # occupied components (`len(unique(z))`), mode 4 (p=0.482), mean 4.76 — semantics consistent, never <4, hedges up to 5–6. ✓
- **ZIP (Ex 19.1)** — P(struct|y=0)=π/(π+(1−π)e^{−λ}) correct; s can be 1 only where y=0; π~Beta, λ~Gamma conjugate; λ uses non-structural (incl. genuine Poisson zeros) — correct. plain λ̂=1.769 (true mean 0.6·3=1.8), ZIP recovers π=0.413, λ=3.019. ✓

## Uncertainty-map semantics
"Uncertain" = P(low cluster) ∈ (0.1,0.9), **identical threshold** for EM (`resp_lo_em`) and Gibbs (`prob_lo_gibbs`) and for the figure band. EM 24 vs Gibbs 38 consistent across print + figure. Ex 19.4 uses a *different* statistic (top-label confidence >0.95) for a *different* question (205 very-sure, 0.97 agree) — legitimately separate, not an inconsistency.

## Citations / notation / consistency
- Sethuraman 1994 (stick-breaking), Ishwaran–Zarepour (truncation), Neal 2000 (by concept), booklet ch.13–14 + insert — all verified against ch.14 source. Antoniak/GEM lineage matches booklet.
- Notation §3 respected: N(μ,σ²)=variance, Gamma rate/scale trap commented inline (`1/bn`), IW/NIG conventions correct.
- SPINE-INDEX callbacks accurate: M01 Pólya-urn/de-Finetti (promises "CRP via Pólya urn (M19)"), M07 nonidentifiability-by-symmetry (established face), M11 augmentation (promises "mixture labels (M19)"), M13 minimal-EM dedup (established "full GMM = M19's"), M10 tempering promise cashed. Module does **not** re-teach M13's minimal example.
- Numbers-contract spot-check (>6): 38/24, 0.916/0.837, 27, −0.01/2.56, 0.000/0.532/0.79, 6.793/23.587, 31.07, −1.791759, 3.0/9.4, 4/0.482/4.76, 1.769/0.413/3.019, 5.88/13.16/2.24, 0.013/0.92, 205/0.97 — all ⊆ printed output at matching precision.

# Review — modules/05-conjugate-updating.md (mathematical-statistics referee)

**Verdict: APPROVE** (3 sev-3 polish findings; 0 sev-1, 0 sev-2). Harness PASS, zero warnings, determinism OK. All 9 Required items present and correct. Every derivation recomputed independently and matches. S2 staged correctly. `nig_post` consistent with module 04.

## Findings table

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | §05.6 plug-in coverage (`0.8307`) | The interval `[4,9]` is built from the 5th/95th Binomial(10, 0.625) percentiles and *called* a "90% interval," but under the plug-in's OWN model it covers `0.9525` (discreteness makes it a ~95% interval). The prose attributes the full `0.90 → 0.8307` gap to the epistemic term, conflating discreteness with epistemic under-coverage. The module *does* flag discreteness for the predictive interval `[2,10]` ("over-covering… support is coarse and discrete") but not symmetrically for the plug-in. Direction of the lesson is correct (and if anything conservative — an over-wide interval still under-covers). | Print the plug-in interval's own coverage (`0.9525`) to isolate the epistemic drop, or add the same discreteness caveat you gave the predictive interval. One sentence. |
| 3 | §05.5 NIG MC block, `stats.invgamma(a=an, scale=bn)` | STYLE §3 requires an inline comment on scipy calls that "embody a convention trap (Gamma rate/scale)," and the module's own Pitfall explicitly names "Gamma/**Inverse-Gamma**… scipy's gamma/invgamma take scale." The one live `invgamma` call carries no inline convention comment (only `# sigma^2 \| y`). Mapping IG(α,β)→`scale=β` is correct; only the required comment is missing. | Add `# IG(a,b): scipy scale = b (course convention, §3)` on the invgamma line. |
| 3 | §05.8 MVN block check | Verification is MC via neighbourhood rejection (`\|x−x2\|<0.1`, ~2831 of 8M kept); diff `0.0096`/`0.0093`. Prose calls this "pure Monte-Carlo error," but it also includes a small finite-window conditioning bias (conditioning on a neighbourhood, not a point). Adequate as a STYLE §6 sanity check, and the exact identity + value-independence of Σ₁\|₂ are stated correctly. For infrastructure load-bearing across M14/20/21 a machine-precision algebraic cross-check would be reassuring. | Either soften "pure Monte-Carlo error" to "Monte-Carlo + finite-window error," or add a 2-line exact cross-check (e.g. Σ₁\|₂ via the precision-matrix/Schur route) alongside the MC overlay. Optional. |

## Required checklist (SYLLABUS 05, 9 items)

1. Open: conjugacy = exp-family closure — ✓ §05.2 (natural-form prior (τ₀,n₀) → posterior (τ₀+S, n₀+n)).
2. Two full derivations (Beta-Binomial §05.3, Normal-Normal §05.4) + compressed table for the other three, each with predictive twist — ✓. NegBin ✓; Student-t df=2aₙ, loc=mₙ, scale²=bₙ(κₙ+1)/(aₙκₙ) ✓ with MC-vs-closed-form ✓; Dirichlet add-α ✓.
3. Master shrinkage formula derived; κ/(κ+n) form; "prior worth κ"; slide n — ✓ §05.3.
4. S2 staged (2-for-2; predict; Beta(3,1)⇒0.75) — ✓ §05.1, **two committed numbers before code** (posterior mean + predictive), Setup→Predict→Reason→Run→Reconcile.
5. Predictive vs plug-in: law of total variance decomposition ✓; strict widening scoped to "these fixed-dispersion families," universal claim **avoided** ✓ (spec compliance); BB 4.69 vs 2.34 ✓, GP 3.0 vs 2.0 ✓; plug-in under-covers predict-first ✓.
6. A/B end-to-end: A=41/1000, B=57/1000, Beta(1,1); P(B>A) by paired draws; E[uplift]; expected loss ship-B vs ship-A; decision printed — ✓ §05.7. Loss = regret max(θ_other−θ_ship,0); decision arithmetic correct.
7. Sequential = batch exercise — ✓ Ex 05.1.
8. Gaussian conditioning toolkit: block formulas derived once + verified on 3-d — ✓ §05.8.
9. Small conjugate library built — ✓ §05.2 (5 helpers).

Plus: Bridge ✓, Pitfalls (5) ✓, Exercises (4; ≥1 surprising [05.2], ≥1 ML bridge [05.3]) ✓, Takeaways (7 ≤7) ✓, 16 blocks (cap 16) ✓, runtime ~6 s ✓.

## Independent recomputation list (all confirmed)

- Beta-Binomial S2: Beta(3,1) mean = predictive = **0.7500** ✓.
- Master shrinkage identity (a+s)/(a+b+n) = κ/(κ+n)·m₀ + n/(κ+n)·θ̂ — algebraic identity holds ✓.
- NIG→Student-t: kₙ=21, aₙ=11, bₙ=43.4607 ⇒ scale=**2.0345**, df=**22**, t sd=**2.1338** ✓; MC agreement (4.6669/4.6672, 2.1329/2.1338, 5th/95th 1.174–1.176 / 8.161–8.163) is a real cross-route check ✓; booklet ch.8 (line 819) supports the citation.
- Gamma-Poisson→NegBin(r=4,p=2/3): mean **2.0**, var **3.0** vs plug-in Poisson var 2.0 ✓.
- Dirichlet add-α / Francisco trap: α=1 ⇒ P(Francisco)=**0.0041**, κ=αV=10⁴; α=0.0001 ⇒ 0.7843, **κ=αV=1** (prior worth 1 obs) ✓ — matches spec exactly.
- Law of total variance decomposition — standard identity, correctly written; BB exact var 4.6875 = closed form ✓.
- Plug-in 90%-interval realized coverage: honest coverage of [4,9] = **0.8317** (module 0.8307, seed-consistent) ✓; semantics caveat = finding #1.
- A/B expected loss: P(B>A)≈**0.9510**, loss ship-B **0.000199** vs ship-A **0.016134**, ship B ✓ (my reseed: 0.951/0.0002/0.0162).
- Ex 05.2 ratio √((K+m)/(K+1)) = **1.569** ✓.
- Ex 05.4: n=5 → 0.1429/0.7407, n=500 → 0.2809/0.3065 ✓.
- MVN block formulas μ₁|₂, Σ₁|₂ correct; index bookkeeping (idx1=[0], idx2=[1,2], np.ix_/solve) correct; check = finding #3.
- `nig_post` parameterization byte-identical to module 04 (kₙ=k₀+n, mₙ=(k₀μ₀+nx̄)/kₙ, aₙ=a₀+n/2, bₙ=b₀+½S+k₀n(x̄−μ₀)²/(2kₙ)) — no contradiction ✓.
- Numbers-contract spot-check (>6): 0.7500, 0.3333/0.6429/0.7956/w_prior 0.008, 13.1209/13.7061/0.8421/0.7947, 2.0/3.0, df 22/scale 2.0345, 0.0417, 4.69/2.34, 0.8307/0.9822, 0.9510/0.000199/0.016134, 0.7999/0.5397, Beta(8,4), 1.569, 0.0041/0.7843 — all match printed output.

## Notes
- Gamma RATE convention: `gamma_poisson_update` returns a rate; no live `stats.gamma(...)` call on it, and NegBin p=b/(b+1) uses the rate correctly. Only the `invgamma` call lacks its inline comment (finding #2).
- Citations (C-B §7.2, §3.4; booklet ch. 3–5, 8) all verified against local sources; booklet ch.8 covers Beta-Binomial, Normal-Normal, and the Student-t posterior predictive as claimed.

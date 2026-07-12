# 11-gibbs-augmentation — Mathematical referee review

**Verdict: APPROVE** (no sev-1/sev-2; 5 sev-3 polish items). Determinism PASS, zero warnings, single-run 15.3 s (matches prose "~15 s"). Every prose backtick-number cross-checked against printed output — all match. Both author deviations flagged in the brief adjudicated **CORRECT AS WRITTEN**.

## Author-deviation rulings

- **(a) `rinvgamma(a,b,rng)` = `1/rng.gamma(a, 1/b)` — RULED CORRECT.** The convention chain is right: X~Gamma(shape a, rate b) ⇒ 1/X~IG(shape a, scale b); numpy `rng.gamma(shape, scale)` takes scale = 1/rate, so `rng.gamma(a, 1/b)` draws Gamma(a, rate b) and its reciprocal is IG(a, scale b) = course/STYLE §3 `invgamma(a=a, scale=b)`. Verified numerically against scipy at (a,b)=(3,5): empirical mean 2.5010 vs scipy IG mean 2.5000, empirical var 6.238 vs 6.25. No rate/scale slip. **Every use site is consistent** with this: §11.2 `rinvgamma(a_cond, b_cond, rng2)`, §11.3 `rinvgamma(a0r+n/2, b0r+0.5·RSS, rng3)`, §11.7 inlined identically as `1.0/r.gamma(a_c, 1.0/b_c)`, Ex 11.2 same inline form. The inline comment correctly documents the trap (STYLE §3 requirement satisfied).
- **(b) Ex 11.4 corrected premise — RULED CORRECT.** Read the two update lines: `z = Xp @ beta_c + normal(...)` and `beta_c = Vb @ (Xp.T @ z) + Lb @ normal(...)`. Neither references `ypr`. Dropping the sign-truncation removes the sole point where the labels enter, so the chain output is genuinely independent of the data — it would print the same numbers for any labels. The substitution β_{t+1} ≈ (XᵀX+I/τ²)⁻¹XᵀX·β_t + noise is right; with τ²=100, n=2000 the operator ≈ I, giving a prior-tethered chain. (Nuance below, F4.)

## Independent recomputations performed

| Quantity | Module | My independent check | Status |
|---|---|---|---|
| rinvgamma convention (moments) | scale=b | empirical mean 2.501 vs scipy 2.500; var 6.24 vs 6.25 | ✓ |
| σ² full-conditional shape | a₀+(n+1)/2 | powers of σ²: −n/2 −1/2 −(a₀+1) ⇒ IG shape a₀+(n+1)/2 | ✓ |
| σ² full-conditional rate | b₀+½Σ(yᵢ−μ)²+κ₀/2(μ−μ₀)² | collected from lik×p(μ\|σ²)×p(σ²); coupling term present | ✓ |
| μ full-conditional | N((κ₀μ₀+nȳ)/(κ₀+n), σ²/(κ₀+n)) | standard NIG conditional | ✓ |
| Exact marginals vs M05 | t_{2aₙ}(mₙ,√(bₙ/(aₙκₙ))), IG(aₙ,bₙ) | matches M05 `nig_post` exactly (kn=41,an=21,bn=69.72) | ✓ |
| Gibbs=MH accept 1 | α=1 | factor cancellation reproduced; prints 1.0000000000 | ✓ |
| lag-1 = ρ² | E[X_{t+1}\|X_t]=ρ²X_t, Var=1 | ρ·ρ chaining correct for stored X-chain | ✓ |
| ESS/M = (1−ρ²)/(1+ρ²) | "theory" | exact for a true Gaussian AR(1) (which this chain is): 0.81→0.1050, 0.9801→0.0100 | ✓ |
| Albert–Chib rtruncnorm | inverse-CDF both signs | y=1: m+Φ⁻¹(Φ(−m)+u(1−Φ(−m))); y=0: m+Φ⁻¹(u·Φ(−m)) — both derived correct | ✓ |
| MAR complete-case bias | −0.3959 | ρ·E[Y₁\|Y₁≤0.3] = 0.7·(−0.617) = −0.432 (finite-n −0.3959; missing frac 0.367 vs P=0.382) — direction/magnitude sensible | ✓ |
| Rao–Blackwell fairness | 58.8× | raw & RB computed from the SAME trajectory per chain; both unbiased for E[σ²\|y]; ratio = var(raw)/var(RB) | ✓ (fair) |

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | §11.3 (L207) & §11.5 (L348) | "each within about one posterior sd of the truth." Actually β₀ in §11.3 is 0.1743/0.0973 ≈ **1.8 sd** off; §11.5 β₀ ≈ 1.4 sd, β₂ ≈ 1.2 sd. The other coefficients are ~1 sd. The claim is a mild overstatement (truth need not sit within 1 sd of a posterior mean, so nothing is *wrong*, but the stated bound is loose). | Soften to "each within about one-to-two posterior sd of the truth" or drop the "one sd" quantifier; the OLS-agreement audit is the load-bearing check, not proximity to truth. |
| 3 | §11.4 (L292) | Single-site ESS/M at ρ=0.99 is quoted as both `0.0101` (from `essfrac[0.99]`) and `0.0111` (from the re-drawn `xs99` in the blocking block). They are two independent MC estimates of the same quantity drawn from different rng states; a careful reader may read them as inconsistent. | Add a half-clause: "single-site ESS/M ≈ `0.0111` (an independent re-estimate of the ρ=0.99 value above, MC-noisy)…"; or reuse the same `xs99`/ESS for both prints. |
| 3 | §11.2 (L126–129, L153) | KS test is run on ~18 000 **autocorrelated** Gibbs draws; the KS null is calibrated for iid samples, so the p-values are not rigorously valid for MCMC output. Here it is benign because this sampler mixes near-perfectly (Ex 11.2 shows lag-1 ≈ 0.0015, so ESS ≈ M), and the reference CDFs are fully specified (not estimated), avoiding the Lilliefors issue. | One footnote: "KS p-values assume independence; valid here only because this chain is essentially uncorrelated (Ex 11.2) — do not read KS p-values off a slowly-mixing chain." Prevents a reader from importing the audit onto a §11.4-style chain. |
| 3 | Ex 11.4 Reconcile (L543) | "a prior-tethered random walk that wanders to wherever the seed sends it." The recursion is a *stationary* AR(1) contracting to the prior mean 0 (operator eigenvalues λ/(λ+1/τ²)<1), not a divergent random walk. The core claim (output independent of the data) is correct and is the point. | Change "random walk that wanders" → "prior-tethered AR(1) that settles around the prior mean, carrying no information from y." |
| 3 | §11.2 (L78, L153, L466) | "correctness proof built into the module" / "the sampler's unit test." The agreement audit is an **Empirical** check (overlay + KS), not a proof. STYLE §6 asks for honest Theorem/Empirical labels. | Reword to "empirical correctness audit" / "the sampler's unit test (empirical)". Cosmetic. |

## Spec-compliance checklist (SYLLABUS "11-gibbs-augmentation", binding)

- [x] **1.** Gibbs = componentwise MH with acceptance 1 — derived (α=1 cancellation) + numerically verified (`1.0000000000`).
- [x] **2.** Normal(μ,σ²) both unknown: both full conditionals derived (coupling term retained); agreement audit **foregrounded** with overlay figure + KS check vs M05's exact NIG. Parameterization matches M05 `nig_post` byte-for-byte (same kn/mn/an/bn formulas; scipy `invgamma(a=an, scale=bn)`, `t(df=2an, loc=mn, scale=√(bn/(an·kn)))`).
- [x] **3.** Bayesian linear regression by Gibbs (β\|σ², σ²\|β), recovery + OLS cross-check to 3 decimals.
- [x] **4.** ρ-sweep, predict-first; lag-1 = ρ² exactly (0.8117@.9, 0.9801@.99); ESS fraction ≈ (1−ρ²)/(1+ρ²) ≈ 0.01@.99; zigzag figure; blocked-Gibbs ESS ratio printed (89.7×); HMC motivated.
- [x] **5.** Albert–Chib probit: truncated-normal latents, derivation + sampler + recovery; Pólya–Gamma mentioned for logistic.
- [x] **6.** Missing-data/MI section: missingness as latents, impute-within-Gibbs, MAR bias removed, MI = repeated posterior completions, MCAR/MAR/MNAR ignorability, PO-as-missing promised for M24.
- [x] **7.** Rao-Blackwellization: conditional mean vs raw draw, variance drop printed (58.8×), booklet ch. 11 tie.
- [x] **8.** Bridge: augmentation = EM's E-step (M13) + VAE latent code (M25) + mixtures (M19).
- [x] Sources: C-B §4.4 cited; booklet ch. 10/11/13 — **verified in source**: ch10-gibbs-sampler.md §10.3 = Rao-Blackwell; ch11-metropolis-hastings.md §11.6 = Rao-Blackwell + L252 Albert–Chib augmentation scratch notes; ch13 = latent/mixture. The "ch. 11 (data augmentation, Rao-Blackwell)" attribution is accurate despite the file's MH title (chapter covers both); ch10.3 is the more canonical Gibbs-RB source and is also cited.
- [x] Deps 05, 10 — both real callbacks (M05 NIG/Gaussian conditioning; M10 MH acceptance ratio).

## Other checks

- **Notation (STYLE §3):** N(·,·)=variance throughout; IG scipy `invgamma(a,scale=b)` and Gamma rate/scale trap both commented inline. Compliant.
- **Numbers contract (STYLE §4.3), ≥6 spot-checks — all pass:** `1.0000000000`, `4.7184/3.4862`, KS `0.688/0.175`, β `2.1743/-1.5846/0.8982` & OLS `2.1749/…`, lag-1 `0.8117/0.9801`, ESS/M `0.1014/0.0101`, blocked `89.7`, probit `0.4524/1.1937/-0.8533`, MAR `-0.3959/0.0149`, RB `0.01509/0.00197/58.8`, Ex11.1 `0.9057/1585`, Ex11.3 `1.3281/0.7093`, Ex11.4 `-0.844/0.77/-0.997`. Every quoted value is printed at matching precision.
- **SPINE-INDEX consistency:** spine (lag-1 = ρ²), M05 promise ("Gibbs audit vs NIG"), and forward pointers (M12 HMC, M13 EM, M19 mixtures, M24 potential outcomes, M25 VAE) all align.
- **Determinism:** two-run byte-identical, PASS in 51.4 s (double run), zero warnings — clean despite the noted safety-classifier gap during authoring; nothing unsafe or fabricated found.

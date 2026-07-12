# Math review — modules/20-gaussian-processes.md

Referee: mathematical-statistics verification. Verdict: **APPROVE** (2 sev-3 nits, 0 sev-1, 0 sev-2).

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | §20.3 Reconcile, line 246 | `1.02e-06` noiseless training-point variance is described as "it equals the jitter". It does not: the jitter is `1e-8`; the value is dominated by the assumed noise `σ_n²=1e-6`. Verified: with jitter set to 0 the variance is `1.000e-06`; with `σ_n²=0, jitter=1e-8` it is `2e-8`. The `1.02e-06` = `σ_n²` (1e-6) + a small jitter contribution. | Replace "(it equals the jitter)" with "(it equals the assumed noise floor `σ_n²=10⁻⁶`)". |
| 3 | header, line 7 | **Runtime.** `~8 s`, but the harness measures `PASS in 13.7s`. STYLE §2 requires the *measured* runtime. | Update to `~14 s` (or re-measure and quote). |

## Required checklist

- [x] **Determinism / harness.** `python tools/run_module.py modules/20-gaussian-processes.md --check-determinism` → `PASS in 13.7s`, exit 0, zero warnings, 6 figures referenced, 4323 prose words, 14 blocks. Byte-identical across runs (gate passes).
- [x] **Spec beats (8/8 present).** (1) two-routes identity + ∞-limit to RBF §20.1; (2) kernel gallery RBF/Matérn-3/2/periodic/linear §20.2; (3) exact GP posterior ~20 lines, M05 `gaussian_condition` callback §20.3; (4) ML-II fit+complexity, M17 Occam callback + overfit foil §20.4; (5) GP mean = KRR machine-precision §20.5; (6) BayesOpt EI ~8 evals, M23 bridge, one fig §20.6; (7) NNGP width 1/10/1000, one fig §20.7; (8) O(n³) honesty + inducing-points + BART §20.8. Jitter idiom `1e-8 I` present and used in every Cholesky/conditioning block (Pitfalls documents it).
- [x] **Deviation ruling — flop-scaling `(n/100)³` instead of wall-clock timings: SOUND.** Wall-clock timings are non-deterministic and would break the byte-identical determinism gate (STYLE §8.2). Printing the analytic O(n³) flop ratio is deterministic, makes the same pedagogical point, and is honestly labeled ("relative cost (n/100)^3"), not presented as a measurement. Correct call.
- [x] **Notation §3.** N(μ,σ²) second-arg-variance respected (σ_n², σ_w², η²); p(·)/P(·) fine; every symbol defined at first use.
- [x] **Citations.** Rasmussen–Williams by concept, ISLP ch.7, booklet ch.14 — all appropriate. Neal (1996) correctly attributed for infinite-width→GP; Snelson–Ghahramani FITC and Titsias SVGP correctly named; BART correctly described. No fabricated page numbers.
- [x] **SPINE-INDEX consistency.** M05 established `gaussian_condition` "toolkit powering M14/M20/M21" — body copied verbatim (confirmed against modules/05 lines 415–421). M14 promises "GP = ∞-basis limit (M20)" — delivered. M17 promises "GP marginal-likelihood Occam (M20)" and its evidence=fit+complexity spine — delivered §20.4. M25/M23 forward-pointers consistent.

## Recomputation list (all independently reproduced)

1. **∞-limit ℓ=√2·h — CORRECT.** Convolution ∫exp(−(x−c)²/2h²)exp(−(x′−c)²/2h²)dc = h√π·exp(−(x−x′)²/4h²) (numeric quad vs analytic diff `8.3e-17`). Matching −(x−x′)²/4h² to RBF −(x−x′)²/2ℓ² gives ℓ²=2h² ⇒ **ℓ=√2·h**. With h=0.4: ℓ=`0.5657`, η²=A·h√π=`0.7090` — matches printed. Convergence `5.432e-01`(M=10)→`8.087e-08`(M=40)→`1.110e-16`(M=160) reproduced exactly.
2. **Two-routes identity — CORRECT and real.** Weight-space vs kernel-form: max|mean diff| = `1.14e-14`, max|var diff| = `9.16e-15` reproduced to the digit. Variance einsum `Kss_diag − ks'Ky⁻¹ks` verified.
3. **GP posterior via `gaussian_condition` — CORRECT.** Joint cov blocks right: noise `σ_n²I` added to the training (y) block only (`Sig[nte:,nte:] += sn2`), cross-block `K_{*n}` noiseless, `K_{**}` prior. Zero-mean form μ₁|₂=Σ₁₂Σ₂₂⁻¹x₂ valid since joint mean 0.
4. **Matérn-3/2** (1+√3r/ℓ)e^(−√3r/ℓ) and **periodic** η²exp(−2sin²(πr/p)/ℓ²) — both match standard MacKay/R&W forms; the classic sin² slip is absent (argument πr/p, period p). PSD: min eig periodic `1e-8`(=jitter), Matérn `1.07e-3` — no negative-eigenvalue hazard in gallery params; linear kernel PSD (outer product + const).
5. **ML-II decomposition — CORRECT, signs coherent.** log-ev = −½yᵀK⁻¹y − ½log|K_y| − (n/2)log2π. Reproduced: ℓ=0.05 → `-32.637 = -12.412 + 2.748` (+const `-22.97`); ℓ=1.581 → `-6.573 = -13.392 + 29.792`; ℓ=2.5 → `-15.778 = -24.903 + 32.099`. Direction is right: tiny-ℓ has the **best** data-fit (`-12.412`, least negative) but the **worst** complexity term (`2.748`, most penalizing — smaller ℓ ⇒ larger |K_y| ⇒ more negative −½log|K_y|); the −(n/2)log2π constant reconciles each row. Overfit ℓ is punished as claimed.
6. **GP mean = KRR — CORRECT.** λ=σ_n²=0.1 used for both `KernelRidge(alpha=0.1)` and `gp_posterior(...,0.1)`; `(K+λI)⁻¹y` identical estimator; max|diff| `8.02e-09`.
7. **EI acquisition — CORRECT (minimization).** EI = (f_best−μ−ξ)Φ(z) + σφ(z), z=(f_best−μ−ξ)/σ — standard improvement-below-best form, consistent with prose E[max(f_best−f,0)]. BayesOpt reaches true min `-6.0207` at `0.7575` in 8 evals.
8. **NNGP — CORRECT.** Nonlinearity is **tanh**; output weights scaled Var(v_j)=σ_v²/H (CLT normalization). Excess kurtosis `1.179→0.247→0.107` → 0 = marginals Gaussianize (correct semantics). Covariance invariance: corr `0.835→0.842` converges (not drifts) while sd stays `0.720→0.722` — the fixed-limit NNGP-kernel claim is the right invariance.
9. **Exercise 20.3 — CORRECT.** Single-point RBF posterior sd = √(1−e^(−d²)) at d lengthscales (corr=e^(−d²/2)): `0.7951, 0.9908, 0.9999, 1.0000` reproduced; super-exponential decay claim right.

## Numbers-contract spot-check (≥6, all pass)

`1.14e-14`, `9.16e-15`, `0.5657`, `0.7090`, `5.432e-01/8.087e-08/1.110e-16`, `1.581/-6.573`, `-12.412/2.748/-32.637`, `8.02e-09`, `-6.0207/0.7575`, `1.179/0.107/0.842`, `512.0×`, `0.0000/0.6010`, `0.0480/0.2888`, Ex-20.3 `0.7951/0.9908`, Ex-20.4 `0.832/0.842/0.185/0.118` — all match printed output.

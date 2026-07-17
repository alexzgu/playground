# P3-precision-thread — second referee (fabrication-sweep certification)

**Verdict: CERTIFIED-CLEAN.** The sev-1 fabricated wall is repaired, the sev-2 clause is added and correct, and all four drifted citations are re-synced. Independent re-derivation of every cross-file claim finds **0 fabrications remaining**.

Triggered because referee-1 found a sev-1 (an invented "module-16 SE-averaging bug"). This is a focused re-verification, not a full re-review.

## 1. Harness / determinism
`python tools/run_module.py prereqs/P3-precision-thread.md --check-determinism` → **PASS in 4.1s**, 12 runnable blocks, **zero warnings**, determinism clean, 2792 prose words, 1 figure, pure numpy/scipy. ✓

## 2. Fabrication sweep — 28 cross-file claims checked, 28 verified (0 fabrications)

Every cite was opened at its stated `module:line`; text/concept verbatim-real unless noted.

| # | anchor | claim | status |
|---|---|---|---|
| 1 | `05:101` | `prec_post = 1.0/tau2 + n/sigma2  # precisions add` | ✓ exact (incl. spacing) |
| 2 | `05:175` | Normal-Normal canonical precision/pw-mean formula | ✓ exact |
| 3 | `04:164` | Fisher info def, I(0.3)=4.7619 | ✓ (def at 164; I=1/(θ(1−θ)) at 165) |
| 4 | `04:185` | `obs_info = n/(thhat*(1-thhat))  # −ℓ''(θ̂)=n·I(θ̂)` = 190.48 | ✓ exact |
| 5 | `08:80` | Cramér–Rao bound 1/(nI), SE=1/√I | ✓ |
| 6 | `08:83` | `crlb = sig2/n_cr  # 1/(nI)` | ✓ exact |
| 7 | `08` (BvM) | Bernstein–von Mises 1/√(nI) posterior width | ✓ (§08.4 at 182+) |
| 8 | `12:411` | HMC stability cliff ε<2/ω, ω²=1/σ² | ✓ exact |
| 9 | `13:127` | Laplace Σ=(−∇²log p)⁻¹ / unconstrained-scale | ✓ (def 123, logit/Jacobian 127; both cites land in section) |
| 10 | `14:102` | `X.T@X/sigma2 + eye(p)/tau2` — precisions add (matrix) | ✓ exact |
| 11 | `16:55` | pitfall "module 16 does this right at 16:55" (`prec=1/s8**2`) | ✓ |
| 12 | `16:56` | `mu_cp` precision-weighted mean | ✓ |
| 13 | `16:57` | `se_cp = np.sqrt(1.0 / np.sum(prec))` | ✓ exact |
| 14 | `16:212` | second-level shrinkage weight `w=(1/s8**2)/(...)` | ✓ exact |
| 15 | `21:22` | "Precisions add: 1/P_t = 1/P⁻_t + 1/r" | ✓ (label 21, formula 22) |
| 16 | `23:61` | ridge/weight-decay precision-form posterior cov | ✓ |
| 17 | `23:231` | `m = cs/prec` posterior mean, precisions add | ✓ |
| 18 | `23:379` | `(1-p_slab)*m0 + p_slab*m1` spike-and-slab blend | ✓ exact |
| 19 | `25:66` | `lam = s2/tau2` (λ=σ²/τ²) | ✓ exact |
| 20 | `25:68` | `map_closed = y.sum()/(len(y)+lam)` shrinkage | ✓ |
| 21 | `EXAM:282` | `mn=(k0*m0+n4*ybar4)/kn` pw-mean (NIG) | ✓ |
| 22 | `EXAM:620` | `cj_var = 1/(1/prior_var+1/r9)  # precisions add` | ✓ exact |
| 23 | `EXAM:681` | `post_var = 1/(1/s0**2+1/se**2)` precisions add | ✓ exact |
| 24 | canon | I(0.3)=4.7619 | ✓ SPINE-INDEX:34 |
| 25 | canon | θ_A: 28→8.23 | ✓ 16:120, SPINE-INDEX:106 |
| 26 | canon | population mean μ=6.49 | ✓ 16:62/120 |
| 27 | canon | τ median = 2.80 | ✓ SPINE-INDEX:106 |
| 28 | self | 7.2143 = plug-in shrink at (μ,τ)=(6.49,2.80) | ✓ re-derived (wj=0.03367 → 7.2143) |

**Referee-1's sev-1 is gone.** The P3.1 wall now reads "Module 16 pools eight schools the same correct way, adding precisions before taking the root," citing the *real* correct line 57 — no invented bug. The pitfall bullet likewise cites `16:55` as the code that does it *right*. Confirmed against 16:55–57: `prec=1/s8**2; mu_cp=Σ(y·prec)/Σprec; se_cp=√(1/Σprec)` — precisions genuinely added.

**Referee-1's four drifted cites are re-synced:** `05:101` (was 103), `04:185` (was 186), `EXAM:282` (was 283), `EXAM:681` (was 682) — all now land exactly on the anchor line.

## 3. Recast 16:55/57 wall — accurate
Module 16 pools by adding precisions (verified above). The printed contrast is arithmetically right: instrument variances 4 and 1 (SEs 2 and 1). Averaging SEs → (2+1)/2 = **1.5000** (the wrong shortcut). Correct combined SE = √(1/(1/4+1/1)) = √0.8 = **0.8944** = 2/√5. Code (`se_avg_wrong=(√vA+√vB)/2`, `√var_combined`) matches the prose exactly. Simulation confirms (0.8007). ✓

## 4. 7.2143-vs-8.23 clause — technically correct
7.2143 is the plug-in shrink at point (μ,τ)=(6.49, 2.80); re-derived independently. 8.23 is module 16's canonical school-A posterior mean (16:120, SPINE-INDEX:106), which marginalizes the τ-posterior (right-tailed, half-Cauchy). Because the shrinkage weight w(τ)=(1/σ²)/(1/σ²+1/τ²) is nonlinear in τ, E_τ[shrink(τ)] ≠ shrink(median τ), so the two quantities legitimately differ (marginalizing gives *less* shrinkage → 8.23 > 7.21). **"Jensen" is an acceptable name** for this E[f]≠f(E) gap — it is the course's standing shorthand for the plug-in-vs-marginal gap (used the same way for predictive-vs-plug-in variance). Minor pedantic note (not a defect): the full posterior marginalizes μ *and* τ, but μ enters shrinkage linearly and contributes no gap, so attributing the difference to τ-nonlinearity is mechanistically correct.

## 5. Set-piece headline prints — correct
- Six-costumes: `all six reduce to the one master formula: True`; each native = pw_mean to ≤8.9e-16. ✓
- Marquee: all three routes print `0.190476` (=1/5.25, with post_prec=1/4+10/2=5.25); `max|diff|=5.08e-11`; Laplace (d) also 0.190476. ✓

## Findings
None. No sev-1/2/3. The two substantive revisions (recast wall, plug-in-vs-marginal clause) are both accurate and strengthen the module; the citation re-sync is complete.

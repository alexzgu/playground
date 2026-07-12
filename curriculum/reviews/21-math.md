# 21-state-space — Mathematical referee review

**Verdict: APPROVE** (0 sev-1, 1 sev-2, 2 sev-3). Harness PASS, determinism clean, all numbers reproduce, all "verbatim" helpers match source, all byte-identity mappings are the genuine KF update.

## Harness / determinism
- `python tools/run_module.py modules/21-state-space.md --check-determinism` → **PASS in 14.9–22.2s**, 11 blocks, 5 figs, 4002 prose words. **Zero WARNING lines** (numbers-contract grep clean; `out1 == out2` byte-identical second run). Well under runtime cap.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 2 | §21.5 opening ("Break either… no closed form… The fallback is module 09's Monte Carlo") | Jumps straight from linear-Gaussian to particles, skipping the **EKF/UKF** family — the linearization / sigma-point filters that keep an *approximate* Gaussian recursion and are what practitioners reach for **first** under mild nonlinearity. Violates BRIEF #6 ("what practitioners actually do"). Module's own "what breaks, when" framing invites the omission. (EnKF is named once in Ex 21.3 but EKF/UKF appear nowhere.) | Add one sentence: for *mild* nonlinearity the EKF (linearize F,H about the mean) or UKF (unscented sigma-points) keep the Gaussian recursion cheap; go to particles when nonlinearity is strong or the posterior is multimodal (where a single Gaussian is hopeless). Not a required beat, so non-blocking. |
| 3 | §21.2 (display eq. + code, F/H/Q/R) | Matrices **Q, R never verbally defined at first use** (STYLE §3). Only scalars q,r are defined (§21.1 model eqs). Reader infers Q,R are the matrix analogues from context. | One clause after "the observation map to a matrix H": "…process-noise covariance Q and observation-noise covariance R (the matrix analogues of q, r)." |
| 3 | Ex 21.1 Reconcile | Internal tension: observed factor is **2.7** (0.3904→0.1461) but text asserts "discount it by √10≈3.2×". At r=2 the gain 0.39 is not deep in the small-gain regime, so the √-law asymptote (3.2) legitimately differs from the finite-value factor (2.7); the prose blurs the two. | Clarify the √(q/r) law is the *asymptotic small-gain* limit; at these finite values the factor is ~2.7, which need not equal √10. Or soften "√10≈3.2×" to "up to √10 asymptotically." |

## Required checklist (5 spec beats — all present)
- [x] **Beat 1** "Nothing new" reveal: 1-D KF derived as marginalize/condition; gain = shrinkage weight (M05 + M16 callbacks explicit); 2-D const-velocity tracking with tilted 2σ ellipses. §21.1–2.
- [x] **Beat 2** AR(p)=conjugate lag regression: Bayesian AR(2) via `nig_regression` verbatim; stationarity-of-**posterior-draws** check (not point estimate). §21.3.
- [x] **Beat 3** OU exact AR(1) discretization (Lawler by concept); filter noisy obs; state-vs-parameter inference explicitly distinguished (boxed). §21.4.
- [x] **Beat 4** Bootstrap PF on SV-lite (~60 lines), predict-first "ESS after 50 steps"; ESS-collapse (M09 `ess_kong` reused); resampling fix; one-step-ahead predictive coverage. §21.5.
- [x] **Beat 5** RTS smoothing paragraph (with backward gain eqs); SMC-samplers/tempering pointer to M18/M19. §21.5 + Bridge.
- [x] Notation §3 respected (variance-second N(·,·); IG rate/scale via `rng.gamma(an,1/bn)`); STYLE §5 predict-then-run on all 4 exercises + 2 marquee demos; 21.3 surprising, 21.4 ML-bridge.
- [x] SPINE-INDEX consistency: shrinkage formula (line 38), `ess_kong` (line 63), `nig_regression` (line 93), `gaussian_condition` (line 39) — all cited correctly and code matches source byte-for-byte.

## Independent recomputation list (all confirmed)
- **KF update = Normal-Normal** — prior N(2,3), y=5, r=1: precisions 1/3+1=4/3 → P=0.75, m=(2/3+5)/(4/3)=4.25, K=3/4=**0.75**. `normal_known_var_update(m_pred,P_pred,r,[y])` maps (prior mean, prior var, obs var, datum) = (2,3,1,5) — this **is** the KF update, not a lookalike. Agreement **8.9e-16** ✓ (machine ε, correct).
- **`gaussian_condition` byte-identity** — Cov(x,y)=P⁻Hᵀ, cond_mean=m⁻+K(y−Hm⁻) with K=P⁻HᵀS⁻¹, cond_cov=(I−KH)P⁻. Genuine KF update. **1.8e-15** ✓.
- **Steady-state Riccati** q=0.5,r=2: P²+qP−rq=0 → P=(−0.5+√4.25)/2=**0.78078**, K=Pₘ/(Pₘ+r)=1.2808/3.2808=**0.39039** ✓ (matches 0.7808/0.3904).
- **4-D CV model** — Qax=[[dt³/3,dt²/2],[dt²/2,dt]]·qa is a proper **CWNA discretized-acceleration** covariance (not a diagonal hack), correctly block-placed on (p_x,v_x) and (p_y,v_y). F rows integrate v into p. ✓ honest.
- **OU exact discretization** — z=x−μ, dz=−θz dt+σdW → z_{t+Δ}=e^{−θΔ}z_t+∫₀^Δ e^{−θ(Δ−s)}σ dW_s; Var=σ²/(2θ)(1−e^{−2θΔ}). θ=0.7,Δ=0.25: a=e^{−0.175}=**0.83946**, s2=0.25/1.4·(1−e^{−0.35})=**0.05273**, statvar=**0.17857**=s2/(1−a²) ✓.
- **AR(2) stationarity triangle** {φ₁+φ₂<1, φ₂−φ₁<1, |φ₂|<1} — standard, correct. Posterior df 2aₙ=2(1+298/2)=**300** ✓ (n=298 lag rows).
- **Prediction-error decomposition** — log p(y_{1:n})=Σ log N(y_t; m⁻_t, S_t), S_t=P⁻_t+r; correct marginal likelihood via one-step predictives. Grid MLE θ̂=**0.749** ✓.
- **Particle filter** — bootstrap (transition-prior) proposal, resample at ESS<N/2; `ess_kong=(Σw)²/Σw²` scale-invariant so normalized weights give correct value. ESS 877.7→43.7→1.48 = M09 fraction-collapse restated on a 100-dim path. ✓. Coverage 0.96 formed from pre-conditioning predictive draws (honest one-step-ahead). ✓.
- **RTS gain** C_t=P_t Fᵀ(P⁻_{t+1})⁻¹, m^s_t=m_t+C_t(m^s_{t+1}−m⁻_{t+1}) — standard, correct.
- **Ex 21.1** r=20: P²+0.5P−10=0 → P=2.9222, K=**0.14611** ✓. **Ex 21.4** σ_η=√(1−a²)=**0.1411** at a=0.99 ✓.

## Honesty of the "nothing new" framing
Correct and non-overclaimed **for the linear-Gaussian class**: the KF genuinely is repeated conjugate updating (verified to ε twice). The one gap is the missing EKF/UKF caveat (sev-2 above) — the claim "no closed form → particles" understates the Gaussian-approximation filters practitioners try first. Callbacks (M05 0.75 two-conversion predictive, M16 partial-pooling with q as τ², M09 ESS collapse) all point at real, verified content.

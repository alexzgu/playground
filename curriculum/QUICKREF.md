# Quick Reference — The Bayesian Spine on one page

*Every entry names the module where you ran it. Distilled from the course; canonical numbers live in [modules/SPINE-INDEX.md](modules/SPINE-INDEX.md).*

## The four lines

1. **Model** = joint distribution p(unknowns, knowns). 2. **Inference** = conditioning: p(θ | y) ∝ p(y | θ) p(θ). 3. **Prediction** = marginalization: p(ỹ | y) = ∫ p(ỹ | θ) p(θ | y) dθ. 4. **Decision** = argmin_a E_{θ|y}[L(θ, a)].

## Notation (course-wide)

N(μ, **σ²**) — second argument is the **variance** · Gamma(α, **β**) — β is the **rate** (scipy: `gamma(a=α, scale=1/β)`) · IG(α, β): `invgamma(a=α, scale=β)` · t_ν(μ, σ²) location–scale · θ unknowns, y data, x covariates (conditioned on), ỹ future, D dataset · E[·], Var[·], Cov[·,·] · KL(q‖p) = E_q[log q − log p].

## Master formulas

| Formula | Statement | Where run |
|---|---|---|
| Odds form of Bayes | posterior odds = prior odds × likelihood ratio | 02 |
| **Master shrinkage** | posterior mean = (κ/(κ+n))·prior mean + (n/(κ+n))·MLE — reappears as ridge, the Kalman gain, partial pooling | 05, 14, 16, 21 |
| Predictive decomposition | Var[ỹ] = E[Var(y\|θ)] + Var[E(y\|θ)] = aleatoric + epistemic | 05, 14 |
| MVN conditioning | μ₁\|₂ = μ₁ + Σ₁₂Σ₂₂⁻¹(x₂−μ₂); Σ₁₁\|₂ = Σ₁₁ − Σ₁₂Σ₂₂⁻¹Σ₂₁ — powers regression, GPs, Kalman | 05 → 14/20/21 |
| Loss → estimator | L2 → mean, L1 → median, 0–1 → mode; pinball(q) → q-quantile | 06 |
| Conditional coverage γ(r) | two-point uniform: γ(r) = r/(1−r) for r<½, else 1; prior-averaged coverage ∫γ·π = 1−α exactly | 06 |
| Ridge ≡ prior | Ridge(α) coefficients = posterior mean under β ~ N(0, τ²I) with α = σ²/τ², to machine precision | 00, 14 |
| James–Stein = EB | δ = (1 − (d−2)/‖X‖²)X; dominates the MLE for d ≥ 3 | 08 |
| Kong ESS | ESS = (Σw)²/Σw² = M/(1+cv²), cv² of **unnormalized** weights; the alarm is the ESS *fraction* collapsing | 09, 21, 24 |
| MH acceptance | α = min{1, [p(θ′)q(θ\|θ′)]/[p(θ)q(θ′\|θ)]} — evidence cancels; detailed balance ⇒ stationarity | 10 |
| Gibbs correlation law | bivariate-normal Gibbs lag-1 autocorrelation = ρ² exactly; ESS/M ≈ (1−ρ²)/(1+ρ²) | 11 |
| Leapfrog stability | ε_crit = 2/ω; a divergence is local curvature exceeding 2/ε | 12 |
| **The ELBO identity** | log p(x) = ELBO(q) + KL(q ‖ p(·\|x)); mean-field variance deficit = 1−ρ² exactly | 13, 25 |
| Partial pooling | wⱼ = (1/σⱼ²)/(1/σⱼ² + 1/τ²) — the master formula one level up | 16 |
| Evidence = Occam | p(y \| model) = prior predictive; fit × complexity penalty, automatic | 17, 20 |
| Kalman gain | K = P⁻/(P⁻ + r) — the shrinkage weight on a conveyor belt | 21 |
| Action threshold | act when p > C_FP/(C_FP + C_FN) — 0.5 only under symmetric costs | 22 |
| Assurance | ∫ power(θ) π(θ) dθ — the number you can act on before the study | 23 |
| Power posterior | p_η ∝ p(y\|θ)^η π(θ); variance × 1/η (exact for flat priors) — honest widening under misspecification | 18 |

## Constants worth memorizing

RW-Metropolis optimal acceptance **0.234** (d→∞ product targets; ~0.44 in 1-D), step ≈ 2.38/√d · HMC optimal acceptance **0.651** · typical set of N(0, I_d): ‖θ‖ concentrates at **√d** (the mode holds nothing) · CRP tables: E[Kₙ] = α[ψ(α+n)−ψ(α)] (α·log n errs in an α-dependent direction).

## Ten judgment rules (each backed by a demo you ran)

1. **Plug-in prediction is most overconfident exactly when you have least data** — 2-of-2 → 0.75, not 1.0 (05); the plug-in bettor lost $13k (00).
2. **Same data, same posterior — p-values can still disagree** — 0.073 vs 0.033 on identical likelihoods (04). Design matters *before* data (23), not after.
3. **Shrinkage is a free lunch in d ≥ 3** — and the frequentist proof of it is an empirical-Bayes posterior mean (08). Never trust the top-k raw estimates: winner's curse (18).
4. **Report ESS, not draw count — and watch the weights, not the estimate** — a passing single-run ESS coexists with a 44%-wrong answer (09); an IPW point estimate "looks fine" at ESS 16% (24).
5. **Geometry is the diagnosis** — divergences mean the model's shape, not the sampler's mood: funnel → non-center (12, 16); acceptance rate is not mixing (19).
6. **A model must predict its own data** — PPC before you compare; the evidence picks degree 3 while training error keeps falling (17); p = 0.049 replicates like a coin flip (17).
7. **The posterior is exactly right about a wrong model** — audit width with the sandwich; temper if needed (18). Calibration is a property of model *plus reporting process*, not paradigm (23).
8. **Conditioning beats unconditional guarantees when you know more** — the "50%" interval you *know* is right (06); condition on ancillaries.
9. **Adjustment sets come from graphs, not greed** — controlling for a collider manufactures bias (24); identification is untestable from the joint alone.
10. **A posterior is not a deliverable; an action is** — thresholds from losses (22), information priced before purchase (EVSI/EIG, 22–23), and Thompson sampling is five lines (22).

## Decision guide (from the capstone)

| Problem | Reach for | Audit with |
|---|---|---|
| Small-n estimation, real prior knowledge | Conjugate/hierarchical posterior (05, 16) | Prior-predictive check (07), sensitivity fan (07) |
| A/B or ship decision | Posterior expected loss + EVSI (05, 22) | Optional-stopping calibration is safe; *selective reporting* is not (23) |
| Many parallel effects | Hierarchical shrinkage / EB at scale (16, 18) | FDR at matched threshold (18); winner's-curse check |
| Black-box uncertainty | Ensembles + temperature scaling (25) | Reliability/ECE (15); conformal for model-free marginal coverage (26) |
| Causal question | Identification first: DAG + backdoor (24) | Overlap/ESS on weights (24); sensitivity to unmeasured confounding |
| Model choice, M-closed | Evidence/Bayes factors with **proper priors** (17) | BF prior-sensitivity table (17); Lindley awareness |
| Model choice, M-open | PSIS-LOO / stacking (17, 18) | PPC on the winner (17) |

## Environment traps (this repo)

Pass observations to NumPyro as **numpy**, not jnp; wrap obs sites in `numpyro.plate` for `Predictive`; ArviZ 1.x: `plot_*` returns a `PlotCollection` (use `.savefig`), `az.waic` is gone (hand-compute), cast log-likelihood to numpy before `az.loo`; scipy `nbinom(r, p)` — p is the *other* outcome's probability (θ=0.5 hides the bug); `rng.gamma(shape, scale)` takes **scale** = 1/rate. All smoke-tested in [tools/ppl_idioms.py](tools/ppl_idioms.py).

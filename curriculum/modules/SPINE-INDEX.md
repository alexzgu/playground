# SPINE-INDEX — shipped modules at a glance

Maintained by the orchestrator after each wave. Wave N+1 authors MUST read this file plus every module their spec calls back to. Format: spine / established helpers & notation / key printed numbers / forward promises.

*Status: Waves 1–3 (00–13) FINAL — every module authored, dual-refereed, revised, harness-green. All numbers canonical.*

## 00-four-lines
- **Spine:** the whole subject is four lines (model = joint, inference = conditioning, prediction = marginalization, decision = expected loss); every procedure is a special case, approximation, or audit.
- **Established:** the standard setup-block pattern (SLUG/FIG/SEED/rng/save); the course notation table (N(μ,σ²) = VARIANCE, Gamma(α,β) = RATE — never re-litigate); harness usage documented for readers.
- **Key numbers:** ridge ≡ posterior-mean `max|diff| = 4.5e-15`; medical PPV `0.0194` (odds 0.0010 × LR 19.8), after second positive `0.2818`; decision losses treat 9.806 / no-treat 19.435 / retest 5.6846 → retest wins (staged as rank-the-actions catch); coin Beta(1,1)+7H3T → Beta(8,4), mean `0.6667` vs MLE 0.7; plug-in bettor `−0.0132`/bet at price 0.68, total `$−13,235` over 10⁶ $1 bets (predictive bettor declines).
- **Promises:** M02 enumeration engine + sequential=batch; M05 conjugacy & rule of succession; M06 MAP=penalized-MLE; M07 priors; M21 Kalman; M22 EVSI; M25 weight decay; which-line table built out by M08/M17/M26.

## 01-probability-as-logic
- **Spine:** exchangeability, not philosophy, makes parameters exist — an exchangeable sequence's running frequency converges to a *random* limit Θ whose law is the prior.
- **Established:** exchangeability (permutation-invariant joint); de Finetti representation (Theorem, infinite exchangeability, simulated not proved); **derived lemma downstream modules may cite:** Cov[Xᵢ,Xⱼ] = Var[Θ] ≥ 0 ⇒ mixtures can't be negatively correlated; Pólya urn ≡ Beta-Binomial predictive (`polya_prob`, `betabin_pred` helpers); Dutch-book coherence (scoped to finite additivity); calibration/ECE.
- **Key numbers:** mixture pairwise corr analytic `0.2`, empirical `0.053` covariance vs analytic 0.05; without-replacement corr −1/(N−1) = `−0.1111` (N=10); Pólya ≡ Beta-Binomial to `1e-12`; rule of succession 6/7 = `0.8571`; ECE honest `0.007` vs overconfident `0.089` (`13.0`× inflation from a 1.6× confidence stretch).
- **Promises:** CRP via Pólya urn (M19); permutation test (M23); conformal-under-exchangeability (M26).

## 02-conditioning-is-inference
- **Spine:** Bayes = ratio of joints; posterior odds = prior odds × likelihood ratio; evidence adds in log-odds.
- **Established:** `condition(prior, likelihood, obs)` enumeration engine — joint table, keep observed column, renormalize; the discarded denominator = evidence p(o) (reused M17). Scales 2 → 2000 hypotheses (German tank). Log-space stabilization idiom (subtract max before exp).
- **Key numbers (post-revision, final):** PPV `0.0194` (exact 11/566), MC estimate ± printed 2·SE; two positives `0.2818`, three positives cross even odds (`0.8860`); PPV=50% at prevalence `0.048` (~1 in 21); tank (m=60, n=5): posterior mean `78.66`, MAP `60`, UMVU `71.0`; risk crossover **≈ N=1075** (UMVU wins ≤1050, Bayes ≥1100); Monty switch 0.6667 (host-knows) vs 0.5000 (host-random); prosecutor 0.5000 / 0.0909.
- **Promises:** loss→summary (M06); prior washout (M07); Stein/admissibility (M08); MCSE (M09); naive-Bayes/logistic as summed logits (M15); evidence reused (M17).

## 03-generative-stories
- **Spine:** a distribution is a compiled generative story — match families by mechanism, price mismatch in bits (KL).
- **Established (course-wide infrastructure):** entropy / cross-entropy / KL defined ONCE (bits vs nats stated); `entropy_bits`, `kl_bits` helpers; Gibbs' inequality via 2-line Jensen; `maxent_on_grid` dual solver (p ∝ exp(Σλ_k T_k)); Poisson-process ↔ Exp/Gamma/Poisson trio; heavy-tail gallery.
- **Key numbers:** Poisson-process gap KS `0.0062`; Cauchy sample-mean IQR ≈ 2 at every n (2.026/2.017/1.931 at n=10/10³/10⁵) vs median-IQR shrinking 0.6597→0.0069; coin H `1.000`/`0.469` bits, KL `0.531`/`0.737`; max-ent KL to target `1.3e-16` (Exp), `1.5e-16` (Normal); mean-only max-ent on counts = **Geometric**, KL(geom‖Poisson) `0.651`; softmax entropy 0.822→2.125→2.322 bits as T rises; CE floor = label entropy `0.802` nats.
- **Promises:** KL → ELBO (M13); CE = NLL training (M15); WAIC/elpd (M17); temperature = tempering (M18/M25); exp-family skeleton = M04.

## 04-likelihood  [SIGNATURE S3]
- **Spine:** identical data ⇒ identical likelihood ⇒ identical posterior, even when p-values differ; evidence is the likelihood, not the intention.
- **Established:** likelihood L(θ) = f(y|θ); factorization theorem (C-B §6.2); `nig_post()` helper (NIG update from (n, Σx, Σx²)); score & Fisher info I(θ) = Var[score] = E[−ℓ″], additive nI; likelihood→loss dictionary (CE/MSE/MAE = Bernoulli/Gaussian/Laplace NLL; MLE = ERM under log loss); censored observations contribute S(c); Pitman–Koopman stated correctly (support condition; Cauchy = growing-dim foil).
- **Key numbers:** binomial p = `0.073` vs neg-binomial p = `0.033` on the same 9-of-12 data; shared likelihood ∝ θ⁹(1−θ)³ (ratio 4.0 const); shared Beta(10,4) posterior, mean `0.7143`; I(0.3) = `4.7619`; censored MLE `0.5376` vs naive drop-censored `0.6452`; x̄ ⊥ residuals corr `−0.0026`.
- **Promises:** conjugacy = exp-family closure + NIG derivation (M05); ancillarity/conditionality (M06); Jeffreys ∝ √I (M07); θ̂ ~ N(θ, 1/nI) and BvM (M08); GLMs + survival (M15); stopping rules at design stage (M23).

## 05-conjugate-updating  [SIGNATURE S2]
- **Spine:** conjugate posterior = prior pseudo-data + real data; posterior mean = (κ/(κ+n))·prior + (n/(κ+n))·MLE — the master shrinkage formula (= ridge, Kalman gain, partial pooling).
- **Established:** conjugate library — `beta_binomial_update`, `normal_known_var_update`, `gamma_poisson_update`, `nig_post` (from M04), `dirichlet_mult_update`, `student_t_predictive(kn,mn,an,bn)` (df=2αₙ, loc=mₙ, scale²=bₙ(κₙ+1)/(αₙκₙ)); **`gaussian_condition(mu, Sigma, idx1, idx2, x2)`** — MVN block conditionals, the toolkit powering M14/M20/M21; law-of-total-variance decomposition (aleatoric+epistemic), strict widening claimed only for fixed-dispersion conjugate families.
- **Key numbers (final):** S2: 2-of-2 → Beta(3,1), predictive `0.7500` vs MLE 1.0; predictive-vs-plug-in var 4.69/2.34 (Beta-Binom), 3.0/2.0 (Gamma-Poisson); plug-in 90% interval covers 0.8307 (its own-model coverage `0.9525` — epistemic drop isolated from discreteness); A/B (41/1000 vs 57/1000): P(B>A) `0.9510`, regret ratio ship-A:ship-B = `81×` (vs the naive 19:1 odds read) → ship B — the course's first fully-staged line-4 decision (M22 reuses the beat); add-α trap: α=1e-4, V=10⁴ ⇒ κ=αV=1; MVN toolkit verified to machine precision via Schur complement (1.1e-16).
- **Promises:** loss→estimator (M06 ✓); washout (M07 ✓); JS/EB (M08 ✓); Gibbs audit vs NIG (M11); ridge λ↔τ² + trumpet (M14); pooling weight (M16); GP posterior (M20); Kalman (M21); EVSI (M22).

## 06-estimates-are-decisions
- **Spine:** point estimates and intervals are answers to a loss function; what you condition on determines what your guarantee means.
- **Established:** loss→estimator dictionary (L2→mean, L1→median, 0-1→mode, derived); pinball/newsvendor → predictive quantile at fractile c_u/(c_u+c_o); MAP=penalized-MLE (ridge=Gaussian=posterior mean; lasso=Laplace: **mode has exact zeros, posterior mean never sparse**); credible (post-data belief) vs confidence (procedure guarantee); two-point uniform conditional coverage Cov(θ|R=r)=r/(1−r) (r<½) else 1; **prior-averaged coverage theorem** ∫Cov·π = 1−α (Fubini); conditionality/ancillary-conditioning (M04 cashed).
- **Key numbers (final):** Gamma(2,1) mode/median/mean `1.0000`/`1.6783`/`2.0000` (E[L2] at mean = posterior variance = 2.0000 exact); newsvendor order `12` at the 0.75 predictive fractile (symmetric-cost exercise: `10`, where median = mean by NB-shape coincidence); lasso MAP `0.0000` vs Laplace posterior mean `0.1432`/`0.3945`; two-point marginal coverage `0.500`, conditional `0.111`/`0.250`/`0.429`/`1.000` at R=0.1/0.2/0.3/0.9; prior-averaged `0.9501`, pointwise `0.9715`@θ=0 / `0.8827`@θ=4, misspecified `0.8288`; two-instruments conditioning gap `7.1×`.
- **Promises:** BvM (M08 ✓); λ↔τ² + horseshoe (M14/M18); thresholds/EVSI (M22); conformal (M26).

## 07-priors
- **Spine:** the prior is part of the model (same status as the likelihood); influence decays like 1/n for identified parameters, is decisive at small n/boundary data, never washes out for unidentified ones.
- **Established:** `prior_predictive(prior_sampler, sim_data, M)` harness (samplers close over their own generator); sensitivity fan as the standard "does the prior matter?" diagnostic (fan spread 0.3000 at n=10 ≈ half the 0.6 span of the prior means); Jeffreys πJ ∝ √I(θ) = Beta(½,½) for Bernoulli, invariance verified through log-odds; "flat isn't flat"; propriety-check discipline (Haldane all-successes diverges); faces of nonidentifiability (symmetry / weak likelihood / structural); regularization = implicit prior (non-polemical).
- **Key numbers:** fan spread 0.3000 (n=10) → 0.0006 (n=10⁴); N(0.5,10²) prior puts 0.9601 outside [0,1]; Jeffreys two-route agreement ~5.6e-12; washout: sum sd 0.0100 vs θ₁ sd 2.2361 at n=10⁴.
- **Promises:** τ priors half-Cauchy/half-Normal (M16); EB λ (M14/M18); label switching (M19); overparameterized nets (M25); causal identification (M24).

## 08-frequentist-bridge  [SIGNATURE S4]
- **Spine:** the theories fuse asymptotically (BvM); where they don't, shrinkage wins — James–Stein IS an empirical-Bayes posterior mean.
- **Established:** JS risk machinery; **BvM 4-condition box** (well-specified / fixed finite-dim identifiable / interior / positive-continuous prior) + breakdown gallery (boundary, unidentified, Neyman–Scott, misspecification→M18); complete-class = risk-set lower boundary is Bayes rules; bootstrap = implicit posterior (Dirichlet(1,…,1)); coverage-audit pattern.
- **Key numbers:** d=10, θ=0: MSE MLE `9.98` vs JS `1.99` vs JS⁺ `1.25`; no dominance d≤2, crossover d=3; E[(d−2)/‖X‖²] = 1/(1+τ²) (exact, drives JS=EB); BvM TV `0.1668`→`0.0165` (n=5→500, Gamma posterior); Neyman–Scott σ̂² → σ²/2 (`0.4988`); minimax coin flat risk `0.0144`; weak-prior credible coverage `0.9499`.
- **Promises:** JS = point-mass-hyperprior EB + Neyman–Scott escape (M16); sandwich/misspecification (M18); admissibility for decisions (M22).

## 09-monte-carlo
- **Spine:** any expectation = sample average with a CLT error bar you must report (MCSE = s/√M); importance sampling fails silently — the weights are the alarm.
- **Established:** `ess_kong(w)` = (Σw)²/Σw² = M/(1+cv²) ≤ M (UNNORMALIZED weights); the tail rule (proposal tails ≥ target tails); rejection acceptance = 1/C, E[trials] = C; ABC = conditioning on a neighborhood; rare-event relative error ≈ 1/√(Mp). Booklet ch. 4 "ESS ≥ n" adjudicated a NAME-COLLISION (prior-augmented sample size n + σ²/δ², correctly derived there), not a misprint.
- **Key numbers:** E[√|Z|] quadrature `0.822179` vs MC 0.821580±0.000698; P(Z>4)=3.167e-5: naive 12/12 zero hits at M=10⁴ vs IS SE 84× smaller; t₃-target/N(0,1)-proposal: single-run ESS 34.7% "passes" while E[θ²] 1.693 vs true 3 (44% low) — the tell is the **ESS fraction collapsing** (62.65%→12.27% at M=10³→10⁶; absolute ESS rises sublinearly; healthy = flat ESS/M); ABC sd 0.1314→0.0653 (exact 0.0634) as ε→0.02; d-ball rejection 1-in-402 at d=10; OPE dominant trajectory = 18-of-20 weight ≈1,574 holding 17.5% (all-1 worst case 1.8²⁰≈127,482 never occurs, P=9.5e-7).
- **Promises:** MCMC (M10); ESS for chains (M10) and particle filters (M21 — cite the fraction-collapse form); typical set (M12); IPW = importance weights (M24); MC-dropout, neural SBI (M25).

## 10-metropolis-hastings
- **Spine:** MH samples any unnormalized target via detailed balance — only ratios matter, so the evidence cancels; diagnostics are necessary-not-sufficient — report ESS, not draw count.
- **Established:** `rw_metropolis`/`rw_metropolis_nd` (log-space accept), `acf_fft`, `ess_1d`, `ess_multichain`, `split_rhat`, `rank_normalize`; DB⇒stationarity 6-line lemma (sufficient-not-necessary; 3-cycle counterexample); ArviZ 1.x defaults = rank-normalized (az.ess bulk / az.rhat rank; both accept raw (chain,draw) arrays); spectral gap 1−λ₂, relaxation 1/(1−λ₂), ACF ~ λ₂^k.
- **Key numbers:** d=50 product target: ESS peak at acceptance `0.240`, step `0.337` = 2.38/√50 (0.234 is the d→∞ scope); 1-D optimum `0.439`; bimodal ±5 trap: 0 crossings, P(θ>0)=`0.0000`; fooling example: single-chain split-R̂ `1.0028` passes, 4-chain rank-R̂ `1.7365` / ESS `6.1` catches (plain-vs-rank matters exactly here: 5.5422 vs 1.7365); hand ESS `2304.9` vs az `2313.4`; 2-state chain λ₂=`0.800`, t_rel=`5.00`, τ_int=`9.00` exact.
- **Promises:** Gibbs = componentwise MH accept-1 (M11 ✓); HMC 0.651 + typical set (M12 ✓); tempering demo (M19); annealing bridge.

## 11-gibbs-augmentation
- **Spine:** sample one full conditional at a time; posterior correlation is the enemy; augmentation invents the latents that restore conjugacy.
- **Established:** `rinvgamma(a,b,rng)` = 1/rng.gamma(a, 1/b) (convention referee-verified vs scipy); two-block Normal(μ,σ²) + linear-regression Gibbs; `gibbs_bvn`, `autocorr_fft`, `ess_ips` (Geyer); `rtruncnorm` inverse-CDF; Albert–Chib probit augmentation; impute-within-Gibbs / MI; MCAR/MAR/MNAR ignorability taxonomy; Rao-Blackwell conditional-mean estimator; **empirical agreement-audit discipline** (KS vs conjugate truth; valid only on well-mixed chains — thin/pool otherwise).
- **Key numbers:** Gibbs↔NIG agreement KS p=0.688/0.175 (t₄₂, IG(21, 69.72)); lag-1 = ρ² EXACT (0.8117@0.9, 0.9801@0.99); ESS/M = (1−ρ²)/(1+ρ²) → ~0.010@0.99 (AR(1)-exact); blocked-Gibbs 89.7× ESS gain; MAR complete-case bias −0.3959 (predicted −0.432) vs imputed 0.0149; Rao-Blackwell 58.8× variance drop (same-trajectory comparison).
- **Promises:** ESS collapse motivates HMC (M12 ✓); augmentation = EM E-step (M13 ✓), mixture labels (M19), VAE code (M25); PO-as-missing-data (M24); Pólya-Gamma → M15.

## 12-hmc  [SIGNATURE S1]
- **Spine:** in high dimension the mass lives in a thin shell at radius ≈√d (the typical set), not at the mode; random walks die there (ESS/iter ∝ 1/d); leapfrog HMC takes long coherent gradient-momentum strides along it.
- **Established:** `leapfrog(q,p,eps,L)` + from-scratch `hmc`; `iat()` (truncated at first negative lag); energy error O(ε²); EXACT leapfrog stability threshold ε_crit = 2/ω (marginal/Jordan-defective at exactly 2); divergence = local curvature exceeding 2/ε; non-centering via LocScaleReparam = the funnel reflex (M16 will reuse); ULA/SGLD = Euler–Maruyama of overdamped Langevin, stationary var 1/(1−ε/4) (AR(1) derivation).
- **Key numbers:** N(0,I₁₀₀₀): mean‖θ‖ `31.61` = √(d−½), sd `0.71`, mass within √d/2 of mode `0.0000`, log-density gap `500` nats; RW ESS/iter ∝ d^−0.94, ~`2492` iters/indep draw at d=1000; ε cliff 2.00 stable / 2.01 explodes; funnel divergences `13`→`0`, v-reach −1.97→−10.01; HMC optimal acceptance ≈`0.651` (Beskos, d→∞ product-target scope) vs RW 0.234.
- **Promises:** non-centering + funnel (M16); SGD-noise ≈ SGLD, tempering (M25); NumPyro/ArviZ idioms established for all later PPL modules.

## 13-laplace-em-vi
- **Spine:** log p(x) = ELBO(q) + KL(q ‖ posterior) — one identity, three families: Laplace (Gaussian curvature-matched at the mode — ELBO-optimal only asymptotically), EM (point mass on θ, EXACT conditional on z), mean-field VI (factorized: means right, variances shrunk).
- **Established:** `elbo_and_kl` grid verifier; `laplace_logit` (fit on unconstrained scale + KL); Laplace evidence formula; minimal known-variance mixture EM (full GMM = M19's); `cavi_gaussian` (unequal-variance target: var_mf,j = (1−ρ²)·Σⱼⱼ exactly); CAVI-for-NIG; SVI/AutoNormal-vs-NUTS comparison pattern (AutoNormal = mean-field in unconstrained space — stated honestly); "when to trust VI" box (point predictions yes; tail risk/interval widths no).
- **Key numbers:** ELBO+KL = `−2.3979` for every q (Beta(8,4) check); Laplace KL 0.0264@n=5 vs 0.0022@n=200 (`11.8×`), evidence −4.62 both routes; EM log-lik −616.52→−411.79 monotone; CAVI var = (1−ρ²)Σⱼⱼ exact (`0.3600`/`0.7200`); CAVI/exact sd ratio = √((aₙ−1)/aₙ) = √0.8 = `0.8944` EXACT (closed form — the t's ν/(ν−2) tail inflation is what mean-field misses); SVI sd(σ) `0.700`× NUTS; reverse-KL mode collapse KL = ln 2 = `0.693`.
- **Promises:** full GMM-EM + Gibbs label uncertainty (M19); VAE = amortized ELBO (M25); evidence/Occam in full (M17).

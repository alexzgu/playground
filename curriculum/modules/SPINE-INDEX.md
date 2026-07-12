# SPINE-INDEX — shipped modules at a glance

Maintained by the orchestrator after each wave. Wave N+1 authors MUST read this file plus every module their spec calls back to. Format: spine / established helpers & notation / key printed numbers / forward promises.

*Status: Wave 1 (00–04) FINAL — authored, dual-reviewed (math + pedagogy, 10 reviews), revised, all harness-green. Numbers below are canonical.*

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

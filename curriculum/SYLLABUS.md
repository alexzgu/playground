# SYLLABUS — The Bayesian Spine (final module specs, v1)

Synthesized from OUTLINE-draft v0 + panel: `panel/proposal-ml-first.md`, `panel/proposal-theory-first.md`, `panel/critique-{rigor,pedagogy,coverage}.md`. This file is the **binding work order**: authors implement their module's spec below, under the contracts in `BRIEF.md` and `STYLE.md`. Where this file cites a number as ✓, the rigor panel machine-verified it — build on it; where it flags a correction, the corrected statement here is authoritative (the draft outline is superseded).

**The four lines** (quoted wherever they do work):
1. A model is a joint distribution p(unknowns, knowns).
2. Inference is conditioning: p(unknowns | knowns).
3. Prediction is marginalization: p(new | knowns) = ∫ p(new | unknowns) p(unknowns | knowns).
4. A decision minimizes posterior expected loss.

**Production protocol (per module).**
1. Author writes `modules/NN-slug.md` to spec; runs `python tools/run_module.py modules/NN-slug.md --check-determinism` until PASS with no warnings; keeps runtime <120 s (hard 300 s).
2. Math verifier audits derivations, honesty labels, numbers contract, and compliance with the rigor notes below.
3. Pedagogy verifier audits spine, predict-before-reveal staging, exercise quality, fluff.
4. Reviser applies findings; re-runs harness; orchestrator integrates and appends to `modules/SPINE-INDEX.md` (spine + established helpers + key numbers + forward promises). Wave N+1 authors must read SPINE-INDEX and every module they call back to.

**PPL note.** NumPyro is the course PPL (PyTensor's C backend is broken in this environment; decision recorded in PROGRESS.md). Copy API idioms **only** from `tools/ppl_idioms.py`. PyMC may appear in clearly-labeled `no-run` illustration blocks; Stan only via the booklet's read-only insert. The coverage panel's "PyMC primary" recommendation is overridden by environment — its "don't dual-implement" rationale stands: NumPyro is the single runnable PPL.

**Signature experiences** (pedagogy panel; stage each as Setup → Predict → Run → Reconcile, and mark it in the module):
S1 the donut/typical set (M12) · S2 the overconfident MLE (M05) · S3 same data, opposite verdicts (M04) · S4 Stein's paradox (M08) · S5 Occam for free (M17).

**Waves.** W1: 00–04 · W2: 05–08 · W3: 09–13 · W4: 14–18 · W5: 19–23 · W6: 24–26 → then global consistency pass.

---

## Part 0 — Orientation

### 00-four-lines — The Four-Line Course
**Spine.** The whole subject is four lines; every named procedure is a special case, approximation, or audit of them.
**Length exception.** 1,500–2,500 words (orientation module).
**Required.**
1. Opening demo: `sklearn.linear_model.Ridge(alpha=10)` on synthetic n=50, p=200 equals `(XᵀX+10I)⁻¹Xᵀy` equals the posterior mean under β ~ N(0, (σ²/10)I) — print `max|diff|` at machine precision. "You were already doing this."
2. Medical test (sens .99, spec .95, prev .001): build the joint, condition → PPV = `0.0194` ✓, then a treat/retest decision under an explicit cost matrix — all four lines in one worked example.
3. Coin demo ending in a **losing bet**: 7 heads in 10 (Beta(1,1) → Beta(8,4), mean `0.6667`); a bet priced between the plug-in MLE (0.7) and the predictive (2/3) — plug-in accepts, predictive declines; simulate replays with θ drawn from the posterior: plug-in bettor's mean profit < 0, printed. The course's visceral hook (full formalization in M05).
4. Fifteen-procedure table (MLE, ridge, lasso, CV, CI, p-value, bootstrap, Kalman, k-means, dropout, ensembles, weight decay, cross-entropy, A/B test, conformal) → "which line?" — rendered predict-then-reveal (blank column, then the answers).
5. Notation table (STYLE.md §3 verbatim), variance/rate conventions stated loudly, how to run modules.
**Sources.** Booklet ch. 1–2; C-B §1.2–1.3; ISLP §6.2.
**Deps.** None.

## Part I — Foundations re-grounded

### 01-probability-as-logic — Probability as the Logic of Uncertainty
**Spine.** Exchangeability, not philosophy, is what makes parameters exist: empirical frequency converges to a *random* limit, and that limit is θ.
**Required.**
1. Two readings of probability (long-run frequency; coherent degree of belief) — both kept, as *evaluation modes* not tribes. Dutch-book: one explicit book of bets with a guaranteed-loss payoff table (compressed to a tight box — the de Finetti simulation carries the module).
2. Calibration as frequency-matching: simulate a well-calibrated forecaster's tallies.
3. de Finetti trio: (a) draw Θ ~ Beta(2,2) then Bernoulli(Θ) — print positive pairwise correlation (not iid!), plot per-replicate running frequencies converging to *different* limits, histogram of limits = Beta(2,2); (b) finite exchangeability ≠ mixture: sampling without replacement is exchangeable with *negative* correlation — no iid mixture can do that (print the correlation); infinite exchangeability is what de Finetti needs; (c) Pólya urn ≡ Beta-Binomial predictive (print matching sequence probabilities; seeds the CRP in M19).
4. de Finetti's representation theorem stated precisely (Theorem label, cited), *simulated* not proved.
5. Permutation-null mention: under H₀ "labels don't matter," exchangeability is the whole assumption — one paragraph, demo lives in M23.
**Bridges.** C-B ch. 1 axioms as shared substrate; "random = unknown to you" bookkeeping; ML: train/test exchangeability as the quiet assumption under every benchmark.
**Sources.** Booklet ch. 1–2; C-B ch. 1.
**Deps.** 00.

### 02-conditioning-is-inference — Conditioning Is Inference
**Spine.** Bayes' rule is nothing but the ratio of joints; posterior odds = prior odds × likelihood ratio.
**Required.**
1. Enumeration engine for finite hypothesis spaces (joint table → condition) — a small reusable function; this module is the home of all needed discrete probability (counting is a trusted prerequisite; half-page pointer only).
2. Medical test full treatment, predict-first ("commit to a PPV guess"): hand computation, then 10⁷-patient simulation; PPV = `0.0194` ✓; likelihood-ratio form: posterior odds = (0.001/0.999)·(0.99/0.05).
3. German tank: observe serials, posterior under uniform prior vs UMVU `m(1+1/n)−1` ✓ (sim mean ≈ 1000.2 at N=1000); predict-first "which wins MSE?"; risk curves both estimators.
4. Sequential = batch (condition twice = condition once on both) — shown numerically.
5. Borel–Kolmogorov box: conditioning on a measure-zero event is ambiguous until you fix the limiting protocol — tie directly to Monty Hall's host-protocol dependence.
6. Monty Hall as an *exercise* (host-always-opens vs host-opens-at-random both settled by the enumeration engine — protocol changes the answer).
7. Naive-Bayes spam: forward pointer to M15 only.
**Bridges.** Log-odds accumulate additively (the ML reader's loss-sum intuition); C-B §1.3.
**Sources.** Booklet ch. 2; C-B ch. 1.
**Deps.** 00, 01.

### 03-generative-stories — Distributions Are Generative Stories
**Spine.** A distribution is a compiled generative story — pick families by matching stories, and measure story mismatch in bits (KL).
**Required.**
1. Poisson process on a timeline: construct from uniform order statistics ✓ → Exponential gaps, Gamma waits, Poisson counts, all three verified against scipy densities.
2. CLT as an emergent story + failure, predict-first: "average n Cauchy draws — what happens to the running mean?" → it *never* settles (sample mean of Cauchy is Cauchy(0,1); IQR ≈ 2 at every n ✓). Heavy-tail gallery; one-line EVT pointer (maxima have their own limit family — GEV; omitted as specialization).
3. Information section (defined ONCE for the whole course): entropy, cross-entropy, KL; KL ≥ 0 via Jensen (two-line derivation); cross-entropy = expected surprise with worked coin numbers; forward-thread: ELBO (M13), NLL training (M15), WAIC (M17).
4. Max-ent derivations: support+mean → Exponential, mean+variance → Normal (stated derivations + numerical check via constrained optimization on a grid); max-ent as "the least-committal story consistent with what you know."
5. ML bridge box: softmax = max-ent under moment constraints; "temperature" as the Lagrange multiplier.
6. Exponential-family *pointer only*: "these stories share an algebraic skeleton — next module" (machinery lives in M04; do NOT re-derive C-B ch. 3 here).
**Sources.** C-B ch. 3 (recap speed); booklet ch. 3.
**Deps.** 02.

### 04-likelihood — Likelihood: the Data's Voice  [SIGNATURE S3]
**Spine.** Identical data ⇒ identical likelihood ⇒ identical posterior — but possibly different p-values; the evidence is the likelihood, not the intention.
**Required.**
1. The likelihood function as evidence summary: plot L(θ) for three datasets of growing size; "the data's fingerprint on hypothesis space."
2. Sufficiency: factorization theorem (stated, used); Bernoulli Σx shuffle test (condition on Σx ⇒ order irrelevant, simulated); sufficiency-collision: two *different* datasets with identical (Σx, Σx²) → byte-identical Normal posteriors, printed.
3. Exponential families, compressed (learner has seen C-B ch. 3): the form, table of Normal/Bernoulli/Poisson/Gamma with natural parameters and sufficient statistics; log-partition derivatives = cumulants, ONE numerical check (Poisson mean/var 3.7 vs 3.696 ✓). Pitman–Koopman one-liner (U(0,θ) needs the max — no fixed-dim summary).
4. Fisher information: definition, E[score]=0, Var(score)=I(θ) verified by simulation for Bernoulli (I = 1/(θ(1−θ))); "curvature of the data's voice"; used in M07 (Jeffreys) and M08 (asymptotics).
5. **S3 staged**: predict-first — "two labs, same 9-successes-in-12 data; same conclusion?" → binomial P(X≥9) = `0.073` ✓ vs negative-binomial (stop at 3rd failure) P = `0.033` ✓; identical likelihood ∝ θ⁹(1−θ)³; identical Beta posterior overlay. One lab reports "significant," the other doesn't; the posterior can't tell them apart.
6. Likelihood principle stated; honest scope note: *design-stage* reasoning (what data to collect — M23) legitimately cares about stopping rules; *post-data inference* doesn't.
7. Censored-likelihood seed: one observation known only as y > c contributes S(c) = 1−F(c) to the likelihood — a 5-line demo (cashed out in M15 survival).
8. Ancillarity anchor: for N(θ,1), x̄ ⊥ (xᵢ−x̄) (Basu instance), simulated; ancillaries return in M06.
9. ML bridge box: likelihood → loss dictionary (cross-entropy = Bernoulli/categorical NLL, MSE = Gaussian NLL, MAE = Laplace NLL); MLE = ERM under log loss; formal GLM treatment deferred to M15.
**Sources.** C-B §6.2, §3.4; booklet ch. 2; Berger–Wolpert by concept.
**Deps.** 02, 03.

## Part II — Exact Bayesian inference

### 05-conjugate-updating — Conjugate Updating End-to-End  [SIGNATURE S2]
**Spine.** Every conjugate posterior reads as prior pseudo-data + real data; the posterior mean is a precision-weighted average — the master shrinkage formula.
**Required.**
1. Open: conjugacy = exponential-family closure (M04's table cashes out: prior in natural form ⇒ posterior in the same family). Why closed forms exist at all.
2. Full derivations for TWO pairs only: Beta-Binomial and Normal-Normal (known σ²). The other three as a compressed "same move, new algebra" table, each with one predictive twist: Gamma-Poisson → predictive = Negative-Binomial (overdispersion); Normal-Inverse-Gamma → predictive = Student-t with df = 2αₙ, loc = mₙ, scale² = bₙ(κₙ+1)/(αₙκₙ) ✓ (print MC vs closed form); Dirichlet-Multinomial → add-α smoothing (language-model bridge).
3. Master shrinkage formula derived: posterior mean = (prior precision·prior mean + data precision·MLE)/(total precision); "the prior is worth κ observations" (Beta: κ = a+b pseudo-trials; slide posterior mean MLE→prior as n varies).
4. **S2 staged** (use the pedagogy panel's worked exercise nearly verbatim): 2-for-2 conversions; predict P(next converts); Beta(3,1) ⇒ `0.75`, not 1.0 — plug-in certainty from two data points is an artifact; recurs as rule of succession, add-α, and M14's trumpet.
5. Predictive vs plug-in: law of total variance DECOMPOSITION (epistemic + aleatoric); claim strict widening **in these fixed-dispersion conjugate families**, not "always" (rigor correction); verified: Beta-Binomial predictive var 4.69 vs plug-in 2.34; Gamma-Poisson 3.0 vs 2.0 ✓; plug-in 90% interval under-covers on simulation (predict-first).
6. A/B test end-to-end (executes line 4): A = 41/1000, B = 57/1000, Beta(1,1) priors; P(B>A) by 10⁵ paired Beta draws; E[uplift]; expected loss of ship-B vs ship-A; the decision, printed.
7. Sequential = batch exercise (predict, then verify identity).
8. **Gaussian conditioning toolkit** (load-bearing for M14/M20/M21): MVN block formulas μ₁|₂ = μ₁+Σ₁₂Σ₂₂⁻¹(x₂−μ₂), Σ₁₁|₂ = Σ₁₁−Σ₁₂Σ₂₂⁻¹Σ₂₁ — derived once, verified numerically on a 3-d example vs brute-force conditional sampling.
9. Build the small conjugate library (reused course-wide).
**Sources.** Booklet ch. 3–5, 8; C-B §7.2.
**Deps.** 04.

### 06-estimates-are-decisions — Estimates and Intervals Are Decisions
**Spine.** Point estimates and intervals are answers to loss functions; what you condition on determines what your guarantee means.
**Required.**
1. LEAD with loss → estimator on a skewed Gamma(2,1) posterior: L2→mean 2.0, L1→median ≈1.68, 0-1→mode 1.0 ✓, each with posterior expected losses printed; derivations for all three.
2. Newsvendor: underage 3× overage ⇒ order = 0.75-quantile of the posterior *predictive*, not its mean; pinball/asymmetric loss ⇒ any quantile (quantile-regression mention).
3. MAP = penalized MLE: ridge = Gaussian-prior MAP (= posterior mean here) ✓; lasso = Laplace-prior MAP with exact zeros ✓ — with the honesty flag: the lasso point estimate is a *mode*; the Laplace-prior posterior *mean* is never sparse (0.14, 0.39 in the worked 1-d cases ✓). Forward pointer to M07 (priors formalized) and M14 (λ↔τ²).
4. Interval semantics: credible = post-data belief about θ; confidence = pre-data procedure guarantee. **Two-point uniform pathology as the centerpiece, rendered as an annotated picture** (this *is* the Welch/Berger–Wolpert example ✓; keep, per rigor + pedagogy): X₁,X₂ ~ U(θ−½, θ+½), interval [X₍₁₎, X₍₂₎]; marginal coverage exactly `0.500` ✓; **conditional on the ancillary R = |X₁−X₂|: coverage = r/(1−r) for r<½ and = 1 for r≥½** (rigor addition 2.1) — plot coverage-vs-r with the simulation overlaid; predict-first ("you saw R=0.9 — how confident are you now in this '50%' interval?").
5. Conditionality/ancillarity box (M04 callback): condition on what you actually saw; two-instruments example as an exercise.
6. Prior-averaged coverage theorem (rigor addition 2.2): under the true prior, ∫Cov(θ)π(θ)dθ = 1−α exactly — verified `0.9503`; pointwise coverage varies (0.971 at θ=0, 0.883 at θ=4); misspecified prior degrades gracefully (0.828). All three numbers printed. This is the precise sense of "Bayesian intervals are calibrated."
7. Jaynes truncated-exponential as an exercise (CI excludes values the data proves possible).
8. BvM forward pointer (M08): when credible ≈ confidence.
**Sources.** C-B §7.3.4, §9.2–9.3; booklet ch. 8.
**Deps.** 05.

### 07-priors — Priors: What They Are and Aren't
**Spine.** The prior is part of the model — same epistemic status as the likelihood (which you also chose); sometimes it matters, often it washes out, and for unidentified parameters it *never* washes out.
**Required.**
1. LEAD with the sensitivity fan (answer the ML skeptic first): 5 defensible priors × n ∈ {10, 10,000} on one problem — posteriors nearly identical at large n, materially different at small n; both fans plotted.
2. Prior predictive checks: simulate fake data from prior+likelihood *before* seeing data; catch an absurd prior (basketball FT% example: N(0.5, 10²) puts most mass outside [0,1] — print the prior-predictive tail masses). The reusable harness.
3. Flat isn't flat: U(0,1) on θ is sharply non-uniform on logit θ (transform histogram); "noninformative" is coordinate-dependent — always ask *flat in what?*
4. Jeffreys for Bernoulli derived two ways: √I(θ) ∝ θ^{−1/2}(1−θ)^{−1/2} = Beta(½,½) ✓; invariance verified by computing the same posterior through the log-odds parameterization. Scope line (rigor): multiparameter Jeffreys = √det I is *often not recommended as-is* (Jeffreys himself preferred the independence prior for N(μ,σ)); reference priors (Bernardo) pointer.
5. Improper priors — a GENUINE failure: Haldane Beta(0,0) with all-successes data ⇒ posterior ∝ θ^{n−1}(1−θ)^{−1}, divergent at 1 (show the integral); plus the hierarchical π(σ) ∝ 1/σ variance-component trap (cite booklet ch. 15's flag after verifying its wording). When improper is safe vs not.
6. Washout and its exception: y = θ₁+θ₂ observed — the sum concentrates, θ₁ alone never does (simulate; posterior of θ₁ stays prior-width). "Faces of nonidentifiability" note: symmetry (M19 label switching), weak likelihood, structural (this demo); DL pointer (overparameterized nets, M25).
7. Regularization = *implicit* prior (softened tone per coverage); weakly-informative defaults as "stability engineering."
**Sources.** Booklet ch. 5–7, 15; BDA3 by concept.
**Deps.** 05, 06.

### 08-frequentist-bridge — The Frequentist Bridge: Stein as Hero  [SIGNATURE S4]
**Spine.** The theories fuse asymptotically (BvM); where they don't, shrinkage wins — the frequentist crown jewel is a Bayesian move.
**Structure (pedagogy):** open with the learner's belief ("the MLE is obviously optimal for a Gaussian mean") → S4 shock → JS = empirical Bayes → BvM reconciliation → audits. Not a treaty; a reveal.
**Required.**
1. Sampling distributions and MLE asymptotics: overlay simulated sampling dist of θ̂ on N(θ, I⁻¹/n).
2. Cramér–Rao stated with its proviso (unbiased T, support free of θ — U(0,θ) foil one-liner); ONE numerical check (x̄ attains 1/(nI)); note shrinkage estimators may beat the CRLB (they're biased — the bound doesn't apply).
3. **S4 staged**: three *unrelated* quantities (batting average, wheat yield, MPG); predict-first ("can they borrow strength? obviously not…"); simulate d=10: total MSE MLE = 10.0 vs James–Stein ≈ 2.0 at θ=0, dominance across ‖θ‖ ✓, JS⁺ better still (1.26 ✓); collapse at d=1,2 (no dominance) — crossover at d=3.
4. James–Stein = empirical Bayes: derive δ = (1 − (d−2)/‖X‖²)X from θᵢ ~ N(0, τ²) with τ̂² from the marginal ✓ — the punchline sentence: "admissibility forced frequentists to invent a posterior mean."
5. BvM: overlay the *posterior* (one dataset) on the *sampling distribution of the MLE* (many datasets); TV distance printed at n ∈ {5, 50, 500}. Conditions EXPLICIT (rigor): well-specified, fixed finite-dim identifiable θ, interior point, prior positive+continuous at θ₀. Breakdown gallery: boundary (U(0,θ)); unidentified (M07 callback); **Neyman–Scott**: (Xᵢ,Yᵢ) ~ N(μᵢ, σ²) pairs ⇒ σ̂²_MLE → σ²/2, printed — infinitely many nuisances void consistency; misspecification ⇒ sandwich-variance mismatch (one line, cashed in M18).
6. Risk-set picture for a 2-point Θ: Bayes rules trace the lower boundary; admissible = (limits of) Bayes — complete-class stated in words, no proof. The "special case" framing is a theorem.
7. One bootstrap figure: classical resampling vs Bayesian bootstrap (Dirichlet(1,…,1) weights ✓) interval overlay; "the bootstrap is an implicit posterior."
8. Coverage audit demo: credible interval under a weak prior ≈ 95% frequentist coverage at moderate n (the audit Bayesians should pass); ties back to M06's coverage numbers.
9. Exercise: binomial minimax estimator (X+√n/2)/(n+√n) has *flat* risk — plot vs MLE's risk; crossing point; minimax = Bayes vs least-favorable prior.
**Sources.** C-B §7.3, §10.1; Efron–Morris by concept; booklet ch. 9 preview.
**Deps.** 04, 05, 06.

## Part III — Computation: integration is the bottleneck

### 09-monte-carlo — Monte Carlo Fundamentals
**Spine.** Any expectation becomes a sample average with a CLT error bar you must report; importance sampling fails *silently* — the weight diagnostics are the alarm.
**Required.**
1. Samples as lingua franca: posterior mean, intervals, P(θ>c), E[g(θ)] — all one `mean()` away; transformations for free.
2. MCSE = s/√M verified across 1,000 replications (the error bar on the error bar); E[√|Z|] estimated by MC and matched against quadrature (author must print the quadrature value — do not trust a remembered constant); π-by-darts error ∝ 1/√M at M = 10³ vs 10⁵.
3. Importance sampling SUCCESS: P(Z>4) = 3.167e-5; naive MC at M=10⁵ typically prints 0; shifted-proposal IS nails it with tiny SE (print both SEs).
4. IS FAILURE, predict-first ("guess the effective sample size of these 10⁵ weighted draws"): N(0,1) proposal for t₃ target — weight histogram, max-weight share, ESS collapse.
5. **ESS, correct formula (rigor sev-1):** ESS = (Σwᵢ)²/Σwᵢ² = M/(1+cv²), cv² = Var(w)/mean(w)² of the **unnormalized** weights (equivalently 1/Σw̄ᵢ² with normalized w̄). If citing the booklet here, flag its "ESS ≥ n" misprint (ch. 4).
6. Rejection sampling with acceptance-rate accounting (tie the bound to the acceptance rate).
7. Rejection-ABC in ~20 lines: infer Binomial θ from a summary statistic with tolerance ε; posterior vs exact Beta overlay as ε shrinks; "likelihood-free = conditioning on a neighborhood"; neural-SBI pointer (M25).
8. Bridge boxes: MC-dropout = averaging stochastic forward passes (M25); off-policy evaluation = importance weighting (RL).
**Sources.** Booklet ch. 3 §3.1, ch. 5; C-B §5.6; MCMT ch. 1 by concept.
**Deps.** 05.

### 10-metropolis-hastings — Metropolis–Hastings from Scratch
**Spine.** Thirty lines that provably target the posterior (detailed balance), plus diagnostics that are necessary but not sufficient — report ESS, not draw count.
**Required.**
1. Just-enough Markov chains: stationarity; detailed balance ⇒ stationarity proved in ~6 lines ✓ (sufficient, not necessary — say so); ergodicity in words; MH acceptance ratio derived, DB verified numerically on a 3-state chain.
2. 30-line RW-MH on a Beta-Binomial posterior; quantile match vs exact.
3. Tuning: **acceptance-vs-ESS sweep on a d=50 iid product target** (rigor sev-1 correction): optimum lands at acceptance ≈ 0.234 with step ≈ 2.38/√d (Roberts–Gelman–Gilks, asymptotic); the 1-D optimum is ≈ 0.44 — print both; state 0.234's scope precisely.
4. Bimodal 1-D target for the mode-hopping FAILURE only (predict-first: "will one chain find both modes?"); parallel-tempering mention (demo in M19).
5. Diagnostics built by hand, then checked against ArviZ: trace, ACF, ESS = M/(1+2Σ_{k≥1}ρ_k) ≤ M; split-R̂; **rank-normalized split-R̂ note** — ArviZ 1.x default is rank-normalized (Vehtari et al. 2021); compute the rank version by hand or print and explain the small discrepancy.
6. Fooling example: a stuck chain that single-chain diagnostics pass and 4-chain split-R̂ catches.
7. Spectral-gap mini: 2-state chain — second eigenvalue computed, relaxation time 1/(1−λ₂) tracks measured ACF (one figure; MCMT by concept). "Mixing is a spectral gap; diagnostics detect its absence."
8. Bridge: simulated annealing = MH with temperature → 0 (optimizer cousin).
**Sources.** Booklet ch. 11, 15; MCMT ch. 3–5, 12 by concept.
**Deps.** 09.

### 11-gibbs-augmentation — Gibbs Sampling and Data Augmentation
**Spine.** Sample one full conditional at a time; posterior correlation is the enemy (lag-1 autocorrelation = ρ², exactly); augmentation invents latents that restore conjugacy — and missing data are just more latents.
**Required.**
1. Gibbs = componentwise MH with acceptance 1 (derived ✓).
2. Normal(μ, σ²) both unknown: derive both full conditionals; run; **agreement audit** vs M05's exact NIG posterior, foregrounded (overlay + KS-style check) — the built-in correctness proof.
3. Bayesian linear regression by Gibbs (β | σ², σ² | β) on synthetic data with recovery check.
4. ρ-sweep, predict-first: bivariate Normal Gibbs zigzag; **lag-1 autocorrelation = ρ² exactly** (0.808 at ρ=.9, 0.980 at ρ=.99 ✓); ESS fraction ≈ (1−ρ²)/(1+ρ²) ≈ 0.01 at ρ=.99; the zigzag figure. Blocked Gibbs fix: ESS ratio printed. Motivates HMC.
5. Albert–Chib probit: truncated-normal latents restore conjugacy ✓ (derivation + sampler + parameter recovery on synthetic data); Pólya-Gamma for logistic = mention.
6. **Missing data & multiple imputation section:** missingness as latent variables inside Gibbs — bivariate Normal with MAR holes, impute-within-Gibbs; multiple imputation = repeated posterior draws of the missing entries; MCAR/MAR/MNAR = when the missingness mechanism drops out of the likelihood (ignorability); PO-as-missing-data promised for M24.
7. Rao-Blackwellization: average E[θ | rest] instead of raw draws; variance drop printed (booklet ch. 11 tie).
8. Bridge: augmentation is EM's E-step and the VAE's latent code (M13/M25).
**Sources.** Booklet ch. 10, 11, 13; C-B §4.4.
**Deps.** 05, 10.

### 12-hmc — HMC and NUTS: Geometry Wins in High Dimension  [SIGNATURE S1]
**Spine.** In high dimension the mass lives in a thin shell — the typical set; random walks die there; gradients + momentum take long coherent moves along it.
**Required.**
1. **S1 staged**: predict-first "where is the mass of N(0, I₁₀₀₀)?" → norms concentrate at √d ≈ 31.6, the mode holds essentially nothing ✓ (histogram at d ∈ {1, 10, 100, 1000}); consequence: plug-in-at-the-mode and RW both fail in high d.
2. RW-MH ESS vs dimension measured at d ≤ 128, power-law fit, extrapolate (rigor feasibility note); one figure.
3. Leapfrog HMC from scratch (~50 lines) on a correlated 2-D Gaussian; energy-error O(ε²) check; **stability threshold ε_crit = 2/ω exact** (ε=2.00 stable, 2.01 explodes ✓) — "a divergence is this mechanism firing"; HMC optimal acceptance ≈ 0.651 (symmetry with 0.234 ✓).
4. Neal's funnel in NumPyro: centered → divergences (scatter plot at the neck, `diverging` extra-field per idioms); non-centered via LocScaleReparam → divergence counts printed before/after.
5. PPL orientation box: NumPyro = course PPL (environment note); PyMC = mainstream API shown in a labeled `no-run` block; Stan = booklet's read-only insert; ArviZ = shared diagnostics layer.
6. SGLD teaser: overdamped Langevin dθ = ½∇log p dt + dW discretized in ~10 lines; stationary law = target; step-size bias noted (Lawler bridge; M25 callback).
7. Trimmed OUT (per panel): banana target.
**Sources.** Booklet insert-bda-hmc-stan, ch. 15; Lawler ch. 3–5 by concept; Neal by concept.
**Deps.** 10, 11.

### 13-laplace-em-vi — Deterministic Approximations: One Idea (the ELBO) Three Ways
**Spine.** Approximate the posterior with a computable shape; every shape has a signed, predictable failure — mean-field gets the mean right and the variance too small, by the factor 1−ρ² exactly.
**Required.**
1. Organize around the exact identity **log p(x) = ELBO(q) + KL(q ‖ p(·|x))** (KL to the POSTERIOR — rigor correction); derive it twice (decomposition + Jensen). All three methods are "choose q's family."
2. Laplace: on the **logit scale** for a Beta posterior (rigor: fair comparison), transform back; KL printed at n ∈ {5, 200} — good then bad; Laplace evidence approximation vs exact conjugate evidence (2-dp agreement at n=100).
3. EM on a minimal latent example (NOT the full GMM — that lives in M19): two-component 1-D mixture, known variances; E/M steps derived as coordinate ascent on the ELBO; log-likelihood monotone, printed trace; **EM = VI with a point mass on θ while q(z) is the EXACT conditional p(z|x,θ)** — the asymmetry is the reduction (rigor wording).
4. CAVI mean-field on a correlated 2-D Gaussian, predict-first ("will the marginals be right?"): means exact, marginal variances shrunk by **1−ρ² exactly** ✓ — the shrunken-ellipse figure.
5. CAVI on the NIG target vs M05's exact answer (mean spot-on, variance deficit measured).
6. SVI/AutoNormal (idioms) vs NUTS on the same model: means agree, tails light; wall-clock vs accuracy table.
7. "When to trust VI" box: point predictions and embeddings yes; tail risk and interval widths no; VAE forward pointer.
**Sources.** Booklet ch. 12–13; Bishop, BDA3 ch. 13 by concept.
**Deps.** 05, 09, 12.

## Part IV — Statistical learning, re-founded

### 14-bayesian-regression — Regression I: Bayesian Linear Models
**Spine.** Regression is a prior over lines conditioned into a posterior over lines; ridge IS the Gaussian prior (λ = σ²/τ², exactly), and cross-validating λ is empirical Bayes.
**Required.**
1. Posterior for β (known σ²) via M05's Gaussian toolkit; posterior-over-lines figure (30 sampled lines through the data).
2. Trumpet plot, predict-first ("sketch the width of your interval at x = 3× the data range"): predictive interval flares off-support while sklearn's point prediction stays mute; predictive variance decomposed aleatoric + epistemic, printed on- and off-support.
3. λ ↔ τ² exact correspondence: `Ridge(alpha)` coefficients == posterior mean, max|diff| at machine precision, for alpha ∈ {0.1, 1, 10, 100}; the table.
4. CV-λ ≈ EB-λ: cross-validated alpha tracks the marginal-likelihood-maximizing τ² on the same data (both printed across replicates) — "you were estimating your prior variance all along."
5. NIG full treatment (unknown σ²): predictive = Student-t (M05 callback); why intervals widen beyond Gaussian.
6. Robust regression: Student-t likelihood as a Gamma scale-mixture of Normals (derivation); 3 injected outliers hijack the Normal fit, barely move the t fit — slopes printed side-by-side; "robustness = marginalizing a latent variance, not an outlier heuristic."
7. Basis expansion (polynomial/spline): bias-variance re-read as prior strength; underfit/overfit = prior too strong/too weak, one figure.
8. Lasso: pointer back to M06's mode-vs-mean honesty (no re-derivation); horseshoe pointer to M18.
**Sources.** ISLP ch. 3, 6; booklet ch. 8; C-B by concept.
**Deps.** 05, 06, 08.

### 15-glms-classification — Regression II: GLMs and Classification
**Spine.** Pick the response's generative story and wire it through a link — cross-entropy training IS categorical-GLM maximum likelihood, and any proper prior cures separation.
**Required.**
1. The GLM recipe (exponential family + linear predictor + link), one table; Bernoulli→logistic, Poisson→log, Normal→identity.
2. Separation, predict-first ("what does the MLE do on linearly separable data?"): ‖ŵ‖ → ∞ (loss curve vs ‖w‖ shown); any proper Gaussian prior fixes it — the generative answer to "why weight decay."
3. Bayesian logistic three ways: Laplace (MAP + Hessian), from-scratch MH, NumPyro NUTS — coefficient posterior overlays agree.
4. Integrate, don't plug: posterior predictive class probability vs σ(xᵀŵ); **MacKay's moderated approximation** σ(xᵀμ/√(1+(π/8)xᵀΣx)) vs MC vs plug-in — gap largest near the boundary and at small n, quantified (rigor addition 2.5).
5. Calibration: reliability diagrams; well-specified model calibrated, overconfident plug-in isn't; the harness (reused in M25).
6. Generative vs discriminative, SOFTENED per rigor: naive Bayes reaches its asymptote fast, logistic has equal-or-lower asymptotic error; show measured error-vs-n curves under well-specified AND misspecified NB; claim "gap shrinks and can reverse," never a guaranteed crossover.
7. Survival section (04's seed cashed): exponential/Weibull with right-censoring — censored points contribute S(c); fit vs "drop the censored rows" (bias printed); "conditioning on exactly what you observed."
8. Ordinal mention: cumulative-link (ordered logit) = one more link; Poisson-with-offset exercise (rates with exposure).
**Sources.** ISLP ch. 4, 11; booklet ch. 8, 11; Ng–Jordan by concept (softened).
**Deps.** 13, 14.

### 16-hierarchical — Hierarchical Models: the Crown Jewel
**Spine.** Partial pooling = precision-weighted blend of group and population — James–Stein made adaptive — and it beats both no-pooling and complete-pooling out of sample.
**Required.**
1. Eight schools complete: y = [28,8,−3,7,−1,1,18,12], σ = [15,10,16,11,9,11,10,18]; no-pool / complete-pool / partial-pool on one axis (THE shrinkage picture); τ posterior; half-Cauchy vs half-Normal on τ sensitivity note.
2. Funnel returns (M12 callback): centered divergences → non-centered fix, counts printed.
3. Pooling-spectrum bake-off, predict-first ("which end of the spectrum predicts held-out data best?"): simulate many group-datasets, held-out MSE vs pooling weight — partial pooling wins; CONJUGATE updates inside the loop (feasibility: no MCMC inside replications).
4. Partial-pooling weight derived: wⱼ = (1/σⱼ²)/(1/σⱼ² + 1/τ²) — M05's master formula at a second level; "borrowing strength" made arithmetic.
5. One applied dataset (radon-style synthetic: counties, varying intercepts, a group-level predictor) with pandas; batting-average = mention only (coverage trim).
6. Empirical Bayes vs full Bayes: τ̂ plug-in vs τ marginalized — EB interval widths too narrow when J is small, printed; "EB = point-estimating the prior; fine at scale, overconfident at J=8."
7. James–Stein CALLBACK (no re-derivation): JS = EB with a point-mass hyperprior at 0.
8. Mixed-effects correspondence: statsmodels MixedLM point estimates vs the Bayesian posterior means, printed side by side — "random effects" = this, renamed; benchmarking/small-area mention (booklet ch. 9).
**Sources.** Booklet ch. 7, 9; Efron–Morris, Gelman–Hill by concept.
**Deps.** 08, 12.

### 17-model-checking — Model Checking and Comparison  [SIGNATURE S5]
**Spine.** A model must be able to predict its own data — the posterior predictive check; and the evidence carries a built-in Occam factor, so complexity control is automatic.
**Required.**
1. PPC as the spine: Poisson fit to overdispersed (NegBin) counts, predict-first ("will the fit notice anything wrong?"); test statistic T = var/mean; posterior-predictive p ≈ 0; the NB fix passes. PPC logic = self-consistency audit, not NHST; a couple of test statistics, graphical PPC.
2. **S5 staged**: polynomials degree 1–9 on data from degree 3, PROPER coefficient priors + moderate SNR (rigor: average a few datasets or pick clear signal); predict-first ("training error only falls — how do you pick 3 without CV?"); evidence computed EXACTLY (conjugate linear-model marginal likelihood) peaks at 3 while train MSE falls monotonically; the Occam factor derived (evidence = prior-predictive density; fit × complexity-penalty decomposition).
3. LOO/WAIC: PSIS-LOO via ArviZ (log-lik idiom) vs brute-force LOO on a small model (agreement printed) vs 10-fold CV; when LOO beats evidence (M-open preview) and vice versa.
4. Bayes factors, lightened (pedagogy): the one crisp Lindley demo — n = 10⁴, x̄ = 0.0258 (z ≈ 2.58, p ≈ 0.01): BF₀₁ = 1.8 → 18 as the H₁ prior widens τ = 0.5 → 5 ✓ — p rejects while the BF favors H₀; the dissection (diffuse alternative pays an Occam tax); BF prior-sensitivity table = the honest caveat; "revisited in M26."
5. p-value calibration: distribution of p under H₀ (uniform) vs realistic effects; what p = 0.049 implies about replication (simulated).
6. MDL one-liner: −log evidence = codelength (03's information section cashes out).
7. Model averaging vs selection: predictive stacking mention.
**Sources.** Booklet ch. 8, 12; BDA3 ch. 6–7 by concept; ISLP ch. 5.
**Deps.** 14, 15, 16.

### 18-scale-and-misspecification — Multiplicity, Misspecification, and Large-Scale Inference  [NEW]
**Spine.** With thousands of parallel problems the prior becomes estimable from the data itself, and shrinkage does multiplicity control automatically; when the model is wrong, the posterior is too narrow — audit it.
**Required.**
1. Winner's curse, predict-first ("the top-scoring effect of 1000 — how big is it really?"): simulate 1000 effects, most null; the naive top-k estimates are inflated; hierarchical shrinkage (Normal-Normal on all 1000) de-biases selection automatically — selected-effect true values vs raw vs shrunk, printed.
2. Two-groups model: z-scores from π₀ = 0.95 null + alternatives; Benjamini–Hochberg vs Bayesian local-fdr(z) (mixture density estimate); discoveries at matched FDR printed; FDR ≈ posterior P(null | z) — the Bayesian reading of BH.
3. Empirical Bayes at scale (Efron): the prior estimated from 1000 parallel problems is no longer a "subjective" object — large-scale inference as the EB regime; M16 EB caveats vanish as J grows (interval-width comparison).
4. Sparsity as multiplicity control: horseshoe prior recovering 5-of-100 nonzero signals (NumPyro, modest sizes); vs ridge (no zeros) and lasso-MAP (M06 callback); global-local shrinkage in one figure.
5. **M-open section:** fit a Normal mean model to skewed, heteroskedastic truth — posterior sd vs sandwich SE printed (the frequentist misspecification audit; M08's BvM-misspec line cashed); "the posterior is exactly right about a wrong model."
6. Power/tempered posteriors: p_η(θ|y) ∝ p(y|θ)^η π(θ), η<1 widens honestly (demo); tempering ↔ SMC pointer (M19/M21).
7. Bagging-as-robustness mention + one small demo or pointer; M-closed / M-complete / M-open vocabulary box ("all models are wrong" made technical).
**Sources.** ISLP ch. 13; Efron LSI by concept; booklet ch. 9 (shrinkage) tie.
**Deps.** 16, 17.

## Part V — Latent structure, functions, and sequences

### 19-mixtures-dp — Latent Structure: Mixtures and the Dirichlet Process
**Spine.** Cluster labels are unknowns like any other — marginalize them; EM's point labels hide uncertainty that Gibbs reveals; a DP lets K grow with the data.
**Required.**
1. 2-D GMM: full EM here (dedup from M13) vs Gibbs with conjugate priors; **the emotional beat, predict-first**: "how sure are we about the boundary points' labels?" — EM's crisp responsibilities vs the posterior label distributions (uncertainty map figure).
2. Label switching shown (μ₁/μ₂ trace swap) and handled (ordering constraint / post-hoc relabeling); nonidentifiability-by-symmetry (M07 callback).
3. Multimodality + parallel tempering demo (M10's mention cashed): two-well posterior; plain chain stuck, tempered ladder mixes; mixing-time-vs-barrier one-liner (MCMT by concept).
4. CRP from scratch: rich-get-richer dynamics; **E[Kₙ] = α[ψ(α+n)−ψ(α)] exact** (rigor sev-1) overlaid on simulations at α ∈ {1,2,5}; asymptotic α·ln(1+n/α); "α log n" only as the n ≫ α limit. CRP exchangeability (M01 Pólya-urn callback).
5. Stick-breaking construction (the booklet's handwritten insert — cite it); truncated-DP mixture on galaxy-like 1-D data; posterior over K histogram ("the data chooses").
6. Zero-inflated Poisson as an exercise (augmentation callback M11).
7. Box: mixtures = the pattern behind HMMs, topic models, VAEs (discrete/continuous latents).
**Sources.** Booklet ch. 13–14 + stick-breaking insert; Neal 2000 by concept.
**Deps.** 11, 13, 17.

### 20-gaussian-processes — Gaussian Processes: Priors over Functions
**Spine.** A GP is Bayesian linear regression pushed to infinitely many basis functions; the kernel is the covariance of a prior over functions, and the marginal likelihood tunes it with built-in Occam.
**Required.**
1. LEAD with the two-routes-identical check: finite Gaussian-weight basis regression vs kernel form k = φᵀΣφ — predictions identical to machine precision, printed; then the ∞-limit to squared-exponential (Gaussian-bump basis, numeric limit check).
2. Kernel gallery: prior draws from RBF / Matérn-3/2 / periodic / linear (what smoothness assumptions LOOK like); hyperparameters morph the draws.
3. Exact GP posterior in ~20 numpy lines (M05 Gaussian toolkit callback): mean, bands, collapse at noiseless data points, widening off-data.
4. ML-II: lengthscale by marginal likelihood; fit-vs-complexity decomposition printed (M17 Occam callback); overfit-lengthscale foil.
5. GP posterior mean = kernel ridge regression ✓ (machine-precision print) — the frequentist special case, again.
6. Bayesian optimization teaser: expected improvement loop finds a 1-D optimum in ~8 evaluations (M23 bridge); one figure.
7. NNGP teaser, one figure: wide 1-hidden-layer nets (width 1/10/1000) → function-space prior approaches a GP ✓.
8. O(n³) honesty; inducing points pointer; BART mention ("another prior over functions — trees; reading map entry").
**Sources.** Rasmussen–Williams by concept; ISLP ch. 7; booklet ch. 14 framing.
**Deps.** 14, 17.

### 21-state-space — State Space: Filtering Is Bayes on a Conveyor Belt
**Spine.** The Kalman filter is module 05's Normal-Normal update on repeat — predict = marginalize, update = condition; when linear-Gaussian breaks, carry the posterior as weighted particles.
**Required.**
1. "Nothing new" as the explicit reveal (pedagogy): derive the 1-D Kalman filter as alternating marginalize/condition; the gain IS the shrinkage weight (M05/M16 callbacks); 2-D position+velocity tracking with uncertainty ellipses.
2. AR(p) = conjugate regression on lags: Bayesian AR(2) fit (M14 machinery verbatim); stationarity-of-posterior-draws check mention.
3. Ornstein–Uhlenbeck: discretize (Lawler bridge: exact AR(1) discretization), filter noisy observations; parameter-vs-state inference distinguished.
4. Bootstrap particle filter (~60 lines) on stochastic-volatility-lite (nonlinear/non-Gaussian), predict-first ("what happens to the weights after 50 steps?"): degeneracy — ESS trace collapse (M09's ESS reused) — then resampling fix; one-step-ahead predictive checks.
5. RTS smoothing mention (one paragraph); SMC-samplers/tempering pointer (M18/M19 callback).
**Sources.** Lawler by concept; Särkkä by concept; booklet ch. 8 framing.
**Deps.** 05, 09, 14.

### 22-decisions-bandits — Decisions and Bandits: Uncertainty You Can Act On
**Spine.** A posterior is not a deliverable — an action is; Thompson sampling (sample θ, act as if true) is embarrassingly simple and near-optimal.
**Required.**
1. Utility → threshold: cancer-screening cost matrix with FN = 10×FP ⇒ act when p > 1/11 ≈ `0.091`, derived (threshold = C_FP/(C_FP+C_FN)) and shown on expected-loss curves; "0.5 is almost never the right threshold"; ROC one-liner.
2. A/B shipping decision (M05's test driven to line 4): expected loss of ship-A/ship-B/keep-testing; stop when EVSI < sampling cost.
3. EVSI/preposterior: price "1,000 more samples" in expected-loss units (simulate future posteriors); value-of-information as the design bridge (M23).
4. Bandit tournament, predict-first ("rank Thompson, ε-greedy, UCB1 before running"): 3-arm Bernoulli, VECTORIZED closed-form Beta updates (feasibility), 10⁴ pulls × 100 reps; cumulative-regret curves; Thompson derived in 5 lines (probability matching on the argmax posterior).
5. Exploration = acting under parameter uncertainty rather than plug-in certainty (deep-RL pointer); admissibility callback (M08).
**Sources.** C-B §8.3.5, §10 decision sections; Russo et al. by concept; booklet ch. 8.
**Deps.** 06, 08 (decision frame), 05.

### 23-experimental-design — Experimental Design
**Spine.** Design determines the likelihood you get to condition on — randomization buys ignorability, and information can be priced before you buy it.
**Required.**
1. Why randomize if you're Bayesian, predict-first: same model fit to a confounded DGP vs a randomized DGP — posterior lands wrong vs right (numbers printed); ignorability = "the likelihood you wrote is the likelihood you got"; formal treatment of confounding deferred to M24.
2. Power vs assurance: classical two-sample power at a point alternative (Montgomery-style) vs assurance = ∫ power × prior (preposterior simulation); both printed; "power answers a θ you don't know; assurance averages over what you believe."
3. **Optional-stopping lab — four claims separated** (rigor sev-2): (a) the posterior is unchanged by θ-independent stopping (likelihood identity, shown); (b) prior-averaged calibration is ALSO preserved under optional stopping (posterior-is-a-martingale; simulate credible-interval coverage under stopping); (c) frequentist Type-I inflates: ~0.20 at 10 looks (≈4×), ~0.46 under continuous monitoring to N=1000 (≈9×; law of iterated logarithm cited) — state the number of looks with every number; (d) SELECTIVE REPORTING (publish-if-significant) breaks calibration for everyone — separate simulation. Plus the genuine Bayesian caveat: sampling-to-a-foregone-conclusion for point-null Bayes factors with diffuse alternatives (M17 callback).
4. 2³ factorial: effects = contrasts = regression coefficients (Montgomery bridge; synthesize data, verify against Montgomery's worked example if cleanly extractable); hierarchical prior on effects (effect sparsity); interaction reading.
5. Expected-information-gain design: choose the next dose in a logistic dose–response by maximizing EIG over a grid (small, exact-ish via quadrature); D-optimality = maximize det(XᵀX) = minimize posterior-covariance det under a flat prior — 2² factorial vs one-factor-at-a-time det ratio printed.
6. Randomization/permutation inference box (M01's exchangeability cashed): permutation p-value on one synthetic experiment; "the design justifies the test."
**Sources.** Montgomery ch. 1–6, 9, 12; booklet ch. 6–7; Lindley by concept.
**Deps.** 04 (LP), 07, 22.

## Part VI — Causality and the modern synthesis

### 24-causal — Causal Inference: A Different Joint Distribution
**Spine.** Causal questions are about a joint that includes outcomes you never observe; identification — not model fit — is what licenses the answer.
**Required.**
1. Potential outcomes (Y(0), Y(1)) as missing data (M11 MI callback); the fundamental problem; ATE identified under randomization ((Y(0),Y(1)) ⊥ T — M23 callback).
2. Confounding demo: simulate a confounded DGP; naive difference biased (numbers); backdoor adjustment recovers truth.
3. DAGs at working depth: d-separation on chain/fork/collider; conditioning on a collider OPENS a path — Simpson's-paradox flip demo (aggregate vs adjusted signs both printed; when adjusting is wrong vs required — collider vs confounder, side by side).
4. Backdoor criterion applied to a 5-node graph; frontdoor mention; do-calculus = three rules named + pointer (not derived); PO ↔ DAG correspondence table.
5. Estimator trio on one dataset: regression adjustment, stratification, IPW — IPW weights = importance weights (M09 callback!); overlap/positivity pitfall shown (extreme weights).
6. "No causes in, no causes out": identification assumptions are not testable from the joint alone (one adversarial example: two DGPs, same observational law, different ATEs).
**Sources.** Imbens–Rubin, Pearl by concept; ISLP framing.
**Deps.** 11, 23.

### 25-deep-learning-lenses — Bayesian Lenses on Deep Learning and Generative AI
**Spine.** Modern deep learning is approximate Bayes in some places and merely rhymes with it in others — sorting practices into theorem / heuristic / open is the transferable skill.
**Structure (pedagogy):** two hands-on labs + two exact demos + the three-column ledger as the deliverable; everything else is explicitly "map, not territory."
**Required.**
1. Theorems first (3 lines each): weight decay = Gaussian-prior MAP ✓; cross-entropy = categorical MLE ✓; label smoothing / early stopping = regularizing priors (label: heuristic).
2. **LAB 1 — ensembles & calibration:** 5 small sklearn MLPs vs a single net on a toy problem; disagreement = epistemic proxy; reliability diagrams + ECE printed (M15 harness); temperature scaling as post-hoc calibration; deep ensembles ≈ multi-modal posterior mixture (label: heuristic with evidence).
3. **LAB 2 — in-context learning as implicit posterior predictive:** exchangeable Beta-Bernoulli sequences; a fitted sequence predictor's p(next | context) vs the exact posterior predictive (agreement printed); de Finetti callback (M01); label: **open/active research**, cite Xie et al. by concept; honest-limits box.
4. **Exact demo — diffusion without a neural net:** forward OU noising of a 2-component GMM stays GMM (closed form!); exact score ∇log p_t available analytically; integrate the reverse SDE by Euler–Maruyama and watch samples reassemble the mixture — diffusion = hierarchical latent chain + score-following reverse dynamics (Lawler bridge; M12 SGLD callback). No training, fully verifiable.
5. **Exact demo — double descent in random-features regression:** min-norm/ridgeless fit, p swept through n; test error peaks at the interpolation threshold and descends past it (exact linear algebra, cheap); the effective-parameters/marginalization reading; label: partially understood.
6. VAE = M13's ELBO with amortized q (annotated equations, `no-run` pseudo-code; no training run); MC-dropout ≈ VI mention (Gal–Ghahramani; label: heuristic); SGD-noise ≈ SGLD sketch (M12 callback; label: heuristic).
7. LLM next-token = categorical MLE at scale; temperature = tempering (M18 callback); the ledger table: ~12 practices × (Bayesian reading | theorem/approx/heuristic/open | what the reading buys you).
8. Overparameterized nets are massively nonidentified (M07 callback); conformal → M26.
**Sources.** ISLP ch. 10; Lawler ch. 2–3, 5; MacKay, Murphy PML2, Song et al., Xie et al. by concept.
**Deps.** 13, 15, 18 (tempering), 12.

### 26-capstone — One Theory, Two Audits (capstone)
**Spine.** One calculus — a joint plus conditioning; two audit cultures — post-data belief and pre-data procedure guarantees; the working statistician runs both.
**Length exception.** 1,500–2,500 words; minimal new code.
**Required.**
1. The ledger, every row pointing to a module the learner RAN: marginalize-vs-profile nuisances (one tiny NIG demo here — the only new code); stopping rules (M23); conditional coverage (M06); Lindley (M17); misspecification (M18); calibration audits (M15/M25).
2. The ML-zoo audit table, ~20 rows (OLS, ridge, lasso, horseshoe, logistic, SVM, trees, RF, boosting, BART, k-means, PCA/PPCA, GP, Kalman, dropout, ensembles, VAE, diffusion, conformal, bootstrap) × (Bayesian reading | status: theorem/approx/heuristic/none | what the reading buys) — **fill-in-first self-test** (blank column presented first; answers follow).
3. Conformal prediction, precisely: split-conformal gives finite-sample, distribution-free, *marginal* coverage under exchangeability; no conditional guarantee; breaks under shift — the model-free audit (rigor wording; M01 exchangeability callback).
4. Calibrated-Bayes stance (Rubin/Little): Bayesian for inference, frequentist for evaluation; the working decision guide ("given problem X, reach for Y, audit with Z") as a compact table.
5. Annotated reading map with "read for" notes: BDA3, MacKay ITILA, Murphy PML1/2, Rasmussen–Williams, Särkkä, Efron LSI, Efron–Hastie CASI, C-B chapters worth a second pass, the booklet chapters, ISLP/Montgomery/MCMT/Lawler sections used.
**Deps.** Everything.

---

## Cross-cutting apparatus (unchanged from draft, now binding)
- Bridge boxes ≥1/module (C-B §, booklet ch., or ML practice — foundational modules 03/04/09/10/11 have theirs named above; do not skip).
- Pitfalls section per module: the 3–5 mistakes practitioners actually make.
- Exercises 3–6 per module in STYLE.md §5 format; ≥1 with a genuinely surprising answer; ≥1 connecting to the learner's ML/DL background.
- Numbers contract, seeds, runtime, figure rules: STYLE.md §4.
- Every module ends with Takeaways (≤7 bullets) and executes at least one of lines 2–4 on its own examples.

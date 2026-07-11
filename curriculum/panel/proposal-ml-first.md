# Proposal — ML-Practitioner-First Curriculum

**Stance.** The learner already fits ridge, trains logistic regressions, cross-validates, ensembles nets,
and ships uncertainty. Each module *opens with a procedure they already run* (usually a scikit-learn /
PyTorch one-liner) and re-derives it as a Bayesian object. Theory enters only when a *named, numeric*
example breaks the procedure — never before. The spine is the brief's four lines, made mechanical:

> **(1) Model = joint distribution over knowns + unknowns.  (2) Inference = condition on data.
> (3) Prediction = posterior predictive.  (4) Decision = argmin expected loss under the posterior.**

Every module ends by executing at least one of lines (2)–(4) on the example it opened with, and prints
the number the prose quotes. Frequentist results appear as *audits and special cases* of this machine,
never as a rival tribe. MCMC is "what you reach for when conjugacy fails," not the subject.

Format per module: **Promise / Examples (numeric) / Derive+verify / Sources / Code / Deps.**

---

## Part 0 — The whole course in one worked example

### M0 — Your ridge regression was already Bayesian
- **Promise:** you can run the four-line machine end-to-end on three problems and see it reduce to things you already do.
- **Examples:** (a) Ridge on synthetic `n=50, p=200` (diabetes-like): `sklearn Ridge(alpha=10)` coefs equal `(XᵀX+10I)⁻¹Xᵀy` equal posterior mean of `β~N(0,(σ²/10)I)` — print `max|diff| < 1e-10`. (b) Medical test `sens=.99, spec=.95, prev=.001` → joint→condition→**PPV=1.94%**, then decide treat/scan under a cost matrix. (c) Coin: `Beta(1,1)` + 7 heads/10 → `Beta(8,4)`, posterior mean `0.667`, decide whether to accept 2:1 odds.
- **Derive+verify:** ridge = MAP = posterior mean (Gaussian prior); Bayes' rule PPV by hand and by 10⁶-sample simulation agree.
- **Sources:** booklet ch01–02 (paradigm, coherence); C-B §1.2–1.3; ISLP §6.2.1.
- **Code:** `m00_spine.py` — the three demos, one figure (prior→posterior→decision).
- **Deps:** none.

## Part A — Re-founding the estimators you already fit (point → posterior)

### M1 — Loss minimization is MAP; MLE is its flat-prior limit
- **Promise:** you can read any training loss as a negative log-posterior and say exactly which prior it assumes.
- **Examples:** (a) `LogisticRegression(penalty=None)` coefs == argmax Bernoulli log-lik via hand Newton–Raphson (print equality, 4 dp). (b) Gaussian mean, `n=20`: MLE=`x̄`=MAP under flat prior. (c) Poisson counts `[2,0,3,1,4]`: MLE `λ̂=2.0` = MAP; cross-entropy = NLL of Bernoulli, MSE = NLL of Gaussian.
- **Derive+verify:** `argmin Σ loss = argmax likelihood = argmax posterior` when `log prior` is constant; simulate that MAP→MLE as prior variance→∞.
- **Sources:** C-B §7.2 (MoM, MLE, Bayes); booklet ch02; ISLP §3.1, §4.3.
- **Code:** `m01_loss_is_nll.py` — Newton logistic; loss↔likelihood table.
- **Deps:** M0.

### M2 — Your regularizer is a prior (ridge=Gaussian, lasso=Laplace)
- **Promise:** you can convert any penalty into a prior and back, and explain what cross-validating `λ` is really estimating.
- **Examples:** (a) Ridge `alpha∈{0.1,1,10,100}` ↔ prior var `τ²=σ²/alpha`; overlay sklearn coefficient path on posterior-mean path (identical). (b) Lasso ↔ `Laplace(b=σ²/alpha)`; recover 5 true nonzeros out of `p=100` as alpha↑; MAP == lasso coefs. (c) CV-selected alpha ≈ empirical-Bayes `τ̂²` from marginal-likelihood max on the same data — print both, show they track.
- **Derive+verify:** MAP under `N(0,τ²)` = ridge with `λ=σ²/τ²`; under Laplace = lasso; simulate CV-λ vs marginal-lik-λ.
- **Sources:** ISLP §6.2 (ridge/lasso); C-B §7.2; booklet ch03 §3.2 (prior construction, Jeffreys/shrinkage).
- **Code:** `m02_reg_is_prior.py` — path overlay, EB-vs-CV λ figure.
- **Deps:** M1.

### M3 — Conjugate updating: the prior worth κ observations
- **Promise:** you can update a belief in closed form, run an A/B test, and quantify how much data your prior is worth.
- **Examples:** (a) A/B test A=30/1000, B=45/1200, `Beta(1,1)` priors → `P(p_B>p_A)` and `P(uplift>1%)` by 10⁵ Beta draws. (b) `Beta(2,8)` = 10 pseudo-trials; after 7/10, `Beta(9,11)` — posterior mean slides prior→MLE. (c) Stream 1000 `Bernoulli(0.3)`; plot posterior mean → 0.3 and interval width ∝ `1/√n`.
- **Derive+verify:** posterior mean is a convex combo `w·MLE+(1−w)·prior-mean`, `w=n/(n+κ)`, `κ=a+b`; sequential == batch update.
- **Sources:** booklet ch03 §3.2–3.3, ch04 §4.2 ("how many observations is the prior worth"); C-B §3.2.
- **Code:** `m03_conjugate.py` — Beta-Binomial A/B; κ read-off; online convergence.
- **Deps:** M1.

### M4 — Normal–Normal, shrinkage, and the James–Stein free lunch
- **Promise:** you can compute a shrinkage estimate and demonstrate it beats the MLE in ≥3 dimensions.
- **Examples:** (a) `σ²=9, δ²=4, n=5` → `λ=δ²/(δ²+σ²/n)=0.69`; posterior mean `0.69·x̄+0.31·θ`. (b) James–Stein: `p=10` means `θ_i~N(0,1)`, one obs each; over 2000 sims JS total MSE / MLE MSE ≈ 0.6 (print). (c) Batting-average preview: 18 players' early AVG shrink toward `.270`.
- **Derive+verify:** Normal–Normal conjugacy + variance-add-through (booklet ch03 predictive `σ²+(1−λ)δ²`); simulate Stein dominance and its collapse at `p=1,2`.
- **Sources:** booklet ch03 (Normal–Normal, prediction), ch09 §9.2 (empirical Bayes); C-B §7.2–7.3, §4.4.
- **Code:** `m04_shrinkage.py` — Stein risk-ratio sim; shrinkage-vs-n figure.
- **Deps:** M3.

### M5 — Exponential families & sufficiency: what you actually need to store
- **Promise:** you can spot when a model has a conjugate prior and reduce a dataset to the few numbers that matter.
- **Examples:** (a) Write Normal, Bernoulli, Poisson, Gamma in exp-family form; read conjugate prior off natural params. (b) Two `N(μ,σ²)` datasets with identical `(Σx, Σx²)` → byte-identical posteriors (verify). (c) Gamma–Poisson: `Σx` sufficient, posterior `Gamma(a+Σx, b+n)` on counts summing to 47 over n=20.
- **Derive+verify:** Fisher–Neyman factorization ⇒ posterior depends on data only through the sufficient statistic; conjugacy = prior in the family's natural form.
- **Sources:** C-B §3.4 (exp families), §6.2 (sufficiency); booklet ch03 §3.2.1 (constructing conjugate priors).
- **Code:** `m05_expfam.py` — sufficiency-collision demo; conjugate-lookup table.
- **Deps:** M3.

## Part B — Turning posteriors into decisions (the payoff, delivered early)

### M6 — The posterior predictive: prediction is a distribution, not a point
- **Promise:** you can produce a predictive distribution that separates aleatoric from epistemic uncertainty.
- **Examples:** (a) Beta-Binomial predictive for next 20 flips is Beta-Binomial, *overdispersed* vs plug-in Binomial — print variance inflation. (b) Normal predictive var `= σ² + (1−λ)δ²`; sweep `n`, watch epistemic term → 0. (c) Poisson–Gamma predictive = Negative-Binomial; on counts mean=3/var=8, plug-in Poisson underpredicts `P(X>10)` — quantify.
- **Derive+verify:** `p(x*|x)=∫p(x*|θ)p(θ|x)dθ`; law of total variance splits it; simulate predictive coverage vs plug-in.
- **Sources:** booklet ch03 (predictive), ch05 §5.2 (prediction), ch08 §8.3; C-B §4.4 (mixtures).
- **Code:** `m06_predictive.py` — overdispersion figure; aleatoric/epistemic split.
- **Deps:** M3, M4.

### M7 — Decision theory: the action, not the posterior, is the deliverable
- **Promise:** you can turn any posterior + loss into the optimal action and defend the threshold.
- **Examples:** (a) On a skewed Gamma posterior (mean 3.0, median 2.7, mode 2.0): squared loss→mean, absolute→median, 0/1→mode (verify all three). (b) Classifier where FN costs 10×FP → optimal threshold `1/11≈0.091`, not 0.5; apply to logistic scores. (c) Newsvendor: demand ~ Poisson–Gamma, order `q` minimizing E[overage+underage] = a posterior quantile.
- **Derive+verify:** Bayes action minimizes posterior expected loss; derive the three estimators as loss-specific; complete-class / admissibility stated, Stein tie-in.
- **Sources:** C-B §7.3.4, §8.3.5 (loss-function optimality); booklet ch08 §8.1 (HPD as loss-driven interval).
- **Code:** `m07_decisions.py` — cost-matrix threshold; newsvendor quantile.
- **Deps:** M6.

### M8 — Frequentist audits: calibration, coverage, and Bernstein–von Mises
- **Promise:** you can check whether your Bayesian intervals are actually calibrated and know when credible ≈ confidence.
- **Examples:** (a) 95% credible interval for a Normal mean covers truth in ~95% of 5000 datasets (`n=20`, weak prior) — print empirical coverage. (b) BvM: logistic-coef posterior → `N(MLE, I⁻¹)`; overlay posterior sd on Fisher SE, equal at `n=500`, divergent at `n=20`. (c) Nonparametric bootstrap of a mean ≈ Bayesian bootstrap (Dirichlet weights) — near-identical intervals.
- **Derive+verify:** BvM asymptotic normality; simulate coverage; bootstrap-as-posterior. Honest note: where they disagree (boundary, strong prior, small n).
- **Sources:** C-B §5.5 (convergence, delta method), §10.1 (asymptotic efficiency, bootstrap), §9.2–9.3 (coverage); booklet ch08.
- **Code:** `m08_audits.py` — coverage sim; BvM overlay; bootstrap-vs-Bayes.
- **Deps:** M7.

### M9 — Testing & model choice: Bayes factors, Lindley, and WAIC = CV
- **Promise:** you can compare models honestly and explain why p-values and Bayes factors can point opposite ways.
- **Examples:** (a) Point null `θ=0`, `n=10⁶`, `z=1.96` (p=.05) → Bayes factor ≈ 19:1 *for* H₀ — Lindley's paradox, print both verdicts. (b) Polynomial regression deg 1–9: WAIC/LOO (arviz) and 10-fold CV both pick ~deg 3; print elpd vs CV-MSE. (c) 1000 tests, 50 true effects: Benjamini–Hochberg FDR vs hierarchical local-FDR shrinkage — compare true/false discoveries.
- **Derive+verify:** marginal likelihood = automatic Occam; WAIC ≈ LOO ≈ CV; Lindley's paradox derived and simulated; FDR as empirical-Bayes.
- **Sources:** booklet ch08 §8.2 (Bayes factor, marginal likelihood), ch10 §10.6 (Bayesian CV), ch12 §12.1 (DIC); C-B §8.2–8.3; ISLP §13 (FDR).
- **Code:** `m09_modelchoice.py` — Lindley demo; WAIC-vs-CV; FDR comparison.
- **Deps:** M6, M8.

## Part C — Computation when conjugacy fails

### M10 — Laplace approximation: the Gaussian error bars you already trust
- **Promise:** you can approximate any smooth posterior with a Gaussian and know when the tails betray you.
- **Examples:** (a) Logistic posterior: Laplace mean=MAP, cov=`(−∇²log p)⁻¹`; overlay on MCMC — matches at `n=200`, tails wrong at `n=20`. (b) Marginal likelihood via Laplace vs exact on a conjugate case (agree to 2 dp). (c) `Beta(8,4)`: Laplace-Normal vs true, expose skew mismatch.
- **Derive+verify:** 2nd-order Taylor of log-posterior; curvature = observed Fisher info; simulate error vs `n`.
- **Sources:** C-B §10.1 (asymptotics, Fisher info); booklet insert-bda-hmc-stan (normal approx); ISLP §4.3.
- **Code:** `m10_laplace.py` — Laplace-vs-MCMC overlay; evidence approximation.
- **Deps:** M1, M8.

### M11 — Monte Carlo & importance sampling
- **Promise:** you can estimate any expectation with a reported Monte Carlo error and rescue rare-event estimates.
- **Examples:** (a) `E[√|Z|]`, `Z~N(0,1)` (booklet ex): MC estimate ± MCSE → exact `0.822` as `M↑`. (b) π by unit-circle darts, error ∝ `1/√M` at `M=10³,10⁵`. (c) `P(Z>4)=3.17e-5`: naive MC fails, shifted-proposal IS succeeds; report ESS `=(Σw)²/Σw²`.
- **Derive+verify:** LLN + CLT give `MCSE=s/√M`; IS identity and weight variance; ESS collapse under bad proposal.
- **Sources:** booklet ch03 §3.1 (MC integration), ch05 §5.9–5.11 (IS, choosing proposal); C-B §5.6 (generating samples).
- **Code:** `m11_montecarlo.py` — MCSE convergence; IS rare-event; ESS diagnostic.
- **Deps:** M6.

### M12 — Gibbs sampling & data augmentation
- **Promise:** you can build a Gibbs sampler from full conditionals and recognize when correlation cripples it.
- **Examples:** (a) Bivariate Normal `ρ=0.9` Gibbs vs exact; autocorrelation shows slow mixing. (b) `N(μ,σ²)` unknown both: Normal|σ² and Inv-Gamma|μ conditionals vs conjugate NIG truth (KS test passes). (c) Pólya-Gamma data-augmented logistic regression Gibbs recovers booklet ch11 coefficients.
- **Derive+verify:** each conditional leaves the joint invariant; Rao-Blackwellized estimator beats raw average; high-ρ mixing failure predicted then measured.
- **Sources:** booklet ch10 (Gibbs, diagnostics, Rao-Blackwell, griddy Gibbs), ch11 §11.4 (logistic), ch13 §13.2 (data augmentation); C-B §4.4.
- **Code:** `m12_gibbs.py` — bivariate + NIG + PG-logistic; autocorr figure.
- **Deps:** M5, M11.

### M13 — Metropolis–Hastings: sampling anything, and why it works
- **Promise:** you can sample from an unnormalized density and tune the proposal to a healthy acceptance rate.
- **Examples:** (a) `Beta(8,4)` by random-walk MH; tune step to 23–44% acceptance; match exact quantiles. (b) Poisson-regression MH (booklet ch11 ex II) vs statsmodels GLM coefs. (c) Numerically verify detailed balance `π(x)P(x→x')=π(x')P(x'→x)` on a 3-state chain.
- **Derive+verify:** MH acceptance `α=min(1, [p(x')q(x|x')]/[p(x)q(x'|x)])` ⇒ detailed balance ⇒ target stationary; acceptance-vs-step tuning curve.
- **Sources:** booklet ch11 (MH, convergence, proposal spread, tuning); MCMT ch3 (Metropolis chains); C-B §7.
- **Code:** `m13_mh.py` — RW-MH; detailed-balance check; acceptance sweep.
- **Deps:** M12.

### M14 — HMC / NUTS and PyMC as the production workhorse
- **Promise:** you can fit a nontrivial model in PyMC with NUTS and explain why gradients buy efficiency.
- **Examples:** (a) The M12/M13 logistic model in PyMC NUTS; ESS/sec far exceeds Gibbs/MH (print). (b) Leapfrog volume preservation + Hamiltonian conservation vs step `ε`; divergences at large `ε`. (c) Unadjusted Langevin `dθ=½∇log p·dt+dW` (Lawler) as discretized SDE: stationary ∝ posterior, bias vs step size.
- **Derive+verify:** Hamiltonian dynamics preserve the canonical density; leapfrog is symplectic; Langevin SDE stationary distribution = target.
- **Sources:** booklet insert-bda-hmc-stan (HMC/NUTS/Stan); Lawler ch3 (Itô, diffusions), §4.3 (Feynman–Kac); MCMT ch3.
- **Code:** `m14_hmc_pymc.py` — PyMC NUTS fit; leapfrog demo (keep draws ≤2000×2 chains for <180s).
- **Deps:** M13.

### M15 — Did it converge? Diagnostics & Markov-chain mixing
- **Promise:** you can certify (or reject) a run with R-hat/ESS and diagnose the geometry that broke it.
- **Examples:** (a) 4 chains, R-hat & ESS via arviz; a too-short-warmup run flagged R-hat>1.1. (b) Neal's funnel: centered param diverges, non-centered fixes it — predict-then-verify. (c) 2-state chain: mixing time vs spectral gap (MCMT); relate ESS to integrated autocorr time `τ_int`.
- **Derive+verify:** R-hat as between/within variance ratio; `MCSE=sd/√ESS`; spectral-gap → mixing-time bound; reparameterization changes geometry not the model.
- **Sources:** booklet ch10 §10.2 (trace, autocorr, Geweke, ESS), ch15 (MCMC difficulties); MCMT ch4–5, ch12 (TVD, coupling, eigenvalues/gap).
- **Code:** `m15_diagnostics.py` — R-hat demo; funnel fix; gap↔mixing sim.
- **Deps:** M14.

### M16 — Variational inference & EM (and the VAE)
- **Promise:** you can trade exactness for speed with a variational posterior and see where it lies to you.
- **Examples:** (a) EM for a 2-component Gaussian mixture on Old-Faithful-like data; log-lik monotone increases. (b) Mean-field ADVI vs NUTS on the logistic model: VI *underestimates* posterior variance — quantify the gap. (c) Tiny VAE on 8×8 digits: ELBO = reconstruction − KL; latent traversal.
- **Derive+verify:** `ELBO = log evidence − KL(q‖posterior)`; EM = coordinate ascent on ELBO; VI variance underestimation is structural.
- **Sources:** C-B §7.2 (EM/latent); booklet ch12 §12.4 (INLA as deterministic approx); ISLP §10 (autoencoders/DL context).
- **Code:** `m16_vi_em.py` — EM mixture; ADVI-vs-NUTS; minimal VAE (numpy/torch, tiny).
- **Deps:** M10, M14.

## Part D — The models that run in production

### M17 — Bayesian regression end-to-end (linear, logistic, robust)
- **Promise:** you can ship a regression with honest coefficient uncertainty and outlier resistance.
- **Examples:** (a) Conjugate Normal-Inverse-Gamma linear regression; coef credible intervals coincide with OLS CIs under a flat prior (verify). (b) Student-t likelihood (`ν=4`) vs Normal on data with 3 injected outliers — t downweights them. (c) PyMC Bayesian logistic with weakly-informative priors; posterior-predictive calibration curve.
- **Derive+verify:** NIG conjugacy; robustness = heavy-tailed likelihood = Normal scale-mixture; calibration by PPC.
- **Sources:** booklet ch05 §5.1 (regression), ch08; C-B §7, §11 (regression); ISLP §3–4.
- **Code:** `m17_bayes_regression.py` — NIG linear; robust-t; PyMC logistic + calibration.
- **Deps:** M7, M14.

### M18 — Hierarchical models & partial pooling (the killer app)
- **Promise:** you can pool information across groups and beat both no-pooling and complete-pooling on held-out error.
- **Examples:** (a) 8 schools `y=[28,8,-3,7,-1,1,18,12]`, `σ=[15,10,16,11,9,11,10,18]`: no-pool vs complete-pool vs partial; posterior for `τ`. (b) Small-area estimation (booklet ch09): county rates with tiny samples shrink to state mean, MSE gain quantified. (c) 18 baseball players' early AVG shrink toward `.270`; predict rest-of-season, beat raw AVG.
- **Derive+verify:** partial-pooling weight `= 1/(1+σ²/τ²)`; hierarchical model = James–Stein made adaptive (ties back to M4); funnel reparam from M15.
- **Sources:** booklet ch07 (hierarchical), ch09 (normal-means, small-area, empirical vs full Bayes, benchmarking); C-B §4.4; Montgomery ch3, ch13 (random effects).
- **Code:** `m18_hierarchical.py` — 8-schools in PyMC (non-centered); shrinkage figure.
- **Deps:** M4, M15, M17.

### M19 — GLMs, counts, and overdispersion
- **Promise:** you can fit the right likelihood for counts/rates and detect when a Poisson is lying.
- **Examples:** (a) Poisson regression on bikeshare-like counts; detect `var≈3×mean` → switch to Negative-Binomial. (b) Zero-inflated Poisson with 40% structural zeros — recover the mixing weight. (c) Varying-intercept (hierarchical) logistic on grouped binary; partial-pool group rates.
- **Derive+verify:** GLM = exp-family + link (ties to M5); overdispersion diagnostic; NB = Poisson–Gamma mixture (ties to M6).
- **Sources:** ISLP §4.6 (GLMs, Poisson); booklet ch11 §11.5 (Poisson regression), ch13 §13.1 (multinomial-Dirichlet); Montgomery §15.1.2.
- **Code:** `m19_glm.py` — Poisson→NB; ZIP; hierarchical logistic.
- **Deps:** M5, M18.

### M20 — Experimental design & sequential experiments
- **Promise:** you can design an experiment to answer a question with the fewest runs and adapt as data arrives.
- **Examples:** (a) Two-sample A/B (Montgomery ch2): sample size to detect `Δ=0.2σ` at power .8; Bayesian assurance vs frequentist power. (b) `2³` factorial (Montgomery ch6): estimate 3 main effects + interactions from 8 runs; posterior on effect sizes. (c) Thompson-sampling bandit on 3 arms beats ε-greedy on cumulative regret over 2000 rounds.
- **Derive+verify:** power/assurance; factorial effect = contrast; Thompson sampling = posterior-matching exploration; D-optimality note.
- **Sources:** Montgomery ch2 (comparative), ch5–6 (factorial/`2ᵏ`), ch9.6 (optimal design); booklet ch04 §4.1 (combining sources); ISLP §13 (testing).
- **Code:** `m20_design.py` — power curve; `2³` effects; bandit-regret sim.
- **Deps:** M7, M9.

### M21 — Nonparametric Bayes: Gaussian processes & Dirichlet-process mixtures
- **Promise:** you can fit functions and clusterings whose complexity grows with the data, with calibrated uncertainty.
- **Examples:** (a) GP regression on 20 noisy `sin` points; predictive bands widen off-data; length-scale posterior. (b) GP vs ridge/spline (ISLP ch7): same mean fit, honest error bars. (c) DP mixture (booklet ch14) on galaxy-velocity-like 1D data: infer 3–6 clusters without fixing K; CRP/stick-breaking.
- **Derive+verify:** GP = Gaussian prior over functions, posterior in closed form; DP via Chinese-restaurant / stick-breaking; concentration `α` controls #clusters.
- **Sources:** booklet ch13 §13.3–13.4, ch14 (Dirichlet process, Pólya urn, DPM); ISLP §7 (splines/GAM), §12.4 (clustering); C-B §4.4.
- **Code:** `m21_nonparametric.py` — GP regression; DP-mixture Gibbs (small n for <180s).
- **Deps:** M12, M16.

### M22 — Deep learning & generative models as Bayesian inference (capstone)
- **Promise:** you can put calibrated uncertainty on a neural net and explain diffusion/LLM sampling in the four-line frame.
- **Examples:** (a) Deep ensemble (5 MLPs) on regression: ensemble spread ≈ epistemic uncertainty; ECE beats a single net. (b) MC-dropout as VI: 100 test-time passes → predictive band on the two-moons boundary. (c) Diffusion: forward Ornstein–Uhlenbeck SDE + reverse-time SDE (Lawler Itô/Girsanov), score `=∇log p`, generate a 2-D swiss-roll; last-layer Laplace on a small net.
- **Derive+verify:** deep ensembles ≈ posterior marginalization; dropout ≈ Bernoulli variational posterior; reverse-time SDE from Girsanov; SGD-with-noise ≈ Langevin (ties to M14); softmax temperature = posterior tempering.
- **Sources:** ISLP §10 (DL, backprop, dropout, double descent); Lawler ch2–3 (BM, Itô), ch5 (Girsanov/change of measure); booklet insert-bda-hmc-stan (Langevin/HMC).
- **Code:** `m22_deep_bayes.py` — ensemble+ECE; MC-dropout; 2-D diffusion + last-layer Laplace (torch, tiny nets).
- **Deps:** M10, M14, M16, M21.

---

## Twelve must-not-miss intuition nuggets

1. **The prior is worth κ pseudo-observations.** `Beta(a,b)` = `a+b` prior trials; watch the posterior mean slide MLE→prior as `n` shrinks. Reframes "how strong is my prior" as a countable quantity. (M3)
2. **Shrinkage is a free lunch in ≥3 dimensions.** James–Stein dominates the MLE even for *unrelated* means — the fact that legitimizes every hierarchical model. Simulate the dominance and its collapse at `p≤2`. (M4)
3. **Two uncertainties, only one shrinks.** Predictive variance = aleatoric (`σ²`, irreducible) + epistemic (`(1−λ)δ²`, →0 with data). Production dashboards that quote one number are hiding which. (M6)
4. **Base rates dominate accuracy.** `sens=.99, spec=.95, prev=.001 → PPV=1.9%`. The likelihood ratio, not the accuracy, moves the posterior. (M0/M7)
5. **Significance is not evidence (Lindley).** At `n=10⁶`, `p=.05` coexists with a Bayes factor of 19:1 *for* the null, and the direction flips with `n`. (M9)
6. **Confidence ≈ credible only asymptotically.** Bernstein–von Mises makes them agree at large `n`; at small `n`/boundaries/strong priors they diverge, and *which you want* depends on conditioning on the data you actually saw. (M8)
7. **Cross-validating λ is empirical Bayes.** Ridge's `λ=σ²/τ²`; the CV-optimal `λ` estimates your prior variance — you were doing Bayes all along. (M2)
8. **The interval encodes the loss.** A 95% HPD interval is shorter than the equal-tailed one and can be *disjoint* for multimodal posteriors — the shape is a decision, not a convention. (M7/M8)
9. **Report ESS, not draw count.** 100k autocorrelated draws can be worth 200 independent ones; `MCSE=sd/√ESS`. The single most common way practitioners fool themselves. (M11/M15)
10. **Geometry, not the model, is the bug.** Neal's funnel: the identical model, re-coordinatized (non-centered), mixes 100× better and stops diverging. (M15/M18)
11. **Deep ensembles are approximate Bayesian marginalization.** Averaging 5 independently trained nets ≈ sampling the weight posterior — which is *why* they calibrate better than one net. (M22)
12. **Marginalize, don't optimize, over nuisances.** Integrating out a Gamma-distributed variance turns a Normal into a Student-t — robustness for free, no outlier heuristics. (M17)

## Eight failure modes this outline is built to avoid

1. **"Derives conjugacy but never makes a decision."** → Decision theory (M7) arrives immediately after the predictive, *before* any MCMC; every inference module ends by executing line (2)–(4) — a threshold, an order quantity, an interval-as-loss.
2. **Bayesian-vs-frequentist tribalism.** → Frequentist results enter as *audits/limits* of the same machine: MLE=MAP (M1), BvM & bootstrap-as-posterior (M8), WAIC=CV (M9). Genuine disagreements (Lindley, stopping rules, conditioning) are shown with numbers, no straw men.
3. **MCMC eats the whole course.** → Five modules of exact/approximate inference (M3–M5 conjugate, M10 Laplace, M16 VI/EM) frame and bound the four MCMC modules; MCMC is explicitly "when conjugacy fails."
4. **Black-box PyMC with no mechanism.** → Gibbs (M12) and MH (M13) are hand-coded from full conditionals and verified against conjugate truth *before* PyMC/NUTS (M14) is allowed.
5. **Toy examples, no failure cases.** → Every sampler module ships a deliberately broken run (`ρ=0.9` Gibbs, Neal's funnel, rare-event IS collapse) with predict-then-verify of the pathology and its fix.
6. **Uncertainty quoted, never calibrated.** → Coverage simulation and PPCs (M6, M8), ECE for the neural net (M22); "95%" must be earned on held-out replicates.
7. **"It can be shown" hand-waving.** → BvM, CLT/delta method, James–Stein dominance, spectral-gap mixing are all *simulated*, and per the brief every stated number is printed by a code block.
8. **DL/GenAI ghettoized in a final survey.** → Regularization-as-prior (M2), VAE-as-VI (M16), and diffusion/BNN/ensembles (M22) are load-bearing, with DL callbacks threaded throughout (weight decay, dropout, SGD-as-Langevin, softmax temperature).

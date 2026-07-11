# DRAFT Outline v0 — "The Bayesian Spine: Statistical and Machine Learning from One Principle"

Status: orchestrator's draft, pre-panel. Each module lists: Promise (what you can do afterward), core examples (specific), key results (derive/simulate/cite), sources, code artifacts. Format contract per module lives in STYLE.md.

Running thread — the whole curriculum is four sentences:
1. A model is a joint distribution p(unknowns, knowns).
2. Inference is conditioning: p(unknowns | knowns).
3. Prediction is marginalization: p(new | knowns) = ∫ p(new | unknowns) p(unknowns | knowns) d(unknowns).
4. A decision minimizes posterior expected loss.
Everything else — MLE, confidence intervals, ridge, cross-entropy, Kalman filters, A/B tests, deep ensembles — is a special case, an approximation, or an audit of these four lines.

---

## Part 0 — Orientation

### 00. The Four-Line Course (orientation + notation)
- **Promise:** You can state the unified view, and for any named procedure (MLE, CI, ridge, dropout) say which of the four lines it approximates.
- **Examples:** one fully-worked micro-example (biased-coin inference → prediction → bet sizing) executing all four lines in ~40 lines of numpy; table mapping 15 familiar procedures to their Bayesian readings.
- **Key results:** "random = unknown to you" (epistemic vs aleatory as bookkeeping, not metaphysics); why "is θ random?" is a modeling choice, not a philosophical commitment.
- **Sources:** booklet ch. 0–1; C-B ch. 1.
- **Code:** the 40-line four-line demo; notation table; how to run modules (`tools/run_module.py`).

## Part I — Foundations re-grounded

### 01. Probability as the Logic of Uncertainty
- **Promise:** You can defend (and attack) both readings of probability, and explain why exchangeability — not philosophy — is what makes parameters exist.
- **Examples:** Dutch-book made concrete (explicit book of bets with guaranteed loss table); frequency-matching (calibration) simulation; de Finetti: simulate an exchangeable-but-not-iid sequence (mixture of coins), show empirical freq converges to a *random* limit = θ; the crooked mint (two-level randomness).
- **Key results:** Cox/Dutch-book sketch (coherence ⇒ probability axioms); de Finetti's representation theorem stated precisely, simulated, not proved; conditional probability as the *only* coherent update (brief).
- **Sources:** booklet ch. 1–2; C-B ch. 1.
- **Code:** Dutch book payoff matrix; exchangeability simulation; posterior-of-limit-frequency demo.

### 02. Conditioning Is Inference
- **Promise:** Given any small discrete generative story you can compute the posterior exactly, by hand and by enumeration code, and diagnose base-rate errors on sight.
- **Examples:** medical test (sens .99 / spec .95 / prev .001 → PPV ≈ 1.9%) hand-computed then simulated with 10⁷ patients; German tank problem (posterior under uniform prior vs UMVU estimator, exact numbers, both simulated); Monty Hall as a conditioning discipline (enumerate the joint); naive-Bayes spam filter on a toy corpus.
- **Key results:** Bayes' rule as ratio of joints (nothing more); likelihood = the data's fingerprint on hypothesis space; posterior odds = prior odds × likelihood ratio; sequential = batch updating.
- **Sources:** booklet ch. 2; C-B ch. 1.
- **Code:** exact enumeration engine for finite hypothesis spaces (reused later); tank-problem estimator shootout (risk curves).

### 03. Distributions Are Generative Stories
- **Promise:** For each standard family you can tell the story that generates it, derive its key facts from the story, and pick families by matching stories — not by habit.
- **Examples:** Poisson process on a timeline → Poisson counts, Exponential gaps, Gamma waits (derived + simulated from uniform order statistics); CLT as an emergent story + where it fails (Cauchy sample means don't settle — simulate); max-ent derivations (support+mean → exponential; mean+variance → normal); Beta as "pseudo-count" posterior; exponential family form and why sufficiency drops out of it.
- **Key results:** exponential families: natural parameter, log-partition derivatives = cumulants (derive, verify numerically); conjugacy = closure of exponential families under Bayes.
- **Sources:** C-B ch. 3 (full text); booklet ch. 3.
- **Code:** Poisson-process construction from scratch; cumulant-vs-numerical-derivative check; heavy-tail CLT failure gallery.

### 04. Likelihood: the Data's Voice
- **Promise:** You can factorize likelihoods, find sufficient statistics, state the likelihood principle, and explain — with numbers — why two experimenters with identical data can report different p-values but must report identical posteriors.
- **Examples:** the stopping-rule pair: Binomial(12) with 9 successes vs Negative-Binomial (sample until 3 failures) — identical likelihood ∝ θ⁹(1−θ)³, p-values 0.073 vs 0.033 (compute both exactly), posterior identical (plot); sufficiency: (Σx) for Bernoulli — simulate that conditioning on Σx makes data order irrelevant; ancillarity teaser.
- **Key results:** factorization theorem (stated, used); likelihood principle (stated; consequences, not dogma — note where frequentist design-stage reasoning still cares about stopping rules); MLE as "peak of the data's voice" — a summary, not yet a philosophy.
- **Sources:** C-B ch. 6 (full text); Berger & Wolpert cited by concept.
- **Code:** exact p-value computations both designs; likelihood overlay; sufficiency shuffle test.

## Part II — Exact Bayesian inference

### 05. Conjugate Updating End-to-End
- **Promise:** You can carry the five workhorse conjugate pairs through prior → posterior → posterior predictive by hand, and read any posterior as "prior pseudo-data + real data".
- **Examples:** Beta-Binomial (A/B test with 41/1000 vs 57/1000 conversions — full analysis: P(B>A), expected uplift, risk); Gamma-Poisson (call-center rates, overdispersed predictive = negative binomial); Normal-Normal (measurement fusion = precision-weighted average — derive the Kalman gain in embryo); Normal-Inverse-Gamma (unknown mean and variance → posterior predictive is Student-t: derive why tails widen); Dirichlet-Multinomial (language-model smoothing = add-α as a prior).
- **Key results:** posterior mean = (prior precision · prior mean + data precision · MLE)/(total precision) — the master shrinkage formula; predictive is *always* wider than plug-in (law of total variance, derive + simulate); sequential=batch.
- **Sources:** booklet ch. 3–5, ch. 8; C-B ch. 7.
- **Code:** conjugate library (reused across the course); A/B analysis returning P(B>A)=…, E[uplift]=…; plug-in vs predictive coverage simulation.

### 06. Estimates and Intervals Are Decisions
- **Promise:** You can derive which point estimate each loss implies, translate any regularizer into its prior, and articulate exactly what a confidence interval does and does not promise — with a demonstration where the difference is dramatic.
- **Examples:** L2→posterior mean, L1→median, 0-1→mode: derive, then verify on a skewed Gamma posterior; ridge = Gaussian prior MAP, lasso = Laplace prior MAP (derive the correspondence exactly; note honestly that the lasso point estimate is a *mode*, and the Laplace-prior posterior mean ≠ sparse); the two-point uniform CI pathology (X₁,X₂ ~ U(θ−½,θ+½): the 50% CI that is *certainly* right when |X₁−X₂|>… and certainly ambiguous otherwise — conditional vs unconditional guarantees, simulated); coverage of Bayesian credible intervals under a well-specified prior (exact match — simulate) and misspecified prior (graceful degradation — simulate).
- **Key results:** decision-theoretic derivations of mean/median/mode; credible vs confidence semantics; where they numerically coincide (preview of BvM).
- **Sources:** C-B ch. 7, 9; booklet ch. 8.
- **Code:** loss-vs-estimator simulation; interval pathology demo; coverage matrices.

### 07. Priors: What They Are and Aren't
- **Promise:** You can choose, defend, and stress-test a prior: conjugate for algebra, weakly-informative for stability, Jeffreys for invariance — and you can show with simulation when it matters and when it washes out.
- **Examples:** derive Jeffreys for Bernoulli (Beta(½,½)) from Fisher information and from reparameterization invariance (compute the same posterior through the log-odds parameterization); improper-prior failure case (posterior fails to normalize — concrete integral); prior predictive checks: simulate fake data from prior+likelihood, catch an absurd prior *before* seeing data (basketball shooting % example); sensitivity envelope: posterior under 5 defensible priors at n=10 vs n=10,000.
- **Key results:** priors as part of the model (same epistemic status as the likelihood — which is also chosen); regularization-as-prior for the ML reader; asymptotic prior washout and its exceptions (unidentified parameters never wash out — simulate one).
- **Sources:** booklet ch. 5–7; BDA3 by concept.
- **Code:** prior predictive check harness (reused); sensitivity fan charts; Jeffreys invariance numerical check.

### 08. The Frequentist Bridge
- **Promise:** You can run the standard asymptotic machine (MLE, Fisher information, Wald intervals), state Bernstein–von Mises, and explain Stein's paradox — and you leave knowing frequentist evaluation is a quality audit Bayesians should pass, not an enemy camp.
- **Examples:** MLE asymptotics simulated (sampling distribution vs N(θ, I⁻¹/n) overlay); BvM: overlay the *posterior* (one dataset) on the *sampling distribution of the MLE* (many datasets) — watch them merge as n grows; Stein's paradox at d=10: simulate MSE of MLE vs James–Stein estimator, then re-derive JS as empirical-Bayes shrinkage (Normal-Normal); bootstrap ↔ Bayesian bootstrap (Rubin) — resample weights vs Dirichlet weights, overlay; complete-class statement in plain words.
- **Key results:** Fisher information; Cramér–Rao (stated, verified numerically); BvM (stated with regularity caveats; simulated); admissibility: every admissible rule is (a limit of) Bayes rules — the punchline that the "special case" framing is a theorem, not propaganda.
- **Sources:** C-B ch. 7, 10 (full text); Efron–Morris by concept.
- **Code:** asymptotics lab; JS-vs-MLE risk simulation; two bootstraps.

## Part III — Computation: integration is the bottleneck

### 09. Monte Carlo Fundamentals
- **Promise:** You can replace any integral with a sample average, attach a correct error bar to it, and recognize (from weight diagnostics) when importance sampling is silently failing.
- **Examples:** posterior summaries from samples (mean, intervals, P(θ>c), transformations — the "samples are a lingua franca" point); MC error bars via CLT with verification across 1,000 replications; importance sampling: works (t-proposal for normal target), then fails catastrophically (normal proposal for t-target — weight histogram, ESS collapse, the single-sample-dominates pathology); rejection sampling with acceptance-rate accounting.
- **Key results:** LLN/CLT for MC; ESS = n/(1+var of normalized weights) heuristics; why "just sample from the posterior" became the paradigm.
- **Sources:** booklet ch. 8; MCMT ch. 1 by concept.
- **Code:** MC error-bar verifier; IS diagnostics dashboard; rejection sampler.

### 10. Metropolis–Hastings from Scratch
- **Promise:** You can write a correct MH sampler in ~30 lines, prove to yourself it targets the right distribution, tune it, and read trace/ACF/R̂/ESS diagnostics like a practitioner.
- **Examples:** just-enough Markov chain theory: stationarity, detailed balance (prove MH satisfies it in 6 lines), ergodicity in words (MCMT bridge: mixing time, spectral gap intuition — one figure); RW-MH on a bimodal 1-D target (watch it fail to mix between modes); step-size sweep → acceptance-rate vs ESS curve (the 0.234 lore, shown empirically, stated as an asymptotic product-target result); split-R̂ catching a stuck chain that single-chain diagnostics miss.
- **Key results:** detailed balance ⇒ stationarity (proved); why burn-in is a red herring vs initialization bias (brief, honest); diagnostics are necessary-not-sufficient (construct a fooling example).
- **Sources:** booklet ch. 11, 15; MCMT ch. 1–5 by concept.
- **Code:** 30-line MH; tuning lab; diagnostics suite built by hand (R̂, ESS via autocorrelation) then checked against ArviZ.
 
### 11. Gibbs Sampling and Data Augmentation
- **Promise:** You can derive full conditionals for conjugate-structured models, implement Gibbs, recognize when it will crawl, and use data augmentation to make non-conjugate problems conjugate.
- **Examples:** Normal model with unknown (μ, σ²) — derive both conditionals, implement, compare to the exact NIG posterior from module 05 (they must agree — a built-in correctness audit); Bayesian linear regression via Gibbs; bivariate normal with ρ=0.99: Gibbs zigzag visualized, ESS collapse quantified vs ρ; Albert–Chib probit data augmentation (derive: truncated-normal latents restore conjugacy).
- **Key results:** Gibbs as componentwise MH with acceptance 1 (derive); convergence rate ↔ posterior correlation (empirical scaling plot); augmentation as "invent latent data that makes the model conjugate".
- **Sources:** booklet ch. 10; C-B ch. 7.
- **Code:** Gibbs-vs-exact overlay; ρ-sweep ESS plot; probit sampler on synthetic data with recovery check.

### 12. HMC and NUTS: Geometry Wins in High Dimension
- **Promise:** You understand *why* random-walk methods die with dimension and gradients rescue you; you can implement leapfrog HMC on paper-sized problems and drive PyMC on real ones, reading divergences as geometry warnings.
- **Examples:** the typical set: norms of d-dim standard normal samples concentrate at √d (simulate d=1…1000) — "the donut", and why the mode is nowhere near the mass; RW-MH ESS vs dimension (power-law decay, measured) vs HMC (flat-ish); from-scratch leapfrog HMC (~50 lines) on a correlated 2-D Gaussian and on the banana (Rosenbrock) target; Neal's funnel: divergences in centered eight-schools-like geometry, fixed by non-centered reparameterization (before/after divergence counts); energy conservation error vs step size (the leapfrog stability boundary, shown).
- **Key results:** Hamiltonian dynamics preserve the target (stated, checked numerically via energy error); why momentum + gradient = coherent long-distance moves; SGLD teaser: Langevin SDE discretization (Lawler bridge, 10 lines).
- **Sources:** booklet insert-bda-hmc-stan (BDA3 excerpt); booklet ch. 15; Lawler by concept; Neal's HMC chapter by concept.
- **Code:** donut demo; dimension-scaling shootout; leapfrog HMC; PyMC funnel with divergence scatter; non-centered fix.

### 13. Deterministic Approximations: Laplace, EM, Variational Inference
- **Promise:** You can pick the right cheap approximation for a given posterior, derive the ELBO three ways, implement CAVI where truth is known, and predict VI's failure mode (variance underestimation) before you see it.
- **Examples:** Laplace approximation on a Beta posterior (good at n=200, bad at n=5 — quantify KL); EM derived as coordinate ascent on the ELBO, implemented for a 2-component GMM with the responsibilities made visible; CAVI for Normal-Inverse-Gamma target (compare against module 05 exact answer: mean spot-on, variance too small — measure the deficit); PyMC ADVI vs NUTS on the same model (time vs accuracy frontier).
- **Key results:** ELBO = log evidence − KL(q‖p) (derive); mean-field ⇒ underdispersion (derive for the Gaussian case, then observe); EM = VI with point-mass q over parameters (derive the reduction); when to trust VI (point predictions, embeddings) vs not (tail risk, intervals).
- **Sources:** booklet ch. 12–13; Bishop by concept; BDA3 ch. 13 by concept.
- **Code:** Laplace-vs-exact KL curve; GMM-EM with log-likelihood ascent plot; CAVI from scratch; ADVI-vs-NUTS benchmark table.

## Part IV — Statistical learning, re-founded

### 14. Regression I: Bayesian Linear Models
- **Promise:** You can derive the full Bayesian linear regression posterior, produce honest predictive intervals that widen off-support, and translate ridge/lasso/elastic-net into priors without notes.
- **Examples:** conjugate normal regression (known σ² then NIG): posterior over the line visualized as sampled lines through data; predictive intervals vs sklearn point predictions on extrapolation (the flaring trumpet plot); ridge path = MAP path as prior precision sweeps (exact correspondence table λ ↔ τ²); robust regression: swap Normal for Student-t likelihood, watch one outlier stop hijacking the fit (side-by-side); basis expansion (polynomials/splines) with the bias-variance tradeoff re-read as prior strength.
- **Key results:** posterior covariance (XᵀX/σ² + Σ₀⁻¹)⁻¹ derived and dissected; predictive variance = aleatoric + epistemic terms (decompose numerically); "regularization is a prior you refuse to name".
- **Sources:** ISLP ch. 3, 6; booklet ch. 8–9; C-B ch. 11–12 by concept.
- **Code:** regression engine from scratch; trumpet plot; λ↔τ² verification; t-robustness demo.

### 15. Regression II: GLMs and Classification
- **Promise:** You can build GLMs generatively (pick response story → link), fit Bayesian logistic regression three ways (Laplace, MH, PyMC), and explain to a DL engineer why cross-entropy training *is* MLE of a categorical GLM.
- **Examples:** logistic regression on separable data: MLE diverges (weights → ∞, show it), any proper prior fixes it — the ML "why do we need weight decay" question answered generatively; Laplace vs MCMC posterior for logistic coefficients (overlay); calibration curves: a well-specified Bayesian model is calibrated, an overconfident one isn't (reliability diagrams); naive Bayes vs logistic regression = generative vs discriminative (Ng–Jordan crossover simulated: NB wins small-n, logistic wins large-n); Poisson regression with exposure offsets (rate modeling done right).
- **Key results:** GLM = exponential family response + linear predictor through link (the recipe); cross-entropy = categorical NLL (two-line derivation); posterior predictive class probabilities ≠ plug-in σ(x·ŵ) — integrate, don't plug (quantify the difference where it matters: near the boundary, small n).
- **Sources:** ISLP ch. 4; booklet ch. 8; Ng–Jordan 2001 by concept.
- **Code:** GLM builder; separation demo; three-way fit comparison; calibration harness (reused in module 23).

### 16. Hierarchical Models: the Crown Jewel
- **Promise:** You can build multilevel models that share strength across groups, explain shrinkage quantitatively, and recognize hierarchical structure hiding inside "random effects", "empirical Bayes", and James–Stein.
- **Examples:** eight schools, complete treatment: no-pooling / complete-pooling / partial-pooling estimates on one axis (the shrinkage picture); the funnel geometry (module 12 callback) and the non-centered fix; batting averages (Efron–Morris): early-season shrinkage beats raw averages at predicting rest-of-season — quantified; radon-style synthetic dataset with pandas (counties, varying intercepts, group-level predictors); hierarchical pseudo-count reading: group posterior = precision-weighted blend of group data and population.
- **Key results:** partial pooling formula (derive from Normal-Normal); why hierarchical predictive beats both extremes (simulate held-out risk across pooling spectrum); empirical Bayes = point-estimated hyperprior (when fine, when overconfident); mixed-effects models = this, under another name.
- **Sources:** booklet ch. 9; Efron–Morris by concept; Gelman & Hill by concept.
- **Code:** eight-schools from scratch (Gibbs or HMC) + PyMC; pooling-spectrum risk simulation; shrinkage plots.

### 17. Model Checking, Comparison, and the Testing Question
- **Promise:** You can audit a model with posterior predictive checks, compare models with LOO/WAIC and Bayes factors (knowing each one's failure modes), and translate between p-values and evidence honestly.
- **Examples:** PPC catches overdispersion: Poisson fit to negative-binomial data, test statistic = variance/mean ratio, posterior predictive p-value ≈ 0 (then the NB fix passes); marginal likelihood as built-in Occam: polynomial degree selection where evidence peaks at true degree while train MSE keeps falling (the Occam factor computed explicitly); Lindley's paradox with real numbers: n=10,000, θ̂ slightly off null → p=0.01 but BF favors the null — dissect why (prior spread on the alternative); BF prior-sensitivity table (same data, BF from 0.5 to 15 as prior widens — the honest caveat); PSIS-LOO via ArviZ compared to brute-force LOO on a small model; p-value calibration: simulate the distribution of p under H₀ (uniform) and under realistic effects — what p=0.049 actually implies about replication.
- **Key results:** PPC logic (self-consistency audit, not NHST); evidence = prior predictive density (derive the Occam factor); WAIC↔LOO asymptotic agreement (stated, verified empirically); why BFs need real priors and CV doesn't; model averaging vs selection (predictive stacking mention).
- **Sources:** booklet ch. 12–13; BDA3 ch. 6–7 by concept; ISLP ch. 5.
- **Code:** PPC harness; explicit evidence integrals (quadrature) for polynomial models; Lindley dissection; LOO comparison.

### 18. Latent Structure: Mixtures, EM's Home Turf, and the Dirichlet Process
- **Promise:** You can treat cluster labels as unknowns like any other, fit mixtures by EM and by Gibbs, handle label switching, and let the data choose the number of clusters with a DP.
- **Examples:** 2-D Gaussian mixture: EM (module 13 callback) vs Gibbs with conjugate priors — posterior uncertainty in the labels that EM's point estimates hide; label switching shown concretely (trace of μ₁ swapping) and handled (relabeling/identifiability constraint); zero-inflated Poisson (real-world count story) via augmentation; CRP simulated from scratch (rich-get-richer table dynamics, E[#clusters] ≈ α log n verified); stick-breaking construction (booklet's handwritten insert!) → truncated-DP mixture fit letting K grow with data.
- **Key results:** mixtures = marginalized discrete latents (the general pattern behind HMMs, topic models, VAEs); EM finds modes, Bayes finds distributions over partitions; DP: derive E[#clusters]; exchangeability of CRP (de Finetti callback).
- **Sources:** booklet ch. 14 + stick-breaking insert; Neal 2000 by concept.
- **Code:** EM-vs-Gibbs mixture lab; CRP simulator; truncated-DP fit with cluster-count posterior.

### 19. Gaussian Processes: Priors over Functions
- **Promise:** You can go from "regression with basis functions" to "prior over functions" without mystery, implement exact GP regression in ~20 numpy lines, tune kernels by marginal likelihood, and connect GPs to kernel methods and wide neural nets.
- **Examples:** finite Gaussian-weight basis regression → kernel k(x,x′)=φ(x)ᵀΣφ(x′) (compute both routes, verify identical predictions); samples from GP priors across kernels (RBF/Matérn/periodic gallery — what smoothness assumptions *look like*); exact GP posterior on 1-D data: mean, bands, and the collapse-at-data-points behavior; marginal-likelihood kernel tuning with the decomposition fit-vs-complexity made explicit (Occam again); Bayesian optimization mini-loop (expected improvement) finding a 1-D optimum in 8 evaluations (module 22 bridge); NNGP one-figure teaser: wide 1-layer net's prior over functions ≈ GP (simulate widths 1, 10, 1000).
- **Key results:** GP = consistent Gaussian marginals (Kolmogorov view, light); posterior mean = kernel ridge regression (derive — the frequentist special case, again); O(n³) honesty + inducing-point mention.
- **Sources:** ISLP by concept; Rasmussen & Williams by concept; booklet ch. 14.
- **Code:** 20-line GP; kernel gallery; ML-II tuning; BayesOpt loop; NNGP width sweep.

## Part V — Sequential data and decisions

### 20. State Space: Filtering Is Just Bayes on a Conveyor Belt
- **Promise:** You can derive the Kalman filter as recursive conjugate updating (nothing new — module 05's Normal-Normal on repeat), implement it, and know when to reach for particle filters.
- **Examples:** 1-D tracking (position+velocity): Kalman derived step by step as predict (marginalize) / update (condition), gain = the shrinkage weight again; parameter inference vs state inference distinguished; discretized Ornstein–Uhlenbeck process (Lawler bridge) filtered from noisy observations; bootstrap particle filter on a nonlinear/non-Gaussian toy (stochastic volatility-lite), weight degeneracy shown, resampling fix shown.
- **Key results:** Kalman = closed-form sequential Bayes (full derivation); predict/update = marginalize/condition (the four lines again); particle filter = sequential importance sampling + resampling (module 09 callback).
- **Sources:** Lawler ch. on OU by concept; booklet ch. 8; Särkkä by concept.
- **Code:** Kalman from scratch + trajectory plots; OU filtering; 60-line particle filter with ESS trace.

### 21. Decisions and Bandits: Uncertainty You Can Act On
- **Promise:** You can turn any posterior into an action via a loss matrix, price information, and implement Thompson sampling — understanding why posterior sampling solves explore/exploit almost embarrassingly well.
- **Examples:** classification threshold from a utility matrix (cancer screening numbers: why 0.5 is almost never the right threshold — expected-loss curves); A/B test as decision problem: expected loss of ship-vs-continue, when to stop (module 05's conjugate machinery driving a real decision); Thompson vs ε-greedy vs UCB on Bernoulli bandits: cumulative regret curves over 10,000 pulls (Thompson's posterior-sampling logic derived in 5 lines); expected value of information: compute EVSI for "should we run 1,000 more samples?" — information priced in expected-loss units.
- **Key results:** Bayes decision rule minimizes posterior expected loss (derive); admissibility connection (module 08 callback); Thompson sampling = probability matching on the posterior over "which arm is best"; exploration = acting under parameter uncertainty rather than plug-in certainty.
- **Sources:** C-B ch. 8, 10 (decision-theory sections, full text); booklet ch. 8; Russo et al. tutorial by concept.
- **Code:** threshold optimizer; A/B stopping simulator; bandit tournament with regret plots; EVSI calculator.

### 22. Experimental Design and Causal Questions
- **Promise:** You can justify randomization in Bayesian terms, compute power's Bayesian sibling (assurance) by simulation, design adaptively without corrupting inference, and treat causal inference as inference over missing potential outcomes.
- **Examples:** why randomize if you're Bayesian: confounded vs randomized data-generating processes, same model — posterior lands wrong under confounding, right under randomization (ignorability made computational); power vs assurance: P(study succeeds) under a point alternative vs averaged over the prior (Montgomery power table ↔ preposterior simulation); sequential design: simulate optional stopping — posterior remains valid (likelihood principle, module 04 callback) while p-value error rates inflate 3–4× (both shown, honestly discussed: what *is* compromised for the Bayesian: calibration under selective reporting); factorial design as regression with interactions (Montgomery 2³ example refit hierarchically — effect sparsity as a prior); potential outcomes as missing data: simulate a backdoor scenario, adjust correctly vs incorrectly.
- **Key results:** ignorability = design gives you the likelihood you think you have; assurance = ∫ power × prior; expected-information-gain design (one worked D-optimal-style example); "no causes in, no causes out" — models can't conjure identification.
- **Sources:** Montgomery ch. 1–6, 12 (full text); booklet ch. 6–7; Rubin/Imbens by concept; Lindley by concept.
- **Code:** confounding-vs-randomization simulator; assurance-by-simulation; optional-stopping calibration lab; 2³ factorial hierarchical refit.

## Part VI — The modern synthesis

### 23. Bayesian Lenses on Deep Learning and Generative AI
- **Promise:** You can read modern ML practice — weight decay, ensembles, VAEs, diffusion, LLM sampling — as approximate Bayesian moves, and know which parts of that reading are theorems, which are heuristics, and which are open.
- **Examples:** weight decay = Gaussian prior (theorem, 3 lines) and label smoothing / early stopping as regularizing priors (heuristic — say so); deep ensembles ≈ multi-modal posterior mixture: 5 small MLPs on a toy regression give calibrated-ish bands where a single net is overconfident (build in numpy/sklearn, no GPU); VAE ELBO term-by-term = module 13's ELBO with amortized q (derivation + annotated pseudo-code; no training run); diffusion models as hierarchical latent chains + score matching ↔ reverse SDE (Lawler bridge, conceptual figure, cite Song et al.); LLM next-token = categorical MLE at scale; in-context learning as implicit posterior predictive (present the exchangeability argument + cite Xie et al. — labeled "active research", with an honest limits box); temperature scaling as post-hoc calibration (module 15's harness reused on an overconfident classifier).
- **Key results:** what's theorem vs heuristic vs open — an explicit three-column table; SGD-as-sampling sketch (SGLD, module 12 callback); marginal-likelihood/Occam view of generalization (module 17 callback); conformal prediction as a frequentist wrapper achieving coverage without a model — the audit-tool framing again.
- **Sources:** booklet insert (HMC/Stan); Lawler by concept; MacKay ch. 28, Murphy PML2, Song/Ho, Xie et al. by concept.
- **Code:** ensemble-vs-single calibration lab (CPU-friendly); temperature scaling; ICL toy: exchangeable sequence prediction with a fitted mixture vs true posterior predictive.

### 24. One Theory, Two Audits — an Honest Closing
- **Promise:** You can articulate, with examples you have personally run, what is genuinely settled by the Bayesian view, what frequentist auditing irreplaceably adds, and how working statisticians actually blend them.
- **Examples:** the ledger, each entry pointing back to a module where you *ran* it: nuisance-parameter marginalization vs profiling (run both on NIG); stopping rules (module 22's lab); calibration audits catching a bad prior (module 06); Lindley (module 17); the "ML zoo" audit table: 20 methods (OLS, ridge, lasso, logistic, SVM, trees, RF, boosting, k-means, PCA, GPs, Kalman, dropout, ensembles, conformal…) × (Bayesian reading | exactness: theorem/approx/none | what the reading buys you); calibrated-Bayes stance (Rubin/Little) as the synthesis.
- **Key results:** a decision guide: "given problem X, reach for Y, audit with Z"; annotated reading map (BDA3, MacKay, Murphy, Rasmussen–Williams, Särkkä, C-B chapters worth a second pass) with "read for" notes.
- **Sources:** everything prior; Little "Calibrated Bayes" by concept.
- **Code:** none new — the ledger links to prior artifacts.

---

## Cross-cutting apparatus (every module)
- **Bridge boxes:** ≥1 per module tying to C-B section, booklet chapter, or an ML-practice concept the learner already knows.
- **Pitfalls section:** the 3–5 mistakes practitioners actually make.
- **Predict-then-run exercises:** 3–6 per module, solutions in `<details>` blocks.
- **Verification contract:** every numeric claim in prose printed by a code block; `tools/run_module.py` must pass; seeds fixed; runtime <180 s target.

## Known open questions for the panel
1. Module count (25) vs depth — merge candidates: 09+10? 20+21? Is 22 too broad (design + causal)?
2. Where does the "counting/combinatorics → discrete probability" C-B ch. 1–2 material belong — module 01, or trusted as prerequisite?
3. Nonparametrics beyond DP+GP (BART? quantile regression?) — worth a module or a mention?
4. Is the two-point uniform CI example (module 06) the best conditional-coverage pathology, or use Jaynes' truncated-exponential or Welch's example?
5. Sequencing: should model checking (17) come before latent structure (18) as drafted, or after GPs?
6. How much MCMT theory (mixing times, spectral gaps) genuinely earns its keep in module 10?
7. PyMC vs NumPyro as the "in practice" library (pymc 6.1/arviz 1.2 installed; API newness is a risk either way).

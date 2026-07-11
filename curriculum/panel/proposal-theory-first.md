# Proposal — Statistical-Theory-First Curriculum

**Stance.** One subject, one object: the joint distribution over knowns and unknowns.
Inference is conditioning; prediction is the posterior predictive; a decision minimizes
expected posterior loss. The spine is a **rigor ladder** —
`probability → likelihood → decision theory → inference → computation → models` — climbed in
that order on purpose. Decision theory sits **before** inference so every estimator, interval,
and test arrives already framed as a decision; computation sits before the big models so we
know *why* a posterior is worth the trouble before we spend 10^6 gradient evaluations on it.

**Load-bearing reframe.** Casella–Berger supplies the skeleton, but frequentist results enter
as *theorems about special cases* of the Bayesian object and as *audits* of it: MLE = MAP under
a flat prior; ridge/lasso = Gaussian/Laplace priors; confidence ≈ credible via Bernstein–von
Mises; admissible = essentially Bayes (complete-class); sampling-distribution coverage as a
calibration check. Where the paradigms truly disagree (stopping rules, Lindley, conditioning),
both numbers are printed and the disagreement is named, not spun.

**Global conventions.** Python only. Every stated number is printed by a code block with a
fixed seed; every asymptotic is checked at finite *n*; exercises are **predict-then-verify**.
MCMC demos are sized for a 2-CPU box (≤4 chains × ~1000 draws, low dimension) to stay <180 s;
`pymc 6.1`/`arviz 1.2` idioms are verified by running, not from memory. `numpy/scipy` for
from-scratch mechanics, `pymc` for the real models, `arviz` for diagnostics.

---

## Part I — Probability as a Joint Distribution (the substrate)

### M1. The Joint Distribution *Is* the Model; Conditioning *Is* Inference
**Promise.** Every later technique is one recurring move — write a joint, then condition.
**Examples.** (a) Disease/test joint: base rate 0.01, sensitivity 0.99, specificity 0.95 →
P(disease | +) = 0.167 (print the table). (b) Bivariate Gaussian (θ, X), ρ=0.8: conditioning on
X=1.5 gives Normal posterior mean 1.2, var 0.36 — conditioning as linear projection (Kalman
update). (c) Monty Hall / three-prisoners: the answer depends on the host's *protocol* (the
joint over the mechanism), not the outcome alone — a first taste of the likelihood principle.
**Key results.** Bayes' theorem, chain rule, law of total probability (C-B §1.2–1.3; booklet ch1–2).
**Code.** Exact posterior tables; Gaussian conditioning in numpy; rejection-sampling MC check.
**Deps.** none.

### M2. Random Variables, Transformations, and Monte Carlo as Integration
**Promise.** Simulation is numerical integration with a √n error bar — quantify it from day one.
**Examples.** (a) Probability-integral transform: −log U ~ Exp(1); inverse-CDF sampling, histogram
vs pdf. (b) Accept–reject for a truncated Normal; report empirical acceptance rate vs the
analytic bound. (c) Tail probability P(Z>4)=3.17e-5: naive MC (SE ≈ 6e-6, often 0 hits) vs
importance sampling with a shifted proposal (SE ≈ 3e-7) — print both standard errors.
**Key results.** Change-of-variables/Jacobian (C-B §2.1), LLN+CLT for MC error (C-B §5.5),
accept–reject (C-B §5.6.3), importance sampling (booklet ch5).
**Code.** Inverse-CDF; accept–reject; importance-sampling tail estimate with SE comparison.
**Deps.** M1.

### M3. Exchangeability and de Finetti: Why Parameters Exist at All
**Promise.** "A parameter" is not metaphysics — it is the mixing measure an exchangeable sequence forces.
**Examples.** (a) Draw a binary sequence by first sampling Θ~Beta(2,2) then Bernoulli(Θ): show
positive pairwise correlation (not iid) and relative frequency → Θ. (b) Sampling *without*
replacement is exchangeable yet **not** a mixture of iid (negative correlation) — de Finetti
needs infinite exchangeability. (c) Pólya urn reproduces the Beta-Binomial predictive; seeds M22.
**Key results.** de Finetti representation theorem; exchangeable ⇒ conditionally iid (booklet ch2).
**Code.** Simulate exchangeable sequences, frequency→Θ; Pólya urn vs Beta-Binomial predictive.
**Deps.** M1.

---

## Part II — Likelihood and Information (what the data carries)

### M4. The Likelihood Function and the Likelihood Principle
**Promise.** The likelihood is the entire evidential content of the data — and that has teeth.
**Examples.** (a) **Stopping-rule paradox**: 9 heads in 12 tosses. Binomial one-sided p ≈ 0.073;
negative-binomial (stop at 3 tails) p ≈ 0.033 — *same* likelihood ∝ θ⁹(1−θ)³, *different*
p-values. Print both. (b) MLE = MAP under a flat prior: logistic regression, sklearn MLE vs pymc
MAP with a wide Normal prior → coincide as prior→flat; cross-entropy = −log-likelihood.
(c) Likelihood ratio as the optimal evidence weight (Neyman–Pearson preview).
**Key results.** Likelihood principle (booklet ch2); MLE=MAP(flat); score has mean zero.
**Code.** Two-p-value computation; MLE-vs-MAP coincidence sweep over prior width.
**Deps.** M1, M2.

### M5. Sufficiency, Exponential Families, and Fisher Information
**Promise.** Conjugacy, sufficiency, and "closed-form Bayes" are the same fact about exponential families.
**Examples.** (a) Normal: (Σxᵢ, Σxᵢ²) sufficient; Rao–Blackwellize a noisy unbiased estimator and
watch variance fall (print before/after). (b) Pitman–Koopman–Darmois: a fixed-dimension sufficient
statistic ⟺ exponential family; Uniform(0,θ) needs the max (order statistic), not a fixed summary.
(c) Fisher information I(θ)=1/(θ(1−θ)) for Bernoulli — verify as the variance of the score by
simulation; additivity nI(θ).
**Key results.** Factorization theorem (C-B §6.2), Basu's theorem (C-B §6.2), Rao–Blackwell
(C-B §7.3), exponential families (C-B §3.4), Fisher information; conjugacy (booklet ch3).
**Code.** Rao–Blackwell variance reduction; score-variance = information check.
**Deps.** M4.

---

## Part III — Decision Theory (the frame, before any procedure)

### M6. Loss, Risk, and the Bayes Rule as Optimal Decision
**Promise.** Point estimates are not "the answer" — they are the loss function's answer.
**Examples.** (a) On a skewed Gamma(2, 1) posterior, squared/absolute/0–1 loss give
mean=2.0, median≈1.68, mode=1.0 — print all three and their posterior expected losses.
(b) Frequentist risk R(θ,δ)=E[L] as a sampling average; risk curves of x̄ vs a shrinkage
estimator **cross** over a θ grid. (c) Newsvendor: underage cost 3, overage cost 1 → optimal
order is the 0.75 quantile of the posterior predictive, not its mean.
**Key results.** Bayes rule minimizes posterior expected loss; mean/median/mode ↔ L2/L1/0–1;
Bayes risk = ∫R dπ (booklet ch8).
**Code.** Three Bayes estimators on a Gamma posterior; risk curves; newsvendor quantile.
**Deps.** M1, M4.

### M7. Admissibility, Complete-Class Theorems, and Minimax
**Promise.** "Admissible" and "Bayes" are almost the same set — this is why Bayes is unavoidable.
**Examples.** (a) The constant estimator δ≡c is admissible (nothing dominates it at θ=c) — a
surprise that trains the definition. (b) Risk-set picture for a 2-point Θ: Bayes rules trace the
lower-left boundary; admissible = boundary. (c) Binomial minimax estimator (X+√n/2)/(n+√n) has
**flat** risk; plot it against the MLE's parabolic risk — they cross; minimax = Bayes vs the
least-favorable prior.
**Key results.** Complete-class theorem; admissibility; minimax as Bayes-with-least-favorable-prior;
Blyth's method (decision-theory canon; booklet ch8 framing).
**Code.** Risk-set plot for 2-point Θ; Binomial minimax vs MLE risk curves.
**Deps.** M6.

### M8. Stein's Paradox: When the Obvious Estimator Is Inadmissible
**Promise.** In ≥3 dimensions the sample mean is beatable *everywhere* — feel it as a risk curve, not a claim.
**Examples.** (a) d=10 Normal means: simulate MSE of MLE (=10) vs James–Stein (≈2 near the
origin, <10 for all θ) — print both. (b) Shrink 18 synthetic "batting averages" toward the grand
mean; JS wins total squared error — the empirical-Bayes reading (seeds M21). (c) d=1,2 show *no*
dominance; d=3 is the crossover — connect to the MLE's admissibility failing.
**Key results.** James–Stein (1961); Stein's unbiased risk estimate (SURE); inadmissibility of the
MLE for d≥3.
**Code.** Risk simulation MLE vs JS across d; SURE curve.
**Deps.** M6, M7.

---

## Part IV — Inference as Conditioning (Bayesian engine + frequentist audits)

### M9. Conjugate Analysis: The Posterior Engine in Closed Form
**Promise.** Before any sampler, get the exact posterior by hand — and the predictive too.
**Examples.** (a) Beta(2,2) + 8/10 → Beta(10,4), mean 0.714, 95% credible ≈ [0.48, 0.90];
sequential = batch. (b) Normal–Normal: prior N(0, 2²), data x̄=1.5, n=10, σ=1 → posterior mean
≈1.46 as a precision-weighted average; "the prior is worth κ observations" (booklet ch4).
(c) Normal–Inverse-Gamma (unknown mean+var): posterior predictive is Student-t — derive the df,
simulate draws vs the analytic density; Poisson–Gamma predictive is Negative-Binomial.
**Key results.** Conjugacy = exponential-family closure (C-B §3.4; booklet ch3–4); posterior
predictive (booklet ch5); precision weighting.
**Code.** Three conjugate updates + posterior-predictive draws vs analytic.
**Deps.** M5, M6.

### M10. Priors: Jeffreys, Reference, Weakly-Informative, and Regularizers
**Promise.** "Noninformative" is a fiction with a Jacobian — choose priors with eyes open.
**Examples.** (a) Flat-isn't-flat: Uniform on θ∈(0,1) is sharply non-flat on logit(θ) (transform +
histogram); Jeffreys Beta(½,½) is invariant. (b) Improper 1/σ can yield an **improper posterior**
in a variance component — the folk trap; a half-Normal(0,1) fixes it. (c) Regularizer duality:
N(0,τ²) prior = ridge with λ=σ²/τ²; Laplace = lasso; MAP path as τ→0 *is* the regularization path.
**Key results.** Jeffreys prior/invariance (booklet ch3); posterior propriety; prior=penalty duality
(ISLP §6.2). Bridges to M20.
**Code.** Flat-isn't-flat transform; ridge/lasso MAP path from a Gaussian/Laplace prior.
**Deps.** M9.

### M11. Point & Interval Estimation and Their Frequentist Audits
**Promise.** Cramér–Rao, UMVUE, and coverage are quality-control instruments for the posterior.
**Examples.** (a) Cramér–Rao: Var(x̄)=σ²/n attains 1/(nI); a shrinkage estimator *beats* the CRLB
(the bound is unbiased-only) — print CRLB vs empirical variance. (b) Coverage audit: Binomial n=10,
nominal-95% Wald CI coverage dips to ≈0.85, Jeffreys/credible interval ≈0.95 — simulate and print.
(c) Conditionality/Basu: the two-instruments mixture experiment — condition on the ancillary (which
instrument) or suffer a misleading unconditional interval.
**Key results.** Cramér–Rao, UMVUE + Lehmann–Scheffé, Rao–Blackwell (C-B §7.3); coverage
calibration; conditionality principle & ancillarity (C-B §6.2, Basu).
**Code.** Coverage simulation (Wald vs Jeffreys vs credible); CRLB attainment check.
**Deps.** M5, M6, M9.

### M12. Testing, Bayes Factors, Model Choice, and Lindley's Paradox
**Promise.** Testing is model comparison; the marginal likelihood is Occam's razor, automatically.
**Examples.** (a) Neyman–Pearson: the LR test traces the optimal ROC for N(0,1) vs N(1,1);
Karlin–Rubin (monotone LR) ⇒ UMP one-sided. (b) Bayes factor for H0:θ=0 vs H1:θ~N(0,τ²): the
marginal likelihood penalizes H1's flexibility (Occam factor) — plot BF vs n. (c) **Lindley's
paradox**: n=10⁴, z=1.96 → p=0.05 rejects, yet posterior P(H0)≈0.8 favors the null. Print p and
posterior side by side; name the disagreement.
**Key results.** Neyman–Pearson lemma & Karlin–Rubin (C-B §8.3), LRT (C-B §8.2); Bayes
factor/marginal likelihood (booklet ch8); Jeffreys–Lindley paradox.
**Code.** ROC/NP threshold; BF vs n; Lindley's numbers.
**Deps.** M6, M9, M11.

### M13. Large-Sample Theory: Bernstein–von Mises and Where It Breaks
**Promise.** Bayes and frequentist answers fuse asymptotically — until three named regimes tear them apart.
**Examples.** (a) BvM: Beta-Binomial posterior vs N(θ̂, I⁻¹) at n=5, 50, 500 — overlay, TV
distance shrinks ~1/√n; so credible ≈ confidence. (b) Delta method for the odds θ/(1−θ):
asymptotic variance g'(θ)²I⁻¹ agrees with bootstrap and posterior sd at large n (three routes,
one number). (c) Breakdowns: **Neyman–Scott** N-pairs give σ̂²_MLE → σ²/2 (print the bias);
boundary θ=0 → half-Normal posterior; Diaconis–Freedman nonparametric inconsistency (noted).
**Key results.** Bernstein–von Mises; asymptotic normality of the MLE + delta method (C-B §5.5.4,
§10.1); Wald/score/LRT equivalence (C-B §10.3); Neyman–Scott inconsistency; bootstrap (ISLP §5.2).
**Code.** BvM overlay + TV distance; delta vs bootstrap vs posterior sd; Neyman–Scott bias.
**Deps.** M11, M12.

---

## Part V — Computation (how to actually condition)

### M14. Deterministic Approximation: Laplace, Quadrature, and EM
**Promise.** Not every posterior needs a sampler — three classical approximations earn their keep.
**Examples.** (a) Laplace approximation of a Beta-Binomial marginal likelihood; error O(n⁻¹) —
print approx vs exact evidence at n=10, 100. (b) Gaussian quadrature nails a 1-D normalizing
constant in ~20 nodes vs a 1000-point grid (booklet ch15). (c) EM for a 2-component Gaussian
mixture (μ=[0,3], n=500): monotone log-likelihood increase (print the trace); label-switching
non-identifiability as a warning.
**Key results.** Laplace approximation (BDA concept); EM monotonicity (Dempster–Laird–Rubin;
C-B §7.2 framing); EM as an MM/ELBO lower bound.
**Code.** Laplace evidence; Gaussian quadrature; EM-GMM with log-likelihood trace.
**Deps.** M9, M13.

### M15. Variational Inference and the ELBO
**Promise.** Turn integration into optimization — and learn exactly which errors that trade buys.
**Examples.** (a) Mean-field CAVI on a conjugate Normal recovers the exact posterior; ELBO
monotone (print trace). (b) **Variance underestimation**: on a correlated bivariate Normal,
mean-field gets the mean right but marginals too narrow (KL(q‖p) is mode-seeking) — plot the
shrunken ellipse. (c) ADVI/black-box VI on logistic regression via pymc vs NUTS: means agree,
tails are light. Bridges to the VAE (M24), whose objective is this ELBO.
**Key results.** ELBO = log-evidence − KL(q‖p) (Jensen); CAVI; mode-seeking KL & variance
underestimation (booklet/BDA VI concept).
**Code.** CAVI Normal; mean-field variance-underestimate plot; pymc ADVI vs NUTS.
**Deps.** M14.

### M16. Metropolis–Hastings and Gibbs from First Principles
**Promise.** Build both samplers from detailed balance, then watch geometry decide their fate.
**Examples.** (a) Random-walk Metropolis on a Beta-Binomial posterior; tune to ~0.234 acceptance;
print acceptance rate and ESS. (b) Gibbs for Normal–Normal–Inverse-Gamma vs the exact conjugate
posterior; Rao–Blackwellized mean beats the plain mean (print variance drop). (c) 2-D correlated
Gaussian: componentwise Gibbs crawls as ρ→0.99 (autocorrelation), blocked Gibbs fixes it — print
ESS ratio.
**Key results.** Detailed balance & MH acceptance (booklet ch11); Gibbs as MH with acceptance 1
(booklet ch10); Rao–Blackwellization; ergodic theorem for MCMC.
**Code.** From-scratch MH + Gibbs; ESS/autocorrelation; blocking demo.
**Deps.** M2, M9.

### M17. Hamiltonian Monte Carlo, Langevin Dynamics, and the SDE Bridge
**Promise.** Gradients + physics beat random walks — and divergences are the model talking back.
**Examples.** (a) HMC with a hand-written leapfrog on a 2-D correlated Gaussian: ~10× the ESS per
gradient of RW-Metropolis; print energy conservation. (b) MALA as the discretized overdamped
Langevin SDE dX = ½∇log π dt + dW — stationary distribution = π (Lawler generator bridge);
uncorrected step-size bias. (c) **Neal's funnel**: HMC diverges in the neck; non-centered
reparameterization removes the divergences (print counts before/after via arviz).
**Key results.** Hamiltonian flow preserves the canonical distribution; leapfrog
reversibility/volume preservation (booklet BDA insert); Langevin SDE stationary law (Lawler,
SDE/generator ch); NUTS.
**Code.** From-scratch HMC leapfrog; MALA; pymc NUTS funnel + non-centered fix.
**Deps.** M16; Lawler stochastic-calculus background.

### M18. Markov-Chain Theory of MCMC: Mixing Times and Diagnostics
**Promise.** Convergence is a spectral gap; diagnostics are how you detect its absence.
**Examples.** (a) Spectral gap: for a 2-state chain and random walk on a cycle, compute the second
eigenvalue and relate relaxation time 1/(1−λ₂) to the observed autocorrelation; TV → 0
geometrically (MCMT). (b) A bimodal target where one chain "looks converged" but 4 chains expose a
missed mode — R-hat, ESS, rank plots catch it (arviz); label-switching in mixtures. (c)
Conductance/bottleneck: a two-well target where mixing time explodes exponentially in barrier
height; parallel tempering rescues it — print mixing time vs barrier.
**Key results.** Spectral gap ↔ mixing time; conductance/Cheeger bound (MCMT ch on eigenvalues &
bottlenecks); R-hat/ESS (booklet ch10); Markov-chain CLT; geometric ergodicity.
**Code.** Eigen-gap vs autocorrelation; multi-chain R-hat catching multimodality; tempering.
**Deps.** M16, M17.

---

## Part VI — Models (the payoff; ML/DL integrated, not ghettoized)

### M19. Regression and GLMs as Bayesian Models
**Promise.** Regression is a prior on weights plus a likelihood — OLS and the t-interval fall out.
**Examples.** (a) Conjugate Bayesian linear regression (Normal–Inverse-Gamma), n=50, p=3:
posterior over β and predictive bands equal OLS + t-intervals under a flat prior — print β
posterior vs OLS. (b) Logistic GLM via Laplace and NUTS; under **separation** the MLE diverges but
Gelman's weakly-informative Cauchy prior regularizes — print the coefficient both ways. (c) Poisson
GLM with overdispersion → Negative-Binomial/hierarchical; a posterior-predictive check flags the
misfit.
**Key results.** GLM = exponential-family likelihood + link (C-B §3.4; ISLP §4.6); Bayesian
regression posterior; Laplace for GLMs; separation regularization.
**Code.** Conjugate linreg; logistic Laplace+NUTS; Poisson/NB posterior-predictive check.
**Deps.** M9, M14, M17.

### M20. Regularization Is a Prior: Ridge, Lasso, Sparsity, and Deep Nets
**Promise.** Weight decay, lasso, early stopping, and dropout are all priors — and shrinkage wins measurably.
**Examples.** (a) Ridge on a collinear design = MAP under N(0,τ²); coefficient path vs λ, and the
ridge **MSE beats OLS** over a range of λ — print the min-MSE λ (Stein, made concrete; callback
M8). (b) Lasso = Laplace prior gives exact zeros at the MAP, but the Bayesian posterior mean (and
the horseshoe) does not — recover a 5-of-100 sparse signal with a horseshoe. (c) Deep nets: weight
decay = Gaussian prior; dropout ≈ approximate Bayesian model averaging (Gal–Ghahramani); a small
MLP shows the test-error U-curve and double descent.
**Key results.** Ridge/lasso as MAP (ISLP §6.2); horseshoe; dropout-as-Bayes; double descent
(ISLP §10.8).
**Code.** Ridge/lasso paths + MSE risk curve; horseshoe support recovery; MLP double descent.
**Deps.** M10, M8, M15.

### M21. Hierarchical Models, Shrinkage, and Multiple Testing
**Promise.** Partial pooling is James–Stein you can believe in — and it is how honest FDR works.
**Examples.** (a) Eight schools: no-pool vs complete-pool vs partial-pool; print shrinkage factors;
the funnel returns (non-centered, callback M17). (b) Empirical Bayes = James–Stein (callback M8):
Poisson–Gamma rates for 20 hospitals shrink toward the grand mean; EB estimate ≈ full-Bayes
posterior mean. (c) 1000 tests, two-groups model → Bayesian/local FDR vs Benjamini–Hochberg — print
discoveries at matched FDR.
**Key results.** Partial pooling/shrinkage; empirical Bayes ↔ JS; two-groups model & FDR (ISLP
§13.4; Efron); hierarchical priors (booklet ch7, ch9).
**Code.** Eight-schools pymc; EB rates; two-groups FDR vs BH.
**Deps.** M8, M17, M9.

### M22. Nonparametric Bayes: Gaussian Processes and Dirichlet Processes
**Promise.** Put a prior on functions and on distributions — infinite parameters, same conditioning move.
**Examples.** (a) GP regression, RBF kernel, n=15: posterior mean+bands, marginal-likelihood
lengthscale selection; GP = Bayesian linear regression in feature space = infinite-width NN (NNGP)
— print the learned lengthscale. (b) Dirichlet process via stick-breaking (Sethuraman); #clusters
grows like α log n; CRP = Pólya urn (callback M3). (c) DP-mixture density estimation on a bimodal
sample infers the component count — contrast with fixed-K EM (callback M14).
**Key results.** GP posterior (Rasmussen concept); Sethuraman stick-breaking; CRP/Pólya urn
(booklet ch13–14); DP concentration ↔ #clusters.
**Code.** GP regression from scratch; stick-breaking DP; DP-mixture Gibbs density.
**Deps.** M3, M9, M16.

### M23. Decision-Theoretic Experimental Design
**Promise.** Choosing *what data to collect* is the highest-leverage decision — treat it as one.
**Examples.** (a) Bayesian optimal design = maximize expected information gain: pick the next dose
in a logistic dose-response to maximize EIG; fewer trials than random to hit a target posterior
variance — print EIG per candidate. (b) Classical D-optimality (Montgomery): a 2² factorial
maximizes det(XᵀX) = minimizes posterior-covariance determinant under a flat prior; factorial vs
one-factor-at-a-time efficiency — print the det ratio. (c) Thompson sampling for a 3-arm Bernoulli
bandit (posterior sampling as decision) vs ε-greedy — print cumulative regret.
**Key results.** Expected information gain / Lindley (booklet decision framing); D/A-optimality
(Montgomery ch6, ch9); Thompson sampling; value of information.
**Code.** EIG dose selection; D-optimal factorial determinant; Thompson vs ε-greedy regret.
**Deps.** M6, M12.

### M24. Deep Generative Models Through the Bayesian Lens
**Promise.** VAEs, diffusion, and in-context learning are the Bayesian object at scale — one lens, three architectures.
**Examples.** (a) VAE: its training objective *is* the ELBO (callback M15) — encoder = amortized
q(z|x), decoder = likelihood; a tiny VAE on 8×8 sklearn digits shows reconstruction and latent
interpolation (print ELBO trace). (b) Diffusion = discretized reverse Langevin SDE (callback M17,
Lawler): forward noising + score-based reverse denoising on a 2-D toy matches the target — anneal
via Langevin. (c) In-context learning as implicit Bayesian updating: a toy exchangeable-sequence
model's predictive p(xₙ₊₁|x₁:ₙ) implements posterior updating (de Finetti, callback M3);
last-layer Laplace gives NN uncertainty.
**Key results.** ELBO/VAE (Kingma–Welling); score-based diffusion ↔ Langevin/SDE (Song; Lawler
bridge); in-context learning as Bayes (concept); Laplace for deep nets.
**Code.** Tiny numpy VAE on digits; 2-D toy diffusion (forward+reverse); exchangeable in-context sim.
**Deps.** M15, M17, M3.

---

## Twelve Must-Not-Miss Intuition Nuggets

1. **James–Stein dominance (M8).** In d≥3 the sample mean is inadmissible *everywhere*; a risk
   simulation, not a sermon. The single fastest route to distrusting "obvious" estimators.
2. **Lindley's paradox (M12).** Same data: p=0.05 rejects while posterior P(H0)≈0.8. p-values and
   posterior probabilities answer different questions; internalize which is which.
3. **Stopping rules & the likelihood principle (M4).** 9/12 heads → p ≈ 0.073 (binomial) vs 0.033
   (negative-binomial), identical likelihood. Design intent changes p-values, not the posterior.
4. **Neyman–Scott inconsistency (M13).** With one nuisance parameter per datum, σ̂²_MLE → σ²/2.
   "MLE is consistent" is a theorem with hypotheses — infinitely many parameters void it.
5. **Bernstein–von Mises *and* its failure (M13).** Credible ≈ confidence at O(1/√n) — then
   boundaries, and nonparametric (Diaconis–Freedman) inconsistency, break the bridge.
6. **The Bayesian Occam factor (M12).** Marginal likelihood penalizes flexibility automatically;
   the "simpler model wins on the same fit" intuition without an ad-hoc penalty.
7. **Flat priors aren't flat (M10).** Uniform on θ is informative on logit(θ); Jeffreys is the
   invariant fix. "Noninformative" is coordinate-dependent — always ask, flat in what?
8. **Borel–Kolmogorov paradox (M1 box).** Conditioning on a measure-zero event is ambiguous until
   the limiting mechanism is fixed. The measure-theoretic reason "condition on the protocol" matters.
9. **Simpson's paradox as a collider (M1/M19 box).** The joint distribution alone cannot answer a
   decision question; the intervention/causal structure can flip the sign. Correlation ≠ do().
10. **Ridge beats OLS in MSE (M20).** A concrete risk curve with a minimizing λ>0 — bias-variance
    as an honest risk decomposition, and shrinkage (M8) cashed out in regression.
11. **Basu's theorem & conditionality (M11).** Complete-sufficient ⟂ ancillary; the two-instruments
    example shows why you condition on ancillaries — unconditional guarantees can mislead.
12. **The folk theorem of statistical computing (M17/M18).** Divergences and poor mixing usually
    signal a bad *model* (funnel geometry), not just a bad sampler. Geometry is the diagnosis.

## Eight Failure Modes of Theory-First Curricula — and How This Outline Avoids Each

1. **Admissibility results the learner never feels.** → Every decision-theory theorem (M7, M8) is
   paired with a *risk simulation the learner runs* (James–Stein curves, minimax flat-risk plot);
   no "it can be shown."
2. **Measure-theoretic throat-clearing before payoff.** → σ-algebras/Radon–Nikodym appear only in
   just-in-time boxes where they resolve a concrete puzzle (Borel paradox, conditioning), using
   Lawler's conditional-expectation-as-projection where SDEs actually need it (M17).
3. **Theorems stated, never checked at finite n.** → BvM, the delta method, and CLT-for-MC are all
   *predict-then-verify* at n=5/50/500 with printed TV distances (M2, M13); the outline shows where
   the approximation is still bad.
4. **Bayesian-vs-frequentist tribalism.** → Bridge-box structure: each frequentist result is
   derived as a special case or audit (MLE=MAP, ridge=prior, coverage checks); genuine
   disagreements (M4 stopping, M12 Lindley) print *both* numbers and are named, not spun.
5. **Toy conjugate examples that never scale.** → An explicit ladder: Beta-Binomial (M9) →
   hierarchical logistic (M19, M21) → GP/DP (M22) → VAE/diffusion (M24), the *same* conditioning
   move at each rung, so rigor is seen to survive contact with real models.
6. **MCMC as an algorithm zoo with no theory of why/when it fails.** → M18 ties convergence to the
   spectral gap and conductance (MCMT) and M17 to the Langevin SDE (Lawler); failure geometry
   (funnel, multimodality, label-switching) is diagnosed, not just listed.
7. **Decision theory and design exiled to appendices.** → Decision theory is Part III (*before*
   inference) and experimental design is a first-class module (M23) with Bayesian OED, D-optimality,
   and bandits — framed as "the reason to compute a posterior at all."
8. **ML/DL bolted on as a separate, un-unified finale.** → Integrated throughout: MLE=MAP (M4),
   cross-entropy=−log-lik (M4), ridge/lasso/dropout=priors (M20), GP=infinite-width NN (M22),
   diffusion=Langevin (M24), in-context learning=implicit Bayes (M24); ISLP is a coverage checklist
   mapped into the model modules, not a terminal chapter.

## Dependency Backbone
`M1→M2,M3 · M2,M1→M4→M5 · M6→M7→M8 · M5,M6→M9→M10 · M9→M11→M12→M13 ·
M13→M14→M15 · M9→M16→M17→M18 · {M9,M14,M17}→M19→M20 · {M8,M17}→M21 · M16→M22 ·
M6,M12→M23 · {M15,M17,M3}→M24`. Parts are sequential; within Part VI, M19–M24 fan out from Part V.

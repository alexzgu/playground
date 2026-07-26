# Glossary

The same idea has three or four names depending on who is talking. This maps
them. **Bold** is the term this guide uses.

## The objects

| Term | What it actually is | Also called |
|---|---|---|
| **Prior** | What you believed about the unknowns before seeing this data. Equivalently: a claim about what data you expected. | regularisation, penalty, weight decay, shrinkage target, inductive bias |
| **Likelihood** | How probable your data is, for each candidate value of the unknowns. Not a probability of the unknowns. | the model, the noise model, the loss (negated and logged) |
| **Posterior** | What you believe after conditioning on the data. In practice, a bag of parameter values. | the fit, the trained model, the answer |
| **Posterior predictive** | The distribution of *new data*, averaging over everything you still don't know. | predictive distribution, forecast distribution |
| **Marginal likelihood** | Probability of the data with the parameters integrated out. Has a built-in complexity penalty. | evidence, model evidence, `p(y)`, the denominator |
| **Hyperparameter** | A parameter of a prior, e.g. how much branches differ. | regularisation strength, `lambda`, `alpha`, `C` |

## The quantities you report

| Term | Meaning | Notes |
|---|---|---|
| **HDI** | Narrowest interval containing X% of the posterior. | highest posterior density interval, HPD |
| **Percentile interval** | Equal probability cut from each tail. | credible interval, quantile interval, PI |
| **Credible interval** | Any interval containing X% of the posterior. | *not* a confidence interval — see below |
| **Confidence interval** | An interval from a *procedure* that covers the truth X% of the time across hypothetical repetitions. | agrees numerically with the credible interval in large samples (Bernstein–von Mises) and can differ sharply in small ones |
| **ESS** | How many independent draws your correlated MCMC sample is worth. | effective sample size, `n_eff` |
| **R-hat** | Whether independent chains agree. Above 1.01, don't use the draws. | Gelman–Rubin, potential scale reduction |
| **elpd** | Expected log predictive density on new data. Higher is better. | out-of-sample log score, negative cross-entropy |

## The models

| This guide | Statistics | Machine learning | Econometrics |
|---|---|---|---|
| linear model | linear regression | linear/ridge/lasso regression | OLS |
| Gaussian prior on coefficients | ridge, Tikhonov | L2, weight decay | shrinkage |
| Laplace prior on coefficients | lasso | L1, sparsity penalty | — |
| logistic model | logistic regression, Bernoulli GLM | logistic regression, cross-entropy classifier | logit |
| Poisson / negative binomial | count GLM | — | count model |
| **hierarchical model** | multilevel model, random effects, mixed model, empirical Bayes | multi-task learning, partial pooling | panel with random effects |
| index variable | one intercept per level | categorical embedding | fixed effects |

## The methods

| Term | What it does | Where in this guide |
|---|---|---|
| **Grid approximation** | Evaluate the posterior on a mesh of candidate values. Works for 1–2 unknowns. | ch 01, 03 |
| **Quadratic approximation** (`quap`) | Fit a Gaussian at the posterior peak using the curvature there. | ch 04 |
| **Laplace approximation** | The same thing, under its usual name. | ch 04 |
| **MCMC** | Sample from any posterior you can evaluate up to a constant. | ch 05 |
| **Metropolis** | The 15-line random-walk sampler. | ch 05 |
| **HMC / NUTS** | Gradient-guided sampler; what NumPyro and Stan run. | ch 05 |
| **Non-centring** | Rewriting `x ~ Normal(mu, tau)` as `x = mu + tau*z, z ~ Normal(0,1)`. Same distribution, far better geometry. | ch 05, 09 |
| **Divergence** | The sampler's report that a region of the posterior has curvature it cannot resolve. Never ignore. | ch 05 |
| **Prior predictive check** | Simulate data from the priors and look at it. | ch 03 |
| **Posterior predictive check** | Simulate data from the fitted model and compare with reality. | ch 06 |
| **PSIS-LOO** | Leave-one-out cross-validation from a single fit, with a reliability diagnostic. | ch 12 |
| **WAIC** | An information criterion that estimates the same quantity as LOO. | ch 12 |
| **EVPI / EVSI** | What perfect information / a specific study is worth, in money. | ch 10 |

## The traps

| Term | The trap |
|---|---|
| **Confounder** | A common cause of treatment and outcome. Control for it. |
| **Collider** | A common *effect* of two variables. Controlling for it invents associations that were not there. |
| **Mediator** | On the causal path. Controlling for it removes the effect you wanted to measure. |
| **Selection** | The rows in your file were chosen by a process. That process is usually a collider. |
| **Base rate** | The prevalence before evidence. Ignoring it is why most positive tests are false. |
| **Winner's curse** | Selecting the maximum of noisy estimates selects partly on the noise, which doesn't repeat. |
| **Overdispersion** | More variance than the model's noise family permits. Barely biases coefficients; destroys intervals. |
| **Identification** | Whether the data can distinguish parameter values at all. Unidentified parameters keep their priors forever, and the posterior can still look narrow. |
| **Calibration** | Whether things you call 30% happen 30% of the time. A property of a model *and a population*. |

## Notation used throughout

| Symbol | Meaning |
|---|---|
| `p(·)` | a density or probability mass function |
| `theta`, `mu`, `sigma`, `tau`, `p` | unknowns — anything you don't know is a random variable |
| `y` | the observed outcome; `x` the predictors you condition on |
| `y_new`, `yrep` | future or simulated data |
| `Normal(mu, sigma)` | **second argument is the standard deviation** in code (numpy, scipy, NumPyro), the *variance* in most textbooks. Watch this. |
| `Gamma(alpha, beta)` | beta is a **rate** here; scipy wants `scale=1/beta` |
| `HalfNormal(s)` | a Normal(0, s) folded to be positive — the default prior for a scale |
| `logit(p)` | `log(p/(1-p))`, the log-odds |
| `~` | "is distributed as" — a stochastic line in a model |
| `=` | a deterministic definition inside a model (e.g. `mu = a + b*x`) |

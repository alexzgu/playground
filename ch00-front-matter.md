# Front matter

### PDF page 1 (cover)

**MA 556, Applied Bayesian Statistics**

**Fall 2025**

Balgobin Nandram
Professor of Statistics, WPI

**About this Course**

Bayesian statistics is very objective, and it is based on a simple idea: Every unknown quantity is a random variable. With the advent of Markov chain Monte Carlo methods more than thirty-five years ago, Bayesian statistics has gained enormous reputation in private companies and government agencies, and it is difficult for Universities to meet the demand. Bayesian statistics is based on the simple Bayes' theorem, learnt in High Schools throughout the world. It makes use of an inferential process that models data, and it summarizes the results in terms of probability distributions for the model parameters. A key feature is that in the Bayesian approach, past information can be updated with new data in an elegant way in order to aid in decision making. Many data sets collected concurrently can be studied simultaneously in a single model. Topics included in the course are the Bayesian inferential framework (model specification, model fitting and model checking); computational methods for posterior simulation and integration including computational diagnostics; regression models, hierarchical models, and ANOVA; time permitting, additional topics will include small area estimation, generalized linear models, multivariate models, missing data problems, and time series analysis. (Prerequisites: knowledge of MA 540 or equivalent is assumed.)

### PDF page 2 (Contents, p. iii)

**Contents**

**1 Lecture One — 1**
1.1 Bayesian Paradigm — 1 · 1.2 Review background of probability — 2 · 1.3 Coherent — 3 · 1.4 Conditional Probability — 3 · 1.5 Distribution Function — 4 · 1.6 Transformations — 4 · 1.7 Extension theorem — 5 · 1.8 Conditional distribution — 5

**2 Lecture Two — 9**
2.1 Bayes' Theorem — 9 · 2.2 Independence — 9 · 2.3 Exchangeability — 9 · 2.4 Conditional expectations and variances — 10 · 2.5 Theorem: De Finetti — 11 · 2.6 Likelihood Principle — 12 · 2.7 Probability (subjective) — 13 (2.7.1 Empirical view of probability — 13 · 2.7.2 Multiplication rule — 14 · 2.7.3 Bayesian view of Probability — 14)

**3 Lecture Three — 17**
3.1 Motivating Monte Carlo Methods (integration) — 19 · 3.2 Prior Constraction [sic] — 20 (3.2.1 How to construct conjugate priors? — 21 · 3.2.2 Two ways to construct objective priors — 22) · 3.3 How to specify the parameters of priors? — 29

**4 Lecture Four — 35**
4.1 Combination of information from different sources — 36 · 4.2 How many observations the prior is worth? — 37 · 4.3 How to draw a sample from a set of values? — 39

### PDF page 3 (Contents, p. iv)

**5 Lecture Five — 41**
5.1 Regression — 41 · 5.2 Prediction — 42 · 5.3 Marginal Likelihood — 44 · 5.4 Big idea — 45 · 5.5 Numerical Integrations — 46 · 5.6 Gibbs Sampler (Brief idea) — 47 · 5.7 Rejection Sampling — 47 · 5.8 Squeeze Method (Envelope) — 48 · 5.9 Monte Carlo Integration — 49 · 5.10 Importance Sampling — 50 · 5.11 How to pick the importance (proposal) density — 52 · 5.12 Multivariant version — 53

**6 Lecture Six — 55**
6.1 Rao-Blackwellized Estimation — 55 · 6.2 ARS: Adaptive Rejection Sampling — 57

**7 Lecture Seven — 61**
7.1 Hierarchical Bayesian Models — 61 · 7.2 Hierarchical Models with Covariates — 62 · 7.3 Conditional predictive ordinate (CPO) and LPML — 62

**8 BAYESIAN INFERENCE — 65**
8.1 Interval Estimation — 65 (8.1.1 Credible Interval — 65 · 8.1.2 Highest Posterior Density (H.P.D) Interval — 66) · 8.2 Hypothesis-Testing — 71 (8.2.1 Bayes Factor — 72 · 8.2.2 Marginal Likelihoods — 73) · 8.3 Prediction — 77 (8.3.1 Examples — 77 · 8.3.2 How do non-Bayesians predict? — 78 · 8.3.3 More examples — 79)

**9 HIERARCHICAL MODELS — 83**
9.1 Normal Means Models — 83 (9.1.1 One-way Random Effects Model — 83 · 9.1.2 Marginal Distributions — 84 · 9.1.3 Hierarchical Model — 84 · 9.1.4 Posterior Distributions — 85 · 9.1.5 More sophistication — 85) · 9.2 Small Area Estimation — 86 (9.2.1 Form of estimation — 86 · 9.2.2 Gaining Strength — 88)

### PDF page 4 (Contents, p. v)

(9.2 continued) 9.2.3 Empirical Bayes Statistics — 89 · 9.2.4 Full Bayesian Analysis — 89 · 9.3 Benchmarking — 90 · 9.4 Big Data — 92 · 9.5 Appendix — 94

**10 GIBBS SAMPLER — 99**
10.1 What is the Gibbs sampler? — 99 · 10.2 How to assess convergence? — 101 (10.2.1 Trace plots — 101 · 10.2.2 Auto correlation — 101 · 10.2.3 Monte Carlo error — 103 · 10.2.4 Geweke test (Geweke 1992) — 103 · 10.2.5 Effective sample size — 104) · 10.3 Rao-Blackwellized estimators — 104 · 10.4 The Griddy Gibbs sampler — 106 · 10.5 Example — 108 · 10.6 Bayesian Cross Validation — 114

**11 METROPOLIS-HASTINGS SAMPLER — 117**
11.1 General Discussion — 117 · 11.2 Convergence — 118 · 11.3 Spread of the proposal density — 120 · 11.4 Example I. Logistic regression model — 120 · 11.5 Example II. Poisson regression model — 122 · 11.6 Rao-Blackwellized estimator — 125 · 11.7 Tuning the Metropolis step — 126 · 11.8 Reversible Jump Markov chain Monte Carlo Sampler — 127

**12 Lecture Eight — 131**
12.1 Bayesian predictive p-value (BPP) — 131 (12.1.1 Deviance information criteria (DIC) — 132) · 12.2 SIR algorithm — 133 · 12.3 Slice sampling — 134 · 12.4 INLA — 135 · 12.5 Multinomial-Dirichlet model — 136

**13 Lecture Nine — 139**
13.1 Hierarchical Multinomial-Dirichlet Model — 140 · 13.2 Data Augmentations — 142 · 13.3 Bayesian Nonparametrics — 142 · 13.4 What is a Dirichlet process? — 142 (13.4.1 Dirichlet Process Model — 143 · 13.4.2 Dirichlet Process Mixture Model — 143)

### PDF page 5 (Contents, p. vi)

**14 Nonparametric Bayesian Statistics — 145**
14.1 Dirichlet Process — 145 (14.1.1 Generalized Polya Urn — 145 · 14.1.2 Dirichlet Process Mixture (DPM) Model — 148) · 14.2 Two more formulations of the Dirichlet Process — 153

**15 Difficulties with MCMC Algorithms — 157**
15.1 Introduction — 157 · 15.2 Numerical Techniques — 160 (15.2.1 Numerical Integration (Gaussian Quadrature) — 160 · 15.2.2 Grid sampler — 161 · 15.2.3 Sampling Importance Resampling (SIR) Algorithm — 161 · 15.2.4 Rao-Blackwellization — 162) · 15.3 Examples — 162 (15.3.1 Generalized Gamma — 162 · 15.3.2 Skewed Exponential Power Distribution — 165 · 15.3.3 Normal-means Model — 167)

**A Rstudio — 171**
A.1 How to Install R Studio — 171 (A.1.1 Install R — 171 · A.1.2 Install R Studio — 171 · A.1.3 R Studio Layout — 171 · A.1.4 Working Directory — 172 · A.1.5 Libraries and packages — 172) · A.2 Basic Tutorial for Data Analysis — 173 (A.2.1 Importing Data in R Studio — 173 · A.2.2 Manipulating Data — 174 · A.2.3 Save and Export Data File — 174 · A.2.4 Load Data File — 175 · A.2.5 Simple Statistics — 175 · A.2.6 Plotting Data — 175 · A.2.7 Draw Random Samples — 176 · A.2.8 Help in R and Communication with Internet — 176)

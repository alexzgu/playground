# Chapter 7 — Lecture Seven
*(PDF pages 66–69; booklet pages 61–64)*


### PDF page 66 (booklet page 61)

# Chapter 7 — Lecture Seven

1. Hypothesis testing, Model choice and Predictive inference
2. More Hierarchical models
3. Gibbs sampler

We have two models, $M_1$ and $M_2$ The respective marginal likelihoods are: *[sic: no period after $M_2$]*

$$f\left(x \mid M_1\right) \ \text{ and } \ f\left(x \mid M_2\right)$$

*(The booklet writes $x$ with an under-tilde to indicate a vector.)*

So the Bayes factor is *(correction: a short hand-hatched strikethrough cancels an [illegible] word after "factor", and handwritten "is" is inserted after it)*

$$BF = \frac{f\left(x \mid M_2\right)}{f\left(x \mid M_1\right)}$$

*[margin note, left of the next equation: "Log Bayes factor"]*

$$\log BF = \log f\left(x \mid M_2\right) - \log f\left(x \mid M_1\right)$$

> ✔ Verified: Taking logs of $BF = f(x\mid M_2)/f(x\mid M_1)$ gives $\log BF = \log f(x\mid M_2) - \log f(x\mid M_1)$.

$$f\left(x \mid M_1\right) = \iint f\left(x \mid M_1, \Omega\right) \pi\left(\Omega \mid M_1\right) d\Omega$$

$$f\left(x \mid M_2\right) = \iint f\left(x \mid M_2, \Omega\right) \pi\left(\Omega \mid M_2\right) d\Omega$$

**7.1 Hierarchical Bayesian Models**

1) Normal means model

$$y_{ij} \mid \mu_i, \sigma^2 \overset{iid}{\sim} N\left(\mu_i, \sigma^2\right), i = 1, \ldots, \ell;\, j = 1, \ldots, n_i, \ldots, N_i$$
$$\mu_i \mid \theta, \delta^2 \sim N\left(\theta, \delta^2\right)$$
$$\pi\left(\theta, \sigma^2, \delta^2\right) \text{ proper prior}$$

*[Handwritten references at the foot of the page, in the instructor's hand:]*
*"Scott-Smith (1968(?))"*
*"⊛ Nandram, Toto, Choi (2011)"*

### PDF page 67 (booklet page 62)

2) Beta-Binomial hierarchical model

$$y_{ij}\mid p_i \overset{iid}{\sim} Bernoulli\,(p_i)$$

$$p_i\mid \mu,\tau \overset{iid}{\sim} \text{Beta}(\mu\tau,(1-\mu)\tau)$$
$$\pi(\mu,\tau) = \tfrac{1}{(1+\tau)^2},\;\text{ proper}$$

> ✔ Verified: The prior $\pi(\mu,\tau)=1/(1+\tau)^2$ on $(0,1)\times(0,\infty)$ is proper (integrates to 1).

3) Poisson-Gamma Model

$$y_{ij}\mid \lambda_i \sim \text{Poisson}\,(n_i\lambda_i)$$
$$\lambda_i\mid \alpha,\beta \sim \text{Gamma}(\alpha,\beta)$$
$$\pi(\alpha,\beta) \propto \tfrac{1}{\beta}\tfrac{1}{(1+\alpha)^2}$$

**7.2 Hierarchical Models with Covariates**

If there are covariance [sic: *covariates*] $x_{ij}$, then normal means model is: *(The booklet writes $x$, $\beta$, $\theta$, $y$ with under-tildes to indicate vectors.)*

$$y_{ij}\mid \beta,\sigma^2 \overset{iid}{\sim} N\left(x'_{ij}\beta + \nu_i,\sigma^2\right)$$
$$\nu_i\mid \delta^2 \sim N\left(0,\delta^2\right)$$
$$\pi\left(\beta,\sigma^2,\delta^2\right)$$

*[margin note, right of this display: "Toto and Nadram (?) (2010)" — i.e. Toto and Nandram (2010)]*

In small area estimation this model is called the Battese-Harter-Fuller (BHF) model. Recall that the model without covariates is called the Scott-Smith (SS) model.

*[margin note, left: "1988", circled by hand — the Battese-Harter-Fuller reference year]*

The Beta-Bernoulli model can extended [sic: *can be extended*] as the logistic regression model

$$y_{ij}\mid \beta,\nu_i \overset{iid}{\sim} \text{Bernoulli}\left(\frac{e^{x'_{ij}\beta+\nu_i}}{1+e^{x'_{ij}\beta+\nu_i}}\right)$$
$$\nu_i\mid \delta^2 \sim N\left(0,\delta^2\right)$$
$$\pi\left(\beta,\delta^2\right)$$

**7.3 Conditional predictive ordinate (CPO) and LPML**

$$CPO_r = f\left(y_r\mid y_{(r)}\right), r = 1,\dots,n$$

$$\widehat{CPO}_r = \left\{\frac{1}{M}\sum_{h=1}^{M}\frac{1}{f\left(y_r\mid\theta^{(h)}\right)}\right\}^{-1}\;\text{— —Harmonic mean of } f\left(y_r\mid\theta^{(h)}\right)$$

> ✔ Verified: The stated $\widehat{CPO}_r$ estimator is exactly the harmonic mean of the $M$ values $f(y_r\mid\theta^{(h)})$.

### PDF page 68 (booklet page 63)

$\theta^{(1)},\dots,\theta^{(M)}$ are samples from $\pi(\theta \mid y)$. This assumes that $y_1,\dots,y_r \mid \theta$ are independent.

Gelfand, Dey and Chang (1992) *[the year "1992" is hand-underlined twice]*

$$\frac{1}{\widehat{CPO}_r} > 40,\ \text{outliers}$$

$$\frac{1}{\widehat{CPO}_r} > 70,\ \text{extreme outliers}$$

*[margin notes, right of the two inequalities: ".025"; ".014" — the reciprocals of the two thresholds]*

> ✔ Verified: The reciprocal of the outlier threshold 40 equals the handwritten margin value 0.025 exactly, so $1/\widehat{CPO}_r>40 \iff \widehat{CPO}_r<0.025$.

> ✔ Verified: The reciprocal of the extreme-outlier threshold 70 is $0.0142857\ldots$, which rounds to the handwritten margin value 0.014 at three decimal places.

Ntzoufras (2009) *(correction: the printed name reads "Ntzonfras" [sic]; a handwritten caret inserts "u" in place of the "n")*

*[margin note, below the name: "Ntzoufras" — written out again by hand]*

$$LPML = \sum_{r=1}^{n} \log\left(\widehat{CPO}_r\right)$$

If we have several models:

$$LPML_g, g = 1,\dots,G\ (G\ \text{models})$$

Select model which maximizes $LPML_g, g = 1,\dots,G$

*[margin note, lower left: "(1979)" above "Fay–Herriot" — an added reference.]*

*[Handwritten work, lower middle of the page: $\widehat{CPO}_r < .025$ — "outliers"; $\widehat{CPO}_r < .014$ — "extreme". These restate the two Gelfand–Dey–Chang thresholds above in terms of $\widehat{CPO}_r$ itself rather than its reciprocal.]*

### PDF page 69 (booklet page 64)

*(Blank page — running header only.)*

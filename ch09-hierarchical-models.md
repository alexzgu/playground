# Chapter 9 — HIERARCHICAL MODELS
*(PDF pages 88–103; booklet pages 83–98)*


### PDF page 88 (booklet page 83)

# Chapter 9 — HIERARCHICAL MODELS

**9.1 Normal Means Models**

One way random effects model is the most ubiquitous model in statistics. It is also called the normal means model.

Random effects are used to accommodate extra variation (overdispersion) due to differences among clusters (groups) of data.

Suppose there are clusters and within the cluster^ there are individuals. There is a single observation on each individual. This is a common structure for familial data which are abundant in applications. *(an insertion caret is hand-drawn between "cluster" and "there", with no legible inserted word)*

*[Handwritten scratch note in dark pen, running across the white space to the right of "abundant in applications." and into the right margin, two cursive lines, largely illegible: "people(?) in the same family(?) [illegible] " / "…in the same(?) batch of material(?)". These appear to be lecture examples of what a "cluster" can be.]*

The normal means model introduces a correlation (intraclass) among the individuals within the same family (cluster)

**9.1.1 One-way Random Effects Model**

Suppose $\theta, \sigma_i^2$ and $\delta^2$ are fixed but unknown. Then the one-way random effects model is

$$Y_{ij} = \theta + \mu_i + \epsilon_{ij}, i = 1, \cdots, l, j = 1, \cdots, n_i$$

*[margin note, right of the equation: a large script "$\ell$", glossing the printed index limit $l$]*

*(The booklet writes $\mu$ with an under-tilde to indicate a vector.)*

where $\mu_i$ are the random effects and $\epsilon_{ij}$ are sampling errors,

$$\mu_1, \ldots, \mu_l \overset{iid}{\sim} N\left(0, \delta^2\right)$$

and independently

$$\epsilon_{i1}, \ldots, \epsilon_{in_i} \overset{iid}{\sim} N\left(0, \sigma_i^2\right)$$

Typically $\theta, \sigma_i^2$ and $\delta^2$ are estimated using the data; the data are used twice.

83

### PDF page 89 (booklet page 84)

**9.1.2 Marginal Distributions**

This one-way random effects model describes the marginal distributions of the $Y_{ij}$. For the $Y_{ij}$ are normally distributed (after integrating out the random effects). [sic: sentence fragment / "For" appears to be a slip for "The"] It is easy to show that,

$$E\left(Y_{ij}\right) = \theta$$

$$\mathrm{Cov}\left(Y_{ij}, Y_{i'j'}\right) = \begin{cases} \sigma_i^2 + \delta^2, & i = i', j = j' \\ \delta^2, & i = i', j \neq j' \\ 0, & \text{else} \end{cases}$$

> ✔ Verified: For $Y_{ij}\mid\mu_i \sim N(\mu_i,\sigma_i^2)$ with $\mu_i \sim N(\theta,\delta^2)$, the marginal moments are $E(Y_{ij})=\theta$, $\mathrm{Var}(Y_{ij})=\sigma_i^2+\delta^2$, and $\mathrm{Cov}(Y_{ij},Y_{ij'})=\delta^2$ for $j\neq j'$.

$$\mathrm{Corr}\left(Y_{ij}, Y_{i'j'}\right) = \begin{cases} 1, & j = j', \; i = i' \\ \dfrac{\delta^2}{\delta^2 + \sigma_i^2}, & j \neq j', i = i' \end{cases}$$

*(correction: the handwritten condition "$i = i'$" (?) is added after the printed "$1, j = j'$" in the first case, which as printed omits it)*

> ✔ Verified: The intraclass correlation is $\mathrm{Corr}(Y_{ij},Y_{ij'}) = \delta^2/(\delta^2+\sigma_i^2)$ for $j\neq j'$, $i=i'$.

&nbsp;&nbsp;&nbsp;&nbsp;Thus, the observations within a cluster are correlated (familial correlation) and the intraclass correlation is $\frac{\delta^2}{\delta^2+\sigma_i^2}$.

**9.1.3 Hierarchical Model**

The one-way random effects model can be rewritten in the hierarchy:
Scott and Smith (JASA 1969)

*[margin note, left of the two displays: "$Y_{ij} = \theta + v_i + e_{ij}$"]*

$$Y_{i1}, \ldots, Y_{im_i} \mid \mu_i, \sigma_i^2 \overset{iid}{\sim} N\left(\mu_i, \sigma_i^2\right) \tag{1}$$

$$\mu_1, \ldots, \mu_l \mid \theta, \delta^2 \overset{iid}{\sim} N\left(\theta, \delta^2\right) \tag{2}$$

Remark: If $\theta, \sigma_i^2$ and $\delta^2$ are fixed but unknown, this model is exactly the one-way random effects model.

&nbsp;&nbsp;&nbsp;&nbsp;This is a two stage hierarchical model. The first statement (1) describes the sampling process, and the second statement (2) describes a prior position.

Remark: Some people might think of (2) as part of the sampling process.

&nbsp;&nbsp;&nbsp;&nbsp;The third stage of the hierarchical model is

*[margin note, left of the display: "Can lead to improper posteriors"]*

$$\begin{aligned} p(\theta) &= 1, \\ \sigma_i^{-2} &\overset{iid}{\sim} \mathrm{Gam}\left(\tfrac{a}{2}, \tfrac{b}{2}\right), \\ \delta^{-2} &\overset{iid}{\sim} \mathrm{Gam}\left(\tfrac{a}{2}, \tfrac{b}{2}\right) \end{aligned} \tag{3}$$

*[Handwritten scratch notes to the right of (3), dark pen, only partly legible: a line of the form "$a = \ldots = b$" (?), with the words "proper prior" (?) below it and "[illegible] approach 0" (?) above right. These appear to be lecture notes on the limiting behaviour of the Gamma hyperprior, matching the left-margin warning about improper posteriors.]*

I call this a three-stage hierarchical model.

### PDF page 90 (booklet page 85)

NOTE. The prior specification $p(\theta) = 1$ is very powerful *[the word "powerful" is hand-underlined]*. This introduces a correlation among the $\mu_i$ 's.

Assumption 1. The individuals within groups share an effect (i.e., they are similar)
Assumption 2. The clusters (groups) share an effect (i.e., they are similar)

The similarity in (1) and (2) depends on $\sigma_i^2$ and $\delta^2$ respectively.

Remarks
1. The model can be generalized to many stages. At each stage the parameters (variables) simply share an effect.
2. A $K$-stage hierarchical model is appropriate for a multi-stage complex survey with $K-1$ stages.

**9.1.4 Posterior Distributions**

Consider a simplified model

$$Y_{i1},\ldots,Y_{in_i}\mid \mu_i,\sigma_i^2 \overset{iid}{\sim} N\left(\mu_i,\sigma_i^2\right)$$
$$\mu_1,\ldots,\mu_l\mid \theta,\delta^2 \overset{iid}{\sim} N\left(\theta,\delta^2\right)$$
$$p(\theta) = 1$$

(i.e., assume $\sigma_i^2$ and $\delta^2$ are fixed and known.)

Let

$$\bar{y}_i = \frac{\sum_{j=1}^{n_i} y_{ij}}{n_i},$$
$$\lambda_i = \frac{\delta^2}{\delta^2 + \sigma_i^2/n_i}, \quad i = 1,\ldots,l$$

By Bayes theorem

$$\mu_i\mid \boldsymbol{y}_i,\theta \overset{ind}{\sim} N\left(\lambda_i\bar{y}_i + (1-\lambda_i)\,\theta,\ (1-\lambda_i)\,\delta^2\right)$$

> ⚠ Check FAILED: The normal–normal update gives posterior $\mu_i\mid\bar y_i,\theta \sim N(\lambda_i\bar y_i+(1-\lambda_i)\theta,\ (1-\lambda_i)\delta^2)$ with $\lambda_i=\delta^2/(\delta^2+\sigma_i^2/n_i)$. — the stated result did not reproduce (see verification log)

Remarks
1. Inference is required about $\mu_i$, but $\theta$ is unknown and random.
2. The unconditional posterior density of $\mu_i\mid\boldsymbol{y}_i$ is obtained by first finding the poste rior [sic] density $\theta\mid\boldsymbol{y}$.

**9.1.5 More sophistication**

We now integrate out $\theta$. Let

$$\nu^2 = \frac{\delta^2}{\sum_{i=1}^{l}\lambda_i} \quad \text{and} \quad \hat{\theta} = \frac{\sum_{i=1}^{l}\lambda_i\bar{y}_i}{\sum_{i=1}^{l}\lambda_i}$$

### PDF page 91 (booklet page 86)

*[margin note, top of page: "best linear unbiased estimator" — a handwritten gloss on "BLUE" below.]*

Here $\hat{\theta}$ is the BLUE of $\theta$. The posterior density of $\theta|\boldsymbol{y}$ is

$$\theta|\boldsymbol{y} \sim N\left(\hat{\theta}, \nu^2\right) \qquad \text{homework!!}$$

Recall that

$$\mu_i|\boldsymbol{y}_i, \theta \overset{ind}{\sim} N\left(\lambda_i \bar{y}_i + (1-\lambda_i)\theta, (1-\lambda_i)\delta^2\right)$$

> ✔ Verified: Normal–normal conjugate update: p(ȳ|μ)p(μ|θ) = p(ȳ|θ) · N(μ; λȳ+(1−λ)θ, (1−λ)δ²) with λ = δ²/(δ²+σ²/n).

$$p(\boldsymbol{\mu}|\boldsymbol{y}) = \int_{-\infty}^{\infty} \left\{\prod_{i=1}^{l} p\left(\mu_i|\boldsymbol{y}_i, \theta\right)\right\} p(\theta|\boldsymbol{y}) d\theta$$

*(The booklet writes $\boldsymbol{y}$, $\boldsymbol{\mu}$ with under-tildes to indicate vectors.)*

Main result:

$$\mu_i|\boldsymbol{y} \sim N\left(\lambda_i \bar{y}_i + (1-\lambda_i)\hat{\theta}, (1-\lambda_i)^2 \nu^2 + (1-\lambda_i)\delta^2\right)$$

> ✔ Verified: Marginalizing θ|y ~ N(θ̂, ν²) yields μ_i|y ~ N(λȳ+(1−λ)θ̂, (1−λ)²ν² + (1−λ)δ²).

$$\text{Cov}\left(\mu_i, \mu_i|\boldsymbol{y}\right) = (1-\lambda_i)\left(1-\lambda_{i'}\right)\nu^2$$

*[sic: the left-hand side is printed with $\mu_i$ twice; the right-hand side shows it should read $\text{Cov}(\mu_i,\mu_{i'}|\boldsymbol{y})$.]*

> ⚠ Check could not run (error): Cov(μ_i, μ_i'|y) = (1−λ_i)(1−λ_i')ν² for i ≠ i'. — NameError: name 'variance' is not defined

## 9.2 Small Area Estimation

The pooling of data across clusters takes places [sic] *(a handwritten stroke crosses the trailing "s", apparently correcting to "takes place")* when $\theta$ is being estimated (i.e., $\theta$ is integrated out). This induces a correlation across means a posteriori. This phenomenon is called a borrowing of strength *[hand-underlined, with a hook drawn into the left margin]*. In fact, this is the key idea in small area estimation. For a review see Pfeffermann (SS, 2013).

Typically only a small sample size is available for many areas, the small areas. The estimators for the small area effects, the random effects in the current example, become very unstable. Thus, there is a need to borrow strength from the ensemble *[hand-underlined with a wavy line]*. This also creates a need for good prior information. Where is that information in this example?

### 9.2.1 Form of estimation

Squared error Loss:

$$E\left\{\left(\mu_i - t(\boldsymbol{y})\right)^2 |\boldsymbol{y}\right\}$$

This is minimized when $t(\boldsymbol{y}) = E(\mu_i|\boldsymbol{y})$ (i.e., , [sic: doubled comma] the posterior mean of $\mu_i|\boldsymbol{y}$ ). This is the reason that $E(\mu_i|\boldsymbol{y})$ is called the Bayes estimator of $\mu_i$

> ✔ Verified: E{(μ − t)² | y} is uniquely minimized over constants t at t = E(μ|y).

$$E\left(\mu_i|\boldsymbol{y}\right) = \lambda_i \bar{y}_i + (1-\lambda_i)\hat{\theta}$$

$$\lambda_i = \frac{\delta^2}{\delta^2 + \sigma_i^2/n_i}$$

$$\hat{\theta} = \frac{\sum_{i=1}^{l} \lambda_i \bar{y}_i}{\sum_{i=1}^{1} \lambda_i}$$

*[sic: the upper limit of the denominator's sum is printed as "1"; it should be $l$, as in the numerator.]*

> ✔ Verified: θ̂ = Σλ_iȳ_i / Σλ_i is the minimum-variance linear unbiased estimator of θ, given Var(ȳ_i) = δ² + σ_i²/n_i = δ²/λ_i.

$$\bar{y}_i = \frac{\sum_{j=1}^{n_i} y_{ij}}{n_i}$$

### PDF page 92 (booklet page 87)

In small area estimation we call $E\left(\mu_i \mid \boldsymbol{y}\right)$ a shrinkage estimator, $\bar{y}_i$ is the direct estimator *[hand-underlined]* of $\mu_i$ and $\hat{\theta}$ is called a synthetic estimator *[hand-underlined]*. We also say that $E\left(\mu_i \mid \boldsymbol{y}\right)$ is a composite estimator *[hand-underlined, the stroke hooking upward at the end]* of $\mu_i$

Note: $E\left(\mu_i \mid \boldsymbol{y}\right) = \hat{\theta} + \lambda_i\left(\bar{y}_i - \hat{\theta}\right)$ is a regression estimation.

Illustrating shrinkage (Regression effect)

*[Figure: a square plot with the direct estimator $\bar{y}_i$ on the horizontal axis (labelled "Direct Estimator" at bottom right) and the Bayes estimator $E(\mu_i|y)$ on the vertical axis (labelled "Bayes Estimator" at top left). A 45° line runs from the lower-left corner to the upper-right corner. A horizontal line is drawn at height $\bar{y}$ and a vertical line at abscissa $\bar{y}$; they cross on the 45° line. About ten "×" data points are scattered near the 45° line. Dashed arrows show the shrinkage: points in the upper-right quadrant are carried left (toward the vertical $\bar{y}$ line) and down onto the 45° line, and points in the lower-left quadrant are carried right and up, i.e. every point is pulled toward $\bar{y}$.]*

Comment: Points above $\bar{y}$ are pulled down closer to $\bar{y}$

  Points below $\bar{y}$ are pushed up closer to $\bar{y}$

Note. In this picture $\hat{\theta} = \bar{y}$

**Two Extremes**

*[margin note, right of this section, handwritten: $\hat{\theta} = \dfrac{\sum_{i=1}^{\ell}\frac{1}{\delta^2+\sigma_i^2/n_i}\,\bar{y}_i}{\sum_{i=1}^{\ell}\frac{1}{\delta^2+\sigma_i^2/n_i}}$ (?), and below it "take $\delta^2 \to 0$" (?)]*

a. As $\delta^2 \to 0$, $\lambda_i \to 0$ for all

$$E\left(\mu_i \mid \boldsymbol{y}\right) \to \hat{\theta} = \frac{\sum_{i=1}^{l} \frac{n_i}{\sigma_i^2} \bar{y}_i}{\sum_{i=1}^{l} \frac{n_i}{\sigma_i^2}}, \qquad \text{Synthetic estimator}$$

*[Handwritten scratch strokes run over the printed $\sigma_i^2$ in both the numerator and the denominator of this fraction, with $\sigma_i^2$ re-written enlarged beneath the denominator's summand. These appear to be lecture scratch marks tracing the $\delta^2 \to 0$ limit of the margin formula above; the printed expression is unchanged.]*

> ✔ Verified: As $\delta^2\to0$, $\lambda_i=\delta^2/(\delta^2+\sigma_i^2/n_i)\to0$, the precision-weighted $\hat\theta\to\sum(n_i/\sigma_i^2)\bar y_i/\sum(n_i/\sigma_i^2)$, and $E(\mu_i|y)=\hat\theta+\lambda_i(\bar y_i-\hat\theta)$ tends to that synthetic estimator.

b. As $\delta^2 \to \infty$, $\lambda_i \to 1$ for all

$$E\left(\mu_i \mid \boldsymbol{y}\right) \to \bar{y}_i, \qquad \text{direct estmator [sic]}$$

> ✔ Verified: As $\delta^2\to\infty$, $\lambda_i\to1$ and $E(\mu_i|y)=\hat\theta+\lambda_i(\bar y_i-\hat\theta)\to\bar y_i$.

Remark. $\delta^2$ *(correction: a handwritten "2" is inserted as a superscript on the printed $\delta$)* measures the similarity among the clusters.

In (a) if $\sigma_i^2 = \sigma^2$, then all the clusters form one huge cluster, and there is complete pooling.

> ✔ Verified: With $\sigma_i^2=\sigma^2$ the synthetic estimator $\sum(n_i/\sigma_i^2)\bar y_i/\sum(n_i/\sigma_i^2)$ equals the pooled mean $\sum n_i\bar y_i/\sum n_i$ (complete pooling).

In (b) the clusters are very different, then it is sensible not to pool at all, and the direct estimator should be used.

### PDF page 93 (booklet page 88)

**Two More Extremes**

These are related to the sampling variance $\sigma_i^2/n_i$, and hence the sample size $n_i$

&nbsp;&nbsp;&nbsp;&nbsp;a. Suppose $\sigma_i^2/n_i \to 0$. Then $\lambda_i \to 1$, and $E\left(\mu_i \mid \boldsymbol{y}\right) \to \bar{y}_i$

&nbsp;&nbsp;&nbsp;&nbsp;b. Suppose $\sigma_i^2/n_i \to \infty$. Then $\lambda_i \to 0$, and $E\left(\mu_i \mid \boldsymbol{y}\right) \to \hat{\theta} = E\left(\mu_i \mid \boldsymbol{y}\right) \to \hat{\theta} = \frac{\sum_{j \neq i} \lambda_j y_j}{\sum_{j \neq i} \lambda_j}$ $\text{[sic: the fragment ``}E(\mu_i\mid\boldsymbol{y}) \to \hat\theta =\text{'' is printed twice]}$

> ✔ Verified: The two extreme cases of the shrinkage factor and the posterior mean, and the leave-one-out reduction of $\hat\theta$.

What does (a) say?

&nbsp;&nbsp;&nbsp;&nbsp;If the $i^{th}$ cluster is very homogenous or the sample size is large, there is no need to pool with other clusters.

(b) is remarkable!! What does it say?

&nbsp;&nbsp;&nbsp;&nbsp;It says that if the $i^{th}$ cluster is very heterogenous or the sample size is too small, then use the pooled estimator formed by the other clusters.

**9.2.2 Gaining Strength**

Recall $\mu_i \mid \boldsymbol{y} \sim N\left(\lambda_i \bar{y}_i + \left(1-\lambda_i\right)\hat{\theta},\; \left(1-\lambda_i\right)^2 \nu^2 + \left(1-\lambda_i\right)\delta^2\right)$

Suppose we have only the $i^{th}$ area:

$$y_{ij} \mid \mu_i \overset{iid}{\sim} N\left(\mu_i, \sigma_i^2\right)$$
$$p\left(\mu_i\right) = 1$$

Then,

$$\mu_i \mid \boldsymbol{y}_i \sim N\left(\bar{y}_i, \frac{\sigma_i^2}{m_i}\right)$$

> ✔ Verified: Flat prior on $\mu_i$ with an iid normal sample gives posterior $N(\bar y_i,\ \sigma_i^2/m_i)$.

NOTE: $\left(1-\lambda_i\right)^2 \nu^2 + \left(1-\lambda_i\right)\delta^2 = \frac{\sigma_i^2}{m_i}\left\{\frac{\lambda_i\left(1 + \sum_{j \neq i} \lambda_j\right)}{\lambda_i + \sum_{j \neq i} \lambda_j}\right\} < \frac{\sigma_i^2}{m_i}$

> ✔ Verified: The NOTE identity for the posterior variance, and the strict inequality $< \sigma_i^2/m_i$.

Remark: There will be a further gain in precision if we allow the $\sigma_i^2$ to share an effect, or if the $\sigma_i^2$ could be taken equal.

### PDF page 94 (booklet page 89)

*[Figure: a boxed sketch of two overlapping normal-shaped densities on a common horizontal axis. The left curve is low and wide, labeled by an arrow from the word "direct"; the right curve is tall and narrow, labeled by an arrow from the word "pooled". Three tick marks on the axis are labeled, left to right: $\bar{y}_i$ (under the mode of the "direct" curve), $\lambda_i\bar{y}_i + (1-\lambda_i)\bar{y}$, and $\bar{y}$ (at the right end). The figure illustrates shrinkage of the direct estimate toward the pooled mean.]*

**9.2.3 Empirical Bayes Statistics**

$$E\left(\mu_i \mid \boldsymbol{y}\right) = \lambda_i \bar{y}_i + \left(1-\lambda_i\right)\hat{\theta}$$

$$\lambda_i = \frac{\delta^2}{\delta^2 + \sigma_i^2/n_i}$$

$$\bar{y} = \frac{\sum_{i=1}^{l} \lambda_i \bar{y}_i}{\sum_{i=1}^{l} \lambda_i}$$

$$\hat{\mu}_i = \lambda_i \bar{y}_i + \left(1-\lambda_i\right)\hat{\theta}$$

> ⚠ Check could not run (error): Normal–normal posterior mean is the shrinkage estimator with weight λ_i = δ²/(δ² + σ_i²/n_i) — No algorithms are implemented to solve equation (-nn*(2*mu - 2*ybar_i)*exp(-(mu - theta)**2/(2*d2))*exp(-nn*(-mu + ybar_i)**2/(2*s2))/(2*s2) - (2*mu - 2*theta)*exp(-(mu - theta)**2/(2*d2))*exp(-nn*(-mu + ybar_i)**2/(2*s2))/(2*d2))*exp((mu - theta)**2/(2*d2))*exp(nn*(-mu + ybar_i)**2/(2*s2)) + 0

> ✔ Verified: ȳ = Σλ_iȳ_i / Σλ_i is exactly the precision-weighted mean under Ȳ_i ~ N(θ, δ²+σ_i²/n_i)

Because $\sigma_i^2$ and $\delta^2$ are really unknown, we substitute reasonable estimators for them in $\hat{\mu}_i$. Now we can proceed in one of two ways:

a. Continue as a Bayesian

$$\text{Bayes}\qquad \mu_i \mid \boldsymbol{y} \sim N\left(\hat{\mu}_i,\; \frac{\left(1-\lambda_i\right)^2 \nu^2 + \left(1-\lambda_i\right)\delta^2}{\hat{\delta}^2,\, \hat{\sigma}_i^2}\right)$$

> ✔ Verified: λ_i σ_i²/n_i = (1-λ_i) δ²

b. Evaluate $\mu_i$ under the marginal densities of the $Y_{ij}$

$$\text{empirical Bayes}\qquad \boldsymbol{Y_i} \sim N\left(\frac{\theta 1_{n_i},\, \sigma_i^2 I_{n_i} + \delta^2 J_{n_i, n_i}}{\hat{\theta} = \bar{y},\, \hat{\delta}^2,\, \sigma_i^2}\right)$$

> ✔ Verified: Marginal Y_i has mean θ·1 and covariance σ_i² I + δ² J

**9.2.4 Full Bayesian Analysis**

The main result can be rewritten as

$$\mu \mid \boldsymbol{y}, \sigma^2, \delta^2 \text{has a l-variate normal density}$$

*(The displayed line is set exactly as shown: no space between $\delta^2$ and "has" [sic]. In both boxed displays above, the horizontal rule separates the distributional parameters from the quantities at which they are evaluated; in the empirical-Bayes display the last entry is written $\sigma_i^2$ without a hat [sic], unlike $\hat{\delta}^2$.)*

### PDF page 95 (booklet page 90)

$$E\left(\mu_i \mid \boldsymbol{y}, \sigma^2, \delta^2\right) = \lambda_i \bar{y}_i + \left(1 - \lambda_i\right)\hat{\theta}$$

$$\operatorname{Cov}\left(\mu_i, \mu_j \mid \boldsymbol{y}, \boldsymbol{\sigma}^2, \delta^2\right) = \begin{cases} \left(1 - \lambda_i\right)^2 \nu^2 + \left(1 - \lambda_i\right)\delta^2, & i = j \\ \left(1 - \lambda_i\right)\left(1 - \lambda_j\right)\nu^2, & i \neq j \end{cases}$$

we need $p(\boldsymbol{\mu}|\boldsymbol{y}) = \int_0^\infty \cdots \int_0^\infty p\left(\boldsymbol{\mu} \mid \boldsymbol{y}, \sigma^2, \delta^2\right) p\left(\boldsymbol{\sigma}^2, \delta^2 | \boldsymbol{y}\right) d\boldsymbol{\sigma}^2 d\delta^2$

*(The booklet writes $\boldsymbol{y}$, $\boldsymbol{\mu}$, $\boldsymbol{\sigma}^2$ with under-tildes to indicate vectors.)*

Let $s_i^2 = \dfrac{\sum_{j=1}^{n_i}\left(y_{ij} - \bar{y}_i\right)^2}{n_i - 1}$. Then,

$$p\left(\sigma^2, \delta^2 | y\right) \propto \frac{\prod_{i=1}^{l}\left(1 - \lambda_i\right)^{1/2}}{\left(\sum_{i=1}^{l}\lambda_i\right)^{1/2}} \; \frac{1}{\prod_{i=1}^{l}\left(\sigma_i^2\right)^{\frac{a+n_i}{2}+1}} \; \frac{1}{\left(\delta^2\right)^{\frac{a}{2}} + 1}$$

$$\times \; e^{\frac{-1}{2}\left[\sum_{i=1}^{l}\left\{\frac{(n_i-1)s_i^2 + b}{\sigma_i^2}\right\} + \frac{b + \sum_{i=1}^{l}\lambda_i\left(\bar{y}_i - \bar{y}\right)^2}{\delta^2}\right]}, \qquad \sigma_1^2, \ldots, \sigma_l^2 \geq 0, \delta^2 > 0$$

*[sic: the last factor of the first line is printed as $\frac{1}{(\delta^2)^{a/2}+1}$; by analogy with the $\sigma_i^2$ factor the exponent is presumably $\frac{a}{2}+1$, i.e. $\frac{1}{(\delta^2)^{\frac{a}{2}+1}}$.]*

Remarks:
(1) If $\sigma_i^2 = \sigma^2$, there is just a 2-dimensional integral.
(2) Otherwise we need the Gibbs sampler. *[a short handwritten mark, [illegible], sits over the end of "sampler" — possibly an inserted "s" (?)]*
(3) $p(\mu|\boldsymbol{y})$ is no longer normally distributed.
(4) If $\sigma_i^2 = \sigma^2$ and $\delta^2 = \rho/(1-\rho)\sigma^2$, we can simply make random draws. *[the printed "$\rho$" in "$(1-\rho)$" is overwritten by hand, with a stroke leading down to the formula below]*

$$\rho = \frac{\delta^2}{\delta^2 + \sigma^2}$$

*[The display above is handwritten, centered beneath remark (4) — it inverts the relation $\delta^2 = \frac{\rho}{1-\rho}\sigma^2$ stated in the remark.]*

> ✔ Verified: The handwritten $\rho = \delta^2/(\delta^2+\sigma^2)$ is the inverse of the printed relation $\delta^2 = \frac{\rho}{1-\rho}\sigma^2$.

## 9.3 Benchmarking

Generally, in small area estimation because the data are sparse, models can fail. But, indeed, models are much needed in small area estimation.

So it is a good to study a model very carefully. [sic] Then model diagnostics (e.g., posterior predictive p-value, DIC, CPO, etc) However, one very important technique used in small area estimation is benchmarking. [sic] Data may be collected at both the small area levels and overall. So we require that the estimates at the small area level add up to the overall which is more precise. For example, data may be collected monthly as well as yearly, and it is best to constraint a model so that the monthly estimates add up to the yearly estimates which are more precise. This benchmarking constraint offers protection against model failure, See Pfeffermann and Tiller (JASA 2006)

There are two types of benchmarking. Internal benchmarking uses the current data to obtain the overall estimate. External benchmarking uses a past survey or census similar to the current one, to obtain the overall estimate. External benchmarking is preferred over internal benchmarking because it not double use the data. [sic] However, external benchmarking may lead to biased estimates and one has to be careful with the external data which may differ significantly from the current data. The key point though is that benchmarking can help reduce bias and possibly increase precision!

### PDF page 96 (booklet page 91)

Then we consider Bayesian benchmarking. Consider the Scott-Smith model

$$y_{ij}\mid\mu_i,\sigma^2 \overset{ind}{\sim} N\left(\mu_i,\sigma^2\right), \qquad j = 1,\cdots,N_i, i = 1,\cdots,l$$

$$\mu_i\mid\theta,\sigma^2,\rho \overset{iid}{\sim} N\left(\theta,\frac{\rho}{1-\rho}\sigma^2\right)$$

$$\pi\left(\theta,\sigma^2,\rho\right) \propto \frac{1}{\sigma^2}$$

One benchmarking constraint is

$$\frac{\sum_{i=1}^{l} N_i\mu_i}{\sum_{i=1}^{l} N_i} = \sum_{i=1}^{l} w_i\mu_i = \psi,\; w_i = \frac{N_i}{\sum_{i=1}^{l} N_i} \qquad i = 1,\cdots,l$$

> ✔ Verified: With $w_i = N_i/\sum_{i=1}^{l} N_i$, the weights sum to 1 and $\sum_i w_i\mu_i$ equals the $N_i$-weighted mean $\left(\sum_i N_i\mu_i\right)/\sum_i N_i$.

One can now put a prior on $\psi$. For example, $\psi \sim N\left(\theta_0,\delta_0\right)$, where $\theta_0$ and $\delta_0$ may be obtained from another survey or census. Less preferably, one may take $y_{ij}\mid\theta_0,\delta_0^2 \overset{iid}{\sim} N\left(\theta_0,\delta_0\right)$, $\pi\left(\theta_0,\delta_0^2\right) \propto \frac{1}{\delta_0^2}$, and $\theta_0$ and $\delta_0$ may be taken to be the posterior means or modes.

Then the Bayesian benchmarking model is

$$y_{ij}\mid\mu_i,\sigma^2 \overset{ind}{\sim} N\left(\mu_i,\sigma^2\right), \quad j = 1,\ldots,N_i, i = 1,\ldots,l$$

$$\mu_i\mid\theta,\sigma^2,\rho \overset{iid}{\sim} N\left(\theta,\frac{\rho}{1-\rho}\sigma^2\right)$$

$$\sum_{i=1}^{l} w_i\mu_i = \psi$$

$$\psi \sim N\left(\theta_0',\delta_0^2\right)$$

$$\pi\left(\theta,\sigma^2,\rho\right) \propto \frac{1}{\sigma^2}$$

&nbsp;&nbsp;&nbsp;&nbsp;The joint posterior density can be written and samples can be obtained using MCMC. The key point, though, is as follows. Let the transformation,

$$\phi = \sum_{i=1}^{l} w_i\mu_i - \psi$$

where we note $\pi = 0$ $\text{[sic: the constraint is } \phi = 0\text{]}$ is the constraint. Observe the one of $\mu_1,\cdots,\mu_l$ becomes redundant. So we transform $\mu_l$ keeping $\mu_1,\cdots,\mu_{l-1}$ untransformed. That is, the new parameters are $\mu_1,\cdots,\mu_{l-1},\phi$, and joint posterior of $\pi\left(\mu_1,\cdots,\mu_{l-1},\phi,\psi,\theta,\sigma^2,\rho|y\right)$. See Nandram and Sayit (SM,2011) for binary data.

We have worked extensively of [sic] the constraint of the following form

$$\sum_{i=1}^{l} w_i\bar{Y}_i = \bar{Y}$$

> ✔ Verified: With $w_i = N_i/\sum_i N_i$, $\bar{Y}_i = \frac{1}{N_i}\sum_{j=1}^{N_i} y_{ij}$, and $\bar{Y}$ the grand mean $\frac{\sum_i\sum_j y_{ij}}{\sum_i N_i}$, the benchmarking constraint $\sum_{i=1}^{l} w_i\bar{Y}_i = \bar{Y}$ holds identically.

### PDF page 97 (booklet page 92)

because our interest is on the finite population mean of each area. Here we do not need $\psi$. See Toto (PhD dissertation 2010), Toto and Nandram (JSPI 2010, JISAS, 2010),Nandram, Toto and Choi (JSCS, 2011)

Still there are many open problems which are associated with many variables (e.g. multinomial and extension of Nandram and Sayit (SM,2011) and hierarchical models with many stages. (Pfeffermann and Tiller JASA 2006). The problem is very difficult when transformations are made on the data and the benchmarking is done on the orig inal [sic] data. Also, how to benchmark the DPM model?

**9.4 Big Data**

In small area estimation the term, big data, refers to numerous areas (e.g. census tracts in the U.S.) Then standard MCMC methods do not work because the time to do the computation is prohibitive. So scientists doing big data analysis are mandated to use numerical approximations. The general problem is to make inference about, where

$$\pi(\boldsymbol{\mu}\mid\boldsymbol{y}) = \int \left\{ \prod_{i=1}^{l} \pi\left(\mu_i \mid \boldsymbol{\theta},\boldsymbol{y}\right) \right\} \pi(\boldsymbol{\theta}\mid\boldsymbol{y})\, d\boldsymbol{\theta}$$

Interest is on $\mu_i, i = 1,\cdots, l\,(l \approx 10^6)$ and $\boldsymbol{\theta}$ is a vector of nuisance parameters, but $\theta$ has very low dimensions ($\approx 2-5$). The problem then is how to account for the nuisance parameters $\boldsymbol{\theta}$ when $\mu_i, i = 1,\cdots, l$ are estimated.

In some cases, $\pi\left(\mu_i \mid \boldsymbol{\theta},\boldsymbol{y}\right)$ are in standard forms. But in other cases reasonable approximations are much needed. Suppose $\pi\left(\mu_i \mid \theta, y\right)$ are in standard form or we have approximated it with a standard form. Letting $\pi(\boldsymbol{\theta})$ denote the prior of $\boldsymbol{\theta}$,

$$\pi(\boldsymbol{\theta}\mid\boldsymbol{y}) \propto \prod_{i=1}^{l} \left[ \int_{-\infty}^{\infty} \pi\left(\mu_i \mid \boldsymbol{\theta},\boldsymbol{y}\right) d\mu_i \right] \pi(\boldsymbol{\theta})$$

and,

$$\pi(\boldsymbol{\theta}\mid\boldsymbol{y}) = \frac{\prod_{i=1}^{l} \left[ \int_{-\infty}^{\infty} \pi\left(\mu_i \mid \boldsymbol{\theta},\boldsymbol{y}\right) d\mu_i \right] \pi(\boldsymbol{\theta})}{\int \prod_{i=1}^{l} \left[ \int_{-\infty}^{\infty} \pi\left(\mu_i \mid \boldsymbol{\theta},\boldsymbol{y}\right) d\mu_i \right] \pi(\boldsymbol{\theta}) d\boldsymbol{\theta}}$$

That is,

$$\pi(\boldsymbol{\theta}\mid\boldsymbol{y}) = \frac{g(\boldsymbol{\theta})\pi(\boldsymbol{\theta})}{\int g(\boldsymbol{\theta})\pi(\boldsymbol{\theta})d\boldsymbol{\theta}}$$

> ✔ Verified: For a concrete standard form, the product-of-integrals collapses to $g(\theta)$, the ratio expression equals $g(\theta)\pi(\theta)/\int g(\theta)\pi(\theta)\,d\theta$, and the result integrates to 1.

where

$$g(\boldsymbol{\theta}) = \prod_{i=1}^{l} \left\{ \int_{-\infty}^{\infty} \pi\left(\mu_i \mid \boldsymbol{\theta},\boldsymbol{y}\right) d\mu_i \right\}$$

### PDF page 98 (booklet page 93)

One can approximate $g(\boldsymbol{\theta})$ as follows.

For simplicity consider the one dimensional case. We can ignore the minimal probability in the tails.

*[Figure: a boxed sketch of a unimodal, right-skewed density over a horizontal axis. The axis is marked with tick points labelled $a_1, a_2, a_3$ near the left, then $a_{g-1}$ and $a_g$ under the mode's right shoulder, and $a_G$ far to the right. A narrow vertical rectangle (one quadrature bin) is drawn between $a_{g-1}$ and $a_g$, its top meeting the curve; a small arrow points up to the interior of that bin, at the midpoint. Beneath the axis the figure carries the label*
$$\boldsymbol{\theta}_i = \frac{a_g + a_{g-1}}{2},\; g = 1,2,\ldots,G$$
*— note the index mismatch: the subscript is $i$ but the running index is $g$ [sic].]*

> ✔ Verified: the bin midpoint $(a_g + a_{g-1})/2$ lies strictly between $a_{g-1}$ and $a_g$.

So that

$$\pi(\theta) \approx \frac{g\left(\theta_g\right)\pi\left(\theta_g\right)}{\sum_{g=1}^{G} g\left(\theta_g\right)\pi\left(\theta_g\right)} = w_g,\; a_{g-1} < \theta < a_g,\, g = 1, 2, \cdots, G$$

> ✔ Verified: the quadrature weights $w_g = g(\theta_g)\pi(\theta_g) / \sum_{h=1}^G g(\theta_h)\pi(\theta_h)$ sum to one.

In low dimensions it is possible to use quadrature, but in higher dimensions one has to use a similar approximation as we discussed above. Then,

$$\pi(\boldsymbol{\mu}|\boldsymbol{y}) \approx \sum_{g=1}^{G}\left[\prod_{i=1}^{l} \pi\left(\mu_i | \boldsymbol{\theta}_g, \boldsymbol{y}\right)\right] w_g$$

and

$$\pi\left(\mu_i | \boldsymbol{g}\right) \approx \sum_{g=1}^{G} \pi\left(\mu_i | \boldsymbol{\theta}_g, \boldsymbol{y}\right) w_g$$

*(the conditioning symbol is printed as $\boldsymbol{g}$ [sic]; from the context this should be $\boldsymbol{y}$, the marginal of the mixture above)*

> ✔ Verified: marginalizing $\pi(\boldsymbol{\mu}|\boldsymbol{y}) \approx \sum_g \left[\prod_{i=1}^{l}\pi(\mu_i|\theta_g,\boldsymbol{y})\right] w_g$ over $\mu_j$ for $j\neq i$ returns $\sum_g \pi(\mu_i|\theta_g,\boldsymbol{y}) w_g$.

Some computation can be done using integrated nested Laplace approximations (INLA); See Rue, Martino and Chopin (JRSSB, 2009).

### PDF page 99 (booklet page 94)

**9.5 Appendix**

<u>Binomial Model Example</u>

$$y_i|\nu_i \overset{iid}{\sim} \text{Bin}\left(n_i, \frac{e^{\nu_i}}{1+e^{\nu_i}}\right), i = 1,\cdots, l$$

$$\nu_i|\theta,\delta^2 \overset{iid}{\sim} N\left(\theta,\delta^2\right), \pi\left(\theta,\delta^2\right)\ \text{ hyperprior}$$

Then

$$\pi\left(\boldsymbol{\nu},\theta,\delta^2|\boldsymbol{y}\right) \propto \prod_{i=1}^{l}\left\{\frac{e^{y_i\nu_i}}{\left(1+e^{\nu_i}\right)^{n_i}}\frac{1}{\sqrt{2\pi\delta^2}}e^{-\frac{1}{2\delta^2}\left(\nu_i-\theta\right)^2}\right\}\pi\left(\theta,\delta^2\right)$$

*(The booklet writes $\nu$ and $y$ with under-tildes to indicate vectors.)*

Look at

$$\pi\left(\nu_i|\boldsymbol{y}\right) \propto \frac{e^{y_i\nu_i}}{\left(1+e^{\nu_i}\right)^{n_i}}, i = 1,\cdots, l\ (\text{i.e., }\ \text{likelihood })$$

<u>Aside</u>

Set $\delta\left(\nu_i\right) = y_i\nu_i - n_i\log\left(1+e^{\nu_i}\right)$. Then *[sic: the function is named $\delta(\nu_i)$ here but is written $\Delta$ in the derivatives that follow; also $\delta$ clashes with the hyperparameter $\delta^2$ above]*

$$\frac{\partial \Delta}{\partial \nu_i} = y_i - \frac{n_i e^{\nu_i}}{1+e^{\nu_i}}$$

> ✔ Verified: First derivative of the binomial log-likelihood kernel $\Delta(\nu)=y\nu-n\log(1+e^{\nu})$ is $y - n e^{\nu}/(1+e^{\nu})$.

$$\frac{\partial^2 \Delta}{\partial \nu_i^2} = -n_i\left\{\frac{e^{\nu_i}\left(1+e^{\nu_i}\right)-e^{2\nu_i}}{\left(1+e^{\nu_i}\right)^2}\right\} = -n_i\frac{e^{\nu_i}}{\left(1+e^{\nu_i}\right)^2}$$

> ✔ Verified: Second derivative equals $-n_i\{(e^{\nu}(1+e^{\nu})-e^{2\nu})/(1+e^{\nu})^2\}$ and simplifies to $-n_i e^{\nu}/(1+e^{\nu})^2$.

Setting $\frac{\partial\Delta}{\partial\nu_i} = 0$, get $\frac{e^{\hat{\nu}_i}}{1+e^{\hat{\nu}_i}} = \frac{y_i}{n_i}$. That is

$$\hat{\nu}_i = \log\left(\frac{y_i}{n_i-y_i}\right), i = 1,\cdots, l$$

> ✔ Verified: The MLE solves $e^{\hat\nu}/(1+e^{\hat\nu})=y/n$, giving $\hat\nu=\log(y/(n-y))$; and it is a maximum.

Adjusting by using empirical logistic transform is needed.

$$\tilde{\nu}_i = \log\left(\frac{y_i+\frac{1}{2}}{n_i-y_i+\frac{1}{2}}\right)$$

$\frac{1}{2}$ to 0s and 1s (like Jeffreys prior). This is needed when $y_i = 0$ or $n_i$( MLE does not exist).

However,

$$\text{Var}\left(\hat{\nu}_i\right) = \left(\frac{n_i e^{\hat{\nu}_i}}{\left(1+e^{\hat{\nu}_i}\right)^2}\right)^{-1} = \hat{\sigma}_i^2$$

> ✔ Verified: $\hat\sigma_i^2 = \big((1+e^{\hat\nu})^2/(n e^{\hat\nu})\big)$ is the inverse observed information and equals $n/(y(n-y))$.

is always defined for the empirical logistic transform (Cox, 1970). We have approximately

$$\hat{\nu}_i \sim N\left(\nu_i, \hat{\sigma}_i^2\right)$$

### PDF page 100 (booklet page 95)

Now

$$y_i\nu_i - n_i log\left(1+e^{\nu_i}\right) \approx y_i\hat{\nu}_i - n_i\log\left(1+e^{\hat{\nu}_i}\right) + \left(y_i - \frac{n_ie^{\hat{\nu}_i}}{1+e^{\hat{\nu}_i}}\right)\left(\nu_i - \hat{\nu}_i\right)$$

$$-\,\frac{1}{2}\frac{n_ie^{\hat{\nu}_i}}{\left(1+e^{\hat{\nu}_i}\right)^2}\left(\nu_i - \hat{\nu}_i\right)^2 + \cdots$$

> ✔ Verified: The linear and quadratic Taylor coefficients of $y\nu - n\log(1+e^{\nu})$ about $\hat{\nu}$ are $y - ne^{\hat\nu}/(1+e^{\hat\nu})$ and $-\tfrac12 n e^{\hat\nu}/(1+e^{\hat\nu})^2$.

But $\hat{\nu}_i$ are MLEs, so second term $=0$ and first term is a constant. So

$$\pi\left(\nu,\theta,\delta^2|dat\right) \propto \prod_{i=1}^{l}\exp\left\{-\frac{1}{2\hat{\sigma}_i^2}\left(\nu_i - \hat{\nu}_i\right)^2\right\}\frac{1}{\sqrt{2\pi\delta^2}}e^{-\frac{1}{2\delta^2}\left(\nu_i-\theta\right)^2}\pi\left(\theta,\delta^2\right)$$

approximately. This is really Laplace approximation.

Now,

$$\frac{1}{\hat{\sigma}_i^2}\left(\nu_i-\hat{\nu}_i\right)^2 + \frac{1}{\delta^2}\left(\nu_i-\theta\right)^2 = \left(\frac{1}{\hat{\sigma}_i^2}+\frac{1}{\delta^2}\right)\left(\nu_i - \frac{\frac{1}{\hat{\sigma}_i^2}\hat{\nu}_i + \frac{1}{\delta^2}\theta}{\frac{1}{\hat{\sigma}_i^2}+\frac{1}{\delta^2}}\right)^2 + \frac{\frac{1}{\hat{\sigma}_i^2}\frac{1}{\delta^2}}{\frac{1}{\hat{\sigma}_i^2}+\frac{1}{\delta^2}}\left(\theta-\hat{\nu}_i\right)^2$$

> ✔ Verified: Completing the square: $\frac{1}{s}(\nu-\hat\nu)^2+\frac{1}{d}(\nu-\theta)^2 = (\frac1s+\frac1d)\left(\nu-\frac{\hat\nu/s+\theta/d}{1/s+1/d}\right)^2+\frac{(1/s)(1/d)}{1/s+1/d}(\theta-\hat\nu)^2$.

$\lambda_i = \frac{\frac{1}{\hat{\sigma}_i^2}}{\frac{1}{\hat{\sigma}_i^2}+\frac{1}{\delta^2}} = \frac{\delta^2}{\delta^2+\hat{\sigma}_i^2}$. We get

> ✔ Verified: $\dfrac{1/s}{1/s+1/d} = \dfrac{d}{d+s}$.

$$\frac{1}{\hat{\sigma}_i^2}\left(\nu_i-\hat{\nu}_i\right)^2 + \frac{1}{\delta^2}\left(\nu_i-\theta\right)^2 = \frac{1}{\lambda_i\hat{\sigma}_i^2}\left(\nu_i - \left(\lambda_i\hat{\nu}_i + \left(1-\lambda_i\right)\theta\right)\right)^2 + \frac{\lambda_i}{\delta^2}\left(\theta-\hat{\nu}_i\right)^2$$

> ✔ Verified: With $\lambda=d/(d+s)$: $\frac{1}{s}(\nu-\hat\nu)^2+\frac{1}{d}(\nu-\theta)^2=\frac{1}{\lambda s}\big(\nu-(\lambda\hat\nu+(1-\lambda)\theta)\big)^2+\frac{\lambda}{d}(\theta-\hat\nu)^2$.

Thus, approximately

$$\pi\left(\nu,\theta,\delta^2|dat\right) \propto \prod_{i=1}^{l}\left\{e^{-\frac{1}{2\lambda_i\hat{\sigma}_i^2}\left(\nu_i-\left(\lambda_i\hat{\nu}_i+\left(1-\lambda_i\right)\theta\right)\right)^2}e^{-\frac{\lambda_i}{2\delta^2}\left(\theta-\hat{\nu}_i\right)^2}\frac{1}{\sqrt{2\pi\hat{\sigma}_i^2}\sqrt{2\pi\hat{\delta}^2}}\right\}\pi\left(\theta,\delta^2\right)$$

That is, approximately

$$\nu_i|\theta,\delta^2,dat \overset{ind}{\sim} N\left(\lambda_i\hat{\nu}_i + \left(1-\lambda_i\right)\theta,\;\left(1-\lambda_i\right)\delta^2\right)$$

> ✔ Verified: The conditional variance $\lambda\hat\sigma^2$ equals the stated $(1-\lambda)\delta^2$, and the stated mean matches the precision-weighted mean.

Then, integrating out $\nu_i$, we get

$$\pi\left(\theta,\delta^2|dat\right) \propto \left\{\prod_{i=1}^{l}\lambda_i\hat{\sigma}_i^2\right\}^{\frac{1}{2}}\prod_{i=1}^{l}\left\{\frac{1}{\sqrt{2\pi\hat{\sigma}_i^2}\sqrt{2\pi\hat{\delta}^2}}\right\}\prod_{i=1}^{l}e^{-\frac{\lambda_i}{2\delta^2}\left(\theta-\hat{\nu}_i\right)^2}\pi\left(\theta,\delta^2\right)$$

> ✔ Verified: $\int_{-\infty}^{\infty}\exp\!\big[-\frac{1}{2\lambda s}(\nu-m)^2\big]\,d\nu = \sqrt{2\pi}\,(\lambda s)^{1/2}$.

### PDF page 101 (booklet page 96)

Let $\overline{\nu} = \frac{\sum_{i=1}^{l} \lambda_i \hat{\nu}_i}{\sum_{i=1}^{l} \lambda_i}$. Then

$$\sum_{i=1}^{l} \lambda_i \left(\theta - \hat{\nu}_i\right)^2 = \sum_{i=1}^{l} \lambda_i \left(\theta - \overline{\nu} + \overline{\nu} - \hat{\nu}_i\right)^2 = \sum_{i=1}^{l} \lambda_i (\theta - \overline{\nu})^2 + \sum_{i=1}^{l} \lambda_i \left(\hat{\nu}_i - \overline{\nu}\right)^2$$

> ✔ Verified: With $\overline{\nu}=\sum\lambda_i\hat\nu_i/\sum\lambda_i$, the weighted sum of squares decomposes as $\sum\lambda_i(\theta-\hat\nu_i)^2=\sum\lambda_i(\theta-\overline\nu)^2+\sum\lambda_i(\hat\nu_i-\overline\nu)^2$.

That is

$$\pi\left(\theta, \delta^2 \mid dat\right) \propto \prod_{i=1}^{l} \left(\frac{\lambda_i}{\delta^2}\right)^{\frac{1}{2}} e^{-\frac{1}{2\delta^2}\left(\sum_{i=1}^{l}\lambda_i\right)\left(\theta - \overline{\nu}\right)^2} e^{-\frac{1}{2\delta^2}\sum_{i=1}^{l}\lambda_i\left(\hat{\nu}_i - \overline{\nu}\right)^2} \pi\left(\theta, \delta^2\right)$$

So, approximately, (letting $\pi(\theta) = 1$)

$$\theta \mid \delta, \boldsymbol{y} \sim N\left(\overline{\nu}, \frac{\delta^2}{\sum_{i=1}^{l} \lambda_i}\right)$$

> ✔ Verified: The exponential kernel in $\theta$ is proportional to a $N(\overline\nu,\ \delta^2/\sum\lambda_i)$ density.

and

$$\pi\left(\delta^2 \mid dat\right) \propto \prod_{i=1}^{l} \left(\frac{\lambda_i}{\delta^2}\right)^{\frac{1}{2}} \left(\frac{\delta^2}{\sum_{i=1}^{l} \lambda_i}\right)^{\frac{1}{2}} e^{-\frac{1}{2\delta^2}\sum_{i=1}^{l} \lambda_i \left(\hat{\nu}_i - \overline{\nu}\right)^2} \pi\left(\delta^2\right)$$

$$= \prod_{i=1}^{l} \left\{ \frac{\lambda_i}{\sum_{i=1}^{l} \lambda_i} \right\}^{\frac{1}{2}} e^{-\frac{1}{2\delta^2}\sum_{i=1}^{l} \lambda_i \left(\hat{\nu}_i - \overline{\nu}\right)^2} \pi\left(\delta^2\right)$$

> ✔ Verified: $(\lambda_i/\delta^2)^{1/2}(\delta^2/\sum_j\lambda_j)^{1/2}=(\lambda_i/\sum_j\lambda_j)^{1/2}$ — the $\delta^2$ cancels.

<u>Aside</u>

$f(\sigma) = \frac{2}{\pi(1+\sigma^2)}, \sigma > 0$, half Cauchy (proper)

> ✔ Verified: The half-Cauchy density $f(\sigma)=\frac{2}{\pi(1+\sigma^2)}$ on $\sigma>0$ is proper (integrates to 1).

$\gamma = \sigma^2$. Then $\sigma = \sqrt{\gamma}$ and $\frac{d\sigma}{d\gamma} = -\frac{1}{2\sqrt{\gamma}}$ $\text{[sic: the derivative of }\sqrt{\gamma}\text{ is }+\tfrac{1}{2\sqrt{\gamma}}\text{; the sign is wrong, though only }|d\sigma/d\gamma|\text{ is used below]}$

That is,

$$f\left(\sigma^2\right) = \frac{1}{\pi\left(1+\sigma^2\right)\sqrt{\sigma^2}}, \sigma^2 > 0$$

> ✔ Verified: Under $\gamma=\sigma^2$ the half-Cauchy becomes $f(\gamma)=\frac{1}{\pi(1+\gamma)\sqrt{\gamma}}$, a proper density on $(0,\infty)$.

Let $\phi = \frac{1}{1+\sigma^2}$, $\sigma^2 = \frac{1-\phi}{\phi}$; $\frac{d\sigma^2}{d\phi} = \frac{-\phi - (1-\phi)}{\phi^2} = -\frac{1}{\phi^2}$

> ✔ Verified: $\phi=\frac{1}{1+\sigma^2}$ inverts to $\sigma^2=\frac{1-\phi}{\phi}$, with $\frac{d\sigma^2}{d\phi}=-\frac{1}{\phi^2}$.

$$\pi(\phi) = \frac{\phi}{\pi\sqrt{\frac{1-\phi}{\phi}}}\,\frac{1}{\phi^2}$$

$$= \frac{\phi^{\frac{3}{2}}}{\pi\phi^2\sqrt{1-\phi}}$$

$$= \frac{1}{\pi\sqrt{\phi(1-\phi)}}, 0 < \phi < 1 \;\left(i.e.\, \phi \sim \text{Beta}\left(\frac{1}{2}, \frac{1}{2}\right)\right)$$

> ⚠ Check FAILED: The transformed density is $\pi(\phi)=\frac{1}{\pi\sqrt{\phi(1-\phi)}}$ on $(0,1)$, i.e. exactly the Beta(1/2, 1/2) density. — the stated result did not reproduce (see verification log)

### PDF page 102 (booklet page 97)

Then,

$$\pi(\phi \mid dat) \propto \left[\prod_{i=1}^{l}\left\{\frac{\lambda_i}{\sum_{i=1}^{l}\lambda_i}\right\}^{\frac{1}{2}} e^{-\frac{1}{2\delta^{2}}\sum_{i=1}^{l}\lambda_i\left(\hat{\nu}_i-\bar{\hat{\nu}}\right)^{2}}\right]_{\delta^{2}=\frac{1-\phi}{\phi}}\;\frac{1}{\{\phi(1-\phi)\}^{\frac{1}{2}}}$$

$$\lambda_i = \frac{\delta^{2}}{\delta^{2}+\hat{\sigma}_i^{2}},\; i = 1,\cdots,l$$

> ✔ Verified: The shrinkage weights $\lambda_i$ lie in $(0,1)$, the normalized weights lie in $(0,1)$ and sum to 1, and the bracketed factor of $\pi(\phi\mid dat)$ is $\le 1$.

Remarks.

(1) The approximate posterior density is proper, provided $y_i \neq 0$ or $n_i$ and $\pi(\theta)$ is proper

> ⚠ Check FAILED: The factor $\{\phi(1-\phi)\}^{-1/2}$ is integrable on $(0,1)$, with $\int_0^1\{\phi(1-\phi)\}^{-1/2}d\phi=\pi$. — the stated result did not reproduce (see verification log)

(2) The least [sic] posterior density is also proper because

$$0 < \frac{e^{y_i\nu_i}}{\left(1+e^{\nu_i}\right)^{m_i}} < 1$$

> ✔ Verified: $0 < e^{y\nu}/(1+e^{\nu})^{m} < 1$ for all real $\nu$ and integers $0\le y\le m$, $m\ge 1$.

provided $\pi(\theta)$ is proper

(3) In high-dimensional problems a similar approximation is feasible.

(4) For low-dimensional problems, the exact calculations can be done using the SIR algorithm.

*(Remark (1) writes the binomial index as $n_i$ while the display in Remark (2) writes $m_i$; both are reproduced as printed.)*

### PDF page 103 (booklet page 98)

*(Blank page — running header only.)*

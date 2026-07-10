# Chapter 10 — GIBBS SAMPLER
*(PDF pages 104–121; booklet pages 99–116)*


### PDF page 104 (booklet page 99)

# Chapter 10 — GIBBS SAMPLER

**10.1 What is the Gibbs sampler?**

The Gibbs sampler is a Markov chain Monte Carlo (MCMC) method for generating a sample from a multivariate posterior density.

Consider three random variables $U, V, W$. The joint density of $U, V, W$ is inaccessible. Suppose the conditional densities $U|V, W$, $V|U, W$ and $W|U, V$ are all simple (i.e., samples can be draw [sic] easily from each of them). Denote the conditional densities by $[U|V, W]$, $[V|U, W]$ and $[W|U, V]$, and the joint density by $[U, V, W]$.

Remark: If the joint density of $[U, V, W]$ is positive on its entire domain, then the joint density $[U, V, W]$ is fully determined by the three conditional densities $[U|V, W]$, $[V|U, W]$ and $[W|U, V]$.

*[in the Remark, the clauses "If the joint density of $[U,V,W]$ is positive on its entire domain" and "is fully determined by the three conditional densities" are each hand-underlined]*

The Gibbs sampler generates a random sample from $[U, V, W]$ as follows:
Let $U^{(0)}, V^{(0)}, W^{(0)}$ be starting values.

$$\text{Draw } U^{(1)} \text{ from } [U|V^{(0)}, W^{(0)}]$$
$$V^{(1)} \text{ from } [V|U^{(1)}, W^{(0)}]$$
$$W^{(1)} \text{ from } [W|U^{(1)}, V^{(1)}]$$

Thus, we obtain the first iterate $(U^{(1)}, V^{(1)}, W^{(1)})$.

*[a small stray hand mark (dot/tick) sits in the blank space to the left of the next display]*

$$\text{Draw } U^{(2)} \text{ from } [U|V^{(1)}, W^{(1)}]$$
$$V^{(2)} \text{ from } [V|U^{(2)}, W^{(1)}]$$
$$W^{(2)} \text{ from } [W|U^{(2)}, V^{(2)}]$$

Thus, we obtain the second iterate $(U^{(2)}, V^{(2)}, W^{(2)})$.
After a large number, $B$, of interations [sic], we obtain $(U^{(B)}, V^{(B)}, W^{(B)})$.

### PDF page 105 (booklet page 100)

**Main result**

Under very mild conditions, *Geman and Geman (IEEE, 1984)* showed that

$$(U^{(n)}, V^{(n)}, W^{(n)}) \overset{d}{\to} (U,V,W) \sim [U,V,W] \text{ as } n \to \infty$$

`Remark (1):` The joint density can be approximated by the empirical distribution of $M$ values $(U^{(n)}, V^{(n)}, W^{(n)}), n = B+1, ..., B+M$, where $B$ is large enough so that the Gibbs sampler has converged, and $M$ is chosen to give sufficient precision to the empirical distribution of interest.

`Remark (2):` $f(U^{(t+1)}|U^{(t)}, U^{(t-1)}, ..., U^{(0)}) = f(U^{(t+1)}|U^{(t)})$ at the $t$-iterate (this also holds for $V$ and $W$). Hence the name Markov Chain *(a stray handwritten diagonal pen slash crosses the "C" of "Chain"; nothing is written in its place)*. Then the iterates are correlated. How do we get a random sample from the posterior density? More importantly *(a small stray handwritten pen tick sits just below this word)*, how do we check for convergence of the Gibbs sampler?

## Illustration (One-way random effects model)

$$y_{i1}, ..., y_{in_i} | \mu_i, \sigma^2 \;\overset{iid.}{\sim}\; N(\mu_i, \sigma^2),\, i = 1, ..., \ell$$

$$\mu_1, ..., \mu_\ell | \theta, \delta^2 \;\overset{iid.}{\sim}\; N(\theta, \delta^2)$$

$$\underbrace{p(\theta) = 1,\; \sigma^{-2} \sim \text{Gamma}\Big(\frac{a}{2}, \frac{b}{2}\Big),\; \delta^{-2} \sim \text{Gamma}\Big(\frac{c}{2}, \frac{d}{2}\Big)}_{\text{independent}}$$

Parameters are $(\mu, \theta, \sigma^2, \delta^2)$, data are $y = \{y_{ij}, j = 1, ..., n_i,\; i = 1, ..., \ell\}$

*(The booklet writes $\mu$ and $y$ with under-tildes to indicate vectors.)*

The joint posterior density is

$$p(\mu, \theta, \sigma^2, \delta^2 | y) \propto p(y | \mu, \theta, \sigma^2, \delta^2) p(\mu, \theta, \sigma^2, \delta^2) \;\;-\!-\textit{Bayes' theorem.}$$

$$= p(y | \mu, \theta, \sigma^2, \delta^2) p(\mu | \theta, \sigma^2, \delta^2) p(\theta | \sigma^2, \delta^2) p(\sigma^2) p(\delta^2)$$

$$= p(y | \mu, \sigma^2) p(\mu | \theta, \delta^2) p(\theta) p(\sigma^2) p(\delta^2)$$

Thus,

$$p(\mu, \theta, \sigma^2, \delta^2 | y) \propto \left\{ \prod_{i=1}^{\ell} \prod_{j=1}^{n_i} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{1}{2\sigma^2}(y_{ij} - \mu_i)^2} \right\} \left\{ \prod_{i=1}^{\ell} \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(\mu_i - \theta)^2} \right\} \times$$

$$\times \left\{ \Big(\frac{1}{\sigma^2}\Big)^{\frac{a}{2}+1} e^{-\frac{b}{2\sigma^2}} \right\} \left\{ \Big(\frac{1}{\delta^2}\Big)^{\frac{c}{2}+1} e^{-\frac{d}{2\delta^2}} \right\}$$

$$-\infty < \mu_i, \theta < \infty, \sigma^2, \delta^2 > 0$$

> ✔ Verified: Change of variables from $\sigma^{-2}\sim\text{Gamma}(a/2,b/2)$ gives $p(\sigma^2)\propto(1/\sigma^2)^{a/2+1}e^{-b/(2\sigma^2)}$.

Conditional posterior densities (cpds)

$$\mu_i | \theta, \sigma^2, \delta^2, y \;\overset{iid.}{\sim}\; \mathcal{N}\{\lambda_i \bar{y}_i + (1 - \lambda_i)\theta,\, (1 - \lambda_i)\delta^2\}$$

> ✔ Verified: The cpd of $\mu_i$ is $N(\lambda_i\bar y_i+(1-\lambda_i)\theta,\ (1-\lambda_i)\delta^2)$ with $\lambda_i=n_i\delta^2/(n_i\delta^2+\sigma^2)$.

### PDF page 106 (booklet page 101)

where $\bar{y}_i = \sum_{j=1}^{n_i} \frac{y_{ij}}{n_i}$ and $\lambda_i = \delta^2/(\delta^2 + \sigma^2/n_i)$, $i = 1, ..., \ell$.

$$\theta \mid \mu, \sigma^2, \delta^2, y \quad \sim \quad \mathcal{N}\left(\bar{\mu}, \frac{\delta^2}{\ell}\right)$$

> ✔ Verified: With $\mu_i \mid \theta \sim \mathcal{N}(\theta, \delta^2)$ independent and a flat prior on $\theta$, the conditional posterior of $\theta$ is $\mathcal{N}(\bar\mu, \delta^2/\ell)$.

where $\bar{\mu} = \sum_{j=1}^{\ell} \frac{\mu_j}{\ell}$.

$$\sigma^{-2} \mid \mu, \theta, \delta^2, y \quad \sim \quad \text{Gamma}\left\{\frac{a + \sum_{i=1}^{\ell} n_i}{2}, \frac{b + \sum_{i=1}^{\ell}\sum_{j=1}^{n_i}(y_{ij} - \mu_i)^2}{2}\right\}$$

> ✔ Verified: Prior $\sigma^{-2}\sim$ Gamma$(a/2, b/2)$ with $y_{ij}\mid\mu_i,\sigma^2\sim\mathcal{N}(\mu_i,\sigma^2)$ gives full conditional Gamma$\{(a+\sum n_i)/2,\;(b+\sum\sum(y_{ij}-\mu_i)^2)/2\}$.

$$\delta^{-2} \mid \mu, \theta, \sigma^2, y \quad \sim \quad \text{Gamma}\left\{\frac{c + \ell}{2}, \frac{d + \sum_{i=1}^{\ell}(\mu_i - \theta)^2}{2}\right\}$$

> ✔ Verified: Prior $\delta^{-2}\sim$ Gamma$(c/2, d/2)$ with $\mu_i\mid\theta,\delta^2\sim\mathcal{N}(\theta,\delta^2)$ gives full conditional Gamma$\{(c+\ell)/2,\;(d+\sum(\mu_i-\theta)^2)/2\}$.

Starts $\hat{\mu}_i = \bar{y}_i, i = 1, ..., \ell$

*[small hand tick-mark in the left margin (?)]*

$$\hat{\theta} = \frac{\sum_{i=1}^{\ell} n_i \bar{y}_i}{\sum_{i=1}^{\ell} n_i}; \quad \hat{\sigma}^2 = \frac{\sum_{i=1}^{\ell}\sum_{j=1}^{n_i}(y_{ij} - \bar{y}_i)^2}{\sum_{i=1}^{\ell}(n_i - 1)}; \quad \hat{\delta}^2 = \frac{\sum_{i=1}^{\ell}(\bar{y}_i - \hat{\theta})^2}{\ell - 1}.$$

## 10.2 How to assess convergence?

We describe three *[the word "three" is hand-underlined with a scribbled double stroke]* tests that can be used to ensure a "random" sample from the joint posterior density through the Gibbs sampler.

`Remark:` Our ultimate objective is to get a random sample from the joint posterior density.

### 10.2.1 Trace plots

Trace plots are used to assess convergence, and to find out when the Markov chain has gone through the transient stage *["transient stage" is hand-underlined]*. These are plots of the parameter values versus their order. We "burn in" B iterates, and *["B iterates, and" is hand-underlined]* then $B + 1, B + 2, ..., B + M$ iterates form a sample from the joint posterior density.
What is B? See Figure 1 for trace plots.

*[A large blank space follows here: Figure 1 is referenced in the text but no figure is printed on this page.]*

If $\theta_1$ and $\theta_2$ are the only parameters, we should "burn in" about 500 iterates. The chain has gone through the transient state after roughly $B = 500$ interates [sic].

### 10.2.2 Auto correlation

Let $U^{(1)}, U^{(2)}, ..., U^{(M)}$ be $M$ iterates for variable $U$ after initial convergence. The auto correlation coefficient of the sequence $\{U^{(i)}\}$ at lag $k$ is:

$$r_k = \frac{\sum_{i=1}^{N-k}(U^{(i)} - \bar{U})(U^{(i+k)} - \bar{U})}{\sum_{i=1}^{N}(U^{(i)} - \bar{U})^2}, \;\text{ where } \bar{U} = N^{-1}\sum_{i=1}^{N} U^{(i)},$$

*[The displayed formula uses $N$ where the preceding sentence defines $M$ iterates; transcribed as printed.]*

### PDF page 107 (booklet page 102)

*[Figure: two hand-drawn trace plots, one above the other. The upper plot has vertical axis $\theta_1^{(t)}$ and horizontal axis $t$ (order), with a tick labelled "100"; the trace starts high, dips into a broad trough, then settles into small oscillations about the axis. The lower plot has vertical axis $\theta_2^{(t)}$ and horizontal axis $t$ (order), with a tick labelled "500"; its trace swings well below and above the axis before flattening out much later. Beneath the lower trace runs a partly legible handwritten line: "1(?) ... [illegible] ... parameters we should(?)".]*

*[margin note, left of the figure, circled by hand: "Caterpillar shape". A long stroke runs from the oval down to a hand-drawn sketch of a vertical axis with a dense fuzzy band of overlapping squiggles beside it — the instructor's sketch of a well-mixed (caterpillar-shaped) trace.]*

Figure 10.1: Trace plots for assessing convergence

and its asymptotic (large $N$) standard error is

$$ste_k = \{\frac{N-k}{N(N+2)}\}^{\frac{1}{2}}.$$

> ✔ Verified: $ste_k=\{(N-k)/(N(N+2))\}^{1/2}$ squares to the exact white-noise variance $(N-k)/(N(N+2))$ of $r_k$, and $\sqrt{N}\,ste_k\to 1$ as $N\to\infty$ for fixed $k$.

Correlation at lag $k$

| | |
|---|---|
| $U^{(1)}$ | $U^{(k+1)}$ |
| $U^{(2)}$ | $U^{(k+2)}$ |
| ... | ... |
| $U^{(N-k)}$ | $U^{(N)}$ |

Correlation is negligible when $r_k$ lies in $\left(-2ste_k, 2ste_k\right)$.

> ✔ Verified: the printed band $(-2ste_k, 2ste_k)$ reduces to the standard $\pm 2/\sqrt{N}$ significance band as $N\to\infty$ with $k$ fixed.

Remark : When the correlation washes out quickly, we say that the Markov chain is strongly mixing (desirable!). When the correlation does not wash out quickly, there are problems with convergence (e.g., a parameter might be weakly identified). *[the word "strongly" is hand-underlined with a wavy line running past the end of the line; a short curved stroke sits in the left margin beside "mixing"; a horizontal hand-stroke runs through "convergence"; "might be weakly identified" is hand-underlined]*

See Figure 2 for correlograms.

Look at all the parameters in the joint posterior density, and use the largest $k_0$, called $k_0^{\star}$. This is the number of iterates we will skip after convergence to obtain a "random" sample.

Remark : We compute $r_k$ for $k = 1, 2, ..., m$, where $m < N$. There is little point in calculating $r_k$ for values of $k$ greater than $N/4$. I usually take $m = 20$.

### PDF page 108 (booklet page 103)

*[Figure 10.2: a hand-drawn correlogram, titled "Correlograms". The vertical axis is labeled "$m_k$" (?) and the horizontal axis "$k$". Two horizontal dashed lines above and below the axis mark the bands "$2\,se_k$" (?) and "$-2\,se_k$" (?). A smooth curve starts near the upper band at $k=0$, decreases monotonically, crosses zero and dips below the lower band to a trough, then rises back up, oscillates with a small wiggle, and finally damps onto the zero line for large $k$. An upward arrow points at the curve at the lag where it re-enters the band from below; the arrow is labeled "$k_0$".]*

Figure 10.2: Correlograms for assessing convergence

**10.2.3 Monte Carlo error**

The Monte Carlo error, also called the numerical standard error (NSE), gives the variation that can be expected in the estimate if the computation were to be done again.

Batch means method

$$\underbrace{\theta^{(1)},...,\theta^{(\ell)}}_{\bar{\theta}_1=\ell^{-1}\sum_{k=1}^{\ell}\theta^{(k)}}\;,\;\underbrace{\theta^{(\ell+1)},...,\theta^{(2\ell)}}_{\bar{\theta}_2}\;,\;\underbrace{\theta^{(2\ell+1)},...,\theta^{(3\ell)}}_{\bar{\theta}_3}\;,\;...,\;\underbrace{\theta^{((n-1)\ell)},...,\theta^{(n\ell)}}_{\bar{\theta}_n=\ell^{-1}\sum_{k=(n-1)\ell}^{n\ell}\theta^{(k)}}$$

$\text{[sic: the last batch is printed as }\theta^{((n-1)\ell)},...,\theta^{(n\ell)}\text{ with the sum running from }k=(n-1)\ell\text{; these limits enclose }\ell+1\text{ terms, so for batches of equal length }\ell\text{ the lower limit should be }(n-1)\ell+1\text{]}$

> ✔ Verified: The printed last-batch summation limits $k=(n-1)\ell$ to $n\ell$ enclose $\ell+1$ terms, not $\ell$; the corrected lower limit $(n-1)\ell+1$ gives exactly $\ell$.

$n$ batches of equal length $\ell$.

$$NSE = \sqrt{\frac{\sum_{k=1}^{n}(\bar{\theta}_k - \bar{\theta})^2}{n(n-1)}}, \text{ where } \bar{\theta} = n^{-1}\sum_{k=1}^{n}\bar{\theta}_k$$

> ✔ Verified: NSE = sqrt( sum_k (thetabar_k - thetabar)^2 / (n(n-1)) ) equals s/sqrt(n), the standard error of the mean of the n batch means.

`Remark` : The $NSE$ gives an idea of the accuracy of the computations. Note that the $NSE$ is not the standard error of one of the parameters in the model!

**10.2.4 Geweke test (Geweke 1992)**

Gives a p-value for a test of stationarity. Checks whether the early part of the chain differs from the later part.

Let $\bar{X}_1, S_1^2$ denote the sample mean and variance of the early part for $n_1$ samples.

Let $\bar{X}_2, S_2^2$ denote the sample mean and variance of the later part for $n_2$ samples.

Compute

$$T = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}}$$

For large $n_1$ and $n_2$, $T \sim N(0,1)$

> ⚠ Check could not run (error): Geweke's T is standardized: with independent Xbar_1, Xbar_2 of common mean mu and variances sigma_1^2/n_1, sigma_2^2/n_2, the statistic has mean 0 and variance 1. — timed out after 90s

Compute p-value (want large p-value).

`Note(1)`: $S_1^2$ and $S_2^2$ need to be adjusted because the two samples are not independent. Geweke's test uses spectral densities and gamma regression to estimate the sample variances.

`Note(2)`: Geweke's test can be used to determine the burn-in period (the smallest early part of the chain that passes the test).

### PDF page 109 (booklet page 104)

**10.2.5 Effective sample size**

Have $M$ iterates (length of chain under study).
Compute the auto correlations at the $i^{th}$ lag, $r_i$, $i = 1, 2, ...$
Find $k$ such that

$$|r_k| < \frac{2}{\sqrt{M}}$$

Compute

$$\tau = \frac{1}{2} + \sum_{i=1}^{k} r_i$$

The effective sample size is given

$$eff_{ss} = \frac{M}{2\tau}$$

> ✔ Verified: The effective sample size $eff_{ss}=M/(2\tau)$ equals $M$ at $\tau=1/2$ and $0.5M$ at $\tau=1$.

`Note:` Want $\tau \approx \frac{1}{2}$ and $eff_{ss} \approx M$. Of course, $\tau$ can differ from $\frac{1}{2}$ and $eff_{ss}$ can be less than $M$, say $eff_{ss}$ as small as $0.5M$ may be reasonable.

## 10.3 Rao-Blackwellized estimators

Suppose that we have a random sample $\{(U^{(i)}, V^{(i)}, W^{(i)}), i = 1, ..., M\}$ from the joint density $[U, V, W]$. Then, $U^{(1)}, U^{(2)}, ..., U^{(M)}$ are a random sample from the marginal distribution of $U$. Thus, an estimator of $E(U)$ is

$$\widehat{E(U)} = M^{-1} \sum_{i=1}^{M} U^{(i)}$$

and similarly, an estimator of $E(U^2)$ is

$$\widehat{E(U^2)} = M^{-1} \sum_{i=1}^{M} U^{(i)2}$$

Also $Var(U)$ can be estimated by

$$\widehat{Var(U)} = \widehat{E(U^2)} - (\widehat{E(U)})^2 \approx S^2 = \frac{\sum_{i=1}^{M}(U^{(i)} - \widehat{E(U)})^2}{M-1}$$

> ✔ Verified: $\widehat{E(U^2)}-(\widehat{E(U)})^2$ equals $\frac{1}{M}\sum(U_i-\bar U)^2 = \frac{M-1}{M}S^2$, hence only approximately $S^2$.

In some situation, there may be better estimators of $E(U), Var(U)$ etc. An estimator with smaller mean square error is obtained by exploiting the form of the conditional distribution of $[U|V, W]$.
For

$$[U] = \int \int [U|V,W][V,W] dV\, dW,$$

$$\widehat{[U]} = M^{-1} \sum_{i=1}^{M} [U|V^{(i)}, W^{(i)}]$$

### PDF page 110 (booklet page 105)

Also,

$$E(U) = E_{V,W}\{E(U\mid V,W)\}$$

> ✔ Verified: The law of total expectation $E(U) = E_{V,W}\{E(U\mid V,W)\}$ holds for a discrete joint distribution.

and an estimation of $E(U)$ is $\widehat{E(U)}$, where

$$\widehat{E(U)} = M^{-1}\sum_{i=1}^{M} E(U\mid V^{(i)}, W^{(i)})$$

This process is called Rao-Blackwellization, and estimators like $\widehat{[U]}$ (?) and $\widehat{E(U)}$ are called Rao-Blackwellized estimators. It is true that $M^{-1}\sum_{i=1}^{M} E(U\mid V^{(i)}, W^{(i)})$ has smaller mean square error than $M^{-1}\sum_{i=1}^{M} U^{(i)}$, as an estimator of $E(U)$.

> ✔ Verified: Rao-Blackwellization does not increase variance: Var(E(U|V,W)) <= Var(U), with equality iff U is (a.s.) a function of (V,W); hence M^{-1} sum E(U|V,W) has no larger MSE than M^{-1} sum U, both being unbiased for E(U).

`Remark:` Use the Rao-Blackwellized estimators whenever it is possible. However, when the conditional does not have a "nice" form, use an "empirical" estimator (e.g., $\bar{U}$) or a nonparameteric [sic] density estimator (kernel).

## Illustration(Normal means model)

*(correction: a handwritten "$\ell$"/"l" is inserted after "mode", making it "model")*

We have a random sample $(\mu^{(h)}, \theta^{(h)}, \sigma^{2(h)}, \delta^{2(h)}),\, h = 1, ..., M$ from the joint posterior density. *(The booklet writes $\mu$, $y$, $\theta$ with under-tildes to indicate vectors.)*

Suppose we need inference for $\mu_i,\, i = 1, ..., \ell$

The conditional posterior density for $\mu_i$ is $f(\mu_i \mid \sigma^2, \delta^2, y)$ where

$$\mu_i \mid \sigma^2, \delta^2, y \;\overset{ind}{\sim}\; N\left\{\lambda_i \bar{y}_i + (1-\lambda_i)\hat{\theta},\; (1-\lambda_i)^2\nu^2 + (1-\lambda_i)\delta^2\right\}$$

$$\lambda_i = \frac{\delta^2}{\delta^2 + \frac{\sigma^2}{n_i}},\quad \nu^2 = \frac{\delta^2}{\sum_{i=1}^{\ell}\lambda_i},\quad \hat{\theta} = \frac{\sum_{i=1}^{\ell}\lambda_i \bar{y}_i}{\sum_{i=1}^{\ell}\lambda_i}$$

[Note that we have integrated out $\theta$.]

$$\widehat{f(\mu_i\mid y)} = M^{-1}\sum_{\ell=1}^{M} f(\mu_i \mid \sigma^{2(h)}, \delta^{2(h)}, y),$$

$\text{[sic: the summation index is printed as }\ell=1\text{ but should be }h=1\text{, matching the superscripts }(h)\text{]}$

$$\widehat{E(\mu_i\mid y)} = M^{-1}\sum_{\ell=1}^{M}\left[\lambda_i^{(h)}\bar{y}_i + (1-\lambda_i^{(h)})\hat{\theta}^{(h)}\right],$$

$\text{[sic: again the index is printed }\ell=1\text{ rather than }h=1\text{]}$

$$Var(\mu_i\mid y) = E\left\{(1-\lambda_i)^2\nu^2 + (1-\lambda_i)\delta^2 \,\Big|\, y\right\} + Var\left\{\lambda_i\bar{y}_i + (1-\lambda_i)\hat{\theta} \,\Big|\, y\right\},$$

> ✔ Verified: For mu_i | sigma^2, delta^2, y ~ N(m, v) with m = lam*ybar + (1-lam)*thetahat and v = (1-lam)^2*nu^2 + (1-lam)*delta^2, the marginal posterior variance equals E{v | y} + Var{m | y}.

and

$$\widehat{Var(\mu_i\mid y)} = M^{-1}\sum_{h=1}^{M}\left\{(1-\lambda_i^{(h)})^2\nu^{2(h)} + (1-\lambda_i^{(h)})\delta^{2(h)}\right\} + M^{-1}\sum_{h=1}^{M}\left(t_i^{(h)} - \bar{t}_i\right)^2,$$

$$\text{where } t_i^{(h)} = \lambda_i^{(h)}\bar{y}_i + (1-\lambda_i^{(h)})\hat{\theta}^{(h)}$$

> ✔ Verified: The printed Monte Carlo estimator is the sample analogue of c3: its second term is exactly the sample variance of t_i^{(h)} about tbar_i, and the whole estimator converges to Var(mu_i | y) as the draws' empirical distribution matches the posterior.

### PDF page 111 (booklet page 106)

**10.4 The Griddy Gibbs sampler**

Suppose some of the conditional posterior densities do not exist in simple forms (i.e., we can not draw samples easily from them). Then, in order to perform a Gibbs sampler we can proceed in at least two ways for these cpds:

<div align="center">

a. Rejection method     b. Grid method

</div>

Method $(a)$ is generally a bad method because the acceptance rate might be too low, and the Gibbs sampler can get stuck a long time.

If method $(b)$ is used, we have a griddy Gibbs sampler *[the phrase "griddy Gibbs sampler" is hand-underlined]*. The same comments apply for drawing from a grid.

**Illustrative example(Beta-Binomial model)**

$$y_{i1},...,y_{in_i}\mid p_i \overset{iid}{\sim} Bernoulli(p_i), i=1,...,\ell$$

$$p_1,...,p_\ell\mid \mu,\tau \overset{iid}{\sim} Beta(\mu\tau,(1-\mu)\tau)$$

$$p(\mu)=1,\; 1<\mu<1\;\text{[sic: should be } 0<\mu<1\text{]};\quad p(\tau)=\frac{1}{(1+\tau)^2},\;\tau>0.$$

> ✔ Verified: The prior $p(\tau)=1/(1+\tau)^2$ integrates to 1 over $\tau>0$.

The parameters are $(p,\mu,\tau)$ and the data are $y=\{y_{ij}, j=1,...,n_i; i=1,...,\ell\}$. Then, the joint posterior density is $\pi(p,\mu,\tau\mid y)$, where
*(The booklet writes $p$, $y$, $\mu$, $\tau$ with under-tildes to indicate vectors.)*

$$\pi(p,\mu,\tau\mid y)\propto\prod_{i=1}^{\ell}\left\{p_i^{y_i}(1-p_i)^{n_i-y_i}\frac{p_i^{\mu\tau-1}(1-p_i)^{(1-\mu)\tau-1}}{B(\mu\tau,(1-\mu)\tau)}\right\}\times\frac{1}{(1+\tau)^2}$$

$$0<p_i<1, i=1,...,\ell;\; 0<\mu<1;\; \tau>0$$

$$y_i=\sum_{j=1}^{n_i}y_{ij}=\#\text{ of ``successes''}, i=1,...,\ell$$

Conditional posterior densities

$$p_i\mid\mu,\tau,y \overset{ind}{\sim} Beta(y_i+\mu\tau,\; n_i-y_i+(1-\mu)\tau)$$

> ✔ Verified: The joint-posterior kernel in $p_i$ equals the $Beta(y_i+\mu\tau,\ n_i-y_i+(1-\mu)\tau)$ density times its Beta normalizing constant.

$$\text{Let } a=\prod_{i=1}^{\ell}p_i,\; b=\prod_{i=1}^{\ell}(1-p_i)$$

$$\pi(\mu\mid p,\tau,y)\propto\frac{a^{\mu\tau-1}b^{(1-\mu)\tau-1}}{\left(B(\mu\tau,(1-\mu)\tau)\right)^{\ell}},\; 0<\mu<1$$

$$\pi(\tau\mid p,\mu,y)\propto\frac{a^{\mu\tau-1}b^{(1-\mu)\tau-1}}{\left(B(\mu\tau,(1-\mu)\tau)\right)^{\ell}}\times\frac{1}{(1+\tau)^2},\;\tau>0$$

> ✔ Verified: $\prod_{i=1}^{\ell} p_i^{\mu\tau-1}(1-p_i)^{(1-\mu)\tau-1}/B(\mu\tau,(1-\mu)\tau) = a^{\mu\tau-1}b^{(1-\mu)\tau-1}/B(\mu\tau,(1-\mu)\tau)^{\ell}$.

### PDF page 112 (booklet page 107)

Observe that (2) and (3) do not have simple forms(i.e., we can not draw samples from them easily).

It is easy to use the grid method in (2) but (3) is more difficult because $\tau$ is unbounded.

How to draw a sample from the cpd of $\tau$?

$$\pi(\tau\mid p,\mu,y) \propto \frac{a^{\mu\tau-1}b^{(1-\mu)\tau-1}}{\left(B(\mu\tau,(1-\mu)\tau)\right)^{\ell}} \times \frac{1}{(1+\tau)^2},\ \tau>0$$

*(The booklet writes $p$ and $y$ with under-tildes to indicate vectors.)*

Make the transformation

$$\phi = \frac{\tau}{\tau+1}\ \text{ to give }\ \tau = \frac{\phi}{1-\phi},\ 0<\phi<1$$

> ✔ Verified: The transformation $\phi=\tau/(\tau+1)$ inverts to $\tau=\phi/(1-\phi)$ for $0<\phi<1$, mapping onto $\tau>0$.

Now

$$\frac{d\tau}{d\phi} = \frac{1}{(1-\phi)^2}$$

> ✔ Verified: $\dfrac{d\tau}{d\phi} = \dfrac{1}{(1-\phi)^2}$ where $\tau=\phi/(1-\phi)$.

So

$$\pi(\phi\mid p,\mu,y) \propto \frac{a^{\mu\tau-1}b^{(1-\mu)\tau-1}}{\left(B(\mu\tau,(1-\mu)\tau)\right)^{\ell}}\Big|_{\tau=\frac{\phi}{1-\phi}},\ 0<\phi<1$$

> ✔ Verified: Under $\tau=\phi/(1-\phi)$ the Jacobian exactly cancels $1/(1+\tau)^2$, so $\pi(\phi\mid\cdot)$ is the $\tau$-kernel with $\tau$ substituted and no leftover $\phi$ factor.

The grid method can now be performed in a manner similar to that for $\pi(\mu\mid p,\tau,y)$.

**Rao-Blackwellized estimators**

There are no Rao-Blackwellized estimators for $\mu$ and $\tau$, but these are essentially nuisance parameters.

A Rao-Blackwellized estimators [sic] for $f(p_i\mid y)$ is

$$\widehat{f(p_i\mid y)} = M^{-1}\sum_{h=1}^{M} f\left(p_i\mid \mu^{(h)},\tau^{(h)},y\right)$$

where

$$f(p_i\mid\mu,\tau,y) = \frac{p_i^{\,y_i+\mu\tau-1}(1-p_i)^{\,n_i-y_i+(1-\mu)\tau-1}}{B\left(y_i+\mu\tau,\ n_i-y_i+(1-\mu)\tau\right)},\ 0<p_i<1,\ i=1,...,\ell$$

$$\text{Let } \lambda_i = \frac{n_i}{n_i+\tau},\ \hat{p}_i = \frac{y_i}{n_i},\ i=1,...,\ell$$

> ⚠ Check FAILED: $f(p_i\mid\mu,\tau,y)$ is a normalized Beta$(y_i+\mu\tau,\ n_i-y_i+(1-\mu)\tau)$ density. — the stated result did not reproduce (see verification log)

Then, a Rao-Blackwellized estimator of $E(p_i\mid y)$ is

$$\widehat{E(p_i\mid y)} = M^{-1}\sum_{h=1}^{M}\left\{\lambda_i^{(h)}\hat{p}_i + (1-\lambda_i^{(h)})\mu^{(h)}\right\}$$

> ✔ Verified: The Beta mean $(y_i+\mu\tau)/(n_i+\tau)$ equals $\lambda_i\hat p_i+(1-\lambda_i)\mu$ with $\lambda_i=n_i/(n_i+\tau)$, $\hat p_i=y_i/n_i$.

and

$$\widehat{Var(p_i\mid y)} = M^{-1}\sum_{h=1}^{M}\frac{y_i+\mu^{(h)}\tau^{(h)}}{(n_i+\tau^{(h)})^2(n_i+\tau^{(h)}+1)} + \frac{1}{M-1}\sum_{h=1}^{M}\left(t_i^{(h)}-\bar{t}_i\right)^2,$$

$\text{[sic: the numerator of the first sum should be } (y_i+\mu^{(h)}\tau^{(h)})\left(n_i-y_i+(1-\mu^{(h)})\tau^{(h)}\right)\text{ — the second Beta parameter is dropped in the printed formula]}$

> ✔ Verified: The conditional Beta variance is $(y_i+\mu\tau)(n_i-y_i+(1-\mu)\tau)/[(n_i+\tau)^2(n_i+\tau+1)]$; the printed numerator $y_i+\mu\tau$ alone is not equal to it.

where

$$t_i^{(h)} = \lambda_i^{(h)}\hat{p}_i + (1-\lambda_i^{(h)})\mu^{(h)}\ \text{ and }\ \bar{t}_i = M^{-1}\sum_{h=1}^{M}t_i^{(h)}$$

### PDF page 113 (booklet page 108)

*[top margin note, handwritten: "Generalization" (?)]*

**10.5 Example**

**Example I. Nested error regression model (NER)**

NHANES III. Bone mineral density (BMD), white females,age 20+ for 35 counties. BMD roughly normally distributed, less normal by county. Linear relationship of BMD with age. See Figure 3 for data.

*[Figure: a histogram of `bmdo` (BMD) with a density scale on the vertical axis (ticks at 0, 1, 2) and horizontal-axis tick labels 0.27, 0.45, 0.63, 0.81, 0.99, 1.17, 1.35. The shape is unimodal and roughly symmetric, peaking just above density 2.5 near bmdo $\approx 0.85$, with a slightly longer left tail — consistent with the reported negative skewness.]*

*[Below the histogram, a SAS-style "Moments" output box:]*

| | | | |
|---|---:|---|---:|
| N | 2075.0000 | Sum Wgts | 2075.0000 |
| Mean | 0.8698 | Sum | 1804.8950 |
| Std Dev | 0.1579 | Variance | 0.0249 |
| Skewness | -0.1939 | Kurtosis | 0.0593 |
| USS | 1621.6765 | CSS | 51.7266 |
| CV | 18.1559 | Std Mean | 0.0035 |

> ✔ Verified: Mean = Sum/N to 4 decimals (1804.8950 / 2075 rounds to 0.8698)

> ✔ Verified: Variance = CSS/(N-1) = 0.0249 and Std Dev = sqrt(Variance) = 0.1579

> ✔ Verified: USS - Sum^2/N equals CSS (uncorrected minus correction = corrected sum of squares)

> ✔ Verified: CV = 100*sd/mean = 18.1559 and Std Mean = sd/sqrt(N) = 0.0035

Figure 10.3: BMD data used in NER model

*[margin notes, handwritten, to the left of and above the displayed equations: "$y_{ij}\sim N(\beta_0+\beta_1 x_{ij}+\nu_i,\ \sigma^2)$"; "$\nu_i\sim N(0,\delta^2)$"; "Two levels (?)"]*

$$y_{ij} = \beta_0 + \beta_1 x_{ij} + \nu_i + e_{ij},\, i = 1, ..., \ell = 35, j = 1, ..., n_i.$$

$$e_{ij} \mid \sigma^2 \; \underset{\sim}{iid} \; Normal(0, \sigma^2)$$

*(The booklet writes the "iid" of each distributional statement with an under-tilde.)*

$$\nu_i \mid \delta^2 \; \underset{\sim}{iid} \; Normal(0, \delta^2)$$

$$p(\beta_0, \beta_1) = 1; \sigma^{-2}, \delta^{-2} \; \underset{\sim}{iid} \; Gamma\!\left(\frac{a}{2}, \frac{b}{2}\right); a = b = 0.002$$

### PDF page 114 (booklet page 109)

Inference is required for the parameters $\beta_0,\beta_1,\nu_i,\sigma^2,\delta^2$. *[a short vertical pen tick (?) sits under $\beta_1$; possibly a stray mark]*
The joint posterior density is

$$\pi(\beta,\nu,\sigma^2,\delta^2\mid y)\propto \prod_{i=1}^{\ell}\prod_{j=1}^{n_i}\left\{\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2\sigma^2}\left(y_{ij}-[\beta_0+\beta_1 x_{ij}+\nu_i]\right)^2}\right\}$$

$$\times\;\prod_{i=1}^{\ell}\left\{\frac{1}{\sqrt{2\pi\delta^2}}e^{-\frac{\nu_i^2}{2\delta^2}}\right\}\;\times\;\left(\frac{1}{\delta^2}\right)^{\frac{a}{2}+1}e^{-\frac{b}{2\delta^2}}\;\times\;\left(\frac{1}{\sigma^2}\right)^{\frac{a}{2}+1}e^{-\frac{b}{2\sigma^2}}$$

*(The booklet writes $\beta$, $\nu$, $y$, $d_{ij}$ with under-tildes to indicate vectors.)*

> ✔ Verified: The factors $(1/\delta^2)^{a/2+1}e^{-b/(2\delta^2)}$ and $(1/\sigma^2)^{a/2+1}e^{-b/(2\sigma^2)}$ are the kernels of $IG(a/2, b/2)$.

**Posterior conditional densities**

Let $d_{ij}=(1,x_{ij})',\; i=1,...,\ell,\; j=1,...,n_i,\; \beta=(\beta_0,\beta_1)'$

$$\beta\mid\nu,\sigma^2,\delta^2,y \;\sim\; Normal\left\{\Big(\sum_i\sum_j d_{ij}d_{ij}'\Big)^{-1}\sum_i\sum_j d_{ij}(y_{ij}-\nu_i),\;\sigma^2\Big(\sum_i\sum_j d_{ij}d_{ij}'\Big)^{-1}\right\}$$

> ✔ Verified: The $\beta$ full conditional is Normal with mean $(\sum\sum dd')^{-1}\sum\sum d(y-\nu)$ and covariance $\sigma^2(\sum\sum dd')^{-1}$.

$$\nu_i\mid\beta,\sigma^2,\delta^2,y \;\; ind\;\; Normal\left\{\frac{\sum_{j=1}^{n_i}(y_{ij}-\beta_0-\beta_1 x_{ij})/\sigma^2}{1/\delta^2+n_i/\sigma^2},\;\frac{1}{\frac{1}{\delta^2}+\frac{n_i}{\sigma^2}}\right\}$$

> ✔ Verified: The $\nu_i$ full conditional is Normal with precision $1/\delta^2 + n_i/\sigma^2$ and mean $\frac{\sum_j (y_{ij}-\beta_0-\beta_1 x_{ij})/\sigma^2}{1/\delta^2 + n_i/\sigma^2}$.

$$\sigma^2\mid\beta,\nu,\delta^2,y \;\sim\; IGamma\left\{\frac{a+\sum_{i=1}^{\ell}n_i}{2},\;\frac{b+\sum_i\sum_j\left[y_{ij}-(\beta_0+\beta_1x_{ij}+\nu_i)\right]^2}{2}\right\}$$

> ✔ Verified: The $\sigma^2$ full conditional is $IGamma\!\left(\frac{a+\sum_i n_i}{2},\frac{b+SSE}{2}\right)$.

*[Handwritten scratch in the left margin, alongside the line below, mostly illegible: "$\lambda_i$"(?), a large brace, a tall $\int$-like stroke(?), a struck-through symbol, "$(\ell-\lambda_i)$"(?) inside a large closing parenthesis, and a large "$\delta^2$" at the right; a long horizontal brace with a hooked tail is drawn underneath the whole cluster. These appear to be lecture scratch notes accompanying the $\delta^2$ conditional.]*

$$\delta^2\mid\beta,\nu,\sigma^2,y \;\sim\; IGamma\left\{\frac{a+\ell}{2},\;\frac{b+\sum_{i=1}^{\ell}\nu_i^2}{2}\right\}$$

> ✔ Verified: The $\delta^2$ full conditional is $IGamma\!\left(\frac{a+\ell}{2},\frac{b+\sum_i \nu_i^2}{2}\right)$.

All cpds are simple, Gibbs sampler applies immediately.

**How to start the Gibbs sampler?**

$$y_{ij}=\beta_0+\beta_1x_{ij}+\nu_i+e_{ij}$$

$$e_{ij}\;\overset{iid}{\sim}\;N(0,\sigma^2),\;\nu_i\;\overset{iid}{\sim}\;N(0,\delta^2),\;d_{ij}=(1,x_{ij})',\;i=1,...,\ell;\;j=1,...,n_i.$$

$$\hat{\beta}=\Big[\sum_i\sum_j d_{ij}d_{ij}'\Big]^{-1}\Big[\sum_i\sum_j d_{ij}\,y_{ij}\Big]$$

> ✔ Verified: $\hat{\beta}=[\sum\sum d_{ij}d_{ij}']^{-1}[\sum\sum d_{ij} y_{ij}]$ minimizes $\sum\sum (y_{ij}-d_{ij}'\beta)^2$.

Then

$$y_{ij}-\hat{\beta}_0-\hat{\beta}_1x_{ij}\approx\nu_i+e_{ij}$$

$$\hat{\nu}_i=n_i^{-1}\sum_{j=1}^{n_i}\left\{y_{ij}-\hat{\beta}_0-\hat{\beta}_1x_{ij}\right\}$$

$$\hat{e}_{ij}=y_{ij}-\hat{\beta}_0-\hat{\beta}_1x_{ij}-\hat{\nu}_i$$

Start at

$$\nu_i=\hat{\nu}_i,\; i=1,...,\ell$$

### PDF page 115 (booklet page 110)

$$\delta^2 = (\ell - 1)^{-1} \sum_{i=1}^{\ell} (\hat{\nu}_i - \bar{\nu})^2, \; \bar{\nu} = \ell^{-1} \sum_{i=1}^{\ell} \hat{\nu}_i$$

> ✔ Verified: The stated $\delta^2 = (\ell-1)^{-1}\sum_{i=1}^{\ell}(\hat\nu_i-\bar\nu)^2$ with $\bar\nu=\ell^{-1}\sum\hat\nu_i$ is unbiased for the variance of the $\hat\nu_i$ (the $(\ell-1)^{-1}$ divisor, not $\ell^{-1}$, is the correct one).

$$\sigma^2 = \sum_i \sum_j \frac{(\hat{e}_{ij} - \bar{\hat{e}})^2}{\sum_{i=1}^{\ell} n_i - 1}$$

**How to "burn in" the Gibbs sampler?**

See Figure 4.

*[Figure 10.4: three stacked trace plots, one per panel, each plotting `del` (vertical axis, ticks at 0.001, 0.002, 0.003, 0.004) against `it` (horizontal axis, ticks at 200, 400, 600, 800, 1000). Top panel: the iterates are concentrated in a tight band below about 0.0015, hugging the bottom of the frame. Middle panel: the cloud is wider, centered near 0.0015–0.002 and scattering up toward 0.004. Bottom panel: similar to the middle panel but denser and reaching the top of the frame, centered near 0.002. Each panel is drawn inside an outer box with a small filled black square at its lower-left corner.]*

*[hand labels: a "1" (?) beside the top panel, a "2" beside the middle panel, and a "3" beside the bottom panel, written in dark pen in the space to the right of each plot, keying the three panels to the numbered list below]*

Figure 10.4: Trace plots and "burn in" used in NER model

1: Drew 1,100, "burn in" 100.
2. Drew 1,500, "burn in" 500.
3. Drew 2,000, "burn in" 1,000.

> ✔ Verified: Each of the three Gibbs runs listed under Figure 10.4 leaves exactly 1,000 retained iterates after burn-in, matching the figure's common horizontal axis (`it` running to 1000).

**Thinning the Gibbs sampler?**

The most difficult parameter to converge is $\delta^2$. We look at the auto correlation coefficient(sample) of the iterates.

### PDF page 116 (booklet page 111)

| Runs | 2,000 | 3,000 | 5,000 | 6,000 |
|---|---|---|---|---|
| Burn in | 1,000 | 1,000 | 1,000 | 1,000 |
| Lag | skip 1 | 2 | 4 | 5 |
| 1 | .560 | .298 | .133 | .070 |
| 2 | .323 | .114 | -.011 | -.044 |
| 3 | .184 | .018 | -.049 | -.035 |
| 4 | .086 | .001 | -.058 | .032 |

Standard error of the sample ACF $\approx$ .032.

> ✔ Verified: The standard error of the sample ACF from 1000 retained iterates, 1/sqrt(1000), rounds to .032.

For inference, ran 6,000, "burn in" 1,000 and took every $5^{th}$ there after [sic].

1000 interates [sic]: "random" sample.

> ✔ Verified: 6,000 runs with burn-in 1,000, keeping every 5th thereafter, yields exactly 1000 iterates.

Posterior means(PM), posterior standard deviations(PSD), numerical standard error(NSE) and 95% credible intervals(CI) for selected parameters.

*[margin note, left, in a hand-drawn oval beside the four $\nu+\beta_0$ rows: "Prediction"]*

*[margin note, right of the table, four cursive lines: "How to [illegible] run(?) the Gibbs Sampler"]*

| Parameter | PM | PSD | NSE | CI |
|---|---|---|---|---|
| $\nu_1 + \beta_0$ | 1.080 | 0.014 | 0.002 | (1.05,1.11) |
| $\nu_{10} + \beta_0$ | 1.080 | 0.018 | 0.003 | (1.04,1.12) |
| $\nu_{25} + \beta_0$ | 1.107 | 0.019 | 0.004 | (1.07,1.15) |
| $\nu_{35} + \beta_0$ | 1.080 | 0.014 | 0.003 | (1.05,1.11) |
| $\beta_1$ | -0.005 | 0.0002 | 0.00004 | (-0.0048,-0.0042) |
| $\sigma^2$ | 0.017 | 0.001 | 0.0001 | (0.016,0.018) |
| $\delta^2$ | 0.0005 | 0.0002 | 0.00004 | (0.0002,0.0011) |

## Example III. Nonresponse binary data

Do you belong to Massachusetts?

103 students, 80 responded, 60 said yes.

**Pattern mixture Model**

See Figure 5.

Each student responded independently.

$$p(y,r,z\mid\pi,p,q) = \frac{n!(\pi p)^{y}(\pi(1-p))^{r-y}((1-\pi)q)^{z}((1-\pi)(1-q))^{n-r-z}}{y!(r-y)!z!(n-r-z)!}$$

> ✔ Verified: The four pattern-mixture cell probabilities sum to 1.

Ignorable nonresponse model: $p = q$. (no problem)

Nonignorable nonresponse model: $p \neq q$. (difficult)

Take $q = ap$, so that $0 < p < \dfrac{1}{a}, a \geq 1$. Take $\pi, p \;\underset{\sim}{ind}\; Uniform(0,1)$

> ✔ Verified: For a > 0, the constraint p < 1/a is exactly q = ap < 1.

Then

$$\pi(\pi,p,z\mid r,y,a) \propto \frac{(\pi p)^{y}(\pi(1-p))^{r-y}((1-\pi)ap)^{z}((1-\pi)(1-ap))^{n-r-z}}{z!(n-r-z)!}$$

> ✔ Verified: Substituting q = ap into p(y,r,z|pi,p,q) reproduces the displayed kernel times n!/(y!(r-y)!).

### PDF page 117 (booklet page 112)

*[Figure 10.5 is entirely handwritten. Reading of the handwritten content:]*

*[Handwritten heading:]* **EXAMPLE III.** Nonresponse binary data.
 Do you belong to Massachusetts?
 103 students, 80 responded, 60 said "Yes."

*[Handwritten, underlined:]* <u>Pattern mixture model</u>

*[Figure: two probability trees drawn side by side. **Left tree** — circled root "$1$"(?); first split into branches labelled $\pi$ and $1-\pi$; each of those splits again, the $\pi$ branch into $p$ and $1-p$, the $1-\pi$ branch into $q$ and $1-q$; the four leaves are labelled $\pi p$, $\pi(1-p)$, $(1-\pi)q$, $(1-\pi)(1-q)$. **Right tree** — circled root "$n$"; the same two-level structure, the first split labelled $\pi$ / $r$ and $1-\pi$ / $n-r$, the second splits labelled $p$, $1-p$ and $q$, $1-q$; the four leaves are the cell counts $y$, $r-y$, $z$, $n-r-z$.]*

*[Handwritten:]* Each student responded independently.

$$p(y,z,r\mid \pi,p,q) \;=\; \frac{n!\,(\pi p)^{y}\big(\pi(1-p)\big)^{r-y}\big((1-\pi)q\big)^{z}\big((1-\pi)(1-q)\big)^{n-r-z}}{y!\,(r-y)!\,z!\,(n-r-z)!}$$

> ✔ Verified: The four pattern-mixture cell probabilities sum to 1 and the four cell counts sum to n, so the displayed multinomial pmf is proper.

*[Handwritten:]* Ignorable nonresponse model: $p=q$ (no problem)

*[Handwritten, marked with a hand asterisk:]* \* Nonignorable nonresponse model: $p\neq q$ (difficult)

*[Handwritten:]* Take $q=ap$, so that $0<p<\frac{1}{a}$, $a>1$

> ✔ Verified: With q = a*p and a > 1, the constraint 0 < q < 1 is equivalent to 0 < p < 1/a.

**Figure 10.5: Pattern mixture model for nonignorable nonresponse**

---

Pessimistic-optimistic range of $p$:

$$\frac{y}{n} < p < 1 - \frac{r-y}{n}. \;\text{Have already } 0 < p < \frac{1}{a}$$

So

$$\frac{y}{n} < p < \min\!\left(\frac{1}{a},\, 1 - \frac{r-y}{n}\right)$$

$$\text{Take } \frac{1}{a} < 1 - \frac{r-y}{n},\ \text{ so } a > \frac{n}{n-r+y}$$

$$\text{That is, } \frac{y}{n} < p < \frac{1}{a},\ \text{ where } a > \frac{n}{n-r+y}$$

> ✔ Verified: For n > 0, a > 0, n-r+y > 0: 1/a < 1 - (r-y)/n  <=>  a > n/(n-r+y).

So

$$\pi(p\mid r,y,a) = \frac{p^{y}(1-p)^{r-y}}{\int_{\frac{y}{n}}^{\frac{1}{a}} p^{y}(1-p)^{r-v}dp},\quad \frac{y}{n} < p < \frac{1}{a},\ a > \frac{n}{n-r+y}$$

*[sic: the exponent in the normalizing integral is printed $r-v$; it should be $r-y$.]*

–truncated beta random variable.

For our data, $n = 103, r = 80, y = 60$,

$$\pi(p\mid r=80,y=60,a) = \frac{p^{60}(1-p)^{20}}{\int_{\frac{60}{103}}^{\frac{1}{a}} p^{60}(1-p)^{20}dp},\quad \frac{60}{103} < p < \frac{1}{a},\ a > \frac{103}{83}\;\text{–truncated beta(61,21)}$$

> ✔ Verified: For n=103, r=80, y=60 the exponents are 60 and 20, the bound is a > 103/83, the kernel is beta(61,21), and 60/103 < 83/103.

### PDF page 118 (booklet page 113)

Sensitivity analysis: vary $a$ to see how the distribution changes.

**Selection model**

See Figure 6.

*[Figure 10.6 is a photographic reproduction of the instructor's handwritten page. At the left is a probability tree: the root splits into a left branch labelled $p$ and a right branch labelled $1-p$; the left node splits into $\pi_1$ and $1-\pi_1$, the right node into $\pi_0$ and $1-\pi_0$. The four leaves are labelled with their probabilities and counts: $\pi_1 p$ with count $y$; $(1-\pi_1)p$ with count $z$; $\pi_0(1-p)$ with count $r-y$; $(1-\pi_0)(1-p)$ with count $n-r-z$. Beneath the leaves: "$y$: observed", "$z$(?): not observed". The heading "Selection model" is hand-underlined at top left.]*

*[Handwritten work filling the right half and bottom of Figure 10.6, legible and duplicating the typeset material below: $p(y,z,r\mid\pi_0,\pi_1,p)=\dfrac{n!(\pi_1p)^y\left((1-\pi_1)p\right)^z\left(\pi_0(1-p)\right)^{r-y}\left((1-\pi_0)(1-p)\right)^{n-r-z}}{y!\,z!\,(r-y)!\,(n-r-z)!}$ … "$\pi_0,\pi_1$ cannot be estimated." … "Take $\pi_0,\pi_1$ ind Beta$(\alpha_0,\beta_0)$, $\alpha_0,\beta_0$ are to be specified." … "Independently, $p\sim$ Uniform$(0,1)$" … "How to specify $\alpha_0,\beta_0$?" … "Take $\pi_1=\pi_0$ (ignorable nonresponse model)" … "$\pi\mid y,z,r\sim$ Beta$(r+1,n-r+1)$" … "$p$ take $\alpha_0=r+1$ with $\beta_0=n-r+1$ [data dependent prior]" … "Then, a posteriori, $\pi(p,\pi_1,\pi_2,z\mid y,r)\propto\dfrac{p^{y+z}(1-p)^{n-(y+z)}\;\pi_0^{r-y+\alpha_0-1}(1-\pi_0)^{n-r-z+\beta_0-1}\;\pi_1^{y+\alpha_0-1}(1-\pi_1)^{z+\beta_0-1}}{z!\,(n-r-z)!}$". In the handwritten posterior the conditioning list reads $\pi_1,\pi_2$ where the typeset version below reads $\pi_0,\pi_1$.]*

**Figure 10.6: Selection model for nonignorable nonresponse**

$$p(y,z,r|\pi_0,\pi_1,p) = \frac{n!(\pi_1 p)^y((1-\pi_1)p)^z(\pi_0(1-p))^{r-y}((1-\pi_0)(1-p))^{n-r-z}}{y!z!(r-y)!(n-r-z)!}$$

> ✔ Verified: The four selection-model cell probabilities sum to 1 and the four cell counts sum to $n$.

$\pi_0,\pi_1$ cannot be estimated.

Take $\pi_0,\pi_1$ $\underset{\sim}{ind}$ $Beta(\alpha_0,\beta_0)$, $\alpha_0,\beta_0$ are to be specified. *(The booklet writes "ind" with an under-tilde, meaning independently distributed.)*

Independently, $p \sim Uniform(0,1)$

How to specify $\alpha_0,\beta_0$? Take $\pi_1 = \pi_0$ (ignorable nonresponse model)

$$\pi|y,z,r \;\sim\; Beta(r+1, n-r+1)$$

> ✔ Verified: Uniform(0,1) prior with Binomial(n, pi) likelihood for r gives posterior Beta(r+1, n-r+1).

So that $\alpha_0 = r+1, \beta_0 = n-r+1$ (data dependent prior).
Then, a posterior,

$$\pi(p,\pi_0,\pi_1,z|y,r) \propto \frac{p^{y+z}(1-p)^{n-(y+z)}\pi_0^{r-y+\alpha_0-1}(1-\pi_0)^{n-r-z+\beta_0-1}\pi_1^{y+\alpha_0-1}(1-\pi_1)^{z+\beta_0-1}}{z!(n-r-z)!}$$

> ✔ Verified: Likelihood x Beta(a0,b0) priors on pi0,pi1 x Uniform(0,1) on p equals the printed posterior kernel up to a factor free of (p, pi0, pi1, z).

### PDF page 119 (booklet page 114)

Integrating over $\pi_0, \pi_1, z$, we get

$$\pi(p\mid y,r) \propto A(p,n,r,y)\,p^{y}(1-p)^{r-y}$$

Where $A(p,n,r,y) = \displaystyle\sum_{z=0}^{n-r}\left\{\frac{B(y+\alpha_0, z+\beta_0)\,B(r-y, n-r-z-\beta_0)}{z!\,(n-r-z)!}\right\} p^{z}(1-p)^{n-r-z}$

$A(p,n,r,y)$ is an adjustment for nonignorability. $\pi(p\mid y,r) \propto p^{y}(1-p)^{n-y}, 0<p<1$ is the posterior density of $p$ under the ignorable nonresponse model.

In our example, $n = 103, r = 80, y = 60$.

> ⚠ Check FAILED: With n=103, y=60, the ignorable-model posterior kernel p^y (1-p)^(n-y) on (0,1) is the Beta(61,44) kernel: it integrates to the finite value B(61,44) = Gamma(61)Gamma(44)/Gamma(105), so dividing by it yields the Beta(61,44) density. — the stated result did not reproduce (see verification log)

`Comment(1)`:&nbsp;&nbsp;&nbsp;&nbsp;The adjustment $A(p,n,r,y)$ depends on $p,n,r,y$. Dependence on $p$ gives a weighted distribution.

`Comment(2)`:&nbsp;&nbsp;&nbsp;&nbsp;A sensitivity analysis is still needed. Check how inference about $p$ changes with $\alpha_0, \beta_0$, look at small perturbations.

## 10.6&nbsp;&nbsp;&nbsp;&nbsp;Bayesian Cross Validation

How can we answer the question, "Is a given model adequate?"

One way to answer this question is to do a Bayesian cross validation.

Let $y$ denote the $n \times 1$ data vector, and $y_{(r)}$ denote the $(n-1) \times 1$ data vector with the $r^{th}$ observation, $y_r$, deleted. *(The booklet writes $y$ and $y_{(r)}$ with under-tildes to indicate vectors.)*

Suppose we use $y_{(r)}$ but not $y_r$ when we fit the model. If the model fits well, it should predict $y_r$ very well.

The predictor of $y_r$ is $E(y_r\mid y_{(r)})$ and its variation is $Var(y_r\mid y_{(r)})$.

Then the standardized deleted residuals are

$$dres_r = \frac{y_r - E(y_r\mid y_{(r)})}{\sqrt{Var(y_r\mid y_{(r)})}}$$

Many large $|dres_r|$ cast doubt upon the model and the signs of $dres_r$'s allow patterns of under fitting or over fitting to be revealed.

`Remark(1)`:&nbsp;&nbsp;&nbsp;&nbsp;We can use $dres_r$ in much the same way as we do in non-Bayesian statistics.

`Remark(2)`:&nbsp;&nbsp;&nbsp;&nbsp;If $f(y_r\mid y_{(r)})$ are approximately normal distributed, we can draw a normal probability plot of the $dres_r$.

`Remark(3)`:&nbsp;&nbsp;&nbsp;&nbsp;I have used $dres_r$ for mortality data analysis extensively at the NCHS.

**Computation**

The formula for $dres_r$ suggests that we have to rerun the Gibbs sampler each time we delete an observation! This could, indeed, be a cumbersome computation problem.

Can we get away with just one run of the Gibbs sampler? Yes!

### PDF page 120 (booklet page 115)

Consider a function $h(.)$ of $y_r$. Then, we need $E(h(y_r)|y_{(r)})$. Now,

$$
\begin{aligned}
E(h(y_r)\mid y_{(r)}) &= \int \ldots \int E(h(y_r)\mid y_{(r)},\theta)\,\pi(\theta\mid y_{(r)})\,d\theta \\[2ex]
&= \int \ldots \int E(h(y_r)\mid y_{(r)},\theta)\,\frac{\pi(\theta\mid y_{(r)})}{\pi(\theta\mid y)}\,\pi(\theta\mid y)\,d\theta \\[3ex]
&= \frac{\displaystyle \int \ldots \int E(h(y_r)\mid y_{(r)},\theta)\,\frac{\pi(\theta\mid y_{(r)})}{\pi(\theta\mid y)}\,\pi(\theta\mid y)\,d\theta}{\displaystyle \int \ldots \int \frac{\pi(\theta\mid y_{(r)})}{\pi(\theta\mid y)}\,\pi(\theta\mid y)\,d\theta}
\end{aligned}
$$

> ✔ Verified: The importance-sampling denominator $\int \frac{\pi(\theta\mid y_{(r)})}{\pi(\theta\mid y)}\pi(\theta\mid y)\,d\theta$ equals 1, so the ratio form on line 3 equals the plain expectation on line 1.

Then

$$
E(h(y_r)\mid y_{(r)}) \approx \frac{\displaystyle M^{-1}\sum_{k=1}^{M} E(h(y_r)\mid y_{(r)},\theta^{(k)})\,\frac{\pi(\theta^{(k)}\mid y_{(r)})}{\pi(\theta^{(k)}\mid y)}}{\displaystyle M^{-1}\sum_{k=1}^{M} \frac{\pi(\theta^{(k)}\mid y_{(r)})}{\pi(\theta^{(k)}\mid y)}}
$$

$$
= \sum_{k=1}^{M} w_r^{(k)}\, E\left\{ h(y_r)\mid y_{(r)},\theta^{(k)} \right\}
$$

where

$$
w_r^{(k)} = \frac{\dfrac{\pi(\theta^{(k)}\mid y_{(r)})}{\pi(\theta^{(k)}\mid y)}}{\displaystyle \sum_{k=1}^{M} \frac{\pi(\theta^{(k)}\mid y_{(r)})}{\pi(\theta^{(k)}\mid y)}},\, r = 1,...,n.k = 1,...,M.
$$

*(sic: the booklet prints "$r = 1,\ldots,n.k = 1,\ldots,M.$" — the separator between the two index ranges is a period rather than a comma or semicolon. Also, the summation index $k$ in the denominator of $w_r^{(k)}$ clashes with the free index $k$ in the numerator.)*

> ✔ Verified: The self-normalized weights $w_r^{(k)}$ sum to 1, and $\dfrac{M^{-1}\sum_k g_k u_k}{M^{-1}\sum_k u_k} = \sum_k w_r^{(k)} g_k$ with $u_k = \pi(\theta^{(k)}\mid y_{(r)})/\pi(\theta^{(k)}\mid y)$.

With $\theta^{(1)},...,\theta^{(M)}$ a random sample from $\pi(\theta\mid y)$, the posterior density with all the data.

Finally, by Bayes' theorem

$$
\frac{\pi(\theta\mid y_{(r)})}{\pi(\theta\mid y)} = \frac{\dfrac{f(y_{(r)}\mid \theta)}{f(y\mid \theta)}}{\dfrac{f(y_{(r)})}{f(y)}}
$$

> ✔ Verified: Bayes' theorem gives $\dfrac{\pi(\theta\mid y_{(r)})}{\pi(\theta\mid y)} = \dfrac{f(y_{(r)}\mid\theta)/f(y\mid\theta)}{f(y_{(r)})/f(y)}$.

### PDF page 121 (booklet page 116)

$$w_r^{(k)} = \frac{f(y_{(r)}\mid\theta^{(k)})[f(y\mid\theta^{(k)})]^{-1}}{\sum_{k=1}^{M} f(y_{(r)}\mid\theta^{(k)})[f(y\mid\theta^{(k)})]^{-1}}$$

> ✔ Verified: The self-normalized importance weights $w_r^{(k)}$ sum to 1 over $k$.

Thus,

$$E(h(y_r)\mid y_{(r)}) = \sum_{k=1}^{M} w_r^{(k)} E\left\{h(y_r)\mid y_{(r)},\theta^{(k)}\right\},\, r = 1,...,n.$$

Remark:  Typically, $y_1,...,y_n\mid\theta$ are independent. Then

$$w_r^{(k)} = \frac{[f(y_r\mid\theta^{(k)})]^{-1}}{\sum_{k=1}^{M}[f(y_r\mid\theta^{(k)})]^{-1}},\, k = 1,...,M,\, r = 1,...,n.$$

> ✔ Verified: Under conditional independence, $f(y_{(r)}\mid\theta)\,[f(y\mid\theta)]^{-1} = [f(y_r\mid\theta)]^{-1}$, so the weight reduces to the Remark's form.

## Illustration(Normal means model)

$$y_{ij},...,y_{in_i}\mid\mu_i,\sigma^2 \;\overset{iid}{\sim}\; N(\mu_i,\sigma^2)$$

*[sic: the first index should be $y_{i1}$, not $y_{ij}$ — cf. the display "$y_{i1},...,y_{in_i}\mid\Omega$" three lines below.]*

$$\mu_1,...,\mu_\ell\mid\theta,\delta^2 \;\overset{iid}{\sim}\; N(\theta,\delta^2)$$

$$p(\theta) = 1,\, \sigma^{-2}\sim\Gamma\!\left(\frac{a}{2},\frac{b}{2}\right),\, \delta^{-2}\sim\Gamma\!\left(\frac{c}{2},\frac{d}{2}\right)$$

$$\Omega(\mu,\theta,\sigma^2,\delta^2)$$

$$y_{i1},...,y_{in_i}\mid\Omega \text{ are independent },\, i = 1,...,\ell$$

Thus,

$$w_{ij}^{(h)} = \frac{\dfrac{1}{f(y_{ij}\mid\Omega^{(h)})}}{\sum_{h=1}^{M}\dfrac{1}{f(y_{ij}\mid\Omega^{(h)})}} = \frac{\dfrac{1}{\dfrac{1}{\sqrt{2\pi\sigma^{2(h)}}}e^{-\frac{1}{2\sigma^{2(h)}}(y_{ij}-\mu_i^{(h)})^2}}}{\sum_{h=1}^{M}\dfrac{1}{\dfrac{1}{\sqrt{2\pi\sigma^{2(h)}}}e^{-\frac{1}{2\sigma^{2(h)}}(y_{ij}-\mu_i^{(h)})^2}}}$$

> ✔ Verified: With $f(y_{ij}\mid\Omega^{(h)})$ the $N(\mu_i^{(h)},\sigma^{2(h)})$ density, the weights equal the displayed explicit expression and sum to 1.

$$h = 1,...,M.\, j = 1,...,n_i.\, i = 1,...,\ell$$

$$E(y_{ij}\mid y_{(ij)}) \approx \sum_{h=1}^{M} w_{ij}^{(h)}\mu_i^{(h)}$$

> ✔ Verified: $E(y_{ij}\mid\Omega^{(h)}) = \mu_i^{(h)}$ for the normal means model.

$$E(y_{ij}^2\mid y_{(ij)}) \approx \sum_{h=1}^{M} w_{ij}^{(h)}[\sigma^{2(h)} + \mu_i^{(h)2}]$$

> ✔ Verified: $E(y_{ij}^2\mid\Omega^{(h)}) = \sigma^{2(h)} + \mu_i^{(h)2}$.

# Chapter 15 — Difficulties with MCMC Algorithms
*(PDF pages 165–178; booklet pages 157–170)*


### PDF page 165 (booklet page 157)

# Chapter 15 — Difficulties with MCMC Algorithms

Weak identifiability, Poor mixing
Numerical techniques
Examples (e.g., GG, SEP, NM)

**15.1 Introduction**

In a model, there may be weakly identified parameters or parameters which are not even identifiable. In such a case when MCMC sampling (e.g., Gibbs, Metropolis-Hastings) is performed, there will be long-range dependence (poor mixing) in the iterates. The ad hoc solution is to use a very long or several short runs with significant 'thinning' to obtain a 'random' sample from the joint posterior density.

Some examples with nonidentifiable parameters are

a. $f(\beta, \alpha, \gamma \mid data) = h(\alpha/\gamma, \beta \mid data)$

So, $\frac{\alpha}{\gamma}$ can not be estimated. If we use a 'weak' prior on $\alpha$ and $\gamma$, and we try to obtain samples from the joint posterior density, there will be difficulties (e.g., long-range dependence, poor mixing.)

b. $f(\beta, \alpha, \gamma \mid data) = g(\alpha + \gamma, \beta \mid data)$

The same problem occurs again.

In many problems it is difficult to show that a parameter is identifiable because two or more parameters may be involved in a complicated manner. But one may experience difficulties in MCMC sampling.

The problem generally occurs in the more practical hierarchical Bayesian models in a

### PDF page 166 (booklet page 158)

slightly different way. For example,

$$Y_i \mid \mu_i, \sigma^2 \overset{ind}{\sim} N(\mu_i, \sigma^2), \; i = 1, \cdots, l$$

$$\mu_i \mid \theta, \delta^2 \overset{iid}{\sim} N(\theta, \delta^2)$$

$$\pi(\theta, \sigma^2, \delta^2) \; \textit{is a prior.}$$

Here,

$$\mu_i = \theta + \delta Z_i, \; Z_i \overset{iid}{\sim} N(0,1)$$

> ✔ Verified: $\mu = \theta + \delta Z$ with $Z \sim N(0,1)$ has density equal to the $N(\theta, \delta^2)$ density.

Thus, the $\mu_i$ are correlated with $(\theta, \delta^2)$ causing difficulties in the Gibbs sampler (Holmes and Held, BA 2006). Sometimes some thinning will work and it will work in this specific problem. In general, though, some reparameterization (Nandram and Chen, JSCS 1996) will help. In most cases one would need to integrate out some parameters. See Holmes and Held (BA 2006). This example will be discussed in detail later.

*[a large hand-drawn brace in the left margin brackets this entire passage, from the sentence below through "...is now recommended." — the Dirichlet process mixture model model statement and the paragraph that follows it]*

A similar problem occurs in the Dirichlet process mixture model,

$$Y_i \mid \mu_i, \sigma^2 \sim N(\mu_i, \sigma^2), \; i = 1, \cdots, l$$

$$\mu_i \mid G \sim G$$

$$G \sim DP\{\alpha, N(\theta, \delta^2)\}$$

with priors $\pi(\alpha)$ and $\pi(\theta, \; \delta^2)$. Escobar and West (JASA 1995) gave a general algorithm in which the infinite dimensional distribution $G$ is integrated out. But it gives poor mixing (long-range dependence). Ever since researches [sic] have been searching for better algorithms. The most recent algorithm keeps $G$ and express [sic] $G$ using the stick breaking representation $G(\mu) = \sum_{s=1}^{\infty} w_s \delta_{\mu_s}(\mu)$ (Sethuraman, 1994). The algorithm of Kalli, Griffin, Walker (SC 2011) is now recommended. This algorithm will be discussed later.

When two or more parameters are weakly identified, we need to integrate some of them out and draw the others simultaneously. When it is desirable to draw two or more parameters at the same time, we use the multiplication rule of probability. Suppose, after integration or no integration, we have three parameters $(\theta_1, \theta_2, \theta_3)$. Then we can write

$$\pi(\theta_1, \theta_2, \theta_3 \mid \boldsymbol{y}) = \pi_1(\theta_1 \mid \boldsymbol{y}) \pi_2(\theta_2 \mid \theta_1, \boldsymbol{y}) \pi(\theta_3 \mid \theta_1, \theta_2, \boldsymbol{y})$$

> ✔ Verified: the stated decomposition $\pi(\theta_1,\theta_2,\theta_3\mid y)=\pi_1(\theta_1\mid y)\,\pi_2(\theta_2\mid\theta_1,y)\,\pi(\theta_3\mid\theta_1,\theta_2,y)$ holds with the marginal/conditional defined by the printed integrals.

where

$$\pi(\theta_1 \mid \boldsymbol{y}) = \int \int \pi(\theta_1, \theta_2, \theta_3 \mid \boldsymbol{y}) d\theta_2 d\theta_3$$

$$\pi(\theta_2 \mid \theta_1, \boldsymbol{y}) = \frac{\int \pi(\theta_1, \theta_2, \theta_3 \mid \boldsymbol{y}) d\theta_3}{\int \int \pi(\theta_1, \theta_2, \theta_3 \mid \boldsymbol{y}) d\theta_2 d\theta_3}$$

$$\propto \int \pi(\theta_1, \theta_2, \theta_3 \mid \boldsymbol{y}) d\theta_3$$

> ✔ Verified: the normalizing denominator of $\pi(\theta_2\mid\theta_1,y)$ does not depend on $\theta_2$, so $\pi(\theta_2\mid\theta_1,y) \propto \int \pi(\theta_1,\theta_2,\theta_3\mid y)\,d\theta_3$.

$$\pi(\theta_3 \mid \theta_1, \theta_2, \boldsymbol{y}) \propto \pi(\theta_1, \theta_2, \theta_3 \mid \boldsymbol{y}), \; \textit{no integration.}$$

It is sensible to consider the importance of the parameters in this decomposition. Here, $\theta_3$ is the most important parameter, followed by $\theta_2$ and then $\theta_1$. Also $\theta_1$ or $\theta_2$ may be nuisance

### PDF page 167 (booklet page 159)

parameters. So, $\pi(\theta_3\mid\theta_1,\theta_2,\boldsymbol{y})$ can be used to form a Rao-Blackwellized density estimator, and therefore relatively efficient.

*[margin note: "Block (Gibbs) sampler"]*

With many more parameters we can use blocking. That is, $\boldsymbol{\theta}_1$, $\boldsymbol{\theta}_2$, $\boldsymbol{\theta}_3$ can each be several parameters. This will improve mixing very much. *(The booklet writes $\theta$ with under-tildes to indicate vectors.)*

The priors, which we commonly used, will contribute to poor mixing as well. In complicated problems we may use 'shrinkage' or 'Cauchy' priors. These will vary with the parameters and whether the parameter is on the real line or a finite interval.

For $\theta$ in $(-\infty,\infty)$, (as a location-parameter)

$$\pi(\theta) = \frac{1}{\pi(1+\theta^2)},\; -\infty < \theta < \infty,\; (Cauchy)$$

$$\text{or preferable } \pi(\theta) = \frac{1}{b\pi\left(1+\left(\frac{\theta-a}{b}\right)^2\right)},\; -\infty < \theta < \infty$$

> ✔ Verified: Both stated Cauchy densities integrate to 1 over $(-\infty,\infty)$.

where $a$ and $b$ are specified (e.g., Gelman, Jakulin, Pittau, and Su, AAS 2008).

For $\sigma > 0$ (as a scale parameter), one may use

$$\pi(\sigma) = \frac{2}{c\pi\left(1+\frac{\sigma^2}{c}\right)},\; \sigma > 0,\; (half\ Cauchy)$$

where $c$ is to be specified. [Note that the prior $\pi(\sigma) \propto \frac{1}{\sigma}$ is no good (Gelman, BA 2006)]. If we take $\phi = \sigma^2$ in $\pi(\sigma) = \frac{2}{c\pi\left(1+\frac{\sigma^2}{c}\right)}$, $\sigma > 0$, we get

$$\pi(\phi) = \frac{1}{c\pi\sqrt{\phi}\left(1+\frac{\phi}{c}\right)},\; \phi > 0$$

> ✔ Verified: With $\phi=\sigma^2$, the change of variables on the half-Cauchy $\pi(\sigma)=\frac{2}{c\pi(1+\sigma^2/c)}$ gives $\pi(\phi)=\frac{1}{c\pi\sqrt{\phi}(1+\phi/c)}$.

That is,

$$\pi(\sigma^2) = \frac{1}{c\pi\sqrt{\sigma^2}\left(1+\frac{\sigma^2}{c}\right)},\; \sigma^2 > 0$$

Shrinkage priors are also used. The idea is as follows.

$$y\mid p \sim Ber(p),\; p \sim Beta(\mu\tau, (1-\mu)\tau)$$

So,

$$p\mid y \sim Beta(y+\mu\tau, (1-y)+(1-\mu)\tau)$$

> ✔ Verified: For $y\mid p\sim Ber(p)$ and $p\sim Beta(\mu\tau,(1-\mu)\tau)$, the posterior is $Beta(y+\mu\tau,(1-y)+(1-\mu)\tau)$.

and

$$E(p\mid y) = \lambda y + (1-\lambda)\mu,\; where\; \lambda = \frac{1}{1+\tau}$$

> ✔ Verified: The posterior mean is $E(p\mid y)=\lambda y+(1-\lambda)\mu$ with $\lambda=1/(1+\tau)$.

and $\lambda$ is called a shrinkage parameter. So, taking $\lambda \sim U(0,1)$ we have

$$\pi(\tau) = \frac{1}{(1+\tau)^2},\; \tau > 0$$

> ✔ Verified: If $\lambda=1/(1+\tau)\sim U(0,1)$, the induced density of $\tau$ is $\pi(\tau)=1/(1+\tau)^2$ on $\tau>0$, and it integrates to 1.

### PDF page 168 (booklet page 160)

As another example,

$$y\mid\mu \sim N(\mu,\sigma^2),\; \mu \sim N(\theta,\delta^2)$$

Then,

$$\mu\mid y \sim N\!\left(\lambda y + (1-\lambda)\theta,\, (1-\lambda)\delta^2\right),\; \lambda = \frac{\delta^2}{\delta^2+\sigma^2}$$

> ✔ Verified: Normal–normal conjugacy: the posterior of $\mu$ is $N(\lambda y+(1-\lambda)\theta,\ (1-\lambda)\delta^2)$ with $\lambda=\delta^2/(\delta^2+\sigma^2)$.

and

$$E(\mu\mid y) = \lambda y + (1-\lambda)\theta$$

Taking $\lambda \sim U(0,1)$, $\pi(\delta^2) = \frac{\sigma^2}{(\sigma^2+\delta^2)^2}$ and one may use $\pi(\delta^2) = \frac{a}{(a+\delta^2)^2}$, $\delta^2 > 0$ as the shrinkage prior for $\delta^2$. Generally $a = 1$ is used (e.g., Albert, Bayesian Statistics 3, 1988), Leonard and Novick (JASA, 1986) and Christensen and Morris (JASA, 1997). For a general discussion about shrinkage priors, see Natarajan and Kass (JASA, 2000).

> ✔ Verified: $\lambda=\delta^2/(\delta^2+\sigma^2)$, $\lambda\sim U(0,1)$, induces $\pi(\delta^2)=\sigma^2/(\sigma^2+\delta^2)^2$ on $\delta^2>0$.

> ✔ Verified: $\pi(\delta^2)=a/(a+\delta^2)^2$ integrates to 1 over $\delta^2>0$ for any $a>0$ (in particular $a=1$).

Shrinkage prior and Cauchy priors are generally recommended deep down in a hierarchical model. Priors like $\pi(\sigma^2) \propto \frac{1}{\sigma^2}$ create difficulties deep down in a hierarchical model (Gelman, BA 2006). Integration, blocking and multiplication rule are used when weakly identified parameters are suspect in a model. Rao-Blackwellization should be used to improve efficiency. Reparametrization is also recommended (Nandram and Chen, JSCS 1996).

**15.2 Numerical Techniques**

**15.2.1 Numerical Integration (Gaussian Quadrature)**

Use orthogonal polynomials,

$$\int f(x)dx \approx \sum_{k=1}^{R} w_k f(x_k)$$

for an $R$-point quadrature with roots $(x_1,\cdots,x_R)$ and weights $(w_1,\cdots,w_R)$.

- $\textit{Legendre}\;:\; \int_a^b f(x)dx = \sum_{k=1}^{R} w_k f(x_k), (a,b)\;:\; \textit{finiteinterval.}$ [sic: "finite interval" is set with no space]
- $\textit{Laguerre}\;:\; \int_0^{\infty} x^{\alpha}e^{-x} f(x)dx = \sum_{k=1}^{R} w_k f(x_k)$
- $\textit{Hermite}\;:\; \int_{-\infty}^{\infty} e^{-x^2} f(x)dx = \sum_{k=1}^{R} w_k f(x_k)$
- $\textit{Jacobi}\;:\; \int_{-1}^{1} (1-x)^{\alpha}(1+x)^{\beta} f(x)dx = \sum_{k=1}^{R} w_k f(x_k),\; ,$ [sic: a stray second comma ends the line]

$a$, $b$ any values (integrability)

### PDF page 169 (booklet page 161)

**15.2.2 Grid sampler**

Awkward density, transform to $(0,1)$.

*[Figure: a smooth bimodal density $\pi(\theta)$ plotted against $\theta$ on the horizontal axis, rising from near zero at $\theta=0$ to a lower left mode, dipping slightly, then rising to a higher right mode before decaying to near zero at $\theta=1$. The horizontal axis is tick-marked at $0$, $.01$, $.02$, then $.60$, $.61$, then $.99$, $1$, indicating a fine grid over $(0,1)$. A narrow vertical strip between $.60$ and $.61$ is drawn under the curve on the rising side of the right mode and is labeled $h_g$ with an arrow pointing to it, representing the height of the density over the $g$th grid interval.]*

Equal widths, so $p_g \propto h_g$, $g = 1, \cdots, G(= 100)$. This creates a probability mass function. Draw a value from this mass function. This gives the interval in which the deviate lies. Now draw a uniform random number from this interval (i.e., jitter the deviate already drawn). If the density is unimodal and its mode lies in the interior of $(0,1)$, the grid procedure works well. This procedure also works well if the density is multimodal with the modes in the interior of $(0,1)$.

However, if a mode is on the boundary, we must use the grid method adaptively. First, locate the high density region, and search in its neighborhood for the 'total' probability. One may use fewer grids($\approx 20$) to do the grid search. Also, if the function is expensive to compute, use another technique.

**15.2.3 Sampling Importance Resampling (SIR) Algorithm**

- Rubin (JASA 1987, BS 1988)

Let $f(x)$ be the density function of interest, and let $f_a(x)$ denote an approximation of $f(x)$ such that $\frac{f(x)}{f_a(x)} < A$, finite (Geweke, EC 1989). To get a sample from $f(x)$, the SIR algorithm subsamples a large sample $M^*$, $x_1, \cdots, x_{M^*} \overset{iid}{\sim} f_a(x)$ with weights

$$w_h \propto \frac{f(x_h)}{f_a(x_h)},\; h = 1, , M^* \quad \text{[sic: the index range is printed with a missing entry, "$h=1, , M^*$"]}$$

*(The booklet writes $x$ with under-tildes to indicate vectors.)*

Subsample without replacement at a rate of at most 10% so that if we want a sample of $M = 1,000$ from $f(x)$, we need $M^* = 10,000$. Thus, we want to be able to draw samples very fast from $f_a(x)$, see Gelman et al. (CH, 3rd edition, 2013).

> ✔ Verified: Subsampling M = 1,000 from M* = 10,000 without replacement corresponds to a rate of exactly 10%.

The boundedness condition is important. So we need to prove it. One can also check that the weights $\{w_h\}$ are not too variable. Clearly, if $w_h = \frac{1}{M^*}$ gives the best (ideal) 'approximation'. So we need $w_h \approx \frac{1}{M^*}$ and specifically we want no dominant weights.

> ✔ Verified: When f = f_a the normalized SIR weights are exactly 1/M* for every h, and any set of normalized weights sums to 1.

### PDF page 170 (booklet page 162)

**15.2.4 Rao-Blackwellization**

Rao-Blackwellization ensures efficiency, much needed in MCMC computations. Let $\theta$ and $\phi$ be two parameters with $\theta$ the parameter of interest. Then, note that

$$\pi(\theta|\boldsymbol{y}) = \int \pi(\theta|\phi,\boldsymbol{y})\pi(\phi|\boldsymbol{y})d\phi$$

*(The booklet writes $y$ with an under-tilde to indicate a vector.)*

and

$$E(\theta|\boldsymbol{y}) = \int E(\theta|\phi,\boldsymbol{y})\pi(\phi|\boldsymbol{y})d\phi$$

> ✔ Verified: Marginalization identities π(θ|y)=∫π(θ|φ,y)π(φ|y)dφ and E(θ|y)=∫E(θ|φ,y)π(φ|y)dφ, checked on a concrete conjugate normal example.

where we assume that $\pi(\theta|\phi,\boldsymbol{y})$ and $E(\theta|\phi,\boldsymbol{y})$ are in closed forms.

Suppose we have a random sample $\phi_1,\cdots,\phi_M \sim \pi(\phi|\boldsymbol{y})$. Then,

$$\hat{\pi}(\theta|\boldsymbol{y}) = \frac{1}{M}\sum_{h=1}^{M} \pi(\theta|\phi^{(h)},\boldsymbol{y})$$

is a Rao-Blackwellized density estimator, and

$$E(\hat{\theta}|\boldsymbol{y}) = \frac{1}{M}\sum_{h=1}^{M} E(\theta|\phi^{(h)},\boldsymbol{y})$$

is a Rao-Blackwellized estimator of $E(\theta|\boldsymbol{y})$.

Suppose we also have a random sample $\theta^{(1)},\cdots,\theta^{(M)}$. Estimators based on $\theta^{(1)},\cdots,\theta^{(M)}$ are not as good as Rao-Blackwellized estimators which have smaller mean squared errors (Gelfand and Smith, JASA 1990). For example, $\frac{1}{M}\sum_{h=1}^{M} E(\theta|\phi^{(h)},\boldsymbol{y})$ has smaller MSE than $\frac{1}{M}\sum_{h=1}^{M}\theta^{(h)}$.

## 15.3 Examples

**15.3.1 Generalized Gamma**

$$f(y|\alpha,\beta,\gamma) = \frac{\gamma\beta(\beta y)^{\alpha\gamma-1}e^{-(\beta y)^{\gamma}}}{\Gamma(\alpha)},\;\; y>0, \alpha,\beta,\gamma>0$$

> ✔ Verified: The generalized gamma density f(y|α,β,γ) = γβ(βy)^{αγ-1} e^{-(βy)^γ} / Γ(α) integrates to 1.

1. It is very flexible and it contains many distributions. When $\gamma=1$, $Y \sim Gam(\alpha,\beta)$. It also contains Weibull, half normal, Rayleigh, lognormal, etc.

> ✔ Verified: When γ=1 the generalized gamma reduces to Gam(α,β) with rate β, i.e. β^α y^{α-1} e^{-βy}/Γ(α).

2. $E(Y^s) = \frac{1}{\beta^s}\frac{\Gamma(\frac{s}{\gamma}+\alpha)}{\Gamma(\alpha)}$, $\;s=1,2,\cdots$

> ✔ Verified: E(Y^s) = β^{-s} Γ(s/γ + α) / Γ(α) for Y ~ GG(α,β,γ).

3. Closed under power transformation (i.e., $Y^s$ has a generalized gamma distribution)

> ✔ Verified: Closure under power transformation: if Y ~ GG(α,β,γ) then Z = Y^s ~ GG(α, β^s, γ/s).

4. $Y^{\gamma} \sim Gam(\alpha,\beta^{\gamma})$ ; it is easy to sample.

> ✔ Verified: W = Y^γ ~ Gam(α, β^γ), i.e. W has density (β^γ)^α w^{α-1} e^{-β^γ w} / Γ(α).

5. $Y_1,\cdots,Y_n \overset{iid}{\sim} GG(\alpha,\beta,\gamma)$

### PDF page 171 (booklet page 163)

MLEs are difficult to obtain and MMEs are generally used. Both skewness and kurtosis are functions of $\alpha$ and $\gamma$, shape parameters. Specifically, $\alpha$ and $\gamma$ are difficult to estimate via MLEs. Interestingly, $\bar{Y}$ independent of $\frac{S}{\bar{Y}}$, $n \geq 3$ is a characterization of this distribution.

Let us consider a stratified random sample as follows.

$$Y_{i1}, Y_{i2}, \cdots, Y_{i,n_i} \mid \beta_i, \alpha, \gamma \overset{ind}{\sim} GG(\alpha, \beta_i, \gamma), \; i = 1, \cdots, H$$

$$\pi(\alpha, \beta_i, \gamma) \propto \prod_{i=1}^{H} \frac{1}{\beta_i} \frac{1}{(1+\alpha)^2} \frac{1}{(1+\gamma)^2}, \; noninformation$$

Now, make the transformation $\phi_i = \beta_i^{\gamma}$, $i = 1, \cdots, H$. Then,

$$\pi(\boldsymbol{\phi}, \alpha, \gamma \mid \boldsymbol{y}) \propto \gamma^{n-H} \prod_{i=1}^{H} \left\{ \frac{\phi_i^{\alpha-1} \left( \prod_{j=1}^{n_i} y_{ij} \right)^{\alpha\gamma-1} e^{-\phi_i \sum_{j=1}^{n_i} y_{ij}^{\gamma}}}{\Gamma(\alpha)} \right\} \frac{1}{(1+\alpha)^2} \frac{1}{(1+\gamma)^2},$$

where $n = \sum_{i=1}^{H} n_i$. Observe that $\phi_i \mid \alpha, \gamma, \boldsymbol{y} \overset{ind}{\sim} Gam\left\{ n_i \left( \alpha - \frac{1}{\gamma} \right) + \frac{1}{\gamma}, \; \sum_{j=1}^{n_i} y_{ij}^{\gamma} \right\},$ *[sic: a stray comma follows the brace]*. Then, integrating out $\boldsymbol{\phi}$,

$$\pi(\alpha, \gamma \mid \boldsymbol{y}) \propto \frac{\gamma^{n-H} \prod_{i=1}^{H} \left( \prod_{j=1}^{n_i} y_{ij} \right)^{\alpha\gamma-1}}{\Gamma(\alpha)^n \prod_{i=1}^{H} \left[ \sum_{j=1}^{n_i} y_{ij}^{\gamma} \right]^{n_i \left( \alpha - \frac{1}{\gamma} \right) + \frac{1}{\gamma}}} \frac{1}{(1+\alpha)^2} \frac{1}{(1+\gamma)^2}$$

> ✔ Verified: Integrating the Gamma kernel in $\phi_i$ yields $\Gamma(a_i)\,b_i^{-a_i}$ with $a_i = n_i(\alpha-1/\gamma)+1/\gamma$, matching the exponent printed on $\sum_j y_{ij}^\gamma$.

Letting $\delta_1 = \frac{1}{(1+\alpha)}$ and $\delta_2 = \frac{1}{(1+\gamma)}$, $0 < \delta_1, \delta_2 < 1$,

$$\pi(\delta_1, \delta_2 \mid \boldsymbol{y}) \propto \left\{ \frac{\gamma^{n-H} \left( \prod_{i=1}^{H} \prod_{j=1}^{n_i} y_{ij} \right)^{\alpha\gamma-1}}{\Gamma(\alpha)^n \prod_{i=1}^{H} \left[ \sum_{j=1}^{n_i} y_{ij}^{\gamma} \right]^{n_i \left( \alpha - \frac{1}{\gamma} \right) + \frac{1}{\gamma}}} \right\}$$

> ✔ Verified: The reparametrization $\delta_1=1/(1+\alpha)$, $\delta_2=1/(1+\gamma)$ has Jacobian $(1+\alpha)^{-2}(1+\gamma)^{-2}$ in reverse, so those two prior factors are exactly absorbed and $\pi(\delta_1,\delta_2\mid y)$ equals the bracketed kernel with no leftover factor.

Tnen [sic],

$$\begin{aligned}
\pi(\delta_1 \mid \boldsymbol{y}) &\propto \quad \int_0^1 \pi(\delta_1, \delta_2 \mid \boldsymbol{y}) \, d\delta_2 \\
&\approx \quad \sum_{g=1}^{G} w_g \pi(\delta_1, \delta_2^{(g)} \mid \boldsymbol{y}) \quad ,
\end{aligned}$$

where $\delta_2^{(g)}$ are the roots of a Legendre polynomials with weights in . *[sic: the sentence has a missing word before the period — "with weights in ."]* Also,

$$\pi(\delta_2 \mid \delta_1, \boldsymbol{y}) \propto \pi(\delta_1, \delta_2 \mid \boldsymbol{y})$$

We can now sample $\delta_1$ and $\delta_2$ using grid samplers. Thus, finally

$$\pi(\boldsymbol{\phi}, \delta_1, \delta_2 \mid \boldsymbol{y}) = \left\{ \prod_{i=1}^{H} \pi_1(\phi_i \mid \delta_1, \delta_2, \boldsymbol{y}) \right\} \pi_2(\delta_2 \mid \delta_1, \boldsymbol{y}) \pi_3(\delta_1 \mid \boldsymbol{y})$$

and the Gibbs sampler is avoided. Retransform to $\alpha$, $\gamma$, $\beta_i$, $i = 1, \cdots, H$.

<u>Length-Biased sampling of shrubs</u>

### PDF page 172 (booklet page 164)

*[Figure: a schematic of a line-transect sampling design. A horizontal baseline runs left to right, annotated at its right end "125 meters". Three vertical transect lines rise from the baseline, labeled I, II, and III from left to right. Transects I and II are each crossed by several short horizontal tick marks at varying heights (the shrubs detected along each transect — some ticks lie to the left of the line, some to the right, some straddle it); transect III has no ticks drawn on it. Below the baseline the figure is captioned "Three transect" [sic], and beneath the three transect labels the counts 18, 22, and 6 are printed.]*

Three transect *[sic]*

| I | II | III |
|---|----|-----|
| 18 | 22 | 6 |

Data on shrubs (Muttlak, PhD Dissertation, 1988)

Gamma

| Parameters | PM | PSD | NE | CrI (lower) | CrI (upper) |
|---|---|---|---|---|---|
| $\alpha$ | 8.46354 | 0.2588 | 0.00273 | 8.02697 | 8.87001 |
| $\beta_1$ | 11.13608 | 0.95171 | 0.01005 | 9.31114 | 13.02689 |
| $\beta_2$ | 6.71812 | 0.53044 | 0.00535 | 5.71673 | 7.76227 |
| $\beta_3$ | 5.83506 | 0.84355 | 0.00866 | 4.26981 | 7.54196 |

> ✔ Verified: Gamma table — each CrI is well-ordered, brackets its posterior mean, and each NE satisfies 0 < NE < PSD.

Generalized Gamma

| Parameters | PM | PSD | NE | CrI (lower) | CrI (upper) |
|---|---|---|---|---|---|
| $\alpha$ | 7.80982 | 0.56412 | 0.0056 | 6.70573 | 8.83051 |
| $\gamma$ | 1.11996 | 0.06952 | 0.00066 | 1.00271 | 1.23006 |
| $\beta_1$ | 7.62576 | 1.91411 | 0.01847 | 4.61915 | 11.29641 |
| $\beta_2$ | 4.61612 | 1.12943 | 0.01069 | 2.83457 | 6.74900 |
| $\beta_3$ | 4.03654 | 1.08502 | 0.01040 | 2.24671 | 6.19703 |

> ✔ Verified: Generalized Gamma table — each CrI is well-ordered, brackets its posterior mean, and each NE satisfies 0 < NE < PSD.

> ✔ Verified: For the shared parameters, the Generalized Gamma posterior is more diffuse than the Gamma posterior (larger PSD and wider CrI).

### PDF page 173 (booklet page 165)

**15.3.2 Skewed Exponential Power Distribution**

Azzalini (Statistica 1986, SJS 1985)
DiCiccio (JASA 2004)

$$f(y|\mu,\sigma^2,\lambda,\alpha) = \frac{1}{2\sigma\alpha^{\frac{1}{\alpha}-1}\Gamma(\frac{1}{\alpha})}\,exp\left\{\frac{-|\frac{y-\mu}{\sigma}|^{2\alpha}}{2\alpha}\right\}\Phi\left\{sign\!\left(\lambda(\tfrac{y-\mu}{\sigma})\right)\frac{|\lambda(\frac{y-\mu}{\sigma})|^{\alpha}}{\sqrt{\alpha}}\right\}$$

*(sic: the constant $2\sigma\alpha^{\frac1\alpha-1}\Gamma(\frac1\alpha)$ normalizes the kernel $\exp\{-|z|^{\alpha}/\alpha\}$, not the printed $\exp\{-|z|^{2\alpha}/(2\alpha)\}$, and the skew-symmetric factor $2$ is absent; as printed the function does not integrate to $1$.)*

where $-\infty < y < \infty$, $-\infty < \lambda$, $\mu < \infty$, $\alpha \geq 1$ (logconcavity ?).

$$Y \sim SEP(\mu,\sigma^2,\lambda,\alpha)$$

1. If $\alpha = 1$, we get the skewed normal density (logconcave).
2. $\alpha$controls [sic: no space] scale and $\lambda$ symmetric; skewness and kurtosis are functions of $\alpha$ and $\lambda$.
3. $Y$ can be generated easily. Set $Z = \frac{Y-\mu}{\sigma}$.

$$f(z|\mu,\sigma^2,\lambda,\alpha) = \frac{1}{2\alpha^{\frac{1}{\alpha}-1}\Gamma(\frac{1}{\alpha})}\,exp\left\{\frac{-|z|^{2\alpha}}{2\alpha}\right\}\Phi\left\{sign(\lambda z)\frac{|\lambda z|^{\alpha}}{\sqrt{\alpha}}\right\}$$

*(sic: as printed, at $\alpha=1$ this is $\tfrac12 e^{-z^2/2}\Phi(\lambda z)$, not the skew-normal density $2\phi(z)\Phi(\lambda z)$ — its total mass is $\sqrt{2\pi}/4 \approx 0.627$, not $1$; the correct constant would be $2/\sqrt{2\pi}$ at $\alpha=1$.)*

> ⚠ Check FAILED: At $\alpha=1$ the printed $f(z|\mu,\sigma^2,\lambda,\alpha)$ is the skew-normal density $2\phi(z)\Phi(\lambda z)$ (in particular it integrates to 1). — the stated result did not reproduce (see verification log)

$$T = R_1(-\alpha B\,lnU)^{1/\alpha},\;\; U \sim U(0,1),\;\; B \sim B\!\left(\frac{1}{\alpha},\,1-\frac{1}{\alpha}\right)$$

| $R_1$ | 1 | -1 |
|---|---|---|
| Prob. | $\frac{1}{2}$ | $\frac{1}{2}$ |

$$,\;\; W = sign(T)|T|^{\frac{\alpha}{2}}\left(\frac{1}{\alpha}\right)^{\frac{1}{2}}$$

| $R_2$ | 1 | -1 |
|---|---|---|
| Prob. | $\Phi(W)$ | $\Phi(-W)$ |

$$,\;\; Z = R_2 T$$

Stefanescu (ECECs (?) 1987), Azzalin [sic] (Statistica 1986)

If $\alpha < 1$ , what can we do?

4. For a random sample from $SEP(\mu,\sigma^2,\lambda,\alpha)$, it is difficult to obtain MLEs (DiCiccio and Monte, JASA 2004).

Now

$$y_1, y_2, \cdots, y_n|\mu,\sigma^2,\lambda,\alpha \sim SEP(\mu,\sigma^2,\lambda,\alpha)$$

$$\pi(\mu,\sigma^2,\lambda,\alpha) = \frac{1}{\pi(1+\mu^2)}\,\frac{1}{(1+\sigma^2)^2}\,\frac{1}{\pi(1+\lambda^2)}\,\frac{1}{(1+\alpha)^2}.$$

> ✔ Verified: The prior $\pi(\mu,\sigma^2,\lambda,\alpha)=\frac{1}{\pi(1+\mu^2)}\frac{1}{(1+\sigma^2)^2}\frac{1}{\pi(1+\lambda^2)}\frac{1}{(1+\alpha)^2}$ integrates to 1 over $\mu,\lambda\in\mathbb{R}$, $\sigma^2>0$, $\alpha>0$.

One possibility is

$$\pi(\mu,\sigma^2|\lambda,\alpha,y) = \int_0^\infty\!\!\int_0^\infty \pi(\mu,\sigma^2,\lambda,\alpha|y)\,d\lambda\,d\alpha.$$

*(sic: the left-hand side is written as the conditional $\pi(\mu,\sigma^2|\lambda,\alpha,y)$ although $\lambda$ and $\alpha$ are integrated out on the right; the $\lambda$ integral is also written over $(0,\infty)$ despite $\lambda$ ranging over the whole real line above.)*

Observe that if $\lambda = 0$, $\alpha = 1$, we get

$$y_1,\cdots,y_n|\mu,\sigma^2 \overset{iid}{\sim} N(\mu,\sigma^2)$$

*(sic: the stated reduction does not hold for the density as printed — at $\lambda=0$, $\alpha=1$ it gives $\frac{1}{4\sigma}e^{-\frac{(y-\mu)^2}{2\sigma^2}}$, not the $N(\mu,\sigma^2)$ pdf $\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(y-\mu)^2}{2\sigma^2}}$.)*

> ⚠ Check FAILED: The printed SEP density at $\lambda=0$, $\alpha=1$ equals the $N(\mu,\sigma^2)$ pdf. — the stated result did not reproduce (see verification log)

### PDF page 174 (booklet page 166)

Now, it is convenient to take

$$\pi(\mu,\sigma^2) \propto \frac{1}{\sigma^2}$$

$$\frac{(n-1)s^2}{\sigma^2}\Big|\boldsymbol{y} \sim \chi^2_{n-1}$$

$$\mu|\sigma^2,\boldsymbol{y} \sim N\!\left(\bar{y}, \frac{\sigma^2}{n}\right)$$

> ✔ Verified: Under the prior $\pi(\mu,\sigma^2)\propto 1/\sigma^2$, integrating $\mu$ out of the normal posterior leaves a kernel in $\sigma^2$ whose change of variables $t=(n-1)s^2/\sigma^2$ is exactly the $\chi^2_{n-1}$ density.

> ✔ Verified: The conditional posterior of $\mu$ given $\sigma^2$ and the data is exactly $N(\bar y,\sigma^2/n)$.

That is, $\pi_*(\mu,\sigma^2|\boldsymbol{y})$ is in closed form and samples can be drawn easily. So, it is sensible to use the SIR algorithm. Then,

$$w_h \propto \frac{\int_0^{\infty}\int_0^{\infty}\pi(\mu^{(h)},\sigma^{2(h)},\lambda,\alpha|\boldsymbol{y})\,d\lambda\,d\alpha}{\pi_*(\mu^{(h)},\sigma^{2(h)}|\boldsymbol{y})}$$

$h = 1,\cdots,M^*$, a large sample from $\pi_*(\mu,\sigma^2|\boldsymbol{y})$. If it is necessary, we can sample $\lambda$ and $\alpha$ via

$$\pi(\lambda,\alpha|\mu,\sigma^2,\boldsymbol{y}) = \pi(\lambda|\alpha,\mu,\sigma^2,\boldsymbol{y})\pi(\alpha|\mu,\sigma^2,\boldsymbol{y}).$$

Reparameterize as following

$$\lambda = \frac{\phi}{\sqrt{1-\phi^2}},\; -1 < \phi < 1,\; \frac{\phi+1}{2} = \gamma,\; 0 < \gamma < 1$$

$$\rho = \frac{1}{\alpha},\; \alpha = \frac{1}{\rho},\; 0 < \rho < 1$$

> ✔ Verified: $\lambda=\phi/\sqrt{1-\phi^2}$ is a strictly increasing bijection from $(-1,1)$ onto $\mathbb{R}$ with inverse $\phi=\lambda/\sqrt{1+\lambda^2}$.

> ✔ Verified: $\gamma=(\phi+1)/2$ carries $(-1,1)$ bijectively onto $(0,1)$, and $\rho=1/\alpha$ is equivalent to $\alpha=1/\rho$ (with $0<\rho<1 \iff \alpha>1$).

Data on Income (Aitkin, C&H, 2010)
Normal

| Parameters | PM | PSD | NE | CrI | |
|---|---|---|---|---|---|
| $\mu$ | 67.22986 | 3.52095 | 0.10288 | 61.07992 | 74.73615 |
| $\sigma^2$ | 543.10760 | 129.05028 | 3.59936 | 322.47012 | 810.90192 |

*[In the booklet the heading "CrI" is centered over the last two columns, which give the lower and upper endpoints of the credible interval.]*

> ✔ Verified: The printed posterior summary table is internally coherent: each posterior mean lies strictly inside its credible interval, each interval is ordered, and each numerical error is smaller than the corresponding posterior standard deviation.

### PDF page 175 (booklet page 167)

Skewed Exponential Power

| Parameters | PM | PSD | NE | CrI | |
|---|---|---|---|---|---|
| $\mu$ | 72.50247 | 3.82345 | 0.14551 | 68.39066 | 79.88062 |
| $\sigma^2$ | 572.33398 | 154.81268 | 7.43032 | 300.77640 | 857.00165 |
| $\alpha$ | | | | | |
| $\gamma$ | | | | | |

*(The $\alpha$ and $\gamma$ rows are printed with no entries.)*

**15.3.3 Normal-means Model**

$$y_{ij}|\mu_i,\sigma^2 \overset{ind}{\sim} N(\mu_i,\sigma^2),\; i=1,\cdots,l,\; j=1,\cdots,n_i,$$
$$\mu_i|\theta,\delta^2 \overset{ind}{\sim} N(\theta,\delta^2)$$
$$\pi(\theta,\sigma^2,\delta^2),\;\text{improper prior;}$$
$$\text{may lead to improper posterior}$$

Note that $y_{ij}|\theta,\sigma^2,\delta^2 \sim N(\theta,\sigma^2+\delta^2)$.

> ✔ Verified: Marginalizing $\mu \sim N(\theta,\delta^2)$ out of $y|\mu \sim N(\mu,\sigma^2)$ yields $N(\theta,\sigma^2+\delta^2)$.

So $Cov(y_{ij},y_{ij'}|\theta,\sigma^2,\delta^2)=\delta^2$, $Cor(y_{ij},y_{ij'}|\theta,\sigma^2,\delta^2)=\frac{\delta^2}{\delta^2+\sigma^2}=\rho$, $0<\rho<1$

> ✔ Verified: For $j\neq j'$, $Cov(y_{ij},y_{ij'})=\delta^2$ and $Cor(y_{ij},y_{ij'})=\delta^2/(\delta^2+\sigma^2)$.

and $\delta^2=\frac{\rho}{1-\rho}\sigma^2$

> ✔ Verified: $\rho=\delta^2/(\delta^2+\sigma^2)$ $\iff$ $\delta^2=\frac{\rho}{1-\rho}\sigma^2$, with $\delta^2>0 \iff 0<\rho<1$.

$$y_{ij}|\mu_i,\sigma^2 \overset{ind}{\sim} N(\mu_i,\sigma^2)$$
$$\mu_i|\theta,\delta^2 \overset{iid}{\sim} N\!\left(\theta,\frac{\rho}{1-\rho}\sigma^2\right)$$
$$\pi(\theta,\sigma^2,\rho) \propto \frac{1}{\sigma^2},\; \textit{(not a problem)}$$

$\pi(\mu,\theta,\sigma^2,\rho|y)$ is proper, $0\le\rho\le 1$. (Nandram, Toto, Choi, JSCS 2011)

*(The booklet sets $\mu$ and $y$ in boldface here to indicate vectors.)*

### PDF page 176 (booklet page 168)

There is no need for a Gibbs sampler because

$$\pi(\boldsymbol{\mu},\theta,\sigma^2,\rho|\boldsymbol{y}) = [\prod_{i=1}^{l}\pi(\mu_i|\theta,\sigma^2,\rho,\boldsymbol{y})]\times\pi(\theta|\sigma^2,\rho,\boldsymbol{y})\times\pi(\sigma^2|\rho,\boldsymbol{y})\times\pi(\rho|\boldsymbol{y})$$

$$\mu_i|\theta,\sigma^2,\rho,\boldsymbol{y}\overset{ind}{\sim} N(\lambda_i\bar{y}_i + (1-\lambda_i)\theta, (1-\lambda_i)\frac{\rho}{1-\rho}\sigma^2),\; i=1,\cdots,l,$$

$$\theta|\sigma^2,\rho,\boldsymbol{y}\sim N(\bar{y}, \frac{\rho\sigma^2}{1-\rho}\frac{1}{\sum_{i=1}^{l}\lambda_i}),\; \bar{y}=\sum_{i=1}^{l}\lambda_i y_i\Big/\sum_{i=1}^{l}\lambda_i$$

$$\lambda_i = \frac{\rho n_i}{(\rho(n_i-1)+1)},\; i=1,\cdots,l$$

$$\sigma^2|\rho,\boldsymbol{y}\sim Gam\Big\{\frac{n-1}{2}, \frac{\sum(n_i-1)s_i^2 + \frac{1-\rho}{rho}\sum\lambda_i(\bar{y}_i-\bar{y})^2}{2}\Big\}$$
*(sic: the booklet prints `rho` in upright text in the denominator instead of the symbol $\rho$ — a LaTeX typo for `\rho`.)*

$$\pi(\rho|\boldsymbol{y})\propto\frac{1}{\sqrt{\sum_{i=1}^{l}\lambda_i}}\sqrt{\frac{\rho}{1-\rho}}\Big\{\prod_{i=1}^{l}\sqrt{1-\lambda_i}\Big\}\Big\{1+\frac{1-\rho}{\rho}\frac{\sum_{i=1}^{l}\lambda_i(\bar{y}_i-\bar{y})^2}{\sum_{i=1}^{l}(n_i-1)s_i^2}\Big\},\; 0\le\rho\le 1$$

<u>Data on Corn (Battese, Harter and Fuller – JASA 1988)</u>

*[margin note, left of this heading, in cursive: "Satellite(?) data pixels(?) / segments(?)"]*

<u>No Gibbs Sampling)</u> [sic: stray closing parenthesis, no opening one]

|   | PM | PSD | NE | CrI | |
|---|---|---|---|---|---|
| 1 | 120.91843 | 6.34870 | 0.22719 | 107.91113 | 132.63448 |
| 2 | 1021.35559 | 267.93613 | 7.83026 | 578.79034 | 1527.67493 |
| 3 | 0.12213 | 0.11012 | 0.00399 | 0.00006 | 0.35002 |

|   |   | PM | PSD | NE | | | |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 165.78 | 126.32561 | 13.06241 | 0.4713 | 104.68925 | 153.95279 |
| 2 | 1 | 96.32 | 118.57426 | 11.92261 | 0.40591 | 92.2757 | 140.01227 |
| 3 | 1 | 76.08 | 115.55293 | 13.53117 | 0.42258 | 86.75901 | 141.61496 |
| 4 | 2 | 150.89 | 126.81919 | 11.59609 | 0.38585 | 105.44631 | 150.54846 |
| 5 | 3 | 158.62334 | 130.47089 | 11.81056 | 0.36817 | 109.05437 | 153.2645 |
| 6 | 3 | 102.52334 | 116.15257 | 10.7749 | 0.30099 | 94.46323 | 136.23317 |
| 7 | 3 | 112.77334 | 118.40436 | 10.38271 | 0.31744 | 98.01175 | 138.65733 |
| 8 | 3 | 144.29668 | 127.37929 | 11.77414 | 0.40307 | 104.29713 | 150.13007 |
| 9 | 4 | 117.59499 | 119.80698 | 9.92397 | 0.3505 | 100.55747 | 139.99747 |
| 10 | 5 | 109.382 | 117.31458 | 9.28502 | 0.29733 | 99.00871 | 135.52664 |
| 11 | 5 | 110.252 | 117.13784 | 9.71864 | 0.38215 | 95.8265 | 134.86015 |
| 12 | 6 | 114.81 | 118.4588 | 8.85927 | 0.27281 | 98.52406 | 133.81252 |

*(The second table prints only the headers PM, PSD, NE over its third, fourth and fifth numeric columns; the remaining three columns are unlabelled.)*

<u>Gibbs Sampling</u>

nmc $= 11000$

nthrow $= 1000$

ngap $= 10$

### PDF page 177 (booklet page 169)

Geweke p-value

```
0.3423239
0.5000000   1000.000
0.9139895
0.5000000   1000.000
0.8757767
0.6703798    745.8459
```

```
1   121.01549     7.21871    0.24762   106.57100    134.82939
2   976.25714   259.63290    7.07859   503.72510   1461.44446
3     0.20912     0.15350    0.00517     0.00011       0.51083
```

```
 1  1   165.78    130.26892   16.49919   0.56252    99.92773   165.7486
 2  1    96.32    114.97064   15.60096   0.56963    83.90848   148.98987
 3  1    76.08    111.27788   15.82035   0.41896    80.89629   142.03387
 4  2   150.89    130.31976   14.07716   0.40605   105.27631   160.52652
 5  3   158.62334 135.89536   14.85845   0.47216   110.31654   166.65144
 6  3   102.52334 114.17322   12.06631   0.40165    88.8833    136.61745
 7  3   112.77334 117.75304   11.79966   0.35538    95.7739    142.6429
 8  3   144.29668 130.51973   12.87984   0.43934   109.66248   160.6871
 9  4   117.59499 119.22592   11.13186   0.33324    98.08789   141.9789
10  5   109.382   114.92945   10.92482   0.28922    90.50347   134.01648
11  5   110.252   115.23555   10.5665    0.31353    93.67265   133.88426
12  6   114.81    118.25127    9.80868   0.35325    99.16428   138.98106
```

*[a long hand-drawn wavy horizontal rule runs across the page here, separating the R output above from the text below]*

Finally, I mention Dirichlet process mixture (DPM) model,

$$y_{ij}\mid \theta_i, \sigma^2 \overset{ind}{\sim} N(\theta_i, \sigma^2),\; j = 1, \cdots, n_i,\; i = 1, \cdots, l$$

$$\theta_i \mid G \overset{iid}{\sim} G$$

$$G \mid \eta, \delta^2 \sim DP(\alpha, N(\eta, \delta^2))$$

If $\alpha \to$, we get the normal-means model. There are two methods to fit model. *[sic: the limit is left blank after "$\alpha \to$"; also "to fit model" is missing an article]*

(1) Marginal method
Here, the infinite dimensional distribution, $G$, is integrated out – Escobar and West (JASA 1994),

$$\theta_1 \sim N(\eta, \delta^2)$$

$$\theta_2 \mid \theta_1 \sim \frac{1}{1+\alpha}\delta_{\theta_1}(\theta_2) + \frac{\alpha}{1+\alpha} N_{\theta_2}(\eta, \delta^2)$$

$$\theta_3 \mid \theta_1, \theta_2 \sim \frac{2}{2+\alpha}\,\frac{\delta_{\theta_1}(\theta_3) + \delta_{\theta_2}(\theta_3)}{2} + \frac{\alpha}{2+\alpha} N_{\theta_3}(\eta, \delta^2)$$

$$\vdots$$

> ✔ Verified: Escobar–West Pólya urn conditionals: mixture weights sum to 1, and the printed $n=1,2$ lines match $\frac{n}{n+\alpha}\bar\delta_n + \frac{\alpha}{n+\alpha}N(\eta,\delta^2)$

### PDF page 178 (booklet page 170)

Poor mixing is a serious problem, the constituents of a cluster remain constant for a long time. There are many methods which attempted to solve this problem (e.g., Neal, JCGS 2000). They are not satisfactory.

(2) Non-marginal (conditional) method
This method keeps the infinite dimensional distribution in the problem (e.g., Kalli, Griffin and Walker, SC 2011). It uses the stick-breaking representation of $G$ (Sethuraman, SS 1994) to sample the joint posterior density.

*(The remainder of the page is blank.)*

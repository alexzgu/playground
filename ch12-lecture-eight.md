# Chapter 12 — Lecture Eight
*(PDF pages 136–143; booklet pages 131–138)*


### PDF page 136 (booklet page 131)

*[Handwritten scratch note in the top right margin, partly legible: an overwritten label — `[illegible]` struck over — reading `$\hat{\theta}$`(?) / `$\hat{p}_{MLE}$`(?), then `$= \sum_{i=1}^{n} \hat{y_i}(\hat{\theta})$`(?) with `n`(?) written below the summation sign, underscored by a long sweeping rule. These appear to be lecture scratch notes on plugging a point estimate $\hat\theta$ into the discrepancy function.]*

# Chapter 12 — Lecture Eight

**12.1 Bayesian predictive $p$-value ($BPP$)**

We start with a discrepancy function

1. $\chi^2$ type

$$T(y, \theta) = \sum_{i=1}^{n} \frac{[y_i - E(y_i \mid \theta)]^2}{Var(y_i \mid \theta)}.$$

*(The booklet writes $y$ and $\theta$ with under-tildes to indicate vectors.)*

2. -2 times log likelihood

$$T(y, \theta) = -2\log(P(y \mid \theta)).$$

3. Power divergence measure
   Needs to make cells. Define $O_i$ observed cell counts. $e_i$ expected cell counts.

*[Figure: hand-drawn in the right margin beside this item — a rectangle ruled into a row of cells, with a second partial row beneath, sketching the partition of the sample space into cells.]*

$$T(y, \theta) = \frac{2}{\tau(\tau+1)} \sum_{i=1}^{k} O_i \left[ \left( \frac{O_i}{e_i} \right)^{\tau} - 1 \right]$$

where $\tau = \frac{2}{3}$ and $e_i$ are functions of $\theta$. (Aside $\sum_{i=1}^{n} \frac{(O_i - e_i)^2}{e_i} \sim \chi^2_{n-1}$)

> ✔ Verified: With τ = 2/3, the power-divergence leading constant 2/(τ(τ+1)) equals 9/5.

> ✔ Verified: For multinomial(N, p) counts with k cells, E[Σ (O_i − e_i)²/e_i] = k − 1 exactly, matching the stated χ²_{k−1} degrees of freedom.

Suppose I can repeatedly sample my model,

$$T(y^{rep}, \theta) = \sum_{i=1}^{n} \frac{[y_i^{rep} - E(y_i \mid \theta)]^2}{Var(y_i \mid \theta)}$$

Define

$$BPP = P\left[ T(y^{rep}, \theta) \geq T(y^{obs}, \theta) \mid y^{obs} \right]$$

$$\int \int_{y^{rep}, \theta} P\left[ T(y^{rep}\theta) \geq T(y^{obs}\theta) \mid y^{obs}, y^{rep}, \theta \right] \pi(y^{rep}, \theta \mid y^{obs}) dy^{rep} d\theta$$

$\text{[sic: the commas in } T(y^{rep}\theta) \text{ and } T(y^{obs}\theta) \text{ are omitted in the booklet]}$

$$\pi(y^{rep}, \theta \mid y^{obs}) = \pi(y^{rep} \mid \theta, y^{obs}) \pi(\theta \mid y^{obs})$$

*(a short hand slash crosses the leading $\pi$ on the right-hand side; it is not a clear deletion and the printed symbol is retained)* *[$\pi(y^{rep}\mid\theta, y^{obs})$ is hand-underlined with a wavy line; $\pi(\theta\mid y^{obs})$ is hand-underlined twice]* *[margin note, below the equation: "draw(?) the posterior (samples)"]*

> ✔ Verified: π(y_rep, θ | y_obs) = π(y_rep | θ, y_obs) · π(θ | y_obs) for a concrete discrete joint distribution.

131

### PDF page 137 (booklet page 132)

*Example.*

$$y_1,\dots y_n \mid \mu,\sigma^2 \overset{iid.}{\sim} \mathcal{N}(\mu,\sigma^2)$$

$$\pi(\mu,\sigma^2) \propto \frac{1}{\sigma^2}$$

$$T(y^{obs},\mu,\sigma^2) = \sum_{i=1}^{n} \frac{(y_i^{obs}-\mu)^2}{\sigma^2}$$

$$T(y^{rep},\mu,\sigma^2) = \sum_{i=1}^{n} \frac{(y_i^{rep}-\mu)^2}{\sigma^2}$$

*(The booklet writes $y$ with under-tildes to indicate vectors.)*

Poor Model: $BPP \le 0.05$ or $BPP \ge 0.95$, professor uses $0.1$ and $0.9$ instead of $0.05$ and $0.95$.

**12.1.1 Deviance information criteria ($DIC$)**

Deviance as: $D(y\mid\theta) = -2\log[P(y\mid\theta)]$. Let $\hat{\theta}$ be the posterior mean of $\theta$. Define

$$D_{\hat{\theta}}(y) = D(y\mid\hat{\theta})$$

$$D_{avg}(y) = E_{\theta\mid y}[D(y\mid\theta)\mid y]$$

$$\hat{D}_{avg} = \frac{1}{M}\sum_{n=1}^{M} D(y\mid\theta^{(n)}), \quad M \text{ samples.}$$

*(correction: a hat is added by hand over the printed $D_{avg}$, and a small trailing mark that may read "$(y)$" (?) — the Monte Carlo estimate of $D_{avg}$)*

We define the complexity of the model (effective number of parameters) as,

$$P_D = \hat{D}_{avg}(y) - D_{\hat{\theta}}(y)$$

$$DIC = 2\hat{D}_{avg}(y) - D_{\hat{\theta}}(y)$$

*(correction: in both displays a hat is added by hand over the printed $D_{avg}$)*

> ✔ Verified: With $P_D = \hat D_{avg} - D_{\hat\theta}$, the booklet's $DIC = 2\hat D_{avg} - D_{\hat\theta}$ equals $D_{\hat\theta} + 2P_D$.

Have two or more models, select the one with the smallest $DIC$.

*Example.* SAT scores for student in a number of schools

*[margin note, left, circled: "8 schools" (?)]* *[margin notes, right: "one-way ANOVA" (?); "random model."]*

$$y_{ij}\mid\mu_i,\sigma^2 \;\sim\; \mathcal{N}(\mu_i,\sigma^2)$$

$$\mu_i\mid\theta,\delta^2 \;\sim\; \mathcal{N}(\theta,\delta^2)$$

where $\pi(\theta)=1$, $\sigma^{-2}\sim Gamma(a,b)$, $\delta^{-2}\sim Gamma(c,d)$.

| Model | DIC |
|---|---|
| $\delta^2 = \infty$ | 79.3 |
| $\delta^2 = 0$ | 61.5 $\star$ |
| $\delta^2 =$ unknown | 63.4 |

> ✔ Verified: In the SAT-schools DIC table, the minimum DIC is 61.5, attained at $\delta^2 = 0$ (the starred row).

### PDF page 138 (booklet page 133)

**12.2 SIR algorithm**

$\pi(\theta\mid x)$: in a multiparameter problem, it may be difficult to draw samples from $\pi(\theta\mid x)$.

*(The booklet writes $\theta$ and $x$ with under-tildes to indicate vectors.)*

Approximate $\pi(\theta\mid x)$ by $\pi_a(\theta\mid x)$, where it is easy to draw samples from $\pi_a(\theta\mid x)$.

$$\pi(\theta_1,\theta_2\mid x) = \pi(\theta_2\mid \theta_1, x)\,\pi(\theta_1\mid x)$$

$$\pi_a(\theta_1,\theta_2\mid x) = \pi_a(\theta_2\mid \theta_1, x)\,\pi(\theta_1\mid x)$$

> ⚠ Check FAILED: The chain rule $\pi(\theta_1,\theta_2\mid x)=\pi(\theta_2\mid\theta_1,x)\,\pi(\theta_1\mid x)$ holds — verified on an exact bivariate example where the conditional and marginal are computed from the joint by definition. — the stated result did not reproduce (see verification log)

Require

$$\frac{\pi(\theta\mid x)}{\pi_a(\theta\mid x)} \le H < \infty$$

$$\pi_a(\theta\mid x) = \begin{cases} \text{importance function or} \\ \text{proporal [sic] density or} \\ \text{candidate generating density} \end{cases}$$

Draw a large sample from $\pi_a(\theta_1,\theta_2\mid x)$, we have $\theta_1,\dots\theta_M$. Take a sample of $\theta_1,\dots\theta_M$ (subsampling) without replacement.

Subsample the $\theta_1,\dots\theta_M$ using weights: *(correction: the "e" in the typeset "weightes" is struck through by hand, giving "weights")*

$$w_h \propto \frac{\pi(\theta_h\mid x)}{\pi_a(\theta_h\mid x)},\; h = 1,\dots,M$$

$$w_h = \frac{\dfrac{\pi(\theta_h\mid x)}{\pi_a(\theta_h\mid x)}}{\sum_{h=1}^{M} \dfrac{\pi(\theta_h\mid x)}{\pi_a(\theta_h\mid x)}},\; h = 1,\dots,M.$$

> ✔ Verified: The normalized SIR weights $w_h = \frac{\pi(\theta_h\mid x)/\pi_a(\theta_h\mid x)}{\sum_{k=1}^{M}\pi(\theta_k\mid x)/\pi_a(\theta_k\mid x)}$ are proportional to the importance ratios $\pi(\theta_h\mid x)/\pi_a(\theta_h\mid x)$ and sum to one.

See Figure 1.

*[Figure 12.1: three roughly horizontal, slightly tilted lines spanning the width of the plot, labelled on the left axis from top to bottom $\frac{10}{M}$, $\frac{1}{M}$, and $\frac{1}{10M}$. Scattered dots lie between and around the lines. An arrow from the label "weights" (top) points to one of the dots; a second arrow from the label "bands" (bottom) points to the lines. A long line runs diagonally from upper right to lower left across the plot.]*

Figure 12.1: Subsample using weights

Needs the weights to be within these bands.

Need anbut [sic] 10% subsampling.

### PDF page 139 (booklet page 134)

*Example.* If we need $1{,}000$, we must draw $10{,}000$ to subsample

| $\theta$ | weight | cumulative probability |
|---|---|---|
| $\theta_1$ | $w_1$ | $w_1$ |
| $\theta_2$ | $w_2$ | $w_1 + w_2$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $\theta_M$ | $w_M$ | $1$ |

Two cautions:

1. Without replacement

2. Each $w_h$ has to be within some range.

**12.3 Slice sampling**

Slice sampler is a technique used to avoid rejection sampling. Slice sampler is actually a Gibbs sampler.
No normalization constant is needed.

*1. Damien et.al JRSSR [sic] 1999.  2. Neal (2003, AS)*

**example**

(1)

$$f(x) \propto e^{-\frac{1}{2}x^2}, \quad -\infty < x < +\infty$$

Introduce a hidden variable (latent variable),

$$f(x,u) \propto I\left(u < e^{-\frac{1}{2}x^2}\right), \quad u \sim U(0,1)$$

> ⚠ Check FAILED: Integrating $I(u < e^{-x^2/2})$ over $u \in (0,1)$ yields $e^{-x^2/2}$, recovering the target marginal. — the stated result did not reproduce (see verification log)

$$u \mid x \sim U\left(0, e^{-\frac{1}{2}x^2}\right)$$

$$x \mid u \sim U\left(x : u < e^{-\frac{1}{2}x^2}\right)$$

$$\ln(u) < -\frac{1}{2}x^2, \quad -2\ln u > x^2, \quad |x| < \sqrt{-2\ln u}$$

> ✔ Verified: For $0 < u < 1$, $\{x : u < e^{-x^2/2}\} = \{x : |x| < \sqrt{-2\ln u}\}$.

Therefore,

$$x \mid u \sim U(-\sqrt{-2\ln u}, +\sqrt{-2\ln u}) \tag{2}$$

Run (1) and (2)

*[Handwritten work filling the entire right margin, dark pen, partly legible. Reading top to bottom: "Bayesian Bootstrap"; then $y_1, \ldots, y_m$ (subscript may be $n$); then $y_1^* \ldots y_k^*$ over $n_1 \ldots n_k$; then $\underset{\sim}{n} \sim \text{Mult}(m, \underset{\sim}{p})$; then $\underset{\sim}{p} \sim \text{Dir}(\underset{\sim}{n})$, beneath which a long horizontal rule is drawn across the margin. Below the rule: $\underset{\sim}{\ell}(?) \sim \text{Dir}(\underset{\sim}{1})$; $\underset{\sim}{n} \sim \text{Mult}(m, \underset{\sim}{p})$; then two [illegible] words; then "New(?) $\text{Mult}(N, \underset{\sim}{p})$" with "sample"(?) written under it; then $\sum_{j=1}^{k} n_j\, y_j^*$; then $\sum \bar{n}_j$ closed by a large hand-drawn bracket that sweeps up through the lines above. At the far right edge: "projection methods", and below it "predictable(?)", "(1) one draw(?)", "also". These are lecture scratch notes on the Bayesian bootstrap — distinct data values $y_j^*$ with multiplicities $n_j$, the Dirichlet–multinomial weight construction, and the resampled mean $\sum_j n_j y_j^*$ — and are unrelated to the printed slice-sampling material they sit beside.]*

*(The booklet writes $n$ and $p$ with under-tildes in these notes to indicate vectors.)*

### PDF page 140 (booklet page 135)

(2)

$$f(x) \propto e^{-\frac{1}{2}x^2}\,\frac{e^x}{(1+e^x)^2},\; -\infty < x < \infty$$

$$f(x,\mu_1,\mu_2) \propto I\!\left(\mu_1 < e^{-\frac{1}{2}x^2}\right) I\left(\mu_1(?) < \frac{e^x}{(1+e^x)^2}\right)$$

*(sic: the second indicator appears to be printed with subscript $\mu_1$; on the evidence of the three conditionals that follow it should read $\mu_2$. The subscript is small in the scan, hence the `(?)`.)*

$$\mu_1 \mid x,\mu_2 \sim U\!\left(0, e^{-\frac{1}{2}x^2}\right)$$

$$\mu_2 \mid x,\mu_1 \sim U\left(0, \frac{e^x}{(1+e^x)^2}\right)$$

$$x \mid \mu_1,\mu_2 \sim U\left(x : \mu_1 < e^{-\frac{1}{2}x^2} \text{ and } \mu_2 < \frac{e^x}{(1+e^x)^2}\right)$$

> ✔ Verified: Marginalizing the slice-sampler augmentation over $\mu_1,\mu_2$ returns the target kernel $e^{-x^2/2}e^x/(1+e^x)^2$.

> ✔ Verified: The full conditionals of the augmented joint are $U(0,e^{-x^2/2})$ and $U(0,e^x/(1+e^x)^2)$.

**Remarks:**

(1) Have a Gibbs sampler with one or more nonstandard CPD's. We can use one of the following techniques:

&nbsp;&nbsp;&nbsp;&nbsp;(a) Accept-reject

&nbsp;&nbsp;&nbsp;&nbsp;(b) Grid method

&nbsp;&nbsp;&nbsp;&nbsp;(c) Metropolis sampler

&nbsp;&nbsp;&nbsp;&nbsp;(d) Slice sampler

&nbsp;&nbsp;&nbsp;&nbsp;(e) SIR algorithm

(2) Product of kernels principle. This allows us to draw an iterate within a Gibbs sampler with running out each component until convergence.

$$a_{12} = \min\left\{ \frac{\dfrac{\pi(\theta_2 \mid x)}{\pi_a(\theta_2 \mid x)}}{\dfrac{\pi(\theta_1 \mid x)}{\pi_a(\theta_1 \mid x)}},\, 1 \right\}$$

*(The booklet writes $x$, $\theta$, $u$, $y$, $\phi$ with under-tildes to indicate vectors.)*

draw $\theta_2 \sim \pi_a(\theta \mid x)$ if $u < a_{12}$. Keep $\theta_2$ otherwise reject $\theta_2$, keep drawing, it will converge, but we do not need to. Professor may run up to 100 times.

## 12.4 INLA

We have a posterior density $\pi(u,\theta,\phi \mid y)$, $u$ is a long vector, length $\approx 10^6$. $\theta,\phi$ relatively very short.

$$\pi(u,\theta,\phi \mid y) = \pi(u \mid \theta,\phi,y)\,\pi(\theta \mid \phi,y)\,\pi(\phi \mid y)$$

$$= \left[\prod_{i=1}^{\ell} \pi(u_i \mid \theta,\phi,y)\right] \pi(\theta \mid \phi,y)\,\pi(\phi \mid y)$$

> ✔ Verified: $\pi(u,\theta,\phi\mid y)=\pi(u\mid\theta,\phi,y)\pi(\theta\mid\phi,y)\pi(\phi\mid y)$ holds exactly (chain rule) on an arbitrary discrete joint.

### PDF page 141 (booklet page 136)

Given $\theta, \phi, y$, $\mu_1, \dots \mu_\ell$ are independent. $\mu_i$ and $\theta$ are normal-like variables, $\phi$ not normal-like

$$\pi_a(u, \theta, \phi \mid y) = \pi_a(u \mid \theta, \phi, y)\,\pi_a(\theta \mid \phi, y)\,\pi_a(\phi \mid y)$$

$$\int_u \int_\theta \pi(u, \theta, \phi \mid y) = \pi_a(\phi \mid u) \quad \text{[sic: the conditioning variable should be } y\text{, and the differentials } du\,d\theta \text{ are omitted]}$$

Assuming $\phi$ is univariate,

$$\pi_a(\phi_h, \mid y) = \frac{w_h g(\phi_h)}{\sum_{h=1}^{100} w_h g(\phi_h)}, h = 1, \dots, 100 \quad \text{[sic: stray comma before the conditioning bar]}$$

Have grids of widths $w_h$ for $\phi$.

*Example.*

$$y_{ij} \mid v_i \overset{iid.}{\sim} Ber\left(\frac{e^{v_i}}{1 + e^{v_i}}\right)$$

$$v_i \mid \theta, \delta^2 \sim \mathcal{N}(\theta, \delta^2)$$

$$\pi(\theta, \delta^2)$$

$$\pi(v, \theta, \delta^2 \mid y) \propto \prod_i \prod_j \left(\frac{e^{v_i}}{1 + e^{v_i}}\right)^{y_{ij}} \left(\frac{1}{1 + e^{v_i}}\right)^{1 - y_{ij}} \prod_i \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(v_i - \theta)^2} \times \pi(\theta, \delta^2)$$

$$= \prod_{i=1}^{l} \left\{ \left(\frac{e^{v_i}}{1 + e^{v_i}}\right)^{s_i} \left(\frac{1}{1 + e^{v_i}}\right)^{n_i - s_i} \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(v_i - \theta)^2} \right\} \times \pi(\theta, \delta^2)$$

> ✔ Verified: The Bernoulli likelihood product over $j$ collapses: $\prod_{j=1}^{n_i} p^{y_{ij}}(1-p)^{1-y_{ij}} = p^{s_i}(1-p)^{n_i-s_i}$ where $s_i=\sum_j y_{ij}$, $p=e^{v_i}/(1+e^{v_i})$.

**12.5 Multinomial-Dirichlet model**

Perform $n$ identical independent trials.

$$n \mid \theta \sim \text{Multinomial}(n, \theta)$$

$$f(n \mid \theta) = \frac{n!}{\prod_{i=1}^{k} n_i!} \prod_{i=1}^{k} \theta_i^{n_i} \text{ where } n_i \geq 0, n = \sum_{i=1}^{k} n_i$$

*Example.*

| Candidate | | |
|---|---|---|
| Bush | 727 | $\theta_1$ |
| Dukakis | 583 | $\theta_2$ |
| others | 137 | $\theta_3$ |
| | 1447 | |

> ✔ Verified: The candidate counts 727, 583, 137 sum to the printed total 1447.

### PDF page 142 (booklet page 137)

$$y \mid \theta \sim \text{Mult}(1447, \theta)$$

*(The booklet writes $y$, $\theta$, $\alpha$, $n$ with under-tildes to indicate vectors.)*

Put a prior on $\theta$

$$\theta \sim \text{Dirichlet}(\alpha), \quad \alpha_1, \dots \alpha_k \text{ specified.}$$

$$\pi(\theta) = \frac{\prod_{i=1}^{k} \theta_i^{\alpha_i - 1}}{D(\alpha)}, \quad \theta_i \geq 0, \sum_{i=1}^{k} \theta_i = 1$$

$$D(\alpha) = \frac{\prod_{i=1}^{k} \Gamma(\alpha_i)}{\Gamma\left(\sum_{i=1}^{k} \alpha_i\right)}$$

$$\pi(\theta \mid n) \propto \prod_{i=1}^{k} \theta_i^{n_i} \prod_{i=1}^{k} \theta_i^{\alpha_i - 1} = \prod_{i=1}^{k} \theta_i^{n_i + \alpha_i - 1}$$

$$\theta \mid n \sim Dir(\alpha + n)$$

> ✔ Verified: The Dirichlet–multinomial posterior kernel $\prod_i \theta_i^{n_i+\alpha_i-1}$ normalizes to $D(\alpha+n)$, i.e. $\theta\mid n \sim Dir(\alpha+n)$.

(1) Take $\alpha_i = 1$, uniform prior

$$\theta \sim Dir(1, ..., 1).$$

(2) Jeffrey's Prior

$$\pi(\theta) \propto \frac{1}{\sqrt{\theta_1 \theta_2 ... \theta_k}}$$

$$\theta \sim Dir\left(\frac{1}{2}, ..., \frac{1}{2}\right)$$

$$\theta \sim Dir(\alpha)$$

$$cov(\theta_i, \theta_j) = -\frac{\alpha_i \alpha_j}{\left(\sum_{j=1}^{k} \alpha_j\right)^2 \left(\sum_{j=1}^{k} \alpha_j + 1\right)}$$

> ✔ Verified: For $\theta \sim Dir(\alpha)$, $cov(\theta_i,\theta_j) = -\alpha_i\alpha_j/(\alpha_0^2(\alpha_0+1))$.

$$\theta_j \sim Beta\left(\alpha_j, \sum_{i \neq j} \alpha_i\right), j = 1, ..., k$$

> ✔ Verified: The marginal of $\theta_1$ under $Dir(\alpha)$ is $Beta(\alpha_1, \sum_{i\neq 1}\alpha_i)$.

Let's say $\theta_j \sim Beta(a, b)$,

$$E(\theta_j) = \frac{a}{a + b}, Var(\theta_j) = \frac{a}{(a+b)^2 (a+b+1)}$$

> ⚠ Check FAILED: For $\theta_j \sim Beta(a,b)$, $E(\theta_j) = a/(a+b)$. — the stated result did not reproduce (see verification log)

> ⚠ Check FAILED: The printed variance is a typo — the true $Beta(a,b)$ variance is $ab/((a+b)^2(a+b+1))$, which differs from the printed $a/((a+b)^2(a+b+1))$. — the stated result did not reproduce (see verification log)

$\text{[sic: the numerator of } Var(\theta_j) \text{ should be } ab \text{, not } a\text{]}$

If $X_j \overset{ind.}{\sim} Gamma(\alpha_j, 1)$, then

$$\left(\frac{X_1}{\sum_{j=1}^{k} X_j}, \frac{X_2}{\sum_{j=1}^{k} X_j}, \cdots, \frac{X_k}{\sum_{j=1}^{k} X_j}\right) \sim Dir(\alpha)$$

> ✔ Verified: Independent $Gamma(\alpha_j,1)$ variates normalized by their sum are $Dir(\alpha)$ (checked at $k=2$, where $Dir$ reduces to $Beta$).

### PDF page 143 (booklet page 138)

*(Blank page — running header only.)*

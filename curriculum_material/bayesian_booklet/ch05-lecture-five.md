# Chapter 5 — Lecture Five
*(PDF pages 46–59; booklet pages 41–54)*


### PDF page 46 (booklet page 41)

# Chapter 5 — Lecture Five

**5.1 Regression**

*[Handwritten work filling the upper-right of the page, in the instructor's hand, partly legible. Best-effort reading, working down the block:*

*$\left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} e^{-\frac{1}{2\sigma^2}\sum_i\left(y_i - x_i'\beta\right)^2}$*

*$\ell = -\frac{n}{2}\ln\sigma^2 - \frac{1}{2\sigma^2}\left(y - x'\beta\right)^2$*

*$\frac{d}{d\beta}\ell = \frac{x}{\sigma^2}\left(y - x'\beta\right)$*

*$\frac{d^2}{d\beta^2}\ell = -\frac{x\,x'}{\sigma^2}$*

*$\frac{d^2}{d\beta\,d\sigma^2} \;\dot=\; -\frac{x}{\sigma^{4}\,(?)}\left(y - x'\beta\right)$  — a small stray pen stroke sits just to the left of this line*

*$\frac{d}{d\sigma^2}\ell = -\frac{n}{2\sigma^2}\,(?) + \frac{1}{2(\sigma^2)^2}\left(y - x'\beta\right)^2$  — parts of the right-hand side are struck through*

*$\frac{d^2}{d(\sigma^2)^2} = $ [struck through, illegible] $\;\frac{n}{2}\frac{1}{(\sigma^2)^2} - \frac{1}{(\sigma^2)^3}\left(y - x'\beta\right)^2$  — with a long horizontal rule struck beneath*

*and a trailing fragment reading roughly $-\frac{1}{2}\frac{n}{(\sigma^2)}\,(?) \;=\; -\frac{n}{2\sigma^2}$ [illegible].*

*These are lecture scratch notes deriving the score and observed-information entries for the normal regression likelihood; the exponents on $\sigma$ are inconsistently written and several terms are crossed out.]*

$$y_1,\dots,y_n\mid\mu,\sigma^2 \overset{\text{ind}}{\sim} N\left(\mu,\sigma^2\right)$$

$$\pi\left(\mu,\sigma^2\right) \propto \frac{1}{\sigma^2}$$

$$\frac{\bar{y}-\mu}{s/\sqrt{n}} \sim t_{n-1}$$

> ✔ Verified: With prior $\pi(\mu,\sigma^2)\propto1/\sigma^2$ and iid normal data, $\sum_i(y_i-\mu)^2=(n-1)s^2+n(\bar y-\mu)^2$, and integrating $\sigma^2$ out of the joint posterior leaves a marginal for $\mu$ proportional to $(1+t^2/(n-1))^{-n/2}$ with $t=(\bar y-\mu)/(s/\sqrt n)$, i.e. the $t_{n-1}$ kernel.

$$x_i = \begin{pmatrix} 1 \\ x_{1i} \\ x_{2i} \\ \vdots \\ x_{(p-1)i} \end{pmatrix} \quad \text{is p-1 covariates.}$$

*(The booklet writes $x_i$, $y$, $\beta$ with under-tildes to indicate vectors; this is the first occurrence in this chapter.)*

*[margin note, right of this display, hand-underlined: "Exchangeability?"]*

Then,

$$y_i\mid\beta,\sigma^2 \overset{\text{ind}}{\sim} N\left(x_i'\beta,\sigma^2\right), \quad i = 1,\dots,n$$

$$x_i'\beta = \left(1, x_{1i},\dots,x_{(p-1)i}\right) \begin{pmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_{p-1} \end{pmatrix}$$

$$= \beta_0 + \beta_1 x_{1i} + \cdots + \beta_{p-1}x_{(p-1)i}$$

> ✔ Verified: $x_i'\beta=(1,x_{1i},\dots,x_{(p-1)i})(\beta_0,\dots,\beta_{p-1})'=\beta_0+\beta_1x_{1i}+\cdots+\beta_{p-1}x_{(p-1)i}$.

Using Jeffreys' independent priors, *(correction: "Jefferys" is corrected by hand — an "e" is inserted above and the misspelled tail struck out — giving "Jeffreys")*

$$\pi\left(\beta,\sigma^2\right) = \pi(\beta)\,\pi\left(\sigma^2\right),\; \pi(\beta) = 1,\; \pi\left(\sigma^2\right) \propto \frac{1}{\sigma^2}$$

$$\pi(\beta,\sigma^2) \propto \frac{1}{\sigma^2}.$$

$$\pi\left(\beta,\sigma^2\mid y\right) \propto \frac{1}{\sigma^2}\left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} e^{-\frac{1}{2\sigma^2}\sum_{i=1}^{n}\left(y_i - x_i'\beta\right)^2}$$

> ✔ Verified: The joint posterior $\pi(\beta,\sigma^2\mid y)$ is proportional to $\frac{1}{\sigma^2}(2\pi\sigma^2)^{-n/2}\exp\{-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-x_i'\beta)^2\}$, i.e. the prior $1/\sigma^2$ times the product of $n$ independent $N(x_i'\beta,\sigma^2)$ densities.

### PDF page 47 (booklet page 42)

$$X_{n\times p} = \begin{pmatrix} x_1' \\ x_2' \\ \vdots \\ x_n' \end{pmatrix}, \quad \hat{\beta} = (X'X)^{-1}X'y, \quad y = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix}$$

*(The booklet writes $\beta$ and $y$ with under-tildes to indicate vectors.)*

$$\sum_{i=1}^{n}\left(y_i - x_i'\beta\right)^2 = \sum_{i=1}^{n}\left[y_i - x_i'\hat{\beta} - x_i'(\beta - \hat{\beta})\right]^2$$

$$= \sum_{i=1}^{n}\left(y_i - x_i'\hat{\beta}\right)^2 + (\beta - \hat{\beta})'X'X\left(\beta - \hat{\beta}\right)$$

> ✔ Verified: The least-squares decomposition $\sum_i (y_i-x_i'\beta)^2 = \sum_i (y_i-x_i'\hat\beta)^2 + (\beta-\hat\beta)'X'X(\beta-\hat\beta)$ holds when $\hat\beta=(X'X)^{-1}X'y$.

$$\pi(\beta,\sigma^2\mid y) \propto \left(\tfrac{1}{\sigma^2}\right)^{\frac{n}{2}+1} e^{-\frac{1}{2\sigma^2}\left[\sum_{i=1}^{n}\left(y_i - x_i'\hat{\beta}\right)^2 + (\beta-\hat{\beta})'X'X(\beta-\hat{\beta})\right]}$$

$$\pi\left(\beta \mid \sigma^2, y\right) \propto e^{-\frac{1}{2\sigma^2}(\beta-\hat{\beta})'X'X(\beta-\hat{\beta})}$$

$$\beta \mid \sigma^2, y \sim N\left(\hat{\beta}, \sigma^2\left(X'X\right)^{-1}\right)$$

> ✔ Verified: $\exp\left(-\frac{1}{2\sigma^2}(\beta-\hat\beta)'X'X(\beta-\hat\beta)\right)$ is the kernel of $N(\hat\beta,\ \sigma^2(X'X)^{-1})$.

$$\pi\left(\sigma^2 \mid y\right) \propto \left(\tfrac{1}{\sigma^2}\right)^{\frac{n-p}{2}+1} e^{-\frac{1}{2\sigma^2}\sum_{i=1}^{n}\left(y_i - x_i'\hat{\beta}\right)^2}$$

$$\sigma^2 \mid y \sim IG\left(\frac{n-p}{2},\ \frac{\sum_{i=1}^{n}\left(y_i - x_i'\beta\right)^2}{2}\right)$$

*(sic: the scale parameter is written with $\beta$ rather than $\hat{\beta}$; the preceding display uses $\hat{\beta}$.)*

> ✔ Verified: $(\sigma^2)^{-(\frac{n-p}{2}+1)}e^{-S/(2\sigma^2)}$ is the $IG\!\left(\frac{n-p}{2},\frac{S}{2}\right)$ kernel, and the corresponding density is proper.

$$\pi(\beta \mid y) = \int \pi\left(\beta \mid \sigma^2, y\right)\pi\left(\sigma^2 \mid y\right)d\sigma^2 \propto \frac{1}{\left[1 + \frac{(\beta-\hat{\beta})'X'X(\beta-\hat{\beta})}{(n-p)\sum_{i=1}^{n}\frac{\left(y_i - x_i'\hat{\beta}\right)^2}{n-p}}\right]^{\frac{n-p+p}{2}}}$$

> ✔ Verified: Marginalizing $\sigma^2$ out of the joint posterior yields the multivariate-$t$ kernel with exponent $\frac{n-p+p}{2}=\frac{n}{2}$.

Consider multivariate student's t distribution, $t_{p,n-p}$
$T \sim t_{p,\nu}$,

$$f(t) = \frac{\Gamma\left(\frac{\nu+p}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)\left(\pi\nu\Sigma\right)^{\frac{1}{2}}} \cdot \frac{1}{\left[1 + \frac{t'\Sigma^{-1}t}{\nu}\right]^{\frac{\nu+p}{2}}}$$

*(sic: for $p>1$ the normalizing factor should carry the determinant, $|\pi\nu\Sigma|^{1/2}$.)*

> ✔ Verified: For $p=1$ the printed multivariate-$t$ density integrates to 1 over $\mathbb{R}$.

## 5.2 Prediction

Consider prediction of $y_{n+1}$

$$\pi\left(y_{n+1} \mid y\right) = \iint \pi\left(y_{n+1} \mid \beta, \sigma^2, y\right)\pi\left(\beta,\sigma^2 \mid y\right)d\beta\,d\sigma^2$$

### PDF page 48 (booklet page 43)

*[margin note, circled, drawn over the running header: "Non Bayesian" — labelling the two displays below]*

*[margin note, circled, top right: "$y_{n+1}$"]*

$$y_{n+1} = x'_{n+1}\beta + \varepsilon_{n+1}, \quad \varepsilon_{n+1} \sim N\left(0,\sigma^2\right)$$

$$\hat{y}_{n+1} = x'_{n+1}\hat{\beta}$$

*(The booklet writes $\beta$, $y$ and $\hat\beta$ with under-tildes to indicate vectors.)*

*[Handwritten work filling the top right margin, partly legible: "$y_1,\dots,y_n\mid\mu,\sigma^2 \overset{iid}{\sim} N(\mu,\sigma^2)$" (?) ... "$\pi(\mu,\sigma^2\mid y)$" (?) ... then a block of three or four lines completely obliterated by cross-hatching ... "$\mu\mid\sigma^2,\bar{y}\,\sim N\!\left(\bar{y},\frac{\sigma^2}{n}\right)$" ... "$\frac{(n-1)s^2}{\sigma^2}$" (?) ... "$\sim$" ... "$(n-1)s^2$" (?) ... and, on the last line, doubly underlined with an arrow pointing to it, "$t$ distribution". These are lecture scratch notes recalling the conjugate/noninformative normal-model result: the conditional posterior of $\mu$ is normal, the scaled sum of squares is $\chi^2$, and the marginal posterior of $\mu$ is a $t$ distribution. Several intermediate symbols are [illegible].]*

**Example (1)** *(correction: the "(1)" is struck through by hand with two diagonal slashes)*

$$y_1,\ldots,y_n\mid\alpha,\beta \overset{ind}{\sim} \text{Gamma}(\alpha,\beta)$$

We can write down Jeffrey's [sic] prior for $\alpha$ and $\beta$

$$\pi(\alpha,\beta) = \frac{1}{\beta}\cdot\frac{1}{(1+\alpha)^2}$$

$$\pi(\alpha,\beta) \propto \frac{1}{\beta}\cdot\sqrt{\alpha\psi'(\alpha)+1} \quad \text{[sic: should be } \sqrt{\alpha\psi'(\alpha)-1}\text{]}$$

*[sic: the printed $+1$ under the root is wrong — the Fisher information determinant is $\det I(\alpha,\beta) = \big(\alpha\psi'(\alpha)-1\big)/\beta^2$, so Jeffreys' prior is $\frac{1}{\beta}\sqrt{\alpha\psi'(\alpha)-1}$.]*

$$\frac{d}{d\alpha}\ln\Gamma(\alpha) = \psi(\alpha), \qquad \frac{d^2}{d\alpha^2}\ln\Gamma(\alpha) = \psi'(\alpha)$$

*[the $\pi(\alpha,\beta)\propto$ line together with the two $\psi$ definitions are enclosed in one large hand-drawn oval]*

> ⚠ Check FAILED: Jeffreys' prior for the rate-parametrized Gamma(α,β) equals (1/β)·sqrt(α ψ'(α) + 1) as printed on the page. — the stated result did not reproduce (see verification log)

$$\pi\left(\alpha,\beta\mid y\right) \propto \prod_{i=1}^{n}\left\{\frac{\beta^{\alpha}y_i^{\alpha-1}e^{-\beta y_i}}{\Gamma(\alpha)}\right\}\frac{1}{\beta}\cdot\frac{1}{(1+\alpha)^2}$$

$$= \frac{\beta^{n\alpha-1}g^{n(\alpha-1)}e^{-n\beta\bar{y}}}{(\Gamma(\alpha))^n}\cdot\frac{1}{(1+\alpha)^2}$$

*[margin note, right of this display: "$g=\left[\prod_{i=1}^{n} y_i\right]^{1/n}$"]*

> ✔ Verified: the product over i collapses to β^(nα−1) g^(n(α−1)) e^(−nβȳ)/Γ(α)^n · 1/(1+α)^2 with g the geometric mean and ȳ the arithmetic mean.

**Example (2)** *(correction: "Exa" and the "(2)" are struck through by hand with diagonal slashes)*

$$\beta\mid\alpha,y \sim \text{Gamma}(n\alpha, n\bar{y})$$

$$\sim \chi^2(2n\alpha, 2n\bar{y})$$

> ✔ Verified: the β-kernel β^(nα−1) e^(−nȳβ) of the joint posterior normalizes to the Gamma(nα, nȳ) density (rate parametrization).

> ✔ Verified: if β ~ Gamma(nα, nȳ) with rate nȳ, then 2nȳβ ~ chi-square with 2nα degrees of freedom.

$$\pi(\alpha\mid y) \propto \frac{g^{n(\alpha-1)}}{(1+\alpha)^2(\Gamma(\alpha))^n}\int_0^{\infty}\beta^{n\alpha-1}e^{-n\bar{y}\beta}\,d\beta$$

$$= \frac{\beta^{n\alpha-1}g^{n(\alpha-1)}e^{-n\beta\bar{y}}}{(\Gamma(\alpha))^n}\cdot\frac{1}{(1+\alpha)^2}$$

*[sic: this second line simply repeats the joint posterior of Example (1) — it still contains $\beta$, which has just been integrated out. The intended right-hand side is $\dfrac{g^{n(\alpha-1)}\Gamma(n\alpha)}{(1+\alpha)^2(\Gamma(\alpha))^n (n\bar y)^{n\alpha}}$.]*

> ✔ Verified: the gamma integral evaluates to Γ(nα)/(nȳ)^(nα).

We can use grid method to draw $\alpha$, $(\phi = \frac{1}{1+\alpha})$

$$\pi\left(\phi\mid y\right) \propto \left[\frac{g^{\alpha-1}}{\Gamma(\alpha)(n\bar{y})^{2}}\right]^{n}\cdot\Gamma(n\alpha) \propto \frac{1-\phi}{\phi}$$

*[the exponent on $(n\bar y)$ is ambiguous in the scan; it is written as "$2$" (?) but must be $\alpha$ for the bracket raised to the $n$th power to reproduce the $(n\bar y)^{n\alpha}$ from the integral above. The trailing "$\propto\frac{1-\phi}{\phi}$" records the substitution $\alpha=\frac{1-\phi}{\phi}$.]*

> ✔ Verified: under φ = 1/(1+α) one has α = (1−φ)/φ, and (1+α)^(−2) times the Jacobian |dα/dφ| equals 1.

Have a sample from $\pi(\beta|y)$

$$\pi(\beta,\alpha\mid y) = \pi(\beta\mid\alpha,y)\pi(\alpha\mid y)$$

Interest in $\beta$

$$\pi\left(\beta\mid y\right) = \int \pi(\beta\mid\alpha,y)\pi(\alpha\mid y)\,d\alpha$$

*[Handwritten work in the lower right margin, two lines heavily struck through with long diagonal strokes and largely illegible: fragments resembling "$\pi(\ldots)$", "$\pi(\beta\mid\ldots)$" and a trailing "$\ldots\mid y)$" can be made out; the rest is [illegible]. Apparently an abandoned alternative to estimator (1) below.]*

$(1)\ \pi(\beta|y) = \frac{1}{M}\sum_{h=1}^{M}\pi\left(\beta\mid\alpha_h, y\right)$

Rao-Blackwellized density estimator of $\beta$ *[this phrase is underlined by hand with a wavy line]*

### PDF page 49 (booklet page 44)

(2)Use histogram and density function in R.

$$E(\beta|y) = \frac{1}{M} \sum_{n=1}^{M} E\left(\beta \mid \alpha_n, y\right)$$

**5.3 Marginal Likelihood**

Rank marginal likelihoods for different models (Bayes factor later)

$$x \mid \theta \;\sim\; f(x \mid \theta)$$

$$\pi(\theta) \quad \text{proper prior}$$

$$f(x) = \int f(x \mid \theta) \pi(\theta) d\theta$$

Example(1):

$$x_1, ..., x_n \mid \mu, \sigma^2 \overset{iid}{\sim} N(\mu, \sigma^2)$$

$$\text{Prior for } \theta, \pi(\theta) \text{ is proper.}$$

$$f(x) = \int f(x \mid \theta) \pi(\theta) d\theta \;\text{ is the marginal likelihood.}$$

Computation is done using Monte Carlo methods

$$\widehat{f(x)} = \frac{1}{M} \sum_{h=1}^{n} f(x \mid \theta_h) \quad \text{[sic: the upper limit should be } M\text{, matching the } \tfrac{1}{M} \text{ factor]}$$

> ✔ Verified: The Monte Carlo estimator averages $f(x\mid\theta_h)$ over prior draws, and $E_\pi[f(x\mid\theta)] = f(x) = \int f(x\mid\theta)\pi(\theta)d\theta$; for $x\mid\theta\sim N(\theta,1)$, $\theta\sim N(0,1)$ this marginal is the $N(0,2)$ density.

In general,

$$f(x) = \int f(x \mid \theta)\pi(\theta) d\theta = \frac{\displaystyle\int f(x\mid\theta)\frac{\pi(\theta)}{g(\theta)} g(\theta) d\theta}{\displaystyle\int \frac{\pi(\theta)}{g(\theta)} g(\theta) d\theta}, g(\theta) \text{ is a proposal density.}$$

> ✔ Verified: Importance-sampling identity: $\int f(x\mid\theta)\pi(\theta)d\theta = \dfrac{\int f(x\mid\theta)\frac{\pi(\theta)}{g(\theta)}g(\theta)d\theta}{\int \frac{\pi(\theta)}{g(\theta)}g(\theta)d\theta}$, with the denominator equal to 1 since $\pi$ is proper.

So

$$\widehat{f(x)} = \frac{\frac{1}{M}\sum_{h=1}^{M} f(x \mid \theta_h)\frac{\pi(\theta_h)}{g(\theta_h)}}{\frac{1}{M}\sum_{h=1}^{M} \frac{\pi(\theta_h)}{g(\theta_h)}} = \sum_{h=1}^{M} w_h f(x \mid \theta_h)$$

> ✔ Verified: The self-normalized estimator equals $\sum_h w_h f(x\mid\theta_h)$ with $w_h$ the normalized importance ratios, and $\sum_h w_h = 1$.

But another method can be done with the basic marginal likelihood identity.

$$\pi(\theta \mid x) = \frac{f(x \mid \theta)\pi(\theta)}{f(x)}$$

> ✔ Verified: The basic marginal likelihood identity $\pi(\theta\mid x) = f(x\mid\theta)\pi(\theta)/f(x)$ yields a proper density; in the conjugate normal example it is $N(x/2, 1/2)$.

### PDF page 50 (booklet page 45)

$$f(x) = \frac{f(x\mid\theta)\pi(\theta)}{\pi(\theta\mid x)}\;\text{— Basic marginal likelihood identity.}$$

*(The booklet writes $x$ and $\theta$ with under-tildes to indicate vectors.)*

Example(2):

$$x\mid p \sim \text{Bin}(n,p)$$

$$p \sim U(0,1)$$

$$
\begin{aligned}
f(x) &= \int_0^1 \binom{n}{x} p^x (1-p)^{n-x} dp \\
&= \binom{n}{x} B(x+1, n-x+1) \\
&= \frac{n!}{x!(n-x)!} \cdot \frac{x!(n-x)!}{(n+1)!} \\
&= \frac{1}{n+1}, \quad x = 0, 1, \ldots, n
\end{aligned}
$$

> ✔ Verified: The binomial–uniform marginal integral equals the binomial coefficient times the Beta function.

> ✔ Verified: The factorial cancellation gives 1/(n+1) for every x = 0,...,n.

*[margin note, to the right of this block: "$\int f(x\mid\theta)\,\pi(\theta)\,d\theta$" (the parameter symbol is cursive; possibly $\lambda$ (?))]*

Example(3):

$$x_1, \ldots, x_n \mid \mu \overset{iid}{\sim} N\left(\mu, \sigma^2\right)$$

$$\mu \sim N\left(\theta, \delta^2\right), \quad \theta, \delta^2, \sigma^2 \text{ are known}$$

$$
\begin{aligned}
&\int \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} e^{-\frac{(n-1)s^2}{2\sigma^2}} \, e^{-\frac{n(\mu-\bar{x})^2}{2\sigma^2}} \cdot \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(\mu-\theta)^2} d\mu \\
\neq\;& \int_{-\infty}^{+\infty} e^{-\frac{n}{2\sigma^2}(\mu-\bar{x})^2 - \frac{1}{2\delta^2}(\mu-\theta)^2} d\mu \\
\neq\;& \int_{-\infty}^{+\infty} e^{-\frac{1}{2(1-\lambda)\delta^2}\left[\mu - (\lambda\bar{x} + (1-\lambda)\theta)\right]^2 - \frac{\lambda}{2\delta^2}(\bar{x}-\theta)^2} d\mu
\end{aligned}
$$

*(correction: the printed "$=$" beginning the second and the third displayed lines are each slashed through by hand into "$\neq$" — the normalizing constants have been dropped)*

*[margin note, left of this display: "Can't drop constant out"]*

*[a hand-drawn "$\times$" sits to the right of the second line's $d\mu$, and a long wavy hand underline runs beneath the Gaussian kernel $e^{-\frac{1}{2(1-\lambda)\delta^2}[\mu-(\lambda\bar{x}+(1-\lambda)\theta)]^2}$ in the third line]*

*[Handwritten work in the right margin, reassembling the constants that were dropped: $\left(\frac{1}{2\pi\sigma^2}\right)^{n/2}$ ... $\frac{1}{\sqrt{2\pi\delta^2}}$ ... $e^{-\frac{(n-1)s^2}{2\sigma^2}}$ ... $e^{-\frac{\lambda}{2\delta^2}(\bar{x}-\theta)^2}$ ... $\sqrt{2\pi(1-\lambda)\delta^2}$. Taken together with the "$\times$" and the wavy underline, these are the factors of $f(x)$: the constants pulled out front, the $(\bar{x}-\theta)^2$ term that does not depend on $\mu$, and the value of the remaining Gaussian $\mu$-integral.]*

> ✔ Verified: Completing the square in mu with lambda = n*delta^2/(sigma^2 + n*delta^2).

> ✔ Verified: The Gaussian kernel integrates to sqrt(2*pi*(1-lambda)*delta^2).

> ✔ Verified: The marginal f(x) equals the product of factors reassembled in the right margin.

## 5.4 Big idea

Have $\pi(\theta\mid x)$, interest in $\pi(\theta_1\mid x)$.

$$\pi(\theta_1\mid x) = \int \ldots \int \pi(\theta_1, \ldots, \theta_{10000}\mid x)\, d\theta_2 \ldots d\theta_{10000}$$

Have a sample from the joint posterior density of $\theta_1, \ldots, \theta_{10000}$. A sample from the posterior density of $\theta_1$ is $\theta_{11}, \ldots, \theta_{1M}$ and so on.

### PDF page 51 (booklet page 46)

| Sample | $\theta_1$ | $\theta_2$ | ... | $\theta_{10000}$ |
|---|---|---|---|---|
| 1 | $\theta_{11}$ | | | |
| 2 | $\theta_{12}$ | | | |
| . | . | | | |
| . | . | | | |
| . | . | | | |
| $M$ | $\theta_{1M}$ | | | |

*(Only the $\theta_1$ column is filled in; the remaining columns are left blank in the booklet. The table is continued from the preceding page.)*

**5.5 Numerical Integrations**

Gaussian quadrature
Orthogonal polynomial

$$\int h(x)f(x)dx \approx \sum_{k=1}^{n} w_k f(x_k)$$

$$w_1, ..., w_n \text{ are weights}$$

$$x_1, ..., x_n \text{ are roots, where } n \text{ is the number of roots.}$$

A specific type of integral gives rise to a specific orthogonal polynomial.
Typically choose: $n = 25, 50, 75, 100$.
1) Legendre polynomial

$$\int_a^b f(x)dx \approx \sum_{k=1}^{n} w_k f(x_k)$$

> ✔ Verified: Gauss-Legendre (weight 1 on [a,b]), n=2, is exact for polynomials of degree ≤ 3.

2) Lagnere [sic: Laguerre] polynomial

$$\int_0^\infty x^\alpha e^{-x} f(x)dx \approx \sum_{k=1}^{n} w_k f(x_k)$$

> ✔ Verified: generalized Gauss-Laguerre (weight x^α e^{-x} on [0,∞)), n=2, α=1/2, is exact for polynomials of degree ≤ 3.

3) Hermite polynomial

$$\int_{-\infty}^{\infty} e^{-x^2} f(x)dx \approx \sum_{k=1}^{n} w_k f(x_k)$$

> ✔ Verified: Gauss-Hermite (weight e^{-x^2} on the whole line), n=2, is exact for polynomials of degree ≤ 3.

4) Jacobi polynomial

$$\int_{-1}^{1} (1-x)^\alpha (1+x)^\beta f(x)dx \approx \sum_{k=1}^{n} w_k f(x_k)$$

> ✔ Verified: Gauss-Jacobi (weight (1-x)^α (1+x)^β on [-1,1]), n=2, α=1, β=2, is exact for polynomials of degree ≤ 3.

Better approximations can be obtained using adaptive quadrature.
Double integrals can be obtained:

$$\int \int f(x,y)dxdy = \sum_{k_2=1}^{n_2} w_{k_2} \sum_{k_1=1}^{n_1} w_{k_1} f(x_{k_1}, x_{k_2})$$

*(The booklet writes `=` rather than `\approx` here, unlike the four rules above; and both arguments of $f$ are written as $x$'s — $f(x_{k_1}, x_{k_2})$ — where the second node set belongs to the $y$ variable.)*

> ✔ Verified: the double-integral tensor-product rule is exact for f polynomial of degree ≤ 2n_i-1 in each variable.

### PDF page 52 (booklet page 47)

**5.6 Gibbs Sampler (Brief idea)**

$$y_1,\ldots,y_n \mid \mu,\sigma^2 \sim N\left(\mu,\sigma^2\right)$$

$$\pi\left(\mu,\sigma^2\right) \propto \frac{1}{\sigma^2}$$

$$\pi\left(\mu,\sigma^2 \mid y\right) \propto \left(\tfrac{1}{\sigma^2}\right)^{\frac{n}{2}+1} e^{-\frac{1}{2\sigma^2}\left[(n-1)s^2 + n(\bar{y}-\mu)^2\right]}$$

> ✔ Verified: Likelihood times prior $1/\sigma^2$ gives kernel $(1/\sigma^2)^{n/2+1}\exp\{-\frac{1}{2\sigma^2}[(n-1)s^2+n(\bar y-\mu)^2]\}$; equivalently $\sum(y_i-\mu)^2=(n-1)s^2+n(\bar y-\mu)^2$.

$$\pi\left(\mu \mid \sigma^2, y\right) \propto e^{-\frac{n}{2\sigma^2}(\mu-\bar{y})^2}$$

$$\sigma^2 \mid \mu, y \sim IG\left(\frac{n}{2}, \frac{(n-1)s^2 + n(\bar{y}-\mu)^2}{2}\right)$$

$$\sim I\chi^2\left(n, (n-1)s^2 + n(\bar{y}-\mu)^2\right)$$

> ✔ Verified: As a function of $\sigma^2$ the joint kernel is $IG(n/2, B/2)$ with $B=(n-1)s^2+n(\bar y-\mu)^2$, and $IG(n/2,B/2)$ coincides with the scaled inverse chi-square $I\chi^2(n,B)$.

$$\mu \mid \sigma^2, y \sim N\left(\bar{y}, \frac{\sigma^2}{n}\right)$$

> ✔ Verified: $\exp\{-\frac{n}{2\sigma^2}(\mu-\bar y)^2\}$ is the kernel of $N(\bar y, \sigma^2/n)$.

*(The booklet writes $y$ and $\theta$ with under-tildes to indicate vectors.)*

New method:

Start with $\sigma^2 = s^2$ (a guess)

Iterative procedure, sample $\mu$

Gibbs Sampler: Keep repeating the procedure until convergence *(correction: the printed phrase "until average" is circled and struck through, replaced by handwritten "convergence")*

In general, $\pi(\theta_1, ..., \theta_k \mid y)$

$$\theta_1 \mid \theta_2, \ldots \theta_k, y$$

$$\theta_2 \mid \theta_1, \theta_3, \ldots, \theta_k, y$$

$$\theta_k \mid \theta_1, \ldots, \theta_{k-1}, y$$

Finally, we can get $\theta^{(1)}, \ldots, \theta^{(M)}$

**5.7 Rejection Sampling**

Accept-reject algorithm:

Now standard distribution: $y \;\sim\; f_Y(y)$

Kernel is enough: $y \;\sim\; f_V(y)$

$$M = \sup_y \frac{f_Y(y)}{f_V(y)} < \infty, \; M > 1.$$

### PDF page 53 (booklet page 48)

Algorithm:

*[margin note, top right: "Casella and Berger"]*

a. $V \sim f_V(y)$

b. $U \sim U(0,1)$

c. If $U \le \dfrac{1}{M}\dfrac{f_Y(v)}{f_V(v)}$ accept $v$, let $y = v$, accept. Otherwise, go back to (a).

Notes:

(1) $P(\text{stops}) = \frac{1}{M}$.

(2) The number of trails [sic] needed to get one $y$ is geometric $\left(\frac{1}{M}\right)$.

> ✔ Verified: The number of trials to acceptance is geometric with success probability $1/M$: the pmf sums to 1, $P(N=1) = 1/M = P(\text{stops})$, and $E[N] = M$.

(3) Normalization constant not needed.

Example:

$$\pi(\theta \mid x) \propto \frac{1}{1+\theta}\theta^{a-1}e^{-b\theta},\ \theta > 0$$

*(The booklet writes $x$ with under-tildes to indicate vectors.)*

$$\pi_a(\theta \mid x) \propto \theta^{a-1}e^{-b\theta}$$

$$\frac{\pi(\theta \mid x)}{\pi_a(\theta \mid x)} = \frac{1}{1+\theta} \le 1$$

> ✔ Verified: The kernel ratio $\pi/\pi_a$ equals $1/(1+\theta)$, is bounded by 1 on $\theta>0$, and its supremum is 1.

$$\theta \;\sim\; \pi_a(\theta \mid x)$$

$$U \;\sim\; U(0,1)$$

$$\text{If } U \le \frac{1}{1+\theta}, \text{ take } \theta. \text{ Otherwise go back to (a).}$$

## 5.8 Squeeze Method (Envelope)

*[the word "(Envelope)" in the section header is hand-underlined with a looping double underline]*

$f(x)$ can be costly to compute. Bound $f(x)$ by $h(y)$ (not a density) from below uniformly. So (a) and (b) remain the same but (c) changes as follows:

(c).1 *(handwritten insertion: "Accept $y$ if")*

$$U \le \frac{h(y)}{M f_V(y)}$$

Else (c).2 *(handwritten insertion: "Accept $y$ if")*

$$U \le \frac{f(y)}{M f_V(y)}$$

When it is expensive to get $f(y)$, this method is useful.

*[handwritten note at the bottom of the page: "$f(y)$ — complicated"]*

### PDF page 54 (booklet page 49)

**5.9 Monte Carlo Integration**

Consider the following problem:

$$E[h(x)] = \int_{-\infty}^{\infty} h(x) f(x)\, dx$$

Where $f(x)$ is a density function. We assume that $E[h(x)]$ is finite, otherwise the computation is meaningless.

Suppose we have a large random sample of size $M$ from $f(x)$. That is

$$X_1, ..., X_M \;\underset{\sim}{iid}\; f(x).$$

*(The booklet sets the "$\sim$" underneath "iid" here rather than as $\overset{iid}{\sim}$; transcribed as printed.)*

Then, a Monte Carlo estimator of $E[h(x)]$ is

$$\hat{h}_M = M^{-1} \sum_{i=1}^{M} h(x_i)$$

Observe that by the SLLN,

$$\hat{h}_M \overset{a.s.}{\longrightarrow} E[h(x)]$$

Thus, if $M$ is chosen large enough,

$$E[h(x)] \approx \hat{h}_M$$

Now, if $E[h^2(x)] < \infty,$ then

$$V_M = Var(\hat{h}_M) = \frac{1}{M} \int_{-\infty}^{\infty} [h(x) - E[h(x)]]^2 f(x)\, dx$$

> ✔ Verified: For an iid sample $X_1,\dots,X_M\sim f$, $Var(M^{-1}\sum h(X_i)) = \frac{1}{M}\int_{-\infty}^{\infty}[h(x)-E[h(x)]]^2 f(x)\,dx$.

Thus, an estimator of the variance $V_M$ is $\dfrac{s_M^2}{M}$, where $s_M^2 = \displaystyle\sum_{i=1}^{M} \frac{[h(x_i) - \hat{h}_M]^2}{M-1}$

For large$M$, using the CLT, *[sic: no space between "large" and "$M$"]*

$$\frac{\hat{h}_M - E[h(x)]}{s/\sqrt{M}} \overset{d}{\to} \text{Normal}(0,1) \;\text{ (see later).}$$

> ✔ Verified: If $Var(\hat h_M) = \sigma^2/M$ where $\sigma^2 = Var(h(X))$, then $(\hat h_M - E[h(x)])/(\sigma/\sqrt M)$ has mean 0 and variance 1.

Note that $s/\sqrt{M}$ is the Monte Carlo error in $\hat{h}_M$. An approximate 95% confidence interval for $E[h(x)]$ is

$$\hat{h}_M \pm 2s/\sqrt{M}$$

> ✔ Verified: $\hat h_M \pm 2s/\sqrt M$ is an approximate 95% interval, i.e. the normal coverage of $\pm 2$ standard errors equals 0.95 to two decimal places.

Example

$$x|\theta \;\sim\; N(\theta, 1), \theta \;\sim\; Cauchy(0,1)$$

### PDF page 55 (booklet page 50)

$$f(x,\theta) = \frac{1}{\pi(1+\theta^2)}\frac{1}{\sqrt{2\pi}}e^{-\frac12(x-\theta)^2}$$

$$f(\theta|x) = \frac{\dfrac{1}{\pi(1+\theta^2)}\dfrac{1}{\sqrt{2\pi}}e^{-\frac12(x-\theta)^2}}{\displaystyle\int_{-\infty}^{\infty}\frac{1}{\pi(1+\theta^2)}\frac{1}{\sqrt{2\pi}}e^{-\frac12(x-\theta)^2}d\theta},\; -\infty < \theta < \infty$$

An interesting quantity is

$$E(\theta|x) = \frac{\displaystyle\int_{-\infty}^{\infty}\frac{\theta}{(1+\theta^2)}\frac{1}{\sqrt{2\pi}}e^{-\frac12(x-\theta)^2}d\theta}{\displaystyle\int_{-\infty}^{\infty}\frac{1}{(1+\theta^2)}\frac{1}{\sqrt{2\pi}}e^{-\frac12(x-\theta)^2}d\theta} < \infty$$

> ✔ Verified: For the Cauchy(0,1) prior and N(θ,1) likelihood, both integrals defining E(θ|x) converge and the denominator is strictly positive, so E(θ|x) < ∞.

$$\text{Suppose } \theta_1,...,\theta_M \overset{iid}{\sim} N(x,1)$$

*(The booklet writes the "iid" of $\overset{iid}{\sim}$ with an under-tilde.)*

Then a Monte Carlo estimation of $E(\theta|x)$ is

$$\hat\theta_M = \frac{\sum_{h=1}^{M}\frac{\theta_h}{1+\theta_h^2}}{\sum_{h=1}^{M}\frac{1}{1+\theta_h^2}} = \sum_{h=1}^{M} w_h\theta_h, \text{where } w_h = \frac{\frac{1}{1+\theta_h^2}}{\sum_{h=1}^{M}\frac{1}{1+\theta_h^2}}$$

*[sic: the summation index $h$ is reused in the denominator of $w_h$, where a distinct dummy index is needed.]*

> ✔ Verified: The self-normalized weighted average identity: ratio of sums equals sum of w_h*theta_h, and the weights sum to one.

$$Var(\hat\theta_M) = \frac{s^2}{M}, \text{where } s^2 = \sum_{h=1}^{M} w_h(\theta_h - \hat\theta_M)^2$$

$$\text{Note that } \hat\theta_M \overset{a.s.}{\longrightarrow} E(\theta|x)$$

## 5.10 Importance Sampling

We are now interested in

$$E = \int_{-\infty}^{\infty} h(x)f(x)dx,$$

But now it is not easy to draw a sample from $f(x)$.
Suppose, however, we can get samples from $g(x)$. That is,

$$X_1,...,X_M \overset{iid}{\sim} g(x)$$

Then,

$$E = \int_{-\infty}^{\infty} h(x)\frac{f(x)}{g(x)}g(x)dx,$$

and one MC estimator is

$$\widetilde{E}_M^{(1)} = M^{-1}\sum_{i=1}^{M} h(x_i)\lfloor\frac{f(x_i)}{g(x_i)}\rfloor$$

*[sic: the brackets around the weight are set as $\lfloor\;\rfloor$ in the scan; ordinary square brackets are intended.]*

> ✔ Verified: Importance sampling identity / unbiasedness: E_g[h(X) f(X)/g(X)] = int h(x) f(x) dx.

### PDF page 56 (booklet page 51)

MC error is $s/\sqrt{M}$, where $s^2 = \dfrac{\sum_{i=1}^{M}[h(x_i)\frac{f(x_i)}{g(x_i)} - \widetilde{E}_M^{(1)}]^2}{M-1}$

Again, by the SLLN, $\widetilde{E}_M^{(1)} \overset{a.s.}{\longrightarrow} E$ as $M \longrightarrow \infty$

Choice of $g(x)$.

$g(x)$ must satisfy:

a. $f(x)$ must not dominate $g(x)$ especially in the tails.

$$\sup_x \frac{f(x)}{g(x)} = B,\; \text{[illegible]}\; B < \infty(\ \text{i.e. } g(x) \text{ has heavier tails than } f(x).)$$

*(correction: each printed "$M$" in this line is struck through by hand and replaced by a handwritten "$B$"; a further printed fragment between them — reading "$1/M$"(?) — is struck through with no replacement and is transcribed as `[illegible]`)*

b. Can draw sample from $g(x)$ easily.

$g(x)$ is called an importance function.

Note that

$$Var(\widetilde{E}_M^{(1)}) = \frac{1}{M}\left\{ E_g[\frac{h(x)f(x)}{g(x)}]^2 - [E_g(\frac{h(x)f(x)}{g(x)})]^2 \right\}$$

> ✔ Verified: Var of the M-sample importance-sampling mean equals (1/M){E_g[W^2] − (E_g[W])^2}, W = h·f/g; verified exactly at M=2 with f=Exp(1), g=Exp(1/2), h(x)=x.

So for finite variance

$$
\begin{aligned}
E_g[\frac{h(x)f(x)}{g(x)}]^2 &= \int_{-\infty}^{\infty} [\frac{h(x)f(x)}{g(x)}]^2 g(x)dx \\
&= \int_{-\infty}^{\infty} \frac{h^2(x)f^2(x)}{g(x)}dx \\
&= \int_{-\infty}^{\infty} h^2(x)[\frac{f(x)}{g(x)}]f(x)dx \\
&= E\left\{ h^2(x)[\frac{f(x)}{g(x)}] \right\} < \infty
\end{aligned}
$$

> ✔ Verified: the identity chain ∫[hf/g]^2 g dx = ∫ h^2 f^2/g dx = ∫ h^2 (f/g) f dx = E_f{h^2 (f/g)}, finite when f/g is bounded.

If the ratio $\frac{f(x)}{g(x)}$ is unbounded, $h^2(x)\frac{f(x)}{g(x)}$ will vary too much, making the estimator $\widetilde{E}_M^{(1)}$ inefficient.

We can obtain a slightly better estimator than $\widetilde{E}_M^{(1)}$ by observing the following:

### PDF page 57 (booklet page 52)

$$E = \int_{-\infty}^{\infty} h(x) f(x)\,dx$$

$$= \frac{\int_{-\infty}^{\infty} h(x) f(x)\,dx}{\int_{-\infty}^{\infty} f(x)\,dx}$$

$$= \frac{\int_{-\infty}^{\infty}\left[h(x)\dfrac{f(x)}{g(x)}\right]g(x)\,dx}{\int_{-\infty}^{\infty}\left[\dfrac{f(x)}{g(x)}\right]g(x)\,dx}$$

> ✔ Verified: For a density f and proposal g, ∫h f dx equals [∫ h(f/g) g dx] / [∫ (f/g) g dx].

Now for $X_1, ..., X_M \overset{iid}{\sim} g(x)$, we have a second Monte Carlo estimator:

$$\widetilde{E}_M^{(2)} = \frac{\sum_{i=1}^{M} h(x_i)\dfrac{f(x_i)}{g(x_i)}}{\sum_{i=1}^{M} \dfrac{f(x_i)}{g(x_i)}} = \sum_{i=1}^{M} w(x_i) h(x_i)$$

$$\text{Where } w(x_i) = \frac{\dfrac{f(x_i)}{g(x_i)}}{\sum_{i=1}^{M} \dfrac{f(x_i)}{g(x_i)}}, i = 1, ..., M$$

> ✔ Verified: The self-normalized weights w(x_i) = (f_i/g_i)/Σ_j(f_j/g_j) make Σ_i w_i h_i equal the ratio estimator.

$$\text{And } Var(\widetilde{E}_M^{(2)}) \approx \frac{1}{M}\sum_{i=1}^{M} w(x_i)[h(x_i) - \widetilde{E}_M^{(2)}]^2$$

$\widetilde{E}_M^{(2)}$ may perform better than $\widetilde{E}_M^{(1)}$. See *Casella and Robert (1998, Bionietrika [sic])*. *[a small hand-drawn caret/hook stroke sits above "Robert"(?); no inserted text is legible]* For one thing, the denominator and numerator will be positively correlated, reducing the variance.

**5.11 How to pick the importance (proposal) density**

$$f(x) = \int f(x\mid\theta)\pi(\theta)d\theta = \int \pi^{*}(\theta\mid x)d\theta \qquad \left(\pi^{*}(\theta\mid x) = f(x\mid\theta)\pi(\theta)\right)$$

*(The booklet writes $x$ with under-tildes to indicate vectors.)*

Generally $\quad \pi(\theta\mid x), \quad g(\theta) = \log(\pi(\theta\mid x)), \quad g'(\hat{\theta}) = 0 \quad g''(\hat{\theta}) \leq 0 \quad \text{at } \hat{\theta}$

$$g(\theta) \approx g(\hat{\theta}) + (\theta - \hat{\theta})g'(\hat{\theta}) + \frac{1}{2}(\theta - \hat{\theta})^2 g''(\hat{\theta})$$

$$\pi(\theta\mid x) \overset{\text{approx}}{\propto} e^{\frac{1}{2}(\theta - \hat{\theta})^2 g''(\hat{\theta})} = e^{-\frac{1}{2}(\theta - \hat{\theta})^2 (-g''(\hat{\theta}))}$$

$$\theta\mid x \overset{\text{approx}}{\sim} N\left(\hat{\theta}, -g''(\hat{\theta})^{-1}\right), \quad \hat{\sigma}^2 = \left(-g''(\hat{\theta})\right)^{-1}$$

> ✔ Verified: With g'(θ̂)=0 and g''(θ̂)<0, exp(½(θ-θ̂)²g''(θ̂)) normalizes to N(θ̂, (-g''(θ̂))^{-1}).

### PDF page 58 (booklet page 53)

$$\theta\mid x,\delta^2 \;\overset{\text{approx}}{\sim}\; N\left(\hat{\theta},\delta^2\hat{\sigma}^2\right)$$

$$\frac{v}{\delta^2} \sim \chi^2_v = \text{Gamma}\left(\frac{v}{2},\frac{1}{2}\right), \quad v:\ \text{degree of freedom}$$

> ✔ Verified: $\chi^2_v$ density equals the $\text{Gamma}(v/2,\ \text{rate}\ 1/2)$ density.

$$\pi(\theta\mid x) = \frac{\Gamma\left(\frac{v+1}{2}\right)}{\Gamma\left(\frac{v}{2}\right)}\cdot\frac{1}{\sqrt{\pi v}\,\hat{\sigma}}\;\frac{1}{\left[1+\frac{1}{v}\left(\frac{\theta-\hat{\theta}}{\hat{\sigma}}\right)^2\right]^{\frac{v+1}{2}}}$$

*(In the scan the radical appears to extend over $\hat{\sigma}$ as well; read as $\sqrt{\pi v}\,\hat{\sigma}$, consistent with the $|\pi v\hat{\Sigma}|^{\frac12}$ of the multivariate version below.)*

> ✔ Verified: the normal/chi-square scale mixture $\theta\mid\delta^2\sim N(\hat\theta,\delta^2\hat\sigma^2)$, $v/\delta^2\sim\chi^2_v$ has marginal equal to the printed $t_v$ density $\frac{\Gamma(\frac{v+1}{2})}{\Gamma(\frac{v}{2})\sqrt{\pi v}\,\hat\sigma}\left[1+\frac{1}{v}\left(\frac{\theta-\hat\theta}{\hat\sigma}\right)^2\right]^{-\frac{v+1}{2}}$ (exact check at $v=3$, $\hat\theta=0$, $\hat\sigma=1$).

$v$ is called a tuning constant.
The procedure is more generally called the Laplace approximation or mode-Hessian approximation.

**5.12  Multivariate version**

*(correction: the printed heading reads "Multivariant"; "iant" is struck through by hand and "iate"(?) is written above it — "Multivariate")*

$$\pi(\theta\mid x), \quad g(\theta) = \log(\pi(\theta\mid x))$$

$$g'(\theta) = G(\theta) = 0, \quad g''(\theta) = H(\theta)$$

Hessian matrix $H(\theta)$ must be negative definite.

$$g(\theta) \approx g(\hat{\theta}) + (\theta-\hat{\theta})'G(\hat{\theta}) + \frac{1}{2}(\theta-\hat{\theta})'H(\hat{\theta})(\theta-\hat{\theta})$$

$$\pi(\hat{\theta}\mid x) \propto e^{-\frac{1}{2}(\theta-\hat{\theta})'[-H(\hat{\theta})]^{-1}(\theta-\hat{\theta})}$$

*(The left side is printed $\pi(\hat\theta\mid x)$ where $\pi(\theta\mid x)$ is meant, and the exponent is printed with $[-H(\hat\theta)]^{-1}$ where the quadratic form calls for $[-H(\hat\theta)]$ — both kept as printed [sic].)*

Let $\hat{\Sigma} = [-H(\hat{\theta})]^{-1}$

$$\theta\mid x \sim N\left(\hat{\theta}, [-H(\hat{\theta})]^{-1}\right)$$

$$\theta\mid x,\delta^2 \sim N_p\left(\hat{\theta}, \delta^2\hat{\Sigma}\right)$$

$$\frac{v}{\delta^2} \sim \chi^2_v$$

$$\pi(\theta\mid x) \;\overset{\text{approx}}{=}\; \frac{\Gamma\left(\frac{v+p}{2}\right)}{\Gamma\left(\frac{v}{2}\right)\left|\pi v\hat{\Sigma}\right|^{\frac{1}{2}}}\;\frac{1}{\left[1+\frac{(\theta-\hat{\theta})'\hat{\Sigma}^{-1}(\theta-\hat{\theta})}{v}\right]^{\frac{v+p}{2}}}$$

> ✔ Verified: the multivariate normal/chi-square scale mixture $\theta\mid\delta^2\sim N_p(\hat\theta,\delta^2\hat\Sigma)$, $v/\delta^2\sim\chi^2_v$ has marginal equal to the printed multivariate $t$ density $\frac{\Gamma(\frac{v+p}{2})}{\Gamma(\frac{v}{2})|\pi v\hat\Sigma|^{1/2}}\left[1+\frac{Q}{v}\right]^{-\frac{v+p}{2}}$ with $Q=(\theta-\hat\theta)'\hat\Sigma^{-1}(\theta-\hat\theta)$ (exact check at $p=2$, $v=3$, $\hat\Sigma=I_2$).

Mode-Hessian approximation or Laplace approximation.

### PDF page 59 (booklet page 54)

*(The entire body of this page is handwritten lecture notes; there is no typeset content below the running header. The booklet writes $\beta$, $x_i$, $y$ with under-tildes to indicate vectors.)*

Mention Logistic regression

$$y_1,\dots,y_n \mid \beta \;\overset{ind}{\sim}\; \mathrm{Ber}\!\left(\frac{e^{x_i'\beta}}{1+e^{x_i'\beta}}\right)$$

$$\pi(\beta)\;\propto\;(?)\;1$$

*[margin note, arrow from $\pi(\beta)\propto 1$: "$p$ covariates"; "multiple regression (?)"]*
*[margin notes, far right: "$y_i = 0$ or $1$"; second line [illegible], possibly "categorical"]*
*[margin note, arrow: "$\to$ Jeffreys' prior"]*

$$\pi(\beta\mid y)\;\propto\;\prod_{i=1}^{n}\frac{e^{\,y_i x_i'\beta}}{1+e^{x_i'\beta}}$$

> ✔ Verified: The Bernoulli likelihood with logistic success probability equals $\prod_i e^{y_i x_i'\beta}/(1+e^{x_i'\beta})$.

$$\ell(\beta) \;=\; \left(\sum_{i=1}^{n} y_i x_i'\right)\beta \;-\; \sum_{i=1}^{n}\log\!\left(1+e^{x_i'\beta}\right)$$

> ✔ Verified: $\ell(\beta) = (\sum_i y_i x_i')\beta - \sum_i \log(1+e^{x_i'\beta})$ is the log of $\prod_i e^{y_i x_i'\beta}/(1+e^{x_i'\beta})$.

$$\ell'(\beta) \;=\; \sum_{i=1}^{n} y_i x_i \;-\; \sum \frac{x_i\, e^{x_i'\beta}}{1+e^{x_i'\beta}}$$

> ✔ Verified: $\nabla_\beta \ell(\beta) = \sum_i y_i x_i - \sum_i x_i e^{x_i'\beta}/(1+e^{x_i'\beta})$.

$$\ell''(\beta) \;=\; -\sum_{i=1}^{n} x_i x_i' \,\frac{e^{x_i'\beta}}{\left(1+e^{x_i'\beta}\right)^{2}} \;=\; H$$

*(correction: immediately before "$H$" a symbol is heavily scribbled out, and a second "$=$" sign is written; the surviving reading is "$= H$")*

> ✔ Verified: $\nabla^2_\beta \ell(\beta) = -\sum_i x_i x_i' e^{x_i'\beta}/(1+e^{x_i'\beta})^2 = H$.

*[margin note, right of the derivative block: $X = \begin{pmatrix} x_1' \\ x_2' \\ \vdots \\ x_n'\end{pmatrix}$, annotated "$n\times p$" beneath the "$X =$".]*

$$\beta\mid y \;\sim\; aN\!\left(\hat\beta,\; (-H)^{-1}_{\hat\beta}\right)$$

*[the word "approx" is written by hand beneath the "$\sim$"]*

$$\beta \mid y,\sigma^{2} \;\sim\; aN\!\left(\hat\beta,\; c^{2}\,(-H)^{-1}_{\hat\beta}\right)$$

$$\frac{\nu}{c}\;\sim\;\chi^{2}_{\nu}\quad\text{(?)}$$

*(correction: the "$\chi$" is struck through by hand; the whole line is faint and the reading of $\nu/c$ versus $\nu/c^{2}$ is uncertain)*

*[margin notes, lower right: "$\hat\beta \to$ mode"; "Newton-Raphson"; "Nelder-Mead"]*

$$\sum_{i=1}^{n} y_i x_i \;-\; \sum x_i \left(1+e^{-x_i'\beta}\right)^{-1}$$

$$\approx\; \sum x_i\left(1 - e^{-x_i'\beta}\right)\quad\text{(?)}$$

$$\approx\; \sum x_i x_i'\beta\quad\text{(?)}$$

$$\hat\beta \;=\; (X'X)^{-1}X'y$$

> ✔ Verified: $\hat\beta = (X'X)^{-1}X'y$ satisfies the normal equations $X'(y - X\hat\beta) = 0$.

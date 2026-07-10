# Chapter 3 — Lecture Three
*(PDF pages 22–39; booklet pages 17–34)*


### PDF page 22 (booklet page 17)

# Chapter 3 — Lecture Three

**Two points**
1. Updating priors.
2. Monte Carlo method.

**How to construct priors?**

Mathematical Model:
Have a prior $\pi(\theta)$.
Have some data $f(x\mid \theta)$.
$$\pi(\theta\mid x) \propto f(x\mid \theta)\pi(\theta) \;\text{— Bayes' theorem.}$$

Want to study future value: prediction or missing value.
This posterior is my prior for all future analyses.
We have $x$, want to study $x^*$.
So $f(x^*\mid x)$ is our interest.
$$f(x^*\mid x) = \int f(x^*\mid \theta, x)\pi(\theta\mid x)d\theta \;\text{— Law of total probability.}$$

Typically, we assume that $x_1, \ldots, x_n, x^*\mid \theta \overset{iid}{\sim} f(x\mid \theta)$, i.e. $x^*\mid \theta$ and $x\mid \theta$ are independent. So
$$f(x^*\mid x) = \int f(x^*\mid \theta)\pi(\theta\mid x)d\theta \;\text{— Bayesian Predictive inference.}$$

**Example (1)**
$$X_1, \ldots, X_n, X_{n+1}\mid \mu \overset{iid}{\sim} N(\mu, \sigma^2)$$
$$\mu \sim N(\theta, \delta^2),\ \theta, \delta^2, \sigma^2 \text{ are known.}$$

### PDF page 23 (booklet page 18)

We have $\mu\mid x \sim N(\lambda\bar{x} + (1-\lambda)\theta, (1-\lambda)\delta^2)$, where $\lambda = \dfrac{\delta^2}{\delta^2 + \frac{\sigma^2}{n}}$.

*(The booklet writes $x$ with an under-tilde to indicate a vector.)*

So,

$$
\begin{aligned}
f(x_{n+1}\mid x) &= \int_{-\infty}^{\infty} f(x_{n+1}\mid x,\mu)\,\pi(\mu\mid x)\,d\mu \\
&= \int_{-\infty}^{\infty} f(x_{n+1}\mid \mu)\,\pi(\mu\mid x)\,d\mu \\
&= \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\sigma^2}}\, e^{-\frac{1}{2\sigma^2}(x_{n+1}-\mu)^2}\, \frac{1}{\sqrt{2\pi(1-\lambda)\delta^2}}\, e^{-\frac{1}{2(1-\lambda)\delta^2}\left[\mu-(\lambda\bar{x}+(1-\lambda)\theta)\right]^2}\, d\mu
\end{aligned}
$$

$f(x_{n+1}\mid x)$ has to be normal.

Simply needs $E(x_{n+1}\mid x)$ and $Var(x_{n+1}\mid x)$.

$$
E(x_{n+1}\mid x) = E_{\mu\mid x}\left[E(x_{n+1}\mid x,\mu)\right] = E(\mu\mid x) = \lambda\bar{x} + (1-\lambda)\theta
$$

$$
\begin{aligned}
Var(x_{n+1}\mid x) &= E_{\mu\mid x}\left[Var(x_{n+1}\mid x,\mu)\right] + Var_{\mu\mid x}\left[E(x_{n+1}\mid x,\mu)\right] \\
&= E(\sigma^2) + Var(\mu\mid x) \\
&= \sigma^2 + (1-\lambda)\delta^2
\end{aligned}
$$

So

$$
x_{n+1}\mid x \sim N\!\left(\lambda\bar{x} + (1-\lambda)\theta,\; \sigma^2 + (1-\lambda)\delta^2\right)
$$

> ✔ Verified: Normal–Normal posterior for $\mu$ has mean $\lambda\bar x+(1-\lambda)\theta$ and variance $(1-\lambda)\delta^2$ with $\lambda=\delta^2/(\delta^2+\sigma^2/n)$

> ✔ Verified: the predictive integral equals the $N(m,\ \sigma^2+v)$ density, i.e. means add-through and variances add

## **Example(2)**

There are two factories, denoted by $\theta = 0$ and $\theta = 1$.

Mathematical Model:

Prior: $P(\theta = 0) = \frac{1}{3} = 1 - P(\theta = 1)$

Y: bolt is defective

$P[Y = 1\mid\theta = 0] = \frac{2}{10} = 1 - P[Y = 0\mid\theta = 0]$

$P[Y = 1\mid\theta = 1] = \frac{1}{10} = 1 - P[Y = 0\mid\theta = 1]$

Assume that bolts are drawn independently.

So if we draw a bolt, what is the probability that this bolt is defective? i.e. $P[Y = 1] = ?$

$$
P[Y=1] = P[Y=1\mid\theta=0]P(\theta=0) + P[Y=1\mid\theta=1]P(\theta=1) = \frac{2}{10}\frac{1}{3} + \frac{1}{10}\frac{2}{3} = \frac{4}{30} = \frac{8}{60}
$$

> ✔ Verified: marginal defective probability $P[Y=1]=4/30=8/60$

Pick a bolt, $Y_1 = 1$

### PDF page 24 (booklet page 19)

$$P[\theta = 0 \mid Y_1 = 1] = \frac{P(Y_1=1 \mid \theta=0)P(\theta=0)}{P(Y_1=1\mid\theta=0)P(\theta=0) + P(Y_1=1\mid\theta=1)P(\theta=1)}$$

$$= \frac{\frac{2}{10}\frac{1}{3}}{\frac{2}{10}\frac{1}{3} + \frac{1}{10}\frac{2}{3}} = \frac{1}{2} = P(\theta = 1 \mid Y_1 = 1)$$

> ✔ Verified: The posterior P[θ=0|Y1=1] = (2/10)(1/3) / [(2/10)(1/3) + (1/10)(2/3)] equals 1/2, hence equals P(θ=1|Y1=1).

Pick another bolt $Y_2$

$$P[Y_2=1 \mid Y_1=1] = P[Y_2=1\mid Y_1=1, \theta=0]P[\theta=0\mid Y_1=1] + P[Y_2=1 \mid Y_1=1, \theta=1]P[\theta=1\mid Y_1=1]$$

$$= \frac{2}{10}\frac{1}{2} + \frac{1}{10}\frac{1}{2} = \frac{3}{20} = \frac{9}{60}$$

> ✔ Verified: P[Y2=1|Y1=1] = (2/10)(1/2) + (1/10)(1/2) = 3/20 = 9/60.

Note $P[Y_1 = 1] < P[Y_2 = 1 \mid Y_1 = 1]$

> ✔ Verified: The marginal P[Y1=1] = 2/15 is strictly less than P[Y2=1|Y1=1] = 3/20.

**3.1 Motivating Monte Carlo Methods (integration)**

$\int_R g(x)f(x)dx = E[g(x)] < \infty$, where $f(x)$ is the density on $R$
$\int g(\theta)\pi(\theta \mid x)d\theta$ is the same thing. *(The booklet writes $x$ with an under-tilde to indicate a vector.)*

If we take $X_1, ..., X_M \overset{iid}{\sim} f(x)$

$\bar{X} = \frac{\sum_{i=1}^{M} X_i}{M} \overset{a.s.}{\longrightarrow} E(X) = \int x f(x)dx < \infty$ – Strong law of large numbers.

So for large $M : \theta = \int x f(x) dx \approx \frac{\sum_{i=1}^{M} X_i}{M}$

So $\hat{\theta} = \frac{\sum_{i=1}^{M} X_i}{M}$ is a simulation consistent estimator of $\theta$.

In the more general problem:

$\frac{\sum_{i=1}^{M} g(X_i)}{M} \overset{a.s.}{\longrightarrow} \int g(x) f(x) dx$

So $\frac{\sum_{i=1}^{M} g(X_i)}{M}$ is a *simulation consistent estimator* of $\int g(x)f(x)dx$. *[hand-drawn star in the left margin marking this line]* *[margin notes, right: "$Y_i = g(X_i)$"; "$\frac{1}{M}\sum_{i=1}^{M} Y_i = \bar{Y}$"]*

Suppose $Var[g(x)] < \infty$

$Var(\bar{Y}) = \frac{\sigma^2}{M}$ *(correction: the printed "$\bar{X}$" is struck through and replaced by handwritten "$\bar{Y}$")*

We can estimate $\sigma^2$ by $s^2 = \frac{\sum_{i=1}^{M}(Y_i - \bar{Y})^2}{M-1}$ *(correction: handwritten "$Y_i - \bar{Y}$" is written above the printed "$X_i - \bar{X}$")*

So $\widehat{Var}(\bar{X}) = \frac{s^2}{M}$

$\widehat{stder}(\bar{Y}) = \sqrt{\widehat{Var}(\bar{Y})} = \frac{s}{\sqrt{M}}$ – Monte Carlo Error or Numerical Standard Error (NSE). *(correction: both printed "$\bar{X}$" symbols are struck through, with a handwritten "$y$" beneath each)*

**Example**

$X_1 \ldots X_n \sim N(\mu, \sigma^2), \quad \mu = 25, \quad \sigma^2 = 9$

$\int_{-\infty}^{+\infty} x f(x) dx = E(X) = 25$

$\int_{-\infty}^{+\infty} x^2 f(x)dx = E(X^2) = \text{Var}(X) + (E(X))^2 = 9 + 625 = 634$ *[the "$x^2$" in the integrand is circled by hand; "634" is hand-underlined]* *[right margin: a heavily scribbled-out note, [illegible]]* *[margin notes, far right: "$Y = X^2$"; "$Z$"]*

> ✔ Verified: For X ~ N(mu=25, sigma^2=9), E(X^2) = Var(X) + (E X)^2 = 9 + 625 = 634, matching the exact Gaussian integral.

HW:
$Z \sim N(0,1)$

### PDF page 25 (booklet page 20)

$$\theta = \int_a^b \sqrt{|z|}\,\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}dz$$

$$= \Big[\int_a^b \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}dz\Big]\int_a^b \sqrt{|z|}\Big[\frac{\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}}{\int_a^b \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}dz}\Big]dz$$

> ⚠ Check could not run (unsafe): The displayed factorization of the truncated-normal integral is an identity (checked numerically on a=-1, b=2 and symbolically as a factorization). — disallowed import: mpmath

**3.2 Prior Construction** *(correction: the printed heading reads "Constraction" [sic]; a handwritten "u" with an insertion caret is inserted over the "a", giving "Construction")*

Two types of prior distributions:
a. Subjective: proper, conjugate.
b. Objective: proper, improper (noninformative).

Objective priors are constructed based on the likelihood function (also conjugate). *(correction: the printed word reads "construted" [sic]; a handwritten "c" with an insertion caret is inserted between "u" and "t")*
Objective priors are two types:
a. Jeffreys' prior.
b. Shrinkage prior.

**Example**

$y_1, ..., y_n \mid \mu \overset{iid}{\sim} N(\mu, \sigma^2)$ *(The booklet writes $\mu$ with under-tildes to indicate vectors.)*

$\mu \sim N(\theta, \delta^2)$ – subjective, also conjugate (prior and posterior are in the same family).

$\mu \mid y \sim N(\lambda \bar{y} + (1-\lambda)\theta, (1-\lambda)\delta^2)$

> ⚠ Check FAILED: Normal-normal conjugacy: posterior is N(lambda*ybar + (1-lambda)*theta, (1-lambda)*delta^2) with lambda = n*delta^2/(sigma^2 + n*delta^2). — the stated result did not reproduce (see verification log)

We say that $\mu \sim N(\theta, \delta^2)$ is a conjugate prior.

**Example**

$X_1, ..., X_n \mid \theta \overset{iid}{\sim} Bernoulli(\theta)$

$\theta \sim Beta(\alpha, \beta)$

$\theta \mid x \sim Beta(s + \alpha, n - s + \beta)$

> ✔ Verified: Beta-Bernoulli conjugacy: prior Beta(alpha,beta) with s successes in n trials gives posterior Beta(s+alpha, n-s+beta).

**Example**

$X_1, ..., X_n \mid \theta \overset{iid}{\sim} f(x \mid \theta) = \theta e^{-\theta x}, x \geq 0$

$\theta \sim Gamma(\alpha, \beta)$

$$\pi(\theta) = \frac{\beta^\alpha \theta^{\alpha-1}e^{-\beta\theta}}{\Gamma(\alpha)}$$

$\theta \mid x \sim Gamma(n + \alpha, n\bar{x} + \beta), \theta > 0$

> ✔ Verified: Gamma-exponential conjugacy: prior Gamma(alpha,beta), n iid Exp(theta) observations give posterior Gamma(n+alpha, n*xbar+beta).

**Why do we use conjugate priors?**

1. Easy to interpret.
2. Easy computations.
3. Very useful today because they are used as building blocks for more complicated models (e.g., hierarchical Bayesian models).
4. Easy to update.

**Example of (4)**

### PDF page 26 (booklet page 21)

$$y_1, \dots, y_{n_1} \sim Bernoulli(\theta)$$

$$\theta \sim Beta(\alpha, \beta)$$

$$\theta \mid \underset{\sim}{y}_1 \;\sim\; Beta(s_1 + \alpha,\; n_1 - s_1 + \beta)$$

*(The booklet writes $y$, $x$ and $X$ with under-tildes to indicate vectors.)*

> ⚠ Check FAILED: Beta(α,β) prior with n₁ Bernoulli trials and s₁ successes yields a Beta(s₁+α, n₁−s₁+β) posterior. — the stated result did not reproduce (see verification log)

$$y_{n_1+1}, \dots, y_{n_1+n_2} \sim Bernoulli(\theta)$$

$$\theta \mid \underset{\sim}{y}_1, \underset{\sim}{y}_2 \;\sim\; Beta(s_1 + s_2 + \alpha,\; n_1 - s_1 + n_2 - s_2 + \beta)$$

> ⚠ Check FAILED: Sequentially updating the stage-one posterior with a second batch (n₂ trials, s₂ successes) gives Beta(s₁+s₂+α, n₁−s₁+n₂−s₂+β). — the stated result did not reproduce (see verification log)

It has the same posterior as:

$$y_1, \dots, y_{n_1}, y_{n_1+1}, \dots, y_{n_1+n_2} \mid \theta \sim Bernoulli(\theta)$$

$$\theta \sim Beta(\alpha, \beta)$$

> ✔ Verified: Pooling all n₁+n₂ observations against the original Beta(α,β) prior gives the same posterior as the two-stage update.

*[a long hand-drawn wavy line is ruled across the page here, closing off the block above; its right end hooks upward like a bracket]*

**Digression – Sufficient Statistics**

$X_1, \dots, X_n \mid \theta \;\underline{iid}\; f(x \mid \theta)$

$T(\underset{\sim}{X})$ is a sufficient statistic.

$f(\underset{\sim}{x} \mid T(\underset{\sim}{x}), \theta)$ does not depend on $\theta$

Factorization Theorem:

If $f(\underset{\sim}{x} \mid \theta) = g(T(\underset{\sim}{x}) \mid \theta) h(\underset{\sim}{x})$, where $g(T(\underset{\sim}{x}) \mid \theta)$ depends on $T(\underset{\sim}{x})$ and $\theta$, $h(\underset{\sim}{x})$ does not depend on $\theta$.

Then $T(\underset{\sim}{x})$ is a sufficient statistic. (True both ways.)

**Example**

$X_1, \dots, X_n \mid \mu \;\underline{iid}\; N(\mu, \sigma^2)$, $\sigma^2$ is known.

$$
\begin{aligned}
f(\underset{\sim}{x} \mid \mu) &= \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} exp\left\{ -\frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2 \right\} \\
&= \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} exp\left\{ -\frac{1}{2\sigma^2}\left[ (n-1)s^2 + n(\bar{x} - \mu)^2 \right] \right\} \\
&= e^{-\frac{n}{2\sigma^2}(\bar{x} - \mu)^2} \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} e^{-\frac{(n-1)s^2}{2\sigma^2}}
\end{aligned}
$$

> ✔ Verified: The sum-of-squares decomposition Σ(xᵢ−μ)² = (n−1)s² + n(x̄−μ)².

> ✔ Verified: The normal likelihood factors as e^{-n(x̄−μ)²/(2σ²)} · (2πσ²)^{−n/2} e^{−(n−1)s²/(2σ²)}, matching line 3 to line 2.

Here $g(\bar{x}, \mu) = e^{-\frac{n}{2\sigma^2}(\bar{x}-\mu)^2}$ and $h(x) = \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} e^{-\frac{(n-1)s^2}{2\sigma^2}}$.

So $\bar{X}$ is a sufficient statistic.

If both $(\mu, \sigma^2)$ are unknown.

$$f(\underset{\sim}{x} \mid \mu, \sigma^2) = f(\underset{\sim}{x} \mid \mu) = g(\bar{x}, s^2, \mu, \sigma^2) h(x)$$

So $(\bar{X}, s^2)$ are joint sufficient for $(\mu, \sigma^2)$.

**3.2.1 How to construct conjugate priors?**

Idea: Look at the likelihood function as a distribution of the parameters.

$$\pi(\theta \mid \underset{\sim}{x}) = \frac{L(\theta \mid \underset{\sim}{x})}{\int L(\theta \mid \underset{\sim}{x}) d\theta} \;\text{— —fiducial inference.}$$

### PDF page 27 (booklet page 22)

Now take the data to be unknown (e.g., sufficient statistics and sample size) to be parameters in the likelihood function. This is now the conjugate prior.

**Examples:**

(1) $X|\lambda \sim \text{pisson}[sic](\lambda)$, $\pi(\lambda) \propto \frac{1}{\sqrt{\lambda}}$, $\lambda > 0$
$\pi(\lambda) = \text{Gamma}(\alpha, \beta)$ is a conjugate prior.

*[the expression $\pi(\lambda) \propto \frac{1}{\sqrt{\lambda}},\ \lambda > 0$ is enclosed in a hand-drawn angular bracket and slashed through with a long diagonal line running off to the upper right]*

> ✔ Verified: For $X\mid\lambda\sim$ Poisson$(\lambda)$, a Gamma$(\alpha,\beta)$ prior is conjugate: posterior kernel $=$ Gamma$(\alpha+x,\beta+1)$ kernel.

(2) $X_1, ..., X_n|\theta \;\; iid \;\; Bernoulli(\theta)$

$L(\theta|x) = f(x|\theta) = \prod_{i=1}^{n} f(x_i|\theta) = \prod_{i=1}^{n} \theta^{x_i}(1-\theta)^{1-x_i} = \theta^{\sum_{i=1}^{n} x_i}(1-\theta)^{n-\sum_{i=1}^{n} x_i} = \theta^{s}(1-\theta)^{n-s}$

> ✔ Verified: $\prod_{i=1}^{n}\theta^{x_i}(1-\theta)^{1-x_i}=\theta^{s}(1-\theta)^{n-s}$, $s=\sum x_i$.

$\pi(\theta) \propto \theta^{\alpha}(1-\theta)^{\beta}$
$\theta \sim Beta(\alpha, \beta)$
So the posterior is still Beta, it is conjugate.

> ⚠ Check FAILED: $\theta^{s}(1-\theta)^{n-s}\theta^{\alpha}(1-\theta)^{\beta}$ is the kernel of Beta$(s+\alpha+1,\ n-s+\beta+1)$ (posterior is still Beta). — the stated result did not reproduce (see verification log)

(3) $X_1, ..., X_n|\mu \;\; iid \;\; N(\mu, \sigma^2)$, $\sigma^2$ is known.

$L(\mu|\bar{x}) \propto e^{-\frac{n}{2\sigma^2}(\mu-\bar{x})^2}$

> ✔ Verified: $\sum_i (x_i-\mu)^2=\sum_i (x_i-\bar x)^2+n(\mu-\bar x)^2$, hence $L(\mu\mid\bar x)\propto e^{-\frac{n}{2\sigma^2}(\mu-\bar x)^2}$.

$\pi(\mu) \propto e^{-\frac{1}{2\delta^2}(\mu-\theta)^2}$
$\mu \sim N(\theta, \delta^2)$
So the posterior is still normal.

*[margin note, right of this example: "noninformative" (hand-underlined) — "does not change the(?) likelihood function" [one further word illegible]; below it "proper" (hand-underlined) — "integrat[es](?) to a finite(?) value"]*

> ✔ Verified: Normal likelihood $\times$ normal prior is a normal kernel in $\mu$ with precision $n/\sigma^2+1/\delta^2$ (posterior still normal).

**3.2.2 Two ways to construct objective priors**

a. Jeffreys' prior – likelihood.
b. Shrinkage prior – start with a conjugate.

*[margin table, right of this subsection — a hand-drawn 2×2 box. The column heading (unwritten, implied by the note above) is "proper", the row heading is "noninformative":]*

| *noninformative* \\ *proper* | yes | no |
|---|---|---|
| **yes** | ✓ 1 | ✓ 2 |
| **no** | ✓ 3 (?) | ✓ 4 |

**Objective Priors**

Alternative to conjugate priors when there is little or no information.
$X_1, ..., X_n|\mu, \sigma^2 \;\; iid \;\; N(\mu, \sigma^2)$

Case 1:
$\pi(\mu, \sigma^2) \propto \frac{1}{\sigma^2}, -\infty < \mu < \infty, \sigma^2 > 0$.
$\int_{0}^{\infty} \int_{-\infty}^{\infty} \frac{1}{\sigma^2} d\mu \, d\sigma^2 = \infty$, so it is improper.

> ✔ Verified: $\int_{0}^{\infty}\int_{-\infty}^{\infty}\sigma^{-2}\,d\mu\,d\sigma^{2}=\infty$ (the prior is improper).

Case 2:
$\sigma^2$ is known.
$\pi(\mu) \propto 1, -\infty < \mu < \infty$

Case 3:
$\mu$ is known, $\pi(\sigma^2) \propto \frac{1}{\sigma^2}, \sigma^2 > 0$

*[a long hand-drawn sweeping curve runs across the whole page width at this line, crossing through the printed text and ending in an arrowhead at the right edge]*

*[Handwritten scratch work in the right margin, alongside Cases 1–3, partly legible: "Location / Scale" at the top; below it a heavily scribbled-out boxed word (appears twice — "proper" / "improper"(?)) and "$Beta(\theta,\cdot)$"(?). Then four numbered examples, matching the four cells of the 2×2 box above:*
*$1{:}\;\; X|\theta \sim$ [scribbled out]$\;$, $\;\theta \sim N(0,1)$(?)*
*$2{:}\;\; X|\mu \sim N(\mu,1)$, $\;\pi(\mu)=1$*
*$3{:}\;\; X|\mu \sim N(\theta,\delta^2)$(?), $\;\mu \sim N(0,\delta^2)$(?)*
*$4{:}\;\; X|\sigma^2 \sim N(0,\sigma^2)$, $\;\pi(\sigma^2)=1$*
*These are lecture scratch notes giving one example prior for each (proper, noninformative) combination.]*

*[hand-drawn star "✳" in the far left margin at this point]*

**Jeffreys' prior**

*[a large hand-drawn oval loops around the "Jeffreys' prior" heading and the $\pi(\theta)$ beginning the next line]*

$\pi(\theta) \propto |I(\theta)|^{\frac{1}{2}}$, where $I(\theta)$ is information matrix in a single observation. *[a wavy hand-underline runs beneath "$I(\theta)$ is information matrix"]*

We need regularity conditions:

### PDF page 28 (booklet page 23)

1. Range of $X$ does not depend on $\theta$.
2. Can interchange differentiation and integration.

So if $\theta$ is just a single parameter, $\pi(\theta) \propto \sqrt{I(\theta)}$

$$I(\theta) = E[\frac{d}{d\theta} logL(\theta|x)]^2 = -E[\frac{d^2}{d\theta^2} logL(\theta|x)]$$

*[both printed $E$'s are circled by hand]*

*[margin notes: "Information"; "Fisher's(?) information" — written across the top right margin, around the printed page number]*

*[margin note, with an arrow pointing up to the first circled $E$: "average over $x|\theta$"]*

&nbsp;

If there are two parameters:

$$\pi(\alpha,\beta) \propto |I(\alpha,\beta)|^{\frac{1}{2}}$$

$$\Delta = log[L(\alpha,\beta|x)]$$

*(The booklet writes $x$ with an under-tilde here to indicate a vector — added by hand.)*

$$\left|\begin{array}{cc} \dfrac{\partial^2 \Delta}{\partial \alpha^2} & \dfrac{\partial^2 \Delta}{\partial \alpha \partial \beta} \\[2ex] \dfrac{\partial^2 \Delta}{\partial \alpha \partial \beta} & \dfrac{\partial^2 \Delta}{\partial \beta^2} \end{array}\right| \;\text{— Hessian Matrix.}$$

*[Handwritten work overlaying and surrounding the determinant, partly legible: a large "$E$" with subscript "$x|\alpha,\beta$"(?) is inserted just inside the left bar, and a hand-drawn closing bar with exponent "$\tfrac{1}{2}$" is added at the upper right, so that the display is being read as $\left| E_{x\mid\alpha,\beta}\left[\text{Hessian}\right]\right|^{1/2}$. In the left margin: "average over" above a struck symbol and "$x\mid\alpha,\beta$"(?).]*

**Examples:**

(1) $X|\mu \sim N(\mu,\sigma^2)$

$L(\mu|x) = (\frac{1}{2\pi\sigma^2})^{\frac{1}{2}} e^{-\frac{1}{2\sigma^2}(x-\mu)^2}$

$logL(\mu|x) = -\frac{1}{2\sigma^2}(x-\mu)^2$

$\frac{d}{d\mu} logL(\mu|x) = \frac{1}{\sigma^2}(x-\mu)$

$-E[\frac{d}{d\mu} logL(\mu|x]^2 = \frac{1}{\sigma^2}E(x-\mu)^2 = 1$  $\text{[sic: the closing parenthesis after } x \text{ is missing, and the leading minus sign is spurious for the squared-score form]}$

> ✔ Verified: Example (1) — score of the normal in $\mu$ is $(x-\mu)/\sigma^2$, and $\frac{1}{\sigma^2}E(x-\mu)^2 = 1$.

$\pi(\mu) \propto 1$

&nbsp;

*[a large hand-drawn brace "$\{$" spans the four lines of Example (2) in the left margin]*

(2) $X|\sigma^2 \sim N(\mu,\sigma^2)$, $\mu$ is known.

$L(\sigma^2|x) = (\frac{1}{2\pi\sigma^2})^{\frac{1}{2}} e^{-\frac{1}{2\sigma^2}(x-\mu)^2}$

$logL(\sigma^2|x) = -\frac{1}{2}log\sigma^2 - \frac{1}{2\sigma^2}(x-\mu)^2$

$\pi(\sigma^2) \propto \frac{1}{\sigma^2}$

> ⚠ Check FAILED: Example (2) — Jeffreys prior for $\sigma^2$ with $\mu$ known is $\propto 1/\sigma^2$. — the stated result did not reproduce (see verification log)

&nbsp;

(3) $X|\mu,\sigma^2 \sim N(\mu,\sigma^2)$

Then we get $\pi(\mu,\sigma^2) \propto (\frac{1}{\sigma^2})^{\frac{3}{2}}$

Don't use this, we use $\pi(\mu,\sigma^2) \propto \frac{1}{\sigma^2}$

(Actually, it assume independence of $\mu$ and $\sigma^2$, $\pi(\mu,\sigma^2) \propto \pi(\mu)\pi(\sigma^2)$.)

> ⚠ Check FAILED: Example (3) — the joint Jeffreys prior for $(\mu,\sigma^2)$ is $\propto (1/\sigma^2)^{3/2}$. — the stated result did not reproduce (see verification log)

*[two long hand-drawn diagonal strokes cut across the block from the "(Actually, it assume ...)" line up to the right of the "(2) $X|\sigma^2 \sim N(\mu,\sigma^2)$, $\mu$ is known." line]*

&nbsp;

(4) $X|\lambda \sim$ Poisson$(\lambda)$,    $E(X) = \lambda$

*[Handwritten work filling the right margin beside Examples (2)–(4), a derivation of the Jeffreys prior for $\sigma^2$, partly legible: $\frac{d}{d\sigma^2}\log L(\sigma^2|x) = -\frac{1}{2\sigma^2} + \frac{1}{2\sigma^4}(x-\mu)^2$ ... $\frac{d^2}{d(\sigma^2)^2}\log L(\sigma^2|x) = +\frac{1}{2\sigma^4} - \frac{1}{\sigma^6}(x-\mu)^2$ ... $\frac{1}{2\sigma^4} - \frac{1}{\sigma^4}(?) = -\frac{1}{2\sigma^4}$ ... $-|I(\cdot)|^{1/2} = \left(\frac{1}{2\sigma^4}\right)^{1/2} = \frac{1}{\sigma^2}$. These are lecture scratch notes verifying $\pi(\sigma^2) \propto 1/\sigma^2$ in Example (2).]*

> ⚠ Check FAILED: Margin scratch work — the first and second derivatives of $\log L(\sigma^2|x)$ and the resulting $-E = 1/(2\sigma^4)$. — the stated result did not reproduce (see verification log)

### PDF page 29 (booklet page 24)

$$f(x\mid\lambda)=\frac{\lambda^{x}e^{-\lambda}}{x!},\qquad x=0,1,\ldots$$

$$\log f(x\mid\lambda)=x\log\lambda-\lambda-\log(x!)$$

$$\frac{\partial}{\partial\lambda}\log f(x\mid\lambda)=\frac{x}{\lambda}-1$$

$$\frac{\partial^{2}}{\partial\lambda^{2}}\log f(x\mid\lambda)=-\frac{x}{\lambda^{2}}$$

$$-E\left[\frac{\partial^{2}}{\partial\lambda^{2}}\log f(x\mid\lambda)\right]=\frac{E(X)}{\lambda^{2}}=\frac{1}{\lambda}=I(\lambda)$$

$$\pi(\lambda)\propto\frac{1}{\sqrt{\lambda}},\qquad \lambda>0,\qquad \text{Improper}$$

> ✔ Verified: Poisson Fisher information is $1/\lambda$ and Jeffreys' prior $\lambda^{-1/2}$ is improper on $(0,\infty)$.

(5) $X\mid p\sim Binomial(n,p)$ , $\;E(x)=np$

$$f(x\mid p)=\binom{n}{x}p^{x}(1-p)^{n-x},\qquad x=0,1,\ldots,n$$

$$\log f(x\mid p)=\log\binom{n}{x}+x\log p+(n-x)\log(1-p)$$

$$\frac{\partial}{\partial p}\log f(x\mid p)=\frac{x}{p}-\frac{n-x}{1-p}$$

$$\frac{\partial^{2}}{\partial p^{2}}\log f(x\mid p)=-\frac{x}{p^{2}}-\frac{n-x}{(1-p)^{2}}$$

$$E\left[\frac{\partial^{2}}{\partial p^{2}}\log f(x\mid p)\right]=-\frac{np}{p^{2}}-\frac{n(1-p)}{(1-p)^{2}}$$

$$I(p)=n\left[\frac{1}{p}+\frac{1}{1-p}\right]\frac{n}{p(1-p)}$$

$$\pi(p)\propto\frac{\sqrt{n}}{\sqrt{p(1-p)}},\qquad 0<p<1\quad,\qquad \text{proper}$$

$$\pi(p)=\frac{p^{\frac{1}{2}-1}(1-p)^{\frac{1}{2}-1}}{B\!\left(\frac{1}{2},\frac{1}{2}\right)}=\frac{1}{\pi\sqrt{p(1-p)}},\;0<p<1,\;\text{Arcsine Distribution}$$

*(sic: the $I(p)$ line as printed juxtaposes $n\left[\frac{1}{p}+\frac{1}{1-p}\right]$ and $\frac{n}{p(1-p)}$ with no equals sign between them; the intended statement is $I(p)=n\left[\frac{1}{p}+\frac{1}{1-p}\right]=\frac{n}{p(1-p)}$.)*

> ✔ Verified: Binomial Fisher information equals $n[1/p + 1/(1-p)] = n/(p(1-p))$.

> ⚠ Check FAILED: The Beta(1/2,1/2) density equals $1/(\pi\sqrt{p(1-p)})$ and is proper. — the stated result did not reproduce (see verification log)

## Normal Example
*(printed as a bold section heading "Normal Example")*

a) $X\mid\mu\sim N\left(\mu,\sigma^{2}\right),\quad \sigma^{2}$ is known

$$f(x\mid\mu)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{1}{2\sigma^{2}}(x-\mu)^{2}},\;-\infty<\mu<+\infty$$

$$\log f(x\mid\mu)=-\frac{1}{2}\log\left(2\pi\sigma^{2}\right)-\frac{1}{2\sigma^{2}}(x-\mu)^{2}$$

$$\frac{\partial}{\partial\mu}\log f(x\mid\mu)=\frac{1}{\sigma^{2}}(x-\mu)$$

$$\frac{\partial^{2}}{\partial\mu^{2}}\log f(x\mid\mu)=-\frac{1}{\sigma^{2}}$$

$$I(\mu)=\frac{1}{\sigma^{2}}\Rightarrow\text{constant}$$

Since $\pi(\mu)\propto 1$, it's improper and noninformative *[the final clause "improper and noninformative" is hand-underlined with a wavy stroke]*

> ✔ Verified: For the normal mean with known variance, $I(\mu)=1/\sigma^2$, a constant.

b) $X\mid\sigma^{2}\sim N\left(\mu,\sigma^{2}\right),\quad \mu$ is known

Get $\pi\left(\theta^{2}\right)\propto\frac{1}{\sigma^{2}}$ improper and noninformative *[sic: "$\theta^2$" should be "$\sigma^2$"]* *[hand underline under "noninformative"]*

$$f\left(x\mid\sigma^{2}\right)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{1}{2\sigma^{2}}(x-\mu)^{2}}$$

*[a small illegible handwritten scrawl [illegible] sits to the right of this line]*

$$\log f\left(x\mid\sigma^{2}\right)=-\frac{1}{2}\log 2\pi-\frac{1}{2}\log\sigma^{2}-\frac{1}{2\sigma^{2}}(x-\mu)^{2}$$

$$\frac{\partial}{\partial\sigma^{2}}\log f\left(x\mid\sigma^{2}\right)=-\frac{1}{2\sigma^{2}}+\frac{1}{2(\sigma^{2})^{2}}(x-\mu)^{2}$$

$$\frac{\partial^{2}}{\partial(\sigma^{2})^{2}}\log f\left(x\mid\sigma^{2}\right)=\frac{1}{2(\sigma^{2})^{2}}-\frac{1}{(\sigma^{2})^{3}}(x-\mu)^{2}$$

$$E\left[\frac{\partial^{2}}{\partial(\sigma^{2})^{2}}\log f\left(x\mid\sigma^{2}\right)\right]=\frac{1}{2(\sigma^{2})^{2}}-\frac{1}{(\sigma^{2})^{2}}=-\frac{1}{2(\sigma^{2})^{2}}$$

$$I\left(\sigma^{2}\right)=\frac{1}{2(\sigma^{2})^{2}}$$

$$\pi\left(\sigma^{2}\right)=\frac{1}{\sqrt{2}\,\sigma^{2}}\propto\frac{1}{\sigma^{2}},\qquad \sigma^{2}>0$$

*(in the scan the radical in the last line appears to extend over "$2\sigma^2$"; the value $\sqrt{I(\sigma^2)}=\frac{1}{\sqrt{2}\,\sigma^{2}}$ and the stated proportionality $\propto\frac{1}{\sigma^{2}}$ both require the radical to cover only the $2$.)*

> ✔ Verified: For the normal variance with known mean, $E[\partial^2_{(\sigma^2)}\log f]=-1/(2(\sigma^2)^2)$, $I(\sigma^2)=1/(2(\sigma^2)^2)$, and $\sqrt{I}=1/(\sqrt2\,\sigma^2)$.

### PDF page 30 (booklet page 25)

c) $X\mid \mu,\sigma^2 \sim N\left(\mu,\sigma^2\right),\quad -\infty < \mu < +\infty,\quad \sigma^2 > 0$

$f\left(x\mid\mu,\sigma^2\right) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2\sigma^2}(x-\mu)^2}$

$\Delta\left(\mu,\sigma^2\right) = \log f\left(x\mid\mu,\sigma^2\right) = -\frac{1}{2}\log 2\pi - \frac{1}{2}\log\sigma^2 - \frac{1}{2\sigma^2}(x-\mu)^2$

$\frac{\partial}{\partial\mu}\Delta\left(\mu,\sigma^2\right) = \frac{1}{\sigma^2}(x-\mu)$

$\frac{\partial^2}{\partial\mu^2}\Delta\left(\mu,\sigma^2\right) = -\frac{1}{\sigma^2}$

$\frac{\partial^2}{\partial\mu\partial\sigma^2}\Delta\left(\mu,\sigma^2\right) = -\frac{1}{(\sigma^2)^2}(x-\mu)$

$\frac{\partial}{\partial\sigma^2}\Delta\left(\mu,\sigma^2\right) = -\frac{1}{2\sigma^2} + \frac{1}{2(\sigma^2)^2}(x-\mu)^2$

$\frac{\partial}{\partial(\sigma^2)^2}\Delta\left(\mu,\sigma^2\right) = \frac{1}{2(\sigma^2)^2} - \frac{1}{(\sigma^2)^3}(x-\mu)^2 \quad \text{[sic: the operator should be }\tfrac{\partial^2}{\partial(\sigma^2)^2}\text{]}$

$E\left[\frac{\partial^2}{\partial(\sigma^2)^2}\Delta\left(\mu,\sigma^2\right)\right] = -\frac{1}{2(\sigma^2)^2}$

> ✔ Verified: The printed derivatives of the normal log-density and the expectation $E[\partial^2_{(\sigma^2)^2}\Delta] = -1/(2(\sigma^2)^2)$ are correct.

$$-H = \begin{bmatrix} \frac{1}{\sigma^2} & 0 \\ 0 & \frac{1}{2(\sigma^2)^2} \end{bmatrix}$$

$\pi\left(\mu,\sigma^2\right) = \left|-H\right|^{\frac{1}{2}} = \left[\frac{1}{\sigma^2}\cdot\frac{1}{2(\sigma^2)^2}\right]^{\frac{1}{2}} = \frac{1}{(\sigma^2)^{\frac{3}{2}}}$, improper and *[illegible handwritten squiggle above the word]* $\underline{\text{non}}$informative *[the prefix "non" is hand-underlined]*

> ✔ Verified: $|-H|^{1/2} = \frac{1}{\sqrt2 (\sigma^2)^{3/2}}$, so the booklet's $\frac{1}{(\sigma^2)^{3/2}}$ is correct only up to the constant $1/\sqrt2$ (i.e. proportional, not equal).

Don't use this form of Jeffery's prior.

**Invariance Property of Jefferys' Prior**

*[Handwritten scratch note in the right margin, alongside this heading: about four lines of slanted cursive crossed by two long diagonal strokes, almost entirely illegible. Partial best-effort reading: "$\phi$ has the ... support of ... Jacobian(?) ...". [illegible]]*

$P(\theta) \propto \sqrt{I(\theta)}$, Jefferys' prior

$\phi = \varphi(\theta),\quad \phi$ is a one-to-one function of $\theta$.

$P(\varphi(\theta)) = \frac{P(\theta)}{\varphi'(\theta)} = \frac{\sqrt{I(\theta)}}{\varphi'(\theta)} = \sqrt{I(\varphi(\theta))}$

Basically, $\sqrt{I(\phi)} = \sqrt{I(\theta)}\left|\frac{d\theta}{d\phi}\right|$

> ✔ Verified: Fisher information transforms as $I(\phi) = I(\theta)(d\theta/d\phi)^2$, hence $\sqrt{I(\phi)} = \sqrt{I(\theta)}|d\theta/d\phi|$.

$P(\theta)$ Jefferys' *(a small handwritten caret/tilde sits over the "ff" of "Jefferys")* prior, $\phi = \varphi(\theta)$?

**Two ways:**

(1) In the likelihood function, change $\theta$ to $\phi$

(2) $p(\theta)$ Jefferys' prior transform *(a handwritten vertical stroke/insertion caret sits at the start of "transform")* to $\phi$

(1) and (2) are the same $\Rightarrow$ this is invariance property. *[the final clause "this is invariance property" is hand-underlined, with a squiggle/arrow drawn beneath the underline]*

*[margin note, opposite the "Two ways" list: "⟶ ... has(?) Jefferys' prior for $\phi$" — the middle words are illegible]*

**Examples**

(1) $X\mid\lambda \sim \text{Poisson}(\lambda),\quad \pi(\lambda) \propto \frac{1}{\sqrt{\lambda}}$

$\phi = \sqrt{\lambda}$?

$\lambda = \phi^2 \qquad \frac{d\lambda}{d\phi} = 2\phi$

$\pi(\phi) \propto \frac{1}{\phi}\cdot 2\phi = 2$

> ✔ Verified: Transforming $\pi(\lambda)\propto\lambda^{-1/2}$ by $\lambda=\phi^2$ gives $\pi(\phi)\propto 2$ (constant), matching $\sqrt{I(\phi)}=2$.

*[Handwritten work in the bottom right margin — the same example done the other way, by re-expressing the likelihood in $\phi$:*
$$\frac{\lambda^x e^{-\lambda}}{x!} \qquad \frac{\phi^{2x}e^{-\phi^2}}{x!}$$
$$\Delta(\phi) = 2x\ln\phi - \phi^2 - \ln x!$$
$$\Delta'(\phi) = \frac{2x}{\phi} - 2\phi$$
$$\Delta''(\phi) = -\frac{2x}{\phi^2}$$
$$E\left(\Delta''(\phi)\right) = \frac{-2\phi^2}{\phi^2} = \underline{\underline{-2}}$$
*The last line's "$-2$" is double-underlined. Note the slip: $\Delta''(\phi)$ should be $-\frac{2x}{\phi^2} - 2$, giving $E[-\Delta''(\phi)] = I(\phi) = 4$ and $\sqrt{I(\phi)} = 2$, which is what the printed $\pi(\phi)\propto 2$ requires; as written the scratch note gives $I(\phi)=2$.]*

> ✔ Verified: In the handwritten scratch work, $\Delta(\phi)$ and $\Delta'(\phi)$ are correct but $\Delta''(\phi) = -2x/\phi^2 - 2$, so $E[-\Delta''(\phi)] = 4$, not the written $2$.

(2) $X\mid p \sim \text{Binomial}\left(n,p\right)$

$\pi(p) = \frac{1}{\pi\sqrt{p(1-p)}},\quad 0 < p < 1$

$\phi = \ln\left(\frac{p}{1-p}\right)\quad,\quad -\infty < \phi < +\infty$

> ⚠ Check FAILED: $\pi(p) = \frac{1}{\pi\sqrt{p(1-p)}}$ integrates to 1 on $(0,1)$ (the arcsine / Beta(1/2,1/2) density). — the stated result did not reproduce (see verification log)

### PDF page 31 (booklet page 26)

$$\frac{p}{1-p}=e^{\phi},\qquad p=\frac{e^{\phi}}{1+e^{\phi}}$$

$$\frac{dp}{d\phi}=\frac{e^{\phi}\left(1+e^{\phi}\right)-e^{2\phi}}{\left(1+e^{\phi}\right)^{2}}=\frac{e^{\phi}}{\left(1+e^{\phi}\right)^{2}}$$

> ✔ Verified: With $p=e^{\phi}/(1+e^{\phi})$, $dp/d\phi$ equals both $\frac{e^{\phi}(1+e^{\phi})-e^{2\phi}}{(1+e^{\phi})^{2}}$ and $\frac{e^{\phi}}{(1+e^{\phi})^{2}}$.

$$\pi(\phi)=\frac{1}{\pi\sqrt{\dfrac{e^{\phi}}{\left(1+e^{\phi}\right)^{2}}}}\cdot\frac{e^{\phi}}{\left(1+e^{\phi}\right)^{2}}=\frac{\sqrt{e^{\phi}}}{1+e^{\phi}}\;\text{[sic: the factor }1/\pi\text{ is dropped from the final expression]}\qquad-\infty<\phi<+\infty$$

> ✔ Verified: The product $\frac{1}{\pi\sqrt{e^{\phi}/(1+e^{\phi})^{2}}}\cdot\frac{e^{\phi}}{(1+e^{\phi})^{2}}$ equals $\frac{\sqrt{e^{\phi}}}{\pi(1+e^{\phi})}$; the printed right-hand side $\frac{\sqrt{e^{\phi}}}{1+e^{\phi}}$ omits the factor $1/\pi$.

*[Handwritten scratch work down the right margin, partly legible — the Fisher-information derivation for the binomial likelihood written in the logit parameter $\phi$. A struck-through "$\phi$" at the top, then:*
$$\left(\frac{e^{\phi}}{1+e^{\phi}}\right)^{y}\left(\frac{1}{1+e^{\phi}}\right)^{n-y}$$
$$\phi y-n\log\!\left(1+e^{\phi}\right)$$
$$y-\frac{ne^{\phi}}{1+e^{\phi}}$$
$$-\left[\frac{ne^{\phi}\left(1+e^{\phi}\right)-ne^{\phi}e^{\phi}}{\left(1+e^{\phi}\right)^{2}}\right]$$
$$-\frac{ne^{\phi}}{\left(1+e^{\phi}\right)^{2}}$$
$$\pi(\phi)\propto\frac{\sqrt{e^{\phi}}}{1+e^{\phi}}$$
$$-\infty<\phi<\infty$$
*These are lecture scratch notes deriving $I(\phi)$ directly from the binomial log-likelihood.]*

> ⚠ Check FAILED: For the binomial log-likelihood in the logit parameter, $\ell(\phi)=\phi y-n\log(1+e^{\phi})$, the Fisher information is $I(\phi)=ne^{\phi}/(1+e^{\phi})^{2}$ and $\sqrt{I(\phi)}\propto\sqrt{e^{\phi}}/(1+e^{\phi})$. — the stated result did not reproduce (see verification log)

Note:

(1) Likelihood changes, the prior changes

(2) Violate the likelihood principle *(correction: the printed line ends at "likelihood"; "principle" is supplied by hand)*

(3) Multiparameters

**Summary** *[handwritten heading, with a long hand-drawn flourish sweeping from it down into the left margin]*

$$x_{1},\dots,x_{n}\mid\theta\ \overset{iid}{\sim}\ f(x\mid\theta)$$

Find Fisher's information in a single observation. *[the sentence is hand-underlined (?)]*

If $\theta$ is a single value, $\pi(\theta)\propto\sqrt{I(\theta)}$

If $\theta$ is a vector, $\pi(\theta)\propto\sqrt{|I(\theta)|}$ – Jeffreys' prior, $I(\theta)=-E\left[\frac{\partial^{2}}{\partial\theta^{2}}\log f(x\mid\theta)\right]$

*[margin note, left: circled "(bad)"]* Jeffreys' prior has a simple difficulty, Jeffreys' prior changes with likelihood function.

Jeffreys' prior is invariant to scale and location of the response, $y$ (?). *(correction: "and location of the response, $y$" is a handwritten insertion after the printed word "scale")*

Jeffreys' prior is invariant to one-to-one transformation.

If $\pi(\theta)\propto\sqrt{I(\theta)},\ \phi=g(\theta),\ g$ is one-to-one, so $\pi(\phi)\propto\sqrt{I(\phi)}$.

If we change variable by transformation:

$$\pi(\phi)\propto\left(\sqrt{I(\theta)}\right)\Big|_{\theta=g^{-1}(\phi)}\left|\frac{d}{d\phi}g^{-1}(\phi)\right|$$

*(correction: "$\theta=$" is handwritten beneath the radical, making the evaluation bar read $\theta=g^{-1}(\phi)$)*

### Examples

(1) $X\sim N(\mu,\sigma^{2})$, $\sigma^{2}$ is known.

$\pi(\mu)=1,\ -\infty<\mu<\infty$, improper = noninformative *(correction: printed "noninformation", amended by hand to "noninformative" (?))*. *[hand check-mark in margin]*

> ✔ Verified: For $X\sim N(\mu,\sigma^{2})$ with $\sigma^{2}$ known, $I(\mu)=1/\sigma^{2}$ and Jeffreys' prior $\sqrt{I(\mu)}$ is free of $\mu$.

(2) $\mu$ is known.

$\pi(\sigma^{2})\propto\frac{1}{\sigma^{2}},\ \sigma^{2}>0$, it is still improper.

> ⚠ Check FAILED: For $X\sim N(\mu,\sigma^{2})$ with $\mu$ known and $v=\sigma^{2}$, $I(v)=1/(2v^{2})$, so $\sqrt{I(v)}\propto 1/\sigma^{2}$. — the stated result did not reproduce (see verification log)

(3) $\pi(\mu,\sigma^{2})\propto\frac{1}{\sigma^{2}},\ -\infty<\mu<\infty,\ \sigma^{2}>0$ (assuming independence)

(4) Actually Jeffreys' prior $\pi(\mu,\sigma^{2})\propto\frac{1}{(\sigma^{2})^{\frac{3}{2}}}$

But we use $\pi(\mu,\sigma^{2})\propto\frac{1}{\sigma^{2}}$

> ⚠ Check FAILED: For $X\sim N(\mu,\sigma^{2})$ with both parameters unknown, $\sqrt{|I(\mu,\sigma^{2})|}\propto(\sigma^{2})^{-3/2}$. — the stated result did not reproduce (see verification log)

### "Shrinkage" prior

Example:

$$y\mid\mu\sim N(\mu,\sigma^{2})$$

### PDF page 32 (booklet page 27)

$$\mu \sim N(\theta, \delta^2), \text{ assume } \theta, \sigma^2, \delta^2 \text{ are known.}$$

So the typical form of the posterior mean is: $E(\mu|y) = \lambda y + (1-\lambda)\theta$, where $\lambda = \frac{\delta^2}{\delta^2 + \sigma^2}$.

> ✔ Verified: Normal–normal posterior mean equals $\lambda y+(1-\lambda)\theta$ with $\lambda=\delta^2/(\delta^2+\sigma^2)$.

$\lambda$ is called the shrinkage parameter.

For a shrinkage prior, take $\lambda \sim U(0,1)$ *[margin note: "Strawderman (1980's)"]*

Assume $\delta^2$ is fixed, look for the prior for $\sigma^2$

Since $\lambda = \frac{\delta^2}{\delta^2 + \sigma^2}$, then we can get the shrinkage prior for $\sigma^2$:

$$\pi(\sigma^2) \propto \frac{\delta^2}{(\delta^2+\sigma^2)^2}, \sigma^2 > 0.$$

> ✔ Verified: $\lambda=\delta^2/(\delta^2+\sigma^2)$ with $\lambda\sim U(0,1)$ induces density $\delta^2/(\delta^2+\sigma^2)^2$ on $\sigma^2>0$.

In some papers (*Albert (1980's), Christiansen and Morris (1997)*), $\pi(\sigma^2) \propto \frac{1}{(1+\sigma^2)^2}, \sigma^2 > 0$.
*(correction: "Christensen" is amended by a handwritten "ian" inserted into the word, giving "Christiansen"; "(1990's)" is replaced by handwritten "1997")*

When the constant is 1, $\pi(\sigma^2) = \frac{1}{(1+\sigma^2)^2}, \sigma^2 > 0$

This is $f(2,2)$ – $f$ distribution of $(2,2)$ degree of freedom.

> ✔ Verified: $1/(1+\sigma^2)^2$ is exactly the $F(2,2)$ density.

Since $\int_0^\infty \frac{1}{(1+\sigma^2)^2} d\sigma^2 = 1$, so it is proper, but noninformative. *[the words "but noninformative" are hand-underlined]*

> ✔ Verified: $\int_0^\infty (1+u)^{-2}\,du = 1$, so the prior is proper.

*[Figure, hand-drawn in the right margin alongside this paragraph: a vertical axis with "$\infty$" written sideways at its top and a circled "0" at the origin; two monotone decreasing curves fall steeply from near the vertical axis and flatten into long right tails, with "$\infty$" marking the far right end of the horizontal axis. Labels, partly legible: "$\pi(\sigma^2)$" (?) at the left of the axis and "$\pi(\sigma^2) \propto \frac{1}{\sigma^2}$" (?) beside the upper curve. These sketch the proper prior against the improper $1/\sigma^2$ prior.]*

*[margin note, left: "Comments", underlined]*

$y_1, ..., y_n | \mu, \sigma^2 \; iid \; N(\mu, \sigma^2)$

$\pi(\mu, \sigma^2) \propto \frac{1}{\sigma^2}$

Since $\frac{\mu - \bar{y}}{\frac{s}{\sqrt{n}}} \mid \mu \sim t_{n-1}$ (non-Bayesian)

*[a large hand-drawn brace groups the three lines above, with a cursive two-word note beside it, largely illegible — possibly "Low energy" (?)]*

Also $\frac{\mu - \bar{y}}{\frac{s}{\sqrt{n}}} | y \sim t_{n-1}$ (Bayesian)

These have the same mathematical form but the interpretations are different (Bayesian versus non-Bayesian)
*(correction: handwritten "the same" is inserted before "mathematical", which is circled by hand)*

Example

$$X|p \sim Bernoulli(p)$$

$$p \sim Beta(\alpha, \beta)$$

If we let $\alpha = \mu\tau, \beta = (1-\mu)\tau, 0 < \mu < 1, \tau > 0$.

Then we can rewrite the model as:

$$X|p \sim Bernoulli(p)$$

$$p \sim Beta(\mu\tau, (1-\mu)\tau)$$

Construct a shrinkage prior for $\tau$.

The posterior mean of $p$ is $E(p|x) = \lambda x + (1-\lambda)\mu, \lambda = \frac{1}{\tau+1}$

> ⚠ Check could not run (error): Beta–Bernoulli posterior mean is $\lambda x+(1-\lambda)\mu$ with $\lambda=1/(\tau+1)$. — timed out after 90s

Take $\lambda \sim U(0,1)$, so $\frac{1}{\tau+1} \sim U(0,1)$, then by transformation,

$\pi(\tau) = \frac{1}{(1+\tau)^2}, \tau > 0$.

> ✔ Verified: $1/(\tau+1)\sim U(0,1)$ induces $\pi(\tau)=1/(1+\tau)^2$ on $\tau>0$.

### PDF page 33 (booklet page 28)

Hierarchical model

$X_{1i},...,X_{ni}|p\ iid\ Bernoulli(p)$

$p_i \mid \mu,\tau \sim Beta(\mu\tau,(1-\mu)\tau),\ \mu \sim U(0,1)$ *(correction: a handwritten vertical bar and "$\mu,\tau$" are inserted after $p_i$, making the line a conditional statement)*

$\pi(\tau) = \frac{1}{(1+\tau)^2}$

This will be discussed more extensively later.

*[Handwritten work in the right margin, alongside the lines above, partly legible: an earlier expression is heavily scribbled out — [illegible — scribbled out] — followed by "$p = \frac{1}{1+\tau}$"; then a circled "1" and "$\tau = \frac{1-p}{p}$"; then "$p \mid \mu,\tau \sim Beta(\mu\tau(?),\ (1-\mu)\tau(?))$" with an under-brace beneath the two Beta arguments and a short arrow pointing back into them from a small annotation (?). A long sweeping hand-drawn rule closes the block off from the rest of the page. These are lecture scratch notes for the reparametrization $p = 1/(1+\tau)$, under which $\pi(\tau) = (1+\tau)^{-2}$ becomes uniform.]*

> ✔ Verified: under $p = 1/(1+\tau)$ with $\pi(\tau) = (1+\tau)^{-2}$, $p$ is Uniform(0,1), and $\tau = (1-p)/p$

Priors for $p$ in $X|p \sim Bernoulli(p)$, some prior for $p$ is $\pi(p)$. *[the whole sentence is hand-underlined, with a hand-drawn bracket at the left margin]*

Many priors suggested

(1) Jeffreys' prior

$$\pi(p) \propto \frac{1}{\sqrt{p(1-p)}}, 0 < p < 1.$$
$$= p^{-\frac{1}{2}}(1-p)^{-\frac{1}{2}} = p^{\frac{1}{2}-1}(1-p)^{\frac{1}{2}-1}$$

> ⚠ Check FAILED: Jeffreys' prior for Bernoulli($p$) is $\propto 1/\sqrt{p(1-p)}$ — the stated result did not reproduce (see verification log)
> ✔ Verified: $1/\sqrt{p(1-p)} = p^{-1/2}(1-p)^{-1/2} = p^{1/2-1}(1-p)^{1/2-1}$ on $(0,1)$

So it is a Beta distribution.

$p \sim Beta(\frac{1}{2},\frac{1}{2})$

Since $\frac{\Gamma(\frac{1}{2})\Gamma(\frac{1}{2})}{\Gamma(1)} = \pi$

> ✔ Verified: $\Gamma(1/2)\Gamma(1/2)/\Gamma(1) = \pi$

Let $\pi(p) = \frac{1}{\pi\sqrt{p(1-p)}}, 0 < p < 1.$ – arc-sine distribution.

So it is a proper prior.

> ✔ Verified: the arc-sine density $\frac{1}{\pi\sqrt{p(1-p)}}$ integrates to 1 on $(0,1)$

(2) $p \sim U(0,1)$

$p \sim Beta(1,1)$

$$\pi(p) = \begin{cases} 1, & 0 < p < 1 \\ 0, & else \end{cases}$$

Practical view of noninformative prior roughly constant over the range of the likelihood function.

$y_1,...,y_n|p \sim Bernoulli(p)$

$$\pi(p) = \begin{cases} 1, & 0 < p < 1 \\ 0, & else \end{cases}$$

$\pi(p|y) \propto p^s(1-p)^{n-s} \sim Beta(s+1, n-s+1)$

> ⚠ Check FAILED: $p^s(1-p)^{n-s}$ is the $Beta(s+1, n-s+1)$ kernel — the stated result did not reproduce (see verification log)

For small $s, n$ the prior is informative.

(3) Haldane's prior

$\pi(p) \propto \frac{1}{p(1-p)}$, improper.

$\pi(p) \propto \frac{p^s(1-p)^{n-s}}{p(1-p)} = p^{s-1}(1-p)^{n-s-1}, s > 0, n-s > 0$

It is $Beta(s, n-s)$, so it is proper.

> ✔ Verified: Haldane posterior $p^s(1-p)^{n-s}/(p(1-p)) = p^{s-1}(1-p)^{n-s-1}$ is $Beta(s, n-s)$, proper iff $s>0$, $n-s>0$

(4) Zellner's prior

$\pi(p) \propto p^p(1-p)^{1-p}, 0 < p < 1.$

### PDF page 34 (booklet page 29)

**3.3 How to specify the parameters of priors?**

*[margin note beside the heading: "(subjective prior)"]*

Example

$$X_1, ..., X_n \mid p \sim Bernoulli(p)$$

$$p \sim Beta(\mu\tau, (1-\mu)\tau) \;\text{Specify}\; \mu, \tau$$

**Two ways:**
(a) Use $X_1, ..., X_n$ to estimate $\mu$ and $\tau$.
This is not good, because it uses the data twice – "double use".

*[margin notes beside this remark: "(incoherent)"; "Strawderman(?) (1973(?))"; "Natarajan and Kass (2000)"]*

(b) Use other data source (e.g., past survey, census.).
$E(p) = \mu$
$Var(p) = \frac{\mu(1-\mu)}{\tau+1}$

> ⚠ Check FAILED: For p ~ Beta(μτ, (1-μ)τ), E(p) = μ and Var(p) = μ(1-μ)/(τ+1). — the stated result did not reproduce (see verification log)

Scientist says that $p \approx 0.5$ and it ranges $(0.4, 0.6)$
So $\begin{cases} \mu = 0.5 \\ \frac{0.5(1-0.5)}{\tau+1} \approx 0.1 \end{cases}$
So we have $\tau = 1.5$.

> ✔ Verified: 0.5(1-0.5)/(τ+1) = 0.1 implies τ = 1.5.

$\tau$ is like a prior sample size, I would take $\tau \approx 2$
$p \sim Beta(0.5 \times 2, 0.5 \times 2) = Beta(1,1)$

> ⚠ Check could not run (error): With μ = 0.5 and τ = 2, Beta(μτ, (1-μ)τ) = Beta(1,1), the uniform density on (0,1). — SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

Data: $1, 1, 1, 0, 0, 0, 1, 1, 0, 0$
So $\hat{p} = \frac{5}{10} = \frac{1}{2}$

> ✔ Verified: The data 1,1,1,0,0,0,1,1,0,0 give p-hat = 5/10 = 1/2.

$\hat{p} \pm a\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ (scientist specifies this interval)

Example
$X_1, ..., X_n \mid \mu \sim N(\mu, \sigma^2)$
$\mu \sim N(\theta, \delta^2)$

$$\begin{pmatrix} X_1 \\ \vdots \\ X_n \end{pmatrix} \sim N\left\{ \begin{pmatrix} \theta \\ \vdots \\ \theta \end{pmatrix}, \sigma^2 \begin{pmatrix} 1 & & \rho \\ & \ddots & \\ \rho & & 1 \end{pmatrix} \right\}$$

$$\hat{\theta} = \frac{1'\Gamma X}{1'\Gamma 1}, \text{ where } \Gamma = \begin{pmatrix} 1 & & \rho \\ & \ddots & \\ \rho & & 1 \end{pmatrix} \text{ where } \rho = \frac{\delta^2}{\delta^2 + \sigma^2}$$

*(The booklet writes $X$ and $1$ with under-tildes in $\hat\theta$ to indicate vectors. The scan shows $\Gamma$ with no visible inverse exponent in the numerator and denominator; $\Gamma^{-1}$ appears to be intended.)*

> ✔ Verified: Under X_i | mu ~ N(mu, sigma^2) iid and mu ~ N(theta, delta^2), the marginal correlation of X_i and X_j (i != j) is delta^2/(delta^2 + sigma^2).

Can find maximum likelihood estimates to get $\theta$

Elicit information about $\theta$, $\sigma^2$, $\delta^2$.
Administrative data

$$Y_1, ..., Y_n \mid \mu \sim N(\mu, \sigma^2)$$
$$\mu \sim N(\theta, \delta^2)$$

### PDF page 35 (booklet page 30)

$$\begin{pmatrix} Y_1 \\ \vdots \\ Y_n \end{pmatrix} \sim N\left\{ \begin{pmatrix} \theta \\ \vdots \\ \theta \end{pmatrix}, \begin{pmatrix} \sigma^2+\delta^2 & & \delta^2 \\ & \ddots & \\ \delta^2 & & \sigma^2+\delta^2 \end{pmatrix} \right\}$$

*[margin note, right margin (handwritten), underlined header "pairing data(?)", above a two-column table of indices:]*

| | |
|---|---|
| 1 | 1, $\vdots$, n |
| 2 | 1, $\vdots$, n |
| $\vdots$ | |
| n | 1, $\vdots$, n |

*[a long horizontal rule is drawn beneath the table]*

Estimate $\sigma^2$ using $s^2$, $\hat{\sigma}^2 = s^2$

intraclass correlation $\rho = \frac{\delta^2}{\delta^2+\sigma^2}$, $\hat{\rho} = \frac{\delta^2}{\delta^2+s^2}$

> ✔ Verified: For the compound-symmetry covariance $\Gamma_{ii}=\sigma^2+\delta^2$, $\Gamma_{ij}=\delta^2$, the off-diagonal correlation is $\delta^2/(\delta^2+\sigma^2)$.

$$\hat{\theta} = \frac{1'\hat{\Gamma}^{-1}Y}{1'\hat{\Gamma}^{-1}1} = \bar{y} \;\text{(simply)},$$

*(The booklet writes $1$, $Y$ and $\theta$ with under-tildes to indicate vectors.)*

where $\hat{\Gamma} = \begin{pmatrix} \hat{\sigma}^2+\hat{\delta}^2 & & \hat{\delta}^2 \\ & \ddots & \\ \hat{\delta}^2 & & \hat{\sigma}^2+\hat{\delta}^2 \end{pmatrix}$

> ✔ Verified: With $\Gamma=\sigma^2 I+\delta^2 J$, the GLS estimator $(1'\Gamma^{-1}Y)/(1'\Gamma^{-1}1)$ equals $\bar{y}$.

**Proper diffused priors**

*[the heading is hand-underlined, the stroke sweeping into the left margin]*

proper but almost improper.

Example

1. $$\sigma^{-2} \sim \text{Gamma}\left(\frac{a}{2}, \frac{a}{2}\right), \quad a \approx 0.002$$

*(the enumerator "1." is handwritten)*

2. $$\sigma^2 \sim U\left(0, 10^6\right)$$

*(the enumerator "2." is handwritten)*

3. $$Y_1, \ldots, Y_n \mid \mu, \sigma^2 \sim N\left(\mu, \sigma^2\right)$$
$$\mu \sim N\left(\bar{y}, 10^5 s^2\right)$$

*(the enumerator "3" is handwritten)*

**A scale-location family**

$$X_1, ..., X_n \mid \mu, \theta \overset{iid}{\sim} \frac{1}{\sigma} f\left(\frac{x-\mu}{\sigma}\right), -\infty < x < \infty$$

$$\mu : \textit{location}$$

$$\sigma : \textit{scale}$$

$f(y) = \frac{1}{\pi(1+y^2)}$, Cauchy, change $y = \frac{x-\mu}{\sigma}$

$$f(x|\mu,\sigma) = \frac{1}{\sigma\pi\left[1+\left(\frac{x-\mu}{\sigma}\right)^2\right]}$$

> ✔ Verified: The Cauchy scale-location density $\frac{1}{\sigma}f(\frac{x-\mu}{\sigma})$, $f(y)=\frac{1}{\pi(1+y^2)}$, equals the booklet's $f(x\mid\mu,\sigma)$ and integrates to 1.

$f(y) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}y^2}$, $-\infty < y < \infty$

$y = \frac{x-\mu}{\sigma}$

$f(x|\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2\sigma^2}(x-\mu)^2}$, $-\infty < x < \infty$

> ✔ Verified: The normal scale-location density $\frac{1}{\sigma}f(\frac{x-\mu}{\sigma})$, $f(y)=\frac{1}{\sqrt{2\pi}}e^{-y^2/2}$, equals the booklet's $N(\mu,\sigma^2)$ density and integrates to 1.

Our prior is $\pi(\mu, \sigma^2) \propto \frac{1}{\sigma^2}$. *[margin note, handwritten: "( not quite Jeffreys' priors )"]*

### PDF page 36 (booklet page 31)

For any location-scale family we specify $\pi(\mu,\sigma^2) \propto \frac{1}{\sigma^2}$.

Example

$$X_1,...,X_n|\mu,\sigma^2\; iid\; N(\mu,\sigma^2)$$

*(The booklet writes σ² with an under-tilde here.)*

*[left margin note: "$(\bar{x},s^2)$ are jointly sufficient statistics"]*

*[Right-margin handwritten notes, running alongside this example:*
*i. $\bar{x}\mid\mu,\sigma^2 \sim N\left(\mu,\frac{\sigma^2}{n}\right)$*
*ii. $\frac{(n-1)s^2}{\sigma^2}\;\Big|\;\mu,\sigma^2 \sim \chi^2_{n-1} \equiv Gam\left(\frac{n-1}{2},\frac{1}{2}\right)$*
*iii. $\bar{x}$ and $s^2\mid\mu,\sigma^2$ are independent]*

> ✔ Verified: The chi-square density with $n-1$ degrees of freedom equals the Gamma density with shape $(n-1)/2$ and rate $1/2$.

$$\pi(\mu,\sigma^2) \propto \frac{1}{\sigma^2}$$

$$L(\mu,\sigma^2|\bar{x},s^2) = \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} exp\left\{-\frac{1}{2\sigma^2}[(n-1)s^2 + n(\bar{x}-\mu)^2]\right\}$$

> ✔ Verified: Sum-of-squares decomposition $\sum (x_i-\mu)^2 = (n-1)s^2 + n(\bar{x}-\mu)^2$, and the resulting likelihood form.

$$\pi(\mu,\sigma^2|\bar{x},s^2) \propto \left(\frac{1}{\sigma^2}\right)^{\frac{n}{2}+1} exp\left\{-\frac{1}{2\sigma^2}[(n-1)s^2 + n(\bar{x}-\mu)^2]\right\}, -\infty < \mu < \infty, \sigma^2 > 0$$

> ✔ Verified: prior $1/\sigma^2$ times the likelihood is proportional to $(1/\sigma^2)^{n/2+1}\exp\{-\frac{1}{2\sigma^2}[(n-1)s^2+n(\bar x-\mu)^2]\}$, with proportionality constant free of $\mu,\sigma^2$.

$$\pi(\mu|\sigma^2,\bar{x},s^2) \propto exp\left\{-\frac{n}{2\sigma^2}(\bar{x}-\mu)^2\right\}$$

$$\mu|\sigma^2,\bar{x},s^2 \sim N\left(\bar{x},\frac{\sigma^2}{n}\right)$$

> ✔ Verified: $\exp\{-\frac{n}{2\sigma^2}(\bar x-\mu)^2\}$ is the kernel of a $N(\bar x,\sigma^2/n)$ density in $\mu$.

### PDF page 37 (booklet page 32)

We are looking for $\pi(\mu|\bar{x},s^2)$

$$\pi(\mu|\bar{x},s^2) = \int_0^{\infty} \pi(\mu|\sigma^2,\bar{x},s^2)\pi(\sigma^2|\bar{x},s^2)d\sigma^2$$

$$\pi(\sigma^2|\bar{x},s^2) \propto \int_{-\infty}^{\infty} \left(\frac{1}{\sigma^2}\right)^{\frac{n}{2}+1} exp\left\{-\frac{1}{2\sigma^2}[(n-1)s^2 + n(\bar{x}-\mu)^2]\right\}$$

$$\propto \left(\frac{1}{\sigma^2}\right)^{\frac{n}{2}+1} e^{-\frac{1}{2\sigma^2}(n-1)s^2} \int_{-\infty}^{\infty} e^{-\frac{n}{\sigma^2}(\mu-\bar{x})^2}d\mu \quad \text{[sic: the exponent should be } -\tfrac{n}{2\sigma^2}(\mu-\bar{x})^2\text{]}$$

$$\propto \left(\frac{1}{\sigma^2}\right)^{\frac{n}{2}+1}\sqrt{\sigma^2}e^{-\frac{1}{2\sigma^2}(n-1)s^2}$$

> ✔ Verified: The integral $\int_{-\infty}^{\infty} e^{-\frac{n}{2\sigma^2}(\mu-\bar{x})^2}d\mu$ equals $\sqrt{2\pi\sigma^2/n}$, i.e. is proportional to $\sqrt{\sigma^2}$.

$$= \left(\frac{1}{\sigma^2}\right)^{\frac{n+1}{2}} e^{-\frac{1}{2\sigma^2}(n-1)s^2}$$

> ✔ Verified: $(1/\sigma^2)^{n/2+1}\sqrt{\sigma^2} = (1/\sigma^2)^{(n+1)/2}$.

$$\pi(\sigma^2|s^2) \propto \left(\frac{1}{\sigma^2}\right)^{\frac{n-1}{2}+1} e^{-\frac{1}{2\sigma^2}(n-1)s^2} \sim \text{inverse gamma distribution.}$$

$$\sigma^2|s^2 \sim IG\left(\frac{n-1}{2},\frac{(n-1)s^2}{2}\right)$$

> ⚠ Check FAILED: $(1/\sigma^2)^{\frac{n-1}{2}+1}e^{-\frac{(n-1)s^2}{2\sigma^2}}$ is the $IG\!\left(\frac{n-1}{2},\frac{(n-1)s^2}{2}\right)$ kernel, and $\frac{n-1}{2}+1=\frac{n+1}{2}$. — the stated result did not reproduce (see verification log)

*[the "Aside:" heading is circled by hand with a large looping ellipse in pencil, drawn from the left margin; its lower arc passes across the "$X \sim Gamma(\alpha,\beta)$" line below]*

Aside:

$X \sim Gamma(\alpha,\beta)$

$f(x) = \frac{\beta^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}, x \geq 0$

Let $y = \frac{1}{x}$, by transformation,

$f(y) = \frac{\beta^{\alpha}}{\Gamma(\alpha)}\left(\frac{1}{y}\right)^{\alpha+1}e^{-\frac{\beta}{y}}, y > 0$

> ✔ Verified: If $X\sim Gamma(\alpha,\beta)$ with $f(x)=\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}$ and $Y=1/X$, then $f(y)=\frac{\beta^\alpha}{\Gamma(\alpha)}(1/y)^{\alpha+1}e^{-\beta/y}$.

$\sigma^{-2}|y \sim \text{Gam}\left(\frac{n-1}{2},\frac{(n-1)s^2}{2}\right)$

$\sigma^2|y \sim \text{InvGam}\left(\frac{n-1}{2},\frac{(n-1)s^2}{2}\right)$

### PDF page 38 (booklet page 33)

$$\pi(\mu\mid\bar{x}) = \int_0^\infty \frac{1}{\sqrt{2\pi\frac{\sigma^2}{n}}} e^{-\frac{n}{2\sigma^2}(\mu-\bar{x})^2} \left(\frac{1}{\sigma^2}\right)^{\frac{n-1}{2}+1} e^{-\frac{1}{2\sigma^2}(n-1)s^2}\, d\sigma^2$$

$$\propto \int_0^\infty \left(\frac{1}{\sigma^2}\right)^{\frac{n}{2}+1} e^{-\frac{1}{2\sigma^2}\{n(\mu-\bar{x})^2+(n-1)s^2\}}\, d\sigma^2$$

> ✔ Verified: The exponent arithmetic 1/2 + (n-1)/2 + 1 = n/2 + 1.

$$= \frac{1}{\left[\frac{n(\mu-\bar{x})^2+(n-1)s^2}{2}\right]^{\frac{n}{2}}} \int_0^\infty \frac{[n(\mu-\bar{x})^2+(n-1)s^2]^{\frac{n}{2}} \left(\frac{1}{\sigma^2}\right)^{\frac{n}{2}+1} e^{-\frac{1}{2\sigma^2}[n(\mu-\bar{x})^3+(n-1)s^2]}}{\Gamma\!\left(\frac{n}{2}\right)}\, d\sigma^2$$

*(sic: the exponent on $(\mu-\bar{x})$ inside the exponential is printed as $3$; it should be $2$. Also, as printed the numerator carries $[\,n(\mu-\bar x)^2+(n-1)s^2\,]^{n/2}$ rather than $\left[\frac{n(\mu-\bar x)^2+(n-1)s^2}{2}\right]^{n/2}$, so the line is an equality only up to a constant factor.)*

> ✔ Verified: ∫_0^∞ (σ²)^{-(n/2+1)} exp(-A/(2σ²)) dσ² = Γ(n/2) / (A/2)^{n/2}.

$$\propto \frac{1}{[n(\mu-\bar{x})^2+(n-1)s^2]^{\frac{n}{2}}}$$

*[margin note, right of this line: "$\nu = n-1$"]*

$$\propto \frac{1}{\left[1+\frac{n(\mu-\bar{x})^2}{(n-1)s^2}\right]^{\frac{n-1+1}{2}}} \sim t_{n-1}.$$

*[margin note, right of this line: "$\dfrac{\Gamma\!\left(\frac{\nu+1}{2}\right)}{\Gamma\!\left(\frac{\nu}{2}\right)\sqrt{\pi\nu}}$" (?) — the $t_\nu$ normalizing constant; a small stray "✗"-like pen mark sits to its right.]*

> ⚠ Check FAILED: [n(μ-x̄)²+(n-1)s²]^{-n/2} equals [1 + n(μ-x̄)²/((n-1)s²)]^{-(n-1+1)/2} times a constant free of μ. — the stated result did not reproduce (see verification log)

> ✔ Verified: Γ((ν+1)/2)/(Γ(ν/2)√(πν)) normalizes (1+t²/ν)^{-(ν+1)/2} to a density.

Aside: *[the word "Aside:" carries a hand double-underline]*

$W \sim \chi^2_\nu$, chi-square on $\nu$ degrees of freedom.

$$f(w) = \frac{w^{\frac{\nu}{2}-1} e^{-\frac{1}{2}w}}{2^{\frac{\nu}{2}}\Gamma\!\left(\frac{\nu}{2}\right)},\; w \ge 0.$$

$$\text{Let } \frac{w}{2} = T,$$

$$f(t) = \frac{(2t)^{\frac{\nu}{2}-1} e^{-t}}{2^{\frac{\nu}{2}}\Gamma\!\left(\frac{\nu}{2}\right)}|2| = \frac{(t)^{\frac{\nu}{2}-1} e^{-t}}{\Gamma\!\left(\frac{\nu}{2}\right)}$$

$$T \sim Gamma\!\left(\frac{\nu}{2}, 1\right)$$

*[margin note, right of this line: "$\equiv\; W \sim \chi^2_\nu$"]*

> ✔ Verified: With W ~ χ²_ν and T = W/2, f(t) = t^{ν/2-1} e^{-t}/Γ(ν/2), i.e. T ~ Gamma(ν/2, 1).

Look chi-square, put a scale parameter. *[a tiny stray pen tick sits above the end of this line]*
Let $W = \beta X$

$$f(x\mid\beta) = \frac{(\beta x)^{\frac{\nu}{2}-1} e^{-\frac{1}{2}\beta x}}{2^{\frac{\nu}{2}}\Gamma\!\left(\frac{\nu}{2}\right)}\beta = \frac{\beta^{\frac{\nu}{2}} x^{\frac{\nu}{2}-1} e^{-\frac{1}{2}\beta x}}{2^{\frac{\nu}{2}}\Gamma\!\left(\frac{\nu}{2}\right)}$$

$$\frac{1}{2}\beta x \sim Gamma\!\left(\frac{\nu}{2}, 1\right)$$

> ✔ Verified: (βx)^{ν/2-1} e^{-βx/2} β / (2^{ν/2}Γ(ν/2)) = β^{ν/2} x^{ν/2-1} e^{-βx/2} / (2^{ν/2}Γ(ν/2)).

Make another transformation to get $f(x)$.

$$X \sim Gamma\!\left(\frac{\nu}{2}, \frac{\beta}{2}\right)$$

> ✔ Verified: β^{ν/2} x^{ν/2-1} e^{-βx/2} / (2^{ν/2}Γ(ν/2)) is the Gamma(ν/2, β/2) density (rate form b^a x^{a-1} e^{-bx}/Γ(a)).

*[Handwritten work filling the bottom third of the page, in dark pen:*
$$W = \beta X \sim \chi^2_\nu \;\equiv\; Gamma\!\left(\frac{\nu}{2}, \frac{1}{2}\right)$$
*(the $X$ in $\beta X$ appears struck through (?)), and below it, two densities written side by side:*
$$f(x) = \frac{\beta^{\frac{\nu}{2}} x^{\frac{\nu}{2}-1} e^{-\frac{1}{2}\beta x}}{2^{\frac{\nu}{2}}\,\Gamma\!\left(\frac{\nu}{2}\right)}, \quad x > 0
\qquad\qquad
f_W(w) = \frac{w^{\frac{\nu}{2}-1} e^{-\frac{1}{2}w}}{2^{\frac{\nu}{2}}\,\Gamma\!\left(\frac{\nu}{2}\right)}, \quad w > 0$$
*A caret/arrow is drawn under the $f$ on the left. These are lecture scratch notes checking the scale-transformation against the plain chi-square density.]*

> ✔ Verified: The χ²_ν density equals the Gamma(ν/2, 1/2) density (rate parametrization) — the handwritten identity.

### PDF page 39 (booklet page 34)

*[This entire page is handwritten lecture work — there is no typeset body text, only the printed running header. What follows is a best-effort reading of the instructor's blackboard notes, which develop the Cauchy / half-Cauchy prior and transform it to an arcsine (Beta(½, ½)) prior.]*

$$f(x) = \frac{1}{\pi(1+x^2)}$$

*[bracketed remark to the right: "competitive(?) to shrinkage prior"]*

> ✔ Verified: the standard Cauchy density $1/(\pi(1+x^2))$ integrates to 1 over the real line

Location parameter $\to \theta$, $\;-\infty < \theta < \infty$

$$f(\theta) = \frac{1}{\pi(1+\theta^2)}, \qquad -\infty < \theta < \infty$$

Adjusted(?):

$$f(\theta \mid \mu_0, \gamma_0) = \frac{1}{\gamma_0\,\pi\left(1 + \left(\dfrac{\theta-\mu_0}{\gamma_0}\right)^{2}\right)}, \qquad -\infty < \theta < \infty$$

*(the numerator carries a struck-through stray symbol before the "1"; the range $-\infty<\theta<\infty$ is written rotated in the right margin)*

> ✔ Verified: the location-scale Cauchy density with location mu0 and scale gamma0 > 0 integrates to 1

$\sigma^2$ — half Cauchy for $\sigma$

*[circled margin note, right: "Heavy tails"]*

$$\pi(\sigma) = \frac{2}{\pi(1+\sigma^2)}, \qquad 0 < \sigma < \infty$$

> ✔ Verified: the half-Cauchy density 2/(pi(1+sigma^2)) integrates to 1 over (0, oo)

$$\phi = \sigma^2$$
$$\sigma = \sqrt{\phi}$$
$$d\sigma = \frac{1}{2\sqrt{\phi}}\,d\phi$$

$$\pi(\phi) = \frac{\cancel{2}}{\cancel{2}\,\pi\sqrt{\phi}\,(1+\phi)} = \frac{1}{\pi\sqrt{\phi}\,(1+\phi)}, \qquad \phi > 0$$

*(correction: the factor 2 from the half-Cauchy and the 2 in $2\sqrt{\phi}$ are each struck through by hand — they cancel)*

> ✔ Verified: phi = sigma^2 with sigma half-Cauchy has density 1/(pi*sqrt(phi)*(1+phi)) on (0, oo), and it is proper

half Cauchy

*[right-margin scratch work:]* Let $\alpha = \dfrac{1}{1+\phi}$, so $\phi = \dfrac{1-\alpha}{\alpha}$ and $d\phi = \dfrac{-\alpha-(1-\alpha)}{\alpha^{2}}\,d\alpha \;=\; -\dfrac{1}{\alpha^{2}}\,d\alpha$

$$\pi(\alpha) \;=\; \frac{\cancel{\alpha}}{\pi\sqrt{\dfrac{1-\alpha}{\alpha}}}\cdot\frac{1}{\alpha^{2}}$$

$$=\; \frac{1}{\pi\sqrt{\alpha(1-\alpha)}}$$

$$B\!\left(\tfrac{1}{2}, \tfrac{1}{2}\right)$$

> ⚠ Check FAILED: alpha = 1/(1+phi) has density 1/(pi*sqrt(alpha*(1-alpha))) = Beta(1/2,1/2) density, and B(1/2,1/2) = pi — the stated result did not reproduce (see verification log)

arc sine

*[Figure, bottom right: a hand-drawn U-shaped (bathtub) curve — the $\text{Beta}(\tfrac12,\tfrac12)$ / arcsine density — rising to vertical asymptotes at both endpoints of the horizontal axis, which is labelled $\alpha$; the vertical axis is labelled $\pi(\alpha)$; tick marks below the axis are labelled $\tfrac{1}{2}$ and $1$.]*

*[circled note beneath the figure: "symmetry"]*

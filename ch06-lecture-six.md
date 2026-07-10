# Chapter 6 — Lecture Six
*(PDF pages 60–65; booklet pages 55–60)*


### PDF page 60 (booklet page 55)

# Chapter 6 — Lecture Six

1. MC Integration
2. Quadrature
3. Numerical Integration
4. Standard Method
Inverse CDF
5. Grid
6. Accept - reject (Envelope method)
7. ARS, adaptive rejection
Sampling of logconcave densities.
Topics: 1. Hypothesis testing
2. Interval estimation

Hierarchical Bayesian model
Rao Blackwellization
MCMC

**6.1 Rao-Blackwellized Estimation**

$$\pi(\theta \mid y) \;\text{- posterior}$$

*(The booklet writes θ and y with under-tildes to indicate vectors.)*

$$\theta^{(1)}, \theta^{(2)}, ..., \theta^{(M)}, \text{usually, } M \approx 1000 \text{ or } 10000$$

Interest in $\theta_1$, so we want to know $\pi(\theta_1 \mid y)$

$$\theta_1^{(1)}, ..., \theta_1^{(M)}$$

$$\text{So } \widehat{E(\theta_1 \mid y)} = \frac{1}{M} \sum_{h=1}^{M} \theta_1^{(h)}$$

$$\widehat{Var(\theta_1 \mid y)} = \frac{1}{M-1} \sum_{i=1}^{M} (\theta_1^{(i)} - \widehat{E(\theta_1 \mid y)})^2$$

*(The two displayed estimators use different summation indices in the source: $h$ in the mean, $i$ in the variance.)*

### PDF page 61 (booklet page 56)

Credible Interval

<div align="center">

95% CI of $\theta_1$ is:

</div>

$$\underbrace{\left(\theta_1^{(1)} < \ldots\right)}_{2.5\%} \; < \ldots < \; \underbrace{\left(\ldots < \theta_1^{(M)}\right)}_{2.5\%}$$

$$\pi(\theta_1 \mid y) = \int \pi(\theta_1 \mid \theta_{(1)}, y)\,\pi(\theta_{(1)} \mid y)\,d\theta_{(1)}$$

*(The booklet writes $y$ and $\theta_{(1)}$ with under-tildes to indicate vectors.)*

> ✔ Verified: The marginal density $\pi(\theta_1\mid y)=\int \pi(\theta_1\mid\theta_2,y)\pi(\theta_2\mid y)\,d\theta_2$ holds; verified exactly for a bivariate normal posterior with correlation $\rho$.

Suppose $\pi(\theta_1 \mid \theta_{(1)}, y)$ has a simple form.

$$\widehat{\pi(\theta_1 \mid y)} = \frac{1}{M}\sum_{h=1}^{M} \pi\!\left(\theta_1 \mid \theta_{(1)}^{(h)}, y\right)$$

<div align="center">

Rao-Blackwellized kernel density estimator.

</div>

$\widehat{\pi(\theta_1 \mid y)}$ obtained R-B, has smaller mean squared error than estimator than $\pi(\theta_1 \mid y)$ [sic: "than estimator than" — the sentence is garbled in the booklet]

> ✔ Verified: The Rao-Blackwellized estimator has MSE no larger than the un-conditioned one: $\operatorname{Var}(E[\theta_1\mid\theta_2]) \le \operatorname{Var}(\theta_1)$, with both unbiased for $E(\theta_1)$.

$$E(\theta_1 \mid y) = \int E(\theta_1 \mid \theta_{(1)}, y)\,\pi(\theta_{(1)} \mid y)\,d\theta_{(1)}$$

> ✔ Verified: Law of iterated expectation $E(\theta_1\mid y)=\int E(\theta_1\mid\theta_2,y)\,\pi(\theta_2\mid y)\,d\theta_2$, verified exactly for the bivariate normal posterior.

$$\widehat{E(\theta_1 \mid y)} = \frac{1}{M}\sum_{h=1}^{M} \phi\!\left(\theta_{(1)}^{(h)}\right)$$

Example:

$$\pi(\theta_1, \theta_2 \mid y)$$

$$\left(\theta_1^{(1)}, \theta_2^{(1)}\right), \ldots, \left(\theta_1^{(M)}, \theta_2^{(M)}\right)$$

$$\theta_1 \mid \theta_2, y \;\sim\; N\!\left(a_{\theta_2}(y),\, \sigma^2_{\theta_2}(y)\right)$$

$$\widehat{E(\theta_1 \mid y)} = \frac{1}{M}\sum_{h=1}^{M} a_{\theta_2^{(h)}}(y)$$

$$\widehat{\pi(\theta_1 \mid y)} = \frac{1}{M}\sum_{h=1}^{M} \frac{1}{\sqrt{2\pi\sigma^2_{\theta_2^{(h)}}(y)}}\, e^{-\frac{1}{2\sigma^2_{\theta_2^{(h)}}}\left[\theta_1 - a_{\theta_2^{(h)}}(y)\right]^2}$$

> ✔ Verified: The printed summand $\frac{1}{\sqrt{2\pi\sigma^2}}\exp\{-\frac{1}{2\sigma^2}[\theta_1-a]^2\}$ is the $N(a,\sigma^2)$ density: it integrates to 1, has mean $a$ and variance $\sigma^2$.

### PDF page 62 (booklet page 57)

*[Handwritten in the top right margin, above the printed page number, four lines of cursive that are largely illegible: "[illegible] degrades(?) / monotonically(?) / with [illegible] $\theta$". A hand-drawn horizontal rule closes the note off from the text below. These appear to be lecture scratch notes on how ARS behaves as the dimension of $\theta$ grows.]*

**6.2 ARS: Adaptive Rejection Sampling**

*Gilks and Wild (1992)* *[the citation is circled by hand]*

$\pi(\theta \mid x)$ is a logconcave density, use the ARS to draw samples. *(The booklet writes θ and x with under-tildes to indicate vectors.)*

A function is called logconcave if the second derivative of its $log \leq 0$ everywhere. *[a small hand-drawn arrow/caret in the space just above the line points at the "$\leq$" sign]*

We say that a function is unimodal if the second derivative of its $log \leq 0$ only at the mode. *[margin note: "unimodal"]*

So logconcave belongs to the class of unimodal densities. *[a second small hand-drawn arrow/caret to the right of this line points back at the "$\leq$" of the line above]*

If a function is logconcave, then there exists a concave function $h(x)$ , so that *[the phrase "exists a concave function" is hand-underlined]*

$$f(x) = e^{h(x)}$$

*[a large hand-drawn oval in the far right margin, level with this display, encloses a short [illegible] expression]*

So

$$h(x) = \log f(x).$$

Note: The MGF of a logconcave density always exists. *[the words "always exists" are hand-underlined]*

Examples:

1.

$$f(x) = \frac{x^{\alpha-1}e^{-x}}{\Gamma(\alpha)}, x \geq 0$$

$$\log f(x) = (\alpha - 1)\log x - x - \log\Gamma(\alpha)$$

$$\frac{d}{dx}\log f(x) = \frac{\alpha - 1}{x} - 1$$

$$\frac{d^2}{dx^2}\log f(x) = -\frac{\alpha - 1}{x^2}$$

So if $\alpha > 1$, $f(x)$ is logconcave.

> ✔ Verified: Gamma(α,1): first log-derivative is (α−1)/x − 1, second is −(α−1)/x², so logconcave iff α ≥ 1.

*[Handwritten in the left margin beside Example 1, four slanted lines, partly legible: "$f(x)$ concave(?) then(?) / concave / — unimodal". Best reading: "$f(x)$ concave $\Rightarrow$ log-concave $\Rightarrow$ unimodal".]*

*[margin notes, right of Example 1, seven lines closed off by a hand-drawn rule: "Tails of log-concave densities are subexponential" (with "subexponential" hand-underlined); "$X \sim$ logconcave $f(x)$"; "$E\{e^{c|X|}\} < \infty$"; "for some $c > 0$".]*

2.

$$f(x) = \frac{1}{\pi(1 + x^2)}, -\infty < x < \infty$$

Not logconcave

> ✔ Verified: Standard Cauchy is not logconcave: (log f)'' = 2(x²−1)/(1+x²)² > 0 for |x| > 1.

3.

$$\log X \; \sim \; N(0,1)$$

i.e. $X$ has a lognormal density – Not logconcave.

> ✔ Verified: Standard lognormal (log X ~ N(0,1)) is not logconcave: (log f)'' = log(x)/x² > 0 for x > 1.

*[Handwritten in the right margin beside Examples 2 and 3, eight lines of very cramped cursive, partly legible: "(Cauchy &(?) / lognormal) / Because / [illegible] don't(?) / have(?) [illegible] / or [illegible] / $E(X^r)$(?) / not logconcave". These are lecture scratch notes tying the two non-logconcave examples back to the failure of the MGF to exist.]*

4.

$$X \; \sim \; N(\mu, \sigma^2) \text{ is logconcave.}$$

So, if $X$ is lognormal, $\log X$ is logconcave.

> ✔ Verified: N(μ,σ²) is logconcave: (log f)'' = −1/σ² < 0.

5.

$$X \; \sim \; Beta(\alpha, \beta), \alpha, \beta > 1 \text{ is logconcave.}$$

> ⚠ Check FAILED: Beta(α,β) with α,β > 1 is logconcave: (log f)'' = −(α−1)/x² − (β−1)/(1−x)² < 0 on (0,1). — the stated result did not reproduce (see verification log)

### PDF page 63 (booklet page 58)

6.

$$f(x) = 2\phi(x)\Phi(\lambda x)$$

Skewed normal density.

> ✔ Verified: The skew-normal density $f(x)=2\phi(x)\Phi(\lambda x)$ integrates to 1 over the real line.

Note: The product of two logconcave densities is logconcave.

*[margin note, left, beside the two displays below: "normalization constant does not matter"]*

$$g(x) = f_1(x)f_2(x)$$

$$\log g(x) = \log f_1(x) + \log f_2(x)$$

> ✔ Verified: $\log g = \log f_1 + \log f_2$ implies $(\log g)'' = (\log f_1)'' + (\log f_2)''$, so a product of logconcave densities is logconcave.

*[Figure: a concave curve (the graph of $\log f(x)$, labelled $logf(x)$ at the right end) drawn as a dotted/solid arc over a horizontal axis with four tick marks labelled $x_1, x_2, x_3, x_4$. Straight chords through the points $(x_i, h(x_i))$ are drawn: the chords joining consecutive points lie below the curve (the piecewise-linear lower hull), while the chords extended beyond their intervals cross above the curve, forming the piecewise-linear upper envelope with kinks between the tick marks. The two envelopes pinch the curve between them.]*

*[margin note, left of the figure: "piecewise linear in $h(x)$ are piecewise exponential in $f(x)$"]*

*[margin note, right, written sideways: "R[illegible] [illegible] (1999)(?)" — apparently a reference citation]*

*[margin note, left: "support of $f(x)$"]*

$$f(x) = e^{h(x)}$$

$$S_n = \{x_0, x_1, ..., x_{n+1}\}$$

$L_{i,i+1}(x)$ is the straight line through $(x_i, h(x_i))$ and $(x_{i+1}, h(x_{i+1}))$

$$\text{For } x \in (x_i, x_{i+1})$$

$$\overline{h_n(x)} = \min\{L_{i-1,i}(x), L_{i+1,i+2}(x)\}$$

$$\underline{h_n(x)} = L_{i,i+1}(x)$$

Envelope are $\underline{h_n(x)} \le h(x) \le \overline{h_n(x)}$ uniform on the support. *(correction: "and" is struck through and replaced by handwritten "are")*

> ✔ Verified: For concave $h$, the interior chord is a lower bound and the two neighbouring extended chords are each an upper bound on $(x_i,x_{i+1})$.

Define

$$\underline{h_n(x)} = -\infty$$

$$\overline{h_n(x)} = \min\{L_{0,1}(x), L_{n,n+1}(x)\} \text{ on } (x_0, x_{n+1})^c$$

$$\underline{f_n(x)} = exp\{\underline{h_n(x)}\}$$ *[an uncertain handwritten label "$A_0$"(?) sits in the left margin at this line; the printed "$exp\{\underline{h_n(x)}\}$" carries a hand-drawn wavy underline]*

$$\overline{f_n(x)} = exp\{\overline{h_n(x)}\}$$

mean(?) that *(correction: the printed "We have" is struck through and replaced by handwritten "mean(s)(?) that")*

*[margin note, bottom left: "approximate"(?)]*

$\underline{f_n(x)} \le f(x) \le \overline{f_n(x)} = \overline{w_n}g_n(x)$, where $\overline{w_n}$ is the normalization constant for $\overline{f_n}$.

(i.e. $g_n$ is a density.)

### PDF page 64 (booklet page 59)

**ARS:**

Initialize $n$ and $S_n$ *(correction: the printed subscripted symbol is overwritten by hand with "$S_n$")*

1. Generate $X \sim g_n(x)$, $U \sim U(0,1)$

2. If $U \leq \dfrac{f_n(x)}{\bar{w}_n g_n(x)}$, accept $x$.

Otherwise, if $U \leq \dfrac{f(x)}{\bar{w}_n g_n(x)}$, accept $x$.

Update $S_n$ to $S_{n+1} = S_n \bigcup \{x\}$ if $x$ is rejected.

$$y = \alpha_i x + \beta_i$$

$r_n$ denote the number of segments.

$$\bar{w}_n = \frac{e^{\alpha_{-1}x_0 + \beta_{-1}}}{\alpha_{-1}} + \sum_{i=0}^{n} e^{\beta_i}\left[\frac{e^{\alpha_i x_{i+1}} - e^{\alpha_i x_i}}{\alpha_i}\right] - \frac{e^{\alpha_{r_n} x_{n+1}}}{\alpha_{r_n+1}}$$

> ✔ Verified: The interior-segment integral of the piecewise-exponential envelope is $e^{\beta_i}(e^{\alpha_i x_{i+1}} - e^{\alpha_i x_i})/\alpha_i$.

> ✔ Verified: The left-tail integral of the envelope is $e^{\alpha_{-1} x_0 + \beta_{-1}}/\alpha_{-1}$ when $\alpha_{-1} > 0$.

1. Select $(x_i, x_{i+1})$ with probability $e^{\beta_i}\left(\dfrac{e^{\alpha_i x_{i+1}} - e^{\alpha_i x_i}}{\bar{w}_n \alpha_i}\right), i = 1, ..., r_n$

2. Generate $U \sim U(0,1)$
$U = \alpha_i^{-1} log\left[e^{\alpha_i x_i} + U e^{\alpha_i x_{i+1}} - e^{\alpha_i x_i}\right]$ $\text{[sic: the parentheses are missing; the inverse-CDF draw is } \alpha_i^{-1}\log\left(e^{\alpha_i x_i} + U\left(e^{\alpha_i x_{i+1}} - e^{\alpha_i x_i}\right)\right)\text{, and the symbol } U \text{ is reused for both the uniform and the returned draw]}$

> ✔ Verified: Inverting the truncated-exponential CDF on $(x_i, x_{i+1})$ yields $x = \alpha_i^{-1}\log\!\left(e^{\alpha_i x_i} + U(e^{\alpha_i x_{i+1}} - e^{\alpha_i x_i})\right)$, and this lies in $[x_i, x_{i+1}]$ for $U \in [0,1]$.

*[Figure, hand-drawn in the upper right: a concave curve $h(x)$ (?) with three straight tangent lines drawn at abscissae $x_1$, $x_2$, $x_3$, meeting above the curve to form a piecewise-linear upper hull; short vertical drop-lines run from the tangent intersections to the horizontal axis, which is labelled $x_1\ x_2\ x_3$ and, at its right end, $x$. This is the standard picture of the tangent envelope to the log-density used by adaptive rejection sampling.]*

*[margin note, below the figure: "Gilks and Wild (1992)"]*

*[Handwritten note across the middle of the page, sprawling and partly illegible: "General purpose, in specific situations one might(?) be better just using the ARS." The clause "specific situations one might" is written above and to the right of the rest, so the intended word order is uncertain.]*

*[Handwritten note: "You don't want to code this!"]*

*[Handwritten note: "— Download MCMCpack", with a caret insertion between "MC" and "pack"; below, indented: "ars".]*

---

*[Handwritten R code, ruled off below a hand-drawn horizontal line; this is the example from the `ars` package documentation:]*

```r
library(MCMCpack)
library(ars)
f <- function(x, mu=0, sigma=1) {-1/(2*sigma^2)*(x-mu)^2}
fprima <- function(x, mu=0, sigma=1) {-1/(sigma^2)*(x-mu)}
mysample <- ars(10000, f, fprima, mu=0, sigma=1)
```

*(correction: in the `fprima` line the "$2$" of "`(2*sigma^2)`" is struck through by hand, giving `-1/(sigma^2)*(x-mu)` — the correct derivative of `f`. In the `f` line a symbol immediately after the opening brace is struck through/overwritten, and a small caret sits above `sigma^2`; the surviving reading is as transcribed. A further caret/arrow "^" appears at the right of the code block with no legible attached text.)*

### PDF page 65 (booklet page 60)

*(Blank page — running header only.)*

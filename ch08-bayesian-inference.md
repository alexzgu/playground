# Chapter 8 — BAYESIAN INFERENCE
*(PDF pages 70–87; booklet pages 65–82)*


### PDF page 70 (booklet page 65)

# Chapter 8 — BAYESIAN INFERENCE

**8.1 Interval Estimation**

It is usually difficult to present the entire posterior density. Typically a measure of center and a measure of spread (e.g. posterior mean and standard deviation) are used. But this is somewhat non-Bayesian at least for asymmetric posterior densities. Why?

Suppose the posterior density for $\theta$ is the following:

$$\theta|y \quad \sim \quad \mathcal{N}\big(\mathbb{E}(\theta|y), (\,\text{std}(\theta|y))^2\big),$$

then a very good 95% *credible* interval for $\theta$ is

$$\mathbb{E}(\theta|y) \pm 1.96\,\text{std}(\theta|y).$$

> ✔ Verified: For a normal posterior, $\mu \pm 1.96\,\sigma$ carries probability 0.95 to the printed precision (i.e. $\Phi(1.96)-\Phi(-1.96)=0.9500$ to 4 decimals), and 1.96 is the correct rounded 0.975 quantile.

For Basyesians [sic] the word *credible* replaces the word *confidence*. We talk about a 95% *credible interval* instead of a 95% *confidence interval*.

`Note:` Throughout we assume that all posterior densities are continuous.

**8.1.1 Credible Interval**

**Definition.** Let $0 \le \alpha \le 1$, typically $\alpha = 0.05$, an interval $(a,b)$ is called a $100(1-\alpha)\%$ *credible interval* if its posterior probability content is $1-\alpha$, i.e.

$$\int_a^b p(\theta|y)d\theta = 1 - \alpha.$$

See Figure 1.

`Remark (1):` Credible intervals are not unique.
`Remark (2):` Credible intervals are easy to construct.

Typically we use credible interval with equal tail probabilities to their left and their right. For a $100(1-\alpha)\%$ credible interval, there is $\frac{\alpha}{2}100\%$ probability in each tail.
See Figure 2.

There are two ways to construct credible intervals.

### PDF page 71 (booklet page 66)

*[Figure 8.1: a smooth right-skewed density curve labeled $p(\theta\mid y)$ over a horizontal $\theta$-axis. Beneath the curve two nested horizontal intervals with end-bars are drawn: an inner one labeled $l_1$ and a wider outer one labeled $l_2$, both spanning the bulk of the density.]*

**Figure 8.1: Credible Interval**

*[Figure 8.2: a smooth, roughly bell-shaped density curve labeled $p(\theta\mid y)$ over a horizontal $\theta$-axis. Two vertical dashed lines cut the curve, one on each side of the mode, delimiting a central region. The left tail area is labeled $\frac{\alpha}{2}$ (with a short pointer into the left tail) and the right tail area is labeled $\frac{\alpha}{2}$ (with an arrow pointing into the right tail).]*

**Figure 8.2: Credible Interval with Equal Tail**

- **Method I: Numerical**

  Let

  $$F(\theta|r) = \int_{-\infty}^{\theta} f(t|y)dt$$

  $\text{[sic: the conditioning symbol should be } y\text{, i.e. } F(\theta\mid y)\text{]}$

  be the *cumuulative* [sic] *distribution function* (C.D.F.). Then

  $$a = F^{-1}\left(\frac{\alpha}{2}\Big|y\right) \quad \text{and} \quad b = F^{-1}\left(1 - \frac{\alpha}{2}\Big|y\right)$$

  give the $100(1-\alpha)\%$ credible interval $(a,b)$. Here $F^{-1}(\cdot|y)$ is the inverse C.D.F.

  > ✔ Verified: Equal-tail inversion of the C.D.F. gives probability content exactly $1-\alpha$: for a posterior with c.d.f. $F$, $\int_{F^{-1}(\alpha/2)}^{F^{-1}(1-\alpha/2)} f(t)\,dt = 1-\alpha$.

- **Method II: Sampling based**

  Draw a sample of 1000 values from $f(\theta|y)$. Order the values

  $$\theta^{(1)} < \theta^{(2)} < ...\theta^{(1000)},$$

  then an estimate of the 95% credible interval is

  $$\left(\theta^{(25)}, \theta^{(975)}\right).$$

  > ✔ Verified: With $n=1000$ ordered draws, indices 25 and 975 are the $0.025$ and $0.975$ empirical quantiles and span 95% of the sample.

  This method is usually used in complex problems.

## 8.1.2 Highest Posterior Density (H.P.D) Interval

Not only should we be concerned with the probability content of the interval, but we wish to use the interval with the highest posterior density.

### PDF page 72 (booklet page 67)

**Definition.** A $100(1-\alpha)\%$ credible interval $(a,b)$ is a *H.P.D. interval* if for any $\theta_1 \in (a,b)$ and $\theta_2 \notin (a,b)$

$$p(\theta_1|y) \geq p(\theta_2|y).$$

See Figure 3.

*[Figure: a right-skewed unimodal density $p(\theta|y)$ drawn over a horizontal $\theta$-axis. Two dashed vertical lines drop from the curve to the axis, marking the endpoints of an interval; a double-headed arrow beneath the axis spans them and is labelled $I$. Inside the interval, a vertical arrow drops from the curve at $\theta_1$ to the axis, labelled $p(\theta_1|y)$; outside the interval, in the right tail, a shorter vertical arrow drops from the curve at $\theta_2$ to the axis, labelled $p(\theta_2|y)$. The axis is labelled $\theta$ at the far right, with tick labels $\theta_1$ and $\theta_2$.]*

Figure 8.3: HPD Interval

Equivalently,

$$\{\theta : p(\theta|y) \geqslant C_\alpha\}$$

Remark (1) : All candidate intervals must contain the mode.
Remark (2) : The $100(1-\alpha)\%$ H.P.D. interval is unique for any unimodal posterior density.
Remark (3) : If the mode is on a boundary of the posterior density, then that boundary is one of end points [sic] of the interval.

**Theorem 8.1.1.** For a unimodal posterior density the $100(1-\alpha)\%$ H.P.D. interval is obtained by solving the following two equations

$$\int_a^b p(\theta|y)d\theta = 1-\alpha \tag{8.1}$$

$$p(a|y) = p(b|y) \tag{8.2}$$

> ✔ Verified: On the unimodal Beta(2,3) posterior with 1−α=0.9, the (a,b) solving ∫_a^b p = 0.9 and p(a)=p(b) satisfies the HPD property (min density inside ≥ max density outside), equals the level set {θ: p(θ) ≥ p(a)}, and is shorter than the equal-tailed 90% interval.

> ✔ Verified: The 90% HPD interval for Beta(2,3) contains the mode (Remark (1)).

for $a$ and $b$.

*Proof.* Straightforward.

First equation (1.1) [sic: should be (8.1)] states that the interval is a $100(1-\alpha)\%$ credible interval. Second equation (1.2)states [sic: missing space; should be (8.2)] that the interval has the highest posterior density (probability) among all $100(1-\alpha)\%$ credible intervals (equal ordinates condition). $\square$

Geometric interpretation slide horizontal line up and down. See Figure 4.

### PDF page 73 (booklet page 68)

*[Figure 8.4: a unimodal, right-skewed posterior density $p(\theta\mid y)$ drawn over a horizontal $\theta$-axis. A dotted horizontal line ("horizontal line") cuts the curve at two points, labelled $p(a\mid y)$ on the left branch and $p(b\mid y)$ on the right branch; dashed vertical drop-lines from these two points meet the axis at $a$ and $b$. An arrow labelled $1-\alpha$ points into the region under the curve between $a$ and $b$.]*

Figure 8.4: HPD Interval with Horizontal Line

**Computation**

$f(\theta|y)$ is a unimodal posterior density; mode is not in the boundary.

$$f(a|y) = f(b|y) \tag{8.3}$$

$$F(b|y) - F(a|y) = \int_a^b f(\theta|y)d\theta = 1 - \alpha \tag{8.4}$$

> ✔ Verified: Equation (8.4) — $F(b\mid y)-F(a\mid y)=\int_a^b f(\theta\mid y)\,d\theta$ holds as an identity for a posterior density with CDF $F$, so the displayed chain equating both to $1-\alpha$ is consistent.

Solve for a:

$$f(a|y) = f\left[F^{-1}\{F(a) + (1-\alpha)\}\right]$$

> ✔ Verified: The displayed "Solve for a" equation — with $b=F^{-1}\{F(a)+(1-\alpha)\}$ the coverage constraint (8.4) holds identically, so (8.3)+(8.4) reduce to $f(a\mid y)=f[F^{-1}\{F(a)+(1-\alpha)\}]$ in the single unknown $a$.

use a numerical routine (e.g. bisection method) start with $(a,b)$ for a credible interval. See Figure 5.

*[Figure 8.5: a symmetric, bell-shaped density $p(\theta|y)$ over a horizontal $\theta$-axis. A dotted horizontal line ("horizontal line") meets the curve at $p(a|y)$ on the left and $p(b|y)$ on the right, with dashed vertical drop-lines to $a$ and $b$ on the axis. An arrow labelled $1-\alpha$ points into the central region under the curve. Two further arrows, labelled $\frac{\alpha}{2}$ on the far left and $\frac{\alpha}{2}$ on the far right, point into the two tail regions outside $a$ and $b$.]*

Figure 8.5: Symmetric Distribution

`Remark:` (Symmetric densities) $m = mode$, the $100(1-\alpha)\%$ H.P.D. interval is $(m-a, m+a)$ where $a$ is given by

$$\int_m^{m+a} f(\theta|y)d\theta = \frac{1-\alpha}{2}.$$

> ✔ Verified: The Remark — for a density symmetric about its mode $m$, $(m-a,m+a)$ satisfies the equal-ordinate condition (8.3), and it is the $100(1-\alpha)\%$ HPD interval exactly when $\int_m^{m+a} f(\theta\mid y)\,d\theta=(1-\alpha)/2$.

**Examples**

1. Normal Model

*[a short faint wavy stroke runs beneath "1. Normal Model" in the left margin; it carries no legible content and may be show-through from the reverse leaf rather than an intentional mark (?)]*

### PDF page 74 (booklet page 69)

$$
\begin{aligned}
X_1,\dots X_n \mid \mu,\sigma^2 \;&\sim\; \mathcal{N}(\mu,\sigma^2)\\[2pt]
p(\mu,\sigma^2) \;&\propto\; \frac{1}{\sigma^2}\\[2pt]
\text{Bayesian}:\; \frac{\mu-\overline{x}}{s/\sqrt{n}}\,\Big|\,\underset{\sim}{x} \;&\sim\; t_{n-1}\\[2pt]
\text{Non-Bayesian}:\; \frac{\mu-\overline{x}}{s/\sqrt{n}}\,\Big|\,\underset{\sim}{x} \;&\sim\; t_{n-1}
\end{aligned}
$$

*(The booklet writes $x$ with an under-tilde to indicate a vector.)*

> ✔ Verified: Under the reference prior $p(\mu,\sigma^2)\propto\sigma^{-2}$, the marginal posterior of $t=(\mu-\bar x)/(s/\sqrt n)$ is Student-$t$ with $n-1$ df (checked exactly at $n=5$).

*[Handwritten work in the right margin, alongside the display above, mostly illegible: an expression `$f(\mu\mid\underset{\sim}{x})$`(?) with a `1`(?) beside it, set over a long fraction bar; beneath the bar `$\int f(\bar{x}\mid\mu)$`(?), with a large `$\int$` sign and `$d\mu$`(?) to the right; a final unattached squiggle below. [illegible]. The layout suggests a statement of Bayes' rule for $\mu$ under the flat prior, i.e. numerator likelihood times $1$, denominator the integral of the likelihood over $\mu$.]*

A $100(1-\alpha)\%$ H.P.D. (confidence) interval for $\mu$ is

$$
\bar{x} \pm \frac{s}{\sqrt{n}}\,t_{n-1,\frac{\alpha}{2}}.
$$

Illustrative Example: 60 young white males from middlesex, MA

$$
\begin{aligned}
\text{BMI}:\;\; \text{avg} \;&=\; 20.38 \qquad \text{std} \;=\; 5.24\\
t_{59,0.025} \;&=\; 2.0003 \;\text{[sic: } t_{59,0.025}=2.0010\text{; the printed }2.0003\text{ is } t_{60,0.025}\text{]} \qquad \text{Interval } (19.03, 21.73)
\end{aligned}
$$

*[sic: the true upper 2.5% point of $t_{59}$ is $2.0010$ to 4 dp; $2.0003$ is the 60-df value. The interval $(19.03, 21.73)$ is unaffected at 2 dp.]*

> ⚠ Check FAILED: $t_{59,0.025} = 2.0003$ (upper 2.5% point of Student-$t$ with 59 df), to 4 dp. — the stated result did not reproduce (see verification log)

> ✔ Verified: $20.38 \pm (5.24/\sqrt{60})\cdot 2.0003 = (19.03, 21.73)$ rounded to 2 dp.

Remark:

$$
\begin{aligned}
\text{Bayesian}\;\;&:\; Pr(19.03 \le \mu \le 21.73 \mid y) = 0.95\\
\text{Non-Bayesian}\;\;&:\; Pr(19.03 \le \mu \le 21.73 \mid y) \overset{??}{=} 0.95 \text{ is meaningless.}
\end{aligned}
$$

2. Binomial Model

$$
\begin{aligned}
x\mid p \;&\sim\; \text{Binomial } (n,p)\\
p \;&\sim\; \text{Beta } (\mu\tau, (1-\mu)\tau)\\
p\mid x = s \;&\sim\; \text{Beta } (s+\mu\tau,\; n-s+(1-\mu)\tau); \quad s = \#\text{ of sucesses [sic]}
\end{aligned}
$$

> ✔ Verified: Beta–Binomial conjugacy: with $p\sim\text{Beta}(\mu\tau,(1-\mu)\tau)$ and $x\mid p\sim\text{Bin}(n,p)$, the posterior at $x=s$ is $\text{Beta}(s+\mu\tau,\ n-s+(1-\mu)\tau)$.

NHIS data: $DE(1), DC(2)$ &nbsp;&nbsp; $\mu = 0.3, \tau = 100$

$$
\begin{aligned}
p_1\mid x_1 &\sim \text{Beta } (67,133) \text{ and independently}\\
p_2\mid x_2 &\sim \text{Beta } (61,136).
\end{aligned}
$$

> ✔ Verified: With $\mu=0.3,\tau=100$, $\text{Beta}(67,133)$ forces $(n,s)=(100,37)$ and $\text{Beta}(61,136)$ forces $(n,s)=(97,31)$.

<div align="center">95% Credible Interval</div>

|  | 1000 | 10000 | Numerical | 95% H.P.D. |
|---|---|---|---|---|
| $p_1$ | $(0.269, 0.400)$ | $(0.272, 0.401)$ | $(0.271, 0.402)$ | $(0.270, 0.401)$ |
| $p_2$ | $(0.249, 0.374)$ | $(0.248, 0.376)$ | $(0.247, 0.376)$ | $(0.246, 0.375)$ *[sic]* |
| $p_2 - p_1$ | $(-0.112, 0.067)$ | $(-0.115, 0.066)$ | | |

*[sic: the exact 95% H.P.D. interval for $\text{Beta}(61,136)$ is $(0.24592, 0.37445)$, i.e. $(0.246, 0.374)$ to 3 dp — the printed upper endpoint $0.375$ is off by one in the last digit.]*

> ✔ Verified: Equal-tailed 95% intervals: $\text{Beta}(67,133)\to(0.271,0.402)$; $\text{Beta}(61,136)\to(0.247,0.376)$, to 3 dp.

> ⚠ Check FAILED: 95% HPD intervals: $\text{Beta}(67,133)\to(0.270,0.401)$; $\text{Beta}(61,136)\to(0.246,0.375)$, to 3 dp. — the stated result did not reproduce (see verification log)

### PDF page 75 (booklet page 70)

$$\begin{aligned}
\text{Artificial example}\;&:\; p\mid x \;\sim\; \text{Beta}(5,500)\\
\text{Numerical}\;&:\; (3.23\times 10^{-3},\, 20.20\times 10^{-3})\\
\text{H.P.D. Interval}\;&:\; (2.42\times 10^{-3},\, 18.62\times 10^{-3}).
\end{aligned}$$

*[sic: the printed lower H.P.D. endpoint is slightly off — the exact 95% H.P.D. interval of Beta(5,500) is $(2.4127\times10^{-3},\,18.6213\times10^{-3})$, so to the printed precision the lower endpoint should be $2.41\times10^{-3}$]*

> ✔ Verified: Beta(5,500) equal-tailed 95% credible interval is (3.23e-3, 20.20e-3) to printed precision.

> ⚠ Check FAILED: Beta(5,500) 95% H.P.D. interval is (2.42e-3, 18.62e-3) to printed precision. — the stated result did not reproduce (see verification log)

3. Poisson Model

*[A long hand-drawn curved rule sweeps rightward beneath this heading, toward the display below.]*

$$\begin{aligned}
x\mid\lambda \;&\sim\; \text{Poisson}(\mu\lambda)\\
p(\lambda) &= 1\\
\lambda\mid x \;&\sim\; \Gamma(x+1, n)
\end{aligned}$$

> ✔ Verified: Poisson(n*lambda) likelihood with flat prior p(lambda)=1 yields posterior Gamma(x+1, rate n).

Homicide data: White males, teenagers and young adults, 15-24 years old

$$\begin{aligned}
91-93(1)\quad & \lambda_1\mid x_1 \sim \text{Gamma}(16, 150269)\\
94-96(2)\quad & \lambda_2\mid x_2 \sim \text{Gamma}(10, 133118),\ \text{independent.}
\end{aligned}$$

<div align="center">

95% Credible Interval

</div>

|  | 1000 | 10000 | Numerical | 95% H.P.D. |
|---|---|---|---|---|
| $\lambda_1\ (\times 10^{-5})$ | $(6.322, 17.301)$ | $(6.129, 16.491)$ | $(6.086, 16.464)$ | $(6.501, 17.968)$ |
| $\lambda_2\ (\times 10^{-5})$ | $(3.618, 13.098)$ | $(3.551, 2.906)$ [sic] | $(3.602, 12.834)$ | $(3.880, 13.888)$ |
| $\frac{\lambda_2}{\lambda_1}$ | $(0.295, 1.484)$ | $(0.300, 1.529)$ |  |  |

*(The booklet writes $\theta$, $\lambda$ with under-tildes to indicate vectors.)*

*[sic: the "95% H.P.D." column cannot be correct — both printed intervals are wider than, and shifted right of, the corresponding equal-tailed "Numerical" intervals, whereas an H.P.D. interval is by definition the shortest 95% interval. The true 95% H.P.D. intervals are approximately $(5.725,\,15.957)\times10^{-5}$ for $\lambda_1\sim\text{Gamma}(16,150269)$ and $(3.224,\,12.247)\times10^{-5}$ for $\lambda_2\sim\text{Gamma}(10,133118)$]*

> ✔ Verified: Gamma(16, rate 150269) equal-tailed 95% interval is (6.086e-5, 16.464e-5) to printed precision.

> ✔ Verified: Gamma(10, rate 133118) equal-tailed 95% interval is (3.602e-5, 12.834e-5) to printed precision.

> ⚠ Check FAILED: Gamma(16, rate 150269) 95% H.P.D. interval is (6.501e-5, 17.968e-5) to printed precision. — the stated result did not reproduce (see verification log)

> ⚠ Check FAILED: Gamma(10, rate 133118) 95% H.P.D. interval is (3.880e-5, 13.888e-5) to printed precision. — the stated result did not reproduce (see verification log)

**H.P.D. (Empirical Methods)**

$\pi(\theta\mid x)$ unimodal, have a sample $\theta_1, \ldots \theta_M$, want 95% H.P.D. interval.

Chen and Shao (1999), *Monte Carlo Estimation of Bayesian Credible and H.P.D. Intervals*, JCGS, 69-92

1. Order $\theta_1, \ldots \theta_M$ to get $\theta_{(1)}, \ldots \theta_{(M)}$;

2. $\tilde{M} = \lfloor 0.95M \rfloor$.

   *[margin note, written sideways in the left margin beside steps 1–2: "floor" (?) — glossing the floor brackets]*

3. Compute the $M - \tilde{M}$ 95% Credible Interval $\left(\theta_{(s)}, \theta_{(\tilde{M}+s)}\right), s = 1, \ldots, M - \tilde{M}$.

   *(a handwritten symbol — "$\mu$"(?) or an insertion caret — is squeezed in above the line just after "$M-\tilde{M}$", together with a double-slash "//" deletion mark; the intended edit is illegible)*

4. Find the shortest interval among the $M - \tilde{M}$ intervals, this is the H.P.D. interval. Of course, a not so optimal credible interval is given by $\left(\theta_{(0.25M)}, \theta_{(0.976M)}\right)$. \text{[sic: the quantile indices should presumably be $0.025M$ and $0.975M$]}

**Remarks**

(1) H.P.D. intervals are desirable.

(2) H.P.D. intervals may be difficult to compute. Credible intervals can be easily obtained from the output of a sampling-based method. *(correction: the printed lowercase "c" of "credible" is overwritten by a handwritten capital "C")*

### PDF page 76 (booklet page 71)

(3) For multimodal densities the construction for H.P.D. intervals (set of intervals) seems to be an open problem. But it can be done.

(4) H.P.D. regions can be constructed for multi-dimensional parameters. For a d-variate normal posterior density, the H.P.D. region is an ellipsoid.

> ✔ Verified: For a d-variate normal density, the level set {f ≥ k} is the ellipsoid {(θ−θ̂)′Σ⁻¹(θ−θ̂) ≤ c} with c = −2·log(k·(2π)^{d/2}·|Σ|^{1/2}).

Recommendation: present H.P.D. intervals when you can, otherwise present a credible interval with equal-tailed probabilities.

*[Handwritten work sprawling across the right margin, much of it written sideways and only partly legible: $1-\alpha \;=\; \int \cdots \dfrac{1}{|2\pi\Sigma|^{1/2}}\, e^{-\frac{1}{2}(\theta-\hat\theta)'\Sigma^{-1}(\theta-\hat\theta)}\, d\theta$ (?), a large brace, and $\ge c$ (?); then below, more clearly, $(\theta-\hat\theta)'\,\Sigma^{-1}\,(\theta-\hat\theta)$, followed by $\le \chi^2_{[\text{illegible}]}$ (?) and $-\frac{1}{2}\big[\;$[illegible]$\;\big]$. These are lecture scratch notes deriving the ellipsoidal H.P.D. region of item (4).]*

**8.2 Hypothesis-Testing**

Bayesian think of hypotheses as models e.g.

- Non-Bayesian

$$X_1, X_2, \dots X_n \overset{iid.}{\sim} \mathcal{N}(\mu, \sigma^2)$$

  assume $\sigma^2$ is known; inference about $\mu$

$$H_0 : \mu = \mu_0 \quad \text{vs.} \quad H_1 : \mu = \mu_1.$$

- Bayesian

$$X_1, X_2, \dots X_n \mid \mu \overset{iid.}{\sim} \mathcal{N}(\mu, \sigma^2)$$

  assume $\sigma^2$ is known; inference about $\mu$

$$
\begin{aligned}
M_1 : \quad & X_1, X_2, \dots X_n \overset{iid.}{\sim} \mathcal{N}(\mu_0, \sigma^2)\\
M_2 : \quad & X_1, X_2, \dots X_n \overset{iid.}{\sim} \mathcal{N}(\mu_1, \sigma^2)
\end{aligned}
$$

`Remark (1):` $M_1$ and $M_2$ are symmetric.
`Remark (2):` Bayesians put a "lump" of probability on point hypotheses. *[the word "lump" is underlined by hand with a wavy stroke]*

Example:
&nbsp;&nbsp;&nbsp;&nbsp;Body mass index of young white males, Middlesex, MA.

$$n = 60,\; \bar{x} = 20.38,\; s = 5.22,\; \mu_0 = 22,\; \sigma^2 = s^2$$

*(correction: the printed symbol "$\mu$" in "$\mu = 60$" is struck through and replaced by handwritten "$n$")*

$$H_0 : \mu = \mu_0 \quad \text{vs.} \quad H_1 : \mu = \mu_1 \;(\mu_1 \ge 22).$$

Ratio of likelihoods is

$$e^{-\frac{n}{\sigma^2}\left(\bar{x} - \frac{\mu_0 + \mu_1}{2}\right)(\mu_1 - \mu_0)},$$

*(correction: the printed numerator of the exponent's fraction reads "$\mu$"; a handwritten "$n$" is written above it)*

> ✔ Verified: Ratio of normal likelihoods L(mu0)/L(mu1) equals exp[-(n/sigma^2)(xbar-(mu0+mu1)/2)(mu1-mu0)].

Neyman-Pearson Lemma:
Reject $H_0$ if the ratio of likelihood is small $=$ Reject $H_0$ if $\bar{x}$ is large. *[the clause "the ratio of likelihood is small" is hand-underlined, with a stroke through the word "of"]*

$$
\begin{aligned}
\text{p-value} \;&=\; Pr(\bar{X} > \bar{x} \mid \mu = \mu_0)\\
&=\; 1 - \Phi\!\left(\frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}\right)
\end{aligned}
$$

> ✔ Verified: Under H0, Pr(Xbar > xbar) = 1 - Phi((xbar-mu0)/(sigma/sqrt(n))).

*[margin note, bottom left: "$H_0$" written above "$H_1$"]*

### PDF page 77 (booklet page 72)

$$\text{p-value} = 0.992$$

| $\mu_1$ | log(ratio) | ratio |
|---|---|---|
| 22 | 0 | 1 |
| 23 | 4.67 | 107 |
| 24 | 11.53 | $10^5$ |
| 25 | 20.61 | $8.9 \times 10^8$ |
| 26 | 31.88 | $7.0 \times 10^13$ *[sic: typeset as $10^1 3$ — only the "1" is raised; the second table below prints $10^{13}$]* |
| 27 | 45.36 | $5.0 \times 10^19$ *[sic: typeset as $10^1 9$; the second table below prints $10^{19}$]* |

> ✔ Verified: exp(log(ratio)) reproduces each printed ratio to the precision printed

`Remark (1):` The p-value is not a function of $\mu_1$

`Remark (2):` As $\mu_1$ increases there is stronger evidence for $H_0$.

`Remark (3):` The ratio of the likelihoods is the *Bayes factor*.

**8.2.1 Bayes Factor**

**Definition.**

$$\text{Prior odds} := P(M_1)/P(M_2)$$

$$\text{Posterior odds} := P(M_1 \mid x)/P(M_2 \mid x)$$

*(The booklet writes $x$ with an under-tilde to indicate a vector.)*

$$\text{Bayes factor} := \frac{\text{Posterior odds}}{\text{Prior odds}}$$

Interpretation: Evidence provided by the data for $M_1$ beyond that provided by the prior.

`Remark (1):` Evidence for $M_1$: $M_1$ in numerator.

`Remark (2):` There is symmetry in $M_1$ and $M_2$.

Measure of strength of evidence for $M_1$

*[margin note, left of this table: "Rule of thumb"]*

| Bayes Factor (BF) | log(B.F.) | Evidence |
|---|---|---|
| $1 \le \text{BF} < 3$ | $0 - 1.099$ | little |
| $3 \le \text{BF} < 20$ | $1.099 - 2.996$ | positive |
| $20 \le \text{BF} < 150$ | $2.996 - 5.011$ | strong |
| $\text{BF} \ge 150$ | $\ge 5.011$ | very strong |

> ✔ Verified: the log-Bayes-factor cut points are ln(3), ln(20), ln(150) rounded to 3 decimals

*Kass and Raftery (1995, JASA)*

Illustrative example

| $\mu_1$ | log(ratio) | ratio |
|---|---|---|
| 22 | 0 | 1 |
| 23 | 4.67 | 107 |
| 24 | 11.53 | $10^5$ |
| 25 | 20.61 | $8.9 \times 10^8$ |
| 26 | 31.88 | $7.0 \times 10^{13}$ |
| 27 | 45.36 | $5.0 \times 10^{19}$ |

> ✔ Verified: the two ratio tables on the page agree entry-for-entry

`Note:` The ratio of the likelihoods for $M_1$ to $M_2$ is Bayes Factor.

### PDF page 78 (booklet page 73)

**8.2.2 Marginal Likelihoods**

**Definition.**

$$\theta \in \Theta$$

$$\pi(\theta) \;\text{prior (must be proper)}$$

$$l(\theta\mid x) \propto f(x\mid\theta) \;\text{is the likelihood function.}$$

*[margin note: a large hand-drawn brace groups the three lines above; the word written beside it is illegible (possibly "one-one"(?))]*

The *Marginal likelihood* is

$$f(x) = \int_\Theta f(x\mid\theta)\pi(\theta)\,d\theta.$$

Note: $f(x\mid\theta)$ not $l(\theta\mid x)$ in the integral.

Remark (1): if $\theta$ is a point mass at $\theta_0$, then $f(x) = f(x\mid\theta_0)$.

> ✔ Verified: A point-mass prior at $\theta_0$ gives marginal likelihood $f(x) = f(x\mid\theta_0)$.

Remark (2): Generalization to multi-parameter problem is conceptually simple,

$$f(x) = \int_\Theta f(x\mid\theta)\pi(\theta)\,d\theta.$$

*(The booklet writes θ with under-tildes here to indicate vectors.)*

Remark (3): Computation of marginal likelihoods is a research activity.

**Theorem 8.2.1.** The Bayes Factor is the ratio of the marginal likelihoods of $M_1$ to $M_2$.

*Proof.* From Bayes' Theorem we have

$$P(M_1\mid x) = f(x\mid M_1)P(M_1)/f(x)$$
$$P(M_2\mid x) = f(x\mid M_2)P(M_2)/f(x)$$

for $f(x) \neq 0$ and

$$\frac{P(M_1\mid x)}{P(M_2\mid x)} = \frac{f(x\mid M_1)P(M_1)}{f(x\mid M_2)P(M_2)}$$

> ✔ Verified: Posterior odds equal $f(x\mid M_1)P(M_1)\,/\,\big(f(x\mid M_2)P(M_2)\big)$.

then

$$\frac{f(x\mid M_1)}{f(x\mid M_2)} = \frac{P(M_1\mid x)/P(M_1)}{P(M_2\mid x)/P(M_2)} = \frac{\text{Posterior odds}}{\text{Prior odds}} = \text{Bayes Factor}$$

*(correction: the printed middle fraction reads $\frac{P(M_1|x)P(M_1)}{P(M_2|x)P(M_2)}$; handwritten slashes are inserted after $P(M_1|x)$ and after $P(M_2|x)$, making both juxtapositions into quotients)*
*[a further handwritten stroke crosses the word "Prior" in "Prior odds"; its purpose is unclear]*
*[illegible handwritten scribble in the right margin, level with the line below, beside the printed end-of-proof box]*

> ✔ Verified: The Bayes factor identity: $f(x|M_1)/f(x|M_2) = \frac{P(M_1|x)/P(M_1)}{P(M_2|x)/P(M_2)} = \text{posterior odds}/\text{prior odds}$.

Note: $f(\theta\mid x) = f(x\mid\theta)\pi(\theta)/f(x)$ Bayes' Theorem $(\Rightarrow)$ $f(x) = f(x\mid\theta)\pi(\theta)/f(\theta\mid x)$.

> ✔ Verified: From $f(\theta|x) = f(x|\theta)\pi(\theta)/f(x)$ it follows that $f(x) = f(x|\theta)\pi(\theta)/f(\theta|x)$.

**Examples**

$$M_1 : X_1, ..., \underline{X_n}\mid\mu_0 \quad \overset{iid.}{\sim} \quad \mathcal{N}(\mu_0,\sigma^2) \quad \sigma^2 \text{ is known.}$$
$$M_2 : X_1, ..., \underline{X_n}\mid\mu \quad \overset{iid.}{\sim} \quad \mathcal{N}(\mu,\sigma^2) \quad \mu \ge \mu_0\,(?)$$
$$\mu \quad \sim \quad \mathcal{N}(\theta,\delta^2)$$
$$\theta, \sigma^2, \delta^2 \text{ are known.}$$

*[$X_n$ is hand-underlined in both model lines]*
*[margin note: "$\mu \ge \mu_0$" (?) is a handwritten addition at the end of the $M_2$ line, hand-underlined; the relation symbol is not fully legible and may be $\neq$]*

### PDF page 79 (booklet page 74)

$$f(x \mid M_1) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{1}{2\sigma^2}(x_i - \mu_0)^2}.$$

*(The booklet writes $x$ and $\mu$ with under-tildes to indicate vectors.)*

Consider $M_2$

$$P(\mu) = \frac{\frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(\mu-\theta)^2}}{\int_{\mu_0}^{\infty} \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(\mu-\theta)^2}\, d\mu} \qquad \mu \ge \mu_0$$

$$f(x \mid M_2) = \frac{\int_{\mu_0}^{\infty} \left\{ \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{1}{2\sigma^2}(x_i-\mu)^2} \right\} \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(\mu-\theta)^2}\, d\mu}{\int_{\mu_0}^{\infty} \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(\mu-\theta)^2}\, d\mu}$$

1. BMI Data

$$n = 60, \;\; \text{avg} \; = 20.38, \;\; \text{std} \; = 5.22$$
$$\mu_0 = 22$$
$$\theta = 20, \sigma^2 = \; \text{std}^2, \delta^2 = 100$$

Use importance sampling to evaluate $f(x \mid M_2)$

$$f(\mu) = \frac{\frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(\mu-\theta)^2}}{\int_{\mu_0}^{\infty} \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(\mu-\theta)^2}\, d\mu} \qquad \mu \ge \mu_0$$

*(correction: the printed "$P$" of "$P(\mu)$" is overwritten by a handwritten "$f$" (?))*

Importance function *[unlabelled curly margin mark to the right of this line]*

$$\mu = \theta + \delta \Phi^{-1}\left\{ U + (1-U)\Phi\left( \frac{\theta - \mu_0}{\delta} \right) \right\} \qquad U \sim U(0,1)$$

$\text{[sic: for the truncation } \mu \ge \mu_0 \text{ the argument should be } \Phi((\mu_0-\theta)/\delta)\text{]}$

> ⚠ Check FAILED: The printed Devroye/inverse-CDF transform $\mu = \theta + \delta\Phi^{-1}\{U + (1-U)\Phi((\theta-\mu_0)/\delta)\}$ has support $\mu \ge \mu_0$. — the stated result did not reproduce (see verification log)

-Devroye's method

| Runs | Log(likelihood) | | Log(BF) |
|---|---|---|---|
| 1000 | -186.7 | -190.508 | 3.798 |
| 10000 | -186.7 | -190.089 | 3.379 |
| 20000 | -186.7 | -190.084 | 3.374 |

*[hand-drawn braces beneath the two Log(likelihood) sub-columns label the "$-186.7$" column "$M_2$" (possibly "$M_3$") and the "$-190.5\ldots$" column "$M_1$".]*

*[margin note, right of the table, written vertically: "positive"]*

*[Handwritten scratch work in the left margin beside the table: "190.508" written above "186.7(00)", a rule drawn beneath, and the difference "3.808" (?) below it, with a long swoosh underneath. This is the Log(BF) subtraction for the 1000-run line.]*

> ✔ Verified: The table's Log(BF) column equals the difference of the two Log(likelihood) entries (first column $-186.710$, printed rounded to $-186.7$), and the handwritten margin subtraction gives $3.808$.

2. Normal

$$
\begin{aligned}
M_1: \quad & X_1, \ldots X_n \mid \mu && \overset{iid.}{\sim} && \mathcal{N}(\mu, \sigma^2) \\
& \mu && \sim && \mathcal{N}(\theta, \delta^2); \quad \mu \le \mu_0 \\
M_2: \quad & X_1, \ldots X_n \mid \mu && \overset{iid.}{\sim} && \mathcal{N}(\mu, \sigma^2) \\
& \mu && \sim && \mathcal{N}(\theta, \delta^2); \quad \mu > \mu_0
\end{aligned}
$$

$$\theta, \sigma^2, \delta^2 \; \text{are known.}$$

$$\mu \mid x \quad \sim \quad \mathcal{N}\big(\lambda \tilde{y} + (1-\lambda)\theta, (1-\lambda)\delta^2\big) \qquad -\infty < \mu < \infty$$

$$\lambda = \frac{\delta^2}{\delta^2 + \sigma^2/n}$$

> ✔ Verified: Normal-normal conjugacy — posterior $\mathcal{N}(\lambda\bar{y}+(1-\lambda)\theta,\;(1-\lambda)\delta^2)$ with $\lambda=\delta^2/(\delta^2+\sigma^2/n)$.

### PDF page 80 (booklet page 75)

Draw samples from posterior density and count the number times [sic: "the number of times"] $\mu > \mu_0$: posterior odds for $M_1$ is

$$Pr(\mu \le \mu_0 \mid x)/Pr(\mu > \mu_0 \mid x),$$

*(The booklet writes $x$ with an under-tilde to indicate a vector.)*

and this is the priori [sic: "prior"] odds is 1. *(correction: a hand-drawn caret is inserted into the printed phrase "the priori odds is 1", with a circled handwritten word beside the equation, best reading "one"(?) — apparently clarifying that the prior odds equal one)*

The printed sentence reads: "and this is the Bayes factor if the priori [sic] odds is 1."

| Iterations | BF | Log(BF) |
|---|---|---|
| 1000 | 99 | 4.60 |
| 5000 | 121 | 4.80 |
| 10000 | 118 | 4.77 |
| 15000 | 108 | 4.68 |
| 20000 | 111 | 4.71 |

*[margin note beside the table: "positive"]*

> ✔ Verified: Log(BF) column equals ln(BF) rounded to two decimals for each row of the iterations table

3. Binomial

*[a stray pen dot sits in the left margin level with the line below]*

$$X\mid p \;\; \sim \text{Binomial}(n,p)$$
$$\pi(p)\ \text{proper}$$

NHIS (1995 Household Survey); doctor visits during the past year

| State | Visit | No Visit | Proportion |
|---|---|---|---|
| DE | 37 | 63 | 0.37 |
| DC | 31 | 66 | 0.32 |

> ✔ Verified: NHIS proportions equal Visit/(Visit+No Visit) to two decimals

(a)

$$\begin{aligned}
M_1: &\quad X\mid p_0 \;\sim\; \text{Binomial}(n,p_0)\\
M_2: &\quad X\mid p \;\sim\; \text{Binomial}(n,p)
\end{aligned}$$
$$p \sim U(0,1),\, p > p_0 \quad \text{i.e.} \quad p \sim U(p_0,1)$$

$p_0 = 0.30$

$$\mathrm{BF} = \frac{\binom{n}{x}p_0^{x}(1-p_0)^{n-x}}{\frac{1}{1-p_0}\int_{p_0}^{1}\binom{n}{x}p^{x}(1-p)^{n-x}\,dp}$$

for DE BF = 2.00; DC BF = 8.10. *[margin note: "positive"]* $\text{[sic: exact evaluation of the displayed formula gives BF} \approx 2.02 \text{ for DE } (n=100,\,x=37) \text{ and } \approx 7.98 \text{ for DC } (n=97,\,x=31)\text{; the printed values appear to be simulation-based estimates]}$

> ⚠ Check FAILED: the Bayes factor formula with p0=3/10 yields 2.00 (DE, n=100, x=37) and 8.10 (DC, n=97, x=31) — the stated result did not reproduce (see verification log)

(b)

$$\begin{aligned}
M_1: &\quad X\mid p \;\sim\; \text{Binomial}(n,p)\\
 &\quad\;\; p \;\sim\; U(0,1)\\
M_2: &\quad X\mid p \;\sim\; \text{Binomial}(n,p)\\
 &\quad\;\; p \;\sim\; \text{Beta}(\mu\tau,(1-\mu)\tau)\\
 &\quad\;\; \mu = 0.30,\ \tau = 100
\end{aligned}$$

### PDF page 81 (booklet page 76)

$$f(x\mid M_1) = \int_0^1 \binom{n}{x} p^x (1-p)^{n-x}\,dp = \frac{1}{n+1}$$

> ✔ Verified: The uniform-prior binomial marginal integrates to $1/(n+1)$.

$$f(x\mid M_2) = \int_0^1 \binom{n}{x} p^x (1-p)^{n-x} \frac{p^{\mu\tau-1}(1-p)^{(1-\mu)\tau-1}}{B(\mu\tau,(1-\mu)\tau)}\,dp$$

$$= \binom{n}{x}\frac{B(x+\mu\tau,\; n-x+(1-\mu)\tau)}{B(\mu\tau,(1-\mu)\tau)}$$

> ✔ Verified: The beta-prior binomial marginal equals $\binom{n}{x}B(x+\mu\tau,\,n-x+(1-\mu)\tau)/B(\mu\tau,(1-\mu)\tau)$.

$$BF = \frac{B(x+1,\; n-x+1)\,B(\mu\tau,(1-\mu)\tau)}{B(x+\mu\tau,\; n-x+(1-\mu)\tau)}$$

> ✔ Verified: $BF = f(x\mid M_1)/f(x\mid M_2) = B(x+1,n-x+1)B(\mu\tau,(1-\mu)\tau)/B(x+\mu\tau,\,n-x+(1-\mu)\tau)$.

for DE BF = 2.74; DC BF = 7.86.

(c)

$$
\begin{array}{lrcl}
M_1: & X_1\mid p & \sim & \text{Bin}(n_1,p) \\
     & X_2\mid p & \sim & \text{Bin}(n_2,p)
\end{array}\;\Bigg\}\ \text{independent}
$$

$$p \;\sim\; U(0,1)$$

$$
\begin{array}{lrcl}
M_2: & X_1\mid p_1 & \sim & \text{Bin}(n_1,p_1) \\
     & X_2\mid p_2 & \sim & \text{Bin}(n_2,p_2)
\end{array}\;\Bigg\}\ \text{independent}
$$

$$p_1, p_2 \;\overset{iid.}{\sim}\; U(0,1)$$

$$f(x_1,x_2\mid M_1) = \binom{n_1}{x_1}\binom{n_2}{x_2} B\big(x_1+x_2+1,\; n_1+n_2-(x_1+x_2)+1\big)$$

> ✔ Verified: Common-$p$ joint marginal equals $\binom{n_1}{x_1}\binom{n_2}{x_2}B(x_1+x_2+1,\,n_1+n_2-(x_1+x_2)+1)$.

$$f(x_1,x_2\mid M_2) = \prod_{i=1}^{2}\binom{n_i}{x_i} B(x_i+1,\; n_i-x_i+1)$$

> ✔ Verified: Independent-$p_i$ joint marginal equals $\prod_{i=1}^{2}\binom{n_i}{x_i}B(x_i+1,\,n_i-x_i+1)$.

$$BF = \frac{\prod_{i=1}^{2}\binom{n_i}{x_i} B(x_i+1,\; n_i-x_i+1)}{\binom{n_1}{x_1}\binom{n_2}{x_2} B\big(x_1+x_2+1,\; n_1+n_2-(x_1+x_2)+1\big)}$$

$$= \frac{\prod_{i=1}^{2} B(x_i+1,\; n_i-x_i+1)}{B\big(x_1+x_2+1,\; n_1+n_2-(x_1+x_2)+1\big)}$$

> ✔ Verified: In the part-(c) Bayes factor the binomial coefficients cancel, giving the reduced ratio of beta functions.

*[margin note, written diagonally beside this $BF$ display: "Positive"(?) — the evidence category for the value $BF = 4.62$ recorded on the next line]*

1: DE 2: DC $\qquad BF = 4.62$.

Final Comment:

$$
\begin{array}{lrcl}
M_1: & y\mid p_0 & \sim & \text{Bin}(n,p_0) \\
M_2: & y\mid p & \sim & \text{Bin}(n,p) \\
     & p & \sim & U(0,1)
\end{array}
$$

$$p(y\mid M_1) = \binom{n}{y} p_0^{\,y}(1-p_0)^{n-y}$$

$$p(y\mid M_2) = \int_0^1 \binom{n}{y} p^y (1-p)^{n-y}\,dp = \frac{1}{n+1}$$

> ✔ Verified: In the Final Comment, $p(y\mid M_2)=\int_0^1\binom{n}{y}p^y(1-p)^{n-y}dp = 1/(n+1)$.

### PDF page 82 (booklet page 77)

Consider the binomial$(n,p)$ pmf MLE:

$$\hat{p} = \frac{y}{n}$$

$$\binom{n}{y}\hat{p}^{\,y}(1-\hat{p})^{n-y} \geq \frac{1}{n+1}$$

> ✔ Verified: p̂ = y/n is the maximizer in p of the binomial(n,p) pmf.

> ✔ Verified: binom(n,y) * (y/n)^y * (1-y/n)^(n-y) >= 1/(n+1) for all 0 <= y <= n.

$\binom{n}{y}p_0^y(1-p_0)^{n-y}$ can be $< \frac{1}{n+1}$ since the binomial pmf is unimodal with $n+1$ mass points.

> ✔ Verified: the binomial pmf evaluated at a p0 away from the MLE can fall below 1/(n+1).

`Remark:` It is not true that the simpler model always wins, this is true if $p_0$ is chosen near $\hat{p}$.

*[a hand-drawn arrow runs in from the left margin, pointing at this Remark]*

## 8.3 Prediction

Prediction is remarkably easy to understand within the Bayesian paradigm.

$$\pi(\theta): \text{ proper or improper prior}$$
$$l(\theta|y) \propto f(y|\theta)$$

- Prior predictive distribution

$$f(y) = \int_{\Theta} f(y|\theta)\pi(\theta)d\theta, \quad \pi(\theta) \text{ must be proper}$$

*[margin note: "Law of total probability"]*

is marginal likelihood.

- Posterior predictive distribution Have data $y_s$ ; need to predict for nonsampled values $y_{ns}$ (or future values)

*(The booklet writes $y_s$ and $y_{ns}$ with under-tildes to indicate vectors.)*

*[margin note: "finite populations"]*

$$f(y_{ns}|y_s) = \int_{\Theta} f(y_{ns}|y_s,\theta)\pi(\theta|y_s)d\theta$$

$$f(y_{ns}|y_s) = \int_{\Theta} f(y_{ns}|\theta)\pi(\theta|y_s)d\theta$$

the posterior distribution $\pi(\theta|y_s)$ must be proper.

### 8.3.1 Examples

1. Normal

$$\underbrace{y_1,\ldots,y_n}_{y\,(\text{obs})}, y_{n+1}|\mu \quad \sim \quad \mathcal{N}(\mu,\sigma^2), \sigma^2 \text{ known}, p(\mu)=1$$

Define $\bar{y} = \sum_{i=1}^{n} \frac{y_i}{n}$, then

$$\mu|y \quad \sim \quad \mathcal{N}\left(\bar{y}, \frac{\sigma^2}{n}\right)$$

> ✔ Verified: flat prior + iid normal likelihood gives posterior N(ybar, sigma^2/n).

### PDF page 83 (booklet page 78)

$$f(y_{n+1}\mid y) = \int_{-\infty}^{\infty} f(y_{n+1}\mid y,\mu)\, p(\mu \mid y)\, d\mu$$

$$= \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{1}{2\sigma^2}(y_{n+1}-\mu)^2} \frac{1}{\sqrt{2\pi\frac{\sigma^2}{n}}} e^{-\frac{n}{2\sigma^2}(\bar{y}-\mu)^2}\, d\mu$$

*(The booklet writes $y$ with under-tildes in $f(y_{n+1}\mid y)$, $f(y_{n+1}\mid y,\mu)$, $p(\mu\mid y)$ and $y_{n+1}\mid y$ to indicate vectors.)*

$$y_{n+1}\mid y \quad\sim\quad \mathcal{N}\!\left(\bar{y}, \left(1+\frac{1}{n}\right)\sigma^2\right)$$

> ✔ Verified: The Gaussian convolution $\int \mathcal{N}(y\mid\mu,\sigma^2)\mathcal{N}(\mu\mid\bar y,\sigma^2/n)\,d\mu$ equals the $\mathcal{N}(\bar y,(1+1/n)\sigma^2)$ density.

suppose $\sigma^2$ is unknown, $p(\sigma^2) \propto \frac{1}{\sigma^2}$, define $s^2 = \frac{\sum_{i=1}^{n}(y_i-\bar{y})^2}{n-1}$,

$$\frac{y_{n+1}-\bar{y}}{s\sqrt{1+\frac{1}{n}}} \quad\sim\quad t_{n-1}$$

> ✔ Verified: With prior $p(\mu,\sigma^2)\propto 1/\sigma^2$, the posterior predictive density of $y_{n+1}$ is proportional to the $t_{n-1}$ kernel in $(y_{n+1}-\bar y)/(s\sqrt{1+1/n})$.

The $100(1-\alpha)\%$ H.P.D. prediction interval for $y_{n+1}$ is

$$\bar{y} \pm s\sqrt{1+\frac{1}{n}}\, t_{n-1,\frac{\alpha}{2}}.$$

2. BMI Data

$$n = 10\ (?),\ \ \mathrm{avg} = 20.38,\ \ \mathrm{std} = 5.22$$

*(The printed sample size reads as "10", but every subsequent computation on this page uses $n = 60$ — $\sqrt{1+\tfrac{1}{60}}$ and $\sqrt{\tfrac{1}{60}}$ — and $y_1,\dots,y_{60}$ are the observations, so this is either a [sic] typo for $n = 60$ or a misreading of a "6" in the scan.)*

predict the BMI value for the $61^{st}$ person from this population.

$$y_1, \dots, y_{60}, y_{61} \mid \mu, \sigma^2 \quad\sim\quad \mathcal{N}(\mu,\sigma^2)$$

$$p(\mu,\sigma^2) \propto \frac{1}{\sigma^2}$$

$$100(1-\alpha)\%\ \text{H.P.D.} : \bar{y} \pm s\sqrt{1+\frac{1}{n}}\, t_{n-1,\frac{\alpha}{2}}$$

$$95\%\ \text{H.P.D. for } y_{61} : 20.38 \pm 5.22\sqrt{\frac{61}{60}} \times 2.0003$$

$$\approx 20.4 \pm 10.5$$

> ✔ Verified: $20.38 \pm 5.22\sqrt{61/60}\times 2.0003 \approx 20.4 \pm 10.5$ (printed precision).

$$95\%\ \text{H.P.D. for } \mu : 20.38 \pm 5.22\sqrt{\frac{1}{60}} \times 2.0003$$

$$\approx 20.4 \pm 1.3$$

> ✔ Verified: $20.38 \pm 5.22\sqrt{1/60}\times 2.0003 \approx 20.4 \pm 1.3$ (printed precision).

Remark: Predicting one observation is difficult, but predicting an average is much easier.

*["Remark:" is hand-underlined with a wavy stroke that sweeps in from the left margin.]*

**8.3.2 How do non-Bayesians predict?**

$$\underbrace{y_1, \dots, y_n}_{\text{observed}}, y_{n+1} \overset{iid.}{\sim} \quad \mathcal{N}(\mu,\sigma^2)$$

### PDF page 84 (booklet page 79)

need inference for $y_{n+1}$, $E(y_{n+1}) = \mu$. A "good" estimation for $\mu$ is $\bar{y} = \sum_{i=1}^{n} \frac{y_i}{n}$. Look at $y_{n+1} - \bar{y}$, again define $s^2 = \frac{\sum_{i=1}^{n}(y_i - \bar{y})^2}{n-1}$

$$\left.\begin{array}{ccc}
\dfrac{y_{n+1} - \bar{y}}{\sigma\sqrt{1 + \frac{1}{n}}} & \sim & \mathcal{N}(0,1)\\[2ex]
\dfrac{(n-1)s^2}{\sigma^2} & \sim & \chi^2_{n-1}
\end{array}\right\}\text{independent}$$

*[margin mark: faint illegible pen mark [illegible]]*

$$\implies \quad \frac{y_{n+1} - \bar{y}}{s\sqrt{1 + \frac{1}{n}}} \quad \sim \quad t_{n-1}$$

> ✔ Verified: For iid normal $y_1,\dots,y_{n+1}$, $\operatorname{Var}(y_{n+1}-\bar{y}) = \sigma^2(1+1/n)$.

> ✔ Verified: The Student-$t$ pivot $Z/\sqrt{V/(n-1)}$ reduces to $(y_{n+1}-\bar y)/(s\sqrt{1+1/n})$.

A $100(1-\alpha)\%$ confidence interval for $y_{n+1}$ is

$$\bar{y} \pm s\sqrt{1 + \frac{1}{n}}\, t_{n-1,\frac{\alpha}{2}}.$$

*[hand-drawn caret/pointer stroke in the left margin, pointing at this Remark]*

Remark: *["Remark:" is hand-underlined]* The non-Bayesian idea is to find the "best" estimator for $E(y_{n+1})$ and then study the distribution of $y_{n+1} - \hat{E}(y_{n+1})$.

**8.3.3 More examples**

1. Bayesian Predictive Inference

$$\underbrace{y_1, \dots, y_n}_{y_s}\ \underbrace{y_{n+1}, \dots, y_N}_{y_{ns}} \quad \sim (\mu, \sigma^2)$$

*(The booklet writes $y_s$ and $y_{ns}$ with under-tildes to indicate vectors.)*

$$p(\mu, \sigma^2) \quad \propto \quad \frac{1}{\sigma^2}$$

Finite population of size $N$ is a (random) sample from an infinite population (super population). Here $y_1, \dots, y_n$ are a random sample from a finite population. Interest:

$$\bar{Y} = \sum_{i=1}^{N} \frac{y_i}{N}\ \text{ finite population mean} = f\bar{y}_s + (1-f)\bar{y}_{ns}$$

> ✔ Verified: $\bar{Y} = f\bar{y}_s + (1-f)\bar{y}_{ns}$ with $f=n/N$.

where $f = \frac{n}{N}$, $\bar{y}_s = \sum_{i=1}^{n} \frac{y_i}{n}, \bar{y}_{ns} = \sum_{i=n+1}^{N} \frac{y_i}{N-n}$. Then,

$$\frac{\bar{Y} - \bar{y}_s}{s\sqrt{(1-f)/n}}\ \Big|\ \bar{y}_s \quad \sim \quad t_{n-1}$$

> ✔ Verified: $(1-f)^2\left(\frac{1}{N-n}+\frac{1}{n}\right) = \frac{1-f}{n}$ when $f=n/N$.

and the $100(1-\alpha)\%$ H.P.D. interval for $\bar{Y}$ is

$$\bar{y}_s \pm s\sqrt{\frac{1-f}{n}}\, t_{n-1,\frac{\alpha}{2}}.$$

Remark: This is an approximate interval used in survey sampling.

### PDF page 85 (booklet page 80)

2. BMI Data

$$n = 10, \;\; \text{avg} \; = 20.38, \;\; \text{std} \; = 5.22$$

assume 10% sampling, predict finite population mean

$$95\% \text{ H.P.D. for } \mu: \quad 20.38 \pm 1.35$$

$$95\% \text{ H.P.D. for } \bar{Y}: \quad 20.38 \pm 5.22\sqrt{\left(1 - \frac{1}{10}\right)/10} \times 2.0003$$

$$\approx 20.38 \pm 1.27$$

*[margin note, right, with an arrow to this line: "$N = 100$"]*

*(The displayed expression does not evaluate to the stated value: $5.22\sqrt{(1-1/10)/10}\times 2.0003 \approx 3.13$, not $1.27$. Transcribed as printed.)*

> ⚠ Check FAILED: The printed 10%-sampling expression $5.22\sqrt{(1-1/10)/10}\times 2.0003$ equals the stated $1.27$ to two decimals. — the stated result did not reproduce (see verification log)

With 1% sampling

$$95\% \text{ H.P.D. for } \bar{Y}: \quad 20.38 \pm 1.34$$

*(The same expression with $f = 1/100$, $5.22\sqrt{(1-1/100)/10}\times 2.0003 \approx 3.29$, does not give the stated $1.34$; the printed values reconcile only if $n = 60$. Transcribed as printed.)*

*[margin note, right, with an arrow to this line: "$N = 1000$"]*

> ⚠ Check FAILED: With 1% sampling, the same expression with $f = 1/100$ equals the stated $1.34$ to two decimals. — the stated result did not reproduce (see verification log)

3. Simple linear regression

Define $y_i = \beta_0 + \beta_1 x_i + e_i$ where

$$e_i \overset{iid.}{\sim} \mathcal{N}(0, \sigma^2) \quad i = 1, 2, ..., n,$$

and $\beta = (\beta_0, \beta_1)$ *(The booklet writes $\beta$ with under-tildes to indicate vectors.)*

$$p(\beta, \sigma^2) \propto \frac{1}{\sigma^2}.$$

Jeffreys' "independence" prior $\hat{\beta}$ is least square estimator of $\beta$ *(correction: a handwritten "e" is inserted into the printed "Jefferys'", giving "Jeffreys'")*

$$\hat{y}_0 = \hat{\beta}_0 + \hat{\beta}_1 x_i.$$

Define $\bar{x} = \sum_{i=1}^{n} \frac{x_i}{n}; \; \hat{\sigma}^2 = \sum_{i=1}^{n} \frac{(y_i - \hat{y}_i)^2}{n-1}$ $\text{[sic: the residual sum of squares is divided by } n-1\text{, while the interval below uses } t_{n-2,\alpha/2}\text{]}$

$$s^2 = \hat{\sigma}^2\left[1 + \frac{1}{n} + \frac{(x_{new} - \bar{x})^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}\right].$$

A $100(1-\alpha)\%$ H.P.D. interval for $y_{new}$ (a future observation at $x_{new}$) is

$$\hat{\beta}_0 + \hat{\beta}_1 x_{new} \pm s t_{n-2, \frac{\alpha}{2}}$$

`Remark:` Inference is exactly the same as for non-Bayesians. *(correction: the printed "is" is struck through with a slash and replaced by handwritten "as")*

4. National Health and Nutrition Examination Survey (NHANES)

14 young ladies age $15 - 24$ in county [sic] with data on BMI and age.

Simple linear regression

$$\text{BMI} \; = 1.54 + 1.15 \; \text{age} \qquad R^2 = 60\%$$

$$\text{NSE} \; = 4.5$$

### PDF page 86 (booklet page 81)

Predict the BMI for a lady of age 24.

$$\text{BMI}_{24} = 1.54 + 1.15 \times 24 = 29.14$$

> ✔ Verified: The point prediction $1.54 + 1.15 \times 24$ equals $29.14$ exactly.

$$s = \sqrt{4.5\left(1 + \frac{1}{24} + \frac{(24 - 19.93)^2}{62.92}\right)} = 2.23 \quad \text{[sic: the formula as printed evaluates to } 2.4233\text{]}$$

*[sic: the printed value $2.23$ does not follow from the printed formula, which gives $2.4233$; the interval on the next line is computed with $2.23$ and is internally consistent with it.]*

> ⚠ Check FAILED: The printed prediction standard error $\sqrt{4.5(1 + 1/24 + (24-19.93)^2/62.92)}$ equals $2.23$ to 2 decimal places. — the stated result did not reproduce (see verification log)

95% H.P.D. interval for the true BMI is

$$29.14 \pm 2.23 \times 2.1788 \approx (24.3,\, 34.0) \qquad t_{12,0.975} = 2.1788.$$

> ✔ Verified: $29.14 \pm 2.23 \times 2.1788$ rounds to the interval $(24.3, 34.0)$ at 1 decimal place.

> ✔ Verified: The upper 0.975 quantile of Student's $t$ with 12 degrees of freedom is $2.1788$ to 4 decimal places.

### PDF page 87 (booklet page 82)

*(Blank page — running header only.)*

# Chapter 4 — Lecture Four
*(PDF pages 40–45; booklet pages 35–40)*


### PDF page 40 (booklet page 35)

# Chapter 4 — Lecture Four

**Example**

$$x_1, ..., x_n \mid \mu, \sigma^2 \overset{\text{iid}}{\sim} N(\mu, \sigma^2)$$

What is the conjugate prior for $(\mu, \sigma^2)$?

$$L(\mu, \sigma^2 \mid x) \propto \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} exp\left\{-\frac{1}{2\sigma^2}[(n-1)s^2 + n(\bar{x} - \mu)^2]\right\}$$

*(The booklet writes $x$ with an under-tilde to indicate a vector.)*

$$\propto \frac{1}{\sqrt{2\pi \frac{\sigma^2}{n}}} e^{-\frac{n}{2\sigma^2}(\mu - \bar{x})^2} \left(\frac{1}{\sigma^2}\right)^{\frac{n-1}{2}} e^{-\frac{(n-1)s^2}{2\sigma^2}}$$

> ✔ Verified: The two displayed expressions for $L(\mu,\sigma^2\mid x)$ differ by the constant $(2\pi)^{(1-n)/2}/\sqrt{n}$, free of $\mu$ and $\sigma^2$.

$$\pi(\mu, \sigma^2) \propto \frac{1}{\sqrt{2\pi \frac{\sigma^2}{k_o}}} e^{-\frac{k_o}{2\sigma^2}(\mu - \mu_o)^2} \left(\frac{1}{\sigma^2}\right)^{\frac{\nu_o}{2} + 1} e^{-\frac{\nu_o \sigma_o^2}{2\sigma^2}}$$

*(correction: the printed relation symbol after $\pi(\mu,\sigma^2)$ is circled by hand and a handwritten "$\propto$" is written above it)*

*[margin note, right of this equation: $\dfrac{\left(\frac{\nu_o \sigma_o^2}{2}\right)^{\frac{\nu_o}{2}}}{\Gamma\!\left(\frac{\nu_o}{2}\right)}$ (?) — the normalizing constant of the scaled inverse-$\chi^2$ factor]*

*[hand arrow in margin pointing at "Nor Inv"]* Nor Inv $\chi^2(\mu_o, \frac{\sigma_o^2}{k_o}, \nu_o, \nu_o\sigma_o^2)$

I claim that this distribution is a conjugate prior. *[the phrase "a conjugate prior" is hand-underlined, with a curved arrow pointing to it]*

$$\pi(\mu, \sigma^2 \mid x) \propto Nor\ Inv(\mu_n, \frac{\sigma_n^2}{k_n}, \nu_n, \nu_n\sigma_n^2)$$

> ⚠ Check FAILED: Prior kernel $\times$ likelihood kernel equals the Nor-Inv-$\chi^2(\mu_n,\sigma_n^2/k_n,\nu_n,\nu_n\sigma_n^2)$ kernel exactly, with $k_n=k_o+n$, $\nu_n=\nu_o+n$, $\nu_n\sigma_n^2=\nu_o\sigma_o^2+(n-1)s^2+\frac{k_o n}{k_o+n}(\bar x-\mu_o)^2$. — the stated result did not reproduce (see verification log)

$$\text{where } \mu_n = \frac{k_o\mu_o}{k_o + n_o} + \frac{n}{k_o + n}\bar{x}$$

$$k_n = k_o + n$$

$$\nu_n = \nu_o + n$$

$$\nu_n\sigma_n^2 = \nu_o\sigma_o^2 + (n-1)s^2 + \frac{k_o n}{k_o + n}(\bar{x} - \mu_o)^2$$

$\text{[sic: the first denominator reads } k_o + n_o \text{; it should be } k_o + n \text{, i.e. } \mu_n = \frac{k_o\mu_o + n\bar{x}}{k_o + n}\text{]}$

> ✔ Verified: Completing the square: $k_o(\mu-\mu_o)^2+n(\mu-\bar x)^2=(k_o+n)(\mu-\mu_n)^2+\frac{k_o n}{k_o+n}(\bar x-\mu_o)^2$ for $\mu_n=\frac{k_o\mu_o+n\bar x}{k_o+n}$; the printed $k_o+n_o$ denominator does not give an identity.

### PDF page 41 (booklet page 36)

$\nu_o\sigma_o^2$ is the prior sum of square, $(n-1)s^2 + \dfrac{k_o n}{k_o+n}(\bar{x}-\mu_o)^2$ is data sum of square.

The posterior can be written as:

1.$\mu|\sigma^2, x \;\sim\; N(\mu_n, \frac{\sigma^2}{k_n})$

2.$\sigma^2|x \;\sim\; Inv\chi^2(\nu_n, \sigma_n^2)$

*(The booklet writes $x$ with under-tildes to indicate vectors.)*

Finally: $\mu|x \;\sim\; t_{\nu_n}(\mu_n, \frac{\sigma_n^2}{k_n})$

That is
$$\frac{1}{\left[1+\dfrac{\left(\dfrac{\mu-\mu_n}{\sigma_n/\sqrt{k_n}}\right)^2}{\nu_n}\right]^{\frac{\nu_n+1}{2}}} \;\sim\; t_{\nu_n}$$

> ✔ Verified: The printed kernel $\left[1+\frac{((\mu-\mu_n)/(\sigma_n/\sqrt{k_n}))^2}{\nu_n}\right]^{-(\nu_n+1)/2}$ is proportional to the Student-$t_{\nu_n}$ density with location $\mu_n$ and scale $\sigma_n/\sqrt{k_n}$.

**4.1 Combination of information from different sources**

NonBayesian

$$\hat{\theta}_1 \;\sim\; N(\theta, \sigma_1^2)$$
$$\hat{\theta}_2 \;\sim\; N(\theta, \sigma_2^2)$$

These two informations [sic] are independent. *[the words "are independent" are hand-underlined, the underline ending in a small back-pointing arrow at the left]*

So
$$w\hat{\theta}_1 + (1-w)\hat{\theta}_2 \;\sim\; N(\theta, w^2\sigma_1^2 + (1-w)^2\sigma_2^2)$$

To find $w$, we minimize $w^2\sigma_1^2 + (1-w)^2\sigma_2^2,\; 0\le w\le 1$.

$$w = \frac{\sigma_2^2}{\sigma_1^2+\sigma_2^2}$$

> ✔ Verified: $w=\sigma_2^2/(\sigma_1^2+\sigma_2^2)$ uniquely minimizes $w^2\sigma_1^2+(1-w)^2\sigma_2^2$ and lies in $[0,1]$.

Bayesian

$$f(\hat{\theta}_1,\hat{\theta}_2|\theta) = \frac{1}{\sqrt{2\pi\sigma_1^2}}e^{-\frac{1}{2\sigma_1^2}(\hat{\theta}_1-\theta)^2} - \frac{1}{\sqrt{2\pi\sigma_2^2}}e^{-\frac{1}{2\sigma_2^2}(\hat{\theta}_2-\theta)^2}$$

$\text{[sic: a minus sign is printed between the two normal densities; by independence the two factors should be multiplied]}$

$$\pi(\theta|\hat{\theta}_1,\hat{\theta}_2) \;\propto\; e^{-\frac{1}{2}\left[\frac{1}{\sigma_1^2}(\theta-\hat{\theta}_1)^2 + \frac{1}{\sigma_2^2}(\theta-\hat{\theta}_2)^2\right]}$$

$$\propto\; e^{-\frac{1}{2}\left(\frac{1}{\sigma_1^2}+\frac{1}{\sigma_2^2}\right)\left[\theta - \frac{\left(\frac{1}{\sigma_1^2}\hat{\theta}_1 + \frac{1}{\sigma_2^2}\hat{\theta}_2\right)}{\frac{1}{\sigma_1^2}+\frac{1}{\sigma_2^2}}\right]^2}$$

> ✔ Verified: Completing the square: the residual after extracting $\left(\frac{1}{\sigma_1^2}+\frac{1}{\sigma_2^2}\right)(\theta-m)^2$ is free of $\theta$.

$$\theta|\hat{\theta}_1,\hat{\theta}_2 \;\sim\; N\left\{ \frac{\left(\frac{1}{\sigma_1^2}\hat{\theta}_1 + \frac{1}{\sigma_2^2}\hat{\theta}_2\right)}{\frac{1}{\sigma_1^2}+\frac{1}{\sigma_2^2}},\; \frac{1}{\frac{1}{\sigma_1^2}+\frac{1}{\sigma_2^2}} \right\}$$

We get the same answers.

> ✔ Verified: Bayesian posterior mean/variance coincide with the optimally-weighted non-Bayesian combination.

### PDF page 42 (booklet page 37)

**4.2 How many observations the prior is worth?**

Don't want prior to "over power" the data.

**Example**

$$X_1,...,X_n|\mu \;\sim\; N(\mu,\sigma^2),\; \sigma^2 \text{is knowm [sic]}$$

$$\mu \;\sim\; N(\theta,\delta^2)$$

Effective sample size (ESS) $ESS \geq n$
Want to know $ESS - n$.
Look at posterior variances.

$$Var_I(\mu|\underset{\sim}{x}) = \frac{1}{\frac{1}{\delta^2} + \frac{n}{\sigma^2}}$$

> ✔ Verified: For $X_i\mid\mu\overset{iid}{\sim}N(\mu,\sigma^2)$ ($i=1..n$, $\sigma^2$ known) and prior $\mu\sim N(\theta,\delta^2)$, the posterior variance of $\mu$ equals $\left(\frac{1}{\delta^2}+\frac{n}{\sigma^2}\right)^{-1}$.

*(The booklet writes $x$ with an under-tilde to indicate a vector.)*

$$Var_N(\mu|\underset{\sim}{x}) = \frac{\sigma^2}{n}$$

*[margin note (left, handwritten): "$\pi(\mu)\propto 1$" (?)]*

$$\frac{Var_N(\mu|\underset{\sim}{x})}{Var_I(\mu|\underset{\sim}{x})} \approx \frac{ESS}{n}$$

*[margin note (left, handwritten): "$\mu|x \sim N\left(\bar{x}, \frac{\sigma^2}{n}\right)$" (?)]*
*[margin note (right, handwritten): "variance $\propto \frac{1}{n}$"]*

$$ESS = \frac{Var_N(\mu|\underset{\sim}{x})}{Var_I(\mu|\underset{\sim}{x})} n = \frac{\sigma^2}{\delta^2} + n.$$

> ✔ Verified: $ESS = \dfrac{Var_N}{Var_I}\,n = \dfrac{\sigma^2/n}{\left(\frac{1}{\delta^2}+\frac{n}{\sigma^2}\right)^{-1}}\,n$ simplifies to $\dfrac{\sigma^2}{\delta^2}+n$, and consequently $ESS\ge n$.

So the prior is equivalent to $\frac{\sigma^2}{\delta^2}$ observations and if $\delta^2 \to \infty$, the prior is worth zero observations, as expected. *(correction: the printed word breaks as "observa-tion"; the final "s" and the phrase "as expected." are handwritten)*

> ✔ Verified: The prior is worth $ESS-n=\sigma^2/\delta^2$ observations, which tends to $0$ as $\delta^2\to\infty$.

**Bayes' Estimators (Decision Theory)** *[the whole heading is hand-underlined, with an arrow drawn to it from the left margin]*

Data: $\underset{\sim}{X}$
Prior: $\pi(\theta)$
Want to estimate $\tau(\theta)$. *[margin note, in a large hand-drawn bracket spanning this line and the next: "e.g $\tau(\theta) = \theta$"]*
Estimator of $\tau(\theta)$ is $d(\underset{\sim}{X})$.

Loss function: *[a hand-drawn underline with a left-pointing arrowhead is drawn beneath this phrase]*

$$L(\theta, d(\underset{\sim}{X}))$$

Nonnegative convex function, $2^{nd}$ derivative $\geq 0$

(1) No data, the Bayes' estimator of $\tau(\theta)$ is any real number $d$ minimizing

$$E[L(\tau(\theta),d)] = \min_{d} \int L(\tau(\theta),d)\pi(\theta)d\theta$$

*[margin note (right, handwritten, underlined): "risk function" — labelling the left-hand side $E[L(\tau(\theta),d)]$]*
*[annotation below the integral: $L(\tau(\theta),d)$ is hand-underlined and labelled "Loss function"]*

### PDF page 43 (booklet page 38)

$$\int L(\tau(\theta),d)\pi(\theta)d\theta \;\text{ is the risk function.}$$

(2) With data, so $x$ observed.

The Bayes' estimator of $\tau(\theta)$ is $d(x)$, so we search $d(x)$ minimizing

$$E[L(\tau(\theta),d(X))\mid x] = \int L(\tau(\theta),d(x))\pi(\theta\mid x)d\theta$$

Typical loss function of the form $L(\tau(\theta),d) = h(d-\tau(\theta))$

Three loss functions:

1) Squared error loss (SEL).

$$L(\theta,d) = [d-\tau(\theta)]^2$$
$$d(x) = E[\tau(\theta)\mid (x)] \quad \text{[sic: the stray parentheses around } x \text{ appear in the booklet]}$$

> ✔ Verified: Under squared error loss, the minimizer over $d$ of the posterior expected loss $E[(d-T)^2\mid x]$ is the posterior mean $E[T\mid x]$.

*[Handwritten scratch note in the right margin, a large hook/brace pointing at the two SEL equations, partly legible: "Note" (?) ... $\frac{\partial}{\partial d}$ (?) ... "$\tau(\theta)\mid x)$" (?). It appears to be lecture scratch for differentiating the posterior expected loss with respect to $d$ to show the SEL estimator is the posterior mean; the middle symbols are [illegible].]*

2) Absolute error loss (AEL).

$$L(\theta,d) = |d-\tau(\theta)|$$
$$d(x)\text{is the median of } \pi(\tau(\theta)\mid x)$$

3) Zero-one loss (ZOL).

$$L(\theta,d) = \begin{cases} 0, & |d-\theta| \le c \\ 1, & |d-\theta| > c \end{cases}$$
$$d(x) \text{ is posterior mode of } \pi(\tau(\theta)\mid x).$$

*[a long hand-drawn vertical stroke is drawn down through the word "of" in the line above; no replacement is written]*

## Example

$$X_1,...,X_n\mid\theta \;\sim\; Bernoulli(\theta)$$
$$\theta \;\sim\; Beta(\alpha,\beta)$$
$$\theta\mid x \;\sim\; Beta(s+\alpha, n-s+\beta)$$

> ⚠ Check FAILED: Bernoulli likelihood with Beta(alpha,beta) prior yields a Beta(s+alpha, n-s+beta) posterior. — the stated result did not reproduce (see verification log)

SEL:

$$E(\theta\mid X) = \frac{s+\alpha}{n+\alpha+\beta}$$

> ⚠ Check FAILED: The posterior mean is (s+alpha)/(n+alpha+beta). — the stated result did not reproduce (see verification log)

AEL:

$$\int_0^a \frac{\theta^{s+\alpha-1}(1-\theta)^{n-s+\beta-1}}{Beta(s+\alpha,n-s+\beta)}d\theta = \frac{1}{2}, \text{ use a root finder.}$$

> ⚠ Check FAILED: The AEL integrand is a normalized density on (0,1), so the equation defines the posterior median. — the stated result did not reproduce (see verification log)

### PDF page 44 (booklet page 39)

ZOL:

$$\frac{s+\alpha-1}{s+\alpha+n+\beta-s-2} = \frac{s+\alpha-1}{\alpha+\beta-2},\ \alpha>1,\ \alpha+\beta>2$$

$\text{[sic: the left denominator simplifies to } n+\alpha+\beta-2\text{, so an } n \text{ appears to be dropped on the right; the stated conditions } \alpha>1,\ \alpha+\beta>2 \text{ match the printed right-hand denominator]}$

> ✔ Verified: The ZOL posterior-mode denominator $s+\alpha+n+\beta-s-2$ equals $n+\alpha+\beta-2$; the printed right-hand side drops the $n$, so the stated equality fails whenever $n\neq 0$.

Just find the maximum of the $\pi(\theta\mid x)$ using differentiation. *[the sentence is hand-underlined with a long looping stroke]*

**Example**

$$X_1,...,X_n \overset{iid}{\sim} N(\mu,\sigma^2)$$

$$\mu \;\sim\; N(\theta,\delta^2)$$

$$\mu\mid x \;\sim\; N[\lambda\bar{x} + (1-\lambda)\mu,\, (1-\lambda)\delta^2],\ \text{where} = \frac{\delta^2}{\delta^2+\frac{\sigma^2}{n}}$$

*[the posterior mean is hand-underlined with a left-pointing arrow]*

$\text{[sic: "where} = \text{" is missing its left-hand side, } \lambda\text{; and } (1-\lambda)\mu \text{ should be } (1-\lambda)\theta \text{, since the prior mean is } \theta\text{]}$

*[Handwritten work below the display, cursive and largely illegible; best-effort reading: "then answer(?) ... the(?) same(?)". These appear to be lecture scratch notes remarking that the answer comes out the same.]*

> ✔ Verified: Normal–normal posterior: $\mu\mid x\sim N[\lambda\bar{x}+(1-\lambda)\theta,\ (1-\lambda)\delta^2]$ with $\lambda=\delta^2/(\delta^2+\sigma^2/n)$ (note the booklet prints $(1-\lambda)\mu$ for the mean).

**4.3 How to draw a sample from a set of values?**

Assume we have data: $y_1 < y_2 < ... < y_n$

The probabilities are: $p_1, p_2, ..., p_n$

*[small hand tick mark above and to the left of the display]*

$$\begin{aligned}
P[y = y_i] &= P[y_{i-1} < y \le y_i]\\
&= P[y \le y_i] - P[y \le y_{i-1}]\\
&= F(y_i) - F(y_{i-1})\\
&= P[F(y_{i-1}) < U \le F(y_i)],\quad U \;\sim\; U(0,1).
\end{aligned}$$

*[left margin, beside this display: a large hand-drawn "R" with a hooked stroke below it, "7"(?) or a downward arrow]*

*[right margin, beside this display: margin note "Casella and Berger"]*

> ✔ Verified: For $U\sim U(0,1)$, $P[F(y_{i-1}) < U \le F(y_i)] = F(y_i)-F(y_{i-1})$ whenever $0\le F(y_{i-1})\le F(y_i)\le 1$.

Draw $U \;\sim\; U(0,1)$

If $F(y_{i-1}) < U \le F(y_i)$, then take this $y_i$.

| data | Probability | CDF=F() |
|---|---|---|
| $y_1$ | $p_1$ | $p_1$ |
| $y_2$ | $p_2$ | $p_1 + p_2$ |
| . | . | . |
| . | . | . |
| . | . | . |
| $y_n$ | $p_n$ | $p_1 + ... + p_n$ |

**Grid Method**

$\pi(\theta\mid x) \propto h(\theta)$

Assume that $0 \le \theta \le 1$

If $-\infty < \theta < \infty$, by transformation, $\phi = \frac{1}{1+e^{\theta}}$, so $0 \le \phi \le 1$.

If $\theta > 0, \phi = \frac{1}{1+\theta}$, so $0 \le \phi \le 1$.

> ⚠ Check FAILED: $\phi=1/(1+e^{\theta})$ maps $(-\infty,\infty)$ onto $(0,1)$; $\phi=1/(1+\theta)$ maps $(0,\infty)$ onto $(0,1)$. Both are strictly monotone (one-to-one). — the stated result did not reproduce (see verification log)

### PDF page 45 (booklet page 40)

*[Figure: a multimodal posterior density $\pi(\phi\mid X)$ plotted against $\phi$, rising from the origin, with three humps of decreasing height (the middle one tallest) and decaying to zero at the right. The area under the curve is partitioned into thin vertical strips of equal width; the second strip from the left is shaded, illustrating the grid cell selected in the discussion below.]*

| $\theta$ | Middle Point | Height | Probability | CDF=F() |
|---|---|---|---|---|
| $0 \sim 0.01$ | $0.005$ | $h_1$ | $h_1/\sum h_i$ | $p_1$ |
| $0.01 \sim 0.02$ | $0.015$ | $h_2$ | $h_2/\sum h_i$ | $p_1 + p_2$ |
| $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ |
| $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ |
| $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ |
| $0.99 \sim 1$ | $0.995$ | $h_{100}$ | $h_{100}/\sum h_i$ | $p_1 + ... + p_{100} = 1$ |

> ✔ Verified: The 100 equal-width bins ((i-1)/100, i/100) on (0,1) have middle points 0.005, 0.015, ..., 0.995.

> ⚠ Check could not run (error): With p_i = h_i / sum_j h_j, the cumulative sum p_1 + ... + p_100 equals 1. — timed out after 90s

First draw a number $U$ between $(0,1)$.

Suppose I draw $(0.01, 0.02)$ interval.

Now draw a uniform number in $(0.01, 0.02)$.

$$\frac{X - 0.01}{0.02 - 0.01} = U \;\sim\; U(0,1)$$

*[margin note, left of this equation: "jittering"]*

> ✔ Verified: X defined by (X - 0.01)/(0.02 - 0.01) = U with U ~ Uniform(0,1) is Uniform(0.01, 0.02).

So $X$ is the value we want.

In some problems, we would need search for the regions of nonzero probability $(\le 10^{-6})$. *[the final clause "for the regions of nonzero probability $(\le 10^{-6})$" is hand-underlined with a wavy stroke]*

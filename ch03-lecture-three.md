# Chapter 3 — Lecture Three
*(PDF pages 22–23; booklet pages 17–18)*


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

So,

$$
\begin{aligned}
f(x_{n+1}\mid x) &= \int_{-\infty}^{\infty} f(x_{n+1}\mid x, \mu)\,\pi(\mu\mid x)\,d\mu \\
&= \int_{-\infty}^{\infty} f(x_{n+1}\mid \mu)\,\pi(\mu\mid x)\,d\mu \\
&= \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{1}{2\sigma^2}(x_{n+1}-\mu)^2} \frac{1}{\sqrt{2\pi(1-\lambda)\delta^2}} e^{-\frac{1}{2(1-\lambda)\delta^2}\left[\mu - (\lambda\bar{x} + (1-\lambda)\theta)\right]^2} d\mu
\end{aligned}
$$

$f(x_{n+1}\mid x)$ has to be normal.

Simply needs $E(x_{n+1}\mid x)$ and $Var(x_{n+1}\mid x)$.

$$
E(x_{n+1}\mid x) = E_{\mu\mid x}\left[E(x_{n+1}\mid x, \mu)\right] = E(\mu\mid x) = \lambda\bar{x} + (1-\lambda)\theta
$$

> ⚠ Check FAILED: The posterior predictive integral equals the normal density with mean $\lambda\bar{x}+(1-\lambda)\theta$ and variance $\sigma^2+(1-\lambda)\delta^2$. — the stated result did not reproduce (see verification log)

$$
\begin{aligned}
Var(x_{n+1}\mid x) &= E_{\mu\mid x}\left[Var(x_{n+1}\mid x, \mu)\right] + Var_{\mu\mid x}\left[E(x_{n+1}\mid x, \mu)\right] \\
&= E(\sigma^2) + Var(\mu\mid x) \\
&= \sigma^2 + (1-\lambda)\delta^2
\end{aligned}
$$

So

$$
x_{n+1}\mid x \sim N(\lambda\bar{x} + (1-\lambda)\theta,\; \sigma^2 + (1-\lambda)\delta^2)
$$

**Example(2)**

There are two factories, denoted by $\theta = 0$ and $\theta = 1$.

Mathematical Model:

Prior: $P(\theta = 0) = \frac{1}{3} = 1 - P(\theta = 1)$

Y: bolt is defective

$P[Y = 1\mid\theta = 0] = \frac{2}{10} = 1 - P[Y = 0\mid\theta = 0]$

$P[Y = 1\mid\theta = 1] = \frac{1}{10} = 1 - P[Y = 0\mid\theta = 1]$

Assume that bolts are drawn independently.

So if we draw a bolt, what is the probability that this bolt is defective? i.e. $P[Y = 1] = ?$

$P[Y = 1] = P[Y = 1\mid\theta = 0]P(\theta = 0) + P[Y = 1\mid\theta = 1]P(\theta = 1) = \frac{2}{10}\frac{1}{3} + \frac{1}{10}\frac{2}{3} = \frac{4}{30} = \frac{8}{60}$

> ⚠ Check could not run (unsafe): $P[Y=1] = \frac{2}{10}\cdot\frac{1}{3} + \frac{1}{10}\cdot\frac{2}{3} = \frac{4}{30} = \frac{8}{60}$. — rejected by import guard

Pick a bolt, $Y_1 = 1$

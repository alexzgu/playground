# Chapter 3 — Lecture Three
*(PDF pages 22–39; booklet pages 17–34)*

> **⚠ PARTIAL:** only PDF page 22 is transcribed below. Pages 23–39 of this chapter (and everything after) are pending — see the STATUS section in README.md.

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

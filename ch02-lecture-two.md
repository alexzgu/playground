# Chapter 2 — Lecture Two
*(PDF pages 14–21; booklet pages 9–16)*

### PDF page 14 (booklet page 9)

# Chapter 2 — Lecture Two

**Review**
1. Bayesian paradigm
2. Calculus of probability — Conditional probabilities — Random variables
3. Coherent
4. Bayes' theorem; Extension rule
5. Identical random variables

**2.1 Bayes' Theorem**

$p(\theta\mid D, H) \propto p(D\mid \theta, H)\cdot p(\theta\mid H)$
$p(\theta_1, \theta_2\mid D) \propto p(D\mid \theta_1, \theta_2)\cdot p(\theta_1, \theta_2)$, dropping $H$
$p(\theta_1\mid D) \propto \int_{\theta_2} p(D\mid \theta_1, \theta_2)\cdot p(\theta_1, \theta_2)\,d\theta_2$, extension rule.
*(The booklet writes $\theta$ with under-tildes to indicate vectors.)*

**2.2 Independence**

$X \perp Y$, $f_{X,Y}(x,y) = f_X(x)f_Y(y)$ for all $x, y$.
$X_1, \ldots, X_n$ independent if $f_{X_1,\ldots,X_n}(x_1,\ldots,x_n) = \prod_{i=1}^n f_{X_i}(x_i)$ for all $(x_1, \ldots, x_n)$.

If $X_1, \ldots, X_n \overset{iid}{\sim} f(x)$: $f_{X_1,\ldots,X_n}(x_1,\ldots,x_n) = \prod_{i=1}^n f(x_i)$.
"iid" same as random sample.

**2.3 Exchangeability**

$X_1, \ldots, X_n$ are called exchangeable if the joint density $f_{X_1,\ldots,X_n}(x_1,\ldots,x_n)$ is invariant to permutations of $1, \ldots, n$.

### PDF page 15 (booklet page 10)

The set of exchangeable random variables contains the set of iid random variables.

Special case: $X_1, \ldots, X_n$ iid $\Rightarrow$ exchangeable.
Exchangeable does not imply iid.
But exchangeable random variables must be identically distributed.
So exchangeable variables are generally correlated. They must be **equi-correlated**.
In general, all $k$-tuples must have same joint distribution.

**Example (1).** $X_1, X_2, X_3 \sim$ exchangeable, so $(X_1, X_2)$, $(X_2, X_3)$ and $(X_1, X_3)$ have the same joint distribution.

**Example (2).**
$$f(x_1, \cdots, x_n) = \frac{B\left(\sum_{i=1}^n x_i + \alpha,\ n - \sum_{i=1}^n x_i + \beta\right)}{B(\alpha, \beta)} \text{ is the function of } \sum_{i=1}^n x_i.$$
Here, $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$.
$\sum_{i=1}^n x_i$ cannot change with permutation of the labels, so $x_1, \cdots, x_n$ are exchangeable.

**Example (3). Multivariate normal**
$$\begin{pmatrix} X_1 \\ \vdots \\ X_n \end{pmatrix} = \underset{n\times 1}{X} \sim N\left\{\begin{pmatrix} \theta \\ \vdots \\ \theta \end{pmatrix},\ \begin{pmatrix} \sigma^2+\delta^2 & \cdots & \delta^2 \\ & \ddots & \\ \delta^2 & \cdots & \sigma^2+\delta^2 \end{pmatrix}\right\}$$
$$\mathrm{Cor}(X_1, X_2) = \frac{\delta^2}{\sigma^2 + \delta^2}$$

More generally,
$$\begin{pmatrix} X_1 \\ \vdots \\ X_n \end{pmatrix} \sim N\left\{\begin{pmatrix} \mu_1 \\ \vdots \\ \mu_2 \end{pmatrix},\ \begin{pmatrix} \sigma_{11}^2 & \rho_{12}\sigma_{11}\sigma_{22} & \cdots \\ \cdots & \sigma_{22}^2 & \cdots \\ \cdots & \ddots & \cdots \end{pmatrix}\right\} \qquad \text{[sic: } \mu_2 \text{ presumably } \mu_n\text{]}$$
Not identically distributed, so they can't be exchangeable!

> ✔ Verified: for the equi-correlated normal, $\mathrm{Cov}(X_1,X_2)=\delta^2$ and $\mathrm{Var}(X_i)=\sigma^2+\delta^2$, so $\mathrm{Cor}=\delta^2/(\sigma^2+\delta^2)$; exchangeability of Example (2) follows since the density depends on the data only through the permutation-symmetric statistic $\sum x_i$.

**2.4 Conditional expectations and variances**

There are two variables $X, Y$; the joint distribution and conditional distribution are $f_{X,Y}(x,y)$, $f_{X\mid Y}(x\mid y)$ respectively.

### PDF page 16 (booklet page 11)

(1) $E(X) = E_Y(E(X\mid Y))$
(2) $\mathrm{Var}(X) = E_Y[\mathrm{Var}(X\mid Y)] + \mathrm{Var}_Y[E(X\mid Y)]$
(3) $\mathrm{Cov}(X, Y) = E_Z[\mathrm{Cov}(X, Y\mid Z)] + \mathrm{Cov}[E(X\mid Z), E(Y\mid Z)]$ for a third random variable $z$

Suppose $X$ and $Y$:
$X, Y\mid \mu \overset{iid}{\sim} N(\mu, \sigma^2)$; $\mu \sim N(\theta, \delta^2)$; $\sigma^2, \delta^2, \theta$ are known.
$$\begin{pmatrix} X \\ Y \end{pmatrix} \sim N\left\{\begin{pmatrix} \theta \\ \theta \end{pmatrix},\ \begin{pmatrix} \delta^2+\sigma^2 & \delta^2 \\ \delta^2 & \delta^2+\sigma^2 \end{pmatrix}\right\}$$
$E(X) = E_\mu[E(X\mid \mu)] = E(\mu) = \theta$
$\mathrm{Var}(X) = E_\mu[\mathrm{Var}(X\mid \mu)] + \mathrm{Var}_\mu[E(X\mid \mu)] = \sigma^2 + \delta^2$
$\mathrm{cov}(X, Y) = E_\mu[\mathrm{cov}(X, Y\mid \mu)] + \mathrm{cov}_\mu[E(X\mid \mu), E(Y\mid \mu)] = E(0) + \mathrm{cov}_\mu[\mu, \mu] = 0 + \delta^2$
*[handwritten below: $\mathrm{Cor}(X,Y) = \frac{\delta^2}{\delta^2+\sigma^2}$, i.e. $\frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)\,\mathrm{Var}(Y)}}$]*

> ✔ Verified: applying the three laws to the normal mixture gives exactly $E(X)=\theta$, $\mathrm{Var}(X)=\sigma^2+\delta^2$, $\mathrm{Cov}(X,Y)=\mathrm{Var}(\mu)=\delta^2$, hence the handwritten correlation $\delta^2/(\delta^2+\sigma^2)$ is correct.

**2.5 Theorem: De Finetti**

Proved an elegant characterization theorem for an infinite sequence of exchangeable random variables. He proved that any such sequence is a mixture of iid random variables.

$X_1, \ldots, X_n\mid Y \overset{iid}{\sim} f_{X\mid Y}(x\mid y)$; $\quad y \sim g(y)$;
$$f_{(X_1,\ldots,X_n)}(x_1,\ldots,x_n) = \int\Big[\prod_{i=1}^n f_{X_i\mid Y}(x_i\mid y)\Big]g(y)\,dy$$
So if $X_1, \ldots, X_n$ are exchangeable, there exists $y$ such that $X_1, \ldots, X_n\mid y$ are iid, and $y \sim g(y)$.

**Example (1).**
$x_1, \ldots, x_n\mid y \overset{iid}{\sim} \mathrm{Bernoulli}(y)$; $\quad y \sim \mathrm{Beta}(\alpha, \beta)$, $0 < y < 1$
$$f(x_1, \ldots, x_n\mid y) = \prod_{i=1}^n y^{x_i}(1-y)^{1-x_i} = y^{\sum_{i=1}^n x_i}(1-y)^{n-\sum_{i=1}^n x_i}$$
$$f(y) = \frac{y^{\alpha-1}(1-y)^{\beta-1}}{B(\alpha,\beta)} \qquad \textit{[margin note: "(mixing distribution)"]}$$
$$f(x_1,\ldots,x_n) = \int_0^1 y^{\sum x_i}(1-y)^{n-\sum x_i}\,\frac{y^{\alpha-1}(1-y)^{\beta-1}}{B(\alpha,\beta)}\,dy = \int_0^1 \frac{y^{\sum x_i+\alpha-1}(1-y)^{n-\sum x_i+\beta-1}}{B(\alpha,\beta)}\,dy = \frac{B\left(\sum x_i+\alpha,\ n-\sum x_i+\beta\right)}{B(\alpha,\beta)}$$

> ✔ Verified symbolically: $\int_0^1 y^{a-1}(1-y)^{b-1}dy = B(a,b)$ with $a=\sum x_i+\alpha$, $b=n-\sum x_i+\beta$ — the closed form matches Example (2) on the previous page, as intended.

### PDF page 17 (booklet page 12)

**Example (2).**
$x_1, \ldots, x_n\mid \beta \overset{iid}{\sim} \mathrm{Gamma}(\alpha, \beta)$; $\quad \beta \sim \mathrm{Gamma}(\alpha_0, \beta_0)$ (HW)
Integrating out $\beta$, we have:
$$f(x_1,\ldots,x_n) = \int_0^\infty \Big\{\prod_{i=1}^n \frac{\beta^\alpha x_i^{\alpha-1}e^{-\beta x_i}}{\Gamma(\alpha)}\Big\}\cdot\frac{\beta_0^{\alpha_0}\beta^{\alpha_0-1}e^{-\beta_0\beta}}{\Gamma(\alpha_0)}\,d\beta$$
$$= \frac{\prod_{i=1}^n x_i^{\alpha-1}\,\beta_0^{\alpha_0}}{[\Gamma(\alpha)]^n\Gamma(\alpha_0)}\int_0^\infty \beta^{n\alpha+\alpha_0-1}e^{-\beta\left(\sum_{i=1}^n x_i+\beta_0\right)}\,d\beta
= \frac{\prod_{i=1}^n x_i^{\alpha-1}\,\beta_0^{\alpha_0}}{[\Gamma(\alpha)]^n\Gamma(\alpha_0)}\cdot\frac{\Gamma(n\alpha+\alpha_0)}{\left[\sum_{i=1}^n x_i+\beta_0\right]^{n\alpha+\alpha_0}}$$

> ✔ Verified symbolically: $\int_0^\infty \beta^{A-1}e^{-B\beta}d\beta = \Gamma(A)/B^A$ with $A=n\alpha+\alpha_0$, $B=\sum x_i+\beta_0$ — the displayed marginal is exact.

**Example (3).**
$x_1, \ldots, x_n\mid \lambda \overset{iid}{\sim} \mathrm{Poission}$ [sic] $(\lambda)$; $\quad \lambda \sim \mathrm{Gamma}(\alpha, \beta)$

**Note:** The mixing distribution is unique.

*[Right margin: handwritten scratch work carrying out Example (3) — $\int_0^\infty \prod\frac{\lambda^{x_i}e^{-\lambda}}{x_i!}\cdot\frac{\beta^\alpha\lambda^{\alpha-1}e^{-\beta\lambda}}{\Gamma(\alpha)}d\lambda$, collecting $\lambda^{\sum x_i+\alpha-1}e^{-(n+\beta)\lambda}$ and arriving at a $\frac{\Gamma(\sum x_i+\alpha)}{(n+\beta)^{\sum x_i+\alpha}}$ factor; partially legible, with "$\lambda>0$" noted.]*

**2.6 Likelihood Principle**

$\pi(\theta\mid D) \propto f(D\mid \theta)\pi(\theta)$
All information about $\theta$ lives in $\pi(\theta\mid D)$.
Bayes' theorem is the essential accompaniment to the scientific investigations (uncertainty).
If $\theta$ is one dimensional, all the information lives in the graph.

The only contribution the data make in Bayes' theorem is through the "probability" $p(D\mid \theta)$, considered as a function of $\theta$, it is called the **likelihood function**.
The **likelihood principle**, which states that the totality of information about $\theta$ provided by $D$, is given by the likelihood of $\theta$ for the observed $D$.
Generally, the principle requires consideration of a unique $D$, that is observed, but all possible values of $\theta$.

$X_1, \ldots, X_n\mid \theta \overset{iid}{\sim} N(\theta, \sigma^2)$, $\sigma^2$ is known.
$$\ell(\theta\mid x) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2\sigma^2}(x_i-\theta)^2} \text{ is the likelihood function.}$$

The problem of non-Bayesian methods is in the violation of this principle.
In considering data values that might have occurred, but did not, they become incoherent.
It is only after the data are observed that the principle applies.
Indeed almost all situations ultimately call for a judgement about a unique occasion and it is a great strength of the Bayesian view that it can handle them. This is a weakness of the

### PDF page 18 (booklet page 13)

frequentist view. *[handwritten near the section header: "(Non-Bayesian)"]*

$X_1, \ldots, X_n\mid \mu \overset{iid}{\sim} N(\mu, \sigma^2) \to$ likelihood function
$\mu \sim N(\theta, \delta^2) \to$ prior
$$\pi(\mu\mid x) \propto \prod_{i=1}^n\Big\{\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2\sigma^2}(x_i-\mu)^2}\Big\}\frac{1}{\sqrt{2\pi\delta^2}}e^{-\frac{1}{2\delta^2}(\mu-\theta)^2}$$
$$\pi(\mu\mid x) \propto \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n}{2}} e^{-\frac{1}{2\sigma^2}[(n-1)s^2+n(\bar{x}-\mu)^2]}\frac{1}{\sqrt{2\pi\delta^2}}e^{-\frac{1}{2\delta^2}(\mu-\theta)^2},$$
where $\bar{x} = \frac{\sum_{i=1}^n x_i}{n}$, $s^2 = \frac{\sum_{i=1}^n(x_i-\bar{x})^2}{n-1}$
$$\pi(\mu\mid x) \propto e^{-\frac{n}{2\sigma^2}(\bar{x}-\mu)^2 - \frac{1}{2\delta^2}(\mu-\theta)^2}$$
we can show that
$$\frac{n}{\sigma^2}(\bar{x}-\mu)^2 + \frac{1}{\delta^2}(\mu-\theta)^2 = \frac{1}{(1-\lambda)\delta^2}\big[\mu - (\lambda\bar{x}+(1-\lambda)\theta)\big]^2 + \frac{\lambda}{\delta^2}(\theta-\bar{x})^2, \qquad \lambda = \frac{\delta^2}{\delta^2+\frac{\sigma^2}{n}}$$
$$\pi(\mu\mid x) \propto e^{-\frac{1}{2(1-\lambda)\delta^2}[\mu-(\lambda\bar{x}+(1-\lambda)\theta)]^2}\cdot e^{-\frac{\lambda}{2\delta^2}(\theta-\bar{x})^2} \propto e^{-\frac{1}{2(1-\lambda)\delta^2}[\mu-(\lambda\bar{x}+(1-\lambda)\theta)]^2}$$
It is a normal distribution. So, $\mu\mid x \sim N\big[\lambda\bar{x}+(1-\lambda)\theta,\ (1-\lambda)\delta^2\big]$

> ✔ Verified symbolically (SymPy): (i) the sufficiency decomposition $\sum(x_i-\mu)^2=(n-1)s^2+n(\bar x-\mu)^2$ is an identity; (ii) with $\lambda=\delta^2/(\delta^2+\sigma^2/n)$ the completing-the-square identity holds exactly, giving the stated posterior. Note this is the $n$-observation generalization of the Groceries result on booklet p. 6 ($n=1$).

**2.7 Probability (subjective)**

There only needs to be one view of probability, a person's judgement, about a quantity that is unknowm [sic] to him. This is the subjective (or personalistic) view of probability. In this view, probability does not exist outside the subject. There is no true probability, but rather an expression of a relationship between you and the world. Bayesian view is not subjective, and it is severely contrained [sic] by coherence, and by the role of data. *[margin note: "Lindley 1983"]*

De Finietti [sic] (1974) wrote,
"*The only objective view of probability is the subjective one, because it can be tested by the rules of probability.*"
In practice, two scientists may disagree, but data and coherence will bring them together.
Subjective probability in its interpretation contains no element of repetition: it has no frequentist basis.
This is different from non-Bayesian methods.

**2.7.1 Empirical view of probability**

e.g. Toss coin 10,000 times and count the number of heads.
We can say $P(\text{heads}) = \frac{6000}{10000} = 0.6$
We can also use the notion of symmetry of the coin; for a 'fair' coin $P(\text{heads}) = \frac{1}{2}$

e.g. We have data: $120, 125, 130, 160, 150$ *lbs*

### PDF page 19 (booklet page 14)

$$P(X > 120) = \frac{\#\,of\,weights > 120}{5} = \frac{4}{5}$$
vague information!
e.g. **Degree of belief**
e.g. $P(\text{rain tomorrow}) = \frac{1}{3}$
$P(\text{Dow Jones index goes up}) = \frac{3}{4}$

> ✔ Verified: of the five weights $(120, 125, 130, 160, 150)$, four exceed $120$ — so $4/5$ is right under the strict inequality (the value $120$ itself is not $>120$).

**2.7.2 Multiplication rule**

$f(x, y) = f(x\mid y)f(y)$
$$f(x_1, x_2, \ldots, x_n) = f(x_1)f(x_2\mid x_1)f(x_3\mid x_1, x_2)\cdots f(x_n\mid x_1, \ldots, x_{n-1}).$$
*[handwritten beneath, starred: "Computational trick"; right-margin notes: "$\to$ multiply/factorize" (partly legible) and "data augmentation"]*

**2.7.3 Bayesian view of Probability**

$f(x) = \int f(x, y)dy = \int f(x\mid y)f(y)dy$. Note that if I remove the integral sign, I get $f(x, y)$. *[this whole sentence is circled by hand]*

In summary, there are five steps in Bayesian statistics.

1. Obtain the full probabilistic models of the observables and nonobservables. Need scientific judgement.
2. Obtain the conditional distribution of the unobservables given the observables,
$$p(\theta\mid D) \propto p(D\mid \theta)p(\theta), \quad \text{Bayes' theorem}$$
3. Fit the model and do a sensitivity study of the model assumptions. (This is called assessment of the model.)
4. Give estimates and ranges of interesting parameters. May perform tests. Typically prediction of unobservables is important – Bayesian predictive inference.
5. What are the substantial conclusions? Are these results reasonable? (Need a scientist.)

**Models**

$X_1, \ldots, X_n$ (data), $\theta$ (unknown)
Have a prior on $\theta$, $\pi(\theta)$
Likelihood function: Have density $f(x\mid \theta)$
Posterior distribution: $\pi(\theta\mid x) \propto f(x\mid \theta)\pi(\theta)$
$$\pi(\theta\mid x) = \frac{f(x\mid \theta)\pi(\theta)}{\int f(x\mid \theta)\pi(\theta)d\theta}$$

### PDF page 20 (booklet page 15)

We need the normalization constant to be proper, $\int f(x\mid \theta)\pi(\theta)d\theta < \infty$
Interest in $\theta_1$: $\pi(\theta_1\mid x) = \int\cdots\int \pi(\theta\mid x)\,d\theta_2\ldots d\theta_k$ (use Markov chain Monte Calo [sic] (MCMC) methods).
$\pi(\theta_1\mid x) = \pi(\theta_1, \hat{\theta}_{(1)}\mid x)$, where $\hat{\theta}_{(1)}$ is some estimate of $\theta_{(1)}$ and $\theta_{(1)}$ excludes $\theta_1$, is **incoherent**.
Should use the extension rule (i.e., integration).

### PDF page 21 (booklet page 16)

*(Blank page — running header only.)*

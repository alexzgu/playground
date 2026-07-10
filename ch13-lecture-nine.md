# Chapter 13 — Lecture Nine
*(PDF pages 144–149; booklet pages 139–144)*


### PDF page 144 (booklet page 139)

# Chapter 13 — Lecture Nine

$$\underset{k\times 1}{n} \mid \theta \sim Multi(n, \theta)$$

$$\theta = (\theta_1, \dots \theta_k)$$

$$\sum_{i=1}^{k}\theta_i = 1,\; \theta_i > 0,\; n_i \ge 0,\; \sum_{i=1}^{k} n_i = n$$

$$\theta \sim Dirichlet(\alpha),\; \alpha_i > 0,\; \sum_{i=1}^{k}\alpha_i = \tau$$

$$\alpha = 1 \qquad \text{uniform prior}$$

$$\theta \mid n \sim Dirichlet(n + \alpha)$$

> ✔ Verified: Dirichlet(1,...,1) has a density that is constant on the simplex (uniform prior), equal to (k-1)!.

> ⚠ Check could not run (error): Multinomial likelihood times Dirichlet(alpha) prior yields exactly the Dirichlet(n+alpha) posterior. — timed out after 90s

*(The booklet writes $n$, $\theta$, $\alpha$ and the constant $1$ with under-tildes to indicate vectors; the subscript $k\times 1$ under $n$ gives its dimension.)*

$\tau$ is interpreted as the number of parameters the prior is worth.

Jeffrey's [sic] Prior $\alpha = \frac{1}{2}1$

> ⚠ Check FAILED: Jeffreys prior for the multinomial is proportional to prod theta_i^{-1/2}, i.e. Dirichlet(alpha_i = 1/2). — the stated result did not reproduce (see verification log)

Haldaness' [sic] prior $\alpha = -1$ *(the minus sign is faint in the scan (?); the vector $1$ carries an under-tilde)*

**Two-way Table of Counts**

|        | gender 1 | gender 2 |
| ------ | -------- | -------- |
| race1  | $n_{11}$ | $n_{12}$ |
| race2  | $n_{21}$ | $n_{22}$ |

$n_{11} + n_{12} + n_{21} + n_{22} = n \qquad n = (n_{11}, n_{12}, n_{21}, n_{22})$

Assuming a random sample

$$n \mid \theta \sim Multi(n, \theta)$$

$$\theta \sim Dir(1)$$

$\theta = (\theta_{11}, \theta_{12}, \theta_{21}, \theta_{22}).$

---
139

### PDF page 145 (booklet page 140)

Test of independence of the two variables

$$\theta_{11} = \theta_{1\cdot}\theta_{\cdot 1}$$
$$\theta_{12} = \theta_{1\cdot}\theta_{\cdot 2}$$

$$n \mid \theta \sim Multi(n, \theta)$$
$$\theta_{1\cdot} \sim Beta(1,1)$$
$$\theta_{\cdot 1} \sim Beta(1,1)$$

*(The booklet writes $n$, $\theta$, $\alpha$, $\mu$ with under-tildes to indicate vectors.)*

Need Bayes' factor $\dfrac{f_{M_1}(n)}{f_{M_0}(n)}$ where

$$f_{M_1}(n) = \int f_{M_1}(n \mid \theta)\pi(\theta)d\theta.$$

If $\theta \sim Dir(\alpha)$

$$\pi(\theta) = \frac{\theta_{11}^{\alpha_{11}-1}\theta_{12}^{\alpha_{12}-1}\theta_{21}^{\alpha_{21}-1}\theta_{22}^{\alpha_{22}-1}}{Dir(\alpha)}$$

in this problem $\pi(\theta) = \dfrac{1}{Dir(1)} = \dfrac{\Gamma(4)}{\Gamma(1)} = 3!$.

> ✔ Verified: For the four-cell uniform Dirichlet, $1/Dir(1,1,1,1) = \Gamma(4)/\Gamma(1) = 3! = 6$.

$$
\begin{aligned}
f_{M_1}&(n)\\
=&\frac{n!\,3!}{n_{11}!n_{12}!n_{21}!n_{22}!}\int \theta_{11}^{n_{11}}\theta_{12}^{n_{12}}\theta_{21}^{n_{21}}\theta_{22}^{n_{22}}\,d\theta\\
=&\frac{n!\,3!\,Dir(n_{11}+1, n_{12}+1, n_{21}+1, n_{22}+1)}{n_{11}!n_{12}!n_{21}!n_{22}!}\int \frac{\theta_{11}^{n_{11}+1-1}\theta_{12}^{n_{12}+1-1}\theta_{21}^{n_{21}+1-1}\theta_{22}^{n_{22}+1-1}}{Dir(n_{11}+1, n_{12}+1, n_{21}+1, n_{22}+1)}\,d\theta
\end{aligned}
$$

> ✔ Verified: The simplex integral of the multinomial kernel equals the Dirichlet normalizing constant with parameters shifted by one: $\int \prod \theta_{ij}^{n_{ij}} d\theta = Dir(n_{11}+1,\dots,n_{22}+1)$.

## **13.1 Hierarchical Multinomial-Dirichlet Model**

If we have groups of counts

$$\underset{k\times 1}{n_i} \Big| \underset{k\times 1}{\theta_i} \sim multi(n_i, \theta_i)_{k\times 1} \tag{13.1}$$

$$\theta_{ij} > 0 \qquad \sum_{j=1}^{k}\theta_{ij} = 1$$

$$\theta_i \mid \mu, \tau \sim Dir(\mu, \tau) \tag{13.2}$$

$$\pi(\mu, \tau) = \frac{(k-1)!}{(\tau+1)^2} \tag{13.3}$$

> ✔ Verified: $\pi(\mu,\tau) = (k-1)!/(\tau+1)^2$ integrates to 1 over the simplex in $\mu$ times $\tau \in (0,\infty)$.

### PDF page 146 (booklet page 141)

It is called Multinomial-Dirichlet Hierarchical Model and this is another small area model. *e.g.,* *(Nandram JSCS 1998)*

*[A large blank space separates the opening sentence from the displayed equations below.]*

*(The booklet writes $\theta$, $\mu$, $n$ with under-tildes to indicate vectors.)*

$$\pi(\theta,\mu,\tau\mid n) \propto \prod_{i=1}^{\ell}\left\{\, n_i!\,\prod_{j=1}^{k}\{\theta_{ij}^{n_{ij}}\mid n_{ij}\} \times \frac{\sum_{j=1}^{k}\theta_{ij}^{\mu_j\tau-1}}{D(\mu\tau)} \right\} \times \frac{1}{(1+\tau)^2}$$

$\text{[sic: the second factor is printed as } \{\theta_{ij}^{n_{ij}}\mid n_{ij}\}\text{; it should be } \theta_{ij}^{n_{ij}}/n_{ij}!\text{. Also the numerator is printed with } \sum_{j=1}^{k}\text{, but the Dirichlet kernel requires } \prod_{j=1}^{k}\theta_{ij}^{\mu_j\tau-1}\text{, as written correctly in the third display below.]}$

$$\theta_i \mid n_i, \mu, \tau \sim Dir(n_i + \mu\tau) \qquad i = 1, ..., \ell$$

> ⚠ Check could not run (error): Multinomial × Dirichlet($\mu\tau$) gives Dirichlet($n_i + \mu\tau$): the kernel $\prod_j \theta_j^{n_j+\tau\mu_j-1}$ integrates over the simplex to $D(n+\mu\tau)=\prod_j\Gamma(n_j+\tau\mu_j)/\Gamma(\sum_j(n_j+\tau\mu_j))$. — timed out after 90s

$$\pi(\mu,\tau\mid\theta,n) \propto \frac{1}{(1+\tau)^2}\prod_{i=1}^{\ell}\frac{\prod_{j=1}^{k}\theta_{ij}^{\tau\mu_j-1}}{D(\mu\tau)}$$

$$\pi(\mu\mid\tau,\theta,n) \propto h(\mu), \qquad \sum_{j=1}^{k}\mu_i = 1, \qquad \mu_i > 0, \qquad \sum_{j=1}^{k-1}\mu_j + \mu_k = 1$$

$\text{[sic: the first constraint is printed } \sum_{j=1}^{k}\mu_i=1\text{, mixing the summation index } j \text{ with the subscript } i\text{; it should read } \sum_{j=1}^{k}\mu_j=1\text{.]}$

$$0 \le \mu_k = 1 - \sum_{j=1}^{k-1}\mu_j \le 1$$

$$0 \le 1 - \sum_{j=2}^{k-1}\mu_j - \mu_1 \le 1$$

> ✔ Verified: $1-\sum_{j=1}^{k-1}\mu_j$ equals $1-\sum_{j=2}^{k-1}\mu_j-\mu_1$.

$$-\left[1 - \sum_{j=2}^{k-1}\mu_j\right] \le -\mu_1 \le 1 - \left[1 - \sum_{j=2}^{k-1}\mu_j\right]$$

> ✔ Verified: the chain $-[1-S] \le -\mu_1 \le 1-[1-S]$ is the chain $0 \le 1-S-\mu_1 \le 1$ shifted by $-(1-S)$, where $S=\sum_{j=2}^{k-1}\mu_j$.

$$0 < \mu_1 < 1 - \sum_{j=2}^{k-1}\mu_j \qquad , i = 1, ..., \ell$$

> ⚠ Check FAILED: $-[1-S] \le -\mu_1$ is equivalent to $\mu_1 \le 1-S$, giving the stated upper bound. — the stated result did not reproduce (see verification log)

$$\pi(\mu_1\mid\mu_{(1)},\tau,\theta,n) \propto h(\mu_1,...,\mu_k) = h\left(\mu_1,...\mu_{k-1}, 1 - \sum_{j=2}^{k-1}\mu_j - \mu_1\right)$$

> ✔ Verified: the final argument of $h$, namely $1-\sum_{j=2}^{k-1}\mu_j-\mu_1$, equals $\mu_k$ under $\sum_{j=1}^{k}\mu_j=1$.

$$\text{where } 0 < \mu_1 < 1 - \sum_{j=2}^{k-1}\mu_j \qquad , i = 1, ..., \ell.$$

### PDF page 147 (booklet page 142)

**13.2 Data Augmentations**

$$\pi(p,q|x) \propto (p+q)^x p^{n-x}, \qquad x = 0,1,...,n, 0 < p,q < 1, slicesampler$$

$$\pi(p,q,\mu|x) \propto I(\mu < (p+q)^x)p^{n-x}$$

$$\pi(p,q|x) \propto \left[\sum_{z=0}^{x} \binom{x}{z} p^z q^{x-z}\right] p^{n-x}$$

> ✔ Verified: The binomial expansion used to introduce the latent variable: $\sum_{z=0}^{x}\binom{x}{z}p^z q^{x-z} = (p+q)^x$.

$$\pi(p,q,z|x) \propto \binom{x}{z} p^z q^{x-z} p^{n-x}, dataaugmentation(notaslicesampler)$$

$$z = 0,...,x \quad , 0 < p,q < 1$$

$$\pi(z|p,q,x) \qquad z|p,q,x \sim Binomial(x, \frac{p}{p+q})$$

> ✔ Verified: Normalizing the augmented joint $\pi(p,q,z\mid x)\propto\binom{x}{z}p^zq^{x-z}p^{n-x}$ over $z=0,\dots,x$ yields $z\mid p,q,x\sim Binomial(x,\;p/(p+q))$.

$$\pi(p|z,q,x) \qquad p|z,q,x \sim Beta(n-x+z+1, 1)$$

> ✔ Verified: Normalizing that joint over $p\in(0,1)$ yields $p\mid z,q,x\sim Beta(n-x+z+1,\,1)$.

$$\pi(q|z,p,x) \qquad q|z,p,x \sim Beta(x-z+1, 1)$$

> ✔ Verified: Normalizing that joint over $q\in(0,1)$ yields $q\mid z,p,x\sim Beta(x-z+1,\,1)$.

z is called a letent [sic] variable.

**13.3 Bayesian Nonparametrics**

Cornerstone is Dirichlet process

$\{\mathcal{X},\mathcal{B},\mathcal{P}\}$, § [sic: presumably $\mathcal{X}$] is a sample sapce [sic], $\mathcal{B}$ is Borel field and $\mathcal{P}$ is a collection of probability measures.

1. $\emptyset \in \mathcal{B}$

2. $A \in \mathcal{B}$ then $A^c \in \mathcal{B}$ (closed under complementation)

3. $A_1, A_2, ... \in \mathcal{B}$, then $\cup_{i=1}^{\infty} A_i \in \mathcal{B}$ (closed under countable unions)

$\mathbb{P} : \mathcal{B} \to [0,1]$

1. $\mathbb{P}(A) \geq 0$

2. $\mathbb{P}(S) = 1$

3. $A_1, A_2, ...$ disjoint in $\mathcal{B}$, then $\mathbb{P}\left(\cup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} \mathbb{P}(A_i)$

**13.4 What is a Dirichlet process?**

let $A_1, ... A_k$ be a partition of $X$ in $\mathcal{B}$. $\mathbb{G} \in \rho$ [sic: presumably $\mathcal{P}$], G could be a CDF, and $\mathbb{G}(A_1)$ is the probability of $A_1$.

Suppose $\mathbb{G}_0$ is a baseline probability measure. $\mathbb{G}$ varies around $\mathbb{G}_0$.

### PDF page 148 (booklet page 143)

Now suppose

$$(\mathbb{G}(A_1), ..., \mathbb{G}(A_k)) \sim Dirichlet(\alpha \mathbb{G}_0(A_1), ..., \alpha \mathbb{G}_0(A_k))$$

> ✔ Verified: For a finite measurable partition $A_1,\dots,A_k$ of $\mathcal{X}$, the Dirichlet parameters $\alpha\mathbb{G}_0(A_i)$ sum to $\alpha$, and the resulting Dirichlet marginal means are $E[\mathbb{G}(A_i)] = \mathbb{G}_0(A_i)$.

$\alpha$ is the concentration parameter. Suppose this is true for all finite measurable partitions of $\mathcal{X}$.

Then $\mathbb{G}$ follows a Dirichlet process, we write

$$\mathbb{G} \sim DP(\alpha, \mathbb{G}_0).$$

Ferguson (1973): $\mathbb{G}$ is discrete with probability one of [sic: presumably "if"] $\mathbb{G}_0$ smooth. $\mathbb{G}_0$ e.g. $N(\mu, \sigma^2)$.

This is the reason why the Dirichlet process is useful for clustering.

We say that $\mathbb{G} \sim DP(\alpha, \mathbb{G}_0)$ is a Dirichlet process prior.

**13.4.1 Dirichlet Process Model**

Suppose we have baseline model:

$$y_1, ... y_n \mid \mu, \sigma^2 \overset{iid.}{\sim} N(\mu, \sigma^2)$$
$$\pi(\mu, \sigma^2) \propto \frac{1}{\sigma^2}$$

$y_1, ... y_n \mid \mathbb{G} \overset{iid}{\sim} \mathbb{G}$
$\mathbb{G} \sim DP(\alpha, \mathbb{G}_0)$
$\pi(\alpha, \mu, \sigma^2)$

*(The three lines above are set flush left in the booklet, not centered like the displayed baseline model; $\pi(\alpha,\mu,\sigma^2)$ is written with no relation symbol or right-hand side.)*

**13.4.2 Dirichlet Process Mixture Model**

$$y_{ij} \mid \mu_i, \sigma^2 \overset{iid.}{\sim} N(\mu_i, \sigma^2), i = 1, \ldots, \ell, j = 1, \ldots, n_i$$
$$\mu_i \mid \theta, \delta^2 \overset{iid.}{\sim} N(\theta, \delta^2)$$
$$\pi(\theta, \sigma^2, \delta^2)$$
$$y_{ij} \mid \mu_i \sigma^2 \overset{iid.}{\sim} N(\mu_i, \sigma^2)$$
$$\mu_i \mid \mathbb{G} \sim \mathbb{G}$$
$$\mathbb{G} \sim DP(\alpha, \mathbb{G}_0)$$

*(In the fourth line the booklet writes $\mu_i \sigma^2$ with no comma between the conditioning arguments — [sic].)*

This model would generally give clusters of $\mu_1, \ldots, \mu_\ell$.

For example, with $\ell = 5$, we have $\mu_1, \mu_2, \mu_3, \mu_4, \mu_5$ and the Dirichlet process might give $\mu_1, \mu_2, \mu_3, \mu_3, \mu_1$; that is, three clusters of sizes $2, 2, 1$.

> ⚠ Check could not run (unsafe): With $\ell = 5$, the realization $(\mu_1, \mu_2, \mu_3, \mu_3, \mu_1)$ has exactly 3 distinct clusters, of sizes 2, 2, 1. — disallowed import: collections

### PDF page 149 (booklet page 144)

*(Blank page — running header only.)*

# Chapter 14 — Nonparametric Bayesian Statistics
*(PDF pages 150–164; booklet pages 145–156)*


### PDF page 150 (booklet page 145)

# Chapter 14 — Nonparametric Bayesian Statistics

**14.1 Dirichlet Process**

Urn contains a number of balls of a fixed number(k) of colors.
Draw a ball at random. Note its color.
Put two balls of the same color back into the urn. [Imagine another urn with an infinite number of balls of each of the k colors.]
*[the bracketed sentence "[Imagine another urn ... k colors.]" is hand-underlined with a single sweeping stroke that trails off into the left margin]*
$P_j$ : the proportion of balls of color j after N draws, $j = 1, ..., k$
Then, $(P_1, P_2, ..., P_k) \overset{d}{\to} \text{Dirichlet}(\alpha_1, \alpha_2, ..., \alpha_k)$, where $\alpha_j$ is the number of balls of the $j^{th}$ color initiatively [sic] in the urn, $j = 1, ..., k$.

> ✔ Verified: The Pólya urn (draw a ball, return it plus one more of the same color) started from $\alpha=(2,1,3)$ assigns to the color sequence $(1,1,2)$ exactly the probability $E[P_1^2 P_2]$ under $\text{Dirichlet}(2,1,3)$, and the Dirichlet marginal mean is $E[P_1]=\alpha_1/\sum_j\alpha_j$; hence the urn proportions have the Dirichlet law the booklet asserts.

**14.1.1 Generalized Polya Urn**

Urn1: finite number(n) of balls of different colors (each color has at least one ball).
Urn2: has a continual [sic] of colors, with probability proportional to $\alpha$, draw a ball from urn2, and with probability proportional to n, draw it from urn1.

If a ball is drawn from urn2, this is a new ball(different color from urn1), place it in urn1.

If a ball is drawn from urn1, replace two balls of its same color to urn1. Then process continuous [sic] indefinitely. This process is, in fact, the Dirichlet Process, and the visual representation is called the Polya Urn Scheme - Blackwell and Mac Queen (1973).

Remarks: (1) If $\alpha$ is large, new balls will tend to be placed in urn1.
(2) If $\alpha$ is small, the number of old balls will increase, "rich gets richer scheme".
(3) Since $\alpha$ is fixed, as the number of balls in urn1 increases, n will dominate $\alpha$ and there will be more and more old balls in urn1.

Comment: Actually, the Dirichlet Process is a stochastic process (evolution) of the "measurements" as the process goes on. The colors of the balls is another stochastic process, called the Polya Urn Scheme or Chinese Restaurant Process. This definition is not particularly

### PDF page 151 (booklet page 146)

important.

**Chinese Restaurant Process(CRP)**

Have a Chinese restaurant with an unbounded number of tables. Each parameter $\mu_i$ denotes a customer who enters the restaurant. A table occupied is denoted by $\mu_i^{\star}$. Next customer enters, sits at a table already occupied with probability proportional to the number of people already seated there and sits at a new table with probability proportional to $\alpha > 0$.

**Dirichlet Process(DP)**

Let $\{S, \beta\}$ be a probability space. $S$: sample space. $\beta$: Borel field.
Let $G_0(\cdot)$ be a probability measure over $\{S, \beta\}$.
Let $\alpha > 0$ real number (strictly positive).

A Dirichlet process, denoted by $DP(\alpha, G_0)$, is the definition of a random measure G(.) over $\{S, \beta\}$ with the following property:

For any finite measurable partitions $A_1, ..., A_r$ of S, the vector

$$(G(A_1), ..., G(A_r)) \sim \text{Dirichlet}(\alpha G_0(A_1), ..., \alpha G_0(A_r))$$

Write $G \sim DP(\alpha, G_0)$

NOTE: The DP is a measure on measures!

Ferguson(1973) established the existence of Dirichlet Process(DP). He also showed that DP is discrete with probability one.

Let $\mu_1, ..., \mu_l$ be n [sic: the parameters are indexed to $l$, but the count is stated as $n$] parameters indexing a set of clusters (groups of data). *(The booklet writes $\mu$ with under-tildes to indicate vectors.)*
Suppose these parameters follow the DP. Then, we can write:
Dirichlet Process Mixture (DPM)

$$\mu_1, ..., \mu_l \mid G \sim G$$

$$G \mid \alpha \sim DP(\alpha, G_0)$$

Note that $E(G) = G_0$. $\alpha$ is a concentration (variability) parameter.

> ✔ Verified: The Dirichlet marginal of a DP has mean $G_0$: if $(G(A_1),\dots,G(A_r))\sim\text{Dirichlet}(\alpha G_0(A_1),\dots,\alpha G_0(A_r))$ with $\sum_i G_0(A_i)=1$, then $E(G(A_i))=G_0(A_i)$; the variance $G_0(A_i)(1-G_0(A_i))/(\alpha+1)$ also vanishes as $\alpha\to\infty$, matching the booklet's limit statement.

As $\alpha \to \infty$, $\mu_1, ..., \mu_l \sim G_0$.
As $\alpha \to 0$, $\mu_1, ..., \mu_l$ become more and more similar.

That is, the DP is a clustering algorithm. There is a positive probability that some of these $\mu_i$ coincide.

### PDF page 152 (booklet page 147)

This clustering property is what makes the DP attractive in numerous applications(eg, machine learning-both unsupervised and supervised). It is also attractive because of its nonparametric nature.

**Consider the Dirichlet Process**

$$X_1,\ldots,X_n \mid G \overset{iid}{\sim} G$$

$$G \sim DP(\alpha, G_0)$$

Let k be the number of distinct values. Then,

$$f(x) = \int_G f(x \mid G) dG(x)$$

NOTE:

(1) So by De Finetti's representation theorem: $X_1, ..., X_n$ are exchangeable (equi-correlated and identically distributed).

(2) $\text{Cor}(X_i, X_j) = \dfrac{1}{1+\alpha}, i \neq j$

> ✔ Verified: For $X_i \mid G \overset{iid}{\sim} G$, $G \sim DP(\alpha, G_0)$, the correlation $\text{Cor}(X_i, X_j) = 1/(1+\alpha)$ for $i \neq j$.

(3) $X_i \sim G_0, \quad i = 1, \ldots, n$

(4) $X_1 \sim G_0$,

$$X_2 \mid x_1 \sim \frac{1}{\alpha+1}\delta_{x_1}(x_2) + \frac{\alpha}{\alpha+1}G_0(x_2)$$

$$X_3 \mid x_1, x_2 \sim \frac{1}{\alpha+2}\sum_{i=1}^{2}\delta_{x_i}(x_3) + \frac{\alpha}{\alpha+2}G_0(x_3)$$

> ✔ Verified: The Pólya-urn predictive mixture weights for $X_2 \mid x_1$ and $X_3 \mid x_1,x_2$ each sum to 1.

(5) Posterior distribution

$$G \mid x_1, ..., x_n \sim DP\{\alpha+n, \frac{1}{\alpha+n}\sum_{i=1}^{n}\delta_{x_i} + \frac{\alpha}{\alpha+n}G_0(x)\}$$

> ✔ Verified: The DP posterior base measure $\frac{1}{\alpha+n}\sum_{i=1}^n \delta_{x_i} + \frac{\alpha}{\alpha+n}G_0$ is a probability measure, and its precision is $\alpha+n$.

(6) Distinct values $X_1^*, ..., X_k^* \overset{iid}{\sim} G_0$

**Proof of (5)**

Consider a partition with K sets $(A_1, ..., A_k)$, any finite K. Let $n_j$ be the number of $X_1, ..., X_n$ following the $A_j, \quad j = 1, ..., k$. Then, given G:

$$(n_1, ..., n_k) \sim \text{Multi}(n, P) \tag{1}$$

where, $P_j = G(A_j), \quad j = 1, \ldots, k$

By the definition of a Dirichlet process,

$$(P_1, ..., P_k) \sim \text{Dirichlet}(\alpha P_1^{(0)}, ..., \alpha P_k^{(0)}) \tag{2}$$

### PDF page 153 (booklet page 148)

Then, by (1) and (2)

$$(P_1, ..., P_k) \mid n \sim \text{Dirichlet}\{(n+\alpha)\cdot\frac{n\cdot\frac{n_1}{n}+\alpha p_1^{(0)}}{n+\alpha}, ..., (n+\alpha)\cdot\frac{n\cdot\frac{n_k}{n}+\alpha p_k^{(0)}}{n+\alpha}\}$$

*(The booklet writes $n$, $x$, and $\mu_{(i)}$ with under-tildes to indicate vectors.)*

> ✔ Verified: Each Dirichlet parameter reduces to $n_j + \alpha p_j^{(0)}$, and the parameters sum to $n+\alpha$.

Thus,

$$G \mid x \sim DP\{\alpha+n, \frac{1}{\alpha+n}\sum_{i=1}^{n}\delta_{x_i} + \frac{\alpha}{\alpha+n}G_0\}$$

> ✔ Verified: The DP posterior base measure has total mass 1.

**14.1.2 Dirichlet Process Mixture (DPM) Model**

Let

$$y_{ij} \mid \mu_i, \phi \overset{\text{iid}}{\sim} f(\cdot \mid \mu_i, \phi), \quad i=1,...,l, \quad j=1,...,n_i$$

$$\mu_i \mid G \overset{\text{iid}}{\sim} G$$

$$G \sim DP(\alpha, G_0)$$

This is a very useful model.

-Escobar and West(1995) JASA 577-588
-Nandram and Choi(2004). Application on nonresponse
-Nandram and Yin(2016 a,b).

The structure of the DP is such that the posterior distribution will strongly support common values, if individual parameters that are 'close', these combining information locally in "space" to estimate the local structure.

Suppose,

$$\mu_i \mid G \overset{\text{iid}}{\sim} G, \quad i=1,\ldots,l$$

$$G \sim DP(\alpha, G_0)$$

Blackwell Mac Queen(1973) (Polya Urn Scheme, Chinese restaurant process)

**Theorem**

$$\mu_1 \sim G_0$$

$$\mu_i \mid \mu_{(i)}, \alpha \quad \begin{cases} = \mu_j & \text{with probability } \frac{1}{\alpha+i-1}\\[2pt] \sim G_0 & \text{with probability } \frac{\alpha}{\alpha+i-1}\end{cases}$$

where $\mu_{(i)} = (\mu_1, \mu_2, \ldots, \mu_{i-1}, \mu_{i+1}, \ldots, \mu_l), \quad j=1,\ldots,l$ $\text{[sic: for the case probabilities to sum to 1 the index must run } j=1,\ldots,i-1\text{]}$

> ✔ Verified: The Polya urn case probabilities sum to 1 with $j$ ranging over $1,\ldots,i-1$.

**Key Idea**
That is, there is a posterior probability that some values coincide.

### PDF page 154 (booklet page 149)

Suppose there are k (random) distinct values $\mu_1^*, ..., \mu_k^*$.
As the process goes on k will vary, so that k is a random variable.

Antoniak(1974) showed that:

$$P(k|\alpha,l) = c_l(k)\alpha^k \frac{\tau(\alpha)}{\tau(\alpha+l)}, \quad 1 \le k \le l$$

*(The booklet writes the gamma function as $\tau(\cdot)$ throughout this passage; $\tau(\alpha)/\tau(\alpha+l)$ is $\Gamma(\alpha)/\Gamma(\alpha+l)$.)*

> ⚠ Check could not run (error): With $c_l(k)=|s(l,k)|$, the Antoniak formula $P(k|\alpha,l)=c_l(k)\alpha^k\Gamma(\alpha)/\Gamma(\alpha+l)$ sums to 1 over $1\le k\le l$ and vanishes at $k=0$. — ImportError: cannot import name 'stirling' from 'sympy' (/home/codespace/.local/lib/python3.12/site-packages/sympy/__init__.py)

$c_l(k)$ are the absolute value of the stirling [sic] number of the first kind obtained by equality:

$$\prod_{k=0}^{l-1}(x-k) = \sum_{k=0}^{l} c_l(k)x^k$$

*(sic: the product index $k$ collides with the summation index $k$; and with the minus sign the expansion produces the signed Stirling numbers $s(l,k)$ — the absolute values $c_l(k)$ come from the rising factorial $\prod_{k=0}^{l-1}(x+k)$.)*

> ⚠ Check could not run (error): The unsigned Stirling numbers come from the rising factorial; the product as printed with $(x-k)$ yields the signed Stirling numbers. — ImportError: cannot import name 'stirling' from 'sympy' (/home/codespace/.local/lib/python3.12/site-packages/sympy/__init__.py)

Recently, Raumasen(2000) [sic] stated that:

$$\frac{\alpha^k\tau(\alpha)}{\tau(\alpha+l)} \text{ is logconcave in } ln(\alpha), \quad \alpha > 0$$

> ⚠ Check could not run (unsafe): $\alpha^k\Gamma(\alpha)/\Gamma(\alpha+l)$ is log-concave in $\ln\alpha$ for $\alpha>0$ (second derivative $\le 0$; identically 0 when $l=1$). — disallowed import: mpmath

**Theorem**
Escobar(1994) Ferguson(1973)

$$\mu_i \mid \mu_{(i)}, y, \Omega, \alpha \quad
\begin{cases}
= \mu_j & \text{with probability } Q_j \quad j \neq i\\[4pt]
\sim \mu_i \mid y, \Omega & \text{with probability } l - \sum_{j\neq 0}^{l} Q_j
\end{cases}$$

*(The booklet writes $\mu_{(i)}$ and $y$ with under-tildes to indicate vectors.)*
*(sic: the second probability is printed as "$l - \sum_{j\neq 0}^{l} Q_j$"; the intended statement is $1 - \sum_{j\neq i} Q_j$.)*

where, $\mu_{(i)} = (\mu_1, \mu_2, \ldots, \mu_{i-1}, \mu_{i+1}, \ldots, \mu_l)$,

$$Q_j = \frac{f(y_i \mid \mu_j)}{\alpha A(y_i,\Omega) + \displaystyle\sum_{\substack{j=1\\ j\neq i}}^{l} f(y_i \mid \mu_j)}$$

$$A(y_i,\Omega) = \int f(y_i \mid \mu_i)\,\pi(\mu_i \mid \Omega)\,d\mu_i$$

Same as $f(y_i \mid \Omega)$, $\quad \Omega$ other parameters

Note: At any stage of the process, there will be $1 \le k \le l$ dectract [sic] values of $\mu_1, \ldots, \mu_k$ , denoted by $\mu_1^*, \ldots, \mu_k^*$

Also write a prior on $\alpha$, $\pi(\alpha)$, we can write down the posterior density of $\alpha$,

$$\begin{aligned}
\pi(\alpha \mid k) &\propto \pi(\alpha) P(k \mid \alpha, l)\\
&= \pi(\alpha)\alpha^k \frac{\tau(\alpha)}{\tau(\alpha+l)}
\end{aligned}$$

### PDF page 155 (booklet page 150)

I have used $\pi(\alpha) = \dfrac{1}{(1+\alpha)^2}, \quad \alpha > 0.$ ( Nandram and Choi, 2004).

> ✔ Verified: $\pi(\alpha)=1/(1+\alpha)^2$ on $\alpha>0$ integrates to exactly 1 (a proper prior).

In my opinion, others have used proper gamma priors, but inference is sensitive to its parameters.( Nandram and Yin, 2016 a, b).

Conditional posterior densities for all other parameters are obtained replacing $\mu_1, \ldots, \mu_k$ by $\mu_1^*, \ldots, \mu_k^*$ at each stage of sampling process (e.g. Gibbs Sampler)

$$
\begin{aligned}
\mu_1^* & \qquad i \in I_1 \\
\mu_2^* & \qquad i \in I_2 \\
\vdots & \\
\mu_k^* & \qquad i \in I_k
\end{aligned}
$$

You have known groups of $\mu_1, \ldots, \mu_k$ into $k$ groups.

Then, use the complete model into the baseline $G_0$.

**Examples**

(1) Parametric: Normal Means

$$
\begin{aligned}
y_{ij} \mid \mu_i, \sigma^2 &\overset{iid}{\sim} \mathcal{N}\left(\mu_i, \sigma^2\right) \\
\mu_i \mid \theta, \delta^2 &\overset{iid}{\sim} \mathcal{N}\left(\theta, \delta^2\right)
\end{aligned}
$$

$$
\pi(\theta) = 1
$$

$$
\begin{cases}
\sigma^2 \sim \operatorname{Gam}\left(\frac{q}{2}, \frac{\sigma}{2}\right) \\
\delta^2 \sim \operatorname{Gam}\left(\frac{q}{2}, \frac{\sigma}{2}\right)
\end{cases} \text{independent}
$$

Nonparametric: Dirichelet [sic] Process

$$
\begin{aligned}
y_{ij} \mid \mu_i, \sigma^2 &\overset{iid}{\sim} \mathcal{N}\left(\mu_i, \sigma^2\right) \quad i = 1, \cdots, l \\
& \hphantom{\overset{iid}{\sim} \mathcal{N}\left(\mu_i, \sigma^2\right) \quad } j = 1, \cdots, n_i
\end{aligned}
$$

$$
\begin{aligned}
\mu_i \mid G &\overset{iid}{\sim} G \\
G \mid \alpha &\sim DP\left(\alpha, G_0\right)
\end{aligned}
$$

$$
\pi(\alpha)
$$

$$
\sigma^2 \sim \operatorname{Gam}\left(\frac{q}{2}, \frac{\sigma}{2}\right) \text{ independent}
$$

(2) Parametric: Beta-binomial

$$
\begin{aligned}
y_{ij} \mid p_i &\overset{iid}{\sim} \operatorname{Ber}(p_i) \\
p_i \mid \mu, \tau &\sim \operatorname{Beta}(\mu\tau, (1-\mu)\tau)
\end{aligned}
$$

$$
\pi\left(\mu, \tau\right) = \frac{1}{(\tau+1)^2} \quad 0 < \mu < 1, \tau > 0
$$

independent

> ✔ Verified: $\pi(\mu,\tau)=1/(\tau+1)^2$ on $0<\mu<1,\ \tau>0$ is a proper joint density integrating to 1, and factors into independent Uniform(0,1) and $(\tau+1)^{-2}$ marginals.

Nonparametric: Dirichelet [sic] Process

$$
\begin{aligned}
y_{ij} \mid p_i &\overset{iid}{\sim} \operatorname{Ber}(p_i) \quad i = 1, \cdots, l \\
& \hphantom{\overset{iid}{\sim} \operatorname{Ber}(p_i) \quad } j = 1, \cdots, n_i
\end{aligned}
$$

$$
\begin{aligned}
p_i \mid G &\overset{iid}{\sim} G \\
G \mid\ &\sim D\left(\alpha, G_0\right)
\end{aligned}
$$

*(The conditioning bar in $G\mid\;\sim D(\alpha,G_0)$ has nothing after it — [sic: the conditioning variable $\alpha$ is omitted, cf. $G\mid\alpha\sim DP(\alpha,G_0)$ in Example (1)]. Note also $D$ here for the $DP$ of Example (1).)*

$$
\pi(\alpha)
$$

### PDF page 156 (booklet page 151)

The Dirichlet process increases the flexibility of such models extensively. There are very little issue about model diagnostics and model choices. However, I think that it is still necessary to access the goodness of fit at $G_0$ and sensitivity of its specification (Nandram and Yin, 2016 a b).

**Normal Means**

*(The booklet writes $y$ with under-tildes to indicate vectors.)*

$$P\left(y_i \mid \mu_i, \Omega\right) = \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n_i}{2}} e^{-\frac{1}{2\sigma^2}\left[(n_i-1)s_i^2 + n_i(\bar{y}_i - \mu_i)^2\right]}$$

$$P\left(y_i \mid \mu_j, \Omega\right) = \left(\frac{1}{2\pi\sigma^2}\right)^{\frac{n_i}{2}} e^{-\frac{1}{2\sigma^2}\left[(n_i-1)s_i^2 + n_i(\bar{y}_i - \mu_j)^2\right]}$$

$$P\left(y_i \mid \Omega\right) = \int \left(\frac{1}{2\pi v^2}\right)^{\frac{n_i}{2}} e^{-\frac{1}{2\sigma^2}\left[(n_i-1)S_i^2 + n_i(\bar{y}_i - \mu_i)^2\right]} \left(\frac{1}{2\pi\delta^2}\right)^{\frac{1}{2}} e^{-\frac{(\mu_i - \theta)^2}{2\delta^2}}\, du_i$$

$$\text{[sic: the base of the first factor is printed } 2\pi v^2 \text{, elsewhere } 2\pi\sigma^2 \text{; and the differential is printed } du_i \text{, should be } d\mu_i\text{]}$$

$$= \left(\frac{1}{2\pi^2}\right)^{\frac{n_i}{2}} \left(\frac{1}{2\pi\delta^2}\right)^{\frac{1}{2}} e^{-\frac{(n_i-1)S_i^2}{2\sigma^2}} \int e^{-\frac{n_i}{2\sigma^2}(\bar{y}_i - \mu_i)^2 - \frac{1}{2\delta^2}\left(u_i - \theta_1^2\right)}\, du_i$$

$$\text{[sic: } \tfrac{1}{2\pi^2} \text{ should be } \tfrac{1}{2\pi\sigma^2}\text{; the second exponent is printed } (u_i - \theta_1^2) \text{, should be } (\mu_i - \theta)^2\text{]}$$

$$= \left(\frac{1}{2\pi^2}\right)^{\frac{n_i}{2}} \left(\frac{1}{2\pi\delta^2}\right)^{\frac{1}{2}} e^{-\frac{(n_i-1)S_i^2}{2\sigma^2}} \cdot \sqrt{\frac{2\pi}{\frac{ni}{\sigma^2} + \frac{1}{\delta^2}}}\; e^{-\frac{1}{2}\left(\frac{\frac{n_i}{\sigma^2}\cdot\frac{1}{\delta^2}}{\frac{n_i}{\sigma^2} + \frac{1}{\delta^2}}\right)(\bar{y}_i - \theta)^2}$$

*(the subscript in $\frac{ni}{\sigma^2}$ under the radical is printed as an upright $ni$ [sic])*

> ✔ Verified: The Gaussian integral collapsing the two exponents equals $\sqrt{2\pi/(n/\sigma^2+1/\delta^2)}\,\exp\!\left(-\tfrac12\,\frac{(n/\sigma^2)(1/\delta^2)}{n/\sigma^2+1/\delta^2}(\bar{y}-\theta)^2\right)$.

$$Q_j = \frac{P\left(y_i \mid \mu_j, \Omega\right)}{\alpha P\left(y_i \mid \Omega\right) + \sum_{\substack{j=1 \\ j \neq i}}^{l} P\left(y_i \mid \mu_j, \Omega\right)} \qquad \text{Some calculation}$$

Gibbs Sampler:

$$\pi(\alpha \mid k, l) \propto \pi(\alpha) \cdot \frac{\alpha^k \tau(\alpha)}{\tau(\alpha + l)}$$

*(the booklet prints $\tau$ where the gamma function $\Gamma$ is meant [sic])*

$$\text{e.g. } \pi(\alpha) = \frac{1}{(1+\alpha)^2}, \quad \alpha > 0$$

> ✔ Verified: $\pi(\alpha)=1/(1+\alpha)^2$ on $\alpha>0$ is a proper (normalized) density.

**How to get $\theta, \sigma^2, \delta^2$ ? Go to parametric model**

Have,

$$y_{ij} \mid \mu_i, \sigma^2 \overset{iid}{\sim} N\left(\mu_i, \sigma^2\right)$$

$$\mu_i \mid \theta, \delta^2 \overset{iid}{\sim} N\left(\theta, \delta^2\right)$$

$$\pi\left(\theta, \sigma^2, \delta^2\right)$$

Now,

$$y_{ij} \mid \mu_i^*, \sigma^2 \overset{iid}{\sim} N\left(\mu_i^*, \sigma^2\right)$$

$$\mu_i^* \mid \theta, \delta^2 \overset{iid}{\sim} N\left(\theta, \delta^2\right)$$

### PDF page 157 (unnumbered insert)

*(This page is a handwritten loose-leaf insert in the instructor's hand; it carries no printed text and no page number. The whole transcript below is handwriting.)*

We have now,

$$y \mid z, \text{etc} \;\sim\; N\!\left(\mu 1 + P z,\; \sigma^2 I_{n\times n}\right); \qquad 1 \text{ is a } n\text{-vector of ones}$$

*(The booklet writes $y$, $z$, $1$, $\gamma$ with under-tildes to indicate vectors.)*

$$z \;\sim\; N\!\left(0,\; \sigma_z^2\,(?)\; I_{m_0\times m_0}\right)$$

$$\pi(\mu, \sigma^2, \rho) \;\propto\; \frac{1}{\sigma^2}$$

We can therefore sample

$$z,\ \mu,\ \rho,\ \sigma^2 \quad \text{easily.}$$

Letting

$$e_p = \sum_{i=1}^{n} I(d_i = p),$$

$$f_p = \sum_{i=1}^{n} I(d_i > p), \qquad p = 1,\dots,m_0,$$

We can show that

$$\gamma_p \mid \text{else} \;\overset{ind}{\sim}\; \text{Beta}\!\left(1-\delta_1+e_p,\; \frac{\delta_2}{1-\delta_2}+(p-1)\delta_1+f_p\right), \qquad p = 1,\dots,m_0$$

> ⚠ Check FAILED: Beta–Bernoulli conjugacy gives the stated full conditional for the stick-breaking weight $\gamma_p$. — the stated result did not reproduce (see verification log)

$$\pi(\delta_1,\delta_2 \mid \gamma, \text{etc}) \;\propto\; \prod_{p=1}^{m}\left\{\text{Beta}_{\gamma_p}\!\left(1-\delta_1,\; \frac{\delta_2}{1-\delta_2}+(p-1)\delta_1\right)\right\}$$

*(the product's upper limit is written as a bare "$m$" — presumably $m_0$; "$\text{Beta}_{\gamma_p}$" denotes the Beta density evaluated at $\gamma_p$)*

$$0 < \delta_1 <(?)\ \tfrac{1}{2}, \qquad \tfrac{1}{2} < \delta_2 < 1$$

*(the first constraint is squeezed between the display and the next line and is only partly legible; the upper bound $\tfrac12$ on $\delta_1$ is a best-effort reading, while "$\tfrac12<\delta_2<1$" is clear)*

> ⚠ Check could not run (unsafe): under $0<\delta_1<\tfrac12$ and $\tfrac12<\delta_2<1$, both Beta shape parameters are positive for all $p\ge 1$. — disallowed call

and we will need $m_0 \ge 3$ for sampling, so reject if $m_0 \le 2$, see above.

This completes sampling from the joint posterior density,

$$\pi\!\left(z,\ \gamma,\ \mu,\ \sigma^2,\ \rho,\ m_0,\ \delta_1,\ \delta_2 \;\middle|\; y\right).$$

Additional posterior inference can be done in the usual way after monitoring the Gibbs sampler for convergence.

### PDF page 158 (booklet page 153)

**14.2 Two more formulations of the Dirichlet Process**

We have discussed extensively the Polya Urn Scheme (Chinese Restaurant Process). There are two more formulations. The three are equivalent.

(1) Mixture
Ishwaran and Zarepoin(2002) [sic: Zarepour]

$$G^L(x) = \sum_{j=1}^{L} \omega'_j S_{X_j}(x), \quad \sum_{j=1}^{L} \omega'_j = 1$$

$$X_j \sim G_0$$

$$(\omega_1,\ldots,\omega_L) \sim \mathrm{Dir}\left(\tfrac{\alpha}{L},\ldots \tfrac{\alpha}{L}\right)$$

*(The point mass is written $S_{X_j}$ here, but $\delta_{X_j}$ in equation (1) below.)*

For any integrable function $f(x)$ with respect to $G_0$:

$$\int f(x)\,dG^{(L)}(x) \overset{d}{\to} \int f(x)\,dG(x), \quad \text{as } L \to \infty$$

That is,

$$G^{(L)} \to G, \quad \text{as } L \to \infty$$

(2) Stick breaking
Setheraman(1994) [sic: Sethuraman]

$$G(x) = \sum_{j=1}^{\infty} \omega_j \delta_{X_j}(x), \quad \sum_{j=1}^{\infty} \omega_j = 1 \tag{1}$$

$$\omega_1 = \gamma_1, \quad \omega_2 = \gamma_2(1-\gamma_1), \quad \ldots, \quad \omega_j = \gamma_j \prod_{i=1}^{j-1}(1-\gamma_i) \tag{2}$$

where,

$$\gamma_j \overset{iid}{\sim} \mathrm{Beta}(1,\alpha)$$

$$W \sim \mathrm{GEM}(\alpha)$$

$$\text{(Griffiths, Eagen and McCloskey)} \quad \text{[sic: Engen]}$$

> ✔ Verified: Stick-breaking partial sums telescope to $1-\prod_{i=1}^{J}(1-\gamma_i)$, hence the weights sum to 1.

> ✔ Verified: For $\gamma_j\overset{iid}{\sim}\mathrm{Beta}(1,\alpha)$, $E[\omega_j]=\frac{1}{1+\alpha}(\frac{\alpha}{1+\alpha})^{j-1}$ and these expectations sum to 1.

$W$ is a random probability measure defined by (1) and (2).

**New Algorithm**
(Kalli, Griffin and Walken 2014) [sic: Walker]
Statistics and computing is based on the slice sampler and data augmentation, stick breaking.

**DPM Model**

$$y_{ij}\mid\theta \overset{iid}{\sim} g\left(y_i, \theta_i\right)$$

*(The booklet writes $\theta$ and $y_i$ with under-tildes to indicate vectors.)*

### PDF page 159 (booklet page 154)

$$y_i = (y_{i1}, \ldots, y_{in_i}) \quad i = 1, \ldots, l$$

*(The booklet writes $y_i$ and $\theta_i$ with under-tildes to indicate vectors.)*

$$\theta_i \mid G \overset{iid}{\sim} G$$

$$G \sim DP(\alpha, G_0)$$

$$f_{\nu, \theta_d}(y_d, u, d) = I\left(u < \varepsilon_d\right) \frac{\omega_d}{\xi_d} g\left(y, \theta_d\right)$$

$\xi_1, \xi_2, \ldots$ a decreasing sequence, $\xi_k = (1-p)^k p, \quad k = 1, 2, \ldots$ for $p$ (a tuning constant)

> ✔ Verified: For 0 < p < 1, the sequence xi_k = (1-p)^k * p is strictly decreasing in k, and sum_{k=1}^inf xi_k = 1-p.

Infinite sequence of $\theta_j, \nu_j, \quad j = 1, 2, \ldots$

The joint posterior density is proportional to

$$\pi(\Omega) \prod_{i=1}^{n} \left\{ I\left(u_i < \varepsilon_{d_i}\right) \frac{\omega_{d_i}}{\xi_{d_i}} g\left(y_i, \theta_{d_i}\right) \right\}$$

*(the indicator is printed with $\varepsilon_{d_i}$ here and in the display above, while steps 3 and 4 below use $\xi_{d_i}$ and $\xi_k$ — [sic], the booklet is inconsistent)*

where, $\pi(\Omega)$ is the joint distribution.

**Gibbs Sampler**

1.
$$\pi\left(\theta_j \middle| \cdot\right) \propto \pi\left(\theta_j\right) \prod_{d_i = j} \left(y_i, \theta_j\right)$$

*(sic: the factor in the product is printed as $\left(y_i, \theta_j\right)$ with the "$g$" apparently omitted)*

2.
$$\gamma_j \middle| . \; \sim \; \text{Beta}\left(a_j, b_j\right), \quad a_j = 1 + \sum_{i=1}^{n} I\left(d_i = j\right) \quad b_j = \alpha + \sum_{i=1}^{n} I\left(d_i > j\right)$$

3.
$$\pi\left(u_i \middle| \cdot\right) \propto I\left(0 < u_i < \xi_{d_i}\right)$$

4.
$$P\left(d_i = k \middle| \cdot\right) \propto I\left(k : \xi_k > u_i\right) \frac{\omega_k}{\xi_k} g\left(y_i, \theta_k\right)$$

where $N = \max N_i, \quad i = 1, \ldots, n, \quad N_i$ is the least value of $t$ s.t. $\xi_t > u_i, \quad i = 1, \ldots, l$

5. All other parameters of $\Omega$

**My Current Interest**

Teh, Jordan, Beal, Blei. (2006)

Dunson (2009) (Local Partition Processes)

Jiani Yin (2016), Arjun Jo (2016), Two PhD Dissertations.

-Hierarchical Dirichlet Process.

-Multiple Dirichlet Process

-Constraint Dirichlet Process

-Machine Learning (clustering)

-Bayesian Uncertainty Analysis

### PDF page 160 (booklet page 155)

-Nonprobability Samples (MRP)

Remark:
The Gibbs Sampler has been making great breakthroughs in science, and engineering possibles [sic]. However, it is simply a 'numerical' integration technique via Monte Carlo methods. The Dirichlet Process is an enormously important piece of statistics of tremendous current interest. It is a pleasure to bring them to you!

### PDF page 161 (unnumbered insert)

*[This page is a fully handwritten lecture insert, in blue pen on ruled paper, with one red-ink correction. It carries no printed booklet page number.]*

**Stick-breaking Process**  |  MA 556 Spring 2024  |  April 19, 2024
*[all three parts of this heading line are hand-underlined]*

The idea to cluster the data and to add robustness against distributional assumptions (e.g., normality) by using mixtures.

The model,

$$y_1,\ldots,y_n \mid \mu,\sigma^2 \overset{iid}{\sim} N(\mu,\sigma^2)$$
$$\pi(\mu,\sigma^2) \propto \frac{1}{\sigma^2}$$

can be made more flexible and robust as follows

$$y_i \mid \rho,\mu,\sigma^2 \overset{ind}{\sim} \sum_{\ell=1}^{m_0} p_\ell\, N\!\left(\mu + z_\ell,\ \sigma^2\right), \qquad i=1,\ldots,n$$
$$\ell = 1,\ldots,m_0 \le n$$
$$z_\ell \mid \sigma^2,\rho \sim N\!\left(0,\ \sigma^2\,\frac{\rho}{1-\rho}\right) \qquad (m_0 \text{ unknown})$$
$$0 < \rho < 1$$

*(The booklet writes $z$ and $y$ with under-tildes to indicate vectors.)*

**Stick-breaking:** *[the word "Stick-breaking" is hand-underlined]*

$$p_1 = v_1,\quad p_2 = v_2(1-v_1),\quad \ldots,\quad p_m = \prod_{\ell=1}^{m-1}(1-v_\ell)$$

> ✔ Verified: The stick-breaking weights $p_1=v_1$, $p_\ell=v_\ell\prod_{j=1}^{\ell-1}(1-v_j)$ for $\ell<m$, and $p_m=\prod_{\ell=1}^{m-1}(1-v_\ell)$ sum to one.

*[margin note, boxed, with a bracket pointing at this display: "Two-parameter Pitman–Yor process. We can write $y \sim PY(a,b)$"]*

$$v_\ell \sim \text{Beta}\!\left(1-\delta_1,\ \frac{\delta_2}{1-\delta_2}(?) + (\ell-1)\delta_1\right), \qquad \ell = 1,\ldots,m_0$$
$$0 < \delta_1 < \tfrac{1}{2},\qquad \tfrac{1}{2} < \delta_2 < 1 \qquad \text{(computational stability)}$$

$$\pi\!\left(\mu,\sigma^2,\rho,\delta_1,\delta_2\right) \propto \frac{1}{\sigma^2}$$

Assuming that all pertinent parameters are stated wfg (?) *[reading uncertain — possibly "wlg", i.e. without loss of generality]*, we can write

$(d_i = \ell)$,

$$f\!\left(y, d \mid \rho, \mu, \sigma^2, z, \text{etc.}\right) \;=\; \prod_{\ell=1}^{m} \Big\{\, p_\ell\, N\!\left(\mu + z_\ell,\ \sigma^2\right) \Big\}^{\,I(d_i=\ell)}, \qquad \begin{array}{l}\ell = 1,\ldots,m\\ i = 1,\ldots,n\end{array}$$

We can now sample $d_i$, $i=1,\ldots,n$; $d_i$ tells us which cluster unit $i$ falls in ($d_i$ are latent variables) *(correction: "latent" is inserted in red ink, the red stroke cancelling the blue letter it replaces)*

Therefore,

$$P\!\left(d_i = \ell \mid y, z, \mu, \sigma^2, \text{etc.}\right) \;=\; \frac{p_\ell\, N\!\left(\mu + z_\ell,\ \sigma^2\right)}{\sum_{\ell=1}^{m} p_\ell\, N\!\left(\mu + z_\ell,\ \sigma^2\right)}, \qquad \begin{array}{l}\ell = 1,\ldots,m\\ i = 1,\ldots,n\end{array}$$

> ✔ Verified: With joint $f(y_i, d_i=\ell) = p_\ell\, N(y_i\mid \mu+z_\ell, \sigma^2)$, Bayes' rule gives $P(d_i=\ell\mid y_i,\cdot) = p_\ell N(\mu+z_\ell,\sigma^2) / \sum_{k=1}^{m} p_k N(\mu+z_k,\sigma^2)$, and these probabilities sum to one.

$\Big[$ Remark: At this point we have $m_0 \le n$; we may need to sample additional $z_\ell$, $v_\ell$; $\ell = m_0+1,\ldots,m$ from their priors. $\Big]$

### PDF page 162 (unnumbered insert)

*(The whole page is a handwritten lecture insert on ruled paper — no typeset text and no printed page number. It develops the partition matrix used for clustering. Red ink appears only in the two labels $d_1$, $d_2$.)*

We have the following partition matrix

*[Handwritten matrix. Columns are headed "clusters" $1,2,3,4,\;⑤,\;\cdots,\;ⓜ$ — the 5th and the $m$-th headers are circled by hand. Two red annotations attach to the circled headers.]*

$$
\begin{array}{c|cccccccc}
 & 1 & 2 & 3 & 4 & ⑤ & \cdots & \; & ⓜ \\\hline
1 & 0 & 0 & 0 & 0 & 1 & \cdot & - & 0 \\
2 & 0 & \cdot & - & \cdot & \cdot & \cdot & 0 & 1 \\
3 & & & & & & & & \\
\vdots & & & & & & & & \\
m & & & & & & & &
\end{array}
$$

*[margin/row-group label at left: "unit", bracketing the row labels $1,2,3,\ldots,m$; column-group label above: "clusters"]*

*(red annotation: the circled column header ⑤ is labelled "$= d_1$", and the circled column header ⓜ is labelled "$= d_2$" — i.e. unit 1 has its 1 in the cluster-$d_1$ column and unit 2 in the cluster-$d_2$ column.)*

etc. This is a $m \times m$ matrix but many columns have 0 column sum. These must be eliminated. Suppose there are $m_0$ nonzero columns. Then the partition matrix, $P$, is a $m \times m_0$ matrix. Here is a simple example with 5 units

*[Handwritten $5\times 5$ matrix with a hand-drawn brace labelled "units" at the left and "clusters" written above the column headers. A hand-drawn rule separates the body from the column-sum row. Circled ①, ②, ③ are written above the column-sum entries of columns 2, 4 and 5 respectively, renumbering the surviving clusters.]*

$$
\begin{array}{c|ccccc}
 & 1 & 2^{\;①} & 3 & 4^{\;②} & 5^{\;③} \\\hline
1 & 0 & 1 & 0 & 0 & 0 \\
2 & 0 & 1 & 0 & 0 & 0 \\
3 & 0 & 0 & 0 & 1 & 0 \\
4 & 0 & 0 & 0 & 1 & 0 \\
5 & 0 & 0 & 0 & 0 & 1 \\\hline
 & 0 & 2 & 0 & 2 & 1
\end{array}
$$

> ✔ Verified: The 5×5 example partition matrix has column sums (0,2,0,2,1), so exactly m₀ = 3 columns are nonzero.

cluster 1: $(1,2)$

$\quad$ 2: $(3,4)$

$\quad$ 3: $(5)$

$m_0 = 3$

Now there are 3 clusters 1, 2, 3.

$$
\mathbb{P} \;=\;
\begin{array}{c|ccc}
 & 1 & 2 & ③ \\\hline
1 & 1 & 0 & 0 \\
2 & 1 & 0 & 0 \\
3 & 0 & 1 & 0 \\
4 & 0 & 1 & 0 \\
5 & 0 & 0 & 1
\end{array}
\qquad (5 \times 3)
$$

> ✔ Verified: Eliminating the zero-sum columns turns the m×m matrix into the stated m×m₀ = 5×3 partition matrix P.

### PDF page 163 (booklet page 152)

$$i \in I_{i^*}, \quad i = 1,\ldots,l, \quad i^* = 1,\ldots,k$$

$$\pi\left(\theta, \sigma^2, \delta^2\right)$$

**Beta-binomial**

$$P\left(y_{ij} \mid p_i\right) = p_i^{s_i}\left(1-p_i\right)^{n_i-s_i}$$

$$P\left(y_{ij} \mid p_j\right) = p_j^{s_i}\left(1-p_j\right)^{n_i-s_i} \quad \text{[sic: the exponents keep the subscript } i \text{ while the probability is } p_j\text{]}$$

*(The booklet writes $y_{ij}$ with an under-tilde to indicate a vector.)*

$$i = 1,\ldots,l, \quad s_i = \sum_{j=1}^{n_i} y_{ij}$$

$$P\left(y_{ij} \mid \mu, \tau\right) = \int_0^1 p_i^{s_i}\left(1-p_i\right)^{n_i-s_i}\,\frac{p_i^{\mu\tau-1}\left(1-p_i\right)^{(1-\mu)\tau-1}}{B(\mu\tau,(1-\mu)\tau)}\,dp_i$$

$$= \frac{B\left(s_i + \mu\tau,\; n_i - s_i + (1-\mu)\tau\right)}{B(\mu\tau,(1-\mu)\tau)}$$

> ⚠ Check FAILED: The beta-binomial marginal integral equals $B(s+\mu\tau,\, n-s+(1-\mu)\tau)/B(\mu\tau,(1-\mu)\tau)$. — the stated result did not reproduce (see verification log)

$$Q_j = \frac{p_j^{s_i}\left(1-p_j\right)^{n_i-s_i}}{\dfrac{B\left(s_i + \mu\tau,\; n_i - s_i + (1-\mu)\tau\right)}{B(\mu\tau,(1-\mu)\tau)} + \displaystyle\sum_{\substack{j=1 \\ j \neq i}}^{l} p_j^{s_i}\left(1-p_j\right)^{n_i-s_i}}$$

$$\pi(\alpha \mid k, l) \propto \pi(\alpha) \cdot \frac{\alpha^k \tau(\alpha)}{\tau(\alpha + l)} \quad \text{[sic: } \tau \text{ here denotes the gamma function } \Gamma\text{, clashing with the } \tau \text{ used above]}$$

**How to get $\mu, \tau$? Go to parametric model**

Have $p_i^*, \quad i = 1,\ldots,k$

$$y_{ij} \mid p_i^* \sim \text{Ber}\left(p_i^*\right)$$

$$p_i^* \mid \mu, \tau \sim \text{Beta}(\mu\tau, (1-\mu)\tau)$$

$$i \in I_{i^*}, \quad i = 1,\ldots,l, \quad i^* = 1,\ldots,k$$

$$\pi(\mu, \tau) = \frac{1}{(1+\tau)^2} \quad 0 < \mu < 1, \quad \tau > 0$$

> ✔ Verified: $\pi(\mu,\tau)=(1+\tau)^{-2}$ integrates to exactly 1 over $0<\mu<1,\ \tau>0$.

Now,

$$\pi\left(\mu, \tau \mid p^*\right) \propto \left[\prod_{i=1}^{k} \frac{p_i^{*\,\mu\tau-1}\left(1-p_i^*\right)^{(1-\mu)\tau-1}}{\mathrm{B}(\mu\tau,(1-\mu)\tau)}\right]$$

$$\propto \frac{1}{(1+\tau)^2}, \quad 0 < \mu < 1, \tau > 0$$

*(The two displayed lines are written as a single chain of $\propto$ relations; the second line reproduces the prior factor rather than the product of the two, so the intended statement is that the posterior is proportional to the bracketed likelihood times $(1+\tau)^{-2}$.)*

### PDF page 164 (booklet page 156)

*(Blank page — running header only.)*

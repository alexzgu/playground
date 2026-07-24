# Chapter 2 — Brownian motion
*(PDF pages 41–88; book pages 35–82)*

### PDF page 41 (book page 35)
# Chapter 2

# Brownian motion

**2.1 Limits of sums of independent variables**

We will discuss two major results about sums of random variables that we hope the reader has seen. They both discuss the limit distribution of

$$ X_1 + X_2 + \cdots + X_n $$

where $X_1, X_2, \ldots, X_n$ are independent, identically distributed random variables.

Suppose $X_1, X_2, \ldots$ have mean $\mu$ and variance $\sigma^2 < \infty$. Let

$$ Z_n = \frac{(X_1 + \cdots + X_n) - n\mu}{\sigma \sqrt{n}}. $$

We let $\Phi$ denote the standard normal distribution function,

$$ \Phi(b) = \int_{-\infty}^{b} \frac{1}{\sqrt{2\pi}} \, e^{-x^2/2} \, dx. $$

While this function cannot be written down explicitly, the numerical values are easily accessible in tables and computer software packages.

**Theorem 2.1.1** (Central Limit Theorem)**.** *As $n \to \infty$, the distribution of $Z_n$ approaches a standard normal distribution. More precisely, if $a < b$, then*

$$ \lim_{n \to \infty} \mathbb{P}\{a \leq Z_n \leq b\} = \Phi(b) - \Phi(a). $$

### PDF page 42 (book page 36)
This amazing theorem states that no matter what distribution we choose for the $X_j$, then as long as the distribution has a finite variance, the scaled random variables approach a normal distribution. This is what is referred to in physics literature as a *universality* result and in the mathematics literature as an *invariance principle*. The assumption that the random variables are identically distributed can be relaxed somewhat. We will not go into details here, but whenever a quantity can be written as a sum of independent (or at least not too dependent) increments, *all of which are small compared to the sum*, then the limiting distribution is normal. This is why it is often reasonable to assume normal distributions in nature.

---

To see a complete proof of Theorem 2.1.1, consult any book on measure-theoretic probability. We will sketch part of the proof which shows how the normal distribution arises. Without loss of generality, we can assume that $\mu = 0, \sigma^2 = 1$ for otherwise we consider $Y_j = (X_j - \mu)/\sigma$. Let $\phi(t) = \mathbb{E}[e^{itX_j}]$ denote the characteristic function of the increments. Then, $\phi$ can be expanded near the origin,

$$ \begin{aligned} \phi(t) &= 1 + i\,\mathbb{E}\left[X_j\right] t + \frac{(i)^2}{2}\,\mathbb{E}\left[X_j^2\right] t^2 + o(t^2) \\ &= 1 - \frac{t^2}{2} + o(t^2), \end{aligned} $$

where $o(t^2)$ denotes a function such that $|o(t^2)|/t^2 \to 0$ as $t \to 0$. Using the independence of the $X_j$, we see that the characteristic function of $Z_n$ is

$$ \phi_{Z_n}(t) = \phi(t/\sqrt{n})^n = \left[1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right)\right]^n \longrightarrow e^{-t^2/2}. $$

The right-hand side is the characteristic function of a standard normal random variable.

---

When one considers sums of independent random variables where a few terms contribute the bulk of the sum, then one does not expect to get normal limits. The prototypical example of a nonnormal limit is the Poisson distribution. Suppose $\lambda > 0$ and $X_1^{(n)}, X_2^{(n)}, \ldots, X_n^{(n)}$ are independent random variables each with

$$ \mathbb{P}\left\{X_j^{(n)} = 1\right\} = 1 - \mathbb{P}\left\{X_j^{(n)} = 0\right\} = \frac{\lambda}{n}. $$

### PDF page 43 (book page 37)

Let
$$ Y_n = X_1^{(n)} + \cdots + X_n^{(n)}, $$
and note that for each $n$, $\mathbb{E}[Y_n] = \lambda$. Recall that a random variable $Y$ has a *Poisson distribution with mean $\lambda$* if for each nonnegative integer $k$,

$$ \mathbb{P}\{Y = k\} = e^{-\lambda}\, \frac{\lambda^k}{k!}. $$

**Theorem 2.1.2** (Convergence to the Poisson distribution). *As $n \to \infty$, the distribution of $Y_n$ approaches a Poisson distribution with mean $\lambda$. More precisely, for every nonnegative integer $k$,*

$$ \lim_{n\to\infty} \mathbb{P}\{Y_n = k\} = e^{-\lambda}\, \frac{\lambda^k}{k!}. $$

*Proof.* For each $n$, $Y_n$ has a binomial distribution with parameters $n$ and $\lambda/n$, and hence

$$
\begin{aligned}
&\lim_{n\to\infty} \mathbb{P}\{Y_n = k\} \\
&= \lim_{n\to\infty} \binom{n}{k} \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n-k} \\
&= \frac{\lambda^k}{k!} \lim_{n\to\infty} \frac{n(n-1)\cdots(n-k+1)}{n^k} \left(1 - \frac{\lambda}{n}\right)^{-k} \left(1 - \frac{\lambda}{n}\right)^{n}
\end{aligned}
$$

Since we are fixing $k$ and letting $n \to \infty$, one can see that

$$ \lim_{n\to\infty} \frac{n(n-1)\cdots(n-k+1)}{n^k} \left(1 - \frac{\lambda}{n}\right)^{-k} = 1, $$

and in calculus one learns the limit

$$ \lim_{n\to\infty} \left(1 - \frac{\lambda}{n}\right)^{n} = e^{-\lambda}. $$

$\square$

We will be taking limits of processes as the time increment goes to zero. The kind of limit we expect will depend on the assumptions. When we take limits of random walks with finite variance, then we are in the regime of the

### PDF page 44 (book page 38)

central limit theorem, and we will expect normal distributions. Also, because all of the increments are small with respect to the sum, the limit process will have paths that are continuous. Here the limit is *Brownian motion* which we discuss in this section.

In the Poisson case, the limit distribution will not have continuous paths but rather will be a *jump process*. The prototypical case is the Poisson process with intensity $\lambda$. In this case, $N_t$ denotes the number of occurrences of an event by time $t$. The function $t \mapsto N_t$ takes on nonnegative integer values and the jumps are always of size $+1$. It satisfies the following conditions.

- For each $s < t$, the random variable $N_t - N_s$ has a Poisson distribution with parameter $\lambda(t - s)$.

- For each $s < t$, the random variable $N_t - N_s$ is independent of the random variables $\{N_r : 0 \le r \le s\}$.

We discuss this further in Section 6.2.

## 2.2 Multivariate normal distribution

Although the normal or Gaussian distribution is a little inconvenient in the sense that the distribution function cannot be computed exactly, there are many other aspects that make the distribution very convenient. In particular, when dealing with many variables, assuming a *joint or multivariate* normal distribution makes computations tractable. In this section we will give the basic definitions. Roughly speaking, the basic assumption is that if $(X_1, \ldots, X_n, Y)$ have a joint normal distribution then not only does each variable have a normal distribution but also, the conditional distribution of $Y$ given $X_1, \ldots, X_n$ is normal with mean $\mathbb{E}[Y \mid X_1, \ldots, X_n]$ and a variance that depends on the joint distribution but not on the observed data points. There are a number of equivalent ways to define a joint normal distribution. We will use the following.

**Definition** A finite sequence of random variables $(X_1, \ldots, X_n)$ has a *joint (or multivariate) normal (or Gaussian)* distribution if they are linear combinations of independent standard normal random variables. In other words, if there exist independent random variables $(Z_1, \ldots, Z_m)$, each $N(0, 1)$, and constants $m_j, a_{jk}$ such that for $j = 1, \ldots, n$,

$$ X_j = m_j + a_{j1} Z_1 + a_{j2} Z_2 + \cdots + a_{jm} Z_m. $$

### PDF page 45 (book page 39)

Clearly $\mathbb{E}[X_j] = m_j$. Let us consider the case of mean-zero (also called *centered*) joint normals, in which case the equation above can be written in matrix form
$$ \mathbf{X} = A\,\mathbf{Z}, $$
where

$$ \mathbf{X} = \begin{pmatrix} X_1 \\ X_2 \\ \vdots \\ X_n \end{pmatrix}, \quad \mathbf{Z} = \begin{pmatrix} Z_1 \\ Z_2 \\ \vdots \\ Z_m \end{pmatrix}, $$

and $A$ is the $n \times m$ matrix with entries $a_{jk}$. Each $X_j$ is a normal random variable with mean zero and variance

$$ \mathbb{E}[X_j^2] = a_{j1}^2 + \cdots + a_{jm}^2. $$

More generally, the covariance of $X_j$ and $X_k$ is given by

$$ \mathrm{Cov}(X_j, X_k) = \mathbb{E}[X_j X_k] = \sum_{l=1}^{m} a_{jl} a_{kl}. $$

Let $\Gamma = AA^T$ be the $n \times n$ matrix whose entries are

$$ \Gamma_{jk} = \mathbb{E}[X_j X_k]. $$

Then $\Gamma$ is called the *covariance matrix*.

We list some important properties. Assume $(X_1, \ldots, X_n)$ has a joint normal distribution with mean zero and covariance matrix $\Gamma$.

- Each $X_j$ has a normal distribution. In fact, if $b_1, \ldots, b_n$ are constants, then
$$ b_1 X_1 + \cdots + b_n X_n, $$
has a normal distribution. We can see this easily since we can write the sum above as a linear combination of the independent normals $Z_1, \ldots, Z_m$.

- The matrix $\Gamma$ is symmetric, $\Gamma_{jk} = \Gamma_{kj}$. Moreover, it is *positive semidefinite* which means that if $\mathbf{b} = (b_1, \ldots, b_n)$ is a vector in $\mathbb{R}^n$, then
$$ \mathbf{b} \cdot \Gamma \mathbf{b} = \sum_{j=1}^{n} \sum_{k=1}^{n} \Gamma_{jk} b_j b_k \ge 0. \tag{2.1} $$

### PDF page 46 (book page 40)

(If the $\geq$ is replaced with $> 0$ for all $\mathbf{b} = (b_1, \ldots, b_n) \neq (0, \ldots, 0)$, then the matrix is called *positive definite.*) The inequality (2.1) can be derived by noting that the left-hand side is the same as

$$ \mathbb{E}\left[(b_1 X_1 + \cdots + b_n X_n)^2\right], $$

which is clearly nonnegative.

- If $\Gamma$ is a positive semidefinite, symmetric matrix, then it is the covariance matrix for a joint normal distribution. The proof of this fact, which we omit, uses linear algebra to deduce that there exists an $n \times n$ matrix $A$ with $AA^T = \Gamma$. (The $A$ is not unique.)

- The distribution of a mean-zero joint normal is determined by the covariance matrix $\Gamma$.

In order to show that the covariance matrix $\Gamma$ determines the distribution of a mean-zero joint normal, we compute the characteristic function. Suppose that $\Gamma = AA^T$ where $A$ is $n \times n$. Using the independence of $Z_1, \ldots, Z_n$ and the characteristic function of the standard normal, $\mathbb{E}[e^{itZ_k}] = e^{-t^2/2}$, we see that the characteristic function of

### PDF page 47 (book page 41)

$(X_1, \ldots, X_n)$ is

$$
\begin{aligned}
\phi(\theta_1, \ldots, \theta_n) &= \mathbb{E}\left[\exp\left\{i(\theta_1 X_1 + \ldots + \theta_n X_n)\right\}\right] \\
&= \mathbb{E}\left[\exp\left\{i \sum_{j=1}^{n} \theta_j \sum_{k=1}^{n} a_{jk} Z_k\right\}\right] \\
&= \mathbb{E}\left[\exp\left\{i \sum_{k=1}^{n} Z_k\Big(\sum_{j=1}^{n} \theta_j a_{jk}\Big)\right\}\right] \\
&= \prod_{k=1}^{n} \mathbb{E}\left[\exp\left\{i Z_k\Big(\sum_{j=1}^{n} \theta_j a_{jk}\Big)\right\}\right] \\
&= \exp\left\{-\frac{1}{2} \sum_{k=1}^{n} \Big(\sum_{j=1}^{n} \theta_j a_{jk}\Big)^2\right\} \\
&= \exp\left\{-\frac{1}{2} \sum_{k=1}^{n} \sum_{j=1}^{n} \sum_{l=1}^{n} \theta_j \theta_i a_{jk} a_{lk}\right\} \\
&= \exp\left\{-\frac{1}{2} \theta A A^T \theta^T\right\} \\
&= \exp\left\{-\frac{1}{2} \theta \Gamma \theta^T\right\}
\end{aligned}
$$

where we write $\theta = (\theta_1, \ldots, \theta_n)$. Even though we used $A$, which is not unique, in our computation, the answer only involves $\Gamma$. Since the characteristic function determines the distribution, the distribution depends only on the covariance matrix.

- If $\Gamma$ is invertible, then $(X_1, \ldots, X_n)$ has a density. We write it in the case that the random variables have mean $\mathbf{m} = (m_1, \ldots, m_n)$,

$$ f(x_1, \ldots, x_n) = f(\mathbf{x}) = $$

$$ \frac{1}{(2\pi)^{n/2} \sqrt{\det \Gamma}} \, \exp\left\{-\frac{(\mathbf{x} - \mathbf{m}) \cdot \Gamma^{-1}(\mathbf{x} - \mathbf{m})^T}{2}\right\}. $$

Sometimes this density is used as a definition of a joint normal. The formula for the density looks messy, but note that if $n = 1$, $\mathbf{m} = m$, $\Gamma = [\sigma^2]$, then the right-hand side is the density of a $N(m, \sigma^2)$ random variable.

### PDF page 48 (book page 42)

- If $(X_1, X_2)$ have a mean-zero joint normal density, and $\mathbb{E}(X_1 X_2) = 0$, then $X_1, X_2$ are independent random variables. To see this let $\sigma_j^2 = \mathbb{E}[X_j^2]$. Then the covariance matrix of $(X_1, X_2)$ is the diagonal matrix with diagonal entries $\sigma_j^2$. If $(Z_1, Z_2)$ are independent $N(0, 1)$ random variables and $Y_1 = \sigma_1 Z_1, Y_2 = \sigma_2 Z_2$, then by our definition $(Y_1, Y_2)$ are joint normal with the same covariance matrix. Since the covariance matrix determines the distribution, $X_1, X_2$ must be independent,

It is a special property about joint normal random variables that orthogonality implies independence. In our construction of Brownian motion, we will use a particular case, that we state as a lemma.

**Proposition 2.2.1.** *Suppose $X, Y$ are independent $N(0, 1)$ random variables and*

$$ Z = \frac{X + Y}{\sqrt{2}}, \qquad W = \frac{X - Y}{\sqrt{2}}. $$

*Then $Z$ and $W$ are independent $N(0, 1)$ random variables.*

*Proof.* By definition $(Z, W)$ has a joint normal distribution and $Z, W$ clearly have mean 0. Using $\mathbb{E}[X^2] = \mathbb{E}[Y^2] = 1$ and $\mathbb{E}[XY] = 0$, we get

$$ \mathbb{E}[Z^2] = 1, \quad \mathbb{E}[W^2] = 1, \quad \mathbb{E}[ZW] = 0. $$

Hence the covariance matrix for $(Z, W)$ is the identity matrix and this is the covariance matrix for independent $N(0, 1)$ random variables. $\square$

## 2.3 Limits of random walks

Brownian motion can be viewed as the limit of random walk as the time and space increments tend to zero. It is necessary to be careful about how the limit is taken. Suppose $X_1, X_2, \ldots$ are independent random variables with $\mathbb{P}\{X_j = 1\} = \mathbb{P}\{X_j = -1\} = 1/2$ and let

$$ S_n = X_1 + \cdots + X_n $$

be the corresponding random walk. Here we have chosen time increment $\Delta t = 1$ and space increment $\Delta x = 1$. Suppose we choose $\Delta t = 1/N$ where $N$ is a large integer. Hence, we view the process at times

$$ \Delta t, 2\Delta t, 3\Delta t, \cdots, $$

### PDF page 49 (book page 43)

and at each time we have a jump of $\pm\Delta x$. At time $1 = N\Delta t$, the value of the process is

$$ W_1^{(N)} = \Delta x\,(X_1 + \cdots + X_N). $$

We would like to choose $\Delta x$ so that $\mathrm{Var}[W_1^{(N)}] = 1$, and since

$$ \begin{aligned} \mathrm{Var}\left[\Delta x\,(X_1 + \cdots + X_N)\right] &= (\Delta x)^2\left[\mathrm{Var}(X_1) + \cdots + \mathrm{Var}(X_N)\right] \\ &= (\Delta x)^2\,N, \end{aligned} $$

we see that we need to choose

$$ \Delta x = \sqrt{1/N} = \sqrt{\Delta t}. $$

We also know from the central limit theorem, that if $N$ is large, then the distribution of

$$ \frac{X_1 + \cdots + X_N}{\sqrt{N}}, $$

is approximately $N(0,1)$.

Brownian motion could be defined formally as the limit of random walks, but there are subtleties in describing the kind of limit. In the next section, we define it directly using the idea of "continuous random motion". However, the random walk intuition is useful to retain.

## 2.4 Brownian motion

*Brownian motion* or the *Wiener process* is a model of random continuous motion. We will start by making the assumptions that underlie the phrase "random continuous motion". Let $B_t = B(t)$ be the value at time $t$. For each $t$, $B_t$ is a random variable.[^1] A collection of random variables indexed by time is called a *stochastic process*. We can view the process in two different ways:

- For each $t$, there is a random variable $B_t$, and there are correlations between the values at different times.

[^1]: In this book and usually in the financial world, the terms Brownian motion and Wiener process are synonymous. However, in the scientific world, the word Brownian motion is often used for a physical process for which what we will describe is one possible mathematical model. The term Wiener process always refers to the model we define. The letter $W_t$ is another standard notation for Brownian motion/Wiener process and is more commonly used in financial literature. We will use both $B_t$ and $W_t$ later in the book when we need two notations.

### PDF page 50 (book page 44)

- The function $t \mapsto B(t)$ is a random function. In other words, it is a random variable whose value is a function.

There are three major assumptions about the random variables $B_t$.

- **Stationary increments**. If $s < t$, then the distribution of $B_t - B_s$ is the same as that of $B_{t-s} - B_0$.

- **Independent increments**. If $s < t$, the random variable $B_t - B_s$ is independent of the values $B_r$ for $r \le s$.

- **Continuous paths**. The function $t \mapsto B_t$ is a continuous function of $t$.

We often assume $B_0 = 0$ for convenience, but we can also take other initial conditions. All of the assumptions above are very reasonable for a model of random continuous motion. However, it is not obvious that these are enough assumptions to characterize our process uniquely. It turns out that they do up to two parameters. One can prove (see Theorem 6.8.4), that if $B_t$ is a process satisfying the three conditions above, then the distribution of $B_t$ for each $t$ must be normal. Suppose $B_t$ is such a process, and let $m, \sigma^2$ be the mean and variance of $B_1$. If $s < t$, then independent, identically distributed increments imply that

$$ \mathbb{E}[B_t] = \mathbb{E}[B_s] + \mathbb{E}[B_t - B_s] = \mathbb{E}[B_s] + \mathbb{E}[B_{t-s}], $$

$$ \mathrm{Var}[B_t] = \mathrm{Var}[B_s] + \mathrm{Var}[B_t - B_s] = \mathrm{Var}[B_s] + \mathrm{Var}[B_{t-s}]. $$

Using this relation, we can see that $\mathbb{E}[B_t] = tm$, $\mathrm{Var}[B_t] = t\sigma^2$. At this point, we have only shown that *if* a process exists, then the increments must have a normal distribution. We will show that such a process exists. It will be convenient to put the normal distribution in the definition.

**Definition** A stochastic process $B_t$ is called a *(one-dimensional) Brownian motion* with *drift $m$* and *variance (parameter) $\sigma^2$* starting at the origin if it satisfies the following.

- $B_0 = 0$.

- For $s < t$, the distribution of $B_t - B_s$ is normal with mean $m(t - s)$ and variance $\sigma^2(t - s)$.

### PDF page 51 (book page 45)

- If $s < t$, the random variable $B_t - B_s$ is independent of the values $B_r$ for $r \le s$.

- With probability one, the function $t \mapsto B_t$ is a continuous function of $t$.

If $m = 0, \sigma^2 = 1$, then $B_t$ is called a *standard Brownian motion*.

Recall that if $Z$ has a $N(0,1)$ distribution and $Y = \sigma Z + m$, then $Y$ has a $N(m, \sigma^2)$ distribution. Given that it is easy to show the following.

- If $B_t$ is a standard Brownian motion and

$$ Y_t = \sigma\,B_t + mt, $$

then $Y_t$ is a Brownian motion with drift $m$ and variance $\sigma^2$.

Indeed, one just checks that it satisfies the conditions above. Hence, in order to establish the *existence* of Brownian motion, it suffices to construct a standard Brownian motion.

There is a mathematical challenge in studying stochastic processes indexed by continuous time. The problem is that the set of positive real numbers is *uncountable*, that is, the elements cannot be enumerated $t_1, t_2, \ldots$. The major axiom of probability theory is the fact that if $A_1, A_2, \ldots$ is a *countable* sequence of disjoint events, then

$$ \mathbb{P}\left[\bigcup_{n=1}^{\infty} A_n\right] = \sum_{n=1}^{\infty} \mathbb{P}[A_n]. $$

This rule does not hold for uncountable unions. An example that we have all had to deal with arises with continuous random variables. Suppose, for instance, that $Z$ has a $N(0,1)$ distribution. Then for each $x \in \mathbb{R}$,

$$ \mathbb{P}\{Z = x\} = 0. $$

However,

$$ 1 = \mathbb{P}\{Z \in \mathbb{R}\} = \mathbb{P}\left[\bigcup_{x \in \mathbb{R}} A_x\right], $$

### PDF page 52 (book page 46)

where $A_x$ denotes the event $\{Z = x\}$. The events $A_x$ are disjoint, each with probability zero, but it is not the case that

$$ \mathbb{P}\left[\bigcup_{x\in\mathbb{R}} A_x\right] = \sum_{x\in\mathbb{R}} \mathbb{P}(A_x) = 0. $$

In constructing Brownian motion, we use the fact that if $g : [0,\infty) \to \mathbb{R}$ is a *continuous* function and we know the value of $g$ on a countable, dense set, such as the *dyadic rationals*

$$ \left\{\frac{k}{2^n} : k = 0, 1, \ldots; n = 0, 1, \ldots\right\}, $$

then we know the value at every $t$. Indeed, we need only find a sequence of dyadic rationals $t_n$ that converge to $t$, and let

$$ g(t) = \lim_{t_n\to t} g(t_n). $$

This is fine if *a priori* we know the function $g$ is continuous. Our strategy for constructing Brownian motion will be:

- First define the process $B_t$ when $t$ is a dyadic rational.

- Prove that with probability one, the function $t \mapsto B_t$ is continuous on the dyadics (this is the hardest step, and we need some care in the definition of continuity).

- Extend $B_t$ to other $t$ by continuity.

The next section shows that one can construct a Brownian motion. The reader can skip this section and just have faith that such a process exists.

## 2.5   Construction of Brownian motion

We will show how to construct Brownian motion. For ease, we will consider $B_t, 0 \le t \le 1$. Once we know how to construct this, we can take a countable collection of such processes and connect them appropriately to get $B_t, 0 \le t < \infty$. We start with a probability space

### PDF page 53 (book page 47)

$(\Omega, \mathcal{F}, \mathbb{P})$ which is large enough so that it contains a countable collection of independent standard normal random variables. Let

$$ \mathcal{D}_n = \left\{\frac{k}{2^n} : k = 0, 1, \ldots, 2^n\right\}, $$

denote the dyadic rationals in $[0, 1]$ with denominator $2^n$ and let $\mathcal{D} = \cup_n \mathcal{D}$. Since $\mathcal{D}$ is a countable set, we can assume that our collection of $N(0, 1)$ random variables

$$ \{Z_q : q \in \mathcal{D}\} $$

is indexed by $\mathcal{D}$.

We will use the independent random variables $\{Z_q\}$ to define the Brownian motion $B_q, q \in \mathcal{D}$. We start by defining $B_0, B_1$, and then $B_{1/2}$, and then $B_{1/4}$ and $B_{3/4}$, and so forth, by always subdividing our intervals. We start with $B_0 = 0$ and we let $B_1 = Z_1$ which is clearly $N(0, 1)$. We then define

$$ B_{1/2} = \frac{B_1}{2} + \frac{Z_{1/2}}{2}, $$

and hence

$$ B_1 - B_{1/2} = \frac{B_1}{2} - \frac{Z_{1/2}}{2}. $$

We think of the definition of $B_{1/2}$ as being $E[B_{1/2} \mid B_1]$ plus some independent randomness. Using Proposition 2.2.1, we can see that $B_{1/2}$ and $B_1 - B_{1/2}$ are independent random variables, each $N(0, 1/2)$. We continue this splitting. If $q = (2k+1)/2^{n+1} \in \mathcal{D}_{n+1} \setminus \mathcal{D}_n$, we define

$$ B_q = B_{k2^{-n}} + \frac{B_{(k+1)2^{-n}} - B_{k2^{-n}}}{2} + \frac{Z_q}{2^{(n+2)/2}}. $$

This formula looks a little complicated, but we can again view this as

$$ B_q = E[B_q \mid B_{k2^{-n}}, B_{(k+1)2^{-n}}] + \text{(independent randomness)}, $$

where the variance of the new randomness is chosen appropriately. By repeated use of Proposition 2.2.1, we can see that for each $n$, the random variables

$$ \left\{B_{k2^{-n}} - B_{(k-1)2^{-n}} : k = 1, \ldots, 2^n\right\} $$

### PDF page 54 (book page 48)

are independent, each with $N(0, 2^{-n})$ distribution. From this we can see that $\{B_q : q \in \mathcal{D}\}$ satisfies the first three properties in the definition of a Brownian motion.

We will define $B_t$ for other $t$ by continuity. To do this we prove a theorem that states that the Brownian motion restricted to $\mathcal{D}$ has *uniformly continuous* paths. In other words, we show that with probability one, for every $\epsilon > 0$, there exists $\delta > 0$ such that if $|s - t| \le \delta$ and $s, t \in \mathcal{D}$, then $|B_s - B_t| < \epsilon$. Equivalently, if we define the random variable

$$ K_n = \sup\left\{|B_s - B_t| : s, t \in \mathcal{D}, |s - t| \le 2^{-n}\right\}, $$

then with probability one, $K_n \to 0$ as $n \to \infty$. Note that $K_n$ is the supremum of a countable number of random variables and hence is a well-defined random variable (perhaps taking the value $\infty$).

**Proposition 2.5.1.** *With probability one, for all $\alpha < 1/2$,*

$$ \lim_{n\to\infty} 2^{\alpha n} K_n = 0. \tag{2.2} $$

*In particular, $K_n \to 0$.*

In order to prove this proposition, it is easier to consider another sequence of random variables

$$ J_n = \max_{j=1,\ldots,2^n} Y(j, n) $$

where $Y(j, n)$ equals

$$ \sup\left\{|B_q - B_{(j-1)2^{-n}}| : q \in \mathcal{D}, (j-1)2^{-n} \le q \le j2^{-n}\right\}. $$

A simple argument using the triangle inequality shows that $K_n \le 3J_n$. It turns out $J_n$ is easier to analyze. For any $\epsilon > 0$,

$$ \mathbb{P}\{J_n \ge \epsilon\} \le \sum_{j=1}^{2^n} \mathbb{P}\{Y(j, n) \ge \epsilon\} = 2^n\, \mathbb{P}\{Y(1, n) \ge \epsilon\}. $$

Also the distribution of

$$ Y(1, n) = \sup\left\{|B_q| : q \in \mathcal{D}, q \le 2^{-n}\right\}. $$

is the same as that of $2^{-n/2}Y$ where

$$ Y = Y(1, 0) = \sup\left\{|B_q| : q \in \mathcal{D}\right\}. $$

### PDF page 55 (book page 49)

Using this we see that

$$ \mathbb{P}\{J_n \geq C\,\sqrt{n}\,2^{-n/2}\} \leq 2^n\,\mathbb{P}\{Y \geq C\,\sqrt{n}\}. $$

We will show below that if $C > \sqrt{2\log 2}$, then

$$ \sum_{n=1}^{\infty} 2^n\,\mathbb{P}\{Y \geq C\,\sqrt{n}\} < \infty. \tag{2.3} $$

The Borel-Cantelli lemma then implies that with probability one, the event $\{J_n \geq 2^{-n/2}n\}$ happens for only finitely many values of $n$. In particular,

$$ \lim_{n\to\infty} 2^{n/2}\,n^{-1}\,J_n = 0, $$

which implies (2.2). To get our estimate, we will need the following lemma which is a form of the "reflection principle" for Brownian motion.

**Lemma 2.5.2.** *For every $a \geq 4$,*

$$ \mathbb{P}\{Y > a\} \leq 4\,\mathbb{P}\{B_1 \geq a\} \leq e^{-a^2/2}. $$

To prove this lemma, let

$$ Y_n = \max\left\{|B_q| : q \in \mathcal{D}_n\right\}. $$

Then

$$ \mathbb{P}\{Y > a\} = \lim_{n\to\infty} \mathbb{P}\{Y_n > a\}, $$

and hence it suffices to prove the inequality for each $n$. Fix $n$ and let $A_k$ be the event that

$$ |B_{k2^{-n}}| > a, \quad |B_{j2^{-n}}| \leq a,\; j = 1, \ldots, k-1. $$

Then the event $\{Y_n > a\}$ can be written as a disjoint union

$$ \{Y_n > a\} = \bigcup_{k=1}^{2^n} A_k. $$

The important observation is that if $|B_{k2^{-n}}| > a$, then with probability at least $1/2$, we have $|B_1| > a$. Indeed, if $B_{k2^{-n}}$ and $B_1 - B_{k2^{-n}}$

### PDF page 56 (book page 50)

have the same sign, which happens with probability $1/2$, then $|B_1| \geq |B_{k2^{-n}}|$. Therefore,

$$ \mathbb{P}\left[A_k \cap \{|B_1| > a\}\right] \geq \frac{1}{2}\,\mathbb{P}(A_k), $$

and hence

$$ \begin{aligned} \mathbb{P}\{|B_1| > a\} &= \sum_{k=1}^{2^n} \mathbb{P}\left[A_k \cap \{|B_1| > a\}\right] \\ &\geq \frac{1}{2} \sum_{k=1}^{2^n} \mathbb{P}\left[A_k\right] \\ &= \frac{1}{2}\,\mathbb{P}\{Y_n > a\}. \end{aligned} $$

Here we use the fact that the events $A_k$ are disjoint. Therefore, since $B_1$ has a $N(0,1)$ distribution,

$$ \mathbb{P}\{Y_n > a\} \leq 2\,\mathbb{P}\{|B_1| > a\} = 4\,\mathbb{P}\{B_1 > a\} = \frac{4}{\sqrt{2\pi}} \int_a^{\infty} e^{-x^2/2}\,dx. $$

To estimate the integral for $a \geq 4$, we write

$$ \begin{aligned} \frac{4}{\sqrt{2\pi}} \int_a^{\infty} e^{-x^2/2}\,dx &\leq 2 \int_a^{\infty} e^{-ax/2}\,dx \\ &= \frac{4}{a}\,e^{-a^2/2} \leq e^{-a^2/2}. \end{aligned} $$

This proves Lemma 2.5.2. If we apply the estimate with $a = C\,\sqrt{n}$, then we see that for large $n$,

$$ \mathbb{P}\{Y > C\,\sqrt{n}\} \leq e^{-C^2 n/2} = 2^{-n\beta}, \quad \beta = \frac{C^2}{2\log 2}. $$

In particular, if $\beta > 1$, then (2.3) holds and this gives (2.2) with probability one.

The hard work is finished, with the proposition, we can now *define $B_t$* for $t \in [0, 1]$ by

$$ B_t = \lim_{t_n\to\infty} B_{t_n} $$

where $t_n \to t, t_n \in \mathcal{D}$. One needs to check that this satisfies the conditions for a Brownian motion. This is relatively straightforward and we omit it.

### PDF page 57 (book page 51)

**2.6 Understanding Brownian motion**

Let $B_t$ be a standard Brownian motion starting at the origin. By doing simulations, one can see that although the paths of the process are continuous they are very rough. To do simulations, we must discretize time. If we let $\Delta t$ be chosen, then we will sample the values

$$ B_0, B_{\Delta t}, B_{2\Delta t}, B_{3\Delta t}, \ldots $$

The increment $B_{(k+1)\Delta t} - B_{k\Delta t}$ is a normal random variable with mean 0 and variance $\Delta t$. If $N_0, N_1, N_2, \ldots$ denote independent $N(0, 1)$ random variables (which can be generated on a computer), we set

$$ B_{(k+1)\Delta t} = B_{k\Delta t} + \sqrt{\Delta t}\,N_k, $$

which we can write as

$$ \Delta B_{k\Delta t} = B_{(k+1)\Delta t} - B_{k\Delta t} = \sqrt{\Delta t}\,N_k. $$

The relationship $|\Delta B_t| = |B_{t+\Delta t} - B_t| \approx \sqrt{\Delta t}$ is fundamental for understanding Brownian motion. As $\Delta t \to 0$, $\sqrt{\Delta t} \to 0$, which is consistent with the continuity of the paths. However, we claim that the paths do not have derivatives. To see why this should be true, recall that the definition of the derivative at time $t$ would be

$$ \lim_{\Delta t\to 0} \frac{B_{t+\Delta t} - B_t}{\Delta t}. $$

As $\Delta t \to 0$, the absolute value of the numerator is of order $\sqrt{\Delta t}$ which is much larger than $\Delta t$ for small $\Delta t$. Hence, we do not expect the limit to exist. In fact, the following stronger statement is true.

**Theorem 2.6.1.** *With probability one, the function $t \mapsto B_t$ is nowhere differentiable.*

Note carefully the statement of this theorem. It is a stronger statement than the similar statement: "for every $t$, with probability one, the derivative does not exists [sic] at $t$". As a comparison, consider the following two statements:

- With probability one, for every $t$, $B_t \neq 1$.

- For every $t$, with probability one, $B_t \neq 1$.

### PDF page 58 (book page 52)

Since $B_t$ has a $N(0, t)$ distribution, the second of these statements is obviously true. However, the first statement is false. To see this, note that $\mathbb{P}\{B_1 > 1\}$ is greater than 0, and if $B_0 = 0, B_1 > 1$, then continuity implies that there exists $t \in (0, 1)$ such that $B_t = 1$. Here again we have the challenge of dealing with uncountably many events of probability 0. Even though for each $t$, $\mathbb{P}\{B_t = 1\} = 0$,

$$ \mathbb{P}\left[\bigcup_{t\in[0,1]} \{B_t = 1\}\right] > 0. $$

While nondifferentiable paths may seem surprising, a little thought about our assumptions will show why we could not expect to have differentiable paths. Suppose that $B_t$ were differentiable at $t$. Then, we could determine the derivative by observing $B_s, 0 \le s \le t$. This would then tell us something about the increment $B_{t+\Delta t} - B_t$ for $\Delta t > 0$. However, our assumptions tell us that $B_{t+\Delta t} - B_t$ is independent of $B_s, 0 \le s \le t$.

We will make a more precise statement about the relationship $|\Delta B_t| = |B_{t+\Delta t} - B_t| \approx \sqrt{\Delta t}$. If $\alpha > 0$, then a function $f : [0, 1] \to \mathbb{R}$ is *Hölder continuous of order $\alpha$* if there exists $C < \infty$ such that for all $0 \le s, t \le 1$,

$$ |f(s) - f(t)| \le C\,|s - t|^{\alpha}. $$

The smaller $\alpha$ is the easier it is to be Hölder continuous of order $\alpha$. Note that differentiable functions are Hölder continuous of order 1 since

$$ |f(s) - f(t)| \approx |f'(t)|\,|s - t|. $$

**Theorem 2.6.2.** *With probability one, for all $\alpha < 1/2$, $B_t$ is Hölder continuous of order $\alpha$ but it is not Hölder continuous of order $1/2$.*

We will be using Brownian motion and functions of Brownian motions to model prices of assets. In all of the Brownian models, the functions will have Hölder exponent $1/2$.

---

We will prove Theorem 2.6.1 for $0 \le t \le 1$. We start by making an observation about differentiable functions. Suppose $B_t$ were differentiable at some $0 \le t \le 1$ with derivative $r$. Then there would exist $\delta$ such that for $|t - s| \le \delta$,

$$ |B_t - B_s| \le 2|r(t - s)|. $$

### PDF page 59 (book page 53)

Hence, we could find a positive integer $M < \infty$ such that for all sufficiently large integers $n$, there exists $k \le n$ such that $Y_{k,n} \le M/n$, where $Y_{k,n}$ is

$$ \max\left\{ \left| B\left(\frac{k + 1}{n}\right) - B\left(\frac{k}{n}\right) \right|, \right. $$

$$ \left. \left| B\left(\frac{k + 2}{n}\right) - B\left(\frac{k + 1}{n}\right) \right|, \left| B\left(\frac{k + 3}{n}\right) - B\left(\frac{k + 2}{n}\right) \right| \right\}. $$

Let $Y_n = \min\{Y_{k,n} : k = 0, 1, \ldots, n - 1\}$ and let $A_M$ be the event that for all $n$ sufficiently large, $Y_n \le M/n$. For each positive integer $M$,

$$
\begin{aligned}
\mathbb{P}\{Y_{k,n} \le M/n\} &= \left[\mathbb{P}\{|B(1/n)| \le M/n\}\right]^3 \\
&= \left[\mathbb{P}\{n^{-1/2}\,|B_1| \le M/n\}\right]^3 \\
&= \left[\int_{|x|\le M/\sqrt{n}} \frac{1}{\sqrt{2\pi}} e^{-y^2/2}\,dy\right]^3 \\
&\le \left[\frac{2M}{\sqrt{n}}\,\frac{1}{\sqrt{2\pi}}\right]^3 \le \frac{M^3}{n^{3/2}},
\end{aligned}
$$

and hence,

$$ \mathbb{P}\{Y_n \le M/n\} \le \sum_{k=0}^{n-1} \mathbb{P}\{Y_{k,n} \le M/n\} \le \frac{M^3}{n^{1/2}} \longrightarrow 0. $$

This shows that $\mathbb{P}(A_M) = 0$ for each $M$, and hence

$$ \mathbb{P}\left[\bigcup_{M=1}^{\infty} A_M\right] = 0. $$

But our first remark shows that the event that $B_t$ is differentiable at some point is contained in $\cup_M A_M$.

Theorem 2.6.2 is a restatement of (2.2).

### PDF page 60 (book page 54)

**2.6.1 Brownian motion as a continuous martingale**

The definition of a martingale in continuous time is essentially the same as in discrete time. Suppose we have an increasing filtration $\{\mathcal{F}_t\}$ of information and integrable random variables $M_t$ such that for each $t$, $M_t$ is $\mathcal{F}_t$-measurable. (We say that $M_t$ is *adapted* to the filtration if $M_t$ is $\mathcal{F}_t$-measurable for each $t$.) Then, $M_t$ is a *martingale* with respect to $\{\mathcal{F}_t\}$ if for each $s < t$,

$$ E\left[M_t \mid \mathcal{F}_s\right] = M_s. $$

When one writes an equality as above there is an implicit "up to an event of probability zero". In discrete time this presents no problem because there are only a countable number of pairs of times $(s, t)$ and hence there can be only a countable number of sets of measure zero. For continuous time, there are instances where some care is needed but we will not worry about this at the moment. As in the discrete case, if the filtration is not mentioned explicitly then one assumes that $\mathcal{F}_t$ is the information contained in $\{M_s : s \le t\}$. In that case, if $B_t$ is a standard Brownian motion and $s < t$,

$$ E[B_t \mid \mathcal{F}_s] = E[B_s \mid \mathcal{F}_s] + E[B_t - B_s \mid \mathcal{F}_s] = B_s + \mathbb{E}[B_t - B_s] = B_s. \tag{2.4} $$

Often we will have more information at time $t$ than the values of the Brownian motion so it is useful to extend our definition of Brownian motion. We say that $B_t$ is Brownian motion with respect to the filtration $\{\mathcal{F}_t\}$ if each $B_t$ is $\mathcal{F}_t$-measurable and $B_t$ satisfies the conditions to be a Brownian motion with the third condition being replaced by

- If $s < t$, the random variable $B_t - B_s$ is independent of $\mathcal{F}_s$.

In other words, although we may have more information at time $s$ than the value of the Brownian motion, there is nothing useful for predicting the future increments. Under these conditions, (2.4) holds and $B_t$ is a martingale with respect to $\{\mathcal{F}_t\}$.

If $M_s, 0 \le s \le t$ is a martingale, then by definition, for each $s \le t$,

$$ E(Y \mid \mathcal{F}_s) = M_s $$

where $Y = M_t$. Conversely, if $Y$ is an integrable random variable that is measurable with respect to $\mathcal{F}_t$, we can define a martingale $M_s, 0 \le s \le t$ by

$$ M_s = \mathbb{E}(Y \mid \mathcal{F}_s). $$

### PDF page 61 (book page 55)

*2.6. UNDERSTANDING BROWNIAN MOTION*

Indeed, if we define $M_s$ as above and $r < s$, then the tower property for conditional expectation implies that

$$ E(M_s \mid \mathcal{F}_r) = E(E(Y \mid \mathcal{F}_s) \mid \mathcal{F}_r) = E(Y \mid \mathcal{F}_r) = M_r. $$

A martingale $M_t$ is called a *continuous martingale* if with probability one the function $t \mapsto M_t$ is a continuous function. The word continuous in continuous martingale refers not just to the fact that time is continuous but also to the fact that the paths are continuous functions of $t$. One can have martingales in continuous time that are not continuous martingales. One example is to let $N_t$ be a Poisson process with rate $\lambda$ as in Section 2.1 and

$$ M_t = N_t - \lambda\, t. $$

Then using the fact that the increments are independent we see that for $s < t$,

$$
\begin{aligned}
E[M_t \mid \mathcal{F}_s] &= E[M_s \mid \mathcal{F}_s] + E[N_t - N_s \mid \mathcal{F}_s] - \lambda(t - s) \\
&= M_s + \mathbb{E}\,[N_t - N_s] - \lambda(t - s) = M_s.
\end{aligned}
$$

Brownian motion with zero drift ($m = 0$) is a continuous martingale with one parameter $\sigma$. As we will see, the *only* continuous martingales are essentially Brownian motion where one allows the $\sigma$ to vary with time. The factor $\sigma$ will be the analogue of the "bet" from the discrete stochastic integral.

---

A continuous time filtration on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ is a collection of sub-$\sigma$-algebras $\{\mathcal{F}_t\}$ of $\mathcal{F}$ such that if $s < t$, then $\mathcal{F}_s \subset \mathcal{F}_t$. It has been found that it is useful to make some additional technical assumptions. First, we assume that $\mathcal{F}$ is *complete* under $\mathbb{P}$, that is, it contains all the nulls sets. A set $A' \subset \Omega$ is a *null set (for $\mathbb{P}$)* if $A' \subset A$ for some $A \in \mathcal{F}$ with $\mathbb{P}(A) = 0$. This is convenient for then one can prove that an event has probability zero by showing that it is contained in an event of probability zero. If $\mathcal{F}$ is not complete, one can complete it by considering the collection of subsets $A \cup A'$ where $A \in \mathcal{F}$ and $A'$ is a null set. In the case of Lebesgue measure on the Borel subsets of $\mathbb{R}$, the completion is the set of Lebesgue measurable sets.

When using filtrations $\{\mathcal{F}_t\}$ one often makes further assumptions:

### PDF page 62 (book page 56)

- *Right continuity.* For each $t$

$$ \mathcal{F}_t = \bigcap_{s>t} \mathcal{F}_s. $$

  It is easy to check that the right-hand side is a $\sigma$-algebra containing $\mathcal{F}_t$. and it is often denoted by $\mathcal{F}_{t+}$. Right continuity states that $\mathcal{F}_t = \mathcal{F}_{t+}$. If the original filtration was not right continuous, we can replace it with the filtration $\{\mathcal{F}_{t+}\}$.

- *(Strong) completeness.* We assume that $\mathcal{F}_t$ contains all the null sets of $\mathcal{F}$ (note that this is stronger than saying that $\mathcal{F}_t$ is complete). If this does not hold initially, we enlarge our $\sigma$-algebra to include all events of the form $A \cup A'$ where $A \in \mathcal{F}_t$ and $A'$ is a null set.

If we start with Brownian motion and let $\mathcal{F}_t$ be the $\sigma$-algebra generated by $\{B_s : s \leq t\}$, then it is not true that $\mathcal{F}_t = \mathcal{F}_{t+}$. However, it is almost true in the sense that every set in $\mathcal{F}_{t+}$ can be written as $A \cup A'$ where $A \in \mathcal{F}_t$ and $A'$ is a null set. This is a consequence of the Blumenthal $0 - 1$ law that states that the $\sigma$-algebra $\mathcal{F}_{0+}$ contains only events of probability zero or one. We will not prove this here but it is related to the Kolmogorov $0 - 1$ law.

At this point one may not appreciate why one wants to make these assumptions, but we will not try to motivate them further.

---

**2.6.2 Brownian motion as a Markov process**

A continuous time process $X_t$ is called *Markov* if for every $t$, the conditional distribution of $\{X_s : s \geq t\}$ given $\{X_r : r \leq t\}$ is the same as the conditional distribution given $X_t$. In other words, the future of the process is conditionally independent of the past given the present value.

Brownian motion is a Markov process. Indeed, if $B_t$ is a Brownian motion with parameters $(m, \sigma^2)$, and

$$ Y_s = B_{t+s}, \quad 0 \leq s < \infty, $$

then the conditional distribution of $\{Y_s\}$ given $\mathcal{F}_t$ is that of a Brownian motion with initial condition $Y_0 = B_t$. Indeed, if

$$ \hat{B}_s = B_{t+s} - B_t, $$

### PDF page 63 (book page 57)

*2.6. UNDERSTANDING BROWNIAN MOTION*

then $\hat{B}_s$ is a Brownian motion that is independent of $\mathcal{F}_t$. There is a stronger notion of this called the *strong Markov property* that we will discuss in Section 2.7.

**2.6.3 Brownian motion as a Gaussian process**

A process $\{X_t\}$ is called a *Gaussian process* if each finite subcollection

$$ (X_{t_1}, \ldots, X_{t_n}) $$

has a joint normal distribution. Recall that to describe a joint normal distribution one needs only give the means and the covariances. Hence the *finite-dimensional distributions* of a Gaussian process are determined by the numbers

$$ m_t = \mathbb{E}[X_t], \quad \Gamma_{st} = \mathrm{Cov}(X_s, X_t). $$

If $B_t$ is a standard Brownian motion and $t_1 < t_2 < \cdots < t_n$, then we can write $B_{t_1}, \ldots, B_{t_n}$ as linear combinations of the independent standard normal random variables

$$ Z_j = \frac{B_{t_j} - B_{t_{j-1}}}{\sqrt{t_j - t_{j-1}}}, \quad j = 1, \ldots, n. $$

Hence $B_t$ is a Gaussian process with mean zero. If $s < t$,

$$
\begin{aligned}
\mathbb{E}[B_s B_t] &= \mathbb{E}\,[B_s\,(B_s + B_t - B_s)] \\
&= \mathbb{E}[B_s^2] + \mathbb{E}[B_s(B_t - B_s)] \\
&= s + \mathbb{E}[B_s]\,\mathbb{E}[B_t - B_s] = s,
\end{aligned}
$$

which gives the general rule

$$ \mathrm{Cov}(B_s, B_t) = \min\{s, t\}. $$

The description of Brownian motion as a Gaussian process describes only the finite-dimensional distributions but our definition includes some aspects that depend on more than finite-dimensional distributions. In particular, one cannot tell from the finite-dimensional distributions alone whether or not the paths are continuous.

### PDF page 64 (book page 58)

**2.6.4  Brownian motion as a self-similar process**

If one looks at a small piece of a Brownian motion and blows it up, then the blown-up picture looks like a Brownian motion provided that the dilation uses the appropriate scaling. We leave the derivation as Exercise 2.12.

**Theorem 2.6.3.** *Suppose $B_t$ is a standard Brownian motion and $a > 0$. Let*

$$ Y_t = \frac{B_{at}}{\sqrt{a}}. $$

*Then $Y_t$ is a standard Brownian motion.*

The key here is that if time is scaled by a factor of $a$, then space must be scaled by a factor of $1/\sqrt{a}$. The proof of this theorem is not difficult; one needs only show that $Y_t$ satisfies the conditions to be a standard Brownian motion. One can check that the scaling is right by computing

$$ \mathrm{Var}[Y_t] = \mathrm{Var}[B_{at}/\sqrt{a}] = a^{-1}\,\mathrm{Var}[B_{at}] = a^{-1}\,(at) = t. $$

**2.7  Computations for Brownian motion**

We will discuss some methods for computing probabilities for Brownian motions. For ease, we will assume that $B_t$ is a standard Brownian motion starting at the origin with respect to a filtration $\{\mathcal{F}_t\}$. If we are interested in probabilities about the Brownian motion at one time $t$, we need only use the normal distribution. Often, it is easier to scale to the standard normal. For example,

$$ \begin{aligned} \mathbb{E}\left[|B_t|\right] = \mathbb{E}\left[t^{1/2}|B_1|\right] &= \frac{t^{1/2}}{\sqrt{2\pi}} \int_{-\infty}^{\infty} |x|\, e^{-x^2/2}\, dx \\ &= \sqrt{\frac{2t}{\pi}} \int_{0}^{\infty} x\, e^{-x^2/2}\, dx \\ &= \sqrt{\frac{2t}{\pi}}, \end{aligned} $$

and

$$ \begin{aligned} \mathbb{P}\{B_t \geq r\} = \mathbb{P}\{\sqrt{t}\, B_1 \geq r\} &= \mathbb{P}\{B_1 \geq r/\sqrt{t}\} \\ &= 1 - \Phi(r/\sqrt{t}) \\ &= \int_{r/\sqrt{t}}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\, dx, \end{aligned} $$

### PDF page 65 (book page 59)

where $\Phi$ denotes the distribution function for a standard normal.

If we are considering probabilities for a finite number of times, we can use the joint normal distribution. Often it is easier to use the Markov property as we now illustrate. We will compute

$$ \mathbb{P}\{B_1 > 0, B_2 > 0\}. $$

The events $\{B_1 > 0\}$ and $\{B_2 > 0\}$ are not independent; we would expect them to be positively correlated. We compute by considering the possibilities at time 1,

$$ \begin{aligned} \mathbb{P}\{B_1 > 0, B_2 > 0\} &= \int_{0}^{\infty} \mathbb{P}\{B_2 > 0 \mid B_1 = x\}\, d\mathbb{P}\{B_1 = x\} \\ &= \int_{0}^{\infty} \mathbb{P}\{B_2 - B_1 > -x\}\, \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\, dx \\ &= \int_{0}^{\infty} \int_{-x}^{\infty} \frac{1}{2\pi} e^{-(x^2+y^2)/2}\, dy\, dx \\ &= \int_{0}^{\infty} \int_{-\pi/4}^{\pi/2} \frac{e^{-r^2/2}}{2\pi}\, d\theta\, r\, dr = \frac{3}{8}. \end{aligned} $$

One needs to review polar coordinates to do the fourth equality. Note that

$$ \mathbb{P}\{B_2 > 0 \mid B_1 > 0\} = \frac{\mathbb{P}\{B_1 > 0, B_2 > 0\}}{\mathbb{P}\{B_1 > 0\}} = \frac{3}{4}, $$

which confirms our intuition that the events are positively correlated.

For more complicated calculations, we need to use the *strong Markov property*. We say that a random variable $T$ taking values in $[0, \infty]$ is a *stopping time (with respect to the filtration $\{\mathcal{F}_t\}$)* if for each $t$, the event $\mathbb{P}\{T \leq t\}$ is $\mathcal{F}_t$-measurable. In other words, the decision to stop can use the information up to time $t$ but cannot use information about the future values of the Brownian motion.

- If $x \in \mathbb{R}$ and

$$ T = \min\{t : B_t = x\}, $$

  then $T$ is a stopping time.

- Constants are stopping times.

### PDF page 66 (book page 60)

- If $S, T$ are stopping times then

$$ S \wedge T = \min\{S, T\} $$

  and

$$ S \vee T = \max\{S, T\} $$

are stopping times.

**Theorem 2.7.1** (Strong Markov Property)**.** *If $T$ is a stopping time with $\mathbb{P}\{T < \infty\} = 1$ and*

$$ Y_t = B_{T+t} - B_T, $$

*then $Y_t$ is a standard Brownian motion. Moreover, $Y$ is independent of*

$$ \{B_t : 0 \leq t \leq T\}. $$

Let us apply this theorem, to prove a very useful tool for computing probabilities.

**Proposition 2.7.2** (Reflection Principle)**.** *If $B_t$ is a standard Brownian motion with $B_0 = 0$, then for every $a > 0$,*

$$ \mathbb{P}\left\{\max_{0 \leq s \leq t} B_s \geq a\right\} = 2\mathbb{P}\{B_t > a\} = 2\left[1 - \Phi(a/\sqrt{t})\right]. $$

To derive the reflection principle, let

$$ T_a = \min\{s : B_s \geq a\} = \min\{s : B_s = a\}. $$

The second equality holds because $B_s$ is a continuous function of $s$. Then

$$ \mathbb{P}\left\{\max_{0 \leq s \leq t} B_s \geq a\right\} = \mathbb{P}\{T_a \leq t\} = \mathbb{P}\{T_a < t\}. $$

The second equality uses the fact that $\mathbb{P}\{T_a = t\} \leq \mathbb{P}\{B_t = a\} = 0$. Since $B_{T_a} = a$,

$$ \begin{aligned} \mathbb{P}\{B_t > a\} &= \mathbb{P}\{T_a < t, B_t > a\} \\ &= \mathbb{P}\{T_a < t\}\, \mathbb{P}\{B_t - B_{T_a} > 0 \mid T_a < t\}. \end{aligned} $$

We now appeal to the Strong Markov Property to say that

$$ \mathbb{P}\{B_t - B_{T_a} > 0 \mid T_a < t\} = 1/2. $$

This gives the first equality of the proposition and the second follows from

$$ \mathbb{P}\{B_t > a\} = \mathbb{P}\{B_1 > a/\sqrt{t}\} = 1 - \Phi(a/\sqrt{t}). $$

### PDF page 67 (book page 61)

**Example 2.7.1.** Let $a > 0$ and let $T_a = \inf\{t : B_t = a\}$. The random variable $T_a$ is called a *passage time*. We will find the density of $T_a$. To do this, we first find its distribution function

$$ F(t) = \mathbb{P}\{T_a \le t\} = \mathbb{P}\left\{ \max_{0 \le s \le t} B_s \ge a \right\} = 2 \left[ 1 - \Phi(a/\sqrt{t}) \right]. $$

The density is obtained by differentiating

$$ f(t) = F'(t) = -2\Phi'\left( \frac{a}{\sqrt{t}} \right) \left( -\frac{a}{2t^{3/2}} \right) = \frac{a}{t^{3/2}\sqrt{2\pi}}\, e^{-\frac{a^2}{2t}}, \quad 0 < t < \infty. $$

**Example 2.7.2.** We will compute

$$ q(r,t) = \mathbb{P}\left\{ B_s = 0 \text{ for some } r \le s \le t \right\}. $$

The scaling rule for Brownian motion (Theorem 2.6.3) shows that $q(r,t) = q(1, t/r)$, so it suffices to compute $q(t) = q(1, 1+t)$. Let $A$ be the event that $B_s = 0$ for some $1 \le s \le 1+t$. The Markov property for Brownian motion and symmetry imply that

$$
\begin{aligned}
q(t) &= \int_{-\infty}^{\infty} \mathbb{P}[A \mid B_1 = r]\, d\mathbb{P}\{B_1 = r\} \\
&= \int_{-\infty}^{\infty} \mathbb{P}[A \mid B_1 = r] \left[ \frac{1}{\sqrt{2\pi}}\, e^{-r^2/2}\, dr \right] \\
&= \sqrt{\frac{2}{\pi}} \int_{0}^{\infty} \mathbb{P}[A \mid B_1 = r]\, e^{-r^2/2}\, dr.
\end{aligned}
$$

The reflection principle and symmetry imply that

$$ \mathbb{P}[A \mid B_1 = r] = \mathbb{P}\left\{ \min_{1 \le s \le 1+t} B_s \le 0 \mid B_1 = r \right\} = $$

$$ \mathbb{P}\left\{ \max_{0 \le s \le t} B_s \ge r \right\} = 2\mathbb{P}\{B_t \ge r\} = 2\left[ 1 - \Phi(r/\sqrt{t}) \right]. $$

Combining this we get

$$ q(t) = \int_{-\infty}^{\infty} 2\left[ 1 - \Phi(r/\sqrt{t}) \right] \frac{1}{\sqrt{2\pi}} e^{-r^2/2}\, dr. $$

This integral can be computed with polar coordinates. We just give the answer

$$ q(t) = 1 - \frac{2}{\pi} \arctan \frac{1}{\sqrt{t}}. $$

### PDF page 68 (book page 62)

If the filtration $\{\mathcal{F}_t\}$ is right continuous then the condition $\{T \le t\} \in \mathcal{F}_t$ for all $t$ is equivalent to the condition that $\{T < t\} \in \mathcal{F}_t$ for all $t$. Indeed,

$$ \{T \le t\} = \bigcap_{n=1}^{\infty} \left\{ T < t + \frac{1}{n} \right\} \in \mathcal{F}_{t+}, $$

$$ \{T < t\} = \bigcup_{n=1}^{\infty} \left\{ T \le t - \frac{1}{n} \right\} \in \mathcal{F}_t. $$

If $T$ is a stopping time, the $\sigma$-algebra $\mathcal{F}_T$ is defined to be the set of events $A \in \mathcal{F}$ such that for each $t$, $A \cap \{T \le t\} \in \mathcal{F}_t$. (It is not hard to show that this is a $\sigma$-algebra.) We think of $\mathcal{F}_T$ as the information available up to time $T$. If $\{T < \infty\}$ let

$$ Y_t = B_{T+t} - B_T, $$

and let $\mathcal{G}_T$ denote the $\sigma$-algebra generated by $\{Y_t : t \ge 0\}$. We can state the strong Markov property as:

- $\{Y_t : t \ge 0\}$ is a standard Brownian motion.

- The $\sigma$-algebras $\mathcal{F}_T$ and $\mathcal{G}_T$ are independent, that is, if $A \in \mathcal{F}_T, A' \in \mathcal{G}_T$, then $\mathbb{P}(A \cap A') = \mathbb{P}(A)\, \mathbb{P}(A')$.

To prove this, one first considers the case where $T$ takes values in $\{k2^{-n} : k = 0, 1, 2, \ldots\}$. By splitting up separately into the events $\{T = k2^{-n}\}$, one can use the usual Markov property to prove the result. For more general stopping times $T$ we approximate $T$ by $T_n$ where $T_n = k2^{-n}$ on the event $\{(k-1)2^{-n} < T \le k2^{-n}\}$. It is important that we approximate "from above" in order to guarantee that the $T_n$ are stopping times. The continuity of the Brownian paths implies that

$$ Y_t = \lim_{n \to \infty} \left[ B_{T_n + t} - B_{T_n} \right], $$

and this can be used to conclude the independence of $\mathcal{F}_T$ and $\mathcal{G}_T$.

### PDF page 69 (book page 63)

**2.8 Quadratic variation**

In the next chapter we will come across quantities such as

$$ Q_n = \sum_{j=1}^{n} \left[ B\left( \frac{j}{n} \right) - B\left( \frac{j-1}{n} \right) \right]^2, $$

where $B_t$ is a standard Brownian motion. We can write $Q_n$ as

$$ \frac{1}{n} \sum_{j=1}^{n} Y_j, $$

where

$$ Y_j = Y_{j,n} = \left[ \frac{B\left( \frac{j}{n} \right) - B\left( \frac{j-1}{n} \right)}{1/\sqrt{n}} \right]^2. $$

The random variables $Y_1, \ldots, Y_n$ are independent, each with the distribution of $Z^2$ where $Z$ is a standard normal. In particular,

$$ \mathbb{E}[Y_j] = \mathbb{E}\left[ Z^2 \right] = 1, \quad \mathbb{E}\left[ Y_j^2 \right] = \mathbb{E}\left[ Z^4 \right] = 3. $$

(One can use integration by parts to calculate $\mathbb{E}[Z^4]$ or one could just look it up somewhere.) Hence $\mathrm{Var}[Y_j] = \mathbb{E}\left[ Y_j^2 \right] - \mathbb{E}[Y_j]^2 = 2$, and

$$ \mathbb{E}[Q_n] = \frac{1}{n} \sum_{j=1}^{n} \mathbb{E}[Y_j] = 1, \quad \mathrm{Var}[Q_n] = \frac{1}{n^2} \sum_{j=1}^{n} \mathrm{Var}[Y_j] = \frac{2}{n}. $$

As $n \to \infty$, the variance of $Q_n$ tends to zero and the random variable approaches a constant random variable of 1.

Similarly, for any time $t$, we let

$$ Q_n(t) = \sum_{j \le tn} \left[ B\left( \frac{j}{n} \right) - B\left( \frac{j-1}{n} \right) \right]^2. $$

As $n \to \infty$, the variance of $Q_n(t)$ goes to zero and it approaches a constant random variable with value $t$.

**Definition** If $X_t$ is a process, the *quadratic variation* is defined by

$$ \langle X \rangle_t = \lim_{n \to \infty} \sum_{j \le tn} \left[ X\left( \frac{j}{n} \right) - X\left( \frac{j-1}{n} \right) \right]^2, $$

where the sum is over all $j$ with $j/n \le t$.

### PDF page 70 (book page 64)

The calculation above shows that the quadratic variation of a standard Brownian motion is the constant process $\langle B\rangle_t = t$. Suppose $W_t$ is a Brownian motion with drift $m$ and variance $\sigma^2$. Then we can write $W_t = \sigma B_t + mt$ where $B_t$ is a standard Brownian motion. Fix $t$ and write

$$\sum \left[ W\left(\frac{j}{n}\right) - W\left(\frac{j-1}{n}\right)\right]^2 = \sigma^2 \sum \left[ B\left(\frac{j}{n}\right) - B\left(\frac{j-1}{n}\right)\right]^2$$
$$+ \frac{2\sigma m}{n} \sum \left[ B\left(\frac{j}{n}\right) - B\left(\frac{j-1}{n}\right)\right] + \sum \frac{m^2}{n^2},$$

where in each case the sum is over $j \leq tn$. As $n \to \infty$,

$$\sigma^2 \sum \left[ B\left(\frac{j}{n}\right) - B\left(\frac{j-1}{n}\right)\right]^2 \longrightarrow \sigma^2 \langle B\rangle_t = \sigma^2 t,$$

$$\frac{2\sigma m}{n} \sum \left[ B\left(\frac{j}{n}\right) - B\left(\frac{j-1}{n}\right)\right] \sim \frac{2\sigma m}{n} B_t \longrightarrow 0,$$

$$\sum \frac{m^2}{n^2} \sim \frac{tnm^2}{n^2} \longrightarrow 0.$$

We have established the following.

**Theorem 2.8.1.** *If $W_t$ is a Brownian motion with drift $m$ and variance $\sigma^2$, then $\langle W\rangle_t = \sigma^2 t$.*

The important facts are that the quadratic variation is not random and that it depends on the variance but not on the mean. It may seem silly at this point to give a name and notation to a quantity which is almost trivial for Brownian motion, but in the next chapter we will deal with processes for which the quadratic variation is not just a linear function of time.

---

If $0 = t_0 < t_1 < \cdots < t_n = t$, we call the times a *partition* of $[0, t]$. We will write $\Pi$ for partitions and write

$$\|\Pi\| = \max_{j=1,\dots,n} \{t_j - t_{j-1}\}.$$

For any partition of $[0, t]$, we define

$$Q(t; \Pi) = \sum_{j=1}^{n} [B(t_j) - B(t_{j-1})]^2 .$$

### PDF page 71 (book page 65)

Computing as above, we see that

$$\mathbb{E}[Q(t; \Pi)] = \sum_{j=1}^{n} (t_j - t_{j-1}) = t,$$

$$\begin{aligned}
\mathrm{Var}[Q(t; \Pi)] &= \sum_{j=1}^{n} \mathrm{Var}\left( [B(t_j) - B(t_{j-1})]^2 \right) \\
&= 2 \sum_{j=1}^{n} (t_j - t_{j-1})^2 \\
&\leq 2\|\Pi\| \sum_{j=1}^{n} (t_j - t_{j-1}) = 2\|\Pi\| t.
\end{aligned}$$

**Theorem 2.8.2.** *Suppose $B$ is a standard Brownian motion, $t > 0$, and $\Pi_n$ is a sequence of partitions of the form*

$$0 = t_{0,n} < t_{1,n} < \cdots < t_{l_n,n} = t,$$

*with $\|\Pi_n\| \to 0$. Then $Q(t; \Pi_n) \to t$ in probability. Moreover, if*

$$\sum_{n=1}^{\infty} \|\Pi_n\| < \infty, \tag{2.5}$$

*then with probability one $Q(t; \Pi_n) \to t$.*

*Proof.* Using Chebyshev's inequality, we see that for each integer $k$,

$$\mathbb{P}\left\{ |Q(t; \Pi_n) - t| > \frac{1}{k} \right\} \leq \frac{\mathrm{Var}[Q(t; \Pi_n)]}{(1/k)^2} \leq 2k^2 \|\Pi_n\| t,$$

and the right-hand side goes to zero as $n \to \infty$. This gives convergence in probability. If (2.5) holds as well, then

$$\sum_{n=1}^{\infty} \mathbb{P}\left\{ |Q(t; \Pi_n) - t| > \frac{1}{k} \right\} < \infty,$$

and hence by the Borel-Cantelli lemma, with probability one, for all $n$ sufficiently large,

$$|Q(t; \Pi_n) - t| \leq \frac{1}{k}. \quad \square$$

### PDF page 72 (book page 66)

It is important to note the order of the quantifiers in this theorem. Let $t = 1$. The theorem states that for every sequence $\{\Pi_n\}$ satisfying (2.5), $Q(1; \Pi_n) \to 1$. The event of measure zero on which convergence does not hold depends on the sequence of partitions. Because there are an uncountable number of such sequences we cannot conclude from the theorem that with probability one, for all sequences $\{\Pi_n\}$ satisfying (2.5), that $Q(1; \Pi_n) \to 1$. In fact, the latter statement is false. Let us give an example. Let us start with the dyadic partition $\Pi_n$ of $[0, 1]$ with $2^n$ intervals of length $2^{-n}$. We will now subdivide some, but not all, of these intervals into two equal pieces. Suppose $[s, t]$ is one of these intervals and let $r$ denote the midpoint. We will subdivide $[s, t]$ into $[s, r]$ and $[r, t]$ if

$$(B_r - B_s)^2 + (B_t - B_r)^2 > (B_t - B_s)^2,$$

and we will retain the interval $[s, t]$ otherwise. This defines a partition $\tilde{\Pi}_n$ with $\|\tilde{\Pi}_n\| \leq \|\Pi_n\|$. It has been chosen so that $Q(1; \tilde{\Pi}_n) \geq Q(1; \Pi_n)$, and one can show (see Exercise 2.5) that

$$\lim_{n\to\infty} Q(1; \tilde{\Pi}_n) = \mathbb{E}\left[ \max\{B_{1/2}^2 + (B_1 - B_{1/2})^2, B_1^2\} \right] > 1.$$

This does not contradict the theorem because the partitions $\tilde{\Pi}_n$ depend on the realization of the Brownian motion.

Sometimes it is convenient to fix a sequence of partitions, say partitions with dyadic intervals. Let

$$Q_n(t) = \sum_{j < t2^n} \left[ B\left(\frac{j+1}{2^n}\right) - B\left(\frac{j}{2^n}\right)\right]^2 .$$

Since the dyadic rationals are countable, the theorem implies that with probability one for every dyadic rational $t$, $Q_n(t) \to t$. However, since $t \mapsto Q_n(t)$ is increasing, we can conclude that with probability one, for every $t0$ [sic], $Q_n(t) \to t$.

# 2.9 Multidimensional Brownian motion

In finance one is often interested in considering the value of many assets at the same time. Multidimensional Brownian motion $B_t$ is random continuous motion in $d$-dimensional space. It can be viewed as $d$ one-dimensional

### PDF page 73 (book page 67)

Brownian motions
$$ B_t = \left( B_t^1, \ldots, B_t^d \right), $$
with perhaps some correlations. If we make the same assumptions that we made in the one-dimensional case (independent, identically distributed increments and continuous paths), then one can show that the increments must be multivariate normal random variables. We use this fact in our definition.

**Definition** The $d$-dimensional process
$$ B_t = \left( B_t^1, \ldots, B_t^d \right), $$
is called a *d-dimensional Brownian motion starting at the origin with drift* $\mathbf{m} = (m_1, \ldots, m_d) \in \mathbb{R}^d$ *and $d \times d$ covariance matrix* $\Gamma$ *with respect to the filtration* $\{\mathcal{F}_t\}$ if each $B_t$ is $\mathcal{F}_t$-measurable and the following holds.

- $B_0 = 0$.

- If $s < t$, the distribution of $B_t - B_s$ is joint normal with mean $(t - s)\mathbf{m}$ and covariance matrix $(t - s)\Gamma$.

- If $s < t$, the random vector $B_t - B_s$ is independent of $\mathcal{F}_s$.

- With probability one, the function $t \mapsto B_t$ is continuous.

In particular, each $B_t^k$ is a Brownian motion with drift $m_k$ and variance $\Gamma_{kk}$ with respect to the filtration $\{\mathcal{F}_t\}$. If $\mathbf{m} = 0$ and $\Gamma = I$, then $B_t^1, \ldots, B_t^d$ are independent standard Brownian motions and $B_t$ is called *standard d-dimensional Brownian motion*.

**Definition** If $X_t, Y_t$ are processes defined on the same probability space, the *covariation (process)* is defined by
$$ \langle X, Y \rangle_t = \lim_{n \to \infty} \sum_{j \leq tn} \left[ X\left(\frac{j}{n}\right) - X\left(\frac{j-1}{n}\right) \right] \left[ Y\left(\frac{j}{n}\right) - Y\left(\frac{j-1}{n}\right) \right], $$
where the sum is over all $j$ with $j/n \leq t$.

If $X = Y$, then the covariation is the same as the quadratic variation, that is
$$ \langle X, X \rangle_t = \langle X \rangle_t. $$

### PDF page 74 (book page 68)

If $B_t = (B_t^1, \ldots, B_t^d)$ is a Brownian motion with drift 0 and covariance matrix $\Gamma$, then
$$ \mathbb{E}\left[ (B_t^i - B_s^i)(B_t^k - B_s^k) \right] = (t - s)\,\Gamma_{ik}. $$
As in the quadratic variation, the drift does not contribute to the covariation. We state the following result which is proved in the same way as for quadratic variation.

**Theorem 2.9.1.** *If $B_t$ is a d-dimensional Brownian motion with drift* $\mathbf{m}$ *and covariance matrix* $\Gamma$*, then*
$$ \langle B^i, B^k \rangle_t = \Gamma_{ik}\, t. $$

In particular, if $B_t = (B_t^1, \ldots, B_t^d)$ is a standard Brownian motion in $\mathbb{R}^d$, then the components are independent and
$$ \langle B^i, B^k \rangle_t = 0, \quad i \neq k. $$

## 2.10 Heat equation and generator

Even if one's interest in Brownian motion comes from other applications, it is useful to consider the diffusion of heat. Heat flow can be viewed by considering a large number of independent "heat particles" each doing random continuous motion. This viewpoint leads to a deterministic partial differential equation (PDE) that describes the evolution of the temperature. Imagine for the moment that the temperature on the line is determined by the density of heat particles. Let $p_t(x)$ denote the temperature at $x$ at time $t$. If the heat particles are moving independently and randomly then we can assume that they are doing Brownian motions. If we also assume that
$$ \int_R p_t(x)\, dx = 1, $$
then reasonable to see $p_t(x)$ as the probability density for Brownian motion.

### 2.10.1 One dimension

We start by taking advantage of what we already know. Assume $B_t$ is a standard Brownian motion starting at the origin and let $p_t(x)$ denote the

### PDF page 75 (book page 69)

density of $B_t$. Since $B_t \sim N(0, t)$, we know that
$$ p_t(x) = \frac{1}{\sqrt{2\pi t}}\, e^{-\frac{x^2}{2t}}. \tag{2.6} $$

We view this as a function of two variables $t, x$. If we are interested in the position at time $s + t$, we can use the Markovian nature of Brownian motion to first observe the position at time $s$ and then to consider what happens in the next time interval of length $t$. This leads to the *Chapman-Kolmogorov equation*
$$ p_{s+t}(x) = \int_{-\infty}^{\infty} p_s(y)\, p_t(x - y)\, dy. \tag{2.7} $$

A straightforward calculation, which we omit, shows that if $p_t(x)$ is given by (2.6), then $p_t(x)$ satisfies (2.7). We emphasize that (2.7) uses the Markovian property: if we are interested in the position at time $t + s$ and are given the information up to time $s$, the only information that is relevant is the position at time $s$.

We will give a heuristic derivation of the PDE that describes the evolution of $p_t(x)$. For a number of our heuristic derivations we will use a *binomial approximation* where we view the Brownian motion as satisfying
$$ \mathbb{P}\left\{ B_{t+\Delta t} = B_t + \Delta x \right\} = \mathbb{P}\left\{ B_{t+\Delta t} = B_t - \Delta x \right\} = \frac{1}{2}, $$
where $\Delta x = \sqrt{\Delta t}$. In the approximation, to be at $x$ at time $t + \Delta t$ one must be at $x \pm \Delta x$ at time $t$ which gives
$$ p_{t+\Delta t}(x) \approx \frac{1}{2}\, p_t(x - \Delta x) + \frac{1}{2}\, p_t(x + \Delta x). $$

Using $\Delta t = (\Delta x)^2$, this implies
$$ \frac{p_{t+\Delta t}(x) - p_t(x)}{\Delta t} = \frac{p_t(x + \Delta x) + p_t(x - \Delta x) - 2\, p_t(x)}{2\,(\Delta x)^2}. \tag{2.8} $$

We now let $\Delta t \to 0$ in (2.8). The definition of the partial derivative implies that
$$ \lim_{\Delta t \to 0} \frac{p_{t+\Delta t}(x) - p_t(x)}{\Delta t} = \partial_t p_t(x). $$

### PDF page 76 (book page 70)

The right-hand side of (2.8) is a little more complicated. Since such limits are fundamental in our study, let us give two ways to compute the limit. One way is to write the right-hand side as

$$ \frac{1}{2\Delta x} \left[ \frac{p_t(x + \Delta x) - p_t(x)}{\Delta x} - \frac{p_t(x) - p_t(x - \Delta x)}{\Delta x} \right]. $$

Waving our hands, we say this is about

$$ \frac{1}{2} \frac{\partial_x p_t(x) - \partial_x p_t(x - \Delta x)}{\Delta x}, $$

and now we have a difference quotient for the first derivatives in which case the limit should be

$$ \frac{1}{2}\, \partial_{xx} p_t(x). $$

Another, essentially equivalent, method to evaluate the limit is to write $f(x) = p_t(x)$ and expand in a Taylor series about $x$,

$$ f(x + \epsilon) = f(x) + f'(x)\, \epsilon + \frac{1}{2}\, f''(x)\, \epsilon^2 + o(\epsilon^2), $$

where $o(\epsilon^2)$ denotes a term such that

$$ \lim_{\epsilon \to 0} \frac{o(\epsilon^2)}{\epsilon^2} = 0. $$

Then we see that

$$ f(x + \epsilon) + f(x - \epsilon) - 2f(x) = f''(x)\, \epsilon^2 + o(\epsilon^2), $$

and hence the limit of the right-hand side of (2.8) is $\partial_{xx} p_t(x)/2$. We have derived the *heat equation*

$$ \partial_t p_t(x) = \frac{1}{2}\, \partial_{xx}\, p_t(x). $$

While we have been a bit sketchy on details, one could start with this equation and note that $p_t$ as defined in (2.6) satisfies this. This is the solution given that $B_0 = 0$, that is, when the "initial density" $p_0(x)$ is the "delta function at 0". (The delta function, written $\delta(\cdot)$ is the probability density of the probability

### PDF page 77 (book page 71)

distribution that gives measure one to the point 0. This is not really a density, but informally we write

$$ \delta(0) = \infty, \qquad \delta(x) = 0, \;\; x \neq 0, $$

$$ \int \delta(x)\, dx = 1. $$

These last equations do not make mathematical sense, but they give a workable heuristic definition.)

If the Brownian motion has variance $\sigma^2$, one binomial approximation is

$$ \mathbb{P}\left\{ B_{t+\Delta t} = B_t + \sigma\, \Delta x \right\} = \mathbb{P}\left\{ B_{t+\Delta t} = B_t - \sigma\, \Delta x \right\} = \frac{1}{2}, $$

where $\Delta x = \sqrt{\Delta t}$. The factor $\sigma$ is put in so that

$$ \mathrm{Var}\left[ B(t + \Delta t) - B(t) \right] = \sigma^2\, \Delta t. $$

We can use the same argument to derive that this density should satisfy the heat equation

$$ \partial_t p_t(x) = \frac{\sigma^2}{2}\, \partial_{xx} p_t(x). $$

The coefficient $\sigma^2$ (or in some texts $(\sigma^2/2)$) is referred to as the *diffusion coefficient*. One can check that a solution to this equation is given by

$$ p_t(x) = \frac{1}{\sqrt{2\pi\sigma^2 t}}\, \exp\left\{ -\frac{x^2}{2\sigma^2 t} \right\}. $$

When the Brownian motion has drift $m$, the equation gets another term. To see what the term should look like, let us first consider the case of deterministic linear motion, that is, motion with drift $m$ but no variance. Then if $p_t(x)$ denotes the density at $x$ at time $t$, we get the relationship

$$ p_{t+\Delta t}(x) = p_t(x - m\, \Delta t), $$

since particles at $x$ at time $t + \Delta t$ must have been at $x - m\Delta t$ at time $t$. This gives

$$ \begin{aligned} \frac{p_{t+\Delta t}(x) - p_t(x)}{\Delta t} &= \frac{p_t(x - m\, \Delta t) - p_t(x)}{\Delta t} \\ &= -m\, \frac{p_t(x) - p_t(x - m\, \Delta t)}{m\Delta t}. \end{aligned} $$

### PDF page 78 (book page 72)

Letting $\Delta t \to 0$, we get the equation for linear motion at rate $m$,

$$ \partial_t p_t(x) = -m\, \partial_x p_t(x). $$

This is a first-order equation which means it contains only first derivatives.

If $B_t$ is Brownian motion with drift $m$ and variance $\sigma^2$, then we can do a similar argument and show that the density $p_t(x)$ satisfies the second order PDE

$$ \partial_t p_t(x) = -m\, \partial_x p_t(x) + \frac{\sigma^2}{2}\, \partial_{xx} p_t(x). $$

As a check, one can consider the appropriate density,

$$ p_t(x) = \frac{1}{\sqrt{2\pi\sigma^2 t}}\, \exp\left\{ -\frac{(x - mt)^2}{2\sigma^2 t} \right\}, $$

and show that it satisfies this equation.

Before summarizing, we will change the notation slightly. Let $p_t(x, y)$ denote the density of $B_t$ given $B_0 = x$. Under this notation $p_t(x) = p_t(0, x)$. We will define an operator on functions. A *(linear) operator* is a function $L$ from (a linear subspace of) functions to functions satisfying $L(af + bg) = aL(f) + bL(g)$ where $a, b$ are constants and $f, g$ are functions. We say that a function $f : \mathbb{R} \to \mathbb{R}$ is $C^2$ if it is twice differentiable and the derivatives are continuous functions of $x$. For any $m, \sigma^2$, we define an operator on $C^2$ functions by

$$ L^* f(x) = -m\, f'(x) + \frac{\sigma^2}{2}\, f''(x). $$

If $f$ is a function of more variables, such as $f_t(x, y)$ we write $L_x^*$ to indicate the operator acting on the variable $x$,

$$ L_x^* f_t(x, y) = -m\, \partial_x f_t(x, y) + \frac{\sigma^2}{2}\, \partial_{xx} f_t(x, y). $$

**Theorem 2.10.1.** *Suppose $B_t$ is a Brownian motion with drift $m$ and variance $\sigma^2$. Then the transition density $p_t(x, y)$ satisfies the heat equation*

$$ \partial_t p_t(x, y) = L_y^* p_t(x, y) $$

*with initial condition $p_0(x, \cdot) = \delta_x(\cdot)$. Here $L^*$ is the operator on functions*

$$ L^* f(y) = -m\, f'(y) + \frac{\sigma^2}{2}\, f''(y). $$

### PDF page 79 (book page 73)

We think of $p_t(x, y)$ as "the probability of being at $y$ at time $t$ given that $B_0 = x$". For driftless Brownian motion, this is the same as the probability of being at $x$ given that one was at $y$. However, the reversal of a Brownian motion with drift $m$ should be a Brownian motion with drift $-m$. This gives the following.

**Theorem 2.10.2.** *Suppose $B_t$ is a Brownian motion with drift $m$ and variance $\sigma^2$. Then the transition density $p_t(x, y)$ satisfies the heat equation*

$$ \partial_t p_t(x, y) = L_x p_t(x, y) $$

*with initial condition $p_0(\cdot, y) = \delta_y(\cdot)$. Here $L$ is the operator on functions*

$$ Lf(x) = m\, f'(x) + \frac{\sigma^2}{2}\, f''(x). $$

The operator $L$ will be more important to us than the operator $L^*$ which is why we give it the simpler notation.

---

Let $H$ denote the real Hilbert space $L^2(\mathbb{R})$ with inner product

$$ (f, g) = \int_{-\infty}^{\infty} f(x)\, g(x)\, dx. $$

The operators $L, L^*$ are not defined on all of $H$ but they can be defined on a dense subspace, for example, the set of $C^2$ functions all of whose derivatives decay rapidly at infinity. The operator $L^*$ is the *adjoint* of $L$ which means,

$$ (L^*f, g) = (f, Lg). $$

One can verify this using the following relations that are obtained by integration by parts:

$$ \int_{-\infty}^{\infty} f(x)\, g'(x)\, dx = -\int_{-\infty}^{\infty} f'(x)\, g(x)\, dx, $$

$$ \int_{-\infty}^{\infty} f(x)\, g''(x)\, dx = \int_{-\infty}^{\infty} f''(x)\, g(x)\, dx. $$

Suppose $B_0$ has an initial density $f$. Then the density of $B_t$ is given by

$$ f_t(y) = P_t^* f(y) := \int_{-\infty}^{\infty} f(x)\, p_t(x, y)\, dx. $$

### PDF page 80 (book page 74)

This is the solution to the equation

$$ \partial_t f_t(y) = L_y^* f_t(y) $$

with initial condition $f_0(y) = f(y)$. We can write the heat equation as a derivative for operators,

$$ \partial_t P_t^* = L^* P_t^*. $$

---

**2.10.2 Expected value at a future time**

Suppose $B_t$ is a Brownian motion with drift $m$ and variance $\sigma^2$, and let $f$ be a function on $\mathbb{R}$. For example, if we consider $B_t$ to be the price of a stock and $f$ to be the worth of a call option at strike price $S$ at time $t$, then

$$ f(x) = (x - S)_+ = \left\{ \begin{array}{ll} x - S & \text{if } x \geq S \\ 0 & \text{if } x < S \end{array} \right. . \tag{2.9} $$

Let $\phi(t, x)$ be the expected value of $f(B_t)$ given that $B_0 = x$. We will write this as

$$ \phi(t, x) = \mathbb{E}^x\left[f(B_t)\right] = \mathbb{E}\left[f(B_t) \mid B_0 = x\right]. $$

Then

$$ \phi(t, x) = \int_{-\infty}^{\infty} f(y)\, p_t(x, y)\, dy. $$

The time derivative can be computed by interchanging differentiation and integration and using the rule from the previous section.

$$
\begin{aligned}
\partial_t \phi(t, x) &= \partial_t \int_{-\infty}^{\infty} f(y)\, p_t(x, y)\, dy \\
&= \int_{-\infty}^{\infty} f(y)\, \partial_t p_t(x, y)\, dy \\
&= \int_{-\infty}^{\infty} f(y)\, L_x p_t(x, y)\, dy \\
&= L_x \int_{-\infty}^{\infty} f(y)\, p_t(x, y)\, dy = L_x \phi(t, x).
\end{aligned}
$$

### PDF page 81 (book page 75)

We will give another derivation of this equation, and while we are at it we will do the multivariate case. Suppose $B_t = (B_t^1, \ldots, B_t^d)$ is a $d$-dimensional Brownian motion with drift $m = (m_1, \ldots, m_d)$ and covariance matrix $\Gamma$. We assume that the Brownian motion is truly $d$-dimensional, or, in other words, that $\Gamma$ is a nonsingular matrix. Let $p_t(x, y)$ be the transition probability. If $f : \mathbb{R}^d \to \mathbb{R}$ is a bounded function, define $P_t f$ by

$$ P_t f(x) = \mathbb{E}^x\left[f(B_t)\right] = \int f(y)\, p_t(x, y)\, dy. $$

Here $x = (x_1, \ldots, x_d), y = (y_1, \ldots, y_d) \in \mathbb{R}^d$ and $dy = dy_1 \cdots dy_d$.

**Definition** The *(infinitesimal) generator* of a Markov process $X_t$ is the operator $L$ on functions defined by

$$ Lf(x) = \lim_{t \to 0} \frac{P_t f(x) - f(x)}{t}, $$

where

$$ P_t f(x) = \mathbb{E}^x\left[f(X_t)\right]. $$

**Theorem 2.10.3.** *If $B_t$ is a $d$-dimensional Brownian motion with drift $m = (m_1, \ldots, m_d)$ and covariance matrix $\Gamma$, then the infinitesimal generator is given by*

$$ Lf(x) = m \cdot \nabla f(x) + \frac{1}{2} \sum_{j=1}^{d} \sum_{k=1}^{d} \Gamma_{jk}\, \partial_{jk} f(x). $$

*In particular, if $f$ is a function and*

$$ \phi(t, x) = P_t f(x) = \mathbb{E}^x[f(B_t)], $$

*then $\phi$ satisfies*

$$ \partial_t \phi(t, x) = L_x \phi(t, x), \quad t > 0, $$

*with initial condition $\phi(0, x) = f(x)$.*

We will give a quick derivation, assuming $f$ is $C^2$ and $t = x = 0$. The second-order Taylor approximation of $f$ around the origin is

$$ f(\epsilon) = f(0) + \sum_{j=1}^{d} b_j\, \epsilon_j + \frac{1}{2} \sum_{j=1}^{d} \sum_{k=1}^{d} a_{jk}\, \epsilon_j\, \epsilon_k + o(|\epsilon|^2), $$

### PDF page 82 (book page 76)

where $\epsilon = (\epsilon_1, \dots, \epsilon_d)$ and

$$ b_j = \partial_j f(0), \quad a_{jk} = \partial_{jk} f(0). $$

In particular,

$$ f(B_t) - f(B_0) = \sum_{j=1}^{d} b_j\, B_t^j + \frac{1}{2} \sum_{j=1}^{d} \sum_{k=1}^{d} a_{jk}\, B_t^j\, B_t^k + o(|B_t|^2). $$

We know that

$$ \mathbb{E}\left[B_t^j\right] = m_j\, t, \quad \mathbb{E}\left(B_t^j\, B_t^k\right) = \Gamma_{jk}\, t, $$

and the expectation of the "error" term $o(|B_t|^2)$ is $o(t)$. Hence,

$$ \frac{d}{dt} \mathbb{E}\left[f(B_t)\right]\big|_{t=0+} = \lim_{t \downarrow 0} \frac{\mathbb{E}[f(B_t) - f(B_0)]}{t} = Lf(0). $$

---

Suppose $f$ is a measurable function that does not grow too fast at infinity. For example, we assume that

$$ e^{-\alpha |x|^2}\, f(x) \to 0, \quad |x| \to \infty, $$

for every $\alpha > 0$. Then

$$ \int_{-\infty}^{\infty} |f(y)|\, p_t(x, y)\, dy < \infty, $$

and hence

$$ \phi(t, x) := P_t f(x) = \int_{-\infty}^{\infty} f(y)\, p_t(x, y)\, dy < \infty $$

is well defined for all $t$. Moreover, for $t > 0$, the interchange of integration

$$ \partial_t \int_{-\infty}^{\infty} f(y)\, p_t(x, y)\, dy = \int_{-\infty}^{\infty} f(y)\, \partial_t p_t(x, y)\, dy $$

can be justified (say by the dominated convergence theorem). Similarly, integrals with respect to $x$ can be taken to show that $\phi(t, \cdot)$ is $C^\infty$ in $x$ and

$$ L_x \phi(t, x) = \int_{-\infty}^{\infty} f(y)\, L_x p_t(x, y)\, dy $$

### PDF page 83 (book page 77)

Therefore, for $t > 0$, $x \mapsto \phi(t, x)$ is $C^2$ and we can take the right derivative with respect to time,

$$ \lim_{s \downarrow 0} \frac{\phi(t + s, x) - \phi(t, x)}{s} = L_x \phi(t, x), $$

using the argument as above. Although this argument only computes the right derivative, since for fixed $x$, $\phi(t, x)$ and $L_x \phi(t, x)$ are continuous functions of $t$, we can conclude that

$$ \partial_t \phi(t, x) = L_x \phi(t, x), \quad t > 0. $$

We cannot expect this to hold at $t = 0$, but we can state that if $f$ is continuous at $x$, then

$$ \lim_{t \downarrow 0} \phi(t, x) = f(x). $$

---

A simple call option works a little differently. Suppose that $B_t$ is a one-dimensional Brownian motion with parameters $m, \sigma^2$. A simple call option at time $T > 0$ with strike price $S$ allows the owner to buy a share of the stock at time $T$ for price $S$. If the price at time $T$ is $B_T$, then the value of the option is $f(B_T) = (B_T - S)_+$ as in (2.9). We are specifying the value of the function at time $T$ rather than at time $0$. However, we can use our work to give a PDE for the expected value of the option. If $t < T$, then the expected value of this option, given that $B_t = x$ is

$$ F(t, x) = \mathbb{E}\left[F(B_T) \mid B_t = x\right] = \mathbb{E}^x\left[F(B_{T-t})\right] = \phi(T - t, x). $$

Since

$$ \partial_t F(t, x) = -\partial_t \phi(T - t, x) = -L_x \phi(T - t, x) = -L_x F(t, x), $$

we get the following.

- If $f$ is a function, $T > 0$ and

$$ F(t, x) = \mathbb{E}[f(B_T) \mid B_t = x], $$

then for $t < T$, $F$ satisfies the *backwards heat equation*

$$ \partial_t F(t, x) = -L_x F(t, x), $$

with terminal condition $F(T, x) = f(x)$.

### PDF page 84 (book page 78)

As in the one-dimensional case, we can find the operator associated to the transition density. If we run a Brownian motion with drift $m$ and covariance matrix $\Gamma$ backwards, we get the same covariance matrix but the drift becomes $-m$. Therefore

- For $t > 0$, the transition probability $p_t(x, y)$ satisfies the equation

$$ \partial_t p_t(x, y) = L_y^* p_t(x, y), $$

  where

$$ L^* f(y) = -m \cdot \nabla f(y) + \frac{1}{2} \sum_{j=1}^{d} \sum_{k=1}^{d} \Gamma_{jk}\, \partial_{jk} f(y). $$

The equations

$$ \partial_t p_t(x, y) = L_x p_t(x, y), \quad \partial_t p_t(x, y) = L_y^* p_t(x, y) $$

are sometimes called the *Kolmogorov backwards* and *forwards equations*, respectively. The name comes from the fact that they can be derived from the Chapman-Kolmogorov equations by writing

$$ p_{t+\Delta t}(x, y) = \int p_{\Delta t}(x, z)\, p_t(z, y)\, dz, $$

$$ p_{t+\Delta t}(x, y) = \int p_t(x, z)\, p_{\Delta t}(z, y)\, dz, $$

respectively. The forward equation is also known as the *Fokker-Planck equation*. We will make more use of the backwards equation.

## 2.11 Exercises

**Exercise 2.1.** Let $Z_1, Z_2, Z_3$ be independent $N(0, 1)$ random variables. Let

$$ X_1 = Z_1 + Z_3, \quad X_2 = Z_2 + 4Z_3, \quad X_3 = 2Z_1 - 2Z_2 + rZ_3 $$

where $r$ is a real number.

1. Explain why $\mathbf{X} = (X_1, X_2, X_3)$ has a joint normal distribution.

2. Find the covariance matrix for $\mathbf{X}$ (in terms of $r$).

### PDF page 85 (book page 79)

3. For what values of $r$ are $X_1$ and $X_3$ independent random variables?

4. For what values of $r$ does the random vector $X$ have a density in $\mathbb{R}^3$?

**Exercise 2.2.** Let $B_t$ be a standard Brownian motion. Find the following probabilities. If you cannot give the answer precisely give it up to at least three decimal places using a table of the normal distribution.

1. $\mathbb{P}\{B_3 \geq 1/2\}$

2. $\mathbb{P}\{B_1 \leq 1/2, B_3 > B_1 + 2\}$

3. $\mathbb{P}(E)$ where $E$ is the event that the path stays below the line $y = 6$ up to time $t = 10$.

4. $\mathbb{P}\{B_4 \leq 0 \mid B_2 \geq 0\}$.

**Exercise 2.3.** Let $B_t$ be a standard Brownian motion. For each positive integer $n$, let

$$ J_n = \sum_{j=1}^{n} \left[ B\left(\frac{j}{n}\right) - B\left(\frac{j-1}{n}\right) \right]^2 . $$

1. Find the mean and variance of the random variable $J_n$.

2. Prove the following "weak law of large numbers": if $\epsilon > 0$, then

$$ \lim_{n \to \infty} \mathbb{P}\left\{ |J_n - 1| > \epsilon \right\} = 0. $$

Hint: this uses Chebyshev's inequality — look it up if this is not familiar to you.

In the next exercise, you can use the following computation. If $X \sim N(0, 1)$, then the moment generating function of $X$ is given by

$$ m(t) = \mathbb{E}\left[ e^{tX} \right] = e^{t^2/2}. $$

**Exercise 2.4.** Suppose $B_t$ is a standard Brownian motion and let $\mathcal{F}_t$ be its corresponding filtration. Let

$$ M_t = e^{\sigma B_t - \frac{\sigma^2 t}{2}}. $$

Show that $M_t$ is a martingale with respect to $\mathcal{F}_t$. In other words, show that if $s < t$, then

$$ E(M_t \mid \mathcal{F}_s) = M_s. $$

### PDF page 86 (book page 80)

**Exercise 2.5.** Let $B_t$ be a standard Brownian motion and let

$$ Y = \max\left\{ B_1^2 + (B_2 - B_1)^2, \ B_2^2 \right\} . $$

- Show that

$$ Y = B_2^2 + 2 B_1 (B_1 - B_2) \, 1\{B_1(B_1 - B_2) \geq 0\}. $$

- Find $\mathbb{E}[Y]$.

- Show that for every $k < \infty$, $\mathbb{E}\left[ Y^k \right] < \infty$.

**Exercise 2.6.** Let $B_t$ be a standard Brownian motion and let $\{\mathcal{F}_t\}$ denote the usual filtration. Suppose $s < t$. Compute the following.

1. $E[B_t^2 \mid \mathcal{F}_s]$

2. $E[B_t^3 \mid \mathcal{F}_s]$

3. $E[B_t^4 \mid \mathcal{F}_s]$

4. $E[e^{4B_t - 2} \mid \mathcal{F}_s]$

**Exercise 2.7.** Let $B_t$ be a standard Brownian motion and let

$$ Y(t) = t \, B(1/t). $$

1. Is $Y(t)$ a Gaussian process?

2. Compute $\mathrm{Cov}(Y(s), Y(t))$.

3. Does $Y(t)$ have the distribution of a standard Brownian motion?

**Exercise 2.8.** If $f(t), 0 \leq t \leq 1$ is a continuous function, define the $(3/2)$-variation up to time one to be

$$ Q = \lim_{n \to \infty} \sum_{j=1}^{n} \left| f\left(\frac{j}{n}\right) - f\left(\frac{j-1}{n}\right) \right|^{3/2} . $$

What is $Q$ if

1. $f$ is a nonconstant, continuously differentiable function on $\mathbb{R}$?

### PDF page 87 (book page 81)

2. $f$ is a Brownian motion?

**Exercise 2.9.** Suppose $B_t$ is a standard Brownian motion. For the functions $\phi(t, x), 0 < t < 1, -\infty < x < \infty$, defined below, give a PDE satisfied by the function.

1. $\phi(t, x) = \mathbb{P}\{B_t \geq 0 \mid B_0 = x\}$.

2. $\phi(t, x) = \mathbb{E}[B_1^2 \mid B_t = x]$.

3. Repeat the two examples above if $B_t$ is a Brownian motion with drift $m$ and variance $\sigma^2$.

**Exercise 2.10.** Suppose $B_t$ is a standard Brownian motion and

$$ M_t = \max_{0 \leq s \leq t} B_s. $$

1. Explain why $M_t$ has the same distribution as $\sqrt{t} \, M_1$.

2. Find the density of $M_1$.

3. Find $\mathbb{E}[M_t]$.

4. If $a > 0$, find $\mathbb{E}[M_1 \, 1\{M_1 \geq a\}]$.

5. Let $\mathcal{F}_t$ be the information in $\{B_s : 0 \leq s \leq t\}$. Find $E[M_2 \mid \mathcal{F}_1]$.

**Exercise 2.11.** Write a program that will simulate a standard Brownian motion using step size $\Delta t = .01$.

1. Graph at least one realization of the Brownian motion to produce a "pretty picture" of a Brownian path.

2. Use simulations to estimate the following probability:

$$ \mathbb{P}\{B_t \leq 2 \text{ for all } t \leq 1\}. $$

Run the simulation enough times to get a good estimate for the probability. Use the reflection principle to calculate the actual probability and compare the result.

**Exercise 2.12.** Prove Theorem 2.6.3.

### PDF page 88 (book page 82)
*(Blank page.)*

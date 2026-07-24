# Chapter 6 — Jump processes
*(PDF pages 191–242; book pages 185–236)*

### PDF page 191 (book page 185)

# Chapter 6

# Jump processes

**6.1 Lévy processes**

The assumptions that led to Brownian motion were:

- Independent increments

- Stationary increments

- Continuous paths.

If we want to consider more general processes, we need to give up at least one of these assumptions. In this chapter we will not assume continuity of paths.

**Definition** A stochastic process $X_t$ is called a *Lévy process* if it has independent, stationary increments. That is to say, for every $s, t > 0$, the random variable $X_{s+t} - X_s$ is independent of $\{X_r : r \leq s\}$ and has the same distribution as $X_t - X_0$.

Brownian motion is the only Lévy process with continuous paths. We have already discussed one example of a Lévy process with discontinuous paths, the Poisson process, and we will describe it in more detail in Section 6.2. Let us give two examples that can be derived from Brownian motion.

**Example 6.1.1.** Suppose $B_t$ is a standard Brownian motion and $T_s = \inf\{t : B_t = s\}$. Using the strong Markov property, we can see that $T_s, s \geq 0$ has i.i.d. increments. Therefore it is a Lévy process. Note that it is increasing,

### PDF page 192 (book page 186)

that is, with probability one if $r < s$, then $T_r < T_s$. We calculated the density of $T_s$ in Example 2.7.1,

$$ f_s(t) = \frac{s}{t^{3/2} \sqrt{2\pi}} \, e^{-\frac{s^2}{2t}}, \quad 0 < t < \infty. $$

In particular, the distribution of $T_s$ is not normal. We claim that (with probability one) the function $s \mapsto T_s$ is not continuous. To see this, let $M = \max_{0 \leq t \leq 1} B_t$ and let $s_0 \in (0, 1)$ be a time $t$ with $B_t = M$. Then by definition of $M, T_s$ we see that $T_M \leq s_0$, but $T_s > 1$ for $s > M$, showing that $T$ is not continuous at $s_0$. The scaling property of Brownian motion implies that $T_s$ has the same distribution as $s^2 T_1$. A tricky calculation which we omit computes the characteristic function

$$ \mathbb{E}[e^{i(r/s^2) T_s}] = \mathbb{E}[e^{irT_1}] = \int_{-\infty}^{\infty} e^{irt} f_1(t) \, dt = e^{\Psi(r)}, $$

where

$$ \Psi(r) = \left\{ \begin{array}{ll} |2r|^{1/2}(1 - i) & \text{if } r \geq 0 \\ |2r|^{1/2}(1 + i) & \text{if } r \leq 0 \end{array} \right. . $$

**Example 6.1.2.** Let $B_t = (B_t^1, B_t^2)$ be a standard two-dimensional Brownian motion. Let

$$ T_s = \inf\{t : B_t^1 = s\}, $$

and

$$ X_s = B^2(T_s). $$

Using the strong Markov property, one can show that the increments are i.i.d. and similarly to Example 6.1.1 that the paths as discontinuous. The scaling property of Brownian motion implies that $X_s$ has the same distribution as $s X_1$. The density of $X_1$ turns out to be Cauchy,

$$ f(x) = \frac{1}{\pi (x^2 + 1)}, \quad -\infty < x < \infty, $$

with characteristic function

$$ \mathbb{E}\left[ e^{irX_t} \right] = \int_{-\infty}^{\infty} e^{irx} f(x) \, dx = e^{-|r|}. $$

### PDF page 193 (book page 187)

Not every distribution can arise as the distribution of the increments of a Lévy process. Indeed, suppose that $X_t$ is a Lévy process. Then we can write

$$ X_1 = \sum_{j=1}^{n} Y_{j,n}, \quad \text{where } Y_{j,n} = X\left(\frac{j}{n}\right) - X\left(\frac{j-1}{n}\right). $$

**Definition** A random variable $X$ has an *infinitely divisible distribution* if for each $n$ we can find independent, identically distributed random variables $Y_{1,n}, \ldots, Y_{n,n}$ such that $X$ has the same distribution as

$$ Y_{1,n} + \cdots + Y_{n,n}. $$

We just noted that if $X_t$ is a Lévy process, then $X_1$ (and, in fact, $X_t$ for each $t$) has an infinitely divisible distribution. The converse is true and it not too difficult to show. If $F$ is the distribution function of an infinitely divisible distribution, then there is a Lévy process $X_t$ such that $X_1$ has distribution $F$. Normal and Poisson random variables are infinitely divisible:

- If $X \sim N(m, \sigma^2)$, then $X$ has the same distribution as the sum of $n$ independent $N(m/n, \sigma^2/n)$ random variables.

- If $X$ has a Poisson distribution with mean $\lambda$, then $X$ has the same distribution as the sum of $n$ independent Poisson random variables with mean $\lambda/n$.

The goal of the next few sections is to show that every infinitely divisible random variable is the sum of a normal random variable and a "generalized Poisson" or "jump" random variable. The category "generalized Poisson" is rather large and will include the distributions in Examples 6.1.1 and 6.1.2.

---

A precise definition of a Lévy process needs another condition. For Brownian motion, we put continuity of the paths into the assumptions. To construct Brownian motion, we first defined Brownian motion on dyadic rationals times, showed that the corresponding process was uniformly continuous, and then extended to other times by continuity. In the case of Lévy processes, we similarly can first define the process at dyadic times to satisfy independent, stationary increments. As we discuss later, we then prove that with probability one, for all times $t$, the limits

$$ X_{t-} = \lim_{q \uparrow t} X_q, \quad X_{t+} = \lim_{q \downarrow t} X_q, $$

### PDF page 194 (book page 188)

exist where the limits are taken over the dyadic rationals. We then define $X_t$ to be $X_{t+}$.

---

## 6.2 Poisson process

The Poisson process is the basic jump Lévy process. It is obtained by taking jumps of size one at a particular rate $\lambda$. Suppose we have such a process, and let $p(s)$ denote the probability that there is at least one jump in the interval $[t, t + s]$. If the increments are to be stationary, this quantity must not depend on $t$. Rate $\lambda$ means that the probability that there is a jump some time during the time interval $[t, t + \Delta t]$ is about $\lambda \Delta t$; more precisely,

$$ p(\Delta t) = \lambda \, \Delta t + o(\Delta t), \quad \Delta t \downarrow 0. $$

We can use this observation to construct the Poisson process.

We consider the *waiting times* between jumps. Let $X_t$ denote the number of jumps that have occurred by time $t$ and let

$$ T = \inf\{t : X_t = 1\} $$

denote the amount of time until the first jump. Using i.i.d. increments, we see that

$$
\begin{aligned}
\mathbb{P}\{T > t\} \;\; &= \;\; \prod_{j=1}^{n} \mathbb{P}\left\{\text{no jump during } \left[\frac{(j-1)t}{n}, \frac{jt}{n}\right]\right\} \\
&= \;\; \left[1 - p\left(\frac{t}{n}\right)\right]^n.
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\mathbb{P}\{T > t\} \;\; &= \;\; \lim_{n \to \infty} \left[1 - p\left(\frac{t}{n}\right)\right]^n \\
&= \;\; \lim_{n \to \infty} \left[1 - \frac{\lambda t}{n} + o\left(\frac{\lambda t}{n}\right)\right]^n = e^{-\lambda t}.
\end{aligned}
$$

Recall that a random variable $T$ has an *exponential distribution* with rate $\lambda$ if it has density

$$ f(t) = \lambda \, e^{-\lambda t}, \quad 0 < t < \infty, $$

### PDF page 195 (book page 189)

and hence

$$ \mathbb{P}\{T > t\} = \int_t^\infty f(s) \, ds = e^{-\lambda t}. $$

Our assumptions imply that the waiting times of a Poisson distribution with parameter $\lambda$ must be exponential with rate $\lambda$. Note that

$$ \mathbb{E}[T] = \int_0^\infty t \, f(t) \, dt = \frac{1}{\lambda}, $$

so that the mean waiting time is (quite reasonably) the reciprocal of the rate. This observation gives a way to construct a Poisson process. This construction also gives a good way to simulate Poisson processes (see Exercise 6.1).

- Let $T_1, T_2, T_3, \ldots$ be independent random variables each exponential with rate $\lambda$.

- Let $\tau_0 = 0$ and for positive integer $n$,

$$ \tau_n = T_1 + \cdots + T_n. $$

In other words, $\tau_n$ is the time at which the $n$th jump occurs.

- Set

$$ X_t = n \quad \text{for} \quad \tau_n \leq t < \tau_{n+1}. $$

Note that we have defined the process so that the paths are right-continuous,

$$ X_t = X_{t+} := \lim_{s \downarrow t} X_s. $$

The paths also have limits from the left, that is, for every $t$ the limit

$$ X_{t-} = \lim_{s \uparrow t} X_s $$

exists. If $t$ is a time that the process jumps, that is, if $t = \tau_n$ for some $n > 0$, then

$$ X_t = X_{t+} = X_{t-} + 1. $$

At all other times the path is continuous, $X_{t-} = X_{t+}$.

The i.i.d. increments follow from the construction. We can use the assumptions to show the following.

### PDF page 196 (book page 190)

- The random variable $X_{t+s} - X_s$ has a Poisson distribution with mean $\lambda t$, that is,

$$ \mathbb{P}\{X_{t+s} - X_s = k\} = e^{-\lambda t}\,\frac{(\lambda t)^k}{k!}. $$

One way to derive this is to write a system of differential equations for the functions

$$ q_k(t) = \mathbb{P}\{X_t = k\}. $$

In the small time interval $[t, t + \Delta t]$, the chance that there is more than one jump is $o(\Delta t)$ and the chance there is exactly one jump is $\lambda \Delta t + o(\Delta t)$. Therefore, up to errors that are $o(\Delta t)$,

$$ \mathbb{P}\{X_{t+\Delta t} = k\} = \mathbb{P}\{X_t = k - 1\}\,(\lambda \Delta t) + \mathbb{P}\{X_t = k\}\,[1 - \lambda\,\Delta t]. $$

This gives

$$ q_k(t + \Delta t) - q_k(t) = \lambda\,\Delta t\,[q_{k-1}(t) - q_k(t)] + o(\Delta t), $$

or

$$ \frac{dq_k(t)}{dt} = \lambda\,[q_{k-1}(t) - q_k(t)]. $$

If we assume $X_0 = 0$, we also have the initial conditions $q_0(0) = 1$ and $q_k(0) = 0$ for $k > 0$. We can solve this system of equations recursively, and this yields the solutions

$$ q_k(t) = e^{-\lambda t}\,\frac{(\lambda t)^k}{k!}. $$

(Although it takes some good guesswork to start with the equations and find $q_k(t)$, it is easy to verify that $q_k(t)$ as given above satisfies the equations.)

When studying infinitely divisible distributions, it will be useful to consider characteristic functions, and for notational ease, we will take logarithms. Since the characteristic function is complex-valued, we take a little care in defining the logarithm.

**Definition** If $X$ is a random variable, then its *characteristic exponent* $\Psi(s) = \Psi_X(s)$ is defined to be the continuous function satisfying

$$ \mathbb{E}[e^{isX}] = e^{\Psi(s)}, \quad \Psi(0) = 0. $$

If $X_t$ is a Lévy process, then the characteristic exponent of the process is the characteristic exponent of $X_1 - X_0$.

### PDF page 197 (book page 191)

Note that if $X, Y$ are independent, then

$$ \Psi_{X+Y} = \Psi_X + \Psi_Y. \tag{6.1} $$

- If $X \sim N(m, \sigma^2)$, then

$$ \Psi(s) = ims - \frac{\sigma^2}{2}\,s^2. $$

- If $X$ is Poisson with mean $\lambda$, then

$$ \Psi(s) = \lambda\,[e^{is} - 1]. $$

This can be seen from the computation

$$ \mathbb{E}[e^{isX}] = \sum_{n=0}^{\infty} e^{isn}\,\mathbb{P}\{X = n\} = \sum_{n=0}^{\infty} \frac{(\lambda e^{is})^n}{n!}\,e^{-\lambda} = e^{\lambda e^{is}}\,e^{-\lambda}. $$

If $X_t$ is a Lévy process starting at the origin with characteristic exponent $\Psi$, then i.i.d. increments and the relation (6.1), imply that

$$ \Psi_{X_t} = t\,\Psi_{X_1} = t\,\Psi. $$

An important property of Lévy processes is the following.

- Suppose $X_t^1, X_t^2$ are independent Lévy processes with $\Psi_{X^1} = \Psi_1, \Psi_{X^2} = \Psi_2$. Then $X_t = X_t^1 + X_t^2$ is a Lévy process with $\Psi_{X_t} = \Psi_1 + \Psi_2$.

For example if $X_t^1$ is a Brownian motion with drift $m$ and variance $\sigma^2$ and $X_t^2$ is an independent Poisson process with rate $\lambda$, then $X_t = X_t^1 + X_t^2$ is a Lévy process with

$$ \Psi(s) = ims - \frac{\sigma^2\,s^2}{2} + \lambda\,[e^{is} - 1]. \tag{6.2} $$

A Lévy process is a Markov process so we can talk about its generator,

$$ Lf(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}[f(X_t) \mid X_0 = x] - f(x)}{t}. $$

Recall that for a Brownian motion $B_t$ with drift $m$ and variance $\sigma^2$,

$$ Lf(x) = m\,f'(x) + \frac{\sigma^2}{2}\,f''(x). $$

### PDF page 198 (book page 192)

Moreover, if

$$ f(t, x) = \mathbb{E}\left[F(B_t) \mid B_0 = x\right], $$

then $f$ satisfies the heat equation

$$ \partial_t f(t, x) = L_x f(t, x). \tag{6.3} $$

We now compute the generator for the Poisson process. Although we think of the Poisson process as taking integer values, there is no problem extending the definition so that $X_0 = x$. In this case the values taken by the process are $x, x + 1, x + 2, \ldots$ Up to terms that are $o(t)$, $\mathbb{P}\{X_t = X_0 + 1\} = 1 - \mathbb{P}\{X_t = X_0\} = \lambda\,t$. Therefore as $t \downarrow 0$,

$$ \mathbb{E}[f(X_t) \mid X_0 = x] = \lambda\,t\,f(x + 1) + [1 - \lambda\,t]\,f(x) + o(t), $$

and

$$ Lf(x) = \lambda\,[f(x + 1) - f(x)]. $$

The same argument shows that if $f(t, x)$ is defined by

$$ f(t, x) = \mathbb{E}\left[F(X_t) \mid X_0 = x\right], $$

then $f$ satisfies the heat equation (6.3) with the generator $L$. We can view the generator as the operator on functions $f$ that makes (6.3) hold.

The generators satisfy the following linearity property: if $X_t^1, X_t^2$ are independent Lévy processes with generators $L_1, L_2$, respectively, then $X_t = X_t^1 + X_t^2$ has generator $L_1 + L_2$. For example, if $X$ is the Lévy process with $\Psi$ as in (6.2),

$$ Lf(x) = m\,f'(x) + \frac{\sigma^2}{2}\,f''(x) + \lambda\,[f(x + 1) - f(x)]. $$

## 6.3 Compound Poisson process

In the Poisson process, the process jumps from $x$ to $x + 1$ at rate $\lambda$. The compound Poisson process generalizes this by allowing the jump size to be random. For the moment we think of the process as having two parameters, a jump rate $\lambda$ and a distribution function $F$. We construct the process as follows.

- Let $T_1, T_2, T_3, \ldots$ be independent random variables each exponential with rate $\lambda$.

### PDF page 199 (book page 193)

- Let $N_t$ denote the corresponding Poisson process as in the previous section,

$$ N_t = n \quad \text{if} \quad T_1 + \cdots + T_n \le t < T_1 + \cdots + T_{n+1}. $$

- Let $Y_1, Y_2, Y_3, \ldots$ be independent random variables, independent of $T_1, T_2, \ldots$, with distribution function $F$, and let

$$ S_n = Y_1 + \cdots + Y_n, \quad S_0 = 0. $$

- Set $X_t = S_{N_t}$.

We call the process $X_t$ a *compound Poisson process (CPP)* starting at the origin.

Let $\mu^{\#}$ denote the distribution of the random variables $Y_j$, that is, if $V \subset \mathbb{R}$, then $\mu^{\#}(V) = \mathbb{P}\{Y_1 \in V\}$. We set

$$ \mu = \lambda\, \mu^{\#} $$

which is a measure on $\mathbb{R}$ with $\mu(\mathbb{R}) = \lambda$. For the usual Poisson process $\mu^{\#}, \mu$ are just "point masses" on the point 1,

$$ \mu^{\#}(\{1\}) = 1, \quad \mu(\{1\}) = \lambda, \quad \mu^{\#}(\mathbb{R} \setminus \{1\}) = \mu(\mathbb{R} \setminus \{1\}) = 0. $$

The measure $\mu$ encodes both $\lambda$ and $\mu^{\#}$ so we can consider $\mu$ as the parameter for the compound Poisson process. For any measure $\mu$ with $\lambda = \mu(\mathbb{R}) < \infty$ there is such a process. The measure $\mu$ is called the *Lévy measure* for the process. Without loss of generality we assume that $\mu(\{0\}) = 0$ since "jumps of size zero" do not affect the process $X_t$. The construction shows that the increments of $X_t$ are i.i.d., and hence $X_t$ is a Lévy process.

**Proposition 6.3.1.** *Suppose $X_t$ is a CPP with Lévy measure $\mu$ with $X_0 = 0$. Then*

$$ \Psi(s) = \int_{-\infty}^{\infty} [e^{isx} - 1]\, d\mu(x), $$

$$ Lf(x) = \int_{-\infty}^{\infty} [f(x + y) - f(x)]\, d\mu(y). \tag{6.4} $$

*Moreover, if*

$$ \sigma^2 := \int x^2\, d\mu(x) < \infty, \tag{6.5} $$

### PDF page 200 (book page 194)

*and*

$$ m = \int x\, d\mu(x), $$

*then $M_t = X_t - tm$ is a square integrable martingale with $\mathrm{Var}[M_t] = t\sigma^2$.*

*Proof.* Let

$$ \phi(s) = \mathbb{E}[e^{isY_j}] = \int_{-\infty}^{\infty} e^{isx}\, d\mu^{\#}(x), $$

denote the characteristic function of a random variable with distribution function $F$. Then,

$$ \mathbb{E}[e^{isX_t}] = \sum_{n=0}^{\infty} \mathbb{P}\{N_t = n\}\, \mathbb{E}[e^{isX_t} \mid N_t = n]. $$

Conditioned on $N_t = n$, the distribution of $X_t$ is that of $Y_1 + \cdots + Y_n$, and hence

$$ \mathbb{E}[e^{isX_t} \mid N_t = n] = \phi(s)^n. $$

Since $N_t$ is Poisson with mean $t\lambda$,

$$
\begin{aligned}
\mathbb{E}[e^{isX_t}] &= \sum_{n=0}^{\infty} e^{-t\lambda}\, \frac{(t\lambda)^n}{n!}\, \phi(s)^n \\
&= e^{-t\lambda} \sum_{n=0}^{\infty} \frac{(t\lambda\phi(s))^n}{n!} \\
&= \exp\{t\lambda\,[\phi(s) - 1]\} \\
&= \exp\left\{ t\lambda \int_{-\infty}^{\infty} [e^{isx} - 1]\, d\mu^{\#}(x) \right\} \\
&= \exp\left\{ t \int_{-\infty}^{\infty} [e^{isx} - 1]\, d\mu(x) \right\}.
\end{aligned}
$$

The second-to-last equality uses the fact that $\mu^{\#}$ is a probability measure.

The computation for the generator $L$ follows from the definition of the CPP. In a small time $\Delta t$, the probability that there is a jump is $\lambda\Delta t + o(\Delta t)$, and given that there is a jump, the amount jumped is given by the distribution $\mu^{\#}$. In other words, the probability that there is a jump in time $\Delta t$ whose size is in $(a, b)$ is given up to an error of size $o(\Delta t)$ by

$$ \lambda\, \Delta t\, \mu^{\#}(a, b) = \Delta t\, \mu(a, b). $$

### PDF page 201 (book page 195)

Therefore,

$$
\begin{aligned}
\mathbb{E}\left[f(X_{\Delta t}) \mid X_0 = x\right] \\
&= [1 - \lambda\Delta t]\, f(x) + \Delta t \int_{-\infty}^{\infty} f(x + y)\, d\mu(y) + o(\Delta t) \\
&= f(x) + \Delta t \int_{-\infty}^{\infty} [f(x + y) - f(x)]\, d\mu(y) + o(\Delta t),
\end{aligned}
$$

which is a restatement of (6.4).

The moments of $X_t$ can be computed by differentiating its characteristic function,

$$ \phi'_{X_t}(0) = i\, \mathbb{E}[X_t], \quad \phi''_{X_t}(0) = -\, \mathbb{E}[X_t^2], $$

assuming that the moments exist. For any positive integer $n$, if

$$ \int_{-\infty}^{\infty} |x|^n\, d\mu(x) < \infty, $$

then we can differentiate under the integral $n$ times to see that

$$ \Psi^{(n)}(s) = i^n \int_{-\infty}^{\infty} x^n\, e^{isx}\, d\mu(x). $$

In particular, if (6.5) holds,

$$ \Psi'(0) = i \int_{-\infty}^{\infty} x\, d\mu(x), \quad \Psi''(0) = - \int_{-\infty}^{\infty} x^2\, d\mu(x), $$

and since $\phi_{X_t}(s) = \exp\{t\Psi(s)\}$ and $\Psi(0) = 0$, we get

$$ \phi'_{X_t}(0) = t\Psi'(0) = it \int_{-\infty}^{\infty} x\, d\mu(x) = itm, $$

$$ \phi''_{X_t}(0) = t\Psi''(0) + [t\Psi'(0)]^2 = -[t\sigma^2 + (tm)^2]. $$

Therefore,

$$ \mathbb{E}[X_t] = tm, \quad \mathrm{Var}[X_t] = \mathbb{E}\left[(X_t - tm)^2\right] = \mathbb{E}\left[X_t^2\right] - (\mathbb{E}[X_t])^2 = t\sigma^2. $$

If $\mathcal{F}_s$ denote the information contained in $\{X_r : r \le s\}$ and $s < t$, then $X_t - X_s$ is independent of $\mathcal{F}_s$ and

$$ E[X_t \mid \mathcal{F}_s] = X_s + E[X_t - X_s \mid \mathcal{F}_s] = X_s + \mathbb{E}[X_t - X_s] = X_s + (t - s)m, $$

### PDF page 202 (book page 196)

and hence

$$ \mathbb{E}[X_t - tm \mid \mathcal{F}_s] = X_s - sm. $$

This shows that $M_t$ is a martingale and

$$ \mathbb{E}[M_t^2] = \mathbb{E}[(X_t - tm)^2] = \text{Var}[X_t] = t\,\sigma^2. $$

$\square$

We call $M_t = X_t - mt$ the *compensated compound Poisson process (compensated CPP)* associated to $X_t$. It is a Lévy process. If $L$ denotes the generator for $X_t$, then $M_t$ has generator

$$
\begin{aligned}
L_M f(x) &= Lf(x) - mf'(x) \\
&= \int_{-\infty}^{\infty} [f(x + y) - f(x) - y\,f'(x)]\,d\mu(y).
\end{aligned}
\tag{6.6}
$$

The quadratic variation of the CPP is defined as before

$$ \langle X \rangle_t = \lim_{n \to \infty} \sum_{j \leq tn} \left[ X\left(\frac{j}{n}\right) - X\left(\frac{j-1}{n}\right) \right]^2. $$

Note that the terms in the sum are zero unless there is a jump in the time interval $[(j-1)/n, j/n]$. Hence we see that

$$ \langle X \rangle_t = \sum_{s \leq t} [X_s - X_{s-}]^2. $$

Unlike the case of Brownian motion, for fixed $t$ the random variable $\langle X \rangle_t$ is not constant. We can similarly find the quadratic variation of the martingale $M_t = X_t - mt$. By expanding the square, we see that this it is the limit as $n \to \infty$ of three sums

$$ \sum_{j \leq tn} \left[ X\left(\frac{j}{n}\right) - X\left(\frac{j-1}{n}\right) \right]^2 $$

$$ + \frac{2m}{n} \sum_{j \leq tn} \left[ X\left(\frac{j}{n}\right) - X\left(\frac{j-1}{n}\right) \right] + \sum_{j \leq tn} \frac{m^2}{n^2}. $$

### PDF page 203 (book page 197)

Since there are only finitely many jumps, we can see that the second and third limits are zero and hence

$$ \langle M \rangle_t = \langle X \rangle_t = \sum_{s \leq t} [X_s - X_{s-}]^2. $$

This next proposition generalizes the last assertion of the previous proposition and sheds light on the meaning of the generator $L$. In some sense, this is an analogue of Itô's formula for CPP. Recall that if $X_t$ is a diffusion satisfying

$$ dX_t = m(X_t)\,dt + \sigma(X_t)\,dB_t, $$

then the Markov process $X_t$ has generator

$$ Lf(x) = m(x)\,f'(x) + \frac{\sigma^2(x)}{2}\,f''(x), $$

and Itô's formula gives

$$ df(X_t) = Lf(X_t)\,dt + f'(X_t)\,\sigma(X_t)\,dB_t. $$

In other words, if

$$ M_t = f(X_t) - \int_0^t Lf(X_s)\,ds, $$

then $M_t$ a (local) martingale satisfying

$$ dM_t = f'(X_t)\,\sigma(X_t)\,dB_t. $$

**Proposition 6.3.2.** *Suppose $X_t$ is a compound Poisson process with Lévy measure $\mu$, and suppose that $f$ is a continuous function such that for all $x, t$,*

$$ \mathbb{E}\left[ f(X_t)^2 \mid X_0 = x \right] < \infty. $$

*Then*

$$ M_t = f(X_t) - \int_0^t Lf(X_s)\,ds $$

*is a square integrable martingale with*

$$ \langle M \rangle_t = \langle f(X) \rangle_t = \sum_{s \leq t} \left[ f(X_s) - f(X_{s-}) \right]^2. $$

### PDF page 204 (book page 198)

The proof of this proposition is similar to the derivation of Itô's formula. We will first show that $M_t$ is a martingale, that is, $E[M_t \mid \mathcal{F}_s] = M_s$. The argument is essentially the same for all $s$ so we will assume that $s = 0$ and $X_0 = x$. We need to show that

$$ \mathbb{E}\left[ f(X_t) - f(X_0) - \int_0^t Lf(X_s)\,ds \right] = 0. $$

This argument is the same for all $t$, so let us assume $t = 1$. Then, as in the proof of Itô's formula, we write

$$ f(X_1) - f(X_0) - \int_0^1 Lf(X_s)\,ds $$

$$ = \sum_{j=1}^{n} \left[ f\left(X_{\frac{j}{n}}\right) - f\left(X_{\frac{(j-1)}{n}}\right) - \int_{(j-1)/n}^{j/n} Lf(X_s)\,ds \right]. $$

We write the expectation of the right-hand side as the sum of two terms

$$ \sum_{j=1}^{n} \mathbb{E}\left[ f\left(X_{\frac{j}{n}}\right) - f\left(X_{\frac{(j-1)}{n}}\right) - \frac{1}{n}\,Lf\left(X_{\frac{(j-1)}{n}}\right) \right] \tag{6.7} $$

$$ \sum_{j=1}^{n} \mathbb{E}\left[ \frac{1}{n}\,Lf\left(X_{\frac{(j-1)}{n}}\right) - \int_{(j-1)/n}^{j/n} Lf(X_s)\,ds \right], \tag{6.8} $$

The definition of $L$ implies that

$$ E\left[ f(X_{t+\Delta t}) \mid \mathcal{F}_t \right] = f(X_t) + Lf(X_t)\,\Delta t + o(\Delta t), $$

and hence

$$ \mathbb{E}\left[ f(X_{t+\Delta t}) - f(X_t) - Lf(X_t)\,\Delta t \right] = o(\Delta t). $$

This shows that the sum in (6.7) has $n$ terms that are $o(1/n)$ and hence the limit is zero. The terms inside the expectation in (6.8) equal zero unless there is a jump between time $(j-1)/n$ and $j/n$. This occurs with probability $O(1/n)$ and in this case the value of the random variable is $O(1/n)$. Hence the expectations are $O(1/n^2)$ and the sum of $n$ of them has limit zero.

The computation of the quadratic variation is essentially the same as in Proposition 6.3.1.

### PDF page 205 (book page 199)

Suppose that $X_t = S_{N_t}$ where $N_t$ is a Poisson process of rate $\lambda$. Let $E_n$ be the event that $N_{t+(1/n)} - N_t \geq 2$ for some $t \leq 1$. We know that $\cap_n E_n$ has probability zero, and hence since $\mathbb{E}[|f(X_1)|] < \infty$,

$$ \lim_{n\to\infty} \mathbb{E}\left[|f(X_1)|\, 1_{E_n}\right] = 0. $$

Therefore,

$$ \mathbb{E}[f(X_1)] = \lim_{n\to\infty} \mathbb{E}[f(X_1) 1_{E_n^c}]. $$

However,

$$ \mathbb{E}\left[[f(X_{t+s}) - f(X_t)]\, 1_{E_n^c}\right] = s\, \mathbb{E}[Lf(X_t)][1 + O(s)]. $$

We therefore get

$$ \mathbb{E}\left[f(X_1) - f(X_0)\right] = \lim_{n\to\infty} \frac{1}{n} \sum_{j=0}^{n-1} \mathbb{E}[Lf(X_{j/n})]. $$

Right-continuity implies that

$$ \lim_{n\to\infty} \frac{1}{n} \sum_{j=0}^{n-1} Lf(X_{j/n}) = \int_0^1 Lf(X_s)\, ds, $$

and the bound $\mathbb{E}[|f(X_1)|] < \infty$ can be used to justify the interchange of limit and expectation.

---

For a CPP the paths $t \mapsto X_t$ are piecewise constant and are discontinuous at the jumps. As for the usual Poisson process, we have defined the path so that is it right-continuous and has left-limits. We call a function *cadlag* (also written *càdlàg*), short for *continue à droite, limite à gauche*, if the paths are right-continuous everywhere and have left-limits. That is, for every $t$, the limits

$$ X_{t+} = \lim_{s\downarrow t} X_s, \qquad X_{t-} = \lim_{s\uparrow t} X_s, $$

exist and $X_t = X_{t+}$. The paths of a CPP are cadlag. We can write

$$ X_t = X_0 + \sum_{0 \leq s \leq t} \left[X_s - X_{s-}\right]. $$

Although as written this sum is over an uncountable number of times $s$, the term $X_s - X_{s-}$ is only nonzero at those $s$ at which the path is discontinuous and this is a finite set.

---

### PDF page 206 (book page 200)

In the next section, we will use the following maximal lemma.

**Lemma 6.3.3.** *If $X_t$ is a CPP satisfying (6.5), $M_t = X_t - tm$, and*

$$ K = \max_{0 \leq t \leq 1} |M_t|, $$

*then*

$$ \mathbb{P}\{|K| \geq a\} \leq \frac{\sigma^2}{a^2}. $$

*Proof.* Let

$$ K_n = \max\{|M_{j/n}| : j = 1, 2, \ldots, n\}. $$

Since $X_t$ has piecewise constant paths, $K = \lim_{n\to\infty} K_n$ and it suffices to show for each $n$ that

$$ \mathbb{P}\{|K_n| \geq a\} \leq \frac{\sigma^2}{a^2}. $$

Fix $n$ and let $Z_j = M_{j/n}, \overline{Z}_n = \max\{|Z_j| : j = 1, \ldots, n\}$. Then $Z_j$ is a discrete-time martingale, and Corollary 1.7.2 gives

$$ \mathbb{P}\{\overline{Z}_n \geq a\} \leq \frac{\mathbb{E}[Z_n^2]}{a^2} = \frac{\mathbb{E}[M_1^2]}{a^2} = \frac{\sigma^2}{a^2}. $$

$\square$

---

## 6.4 Integration with respect to compound Poisson processes

Defining the integral with respect to a compound Poisson process is easy. If $X_t$ is a CPP and $A_t$ is another process, we could let

$$ \int_0^t A_s\, dX_s = \sum_{0 \leq s \leq t} A_s \left[X_s - X_{s-}\right]. \tag{6.9} $$

As noted before, there are only a finite number of nonzero terms in the sum so the sum is well defined. This definition requires no assumptions on the process $A_s$. However, if we want the integral to satisfy some of the properties of the Itô integral, we will need to assume more.

### PDF page 207 (book page 201)

Suppose that $\mathbb{E}[X_1] = m, \mathrm{Var}[X_1] = \sigma^2$, and let $M_t$ be the square integrable martingale $M_t = X_t - mt$. Then if the paths of $A_t$ are Riemann integrable, and the integral

$$ Z_t = \int_0^t A_s\, dM_s = \int_0^t A_s\, dX_s - m \int_0^t A_s\, ds $$

is well defined. Let $\mathcal{F}_t$ denote the information contained in $\{M_s : s \leq t\}$ which is the same as the information contained in $\{X_s : s \leq t\}$. In analogy with the Itô integral, we might hope that if $A_t$ is square integrable, piecewise continuous, and adapted to $\{\mathcal{F}_t\}$, then $Z_t$ would be a martingale. However, this is not always the case as we now show.

**Example 6.4.1.** Suppose $X_t$ is the CPP that takes jumps of rate 1 and when it jumps it chooses $\pm 1$ each with the same probability. In other words, the Lévy measure of $X$ is the probability measure with $\mu(\{1\}) = \mu(\{-1\}) = 1/2$. Then $m = 0, \sigma^2 = 1$, and $A_t = X_t - X_{t-}$ is adapted to $\{\mathcal{F}_t\}$. It is discontinuous only at the jumps of $X_t$ and hence is piecewise continuous. However, if we define the integral as in (6.9), then

$$ \int_0^t A_s\, dX_s = \sum_{0 \leq s \leq t} \left[X_s - X_{s-}\right]^2, $$

which has positive expectation (since it is nonnegative and has a positive probability to be strictly positive).

The problem in our setup is that we allow a betting strategy that sees a jump at time $s$ and immediately changes the bet to take advantage of this. In our frameweork [sic], we will not allow these instantaneous changes by restricting to strategies that are *left*-continuous.

**Proposition 6.4.1.** *Suppose $X_t$ is a CPP with $\sigma^2 < \infty$ and $M_t = X_t - mt$. Suppose that $A_t$ is a process satisfying:*

- *each $A_t$ is measurable with respect to $\{X_s : 0 \leq s \leq t\}$;*

- *with probability one, the paths of $A_t$ are left-continuous, that is, $A_t = A_{t-}$;*

- *for every $t < \infty$,*

$$ \int_0^t \mathbb{E}[A_s^2]\, ds < \infty. $$

### PDF page 208 (book page 202)

*Then*

$$ Z_t = \int_0^t A_s \, dM_s $$

*is a square integrable martingale with*

$$ \mathbb{E}\left[Z_t^2\right] = \sigma^2 \int_0^t \mathbb{E}\left[A_s^2\right] \, ds. \tag{6.10} $$

Rather than assuming that $A_s$ is left-continuous, we can assume that $A_s$ has cadlag paths, but then we change the definition in (6.9) to

$$ \int_0^t A_s \, dX_s = \sum_{0 \leq s \leq t} A_{s-} \left[X_s - X_{s-}\right]. $$

---

*Proof of Proposition 6.4.1.* If $s < t$, then arguing as before,

$$ E[A_s \, (M_t - M_s) \mid \mathcal{F}_s] = A_s \, E[M_t - M_s \mid \mathcal{F}_s] = 0, \tag{6.11} $$

$$
\begin{aligned}
\mathbb{E}[A_s^2 \, (M_t - M_s)^2] &= \mathbb{E}\left[E(A_s^2 \, (M_t - M_s)^2 \mid \mathcal{F}_s)\right] \\
&= \mathbb{E}\left[A_s^2 \, \mathbb{E}[(M_t - M_s)^2]\right] \\
&= \sigma^2 \, (t - s) \, \mathbb{E}[A_s^2].
\end{aligned}
\tag{6.12}
$$

For each $t$, the probability that $M_{t-} \neq M_t = 0$. Therefore, with probability one, for all rational times $t$, $M_t = M_{t-}$. Suppose that $A_s$ is a simple process that changes values only at times in $\{0, 1/n, 2/n, 3/n, \ldots\}$. Then with probability one, for all $t$, if $j/n \leq t < (j+1)/n$,

$$ Z_t = \int_0^t A_s \, dM_s = \sum_{i=0}^{j-1} A\left(\frac{i}{n}\right) \left[M\left(\frac{i+1}{n}\right) - M\left(\frac{i}{n}\right)\right]. $$

This expression uses the fact $M_t = M_{t-}$ for all rational $t$. Using this expression and (6.11) and (6.12) we see that $Z_t$ is a square integrable martingale satisfying (6.10).

We now assume that $A_t$ is adapted, left-continuous, and uniformly bounded, that is, with probability one, $|A_t| \leq C$ for all $t$. Define $A_t^n$ by

$$ A_t^n = A_{j/n} \quad \text{if} \quad \frac{j}{n} < t \leq \frac{j+1}{n}. $$

### PDF page 209 (book page 203)

Left-continuity implies that with probability one for all $t$

$$ A_t = \lim_{n \to \infty} A_t^n, $$

and hence

$$ \int_0^t A_s \, dM_s = \lim_{n \to \infty} \int_0^t A_s^n \, dM_s. $$

Using uniform boundedness, one can interchange limits and expectations to get (6.11) and (6.12).

Finally to remove the boundedness assumption, we let $T_n = \inf\{t : |A_t| = n\}$ and let $A_{t,n} = A_{t \wedge T_n}$. As $n \to \infty$, $A_{t,n} \to A_t$, and we can argue as before. $\square$

---

**Example 6.4.2.** Suppose $X_t$ is a CPP with Lévy measure $\mu$ satisfying

$$ \int_{-\infty}^{\infty} e^{2y} \, d\mu(y) < \infty. $$

Let $f(x) = e^x$ and $S_t = f(X_t) = e^{X_t}$ which we can consider as a simple model of an asset price with jumps. This is an analogue of geometric Brownian motion for jump processes. Note that

$$ f(x + y) - f(x) = e^x \, h(y) \quad \text{where} \quad h(y) = e^y - 1, $$

and hence

$$ Lf(x) = \int_{-\infty}^{\infty} [f(x + y) - f(x)] \, d\mu(y) = r e^x, $$

where

$$ r = \int_{-\infty}^{\infty} h(y) \, d\mu(y) < \infty. $$

Note that

$$ S_t - S_{t-} = S_{t-} \, h(X_t - X_{t-}). \tag{6.13} $$

In particular, the jump times for $S$ are the same as the jump times for $X$. Let

$$ \hat{X}_t = \sum_{s \leq t} h(X_t - X_{t-}) $$

### PDF page 210 (book page 204)

be the CPP with $\hat{X}_0 = 0$ that takes a jump of size $h(y)$ whenever $X_t$ takes a jump of size $y$. This process has Lévy measure $\hat{\mu}$ where

$$ \hat{\mu}(h(V)) = \mu(V), \tag{6.14} $$

with mean $\hat{m} = r$. If $\hat{Y}_t = \hat{X}_t - r \, t$ is the compensated CPP, we can write (6.13) as

$$ dS_t = S_{t-} \, d\hat{X}_t = S_{t-} \, d\hat{Y}_t + r \, S_{t-} \, dt = S_{t-} \left[d\hat{Y}_t + r \, dt\right]. $$

Since $S_t$ is piecewise continuous, it does not matter in the $dt$ integral whether we write $S_t$ or $S_{t-}$. However, we must write $S_{t-}$ in the $d\hat{X}_t$ and $d\hat{Y}_t$ integrals.

If $r = 0$, that is, if

$$ \int_{-\infty}^{\infty} [e^y - 1] \, d\mu(y) = 0, $$

then $\hat{X}_t$ and hence $S_t$ are actually martingales. If $r \neq 0$, we let $\tilde{S}_t = e^{-rt} S_t = e^{X_t - rt}$. Since $t \mapsto e^{-rt}$ is differentiable, we can use the product rule

$$ d\tilde{S}_t = S_t \, d[e^{-rt}] + e^{-rt} \, dS_t = \tilde{S}_{t-} \, d\hat{Y}_t. $$

**Example 6.4.3.** We will proceed backwards through the last example to solve the exponential differential equation for compound Poisson processes. Suppose $\hat{X}_t$ is a CPP whose Lévy measure $\hat{\mu}$ satisfies $\hat{\mu}\{x : x \leq -1\} = 0$ and

$$ \int_{-1}^{\infty} x^2 \, d\hat{\mu}(x) < \infty. $$

Let

$$ \hat{m} = \int_{-1}^{\infty} x \, d\hat{\mu}(x) < \infty, $$

and let $\hat{Y}_t = \hat{X}_t - \hat{m} \, t$ be the compensated CPP which is a square integrable martingale. Let $\mu$ be the measure as defined in (6.14) and let $X_t$ denote the corresponding process as in the previous example. In other words, if $\hat{X}_t$ has a jump of size $y$, then $X_t$ has a jump of size $h^{-1}(y) = \log[1 + y]$. Then the solutions to the exponential differential equation

$$ dZ_t = Z_{t-} \, d\hat{X}_t, \quad dM_t = M_{t-} \, d\hat{Y}_t, $$

are

$$ Z_t = Z_0 \, e^{X_t}, \quad M_t = Z_0 \, e^{X_t - \hat{m}t}. $$

### PDF page 211 (book page 205)

Note that we can write

$$ Z_t = Z_0 \, \exp\left\{ \sum_{0<s\leq t} \log[1 + (\hat{X}_s - \hat{X}_{s-})] \right\}. $$

**Example 6.4.4.** More generally, the equations

$$ dZ_t = A_{t-}\, Z_{t-}\, dX_t, \qquad dM_t = A_{t-}\, M_{t-}\, dY_t $$

where $X$ is a CPP with compensated process $Y_t = X_t - mt$, have solutions

$$ Z_t = Z_0 \, \exp\left\{ \sum_{0<s\leq t} \log[1 + A_{s-}\,(X_s - X_{s-})] \right\}, $$

$$ M_t = Z_t \, \exp\left\{ -m \int_0^t A_{s-}\, ds \right\} = Z_t \, \exp\left\{ -m \int_0^t A_s\, ds \right\}. $$

## 6.5 Change of measure

Suppose $X_t$ is a CPP defined on the probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with Lévy measure $\mu$ and corresponding filtration $\{\mathcal{F}_t\}$. We would like to do the analogue of the Girsanov theorem to change the measure.

Suppose that strictly positive martingale $M_t$ is a strictly positive martingale with respect to $\{\mathcal{F}_t\}$ with $M_0 = 1$. As before, we can define a new probability measure $Q$ by saying that if $V$ is $\mathcal{F}_t$-measurable, then

$$ Q[V] = \mathbb{E}\left[M_t \, 1_V\right]. $$

If we let $\mathbb{P}_t, Q_t$ denote $\mathbb{P}, Q$ restricted to $\mathcal{F}_t$, then $\mathbb{P}_t$ and $Q_t$ are mutually absolutely continuous with

$$ \frac{dQ_t}{d\mathbb{P}_t} = M_t, \qquad \frac{d\mathbb{P}_t}{dQ_t} = \frac{1}{M_t}. $$

If $\nu$ is a another [sic] measure on $\mathbb{R}$, we can ask if we can find a martingale so that under the measure $Q$, $X_t$ is a CPP with Lévy measure $\nu$. A necessary condition for this to hold is that $\mu$ and $\nu$ are mutually absolutely continuous measures on $\mathbb{R}$. Indeed, if $V$ is a subset of $\mathbb{R}$ with $\mu(V) > 0, \nu(V) = 0$, then $X_t$ under $\mathbb{P}$ has positive probability of having $X_s - X_{s-} \in V$ for some $s \leq 1$, while this has zero probability under $Q$.

### PDF page 212 (book page 206)

Maybe a bit surprising is the fact that the converse holds. Suppose $\nu, \mu$ are mutually absolutely continuous and let $f = d\nu/d\mu$ which we assume is strictly positive. With respect to $\mathbb{P}$, $X_t$ satisfies

$$ \mathbb{P}\{X_{t+\Delta t} - X_t \in V\} = \mu(V)\, \Delta t + o(\Delta t), $$

and we would like

$$ Q\{X_{t+\Delta t} - X_t \in V\} = \nu(V)\, \Delta t + o(\Delta t), $$

which would give

$$ \frac{Q\{X_{t+\Delta t} - X_t \in V\}}{\mathbb{P}\{X_{t+\Delta t} - X_t \in V\}} = \frac{\nu(V)}{\mu(V)} + o(\Delta t). $$

To get this we choose

$$ M_t = \exp\left\{ \sum_{s\leq t} f(X_s - X_{s-}) - rt \right\}, \qquad r = \nu(\mathbb{R}) - \mu(\mathbb{R}). $$

Suppose we model an asset price by $S_t = e^{X_t}$ where $X_t$ is a CPP, and suppose that $\nu$ is any measure equivalent to $\mu$ with

$$ \int_{-\infty}^{\infty} [e^y - 1]\, d\nu(y) = 0. $$

Then $Q$ is equivalent to $\mathbb{P}$, and (see Example 6.4.2) $S$ is a martingale with respect to $Q$. In particular, there are many different measures $Q$ that are equivalent to $\mathbb{P}$ that make $S_t$ a martingale. This is in contrast to the case when $X_t$ is a Brownian motion where such a measure is unique.

## 6.6 Generalized Poisson processes I

The generalized Poisson process is like the CPP except that the jump times form a dense subset of the real line. Suppose that $\mu$ is a measure on $\mathbb{R}$. We want to consider the process $X_t$ that, roughly speaking, satisfies the condition that the probability of a jump whose size lies in $[a, b]$ occurring in time $\Delta t$ is about $\mu[a, b]\, \Delta t$. The CPP assumes that

$$ \mu(\mathbb{R}) = \int_{-\infty}^{\infty} d\mu(x) < \infty, $$

### PDF page 213 (book page 207)

and this implies that there are only a finite number of jumps in a bounded time interval. In this section we allow an infinite number of jumps ($\mu(\mathbb{R}) = \infty$), but require the expected sum of the absolute values of the jumps in an interval to be finite. This translates to the condition

$$ \int_{-\infty}^{\infty} |x|\, d\mu(x) < \infty. \tag{6.15} $$

This implies that

$$ \mu\{x : |x| > \epsilon\} < \infty \qquad \text{for every} \qquad \epsilon > 0, \tag{6.16} $$

but it is possible for $\mu\{x : |x| > 0\}$ to be infinite.

To be more specific, let $\mu_\epsilon$ denote the measure $\mu$ restricted to jumps of absolute value strictly greater than $\epsilon$. For each $\epsilon$, we have a compound process with Lévy measure $\mu_\epsilon$ which can be written as

$$ X_t^\epsilon = \sum_{0\leq s\leq t} (X_s^\epsilon - X_{s-}^\epsilon). $$

Let us write

$$ V_t^\epsilon = \sum_{0\leq s\leq t} \left| X_s^\epsilon - X_{s-}^\epsilon \right|, $$

which is a CPP with measure $\bar{\mu}_\epsilon$ defined by

$$ \bar{\mu}_\epsilon(a, b) = \mu_\epsilon(a, b) + \mu_\epsilon(-b, -a), \quad \epsilon \leq a < b < \infty. $$

In other words $V_t^\epsilon$ has the same jumps as $X_t^\epsilon$ except that they all go in the positive direction. As $\epsilon \downarrow 0$, $V_t^\epsilon$ increases (since we are adding jumps and they are all in the same direction) and using (6.15), we see that

$$ \lim_{\epsilon\downarrow 0} \mathbb{E}\left[V_t^\epsilon\right] = t \int_{-\infty}^{\infty} |x|\, d\mu(x) < \infty. $$

Hence we can define

$$ V_t = \lim_{\epsilon\downarrow 0} V_t^\epsilon $$

and $\mathbb{E}[V_t] < \infty$. Similarly, we can define

$$ X_t = \lim_{\epsilon\downarrow 0} X_t^\epsilon. $$

### PDF page 214 (book page 208)

Since $|X_t^\epsilon| \le V_t$, the dominated convergence theorem is used to justify interchanges of limits.

Let $\mathcal{T}_n$ be the set of times such that the process $X_t^{1/n}$ is discontinuous, and let

$$ \mathcal{T} = \bigcup_{n=1}^{\infty} \mathcal{T}_n. $$

Since each $\mathcal{T}_n$ is finite, the set $\mathcal{T}$ is countable, but if $\mu(\mathbb{R}) = \infty$ , $\mathcal{T}$ will be infinite and, in fact, dense in every interval. Even though there are jumps in every interval, the paths are cadlag, that is, they are right continuous and the limits

$$ X_{t-} = \lim_{s \uparrow t} X_s $$

exist for every $s$.

Calculating as in the previous section we can see the following.

**Proposition 6.6.1.** *Suppose $X_t$ is a generalized Poisson process with Lévy measure $\mu$. Then*

$$ \Psi(s) = \int_{-\infty}^{\infty} [e^{ixs} - 1]\, d\mu(x), $$

$$ \mathbb{E}[X_t] = tm, \quad m = \int_{-\infty}^{\infty} x\, d\mu(x), $$

$$ Lf(x) = \int_{-\infty}^{\infty} [f(x + y) - f(x)]\, d\mu(y), $$

$$ \mathrm{Var}[X_t] = \mathbb{E}[(X_t - mt)^2] = t \int_{-\infty}^{\infty} x^2\, d\mu(x). $$

---

One may worry about the existence of the integrals above. Taylor's theorem implies that

$$ e^{ixs} - 1 = ixs - \frac{x^2 s^2}{2} + O(|xs|^3). $$

Using this and (6.15) we can see that

$$ \int_{|x| \le 1} |e^{ixs} - 1|\, d\mu(x) < \infty. $$

### PDF page 215 (book page 209)

Also,

$$ \int_{|x| > 1} |e^{ixs} - 1|\, d\mu(x) \le 2\, \mu\{x : |x| > 1\} < \infty. $$

For the generator $L$ we assume that $f$ is $C^1$ and hence for $y$ near the origin

$$ f(x + y) - f(x) = O(|y|). $$

Then,

$$ \int_{|x| \le 1} |f(x + y) - f(x)|\, d\mu(y) < \infty. $$

Finiteness of the integral

$$ \int_{|x| > 1} |f(x + y) - f(x)|\, d\mu(y) $$

requires some assumptions on the growth of $f$ at infinity.

---

We can relax the conditions somewhat by requiring (6.16) to hold but replacing (6.15) with the weaker condition

$$ \int_{-1}^{1} |x|\, d\mu(x) < \infty. \tag{6.17} $$

Indeed, if (6.16) and (6.17) hold we can write

$$ \mu = \mu_1 + \mu_2, $$

where $\mu_1$ is $\mu$ restricted to $\{|x| \le 1\}$ and $\mu_2$ is $\mu$ restricted to $\{|x| > 1\}$. To $\mu_1$ we associate the generalized Poisson process $X_t^1$ and to $\mu_2$ we associate an independent CPP, and then set $X_t = X_t^1 + X_t^2$. In this case it is possible that $\mathbb{E}[|X_t|] = \infty$. However, the formulas for $\Psi$ and $L$ are the same as above.

**Example 6.6.1** (Positive Stable Processes)**.** Suppose that $0 < \beta < 1$ and $\mu$ is defined by

$$ d\mu(x) = c\, x^{-(1+\beta)}\, dx, \quad 0 < x < \infty, $$

where $c > 0$. In other words, the probability of a jump of size between $x$ and $x + \Delta x$ in time $\Delta t$, is approximately

$$ c\, x^{-(1+\beta)}\, (\Delta t)\, (\Delta x). $$

### PDF page 216 (book page 210)

Note that

$$ \int_{\epsilon}^{\infty} c\, x^{-(1+\beta)}\, dx = \frac{c}{\beta}\, \epsilon^{-\beta}, $$

$$ \int_{0}^{1} x\, d\mu(x) = c \int_{0}^{1} x^{-\beta}\, dx = \frac{c}{1 - \beta} < \infty, $$

$$ \int_{0}^{\infty} x\, d\mu(x) = c \int_{0}^{\infty} x^{-\beta}\, dx = \infty. $$

Therefore, $\mu$ satisfies (6.16) and (6.17), but not (6.15). The corresponding generalized Poisson process has

$$ \Psi(s) = c \int_{0}^{\infty} [e^{isx} - 1]\, x^{-(1+\beta)}\, dx. $$

With careful integration, this integral can be computed but we omit it. Using the change of variables $y = rx$, we can see that if $r > 0$, then

$$ \Psi(rs) = c \int_{0}^{\infty} [e^{irsx} - 1]\, x^{-(1+\beta)}\, dx = cr^{\beta} \int_{0}^{\infty} [e^{isy} - 1]\, y^{-(1+\beta)}\, dy. $$

This implies that the distribution of $rX_1$ is the same as that of $X_{r^\beta}$. In particular, $X_{1/n}$ has the same distribution as $n^{-1/\beta} X_1$ and hence we can write

$$ X_1 = \frac{Z_1 + \cdots + Z_n}{n^{1/\beta}}, \quad Z_j = n^{1/\beta} [X_{j/n} - X_{(j-1)/n}], $$

where $Z_1, \ldots, Z_n$ are independent with the same distribution as $X_1$. The process $X_t$ is called the *positive stable process* with exponent $\beta$.

**Example 6.6.2** (Gamma process)**.** Suppose $\lambda > 0$ and $\mu$ is defined by

$$ d\mu(x) = \frac{e^{-\lambda x}}{x}\, dx, \quad 0 < x < \infty. $$

Note that

$$ \int_{0}^{\infty} d\mu(x) = \infty, \quad \int_{0}^{\infty} x\, d\mu(x) < \infty. $$

Using a table of integrals, we can see that the characteristic exponent is

$$ \Psi(s) = \int_{0}^{\infty} [e^{isx} - 1]\, d\mu(x) = \int_{0}^{\infty} \frac{e^{(is-\lambda)x} - e^{-\lambda x}}{x}\, dx = \log \frac{\lambda}{\lambda - is}. $$

### PDF page 217 (book page 211)

In other words, the characteristic function of $X_t$ is $\phi_{X_t}(s) = [\lambda/(\lambda-is)]^t$. This is the characteristic function of a Gamma random variable with parameters $\lambda$ and $t$, that is, the density of $X_t$ is

$$ f_t(x) = \frac{\lambda}{\Gamma(t)}\,(\lambda x)^{t-1}\,e^{-\lambda x}, \quad 0 < x < 1, $$

where

$$ \Gamma(t) = \int_0^\infty x^{t-1}\,e^{-x}\,dx, $$

is the Gamma function. Important values of $t$ are the following.

- $X_1$ has the distribution of an exponential random variable with rate $\lambda$.

- If $n$ is a positive integer, then $X_n$ has the distribution of the sum of $n$ independent random variables each exponential with rate $\lambda$. If $N_s$ is a Poisson process with rate $\lambda$ with $N_0 = 0$, then $X_n$ has the same distribution as $\inf\{s : N_s = n\}$.

- If $\lambda = 1/2$ and $n$ is a positive integer, then $X_{n/2}$ has a $\chi^2$ distribution with $n$ degrees of freedom, that is, it has the same distribution as

$$ Z_1^2 + \cdots + Z_n^2, $$

  where $Z_1, \ldots, Z_n$ are independent, standard normal random variables.

The process $X_t$ is called the *Gamma process with parameter $\lambda$*.

## 6.7 Generalized Poisson processes II

In the previous section, we assumed that the expected sum of the absolute values of the jump was finite. There are jump Lévy processes that do not satisfy this condition. These processes have many "small" jumps. Although the absolute values of the jumps are not summable, there is enough cancellation between the positive jumps and negative jumps to give a nontrivial process.

We will construct such a process associated to a Lévy measure $\mu$ satisying the following assumptions.

- For every $\epsilon > 0$, the number of jumps of absolute value greater than $\epsilon$ in a finite time interval is finite. More precisely, if $\mu_\epsilon$ denotes $\mu$ restricted to $\{|x| > \epsilon\}$, then

$$ \mu_\epsilon(\mathbb{R}) = \mu\left\{x : |x| > \epsilon\right\} < \infty \quad \text{for every} \quad \epsilon > 0. \tag{6.18} $$

### PDF page 218 (book page 212)

- All jumps are bounded in absolute value by 1, that is,

$$ \mu\{x : |x| > 1\} = 0. \tag{6.19} $$

- The second moment of the measure is finite,

$$ \sigma^2 := \int_{-\infty}^\infty x^2\,d\mu(x) < \infty. \tag{6.20} $$

Note that (6.20) can hold even if (6.15) does not hold.

Let

$$ m_\epsilon = \int_{-\infty}^\infty x\,d\mu_\epsilon(x) = \int_{\epsilon < |x| \leq 1} x\,d\mu(x), $$

which is finite and well defined for all $\epsilon > 0$ by (6.18)–(6.20). For each $\epsilon > 0$, there is a CPP $X_t^\epsilon$ associated to the measure $\mu_\epsilon$ and a correponding [sic] compensated Poisson process $M_t^\epsilon = X_t^\epsilon - m_\epsilon t$.

**Definition** Suppose $\mu$ is a measure on $\mathbb{R}$ satisfying (6.18)–(6.20). Then the *compensated generalized Poisson process (CGPP) with Lévy measure $\mu$* is given by

$$ Y_t = \lim_{\epsilon \downarrow 0} M_t^\epsilon = \lim_{\epsilon \downarrow 0} [X_t^\epsilon - m_\epsilon t]. \tag{6.21} $$

Two important cases are the following.

- If

$$ \int_{-\infty}^\infty |x|\,d\mu(x) < \infty, $$

  then the (uncompensated) generalized Poisson process

$$ X_t = \lim_{\epsilon \downarrow 0} X_t^\epsilon, $$

  as in the previous section exists. In this case

$$ Y_t = X_t - mt, $$

  where

$$ m = \lim_{\epsilon \downarrow 0} m_\epsilon = \int_{-\infty}^\infty x\,d\mu(x). $$

### PDF page 219 (book page 213)

- If $\mu$ is symmetric about the origin, that is, if for every $0 < a < b$ the rate of jumps with increments in $[a, b]$ is the same as that of jumps in $[-b, -a]$, then $m_\epsilon = 0$ for every $\epsilon$ and

$$ Y_t = \lim_{\epsilon \downarrow 0} X_t^\epsilon. $$

**Proposition 6.7.1.** *If $Y_t$ is a CGPP with Lévy measure $\mu$, then*

$$ \Psi(s) = \int_{-1}^1 [e^{isx} - 1 - isx]\,d\mu(x), $$

$$ Lf(s) = \int_{-\infty}^\infty [f(x + y) - f(x) - yf'(x)]\,d\mu(y). $$

*The latter quantity is defined provided that $f$ is a $C^2$ function. If also $\mathbb{E}[f(Y_t)^2] < \infty$, then*

$$ M_t = f(Y_t) - \int_0^t Lf(Y_s)\,ds $$

*is a square integrable martingale with*

$$ \langle M \rangle_t = \sum_{s \leq t} [f(Y_s) - f(Y_{s-})]^2. $$

*Proof.* Let $X^\epsilon = X_1^\epsilon$ and $M^\epsilon = M_1^\epsilon = X^\epsilon - m_\epsilon$. Let $\Psi^\epsilon = \Psi_{M_\epsilon}$ and note that

$$ \Psi^\epsilon(s) = \Psi_{X_\epsilon}(s) - im_\epsilon s = \int_{|x| > \epsilon} [e^{isx} - 1]d\mu(x) - im_\epsilon s. $$

Since

$$ m_\epsilon = \int_{|x| > \epsilon} x\,d\mu(x), $$

we can write

$$ \Psi^\epsilon(s) = \int_{|x| > \epsilon} [e^{isx} - 1 - isx]\,d\mu(x). $$

Using Taylor series, we see that $|e^{isx} - 1 - isx| = O(s^2x^2)$, and hence (6.20) implies that for each $s$,

$$ \int |e^{isx} - 1 - isx|\,d\mu(x) < \infty. $$

### PDF page 220 (book page 214)

This allows us to use the dominated convergence theorem to conclude that

$$ \lim_{\epsilon\downarrow0} \Psi^\epsilon(s) = \int_{-1}^{1} [e^{isx} - 1 - isx]\, d\mu(x). $$

Since $Y = \lim_{\epsilon\downarrow0} M^\epsilon$, we can conclude that this limit equals $\Psi(s)$.

The second equation is obtained by taking the limit of (6.6). $\square$

A particular case of the proposition is $f(x) = x$ in which we conclude that $Y_t$ is a square integrable martingale with

$$ \langle Y \rangle_t = \sum_{s\leq t} [Y_s - Y_{s-}]^2. $$

The same argument shows that the moment generating function also exists and

$$ \mathbb{E}[e^{sY_t}] = \exp\left\{ t \int_{-1}^{1} [e^{sx} - 1 - sx]\, d\mu(x) \right\}, \quad s \in \mathbb{R}. $$

In particular, $\mathbb{E}[e^{sY_t}] < \infty$ for all $s, t$. (This is in contrast to CCPs for which this expectation could be infinite.)

---

We will establish existence of the limit in (6.21) both in $L^2$ and with probability one. Let us first consider the case $t = 1$. Let

$$ Y^\epsilon = Y^\epsilon_1 = X^\epsilon_1 - m_\epsilon. $$

It suffices to prove the existence of

$$ Y = \lim_{\epsilon\downarrow0} Y^\epsilon. $$

Let $Z_n = Y^{2^{-n}} - Y^{2^{-(n+1)}}$, so that

$$ Y = \sum_{n=0}^{\infty} Z_n. $$

The random variables $Z_n$ are independent, mean zero, and

$$ \sum_{n=0}^{\infty} \mathrm{Var}[Z_n] < \infty. $$

### PDF page 221 (book page 215)

Therefore $\sum Z_n$ converges to a random variable $Y$ in both $L^2$ and with probability one (see Exercise 1.14). If $2^{-n} \leq \epsilon < 2^{-n+1}$, then

$$ \mathbb{E}\left[ (Y^\epsilon - \sum_{k=0}^{n} Z_k)^2 \right] \leq \int_{2^{-n}}^{2^{-n+1}} x^2\, d\mu(x), $$

which goes to zero as $n \to \infty$. Hence

$$ \lim_{\epsilon\downarrow0} \mathbb{E}\left[ |Y^\epsilon - Y|^2 \right] = 0. $$

Convergence with probability one can be deduced from Lemma 6.3.3.

We now define $Y_q$ as in (6.21) for $q \in \mathcal{D}$ as the limit with probability one. For other $t$ we define

$$ Y_{t+} = \lim_{q\downarrow t} Y_q, \qquad Y_{t-} = \lim_{q\uparrow t} Y_q. \tag{6.22} $$

Here we use the shorthand that when $q$ is the index, the limit is taken over $\mathcal{D}$ only. Define the jump time $\mathcal{T}_\epsilon$ to be the set of times $s$ such that $X^\epsilon$ is discontinuous and $\mathcal{T} = \cup_{j=1}^{\infty} \mathcal{T}_{1/j}$. With probability one each $\mathcal{T}_\epsilon$ is finite and hence $\mathcal{T}$ is countable.

**Proposition 6.7.2.** *With probability one, the limits in* (6.22) *exists for all $t$. Moreover, they are equal unless $t \in \mathcal{T}$.*

*Proof.* Let

$$ S^2_\epsilon = \mathbb{E}\left[ (Y - Y_\epsilon)^2 \right] = \int_{|x|\leq\epsilon} x^2\, d\mu(x). $$

Let

$$ M^\epsilon = \sup\left\{ |Y_q - Y^\epsilon_q| : q \in \mathcal{D}, q \leq 1 \right\}. $$

Using Lemma 6.3.3 (first for $Y^\delta_t - Y^\epsilon_t$ and then letting $\delta \downarrow 0$), we can see that

$$ \mathbb{P}\{M \geq a\} \leq \frac{S^2_\epsilon}{a^2}. $$

We can find $\epsilon_n \downarrow 0$ such that

$$ \sum_{n=1}^{\infty} n^2\, S^2_{\epsilon_n} < \infty. $$

### PDF page 222 (book page 216)

Then if $M_n = M^{\epsilon_n}$, by the Borel-Cantelli lemma, with probability one, for all $n$ sufficiently large $M_n \leq 1/n$ and this inequality implies that for all $t$,

$$ \left| \limsup_{q\downarrow t} Y_{q+} - \lim_{q\downarrow t} Y^{\epsilon_n}_{q+} \right| \leq \frac{1}{n}. $$

Similar estimates hold for the liminf and for limits from the left. $\square$

We now define $Y_t$ for all $t$ by $Y_t = Y_{t+}$, and then the paths of $Y_t$ are cadlag.

---

# 6.8 The Lévy-Khinchin characterization

The next theorem tells us that all Lévy processes can be given as independent sums of the processes we have described.

**Theorem 6.8.1.** *Suppose $X_t$ is a Lévy process with $X_0 = 0$. Then $X_t$ can be written as*

$$ X_t = m\, t + \sigma\, B_t + C_t + Y_t, \tag{6.23} $$

*where $m \in \mathbb{R}, \sigma \geq 0$, and $B_t, C_t, Y_t$ are independent of the following types:*

- *$B_t$ is a standard Brownian motion,*

- *$C_t$ is a compound Poisson process with Lévy measure $\mu_C$ satisfying*

$$ \mu_C\{|x| \leq 1\} = 0, $$

$$ \mu_C(\mathbb{R}) = \mu_C\{|x| > 1\} < \infty, $$

- *$Y_t$ is a compensated generalized Poisson process with Lévy measure $\mu_Y$ satisfying*

$$ \mu_Y(\{0\}) = 0, \quad \mu_Y\{|x| > 1\} = 0, $$

$$ \int_{-\infty}^{\infty} x^2\, d\mu_Y(x) < \infty. $$

### PDF page 223 (book page 217)

The process $C_t+Y_t$ is called a *pure jump Lévy process*. We can summarize the theorem by saying that every Lévy process is the independent sum of a Brownian motion (with mean $m$ and variance $\sigma^2$) and a pure jump process (with Lévy measure $\mu = \mu_C + \mu_Y$.)

We have not included the generalized Poisson process in our decomposition (6.23). If $X_t$ is such a process we can write it as

$$ X_t = C_t + \hat{X}_t $$

where $C_t$ denotes the sum of jumps of absolute value greater than one. Then we can write $\hat{X}_t = Y_t + \hat{m}t$ where $Y_t$ is a compensated generalized Poisson process and $\hat{m} = \mathbb{E}[\hat{X}_1]$, which by the assumptions is finite.

The conditions on $\mu_C, \mu_Y$ can be summarized as follows:

$$ \mu(\{0\}) = 0, \qquad \int_{-\infty}^{\infty} [x^2 \wedge 1] \, d\mu(x) < \infty. \tag{6.24} $$

To specify the distribution of a Lévy processes, one needs to give $m \in \mathbb{R}, \sigma > 0$ and a measure $\mu$ satisfying (6.24). We then set $\mu_C$ to be $\mu$ restricted to $\{|x| > 1\}$ and $\mu_Y$ to be $\mu$ restricted to $\{|x| \leq 1\}$. We have already shown that $(m, \sigma, \mu)$ determine a Lévy process. To prove the theorem, therefore, we need to show that any Lévy process can be written like this.

We will not give the entire proof of this theorem, but let us sketch how one derives it. Suppose $X_t$ is a Lévy process. Suppose that the process has jumps. For every $a > 0$, we can write

$$ X_t = \hat{X}_{t,a} + \hat{C}_{t,a}, $$

where $\hat{C}_{t,a}$ denotes the movement by jumps of absolute value greater than $a$ and $\hat{X}_{t,a}$ denotes a Lévy process with all jumps bounded by $a$. For each $a$ one can show that $\hat{C}_{t,a}$ is a CPP independent of $\hat{X}_{t,a}$. We let $a$ go to zero, and after careful analysis we see that

$$ X_t = Z_t + C_{t,1} + Y_t, $$

where $Y_t$ is compensated generalized Poisson process and $Z_t$ is a Lévy process with continuous paths. We then show that $Z_t$ must be a Brownian motion. The following theorem is related and proved similarly.

### PDF page 224 (book page 218)

**Theorem 6.8.2.** *(Lévy-Khinchin) If $X$ has an infinitely divisible distribution, then there exist $m, \sigma, \mu_C, \mu_Y$ satisfying the conditions of Theorem 6.8.1 such that*

$$ \Psi_X(s) = ims - \frac{\sigma^2}{2}\, s^2 + \int_{|x|>1} [e^{isx} - 1] \, d\mu_C(x) $$

$$ + \int_{|x|\leq 1} [e^{isx} - 1 - isx] \, d\mu_Y(x). $$

We show how to prove this theorem and then prove another theorem which is a key step in the proof of Theorem 6.8.1.

Here we will show that if $X$ has an infinitely divisible distribution, then the characteristic function of $X$ can be written as $\phi(s) = e^{\Psi(s)}$ where

$$ \Psi(s) = ims - \frac{\sigma^2 s}{2} + \int [e^{isx} - 1 - isx\mathbf{1}\{|x| \leq 1\}] \, \mu(dx), $$

where $m \in \mathbb{R}, \sigma^2 \geq 0$, and $\mu$ is a measure on $\mathbb{R}$ with $\mu\{0\} = 0$ and

$$ \int \frac{x^2}{1 + x^2} \, \mu(dx) < \infty. $$

We fix $X$ and allow all constants to depend on the distribution of $X$. Let $s_0$ be such that $|\phi(s) - 1| \leq 1/2, \quad s \leq s_0$.

Since $X$ is infinitely divisible we can write

$$ X = Y_{1,n} + \cdots + Y_{n,n}, $$

where $Y_{1,n}, \ldots, Y_{n,n}$ are i.i.d. We write $\mu_n$ for the distribution of $Y_{1.n}$ and $\nu_n = n\mu_n$. We let $\tilde{Y}_{j,n} = Y_{j,n} \mathbf{1}\{|Y_{j,n}| \leq 1\}$ and let

$$ \tilde{m}_n = \mathbb{E}[\tilde{Y}_{j,n}], \qquad \tilde{\sigma}_n^2 = \mathrm{Var}[\tilde{Y}_{j,n}]. $$

Let $\phi_n(s) = e^{\Psi_n(s)}$ denote the characteristic function of $Y_{1,n}$ and note that $\phi(s) = \phi_n(s)^n$. It suffices to find $m, \sigma^2, \mu$ and a subsequence $n_j$ such that for $|s| \leq s_0$,

$$ \lim_{j \to \infty} n_j \, \Psi_{n_j}(s) = ims - \frac{\sigma^2 s}{2} + \int [e^{isx} - 1 - isx\mathbf{1}\{|x| \leq 1\}] \, \mu(dx). \tag{6.25} $$

### PDF page 225 (book page 219)

**Lemma 6.8.3.**

- *For all $\epsilon > 0$, there exists $M_\epsilon < \infty$ such that for all $n$, $\nu_n\{|x| \geq M_\epsilon\} \leq \epsilon$.*
- *For every $y > 0$, there exists $r < \infty$ such that for all $n$, $\nu_n\{|x| \geq y\} \leq r$.*
- 
$$ \sup_n n[\tilde{\mu}_n + \tilde{\sigma}_n^2] < \infty. $$

*Proof.* By symmetry it suffices to estimate $\nu_n\{x \geq r\}$. We first make the easy observation that for every $r < \infty$, for all $n$ sufficiently large $\mu_n(-\infty, 1) \geq r/n$. Indeed, if this were not true, then there exists a subsequence $n_j$ such that with probability at least

$$ \left(1 - \frac{r}{n_j}\right)^{n_j} \sim e^{-r} $$

we would have $Y_{j,n_j} \geq 1$ for $j = 1, \ldots, n_j$ which implies that with positive probability $X = \infty$.

Let $M, r < \infty$ and let $q_n = \min\{r/n, \mu_n[M, \infty)\}$ and for $n > 2/r$ define $\delta_n^{\pm}$ to be the infimum (supremum) of all numbers such that

$$ \mathbb{P}\{Y_{1,n} \geq \delta_n^+\} \leq q_n, \quad \mathbb{P}\{Y_{1,n} \leq \delta_n^-\} \leq q_n. $$

Using this we can find a random variable with the same distribution as $Y_{1,n}$ by the following.

- With probability $1 - 2q_n$ choose from distribution $\rho_1$ and with probability $2q_n$ choose from distribution $\rho_2$.
- Distribution $\rho_2$ satisfies $\rho_2(-\infty, 1] = \frac{1}{2}, \rho_2[M, \infty) = \frac{1}{2}$.

By focusing on the first time that one chooses from $\rho_2$ we see that the conditional distribution on a set of probability $p_n := 1 - (1 - q_n)^n$ has a "spread" of at least $M - 1$. Another way of saying this is that if $x$ is the median of the distribution of the sum of the remaining terms, there is probability at last $p_n/4$ of being less than $x+1$ and probability at last $p_n/4$ of being greater than $x + M$.

If $a > 0$, let $r_n = n\mathbb{P}\{a \leq Y_{1,n}\}$ and assume $r_n \geq 1$. Using the first part we can find $b$ (independent of $n, a$) with $\mathbb{P}\{a \leq Y_{1,n} \leq b\} \geq r_n/(2n)$. If $0 < s < 1/2b$, then

$$ |1 - e^{iys}| \geq c \, y^2 s^2, \quad 0 \leq |y| \leq b. $$

### PDF page 226 (book page 220)

Find $0 \le s \le 1/2b$ such that $|\phi(s)| \ge 1/e$. We have for $n$ sufficiently large

$$ |\phi_n(s)| \le 1 - \frac{cs^2a^2r_n}{2n}. $$

and hence

$$ \liminf_{n\to\infty} 2ncs^2a^2r_n \le 1. $$

Let $Y_n = \sum_j \tilde{Y}_{1,n}$. Using the second part, we see that $\mathbb{P}\{\tilde{Y}_{j,n} = Y_{j,n}, j = 1, \ldots, n\} \ge c$, and hence the $\{Y_n\}$ are tight, that is, for every $\epsilon > 0$, there exists $K_\epsilon$ such that for all $n$, $\mathbb{P}\{|Y_{j,n}| > K_\epsilon\} < \epsilon$. Chebyshev's inequality gives

$$ \mathbb{P}\left\{|Y_n| \le \frac{n|\tilde{m}_n|}{2}\right\} \le \mathbb{P}\left\{|Y_n - n\tilde{m}_n| \ge \frac{n|\tilde{m}_n|}{2}\right\} \le \frac{4n\tilde{\sigma}_n^2}{n^2\tilde{m}_n^2}. $$

If $n\tilde{\sigma}_n^2$ is bounded and $n_j$ is a subsequence with $n_j|\tilde{m}_{n_j}| \to \infty$, then we would have

$$ \limsup_{y\to\infty} \mathbb{P}\left\{|Y_{n_j}| \ge \frac{n_j|\tilde{m}_{n_j}|}{2}\right\} = 1, $$

which contradicts the tightness of $Y_n$. Suppose $n_j\tilde{\sigma}_{n_j}^2 \to \infty$. Then tightness gives that $|\tilde{m}_{n_j}|^2 = o(\tilde{\sigma}_{n_j}^2)$ and hence $\mathbb{E}[|\tilde{Y}_{1,n_j}|^3] \le \mathbb{E}[\tilde{Y}_{1,n_j}^2] \sim \tilde{\sigma}_{n_j}^2$. To be a bit more precise, we would assume that

$$ \frac{Y_n - n\,\tilde{m}_n}{\sqrt{n\tilde{\sigma}_n^2}} $$

would approach a normal distribution. If $n\tilde{\sigma}_n^2 \to \infty$ this would indicate that $Y_n$ is not tight and one can make this precise with the Berry-Esseen theorem (using the upper bound on the thrid [sic] moment). Hence $n\tilde{\sigma}_n^2$ is bounded and hence $n|\tilde{m}_n|$ is bounded.

$\square$

Using the lemma we can find a measure $\mu$ with $\mu\{0\} = 0$ and a subsequence $n_j$ such that for all bounded continuous functions $f$ that vanish in a neighborhood of the origin,

$$ \lim_{j\to\infty} \int f(x)\nu_{n_j}(dx) = \int f(x)\mu(dx). $$

### PDF page 227 (book page 221)

**6.8. THE LÉVY-KHINCHIN CHARACTERIZATION**

By taking a subsubsequence if necessary we can also conclude that there exists $\tilde{m}, \tilde{\sigma}^2$ such that

$$ \lim_{j\to\infty} n_j \tilde{m}_{n_j} = \tilde{m}, \qquad \lim_{j\to\infty} n_j \sigma_{n_j}^2 = \tilde{\sigma}^2. $$

We will assume that $\mu\{-1, 1\} = 0$. If this is not the case, find $b$ with $\mu\{-b, b\} = 0$ and do the proof similarly defining $\tilde{Y}_{1,n} = Y_{1,n}\, 1\{|\tilde{Y}_{1,n}| \le b\}$. We will establish (6.25) with this $\mu$, $m = \tilde{m}$ and

$$ \sigma^2 = \tilde{\sigma}^2 - \int_{|x|\le 1} x^2\, \mu(dx). $$

For the remainder we fix $s$ with $|s| \le s_0$ and allow constants to depend on $s$. We note that

$$ |\phi_n(s) - 1| \le c/n, $$

and hence

$$ \phi(s) = [1 + \phi_n(s) - 1]^n = \exp\{n(\phi_n(s) - 1)\}\, [1 + O(n^{-1})], $$

$$
\begin{aligned}
\Psi(s) + O(n^{-1}) &= n\,[\phi_n(s) - 1] \\
&= \int [e^{isx} - 1]\, \nu_n(dx) \\
&= isn\tilde{m}_n + \int [e^{isx} - 1 - isx1\{|x| \le 1\}]\, \nu_n(dx).
\end{aligned}
$$

$$ \lim_{j\to\infty} \int_{|x|>a} [e^{isx} - 1 - isxg_\epsilon(x)]\, \nu_{n_j}(dx) = \int_{|x|>a} [e^{isx} - 1 - isxg_\epsilon]\, \mu(dx). $$

Using $\mu\{-a, a - 1, 1\} = 0$ (to handle the discontinuity of the integrand at $x = \pm a, \pm 1$), we can see that

$$ \lim_{j\to\infty} \int_{|x|>a} [e^{isx} - 1 - isx1\{|x| \le 1\}]\, \nu_{n_j}(dx) $$

$$ = \int_{|x|>a} [e^{isx} - 1 - isx1\{|x| \le 1\}]\, \mu(dx). $$

Also,

### PDF page 228 (book page 222)

$$
\begin{aligned}
\Bigg| \int_{|x|\le a} &[e^{isx} - 1 - isx1\{|x| \le 1\}]\, \nu_n(dx) + \frac{s^2}{2} \int_{|x|\le a} x^2\, \nu_n(x) \Bigg| \\
&\le c \int_{|x|\le a} |x|^3\nu_n(dx) \\
&\le c\,a \int_{|x|\le a} x^2\nu_n(dx) \\
&\le ca.
\end{aligned}
$$

Also, as $j \to \infty$, again using $\mu\{\pm a, \pm 1\} = 0$,

$$
\begin{aligned}
\int_{|x|\le a} x^2\, \nu_{n_j}(x) &= \int_{|x|\le 1} x^2\, \nu_{n_j}(x) - \int_{a<|x|\le 1} x^2\, \nu_{n_j}(x) \\
&= o(1) + \tilde{\sigma}^2 - \int_{a<|x|\le 1} x^2\mu(dx).
\end{aligned}
$$

By taking $a \to 0$ at an appropriate rate, we see that

$$ \lim_{j\to\infty} \int [e^{isx} - 1 - isx1\{|x| \le 1\}]\, \nu_{n_j}(dx) $$

$$ = -\frac{s^2}{2}\left[\tilde{\sigma}^2 - \int x^2\, 1\{|x| \le 1\}]\, \mu(dx)\right] $$

$$ + \int [e^{isx} - 1 - isx1\{|x| \le 1\}]\, \nu(dx). $$

**Theorem 6.8.4.** *Suppose $X_t$ is a Lévy process with continuous paths. Then $X_t$ is a Brownian motion.*

*Proof.* All we need to show is that $X_1$ has a normal distribution. Let

$$ X_{j,n} = X_{j/n} - X_{(j-1)/n}, $$

$$ M_n = \max\{|X_{j,n}| : j = 1, \ldots, n\}. $$

Continuity of the paths implies that $M_n \to 0$ and hence for every $a > 0$, $\mathbb{P}\{M_n < a\} \to 1$. Independence of the increments implies that

$$
\begin{aligned}
\mathbb{P}\{M_n < a\} &= \left[1 - \mathbb{P}\{|X_{1/n}| \ge a\}\right]^n \\
&\le \exp\left\{-n\mathbb{P}\{|X_{1/n}| \ge a\}\right\}.
\end{aligned}
$$

### PDF page 229 (book page 223)

Therefore, for every $a > 0$,

$$ \lim_{n\to\infty} n\,\mathbb{P}\{|X_{1/n}| \geq a\} = 0. \tag{6.26} $$

This implies that there exists a sequence $a_n \downarrow 0$ with

$$ \lim_{n\to\infty} n\,\mathbb{P}\{X_{1/n} \geq a_n\} = 0. \tag{6.27} $$

We claim that all the moments of $X_1$ are finite. To see this let $J = \max_{0\leq t\leq 1} |X_t|$ and find $k$ such that $\mathbb{P}\{J \geq k\} \leq 1/2$. Then using continuity of the paths, by stopping at the first time $t$ that $|X_t| = nk$, we can see that

$$ \mathbb{P}\{J \geq (n+1)k \mid J \geq nk\} \leq 1/2, $$

and hence

$$ \mathbb{P}\{J \geq nk\} \leq (1/2)^n, $$

from which finiteness of the moments follows. Let $m = \mathbb{E}[X_1]$, $\sigma^2 = \mathrm{Var}[X_1]$, and note that $\mathbb{E}[X_1^2] = m^2 + \sigma^2$. Our goal is to show that $X_1 \sim N(m, \sigma^2)$. Let

$$ \tilde{X}_{j,n} = X_{j,n}\, 1\{|X_{j,n}| \leq a_n\}, \quad Z_n = \sum_{j=1}^{n} \tilde{X}_{j,n}. $$

Let $\phi_n$ denote the characteristic function of $\tilde{X}_{j,n}$ and hence $[\phi_n]^n$ is the characteristic function of $Z_n$. It follows from (6.27) that $Z_n \to X_1$ in distribution, so it suffices to prove that for every $s$

$$ \lim_{n\to\infty} [\phi_n(s)]^n = \exp\left\{ ims - \frac{\sigma^2 s^2}{2} \right\}. $$

Also, it is easy to check that $\mathbb{E}[Z_n] \to m$, $\mathrm{Var}[Z_n] \to \sigma^2$ and hence

$$ \mathbb{E}[\tilde{X}_{1,n}] = \frac{m\,[1 + o(1)]}{n}, \quad \mathbb{E}[\tilde{X}_{1,n}^2] = \left[\frac{m^2}{n^2} + \frac{\sigma^2}{n}\right] (1 + o(1)). $$

Also, since $|\tilde{X}_{1,n}| \leq a_n$,

$$ \mathbb{E}[|\tilde{X}_{1,n}|^3] \leq a_n\, \mathbb{E}[\tilde{X}_{1,n}^2] = a_n \left[\frac{m^2}{n^2} + \frac{\sigma^2}{n}\right] [1 + o(1)]. $$

### PDF page 230 (book page 224)

(This estimate uses (6.27) which in turn uses the fact that the paths are continuous.) Using these estimates, we see that for fixed $s$,

$$ \phi_n(s) = 1 + \frac{ims}{n} - \frac{\sigma^2 s^2}{2n} + o\left(\frac{1}{n}\right), $$

where the $o(\cdot)$ term depend on $s$. This implies that

$$ \begin{aligned} \lim_{n\to\infty} \phi_n(s)^n &= \lim_{n\to\infty} \left[ 1 + \frac{ims}{n} - \frac{\sigma^2 s^2}{2n} + o\left(\frac{1}{n}\right) \right]^n \\ &= \exp\left\{ ims - \frac{\sigma^2 s^2}{2} \right\}. \end{aligned} $$

$\square$

**6.9 Integration with respect to Lévy processes**

Suppose $X_t$ is a Lévy process which by Theorem 6.8.1 we can write as

$$ X_t = m\,t + \sigma\,B_t + C_t + Y_t. $$

We will define the integral

$$ \int_0^t A_s\, X_s $$

by

$$ m \int_0^t A_s\, ds + \sigma \int_0^t A_s\, dB_s + \int_0^t A_s\, dC_s + \int_0^t A_s\, dY_s. $$

The first integral is a Riemann integral, the second is an Itô integral as in Chapter 3, the third integral was defined in Section 6.4, and this leaves us only the fourth integral to define. As we saw in Section (6.4), the third integral does not have the properties we want unless we assume that $A_t$ is left continuous. The same problems exists for the fourth integral so we will restrict to such processes.

Assume that $Y_t$ is a process with Lévy measure $\mu$ satisfying (6.18)–(6.20). Then $Y_t$ is a square integrable martingale with $\mathbb{E}[Y_t] = \sigma^2\, t$ (this is not the same $\sigma$ as in the previous paragraph). This will allow us to define

$$ \int_0^t A_s\, dY_s $$

### PDF page 231 (book page 225)

as an Itô integral as in Chapter 3.

We start with simple processes. Suppose $A_t$ is a simple process as in Section 3.2.2. To be specific, suppose that times $0 \leq t_0 < t_1 < \cdots < t_n < \infty$ are given, and $A_s = A_{t_j}$ t for $t_j \leq s < t_{j+1}$. Then, we define

$$ \int_0^t A_s\, dY_s = \sum_{i=0}^{j-1} A_{t_i}\, [Y_{t_{i+1}} - Y_{t_i}] + A_{t_j}\, [Y_t - Y_{t_j}]. $$

With probability one, the paths of $Y_t$ are continuous at the times $t_1, \ldots, t_n$ so the definition above does not care whether we choose the simple process $A_s$ to be right continuous or left continuous. The following proposition is proved in the same way as Proposition 3.2.1.

**Proposition 6.9.1.** *Suppose $A_t, \hat{A}_t$ are bounded simple processes adapted to the filtration of the process $Y_t$.*

- **Linearity.** *If $a, b$ are constants, then $aA_t + b\hat{A}_t$ is also a simple process and*
$$ \int_0^t (aA_s + b\hat{A}_s)\, dY_s = a \int_0^t A_s\, dY_s + b \int_0^t \hat{A}_s\, dY_s. $$
*Moreover, if $0 < r < t$,*
$$ \int_0^t A_s\, ds = \int_0^r A_s\, dY_s + \int_r^t A_s\, dY_s. $$

- **Martingale property.** *The process*
$$ Z_t = \int_0^t A_s\, dY_s $$
*is a martingale with respect to $\{\mathcal{F}_t\}$.*

- **Variance rule**. *$Z_t$ is square integrable and*
$$ \mathrm{Var}[Z_t] = \sigma^2 \mathbb{E}\left[ Z_t^2 \right] = \int_0^t \mathbb{E}[A_s^2]\, ds. $$

- **Cadlag paths**. *With probability one, the function $t \mapsto Z_t$ is cadlag.*

### PDF page 232 (book page 226)

We now suppose that $A_s$ is an adapted process with left continuous paths. If $\tilde{A}_s$ is an adapted process with cadlag paths, we could take $A_s = \tilde{A}_{s-}$. We approximate $A_s$ by a simple process $A_s^{(n)}$ by choosing

$$ A_s^{(n)} = 2^n \int_{(j-1)2^{-n}}^{j2^{-n}} A_r \, dr \qquad \text{if} \quad \frac{j}{2^n} < r \le \frac{j+1}{2^n}. $$

The integral is defined by

$$ \int_0^t A_s \, dY_s = \lim_{n \to \infty} \int_0^t A_s^{(n)} \, dY_s. $$

---

Let us give be more precise about this definition. Suppose that $A_t$ is a process with left continuous paths with right limits, that is, the left continuous version of a processes with cadlag paths. Assume that exists $K < \infty$ such that with probability one. $|A_t| \le K$ for all $t$. Since with probability one, the paths are left continuous, we know that

$$ \lim_{n \to \infty} A_t^{(n)} = A_t. $$

SInce $|A_t^{(n)}| \le K$, we can used dominated convergence (for Lebesgue measure) to show that with probability one,

$$ \lim_{n \to \infty} \int_0^t |A_s^{(n)} - A_s|^2 \, ds = 0, $$

and dominated convegence for $\mathbb{P}$ to see that

$$ \lim_{n \to \infty} \mathbb{E}\left[ \int_0^t |A_s^{(n)} - A_s|^2 \, ds \right] = \lim_{n \to \infty} \int_0^t \mathbb{E}\left[ |A_s^{(n)} - A_s|^2 \right] ds = 0. $$

As in the case for Brownian motion, we use the proposition to see that for fixed $t$, the sequence of random variables

$$ Z_t^{(n)} := \int_0^t A_s^{(n)} \, dA_s, $$

is a Cauchy sequence in $L^2$ and has a limit $Z_t$ in $L^2$.

We use this method to define the integral at dyadic times $t$, an we define it at other times by

$$ Z_t = \lim_{t_n \downarrow t} Z_{t_n} $$

where $t_n$ are dyadic rationals.

---

### PDF page 233 (book page 227)

## 6.10 Symmetric stable process

An important example of a Lévy process is the symmetric stable process. A random variable $X$ has a symmetric stable distribution with parameter $\alpha \in (0, 2]$ if $\Psi_X(s) = -|cs|^\alpha$ for some $c > 0$. If $\alpha = 2$, this means that $X$ has a normal distribution with mean zero and variance $2c^2$. For $0 < \alpha < 2$ these distributions arise in Lévy processes that we call symmetric $\alpha$-stable processes. The term stable comes from the following property.

**Proposition 6.10.1.** *If $X$ has a symmetric $\alpha$-stable distribution and $X_1, \ldots, X_n$ are independent random variables with the same distribution as $X$, then $X$ has the same distribution as*

$$ Y = \frac{X_1 + \cdots + X_n}{n^{1/\alpha}}. $$

*Proof.* Using properties of characteristic functions, we get

$$ \Psi_Y(s) = \sum_{j=1}^n \Psi_{X_j}(s/n^{1/\alpha}) = n\Psi_X(s/n^{1/\alpha}) = \Psi_X(s). $$

$\square$

**Definition** If $0 < \alpha \le 2$, then a Lévy process $X_t$ is a *symmetric stable process* if

$$ \Psi(s) = -|cs|^\alpha $$

for some $c > 0$.

**Proposition 6.10.2.** *Suppose $0 < \alpha < 2$, $C > 0$ and $X_t$ is a Lévy process with Lévy measure*

$$ d\mu(x) = \frac{C}{|x|^{1+\alpha}} \, dx. \tag{6.28} $$

*Then $X_t$ is a symmetric $\alpha$-stable process with $\Psi(s) = -Cb_\alpha|s|^\alpha$ where*

$$ b_\alpha = 2 \int_0^\infty \frac{1 - \cos y}{y^{1+\alpha}} \, dy < \infty. $$

The condition $0 < \alpha < 2$ is needed to guarantee that $\mu$ as defined in (6.28) satisfies (6.24). Since $1 - \cos(y) = O(y^2)$ as $y \to 0$, we can see that $b_\alpha$ is finite. In fact, it can be calculated

$$ b_\alpha = \frac{\pi}{\Gamma(\alpha + 1) \sin(\alpha\pi/2)}, $$

### PDF page 234 (book page 228)

where $\Gamma$ denotes the Gamma function. The proof of the proposition is a simple computation. We write

$$ \Psi(s) = C \int_{|x|\le 1} [e^{isx} - 1 - isx] \frac{dx}{|x|^{1+\alpha}} + C \int_{|x|>1} [e^{isx} - 1] \frac{dx}{|x|^{1+\alpha}}. $$

Using $e^{isx} = \cos(sx) + i\sin(sx)$ and the fact that $\mu$ is symmetric about the origin, we see that

$$
\begin{aligned}
\Psi(s) &= 2C \int_0^\infty \frac{\cos(sx) - 1}{x^{1+\alpha}} \, dx \\
&= 2C|s|^\alpha \int_0^\infty \frac{\cos(y) - 1}{y^{1+\alpha}} \, dy = -Cb_\alpha|s|^\alpha.
\end{aligned}
$$

Suppose $X_t$ has a symmetric $\alpha$-stable process with Lévy measure as in (6.28) with $C = 1/b_\alpha$. It can be shown that $X_1$ has a symmetric density $g_\alpha$,

$$ \mathbb{P}\{a \le X \le b\} = \int_a^b g_\alpha(x) \, dx. $$

This density is bounded. Unfortunately, except for the case $\alpha = 1$, there is no explicit form expression for the density. Despite this fact, it is known that

$$ g_\alpha(x) \sim \frac{1}{|x|^{1+\alpha}}, \quad |x| \to \infty, $$

and hence

$$ \mathbb{P}\{|X_1| \ge K\} \sim \int_{|x|\ge K} g_\alpha(x) \, dx = \frac{2}{\alpha K^\alpha}. $$

This comes from the fact that the easiest way for $|X_1|$ to be unusually large is for there to be a single very large jump, and the probability of a jump of size at least $K$ by time one is asymptotic to $\mu\{|x| \ge K\}$.

If $\alpha = 1$, then $b_\alpha = \pi$ and the corresponding Lévy measure is

$$ d\mu(x) = \frac{1}{\pi\, x^2}. $$

The density of $X_1$ is the *Cauchy density*

$$ g_1(x) = \frac{1}{\pi\,(x^2 + 1)}. $$

### PDF page 235 (book page 229)

The easiest way to check this is to compute the characteristic function of $g_t$ and obtain $e^{-|s|}$.

Symmetric stable distribution arise as limit distributions for sums of symmetric random variables with "heavy tails". The next proposition gives one version.

**Proposition 6.10.3.** *Suppose $\alpha, c > 0$ and $X_1, X_2, \ldots$ are independent, identically distributed random variables with a bounded density $f$ satisfying $f(x) = f(-x)$ and*

$$ f(x) \sim \frac{c}{x^{1+\alpha}}, \quad x \to \infty, \tag{6.29} $$

*where $\sim$ means the ratio of the two sides converges to one.*

- *If $0 < \alpha < 2$, and*

$$ Z_n = \frac{X_1 + \cdots + X_n}{n^{1/\alpha}}, \tag{6.30} $$

  *then $Z_n$ converges in distribution to an $\alpha$-symmetic random variable.*

- *If $\alpha > 2$, and*

$$ Z_n = \frac{X_1 + \cdots + X_n}{\sqrt{n}}, $$

  *then $Z_n$ converges in distribution to a centered normal random variable.*

- *If $\alpha = 2$, and*

$$ Z_n = \frac{X_1 + \cdots + X_n}{\sqrt{n \log n}}, $$

  *then $Z_n$ converges in distribution to a centered normal random variable.*

If $\alpha > 2$, then $\mathrm{Var}[X_j] < \infty$, and hence the result is a restatement of the central limit theorem.

---

We will prove the proposition for $0 < \alpha < 2$. Our first observation is that if $X_1, X_2, \ldots$ are independent, identically distributed random variables whose characteristic exponent $\Psi$ satisfies

$$ \Psi(s) = -r\,|s|^\alpha + o(|s|^\alpha), \quad s \to 0, \tag{6.31} $$

then $Z_n$ as defined in (6.30) converges to an $\alpha$-stable distribution. This follows since for each $s$,

$$ \lim_{n \to \infty} \Psi_{Z_n}(s) = \lim_{n \to \infty} n\,\Psi(s/n^{1/\alpha}) = -r\,|s|^\alpha. $$

### PDF page 236 (book page 230)

Therefore, we only need to show that (6.29) implies (6.31).

Let $\phi$ denote the characteristic function of $X_1$, and note that $-\Psi(s) = -\log \phi(s) \sim \phi(s) - 1$ as $s \to 0$. By changing variables, we see that if $s > 0$,

$$
\begin{aligned}
\phi(s) - 1 &= \int_{-\infty}^{\infty} [e^{isx} - 1]\, f(x)\, dx \\
&= 2 \int_{0}^{\infty} [\cos(sx) - 1]\, f(x)\, dx \\
&= 2s^{-1} \int_{0}^{\infty} [\cos y - 1]\, f(y/s)\, dy \\
&= 2s^{\alpha} \int_{0}^{\infty} [\cos y - 1]\, s^{-(1+\alpha)}\, f(y/s)\, dy
\end{aligned}
$$

We claim that

$$ \lim_{s \downarrow 0} \int_{0}^{\infty} [\cos y - 1]\, s^{-(1+\alpha)}\, f(y/s)\, dy = cI, $$

where

$$ I = \int_{0}^{\infty} \frac{\cos y - 1}{y^{1+\alpha}}\, dy, $$

from which (6.31) follows with $r = 2cI$. To see this, let $\epsilon = (2-\alpha)/6 > 0$ and note that

$$
\begin{aligned}
\left| \int_{0}^{s^{1-\epsilon}} [\cos y - 1]\, s^{-(1+\alpha)}\, f(y/s)\, dy \right| &\leq C\, s^{-(1+\alpha)} \int_{0}^{s^{1-\epsilon}} y^2\, dy \\
&\leq C s^{(2-\alpha)/2} \longrightarrow 0.
\end{aligned}
$$

Also, for $y \geq s^{1-\epsilon}$,

$$ f(y/s) = c\,(y/s)^{-(1+\alpha)}\,[1 + o(1)], $$

and hence

$$
\begin{aligned}
\lim_{s \downarrow 0} \int_{s^{1-\epsilon}}^{\infty} [\cos y - 1]\, s^{-(1+\alpha)}\, f(y/s)\, dy \\
= c \lim_{s \downarrow 0} \int_{s^{1-\epsilon}}^{\infty} [\cos y - 1]\, y^{-(1+\alpha)}\, dy = cI.
\end{aligned}
$$

---

Proposition 6.10.3 only uses stable processes for $\alpha \leq 2$. The next proposition that shows that there are no nontrivial stable process for $\alpha > 2$.

### PDF page 237 (book page 231)

**Proposition 6.10.4.** *Suppose $0 < \beta < 1/2$, and $X_1, X_2, \ldots$ are independent, identically distributed each having the same distribution as*

$$ \frac{X_1 + \cdots + X_n}{n^\beta}. $$

*Then $\mathbb{P}\{X_j = 0\} = 1$.*

---

We use the following lemma to prove Proposition 6.10.4.

**Lemma 6.10.5.** *Suppose $X$ is a nonconstant random variable with characteristic function $\phi$. Then there exists $\epsilon > 0$ such that if $|s| \leq \epsilon$, then*

$$ |\phi(s)| \leq 1 - \epsilon\, s^2. $$

*Proof.* Let us first assume that $X$ is bounded with mean $m$ and variance $\sigma^2 > 0$. Then, the characteristic function satisfies

$$ \phi(s) = e^{ims} \left[ 1 - \frac{\sigma^2}{2}\, s^2 + O(|s|^3) \right], \quad s \downarrow 0, $$

and hence there exists $\epsilon > 0$ such that

$$ |\phi(s)| \leq \left| 1 - \frac{\sigma^2}{4}\, s^2 \right|, \quad |s| \leq \epsilon. $$

For general nonconstant $X$, we can find a bounded interval $I$ such that $\mathbb{P}\{X \in I\} = \rho > 0$ and such the variance $\sigma^2$ of the conditional distribution given $X \in I$ is positive. Then,

$$ \phi(s) = \rho\, \mathbb{E}[e^{isX} \mid X \in I] + (1 - \rho)\, \mathbb{E}[e^{isX} \mid X \notin I]. $$

There exists $\epsilon > 0$ such that if $|s| \leq \epsilon$, $|\mathbb{E}[e^{isX} \mid X \in I]| \leq 1 - (\sigma^2 s^2/4)$ and hence

$$ |\phi(s)| \leq \rho \left( 1 - \frac{\sigma^2}{4}\, s^2 \right) + 1 - \rho = 1 - \frac{\rho\sigma^2}{4}\, s^2. $$

$\square$

To prove Proposition 6.10.4, let $\phi$ denote the characteristic function of $X_j$. Then

$$ \phi(s) = \phi(n^{-\beta}\, s)^n. $$

### PDF page 238 (book page 232)

If the distribution of $X_j$ is nontrivial, then there exists $\epsilon > 0$ such that for $|s| \leq \epsilon$,
$$ |\phi(s)| \leq 1 - \epsilon\, s^2, $$
and hence for every $s \neq 0$,
$$ \begin{aligned} |\phi(s)| = \lim_{n\to\infty} |\phi(n^{-\beta}\, s)|^n \;\; &\leq\; \lim_{n\to\infty} \left(1 - \epsilon\, n^{-2\beta}\, s^2\right)^n \\ &\leq\; \lim_{n\to\infty} \exp\left\{-\epsilon\, s^2\, n^{1-2\beta}\right\} = 0. \end{aligned} $$

Since $\phi$ is continuous at $0$ with $\phi(0) = 1$, this is a contradiction. Therefore, $\mathbb{P}\{X_j = c\} = 1$ for some $c$ and since $c = (c + \cdots + c)/n^\beta$, $c = 0$.

---

## 6.11 Exercises

**Exercise 6.1.** Suppose $F(t) = \mathbb{P}\{T \leq t\}$ is the distribution function of a continuous random variable $T$. Define the "inverse" function $G$ by
$$ G(r) = \sup\{t : F(t) \leq r\}. $$

1. Suppose $U$ is a random variable distributed uniformly on $[0, 1]$. Show that $G(U)$ has distribution function $F$.

2. Find $G$ in the case that $T$ is exponential with rate $\lambda$.

3. Use the waiting time method as described in Section 6.2 to sample from a Poisson process $X_t$ with rate $\lambda = 3/2$. Run at least 3000 trials to estimate the distributon [sic] of $X_3$.

4. Compare the simulations with the actual distribution for $X_3$.

**Exercise 6.2.** Suppose $Y_t$ is a Poisson process with parameter 2.

1. Find $\mathbb{P}\{Y_3 \geq 2\}$.

2. Find $\mathbb{P}\{Y_4 \geq Y_1 + 2 \mid Y_1 = 4\}$.

3. Find $\mathbb{P}\{Y_1 = 1 \mid Y_3 = 4\}$.

### PDF page 239 (book page 233)

4. Find a nonrandom function $a(t)$ such that
$$ X_t = Y_t - a(t) $$
is a martingale, that is, if $s \leq t$,
$$ E[X_t \mid \mathcal{F}_s] = E[X_t \mid Y_s] = X_s. $$
Here $\mathcal{F}_t$ denotes the information in $\{Y_s : s \leq t\}$.

**Exercise 6.3.** Suppose $X_t$ is a compound Poisson process with $\lambda = 2$, and measure $\mu^{\#}$ is given by a $N(0, 1)$ distribution. In other words, the process jumps when a Poisson process of rate 2 jumps and when it jumps it chooses a jump size from a $N(0, 1)$ distribution.

- Find the function $f$ so that the Lévy measure $\mu$ can be written as $d\mu = f(x)\, dx$.

- Find $\mathbb{E}[X_t]$.

- Find $\mathbb{E}[X_t^2]$

- What is the generator $L$ of the process $X_t$?

- Does there exist a process $S_t$ such that for each $t$, $S_t$ is measurable with respect to $\mathcal{F}_t$, the information in $\{X_s : 0 \leq s \leq t\}$, and such that

  - With probability one, $S_t$ is differentiable with respect to $t$,
  - $M_t = X_t^2 - S_t$ is a martingale

  If so find it.

**Exercise 6.4.** Let $X_t$ be as in Exercise 6.3 and let
$$ Z_t = \exp\{X_t\}. $$

1. Find $\mathbb{E}[Z_t]$.

2. Find a continuous process $S_t$, adapted to the information in $\{\mathcal{F}_t\}$, with $S_t > 0$ such that $S_t$ is differentiable with respect to $t$ (except at the $t$ at which $X_t$ jumps) and
$$ M_t = Z_t - S_t $$
is a martingale? Explain why $S_t$ is not differentiable at the jump times of $X_t$.

### PDF page 240 (book page 234)

3. Does there exist a process $A_t$, adapted to the information in $\{\mathcal{F}_t\}$, with $A_t > 0$ such that $A_t$ is differentiable with respect to $t$ (except at the $t$ at which $X_t$ jumps) and
$$ M_t = Z_t\, A_t $$
is a martingale?

**Exercise 6.5.** Suppose $Y_t$ is a Cauchy process, that is, a Lévy process such that $Y_1$ has a Cauchy distribution. Show why the following statement holds: for every $r > 0$ and $t > 0$,
$$ \mathbb{P}\left\{\max_{0 \leq s \leq t} Y_s > r\right\} \;\; (*) \;\; 2\,\mathbb{P}\{Y_t > r\}. $$

Here $(*)$ is one of the following: $>, =, <$. Your task is to figure out which of $>, =, <$ should go into the statement and explain why the relation holds. (Hint: go back to the derivation of the reflection principle for Brownian motion. The only things about the Cauchy process that you should need to use are that it is symmetric about the origin and has jumps. Indeed, the same answer should be true for any symmetric Lévy process with jumps.)

**Exercise 6.6.** Suppose $X_t$ is a Poisson process with rate 1 and let $r > 0$ with filtration $\{\mathcal{F}_t\}$, and
$$ \tilde{S}_t = e^{X_t - rt}. $$

1. Find a strictly positive martingale $M_t$ with $M_0 = 1$ such that $\tilde{S}_t$ is a martingale with respect to the tilted measure $Q$ given by
$$ Q(V) = \mathbb{E}\left[1_V\, M_t\right], \quad V \in \mathcal{F}_t. $$

2. Is your choice of $M_t$ and $Q$ unique?

**Exercise 6.7.** Suppose $f : \mathbb{R} \to \mathbb{R}$ is a function that is right continuous at every point. Let
$$ K_f = \sup\{|f(x)| : 0 \leq x \leq 1\}. $$

1. Give an example to show that it is possible that $K_f = \infty$.

2. Show that if $f$ is a cadlag function, then $K_f < \infty$.

### PDF page 241 (book page 235)

**Exercise 6.8.** Suppose $X_t$ is a generalized Poisson process with Lévy measure $\mu$ given by

$$ d\mu(x) = \frac{dx}{x}, \quad 0 < x < 1. $$

1. Is this a generalized Poisson process of Type I?

2. Find $\mathbb{E}[X_t], \operatorname{Var}[X_t]$.

3. What is the probability that there are no jumps of size greater than $1/2$ by time $t = 2$?

4. Let

$$ f(t, x) = \mathbb{E}\left[ X_t^4 \mid X_0 = x \right]. $$

Find the function $g(x)$ such that

$$ \frac{d}{dt} f(t, x) \mid_{t=0} = g(x). $$

**Exercise 6.9.** Suppose $X_t$ is as in Exercise 6.8 and $B_t$ is an independent standard Brownian motion. Let $Y_t = X_t + t + 2B_t$ and answer the same questions for $Y_t$.

**Exercise 6.10.** Do Exercise 6.8 where

$$ d\mu(x) = \frac{dx}{|x|^{5/2}}, \quad 0 < |x| < 1. $$

### PDF page 242 (book page 236)

*(Blank page.)*

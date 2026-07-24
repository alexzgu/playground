# Chapter 3 — Stochastic integration
*(PDF pages 89–130; book pages 83–124)*

### PDF page 89 (book page 83)
# Chapter 3 — Stochastic integration

**3.1 What is stochastic calculus?**

Before venturing into stochastic calculus, it will be useful to review the basic ideas behind the usual differential and integral calculus. The main deep idea of calculus is that one can find values of a function knowing the rate of change of the function. For example, suppose $f(t)$ denotes the position of a (one-dimensional) particle at time $t$, and we are given the rate of change

$$ df(t) = C(t, f(t)) \, dt, $$

or as it is usually written,

$$ \frac{df}{dt} = f'(t) = C(t, f(t)). $$

In other words, at time $t$ the graph of $f$ moves for an infinitesimal amount of time along a straight line with slope $C(t, f(t))$. This is an example of a differential equation, where the rate depends both on time and position. If we are given an initial condition $f(0) = x_0$, then (under some hypotheses on the rate function $C$, see the end of Section 3.5), the function is defined and can be given by

$$ f(t) = x_0 + \int_0^t C(s, f(s)) \, ds. $$

If one is lucky, then one can do the integration and find the function exactly. If one cannot do this, one can still use a computer to approximate the solution.

### PDF page 90 (book page 84)
The simplest, but still useful, technique is *Euler's method* where one chooses a small increment $\Delta t$ and then writes

$$ f((k + 1)\Delta t) = f(k\Delta t) + \Delta t \, C(k\Delta t, f(k\Delta t)). $$

Stochastic calculus is similar, except that one adds randomness to the change. We will make sense of equations such as

$$ dX_t = m(t, X_t) \, dt + \sigma(t, X_t) \, dB_t, \tag{3.1} $$

where $B_t$ is a standard Brownian motion. This is an example of a *stochastic differential equation (SDE)*. We should read this equation as stating that at time $t$, $X_t$ is evolving like a Brownian motion with drift $m(t, X_t)$ and variance $\sigma(t, X_t)^2$. Solving such equations exactly is much harder than for usual calculus, and we often have to resort to numerical methods. One technique is the *stochastic Euler method* which allows us to do *Monte Carlo simulations* of the process. This is easy enough to describe so we give the formula now

$$ X((k + 1)\Delta t) = $$

$$ X(k\Delta t) + \Delta t \, m(k\Delta t, X(k\Delta t)) + \sqrt{\Delta t} \, \sigma(k\Delta_t, X(k\Delta t)) \, N_k, $$

where $N_k$ is a $N(0, 1)$ random variable.

The standard approach to calculus is to define the derivative, then define the integral, and then give the relationship between the two. One could also define the integral first. In stochastic calculus, the derivative is not so easily defined, so in order to give a mathematical formulation we concentrate on defining the stochastic integral. We will say that $X_t$ is a solution to (3.1) if

$$ X_t = X_0 + \int_0^t m(s, X_s) \, ds + \int_0^t \sigma(s, X_s) \, dB_s. $$

The $ds$ integral is the usual integral from calculus; the integrand $m(s, X_s)$ is random, but that does not give any problem in defining the integral. The main task will be to give precise meaning to the second term, and more generally to

$$ \int_0^t A_s \, dB_s. $$

There are several approaches to stochastic integration. The approach we give, which is most commonly used in mathematical finance, is that of the *Itô integral*.

### PDF page 91 (book page 85)

**3.2 Stochastic integral**

Let $B_t$ be a standard (one-dimensional) Brownian motion with respect to a filtration $\{\mathcal{F}_t\}$. We want to define the process

$$ Z_t = \int_0^t A_s \, dB_s. $$

We think of $Z_t$ as a Brownian motion which at time $s$ has variance $A_s^2$. In analogy to the discrete stochastic integral, we think of $A_s$ as the amount "bet" or "invested" at time $s$ with negative bets indicating bets that the process will go down. Also, as in the discrete case, we want to restrict our betting strategies to those that cannot look into the future. For continuous time processes for which changes are happening infinitesimally it is somewhat trickier to make the last condition precise. We will start by doing some easy cases and then define more complicated cases by taking limits.

**3.2.1 Review of Riemann integration**

Let us review the definition of the usual Riemann integral from calculus. Suppose $f(t)$ is a continuous function and we wish to define

$$ \int_0^1 f(t) \, dt. $$

We partition $[0, 1]$ into small intervals, say

$$ 0 = t_0 < t_1 < \cdots < t_n = 1, $$

and approximate $f(t)$ by a *step function*

$$ f_n(t) = f(s_j), \quad t_{j-1} < t \leq t_j, $$

where $s_j$ is some point chosen in $[t_{j-1}, t_j]$. We define

$$ \int_0^1 f_n(t) \, dt = \sum_{j=1}^n f(s_j) \, (t_j - t_{j-1}). $$

It is a theorem that if we take a sequence of partitions such that the maximum length of the intervals $[t_{j-1}, t_j]$ goes to zero, then the limit

$$ \int_0^1 f(t) \, dt = \lim_{n \to \infty} \int_0^1 f_n(t) \, dt $$

### PDF page 92 (book page 86)

exists and is independent of the choice of sequence of partitions or the choice of $s_j$. This is the *definition* of the left-hand side. One later proves the important facts, for example, the fundamental theorem of calculus,

$$ \int_a^b f'(t) \, dt = f(b) - f(a). $$

**3.2.2 Integration of simple processes**

The analogue of a step function for the stochastic integral is a *simple process*. This corresponds to a betting strategy that allows one to change bets only at a prescribed finite set of times. To be more precise, a process $A_t$ is a simple process if there exist times

$$ 0 = t_0 < t_1 < \cdots < t_n < \infty $$

and random variables $Y_j, j = 0, 1, \ldots, n$ that are $\mathcal{F}_{t_j}$-measurable such that

$$ A_t = Y_j, \quad t_j \leq t < t_{j+1}. $$

Here we set $t_{n+1} = \infty$. Since $Y_j$ is $\mathcal{F}_{t_j}$-measurable, $A_t$ is $\mathcal{F}_t$-measurable. We also assume that $\mathbb{E}[Y_j^2] < \infty$ for each $j$. If $A_t$ is a simple process we define

$$ Z_t = \int_0^t A_s \, dB_s, $$

by

$$ Z_{t_j} = \sum_{i=0}^{j-1} Y_i \, [B_{t_{i+1}} - B_{t_i}], $$

and, more generally,

$$ Z_t = Z_{t_j} + Y_j \, [B_t - B_{t_j}] \quad \text{if } t_j \leq t \leq t_{j+1}, $$

$$ \int_r^t A_s \, dB_s = Z_t - Z_r. $$

There are four important properties of the stochastic integral of simple processes which we give in the next proposition. The reader should compare these with the properties of integration with respect to random walk in Section 1.6.

### PDF page 93 (book page 87)

**Proposition 3.2.1.** *Suppose $B_t$ is a standard Brownian motion with respect to a filtration $\{\mathcal{F}_t\}$, and $A_t, C_t$ are simple processes.*

- **Linearity.** *If $a, b$ are constants, then $aA_t + bC_t$ is also a simple process and*
$$ \int_0^t (aA_s + bC_s) \, dB_s = a \int_0^t A_s \, dB_s + b \int_0^t C_s \, dB_s. $$
  *Moreover, if $0 < r < t$,*
$$ \int_0^t A_s \, dB_s = \int_0^r A_s \, dB_s + \int_r^t A_s \, dB_s. $$

- **Martingale property.** *The process*
$$ Z_t = \int_0^t A_s \, dB_s $$
  *is a martingale with respect to $\{\mathcal{F}_t\}$.*

- **Variance rule**. *$Z_t$ is square integrable and*
$$ \mathrm{Var}[Z_t] = \mathbb{E}\left[ Z_t^2 \right] = \int_0^t \mathbb{E}[A_s^2] \, ds. $$

- **Continuity**. *With probability one, the function $t \mapsto Z_t$ is a continuous function.*

Let us discuss the proof of the proposition. Linearity follows immediately from the definition, and continuity follows from the continuity of Brownian motion. To show that $Z_t$ is a martingale, we need to show that

$$ E(Z_t \mid \mathcal{F}_s) = Z_s \quad \text{if} \quad s < t. \tag{3.2} $$

We will do this in the case $t = t_j, s = t_k$ for some $j > k$ and leave the other cases for the reader. In this case

$$ Z_s = \sum_{i=0}^{k-1} Y_i \, [B_{t_{i+1}} - B_{t_i}], $$

and

$$ Z_t = Z_s + \sum_{i=k}^{j-1} Y_i \, [B_{t_{i+1}} - B_{t_i}]. $$

### PDF page 94 (book page 88)

Since $E(Z_s \mid \mathcal{F}_s) = Z_s$, we see that

$$ E(Z_t \mid \mathcal{F}_s) = Z_s + \sum_{i=k}^{j-1} E\left[ Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] \mid \mathcal{F}_s \right]. $$

For $k \le i \le j-1$, we have $t_i \ge s$ and hence

$$ E\left[ Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] \mid \mathcal{F}_s \right] = E\left[ E\left( Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] \mid \mathcal{F}_{t_i} \right) \mid \mathcal{F}_s \right]. $$

Since $Y_i$ is $\mathcal{F}_{t_i}$-measurable and $B_{t_{i+1}} - B_{t_i}$ is independent of $\mathcal{F}_{t_i}$,

$$ E\left( Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] \mid \mathcal{F}_{t_i} \right) = Y_i\, E\left( B_{t_{i+1}} - B_{t_i} \mid \mathcal{F}_{t_i} \right) = Y_i\, \mathbb{E}[B_{t_{i+1}} - B_{t_i}] = 0. $$

This gives (3.2).

We will prove the variance rule for $t = t_j$ in which case

$$ Z_t^2 = \sum_{i=0}^{j-1} \sum_{k=0}^{j-1} Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] Y_k \left[ B_{t_{k+1}} - B_{t_k} \right]. $$

If $i < k$,

$$ \begin{aligned} &\mathbb{E}\left[ Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] Y_k \left[ B_{t_{k+1}} - B_{t_k} \right] \right] \\ &= \mathbb{E}\left[ E\left( Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] Y_k \left[ B_{t_{k+1}} - B_{t_k} \right] \mid \mathcal{F}_{t_k} \right) \right]. \end{aligned} $$

The random variables $Y_i, Y_k, B_{t_{i+1}} - B_{t_i}$ are all $\mathcal{F}_{t_k}$-measurable while $B_{t_{k+1}} - B_{t_k}$ is independent of $\mathcal{F}_{t_k}$, and hence

$$ \begin{aligned} E\left( Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] Y_k \left[ B_{t_{k+1}} - B_{t_k} \right] \mid \mathcal{F}_{t_k} \right) \\ = \ Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] Y_k\, E\left( B_{t_{k+1}} - B_{t_k} \mid \mathcal{F}_{t_k} \right) \\ = \ Y_i \left[ B_{t_{i+1}} - B_{t_i} \right] Y_k\, \mathbb{E}\left[ B_{t_{k+1}} - B_{t_k} \right] = 0. \end{aligned} $$

Arguing similarly for $i > k$, we see that

$$ \mathbb{E}[Z_t^2] = \sum_{i=0}^{j-1} \mathbb{E}\left[ Y_i^2 \left( B_{t_{i+1}} - B_{t_i} \right)^2 \right]. $$

(We have just reproduced the argument showing orthogonality of martingale increments.) Since $Y_i^2$ is $\mathcal{F}_{t_i}$-measurable and $(B_{t_{i+1}} - B_{t_i})^2$ is independent of $\mathcal{F}_{t_i}$, we get

$$ \begin{aligned} E\left[ Y_i^2 \left( B_{t_{i+1}} - B_{t_i} \right)^2 \mid \mathcal{F}_{t_i} \right] &= Y_i^2\, E\left[ \left( B_{t_{i+1}} - B_{t_i} \right)^2 \mid \mathcal{F}_{t_i} \right] \\ &= Y_i^2\, \mathbb{E}\left[ \left( B_{t_{i+1}} - B_{t_i} \right)^2 \right] \\ &= Y_i^2 \left( t_{i+1} - t_i \right), \end{aligned} $$

### PDF page 95 (book page 89)

and hence,

$$ \begin{aligned} \mathbb{E}\left[ Y_i^2 \left( B_{t_{i+1}} - B_{t_i} \right)^2 \right] &= \mathbb{E}\left[ E\left( Y_i^2 \left( B_{t_{i+1}} - B_{t_i} \right)^2 \mid \mathcal{F}_{t_i} \right) \right] \\ &= \mathbb{E}[Y_i^2] \left( t_{i+1} - t_i \right). \end{aligned} $$

The function $s \mapsto \mathbb{E}[A_s^2]$ is a step function that takes on the value $\mathbb{E}[Y_i^2]$ for $t_i \le s < t_{i+1}$. Therefore,

$$ \mathbb{E}[Z_t^2] = \sum_{i=0}^{j-1} \mathbb{E}[Y_i^2] \left( t_{i+1} - t_i \right) = \int_0^t \mathbb{E}[A_s^2]\, ds. $$

**3.2.3 Integration of continuous processes**

In this section we will assume that $A_t$ is a process with continuous paths that is adapted to the filtration $\{\mathcal{F}_t\}$. Recall that this implies that each $A_t$ is $\mathcal{F}_t$-measurable. To integrate these processes we use the following approximation result.

**Lemma 3.2.2.** *Suppose $A_t$ is a process with continuous paths, adapted to the filtration $\{\mathcal{F}_t\}$. Suppose also that there exists $C < \infty$ such that with probability one $|A_t| \le C$ for all $t$. Then there exists a sequence of simple processes $A_t^{(n)}$ such that for all $t$,*

$$ \lim_{n \to \infty} \int_0^t \mathbb{E}\left[ |A_s - A_s^{(n)}|^2 \right]\, ds = 0. \tag{3.3} $$

*Moreover, for all $n, t$, $|A_t^{(n)}| \le C$.*

---

We will prove this lemma for $t = 1$. let

$$ A_t^{(n)} = A(j, n), \qquad \frac{j}{n} \le t < \frac{j+1}{n}, $$

where $A(0, n) = A_0$ and for $j \ge 1$,

$$ A(j, n) = n \int_{(j-1)/n}^{j/n} A_s\, ds. $$

### PDF page 96 (book page 90)

It suffices to prove (3.3) for each fixed value of $t$ and for ease we will choose $t = 1$. By construction, the $A_t^{(n)}$ are simple processes satisfying $|A_t^{(n)}| \le C$. Since (with probability one) the function $t \mapsto A_t$ is continuous, we have

$$ A_t^{(n)} \to A_t, $$

and hence by the bounded convergence theorem applied to Lebesgue measure,

$$ \lim_{n \to \infty} Y_n = 0, $$

where

$$ Y_n = \int_0^1 [A_t^{(n)} - A_t]^2\, dt. \tag{3.4} $$

Since the random variables $\{Y_n\}$ are uniformly bounded, this implies

$$ \lim_{n \to \infty} \mathbb{E}\left[ \int_0^1 [A_t^{(n)} - A_t]^2\, dt \right] = \lim_{n \to \infty} \mathbb{E}[Y_n] = 0. $$

---

Given the lemma, we can define

$$ \int_0^t A_s\, dB_s, $$

for a bounded, continuous process $A_s$ as follows. Find a sequence of simple process $A_s^{(n)}$ satisfying (3.3). Then it can be shown that for each $t$ there is an square integrable random variable $Z_t$ such that

$$ Z_t = \lim_{n \to \infty} \int_0^t A_s^{(n)}\, dB_s. $$

We define

$$ \int_0^t A_s\, dB_s = Z_t. $$

The integral satisfies four properties which should start becoming familiar.

**Proposition 3.2.3.** *Suppose $B_t$ is a standard Brownian motion with respect to a filtration $\{\mathcal{F}_t\}$, and $A_t, C_t$ are bounded, adapted processes with continuous paths.*

### PDF page 97 (book page 91)

- **Linearity.** *If $a, b$ are constants, then*

$$ \int_0^t (aA_s + bC_s)\, dB_s = a \int_0^t A_s\, dB_s + b \int_0^t C_s\, dB_s. $$

  *Also, if $r < t$,*

$$ \int_0^t A_s\, dB_s = \int_0^r A_s\, dB_s + \int_r^t A_s\, dB_s. $$

- **Martingale property.** *The process*

$$ Z_t = \int_0^t A_s\, dB_s $$

  *is a martingale with respect to $\{\mathcal{F}_t\}$.*

- **Variance rule**. *$Z_t$ is square integrable and*

$$ \mathrm{Var}[Z_t] = \mathbb{E}\left[ Z_t^2 \right] = \int_0^t \mathbb{E}[A_s^2]\, ds. $$

- **Continuity.** *With probability one, $t \mapsto Z_t$ is a continuous function.*

---

For fixed $t$, the existence of $Z_t$ follows from the estimate (3.3) and the completeness of $L^2$. In this case, the convergence is in $L^2$. However, there are issues dealing with the fact that there are an uncountable number of times. This can be handled similarly to the construction of Brownian motion. For convenience, we restrict to $0 \le t \le 1$.

We first consider $t \in \mathcal{D}$ and define $Z_t, t \in \mathcal{D}$ as the $L^2$ limit which is defined for $t \in \mathcal{D}$ up to a single event of probability zero. Suppose $A_t$ is a simple process with $|A_t| \le C$. Then (Exercise 3.1) one can show that
$$ \mathbb{E}[(Z_t - Z_s)^4] \le 4\, C^4\, |t - s|^2. $$

By Fatou's lemma, this bound will also hold for the limit process. This estimate and an argument first due to Kolmogorov suffice to give continuity. We leave the argument as Exercise 3.11.

### PDF page 98 (book page 92)

Let $A_t^{(n)}$ be a sequence of simple processes and let $Z_t^{(n)}, Z_t$ denote the corresponding stochastic integrals. Let

$$ \|A^{(n)} - A\|^2 = \mathbb{E}\left[ (Z_1^{(n)} - Z_1)^2 \right] = \int_0^1 \mathbb{E}\left[ (A_t^{(n)} - A_t)^2 \right] dt, $$

and let
$$ Q_n = \max_{0 \le t \le 1} |Z_t^{(n)} - Z_t|. $$

If we view $Z^{(n)}, Z$ as random variables taking values in $C[0, 1]$, the set of continuous functions on $[0, 1]$ with the supremum norm, then $Q_n$ is the distance between $Z^{(n)}$ and $Z$. The next proposition establishes convergence with probability one in this space.

**Proposition 3.2.4.** *If*

$$ \sum_{n=1}^{\infty} \|A^{(n)} - A\|^2 < \infty, \tag{3.5} $$

*then with probability one, $Q_n \to 0$.*

*Proof.* By the Borel-Cantelli lemma, it suffices to show that for every $\epsilon > 0$,
$$ \sum_{n=1}^{\infty} \mathbb{P}\{Q_n > \epsilon\} < \infty. $$

Continuity of $Z_t^{(n)}$ and $Z_t$ implies that
$$ \mathbb{P}\{Q_n > \epsilon\} = \lim_{m \to \infty} \mathbb{P}\left\{ \max_{t \in \mathcal{D}_m} |Z_t^{(n)} - Z_t| > \epsilon \right\}. $$

For fixed $m$, the process $M_t = Z_t^{(n)} - Z_t, t \in \mathcal{D}_m$, is a discrete time martingale and Corollary 1.7.2 implies that
$$ \mathbb{P}\left\{ \max_{t \in \mathcal{D}_m} |M_t| > \epsilon \right\} \le \frac{\mathbb{E}[M_1^2]}{\epsilon^2}. $$

Therefore,
$$ \mathbb{P}\{Q_n > \epsilon\} \le \frac{\mathbb{E}[M_1^2]}{\epsilon^2} = \epsilon^{-2}\, \|A^{(n)} - A_t\|^2. \quad \square $$

Let us emphasize the order of quantifiers in the proposition. Given a sequence $A^{(n)}$ of approximating simple processes satisfying (3.5), we get convergence with probability one. It is not true that with probability one, we get convergence for every sequence. See an analogous discussion in Section 2.8 about the quadratic variation.

### PDF page 99 (book page 93)

---

If $A_t$ is adapted with continuous paths, but not necessarily bounded, we can still define
$$ Z_t = \int_0^t A_s\, dB_s $$

as follows. For each $n < \infty$, let $T_n = \min\{t : |A_t| = n\}$ and let $A_s^{(n)} = A_{s \wedge T_n}$. Then $A_s^{(n)}$ is a bounded, continuous process and

$$ Z_t^{(n)} = \int_0^t A_s^{(n)}\, dB_s. $$

is well defined. We define
$$ Z_t = \lim_{n \to \infty} Z_t^{(n)}. $$

The existence of this limit is easy to establish. Indeed, let
$$ K_t = \max_{0 \le s \le t} |A_s|. $$

Then for $n \ge K_t$, $A_s^{(n)} = A_s$ for $0 \le s \le t$, and hence
$$ Z_t^{(n)} = Z_t, \quad t \ge K_t. $$

There is a subtlety here. Since $K_t$ is a random variable, the $n$ that one needs to choose may depend on the path. Although $Z_t$ is well defined in the limit and satisfies linearity and continuity, we will see in Section 4.1 that it might not satisfy the martingale property. Let us not worry about this at the moment. We will state the following.

**Proposition 3.2.5.** *Suppose $B_t$ is a standard Brownian motion with respect to a filtration $\{\mathcal{F}_t\}$, and $A_t, C_t$ are adapted processes with continuous paths.*

- **Linearity.** *If $a, b$ are constants and $r < t$, then*

$$ \int_0^t (aA_s + bC_s)\, dB_s = a \int_0^t A_s\, dB_s + b \int_0^t C_s\, dB_s, $$

$$ \int_0^t A_s\, dB_s = \int_0^r A_s\, dB_s + \int_r^t A_s\, dB_s. $$

### PDF page 100 (book page 94)

- **Variance rule**. *The variance of $Z_t$ satisfies*

$$ \mathrm{Var}[Z_t] = \mathbb{E}\left[ Z_t^2 \right] = \int_0^t \mathbb{E}[A_s^2]\, ds. $$

  *It is possible for both sides to equal infinity. However, if $\mathrm{Var}[Z_t] < \infty$ for all $t$, then $Z_t$ is a square integrable martingale.*

- **Continuity** *With probability one, $t \mapsto Z_t$ is a continuous function.*

We can relax the condition of continuous paths. We say that the paths are piecewise continuous if with probability one on each finite interval the paths are continuous except a finite number of points, say $0 < t_1 < t_2 < \cdots < t_n = t$. For a piecewise continuous function with discontinuities at times $t_1, t_2, \ldots$, we define

$$ \int_0^t A_s\, dB_s = \int_0^{t_1} A_s\, dB_s + \cdots + \int_{t_{n-1}}^{t_n} A_s\, dB_s. \tag{3.6} $$

The value of this integral does not depend on how we define $A_t$ at the discontinuity. In this book, the process $A_t$ will have continuous or piecewise continuous paths although the integral can be extended to more general processes. Note that the simple processes have piecewise continuous paths. One important case that arises comes from a stopping time. Suppose $T$ is a stopping time with respect to $\{\mathcal{F}_t\}$. Then if $A_t$ is a continuous, adapted process and

$$ Z_t = \int_0^t A_s\, dB_s, $$

then

$$ Z_{t \wedge T} = \int_0^{t \wedge T} A_s\, dB_s = \int_0^t A_{s,T}\, dB_s, $$

where $A_{s,T}$ denotes the piecewise continuous process,

$$ A_{s,T} = \left\{ \begin{array}{ll} A_s & s < T \\ 0 & s \geq T \end{array} \right. . $$

In other words, stopping a stochastic integral is the same as changing the bet to zero.

### PDF page 101 (book page 95)

Continuity of paths is much more than is needed for the stochastic integral to exist. If $A_t$ is a uniformly bounded, adapted process, and we let

$$ A_t^{(n)} = n \int_{t-\frac{1}{n}}^t A_s\, ds, \tag{3.7} $$

then $A_t^{(n)}$ is an adapted continuous process. This requires some assumptions on the process $A_t$ so that integrals as in (3.4) and (3.7) exists, at least as Lebesgue integrals, and so that we can use Fubini's theorem to interchange expectation and integrals on the line. The condition to guarantee this is called *progressive measurablility* [sic], but we will not go into details here. If the $A_t$ are uniformly bounded, then the Lebesgue density theory implies that $A_t^{(n)} \to A_t$ for Lebesgue almost every $t$. Hence, with probability one,

$$ \int_0^1 [A_t^{(n)} - A_t]^2\, dt \longrightarrow 0, $$

and since the processes are bounded the convergence is also in $L^2$. For such processes we can define the stochastic integral as above as an $L^2$-limit.

---

We will write the stochastic differential

$$ dX_t = A_t\, dB_t, $$

to mean that $X_t$ satisfies

$$ X_t = X_0 + \int_0^t A_s\, dB_s. $$

This has been made mathematically precise by the definition of the integral. Intuitively, we think of $X_t$ as a process that at time $t$ evolves like a Brownian motion with zero drift and variance $A_t^2$. This is well defined for any adapted, continuous process $A_t$, and $X_t$ is a continuous function of $t$. In particular, if $\phi$ is a bounded continuous function, then we can hope to solve the equation

$$ dX_t = \phi(X_t)\, dB_t. $$

Solving such an equation can be difficult (see the end of Section 3.5), but simulating such a process is straightforward using the stochastic Euler rule:

$$ X_{t+\Delta t} = X_t + \phi(X_t)\, \sqrt{\Delta t}\, N, $$

### PDF page 102 (book page 96)

where $N \sim N(0,1)$.

The rules of stochastic calculus are not the same as those of usual calculus. As an example, consider the integral

$$ Z_t = \int_0^t B_s\, dB_s. $$

Although $B_t$ is not a bounded process, it is continuous, adapted and

$$ \int_0^t \mathbb{E}[B_s^2]\, ds = \int_0^t s\, ds = \frac{t^2}{2} < \infty, $$

so $Z_t$ is a square integrable martingale. If one naively followed the rules of calculus, one might hope that

$$ Z_t = \frac{1}{2} \left[ B_t^2 - B_0^2 \right] = \frac{B_t^2}{2}. $$

However, a quick check shows that this cannot be correct. The left-hand side is a martingale with $Z_0 = 0$ and hence

$$ \mathbb{E}[Z_t] = 0. $$

However,

$$ \mathbb{E}\left[ B_t^2/2 \right] = t/2 \neq 0. $$

In the next section we will derive the main tool for calculating integrals, *Itô's formula or lemma*. Using this we will show that, in fact,

$$ Z_t = \frac{1}{2} [B_t^2 - t]. \tag{3.8} $$

This is a very special case. In general, one must do more than just subtract the expectation. One thing to note about the solution — for $t > 0$, the random variable on the right-hand side of (3.8) does not have a normal distribution. Even though stochastic integrals are defined as limits of normal increments, the "betting" factor $A_t$ can depend on the past and this allows one to get non-normal random variables. If the integrand $A_t = f(t)$ is nonrandom, then the integral

$$ \int_0^t f(s)\, dB_s, $$

### PDF page 103 (book page 97)

is really a limit of normal random variables and hence has a normal distribution (see Exercise 3.8).

If

$$ Z_t = \int_0^t A_s \, dB_s, $$

then the *quadratic variation* of $Z$ is defined by

$$ \langle Z \rangle_t = \lim_{n \to \infty} \sum_{j \le nt} \left[ Z\left(\frac{j}{n}\right) - Z\left(\frac{j-1}{n}\right) \right]^2 . $$

**Theorem 3.2.6.** *If $A_t$ is an adapted process with continuous or piecewise continuous paths and*

$$ Z_t = \int_0^t A_s \, dB_s, $$

*then*

$$ \langle Z \rangle_t = \int_0^t A_s^2 \, ds. $$

Note that if $\sigma > 0$ is a constant and $Z_t = \int_0^t \sigma \, dB_s$, then $Z$ is a Brownian motion with variance parameter $\sigma^2$ for which we have already seen that $\langle Z \rangle_t = \sigma^2 t$. The quadratic variation $\langle Z \rangle_t$ should be viewed as the "total amount of randomness" or the "total amount of betting" that has been done up to time $t$. For Brownian motion, the betting rate stays constant and hence the quadratic variation grows linearly. For more general stochastic integrals, the current bet depends on the results of the games up to that point and hence is a random variable. The quadratic variation at time $t$ is a random variable with mean

$$ \mathbb{E}\left[ \langle Z \rangle_t \right] = \mathbb{E}\left[ \int_0^t A_s^2 \, ds \right] = \int_0^t \mathbb{E}\left[ A_s^2 \right] \, ds. $$

---

An alternative way to define the quadratic variation $\langle Z \rangle_t$ for square integrable martingales is as the unique increasing process such that

$$ M_t = Z_t^2 - \langle Z \rangle_t $$

is a martingale. If $A_t$ is a simple process, it is not hard (Exercise 3.4) to show that $M_t$ as defined above is a martingale. More generally, one

### PDF page 104 (book page 98)

can establish this by taking limits. To show that this characterization defines $\langle Z \rangle$ uniquely, we need the following proposition. The total variation of a function $f : [0, \infty) \to \mathbb{R}$ is defined as

$$ V_t(f) = \sup \sum_{j=1}^n |f(t_{j-1}) - f(t_j)| \le K, $$

where the supremum is over all partitions

$$ 0 = t_0 < t_1 < t_2 < \cdots < t_n = t. $$

We say $f$ has *bounded variation (locally)* if $V_t(f) < \infty$ for all $t$. Increasing functions clearly have bounded variation, and it is not too hard to see that the difference of increasing functions has bounded variation. Also, if $f$ is continuous with bounded variation,

$$ \lim_{t \downarrow 0} V_t(f) = 0. $$

The next proposition shows that nontrivial continuous martingales never have paths of bounded variation.

**Proposition 3.2.7.** *Suppose $M_t$ is a square integrable martingale with respect to $\{\mathcal{F}_t\}$ with $M_0 = 0$ such that with probability one, the paths of $M_t$ are continuous with bounded variation. Then $M_t = 0$ for every $t$.*

*Proof.* Since $M_t$ has continuous paths, it suffices to show that $\mathbb{P}\{M_t = 0\} = 1$ for every rational $t$. The argument is the same for all $t$, so let us assume $t = 1$. We first make the stronger assumption that $V_1(M) \le K < \infty$. Let

$$ Q_n = \sum_{j=1}^n \left[ M\left(\frac{j}{n}\right) - M\left(\frac{j-1}{n}\right) \right]^2 , $$

$$ \delta_n = \max_{j=1,\dots,n} \left\{ \left| M\left(\frac{j}{n}\right) - M\left(\frac{j-1}{n}\right) \right| \right\} , $$

and note that

$$ Q_n \le \delta_n \sum_{j=1}^n \left| M\left(\frac{j}{n}\right) - M\left(\frac{j-1}{n}\right) \right| \le \delta_n \, K. $$

### PDF page 105 (book page 99)

Orthogonality of martingale increments implies that $\mathbb{E}[M_1^2] = \mathbb{E}[Q_n]$. Continuity of the paths implies that with probability one $\delta_n \downarrow 0$ and hence $Q_n \to 0$. Since $Q_n \le \delta_n K \le K^2$, we can use the bounded convergence theorem to conclude that

$$ \mathbb{E}\left[ M_1^2 \right] = \lim_{n \to \infty} \mathbb{E}[Q_n] = 0. $$

If $V_1(M)$ is not bounded, we can consider the stopping times

$$ T_K = \inf\{t : V_t(M) = K\}. $$

The argument above gives $\mathbb{E}\left[ M_{1 \wedge T_K}^2 \right] = 0$ for each $K$, and hence with probability one for each $K$, $M_{1 \wedge T_K} = 0$. But $M_1 = \lim_{K \to \infty} M_{1 \wedge T_K}$. $\square$

Using the proposition, we see that if $Y_t$ is an increasing adapted process such that $Z_t^2 - Y_t$ is a martingale, then

$$ M_t - (Z_t^2 - Y_t) = Y_t - \langle Z \rangle_t, $$

is a continuous martingale with paths of bounded variation. Therefore, $Y_t = \langle Z \rangle_t$.

## 3.3 Itô's formula

Itô's formula is the fundamental theorem of stochastic calculus. Before stating it, let us review the fundamental theorem of ordinary calculus. Suppose $f$ is a $C^1$ function. (We recall that a function if $C^k$ if it has $k$ continuous derivatives.) Then we can expand $f$ in a Taylor approximation,

$$ f(t + s) = f(t) + f'(t) \, s + o(s), $$

where $o(s)$ denotes a term such that $o(s)/s \to 0$ as $s \to 0$. We write $f$ as a telescoping sum:

$$ f(1) = f(0) + \sum_{j=1}^n \left[ f\left(\frac{j}{n}\right) - f\left(\frac{j-1}{n}\right) \right] . $$

### PDF page 106 (book page 100)

The Taylor approximation gives

$$ f\left(\frac{j}{n}\right) - f\left(\frac{j-1}{n}\right) = f'\left(\frac{j-1}{n}\right)\frac{1}{n} + o\left(\frac{1}{n}\right). $$

Hence,

$$ f(1) = f(0) + \lim_{n\to\infty}\sum_{j=1}^{n} f'\left(\frac{j-1}{n}\right)\frac{1}{n} + \lim_{n\to\infty}\sum_{j=1}^{n} o\left(\frac{1}{n}\right). $$

The first limit on the right-hand side is the Riemann sum approximation of the definite integral and the second limit equals zero since $n\,o(1/n) \to 0$. Therefore,

$$ f(1) = f(0) + \int_0^1 f'(t)\,dt. $$

Itô's formula is similar but it requires considering both first and second derivatives.

**Theorem 3.3.1** (Itô's formula I)**.** *Suppose $f$ is a $C^2$ function and $B_t$ is a standard Brownian motion. Then for every $t$,*

$$ f(B_t) = f(B_0) + \int_0^t f'(B_s)\,dB_s + \frac{1}{2}\int_0^t f''(B_s)\,ds. $$

The theorem is often written in the differential form

$$ df(B_t) = f'(B_t)\,dB_t + \frac{1}{2}\,f''(B_t)\,dt. $$

In other words, the process $Y_t = f(B_t)$ at time $t$ evolves like a Brownian motion with drift $f''(B_t)/2$ and variance $f'(B_t)^2$. Note that $f'(B_t)$ is a continuous adapted process so the stochastic integral is well defined.

To see where the formula comes from, let us assume for ease that $t = 1$. Let us expand $f$ in a second-order Taylor approximation,

$$ f(x + y) = f(x) + f'(x)\,y + \frac{1}{2}\,f''(x)\,y^2 + o(y^2), $$

where $o(y^2)/y^2 \to 0$ as $y \to 0$. Similarly to above, we write

$$ f(B_1) - f(B_0) = \sum_{j=1}^{n}\left[ f\left(B_{j/n}\right) - f\left(B_{(j-1)/n}\right)\right]. $$

### PDF page 107 (book page 101)

Using the Taylor approximation, we write

$$ f\left(B_{j/n}\right) - f\left(B_{(j-1)/n}\right) $$

$$ = f'\left(B_{(j-1)/n}\right)\Delta_{j,n} + \frac{1}{2}\,f''\left(B_{(j-1)/n}\right)\Delta_{j,n}^2 + o(\Delta_{j,n}^2), $$

where

$$ \Delta_{j,n} = B_{j/n} - B_{(j-1)/n}. $$

Hence $f(B_1) - f(B_0)$ is equal to the sum of the following three limits:

$$ \lim_{n\to\infty}\sum_{j=1}^{n} f'\left(B_{(j-1)/n}\right)\left[B_{j/n} - B_{(j-1)/n}\right], \tag{3.9} $$

$$ \lim_{n\to\infty}\frac{1}{2}\sum_{j=1}^{n} f''\left(B_{(j-1)/n}\right)\left[B_{j/n} - B_{(j-1)/n}\right]^2, \tag{3.10} $$

$$ \lim_{n\to\infty}\sum_{j=1}^{n} o\!\left(\left[B_{j/n} - B_{(j-1)/n}\right]^2\right). \tag{3.11} $$

The increment of the Brownian motion satisfies $\left[B_{j/n} - B_{(j-1)/n}\right]^2 \approx 1/n$. Since the sum in (3.11) looks like $n$ terms of smaller order than $1/n$ the limit equals zero. The limit in (3.9) is a simple process approximation to a stochastic integral and hence we see that the limit is

$$ \int_0^1 f'(B_t)\,dB_t. $$

If $f''$ were constant, say $b$, then the limit in (3.10) would be

$$ \lim_{n\to\infty}\frac{b}{2}\sum_{j=1}^{n}\left[B_{j/n} - B_{(j-1)/n}\right]^2 = \frac{b}{2}\,\langle B\rangle_1 = \frac{b}{2}. $$

This tells us what the limit should be in general. Let $h(t) = f''(B_t)$ which is a continuous function. For every $\epsilon > 0$, there exists a step function $h_\epsilon(t)$ such that $|h(t) - h_\epsilon(t)| < \epsilon$ for every $t$. For fixed $\epsilon$, we can consider each interval on which $h_\epsilon$ is constant to see that

$$ \lim_{n\to\infty}\sum_{j=1}^{n} h_\epsilon(t)\left[B_{j/n} - B_{(j-1)/n}\right]^2 = \int_0^1 h_\epsilon(t)\,dt. $$

### PDF page 108 (book page 102)

Also,

$$ \left|\sum_{j=1}^{n}[h(t) - h_\epsilon(t)]\left[B_{j/n} - B_{(j-1)/n}\right]^2\right| \le \epsilon\sum_{j=1}^{n}\left[B_{j/n} - B_{(j-1)/n}\right]^2 \to \epsilon. $$

Therefore, the limit in (3.10) is the same as

$$ \lim_{\epsilon\to 0}\frac{1}{2}\int_0^1 h_\epsilon(t)\,dt = \frac{1}{2}\int_0^1 h(t)\,dt = \frac{1}{2}\int_0^1 f''(B_t)\,dt. $$

**Example 3.3.1.** Let $f(x) = x^2$. Then $f'(x) = 2x, f''(x) = 2$, and hence

$$ B_t^2 = B_0^2 + \int_0^t f'(B_s)\,dB_s + \frac{1}{2}\int_0^t f''(B_s)\,ds = 2\int_0^t B_s\,dB_s + t. $$

This gives the equation

$$ \int_0^t B_s\,dB_s = \frac{1}{2}\,[B_t^2 - t], $$

which we mentioned in the last section. This example is particularly easy because $f''$ is constant. If $f''$ is not constant, then $f''(B_t)$ is a random variable, and the $dt$ integral is not so easy to compute.

**Example 3.3.2.** Let $f(x) = e^{\sigma x}$ where $\sigma > 0$. Then $f'(x) = \sigma e^{\sigma x} = \sigma\,f(x), f''(x) = \sigma^2 e^{\sigma x} = \sigma^2\,f(x)$. Let $X_t = f(B_t) = e^{\sigma B_t}$. Then

$$ dX_t = f'(B_t)\,dB_t + \frac{1}{2}\,f''(B_t)\,dt = \sigma\,X_t\,dB_t + \frac{\sigma^2}{2}\,X_t\,dt. $$

The process $X_t$ is an example of *geometric Brownian motion* which we discuss in more detail in the next section.

---

The derivation of Itô's formula given above is essentially correct but ignores some technical details. For ease assume $t = 1$ and assume we have a partition $\Pi$ of the form

$$ 0 = t_0 < t_1 < \cdots < t_n = 1, $$

### PDF page 109 (book page 103)

with mesh $\|\Pi\| = \max\{t_j - t_{j-1}\}$. Then we write

$$ f(B_1) = f(B_0) + \sum_{j=1}^{n} \left[ f(B_{t_j}) - f(B_{t_{j-1}}) \right] . $$

Taylor's theorem implies that

$$
\begin{aligned}
\frac{m(j,n)}{2} & \left[ B_{t_j} - B_{t_{j-1}} \right]^2 \\
&\leq \ f(B_{t_j}) - f(B_{t_{j-1}}) - f'(B_{t_{j-1}}) \left[ B_{t_j} - B_{t_{j-1}} \right] \\
&\leq \ \frac{M(j,n)}{2} \left[ B_{t_j} - B_{t_{j-1}} \right]^2 ,
\end{aligned}
$$

where $m(j,n), M(j,n)$ denote the minimum and maximum of $f''(x)$ for $x$ on the interval with endpoints $B_{t_{j-1}}$ and $B_{t_j}$. Hence if we let

$$ Q^1(\Pi) = \sum_{j=1}^{n} f'(B_{t_{j-1}}) \left[ B_{t_j} - B_{t_{j-1}} \right] , $$

$$ Q_+^2(\Pi) = \sum_{j=1}^{n} \frac{M(j,n)}{2} \left[ B_{t_j} - B_{t_{j-1}} \right]^2 , $$

$$ Q_-^2(\Pi) = \sum_{j=1}^{n} \frac{m(j,n)}{2} \left[ B_{t_j} - B_{t_{j-1}} \right]^2 , $$

we have

$$ Q_-^2(\Pi) \leq f(B_1) - f(B_0) - Q^1(\Pi) \leq Q_+^2(\Pi). $$

We now suppose that we have a sequence of partitions $\Pi_n$ of the form

$$ 0 = t_{0,n} < t_{1,n} < \cdots < t_{k_n,n} = 1, $$

with $\sum \|\Pi_n\| < \infty$. Then we have seen that with probability one, for all $0 < s < t < 1$,

$$ \lim_{n \to \infty} \sum_{s \leq t_{j,n} < t} \left[ B_{t_{j,n}} - B_{t_{j-1,n}} \right]^2 = t - s. $$

Using the continuity of $B_t$ and $f''$, we can see that on the event that this is true, we also have

$$ \lim_{n \to \infty} Q_-^2(\Pi_n) = \lim_{n \to \infty} Q_+^2(\Pi_n) = \frac{1}{2} \int_0^1 f''(B_s) \, ds. $$

### PDF page 110 (book page 104)

We now assume for the moment that there exists $K < \infty$ such that $|f''(x)| \leq K$ for all $x$. This happens, for example, if $f$ has compact support. Then

$$ |f'(B_s) - f'(B_{t_{j-1,n}})| \leq K \, |B_s - B_{t_{j-1,n}}|. $$

Let $A_t = f'(B_t)$ and let $A_t^{(n)}$ be the simple process that equals $f'(B_{t_{j-1,n}})$ for $t_{j-1,n} \leq t < t_{j,n}$. For $t_{j-1,n} \leq s < t_{j,n}$,

$$ \mathbb{E}([A_t - A_t^{(n)}]^2) \leq K^2 \, \mathbb{E}([B_s - B_{t_{j-1,n}}]^2) = K^2 \, [s - t_{j-1,n}] \leq K^2 \, \|\Pi_n\|. $$

Therefore,

$$ \int_0^1 \mathbb{E}([A_t - A_t^{(n)}]^2) \, dt \leq K^2 \, \|\Pi_n\|. $$

In particular, we get the following.

**Proposition 3.3.2.** *Suppose that $f''$ is bounded and $\{\Pi_n\}$ is a sequence of partitions with $\sum \|\Pi_n\| < \infty$. Let*

$$ Y_t^{(n)} = f(B_0) + \sum_{j=1}^{k_n} f'(B_{t_{j-1,n}}) \, [B_{t_{j,n}} - B_{t_{j-1,n}}] $$

$$ + \sum_{j=1}^{k_n} \frac{f''(B_{t_{j-1,n}})}{2} \, [B_{t_{j,n}} - B_{t_{j-1,n}}]^2. $$

*Then with probability one*

$$ \lim_{n \to \infty} \max_{0 \leq t \leq 1} |f(B_t) - Y_t^{(n)}| = 0. $$

If $f''$ is not bounded, we can still prove Itô's formula by using stopping times. This general procedure is often called *localization*. For each $K$, let

$$ T_K = \inf\{t : |f''(B_t)| \geq K\}. $$

Then, our argument shows that with probability one for each $K$,

$$ f\left(B_{t \wedge T_K}\right) = \int_0^{t \wedge T_K} f'(B_s) \, dB_s + \frac{1}{2} \int_0^{t \wedge T_K} f''(B_s) \, ds. $$

However, with probability one $T_K \to \infty$ as $K \to \infty$, and hence this gives us a formula for $f(B_t)$.

### PDF page 111 (book page 105)

Suppose that $f$ is defined only on an interval $I = (a,b)$ and $B_0 \in I$. Let

$$ T_\epsilon = \inf\{t : B_t \leq a + \epsilon \text{ or } B_t \geq b - \epsilon\}, \quad T = T_0. $$

We can apply Itô's formula to conclude for all $t$ and all $\epsilon > 0$.

$$ f(B_{t \wedge T_\epsilon}) = f(B_0) + \int_0^{t \wedge T_\epsilon} f'(B_s) \, dB_s + \frac{1}{2} \int_0^{t \wedge T_\epsilon} f''(s) \, ds. $$

This is sometimes written shorthand as

$$ df(B_t) = f'(B_t) \, dB_t + \frac{1}{2} f''(B_t) \, dt, \quad 0 \leq t < T. $$

The general strategy for proving the generalizations of Itô's formula that we give in the next couple of sections is the same, and we will not give the details.

## 3.4 More versions of Itô's formula

We first extend Itô's formula to functions that depend on time as well as position.

**Theorem 3.4.1** (Itô's Formula II)**.** *Suppose $f(t,x)$ is a function that is $C^1$ in $t$ and $C^2$ in $x$. If $B_t$ is a standard Brownian motion, then*

$$ f(t, B_t) = f(0, B_0) + \int_0^t \partial_x f(s, B_s) \, dB_s $$

$$ + \int_0^t \left[ \partial_s f(s, B_s) + \frac{1}{2} \partial_{xx} f(s, B_s) \right] ds, $$

*or in differential form,*

$$ df(t, B_t) = \partial_x f(t, B_t) \, dB_t + \left[ \partial_t f(t, B_t) + \frac{1}{2} \partial_{xx} f(t, B_t) \right] dt. $$

This is derived similarly to the first version except when we expand with a Taylor polynomial around $x$ we get another term:

$$ f(t + \Delta t, x + \Delta x) - f(t, x) = $$

### PDF page 112 (book page 106)

$$ \partial_t f(t, x)\,\Delta t + o(\Delta t) + \partial_x f(t, x)\,\Delta x + \frac{1}{2}\partial_{xx} f(t, x)\,(\Delta x)^2 + o((\Delta x)^2). $$

If we set $\Delta t = 1/n$ and write a telescoping sum for $f(1, B_1) - f(0, B_0)$ we get terms as (3.9)– (3.11) as well as two more terms:

$$ \lim_{n\to\infty} \sum_{j=1}^{n} \partial_t f((j-1)/n, B_{(j-1)/n})\,(1/n), \tag{3.12} $$

$$ \lim_{n\to\infty} \sum_{j=1}^{n} o(1/n). \tag{3.13} $$

The limit in (3.13) equals zero, and the sum in (3.12) is a Riemann sum approximation of a integral and hence the limit is

$$ \int_0^1 \partial_t f(t, B_t)\,dt. $$

**Example 3.4.1.** Let $f(t, x) = e^{at+bx}$. Then

$$ \partial_t f(t, x) = a\,f(t, x), \quad \partial_x f(t, x) = b\,f(t, x), \quad \partial_{xx} f(t, x) = b^2\,f(t, x). $$

Therefore, if $X_t = f(t, B_t) = \exp\{at + bB_t\}$,

$$
\begin{aligned}
dX_t &= \left[\partial_t f(t, B_t) + \frac{1}{2}\,\partial_{xx} f(t, B_t)\right] dt + \partial_x f(t, B_t)\,dB_t \\
&= \left(a + \frac{b^2}{2}\right) X_t\,dt + b\,X_t\,dB_t.
\end{aligned}
$$

**Definition** A process $X_t$ is a *geometric Brownian motion* with *drift $m$* and *volatility $\sigma$* if it satisfies the SDE

$$ dX_t = m\,X_t\,dt + \sigma\,X_t\,dB_t = X_t\,[m\,dt + \sigma\,dB_t], \tag{3.14} $$

where $B_t$ is a standard Brownian motion.

Example 3.4.1 shows that if $B_t$ is a standard Brownian motion and

$$ X_t = X_0 \exp\left\{\left(m - \frac{\sigma^2}{2}\right) t + \sigma\,B_t\right\}, \tag{3.15} $$

### PDF page 113 (book page 107)

then $X_t$ is a geometric Brownian motion with parameters $(m, \sigma)$. Even though we have an exact expression (3.15) for geometric Brownian motion, it is generally more useful to think of it in terms of its SDE (3.14).

Geometric Brownian motion is more natural than usual Brownian motion for modeling prices of assets such as stock. It measures changes in terms of fractions or percentages of the current price rather than the listed price per share. In particular, the latter quantity includes a rather arbitrary unit "share" which does not appear if one models with geometric Brownian motion.

The geometric Brownian motion (3.15) is what is sometimes called a "strong" solution to the SDE (3.14). (All of the solutions to SDEs that we discuss in this book are strong solutions.) We will not give the exact definition, but roughly speaking, if one uses the same Brownian motion $B_t$ in both places, one gets the same function. Let us explain this in terms of simulation. Suppose a small $\Delta t$ is chosen. Then we can define $B_{k\Delta t}$ by $B_0 = 0$ and

$$ B_{k\Delta t} = B_{(k-1)\Delta t} + \sqrt{\Delta t}\,N_k, \tag{3.16} $$

where $N_1, N_2, \ldots$ is a sequence of independent $N(0, 1)$ random variables. Using the *same* sequence, we could define an approximate solution to (3.14) by choosing $X_0 = e^0 = 1$ and

$$ X_{k\Delta t} = X_{(k-1)\Delta t} + X_{(k-1)\Delta t}\left[m\,\Delta t + \sigma\,\sqrt{\Delta t}\,N_j\right]. \tag{3.17} $$

If $\Delta t$ is small, this should be very close to

$$ Y_{k\Delta t} = \exp\left\{\left(m - \frac{\sigma^2}{2}\right)(k\Delta t) + \sigma\,B_{k\Delta t}\right\}. \tag{3.18} $$

In Exercise 3.9 you are asked to do a simulation to compare (3.17) and (3.18).

To do formal[^1] calculations in usual calculus, one writes down differentials and throws away all terms that are of smaller order than $dt$. In stochastic calculus, one can go far computing similarly using the rules

$$ (dB_t)^2 = dt, \quad (dB_t)(dt) = 0, \quad (dt)^2 = 0. $$

[^1]: Mathematicians use the word formal to refer to calculations that look correct "in form", but for which not all the steps have been justified. When they construct proofs, they often start with formal calculations and then go back and justify the steps.

### PDF page 114 (book page 108)

In some of our derivations below, we will use this kind of argument. For example, a formal derivation of Itô's formula II can be given as

$$ df(t, B_t) = \partial_t f(t, B_t)\,dt + \partial_x f(t, B_t)\,dB_t + \frac{1}{2}\,\partial_{xx} f(t, B_t)\,(dB_t)^2 $$

$$ + o(dt) + o((dt)(dB_t)) + o((dB_t)^2). $$

By setting $(dB_t)^2 = dt$ and setting the last three terms equal to zero we get the formula.

Suppose that $X_t$ satisfies

$$ dX_t = R_t\,dt + A_t\,dB_t, \tag{3.19} $$

which we recall is equivalent to

$$ X_t = X_0 + \int_0^t R_s\,ds + \int_0^t A_s\,dB_s. $$

Whenever we write such equations we will assume implicitly that $R_t, A_t$ are adapted processes with piecewise continuous paths. As before, we define the quadratic variation by

$$ \langle X\rangle_t = \lim_{n\to\infty} \sum_{j\le tn} \left[X\left(\frac{j}{n}\right) - X\left(\frac{j-1}{n}\right)\right]^2. $$

As in the case for Brownian motion, the drift term does not contribute to the quadratic variation,

$$ \langle X\rangle_t = \left\langle \int A\,dB\right\rangle_t = \int_0^t A_s^2\,ds. $$

This is often written in the differential form

$$ d\,\langle X\rangle_t = A_t^2\,dt. $$

To see that $R_t$ does not appear, we can do the formal calculation

$$
\begin{aligned}
(dX_t)^2 &= (R_t\,dt + A_t\,dB_t)^2 \\
&= R_t^2\,(dt)^2 + 2\,R_t\,A_t\,(dt)(dB_t) + A_t^2\,(dB_t)^2 = A_t^2\,dt.
\end{aligned}
$$

### PDF page 115 (book page 109)

If $X_t$ satisfies (3.19) and $H_t$ is another adapted process we define

$$ \int_0^t H_s \, dX_s = \int_0^t H_s \, R_s \, ds + \int_0^t H_s \, A_s \, dB_s. $$

If we view this in terms of simulation then

$$ Y_t = \int_0^t H_s \, dX_s $$

can be simulated by

$$ \Delta Y_t = H_t \, \Delta X_t = H_t \left[ X_{t+\Delta t} - X_t \right] = H_t \left[ R_t \, \Delta t + A_t \sqrt{\Delta t} \, N \right], $$

where $N \sim N(0, 1)$.

**Theorem 3.4.2** (Itô's formula III). *Suppose $X_t$ satisfies (3.19) and $f(t, x)$ is $C^1$ in $t$ and $C^2$ in $x$. Then*

$$
\begin{aligned}
df(t, X_t) &= \partial_t f(t, X_t) \, dt + \partial_x f(t, X_t) \, dX_t + \frac{1}{2} \, \partial_{xx} f(t, X_t) \, d\langle X \rangle_t \\
&= \left[ \partial_t f(t, X_t) + R_t \, \partial_x f(t, X_t) + \frac{A_t^2}{2} \partial_{xx} f(t, X_t) \right] dt \\
&\quad + A_t \, \partial_x f(t, X_t) \, dB_t.
\end{aligned}
$$

**Example 3.4.2.** Suppose $X$ is a geometric Brownian motion satisfying

$$ dX_t = m \, X_t \, dt + \sigma \, X_t \, dB_t. $$

Let $f(t, x) = e^{-t} x^3$. Then

$$ \partial_t f(t, x) = -e^{-t} \, x^3 = -f(t, x), $$

$$ \partial_x f(t, x) = 3x^2 \, e^{-t} = \frac{3}{x} \, f(t, x), \quad \partial_{xx} f(t, x) = 6x \, e^{-t} = \frac{6}{x^2} \, f(t, x), $$

and

$$
\begin{aligned}
df(t, X_t) &= \partial_t f(t, X_t) \, dt + \partial_x f(t, X_t) \, dX_t + \frac{1}{2} \, \partial_{xx} f(t, X_t) \, d\langle X \rangle_t \\
&= \left[ \partial_t f(t, X_t) + m \, X_t \, \partial_x f(t, X_t) + \frac{\sigma^2 \, X_t^2}{2} \, \partial_{xx} f(t, X_t) \right] dt \\
&\quad + \sigma \, X_t \, \partial_x f(t, X_t) \, dB_t \\
&= \left( -1 + 3m + \frac{6\sigma^2}{2} \right) f(t, X_t) \, dt + 3 \, \sigma \, f(t, X_t) \, dB_t.
\end{aligned}
$$

$$ d[e^{-t} X_t^3] = 3 e^{-t} X_t^3 \left[ \left( -\frac{1}{3} + m + \sigma^2 \right) dt + \sigma \, dB_t \right]. $$

### PDF page 116 (book page 110)

**Example 3.4.3.** The *exponential SDE* is

$$ dX_t = A_t \, X_t \, dB_t \quad X_0 = x_0. $$

We claim that the solution is

$$ X_t = x_0 \, \exp \left\{ \int_0^t A_s \, dB_s - \frac{1}{2} \int_0^t A_s^2 \, ds \right\}. \tag{3.20} $$

To see this, let

$$ Y_t = \int_0^t A_s \, dB_s - \frac{1}{2} \int_0^t A_s^2 \, ds, $$

which satisfies

$$ dY_t = -\frac{A_t^2}{2} \, dt + A_t \, dB_t, \quad d\langle Y \rangle_t = A_t^2 \, dt. $$

If $f(x) = x_0 \, e^x$, then $f(x) = f'(x) = f''(x)$ and

$$ df(Y_t) = f'(Y_t) \, dY_t + \frac{1}{2} f''(Y_t) \, d\langle Y \rangle_t = A_t \, X_t \, dB_t. $$

We can compare (3.20) to the solution to the deterministic exponential equation

$$ f'(t) = r(t) \, f(t) \, dt, \quad f(0) = x_0, $$

which is

$$ f(t) = x_0 \, \exp \left\{ \int_0^t r(s) \, ds \right\}. $$

Itô's formula requires that the function $f(t, x)$ be $C^1$ in $t$ and $C^2$ in $x$. In applications, one often has functions that are $C^2$ only for $x$ in an interval of the reals. In this case, we can use Itô's formula until the (random) time that the process leave the interval.

**Theorem 3.4.3** (Itô's formula III, local form). *Suppose $X_t$ satisfies (3.19) with $a < X_0 < b$, and $f(t, x)$ is $C^1$ in $t$ and $C^2$ in $x$ for $a < x < b$. Let $T = \inf\{t : X_t = a \text{ or } X_t = b\}$. Then if $t < T$,*

$$ f(t, X_t) = f(0, X_0) + \int_0^t A_s \, \partial_x f(s, X_s) \, dB_s $$

$$ + \int_0^t \left[ \partial_s f(s, X_s) + R_s \, \partial_x f(s, X_s) + \frac{A_s^2}{2} \partial_{xx} f(s, X_s) \right] ds. $$

### PDF page 117 (book page 111)

We write the conclusion of the theorem in differential form by

$$ df(t, X_t) = \dot{f}(t, X_t) \, dt + f'(t, X_t) \, dX_t + \frac{1}{2} \, f''(t, X_t) \, d\langle X \rangle_t \quad t < T. $$

**Example 3.4.4.** Suppose that $B_t$ is a standard Brownian motion, and $Y_t = t/B_t^2$. Let $T = \inf\{t : B_t = 0\}$. Then we can use Itô's formula to see that for $t < T$,

$$
\begin{aligned}
dY_t &= \dot{f}(t, B_t) \, dt + f'(t, B_t) \, dB_t + \frac{1}{2} \, f''(t, B_t) \, dt \\
&= [B_t^{-2} + 3t B_t^{-4}] \, dt - 2t B_t^{-3} \, dB_t.
\end{aligned}
$$

---

To prove the local form of Itô's formula, we let $\epsilon > 0$ and $T_\epsilon = \inf\{t : X_t \leq a + 2\epsilon \text{ or } X_t \geq b - 2\epsilon\}$. We can find a $C^\infty$ function $\phi_\epsilon$ such that $\phi_\epsilon(x) = 0$ if $x < a + \epsilon$ or $x > b - \epsilon$ and such that $\phi(x) = 1$ for $a + 2\epsilon \leq x \leq b - 2\epsilon$. Let $f_\epsilon(t, x) = \phi_\epsilon(x) \, f(t, x)$. Then $f_\epsilon$ satisfies the conditions of Itô's formula and

$$ f_\epsilon(t, X_t) - f_\epsilon(0, X_0) = \int_0^t A_s \, f'_\epsilon(s, X_s) \, dB_s $$

$$ + \int_0^t \left[ \dot{f}_\epsilon(s, X_s) + R_s \, f'_\epsilon(s, X_s) + \frac{A_s^2}{2} f''_\epsilon(s, X_s) \right] ds. $$

If $t < T_\epsilon$, then both sides of this equation are not changed if we replace $f_\epsilon$ with $f$.

---

# 3.5 Diffusions

Geometric Brownian motion is an example of a time-homogeneous diffusion. We say that $X_t$ is a *diffusion (process)* if it is a solution to an SDE of the form

$$ dX_t = m(t, X_t) \, dt + \sigma(t, X_t) \, dB_t, \tag{3.21} $$

where $m(t, x), \sigma(t, x)$ are functions. It is called *time-homogeneous* if the functions do not depend on $t$,

$$ dX_t = m(X_t) \, dt + \sigma(X_t) \, dB_t. $$

### PDF page 118 (book page 112)

Diffusion processes are Markov processes. Given all the information in $\mathcal{F}_t$, the only important information needed to give the conditional distribution of $X_s, s \geq t$ is $X_t$. Simulations of diffusions can be done using the stochastic Euler rule:

$$ X_{t+\Delta t} = X_t + m(t, X_t)\,\Delta t + \sigma(t, X_t)\,\sqrt{\Delta t}\,N, $$

where $N \sim N(0, 1)$. The study of diffusions leads to partial differential equations.

We define the generator $L = L^0$ of a (time homogeneous) Markov process $X_t$ by

$$ Lf(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}^x[f(X_t)] - f(x)}{t}. $$

We will use Itô's formula to understand the generator of the diffusion $X_t$. For ease, we will assume that $m$ and $\sigma$ are bounded continuous functions. If $f : \mathbb{R} \to \mathbb{R}$ is a $C^2$ function with bounded first and second derivatives, then Itô's formula gives

$$ \begin{aligned}
df(X_t) &= f'(X_t)\,dX_t + \frac{1}{2}\,f''(X_t)\,d\langle X \rangle_t \\
&= \left[ m(t, X_t)\,f'(X_t) + \frac{\sigma^2(t, X_t)}{2}\,f''(X_t) \right] dt \\
&\quad + f'(X_t)\,\sigma(t, X_t)\,dB_t.
\end{aligned} $$

That is,

$$ \begin{aligned}
f(X_t) - f(X_0) &= \int_0^t \left[ m(s, X_s)\,f'(X_s) + \frac{\sigma^2(s, X_s)}{2}\,f''(X_s) \right] ds \\
&\quad + \int_0^t f'(X_s)\,\sigma(s, X_s)\,dB_s.
\end{aligned} $$

The second term on the right-hand side is a martingale (since the integrand is bounded) and has expectation zero, so the expectation of the right-hand side is

$$ t\,\mathbb{E}[Y_t], $$

where

$$ Y_t = \frac{1}{t} \int_0^t \left[ m(s, X_s)\,f'(X_s) + \frac{\sigma^2(s, X_s)}{2}\,f''(X_s) \right] ds. $$

### PDF page 119 (book page 113)

The fundamental theorem of calculus implies that

$$ \lim_{t \downarrow 0} Y_t = m(0, X_0)\,f'(X_0) + \frac{\sigma^2(0, X_0)}{2}\,f''(X_0). $$

Moreover, the random variables $Y_t$ are uniformly bounded which allows us to take the limit inside the expectation,

$$ Lf(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}^x[f(X_t)] - f(x)}{t} = m(0, x)\,f'(x) + \frac{\sigma^2(0, x)}{2}\,f''(x). $$

Similarly, if we define

$$ L^t f(x) = \lim_{s \downarrow 0} \frac{\mathbb{E}[f(X_{t+s}) - f(X_t) \mid X_t = x]}{s}, $$

we get

$$ L^t f(x) = m(t, x)\,f'(x) + \frac{\sigma^2(t, x)}{2}\,f''(x). $$

The assumption that $m, \sigma$ are bounded is stronger than we would like (for example, the differential equation (3.14) for geometric Brownian motion does not satisfy this), but one can ease this by stopping the path before it gets too large. We will not worry about this now.

---

In this section we assumed we had a solution to the SDE (3.21). This leads naturally to the question: given functions $m(t, x), \sigma(t, x)$, can we find a process $X_t$ satisfying (3.21)?

Consider first the deterministic equation

$$ y'(t) = F(t, y(t)), \quad y(0) = y_0. \tag{3.22} $$

We will assume that $F$ is uniformly Lipschitz, that is, there exists $\beta < \infty$ such that for all $t, x, y$,

$$ |F(t, x) - F(t, y)| \leq \beta\,|x - y|. \tag{3.23} $$

We can construct a solution to (3.22) valid for $0 \leq t \leq t_0$ by using the following method called *Picard iteration*. We start with the initial function

$$ y_0(t) = y_0, $$

### PDF page 120 (book page 114)

and recursively define

$$ y_k(t) = y_0 + \int_0^t F(s, y_{k-1}(s))\,ds. $$

Note that

$$ |y_1(t) - y_0(t)| \leq \int_0^t |F(s, y_0)|\,ds \leq Ct, $$

where $C = C(y_0, t_0) = \max_{0 \leq s \leq t_0} |F(s, y_0)|$, and for $k \geq 1$,

$$ \begin{aligned}
|y_{k+1}(t) - y_k(t)| &\leq \int_0^t |F(s, y_k(s)) - F(s, y_{k-1}(s))|\,ds \\
&\leq \beta \int_0^t |y_k(s) - y_{k-1}(s)|\,ds.
\end{aligned} $$

Using this estimate and induction, we see that

$$ |y_{k+1}(t) - y_k(t)| \leq \frac{\beta^k\,C\,t^{k+1}}{(k + 1)!}, \quad 0 \leq t \leq t_0. $$

In particular, the limit

$$ y(t) = \lim_{k \to \infty} y_k(t), $$

exists and

$$ |y_k(t) - y(t)| \leq C \sum_{j=k}^{\infty} \frac{\beta^j\,t^{j+1}}{(j + 1)!}. $$

If we let

$$ \tilde{y}(t) = y_0 + \int_0^t F(s, y(s))\,ds, $$

then for each $k$,

$$ \begin{aligned}
|\tilde{y}(t) - y_{k+1}(t)| &\leq \int_0^t |F(s, y(s)) - F(s, y_k(s))|\,ds \\
&\leq \beta \int_0^t |y(s) - y_k(s)|\,ds,
\end{aligned} $$

and hence $\tilde{y} = y$, and $y$ satisfies (3.22). This argument assumed that (3.23) holds for all $s, t, x, y$, and we put no restriction on $t_0$. If instead we had such an estimate only for times near zero and $x, y$ near $y_0$, we could establish the same result for some (but not necessarily all) positive values of $t_0$.

### PDF page 121 (book page 115)

Let us now consider (3.21) where the functions $m(t, x)$ and $\sigma(t, x)$ both satisfy (3.23). For ease, choose $t_0 = 1$ and define recursively

$$ X_t^0 = y_0, \quad 0 \leq t \leq 1, $$

$$ X_t^{(k+1)} = y_0 + \int_0^t m(s, X_s^{(k)}) \, ds + \int_0^t \sigma(s, X_s^{(k)}) \, dB_s, $$

so that

$$ \mathbb{E}\left[ |X_t^{(k+1)} - X_t^k|^2 \right] \leq 2\mathbb{E}\left[ \left( \int_0^t \beta \, |X_s^{(k)} - X_s^{(k-1)}| \, ds \right)^2 \right] $$

$$ + 2 \, \mathbb{E}\left[ \left( \int_0^t [\sigma(s, X_s^{(k)}) - \sigma(s, X_s^{(k-1)})] \, dB_s \right)^2 \right]. $$

Using the Hölder inequality on the $ds$ integral we see that for $t \leq 1$,

$$ \mathbb{E}\left[ \left( \int_0^t \beta \, |X_s^{(k)} - X_s^{(k-1)}| \, ds \right)^2 \right] $$
$$ \leq \quad \mathbb{E}\left[ \beta^2 \, t \int_0^t |X_s^{(k)} - X_s^{(k-1)}|^2 \, ds \right] $$
$$ \leq \quad \beta^2 \int_0^t \mathbb{E}\left[ |X_s^{(k)} - X_s^{(k-1)}|^2 \right] ds. $$

The variance rule for the stochastic integral gives

$$ \mathbb{E}\left[ \left( \int_0^t [\sigma(s, X_s^{(k)}) - \sigma(s, X_s^{(k-1)})] \, dB_s \right)^2 \right] $$
$$ = \quad \int_0^t \mathbb{E}\left( [\sigma(s, X_s^{(k)}) - \sigma(s, X_s^{(k-1)})]^2 \right) ds $$
$$ \leq \quad \beta^2 \int_0^t \mathbb{E}\left[ |X_s^{(k)} - X_s^{(k-1)}|^2 \right] ds. $$

Combining these estimates, we see that there exists $\lambda < \infty$ such that for all $0 \leq t \leq 1$ and positive integers $k$,

$$ \mathbb{E}\left[ |X_t^{(k+1)} - X_t^k|^2 \right] \leq \frac{\lambda^{k+1} \, t^{k+1}}{(k + 1)!}. $$

We then define $X_t = \lim_k X_t^{(k)}$; as before, we do this for dyadic $t$ as an $L^2$ limit and extend it to other $t$ by continuity. This gives a solution.

### PDF page 122 (book page 116)

If the Lipschitz condition holds only locally, then we can use this argument to show that there exists a stopping time $T$ with $\mathbb{P}\{T > 0\} = 1$ such that $X_t, 0 \leq t < T$ satisfies the equation. In the random case the time $T$ for which the solution is valid is a random variable.

## 3.6 Covariation and the product rule

Suppose $X_t, Y_t$ satisfy

$$ dX_t = H_t \, dt + A_t \, dB_t, \quad dY_t = K_t \, dt + C_t \, dB_t. \tag{3.24} $$

Here $B_t$ is the same standard Brownian motion in both equations. As before, the covariation process is defined by

$$ \langle X, Y \rangle_t = \lim_{n \to \infty} \sum_{j \leq tn} \left[ X\left(\frac{j}{n}\right) - X\left(\frac{j-1}{n}\right) \right] \left[ Y\left(\frac{j}{n}\right) - Y\left(\frac{j-1}{n}\right) \right]. $$

Using the formal rules for stochastic calculus we get

$$ [dX_t] \, [dY_t] \quad = \quad [H_t \, dt + A_t \, dB_t] \, [K_t \, dt + C_t \, dB_t] $$
$$ = \quad A_t \, C_t \, dt + O((dt)^2) + O((dt)(dB_t)). $$

This indeed shows what happens and we get

$$ \langle X, Y \rangle_t = \int_0^t A_s \, C_s \, ds, $$

or in differential form,

$$ d\langle X, Y \rangle_t = A_t \, C_t \, dt. $$

The product rule for the usual derivative can be written in differential form as

$$ d(fg) = f \, dg + g \, df = fg' \, dt + f'g \, dt. $$

It can be obtained formally by writing

$$ d(fg) \quad = \quad f(t + dt) \, g(t + dt) - f(t) \, g(t) $$
$$ = \quad [f(t + dt) - f(t)] \, g(t + dt) + f(t) \, [g(t + dt) - g(t)] $$
$$ = \quad (df)g + (dg)f + (df)(dg). $$

### PDF page 123 (book page 117)

Since $df = f'dt, dg = g'dt$ and $df \, dg = O((dt)^2)$, we get the usual product formula.

If $X_t, Y_t$ are process as above, then when we take the stochastic differential $d(X_t Y_t)$ we get in the same way

$$ d(X_t Y_t) = X_t \, dY_t + Y_t \, dX_t + (dX_t) \, (dY_t). $$

However, the $(dX_t) \, (dY_t)$ term does not vanish, but rather equals $d\langle X, Y \rangle_t$. This gives the stochastic product rule.

**Theorem 3.6.1** (Stochastic product rule). *If $X_t, Y_t$ satisfy (3.24), then*

$$ d(X_t Y_t) = X_t \, dY_t + Y_t \, dX_t + d\langle X, Y \rangle_t. $$

*In other words,*

$$ X_t Y_t \quad = \quad X_0 \, Y_0 + \int_0^t X_s \, dY_s + \int_0^t Y_s \, dX_s + \int_0^t d\langle XY \rangle_s $$
$$ = \quad X_0 \, Y_0 + \int_0^t [X_s \, K_s + Y_s \, H_s + A_s \, C_s] \, ds $$
$$ + \int_0^t [X_s \, C_s + Y_s \, A_s] \, dB_s. $$

**Example 3.6.1.** Suppose $B_t$ is a standard Brownian motion and $X_t$ is the geometric Brownian motion satisfying

$$ dX_t = m \, X_t \, dt + \sigma \, X_t \, dB_t. $$

Then in the notation of (3.24), $H_t = m \, X_t$ and $A_t = \sigma \, X_t$. If we set $Y_t = B_t$, then $K_t = 0, C_t = 1$. Therefore,

$$ d(B_t X_t) \quad = \quad B_t \, dX_t + X_t \, dB_t + d\langle B, X \rangle_t $$
$$ = \quad B_t \, [m \, X_t \, dt + \sigma \, X_t \, dB_t] + X_t \, dB_t + \sigma \, X_t \, dt $$
$$ = \quad X_t \, [(m \, B_t + \sigma) \, dt + (\sigma \, B_t + 1) \, dB_t]. $$

## 3.7 Several Brownian motions

Up to this point, we have integrated with respect to a single Brownian motion. Extending the definitions to several Brownian motions is straightforward.

### PDF page 124 (book page 118)

Suppose that $B_t^1, \ldots, B_t^d$ are independent Brownian motions with respect to the filtration $\{\mathcal{F}_t\}$, and that $A_t^1, \ldots, A_t^d$ are adapted processes. We write

$$ dX_t = H_t \, dt + \sum_{j=1}^d A_t^j \, dB_t^j, $$

to mean

$$ X_t = X_0 + \int_0^t H_s \, ds + \sum_{j=1}^d \int_0^t A_s^j \, dB_s^j. $$

The covariation process can be computed if we remember the rule

$$ \langle B^i, B^j \rangle = 0, \quad i \neq j. $$

In particular, if

$$ Y_t = Y_0 + \int_0^t K_s \, ds + \sum_{j=1}^d \int_0^t C_s^j \, dB_s^j, $$

then

$$ d\langle X, Y \rangle_t = \sum_{j=1}^d A_t^j \, C_t^j \, dt. $$

Itô's formula for several processes can be obtained by expanding in a Taylor approximation. As before, we need the first order term in the time variable and all second order terms in the space variables. We state the theorem; the proof is essentially the same as for the previous version. The reader may note that this version includes all the previous versions as special cases, so we call this the final form. If $f : [0, \infty) \times \mathbb{R}^d \to \mathbb{R}$ is a function, we write

$$ \dot{f}(t, \mathbf{x}) = \partial_t f(t, \mathbf{x}), \quad \partial_j f(t, \mathbf{x}) = \partial_{x_j} f(t, \mathbf{x}), \quad \partial_{jk} f(t, \mathbf{x}) = \partial_{x_j x_k} f(t, \mathbf{x}). $$

If $\mathbf{X}_t = (X_t^1, \ldots, X_t^n)$ we write

$$ \nabla f(t, \mathbf{X}_t) \cdot d\mathbf{X}_t = \sum_{k=1}^n \partial_k f(t, \mathbf{X}_t) \, dX_t^k. $$

**Theorem 3.7.1** (Itô's formula, final form)**.** *Suppose $B_t^1, \ldots, B_t^d$ are independent standard Brownian motions, and $X_t^1, \ldots, X_t^n$ are processes satisfying*

$$ dX_t^k = H_t^k \, dt + \sum_{i=1}^d A_t^{i,k} \, dB_t^i. $$

### PDF page 125 (book page 119)

*Suppose $f(t, \mathbf{x}), t \geq 0, \mathbf{x} \in \mathbb{R}^n$, is a function that is $C^1$ in $t$ and $C^2$ in $\mathbf{x} = (x_1, \ldots, x_n)$. Then, if $\mathbf{X}_t = (X_t^1, \ldots, X_t^n)$,*

$$ df(t, \mathbf{X}_t) = \dot{f}(t, \mathbf{X}_t) \, dt + \nabla f(t, \mathbf{X}_t) \cdot d\mathbf{X}_t $$

$$ + \frac{1}{2} \sum_{j=1}^n \sum_{k=1}^n \partial_{jk} f(t, \mathbf{X}_t) \, d\langle X^j, X^k \rangle_t. $$

*In other words,*

$$ f(t, \mathbf{X}_t) - f(0, \mathbf{X}_0) = \sum_{i=1}^d \int_0^t \left[ \sum_{k=1}^n \partial_k f(s, \mathbf{X}_s) \, A_s^{i,k} \right] dB_s^i $$

$$ + \int_0^t \left[ \dot{f}(s, \mathbf{X}_s) + \left( \sum_{k=1}^n \partial_k f(s, \mathbf{X}_s) \, H_s^k \right) \right. $$

$$ \left. + \left( \frac{1}{2} \sum_{i=1}^d \sum_{j=1}^n \sum_{k=1}^n \partial_{jk} f(s, \mathbf{X}_s) \, A_s^{i,j} \, A_s^{i,k} \right) \right] dt $$

If $f(t, x)$ is $C^2$ only in an open subset $U \subset \mathbb{R}^n$, we can give a local form of this theorem as in Theorem 3.4.3 to see that the conclusion holds until the first time that $\mathbf{X}_t$ leaves $U$. Since it comes up often, we state a particular case of this theorem. The *Laplacian* of a function $f : \mathbb{R}^d \to \mathbb{R}$ is defined by

$$ \nabla^2 f(\mathbf{x}) = \sum_{j=1}^d \partial_{jj} f(\mathbf{x}). $$

Other standard notations for $\nabla^2$ are $\Delta$ and $\nabla \cdot \nabla$. In the statement below the gradient $\nabla$ and the Laplacian $\nabla^2$ are taken with respect to the $\mathbf{x}$ variable only.

**Theorem 3.7.2.** *Suppose $B_t = (B_t^1, \ldots, B_t^d)$ is a standard Brownian motion in $\mathbb{R}^d$. Then if $f : [0, \infty) \times \mathbb{R}^d$ is $C^1$ in $t$ and $C^2$ in $\mathbf{x} \in \mathbb{R}^d$, then*

$$ df(t, B_t) = \nabla f(t, B_t) \cdot dB_t + \left[ \dot{f}(t, B_t) + \frac{1}{2} \nabla^2 f(t, B_t) \right] dt $$

A function $f$ is *harmonic* if $\nabla^2 f = 0$. There is a close relationship between Brownian motion, martingales, and harmonic functions that we discuss in Chapter 8.

### PDF page 126 (book page 120)

## 3.8 Exercises

**Exercise 3.1.** Suppose $A_t$ is a simple process with $|A_t| \leq C$ for all $t$. Let

$$ Z_t = \int_0^t A_s \, dB_s. $$

Show that

$$ \mathbb{E}\left[ Z_t^4 \right] \leq 4 \, C^4 \, t^2. $$

Hint: We may assume $C = 1$. By conditioning with respect to $\mathcal{F}_t$ show that if $s, t > 0$,

$$ \mathbb{E}\left[ Z_{t+s}^4 \right] \leq \mathbb{E}\left[ Z_t^4 \right] + s^2 + 2 \sqrt{\mathbb{E}[Z_t^4]} \, s. $$

**Exercise 3.2.** Use Itô's formula to find the stochastic differential $f(t, B_t)$ where $B_t$ is a standard Brownian motion and

1. $f(t, x) = \sin x$;

2. $f(t, x) = e^{-t} \, (x/t)^2$

3. Repeat these exercises for $f(t, X_t)$ where

$$ dX_t = X_t \, [m \, dt + \sigma \, dB_t]. $$

**Exercise 3.3.** Suppose an asset follows the following geometric SDE,

$$ dX_t = 4 \, X_t \, dt + X_t \, dB_t. $$

1. Write the exact solution of this equation. In other words, find $X_t$ as a function of $B_t$.

2. Suppose $X_0 = 2$. What is the probability that $X_1 > 8$?

3. Suppose $X_0 = 1$. What is the probability that $X_2 < 6$?

4. Suppose $X_0 = 4.4565$. What is the probability that $X_t < 0$ for some $2 < t < 5$?.

### PDF page 127 (book page 121)

**Exercise 3.4.** Show that if $B_t$ is a standard Brownian motion, $A_t$ is a simple process, and

$$ Z_t = \int_0^t A_s \, dB_s, $$

then

$$ M_t = Z_t^2 - \langle Z \rangle_t $$

is a martingale.

**Exercise 3.5.** Suppose that two assets $X_t, Y_t$ follow the SDEs

$$ dX_t = X_t \, [\mu_1 \, dt + \sigma_1 \, dB_t], $$

$$ dY_t = Y_t \, [\mu_2 \, dt + \sigma_2 \, dB_t], $$

where $B_t$ is a standard Brownian motion. Suppose also that $X_0 = Y_0 = 1$.

1. Let $Z_t = X_t Y_t$. Give the SDE satisfied by $Z_t$; in other words write an expression for $dZ_t$ in terms of $Z_t, \mu_1, \mu_2, \sigma_1, \sigma_1$.

2. Does there exist a function $f : \mathbb{R} \to \mathbb{R}$ such that $f(X_t) = B_t$ for all $t$?

3. Does there exist a function $g : \mathbb{R} \to \mathbb{R}$ such that $g(Z_t) = B_t$ for all $t$?

**Exercise 3.6.** Suppose $B_t$ is a standard Brownian motion and $X_t$ satisfies

$$ dX_t = X_t^2 \, dt + X_t \, dB_t. $$

For each of the following find $A_t, C_t$ such that

$$ d\langle Y \rangle_t = A_t \, dt, \quad d\langle Y, X \rangle_t = C_t \, dt. $$

1. $Y_t = B_t$.

2. $Y_t = X_t^3$.

3.
$$ Y_t = \exp \left\{ \int_0^t (X_s^2 + 1) \, ds \right\}. $$

**Exercise 3.7.** Consider the geometric SDE

$$ dX_t = X_t[ -2 \, dt + 2 \, dB_t]. $$

Use the stochastic Euler's method to do Monte Carlo simulations for $X_t, 0 \le t \le 2$ assuming $X_0 = 1$. Use $\Delta t = .01$.

### PDF page 128 (book page 122)

1. Graph at least one of your simulations.

2. Use the simulation to estimate the probability that $X_2 \ge 3$. Do at least 1000 simulations.

3. Compute the exact probability (up to at least three decimal places) that $X_2 \ge 3$ and compare this to your simulations.

**Exercise 3.8.** Suppose $f(t)$ is a (nonrandom) continuously differentiable function of $t$ and $B_t$ is a standard Brownian motion. Justify the integration by parts formula

$$ \int_r^s f(t) \, dB_t = f(s) \, B_s - f(r) \, B_r - \int_r^s B_t \, f'(t) \, dt. $$

(Hint: write the left-hand side as a limit of simple process approximations and do "summation by parts" on the approximations.) Explain why $\int_r^s f(t) \, dB_t$ has a normal distribution.

**Exercise 3.9.** Let $m = 1, \sigma = 2, \Delta t = 1/1000$ and simulate geometric Brownian motion

$$ dX_t = X_t \, dt + 2 \, X_t \, dB_t, \quad X_0 = 1, $$

using both (3.17) and (3.18). Be sure that the same sequence of normal random variables $N_1, N_2, \ldots$ is used for (3.17) and (3.16). Run the simulation at least 20 times and compare the values of $X_{1/4}, X_{1/2}, X_{3/4}, X_1$ obtained from the two formulas.

**Exercise 3.10.** Suppose that $X_t$ satisfies the SDE

$$ dX_t = X_t \, [(1/2) \, dt + dB_t], \quad X_0 = 2 $$

Let

$$ M = \max_{0 \le t \le 1} X_t. $$

1. Find the density of $M$.

2. Find the probability that $M \ge 4$.

Hint: Write $X_t = f(B_t)$ for an appropriate function.

### PDF page 129 (book page 123)

**Exercise 3.11.** Suppose $Z_t, t \in \mathcal{D}$ are defined and there exists $c < \infty$, $\alpha < \infty$, $\beta > 0$ such that for all $s, t \in \mathcal{D}$

$$ \mathbb{E}\left[ |Z_t - Z_s|^\alpha \right] \le c \, |t - s|^{1+\beta}. $$

Let $\epsilon = \beta/(2\alpha)$.

- Show that

$$ \mathbb{P}\{ \exists s \in \mathcal{D}_n : |Z_{s+2^{-n}} - Z_s| \ge 2^{-n\epsilon} \} \le c \, 2^{-n\beta/2}. $$

- Show that with probability one, for all $n$ sufficiently large and all $s \in \mathcal{D}_n$,
$$ |Z_{s+2^{-n}} - Z_s| \le 2^{-n\epsilon}. $$

- Show that with probability one, there exists $C$ such that for all $s, t \in \mathcal{D}$,
$$ |Z_s - Z_t| \le C \, |s - t|^\epsilon. $$

### PDF page 130 (book page 124)
*(Blank page.)*

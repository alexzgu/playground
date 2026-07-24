# Chapter 4 — More stochastic calculus
*(PDF pages 131–150; book pages 125–144)*

### PDF page 131 (book page 125)
# Chapter 4 — More stochastic calculus

**4.1 Martingales and local martingales**

In the last chapter we defined

$$ Z_t = \int_0^t A_s \, dB_s, $$

where $B_t$ is a standard Brownian motion and $A_s$ is a continuous or piecewise continuous process. If

$$ \int_0^t \mathbb{E}[A_s^2] \, ds < \infty $$

for each $t$, then $Z_t$ is a square integrable martingale. However, our next example will show that if this inequality does not hold, the stochastic integral might not be a martingale. Our example is a modification of the martingale betting strategy from Section 1.2. In that example, we beat a fair game by doubling our bet until we won. We recall that if $W_n$ denotes the winnings after $n$ plays, then $\mathbb{E}[W_n] = 0$, but with probability one $W_\infty = 1$. In order to beat the game, we had to allow for arbitrarily large numbers of plays of the game until we won. In continuous time, one can do the same idea, but adapt it so that we guarantee to win by time 1.

**Example 4.1.1.** (Martingale betting strategy revisited) We will consider

$$ Z_t = \int_0^t A_s \, dB_s $$

### PDF page 132 (book page 126)
with a betting strategy $A_s$ that changes only at times $t_0 < t_1 < t_2 < \cdots < 1$ where

$$ t_n = 1 - 2^{-n}. $$

We start by setting $A_t = 1$ for $0 \leq t < 1/2$. Then $Z_{1/2} = B_{1/2}$. Note that

$$ \mathbb{P}\{Z_{1/2} \geq 1\} = \mathbb{P}\{B_{1/2} \geq 1\} = \mathbb{P}\{B_1 \geq \sqrt{2}\} = 1 - \Phi(\sqrt{2}) =: q > 0. $$

If $Z_{1/2} \geq 1$, we stop, that is, we set $A_t = 0$ for $1/2 \leq t \leq 1$. If $Z_{1/2} < 1$, let $x = 1 - Z_{1/2} > 0$. Define $a$ by the formula

$$ \mathbb{P}\{a[B_{3/4} - B_{1/2}] \geq x\} = q. $$

We set $A_t = a$ for $1/2 \leq t < 3/4$. Note that we only need to know $Z_{1/2}$ to determine $a$ and hence $a$ is $\mathcal{F}_{1/2}$-measurable. Also, if $a[B_{3/4} - B_{1/2}] \geq x$, then

$$ Z_{3/4} = \int_0^{3/4} A_s \, dB_s = Z_{1/2} + a[B_{3/4} - B_{1/2}] \geq 1. $$

Therefore,

$$ \mathbb{P}\{Z_{3/4} \geq 1 \mid Z_{1/2} < 1\} = q, $$

and hence

$$ \mathbb{P}\{Z_{3/4} < 1\} = (1 - q)^2. $$

If $Z_{3/4} \geq 1$, we set $A_t = 0$ for $3/4 \leq t \leq 1$. Otherwise, we proceed as above. At each time $t_n$ we adjust the bet so that

$$ \mathbb{P}\{Z_{t_{n+1}} \geq 1 \mid Z_{t_n} < 1\} = q, $$

and hence

$$ \mathbb{P}\{Z_{t_n} < 1\} \leq (1 - q)^n. $$

Using this strategy, with probability one $Z_1 \geq 1$, and hence, $\mathbb{E}[Z_1] \geq 1$. Therefore, $Z_t$ is not a martingale. Our choice of strategy used discontinuous bets, but it is not difficult to adapt this example so that $t \mapsto A_t$ is a continuous function except at the one time at which the bet changes to zero.

Although the stochastic integral may not be a martingale, it is almost a martingale in the sense that one needs to make the bets arbitrarily large to find a way to change the expectation. The next definition makes precise the idea of a process that is a martingale "if it is stopped before the values get big".

### PDF page 133 (book page 127)

**Definition** A continuous process $M_t$ adapted to the filtration $\{\mathcal{F}_t\}$ is called a *local martingale* on $[0, T)$ if there exists an increasing sequence of stopping times

$$ \tau_1 \leq \tau_2 \leq \tau_3 \leq \cdots $$

such that with probability one

$$ \lim_{j\to\infty} \tau_j = T, $$

and for each $j$,

$$ M_t^{(j)} = M_{t\wedge\tau_j}, $$

is a martingale.

In the case of the stochastic integral

$$ Z_t = \int_0^t A_s \, dB_s, $$

we let $\{\tau_j\}$ be the stopping times,

$$ \tau_j = \inf\left\{ t : \langle Z \rangle_t = \int_0^t A_s^2 \, ds = j \right\}. $$

Then for each $j$, $M_t^{(j)}$ is a square integrable martingale. Therefore, $Z_t$ is a local martingale on $[0, T)$ where

$$ T = \inf\left\{ t : \int_0^t A_s^2 \, ds = \infty \right\}. $$

The stochastic integral $Z_t$ is not defined after time $T$. Note that if $s \mapsto A_s$ is continuous for all $s \in [0, \infty)$, then $T = \infty$.

More generally, suppose that

$$ dX_t = R_t \, dt + A_t \, dB_t. $$

If $R_t \neq 0$, then $X_t$ is not a martingale. In other words, if $X_t$ is to be a martingale we need $R_t \equiv 0$. However, as we have just shown, it is possible for $R_t \equiv 0$ but $X_t$ to not be a martingale. It is a local martingale in this case. In an abuse of terminology, it is standard to refer to $A_t \, dB_t$ as the "martingale part" of $dX_t$ even though one should say the "local martingale part".

For continuous martingales, we have the optional sampling theorem which states under certain circumstances that one cannot beat a fair game. The next theorem includes two versions which are the most useful for applications.

### PDF page 134 (book page 128)

**Theorem 4.1.1** (Optional Sampling Theorem)**.** *Suppose $Z_t$ is a continuous martingale and $T$ is a stopping time, both with respect to the filtration $\{\mathcal{F}_t\}$.*

- *If $M_t = Z_{t\wedge T}$, then $M_t$ is a continuous martingale with respect to $\{\mathcal{F}_t\}$. In particular, $\mathbb{E}[Z_{t\wedge T}] = \mathbb{E}[Z_0]$.*

- *Suppose there exists $C < \infty$ such that for all $t$, $\mathbb{E}[Z_{t\wedge T}^2] \leq C$. Then if $\mathbb{P}\{T < \infty\} = 1$, $\mathbb{E}[Z_T] = \mathbb{E}[Z_0]$.*

**Example 4.1.2.** Suppose $Z_t$ is a continuous martingale with $Z_0 = 0$. Suppose that $a, b > 0$ and let

$$ T = \inf\{t : Z_t = -a \text{ or } Z_t = b\}. $$

Suppose that $\mathbb{P}\{T < \infty\} = 1$, which happens, for example, if $Z_t$ is a standard Brownian motion. Then $Z_{t\wedge T}$ is a bounded martingale and hence

$$ 0 = \mathbb{E}[Z_0] = \mathbb{E}[Z_T] = -a\, \mathbb{P}\{Z_T = a\} + b\, \mathbb{P}\{Z_T = b\}. $$

By solving, we get

$$ \mathbb{P}\{Z_T = b\} = \frac{a}{a + b}, $$

which is the gambler's ruin estimate for continuous martingales.

---

Results about continuous martingales can be deduced from corresponding results about discrete-time martingales. If $Z_t$ is a continuous martingale and

$$ D_n = \left\{ \frac{k}{2^n} : k = 0, 1, \ldots \right\}, $$

then $Z_t, t \in D_n$ is a discrete-time martingale. If $T_n$ is a stopping time taking values in $D_n$, then $Z_{t\wedge T_n}$ is also a martingale.

For more general $T$, we define $T_n$ by

$$ T_n = \frac{k}{2^n} \quad \text{if} \quad \frac{k-1}{2^n} \leq T < \frac{k}{2^n}, \quad k = 1, 2, \ldots, n2^n, $$

$$ T_n = n \quad \text{if} \quad T \geq n, $$

Suppose $s < t$ and let $s_n, t_n$ denote the smallest element of $D_n$ greater than or equal to $s, t$, respectively. If $A$ is an $\mathcal{F}_s$-measurable event, then

### PDF page 135 (book page 129)

it is also $\mathcal{F}_{s_n}$ measurable, and since $Z_{r\wedge T_n}, r \in D_n$ is a discrete-time martingale,

$$ \mathbb{E}\left[ 1_A \, Z_{s_n\wedge T_n} \right] = \mathbb{E}\left[ 1_A \, Z_{t_n\wedge T_n} \right]. $$

Since $Z$ has continuous paths, we know that as $n \to \infty$,

$$ Z_{s_n\wedge T_n} \to Z_{s\wedge T}, \quad Z_{t_n\wedge T_n} \to Z_{t\wedge T}. $$

In general, if $X_n$ is a sequence of random variables converging to $X$, we cannot conclude that $\mathbb{E}[X_n] \to \mathbb{E}[X]$. However, this will hold if the sequence $\{X_n\}$ is *uniformly integrable*, that is, if for every $\epsilon > 0$, there exists $K < \infty$ such that for all $n$,

$$ \mathbb{E}\left[ |X_n| \, 1\{|X_n| \geq K\} \right] < \epsilon. $$

(We leave this as an exercise or the reader can check a book on measure-theoretic probability.)

**Lemma 4.1.2.** *For every positive integer $m$, the collection of random variables $\{Z_{T_n}\}$ where $n$ ranges over all positive integers, $T$ ranges over all stopping times with $T \leq m$, and $T_n$ is defined as above, is uniformly integrable.*

*Proof.* Let $T$ be a stopping time with $T \leq m$ and $n$ a positive integer. Note that $N_t = |Z_t|, t \in D_n$ is a submartingale. Let $K > 0$ and let $\tau_n = \tau_{n,K}$ be the first $t \in D_n$ such that $N_t \geq K$. If $t \in D_n$, let $A_t = A_{t,n}$ be the event $\{\tau_n = t\}$. Since $N_t$ is a discrete-time submartingale, if $t \leq m$,

$$ \mathbb{E}\left[ N_m \, 1_{A_t} \right] \geq \mathbb{E}\left[ N_{T_n} \, 1_{A_t} \right]. $$

By summing over $t \in D_n, t \leq m$, we see that

$$ \mathbb{E}\left[ N_{T_n} \, J_{n,K} \right] \leq \mathbb{E}\left[ N_m \, J_{n,K} \right]. $$

where $J_{n,K} = 1\{\tau_n \leq m\}$. As $n \to \infty$. the random variables $J_{n,K}$ converge monotonically to

$$ J_{\infty,K} = 1\left\{ \max_{0\leq s\leq t} N_s > K \right\}. $$

Therefore, for each $K < \infty$,

$$ \mathbb{E}\left[ N_{T_n} \, 1\{N_{T_n} > K\} \right] \leq \mathbb{E}\left[ N_{m\wedge T_n} \, J_{\infty,K} \right] \leq \mathbb{E}\left[ |Z_m| \, J_{\infty,K} \right]. $$

### PDF page 136 (book page 130)

Note that the right-hand side is independent of $T$ and $n$. As $K \to \infty$, $J_{\infty,K} \to 0$, and since $Z_m$ is integrable,

$$ \lim_{K \to \infty} \mathbb{E}\left[|Z_m|\, J_{\infty,K}\right] = 0. $$

$\square$

Using the lemma, we now conclude

$$ \mathbb{E}\left[1_A\, Z_{s \wedge T}\right] = \mathbb{E}\left[1_A\, Z_{t \wedge T}\right]. $$

A sufficient condition for uniform integrability of $\{X_n\}$ is the existence of $C < \infty$ such that $\mathbb{E}[X_n^2] \leq C$ for all $n$. Indeed,

$$ \mathbb{E}\left[|X_n|\, 1\{|X_n| \geq K\}\right] \leq K^{-1}\, \mathbb{E}\left[\, |X_n|^2\, 1\{|X_n| \geq K\}\right] \leq C/K. $$

In particular, if $\mathbb{E}[Z_{t \wedge T}^2] \leq C$ for all $t$ and $\mathbb{P}\{T < \infty\} = 1$, then $Z_{n \wedge T} \to Z_T$ with probability one and uniform integrability implies that

$$ \mathbb{E}[Z_T] = \lim_{n \to \infty} \mathbb{E}[Z_{n \wedge T}] = \lim_{n \to \infty} \mathbb{E}[Z_0] = \mathbb{E}[Z_0]. $$

Two other theorems that extend almost immediately to the continuous martingale setting are the following. The proofs are essentially the same as for their discrete counterparts.

**Theorem 4.1.3.** *(Martingale Convergence Theorem) Suppose $Z_t$ is a continuous martingale and there exists $C < \infty$ such that $\mathbb{E}\left[|Z_t|\right] \leq C$ for all $t$. Then there exists a random variable $Z_\infty$ such that with probability one*

$$ \lim_{t \to \infty} Z_t = Z_\infty. $$

**Theorem 4.1.4.** *(Maximal inequality). Suppose $Z_t$ is a continuous square integrable martingale, and let*

$$ N_t = \max_{0 \leq s \leq t} |Z_t|. $$

*Then for every $a > 0$,*

$$ \mathbb{P}\{N_t \geq a\} \leq \frac{\mathbb{E}[Z_t^2]}{a^2}. $$

### PDF page 137 (book page 131)

**4.2 An example: the Bessel process**

The Bessel process with parameter $a$ is the solution to the SDE

$$ dX_t = \frac{a}{X_t}\, dt + dB_t, \quad X_0 = x_0 > 0. $$

If we choose $a = (d-1)/2$, this is called the Bessel-$d$ process and is related to $d$-dimensional Brownian motion (see Exercise 4.4). Let $T_\epsilon = \inf\{t : X_t \leq \epsilon\}$. There is no problem finding a solution to this equation for $t < T_\epsilon$, and hence it is well defined for $t < T$ where

$$ T = T_0 = \inf\{t : X_t = 0\}. $$

At time $T$ the equation is ill-defined so we will not consider the process for $t > T$. If $a > 0$, then when $X_t$ gets close to $0$, there is a strong drift away from the origin. It is not obvious whether or not this is strong enough to keep the diffusion from reaching the origin.

Suppose that $0 < r < R < \infty$ and let

$$ \tau = \tau(r, R) = \inf\{t : X_t = r \text{ or } X_t = R\}. $$

For $r \leq x \leq R$, let

$$ \phi(x) = \mathbb{P}\{X_\tau = R \mid X_0 = x\}. $$

We will use Itô's formula to compute $\phi$. Note that $\phi(r) = 0, \phi(R) = 1$. Let $J$ denote the indicator function of the event $\{X_\tau = R\}$ and let

$$ M_t = E[J \mid \mathcal{F}_t]. $$

The tower property for conditional expectation implies that $M_t$ is a martingale; indeed, if $s < t$,

$$ E[M_t \mid \mathcal{F}_s] = E[\, E(J \mid \mathcal{F}_t) \mid \mathcal{F}_s] = E[J \mid \mathcal{F}_s] = M_s. $$

The Markovian nature of the diffusion $X$ implies that

$$ E[J \mid \mathcal{F}_t] = \phi(X_{t \wedge \tau}). $$

In other words, if $\tau \leq t$, then we already know whether or not $\{X_\tau = R\}$. However, if $\tau > t$, the only useful information in $\mathcal{F}_t$ for predicting if $X_\tau = R$ is $X_t$, and the conditional probability is the probability that this occurs given

### PDF page 138 (book page 132)

that the process started at $X_t$. The upshot of this reasoning is that $\phi(X_{t \wedge \tau})$ must be a martingale. Itô's formula (see Theorem 3.4.3) gives for $t < T$,

$$ \begin{aligned} d\phi(X_t) &= \phi'(X_t)\, dX_t + \frac{1}{2}\, \phi''(X_t)\, d\langle X \rangle_t \\ &= \left[\frac{a\, \phi'(X_t)}{X_t} + \frac{\phi''(X_t)}{2}\right] dt + \phi'(X_t)\, dB_t. \end{aligned} $$

If this is to be a martingale, the $dt$ term must vanish at all times. The way to guarantee this is to choose $\phi$ to satisfy the ordinary differential equation (ODE)

$$ x\, \phi''(x) + 2a\, \phi'(x) = 0. $$

Solving such equations is standard (and this one is particularly easy for one can solve the first-order equation for $g(x) = \phi'(x)$), and the solutions are of the form

$$ \phi(x) = c_1 + c_2\, x^{1-2a}, \quad a \neq \frac{1}{2}, $$

$$ \phi(x) = c_1 + c_2\, \log x, \quad a = \frac{1}{2}, $$

where $c_1, c_2$ are arbitrary constants. The boundary conditions $\phi(r) = 0, \phi(R) = 1$ determine the constants giving

$$ \phi(x) = \frac{x^{1-2a} - r^{1-2a}}{R^{1-2a} - r^{1-2a}}, \quad a \neq \frac{1}{2}, \tag{4.1} $$

$$ \phi(x) = \frac{\log x - \log r}{\log R - \log r}, \quad a = \frac{1}{2}. \tag{4.2} $$

We now answer the question that we posed.

**Proposition 4.2.1.** *If $a \geq 1/2$, then $\mathbb{P}\{T = \infty\} = 1$, that is, with probability one the Bessel process never reaches zero. If $a < 1/2$, then $\mathbb{P}\{T < \infty\} = 1$.*

*Proof.* Assume $X_0 = x < R$ and let $\tau(r, R)$ be defined as above. If $T < \infty$, then there must be $R < \infty$ such that $X_{\tau(r,R)} = r$ for all $r > 0$. Using the form of the probability in (4.1) and (4.2), we can see that

$$ \lim_{r \to 0} \mathbb{P}\{X_{\tau(r,R)} = r\} = \begin{cases} 0 & \text{if } a \geq 1/2 \\ 1 - (x/R)^{1-2a} & \text{if } a < 1/2 \end{cases} $$

$\square$

### PDF page 139 (book page 133)

The alert reader will note that we cheated a little bit in our derivation of $\phi$ because we assumed that $\phi$ was $C^2$. After assuming this, we obtained a differential equation and found what $\phi$ should be. To finish a proof, we can start with $\phi$ as defined in (4.1) or (4.2), and use Itô's formula to show that $M_t = \phi(X_{t\wedge\tau})$ is a continuous martingale. Since it is also bounded, we can use the optional sampling theorem to conclude that

$$ \phi(x_0) = \mathbb{E}[M_0] = \mathbb{E}[M_\tau] = \mathbb{P}\{X_\tau = R\}. $$

This kind of argument is often done in stochastic calculus where one first assumes sufficient smoothness of a a [sic] function in order to use Itô's formula and obtain a differential equation for the function. Once the differential equation is solved, one can go back and redo the Itô's formula calculation rigorously.

## 4.3 Feynman-Kac formula

Suppose that the price of a stock follows a geometric Brownian motion

$$ dX_t = m\,X_t\,dt + \sigma\,X_t\,dB_t. \tag{4.3} $$

Suppose that at some future time $T$ we have an option to buy a share of the stock at price $S$. We will exercise the option only if $X_T \geq S$ and the value of the option at time $T$ is $F(X_T)$ where

$$ F(x) = (x - S)_+ = \max\{x - S, 0\}. $$

Suppose that there is an inflation rate of $r$ so that $x$ dollars at time $t$ in future is worth only $e^{-rt}x$ in current dollars. Let $\phi(t, x)$ be the expected value of this option at time $t$, measured in dollars at time $t$, given that the current price of the stock is $x$,

$$ \phi(t, x) = \mathbb{E}\left[e^{-r(T-t)}F(X_T) \mid X_t = x\right]. \tag{4.4} $$

The Feynman-Kac formula gives a PDE for this quantity.

### PDF page 140 (book page 134)

Since it is not any harder, we generalize and assume that $X_t$ satisfies the SDE

$$ dX_t = m(t, X_t)\,dt + \sigma(t, X_t)\,dB_t, \quad X_0 = x_0, $$

and that there is a payoff $F(X_T)$ at some future time $T$. Suppose also that there is an inflation rate $r(t, x)$ so that if $R_t$ denotes the value at time $t$ of $R_0$ dollars at time 0,

$$ dR_t = r(t, X_t)\,R_t\,dt, $$

$$ R_t = R_0\,\exp\left\{\int_0^t r(s, X_s)\,ds\right\}. $$

If $\phi(t, x)$ denote the expected value of the payoff in time $t$ dollars given $X_t = x$, then

$$ \phi(t, x) = \mathbb{E}\left[\exp\left\{-\int_t^T r(s, X_s)\,ds\right\}\,F(X_T) \mid X_t = x\right]. \tag{4.5} $$

We will use Itô's formula to derive a PDE for $\phi$ under the assumption that $\phi$ is $C^1$ in $t$ and $C^2$ in $x$.

Let

$$ M_t = E\left[R_T^{-1}\,F(X_T) \mid \mathcal{F}_t\right]. $$

The tower property for conditional expectation implies that if $s < t$,

$$ E[M_t \mid \mathcal{F}_s] = E[E(M_T \mid \mathcal{F}_t) \mid \mathcal{F}_s] = E[M_T \mid \mathcal{F}_s] = M_s. $$

In other words, $M_t$ is a martingale. Since $R_t$ is $\mathcal{F}_t$-measurable, we see that

$$ M_t = R_t^{-1}\,E\left[\exp\left\{-\int_t^T r(s, X_s)\,ds\right\}\,F(X_T) \mid \mathcal{F}_t\right]. $$

However, since $X_t$ is a Markov process, the only relevant information in $\mathcal{F}_t$ is given by the value $X_t$. Hence, by the definition of $\phi$,

$$ M_t = R_t^{-1}\,\phi(t, X_t). \tag{4.6} $$

Our conclusion is that $M_t$ as given in (4.6) must be a martingale. Itô's formula gives

$$ d\phi(t, X_t) = \partial_t\phi(t, X_t)\,dt + \partial_x\phi(t, X_t)\,dX_t + \frac{1}{2}\,\partial_{xx}\,\phi(t, X_t)\,d\langle X\rangle_t. $$

### PDF page 141 (book page 135)

In particular,

$$ d\phi(t, X_t) = H_t\,dt + A_t\,dB_t, $$

with

$$ H_t = \partial_t\phi(t, X_t) + m(t, X_t)\,\partial_x\phi(t, X_t) + \frac{1}{2}\,\sigma(t, X_t)^2\,\partial_{xx}\phi(t, X_t), $$

$$ A_t = \sigma(t, X_t)\,\partial_x\phi(t, X_t). $$

Since $\langle R\rangle_t = 0$, the stochastic product rule implies that

$$ d[R_t^{-1}\phi(t, X_t)] = R_t^{-1}\,d\phi(t, X_t) + \phi(t, X_t)\,d[R_t^{-1}], $$

and hence the $dt$ term of $d[R_t^{-1}\phi(t, X_t)]$ is $R_t^{-1}$ times

$$ -r(t, X_t)\,\phi(t, X_t) + \partial_t\phi(t, X_t) + m(t, X_t)\,\partial_x\phi(t, X_t) $$

$$ +\frac{1}{2}\,\sigma(t, X_t)^2\,\partial_{xx}\phi(t, X_t). $$

Since $M_t$ is a martingale, the $dt$ term must be identically zero. This happens only if for all $t, x$,

$$ -r(t, x)\,\phi(t, x) + \partial_t\phi(t, x) + m(t, x)\,\partial_x\phi(t, x) $$

$$ +\frac{1}{2}\,\sigma(t, x)^2\,\partial_{xx}\phi(t, x) = 0. $$

We have derived the following.[^1]

**Theorem 4.3.1** (Feynman-Kac formula)**.** *Suppose $X_t$ satisfies*

$$ dX_t = m(t, X_t)\,dt + \sigma(t, X_t)\,dB_t, \quad X_0 = x_0, $$

*and $r(t, x) \geq 0$ is a discounting rate. Suppose a payoff $F$ at time $T$ is given with $\mathbb{E}[|F(X_T)|] < \infty$. If $\phi(t, x), 0 \leq t \leq T$ is defined as in (4.5), and $\phi(t, x)$ is $C^1$ in $t$ and $C^2$ in $x$, then $\phi(t, x)$ satisfies the PDE*

$$ \partial_t\phi(t, x) = -m(t, x)\,\partial_x\phi(t, x) $$

$$ -\frac{1}{2}\,\sigma(t, x)^2\,\partial_{xx}\phi(t, x) + r(t, x)\,\phi(t, x), $$

*for $0 \leq t < T$, with terminal condition $\phi(T, x) = F(x)$.*

[^1]: One of our assumptions in Theorem 4.3.1 is that $\phi$ is sufficiently differentiable. One can give conditions on the coefficients and payoff function $F$ under which this holds, and they include the examples that we give, but the general theory is beyond what we will discuss in this book. See I. Karatzas and S. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd. ed, Springer (1991), Section 5.7.B for a discussion of this.

### PDF page 142 (book page 136)

**Example 4.3.1.** Suppose $X_t$ satisfies (4.3). Then $m(t, x) = mx, \sigma(t, x) = \sigma x$ and $\phi$ is as given in (4.4). The Feynman-Kac formula gives

$$ \partial_t\phi = r\,\phi - mx\,\partial_x\phi - \frac{\sigma^2\,x^2}{2}\,\partial_{xx}\phi. \tag{4.7} $$

This is a version of the *Black-Scholes PDE*. We will return to this later.

Let us give a somewhat different derivation of the Feynman-Kac formula using the generator. Again, suppose that $X_t$ satisfies

$$ dX_t = m(t, X_t)\,dt + \sigma(t, X_t)\,dB_t, $$

and that $F$ is a function that does not grow too quickly. Let

$$ f(t, x) = \mathbb{E}\left[F(X_T) \mid X_t = x\right]. $$

Let $r(t) \geq 0$ be a discount rate which for ease we will assume is a deterministic function of time, and

$$ R_t = R_0\,\exp\left\{\int_0^t r(s)\,ds\right\}. $$

Let

$$ \phi(t, x) = \mathbb{E}\left[(R_t/R_T)\,F(X_T) \mid X_t = x\right] = \exp\left\{-\int_t^T r(s)\,ds\right\}\,f(t, x) $$

Recall that

$$ \partial_t f(t, x) = -L_x^t f(t, x), $$

where $L^t$ is the generator

$$ L^t h(x) = m(t, x)\,h'(x) + \frac{\sigma(t, x)}{2}\,h''(x). $$

Therefore,

$$ \begin{aligned} \partial_t\phi(t, x) &= r(t)\,\exp\left\{-\int_t^T r(s)\,ds\right\}\,f(t, x) \\ &\quad -\exp\left\{-\int_t^T r(s)\,ds\right\}\,L_x^t f(t, x) \\ &= r(t)\,\phi(t, x) - L_x^t\phi(t, x) \\ &= r(t)\,\phi(t, x) - m(t, x)\,\partial_x\phi(t, x) - \frac{\sigma^2(t, x)}{2}\,\partial_{xx}\phi(t.x), \end{aligned} $$

which is the Feynman-Kac PDE.

### PDF page 143 (book page 137)

## 4.4 Binomial approximations

In the next few sections we will be considering the SDE

$$ dX_t = m(t, X_t)\,dt + \sigma(t, X_t)\,dB_t. $$

We will give some heuristic derivations based on discrete approximations. Recall that the Euler method to sample from this equation uses the rule

$$ X(t + \Delta t) = X(t) + m(t, X(t))\,\Delta t + \sigma(t, X(t))\,\sqrt{\Delta t}\,Z $$

where $Z \sim N(0, 1)$. Here we wish to consider some *binomial* sampling schemes, that is, schemes such that given $X(t)$, $X(t + \Delta t)$ takes one of two values.

If $X_t$ is Brownian motion with drift zero and variance $\sigma^2$,

$$ dX_t = \sigma\,dB_t, $$

then the binomial scheme is approximation by random walk,

$$ \mathbb{P}\{X(t + \Delta t) - X(t) = \sigma\,\sqrt{\Delta t} \mid X(t)\} $$

$$ = \mathbb{P}\{X(t + \Delta t) - X(t) = -\sigma\,\sqrt{\Delta t} \mid X(t)\} = \frac{1}{2}. $$

In this case the values of $X(k\Delta t)$ lie in the lattice of points

$$ \left\{\ldots, -2\sigma\sqrt{\Delta t}, -\sigma\sqrt{\Delta t}, 0, \sigma\sqrt{\Delta t}, 2\sigma\sqrt{\Delta t}, \ldots\right\}. $$

If $m \equiv 0$ and $\sigma(t, x)$ is not constant, we can change this rule to

$$ \mathbb{P}\{X(t + \Delta t) - X(t) = \pm\sigma(t, X(t))\,\sqrt{\Delta t} \mid X(t)\} = \frac{1}{2}, $$

but then the values of $X(t)$ do not stay in a lattice.

Suppose $\sigma$ is constant, but $m$ varies,

$$ dX_t = m(t, X_t)\,dt + \sigma\,dB_t. $$

There are two reasonable ways to incorporate drift in this binomial model. One is to use a version of the Euler's method and set

$$ \mathbb{P}\{X(t + \Delta t) - X(t) = m(t, X_t)\,\Delta t \pm \sigma\,\sqrt{\Delta t} \mid X(t)\} = \frac{1}{2}, $$

### PDF page 144 (book page 138)

for which it is immediate that

$$ \begin{aligned} &E\left[X(t + \Delta t) - X(t) \mid \mathcal{F}_t\right] \\ &= E\left[X(t + \Delta t) - X(t) \mid X(t)\right] = m(t, X_t)\,\Delta t. \end{aligned} \tag{4.8} $$

This method has the disadvantage that we do not stay on a lattice of points. Another approach is to always make the jumps $\pm\sigma\sqrt{\Delta t}$ but to change the probabilities based on the drift. In particular, we let

$$ \mathbb{P}\{X(t + \Delta t) - X(t) = \sigma\,\sqrt{\Delta t} \mid X(t)\} = \frac{1}{2}\left[1 + \frac{m(t, X_t)}{\sigma}\,\sqrt{\Delta t}\right], $$

$$ \mathbb{P}\{X(t + \Delta t) - X(t) = -\sigma\,\sqrt{\Delta t} \mid X(t)\} = \frac{1}{2}\left[1 - \frac{m(t, X_t)}{\sigma}\,\sqrt{\Delta t}\right]. $$

The probabilities are chosen so that (4.8) holds for this scheme as well. These two binomial methods illustrate the two main ways to incorporate a drift term (in other words, to turn a fair game into an unfair game):

- Choose an increment with mean zero and then add a small amount to it.

- Change the probabilities of the increment so that it does not have mean zero.

**Example 4.4.1.** We will use the latter rule to sample from Brownian motion with constant drift $m \neq 0$ and $\sigma^2 = 1$. Our procedure for simulating uses

$$ \mathbb{P}\{X(t + \Delta t) - X(t) = \pm\sqrt{\Delta t} \mid X(t)\} = \frac{1}{2}\left[1 \pm m\,\sqrt{\Delta t}\right]. \tag{4.9} $$

Suppose that $\Delta t = 1/N$ for some large integer $N$, and let us consider the distribution of $X(1)$. There are $2^N$ possible paths that the discrete process can take which can be represented by

$$ \omega = (a_1, a_2, \ldots, a_N) $$

where $a_j = +1$ or $-1$ depending on whether that step goes up or down. Let $J = J(\omega)$ denote the number of $+1$'s, and define $r$ by $J = (N/2) + r\sqrt{N}$. Note that the position at time 1 is

$$ \begin{aligned} X(1) &= \sqrt{\Delta t}\,[a_1 + \cdots + a_N] \\ &= J\sqrt{\Delta t} - (N - J)\sqrt{\Delta t} \\ &= 2r\sqrt{N}\sqrt{\Delta t} = 2r. \end{aligned} $$

### PDF page 145 (book page 139)

For each $\omega$, the probability of its occurring is

$$ q(\omega) = \left(\frac{1}{2}\right)^N \left[1 + m\sqrt{\Delta t}\right]^J \left[1 - m\sqrt{\Delta t}\right]^{N-J}. $$

If $m$ were 0, then the probability would be be [sic] just $(1/2)^N$. Therefore, the *ratio* of the probabilities for $m \neq 0$ to $m = 0$ is

$$ \left[1 + \frac{m}{\sqrt{N}}\right]^J \left[1 - \frac{m}{\sqrt{N}}\right]^{N-J} $$

$$ = \left[1 - \frac{m^2}{N}\right]^{N/2} \left[1 + \frac{m}{\sqrt{N}}\right]^{r\sqrt{N}} \left[1 - \frac{m}{\sqrt{N}}\right]^{-r\sqrt{N}}. $$

Using the relation $\left(1 + \frac{a}{N}\right)^N \sim e^a$, we see that the limit of the right-hand side as $N \to \infty$ is

$$ e^{-m^2/2}\, e^{2rm} = e^{mX(1)}\, e^{-m^2/2}. $$

Given this, we see that in order to sample from a Brownian motion with drift, we could first sample from a Brownian motion without drift and then weight the samples by the factor $e^{mX(1)}\, e^{-m^2/2}$. We will show how to do this directly in Section 5.2.

As one more application of binomial approximations, we will give a heuristic argument for the following theorem.

**Theorem 4.4.1.** *Suppose that*

$$ dX_t = m(X_t)\, dt + \sigma\, dB_t, $$

*where $m$ is continuously differentiable, and let $p(t,x)$ denote the density of $X_t$ at time $t$. Then*

$$ \partial_t p(t, x) = L^*_x p(t, x), $$

*where*

$$
\begin{aligned}
L^* f(x) &= -[m(x)\, f(x)]' + \frac{\sigma^2}{2}\, f''(x) \\
&= -m'(x)\, f(x) - m(x)\, f'(x) + \frac{\sigma^2}{2}\, f''(x).
\end{aligned}
$$

—

### PDF page 146 (book page 140)

Recall that

$$ L f(x) = m(x)\, f'(x) + \frac{\sigma^2}{2}\, f''(x). $$

If $m$ is constant, then as we saw before, one obtains $L^*$ from $L$ by just changing the sign of the drift. For varying $m$ we get another term. We will derive the expression for $L^*$ by using the binomial approximation

$$ \mathbb{P}\{X(t + \Delta t) - X(t) = \pm\sigma\sqrt{\Delta t} \mid X(t)\} = \frac{1}{2}\left[1 \pm \frac{m(X_t)}{\sigma}\sqrt{\Delta t}\right]. $$

Let $\epsilon = \sqrt{\Delta t}, \epsilon^2 = \Delta t$. To be at position $x = k\epsilon$ at time $t + \epsilon^2$, one must be at position $x \pm \sigma\epsilon$ at time $t$. This gives the relation

$$ p(t + \epsilon^2, x) = p(t, x - \sigma\epsilon)\, \frac{1}{2}\left[1 + \frac{m(x - \sigma\epsilon)\, \epsilon}{\sigma}\right] $$

$$ + p(t, x + \sigma\epsilon)\, \frac{1}{2}\left[1 - \frac{m(x + \sigma\epsilon)}{\sigma}\, \epsilon\right]. \tag{4.10} $$

We know that

$$ p(t + \epsilon^2, x) = p(t, x) + \partial_t p(t, x)\, \epsilon^2 + o(\epsilon^2). \tag{4.11} $$

The definition of the derivative (see Section 2.10.1), implies that

$$ \frac{p(t, x + \sigma\epsilon) + p(t, x - \sigma\epsilon)}{2} = p(t, x) + \frac{\sigma^2\, \epsilon^2}{2}\, \partial_{xx} p(t, x) + o(\epsilon^2). $$

$$ p(t, x \pm \sigma\epsilon) = p(t, x) \pm \partial_x p(t, x)\, \sigma\epsilon + o(\epsilon), $$

$$ m(x \pm \sigma\epsilon) = m(x) \pm m'(x)\, \sigma\epsilon + o(\epsilon), $$

Plugging in, we see that the right-hand side of (4.10) equals

$$ p(t, x) + \epsilon^2 \left[\frac{\sigma^2}{2}\, \partial_{xx} p(t, x) - m'(x)\, p(t, x) - m(x)\, \partial_x p(t, x)\right] + o(\epsilon^2). $$

Comparing this with (4.11) gives us the result.

### PDF page 147 (book page 141)

One can also derive this result by considering $L^*$ as the adjoint of $L$. In other words, $L^*$ is defined by

$$ \int_{-\infty}^{\infty} L^* f(x)\, g(x)\, dx = \int_{-\infty}^{\infty} f(x)\, L g(x)\, dx. $$

If

$$ L g(x) = m(x)\, g'(x) + \frac{\sigma^2}{2} g''(x), $$

then integration by parts gives

$$ L^* f(x) = -[m(x)\, f(x)]' + \frac{\sigma^2}{2} f''(x). $$

# 4.5 Continuous martingales

Earlier we made the comment that Brownian motion is the only continuous martingale. We will make this explicit in this section.

**Proposition 4.5.1.** *Suppose that $M_t$ is a continuous martingale with respect to a filtration $\{\mathcal{F}_t\}$ with $M_0 = 0$, and suppose that the quadratic variation of $M_t$ is the same as that of standard Brownian motion,*

$$ \langle M \rangle_t = \lim_{n \to \infty} \sum_{j < 2^n t} \left[ M\left(\frac{j+1}{2^n}\right) - M\left(\frac{j}{2^n}\right)\right]^2 = t. $$

*Then every $\lambda \in \mathbb{R}$,*

$$ \mathbb{E}\left[\exp\{i\lambda M_t\}\right] = e^{-\lambda^2 t/2}. $$

*Sketch of proof.* Fix $\lambda$ and let $f(x) = e^{i\lambda x}$. Note that the derivatives of $f$ are uniformly bounded in $x$. Following the proof of Itô's formula we can show that

$$ f(M_t) - f(M_0) = N_t + \frac{1}{2}\int_0^t f''(M_s)\, ds = N_t - \frac{\lambda^2}{2}\int_0^t f(M_s)\, ds, $$

where $N_t$ is a martingale. In particular, if $r < t$,

$$ \mathbb{E}[f(M_t) - f(M_r)] = \frac{1}{2}\, \mathbb{E}\left[\int_r^t f''(M_s)\, ds\right] = -\frac{\lambda^2}{2}\int_r^t \mathbb{E}[f(M_s)]\, ds. $$

### PDF page 148 (book page 142)

If we let $G(t) = \mathbb{E}[f(M_t)]$, we get the equation

$$ G'(t) = -\frac{\lambda^2}{2}\, G(t), \quad G(0) = 1, $$

which has solution $G(t) = e^{-\lambda^2 t/2}$. $\square$

**Theorem 4.5.2.** *Suppose that $M_t$ is a continuous martingale with respect to a filtration $\{\mathcal{F}_t\}$ with $M_0 = 0$, and suppose that the quadratic variation of $M_t$ is the same as that of standard Brownian motion*

$$ \langle M \rangle_t = \lim_{n \to \infty} \sum_{j < 2^n t} \left[ M\left( \frac{j+1}{2^n} \right) - M\left( \frac{j}{2^n} \right) \right]^2 = t. $$

*Then $M_t$ is a standard Brownian motion.*

*Proof.* We need to show that $M_t$ satisfies the conditions of a standard Brownian motion. We are given $M_0 = 0$ and that $t \mapsto M_t$ is continuous, so we only need to establish independent, normal increments. One way to express both of these conditions is to say that for every $s < t$, the conditional distribution of $M_t - M_s$ given $\mathcal{F}_s$ is $N(0, t - s)$. But the proposition above shows that for every $\lambda$,

$$ E\left( e^{i\lambda(M_t - M_s)} \mid \mathcal{F}_s \right) = e^{-\lambda^2(t-s)/2}. $$

Since the characteristic function determines the distribution, we are finished. $\square$

---

This theorem can be extended to say that any continuous martingale is a time change of a Brownian motion. To be precise, suppose that $M_t$ is a continuous martingale. The quadratic variation can be defined as the process $\langle M \rangle_t$ such that $M_t^2 - \langle M \rangle_t$ is a local martingale. Let

$$ \tau_s = \inf\{t : \langle M \rangle_t = s\}. $$

Then $Y_s = M_{\tau_s}$ is a continuous martingale whose quadratic variation is the same as standard Brownian motion. Hence $Y_s$ is a standard Brownian motion.

---

### PDF page 149 (book page 143)

**4.6 Exercises**

**Exercise 4.1.** A process $X_t$ satisfies the Ornstein-Uhlenbeck SDE if

$$ dX_t = mX_t\, dt + dB_t, $$

where $m \in \mathbb{R}$ and $B_t$ is a standard Brownian motion. Suppose that $X_0 = 1$, $R > 1$ and $T = T_R$ is the first time that $X_t = R$ or $X_t = 0$.

1. Find a function $F$ with $F(0) = 0$ and $F(x) > 0$ for $x > 0$ such that $F(X_{t \wedge T})$ is a martingale. (You may leave your answer in terms of a definite integral.)

2. Find the probability that $X_T = R$. You can write the answer in terms of the function $F$.

3. For what values of $m$ is it true that

$$ \lim_{R \to \infty} \mathbb{P}\{X_T = R\} = 0 \ ? $$

**Exercise 4.2.** Suppose $B_t$ is a standard Brownian motion and $X_t$ satisfies the SDE

$$ dX_t = a \cot(X_t)\, dt + dB_t, \quad X_0 = x_0 \in (0, \pi/2), $$

where $a \in \mathbb{R}$. For $\epsilon > 0$, let

$$ T_\epsilon = \min\{t : \sin(X_t) = \sin \epsilon\}, $$

$$ T = T_{0+} = \min\left\{t : X_t \in \{0, \pi\}\right\} = \min\{t : \sin(X_t) = 0\}, $$

We will only consider the process $X_t$ for $t \leq T$. Let

$$ \tau = \min\{t : X_t = \pi/2\}. $$

1. Find a function $F(x)$ that is positive for $0 < x < \pi/2$ with $F(\pi/2) = 0$ and such that $M_t = F(X_{t \wedge T})$ is a local martingale for $t < T$. (It suffices to write $F$ in the form

$$ F(x) = \int_x^{\pi/2} g(y)\, dy, $$

### PDF page 150 (book page 144)

where $g$ is an explicit function.)

2. For which values of $a$ is

$$ F(0+) = \lim_{\epsilon \downarrow 0} F(\epsilon) < \infty \ ? $$

3. Assume that $0 < \epsilon < x_0 < \pi/2$ and let

$$ q(x_0, \epsilon) = \mathbb{P}\{T_\epsilon < \tau\}. $$

Write $q(x_0, \epsilon)$ explicitly in terms of $F$.

4. For whch [sic] values of $a$ is it the case that

$$ \lim_{\epsilon \downarrow 0} q(x_0, \epsilon) = 0 \ ? $$

**Exercise 4.3.** Suppose $B_t$ is a standard Brownian motion and let $X_t = e^{B_t} + 2$. Let

$$ \phi(t, x) = \mathbb{E}\left[ e^{-2(T-t)} \left(X_T^3 - 1\right) e^{-X_T} \mid X_t = x \right], \quad 0 < t < T. $$

Use the Feynman-Kac theorem to find a second-order PDE that $\phi$ satisfies.

**Exercise 4.4.** Suppose $B_1^1, \ldots, B_t^d$ are independent standard Brownian motions and let

$$ X_t = \sqrt{(B_t^1)^2 + \cdots + (B_t^d)^2}. $$

1. Use Itô's formula to show that

$$ dX_t = \frac{a}{X_t}\, dt + dM_t, $$

where $a = (d-1)/2$ and $M_t$ is a continuous martingale satisfying

$$ dM_t = \sum_{j=1}^{d} A_t^j\, dB_t^j, $$

for suitable processes $A_t^j$.

2. Show that $\langle M \rangle_t = t$.

3. Explain why $M_t$ is a standard Brownian motion. (Hint: use Proposition 4.5.1.)

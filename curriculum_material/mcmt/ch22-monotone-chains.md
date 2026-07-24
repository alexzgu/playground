# Chapter 22 — Monotone Chains
*(PDF pages 321–338; book pages 305–322)*

### PDF page 321 (book page 305)

CHAPTER 22

# Chapter 22 — Monotone Chains

**22.1. Introduction**

Given that you can simulate a Markov chain, but have no a priori bound on the mixing time, how can you estimate the mixing time?

This is difficult in general, but a good method exists for *monotone* chains. Suppose that $(\mathcal{X}, \preceq)$ is a partially ordered state space. A coupling $\{(X_t, Y_t)\}$ on $\mathcal{X} \times \mathcal{X}$ is called **monotone** if $X_t \preceq Y_t$ whenever $X_0 \preceq Y_0$. A **monotone chain** is one for which there exists a monotone coupling for any two ordered initial states. For many monotone chains, there exist top and bottom states, and one can construct grand couplings such that all chains have coupled when the chains started from top and bottom states collide.

In such cases, if $\tau$ is the time when the extreme states have coupled, then

$$ \bar{d}(t) \le \mathbf{P}\{\tau > t\}, $$

so tail estimates for $\tau$ yield bounds on mixing times. This tail probability can be estimated by simulation. Without monotonicity, estimates are needed for coupling times for many pairs of initial states.

We give a few examples.

EXAMPLE 22.1. Let $\mathcal{X} = \{0, 1, 2, \ldots, n\}$, and consider the symmetric nearest-neighbor walk with holding at $0$ and $n$:

$$ P(j,k) = \frac{1}{2} \quad \text{if and only if } |j - k| = 1 \text{ or } j = k = 0 \text{ or } j = k = n \,. $$

As discussed in Example 5.1, we can start two walkers at $j < k$, chains $(X_t)$ and $(Y_t)$, both with transition matrix $P$, so that $X_t \le Y_t$ always.

In fact, we can construct a grand coupling $(X_t^k)$, where $k \in \{0, 1, \ldots, n\}$, so that $X_0^j = j$ and $X_t^j \le X_t^k$ always whenever $j \le k$. If $\tau$ is the time it takes for $X_t^0$ to meet $X_t^n$, then all the chains $(X_t^k)$ must agree at time $\tau$. Thus

$$ \bar{d}(t) \le \mathbf{P}\{\tau > t\} \,, $$

and bounds on the single coupling time $\tau$ bound the mixing time. Note the expected time for the top chain to hit $0$ is $O(n^2)$, which implies that $t_{\mathrm{mix}} = O(n^2)$.

EXAMPLE 22.2 (Ising Model). Consider Glauber dynamics for the Ising model on a finite graph $G = (V, E)$, introduced in Section 3.3. Simultaneously, for each starting state $\sigma \in \mathcal{X} = \{-1, 1\}^V$, we can construct Markov chains $(X_t^\sigma)$ evolving together. This is achieved as follows: Select the same vertex $v$ to update in each chain, and generate a single uniform $[0, 1]$ random variable $U$. The probability of

### PDF page 322 (book page 306)

updating to $+1$ at $v$ when in state $\theta$ is

$$ p(\theta, v) = \frac{1}{2} \left[ 1 + \tanh \left( \beta \sum_{w:w \sim v} \theta(w) \right) \right] . \tag{22.1} $$

Given the configuration $X_t^\sigma$, the configuration $X_{t+1}^\sigma$ is defined by updating the spin at $v$ to be $+1$ if

$$ 1 - U \le p(X_t^\sigma, v) \,, $$

and to be $-1$ otherwise. Since $p(\theta, v)$ is non-decreasing in $\theta$, the coupling is monotone. As before, when the chain started from all $+1$'s meets the chain started from all $-1$'s, all intermediate chains agree as well.

EXAMPLE 22.3 (Noisy Voter Model). This chain can be considered a linearization of the Glauber dynamics for the Ising model. For the Ising model, the chance of updating to a $+1$ at a given vertex depends exponentially on the total weight of the neighboring vertices. For the *noisy voter model*, the chance of updating to a $+1$ depends linearly on the weight of the neighbors.

Let the state space $\mathcal{X}$ be the set $\{-1, 1\}^V$, where $V$ are the vertices of a graph $(V, E)$. The *voter model* evolves as follows: a vertex $v$ is chosen uniformly at random, and a neighbor $w$ of $v$ is chosen uniformly among neighbors of $v$. If the chain is at state $\sigma$, then the new state $\sigma'$ agrees with $\sigma$ everywhere except possibly at $v$, where $\sigma'(v) = \sigma(w)$. That is, the new value at $v$ is taken from the previous value at $w$.

This chain has absorbing states at the all $-1$ and all $+1$ configurations. The noisy voter model updates at $v$ by choosing a neighbor and adopting its value with probability $p$, and by picking a random value (uniformly from $\{-1, 1\}$) with probability $1 - p$.

A grand coupling is constructed as follows: In all copies of the chain, pick the same vertex $v$ to update, and use the same $p$-coin toss to determine if the spin at $v$ will be chosen from a neighbor or randomized. In the case that a spin from neighbor $w$ is adopted, use the same neighbor $w$ for all chains. Otherwise, a single randomly chosen spin updates all chains simultaneously at $v$. If the initial state $\sigma$ dominates the initial state $\theta$, then at each subsequent time the chain started from $\sigma$ will dominate the chain started from $\theta$. When the chain started from the all $-1$ state meets the chain started from the all $1$ state, all intermediate chains will agree. Thus $\bar{d}(t)$ is again bounded by $\mathbf{P}\{\tau > t\}$, where $\tau$ is the coupling time of the extremal states.

**22.2. Stochastic Domination**

**22.2.1. Probabilities on $\mathbb{R}$.** Given two probability distributions $\mu$ and $\nu$ on $\mathbb{R}$, we say that $\nu$ **stochastically dominates** $\mu$ and write $\mu \preceq \nu$ if

$$ \mu(t, \infty) \le \nu(t, \infty) \quad \text{for all } t \in \mathbb{R} \,. $$

Similarly, we say that a random variable $Y$ stochastically dominates a random variable $X$ if $\mathbf{P}\{X > t\} \le \mathbf{P}\{Y > t\}$ for all $t$.

EXAMPLE 22.4. Suppose that $X$ and $Y$ are exponential random variables with means $a$ and $b$ respectively, with $a \le b$. Then

$$ \mathbf{P}\{X > t\} = e^{-t/a} \le e^{-t/b} = \mathbf{P}\{Y > t\}, $$

so $X \preceq Y$.

### PDF page 323 (book page 307)

LEMMA 22.5. *Let $\mu$ and $\nu$ be two probability measures on $\mathbb{R}$. The following are equivalent:*

(i) *$\mu \preceq \nu$.*
(ii) *There exists a pair of random variables $(X, Y)$, defined on a common probability space, so that the distribution of $X$ is $\mu$, the distribution of $Y$ is $\nu$, and $X \le Y$ with probability one.*
(iii) *For any $X$ and $Y$ with distributions $\mu$ and $\nu$, respectively, if $f$ is a continuous non-decreasing function, then*

$$ \mathbf{E}[f(X)] \le \mathbf{E}[f(Y)] \,, $$

*provided the expectations are defined.*

PROOF. (i) $\Rightarrow$ (ii). Suppose $\mu \preceq \nu$. Set

$$ \varphi_\mu(u) := \inf\{t \,:\, F_\mu(t) \ge u\}, $$

where $F_\mu(t) = \mu(-\infty, t]$ is the distribution function of $\mu$. The reader should check that $\varphi_\mu(u) \le x$ if and only if $u \le F_\mu(x)$. If $U$ is uniform on $(0, 1)$, then for $t \in \mathbb{R}$,

$$ \mathbf{P}\{\varphi_\mu(U) \le t\} = \mathbf{P}\{U \le F_\mu(t)\} = F_\mu(t) \,. $$

That is, $\varphi_\mu(U)$ has distribution $\mu$. We can define $\varphi_\nu$ similarly so that $\varphi_\nu(U)$ has distribution $\nu$.

Now let $U$ be uniform on $(0, 1)$, and let $(X, Y) = (\varphi_\mu(U), \varphi_\nu(U))$. From above, the marginal distributions of $X$ and $Y$ are $\mu$ and $\nu$, respectively. Also, since $\mu \preceq \nu$, it follows that

$$ \{t \,:\, F_\nu(t) \ge u\} \subseteq \{t \,:\, F_\mu(t) \ge u\}, $$

and so $\varphi_\mu(u) \le \varphi_\nu(u)$ for all $u \in (0, 1)$. It is immediate that $X \le Y$.

The implication (ii) $\Rightarrow$ (iii) is clear. To prove that (iii) $\Rightarrow$ (i), let $f_n$ be a continuous increasing function which vanishes on $(-\infty, t]$ and takes the value $1$ on $[t + 1/n, \infty)$. Then

$$ \mathbf{P}\{X \ge t + 1/n\} \le \mathbf{E}[f_n(X)] \le \mathbf{E}[f_n(Y)] \le \mathbf{P}\{Y > t\} \,. $$

Passing to the limit shows that $\mathbf{P}\{X > t\} \le \mathbf{P}\{Y > t\}$. $\blacksquare$

**22.2.2. Probabilities on Partially Ordered Sets.** Suppose now that $\mathcal{X}$ is a set with a partial order $\preceq$. We can generalize the definition of stochastic domination to probability measures $\mu$ and $\nu$ on $\mathcal{X}$. We use the property (iii) in Lemma 22.5 as the general definition. A real-valued function $f$ on $\mathcal{X}$ is **increasing** if $f(x) \le f(y)$ whenever $x \preceq y$.

For measures $\mu$ and $\nu$ on a partially ordered set $\mathcal{X}$, $\nu$ **stochastically dominates** $\mu$, written $\mu \preceq \nu$, if $E_\mu(f) \le E_\nu(f)$ for all increasing $f : \mathcal{X} \to \mathbb{R}$.

The following generalizes Lemma 22.5 from $\mathbb{R}$ to partially ordered sets.

THEOREM 22.6 (Strassen). *Suppose that $\mathcal{X}$ is a partially ordered finite set. Two probability measures $\mu$ and $\nu$ on $\mathcal{X}$ satisfy $\mu \preceq \nu$ if and only if there exists a $\mathcal{X} \times \mathcal{X}$-valued random element $(X, Y)$ such that $X$ has distribution $\mu$ and $Y$ has distribution $\nu$, and satisfying $\mathbf{P}\{X \preceq Y\} = 1$.*

The proof that the existence of a monotone coupling $X \preceq Y$ implies $\mu \preceq \nu$ is easy; in practice it is this implication which is useful. We include here the proof of this direction, and delay the proof of the other implication until Section 22.8.

### PDF page 324 (book page 308)

PROOF OF SUFFICIENCY IN THEOREM 22.6. Suppose that such a coupling $(X, Y)$ exists. Then for any increasing $f$, we have $f(X) \leq f(Y)$ and

$$ E_\mu(f) = \mathbf{E}[f(X)] \leq \mathbf{E}[f(Y)] = E_\nu(f) \, . $$

$\blacksquare$

**22.3. Definition and Examples of Monotone Markov Chains**

Let $\mathcal{X}$ be a finite set with a partial order, which we denote by $\preceq$. We say that a Markov chain $(X_t)$ on $\mathcal{X}$ with transition matrix $P$ is a **monotone chain** if $Pf$ is an increasing function whenever $f$ is increasing.

PROPOSITION 22.7. *The following conditions are equivalent:*

 (i) *$P$ is a monotone chain.*
 (ii) *If $\mu \preceq \nu$, then $\mu P \preceq \nu P$.*
 (iii) *For every pair of comparable states $x, y \in \mathcal{X}$ with $x \preceq y$, there exists a coupling $(X, Y)$ of $P(x, \cdot)$ with $P(y, \cdot)$ satisfying $X \preceq Y$.*

PROOF. (i) $\Rightarrow$ (ii). Let $f$ be an increasing function. Then $Pf$ is increasing, so

$$ (\mu P)f = \mu(Pf) \leq \nu(Pf) = (\nu P)f \, . $$

(ii) $\Rightarrow$ (iii). If $x \preceq y$, then $\delta_x P \preceq \delta_y P$. Theorem 22.6 yields the required coupling.

(iii) $\Rightarrow$ (i). Let $x \preceq y$, and let $(X, Y)$ be the coupling of $P(x, \cdot)$ with $P(y, \cdot)$ satisfying $X \preceq Y$. For increasing $f$,

$$ (Pf)(x) = \mathbf{E}f(X) \leq \mathbf{E}f(Y) = (Pf)(y) \, . $$

$\blacksquare$

EXAMPLE 22.8 (Random Walk on Path). Consider nearest-neighbor random walk on $\mathbb{Z}$ which moves up with probability $p$ and down with probability $1 - p$, and censors any attempted moves outside $\mathcal{X} = \{0, 1, \ldots, n\}$.

Let $f$ be increasing on $\{0, 1, \ldots, n\}$, and suppose $0 \leq x \leq y \leq n$.

$$
\begin{aligned}
Pf(x) &= (1 - p)f((x - 1) \vee 0) + pf((x + 1) \wedge n) \\
&\leq (1 - p)f((y - 1) \vee 0) + pf((y + 1) \wedge n) = Pf(y) \, ,
\end{aligned}
$$

so $P$ is monotone.

**22.3.1. General Spin systems.** Let $S$ be a finite totally ordered set, and denote by $-$ and $+$ the least and greatest elements of $S$, respectively; without loss of generality, we assume $S \subset \mathbb{R}$. We call an element of $S$ a **spin**. Suppose that $V$ is a finite set; $V$ will often be the vertex set of a finite graph. We will call the elements of $V$ **sites**. Suppose that $\mathcal{X} \subset S^V$, and let $\mu$ be a probability on $\mathcal{X}$. For a configuration $\sigma$, set

$$ \sigma_v^\bullet = \{\tau \in \mathcal{X} \, : \, \tau(w) = \sigma(w) \text{ for all } w \in V \setminus \{v\}\} \, , $$

the set of configurations which agree with $\sigma$ off site $v$. Let $\mu_v^\sigma$ be the probability distribution on $S$ defined as the projection at $v$ of $\mu$ conditioned on $\sigma_v^\bullet$:

$$ \mu_v^\sigma(s) = \frac{\mu(\{\tau \in \mathcal{X} \, : \, \tau(v) = s\} \cap \sigma_v^\bullet)}{\mu(\sigma_v^\bullet)} \, . $$

That is, $\mu_v^\sigma$ is the probability $\mu$ conditioned to agree with $\sigma$ off the site $v$. We write $P_v$ for the Markov chain which updates $\sigma$ at $v$ to a spin chosen from $\mu_v^\sigma$.

### PDF page 325 (book page 309)

The Glauber dynamics for $\mu$ is the Markov chain which evolves from the state $\sigma \in \mathcal{X}$ by selecting a site $v \in V$ uniformly at random, and then updates the value at $v$ by choosing according to the distribution $\mu_v^\sigma$. The transition matrix for this chain is $\frac{1}{|V|} \sum_{v \in V} P_v$.

We say that $\mu$ is a **monotone spin system** if $P_v$ is a monotone chain for all $v$.

EXAMPLE 22.9 (Ising Model). We saw in Example 22.2 that the Glauber dynamics for the Ising model has a monotone coupling when a vertex is chosen uniformly at random for updating. The same construction works for a specified update vertex, whence the Glauber chain is a monotone spin system.

EXAMPLE 22.10 (Hardcore model on bipartite graph). Let $G = (V, E)$ be a bipartite graph; the vertices are partitioned into *even* and *odd* sites so that no edge contains two even vertices or two odd vertices. Fix a positive $k$ such that

$$ \mathcal{X} = \{\omega \in \{0, 1\}^V \, : \, \sum_{v \in V} \omega(v) = k \, , \quad \text{and} \quad \omega(v)\omega(z) = 0 \text{ for all } \{v, z\} \in E\} $$

is not empty. A site $v$ in configuration $\omega$ with $\omega(v) = 1$ is called "occupied"; configurations prohibit two neighboring sites to both be occupied. The hardcore model with $k$ particles is the uniform distribution on $\mathcal{X}$.

Consider the following ordering on $\mathcal{X}$: declare $\omega \preceq \eta$ if $\omega(v) \leq \eta(v)$ at all even $v$ and $\omega(v) \geq \eta(v)$ at all odd $v$. This is a monotone spin system; see Exercise 22.5.

**22.4. Positive Correlations**

A probability distribution $\mu$ on the partially ordered set $\mathcal{X}$ has **positive correlations** if for all increasing functions $f, g$ we have

$$ \int_{\mathcal{X}} f(x)g(x)\mu(dx) \geq \int_{\mathcal{X}} f(x)\mu(dx) \int_{\mathcal{X}} g(x)\mu(dx) \, , \tag{22.2} $$

provided the integrals exist.

REMARK 22.11. We write the integral of $f$ against a general measure $\mu$ as $\int_{\mathcal{X}} f(x)\mu(dx)$. The reader unfamiliar with measure theory should substitute the sum $\sum_{x \in \mathcal{X}} f(x)\mu(x)$ for the integral in the case that $\mathcal{X}$ is a countable set, and $\int_{\mathcal{X}} f(x)\varphi(x)dx$ in the case where $\mathcal{X}$ is a region of Euclidean space and $\varphi$ is a probability density function supported on $\mathcal{X}$. All the proofs in this section remain valid after making these substitutions.

We will say that a chain with transition matrix $P$ and stationary distribution $\pi$ has positive correlations if $\pi$ has positive correlations.

LEMMA 22.12 (Chebyshev). *If $\mathcal{X}$ is totally ordered, then any probability measure $\mu$ on $\mathcal{X}$ has positive correlations.*

PROOF. This was an early application of a coupling argument. Given increasing functions $f$ and $g$ on $\mathcal{X}$, and independent random variables $X$ and $Y$ with distribution $\mu$, the events $\{f(X) \leq f(Y)\}$ and $\{g(X) \leq g(Y)\}$ coincide, hence

$$ [f(X) - f(Y)][g(X) - g(Y)] \geq 0 \, . $$

### PDF page 326 (book page 310)

Taking expectations shows that

$$
\begin{aligned}
0 \leq \mathbf{E}\,[(f(X) - f(Y))(g(X) - g(Y))] \\
= \mathbf{E}\,[f(X)g(X)] - \mathbf{E}\,[f(X)g(Y)] \\
- \mathbf{E}\,[f(Y)g(X)] + \mathbf{E}\,[f(Y)g(Y)] \, .
\end{aligned}
$$

Because $X$ and $Y$ both have the same distribution, the first and last terms are equal, and because $X$ and $Y$ are independent and have the same distribution, the two middle terms both equal $\mathbf{E}[f(X)]\mathbf{E}[g(X)]$. We conclude that

$$ \mathbf{E}[f(X)g(X)] \geq \mathbf{E}[f(X)]\mathbf{E}[g(X)] \, . $$

In different notation, this is (22.2). $\blacksquare$

Given partially ordered sets $\mathcal{X}_1, \ldots, \mathcal{X}_n$, we define the **coordinate-wise partial order** on $\mathcal{X}_1 \times \cdots \times \mathcal{X}_n$ to be the partial order $\preceq$ with $x \preceq y$ if $x_i \preceq y_i$ for all $i = 1, \ldots, n$.

LEMMA 22.13. *Let $\mathcal{X}$ and $\mathcal{Y}$ be partially ordered sets, and suppose that $\mu$ is a probability measure on $\mathcal{X}$ with positive correlations and $\nu$ is a probability measure on $\mathcal{Y}$ with positive correlations. If $\mathcal{X} \times \mathcal{Y}$ is given the coordinate-wise partial order then the product measure $\mu \times \nu$ on $\mathcal{X} \times \mathcal{Y}$ has positive correlations.*

PROOF. Let $f$ and $g$ be bounded increasing functions on the product space. Then for all $y \in \mathcal{Y}$ fixed, $x \mapsto f(x, y)$ and $x \mapsto g(x, y)$ are increasing. Thus, since $\mu$ has positive correlations on $\mathcal{X}$, for $y \in \mathcal{Y}$ fixed,

$$ \int_{\mathcal{X}} f(x, y)g(x, y)\mu(dx) \geq F(y)G(y) \, , \tag{22.3} $$

where

$$ F(y) := \int_{\mathcal{X}} f(x, y)\mu(dx) \quad \text{and} \quad G(y) := \int_{\mathcal{X}} g(x, y)\mu(dx) \, . $$

Integrating (22.3) shows that

$$ \iint_{\mathcal{X} \times \mathcal{Y}} f(x, y)g(x, y)(\mu \times \nu)(dx, dy) \geq \int_{\mathcal{Y}} F(y)G(y)\nu(dy) \, . \tag{22.4} $$

Observe that $F$ and $G$ are both increasing on $\mathcal{Y}$. Since $\nu$ has positive correlations on $\mathcal{Y}$,

$$
\begin{aligned}
\int_{\mathcal{Y}} F(y)G(y)\nu(dy) &\geq \int_{\mathcal{Y}} F(y)\nu(dy) \int_{\mathcal{Y}} G(y)\nu(dy) \\
&= \iint_{\mathcal{X} \times \mathcal{Y}} f(x, y)(\mu \times \nu)(dx, dy) \iint_{\mathcal{X} \times \mathcal{Y}} g(x, y)(\mu \times \nu)(dx, dy) \, . \tag{22.5}
\end{aligned}
$$

Putting together (22.5) and (22.4) shows that $\mu \times \nu$ has positive correlations. $\blacksquare$

The previous two lemmas and induction give:

LEMMA 22.14 (Harris Inequality). *Let $\mathcal{X} = \mathcal{X}_1 \times \cdots \times \mathcal{X}_n$, where each $\mathcal{X}_i$ is totally ordered. Using the coordinate-wise partial order on the product, any product probability on $\mathcal{X}$ has positive correlations.*

### PDF page 327 (book page 311)

EXAMPLE 22.15 (Ising model). Recall that the Ising model on $G = (V, E)$ is the probability distribution on $\mathcal{X} = \{-1, 1\}^V$ given by

$$ \mu(\sigma) = Z(\beta)^{-1} \exp\Big( \beta \sum_{\{v,w\} \in E} \sigma(v)\sigma(w) \Big), $$

where $Z(\beta)$ is a normalizing constant. Next we will show that the Harris inequality implies that $\mu$ has positive correlations. As shown in Section 3.3.5, the Glauber dynamics, when updating configuration $\sigma$ at $v$, has probability

$$ p(\sigma, v) = \frac{1}{2}\Big(1 + \tanh\big(\beta S(\sigma, v)\big)\Big) $$

of updating to a $+1$ spin, where $S(\sigma, v) = \sum_{u \,:\, \{u,v\} \in E} \sigma(u)$.

Since tanh is increasing, and $S(\sigma, v)$ is increasing in $\sigma$, it follows that $p(\sigma, v)$ is increasing in $\sigma$. This implies that this is a monotone system.

Let $v_1, \ldots, v_t$ be any sequence of vertices in $V$. Let $\Phi_s : \mathcal{X} \times [0, 1] \to \mathcal{X}$ be defined by

$$ \Phi_s(\sigma, u)(v) = \begin{cases} \sigma(v) & v \neq v_s \\ +1 & v = v_s \text{ and } u > 1 - p(\sigma, v_s) \\ -1 & v = v_s \text{ and } u \leq 1 - p(\sigma, v_s) \,. \end{cases} \tag{22.6} $$

If $U$ is uniform on $[0, 1]$, then the distribution of $\Phi_s(\sigma, U)$ is the same as the distribution of the state obtained by applying one Glauber update to $\sigma$ at vertex $v_s$. Define recursively $F_s(u_1, \ldots, u_s)$ by

$$ F_1(u_1) = \Phi_1(\sigma, u_1), $$
$$ F_s(u_1, \ldots, u_s) = \Phi_s(F_{s-1}(u_1, \ldots, u_{s-1}), u_s) \,. $$

By induction, if $(u_1, \ldots, u_t) \preceq (u_1', \ldots, u_t')$, then $F_t(u_1, \ldots, u_t) \preceq F_t(u_1', \ldots, u_t')$. If $U_1, \ldots, U_t$ are i.i.d. uniform $[0, 1]$ random variables, then the distribution $\mu_t$ of $F_t(U_1, \ldots, U_t)$ has the same distribution as applying Glauber updates sequentially at vertices $v_1, \ldots, v_t$.

Let $f, g$ be two increasing functions on $\mathcal{X}$. The compositions $f \circ F_t$ and $g \circ F_t$ are also increasing, so by Lemma 22.14,

$$ \int (f \cdot g)\, d\mu_t = \mathbf{E}_\sigma\left[ (f \circ F_t)(U_1, \ldots, U_t) \cdot (g \circ F_t)(U_1, \ldots, U_t) \right] $$
$$ \geq \mathbf{E}_\sigma\left[ (f \circ F_t)(U_1, \ldots, U_t) \right] \mathbf{E}_\sigma\left[ (g \circ F_t)(U_1, \ldots, U_t) \right] $$
$$ = \int f\, d\mu_t \int g\, d\mu_t \,. $$

Suppose that $v_1, \ldots, v_n$ enumerates the vertices $V$ in some order. Consider the Markov chain which in *one step* sequentially implements Glauber updates at $v_1, \ldots, v_n$. This is called *systematic scan*. This chain is irreducible, aperiodic, and has stationary distribution $\mu$. The distribution of $P(\sigma, \cdot)$ is $\mu_n$ defined above. We can conclude that for any increasing functions $f$ and $g$ on $\mathcal{X}$, if $X_t$ is this chain after $t$ steps,

$$ \mathbf{E}[f(X_t)g(X_t)] \geq \mathbf{E}[f(X_t)]\mathbf{E}[g(X_t)] \,. $$

By the Convergence Theorem (Theorem 4.9), letting $t \to \infty$,

$$ E_\mu(fg) \geq E_\mu(f)E_\mu(g) \,. $$

### PDF page 328 (book page 312)

In general, for any monotone chain which makes transitions only to comparable states, the stationary measure has positive correlations:

THEOREM 22.16. *Suppose that $P$ is a monotone, irreducible transition matrix with stationary distribution $\pi$, and that $x$ and $y$ are comparable whenever $P(x, y) > 0$. Then $\pi$ has positive correlations.*

The hypothesis in the above Theorem is satisfied in monotone spin systems and in the exclusion process studied in Chapter 23.

PROOF. Let $f$ and $g$ be non-negative increasing functions such that $E_\pi(f), E_\pi(g)$ and $E_\pi(fg)$ all exist. Suppose that $(X_0, X_1)$ are two steps of a stationary chain. Since $X_0$ and $X_1$ are comparable,

$$ [f(X_1) - f(X_0)] \cdot [g(X_1) - g(X_0)] \geq 0 \,, $$

and taking expectations shows that

$$ \int (fg)d\pi \geq \frac{1}{2} \left[ \mathbf{E}_\pi(g(X_0)f(X_1)) + \mathbf{E}_\pi(f(X_0)g(X_1)) \right] $$
$$ = \frac{1}{2} \left[ \int (g \cdot Pf)d\pi + \int (f \cdot Pg)d\pi \right] \,. \tag{22.7} $$

We show now by induction that

$$ E_\pi(fg) \geq 2^{-n} \sum_{k=0}^{n} \binom{n}{k} \int (P^k f \cdot P^{n-k} g)d\pi \,. \tag{22.8} $$

Suppose (22.8) holds for $n$. Note that applying (22.7) to the functions $P^k f$ and $P^{n-k}g$ (both increasing since $P$ is monotone) yields

$$ \int P^k f \cdot P^{n-k} g \, d\pi \geq \frac{1}{2} \left[ \int (P^{k+1}f \cdot P^{n-k}g)d\pi + \int (P^k f \cdot P^{n-k+1}g)d\pi \right] \,. $$

Using the induction hypothesis and the above inequality shows that

$$ E_\pi(fg) \geq \frac{1}{2^{n+1}} \left[ \sum_{k=0}^{n} \binom{n}{k} \int P^{k+1}f \cdot P^{n-k}g \, d\pi + \sum_{\ell=0}^{n} \binom{n}{\ell} \int P^\ell f \cdot P^{n+1-\ell}g \, d\pi \right] \,. $$

Changing the index to $\ell = k + 1$ in the first sum, and using the identity $\binom{n+1}{\ell} = \binom{n}{\ell} + \binom{n}{\ell-1}$ yields (22.8) with $n + 1$ replacing $n$.

If $\alpha_n(k) = \int (P^k f \cdot P^{n-k}g)d\pi$, then the right-hand side of (22.8) is the expectation of $\alpha_n$ with respect to a Binomial $(n, 2^{-1})$ distribution. By Chebyshev's inequality or the Central Limit Theorem,

$$ \sum_{|k - n/2| > n/4} 2^{-n} \binom{n}{k} \alpha_n(k) \to 0 $$

as $n \to \infty$. For $|k - n/2| \leq n/4$, we have $\alpha_n(k) \to E_\pi(f)E_\pi(g)$, by the Convergence Theorem. Thus, the right-hand side of (22.8) converges to $\int f\, d\pi \cdot \int g\, d\pi$, proving that $\pi$ has positive correlations.

$\blacksquare$

### PDF page 329 (book page 313)

**22.5. The Second Eigenfunction**

Sometimes one can guess the second eigenfunction and thereby determine the relaxation time for a chain. In that regard, the following lemmas for monotone chains are very useful.

LEMMA 22.17. *Suppose that $\mathcal{X}$ has a partial order and $P$ is a reversible monotone Markov chain on $\mathcal{X}$ with stationary distribution $\pi$. The second eigenvalue $\lambda_2$ has an increasing eigenfunction.*

PROOF. Suppose that $|\mathcal{X}| = n$. If $\lambda_2 = 0$, then the corresponding eigenfunction $f_2 \equiv 0$, so we are done. Suppose $\lambda_2 \neq 0$.

*Claim:* There is an increasing $f$ with $E_\pi(f) = 0$ and $\langle f, f_2 \rangle_\pi = 1$.

Any partial order can be extended to a total order (see Exercise 22.3). Thus, extend $(\mathcal{X}, \preceq)$ to a total order. Enumerate the states according to this order as $\{v_i\}_{i=1}^n$. Let $f(v_i) := i - c$, where $c = \sum_i i\pi(v_i)$. If $a_2 = \langle f, f_2 \rangle_\pi \neq 0$, we are done by rescaling, so assume that $a_2 = 0$. There exists $i$ with $f_2(v_i) \neq f_2(v_{i+1})$, since $f_2$ is orthogonal to $\mathbf{1}$. Set for small $\varepsilon$

$$ \tilde{f}(v) = \begin{cases} f(v) & v \neq v_i, v_{i+1} \\ f(v_i) + \frac{\varepsilon}{\pi(v_i)} & v = v_i \\ f(v_{i+1}) - \frac{\varepsilon}{\pi(v_{i+1})} & v = v_{i+1} \,. \end{cases} $$

Thus

$$ \langle \tilde{f}, f_2 \rangle_\pi = \langle f, f_2 \rangle_\pi + \varepsilon[f_2(v_i) - f_2(v_{i+1})] \neq 0 \,, $$

and $E_\pi(\tilde{f}) = 0$. This proves the claim.

We can write $f$ as a linear combination of eigenvectors $f = \sum_{i=2}^{n} a_i f_i$, where $a_2 = 1$. Iterating, we have

$$ \frac{P^{2t}f}{\lambda_2^{2t}} = f_2 + \sum_{i=3}^{n} a_i \left( \frac{\lambda_i}{\lambda_2} \right)^{2t} f_i \to f_2 \,. $$

Since $P^{2t}f$ is increasing for all $t$, the limit $f_2$ must also be increasing. $\blacksquare$

LEMMA 22.18. *Let $P$ be a reversible monotone chain such that $x$ and $y$ are comparable if $P(x, y) > 0$. If $P$ has a strictly increasing eigenfunction $f$, then $f$ corresponds to $\lambda_2$.*

PROOF. Since $P$ is monotone, $Pf = \lambda f$ is weakly increasing, so $\lambda \geq 0$. Therefore, $\lambda_2 \geq \lambda \geq 0$. If $\lambda_2 = 0$, then we are done; thus we assume that $\lambda_2 > 0$.

Let $g$ be any weakly increasing non-constant eigenfunction. Then

$$ E_\pi(f) = 0, \quad E_\pi(g) = 0 \,. $$

Since $f$ is strictly increasing, so is $f - \varepsilon g$ for some sufficiently small $\varepsilon > 0$. By Theorem 22.16,

$$ E_\pi((f - \varepsilon g)g) \geq E_\pi(f - \varepsilon g)E_\pi(g) \,, $$

implying that

$$ E_\pi(fg) - \varepsilon E_\pi(g^2) \geq E_\pi(f)E_\pi(g) - \varepsilon(E_\pi g)^2 = 0 \,. $$

Thus $E_\pi(fg) > 0$, so $f$ and $g$ correspond to the same eigenvalue $\lambda$. Lemma 22.17 guarantees there is a weakly increasing $g$ corresponding to $\lambda_2$; hence $f$ must also correspond to $\lambda_2$. $\blacksquare$

### PDF page 330 (book page 314)

EXAMPLE 22.19 (Ising on $n$-cycle). Let $P$ be the Glauber dynamics for the Ising model on the $n$-cycle. In this case, the probability of updating $\sigma$ at $k$ to $+1$ is

$$ p(\sigma, k) = \frac{1}{2} \left[ 1 + \tanh \left( \beta(\sigma(k-1) + \sigma(k+1)) \right) \right] , $$

where $k \pm 1$ are modulo $n$. The sum $s_k = \sigma(k-1) + \sigma(k+1)$ takes values in $\{-2, 0, 2\}$, and since $\tanh$ is an odd function, for $s \in \{-2, 0, 2\}$,

$$ \tanh(s\beta) = s \left[ \frac{1}{2} \tanh(2\beta) \right] . $$

Therefore, if $g_k(\sigma) = \sigma(k)$, then

$$ Pg_k(\sigma) = \left( 1 - \frac{1}{n} \right) g_k(\sigma) + \frac{1}{n} \tanh \left[ \beta(\sigma(k-1) + \sigma(k+1)) \right] $$
$$ = \left( 1 - \frac{1}{n} \right) g_k(\sigma) + \frac{1}{2n} \tanh(2\beta) \left( \sigma(k-1) + \sigma(k+1) \right) . $$

If $f = \sum_k g_k$, then summing the above identity over $k$ shows that

$$ Pf = \left( 1 - \frac{1 - \tanh(2\beta)}{n} \right) f . $$

By Lemma 22.18, the function $f$ must be the second eigenfunction, and

$$ \lambda_2 = 1 - \frac{1 - \tanh(2\beta)}{n} . $$

In particular,

$$ t_{\mathrm{rel}} = \frac{n}{1 - \tanh(2\beta)} . $$

Another application of Lemma 22.18 can be found in Proposition 23.1, where it is used to show that in the random adjacent transposition shuffle, the relaxation time of the entire chain is the same as for a single card.

**22.6. Censoring Inequality**

For a given distribution $\mu$ on $\mathcal{X} \subset S^V$ and an enumeration of $V$, the *systematic scan* sequentially updates all the sites in $V$. When updating a configuration $\sigma$ at site $v$, the spin is chosen according to the distribution $\mu_v^\sigma$, the law $\mu$ conditioned to agree with $\sigma$ outside $v$. When iterated, the distribution converges to $\mu$.

This raises the following question: given a specified sequence of sites

$$ v_1, \ldots, v_s, \ldots, v_t , $$

can omitting the update at $v_s$ decrease the distance to stationarity? The following answers this question when $\mu$ is a monotone system started from the maximal state.

THEOREM 22.20. *Let $\pi$ be a monotone spin system such that $\mathcal{X}$ has a maximal state. Let $\mu$ be the distribution resulting from updates at sites $v_1, \ldots, v_m$, starting from the maximal state, and let $\nu$ be the distribution resulting from updates at a subsequence $v_{i_1}, \ldots, v_{i_k}$, also started from the maximal state. Then $\mu \preceq \nu$, and*

$$ \|\mu - \pi\|_{\mathrm{TV}} \leq \|\nu - \pi\|_{\mathrm{TV}} . $$

### PDF page 331 (book page 315)

In words, censoring updates never decreases the distance to stationarity.

By induction, we can assume $\nu$ is the distribution after updates at

$$ v_1, \ldots, v_{j-1}, v_{j+1}, \ldots, v_m . $$

To prove Theorem 22.20, we will first prove that $\frac{\mu}{\pi}$ and $\frac{\nu}{\pi}$ are increasing.

Given a spin configuration $\sigma$, a site $v$, and a spin $s$, denote by $\sigma_v^s$ the configuration obtained from $\sigma$ by setting the spin at $v$ to $s$:

$$ \sigma_v^s(w) = \begin{cases} \sigma(w) & \text{if } w \neq v, \\ s & \text{if } w = v . \end{cases} $$

Write $\sigma_v^\bullet = \{\sigma_v^s\}_{s \in S}$ for the set of spin configurations that are identical to $\sigma$ except possibly at $v$. Given a distribution $\mu$, denote by $\mu_v$ the distribution resulting from an update at $v$. Then

$$ \mu_v(\sigma) = \frac{\pi(\sigma)}{\pi(\sigma_v^\bullet)} \mu(\sigma_v^\bullet). \tag{22.9} $$

LEMMA 22.21. *For any distribution $\mu$, if $\frac{\mu}{\pi}$ is increasing, then $\frac{\mu_v}{\pi}$ is also increasing for any site $v$.*

PROOF. Define $f : S^V \to \mathbb{R}$ by

$$ f(\sigma) := \max \left\{ \frac{\mu(\omega)}{\pi(\omega)} \, : \, \omega \in \mathcal{X}, \ \omega \preceq \sigma \right\} \tag{22.10} $$

with the convention that $f(\sigma) = 0$ if there is no $\omega \in \mathcal{X}$ satisfying $\omega \preceq \sigma$. Then $f$ is increasing on $S^V$, and $f$ agrees with $\mu/\pi$ on $\mathcal{X}$.

Let $\sigma \preceq \tau$ be two configurations in $\mathcal{X}$; we wish to show that

$$ \frac{\mu_v}{\pi}(\sigma) \leq \frac{\mu_v}{\pi}(\tau). \tag{22.11} $$

Note first that for any $s \in S$, because $f$ is increasing, $f(\sigma_v^s) \leq f(\tau_v^s)$. Furthermore, $f(\tau_v^s)$ is an increasing function of $s$. Thus, by (22.9),

$$ \frac{\mu_v}{\pi}(\sigma) = \frac{\mu(\sigma_v^\bullet)}{\pi(\sigma_v^\bullet)} = \sum_{s \in S} f(\sigma_v^s) \frac{\pi(\sigma_v^s)}{\pi(\sigma_v^\bullet)} $$
$$ = P_v f(\sigma) \leq P_v f(\tau) = \sum_{s \in S} f(\tau_v^s) \frac{\pi(\tau_v^s)}{\pi(\tau_v^\bullet)} = \frac{\mu_v}{\pi}(\tau) , $$

where the inequality follows because, by monotonicity, $P_v f$ is increasing. $\blacksquare$

LEMMA 22.22. *For any $\mu$, $\nu$ such that $\frac{\mu}{\pi}$ is increasing and $\mu \preceq \nu$, we have*

$$ \|\mu - \pi\|_{\mathrm{TV}} \leq \|\nu - \pi\|_{\mathrm{TV}} . $$

PROOF. Let $A = \{\sigma \, : \, \mu(\sigma) > \pi(\sigma)\}$. The function $1_A$ is increasing, so

$$ \|\mu - \pi\|_{\mathrm{TV}} = \sum_{\sigma \in A} [\mu(\sigma) - \pi(\sigma)] = \mu(A) - \pi(A) \leq \nu(A) - \pi(A) \leq \|\nu - \pi\|_{\mathrm{TV}} . $$

$\blacksquare$

LEMMA 22.23. *If the set $S$ is totally ordered, and $\alpha$ and $\beta$ are probability distributions on $S$ such that $\frac{\alpha}{\beta}$ is increasing, and $\beta > 0$ on $S$, then $\alpha \succeq \beta$.*

### PDF page 332 (book page 316)

PROOF. If $g$ is an increasing function on $S$, then by Lemma 22.12, we have

$$ \sum_{s \in S} g(s)\alpha(s) = \sum_{s \in S} g(s) \frac{\alpha(s)}{\beta(s)} \beta(s) $$
$$ \geq \sum_{s \in S} g(s)\beta(s) \cdot \sum_{s \in S} \frac{\alpha(s)}{\beta(s)} \beta(s) $$
$$ = \sum_{s \in S} g(s)\beta(s) . $$

$\blacksquare$

LEMMA 22.24. *If $\frac{\mu}{\pi}$ is increasing, then $\mu \succeq \mu_v$ for all sites $v$.*

PROOF. Fix $\sigma \in \mathcal{X}$ and $v \in V$, and let

$$ S' = S'(\sigma, v) = \{s \in S \, : \, \sigma_v^s \in \mathcal{X}\} . $$

Let $c := (\pi/\mu)(\sigma_v^\bullet)$. The ratio $\frac{\mu}{\mu_v}(\sigma_v^s) = c \frac{\mu}{\pi}(\sigma_v^s)$ is an increasing function of $s \in S'$.

Fix an increasing function $f : \mathcal{X} \to \mathbb{R}$. For $\tau \in \{-1, 1\}^{V \setminus \{v\}}$, let

$$ \mathcal{X}(v, \tau) = \{\sigma \in \mathcal{X} \, : \, \sigma(w) = \tau(w), \ w \neq v\} . $$

By Lemma 22.23,

$$ \mu(\cdot \mid \mathcal{X}(v, \tau)) \succeq \mu_v(\cdot \mid X(v, \tau)) . $$

Because $\mu_v(\mathcal{X}(v, \tau)) = \mu(\mathcal{X}(v, \tau))$,

$$ \sum_{\sigma \in \mathcal{X}(v, \tau)} f(\sigma)\mu(\sigma) \geq \sum_{\sigma \in \mathcal{X}(v, \tau)} f(\sigma)\mu_v(\sigma) . $$

Summing over all $\tau \in \{-1, 1\}^{V \setminus \{v\}}$ finishes the proof. $\blacksquare$

PROOF OF THEOREM 22.20. Let $\mu^0$ be the distribution concentrated at the top configuration, and $\mu^i = (\mu^{i-1})_{v_i}$ for $i \geq 1$. Applying Lemma 22.21 inductively, we have that each $\mu^i/\pi$ is increasing, for $0 \leq i \leq m$. In particular, we see from Lemma 22.24 that $\mu^{j-1} \succeq (\mu^{j-1})_{v_j} = \mu^j$.

If we define $\nu^i$ in the same manner as $\mu^i$, except that $\nu^j = \nu^{j-1}$, then because stochastic dominance persists under updates (Proposition 22.7), we have $\nu^i \succeq \mu^i$ for all $i$; when $i = m$, we get $\mu \preceq \nu$ as desired.

Lemma 22.22 finishes the proof. $\blacksquare$

**22.6.1. Application: fast mixing for Ising model on ladder.** The circular ladder graph of length $n$ has vertex set $\{0, 1\} \times \mathbb{Z}_n$ with edges between $(i, j)$ and $(i, j+1 \mod n)$ and between $(0, j)$ and $(1, j)$. See Figure 22.1.

In Section 15.5, we showed a bound on the relaxation time of $O(n)$, from which we derived an $O(n^2)$ bound on the mixing time. In fact, an upper bound of $O(n \log n)$ can be shown using the censoring inequality.

If $+$ denotes the all-plus configuration, then define

$$ t_{\mathrm{mix}}^+ = \min\{t \, : \, \|P^t(+, \cdot) - \pi\|_{\mathrm{TV}} < 1/4\} . $$

THEOREM 22.25. *The Glauber dynamics for the Ising model on the ladder graph of length $n$ satisfies $t_{\mathrm{mix}}^+ = O(n \log n)$.*

### PDF page 333 (book page 317)

**FIGURE 22.1.** The ladder graph with $n = 32$. The set of vertices enclosed in the dashed box is a block of length $\ell = 2$. *[Figure: A ladder graph drawn as a cylinder — two concentric rings of vertices (top rim and bottom rim) connected by vertical "rung" edges, forming a ladder wrapped into a ring. A dashed rectangular box in the front encloses a small group of vertices, marking one block.]*

In fact, the proof can be modified to yield an $O(n \log n)$ bound on $t_{\mathrm{mix}}$. The couplings in the proof are monotone, and thus they can be combined and extended to a monotone grand coupling, which then bounds the distance from the worst-case starting position.

PROOF. We use the Hamming metric:
$$ \rho(\sigma, \tau) = \frac{1}{2} \sum_{v \in V} |\sigma(v) - \tau(v)| \,, $$
and recall that $\rho_K$ denotes the transportation metric.

Suppose that $\ell$ is odd and $\ell + 1$ divides $n$. Let $\mathcal{B} = \{B_z \, : \, z \in \{0, 1, \ldots, n\}\}$, where $B_z$ is the sub-ladder of side-length $\ell - 1$ centered at the edge $\{(z, 0), (z, 1)\}$ (so the cardinality of $B_z$ is $2 \times \ell$).

For any $u \in V$ and $s = \pm 1$, suppose $\sigma' = \sigma_u^s$ is obtained from $\sigma$ by changing the spin at $u$ to $s$. Let $U_B \sigma$ be the distribution of the update to $\sigma$ when updating block $B$. (See Section 15.5 for the definition of block dynamics.) Since $\rho(\sigma, \sigma') = 1$, we have $\rho_K(U_B \sigma, U_B \sigma') = 1$ when neither $B$ nor $\partial B$ contains $u$. (The boundary $\partial B$ is the set

$$ \{v \, : \, v \notin B, \ \text{there exists } w \text{ with } \{w, v\} \in E, \ \text{and } w \in B\} \,.) $$

If $u \in B$, then $\rho_K(U_B \sigma, U_B \sigma') = 0$. We proved in Theorem 15.11 that the block dynamics determined by $\mathcal{B}$ is contracting. In particular, we showed that if $u \in \partial B$, then
$$ \rho_K(U_B \sigma, U_B \sigma') \leq 8 e^{24\beta} \,. \tag{22.12} $$

Suppose now that we choose $j$ uniformly at random in $\{0, \ldots, \ell\}$ and update (in the normal fashion) all the blocks $B_{j + (\ell+1)k}$ where $k \in \{0, 1, \ldots, \frac{n}{\ell+1} - 1\}$. These blocks are disjoint, and, moreover, no block has an exterior neighbor belonging to another block, hence it makes no difference in what order the updates are made. We call this series of updates a "global block update," and claim that it is contracting— meaning, in this case, that a *single* global block update reduces the transportation distance between any two configurations $\sigma$ and $\tau$ by a constant factor $1 - \gamma$.

To see this, we reduce to the case where $\sigma$ and $\tau = \sigma'$ differ only at a vertex $u$ and average over choice of $j$ to get the transportation distance after one global update is at most
$$ \frac{1}{(\ell + 1)} \sum_{\partial B \ni u} \rho_K(U_B \sigma, U_B \sigma') \,. $$

### PDF page 334 (book page 318)

By (22.12), this is at most $1/2$ for $\ell > 32 e^{24\beta}$.

For $\delta > 0$ that we will specify later, suppose that $t_1 = t_1(\delta)$ has the following property: for any $t > t_1$, performing $t$ single-site updates uniformly at random on the sites *inside* a block $B$ suffices (regardless of boundary spins) to bring the transportation distance between the resulting configuration on $B$ and the block-update configuration down to at most $\delta$. (In fact, if $t_0 = t_{\mathrm{mix}}$ for an $\ell$-block of the ladder maximized over the boundary conditions, we can take $t_1 = t_0 \log(2\ell/\delta)$.) Letting $W_B^t \sigma$ denote the distribution that results when $t$ single-site updates are performed on $B$, the triangle inequality gives
$$ \rho_K(W_B^t \sigma, W_B^t \sigma') \leq \rho_K(U_B \sigma, U_B \sigma') + 2\delta \,, $$
for all $t > t_1$.

Suppose next that $\mathbf{T}$ is a nonnegative-integer-valued random variable that satisfies $\mathbf{P}\{\mathbf{T} < t\} \leq \delta/2\ell$. Since the Hamming distance of any two configurations on $B$ is bounded by $2\ell$, if we perform $\mathbf{T}$ random single-site updates on the block $B$, we get
$$ \begin{aligned} \rho_K(W_B^{\mathbf{T}} \sigma, W_B^{\mathbf{T}} \sigma') &\leq \rho_K(W_B^t \sigma, W_B^t \sigma') + 2\ell \mathbf{P}\{\mathbf{T} < t\} \\ &\leq \rho_K(U_B \sigma, U_B \sigma') + 3\delta \,. \end{aligned} \tag{22.13} $$

Suppose we select, uniformly at random, $2tn/\ell$ sites in $V$. For any block $B$, the number of times that we select a site from $B$ will be a binomially distributed random variable $\mathbf{T}$ with mean $2t$; its probability of falling below $t$ is bounded above by $e^{-t/4}$ (see, e.g., **Alon and Spencer (2008)**, Theorem A.1.13, p. 312). By taking $t \geq \max\{t_1, 4 \log(2\ell/\delta)\}$ we ensure that $\mathbf{P}\{\mathbf{T} < t\} \leq \delta/2\ell$ as required for (22.13). Note that $t$ depends only on $\ell$ and $\delta$.

Let $W$ denote the following global update procedure: choose $j$ uniformly at random as above, perform $2tn/\ell$ random single site updates, but *censor* all updates of sites not in $\bigcup_k B_{j + (\ell+1)k}$. To bound the expected distance between $W\sigma$ and $W\sigma'$, it suffices to consider blocks $B$ such that $u$ is in $B$ or in the exterior boundary $\partial B$. With probability $\ell/(\ell + 1)$, the vertex $u$ is in one of the updated blocks. The expected number of blocks with $u \in \partial B$ is $2/(\ell + 1)$. Therefore, using our assumption that $\ell > 1$,
$$ \rho_K(W\sigma, W\sigma') \leq \frac{1}{2} + 3\delta \left( \frac{2}{\ell + 1} \right) \leq \frac{1}{2} + \frac{6\delta}{\ell + 1} \,. $$

Taking $\delta = \ell/24$, the right-hand side is at most $\frac{3}{4}$. Thus for any two configurations $\sigma, \tau$, the censored Glauber dynamics procedure above yields
$$ \rho_K(W\sigma, W\tau) \leq \frac{3}{4} \rho(\sigma, \tau) \,. $$

We deduce that $O(\log n)$ iterations of $W$ suffice to reduce the maximal transportation distance from its initial value $2n$ (the distance between the top and bottom configurations) to any desired small constant. Recall that transportation distance dominates total variation distance, and each application of $W$ involves $2tn/\ell = O(n)$ single site updates, with censoring of updates that fall on the (random) boundary. Thus with this censoring, uniformly random single-site updates mix (starting from the all plus state) in time $O(n \log n)$.

### PDF page 335 (book page 319)

By Theorem 22.20, censoring these updates cannot improve mixing time, hence the mixing time (starting from all plus state) for standard single-site Glauber dynamics is again $O(n \log n)$. $\blacksquare$

**22.7. Lower bound on $\bar{d}$**

Consider a monotone chains with maximal and minimal states, and let $\tau$ be the time for a monotone coupling from these two states to meet. We saw that the tail of $\tau$ bounds $\bar{d}$, and $t_{\mathrm{mix}} \leq 4\mathbf{E}\tau$. How far off can this bound be? The following gives an answer.

THEOREM 22.26 (**Propp and Wilson (1996**, Theorem 5)). *Let $\ell$ be the length of the longest chain (totally ordered subset) in the partially ordered state space $\mathcal{X}$. Let $0$ and $1$ denote the minimal and maximal states, and fix a monotone coupling $\{(X_t, Y_t)\}$ started from $(0, 1)$. Let $\tau = \min\{t \, : \, X_t = Y_t\}$. We have*
$$ \mathbf{P}\{\tau > k\} \leq \ell \bar{d}(k) \,. \tag{22.14} $$

PROOF. For any $x \in \mathcal{X}$, let $h(x)$ denote the length of the longest chain whose top element is $x$. If $X_k \neq Y_k$, then $h(X_k) + 1 \leq h(Y_k)$. Therefore,
$$ \begin{aligned} \mathbf{P}\{\tau > k\} = \mathbf{P}\{X_k \neq Y_k\} &\leq \mathbf{E}[h(Y_k) - h(X_k)] = E_{P^k(1, \cdot)}[h] - E_{P^k(0, \cdot)}[h] \\ &\leq \left\| P^k(1, \cdot) - P^k(0, \cdot) \right\|_{\mathrm{TV}} \left[ \max_x h(x) - \min_x h(x) \right] \leq \bar{d}(k) \ell \,. \end{aligned} $$
$\blacksquare$

As a consequence of (22.14) we derive the lower bound
$$ t_{\mathrm{mix}} \geq \frac{\mathbf{E}(\tau)}{2 \lceil \log_2 \ell \rceil} \,. \tag{22.15} $$

Set
$$ k_0 := t_{\mathrm{mix}} \lceil \log_2(\ell + 1) \rceil \,. \tag{22.16} $$

By submultiplicity,
$$ \bar{d}(k_0) \leq \bar{d}(t_{\mathrm{mix}})^{\lceil \log_2(\ell+1) \rceil} \leq \frac{1}{\ell + 1} \,. $$

Note that by considering blocks of $k_0$ terms in the infinite sum,
$$ \begin{aligned} \mathbf{E}(\tau) = \sum_{k \geq 0} \mathbf{P}\{\tau > k\} &\leq k_0 + \sum_{j=1}^{\infty} k_0 \mathbf{P}\{\tau > k_0 j\} \\ &\leq k_0 + k_0 \sum_{j=1}^{\infty} \ell \bar{d}(k_0 j) \leq k_0 + k_0 \sum_{j=1}^{\infty} \ell \bar{d}(k_0)^j \leq 2k_0 \,. \end{aligned} $$

The second inequality follows from Theorem 22.26, and the third from the submultiplicativity of $\bar{d}$. Combining this with (22.16) proves (22.15).

### PDF page 336 (book page 320)

**22.8. Proof of Strassen's Theorem**

We complete the proof of Theorem 22.6 here.

PROOF OF NECESSITY IN THEOREM 22.6. Let $\mu$ and $\nu$ be probability measures on $\mathcal{X}$ with $\mu \preceq \nu$. It will be enough to show that there exists a probability measure $\theta$ on

$$ \Delta_\downarrow = \{(x,y) \in \mathcal{X} \times \mathcal{X} \,:\, x \preceq y\} $$

such that $\sum_{y \in \mathcal{X}} \theta(x,y) = \mu(x)$ for all $x \in \mathcal{X}$, and $\sum_{x \in \mathcal{X}} \theta(x,y) = \nu(y)$ for all $y \in \mathcal{X}$.

The set of positive measures $\theta$ on $\Delta_\downarrow$ satisfying

$$ \theta_1(x) := \sum_{y \in \mathcal{X} \,:\, y \succeq x} \theta(x,y) \le \mu(x) \quad \text{for all } x \,, $$

$$ \theta_2(y) := \sum_{x \in \mathcal{X} \,:\, x \preceq y} \theta(x,y) \le \nu(y) \quad \text{for all } y \,, $$

$$ \|\theta\|_1 = \sum_{(x,y) \in \Delta_\downarrow} \theta(x,y) \le 1 \,, $$

forms a compact subset of Euclidean space. Since $\theta \mapsto \|\theta\|_1$ is continuous, there exists an element of this set with $\|\theta\|_1$ maximal. We take $\theta$ to be this maximal measure. We will show that in fact we must have $\|\theta\|_1 = 1$.

First, we inductively define sets $\{A_i\}$ and $\{B_i\}$: Set

$$ A_1 = \{x \in \mathcal{X} \,:\, \theta_1(x) < \mu(x)\} \,, $$

$$ B_i = \{y \in \mathcal{X} \,:\, \text{there exists } x \in A_i \text{ with } x \preceq y\} \,, $$

$$ A_{i+1} = \{x \in \mathcal{X} \,:\, \text{there exists } y \in B_i \text{ with } \theta(x,y) > 0\} \,. $$

Finally, let $A := \bigcup A_i$ and $B := \bigcup B_i$.

We now show that $\theta_2(y) = \nu(y)$ for all $y \in B$.

Suppose otherwise, in which case there must exist a $k$ and $y_k \in B_k$ with $\theta_2(y_k) < \nu(y_k)$. From the construction of the sets $\{A_i\}$ and $\{B_i\}$, there is a sequence $x_1, y_1, x_2, y_2, \ldots, x_k, y_k$ with $x_i \in A_i$ and $y_i \in B_i$ satisfying

$$ \theta_1(x_1) < \mu(x_1) \,, \quad x_i \preceq y_i \,, \quad \theta(x_{i+1}, y_i) > 0 \,. $$

Now choose $\varepsilon$ such that

$$ \varepsilon \le \min\Big\{ \min_{1 \le i \le k-1} \theta(x_{i+1}, y_i),\ \mu(x_1) - \theta_1(x_1),\ \nu(y_k) - \theta_2(y_k) \Big\} \,, $$

and define

$$ \tilde{\theta} := \theta + \sum_{i=1}^{k} \varepsilon \mathbf{1}_{\{(x_i, y_i)\}} - \sum_{i=1}^{k-1} \varepsilon \mathbf{1}_{\{(x_{i+1}, y_i)\}} \,. $$

Then $\tilde{\theta}$ is a positive measure on $\Delta_\downarrow$ satisfying the constraints $\tilde{\theta}_1(x) \le \mu(x)$ and $\tilde{\theta}_2(y) \le \nu(y)$, yet $\|\tilde{\theta}\|_1 > \|\theta\|_1$. This contradicts the maximality of $\theta$.

Thus we have shown that $\theta_2(y) = \nu(y)$ for all $y \in B$.

### PDF page 337 (book page 321)

Note that $A^c \subseteq A_1^c$. We have

$$
\begin{aligned}
\theta_1(A^c) + \theta_2(B) &= \mu(A^c) + \nu(B) \\
&\ge \mu(A^c) + \mu(B) \quad \text{(since } B \text{ is an increasing set)} \\
&\ge \mu(A^c) + \mu(A) \quad \text{(since } B \supseteq A) \\
&= 1 \,.
\end{aligned}
$$

(An increasing set $B$ is a set whose indicator function is increasing.) On the other hand,

$$ \theta_1(A^c) + \theta_2(B) = \sum_{x \in A^c} \sum_{y \succeq x} \theta(x,y) + \sum_{y \in B} \sum_{x \preceq y} \theta(x,y) \le \|\theta\|_1 \,, $$

because for $x \in A^c$ and $y \in B$ we have $\theta(x,y) = 0$ (as otherwise $x \in A$). This shows that $\|\theta\|_1 = 1$, i.e., $\theta$ defines a probability distribution. It must also be that $\theta_1(x) = \mu(x)$ and $\theta_2(y) = \nu(y)$ for all $x$ and $y$. $\blacksquare$

**22.9. Exercises**

EXERCISE 22.1. The Beach model places labels $\{-k, \ldots, 0, \ldots, k\}$ on the vertices of a graph subject to the constraint that positive and negative spins cannot be adjacent. Let $\pi$ be the uniform measure on allowed configurations. Verify the Beach model is monotone.

EXERCISE 22.2. For random walk on the hypercube, prove the monotone coupling does not minimize the expected time to couple the top and bottom states.

*Hint:* See Chapter 18.

EXERCISE 22.3. Show that any partial order on a finite set can be extended to a total order.

*Hint:* Pick any incomparable pair, order it arbitrarily, and take the transitive closure. Repeat.

EXERCISE 22.4. This exercise concerns the *strictly* increasing assumption in Lemma 22.18. Give an example of a monotone chain and an increasing, nonconstant eigenfunction which does not correspond to $\lambda_2$.

*Hint:* Consider a product chain.

EXERCISE 22.5. Show that the hardcore model on a bipartite graph, with the ordering given in Example 22.10, is a monotone spin system.

EXERCISE 22.6. Show that Theorem 22.16 is false without the condition that $x$ and $y$ are comparable whenever $P(x,y) > 0$.

EXERCISE 22.7. Consider Glauber dynamics $(X_t)$ for the Ising model on an $n$-vertex graph $G = (V, E)$.

(a) For a sequence of nodes $v_1, v_2, \ldots v_t$, denote by $\mu^t$ the distribution of the configuration obtained by starting at the all plus state $\oplus$ and updating at $v_1, v_2, \ldots v_t$. Show that the all minus state $\ominus$ satisfies $\mu^t(\ominus) \le \pi(\ominus)$.

&nbsp;&nbsp;&nbsp;&nbsp;*Hint:* Apply Lemma 22.21 $t$ times.

(b) Let $\tau$ be the first time where all nodes in $V$ have been refreshed by the dynamics. Show that

$$ \mathbf{P}_\oplus\{X_t = \ominus \mid \tau \le t\} \le \pi(\ominus) $$

for all $t$.

&nbsp;&nbsp;&nbsp;&nbsp;*Hint:* Condition on the sequence of updated vertices $v_1, v_2, \ldots v_t$.

### PDF page 338 (book page 322)

(c) Infer that

$$ s(t) \ge 1 - P^t(\oplus, \ominus) \ge 1 - \mathbf{P}\{\tau \le t\} $$

for all $t$.

&nbsp;&nbsp;&nbsp;&nbsp;*Hint:*

$$ P^t(\oplus, \ominus) = \mathbf{P}\{\tau \le t\} \cdot \mathbf{P}_\oplus\{X_t = \ominus \mid \tau \le t\} \,. $$

(d) In particular, for $t = n \log(n) - c_\delta n$, we have $s(t) \ge 1 - \delta$.

&nbsp;&nbsp;&nbsp;&nbsp;*Hint*: In fact,

$$ \liminf_{n \to \infty} s(n \log(n) - cn) \ge 1 - e^{-e^c} + o(1) \,, $$

by (2.25).

(e) Deduce that for any $\varepsilon < 1/2$ we have $t_{\text{mix}}(\varepsilon) \ge n \log(n)/2 - O(n)$.

&nbsp;&nbsp;&nbsp;&nbsp;*Hint:* Use Lemma 6.17.

**22.10. Notes**

Strassen (1965) proved the coupling equivalence of stochastic domination in the generality that $\mathcal{X}$ is a Polish space equipped with a partial order. The proof given here is the augmenting path method from the min-cut/max-flow theorem.

The idea of using dynamics to prove positive correlations is due to Holley (1974).

Nacu (2003) shows that the relaxation time of the Glauber dynamics of the Ising model on the cycle is increasing in the interaction parameters. He identifies the second eigenfunction using Lemmas 22.17 and 22.18, which can be found there. A variant of Lemma 22.18 appears in Wilson (2004a).

Theorem 22.20 is due to Peres and Winkler (2013). Holroyd (2011) provides examples of non-monotone systems where extra updates can delay mixing. An open problem is whether Glauber dynamics for the Potts model, started from a monochromatic configuration, has the same censoring property as the Ising model. For some additional applications of Theorem 22.20, see Ding, Lubetzky, and Peres (2010b), Caputo, Lubetzky, Martinelli, Sly, and Toninelli (2014), Restrepo, Štefankovič, Vera, Vigoda, and Yang (2014), Martinelli and Wouts (2012), Laslier and Toninelli (2015), Ding and Peres (2011).

The problem of comparing Glauber updates at deterministic vs. random locations for spin systems is surveyed in Diaconis (2013), and partial results in the monotone case are in Peres and Winkler (2013).

For one-dimensional systems, there is a general proof of an $O(n \log n)$ upper bound in Martinelli (1999).

The argument outlined in Exercise 22.7 is due to Evita Nestoridi (personal communication, 2016). Part (e) is due to Ding and Peres (2011) (see the arXiv version) in a slightly stronger form. Earlier, Hayes and Sinclair (2007) proved for general spin systems that $t_{\text{mix}} > c(\Delta) n \log(n)$, where $\Delta$ is the maximal degree. In their bound, $c(\Delta) \to 0$ as $\Delta \to \infty$.

Besides the examples in this chapter, another important example of a monotone system is the exclusion process in Chapter 23.

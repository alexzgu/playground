# Chapter 21 — Countable State Space Chains*
*(PDF pages 307–320; book pages 291–304)*

### PDF page 307 (book page 291)

CHAPTER 21

# Countable State Space Chains*

In this chapter we treat the case where $\mathcal{X}$ is not necessarily finite, although we assume it is a countable set. A classical example is the simple random walk on $\mathbb{Z}^d$, which we have already met in the case $d = 1$ in Section 2.7. There is a striking dependence on the dimension $d$: For $d = 2$, the walk returns infinitely often to its starting point, while for $d \geq 3$, the number of returns is finite. We will return to this example later.

As before, $P$ is a function from $\mathcal{X} \times \mathcal{X}$ to $[0, 1]$ satisfying $\sum_{y \in \mathcal{X}} P(x, y) = 1$ for all $x \in \mathcal{X}$. We still think of $P$ as a matrix, except now it has countably many rows and columns. The matrix arithmetic in the finite case extends to the countable case without any problem, as do the concepts of irreducibility and aperiodicity. The joint distribution of the infinite sequence $(X_t)$ is still specified by $P$ together with a starting distribution $\mu$ on $\mathcal{X}$.

**21.1. Recurrence and Transience**

EXAMPLE 21.1 (Simple random walk on $\mathbb{Z}$). Let $(X_t)$ have transition matrix

$$ P(j, k) = \begin{cases} 1/2 & \text{if } k = j \pm 1, \\ 0 & \text{otherwise.} \end{cases} $$

Let $A_k$ be the event that the walk started from zero reaches absolute value $2^k$ before it returns to zero. By symmetry, $\mathbf{P}_0(A_1) = 1/2$ and $\mathbf{P}_0(A_{k+1} \mid A_k) = 1/2$. Thus $\mathbf{P}_0(A_k) = 2^{-k}$, and in particular

$$ \mathbf{P}_0\{\tau_0^+ = \infty\} = \mathbf{P}_0\left(\bigcap_{k=1}^{\infty} A_k\right) = \lim_{k \to \infty} \mathbf{P}_0(A_k) = 0. $$

The penultimate equality follows since the events $\{A_k\}$ are decreasing.

EXAMPLE 21.2 (Biased random walk on $\mathbb{Z}$). Suppose now that a particle on $\mathbb{Z}$ makes biased moves, so that

$$ P(j, k) = \begin{cases} q & \text{for } k = j - 1, \\ p & \text{for } k = j + 1, \end{cases} $$

where $q < p$ and $q + p = 1$. Recall the gambler's ruin formula (9.20) for biased random walk,

$$ \mathbf{P}_k\{\tau_n < \tau_0\} = \frac{1 - (q/p)^k}{1 - (q/p)^n}. $$

Thus,

$$ \mathbf{P}_1\{\tau_0 = \infty\} = p\mathbf{P}_1\left(\bigcap_{n=2}^{\infty}\{\tau_n < \tau_0\}\right) = \lim_{n} \frac{1 - (q/p)}{1 - (q/p)^n} = \frac{p - q}{p} > 0. $$

### PDF page 308 (book page 292)

The first equality holds because the probability the walk remains in a bounded interval forever is zero. Since $\mathbf{P}_0\{\tau_0^+ = \infty\} = \mathbf{P}_1\{\tau_0 = \infty\}$, there is a positive probability that the biased random walk never returns to its starting position.

We have seen that the unbiased random walk on $\mathbb{Z}$ (Example 21.1) and the biased random walk on $\mathbb{Z}$ (Example 21.2) have quite different behavior. We make the following definition to describe this difference.

We define a state $x \in \mathcal{X}$ to be **_recurrent_** if $\mathbf{P}_x\{\tau_x^+ < \infty\} = 1$. Otherwise, $x$ is called **_transient_**.

PROPOSITION 21.3. *Suppose that $P$ is the transition matrix of an irreducible Markov chain $(X_t)$. Define $G(x, y) := \mathbf{E}_x\left(\sum_{t=0}^{\infty} \mathbf{1}_{\{X_t=y\}}\right) = \sum_{t=0}^{\infty} P^t(x, y)$ to be the expected number of visits to $y$ starting from $x$. The following are equivalent:*

(i) *$G(x, x) = \infty$ for some $x \in \mathcal{X}$.*
(ii) *$G(x, y) = \infty$ for all $x, y \in \mathcal{X}$.*
(iii) *$\mathbf{P}_x\{\tau_x^+ < \infty\} = 1$ for some $x \in \mathcal{X}$.*
(iv) *$\mathbf{P}_x\{\tau_y^+ < \infty\} = 1$ for all $x, y \in \mathcal{X}$.*

PROOF. (i) $\Leftrightarrow$ (iii). Every time the chain visits $x$, it has the same probability of eventually returning to $x$, independent of the past. Thus the number of visits to $x$ is a geometric random variable with success probability $1 - \mathbf{P}_x\{\tau_x^+ < \infty\}$. We conclude that $\mathbf{P}_x\{\tau_x^+ = \infty\} > 0$ if and only if $G(x, x) < \infty$.

(i) $\Leftrightarrow$ (ii). Suppose $G(x_0, x_0) = \infty$, and let $x, y \in \mathcal{X}$. By irreducibility, there exist $r$ and $s$ such that $P^r(x, x_0) > 0$ and $P^s(x_0, y) > 0$. Then

$$ P^r(x, x_0)P^t(x_0, x_0)P^s(x_0, y) \leq P^{r+t+s}(x, y). $$

Thus,

$$ G(x, y) \geq \sum_{t=0}^{\infty} P^{r+t+s}(x, y) \geq P^r(x, x_0)P^s(x_0, y) \sum_{t=0}^{\infty} P^t(x_0, x_0) = \infty \,. \tag{21.1} $$

(iii) $\Leftrightarrow$ (iv). Fix states $x, y$. If $\mathbf{P}_y\{\tau_x > \tau_y^+\} = 1$, then iterating gives $\mathbf{P}_y\{\tau_x = \infty\} = 1$, contradicting irreducibility. Thus $\mathbf{P}_y\{\tau_x < \tau_y^+\} > 0$. Now suppose that (iv) fails for $x, y$, i.e., $\mathbf{P}_x\{\tau_y^+ = \infty\} > 0$. Then

$$ \mathbf{P}_y\{\tau_y^+ = \infty\} \geq \mathbf{P}_y\{\tau_x < \tau_y^+\} \cdot \mathbf{P}_x\{\tau_y^+ = \infty\} > 0 \,, $$

which implies that the number of returns to $y$ is a geometric variable of expectation $G(y, y) < \infty$, contradicting (ii). $\blacksquare$

By Proposition 21.3, for an irreducible chain, a single state is recurrent if and only if all states are recurrent. For this reason, an irreducible chain can be classified as either recurrent or transient.

EXAMPLE 21.4 (Simple random walk on $\mathbb{Z}$, revisited). Another proof that the simple random walker on $\mathbb{Z}$ discussed in Example 21.1 is recurrent uses Proposition 21.3.

When started at 0, the walk can return to 0 only at even times, with the probability of returning after $2t$ steps equal to $\mathbf{P}_0\{X_{2t} = 0\} = \binom{2t}{t}2^{-2t}$. By application of Stirling's formula (A.18), $\mathbf{P}_0\{X_{2t} = 0\} \sim ct^{-1/2}$. Therefore,

$$ G(0, 0) = \sum_{t=0}^{\infty} \mathbf{P}_0\{X_{2t} = 0\} = \infty, $$

### PDF page 309 (book page 293)

so by Proposition 21.3 the chain is recurrent.

EXAMPLE 21.5. The simple random walk on $\mathbb{Z}^2$ moves at each step by selecting each of the four neighboring locations with equal probability. Instead, consider at first the "corner" walk, which at each move adds with equal probability one of $\{(1,1),(1,-1),(-1,1),(-1,-1)\}$ to the current location. The advantage of this walk is that its coordinates are independent simple random walks on $\mathbb{Z}$. So

$$ \mathbf{P}_{(0,0)}\{X_{2t} = (0,0)\} = \mathbf{P}_{(0,0)}\left\{ X_{2t}^{(1)} = 0 \right\} \mathbf{P}_{(0,0)}\left\{ X_{2t}^{(2)} = 0 \right\} \sim \frac{c}{n}. $$

Again by Proposition 21.3, the chain is recurrent. Now notice that the usual nearest-neighbor simple random walk is a rotation of the corner walk by $\pi/4$, followed by a dilation, so it is recurrent.

For random walks on infinite graphs, the electrical network theory of Chapter 9 is very useful for deciding if a chain is recurrent.

**21.2. Infinite Networks**

For an infinite connected graph $G = (V, E)$ with edge conductances $\{c(e)\}_{e \in E}$, let $a \in V$, and let $\{G_n = (V_n, E_n)\}$ be a sequence of finite connected subgraphs containing $a$ such that

(i) $E_n$ contains all edges in $E$ with both endpoints in $V_n$,
(ii) $V_n \subset V_{n+1}$ for all $n$, and
(iii) $\bigcup_{n=1}^{\infty} V_n = V$.

For each $n$, construct a modified network $G_n^\star$ in which all the vertices in $V \setminus V_n$ are replaced by a single vertex $z_n$ (adjacent to all vertices in $V_n$ which are adjacent to vertices in $V \setminus V_n$), and set

$$ c(x, z_n) = \sum_{\substack{\{x,z\} \in E \\ z \in V \setminus V_n}} c(x, z) . $$

Define

$$ \mathcal{R}(a \leftrightarrow \infty) := \lim_{n \to \infty} \mathcal{R}\left(a \leftrightarrow z_n \text{ in } G_n^\star\right) . $$

The limit above exists and does not depend on the sequence $\{G_n\}$ by Rayleigh's Monotonicity Principle. Define $\mathcal{C}(a \leftrightarrow \infty) := [\mathcal{R}(a \leftrightarrow \infty)]^{-1}$. By (9.12),

$$ \mathbf{P}_a\{\tau_a^+ = \infty\} = \lim_{n \to \infty} \mathbf{P}_a\{\tau_{z_n} < \tau_a^+\} = \lim_{n \to \infty} \frac{\mathcal{C}(a \leftrightarrow z_n)}{\pi(a)} = \frac{\mathcal{C}(a \leftrightarrow \infty)}{\pi(a)}. \tag{21.2} $$

The first and fourth expressions above refer to the network $G$, while the second and third refer to the networks $G_n^\star$.

A flow on $G$ from $a$ to infinity is an antisymmetric edge function obeying the node law at all vertices except $a$. Thomson's Principle (Theorem 9.10) remains valid for infinite networks:

$$ \mathcal{R}(a \leftrightarrow \infty) = \inf \left\{ \mathcal{E}(\theta) \, : \, \theta \text{ a unit flow from } a \text{ to } \infty \right\}. \tag{21.3} $$

As a consequence, Rayleigh's Monotonicity Law (Theorem 9.12) also holds for infinite networks.

The next proposition summarizes the connections between resistance and recurrence.

PROPOSITION 21.6. *Let $\langle G, \{c(e)\}\rangle$ be a network. The following are equivalent:*

### PDF page 310 (book page 294)

(i) *The weighted random walk on the network is transient.*
(ii) *There is some node $a$ with $\mathcal{C}(a \leftrightarrow \infty) > 0$. (Equivalently, $\mathcal{R}(a \leftrightarrow \infty) < \infty$.)*
(iii) *There is a flow $\theta$ from some node $a$ to infinity with $\|\theta\| > 0$ and $\mathcal{E}(\theta) < \infty$.*

PROOF. That (i) and (ii) are equivalent follows from (21.2), and (21.3) implies the equivalence of (ii) and (iii). $\blacksquare$

In an infinite network $\langle G, \{c_e\}\rangle$, a version of Proposition 9.16 (the Nash-Williams inequality) is valid.

PROPOSITION 21.7 (Nash-Williams). *If there exist disjoint edge-cutsets $\{\Pi_n\}$ that separate $a$ from $\infty$ and satisfy*

$$ \sum_n \left( \sum_{e \in \Pi_n} c(e) \right)^{-1} = \infty, \tag{21.4} $$

*then the weighted random walk on $\langle G, \{c_e\}\rangle$ is recurrent.*

PROOF. Recall the definition of $z_n$ given in the beginning of this section. The assumption (21.4) implies that $\mathcal{R}(a \leftrightarrow z_n) \to \infty$. Consequently, by Proposition 9.5, $\mathbf{P}_a\{\tau_{z_n} < \tau_a^+\} \to 0$, and the chain is recurrent. $\blacksquare$

EXAMPLE 21.8 ($\mathbb{Z}^2$ is recurrent). Take $c(e) = 1$ for each edge of $G = \mathbb{Z}^2$ and consider the cutsets consisting of edges joining vertices in $\partial\square_n$ to vertices in $\partial\square_{n+1}$, where $\square_n := [-n, n]^2$. Then by the Nash-Williams inequality,

$$ \mathcal{R}(a \leftrightarrow \infty) \geq \sum_n \frac{1}{4(2n + 1)} = \infty. $$

Thus, simple random walk on $\mathbb{Z}^2$ is recurrent. Moreover, we obtain a lower bound for the resistance from the center of a square $\square_n = [-n, n]^2$ to its boundary:

$$ \mathcal{R}(0 \leftrightarrow \partial\square_n) \geq c \log n. $$

EXAMPLE 21.9 ($\mathbb{Z}^3$ is transient). To each directed edge $\vec{e}$ in the lattice $\mathbb{Z}^3$, attach an orthogonal unit square $\square_e$ intersecting $\vec{e}$ at its midpoint $m_e$. Let $\sigma_e$ be the sign of the scalar product between $\vec{e}$ and the vector from 0 to $m_e$. Define $\theta(\vec{e})$ to be the area of the radial projection of $\square_e$ onto the sphere of radius $1/4$ centered at the origin, multiplied by $\sigma_e$. (See Figure 21.1). By considering the projections of all faces of the unit cube centered at a lattice point $x \neq 0$, we can easily verify that $\theta$ satisfies the node law at $x$. (Almost every ray from the origin that intersects the cube enters it through a face $\square_{xy}$ with $\sigma_{xy} = -1$ and exits through a face $\square_{xz}$ with $\sigma_{xz} = 1$.) Note $\theta(\vec{0y}) > 0$ for all neighbors $y$ of 0. Hence $\theta$ is a non-zero flow from 0 to $\infty$ in $\mathbb{Z}^3$. For a square of distance $r$ from the origin, projecting onto the sphere of radius $1/4$ reduces area by order $r^2$. Therefore,

$$ \mathcal{E}(\theta) \leq \sum_n C_1 n^2 \left( \frac{C_2}{n^2} \right)^2 < \infty. $$

By Proposition 21.6, $\mathbb{Z}^3$ is transient. This works for any $\mathbb{Z}^d$, $d \geq 3$. An analytic description of the same flow was given by T. Lyons (**1983**).

### PDF page 311 (book page 295)

*[Figure: a three-dimensional diagram showing a small sphere at the origin (with coordinate axes passing through it), and a tilted unit square positioned above and to the right. Two dots mark points, and dashed lines from the origin/sphere fan outward to the corners of the square, illustrating the radial projection of the square onto the sphere.]*

FIGURE 21.1. Projecting a unit square orthogonal to the directed edge $((0,0,2),(1,0,2))$ onto the sphere of radius $1/4$ centered at the origin.

**21.3. Positive Recurrence and Convergence**

The Convergence Theorem as stated in Theorem 4.9 does not hold for all irreducible and aperiodic chains on infinite state spaces. If the chain is transient, then by Proposition 21.3, $\sum_{t=0}^{\infty} \mathbf{P}_x\{X_t = y\} < \infty$ for all $x, y \in X$. This implies that for all $x, y \in \mathcal{X}$,

$$ \lim_{t \to \infty} \mathbf{P}_x\{X_t = y\} = 0. \tag{21.5} $$

That is, if there is a probability $\pi$ on $\mathcal{X}$ such that $(\mu P^t)(x) \to \pi(x)$ for all $x \in \mathcal{X}$, then the chain must be recurrent.

However, recurrence is not sufficient. For example, the simple random walker of Example 21.4, a recurrent chain, also satisfies (21.5). A condition stronger than recurrence is required.

EXAMPLE 21.10. We have already seen that the simple random walker on $\mathbb{Z}$ is recurrent. Let $\alpha = \mathbf{E}_1(\tau_0)$. By conditioning on the first move of the walk,

$$ \alpha = \frac{1}{2} \cdot 1 + \frac{1}{2}[1 + \mathbf{E}_2(\tau_0)] = 1 + \alpha. $$

The last equality follows since the time to go from 2 to 0 equals the time to go from 2 to 1 plus the time to go from 1 to 0. There is no finite number $\alpha$ which satisfies this equation, so we must have $\alpha = \infty$. From this it follows that $\mathbf{E}_0(\tau_0^+) = \infty$. Thus, although $\tau_0$ is a finite random variable with probability one, it has infinite expectation.

A state $x$ is called ***positive recurrent*** if $\mathbf{E}_x(\tau_x^+) < \infty$. As Example 21.10 shows, this property is strictly stronger than recurrence.

PROPOSITION 21.11. *If $(X_t)$ is a Markov chain with irreducible transition matrix $P$, then the following are equivalent:*

### PDF page 312 (book page 296)

(i) $\mathbf{E}_z(\tau_z^+) < \infty$ *for some $z \in \mathcal{X}$.*
(ii) $\mathbf{E}_x(\tau_y^+) < \infty$ *for all $x, y \in \mathcal{X}$.*

PROOF. Suppose that $\mathbf{E}_z(\tau_z^+) < \infty$. By the strong Markov property at time $\tau_x$,

$$ \infty > \mathbf{E}_z \tau_z^+ \geq \mathbf{P}_z\{\tau_x < \tau_z^+\}\mathbf{E}_z(\tau_z^+ \mid \tau_x < \tau_z^+) \geq \mathbf{P}_x\{\tau_x < \tau_z^+\}\mathbf{E}_x(\tau_z^+). $$

By irreducibility, $\mathbf{P}_z\{\tau_x < \tau_z^+\} > 0$, whence $\mathbf{E}_x(\tau_z^+) < \infty$.

Now take any $x, y \in \mathcal{X}$. Let $\tau_z^{(0)} = \tau_z^+$ and, for $k \geq 1$,

$$ \tau_z^{(k)} = \inf\{t > \tau^{(k-1)} \,:\, X_t = z\} \,. $$

Define $\tau_{z,y} = \inf\{t > \tau_z^+ \,:\, X_t = y\}$, and set

$$ K = \inf\{k \geq 1 \,:\, \tau_z^{(k-1)} < \tau_{z,y} \leq \tau_z^{(k)}\} \,. $$

The distribution of $K$ is geometric with success probability $\mathbf{P}_z\{\tau_y^+ \leq \tau_z^+\}$; this probability is positive by irreducibility, and thus $\mathbf{E}(K) < \infty$. We have

$$ \tau_y^+ \leq \tau_z^+ + \sum_{k=1}^{K}[\tau_z^{(k)} - \tau_z^{(k-1)}] \,. $$

Since the strong Markov property implies that the excursion lengths $\{\tau_z^{(k)} - \tau_z^{(k-1)}\}_{k=1}^{\infty}$ are independent and identically distributed, and also that $\{K < k\}$ is independent of $\tau_z^{(k)} - \tau_z^{(k-1)}$, by Wald's Identity (Exercise 6.7), we have

$$ \mathbf{E}_x(\tau_y^+) \leq \mathbf{E}_x(\tau_z^+) + \mathbf{E}(K)\mathbf{E}_z(\tau_z^+) < \infty \,. $$

$\blacksquare$

Thus if a single state of the chain is positive recurrent, all states are positive recurrent. We can therefore classify an irreducible chain as positive recurrent if one state and hence all states are positive recurrent. A chain which is recurrent but not positive recurrent is called **null recurrent**.

We first show that existence of a stationary distribution gives a formula for the expected return times.

LEMMA 21.12 (Kac). *Let $(X_t)$ be an irreducible Markov chain with transition matrix $P$. Suppose that there is a stationary distribution $\pi$ solving $\pi = \pi P$. Then for any set $S \subset \mathcal{X}$,*

$$ \sum_{x \in S} \pi(x)\mathbf{E}_x(\tau_S^+) = 1. \tag{21.6} $$

*In other words, the expected return time to $S$ when starting at the stationary distribution conditioned on $S$ is $\pi(S)^{-1}$. In particular, for all $x \in \mathcal{X}$,*

$$ \pi(x) = \frac{1}{\mathbf{E}_x(\tau_x^+)} \,. \tag{21.7} $$

PROOF. Let $(Y_t)$ be the reversed chain with transition matrix $\hat{P}$, defined in (1.32).

First we show that both $(X_t)$ and $(Y_t)$ are recurrent. Fix a state $x$ and define

$$ \alpha(t) := \mathbf{P}_\pi\{X_t = x, X_s \neq x \text{ for } s > t\}. $$

By stationarity,

$$ \alpha(t) = \mathbf{P}_\pi\{X_t = x\}\mathbf{P}_x\{\tau_x^+ = \infty\} = \pi(x)\mathbf{P}_x\{\tau_x^+ = \infty\}. \tag{21.8} $$

### PDF page 313 (book page 297)

Since the events $\{X_t = x, X_s \neq x \text{ for } s > t\}$ are disjoint for distinct $t$,

$$ \sum_{t=0}^{\infty} \alpha(t) \leq 1. $$

Since it is clear from (21.8) that $\alpha(t)$ does not depend on $t$, it must be that $\alpha(t) = 0$ for all $t$. From the identity (21.8) and Exercise 21.2, it follows that $\mathbf{P}_x\{\tau_x^+ < \infty\} = 1$. The same argument works for the reversed chain as well, so $(Y_t)$ is also recurrent.

For $x \in S, y \in \mathcal{X}$ and $t \geq 0$, sum the identity

$$ \pi(z_0)P(z_0, z_1)P(z_1, z_2)\cdots P(z_{t-1}, z_t) = \pi(z_t)\hat{P}(z_t, z_{t-1})\cdots \hat{P}(z_1, z_0) $$

over all sequences where $z_0 = x$, the states $z_1, \ldots, z_{t-1}$ are not in $S$, and $z_t = y$ to obtain

$$ \pi(x)\mathbf{P}_x\{\tau_S^+ \geq t, X_t = y\} = \pi(y)\hat{\mathbf{P}}_y\{\tau_S^+ = t, Y_t = x\}. \tag{21.9} $$

(We write $\hat{\mathbf{P}}$ for the probability measure corresponding to the reversed chain.) Summing over all $x \in S$, $y \in \mathcal{X}$, and $t \geq 0$ shows that

$$ \sum_{x \in S} \pi(x)\sum_{t=1}^{\infty}\mathbf{P}_x\{\tau_S^+ \geq t\} = \hat{\mathbf{P}}_\pi\{\tau_S^+ < \infty\} = 1. $$

(The last equality follows from recurrence of $(Y_t)$.) Since $\tau_S^+$ takes only positive integer values, this simplifies to

$$ \sum_{x \in S} \pi(x)\mathbf{E}_x\{\tau_S^+\} = 1. \tag{21.10} $$

$\blacksquare$

The following relates positive recurrence to the existence of a stationary distribution:

THEOREM 21.13. *An irreducible Markov chain with transition matrix $P$ is positive recurrent if and only if there exists a probability distribution $\pi$ on $\mathcal{X}$ such that $\pi = \pi P$.*

PROOF. That the chain is positive recurrent when a stationary distribution exists follows from Lemma 21.12 and Exercise 21.2.

Define, as in (1.19),

$$ \tilde{\pi}_z(y) = \mathbf{E}_z\left(\sum_{t=0}^{\tau_z^+ - 1} \mathbf{1}_{\{X_t = y\}}\right) \tag{21.11} $$

For any recurrent chain, $\tilde{\pi}_z(y) < \infty$ for all $y \in \mathcal{X}$: If the walk visits $y$ before returning to $x$, the number of additional visits to $y$ before hitting $z$ is a geometric random variable with parameter $\mathbf{P}_y\{\tau_y^+ < \tau_z\} < 1$. Also, in any recurrent chain, $\tilde{\pi}_z$ defines a stationary measure, as the proof of Proposition 1.14 shows. If the chain is positive recurrent, then $\mathbf{E}_z(\tau_z^+) < \infty$, and $\frac{\tilde{\pi}_z}{\mathbf{E}_z(\tau_z^+)}$ is a stationary distribution. $\blacksquare$

The uniqueness of $\pi$ in the positive recurrent case follows from (21.7). To prove an analagous [sic] statement for the null-recurrent case we will need the following lemma.

LEMMA 21.14. *Suppose that $\{X_n\}$ is a recurrent irreducible Markov chain with transition matrix $P$. If $h$ is $P$-harmonic and non-negative, then $h$ is constant.*

### PDF page 314 (book page 298)

PROOF. Note that $h(X_n)$ is a martingale. Thus if $\tau_y$ is the hitting time of $y$, then

$$ h(x) = \mathbf{E}_x[h(X_{\tau_y \wedge n})] \geq h(y)\mathbf{P}_x\{\tau_y < n\} \,. $$

By recurrence, we can take $n$ large enough so that

$$ h(x) \geq (1 - \varepsilon)h(y) \,. $$

Similarly, $h(y) \geq (1 - \varepsilon)h(x)$. Letting $\varepsilon \to 0$ shows that $h(x) = h(y)$. $\blacksquare$

We refer to a non-negative row vector $\mu$ indexed by the elements of $\mathcal{X}$ as a **measure** on $\mathcal{X}$. If $\mu = \mu P$, then $\mu$ is called a **stationary measure**.

PROPOSITION 21.15. *Let $P$ be irreducible and suppose the Markov chain with transition matrix $P$ is recurrent. Let $\pi$ and $\mu$ be two measures satisfying $\pi = \pi P$ and $\mu = \mu P$. Then $\mu = c\pi$ for some constant $c$.*

PROOF. Let $h = \mu/\pi$. Then $h$ is harmonic for $\hat{P}$, the time-reversal of $P$. Since $\hat{P}^t(x, x) = P^t(x, x)$ for all $t \geq 1$, the $\hat{P}$-chain is also recurrent. The conclusion follows from the fact that all such functions are constant. (Lemma 21.14.) $\blacksquare$

THEOREM 21.16. *Let $P$ be an irreducible and aperiodic transition matrix for a Markov chain $(X_t)$. If the chain is positive recurrent, then there is a unique probability distribution $\pi$ on $\mathcal{X}$ such that $\pi = \pi P$ and for all $x \in \mathcal{X}$,*

$$ \lim_{t \to \infty}\|P^t(x, \cdot) - \pi\|_{TV} = 0. \tag{21.12} $$

PROOF. The existence of $\pi$ solving $\pi = \pi P$ is one direction of Theorem 21.13.

We now show that for any two states $x$ and $y$ we can couple together the chain started from $x$ with the chain started from $y$ so that the two chains eventually meet with probability one.

Consider the chain on $\mathcal{X} \times \mathcal{X}$ with transition matrix

$$ Q((x, y), (z, w)) = P(x, z)P(y, w), \quad \text{for all } (x, y) \in \mathcal{X} \times \mathcal{X}, \, (z, w) \in \mathcal{X} \times \mathcal{X}. \tag{21.13} $$

This chain makes independent moves in the two coordinates, each according to the matrix $P$. Aperiodicity of $P$ implies that $Q$ is irreducible (see Exercise 21.6). If $(X_t, Y_t)$ is a chain started with product distribution $\mu \times \nu$ and run with transition matrix $Q$, then $(X_t)$ is a Markov chain with transition matrix $P$ and initial distribution $\mu$, and $(Y_t)$ is a Markov chain with transition matrix $P$ and initial distribution $\nu$.

Note that

$$ \begin{aligned} (\pi \times \pi)Q(z, w) &= \sum_{(x,y) \in \mathcal{X} \times \mathcal{X}} (\pi \times \pi)(x, y)P(x, z)P(y, w) \\ &= \sum_{x \in \mathcal{X}} \pi(x)P(x, z)\sum_{y \in \mathcal{X}} \pi(y)P(y, w). \end{aligned} $$

Since $\pi = \pi P$, the right-hand side equals $\pi(z)\pi(w) = (\pi \times \pi)(z, w)$. Thus $\pi \times \pi$ is a stationary distribution for $Q$. By Theorem 21.13, the chain $(X_t, Y_t)$ is positive recurrent. In particular, for any fixed $x_0$, if

$$ \tau := \min\{t > 0 \,:\, (X_t, Y_t) = (x_0, x_0)\}, $$

then

$$ \mathbf{P}_{x,y}\{\tau < \infty\} = 1 \quad \text{for all } x, y \in \mathcal{X}. \tag{21.14} $$

### PDF page 315 (book page 299)

To construct the coupling, run the pair of chains with transitions (21.13) until they meet. Afterwards, keep them together. To obtain (21.12), note that if the chain $(X_t, Y_t)$ is started with the distribution $\delta_x \times \pi$, then for fixed $t$ the pair of random variables $X_t$ and $Y_t$ is a coupling of $P^t(x, \cdot)$ with $\pi$. Thus by Proposition 4.7 we have

$$ \left\| P^t(x, \cdot) - \pi \right\|_{\mathrm{TV}} \leq \mathbf{P}_{\delta_x \times \pi}\{X_t \neq Y_t\} \leq \mathbf{P}_{\delta_x \times \pi}\{\tau > t\}. \tag{21.15} $$

From (21.14),

$$ \lim_{t \to \infty} \mathbf{P}_{\delta_x \times \pi}\{\tau > t\} = \sum_{y \in \mathcal{X}} \pi(y) \lim_{t \to \infty} \mathbf{P}_{x,y}\{\tau > t\} = 0. $$

(See Exercise 21.10 for a justification of the exchange of limits.)

This and (21.15) imply (21.12). $\blacksquare$

EXAMPLE 21.17. Consider a nearest-neighbor random walk on $\mathbb{Z}^+$ which moves up with probability $p$ and down with probability $q$. If the walk is at 0, it remains at 0 with probability $q$. Assume that $q > p$.

The equation $\pi = \pi P$ reads as

$$ \pi(0) = q\pi(1) + q\pi(0), $$
$$ \pi(k) = p\pi(k-1) + q\pi(k+1). $$

Solving, $\pi(1) = \pi(0)(p/q)$ and working up the ladder,

$$ \pi(k) = (p/q)^k \pi(0). $$

Here $\pi$ can be normalized to be a probability distribution, in which case

$$ \pi(k) = (p/q)^k (1 - p/q). $$

Since there is a solution to $\pi P = \pi$ which is a probability distribution, the chain is positive recurrent.

By Proposition 1.20, if a solution can be found to the detailed balance equations

$$ \pi(x)P(x,y) = \pi(y)P(y,x), \quad x, y \in \mathcal{X}, $$

then provided $\pi$ is a probability distribution, the chain is positive recurrent.

EXAMPLE 21.18 (Birth-and-death chains). A ***birth-and-death*** chain on $\{0, 1, \ldots, \}$ is a nearest-neighbor chain which moves up when at $k$ with probability $p_k$ and down with probability $q_k = 1 - p_k$. The detailed balance equations are, for $j \geq 1$,

$$ \pi(j)p_j = \pi(j+1)q_{j+1}. $$

Thus $\pi(j+1)/\pi(j) = p_j/q_{j+1}$ and so

$$ \pi(k) = \pi(0) \prod_{j=0}^{k-1} \frac{\pi(j+1)}{\pi(j)} = \pi(0) \prod_{j=0}^{k-1} \frac{p_j}{q_{j+1}}. $$

This can be made into a probability distribution provided that

$$ \sum_{k=1}^{\infty} \prod_{j=0}^{k-1} \frac{p_j}{q_{j+1}} < \infty, \tag{21.16} $$

in which case we take $\pi(0)^{-1}$ to equal this sum.

If the sum in (21.16) is finite, the chain is positive recurrent.

### PDF page 316 (book page 300)

**21.4. Null Recurrence and Convergence**

We now discuss the asymptotic behavior of $P^t(x, y)$ in the null recurrent case.

THEOREM 21.19. *If $P$ is the transition matrix on $\mathcal{X}$ of a null-recurrent irreducible chain, then*

$$ \lim_{t \to \infty} P^t(x, y) = 0 \quad \text{for all } x, y \in \mathcal{X}. \tag{21.17} $$

PROOF. We first prove this under the assumption that $P$ is aperiodic.

Define by (21.11) the measure $\mu = \tilde{\pi}_y$, which is a stationary measure for $P$, and satisfies $\mu(y) = 1$. By null recurrence, $\mu(\mathcal{X}) = \infty$.

Consider the transition matrix $Q$ defined in (21.13). As we remark there, aperiodicity of $P$ implies that $Q$ is irreducible. If $\sum_t P^t(x,y)^2 < \infty$, then we are done, so we assume that $\sum_t P^t(x,y)^2 = \infty$. This implies that $Q$ is recurrent.

Take a finite set $A$ with $\mu(A) > M$, which exists since $\mu(\mathcal{X}) = \infty$. The measure

$$ \mu_A(z) = \frac{\mu(z)}{\mu(A)} \mathbf{1}\{z \in A\} $$

satisfies

$$ \mu_A P^n \leq \frac{\mu P^n}{\mu(A)} = \frac{\mu}{\mu(A)} \,. $$

Let $(X_t, Z_t)$ be a chain started from $\delta_x \times \mu_A$ with transition matrix $Q$. Then $(X_t, Z_t)$ is irreducible and recurrent, so the stopping time $\tau$ equal to the first hitting time of $(x, x)$ is finite almost surely. Defining

$$ \tilde{Z}_t = \begin{cases} Z_t & \text{if } t < \tau, \\ X_t & \text{if } t \geq \tau \,, \end{cases} $$

the process $(\tilde{Z}_t)$ is a Markov chain with the same distribution as $(Z_t)$. We have that

$$ \mathbf{P}_{x,\mu_A}\{\tilde{Z}_t = y\} = \mu_A P^t(y) \leq \frac{\mu(y)}{\mu(A)} \leq \frac{1}{M} \,. $$

Thus,

$$ \mathbf{P}_x\{X_t = y\} \leq \mathbf{P}_{x,\mu_A}\{\tau > t\} + \mathbf{P}_{x,\mu_A}\{\tilde{Z}_t = y\} \,, $$

whence

$$ \limsup_{t \to \infty} \mathbf{P}_x\{X_t = y\} \leq \frac{1}{M} \,. $$

Since $M$ was arbitrary, this proves (21.17) for aperiodic $P$.

Now suppose that $P$ is periodic. Fix $x, y \in \mathcal{X}$, and let

$$ \ell := \gcd\{t \,:\, P^t(x, x) > 0\} \,. $$

There exists $q, r$ (depending on $x, y$) such that $P^{q\ell+r}(x, y) > 0$. The definition of $\ell$ implies that $P^s(y, x) > 0$ only if $s = -r \mod \ell$. Therefore, $P^t(x, y) > 0$ only if $t = r \mod \ell$. Let

$$ \mathcal{X}_r = \{z \in \mathcal{X} \,:\, P^{s\ell+r}(x, z) > 0 \text{ for some } s \geq 0\} \,. $$

By an argument analogous to the one immediately above, $P^\ell$ is irreducible on $\mathcal{X}_r$. Clearly $P^\ell$ is also null recurrent, whence every $z \in \mathcal{X}_r$ satisfies $P^{kl}(z, y) \to 0$. Since

$$ P^{k\ell+r}(x, y) = \sum_{z \in \mathcal{X}_r} P^r(x, z) P^{k\ell}(z, y) \,, $$

Exercise 21.10 implies that $P^{k\ell+r}(x, y) \to 0$ as $k \to \infty$. $\blacksquare$

### PDF page 317 (book page 301)

**21.5. Bounds on Return Probabilities**

THEOREM 21.20. *Let $G$ be an infinite graph with maximum degree at most $\Delta$, and consider the lazy simple random walk on $G$. For an integer $r > 0$ let $B(x, r)$ denote the ball of radius $r$ (using the graph distance) centered at $x$. Then*

$$ P^T(x, x) \leq \frac{\Delta}{|B(x, r)|} + \frac{2\Delta^2 r}{T}. \tag{21.18} $$

*Taking $r = \lfloor \sqrt{T} \rfloor$ in (21.18) shows that*

$$ P^T(x, x) \leq \frac{3\Delta^2}{\sqrt{T}} \quad \text{for all } T > 0 \,. $$

*If $T = r \cdot |B(x, r)|$ , then*

$$ P^T(x, x) \leq \frac{3\Delta^2}{|B(x, r)|}. $$

PROOF. It is clear that in order to prove the statement we may assume we are performing a random walk on the *finite* graph $B(x, T)$ instead of $G$. Let $(X_t)_{t=0}^{\infty}$ denote the lazy simple random walk on $B(x, T)$ and denote its stationary distribution by $\pi$. Define

$$ \tau(x) := \min\{t \geq T \,:\, X_t = x\} \,. $$

We also consider the ***induced chain*** on $B = B(x, r)$ and denote this by $(\tilde{X}_t)_{t=1}^{\infty}$. To define it formally, let $\tau_1 < \tau_2 < \cdots$ be all the times such that $X_{\tau_t} \in B$ and write $\tilde{X}_t = X_{\tau_t}$. We write $\tilde{\pi}$ for the corresponding stationary distribution on $B = B(x, r)$ and $\tilde{\tau}(x)$ for the smallest $t$ such that $\tau_t \geq T$ and $\tilde{X}_t = x$. For any $x \in B$ we have that $\pi(x) = \tilde{\pi}(x)\pi(B)$. Also, Lemma 10.5 gives that

$$ \mathbf{E}_x \,(\text{number of visits of } X_t \text{ to } y \text{ before time } \tau(x)) = \pi(y)\mathbf{E}_x\tau(x). $$

We sum this over $y \in B$ to get

$$ \mathbf{E}_x \,(\text{number of visits of } X_t \text{ to } B \text{ before time } \tau(x)) = \pi(B)\mathbf{E}_x\tau(x). $$

Observe that the number of visits of $X_t$ to $B$ before $\tau(x)$ equals $\tilde{\tau}(x)$ and hence

$$ \mathbf{E}_x\tau(x) = \frac{\mathbf{E}_x\tilde{\tau}(x)}{\pi(B)}. \tag{21.19} $$

We now use Lemma 10.5 again to get

$$ \sum_{t=0}^{T-1} P^t(x, x) = \mathbf{E}_x \,(\text{number of visits to } x \text{ before time } \tau(x)) $$
$$ = \pi(x)\mathbf{E}_x\tau(x) = \tilde{\pi}(x)\mathbf{E}_x\tilde{\tau}(x), \tag{21.20} $$

where the last equality is due to (21.19). Denote by $\sigma$ the minimal $t \geq T$ such that $X_t \in B$ and let $\nu$ be the distribution of $X_\sigma$. Observe that $\mathbf{E}_x\tilde{\tau}(x) \leq T + \mathbf{E}_\nu\tilde{\tau}_0(x)$ where $\tilde{\tau}_0(x)$ is the first hitting time of $x$ in the induced chain. Since $P^t(x, x)$ is weakly decreasing in $t$ (Proposition 10.25), we infer that

$$ TP^T(x, x) \leq \tilde{\pi}(x)[T + \mathbf{E}_\nu\tilde{\tau}_0(x)]. $$

The effective resistances in the induced chain and the original chain are the same; see Exercise 21.11. We use the Commute Time Identity (Proposition 10.7) and bound the effective resistance from above by the distance to get

$$ \mathbf{E}_\nu\tilde{\tau}_0(x) \leq 2\Delta r|B(x, r)|. $$

### PDF page 318 (book page 302)

Since $\widetilde{\pi}(x) \leq \Delta/|B(x,r)|$, we conclude that

$$ TP^T(x,x) \leq \frac{\Delta T}{|B(x,r)|} + 2\Delta^2 r. $$

This immediately gives that

$$ P^T(x,x) \leq \frac{\Delta}{|B(x,r)|} + \frac{2\Delta^2 r}{T}. $$

$\blacksquare$

**Exercises**

EXERCISE 21.1. Use the Strong Law of Large Numbers to prove that the biased random walk in Example 21.2 is transient.

EXERCISE 21.2. Suppose that $P$ is irreducible. Show that if $\pi = \pi P$ for a probability distribution $\pi$, then $\pi(x) > 0$ for all $x \in \mathcal{X}$.

EXERCISE 21.3. Fix $k > 1$. Define the $k$**-fuzz** of an undirected graph $G = (V,E)$ as the graph $G_k = (V, E_k)$ where for any two distinct vertices $v, w \in V$, the edge $\{v,w\}$ is in $E_k$ if and only if there is a path of at most $k$ edges in $E$ connecting $v$ to $w$. Show that for $G$ with bounded degrees, $G$ is transient if and only if $G_k$ is transient.

A solution can be found in Doyle and Snell (1984, Section 8.4).

EXERCISE 21.4. Show that any subgraph of a recurrent graph must be recurrent.

EXERCISE 21.5. Consider lazy random walk on an infinite graph $G$. Show that $\sum_t P^t(x,x)^3 < \infty$.

EXERCISE 21.6. Let $P$ be an irreducible and aperiodic transition matrix on $\mathcal{X}$. Let $Q$ be the matrix on $\mathcal{X} \times \mathcal{X}$ defined by

$$ Q((x,y), (z,w)) = P(x,z)P(y,w), \quad (x,y) \in \mathcal{X} \times \mathcal{X}, \ (z,w) \in \mathcal{X} \times \mathcal{X}. $$

Show that $Q$ is irreducible.

EXERCISE 21.7. Consider the discrete-time single server FIFO (first in, first out) queue: at every step, if there is a customer waiting, exactly one of the following happens:

&nbsp;&nbsp;&nbsp;&nbsp;(1) a new customer arrives (with probability $\alpha$) or
&nbsp;&nbsp;&nbsp;&nbsp;(2) an existing customer is served (with probability $\beta = 1 - \alpha$).

If there are no customers waiting, then (1) still has probability $\alpha$, but (2) is replaced by "nothing happens". Let $X_t$ be the number of customers in the queue at time $t$.
&nbsp;&nbsp;&nbsp;&nbsp;Show that $(X_t)$ is

(a) positive recurrent if $\alpha < \beta$,
(b) null recurrent if $\alpha = \beta$,
(c) transient if $\alpha > \beta$.

EXERCISE 21.8. Consider the same set-up as Exercise 21.7. In the positive recurrent case, determine the stationary distribution $\pi$ and the $\pi$-expectation of the time $T$ from the arrival of a customer until he is served.

### PDF page 319 (book page 303)

EXERCISE 21.9. Let $P$ be the transition matrix for simple random walk on $\mathbb{Z}$. Show that the walk is not positive recurrent by showing there are no probability distributions $\pi$ on $\mathbb{Z}$ satisfying $\pi P = \pi$.

EXERCISE 21.10. Let $\{f_t\}_{t \geq 0}$ be a sequence of functions on a countable space $\mathcal{X}$, and let $\pi$ be a measure on $\mathcal{X}$ with $\sum_{y \in \mathcal{X}} \pi(y) = M < \infty$. Suppose that $\lim_{t \to \infty} f_t(y) = 0$ for all $y$, and $|f_t(y)| \leq B$ for all $t$ and $y$. Show that

$$ \lim_{t \to \infty} \sum_{y \in \mathcal{X}} \pi(y) f_t(y) = 0 \,. $$

EXERCISE 21.11.

(a) Suppose $\nu$ is a reversing measure for $P$, i.e. satisifies [sic]

$$ \nu(x)P(x,y) = \nu(y)P(y,x) \,, $$

and let $P_A$ be the induced chain on the set $A$. Show that the restriction of $\nu$ to $A$ is a reversing measure for $P_A$.
(b) Give the original chain edge-conductances $c(x,y) = \nu(x)P(x,y)$, and the induced chain edge-conductances $c_A(x,y) = \nu(x)P_A(x,y)$. Show that for any two states $z, w$,

$$ \mathcal{R}(z \leftrightarrow w) = \mathcal{R}_A(z \leftrightarrow w) \,. $$

*Hint:* Consider escape probabilities.

EXERCISE 21.12. Let $P$ be an irreducible transition matrix on $\mathcal{X}$. Show that $P$ is transient if and only if there exists $h : \mathcal{X} \to [0, \infty)$ which is non-constant and satisfies $Ph \leq h$.

EXERCISE 21.13. Show that for simple random walk on $\mathbb{Z}^3$, the function $h(x) = \|x\|_2^{-\alpha} \wedge \varepsilon$, where $\alpha < 1$, satisfies $Ph \leq h$ for $\varepsilon$ small enough, and conclude that the walk is transient.

EXERCISE 21.14. Let $P$ be an irreducible transition matrix on $\mathcal{X}$. A (positive) measure $\mu$ on $\mathcal{X}$ is *excessive* if $\mu \geq \mu P$. Show that if there exists an excessive measure which is not stationary, then the chain is transient.

*Hint:* Let $\pi$ be a stationary measure. Show that $\frac{\mu}{\pi}$ is superharmonic for the reversed chain.

EXERCISE 21.15. Let $P$ be an irreducible transition matrix on $\mathcal{X}$ which is transient. Show that there exists an excessive measure which is not stationary.

EXERCISE 21.16. Divide $\mathbb{Z}^2$ into four quadrants by the two main diagonals in $\mathbb{Z}^2$. If a particle is in the right or left quadrants, it moves up or down each with probability 0.3, and left or right each with probabilities 0.2 each. If the particle is in the upper or lower quadrants, it moves up or down each with probability 0.2, and left or right each with probabilities 0.3. On the diagonals, the particle moves to each neighbor with probability 0.25.
&nbsp;&nbsp;&nbsp;&nbsp;Use the previous exercise to show that this chain is transient.

EXERCISE 21.17. Let $P$ be an irreducible transition matrix on $\mathcal{X}$. Suppose that there exists $h : \mathcal{X} \to [0, \infty)$ such that $Ph(x) \leq h(x)$ for all $x \notin A$, where $A$ is a finite set, and $h(x) \to \infty$ as $x \to \infty$. Show that the chain is recurrent.

EXERCISE 21.18. Let $P$ be the transition matrix for simple random walk on $\mathbb{Z}^2$. Let $h(x) = \sqrt{\log(\|x\|_2)}$. Show that $Ph(x) \leq h(x)$ for $\|x\|_2 > r$ for some $r$, and conclude that the chain is recurrent.

### PDF page 320 (book page 304)

**Notes**

**Further reading.** Many texts, including Feller (1968) and Doyle and Snell (1984), also give proofs of the recurrence of random walk in one and two dimensions and of the transience in three or more.

Lyons (1983) used flows for analyzing chains with infinite state spaces.

For much more on infinite networks, see Soardi (1994), Woess (2000), Lyons and Peres (2016), and Barlow (2017).

Pólya's Urn is used to construct flows in Levin and Peres (2010), proving the transience of $\mathbb{Z}^d$ for $d \geq 3$.

For more on Markov chains with infinite state spaces, see, e.g., Feller (1968), Norris (1998), or Kemeny, Snell, and Knapp (1976). See also Thorisson (2000).

The proof of Theorem 21.19 comes from Thorisson (2000).

Theorem 21.20 is from Barlow, Coulhon, and Kumagai (2005) (see Proposition 3.3 there), although the proof given here is different.

For more on effective resistence in induced chains, as discussed in Exercise 21.11, see Exercise 2.69 in Lyons and Peres (2016).

For non-reversible chains, determining transience/recurrence can be difficult. See Zeitouni (2004), where the chain in Exercise 21.16, due to Nina Gantert, is discussed. For generalizations of Exercise 21.13, see Lemma 2.2 of Peres, Popov, and Sousi (2013). Exercises 21.12 through 21.18 are examples of the method of Lyapunov functions; for a comprehensive account of this method, see Menshikov, Popov, and Wade (2017).

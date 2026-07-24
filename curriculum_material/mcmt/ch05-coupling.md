# Chapter 5 — Coupling
*(PDF pages 76–90; book pages 60–74)*

### PDF page 76 (book page 60)

CHAPTER 5

# Coupling

**5.1. Definition**

As we defined in Section 4.1, a coupling of two probability distributions $\mu$ and $\nu$ is a pair of random variables $(X, Y)$, defined on the same probability space, such that the marginal distribution of $X$ is $\mu$ and the marginal distribution of $Y$ is $\nu$.

Couplings are useful because a comparison between distributions is reduced to a comparison between random variables. Proposition 4.7 characterized $\|\mu - \nu\|_{\mathrm{TV}}$ as the minimum, over all couplings $(X, Y)$ of $\mu$ and $\nu$, of the probability that $X$ and $Y$ are different. This provides an effective method of obtaining upper bounds on the total variation distance.

In this chapter, we will extract more information by coupling not only pairs of distributions, but entire Markov chain trajectories. Here is a simple initial example.

EXAMPLE 5.1. A simple random walk on the segment $\{0, 1, \ldots, n\}$ is a Markov chain which moves either up or down at each move with equal probability. If the walk attempts to move outside the interval when at a boundary point, it stays put. It is intuitively clear that $P^t(x, n) \leq P^t(y, n)$ whenever $x \leq y$, as this says that the chance of being at the "top" value $n$ after $t$ steps does not decrease as you increase the height of the starting position.

A simple proof uses a coupling of the distributions $P^t(x, \cdot)$ and $P^t(y, \cdot)$. Let $\Delta_1, \Delta_2, \ldots$ be a sequence of i.i.d. (that is, independent and identically distributed)

**FIGURE 5.1.** Coupled random walks on $\{0, 1, 2, 3, 4\}$. The walks stay together after meeting. *[Figure: a plot with vertical axis labeled 0,1,2,3,4. Two coupled random walk trajectories start at labeled points — $y$ at height 3 (walk $Y_t$) and $x$ at height 2 (walk $X_t$) — descend, meet, and then continue together as a single bold path with an arrow at the end.]*

### PDF page 77 (book page 61)

$\{-1, 1\}$-valued random variables with zero mean, so each $\Delta_i$ is equally likely to be $+1$ as $-1$. We will define together two random walks on $\{0, 1, \ldots, n\}$: the walk $(X_t)$ starts at $x$, while the walk $(Y_t)$ starts at $y$.

We use the same rule for moving in both chains $(X_t)$ and $(Y_t)$: if $\Delta_t = +1$, move the chain up if possible, and if $\Delta_t = -1$, move the chain down if possible. Once the two chains meet (necessarily either at 0 or $n$), they stay together thereafter.

Clearly the distribution of $X_t$ is $P^t(x, \cdot)$, and the distribution of $Y_t$ is $P^t(y, \cdot)$. Importantly, $X_t$ and $Y_t$ are defined on the same underlying probability space, as both chains use the sequence $(\Delta_t)$ to determine their moves.

It is clear that if $x \leq y$, then $X_t \leq Y_t$ for all $t$. In particular, if $X_t = n$, the top state, then it must be that $Y_t = n$ also. From this we can conclude that

$$ P^t(x, n) = \mathbf{P}\{X_t = n\} \leq \mathbf{P}\{Y_t = n\} = P^t(y, n). \tag{5.1} $$

This argument shows the power of coupling. We were able to couple together the two chains in such a way that $X_t \leq Y_t$ always, and from this fact about the random variables we could easily read off information about the distributions.

In the rest of this chapter, we will see how building two simultaneous copies of a Markov chain using a common source of randomness, as we did in the previous example, can be useful for getting bounds on the distance to stationarity.

We define a ***coupling of Markov chains*** with transition matrix $P$ to be a process $(X_t, Y_t)_{t=0}^{\infty}$ with the property that both $(X_t)$ and $(Y_t)$ are Markov chains with transition matrix $P$, although the two chains may possibly have different starting distributions.

Given a Markov chain on $\mathcal{X}$ with transition matrix $P$, a ***Markovian coupling*** of two $P$-chains is a Markov chain $\{(X_t, Y_t)\}_{t \geq 0}$ with state space $\mathcal{X} \times \mathcal{X}$ which satisfies, for all $x, y, x', y'$,

$$ \mathbf{P}\{X_{t+1} = x' \mid X_t = x, \ Y_t = y\} = P(x, x') $$
$$ \mathbf{P}\{Y_{t+1} = y' \mid X_t = x, \ Y_t = y\} = P(y, y') \,. $$

EXAMPLE 5.2. Consider the transition matrix on $\{0, 1\}$ given by

$$ P(x, y) = \frac{1}{2} \quad \text{for all } x, y \in \{0, 1\} \,, $$

corresponding to a sequence of i.i.d. fair bits. Let $(Y_t)_{t \geq 0}$ be a Markov chain with transition matrix $P$ started with a fair coin toss, and set $X_0 = 0$ and $X_{t+1} = Y_t$ for $t \geq 0$. Both $(X_t)$ and $(Y_t)$ are Markov chains with transition matrix $P$, so $\{(X_t, Y_t)\}$ is a coupling. Moreover, the sequence $\{(X_t, Y_t)\}_{t \geq 0}$ is itself a Markov chain, but it is not a Markovian coupling.

REMARK 5.3. All couplings used in this book will be Markovian.

Any Markovian coupling of Markov chains with transition matrix $P$ can be modified so that the two chains stay together at all times after their first simultaneous visit to a single state—more precisely, so that

$$ \text{if } X_s = Y_s, \text{ then } X_t = Y_t \text{ for } t \geq s. \tag{5.2} $$

To construct a coupling satisfying (5.2), simply run the chains according to the original coupling until they meet, then run them together.

### PDF page 78 (book page 62)

NOTATION. If $(X_t)$ and $(Y_t)$ are coupled Markov chains with $X_0 = x$ and $Y_0 = y$, then we will often write $\mathbf{P}_{x,y}$ for the probability on the space where $(X_t)$ and $(Y_t)$ are both defined.

**5.2. Bounding Total Variation Distance**

As usual, we will fix an irreducible transition matrix $P$ on the state space $\mathcal{X}$ and write $\pi$ for its stationary distribution. The following is the key tool used in this chapter.

THEOREM 5.4. *Let $\{(X_t, Y_t)\}$ be a coupling satisfying* (5.2) *for which $X_0 = x$ and $Y_0 = y$. Let $\tau_{\mathrm{couple}}$ be the coalescence time of the chains:*

$$ \tau_{\mathrm{couple}} := \min\{t \,:\, X_s = Y_s \text{ for all } s \geq t\}. \tag{5.3} $$

*Then*

$$ \left\| P^t(x, \cdot) - P^t(y, \cdot) \right\|_{\mathrm{TV}} \leq \mathbf{P}_{x,y}\{\tau_{\mathrm{couple}} > t\}. \tag{5.4} $$

PROOF. Notice that $P^t(x, z) = \mathbf{P}_{x,y}\{X_t = z\}$ and $P^t(y, z) = \mathbf{P}_{x,y}\{Y_t = z\}$. Consequently, $(X_t, Y_t)$ is a coupling of $P^t(x, \cdot)$ with $P^t(y, \cdot)$, whence Proposition 4.7 implies that

$$ \left\| P^t(x, \cdot) - P^t(y, \cdot) \right\|_{\mathrm{TV}} \leq \mathbf{P}_{x,y}\{X_t \neq Y_t\}. \tag{5.5} $$

By (5.2), $\mathbf{P}_{x,y}\{X_t \neq Y_t\} = \mathbf{P}_{x,y}\{\tau_{\mathrm{couple}} > t\}$, which with (5.5) establishes (5.4). $\blacksquare$

Combining Theorem 5.4 with Lemma 4.10 proves the following:

COROLLARY 5.5. *Suppose that for each pair of states $x, y \in \mathcal{X}$ there is a coupling $(X_t, Y_t)$ with $X_0 = x$ and $Y_0 = y$. For each such coupling, let $\tau_{\mathrm{couple}}$ be the coalescence time of the chains, as defined in* (5.3)*. Then*

$$ d(t) \leq \max_{x,y \in \mathcal{X}} \mathbf{P}_{x,y}\{\tau_{\mathrm{couple}} > t\} \,, $$

*and therefore $t_{\mathrm{mix}} \leq 4 \max_{x,y} \mathbf{E}_{x,y}(\tau_{\mathrm{couple}})$.*

**5.3. Examples**

**5.3.1. Random walk on the hypercube.** The simple random walk on the hypercube $\{0, 1\}^n$ was defined in Section 2.3.

To avoid periodicity, we study the lazy chain: at each time step, the walker remains at her current position with probability $1/2$ and with probability $1/2$ moves to a position chosen uniformly at random among all neighboring vertices.

As remarked in Section 2.3, a convenient way to generate the lazy walk is as follows: pick one of the $n$ coordinates uniformly at random, and *refresh* the bit at this coordinate with a random fair bit (one which equals 0 or 1 each with probability $1/2$).

This algorithm for running the walk leads to the following coupling of two walks with possibly different starting positions: first, pick among the $n$ coordinates uniformly at random; suppose that coordinate $i$ is selected. *In both walks*, replace the bit at coordinate $i$ *with the same* random fair bit. (See Figure 5.2.) From this time onwards, both walks will agree in the $i$-th coordinate. A moment's thought reveals that individually each of the walks is indeed a lazy random walk on the hypercube.

### PDF page 79 (book page 63)

**FIGURE 5.2.** One step in two coupled lazy walks on the hypercube. First, choose a coordinate to update—here, the sixth. Then, flip a 0/1 coin and use the result to update the chosen coordinate to the same value in both walks. *[Figure: Two coupled binary strings, each labeled "Copy 1:" and "Copy 2:". Top pair — Copy 1: `0 0 1 1 0 [1] 0 0 1 1`, Copy 2: `0 1 1 0 0 [0] 1 0 1 0`, with the sixth coordinate boxed in each. A curved arrow at the top right points to a small oval containing "1" (a coin flip). A large brace beneath the top pair leads to the bottom pair — Copy 1: `0 0 1 1 0 [1] 0 0 1 1`, Copy 2: `0 1 1 0 0 [1] 1 0 1 0`, with the sixth coordinate now boxed and set to 1 in both copies.]*

If $\tau$ is the first time when all of the coordinates have been selected at least once, then the two walkers agree with each other from time $\tau$ onwards. (If the initial states agree in some coordinates, the first time the walkers agree could be strictly before $\tau$.) The distribution of $\tau$ is exactly the same as the coupon collector random variable studied in Section 2.2. Using Corollary 5.5, together with the bound on the tail of $\tau$ given in Proposition 2.4, shows that

$$ d(n \log n + cn) \leq \mathbf{P}\{\tau > n \log n + cn\} \leq e^{-c}. $$

It is immediate from the above that

$$ t_{\mathrm{mix}}(\varepsilon) \leq n \log n + \log(1/\varepsilon)n. \tag{5.6} $$

Simply, $t_{\mathrm{mix}} = O(n \log n)$. The upper bound in (5.6) is off by a factor of two and will be sharpened in Section 18.2.2 via a more sophisticated coupling. The corresponding lower bound is in Proposition 7.14.

**5.3.2. Random walk on the cycle.** We defined random walk on the $n$-cycle in Example 1.4. The underlying graph of this walk, $\mathbb{Z}_n$, has vertex set $\{1, 2, \ldots, n\}$ and edges between $j$ and $k$ whenever $j \equiv k \pm 1 \mod n$. See Figure 1.3.

We consider the lazy $(p-q)$-biased walk, which remains in its current position with probability $1/2$, moves clockwise with probability $p/2$, and moves counterclockwise with probability $q/2$. Here $p + q = 1$, and we allow the unbiased case $p = q = \frac{1}{2}$.

We show that $\frac{1}{32}n^2 \leq t_{\mathrm{mix}} \leq n^2$.

*Upper bound.* We construct a coupling $(X_t, Y_t)$ of two particles performing lazy walks on $\mathbb{Z}_n$, one started from $x$ and the other started from $y$. In this coupling, the two particles will never move simultaneously, ensuring that they will not jump over one another when they come to within unit distance. Until the two particles meet, at each unit of time, a fair coin is tossed, independent of all previous tosses, to determine which of the two particles will jump. The particle that is selected makes a clockwise increment with probability $p$ and a counter-clockwise increment with probability $q$. Once the two particles collide, thereafter they make identical moves. Let $D_t$ be the clockwise distance from $X_t$ to $Y_t$. Note that the process $(D_t)$ is a simple random walk on the interior vertices of $\{0, 1, 2, \ldots, n\}$ and gets absorbed at either $0$ or $n$. By Proposition 2.1, if $\tau = \min\{t \geq 0 \, : \, D_t \in \{0, n\}\}$,

### PDF page 80 (book page 64)

**FIGURE 5.3.** The 2-torus $\mathbb{Z}_{20}^2$. *[Figure: A 3D rendering of a torus (doughnut shape) whose surface is drawn as a grid mesh, representing the graph $\mathbb{Z}_{20}^2$.]*

then $\mathbf{E}_{x,y}(\tau) = k(n-k)$, where $k$ is the clockwise distance between $x$ and $y$. Since $\tau = \tau_{\mathrm{couple}}$, by Corollary 5.5,

$$ d(t) \leq \max_{x,y \in \mathbb{Z}_n} \mathbf{P}_{x,y}\{\tau > t\} \leq \frac{\max_{x,y} \mathbf{E}_{x,y}(\tau)}{t} \leq \frac{n^2}{4t}. $$

The right-hand side equals $1/4$ for $t = n^2$, whence $t_{\mathrm{mix}} \leq n^2$.

*Lower bound.* Suppose that $X_0 = x_0$. Let $(S_t)$ be lazy $(p-q)$-biased random walk on $\mathbb{Z}$, write $X_t = S_t \mod n$, and let $\rho$ be distance on the cycle. If $\mu_t = t(p-q)/2$, set

$$ A_t = \{k \, : \, \rho(k, \lfloor x_0 + \mu_t \rfloor \mod n) \geq n/4\} . $$

Note that $\pi(A_t) \geq 1/2$. Using Chebyshev's inequality, since $\mathrm{Var}(S_t) = t(\frac{1}{4} + pq) \leq t/2$,

$$ \mathbf{P}\{X_t \in A_t\} \leq \mathbf{P}\{|S_t - \mu_t| \geq n/4\} \leq \frac{8t}{n^2} < \frac{1}{4} $$

for $t < n^2/32$. Thus, for $t < n^2/32$,

$$ d(t) \geq \pi(A_t) - \mathbf{P}\{X_t \in A_t\} > \frac{1}{2} - \frac{1}{4} \, , $$

so $t_{\mathrm{mix}} \geq n^2/32$.

**5.3.3. Random walk on the torus.** The *$d$-dimensional torus* is the graph whose vertex set is the Cartesian product

$$ \mathbb{Z}_n^d = \underbrace{\mathbb{Z}_n \times \cdots \times \mathbb{Z}_n}_{d \text{ times}} . $$

Vertices $\boldsymbol{x} = (x^1, \ldots, x^d)$ and $\boldsymbol{y} = (y^1, y^2, \ldots, y^d)$ are neighbors in $\mathbb{Z}_n^d$ if for some $j \in \{1, 2, \ldots, d\}$, we have $x^i = y^i$ for all $i \neq j$ and $x^j \equiv y^j \pm 1 \mod n$. See Figure 5.3 for an example.

When $n$ is even, the graph $\mathbb{Z}_n^d$ is bipartite and the associated random walk is periodic. To avoid this complication, we consider the lazy random walk on $\mathbb{Z}_n^d$, defined in Section 1.3. This walk remains at its current position with probability $1/2$ at each move.

We now use coupling to bound the mixing time of the lazy random walk on $\mathbb{Z}_n^d$.

### PDF page 81 (book page 65)

THEOREM 5.6. *For the lazy random walk on the d-dimension torus $\mathbb{Z}_n^d$, if $\varepsilon < \frac{1}{2}$, then*

$$ t_{\mathrm{mix}}(\varepsilon) \leq dn^2 \lceil \log_4(d/\varepsilon) \rceil . \tag{5.7} $$

PROOF. We prove $t_{\mathrm{mix}} \leq d^2 n^2$, and leave as a solved exercise (Exercise 5.4) the stated bound.

In order to apply Corollary 5.5 to prove this theorem, we construct a coupling for each pair $(\boldsymbol{x}, \boldsymbol{y})$ of starting states and bound the expected value of the coupling time $\tau_{\mathrm{couple}} = \tau_{\boldsymbol{x}, \boldsymbol{y}}$.

To couple together a random walk $(\boldsymbol{X}_t)$ started at $\boldsymbol{x}$ with a random walk $(\boldsymbol{Y}_t)$ started at $\boldsymbol{y}$, first pick one of the $d$ coordinates at random. If the positions of the two walks agree in the chosen coordinate, we move both of the walks by $+1$, $-1$, or $0$ in that coordinate, with probabilities $1/4$, $1/4$ and $1/2$, respectively. If the positions of the two walks differ in the chosen coordinate, we randomly choose one of the chains to move, leaving the other fixed. We then move the selected walk by $+1$ or $-1$ in the chosen coordinate, with the sign determined by a fair coin toss.

Let $\boldsymbol{X}_t = (X_t^1, \ldots, X_t^d)$ and $\boldsymbol{Y}_t = (Y_t^1, \ldots, Y_t^d)$, and let

$$ \tau_i := \min\{t \geq 0 \, : \, X_t^i = Y_t^i\} $$

be the time required for the chains to agree in coordinate $i$.

The clockwise difference between $X_t^i$ and $Y_t^i$, viewed at the times when coordinate $i$ is selected, behaves just as the coupling of the lazy walk on the cycle $\mathbb{Z}_n$ discussed above. Thus, the expected number of moves in coordinate $i$ needed to make the two chains agree on that coordinate is not more than $n^2/4$.

Since coordinate $i$ is selected with probability $1/d$ at each move, there is a geometric waiting time between moves with expectation $d$. Exercise 5.3 implies that

$$ \mathbf{E}_{\boldsymbol{x}, \boldsymbol{y}}(\tau_i) \leq \frac{dn^2}{4}. \tag{5.8} $$

The coupling time we are interested in is $\tau_{\mathrm{couple}} = \max_{1 \leq i \leq d} \tau_i$, and we can bound the maximum by a sum to get

$$ \mathbf{E}_{\boldsymbol{x}, \boldsymbol{y}}(\tau_{\mathrm{couple}}) \leq \frac{d^2 n^2}{4}. \tag{5.9} $$

This bound is independent of the starting states, and we can use Markov's inequality to show that

$$ \mathbf{P}_{\boldsymbol{x}, \boldsymbol{y}}\{\tau_{\mathrm{couple}} > t\} \leq \frac{\mathbf{E}_{\boldsymbol{x}, \boldsymbol{y}}(\tau_{\mathrm{couple}})}{t} \leq \frac{1}{t} \frac{d^2 n^2}{4}. \tag{5.10} $$

Taking $t_0 = d^2 n^2$ shows that $d(t_0) \leq 1/4$, and so $t_{\mathrm{mix}} \leq d^2 n^2$. $\blacksquare$

**5.3.4. Random walk on a finite binary tree.** Since trees will appear in several examples in the sequel, we collect some definitions here. A ***tree*** is a connected graph with no cycles. (See Exercise 1.3 and Exercise 1.4.) A ***rooted*** tree has a distinguished vertex, called the ***root***. The ***depth*** of a vertex $v$ is its graph distance to the root. A ***level*** of the tree consists of all vertices at the same depth. The ***children*** of $v$ are the neighbors of $v$ with depth larger than $v$. A ***leaf*** is a vertex with degree one.

A ***rooted finite $b$-ary tree of depth*** $k$, denoted by $T_{b,k}$, is a tree with a distinguished vertex $\rho$, the root, such that

- $\rho$ has degree $b$,

### PDF page 82 (book page 66)

- every vertex at distance $j$ from the root, where $1 \leq j \leq k-1$, has degree $b+1$,
- the vertices at distance $k$ from $\rho$ are leaves.

There are $n = (b^{k+1} - 1)/(b-1)$ vertices in $T_{b,k}$.

In this example, we consider the lazy random walk on the finite **binary tree** $T_{2,k}$; this walk remains at its current position with probability $1/2$.

**FIGURE 5.4.** A binary tree of height 3. *[Figure: a complete binary tree drawn top-down — a single root node at top, branching into 2 nodes, then 4 nodes, then 8 leaf nodes at the bottom.]*

Consider the following coupling $(X_t, Y_t)$ of two lazy random walks, started from states $x_0$ and $y_0$ on the tree. Assume, without loss of generality, that $x_0$ is at least as close to the root as $y_0$. At each move, toss a fair coin to decide which of the two chains moves: if the coin lands heads, then $Y_{t+1} = Y_t$, while $X_{t+1}$ is chosen from the neighbors of $X_t$ uniformly at random. If the coin toss lands tails, then $X_{t+1} = X_t$, and $Y_{t+1}$ is chosen from the neighbors of $Y_t$ uniformly at random. Run the two chains according to this rule until the first time they are at the same level of the tree. Once the two chains are at the same level, change the coupling to the following updating rule: let $X_t$ evolve as a lazy random walk, and couple $Y_t$ to $X_t$ so that $Y_t$ moves closer to (further from) the root if and only if $X_t$ moves closer to (further from) the root, respectively.

Define
$$
\tau = \min\{t \geq 0 \,:\, X_t = Y_t\}\,,
$$
$$
\tau_\rho = \min\{t \geq 0 \,:\, Y_t = \rho\}\,.
$$
Observe that if $Y_t$ is at the root, then $\tau \leq t$. Thus $\mathbf{E}(\tau) \leq \mathbf{E}_{y_0}(\tau_\rho)$. The distance of $Y_t$ from the leaves is a birth-and-death chain with $p = 1/6$ and $q = 1/3$. By (2.14),
$$
\mathbf{E}_{y_0}(\tau_\rho) \leq -6 \left(k + 2(1 - 2^k)\right) \leq 6n\,.
$$
More careful attention to the holding probabilities at the leaves yields a bound of $4n$. Alternatively, the latter bound can be obtained via the commute time bound derived in Example 10.15.

We conclude that $t_{\mathrm{mix}} \leq 16n$.

**5.3.5. The winning streak.** The *winning streak* chain with window $n$ has a time-reversal with a significantly different mixing time. Indeed, a coupling argument we provide shortly shows that the chain has mixing time at most 2, while a simple direct argument shows that the mixing time of the reversal is exactly $n$.

### PDF page 83 (book page 67)

**FIGURE 5.5.** The winning streak for $n = 5$. Here $X_t = 2$, $X_{t+1} = 3$, and $X_{t+2} = 0$. *[Figure: three rows of bit cells. time $t$: 1 0 1 0 [0 1 1 1 0] 0 0 0, window boxed around "0 1 1 1 0"; time $t+1$: 1 0 1 [0 0 1 1 1] 0 0 0 0, window boxed around "0 0 1 1 1"; time $t+2$: 1 0 [1 0 0 1 1] 1 0 0 0 0, window boxed around "1 0 0 1 1".]*

**FIGURE 5.6.** The time reversal of the winning streak for $n = 5$. Here $\widehat{X}_t = 0$, $\widehat{X}_{t+1} = 3$, and $\widehat{X}_{t+2} = 2$. *[Figure: three rows of bit cells. time $t$: 1 0 [1 0 0 1 1] 1 0 0 0 0, with a window boxed around bits "1 0 0 1 1"; time $t+1$: 1 0 1 [0 0 1 1 1] 0 0 0 0, window boxed around "0 0 1 1 1"; time $t+2$: 1 0 1 0 [0 1 1 1 0] 0 0 0, window boxed around "0 1 1 1 0".]*

**FIGURE 5.7.** The underlying graphs of the transitions of (a) the winning streak chain for $n = 5$ and (b) its time reversal. *[Figure: two directed graphs, each on vertices 0,1,2,3,4,5 arranged in a line. (a): from each vertex arcs go forward to vertex $i+1$ and there is a self-loop at 0 and arcs back to 0 from every vertex (arcs curving from the right vertices back to 0); a self-loop at 5. (b): the mirror image — arcs run leftward between consecutive vertices and long arcs from 0 out to each vertex, self-loops at 0 and 5.]*

Imagine a creature with bounded memory tossing a fair coin repeatedly and trying to track the length of the last run of heads. If more than $n$ heads occur in a row, the creature only remembers $n$ of them. Hence the current state of our chain is the minimum of $n$ and the length of the last run of heads.

For an $n$ bit word $b = (b_1, \ldots, b_n)$, define
$$
r(b) = \begin{cases} 0 & \text{if } b_n = 0, \\ \max\{m \,:\, b_{n-m+1} = \cdots = b_n = 1\} & \text{otherwise}\,. \end{cases}
$$
That is, $r(b)$ is the length of the block of 1's starting at the right-most bit of $b$. For arbitrary initial bits $B_{-n+1}, \ldots, B_0$, and independent fair bits $B_1, B_2, \ldots$, let
$$
X_t = r(B_{t-n+1}, B_{t-n+2}, \ldots, B_t)\,. \tag{5.11}
$$
The sequence $(X_t)$ is a Markov chain with state space $\{0, \ldots, n\}$ and non-zero transitions given by
$$
\begin{aligned}
P(i, 0) &= 1/2 \text{ for } 0 \leq i \leq n, \\
P(i, i+1) &= 1/2 \text{ for } 0 \leq i < n, \\
P(n, n) &= 1/2.
\end{aligned} \tag{5.12}
$$
Starting $(X_t)$ at state $a$ is equivalent to fixing initial bits with $r(B_{-n+1}, \ldots, B_0) = a$. See Figures 5.5 and 5.7. It is straightforward to check that
$$
\pi(i) = \begin{cases} 1/2^{i+1} & \text{if } i = 0, 1, \ldots, n-1, \\ 1/2^n & \text{if } i = n \end{cases} \tag{5.13}
$$

### PDF page 84 (book page 68)

is stationary for $P$.

Fix a pair of initial values $a, b \in \{0, \ldots, n\}$ for the chain. We will couple the chains $(X_t^x)$ and $(Y_t^x)$ by coupling bit streams $(B_t^x)_{t=-n+1}^\infty$ and $(B_t^y)_{t=-n+1}^\infty$, from which the two chains will be constructed as in (5.11). Let $x$ and $y$ be bitstrings of length $n$ whose ending block of 1's have length exactly $a$ and $b$, respectively. We set $(B_{-n+1}^x, \ldots, B_0^x) = x$ and $(B_{-n+1}^y, \ldots, B_0^y) = y$, and for $t \geq 1$, set $B_t^x = B_t^y = B_t$, where $(B_t)_{t=1}^\infty$ is an i.i.d. fair bit sequence. As soon as one of the added bits is 0, both chains fall into state 0, and they remain coupled thereafter.

Hence
$$
\mathbf{P}\{\tau_{\mathrm{couple}} > t\} \leq 2^{-t}
$$
and Corollary 5.5 gives
$$
d(t) \leq 2^{-t}.
$$
By the definition (4.30) of mixing time, we have
$$
t_{\mathrm{mix}}(\varepsilon) \leq \lceil \log_2 \left(\frac{1}{\varepsilon}\right) \rceil,
$$
which depends only on $\varepsilon$, and not on $n$. In particular, $t_{\mathrm{mix}} \leq 2$ for all $n$.

Now for the time-reversal. It is straightforward to check that the time reversal of $P$ has non-zero entries
$$
\begin{aligned}
\widehat{P}(0, i) &= \pi(i) && \text{for } 0 \leq i \leq n, \\
\widehat{P}(i, i-1) &= 1 && \text{for } 1 \leq i < n, \\
\widehat{P}(n, n) = \widehat{P}(n, n-1) &= 1/2. &&
\end{aligned} \tag{5.14}
$$
The coin-flip interpretation of the winning streak carries over to its time reversal. Imagine a window of width $n$ moving *leftwards* along a string of independent random bits. Then the sequence of lengths $(\widehat{X}_t)$ of the rightmost block of 1's in the window is a version of the reverse winning streak chain. See Figures 5.6 and 5.7. Indeed, if $(B_t)_{t=-\infty}^{n-1}$ are the i.i.d. fair bits, then
$$
\widehat{X}_t = r(B_{-t}, \ldots, B_{-t+n-1})\,.
$$
In particular,
$$
\widehat{X}_n = r(B_{-n}, B_{-n+1}, \ldots, B_{-1}),
$$
and $(B_{-n}, \ldots, B_{-1})$ is uniform over all $2^n$ bitwords of length $n$, independent of the initial bits $(B_0, \ldots, B_{n-1})$. From this, it is clear that $\widehat{X}_n$ has the following remarkable property: after $n$ steps, its distribution is exactly stationary, regardless of initial distribution.

For a lower bound, consider the chain started at $n$. On the first move, with probability $1/2$ it moves to $n-1$, in which case after $n-1$ moves it must be at state 1. Hence $\widehat{P}^{n-1}(n, 1) = 1/2$, and the definition (4.1) of total variation distance implies that
$$
\widehat{d}(n-1) \geq |\widehat{P}^{n-1}(n, 1) - \pi(1)| = \frac{1}{4}.
$$
We conclude that for the reverse winning streak chain, we have
$$
\widehat{t_{\mathrm{mix}}}(\varepsilon) = n
$$
for any positive $\varepsilon < 1/4$.

Essentially the same chain (the *greasy ladder*) is discussed in Example 24.20.

### PDF page 85 (book page 69)

**5.3.6. Distance between $P^t(x, \cdot)$ and $P^{t+1}(x, \cdot)$.**

PROPOSITION 5.7. *Let $Q$ be an irreducible transition matrix and consider the lazy chain with transition matrix $P = (Q + I)/2$. The distributions at time $t$ and $t + 1$ satisfy*

$$\left\|P^t(x, \cdot) - P^{t+1}(x, \cdot)\right\|_{\mathrm{TV}} \leq \frac{1}{\sqrt{t}}. \tag{5.15}$$

PROOF. Let $(N_t, M_t)$ be a coupling of the Binomial$(t, \frac{1}{2})$ distribution with the Binomial$(t + 1, \frac{1}{2})$ distribution, and let $(Z_t)$ be a Markov chain with transition matrix $Q$ started from $x$ and independent of $(N_t, M_t)$. The pair $(Z_{N_t}, Z_{M_t})$ is a coupling of the law $P^t(x, \cdot)$ with $P^{t+1}(x, \cdot)$, and

$$\left\|P^t(x, \cdot) - P^{t+1}(x, \cdot)\right\|_{\mathrm{TV}} \leq \mathbf{P}\{Z_{N_t} \neq Z_{M_t}\} \leq \mathbf{P}\{N_t \neq M_t\}. \tag{5.16}$$

Taking an infimum over all couplings $(N_t, M_t)$,

$$\left\|P^t(x, \cdot) - P^{t+1}(x, \cdot)\right\|_{\mathrm{TV}} \leq \|\mathrm{Bin}(t, 1/2) - \mathrm{Bin}(t + 1, 1/2)\|_{\mathrm{TV}} .$$

From (4.5), the right-hand side equals

$$2^{-t-1} \sum_{k \leq t/2} \left[ 2\binom{t}{k} - \binom{t+1}{k} \right]$$
$$= 2^{-t-1} \sum_{k \leq t/2} \left[ \binom{t}{k} - \binom{t}{k-1} \right] = 2^{-t-1} \binom{t}{\lfloor t/2 \rfloor} .$$

Applying Stirling's Formula as in the proof of Lemma 2.22 bounds the above by $\sqrt{\frac{2}{\pi t}}$.
$\blacksquare$

**5.4. Grand Couplings**

It can be useful to construct simultaneously, using a common source of randomness, Markov chains started from each state in $\mathcal{X}$. That is, we want to construct a collection of random variables $\{X_t^x : x \in \mathcal{X}, t = 0, 1, 2, \ldots\}$ such that for each $x \in \mathcal{X}$, the sequence $(X_t^x)_{t=0}^\infty$ is a Markov chain with transition matrix $P$ started from $x$. We call such a collection a ***grand coupling***.

The random mapping representation of a chain, discussed in Section 1.2, can be used to construct a grand coupling. Let $f : \mathcal{X} \times \Lambda \to \mathcal{X}$ be a function and $Z$ a $\Lambda$-valued random variable such that $P(x, y) = \mathbf{P}\{f(x, Z) = y\}$. Proposition 1.5 guarantees that such an $(f, Z)$ pair exists. Let $Z_1, Z_2, \ldots$ be an i.i.d. sequence, each with the same distribution as $Z$, and define

$$X_0^x = x, \quad X_t^x = f(X_{t-1}^x, Z_t) \text{ for } t \geq 1. \tag{5.17}$$

Since each of $(X_t^x)_{t=0}^\infty$ is a Markov chain started from $x$ with transition matrix $P$, this yields a grand coupling. We emphasize that the chains $(X_t^x)_{t=0}^\infty$ all live on the same probability space, each being determined by the same sequence of random variables $(Z_t)_{t=1}^\infty$.

### PDF page 86 (book page 70)

**5.4.1. Random colorings.** Random proper colorings of a graph were introduced in Section 3.3.1. For a graph $G$ with vertex set $V$, let $\mathcal{X}$ be the set of proper colorings of $G$, and let $\pi$ be the uniform distribution on $\mathcal{X}$. In Example 3.5, the Metropolis chain for $\pi$ was introduced. A transition for this chain is made by first selecting a vertex $v$ uniformly from $V$ and then selecting a color $k$ uniformly from $\{1, 2, \ldots, q\}$. If placing color $k$ at vertex $v$ is permissible (that is, if no neighbor of $v$ has color $k$), then vertex $v$ is assigned color $k$. Otherwise, no transition is made.

Note that in fact this transition rule can be defined on the space $\tilde{\mathcal{X}}$ of all (not necessarily proper) colorings, and the grand coupling can be defined simultaneously for all colorings in $\tilde{\mathcal{X}}$.

Using grand couplings, we can prove the following theorem:

THEOREM 5.8. *Let $G$ be a graph with $n$ vertices and maximal degree $\Delta$. For the Metropolis chain on proper colorings of $G$, if $q > 3\Delta$ and $c_{\mathrm{met}}(\Delta, q) := 1 - (3\Delta/q)$, then*

$$t_{\mathrm{mix}}(\varepsilon) \leq \lceil c_{\mathrm{met}}(\Delta, q)^{-1} n \log n + \log(1/\varepsilon) \rceil. \tag{5.18}$$

In Chapter 14 we show that for Glauber dynamics on proper colorings (see Section 3.3 for the definition of this chain), if $q > 2\Delta$, then the mixing time is of order $n \log n$.

PROOF. Just as for a single Metropolis chain on colorings, the grand coupling at each move generates a single vertex and color pair $(v, k)$, uniformly at random from $V \times \{1, \ldots, q\}$ and independently of the past. For each $x \in \tilde{\mathcal{X}}$, the coloring $X_t^x$ is updated by attempting to re-color vertex $v$ with color $k$, accepting the update if and only if the proposed new color is different from the colors at vertices neighboring $v$. (If a re-coloring is not accepted, the chain $X_t^x$ remains in its current state.) The essential point is that the same vertex and color are used for all the chains $(X_t^x)$.

For two colorings $x, y \in \tilde{\mathcal{X}}$, define

$$\rho(x, y) := \sum_{v \in V} \mathbf{1}_{\{x(v) \neq y(v)\}}$$

to be the number of vertices where $x$ and $y$ disagree, and note that $\rho$ is a metric on $\tilde{\mathcal{X}}$.

Suppose $\rho(x, y) = 1$, so that $x$ and $y$ agree everywhere except at vertex $v_0$. Write $\mathcal{N}$ for the set of colors appearing among the neighbors of $v_0$ in $x$, which is the same as the set of colors appearing among the neighbors of $v_0$ in $y$. Recall that $v$ represents a random sample from $V$, and $k$ a random sample from $\{1, 2, \ldots, q\}$, independent of $v$. We consider the distance after updating $x$ and $y$ in one step of the grand coupling, that is, $\rho(X_1^x, X_1^y)$.

This distance is zero if and only if the vertex $v_0$ is selected for updating and the color proposed is not in $\mathcal{N}$. This occurs with probability

$$\mathbf{P}\{\rho(X_1^x, X_1^y) = 0\} = \left(\frac{1}{n}\right) \left(\frac{q - |\mathcal{N}|}{q}\right) \geq \frac{q - \Delta}{nq}, \tag{5.19}$$

where $\Delta$ denotes the maximum vertex degree in the graph.

Suppose now a vertex $w$ which is a neighbor of $v_0$ is selected for updating.

*Case 1.* The proposed color is $x(v_0)$ or $y(v_0)$. In this case, the number of disagreements may possibly increase by at most one.

*Case 2.* Neither the color $x(v_0)$ or $y(v_0)$ is proposed. In this case, the new color will be accepted in $x$ if and only if it accepted in $y$.

### PDF page 87 (book page 71)

**FIGURE 5.8.** Two colorings which disagree only at $v_0$. The one on the left can be updated with the color 5 at a neighbor of $w$ of $v_0$, while the one on the right cannot be updated with a 5 at $w$. If vertex $w$ is selected for updating and color 5 is proposed, the two configurations will disagree at both $v_0$ and $w$. *[Figure: Two side-by-side diagrams. Each shows a central vertex labeled 6 (marked $w$) connected by four edges to surrounding vertices; edges continue as dashed lines beyond. Left diagram: top vertex 1, right vertex 2 (marked $v_0$), left vertex 3, bottom vertex 4, with a curved arrow pointing to the region and the label "5 permitted". Right diagram: top vertex 1, right vertex 5 (marked $v_0$), left vertex 3, bottom vertex 4, with a curved arrow and the label "5 not permitted".]*

Thus, the only way a new disagreement can possibly be introduced is if a neighbor of $v_0$ is selected for updating, and either $x(v_0)$ or $y(v_0)$ is proposed.

We conclude that

$$\mathbf{P}\{\rho(X_1^x, X_1^y) = 2\} \leq \left(\frac{\Delta}{n}\right) \left(\frac{2}{q}\right). \tag{5.20}$$

Using the bounds (5.19) and (5.20),

$$\mathbf{E}\left(\rho(X_1^x, X_1^y) - 1\right) \leq \frac{2\Delta}{nq} - \frac{(q - \Delta)}{nq} = \frac{3\Delta - q}{nq},$$

and so

$$\mathbf{E}\left(\rho(X_1^x, X_1^y)\right) \leq 1 - \frac{q - 3\Delta}{nq}.$$

If $q > 3\Delta$, then $c_{\mathrm{met}}(\Delta, q) = 1 - (3\Delta/q) > 0$ and

$$\mathbf{E}\left(\rho(X_1^x, X_1^y)\right) \leq 1 - \frac{c_{\mathrm{met}}(\Delta, q)}{n} < 1. \tag{5.21}$$

Now, suppose that $x$ and $y$ are colorings with $\rho(x, y) = r$. There are colorings $x_0 = x, x_1, \ldots, x_r = y$ such that $\rho(x_k, x_{k-1}) = 1$. Since $\rho$ is a metric and the inequality (5.21) can be applied to each of $\mathbf{E}\left(\rho(X_1^{x_k}, X_1^{x_{k-1}})\right)$,

$$\mathbf{E}\left(\rho(X_1^x, X_1^y)\right) \leq \sum_{k=1}^r \mathbf{E}\left(\rho(X_1^{x_k}, X_1^{x_{k-1}})\right)$$
$$\leq r \left(1 - \frac{c_{\mathrm{met}}(\Delta, q)}{n}\right) = \rho(x, y) \left(1 - \frac{c_{\mathrm{met}}(\Delta, q)}{n}\right).$$

### PDF page 88 (book page 72)

Conditional on the event that $X_{t-1}^x = x_{t-1}$ and $X_{t-1}^y = y_{t-1}$, the random vector $(X_t^x, X_t^y)$ has the same distribution as $(X_1^{x_{t-1}}, X_1^{y_{t-1}})$. Hence,

$$ \mathbf{E}\left(\rho(X_t^x, X_t^y) \mid X_{t-1}^x = x_{t-1},\, X_{t-1}^y = y_{t-1}\right) = \mathbf{E}\left(\rho(X_1^{x_{t-1}}, X_1^{y_{t-1}})\right) $$
$$ \leq \rho(x_{t-1}, y_{t-1})\left(1 - \frac{c_{\mathrm{met}}(\Delta, q)}{n}\right). $$

Taking an expectation over $(X_{t-1}^x, X_{t-1}^y)$ shows that

$$ \mathbf{E}\left(\rho(X_t^x, X_t^y)\right) \leq \mathbf{E}\left(\rho(X_{t-1}^x, X_{t-1}^y)\right)\left(1 - \frac{c_{\mathrm{met}}(\Delta, q)}{n}\right). $$

Iterating the above inequality shows that

$$ \mathbf{E}\left(\rho(X_t^x, X_t^y)\right) \leq \rho(x, y)\left(1 - \frac{c_{\mathrm{met}}(\Delta, q)}{n}\right)^t. $$

Moreover, by Markov's inequality, since $\rho(x, y) \geq 1$ when $x \neq y$,

$$ \mathbf{P}\{X_t^x \neq X_t^y\} = \mathbf{P}\{\rho(X_t^x, X_t^y) \geq 1\} $$
$$ \leq \rho(x, y)\left(1 - \frac{c_{\mathrm{met}}(\Delta, q)}{n}\right)^t \leq n e^{-t(c_{\mathrm{met}}(\Delta, q)/n)}. $$

Since the above holds for all colorings $x, y \in \tilde{\mathcal{X}}$, in particular it holds for all proper colorings $x, y \in \mathcal{X}$. By Corollary 5.5 and the above inequality, $d(t) \leq n e^{-t(c_{\mathrm{met}}(\Delta, q)/n)}$, whence if

$$ t \geq c_{\mathrm{met}}(\Delta, q)^{-1} n \left[\log n + \log(1/\varepsilon)\right], $$

then $d(t) \leq \varepsilon$. This establishes (5.18). $\blacksquare$

**5.4.2. Hardcore model.** The hardcore model with fugacity $\lambda$ was introduced in Section 3.3.4. We use a grand coupling to show that if $\lambda$ is small enough, the Glauber dynamics has a mixing time of the order $n \log n$.

THEOREM 5.9. *Let $c_H(\lambda) := [1 + \lambda(1 - \Delta)]/(1 + \lambda)$. For the Glauber dynamics for the hardcore model on a graph with maximum degree $\Delta$ and $n$ vertices, if $\lambda < (\Delta - 1)^{-1}$, then*

$$ t_{\mathrm{mix}}(\varepsilon) \leq \frac{n}{c_H(\lambda)}[\log n + \log(1/\varepsilon)]. $$

PROOF. We again use the grand coupling which is run as follows: a vertex $v$ is selected uniformly at random, and a coin with probability $\lambda/(1 + \lambda)$ of heads is tossed, independently of the choice of $v$. Each hardcore configuration $x$ is updated using $v$ and the result of the coin toss. If the coin lands tails, any particle present at $v$ in $x$ is removed. If the coin lands heads and all neighbors of $v$ are unoccupied in the configuration $x$, then a particle is placed at $v$.

We let $\rho(x, y) = \sum_{v \in V} \mathbf{1}_{\{x(v) \neq y(v)\}}$ be the number of sites where $x$ and $y$ disagree. Suppose that $x$ and $y$ satisfy $\rho(x, y) = 1$, so that the two configurations differ only at $v_0$. Without loss of generality, assume that $x(v_0) = 1$ and $y(v_0) = 0$.

If vertex $v_0$ is selected, then $\rho(X_1^x, X_1^y) = 0$, since the neighbors of $v_0$ agree in both $x$ and $y$ so the same action will be taken for the two configurations.

Let $w$ be a neighbor of $v_0$. If none of the neighbors of $w$ different from $v_0$ are occupied (these sites have the same status in $x$ and $y$) and the coin toss is heads, then $x$ and $y$ will be updated differently. Indeed, it will be possible to place a

### PDF page 89 (book page 73)

particle at $w$ in $y$, but not in $x$. This is the only case in which a new disagreement between $x$ and $y$ can be introduced.

Therefore,

$$ \mathbf{E}\left(\rho(X_1^x, X_1^y)\right) \leq 1 - \frac{1}{n} + \frac{\Delta}{n}\frac{\lambda}{1 + \lambda} = 1 - \frac{1}{n}\left[\frac{1 - \lambda(\Delta - 1)}{1 + \lambda}\right]. $$

If $\lambda < (\Delta - 1)^{-1}$, then $c_H(\lambda) > 0$ and

$$ \mathbf{E}\left(\rho(X_1^x, X_1^y)\right) \leq 1 - \frac{c_H(\lambda)}{n} \leq e^{-c_H(\lambda)/n}. $$

The remainder of the theorem follows exactly the same argument as is used at the end of Theorem 5.8. $\blacksquare$

### Exercises

EXERCISE 5.1. A mild generalization of Theorem 5.4 can be used to give an alternative proof of the Convergence Theorem.

(a) Show that when $(X_t, Y_t)$ is a coupling satisfying (5.2) for which $X_0 \sim \mu$ and $Y_0 \sim \nu$, then

$$ \left\|\mu P^t - \nu P^t\right\|_{\mathrm{TV}} \leq \mathbf{P}\{\tau_{\mathrm{couple}} > t\}. \tag{5.22} $$

(b) If in (a) we take $\nu = \pi$, where $\pi$ is the stationary distribution, then (by definition) $\pi P^t = \pi$, and (5.22) bounds the difference between $\mu P^t$ and $\pi$. The only thing left to check is that there exists a coupling guaranteed to coalesce, that is, for which $\mathbf{P}\{\tau_{\mathrm{couple}} < \infty\} = 1$. Show that if the chains $(X_t)$ and $(Y_t)$ are taken to be independent of one another, then they are assured to eventually meet.

EXERCISE 5.2. Let $(X_t, Y_t)$ be a Markovian coupling such that for some $0 < \alpha < 1$ and some $t_0 > 0$, the coupling time $\tau_{\mathrm{couple}} = \min\{t \geq 0 : X_t = Y_t\}$ satisfies $\mathbf{P}\{\tau_{\mathrm{couple}} \leq t_0\} \geq \alpha$ for *all* pairs of initial states $(x, y)$. Prove that

$$ \mathbf{E}(\tau_{\mathrm{couple}}) \leq \frac{t_0}{\alpha}. $$

EXERCISE 5.3. Show that if $X_1, X_2, \ldots$ are independent and each have mean $\mu$ and if $\tau$ is a $\mathbb{Z}^+$-valued random variable independent of all the $X_i$'s and with $\mathbf{E}(\tau) < \infty$, then

$$ \mathbf{E}\left(\sum_{i=1}^{\tau} X_i\right) = \mu \mathbf{E}(\tau). $$

EXERCISE 5.4. We can get a better bound on the mixing time for the lazy walker on the $d$-dimensional torus by sharpening the analysis of the "coordinate-by-coordinate" coupling given in the proof of Theorem 5.6.

Let $t \geq k d n^2$.

(a) Show that the probability that the first coordinates of the two walks have not yet coupled by time $t$ is less than $(1/4)^k$.

(b) By making an appropriate choice of $k$ and considering all the coordinates, obtain the bound on $t_{\mathrm{mix}}(\varepsilon)$ in Theorem 5.6.

EXERCISE 5.5. Extend the calculation in Section 5.3.4 to obtain an upper bound on the mixing time on the finite $b$-ary tree.

### PDF page 90 (book page 74)

### Notes

The use of coupling in probability is usually traced back to **Doeblin (1938)**. Couplings of Markov chains were first studied in **Pitman (1974)** and Griffeath (**1974/75**). See also **Pitman (1976)**. See **Luby, Randall, and Sinclair (1995)** and **Luby, Randall, and Sinclair (2001)** for interesting examples of couplings.

For Glauber dynamics on colorings, it is shown in Chapter 14 that if the number of colors $q$ satisfies $q > 2\Delta$, then the mixing time is $O(n \log n)$.

The same chain as in Theorem 5.9 was considered by **Luby and Vigoda (1999)**, **Luby and Vigoda (1995)**, and **Vigoda (2001)**. The last reference proves that $t_{\mathrm{mix}} = O(n \log n)$ provided $\lambda < 2/(\Delta - 2)$.

For an example of a coupling which is not Markovian, see **Hayes and Vigoda (2003)**.

**Further reading.** For more on coupling and its applications in probability, see **Lindvall (2002)** and **Thorisson (2000)**.

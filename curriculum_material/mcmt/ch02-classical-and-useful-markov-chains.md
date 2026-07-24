# Chapter 2 — Classical (and Useful) Markov Chains
*(PDF pages 37–53; book pages 21–37)*

### PDF page 37 (book page 21)

CHAPTER 2

# Chapter 2 — Classical (and Useful) Markov Chains

Here we present several basic and important examples of Markov chains. The results we prove in this chapter will be used in many places throughout the book.

This is also the only chapter in the book where the central chains are not always irreducible. Indeed, two of our examples, gambler's ruin and coupon collecting, both have absorbing states. For each we examine closely how long it takes to be absorbed.

**2.1. Gambler's Ruin**

Consider a gambler betting on the outcome of a sequence of independent fair coin tosses. If the coin comes up heads, she adds one dollar to her purse; if the coin lands tails up, she loses one dollar. If she ever reaches a fortune of $n$ dollars, she will stop playing. If her purse is ever empty, then she must stop betting.

The gambler's situation can be modeled by a random walk on a path with vertices $\{0, 1, \ldots, n\}$. At all interior vertices, the walk is equally likely to go up by 1 or down by 1. That states 0 and $n$ are absorbing, meaning that once the walk arrives at either 0 or $n$, it stays forever (cf. Section 1.7).

There are two questions that immediately come to mind: how long will it take for the gambler to arrive at one of the two possible fates? What are the probabilities of the two possibilities?

PROPOSITION 2.1. *Assume that a gambler making fair unit bets on coin flips will abandon the game when her fortune falls to 0 or rises to $n$. Let $X_t$ be gambler's fortune at time $t$ and let $\tau$ be the time required to be absorbed at one of 0 or $n$. Assume that $X_0 = k$, where $0 \le k \le n$. Then*

$$\mathbf{P}_k\{X_\tau = n\} = k/n \tag{2.1}$$

$$\mathbf{E}_k(\tau) = k(n - k). \tag{2.2}$$

PROOF. Let $p_k$ be the probability that the gambler reaches a fortune of $n$ before ruin, given that she starts with $k$ dollars. We solve simultaneously for $p_0, p_1, \ldots, p_n$. Clearly $p_0 = 0$ and $p_n = 1$, while

$$p_k = \frac{1}{2} p_{k-1} + \frac{1}{2} p_{k+1} \quad \text{for } 1 \le k \le n - 1. \tag{2.3}$$

To obtain (2.3), first observe that with probability $1/2$, the walk moves to $k + 1$. The conditional probability of reaching $n$ before 0, starting from $k + 1$, is exactly $p_{k+1}$. Similarly, with probability $1/2$ the walk moves to $k - 1$, and the conditional probability of reaching $n$ before 0 from state $k - 1$ is $p_{k-1}$.

Solving the system (2.3) of linear equations yields $p_k = k/n$ for $0 \le k \le n$.

For (2.2), again we try to solve for all the values at once. To this end, write $f_k$ for the expected time $\mathbf{E}_k(\tau)$ to be absorbed, starting at position $k$. Clearly,

### PDF page 38 (book page 22)

**FIGURE 2.1.** How long until the walk reaches either 0 or $n$? What is the probability of each? *[Figure: a horizontal path with four filled vertices labeled 0, 1, 2, and n from left to right; a solid line connects 0–1–2, and a dashed line connects 2 to n. A small stick figure stands above vertex 1.]*

$f_0 = f_n = 0$; the walk is started at one of the absorbing states. For $1 \le k \le n - 1$, it is true that

$$f_k = \frac{1}{2} \left(1 + f_{k+1}\right) + \frac{1}{2} \left(1 + f_{k-1}\right). \tag{2.4}$$

Why? When the first step of the walk increases the gambler's fortune, then the conditional expectation of $\tau$ is 1 (for the initial step) plus the expected additional time needed. The expected additional time needed is $f_{k+1}$, because the walk is now at position $k + 1$. Parallel reasoning applies when the gambler's fortune first decreases.

Exercise 2.1 asks the reader to solve this system of equations, completing the proof of (2.2). $\blacksquare$

REMARK 2.2. See Chapter 9 for powerful generalizations of the simple methods we have just applied.

**2.2. Coupon Collecting**

A company issues $n$ different types of coupons. A collector desires a complete set. We suppose each coupon he acquires is equally likely to be each of the $n$ types. How many coupons must he obtain so that his collection contains all $n$ types?

It may not be obvious why this is a Markov chain. Let $X_t$ denote the number of different types represented among the collector's first $t$ coupons. Clearly $X_0 = 0$. When the collector has coupons of $k$ different types, there are $n - k$ types missing. Of the $n$ possibilities for his next coupon, only $n - k$ will expand his collection. Hence

$$\mathbf{P}\{X_{t+1} = k + 1 \mid X_t = k\} = \frac{n - k}{n}$$

and

$$\mathbf{P}\{X_{t+1} = k \mid X_t = k\} = \frac{k}{n}.$$

Every trajectory of this chain is non-decreasing. Once the chain arrives at state $n$ (corresponding to a complete collection), it is absorbed there. We are interested in the number of steps required to reach the absorbing state.

PROPOSITION 2.3. *Consider a collector attempting to collect a complete set of coupons. Assume that each new coupon is chosen uniformly and independently from the set of $n$ possible types, and let $\tau$ be the (random) number of coupons collected when the set first contains every type. Then*

$$\mathbf{E}(\tau) = n \sum_{k=1}^{n} \frac{1}{k}.$$

### PDF page 39 (book page 23)

PROOF. The expectation $\mathbf{E}(\tau)$ can be computed by writing $\tau$ as a sum of geometric random variables. Let $\tau_k$ be the total number of coupons accumulated when the collection first contains $k$ distinct coupons. Then

$$\tau = \tau_n = \tau_1 + (\tau_2 - \tau_1) + \cdots + (\tau_n - \tau_{n-1}). \tag{2.5}$$

Furthermore, $\tau_k - \tau_{k-1}$ is a geometric random variable with success probability $(n-k+1)/n$: after collecting $\tau_{k-1}$ coupons, there are $n-k+1$ types missing from the collection. Each subsequent coupon drawn has the same probability $(n - k + 1)/n$ of being a type not already collected, until a new type is finally drawn. Thus $\mathbf{E}(\tau_k - \tau_{k-1}) = n/(n - k + 1)$ and

$$\mathbf{E}(\tau) = \sum_{k=1}^{n} \mathbf{E}(\tau_k - \tau_{k-1}) = n \sum_{k=1}^{n} \frac{1}{n - k + 1} = n \sum_{k=1}^{n} \frac{1}{k}. \tag{2.6}$$

$\blacksquare$

While the argument for Proposition 2.3 is simple and vivid, we will often need to know more about the distribution of $\tau$ in future applications. Recall that $|\sum_{k=1}^{n} 1/k - \log n| \le 1$, whence $|\mathbf{E}(\tau) - n \log n| \le n$ (see Exercise 2.4 for a better estimate). Proposition 2.4 says that $\tau$ is unlikely to be much larger than its expected value.

PROPOSITION 2.4. *Let $\tau$ be a coupon collector random variable, as in Proposition 2.3. For any $c > 0$,*

$$\mathbf{P}\{\tau > \lceil n \log n + cn \rceil\} \le e^{-c}. \tag{2.7}$$

NOTATION. Throughout the text, we use log to denote the natural logarithm.

PROOF. Let $A_i$ be the event that the $i$-th type does not appear among the first $\lceil n \log n + cn \rceil$ coupons drawn. Observe first that

$$\mathbf{P}\{\tau > \lceil n \log n + cn \rceil\} = \mathbf{P}\left(\bigcup_{i=1}^{n} A_i\right) \le \sum_{i=1}^{n} \mathbf{P}(A_i).$$

Since each trial has probability $1 - n^{-1}$ of *not* drawing coupon $i$ and the trials are independent, the right-hand side above is equal to

$$\sum_{i=1}^{n} \left(1 - \frac{1}{n}\right)^{\lceil n \log n + cn \rceil} \le n \exp\left(-\frac{n \log n + cn}{n}\right) = e^{-c},$$

proving (2.7). $\blacksquare$

**2.3. The Hypercube and the Ehrenfest Urn Model**

The $n$-***dimensional hypercube*** is a graph whose vertices are the binary $n$-tuples $\{0, 1\}^n$. Two vertices are connected by an edge when they differ in exactly one coordinate. See Figure 2.2 for an illustration of the three-dimensional hypercube.

The simple random walk on the hypercube moves from a vertex $(x^1, x^2, \ldots, x^n)$ by choosing a coordinate $j \in \{1, 2, \ldots, n\}$ uniformly at random and setting the new state equal to $(x^1, \ldots, x^{j-1}, 1 - x^j, x^{j+1}, \ldots, x^n)$. That is, the bit at the walk's chosen coordinate is flipped. (This is a special case of the walk defined in Section 1.4.)

### PDF page 40 (book page 24)

**FIGURE 2.2.** The three-dimensional hypercube. *[Figure: a three-dimensional cube (the hypercube graph on $\{0,1\}^3$), with the eight vertices labeled by bitstrings. Front face lower-left to upper-left-back etc.: vertices labeled 011, 111 (top), 001, 101 (upper middle), 010, 110 (lower middle), 000, 100 (bottom). Edges connect bitstrings differing in a single coordinate.]*

Unfortunately, the simple random walk on the hypercube is periodic, since every move flips the parity of the number of 1's. The **lazy random walk**, which does not have this problem, remains at its current position with probability $1/2$ and moves as above with probability $1/2$. This chain can be realized by choosing a coordinate uniformly at random and *refreshing* the bit at this coordinate by replacing it with an unbiased random bit independent of time, current state, and coordinate chosen.

Since the hypercube is an $n$-regular graph, Example 1.12 implies that the stationary distribution of both the simple and lazy random walks is uniform on $\{0,1\}^n$.

We now consider a process, the **Ehrenfest urn**, which at first glance appears quite different. Suppose $n$ balls are distributed among two urns, I and II. At each move, a ball is selected uniformly at random and transferred from its current urn to the other urn. If $X_t$ is the number of balls in urn I at time $t$, then the transition matrix for $(X_t)$ is

$$ P(j,k) = \begin{cases} \frac{n-j}{n} & \text{if } k = j+1, \\ \frac{j}{n} & \text{if } k = j-1, \\ 0 & \text{otherwise.} \end{cases} \tag{2.8} $$

Thus $(X_t)$ is a Markov chain with state space $\mathcal{X} = \{0,1,2,\ldots,n\}$ that moves by $\pm 1$ on each move and is biased towards the middle of the interval. The stationary distribution for this chain is binomial with parameters $n$ and $1/2$ (see Exercise 2.5).

The Ehrenfest urn is a projection (in a sense that will be defined precisely in Section 2.3.1) of the random walk on the $n$-dimensional hypercube. This is unsurprising given the standard bijection between $\{0,1\}^n$ and subsets of $\{1,\ldots,n\}$, under which a set corresponds to the vector with 1's in the positions of its elements. We can view the position of the random walk on the hypercube as specifying the set of balls in Ehrenfest urn I; then changing a bit corresponds to moving a ball into or out of the urn.

Define the **Hamming weight** $W(\boldsymbol{x})$ of a vector $\boldsymbol{x} := (x^1,\ldots,x^n) \in \{0,1\}^n$ to be its number of coordinates with value 1:

$$ W(\boldsymbol{x}) = \sum_{j=1}^{n} x^j. \tag{2.9} $$

Let $(\boldsymbol{X}_t)$ be the simple random walk on the $n$-dimensional hypercube, and let $W_t = W(\boldsymbol{X}_t)$ be the Hamming weight of the walk's position at time $t$.

When $W_t = j$, the weight increments by a unit amount when one of the $n-j$ coordinates with value 0 is selected. Likewise, when one of the $j$ coordinates with

### PDF page 41 (book page 25)

value 1 is selected, the weight decrements by one unit. From this description, it is clear that $(W_t)$ is a Markov chain with transition probabilities given by (2.8).

**2.3.1. Projections of chains.** The Ehrenfest urn is a *projection*, which we define in this section, of the simple random walk on the hypercube.

Assume that we are given a Markov chain $(X_0, X_1, \ldots)$ with state space $\mathcal{X}$ and transition matrix $P$ and also some equivalence relation that partitions $\mathcal{X}$ into equivalence classes. We denote the equivalence class of $x \in \mathcal{X}$ by $[x]$. (For the Ehrenfest example, two bitstrings are equivalent when they contain the same number of 1's.)

Under what circumstances will $([X_0], [X_1], \ldots)$ also be a Markov chain? For this to happen, knowledge of what equivalence class we are in at time $t$ must suffice to determine the distribution over equivalence classes at time $t+1$. If the probability $P(x, [y])$ is always the same as $P(x', [y])$ when $x$ and $x'$ are in the same equivalence class, that is clearly enough. We summarize this in the following lemma.

LEMMA 2.5. *Let $\mathcal{X}$ be the state space of a Markov chain $(X_t)$ with transition matrix $P$. Let $\sim$ be an equivalence relation on $\mathcal{X}$ with equivalence classes $\mathcal{X}^\sharp = \{[x] : x \in \mathcal{X}\}$, and assume that $P$ satisfies*

$$ P(x, [y]) = P(x', [y]) \tag{2.10} $$

*whenever $x \sim x'$. Then $([X_t])$ is a Markov chain with state space $\mathcal{X}^\sharp$ and transition matrix $P^\sharp$ defined by $P^\sharp([x], [y]) := P(x, [y])$.*

The process of constructing a new chain by taking equivalence classes for an equivalence relation compatible with the transition matrix (in the sense of (2.10)) is called **projection**, or sometimes **lumping**.

**2.4. The Pólya Urn Model**

Consider the following process, known as **Pólya's urn**. Start with an urn containing two balls, one black and one white. From this point on, proceed by choosing a ball at random from those already in the urn; return the chosen ball to the urn and add another ball of the same color. If there are $j$ black balls in the urn after $k$ balls have been added (so that there are $k+2$ balls total in the urn), then the probability that another black ball is added is $j/(k+2)$. The sequence of ordered pairs listing the numbers of black and white balls is a Markov chain with state space $\{1, 2, \ldots\}^2$.

LEMMA 2.6. *Let $B_k$ be the number of black balls in Pólya's urn after the addition of $k$ balls. The distribution of $B_k$ is uniform on $\{1, 2, \ldots, k+1\}$.*

PROOF. We prove this by induction on $k$. For $k = 1$, this is obvious. Suppose that $B_{k-1}$ is uniform on $\{1, 2, \ldots, k\}$. Then for every $j = 1, 2, \ldots, k+1$,

$$ \begin{aligned} \mathbf{P}\{B_k = j\} &= \left(\frac{j-1}{k+1}\right) \mathbf{P}\{B_{k-1} = j-1\} + \left(\frac{k+1-j}{k+1}\right) \mathbf{P}\{B_{k-1} = j\} \\ &= \left(\frac{j-1}{k+1}\right)\frac{1}{k} + \left(\frac{k+1-j}{k+1}\right)\frac{1}{k} = \frac{1}{k+1}\,. \end{aligned} $$

$\blacksquare$

We will have need for the $d$**-color Pólya urn**, the following generalization: Initially, for each $i = 1, \ldots, d$, the urn contains a single ball of color $i$ (for a total of $d$ balls). At each step, a ball is drawn uniformly at random and replaced along

### PDF page 42 (book page 26)

with an additional ball of the same color. We let $N_t^i$ be the number of balls of color $i$ at time $t$, and write $\boldsymbol{N}_t$ for the vector $(N_t^1, \ldots, N_t^d)$. We will need the following lemma.

LEMMA 2.7. *Let $\{\boldsymbol{N}_t\}_{t \geq 0}$ be the $d$-dimensional Pólya urn process. The vector $\boldsymbol{N}_t$ is uniformly distributed over*

$$ V_t = \left\{ (x_1, \ldots, x_d) : x_i \in \mathbb{Z},\, x_i \geq 1 \text{ for all } i = 1, \ldots, d, \quad \text{and} \quad \sum_{i=1}^{d} x_i = t + d \right\}. $$

*In particular, since $|V_t| = \binom{t+d-1}{d-1}$,*

$$ \mathbf{P}\{\boldsymbol{N}_t = \boldsymbol{v}\} = \frac{1}{\binom{t+d-1}{d-1}} \quad \text{for all } \boldsymbol{v} \in V_t\,. $$

The proof is similar to the proof of Lemma 2.6; Exercise 2.11 asks for a verification.

**2.5. Birth-and-Death Chains**

A **birth-and-death chain** has state space $\mathcal{X} = \{0, 1, 2, \ldots, n\}$. In one step the state can increase or decrease by at most 1. The current state can be thought of as the size of some population; in a single step of the chain there can be at most one birth or death. The transition probabilities can be specified by $\{(p_k, r_k, q_k)\}_{k=0}^{n}$, where $p_k + r_k + q_k = 1$ for each $k$ and

- $p_k$ is the probability of moving from $k$ to $k+1$ when $0 \leq k < n$,
- $q_k$ is the probability of moving from $k$ to $k-1$ when $0 < k \leq n$,
- $r_k$ is the probability of remaining at $k$ when $0 \leq k \leq n$,
- $q_0 = p_n = 0$.

PROPOSITION 2.8. *Every birth-and-death chain is reversible.*

PROOF. A function $w$ on $\mathcal{X}$ satisfies the detailed balance equations (1.29) if and only if

$$ p_{k-1} w_{k-1} = q_k w_k $$

for $1 \leq k \leq n$. For our birth-and-death chain, a solution is given by $w_0 = 1$ and

$$ w_k = \prod_{i=1}^{k} \frac{p_{i-1}}{q_i} $$

for $1 \leq k \leq n$. Normalizing so that the sum is unity yields

$$ \pi_k = \frac{w_k}{\sum_{j=0}^{n} w_j} $$

for $0 \leq k \leq n$. (By Proposition 1.20, $\pi$ is also a stationary distribution.) $\blacksquare$

Now, fix $\ell \in \{0, 1, \ldots, n\}$. Consider restricting the original chain to $\{0, 1, \ldots, \ell\}$:

- For any $k \in \{0, 1, \ldots, \ell-1\}$, the chain makes transitions from $k$ as before, moving down with probability $q_k$, remaining in place with probability $r_k$, and moving up with probability $p_k$.
- At $\ell$, the chain either moves down or remains in place, with probabilities $q_\ell$ and $r_\ell + p_\ell$, respectively.

### PDF page 43 (book page 27)

We write $\tilde{\mathbf{E}}$ for expectations for this new chain. By the proof of Proposition 2.8, the stationary probability $\tilde{\pi}$ of the truncated chain is given by

$$ \tilde{\pi}(k) = \frac{w_k}{\sum_{j=0}^{\ell} w_j} $$

for $0 \leq k \leq \ell$. Since in the truncated chain the only possible moves from $\ell$ are to stay put or to step down to $\ell - 1$, the expected first return time $\tilde{\mathbf{E}}_\ell(\tau_\ell^+)$ satisfies

$$ \tilde{\mathbf{E}}_\ell(\tau_\ell^+) = (r_\ell + p_\ell) \cdot 1 + q_\ell \left( \tilde{\mathbf{E}}_{\ell-1}(\tau_\ell) + 1 \right) = 1 + q_\ell \tilde{\mathbf{E}}_{\ell-1}(\tau_\ell). \tag{2.11} $$

By Proposition 1.19,

$$ \tilde{\mathbf{E}}_\ell(\tau_\ell^+) = \frac{1}{\tilde{\pi}(\ell)} = \frac{1}{w_\ell} \sum_{j=0}^{\ell} w_j. \tag{2.12} $$

We have constructed the truncated chain so that $\tilde{\mathbf{E}}_{\ell-1}(\tau_\ell) = \mathbf{E}_{\ell-1}(\tau_\ell)$. Rearranging (2.11) and (2.12) gives

$$ \mathbf{E}_{\ell-1}(\tau_\ell) = \frac{1}{q_\ell} \left( \sum_{j=0}^{\ell} \frac{w_j}{w_\ell} - 1 \right) = \frac{1}{q_\ell w_\ell} \sum_{j=0}^{l-1} w_j. \tag{2.13} $$

To find $\mathbf{E}_a(\tau_b)$ for $a < b$, just sum:

$$ \mathbf{E}_a(\tau_b) = \sum_{\ell=a+1}^{b} \mathbf{E}_{\ell-1}(\tau_\ell). $$

Consider two important special cases. Suppose that

$$ (q_k, r_k, p_k) = (q, r, p) \text{ for } 1 \leq k < n, $$
$$ (q_0, r_0, p_0) = (0, r + q, p), \quad (q_n, r_n, p_n) = (q, r + p, 0) $$

for $p, r, q \geq 0$ with $p + r + q = 1$. First consider the case where $p \neq q$. We have $w_k = (p/q)^k$ for $0 \leq k \leq n$, and from (2.13), for $1 \leq \ell \leq n$,

$$ \mathbf{E}_{\ell-1}(\tau_\ell) = \frac{1}{q(p/q)^\ell} \sum_{j=0}^{\ell-1} (p/q)^j = \frac{(p/q)^\ell - 1}{q(p/q)^\ell[(p/q) - 1]} = \frac{1}{p - q} \left[ 1 - \left( \frac{q}{p} \right)^\ell \right]. $$

In particular,

$$ \mathbf{E}_0(\tau_n) = \frac{1}{p - q} \left[ n - q \left( \frac{1 - (q/p)^n}{p - q} \right) \right]. \tag{2.14} $$

If $p = q$, then $w_j = 1$ for all $j$ and

$$ \mathbf{E}_{\ell-1}(\tau_\ell) = \frac{\ell}{p}. $$

**2.6. Random Walks on Groups**

Several of the examples we have already examined and many others we will study in future chapters share important symmetry properties, which we make explicit here. Recall that a **group** is a set $G$ endowed with an associative operation $\cdot : G \times G \to G$ and an **identity** id $\in G$ such that for all $g \in G$,

(i) id $\cdot g = g$ and $g \cdot$ id $= g$.
(ii) there exists an **inverse** $g^{-1} \in G$ for which $g \cdot g^{-1} = g^{-1} \cdot g = $ id.

### PDF page 44 (book page 28)

Given a probability distribution $\mu$ on a group $(G, \cdot)$, we define the **left random walk on $G$ with increment distribution** $\mu$ as follows: it is a Markov chain with state space $G$ and which moves by multiplying the current state *on the left* by a random element of $G$ selected according to $\mu$. Equivalently, the transition matrix $P$ of this chain has entries

$$ P(g, hg) = \mu(h) $$

for all $g, h \in G$.

REMARK 2.9. We multiply the current state by the increment *on the left*. Alternatively, one can consider the **right random walk**, where $P(g, gh) = \mu(h)$.

EXAMPLE 2.10 (The $n$-cycle). Let $\mu$ assign probability $1/2$ to each of $1$ and $n-1 \equiv -1 \pmod{n}$ in the additive cyclic group $\mathbb{Z}_n = \{0, 1, \ldots, n-1\}$. The **simple random walk on the $n$-cycle** first introduced in Example 1.4 is the random walk on $\mathbb{Z}_n$ with increment distribution $\mu$. Similarly, let $\nu$ assign weight $1/4$ to both $1$ and $n-1$ and weight $1/2$ to $0$. Then **lazy random walk on the $n$-cycle**, discussed in Example 1.8, is the random walk on $\mathbb{Z}_n$ with increment distribution $\nu$.

EXAMPLE 2.11 (The hypercube). The hypercube random walks defined in Section 2.3 are random walks on the group $\mathbb{Z}_2^n$, which is the direct product of $n$ copies of the two-element group $\mathbb{Z}_2 = \{0, 1\}$. For the simple random walk the increment distribution is uniform on the set $\{\mathbf{e}_i : 1 \leq i \leq n\}$, where the vector $\mathbf{e}_i$ has a 1 in the $i$-th place and 0 in all other entries. For the lazy version, the increment distribution gives the vector $\mathbf{0}$ (with all zero entries) weight $1/2$ and each $\mathbf{e}_i$ weight $1/2n$.

PROPOSITION 2.12. *Let $P$ be the transition matrix of a random walk on a finite group $G$ and let $U$ be the uniform probability distribution on $G$. Then $U$ is a stationary distribution for $P$.*

PROOF. Let $\mu$ be the increment distribution of the random walk. For any $g \in G$,

$$ \sum_{h \in G} U(h)P(h, g) = \frac{1}{|G|} \sum_{k \in G} P(k^{-1}g, g) = \frac{1}{|G|} \sum_{k \in G} \mu(k) = \frac{1}{|G|} = U(g). $$

For the first equality, we re-indexed by setting $k = gh^{-1}$. $\blacksquare$

**2.6.1. Generating sets, irreducibility, Cayley graphs, and reversibility.** For a set $H \subset G$, let $\langle H \rangle$ be the smallest group containing all the elements of $H$; recall that every element of $\langle H \rangle$ can be written as a product of elements in $H$ and their inverses. A set $H$ is said to **generate** $G$ if $\langle H \rangle = G$.

PROPOSITION 2.13. *Let $\mu$ be a probability distribution on a finite group $G$. The random walk on $G$ with increment distribution $\mu$ is irreducible if and only if $S = \{g \in G : \mu(g) > 0\}$ generates $G$.*

PROOF. Let $a$ be an arbitrary element of $G$. If the random walk is irreducible, then there exists an $r > 0$ such that $P^r(\text{id}, a) > 0$. In order for this to occur, there must be a sequence $s_1, \ldots, s_r \in G$ such that $a = s_r s_{r-1} \ldots s_1$ and $s_i \in S$ for $i = 1, \ldots, r$. Thus $a \in \langle S \rangle$.

Now assume $S$ generates $G$, and consider $a, b \in G$. We know that $ba^{-1}$ can be written as a word in the elements of $S$ and their inverses. Since every element of $G$ has finite order, any inverse appearing in the expression for $ba^{-1}$ can be rewritten

### PDF page 45 (book page 29)

as a positive power of the same group element. Let the resulting expression be $ba^{-1} = s_r s_{r-1} \ldots s_1$, where $s_i \in S$ for $i = 1, \ldots, r$. Then

$$ P^m(a, b) \geq P(a, s_1 a)P(s_1 a, s_2 s_1 a) \cdots P(s_{r-1} s_{r-2} \ldots s_1 a, (ba^{-1})a) $$
$$ = \mu(s_1)\mu(s_2) \ldots \mu(s_r) > 0. $$

$\blacksquare$

When $S$ is a set which generates a finite group $G$, the **directed Cayley graph** associated to $G$ and $S$ is the directed graph with vertex set $G$ in which $(v, w)$ is an edge if and only if $v = sw$ for some generator $s \in S$. (When id $\in S$, the graph has loops.)

We call a set $S$ of generators of $G$ **symmetric** if $s \in S$ implies $s^{-1} \in S$. When $S$ is symmetric, all edges in the directed Cayley graph are bidirectional, and it may be viewed as an ordinary graph. When $G$ is finite and $S$ is a symmetric set that generates $G$, the simple random walk (as defined in Section 1.4) on the corresponding Cayley graph is the same as the random walk on $G$ with increment distribution $\mu$ taken to be the uniform distribution on $S$.

In parallel fashion, we call a probability distribution $\mu$ on a group $G$ **symmetric** if $\mu(g) = \mu(g^{-1})$ for every $g \in G$.

PROPOSITION 2.14. *The random walk on a finite group $G$ with increment distribution $\mu$ is reversible if $\mu$ is symmetric.*

PROOF. Let $U$ be the uniform probability distribution on $G$. For any $g, h \in G$, we have that

$$ U(g)P(g, h) = \frac{\mu(hg^{-1})}{|G|} \qquad \text{and} \qquad U(h)P(h, g) = \frac{\mu(gh^{-1})}{|G|} $$

are equal if and only if $\mu(hg^{-1}) = \mu((hg^{-1})^{-1})$. $\blacksquare$

REMARK 2.15. The converse of Proposition 2.14 is also true; see Exercise 2.7.

**2.6.2. Transitive chains.** A Markov chain is called **transitive** if for each pair $(x, y) \in \mathcal{X} \times \mathcal{X}$ there is a bijection $\varphi = \varphi_{(x,y)} : \mathcal{X} \to \mathcal{X}$ such that

$$ \varphi(x) = y \quad \text{and} \quad P(z, w) = P(\varphi(z), \varphi(w)) \text{ for all } z, w \in \mathcal{X}. \tag{2.15} $$

Roughly, this means the chain "looks the same" from any point in the state space $\mathcal{X}$. Clearly any random walk on a group is transitive; set $\varphi_{(x,y)}(g) = gx^{-1}y$. However, there are examples of transitive chains that are not random walks on groups; see **McKay and Praeger (1996)**.

Many properties of random walks on groups generalize to the transitive case, including Proposition 2.12.

PROPOSITION 2.16. *Let $P$ be the transition matrix of a transitive Markov chain on a finite state space $\mathcal{X}$. Then the uniform probability distribution on $\mathcal{X}$ is stationary for $P$.*

PROOF. Fix $x, y \in \mathcal{X}$ and let $\varphi : \mathcal{X} \to \mathcal{X}$ be a transition-probability-preserving bijection for which $\varphi(x) = y$. Let $U$ be the uniform probability on $\mathcal{X}$. Then

$$ \sum_{z \in \mathcal{X}} U(z)P(z, x) = \sum_{z \in \mathcal{X}} U(\varphi(z))P(\varphi(z), y) = \sum_{w \in \mathcal{X}} U(w)P(w, y), $$

### PDF page 46 (book page 30)

where we have re-indexed with $w = \varphi(z)$. We have shown that when the chain is started in the uniform distribution and run one step, the total weight arriving at each state is the same. Since $\sum_{x,z\in\mathcal{X}} U(z)P(z,x) = 1$, we must have

$$ \sum_{z\in\mathcal{X}} U(z)P(z,x) = \frac{1}{|\mathcal{X}|} = U(x). $$

$\blacksquare$

**2.7. Random Walks on $\mathbb{Z}$ and Reflection Principles**

A ***nearest-neighbor random walk*** on $\mathbb{Z}$ moves right and left by at most one step on each move, and each move is independent of the past. More precisely, if $(\Delta_t)$ is a sequence of independent and identically distributed $\{-1,0,1\}$-valued random variables and $X_t = \sum_{s=1}^{t} \Delta_s$, then the sequence $(X_t)$ is a nearest-neighbor random walk with increments $(\Delta_t)$.

This sequence of random variables is a Markov chain with infinite state space $\mathbb{Z}$ and transition matrix

$$ P(k, k+1) = p, \quad P(k,k) = r, \quad P(k, k-1) = q, $$

where $p + r + q = 1$.

The special case where $p = q = 1/2$, $r = 0$ is the simple random walk on $\mathbb{Z}$, as defined in Section 1.4. In this case

$$ \mathbf{P}_0\{X_t = k\} = \begin{cases} \binom{t}{\frac{t-k}{2}} 2^{-t} & \text{if } t-k \text{ is even,} \\ 0 & \text{otherwise,} \end{cases} \tag{2.16} $$

since there are $\binom{t}{\frac{t-k}{2}}$ possible paths of length $t$ from $0$ to $k$.

When $p = q = 1/4$ and $r = 1/2$, the chain is the lazy simple random walk on $\mathbb{Z}$. (Recall the definition of lazy chains in Section 1.3.)

THEOREM 2.17. *Let $(X_t)$ be simple random walk on $\mathbb{Z}$, and recall that*

$$ \tau_0 = \min\{t \geq 0 \,:\, X_t = 0\} $$

*is the first time the walk hits zero. Then*

$$ \mathbf{P}_k\{\tau_0 > r\} \leq \frac{6k}{\sqrt{r}} \tag{2.17} $$

*for any integers $k, r > 0$.*

We prove this by a sequence of lemmas which are of independent interest.

LEMMA 2.18 (Reflection Principle). *Let $(X_t)$ be the simple random walk or the lazy simple random walk on $\mathbb{Z}$. For any positive integers $j$, $k$, and $r$,*

$$ \mathbf{P}_k\{\tau_0 < r, X_r = j\} = \mathbf{P}_k\{X_r = -j\} \tag{2.18} $$

*and*

$$ \mathbf{P}_k\{\tau_0 < r, X_r > 0\} = \mathbf{P}_k\{X_r < 0\}. \tag{2.19} $$

PROOF. By the Markov property, if the first time the walk visits $0$ is at time $s$, then from time $s$ onwards, the walk has the same distribution as the walk started from zero, and is independent of the history of the walk up until time $s$. Hence for any $s < r$ and $j > 0$ we have

$$ \mathbf{P}_k\{\tau_0 = s, X_r = j\} = \mathbf{P}_k\{\tau_0 = s\}\mathbf{P}_0\{X_{r-s} = j\}. $$

### PDF page 47 (book page 31)

**FIGURE 2.3.** A path hitting zero and ending above zero can be transformed, by reflection, into a path ending below zero. *[Figure: a piecewise-linear random-walk path plotted against a horizontal zero axis; the solid path starts above zero, oscillates down to touch/cross zero, then rises to end above zero. After the first time it hits zero, the continuation is reflected across the axis (shown dotted) to produce a path that instead descends to end below zero.]*

The distribution of $X_t$ is symmetric when started at $0$, so the right-hand side is equal to

$$ \mathbf{P}_k\{\tau_0 = s\}\mathbf{P}_0\{X_{r-s} = -j\} = \mathbf{P}_k\{\tau_0 = s, X_r = -j\}. $$

Summing over $s < r$, we obtain

$$ \mathbf{P}_k\{\tau_0 < r, X_r = j\} = \mathbf{P}_k\{\tau_0 < r, X_r = -j\} = \mathbf{P}_k\{X_r = -j\}. $$

To justify the last equality, note that a random walk started from $k > 0$ must pass through $0$ before reaching a negative integer.

Finally, summing (2.18) over all $j > 0$ yields (2.19). $\blacksquare$

REMARK 2.19. There is also a simple combinatorial interpretation of the proof of Lemma 2.18. There is a one-to-one correspondence between walk paths which hit $0$ before time $r$ and are positive at time $r$ and walk paths which are negative at time $r$. This is illustrated in Figure 2.3: to obtain a bijection from the former set of paths to the latter set, reflect a path after the first time it hits $0$.

EXAMPLE 2.20 (First passage time for simple random walk). A nice application of Lemma 2.18 gives the distribution of $\tau_0$ when starting from $1$ for simple random walk on $\mathbb{Z}$. We have

$$ \begin{aligned} \mathbf{P}_1\{\tau_0 = 2m+1\} &= \mathbf{P}_1\{\tau_0 > 2m, X_{2m} = 1, X_{2m+1} = 0\} \\ &= \mathbf{P}_1\{\tau_0 > 2m, X_{2m} = 1\} \cdot \mathbf{P}_1\{X_{2m+1} = 0 \mid X_{2m} = 1\} \\ &= \mathbf{P}_1\{\tau_0 > 2m, X_{2m} = 1\} \cdot \left(\frac{1}{2}\right). \end{aligned} $$

Rewriting and using Lemma 2.18 yields

$$ \begin{aligned} \mathbf{P}_1\{\tau_0 = 2m+1\} &= \frac{1}{2}\Big[\mathbf{P}_1\{X_{2m} = 1\} - \mathbf{P}_1\{\tau_0 \leq 2m, X_{2m} = 1\}\Big] \\ &= \frac{1}{2}\Big[\mathbf{P}_1\{X_{2m} = 1\} - \mathbf{P}_1\{X_{2m} = -1\}\Big]. \end{aligned} $$

### PDF page 48 (book page 32)

Substituting using (2.16) shows that

$$ \mathbf{P}_1\{\tau_0 = 2m+1\} = \frac{1}{2}\left[\binom{2m}{m}2^{-2m} - \binom{2m}{m-1}2^{-2m}\right] = \frac{1}{(m+1)2^{2m+1}}\binom{2m}{m}. $$

The right-hand side above equals $C_m/2^{2m+1}$, where $C_m$ is the $m$-th ***Catalan number***.

LEMMA 2.21. *When $(X_t)$ is simple random walk or lazy simple random walk on $\mathbb{Z}$, we have*

$$ \mathbf{P}_k\{\tau_0 > r\} = \mathbf{P}_0\{-k < X_r \leq k\} $$

*for any $k > 0$.*

PROOF. Observe that

$$ \mathbf{P}_k\{X_r > 0\} = \mathbf{P}_k\{X_r > 0, \tau_0 \leq r\} + \mathbf{P}_k\{\tau_0 > r\}. $$

By Lemma 2.18,

$$ \mathbf{P}_k\{X_r > 0\} = \mathbf{P}_k\{X_r < 0\} + \mathbf{P}_k\{\tau_0 > r\}. $$

By symmetry of the walk, $\mathbf{P}_k\{X_r < 0\} = \mathbf{P}_k\{X_r > 2k\}$, and so

$$ \begin{aligned} \mathbf{P}_k\{\tau_0 > r\} &= \mathbf{P}_k\{X_r > 0\} - \mathbf{P}_k\{X_r > 2k\} \\ &= \mathbf{P}_k\{0 < X_r \leq 2k\} = \mathbf{P}_0\{-k < X_r \leq k\}. \end{aligned} $$

$\blacksquare$

LEMMA 2.22. *For the simple random walk $(X_t)$ on $\mathbb{Z}$,*

$$ \mathbf{P}_0\{X_t = k\} \leq \frac{3}{\sqrt{t}}. \tag{2.20} $$

REMARK 2.23. By applying Stirling's formula a bit more carefully than we do in the proof below, one can see that in fact

$$ \mathbf{P}_0\{X_{2r} = 2k\} \leq \frac{1}{\sqrt{\pi r}}\left[1 + o(1)\right]. $$

Hence the constant $3$ is nowhere near the best possible. Our goal here is to give an explicit upper bound valid for all $k$ without working too hard to achieve the best possible constant. Indeed, note that for simple random walk, if $t$ and $k$ have different parities, the probability on the left-hand side of (2.20) is $0$.

PROOF. If $X_{2r} = 2k$, there are $r+k$ "up" moves and $r-k$ "down" moves. The probability of this is $\binom{2r}{r+k}2^{-2r}$. The reader should check that $\binom{2r}{r+k}$ is maximized at $k = 0$, so for $k = 0, 1, \ldots, r$,

$$ \mathbf{P}_0\{X_{2r} = 2k\} \leq \binom{2r}{r}2^{-2r} = \frac{(2r)!}{(r!)^2 2^{2r}}. $$

By Stirling's formula (use the bounds $1 \leq e^{1/(12n+1)} \leq e^{1/(12n)} \leq 2$ in (A.19)), we obtain the bound

$$ \mathbf{P}_0\{X_{2r} = 2k\} \leq \sqrt{\frac{8}{\pi}}\frac{1}{\sqrt{2r}}. \tag{2.21} $$

To bound $\mathbf{P}_0\{X_{2r+1} = 2k+1\}$, condition on the first step of the walk and use the bound above. Then use the simple bound $[t/(t-1)]^{1/2} \leq \sqrt{2}$ to see that

$$ \mathbf{P}_0\{X_{2r+1} = 2k+1\} \leq \frac{4}{\sqrt{\pi}}\frac{1}{\sqrt{2r+1}}. \tag{2.22} $$

### PDF page 49 (book page 33)

**FIGURE 2.4.** For the Ballot Theorem: reflecting a "bad" path after the first time the vote counts are equal yields a path to $(b, a)$. *[Figure: An up-right (staircase) path in the first quadrant starting at the origin, rising in unit steps to the point $(a,b)$. A dashed diagonal line $x=y$ runs through the plot. After the first time the path meets the diagonal, its remaining portion is reflected across the diagonal (shown dashed), ending at the point $(b,a)$ below the line.]*

Putting together (2.21) and (2.22) establishes (2.20), since $4/\sqrt{\pi} \le 3$. $\blacksquare$

PROOF OF THEOREM 2.17. Combining Lemma 2.21 and Lemma 2.22, we obtain (2.17). $\blacksquare$

**2.7.1. The Ballot Theorem\*.** The bijection illustrated in Figure 2.3 has another very nice consequence. Define an ***up-right path*** to be a path through the two-dimensional grid in which every segment heads either up or to the right.

THEOREM 2.24 (Ballot Theorem). *Fix positive integers $a$ and $b$ with $a < b$. An up-right path from $(0,0)$ to $(a, b)$ chosen uniformly at random has probability $\frac{b-a}{a+b}$ of lying strictly above the line $x = y$ (except for its initial point).*

There is a vivid interpretation of Theorem 2.24. Imagine that $a + b$ votes are being tallied. The up-right path graphs the progress of the pair (votes for candidate A, votes for candidate B) as the votes are counted. Assume we are given that the final totals are $a$ votes for A and $b$ votes for B. Then the probability that the winning candidate was always ahead, from the first vote counted to the last, under the assumption that all possible paths leading to these final totals are equally likely, is exactly $(b - a)/(a + b)$.

PROOF. The total number of up-right paths from $(0, 0)$ to $(a, b)$ is $\binom{a+b}{b}$, since there are $a + b$ steps total, of which exactly $b$ steps go up.

How many paths never touch the line $x = y$ after the first step? Any such path must have its first step up, and there are $\binom{a+b-1}{b-1}$ such paths. How many of those paths touch the line $x = y$?

Given a path whose first step is up and that touches the line $x = y$, reflecting the portion after the first touch of $x = y$ yields a path from $(0, 0)$ whose first step is up and which ends at $(b, a)$. See Figure 2.4. Since every up-right path whose first step is up and which ends at $(b, a)$ must cross $x = y$, we obtain every such path via this reflection. Hence there are $\binom{a+b-1}{b}$ "bad" paths to subtract, and the desired probability is

$$ \frac{\binom{a+b-1}{b-1} - \binom{a+b-1}{b}}{\binom{a+b}{b}} = \frac{a!b!}{(a+b)!}\left(\frac{(a+b-1)!}{a!(b-1)!} - \frac{(a+b-1)!}{(a-1)!b!}\right) = \frac{b-a}{a+b}. $$

$\blacksquare$

### PDF page 50 (book page 34)

REMARK 2.25. Figures 2.3 and 2.4 clearly illustrate versions of the same bijection. The key step in the proof of Theorem 2.24, counting the "bad" paths, is a case of (2.18): look at the paths after their first step, and set $k = 1$, $r = a + b - 1$ and $j = b - a$.

**Exercises**

EXERCISE 2.1. Show that the system of equations for $0 < k < n$

$$ f_k = \frac{1}{2}\left(1 + f_{k+1}\right) + \frac{1}{2}\left(1 + f_{k-1}\right), \tag{2.23} $$

together with the boundary conditions $f_0 = f_n = 0$ has a unique solution $f_k = k(n - k)$.

*Hint:* One approach is to define $\Delta_k = f_k - f_{k-1}$ for $1 \le k \le n$. Check that $\Delta_k = \Delta_{k+1} + 2$ (so the $\Delta_k$'s form an arithmetic progression) and that $\sum_{k=1}^{n} \Delta_k = 0$.

EXERCISE 2.2. Consider a hesitant gambler: at each time, she flips a coin with probability $p$ of success. If it comes up heads, she places a fair one dollar bet. If tails, she does nothing that round, and her fortune stays the same. If her fortune ever reaches 0 or $n$, she stops playing. Assuming that her initial fortune is $k$, find the expected number of rounds she will play, in terms of $n$, $k$, and $p$.

EXERCISE 2.3. Consider a random walk on the path $\{0, 1, \ldots, n\}$ in which the walk moves left or right with equal probability except when at $n$ and 0. When at the end points, it remains at the current location with probability $1/2$, and moves one unit towards the center with probability $1/2$. Compute the expected time of the walk's absorption at state 0, given that it starts at state $n$.

EXERCISE 2.4. Use the inequalities $1/(k + 1) \le \int_k^{k+1} \frac{dx}{x} \le 1/k$ to show that

$$ \log(n + 1) \le \sum_{k=1}^{n} k^{-1} \le 1 + \log n. \tag{2.24} $$

EXERCISE 2.5. Let $P$ be the transition matrix for the Ehrenfest chain described in (2.8). Show that the binomial distribution with parameters $n$ and $1/2$ is the stationary distribution for this chain.

EXERCISE 2.6. Give an example of a random walk on a finite abelian group which is *not* reversible.

EXERCISE 2.7. Show that if a random walk on a finite group is reversible, then the increment distribution is symmetric.

EXERCISE 2.8. Show that when the transition matrix $P$ of a Markov chain is transitive, then the transition matrix $\widehat{P}$ of its time reversal is also transitive.

EXERCISE 2.9. Fix $n \ge 1$. Show that simple random walk on the $n$-cycle, defined in Example 1.4, is a projection (in the sense of Section 2.3.1) of the simple random walk on $\mathbb{Z}$ defined in Section 2.7.

EXERCISE 2.10 (Reflection Principle). Let $(S_n)$ be the simple random walk on $\mathbb{Z}$. Show that

$$ \mathbf{P}\left\{\max_{1 \le j \le n} |S_j| \ge c\right\} \le 2\mathbf{P}\left\{|S_n| \ge c\right\}. $$

### PDF page 51 (book page 35)

EXERCISE 2.11. Consider the $d$-color Pólya urn: Initially the urn contains one ball of each of $d$ distinct colors. At each unit of time, a ball is selected uniformly at random from the urn and replaced along with an additional ball of the same color. Let $N_t^i$ be the the [sic] number of balls in the urn of color $i$ after $t$ steps. Prove Lemma 2.7, which states that if $\boldsymbol{N}_t := (N_t^1, \ldots, N_t^d)$, then $\boldsymbol{N}_t$ is uniformly distributed over the set

$$ V_t = \left\{(x_1, \ldots, x_d) \, : \, x_i \in \mathbb{Z},\, x_i \ge 1 \text{ for all } i = 1, \ldots, d, \ \text{ and } \ \sum_{i=1}^{d} x_i = t + d\right\}. $$

**Notes**

Many of the examples in this chapter are also discussed in **Feller (1968)**. See Chapter XIV for the gambler's ruin, Section IX.3 for coupon collecting, Section V.2 for urn models, and Chapter III for the reflection principle. Grinstead and Snell (**1997**, Chapter 12) discusses gambler's ruin.

See any undergraduate algebra book, for example **Herstein (1975)** or Artin (**1991**), for more information on groups. Much more can be said about random walks on groups than for general Markov chains. **Diaconis (1988a)** is a starting place.

Pólya's urn was introduced in **Eggenberger and Pólya (1923)** and **Pólya (1931)**. Urns are fundamental models for reinforced processes. See **Pemantle (2007)** for a wealth of information and many references on urn processes and more generally processes with reinforcement. The book **Johnson and Kotz (1977)** is devoted to urn models.

See **Stanley (1999**, pp. 219–229) and **Stanley (2008)** for many interpretations of the Catalan numbers.

The exact asymptotics for the coupon collectors variable $\tau$ (to collect all coupon types) is in **Erdős and Rényi (1961)**. They prove that

$$ \lim_{n \to \infty} \mathbf{P}\{\tau < n \log n + cn\} = e^{-e^{-c}}. \tag{2.25} $$

**Complements.** Generalizations of Theorem 2.17 to walks on $\mathbb{Z}$ other than simple random walks are very useful; we include one here.

THEOREM 2.26. *Let $(\Delta_i)$ be i.i.d. integer-valued variables with mean zero and variance $\sigma^2$. Let $X_t = \sum_{i=1}^{t} \Delta_i$. Then*

$$ \mathbf{P}\{X_t \ne 0 \text{ for } 1 \le t \le r\} \le \frac{4\sigma}{\sqrt{r}}. \tag{2.26} $$

REMARK 2.27. The constant in this estimate is not sharp, but we will give a very elementary proof based on Chebyshev's inequality.

PROOF. For $I \subseteq \mathbb{Z}$, let

$$ L_r(I) := \{t \in \{0, 1, \ldots, r\} \, : \, X_t \in I\} $$

be the set of times up to and including $r$ when the walk visits $I$, and write $L_r(v) = L_r(\{v\})$. Define also

$$ A_r := \{t \in L_r(0) \, : \, X_{t+u} \ne 0 \text{ for } 1 \le u \le r\}, $$

### PDF page 52 (book page 36)

the set of times $t$ in $L_r(0)$ where the walk does not visit 0 for $r$ steps after $t$. Since the future of the walk after visiting 0 is independent of the walk up until this time,

$$ \mathbf{P}\{t \in A_r\} = \mathbf{P}\{t \in L_r(0)\}\alpha_r, $$

where

$$ \alpha_r := \mathbf{P}_0\{X_t \neq 0,\, t = 1, \ldots, r\}. $$

Summing this over $t \in \{0, 1, \ldots, r\}$ and noting that $|A_r| \leq 1$ gives

$$ 1 \geq \mathbf{E}|A_r| = \mathbf{E}|L_r(0)|\alpha_r. \tag{2.27} $$

It remains to estimate $\mathbf{E}|L_r(0)|$ from below, and this can be done using the local Central Limit Theorem or (in special cases) Stirling's formula.

A more direct (but less precise) approach is to first use Chebyshev's inequality to show that

$$ \mathbf{P}\{|X_t| \geq \sigma\sqrt{r}\} \leq \frac{t}{r} $$

and then deduce for $I = (-\sigma\sqrt{r}, \sigma\sqrt{r})$ that

$$ \mathbf{E}|L_r(I^c)| \leq \sum_{t=1}^{r} \frac{t}{r} = \frac{r+1}{2}, $$

whence $\mathbf{E}|L_r(I)| \geq r/2$. For any $v \neq 0$, we have

$$ \mathbf{E}|L_r(v)| = \mathbf{E}\left(\sum_{t=0}^{r} \mathbf{1}_{\{X_t=v\}}\right) = \mathbf{E}\left(\sum_{t=\tau_v}^{r} \mathbf{1}_{\{X_t=v\}}\right). \tag{2.28} $$

By the Markov property, the chain after time $\tau_v$ has the same distribution as the chain started from $v$. Hence the right-hand side of $(2.28)$ is bounded above by

$$ \mathbf{E}_v\left(\sum_{t=0}^{r} \mathbf{1}_{\{X_t=v\}}\right) = \mathbf{E}_0\left(\sum_{t=0}^{r} \mathbf{1}_{\{X_t=0\}}\right). $$

We conclude that $r/2 \leq \mathbf{E}|L_r(I)| \leq 2\sigma\sqrt{r}\mathbf{E}|L_r(0)|$. Thus $\mathbf{E}|L_r(0)| \geq \sqrt{r}/(4\sigma)$. In conjunction with $(2.27)$ this proves $(2.26)$. $\blacksquare$

COROLLARY 2.28. *For the lazy simple random walk on $\mathbb{Z}$ started at height $k$,*

$$ \mathbf{P}_k\{\tau_0^+ > r\} \leq \frac{3k}{\sqrt{r}}. \tag{2.29} $$

PROOF. By conditioning on the first move of the walk and then using the fact that the distribution of the walk is symmetric about 0, for $r \geq 1$,

$$
\begin{aligned}
\mathbf{P}_0\{\tau_0^+ > r\} &\geq \mathbf{P}_0\{\tau_0^+ > r + 1\} \\
&= \frac{1}{4}\mathbf{P}_1\{\tau_0^+ > r\} + \frac{1}{4}\mathbf{P}_{-1}\{\tau_0^+ > r\} + \frac{1}{2}\mathbf{P}_0\{\tau_0^+ > r\} \\
&= \frac{1}{2}\mathbf{P}_1\{\tau_0^+ > r\} + \frac{1}{2}\mathbf{P}_0\{\tau_0^+ > r\}.
\end{aligned}
$$

Subtracting the second term on the right-hand side from both sides,

$$ \mathbf{P}_1\{\tau_0^+ > r\} \leq \mathbf{P}_0\{\tau_0^+ > r\}. \tag{2.30} $$

Note that when starting from 1, the event that the walk hits height $k$ before visiting 0 for the first time and subsequently does not hit 0 for $r$ steps is contained

### PDF page 53 (book page 37)

in the event that the walk started from 1 does not hit 0 for $r - 1$ steps. Thus, from $(2.30)$ and Theorem $2.26$,

$$ \mathbf{P}_1\{\tau_k < \tau_0\}\mathbf{P}_k\{\tau_0^+ > r\} \leq \mathbf{P}_1\{\tau_0 > r\} \leq \mathbf{P}_0\{\tau_0^+ > r\} \leq \frac{2\sqrt{2}}{\sqrt{r}}. \tag{2.31} $$

(The variance $\sigma^2$ of the increments of the lazy random walk is $1/2$.) From the gambler's ruin formula given in $(2.1)$, the chance that a simple random walk starting from height 1 hits $k$ before visiting 0 is $1/k$. The probability is the same for a lazy random walk, so together with $(2.31)$ this implies $(2.29)$. $\blacksquare$

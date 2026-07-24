# Chapter 6 — Strong Stationary Times
*(PDF pages 91–103; book pages 75–87)*

### PDF page 91 (book page 75)

CHAPTER 6

# Strong Stationary Times

**6.1. Top-to-Random Shuffle**

We begin this chapter with an example. Consider the following (slow) method of shuffling a deck of $n$ cards: take the top card and insert it uniformly at random in the deck. This process will eventually mix up the deck—the successive arrangements of the deck are a random walk on the group $\mathcal{S}_n$ of $n!$ possible permutations of the cards, which by Proposition 2.12 has uniform stationary distribution.

**FIGURE 6.1.** The top-to-random shuffle. *[Figure: A stack of hatched cards fanned diagonally; the top card is being lifted and moved along a curved arrow to be reinserted into the deck, where a hand holds a card poised to slide into one of the slots. Label "Original bottom card" points to the lowest card in the stack; label "Next card to be placed in one of the slots under the original bottom card" points to the card held by the hand, with arrows indicating candidate insertion slots.]*

How long must we shuffle using this method until the arrangement of the deck is close to random?

Let $\tau_{\text{top}}$ be the time *one move after the first occasion when the original bottom card has moved to the top of the deck.* We show now that the arrangement of cards

### PDF page 92 (book page 76)

at time $\tau_{\text{top}}$ is distributed uniformly on the set $\mathcal{S}_n$ of all permutations of $\{1, \ldots, n\}$ and moreover this random element of $\mathcal{S}_n$ is independent of the time $\tau_{\text{top}}$.

More generally, we prove the following:

PROPOSITION 6.1. *Let $(X_t)$ be the random walk on $\mathcal{S}_n$ corresponding to the top-to-random shuffle on $n$ cards. Given at time $t$ that there are $k$ cards under the original bottom card, each of the $k!$ possible orderings of these cards are equally likely. Therefore, if $\tau_{\text{top}}$ is one shuffle after the first time that the original bottom card moves to the top of the deck, then the distribution of $X_{\tau_{\text{top}}}$ is uniform over $\mathcal{S}_n$, and the time $\tau_{\text{top}}$ is independent of $X_{\tau_{\text{top}}}$.*

PROOF. When $t = 0$, there are no cards under the original bottom card, and the claim is trivially valid. Now suppose that the claim holds at time $t$. There are two possibilities at time $t + 1$: either a card is placed under the original bottom card, or not. In the second case, the cards under the original bottom card remain in random order. In the first case, given that the card is placed under the original bottom card, each of the $k + 1$ possible locations for the card is equally likely, and so each of the $(k + 1)!$ orderings are equiprobable. $\blacksquare$

The above theorem implies that, for any $t$, given that $\tau_{\text{top}} = t$, the distribution of $X_t$ is uniform. In this chapter, we show how we can use the distribution of the *random* time $\tau_{\text{top}}$ to bound $t_{\text{mix}}$, the *fixed* number of steps needed for the distribution of the chain to be *approximately* stationary.

We conclude the introduction with another example.

EXAMPLE 6.2 (Random walk on the hypercube). The lazy random walk $(\boldsymbol{X}_t)$ on the hypercube $\{0, 1\}^n$ was introduced in Section 2.3, and we used coupling to bound the mixing time in Section 5.3.1. Recall that a move of this walk can be constructed using the following random mapping representation: an element $(j, B)$ from $\{1, 2, \ldots, n\} \times \{0, 1\}$ is selected uniformly at random, and coordinate $j$ of the current state is updated with the bit $B$.

In this construction, the chain is determined by the i.i.d. sequence $(Z_t)$, where $Z_t = (j_t, B_t)$ is the coordinate and bit pair used to update at step $t$.

Define
$$ \tau_{\text{refresh}} := \min \left\{ t \geq 0 \, : \, \{j_1, \ldots, j_t\} = \{1, 2, \ldots, n\} \right\}, $$
the first time when all the coordinates have been selected at least once for updating.

Because at time $\tau_{\text{refresh}}$ all of the coordinates have been replaced with independent fair bits, the distribution of the chain at this time is uniform on $\{0, 1\}^n$. That is, $X_{\tau_{\text{refresh}}}$ is an exact sample from the stationary distribution $\pi$.

**6.2. Markov Chains with Filtrations**

In Example 6.2, the random time $\tau_{\text{refresh}}$ is not a function of $(X_t)$, but it is a function of the update variables $(Z_t)$.

Indeed, in this example and others, the Markov chain is specified using a random mapping representation, as described in Section 1.2, and it is useful to track not just the chain itself, but the variables which are used to generate the chain. For this reason it will sometimes be necessary to consider Markov chains with respect to filtrations, which we define below.

We make use of the conditional expectation of a random variable with respect to a $\sigma$-algebra. See Appendix A.2 for the definition and basic properties.

### PDF page 93 (book page 77)

Let $\{\mathcal{F}_t\}$ be a *filtration*, a sequence of $\sigma$-algebras such that $\mathcal{F}_t \subset \mathcal{F}_{t+1}$ for all $t$. We say that $\{X_t\}$ is *adapted* to $\{\mathcal{F}_t\}$ if $X_t$ is $\mathcal{F}_t$-measurable for all $t$. If $\mathcal{H}_t = \sigma(X_0, X_1, \ldots, X_t)$, then $\{\mathcal{H}_t\}$ is called the *natural filtration*. Clearly $\{X_t\}$ is adapted to the natural filtration.

Suppose that $\{X_t\}$ is adapted to $\{\mathcal{F}_t\}$. We say that $\{X_t\}$ is a **Markov chain with respect to** $\{\mathcal{F}_t\}$ if
$$ \mathbf{P}_x\{X_{t+1} = y \mid \mathcal{F}_t\} = P(X_t, y), \tag{6.1} $$
where $P$ is a transition matrix. A Markov chain as defined by (1.1) satisfies (6.1) when $\{\mathcal{F}_t\}$ is the natural filtration.

A **stopping time** for the filtration $\{\mathcal{F}_t\}$ is a random variable $\tau$ with values in $\{0, 1, \ldots\}$ such that $\{\tau = t\} \in \mathcal{F}_t$. If the filtration of a stopping time is not specified, it will be assumed to be the natural filtration.

Suppose you give instructions to your stock broker to sell a particular security when its value next drops below 32 dollars per share. This directive can be implemented by a computer program: at each unit of time, the value of the security is checked; if the value at that time is at least 32, no action is taken, while if the value is less than 32, the asset is sold and the program quits.

You would like to tell your broker to sell a stock at the first time its value equals its maximum value over its lifetime. However, this is not a reasonable instruction, because to determine on Wednesday whether or not to sell, the broker needs to know that on Thursday the value will not rise and in fact for the entire infinite future that the value will never exceed its present value. To determine the correct decision on Wednesday, the broker must be able to see into the future!

The first instruction is an example of a stopping time, while the second rule is not.

EXAMPLE 6.3 (Hitting times). Fix $A \subseteq \mathcal{X}$. The vector $(X_0, X_1, \ldots, X_t)$ determines whether a site in $A$ is visited for the first time at time $t$. That is, if
$$ \tau_A = \min\{t \geq 0 \, : \, X_t \in A\} $$
is the first time that the sequence $(X_t)$ is in $A$, then
$$ \{\tau_A = t\} = \{X_0 \notin A, X_1 \notin A, \ldots, X_{t-1} \notin A, X_t \in A\}. $$
Therefore, $\tau_A$ is a stopping time for the natural filtration, since the set on the right-hand side above is clearly an element of $\sigma(X_0, \ldots, X_t)$. (We saw the special case where $A = \{x\}$ consists of a single state in Section 1.5.2.)

EXAMPLE 6.4 (Example 6.2, continued). The random time $\tau_{\text{refresh}}$ is not a stopping time for the natural filtration. However, it is a stopping time for $\mathcal{F}_t = \sigma(Z_0, Z_1, \ldots, Z_t)$, where $Z_t$ is the random vector defined in Example 6.2.

EXAMPLE 6.5. Consider the top-to-random shuffle, defined in Section 6.1. Let $A$ be the set of arrangements having the original bottom card on top. Then $\tau_{\text{top}} = \tau_A + 1$. By Exercise 6.1, $\tau_{\text{top}}$ is a stopping time.

**6.3. Stationary Times**

For the top-to-random shuffle, one shuffle after the original bottom card rises to the top, the deck is in completely random order. Likewise, for the lazy random walker on the hypercube, at the first time when all of the coordinates have been

### PDF page 94 (book page 78)

updated, the state of the chain is a random sample from $\{0,1\}^n$. These random times are examples of **stationary times**, which we now define.

Let $(X_t)$ be an irreducible Markov chain with stationary distribution $\pi$. Suppose that $\{\mathcal{F}_t\}$ is a filtration, and $\{X_t\}$ is adapted to $\{\mathcal{F}_t\}$. A **stationary time** $\tau$ for $(X_t)$ is an $\{\mathcal{F}_t\}$-stopping time, possibly depending on the starting position $x$, such that the distribution of $X_\tau$ is $\pi$:

$$ \mathbf{P}_x\{X_\tau = y\} = \pi(y) \quad \text{for all } y. \tag{6.2} $$

EXAMPLE 6.6. Let $(X_t)$ be an irreducible Markov chain with state space $\mathcal{X}$ and stationary distribution $\pi$. Let $\xi$ be a $\mathcal{X}$-valued random variable with distribution $\pi$, and define

$$ \tau = \min\{t \geq 0 \,:\, X_t = \xi\}. $$

Let $\mathcal{F}_t = \sigma(\xi, X_0, X_1, \ldots, X_t)$. The time $\tau$ is an $\{\mathcal{F}_t\}$-stopping time stopping time, and because $X_\tau = \xi$, it follows that $\tau$ is a stationary time.

Suppose the chain starts at $x_0$. If $\tau = 0$, then $X_\tau = x_0$; therefore, $\tau$ and $X_\tau$ are not independent.

EXAMPLE 6.7. Let $(X_t)$ be the random walk on the $n$-cycle. Define $\tau$ by tossing a coin with probability of heads $1/n$. If "heads", let $\tau = 0$; if "tails", let $\tau$ be the first time every state has been visited at least once. Given "tails", the distribution of $X_\tau$ is uniform over all $n-1$ states different from the starting state. (See Exercise 6.10.) This shows that $X_\tau$ has the uniform distribution, whence $\tau$ is a stationary time.

However, $\tau = 0$ implies that $X_\tau$ is the starting state. Therefore, as in Example 6.6, $\tau$ and $X_\tau$ are not independent.

As mentioned at the end of Section 6.1, we want to use the time $\tau_{\text{top}}$ to bound $t_{\text{mix}}$. To carry out this program, we need a property of $\tau_{\text{top}}$ stronger than (6.2). We will need that $\tau_{\text{top}}$ is independent of $X_{\tau_{\text{top}}}$, a property not enjoyed by the stationary times in Example 6.6 and Example 6.7.

**6.4. Strong Stationary Times and Bounding Distance**

Let $(X_t)$ be a Markov chain with respect to the filtration $\{\mathcal{F}_t\}$, with stationary distribution $\pi$. A **strong stationary time** for $(X_t)$ and starting position $x$ is an $\{\mathcal{F}_t\}$-stopping time $\tau$, such that for all times $t$ and all $y$,

$$ \mathbf{P}_x\{\tau = t, \; X_\tau = y\} = \mathbf{P}_x\{\tau = t\}\pi(y). \tag{6.3} $$

In words, $X_\tau$ has distribution $\pi$ and is independent of $\tau$.

REMARK 6.8. If $\tau$ is a strong stationary time starting from $x$, then

$$ \mathbf{P}_x\{\tau \leq t, \, X_t = y\} = \sum_{s \leq t} \sum_z \mathbf{P}_x\{\tau = s, \, X_s = z, \, X_t = y\} $$
$$ = \sum_{s \leq t} \sum_z P^{t-s}(z, y)\mathbf{P}_x\{\tau = s\}\pi(z). $$

It follows from the stationarity of $\pi$ that $\sum_z \pi(z)P^{t-s}(z, y) = \pi(y)$, whence for all $t \geq 0$ and $y$,

$$ \mathbf{P}_x\{\tau \leq t, \, X_t = y\} = \mathbf{P}_x\{\tau \leq t\}\pi(y). \tag{6.4} $$

### PDF page 95 (book page 79)

EXAMPLE 6.9. For the top-to-random shuffle, the first time $\tau_{\text{top}}$ when the original bottom card gets placed into the deck by a shuffle is a strong stationary time. This is the content of Proposition 6.1.

EXAMPLE 6.10. We return to Example 6.2, the lazy random walk on the hypercube. The time $\tau_{\text{refresh}}$, the first time each of the coordinates have been refreshed with an independent fair bit, is a strong stationary time.

We now return to the program suggested at the end of Section 6.1 and use strong stationary times to bound $t_{\text{mix}}$.

The route from strong stationary times to bounding convergence time is the following proposition:

PROPOSITION 6.11. *If $\tau$ is a strong stationary time for starting state $x$, then*

$$ \|P^t(x, \cdot) - \pi\|_{\text{TV}} \leq \mathbf{P}_x\{\tau > t\}. \tag{6.5} $$

We break the proof into two lemmas. It will be convenient to introduce a parameter $s_x(t)$, called **separation distance** and defined by

$$ s_x(t) := \max_{y \in \mathcal{X}} \left[ 1 - \frac{P^t(x, y)}{\pi(y)} \right]. \tag{6.6} $$

The distance $s_x(t)$ is weakly decreasing in $t$ (see Exercise 6.4.) We also define

$$ s(t) := \max_{x \in \mathcal{X}} s_x(t). \tag{6.7} $$

The Convergence Theorem implies that $s(t) \to 0$ as $t \to \infty$ for aperiodic irreducible chains. See also Lemma 6.17.

The separation distance superficially resembles the $\ell^\infty$ distance, but (at least for reversible chains), it is closer to total variation distance. See Lemma 6.17. For example, for lazy random walk on the $n$-vertex complete graph, $s(2) \leq 1/4$, while $t_{\text{mix}}^{(\infty)}$ is of order $\log n$. See Exercise 6.5.

The relationship between $s_x(t)$ and strong stationary times is

LEMMA 6.12. *If $\tau$ is a strong stationary time for starting state $x$, then*

$$ s_x(t) \leq \mathbf{P}_x\{\tau > t\}. \tag{6.8} $$

PROOF. Fix $x \in \mathcal{X}$. Observe that for every $y \in \mathcal{X}$,

$$ 1 - \frac{P^t(x, y)}{\pi(y)} = 1 - \frac{\mathbf{P}_x\{X_t = y\}}{\pi(y)} \leq 1 - \frac{\mathbf{P}_x\{X_t = y, \, \tau \leq t\}}{\pi(y)}. \tag{6.9} $$

By Remark 6.8, the right-hand side equals

$$ 1 - \frac{\pi(y)\mathbf{P}_x\{\tau \leq t\}}{\pi(y)} = \mathbf{P}_x\{\tau > t\}. \tag{6.10} $$

$\blacksquare$

DEFINITION 6.13. Given starting state $x$, a state $y$ is a **halting state** for a stopping time $\tau$ if $X_t = y$ implies $\tau \leq t$. For example, when starting the lazy random walk on the hypercube at $(0, \ldots, 0)$, the state $(1, \ldots, 1)$ is a halting state for the stopping time $\tau_{\text{refresh}}$ defined in Example 6.2.

### PDF page 96 (book page 80)

PROPOSITION 6.14. *If there exists a halting state for starting state $x$, then $\tau$ is an optimal strong stationary time for $x$, i.e.*

$$ s_x(t) = \mathbf{P}_x\{\tau > t\}\,, $$

*and it is stochastically dominated under $\mathbf{P}_x$ by every other strong stationary time.*

PROOF. If $y$ is a halting state for starting state $x$ and the stopping time $\tau$, then inequality (6.9) is an equality for every $t$. Therefore, if there exists a halting state for starting state $x$, then (6.8) is also an equality. $\blacksquare$

The converse is false: for simple random walk on a triangle there is no strong stationary time with a halting state. See Example 24.15.

EXAMPLE 6.15. Consider the top-to-random shuffle again (Section 6.1). Let $\tau$ be one shuffle after the first time that the next-to-bottom card comes to the top. As noted in Exercise 6.2, $\tau$ is a strong stationary time.

Note that every configuration with the next-to-bottom card in the bottom position is a halting state, so this must be an optimal strong stationary time.

We give a construction of strong stationary time with a halting state for birth-and-death chains in Chapter 17, Example 17.26.

The next lemma along with Lemma 6.12 proves Proposition 6.11.

LEMMA 6.16. *The separation distance $s_x(t)$ satisfies*

$$ \left\| P^t(x, \cdot) - \pi \right\|_{\text{TV}} \leq s_x(t), \tag{6.11} $$

*and therefore $d(t) \leq s(t)$.*

PROOF. We have

$$ \|P^t(x, \cdot) - \pi\|_{\text{TV}} = \sum_{\substack{y \in \mathcal{X} \\ P^t(x,y) < \pi(y)}} \left[ \pi(y) - P^t(x, y) \right] = \sum_{\substack{y \in \mathcal{X} \\ P^t(x,y) < \pi(y)}} \pi(y) \left[ 1 - \frac{P^t(x, y)}{\pi(y)} \right] $$
$$ \leq \max_y \left[ 1 - \frac{P^t(x, y)}{\pi(y)} \right] = s_x(t). $$

$\blacksquare$

Recall the definition of $\bar{d}$ in (4.23).

LEMMA 6.17. *For a reversible chain, the separation and total variation distances satisfy*

$$ s(2t) \leq 1 - (1 - \bar{d}(t))^2 \leq 2\bar{d}(t) \leq 4d(t)\,. \tag{6.12} $$

PROOF. The middle inequality follows from expanding the square, and the last from Lemma 4.10, so it remains to prove the first inequality.

By reversibility, $P^t(z, y)/\pi(y) = P^t(y, z)/\pi(z)$, whence

$$ \frac{P^{2t}(x, y)}{\pi(y)} = \sum_{z \in \mathcal{X}} \frac{P^t(x, z)P^t(z, y)}{\pi(y)} = \sum_{z \in \mathcal{X}} \pi(z)\frac{P^t(x, z)P^t(y, z)}{\pi(z)^2}. $$

### PDF page 97 (book page 81)

**FIGURE 6.2.** Two complete graphs (on 4 vertices), "glued" at a single vertex. Loops have been added so that every vertex has the same degree (count each loop as one edge). *[Figure: Two identical "flower" clusters joined edge-to-edge, sharing a central vertex. Each cluster is a complete graph on 4 solid-black vertices (drawn as filled circles) with all six edges present, and every vertex has several small loops (petals) attached, giving the flower appearance. The two clusters meet at the middle vertex, which sits between them.]*

Applying Cauchy-Schwarz to the right-hand side above, we have

$$\frac{P^{2t}(x,y)}{\pi(y)} \geq \left( \sum_{z\in\mathcal{X}} \sqrt{P^t(x,z)P^t(y,z)} \right)^2$$
$$\geq \left( \sum_{z\in\mathcal{X}} P^t(x,z) \wedge P^t(y,z) \right)^2 .$$

From equation (4.13),

$$\frac{P^{2t}(x,y)}{\pi(y)} \geq \left( 1 - \left\| P^t(x,\cdot) - P^t(y,\cdot) \right\|_{\mathrm{TV}} \right)^2 \geq \left( 1 - \bar{d}(t) \right)^2 .$$

Subtracting both sides of the inequality from 1 and maximizing over $x$ and $y$ yields (6.12). $\blacksquare$

### **6.5. Examples**

**6.5.1. Two glued complete graphs.** Consider the graph $G$ obtained by taking two complete graphs on $n$ vertices and "gluing" them together at a single vertex. We analyze here simple random walk on a slightly modified graph, $G'$.

Let $v^\star$ be the vertex where the two complete graphs meet. After gluing, $v^\star$ has degree $2n - 2$, while every other vertex has degree $n - 1$. To make the graph regular and to ensure non-zero holding probability at each vertex, in $G'$ we add one loop at $v^\star$ and $n$ loops at all other vertices. (See Figure 6.2 for an illustration when $n = 4$.) The uniform distribution is stationary for simple random walk on $G'$, since it is regular of degree $2n - 1$.

It is clear that when at $v^\star$, the next state is equally likely to be each of the $2n - 1$ vertices. Thus, if $\tau_{v^\star}$ is the hitting time of $v^\star$, then $\tau = \tau_{v^\star} + 1$ is a strong stationary time .

### PDF page 98 (book page 82)

When the walk is *not* at $v^\star$, the probability of moving to $v^\star$ is $1/(2n-1)$. That is, $\tau_{v^\star}$ is geometric with parameter $1/(2n-1)$. Therefore,

$$\mathbf{P}_x\{\tau > t\} \leq \left( 1 - \frac{1}{2n-1} \right)^{t-1} . \tag{6.13}$$

Thus $\mathbf{P}_x\{\tau > t\} \leq e^{-2}$ when $t = 4n$, and

$$t_{\mathrm{mix}} \leq 4n.$$

A lower bound on $t_{\mathrm{mix}}$ of order $n$ is obtained in Exercise 6.8.

**6.5.2. Random walk on the hypercube.** We return to Example 6.2, the lazy random walker on $\{0,1\}^n$. As noted in Example 6.10, the random variable $\tau_{\mathrm{refresh}}$, the time when each coordinate has been selected at least once for the first time, is a strong stationary time. The time $\tau_{\mathrm{refresh}}$ already occurred in the coordinate-by-coordinate coupling used in Section 5.3.1, and is identical to the coupon collector's time of Section 2.2. It is therefore not surprising that we obtain here exactly the same upper bound for $t_{\mathrm{mix}}$ as was found using the coupling method. In particular, combining Proposition 2.4 and Lemma 6.12 shows that the separation distance satisfies, for each $x$,

$$s_x(n \log n + cn) \leq e^{-c}. \tag{6.14}$$

By Lemma 6.16,

$$t_{\mathrm{mix}}(\varepsilon) \leq n \log n + \log(\varepsilon^{-1})n. \tag{6.15}$$

REMARK 6.18. The reason we explicitly give a bound on the separation distance here and appeal to Lemma 6.16, instead of applying directly Proposition 6.11, is that there is a matching lower bound on $s(t)$, which we give in Section 18.4. This contrasts with the lower bound on $d(t)$ we will find in Section 7.3.1, which implies $t_{\mathrm{mix}}(1 - \varepsilon) \geq (1/2)n \log n - c(\varepsilon)n$. In fact, the estimate on $t_{\mathrm{mix}}(\varepsilon)$ given in (6.15) is off by a factor of two, as we will see in Section 18.2.2.

**6.5.3. Top-to-random shuffle.** We revisit the top-to-random shuffle introduced in Section 6.1. As noted in Example 6.9, the time $\tau_{\mathrm{top}}$ is a strong stationary time.

Consider the motion of the original bottom card. When there are $k$ cards beneath it, the chance that it rises one card remains $(k + 1)/n$ until a shuffle puts the top card underneath it. Thus, the distribution of $\tau_{\mathrm{top}}$ is the same as the coupon collector's time. As above for the lazy hypercube walker, combining Proposition 6.11 and Proposition 2.4 yields

$$d(n \log n + \alpha n) \leq e^{-\alpha} \quad \text{for all } n. \tag{6.16}$$

Consequently,

$$t_{\mathrm{mix}}(\varepsilon) \leq n \log n + \log(\varepsilon^{-1})n. \tag{6.17}$$

**6.5.4. The move-to-front chain.** A certain professor owns many books, arranged on his shelves. When he finishes with a book drawn from his collection, he does not waste time re-shelving it in its proper location. Instead, he puts it at the very beginning of his collection, in front of all the shelved books.

If his choice of book is random, this is an example of the ***move-to-front*** chain. Any setting where items are stored in a stack, removed at random locations, and placed on the top of the stack can be modeled by the move-to-front chain.

### PDF page 99 (book page 83)

*[Figure: A pen-and-ink line drawing of a bespectacled professor wearing suspenders, standing at a bookshelf and pulling out a book with one raised hand. On top of the shelf sit a playing card, dice, a Rubik's cube, tangled rings, and a steaming mug labeled "MSRI." A small bird perches on a windowsill to the left; a cat lies curled on the lower shelf. A box on a middle shelf bears handwritten labels.]*

Drawing by Yelena Shvets

**FIGURE 6.3.** The move-to-front rule in action.

Let $P$ be the transition matrix (on permutations of $\{1, 2, \ldots, n\}$) corresponding to this method of rearranging elements.

The time reversal $\widehat{P}$ of the move-to-front chain is the top-to-random shuffle, as intuition would expect. It is clear from the definition that for every permissible transition $\sigma_1 \to \sigma_2$ for move-to-front, the transition $\sigma_2 \to \sigma_1$ is permissible for top-to-random, and both have probability $n^{-1}$.

By Lemma 4.13, the mixing time for move-to-front will be identical to that of the top-to-random shuffle. Consequently, the mixing time for move-to-front is not more than $n \log n - \log(\varepsilon)n$.

**6.5.5. Lazy random walk on cycle.** Here is a recursive description of a strong stationary time $\tau_k$ for lazy random walk $(X_t)$ on a cycle $\mathbb{Z}_n$ with $n = 2^k$ points.

For $k = 1$, waiting one step will do: $\tau_1 = 1$ with mean $m_1 = 1$. Suppose we have constructed $\tau_k$ already and are now given a cycle with $2^{k+1}$ points. Set $T_0 = 0$ and define $T_1 = t_1$ as the time it takes the lazy walk to make two $\pm 1$ steps. Then $T_1$ is a sum of two geometric$(1/2)$ random variables and thus has mean 4. Given $T_1, \ldots, T_j$, define $t_{j+1}$ as the time it takes the lazy random walk to make

### PDF page 100 (book page 84)

two steps of $\pm 1$ after time $T_j$ and let $T_{j+1} = T_j + t_{j+1}$. Observe that the process $(X_{T_j})$ for $j \geq 0$ is lazy random walk on the even points of the cycle. Therefore at time $T_{\tau_k}$ the location of $X_{T_{\tau_k}}$ is uniform among the even points on the $2^{k+1}$-cycle, even if we condition on the value of $T_{\tau_k}$. It follows that $\tau_{k+1} = T_{\tau_k} + 1$ is a strong stationary time for the lazy random walk on the $2^{k+1}$-cycle. Exercise 6.9 completes the discussion by showing that $\mathbf{E}\tau_k = (4^k - 1)/3$.

**6.6. Stationary Times and Cesaro Mixing Time**

We have seen that *strong* stationary times fit naturally with separation distance and can be used to bound the mixing time. Next, we show that stationary times fit naturally with an alternative definition of mixing time.

Consider a finite chain $(X_t)$ with transition matrix $P$ and stationary distribution $\pi$ on $\mathcal{X}$. Given $t \geq 1$, suppose that we choose uniformly a time $\sigma \in \{1, 2, \ldots, t\}$, and run the Markov chain for $\sigma$ steps. Then the state $X_\sigma$ has distribution

$$ \nu_x^t := \frac{1}{t} \sum_{s=1}^{t} P^s(x, \cdot). \tag{6.18} $$

The **Cesaro mixing time** $t_{\text{Ces}}(\varepsilon)$ is defined as the first $t$ such that for all $x \in \mathcal{X}$,

$$ \|\nu_x^t - \pi\|_{\text{TV}} \leq \varepsilon \,. $$

Exercise 6.11 shows that

$$ t_{\text{Ces}}(1/4) \leq 7 t_{\text{mix}} \,. $$

The following general result due to **Lovász and Winkler (1998)** shows that the expectation of every stationary time yields an upper bound for $t_{\text{Ces}}(1/4)$. Remarkably, this does not need reversibility or laziness. For reversible chains, the converse is proved in Proposition 24.8.

THEOREM 6.19. *Consider a finite chain with transition matrix $P$ and stationary distribution $\pi$ on $\mathcal{X}$. If $\tau$ is a stationary time for the chain, then $t_{\text{Ces}}(1/4) \leq 4 \max_{x \in \mathcal{X}} \mathbf{E}_x(\tau) + 1$.*

PROOF. Since $\tau$ is a stationary time, so is $\tau + s$ for every $s \geq 1$. Therefore, for every $y \in \mathcal{X}$,

$$ t\pi(y) = \sum_{s=1}^{t} \mathbf{P}_x \{X_{\tau+s} = y\} = \sum_{\ell=1}^{\infty} \mathbf{P}_x \{X_\ell = y,\, \tau < \ell \leq \tau + t\} \,. $$

Consequently,

$$ t\nu_x^t(y) - t\pi(y) \leq \sum_{\ell=1}^{t} \mathbf{P}_x \{X_\ell = y,\, \tau \geq \ell\} \,. $$

Summing the last inequality over all $y \in \mathcal{X}$ such that the left-hand side is positive,

$$ t\|\nu_x^t - \pi\|_{\text{TV}} \leq \sum_{\ell=1}^{t} \mathbf{P}_x \{\tau \geq \ell\} \leq \mathbf{E}_x (\tau) \,. $$

Thus for $t \geq 4\mathbf{E}_x(\tau)$ we have $\|\nu_x^t - \pi\|_{\text{TV}} \leq 1/4$. $\blacksquare$

### PDF page 101 (book page 85)

REMARK 6.20. Note that if we choose a state $\xi$ according to $\pi$, and then let $\tau$ be the first hitting time of $\xi$, then $X_\tau = \xi$, whence $\tau$ is a stationary time. But then

$$ \mathbf{E}_x(\tau) \leq \max_y \mathbf{E}_x \tau_y \quad \text{ for all } x \,. $$

The quantity $\max_{x,y} \mathbf{E}_x \tau_y$ is denoted by $t_{\text{hit}}$, and is discussed in Chapter 10. In particular, combining this with Theorem 6.19 shows that

$$ t_{\text{Ces}}(1/4) \leq 4 t_{\text{hit}} + 1 \,. \tag{6.19} $$

We return to $t_{\text{Ces}}$ and its connection to other mixing parameters in Chapter 24.

**6.7. Optimal Strong Stationary Times\***

Consider an irreducible and aperiodic Markov chain $(X_t)$.

PROPOSITION 6.21. *For every starting state $x$, there exists a strong stationary time $\tau$ such that, for all $t \geq 0$,*

$$ s_x(t) = \mathbf{P}_x\{\tau > t\} \,. \tag{6.20} $$

PROOF. Fix $x \in \mathcal{X}$, and let $a_t := \min_y \frac{P^t(x,y)}{\pi(y)} = 1 - s_x(t)$. Note that $a_t$ is non-decreasing. (See Exercise 6.4.) If there exists a strong stationary time $\tau$ satisfying (6.20), then $\mathbf{P}_x\{\tau = t\} = a_t - a_{t-1}$ and

$$ \mathbf{P}_x\{X_t = y,\, \tau = t\} = \pi(y)(a_t - a_{t-1}) \quad \text{ for all } t \geq 0,\, y \in \mathcal{X} \,. \tag{6.21} $$

Likewise, by (6.4), if (6.21) holds, then

$$ \mathbf{P}_x\{X_t = y,\, \tau \leq t\} = \pi(y)a_t \quad \text{ for all } t \geq 0,\, y \in \mathcal{X} \,. \tag{6.22} $$

Since

$$ \begin{aligned} \mathbf{P}_x\{X_t = y,\, \tau = t\} \\ = \mathbf{P}_x\{\tau = t \mid X_t = y,\, \tau > t-1\}\mathbf{P}_x\{X_t = y,\, \tau > t-1\} \\ = \mathbf{P}_x\{\tau = t \mid X_t = y,\, \tau > t-1\} \left( P^t(x,y) - \mathbf{P}_x\{X_t = y,\, \tau \leq t-1\} \right) \,, \end{aligned} \tag{6.23} $$

if the optimal $\tau$ exists (so that (6.21) and (6.22) are satisfied), then

$$ \mathbf{P}_x\{\tau = t \mid X_t = y,\, \tau > t-1\} = \frac{a_t - a_{t-1}}{P^t(x,y)/\pi(y) - a_{t-1}} \,. \tag{6.24} $$

The quantity on the right is in $[0,1]$ since $a_t$ is non-decreasing and $a_t \leq P^t(x,y)/\pi(y)$. To construct $\tau$ which satisfies (6.24), let $U_1, U_2, \ldots$ be i.i.d. Uniform$[0,1]$ random variables independent of $(X_t)$, and define

$$ \tau = \min\Big\{t \geq 1 \,:\, U_t \leq \frac{a_t - a_{t-1}}{P^t(x, X_t)/\pi(X_t) - a_{t-1}}\Big\} \,. $$

Clearly (6.24) holds. We now show the equality (6.21) holds by induction. The case $t = 1$ is immediate. For the induction step, assume that (6.21) holds with $s$ replacing $t$ for all $s < t$. The proof of (6.4) shows that

$$ \mathbf{P}_x\{X_t = y,\, \tau \leq t-1\} = \pi(y)a_{t-1} \,. $$

Equation (6.23) yields the induction step and then proves (6.21). Summing (6.22) over $y$ shows that $\mathbf{P}_x\{\tau \leq t\} = a_t$ for all $t$. Consequently, (6.20) holds. In particular, $\mathbf{P}_x\{\tau < \infty\} = 1$, since $a_t \to 1$ for an aperiodic and irreducible chain. The strong stationarity of $\tau$ follows from (6.21). $\blacksquare$

### PDF page 102 (book page 86)

**Exercises**

EXERCISE 6.1. Show that if $\tau$ and $\tau'$ are stopping times for the filtration $\{\mathcal{F}_t\}$, then $\tau + \tau'$ is a stopping time for $\{\mathcal{F}_t\}$. In particular, if $r$ is a non-random and non-negative integer and $\tau$ is a stopping time, then $\tau + r$ is a stopping time.

EXERCISE 6.2. Consider the top-to-random shuffle. Show that the time until the card initially one card from the bottom rises to the top, plus one more move, is a strong stationary time, and find its expectation.

EXERCISE 6.3. Show that for the Markov chain on two complete graphs in Section 6.5.1, the stationary distribution is uniform on all $2n - 1$ vertices.

EXERCISE 6.4. Let $s(t)$ be defined as in (6.7).
(a) Show that for each $t \geq 1$ there is a stochastic matrix $Q_t$ so that $P^t(x, \cdot) = [1 - s_x(t)]\,\pi + s_x(t)Q_t(x, \cdot)$ and $\pi = \pi Q_t$.
(b) Using the representation in (a), show that

$$ P^{t+u}(x, y) = [1 - s_x s(t)s(u)]\,\pi(y) + s_x(t)s(u) \sum_{z \in \mathcal{X}} Q_t(x, z)Q_u(z, y). \tag{6.25} $$

(c) Using (6.25), establish that $s_x(t + u) \leq s_x(t)s(u)$ and deduce that $s$ is submultiplicative, i.e., $s(t + u) \leq s(t)s(u)$.
(d) Deduce that $s_x(t)$ is weakly decreasing in $t$.

EXERCISE 6.5. For the lazy random walk on the $n$-vertex complete graph, show that $t_{\text{mix}}^{(\infty)} \asymp \log n$, yet the separation distance satisfies $s(2) \leq \frac{1}{4}$.

EXERCISE 6.6. Suppose that for every $x \in \mathcal{X}$ there is a strong stationary time $\tau$ starting from $x$ such that $\mathbf{P}_x\{\tau > t_0\} \leq \varepsilon$. Show that $d(t) \leq \varepsilon^{\lfloor t/t_0 \rfloor}$.

EXERCISE 6.7 (Wald's Identity). Let $(Y_t)$ be a sequence of independent and identically distributed random variables such that $\mathbf{E}(|Y_t|) < \infty$.
(a) Show that if $\tau$ is a random time so that the event $\{\tau \geq t\}$ is independent of $Y_t$ for all $t$ and $\mathbf{E}(\tau) < \infty$, then

$$ \mathbf{E}\left(\sum_{t=1}^{\tau} Y_t\right) = \mathbf{E}(\tau)\mathbf{E}(Y_1). \tag{6.26} $$

*Hint*: Write $\sum_{t=1}^{\tau} Y_t = \sum_{t=1}^{\infty} Y_t \mathbf{1}_{\{\tau \geq t\}}$. First consider the case where $Y_t \geq 0$.
(b) Let $\tau$ be a stopping time for the sequence $(Y_t)$. Show that $\{\tau \geq t\}$ is independent of $Y_t$, so (6.26) holds provided that $\mathbf{E}(\tau) < \infty$.

EXERCISE 6.8. Consider the Markov chain of Section 6.5.1 defined on two glued complete graphs. By considering the set $A \subset \mathcal{X}$ of all vertices in one of the two complete graphs, show that $t_{\text{mix}} \geq (n/2)\,[1 + o(1)]$.

EXERCISE 6.9. Let $\tau_k$ be the stopping time constructed in Section 6.5.5, and let $m_k = \mathbf{E}(\tau_k)$. Show that $m_{k+1} = 4m_k + 1$, so that $m_k = \sum_{i=0}^{k-1} 4^i = (4^k - 1)/3$.

EXERCISE 6.10. For a graph $G$, let $W$ be the (random) vertex occupied at the first time the random walk has visited every vertex. That is, $W$ is the last new vertex to be visited by the random walk. Prove the following remarkable fact: for random walk on an $n$-cycle, $W$ is uniformly distributed over all vertices different from the starting vertex.

### PDF page 103 (book page 87)

REMARK 6.22. **Lovász and Winkler (1993)** prove that if a graph $G$ has the property that, for every starting state $x$, the last vertex to be reached is uniformly distributed over the vertices of $G$ other than $x$, then $G$ is either a cycle or a complete graph.

EXERCISE 6.11. Show that $t_{\mathrm{Ces}}(1/4) \leq 7 t_{\mathrm{mix}}$.

**Notes**

Strong stationary times were introduced by Aldous and Diaconis (**1986**, **1987**). An important class of strong stationary times was constructed by **Diaconis and Fill (1990)**. The thesis of **Pak (1997)** has many examples of strong stationary times.

The inequality (6.12) was proven in **Aldous and Diaconis (1987)**.

**Lovász and Winkler (1995b**, Theorem 5.1) showed that a stationary time has minimal expectation among all stationary times if and only if it has a halting state. (See also **Lovász and Winkler (1998)**.)

Section 6.7 comes from **Aldous and Diaconis (1987)**.

The strong stationary time we give for the cycle in Section 6.5.5 is due to **Diaconis and Fill (1990)**, although the exposition is different. The idea goes back to the construction of a Skorokhod embedding due to **Dubins (1968)**.

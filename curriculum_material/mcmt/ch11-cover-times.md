# Chapter 11 — Cover Times
*(PDF pages 166–176; book pages 150–160)*

### PDF page 166 (book page 150)

CHAPTER 11

# Chapter 11 — Cover Times

**11.1. Definitions**

Let $(X_t)$ be a finite Markov chain with state space $\mathcal{X}$. The ***cover time variable*** $\tau_{\mathrm{cov}}$ of $(X_t)$ is the first time at which all the states have been visited. More formally, $\tau_{\mathrm{cov}}$ is the minimal value such that, for every state $y \in \mathcal{X}$, there exists $t \leq \tau_{\mathrm{cov}}$ with $X_t = y$.

We also define the ***cover time*** as the mean of $\tau_{\mathrm{cov}}$ from the worst-case initial state:
$$ t_{\mathrm{cov}} = \max_{x \in \mathcal{X}} \mathbf{E}_x \tau_{\mathrm{cov}}. \tag{11.1} $$

Cover times have been studied extensively by computer scientists. For example, random walks can be used to verify the connectivity of a network, and the cover time provides an estimate of the running time.

EXAMPLE 11.1 (Cover time of cycle). **Lovász (1993**) gives an elegant computation of the cover time $t_{\mathrm{cov}}$ of simple random walk on the $n$-cycle. This walk is simply the remainder modulo $n$ of a simple random walk on $\mathbb{Z}$. The walk on the remainders has covered all $n$ states exactly when the walk on $\mathbb{Z}$ has first visited $n$ distinct states.

Let $c_n$ be the expected value of the time when a simple random walk on $\mathbb{Z}$ has first visited $n$ distinct states, and consider a walk which has just reached its $(n-1)$-st new state. The visited states form a subsegment of the number line and the walk must be at one end of that segment. Reaching the $n$-th new state is now a gambler's ruin situation: the walker's position corresponds to a fortune of 1 (or $n-1$), and we are waiting for her to reach either 0 or $n$. Either way, the expected time is $(1)(n-1) = n-1$, as shown in Exercise 2.1. It follows that
$$ c_n = c_{n-1} + (n-1) \quad \text{for} \quad n \geq 1. $$
Since $c_1 = 0$ (the first state visited is $X_0 = 0$), we have $c_n = n(n-1)/2$.

**11.2. The Matthews Method**

Fix an irreducible chain with state space $\mathcal{X}$. Recall the definition (10.6) of $t_{\mathrm{hit}}$, and let $x, y \in \mathcal{X}$ be states for which $t_{\mathrm{hit}} = \mathbf{E}_x \tau_y$. Since any walk started at $x$ must have visited $y$ by the time all states are covered, we have
$$ t_{\mathrm{hit}} = \mathbf{E}_x \tau_y \leq \mathbf{E}_x \tau_{\mathrm{cov}} \leq t_{\mathrm{cov}}. \tag{11.2} $$

It is more interesting to give an upper bound on cover times in terms of hitting times. A walk covering all the states can visit them in many different orders, and this indeterminacy can be exploited. Randomizing the order in which we check whether states have been visited (which, following **Aldous and Fill (1999)**, we will call the Matthews method—see **Matthews (1988a)** for the original version)

150

### PDF page 167 (book page 151)

allows us to prove both upper and lower bounds. Despite the simplicity of the arguments, these bounds are often remarkably good.

THEOREM 11.2 (Matthews (**1988a**)). *Let $(X_t)$ be an irreducible finite Markov chain on $n > 1$ states. Then*
$$ t_{\mathrm{cov}} \leq t_{\mathrm{hit}} \left( 1 + \frac{1}{2} + \cdots + \frac{1}{n-1} \right). $$

PROOF. Without loss of generality, we may assume that our state space is $\{1, \ldots, n\}$ and our starting state is $n$. Let $\sigma$ be a uniform random permutation of $\{1, 2, \ldots, n-1\}$, chosen independently of the chain. We will look for states in order $\sigma$. Let $T_k$ be the first time that the states $\sigma(1), \ldots, \sigma(k)$ have all been visited, and let $L_k = X_{T_k}$ be the last state among $\sigma(1), \ldots, \sigma(k)$ to be visited.

For any $1 \leq s \leq n-1$, we have
$$ \mathbf{E}_n(T_1 \mid \sigma(1) = s) = \mathbf{E}_n(\tau_s) \leq t_{\mathrm{hit}}. $$
Averaging over $s$ shows that $\mathbf{E}_x(T_1) \leq t_{\mathrm{hit}}$.

For any choice of distinct $1 \leq r \neq s \leq n-1$, we have
$$ \mathbf{E}_n(T_k - T_{k-1} \mid L_{k-1} = r, \ \sigma(k) = s = L_k) = \mathbf{E}_r(\tau_s) \leq t_{\mathrm{hit}}. $$
Averaging over of $r$ and $s$ yields
$$ \mathbf{E}_n(T_k - T_{k-1} \mid L_k = \sigma(k)) \leq t_{\mathrm{hit}}. $$
Observe that, for any set $S$ of $k$ elements, we have
$$ \mathbf{P}_n\{L_k = \sigma(k) \mid \{\sigma(1), \ldots, \sigma(k)\} = S, \ \{X_t\}_t\} = \frac{1}{k}. \tag{11.3} $$
Consequently, since $\mathbf{E}_n(T_k - T_{k-1} \mid L_k \neq \sigma(k)) = 0$,
$$ \mathbf{E}_n(T_k - T_{k-1}) \leq \mathbf{P}_n\{L_k = \sigma(k)\} \cdot t_{\mathrm{hit}} = \frac{t_{\mathrm{hit}}}{k}. $$
Therefore,
$$ t_{\mathrm{cov}} = \mathbf{E}_n(T_{n-1}) \leq t_{\mathrm{hit}} \sum_{k=1}^{n-1} \frac{1}{k}. $$
$\blacksquare$

EXAMPLE 11.3. For random walk on a complete graph with self-loops, the cover time coincides with the time to obtain a complete collection in the coupon collector's problem. In this case $\mathbf{E}_i(\tau_j) = n$ is constant for $i \neq j$, so the upper bound is tight.

A slight modification of this technique can be used to prove lower bounds: instead of looking for every state along the way to the cover time, we look for the elements of some $A \subseteq \mathcal{X}$. Define $\tau^A_{\mathrm{cov}}$ to be the first time such that every state of $A$ has been visited by the chain. When the elements of $A$ are far away from each other, in the sense that the hitting time between any two of them is large, the time to visit just the elements of $A$ can give a good lower bound on the overall cover time.

PROPOSITION 11.4. *Let $A \subset \mathcal{X}$. Set $t^A_{\min} = \min_{a,b \in A, a \neq b} \mathbf{E}_a(\tau_b)$. Then*
$$ t_{\mathrm{cov}} \geq \max_{A \subseteq \mathcal{X}} t^A_{\min} \left( 1 + \frac{1}{2} + \cdots + \frac{1}{|A|-1} \right). $$

### PDF page 168 (book page 152)

PROOF. Fix an initial state $x \in A$ and let $\sigma$ be a uniform random permutation of the elements of $A$, chosen independently of the chain trajectory. Let $T_k$ be the first time at which all of $\sigma(1), \sigma(2), \ldots, \sigma(k)$ have been visited, and let $L_k = X_{T_k}$.

With probability $1/|A|$ we have $\sigma(1) = x$ and $T_1 = 0$. Otherwise, the walk must proceed from $x$ to $\sigma(1)$. Thus
$$ \mathbf{E}_x(T_1) \geq \frac{1}{|A|} 0 + \frac{|A|-1}{|A|} t^A_{\min} = \left( 1 - \frac{1}{|A|} \right) t^A_{\min}. \tag{11.4} $$
For $2 \leq k \leq |A|$ and $r, s \in A$, as in the proof of the upper bound, we have
$$ \mathbf{E}_x(T_k - T_{k-1} \mid \sigma(k-1) = r \text{ and } \sigma(k) = L_k = s) \geq t^A_{\min}. $$
Averaging over $r$ and $s$ shows that
$$ \mathbf{E}_x(T_k - T_{k-1} \mid L_k = \sigma(k)) \geq t^A_{\min}, $$
and since $\mathbf{E}_x(T_k - T_{k-1} \mid L_k \neq \sigma(k)) = 0$, we deduce (again also using (11.3)) that
$$ \mathbf{E}_x(T_k - T_{k-1}) \geq \frac{1}{k} t^A_{\min}. \tag{11.5} $$
Adding up (11.4) and the bound of (11.5) for $2 \leq k \leq |A|$ gives
$$ \mathbf{E}_x(\tau^A_{\mathrm{cov}}) \geq t^A_{\min} \left( 1 + \frac{1}{2} + \cdots + \frac{1}{|A|-1} \right) $$
(note that the negative portion of the first term cancels with the last term).

Since $t_{\mathrm{cov}} \geq \mathbf{E}_x(\tau_{\mathrm{cov}}) \geq \mathbf{E}_x(\tau^A_{\mathrm{cov}})$ for every $x \in A$, we are done. $\blacksquare$

**11.3. Applications of the Matthews Method**

**11.3.1. Binary trees.** Consider simple random walk on the rooted binary tree with depth $k$ and $n = 2^{k+1} - 1$ vertices, which we first discussed in Section 5.3.4. The commute time between the root $\rho$ and a leaf $a$ is, by Proposition 10.7 (the Commute Time Identity), equal to
$$ t_{\rho \leftrightarrow a} = 2(n-1)k, $$
since the effective resistance between the root and the leaf is $k$, by Example 9.7, and the total conductance $c_G$ of the network is twice the number of edges. The maximal hitting time will be realized by pairs of leaves $a, b$ whose most recent common ancestor is the root (see Exercise 10.4). For such a pair, the hitting time will, by symmetry, be the same as the commute time between the root and one of the leaves, whence
$$ \mathbf{E}_a \tau_b = 2(n-1)k. $$
Hence Theorem 11.2 gives
$$ t_{\mathrm{cov}} \leq 2(n-1)k \left( 1 + \frac{1}{2} + \cdots + \frac{1}{n} \right) = (2 + o(1))(\log 2) n k^2. \tag{11.6} $$

For a lower bound, we need an appropriate set $A \subseteq X$. Fix a level $h$ in the tree, and let $A$ be a set of $2^h$ leaves chosen so that each vertex at level $h$ has a unique descendant in $A$. Notice that the larger $h$ is, the more vertices there are in $A$—and the closer together those vertices can be. We will choose a value of $h$ below to optimize our bound.

For two distinct leaves $a, b$, the hitting time from one to the other is the same as the commute time from their common ancestor to one of them, say $a$. If $a, b \in A$,

### PDF page 169 (book page 153)

then their least common ancestor is at level $h' < h$. Thus, by the Commute Time Identity (Proposition 10.7) and Example 9.7, we have

$$ \mathbf{E}_a \tau_b = 2(n-1)(k-h'), $$

which is clearly minimized when $h' = h - 1$. By Proposition 11.4,

$$ t_{\mathrm{cov}} \geq 2(n-1)(k-h+1)\left(1 + \frac{1}{2} + \cdots + \frac{1}{2^h - 1}\right) $$
$$ = (2 + o(1))(\log 2)n(k-h)h. \tag{11.7} $$

Setting $h = \lfloor k/2 \rfloor$ in (11.7) gives

$$ t_{\mathrm{cov}} \geq \frac{1}{4} \cdot (2 + o(1))(\log 2)nk^2. \tag{11.8} $$

There is still a factor of 4 gap between the upper bound of (11.6) and the lower bound of (11.8). In fact, the upper bound is sharp. See the Notes.

**11.3.2. Tori.** In Section 10.6 we estimated (up to a bounded factor) the hitting times of simple random walks on finite tori of various dimensions. These bounds can be combined with Matthews' method to bound the cover time. We discuss the case of dimension at least 3 first, since the details are a bit simpler.

When the dimension $d \geq 3$, Proposition 10.21 tells us that there exist constants $c_d$ and $C_d$ such that for any distinct vertices $x, y$ of $\mathbb{Z}_n^d$,

$$ c_d n^d \leq \mathbf{E}_x(\tau_y) \leq C_d n^d. $$

By Theorem 11.2, the cover time satisfies

$$ t_{\mathrm{cov}} \leq C_d n^d \left(1 + \frac{1}{2} + \cdots + \frac{1}{n^d}\right) \tag{11.9} $$

$$ = C_d d n^d \log n (1 + o(1)). \tag{11.10} $$

To derive an almost-matching lower bound from Proposition 11.4, we take $A$ to be $\mathbb{Z}_n^d$, and obtain

$$ t_{\mathrm{cov}} \geq t_{\min}^A \left(1 + \frac{1}{2} + \cdots + \frac{1}{|A| - 1}\right) $$
$$ \geq c_d d n^d \log n (1 + o(1)), $$

which is only a constant factor away from our upper bound.

In dimension 2, Proposition 10.21 says that when $x$ and $y$ are vertices of $\mathbb{Z}_n^2$ at distance $k$,

$$ c_2 n^2 \log(k) \leq \mathbf{E}_x(\tau_y) \leq C_2 n^2 \log(k + 1). $$

In this case the Matthews upper bound gives

$$ \mathbf{E}(\tau_{\mathrm{cov}}) \leq 2C_2 n^2 (\log n)^2 (1 + o(1)), \tag{11.11} $$

since the furthest apart two points can be is $n$.

To get a good lower bound, we must choose a set $A$ which is as large as possible, but for which the minimum distance between points is also large. Let $A$ be the

### PDF page 170 (book page 154)

**FIGURE 11.1.** Black squares show the states unvisited by a single trajectory of simple random walk on a $75 \times 75$ torus. This trajectory took 145,404 steps to cover. The diagrams show the walk after 10%, 20%, ..., 100% of its cover time.

*[Figure: a 2×5 grid of ten small square panels, each showing the states of a 75×75 torus not yet visited by a single random walk, plotted as black squares on white. The panels correspond to 10%, 20%, ..., 100% of the cover time. In the first panel a large connected black region fills much of the square; across successive panels the black region shrinks and fragments, until in the last few panels only a handful of scattered isolated black dots remain, and the final panel is essentially empty.]*

set of all points in $Z_n^2$ both of whose coordinates are multiples of $\lfloor \sqrt{n} \rfloor$. Then Proposition 11.4 and Proposition 10.21 imply

$$ \mathbf{E}(\tau_{\mathrm{cov}}) \geq c_2 n^2 \log(\lfloor \sqrt{n} \rfloor)\left(1 + \frac{1}{2} + \cdots + \frac{1}{|A| - 1}\right) $$
$$ = \frac{c_2}{2} n^2 (\log n)^2 (1 + o(1)). $$

Figure 11.1 shows the points of a $75 \times 75$ torus left uncovered by a single random walk trajectory at equally spaced fractions of its cover time.

Exercises 11.4 and 11.5 use improved estimates on the hitting times to get our upper and lower bounds for cover times on tori even closer together.

**11.4. Spanning Tree Bound for Cover Time**

A ***depth-first search*** (DFS) of a tree $T$ is defined inductively as follows: For a tree with single node $v_0$, the DFS is simply $v_0$. Now suppose that $T$ is a tree of depth $n \geq 1$ and root $v_0$, and that the DFS of a tree of depth $n - 1$ is defined. Let $v_1, \ldots, v_m$ be the children of the root. Since, for each $k = 1, \ldots, m$, the subtree rooted at $v_k$ is of depth at most $n - 1$, the depth-first search of that tree is defined; denote it by $\Gamma_k$. The DFS of $T$ is defined to be the path $v_0, \Gamma_1, v_0, \Gamma_2, \ldots, v_0, \Gamma_m, v_0$.

THEOREM 11.5. *Let $T$ be a spanning tree of a graph $G$, and identify $T$ with its edge set. The cover time for a random walk on a graph $G$ satisfies*

$$ t_{\mathrm{cov}} \leq 2|E| \sum_{(x,y) \in T} \mathcal{R}(x \leftrightarrow y) \leq 2(n-1)|E|. \tag{11.12} $$

PROOF. Let $x_0, x_1, \ldots, x_{2n-2}$ be a depth-first search of $T$. Then

$$ t_{\mathrm{cov}} \leq \sum_{i=1}^{2n-2} \mathbf{E}_{x_{i-1}} \tau_{x_i}, \tag{11.13} $$

where the expected hitting time is for the random walk on the original graph $G$. Since each edge $e$ of $T$ is traversed once in each direction, from (11.13) and the

### PDF page 171 (book page 155)

Commute Time Identity (Proposition 10.7) we obtain

$$ t_{\mathrm{cov}} \leq \sum_{(x,y) \in T} t_{x \leftrightarrow y} = 2 \sum_{(x,y) \in T} \mathcal{R}(x \leftrightarrow y)|E|. \tag{11.14} $$

Since $\mathcal{R}(x \leftrightarrow y) \leq 1$ for $x \sim y$, and there are $n - 1$ edges in $T$, (11.14) yields (11.12). $\blacksquare$

We give a general bound on the cover time for $d$-regular graphs which uses Theorem 11.5:

THEOREM 11.6. *For simple random walk on a $d$-regular graph $G$ with $n$ vertices, the cover time satisfies*

$$ t_{\mathrm{cov}} \leq 3n^2. $$

PROOF. For an edge $e = \{x, y\}$, identify (glue together) all vertices different from $x$ and $y$ into a single vertex $z$, as illustrated in Figure 11.2. In the resulting graph, $x$ and $y$ are connected in parallel by $e$ and a path through $z$ of conductance $(d-1)/2$, whence the effective conductance between $x$ and $y$ (in the glued graph) is $(d+1)/2$. By Rayleigh's Monotonicity Law (Theorem 9.12),

$$ \mathcal{R}(x \leftrightarrow y) \geq \mathcal{R}^{\mathrm{Glued}}(x \leftrightarrow y) = \frac{2}{d+1}. $$

**FIGURE 11.2.** Graph after glueing together all vertices different from $x$ and $y$, where $d = 4$.

*[Figure: three filled black vertices — $x$ at upper left, $y$ at upper right, and $z$ at the bottom center. A single edge connects $x$ directly to $y$ across the top. Multiple parallel curved edges connect $x$ down to $z$ and $z$ up to $y$, illustrating the path through $z$.]*

Let $T$ be any spanning tree of $G$. Since there are $nd/2$ edges in $G$, there are $nd/2 - (n-1)$ edges not in $T$, and

$$ \sum_{e \notin T} \mathcal{R}(e) \geq \frac{2}{d+1}\left(\frac{nd}{2} - (n-1)\right). $$

By Foster's Identity ($\sum_{e \in G} \mathcal{R}(e) = (n-1)$, see Exercise 10.20),

$$ \sum_{e \in T} \mathcal{R}(e) \leq (n-1) - \frac{2}{d+1}\left(\frac{nd}{2} - (n-1)\right) \leq \frac{3(n-1)}{d+1}. $$

Finally, applying Theorem 11.5 shows that

$$ t_{\mathrm{cov}} \leq nd \cdot \frac{3n}{d} = 3n^2. $$

$\blacksquare$

### PDF page 172 (book page 156)

**11.5. Waiting for all patterns in coin tossing**

In Section 17.3.2, we will use elementary martingale methods to compute the expected time to the first occurrence of a specified pattern (such as $HTHHTTH$) in a sequence of independent fair coin tosses. Here we examine the time required for *all* $2^k$ patterns of length $k$ to have appeared. In order to apply the Matthews method, we first give a simple universal bound on the expected hitting time of any pattern.

Consider the Markov chain whose state space is the collection $\mathcal{X} = \{0,1\}^k$ of binary $k$-tuples and whose transitions are as follows: at each step, delete the leftmost bit and append on the right a new fair random bit independent of all earlier bits. We can also view this chain as sliding a window of width $k$ from left to right along a stream of independent fair bits. (In fact, the winning streak chain of Section 5.3.5 is a lumping of this chain—see Lemma 2.5.) We call this the **shift chain on binary $k$-tuples**.

In the coin tossing picture, it is natural to consider the *waiting time* $w_x$ for a pattern $x \in \{0,1\}^k$, which is defined to be the number of steps required for $x$ to appear using all "new" bits—that is, without any overlap with the initial state. Note that

$$ w_x \geq k \quad \text{and} \quad w_x \geq \tau_x \quad \text{for all } x \in \{0,1\}^k. \tag{11.15} $$

Also, $w_x$ does not depend on the initial state of the chain. Hence

$$ \mathbf{E}w_x \geq \mathbf{E}_x \tau_x^+ = 2^k \tag{11.16} $$

(the last equality follows immediately from (1.28), since our chain has a uniform stationary distribution).

LEMMA 11.7. *Fix $k \geq 1$. For the shift chain on binary $k$-tuples,*

$$ H_k := \max_{x \in \{0,1\}^k} \mathbf{E}w_x = 2^{k+1} - 2. $$

PROOF. When $k = 1$, $w_x$ is geometric with parameter 2. Hence $H_1 = 2$.

Now fix a pattern $x$ of length $k + 1$ and let $x^-$ be the pattern consisting of the first $k$ bits of $x$. To arrive at $x$, we must first build up $x^-$. Flipping one more coin has probability $1/2$ of completing pattern $x$. If it does not, we resume waiting for $x$. The additional time required is certainly bounded by the time required to construct $x$ from entirely new bits. Hence

$$ \mathbf{E}w_x \leq \mathbf{E}w_{x^-} + 1 + \frac{1}{2}\mathbf{E}w_x. \tag{11.17} $$

To bound $H_{k+1}$ in terms of $H_k$, choose an $x$ that achieves $H_{k+1} = \mathbf{E}w_x$. On the right-hand-side of (11.17), the first term is bounded by $H_k$, while the third is equal to $(1/2)H_{k+1}$. We conclude that

$$ H_{k+1} \leq H_k + 1 + \frac{1}{2}H_{k+1}, $$

which can be rewritten as

$$ H_{k+1} \leq 2H_k + 2. $$

This recursion, together with the initial condition $H_1 = 2$, implies $H_k \leq 2^{k+1} - 2$.

When $x$ is a constant pattern (all 0's or all 1's) of length $k$ and $y$ is any pattern ending in the opposite bit, we have $\mathbf{E}_y \tau_x = H_k = 2^{k+1} - 2$. Indeed, since one inappropriate bit requires a copy of $x$ to be built from new bits, equality of hitting time and waiting time holds throughout the induction above. $\blacksquare$

### PDF page 173 (book page 157)

We can now combine Lemma 11.7 with (11.15) and the Matthews upper bound of Theorem 11.2, obtaining

$$ \mathbf{E}_x(\tau_{\mathrm{cov}}) \leq H_k \left(1 + \frac{1}{2} + \cdots + \frac{1}{2^k}\right) = (\log 2)k2^{k+1}(1 + o(1)). \tag{11.18} $$

Looking more closely at the relationship between hitting times and waiting times will allow us to improve this upper bound by a factor of 2 and to prove a matching lower bound, which we leave to the Notes.

LEMMA 11.8. *Let $\theta = \theta_{a,b} = \mathbf{P}_a(\tau_b^+ < k)$. Then for any $a, b \in \{0,1\}^k$ we have*

$$ \mathbf{E}w_b \leq \frac{\mathbf{E}_a \tau_b^+ + k\theta}{1 - \theta}. $$

PROOF. The following inequality is true:

$$ w_b \leq \tau_b^+ + \mathbf{1}_{\{\tau_b^+ < k\}}(k + w_b^*), \tag{11.19} $$

where $w_b^*$ is the amount of time required to build $b$ with all new bits, starting after the $k$-th bit has been added. (Note that $w_b^*$ has the same distribution as $w_b$.) Indeed, if $\tau_b^+ \geq k$, then $w_b = \tau_b^+$. If $\tau_b^+ < k$, then we wait for a new copy of $b$ that begins after the first $k$ bits.

Since $w_b^*$ is independent of the event $\{\tau_b^+ < k\}$, taking expectations on both sides of (11.19) yields

$$ \mathbf{E}w_b \leq \mathbf{E}_a \tau_b^+ + \theta(k + \mathbf{E}w_b) $$

(since $\mathbf{E}_a w_b$ does not depend on the initial state $a$, we drop the subscript), and rearranging terms completes the proof. $\blacksquare$

PROPOSITION 11.9. *The cover time satisfies*

$$ t_{\mathrm{cov}} \geq (\log 2)k2^k(1 + o(1)). $$

PROOF. Fix $j = \lceil \log_2 k \rceil$ and let $A \subseteq \{0,1\}^k$ consist of those bitstrings that end with $j$ zeroes followed by a 1. Fix $a, b \in A$, where $a \neq b$. By Lemma 11.8, we have

$$ \mathbf{E}_a \tau_b^+ \geq (1 - \theta)\mathbf{E}w_b - k\theta, \tag{11.20} $$

where our choice of $A$ ensures

$$ \theta = \mathbf{P}_a(\tau_b^+ < k) \leq 2^{-(j+1)} + \cdots + 2^{-(k-1)} < 2^{-j} \leq \frac{1}{k}. $$

By (11.16) and (11.20) we infer that

$$ \mathbf{E}_a \tau_b^+ \geq 2^k(1 + o(1)). $$

Now apply Proposition 11.4. Since $|A| = 2^{k-j-1}$, we conclude that

$$ t_{\mathrm{cov}} \geq (k - j - 1)(\log 2)2^k(1 + o(1)) = (\log 2)k2^k(1 + o(1)). $$

$\blacksquare$

### PDF page 174 (book page 158)

**Exercises**

EXERCISE 11.1. Let $Y$ be a random variable on some probability space, and let $B = \bigcup_j B_j$ be a partition of an event $B$ into (finitely or countably many) disjoint subevents $B_j$.

(a) Prove that when $\mathbf{E}(Y \mid B_j) \leq M$ for every $j$, then $\mathbf{E}(Y \mid B) \leq M$.
(b) Give an example to show that the conclusion of part (a) can fail when the events $B_j$ are not disjoint.

EXERCISE 11.2. What upper and lower bounds does the Matthews method give for the cycle $\mathbb{Z}_n$? Compare to the actual value, computed in Example 11.1, and explain why the Matthews method gives a poor result for this family of chains.

EXERCISE 11.3. Show that the cover time of the $m$-dimensional hypercube is asymptotic to $m2^m \log(2)$ as $m \to \infty$.

EXERCISE 11.4. In this exercise, we demonstrate that for tori of dimension $d \geq 3$, just a little more information on the hitting times suffices to prove a matching lower bound.

(a) Show that when a sequence of pairs of points $x_n, y_n \in \mathbb{Z}_n^d$ has the property that the distance between them tends to infinity with $n$, then the upper-bound constant $C_d$ of (10.28) can be chosen so that $\mathbf{E}_{x_n}(\tau_{y_n})/n^d \to C_d$.
(b) Give a lower bound on $t_{\mathrm{cov}}$ that has the same initial constant as the upper bound of (11.9).

EXERCISE 11.5. Following the example of Exercise 11.4, derive a lower bound for $\mathbf{E}(\tau_{\mathrm{cov}})$ on the two-dimensional torus that is within a factor of 4 of the upper bound (11.11).

EXERCISE 11.6. Given an irreducible Markov chain $(X_t)_{t \geq 1}$, show that $\mathbf{E}_x(\tau_{\mathrm{cov}})$ can be determined by solving a system of linear equation in at most $n2^n$ variables.

*Hint:* Consider the process $(R_t, X_t)_{t \geq 1}$, where $R_t$ is the set $\{X_0, \ldots, X_t\}$, and use Exercise 10.22.

EXERCISE 11.7. Consider an irreducible finite Markov chain on state space $\mathcal{X}$ with transition matrix $P$, and let $\tau_{\mathrm{cov}}$ be its cover time. Let $t_m$ have the following property: for any $x \in \mathcal{X}$,

$$ \mathbf{P}_x\{\tau_{\mathrm{cov}} \leq t_m\} \geq 1/2. $$

Show that $t_{\mathrm{cov}} \leq 2t_m$.

**Notes**

The Matthews method first appeared in **Matthews (1988a)**. **Matthews (1989)** looked at the cover time of the hypercube, which appears in Exercise 11.3.

The argument we give for a lower bound on the cover time of the binary tree is due to **Zuckerman (1992)**. **Aldous (1991a)** shows that the upper bound is asymptotically sharp; **Peres (2002)** presents a simpler version of the argument.

In the *American Mathematical Monthly*, **Wilf (1989)** described his surprise at the time required for a simulated random walker to visit every pixel of his computer screen. This time is, of course, the cover time for the two-dimensional finite torus. The exact asymptotics of the cover time on $Z_n^2$ have been determined.

### PDF page 175 (book page 159)

Zuckerman (1992) estimated the cover time to within a constant, while Dembo, Peres, Rosen, and Zeitouni (2004) showed that

$$ \mathbf{E}(\tau_{\mathrm{cov}}) \sim \frac{4}{\pi} n^2 (\log n)^2. $$

For more on waiting times for patterns in coin tossing, see Section 17.3.2. Móri (1987) found the cover time for all patterns of length $k$ using ideas from Aldous (1983a). The collection Godbole and Papastavridis (1994) has many further papers on this topic. A single issue of the *Journal of Theoretical Probability* contained several papers on cover times: these include Aldous (1989a), Aldous (1989b), Broder and Karlin (1989), Kahn, Linial, Nisan, and Saks (1989), and Zuckerman (1989).

Aldous (1991b) gives a condition guaranteeing that the cover time variable is well-approximated by its mean. See Theorem 19.6 for a statement.

Theorem 11.5 is due to Aleliunas, Karp, Lipton, Lovász, and Rackoff (1979). Kahn, Linial, Nisan, and Saks (1989) proved an upper bound of $4n^2$ on the cover time of a regular graph with $n$ vertices. This was improved to $3n^2$ by Coppersmith, Feige, and Shearer (1996), and $2n^2$ by Feige (1997).

Feige (1995a) proved a $[1 + o(1)]n \log n$ lower bound on the cover time of an $n$-vertex graph. This was conjectured by Aldous and others, since the complete graph on $n$ vertices has $t_{\mathrm{cov}} = [1 + o(1)]n \log n$. Feige (1995a) proved the upper bound $t_{\mathrm{cov}} \leq [\frac{4}{27} + o(1)]n^3$ on all $n$-vertex graphs, as also conjectured by Aldous. This bound is tight for the "lollipop graph", the graph consisting of a path of length $n/3$ connected to a clique of size $2n/3$.

Barnes and Feige (1996) proved a conjecture of Linial that the $k$-*exploration time*, the expected time to visit $k$ distinct vertices, is at most $O(k^3)$ in any connected graph with at least $k$ vertices. Boczkowski, Peres, and Sousi (2016) proved similar bounds for cover time and exploration times in Eulerian directed graphs.

**Computing the cover time.** As shown in Exercise 11.6, $t_{\mathrm{cov}}$ can be found exactly by solving exponentially many (in $n$) linear equations. Open Problem 35 of Aldous and Fill (1999) asks if $t_{\mathrm{cov}}$ can be deterministically calculated in polynomial time. Matthews' upper bound (which can be determined in polynomial time) estimates $t_{\mathrm{cov}}$ up to a factor of $\log n$. Kahn, Kim, Lovász, and Vu (2000) found a polynomially computable lower bound (based on Matthews' lower bound) which estimates $t_{\mathrm{cov}}$ up to a factor of $O((\log \log n)^2)$. Ding, Lee, and Peres (2012) found a polynomially computable quantity (related to the Gaussian free field) which estimates $t_{\mathrm{cov}}$ up to $O(1)$.

**Complement.** We can improve the upper bound in (11.18) (on the waiting time to see all binary words of length $k$) to match the lower bound in Proposition 11.9.

We apply a variant on the Matthews method which, at first glance, may seem unlikely to help. For any $B \subseteq \mathcal{X}$, the argument for the Matthews bound immediately gives

$$ \mathbf{E}_x \tau_{\mathrm{cov}}^B \leq \max_{b, b' \in B} \mathbf{E}_b \tau_b' \left( 1 + \frac{1}{2} + \cdots + \frac{1}{|B|} \right). \tag{11.21} $$

### PDF page 176 (book page 160)

Certainly the total cover time $\tau_{\mathrm{cov}}$ is bounded by the time taken to visit first all the states in $B$ and then all the states in $B^c$. Hence

$$ \mathbf{E}_x \tau_{\mathrm{cov}} \leq \mathbf{E}_x \tau_{\mathrm{cov}}^B + \max_{y \in \mathcal{X}} \mathbf{E}_y \tau_{\mathrm{cov}}^{B^c}. \tag{11.22} $$

If the states that take a long time to hit form a small fraction of $\mathcal{X}$, then separating those states from the rest can yield a better bound on $t_{\mathrm{cov}}$ than direct application of Theorem 11.2. For the current example of waiting for all possible patterns in coin tossing, we improve the bound by a factor of 2—obtaining an asymptotic match with the lower bound of Proposition 11.9.

PROPOSITION 11.10. *The cover time satisfies*
$$ t_{\mathrm{cov}} \leq (\log 2)k 2^k (1 + o(1)). $$

PROOF. We partition the state space $\{0, 1\}^k$ into two sets. Fix $j = \lceil \log_2 k \rceil$ and let $B$ be the set of all strings $b \in \{0, 1\}^k$ with the following property: any bitstring that is both a suffix and a prefix of $b$ must have length less than $k - j$. For any string $b \in B$, we must have $\tau_b^+ > j$ when starting from $b$.

Since for $m < k$ there are only $2^m$ strings of length $k$ such that the prefix of length $k - m$ equals the suffix of that length, we have

$$ |B^c| \leq 2 + 4 + \cdots + 2^j \leq 2^{j+1} \leq 4k. $$

For $a, b \in B$, we can use Lemma 11.8 to bound the maximum expected hitting time. We have

$$ \mathbf{E}_a \tau_b \leq \mathbf{E} w_b \leq \frac{\mathbf{E}_b \tau_b^+ + k\theta}{1 - \theta}. $$

(Since $\mathbf{E} w_b$ does not depend on the initial state, we have taken the initial state to be $b$ as we apply Lemma 11.8.)

Since our chain has a uniform stationary distribution, (1.28) implies that $\mathbf{E}_b \tau_b^+ = 2^k$. By our choice of $B$, we have $\theta = \mathbf{P}_b(\tau_b^+ < k) \leq 1/k$. Thus

$$ \mathbf{E}_a \tau_b \leq \frac{2^k + k(1/k)}{1 - 1/k} = 2^k (1 + o(1)). \tag{11.23} $$

For $a, b \in B^c$, we again use Lemma 11.7 to bound $\mathbf{E}_a \tau_b$. Finally we apply (11.22), obtaining

$$ \begin{aligned} t_{\mathrm{cov}} &\leq (\log |B| + o(1)) \left( 2^k (1 + o(1)) + (\log |B^c| + o(1)) \left( 2^{k+1} + o(1) \right) \right) \\ &= (\log 2)k 2^k (1 + o(1)). \end{aligned} $$

$\blacksquare$

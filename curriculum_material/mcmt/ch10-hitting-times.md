# Chapter 10 — Hitting Times
*(PDF pages 144–165; book pages 128–149)*

### PDF page 144 (book page 128)

CHAPTER 10

# Hitting Times

**10.1. Definition**

Global maps are often unavailable for real networks that have grown without central organization, such as the internet. However, sometimes the structure can be queried locally, meaning that given a specific node $v$, for some cost all nodes connected by a single link to $v$ can be determined. How can such local queries be used to determine whether two nodes $v$ and $w$ can be connected by a path in the network?

Suppose you have limited storage, but you are not concerned about time. In this case, one approach is to start a random walk at $v$, allow the walk to explore the graph for some time, and observe whether the node $w$ is ever encountered. If the walk visits node $w$, then clearly $v$ and $w$ must belong to the same connected component of the network. On the other hand, if node $w$ has not been visited by the walk by time $t$, it is possible that $w$ is not accessible from $v$—but perhaps the walker was simply unlucky. It is of course important to distinguish between these two possibilities. In particular, when $w$ is connected to $v$, we desire an estimate of the expected time until the walk visits $w$ starting at $v$.

Given a Markov chain $(X_t)$ with state space $\mathcal{X}$, it is natural to define the **hitting time** $\tau_A$ of a subset $A \subseteq \mathcal{X}$ by

$$ \tau_A := \min\{t \geq 0 \ : \ X_t \in A\}. $$

We will simply write $\tau_w$ for $\tau_{\{w\}}$, consistent with our notation in Section 1.5.2.

We have already seen the usefulness of hitting times. In Section 1.5.3 we used a variant

$$ \tau_x^+ = \min\{t \geq 1 \ : \ X_t = x\} $$

(called the **first return time** when $X_0 = x$) to build a stationary distribution.

To connect our discussion of hitting times to mixing times, we mention now the problem of estimating the mixing time for two "glued" tori, the graph considered in Example 7.5.

Let $V_1$ be the collection of nodes in the right-hand torus, and let $v^\star$ be the node connecting the two tori.

When the walk is started at a node $x$ in the left-hand torus, we have

$$ \|P^t(x, \cdot) - \pi\|_{\mathrm{TV}} \geq \pi(V_1) - P^t(x, V_1) \geq \frac{1}{2} - \mathbf{P}_x\{X_t \in V_1\} \geq \frac{1}{2} - \mathbf{P}_x\{\tau_{v^\star} \leq t\}. \tag{10.1} $$

If the walk is unlikely to have exited the left-hand torus by time $t$, then (10.1) shows that $d(t)$ is not much smaller than $1/2$. In view of this, it is not surprising that estimates for $\mathbf{E}_x(\tau_{v^\star})$ are useful for bounding $t_{\mathrm{mix}}$ for this chain. These ideas are developed in Section 10.8.

### PDF page 145 (book page 129)

**10.2. Random Target Times**

For a Markov chain with stationary distribution $\pi$, let

$$ t_\odot^a := \sum_{x \in \mathcal{X}} \mathbf{E}_a(\tau_x)\pi(x) \tag{10.2} $$

be the expected time for the chain, started at $a$, to hit a "random target", that is, a vertex selected at random according to $\pi$.

LEMMA 10.1 (Random Target Lemma). *For an irreducible Markov chain on the state space $\mathcal{X}$ with stationary distribution $\pi$, the target time $t_\odot^a$ does not depend on $a \in \mathcal{X}$.*

In view of the above lemma, the following definition of the **target time** is proper, for any $a \in \mathcal{X}$:

$$ t_\odot := t_\odot^a \,. $$

PROOF. Set $h_x(a) := \mathbf{E}_a(\tau_x)$, and observe that for $x \neq a$,

$$ h_x(a) = \sum_{y \in \mathcal{X}} \mathbf{E}_a(\tau_x \mid X_1 = y)P(a,y) = \sum_{y \in \mathcal{X}} \left(1 + h_x(y)\right) P(a,y) = (Ph_x)(a) + 1, $$

so that

$$ (Ph_x)(a) = h_x(a) - 1. \tag{10.3} $$

Also,

$$ \mathbf{E}_a(\tau_a^+) = \sum_{y \in \mathcal{X}} \mathbf{E}_a(\tau_a^+ \mid X_1 = y)P(a,y) = \sum_{y \in \mathcal{X}} \left(1 + h_a(y)\right) P(a,y) = 1 + (Ph_a)(a). $$

Since $\mathbf{E}_a(\tau_a^+) = \pi(a)^{-1}$,

$$ (Ph_a)(a) = \frac{1}{\pi(a)} - 1. \tag{10.4} $$

Thus, letting $h(a) := \sum_{x \in \mathcal{X}} h_x(a)\pi(x)$, (10.3) and (10.4) show that

$$ (Ph)(a) = \sum_{x \in \mathcal{X}} (Ph_x)(a)\pi(x) = \sum_{x \neq a}(h_x(a) - 1)\pi(x) + \pi(a)\left(\frac{1}{\pi(a)} - 1\right). $$

Simplifying the right-hand side and using that $h_a(a) = 0$ yields

$$ (Ph)(a) = h(a). $$

That is, $h$ is harmonic. Applying Lemma 1.16 shows that $h$ is a constant function. $\blacksquare$

Since $t_\odot$ does not depend on the state $a$, it is true that

$$ t_\odot = \sum_{x,y \in \mathcal{X}} \pi(x)\pi(y)\mathbf{E}_x(\tau_y) = \mathbf{E}_\pi(\tau_\pi). \tag{10.5} $$

We will often find it useful to estimate the worst-case hitting times between states in a chain. Define

$$ t_{\mathrm{hit}} := \max_{x,y \in \mathcal{X}} \mathbf{E}_x(\tau_y). \tag{10.6} $$

LEMMA 10.2. *For an irreducible Markov chain with state space $\mathcal{X}$ and stationary distribution $\pi$,*

$$ t_{\mathrm{hit}} \leq 2\max_w \mathbf{E}_\pi(\tau_w). $$

### PDF page 146 (book page 130)

**FIGURE 10.1.** For random walk on this family of graphs, $t_{\mathrm{hit}} \gg t_\odot$. *[Figure: a complete graph on eight vertices with all pairs connected by edges; the rightmost vertex, labeled $w$, has a single additional edge extending to an isolated leaf vertex labeled $v$. Three vertices are labeled: $u$ on the left, $w$ on the right, and $x$ at the lower right of the complete graph.]*

PROOF. For any $a, y \in \mathcal{X}$, we have

$$ \mathbf{E}_a(\tau_y) \leq \mathbf{E}_a(\tau_\pi) + \mathbf{E}_\pi(\tau_y), \tag{10.7} $$

since we can insist that the chain go from $a$ to $y$ via a random state $x$ chosen according to $\pi$. By Lemma 10.1,

$$ \mathbf{E}_a(\tau_\pi) = \mathbf{E}_\pi(\tau_\pi) \leq \max_w \mathbf{E}_\pi(\tau_w). $$

It is now clear that (10.7) implies the desired inequality. $\blacksquare$

Note that for a transitive chain, $\mathbf{E}_\pi(\tau_w)$ does not depend on $w$. By averaging, for any $w$, we obtain $\mathbf{E}_\pi(\tau_w) = \mathbf{E}_\pi(\tau_\pi) = t_\odot$. Combing this with Lemma 10.2 proves:

COROLLARY 10.3. *For an irreducible transitive Markov chain,*

$$ t_{\mathrm{hit}} \leq 2t_\odot. $$

EXAMPLE 10.4. When the underlying chain is not transitive, it is possible for $t_{\mathrm{hit}}$ to be much larger than $t_\odot$. Consider the example of simple random walk on a complete graph on $n$ vertices with a leaf attached to one vertex (see Figure 10.1). Let $v$ be the leaf and let $w$ be the neighbor of the leaf; call the other vertices **ordinary**. Let the initial state of the walk be $v$. The first return time to $v$ satisfies both

$$ \mathbf{E}_v\tau_v^+ = \mathbf{E}_v\tau_w + \mathbf{E}_w\tau_v = 1 + \mathbf{E}_w\tau_v $$

(since the walk must take its first step to $w$) and

$$ \mathbf{E}_v\tau_v^+ = \frac{1}{\pi(v)} = \frac{2\binom{n}{2} + 2}{1} = n^2 - n + 2, $$

by Proposition 1.19. Hence

$$ t_{\mathrm{hit}} \geq \mathbf{E}_w\tau_v = n^2 - n + 1 \,. $$

By the Random Target Lemma and symmetry,

$$ t_\odot = \mathbf{E}_v\tau_\pi = \pi(w) + (n-1)\pi(u)[1 + \mathbf{E}_w\tau_u] \,. \tag{10.8} $$

where $u \notin \{v, w\}$. Let $x \notin \{u, v, w\}$. By conditioning on the first step of the walk and exploiting symmetry, we have

$$ \mathbf{E}_w\tau_u = 1 + \frac{1}{n}\left(\mathbf{E}_v\tau_u + (n-2)\mathbf{E}_x\tau_u\right) $$
$$ = 1 + \frac{1}{n}\left(1 + \mathbf{E}_w\tau_u + (n-2)\mathbf{E}_x\tau_u\right) $$

### PDF page 147 (book page 131)

and

$$ \mathbf{E}_x\tau_u = 1 + \frac{1}{n-1}\left(\mathbf{E}_w\tau_u + (n-3)\mathbf{E}_x\tau_u\right) \,. $$

We have two equations in the two unknowns $\mathbf{E}_w\tau_u$ and $\mathbf{E}_x\tau_u$. Solving yields

$$ \mathbf{E}_w\tau_u = \frac{n^2 - n + 4}{n} \leq n \,, \quad \text{ for } n \geq 4 \,. $$

This along with (10.8) yields $t_\odot = O(n) \ll t_{\mathrm{hit}}$.

**10.3. Commute Time**

The **commute time** between nodes $a$ and $b$ in a network is the expected time to move from $a$ to $b$ and then back to $a$. We denote by $\tau_{a,b}$ the (random) amount of time to transit from $a$ to $b$ and then back to $a$. That is,

$$ \tau_{a,b} = \min\{t \geq \tau_b \,:\, X_t = a\}, \tag{10.9} $$

where $X_0 = a$. The commute time is then

$$ t_{a \leftrightarrow b} := \mathbf{E}_a(\tau_{a,b}) \,. \tag{10.10} $$

Note that $t_{a \leftrightarrow b} = \mathbf{E}_a(\tau_b) + \mathbf{E}_b(\tau_a)$. The maximal commute time is

$$ t_{\mathrm{comm}} = \max_{a,b \in \mathcal{X}} t_{a \leftrightarrow b} \,. \tag{10.11} $$

The commute time is of intrinsic interest and can be computed or estimated using resistance (the **commute time identity**, Proposition 10.7). In graphs for which $\mathbf{E}_a(\tau_b) = \mathbf{E}_b(\tau_a)$, the expected hitting time is half the commute time, so estimates for the commute time yield estimates for hitting times. Transitive networks (defined below) enjoy this property (Proposition 10.10).

The following lemma will be used in the proof of the commute time identity:

LEMMA 10.5. *Let $(X_t)$ be a Markov chain with transition matrix $P$. Suppose that for two probability distributions $\mu$ and $\nu$ on $\mathcal{X}$, there is a stopping time $\tau$ with $\mathbf{P}_\mu\{\tau < \infty\} = 1$ and such that $\mathbf{P}_\mu\{X_\tau = \cdot\} = \nu$. If $\rho$ is the row vector*

$$ \rho(x) := \mathbf{E}_\mu\left(\sum_{t=0}^{\tau-1} \mathbf{1}_{\{X_t = x\}}\right) \,, \tag{10.12} $$

*then $\rho P = \rho - \mu + \nu$. In particular, if $\mu = \nu$ then $\rho P = \rho$. Thus, if $\mu = \nu$ and $\mathbf{E}_\mu(\tau) < \infty$, then $\frac{\rho}{\mathbf{E}_\mu(\tau)}$ is a stationary distribution $\pi$ for $P$.*

The proof is very similar to the proof of Proposition 1.14. The details are left to the reader in Exercise 10.1.

REMARK 10.6. When $\tau$ satisfies $\mathbf{P}_a\{X_\tau = a\} = 1$ (for example, $\tau = \tau_a^+$ or $\tau = \tau_{a,b}$), then $\rho$ as defined by (10.12) equals the Green's function $G_\tau(a, \cdot)$, and Lemma 10.5 says that

$$ \frac{G_\tau(a,x)}{\mathbf{E}_a(\tau)} = \pi(x) \,. \tag{10.13} $$

Recall that $\mathcal{R}(a \leftrightarrow b)$ is the effective resistance between the vertices $a$ and $b$ in a network. (See Section 9.4.)

### PDF page 148 (book page 132)

PROPOSITION 10.7 (Commute Time Identity). *Let $(G, \{c(e)\})$ be a network, and let $(X_t)$ be the random walk on this network. For any nodes $a$ and $b$ in $V$,*

$$ t_{a \leftrightarrow b} = c_G \mathcal{R}(a \leftrightarrow b). \tag{10.14} $$

*(Recall that $c(x) = \sum_{y \,:\, y \sim x} c(x, y)$ and that $c_G = \sum_{x \in V} c(x) = 2 \sum_{e \in E} c(e)$.)*

PROOF. By (10.13),

$$ \frac{G_{\tau_{a,b}}(a, a)}{\mathbf{E}_a(\tau_{a,b})} = \pi(a) = \frac{c(a)}{c_G}. $$

By definition, after visiting $b$, the chain does not visit $a$ until time $\tau_{a,b}$, so $G_{\tau_{a,b}}(a, a) = G_{\tau_b}(a, a)$. The conclusion follows from Lemma 9.6. $\blacksquare$

Exercise 9.8 shows that the resistances obey a triangle inequality. We can use Proposition 10.7 to provide another proof.

COROLLARY 10.8. *The resistance $\mathcal{R}$ satisfies a triangle inequality: If $a, b, c$ are vertices, then*

$$ \mathcal{R}(a \leftrightarrow c) \le \mathcal{R}(a \leftrightarrow b) + \mathcal{R}(b \leftrightarrow c). \tag{10.15} $$

PROOF. It is clear that $\mathbf{E}_a \tau_c \le \mathbf{E}_a \tau_b + \mathbf{E}_b \tau_c$ for nodes $a, b, c$. Switching the roles of $a$ and $c$ shows that commute times satisfy a triangle inequality. $\blacksquare$

Note that $\mathbf{E}_a(\tau_b)$ and $\mathbf{E}_b(\tau_a)$ can be very different for general Markov chains and even for reversible chains (see Exercise 10.3). However, for certain types of random walks on networks they are equal. A network $\langle G, \{c(e)\} \rangle$ is ***transitive*** if for any pair of vertices $x, y \in V$ there exists a permutation $\psi_{x,y} : V \to V$ with

$$ \psi_{x,y}(x) = y \quad \text{and} \quad c(\psi_{x,y}(u), \psi_{x,y}(v)) = c(u, v) \text{ for all } u, v \in V. \tag{10.16} $$

Such maps $\psi$ are also called network automorphisms.

On a transitive network, the stationary distribution $\pi$ is uniform.

REMARK 10.9. In Section 2.6.2 we defined transitive Markov chains. The reader should check that a random walk on a transitive network is a transitive Markov chain.

For a random walk $(X_t)$ on a transitive network,

$$ \begin{aligned} \mathbf{P}_a &\{(X_0, \ldots, X_t) = (a_0, \ldots, a_t)\} \\ &= \mathbf{P}_{\psi(a)} \{(X_0, \ldots, X_t) = (\psi(a_0), \ldots, \psi(a_t))\}. \end{aligned} \tag{10.17} $$

PROPOSITION 10.10. *For a random walk on a transitive connected network $\langle G, \{c(e)\} \rangle$, for any vertices $a, b \in V$,*

$$ \mathbf{E}_a(\tau_b) = \mathbf{E}_b(\tau_a). \tag{10.18} $$

REMARK 10.11. Note that the biased random walk on a cycle is a transitive Markov chain, but (10.18) fails for it. Thus, reversibility is a crucial assumption.

PROOF. Suppose $\xi$ and $\eta$ are finite strings with letters in $V$, that is, $\xi \in V^m$ and $\eta \in V^n$. We say that $\xi \preceq \eta$ if and only if $\xi$ is a subsequence of $\eta$.

Let $\tau_{ab}$ be the time required to first visit $a$ and then hit $b$. That is,

$$ \tau_{ab} = \min\{t \ge 0 \,:\, ab \preceq (X_0, \ldots, X_t)\}. $$

### PDF page 149 (book page 133)

Using the identity (1.31) for reversed chains,

$$ \mathbf{P}_\pi\{\tau_{ab} > k\} = \mathbf{P}_\pi\{ab \not\preceq X_0 \ldots X_k\} = \mathbf{P}_\pi\{ab \not\preceq X_k \ldots X_0\}. \tag{10.19} $$

Clearly, $ab \preceq X_k \ldots X_0$ is equivalent to $ba \preceq X_0 \ldots X_k$ (just read from right to left), so the right-hand side of (10.19) equals

$$ \mathbf{P}_\pi\{ba \not\preceq X_0 \ldots X_k\} = \mathbf{P}_\pi\{\tau_{ba} > k\}. $$

Summing over $k$ shows that

$$ \mathbf{E}_\pi \tau_{ab} = \mathbf{E}_\pi \tau_{ba}. \tag{10.20} $$

So far, we have not used transitivity. By transitivity,

$$ \mathbf{E}_\pi \tau_a = \mathbf{E}_\pi \tau_b. \tag{10.21} $$

Indeed, if $\psi$ is the network automorphism with $\psi(a) = b$, then $\mathbf{E}_x \tau_a = \mathbf{E}_{\psi(x)} \tau_b$. Since $\pi$ is uniform, averaging over $x$ establishes (10.21). Subtracting (10.21) from (10.20) finishes the proof. $\blacksquare$

Without requiring transitivity, the following cycle identity holds:

LEMMA 10.12. *For any three states $a, b, c$ of a reversible Markov chain,*

$$ \mathbf{E}_a(\tau_b) + \mathbf{E}_b(\tau_c) + \mathbf{E}_c(\tau_a) = \mathbf{E}_a(\tau_c) + \mathbf{E}_c(\tau_b) + \mathbf{E}_b(\tau_a). $$

REMARK 10.13. We can reword this lemma as

$$ \mathbf{E}_a(\tau_{bca}) = \mathbf{E}_a(\tau_{cba}), \tag{10.22} $$

where $\tau_{bca}$ is the time to visit $b$, then visit $c$, and then hit $a$.

A natural approach to proving this is to assume that reversing a sequence started from $X_0 = a$ and having $\tau_{bca} = n$ yields a sequence started from $a$ having $\tau_{cba} = n$. However, this is not true. For example, if $X_0 X_1 X_2 X_3 X_4 X_5 = acabca$, then $\tau_{bca} = 5$, yet the reversed sequence $acbaca$ has $\tau_{cba} = 3$.

PROOF OF LEMMA 10.12. Adding $\mathbf{E}_\pi \tau_a$ to both sides of the claimed identity (10.22) shows that it is equivalent to

$$ \mathbf{E}_\pi(\tau_{abca}) = \mathbf{E}_\pi(\tau_{acba}). $$

The latter equality is proved in the same manner as (10.20). $\blacksquare$

REMARK 10.14. The proof of Lemma 10.12 can be generalized to obtain

$$ \mathbf{E}_a(\tau_{a_1 a_0 \ldots a_m a}) = \mathbf{E}_a(\tau_{a_m a_{m-1} \ldots a_1 a}). \tag{10.23} $$

EXAMPLE 10.15 (Random walk on rooted finite binary trees). The rooted and finite binary tree of depth $k$ was defined in Section 5.3.4. We let $n$ denote the number of vertices and note that the number of edges equals $n - 1$.

We compute the expected commute time between the root and the set of leaves $B$. Identify all vertices at level $j$ for $j = 1$ to $k$ to obtain the graph shown in Figure 10.2.

Using the network reduction rules, this is equivalent to a segment of length $k$, with conductance between vertices $j - 1$ and $j$ equal to $2^j$ for $1 \le j \le k$. Thus the effective resistance from the root to the set of leaves $B$ equals

$$ \mathcal{R}(a \leftrightarrow B) = \sum_{j=1}^{k} 2^{-j} = 1 - 2^{-k} \le 1. $$

### PDF page 150 (book page 134)

*[Figure: A horizontal chain of four filled dots connected by curved multi-edges. The leftmost pair of dots is joined by two arcs; the next pair by three arcs; a dashed line connects to the rightmost pair, which is joined by many nested arcs (some dashed), depicting the multigraph obtained by identifying levels of a binary tree.]*

FIGURE 10.2. A binary tree after identifying all vertices at the same distance from the root

Using the Commute Time Identity (Proposition 10.7), since $c_G = 2(n - 1)$, the expected commute time is bounded by $2n$. For the lazy random walk, the expected commute time is bounded by $4n$.

This completes the proof in Section 5.3.4 that for the lazy random walk on this tree, $t_{\text{mix}} \le 16n$.

We can give a general bound for the commute time of simple random walk on simple graphs, that is, graphs without multiple edges or loops.

PROPOSITION 10.16.

(a) *For random walk on a simple graph with $n$ vertices and $m$ edges,*

$$ t_{a \leftrightarrow b} \le 2nm \le n^3 \quad \text{for all } a, b. $$

(b) *For random walk on a $d$-regular graph on $n$ vertices,*

$$ t_{a \leftrightarrow b} \le 3n^2 - nd \quad \text{for all } a, b. $$

PROOF. Since $\mathcal{R}(a \leftrightarrow b) \le \text{diam}$ and $2m \le n^2$, Proposition 10.7 implies that

$$ t_{a \leftrightarrow b} = \mathcal{R}(a \leftrightarrow b) \cdot 2m \le 2mn \le n^3. $$

For a regular graph, we first show that $\text{diam} \le \frac{3n}{d}$. To see this, let $\tilde{\mathcal{N}}(x)$ consist of $x$ together with its neighbors. Let $x, y \in \mathcal{X}$ be extremal points, so $d(x, y) = \ell = \text{diam}$, and let the path $x_0 = x, x_1, \ldots, x_\ell = y$ be such that $\{x_{i-1}, x_i\}$ is an edge. Note that $\tilde{\mathcal{N}}(x_i) \cap \tilde{\mathcal{N}}(x_j) = \varnothing$ for $j > i + 2$, as otherwise the path would not be minimal. Therefore, the sum $\sum_{i=0}^{\ell} |\tilde{\mathcal{N}}(x_i)|$ counts each vertex in the graph at most 3 times. We conclude that

$$ (d + 1)(\ell + 1) = \sum_{i=0}^{\ell} |\tilde{\mathcal{N}}(x_i)| \le 3n, $$

and since $\ell = \text{diam}$, we obtain that $\text{diam} \le \frac{3n}{d} - 1$. Part (b) then follows again from Proposition 10.7. $\blacksquare$

**10.4. Hitting Times on Trees**

Let $T$ be a finite tree with edge conductances $\{c(e)\}$, and consider any edge $\{x, y\}$ with $c(x, y) > 0$. If $y$ and all edges containing $y$ are removed, the graph becomes disconnected; remove all remaining components except the one containing

### PDF page 151 (book page 135)

*[Figure: two small trees side by side, labeled $T$ (left) and $\widetilde{T}$ (right). In $T$, a vertex $y$ and vertex $v$ are marked among branching edges. In $\widetilde{T}$, vertex $y$ is a leaf attached by an edge to vertex $x$, with further branches.]*

FIGURE 10.3. The modified tree $\widetilde{T}$.

$x$, add $y$ and the edge $\{x, y\}$ with weight $c(x, y)$, and call the resulting network $\widetilde{T}$ and its edge set $\tilde{E}$. (See Figure 10.3.)

Writing $\tilde{\mathbf{E}}$ for expectation of the walk on $\widetilde{T}$ and $\tilde{c} = \sum_{u,v} \tilde{c}(u, v)$, we have

$$\tilde{\mathbf{E}}_y[\tau_y^+] = \frac{1}{\tilde{\pi}(y)} = \frac{\tilde{c}}{\tilde{c}(x, y)}\,.$$

(Note in the unweighted case the right-hand side equals $2|\tilde{E}|$.)

On the other hand, in the modified tree, the expected time to return to $y$ must be one more than the expected time to go from $x$ to $y$ in the original graph, since from $y$ the only move possible is to $x$, and the walk on the original graph viewed up until a visit to $y$ (when started from $x$) is the same as the walk on the modified graph. Therefore,

$$\tilde{\mathbf{E}}_y(\tau_y^+) = 1 + \mathbf{E}_x(\tau_y)\,.$$

Putting these two equalities together shows that

$$\mathbf{E}_x(\tau_y) = \begin{cases} 2|\tilde{E}| - 1 & \text{for unweighted graphs} \\ \frac{\tilde{c}}{\tilde{c}(x,y)} - 1 & \text{for networks}\,. \end{cases} \tag{10.24}$$

The expected hitting times between any two vertices can be found by adding the expected hitting times between neighboring vertices along a path connecting them.

EXAMPLE 10.17 (Hitting times on binary tree). Let $T$ be the binary tree of depth $k$, with root $\rho$. Let $v$ be any leaf of the tree. Let $v = v_0, v_1, \ldots, v_k = \rho$ be the unique path connecting $v$ to $\rho$. Using (10.24),

$$\mathbf{E}_{v_{i-1}}[\tau_{v_i}] = 2(2^i - 1) - 1 = 2^{i+1} - 3\,.$$

Therefore,

$$\mathbf{E}_{v_0}[\tau_\rho] = \sum_{i=1}^{k}(2^{i+1} - 3) = 2^{k+2} - (3k + 4)\,.$$

On the other hand, we have that

$$\mathbf{E}_{v_i}[\tau_{v_{i-1}}] = 2(2^{k+1} - 2^i) - 1,$$

so

$$\mathbf{E}_\rho[\tau_{v_0}] = \sum_{i=1}^{k}\mathbf{E}_{v_i}[\tau_{v_{i-1}}] = (k - 1)2^{k+2} - (k - 4)\,.$$

We conclude that the expected time to travel from the root to a leaf is larger than the expected time to travel from a leaf to the root. The first expectation is

### PDF page 152 (book page 136)

of order the volume of the tree, while the second is of order the depth times the volume.

EXAMPLE 10.18 (Hitting times on comb with linear backbone). Consider the graph obtained by starting with a path of length $n$, and attaching to each vertex $k \in \{1, 2, \ldots, n\}$ of this path another path of length $f(k)$. The resulting graph is a tree. (See Figure 10.4.)

*[Figure: a "comb" graph. A horizontal backbone path has vertices labeled $1, 2, 3, \ldots, n{-}1, n$ (with a dashed segment indicating omitted middle vertices). From each backbone vertex $k$ a vertical path of length $f(k)$ rises upward, with its top vertex labeled $f(1), f(2), f(3), \ldots, f(n{-}1), f(n)$; the teeth grow taller toward the right.]*

FIGURE 10.4. The comb graph.

Writing $F(j) := \sum_{i=1}^{j} f(i)$, we have that

$$\mathbf{E}_j[\tau_{j+1}] = 2[F(j) + j] - 1,$$

and so

$$\mathbf{E}_1[\tau_n] = 2\sum_{j=1}^{n-1} F(j) + (n - 1)n - (n - 1) = 2\sum_{j=1}^{n-1} F(j) + (n - 1)^2\,.$$

EXAMPLE 10.19 (Path). Fix $0 < p < 1$, and set $q := 1 - p$ and $\alpha := p/q$. Consider the path with vertices $\{-m, -m{+}1, \ldots, 0, 1, 2, \ldots, n\}$ and edges $\{k, k{+}1\}$ with $c(k, k + 1) = \alpha^k$ for $k = -m, \ldots, 0, \ldots, n - 1$.

We have $\tilde{c} = (2p\alpha^k - 2q\alpha^{-m})/(p - q)$, and (10.24) in this case yields

$$\mathbf{E}_k(\tau_{k+1}) = \frac{p + q(1 - 2\alpha^{-(m+k)})}{p - q}\,. \tag{10.25}$$

Letting $m \to \infty$, if $p > 1/2$, then for biased random walk on all of $\mathbb{Z}$, we have

$$\mathbf{E}_k(\tau_{k+1}) = \frac{1}{p - q}\,. \tag{10.26}$$

### PDF page 153 (book page 137)

**10.5. Hitting Times for Eulerian Graphs**

A directed graph $G = (V, E)$ is called **Eulerian** if it is strongly connected and the in-degree equals the out-degree at every vertex. See Exercise 10.5 for the origin of the term.

PROPOSITION 10.20. *Let $G = (V, E)$ be an Eulerian directed graph. Let $m = |E|$, and assume that there exists a directed path of length $\ell$ from vertex $x$ to vertex $y$. Then*

$$\mathbf{E}_x(\tau_y) + \mathbf{E}_y(\tau_x) \le \ell \cdot m\,.$$

PROOF. It is enough to prove this for the case where there is a directed edge $(x, y)$, since otherwise $\mathbf{E}_x(\tau_y)$ is bounded by the sum of the expected hitting times along the path from $x$ to $y$, and similarly for $\mathbf{E}_y(\tau_x)$.

Consider the chain $Z_t = (X_t, X_{t+1})$ on directed edges. This chain has transition matrix $\tilde{P}$, where

$$\tilde{P}((x, y), (y, z)) = P(y, z)$$
$$\tilde{P}((x, y), (u, v)) = 0 \quad \text{if } y \ne u\,.$$

The stationary distribution for $\tilde{P}$ is uniform on $E$. By Proposition 1.19, $\mathbf{E}_{(x,y)}\big(\tau_{(x,y)}^+\big) = m$. If $Z_0 = (x, y) = Z_t$ for some time $t$, then $X_1 = y$ and $X_t = x$ and $X_{t+1} = y$. Therefore, $\tau_{(x,y)}^+$ for the chain $Z$ bounds the commute time from $x$ to $y$ in $G$. $\blacksquare$

**10.6. Hitting Times for the Torus**

Since the torus is transitive, Proposition 10.10 and the Commute Time Identity (Proposition 10.7) imply that for random walk on the $d$-dimensional torus,

$$\mathbf{E}_a(\tau_b) = dn^d \mathcal{R}(a \leftrightarrow b). \tag{10.27}$$

(For an unweighted graph, $c = 2 \times |\text{edges}|$.)

PROPOSITION 10.21. *Consider the simple random walk on the torus $\mathbb{Z}_n^d$. There exist constants $0 < c_d \le C_d < \infty$ such that if $x$ and $y$ are at distance $k \ge 1$, then*

$$c_d n^d \le \mathbf{E}_x(\tau_y) \le C_d n^d \qquad \text{uniformly in } k \text{ if } d \ge 3, \tag{10.28}$$
$$c_2 n^2 \log(k) \le \mathbf{E}_x(\tau_y) \le C_2 n^2 \log(k + 1) \qquad \text{if } d = 2. \tag{10.29}$$

For the upper bounds, we will need to define flows via the $d$-color Pólya urn; see Lemma 2.7.

PROOF OF PROPOSITION 10.21. First, the lower bounds. For $j \ge 0$, let $\Pi_j$ be the edge-boundary of the cube of side-length $2j$ centered at $x$, i.e., the set of edges connecting the cube to its complement. For $1 \le j \le k/d$, the edges in $\Pi_j$ form an edge-cutset separating $x$ from $y$. Since $|\Pi_j| \le \tilde{c}_d \cdot j^{d-1}$, Proposition 9.16 yields

$$\mathcal{R}(x \leftrightarrow y) \ge \frac{1}{\tilde{c}_d}\sum_{j=1}^{k/d}\frac{1}{j^{d-1}}\,. \tag{10.30}$$

The lower bound in (10.29) follows from the above and (10.27), since $\sum_{j=1}^{r} j^{-1}$ is comparable to $\log r$. For $d \ge 3$, the right-hand side of (10.30) is bounded below by

### PDF page 154 (book page 138)

*[Figure: a cube drawn in perspective. The bottom-front-left corner is labeled $x$ (a filled dot) and the top-back-right corner is labeled $y$ (a filled dot). The bottom-front edge is marked with length $k$, the bottom-right receding edge is marked with length $k$, and the right vertical edge is marked with length $k$.]*

FIGURE 10.5. The vertices $x$ and $y$ are antipodal vertices on the boundary of a cube of side-length $k$.

$(\tilde{c}_d)^{-1}$ by omitting all but the first term in the sum. The lower bound in (10.28) again follows from this bound together with (10.27).

Now for the upper bounds. Let $d \geq 3$. First, assume that

$$ x = (1, \ldots, 1) = \mathbf{1} \quad \text{and} \quad y = (k+1, \ldots, k+1) = (k+1)\mathbf{1} $$

are antipodal points on a hypercube of side-length $k$, where $k$ is even. (So the distance between $x$ and $y$ is $d \cdot k$. See Figure 10.5.) Also, assume that $k < n/d$ to ensure that the distance between $\mathbf{1}$ and $(k+1)\mathbf{1}$ is less than $n$, guarantying that $\{1, 2, \ldots, k+1\}^d$ does not "wrap around" the torus. We run the Pólya urn process $\{\boldsymbol{N}_t\}_{t \geq 0}$ until it hits the hyperplane $V_{kd/2}$, where

$$ V_j := \left\{ (x_1, \ldots, x_d) \in \mathbb{Z}^d : \sum_{i=1}^{d} x_i = j + d \right\}. $$

Let $\vec{E}_k$ be all oriented edges of the form

$$ \left( (x_1, \ldots, x_i, \ldots, x_d),\ (x_1, \ldots, x_i + 1, \ldots, x_d) \right), $$

where $1 \leq x_j \leq k+1$ for $1 \leq j \leq d$, and $x_i \leq k$. For an oriented edge $e$ in $\vec{E}_k$, define the flow $f$ by

$$ f(e) = \mathbf{P}\{((N_t^1, \ldots, N_t^d), (N_{t+1}^1, \ldots, N_{t+1}^d)) = e \text{ for some } t \geq 0\}. $$

If, for an edge $(a, b)$, the reversal $(b, a) \in \vec{E}_k$, then define $f(a, b) = -f(b, a)$. Complete the definition of $f$ for all edges in the graph with vertex set $\{1, 2, \ldots, k+1\}^d$ by giving the other half of the cube the symmetrical flow values. In particular, for $e$ on the other half of the cube,

$$ f(e) = -f((k+1)\mathbf{1} - e). $$

Thus, $f$ defines a unit flow from $\mathbf{1}$ to $(k+1)\mathbf{1}$.

From Lemma 2.7, for each $j \geq 1$, the process $\{\boldsymbol{N}_t\}_{t \geq 1} := \{(N_t^1, \ldots, N_t^d)\}_{t \geq 1}$ is equally likely to pass through each of the vertices in $V_j$. For $v \in V_j$ where

### PDF page 155 (book page 139)

$1 \leq j \leq kd/2$, the urn process visits $v$ if and only if it traverses one of the oriented edges pointing to $v$, whence

$$ \sum_{u\,:\,(u,v)\in\vec{E}_k} f(u,v)^2 \leq \left[ \sum_{u\,:\,(u,v)\in\vec{E}_k} f(u,v) \right]^2 $$
$$ = \mathbf{P}\{\boldsymbol{N}_t = v \text{ for some } t \geq 0\}^2 = \binom{j+d-1}{d-1}^{-2}. $$

By symmetry, the energy of $f$ equals

$$ 2 \sum_{e\in\vec{E}_k} f(e)^2 = 2 \sum_{j=1}^{kd/2} \sum_{v\in V_j} \sum_{u\,:\,(u,v)\in\vec{E}_k} f(u,v)^2 \leq 2 \sum_{j=1}^{kd/2} \binom{j+d-1}{d-1}^{-1}. $$

Suppose first that $d \geq 3$. The sum on the right-hand side is bounded by

$$ 2 \sum_{j=1}^{\infty} \binom{j+d-1}{d-1}^{-1} = \frac{2}{d-2}\,; $$

See Exercise 10.18. By Thomson's Principle (Theorem 9.10),

$$ \mathcal{R}(\mathbf{1} \leftrightarrow (k+1)\mathbf{1}) \leq \frac{2}{d-2}\,. $$

Now suppose that $x$ and $y$ differ by $2k$ in a single coordinate. Without loss of generality, we can assume that $x = \mathbf{1}$ and $y = (2k+1, 1, \ldots, 1)$. Let $z = (k+1)\mathbf{1}$ (see Figure 10.6). By symmetry, $\mathcal{R}(z \leftrightarrow y) = \mathcal{R}(x \leftrightarrow y)$. By the triangle inequality for effective resistances (Corollary 10.8),

$$ \mathcal{R}(x \leftrightarrow y) \leq \mathcal{R}(x \leftrightarrow z) + \mathcal{R}(z \leftrightarrow y) \leq \frac{4}{d-2}\,. $$

If $x$ and $y$ differ in a single coordinate by an odd integer amount, then the triangle inequality shows that $\mathcal{R}(x \leftrightarrow y) \leq \frac{4}{d-2} + 1$.

Now, if $x$ and $y$ are arbitrary points, then there exist vertices $\{z_j\}_{j=0}^{d}$ with $x = z_0$ and $z_d = y$ so that each pair $(z_{i-1}, z_i)$ differs only in the $i$-th coordinate. By the triangle inequality, $\mathcal{R}(x \leftrightarrow y) \leq \frac{4d}{d-2} + d$.

Now suppose $d = 2$: If the points $x$ and $y$ are the diagonally opposite corners of a square, the upper bound in (10.29) follows using the flow constructed from Pólya's urn process, described in Section 2.4 in Proposition 9.17.

Now consider the case where $x$ and $y$ are in the corners of a non-square rectangle. Suppose that $x = (a, b)$ and $y = (c, h)$, and assume without loss of generality that $a \leq c$, $b \leq h$, $(c-a) \leq (h-b)$. Assume also that $c - a$ and $h - b$ have the same parity. The line with slope $-1$ through $x$ and the line with slope $1$ through $y$ meet at the point $z$ (see Figure 10.7), where

$$ z = \left( \frac{(a+c)+(b-h)}{2}, \frac{(a-c)+(b+h)}{2} \right). $$

### PDF page 156 (book page 140)

*[Figure: a rectangular box (two cubes side by side) drawn in perspective. The bottom-front-left corner is labeled $x$ (filled dot) and the bottom-front-right corner is labeled $y$ (filled dot); the top-back-middle corner is labeled $z$ (filled dot). The bottom-front edge is divided into two segments each marked with length $k$.]*

FIGURE 10.6. If $x$ and $y$ are points of $\mathbb{Z}^d$ differing only in a single coordinate by $2k$, then a flow is constructed from $x$ to $y$ via a third vertex $z$. The point $z$ is an antipodal point to $x$ (also $y$) on the boundary of a cube of side-length $k$.

By Proposition 9.17,

$$ \mathcal{R}(y \leftrightarrow z) \leq 2 \log \left( \frac{(c-a)+(h-b)}{2} \right) \leq 2 \log(k+1), $$
$$ \mathcal{R}(z \leftrightarrow x) \leq 2 \log \left( \frac{(a-c)+(h-b)}{2} \right) \leq 2 \log(k+1). $$

By the triangle inequality for resistances (Corollary 10.8),

$$ \mathcal{R}(x \leftrightarrow y) \leq 4 \log(k+1). \tag{10.31} $$

When $(c-a)$ and $(h-b)$ have opposite parities, let $x'$ be a lattice point at unit distance from $x$ and closer to $y$. Applying the triangle inequality again shows that

$$ \mathcal{R}(x \leftrightarrow y) \leq \mathcal{R}(x \leftrightarrow x') + \mathcal{R}(x' \leftrightarrow y) \leq 1 + 4 \log(k+1) \leq 6 \log(k+1). \tag{10.32} $$

Thus (10.31) and (10.32), together with (10.27), establish the upper bound in (10.29).

$\blacksquare$

**10.7. Bounding Mixing Times via Hitting Times**

**10.7.1. Hitting Time Bound.** The goal of this section is to prove the following:

THEOREM 10.22. *Consider a finite reversible chain with transition matrix $P$ and stationary distribution $\pi$ on $\mathcal{X}$. If the chain satisfies $P(x, x) \geq 1/2$ for all $x$, then the $\ell^\infty$ mixing time (defined in (4.44)) satisfies*

$$ t_{\mathrm{mix}}^{(\infty)}(1/4) \leq 4 \max_{x \in \mathcal{X}} \mathbf{E}_\pi(\tau_x) + 1. \tag{10.33} $$

### PDF page 157 (book page 141)

*[Figure: A 9×9 grid graph (lattice). A path/flow is drawn in bold from vertex $x$ (lower middle) up-left to vertex $z$ (center-left), then a "V" shape from $z$ with one bold edge going up-right to vertex $y$ (upper right) and another bold edge going down-right toward $x$.]*

FIGURE 10.7. Constructing a flow from $x$ to $y$.

*Thus,*

$$ t_{\text{mix}}(1/4) \le t_{\text{mix}}^{(2)}(1/2) = \lceil \tfrac{1}{2} t_{\text{mix}}^{(\infty)}(1/4) \rceil \le 2 \max_{x \in \mathcal{X}} \mathbf{E}_\pi(\tau_x) + 1 \tag{10.34} $$

REMARK 10.23. Clearly, $\mathbf{E}_\pi(\tau_x) \le t_{\text{hit}}$, so the bound (10.34) implies that

$$ t_{\text{mix}} \le 2 t_{\text{hit}} + 1. \tag{10.35} $$

REMARK 10.24. Equation 10.34 may not hold if the chain is not reversible; see Exercise 10.14. However, a similar inequality for the Cesaro mixing time $t_{\text{Ces}}$ (defined in Section 6.6) does not require laziness or reversibility: as discussed in Remark 6.20,

$$ t_{\text{Ces}}(1/4) \le 4 t_{\text{hit}} + 1 $$

for any irreducible chain.

To prove Theorem 10.22, we will need a few preliminary results.

PROPOSITION 10.25. *Let $P$ be the transition matrix for a finite reversible chain on state space $\mathcal{X}$ with stationary distribution $\pi$.*

(i) *For all $t \ge 0$ and $x \in \mathcal{X}$ we have $P^{2t+2}(x,x) \le P^{2t}(x,x)$.*
(ii) *If the chain $P_L$ is lazy, that is $P_L(x,x) \ge 1/2$ for all $x$, then for all $t \ge 0$ and $x \in \mathcal{X}$ we have $P_L^{t+1}(x,x) \le P_L^t(x,x)$.*

See Exercise 12.5 for a proof using eigenvalues. Here, we give a direct proof using the Cauchy-Schwarz inequality.

PROOF. (i) Since $P^{2t+2}(x,x) = \sum_{y,z \in \mathcal{X}} P^t(x,y) P^2(y,z) P^t(z,x)$, we have

$$ \pi(x) P^{2t+2}(x,x) = \sum_{y,z \in \mathcal{X}} P^t(y,x) \pi(y) P^2(y,z) P^t(z,x) = \sum_{y,z \in \mathcal{X}} \psi(y,z) \psi(z,y), \tag{10.36} $$

where $\psi(y,z) = P^t(y,x) \sqrt{\pi(y) P^2(y,z)}$. (By Exercise 1.8, the matrix $P^2$ is reversible with respect to $\pi$.)

### PDF page 158 (book page 142)

*[Figure: A square with four corner vertices labeled $w$ (top-left), $z$ (top-right), $x$ (bottom-left), $y$ (bottom-right). On each of the four edges there is an added midpoint vertex labeled: $m_{wz}$ on the top edge, $m_{yz}$ on the right edge, $m_{xy}$ on the bottom edge, and $m_{wx}$ on the left edge.]*

FIGURE 10.8. Adding states $m_{xy}$ for each pair $x, y \in \mathcal{X}$.

By Cauchy-Schwarz, the right-hand side of (10.36) is at most

$$ \sum_{y,z \in \mathcal{X}} \psi(y,z)^2 = \sum_{y \in \mathcal{X}} [P^t(y,x)]^2 \pi(y) = \pi(x) P^{2t}(x,x). $$

(ii) Define $P = 2P_L - I$. Enlarge the state space by adding a new state $m_{xy} = m_{yx}$ for each pair of states $x, y \in \mathcal{X}$ with $P(x,y) > 0$. (See Figure 10.8.)

On the larger state space $\mathcal{X}_K$ define a transition matrix $K$ by

$$
\begin{aligned}
K(x, m_{xy}) &= P(x,y) && \text{for } x, y \in \mathcal{X}, \\
K(m_{xy}, x) &= K(m_{xy}, y) = 1/2 && \text{for } x \ne y, \\
K(m_{xx}, x) &= 1 && \text{for all } x,
\end{aligned}
$$

other transitions having $K$-probability 0. Then $K$ is reversible with stationary measure $\pi_K$ given by $\pi_K(x) = \pi(x)/2$ for $x \in \mathcal{X}$ and

$$ \pi_K(m_{xy}) = \begin{cases} \pi(x) P(x,y) & \text{if } x \ne y \\ \pi(x) \frac{P(x,x)}{2} & \text{if } x = y \end{cases}. $$

Clearly $K^2(x,y) = P_L(x,y)$ for $x, y \in \mathcal{X}$, so $K^{2t}(x,y) = P_L^t(x,y)$, and the claimed monotonicity follows. $\blacksquare$

One useful application of the augmented matrix $K$ in the proof of (ii) above is

$$ \Big| \frac{P^t(x,y)}{\pi(y)} - 1 \Big| \le \sqrt{\frac{P^t(x,x)}{\pi(x)} - 1} \sqrt{\frac{P^t(y,y)}{\pi(y)} - 1}. \tag{10.37} $$

See Exercise 10.19.

The following proposition, which does not require reversibility, relates the mean hitting time of a state $x$ to return probabilities.

PROPOSITION 10.26 (Hitting time from stationarity). *Consider a finite irreducible aperiodic chain with transition matrix $P$ with stationary distribution $\pi$ on $\mathcal{X}$. Then for any $x \in \mathcal{X}$,*

$$ \pi(x) \mathbf{E}_\pi(\tau_x) = \sum_{t=0}^{\infty} [P^t(x,x) - \pi(x)]. \tag{10.38} $$

We give two proofs, one using generating functions and one using stopping times, following (**Aldous and Fill, 1999**, Lemma 11, Chapter 2).

### PDF page 159 (book page 143)

PROOF OF PROPOSITION 10.26 VIA GENERATING FUNCTIONS. Define

$$ f_k := \mathbf{P}_\pi \{\tau_x = k\} \quad \text{and} \quad u_k := P^k(x,x) - \pi(x). $$

Since $\mathbf{P}_\pi\{\tau_x = k\} \le \mathbf{P}_\pi\{\tau_x \ge k\} \le C\alpha^k$ for some $\alpha < 1$ (see (1.18)), the power series $F(s) := \sum_{k=0}^{\infty} f_k s^k$ converges in an interval $[0, 1+\delta_1]$ for some $\delta_1 > 0$.

Also, since $|P^k(x,x) - \pi(x)| \le d(k)$ and $d(k)$ decays at least geometrically fast (Theorem 4.9), $U(s) := \sum_{k=0}^{\infty} u_k s^k$ converges in an interval $[0, 1+\delta_2]$ for some $\delta_2 > 0$. Note that $F'(1) = \sum_{k=0}^{\infty} k f_k = \mathbf{E}_\pi(\tau_x)$ and $U(1)$ equals the right-hand side of (10.38).

For every $m \ge 0$,

$$
\begin{aligned}
\pi(x) = \mathbf{P}_\pi\{X_m = x\} = \sum_{k=0}^{m} f_k P^{m-k}(x,x) &= \sum_{k=0}^{m} f_k \left[ \left( P^{m-k}(x,x) - \pi(x) \right) + \pi(x) \right] \\
&= \sum_{k=0}^{m} f_k [u_{m-k} + \pi(x)].
\end{aligned}
$$

Thus, the constant sequence with every element equal to $\pi(x)$ is the convolution of the sequence $\{f_k\}_{k=0}^{\infty}$ with the sequence $\{u_k + \pi(x)\}_{k=0}^{\infty}$, so its generating function $\sum_{m=0}^{\infty} \pi(x) s^m = \pi(x)(1-s)^{-1}$ equals the product of the generating function $F$ with the generating function

$$ \sum_{m=0}^{\infty} [u_m + \pi(x)] s^m = U(s) + \pi(x) \sum_{m=0}^{\infty} s^m = U(S) + \frac{\pi(x)}{1-s}. $$

(See Exercise 10.10.) That is, for $0 < s < 1$,

$$ \frac{\pi(x)}{1-s} = \sum_{m=0}^{\infty} \pi(x) s^m = F(s) \left[ U(s) + \frac{\pi(x)}{1-s} \right], $$

and multiplying by $1-s$ gives $\pi(x) = F(s)[(1-s)U(s) + \pi(x)]$, which clearly holds also for $s = 1$. Differentiating the last equation from the left at $s = 1$, we obtain that $0 = F'(1)\pi(x) - U(1)$, and this is equivalent to (10.38). $\blacksquare$

PROOF OF PROPOSITION 10.26 VIA STOPPING TIMES. Define

$$ \tau_x^{(m)} := \min\{t \ge m : X_t = x\}, $$

and write $\mu_m := P^m(x, \cdot)$. By the Convergence Theorem (Theorem 4.9), $\mu_m$ tends to $\pi$ as $m \to \infty$. By Lemma 10.5, we can represent the expected number of visits to $x$ before time $\tau_x^{(m)}$ as

$$ \sum_{k=0}^{m-1} P^k(x,x) = \pi(x) \mathbf{E}_x\left( \tau_x^{(m)} \right) = \pi(x)[m + \mathbf{E}_{\mu_m}(\tau_x)]. $$

Thus $\sum_{k=0}^{m-1} [P^k(x,x) - \pi(x)] = \pi(x) \mathbf{E}_{\mu_m}(\tau_x)$.

Taking $m \to \infty$ completes the proof. $\blacksquare$

We are now able to prove Theorem 10.22.

PROOF OF THEOREM 10.22. By the identity (10.38) in Proposition 10.26 and the monotonicity in Proposition 10.25(ii), for any $t > 0$ we have

$$ \pi(x) \mathbf{E}_\pi(\tau_x) \ge \sum_{k=1}^{t} [P^k(x,x) - \pi(x)] \ge t[P^t(x,x) - \pi(x)]. $$

### PDF page 160 (book page 144)

Dividing by $t\,\pi(x)$

$$ \frac{\mathbf{E}_\pi\left(\tau_x\right)}{t} \geq \left| \frac{P^t(x,x)}{\pi(x)} - 1 \right| . $$

Therefore, by (10.37),

$$ \max_x \frac{\mathbf{E}_\pi\left(\tau_x\right)}{t} \geq \max_x \left| \frac{P^t(x,x)}{\pi(x)} - 1 \right| $$
$$ = \max_{x,y} \sqrt{\frac{P^t(x,x)}{\pi(x)} - 1}\sqrt{\frac{P^t(y,y)}{\pi(y)} - 1} $$
$$ \geq \max_{x,y} \left| \frac{P^t(x,y)}{\pi(y)} - 1 \right| = d^{(\infty)}(t) . $$

Thus the left-hand side is less than $1/4$ for $t \geq \max_x 4\mathbf{E}_\pi(\tau_x)$. $\blacksquare$

EXAMPLE 10.27 (Lazy random walk on the cycle). In Section 5.3.2 we proved that $t_{\mathrm{mix}} \leq n^2$ for the lazy random walk on the cycle $\mathbb{Z}_n$. However, Theorem 10.22 can also be used.

Label the states of $\mathbb{Z}_n$ with $\{0, 1, \ldots, n-1\}$. By identifying the states $0$ and $n$, we can see that $\mathbf{E}_k(\tau_0)$ for the lazy simple random walk on the cycle must be the same as the expected time to ruin or success in a lazy gambler's ruin on the path $\{0, 1, \ldots, n\}$. Hence, for lazy simple random walk on the cycle, Exercise 2.1 implies

$$ t_{\mathrm{hit}} = \max_{x,y}\mathbf{E}_x(\tau_y) = \max_{0 \leq k \leq n} 2k(n-k) = \left\lfloor \frac{n^2}{2} \right\rfloor . $$

(The factor of 2 comes from the laziness.) Therefore, (10.35) gives

$$ t_{\mathrm{mix}} \leq n^2 + 1. $$

PROPOSITION 10.28.

(a) *For lazy random walk on a simple graph with $m$ edges and $n$ vertices,*

$$ t_{\mathrm{hit}} \leq 4nm \leq 2n^3 \,, $$

*and*

$$ t_{\mathrm{mix}}^{(\infty)} \leq 16nm + 1 \leq 8n^3 \,, \ \ so \ \ t_{\mathrm{mix}} \leq 8nm + 1 \leq 4n^3 \,. $$

(b) *For lazy random walk on a $d$-regular graph with $n$ vertices,*

$$ t_{\mathrm{mix}}^{(\infty)} \leq 24n^2 - 7nd \,, \ \ so \ \ t_{\mathrm{mix}} \leq 12n^2 \,. $$

PROOF. Since $t_{\mathrm{hit}} \leq \max_{a,b} t_{a \leftrightarrow b}$, this result follows from Proposition 10.16 together with Theorem 10.22. (The extra factor of 2 comes from the laziness of the walk.) $\blacksquare$

### 10.8. Mixing for the Walk on Two Glued Graphs

For a graph $G = (V, E)$ and a vertex $v_\star \in V$, we consider the graph $H$ obtained by glueing two copies of $G$ at $v_\star$. See Figure 7.2 for an example. More precisely, the vertex set of $H$ is

$$ W = \{(v, i) \,:\, v \in V, \ i \in \{1, 2\}\}, \tag{10.39} $$

with the elements $(v_\star, 1)$ and $(v_\star, 2)$ identified. The edge set of $H$ is

$$ \{\{(v, i), (w, j)\} \,:\, \{v, w\} \in E, \ i = j\}. \tag{10.40} $$

We state the main result of this section:

### PDF page 161 (book page 145)

PROPOSITION 10.29. *Let $H$ be the graph obtained by gluing together two copies of $G$ at the vertex $v_\star$ as defined above. Let $\tau_{\mathrm{couple}}^G$ be the time for a coupling of two random walks on $G$ to meet. Then there is a coupling of two random walks on $H$ which has a coupling time $\tau_{\mathrm{couple}}^H$ satisfying*

$$ \max_{u,v \in H} \mathbf{E}_{u,v}\left(\tau_{\mathrm{couple}}^H\right) \leq \max_{x,y \in G}\mathbf{E}_{x,y}\left(\tau_{\mathrm{couple}}^G\right) + \max_{x \in G}\mathbf{E}_x\left(\tau_{v_\star}^G\right) . \tag{10.41} $$

*(Here $\tau_{v_\star}^G$ is the hitting time of $v_\star$ in the graph $G$.)*

OUTLINE OF PROOF. Given a starting point in $H$, a random walk in $G$ can be lifted to a random walk in $H$ in a unique way. (At $v_\star$, the particle moves to each copy with equal probability.) Applying this lifting to the given coupling in $G$ yields a coupling in $H$ where at time $\tau_{\mathrm{couple}}^G$ the particles have either met or are at corresponding vertices in the two copies. From there after, move the particles in parallel until they hit $v_\star$. $\blacksquare$

Solved Exercise 10.21 asks to provide the details.

We can now return to the example mentioned in this chapter's introduction:

COROLLARY 10.30. *Consider the lazy random walk on the graph $H$ obtained by gluing two copies of the discrete torus $\mathbb{Z}_n^d$ at a single vertex. (See Example 7.5 and in particular Figure 7.2.)*

(i) *For $d \geq 3$, there are constants $c_d$ and $C_d$ such that*

$$ c_d n^d \leq t_{\mathrm{mix}} \leq C_d n^d . \tag{10.42} $$

(ii) *For $d = 2$, there are constants $c_2, C_2$ such that*

$$ c_2 n^2 \log n \leq t_{\mathrm{mix}} \leq C_2 n^2 \log n . \tag{10.43} $$

Before we prove this, we state the following general lemma on hitting times.

LEMMA 10.31. *For $y \in \mathcal{X}$, let $H_y := \max_{x \in \mathcal{X}} \mathbf{E}_x(\tau_y)$. For every $\varepsilon > 0$, there exists $x \in \mathcal{X}$ such that*

$$ \mathbf{P}_x\left\{\tau_y \leq \frac{\varepsilon}{3}H_y\right\} < \varepsilon . \tag{10.44} $$

PROOF. The main step is to show that for any integer $T \geq 1$, if

$$ \mathbf{P}_x\{\tau_y \leq T\} \geq \varepsilon \ \ \text{for all} \ \ x \in \mathcal{X} , \tag{10.45} $$

then $H_y \leq T/\varepsilon$. Indeed, (10.45) implies, by induction, that for all $k \geq 1$,

$$ \mathbf{P}_x\{\tau_y > kT\} \leq (1 - \varepsilon)^k . $$

Therefore, for every $x \in \mathcal{X}$,

$$ \mathbf{E}_x(\tau_y) = \sum_{m=0}^{\infty} \mathbf{P}_x\{\tau_y > m\} \leq \sum_{k=0}^{\infty} T\mathbf{P}_x\{\tau_y > kT\} \leq T\sum_{k=0}^{\infty}(1 - \varepsilon)^k = T/\varepsilon . $$

Thus $H_y \leq T/\varepsilon$. To prove (10.44), we may assume that $\frac{\varepsilon}{3}H_y \geq 1$ (otherwise (10.44) trivially holds for any $x \neq y$). Suppose there exists $\varepsilon > 0$ such that for all $x$, (10.44) fails. Then $T := \left\lceil \frac{\varepsilon}{3}H_y \right\rceil$ satisfies (10.45), so we obtain the contradiction

$$ H_y \leq \frac{T}{\varepsilon} \leq \frac{H_y}{3} + \frac{1}{\varepsilon} \leq \frac{2}{3}H_y . $$

$\blacksquare$

### PDF page 162 (book page 146)

PROOF OF COROLLARY 10.30.

*Proof of upper bound in* (10.42). Using Proposition 10.29 with the bound for $d \geq 3$ in Proposition 10.21 and (5.9) gives

$$ \max_{x,y \in H} \mathbf{E}_{x.y}(\tau_{\mathrm{couple}}) \leq C_d n^d . \tag{10.46} $$

The bound on $t_{\mathrm{mix}}$ follows from Theorem 5.4.

The lower bound in (10.42) was already proven in Example 7.5.

*Proof of lower bound in* (10.43). Recalling that $v_\star$ is the vertex where the two tori are attached, by Proposition 10.21 and Lemma 10.31, there exists a $x \in \mathcal{X}$ and a constant $c_1$ such that

$$ \mathbf{P}_x\{\tau_{v_\star} > c_2 n^2 \log n\} \geq \tfrac{7}{8} . $$

If $A$ is the set of vertices in the torus not containing $x$, and $t \leq c_2 n^2 \log n$, then

$$ \mathbf{P}_x\{X_t \in A\} \leq \mathbf{P}_x\{\tau_{v_\star} \leq t\} \leq \frac{1}{8} . $$

On the other hand, $\pi(A) \geq 1/2$. We conclude that for $t \leq c_2 n^2 \log n$,

$$ \left\|P^t(x, \cdot) - \pi\right\|_{\mathrm{TV}} \geq \pi(A) - P^t(x, A) \geq \frac{1}{2} - \frac{1}{8} = \frac{3}{8}, $$

whence $t_{\mathrm{mix}} \geq c_2 n^2 \log n$.

*Proof of upper bound in* (10.43). Applying Proposition 10.29, using the bounds in Proposition 10.21 and the bound (5.9) for the coupling on the torus used in Theorem 5.6 shows that there is a coupling with

$$ \max_{x,y \in H} \mathbf{E}_{x,y}(\tau_{\mathrm{couple}}) \leq C_2 n^2 \log n. \tag{10.47} $$

Applying Theorem 5.4 again proves the right-hand inequality in (10.43).

$\blacksquare$

### Exercises

EXERCISE 10.1. Prove Lemma 10.5 by copying the proof in Proposition 1.14, substituting $\rho$ in place of $\tilde{\pi}$.

EXERCISE 10.2. Is the expected waiting time for the sequence $TTT$ to appear in a sequence of fair coin tosses the same as the waiting time for the sequence $HTH$?

EXERCISE 10.3. Let $G$ be a connected graph on at least 3 vertices in which the vertex $v$ has only one neighbor, namely $w$. Show that the simple random walk on $G$ satisfies $\mathbf{E}_v\tau_w \neq \mathbf{E}_w\tau_v$.

EXERCISE 10.4. Consider simple random walk on the binary tree of depth $k$ with $n = 2^{k+1} - 1$ vertices (first defined in Section 5.3.4).

(a) Let $a$ and $b$ be two vertices at level $m$ whose most recent common ancestor $c$ is at level $h < m$. Find $\mathbf{E}_a\tau_b$.

(b) Show that the maximal value of $\mathbf{E}_a\tau_b$ is achieved when $a$ and $b$ are leaves whose most recent common ancestor is the root of the tree.

EXERCISE 10.5. In a directed graph $G$, an Eulerian cycle is a directed cycle which contains every edge of $G$ exactly once. Show that $G$ is Eulerian (as defined in the beginning of Section 10.5) if and only if it contains an Eulerian cycle.

### PDF page 163 (book page 147)

EXERCISE 10.6. Let $\mathbf{0} = (0, 0, \ldots, 0)$ be the all-zero vector in the $m$-dimensional hypercube $\{0, 1\}^m$, and let $v$ be a vertex with Hamming weight $k$. Write $h_m(k)$ for the expected hitting time from $v$ to $\mathbf{0}$ for simple (that is, not lazy) random walk on the hypercube. Determine $h_m(1)$ and $h_m(m)$. Deduce that both $\min_{k>0} h_m(k)$ and $\max_{k>0} h_m(k)$ are asymptotic to $2^m$ as $m$ tends to infinity. (We say that $f(m)$ is asymptotic to $g(m)$ if their ratio tends to 1.)

*Hint*: Consider the multigraph $G_m$ obtained by gluing together all vertices of Hamming weight $k$ for each $k$ between 1 and $m - 1$. This is a graph on the vertex set $\{0, 1, 2, \ldots, m\}$ with $k\binom{m}{k}$ edges from $k - 1$ to $k$.

EXERCISE 10.7. Use Proposition 10.29 to bound the mixing time for two hypercubes identified at a single vertex. Prove a lower bound of the same order.

EXERCISE 10.8. Let $(X_t)$ be a random walk on a network with conductances $\{c_e\}$. Show that

$$\mathbf{E}_a(\tau_{bca}) = [\mathcal{R}(a \leftrightarrow b) + \mathcal{R}(b \leftrightarrow c) + \mathcal{R}(c \leftrightarrow a)] \sum_{e \in E} c_e,$$

where $\tau_{bca}$ is the first time that the sequence $(b, c, a)$ appears as a subsequence of $(X_1, X_2, \ldots)$.

EXERCISE 10.9. Show that for a random walk $(X_t)$ on a network, for every three vertices $a, x, z$,

$$\mathbf{P}_x\{\tau_z < \tau_a\} = \frac{\mathcal{R}(a \leftrightarrow x) - \mathcal{R}(x \leftrightarrow z) + \mathcal{R}(a \leftrightarrow z)}{2\mathcal{R}(a \leftrightarrow z)}.$$

*Hint:* Run the chain from $x$ until it first visits $a$ and then $z$. This will also be the first visit to $z$ from $x$, unless $\tau_z < \tau_a$. In the latter case the path from $x$ to $a$ to $z$ involves an extra commute from $z$ to $a$ beyond time $\tau_z$. Thus, starting from $x$ we have

$$\tau_{az} = \tau_z + \mathbf{1}_{\{\tau_z < \tau_a\}}\tau'_{az}, \tag{10.48}$$

where the variable $\tau'_{az}$ refers to the chain starting from its first visit to $z$. Now take expectations and use the cycle identity (Lemma 10.12).

EXERCISE 10.10. Suppose that $\{a_k\}$ is a sequence with generating function $A(s) := \sum_{k=0}^{\infty} a_k s^k$ and $\{b_k\}$ is a sequence with generating function $B(s) := \sum_{k=0}^{\infty} b_k s^k$. Let $\{c_k\}$ be the sequence defined as $c_k := \sum_{j=0}^{k} a_j b_{k-j}$, called the **convolution** of $\{a_k\}$ and $\{b_k\}$. Show that the generating function of $\{c_k\}$ equals $A(s)B(s)$.

EXERCISE 10.11. Let $\tau_x^\sharp$ denote the first even time that the Markov chain visits $x$. Prove that the inequality

$$t_{\mathrm{mix}}(1/4) \leq 8 \max_{x \in \mathcal{X}} \mathbf{E}_\pi\left(\tau_x^\sharp\right) + 1$$

holds without assuming the chain is lazy (cf. Theorem 10.22).

EXERCISE 10.12. Show that for simple random walk (not lazy) on the $n$-cycle $\mathbb{Z}_n$, with $n$ odd, $t_{\mathrm{mix}} = O(n^2)$.

*Hint:* Use Exercise 10.11.

### PDF page 164 (book page 148)

EXERCISE 10.13. Consider a lazy biased random walk on the $n$-cycle. That is, at each time $t \geq 1$, the particle walks one step clockwise with probability $p \in (1/4, 1/2)$, stays put with probability $1/2$, and walks one step counterclockwise with probability $1/2 - p$.

Show that $t_{\mathrm{mix}}(1/4)$ is bounded above and below by constant multiples of $n^2$, but $t_{\mathrm{Ces}}(1/4)$ is bounded above and below by constant multiples of $n$.

EXERCISE 10.14. Show that equation (10.34) may not hold if the chain is not reversible.

*Hint:* Consider the lazy biased random walk on the cycle.

EXERCISE 10.15. Suppose that $\tau$ is a strong stationary time for simple random walk started at the vertex $v$ on the graph $G$. Let $H$ consist of two copies $G_1$ and $G_2$ of $G$, glued at $v$. Note that $\deg_H(v) = 2 \deg_G(v)$. Let $\tau_v$ be the hitting time of $v$:

$$\tau_v = \min\{t \geq 0 \ : \ X_t = v\}.$$

Show that starting from any vertex $x$ in $H$, the random time $\tau_v + \tau$ is a strong stationary time for $H$ (where $\tau$ is applied to the walk after it hits $v$).

REMARK 10.32. It is also instructive to give a general direct argument controlling mixing time in the graph $H$ described in Exercise 10.15:

Let $h_{\max}$ be the maximum expected hitting time of $v$ in $G$, maximized over starting vertices. For $t > 2kh_{\max} + t_{\mathrm{mix}G}(\varepsilon)$ we have in $H$ that

$$|P^t(x, A) - \pi(A)| < 2^{-k} + \varepsilon. \tag{10.49}$$

Indeed for all $x$ in $H$, we have $\mathbf{P}_x\{\tau_v > 2h_{\max}\} < 1/2$ and iterating, $\mathbf{P}_x\{\tau_v > 2kh_{\max}\} < (1/2)^k$. On the other hand, conditioning on $\tau_v < 2kh_{\max}$, the bound (10.49) follows from considering the projected walk.

EXERCISE 10.16. Give a sequence of graphs with maximum degree bounded by $d$ such that $t_{\mathrm{hit}}/t_{\odot} \to \infty$.

*Hint:* Consider a cube $[-k, k]^3 \cap \mathbb{Z}^3$ with a path segment attached.

EXERCISE 10.17. Consider an irreducible Markov chain $P$ on the state space $\mathcal{X} = \{1, 2, \ldots, n\}$, where $n > 1$, and let $H_{i,j} = \mathbf{E}_i\tau_j$. The purpose of this exercise is to show that the $P$ is determined by the matrix $H$. Let $\mathbf{1}$ be the column vector with all entries equal to 1. Let $D$ be the diagonal matrix with $i$-th diagonal entry $1/\pi_i$. The superscript $T$ denotes the transpose operation.

(a) Show that $H\pi^T = c\mathbf{1}$ for some constant $c$.
(b) Show that $(P - I)H = D - \mathbf{1}\mathbf{1}^T$.
(c) Show that $H$ is invertible.

EXERCISE 10.18. Prove that for $d \geq 3$,

$$\sum_{j=1}^{\infty} \binom{j + d - 1}{d - 1}^{-1} = \frac{1}{d - 2}.$$

EXERCISE 10.19. Prove that for a lazy reversible chain,

$$\left|\frac{P^t(x, y)}{\pi(y)} - 1\right| \leq \sqrt{\left(\frac{P^t(x, x)}{\pi(x)} - 1\right)\left(\frac{P^t(y, y)}{\pi(y)} - 1\right)}. \tag{10.50}$$

*Hint:* Use the augmented transition kernel $K$ in the proof of Proposition 10.25(ii).

### PDF page 165 (book page 149)

EXERCISE 10.20. Let $G = (V, E)$ be a connected simple graph with $n$ vertices. Let $\mathcal{R}(e)$ denote the effective resistance between the vertices of the edge $e$. Prove Foster's Identity,

$$\sum_{e \in E} \mathcal{R}(e) = n - 1. \tag{10.51}$$

*Hint:* Use the identity

$$\sum_{\{x,y\} \in E} t_{x \leftrightarrow y} = \sum_x \sum_{y \, : \, y \sim x} \mathbf{E}_y \tau_x = \sum_x d(x)(\mathbf{E}_x \tau_x^+ - 1).$$

EXERCISE 10.21. Provide the details for the proof of Proposition 10.29.

EXERCISE 10.22. Let $A \subset \mathcal{X}$ be a set which is accessible from all states.

(a) Show that all the hitting times $h_{x,A} = \mathbf{E}_x \tau_A$ for a target set $A$ are determined by the linear equations

$$h_{x,A} = 1 + \sum_y P(x, y)h_{y,A} \quad \text{for } x \notin A$$

with the boundary conditions $h_{a,A} = 0$ for all $a \in A$.
(b) Show that there exists a unique solution to these equations.

&nbsp;&nbsp;&nbsp;&nbsp;*Hint:* A function which is harmonic on $\mathcal{X} \setminus A$ and vanishes on $A$ is identically zero.

**Notes**

The commute time identity appears in **Chandra, Raghavan, Ruzzo, Smolensky, and Tiwari (1996)**.

Theorem 10.22 is a simplified version of Lemma 15 in **Aldous and Fill (1999**, Chapter 4), which bounds $t_{\mathrm{mix}}$ by $O(t_{\odot})$.

A graph similar to our glued tori was analyzed in **Saloff-Coste (1997**, Section 3.2) using other methods. This graph originated in **Diaconis and Saloff-Coste (1996a**, Remark 6.1).

Lemma 10.12 is from **Coppersmith, Tetali, and Winkler (1993)**. See **Tetali (1999)** for related results.

Theorem 10.22 was stated for total-variation mixing time in the first edition of this book, although the proof yielded a bound on the $\ell^\infty$ mixing time. This is explicitly stated in the current edition.

Another proof of Proposition 10.28 is given in **Lyons and Oveis Gharan (2012)**.

**Doyle and Steiner (2011)** proved a variational principle which implies the following: Given any irreducible Markov chain $P$ with state space $\mathcal{X}$, let $\hat{P}$ be its time-reversal and call $\tilde{P} = (P + \hat{P})/2$ the *symmetrization* of $P$. Then symmetrization cannot decrease commute times, i.e., for every $x, y \in \mathcal{X}$,

$$t_{x \leftrightarrow y}^P \leq t_{x \leftrightarrow y}^{\tilde{P}}. \tag{10.52}$$

Exercise 2.122 in **Lyons and Peres (2016)** outlines their approach. Other proofs of (10.52) were given by **Gaudillière and Landim (2014)** and **Balázs and Folly (2016)**.

The connection between hitting and mixing times is further discussed in Chapter 24.

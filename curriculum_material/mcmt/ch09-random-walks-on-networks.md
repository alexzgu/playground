# Chapter 9 — Random Walks on Networks
*(PDF pages 132–143; book pages 116–127)*

### PDF page 132 (book page 116)

CHAPTER 9

# Random Walks on Networks

**9.1. Networks and Reversible Markov Chains**

Electrical networks provide a different language for reversible Markov chains. This point of view is useful because of the insight gained from the familiar physical laws of electrical networks.

A ***network*** is a finite undirected connected graph $G$ with vertex set $V$ and edge set $E$, endowed additionally with non-negative numbers $\{c(e)\}$, called ***conductances***, that are associated to the edges of $G$. We often write $c(x, y)$ for $c(\{x, y\})$; clearly $c(x, y) = c(y, x)$. The reciprocal $r(e) = 1/c(e)$ is called the ***resistance*** of the edge $e$.

A network will be denoted by the pair $(G, \{c(e)\})$. Vertices of $G$ are often called ***nodes***. For $x, y \in V$, we will write $x \sim y$ to indicate that $\{x, y\}$ belongs to $E$.

Consider the Markov chain on the nodes of $G$ with transition matrix

$$ P(x, y) = \frac{c(x, y)}{c(x)}, \tag{9.1} $$

where $c(x) = \sum_{y \,:\, y \sim x} c(x, y)$. This process is called the ***weighted random walk*** on $G$ with edge conductances $\{c(e)\}$, or the Markov chain associated to the network $(G, \{c(e)\})$. This Markov chain is reversible with respect to the probability $\pi$ defined by $\pi(x) := c(x)/c_G$, where $c_G = \sum_{x \in V} c(x)$:

$$ \pi(x)P(x, y) = \frac{c(x)}{c_G} \frac{c(x, y)}{c(x)} = \frac{c(y)}{c_G} \frac{c(y, x)}{c(y)} = \pi(y)P(y, x). $$

By Proposition 1.20, $\pi$ is stationary for $P$. Note that

$$ c_G = \sum_{x \in V} \sum_{\substack{y \in V \\ y \sim x}} c(x, y). $$

In the case that the graph has no loops, we have

$$ c_G = 2 \sum_{e \in E} c(e). $$

Simple random walk on $G$ is the special case where all the edge weights are equal to 1.

We now show that every reversible Markov chain is a weighted random walk on a network. Suppose $P$ is a transition matrix on a finite set $\mathcal{X}$ which is reversible with respect to the probability $\pi$ (that is, (1.29) holds). Define a graph with vertex set $\mathcal{X}$ by declaring $\{x, y\}$ an edge if $P(x, y) > 0$. This is a proper definition, since reversibility implies that $P(x, y) > 0$ exactly when $P(y, x) > 0$. Next, define conductances on edges by $c(x, y) = \pi(x)P(x, y)$. This is symmetric by reversibility. With this choice of weights, we have $c(x) = \pi(x)$, and thus the transition matrix

### PDF page 133 (book page 117)

associated with this network is just $P$. The study of reversible Markov chains is thus equivalent to the study of random walks on networks.

**9.2. Harmonic Functions**

We assume throughout this section that $P$ is the transition matrix of an irreducible Markov chain with state space $\mathcal{X}$. We do *not* assume in this section that $P$ is reversible; indeed, Proposition 9.1 is true for all irreducible chains.

Recall from Section 1.5.4 that we call a function $h : \mathcal{X} \to \mathbb{R}$ ***harmonic*** for $P$ at a vertex $x$ if

$$ h(x) = \sum_{y \in \mathcal{X}} P(x,y) h(y). \tag{9.2} $$

When $P$ is the transition matrix for a simple random walk on a graph, (9.2) means that $h(x)$ is the average of the values of $h$ at neighboring vertices.

Recall that when $B$ is a set of states, we define the hitting time $\tau_B$ by $\tau_B = \min\{t \geq 0 \, : \, X_t \in B\}$.

**PROPOSITION 9.1.** *Let $(X_t)$ be a Markov chain with irreducible transition matrix $P$, let $B \subset \mathcal{X}$, and let $h_B : B \to \mathbb{R}$ be a function defined on $B$. The function $h : \mathcal{X} \to \mathbb{R}$ defined by $h(x) := \mathbf{E}_x h_B(X_{\tau_B})$ is the unique extension $h$ of $h_B$ to $\mathcal{X}$ such that $h(x) = h_B(x)$ for all $x \in B$, and $h$ is harmonic for $P$ at all $x \in \mathcal{X} \setminus B$.*

**REMARK 9.2.** The proof of uniqueness below, derived from the maximum principle, should remind you of that of Lemma 1.16.

*PROOF.* We first show that $h(x) = \mathbf{E}_x h(X_{\tau_B})$ is a harmonic extension of $h_B$. Clearly $h(x) = h_B(x)$ for all $x \in B$. Suppose that $x \in \mathcal{X} \setminus B$. Then

$$ h(x) = \mathbf{E}_x h(X_{\tau_B}) = \sum_{y \in \mathcal{X}} P(x,y) \mathbf{E}_x[h(X_{\tau_B}) \mid X_1 = y]. \tag{9.3} $$

Observe that $x \in \mathcal{X} \setminus B$ implies that $\tau_B \geq 1$. By the Markov property, it follows that

$$ \mathbf{E}_x[h(X_{\tau_B}) \mid X_1 = y] = \mathbf{E}_y h(X_{\tau_B}) = h(y). \tag{9.4} $$

Substituting (9.4) in (9.3) shows that $h$ is harmonic at $x$.

We now show uniqueness. Suppose $g : \mathcal{X} \to \mathbb{R}$ is a function which is harmonic on $\mathcal{X} \setminus B$ and satisfies $g(x) = 0$ for all $x \in B$. We first show that $g \leq 0$. Define

$$ A := \left\{ u \in \mathcal{X} \, : \, g(u) = \max_{\mathcal{X}} g \right\}. $$

Fix $x \in A$. If $x \in B$ then $g \leq 0$ on $\mathcal{X}$, so we may assume that $x \notin B$. Suppose that $P(x,y) > 0$. Harmonicity of $g$ on $\mathcal{X} \setminus B$ implies that

$$ g(x) = \sum_{z \in \mathcal{X}} g(z) P(x,z) = g(y) P(x,y) + \sum_{z \in \mathcal{X} \setminus \{y\}} g(z) P(x,z) \, . $$

If $g(y) < g(x)$ this would yield a contradiction, so we infer that $y \in A$.

By irreducibility, there exists a sequence of states $y_0, y_1, \ldots, y_r$ such that $y_0 = x$ and $y_r \in B$, each $y_i \notin B$ for $i < r$, and $P(y_{i-1}, y_i) > 0$ for $i = 1, 2, \ldots, r$. Therefore, each $y_i \in A$; in particular, $y_r \in A$. Since $g(y_r) = 0$, it follows that $\max_{\mathcal{X}} g = 0$. Applying this argument to $-g$ shows that $\min_{\mathcal{X}} g \geq 0$, whence $g \equiv 0$ on $\mathcal{X}$.

Now, if $h$ and $\tilde{h}$ are both harmonic on $\mathcal{X} \setminus B$ and agree on $B$, then the difference $h - \tilde{h}$ is harmonic on $\mathcal{X} \setminus B$ and vanishes on $B$. Therefore, $h(x) - \tilde{h}(x) = 0$ for all $x \in \mathcal{X}$. $\blacksquare$

### PDF page 134 (book page 118)

**REMARK 9.3.** Note that requiring $h$ to be harmonic on $\mathcal{X} \setminus B$ yields a system of $|\mathcal{X}| - |B|$ linear equations in the $|\mathcal{X}| - |B|$ unknowns $\{h(x)\}_{x \in \mathcal{X} \setminus B}$. For such a system of equations, existence of a solution implies uniqueness.

**9.3. Voltages and Current Flows**

Consider a network $(G, \{c(e)\})$. We distinguish two nodes, $a$ and $z$, which are called the ***source*** and the ***sink*** of the network. A function $W$ which is harmonic on $V \setminus \{a, z\}$ will be called a ***voltage***. Proposition 9.1 implies that a voltage is completely determined by its boundary values $W(a)$ and $W(z)$.

An ***oriented edge*** $\overrightarrow{e} = \overrightarrow{xy}$ is an *ordered* pair of nodes $(x, y)$. A ***flow*** $\theta$ is a function on oriented edges which is antisymmetric, meaning that $\theta(\overrightarrow{xy}) = -\theta(\overrightarrow{yx})$. For a flow $\theta$, define the ***divergence*** of $\theta$ at $x$ by

$$ \operatorname{div} \theta(x) := \sum_{y \, : \, y \sim x} \theta(\overrightarrow{xy}). $$

We note that for any flow $\theta$ we have

$$ \sum_{x \in V} \operatorname{div} \theta(x) = \sum_{x \in V} \sum_{y \, : \, y \sim x} \theta(\overrightarrow{xy}) = \sum_{\{x,y\} \in E} [\theta(\overrightarrow{xy}) + \theta(\overrightarrow{yx})] = 0. \tag{9.5} $$

A ***flow from*** $a$ ***to*** $z$ is a flow $\theta$ satisfying

(i) ***Kirchhoff's node law***:

$$ \operatorname{div} \theta(x) = 0 \quad \text{at all } x \notin \{a, z\}, \tag{9.6} $$

and

(ii) $\operatorname{div} \theta(a) \geq 0$.

Note that (9.6) is the requirement that "flow in equals flow out" for any node not $a$ or $z$.

We define the ***strength*** of a flow $\theta$ from $a$ to $z$ to be $\|\theta\| := \operatorname{div} \theta(a)$. A ***unit flow*** from $a$ to $z$ is a flow from $a$ to $z$ with strength 1. Observe that (9.5) implies that $\operatorname{div} \theta(a) = - \operatorname{div} \theta(z)$.

Observe that it is only flows that are defined on oriented edges. Conductance and resistance are defined for unoriented edges. We may of course define them (for future notational convenience) on oriented edges by $c(\overrightarrow{xy}) = c(\overrightarrow{yx}) = c(x,y)$ and $r(\overrightarrow{xy}) = r(\overrightarrow{yx}) = r(x,y)$.

Given a voltage $W$ on the network, the ***current flow*** $I$ associated with $W$ is defined on oriented edges by

$$ I(\overrightarrow{xy}) = \frac{W(x) - W(y)}{r(\overrightarrow{xy})} = c(\overrightarrow{xy}) \left[ W(x) - W(y) \right]. \tag{9.7} $$

Since $I$ is clearly antisymmetric, to verify that $I$ is a flow, it suffices to check that it obeys the node law (9.6) at every $x \notin \{a, z\}$:

$$ \sum_{y \, : \, y \sim x} I(\overrightarrow{xy}) = \sum_{y \, : \, y \sim x} c(x,y)[W(x) - W(y)] $$
$$ = c(x)W(x) - c(x) \sum_{y \, : \, y \sim x} W(y) P(x,y) = 0. $$

The definition (9.7) immediately implies that the current flow satisfies ***Ohm's law***:

$$ r(\overrightarrow{xy}) I(\overrightarrow{xy}) = W(x) - W(y). \tag{9.8} $$

### PDF page 135 (book page 119)

It is easy to see that there is a unique unit current flow; this also follows from Proposition 9.4.

Finally, a current flow also satisfies the ***cycle law***. If the oriented edges $\overrightarrow{e_1}, \ldots, \overrightarrow{e_m}$ form an oriented cycle (i.e., for some $x_0, \ldots, x_{m-1} \in V$ we have $\overrightarrow{e_i} = (x_{i-1}, x_i)$, where $x_m = x_0$), then

$$ \sum_{i=1}^{m} r(\overrightarrow{e_i}) I(\overrightarrow{e_i}) = \sum_{i=1}^{m} [W(x_{i-1}) - W(x_i)] = 0 \, . \tag{9.9} $$

Notice that adding a constant to all values of a voltage affects neither its harmonicity nor the current flow it determines. Hence we may, without loss of generality, assume our voltage function $W$ satisfies $W(z) = 0$. Such a voltage function is uniquely determined by $W(a)$.

**PROPOSITION 9.4** (Node law/cycle law/strength). *If $\theta$ is a flow from $a$ to $z$ satisfying the cycle law*

$$ \sum_{i=1}^{m} r(\overrightarrow{e_i}) \theta(\overrightarrow{e_i}) = 0 \tag{9.10} $$

*for any cycle $\overrightarrow{e_1}, \ldots, \overrightarrow{e_m}$ and if $\|\theta\| = \|I\|$, then $\theta = I$.*

*PROOF.* The function $f = \theta - I$ satisfies the node law at all nodes and the cycle law. Suppose $f(\overrightarrow{e_1}) > 0$ for some oriented edge $\overrightarrow{e_1}$. By the node law, $e_1$ must lead to some oriented edge $\overrightarrow{e_2}$ with $f(\overrightarrow{e_2}) > 0$. Iterate this process to obtain a sequence of oriented edges on which $f$ is strictly positive. Since the underlying network is finite, this sequence must eventually revisit a node. The resulting cycle violates the cycle law. $\blacksquare$

**9.4. Effective Resistance**

Given a network, the ratio $[W(a) - W(z)]/\|I\|$, where $I$ is the current flow corresponding to the voltage $W$, is independent of the voltage $W$ applied to the network. Define the ***effective resistance*** between vertices $a$ and $z$ by

$$ \mathcal{R}(a \leftrightarrow z) := \frac{W(a) - W(z)}{\|I\|}. \tag{9.11} $$

In parallel with our earlier definitions, we also define the ***effective conductance*** $\mathcal{C}(a \leftrightarrow z) = 1/\mathcal{R}(a \leftrightarrow z)$. Why is $\mathcal{R}(a \leftrightarrow z)$ called the "effective resistance" of the network? Imagine replacing our entire network by a single edge joining $a$ to $z$ with resistance $\mathcal{R}(a \leftrightarrow z)$. If we now apply the same voltage to $a$ and $z$ in both networks, then the amount of current flowing from $a$ to $z$ in the single-edge network is the same as in the original.

Next, we discuss the connection between effective resistance and the ***escape probability*** $\mathbf{P}_a\{\tau_z < \tau_a^+\}$ that a walker started at $a$ hits $z$ before returning to $a$.

**PROPOSITION 9.5.** *For any $a, z \in \mathcal{X}$ with $a \neq z$,*

$$ \mathbf{P}_a\{\tau_z < \tau_a^+\} = \frac{1}{c(a) \mathcal{R}(a \leftrightarrow z)} = \frac{\mathcal{C}(a \leftrightarrow z)}{c(a)}. \tag{9.12} $$

*PROOF.* Applying Proposition 9.1 to $B = \{a, z\}$ and $h_B = \mathbf{1}_{\{z\}}$ yields that

$$ x \mapsto \mathbf{E}_x h_B(X_{\tau_B}) = \mathbf{P}_x\{\tau_z < \tau_a\} $$

### PDF page 136 (book page 120)

is the unique harmonic function on $\mathcal{X} \setminus \{a, z\}$ with value 0 at $a$ and value 1 at $z$. Since the function

$$ x \mapsto \frac{W(a) - W(x)}{W(a) - W(z)} $$

is also harmonic on $\mathcal{X} \setminus \{a, z\}$ with the same boundary values, Proposition 9.1 implies that

$$ \mathbf{P}_x\{\tau_z < \tau_a\} = \frac{W(a) - W(x)}{W(a) - W(z)}. \tag{9.13} $$

Therefore,

$$ \mathbf{P}_a\{\tau_z < \tau_a^+\} = \sum_{x \in V} P(a, x)\mathbf{P}_x\{\tau_z < \tau_a\} = \sum_{x \,:\, x \sim a} \frac{c(a, x)}{c(a)} \frac{W(a) - W(x)}{W(a) - W(z)}. \tag{9.14} $$

By the definition (9.7) of current flow, the above is equal to

$$ \frac{\sum_{x \,:\, x \sim a} I(\overrightarrow{ax})}{c(a)\,[W(a) - W(z)]} = \frac{\|I\|}{c(a)\,[W(a) - W(z)]} = \frac{1}{c(a)\mathcal{R}(a \leftrightarrow z)}, \tag{9.15} $$

showing (9.12). $\blacksquare$

The **_Green's function_** for a random walk stopped at a stopping time $\tau$ is defined by

$$ G_\tau(a, x) := \mathbf{E}_a\,(\text{number of visits to } x \text{ before } \tau) = \mathbf{E}_a \left( \sum_{t=0}^{\infty} \mathbf{1}_{\{X_t = x, \tau > t\}} \right). \tag{9.16} $$

LEMMA 9.6. *If $G_{\tau_z}(a, x)$ is the Green's function defined in (9.16), then*

$$ G_{\tau_z}(a, a) = c(a)\mathcal{R}(a \leftrightarrow z). \tag{9.17} $$

PROOF. The number of visits to $a$ before visiting $z$ has a geometric distribution with parameter $\mathbf{P}_a\{\tau_z < \tau_a^+\}$. The lemma then follows from (9.12). $\blacksquare$

It is often possible to replace a network by a simplified one without changing quantities of interest, for example the effective resistance between a pair of nodes. The following laws are very useful.

**Parallel Law**. *Conductances in parallel add*: suppose edges $e_1$ and $e_2$, with conductances $c_1$ and $c_2$, respectively, share vertices $v_1$ and $v_2$ as endpoints. Then both edges can be replaced with a single edge $e$ of conductance $c_1 + c_2$ yielding a new network $\tilde{G}$. All voltages and currents in $\tilde{G} \setminus \{e\}$ are unchanged and the current $\tilde{I}(\overrightarrow{e})$ equals $I(\overrightarrow{e_1}) + I(\overrightarrow{e_2})$. For a proof, check Ohm's and Kirchhoff's laws with $\tilde{I}(\overrightarrow{e}) := I(\overrightarrow{e_1}) + I(\overrightarrow{e_2})$.

**Series Law**. *Resistances in series add*: if $v \in V \setminus \{a, z\}$ is a node of degree 2 with neighbors $v_1$ and $v_2$, the edges $(v_1, v)$ and $(v, v_2)$ can be replaced by a single edge $(v_1, v_2)$ of resistance $r(v_1, v) + r(v, v_2)$, yielding a new network $\hat{G}$. All voltages and currents in $G \setminus \{v\}$ remain the same and the current that flows from $v_1$ to $v_2$ equals $I(\overrightarrow{v_1 v}) = I(\overrightarrow{v v_2})$. For a proof, check again Ohm's and Kirchhoff's laws, with $\hat{I}(\overrightarrow{v_1 v_2}) := I(\overrightarrow{v_1 v})$.

**Gluing**. We define the network operation of *gluing* vertices $v$ and $w$ by identifying $v$ and $w$ and keeping all existing edges. In particular, any edges between $v$ and $w$ become loops. If the voltages at $v$ and $w$ are the same and $v$ and $w$ are glued, then because current never flows between vertices with the same voltage, voltages and currents are unchanged.

### PDF page 137 (book page 121)

EXAMPLE 9.7. When $a$ and $z$ are two vertices in a tree $\Gamma$ with unit resistance on each edge, then $\mathcal{R}(a \leftrightarrow z)$ is equal to the length of the unique path joining $a$ and $z$. (For any vertex $x$ not along the path joining $a$ and $z$, there is a unique path from $x$ to $a$. Let $x_0$ be the vertex at which the $x$–$a$ path first hits the $a$–$z$ path. Then $W(x) = W(x_0)$.)

EXAMPLE 9.8. For a tree $\Gamma$ with root $\rho$, let $\Gamma_n$ be the set of vertices at distance $n$ from $\rho$. Consider the case of a spherically symmetric tree, in which all vertices of $\Gamma_n$ have the same degree for all $n \geq 0$. Suppose that all edges at the same distance from the root have the same resistance, that is, $r(e) = r_i$ if the vertex of $e$ furthest from the root is at distance $i$ to the root, $i \geq 1$. Glue all the vertices in each level; this will not affect effective resistances, so we infer that

$$ \mathcal{R}(\rho \leftrightarrow \Gamma_M) = \sum_{i=1}^{M} \frac{r_i}{|\Gamma_i|} \tag{9.18} $$

and

$$ \mathbf{P}_\rho\{\tau_{\Gamma_M} < \tau_\rho^+\} = \frac{r_1/|\Gamma_1|}{\sum_{i=1}^{M} r_i/|\Gamma_i|}. \tag{9.19} $$

Therefore, $\lim_{M \to \infty} \mathbf{P}_\rho\{\tau_{\Gamma_M} < \tau_\rho^+\} > 0$ if and only if $\sum_{i=1}^{\infty} r_i/|\Gamma_i| < \infty$.

EXAMPLE 9.9 (Biased nearest-neighbor random walk). Fix $\alpha > 0$ with $\alpha \neq 1$ and consider the path with vertices $\{0, 1, \ldots, n\}$ and conductances $c(k-1, k) = \alpha^k$ for $k = 1, \ldots, n$. Then for all interior vertices $0 < k < n$ we have

$$ P(k, k+1) = \frac{\alpha}{1 + \alpha}, $$
$$ P(k, k-1) = \frac{1}{1 + \alpha}. $$

If $p = \alpha/(1 + \alpha)$, then this is the walk that, when at an interior vertex, moves up with probability $p$ and down with probability $1 - p$. (Note: this is also an example of a birth-and-death chain, as defined in Section 2.5.)

Using the Series Law, we can replace the $k$ edges to the left of vertex $k$ by a single edge of resistance

$$ r_1 := \sum_{j=1}^{k} \alpha^{-j} = \frac{1 - \alpha^{-k}}{\alpha - 1}. $$

Likewise, we can replace the $(n - k)$ edges to the right of $k$ by a single edge of resistance

$$ r_2 := \sum_{j=k+1}^{n} \alpha^{-j} = \frac{\alpha^{-k} - \alpha^{-n}}{\alpha - 1} $$

The probability $\mathbf{P}_k\{\tau_n < \tau_0\}$ is not changed by this modification, so we can calculate simply that

$$ \mathbf{P}_k\{\tau_n < \tau_0\} = \frac{r_2^{-1}}{r_1^{-1} + r_2^{-1}} = \frac{\alpha^{-k} - 1}{\alpha^{-n} - 1}. $$

In particular, for the biased random walk which moves up with probability $p$,

$$ \mathbf{P}_k\{\tau_n < \tau_0\} = \frac{[(1-p)/p]^k - 1}{[(1-p)/p]^n - 1}. \tag{9.20} $$

### PDF page 138 (book page 122)

Define the **_energy_** of a flow $\theta$ by

$$ \mathcal{E}(\theta) := \sum_{e} [\theta(e)]^2 r(e). $$

THEOREM 9.10 (Thomson's Principle). *For any finite connected graph,*

$$ \mathcal{R}(a \leftrightarrow z) = \inf \left\{ \mathcal{E}(\theta) : \theta \text{ a unit flow from } a \text{ to } z \right\}. \tag{9.21} $$

*The unique minimizer in the* inf *above is the unit current flow.*

REMARK 9.11. The sum in $\mathcal{E}(\theta)$ is over unoriented edges, so each edge $\{x, y\}$ is only considered once in the definition of energy. Although $\theta$ is defined on oriented edges, it is antisymmetric and hence $\theta(e)^2$ is unambiguous.

PROOF. Fixing some unit flow $\theta_0$ from $a$ to $z$, the set

$$ K = \{\text{unit flows } \theta \text{ from } a \text{ to } z : \mathcal{E}(\theta) \leq \mathcal{E}(\theta_0)\} $$

is a compact subset of $\mathbb{R}^{|E|}$. Therefore, there there exists a unit flow $\theta$ from $a$ to $z$ minimizing $\mathcal{E}(\theta)$ subject to $\|\theta\| = 1$. By Proposition 9.4, to prove that the unit current flow is the unique minimizer, it is enough to verify that any unit flow $\theta$ of minimal energy satisfies the cycle law.

Let the edges $\overrightarrow{e_1}, \ldots, \overrightarrow{e_n}$ form a cycle. Set $\gamma(\overrightarrow{e_i}) = 1$ for all $1 \leq i \leq n$ and set $\gamma$ equal to zero on all other edges. Note that $\gamma$ satisfies the node law, so it is a flow, but $\sum \gamma(\overrightarrow{e_i}) = n \neq 0$. For any $\varepsilon \in \mathbb{R}$, we have by energy minimality that

$$ 0 \leq \mathcal{E}(\theta + \varepsilon\gamma) - \mathcal{E}(\theta) = \sum_{i=1}^{n} \left[ (\theta(\overrightarrow{e_i}) + \varepsilon)^2 - \theta(\overrightarrow{e_i})^2 \right] r(\overrightarrow{e_i}) $$
$$ = 2\varepsilon \sum_{i=1}^{n} r(\overrightarrow{e_i})\theta(\overrightarrow{e_i}) + O(\varepsilon^2). $$

Dividing both sides by $\varepsilon > 0$ shows that

$$ 0 \leq 2 \sum_{i=1}^{n} r(\overrightarrow{e_i})\theta(\overrightarrow{e_i}) + O(\varepsilon), $$

and letting $\varepsilon \downarrow 0$ shows that $0 \leq \sum_{i=1}^{n} r(e_i)\theta(\overrightarrow{e_i})$. Similarly, dividing by $\varepsilon < 0$ and then letting $\varepsilon \uparrow 0$ shows that $0 \geq \sum_{i=1}^{n} r(e_i)\theta(\overrightarrow{e_i})$. Therefore, $\sum_{i=1}^{n} r(e_i)\theta(\overrightarrow{e_i}) = 0$, verifying that $\theta$ satisfies the cycle law.

We complete the proof by showing that the unit current flow $I$ has $\mathcal{E}(I) = \mathcal{R}(a \leftrightarrow z)$:

$$ \sum_{e} r(e)I(e)^2 = \frac{1}{2} \sum_{x} \sum_{y} r(x, y) \left[ \frac{W(x) - W(y)}{r(x, y)} \right]^2 $$
$$ = \frac{1}{2} \sum_{x} \sum_{y} c(x, y)[W(x) - W(y)]^2 $$
$$ = \frac{1}{2} \sum_{x} \sum_{y} [W(x) - W(y)]I(\overrightarrow{xy}). $$

Since $I$ is antisymmetric,

$$ \frac{1}{2} \sum_{x} \sum_{y} [W(x) - W(y)]I(\overrightarrow{xy}) = \sum_{x} W(x) \sum_{y} I(\overrightarrow{xy}). \tag{9.22} $$

### PDF page 139 (book page 123)

By the node law, $\sum_y I(\overrightarrow{xy}) = 0$ for any $x \notin \{a, z\}$, while $\sum_y I(\overrightarrow{ay}) = \|I\| = -\sum_y I(\overrightarrow{zy})$, so the right-hand side of (9.22) equals

$$ \|I\| \left( W(a) - W(z) \right). $$

Since $\|I\| = 1$, we conclude that the right-hand side of (9.22) is equal to $(W(a) - W(z))/\|I\| = \mathcal{R}(a \leftrightarrow z)$. $\blacksquare$

Let $a, z$ be vertices in a network and suppose that we add to the network an edge which is not incident to $a$. How does this affect the escape probability from $a$ to $z$? From the point of view of probability, the answer is not obvious. In the language of electrical networks, this question is answered by Rayleigh's Law.

If $r = \{r(e)\}$ are assignments of resistances to the edges of a graph $G$, write $\mathcal{R}(a \leftrightarrow z; r)$ to denote the effective resistance computed with these resistances.

THEOREM 9.12 (Rayleigh's Monotonicity Law). *If $\{r(e)\}$ and $\{r'(e)\}$ are two assignments of resistances to the edges of the same graph $G$ that satisfy $r(e) \leq r'(e)$ for all $e$, then*

$$ \mathcal{R}(a \leftrightarrow z; r) \ \leq \ \mathcal{R}(a \leftrightarrow z; r'). \tag{9.23} $$

PROOF. Note that $\inf_\theta \sum_e r(e)\theta(e)^2 \leq \inf_\theta \sum_e r'(e)\theta(e)^2$ and apply Thomson's Principle (Theorem 9.10). $\blacksquare$

COROLLARY 9.13. *Adding an edge does not increase the effective resistance $\mathcal{R}(a \leftrightarrow z)$. If the added edge is not incident to $a$, then the addition does not decrease the escape probability $\mathbf{P}_a\{\tau_z < \tau_a^+\} = [c(a)\mathcal{R}(a \leftrightarrow z)]^{-1}$.*

PROOF. Before we add an edge to a network, we can think of it as existing already with $c = 0$ or $r = \infty$. By adding the edge, we reduce its resistance to a finite number.

Combining this with the relationship (9.12) shows that the addition of an edge not incident to $a$ (which we regard as changing a conductance from 0 to a non-zero value) cannot decrease the escape probability $\mathbf{P}_a\{\tau_z < \tau_a^+\}$. $\blacksquare$

COROLLARY 9.14. *The operation of gluing vertices cannot increase effective resistance.*

PROOF. When we glue vertices together, we take an infimum in Thomson's Principle (Theorem 9.10) over a larger class of flows. $\blacksquare$

A technique due to Nash-Williams often gives simple but useful lower bounds on effective resistance. We call $\Pi \subseteq E$ an **edge-cutset separating** $a$ **from** $z$ if every path from $a$ to $z$ includes some edge in $\Pi$.

LEMMA 9.15. *If $\theta$ is a flow from $a$ to $z$, and $\Pi$ is an edge-cutset separating $a$ from $z$, then*

$$ \|\theta\| \leq \sum_{e \in \Pi} |\theta(e)|. $$

PROOF. Let

$$ S = \{x \ : \ a \text{ and } x \text{ are connected in } G \setminus \Pi\}. $$

We have

$$ \sum_{x \in S} \sum_y \theta(\overrightarrow{xy}) = \sum_{x \in S} \sum_{y \notin S} \theta(\overrightarrow{xy}) \leq \sum_{e \in \Pi} |\theta(e)|, $$

### PDF page 140 (book page 124)

the equality holding because if $y \in S$, then both the directed edges $(x, y)$ and $(y, x)$ appear in the sum. On the other hand,

$$ \sum_{x \in S} \sum_y \theta(\overrightarrow{xy}) = \|\theta\|, $$

since the node law holds for all $x \neq a$. $\blacksquare$

PROPOSITION 9.16. *If $\{\Pi_k\}$ are disjoint edge-cutsets which separate nodes $a$ and $z$, then*

$$ \mathcal{R}(a \leftrightarrow z) \geq \sum_k \left( \sum_{e \in \Pi_k} c(e) \right)^{-1}. \tag{9.24} $$

*The inequality* (9.24) *is called the* Nash-Williams inequality.

PROOF. Let $\theta$ be a unit flow from $a$ to $z$. For any $k$, by the Cauchy-Schwarz inequality

$$ \sum_{e \in \Pi_k} c(e) \cdot \sum_{e \in \Pi_k} r(e)\theta(e)^2 \geq \left( \sum_{e \in \Pi_k} \sqrt{c(e)}\sqrt{r(e)}|\theta(e)| \right)^2 = \left( \sum_{e \in \Pi_k} |\theta(e)| \right)^2. $$

By Lemma 9.15, the right-hand side is bounded below by $\|\theta\|^2 = 1$. Therefore

$$ \sum_e r(e)\theta(e)^2 \geq \sum_k \sum_{e \in \Pi_k} r(e)\theta(e)^2 \geq \sum_k \left( \sum_{e \in \Pi_k} c(e) \right)^{-1}. $$

By Thomson's Principle (Theorem 9.10), we are done. $\blacksquare$

**9.5. Escape Probabilities on a Square**

We now use the inequalities we have developed to bound effective resistance in a non-trivial example. Let $B_n$ be the $n \times n$ two-dimensional grid graph: the vertices are pairs of integers $(z, w)$ such that $1 \leq z, w \leq n$, while the edges are pairs of points at unit (Euclidean) distance.

PROPOSITION 9.17. *Let $a = (1, 1)$ be the lower left-hand corner of $B_n$, and let $z = (n, n)$ be the upper right-hand corner of $B_n$. Suppose each edge of $B_n$ has unit conductance. The effective resistance $\mathcal{R}(a \leftrightarrow z)$ satisfies*

$$ \frac{\log n}{2} \leq \mathcal{R}(a \leftrightarrow z) \leq 2 \log n. \tag{9.25} $$

We separate the proof into the lower and upper bounds.

PROOF OF LOWER BOUND IN (9.25). Let $\Pi_k$ be the edge set

$$ \Pi_k = \{\{v, w\} \in E(B_n) \ : \ \|v\|_\infty = k, \|w\|_\infty = k + 1\}, $$

where $\|(v_1, v_2)\|_\infty = \max\{v_1, v_2\}$. (See Figure 9.1.) Since every path from $a$ to $z$ must use an edge in $\Pi_k$, the set $\Pi_k$ is a cutset. Since each edge has unit conductance,

### PDF page 141 (book page 125)

**FIGURE 9.1.** The graph $B_5$. The cutset $\Pi_3$ contains the edges drawn with dashed lines. *[Figure: A $5 \times 5$ grid graph of nodes (dots) connected by horizontal and vertical edges. The top-right corner node is labeled $z$; the bottom-left corner node is labeled $a = (1,1)$. Several interior edges — forming an L-shaped diagonal band separating the lower-left region from the upper-right region — are drawn as dashed lines, representing the cutset $\Pi_3$.]*

$\sum_{e \in \Pi_k} c(e)$ equals the number of edges in $\Pi_k$, namely $2k$. By Proposition 9.16 and Exercise 2.4,

$$ \mathcal{R}(a \leftrightarrow z) \geq \sum_{k=1}^{n-1} \frac{1}{2k} \geq \frac{\log n}{2}. \tag{9.26} $$

$\blacksquare$

PROOF OF UPPER BOUND IN (9.25). Thomson's Principle (Theorem 9.10) says that the effective resistance is the minimal possible energy of a unit flow from $a$ to $z$. So to get an upper bound on resistance, we build a unit flow on the square.

Consider Pólya's urn process, described in Section 2.4. The sequence of ordered pairs listing the numbers of black and white balls is a Markov chain with state space $\{1, 2, \ldots\}^2$.

Run this process on the square—note that it necessarily starts at vertex $a = (1, 1)$—and stop when you reach the main diagonal $x + y = n + 1$. Direct all edges of the square from bottom left to top right and give each edge $e$ on the bottom left half of the square the flow

$$ f(e) = \mathbf{P}\{\text{the process went through } e\}. $$

To finish the construction, give the upper right half of the square the symmetrical flow values.

From Lemma 2.6, it follows that for any $k \geq 0$, the Pólya's urn process is equally likely to pass through each of the $k + 1$ pairs $(i, j)$ for which $i + j = k + 2$. Consequently, when $(i, j)$ is a vertex in the square for which $i + j = k + 2$, the sum of the flows on its incoming edges is $\frac{1}{k+1}$. Thus the energy of the flow $f$ can be bounded by

$$ \mathcal{E}(f) \leq \sum_{k=1}^{n-1} 2 \left( \frac{1}{k+1} \right)^2 (k+1) \leq 2 \log n. $$

$\blacksquare$

**Exercises**

EXERCISE 9.1. Generalize the flow in the upper bound of (9.25) to higher dimensions, using an urn with balls of $d$ colors. Use this to show that the resistance between opposite corners of the $d$-dimensional box of side length $n$ is bounded independent of $n$, when $d \geq 3$.

### PDF page 142 (book page 126)

EXERCISE 9.2. An Oregon professor has $n$ umbrellas, of which initially $k \in (0, n)$ are at his office and $n - k$ are at his home. Every day, the professor walks to the office in the morning and returns home in the evening. In each trip, he takes an umbrella with him only if it is raining. Assume that in every trip between home and office or back, the chance of rain is $p \in (0, 1)$, independently of other trips.

(a) Asymptotically, in what fraction of his trips does the professor get wet?

(b) Determine the expected number of trips until all $n$ umbrellas are at the same location.

(c) Determine the expected number of trips until the professor gets wet.

EXERCISE 9.3 (Gambler's ruin). In Section 2.1, we defined simple random walk on $\{0, 1, 2, \ldots, n\}$. Use the network reduction laws to show that $\mathbf{P}_x\{\tau_n < \tau_0\} = x/n$.

EXERCISE 9.4. Let $\theta$ be a flow from $a$ to $z$ which satisfies both the cycle law and $\|\theta\| = \|I\|$. Define a function $h$ on nodes by

$$ h(x) = \sum_{i=1}^{m} \left[ \theta(\vec{e_i}) - I(\vec{e_i}) \right] r(\vec{e_i}), \tag{9.27} $$

where $\vec{e_i}, \ldots, \vec{e_m}$ is an arbitrary path from $a$ to $x$.

(a) Show that $h$ is well-defined (i.e. $h(x)$ does not depend on the choice of path) and harmonic at all nodes.

(b) Use part (a) to give an alternate proof of Proposition 9.4.

EXERCISE 9.5. Show that if, in a network with source $a$ and sink $z$, vertices with different voltages are glued together, then the effective resistance from $a$ to $z$ will strictly decrease.

EXERCISE 9.6. Show that $\mathcal{R}(a \leftrightarrow z)$ is a concave function of $\{r(e)\}$.

EXERCISE 9.7. Let $B_n$ be the subset of $\mathbb{Z}^2$ contained in the box of side length $2n$ centered at 0. Let $\partial B_n$ be the set of vertices along the perimeter of the box. Show that for simple random walk on $B_n$,

$$ \lim_{n \to \infty} \mathbf{P}_0\{\tau_{\partial B_n} < \tau_0^+\} = 0. $$

EXERCISE 9.8. Show that effective resistances form a metric on any network with conductances $\{c(e)\}$.

*Hint:* The only non-obvious statement is the triangle inequality

$$ \mathcal{R}(x \leftrightarrow z) \leq \mathcal{R}(x \leftrightarrow y) + \mathcal{R}(y \leftrightarrow z). $$

Adding the unit current flow from $x$ to $y$ to the unit current flow from $y$ to $z$ gives the unit current flow from $x$ to $z$ (check Kirchhoff's laws!). Now use the corresponding voltage functions.

EXERCISE 9.9. Given a network $(G = (V, E), \{c(e)\})$, define the *Dirichlet energy* of a function $f : V \to \mathbb{R}$ by

$$ \mathcal{E}_{\mathrm{Dir}}(f) = \frac{1}{2} \sum_{v,w} [f(v) - f(w)]^2 c(v, w) . $$

(a) Prove that

$$ \min_{\substack{f \\ f(v)=1, f(w)=0}} \mathcal{E}_{\mathrm{Dir}}(f) = \mathcal{C}(v \leftrightarrow w) , $$

### PDF page 143 (book page 127)

and the unique minimizer is harmonic on $V \setminus \{v, w\}$.

(b) Deduce that $\mathcal{C}(v \leftrightarrow w)$ is a convex function of the edge conductances.

**Notes**

Proposition 9.16 appeared in **Nash-Williams (1959)**.

**Further reading.** The basic reference for the connection between electrical networks and random walks on graphs is **Doyle and Snell (1984)**, and we borrow here from **Peres (1999)**. For more on this topic, see **Soardi (1994)**, **Bollobás (1998)**, and **Lyons and Peres (2016)**.

The Dirichlet variational principle in Exercise 9.9 is explained and used in **Liggett (1985)**.

The connection to the transience and recurrence of infinite networks is given in Section 21.2.

For more on discrete harmonic functions, see **Lawler (1991)**. For an introduction to (continuous) harmonic functions, see **Ahlfors (1978**, Chapter 6).

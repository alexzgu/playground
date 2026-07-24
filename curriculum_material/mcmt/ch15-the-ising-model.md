# Chapter 15 — The Ising Model
*(PDF pages 231–247; book pages 215–231)*

### PDF page 231 (book page 215)

CHAPTER 15

# The Ising Model

The Ising model on a graph $G = (V, E)$ at inverse temperature $\beta$ was introduced in Section 3.3.5. It is the probability distribution on $\mathcal{X} = \{-1, 1\}^V$ defined by

$$ \pi(\sigma) = Z(\beta)^{-1} \exp\left( \beta \sum_{\{v,w\} \in E} \sigma(v)\sigma(w) \right). $$

Here we study in detail the Glauber dynamics for this distribution. As discussed in Section 3.3.5, this chain evolves by selecting a vertex $v$ at random and updating the spin at $v$ according to the distribution $\pi$ conditioned to agree with the spins at all vertices not equal to $v$. If the current configuration is $\sigma$ and vertex $v$ is selected, then the chance the spin at $v$ is updated to $+1$ is equal to

$$ p(\sigma, v) := \frac{e^{\beta S(\sigma,v)}}{e^{\beta S(\sigma,v)} + e^{-\beta S(\sigma,v)}} = \frac{1 + \tanh(\beta S(\sigma, v))}{2}. \tag{15.1} $$

Thus, the transition matrix for this chain is given by

$$ P(\sigma, \sigma') = \frac{1}{n} \sum_{v \in V} \frac{e^{\beta\, \sigma'(v)\, S(\sigma,v)}}{e^{\beta\, \sigma'(v)\, S(\sigma,v)} + e^{-\beta\, \sigma'(v)\, S(\sigma,v)}} \cdot \mathbf{1}_{\{\sigma'(w)=\sigma(w) \text{ for all } w \neq v\}}, $$

where $S(\sigma, v) = \sum_{w \,:\, w \sim v} \sigma(w)$ and $n = |V|$.

We will be particularly interested in how the mixing time varies with $\beta$. Generically, for small $\beta$, the chain will mix rapidly, while for large $\beta$, the chain will converge slowly. Understanding this phase transition between slow and fast mixing has been a topic of great interest and activity since the late 1980's; here we only scratch the surface.

One simple but general observation is that for any $\beta$ and any graph on $n$ vertices, $t_{\mathrm{rel}} \geq \frac{n}{2}$; see Exercise 15.1.

**15.1. Fast Mixing at High Temperature**

In this section we use the path coupling technique of Chapter 14 to show that on any graph of bounded degree, for small values of $\beta$, the Glauber dynamics for the Ising model is fast mixing.

THEOREM 15.1. *Consider the Glauber dynamics for the Ising model on a graph with $n$ vertices and maximal degree $\Delta$.*

(i) *Let $c(\beta) := 1 - \Delta \tanh(\beta)$. If $\Delta \cdot \tanh(\beta) < 1$, then*

$$ t_{\mathrm{rel}} \leq \frac{n}{c(\beta)} \,. \tag{15.2} $$

215

### PDF page 232 (book page 216)

*Also,*

$$ d(t) \leq n \left( 1 - \frac{c(\beta)}{n} \right)^t , \tag{15.3} $$

*and*

$$ t_{\mathrm{mix}}(\varepsilon) \leq \left\lceil \frac{n(\log n + \log(1/\varepsilon))}{c(\beta)} \right\rceil . \tag{15.4} $$

*In particular, (15.4) holds whenever $\beta < \Delta^{-1}$.*

(ii) *Suppose every vertex of the graph has even degree. Let*

$$ c_e(\beta) := 1 - (\Delta/2) \tanh(2\beta). $$

*If $(\Delta/2) \cdot \tanh(2\beta) < 1$, then*

$$ t_{\mathrm{rel}} \leq \frac{n}{c_e(\beta)} \,. \tag{15.5} $$

*Also,*

$$ d(t) \leq n \left( 1 - \frac{c_e(\beta)}{n} \right)^t , \tag{15.6} $$

*and*

$$ t_{\mathrm{mix}}(\varepsilon) \leq \left\lceil \frac{n(\log n + \log(1/\varepsilon))}{c_e(\beta)} \right\rceil . \tag{15.7} $$

REMARK 15.2. We use the improvement for even-degree graphs given in part (ii) to analyze Glauber dynamics for the cycle in Theorem 15.5.

LEMMA 15.3. *The function $\varphi(x) := \tanh(\beta(x + 1)) - \tanh(\beta(x - 1))$ is even and decreasing on $[0, \infty)$, whence*

$$ \sup_{x \in \mathbb{R}} \varphi(x) = \varphi(0) = 2\tanh(\beta) \tag{15.8} $$

*and*

$$ \sup_{k \text{ odd integer}} \varphi(k) = \varphi(1) = \tanh(2\beta). \tag{15.9} $$

PROOF. Let $\psi(x) := \tanh(\beta x)$; observe that $\psi'(x) = \beta / \cosh^2(\beta x)$. The function $\psi'$ is strictly positive and decreasing on $[0, \infty)$ and is even. Therefore, for $x > 0$,

$$ \varphi'(x) = \psi'(x + 1) - \psi'(x - 1) < 0, $$

as is seen by considering separately the case where $x - 1 > 0$ and the case where $x - 1 \leq 0$. Because tanh is an odd function,

$$ \varphi(-x) = \psi(-x + 1) - \psi(-x - 1) = -\psi(x - 1) + \psi(x + 1) = \varphi(x), $$

so $\varphi$ is even. $\blacksquare$

PROOF OF THEOREM 15.1. *Proof of (i).* Define the distance $\rho$ on $\mathcal{X}$ by

$$ \rho(\sigma, \tau) = \frac{1}{2} \sum_{u \in V} |\sigma(u) - \tau(u)|. $$

The distance $\rho$ is a path metric as defined in Section 14.2.

Let $\sigma$ and $\tau$ be two configurations with $\rho(\sigma, \tau) = 1$. The spins of $\sigma$ and $\tau$ agree everywhere except at a single vertex $v$. Assume that $\sigma(v) = -1$ and $\tau(v) = +1$.

Define $\mathcal{N}(v) := \{u \,:\, u \sim v\}$ to be the set of neighboring vertices to $v$.

We describe now a coupling $(X, Y)$ of one step of the chain started in configuration $\sigma$ with one step of the chain started in configuration $\tau$.

### PDF page 233 (book page 217)

Pick a vertex $w$ uniformly at random from $V$. If $w \notin \mathcal{N}(v)$, then the neighbors of $w$ agree in both $\sigma$ and $\tau$. As the probability of updating the spin at $w$ to $+1$, given in (3.11), depends only on the spins at the neighbors of $w$, it is the same for the chain started in $\sigma$ as for the chain started in $\tau$. Thus we can update both chains together.

If $w \in \mathcal{N}(v)$, the probabilities of updating to $+1$ at $w$ are no longer the same for the two chains, so we cannot *always* update together. We do, however, use a single random variable as the common source of noise to update both chains, so the two chains agree as often as is possible. In particular, let $U$ be a uniform random variable on $[0, 1]$ and set

$$ X(w) = \begin{cases} +1 & \text{if } U \leq p(\sigma, w), \\ -1 & \text{if } U > p(\sigma, w) \end{cases} \quad \text{and} \quad Y(w) = \begin{cases} +1 & \text{if } U \leq p(\tau, w), \\ -1 & \text{if } U > p(\tau, w). \end{cases} $$

Set $X(u) = \sigma(u)$ and $Y(u) = \tau(u)$ for $u \neq w$. (Note that since tanh is non-decreasing, and since $S(w, \sigma) \leq S(w, \tau)$ owing to $\sigma(v) = -1$ and $\tau(v) = +1$, we always have $p(\sigma, w) \leq p(\tau, w)$.)

If $w = v$, then $\rho(X, Y) = 0$. If $w \notin \mathcal{N}(v) \cup \{v\}$, then $\rho(X, Y) = 1$. If $w \in \mathcal{N}(v)$ and $p(\sigma, w) < U \leq p(\tau, w)$, then $\rho(X, Y) = 2$. Thus,

$$ \mathbf{E}_{\sigma,\tau}(\rho(X, Y)) \leq 1 - \frac{1}{n} + \frac{1}{n} \sum_{w \in \mathcal{N}(v)} \left[ p(\tau, w) - p(\sigma, w) \right]. \tag{15.10} $$

Let $s := S(w, \tau) - 1 = S(w, \sigma) + 1$. By (15.1),

$$ p(\tau, w) - p(\sigma, w) = \frac{1}{2} \left[ \tanh(\beta(s + 1)) - \tanh(\beta(s - 1)) \right]. \tag{15.11} $$

Applying (15.8) shows that

$$ p(\tau, w) - p(\sigma, w) \leq \tanh(\beta). \tag{15.12} $$

Using the above bound in inequality (15.10) yields

$$ \mathbf{E}_{\sigma,\tau} \left( \rho(X, Y) \right) \leq 1 - \frac{[1 - \Delta \tanh(\beta)]}{n} = 1 - \frac{c(\beta)}{n} \,. $$

If $\Delta \tanh(\beta) < 1$, then $c(\beta) > 0$. Applying Theorem 13.1 and using that $\rho_K$ is a metric, whence satisfies the triangle inequality, yields (15.2).

Observe that $\mathrm{diam}(\mathcal{X}) = n$. Applying Corollary 14.8 with $e^{-\alpha} = 1 - c(\beta)/n$ establishes (15.3). Using that $1 - c(\beta)/n \leq e^{-c(\beta)/n}$ establishes (15.4).

Since $\tanh(x) \leq x$, if $\beta < \Delta^{-1}$, then $\Delta \tanh(\beta) < 1$.

*Proof of (ii).* Note that if every vertex in the graph has even degree, then $s$ takes on only odd values. Applying (15.9) shows that

$$ p(\tau, w) - p(\sigma, w) = \frac{1}{2} \left[ \tanh(\beta(s + 1)) - \tanh(\beta(s - 1)) \right] \leq \frac{\tanh(2\beta)}{2}. $$

Using the above bound in inequality (15.10) shows that

$$ \mathbf{E}_{\sigma,\tau} \left( \rho(X, Y) \right) \leq 1 - \frac{1 - (\Delta/2)\tanh(2\beta)}{n} = 1 - \frac{c_e(\beta)}{n} \,. $$

Assume that $(\Delta/2)\tanh(2\beta) < 1$. Applying Theorem 13.1 yields (15.5). Using Corollary 14.8 with $e^{-\alpha} = 1 - \frac{c_e(\beta)}{n}$ yields (15.6). Since $1 - \frac{c_e(\beta)}{n} \leq e^{-c_e(\beta)/n}$, we obtain (15.7). $\blacksquare$

### PDF page 234 (book page 218)

**15.2. The Complete Graph**

Let $G$ be the complete graph on $n$ vertices, the graph which includes all $\binom{n}{2}$ possible edges. Since the interaction term $\sigma(v) \sum_{w \,:\, w \sim v} \sigma(w)$ is of order $n$, we take $\beta = \alpha/n$ with $\alpha = O(1)$, so that the total contribution of a single site to $\beta \sum \sigma(v)\sigma(w)$ is $O(1)$.

THEOREM 15.4. *Let $G$ be the complete graph on $n$ vertices, and consider Glauber dynamics for the Ising model on $G$ with $\beta = \alpha/n$.*

(i) *If $\alpha < 1$, then*

$$ t_{\mathrm{mix}}(\varepsilon) \leq \Big\lceil \frac{n(\log n + \log(1/\varepsilon))}{1 - \alpha} \Big\rceil. \tag{15.13} $$

(ii) *There exists a universal constant $C_0 > 0$ such that, if $\alpha > 1$, then $t_{\mathrm{mix}} \geq C_0 \exp\left[r(\alpha)n\right]$, where $r(\alpha) > 0$.*

PROOF. *Proof of* (i). Note that $\Delta \tanh(\beta) = (n-1)\tanh(\alpha/n) \leq \alpha$. Thus if $\alpha < 1$, then Theorem 15.1(i) establishes (15.13).

*Proof of* (ii). Define $A_k := \{\sigma \,:\, |\{v \,:\, \sigma(v) = 1\}| = k\}$. By counting, $\pi(A_k) = a_k/Z(\alpha)$, where

$$ a_k := \binom{n}{k} \exp\left\{ \frac{\alpha}{n} \left[ \binom{k}{2} + \binom{n-k}{2} - k(n-k) \right] \right\}. $$

Taking logarithms and applying Stirling's formula shows that

$$ \log(a_{\lfloor cn \rfloor}) = n\varphi_\alpha(c)[1 + o(1)], $$

where

$$ \varphi_\alpha(c) := -c\log(c) - (1-c)\log(1-c) + \alpha\left[\frac{(1-2c)^2}{2}\right]. \tag{15.14} $$

Taking derivatives shows that

$$ \varphi'_\alpha(1/2) = 0, $$
$$ \varphi''_\alpha(1/2) = -4(1 - \alpha). $$

Hence $c = 1/2$ is a critical point of $\varphi_\alpha$, and in particular it is a local maximum or minimum depending on the value of $\alpha$. See Figure 15.1 for the graph of $\varphi_\alpha$ for $\alpha = 0.9$ and $\alpha = 1.1$. Take $\alpha > 1$, in which case $\varphi_\alpha$ has a local minimum at $1/2$. Define

$$ S = \left\{ \sigma \,:\, \sum_{u \in V} \sigma(u) < 0 \right\}. $$

By symmetry, $\pi(S) \leq 1/2$. Observe that the only way to get from $S$ to $S^c$ is through $A_{\lfloor n/2 \rfloor}$, since we are only allowed to change one spin at a time. Thus

$$ Q(S, S^c) \leq \pi(A_{\lfloor n/2 \rfloor}) \quad \text{and} \quad \pi(S) = \sum_{j \leq \lfloor n/2 \rfloor} \pi(A_j). $$

Let $c_\alpha$ be the value of $c$ maximizing $\varphi_\alpha$ over $[0, 1/2]$. Since $1/2$ is a strict local minimum, $c_\alpha < 1/2$. Therefore,

$$ \Phi(S) \leq \frac{\exp\{\varphi_\alpha(1/2)n[1 + o(1)]\}}{Z(\alpha)\pi(A_{\lfloor c_\alpha n \rfloor})} = \frac{\exp\{\varphi_\alpha(1/2)n[1 + o(1)]\}}{\exp\{\varphi_\alpha(c_\alpha)n[1 + o(1)]\}}. $$

Since $\varphi_\alpha(c_\alpha) > \varphi_\alpha(1/2)$, there is an $r(\alpha) > 0$ and constant $b > 0$ so that $\Phi_\star \leq be^{-nr(\alpha)}$. The conclusion follows from Theorem 7.4. $\blacksquare$

### PDF page 235 (book page 219)

*[Figure: a plot of the function $\varphi_\alpha$ over the horizontal axis from about 0.1 to 0.9 (ticks at 0.2, 0.4, 0.6, 0.8) and vertical axis labeled 0.68, 0.685, 0.69, 0.695. A solid concave-down curve peaks near the center at about 0.6915 (the $\alpha = 0.9$ case); a dashed curve dips to a local minimum near the center and rises on both sides (the $\alpha = 1.1$ case).]*

FIGURE 15.1. The function $\varphi_\alpha$ defined in (15.14). The dashed graph corresponds to $\alpha = 1.1$, the solid line to $\alpha = 0.9$.

**15.3. The Cycle**

THEOREM 15.5. *Let $c_{\mathrm{O}}(\beta) := 1 - \tanh(2\beta)$. The Glauber dynamics for the Ising model on the $n$-cycle satisfies, for any $\beta > 0$,*

$$ t_{\mathrm{rel}} = \frac{n}{c_{\mathrm{O}}(\beta)}. \tag{15.15} $$

*For fixed $\varepsilon > 0$,*

$$ \frac{1 + o(1)}{2c_{\mathrm{O}}(\beta)} \leq \frac{t_{\mathrm{mix}}(\varepsilon)}{n \log n} \leq \frac{1 + o(1)}{c_{\mathrm{O}}(\beta)}. \tag{15.16} $$

PROOF. *Upper bounds.* Note that $\Delta = 2$, whence $(\Delta/2)\tanh(2\beta) = \tanh(2\beta) < 1$. Theorem 15.1(ii) shows that

$$ t_{\mathrm{mix}}(\varepsilon) \leq \Big\lceil \frac{n(\log n + \log(1/\varepsilon))}{c_{\mathrm{O}}(\beta)} \Big\rceil $$

for all $\beta$.

*Lower bound.* We will use Wilson's method (Theorem 13.28).

*Claim:* The function $\Phi : \mathcal{X} \to \mathbb{R}$ defined by $\Phi(\sigma) := \sum_{i=1}^n \sigma(i)$ is an eigenfunction with eigenvalue

$$ \lambda = 1 - \frac{1 - \tanh(2\beta)}{n}. \tag{15.17} $$

This and (15.5) prove (15.15).

*Proof of Claim:* We first consider the action of $P$ on $\varphi_i : \mathcal{X} \to \mathbb{R}$ defined by $\varphi_i(\sigma) := \sigma_i$. Recall that if vertex $i$ is selected for updating, a positive spin is placed at $i$ with probability

$$ \frac{1 + \tanh\left[\beta(\sigma(i-1) + \sigma(i+1))\right]}{2}. $$

(See (3.11); here $S(\sigma, i) = \sum_{j \,:\, j \sim i} \sigma(j) = \sigma(i-1) + \sigma(i+1)$.) Therefore,

$$
\begin{aligned}
(P\varphi_i)(\sigma) &= (+1)\left( \frac{1 + \tanh[\beta(\sigma(i-1) + \sigma(i+1))]}{2n} \right) \\
&\quad + (-1)\left( \frac{1 - \tanh[\beta(\sigma(i-1) + \sigma(i+1))]}{2n} \right) + \left(1 - \frac{1}{n}\right)\sigma(i) \\
&= \frac{\tanh[\beta(\sigma(i-1) + \sigma(i+1))]}{n} + \left(1 - \frac{1}{n}\right)\sigma(i).
\end{aligned}
$$

### PDF page 236 (book page 220)

The variable $[\sigma(i-1) + \sigma(i+1)]$ takes values in $\{-2, 0, 2\}$; since the function $\tanh$ is odd, it is linear on $\{-2, 0, 2\}$ and in particular, for $x \in \{-2, 0, 2\}$,

$$ \tanh(\beta x) = \frac{\tanh(2\beta)}{2} x. $$

We conclude that

$$ (P\varphi_i)(\sigma) = \frac{\tanh(2\beta)}{2n}\left(\sigma(i-1) + \sigma(i+1)\right) + \left(1 - \frac{1}{n}\right)\sigma(i). $$

Summing over $i$,

$$ (P\Phi)(\sigma) = \frac{\tanh(2\beta)}{n}\Phi(\sigma) + \left(1 - \frac{1}{n}\right)\Phi(\sigma) = \left(1 - \frac{1 - \tanh(2\beta)}{n}\right)\Phi(\sigma), $$

proving that $\Phi$ is an eigenfunction with eigenvalue $\lambda$ defined in (15.17).

Note that if $\tilde{\sigma}$ is the state obtained after updating $\sigma$ according to the Glauber dynamics, then $|\Phi(\tilde{\sigma}) - \Phi(\sigma)| \leq 2$. Therefore, taking $x$ to be the all-plus configuration, (13.28) yields

$$
\begin{aligned}
t_{\mathrm{mix}}(\varepsilon) &\geq [1 + o(1)]\left[ \frac{n}{2c_{\mathrm{O}}(\beta)} \left( \log\left( \frac{\frac{c_{\mathrm{O}}(\beta)}{n}n^2}{8} \right) + \log\left( \frac{1}{2\varepsilon} \right) \right) \right] \\
&= \frac{[1 + o(1)]n \log n}{2c_{\mathrm{O}}(\beta)}.
\end{aligned}
$$

$\blacksquare$

**15.4. The Tree**

Our applications of path coupling have heretofore used path metrics with unit edge lengths. Let $\theta := \tanh(\beta)$. The coupling of Glauber dynamics for the Ising model that was used in Theorem 15.1 contracts the Hamming distance, provided $\theta\Delta < 1$. Therefore, the Glauber dynamics for the Ising model on a $b$-ary tree mixes in $O(n \log n)$ steps, provided $\theta < 1/(b + 1)$. We now improve this, showing that the same coupling contracts a weighted path metric whenever $\theta < 1/(2\sqrt{b})$. While this result is not the best possible (see the Notes), it does illustrate the utility of allowing for variable edge lengths in the path metric.

Let $T$ be a finite, rooted $b$-ary tree of depth $k$. Fix $0 < \alpha < 1$. We define a graph with vertex set $\{-1, 1\}^T$ by placing an edge between configurations $\sigma$ and $\tau$ if they agree everywhere except at a single vertex $v$. The length of this edge is defined to be $\alpha^{|v|-k}$, where $|v|$ denotes the depth of vertex $v$. The shortest path between arbitrary configurations $\sigma$ and $\tau$ has length

$$ \rho(\sigma, \tau) = \sum_{v \in T} \alpha^{|v|-k}\mathbf{1}_{\{\sigma(v) \neq \tau(v)\}}. \tag{15.18} $$

THEOREM 15.6. *Let $\theta := \tanh(\beta)$. Consider the Glauber dynamics for the Ising model on $T$, the finite rooted $b$-ary tree of depth $k$, that has $n \asymp b^k$ vertices. If $\alpha = 1/\sqrt{b}$, then for any pair of neighboring configurations $\sigma$ and $\tau$, there is a coupling $(X_1, Y_1)$ of the Glauber dynamics started from $\sigma$ and $\tau$ such that the metric $\rho$ defined in (15.18) contracts when $\theta < 1/(2\sqrt{b})$: For $c_\theta := 1 - 2\theta\sqrt{b}$, we have*

$$ \mathbf{E}_{\sigma, \tau}[\rho(X_1, Y_1)] \leq \left(1 - \frac{c_\theta}{n}\right)\rho(\sigma, \tau). $$

### PDF page 237 (book page 221)

*Therefore, if $\theta < 1/(2\sqrt{b})$, then*

$$ t_{\mathrm{mix}}(\varepsilon) \leq \frac{n}{c_\theta} \left[ \frac{3}{2} \log n + \log(1/\varepsilon) \right]. $$

PROOF. Suppose that $\sigma$ and $\tau$ are configurations which agree everywhere except $v$, where $-1 = \sigma(v) = -\tau(v)$. Therefore, $\rho(\sigma, \tau) = \alpha^{|v|-k}$. Let $(X_1, Y_1)$ be one step of the coupling used in Theorem 15.1.

We say the coupling **fails** if a neighbor $w$ of $v$ is selected and the coupling does not update the spin at $w$ identically in both $\sigma$ and $\tau$. Given a neighbor of $v$ is selected for updating, the coupling fails with probability

$$ p(\tau, w) - p(\sigma, w) \leq \theta. $$

(See (15.12).)

If a child $w$ of $v$ is selected for updating and the coupling fails, then the distance increases by

$$ \rho(X_1, Y_1) - \rho(\sigma, \tau) = \alpha^{|v|-k+1} = \alpha \rho(\sigma, \tau). $$

If the parent of $v$ is selected for updating and the coupling fails, then the distance increases by

$$ \rho(X_1, Y_1) - \rho(\sigma, \tau) = \alpha^{|v|-k-1} = \alpha^{-1} \rho(\sigma, \tau). $$

Therefore,

$$ \frac{\mathbf{E}_{\sigma,\tau}[\rho(X_1, Y_1)]}{\rho(\sigma, \tau)} \leq 1 - \frac{1}{n} + \frac{(\alpha^{-1} + b\alpha)\theta}{n}. \tag{15.19} $$

The function $\alpha \mapsto \alpha^{-1} + b\alpha$ is minimized over $[0,1]$ at $\alpha = 1/\sqrt{b}$, where it has value $2\sqrt{b}$. Thus, the right-hand side of (15.19), for this choice of $\alpha$, equals

$$ 1 - \frac{1 - 2\theta\sqrt{b}}{n}. $$

For $\theta < 1/[2\sqrt{b}]$ we obtain a contraction.

The diameter of the tree in the metric $\rho$ is not more than $\alpha^{-k} n = b^{k/2} n$. Since $b^k < n$, the diameter is at most $n^{3/2}$. Applying Corollary 14.8 completes the proof. $\blacksquare$

We now show that at any temperature, the mixing time on a finite $b$-ary tree is at most polynomial in the volume of the tree.

THEOREM 15.7. *The Glauber dynamics for the Ising model on the finite, rooted, $b$-ary tree of depth $k$ satisfies*

$$ t_{\mathrm{rel}} \leq n_k^{c_T(\beta,b)}, $$

*where $c_T(\beta,b) := 2\beta(3b+1)/\log b + 1$ and $n_k$ is the number of vertices in the tree.*

To prove Theorem 15.7, we first need a proposition showing the effect on the dynamics of removing an edge of the underlying graph. The following applies more generally than for trees.

PROPOSITION 15.8. *Let $G = (V, E)$ have maximum degree $\Delta$, where $|V| = n$, and let $\tilde{G} = (V, \tilde{E})$, where $\tilde{E} \subset E$. Let $r = |E \setminus \tilde{E}|$. If $\gamma$ is the spectral gap for Glauber dynamics for the Ising model on $G$ and $\tilde{\gamma}$ is the spectral gap for the dynamics on $\tilde{G}$, then*

$$ \frac{1}{\gamma} \leq \frac{e^{2\beta(\Delta+2r)}}{\tilde{\gamma}} $$

### PDF page 238 (book page 222)

**FIGURE 15.2.** The tree $\tilde{T}_{2,3}$. *[Figure: a binary tree of depth 3 with edges to the root removed. An isolated root vertex sits at the top; below it, two disjoint subtrees, each a rooted binary tree of depth 2 (one internal root, two children, and four leaves).]*

PROOF. We have for any $\sigma \in \{-1, 1\}^V$,

$$ \begin{aligned} \pi(\sigma) &= \frac{e^{\beta \sum_{\{v,w\} \in \tilde{E}} \sigma(v)\sigma(w) + \beta \sum_{\{v,w\} \in E \setminus \tilde{E}} \sigma(v)\sigma(w)}}{\sum_\tau e^{\beta \sum_{\{v,w\} \in \tilde{E}} \tau(v)\tau(w) + \beta \sum_{\{v,w\} \in E \setminus \tilde{E}} \tau(v)\tau(w)}} \\ &\geq \frac{e^{-\beta r}}{e^{\beta r}} \frac{e^{\beta \sum_{\{v,w\} \in \tilde{E}} \sigma(v)\sigma(w)}}{\sum_\tau e^{\beta \sum_{\{v,w\} \in \tilde{E}} \tau(v)\tau(w)}} \\ &= e^{-2\beta r} \tilde{\pi}(\sigma). \end{aligned} $$

Therefore,

$$ \tilde{\pi}(\sigma) \leq e^{2\beta r} \pi(\sigma). \tag{15.20} $$

Since the transition matrix is given by (3.12), for any configurations $\sigma$ and $\tau$, we have

$$ P(\sigma, \tau) \geq \frac{1}{n} \frac{1}{1 + e^{2\beta\Delta}} \mathbf{1}\{P(\sigma, \tau) > 0\} $$

and also

$$ \tilde{P}(\sigma, \tau) \leq \frac{1}{n} \frac{e^{2\beta\Delta}}{1 + e^{2\beta\Delta}} \mathbf{1}\{P(\sigma, \tau) > 0\}. $$

Combining these two inequalities shows that $\tilde{P}(\sigma, \tau) \leq e^{2\beta\Delta} P(\sigma, \tau)$, whence by (15.20) we have

$$ \tilde{\pi}(\sigma)\tilde{P}(\sigma, \tau) \leq e^{2\beta(\Delta+r)} \pi(\sigma) P(\sigma, \tau), $$

and by (13.2), $\tilde{\mathcal{E}}(f) \leq e^{2\beta(\Delta+r)} \mathcal{E}(f)$ for any function $f$. Since $\pi(\sigma) \leq e^{2\beta r} \tilde{\pi}(\sigma)$ (as seen by reversing the roles of $\pi$ and $\tilde{\pi}$ in the proof of (15.20)), by Lemma 13.18 we have that

$$ \tilde{\gamma} \leq e^{2\beta(\Delta+2r)} \gamma. $$

$\blacksquare$

PROOF OF THEOREM 15.7. Let $\tilde{T}_{b,k}$ be the graph obtained by removing all edges incident to the root. (See Figure 15.2.)

By Proposition 15.8,

$$ \frac{t_{\mathrm{rel}}(T_{k+1})}{n_{k+1}} \leq e^{2\beta(3b+1)} \frac{t_{\mathrm{rel}}(\tilde{T}_{b,k+1})}{n_{k+1}}. $$

### PDF page 239 (book page 223)

Applying Lemma 12.14 shows that

$$ \frac{t_{\mathrm{rel}}(\tilde{T}_{b,k+1})}{n_{k+1}} = \max\left\{ 1, \frac{t_{\mathrm{rel}}(T_k)}{n_k} \right\}. $$

Therefore, if $t_k := t_{\mathrm{rel}}(T_k)/n_k$, then $t_{k+1} \leq e^{2\beta(3b+1)} \max\{t_k, 1\}$. We conclude that, since $n_k \geq b^k$,

$$ t_{\mathrm{rel}}(T_k) \leq e^{2\beta(3b+1)k} n_k = (b^k)^{2\beta(3b+1)/\log b} n_k \leq n_k^{1+2\beta(3b+1)/\log b}. $$

$\blacksquare$

REMARK 15.9. The proof of Theorem 15.7 shows the utility of studying product systems. Even though the dynamics on the tree does not have independent components, it can be compared to the dynamics on disjoint components, which has product form.

### **15.5. Block Dynamics**

Let $V_i \subset V$ for $i = 1, \ldots, b$ be subsets of vertices, which we will refer to as **blocks**. The **block dynamics** for the Ising model is the Markov chain defined as follows: a block $V_i$ is picked uniformly at random among the $b$ blocks, and the configuration $\sigma$ is updated according to the measure $\pi$ conditioned to agree with $\sigma$ everywhere outside of $V_i$. More precisely, for $W \subset V$ let

$$ \mathcal{X}_{\sigma,W} := \{\tau \in \mathcal{X} \,:\, \tau(v) = \sigma(v) \text{ for all } v \notin W\} $$

be the set of configurations agreeing with $\sigma$ outside of $W$, and define the transition matrix

$$ P_W(\sigma, \tau) := \pi(\tau \mid \mathcal{X}_{\sigma,W}) = \frac{\pi(\tau)\mathbf{1}_{\{\tau \in \mathcal{X}_{\sigma,W}\}}}{\pi(\mathcal{X}_{\sigma,W})}. $$

The block dynamics has transition matrix $\tilde{P} := b^{-1} \sum_{i=1}^b P_{V_i}$.

THEOREM 15.10. *Consider the block dynamics for the Ising model, with blocks $\{V_i\}_{i=1}^b$. Let $M := \max_{1 \leq i \leq b} |V_i|$, and let $M_\star := \max_{v \in V} |\{i \,:\, v \in V_i\}|$. Assume that $\bigcup_{i=1}^b V_i = V$. Write $\gamma_B$ for the spectral gap of the block dynamics and $\gamma$ for the spectral gap of the single-site dynamics. Let $\Delta$ denote the maximum degree of the graph. Then*

$$ \gamma_B \leq \left[ M^2 \cdot M_\star \cdot (4e^{2\beta\Delta(M+1)}) \right] \gamma. $$

PROOF. We will apply the Comparison Theorem (Theorem 13.20), which requires that we define, for each block move from $\sigma$ to $\tau$, a sequence of single-site moves starting from $\sigma$ and ending at $\tau$.

For $\sigma$ and $\tau$ which differ only in the block $W$, define the path $\Gamma_{\sigma,\tau}$ as follows: enumerate the vertices where $\sigma$ and $\tau$ differ as $v_1, \ldots, v_r$. Obtain the $k$-th state in the path from the $(k-1)$-st by flipping the spin at $v_k$.

For these paths, we must bound the congestion ratio, defined in (13.13) and denoted here by $R$.

Suppose that $e = (\sigma_0, \tau_0)$, where $\sigma_0$ and $\tau_0$ agree everywhere except at vertex $v$. Since $\tilde{P}(\sigma, \tau) > 0$ only for $\sigma$ and $\tau$ which differ by a single block update, $|\Gamma_{\sigma,\tau}| \leq M$

### PDF page 240 (book page 224)

whenever $\tilde{P}(\sigma, \tau) > 0$. Therefore,

$$ R_e := \frac{1}{Q(e)} \sum_{\substack{\sigma, \tau \\ e \in \Gamma_{\sigma,\tau}}} \pi(\sigma) \tilde{P}(\sigma, \tau) |\Gamma_{\sigma,\tau}| \leq M \sum_{\substack{\sigma, \tau \\ e \in \Gamma_{\sigma,\tau}}} \frac{1}{b} \sum_{i \,:\, v \in V_i} \frac{\pi(\sigma) P_{V_i}(\sigma, \tau)}{\pi(\sigma_0) P(\sigma_0, \tau_0)}. \tag{15.21} $$

Observe that if $\sigma$ and $\tau$ differ at $r$ vertices, say $D = \{v_1, \ldots, v_r\}$, then

$$ \frac{\pi(\sigma)}{\pi(\tau)} = \frac{\exp\left(\beta \sum_{\{u,w\} \cap D \neq \varnothing} \sigma(u)\sigma(w)\right)}{\exp\left(\beta \sum_{\{u,w\} \cap D \neq \varnothing} \tau(u)\tau(w)\right)} $$
$$ \leq e^{2\beta\Delta r}. \tag{15.22} $$

Write $\sigma \overset{V_i}{\to} \tau$ to indicate that $\tau$ can be obtained from $\sigma$ by a $V_i$-block update. Bounding $P_{V_i}(\sigma, \tau)$ above by $\mathbf{1}\{\sigma \overset{V_i}{\to} \tau\}$ and $P(\sigma_0, \tau_0)$ below by $1/(2ne^{2\beta\Delta})$ yields

$$ \frac{P_{V_i}(\sigma, \tau)}{P(\sigma_0, \tau_0)} \leq 2ne^{2\beta\Delta} \mathbf{1}\{\sigma \overset{V_i}{\to} \tau\}. \tag{15.23} $$

Using the bounds (15.22) and (15.23) in (15.21) shows that

$$ R_e \leq \left(\frac{M}{b}\right)\left(2ne^{2\beta\Delta}\right)\left(e^{2\beta\Delta M}\right) \sum_i \mathbf{1}\{v \in V_i\} \sum_{\substack{\sigma, \tau \\ e \in \Gamma_{\sigma,\tau}}} \mathbf{1}\{\sigma \overset{V_i}{\to} \tau\}. \tag{15.24} $$

Since configurations $\sigma$ and $\tau$ differing in a $V_i$-block move and satisfying $e \in \Gamma_{\sigma,\tau}$ both agree with $\sigma_0$ outside $V_i$, there are most $(2^M)^2 = 4^M$ such pairs. Therefore, by (15.24),

$$ R := \max_e R_e \leq 2\left(\frac{n}{b}\right) Me^{2\beta\Delta(M+1)} M_\star 4^M. $$

Since there is at least one block for each site by the hypothesis that $\bigcup V_i = V$, we have $(n/b) \leq M$. Finally, we achieve the bound $R \leq M^2 \cdot M_\star \left(4e^{2\beta\Delta(M+1)}\right)$. $\blacksquare$

The ladder graph shown in Figure 15.3 is essentially a one-dimensional graph, so in view of Theorem 15.5 it should not be surprising that at any temperature it has a relaxation time of the order $n$. The proof is a very nice illustration of the technique of comparing the single-site dynamics to block dynamics.

Write $L_n$ for the ***circular ladder graph*** having vertex set $V = \mathbb{Z}_n \times \{0, 1\}$ and edge set

$$ \{ \{(k,a), (j,a)\} \,:\, j \equiv k - 1 \mod n, \, a \in \{0,1\} \} \cup \{ \{(k,0), (k,1)\} \,:\, k \in \mathbb{Z}_n \}. $$

See Figure 15.3 for an example with $n = 32$. We will call an edge of the form $\{(k,0), (k,1)\}$ a ***rung***.

THEOREM 15.11. *Let $L_n$ denote the circular ladder graph defined above. There exist $c_0(\beta)$ and $c_1(\beta)$, not depending on $n$, such that the Glauber dynamics for the Ising model on $L_n$ satisfies $t_{\mathrm{rel}} \leq c_0(\beta)n$, whence $t_{\mathrm{mix}} \leq c_1(\beta)n^2$.*

PROOF. Define the random variable $\Upsilon_k$ on the probability space $(\{-1,1\}^V, \pi)$ by $\Upsilon_k(\sigma) := (\sigma(k,0), \sigma(k,1))$. That is, $\Upsilon_k(\sigma)$ is the pair of spins on the $k$-th rung in configuration $\sigma$.

Define the *$j$-th $\ell$-block* to be the vertex set

$$ V_j := \{(k,a) \,:\, j + 1 \leq k \leq j + \ell, \, a \in \{0,1\}\}. $$

### PDF page 241 (book page 225)

**FIGURE 15.3.** The ladder graph with $n = 32$. The set of vertices enclosed in the dashed box is a block of length $\ell = 3$. *[Figure: a three-dimensional drawing of a circular ladder graph — two concentric rings of vertices connected by vertical rungs, forming a prism-like cylinder. A dashed rectangular box in the front encloses three consecutive rungs, marking a block of length $\ell = 3$.]*

For $j \leq i < j + \ell$, the conditional distribution of $\Upsilon_{i+1}$, given $(\Upsilon_j, \ldots, \Upsilon_i)$ and $\Upsilon_{j+\ell+1}$, depends only on $\Upsilon_i$ and $\Upsilon_{j+\ell+1}$. Therefore, given $\Upsilon_j$ and $\Upsilon_{j+\ell+1}$, the sequence $(\Upsilon_i)_{i=j}^{j+\ell}$ is a time-inhomogeneous Markov chain. If block $V_j$ is selected to be updated in the block dynamics, the update can be realized by running this chain. We call this the ***sequential*** method of updating.

We now describe how to couple the block dynamics started from $\sigma$ with the block dynamics started from $\tau$, in the case that $\sigma$ and $\tau$ differ at only a single site, say $(j, a)$. Always select the same block to update in both chains. If a block is selected which contains $(j, a)$, then the two chains can be updated together, and the difference at $(j, a)$ is eliminated. The only difficulty occurs when $(j, a)$ is a neighbor of a vertex belonging to the selected block.

We treat the case where block $V_j$ is selected; the case where the block is immediately to the left of $(j, a)$ is identical. We will use the sequential method of updating on both chains. Let $(\Upsilon_i)_{i=j}^{j+\ell}$ denote the chain used to update $\sigma$, and let $(\tilde{\Upsilon}_i)_{i=j}^{j+\ell}$ denote the chain used to update $\tau$. We run $\Upsilon$ and $\tilde{\Upsilon}$ independently until they meet, and after the two chains meet, we perform identical transitions in the two chains.

Since $\pi(\sigma)/\pi(\tilde{\sigma}) \leq e^{10\beta}$ when $\sigma$ and $\tilde{\sigma}$ differ on a rung (as at most 5 edges are involved), the probability that the spins on a rung take any of the four possible $\pm 1$ pairs, given the spins outside the rung, is at least $[4e^{10\beta}]^{-1}$. Thus, as the sequential update chains move across the rungs, at each rung there is a chance of at least $(1/4)e^{-20\beta}$, given the previous rungs, that the two chains will have the same value. Therefore, the expected total number of vertices where the two updates disagree is bounded by $8e^{20\beta}$.

Let $\rho$ denote Hamming distance between configurations, so $\rho(\sigma, \tau) = 1$. Let $(X_1, Y_1)$ be the pair of configurations obtained after one step of the coupling. Since $\ell$ of the $n$ blocks will contain $(j, a)$ and two of the blocks have vertices neighboring $(j, a)$, we have

$$ \mathbf{E}_{\sigma,\tau}\rho(X_1, Y_1) \leq 1 - \frac{\ell}{n} + \frac{2}{n} 8e^{20\beta}. $$

If we take $\ell = \ell(\beta) = 16e^{20\beta} + 1$, then

$$ \mathbf{E}_{\sigma,\tau}\rho(X_1, Y_1) \leq 1 - \frac{1}{n} \leq e^{-1/n} \tag{15.25} $$

### PDF page 242 (book page 226)

for any $\sigma$ and $\tau$ with $\rho(\sigma, \tau) = 1$. By Theorem 14.6, for any two configurations $\sigma$ and $\tau$, there exists a coupling $(X_1, Y_1)$ of the block dynamics satisfying

$$ \mathbf{E}_{\sigma,\tau}\rho(X_1, Y_1) \leq \rho(\sigma, \tau)\left(1 - \frac{1}{n}\right). $$

Let $\gamma$ and $\gamma_B$ denote the spectral gaps for the Glauber dynamics and the block dynamics, respectively. Theorem 13.1 implies that $\gamma_B \geq 1/n$. By Theorem 15.10, we conclude that $\gamma \geq c_0(\beta)/n$ for some $c_0(\beta) > 0$. Applying Theorem 12.4 shows that $t_{\mathrm{mix}} \leq c_1(\beta)n^2$. $\blacksquare$

REMARK 15.12. In fact, for the Ising model on the circular ladder graph, $t_{\mathrm{mix}} \leq c(\beta)n \log n$, although different methods are needed to prove this. See **Martinelli (1999)**. In Chapter 22, we will use the censoring inequality (Theorem 22.20) to show that convergence to equilibrium starting from the all-plus state takes $O(n \log n)$ steps; see Theorem 22.25.

**15.6. Lower Bound for Ising on Square\***

Consider the Glauber dynamics for the Ising model in an $n \times n$ box: $V = \{(j,k) \,:\, 0 \leq j, k \leq n - 1\}$ and edges connect vertices at unit Euclidean distance.

In this section we prove

THEOREM 15.13 (**Schonmann (1987)** and **Thomas (1989)**). *The relaxation time $(1 - \lambda_\star)^{-1}$ of the Glauber dynamics for the Ising model in an $n \times n$ square in two dimensions is at least $\exp\left(\psi(\beta)n\right)$, where $\psi(\beta) > 0$ if $\beta$ is large enough.*

*More precisely, let $\alpha_\ell < 3^\ell$ be the number of self-avoiding lattice paths starting from the origin in $\mathbb{Z}^2$ that have length $\ell$, and let $\alpha \leq 3$ be the "connective constant" for the planar square lattice, defined by $\alpha := \lim_{\ell \to \infty} \sqrt[\ell]{\alpha_\ell}$. If $\beta > (1/2)\log(\alpha)$, then $\psi(\beta) > 0$.*

Much sharper and more general results are known; see the partial history in the notes. We provide here a proof following closely the method used in **Randall (2006)** for the hardcore lattice gas.

The key idea in **Randall (2006)** is not to use the usual cut determined by the magnetization (as in the proof of Theorem 15.4), but rather a topological obstruction. As noted by Fabio Martinelli (personal communication), this idea was already present in **Thomas (1989)**, where contours were directly used to define a cut and obtain the right order lower bound for the relaxation time. The argument in **Thomas (1989)** works in all dimensions and hence is harder to read.

REMARK 15.14. An upper bound of order $\exp(C(\beta)n^{d-1})$ on the relaxation time in all dimensions follows from the "path method" of **Sinclair and Jerrum (1989)** for all $\beta$. The constant $C(\beta)$ obtained that way is not optimal.

In proving Theorem 15.13, it will be convenient to attach the spins to the faces (lattice squares) of the lattice rather than the nodes.

DEFINITION 15.15. A ***fault line*** (with at most $k$ defects) is a self-avoiding lattice path from the left side to the right side or from the top to the bottom of $[0, n]^2$, where each edge of the path (with at most $k$ exceptions) is adjacent to two faces with different spins on them. Thus no edges in the fault line are on the boundary of $[0, n]^2$. See Figure 15.4 for an illustration.

### PDF page 243 (book page 227)

*[Figure: a 4×4 grid of lattice squares. In the second row from top, the leftmost two squares are shaded (positive spins), the rest of that row white; in the third row, the middle two squares are shaded; in the bottom row, the middle two squares are shaded. A bold fault line runs along the top edge of the second row for the leftmost two squares, then steps down along the vertical edge, then continues rightward along the lower edge of the second-row/third-row boundary toward the right side.]*

**FIGURE 15.4.** A fault line with one defect. Positive spins are indicated by shaded squares, while negative spins are indicated by white squares. The fault line is drawn in bold.

**LEMMA 15.16.** *Denote by $F_k$ the set of Ising configurations in $[0, n]^2$ that have a fault line with at most $k$ defects. Then $\pi(F_k) \leq \sum_{\ell \geq n} 2(n + 1)\alpha_\ell e^{2\beta(2k-\ell)}$. In particular, if $k$ is fixed and $\beta > (1/2)\log(\alpha)$, then $\pi(F_k)$ decays exponentially in $n$.*

PROOF. For a self-avoiding lattice path $\varphi$ of length $\ell$ from the left side to the right side (or from top to bottom) of $[0, n]^2$, let $F_\varphi$ be the set of Ising configurations in $[0, n]^2$ that have $\varphi$ as a fault line with at most $k$ defects. Flipping all the spins on one side of the fault line (say, the side that contains the upper left corner) defines a one-to-one mapping from $F_\varphi$ to its complement that magnifies probability by a factor of $e^{2\beta(\ell-2k)}$. This yields that $\pi(F_\varphi) \leq e^{2\beta(2k-\ell)}$.

The number of self-avoiding lattice paths from left to right in $[0, n]^2$ is at most $(n + 1)\alpha_\ell$. Thus, summing this over all self-avoiding lattice paths $\varphi$ of length $\ell$ from top to bottom and from left to right of $[0, n]^2$ and over all $\ell \geq n$ completes the proof. $\blacksquare$

**LEMMA 15.17.**
(i) *If in a configuration $\sigma$ there is no all-plus crossing from the left side $L$ of $[0, n]^2$ to the right side $R$ and there is also no all-minus crossing, then there is a fault line with no defects from the top to the bottom of $[0, n]^2$.*
(ii) *Similarly, if $\Gamma_+$ is a path of lattice squares (all labeled plus in $\sigma$) from a square $q$ in $[0, n]^2$ to the top side of $[0, n]^2$ and $\Gamma_-$ is a path of lattice squares (all labeled minus) from the same square $q$ to the top of $[0, n]^2$, then there is a lattice path $\xi$ from the boundary of $q$ to the top of $[0, n]^2$ such that every edge in $\xi$ is adjacent to two lattice squares with different labels in $\sigma$.*

PROOF.
(i) For the first statement, let $A$ be the collection of lattice squares that can be reached from $L$ by a path of lattice squares of the same label in $\sigma$. Let $A^\star$ equal $A$ together with the set of squares that are separated from $R$ by $A$. Then the boundary of $A^\star$ consists of part of the boundary of $[0, n]^2$ and a fault line.

### PDF page 244 (book page 228)

(ii) Suppose $q$ itself is labeled minus in $\sigma$ and $\Gamma_+$ terminates in a square $q_+$ on the top of $[0, n]^2$ which is to the left of the square $q_-$ where $\Gamma_-$ terminates. Let $A_+$ be the collection of lattice squares that can be reached from $\Gamma_+$ by a path of lattice squares labeled plus in $\sigma$ and denote by $A_+^\star$ the set $A_+$ together with the set of squares that are separated from the boundary of $[0, n]^2$ by $A_+$. Let $\xi_1$ be a directed lattice edge with $q$ on its right and a square of $\Gamma_+$ on its left. Continue $\xi_1$ to a directed lattice path $\xi$ leading to the boundary of $[0, n]^2$, by inductively choosing the next edge $\xi_j$ to have a square (labeled plus) of $A_+$ on its left and a square (labeled minus) not in $A_+^\star$ on its right. It is easy to check that such a choice is always possible (until $\xi$ reaches the boundary of $[0, n]^2]$), the path $\xi$ cannot cycle and it must terminate between $q_+$ and $q_-$ on the top side of $[0, n]^2$. $\blacksquare$

PROOF OF THEOREM 15.13. Following **Randall (2006)**, let $S_+$ be the set of configurations that have a top-to-bottom and a left-to-right crossing of pluses. Similarly define $S_-$. Note that $S_+ \cap S_0 = \varnothing$. On the complement of $S_+ \cup S_-$ there is either no monochromatic crossing left-to-right (whence there is a top-to-bottom fault line by Lemma 15.17) or there is no monochromatic crossing top-to-bottom (whence there is a left-to-right fault line). By Lemma 15.16, $\pi(S_+) \to 1/2$ as $n \to \infty$.

Let $\partial S_+$ denote the external vertex boundary of $S_+$, that is, the set of configurations outside $S_+$ that are one flip away from $S_+$. It suffices to show that $\pi(\partial S_+)$ decays exponentially in $n$ for $\beta > \frac{1}{2}\log(\alpha)$. By Lemma 15.16, it is enough to verify that every configuration $\sigma \in \partial S_+$ has a fault line with at most 3 defects.

The case $\sigma \notin S_-$ is handled by Lemma 15.17. Fix $\sigma \in \partial S_+ \cap S_-$ and let $q$ be a lattice square such that flipping $\sigma(q)$ will transform $\sigma$ to an element of $S_+$. By Lemma 15.17, there is a lattice path $\xi$ from the boundary of $q$ to the top of $[0, n]^2$ such that every edge in $\xi$ is adjacent to two lattice squares with different labels in $\sigma$; by symmetry, there is also such a path $\xi^\star$ from the boundary of $q$ to the bottom of $[0, n]^2$. By adding at most three edges of $q$, we can concatenate these paths to obtain a fault line with at most three defects.

Lemma 15.16 completes the proof. $\blacksquare$

<div align="center">

**Exercises**

</div>

EXERCISE 15.1. Show that for Glauber dynamics for the Ising model, for all $\beta$,
$$ t_{\text{rel}} \geq \frac{n}{2}\,. $$
*Hint:* Apply Lemma 13.7 with the test function which is the spin at a single vertex.

EXERCISE 15.2. Let $(G_n)$ be a sequence of expander graphs with maximal degree $\Delta$ and $\Phi_\star(G_n) \geq \varphi$. Find $\beta(\Delta, \varphi)$ such that for $\beta > \beta(\Delta, \varphi)$, the relaxation time of Glauber dynamics for the Ising model on $G_n$ grows exponentially in $n$.

EXERCISE 15.3. Consider the Ising model on the $b$-ary tree of depth $k$, and let $f(\sigma) = \sum_{v \,:\, |v|=k} \sigma(v)$. Let $\theta = \tanh(\beta)$. Show that
$$ \text{Var}_\pi(f) \asymp \sum_{j=0}^{k} b^{k+j}\theta^{2j} \asymp \begin{cases} b^k & \text{if } \theta < 1/\sqrt{b}, \\ kb^k \asymp n\log n & \text{if } \theta = 1/\sqrt{b}, \\ (b\theta)^{2k} \asymp n^{1+\alpha} & \text{if } \theta > 1/\sqrt{b}, \end{cases} $$

### PDF page 245 (book page 229)

where $\alpha = \log(b\theta^2)/\log(b) > 0$. (Recall that $a_n \asymp b_n$ means that there are non-zero and finite constants $c$ and $C$ such that $c \leq a_n/b_n \leq C$.) Use this to obtain lower bounds on $t_{\text{rel}}$ in the three regimes.

EXERCISE 15.4. Let $G$ be a graph with vertex set $V$ of size $n$ and maximal degree $\Delta$. Let $\pi_\beta$ be the Ising model on $G$, and assume that $\beta$ satisfies $\Delta \tanh(\beta) < 1$. Show that there is a constant $C(\beta)$ such that any $f$ of the form $f(\sigma) = \sum_{v \in V} a_v \sigma(v)$, where $|a_v| \leq 1$, has $\text{Var}_{\pi_\beta}(f) \leq C(\beta)n$.
*Hint:* Use (15.2) together with Lemma 13.7.

EXERCISE 15.5. In the same set-up as the previous exercise, show that there is a constant $C_2(\beta)$ such that any $f(\sigma) = \sum_{w,v \in V} a_{v,w}\sigma(v)\sigma(w)$ with $|a_{v,w}| \leq 1$ satisfies $\text{Var}_{\pi_\beta}(f) \leq C_2(\beta)n^2$.

EXERCISE 15.6.
(a) For the rectangle $\{1, \ldots, k\} \times \{1, \ldots, \ell\} \subset \mathbb{Z}^2$, show that the cut-width $w_G$ (defined in the Notes) satisfies $|w_G - \min\{k, \ell\}| \leq 1$.
(b) For $G = \mathbb{Z}_n^d$, show that $w_G$ is of order $n^{d-1}$.
(c) For $G$ any tree of depth $k$ and maximum degree $\Delta$, show that $w_G$ is at most $\Delta k$.

<div align="center">

**Notes**

</div>

The upper and lower bounds obtained in Theorem 15.5 for the mixing time for Glauber dynamics on the cycle are within a factor of two of each other. The lower bound is sharp as was proven by **Lubetzky and Sly (2013)**. A simpler proof was later given in **Cox, Peres, and Steif (2016)**.

Theorem 15.7 is due to **Kenyon, Mossel, and Peres (2001)**. They showed that the relaxation time of the Glauber dynamics for the Ising model on the $b$-ary tree has the following behavior: if $\theta < 1/\sqrt{b}$, then $t_{\text{rel}} \asymp n$, if $\theta = 1/\sqrt{b}$, then $t_{\text{rel}} \asymp n\log n$, and if $\theta > 1/\sqrt{b}$, then $t_{\text{rel}} \geq c_1 n^{1+\alpha}$, where $\alpha > 0$ depends on $\beta$. The case $\theta > 1/\sqrt{b}$ can be proved by using the function $f(\sigma) = \sum_{\text{leaves}} \sigma(v)$ in the variational principle (Lemma 13.7); see Exercise 15.3. See **Berger, Kenyon, Mossel, and Peres (2005)** and **Martinelli, Sinclair, and Weitz (2004)** for extensions.

**Levin, Luczak, and Peres (2010)** showed that at the critical parameter $\beta = 1/n$ for the Ising model on the complete graph, the mixing time of the Glauber dynamics satisfies $1/c \leq \frac{t_{\text{mix}}}{n^{3/2}} \leq c$ for a constant $c$. The same paper also showed that if $\beta = \alpha/n$ with $\alpha > 1$ and the dynamics are restricted to the part of the state space where $\sum \sigma(v) > 0$, then $t_{\text{mix}} = O(n\log n)$. In the case where $\alpha < 1$, they show that the chain has a cutoff. (See Chapter 18 for the definition of cutoff.) These results were further refined by **Ding, Lubetzky, and Peres (2009)**.

**A partial history of Ising on the square lattice.** For the ferromagnetic Ising model with no external field and free boundary, **Chayes, Chayes, and Schonmann (1987)**, based on earlier work of **Schonmann (1987)**, proved

THEOREM 15.18. *In dimension 2, let $m^\star$ denote the "spontaneous magnetization", i.e., the expected spin at the origin in the plus measure in the whole lattice. Denote by $p(n; a, b)$ the probability that the magnetization (average of spins) in an $n \times n$ square is in an interval $(a, b)$. If $-m^\star < a < b < m^\star$, then $p(n; a, b)$ decays exponentially in $n$.*

### PDF page 246 (book page 230)

(The rate function was not obtained, only upper and lower bounds.)

Using the easy direction of the Cheeger inequality (Theorem 13.10), which is an immediate consequence of the variational formula for eigenvalues, this yields Theorem 15.13 for all $\beta > \beta_c$ in $\mathbb{Z}^2$. (For the planar square lattice Onsager proved that $\beta_c = \log(1 + \sqrt{2})/2$; see Chapter II of **Simon (1993)**.)

Theorem 15.13 was stated explicitly and proved in **Thomas (1989)** who extended it to all dimensions $d \geq 2$. He did not use the magnetization to define a cut, but instead his cut was defined by configurations where there is a contour of length (or in higher dimensions $d \geq 3$, surface area) larger than $an^{d-1}$ for a suitable small $a > 0$. Again the rate function was only obtained up to a constant factor and he assumed $\beta$ was large enough for a Peierls argument to work.

In the breakthrough book of **Dobrushin, Kotecký, and Shlosman (1992)** the correct rate function (involving surface tension) for the large deviations of magnetization in 2 dimensions was identified and established for large $\beta$.

This was extended by **Ioffe (1995)** to all $\beta > \beta_c$. The consequences for mixing time (a sharp lower bound) and a corresponding sharp upper bound were established in **Cesi, Guadagni, Martinelli, and Schonmann (1996)**.

In higher dimensions, a lower bound for mixing time of the right order (exponential in $n^{d-1}$) for all $\beta > \beta_c(d)$ follows from the magnetization large deviation bounds of **Pisztora (1996)** combined with the work of **Bodineau (2005)**.

Other key papers about the Ising model on the lattice and the corresponding Glauber dynamics include **Dobrushin and Shlosman (1987)**, **Stroock and Zegarliński (1992)**, **Martinelli and Olivieri (1994)**, and **Martinelli, Olivieri, and Schonmann (1994)**.

**Lubetzky and Sly (2013)** and **Lubetzky and Sly (2016)** showed that the Glauber dynamics for the Ising model on $\mathbb{Z}_n^d$ has cutoff for $\beta < \beta_c$. In **Lubetzky and Sly (2012)** they show that at $\beta_c$ on $\mathbb{Z}_n^2$, the mixing time is polynomial in $n$.

The *cut-width* $w_G$ of a graph $G$ is the smallest integer such that there exists a labeling $v_1, \ldots, v_n$ of the vertices such that for all $1 \leq k \leq n$, the number of edges from $\{v_1, \ldots, v_k\}$ to $\{v_{k+1}, \ldots, v_n\}$, is at most $w_G$. See Exercise 15.6 for examples of cut-width.

For the Ising model on a finite graph $G$ with $n$ vertices and maximal degree $\Delta$,

$$ t_{\mathrm{rel}} \leq n^2 e^{(4w_G + 2\Delta)\beta} . $$

This is proved using the ideas of **Jerrum and Sinclair (1989)** in Proposition 1.1 of **Kenyon, Mossel, and Peres (2001)**.

A different Markov chain which has the Ising model as its stationary distribution is the Swendsen-Wang dynamics. This is analyzed in detail on the complete graph in **Long, Nachmias, Ning, and Peres (2014)**. **Guo and Jerrum (2017)** show that this chain has a polynomial mixing time on any graph.

A natural generalization of the Ising model is the **Potts model**, where the spins takes values $\{1, \ldots, q\}$ and the probability of a configuration is

$$ \mu_\beta(\sigma) = Z_\beta^{-1} e^{\beta \sum_{u \sim v} \mathbf{1}\{\sigma(u) = \sigma(v)\}} . $$

A modification of the proof of Theorem 15.1 shows that for $\beta$ sufficiently small (depending on the maximal degree of the graph), there is a contractive coupling of the corresponding Glauber dynamics. Therefore, for $\beta$ in this range, $t_{\mathrm{rel}} = O(n)$ and $t_{\mathrm{mix}} = O(n \log n)$. **Lubetzky and Sly (2014a)** show cutoff for the Glauber dynamics for the Potts model on $\mathbb{Z}_n^d$, for $\beta$ sufficiently small. **Borgs, Chayes,**

### PDF page 247 (book page 231)

**Frieze, Kim, Tetali, Vigoda, and Vu (1999)** show that the Glauber dynamics for the Potts model mixes slowly for large $\beta$; see also **Borgs, Chayes, and Tetali (2012)**. **Gheissari and Lubetzky (2016)** analyze the critical case on $\mathbb{Z}_n^2$. See **Cuff, Ding, Louidor, Lubetzky, Peres, and Sly (2012)** for the full story on the complete graph.

**Further reading.** An excellent source on dynamics for the Ising model is **Martinelli (1999)**. **Simon (1993)** contains more on the Ising model. Ising's thesis (published as **Ising (1925)**) concerned the one-dimensional model. For information on the life of Ising, see **Kobe (1997)**.

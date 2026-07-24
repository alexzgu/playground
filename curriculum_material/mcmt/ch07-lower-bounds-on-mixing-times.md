# Chapter 7 — Lower Bounds on Mixing Times
*(PDF pages 104–115; book pages 88–99)*

### PDF page 104 (book page 88)

CHAPTER 7

# Lower Bounds on Mixing Times

So far, we have focused on finding upper bounds on $t_{\mathrm{mix}}$. It is natural to ask if a given upper bound is the best possible, and so in this chapter we turn to methods of obtaining lower bounds on $t_{\mathrm{mix}}$.

**7.1. Counting and Diameter Bounds**

**7.1.1. Counting bound.** If the possible locations of a chain after $t$ steps do not form a significant fraction of the state space, then the distribution of the chain at time $t$ cannot be close to uniform. This idea can be used to obtain lower bounds on the mixing time.

Let $(X_t)$ be a Markov chain with irreducible and aperiodic transition matrix $P$ on the state space $\mathcal{X}$, and suppose that the stationary distribution $\pi$ is uniform over $\mathcal{X}$. Define $d_{\mathrm{out}}(x) := |\{y \,:\, P(x,y) > 0\}|$ to be the number of states accessible in one step from $x$, and let

$$ \Delta := \max_{x \in \mathcal{X}} d_{\mathrm{out}}(x). \tag{7.1} $$

Denote by $\mathcal{X}_t^x$ the set of states accessible from $x$ in exactly $t$ steps, and observe that $|\mathcal{X}_t^x| \leq \Delta^t$. If $\Delta^t < (1 - \varepsilon)|\mathcal{X}|$, then from the definition of total variation distance we have that

$$ \left\|P^t(x, \cdot) - \pi\right\|_{\mathrm{TV}} \geq P^t(x, \mathcal{X}_t^x) - \pi(\mathcal{X}_t^x) \geq 1 - \frac{\Delta^t}{|\mathcal{X}|} > \varepsilon. $$

This implies that

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{\log(|\mathcal{X}|(1 - \varepsilon))}{\log \Delta}. \tag{7.2} $$

In the reversible case when $\Delta \geq 3$, we have

$$ |\mathcal{X}_t^x| \leq 1 + \Delta \sum_{j=1}^{t-1} (\Delta - 1)^j \leq 3(\Delta - 1)^t \,, $$

so

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{\log(|\mathcal{X}|(1 - \varepsilon)/3)}{\log(\Delta - 1)} \,. \tag{7.3} $$

EXAMPLE 7.1. For random walk on a $d$-regular graph $(d \geq 3)$, the stationary distribution is uniform, so

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{\log(|\mathcal{X}|(1 - \varepsilon)/3)}{\log(d - 1)} \,. $$

We use the bound (7.2) to bound below the mixing time for the riffle shuffle in Proposition 8.13.

### PDF page 105 (book page 89)

**7.1.2. Diameter bound.** Given a transition matrix $P$ on $\mathcal{X}$, construct a graph with vertex set $\mathcal{X}$ and which includes the edge $\{x,y\}$ for all $x$ and $y$ with $P(x,y) + P(y,x) > 0$. Define the ***diameter*** of a Markov chain to be the diameter of this graph, that is, the maximal graph distance between distinct vertices.

Let $P$ be an irreducible and aperiodic transition matrix on $\mathcal{X}$ with diameter $L$, and suppose that $x_0$ and $y_0$ are states at maximal graph distance $L$. Then $P^{\lfloor (L-1)/2 \rfloor}(x_0, \cdot)$ and $P^{\lfloor (L-1)/2 \rfloor}(y_0, \cdot)$ are positive on disjoint vertex sets. Consequently, $\bar{d}(\lfloor (L-1)/2 \rfloor) = 1$ and for any $\varepsilon < 1/2$,

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{L}{2}. \tag{7.4} $$

REMARK 7.2. Recalling the definition of $t_{\mathrm{Ces}}$ from Section 6.6, the same proof shows that $t_{\mathrm{Ces}}(\varepsilon) \geq \frac{L}{2}$ for any $\varepsilon < 1/2$.

**7.2. Bottleneck Ratio**

***Bottlenecks*** in the state space $\mathcal{X}$ of a Markov chain are geometric features that control mixing time. A bottleneck makes portions of $\mathcal{X}$ difficult to reach from some starting locations, limiting the speed of convergence. Figure 7.1 is a sketch of a graph with an obvious bottleneck.

**FIGURE 7.1.** A graph with a bottleneck. *[Figure: a cross-hatched shape resembling two rounded blobs joined by a narrow neck (a dumbbell/peanut form), illustrating a bottleneck between two large regions of the state space.]*

As usual, $P$ is the irreducible and aperiodic transition matrix for a Markov chain on $\mathcal{X}$ with stationary distribution $\pi$.

The ***edge measure*** $Q$ is defined by

$$ Q(x,y) := \pi(x)P(x,y), \quad Q(A,B) = \sum_{x \in A, y \in B} Q(x,y). \tag{7.5} $$

Here $Q(A,B)$ is the probability of moving from $A$ to $B$ in one step when starting from the stationary distribution.

The ***bottleneck ratio*** of the set $S$ is defined to be

$$ \Phi(S) := \frac{Q(S, S^c)}{\pi(S)}, \tag{7.6} $$

while the bottleneck ratio of the whole chain (also known as the ***expansion***) is

$$ \Phi_\star := \min_{S \,:\, \pi(S) \leq \frac{1}{2}} \Phi(S). \tag{7.7} $$

### PDF page 106 (book page 90)

**FIGURE 7.2.** Two "glued" two-dimensional tori. *[Figure: two side-by-side circular-torus graphs, each a dense mesh of vertices and edges, meeting at one shared vertex.]*

For simple random walk on a graph with vertices $\mathcal{X}$ and edge set $E$,

$$ Q(x,y) = \begin{cases} \frac{\deg(x)}{2|E|} \frac{1}{\deg(x)} = \frac{1}{2|E|} & \text{if } \{x,y\} \text{ is an edge,} \\ 0 & \text{otherwise.} \end{cases} $$

In this case, $2|E|Q(S, S^c)$ is the size of the **boundary** $\partial S$ of $S$, the collection of edges having one vertex in $S$ and one vertex in $S^c$. The bottleneck ratio, in this case, becomes

$$ \Phi(S) = \frac{|\partial S|}{\sum_{x \in S} \deg(x)}. \tag{7.8} $$

REMARK 7.3. If the walk is lazy, then $Q(x,y) = (4|E|)^{-1}\mathbf{1}_{\{\{x,y\}\in E\}}$, and the bottleneck ratio equals $\Phi(S) = |\partial S|/(2\sum_{x \in S} \deg(x))$.

If the graph is regular with degree $d$, then $\Phi(S) = d^{-1}|\partial S|/|S|$, which is proportional to the ratio of the size of the boundary of $S$ to the volume of $S$.

The relationship of $\Phi_\star$ to $t_{\mathrm{mix}}$ is the following theorem:

THEOREM 7.4. *If $\Phi_\star$ is the bottleneck ratio defined in* (7.7), *then*

$$ t_{\mathrm{mix}} = t_{\mathrm{mix}}(1/4) \geq \frac{1}{4\Phi_\star}. \tag{7.9} $$

PROOF. Consider a stationary chain $\{X_t\}$, so that $X_0$ (and necessarily $X_t$ for all $t$) has distribution $\pi$. For this chain,

$$ \begin{aligned} \mathbf{P}_\pi\{X_0 \in A, \ X_t \in A^c\} &\leq \sum_{r=1}^{t} \mathbf{P}_\pi\{X_{r-1} \in A, \ X_r \in A^c\} \\ &= t\mathbf{P}_\pi\{X_0 \in A, \ X_1 \in A^c\} \\ &= tQ(A, A^c). \end{aligned} $$

Dividing by $\pi(A)$ shows that

$$ \mathbf{P}_\pi\{X_t \in A^c \mid X_0 \in A\} \leq t\Phi(A), \tag{7.10} $$

so there exists $x$ with $P^t(x, A) \geq 1 - t\Phi(A)$. Therefore,

$$ d(t) \geq 1 - t\Phi(A) - \pi(A). $$

If $\pi(A) \leq 1/2$ and $t < 1/[4\Phi(A)]$, then $d(t) > 1/4$. Therefore, $t_{\mathrm{mix}} \geq 1/[4\Phi(A)]$. Maximizing over $A$ with $\pi(A) \leq 1/2$ completes the proof. $\blacksquare$

### PDF page 107 (book page 91)

**FIGURE 7.3.** The star graph with 11 vertices. *[Figure: a star graph — one central vertex connected by straight edges to 10 outer vertices radiating in all directions.]*

EXAMPLE 7.5 (Two glued tori). Consider the graph consisting of two copies of the $d$-dimensional torus $\mathbb{Z}_n^d$ "glued" together at a single vertex $v^\star$; see Figure 7.2 for an example of dimension two. Denote by $V_1$ and $V_2$ the sets of vertices in the right and left tori, respectively. Note that $V_1 \cap V_2 = \{v^\star\}$. Let $A = V_1 \setminus \{v^\star\}$.

The set $\partial A$ consists of $2d$ edges. Also, $\sum_{x \in A} \deg(x) = 2d(n^d - 1)$. Consequently, the lazy random walk on this graph has

$$ \Phi_\star \leq \Phi(A) = \frac{2d}{2[2d(n^d - 1)]} = \frac{1}{2(n^d - 1)}. $$

(See Remark 7.3.) Theorem 7.4 implies that $t_{\mathrm{mix}} \geq (n^d - 1)/2$. In Corollary 10.30 we prove a matching upper bound of order $n^d$ for $d \geq 3$ and show that the correct order of $t_{\mathrm{mix}}$ for $d = 2$ is $n^2 \log n$.

EXAMPLE 7.6 (Coloring the star). Let $\mathcal{X}$ be the set of all proper $q$-colorings of a graph $G$, and let $\pi$ be the uniform distribution on $\mathcal{X}$. Recall from Example 3.5 that Glauber dynamics for $\pi$ is the Markov chain which makes transitions as follows: at each step, a vertex is chosen from $V$ uniformly at random, and the color at this vertex is chosen uniformly at random from all **feasible colors**. The feasible colors at vertex $v$ are all colors *not* present among the neighbors of $v$.

We will prove (Theorem 14.10) that if $q > 2\Delta$, where $\Delta$ is the maximum degree of the graph, then the Glauber dynamics has mixing time $O(|V| \log |V|)$.

We show, by example, that quite different behavior may occur if the maximal degree is large compared to $q$.

The graph we study here is the **star** with $n$ vertices, shown in Figure 7.3. This graph is a tree of depth 1 with $n - 1$ leaves.

Let $v_\star$ denote the root vertex and let $S \subseteq \mathcal{X}$ be the set of proper colorings such that $v_\star$ has color 1:

$$ S := \{x \in \mathcal{X} \ : \ x(v_\star) = 1\}. $$

For $(x, y) \in S \times S^c$, the edge measure $Q(x,y)$ is non-zero if and only if
- $x(v_\star) = 1$ and $y(v_\star) \neq 1$,
- $x(v) = y(v)$ for all leaves $v$, and
- $x(v) \notin \{1, y(v_\star)\}$ for all leaves $v$.

### PDF page 108 (book page 92)

The number of such $(x, y)$ pairs is therefore equal to $(q-1)(q-2)^{n-1}$, since there are $(q-1)$ possibilities for the color $y(v_\star)$ and $(q-2)$ possibilities for the color (identical in both $x$ and $y$) of each of the $n-1$ leaves. Also, for such pairs, $Q(x,y) \leq (|\mathcal{X}|n)^{-1}$. It follows that

$$ \sum_{x \in S, y \in S^c} Q(x, y) \leq \frac{1}{|\mathcal{X}|n}(q-1)(q-2)^{n-1}. \tag{7.11} $$

Since $x \in S$ if and only if $x(v_\star) = 1$ and $x(v) \neq 1$ for all $v \neq v_\star$, we have that $|S| = (q-1)^{n-1}$. Together with (7.11), this implies

$$ \frac{Q(S, S^c)}{\pi(S)} \leq \frac{(q-1)(q-2)^{n-1}}{n(q-1)^{n-1}} = \frac{(q-1)^2}{n(q-2)}\left(1 - \frac{1}{q-1}\right)^n \leq \frac{(q-1)^2}{n(q-2)}e^{-n/(q-1)}. $$

Consequently, by Theorem 7.4, the mixing time is at least of exponential order:

$$ t_{\mathrm{mix}} \geq \frac{n(q-2)}{4(q-1)^2}e^{n/(q-1)}. $$

REMARK 7.7. In fact, this argument shows that if $n/(q \log q) \to \infty$, then $t_{\mathrm{mix}}$ is super-polynomial in $n$.

EXAMPLE 7.8 (Binary tree). Consider the lazy random walk on the rooted binary tree of depth $k$. (See Section 5.3.4 for the definition.) Let $n$ be the number of vertices, so $n = 2^{k+1} - 1$. The number of edges is $n - 1$. In Section 5.3.4 we showed that $t_{\mathrm{mix}} \leq 16n$. We now show that $t_{\mathrm{mix}} \geq (n-2)/2$.

Let $v_0$ denote the root. Label the vertices adjacent to $v_0$ as $v_r$ and $v_\ell$. Call $w$ a **descendant** of $v$ if the shortest path from $w$ to $v_0$ passes through $v$. Let $S$ consist of the right-hand side of the tree, that is, $v_r$ and all of its descendants.

We write $|v|$ for the length of the shortest path from $v$ to $v_0$. By Example 1.12, the stationary distribution is

$$ \pi(v) = \begin{cases} \frac{2}{2n-2} & \text{for } v = v_0, \\ \frac{3}{2n-2} & \text{for } 0 < |v| < k, \\ \frac{1}{2n-2} & \text{for } |v| = k. \end{cases} $$

Summing $\pi(v)$ over $v \in S$ shows that $\pi(S) = (n-2)/(2n-2)$. Since there is only one edge from $S$ to $S^c$,

$$ Q(S, S^c) = \pi(v_r)P(v_r, v_0) = \left(\frac{3}{2n-2}\right)\frac{1}{6} = \frac{1}{4(n-1)}, $$

and so $\Phi(S) = 1/[2(n-2)]$ . Applying Theorem 7.4 establishes the lower bound

$$ t_{\mathrm{mix}} \geq \frac{n-2}{2}. $$

**7.3. Distinguishing Statistics**

One way to produce a lower bound on the mixing time $t_{\mathrm{mix}}$ is to find a statistic $f$ (a real-valued function) on $\mathcal{X}$ such that the distance between the distribution of $f(X_t)$ and the distribution of $f$ under the stationary distribution $\pi$ can be bounded from below.

Let $\mu$ and $\nu$ be two probability distributions on $\mathcal{X}$, and let $f$ be a real-valued function defined on $\mathcal{X}$. We write $E_\mu$ to indicate expectations of random variables

### PDF page 109 (book page 93)

(on sample space $\mathcal{X}$) with respect to the probability distribution $\mu$:

$$ E_\mu(f) := \sum_{x \in \mathcal{X}} f(x)\mu(x). $$

(Note the distinction between $E_\mu$ with $\mathbf{E}_\mu$, the expectation operator corresponding to the Markov chain $(X_t)$ started with initial distribution $\mu$.) Likewise $\mathrm{Var}_\mu(f)$ indicates variance computed with respect to the probability distribution $\mu$.

PROPOSITION 7.9. *For $f : \mathcal{X} \to \mathbb{R}$, define $\sigma_\star^2 := \max\{\mathrm{Var}_\mu(f), \mathrm{Var}_\nu(f)\}$. If*

$$ |E_\nu(f) - E_\mu(f)| \geq r\sigma_\star $$

*then*

$$ \|\mu - \nu\|_{\mathrm{TV}} \geq 1 - \frac{8}{r^2}\,. $$

*In particular, if for a Markov chain $(X_t)$ with transition matrix $P$ the function $f$ satisfies*

$$ |\mathbf{E}_x[f(X_t)] - E_\pi(f)| \geq r\sigma_\star\,, $$

*then*

$$ \left\|P^t(x, \cdot) - \pi\right\|_{\mathrm{TV}} \geq 1 - \frac{8}{r^2}\,. $$

Before proving this, we provide a useful lemma. When $\mu$ is a probability distribution on $\mathcal{X}$ and $f : \mathcal{X} \to \Lambda$, write $\mu f^{-1}$ for the probability distribution defined by

$$ (\mu f^{-1})(A) := \mu(f^{-1}(A)) $$

for $A \subseteq \Lambda$. When $X$ is an $\mathcal{X}$-valued random variable with distribution $\mu$, then $f(X)$ has distribution $\mu f^{-1}$ on $\Lambda$.

LEMMA 7.10. *Let $\mu$ and $\nu$ be probability distributions on $\mathcal{X}$, and let $f : \mathcal{X} \to \Lambda$ be a function on $\mathcal{X}$, where $\Lambda$ is a finite set. Then*

$$ \|\mu - \nu\|_{\mathrm{TV}} \geq \left\|\mu f^{-1} - \nu f^{-1}\right\|_{\mathrm{TV}}\,. $$

PROOF. Since

$$ |\mu f^{-1}(B) - \nu f^{-1}(B)| = |\mu(f^{-1}(B)) - \nu(f^{-1}(B))|, $$

it follows that

$$ \max_{B \subset \Lambda} |\mu f^{-1}(B) - \nu f^{-1}(B)| \leq \max_{A \subset \mathcal{X}} |\mu(A) - \nu(A)|. $$

$\blacksquare$

REMARK 7.11. Lemma 7.10 can be used to lower bound the distance of some chain from stationarity in terms of the corresponding distance for a projection (in the sense of Section 2.3.1) of that chain. To do so, take $\Lambda$ to be the relevant partition of $\mathcal{X}$.

PROOF OF PROPOSITION 7.9. Suppose without loss of generality that $E_\mu(f) \leq E_\nu(f)$. If $A = (E_\mu(f) + r\sigma_\star/2, \infty)$, then Chebyshev's inequality yields that

$$ \mu f^{-1}(A) \leq \frac{4}{r^2} \quad \text{and} \quad \nu f^{-1}(A) \geq 1 - \frac{4}{r^2}, $$

whence

$$ \left\|\mu f^{-1} - \nu f^{-1}\right\|_{\mathrm{TV}} \geq 1 - \frac{8}{r^2}. $$

Lemma 7.10 finishes the proof. $\blacksquare$

### PDF page 110 (book page 94)

The following is similar to Proposition 7.9, but gives a better constant in the lower bound.

PROPOSITION 7.12*. *Let $\mu$ and $\nu$ be two probability distributions on $\mathcal{X}$, and let $f$ be a real-valued function on $\mathcal{X}$. If*

$$ |E_\mu(f) - E_\nu(f)| \geq r\sigma, \tag{7.12} $$

*where $\sigma^2 = [\mathrm{Var}_\mu(f) + \mathrm{Var}_\nu(f)]/2$, then*

$$ \|\mu - \nu\|_{\mathrm{TV}} \geq 1 - \frac{4}{4 + r^2}. \tag{7.13} $$

PROOF OF PROPOSITION 7.12. If $\alpha$ is a probability distribution on a finite subset $\Lambda$ of $\mathbb{R}$, the translation of $\alpha$ by $c$ is the probability distribution $\alpha_c$ on $\Lambda + c$ defined by $\alpha_c(x) = \alpha(x - c)$. Total variation distance is ***translation invariant***: if $\alpha$ and $\beta$ are two probability distributions on a finite subset $\Lambda$ of $\mathbb{R}$, then $\|\alpha_c - \beta_c\|_{\mathrm{TV}} = \|\alpha - \beta\|_{\mathrm{TV}}$.

Suppose that $\alpha$ and $\beta$ are probability distributions on a finite subset $\Lambda$ of $\mathbb{R}$. Let

$$ m_\alpha := \sum_{x \in \Lambda} x\alpha(x), \quad m_\beta := \sum_{x \in \Lambda} x\beta(x) $$

be the mean of $\alpha$ and $\beta$, respectively, and assume that $m_\alpha > m_\beta$. Let $M = (m_\alpha - m_\beta)/2$. By translating, we can assume that $m_\alpha = M$ and $m_\beta = -M$. Let $\eta = (\alpha + \beta)/2$, and define

$$ r(x) := \frac{\alpha(x)}{\eta(x)}, \quad s(x) := \frac{\beta(x)}{\eta(x)}. $$

By Cauchy-Schwarz,

$$ 4M^2 = \left[\sum_{x \in \Lambda} x[r(x) - s(x)]\eta(x)\right]^2 \leq \left(\sum_{x \in \Lambda} x^2\eta(x)\right)\left(\sum_{x \in \Lambda}[r(x) - s(x)]^2\eta(x)\right). \tag{7.14} $$

If $\alpha = \mu f^{-1}, \beta = \nu f^{-1}$, and $\Lambda = f(\mathcal{X})$, then $m_{\mu f^{-1}} = E_\mu(f)$, and (7.12) implies that $4M^2 \geq r^2\sigma^2$. Note that

$$ \sum_{x \in \Lambda} x^2\eta(x) = \frac{m_\alpha^2 + \mathrm{Var}(\alpha) + m_\beta^2 + \mathrm{Var}(\beta)}{2} = M^2 + \sigma^2. \tag{7.15} $$

Since

$$ |r(x) - s(x)| = 2\frac{|\alpha(x) - \beta(x)|}{\alpha(x) + \beta(x)} \leq 2, $$

we have

$$ \sum_{x \in \Lambda}[r(x) - s(x)]^2\eta(x) \leq 2 \sum_{x \in \Lambda} |r(x) - s(x)|\eta(x) $$

$$ = 2 \sum_{x \in \Lambda} |\alpha(x) - \beta(x)| = 4\|\alpha - \beta\|_{\mathrm{TV}}\,. \tag{7.16} $$

Putting together (7.14), (7.15), and (7.16) shows that

$$ M^2 \leq (M^2 + \sigma^2)\,\|\alpha - \beta\|_{\mathrm{TV}}\,, $$

### PDF page 111 (book page 95)

and rearranging shows that

$$ \|\alpha - \beta\|_{\mathrm{TV}} \geq 1 - \frac{\sigma^2}{\sigma^2 + M^2}. $$

If $4M^2 \geq r^2\sigma^2$, then

$$ \|\alpha - \beta\|_{\mathrm{TV}} \geq 1 - \frac{4}{4 + r^2}. \tag{7.17} $$

Recalling the definitions of $\alpha$ and $\beta$, the above yields

$$ \left\|\mu f^{-1} - \nu f^{-1}\right\|_{\mathrm{TV}} \geq 1 - \frac{4}{4 + r^2}. $$

This together with Lemma 7.10 establishes (7.13). $\blacksquare$

**7.3.1. Random walk on hypercube.** We use Proposition 7.9 to bound below the mixing time for the random walk on the hypercube, studied in Section 6.5.2.

First we record a simple lemma concerning the coupon collector problem introduced in Section 2.2.

LEMMA 7.13. *Consider the coupon collecting problem with $n$ distinct coupon types, and let $I_j(t)$ be the indicator of the event that the $j$-th coupon has* not *been collected by time $t$. Let $R_t = \sum_{j=1}^n I_j(t)$ be the number of coupon types not collected by time $t$. The random variables $I_j(t)$ are negatively correlated, and letting $p = \left(1 - \frac{1}{n}\right)^t$, we have for $t \geq 0$*

$$ \mathbf{E}(R_t) = np, \tag{7.18} $$

$$ \mathrm{Var}(R_t) \leq np(1 - p) \leq \frac{n}{4}. \tag{7.19} $$

PROOF. Since $I_j(t) = 1$ if and only if the first $t$ coupons are not of type $j$, it follows that

$$ \mathbf{E}\left(I_j(t)\right) = \left(1 - \frac{1}{n}\right)^t = p \quad \text{and} \quad \mathrm{Var}(I_j(t)) = p(1 - p). $$

Similarly, for $j \neq k$,

$$ \mathbf{E}\left(I_j(t)I_k(t)\right) = \left(1 - \frac{2}{n}\right)^t, $$

whence

$$ \mathrm{Cov}(I_j(t), I_k(t)) = \left(1 - \frac{2}{n}\right)^t - \left(1 - \frac{1}{n}\right)^{2t} \leq 0. $$

From this (7.18) and (7.19) follow. $\blacksquare$

PROPOSITION 7.14. *For the lazy random walk on the $n$-dimensional hypercube,*

$$ d\left(\frac{1}{2}n \log n - \alpha n\right) \geq 1 - 8e^{2-2\alpha}. \tag{7.20} $$

PROOF. Let $\mathbf{1}$ denote the vector of ones $(1, 1, \ldots, 1)$, and let $W(\boldsymbol{x}) = \sum_{i=1}^n x^i$ be the Hamming weight of $\boldsymbol{x} = (x^1, \ldots, x^n) \in \{0, 1\}^n$. We will apply Proposition 7.9 with $f = W$. The position of the walker at time $t$, started at $\mathbf{1}$, is denoted by $\boldsymbol{X}_t = (X_t^1, \ldots, X_t^n)$.

As $\pi$ is uniform on $\{0, 1\}^n$, the distribution of the random variable $W$ under $\pi$ is binomial with parameters $n$ and $p = 1/2$. In particular,

$$ E_\pi(W) = \frac{n}{2}, \quad \mathrm{Var}_\pi(W) = \frac{n}{4}. $$

### PDF page 112 (book page 96)

Let $R_t$ be the number of coordinates not updated by time $t$. When starting from $\mathbf{1}$, the conditional distribution of $W(\boldsymbol{X}_t)$ given $R_t = r$ is the same as that of $r + B$, where $B$ is a binomial random variable with parameters $n - r$ and $1/2$. Consequently,

$$ \mathbf{E_1}(W(\boldsymbol{X}_t) \mid R_t) = R_t + \frac{(n - R_t)}{2} = \frac{1}{2}(R_t + n). $$

By (7.18),

$$ \mathbf{E_1}(W(\boldsymbol{X}_t)) = \frac{n}{2}\left[1 + \left(1 - \frac{1}{n}\right)^t\right]. $$

Using the identity $\mathrm{Var_1}(W(\boldsymbol{X}_t)) = \mathrm{Var_1}(\mathbf{E}(W(\boldsymbol{X}_t) \mid R_t)) + \mathbf{E_1}(\mathrm{Var_1}(W(\boldsymbol{X}_t) \mid R_t))$,

$$ \mathrm{Var_1}(W(\boldsymbol{X}_t)) = \frac{1}{4}\,\mathrm{Var_1}(R_t) + \frac{1}{4}[n - \mathbf{E_1}(R_t)]. $$

By Lemma 7.13, $R_t$ is the sum of negatively correlated indicators and consequently $\mathrm{Var_1}(R_t) \le \mathbf{E_1}(R_t)$. We conclude that

$$ \mathrm{Var_1}(W(\boldsymbol{X}_t)) \le \frac{n}{4}. $$

Setting

$$ \sigma = \sqrt{\max\{\mathrm{Var}_\pi(W), \mathrm{Var_1}(W(\boldsymbol{X}_t))\}} = \frac{\sqrt{n}}{2}, $$

we have

$$ |E_\pi(W) - \mathbf{E_1}(W(\boldsymbol{X}_t))| = \frac{n}{2}\left(1 - \frac{1}{n}\right)^t = \sigma\sqrt{n}\left(1 - \frac{1}{n}\right)^t. $$

Setting

$$ t_n := \frac{1}{2}(n - 1)\log n - (\alpha - 1)n > \frac{1}{2}n\log n - \alpha n $$

and using that $(1 - 1/n)^{n-1} > e^{-1} > (1 - 1/n)^n$, gives

$$ |E_\pi(W) - \mathbf{E_1}(W(\boldsymbol{X}_{t_n}))| > e^{\alpha - 1}\sigma\,, $$

and applying Proposition 7.9 yields

$$ d\left(\frac{1}{2}n\log n - \alpha n\right) \ge \left\|P^{t_n}(\mathbf{1}, \cdot) - \pi\right\|_{\mathrm{TV}} \ge 1 - 8e^{2 - 2\alpha}\,. \tag{7.21} $$

$\blacksquare$

### 7.4. Examples

**7.4.1. Top-to-random shuffle.** The top-to-random shuffle was introduced in Section 6.1 and upper bounds on $d(t)$ and $t_{\mathrm{mix}}$ were obtained in Section 6.5.3. Here we obtain matching lower bounds.

The bound below, from **Aldous and Diaconis (1986)**, uses only the definition of total variation distance.

PROPOSITION 7.15. *Let $(X_t)$ be the top-to-random chain on $n$ cards. For any $\varepsilon > 0$, there exists a constant $\alpha(\varepsilon)$ such that $\alpha > \alpha(\varepsilon)$ implies that for all sufficiently large $n$,*

$$ d_n(n\log n - \alpha n) \ge 1 - \varepsilon. \tag{7.22} $$

*That is,*

$$ t_{\mathrm{mix}}(1 - \varepsilon) \ge n\log n - \alpha n. \tag{7.23} $$

### PDF page 113 (book page 97)

PROOF. Let id be the identity permutation; we will bound $\|P^t(\mathrm{id}, \cdot) - \pi\|_{\mathrm{TV}}$ from below. The bound is based on the events

$$ A_j = \{\text{the original bottom } j \text{ cards are in their original relative order}\}. \tag{7.24} $$

Let $\tau_j$ be the time required for the card initially $j$-th from the bottom to reach the top. Then

$$ \tau_j = \sum_{i=j}^{n-1} \tau_{j,i}, $$

where $\tau_{j,i}$ is the time it takes the card initially $j$-th from the bottom to ascend from position $i$ (from the bottom) to position $i + 1$. The variables $\{\tau_{j,i}\}_{i=j}^{n-1}$ are independent and $\tau_{j,i}$ has a geometric distribution with parameter $p = i/n$, whence $\mathbf{E}(\tau_{j,i}) = n/i$ and $\mathrm{Var}(\tau_{j,i}) < n^2/i^2$. We obtain the bounds

$$ \mathbf{E}(\tau_j) = \sum_{i=j}^{n-1} \frac{n}{i} \ge n\int_j^n \frac{dx}{x} = n(\log n - \log j) \tag{7.25} $$

and

$$ \mathrm{Var}(\tau_j) \le n^2 \sum_{i=j}^{\infty} \frac{1}{i(i-1)} \le \frac{n^2}{j-1}. \tag{7.26} $$

Using the bounds (7.25) and (7.26), together with Chebyshev's inequality, yields

$$ \mathbf{P}\{\tau_j < n\log n - \alpha n\} \le \mathbf{P}\{\tau_j - \mathbf{E}(\tau_j) < -n(\alpha - \log j)\} $$
$$ \le \frac{1}{j-1}, $$

provided that $\alpha \ge \log j + 1$. Define $t_n(\alpha) = n\log n - \alpha n$. If $\tau_j \ge t_n(\alpha)$, then the original $j$ bottom cards remain in their original relative order at time $t_n(\alpha)$, so

$$ P^{t_n(\alpha)}(\mathrm{id}, A_j) \ge \mathbf{P}\{\tau_j \ge t_n(\alpha)\} \ge 1 - \frac{1}{j-1}, $$

for $\alpha \ge \log j + 1$. On the other hand, for the uniform stationary distribution

$$ \pi(A_j) = 1/(j!) \le (j-1)^{-1}, $$

whence, for $\alpha \ge \log j + 1$,

$$ d_n(t_n(\alpha)) \ge \left\|P^{t_n(\alpha)}(\mathrm{id}, \cdot) - \pi\right\|_{\mathrm{TV}} \ge P^{t_n(\alpha)}(\mathrm{id}, A_j) - \pi(A_j) > 1 - \frac{2}{j-1}. \tag{7.27} $$

Taking $j = \lceil e^{\alpha - 1}\rceil$, provided $n \ge e^{\alpha - 1}$, we have

$$ d_n(t_n(\alpha)) > g(\alpha) := 1 - \frac{2}{\lceil e^{\alpha - 1}\rceil - 1}. $$

Therefore,

$$ \liminf_{n \to \infty} d_n(t_n(\alpha)) \ge g(\alpha), $$

where $g(\alpha) \to 1$ as $\alpha \to \infty$. $\blacksquare$

### PDF page 114 (book page 98)

**7.4.2. East model.** Let

$$ \mathcal{X} := \{x \in \{0,1\}^{n+1} \,:\, x(n+1) = 1\}. $$

The **East model** is the Markov chain on $\mathcal{X}$ which moves from $x$ by selecting a coordinate $k$ from $\{1, 2, \ldots, n\}$ at random and flipping the value $x(k)$ at $k$ if and only if $x(k + 1) = 1$. The reader should check that the uniform measure on $\mathcal{X}$ is stationary for these dynamics.

THEOREM 7.16. *For the East model, $t_{\mathrm{mix}} \ge n^2 - 2n^{3/2}$.*

PROOF. If $A = \{x \,:\, x(1) = 1\}$, then $\pi(A) = 1/2$.

On the other hand, we now show that it takes order $n^2$ steps until $X_t(1) = 1$ with probability near $1/2$ when starting from $x_0 = (0, 0, \ldots, 0, 1)$. Consider the motion of the left-most 1: it moves to the left by one if and only if the site immediately to its left is chosen. Thus, the waiting time for the left-most 1 to move from $k + 1$ to $k$ bounded below by a geometric random variable $G_k$ with mean $n$. The sum $G = \sum_{k=1}^{n} G_k$ has mean $n^2$ and variance $(1 - n^{-1})n^3$. Therefore, if $t(n, \alpha) = n^2 - \alpha n^{3/2}$, then

$$ \mathbf{P}\{X_{t(n,\alpha)}(1) = 1\} \le \mathbf{P}\{G - n^2 \le -\alpha n^{3/2}\} \le \frac{1}{\alpha^2}\,, $$

and therefor [sic]

$$ |P^{t(n,\alpha)}(x_0, A) - \pi(A)| \ge \frac{1}{2} - \frac{1}{\alpha^2}. $$

Thus, if $t \le n^2 - 2n^{3/2}$, then $d(t) \ge 1/4$. In other words, $t_{\mathrm{mix}} \ge n^2 - 2n^{3/2}$. $\blacksquare$

### Exercises

EXERCISE 7.1. Let $\boldsymbol{X}_t = (X_t^1, \ldots, X_t^n)$ be the position of the lazy random walker on the hypercube $\{0,1\}^n$, started at $\boldsymbol{X}_0 = \mathbf{1} = (1, \ldots, 1)$. Show that the covariance between $X_t^i$ and $X_t^j$ is negative. Conclude that if $W(\boldsymbol{X}_t) = \sum_{i=1}^{n} X_t^i$, then $\mathrm{Var}(W(\boldsymbol{X}_t)) \le n/4$.

*Hint*: It may be easier to consider the variables $Y_t^i = 2X_t^i - 1$.

EXERCISE 7.2. Show that $Q(S, S^c) = Q(S^c, S)$ for any $S \subset \mathcal{X}$. (This is easy in the reversible case, but holds generally.)

EXERCISE 7.3. An **empty graph** has no edges. Show that there is a constant $c(q)$ so that Glauber dynamics on the set of proper colorings of the empty graph satisfies

$$ t_{\mathrm{mix}} \ge \frac{1}{2}n\log n - c(q)n. $$

*Hint*: Copy the idea of the proof of Proposition 7.14.

EXERCISE 7.4. Let $\mathcal{X} = GL_n(\mathbb{F}_2)$, the set invertible $n \times n$ matrices over $\mathbb{F}_2$. Consider the chain which selects uniformly an ordered pair $(i, j)$ of rows $(i \ne j)$ and adds rows $i$ to row $j$ mod 2.

(a) Show that there is a constant $\gamma > 0$ so that $|\mathcal{X}|/2^{n^2} \to \gamma$ as $n \to \infty$.
(b) Show that $t_{\mathrm{mix}} > cn^2/\log n$ for a positive constant $c$.

### PDF page 115 (book page 99)

**Notes**

The bottleneck ratio $\Phi_\star$ has many names in the literature, including *conductance*, *Cheeger constant*, and *isoperimetric constant*. It is more common to relate $\Phi_\star$ to the *spectral gap* of a Markov chain. The approach to the lower bound for $t_{\mathrm{mix}}$ presented here is more direct and avoids reversibility. Results related to Theorem 7.4 can be found in **Mihail (1989)**, **Fill (1991)**, and **Chen, Lovász, and Pak (1999)**.

**Hayes and Sinclair (2007)** have shown that for Glauber dynamics for $q$-colorings on an $n$-vertex graph of maximal degree $\Delta$, the mixing time is bounded below by $c_{\Delta,q} n \log n$. Their results applies [sic] to a wider class of chains. However, for colorings, it remains open if $c_{\Delta,q}$ can be replaced by a universal constant $c$.

Using bounds of **Varopoulos (1985)** and **Carne (1985)**, one can prove that for simple random walk on an $n$-vertex simple graph, for $n \geq 64$,

$$ t_{\mathrm{mix}} \geq \frac{\mathrm{diam}^2}{20 \log n} \,. $$

See Proposition 13.7 in **Lyons and Peres (2016)**.

Upper bounds on the relaxation time (see Section 12.2) for the East model are obtained in **Aldous and Diaconis (2002)**, which imply that $t_{\mathrm{mix}} = O(n^2)$. See also **Cancrini, Martinelli, Roberto, and Toninelli (2008)** for results concerning a class of models including the East model. For combinatorics related to the East model, see **Chung, Diaconis, and Graham (2001)**.

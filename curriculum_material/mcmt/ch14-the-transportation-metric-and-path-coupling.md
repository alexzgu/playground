# Chapter 14 — The Transportation Metric and Path Coupling
*(PDF pages 217–230; book pages 201–214)*

### PDF page 217 (book page 201)

CHAPTER 14

# The Transportation Metric and Path Coupling

Let $P$ be a transition matrix on a metric space $(\mathcal{X}, \rho)$, where the metric $\rho$ satisfies $\rho(x, y) \geq \mathbf{1}\{x \neq y\}$. Suppose, for all states $x$ and $y$, there exists a coupling $(X_1, Y_1)$ of $P(x, \cdot)$ with $P(y, \cdot)$ that contracts $\rho$ on average, i.e., which satisfies

$$ \mathbf{E}_{x,y}\rho(X_1, Y_1) \leq e^{-\alpha}\rho(x, y), \quad \text{for all } x, y \in \mathcal{X}, \tag{14.1} $$

for some $\alpha > 0$. The **diameter** of $\mathcal{X}$ is defined to be $\operatorname{diam}(\mathcal{X}) := \max_{x,y \in \mathcal{X}} \rho(x, y)$. By iterating (14.1), we have

$$ \mathbf{E}_{x,y}\rho(X_t, Y_t) \leq e^{-\alpha t}\operatorname{diam}(\mathcal{X}). $$

We conclude that

$$ \left\|P^t(x, \cdot) - P^t(y, \cdot)\right\|_{\mathrm{TV}} \leq \mathbf{P}_{x,y}\{X_t \neq Y_t\} = \mathbf{P}_{x,y}\{\rho(X_t, Y_t) \geq 1\} \\ \leq \mathbf{E}_{x,y}\rho(X_t, Y_t) \leq \operatorname{diam}(\mathcal{X})e^{-\alpha t}, $$

whence

$$ t_{\mathrm{mix}}(\varepsilon) \leq \left\lceil \frac{1}{\alpha}\left[\log(\operatorname{diam}(\mathcal{X})) + \log(1/\varepsilon)\right] \right\rceil. $$

This is the method used in Theorem 5.8 to bound the mixing time of the Metropolis chain for proper colorings and also used in Theorem 5.9 for the hardcore chain.

**Path coupling** is a technique that simplifies the construction of couplings satisfying (14.1), when $\rho$ is a *path metric*, defined below. While the argument just given requires verification of (14.1) *for all* pairs $x, y \in \mathcal{X}$, the path-coupling technique shows that it is enough to construct couplings satisfying (14.1) only for neighboring pairs.

**14.1. The Transportation Metric**

Recall that a coupling of probability distributions $\mu$ and $\nu$ is a pair $(X, Y)$ of random variables defined on a single probability space such that $X$ has distribution $\mu$ and $Y$ has distribution $\nu$.

For a given distance $\rho$ defined on the state space $\mathcal{X}$, the **transportation metric** between two distributions on $\mathcal{X}$ is defined by

$$ \rho_K(\mu, \nu) := \inf\{\mathbf{E}(\rho(X, Y)) : (X, Y) \text{ is a coupling of } \mu \text{ and } \nu\}. \tag{14.2} $$

By Proposition 4.7, if $\rho(x, y) = \mathbf{1}_{\{x \neq y\}}$, then $\rho_K(\mu, \nu) = \|\mu - \nu\|_{\mathrm{TV}}$.

REMARK 14.1. It is sometimes convenient to describe couplings using probability distributions on the product space $\mathcal{X} \times \mathcal{X}$, instead of random variables. When $q$ is a probability distribution on $\mathcal{X} \times \mathcal{X}$, its **projection onto the first coordinate** is the probability distribution on $\mathcal{X}$ equal to

$$ q(\cdot \times \mathcal{X}) = \sum_{y \in \mathcal{X}} q(\cdot, y). $$

201

### PDF page 218 (book page 202)

Likewise, its **projection onto the second coordinate** is the distribution $q(\mathcal{X} \times \cdot)$.

Given a coupling $(X, Y)$ of $\mu$ and $\nu$ as defined above, the distribution of $(X, Y)$ on $\mathcal{X} \times \mathcal{X}$ has projections $\mu$ and $\nu$ on the first and second coordinates, respectively. Conversely, given a probability distribution $q$ on $\mathcal{X} \times \mathcal{X}$ with projections $\mu$ and $\nu$, the identity function on the probability space $(\mathcal{X} \times \mathcal{X}, q)$ is a coupling of $\mu$ and $\nu$.

Consequently, since $\mathbf{E}(\rho(X, Y)) = \sum_{(x,y) \in \mathcal{X} \times \mathcal{X}} \rho(x, y)q(x, y)$ when $(X, Y)$ has distribution $q$, the transportation metric can also be written as

$$ \rho_K(\mu, \nu) = \inf\left\{ \sum_{(x,y) \in \mathcal{X} \times \mathcal{X}} \rho(x, y)q(x, y) : q(\cdot \times \mathcal{X}) = \mu, \ q(\mathcal{X} \times \cdot) = \nu \right\}. \tag{14.3} $$

REMARK 14.2. The set of probability distributions on $\mathcal{X} \times \mathcal{X}$ can be identified with the $(|\mathcal{X}|^2\text{-}1)$-dimensional simplex, which is a compact subset of $\mathbb{R}^{|\mathcal{X}|^2}$. The set of distributions on $\mathcal{X} \times \mathcal{X}$ which project on the first coordinate to $\mu$ and project on the second coordinate to $\nu$ is a closed subset of this simplex and hence is compact. The function

$$ q \mapsto \sum_{(x,y) \in \mathcal{X} \times \mathcal{X}} \rho(x, y)q(x, y) $$

is continuous on this set. Hence there is a $q_\star$ such that

$$ \sum_{(x,y) \in \mathcal{X} \times \mathcal{X}} \rho(x, y)q_\star(x, y) = \rho_K(\mu, \nu). $$

Such a $q_\star$ is called an $\rho$-**optimal coupling** of $\mu$ and $\nu$. Equivalently, there is a pair of random variables $(X_\star, Y_\star)$, also called a $\rho$-optimal coupling, such that

$$ \mathbf{E}(\rho(X_\star, Y_\star)) = \rho_K(\mu, \nu). $$

LEMMA 14.3. *The function $\rho_K$ defined in* (14.2) *is a metric on the space of probability distributions on $\mathcal{X}$.*

PROOF. We check the triangle inequality and leave the verification of the other two conditions to the reader.

Let $\mu, \nu$ and $\eta$ be probability distributions on $\mathcal{X}$. Let $p$ be a probability distribution on $\mathcal{X} \times \mathcal{X}$ which is a coupling of $\mu$ and $\nu$, and let $q$ be a probability distribution on $\mathcal{X} \times \mathcal{X}$ which is a coupling of $\nu$ and $\eta$. Define the probability distribution $r$ on $\mathcal{X} \times \mathcal{X} \times \mathcal{X}$ by

$$ r(x, y, z) := \frac{p(x, y)q(y, z)}{\nu(y)}. \tag{14.4} $$

(See Remark 14.4 for the motivation of this definition.) Note that the projection of $r$ onto its first two coordinates is $p$, and the projection of $r$ onto its last two coordinates is $q$. The projection of $r$ onto the first and last coordinates is a coupling of $\mu$ and $\eta$.

Assume now that $p$ is a $\rho$-optimal coupling of $\mu$ and $\nu$. (See Remark 14.2.) Likewise, suppose that $q$ is a $\rho$-optimal coupling of $\nu$ and $\eta$.

Let $(X, Y, Z)$ be a random vector with probability distribution $r$. Since $\rho$ is a metric,

$$ \rho(X, Z) \leq \rho(X, Y) + \rho(Y, Z). $$

Taking expectation, because $(X, Y)$ is an optimal coupling of $\mu$ and $\nu$ and $(Y, Z)$ is an optimal coupling of $\nu$ and $\eta$,

$$ \mathbf{E}(\rho(X, Z)) \leq \mathbf{E}(\rho(X, Y)) + \mathbf{E}(\rho(Y, Z)) = \rho_K(\mu, \nu) + \rho_K(\nu, \eta). $$

### PDF page 219 (book page 203)

Since $(X, Z)$ is a coupling of $\mu$ and $\eta$, we conclude that

$$ \rho_K(\mu, \eta) \leq \rho_K(\mu, \nu) + \rho_K(\nu, \eta). $$

$\blacksquare$

The transportation metric $\rho_K$ extends the metric $\rho$ on $\mathcal{X}$ to a metric on the space of probability distributions on $\mathcal{X}$. In particular, if $\delta_x$ denotes the probability distribution which puts unit mass on $x$, then $\rho_K(\delta_x, \delta_y) = \rho(x, y)$.

REMARK 14.4. The probability distribution $r$ defined in (14.4) can be thought of as three steps of a time-inhomogeneous Markov chain. The first state $X$ is generated according to $\mu$. Given $X = x$, the second state $Y$ is generated according to $p(x, \cdot)/\mu(x)$, and given $Y = y$, the third state $Z$ is generated according to $q(y, \cdot)/\nu(y)$. Thus,

$$ \mathbf{P}\{X = x, Y = y, Z = z\} = \mu(x)\frac{p(x, y)}{\mu(x)}\frac{q(y, z)}{\nu(y)} = r(x, y, z). $$

**14.2. Path Coupling**

Suppose that the state space $\mathcal{X}$ of a Markov chain $(X_t)$ is the vertex set of a connected graph $G = (\mathcal{X}, E_0)$ and $\ell$ is a length function defined on $E_0$. That is, $\ell$ assigns length $\ell(x, y)$ to each edge $\{x, y\} \in E_0$. We assume that $\ell(x, y) \geq 1$ for all edges $\{x, y\}$.

REMARK 14.5. This graph structure may be different from the structure inherited from the permissible transitions of the Markov chain $(X_t)$.

If $x_0, x_1, \ldots, x_r$ is a path in $G$, we define its **length** to be $\sum_{i=1}^{r} \ell(x_{i-1}, x_i)$. The **path metric** on $\mathcal{X}$ is defined by

$$ \rho(x, y) = \min\{\text{length of } \xi : \xi \text{ a path from } x \text{ to } y\}. \tag{14.5} $$

Since we have assumed that $\ell(x, y) \geq 1$, it follows that $\rho(x, y) \geq \mathbf{1}\{x \neq y\}$, whence for any pair $(X, Y)$,

$$ \mathbf{P}\{X \neq Y\} = \mathbf{E}\left(\mathbf{1}_{\{X \neq Y\}}\right) \leq \mathbf{E}\rho(X, Y). \tag{14.6} $$

Minimizing over all couplings $(X, Y)$ of $\mu$ and $\nu$ shows that

$$ \|\mu - \nu\|_{\mathrm{TV}} \leq \rho_K(\mu, \nu). \tag{14.7} $$

While **Bubley and Dyer (1997)** discovered the following theorem and applied it to mixing, the key idea is the application of the triangle inequality for the transportation metric, which goes back to **Kantorovich (1942)**.

THEOREM 14.6 (**Bubley and Dyer (1997)**). *Suppose the state space $\mathcal{X}$ of a Markov chain is the vertex set of a graph with length function $\ell$ defined on edges. Let $\rho$ be the corresponding path metric defined in* (14.5). *Suppose that for each edge $\{x, y\}$ there exists a coupling $(X_1, Y_1)$ of the distributions $P(x, \cdot)$ and $P(y, \cdot)$ such that*

$$ \mathbf{E}_{x,y}\left(\rho(X_1, Y_1)\right) \leq \rho(x, y)e^{-\alpha} \tag{14.8} $$

*Then for any two probability measures $\mu$ and $\nu$ on $\mathcal{X}$,*

$$ \rho_K(\mu P, \nu P) \leq e^{-\alpha}\rho_K(\mu, \nu). \tag{14.9} $$

### PDF page 220 (book page 204)

REMARK 14.7. The definition of $t_{\mathrm{mix}}$ requires a unique stationary distribution, which is implied by (14.9). In particular, the assumption that $P$ is irreducible is not required, and $\pi$ may be supported on a proper subset of $\mathcal{X}$.

Recall that $d(t) = \max_{x \in \mathcal{X}} \|P^t(x, \cdot) - \pi\|_{\mathrm{TV}}$ and $\mathrm{diam}(\mathcal{X}) = \max_{x,y \in \mathcal{X}} \rho(x, y)$.

COROLLARY 14.8. *Suppose that the hypotheses of Theorem 14.6 hold. Then*

$$ d(t) \leq e^{-\alpha t} \mathrm{diam}(\mathcal{X}), $$

*and consequently*

$$ t_{\mathrm{mix}}(\varepsilon) \leq \left\lceil \frac{-\log(\varepsilon) + \log(\mathrm{diam}(\mathcal{X}))}{\alpha} \right\rceil . $$

PROOF. By iterating (14.9), it follows that

$$ \rho_K(\mu P^t, \nu P^t) \leq e^{-\alpha t} \rho_K(\mu, \nu) \leq e^{-\alpha t} \max_{x,y} \rho(x, y). \tag{14.10} $$

Applying (14.7) and setting $\mu = \delta_x$ and $\nu = \pi$ shows that

$$ \left\| P^t(x, \cdot) - \pi \right\|_{\mathrm{TV}} \leq e^{-\alpha t} \mathrm{diam}(\mathcal{X}). \tag{14.11} $$

$\blacksquare$

PROOF OF THEOREM 14.6. We begin by showing that for arbitrary (not necessarily neighboring) $x, y \in \mathcal{X}$,

$$ \rho_K(P(x, \cdot), P(y, \cdot)) \leq e^{-\alpha} \rho(x, y). \tag{14.12} $$

Fix $x, y \in \mathcal{X}$, and let $(x_0, x_1, \ldots, x_r)$ be a path achieving the minimum in (14.5). By the triangle inequality for $\rho_K$,

$$ \rho_K(P(x, \cdot), P(y, \cdot)) \leq \sum_{k=1}^r \rho_K(P(x_{k-1}, \cdot), P(x_k, \cdot)). \tag{14.13} $$

Since $\rho_K$ is a minimum over all couplings, the hypotheses of the theorem imply that, for any edge $\{a, b\}$,

$$ \rho_K(P(a, \cdot), P(b, \cdot)) \leq e^{-\alpha} \ell(a, b). \tag{14.14} $$

Using the bound (14.14) on each of the terms in the sum appearing on the right-hand side of (14.13) shows that

$$ \rho_K(P(x, \cdot), P(y, \cdot)) \leq e^{-\alpha} \sum_{k=1}^r \ell(x_{k-1}, x_k). $$

Since the path $(x_0, \ldots, x_k)$ was chosen to be of shortest length, the sum on the right-hand side above equals $\rho(x, y)$. This establishes (14.12).

Let $\eta$ be a $\rho$-optimal coupling of $\mu$ and $\nu$, so that

$$ \rho_K(\mu, \nu) = \sum_{x,y \in \mathcal{X}} \rho(x, y) \eta(x, y). \tag{14.15} $$

By (14.12), we know that for all $x, y$ there exists a coupling $\theta_{x,y}$ of $P(x, \cdot)$ and $P(y, \cdot)$ such that

$$ \sum_{u,w \in \mathcal{X}} \rho(u, w) \theta_{x,y}(u, w) \leq e^{-\alpha} \rho(x, y). \tag{14.16} $$

### PDF page 221 (book page 205)

$$
\begin{array}{ccccccccc}
\sigma & + & + & - & + & - & + & - & - \\
\tau & + & + & - & - & - & + & + & - \\
 & & & & i & & & j &
\end{array}
$$

FIGURE 14.1. Two configurations differing at exactly two cards. . *[Figure: two rows labeled $\sigma$ and $\tau$, each a sequence of nine $+/-$ signs; the columns marked $i$ and $j$ are the two positions where the rows differ.]*

Consider the probability distribution $\theta := \sum_{x,y \in \mathcal{X}} \eta(x, y) \theta_{x,y}$ on $\mathcal{X} \times \mathcal{X}$. (This is a coupling of $\mu P$ with $\nu P$.) We have by (14.16) and (14.15) that

$$
\begin{aligned}
\sum_{u,w \in \mathcal{X}} \rho(u, w) \theta(u, w) &= \sum_{x,y \in \mathcal{X}} \sum_{u,w \in \mathcal{X}} \rho(u, w) \theta_{x,y}(u, w) \eta(x, y) \\
&\leq e^{-\alpha} \sum_{x,y \in \mathcal{X}} \rho(x, y) \eta(x, y) \\
&= e^{-\alpha} \rho_K(\mu, \nu).
\end{aligned}
$$

Therefore, the theorem is proved, because $\rho_K(\mu P, \nu P) \leq \sum_{u,w \in \mathcal{X}} \rho(u, w) \theta(u, w)$.
$\blacksquare$

EXAMPLE 14.9 (Exclusion Process on Complete Graph). The state space of this chain is the set of all configurations of $n$ cards, where $k$ cards are $+$ and the other $n - k$ are $-$; cards of the same signs are indistinguishable. Assume $n > 2$ and $k \leq n/2$. The chain moves by interchanging two cards chosen at random.

We construct a path coupling. The distance $\rho$ between two configurations is half the number of cards with differing signs. (Note that the minimal distance between non-identical configurations is 1, since configurations must have at least two different cards.)

Consider two decks $\sigma$ and $\tau$ that differ only at two positions $i < j$. Note that $\{\sigma(i), \sigma(j)\} = \{\tau(i), \tau(j)\} = \{+, -\}$. We will construct a coupling of a random configuration $\sigma_1$ distributed according to $P(\sigma, \cdot)$ with a random configuration $\tau_1$ distributed according to $P(\tau, \cdot)$. In Figure 14.1, a $(\sigma, \tau)$ pair is shown with $i = 4$ and $j = 7$. We pick two positions $L$ and $R$ uniformly at random and interchange the cards in $\sigma$ occupying position $L$ and position $R$. We will pick two positions $L'$ and $R'$ for $\tau$ and interchange those cards in $\tau$. We choose $L'$ and $R'$ as follows:

(1) Both $L, R \notin \{i, j\}$. We pick $L' = L$ and $R' = R$. Then $\sigma_1 = \sigma$ and $\tau_1 = \tau$. Hence $\rho(\sigma_1, \tau_1) = \rho(\sigma, \tau) = 1$.
(2) $L \in \{i, j\}$ and $R \notin \{i, j\}$. Then we pick $R' = R$ and let $L'$ be the card in $\{i, j\}$ which is different from $L$.
&nbsp;&nbsp;(a) Suppose $\sigma(L) = \sigma(R)$.

$$
\begin{array}{ccccccccc}
 & & & R & & L & & & \\
\sigma & + & + & - & + & - & + & - & - \\
\tau & + & + & - & - & - & + & + & - \\
 & & & R' & & & & L' &
\end{array}
$$

&nbsp;&nbsp;Then $\sigma_1 = \sigma$ and

$$ \tau(R') = \sigma(R) = \sigma(L) = \tau(L') . $$

&nbsp;&nbsp;Hence $\tau_1 = \tau$, so $\rho(\sigma_1, \tau_1) = \rho(\sigma, \tau) = 1$.

### PDF page 222 (book page 206)

&nbsp;&nbsp;(b) Suppose $\sigma(L) \neq \sigma(R)$.

$$
\begin{array}{ccccccccc}
 & & & R & L & & & & \\
\sigma & + & + & - & + & - & + & - & - \\
\tau & + & + & - & - & - & + & + & - \\
 & & & R' & & & & L' &
\end{array}
$$

&nbsp;&nbsp;Then $\sigma_1 = \tau_1$, so $\rho(\sigma_1, \tau_1) = 0$.

(3) $L \notin \{i, j\}$ and $R \in \{i, j\}$. This case is similar to Case 2. Now we pick $L' = L$ and let $R'$ be the card in $\{i, j\}$ that is different from $R$. In the same way:
&nbsp;&nbsp;(a) Suppose $\sigma(R) = \sigma(L)$. Then $\rho(\sigma_1, \tau_1) = \rho(\sigma, \tau) = 1$.
&nbsp;&nbsp;(b) Suppose $\sigma(R) \neq \sigma(L)$. Then $\rho(\sigma_1, \tau_1) = 0$.
(4) $L, R \in \{i, j\}$. We pick $L' = R$ and $R' = L$. Then $\rho(\sigma_1, \tau_1) = \rho(\sigma, \tau) = 1$.

$$
\begin{array}{ccccccccc}
 & & & & L & & & R & \\
\sigma & + & + & - & + & - & + & - & - \\
\tau & + & + & - & - & - & + & + & - \\
 & & & & R' & & & L' &
\end{array}
$$

Since we always match position $i$ in $\sigma$ with position $j$ in $\tau$, and position $j$ in $\sigma$ with position $i$ in $\tau$, we have constructed a coupling of $P(\sigma, \cdot)$ and $P(\tau, \cdot)$.

Now the distance decreases to 0 only when one of $L$ and $R$ is chosen in $\{i, j\}$, and $\sigma(L) \neq \sigma(R)$. This happens with probability

$$ 2 \cdot \left( \frac{1}{n} \frac{n - k - 1}{n - 1} + \frac{1}{n} \frac{k - 1}{n - 1} \right) = \frac{2}{n} \frac{n - 2}{n - 1} $$

In the remaining cases $\rho(\sigma_1, \tau_1)$ stays at 1. Hence

$$ \mathbb{E}_{\sigma,\tau} \rho(\sigma_1, \tau_1) = 1 - \frac{2}{n} \frac{n - 2}{n - 1} \leq e^{-\frac{2}{n} \frac{n-2}{n-1}} \rho(\sigma, \tau). $$

Applying Corollary 14.8 yields

$$ t_{\mathrm{mix}}(\varepsilon) \leq \frac{n}{2}[1 + o(1)] \left(\log(k) + \log(1/\varepsilon)\right) . $$

For a lower bound, see Exercise 14.10. The upper bound can be improved to $\frac{1}{4} n \log n[1 + o(1)]$; see Exercise 18.2.

**14.3. Rapid Mixing for Colorings**

Recall from Section 3.1 that proper $q$-colorings of a graph $G = (V, E)$ are elements $x$ of $\mathcal{X} = \{1, 2, \ldots, q\}^V$ such that $x(v) \neq x(w)$ for $\{v, w\} \in E$.

In Section 5.4.1, the mixing time of the Metropolis chain for proper $q$-colorings was analyzed for sufficiently large $q$. Here we analyze the mixing time for the Glauber dynamics.

We extend the definition of Glauber dynamics for proper $q$-colorings of a graph $G$ with $n$ vertices (as given in Section 3.3) to *all* colorings $\mathcal{X}$ as follows: at each move, a vertex $w$ is chosen uniformly at random and $w$ is assigned a color chosen uniformly from the colors not present among the neighbors of $w$. (See Figure 14.2.) If the chain starts at a proper coloring, it will remain in the set of proper colorings. Let $\pi$ be uniform probability distribution on *proper $q$-colorings*. The dynamics are reversible with respect to $\pi$.

### PDF page 223 (book page 207)

*[Figure: a 3×3 grid of vertices on a graph. Top row vertices colored 1, 5, 6; middle row 5, (center vertex $w$, uncolored), 3; bottom row 2, 1, 5. Dashed arrows extend outward from the boundary vertices. The center vertex is labeled $w$.]*

Colors: $\{\cancel{1},\, 2,\, \cancel{3},\, 4,\, \cancel{5},\, 6\}$

FIGURE 14.2. Updating at vertex $w$. The colors of the neighbors are not available, as indicated.

THEOREM 14.10. *Consider the Glauber dynamics chain for $q$-colorings of a graph with $n$ vertices and maximum degree $\Delta$. If $q > 2\Delta$, then the mixing time satisfies*

$$ t_{\mathrm{mix}}(\varepsilon) \leq \left\lceil \left( \frac{q - \Delta}{q - 2\Delta} \right) n \left( \log n - \log \varepsilon \right) \right\rceil. \tag{14.17} $$

PROOF. The metric here is $\rho(x,y) = \sum_{v \in V} \mathbf{1}\{x(v) \neq y(v)\}$, the number of sites at which $x$ and $y$ differ. Two colorings are neighbors if and only if they differ at a single vertex. Note that this neighboring rule defines a graph different from the graph defined by the transitions of the chain, since the chain moves only among proper colorings.

Recall that $A_v(x)$ is the set of allowable colors at $v$ in configuration $x$.

Let $x$ and $y$ be two configurations which agree everywhere except at vertex $v$. We describe how to simultaneously evolve two chains, one started at $x$ and the other started at $y$, such that each chain viewed alone is a Glauber chain.

First, we pick a vertex $w$ uniformly at random from the vertex set of the graph. (We use a lowercase letter for the random variable $w$ to emphasize that its value is a vertex.) We will update the color of $w$ in both the chain started from $x$ and the chain started from $y$.

If $v$ is not a neighbor of $w$, then we can update the two chains with the same color. Each chain is updated with the correct distribution because $A_w(x) = A_w(y)$.

Suppose now one of the neighbors of $w$ is $v$. Without loss of generality, we will assume that $|A_w(x)| \leq |A_w(y)|$.

Generate a random color $U$ from $A_w(y)$ and use this to update $y$ at $w$. If $U \neq x(v)$, then update the configuration $x$ at $w$ to $U$. We subdivide the case $U = x(v)$ into subcases based on whether or not $|A_w(x)| = |A_w(y)|$:

| case | how to update $x$ at $w$ |
|---|---|
| $|A_w(x)| = |A_w(y)|$ | set $x(w) = y(v)$ |
| $|A_w(x)| < |A_w(y)|$ | draw a random color from $A_w(x)$ |

(Figure 14.3 illustrates the second scenario above.) The reader should check that this updates $x$ at $w$ to a color chosen uniformly from $A_w(x)$. The probability

### PDF page 224 (book page 208)

Colors: $\{1, 2, 3, 4, 5, 6\}$

*[Figure: two side-by-side 3×3 grids of graph vertices. Left grid, labeled $x$ at top: top row 1, 5, 6; middle row 5, (center vertex "?" labeled $w$), 3 (labeled $v$); bottom row 2, 1, 5; annotated below "Available: {2,4,6}". Right grid, labeled $y$ at top: top row 1, 5, 6; middle row 5, (center vertex "?" labeled $w$), 1 (labeled $v$); bottom row 2, 1, 5; annotated below "Available: {2,4,6} and 3". Dashed arrows extend outward from boundary vertices in both grids.]*

FIGURE 14.3. Jointly updating $x$ and $y$ when they differ only at vertex $v$ and $|A_w(x)| < |A_w(y)|$

that the two configurations do not update to the same color is $1/|A_w(y)|$, which is bounded above by $1/(q - \Delta)$.

Given two states $x$ and $y$ which are at unit distance, we have constructed a coupling $(X_1, Y_1)$ of $P(x, \cdot)$ and $P(y, \cdot)$. The distance $\rho(X_1, Y_1)$ increases from 1 only in the case where a neighbor of $v$ is updated and the updates are different in the two configurations. Also, the distance decreases when $v$ is selected to be updated. In all other cases the distance stays at 1. Therefore,

$$ \mathbf{E}_{x,y} \left( \rho(X_1, Y_1) \right) \leq 1 - \frac{1}{n} + \frac{\deg(v)}{n} \left( \frac{1}{q - \Delta} \right). \tag{14.18} $$

The right-hand side of (14.18) is bounded by

$$ 1 - \frac{1}{n} \left( 1 - \frac{\Delta}{q - \Delta} \right). \tag{14.19} $$

Because $2\Delta < q$, this is smaller than 1. Letting $c(q, \Delta) := [1 - \Delta/(q - \Delta)]$,

$$ \mathbf{E}_{x,y} \left( \rho(X_1, Y_1) \right) \leq \exp \left( - \frac{c(q, \Delta)}{n} \right). $$

By Remark 14.7, $\pi$ is the unique stationary distribution. Applying Corollary 14.8 shows that

$$ \max_{x \in \mathcal{X}} \left\| P^t(x, \cdot) - \pi \right\|_{\mathrm{TV}} \leq n \exp \left( - \frac{c(q, \Delta)}{n} t \right) $$

and that

$$ t_{\mathrm{mix}}(\varepsilon) \leq \left\lceil \frac{n}{c(q, \Delta)} \left( \log n + \log \varepsilon^{-1} \right) \right\rceil. \tag{14.20} $$

(Note that $c(q, \Delta) > 0$ because $q > 2\Delta$.) This establishes (14.17). $\blacksquare$

### PDF page 225 (book page 209)

*[Figure: a horizontal path of 8 vertices labeled 1 through 8 left to right, connected by edges. Vertices 1, 3, 6, 8 are filled (black) circles; vertices 2, 4, 5, 7 are open (white) circles.]*

FIGURE 14.4. A configuration of the hardcore model on the 8-vertex path. Filled circles correspond to occupied sites.

Some condition on $q$ and $\Delta$ is necessary to achieve the fast rate of convergence (order $n \log n$) established in Theorem 14.10, although the condition $q > 2\Delta$ is not the best known. Example 7.6 shows that if $\Delta$ is allowed to grow with $n$ while $q$ remains fixed, then the mixing time can be exponential in $n$.

Exercise 7.3 shows that for the graph having no edges, in which case the colors at distinct vertices do not interact, the mixing time is at least of order $n \log n$.

**14.4. Approximate Counting**

**14.4.1. Sampling and counting.** For sufficiently simple combinatorial sets, it can be easy both to count and to generate a uniform random sample.

EXAMPLE 14.11 (One-dimensional colorings). Recall the definition of proper $q$-coloring from Section 3.1. On the path with $n$ vertices there are exactly $q(q-1)^{n-1}$ proper colorings: color vertex 1 arbitrarily, and then for each successive vertex $i > 1$, choose a color different from that of vertex $i - 1$. This description of the enumeration is easily modified to a uniform sampling algorithm, as Exercise 14.4 asks the reader to check.

EXAMPLE 14.12 (One-dimensional hardcore model). Now consider the set $\mathcal{X}_n$ of hardcore configurations on the path with $n$ vertices (recall the definition of the hardcore model in Section 3.3, and see Figure 14.4). Exercise 14.5 asks the reader to check that $|\mathcal{X}_n| = f_{n+1}$, where $f_n$ is the $n$-th Fibonacci number, and Exercise 14.6 asks the reader to check that the following recursive algorithm inductively generates a uniform sample from $\mathcal{X}_n$: suppose you are able to generate uniform samples from $\mathcal{X}_k$ for $k \leq n-1$. With probability $f_{n-1}/f_{n+1}$, put a 1 at location $n$, a 0 at location $n - 1$, and then generate a random element of $\mathcal{X}_{n-2}$ to fill out the configuration at $\{1, 2, \ldots, n - 2\}$. With the remaining probability $f_n/f_{n+1}$, put a 0 at location $n$ and fill out the positions $\{1, 2, \ldots, n - 1\}$ with a random element of $\mathcal{X}_{n-1}$.

REMARK 14.13. For more examples of sets enumerated by the Fibonacci numbers, see **Stanley (1986**, Chapter 1, Exercise 14) and Section 6.6 of **Graham, Knuth, and Patashnik (1994)**. **Benjamin and Quinn (2003)** use combinatorial interpretations to prove Fibonacci identities (and many other things).

For both models, both sampling and counting become more difficult on more complicated graphs. Fortunately, Markov chains (such as the Glauber dynamics for both these examples) can efficiently sample large combinatorial sets which (unlike the elementary methods described above and in greater generality in Appendix B) do not require enumerating the set or even knowing how many elements are in the set. In Section 14.4.2 we show how Markov chains can be used in an approximate counting algorithm for colorings.

### PDF page 226 (book page 210)

**14.4.2. Approximately counting colorings.** Many innovations in the study of mixing times for Markov chains came from researchers motivated by the problem of *counting* combinatorial structures. While determining the exact size of a complicated set may be a "hard" problem, an approximate answer is often possible using Markov chains.

In this section, we show how the number of proper colorings can be estimated using the Markov chain analyzed in the previous section. We adapt the method described in **Jerrum and Sinclair (1996**) to this setting.

THEOREM 14.14. *Let $\mathcal{X}$ be the set of all proper $q$-colorings of the graph $G$ of $n$ vertices and maximal degree $\Delta$. Fix $q > 2\Delta$, and set $c(q, \Delta) = 1 - \Delta/(q - \Delta)$. Given $\eta$ and $\varepsilon$, there is a random variable $W$ which can be simulated using no more than*

$$ n \left\lceil \frac{n \log n + n \log(6eqn/\varepsilon)}{c(q, \Delta)} \right\rceil \left\lceil \frac{27qn}{\eta \varepsilon^2} \right\rceil \tag{14.21} $$

*Glauber updates and which satisfies*

$$ \mathbf{P}\{(1 - \varepsilon)|\mathcal{X}|^{-1} \leq W \leq (1 + \varepsilon)|\mathcal{X}|^{-1}\} \geq 1 - \eta. \tag{14.22} $$

REMARK 14.15. This is an example of a ***fully polynomial randomized approximation scheme***, an algorithm for approximating values of the function $n \mapsto |\mathcal{X}_n|$ having a run-time that is polynomial in both the *instance size $n$* and the inverse error tolerated, $\varepsilon^{-1}$.

Let $x_0$ be a proper coloring of $G$. Enumerate the vertices of $G$ as $\{v_1, v_2, \ldots, v_n\}$. Define for $k = 0, 1, \ldots, n$

$$ \mathcal{X}_k = \{x \in \mathcal{X} \,:\, x(v_j) = x_0(v_j) \text{ for } j > k\}. $$

Elements of $\mathcal{X}_k$ have $k$ free vertices, while the $n - k$ vertices $\{v_{k+1}, \ldots, v_n\}$ are colored in agreement with $x_0$. In particular, $|\mathcal{X}_0| = 1$ and $|\mathcal{X}_n| = |\mathcal{X}|$.

To prove Theorem 14.14, we will run Glauber dynamics on $\mathcal{X}_k$ for each $k$ to estimate the ratio $|\mathcal{X}_{k-1}|/|\mathcal{X}_k|$, and then multiply these estimates. It will be useful to know that the ratios $|\mathcal{X}_{k-1}|/|\mathcal{X}_k|$ are not too small.

LEMMA 14.16. *Let $\mathcal{X}_k$ be as defined above. If $q > 2\Delta$, then $\frac{|\mathcal{X}_{k-1}|}{|\mathcal{X}_k|} \geq \frac{1}{qe}$.*

PROOF. Call the $r$ neighbors of $v_k$ which are also in the set $\{v_1, \ldots, v_{k-1}\}$ the *free* neighbors of $v_k$. Consider the process with initial distribution the uniform measure on $|\mathcal{X}_k|$, and which updates, in a pre-specified order, the free neighbors of $v_k$, followed by an update at $v_k$. Updates at a site are made by chosing uniformly among the allowable colors for that site; each update preserves the uniform distribution on $\mathcal{X}_k$. Write $Y$ for the final state of this $(r + 1)$-step process. Let $A$ be the event that each of the free neighbors of $v_k$ is updated to a value different from $x_0(v_k)$ and that $v_k$ is updated to $x_0(v_k)$. Since $Y \in \mathcal{X}_{k-1}$ if and only if $A$ occurs,

$$ \frac{|\mathcal{X}_{k-1}|}{|\mathcal{X}_k|} = \mathbf{P}\{Y \in \mathcal{X}_{k-1}\} = \mathbf{P}(A) \geq \left( \frac{q - \Delta - 1}{q - \Delta} \right)^\Delta \frac{1}{q} $$

$$ \geq \left( \frac{\Delta}{\Delta + 1} \right)^\Delta \frac{1}{q} \geq \frac{1}{eq} \,. $$

$\blacksquare$

### PDF page 227 (book page 211)

PROOF OF THEOREM 14.14. This proof follows closely the argument of **Jerrum and Sinclair (1996**). Fix a proper coloring $x_0$, and let $\mathcal{X}_k$ be as defined above.

A random element of $\mathcal{X}_k$ can be generated using a slight modification to the Glauber dynamics introduced in Section 3.3.1 and analyzed in Section 14.3. The chain evolves as before, but only the colors at vertices $\{v_1, \ldots, v_k\}$ are updated. The other vertices are frozen in the configuration specified by $x_0$. The bound of Theorem 14.10 on $t_{\mathrm{mix}}(\varepsilon)$ still holds, with $k$ replacing $n$. In addition, (14.20) itself holds, since $k \leq n$. By definition of $t_{\mathrm{mix}}(\varepsilon)$, if

$$ t(n, \varepsilon) := \left\lceil \frac{n \log n + n \log(6eqn/\varepsilon)}{c(q, \Delta)} \right\rceil \,, $$

then the Glauber dynamics $P_k$ on $\mathcal{X}_k$ satisfies

$$ \left\| P_k^{t(n,\varepsilon)}(x_0, \cdot) - \pi_k \right\|_{\mathrm{TV}} < \frac{\varepsilon}{6eqn}, \tag{14.23} $$

where $\pi_k$ is uniform on $\mathcal{X}_k$.

The ratio $|\mathcal{X}_{k-1}|/|\mathcal{X}_k|$ can be estimated as follows: a random element from $\mathcal{X}_k$ can be generated by running the Markov chain for $t(n, \varepsilon)$ steps. Repeating independently $a_n := \lceil 27qn/\eta \varepsilon^2 \rceil$ times yields $a_n$ elements of $\mathcal{X}_k$. Let $Z_{k,i}$, for $i = 1, \ldots, a_n$, be the indicator that the $i$-th sample is an element of $\mathcal{X}_{k-1}$. (Observe that to check if an element $x$ of $\mathcal{X}_k$ is also an element of $\mathcal{X}_{k-1}$, it is enough to determine if $x(v_k) = x_0(v_k)$.) Using (14.23) yields

$$ |\mathbf{E}Z_{k,i} - \pi_k(\mathcal{X}_{k-1})| = |P_k^{t(n,\varepsilon)}(x_0, \mathcal{X}_{k-1}) - \pi_k(\mathcal{X}_{k-1})| \leq \frac{\varepsilon}{6eqn}. $$

Therefore, if $W_k := a_n^{-1} \sum_{i=1}^{a_n} Z_{k,i}$ is the fraction of these samples which fall in $\mathcal{X}_{k-1}$, then

$$ \left| \mathbf{E}W_k - \frac{|\mathcal{X}_{k-1}|}{|\mathcal{X}_k|} \right| = \left| \mathbf{E}Z_{k,1} - \frac{|\mathcal{X}_{k-1}|}{|\mathcal{X}_k|} \right| \leq \frac{\varepsilon}{6eqn} \tag{14.24} $$

Because $Z_{k,i}$ is a Bernoulli($\mathbf{E}Z_{k,i}$) random variable and the $Z_{k,i}$'s are independent,

$$ \mathrm{Var}(W_k) = \frac{1}{a_n^2} \sum_{i=1}^{a_n} \mathbf{E}Z_{k,i}[1 - \mathbf{E}Z_{k,i}] \leq \frac{1}{a_n^2} \sum_{i=1}^{a_n} \mathbf{E}Z_{k,i} \leq \frac{\mathbf{E}(W_k)}{a_n}. $$

Consequently,

$$ \frac{\mathrm{Var}(W_k)}{\mathbf{E}^2(W_k)} \leq \frac{1}{a_n \mathbf{E}(W_k)}. \tag{14.25} $$

By Lemma 14.16, $|\mathcal{X}_{k-1}|/|\mathcal{X}_k| \geq (eq)^{-1}$, and so from (14.24),

$$ \mathbf{E}(W_k) \geq \frac{1}{eq} - \frac{\varepsilon}{6eqn} \geq \frac{1}{3q}. $$

Using the above in (14.25) shows that

$$ \frac{\mathrm{Var}(W_k)}{\mathbf{E}^2(W_k)} \leq \frac{3q}{a_n} \leq \frac{\eta \varepsilon^2}{9n}. \tag{14.26} $$

From (14.24) and Lemma 14.16 we obtain

$$ 1 - \frac{\varepsilon}{6} \leq \frac{|\mathcal{X}_k|}{|\mathcal{X}_{k-1}|} \mathbf{E}W_k \leq 1 + \frac{\varepsilon}{6} \,. $$

### PDF page 228 (book page 212)

Let $W = \prod_{i=1}^n W_i$. Multiplying over $k = 1, \ldots, n$ yields

$$ 1 - \frac{n\varepsilon}{6} \leq \left( 1 - \frac{\varepsilon}{6} \right)^n \leq |\mathcal{X}|\mathbf{E}W \leq \left( 1 + \frac{\varepsilon}{6} \right)^n \leq e^{n\varepsilon/6} \leq 1 + \frac{n\varepsilon}{3} \,. $$

Therefore,

$$ \left| \mathbf{E}(W) - \frac{1}{|\mathcal{X}|} \right| \leq \frac{\varepsilon}{3|\mathcal{X}|} \,. \tag{14.27} $$

Also,

$$ \mathbf{E} \left( \frac{W}{\mathbf{E}W} \right)^2 = \mathbf{E} \prod_{i=1}^n \left( \frac{W_i}{\mathbf{E}W_i} \right)^2 = \prod_{i=1}^n \frac{\mathbf{E}W_i^2}{(\mathbf{E}W_i)^2}. $$

Subtracting 1 from both sides shows that

$$ \frac{\mathrm{Var}(W)}{\mathbf{E}^2(W)} = \prod_{k=1}^n \left[ 1 + \frac{\mathrm{Var}\, W_k}{\mathbf{E}^2(W_k)} \right] - 1. $$

This identity, together with (14.26), shows that

$$ \frac{\mathrm{Var}(W)}{\mathbf{E}^2(W)} \leq \prod_{k=1}^n \left[ 1 + \frac{\eta \varepsilon^2}{9n} \right] - 1 \leq e^{\eta \varepsilon^2/9} - 1 \leq \frac{2\eta \varepsilon^2}{9}. $$

(The last inequality uses that $e^x \leq 1 + 2x$ for $0 \leq x \leq 1$.) By Chebyshev's inequality,

$$ \mathbf{P}\{|W - \mathbf{E}(W)| \geq \mathbf{E}(W)\varepsilon/2\} \leq \eta. $$

On the event $|W - \mathbf{E}(W)| < \mathbf{E}(W)\varepsilon/2$, using (14.27) and the triangle inequality,

$$ |W - \frac{1}{|\mathcal{X}|}| \leq \frac{\varepsilon}{3|\mathcal{X}|} + \frac{\varepsilon}{2}|\mathbf{E}(W)| $$

$$ \leq \frac{\varepsilon}{3|\mathcal{X}|} + \frac{\varepsilon}{2} \left( \frac{1}{|\mathcal{X}|} + \frac{1}{3|\mathcal{X}|} \right) = \frac{\varepsilon}{|\mathcal{X}|} $$

Thus (14.22) is established.

We need $a_n$ samples for each $\mathcal{X}_k$, which shows that at most (14.21) Glauber updates are required.

$\blacksquare$

With more care, the number of required Glauber updates can be reduced further. See Exercise 14.13.

<div align="center">

**Exercises**

</div>

EXERCISE 14.1. Let $M$ be an arbitrary set, and, for $a, b \in M$, define

$$ \rho(a, b) = \begin{cases} 0 & \text{if } a = b, \\ 1 & \text{if } a \neq b. \end{cases} \tag{14.28} $$

Check that $M$ is a metric space under the distance $\rho$ and the corresponding transportation metric is the total variation distance.

EXERCISE 14.2. A real-valued function $f$ on a metric space $(\Omega, \rho)$ is called ***Lipschitz*** if there is a constant $c$ so that for all $x, y \in \Omega$,

$$ |f(x) - f(y)| \leq c\rho(x, y), \tag{14.29} $$

### PDF page 229 (book page 213)

where $\rho$ is the distance on $\Omega$. We denote the best constant $c$ in (14.29) by $\mathrm{Lip}(f)$:

$$ \mathrm{Lip}(f) := \max_{\substack{x,y \in \Omega \\ x \neq y}} \frac{|f(x) - f(y)|}{\rho(x,y)}. $$

For a probability $\mu$ on $\Omega$, the integral $\int f d\mu$ denotes the sum $\sum_{x \in \Omega} f(x)\mu(x)$. Define

$$ \tilde{\rho}_k(\mu, \nu) = \sup_{f \,:\, \mathrm{Lip}(f) \leq 1} \left| \int f d\mu - \int f d\nu \right|. $$

Show that $\tilde{\rho}_K \leq \rho_K$. (In fact, $\tilde{\rho}_K = \rho_K$; see Notes.)

EXERCISE 14.3. Assume the state space $\mathcal{X}$ is a graph and $\rho$ is the graph distance on $\mathcal{X}$, and $P$ is an irreducible transition matrix on $\mathcal{X}$. Let diam be the diameter of $\mathcal{X}$ with respect to this metric, and suppose that

$$ \rho_K(\mu P, \nu P) \leq e^{-\alpha} \rho_K(\mu, \nu) \,. $$

Show that

$$ \mathrm{diam} \leq \frac{2}{1 - e^{-\alpha}} \,. $$

In the lazy case, the right-hand side can be reduced to $\frac{1}{1 - e^{-\alpha}}$.

Check that this inequality is sharp for lazy random walk on the hypercube.

*Hint:* Consider the optimal coupling of $P(x, \cdot)$ with $P(y, \cdot)$, where $\rho(x, y) = \mathrm{diam}$.

EXERCISE 14.4. Let $H(1)$ be a uniform sample from $[k]$. Given that $H(i)$ has been assigned for $i = 1, \ldots, j-1$, choose $H(j)$ uniformly from $[k] \setminus \{H(j-1)\}$. Repeat for $j = 2, \ldots, n$. Show that $H$ is a uniform sample from $\mathcal{X}_{k,n}$, the set of proper $k$-colorings of the $n$-vertex path.

EXERCISE 14.5. Recall that the ***Fibonacci numbers*** are defined by $f_0 := f_1 := 1$ and $f_n := f_{n-1} + f_{n-2}$ for $n \geq 2$. Show that the number of configurations in the one-dimensional hardcore model with $n$ sites is $f_{n+1}$.

EXERCISE 14.6. Show that the algorithm described in Example 14.12 generates a uniform sample from $\mathcal{X}_n$.

EXERCISE 14.7. Describe a simple exact sampling mechanism, in the style of Exercises 14.4 and 14.6, for the Ising model on the $n$-vertex path.

EXERCISE 14.8. Consider the chain on state space $\{0,1\}^n$ which at each move flips the bits at $\delta n$ of the coordinates, where these coordinates are chosen uniformly at random.

Show that the mixing time for this chain is $O(\log n)$.

EXERCISE 14.9. Provide another proof of Theorem 13.1 by using (12.37).

EXERCISE 14.10. In Example 14.9, assume $k = n/2$ and prove the lower bound, for all $\varepsilon > 0$,

$$ t_{\mathrm{mix}}(\varepsilon) \geq [1 + o(1)] \frac{n \log n}{4} \quad \text{as } n \to \infty \,. $$

EXERCISE 14.11. Suppose that $G$ is a graph with maximum degree $\Delta$. Show that if $q \geq \Delta + 2$, then the Glauber dynamics on the space of proper $q$-coloring of $G$ is irreducible. (Equivalently, the graph on proper $q$-colorings induced by single-site updates is connected.)

### PDF page 230 (book page 214)

EXERCISE 14.12. Suppose that $G$ is a finite tree and $q \geq 3$. Show that the graph on proper $q$-colorings induced by single-site Glauber updates is connected.

EXERCISE 14.13. Reduce the running time of the counting procedure in Theorem 14.14 by using Theorem 13.1 and Theorem 12.21.

**Notes**

The transportation metric was introduced in **Kantorovich (1942)**. It has been rediscovered many times and is also known as the Wasserstein metric, thanks to a reintroduction in **Vasershtein (1969)**. For some history of this metric, see **Vershik (2004)**. See also **Villani (2003)**.

The name "transportation metric" comes from the following problem: suppose a unit of materiel is spread over $n$ locations $\{1, 2, \ldots, n\}$ according to the distribution $\mu$, so that proportion $\mu(i)$ is at location $i$. You wish to re-allocate the materiel according to another distribution $\nu$, and the per unit cost of moving from location $i$ to location $j$ is $\rho(i, j)$. For each $i$ and $j$, what proportion $p(i, j)$ of mass at location $i$ should be moved to location $j$ so that $\sum_{i=1}^{n} \mu(i)p(i,j)$, the total amount moved to location $j$, equals $\nu(j)$ and so that the total cost is minimized? The total cost when using $p$ equals

$$ \sum_{i=1}^{n} \sum_{j=1}^{n} \rho(i,j)\mu(i)p(i,j). $$

Since $q(i, j) = \mu(i)p(i, j)$ is a coupling of $\mu$ and $\nu$, the problem is equivalent to finding the coupling $q$ which minimizes

$$ \sum_{1 \leq i,j \leq n} \rho(i,j)q(i,j). $$

The problem of mixing for chains with stationary distribution uniform over proper $q$-colorings was first analyzed by **Jerrum (1995)**, whose bound we present as Theorem 14.10, and independently by **Salas and Sokal (1997)**. **Vigoda (2000)** showed that if the number of colors $q$ is larger than $(11/6)\Delta$, then the mixing times for the Glauber dynamics for random colorings is $O(n^2 \log n)$. Combining his paper with Theorem 13.1 shows that this can be reduced to $O(n^2)$. **Dyer, Greenhill, and Molloy (2002)** show that the mixing time is $O(n \log n)$ provided $q \geq (2 - 10^{-12})\Delta$. A key open question is whether $q > \Delta + C$ suffices to imply the mixing time is polynomial, or perhaps even $O(n \log n)$. **Frieze and Vigoda (2007)** wrote a survey on using Markov chains to sample from colorings.

The inequality in Exercise 14.2 is actually an equality, as was shown in **Kantorovich and Rubinstein (1958)**. In fact, the theorem is valid more generally on separable metric spaces; the proof uses a form of duality. See **Dudley (2002**, Theorem 11.8.2).

The relation between sampling and approximate counting first appeared in **Jerrum, Valiant, and Vazirani (1986)**. **Jerrum, Sinclair, and Vigoda (2004)** approximately count perfect matchings in bipartite graphs. For more on approximate counting, see **Sinclair (1993)**.

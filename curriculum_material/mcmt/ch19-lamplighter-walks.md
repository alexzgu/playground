# Chapter 19 — Lamplighter Walks
*(PDF pages 288–295; book pages 272–279)*

### PDF page 288 (book page 272)

CHAPTER 19

# Chapter 19 — Lamplighter Walks

**19.1. Introduction**

Imagine placing a lamp at each vertex of a finite graph $G = (V, E)$. Now allow a (possibly intoxicated?) lamplighter to perform a random walk on $G$, switching lights randomly on and off as he visits them.

This process can be modeled as a random walk on the **wreath product** $G^\diamond$, whose vertex set is $V^\diamond = \{0,1\}^V \times V$, the ordered pairs $(f, v)$ with $v \in V$ and $f \in \{0,1\}^V$. There is an edge between $(f, v)$ and $(h, w)$ in the graph $G^\diamond$ if $v, w$ are adjacent or identical in $G$ and $f(u) = h(u)$ for $u \notin \{v, w\}$. We call $f$ the **configuration of the lamps** and $v$ the **position of the lamplighter**. In the configuration function $f$, zeroes correspond to lamps that are off, and ones correspond to lamps that are on.

We now construct a Markov chain on $G^\diamond$. Let $\Upsilon$ denote the transition matrix for the lamplighter walk, and let $P$ be the transition matrix of the lazy simple random walk on $G$.

- For $v \neq w$, $\Upsilon[(f, v), (h, w)] = P(v, w)/4$ if $f$ and $h$ agree outside of $\{v, w\}$.
- When $v = w$, $\Upsilon[(f, v), (h, v)] = P(v, v)/2$ if $f$ and $h$ agree off of $\{v\}$.

*[Figure: an octagonal ring (an 8-cycle) of eight lampposts, each with a lantern, with a stick-figure lamplighter standing at the top of the cycle.]*

FIGURE 19.1. A lamplighter on an 8-cycle.

### PDF page 289 (book page 273)

That is, at each time step, the current lamp is randomized, the lamplighter moves from $v$ to $w$, and then the new lamp is also randomized. (The lamp at $w$ is randomized in order to make the chain reversible. We have used the lazy walk on $G$ as the basis for the construction to avoid periodicity problems later.) We will assume throughout this chapter that $G$ is connected, which implies that both $P$ and $\Upsilon$ are irreducible. We write $\pi$ for the stationary distribution of $P$, and $\pi^\diamond$ for the stationary distribution of $\Upsilon$. Note that $\pi^\diamond$ is the product measure $[(\delta_0 + \delta_1)/2]^V \otimes \pi$.

Since the configuration of lamps on visited states is uniformly distributed, allowing the lamplighter to walk for the cover time of the underlying walk suffices to randomize the lamp configuration—although perhaps not the position of the lamplighter himself. In this chapter we study several connections between the underlying chain $G$ and the lamplighter chain $G^\diamond$.

We have by now defined several time parameters associated with a finite Markov chain. Define $t_1 \lesssim t_2$ if there exists a constant $c > 0$ such that $t_1 \leq ct_2$. We have shown

$$ t_{\mathrm{rel}} \lesssim t_{\mathrm{mix}} \lesssim t_{\mathrm{hit}} \lesssim t_{\mathrm{cov}}, \tag{19.1} $$

where the first inequality holds for reversible chains (Theorem 12.5), the second inequality holds for reversible lazy chains (Remark 10.23), and the last holds generally.

In the next section, we prove that the relaxation time $t_{\mathrm{rel}}$ of the lamplighter walk is comparable to the maximal hitting time $t_{\mathrm{hit}}$ of the underlying walk (Theorem 19.1). In Section 19.3, we show that the cover time $t_{\mathrm{cov}}$ of the walk on $G$ is comparable to the mixing time for the lamplighter walk on $G^\diamond$.

**19.2. Relaxation Time Bounds**

THEOREM 19.1. *Let $G$ be a graph and $G^\diamond$ the corresponding lamplighter graph. Then*

$$ \frac{1}{4\log 4} t_{\mathrm{hit}}(G) \leq t_{\mathrm{rel}}(G^\diamond) \leq 6 t_{\mathrm{hit}}(G) \,. \tag{19.2} $$

PROOF. To prove the lower bound, we use the variational formula of Lemma 13.7 to show that the spectral gap for the transition matrix $\Upsilon^t$ is bounded away from 1 when $t = t_{\mathrm{hit}}(G_n)/4$. For the upper bound, we use the coupling contraction method of **Chen (1998)**, which we have already discussed (Theorem 13.1). The geometry of lamplighter graphs allows us to refine this coupling argument and restrict our attention to pairs of states such that the position of the lamplighter is the same in both states.

*Lower bound.* Fix a vertex $w \in G$ that maximizes $\mathbf{E}_\pi(\tau_w)$, and define $\varphi : V^\diamond \to \{0, 1\}$ by $\varphi(f, v) = f(w)$. Then $\mathrm{Var}_{\pi^\diamond}(\varphi) = 1/4$. Let $(Y_t)$ be the Markov chain on $G^\diamond$ with initial distribution $\pi^\diamond$, so that $Y_t$ has distribution $\pi^\diamond$ for all $t \geq 0$. We write $Y_t = (F_t, X_t)$, where $X_t$ is the position of the walk at time $t$, and $F_t$ is the configuration of lamps at time $t$. Applying Lemma 13.6 to $\Upsilon^t$ and then conditioning on the walk's path up to time $t$ shows that

$$ \begin{aligned} \mathcal{E}_t^\diamond(\varphi) &= \frac{1}{2}\mathbf{E}_{\pi^\diamond}\left[\varphi(Y_t) - \varphi(Y_0)\right]^2 \\ &= \frac{1}{2}\mathbf{E}_{\pi^\diamond}\left(\mathbf{E}_{\pi^\diamond}[(\varphi(Y_t) - \varphi(Y_0))^2 \mid X_0, \ldots, X_t]\right). \end{aligned} \tag{19.3} $$

### PDF page 290 (book page 274)

Observe that

$$ \begin{aligned} \mathbf{E}_{\pi^\diamond}[(\varphi(Y_t) - \varphi(Y_0))^2 \mid X_0, \ldots X_t] &= \mathbf{E}_{\pi^\diamond}[(F_t(w) - F_0(w))^2 \mid X_0, \ldots, X_t] \\ &= \frac{1}{2}\mathbf{1}_{\{\tau_w \leq t\}}, \end{aligned} $$

as $|F_t(w) - F_0(w)| = 1$ if and only if the walk visits $w$ by time $t$, and, at the walk's last visit to $w$ before or at time $t$, the lamp at $w$ is refreshed to a state different from its initial state. Combining the above equality with (19.3) shows that

$$ \mathcal{E}_t^\diamond(\varphi) = \frac{1}{4}\mathbf{P}_\pi\{\tau_w \leq t\}. \tag{19.4} $$

For any $t$,

$$ \mathbf{E}_v\tau_w \leq t + t_{\mathrm{hit}}\mathbf{P}_v\{\tau_w > t\}. \tag{19.5} $$

This follows because if a walk on $G$ started at $v$ has not hit $w$ by time $t$, the expected additional time to arrive at $w$ is bounded by $t_{\mathrm{hit}}$. Averaging (19.5) over $\pi$ shows that

$$ \mathbf{E}_\pi\tau_w \leq t + t_{\mathrm{hit}}\mathbf{P}_\pi\{\tau_w > t\}. \tag{19.6} $$

By Lemma 10.2 and our choice of $w$, we have $t_{\mathrm{hit}} \leq 2\mathbf{E}_\pi\tau_w$, whence (19.6) implies that

$$ t_{\mathrm{hit}} \leq 2t + 2t_{\mathrm{hit}}\mathbf{P}_\pi\{\tau_w > t\}. $$

Substituting $t = t_{\mathrm{hit}}/4$ and rearranging yields

$$ \mathbf{P}_\pi\{\tau_w \leq t_{\mathrm{hit}}/4\} \leq \frac{3}{4}. $$

Let $\Lambda_2$ be the second largest eigenvalue of $\Upsilon$. By Remark 13.8 and (19.4), we thus have

$$ 1 - \Lambda_2^{t_{\mathrm{hit}}/4} \leq \frac{\mathcal{E}_{t_{\mathrm{hit}}/4}^\diamond(\varphi)}{\mathrm{Var}_{\pi^\diamond}(\varphi)} \leq \frac{3}{4} \,. $$

Therefore

$$ \log 4 \geq \frac{t_{\mathrm{hit}}}{4}(1 - \Lambda_2), $$

which gives the claimed lower bound on $t_{\mathrm{rel}}(G^\diamond)$, with $c_1 = \frac{1}{4\log 4}$. (Note that since the walk is lazy, $|\Lambda_2| = \Lambda_2$.)

*Upper bound.* If $\Lambda_2 < 1/2$, then $t_{\mathrm{rel}}(G^\diamond) \leq 2 \leq 2t_{\mathrm{hit}}(G)$. Thus we assume without loss of generality that $\Lambda_2 \geq 1/2$. We use a coupling argument related to that of Theorem 13.1. Suppose $\varphi$ is an eigenfunction for $\Upsilon$ with eigenvalue $\Lambda_2$. Note that for lamp configurations $f$ and $g$ on $G$, the $\ell^1$ norm $\|f - g\|_1$ is equal to the number of bits in which $f$ and $g$ differ. Let

$$ M = \max_{f,g,x} \frac{|\varphi(f, x) - \varphi(g, x)|}{\|f - g\|_1}. $$

(Note that $M$ is a restricted version of a Lipschitz constant: the maximum is taken only over states with the same lamplighter position.)

If $M = 0$, then $\varphi(f, x)$ depends only on $x$ and $\psi(x) = \varphi(f, x)$ is an eigenfunction for the transition matrix $P$ with eigenvalue $\Lambda_2$. Applying (12.15) with $t = 2t_{\mathrm{hit}} + 1$ together with (10.34) yields

$$ \Lambda_2^{2t_{\mathrm{hit}}+1} \leq 2d(2t_{\mathrm{hit}} + 1) \leq 2\frac{1}{4} = \frac{1}{2} \,. $$

Now we treat the case $M > 0$. Couple two lamplighter walks, one started at $(f, x)$ and one at $(g, x)$, by using the same lamplighter steps and updating the

### PDF page 291 (book page 275)

configurations so that they agree at each site visited by the lamplighter. Let $(F_t, X_t)$ and $(G_t, X_t)$ denote the positions of the coupled walks after $t = 2t_{\text{hit}}$ steps. Because $\varphi$ is an eigenfunction for $\Upsilon$,

$$
\begin{aligned}
\Lambda_2^{2t_{\text{hit}}} M &= \sup_{f,g,x} \frac{\left|\Upsilon^{2t_{\text{hit}}}\varphi(f,x) - \Upsilon^{2t_{\text{hit}}}\varphi(g,x)\right|}{\|f - g\|_1} \\
&\leq \sup_{f,g,x} \mathbf{E}\left[\frac{|\varphi(F_t, X_t) - \varphi(G_t, X_t)|}{\|F_t - G_t\|_1} \frac{\|F_t - G_t\|_1}{\|f - g\|_1}\right] \\
&\leq M \sup_{f,g,x} \frac{\mathbf{E}\,\|F_t - G_t\|_1}{\|f - g\|_1}.
\end{aligned}
$$

At time $t = 2t_{\text{hit}}$, each lamp that contributes to $\|f - g\|_1$ has probability of at least $1/2$ of having been visited, so $\mathbf{E}\,\|F_t - G_t\|_1 \leq \|f - g\|_1 / 2$. Dividing by $M$ gives the bound of $\Lambda_2^{2t_{\text{hit}}} \leq 1/2$.

Thus in both cases, $\Lambda_2^{2t_{\text{hit}}+1} \leq 1/2$. Let $\Gamma = 1 - \Lambda_2$. Then

$$
\frac{1}{2} \geq (1 - \Gamma)^{2t_{\text{hit}}+1} \geq 1 - (2t_{\text{hit}} + 1)\Gamma \geq 1 - 3t_{\text{hit}}\Gamma\,.
$$

We conclude that $t_{\text{rel}}(G^\diamond) \leq 6t_{\text{hit}}(G)$. $\blacksquare$

**19.3. Mixing Time Bounds**

THEOREM 19.2. *Let $t_{\text{cov}}$ be the cover time for lazy simple random walk on $G$. The mixing time $t_{\text{mix}}(G^\diamond)$ of the lamplighter chain on $G^\diamond$ satisfies*

$$
\frac{1}{8}t_{\text{cov}} \leq t_{\text{mix}}(G^\diamond) \leq 17t_{\text{cov}}\,. \tag{19.7}
$$

We first prove a lemma needed in the proof of the lower bound.

LEMMA 19.3. *Let $G$ be a graph with vertex set $V$. For the lamplighter chain on $G^\diamond$, the separation distance $s^\diamond(t)$ satisfies*

$$
s^\diamond(t) \geq \mathbf{P}_w\{\tau_{\text{cov}} > t\} \tag{19.8}
$$

*for every $w \in V$ and $t > 0$.*

PROOF. Let $w_t \in V$ be the vertex minimizing $\mathbf{P}_w\{X_t = w_t \mid \tau_{\text{cov}} \leq t\}/\pi(w_t)$. Since $\mathbf{P}_w\{X_t = \cdot \mid \tau_{\text{cov}} \leq t\}$ and $\pi$ are both probability distributions on $V$, we have $\mathbf{P}_w\{X_t = w_t \mid \tau_{\text{cov}} \leq t\} \leq \pi(w_t)$. Suppose $|V| = n$. Since the only way to go from all lamps off to all lamps on is to visit every vertex, we have

$$
\begin{aligned}
\frac{\Upsilon^t((\mathbf{0}, w), (\mathbf{1}, w_t))}{\pi^\diamond(\mathbf{1}, w_t)} &= \frac{\mathbf{P}_w\{\tau_{\text{cov}} \leq t\}2^{-n}\mathbf{P}_w\{X_t = w_t \mid \tau_{\text{cov}} \leq t\}}{2^{-n}\pi(w_t)} \\
&\leq \mathbf{P}_w\{\tau_{\text{cov}} \leq t\}. \tag{19.9}
\end{aligned}
$$

Subtracting from 1 yields $s^\diamond(t) \geq \mathbf{P}_w\{\tau_{\text{cov}} > t\}$. $\blacksquare$

PROOF OF THEOREM 19.2. Throughout the proof, diamonds indicate parameters for the lamplighter chain.

*Upper bound.* Let $(F_t, X_t)$ denote the state of the lamplighter chain at time $t$. We will run the lamplighter chain long enough that, with high probability, every lamp has been visited and enough additional steps have been taken to randomize the position of the lamplighter.

### PDF page 292 (book page 276)

Set $u = 8t_{\text{cov}} + t_{\text{mix}}(G, 1/8)$ and fix an initial state $(\mathbf{0}, v)$. Define the probability distribution $\mu_s$ on $G^\diamond$ by

$$
\mu_s = \mathbf{P}_{(\mathbf{0},v)}\{(F_u, X_u) \in \cdot \mid \tau_{\text{cov}} = s\}.
$$

Then

$$
\Upsilon^u((0, v), \cdot) = \sum_s \mathbf{P}_{(\mathbf{0},v)}\{\tau_{\text{cov}} = s\}\mu_s.
$$

By the triangle inequality,

$$
\|\Upsilon^u((\mathbf{0}, v), \cdot) - \pi^\diamond\|_{\text{TV}} \leq \sum_s \mathbf{P}_{(\mathbf{0},v)}\{\tau_{\text{cov}} = s\}\,\|\mu_s - \pi^\diamond\|_{\text{TV}}\,. \tag{19.10}
$$

Since $\mathbf{P}\{\tau_{\text{cov}} > 8t_{\text{cov}}\} < 1/8$ and the total variation distance between distributions is bounded by 1, we can bound

$$
\|\Upsilon^u((\mathbf{0}, v), \cdot) - \pi^\diamond\|_{\text{TV}} \leq 1/8 + \sum_{s \leq 8t_{\text{cov}}} \mathbf{P}_{(\mathbf{0},v)}\{\tau_{\text{cov}} = s\}\,\|\mu_s - \pi^\diamond\|_{\text{TV}}\,. \tag{19.11}
$$

Recall that $G$ has vertex set $V$. Let $\nu$ denote the uniform distribution on $\{0,1\}^V$. For $s \leq u$, conditional on $\tau_{\text{cov}} = s$ and $X_s = x$, the distribution of $F_u$ equals $\nu$, the distribution of $X_u$ is $P^{u-s}(x, \cdot)$, and $F_u$ and $X_u$ are independent. Thus,

$$
\begin{aligned}
\mu_s &= \sum_{x \in V} \mathbf{P}_{(\mathbf{0},v)}\{(F_u, X_u) \in \cdot \mid \tau_{\text{cov}} = s,\, X_s = x\}\mathbf{P}_{(\mathbf{0},v)}\{X_s = x \mid \tau_{\text{cov}} = s\} \\
&= \sum_{x \in V} [\nu \times P^{u-s}(x, \cdot)]\mathbf{P}_{(\mathbf{0},v)}\{X_s = x \mid \tau_{\text{cov}} = s\}.
\end{aligned}
$$

By the triangle inequality and Exercise 4.4, since $\pi^\diamond = \nu \times \pi$,

$$
\begin{aligned}
\|\mu_s - \pi^\diamond\|_{\text{TV}} &\leq \sum_{x \in V} \left\|\nu \times P^{u-s}(x, \cdot) - \pi^\diamond\right\|_{\text{TV}} \mathbf{P}_{(\mathbf{0},v)}\{X_s = x \mid \tau_{\text{cov}} = s\} \\
&\leq \max_{x \in V}\left\|P^{u-s}(x, \cdot) - \pi\right\|_{\text{TV}}\,. \tag{19.12}
\end{aligned}
$$

For $s \leq 8t_{\text{cov}}$, we have $u - s \geq t_{\text{mix}}(G, 1/8)$, by definition of $u$. Consequently, by (19.12), for $s \leq 8t_{\text{cov}}$,

$$
\|\mu_s - \pi^\diamond\|_{\text{TV}} \leq \frac{1}{8}. \tag{19.13}
$$

Using (19.13) in (19.11) shows that

$$
\|\Upsilon^u((\mathbf{0}, v), \cdot) - \pi^\diamond\|_{\text{TV}} \leq 1/8 + (1)(1/8) = 1/4. \tag{19.14}
$$

To complete the upper bound, by (4.33) and (10.35)

$$
t_{\text{mix}}(G, 1/8) \leq 3t_{\text{mix}} \leq 9t_{\text{cov}}\,.
$$

Since $u = 8t_{\text{cov}} + t_{\text{mix}}(G, 1/8)$, it follows that $t_{\text{mix}} \leq 17t_{\text{cov}}$.

*Lower bound.* Lemmas 4.10 and 4.11 imply that

$$
\bar{d}^\diamond(2t_{\text{mix}}^\diamond) \leq 1/4,
$$

and Lemma 6.17 yields

$$
s^\diamond(4t_{\text{mix}}^\diamond) \leq 1 - (1 - \bar{d}^\diamond(2t_{\text{mix}}^\diamond))^2 \leq 1 - (3/4)^2 < 1/2.
$$

By Lemma 19.3 applied to $G$ with $t = 4t_{\text{mix}}^\diamond$, we have

$$
\mathbf{P}_w\{\tau_{\text{cov}} > 4t_{\text{mix}}^\diamond\} < 1/2.
$$

Exercise 11.7 implies that $t_{\text{cov}} \leq 8t_{\text{mix}}^\diamond$. $\blacksquare$

### PDF page 293 (book page 277)

**19.4. Examples**

If $a_n = O(b_n)$ and $b_n = O(a_n)$, then we write $a_n = \Theta(b_n)$.

**19.4.1. The complete graph.** When $G_n$ is the complete graph on $n$ vertices, with self-loops, then the chain we study on $G_n^\diamond$ is a random walk on the hypercube— although not quite the standard one, since two bits can change in a single step. The maximal hitting time is $n$ and the expected cover time is an example of the coupon collector problem. Hence the relaxation time and the mixing time for $G_n^\diamond$ are $\Theta(n)$ and $\Theta(n \log n)$, respectively, just as for the standard walk on the hypercube.

**19.4.2. Hypercube.** Let $G_n = \mathbb{Z}_2^n$, the $n$-dimensional hypercube. We showed in Exercise 10.6 that the maximal hitting time is $\Theta(2^n)$ and in Exercise 11.3 that the cover time is $\Theta(n2^n)$. In Example 12.16, we saw that for lazy random walk on $G_n$, we have $t_{\text{rel}}(G_n) = n$. Finally, in Section 12.6, we showed that $t_{\text{mix}}(G_n, \varepsilon) \sim (n \log n)/2$. By Theorem 19.1, $t_{\text{rel}}(G_n^\diamond) = \Theta(2^n)$. Theorem 19.2 shows that the $t_{\text{mix}}(G_n^\diamond) = \Theta(n2^n)$.

**19.4.3. Tori.** If the base graph $G$ is the $\mathbb{Z}_n$, then $t_{\text{hit}}(G) = \Theta(n^2)$ and $t_{\text{cov}} = \Theta(n^2)$. (See Section 2.1 and Example 11.1.) Hence the lamplighter chain on the cycle has both its relaxation time and its mixing time are $\Theta(n^2)$. In particular, by Proposition 18.4, there is no cutoff.

For higher-dimensional tori, we have proved enough about hitting and cover times to see that the relaxation time and the mixing time grow at different rates in every dimension $d \geq 2$.

THEOREM 19.4. *The lamplighter chains on $(\mathbb{Z}_n^d)^\diamond$ satisfy, for suitable constants $c_d, C_d$ and $c_d', C_d'$,*

$$
c_2 n^2 \log n \leq t_{\text{rel}}((\mathbb{Z}_n^2)^\diamond) \leq C_2 n^2 \log n\,, \tag{19.15}
$$

$$
c_2' n^2 (\log n)^2 \leq t_{\text{mix}}((\mathbb{Z}_n^2)^\diamond) \leq C_2' n^2 (\log n)^2\,, \tag{19.16}
$$

*and for $d \geq 3$,*

$$
c_d n^d \leq t_{\text{rel}}((\mathbb{Z}_n^d)^\diamond) \leq C_d n^d\,, \tag{19.17}
$$

$$
c_d' n^d \log n \leq t_{\text{mix}}((\mathbb{Z}_n^d)^\diamond) \leq C_d' n^d \log n\,. \tag{19.18}
$$

PROOF. These follow immediately from combining the bounds on the hitting time and the cover time for tori from Proposition 10.21 and Section 11.3.2, respectively, with Theorems 19.1 and 19.2. $\blacksquare$

**Exercises**

EXERCISE 19.1. Show that the diameter of $G^\diamond$ is at most $c|V|$, where $V$ is the vertex set of the base graph $G$.

*Hint:* Consider depth-first search on the spanning tree of $G$.

EXERCISE 19.2. Show that $t_{\text{mix}}(G^\diamond) = O(n^2)$ for a regular graph $G$ on $n$ vertices.

### PDF page 294 (book page 278)

**Notes**

**Häggström and Jonasson (1997)** analyzed the lamplighter chains on the cycle and the complete graph.

The results of this chapter are primarily taken from **Peres and Revelle (2004)**, which derives sharper versions of the bounds we discuss, especially in the case of the two-dimensional torus, and also considers the time required for convergence in the uniform metric. The extension of the lower bound on mixing time in Theorem 19.2 to general (rather than vertex-transitive) graphs is new.

Random walks on (infinite) lamplighter groups were analyzed by Kaĭmanovich and Vershik (**1983**). Their ideas motivate some of the analysis in this chapter.

**Scarabotti and Tolli (2008)** study the eigenvalues of lamplighter walks. They compute the spectra for the complete graph and the cycle, and use representations of wreath products to give more general results.

**Peres and Revelle (2004)** also bound the $\ell^\infty$ mixing time. These bounds were sharpened by **Komjáthy, Miller, and Peres (2014)**.

Let $(G_n)$ be a sequence of graphs. If the lamplighter chains on $(G_n^\diamond)$ have a cutoff in total-variation, then the random walks on $G_n$ must satisfy $t_{\text{hit}}(G_n) = o(t_{\text{cov}}(G_n))$ (by Proposition 18.4), and

$$ \frac{t_{\text{cov}}(G_n)}{2} \le t_{\text{mix}}(G_n^\diamond)[1 + o(1)] \le t_{\text{cov}}(G_n) \,, $$

by Lemma 6.17 and Theorem 19.5 below. **Peres and Revelle (2004)** show cutoff at $t_{\text{cov}}(G_n)$ for the lamplighter chain when the base graph is $G_n = \mathbb{Z}_n^2$. **Miller and Peres (2012)** show that if $G_n = \mathbb{Z}_n^d$ for $d \ge 3$, then there is cutoff for the lamplighter on $G_n^\diamond$ at $t_{\text{cov}}(G_n)/2$. **Dembo, Ding, Miller, and Peres (2013)** show that for any $\alpha \in [1/2, 1]$, there exist a sequence of base graphs $(G_n)$ so that the lamplighter chains on $(G_n^\diamond)$ have cutoff at time $\alpha t_{\text{cov}}(G_n)$.

**Komjáthy and Peres (2013)** considered generalized lamplighter graphs, denoted $H \wr G$, where the lamps take values in a general graph $H$. (When both $G$ and $H$ are groups, this is a Cayley graph of the *wreath product* of $H$ and $G$.) They prove that, for a regular base graph $G$ with vertex set $V$,

$$ t_{\text{rel}}(H \wr G) \asymp t_{\text{hit}}(G) + |V| t_{\text{rel}}(H) \,. $$

**Complements.** Recall the discussion in Section 18.4 of cutoff in separation distance.

THEOREM 19.5. *Let $(G_n)$ be a sequence of graphs with vertex set $V_n$ with $|V_n| \to \infty$. If $t_{\text{hit}}^{(n)} = o\left(t_{\text{cov}}^{(n)}\right)$ as $n \to \infty$, then $(G_n^\diamond)$ has a separation cutoff at time $t_{\text{cov}}^{(n)}$.*

Note that by Theorems 19.1 and 19.2, the hypothesis above implies that $t_{\text{rel}}(G_n^\diamond) = o(t_{\text{mix}}(G_n^\diamond))$.

To prove Theorem 19.5, we will need the following result of **Aldous (1991b)** on the concentration of the cover time.

THEOREM 19.6 (Aldous). *Let $(G_n)$ be a family of graphs with $|V_n| \to \infty$. If $t_{\text{hit}}^{(n)} = o\left(t_{\text{cov}}^{(n)}\right)$ as $n \to \infty$, then*

$$ \frac{\tau_{\text{cov}}^{(n)}}{t_{\text{cov}}^{(n)}} \to 1 \quad \text{in probablity[sic].} $$

### PDF page 295 (book page 279)

PROOF OF THEOREM 19.5. *Lower bound.* Fix $\varepsilon > 0$ and a starting vertex $w$. Take $t < (1 - \varepsilon)t_{\text{cov}}^{(n)}(G_n)$. Applying Lemma 19.3 to $G_n$ gives

$$ s^\diamond(t) \ge \mathbf{P}_w\{\tau_{\text{cov}}^{(n)} > t\} = 1 - \mathbf{P}_w\{\tau_{\text{cov}}^{(n)} \le t\}. $$

However, Theorem 19.6 implies that $\mathbf{P}_w\{\tau_{\text{cov}}^{(n)} \le t\}$ goes to 0, so we are done.

*Upper bound.* Again fix $\varepsilon > 0$, and take $t > (1 + 2\varepsilon)t_{\text{cov}}^{(n)}$. Then for any vertices $v, w$ and any lamp configuration $f$ we have

$$ \Upsilon^t((\mathbf{0}, w), (f, v)) \ge \mathbf{P}_w\{\tau_{\text{cov}}^{(n)} < (1 + \varepsilon)t_{\text{cov}}^{(n)}\} 2^{-|V|} \min_{u \in V_n} P^{\varepsilon t_{\text{cov}}^{(n)}}(u, v), \tag{19.19} $$

by conditioning on the location of the lamplighter at time $t - \varepsilon t_{\text{cov}}^{(n)}$ and recalling that once all vertices have been visited, the lamp configuration is uniform.

Theorem 19.6 implies

$$ \mathbf{P}_w\{\tau_{\text{cov}}^{(n)} < (1 + \varepsilon)t_{\text{cov}}^{(n)}\} = 1 - o(1). \tag{19.20} $$

Theorem 10.22 implies that $t_{\text{mix}} < 3t_{\text{hit}}$ for sufficiently large $n$, so our initial hypothesis implies that $t_{\text{mix}} = o(\varepsilon t_{\text{cov}}^{(n)})$. Applying Lemma 6.17 now tells us that

$$ \min_{u \in V_n} P^{\varepsilon t_{\text{cov}}^{(n)}}(u, v) = \pi(v)(1 - o(1)). \tag{19.21} $$

Taken together (19.19), (19.20), and (19.21) guarantee that the separation distance for the lamplighter chain at time $t$ is $o(1)$. $\blacksquare$

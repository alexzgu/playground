# Chapter 16 — From Shuffling Cards to Shuffling Genes
*(PDF pages 248–258; book pages 232–242)*

### PDF page 248 (book page 232)

CHAPTER 16

# From Shuffling Cards to Shuffling Genes

One reasonable restriction of the random transposition shuffle is to only allow interchanges of adjacent cards—see Figure 16.1. Restricting the moves in this

*[Figure: six playing cards in a row, face-down (cross-hatched backs) with small numbered labels 1, 2, 3, 4, 5, 6; two curved arrows beneath cards 2 and 3 pointing at each other, indicating a swap of the two neighboring cards.]*

FIGURE 16.1. An adjacent transposition swaps two neighboring cards.

manner slows the shuffle down. It also breaks the symmetry of the random transpositions walk enough to require different methods of analysis.

In Section 16.1 we examine the mixing of the random adjacent transpositions walk using several different methods: upper bounds via comparison (way off) and coupling (quite sharp) and lower bounds via following a single card (off by a log factor) and Wilson's method (sharp).

A generalization of the random adjacent transpositions model, in which entire segments of a permutation are reversed in place, can be interpreted as modeling large-scale genome changes. Varying the maximum allowed length of the reversed segments impacts the mixing time significantly. We study these reversal chains in Section 16.2.

**16.1. Random Adjacent Transpositions**

As usual we consider a lazy version of the chain to avoid periodicity problems. The resulting increment distribution assigns probability $1/[2(n-1)]$ to each of the transpositions $(1\,2), \ldots, (n-1\,n)$ and probability $1/2$ to id.

### PDF page 249 (book page 233)

**16.1.1. Upper bound via comparison.** We can bound the convergence of the random adjacent transposition shuffle by comparing it with the random transposition shuffle. While our analysis considers only the spectral gap and thus gives a poor upper bound on the mixing time, we illustrate the method because it can be used for many types of shuffle chains.

Note: in the course of this proof, we will introduce several constants $C_1, C_2, \ldots$. Since we are deriving such (asymptotically) poor bounds, we will not make any effort to optimize their values. Each one does not depend on $n$.

First, we bound the relaxation time of the random transpositions shuffle by its mixing time. By Theorem 12.5 and Corollary 8.10,

$$ t_{\mathrm{rel}} = O(n \log n). \tag{16.1} $$

(We are already off by a factor of $\log n$, but we will lose so much more along the way that it scarcely matters.)

Next we compare. In order to apply Corollary 13.24, we must express an arbitrary transposition $(a\,b)$, where $1 \le a < b \le n$, in terms of adjacent transpositions. Note that

$$ (a\,b) = (a\,a+1)\cdots(b-1\,b-2)(b-1\,b)(b-1\,b-2)\cdots(a+1\,a+2)(a\,a+1). \tag{16.2} $$

This path has length at most $2n - 3$ and uses any single adjacent transposition at most twice.

We must estimate the congestion ratio

$$ B = \max_{s \in S} \frac{1}{\mu(s)} \sum_{\sigma \in \tilde{S}} \tilde{\mu}(\sigma) N(s, \sigma) \, |\sigma| \le \max_{s \in S} \frac{4(n-1)}{n^2} \sum_{\sigma \in \tilde{S}} N(s, \sigma) \, |\sigma|. \tag{16.3} $$

Here $S$ is the support of the random adjacent transposition walk, $\mu$ is its increment distribution, $\tilde{S}$ and $\tilde{\mu}$ are the corresponding features of the random transpositions walk, $N(s, \sigma)$ is the number of times $s$ is used in the expansion of $\sigma$ as a product of adjacent transpositions, and $|\sigma|$ is the total length of this expansion of $\sigma$. Observe that an adjacent transposition $s = (i\,i+1)$ lies on the generator path of $(a\,b)$ exactly when $a \le i < i + 1 \le b$, no generator path uses any adjacent transposition more than twice, and the length of the generator paths is bounded by $(2n-3)$. Therefore, the summation on the right-hand-side of (16.3) is bounded by $2i(n-i)(2n-3) \le n^3$. Hence

$$ B \le 4n^2, $$

and Corollary 13.24 tells us that the relaxation time of the random adjacent transpositions chain is at most $C_2 n^3 \log n$.

Finally, we use Theorem 12.4 to bound the mixing time by the relaxation time. Here the stationary distribution is uniform, $\pi(\sigma) = 1/n!$ for all $\sigma \in \mathcal{S}_n$. The mixing time of the random adjacent transpositions chain thus satisfies

$$ t_{\mathrm{mix}} \le \log(4n!) C_2 n^3 \log n \le C_3 n^4 \log^2 n. $$

**16.1.2. Upper bound via coupling.** In order to couple two copies $(\sigma_t)$ and $(\sigma_t')$ (the "left" and "right" decks) of the lazy version of the random adjacent transpositions chain, proceed as follows. First, choose a pair $(i, i + 1)$ of adjacent locations uniformly from the possibilities. Flip a fair coin to decide whether to perform the transposition on the left deck. Now, examine the cards at locations $i$ and $i + 1$ in the decks $\sigma$ and $\sigma'$.

### PDF page 250 (book page 234)

- If either $\sigma_t(i) = \sigma_t'(i+1)$ or $\sigma_t(i+1) = \sigma_t'(i)$, then do the opposite on the right deck: transpose if the left deck stayed still, and vice versa.
- Otherwise, perform the same action on the right deck as on the left deck.

We first consider $\tau_a$, the time required for a particular card $a$ to *synchronize*, i.e. to reach the same position in the two decks. Let $X_t$ be the (unsigned) distance between the positions of $a$ in the two decks at time $t$. Our coupling ensures that $|X_{t+1} - X_t| \le 1$ and that if $t \ge \tau_a$, then $X_t = 0$.

Let $M$ be the transition matrix of a random walk on the path with vertices $\{0, \ldots, n-1\}$ that moves up or down, each with probability $1/(n-1)$, at all interior vertices; from $n - 1$ it moves down with probability $1/(n - 1)$, and, under all other circumstances, it stays where it is. In particular, it absorbs at state 0.

Note that for $1 \le i \le n - 1$,

$$ \mathbf{P}\{X_{t+1} = i - 1 \mid X_t = i, \sigma_t, \sigma_t'\} = M(i, i - 1). $$

However, since one or both of the cards might be at the top or bottom of a deck and thus block the distance from increasing, we can only say

$$ \mathbf{P}\{X_{t+1} = i + 1 \mid X_t = i, \sigma_t, \sigma_t'\} \le M(i, i + 1). $$

Even though the sequence $(X_t)$ is not a Markov chain, the above inequalities imply that we can couple it to a random walk $(Y_t)$ with transition matrix $M$ in such a way that $Y_0 = X_0$ and $X_t \le Y_t$ for all $t \ge 0$. Under this coupling $\tau_a$ is bounded by the time $\tau_0^Y$ it takes $(Y_t)$ to absorb at 0.

The chain $(Y_t)$ is best viewed as a delayed version of a simple random walk on the path $\{0, \ldots, n-1\}$, with a hold probability of $1/2$ at $n - 1$ and absorption at 0. At interior nodes, with probability $1 - 2/(n - 1)$, the chain $(Y_t)$ does nothing, and with probability $2/(n-1)$, it takes a step in that walk. Exercises 2.3 and 2.2 imply that $\mathbf{E}(\tau_0^Y)$ is bounded by $(n - 1)n^2/2$, regardless of initial state. Hence

$$ \mathbf{E}(\tau_a) \le \frac{(n-1)n^2}{2}. $$

By Markov's inequality,

$$ \mathbf{P}\{\tau_a > n^3\} < 1/2 \,. $$

If we run $2 \log_2 n$ blocks, each consisting of $n^3$ shuffles, we can see that

$$ \mathbf{P}\{\tau_a > 2n^3 \lceil \log_2 n \rceil\} < \frac{1}{n^2}. \tag{16.4} $$

Therefore,

$$ \mathbf{P}\{\tau_{\mathrm{couple}} > 2n^3 \lceil \log_2 n \rceil\} \le \sum_{a=1}^{n} \mathbf{P}\{\tau_a > 2n^3 \lceil \log_2 n \rceil\} < \frac{1}{n}, \tag{16.5} $$

regardless of the initial states of the decks. Theorem 5.4 immediately implies that

$$ t_{\mathrm{mix}}(\varepsilon) < 2n^3 \lceil \log_2 n \rceil $$

for sufficiently large $n$.

### PDF page 251 (book page 235)

**16.1.3. Lower bound via following a single card.** Consider the set of permutations

$$ A = \{\sigma \,:\, \sigma(1) \ge \lfloor n/2 \rfloor\}. $$

Under the uniform distribution we have $\pi(A) \ge 1/2$, because card 1 is equally likely to be in any of the $n$ possible positions.

Note that the sequence $(\sigma_t(1))$ is a Markov chain on $\{1, 2, \ldots, n\}$ which moves up or down one unit, with probability $1/2(n - 1)$ each, except at the endpoints. When at an endpoint, it moves with probability $1/2(n - 1)$ to the neighboring position.

If $(\tilde{S}_t)$ is a random walk on $\mathbb{Z}$ with $\tilde{S}_0 = 0$ which remains in place with probability $1 - 1/(n - 1)$, and increments by $\pm 1$ with equal probability when it moves, then

$$ \mathbf{P}\{\sigma_t(1) - 1 \ge z\} \le \mathbf{P}\{|\tilde{S}_t| \ge z\}. $$

In particular,

$$ \mathbf{P}\{\sigma_t(1) \ge n/2 + 1\} \le \frac{4\mathbf{E}\tilde{S}_t^2}{n^2} \le \frac{4t}{n^2(n - 1)}. $$

Therefore,

$$ \left\| P^t(\mathrm{id}, \cdot) - \pi \right\|_{\mathrm{TV}} \ge \pi(A) - P^t(\mathrm{id}, A) \ge \frac{1}{2} - \frac{4t}{n^2(n - 1)}. $$

Thus if $t \le n^2(n - 1)/16$, then $d(t) \ge 1/4$. We conclude that $t_{\mathrm{mix}} \ge n^2(n - 1)/16$.

**16.1.4. Lower bound via Wilson's method.** In order to apply Wilson's method (Theorem 13.28) to the random adjacent transpositions shuffle, we must specify an eigenfunction and initial state.

Lemma 12.9 tells us that when $\varphi : [n] \to \mathbb{R}$ is an eigenfunction of the single-card chain with eigenvalue $\lambda$, then $\Phi_k : \mathcal{S}_n \to \mathbb{R}$ defined by $\Phi_k(\sigma) = \varphi(\sigma(k))$ is an eigenfunction of the shuffle chain with eigenvalue $\lambda$.

For the random adjacent transpositions chain, the single-card chain $P'$ is an extremely lazy version of a random walk on the path whose eigenfunctions and eigenvalues were determined in Section 12.3.2. Let $M$ be the transition matrix of simple random walk on the $n$-path with holding probability $1/2$ at the endpoints. Then we have

$$ P' = \frac{1}{n - 1} M + \frac{n - 2}{n - 1} I. $$

It follows from (12.21) that

$$ \varphi(k) = \cos\left(\frac{(2k - 1)\pi}{2n}\right) $$

is an eigenfunction of $P'$ with eigenvalue

$$ \lambda = \frac{1}{n - 1} \cos\left(\frac{\pi}{n}\right) + \frac{n - 2}{n - 1} = 1 - \frac{\pi^2}{2n^3} + O\left(\frac{1}{n^4}\right). \tag{16.6} $$

Hence, for any $k \in [n]$ the function $\sigma \mapsto \varphi(\sigma(k))$ is an eigenfunction of the random transposition walk with eigenvalue $\lambda$. Since these eigenfunctions all lie in the same eigenspace, so will any linear combination of them. We set

$$ \Phi(\sigma) = \sum_{k \in [n]} \varphi(k)\varphi(\sigma(k)). \tag{16.7} $$

### PDF page 252 (book page 236)

REMARK 16.1. See Exercise 16.2 for some motivation of our choice of $\Phi$. By making sure that $\Phi(\mathrm{id})$ is as large as possible, we ensure that when $\Phi(\sigma_t)$ is small, then $\sigma_t$ is in some sense likely to be far away from the identity.

Now consider the effect of a single adjacent transposition $(k-1\,k)$ on $\Phi$. Only two terms in (16.7) change, and we compute

$$\begin{aligned}
|\Phi(\sigma \circ (k-1\,k)) - \Phi(\sigma)| &= |\varphi(k)\varphi(\sigma(k-1)) + \varphi(k-1)\varphi(\sigma(k)) \\
&\qquad - \varphi(k-1)\varphi(\sigma(k-1)) - \varphi(k)\varphi(\sigma(k))| \\
&= |(\varphi(k) - \varphi(k-1))(\varphi(\sigma(k)) - \varphi(\sigma(k-1)))|.
\end{aligned}$$

Since $d\varphi(x)/dx$ is bounded in absolute value by $\pi/n$ and $\varphi(x)$ itself is bounded in absolute value by 1, we may conclude that

$$ |\Phi(\sigma \circ (k-1\,k)) - \Phi(\sigma)| \leq \frac{\pi}{n}(2) = \frac{2\pi}{n}. \tag{16.8} $$

We recall the bound (13.28) from Theorem 13.28:

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{1}{2\log(1/\lambda)}\left[\log\left(\frac{(1-\lambda)\Phi(\sigma)^2}{2R}\right) + \log\left(\frac{1-\varepsilon}{\varepsilon}\right)\right], $$

where (16.8) shows that we can take $R = 4\pi^2/n^2$. Exercise 16.3 proves that $\Phi(\mathrm{id}) = n/2$. Therefore, evaluating the right-hand side yields

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{n^3\log n}{\pi^2} + [C_\varepsilon + o(1)]n^3 \tag{16.9} $$

(Here $C_\varepsilon$ can be taken to be $\log\left(\frac{1-\varepsilon}{64\pi^2\varepsilon}\right)$.)

**16.2. Shuffling Genes**

Although it is amusing to view permutations as arrangements of a deck of cards, they occur in many other contexts. For example, there are (rare) mutation events involving large-scale rearrangements of segments of DNA. Biologists can use the relative order of homologous genes to estimate the evolutionary distance between two organisms. **Durrett (2003)** has studied the mixing behavior of the random walk on $\mathcal{S}_n$ corresponding to one of these large-scale rearrangement mechanisms, *reversals*.

Fix $n > 0$. For $1 \leq i \leq j \leq n$, define the ***reversal*** $\rho_{i,j} \in \mathcal{S}_n$ to be the permutation that reverses the order of all elements in places $i$ through $j$. (The reversal $\rho_{i,i}$ is simply the identity.)

Since not all possible reversals are equally likely in the chromosomal context, we would like to be able to limit what reversals are allowed as steps in our random walks. One (simplistic) restrictive assumption is to require that the endpoints of the reversal are at distance at most $L$ from each other.

To avoid complications at the ends of segments, we will treat our sequences as circular arrangements. See Figure 16.2. With these assumptions, we define the $L$-reversal walk.

Let $L = L(n)$ be a function of $n$ satisfying $1 \leq L(n) \leq n$. The $L$-***reversal chain*** on $\mathcal{S}_n$ is the random walk on $\mathcal{S}_n$ whose increment distribution is uniform on the set of all reversals of (circular) segments of length at most $L$. (Note that this includes the $n$ segments of length 1; reversing a segment of length 1 results in the identity permutation.)

### PDF page 253 (book page 237)

Applying $\rho_{4,7}$:

| 9 | 4 | 2 | 5 | 1 | 8 | 6 | 3 | 7 | $\Rightarrow$ | 9 | 4 | 2 | 6 | 8 | 1 | 5 | 3 | 7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Applying $\rho_{9,3}$:

| 9 | 4 | 2 | 5 | 1 | 8 | 6 | 3 | 7 | $\Rightarrow$ | 4 | 9 | 7 | 5 | 1 | 8 | 6 | 3 | 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

FIGURE 16.2. Applying reversals to permutations of length 9. Note that the second reversal wraps around the ends of the permutation.

*[Figure: A circular (ring) arrangement of ten labeled nodes, read clockwise from the top: 4, 8, 3, 1, 2, 10, 7, 6, 5, 9. Adjacent nodes are joined by arcs around the ring; three of the edges — 5–6, 6–7, and 1–2 — are drawn in bold, marking the three conserved edges.]*

FIGURE 16.3. The permutation $1, 3, 8, 4, 9, 5, 6, 7, 10, 2$ has three conserved edges.

Equivalently, to perform a step in the $L$-reversal chain: choose $i \in [n]$ uniformly, and then choose $k \in [0, L-1]$ uniformly. Perform the reversal $\rho_{i,i+k}$ (which will wrap around the ends of the sequence when $i + k > n$). Note that the total probability assigned to id is $n/nL = 1/L$.

Since each reversal is its own inverse, Proposition 2.14 ensures that the $L$-reversal chain is reversible.

In Section 16.2.1 we give a lower bound on the mixing time of the $L$-reversal chain that is sharp in some cases. In Section 16.2.2, we will present an upper bound.

**16.2.1. Lower bound.** Although a single reversal can move many elements, it can break at most two adjacencies. We use the number of preserved adjacencies to lower bound the mixing time.

PROPOSITION 16.2. *Consider the family of $L$-reversal chains, where $L = L(n)$ satisfies $1 \leq L(n) < n/2$. For every $\varepsilon \in (0, 1)$, there exists $c_\varepsilon$ so that*

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{n\log n}{2} - c_\varepsilon n \quad \text{ as } n \to \infty . $$

Another lower bound is in Exercise 16.4: For $\varepsilon \in (0, 1)$, there exists $C_\varepsilon$ such that

$$ t_{\mathrm{mix}}(\varepsilon) \geq C_\varepsilon \frac{n^3}{L^3} . $$

PROOF. Say that the edge connecting $k$ and $k + 1$ is ***conserved*** if

$$ \sigma(k+1) - \sigma(k) = \pm 1 \mod n . $$

(See Figure 16.3.)

### PDF page 254 (book page 238)

Under the uniform distribution $\pi$ on $\mathcal{S}_n$, each cycle edge is conserved with probability $2/(n-1)$. Hence the expected number of conserved edges under $\pi$ is $2 + o(1)$.

Now consider running the $L$-reversal chain. Each reversal cuts two edges in the cycle and reverses the shorter arc between them. If the singleton $i$ is reversed, the configuration is unchanged, but the two edges adjacent to $i$ are considered cut. Call an edge ***undisturbed*** if it has not been cut by any reversal. Every undisturbed edge is conserved (and some disturbed edges may be conserved as well).

Start running the $L$-reversal chain from the identity permutation, and let $U(t)$ be the number of undisturbed edges at time

$$ t = t(n) = \frac{n}{2}\log n - c_\varepsilon n , $$

where $c_\varepsilon$ will be specisified [sic] later. We write $U(t) = U_1 + \cdots + U_n$, where $U_k = U_k(t)$ is the indicator of the edge $(k, k+1)$ being undisturbed after $t$ steps. Under the $L$-reversal model, each edge probability $2/n$ of being disturbed in each step, so

$$ \mathbf{E}[U(t)] = n\left(1 - \frac{2}{n}\right)^t \to e^{2c_\varepsilon} \quad \text{ as } n \to \infty $$

We can also use indicators to estimate the variance of $U(t)$. At each step of the chain, there are $nL$ reversals that can be chosen. Each edge is disturbed by exactly $2L$ legal reversals, since it can be either the right or the left endpoint of reversals of $L$ different lengths. If the edges are more than $L$ steps apart, no legal reversal breaks both. If they are closer than that, exactly one reversal breaks both. Hence, for $i \neq j$,

$$ \mathbf{P}\{U_i = 1 \text{ and } U_j = 1\} = \begin{cases} \left(\frac{nL - (4L-1)}{nL}\right)^t & \text{if } 1 \leq j - i \leq L \text{ or } 1 \leq i - j \leq L, \\ \left(\frac{nL - 4L}{nL}\right)^t & \text{otherwise} \end{cases} $$

(in this computation, the subscripts must be interpreted mod $n$). Observe that if $|i - j| > L$, then

$$ [(nL - 4L)/nL]^t = \left(1 - \frac{4}{n}\right)^t \leq \mathbf{P}\{U_i = 1\}\mathbf{P}\{U_j = 1\} , $$

so $\mathrm{Cov}(U_i, U_j) \leq 0$.

Write $p = \mathbf{P}(U_k = 1) = (1 - 2/n)^t = [1 + o(1)]e^{2c_\varepsilon}/n$. We can now estimate

$$\begin{aligned}
\mathrm{Var}(U(t)) &= \sum_{i=1}^{n}\mathrm{Var}U_i + \sum_{i \neq j}\mathrm{Cov}(U_i, U_j) \\
&\leq np(1-p) + 2nL\left(\left(1 - \frac{4 - 1/L}{n}\right)^t - p^2\right) .
\end{aligned}$$

By the mean value theorem, the second term is at most

$$ 2nL \cdot \frac{t}{nL}\left(1 - \frac{3}{n}\right)^{t-1} = n\log n \cdot O(n^{-3/2}) = o(1) . $$

We can conclude that

$$ \mathrm{Var}[U(t)] \leq [1 + o(1)]\mathbf{E}[U(t)]. \tag{16.10} $$

### PDF page 255 (book page 239)

*[Figure: a horizontal strip of cells representing positions. From left to right: a cell labeled $a$, then cells with a double-headed arrow labeled $L-1$ spanning to a cell $c_1$, another $L-1$ arrow to a cell $c_2$, then "..." , then a cell $c_{d-1}$, an $L-1$ arrow to a cell $c_d$, and an arrow labeled $r$ to a cell $b$ at the right.]*

FIGURE 16.4.    To express $(a\,b)$ in terms of short transpositions, first carry the marker at position $a$ over to position $b$; then perform all but the last transposition in reverse order to take the marker at position $b$ over to position $a$.

Let $A \subseteq \mathcal{S}_n$ be the set of permutations with at least $\mathbf{E}[U(t)]/2$ conserved edges. Under the uniform distribution $\pi$ on $\mathcal{S}_n$, the event $A$ has probability less than or equal to $5/\mathbf{E}[U(t)]$, by Markov's inequality.

By Chebyshev's inequality and $(16.10)$, for sufficiently large $n$ we have

$$ P^t(\mathrm{id}, A^c) \leq \mathbf{P}\{|U(t) - \mathbf{E}[U(t)]| > \mathbf{E}[U(t)]/2\} \leq \frac{\mathrm{Var}[U(t)]}{(\mathbf{E}[U(t)]/2)^2} < \frac{5}{\mathbf{E}[U(t)]}. $$

By the definition $(4.1)$ of total variation distance,

$$ \big\| P^t(\mathrm{id}, \cdot) - \pi \big\|_{\mathrm{TV}} \geq \left(1 - \frac{5}{\mathbf{E}[U(t)]}\right) - \frac{5}{\mathbf{E}[U(t)]} = 1 - \frac{10}{\mathbf{E}[U(t)]}. $$

Since $\mathbf{E}[U(t)] \to e^{2c_\varepsilon}$, the right-hand side is greater than $\varepsilon$ for large enough $c_\varepsilon$.    $\blacksquare$

**16.2.2. Upper bound.** We now give an upper bound on the mixing time of the $L$-reversal chain via the comparison method. To avoid problems with negative eigenvalues, we consider a lazy version of the $L$-reversal chain: at each step, with probability $1/2$, perform a uniformly chosen $L$-reversal, and with probability $1/2$, do nothing.

Again, our examplar chain for comparison will be the random transposition chain.

To bound the relaxation time of the $L$-reversal chain, we must expand each transposition $(a\,b) \in \mathcal{S}_n$ as a product of $L$-reversals. We can assume $b = a + k$ mod $n$ where $1 \leq k \leq n/2$. Call the transposition $(a\,b)$ **short** when $k < L$ and **long** otherwise. When $b = a + 1$, we have $(a\,b) = \rho_{a,b}$. When $a + 2 \leq b < a + L$, we have $(a\,b) = \rho_{a+1,b-1}\,\rho_{a,b}$. We use these paths of length 1 or 2 for all short transpositions. We will express our other paths below in terms of short transpositions; to complete the expansion, we replace each short transposition with two $L$-reversals.

*Paths for long transpositions, first method.* Let $(a\,b)$ be a long transposition. We build $(a\,b)$ by taking the marker at position $a$ on maximal length leaps for as long as we can, then finishing with a correctly-sized jump to get to position $b$; then take the marker that was at position $b$ over to position $a$ with maximal length leaps. More precisely, write

$$ b = a + d(L - 1) + r, $$

with $0 \leq r < L - 1$, and set $c_i = a + i(L - 1)$ for $1 \leq i \leq d$. Then

$$ (a\,b) = [(a\ c_1)(c_1\ c_2)\ldots(c_{d-1}\ c_d)]\,(b\ c_d)\,[(c_d\ c_{d-1})\ldots(c_2\ c_1)(c_1\ a)]. $$

See Figure 16.4.

### PDF page 256 (book page 240)

Consider the congestion ratio

$$ B = \max_{s \in S} \frac{1}{\mu(s)} \sum_{\tilde{s} \in \tilde{S}} \tilde{\mu}(\tilde{s}) N(s, \tilde{s})\,|\tilde{s}| \leq \max_{\rho_{i,j} \in S} 4Ln \sum_{\tilde{s} \in \tilde{S}} \frac{1}{n^2} N(s, \tilde{s}) \cdot O\left(\frac{n}{L}\right) $$

of Corollary $13.24$. Here $S$ and $\mu$ come from the $L$-reversal walk, while $\tilde{S}$ and $\tilde{\mu}$ come from the random transpositions walk. The inequality holds because the length of all generator paths is at most $O(n/L)$. Observe that $N(s, \tilde{s}) \leq 2$.

We must still bound the number of different paths in which a particular reversal might appear. This will clearly be maximized for the reversals of length $L-1$, which are used in both the "leaps" of length $L-1$ and the final positioning jumps. Given a reversal $\rho = \rho_{i,i+L-1}$, there are at most $(n/2)/(L-1)$ possible positions for the left endpoint $a$ of a long transposition whose path includes $\rho$. For each possible left endpoint, there are fewer than $n/2$ possible positions for the right endpoint $b$. The reversal $\rho$ is also used for short transpositions, but the number of those is only $O(1)$. Hence for this collection of paths we have

$$ B = O\left(\frac{n^2}{L}\right). $$

*Paths for long transpositions, second method.* We now use a similar strategy for moving markers long distances, but try to balance the usage of short transpositions of all available sizes. Write

$$ b = a + c\left(\frac{L(L - 1)}{2}\right) + r, $$

with $0 \leq r < L(L - 1)/2$.

To move the marker at position $a$ to position $b$, do the following $c$ times: apply the transpositions that move the marker by $L - 1$ positions, then by $L - 2$ positions, and so on, down to moving 1 position. To cover the last $r$ steps, apply transpositions of lengths $L - 1, L - 2, \ldots$ until the next in sequence hits exactly or would overshoot; if necessary, apply one more transposition to complete moving the marker to position $b$. Reverse all but the last transposition to move the marker from position $b$ to position $a$.

Estimating the congestion ratio works very similarly to the first method. The main difference arises in estimating the number of transpositions $(a\,b)$ whose paths use a particular reversal $\rho = \rho_{i,j}$. Now the left endpoint $a$ can fall at one of at most $2\left(\frac{n/2}{L(L-1)/2}\right)$ positions (the factor of 2 comes from the possibility that $\rho$ is the final jump), since there are at most this number of possible positions for a transposition of the same length as $\rho$ in one of our paths. The right endpoint $b$ again has at most $n/2$ possible values. We get

$$ B = O\left(\frac{n^2}{L^2}\right). \tag{16.11} $$

That is, we have asymptotically reduced the congestion ratio by a factor of $L$ by changing the paths to use reversals of all sizes evenly.

By Corollary $13.24$ and the laziness of the $L$-reversal chain, we have

$$ t_{\mathrm{rel}} = O\left(\frac{n^3 \log n}{L^2}\right) $$

### PDF page 257 (book page 241)

for the $L$-reversal chain. By Theorem $12.4$,

$$ t_{\mathrm{mix}} \leq \left(\frac{1}{2}\log n! + \log 2\right) \cdot t_{\mathrm{rel}} = O\left(\frac{n^4 \log^2 n}{L^2}\right). $$

**Exercise**

EXERCISE 16.1. Modify the argument of Proposition $16.2$ to cover the case $n/2 < L < n - 1$. (Hint: there are now pairs of edges both of which can be broken by two different allowed reversals.)

EXERCISE 16.2. Let $\varphi : [n] \to \mathbb{R}$ be any function. Let $\sigma \in \mathcal{S}_n$. Show that the value of

$$ \varphi_\sigma = \sum_{k \in [n]} \varphi(k)\varphi(\sigma(k)) $$

is maximized when $\sigma = \mathrm{id}$.

EXERCISE 16.3. Show that for any positive integer $n$,

$$ \sum_{k \in [n]} \cos^2\left(\frac{(2k - 1)\pi}{2n}\right) = \frac{n}{2}. $$

EXERCISE 16.4. Show that for the $L$-reversal chain, there is a constant $C_\varepsilon$ such that

$$ t_{\mathrm{mix}}(\varepsilon) \geq C_\varepsilon \frac{n^3}{L^3}. $$

*Hint:* Follow a single label.

**Notes**

The coupling upper bound for random adjacent transpositions is described in **Aldous (1983b)** and also discussed in **Wilson (2004a)**. **Diaconis and Shahshahani (1981)** derived very precise information on the spectrum and convergence behavior of the random transpositions walk; **Diaconis and Saloff-Coste (1993b)** use these results to obtain an $O(n^3 \log n)$ upper bound on the mixing time of the random adjacent transpositions chain.

**Diaconis and Saloff-Coste (1993b)** proved the $\Omega(n^3)$ lower bound we present for this chain and conjectured that the mixing time is of order $n^3 \log n$. **Wilson (2004a)** showed that $(1/\pi^2 - o(1))n^3 \log n \leq t_{\mathrm{mix}}(\varepsilon) \leq (2/\pi^2 + o(1))n^3 \log n$ for all $\varepsilon \in (0, 1)$. **Lacoin (2016a)** proved that in fact there is a cutoff and $t_{\mathrm{mix}}(\varepsilon) = [1 + o(1)](1/\pi^2)n^3 \log n$.

**Durrett (2003)** introduced the $L$-reversal chain and proved both bounds we present. For the upper bound, our presentation has again significantly weakened the result by considering only the spectral gap; Durrett proved an upper bound of order $O\left(\frac{n^3 \log n}{L^2}\right)$.

**Durrett (2003)** also used Wilson's method to give another lower bound, of order $\Omega\left(\frac{n^3 \log n}{L^3}\right)$, when $L \sim n^\alpha$ for some $0 < \alpha < 1$. Taking the maximum of the two lower bounds for $L$ in this range tells us that the mixing of the $L$-reversal chain takes at least $\Omega(n^{1 \vee (3 - 3\alpha)} \log n)$ steps—see Figure $16.5$. Durrett conjectured that this lower bound is, in fact, sharp.

### PDF page 258 (book page 242)

*[Figure: a plot on axes. The horizontal axis is marked at $1/3$, $2/3$, and $1$; the vertical axis is marked at $1$, $2$, $3$. A line starts at height $3$ above the origin, decreases linearly to height $1$ at horizontal position $2/3$, then stays flat at height $1$ out to $1$.]*

FIGURE 16.5.   When $L = n^\alpha$ and $0 < \alpha < 1$, the mixing of the $L$-reversal chain takes at least $\Omega(n^{1\vee(3-3\alpha)} \log n)$ steps. This plot shows $1 \vee (3 - 3\alpha)$.

**Cancrini, Caputo, and Martinelli (2006)** showed that the relaxation time of the $L$-reversal chain is $\Theta(n^{1\vee(3-3\alpha)})$. **Morris (2009)** has proved an upper bound on the mixing time that is only $O(\log^2 n)$ larger than Durrett's conjecture.

**Kandel, Matias, Unger, and Winkler (1996)** discuss shuffles relevant to a different problem in genomic sequence analysis.

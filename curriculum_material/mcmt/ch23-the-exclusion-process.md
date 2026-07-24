# Chapter 23 — The Exclusion Process
*(PDF pages 339–350; book pages 323–334)*

### PDF page 339 (book page 323)

CHAPTER 23

# The Exclusion Process

**23.1. Introduction**

**23.1.1. Interchange Process.** Given a graph $G = (V, E)$ with $|V| = n$, consider the state space consisting of assignments of the labels $\{1, 2, \ldots, n\}$ to vertices in $V$, with no two vertices receiving the same label. Formally, define the state space $\mathcal{X}$ to be the subset of $\{1, 2, \ldots, n\}^V$ equal to the bijections. The ***interchange process*** evolves as follows: at each unit of time, an edge is selected uniformly at random. With probability $1/2$, the labels at its endpoints are exchanged, and with probability $1/2$, the configuration is unchanged. That is, when in configuration $\sigma$ and edge $e = \{v, w\}$ is selected, with probability $1/2$ the process remains at $\sigma$ and with probability $1/2$ it moves to $\sigma'$, where

$$ \sigma'(u) = \begin{cases} \sigma(u) & u \notin \{v, w\} \\ \sigma(w) & u = v \\ \sigma(v) & u = w \end{cases} . $$

The interchange process on the $n$-path is identical to the random adjacent transposition chain, studied in Section 16.1.

Let $v = \sigma^{-1}(j)$ be the position of label $j$ in the configuration $\sigma$. The chance that label $j$ moves equals $\deg(v)/2|E|$, in which case it moves to a neighbor chosen uniformly at random. Thus, if the graph is regular with degree $d$, then each label is performing a simple random walk with holding probability $1 - \frac{d}{2|E|}$.

Often the interchange process is studied in continuous time. Continuizing the discrete-time chain just described is equivalent to the following: Place independent Poisson clocks, each run at rate $1/2|E|$, on each edge. When a clock "rings", the labels on its endpoints are exchanged. It is, however, conventional in the literature to run the $|E|$ independent edge clocks all at *unit* rate, in which case the process as a whole makes transitions at rate $|E|$. If the graph is $d$-regular, then each label performs a simple random walk at rate $d$.

**23.1.2. Exclusion Process.** Suppose that $k$ indistinguishable particles are placed on the vertices of the graph $G$. The $k$-***exclusion process*** evolves as follows: First, an edge is selected uniformly at random. If both of its endpoints are occupied by particles or both are unoccupied, then the configuration is unchanged. If there is exactly one particle among the two endpoints, then with probability $1/2$ the particle is placed on the right, and with probability $1/2$ it is placed on the left.

The $k$-exclusion process is a projection of the interchange process. Instead of tracking the position of all $n$ labels, only the positions of the first $k$ are observed, and these labels are not distinguished from each other. Formally, the function

### PDF page 340 (book page 324)

$T_k : \mathcal{X} \to \{0, 1\}^V$ given by

$$ T_k(\sigma)(v) = \mathbf{1}_{\{\sigma(v) \in \{1, 2, \ldots, k\}\}} $$

projects from the state space of the interchange process to $\{0, 1\}^V$. If $\{\sigma_t\}$ is the interchange process, then $X_t^{(k)} = T_k(\sigma_t)$ is the $k$-exclusion process.

As for the interchange process, a common parameterization of the continuous-time exclusion process places a unit rate clock on each edge, and swaps the labels of the endpoints of an edge when its clock rings. Note this is $2|E|$ faster than the continuization of the discrete-time process just described. The overall rate at which some clock on an edge containing vertex $v$ rings is $\deg(v)$, and given a ring occurs among these edges, it is equally likely to be at any of them. So a particle at vertex $v$ moves at rate $\deg(v)$; when it moves, it picks a neighbor uniformly and attempts a move, censoring any move to an occupied site. In a $d$-regular graph, one could equivalently place a (rate $d$) clock on each *particle*, and make equiprobable nearest-neighbor moves (censored if to an occupied site) at each ring. The name "exclusion" derives from this description. Still equivalently, one could run a single rate $dk$ clock and, at ring times, select a particle at random and make a censored nearest-neighbor move of the chosen particle.

We consider now the case where $G$ is the interval $\{1, 2, \ldots, n\}$. There is a bijection between the state space $\mathcal{X} = \{x \in \{0, 1\}^n : \sum_{i=1}^n x(i) = k\}$ of the $k$-exclusion process on $G$ and paths $f : \{0, 1, \ldots, n\} \to \mathbb{Z}$ with

$$ f(0) = 0 \quad f(j) = f(j - 1) \pm 1 \text{ for } j = 1, \ldots, n, \quad \text{and } f(n) = 2k - n . $$

A particle at site $j$ corresponds to a unit increase from $j - 1$ to $j$, while a "hole" (unoccupied site) at $j$ corresponds to a unit decrease. See Figure 23.2. Formally, given $x \in \mathcal{X}$, the corresponding path $f$ is

$$ f(j) = f(j - 1) + (-1)^{x(j)+1}, \quad j = 1, \ldots, n . $$

The dynamics for the exclusion process induce dynamics for the path-valued representation. Since edges in the graph correspond to nodes of the path, we select each interior node of the path with probability $1/(n-1)$. Edges with two occupied or unoccupied vertices correspond to locally monotone nodes of the path (increasing for occupied edges and decreasing for unoccupied edges), a particle followed by a hole corresponds to a local maximum, and a hole followed by a particle corresponds to a local minimum. If a monotone node is selected, nothing changes, while if a local extremum is selected, it is "refreshed": with probability $1/2$ a local maximum is imposed, and with probability $1/2$ a local minimum is imposed. See Figures 23.1 and 23.2. In Figure 23.2, the edge $\{2, 3\}$ is updated. The particle at 2 moves to 3, corresponding to inverting the third node of the path.

We have already seen that a configuration $\sigma$ in the interchange process yields a configuration $T_k(\sigma)$ in the $k$-exclusion process, for all $k$. Conversely, given exclusion configurations $T_1(\sigma), \ldots, T_n(\sigma)$, we can reconstruct $\sigma$ by noting that the position $\sigma^{-1}(j)$ of the $j$-th label is the unique coordinate where $T_j(\sigma)$ and $T_{j-1}(\sigma)$ differ. The correspondence between an interchange configuration and its projections to all $n + 1$ exclusion processes is shown in Figure 23.3.

### PDF page 341 (book page 325)

**FIGURE 23.1.** The possible transitions from a given configuration. *[Figure: At top, a lattice path over the interval marked 0–6, with peaks/valleys: rising from 0 to a peak at 2, down to 4, up to 5, down to 6. Three dotted arrows point downward-left, down, and downward-right to three possible successor paths below. Left path: local extremum refreshed near node 2 (dashed segment showing a valley/minimum imposed). Middle path: extremum refreshed near node 4 (dashed segment). Right path: extremum refreshed near node 5 (dashed diamond shape between 4, 5, 6). Each of the three lower paths is drawn over the same 0–6 interval.]*

**FIGURE 23.2.** The correspondence between particle representation and path representation for neighboring configurations $x, y$. Node 2 of the path is updated in configuration $x$ to obtain $y$. This corresponds to exchanging the particle at vertex 2 with the hole at vertex 3. *[Figure: Top: particle configuration $x$ shown as a row of dots — filled (particles) and open (holes) circles: ●●○●○○○● labeled $x$. Below it a double-headed vertical arrow to a lattice path over interval 0–8 rising to peaks at 2 and 4, then descending with dashed segments to a minimum near 7 and back up to 8. A large bracket/brace on the left with a downward arrow connects the top diagram to the bottom one. Bottom: particle configuration $y$: ●○●●○○○● labeled $y$, with a double-headed arrow to its corresponding lattice path over 0–8, with a peak at 1, a larger peak at 4, dashed descending segments to a minimum near 7 and up to 8. The two paths differ by inverting node 2/3.]*

**23.1.3. Monotonicity.** We discuss here the interchange process on the $n$-path. Consider the following ordering on the interchange process: We declare

### PDF page 342 (book page 326)

*[Figure: At the top, a table showing the correspondence between an interchange configuration and its exclusion projections. Column labels: 1 4 3 5 2, then $\sigma$, then "interchange". The rows are labeled $k=0$ through $k=5$; each row is a sequence of five circles (open ○ or filled ●) representing the exclusion configuration at level $k$. Row $k=0$: ○ ○ ○ ○ ○; $k=1$: ● ○ ○ ○ ○; $k=2$: ● ○ ○ ○ ●; $k=3$: ● ○ ● ○ ●; $k=4$: ● ● ● ○ ●; $k=5$: ● ● ● ● ●. A large brace on the right groups the rows under the label "exclusion". Below the table is a path/lattice diagram showing the six exclusion path representations stacked, with the levels labeled $k=5$, $k=4$, $k=3$, $k=2$, $k=1$, $k=0$ from top to bottom.]*

**FIGURE 23.3.** Correspondence between interchange configuration on $\{1,2,3,4,5\}$ and all 6 of its projections to exclusion configurations.

$\sigma \preceq \eta$ if

$$ |\sigma^{-1}\{1,2,\ldots,k\} \cap \{1,\ldots,\ell\}| \leq |\eta^{-1}\{1,2,\ldots,k\} \cap \{1,\ldots,\ell\}| $$
$$ \text{for all } k = 1,\ldots,n \ \text{ and } \ell = 1,\ldots,n\,. \tag{23.1} $$

The configurations $\sigma$ and $\eta$ satisfy $\sigma \preceq \eta$ if and only if for all $k$, the path representation of the projection onto the $k$-exclusion process, $x^{(k)} = T_k(\sigma)$, lies below or at the same height as the path representation of the projection $y^{(k)} = T_k(\eta)$. See Figure 23.4 for an illustration.

The interchange process is monotone: Let $\sigma \preceq \eta$. We couple together all the $k$-exclusion processes, using their path representation. We select for all the exclusion processes in both $\eta$ and $\sigma$ the same node. Toss a fair coin. If the node is not a local extremum, we do nothing. If the coin is "heads", we replace the node with a local maximum. If "tails", we replace with a local minimum. Since all the exclusion paths of $\sigma$ are below those of $\eta$ before updating, in all cases this ordering is preserved after updating.

In the interchange process, the probability that label $j$ moves is $1/(n-1)$ when at an interior node, in which case it moves to each neighbor with equal probability. When at an endpoint, the chance it moves to the interior node is $1/2(n-1)$, otherwise it remains in place. Thus, the $j$-th label is performing a delayed simple random walk on $\{1,2\ldots,n\}$ with self loops at 1 and $n$. The delay probability equals $1 - 1/(n-1)$.

### PDF page 343 (book page 327)

*[Figure: Two path/lattice diagrams side by side, separated by the symbol $\preceq$. The left diagram has column labels 4 2 3 1 and a label 3 at the bottom; the right diagram has column labels 4 2 1 3 and a label 3 at the bottom. Each diagram shows path representations at levels labeled $k=4$, $k=3$, $k=2$, $k=1$, $k=0$ from top to bottom. Each path of the left permutation lies below the corresponding path of the right permutation.]*

**FIGURE 23.4.** Each path of the permutation on the left lies below the corresponding path of the permutation on the right. If an update at node 3 is performed, the left configuration is left unchanged, while the configuration on the right is updated to the one on the left.

**PROPOSITION 23.1.** *Let $G_n$ denote the $n$-path with loops at 1 and $n$. Let $t_{\mathrm{rel}}$ be the relaxation time for the interchange process on the $n$-path, and let $t_{\mathrm{rel}}(\mathrm{single})$ be the relaxation time for the random walk on $G_n$ with delay probability $1 - (n-1)^{-1}$. Then*

$$ t_{\mathrm{rel}} = t_{\mathrm{rel}}(\mathrm{single})\,. $$

**PROOF.** Let $\varphi(j) = \cos(\pi(2j-1)/2n)$ for $j = 1,2,\ldots,n$ be the second eigenfunction for the simple random walk on $G_n$, with eigenvalue $\lambda_2 = \cos(\pi/n)$. (See (12.21).) If $\sigma_1$ is the permutation after one step of the interchange process started from $\sigma$, then since $\sigma_1^{-1}(j)$ is obtained from $\sigma^{-1}(j)$ by one step of a delayed random walk, we obtain

$$ \mathbf{E}_\sigma[\varphi(\sigma_1^{-1}(j))] = \left[ \frac{1}{n-1}(\lambda_2 - 1) + 1 \right] \varphi(\sigma^{-1}(j))\,. \tag{23.2} $$

That is, for each $j = 1,\ldots,n$, the function $\psi_j(\sigma) = \varphi(\sigma^{-1}(j))$ is an eigenfunction for the interchange process on the $n$-path, with eigenvalue equal to the eigenvalue for the random walk on $G_n$ with delay probability $1 - 1/(n-1)$. In particular, any linear combination of the $\psi_j$'s is also an eigenfunction with the same eigenvalue.

We now show that

$$ \Psi(\sigma) = \sum_{j=1}^{n} \varphi(j)\psi_j(\sigma) $$

is a strictly increasing eigenfunction. By Exercise 23.2, it is enough to show that $\Psi(\sigma) < \Psi(\eta)$ when $\sigma \preceq \eta$ and $\eta$ is obtained from $\sigma$ by a single adjacent transposition.

Suppose in particular that $\eta$ and $\sigma$ differ at $a$ and $a+1$. The labels at $a$ and $a+1$ are in decreasing order in $\sigma$ and increasing order in $\eta$. Denote these two labels by $j < k$. Thus $\sigma(a) = k = \eta(a+1)$ and $\sigma(a+1) = j = \eta(a)$. Since $\varphi$ is itself a strictly decreasing function, we have

$$ [\varphi(k) - \varphi(j)][\varphi(a) - \varphi(a+1)] < 0\,. $$

### PDF page 344 (book page 328)

Rearranging shows that

$$ \varphi(k)\varphi(a) + \varphi(j)\varphi(a+1) < \varphi(j)\varphi(a) + \varphi(k)\varphi(a+1)\,, $$

and this implies that $\Psi(\sigma) < \Psi(\eta)$.

By Lemma 22.18, $\Psi$ must be an eigenfunction corresponding to the second largest eigenvalue. Consequently, the relaxation times for the single particle and for the entire process must be the same. $\blacksquare$

**23.2. Mixing Time of $k$-exclusion on the $n$-path**

**PROPOSITION 23.2.** *For the discrete-time $k$-exclusion process on the $n$-path $\{1,\ldots,n\}$, for $\varepsilon \in (0,1)$, uniformly over $k \leq n/2$,*

$$ [1 + o(1)]\frac{n^3}{\pi^2}\left[ \log k - c_1 + \log\left(\frac{1-\varepsilon}{\varepsilon}\right) \right] \leq t_{\mathrm{mix}}(\varepsilon) \leq n^3\lceil \log_2(k/\varepsilon) \rceil\,, $$

*where $c_1$ is a universal constant.*

**PROOF.** For the lower bound, we apply Wilson's method (Theorem 13.28).

As discussed in the proof of Proposition 23.1, if $\varphi(j) = \cos(\pi(2j-1)/2n)$ for $j = 1,2,\ldots,n$ is the second eigenfunction for the simple random walk on $G_n$, with eigenvalue $\lambda_2 = \cos(\pi/n)$, then for each $j = 1,\ldots,n$, the function $\psi_j(\sigma) = \varphi(\sigma^{-1}(j))$ is an eigenfunction for the interchange process, with eigenvalue

$$ \lambda = 1 - \frac{1}{n-1}(1 - \lambda_2)\,. \tag{23.3} $$

The function $\tilde{\Phi}(\sigma) = \sum_{j=1}^{k} \psi_j(\sigma)$ is thus an eigenfunction for the interchange process, also with eigenvalue $\lambda$. By Lemma 12.9, the function $\Phi(x) = \sum_{i=1}^{n} \varphi(i)x(i)$ is an eigenfunction for the $k$-exclusion process with the same eigenvalue $\lambda$.

Since

$$ \lambda_2 = \cos(\pi/n) = 1 - \pi^2/2n^2 + O(n^{-4})\,, $$

it follows that

$$ 1 - \lambda = \frac{\pi^2}{2n^2(n-1)} + O(n^{-5})\,. $$

We have $|\Phi(X_1) - \Phi(x)| \leq \pi/n$, since the derivative of $u \mapsto \cos(\pi u/2n)$ is bounded by $\pi/2n$. Together with the inequality $\mathbf{P}_x\{X_1 \neq x\} \leq k/(n-1)$, this implies

$$ \mathbf{E}_x[(\Phi(X_1) - \Phi(x))^2] \leq R = \frac{\pi^2 k}{n^2(n-1)}\,. $$

Since by assumption $k \leq n/2$, the configuration $x(j) = \mathbf{1}\{j \leq k\}$ satisfies

$$ \Phi(x) \geq \sum_{j \leq 2k/3} \cos(\pi(2j-1)/2n) \geq \cos(2\pi/3)\lfloor \frac{2k}{3} \rfloor = \frac{1}{2}\lfloor \frac{k}{3} \rfloor\,. $$

Applying Theorem 13.28 shows that there is some universal constant $c_1$ such that

$$ t_{\mathrm{mix}}(\varepsilon) \geq [1 + o(1)]\frac{n^3}{\pi^2}\left[ \log k - c_1 + \log\left(\frac{1-\varepsilon}{\varepsilon}\right) \right]\,. $$

For the upper bound, recall that random adjacent transpositions is the interchange process on the $n$-path. In the coupling discussed in Section 16.1.2, if $\tau_a$ is the time for a single card (label) to couple, then

$$ \mathbf{P}\{\tau_a > n^3\} \leq \frac{1}{2}\,. $$

### PDF page 345 (book page 329)

Taking blocks of size $\lceil \log_2(k/\varepsilon) \rceil$ shows that

$$ \mathbf{P}\{\tau_a > n^3 \lceil \log_2(k/\varepsilon) \rceil\} \le \frac{\varepsilon}{k} \,. $$

Summing this over $a = 1, \dots, k$ shows that the time $\tau$ for the first $k$ cards to couple satisfies the bound

$$ \mathbf{P}\{\tau > n^3 \lceil \log_2(k/\varepsilon) \rceil\} \le \varepsilon. $$

For the projection of random adjacent transpositions in which only the first $k$ labels are tracked, this yields

$$ t_{\mathrm{mix}}(\varepsilon) \le n^3 \lceil \log_2(k/\varepsilon) \rceil \,. $$

Since this process projects further to the $k$-exclusion process, this bound holds for the latter process as well. $\blacksquare$

REMARK 23.3. The lower bound is not informative when $k$ is a small constant. In that case, an order $n^3$ lower bound follows from comparison with delayed simple random walk on $G_n$.

**23.3. Biased Exclusion**

The *biased exclusion process* is the following chain on

$$ \mathcal{X} = \{x \in \{0,1\}^{2n} \,:\, \sum_{i=1}^{2n} x(i) = n\} \,, $$

where we now assume there are $2n$ sites and $n$ particles. At each unit of time, one among the $2n - 1$ internal edges is chosen. If both endpoints of the edge are unoccupied or both occupied, then leave the configuration unchanged. If there is exactly one particle among the two endpoints, then with probability $q = 1 - p$, place the particle on the left and with probability $p$, place the particle on the right. Thus, the probability that a particle is moved to an unoccupied site immediately to its right equals $\frac{p}{2n-1}$, and the probability that a particle is moved to an unoccupied site immediately to its left is $\frac{1-p}{2n-1}$.

We consider configurations $x$ and $y$ to be adjacent if $y$ can be obtained from $x$ by taking a particle and moving it to an adjacent unoccupied site. In the path representation, moving a particle to the right corresponds to changing a local maximum (i.e., an "up-down") to a local minimum (i.e., a "down-up"). Moving a particle to the left changes a local minimum to a local maximum.

Using the path description of $\mathcal{X}$, a node $v \in \{1, 2, \dots, 2n - 1\}$ is chosen uniformly at random. If $v$ is adjacent to two "up" edges or two "down" edges, then the configuration is unchanged. Otherwise, the node $v$ is refreshed to be a local maximum with probability $1 - p$ and a local minimum with probability $p$, irrespective of its current state. See Figure 23.2.

THEOREM 23.4. *Consider the biased exclusion process with bias $\beta = \beta_n = 2p_n - 1 > 0$ on the segment of length $2n$ and with $n$ particles.*

(i) *If $1 \le n\beta \le 7\log n$, then for a universal constant $c_1$,*

$$ t_{\mathrm{mix}} \le c_1 \frac{n \log n}{\beta^2} \,. $$

### PDF page 346 (book page 330)

*[Figure: Two path-representation diagrams over sites $0$ through $6$. Left panel: a tent-shaped path rising to a peak; near the top an "up-down" configuration labeled $x$ (open circle marks the removed/added midpoint) and a dashed diamond below marked $y$; a vertical bracket to the right labels $h = 2$. Right panel: an inverted (valley-shaped) path over sites $0$ through $6$ dipping to a trough; a dashed diamond configuration marked $x$ with open circle and $y$ below at the bottom; a vertical bracket to the right labels $h = \text{-}2$.]*

FIGURE 23.5. Neighboring configurations $x$ and $y$.

(ii) *For any fixed constant $\beta^\star < 1$, if $n\beta > 7\log n$ and $\beta < \beta^\star$, then*

$$ t_{\mathrm{mix}} \asymp \frac{n^2}{\beta} \,. $$

*(The notation $a_n \asymp b_n$ means that there are constants $c_2, c_3$, depending only on $\beta^\star$, such that $c_2 \le \frac{a_n}{b_n} \le c_3$.)*

REMARK 23.5. The statement above does not specify what happens when $n\beta < 1$, or give a lower bound in the case $1 < n\beta \le 7\log n$. The complete picture is given in the Notes.

PROOF. *Upper bound.*

For $\alpha > 1$, define the distance between two configurations $x$ and $y$ which differ by a single transition to be

$$ \ell(x,y) = \alpha^{n+h}, $$

where $h$ is the height of the midpoint of the diamond that is removed or added. (See Figure 23.5.) Note that $\alpha > 1$ and $h \ge -n$ guarantee that $\ell(x,y) \ge 1$, so we can use Theorem 14.6. We again let $\rho$ denote the path metric on $\mathcal{X}$ corresponding to $\ell$, as defined in (14.5).

We couple from a pair of initial configurations $x$ and $y$ which differ at a single node $v$ as follows: choose the same node in both configurations, and propose a local maximum with probability $1 - p$ and a local minimum with probability $p$. For both

### PDF page 347 (book page 331)

$x$ and $y$, if the current node $v$ is a local extremum, refresh it with the proposed extremum; otherwise, remain at the current state.

Let $(X_1, Y_1)$ be the state after one step of this coupling. There are several cases to consider.

The first case is shown in the left panel of Figure 23.5. Let $x$ be the upper configuration, and $y$ the lower. Here the edge between $v - 2$ and $v - 1$ is "up", while the edge between $v + 1$ and $v + 2$ is "down", in both $x$ and $y$. If $v$ is selected, the distance decreases by $\alpha^{n+h}$. If either $v - 1$ or $v + 1$ is selected, and a local minimum is selected, then the lower configuration $y$ is changed, while the upper configuration $x$ remains unchanged. Thus the distance increases by $\alpha^{n+h-1}$ in that case. We conclude that

$$ \mathbf{E}_{x,y}[\rho(X_1, Y_1)] - \rho(x, y) = -\frac{1}{2n-1}\alpha^{h+n} + \frac{2}{2n-1}p\alpha^{h+n-1} $$

$$ = \frac{\alpha^{h+n}}{2n-1}\left(\frac{2p}{\alpha} - 1\right) \,. \tag{23.4} $$

In the case where $x$ and $y$ at $v - 2, v - 1, v, v + 1, v + 2$ are as in the right panel of Figure 23.5, we obtain

$$ \mathbf{E}_{x,y}[\rho(X_1, Y_1)] - \rho(x, y) = -\frac{1}{2n-1}\alpha^{h+n} + \frac{2}{2n-1}(1-p)\alpha^{h+n+1} $$

$$ = \frac{\alpha^{h+n}}{2n-1}\left(2\alpha(1-p) - 1\right) \,. \tag{23.5} $$

(We create an additional disagreement at height $h + 1$ if either $v - 1$ or $v + 1$ is selected and a local maximum is proposed; the top configuration can accept the proposal, while the bottom one rejects it.) To obtain as large a uniform contraction as possible, we set the right-hand sides of (23.4) and (23.5) equal to one another and solve for $\alpha$. This yields

$$ \alpha = \sqrt{\frac{p}{q}} = \sqrt{\frac{1 + \beta}{1 - \beta}}, $$

for $\beta = p - q$. Since $p > 1/2$, the value

$$ \theta := 1 - 2\sqrt{pq} $$

satisfies $\theta > 0$, and both (23.4) and (23.5) reduce to

$$ \mathbf{E}_{x,y}[\rho(X_1, Y_1)] - \rho(x, y) = -\frac{\alpha^{h+n}}{2n-1}\theta \,. \tag{23.6} $$

Now consider the case on the left of Figure 23.6. We have

$$ \mathbf{E}_{x,y}[\rho(X_1, Y_1)] - \rho(x, y) = -\frac{1}{2n-1}\alpha^{h+n} + \frac{1}{2n-1}q\alpha^{h+n+1} + \frac{1}{2n-1}p\alpha^{h+n-1} $$

$$ = \frac{\alpha^{h+n}}{2n-1}\left(q\alpha + \frac{p}{\alpha} - 1\right) $$

$$ = -\frac{\alpha^{h+n}}{2n-1}\theta \,, $$

which gives again the same expected decrease as (23.6). (In this case, a local max proposed at $v - 1$ will be accepted only by the top configuration, and a local min proposed at $v + 1$ will be accepted only by the bottom configuration.) The case on the right of Figure 23.6 is the same.

### PDF page 348 (book page 332)

**FIGURE 23.6.** More neighboring configurations.
*[Figure: two side-by-side "mountain range" height-function diagrams over the integer sites 0 through 8. In each, a piecewise-linear path of up/down unit edges (with dots marking lattice points along it) has a small dashed diamond marking a local move: a peak labeled $x$ that can be flipped to a valley labeled $y$. In the left diagram the move is near sites 4–6; in the right diagram near sites 2–4.]*

Thus, (23.6) holds in all cases. That is, since $\rho(x,y) = \ell(x,y) = \alpha^{h+n}$,
$$ \mathbf{E}_{x,y}[\rho(X_1, Y_1)] = \rho(x,y)\left(1 - \frac{\theta}{2n-1}\right) \le \rho(x,y)e^{-\frac{\theta}{2n-1}} \, . $$

The diameter of the state space is the distance from the configuration with $n$ "up" edges followed by $n$ "down" edges to its reflection across the horizontal axis, which equals
$$ \alpha^n \sum_{k=1}^{n} k\alpha^{n-k} + \alpha^n \sum_{k=1}^{n-1}(n-k)\alpha^{-k} = \alpha\left(\frac{\alpha^n - 1}{\alpha - 1}\right)^2 \, . $$

Since $\theta \ge \beta^2/2$, Corollary 14.8 yields
$$ t_{\mathrm{mix}}(\varepsilon) \le \frac{4n}{\beta^2}\left[\log(1/\varepsilon) + \log\left[\alpha\left(\frac{\alpha^n - 1}{\alpha - 1}\right)^2\right]\right] \, . $$

Note that $\alpha = 1 + \beta + O(\beta^2)$ for $\beta \le \beta^\star$, so
$$ t_{\mathrm{mix}}(\varepsilon) \le \frac{4n}{\beta^2}\left[\log(\varepsilon^{-1}) + (2n+1)[\beta + O(\beta^2)] - 2\log\beta + O(\beta)\right] \, . \tag{23.7} $$

The right-hand side is $O\left(\frac{n \log n}{\beta^2}\right)$ for $1 \le n\beta \le 7 \log n$.

For $(7 \log n)/n \le \beta \le \beta^\star$, the right-hand side of (23.7) is $O(n^2/\beta)$.

If $\beta = \frac{1}{n}$, then $t_{\mathrm{mix}}(\varepsilon) = O(n^3 \log n)$, which is the same order as the mixing time in the symmetric case.

*Lower Bound.* We use the particle description here. The stationary distribution is given by
$$ \pi(x) = \frac{1}{Z}\prod_{i=1}^{n}\left(\frac{p}{q}\right)^{k_i(x)} = \frac{1}{Z}(p/q)^{\sum_{i=1}^{n} k_i(x)}, $$

where $(k_1(x), \ldots, k_n(x))$ are the locations of the $n$ particles in the configuration $x$, and $Z$ is a normalizing constant. We will check detailed balance: if $x'$ is obtained from $x$ by moving a particle from $j$ to $j+1$, then
$$ \frac{\pi(x)P(x,x')}{\pi(x')P(x',x)} = \frac{1}{(p/q)}\frac{\frac{1}{2n-1}p}{\frac{1}{2n-1}q} = 1 \, . $$

Let $L(x)$ be the location of the left-most particle of the configuration $x$, and let $R(x)$ be the location of the right-most unoccupied site of the configuration $x$.

### PDF page 349 (book page 333)

Let
$$ \mathcal{X}_{\ell,r} = \{x \, : \, L(x) = \ell, \; R(x) = r\} \, , $$
and consider the transformation $T : \mathcal{X}_{\ell,r} \to \mathcal{X}$ which takes the particle at $\ell$ and moves it to $r$. Note that $T$ is one-to-one on $\mathcal{X}_{\ell,r}$.

We have
$$ \pi(\mathcal{X}_{\ell,r})\left(\frac{p}{q}\right)^{r-\ell} \le \sum_{x \in \mathcal{X}_{\ell,r}} \pi(T(x)) \le 1 \, , $$
so
$$ \pi(\mathcal{X}_{\ell,r}) \le \alpha^{-2(r-\ell)} \, . $$
Fix $2/7 < b < 1/3$, and let $G = \{x \, : \, L(x) \le (1-b)n\}$. We have
$$ \pi(G) \le \sum_{\ell \le (1-b)n, \; r \ge n} \pi(\mathcal{X}_{\ell,r}) \le n^2 \alpha^{-bn} \, . $$

Since $\beta n \ge 7 \log n$, we have
$$ n^2 \alpha^{-bn} \le n^2 e^{-\beta bn} \le n^{2-7b} \to 0 \, . $$

We consider now starting from a configuration $x_0$ with $L(x_0) = bn$.

The trajectory of the left-most particle, $(L_t)$, can be coupled with a delayed biased nearest-neighbor walk $(S_t)$ on $\mathbb{Z}$, with $S_0 = bn$ and such that $L_t \le S_t$, as long as $S_t > 1$: If $L_t < S_t$, then we can couple so that only one moves in the next step. If $L_t = S_t$, then move the particles together when possible. The holding probability for $(S_t)$ equals $1 - \frac{1}{2n-1}$. By the gambler's ruin, the chance that $(S_t)$ ever reaches 1 is bounded above by $(q/p)^{bn-1}$. Therefore,
$$ \mathbf{P}_{x_0}\{L_t > (1-b)n\} \le (q/p)^{bn-1} + \mathbf{P}_{bn}\{S_t > (1-b)n\} \, . \tag{23.8} $$

By Chebyshev's Inequality (recalling $S_0 = bn$),
$$ \mathbf{P}_{bn}\{|S_t - bn - \beta t/(2n-1)| > M\} \le \frac{\mathrm{Var}(S_t)}{M^2} \le \frac{t}{M^2(2n-1)} \, . $$

Taking $t_n = \frac{(1-3b)(2n-1)n}{\beta}$ and $M = bn$ shows that
$$ \mathbf{P}_{bn}\{S_{t_n} > (1-b)n\} \le \frac{(1-3b)}{\beta b^2 n} \to 0 \, , $$

as long as $\beta n \to \infty$. Combining with (23.8) shows that
$$ \mathbf{P}_{x_0}\{L_{t_n} > (1-b)\} \le (q/p)^{bn-1} + \frac{(1-3b)}{\beta b^2 n} \, . $$

We conclude that as long as $\beta n \to \infty$,
$$ d(t_n) \ge \mathbf{P}_{x_0}\{X_{t_n} \in G\} - \pi(G) \ge 1 - o(1) $$

as $n \to \infty$, whence $t_{\mathrm{mix}}(\varepsilon) \ge \frac{(1-3b)(2n-1)n}{\beta}$ for sufficiently large $n$.

$\blacksquare$

### **23.4. Exercises**

EXERCISE 23.1. For the biased exclusion process, bound $t_{\mathrm{mix}}$ as a function of $k, n$ and $p$ when there are $k$ particles.

EXERCISE 23.2. Suppose $\sigma$ and $\eta$ are permutations on $\{1, 2, \ldots, n\}$, and $\preceq$ is the partial order defined in Section 23.1.3. Show that $\sigma \preceq \eta$ if and only if there is a sequence of adjacent transpositions $\sigma = \sigma_1, \ldots, \sigma_r = \eta$ with $\sigma_i \preceq \sigma_{i+1}$.

### PDF page 350 (book page 334)

### **23.5. Notes**

As mentioned in the Notes of Chapter 16, Wilson first proved a pre-cutoff for random adjacent transpositions, showing that $1 \le \frac{t_{\mathrm{mix}}(\varepsilon)}{\pi^{-2}n^3 \log n}[1 + o(1)] \le 2$; **Lacoin (2016a)** proved a cutoff at $n^3 \log n/(\pi^2)$. In the same paper, he proves cutoff for random adjacent transpositions. On the $n$-cycle, **Lacoin (2016b)** proved a cutoff at $n^3 \log n/4\pi^2$ for the exclusion process with $n/2$ particles. Cutoff for the biased exclusion on the $n$-path remains an open problem, as does cutoff for the interchange process on the cycle.

For the exclusion process with $k$ particles on the $d$-dimensional torus with side-length $n$, **Morris (2006)** proved that
$$ t_{\mathrm{mix}} \le cn^3(\log d)(d + \log k) \, . $$

**Benjamini, Berger, Hoffman, and Mossel (2005)** first proved that $t_{\mathrm{mix}} = O(n^2)$ for the biased exclusion process on the line. The path coupling proof we give follows **Greenberg, Pascoe, and Randall (2009)**. **Levin and Peres (2016)** give a more detailed view of the dependence on $\beta$:

THEOREM. *Consider the $\beta$-biased exclusion process on $\{1, 2, \ldots, n\}$ with $k$ particles. We assume that $k/n \to \rho$ for $0 < \rho \le 1/2$.*
(i) *If $n\beta \le 1$, then*
$$ t_{\mathrm{mix}}^{(n)} \asymp n^3 \log n \, . \tag{23.9} $$
(ii) *If $1 \le n\beta \le \log n$, then*
$$ t_{\mathrm{mix}}^{(n)} \asymp \frac{n \log n}{\beta^2} \, . \tag{23.10} $$
(iii) *If $n\beta > \log n$ and $\beta < const. < 1$, then*
$$ t_{\mathrm{mix}}^{(n)} \asymp \frac{n^2}{\beta} \, . \tag{23.11} $$
*Moreover, in all regimes, the process has a pre-cutoff.*

For fixed $\beta$, **Labbé and Lacoin (2016)** prove the process has a cutoff.

The proof of monotonicity in Section 23.1.3 applies to the biased exclusion process as well.

D. Aldous conjectured that Proposition 23.1 holds on any graph. This was proven by **Caputo, Liggett, and Richthammer (2010)**.

Estimates for the mixing time of the interchange process and the exclusion process on general graphs were given by **Jonasson (2012)**, and by **Oliveira (2013)**, respectively.

For more on the exclusion on infinite graphs, see **Liggett (1985)** and **Liggett (1999)**.

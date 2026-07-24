# Chapter 18 — The Cutoff Phenomenon
*(PDF pages 277–287; book pages 261–271)*

### PDF page 277 (book page 261)

CHAPTER 18

# The Cutoff Phenomenon

**18.1. Definition**

For the top-to-random shuffle on $n$ cards, we obtained in Section 6.5.3 the bound

$$ d_n(n \log n + \alpha n) \leq e^{-\alpha}, \tag{18.1} $$

while in Section 7.4.1 we showed that

$$ \liminf_{n \to \infty} d_n(n \log n - \alpha n) \geq 1 - 2e^{2-\alpha}. \tag{18.2} $$

In particular, the upper bound in (18.1) tends to 0 as $\alpha \to \infty$, and the lower bound in (18.2) tends to 1 as $\alpha \to \infty$. It follows that $t_{\mathrm{mix}}(\varepsilon) = n \log n \left[ 1 + h(n, \varepsilon) \right]$, where $\lim_{n\to\infty} h(n, \varepsilon) = 0$ for all $\varepsilon$. This is a much more precise statement than the fact that the mixing time is of the order $n \log n$.

The previous example motivates the following definition. Suppose, for a sequence of Markov chains indexed by $n = 1, 2, \ldots$, the mixing time for the $n$-th chain is denoted by $t_{\mathrm{mix}}^{(n)}(\varepsilon)$. This sequence of chains has a **cutoff** if, for all $\varepsilon \in (0, 1)$,

$$ \lim_{n \to \infty} \frac{t_{\mathrm{mix}}^{(n)}(\varepsilon)}{t_{\mathrm{mix}}^{(n)}(1 - \varepsilon)} = 1. \tag{18.3} $$

The bounds (18.1) and (18.2) for the top-to-random chain show that the total variation distance $d_n$ for the $n$-card chain "falls off a cliff" at $t_{\mathrm{mix}}^{(n)}$. More precisely, when time is rescaled by $n \log n$, as $n \to \infty$ the function $d_n$ approaches a step function:

$$ \lim_{n \to \infty} d_n(cn \log n) = \begin{cases} 1 & \text{if } c < 1, \\ 0 & \text{if } c > 1. \end{cases} \tag{18.4} $$

In fact, this property characterizes when a sequence of chains has a cutoff.

LEMMA 18.1. *Let $t_{\mathrm{mix}}^{(n)}$ and $d_n$ be the mixing time and distance to stationarity, respectively, for the $n$-th chain in a sequence of Markov chains. The sequence has a cutoff if and only if*

$$ \lim_{n \to \infty} d_n(ct_{\mathrm{mix}}^{(n)}) = \begin{cases} 1 & \text{if } c < 1, \\ 0 & \text{if } c > 1. \end{cases} $$

### PDF page 278 (book page 262)

**FIGURE 18.1.** For a chain with a cutoff, the graph of $d_n(t)$ against $t$, when viewed on the time-scale of $t_{\mathrm{mix}}^{(n)}$, approaches a step function as $n \to \infty$. *[Figure: a plot with vertical axis labeled $d_n(t)$ and horizontal axis labeled $t$; the curve starts near the top (value near 1), stays roughly flat, then drops sharply down to near 0 at the point marked $t_{\mathrm{mix}}^{(n)}$ on the horizontal axis, remaining near 0 thereafter.]*

The proof is left to the reader as Exercise 18.1.

Returning to the example of the top-to-random shuffle on $n$ cards, the bounds (18.1) and (18.2) show that in an interval of length $\alpha n$ centered at $n \log n$, the total variation distance decreased from near 1 to near 0. The next definition formalizes this property.

A sequence of Markov chains has a cutoff with a **window** of size $O(w_n)$ if $w_n = o\left(t_{\mathrm{mix}}^{(n)}\right)$ and

$$ \lim_{\alpha \to -\infty} \liminf_{n \to \infty} d_n\left(t_{\mathrm{mix}}^{(n)} + \alpha w_n\right) = 1, $$

$$ \lim_{\alpha \to \infty} \limsup_{n \to \infty} d_n\left(t_{\mathrm{mix}}^{(n)} + \alpha w_n\right) = 0. $$

We say a family of chains has a **pre-cutoff** if it satisfies the weaker condition

$$ \sup_{0 < \varepsilon < 1/2} \limsup_{n \to \infty} \frac{t_{\mathrm{mix}}^{(n)}(\varepsilon)}{t_{\mathrm{mix}}^{(n)}(1 - \varepsilon)} < \infty. \tag{18.5} $$

Theorem 15.5 proved that the Glauber dynamics for the Ising model on the $n$-cycle has a pre-cutoff; as mentioned in the Notes to Chapter 15, that family of chains has a cutoff.

There are examples of chains with pre-cutoff but not cutoff; see the Notes.

**18.2. Examples of Cutoff**

**18.2.1. Biased random walk on a line segment.** Let $p \in (1/2, 1)$ and $q = 1 - p$, so $\beta := (p - q)/2 = p - 1/2 > 0$. Consider the lazy nearest-neighbor random walk with bias $\beta$ on the interval $\mathcal{X} = \{0, 1, \ldots, n\}$. When at an interior vertex, the walk remains in its current position with probability $1/2$, moves to the right with probability $p/2$, and moves to the left with probability $q/2$. When at an end-vertex, the walk remains in place with probability $1/2$ and moves to the adjacent interior vertex with probability $1/2$.

### PDF page 279 (book page 263)

THEOREM 18.2. *The lazy random walk $(X_t)$ with bias $\beta = p - 1/2$ on $\{0, 1, 2, \ldots, n\}$ has a cutoff at $\beta^{-1}n$ with a window of size $O(\sqrt{n})$. More precisely, there is constant $c(\beta) > 0$ such that for all $\alpha \in \mathbb{R}$,*

$$ \lim_{n \to \infty} d_n\left(\frac{n}{\beta} + \alpha\sqrt{n}\right) = \Phi(-c(\beta)\alpha)\,, \tag{18.6} $$

*where $\Phi$ is the standard Normal distribution function.*

The precise limit in (18.6) goes beyond proving a window of size $O(\sqrt{n})$ and describes the *shape* of the cutoff.

PROOF. We write $t_n(\alpha) := \beta^{-1}n + \alpha\sqrt{n}$.

*Upper bound, Step 1.* We first prove that if $\tau_n := \min\{t \geq 0 \, : \, X_t = n\}$, then

$$ \limsup_{n \to \infty} \mathbf{P}_0\{\tau_n > t_n(\alpha)\} \leq \Phi(-c(\beta)\alpha), \tag{18.7} $$

where $c(\beta) > 0$ depends on $\beta$ only and $\Phi$ is the standard normal distribution function.

Let $(S_t)$ be a lazy $\beta$-biased nearest-neighbor random walk on all of $\mathbb{Z}$, so $\mathbf{E}_k S_t = k + \beta t$. We couple $(X_t)$ to $(S_t)$ until time $\tau_n := \min\{t \geq 0 \, : \, X_t = n\}$, as follows: let $X_0 = S_0$, and set

$$ X_{t+1} = \begin{cases} 1 & \text{if } X_t = 0 \text{ and } S_{t+1} - S_t = -1, \\ X_t + (S_{t+1} - S_t) & \text{otherwise.} \end{cases} \tag{18.8} $$

This coupling satisfies $X_t \geq S_t$ for all $t \leq \tau_n$.

We have $\mathbf{E}_0 S_{t_n(\alpha)} = t_n(\alpha)\beta = n + \alpha\beta\sqrt{n}$, and

$$ \mathbf{P}_0\{S_{t_n(\alpha)} < n\} = \mathbf{P}_0\left\{ \frac{S_{t_n(\alpha)} - \mathbf{E}S_{t_n(\alpha)}}{\sqrt{t_n(\alpha)v}} < \frac{-\alpha\beta\sqrt{n}}{\sqrt{t_n(\alpha)v}} \right\}, $$

where $v = \frac{1}{2} - \beta^2$. By the Central Limit Theorem, the right-hand side above converges as $n \to \infty$ to $\Phi(-c(\beta)\alpha)$, where $c(\beta) = \beta^{3/2}/\sqrt{v}$. Thus

$$ \limsup_{n \to \infty} \mathbf{P}_0\{S_{t_n(\alpha)} < n\} = \Phi(-c(\beta)\alpha). \tag{18.9} $$

Since $X_t \geq S_t$ for $t \leq \tau_n$,

$$ \mathbf{P}_0\{\tau_n > t_n(\alpha)\} \leq \mathbf{P}_0\left\{ \max_{0 \leq s \leq t_n(\alpha)} S_s < n \right\} \leq \mathbf{P}_0\left\{ S_{t_n(\alpha)} < n \right\}, $$

which with (18.9) implies (18.7).

*Upper bound, Step 2.* We now show that we can couple two copies of $(X_t)$ so that the meeting time of the two chains is bounded by $\tau_n$.

We couple as follows: toss a coin to decide which particle to move. Move the chosen particle up one unit with probability $p$ and down one unit with probability $q$, unless it is at an end-vertex, in which case move it with probability one to the neighboring interior vertex. The time $\tau_{\text{couple}}$ until the particles meet is bounded by the time it takes the bottom particle to hit $n$, whence

$$ d_n(t_n(\alpha)) \leq \mathbf{P}_{x,y}\{\tau_{\text{couple}} > t_n(\alpha)\} \leq \mathbf{P}_0\{\tau_n > t_n(\alpha)\}. $$

This bound and (18.7) show that

$$ \limsup_{n \to \infty} d_n(t_n(\alpha)) \leq \Phi(-c(\beta)\alpha)\,. \tag{18.10} $$

### PDF page 280 (book page 264)

*Lower bound, Step 1.* Let $\theta := (q/p)$. We first prove that

$$ \limsup_{n \to \infty} \mathbf{P}_0\{X_{t_n(\alpha)} > n - h\} \leq 1 - \Phi(-c(\beta)\alpha) + \theta^{h-1}. \tag{18.11} $$

Let $(\tilde{X}_t)$ be the lazy biased random walk on $\{0, 1, \ldots\}$, with reflection at 0. By coupling with $(X_t)$ so that $X_t \leq \tilde{X}_t$, for $x \geq 0$ we have

$$ \mathbf{P}_0\{X_t > x\} \leq \mathbf{P}_0\{\tilde{X}_t > x\}. \tag{18.12} $$

Recall that $(S_t)$ is the biased lazy walk on all of $\mathbb{Z}$. Couple $(\tilde{X}_t)$ with $(S_t)$ so that $S_t \leq \tilde{X}_t$. Observe that $\tilde{X}_t - S_t$ increases (by a unit amount) only when $\tilde{X}_t$ is at 0, which implies that, for any $t$,

$$ \mathbf{P}_0\{\tilde{X}_t - S_t \geq h\} \leq \mathbf{P}_0\{\text{at least } h - 1 \text{ returns of } (\tilde{X}_t) \text{ to } 0\}. $$

By (9.20), the chance that the biased random walk on $\mathbb{Z}$, when starting from 1, hits 0 before $n$ equals $1 - (1 - \theta)/(1 - \theta^n)$. Letting $n \to \infty$, the chance that the biased random walk on $\mathbb{Z}$, when starting from 1, ever visits 0 equals $\theta$. Therefore,

$$ \mathbf{P}_0\{\text{at least } h - 1 \text{ returns of } (\tilde{X}_t) \text{ to } 0\} = \theta^{h-1}, $$

and consequently,

$$ \mathbf{P}_0\{\tilde{X}_t - S_t \geq h\} \leq \theta^{h-1}. \tag{18.13} $$

By (18.12) and (18.13),

$$ \mathbf{P}_0\{X_{t_n(\alpha)} > n - h\} \leq \mathbf{P}_0\{S_{t_n(\alpha)} > n - 2h\} + \mathbf{P}_0\{\tilde{X}_{t_n(\alpha)} - S_{t_n(\alpha)} \geq h\} $$
$$ \leq \mathbf{P}_0\{S_{t_n(\alpha)} > n - 2h\} + \theta^{h-1}. \tag{18.14} $$

By the Central Limit Theorem,

$$ \lim_{n \to \infty} \mathbf{P}_0\{S_{t_n(\alpha)} > n - 2h\} = 1 - \Phi(-c(\beta)\alpha), $$

which together with (18.14) establishes (18.11).

*Lower bound, Step 2.* The stationary distribution equals

$$ \pi^{(n)}(k) = \left[ \frac{(p/q) - 1}{(p/q)^{n+1} - 1} \right] (p/q)^k. $$

If $A_h = \{n - h + 1, \ldots, n\}$, then

$$ \pi^{(n)}(A_h) = \frac{1 - (q/p)^h}{1 - (q/p)^{n+1}}. $$

Therefore,

$$ \liminf_{n \to \infty} d_n(t_n(\alpha)) \geq \liminf_{n \to \infty} \left[ \pi^{(n)}(A_h) - \mathbf{P}_0\{X_{t_n(\alpha)} > n - h\} \right] $$
$$ \geq 1 - \theta^h - \left[ 1 - \Phi(-c(\beta)\alpha) + \theta^{h-1} \right]. $$

This holds for any $h$, so

$$ \liminf_{n \to \infty} d_n(t_n(\alpha)) \geq \Phi(-c(\beta)\alpha)\,. $$

Combining with (18.10) shows that

$$ \lim_{n \to \infty} d_n(t_n(\alpha)) = \Phi(-c(\beta)\alpha)\,. $$

$\blacksquare$

### PDF page 281 (book page 265)

**18.2.2. Random walk on the hypercube.** We return to the lazy random walk on the $n$-dimensional hypercube. Proposition 7.14 shows that

$$ t_{\text{mix}}(1 - \varepsilon) \geq \frac{1}{2}n \log n - c_\ell(\varepsilon)n. \tag{18.15} $$

In Section 5.3.1, it was shown via coupling that

$$ t_{\text{mix}}(\varepsilon) \leq n \log n + c_u(\varepsilon)n\,. $$

This was improved in Example 12.19, where it was shown that

$$ t_{\text{mix}}(\varepsilon) \leq \frac{1}{2}n \log n + c_s(\varepsilon)n\,, $$

which when combined with the lower bound proves there is a cutoff at $\frac{1}{2}n \log n$ with a window of size $O(n)$. The proof given there relies on knowing all the eigenvalues of the chain. We give a different proof here that does not require the eigenvalues.

THEOREM 18.3. *The lazy random walk on the $n$-dimensional hypercube has a cutoff at $(1/2)n \log n$ with a window of size $O(n)$.*

PROOF. Let $\boldsymbol{X}_t = (X_t^1, \ldots, X_t^n)$ be the position of the random walk at time $t$, and let $W_t = W(\boldsymbol{X}_t) = \sum_{i=1}^{n} X_t^i$ be the Hamming weight of $\boldsymbol{X}_t$. As follows from the discussion in Section 2.3, $(W_t)$ is a lazy version of the Ehrenfest urn chain whose transition matrix is given in (2.8). We write $\pi_W$ for the stationary distribution of $(W_t)$, which is binomial with parameters $n$ and $1/2$.

The study of $(\boldsymbol{X}_t)$ can be reduced to the study of $(W_t)$ because of the following identity:

$$ \|\mathbf{P}_{\boldsymbol{1}}\{\boldsymbol{X}_t \in \cdot\} - \pi\|_{\text{TV}} = \|\mathbf{P}_n\{W_t \in \cdot\} - \pi_W\|_{\text{TV}}\,. \tag{18.16} $$

*Proof of* (18.16). Let $\mathcal{X}_w := \{\boldsymbol{x} \, : \, W(\boldsymbol{x}) = w\}$. Note that by symmetry, the functions $\boldsymbol{x} \mapsto \mathbf{P}_{\boldsymbol{1}}\{\boldsymbol{X}_t = \boldsymbol{x}\}$ and $\pi$ are constant over $\mathcal{X}_w$. Therefore,

$$ \sum_{\boldsymbol{x} \, : \, W(\boldsymbol{x}) = w} |\mathbf{P}_{\boldsymbol{1}}\{\boldsymbol{X}_t = \boldsymbol{x}\} - \pi(\boldsymbol{x})| = \left| \sum_{\boldsymbol{x} \, : \, W(\boldsymbol{x}) = w} \mathbf{P}_{\boldsymbol{1}}\{\boldsymbol{X}_t = \boldsymbol{x}\} - \pi(\boldsymbol{x}) \right| $$
$$ = |\mathbf{P}_{\boldsymbol{1}}\{W_t = w\} - \pi_W(w)|\,. $$

(The absolute values can be moved outside the sum in the first equality because all of the terms in the sum are equal.) Summing over $w \in \{0, 1, \ldots, n\}$ and dividing by 2 yields (18.16).

Since $(\boldsymbol{X}_t)$ is a transitive chain,

$$ d(t) = \|\mathbf{P}_{\boldsymbol{1}}\{\boldsymbol{X}_t \in \cdot\} - \pi\|_{\text{TV}}\,, $$

and it is enough to bound the right-hand side of (18.16).

We now construct a coupling $(W_t, Z_t)$ of the lazy Ehrenfest chain started from $w$ with the lazy Ehrenfest chain started from $z$. Provided that the two particles have not yet collided, at each move, a fair coin is tossed to determine which of the two particles moves; the chosen particle makes a transition according to the matrix (2.8), while the other particle remains in its current position. The particles move together once they have met for the first time.

Suppose, without loss of generality, that $z \geq w$. Since the particles never cross each other, $Z_t \geq W_t$ for all $t$. Consequently, if $D_t = |Z_t - W_t|$, then $D_t = Z_t - W_t \geq$

### PDF page 282 (book page 266)

0. Let $\tau := \min\{t \geq 0 \,:\, Z_t = W_t\}$. Conditioning that $(Z_t, W_t) = (z_t, w_t)$, where $z_t \neq w_t$

$$ D_{t+1} - D_t = \begin{cases} 1 & \text{with probability } (1/2)(1 - z_t/n) + (1/2)w_t/n, \\ -1 & \text{with probability } (1/2)z_t/n + (1/2)(1 - w_t/n). \end{cases} \tag{18.17} $$

From (18.17) we see that on the event $\{\tau > t\}$,

$$ \mathbf{E}_{z,w}[D_{t+1} - D_t \mid Z_t = z_t, W_t = w_t] = -\frac{(z_t - w_t)}{n} = -\frac{D_t}{n}. \tag{18.18} $$

Because $\mathbf{1}\{\tau > t\} = \mathbf{1}\{Z_t \neq W_t\}$,

$$ \mathbf{E}_{z,w}[\mathbf{1}\{\tau > t\}D_{t+1} \mid Z_t, W_t] = \left(1 - \frac{1}{n}\right) D_t \mathbf{1}\{\tau > t\}. $$

Taking expectation, we have

$$ \mathbf{E}_{z,w}[D_{t+1}\mathbf{1}\{\tau > t\}] = \left(1 - \frac{1}{n}\right) \mathbf{E}_{z,w}[D_t \mathbf{1}\{\tau > t\}]. $$

Since $\mathbf{1}\{\tau > t + 1\} \leq \mathbf{1}\{\tau > t\}$, we have

$$ \mathbf{E}_{z,w}[D_{t+1}\mathbf{1}\{\tau > t + 1\}] \leq \left(1 - \frac{1}{n}\right) \mathbf{E}_{z,w}[D_t \mathbf{1}\{\tau > t\}]. $$

By induction,

$$ \mathbf{E}_{z,w}[D_t \mathbf{1}\{\tau > t\}] \leq \left(1 - \frac{1}{n}\right)^t (z - w) \leq ne^{-t/n}. \tag{18.19} $$

Also, from (18.17), provided $\tau > t$, the process $(D_t)$ is at least as likely to move downwards as it is to move upwards. Thus, until time $\tau$, the process $(D_t)$ can be coupled with a simple random walk $(S_t)$ so that $S_0 = D_0$ and $D_t \leq S_t$.

If $\tilde{\tau} := \min\{t \geq 0 \,:\, S_t = 0\}$, then $\tau \leq \tilde{\tau}$. By Theorem 2.26, there is a constant $c_1$ such that for $k \geq 0$,

$$ \mathbf{P}_k\{\tau > u\} \leq \mathbf{P}_k\{\tilde{\tau} > u\} \leq \frac{c_1 k}{\sqrt{u}}. \tag{18.20} $$

By (18.20),

$$ \mathbf{P}_{z,w}\{\tau > s + u \mid D_s\} = \mathbf{1}\{\tau > s\}\mathbf{P}_{D_s}\{\tau > u\} \leq \frac{c_1 D_s \mathbf{1}\{\tau > s\}}{\sqrt{u}}. $$

Taking expectation above and applying (18.19) shows that

$$ \mathbf{P}_{z,w}\{\tau > s + u\} \leq \frac{c_1 ne^{-s/n}}{\sqrt{u}}. \tag{18.21} $$

Letting $u = \alpha n$ and $s = (1/2)n \log n$ above, by Corollary 5.5 we have

$$ d_n((1/2)n \log n + \alpha n) \leq \frac{c_1}{\sqrt{\alpha}}. $$

We conclude that

$$ \lim_{\alpha \to \infty} \limsup_{n \to \infty} d_n((1/2)n \log n + \alpha n) = 0. $$

The lower bound (7.20) completes the proof. $\blacksquare$

### PDF page 283 (book page 267)

**18.3. A Necessary Condition for Cutoff**

When does a family of chains have a cutoff? The following proposition gives a necessary condition.

PROPOSITION 18.4. *For a sequence of irreducible aperiodic reversible Markov chains with relaxation times $\{t_{\mathrm{rel}}^{(n)}\}$ and mixing times $\{t_{\mathrm{mix}}^{(n)}\}$, if there is a pre-cutoff, then $t_{\mathrm{mix}}^{(n)}/(t_{\mathrm{rel}}^{(n)} - 1) \to \infty$ as $n \to \infty$.*

PROOF. If $t_{\mathrm{mix}}^{(n)}/(t_{\mathrm{rel}}^{(n)} - 1)$ does not tend to infinity, then there is an infinite set of integers $J$ and a constant $c_1 > 0$ such that $(t_{\mathrm{rel}}^{(n)} - 1)/t_{\mathrm{mix}}^{(n)} \geq c_1$ for $n \in J$. Dividing both sides of (12.14) by $t_{\mathrm{mix}}^{(n)}$, we have for $n \in J$,

$$ \frac{t_{\mathrm{mix}}^{(n)}(\varepsilon)}{t_{\mathrm{mix}}^{(n)}} \geq \frac{t_{\mathrm{rel}}^{(n)} - 1}{t_{\mathrm{mix}}^{(n)}} \log\left(\frac{1}{2\varepsilon}\right) \geq c_1 \log\left(\frac{1}{2\varepsilon}\right). $$

As $\varepsilon \to 0$, the right-hand side increases to infinity. This contradicts the definition of (18.5). $\blacksquare$

Recall that we write $a_n \asymp b_n$ to mean that there exist positive and finite constants $c_1$ and $c_2$, not depending on $n$, such that $c_1 \leq a_n/b_n \leq c_2$ for all $n$.

EXAMPLE 18.5. Consider the lazy random walk on the cycle $\mathbb{Z}_n$. In Section 5.3.2 we showed that $t_{\mathrm{mix}}^{(n)}$ is of order $n^2$. In Section 12.3.1, we computed the eigenvalues of the transition matrix, finding that $t_{\mathrm{rel}}^{(n)} \asymp n^2$ also. By Proposition 18.4, there is no pre-cutoff.

EXAMPLE 18.6. Let $T_n$ be the rooted binary tree with $n$ vertices. In Example 7.8, we showed that the lazy simple random walk has $t_{\mathrm{mix}} \asymp n$. Together with Theorem 12.5, this implies that there exists a constant $c_1$ such that $t_{\mathrm{rel}} \leq c_1 n$. In Example 7.8, we actually showed that $\Phi_\star \leq 1/(n-2)$. Thus, by Theorem 13.10, we have $\gamma \leq 2/(n-2)$, whence $t_{\mathrm{rel}} \geq c_2 n$ for some constant positive $c_2$. An application of Proposition 18.4 shows that there is no pre-cutoff for this family of chains.

The question remains if there are conditions which ensure that the converse of Proposition 18.4 holds. Below we give a variant of an example due to Igor Pak (personal communication) which shows the converse is not true in general.

EXAMPLE 18.7. Let $\{P_n\}$ be a family of reversible transition matrices with a cutoff, and with $\inf_n t_{\mathrm{rel}}^{(n)} - 1 > 0$. By Proposition 18.4, $t_{\mathrm{rel}}^{(n)} = o(t_{\mathrm{mix}}^{(n)})$. (Take, e.g., the lazy random walk on the hypercube.) Let $L_n := \sqrt{t_{\mathrm{rel}}^{(n)} t_{\mathrm{mix}}^{(n)}}$, and define the matrix

$$ \tilde{P}_n = \left(1 - \frac{1}{L_n}\right)P_n + \frac{1}{L_n}\Pi_n, $$

where $\Pi_n(x, y) := \pi_n(y)$ for all $x$.

We first prove that

$$ \left\| \tilde{P}_n^t(x, \cdot) - \pi_n \right\|_{\mathrm{TV}} = \left(1 - \frac{1}{L_n}\right)^t \left\| P_n^t(x, \cdot) - \pi_n \right\|_{\mathrm{TV}}. \tag{18.22} $$

*Proof of* (18.22). One step of the new chain $(\tilde{X}_t)$ can be generated by first tossing a coin with probability $1/L_n$ of heads; if heads, a sample from $\pi_n$ is produced, and

### PDF page 284 (book page 268)

if tails, a transition from $P_n$ is used. If $\tau$ is the first time that the coin lands heads, then $\tau$ has a geometric distribution with success probability $1/L_n$. Accordingly,

$$ \begin{aligned} \mathbf{P}_x\{\tilde{X}_t^{(n)} = y\} - \pi_n(y) &= \mathbf{P}_x\{\tilde{X}_t^{(n)} = y, \tau \leq t\} + \mathbf{P}_x\{\tilde{X}_t^{(n)} = y, \tau > t\} - \pi_n(y) \\ &= -\pi_n(y)[1 - \mathbf{P}_x\{\tau \leq t\}] + P_n^t(x, y)\mathbf{P}_x\{\tau > t\} \\ &= \left[P_n^t(x, y) - \pi_n(y)\right]\mathbf{P}_x\{\tau > t\}. \end{aligned} $$

Taking absolute value and summing over $y$ gives (18.22). We conclude that

$$ \tilde{d}_n(t) = (1 - L_n^{-1})^t d_n(t). $$

Therefore,

$$ \tilde{d}_n(\beta L_n) \leq e^{-\beta}d_n(\beta L_n) \leq e^{-\beta}, $$

and $\tilde{t}_{\mathrm{mix}}^{(n)} \leq c_1 L_n$ for some constant $c_1$. On the other hand

$$ \tilde{d}_n(\beta L_n) = e^{-\beta[1+o(1)]}d_n(\beta L_n). \tag{18.23} $$

Since $L_n = o(t_{\mathrm{mix}}^{(n)})$ and the $P_n$-chains have a cutoff, we have that $d_n(\beta L_n) \to 1$ for all $\beta$, whence from the above,

$$ \lim_{n \to \infty} \tilde{d}_n(\beta L_n) = e^{-\beta}. $$

This shows both that $\tilde{t}_{\mathrm{mix}}^{(n)} \asymp L_n$ and that there is no pre-cutoff for the $\tilde{P}$-chains.

Let $\{\lambda_j^{(n)}\}_{j=1}^n$ be the eigenvalues of $P_n$. As can be directly verified, $\tilde{\lambda}_j^{(n)} := (1 - 1/L_n)\lambda_j^{(n)}$ is an eigenvalue of $\tilde{P}_n$ for $j > 1$. Thus,

$$ \tilde{\gamma}_n = 1 - \left(1 - \frac{1}{L_n}\right)(1 - \gamma_n) = \gamma_n \left[1 + o(1)\right]. $$

(We have used that $\gamma_n L_n \to \infty$, which follows from our assumption.) We conclude that $\tilde{t}_{\mathrm{rel}}^{(n)} = [1 + o(1)]t_{\mathrm{rel}}^{(n)}$. However, $\tilde{t}_{\mathrm{rel}}^{(n)} = o(\tilde{t}_{\mathrm{mix}}^{(n)})$, since $\tilde{t}_{\mathrm{mix}}^{(n)} \asymp L_n$.

**18.4. Separation Cutoff**

The mixing time can be defined for other distances. The separation distance, defined in Section 6.4, is $s(t) = \max_{x \in \mathcal{X}} s_x(t)$, where

$$ s_x(t) := \max_{y \in \mathcal{X}} \left[1 - \frac{P^t(x, y)}{\pi(y)}\right]. $$

We define

$$ t_{\mathrm{sep}}(\varepsilon) := \inf\{t \geq 0 \,:\, s(t) \leq \varepsilon\}. $$

A family of Markov chains with separation mixing times $\{t_{\mathrm{sep}}^{(n)}\}$ has a ***separation cutoff*** if

$$ \lim_{n \to \infty} \frac{t_{\mathrm{sep}}^{(n)}(\varepsilon)}{t_{\mathrm{sep}}^{(n)}(1 - \varepsilon)} = 1 \quad \text{for all } \varepsilon \in (0, 1). $$

THEOREM 18.8. *The lazy random walk on the $n$-dimensional hypercube has a separation cutoff at $n \log n$ with a window of order $n$.*

### PDF page 285 (book page 269)

*Proof.* We proved the following upper bound in Section 6.5.2:

$$ s(n \log n + \alpha n) \leq e^{-\alpha}. \tag{18.24} $$

We are left with the task of proving a lower bound. Recall that $\tau_{\mathrm{refresh}}$ is the strong stationary time equal to the first time all the coordinates have been selected for updating. Since, when starting from $\mathbf{1}$, the state $\mathbf{0}$ is a halting state for $\tau_{\mathrm{refresh}}$, it follows that

$$ s_{\mathbf{1}}(t) = \mathbf{P_1}\{\tau_{\mathrm{refresh}} > t\}. $$

(See Proposition 6.14.)

Let $R_t$ be the number of coordinates not updated by time $t$. Let $t_n := n \log n - \alpha n$. By Lemma 7.13, we have

$$ \mathbf{E}R_{t_n} = n(1 - n^{-1})^{t_n} \to e^{\alpha} \quad \text{and} \quad \mathrm{Var}(R_{t_n}) \leq e^{\alpha}. $$

Therefore, by Chebyshev's inequality, there exists $c_1 > 0$ such that

$$ \mathbf{P_1}\{\tau_{\mathrm{refresh}} \leq t_n\} = \mathbf{P_1}\{R_{t_n} = 0\} \leq c_1 e^{-\alpha}. $$

Thus,

$$ s_{\mathbf{1}}(n \log n - \alpha n) \geq 1 - c_1 e^{-\alpha}. \tag{18.25} $$

The bounds (18.24) and (18.25) together imply a separation cutoff at $n \log n$ with a window size $O(n)$. $\blacksquare$

**Exercises**

EXERCISE 18.1. Let $t_{\mathrm{mix}}^n$ and $d_n$ denote the mixing time and distance to stationarity, respectively, for the $n$-th chain in a sequence of Markov chains. Show that the sequence has a cutoff if and only if

$$ \lim_{n \to \infty} d_n(ct_{\mathrm{mix}}^n) = \begin{cases} 1 & \text{if } c < 1, \\ 0 & \text{if } c > 1. \end{cases} \tag{18.26} $$

EXERCISE 18.2. Show that the exclusion process on the complete graph with $k = n/2$ (Example 14.9) has cutoff at $(1/4)n \log n$.

EXERCISE 18.3 (Bernoulli-Laplace Diffusion). Consider two urns, the left containing $n/2$ red balls, the right containing $n/2$ black balls. In every step a ball is chosen at random in each urn and the two balls are switched. Show that this chain has cutoff at $(1/8)n \log n$.

*Hint:* Observe that the previous chain is a lazy version of this chain.

EXERCISE 18.4. Consider lazy simple random walk on $\mathbb{Z}_n^n$. Show the chain has cutoff at time $cn^3 \log n$ and determine the constant $c$.

EXERCISE 18.5. Consider the top-to-random transposition shuffle, which transposes the top card with a randomly chosen card from the deck. (Note the randomly chosen card may be the top card.) The chain has a cutoff at $n \log n$. Prove the chain has a precut-off.

**Notes**

The biased random walk on the interval is studied in **Diaconis and Fill (1990)**; see also the discussion in **Diaconis and Saloff-Coste (2006)**, which contains many examples. More on cutoff is discussed in **Chen and Saloff-Coste (2008)**.

### PDF page 286 (book page 270)

**FIGURE 18.2.** Random walk on the network shown on the top has a pre-cutoff, but no cutoff. The shape of the graph of $d(t)$ is shown on the bottom. *[Figure: At the top, a network diagram of a random walk. Starting from a left-most endpoint, a path of vertices (dashed, labeled $5n$) with transition probabilities $1/3$ (left) and $2/3$ (right) leads to a fork. From the fork, two paths lead to a right-most endpoint: a top path (dashed, labeled $2n$) of vertices with transition probabilities $1/3$ and $2/3$, and a bottom path (dashed, labeled $n$) of vertices with transition probabilities $1/5$ and $4/5$. Below, a plot of $d(t)$ versus $t$ showing a curve that starts high, drops sharply near $15n$, has a small plateau between $(15+5/3)n$ and $21n$, then drops again to near zero. The $t$-axis is marked at $15n$, $(15+5/3)n$, and $21n$.]*

**A chain with pre-cutoff, but no cutoff.** David Aldous (**2004**) created the chain whose transition probabilities are shown in Figure 18.2. Assume the right-most state has a loop. The shape of the graph of $d(t)$ as a function of $t$ is shown on the bottom of the figure. Since the stationary distribution grows geometrically from left-to-right, the chain mixes once it reaches near the right-most point. It takes about $15n$ steps for a particle started at the left-most endpoint to reach the fork. With probability about $3/4$, it first reaches the right endpoint via the bottom path. (This can be calculated using effective resistances; see Section 9.4.) When the walker takes the bottom path, it takes about $(5/3)n$ additional steps to reach the right. In fact, the time will be within order $\sqrt{n}$ of $(5/3)n$ with high probability. In the event that the walker takes the top path, it takes about $6n$ steps (again $\pm O(\sqrt{n})$) to reach the right endpoint. Thus the total variation distance will drop by $3/4$ at time $[15 + (5/3)]n$, and it will drop by the remaining $1/4$ at around time $(15 + 6)n$. Both of these drops will occur within windows of order $\sqrt{n}$. Thus, the ratio $t_{\mathrm{mix}}(\varepsilon)/t_{\mathrm{mix}}(1 - \varepsilon)$ will stay bounded as $n \to \infty$, but it does not tend to 1.

The proof of Theorem 18.3 is adapted in **Levin, Luczak, and Peres (2010)** to establish cutoff for the Glauber dynamics of the Ising model on the complete graph at high temperature.

**Ding, Lubetzky, and Peres (2010a)** analyzed the cutoff phenomena for birth-and-death chains, proving:

THEOREM. *For any $0 < \varepsilon < \frac{1}{2}$ there exists an explicit $c_\varepsilon > 0$ such that every lazy irreducible birth-and-death chain $(X_t)$ satisfies*

$$ t_{\mathrm{mix}}(\varepsilon) - t_{\mathrm{mix}}(1 - \varepsilon) \leq c_\varepsilon \sqrt{t_{\mathrm{rel}} \cdot t_{\mathrm{mix}}(\tfrac{1}{4})}. \tag{18.27} $$

### PDF page 287 (book page 271)

COROLLARY. *Let $(X_t^{(n)})$ be a sequence of lazy irreducible birth-and-death chains. Then it exhibits cutoff in total-variation distance if and only if $t_{\mathrm{mix}}^{(n)} \cdot \gamma(n)$ tends to infinity with $n$. Furthermore, the cutoff window size is at most the geometric mean between the mixing time and relaxation time.*

Earlier, **Diaconis and Saloff-Coste (2006)** obtained a similar result for separation cutoff. Thus, for birth-and-death chains, total-variation and separation cutoffs are equivalent. However, **Hermon, Lacoin, and Peres (2016)** show that this does not hold for general reversible chains.

The equivalence of cutoff to the condition $t_{\mathrm{rel}} = o(t_{\mathrm{mix}})$ is shown for random walk on weighted trees in **Basu, Hermon, and Peres (2015)**.

**Lacoin (2015)** shows that chains that are $n$-fold products always exhibit precutoff, but need not exhibit cutoff.

**Lubetzky and Sly (2010)** prove cutoff for random regular graphs:

THEOREM. *Let $G$ be a random $d$-regular graph for $d \geq 3$ fixed. Then with high probability, the simple random walk on $G$ exhibits cutoff at time $\frac{d}{d-2} \log_{d-1} n$ with a window of order $\sqrt{\log n}$.*

Extensions to random graphs that are not regular are given in **Ben-Hamou and Salez (2015)** (for non-backtracking walk) and **Berestycki, Lubetzky, Peres, and Sly (2015)**.

Ramanujan graphs are expanders with the largest possible spectral gap. Cutoff on these graphs was established in **Lubetzky and Peres (2016)**.

**Ganguly, Lubetzky, and Martinelli (2015)** prove cutoff for the East model (introduced in Section 7.4.2).

A precise analysis of the Bernoulli-Laplace chain in Exercise 18.3 is given by **Diaconis and Shahshahani (1987)**. The top-to-random transposition chain in Exercise 18.5 was analyzed via Fourier methods in **Diaconis (1988b)**.

Cutoff results for the Ising model are mentioned in the Notes to Chapter 15. Cutoff for the lamplighter walks is discussed in the next chapter.

Some references that treat cutoff in special chains are **Pourmiri and Sauerwald (2014)** and **Peres and Sousi (2015b)**.

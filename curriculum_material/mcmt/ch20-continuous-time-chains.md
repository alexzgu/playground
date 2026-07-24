# Chapter 20 — Continuous-Time Chains*
*(PDF pages 296–306; book pages 280–290)*

### PDF page 296 (book page 280)

CHAPTER 20

# Continuous-Time Chains*

**20.1. Definitions**

We now construct, given a transition matrix $P$, a process $(X_t)_{t \in [0, \infty)}$ which we call the ***continuous-time chain*** with transition matrix $P$. The random times between transitions for this process are i.i.d. exponential random variables of rate $r$, and at these transition times moves are made according to $P$. Continuous-time chains are often natural models in applications, since they do not require transitions to occur at regularly specified intervals.

More precisely, let $T_1, T_2, \ldots$ be independent and identically distributed exponential random variables of rate $r$. That is, each $T_i$ takes values in $[0, \infty)$ and has distribution function

$$ \mathbf{P}\{T_i \le t\} = \begin{cases} 1 - e^{-rt} & \text{if } t \ge 0, \\ 0 & \text{if } t < 0. \end{cases} $$

Let $(\Phi_k)_{k=0}^\infty$ be a Markov chain with transition matrix $P$, independent of the random variables $(T_k)_{k=1}^\infty$. Let $S_0 = 0$ and $S_k := \sum_{i=1}^k T_i$ for $k \ge 1$. Define

$$ X_t := \Phi_k \quad \text{for } S_k \le t < S_{k+1}. \tag{20.1} $$

Change-of-states occur only at the ***transition times*** $S_1, S_2, \ldots$. (Note, however, that if $P(x, x) > 0$ for at least one state $x \in \mathcal{X}$, then it is possible that the chain does not change state at a transition time.)

Define $N_t := \max\{k : S_k \le t\}$ to be the number of transition times up to and including time $t$. Observe that $N_t = k$ if and only if $S_k \le t < S_{k+1}$. From the definition (20.1),

$$ \mathbf{P}_x\{X_t = y \mid N_t = k\} = \mathbf{P}_x\{\Phi_k = y\} = P^k(x, y). \tag{20.2} $$

Also, the distribution of $N_t$ is Poisson with mean $r \cdot t$ (Exercise 20.3):

$$ \mathbf{P}\{N_t = k\} = \frac{e^{-rt}(rt)^k}{k!}. \tag{20.3} $$

In the construction above, the starting point was a transition matrix $P$. In practice, instead one often is given non-negative ***jumps rates*** $q(x, y)$ for $x \ne y$. (These are not assumed to be bounded by 1.) Suppose continuous-time dynamics when currently in state $x$ are as follows: Each $y \ne x$ is given a Poisson clock run at rate $q(x, y)$, and these clocks are independent of one another. If the first among these clocks to ring is at $y$, then a jump from $x$ to $y$ is made. Thus, the total jump rate at $x$ is given by $q(x) := \sum_{y : y \ne x} q(x, y)$, and when a jump occurs, some $y \ne x$ is chosen according to the distribution $q(x, \cdot)/q(x)$. Let $Q$ be the jump matrix

### PDF page 297 (book page 281)

specified by

$$ Q(x,y) = \begin{cases} q(x,y) & \text{if } x \neq y, \\ -q(x) & \text{if } y = x \, . \end{cases} $$

Note that $\sum_y Q(x,y) = 0$ for all $x$. In the case of continuizing a matrix $P$ at rate 1, we have $Q = P - I$.

For any jump matrix $Q$, set $r = \max_{x \in \mathcal{X}} q(x)$ and define

$$ P(x,y) = \frac{q(x,y)}{r} \quad \text{for } x \neq y $$

$$ P(x,x) = 1 - \frac{q(x)}{r} \, . $$

With this transition matrix, $Q = r(P - I)$, and the chain corresponding to $Q$ is the same process as continuizing the transition matrix $P$ at rate $r$.

A probability $\pi$ is stationary for $P$ if and only if $\pi Q = 0$. Note that if $\varphi$ is an eigenfunction of $P$ with eigenvalue $\lambda$, then $\varphi$ is also an eigenfunction of $Q = r(P-I)$ with eigenvalue $-r(1 - \lambda)$.

The **heat kernel** $H_t$ is defined by $H_t(x,y) := \mathbf{P}_x\{X_t = y\}$. From (20.2) and (20.3), it follows that

$$ H_t(x,y) = \sum_{k=0}^{\infty} \mathbf{P}_x\{X_t = y \mid N_t = k\}\mathbf{P}_x\{N_t = k\} \tag{20.4} $$

$$ = \sum_{k=0}^{\infty} \frac{e^{-rt}(rt)^k}{k!} P^k(x,y). \tag{20.5} $$

For an $m \times m$ matrix $M$, define the $m \times m$ matrix $e^M := \sum_{i=0}^{\infty} \frac{M^i}{i!}$. In matrix representation,

$$ H_t = e^{rt(P-I)} = e^{tQ}. \tag{20.6} $$

For a function $f : \mathcal{X} \to \mathbb{R}$, differentiating (20.5) shows that, setting $Q = r(P - I)$,

$$ \frac{d}{dt} H_t f = H_t Q f = Q H_t f \tag{20.7} $$

Note that if $\varphi$ is an eigenfunction of $Q$ with eigenvalue $\mu$, then solving the differential equation (20.7) shows that

$$ H_t \varphi = e^{\mu t} \varphi \, . $$

In particular, if $Q = r(P - I)$ and $\varphi$ is an eigenfunction of $P$ with eigenvalue $\lambda$, then

$$ H_t \varphi = e^{-r(1-\lambda)t} \varphi \, . \tag{20.8} $$

As well, if $\varphi$ is an eigenfunction of $H_t$ with eigenvalue $e^{\mu t}$ for all $t$, then $\varphi$ is an eigenfunction of $Q$ with eigenvalue $\mu$.

**20.2. Continuous-Time Mixing**

The heat kernel for a continuous-time chain converges to a stationary distribution as $t \to \infty$.

### PDF page 298 (book page 282)

**Theorem 20.1.** *Let $P$ be an irreducible transition matrix, and let $H_t$ be the corresponding heat kernel. Then there exists a unique probability distribution $\pi$ such that $\pi H_t = \pi$ for all $t \geq 0$ and*

$$ \max_{x \in \mathcal{X}} \|H_t(x,\cdot) - \pi\|_{\mathrm{TV}} \to 0 \quad as \quad t \to \infty. $$

The total variation distance in the theorem is monotone decreasing in $t$; see Exercise 20.2.

**Remark 20.2.** The above theorem does not require that $P$ is aperiodic, unlike Theorem 4.9. This is one advantage of working with continuous-time chains.

This theorem is easy to prove directly; see Exercise 20.1. Below, we prove the stronger Theorem 20.3.

In view of Theorem 20.1 and Exercise 20.2, we define

$$ t_{\mathrm{mix}}^{\mathrm{cont}}(\varepsilon) := \inf \left\{ t \geq 0 \, : \, \max_{x \in \mathcal{X}} \|H_t(x,\cdot) - \pi\|_{\mathrm{TV}} \leq \varepsilon \right\}. \tag{20.9} $$

Note that if $H_t^{(r)}$ is the heat kernel corresponding to $P$ run at rate $r$, and $H_t$ is the heat kernel corresponding to $P$ run at unit rate, then $H_t = H_{t/r}^{(r)}$, so that

$$ t_{\mathrm{mix}}^{\mathrm{cont}}(\varepsilon) = r \cdot t_{\mathrm{mix}}^{\mathrm{cont},(r)}(\varepsilon) \, . $$

Note that $\|H_t(x,\cdot) - \pi\|_{\mathrm{TV}}$ is monotone non-increasing in $t$. (Exercise 20.2.) Thus, the next theorem, which relates the mixing time of lazy Markov chains with the mixing time of the related continuous-time Markov chain, implies Theorem 20.1.

**Theorem 20.3.** *Let $P$ be an irreducible transition matrix, not necessarily aperiodic or reversible. Let $\tilde{P} = (1/2)(I + P)$ be the lazy version of $P$, and let $H_t$ be the heat kernel associated to $P$ run at rate 1.*

(i) *Let $N_{2k}$ be a Poisson(2k) random variable. Then*

$$ \|H_k(x,\cdot) - \pi\|_{\mathrm{TV}} \leq \left\| \widetilde{P}^k(x,\cdot) - \pi \right\|_{\mathrm{TV}} + \mathbf{P}\{N_{2k} < k\} \, . \tag{20.10} $$

(ii) *Let $Y$ be a binomial$(4m, \frac{1}{2})$ random variable, let $\Psi$ be a Poisson(m) random variable, and define*

$$ \eta_m := \|\mathbf{P}\{Y \in \cdot\} - \mathbf{P}\{\Psi + m \in \cdot\}\|_{\mathrm{TV}} \, . $$

*Then*

$$ \left\| \widetilde{P}^{4m}(x,\cdot) - \pi \right\|_{\mathrm{TV}} \leq \|H_m(x,\cdot) - \pi\|_{\mathrm{TV}} + \eta_m $$

Note that $\lim_{k \to \infty} \mathbf{P}\{N_{2k} < k\} = 0$ by the Law of Large Numbers. Moreover, good explicit bounds can be obtained, for example, $\mathbf{P}\{N_{2k} < k\} \leq (e/4)^k$ (Exercise 20.6).

Part (ii) of the above theorem is meaningful due to the following lemma:

**Lemma 20.4.** *Let $Y$ be a binomial$(4m, \frac{1}{2})$ random variable, and let $\Psi = \Psi_m$ be a Poisson variable with mean $m$. Then*

$$ \eta_m := \|\mathbf{P}\{Y \in \cdot\} - \mathbf{P}\{\Psi + m \in \cdot\}\|_{\mathrm{TV}} \to 0 $$

*as $m \to \infty$.*

### PDF page 299 (book page 283)

**Proof of Lemma 20.4.** Note that $Y$ and $\Psi + m$ both have mean $2m$ and variance $m$. Given $\varepsilon > 0$, let $A = 2\varepsilon^{-1/2}$. By Chebyshev's inequality,

$$ \mathbf{P}\left\{ |Y - 2m| \geq A\sqrt{m} \right\} \leq \varepsilon/4 \quad \text{and} \quad \mathbf{P}\left\{ |\Psi - m| \geq A\sqrt{m} \right\} \leq \varepsilon/4. \tag{20.11} $$

The local Central Limit Theorem (see, for example, **Durrett (2005)**), or direct approximation via Stirling's formula (A.18) (see Exercise 20.5), implies that, uniformly for $|j| \leq A\sqrt{m}$,

$$ \mathbf{P}\{Y = 2m + j\} \sim \frac{1}{\sqrt{2\pi m}} e^{-j^2/2m}, $$

$$ \mathbf{P}\{\Psi + m = 2m + j\} \sim \frac{1}{\sqrt{2\pi m}} e^{-j^2/2m}. $$

Here we write $a_m \sim b_m$ to mean that the ratio $a_m/b_m$ tends to 1 as $m \to \infty$, uniformly for all $j$ such that $|j| \leq A\sqrt{m}$.

Thus for large $m$ we have

$$ \sum_{|j| \leq A\sqrt{m}} [\mathbf{P}\{Y = 2m + j\} - \mathbf{P}\{\Psi + m = 2m + j\}] $$

$$ \leq \sum_{|j| \leq A\sqrt{m}} \varepsilon \mathbf{P}\{Y = 2m + j\} \leq \varepsilon. $$

Dividing this by 2 and using (20.11) establishes the lemma. $\blacksquare$

**Proof of Theorem 20.3.** (i), *Step 1.* Recall that $N_t$ is the Poisson random variable indicating the number of transitions in the continuous-time chain. We first prove

$$ \|H_t(x,\cdot) - \pi\|_{\mathrm{TV}} \leq \mathbf{P}\{N_t < k\} + \left\| P^k(x,\cdot) - \pi \right\|_{\mathrm{TV}} \, . \tag{20.12} $$

Conditioning on the value of $N_t$ and applying the triangle inequality give

$$ \|H_t(x,\cdot) - \pi\|_{\mathrm{TV}} \leq \sum_{j \geq 0} \mathbf{P}\{N_t = j\} \|P^j(x,\cdot) - \pi\|_{\mathrm{TV}} \, . \tag{20.13} $$

Partitioning the sum on the right into terms with $j < k$ and $j \geq k$, and using the monotonicity of $\|P^j(x,\cdot) - \pi\|_{\mathrm{TV}}$ in $j$ yields (20.12) from (20.13).

*Step 2.* Let $\widetilde{H}_t$ be the continuous-time version of the lazy chain $\widetilde{P}$. The matrix exponentiation of (20.6) shows that

$$ \widetilde{H}_t = e^{t(\widetilde{P}-I)} = e^{t(\frac{P+I}{2}-I)} = e^{\frac{t}{2}(P-I)} = H_{t/2} \, . \tag{20.14} $$

*Step 3.* By (20.12) applied to $\tilde{H}_t$ and (20.14), we have

$$ \left\| H_{t/2}(x,\cdot) - \pi \right\|_{\mathrm{TV}} \leq \left\| \tilde{P}^k(x,\cdot) - \pi \right\|_{\mathrm{TV}} + \mathbf{P}\{N_t < k\} \, . \tag{20.15} $$

Finally, set $t = 2k$ in (20.15) to prove (20.10).

Part (ii).

After the discrete-time chain has been run for $N_m$ steps, running it for another $m$ steps will not increase the distance to $\pi$, so

$$ \|H_m P^m(x,\cdot) - \pi\|_{\mathrm{TV}} \leq \|H_m(x,\cdot) - \pi\|_{\mathrm{TV}} \, . \tag{20.16} $$

### PDF page 300 (book page 284)

(Observe that the matrices $H_m$ and $P^m$ commute.) Now

$$ H_m P^m = \sum_{k \geq 0} \mathbf{P}\{\Psi + m = k\} P^k, $$

$$ \widetilde{P}^{4m} = \sum_{k \geq 0} \mathbf{P}\{Y = k\} P^k, $$

where $\Psi$ is Poisson$(m)$ and $Y$ is binomial$(4m, \frac{1}{2})$. By the triangle inequality,

$$ \|H_m P^m(x, \cdot) - \widetilde{P}^{4m}(x, \cdot)\|_{\mathrm{TV}} \leq \eta_m \,, $$

whence (by (20.16))

$$ \|\widetilde{P}^{4m}(x, \cdot) - \pi\|_{\mathrm{TV}} \leq \|H_m P^m(x, \cdot) - \pi\|_{\mathrm{TV}} + \eta_m $$
$$ \leq \|H_m(x, \cdot) - \pi\|_{\mathrm{TV}} + \eta_m, $$

as needed. $\blacksquare$

## **20.3. Spectral Gap**

Given $f \in \mathbb{R}^{\mathcal{X}}$, the function $H_t f : \mathcal{X} \to \mathbb{R}$ is defined by

$$ (H_t f)(x) := \sum_y H_t(x, y) f(y). $$

The following is a continuous-time version of the inequality (12.8).

**Lemma 20.5.** *Let $P$ be a reversible and irreducible transition matrix with spectral gap $\gamma = 1 - \lambda_2$, and let $H_t$ be the heat-kernel for the corresponding continuous chain, run at rate $r$. For $f \in \mathbb{R}^{\mathcal{X}}$,*

$$ \|H_t f - E_\pi(f)\|_2^2 \leq e^{-2\gamma r t} \operatorname{Var}_\pi(f). $$

*Proof.* First, assume that $E_\pi(f) = 0$. Note that $\frac{d}{dt} e^{tM} = M e^{tM}$, as can be verified from the power series definiton [sic] of the matrix exponential. Since $H_t = e^{rt(P-I)}$,

$$ \frac{d}{dt} H_t f(x) = r(P - I)(H_t f)(x) \,. \tag{20.17} $$

Letting $u(t) := \|H_t f\|_2^2$, from (20.17) it follows that

$$ u'(t) = -2r \sum_{x \in \mathcal{X}} H_t f(x) \cdot (I - P)(H_t f)(x) \cdot \pi(x) $$
$$ = -2r \langle H_t f, (I - P)(H_t f) \rangle_\pi $$
$$ = -2r \mathcal{E}(H_t f). $$

Lemma 13.7 implies that $-2r\mathcal{E}(H_t f) \leq -2r\gamma \|H_t f\|_2^2 = -2r\gamma u(t)$, whence $u'(t) \leq -2r\gamma u(t)$. Integrating $u'(t)/u(t)$, since $u(0) = \|f\|_2^2$, we conclude that

$$ \|H_t f\|_2^2 = u(t) \leq \|f\|_2^2 e^{-2r\gamma t}. $$

If $E_\pi(f) \neq 0$, apply the above result to the function $f - E_\pi(f)$. $\blacksquare$

The following is the continuous-time version of Theorem 12.4.

### PDF page 301 (book page 285)

**Theorem 20.6.** *Let $P$ be an irreducible and reversible transition matrix with spectral gap $\gamma$. Let $H_t$ be the corresponding heat kernel run at rate $r$. Then*

$$ |H_t(x, y) - \pi(y)| \leq \sqrt{\frac{\pi(y)}{\pi(x)}} e^{-\gamma r t}, \tag{20.18} $$

*and so*

$$ t_{\mathrm{mix}}^{\mathrm{cont}}(\varepsilon) \leq \log\left(\frac{1}{\varepsilon \pi_{\min}}\right) \frac{1}{r\gamma}. \tag{20.19} $$

*Proof.* If $f_x(y) = \mathbf{1}_{\{y = x\}} / \pi(x)$, then $H_t f_x(y) = H_t(y, x)/\pi(x)$. The reader should check that $\pi(x) H_t(x, y) = \pi(y) H_t(y, x)$, and so $H_t f_x(y) = H_t f_y(x)$. From Lemma 20.5, since $E_\pi(f_x) = 1$ and $\operatorname{Var}_\pi(f_x) = (1 - \pi(x))/\pi(x)$, we have

$$ \|H_t f_x - 1\|_2^2 \leq e^{-2r\gamma t} \operatorname{Var}_\pi(f_x) \leq \frac{e^{-2r\gamma t}}{\pi(x)}. \tag{20.20} $$

Note that

$$ H_t f_x(y) = \frac{H_t(x, y)}{\pi(y)} = \frac{\sum_{z \in \mathcal{X}} H_{t/2}(x, z) H_{t/2}(z, y)}{\pi(y)} $$
$$ = \sum_{z \in \mathcal{X}} H_{t/2} f_x(z) \cdot H_{t/2} f_z(y) \cdot \pi(z) = \sum_{z \in \mathcal{X}} H_{t/2} f_x(z) \cdot H_{t/2} f_y(z) \cdot \pi(z). $$

Therefore, by Cauchy-Schwarz,

$$ |H_t f_x(y) - 1| = \left| \sum_{z \in \mathcal{X}} \Big[ H_{t/2} f_x(z) - 1 \Big] \Big[ H_{t/2} f_y(z) - 1 \Big] \pi(z) \right| $$
$$ \leq \|H_{t/2} f_x - 1\|_2 \, \|H_{t/2} f_y - 1\|_2. $$

The above with (20.20) shows that

$$ \left| \frac{H_t(x, y)}{\pi(y)} - 1 \right| \leq \frac{e^{-\gamma r t}}{\sqrt{\pi(x)\pi(y)}}. $$

Multiplying by $\pi(y)$ gives (20.18) . Summing over $y$ gives

$$ 2 \|H_t(x, \cdot) - \pi\|_{\mathrm{TV}} \leq e^{-r\gamma t} \sum_{y \in \mathcal{X}} \frac{\pi(y)}{\sqrt{\pi(y)\pi(x)}} \leq \frac{e^{-r\gamma t}}{\pi_{\min}}, \tag{20.21} $$

from which follows (20.19) . $\blacksquare$

## **20.4. Product Chains**

For each $i = 1, \ldots, n$, let $P_i$ be a reversible transition matrix on $\mathcal{X}_i$ with stationary distribution $\pi^{(i)}$. Define $\tilde{P}_i$ to be the lift of $P_i$ to $\mathcal{X} = \prod_{i=1}^{n} \mathcal{X}_i$: for $\boldsymbol{x} = (x^{(1)}, \ldots, x^{(n)}) \in \mathcal{X}$ and $\boldsymbol{y} = (y^{(1)}, \ldots, y^{(n)}) \in \mathcal{X}$,

$$ \tilde{P}_i(\boldsymbol{x}, \boldsymbol{y}) := \begin{cases} P_i(x^{(i)}, y^{(i)}) & \text{if } x^{(j)} = y^{(j)} \text{ for } j \neq i, \\ 0 & \text{otherwise.} \end{cases} \tag{20.22} $$

We consider the continuous-time chain with transition matrix $P := n^{-1} \sum_{i=1}^{n} \tilde{P}_i$.

The following gives good upper and lower bounds on $t_{\mathrm{mix}}(\varepsilon)$ for this product chain.

### PDF page 302 (book page 286)

**Theorem 20.7.** *Suppose, for $i = 1, \ldots, n$, the spectral gap $\gamma_i$ for the chain with reversible transition matrix $P_i$ is bounded below by $\gamma$ and the stationary distribution $\pi^{(i)}$ satisfies $\sqrt{\pi_{\min}^{(i)}} \geq c_0$, for some constant $c_0 > 0$. If $P := n^{-1} \sum_{i=1}^{n} \tilde{P}_i$, where $\tilde{P}_i$ is the matrix defined in (20.22), then the Markov chain with matrix $P$ satisfies*

$$ t_{\mathrm{mix}}^{\mathrm{cont}}(\varepsilon) \leq \frac{1}{2\gamma} n \log n + \frac{1}{\gamma} n \log(1/[c_0 \varepsilon]). \tag{20.23} $$

*If the spectral gap $\gamma_i = \gamma$ for all $i$, then*

$$ t_{\mathrm{mix}}^{\mathrm{cont}}(\varepsilon) \geq \frac{n}{2\gamma} \left\{ \log n - \log \big[ 8 \log\big(1/(1 - \varepsilon)\big) \big] \right\}. \tag{20.24} $$

**Corollary 20.8.** *For a reversible transition matrix $P$ with spectral gap $\gamma$, let $P_{(n)} := \frac{1}{n} \sum_{i=1}^{n} \tilde{P}_i$, where $\tilde{P}_i$ is the transition matrix on $\mathcal{X}^n$ defined by*

$$ \tilde{P}_i(\boldsymbol{x}, \boldsymbol{y}) = P(x^{(i)}, y^{(i)}) \mathbf{1}_{\{x^{(j)} = y^{(j)}, \, j \neq i\}}. $$

*The family of Markov chains with transition matrices $P_{(n)}$ has a cutoff at $\frac{1}{2\gamma} n \log n$.*

To obtain a good upper bound on $d(t)$ for product chains, we need to use a distance which is better suited for product distributions than is the total variation distance. For two distributions $\mu$ and $\nu$ on $\mathcal{X}$, define the **Hellinger affinity** as

$$ I(\mu, \nu) := \sum_{x \in \mathcal{X}} \sqrt{\nu(x)\mu(x)}. \tag{20.25} $$

The **Hellinger distance** is defined as

$$ d_H(\mu, \nu) := \sqrt{2 - 2I(\mu, \nu)}. \tag{20.26} $$

Note also that

$$ d_H(\mu, \nu) = \sqrt{\sum_{x \in \mathcal{X}} \left( \sqrt{\mu(x)} - \sqrt{\nu(x)} \right)^2}. \tag{20.27} $$

The measure $\nu$ **dominates** $\mu$ if $\nu(x) = 0$ implies $\mu(x) = 0$, in which case we write $\mu \ll \nu$. If $\mu \ll \nu$, then we can define $g(x) := \frac{\mu(x)}{\nu(x)} \mathbf{1}_{\{\nu(x) > 0\}}$, and we also have the identity

$$ d_H(\mu, \nu) = \|\sqrt{g} - 1\|_{\ell^2(\nu)}. \tag{20.28} $$

The following lemma shows why the Hellinger distance is useful for product measure.

**Lemma 20.9.** *For measures $\mu^{(i)}$ and $\nu^{(i)}$ on $\mathcal{X}_i$, let $\mu := \prod_{i=1}^{n} \mu^{(i)}$ and $\nu := \prod_{i=1}^{n} \nu^{(i)}$. The Hellinger affinity satisfies*

$$ I(\mu, \nu) = \prod_{i=1}^{n} I(\mu^{(i)}, \nu^{(i)}), $$

*and therefore*

$$ d_H^2(\mu, \nu) \leq \sum_{i=1}^{n} d_H^2(\mu^{(i)}, \nu^{(i)}). \tag{20.29} $$

The proof is left as Exercise 20.7.

We will also need to compare Hellinger with other distances.

### PDF page 303 (book page 287)

LEMMA 20.10. *Let $\mu$ and $\nu$ be probability distributions on $\mathcal{X}$. The total variation distance and Hellinger distance satisfy*

$$ \|\mu - \nu\|_{\mathrm{TV}} \leq d_H(\mu, \nu). \tag{20.30} $$

*If $\mu \ll \nu$, then*

$$ d_H(\mu, \nu) \leq \|g - 1\|_{\ell^2(\nu)}, \tag{20.31} $$

*where $g(x) = \frac{\mu(x)}{\nu(x)} \mathbf{1}_{\{\mu(x) > 0\}}$.*

PROOF. First, observe that

$$ \begin{aligned} \|\mu - \mu\|_{\mathrm{TV}} &= \frac{1}{2} \sum_{x \in \mathcal{X}} |\mu(x) - \nu(x)| \\ &= \frac{1}{2} \sum_{x \in \mathcal{X}} |\sqrt{\mu(x)} - \sqrt{\nu(x)}| \left( \sqrt{\mu(x)} + \sqrt{\nu(x)} \right). \end{aligned} \tag{20.32} $$

By the Cauchy-Schwarz inequality,

$$ \sum_{x \in \mathcal{X}} \left( \sqrt{\mu(x)} + \sqrt{\nu(x)} \right)^2 = 2 + 2 \sum_{x \in \mathcal{X}} \sqrt{\mu(x)\nu(x)} \leq 4. \tag{20.33} $$

Applying Cauchy-Schwarz on the right-hand side of (20.32) and using the bound (20.33) shows that

$$ \|\mu - \nu\|_{\mathrm{TV}}^2 \leq \frac{1}{4} \left[ \sum_{x \in \mathcal{X}} \left( \sqrt{\mu(x)} - \sqrt{\nu(x)} \right)^2 \right] 4 = d_H^2(\mu, \nu). $$

To prove (20.31), use (20.28) and the inequality $(1 - \sqrt{u})^2 \leq (1 - u)^2$, valid for all $u \geq 0$:

$$ d_H(\mu, \nu) = \|\sqrt{g} - 1\|_2 \leq \|g - 1\|_2. $$

$\blacksquare$

We will also make use of the following lemma, useful for obtaining lower bounds. This is the continuous-time version of the bound (12.15) in the proof of Theorem 12.4.

LEMMA 20.11. *Let $P$ be an irreducible reversible transition matrix, and let $H_t$ be the heat kernel of the associated continuous-time Markov chain. If $\lambda$ is an eigenvalue of $P$, then*

$$ \max_{x \in \mathcal{X}} \|H_t(x, \cdot) - \pi\|_{\mathrm{TV}} \geq \frac{1}{2} e^{-(1-\lambda)t}. \tag{20.34} $$

PROOF. Let $f$ be an eigenfunction of $P$ with eigenvalue $\lambda$. We have that

$$ H_t f(x) = \sum_{k=0}^{\infty} e^{-t} \frac{t^k}{k!} P^k f(x) = e^{-t} \sum_{k=0}^{\infty} \frac{(t\lambda)^k}{k!} f(x) = e^{-t(1-\lambda)} f(x). $$

Since $f$ is orthogonal to $\mathbf{1}$, we have $\sum_{y \in \mathcal{X}} f(y)\pi(y) = 0$, whence

$$ \begin{aligned} e^{-t(1-\lambda)} |f(x)| = |H_t f(x)| \\ = \left| \sum_{y \in \mathcal{X}} [H_t(x, y) f(y) - \pi(y) f(y)] \right| \\ \leq \|f\|_\infty 2 \|H_t(x, \cdot) - \pi\|_{\mathrm{TV}}. \end{aligned} $$

### PDF page 304 (book page 288)

Taking $x$ with $f(x) = \|f\|_\infty$ yields (20.34). $\blacksquare$

PROOF OF THEOREM 20.7. *Proof of* (20.23). Let $\boldsymbol{X}_t = (X_t^{(1)}, \ldots, X_t^{(n)})$ be the Markov chain with transition matrix $P$ and heat kernel $H_t$. Note that

$$ H_t = \prod_{i=1}^{n} e^{(t/n)(\tilde{P}_i - I)}, $$

which follows from Exercise 20.4 since $\tilde{P}_i$ and $\tilde{P}_j$ commute. Therefore, for $\boldsymbol{x}, \boldsymbol{y} \in \mathcal{X}$,

$$ \mathbf{P}_{\boldsymbol{x}} \{ \boldsymbol{X}_t = \boldsymbol{y} \} = H_t(\boldsymbol{x}, \boldsymbol{y}) = \prod_{i=1}^{n} e^{(t/n)(\tilde{P}_i - I)}(\boldsymbol{x}, \boldsymbol{y}) = \prod_{i=1}^{n} \mathbf{P}_{\boldsymbol{x}} \{ X_{t/n}^{(i)} = y^{(i)} \}. \tag{20.35} $$

Since (20.35) implies that $H_t(\boldsymbol{x}, \cdot) = \prod_{i=1}^{n} H_{t/n}^{(i)}(x^{(i)}, \cdot)$, by (20.29),

$$ d_H^2(H_t(\boldsymbol{x}, \cdot), \boldsymbol{\pi}) \leq \sum_{i=1}^{n} d_H^2 \left( H_{t/n}^{(i)}(x^{(i)}, \cdot), \ \pi^{(i)} \right). $$

Using (20.30) and (20.31) together with the above inequality shows that

$$ \|H_t(\boldsymbol{x}, \cdot) - \boldsymbol{\pi}\|_{\mathrm{TV}}^2 \leq \sum_{i=1}^{n} \left\| \frac{H_t^{(i)}(x^{(i)}, \cdot)}{\pi^{(i)}} - 1 \right\|_2^2. $$

Combining the above with (20.20) and using the hypotheses of the theorem yields

$$ \|H_t(\boldsymbol{x}, \cdot) - \boldsymbol{\pi}\|_{\mathrm{TV}}^2 \leq \sum_{i=1}^{n} \frac{e^{-2\gamma_i t}}{\pi^{(i)}(x^{(i)})} \leq \frac{n e^{-2\gamma t}}{c_0^2}. $$

In particular,

$$ \|H_t(\boldsymbol{x}, \cdot) - \boldsymbol{\pi}\|_{\mathrm{TV}} \leq \frac{\sqrt{n} e^{-\gamma t}}{c_0}, $$

from which follows (20.23).

*Proof of* (20.24). Pick $x_0^{(i)}$ which maximizes $\left\| H_t^{(i)}(x, \cdot) - \pi^{(i)} \right\|_{\mathrm{TV}}$. From (20.30), it follows that

$$ I \left( H_{t/n}^{(i)}(x_0^{(i)}, \cdot), \ \pi^{(i)} \right) \leq 1 - \frac{1}{2} \left\| H_{t/n}^{(i)}(x_0^{(i)}, \cdot) - \pi^{(i)} \right\|_{\mathrm{TV}}^2. $$

Applying Lemma 20.11 and using the above inequality shows that

$$ I \left( H_{t/n}^{(i)}(x_0^{(i)}, \cdot), \ \pi^{(i)} \right) \leq 1 - \frac{e^{-2\gamma t/n}}{8}. $$

Let $\boldsymbol{x}_0 := \left( x_0^{(1)}, \ldots, x_0^{(n)} \right)$. By Lemma 20.9,

$$ I \left( H_t(\boldsymbol{x}_0, \cdot), \boldsymbol{\pi} \right) \leq \left( 1 - \frac{e^{-2\gamma t/n}}{8} \right)^n. \tag{20.36} $$

Note that by (4.13), for any two distributions $\mu$ and $\nu$,

$$ I(\mu, \nu) = \sum_{x \in \mathcal{X}} \sqrt{\mu(x)\nu(x)} \geq \sum_{x \in \mathcal{X}} \mu(x) \wedge \nu(x) = 1 - \|\mu - \nu\|_{\mathrm{TV}}, $$

and consequently,

$$ \|\mu - \nu\|_{\mathrm{TV}} \geq 1 - I(\mu, \nu). \tag{20.37} $$

### PDF page 305 (book page 289)

Using (20.37) in (20.36) shows that

$$ \|H_t(\boldsymbol{x}_0, \cdot) - \boldsymbol{\pi}\|_{\mathrm{TV}} \geq 1 - \left( 1 - \frac{e^{-2\gamma t/n}}{8} \right)^n. $$

Therefore, if

$$ t < \frac{n}{2\gamma} \left\{ \log n - \log \left[ 8 \log \left( 1/(1 - \varepsilon) \right) \right] \right\}, $$

then

$$ \|H_t(\boldsymbol{x}_0, \cdot) - \boldsymbol{\pi}\|_{\mathrm{TV}} > \varepsilon. $$

That is, (20.24) holds. $\blacksquare$

**Exercises**

EXERCISE 20.1. Prove Theorem 20.1 using Theorem 4.9.
*Hint.* The continuization of the lazy chain $(P + I)/2$ is $H_{t/2}$.

EXERCISE 20.2. Let $H_t$ be the heat kernel corresponding to irreducible transition matrix $P$ with stationary distribution $\pi$. Show that $\|H_t(x, \cdot) - \pi\|_{\mathrm{TV}}$ is non-increasing in $t$.
*Hint:* $H_{t+s} = H_t H_s$.

EXERCISE 20.3. Let $T_1, T_2, \ldots$ be an i.i.d. sequence of exponential random variables of rate $\mu$, let $S_k = \sum_{i=1}^{k} T_i$, and let $N_t = \max\{k : S_k \leq t\}$.
(a) Show that $S_k$ has a gamma distribution with shape parameter $k$ and rate parameter $\mu$, i.e. its density function is

$$ f_k(s) = \frac{\mu^k s^{k-1} e^{-\mu s}}{(k-1)!}. $$

(b) Show by computing $\mathbf{P}\{S_k \leq t < S_{k+1}\}$ that $N_t$ is a Poisson random variable with mean $\mu t$.

EXERCISE 20.4. Show that if $A$ and $B$ are $m \times m$ matrices which commute, then $e^{A+B} = e^A e^B$.

EXERCISE 20.5.
(i) Let $Y$ be a binomial random variable with parameters $4m$ and $1/2$. Show that

$$ \mathbf{P}\{Y = 2m + j\} = \frac{1}{\sqrt{2\pi m}} e^{-j^2/2n} \left[ 1 + \varepsilon_m \right], \tag{20.38} $$

where $\varepsilon_m \to 0$ uniformly for $j/\sqrt{m} \leq A$.
(ii) Let $\Psi$ be Poisson with mean $m$. Prove that $\mathbf{P}\{\Psi + m = 2m + j\}$ is asymptotic in $m$ to the right-hand side of (20.38), again for $j \leq A\sqrt{m}$.

EXERCISE 20.6. Show that if $N_{2k}$ is Poisson$(2k)$, then $\mathbf{P}\{N_{2k} < k\} \leq (e/4)^k$.

EXERCISE 20.7. Show that if $\mu = \prod_{i=1}^{n} \mu_i$ and $\nu = \prod_{i=1}^{n} \nu_i$, then

$$ I(\mu, \nu) = \prod_{i=1}^{n} I(\mu_i, \nu_i), $$

and therefore

$$ d_H^2(\mu, \nu) \leq \sum_{i=1}^{n} d_H^2(\mu_i, \nu_i). $$

### PDF page 306 (book page 290)

**Notes**

To make the estimates in Section 20.2 more quantitative, one needs an estimate of the convergence rate for $\eta_m$ in Lemma 20.4. This can be done in at least three ways:

(1) We could apply a version of Stirling's formula with error bounds (see (A.19)) in conjunction with large deviation estimates for $Y$ and $\Psi$.
(2) We could replace Stirling's formula with a precise version of the local Central Limit Theorem; see e.g. **Spitzer (1976)**.
(3) One can also use Stein's method; see **Chyakanavichyus and Vaĭtkus (2001)** or **Röllin (2007)**.

These methods all show that $\eta_m$ is of order $m^{-1/2}$.

More refined results comparing mixing of continuous time chains to discrete versions were obtained by Chen and Saloff-Coste (**2013**).

Mixing of product chains is studied in **Diaconis and Saloff-Coste (1996b**, Theorem 2.9). See also Barrera, Lachaud, and Ycart (**2006**), who study cutoff for products. Refinements of Theorem 20.7 were given by **Lubetzky and Sly (2014a)** and **Lacoin (2015)**.

The Hellinger distance was used by **Kakutani (1948)** to characterize when two product measures on an infinite product space are singular.

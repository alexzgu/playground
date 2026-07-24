# Appendix D — Solutions to Selected Exercises
*(PDF pages 408–461; book pages 392–445)*

### PDF page 408 (book page 392)

APPENDIX D

# Appendix D — Solutions to Selected Exercises

**Solutions to selected Chapter 1 exercises.**

**1.6.** Fix $x_0$. Define for $k = 0, 1, \ldots, b-1$ the sets
$$ \mathcal{C}_k := \{x \in \mathcal{X} \,:\, P^{mb+k}(x_0, x) > 0 \text{ for some } m\}. \tag{D.1} $$

*Claim:* Each $x$ belongs to only one of the sets $\mathcal{C}_k$.

PROOF. Suppose $P^{mb+k}(x_0, x) > 0$ and $P^{m'b+j}(x_0, x) > 0$. Suppose, without loss of generality, that $j \leq k$. There exists some $r$ such that $P^r(x, x_0) > 0$, whence $r + mb + k \in \mathcal{T}(x_0)$. Therefore, $b$ divides $r + k$. By the same reasoning, $b$ divides $r + j$. Therefore, $b$ must divide $r + k - (r + j) = k - j$. As $j \leq k < b$, it must be that $k = j$. $\blacksquare$

*Claim:* The chain $(X_{bt})_{t=0}^{\infty}$, when started from $x \in \mathcal{C}_k$, is irreducible on $\mathcal{C}_k$.

PROOF. Let $x, y \in \mathcal{C}_k$. There exists $r$ such that $P^r(x, x_0) > 0$. Also, by definition of $\mathcal{C}_k$, there exists $m$ such that $P^{mb+k}(x_0, x) > 0$. Therefore, $r + mb + k \in \mathcal{T}(x_0)$, whence $b$ divides $r + k$. Also, there exists $m'$ such that $P^{m'b+k}(x_0, y) > 0$. Therefore, $P^{r+m'b+k}(x, y) > 0$. Since $b$ divides $r + k$, we have $r + m'b + k = tb$ for some $t$. $\blacksquare$

Suppose that $x \in \mathcal{C}_i$ and $P(x, y) > 0$. By definition, there exists $m$ such that $P^{mb+i}(x_0, y) > 0$. Since
$$ P^{mb+i+1}(x_0, y) \geq P^{mb+i}(x_0, x)P(x, y) > 0, $$
it follows that $y \in \mathcal{C}_{i+1}$.
$\blacksquare$

**1.8.** Observe that
$$
\begin{aligned}
\pi(x)P^2(x, y) &= \pi(x)\sum_{z \in \mathcal{X}} P(x, z)P(z, y) \\
&= \sum_{z \in \mathcal{X}} \pi(z)P(z, x)P(z, y) \\
&= \sum_{z \in \mathcal{X}} \pi(z)P(z, y)P(z, x) \\
&= \sum_{z \in \mathcal{X}} \pi(y)P(y, z)P(z, x) \\
&= \pi(y)\sum_{z \in \mathcal{X}} P(y, z)P(z, x) \\
&= \pi(y)P^2(y, x).
\end{aligned}
$$

### PDF page 409 (book page 393)

Therefore, $\pi$ is the stationary distribution for $P^2$. $\blacksquare$

**1.10.** Let $x_0$ be such that $h(x_0) = \max_{x \in \mathcal{X}} h(x)$. If $x_0 \in B$, then we are done, so assume that $x_0 \notin B$. Since the chain is assumed irreducible, for any $b \in B$, there exists $x_0, x_1, \ldots, x_r = b$ such that $P(x_i, x_{i+1}) > 0$ for $i = 0, 1, \ldots, r-1$. Let $s \leq r$ be the smallest integer such that $x_s \in B$.

We show by induction that $h(x_i) = h(x_0)$ for $i \leq s$. For $i = 0$, this is clearly true. Assume $h(x_j) = h(x_0)$ for some $j < s$. Since $x_j \notin B$ by definition of $s$,
$$ h(x_j) = \sum_{y \in \mathcal{X}} P(x_j, y)h(y) \,. $$
If $h(x_{j+1}) < h(x_0)$, then (since $P(x_j, x_{j+1}) > 0$)
$$ h(x_j) < h(x_0)P(x_j, x_{j+1}) + h(x_0) \sum_{y \neq x_{j+1}} P(x_j, y) = h(x_0) \,. $$
This is a contradiction, and we must have $h(x_{j+1}) = h(x_0)$. This completes the induction, and in particular $h(x_s) = h(x_0)$, and $x_s \in B$. $\blacksquare$

**Solutions to selected Chapter 2 exercises.**

**2.2.** Let $f_k$ be the expected value of the time until our gambler stops playing. Just as for the regular gambler's ruin, the values $f_k$ are related:
$$ f_0 = f_n = 0 \quad \text{and} \quad f_k = \frac{p}{2}(1 + f_{k-1}) + \frac{p}{2}(1 + f_{k+1}) + (1 - p)(1 + f_k). $$
It is easy to check that setting $f_k = k(n - k)/p$ solves this system of equations. (Note that the answer is just what it should be. If she only bets a fraction $p$ of the time, then it should take a factor of $1/p$ longer to reach her final state.) $\blacksquare$

**2.3.** Let $(X_t)$ be a fair random walk on the set $\{0, \ldots, 2n+1\}$, starting at the state $n$ and absorbing at $0$ and $2n + 1$. By Proposition 2.1, the expected time for this walk to be absorbed is $(n + 1)n$.

The walk described in the problem can be viewed as $\min\{X_t, 2n + 1 - X_t\}$. Hence its expected time to absorption is also $(n + 1)n$. $\blacksquare$

**2.5.** For $1 \leq k \leq n - 1$,
$$
\begin{aligned}
\binom{n}{k+1}&P(k+1, k) + \binom{n}{k-1}P(k-1, k) \\
&= \frac{n!}{(k+1)!(n-k-1)!}\frac{k+1}{n} + \frac{n!}{(k-1)!(n-k+1)!}\frac{n-k+1}{n} \\
&= \binom{n-1}{k} + \binom{n-1}{k-1} = \binom{n}{k}.
\end{aligned}
$$
The last combinatorial identity, often called Pascal's identity, follows from splitting the set of $k$-element subsets of a $d$-element set into those which contain a distinguished element and those which do not. Thus if $\pi(k) = 2^{-n}\binom{n}{k}$, then $\pi$ satisfies $\pi(k) = \sum_{x \in \mathcal{X}} \pi(x)P(x, k)$ for $1 \leq k \neq n - 1$.

The boundary cases are as follows:
$$ \sum_{x \in \mathcal{X}} \pi(x)P(x, 0) = \pi(1)P(1, 0) = 2^{-n}\binom{n}{1}\frac{1}{n} = 2^{-n}\binom{n}{0} = \pi(0), $$

### PDF page 410 (book page 394)

and
$$ \sum_{x \in \mathcal{X}} \pi(x)P(x, n) = \pi(n-1)P(n-1, n) = 2^{-n}\binom{n}{n-1}\frac{1}{n} = 2^{-n}\binom{n}{n} = \pi(n) \,. $$

Alternatively, note that the Ehrenfest urn is $H(X_t)$, where $X_t$ is random walk on the $n$-dimensional hypercube, and $H(x)$ is the number of 1's in the vector $x \in \{0, 1\}^n$. Since the $n$-dimensional hypercube is $n$-regular, the uniform probability distribution on the vertex set is stationary. Thus, the stationary measure $\pi$ for the Ehrenfest urn assigns to $k$ mass proportional to the number of vectors $y$ with exactly $k$ 1's. $\blacksquare$

**2.8.** Let $\varphi$ be the function which maps $y \mapsto x$ and preserves $P$. Then
$$ \hat{P}(z, w) = \frac{\pi(w)P(w, z)}{\pi(z)} = \frac{\pi(w)P(\varphi(w), \varphi(z))}{\pi(z)} \,. \tag{D.2} $$
Since $\pi$ is uniform, $\pi(x) = \pi(\varphi(x))$ for all $x$, whence the right-hand side of (D.2) equals
$$ \frac{\pi(\varphi(w))P(\varphi(w), \varphi(z))}{\pi(\varphi(z))} = \hat{P}(\varphi(z), \varphi(w)) \,. $$
$\blacksquare$

**2.10.** Suppose that the reflected walk hits $c$ at or before time $n$. It has probability at least $1/2$ of finishing at time $n$ in $[c, \infty)$. (The probability can be larger than $1/2$ because of the reflecting at $0$.) Thus
$$ \mathbf{P}\left\{\max_{1 \leq j \leq n} |S_j| \geq c\right\}\frac{1}{2} \leq \mathbf{P}\left\{|S_n| \geq c\right\} \,. $$
$\blacksquare$

**Solutions to selected Chapter 3 exercises.**

**3.1.** Fix $x, y \in X$. Suppose first that $\pi(x)\Psi(x, y) \geq \pi(y)\Psi(y, x)$. In this case,
$$ \pi(x)P(x, y) = \pi(x)\Psi(x, y)\frac{\pi(y)\Psi(y, x)}{\pi(x)\Psi(x, y)} = \pi(y)\Psi(y, x). $$
On the other hand, $\pi(y)P(y, x) = \pi(y)\Psi(y, x)$, so
$$ \pi(x)P(x, y) = \pi(y)P(y, x). \tag{D.3} $$
Similarly, if $\pi(x)\Psi(x, y) < \pi(y)\Psi(x, y)$, then $\pi(x)P(x, y) = \pi(x)\Psi(x, y)$. Also,
$$ \pi(y)P(y, x) = \pi(y)\Psi(y, x)\frac{\pi(x)\Psi(x, y)}{\pi(y)\Psi(y, x)} = \pi(x)\Psi(x, y). $$
Therefore, in this case, the detailed balance equation (D.3) is also satisfied. $\blacksquare$

### PDF page 411 (book page 395)

**Solutions to selected Chapter 4 exercises.**

4.1. By Proposition 4.2 and the triangle inequality we have

$$
\begin{aligned}
\left\|\mu P^t - \pi\right\|_{\mathrm{TV}} &= \frac{1}{2} \sum_{y \in \mathcal{X}} |\mu P^t(y) - \pi(y)| \\
&= \frac{1}{2} \sum_{y \in \mathcal{X}} \left| \sum_{x \in \mathcal{X}} \mu(x) P^t(x,y) - \sum_{x \in \mathcal{X}} \mu(x) \pi(y) \right| \\
&\leq \frac{1}{2} \sum_{y \in \mathcal{X}} \sum_{x \in \mathcal{X}} \mu(x) |P^t(x,y) - \pi(y)| \\
&= \sum_{x \in \mathcal{X}} \mu(x) \frac{1}{2} \sum_{y \in \mathcal{X}} |P^t(x,y) - \pi(y)| \\
&= \sum_{x \in \mathcal{X}} \mu(x) \left\| P^t(x,\cdot) - \pi \right\|_{\mathrm{TV}} \\
&\leq \max_{x \in \mathcal{X}} \left\| P^t(x,\cdot) - \pi \right\|_{\mathrm{TV}}.
\end{aligned}
$$

Since this holds for any $\mu$, we have

$$
\sup_\mu \left\|\mu P^t - \pi\right\|_{\mathrm{TV}} \leq \max_{x \in \mathcal{X}} \left\| P^t(x,\cdot) - \pi \right\|_{\mathrm{TV}} = d(t).
$$

The opposite inequality holds, since the set of probabilities on $\mathcal{X}$ includes the point masses.

Similarly, if $\alpha$ and $\beta$ are two probabilities on $\mathcal{X}$, then

$$
\begin{aligned}
\|\alpha P - \beta P\|_{\mathrm{TV}} &= \frac{1}{2} \sum_{z \in \mathcal{X}} \left| \alpha P(z) - \sum_{w \in \mathcal{X}} \beta(w) P(w,z) \right| \\
&\leq \frac{1}{2} \sum_{z \in \mathcal{X}} \sum_{w \in \mathcal{X}} \beta(w) |\alpha P(z) - P(w,z)| \\
&= \sum_{w \in \mathcal{X}} \beta(w) \frac{1}{2} \sum_{z \in \mathcal{X}} |\alpha P(z) - P(w,z)| \\
&= \sum_{w \in \mathcal{X}} \beta(w) \|\alpha P - P(w,\cdot)\|_{\mathrm{TV}} \\
&\leq \max_{w \in \mathcal{X}} \|\alpha P - P(w,\cdot)\|_{\mathrm{TV}}.
\end{aligned}
\tag{D.4}
$$

Thus, applying (D.4) with $\alpha = \mu$ and $\beta = \nu$ gives that

$$
\|\mu P - \nu P\|_{\mathrm{TV}} \leq \max_{y \in \mathcal{X}} \|\mu P - P(y,\cdot)\|_{\mathrm{TV}}.
\tag{D.5}
$$

Applying (D.4) with $\alpha = \delta_y$, where $\delta_y(z) = \mathbf{1}_{\{z=y\}}$, and $\beta = \mu$ shows that

$$
\|\mu P - P(y,\cdot)\|_{\mathrm{TV}} = \|P(y,\cdot) - \mu P\|_{\mathrm{TV}} \leq \max_{x \in \mathcal{X}} \|P(y,\cdot) - P(x,\cdot)\|_{\mathrm{TV}}.
\tag{D.6}
$$

Combining (D.5) with (D.6) shows that

$$
\|\mu P - \nu P\|_{\mathrm{TV}} \leq \max_{x,y \in \mathcal{X}} \|P(x,\cdot) - P(y,\cdot)\|_{\mathrm{TV}}.
$$

$\blacksquare$

### PDF page 412 (book page 396)

4.2. This is a standard exercise in manipulation of sums and inequalities. Apply Proposition 4.2, expand the matrix multiplication, apply the triangle inequality, switch order of summation, and apply Proposition 4.2 once more:

$$
\begin{aligned}
\|\mu P - \nu P\|_{\mathrm{TV}} &= \frac{1}{2} \sum_{x \in \mathcal{X}} |\mu P(x) - \nu P(x)| \\
&= \frac{1}{2} \sum_{x \in \mathcal{X}} \left| \sum_{y \in \mathcal{X}} \mu(y) P(y,x) - \sum_{y \in \mathcal{X}} \nu(y) P(y,x) \right| \\
&= \frac{1}{2} \sum_{x \in \mathcal{X}} \left| \sum_{y \in \mathcal{X}} P(y,x) \left[ \mu(y) - \nu(y) \right] \right| \\
&\leq \frac{1}{2} \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{X}} P(y,x) \left| \mu(y) - \nu(y) \right| \\
&= \frac{1}{2} \sum_{y \in \mathcal{X}} |\mu(y) - \nu(y)| \sum_{x \in \mathcal{X}} P(y,x) \\
&= \frac{1}{2} \sum_{y \in \mathcal{X}} |\mu(y) - \nu(y)| \\
&= \|\mu - \nu\|_{\mathrm{TV}}.
\end{aligned}
$$

$\blacksquare$

4.4. For $i = 1, \ldots, n$, let $\left(X^{(i)}, Y^{(i)}\right)$ be the optimal coupling of $\mu_i$ and $\nu_i$. Let

$$
\begin{aligned}
\boldsymbol{X} &:= (X^{(1)}, \ldots, X^{(n)}), \\
\boldsymbol{Y} &:= (Y^{(1)}, \ldots, Y^{(n)}).
\end{aligned}
$$

Since the distribution of $\boldsymbol{X}$ is $\mu$ and the distribution of $\boldsymbol{Y}$ is $\nu$, the pair $(\boldsymbol{X}, \boldsymbol{Y})$ is a coupling of $\mu$ and $\nu$. Thus

$$
\|\mu - \nu\|_{\mathrm{TV}} \leq \mathbf{P}\{\boldsymbol{X} \neq \boldsymbol{Y}\} \leq \sum_{i=1}^n \mathbf{P}\{X_i \neq Y_i\} = \sum_{i=1}^n \|\mu_i - \nu_i\|_{\mathrm{TV}}.
$$

$\blacksquare$

4.5. Suppose that $p < r$. The function $x \mapsto x^{p/r}$ is concave. By Jensen's Inequality,

$$
\sum_{x \in \mathcal{X}} |f(x)|^p \pi(x) = \sum_{x \in \mathcal{X}} \left( |f(x)|^r \right)^{p/r} \pi(x) \leq \left[ \sum_{x \in \mathcal{X}} |f(x)|^r \pi(x) \right]^{p/r}.
$$

Taking $p$-th roots on both sides show that $\|f\|_p \leq \|f\|_r$. $\blacksquare$

**Solutions to selected Chapter 5 exercises.**

5.1. Consider the following coupling of the chain started from $x$ and the chain started from $\pi$: run the chains independently until the time $\tau$ when they meet, and then run them together. Recall that by aperiodicity and irreducibility, there is some $r$ so that $\alpha := \min_{x,y} P^r(x,y) \geq 0$.

Fix some state $x_0$. Then the probability that both chains, starting from say $x$ and $y$, are not at $x_0$ after $r$ steps is at most $(1 - \alpha^2)$. If the two chains are not at

### PDF page 413 (book page 397)

$x_0$ after these $r$ steps, the probability that they are not both at $x_0$ after another $r$ steps is again $(1 - \alpha^2)$. Continuing in this way, we get that $\mathbf{P}\{\tau > kr\} \leq (1 - \alpha^2)^k$. This shows that $\mathbf{P}\{\tau < \infty\} = 1$. $\blacksquare$

5.2. We show that

$$
\mathbf{P}\{\tau_{\mathrm{couple}} > kt_0\} \leq (1 - \alpha)^k,
\tag{D.7}
$$

from which the conclusion then follows by summing. An *unsuccessful coupling attempt* occurs at trial $j$ if $X_t \neq Y_t$ for all $jt_0 < t \leq (j + 1)t_0$. Since $(X_t, Y_t)$ is a Markovian coupling, so is $(X_{t+jt_0}, Y_{t+jt_0})$ for any $j$, and we can apply the given bound on the probability of not coupling to any length-$t_0$ segment of the trajectories. Hence the probability of an unsuccessful coupling attempt at trial $j$ is at most $(1 - \alpha)$. It follows that the probability that all the first $k$ attempts are unsuccessful is at most $(1 - \alpha)^k$. $\blacksquare$

5.4. If $\tau_i$ is the coupling time of the $i$-th coordinate, we have seen already that $\mathbf{E}(\tau_i) \leq dn^2/4$, so

$$
\mathbf{P}\{\tau_i > dn^2\} \leq \frac{\mathbf{E}(\tau_i)}{dn^2} \leq \frac{1}{4}.
$$

By induction,

$$
\mathbf{P}\{\tau_i > kdn^2\} \leq 4^{-k}.
$$

If $G_i = \{\tau_i > kdn^2\}$, then

$$
\mathbf{P}\left\{ \max_{1 \leq i \leq d} \tau_i > kdn^2 \right\} \leq \mathbf{P}\left( \bigcup_{i=1}^d G_i \right) \leq d4^{-k}.
$$

Taking $k = \lceil \log_4(d/\varepsilon) \rceil$ makes the right-hand side at most $\varepsilon$. Thus

$$
t_{\mathrm{mix}}(\varepsilon) \leq dn^2 \lceil \log_4(d/\varepsilon) \rceil.
$$

$\blacksquare$

**Solutions to selected Chapter 6 exercises.**

6.1. Observe that if $\tau$ is a stopping time and $r$ is a non-random and non-negative integer, then

$$
\{\tau + r = t\} = \{\tau = t - r\} \in \mathcal{F}_{t-r} \subset \mathcal{F}_t.
$$

$\blacksquare$

6.3. Let $\varepsilon := [2(2n - 1)]^{-1}$. Let $\mu(v) = (2n - 1)^{-1}$. For $v \neq v^\star$,

$$
\begin{aligned}
\sum_w \mu(w) P(w,v) &= \sum_{\substack{w \,:\, w \sim v \\ w \neq v}} \frac{1}{(2n-1)} \left[ \frac{1}{2} - \varepsilon \right] \frac{1}{n-1} + \frac{1}{(2n-1)} \left[ \frac{1}{2} + \varepsilon \right] \\
&= \frac{1}{(2n-1)} \left\{ (n-1) \left[ \frac{1}{2} - \varepsilon \right] \frac{1}{n-1} + \left[ \frac{1}{2} + \varepsilon \right] \right\} \\
&= \frac{1}{2n-1}.
\end{aligned}
$$

### PDF page 414 (book page 398)
Also,

$$ \sum_w \mu(w)P(w,v^\star) = (2n-2)\frac{1}{2n-1}\left[\frac{1}{2}-\varepsilon\right]\frac{1}{n-1} + \frac{1}{2n-1}\left(\frac{1}{2n-1}\right) $$
$$ = \frac{1}{2n-1}. $$

$\blacksquare$

**6.6.** By Exercise 6.4,

$$ s(t) = s\left(t_0\frac{t}{t_0}\right) \le s(t_0)^{\lfloor t/t_0\rfloor}. $$

Since $s(t_0) \le \varepsilon$ by hypothesis, applying Lemma 6.16 finishes the solution. $\blacksquare$

**6.7.** By the Monotone Convergence Theorem,

$$ \mathbf{E}\left(\sum_{t=1}^{\tau}|Y_t|\right) = \sum_{t=1}^{\infty}\mathbf{E}\left(|Y_t|\mathbf{1}_{\{\tau\ge t\}}\right). \tag{D.8} $$

Since the event $\{\tau \ge t\}$ is by assumption independent of $Y_t$ and $\mathbf{E}|Y_t| = \mathbf{E}|Y_1|$ for all $t \ge 1$, the right-hand side equals

$$ \sum_{t=1}^{\infty}\mathbf{E}|Y_1|\mathbf{P}\{\tau\ge t\} = \mathbf{E}|Y_1|\sum_{t=1}^{\infty}\mathbf{P}\{\tau\ge t\} = \mathbf{E}|Y_1|\mathbf{E}(\tau) < \infty. \tag{D.9} $$

By the Dominated Convergence Theorem, since

$$ \left|\sum_{t=1}^{\infty}Y_t\mathbf{1}_{\{\tau\ge t\}}\right| \le \sum_{t=1}^{\infty}|Y_t|\mathbf{1}_{\{\tau\ge t\}} $$

and (D.9) shows that the expectation of the non-negative random variable on the right-hand side above is finite,

$$ \mathbf{E}\left(\sum_{t=1}^{\infty}Y_t\mathbf{1}_{\{\tau\ge t\}}\right) = \sum_{t=1}^{\infty}\mathbf{E}(Y_t\mathbf{1}_{\{\tau\ge t\}}) = \mathbf{E}(Y_1)\sum_{t=1}^{\infty}\mathbf{P}\{\tau\ge t\} = \mathbf{E}(Y_1)\mathbf{E}(\tau). $$

Now suppose that $\tau$ is a stopping time. For each $t$,

$$ \{\tau \ge t\} = \{\tau \le t-1\}^c \in \sigma(Y_1,\ldots,Y_{t-1}). \tag{D.10} $$

Since the sequence $(Y_t)$ is i.i.d., (D.10) shows that $\{\tau \ge t\}$ is independent of $Y_t$. $\blacksquare$

**6.8.** Let $A$ be the set of vertices in one of the complete graphs making up $G$. Clearly, $\pi(A) = n/(2n-1) \ge 2^{-1}$.

On the other hand, for $x \notin A$,

$$ P^t(x,A) = 1 - (1-\alpha_n)^t \tag{D.11} $$

where

$$ \alpha_n = \frac{1}{2}\left[1 - \frac{1}{2(n-1)}\right]\frac{1}{n-1} = \frac{1}{2n}\left[1 + o(1)\right]. $$

The total variation distance can be bounded below:

$$ \left\|P^t(x,\cdot) - \pi\right\|_{\mathrm{TV}} \ge \pi(A) - P^t(x,A) \ge (1-\alpha_n)^t - \frac{1}{2}. \tag{D.12} $$

Since

$$ \log(1-\alpha_n)^t \ge t(-\alpha_n - \alpha_n^2/2) $$

### PDF page 415 (book page 399)
and $-1/4 \ge \log(3/4)$, if $t < [4\alpha_n(1-\alpha_n/2)]^{-1}$, then

$$ (1-\alpha_n)^t - \frac{1}{2} \ge \frac{1}{4}. $$

This implies that $t_{\mathrm{mix}}(1/4) \ge \frac{n}{2}\left[1 + o(1)\right]$. $\blacksquare$

**6.10.** Let $\tau$ be the first time all the vertices have been visited at least once, and let $\tau_k$ be the first time that vertex $k$ has been reached. We have

$$
\begin{aligned}
\mathbf{P}_0\{X_\tau = k\} &= \mathbf{P}_0\{X_\tau = k \mid \tau_{k-1} < \tau_{k+1}\}\mathbf{P}_0\{\tau_{k-1} < \tau_{k+1}\} \\
&\quad + \mathbf{P}_0\{X_\tau = k \mid \tau_{k+1} < \tau_{k-1}\}\mathbf{P}_0\{\tau_{k+1} < \tau_{k-1}\} \\
&= \mathbf{P}_{k-1}\{\tau_{k+1} < \tau_k\}\mathbf{P}_0\{\tau_{k-1} < \tau_{k+1}\} \\
&\quad + \mathbf{P}_{k+1}\{\tau_{k-1} < \tau_k\}\mathbf{P}_0\{\tau_{k+1} < \tau_{k-1}\} \\
&= \frac{1}{n-1}\mathbf{P}_0\{\tau_{k-1} < \tau_{k+1}\} + \frac{1}{n-1}\mathbf{P}_0\{\tau_{k+1} < \tau_{k-1}\} \\
&= \frac{1}{n-1}.
\end{aligned}
$$

The identity $\mathbf{P}_{k+1}\{\tau_{k-1} < \tau_k\} = 1/(n-1)$ comes from breaking the cycle at $k$ and using the gambler's ruin on the resulting segment. $\blacksquare$

**6.11.** Setting $t = t_{\mathrm{mix}}$, if $\ell = 7$, then

$$
\frac{1}{\ell t}\sum_{s=1}^{\ell t}\left\|P^t(x,\cdot) - \pi\right\|_{\mathrm{TV}} \le \frac{t + \frac{t}{4} + \frac{t}{4} + \frac{t}{8} + \cdots + \frac{t}{2^{\ell-1}}}{\ell t}
$$
$$
\le \frac{1}{4}\,.
$$

$\blacksquare$

**Solutions to Chapter 7 exercises.**

**7.1.** Let $Y_t^i = 2X_t^i - 1$. Since covariance is bilinear, $\mathrm{Cov}(Y_t^i, Y_t^j) = 4\,\mathrm{Cov}(X_t^i, X_t^j)$ and it is enough to check that $\mathrm{Cov}(Y_t^i, Y_t^j) \le 0$.

If the $i$-th coordinate is chosen in the first $t$ steps, the conditional expectation of $Y_t^i$ is 0. Thus

$$ \mathbf{E}(Y_t^i) = \left(1 - \frac{1}{n}\right)^t. $$

Similarly,

$$ \mathbf{E}(Y_t^i Y_t^j) = \left(1 - \frac{2}{n}\right)^t $$

since we only have a positive contribution if both the coordinates $i, j$ were not chosen in the first $t$ steps. Finally,

$$
\begin{aligned}
\mathrm{Cov}\left(Y_t^i, Y_t^j\right) &= \mathbf{E}\left(Y_t^i Y_t^j\right) - \mathbf{E}\left(Y_t^i\right)\mathbf{E}\left(Y_t^j\right) \\
&= \left(1 - \frac{2}{n}\right)^t - \left(1 - \frac{1}{n}\right)^{2t} \\
&< 0,
\end{aligned}
$$

because $(1 - 2/n) < (1 - 1/n)^2$.

### PDF page 416 (book page 400)
The variance of the sum $W_t = \sum_{i=1}^n X_t^i$ is

$$ \mathrm{Var}(W_t) = \sum_{i=1}^n \mathrm{Var}(X_t^i) + \sum_{i\ne j}\mathrm{Cov}(X_t^i, X_t^j) \le \sum_{i=1}^n \frac{1}{4}. $$

$\blacksquare$

**7.2.**

$$
\begin{aligned}
Q(S, S^c) &= \sum_{x\in S}\sum_{y\in S^c}\pi(x)P(x,y) \\
&= \sum_{y\in S^c}\left[\sum_{x\in\mathcal{X}}\pi(x)P(x,y) - \sum_{x\in S^c}\pi(x)P(x,y)\right] \\
&= \sum_{y\in S^c}\sum_{x\in\mathcal{X}}\pi(x)P(x,y) - \sum_{x\in S^c}\pi(x)\sum_{y\in S^c}P(x,y) \\
&= \sum_{y\in S^c}\pi(y) - \sum_{x\in S^c}\pi(x)\left[1 - \sum_{y\in S}P(x,y)\right] \\
&= \sum_{y\in S^c}\pi(y) - \sum_{x\in S^c}\pi(x) + \sum_{x\in S^c}\sum_{y\in S}\pi(x)P(x,y) \\
&= \sum_{x\in S^c}\sum_{y\in S}\pi(x)P(x,y) \\
&= Q(S^c, S).
\end{aligned}
$$

$\blacksquare$

**7.3.** Let $\{v_1,\ldots,v_n\}$ be the vertex set of the graph, and let $(X_t)$ be the Markov chain started with the initial configuration $\boldsymbol{q}$ in which every vertex has color $q$.

Let $N : \mathcal{X} \to \{0,1,\ldots,n\}$ be the number of sites in the configuration $x$ colored with $q$. That is,

$$ N(x) = \sum_{i=1}^n \mathbf{1}_{\{x(v_i)=q\}}. \tag{D.13} $$

We write $N_t$ for $N(X_t)$.

We compare the mean and variance of the random variable $N$ under the uniform measure $\pi$ and under the measure $P^t(\boldsymbol{q},\cdot)$. (Note that the distribution of $N(X_t)$ equals the distribution of $N$ under $P^t(\boldsymbol{q},\cdot)$.)

The distribution of $N$ under the stationary measure $\pi$ is binomial with parameters $n$ and $1/q$, implying

$$ E_\pi(N) = \frac{n}{q}, \quad \mathrm{Var}_\pi(N) = n\frac{1}{q}\left(1 - \frac{1}{q}\right) \le \frac{n}{4}. $$

Let $X_i(t) = \mathbf{1}_{\{X_t(v_i)=q\}}$, the indicator that vertex $v_i$ has color $q$. Since $X_i(t) = 0$ if and only if vertex $v_i$ has been updated at least once by time $t$ and the latest of these updates is *not* to color $q$, we have

$$ \mathbf{E}_{\boldsymbol{q}}(X_i(t)) = 1 - \left[1 - \left(1 - \frac{1}{n}\right)^t\right]\frac{q-1}{q} = \frac{1}{q} + \frac{q-1}{q}\left(1 - \frac{1}{n}\right)^t $$

### PDF page 417 (book page 401)

and

$$ \mathbf{E}_{\boldsymbol{q}}(N_t) = \frac{n}{q} + \frac{n(q-1)}{q} \left( 1 - \frac{1}{n} \right)^t . $$

Consequently,

$$ \mathbf{E}_{\boldsymbol{q}}(N_t) - E_\pi(N) = \left( \frac{q-1}{q} \right) n \left( 1 - \frac{1}{n} \right)^t . $$

The random variables $\{X_i(t)\}$ are negatively correlated; check that $Y_i = qX_i - (q-1)$ are negatively correlated as in the solution to Exercise 7.1. Thus,

$$ \sigma^2 := \max\{\mathrm{Var}_{\boldsymbol{q}}(N_t), \mathrm{Var}_\pi(N)\} \leq \frac{n}{4}, $$

and

$$ |E_\pi(N) - \mathbf{E}_{\boldsymbol{q}}(N(X_t))| = \frac{n}{2} \left( 1 - \frac{1}{n} \right)^t \geq \sigma \frac{2(q-1)}{q} \sqrt{n} \left( 1 - \frac{1}{n} \right)^t . $$

Letting $r(t) = [2(q-1)/q]\sqrt{n}(1 - n^{-1})^t$,

$$ \begin{aligned} \log(r^2(t)) &= 2t \log(1 - n^{-1}) + \frac{2(q-1)}{q} \log n \\ &\geq 2t \left( -\frac{1}{n} - \frac{1}{2n^2} \right) + \frac{2(q-1)}{q} \log n, \end{aligned} \tag{D.14} $$

where the inequality follows from $\log(1-x) \geq -x - x^2/2$, for $x \geq 0$. As in the proof of Proposition 7.14, it is possible to find a $c(q)$ so that for $t \leq (1/2)n \log n - c(q)n$, the inequality $r^2(t) \geq 32/3$ holds. By Proposition 7.12, $t_{\mathrm{mix}} \geq (1/2)n \log n - c(q)n$. $\blacksquare$

**Solutions to selected Chapter 8 exercises.**

8.1. Given a specific permutation $\eta \in \mathcal{S}_n$, the probability that $\sigma_k(j) = \eta(j)$ for $j = 1, 2, \ldots, k$ is equal to $\prod_{i=0}^{k-1} (n-i)^{-1}$, as can be seen by induction on $k = 1, \ldots, n-1$. $\blacksquare$

8.4.
(a) This is by now a standard application of the parity of permutations. Note that any sequence of moves in which the empty space ends up in the lower right corner must be of even length. Since every move is a single transposition, the permutation of the tiles (including the empty space as a tile) in any such position must be even. However, the desired permutation (switching two adjacent tiles in the bottom row) is odd.
(b) In fact, all even permutations of tiles can be achieved, but it is not entirely trivial to demonstrate. See **Archer (1999)** for an elementary proof and some historical discussion. Zhentao Lee discovered a new and elegant elementary proof during our 2006 MSRI workshop.

$\blacksquare$

8.5. The function $\sigma$ is a permutation if all of the images are distinct, which occurs with probability

$$ p_n := \frac{n!}{n^n}. $$

### PDF page 418 (book page 402)

By Stirling's formula, the expected number of trials needed is asymptotic to

$$ \frac{e^n}{\sqrt{2\pi n}}, $$

since the number of trials needed is geometric with parameter $p_n$. $\blacksquare$

8.6. The proposed method clearly yields a uniform permutation when $n = 1$ or $n = 2$. However, it fails to do so for for [sic] all larger values of $n$. One way to see this is to note that at each stage in the algorithm, there are $n$ options. Hence the probability of each possible permutation must be an integral multiple of $1/n^n$. For $n \geq 3$, $n!$ is not a factor of $n^n$, so no permutation can have probability $1/n!$ of occurring. $\blacksquare$

8.7. False! Consider, for example, the distribution that assigns weight $1/2$ each to the identity and to the permutation that lists the elements of $[n]$ in reverse order. $\blacksquare$

8.8. False! Consider, for example, the distribution that puts weight $1/n$ on all the cyclic shifts of a sorted deck: $123 \ldots n, 23 \ldots n1, \ldots, n12 \ldots n-1$. $\blacksquare$

8.10.
(a) Just as assigning $n$ independent bits is the same as assigning a number chosen uniformly from $\{0, \ldots, 2^n - 1\}$ (as we implicitly argued in the proof of Proposition 8.11), assigning a digit in base $a$ and then a digit in base $b$, is the same as assigning a digit in base $ab$.
(b) To perform a forwards $a$-shuffle, divide the deck into $a$ multinomially-distributed stacks, then uniformly choose an arrangement from all possible permutations that preserve the relative order within each stack. The resulting deck has at most $a$ rising sequences, and there are $a^n$ ways to divide and then riffle together (some of which can lead to identical permutations).

Given a permutation $\pi$ with $r \leq a$ rising sequences, we need to count the number of ways it could possibly arise from a deck divided into $a$ parts. Each rising sequence is a union of stacks, so the rising sequences together determine the positions of $r - 1$ out of the $a - 1$ dividers between stacks. The remaining $a - r$ dividers can be placed in any of the $n + 1$ possible positions, repetition allowed, irrespective of the positions of the $r - 1$ dividers already determined.

For example: set $a = 5$ and let $\pi \in \mathcal{S}_9$ be 152738946. The rising sequences are $(1, 2, 3, 4)$, $(5, 6)$, and $(7, 8, 9)$, so there must be packet divisions between 4 and 5 and between 6 and 7, and two additional dividers must be placed.

This is a standard choosing-with-repetition scenario. We can imagine building a row of length $n + (a - r)$ objects, of which $n$ are numbers and $a - r$ are dividers. There are $\binom{n+a-r}{n}$ such rows.

Since each (division, riffle) pair has probability $1/a^n$, the probability that $\pi$ arises from an $a$-shuffle is exactly $\binom{n+a-r}{n}/a^n$.

$\blacksquare$

**Solutions to selected Chapter 9 exercises.**

9.1. Let $d \geq 2$. Let $U_{-d+1} = 1$, and let

$$ U_{-d+2}, U_{-d+3}, \ldots, U_0, U_1, \ldots, $$

### PDF page 419 (book page 403)

be i.i.d. and uniform on $[0, 1]$. Let $V_1 \leq \cdots \leq V_d$ be the order statistics for $U_{-d+1}, \ldots, U_0$, i.e., $V_j$ is the $j$-th smallest among these variables. Let $V_0 = 0$, and define, for $1 \leq j \leq d$,

$$ A_t^{(j)} := |\{-d + 1 \leq k \leq t\} : V_{j-1} < U_k \leq V_j\}|. $$

Observe that $A_0^{(j)} = 1$ for all $1 \leq j \leq d$.

Consider an urn with initially $d$ balls, each of a different color. At each unit of time, a ball is drawn at random and replaced along with an additional ball of the same color. Let $B_t^{(j)}$ be the number of balls of color $j$ after $t$ draws.

*Claim:* The distribution of $(\{A_t^{(j)}\}_{j=1}^d)$ and $(\{B_t^{(j)}\}_{j=1}^d)$ are the same.

Proof of Claim. Conditioned on the relative positions of $(U_{-d+2}, \ldots, U_t)$, the relative position of $U_{t+1}$ is uniform on all $t + d$ possibilities. Thus the conditional probability that $U_{t+1}$ falls between $V_{j-1}$ and $V_j$ is proportional to the number among $U_0, \ldots, U_t$ which fall in this interval, plus one. Thus, the conditional probability that $A_t^{(j)}$ increases by one equals $A_t^{(j)}/(t + d)$. This shows the transition probabilities for $\{A_t^{(j)}\}_{j=1}^d$ are exactly equal to those for $\{B_t^{(j)}\}_{j=1}^d$. Since they begin with the same initial distribution, their distributions are the same for $t = 0, \ldots, n$. $\blacksquare$

It is clear that the distribution of the $d$-dimensional vector $(A_t^{(1)}, \ldots, A_t^{(d)})$ is uniform over

$$ \left\{ (x_1, \ldots, x_d) : \sum_{i=1}^d x_i = t + d, \ x_i \geq 1, \text{ for } 1 \leq i \leq d \right\}. $$

Construct a flow $\theta$ on the box $\{1, 2, \ldots, n\}^d$ as in the proof of Proposition 9.17 by defining for edges in the lower half of the box

$$ \theta(e) = \mathbf{P}\{\text{Polya's } d\text{-colored process goes thru } e\}. $$

From above, we know that the process is equally likely to pass through each $d$-tuple $\boldsymbol{x}$ with $\sum x_i = k + d$. There are $\binom{k+d-1}{d-1}$ such $d$-tuples, whence each such edge has flow $[\binom{k+d-1}{d-1}]^{-1}$. There are constants $c_1, c_2$ (depending on $d$) such that $c_1 \leq \binom{k+d-1}{d-1}/k^{d-1} \leq c_2$. Therefore, the energy is bounded by

$$ \mathcal{E}(\theta) \leq 2 \sum_{k=1}^{n-1} \binom{k+d-1}{d-1}^{-2} \binom{k+d-1}{d-1} \leq c_3(d) \sum_{k=1}^{n-1} k^{-d+1} \leq c_4(d), $$

the last bound holding only when $d \geq 3$. $\blacksquare$

9.5. In the new network obtained by gluing the two vertices, the voltage function cannot be the same as the voltage in the original network. Thus the corresponding current flow must differ. However, the old current flow remains a flow. By the uniqueness part of Thomson's Principle (Theorem 9.10), the effective resistance must change. $\blacksquare$

9.8. Let $W_1$ be a voltage function for the unit current flow from $x$ to $y$ so that $W_1(x) = \mathcal{R}(x \leftrightarrow y)$ and $W_1(y) = 0$. Let $W_2$ be a voltage function for the unit

### PDF page 420 (book page 404)

current flow from $y$ to $z$ so that $W_2(y) = \mathcal{R}(y \leftrightarrow z)$ and $W_2(z) = 0$. By harmonicity (the maximum principle) at all vertices $v$ we have

$$ 0 \leq W_1(v) \leq \mathcal{R}(x \leftrightarrow y) \tag{D.15} $$

$$ 0 \leq W_2(v) \leq \mathcal{R}(y \leftrightarrow z) \tag{D.16} $$

Recall the hint. Thus $W_3 = W_1 + W_2$ is a voltage function for the unit current flow from $x$ to $z$ and

$$ \mathcal{R}(x \leftrightarrow z) = W_3(x) - W_3(z) = \mathcal{R}(x \leftrightarrow y) + W_2(x) - W_1(z). \tag{D.17} $$

Applying (D.16) gives $W_2(x) \leq \mathcal{R}(y \leftrightarrow z)$ and (D.15) gives $W_1(z) \geq 0$ so finally by (D.17) we get the triangle inequality. $\blacksquare$

**Solutions to selected Chapter 10 exercises.**

10.1. Switiching [sic] the order of summation,

$$ \begin{aligned} \rho P(y) = \sum_{x \in \mathcal{X}} \rho(x) P(x,y) &= \sum_{x \in \mathcal{X}} \sum_{t=0}^{\infty} \mathbf{P}_\mu \left\{ X_t = x, \ \tau \geq t+1 \right\} P(x,y) \\ &= \sum_{t=0}^{\infty} \sum_{x \in \mathcal{X}} \mathbf{P}_\mu \left\{ X_t = x, \ \tau \geq t+1 \right\} P(x,y). \end{aligned} \tag{D.18} $$

Since $\tau$ is a stopping time, the Markov property implies that

$$ \mathbf{P}_\mu \{X_t = x, \, X_{t+1} = y, \, \tau \geq t+1\} = \mathbf{P}_\mu \{X_t = x, \, \tau \geq t+1\} P(x,y). \tag{D.19} $$

Therefore,

$$ \sum_{x \in \mathcal{X}} \mathbf{P}_\mu \{X_t = x, \, \tau \geq t+1\} P(x,y) = \mathbf{P}_\mu \{X_{t+1} = y, \, \tau \geq t+1\}, $$

and the right-hand side of (D.18) equals $\sum_{t=1}^{\infty} \mathbf{P}_\mu \{X_t = y, \, \tau \geq t\}$. Observe that

$$ \begin{aligned} \rho(y) &= \mathbf{P}_\mu \{X_0 = y, \ \tau \geq 1\} + \sum_{t=1}^{\infty} \mathbf{P}_\mu \{X_t = y, \ \tau \geq t\} - \sum_{t=1}^{\infty} \mathbf{P}_\mu \{X_t = y, \ \tau = t\} \\ &= \mathbf{P}_\mu \{X_0 = y, \ \tau \geq 1\} + \sum_{t=1}^{\infty} \mathbf{P}_\mu \{X_t = y, \ \tau \geq t\} - \mathbf{P}_\mu \{X_\tau = y\}. \end{aligned} $$

Since $\tau \geq 1$ always, the first term equals $\mu(y)$. By hypothesis, the final term equals $\nu$. We have shown the middle summation equals $\rho P(y)$, whence we must have

$$ \rho(y) = \mu(y) + \rho P(y) - \nu(y). $$

$\blacksquare$

10.4.
(a) By the Commute Time Identity (Proposition 10.7) and Example 9.7, the value is $2(n-1)(m-h)$.
(b) By (a), these pairs are clearly maximal over all those which are at the same level. If $a$ is at level $m$ and $b$ is at level $h$, where $h < m$, let $c$ be a descendant of $b$ at level $m$. Since every walk from $a$ to $c$ must pass through $b$, we have $\mathbf{E}_a \tau_b \leq \mathbf{E}_a \tau_c$. A similar argument goes through when $a$ is higher than $b$. $\blacksquare$

### PDF page 421 (book page 405)

10.6. Observe that $h_m(k)$ is the mean hitting time from $k$ to 0 in $G_k$, which implies that $h_m(k)$ is monotone increasing in $k$. (This is intuitively clear but harder to prove directly on the cube.) The expected return time from $o$ to itself in the hypercube equals $2^m$ but considering the first step, it also equals $1 + h_m(1)$. Thus

$$ h_m(1) = 2^m - 1. \tag{D.20} $$

To compute $h_m(m)$, use symmetry and the Commute Time Identity. The effective resistance between $0$ and $m$ in $G_m$ is $\mathcal{R}(0 \leftrightarrow m) = \sum_{k=1}^{m} [k\binom{m}{k}]^{-1}$. In this sum all but the first and last terms are negligible: the sum of the other terms is at most $4/m^2$ (check!). Thus

$$ 2h_m(m) = 2\mathcal{R}(0 \leftrightarrow m)|\text{edges}(G_m)| \leq 2\left(\frac{2}{m} + \frac{4}{m^2}\right)(m2^{m-1}), $$

so

$$ h_m(m) \leq 2^m(1 + 2/m). \tag{D.21} $$

Equality (D.20) together with (D.21) and monotonicity concludes the proof. $\blacksquare$

10.8. By Lemma 10.12,

$$ \begin{aligned} 2\mathbf{E}_a(\tau_{bca}) &= [\mathbf{E}_a(\tau_b) + \mathbf{E}_b(\tau_c) + \mathbf{E}_c(\tau_a)] + [\mathbf{E}_a(\tau_c) + \mathbf{E}_c(\tau_b) + \mathbf{E}_b(\tau_a)] \\ &= [\mathbf{E}_a(\tau_b) + \mathbf{E}_b(\tau_a)] + [\mathbf{E}_b(\tau_c) + \mathbf{E}_c(\tau_b)] + [\mathbf{E}_c(\tau_a) + \mathbf{E}_a(\tau_c)]. \end{aligned} $$

Then the conclusion follows from Proposition 10.7. $\blacksquare$

10.9. Taking expectations in (10.48) yields

$$ \mathbf{E}_x(\tau_a) + \mathbf{E}_a(\tau_z) = \mathbf{E}_x(\tau_z) + \mathbf{P}_x\{\tau_z < \tau_a\} \left[ \mathbf{E}_z(\tau_a) + \mathbf{E}_a(\tau_z) \right], $$

which shows that

$$ \mathbf{P}_x\{\tau_z < \tau_a\} = \frac{\mathbf{E}_x(\tau_a) + \mathbf{E}_a(\tau_z) - \mathbf{E}_x(\tau_z)}{\mathbf{E}_z(\tau_a) + \mathbf{E}_a(\tau_z)}, \tag{D.22} $$

without assuming reversibility.

In the reversible case, the cycle identity (Lemma 10.12) yields

$$ \mathbf{E}_x(\tau_a) + \mathbf{E}_a(\tau_z) - \mathbf{E}_x(\tau_z) = \mathbf{E}_a(\tau_x) + \mathbf{E}_z(\tau_a) - \mathbf{E}_z(\tau_x). \tag{D.23} $$

Adding the two sides of (D.23) together establishes that

$$ \begin{aligned} &\mathbf{E}_x(\tau_a) + \mathbf{E}_a(\tau_z) - \mathbf{E}_z(\tau_z) \\ &\qquad = \frac{1}{2} \left\{ [\mathbf{E}_x(\tau_a) + \mathbf{E}_a(\tau_x)] + [\mathbf{E}_a(\tau_z) + \mathbf{E}_z(\tau_a)] - [\mathbf{E}_x(\tau_z) + \mathbf{E}_z(\tau_x)] \right\}. \end{aligned} $$

Let $c_G = \sum_{x \in V} c(x) = 2\sum_e c(e)$, as usual. Then by the Commute Time Identity (Proposition 10.7), the denominator in (D.22) is $c_G \mathcal{R}(a \leftrightarrow z)$ and the numerator is $(1/2)c_G [\mathcal{R}(x \leftrightarrow a) + \mathcal{R}(a \leftrightarrow z) - \mathcal{R}(z \leftrightarrow x)]$. $\blacksquare$

### PDF page 422 (book page 406)

10.10.

$$ \begin{aligned} \sum_{k=0}^{\infty} c_k s^k &= \sum_{k=0}^{\infty} \sum_{j=0}^{k} a_j b_{k-j} s^k \\ &= \sum_{k=0}^{\infty} \sum_{j=0}^{\infty} a_j s^j b_{k-j} s^{k-j} \mathbf{1}_{\{k \geq j\}} \\ &= \sum_{j=0}^{\infty} \sum_{k=0}^{\infty} a^j s^j b_{k-j} s^{k-j} \mathbf{1}_{\{k \geq j\}} \\ &= \sum_{j=0}^{\infty} a^j s^j \sum_{k=0}^{\infty} b_{k-j} s^{k-j} \mathbf{1}_{\{k \geq j\}} \\ &= \sum_{j=0}^{\infty} a^j s^j \sum_{\ell=0}^{\infty} b_\ell s^\ell \\ &= A(s)B(s). \end{aligned} $$

The penultimate equality follows from letting $\ell = k - j$. The reader should check that the change of the order of summation is justified. $\blacksquare$

10.17. Part (a) is the Random Target Lemma. For (b),

$$ (H + D)_{i,j} = \mathbf{E}_i \tau_j^+ = 1 + \sum_\ell P_{i,\ell} H_{j,\ell} = 1 + (PH)_{i,j}. $$

For (c): Suppose that $H\gamma = 0$. Then by (b), if $H\gamma = 0$, then by (b),

$$ D\gamma = \mathbf{1}\mathbf{1}^T \gamma = c_1 \mathbf{1}, $$

whence $\gamma = c_1 \pi^T$. Therefore, $c_1 = 0$ since $H\pi^T > 0$. $\blacksquare$

10.18. Write

$$ \frac{(d-2)}{(j+d-1)\cdots(j+1)} = \frac{1}{(j+1)\cdots(j+d-2)} - \frac{1}{(j+2)\cdots(j+d-1)}. $$

$\blacksquare$

10.19. Let $K$ be the transition matrix defined on the augmented state space in the proof of of [sic] Proposition 10.25(ii).

Let $h_t(\zeta, \omega) = \frac{K^t(\zeta,\omega) - 2\pi_K(\omega)}{\pi_K(\omega)}$, so that $h_t(\zeta, \omega) = h_t(\omega, \zeta)$. Applying Cauchy-Schwarz shows that

$$ \begin{aligned} \left| \frac{K^{2t}(x,y) - 2\pi_K(y)}{\pi_K(y)} \right| &= \left| \sum_\zeta \pi_K(\zeta) h_t(x,\zeta) h_t(\zeta,y) \right| \\ &\leq \sqrt{\sum_\zeta \pi_K(\zeta) h_t(x,\zeta)^2 \sum_\zeta \pi_K(\zeta) h_t(y,\zeta)^2} \\ &= \sqrt{h_{2t}(x,x) h_{2t}(y,y)}. \end{aligned} $$

Since $P^t(x,y) = K^{2t}(x,y)$, dividing by 2 on both sides finishes the proof. $\blacksquare$

### PDF page 423 (book page 407)

**10.21.** Let $\psi : W \to V$ be defined by $\psi(v, i) = v$, and let $\varphi : W \to \{1, 2\}$ be defined by $\varphi(v, i) = i$ for $v \neq v_\star$, and $\varphi(v_\star, i) = 1$.

Given a random walk $(X_t^0)$ on $G$, we show now that a random walk $(X_t)$ can be defined on $H$ satisfying $\psi(X_t) = X_t^0$. Suppose that $(X_s)_{s \leq t}$ has already been defined and that $\varphi(X_t) = i$. If $X_t^0 \neq v_\star$, then define $X_{t+1} = (X_{t+1}^0, i)$. If $X_t^0 = v_\star$, then toss a coin, and define

$$ X_{t+1} = \begin{cases} (X_{t+1}^0, 1) & \text{if heads,} \\ (X_{t+1}^0, 2) & \text{if tails.} \end{cases} $$

We now define a coupling $(X_t, Y_t)$ of two random walks on $H$. Let $(X_t^0, Y_t^0)$ be a coupling of two random walks on $G$. Until time

$$ \tau_{\text{couple}}^G := \min\{t \geq 0 \,:\, X_t^0 = Y_t^0\}, $$

define $(X_t)_{t \leq \tau_{\text{couple}}^G}$ and $(Y_t)_{t \leq \tau_{\text{couple}}^G}$ by lifting the walks $(X_t^0)$ and $(Y_t^0)$ to $H$ via the procedure described above.

If $X_{\tau_{\text{couple}}^G} = Y_{\tau_{\text{couple}}^G}$, then let $(X_t)$ and $(Y_t)$ evolve together for $t \geq \tau_{\text{couple}}^G$.

Suppose, without loss of generality, that $\varphi(X_{\tau_{\text{couple}}^G}) = 1$ and $\varphi(Y_{\tau_{\text{couple}}^G}) = 2$. Until time

$$ \tau_{(v^\star, 1)} := \inf\{t \geq \tau_{\text{couple}}^G \,:\, X_t = (v_\star, 1)\}, $$

couple $(Y_t)$ to $(X_t)$ by setting $Y_t = (\psi(X_t), 2)$. Observe that $\tau_{(v^\star, 1)} = \tau_{\text{couple}}^H$, since $(v_\star, 1)$ is identified with $(v_\star, 2)$. The expected difference $\tau_{\text{couple}}^H - \tau_{\text{couple}}^G$ is bounded by $\max_{x \in G} \mathbf{E}_x(\tau_{v_\star})$, whence for $u, v \in H$,

$$ \mathbf{E}_{u,v}(\tau_{\text{couple}}^H) \leq \mathbf{E}_{\psi(u), \psi(v)}(\tau_{\text{couple}}^G) + \max_{x \in G} \mathbf{E}_x(\tau_{v_\star}). $$

$\blacksquare$

**Solutions to selected Chapter 11 exercises.**

**11.1.**

(a) Use the fact that, since the $B_j$'s partition $B$, $\mathbf{E}(Y \mid B) = \sum_j \mathbf{P}(B_j)\mathbf{E}(Y \mid B_j)$.
(b) Many examples are possible; a small one is $\mathcal{X} = B = \{1, 2, 3\}$, $Y = \mathbf{1}_{\{1,3\}}$, $B_1 = \{1, 2\}$, $B_2 = \{2, 3\}$, $M = 1/2$.

$\blacksquare$

**11.7.** Consider starting at a state $x \in \mathcal{X}$ and running in successive intervals of $t_m$ steps. The probability of states being missed in the first interval is at most $1/2$. If some states are missed in the first interval, then the probability that all are covered by the end of the second interval is at least $1/2$, by the definition of $t_m$. Hence the probability of not covering by time $2t_m$ is at most $1/4$. In general,

$$ \mathbf{P}_x\{\tau_{\text{cov}} > kt_m\} \leq \frac{1}{2^k}. $$

We may conclude that $\tau_{\text{cov}}$ is dominated by $t_m$ times a geometric random variable with success probability $1/2$, and thus $t_{\text{cov}}$ is at most $2t_m$. $\blacksquare$

### PDF page 424 (book page 408)

**Solutions to selected Chapter 12 exercises.**

**12.1.**

(a) For any function $f$,

$$ \|Pf\|_\infty = \max_{x \in \mathcal{X}} \left| \sum_{y \in \mathcal{X}} P(x, y)f(y) \right| \leq \|f\|_\infty. $$

If $P\varphi = \lambda\varphi$, then $\|Pf\|_\infty = |\lambda| \, \|f\|_\infty \leq \|f\|_\infty$. This implies that $|\lambda| \leq 1$.
(c) Assume that $a$ divides $\mathcal{T}(x)$. If $b$ is the gcd of $\mathcal{T}(x)$, then $a$ divides $b$. If $\omega$ is an $a$-th root of unity, then $\omega^b = 1$.

Let $\mathcal{C}_j$ be the subset of $\mathcal{X}$ defined in (D.1), for $j = 0, \ldots, b$. It is shown in the solution to Exercise 1.6 that
(i) there is a unique $j(x) \in \{0, \ldots, b-1\}$ such that $x \in \mathcal{C}_{j(x)}$ and
(ii) if $P(x, y) > 0$, then $j(y) = j(x) \oplus 1$. (Here $\oplus$ is addition modulo $b$.)
Let $f : \mathcal{X} \to \mathbb{C}$ be defined by $f(x) = \omega^{j(x)}$. We have that, for some $\ell \in \mathbb{Z}$,

$$ Pf(x) = \sum_{y \in \mathcal{X}} P(x, y)\omega^{j(y)} = \omega^{j(x) \oplus 1} = \omega^{j(x)+1+\ell b} = \omega\omega^{j(x)} = \omega f(x). $$

Therefore, $f(x)$ is an eigenfunction with eigenvalue $\omega$.

Let $\omega$ be an $a$-th root of unit, and suppose that $\omega f = Pf$ for some $f$. Choose $x$ such that $|f(x)| = r := \max_{y \in \mathcal{X}} |f(y)|$. Since

$$ \omega f(x) = Pf(x) = \sum_{y \in \mathcal{X}} P(x, y)f(y), $$

taking absolute values shows that

$$ r \leq \sum_{y \in \mathcal{X}} P(x, y)|f(y)| \leq r. $$

We conclude that if $P(x, y) > 0$, then $|f(y)| = r$. By irreducibility, $|f(y)| = r$ for all $y \in \mathcal{X}$.

Since the average of complex numbers of norm $r$ has norm $r$ if and only if all the values have the same angle, it follows that $f(y)$ has the same value for all $y$ with $P(x, y) > 0$. Therefore, if $P(x, y) > 0$, then $f(y) = \omega f(x)$. Now fix $x_0 \in \mathcal{X}$ and define for $j = 0, 1, \ldots, k-1$

$$ \mathcal{C}_j = \{z \in \mathcal{X} \,:\, f(z) = \omega^j f(x_0)\}. $$

It is clear that if $P(x, y) > 0$ and $x \in \mathcal{C}_j$, then $x \in \mathcal{C}_{j \oplus 1}$, where $\oplus$ is addition modulo $k$. Also, it is clear that if $t \in \mathcal{T}(x_0)$, then $k$ divides $t$.

$\blacksquare$

**12.3.** Let $f$ be an eigenfunction of $P_L$ with eigenvalue $\mu$. Then

$$ \mu f = P_L f = \frac{Pf + f}{2}. $$

Rearranging shows that $(2\mu - 1)$ is an eigenvalue of $P$. Thus $2\mu - 1 \geq -1$, or equivalently, $\mu \geq 0$. $\blacksquare$

### PDF page 425 (book page 409)

**12.4.** We first observe that $E_\pi(P^t f) = \pi P^t f = \pi f = E_\pi(f)$. Since the first eigenfunction $f_1 \equiv 1$, it follows from (12.5) that $P^t f - E_\pi(P^t f) = \sum_{j=2}^{\mathcal{X}} \langle f, f_j \rangle_\pi f_j \lambda_j^t$. Since the $f_j$'s are an orthonormal basis,

$$ \text{Var}_\pi(f) = \|P^t f - E_\pi(P^t f)\|_{\ell^2(\pi)}^2 = \sum_{j=2}^{|\mathcal{X}|} \langle f, f_j \rangle_\pi^2 \lambda_j^{2t} \leq (1 - \gamma_\star)^{2t} \sum_{j=2}^{|\mathcal{X}|} \langle f, f_j \rangle_\pi^2 \,. $$

We observe that

$$ \sum_{j=2}^{|\mathcal{X}|} \langle f, f_j \rangle_\pi^2 = E_\pi(f^2) - E_\pi^2(f) = \text{Var}_\pi(f). $$

$\blacksquare$

**12.5.** According to (12.2),

$$ \frac{P^{2t+2}(x, x)}{\pi(x)} = \sum_{j=1}^{|\mathcal{X}|} f_j(x)^2 \lambda_j^{2t+2}. $$

Since $\lambda_j^2 \leq 1$ for all $j$, the right-hand side is bounded above by $\sum_{j=1}^{|\mathcal{X}|} f_j(x)^2 \lambda_j^{2t}$, which equals $P^{2t}(x, x)/\pi(x)$. $\blacksquare$

**12.9.** For the upper bound, show that for the strong stationary time $\tau$ in Proposition 8.11,

$$ 2^{-t} \leq \mathbf{P}\{\tau > t\} \leq n^2 2^{-t} \,, $$

and apply Corollary 12.7.

For the lower bound, show that the function giving the distance of card 1 to the middle of the deck is an eigenfunction for the time-reversed chain, with eigenvalue $1/2$. $\blacksquare$

**Solutions to selected Chapter 13 exercises.**

**13.3.** For a directed edge $e = (z, w)$, we define $\nabla f(e) := f(w) - f(z)$. Observe that

$$ 2\tilde{\mathcal{E}}(f) = \sum_{(x,y) \in \tilde{E}} \tilde{Q}(x, y)[f(x) - f(y)]^2 = \sum_{x,y} \tilde{Q}(x, y) \sum_{\Gamma \in \mathcal{P}_{xy}} \nu_{xy}(\Gamma) \left[ \sum_{e \in \Gamma} \nabla f(e) \right]^2 . $$

Applying the Cauchy-Schwarz inequality yields

$$ \begin{aligned} 2\tilde{\mathcal{E}}(f) &\leq \sum_{x,y} \tilde{Q}(x, y) \sum_{\Gamma \in \mathcal{P}_{xy}} \nu_{xy}(\Gamma)|\Gamma| \sum_{e \in \Gamma} [\nabla f(e)]^2 \\ &= \sum_{e \in E} [\nabla f(e)]^2 \sum_{(x,y) \in \tilde{E}} \tilde{Q}(x, y) \sum_{\Gamma : e \in \Gamma \in \mathcal{P}_{xy}} \nu_{xy}(\Gamma)|\Gamma|. \end{aligned} $$

By the definition of the congestion ratio, the right-hand side is bounded above by

$$ \sum_{(z,w) \in E} BQ(z, w)[f(w) - f(z)]^2 = 2B\mathcal{E}(f), $$

completing the proof of (13.14).

The inequality (13.17) follows from Lemma 13.18. $\blacksquare$

### PDF page 426 (book page 410)

**13.4.** We compute the congestion ratio

$$ B := \max_{e \in E} \left( \frac{1}{Q(e)} \sum_{(x,y) \in \tilde{E}} \tilde{Q}(x,y) \sum_{\Gamma : e \in \Gamma \in \mathcal{P}_{xy}} \nu_{xy}(\Gamma)|\Gamma| \right) $$

necessary to apply Corollary 13.23, following the outline of the proof of Corollary 13.24. To get a measure on paths between $b$ and $c$, we write $c = ab$ and give weight $\nu_a(s_1, \ldots, s_k)$ to the path $\Gamma_{bc}$ corresponding to $c = s_1 \cdots s_k b$.

For how many pairs $\{g, h\} \in \tilde{E}$ does a specific $e \in E$ appear in some $\Gamma_{gh}$, and with what weight does it appear? Let $s \in S$ be the generator corresponding to $e$, that is, $e = \{b, sb\}$ for some $b \in G$. For every occurrence of an edge $\{c, sc\}$ using $s$ in some $\Gamma \in \mathcal{P}_a$, where $a \in \tilde{S}$, the edge $e$ appears in the path $\Gamma_{c^{-1}b, ac^{-1}b} \in \mathcal{P}_{c^{-1}b, ac^{-1}b}$. Furthermore, $\nu_{c^{-1}b, ac^{-1}b}(\Gamma_{c^{-1}b, ac^{-1}b}) = \nu_a(\Gamma)$.

Hence the congestion ratio simplifies to

$$ B = \max_{s \in S} \frac{1}{\mu(s)} \sum_{a \in \tilde{S}} \tilde{\mu}(a) \sum_{\Gamma \in \mathcal{P}_a} \nu_a(\Gamma) N(s, \Gamma) |\Gamma|. $$

$\blacksquare$

**13.5.** We bound $\binom{n}{\delta k} \leq n^{\delta k}/(\delta k)!$ and similarly bound $\binom{(1+\delta)k}{\delta k}$. Also, $\binom{n}{k} \geq n^k/k^k$. This gives

$$ \sum_{k=1}^{n/2} \frac{\binom{n}{\delta k}\binom{(1+\delta)k}{\delta k}^2}{\binom{n}{k}} \leq \sum_{k=1}^{n/2} \frac{n^{\delta k}((1+\delta)k)^{2\delta k}k^k}{(\delta k)!^3 n^k}. $$

Recall that for any integer $\ell$ we have $\ell! > (\ell/e)^\ell$, and we bound $(\delta k)!$ by this. We get

$$ \sum_{k=1}^{n/2} \frac{\binom{n}{\delta k}\binom{(1+\delta)k}{\delta k}^2}{\binom{n}{k}} \leq \sum_{k=1}^{\log n} \left( \frac{\log n}{n} \right)^{(1-\delta)k} \left[ \frac{e^3(1+\delta)^2}{\delta^3} \right]^{\delta k} \\ + \sum_{k=\log n}^{n/2} \left( \frac{k}{n} \right)^{(1-\delta)k} \left[ \frac{e^3(1+\delta)^2}{\delta^3} \right]^{\delta k}. $$

The first sum clearly tends to 0 as $n$ tends to $\infty$ for any $\delta \in (0, 1)$. Since $k/n \leq 1/2$ and

$$ (1/2)^{(1-\delta)} \left[ \frac{e^3(1+\delta)^2}{\delta^3} \right]^\delta < 0.8 $$

for $\delta < 0.03$, for any such $\delta$ the second sum tends to 0 as $n$ tends to $\infty$. $\blacksquare$

**Solutions to selected Chapter 14 exercises.**

**14.2.** If $\text{Lip}(f) \leq 1$ and $(X, Y)$ is a coupling of $\mu$ and $\nu$ attaining the minimum in the definition of transportation distance, then

$$ \left| \int f d\mu - \int f d\nu \right| = |\mathbf{E}\left(f(X) - f(Y)\right)| \leq \mathbf{E}\left(\rho(X, Y)\right) = \rho_K(\mu, \nu), $$

where we used $\text{Lip}(f) \leq 1$ for the inequality and the fact that $(X, Y)$ is the optimal coupling for the last equality. $\blacksquare$

### PDF page 427 (book page 411)

**14.3.** Let $x, y$ satisfy $\rho(x, y) = \text{diam}$. Let $(X, Y)$ be the optimal coupling of $P(x, \cdot)$ with $P(y, \cdot)$. Then

$$ \text{diam} - 2 \leq \mathbf{E}(\rho(X, Y)) = \rho_K(P(x, \cdot), P(y, \cdot)) \leq e^{-\alpha}\text{diam}. $$

$\blacksquare$

**14.4.** We proceed by induction. Let $H_j$ be the function defined in the first $j$ steps described above; the domain of $H_j$ is $[j]$. Clearly $H_1$ is uniform on $\mathcal{X}_{k,1}$. Suppose $H_{j-1}$ is uniform on $\mathcal{X}_{k,j-1}$. Let $h \in \mathcal{X}_{k,j}$. Write $h_{j-1}$ for the restriction of $h$ to the domain $[j-1]$. Then

$$ \mathbf{P}\{H_{j-1} = h_{j-1}\} = |\mathcal{X}_{k,j-1}|^{-1}, $$

by the induction hypothesis. Note that

$$ |\mathcal{X}_{k,j}| = (k-1)|\mathcal{X}_{k,j-1}|, $$

since for each element of $\mathcal{X}_{k,j-1}$ there are $k-1$ ways to extend it to an element of $\mathcal{X}_{k,j}$, and every element of $\mathcal{X}_{k,j}$ can be obtained as such an extension. By the construction and the induction hypothesis,

$$ \begin{aligned} \mathbf{P}\{H_j = h\} &= \mathbf{P}\{H_{j-1} = h_{j-1}\}\mathbf{P}\{H_j = h \mid H_{j-1} = h_{j-1}\} \\ &= \frac{1}{|\mathcal{X}_{k,j-1}|}\frac{1}{(k-1)} \\ &= |\mathcal{X}_{k,j}|^{-1}. \end{aligned} $$

$\blacksquare$

**14.5.** This is established by induction. The cases $n = 1$ and $n = 2$ are clear. Suppose it holds for $n \leq k-1$ for some $k \geq 3$. The number of configurations $\omega \in \mathcal{X}_k$ with $\omega(k) = 0$ is the same as the total number of configurations in $\mathcal{X}_{k-1}$. Also, the number of configurations $\omega \in \mathcal{X}_k$ with $\omega(k) = 1$ is the same as the number of configurations in $\mathcal{X}_{k-1}$ having no particle at $k-1$, which is the same as the number of configurations in $\mathcal{X}_{k-2}$. $\blacksquare$

**14.6.** Let $\omega$ be an element of $\mathcal{X}_n$, and let $X$ be the random element of $\mathcal{X}_n$ generated by the algorithm. If $\omega(n) = 1$, then

$$ \mathbf{P}\{X = \omega\} = \frac{1}{f_{n-1}}\left(\frac{f_{n-1}}{f_{n+1}}\right) = \frac{1}{f_{n+1}}. $$

Similarly, if $\omega(n) = 0$, then

$$ \mathbf{P}\{X = \omega\} = \frac{1}{f_n}\left(\frac{f_n}{f_{n+1}}\right) = \frac{1}{f_{n+1}}. $$

$\blacksquare$

**Solutions to selected Chapter 16 exercises.**

**16.2.** By Cauchy-Schwarz, for any permutation $\sigma \in \mathcal{S}_n$ we have

$$ \varphi_\sigma = \sum_{k \in [n]} \varphi(k)\varphi(\sigma(k)) \leq \left( \sum_{k \in [n]} \varphi(k)^2 \right)^{1/2} \left( \sum_{k \in [n]} \varphi(\sigma(k))^2 \right)^{1/2} = \varphi_{\text{id}}. $$

$\blacksquare$

### PDF page 428 (book page 412)

**16.3.** By the half-angle identity $\cos^2 \theta = (\cos(2\theta) + 1)/2$, we have

$$ \sum_{k \in [n]} \cos^2 \left( \frac{(2k-1)\pi}{2n} \right) = \frac{1}{2} \sum_{k \in [n]} \left( \cos \left( \frac{(2k-1)\pi}{n} \right) + 1 \right). $$

Now,

$$ \sum_{k \in [n]} \cos \left( \frac{(2k-1)\pi}{n} \right) = \text{Re}\left( e^{-\pi/n} \sum_{k \in [n]} e^{2k\pi/n} \right) = 0, $$

since the sum of the $n$-th roots of unity is 0. Hence

$$ \sum_{k \in [n]} \cos^2 \left( \frac{(2k-1)\pi}{2n} \right) = \frac{n}{2}. $$

$\blacksquare$

**Solutions to selected Chapter 17 exercises.**

**17.1.** Let $(X_t)$ be simple random walk on $\mathbb{Z}$.

$$ \begin{aligned} M_{t+1} - M_t &= (X_t + \Delta X_t)^3 - 3(t+1)(X_t + \Delta X_t) - X_t^3 + 3tX_t \\ &= 3X_t^2(\Delta X_t) + 3X_t(\Delta X_t)^2 + (\Delta X_t)^3 - 3t(\Delta X_t) - 3X_t - \Delta X_t. \end{aligned} $$

Note that $(\Delta X_t)^2 = 1$, so

$$ M_{t+1} - M_t = (\Delta X_t)(3X_t^2 - 3t), $$

and

$$ \mathbf{E}_k\left(M_{t+1} - M_t \mid X_t\right) = (3X_t^2 - 3t)\mathbf{E}_k(\Delta X_t \mid X_t) = 0. $$

Using the Optional Stopping Theorem,

$$ \begin{aligned} k^3 &= \mathbf{E}_k(M_\tau) \\ &= \mathbf{E}_k\left[\left(X_\tau^3 - 3\tau X_\tau\right)\mathbf{1}_{\{X_\tau = n\}}\right] \\ &= n^3\mathbf{P}_k\{X_\tau = n\} - 3n\mathbf{E}_k\left(\tau\mathbf{1}_{\{X_\tau = n\}}\right). \end{aligned} $$

Dividing through by $kn^{-1} = \mathbf{P}_k\{X_\tau = n\}$ shows that

$$ nk^2 = n^3 - 3n\mathbf{E}_k\left(\tau \mid X_\tau = n\right). $$

Rearranging,

$$ \mathbf{E}_k\left(\tau \mid X_\tau = n\right) = \frac{n^2 - k^2}{3}. $$

The careful reader will notice that we have used the Optional Stopping Theorem without verifying its hypotheses! The application can be justified by applying it to $\tau \wedge B$ and then letting $B \to \infty$ and appealing to the Dominated Convergence Theorem. $\blacksquare$

**17.3.** Suppose that $(X_t)$ is a supermartingale with respect to the sequence $(Y_t)$. Define

$$ A_t = -\sum_{s=1}^{t} \mathbf{E}(X_s - X_{s-1} \mid Y_0, \ldots, Y_{s-1}). $$

Since $A_t$ is a function of $Y_0, \ldots, Y_{t-1}$, it is previsible. The supermartingale property ensures that

$$ A_t - A_{t-1} = -\mathbf{E}(X_t - X_{t-1} \mid Y_0, \ldots, Y_{t-1}) \geq 0, $$

### PDF page 429 (book page 413)

whence the sequence $A_t$ is non-decreasing. Define $M_t := X_t + A_t$. Then

$$
\begin{aligned}
\mathbf{E}(M_{t+1} - M_t \mid Y_0, \ldots, Y_t) &= \mathbf{E}(X_{t+1} - X_t \mid Y_0, \ldots, Y_t) \\
&\quad - \mathbf{E}(\mathbf{E}(X_{t+1} - X_t \mid Y_0, \ldots, Y_t) \mid Y_0, \ldots, Y_t) \\
&= 0.
\end{aligned}
$$

$\blacksquare$

17.4. Using the Doob decomposition, $Z_t = M_t - A_t$, where $(M_t)$ is a martingale with $M_0 = Z_0$ and $(A_t)$ is a previsible and non-decreasing sequence with $A_0 = 0$.

Note that since both $Z_t$ and $A_t$ are non-negative, so is $(M_t)$. Furthermore,

$$
A_{t+1} - A_t = -\mathbf{E}(Z_{t+1} - Z_t \mid \mathcal{F}_t) \leq B,
$$

so

$$
M_{t+1} - M_t \leq Z_{t+1} - Z_t + B \leq 2B.
$$

Since $(A_t)$ is previsible, on the event that $\tau > t$,

$$
\operatorname{Var}(M_{t+1} \mid \mathcal{F}_t) = \operatorname{Var}(Z_{t+1} \mid \mathcal{F}_t) \geq \sigma^2 > 0. \tag{D.24}
$$

Given $h \geq 2B$, consider the stopping time

$$
\tau_h = \min\left\{t \,:\, M_t \geq h\right\} \wedge \tau \wedge u.
$$

Since $\tau_h$ is bounded by $u$, the Optional Stopping Theorem yields

$$
k = \mathbf{E}(M_{\tau_h}) \geq h\mathbf{P}\{M_{\tau_h} \geq h\}.
$$

Rearranging, we have that

$$
\mathbf{P}\{M_{\tau_h} \geq h\} \leq \frac{k}{h}. \tag{D.25}
$$

Let

$$
W_t := M_t^2 - hM_t - \sigma^2 t.
$$

The inequality (D.24) implies that $\mathbf{E}(W_{t+1} \mid \mathcal{F}_t) \geq W_t$ whenever $\tau > t$. That is, $W_{t \wedge \tau}$ is a submartingale. By optional stopping, since $\tau_h$ is bounded and $\tau_h \wedge \tau = \tau_h$,

$$
-kh \leq \mathbf{E}(W_0) \leq \mathbf{E}(W_{\tau_h}) = \mathbf{E}\left(M_{\tau_h}(M_{\tau_h} - h)\right) - \sigma^2 \mathbf{E}(\tau_h).
$$

Since $M_{\tau_h}(M_{\tau_h} - h)$ is non-positive on the event $M_{\tau_h} \leq h$, the right-hand side above is bounded above by

$$
(h + 2B)(2B)\mathbf{P}\{M_{\tau_h} > h\} - \sigma^2 \mathbf{E}(\tau_h) \leq 2h^2 \mathbf{P}\{M_{\tau_h} > h\} - \sigma^2 \mathbf{E}(\tau_h).
$$

Combining these two bounds and using (D.25) shows that $\sigma^2 \mathbf{E}(\tau_h) \leq kh + 2h^2(k/h) = 3kh$. Therefore,

$$
\begin{aligned}
\mathbf{P}\{\tau > u\} &\leq \mathbf{P}\{M_{\tau_h} \geq h\} + \mathbf{P}\{\tau_h \geq u\} \\
&\leq \frac{k}{h} + \frac{3kh}{u\sigma^2},
\end{aligned}
$$

using Markov's inequality and the bound on $\mathbf{E}(\tau_h)$ in the last step.

Optimize by choosing $h = \sqrt{u\sigma^2/3}$, obtaining

$$
\mathbf{P}\{\tau > u\} \leq \frac{2\sqrt{3}k}{\sigma\sqrt{u}} \leq \frac{4k}{\sigma\sqrt{u}}. \tag{D.26}
$$

$\blacksquare$

### PDF page 430 (book page 414)

**Solution to Chapter 18 exercise.**

18.1. First suppose that the chain satisfies (18.26). Then for any $\gamma > 0$, for $n$ large enough,

$$
\begin{aligned}
t_{\mathrm{mix}}(\varepsilon) &\leq (1 + \gamma)t_{\mathrm{mix}}^n, \\
t_{\mathrm{mix}}(1 - \varepsilon) &\geq (1 - \gamma)t_{\mathrm{mix}}^n.
\end{aligned}
$$

Thus

$$
\frac{t_{\mathrm{mix}}(\varepsilon)}{t_{\mathrm{mix}}(1 - \varepsilon)} \leq \frac{1 + \gamma}{1 - \gamma}.
$$

Letting $\gamma \downarrow 0$ shows that (18.3) holds.

Suppose that (18.3) holds. Fix $\gamma > 0$. For any $\varepsilon > 0$, for $n$ large enough, $t_{\mathrm{mix}}(\varepsilon) \leq (1 + \gamma)t_{\mathrm{mix}}^n$. That is, $\lim_{n \to \infty} d_n\left((1 + \gamma)t_{\mathrm{mix}}^n\right) \leq \varepsilon$. Since this holds for all $\varepsilon$,

$$
\lim_{n \to \infty} d_n\left((1 + \gamma)t_{\mathrm{mix}}^n\right) = 0.
$$

Also, $\lim_{n \to \infty} d_n\left((1 - \gamma)t_{\mathrm{mix}}^n\right) \geq 1 - \varepsilon$, since $t_{\mathrm{mix}}(1 - \varepsilon) \geq (1 - \gamma)t_{\mathrm{mix}}^n$ for $n$ sufficiently large. Consequently,

$$
\lim_{n \to \infty} d_n\left((1 - \gamma)t_{\mathrm{mix}}^n\right) = 1.
$$

$\blacksquare$

**Solutions to selected Chapter 20 exercises.**

20.3. The distribution of a sum of $n$ independent exponential random variables with rate $\mu$ has a Gamma distribution with parameters $n$ and $\mu$, so $S_k$ has density

$$
f_k(s) = \frac{\mu^k s^{k-1}e^{-\mu s}}{(k - 1)!}.
$$

Since $S_k$ and $X_{k+1}$ are independent,

$$
\begin{aligned}
\mathbf{P}\{S_k \leq t < S_k + X_{k+1}\} &= \int_0^t \frac{\mu^k s^{k-1}e^{-\mu s}}{(k - 1)!} \int_{t-s}^\infty \mu e^{-\mu x}dx\,ds \\
&= \int_0^t \frac{\mu^k s^{k-1}}{(k - 1)!}e^{-\mu t}ds \\
&= \frac{(\mu t)^k e^{-\mu t}}{k!}.
\end{aligned}
$$

$\blacksquare$

20.4. From the definition of $e^{A+B}$,

$$
e^{A+B} = \sum_{n=0}^\infty \frac{(A + B)^n}{n!}. \tag{D.27}
$$

Since $A$ and $B$ commute, $(A + B)^n$ has a binomial formula:

$$
(A + B)^n = \sum_{k=0}^n \binom{n}{k}A^n B^{n-k}.
$$

Therefore, the left-hand side of (D.27) equals

$$
\sum_{n=0}^\infty \sum_{k=0}^n \frac{A^k}{k!}\frac{B^{n-k}}{(n - k)!} = \sum_{k=0}^\infty \frac{A^k}{k!}\sum_{j=0}^\infty \frac{A^j}{j!} = e^A e^B.
$$

### PDF page 431 (book page 415)

$\blacksquare$

20.7. Let $\mathcal{X} = \prod_{i=1}^n \mathcal{X}_i$. We have

$$
\begin{aligned}
I(\mu, \nu) &= \sum_{\boldsymbol{x} \in \mathcal{X}} \sqrt{\mu(\boldsymbol{x})\nu(\boldsymbol{y})} = \sum_{x_1 \in \mathcal{X}_1} \cdots \sum_{x_n \in \mathcal{X}_n} \sqrt{\prod_{i=1}^n \mu_i(x_i)\prod_{i=1}^n \nu_i(x_i)} \\
&= \left[\sum_{x_1 \in \mathcal{X}_1} \sqrt{\mu_1(x_1)\nu_1(x_1)}\right] \cdots \left[\sum_{x_n \in \mathcal{X}_n} \sqrt{\mu_n(x_n)\nu_n(x_n)}\right] = \prod_{i=1}^n I(\mu_i, \nu_i).
\end{aligned}
$$

$\blacksquare$

**Solutions to selected Chapter 21 exercises.**

21.1. We can write $X_t = x + \sum_{s=1}^t Y_s$, where $x \in \mathcal{X}$ and $(Y_s)_{s=1}^\infty$ is an i.i.d. sequence of $\{-1, 1\}$-valued random variables satisfying

$$
\begin{aligned}
\mathbf{P}\{Y_s = +1\} &= p, \\
\mathbf{P}\{Y_s = -1\} &= q.
\end{aligned}
$$

By the Strong Law, $\mathbf{P}_0\{\lim_{t \to \infty} t^{-1}X_t = (p - q)\} = 1$. In particular,

$$
\mathbf{P}_0\{X_t > (p - q)t/2 \text{ for } t \text{ sufficiently large}\} = 1.
$$

That is, with probability one, there are only finitely many visits of the walker to 0. Since the number of visits to 0 is a geometric random variable with parameter $\mathbf{P}_0\{\tau_0^+ = \infty\}$ (see the proof of Proposition 21.3), this probability must be positive. $\blacksquare$

21.2. Suppose that $\pi(v) = 0$. Since $\pi = \pi P$,

$$
0 = \pi(v) = \sum_{u \in X} \pi(u)P(u, v).
$$

Since all the terms on the right-hand side are non-negative, each is zero. That is, if $P(u, v) > 0$, it must be that $\pi(u) = 0$.

Suppose that there is some $y \in \mathcal{X}$ so that $\pi(y) = 0$. By irreducibility, for any $x \in \mathcal{X}$, there is a sequence $u_0, \ldots, u_t$ so that $u_0 = x$, $u_t = y$, and each $P(u_{i-1}, u_i) > 0$ for $i = 1, \ldots, t$. Then by induction it is easy to see that $\pi(u_i) = 0$ for each of $i = 0, 1, 2, \ldots, t$. Thus $\pi(x) = 0$ for all $x \in \mathcal{X}$, and $\pi$ is not a probability distribution. $\blacksquare$

21.4. If the original graph is regarded as a network with conductances $c(e) = 1$ for all $e$, then the subgraph is also a network, but with $c(e) = 0$ for all edges which are omitted. By Rayleigh's Monotonicity Law, the effective resistance from a fixed vertex $v$ to $\infty$ is not smaller in the subgraph than for the original graph. This together with Proposition 21.6 shows that the subgraph must be recurrent. $\blacksquare$

21.5. This solution is due to Tom Hutchcroft. Since $G$ is infinite, it contains a copy of $\mathbb{Z}^+$. Thus considering the Markov chain on $G^3$ with transition matrix

$$
Q(x_1, y_1, z_1, x_2, y_2, z_2) = P(x_1, y_1)P(x_2, y_2)P(x_3, y_3),
$$

gives a graph which contains a $k$-fuzz (see Exercise 21.3) of simple random walk on $(\mathbb{Z}^+)^3$. Thus it is transient and the sum $\sum_t P^t(x, x)^3$ converges. $\blacksquare$

### PDF page 432 (book page 416)

**21.6.** Define

$$ A_{x,y} = \{t \,:\, P^t(x,y) > 0\}. $$

By aperiodicity, g.c.d.$(A_{x,x}) = 1$. Since $A_{x,x}$ is closed under addition, there is some $t_x$ so that $t \in A_{x,x}$ for $t \geq t_x$. (See Lemma 1.30.) Also, by irreducibility, there is some $s$ so that $P^s(x,y) > 0$. Since

$$ P^{t+s}(x,y) \geq P^t(x,x)P^s(x,y), $$

if $t \geq t_x$, then $t + s \in A_{y,x}$. That is, there exists $t_{x,y}$ such that if $t \geq t_{x,y}$, then $t \in A_{x,y}$.

Let $t_0 = \max\{t_{x,z}, \, t_{y,w}\}$. If $t \geq t_0$, then $P^t(x,z) > 0$ and $P^t(y,w) > 0$. In particular,

$$ P^{t_0}((x,y), \, (z,w)) = P^{t_0}(x,z)P^{t_0}(y,w) > 0. $$

$\blacksquare$

**21.7.** $(X_t)$ is a nearest-neighbor random walk on $\mathbb{Z}^+$ which increases by 1 with probability $\alpha$ and decreases by 1 with probability $\beta = 1 - \alpha$. When the walker is at 0, instead of decreasing with probability $\beta$, it remains at 0. Thus if $\alpha < \beta$, then the chain is a downwardly biased random walk on $\mathbb{Z}^+$, which was shown in Example 21.17 to be positive recurrent.

If $\alpha = \beta$, this is an unbiased random walk on $\mathbb{Z}^+$. This is null recurrent for the same reason that the simple random walk on $\mathbb{Z}$ is null recurrent, shown in Example 21.10.

Consider the network with $V = \mathbb{Z}^+$ and with $c(k, k+1) = r^k$. If $r = p/(1-p)$, then the random walk on the network corresponds to a nearest-neighbor random walk which moves "up" with probability $p$. The effective resistance from 0 to $n$ is

$$ \mathcal{R}(0 \leftrightarrow n) = \sum_{k=1}^{n} r^{-k}. $$

If $p > 1/2$, then $r > 1$ and the right-hand side converges to a finite number, so $\mathcal{R}(0 \leftrightarrow \infty) < \infty$. By Proposition 21.6 this walk is transient. The FIFO queue of this problem is an upwardly biased random walk when $\alpha > \beta$, and thus it is transient as well. $\blacksquare$

**21.8.** Let $r = \alpha/\beta$. Then $\pi(k) = (1 - r)r^k$ for all $k \geq 0$, that is, $\pi$ is the geometric distribution with probability $r$ shifted by 1 to the left. Thus

$$ E_\pi(X + 1) = 1/(1 - r) = \beta/(\beta - \alpha). $$

Since $\mathbf{E}(T \mid X \text{ before arrival}) = (1 + X)/\beta$, we conclude that $\mathbf{E}_\pi(T) = 1/(\beta - \alpha)$. $\blacksquare$

**21.9.** Suppose that $\mu = \mu P$, so that for all $k$,

$$ \mu(k) = \frac{\mu(k - 1) + \mu(k + 1)}{2}. $$

The difference sequence $d(k) = \mu(k) - \mu(k - 1)$ is easily seen to be constant, and hence $\mu$ is not bounded. $\blacksquare$

### PDF page 433 (book page 417)

**Solutions to selected Chapter 22 exercises.**

**22.5.** The measure $\mu$ is a monotone spin system in this ordering: Suppose $v$ is even. Then $\sigma \preceq \tau$ means that $\sigma(w) \geq \tau(w)$ at any neighbor of $w$ of $v$, since $w$ must be odd. Therefore, if a neighbor is occupied in $\tau$, then this neighbor is occupied in $\sigma$ also, and the conditional probability of $v$ being updated to an occupied site is zero in both configurations. If no neighbor is occupied in $\tau$, then it is possible that a neighbor may be occupied in $\sigma$. If so, then $v$ may possibly be updated to an occupied site in $\tau$, but may not be occupied when updated in $\sigma$. In this case, $\sigma'(v) \leq \tau'(v)$, whence $\sigma' \preceq \tau'$, where $(\sigma', \tau')$ are the updated configurations.

Suppose $v$ is odd. Then $\sigma \preceq \tau$ means that $\sigma(w) \leq \tau(w)$ at any (necessarily even) neighbor $w$ of $v$. If a neighbor is occupied in $\sigma$, it will be occupied in $\tau$, and neither configuration can be updated to an occupied $v$. If no neighbor is occupied in $\sigma$, there remains the possibly of an occupied neighbor in $\tau$. Supposing this to be the case, then $\sigma$ may be updated at $v$ to be occupied, while this cannot occur in $\tau$. Thus $\sigma'(v) \geq \tau'(v)$ and therefore $\sigma' \prec \tau'$. $\blacksquare$

**Solutions to selected Chapter 23 exercises.**

**23.2.** Suppose $\sigma \prec \eta$. There is some minimal $k$ and $\ell$ where the inequality in (23.1) is strict. Thus in the $k$-exclusion for $\eta$, there is a particle at $\ell$, while there is a hole in the $k$-exclusion for $\sigma$. There are holes in the $k$-exclusion for $\sigma$ at $\{\ell, \ell + 1, \ldots, r - 1\}$ and a particle at $r$, for some $r$. By making a swap in $\sigma$ at $\{(r - 1), r\}$, a configuration ordered between $\sigma$ and $\eta$ is obtained. Continuing this process eventually leads to $\eta$. $\blacksquare$

**Solutions to selected Chapter 24 exercises.**

**24.1.** Let $(\Xi, \Theta)$ be the optimal coupling of $\mathbf{P}_x\{X_T = \cdot\}$ with $\pi$. Conditioned on $(\Xi, \Theta) = (\xi, \theta)$, run copies of the chain $(X_t^\xi)_{t \geq 0}$ and $(Y_t^\theta)_{t \geq 0}$ independently and started from $(\xi, \theta)$ until they meet, after which run them together. Note that $(X_{T'}^\Xi, Y_{T'}^\Theta)$ is a coupling of $\mathbf{P}_x\{X_{T+T'} = \cdot\}$ with $\pi$. Then

$$ \|\mathbf{P}_x\{X_{T+T'} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \mathbf{P}\{X_{T'}^\Xi \neq Y_{T'}^\Theta\} $$
$$ \leq \mathbf{P}\{\Xi \neq \Theta\} = \|\mathbf{P}_x\{X_T = \cdot\} - \pi\|_{\mathrm{TV}} \,. $$

$\blacksquare$

**24.2.** Note that $Z_{t+1} - Z_t$ and $Z_t$ are independent, and that

$$ \mathbf{P}\{Z_{t+1} = Z_t \mid Z_t\} = \frac{t}{t + 1} \,. $$

For $k \geq 1$,

$$ \mathbf{P}\{Z_{t+1} = Z_t + k \mid Z_t\} = \left(\frac{t}{t+1}\right)^{k-1} \left(\frac{1}{t+1}\right)^2 \,. $$

Since $Z_{t+1} = (Z_{t+1} - Z_t) + Z_t$ and the two terms are independent, Exercise 24.1 finishes the proof. $\blacksquare$

**24.4.** For each $s$, let $U_s$ be a uniform random variable in $\{1, \ldots, s\}$ and $Z_s$ an independent geometric random variable of mean $s$.

We will first show that there exists a positive constant $c_1$ such that

$$ t_{\mathrm{Ces}} \leq c_1 t_{\mathrm{G}}. \tag{D.28} $$

### PDF page 434 (book page 418)

Letting $t = t_{\mathrm{G}}(1/8)$, for all $x$,

$$ \|\mathbf{P}_x\{X_{Z_t} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \frac{1}{8}. \tag{D.29} $$

Note that $\mathbf{P}\{U_{8t} = j\} \leq \frac{1}{8t}$, and so using Exercise 24.3 and then Lemma 24.6 yields

$$ \|\mathbf{P}_x\{X_{U_{8t}} = \cdot\} - \mathbf{P}_x\{X_{U_{8t}+Z_t} = \cdot\}\|_{\mathrm{TV}} $$
$$ \leq \|\mathbf{P}_x\{U_{8t} = \cdot\} - \mathbf{P}_x\{U_{8t} + Z_t = \cdot\}\|_{\mathrm{TV}} \leq \frac{1}{8t}\mathbf{E}(Z_t) = \frac{1}{8}. \tag{D.30} $$

By the triangle inequality for total variation we deduce

$$ \|\mathbf{P}_x\{X_{U_{8t}} = \cdot\} - \pi\|_{\mathrm{TV}} $$
$$ \leq \|\mathbf{P}_x\{X_{U_{8t}} = \cdot\} - \mathbf{P}_x\{X_{U_{8t}+Z_t} = \cdot\}\|_{\mathrm{TV}} + \|\mathbf{P}_x\{X_{U_{8t}+Z_t} = \cdot\} - \pi\|_{\mathrm{TV}} \,. \tag{D.31} $$

From Exercise 24.1 and (D.29) it follows that

$$ \|\mathbf{P}_x\{X_{U_{8t}+Z_t} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \|\mathbf{P}_x\{X_{Z_t} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \frac{1}{8}. \tag{D.32} $$

The bounds (D.30) and (D.32) in (D.31) show that

$$ \|\mathbf{P}_x\{X_{U_{8t}} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \frac{1}{4}, $$

which gives that $t_{\mathrm{Ces}} \leq 8t$. From Corollary 24.17 we get that there exists a constant $c$ such that $t_{\mathrm{G}}(1/8) \leq ct_{\mathrm{G}}$ and this concludes the proof of (D.28).

We will now show that there exists a positive constant $c_2$ such that $t_{\mathrm{G}} \leq c_2 t_{\mathrm{Ces}}$. Let $t = t_{\mathrm{Ces}}$, i.e. for all $x$

$$ \|\mathbf{P}_x\{X_{U_t} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \frac{1}{4}. \tag{D.33} $$

From Lemma 24.6 and Exercise 24.3 we get that

$$ \|\mathbf{P}_x\{X_{Z_{8t}} = \cdot\} - \mathbf{P}_x\{X_{U_t + Z_{8t}} = \cdot\}\|_{\mathrm{TV}} \leq \|\mathbf{P}_x\{Z_{8t} = \cdot\} - \mathbf{P}_x\{Z_{8t} + U_t = \cdot\}\|_{\mathrm{TV}} \leq \frac{1}{8}. $$

So, in the same way as in the proof of (D.28) we obtain

$$ \|\mathbf{P}_x\{X_{Z_{8t}} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \frac{3}{8}. $$

Hence, we deduce that $t_{\mathrm{G}}(3/8) \leq 8t$ and from Corollary 24.17 again there exists a positive constant $c'$ such that $t_{\mathrm{G}} \leq c't_{\mathrm{G}}(3/8)$ and this finishes the proof. $\blacksquare$

**Solutions to selected Appendix B exercises.**

**B.4.** Let $g(y, u)$ be the joint density of $(Y, U_Y)$. Then

$$ f_{Y,U}(y, u) = f_Y(y)f_{U_Y|Y}(u \mid y) $$
$$ = g(y)\mathbf{1}\{g(y) > 0\}\frac{\mathbf{1}\{0 \leq u \leq Cg(y)\}}{Cg(y)} = \frac{1}{C}\mathbf{1}\{g(y) > 0, u \leq Cg(y)\}. \tag{D.34} $$

This is the density for a point $(Y, U)$ drawn from the region under the graph of the function $g$.

### PDF page 435 (book page 419)

Conversely, let $(Y, U)$ be a uniform point from the region under the graph of the function $g$. Its density is the right-hand side of (D.34). The marginal density of $Y$ is

$$ f_Y(y) = \int_{-\infty}^{\infty} \frac{1}{C} \mathbf{1}\{g(y) > 0, u \le Cg(y)\} du = \mathbf{1}\{g(y) > 0\} \frac{1}{C} Cg(y) = g(y). \tag{D.35} $$

$\blacksquare$

B.9. Let $R$ be any region of $TA$. First, note that since $\mathrm{rank}(T) = d$, by the Rank Theorem, $T$ is one-to-one. Consequently, $TT^{-1}R = R$, and

$$ \mathrm{Volume}_d(R) = \mathrm{Volume}_d(TT^{-1}R) = \sqrt{\det(T^t T)}\, \mathrm{Volume}(T^{-1}R), $$

so that $\mathrm{Volume}(T^{-1}R) = \mathrm{Volume}_d(R)/\sqrt{\det(T^t T)}$. To find the distribution of $Y$, we compute

$$ \mathbf{P}\{Y \in R\} = \mathbf{P}\{TX \in R\} = \mathbf{P}\{X \in T^{-1}R\}. \tag{D.36} $$

Since $X$ is uniform, the right-hand side is

$$ \frac{\mathrm{Volume}(T^{-1}R)}{\mathrm{Volume}(A)} = \frac{\mathrm{Volume}_d(R)}{\sqrt{\det(T^t T)}\, \mathrm{Volume}(A)} = \frac{\mathrm{Volume}_d(R)}{\mathrm{Volume}_d(TA)}. \tag{D.37} $$

$\blacksquare$

B.11.

(a) $x \le U_{(k)} \le x + dx$ if and only if among $\{U_1, U_2, \ldots, U_n\}$ exactly $k - 1$ lie to the left of $x$, one is in $[x, x + dx]$, and $n - k$ variables exceed $x + dx$. This occurs with probability

$$ \binom{n}{(k-1), 1, (n-k)} x^{k-1}(1 - x)^{n-k} dx. $$

Thus,

$$
\begin{aligned}
\mathbf{E}\left(U_{(k)}\right) &= \int_0^1 \frac{n!}{(k-1)!(n-k)!} x^k (1 - x)^{n-k} dx \\
&= \frac{n!}{(k-1)!(n-k)!} \frac{(n-k)! k!}{(n+1)!} \\
&= \frac{k}{n+1}.
\end{aligned}
$$

(The integral can be evaluated by observing that the function

$$ x \mapsto \frac{k!(n-k)!}{(n+1)!} x^k (1 - x)^{n-k} $$

is the density for a Beta random variable with parameters $k + 1$ and $n - k + 1$.)

(b) The distribution function for $U_{(n)}$ is

$$ F_n(x) = \mathbf{P}\{U_1 \le x, U_2 \le x, \ldots, U_n \le x\} = \mathbf{P}\{U_1 \le x\}^n = x^n. $$

Differentiating, the density function for $U_{(n)}$ is

$$ f_n(x) = nx^{n-1}. $$

Consequently,

$$ \mathbf{E}\left(U_{(n)}\right) = \int_0^1 xnx^{n-1} dx = \frac{n}{n+1} x^{n+1} \Big|_0^1 = \frac{n}{n+1}. $$

### PDF page 436 (book page 420)

We proceed by induction, showing that

$$ \mathbf{E}\left(U_{(n-k)}\right) = \frac{n - k}{n + 1}. \tag{D.38} $$

We just established the case $k = 0$. Now suppose (D.38) holds for $k = j$. Given $U_{(n-j)}$, the order statistics $U_{(i)}$ for $i = 1, \ldots, n - j - 1$ have the distribution of the order statistics for $n - j - 1$ independent variables uniform on $[0, U_{(n-j)}]$. Thus,

$$ \mathbf{E}\left(U_{(n-j-1)} \mid U_{(n-j)}\right) = U_{(n-j)} \frac{n - j - 1}{n - j}, $$

and so

$$ \mathbf{E}\left(U_{(n-j-1)}\right) = \mathbf{E}\left(\mathbf{E}\left(U_{(n-j-1)} \mid U_{(n-j)}\right)\right) = \mathbf{E}\left(U_{(n-j)}\right) \frac{n - j - 1}{n - j}. $$

Since (D.38) holds for $k = j$ by assumption,

$$ \mathbf{E}\left(U_{(n-j-1)}\right) = \frac{n - j}{n + 1} \frac{n - j - 1}{n - j} = \frac{n - j - 1}{n + 1}. $$

This establishes (D.38) for $j = k$.

(c) The joint density of $(S_1, S_2, \ldots, S_{n+1})$ is $e^{-s_{n+1}} \mathbf{1}_{\{0 < s_1 < \cdots < s_{n+1}\}}$, as can be verified by induction:

$$
\begin{aligned}
f_{S_1, S_2, \ldots, S_{n+1}}(s_1, \ldots, s_{n+1}) &= f_{S_1, S_2, \ldots, S_n}(s_1, \ldots, s_n) f_{S_{n+1} \mid S_1, \ldots, S_n}(s_{n+1} \mid s_1, \ldots, s_n) \\
&= e^{-s_n} \mathbf{1}_{\{0 < s_1 < \cdots < s_n\}} e^{-(s_{n+1} - s_n)} \mathbf{1}_{\{s_n < s_{n+1}\}} \\
&= e^{-s_{n+1}} \mathbf{1}_{\{0 < s_1 < \cdots < s_{n+1}\}}.
\end{aligned}
$$

Because the density of $S_{n+1}$ is $s_{n+1}^n e^{-s_{n+1}}/(n!) \mathbf{1}_{\{s_{n+1} > 0\}}$,

$$ f_{S_1, \ldots, S_n \mid S_{n+1}}(s_1, \ldots, s_n \mid s_{n+1}) = \frac{n!}{s_{n+1}^n} \mathbf{1}_{\{0 < s_1 < \cdots < s_n < s_{n+1}\}}. $$

If $T_k = S_k/S_{n+1}$ for $k = 1, \ldots, n$, then

$$ f_{T_1, \ldots, T_k \mid S_{n+1}}(t_1, \ldots, t_n \mid s_{n+1}) = n! \mathbf{1}_{\{0 < t_1 < \cdots < t_n < 1\}}. $$

Since the right-hand side does not depend on $s_{n+1}$, the vector

$$ \left(\frac{S_1}{S_{n+1}}, \frac{S_2}{S_{n+1}}, \ldots, \frac{S_1}{S_{n+1}}\right) $$

is uniform over the set

$$ \{(x_1, \ldots, x_n) \, : \, x_1 < x_2 < \cdots < x_n\}. $$

$\blacksquare$

B.14. We proceed by induction on $n$. The base case $n = 1$ is clear. Assume that the $(n - 1)$-step algorithm indeed produces a uniformly distributed $\xi_{n-1} \in \Xi_{n-1}^{\mathrm{nr}}$. Extend $\xi_{n-1}$ to $\xi_n$ according to the algorithm, picking one of the three available extensions at random. Note that $|\Xi_n^{\mathrm{nr}}| = 4 \cdot 3^{n-1}$. For $h$ any path in $\Xi_n^{\mathrm{nr}}$, let $h_{n-1}$ be the projection of $h$ to $\Xi_{n-1}^{\mathrm{nr}}$, and observe that

$$
\begin{aligned}
\mathbf{P}\{\xi_n = h\} &= \mathbf{P}\{\xi_n = h \mid \xi_{n-1} = h_{n-1}\} \mathbf{P}\{\xi_{n-1} = h_{n-1}\} \\
&= \frac{1}{3}\left(\frac{1}{4 \cdot 3^{n-2}}\right) = \frac{1}{4 \cdot 3^{n-1}}.
\end{aligned}
$$

$\blacksquare$

### PDF page 437 (book page 421)

B.15. Since the number of self-avoiding walks of length $n$ is clearly bounded by $c_{n,4}$ and our method for generating non-reversing paths is uniform over $\Xi_n^{\mathrm{nr}}$ which has size $4 \cdot 3^{n-1}$, the second part follows from the first.

There are $4(3^3) - 8$ walks of length 4 starting at the origin which are non-reversing and do not return to the origin. At each 4-step stage later in the walk, there are $3^4$ non-reversing paths of length 4, of which six create loops. This establishes (B.26). $\blacksquare$

**Solution to exercise from Appendix C.**

C.1. Define $A_n = n^{-1} \sum_{k=1}^n a_k$. Let $n_k \le m < n_{k+1}$. Then

$$ A_m = \frac{n_k}{m} A_{n_k} + \frac{\sum_{j=n_k+1}^m a_j}{m}. $$

Because $n_k/n_{k+1} \le n_k/m \le 1$, the ratio $n_k/m$ tends to 1. Thus the first term tends to $a$. If $|a_j| \le B$, then the absolute value of the second term is bounded by

$$ B\left(\frac{n_{k+1} - n_k}{n_k}\right) \to 0. $$

Thus $A_m \to a$. $\blacksquare$

### PDF page 438 (book page 422)

# Bibliography

The pages on which a reference appears follow the symbol ↑.

Ahlfors, L. V. 1978. *Complex analysis*, 3rd ed., McGraw-Hill Book Co., New York. An introduction to the theory of analytic functions of one complex variable; International Series in Pure and Applied Mathematics. ↑127

Aldous, D. J. 1982. *Some inequalities for reversible Markov chains*, J. London Math. Soc. (2) **25**, no. 3, 564–576. ↑336, 346

Aldous, D. J. 1983a. *On the time taken by random walks on finite groups to visit every state*, Z. Wahrsch. Verw. Gebiete **62**, no. 3, 361–374. ↑159

Aldous, D. 1983b. *Random walks on finite groups and rapidly mixing Markov chains*, Seminar on probability, XVII, Lecture Notes in Math., vol. 986, Springer, Berlin, pp. 243–297. ↑58, 241

Aldous, D. 1989a. *An introduction to covering problems for random walks on graphs*, J. Theoret. Probab. **2**, no. 1, 87–89. ↑159

Aldous, D. J. 1989b. *Lower bounds for covering times for reversible Markov chains and random walks on graphs*, J. Theoret. Probab. **2**, no. 1, 91–100. ↑159

Aldous, D. 1990. *A random walk construction of uniform spanning trees and uniform labelled trees*, SIAM Journal on Discrete Mathematics **3**, 450–465. ↑358

Aldous, D. J. 1991a. *Random walk covering of some special trees*, J. Math. Anal. Appl. **157**, no. 1, 271–283. ↑158

Aldous, D. J. 1991b. *Threshold limits for cover times*, J. Theoret. Probab. **4**, no. 1, 197–211. ↑159, 278

Aldous, D. 1995. *On simulating a Markov chain stationary distribution when transition probabilities are unknown* (D. Aldous, P. Diaconis, J. Spencer, and J. M. Steele, eds.), IMA Volumes in Mathematics and its Applications, vol. 72, Springer-Verlag. ↑357

Aldous, D. J. 1999. unpublished note. ↑199

Aldous, D. J. 2004, American Institute of Mathematics (AIM) research workshop "Sharp Thresholds for Mixing Times" (Palo Alto, December 2004), available at `http://www.aimath.org/WWN/mixingtimes`. ↑270

Aldous, D. and P. Diaconis. 1986. *Shuffling cards and stopping times*, Amer. Math. Monthly **93**, no. 5, 333–348. ↑58, 87, 96, 113, 114

Aldous, D. and P. Diaconis. 1987. *Strong uniform times and finite random walks*, Adv. in Appl. Math. **8**, no. 1, 69–97. ↑87

Aldous, D. and P. Diaconis. 2002. *The asymmetric one-dimensional constrained Ising model: rigorous results*, J. Statist. Phys. **107**, no. 5-6, 945–975. ↑99

Aldous, D. and J. Fill. 1999. *Reversible Markov chains and random walks on graphs*, available at `http://www.stat.berkeley.edu/~aldous/RWG/book.html`. ↑xv, 19, 58, 142, 149, 150, 159, 359

Aleliunas, R., R. M. Karp, R. J. Lipton, L. Lovász, and C. Rackoff. 1979. *Random walks, universal traversal sequences, and the complexity of maze problems*, 20th Annual Symposium on Foundations of Computer Science (San Juan, Puerto Rico, 1979), IEEE, New York, pp. 218–223. ↑159

Alon, N. 1986. *Eigenvalues and expanders*, Combinatorica **6**, no. 2, 83–96. ↑199

Alon, N. and V. D. Milman. 1985. $\lambda_1$, *isoperimetric inequalities for graphs, and superconcentrators*, J. Combin. Theory Ser. B **38**, no. 1, 73–88. ↑199

Alon, N. and J. H. Spencer. 2008. *The probabilistic method*, 3rd ed., Wiley-Interscience Series in Discrete Mathematics and Optimization, John Wiley & Sons Inc., Hoboken, NJ. With an appendix on the life and work of Paul Erdős. ↑318

### PDF page 439 (book page 423)

Anantharam, V. and P. Tsoucas. 1989. *A proof of the Markov chain tree theorem*, Statistics and Probability Letters **8**, 189–192. ↑358

Angel, O., Y. Peres, and D. B. Wilson. 2008. *Card shuffling and Diophantine approximation*, Ann. Appl. Probab. **18**, no. 3, 1215–1231. ↑

Archer, A. F. 1999. *A modern treatment of the 15 puzzle*, Amer. Math. Monthly **106**, no. 9, 793–799. ↑401

Artin, M. 1991. *Algebra*, Prentice Hall Inc., Englewood Cliffs, NJ. ↑35, 112

Asmussen, S., P. Glynn, and H. Thorisson. 1992. *Stationary detection in the initial transient problem*, ACM Transactions on Modeling and Computer Simulation **2**, 130–157. ↑357

Balázs, M. and Á. Folly. 2016. *An electric network for nonreversible Markov chains*, Amer. Math. Monthly **123**, no. 7, 657–682. ↑149

Barnes, G. and U. Feige. 1996. *Short random walks on graphs*, SIAM J. Discrete Math. **9**, no. 1, 19–28. ↑159

Barlow, M. T. 2017. *Random Walks and Heat Kernels on Graphs*, Cambridge University Press. ↑304

Barlow, M. T., T. Coulhon, and T. Kumagai. 2005. *Characterization of sub-Gaussian heat kernel estimates on strongly recurrent graphs*, Comm. Pure Appl. Math. **58**, no. 12, 1642–1677. ↑304

Barrera, J., B. Lachaud, and B. Ycart. 2006. *Cut-off for n-tuples of exponentially converging processes*, Stochastic Process. Appl. **116**, no. 10, 1433–1446. ↑290

Basharin, G. P., A. N. Langville, and V. A. Naumov. 2004. *The life and work of A. A. Markov*, Linear Algebra Appl. **386**, 3–26. ↑18

Basu, R., J. Hermon, and Y. Peres. 2015. *Characterization of cutoff for reversible Markov chains*, Proceedings of the Twenty-Sixth Annual ACM-SIAM Symposium on Discrete Algorithms, SIAM, Philadelphia, PA, pp. 1774–1791. ↑271

Baxter, J. R. and R. V. Chacon. 1976. *Stopping times for recurrent Markov processes*, Illinois J. Math. **20**, no. 3, 467–475. ↑

Baxter, R. J. 1982. *Exactly Solved Models in Statistical Mechanics*, Academic Press. ↑349

Bayer, D. and P. Diaconis. 1992. *Trailing the dovetail shuffle to its lair*, Ann. Appl. Probab. **2**, no. 2, 294–313. ↑112, 114, 178

Ben-Hamou, A. and J. Salez. 2015. *Cutoff for non-backtracking random walks on sparse random graphs*, Ann. Probab. to appear. ↑271

Benjamin, A. T. and J. J. Quinn. 2003. *Proofs that really count: The art of combinatorial proof*, Dolciani Mathematical Expositions, vol. 27, Math. Assoc. Amer., Washington, D. C. ↑209

Benjamini, I., N. Berger, C. Hoffman, and E. Mossel. 2005. *Mixing times of the biased card shuffling and the asymmetric exclusion process*, Trans. Amer. Math. Soc. **357**, no. 8, 3013–3029 (electronic). ↑334

Berestycki, N., E. Lubetzky, Y. Peres, and A. Sly. 2015. *Random walks on the random graph*, available at `arxiv:1504.01999`. ↑271

Berger, N., C. Kenyon, E. Mossel, and Y. Peres. 2005. *Glauber dynamics on trees and hyperbolic graphs*, Probab. Theory Related Fields **131**, no. 3, 311–340. ↑229

Billingsley, P. 1995. *Probability and measure*, 3rd ed., Wiley Series in Probability and Mathematical Statistics, John Wiley & Sons Inc., New York. ↑363, 369

Borgs, C., J. T. Chayes, A. Frieze, J. H. Kim, P. Tetali, E. Vigoda, and V. H. Vu. 1999. *Torpid mixing of some Monte Carlo Markov chain algorithms in statistical physics*, 40th Annual Symposium on Foundations of Computer Science (New York, 1999), IEEE Computer Soc., Los Alamitos, CA, pp. 218–229, DOI 10.1109/SFFCS.1999.814594. MR1917562 ↑230

Borgs, C., J. T. Chayes, and P. Tetali. 2012. *Tight bounds for mixing of the Swendsen-Wang algorithm at the Potts transition point*, Probab. Theory Related Fields **152**, no. 3-4, 509–557, DOI 10.1007/s00440-010-0329-0. MR2892955 ↑231

Borovkov, A. A. and S. G. Foss. 1992. *Stochastically recursive sequences and their generalizations*, Siberian Advances in Mathematics **2**, 16–81. ↑349

Boczkowski, L., Y. Peres, and P. Sousi. 2016. *Sensitivity of mixing times in Eulerian digraphs*, available at `arxiv:1603.05639`. ↑159

Bodineau, T. 2005. *Slab percolation for the Ising model*, Probab. Theory Related Fields **132**, no. 1, 83–118. ↑230

Bollobás, B. 1988. *The isoperimetric number of random regular graphs*, European J. Combin. **9**, no. 3, 241–244, DOI 10.1016/S0195-6698(88)80014-3. MR947025 ↑200

### PDF page 440 (book page 424)

Bollobás, B. 1998. *Modern graph theory*, Graduate Texts in Mathematics, vol. 184, Springer-Verlag, New York. ↑127

Boucheron, S., G. Lugosi, and P. Massart. 2013. *Concentration inequalities*, Oxford University Press, Oxford. A nonasymptotic theory of independence; With a foreword by Michel Ledoux. ↑200

Brémaud, P. 1999. *Markov chains*, Texts in Applied Mathematics, vol. 31, Springer-Verlag, New York. Gibbs fields, Monte Carlo simulation, and queues. ↑45

Broder, A. 1989. *Generating random spanning trees*, 30th Annual Symposium on Foundations of Computer Science, pp. 442–447. ↑358

Broder, A. Z. and A. R. Karlin. 1989. *Bounds on the cover time*, J. Theoret. Probab. **2**, no. 1, 101–120. ↑159

Bubley, R. and M. Dyer. 1997. *Path coupling: A technique for proving rapid mixing in Markov chains*, Proceedings of the 38th Annual Symposium on Foundations of Computer Science, pp. 223–231. ↑203

Cancrini, N., P. Caputo, and F. Martinelli. 2006. *Relaxation time of L-reversal chains and other chromosome shuffles*, Ann. Appl. Probab. **16**, no. 3, 1506–1527. ↑241

Cancrini, N., F. Martinelli, C. Roberto, and C. Toninelli. 2008. *Kinetically constrained spin models*, Probab. Theory Related Fields **140**, no. 3-4, 459–504. ↑99

Caputo, P., T. M. Liggett, and T. Richthammer. 2010. *Proof of Aldous' spectral gap conjecture*, J. Amer. Math. Soc. **23**, no. 3, 831–851. ↑334, 362

Caputo, P., E. Lubetzky, F. Martinelli, A. Sly, and F. L. Toninelli. 2014. *Dynamics of $(2+1)$-dimensional SOS surfaces above a wall: slow mixing induced by entropic repulsion*, Ann. Probab. **42**, no. 4, 1516–1589. ↑322

Carne, T. K. 1985. *A transmutation formula for Markov chains*, Bull. Sci. Math. (2) **109**, no. 4, 399–405 (English, with French summary). ↑99

Cerf, R. and A. Pisztora. 2000. *On the Wulff crystal in the Ising model*, Ann. Probab. **28**, no. 3, 947–1017. ↑

Cesi, F., G. Guadagni, F. Martinelli, and R. H. Schonmann. 1996. *On the two-dimensional stochastic Ising model in the phase coexistence region near the critical point*, J. Statist. Phys. **85**, no. 1-2, 55–102. ↑230

Chandra, A. K., P. Raghavan, W. L. Ruzzo, R. Smolensky, and P. Tiwari. 1996. *The electrical resistance of a graph captures its commute and cover times*, Comput. Complexity **6**, no. 4, 312–340. Extended abstract originally published in *Proc. 21st ACM Symp. Theory of Computing* (1989) 574–586. ↑149

Chayes, J. T., L. Chayes, and R. H. Schonmann. 1987. *Exponential decay of connectivities in the two-dimensional Ising model*, J. Statist. Phys. **49**, no. 3-4, 433–445. ↑229

Cheeger, J. 1970. *A lower bound for the smallest eigenvalue of the Laplacian*, Problems in analysis (Papers dedicated to Salomon Bochner, 1969), Princeton Univ. Press, Princeton, pp. 195–199. ↑199

Chen, F., L. Lovász, and I. Pak. 1999. *Lifting Markov chains to speed up mixing*, Annual ACM Symposium on Theory of Computing (Atlanta, GA, 1999), ACM, New York, pp. 275–281 (electronic). ↑99

Chen, G.-Y. and L. Saloff-Coste. 2008. *The cutoff phenomenon for ergodic Markov processes*, Electron. J. Probab. **13**, no. 3, 26–78. ↑269

Chen, G.-Y. and L. Saloff-Coste. 2013. *Comparison of cutoffs between lazy walks and Markovian semigroups*, J. Appl. Probab. **50**, no. 4, 943–959. ↑290

Chen, M.-F. 1998. *Trilogy of couplings and general formulas for lower bound of spectral gap*, Probability towards 2000 (New York, 1995), Lecture Notes in Statist., vol. 128, Springer, New York, pp. 123–136. ↑180, 273

Chung, F., P. Diaconis, and R. Graham. 2001. *Combinatorics for the East model*, Adv. in Appl. Math. **27**, no. 1, 192–206. ↑99

Chyakanavichyus, V. and P. Vaïtkus. 2001. *Centered Poisson approximation by the Stein method*, Liet. Mat. Rink. **41**, no. 4, 409–423 (Russian, with Russian and Lithuanian summaries); English transl.,. 2001, Lithuanian Math. J. **41**, no. 4, 319–329. ↑290

Coppersmith, D., U. Feige, and J. Shearer. 1996. *Random walks on regular and irregular graphs*, SIAM J. Discrete Math. **9**, no. 2, 301–308. ↑159

Coppersmith, D., P. Tetali, and P. Winkler. 1993. *Collisions among random walks on a graph*, SIAM J. Discrete Math. **6**, no. 3, 363–374. ↑149

### PDF page 441 (book page 425)
Cox, J. T., Y. Peres, and J. E. Steif. 2016. *Cutoff for the noisy voter model*, Ann. Appl. Probab. **26**, no. 2, 917–932. ↑229

Cuff, P., J. Ding, O. Louidor, E. Lubetzky, Y. Peres, and A. Sly. 2012. *Glauber dynamics for the mean-field Potts model*, J. Stat. Phys. **149**, no. 3, 432–477. ↑231

Dembo, A., J. Ding, J. Miller, and Y. Peres. 2013. *Cut-off for lamplighter chains on tori: dimension interpolation and phase transition*, arXiv preprint arXiv:1312.4522. ↑278

Dembo, A., Y. Peres, J. Rosen, and O. Zeitouni. 2004. *Cover times for Brownian motion and random walk in two dimensions*, Ann. Math. **160**, 433–464. ↑159

Denardo, E. V. 1977. *Periods of connected networks and powers of nonnegative matrices*, Mathematics of Operations Research **2**, no. 1, 20–24. ↑20

Devroye, L. 1986. *Nonuniform random variate generation*, Springer-Verlag, New York. ↑389

Diaconis, P. 1988a. *Group Representations in Probability and Statistics*, Lecture Notes - Monograph Series, vol. 11, Inst. Math. Stat., Hayward, CA. ↑35, 106, 112, 114, 178

Diaconis, P. 1988b. *Applications of noncommutative Fourier analysis to probability problems*, École d'Été de Probabilités de Saint-Flour XV–XVII, 1985–87, Lecture Notes in Math., vol. 1362, Springer, Berlin, pp. 51–100. ↑271

Diaconis, P. 1996. *The cutoff phenomenon in finite Markov chains*, Proc. Nat. Acad. Sci. U.S.A. **93**, no. 4, 1659–1664. ↑

Diaconis, P. 2003. *Mathematical developments from the analysis of riffle shuffling*, Groups, combinatorics & geometry (Durham, 2001), World Sci. Publ., River Edge, NJ, pp. 73–97. ↑114

Diaconis, P. 2013. *Some things we've learned (about Markov chain Monte Carlo)*, Bernoulli **19**, no. 4, 1294–1305. ↑322

Diaconis, P. and J. A. Fill. 1990. *Strong stationary times via a new form of duality*, Ann. Probab. **18**, no. 4, 1483–1522. ↑87, 178, 256, 257, 269

Diaconis, P. and D. Freedman. 1999. *Iterated random functions*, SIAM Review **41**, 45–76. ↑349

Diaconis, P., M. McGrath, and J. Pitman. 1995. *Riffle shuffles, cycles, and descents*, Combinatorica **15**, no. 1, 11–29. ↑114

Diaconis, P. and L. Saloff-Coste. 1993a. *Comparison theorems for reversible Markov chains*, Ann. Appl. Probab. **3**, no. 3, 696–730. ↑199

Diaconis, P. and L. Saloff-Coste. 1993b. *Comparison techniques for random walk on finite groups*, Ann. Probab. **21**, no. 4, 2131–2156. ↑199, 241

Diaconis, P. and L. Saloff-Coste. 1996a. *Nash inequalities for finite Markov chains*, J. Theoret. Probab. **9**, no. 2, 459–510. ↑149

Diaconis, P. and L. Saloff-Coste. 1996b. *Logarithmic Sobolev inequalities for finite Markov chains*, Ann. Appl. Probab. **6**, no. 3, 695–750. ↑290

Diaconis, P. and L. Saloff-Coste. 1996c. *Walks on generating sets of abelian groups*, Probab. Theory Related Fields **105**, no. 3, 393–421. ↑361

Diaconis, P. and L. Saloff-Coste. 1998. *What do we know about the Metropolis algorithm?*, J. Comput. System Sci. **57**, no. 1, 20–36. 27th Annual ACM Symposium on the Theory of Computing (STOC'95) (Las Vegas, NV). ↑45

Diaconis, P. and L. Saloff-Coste. 2006. *Separation cut-offs for birth and death chains*, Ann. Appl. Probab. **16**, no. 4, 2098–2122. ↑269, 271, 362

Diaconis, P. and M. Shahshahani. 1981. *Generating a random permutation with random transpositions*, Z. Wahrsch. Verw. Gebiete **57**, no. 2, 159–179. ↑102, 165, 178, 241

Diaconis, P. and M. Shahshahani. 1987. *Time to reach stationarity in the Bernoulli-Laplace diffusion model*, SIAM J. Math. Anal. **18**, no. 1, 208–218. ↑271

Diaconis, P. and D. Stroock. 1991. *Geometric bounds for eigenvalues of Markov chains*, Ann. Appl. Probab. **1**, no. 1, 36–61. ↑199

Ding, J., J. R. Lee, and Y. Peres. 2012. *Cover times, blanket times, and majorizing measures*, Ann. of Math. (2) **175**, no. 3, 1409–1471. ↑159

Ding, J., E. Lubetzky, and Y. Peres. 2009. *The mixing time evolution of Glauber dynamics for the mean-field Ising model*, Comm. Math. Phys. **289**, no. 2, 725–764. ↑229

Ding, J., E. Lubetzky, and Y. Peres. 2010a. *Total variation cutoff in birth-and-death chains*, Probab. Theory Related Fields **146**, no. 1-2, 61–85. ↑270, 362

Ding, J., E. Lubetzky, and Y. Peres. 2010b. *Mixing time of critical Ising model on trees is polynomial in the height*, Comm. Math. Phys. **295**, no. 1, 161–207. ↑322

### PDF page 442 (book page 426)
Ding, J. and Y. Peres. 2011. *Mixing time for the Ising model: a uniform lower bound for all graphs*, Ann. Inst. Henri Poincaré Probab. Stat. **47**, no. 4, 1020–1028, available at arXiv:0909.5162v2. ↑322, 361

Dobrushin, R., R. Kotecký, and S. Shlosman. 1992. *Wulff construction. A global shape from local interaction*, Translations of Mathematical Monographs, vol. 104, American Mathematical Society, Providence, RI. Translated from the Russian by the authors. ↑230

Dobrushin, R. L. and S. B. Shlosman. 1987. *Completely analytical interactions: constructive description*, J. Statist. Phys. **46**, no. 5-6, 983–1014. ↑230

Doeblin, W. 1938. *Exposé de la théorie des chaînes simple constantes de Markov à un nombre fini d'états*, Rev. Math. Union Interbalkan. **2**, 77–105. ↑74

Doob, J. L. 1953. *Stochastic processes*, John Wiley & Sons Inc., New York. ↑259

Doyle, P. G. and E. J. Snell. 1984. *Random walks and electrical networks*, Carus Math. Monographs, vol. 22, Math. Assoc. Amer., Washington, D. C. ↑127, 302, 304

Doyle, P. G. and J. Steiner. 2011. *Commuting time geometry of ergodic Markov chains*, available at arxiv:1107.2612. ↑149

Dubins, L. E. 1968. *On a theorem of Skorohod*, Ann. Math. Statist. **39**, 2094–2097. ↑87

Dudley, R. M. 2002. *Real analysis and probability*, Cambridge Studies in Advanced Mathematics, vol. 74, Cambridge University Press, Cambridge. Revised reprint of the 1989 original. ↑214

Durrett, R. 2003. *Shuffling chromosomes*, J. Theoret. Probab. **16**, 725–750. ↑236, 241

Durrett, R. 2005. *Probability: theory and examples*, third edition, Brooks/Cole, Belmont, CA. ↑283, 363

Dyer, M., L. A. Goldberg, and M. Jerrum. 2006a. *Dobrushin conditions and systematic scan*, Approximation, randomization and combinatorial optimization, Lecture Notes in Comput. Sci., vol. 4110, Springer, Berlin, pp. 327–338. ↑360

Dyer, M., L. A. Goldberg, and M. Jerrum. 2006b. *Systematic scan for sampling colorings*, Ann. Appl. Probab. **16**, no. 1, 185–230. ↑360

Dyer, M., L. A. Goldberg, M. Jerrum, and R. Martin. 2006. *Markov chain comparison*, Probab. Surv. **3**, 89–111 (electronic). ↑199

Dyer, M. and C. Greenhill. 2000. *On Markov chains for independent sets*, J. Algorithms **35**, no. 1, 17–49. ↑357

Dyer, M., C. Greenhill, and M. Molloy. 2002. *Very rapid mixing of the Glauber dynamics for proper colorings on bounded-degree graphs*, Random Structures Algorithms **20**, no. 1, 98–114. ↑214

Dyer, M., C. Greenhill, and M. Ullrich. 2014. *Structure and eigenvalues of heat-bath Markov chains*, Linear Algebra Appl. **454**, 57–71, DOI 10.1016/j.laa.2014.04.018. ↑178

Eggenberger, F. and G Pólya. 1923. *Über die Statistik vorketter vorgänge*, Zeit. Angew. Math. Mech. **3**, 279–289. ↑35

Elias, P. 1972. *The efficient construction of an unbiased random sequence*, Ann. Math. Statist. **43**, 865–870. ↑389

Einstein, A. 1934. *On the method of theoretical physics*, Philosophy of Science **1**, no. 2, 163–169. ↑1

Erdős, P. and A. Rényi. 1961. *On a classical problem of probability theory*, Magyar Tud. Akad. Mat. Kutató Int. Közl. **6**, 215–220 (English, with Russian summary). ↑35

Feige, U. 1995a. *A tight lower bound on the cover time for random walks on graphs*, Random Structures Algorithms **6**, no. 4, 433–438. ↑159

Feige, U. 1995b. *A tight upper bound on the cover time for random walks on graphs*, Random Structures Algorithms **6**, no. 1, 51–54. ↑

Feige, U. 1997. *Collecting coupons on trees, and the cover time of random walks*, Comput. Complexity **6**, no. 4, 341–356. ↑159

Feller, W. 1968. *An introduction to probability theory and its applications*, third edition, Vol. 1, Wiley, New York. ↑19, 35, 178, 304, 363

Fill, J. A. 1991. *Eigenvalue bounds on convergence to stationarity for nonreversible Markov chains, with an application to the exclusion process*, Ann. Appl. Probab. **1**, no. 1, 62–87. ↑99

Fill, J. A. 1998. *An interruptible algorithm for perfect sampling via Markov chains*, Annals of Applied Probability **8**, 131–162. ↑349, 354

Fill, J. A. 2009. *On hitting times and fastest strong stationary times for skip-free and more general chains*, J. Theoret. Probab. **22**, no. 3, 587–600. ↑178

### PDF page 443 (book page 427)
Fill, J. A. and M. Huber. 2000. *The randomness recycler: A new technique for perfect sampling*, 41st Annual Symposium on Foundations of Computer Science, pp. 503–511. ↑349

Fill, J. A., M. Machida, D. J. Murdoch, and J. S. Rosenthal. 2000. *Extension of Fill's perfect rejection sampling algorithm to general chains*, Random Structure and Algorithms **17**, 290–316. ↑349

Folland, G. B. 1999. *Real analysis*, 2nd ed., Pure and Applied Mathematics (New York), John Wiley & Sons, Inc., New York. Modern techniques and their applications; A Wiley-Interscience Publication. ↑59

Frieze, A. and E. Vigoda. 2007. *A survey on the use of Markov chains to randomly sample colourings*, Combinatorics, complexity, and chance, Oxford Lecture Ser. Math. Appl., vol. 34, Oxford Univ. Press, Oxford, pp. 53–71. ↑214

Ganapathy, M. K. 2007. *Robust Mixing*, Electronic Journal of Probability **12**, 262–299. ↑114

Ganguly, S., E. Lubetzky, and F. Martinelli. 2015. *Cutoff for the east process*, Comm. Math. Phys. **335**, no. 3, 1287–1322. ↑271

Ganguly, S. and F. Martinelli. 2016. *Upper triangular matrix walk: Cutoff for finitely many columns*, available at arXiv:1612.08741. ↑362

Gaudillière, A. and C. Landim. 2014. *A Dirichlet principle for non reversible Markov chains and some recurrence theorems*, Probab. Theory Related Fields **158**, no. 1-2, 55–89, DOI 10.1007/s00440-012-0477-5. MR3152780 ↑149

Gheissari, R. and E. Lubetzky. 2016. *Mixing times of critical 2D Potts models*, available at arxiv:1607.02182. ↑231

Godbole, A. P. and S. G. Papastavridis (eds.) 1994. *Runs and patterns in probability: selected papers*, Mathematics and its Applications, vol. 283, Kluwer Academic Publishers Group, Dordrecht. ↑159

Greenberg, S., A. Pascoe, and D. Randall. 2009. *Sampling biased lattice configurations using exponential metrics*, ACM-SIAM Symposium on Discrete Algorithms (New York, New York, 2009), pp. 76-85. ↑334

Graham, R. L., D. E. Knuth, and O. Patashnik. 1994. *Concrete mathematics: A foundation for computer science*, second edition, Addison Wesley, Reading, Massachusetts. ↑112, 209

Griffeath, D. 1974/75. *A maximal coupling for Markov chains*, Z. Wahrscheinlichkeitstheorie und Verw. Gebiete **31**, 95–106. ↑74

Griffiths, S., R. J. Kang, R. Imbuzeiro Oliveira, and V. Patel. 2012. *Tight inequalities among set hitting times in Markov chains*, Proc. Amer. Math. Soc. ↑347

Grinstead, C. and L. Snell. 1997. *Introduction to Probability*, 2nd revised edition, American Mathematical Society, Providence. ↑35, 58

Guo, H. and M. Jerrum. 2017. *Random cluster dynamics for the Ising model is rapidly mixing*, Proceedings of the Twenty-Eighth Annual ACM-SIAM Symposium on Discrete Algorithms, pp. 1818–1827. ↑230

Häggström, O. 2002. *Finite Markov chains and algorithmic applications*, London Mathematical Society Student Texts, vol. 52, Cambridge University Press, Cambridge. ↑xv, 58

Häggström, O. 2007. *Problem solving is often a matter of cooking up an appropriate Markov chain*, Scand. J. Statist. **34**, no. 4, 768–780. ↑46

Häggström, O. and J. Jonasson. 1997. *Rates of convergence for lamplighter processes*, Stochastic Process. Appl. **67**, no. 2, 227–249. ↑278

Häggström, O. and K. Nelander. 1998. *Exact sampling from anti-monotone systems*, Statist. Neerlandica **52**, no. 3, 360–380. ↑358

Häggström, O. and K. Nelander. 1999. *On exact simulation of Markov random fields using coupling from the past*, Scand. J. Statist. **26**, no. 3, 395–411. ↑355, 356

Hajek, B. 1988. *Cooling schedules for optimal annealing*, Math. Oper. Res. **13**, no. 2, 311–329. ↑46

Handjani, S. and D. Jungreis. 1996. *Rate of convergence for shuffling cards by transpositions*, J. Theoret. Probab. **9**, no. 4, 983–993. ↑362

Hastings, W. K. 1970. *Monte Carlo sampling methods using Markov chains and their applications*, Biometrika **57**, no. 1, 97 –109. ↑45

Hayes, T. P. and A. Sinclair. 2007. *A general lower bound for mixing of single-site dynamics on graphs*, Ann. Appl. Probab. **17**, no. 3, 931–952. ↑99, 322, 361

### PDF page 444 (book page 428)

Hayes, T. P and E. Vigoda. 2003. *A non-Markovian coupling for randomly sampling colorings*, Proceedings of the 44th Annual IEEE Symposium on Foundations of Computer Science, pp. 618–627. ↑74

Hermon, J., H. Lacoin, and Y. Peres. 2016. *Total variation and separation cutoffs are not equivalent and neither one implies the other*, Electron. J. Probab. **21**, Paper No. 44, 36. ↑271, 362

Herstein, I. N. 1975. *Topics in algebra*, 2nd ed., John Wiley and Sons, New York. ↑35, 112

Hoeffding, W. 1963. *Probability inequalities for sums of bounded random variables*, J. Amer. Statist. Assoc. **58**, 13–30. MR0144363 (26 #1908) ↑367

Holley, R. 1974. *Remarks on the* FKG *inequalities*, Comm. Math. Phys. **36**, 227–231. ↑322

Holley, R. and D. Stroock. 1988. *Simulated annealing via Sobolev inequalities*, Comm. Math. Phys. **115**, no. 4, 553–569. ↑46

Holroyd, A. E. 2011. *Some circumstances where extra updates can delay mixing*, J. Stat. Phys. **145**, no. 6, 1649–1652. ↑322

Hoory, S., N. Linial, and A. Wigderson. 2006. *Expander graphs and their applications*, Bull. Amer. Math. Soc. (N.S.) **43**, no. 4, 439–561 (electronic). ↑200

Horn, R. A. and C. R. Johnson. 1990. *Matrix analysis*, Cambridge University Press, Cambridge. ↑177, 178, 374

Huber, M. 1998. *Exact sampling and approximate counting techniques*, Proceedings of the 30th Annual ACM Symposium on the Theory of Computing, pp. 31–40. ↑355

Ioffe, D. 1995. *Exact large deviation bounds up to $T_c$ for the Ising model in two dimensions*, Probab. Theory Related Fields **102**, no. 3, 313–330. ↑230

Ising, E. 1925. *Beitrag zur theorie der ferromagnetismus*, Zeitschrift Fur Physik **31**, 253–258. ↑231

Jerison, D. 2013. *General mixing time bounds for finite Markov chains via the absolute spectral gap*, available at `arxiv:1310.8021`. ↑178

Jerrum, M. R. 1995. *A very simple algorithm for estimating the number of k-colorings of a low-degree graph*, Random Structures Algorithms **7**, no. 2, 157–165. ↑214

Jerrum, M. 2003. *Counting, sampling and integrating: algorithms and complexity*, Lectures in Mathematics ETH Zürich, Birkhäuser Verlag, Basel. ↑xv, 58

Jerrum, M. R. and A. J. Sinclair. 1989. *Approximating the permanent*, SIAM Journal on Computing **18**, 1149–1178. ↑199, 230

Jerrum, M. and A. Sinclair. 1996. *The Markov chain Monte Carlo method: an approach to approximate counting and integration*, Approximation Algorithms for NP-hard Problems. ↑210, 211

Jerrum, M., A. Sinclair, and E. Vigoda. 2004. *A polynomial-time approximation algorithm for the permanent of a matrix with nonnegative entries*, J. ACM **51**, no. 4, 671–697 (electronic). ↑214

Jerrum, M. R., L. G. Valiant, and V. V. Vazirani. 1986. *Random generation of combinatorial structures from a uniform distribution*, Theoret. Comput. Sci. **43**, no. 2-3, 169–188. ↑214

Johnson, N. L. and S. Kotz. 1977. *Urn models and their application*, John Wiley & Sons, New York-London-Sydney. An approach to modern discrete probability theory; Wiley Series in Probability and Mathematical Statistics. ↑35

Jonasson, J. 2012. *Mixing times for the interchange process*, ALEA Lat. Am. J. Probab. Math. Stat. **9**, no. 2, 667–683. ↑334, 362

Kahn, J., J. H. Kim, L. Lovász, and V. H. Vu. 2000. *The cover time, the blanket time, and the Matthews bound*, 41st Annual Symposium on Foundations of Computer Science (Redondo Beach, CA, 2000), IEEE Comput. Soc. Press, Los Alamitos, CA, pp. 467–475. ↑159

Kahn, J. D., N. Linial, N. Nisan, and M. E. Saks. 1989. *On the cover time of random walks on graphs*, J. Theoret. Probab. **2**, no. 1, 121–128. ↑159

Kaĭmanovich, V. A. and A. M. Vershik. 1983. *Random walks on discrete groups: boundary and entropy*, Ann. Probab. **11**, no. 3, 457–490. ↑278

Kakutani, S. 1948. *On equivalence of infinite product measures*, Ann. of Math. (2) **49**, 214–224. ↑290

Kandel, D., Y. Matias, R. Unger, and P. Winkler. 1996. *Shuffling biological sequences*, Discrete Applied Mathematics **71**, 171–185. ↑242

Kantorovich, L. V. 1942. *On the translocation of masses*, C. R. (Doklady) Acad. Sci. URSS (N.S.) **37**, 199–201. ↑203, 214

### PDF page 445 (book page 429)

Kantorovich, L. V. and G. S. Rubinstein. 1958. *On a space of completely additive functions*, Vestnik Leningrad. Univ. **13**, no. 7, 52–59 (Russian, with English summary). ↑214

Karlin, S. and J. McGregor. 1959. *Coincidence properties of birth and death processes*, Pacific J. Math. **9**, 1109–1140. ↑178

Karlin, S. and H. M. Taylor. 1975. *A first course in stochastic processes*, 2nd ed., Academic Press, New York. ↑19

Karlin, S. and H. M. Taylor. 1981. *A second course in stochastic processes*, Academic Press Inc. [Harcourt Brace Jovanovich Publishers], New York. ↑178

Kassabov, M. 2005. *Kazhdan constants for* $\mathrm{SL}_n(\mathbb{Z})$, Internat. J. Algebra Comput. **15**, no. 5-6, 971–995. ↑361

Kasteleyn, P. W. 1961. *The statistics of dimers on a lattice I. The number of dimer arrangements on a quadratic lattice*, Physica **27**, no. 12, 1209–1225. ↑384

Keilson, J. 1979. *Markov chain models—rarity and exponentiality*, Applied Mathematical Sciences, vol. 28, Springer-Verlag, New York. ↑178

Kemeny, J. G., J. L. Snell, and A. W. Knapp. 1976. *Denumerable Markov chains*, 2nd ed., Springer-Verlag, New York. With a chapter on Markov random fields, by David Griffeath; Graduate Texts in Mathematics, No. 40. ↑304

Kendall, W. S. and J. Møller. 2000. *Perfect simulation using dominating processes on ordered spaces, with application to locally stable point processes*, Adv. in Appl. Probab. **32**, no. 3, 844–865. ↑349

Kenyon, C., E. Mossel, and Y. Peres. 2001. *Glauber dynamics on trees and hyperbolic graphs*, 42nd IEEE Symposium on Foundations of Computer Science (Las Vegas, NV, 2001), IEEE Computer Soc., Los Alamitos, CA, pp. 568–578. ↑229, 230

Knuth, D. 1997. *The art of computer programming*, third edition, Vol. 2: Seminumerical Algorithms, Addison-Wesley, Reading, Massachusetts. ↑383

Kobe, S. 1997. *Ernst Ising—physicist and teacher*, J. Statist. Phys. **88**, no. 3-4, 991–995. ↑231

Kolata, G. January 9, 1990. *In shuffling cards, 7 is winning number*, New York Times, C1. ↑111, 114

Komjáthy, J., J. Miller, and Y. Peres. 2014. *Uniform mixing time for random walk on lamplighter graphs*, Ann. Inst. Henri Poincaré Probab. Stat. **50**, no. 4, 1140–1160 (English, with English and French summaries). ↑278

Komjáthy, J. and Y. Peres. 2013. *Mixing and relaxation time for random walk on wreath product graphs*, Electron. J. Probab. **18**, no. 71, 23, DOI 10.1214/EJP.v18-2321. MR3091717 ↑278

Labbé, C. and H. Lacoin. 2016. *Cutoff phenomenon for the asymmetric simple exclusion process and the biased card shuffling*, available at `arxiv:1610.07383v1`. ↑334

Lacoin, H. 2015. *A product chain without cutoff*, Electron. Commun. Probab. **20**, no. 19, 9. ↑271, 290

Lacoin, H. 2016a. *Mixing time and cutoff for the adjacent transposition shuffle and the simple exclusion*, Ann. Probab. **44**, no. 2, 1426–1487. ↑241, 334, 362

Lacoin, H. 2016b. *The cutoff profile for the simple exclusion process on the circle*, Ann. Probab. **44**, no. 5, 3399–3430. ↑334

Laslier, B. and F. L. Toninelli. 2015. *How quickly can we sample a uniform domino tiling of the $2L \times 2L$ square via Glauber dynamics?*, Probab. Theory Related Fields **161**, no. 3-4, 509–559. ↑322

Lawler, G. F. 1991. *Intersections of random walks*, Probability and its Applications, Birkhäuser Boston, Inc., Boston, MA. ↑127

Lawler, G. and A. Sokal. 1988. *Bounds on the $L^2$ spectrum for Markov chains and Markov processes: a generalization of Cheeger's inequality*, Trans. Amer. Math. Soc. **309**, 557–580. ↑199

Lee, J. R. and T. Qin. 2012. *A note on mixing times of planar random walks*, available at `arxiv:1205.3980`. ↑

León, C. A. and F. Perron. 2004. *Optimal Hoeffding bounds for discrete reversible Markov chains*, Ann. Appl. Probab. **14**, no. 2, 958–970. ↑178

Letac, G. 1986. *A contraction principle for certain Markov chains and its applications*, Contemporary Mathematics **50**, 263–273. ↑349

Levin, D. A. and Y. Peres. 2010. *Pólya's theorem on random walks via Pólya's urn*, Amer. Math. Monthly **117**, no. 3, 220–231. ↑304

Levin, D. A. and Y. Peres. 2016. *Mixing of the exclusion process with small bias*, J. Stat. Phys. **165**, no. 6, 1036–1050. ↑334

### PDF page 446 (book page 430)

Levin, D. A., M. J. Luczak, and Y. Peres. 2010. *Glauber dynamics for the mean-field Ising model: cut-off, critical power law, and metastability*, Probab. Theory Related Fields **146**, no. 1-2, 223–265. ↑229, 270, 361

Li, S.-Y. R. 1980. *A martingale approach to the study of occurrence of sequence patterns in repeated experiments*, Ann. Probab. **8**, no. 6, 1171–1176. ↑259

Liggett, T. M. 1985. *Interacting particle systems*, Springer-Verlag, New York. ↑127, 334

Liggett, T. M. 1999. *Stochastic interacting systems: contact, voter and exclusion processes*, Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 324, Springer-Verlag, Berlin. ↑334

Lindvall, T. 2002. *Lectures on the coupling method*, Dover, Mineola, New York. ↑74

Littlewood, J. E. 1948. *Large Numbers*, Mathematical Gazette **32**, no. 300. ↑100

Logan, B. F. and L. A. Shepp. 1977. *A variational problem for random Young tableaux*, Advances in Math. **26**, no. 2, 206–222. ↑

Long, Y., A. Nachmias, W. Ning, and Y. Peres. 2014. *A power law of order 1/4 for critical mean field Swendsen-Wang dynamics*, Mem. Amer. Math. Soc. **232**, no. 1092, vi+84. ↑230

Lovász, L. 1993. *Random walks on graphs: a survey*, Combinatorics, Paul Erdős is Eighty, pp. 1–46. ↑58, 150

Lovász, L. and R. Kannan. 1999. *Faster mixing via average conductance*, Annual ACM Symposium on Theory of Computing (Atlanta, GA, 1999), ACM, New York, pp. 282–287 (electronic). ↑260

Lovász, L. and P. Winkler. 1993. *On the last new vertex visited by a random walk*, J. Graph Theory **17**, 593–596. ↑87

Lovász, L. and P. Winkler. 1995a. *Exact mixing in an unknown Markov chain*, Electronic Journal of Combinatorics **2**. Paper #R15. ↑357

Lovász, L. and P. Winkler. 1995b. *Efficient stopping rules for Markov chains*, Proc. 27th ACM Symp. on the Theory of Computing, pp. 76–82. ↑87, 336, 346

Lovász, L. and P. Winkler. 1998. *Mixing times*, Microsurveys in discrete probability (Princeton, NJ, 1997), DIMACS Ser. Discrete Math. Theoret. Comput. Sci., vol. 41, Amer. Math. Soc., Providence, RI, pp. 85–133. ↑58, 84, 87, 335, 336, 347

Loynes, R. M. 1962. *The stability of a queue with non-independent inter-arrival and service times*, Proceedings of the Cambridge Philosophical Society **58**, 497–520. ↑349

Lubetzky, E., F. Martinelli, A. Sly, and F. L. Toninelli. 2013. *Quasi-polynomial mixing of the 2D stochastic Ising model with "plus" boundary up to criticality*, J. Eur. Math. Soc. (JEMS) **15**, no. 2, 339–386. ↑359

Lubetzky, E. and Y. Peres. 2016. *Cutoff on all Ramanujan graphs*, Geom. Funct. Anal. **26**, no. 4, 1190–1216, DOI 10.1007/s00039-016-0382-7. MR3558308 ↑271

Lubetzky, E. and A. Sly. 2010. *Cutoff phenomena for random walks on random regular graphs*, Duke Math. J. **153**, no. 3, 475–510. ↑271

Lubetzky, E. and A. Sly. 2012. *Critical Ising on the square lattice mixes in polynomial time*, Comm. Math. Phys. **313**, no. 3, 815–836. ↑230

Lubetzky, E. and A. Sly. 2013. *Cutoff for the Ising model on the lattice*, Invent. Math. **191**, no. 3, 719–755. ↑229, 230, 361

Lubetzky, E. and A. Sly. 2014a. *Cutoff for general spin systems with arbitrary boundary conditions*, Comm. Pure Appl. Math. **67**, no. 6, 982–1027. ↑230, 290, 361

Lubetzky, E. and A. Sly. 2014b. *Universality of cutoff for the Ising model*. Preprint. ↑361

Lubetzky, E. and A. Sly. 2016. *Information percolation and cutoff for the stochastic Ising model*, J. Amer. Math. Soc. **29**, no. 3, 729–774. ↑230, 361

Lubotzky, A. 1994. *Discrete groups, expanding graphs and invariant measures*, Progress in Mathematics, vol. 125, Birkhäuser Verlag, Basel. With an appendix by Jonathan D. Rogawski. ↑200

Luby, M., D. Randall, and A. Sinclair. 1995. *Markov chain algorithms for planar lattice structures*, Proceedings of the 36th IEEE Symposium on Foundations of Computing, pp. 150–159. ↑74, 384

Luby, M., D. Randall, and A. Sinclair. 2001. *Markov chain algorithms for planar lattice structures*, SIAM J. Comput. **31**, 167–192. ↑74

Luby, M. and E. Vigoda. 1995. *Approximately counting up to four*, Proceedings of the Twenty-Ninth Annual ACM Symposium on Theory of Computing, pp. 150–159. Extended abstract. ↑74

Luby, M. and E. Vigoda. 1999. *Fast convergence of the Glauber dynamics for sampling independent sets*, Random Structures and Algorithms **15**, no. 3-4, 229–241. ↑74

### PDF page 447 (book page 431)

Lyons, R. 2005. *Asymptotic enumeration of spanning trees*, Combin. Probab. Comput. **14**, no. 4, 491–522. ↑253

Lyons, R and S. Oveis Gharan. 2012. *Sharp Bounds on Random Walk Eigenvalues via Spectral Embedding*, available at [arxiv:1211.0589](arxiv:1211.0589). ↑149

Lyons, T. 1983. *A simple criterion for transience of a reversible Markov chain*, Ann. Probab. **11**, no. 2, 393–402. ↑294, 304

Lyons, R. and Y. Peres. 2016. *Probability on Trees and Networks*, Cambridge University Press, Cambridge. ↑99, 127, 149, 304

Madras, N. and D. Randall. 1996. *Factoring graphs to bound mixing rates*, Proceedings of the 37th IEEE Symposium on Foundations of Computing, pp. 194–203. ↑199

Madras, N. and G. Slade. 1993. *The self-avoiding walk*, Birkhäuser, Boston. ↑384, 385

Mann, B. 1994. *How many times should you shuffle a deck of cards?*, UMAP J. **15**, no. 4, 303–332. ↑114

Markov, A. A. 1906. *Rasprostranenie zakona bol'shih chisel na velichiny, zavisyaschie drug ot druga*, Izvestiya Fiziko-matematicheskogo obschestva pri Kazanskom universitete, 2-ya seriya **15**, 135–156. ↑18

Martinelli, F. 1994. *On the two-dimensional dynamical Ising model in the phase coexistence region*, J. Statist. Phys. **76**, no. 5-6, 1179–1246. ↑359

Martinelli, F. 1999. *Lectures on Glauber dynamics for discrete spin models*, Lectures on probability theory and statistics (Saint-Flour, 1997), Lecture Notes in Math., vol. 1717, Springer, Berlin, pp. 93–191. ↑226, 231, 322, 360

Martinelli, F. and E. Olivieri. 1994. *Approach to equilibrium of Glauber dynamics in the one phase region. I. The attractive case*, Comm. Math. Phys. **161**, no. 3, 447–486. ↑230

Martinelli, F., E. Olivieri, and R. H. Schonmann. 1994. *For* 2*-D lattice spin systems weak mixing implies strong mixing*, Comm. Math. Phys. **165**, no. 1, 33–47. ↑230

Martinelli, F., A. Sinclair, and D. Weitz. 2004. *Glauber dynamics on trees: boundary conditions and mixing time*, Comm. Math. Phys. **250**, no. 2, 301–334. ↑229

Martinelli, F. and M. Wouts. 2012. *Glauber dynamics for the quantum Ising model in a transverse field on a regular tree*, J. Stat. Phys. **146**, no. 5, 1059–1088. ↑322

Matthews, P. 1988a. *Covering problems for Markov chains*, Ann. Probab. **16**, 1215–1228. ↑150, 151, 158

Matthews, P. 1988b. *A strong uniform time for random transpositions*, J. Theoret. Probab. **1**, no. 4, 411–423. ↑112, 165

Matthews, P. 1989. *Some sample path properties of a random walk on the cube*, J. Theoret. Probab. **2**, no. 1, 129–146. ↑158

McKay, B. D. and C. E. Praeger. 1996. *Vertex-transitive graphs that are not Cayley graphs. II*, J. Graph Theory **22**, no. 4, 321–334. ↑29

Menshikov, M., S. Popov, and A. Wade. 2017. *Non-homogeneous Random Walks: Lyapunov Function Methods for Near-Critical Stochastic Systems*, Vol. 209, Cambridge University Press. ↑304

Metropolis, N., A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller. 1953. *Equation of state calculations by fast computing machines*, J. Chem. Phys. **21**, 1087–1092. ↑45

Mihail, M. 1989. *Conductance and convergence of Markov chains - A combinatorial treatment of expanders*, Proceedings of the 30th Annual Conference on Foundations of Computer Science, 1989, pp. 526–531. ↑99

Miller, J. and Y. Peres. 2012. *Uniformity of the uncovered set of random walk and cutoff for lamplighter chains*, Ann. Probab. **40**, no. 2, 535–577. ↑278, 362

Mironov, I. 2002. *(Not so) random shuffles of RC4*, Advances in cryptology—CRYPTO 2002, Lecture Notes in Comput. Sci., vol. 2442, Springer, Berlin, pp. 304–319. ↑114

Montenegro, R. and P. Tetali. 2006. *Mathematical aspects of mixing times in Markov chains*, Vol. 1. ↑xv, 58

Móri, T. F. 1987. *On the expectation of the maximum waiting time*, Ann. Univ. Sci. Budapest. Sect. Comput. **7**, 111–115 (1988). ↑159

Morris, B. 2006. *The mixing time for simple exclusion*, Ann. Appl. Probab. **16**, no. 2, 615–635. ↑334

Morris, B. 2009. *Improved mixing time bounds for the Thorp shuffle and L-reversal chain*, Ann. Probab. **37**, no. 2, 453–477. ↑242

### PDF page 448 (book page 432)

Morris, B., W. Ning, and Y. Peres. 2014. *Mixing time of the card-cyclic-to-random shuffle*, Ann. Appl. Probab. **24**, no. 5, 1835–1849. ↑360

Morris, B. and Y. Peres. 2005. *Evolving sets, mixing and heat kernel bounds*, Probab. Theory Related Fields **133**, no. 2, 245–266. ↑249, 260

Morris, B. and C. Qin. 2014. *Improved bounds for the mixing time of the random-to-random insertion shuffle*, available at [arXiv:1412.0070](arXiv:1412.0070). ↑360

Mossel, E., Y. Peres, and A. Sinclair. 2004. *Shuffling by semi-random transpositions*, Proceedings of the 45th Annual IEEE Symposium on Foundations of Computer Science (FOCS'04) October 17 - 19, 2004, Rome, Italy, pp. 572–581. ↑114, 200, 360

Nacu, Ş. 2003. *Glauber dynamics on the cycle is monotone*, Probab. Theory Related Fields **127**, no. 2, 177–185. ↑322, 359

Nash-Williams, C. St. J. A. 1959. *Random walks and electric currents in networks*, Proc. Cambridge Philos. Soc. **55**, 181–194. ↑127

von Neumann, J. 1951. *Various techniques used in connection with random digits*, National Bureau of Standards Applied Mathematics Series **12**, 36–38. ↑376, 389

Norris, J. R. 1998. *Markov chains*, Cambridge Series in Statistical and Probabilistic Mathematics, vol. 2, Cambridge University Press, Cambridge. Reprint of 1997 original. ↑xv, 304

Oliveira, R. I. 2012. *Mixing and hitting times for finite Markov chains*, Electron. J. Probab. **17**, no. 70, 12. ↑346

Oliveira, R. I. 2013. *Mixing of the symmetric exclusion processes in terms of the corresponding single-particle random walk*, Ann. Probab. **41**, no. 2, 871–913. ↑334

Pak, I. 1997. *Random Walks on Groups : Strong Uniform Time Approach*, Ph.D. thesis, Harvard University. ↑87

Pemantle, R. 2007. *A survey of random processes with reinforcement*, Probab. Surv. **4**, 1–79 (electronic). ↑35

Peres, Y. 1992. *Iterating von Neumann's procedure for extracting random bits*, Ann. Stat. **20**, no. 1, 590–597. ↑377, 389

Peres, Y. 1999. *Probability on trees: an introductory climb*, Lectures on Probability Theory and Statistics, Ecole d'Ete de Probabilites de Saint-Flour XXVII - 1997, pp. 193–280. ↑127

Peres, Y. 2002. *Brownian intersections, cover times and thick points via trees*, (Beijing, 2002), Higher Ed. Press, Beijing, pp. 73–78. ↑158

Peres, Y., S. Popov, and P. Sousi. 2013. *On recurrence and transience of self-interacting random walks*, Bull. Braz. Math. Soc. (N.S.) **44**, no. 4, 841–867. ↑304

Peres, Y. and D. Revelle. 2004. *Mixing times for random walks on finite lamplighter groups*, Electron. J. Probab. **9**, no. 26, 825–845 (electronic). ↑278

Peres, Y. and A. Sly. 2013. *Mixing of the upper triangular matrix walk*, Probab. Theory Related Fields **156**, no. 3-4, 581–591. ↑362

Peres, Y. and P. Sousi. 2015a. *Mixing times are hitting times of large sets*, J. Theoret. Probab. **28**, no. 2, 488–519. ↑335, 346, 347

Peres, Y. and P. Sousi. 2015b. *Total variation cutoff in a tree*, Ann. Fac. Sci. Toulouse Math. (6) **24**, no. 4, 763–779, DOI 10.5802/afst.1463 (English, with English and French summaries). MR3434255 ↑271

Peres, Y. and P. Winkler. 2013. *Can extra updates delay mixing?*, Comm. Math. Phys. **323**, no. 3, 1007–1016. ↑322, 361

Pinsker, M. S. 1973. *On the complexity of a concentrator*, Proc. 7th Int. Teletraffic Conf., Stockholm, Sweden, pp. 318/1–318/4. ↑196, 200

Pisztora, A. 1996. *Surface order large deviations for Ising, Potts and percolation models*, Probab. Theory and Related Fields **104**, no. 4, 427–466. ↑230

Pitman, J. W. 1974. *Uniform rates of convergence for Markov chain transition probabilities*, Z. Wahrscheinlichkeitstheorie und Verw. Gebiete **29**, 193–227. ↑74

Pitman, J. W. 1976. *On coupling of Markov chains*, Z. Wahrscheinlichkeitstheorie und Verw. Gebiete **35**, no. 4, 315–322. ↑74

Pólya, G. 1931. *Sur quelques points de la théorie des probabilités*, Ann. Inst. H. Poincaré **1**, 117–161. ↑35

Pourmiri, A. and T. Sauerwald. 2014. *Cutoff phenomenon for random walks on Kneser graphs*, Discrete Appl. Math. **176**, 100–106. ↑271

Preston, C. J. 1974. *Gibbs states on countable sets*, Cambridge University Press, London-New York. Cambridge Tracts in Mathematics, No. 68. ↑

### PDF page 449 (book page 433)

Propp, J. and D. Wilson. 1996. *Exact sampling with coupled Markov chains and applications to statistical mechanics*, Random Structure and Algorithms **9**, 223–252. ↑319, 348, 349, 354

Propp, J. and D. Wilson. 1998. *How to get a perfectly random sample from a generic Markov chain and generate a random spanning tree of a directed graph*, Journal of Algorithms (SODA '96 special issue) **27**, no. 2, 170–217. ↑357, 358

Quastel, J. 1992. *Diffusion of color in the simple exclusion process*, Comm. Pure Appl. Math. **45**, no. 6, 623–679. ↑199

Randall, D. 2006. *Slow mixing of Glauber dynamics via topological obstructions*, SODA (2006). Available at http://www.math.gatech.edu/~randall/reprints.html. ↑226, 228

Randall, D. and A. Sinclair. 2000. *Self-testing algorithms for self-avoiding walks*, Journal of Mathematical Physics **41**, no. 3, 1570–1584. ↑384, 386

Randall, D. and P. Tetali. 2000. *Analyzing Glauber dynamics by comparison of Markov chains*, J. Math. Phys. **41**, no. 3, 1598–1615. Probabilistic techniques in equilibrium and nonequilibrium statistical physics. ↑199

Restrepo, R., D. Štefankovič, J. C. Vera, E. Vigoda, and L. Yang. 2014. *Phase transition for Glauber dynamics for independent sets on regular trees*, SIAM J. Discrete Math. **28**, no. 2, 835–861. ↑322

Riordan, J. 1944. *Three-line Latin rectangles*, Amer. Math. Monthly **51**, 450–452. ↑197

Röllin, A. 2007. *Translated Poisson approximation using exchangeable pair couplings*, Ann. Appl. Probab. **17**, no. 5-6, 1596–1614. ↑290

Salas, J. and A. D. Sokal. 1997. *Absence of phase transition for antiferromagnetic Potts models via the Dobrushin uniqueness theorem*, J. Statist. Phys. **86**, no. 3-4, 551–579. ↑214

Saloff-Coste, L. 1997. *Lectures on finite Markov chains*, Lectures on Probability Theory and Statistics, Ecole d'Ete de Probabilites de Saint-Flour XXVI - 1996, pp. 301–413. ↑58, 149

Saloff-Coste, L. and J. Zúñiga. 2007. *Convergence of some time inhomogeneous Markov chains via spectral techniques*, Stochastic Process. Appl. **117**, no. 8, 961–979. ↑114

Saloff-Coste, L. and J. Zúñiga. 2008. *Refined estimates for some basic random walks on the symmetric and alternating groups*, ALEA Lat. Am. J. Probab. Math. Stat. **4**, 359–392. ↑360

Sarnak, P. 2004. *What is. . . an expander?*, Notices Amer. Math. Soc. **51**, no. 7, 762–763. ↑200

Scarabotti, F. and F. Tolli. 2008. *Harmonic analysis of finite lamplighter random walks*, J. Dyn. Control Syst. **14**, no. 2, 251–282, available at [arXiv:math.PR/0701603](arXiv:math.PR/0701603). ↑278

Schonmann, R. H. 1987. *Second order large deviation estimates for ferromagnetic systems in the phase coexistence region*, Comm. Math. Phys. **112**, no. 3, 409–422. ↑226, 229

Seneta, E. 2006. *Non-negative matrices and Markov chains*, Springer Series in Statistics, Springer, New York. Revised reprint of the second (1981) edition [Springer-Verlag, New York]. ↑19, 58

Simon, B. 1993. *The statistical mechanics of lattice gases. Vol. I*, Princeton Series in Physics, Princeton University Press, Princeton, NJ. ↑230, 231

Sinclair, A. 1992. *Improved bounds for mixing rates of Markov chains and multicommodity flow*, Combin. Probab. Comput. **1**, no. 4, 351–370. ↑

Sinclair, A. 1993. *Algorithms for random generation and counting*, Progress in Theoretical Computer Science, Birkhäuser Boston Inc., Boston, MA. A Markov chain approach. ↑58, 214

Sinclair, A. and M. Jerrum. 1989. *Approximate counting, uniform generation and rapidly mixing Markov chains*, Inform. and Comput. **82**, no. 1, 93–133. ↑199, 226

Snell, J. L. 1997. *A conversation with Joe Doob*, Statist. Sci. **12**, no. 4, 301–311. ↑363

Soardi, P. M. 1994. *Potential theory on infinite networks*, Lecture Notes in Mathematics, vol. 1590, Springer-Verlag, Berlin. ↑127, 304

Spielman, D. A. and S.-H. Teng. 1996. *Spectral partitioning works: planar graphs and finite element meshes*, 37th Annual Symposium on Foundations of Computer Science (Burlington, VT, 1996), IEEE Comput. Soc. Press, Los Alamitos, CA. ↑178

Spitzer, F. 1976. *Principles of random walks*, 2nd ed., Springer-Verlag, New York. Graduate Texts in Mathematics, Vol. 34. ↑290

Stanley, R. P. 1986. *Enumerative combinatorics*, Vol. 1, Wadsworth & Brooks/Cole, Belmont, California. ↑209

Stanley, R. P. 1999. *Enumerative Combinatorics*, Vol. 2, Cambridge University Press. ↑35

Stanley, R. P. 2008. *Catalan Addendum*. Available at http://www-math.mit.edu/~rstan/ec/catadd.pdf. ↑35

### PDF page 450 (book page 434)

Steele, J. M. 1997. *Probability theory and combinatorial optimization*, CBMS-NSF Regional Conference Series in Applied Mathematics, vol. 69, Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA. ↑367

Strassen, V. 1965. *The existence of probability measures with given marginals*, Ann. Math. Statist. **36**, 423–439. MR0177430 (31 #1693) ↑322

Stroock, D. W. and B. Zegarliński. 1992. *The equivalence of the logarithmic Sobolev inequality and the Dobrushin-Shlosman mixing condition*, Comm. Math. Phys. **144**, no. 2, 303–323. ↑230

Subag, E. 2013. *A lower bound for the mixing time of the random-to-random insertions shuffle*, Electron. J. Probab. **18**, no. 20, 20. ↑360

Sugimine, N. 2002. *A lower bound on the spectral gap of the 3-dimensional stochastic Ising models*, J. Math. Kyoto Univ. **42**, no. 4, 751–788 (2003). ↑359

Tetali, P. 1999. *Design of on-line algorithms using hitting times*, SIAM J. Comput. **28**, no. 4, 1232–1246 (electronic). ↑149

Thomas, L. E. 1989. *Bound on the mass gap for finite volume stochastic Ising models at low temperature*, Comm. Math. Phys. **126**, no. 1, 1–11. ↑226, 230

Thorisson, H. 1988. *Backward limits*, Annals of Probability **16**, 914–924. ↑349

Thorisson, H. 2000. *Coupling, stationarity, and regeneration*, Probability and its Applications (New York), Springer-Verlag, New York. ↑74, 304

Thorp, E. O. 1965. *Elementary Problem E1763*, Amer. Math. Monthly **72**, no. 2, 183. ↑112, 113

Thurston, W. P. 1990. *Conway's tiling groups*, Amer. Math. Monthly **97**, no. 8, 757–773. ↑8

Uyemura-Reyes, J. C. 2002. *Random Walk, Semidirect Products, and Card Shuffling*, Ph.D. thesis, Stanford University. ↑360

Varopoulos, N. Th. 1985. *Long range estimates for Markov chains*, Bull. Sci. Math. (2) **109**, no. 3, 225–252 (English, with French summary). ↑99

Vasershtein, L. N. 1969. *Markov processes over denumerable products of spaces describing large system of automata*, Problemy Peredači Informacii **5**, no. 3, 64–72 (Russian); English transl.,. 1969, Problems of Information Transmission **5**, no. 3, 47–52. ↑214

Vershik, A. M. 2004. *The Kantorovich metric: the initial history and little-known applications*, Zap. Nauchn. Sem. S.-Peterburg. Otdel. Mat. Inst. Steklov. (POMI) **312**, no. Teor. Predst. Din. Sist. Komb. i Algoritm. Metody. 11, 69–85, 311 (Russian, with English and Russian summaries); English transl.,. 2004, J. Math. Sci. (N. Y.) **133**, no. 4, 1410–1417, available at arxiv:math.FA/0503035. ↑214

Veršik, A. M. and S. V. Kerov. 1977. *Asymptotic behavior of the Plancherel measure of the symmetric group and the limit form of Young tableaux*, Dokl. Akad. Nauk SSSR **233**, no. 6, 1024–1027 (Russian). ↑

Vigoda, E. 2000. *Improved bounds for sampling colorings*, J. Math. Phys. **41**, no. 3, 1555–1569. ↑214

Vigoda, E. 2001. *A note on the Glauber dynamics for sampling independent sets*, Electron. J. Combin. **8**, no. 1, Research Paper 8, 8 pp. (electronic). ↑74, 357

Villani, C. 2003. *Topics in optimal transportation*, Graduate Studies in Mathematics, vol. 58, American Mathematical Society, Providence, RI. ↑214

Wilf, H. S. 1989. *The editor's corner: The white screen problem*, Amer. Math. Monthly **96**, 704–707. ↑158

Williams, D. 1991. *Probability with martingales*, Cambridge Mathematical Textbooks, Cambridge University Press, Cambridge. ↑259

Wilson, D. B. 2000a. *Layered multishift coupling for use in perfect sampling algorithms (with a primer on CFTP)* (N. Madras, ed.), Fields Institute Communications, vol. 26, American Mathematical Society. ↑358

Wilson, D. B. 2000b. *How to couple from the past using a read-once source of randomness*, Random Structures and Algorithms **16**, 85–113. ↑349, 354

Wilson, D. B. 2003. *Mixing time of the Rudvalis shuffle*, Electron. Comm. Probab. **8**, 77–85 (electronic). ↑200

Wilson, D. B. 2004a. *Mixing times of Lozenge tiling and card shuffling Markov chains*, Ann. Appl. Probab. **14**, no. 1, 274–325. ↑192, 193, 200, 241, 322, 384

Wilson, D. B. 2004b. *Perfectly Random Sampling with Markov Chains*. Available at http://research.microsoft.com/~dbwilson/exact/. ↑358

Woess, W. 2000. *Random walks on infinite graphs and groups*, Cambridge Tracts in Mathematics, vol. 138, Cambridge University Press, Cambridge. ↑304

### PDF page 451 (book page 435)

Zeitouni, O. 2004. *Random walks in random environment*, Lectures on probability theory and statistics, Lecture Notes in Math., vol. 1837, Springer, Berlin, pp. 189–312. ↑304

Zuckerman, D. 1989. *Covering times of random walks on bounded degree trees and other graphs*, J. Theoret. Probab. **2**, no. 1, 147–157. ↑159

Zuckerman, D. 1992. *A technique for lower bounding the cover time*, SIAM J. Discrete Math. **5**, 81–87. ↑158, 159

van Zuylen, A. and F. Schalekamp. 2004. *The Achilles' heel of the GSR shuffle. A note on new age solitaire*, Probab. Engrg. Inform. Sci. **18**, no. 3, 315–328. ↑114

### PDF page 452 (no printed page number)

*(Blank page.)*

### PDF page 453 (book page 437)

# Notation Index

The symbol := means *defined as*.

The set $\{\dots, -1, 0, 1, \dots\}$ of integers is denoted $\mathbb{Z}$ and the set of real numbers is denoted $\mathbb{R}$.

For sequences $(a_n)$ and $(b_n)$, the notation $a_n = O(b_n)$ means that for some $c > 0$ we have $a_n/b_n \le c$ for all $n$, while $a_n = o(b_n)$ means that $\lim_{n\to\infty} a_n/b_n = 0$, and $a_n \asymp b_n$ means both $a_n = O(b_n)$ and $b_n = O(a_n)$ are true.

*(Notation index, left column then right column:)*

$A_n$ (alternating group), 101
$B$ (congestion ratio), 188
$\mathcal{C}(a \leftrightarrow z)$ (effective conductance), 119
$\mathcal{E}(f, h)$ Dirichlet form), 181
$\mathcal{E}(f)$ (Dirichlet form), 181
$E$ (edge set), 8
$\mathbf{E}$ (expectation), 365
$\mathbf{E}_\mu$ (expectation from initial distribution $\mu$), 4
$\mathbf{E}_x$ (expectation from initial state $x$), 5
$E_\mu$ (expectation w.r.t. $\mu$), 93, 390
$G$ (graph), 8
$G^\diamond$ (lamplighter graph), 272
$I$ (current flow), 118
$P$ (transition matrix), 2
$P_A$ (transition matrix of induced chain), 186
$\widehat{P}$ (time reversal), 14
$\mathbf{P}\{X \in B\}$ (probability of event), 364
$\mathbf{P}_\mu$ (probability from initial distribution $\mu$), 4
$\mathbf{P}_x$ (probability from initial state $x$), 5
$\mathbf{P}_{x,y}$ (probability w.r.t. coupling started from $x$ and $y$), 62
$Q(x, y)$ (edge measure), 89
$\mathcal{R}(a \leftrightarrow z)$ (effective resistance), 119
$\mathcal{S}_n$ (symmetric group), 75
$S^V$ (configuration set), 41
$V$ (vertex set), 8
Var (variance), 365
$\mathrm{Var}_\mu$ (variance w.r.t. $\mu$), 93
$W$ (voltage), 118

$\mathbb{Z}_n$ ($n$-cycle), 63
$\mathbb{Z}_n^d$ (torus), 64

$c(e)$ (conductance), 116
$d(t)$ (total variation distance), 53
$\bar{d}(t)$ (total variation distance), 53
$d_H$ (Hellinger distance), 58, 286
id (identity element), 27
i.i.d. (independent and identically distributed), 60
$r(e)$ (resistance), 116
$s_x(t)$ (separation distance started from $x$), 79
$s(t)$ (separation distance), 79
$t_{\mathrm{cov}}$ (worst case mean cover time), 150
$t_{\mathrm{hit}}$ (maximal hitting time), 129
$t_{\mathrm{mix}}(\varepsilon)$ (mixing time), 54
$t_{\mathrm{Ces}}$ (Cesaro mixing time), 84
$t_{\mathrm{mix}}^{\mathrm{cont}}$ (continuous mixing time), 282
$t_{\mathrm{rel}}$ (relaxation time), 163
$t_\odot$ (target time), 129

$\beta$ (inverse temperature), 44
$\delta_x$ (Dirac delta), 5
$\Delta$ (maximum degree), 70
$\Gamma_{xy}$ (path), 188
$\gamma$ (spectral gap), 163
$\gamma_\star$ (absolute spectral gap), 163
$\lambda_j$ (eigenvalue of transition matrix), 163
$\lambda_\star$ (maximal non-trivial eigenvalue), 163
$\mathcal{X}$ (state space), 2
$\omega$ (root of unity), 165
$\Phi(S)$ (bottleneck ratio of set), 89

### PDF page 454 (book page 438)

*(Notation index, continued:)*

$\Phi_\star$ (bottleneck ratio), 89
$\pi$ (stationary distribution), 9
$\rho$ (metric), 201, 373
$\rho_K(\mu, \nu)$ (transportation metric), 201
$\rho_{i,j}$ (reversal), 236
$\sigma$ (Ising spin), 44
$\tau_A$ (hitting time for set), 77, 117, 128
$\tau_{a,b}$ (commute time), 131
$\tau_{\mathrm{couple}}$ (coupling time), 62
$\tau_{\mathrm{cov}}$ (cover time variable), 150
$\tau_{\mathrm{cov}}^A$ (cover time for set), 151
$\tau_x$ (hitting time), 10, 128
$\tau_x^+$ (first return time), 10, 128
$\theta$ (flow), 118

$\wedge$ (min), 39
$(ijk)$ (cycle (permutation)), 100
$\partial S$ (boundary of $S$), 90
$\ell^2(\pi)$ (inner product space), 161
$[x]$ (equivalence class), 25
$\langle \cdot, \cdot \rangle$ (standard inner product), 161
$\langle \cdot, \cdot \rangle_\pi$ (inner product w.r.t. $\pi$), 161
$\widehat{\mu}$ (reversed distribution), 55
$\mathbf{1}_A$ (indicator function), 14
$\sim$ (adjacent to), 8
$\|\mu - \nu\|_{\mathrm{TV}}$ (total variation distance), 47

### PDF page 455 (book page 439)

# Index

Italics indicate that the reference is to an exercise.

*(Index, left column then right column:)*

absolute spectral gap, 163
absorbing state, 15
acceptance-rejection sampling, 378
alternating group, 101, *110*
aperiodic chain, 7
approximate counting, 210
averaging over paths, 190

ballot theorem, 33
binary tree, 66
&nbsp;&nbsp;Ising model on, 220
&nbsp;&nbsp;random walk on
&nbsp;&nbsp;&nbsp;&nbsp;bottleneck ratio lower bound, 92
&nbsp;&nbsp;&nbsp;&nbsp;commute time, 133
&nbsp;&nbsp;&nbsp;&nbsp;coupling upper bound, 66
&nbsp;&nbsp;&nbsp;&nbsp;cover time, 152
&nbsp;&nbsp;&nbsp;&nbsp;hitting time, *146*
&nbsp;&nbsp;&nbsp;&nbsp;no cutoff, 267
birth-and-death chain, 26, *259*, 299
&nbsp;&nbsp;stationary distribution, 26
block dynamics
&nbsp;&nbsp;for Ising model, 223, 361
bottleneck ratio, 89, 90
&nbsp;&nbsp;bounds on relaxation time, 183
&nbsp;&nbsp;lower bound on mixing time, 89
boundary, 90
Bounded Convergence Theorem, 369

Catalan number, 32
Cayley graph, 29
censoring inequality, 314
Central Limit Theorem, 367
Cesaro mixing time, 84, 335
CFTP, *see also* coupling from the past
Chebyshev's inequality, 365
Cheeger constant, 99
children (in tree), 65
coin tossing patterns, *see also* patterns in coin tossing
colorings, 38
&nbsp;&nbsp;approximate counting of, 210
&nbsp;&nbsp;Glauber dynamics for, 41, 360
&nbsp;&nbsp;&nbsp;&nbsp;exponential lower bound on star, 91

&nbsp;&nbsp;&nbsp;&nbsp;lower bound on empty graph, *98*
&nbsp;&nbsp;&nbsp;&nbsp;path coupling upper bound, 206, 207
&nbsp;&nbsp;Metropolis dynamics for
&nbsp;&nbsp;&nbsp;&nbsp;grand coupling upper bound, 70
&nbsp;&nbsp;&nbsp;&nbsp;relaxation time, 180
communicating classes, 15
commute time, 131
&nbsp;&nbsp;Identity, 132
comparison of Markov chains, 185
&nbsp;&nbsp;canonical paths, 188
&nbsp;&nbsp;on groups, 190
&nbsp;&nbsp;randomized paths, 190
&nbsp;&nbsp;theorem, 188, 223, 233, 239
complete graph, 81
&nbsp;&nbsp;Ising model on, 218
&nbsp;&nbsp;lamplighter chain on, 277
conductance, 116
&nbsp;&nbsp;bottleneck ratio, 99
configuration, 41
congestion ratio, 188, 190
connected graph, *17*
connective constant, 226
continuous-time chain, 280
&nbsp;&nbsp;Convergence Theorem, 282
&nbsp;&nbsp;product chains, 285
&nbsp;&nbsp;relation to lazy chain, 282
&nbsp;&nbsp;relaxation time, 284
Convergence Theorem, 52
&nbsp;&nbsp;continuous time, 282
&nbsp;&nbsp;coupling proof, *73*
&nbsp;&nbsp;null recurrent chain, 300
&nbsp;&nbsp;positive recurrent chain, 298
convolution, 143, *147*
counting lower bound, 88
coupling
&nbsp;&nbsp;bound on $d(t)$, 62
&nbsp;&nbsp;characterization of total variation distance, 50
&nbsp;&nbsp;from the past, 348
&nbsp;&nbsp;grand, 69, 70, 351, 354
&nbsp;&nbsp;Markovian, 61, *73*
&nbsp;&nbsp;of distributions, 49, 50, 201

### PDF page 456 (book page 440)

of Markov chains, 61
of random variables, 49, 201
optimal, 50, 202
coupon collector, 22, 63, 82, 95
cover time variable, 150
current flow, 118
cutoff, 261
open problems, 360
window, 262
cutset
edge, 123
cycle
biased random walk on, 14
Ising model on
mixing time pre-cutoff, 219
random walk on, 5, 8, *17*, 28, *34*, 78
bottleneck ratio, 183
coupling upper bound, 63
cover time, 150, *158*
eigenvalues and eigenfunctions, 165
hitting time upper bound, 144
last vertex visited, *86*
lower bound, 63
no cutoff, 267
spectral gap, 166
strong stationary time upper bound, 83, *86*
cycle law, 119
cycle notation, 100
cyclic-to-random shuffle, 113

degree of vertex, 8
density function, 364
depth (of tree), 65
descendant (in tree), 92
detailed balance equations, 13
diameter, 89, 201
diameter lower bound, 89
dimer system, 383
Dirichlet form, 181
distinguishing statistic, 92
distribution function, 364
divergence
of flow, 118
Dominated Convergence Theorem, 369
domino tiling, 384
Doob $h$-transform, 255
Doob decomposition, *259*
Durrett chain
comparison upper bound, 239
distinguishing statistic lower bound, 237

East model, 362
lower bound, 98
edge cutset, 123
edge measure, 89
effective conductance, 119
effective resistance, 119
gluing nodes, 120, 123

of grid graph, 124
of tree, 121
Parallel Law, 120
Series Law, 120
triangle inequality, *126*, 132
Ehrenfest urn, 24, *34*, 265
eigenvalues of transition matrix, 161, *177*
empty graph, *98*
energy
of flow, 122
of Ising configuration, 44
ergodic theorem, 390
escape probability, 119
essential state, 15
Eulerian graphs, 137
even permutation, 101
event, 363
evolving-set process, 249
exclusion process, 323
biased, 329
monotonicity of, 325
on path
mixing time, 328
expander graph, 196
Ising model on, *228*
ExpanderMixingLemma, 177
expectation, 365

Fibonacci numbers, *213*
FIFO queue, *302*
"fifteen" puzzle, *110*
first return time, 10, 128
flow, 118
fpras, 210
fugacity, 43
fully polynomial randomized approximation scheme, 210

gambler's ruin, 21, *34*, *126*, 246
Gaussian elimination chain, 362
generating function, 142
generating set, 28
geometric mixing time, 335
Gibbs distribution, 44
Gibbs sampler, 41
Glauber dynamics
definition, 42
for colorings, 41, 360
path coupling upper bound, 206, 207
for hardcore model, 44, 72
coupling from the past, 355
relaxation time, 181
for Ising model, 44, 185, 215
coupling from the past, 350
for product measure, 170
glued graphs, 144
complete, 81
lower bound, *86*

### PDF page 457 (book page 441)

strong stationary time upper bound, 82
hypercube
hitting time upper bound, *147*
strong stationary time, *148*
torus
bottleneck ratio lower bound, 91
hitting time upper bound, 128, 146
gluing (in networks), 120, 123
grand coupling, 69, 70, 351, 354
graph, 8
Cayley, 29
colorings, *see also* colorings
complete, 81
connected, *17*
degree of vertex, 8
diameter, 89
empty, *98*
expander, 196, *228*
glued, *see also* glued graphs
grid, 124
ladder, 224
loop, 9
multiple edges, 9
oriented, 118
proper coloring of, 38, *see also* colorings
regular, 10
counting lower bound, 88
simple random walk on, 8
Green's function, 120, 292
grid graph, 124
Ising model on, 226
group, 27
generating set of, 28
random walk on, 28, 75, 100, 190
symmetric, 75

halting state, 79
Hamming weight, 24
hardcore model, 42
Glauber dynamics for, 44
coupling from the past, 355
grand coupling upper bound, 72
relaxation time, 181
monotone, 309
with fugacity, 43, 72
harmonic function, 12, *18*, 117, 255
Harris inequality, 310
heat bath algorithm, *see also* Glauber dynamics
heat kernel, 281
Hellinger distance, 58, 286, *289*
hill climb algorithm, 40
hitting time, 10, 77, 117, 128
cycle identity, 133
upper bound on mixing time, 140
worst case, 129
hypercube, 23

lamplighter chain on, 277
random walk on, 28
$\ell^2$ upper bound, 173
bottleneck ratio, 183
coupling upper bound, 63
cover time, *158*
cutoff, 173, 265
distinguishing statistic lower bound, 95
eigenvalues and eigenfunctions of, 171
hitting time, *147*
relaxation time, 181
separation cutoff, 268
strong stationary time upper bound, 76, 79, 82
Wilson's method lower bound, 193

i.i.d., 60
increment distribution, 28
independent, 365
indicator function, 14
induced chain, 186, 301
inessential state, 15
interchange process, 323, 362
inverse distribution, 108
method of simulation, 378
irreducible chain, 7
Ising model, 44, 215
block dynamics, 223, 361
comparison of Glauber and Metropolis, 185
energy, 44
fast mixing at high temperature, 215
Gibbs distribution for, 44
Glauber dynamics for, 44
coupling from the past, 349
infinite temperature, 44
inverse temperature, 44
monotone, 305
on complete graph
mixing time bounds, 218
on cycle
mixing time pre-cutoff, 219
relaxation time, 314
on expander, *228*
on grid
relaxation time lower bound, 226
on tree, *228*
mixing time upper bound, 220
open problems, 359
partial order on configurations, 350
partition function, 44
positive correlations, 311
isoperimetric constant, 99

$k$-fuzz, *302*
Kac lemma, 296
Kirchhoff's node law, 118

$\ell^p(\pi)$ distance, 172

### PDF page 458 (book page 442)

$L$-reversal chain, *see also* Durrett chain
ladder graph, 224
lamplighter chain, 272, 362
mixing time, 275
on cycle, 277
on hypercube, 277
on torus, 277
relaxation time, 273
separation cutoff, 278
Laws of Large Numbers, 365
lazy version of a Markov chain, 8, *177*, 282
leaf, *17*, 65
level (of tree), 65
linear congruential sequence, 383
Lipschitz constant, 180, *212*
loop, 9
lower bound methods
bottleneck ratio, 89, 90
counting bound, 88
diameter bound, 89
distinguishing statistic, 92
Wilson's method, 192
lozenge tiling, 352
lumped chain, *see also* projection

Markov chain
aperiodic, 7
birth-and-death, 26
communicating classes of, 15
comparison of, *see also* comparison of Markov chains
continuous time, 280
Convergence Theorem, 52, *73*
coupling, 61
definition of, 2
ergodic theorem, 390
exclusion process, *see also* exclusion process
irreducible, 7
lamplighter, *see also* lamplighter chain
lazy version of, 8
mixing time of, 54
Monte Carlo method, 38, 348
null recurrent, 296
periodic, 7, *177*
positive recurrent, 296
product, *see also* product chain
projection of, 25, *34*
random mapping representation of, 6, 69
recurrent, 292
reversible, 14, 117
stationary distribution of, 9
time averages, 173
time reversal of, 14, *34*
time-inhomogeneous, 19, 113, 203
transient, 292
transitive, 29, *34*
unknown, 357

Markov property, 2
Markov's inequality, 365
Markovian coupling, 61, *73*
martingale, 243
Matthews method
lower bound on cover time, 151
upper bound on cover time, 151
maximum principle, *18*, 117
MCMC, *see also* Markov chain Monte Carlo method
metric space, 201, 373
Metropolis algorithm, 38
arbitrary base chain, 40
for colorings, 70, 180
for Ising model, 185
symmetric base chain, 38
minimum expectation of a stationary time, 336
mixing time, 54
$\ell^2$ upper bound, 172
Cesaro, 84
continuous time, 282
coupling upper bound, 62
hitting time upper bound, 140
path coupling upper bound, 204
relaxation time lower bound, 164
relaxation time upper bound, 163
monotone chains, 305
positive correlations, 312
Monotone Convergence Theorem, 369
monotone spin system, 309
Monte Carlo method, 38, 348
move-to-front chain, 82

Nash-Williams inequality, 124, 294
network, 116
infinite, 293
node, 116
node law, 118
null recurrent, 296

odd permutation, 101
Ohm's law, 118
optimal coupling, 50, 202
Optional Stopping Theorem, 245
order statistic, *388*
oriented edge, 118

Parallel Law, 120
parity (of permutation), 101
partition function, 44
path
metric, 203
random walk on, 60, *see also*
birth-and-death chain, *see also*
gambler's ruin, 121, 262
eigenvalues and eigenfunctions, 167, 168
path coupling, 201

### PDF page 459 (book page 443)

*(Index — two columns.)*

**Left column:**

- upper bound on mixing time, 204, 215
- patterns in coin tossing
  - cover time, 156
  - hitting time, *146*, 247
- perfect sampling, *see also* sampling, exact
- periodic chain, 7
  - eigenvalues of, *177*
- pivot chain for self-avoiding walk, 384
- Pólya's urn, 25, 125, *125*, 139
- positive correlations
  - definition of, 309
  - of product measures, 310
- positive recurrent, 295
- pre-cutoff, 262, 270
  - mixing time of Ising model on cycle, 219
- previsible sequence, 244
- probability
  - distribution, 364
  - measure, 363
  - space, 363
- product chain
  - eigenvalues and eigenfunctions of, 169, *177*
  - in continuous time, 285
  - spectral gap, 170
  - Wilson's method lower bound, 195
- projection, 25, *34*, 166
  - onto coordinate, 201
- proper colorings, *see also* colorings
- pseudorandom number generator, 382

- random adjacent transpositions, 232
  - comparison upper bound, 233
  - coupling upper bound, 233
  - single card lower bound, 235
  - Wilson's method lower bound, 235
- random colorings, 91
- random mapping representation, 6, 69
- random number generator, *see also* pseudorandom number generator
- random sample, 38
- Random Target Lemma, 129
- random transposition shuffle, 102, *111*
  - coupling upper bound, 104
  - lower bound, 102
  - relaxation time, 165
  - strong stationary time upper bound, 105, 112
- random variable, 364
- random walk
  - on $\mathbb{R}$, 243
  - on $\mathbb{Z}$, 30, 292, *303*
    - biased, 244
    - null recurrent, 295
  - on $\mathbb{Z}^d$, 291
    - recurrent for $d = 2$, 294
    - transient for $d = 3$, 294
  - on binary tree

**Right column:**

- bottleneck ratio lower bound, 92
- commute time, 133
- coupling upper bound, 66
- cover time, 152
- hitting time, *146*
- no cutoff, 267
- on cycle, 5, 8, *17*, 28, *34*, 78
  - bottleneck ratio, 183
  - coupling upper bound, 63
  - cover time, 150, *158*
  - eigenvalues and eigenfunctions, 165
  - hitting time upper bound, 144
  - last vertex visited, *86*
  - lower bound, 63
  - no cutoff, 267
  - spectral gap, 166
  - strong stationary time upper bound, 83, *86*
- on group, 27, 75, 100, 190
- on hypercube, 23, 28
  - $\ell^2$ upper bound, 173
  - bottleneck ratio, 183
  - coupling upper bound, 63
  - cover time, *158*
  - cutoff, 173, 265
  - distinguishing statistic lower bound, 95
  - eigenvalues and eigenfunctions of, 171
  - hitting time, *147*
  - relaxation time, 181
  - separation cutoff, 268
  - strong stationary time upper bound, 76, 79, 82
  - Wilson's method lower bound, 193
- on path, 60, *see also* birth-and-death chain, *see also* gambler's ruin, 121, 262
  - eigenvalues and eigenfunctions, 167, 168
- on torus, 64
  - coupling upper bound, 65, *73*
  - cover time, 153, *158*
  - hitting time, 137
  - perturbed, 189, *198*
- self-avoiding, 383
- simple, 8, 14, 116, 189
- weighted, 116
- randomized paths, 190
- Rayleigh's Monotonicity Law, 123, 293
- Rayleigh-Ritz theorem, 374
- recurrent, 292, *302*
- reflection principle, 30, 34, *34*
- regular graph, 10
  - counting lower bound, 88
- relaxation time, 163
  - bottleneck ratio bounds, 183
  - continuous time, 284
  - coupling upper bound, 180
  - mixing time lower bound, 163

### PDF page 460 (book page 444)

*(Index — two columns.)*

**Left column:**

- mixing time upper bound, 164
- variational characterization of, 182
- resistance, 116
- return probability, 142, 253, 301
- reversal, 236, *see also* Durrett chain
- reversed chain, *see also* time reversal
- reversed distribution, 55
- reversibility, 14, 117
  - detailed balance equations, 13
- riffle shuffle, 107, 114
  - counting lower bound, 110
  - generalized, *111*
  - strong stationary time upper bound, 109
- rising sequence, 107
- rooted tree, 65
- roots of unity, 165

- sampling, 377
  - and counting, 209
  - exact, 209, 354
- self-avoiding walk, 383, 384, *389*
- semi-random transpositions, 113
- separation distance, 79, 80, *86*, 362
  - total variation upper bound, 80
  - upper bound on total variation, 80
- Series Law, 120
- shift chain, *see also* patterns in coin tossing
- shuffle
  - cyclic-to-random, 113
  - move-to-front, 82
  - open problems, 360
  - random adjacent transposition, 232
    - comparison upper bound, 233
    - coupling upper bound, 233
    - single card lower bound, 235
    - Wilson's method lower bound, 235
  - random transposition, 102, *111*
    - coupling upper bound, 104
    - lower bound, 102
    - relaxation time, 165
    - strong stationary time upper bound, 105, 112
  - riffle, 107, 114
    - counting lower bound, 110
    - generalized, *111*
    - strong stationary time upper bound, 109
  - semi-random transpositions, 113
  - top-to-random, 75
    - cutoff, 261
    - lower bound, 96
    - strong stationary time upper bound, 79, 82, *86*
- simple random walk, 8, 116, 189
  - stationary distribution of, 10
- simplex, 382
- simulation
  - of random variables, 375, 377

**Right column:**

- sink, 118
- source, 118
- spectral gap, 163, *see also* relaxation time
  - absolute, 163
  - bottleneck ratio bounds, 183
  - variational characterization of, 182
- spectral theorem for symmetric matrices, 374
- spin system, 44
  - montone [sic], 309
- star, 91
- stationary distribution, 9
  - uniqueness of, 13, 17
- stationary time, 78, 84
  - strong, 78, 256
- Stirling's formula, 374
- stochastic domination, 306
- stochastic flow, *see also* grand coupling
- stopping time, *86*, 245
- Strassen's Theorem, 307
- strength
  - of flow, 118
- Strong Law of Large Numbers, 366
- strong stationary time, 78, 256
- submartingale, 243
- submultiplicativity
  - of $\bar{d}(t)$, 54
  - of $s(t)$, *86*
- supermartingale, 243, *259*
- support, 364
- symmetric group, 75, 100
- symmetric matrix, 374
- systematic updates, 360

- target time, 129, 130
- tensor product, 169
- Thomson's Principle, 122, 293
- tiling
  - domino, 384
  - lozenge, 352
- time averages, 173
- time reversal, 14, *34*, 55, 58, 68, 83, 108
- time-inhomogeneous Markov chain, 19, 113, 203
- top-to-random shuffle, 75
  - cutoff, 261
  - lower bound, 96
  - strong stationary time upper bound, 79, 82, *86*
- torus
  - definition of, 64
  - glued
    - bottleneck ratio lower bound, 91
    - hitting time upper bound, 146
  - lamplighter chain on, 277
  - random walk on
    - coupling upper bound, 65, *73*
    - cover time, 153, *158*

### PDF page 461 (book page 445)

*(Index — single column layout on this page.)*

- hitting time, 137
- perturbed, 189, *198*
- total variation distance, 47
  - coupling characterization of, 50
  - Hellinger distance upper bound, 287
  - monotonicity of, *57*
  - separation distance upper bound, 80
  - standardized $(d(t), \bar{d}(t))$, 53
  - upper bound on separation distance, 80
- transient, 292
- transition matrix
  - definition of, 2
  - eigenvalues of, 161, *177*
  - multiply on left, 5
  - multiply on right, 5
  - spectral representation of, 161
- transition probabilities, $t$-step, 5
- transition times, 280
- transitive
  - chain, 29, *34*, 58, 360
  - network, 132
- transportation metric, 201, *212*
- transpose (of a matrix), 374
- transposition, 101
- tree, *17*, 65
  - binary, 66, *see also* binary tree
  - effective resistance, 121
  - Ising model on, 220, *228*
  - rooted, 65
- triangle inequality, 373

- unbiasing
  - von Neumann, 376
- unit flow, 118
- unity
  - roots of, 165
- unknown chain
  - sampling from, 357
- up-right path, 33
- urn model
  - Ehrenfest, 24, *34*, 265
  - Pólya, 25, 125, *125*, 139

- variance, 365
- voltage, 118
- von Neumann unbiasing, 376

- Wald's identity, *86*
- Weak Law of Large Numbers, 365
- weighted random walk, 116
- Wilson's method, 192, 219, 235
- window (of cutoff), 262
- winning streak, 55, 66
  - time reversal, 68
- wreath product, 272

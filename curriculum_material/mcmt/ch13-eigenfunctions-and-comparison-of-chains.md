# Chapter 13 — Eigenfunctions and Comparison of Chains
*(PDF pages 196–216; book pages 180–200)*

### PDF page 196 (book page 180)

CHAPTER 13

# Eigenfunctions and Comparison of Chains

**13.1. Bounds on Spectral Gap via Contractions**

In Chapter 5 we used coupling to give a direct bound on the mixing time (see Corollary 5.5). We now show that coupling can also be used to obtain bounds on the relaxation time.

THEOREM 13.1 (M. F. Chen (1998)). *Let $\mathcal{X}$ be a metric space with metric $\rho$, and let $P$ be the transition matrix of a Markov chain with state space $\mathcal{X}$. Suppose there exists a constant $\theta < 1$ such that for each $x, y \in \mathcal{X}$ there exists a coupling $(X_1, Y_1)$ of $P(x, \cdot)$ and $P(y, \cdot)$ satisfying*

$$\mathbf{E}_{x,y}\left(\rho(X_1, Y_1)\right) \leq \theta\rho(x, y). \tag{13.1}$$

*If $\lambda \neq 1$ is an eigenvalue of $P$, then $|\lambda| \leq \theta$. In particular, the absolute spectral gap satisfies*

$$\gamma_\star \geq 1 - \theta.$$

The ***Lipschitz constant*** of a function $f : \mathcal{X} \to \mathbb{R}$ is defined by

$$\mathrm{Lip}(f) := \max_{\substack{x,y \in \mathcal{X} \\ x \neq y}} \frac{|f(x) - f(y)|}{\rho(x, y)}.$$

PROOF. For any function $f$,

$$|Pf(x) - Pf(y)| = |\mathbf{E}_{x,y}\left(f(X_1) - f(Y_1)\right)| \leq \mathbf{E}_{x,y}\left(|f(X_1) - f(Y_1)|\right).$$

By the definition of $\mathrm{Lip}(f)$ and the hypothesis (13.1),

$$|Pf(x) - Pf(y)| \leq \mathrm{Lip}(f)\mathbf{E}_{x,y}\left(\rho(X_1, Y_1)\right) \leq \theta\,\mathrm{Lip}(f)\rho(x, y).$$

This proves that

$$\mathrm{Lip}(Pf) \leq \theta\,\mathrm{Lip}(f).$$

Taking $\varphi$ to be a non-constant eigenfunction with eigenvalue $\lambda$,

$$|\lambda|\,\mathrm{Lip}(\varphi) = \mathrm{Lip}(\lambda\varphi) = \mathrm{Lip}(P\varphi) \leq \theta\,\mathrm{Lip}(\varphi).$$

$\blacksquare$

EXAMPLE 13.2 (Metropolis chain for random colorings). Recall the Metropolis chain whose stationary distribution is uniform over all proper $q$-colorings of a graph, introduced in Example 3.5. At each move this chain picks a vertex $v$ uniformly at random and a color $k$ uniformly at random, then recolors $v$ with $k$ if the resulting coloring is proper.

The proof of Theorem 5.8 constructed, in the case $q > 3\Delta$, a coupling $(X_1, Y_1)$ of $P(x, \cdot)$ with $P(y, \cdot)$ for each pair $(x, y)$ such that

$$\mathbf{E}\left(\rho(X_1, Y_1)\right) \leq \left(1 - \frac{1}{n(3\Delta + 1)}\right)\rho(x, y).$$

### PDF page 197 (book page 181)

Applying Theorem 13.1 shows that if $q > 3\Delta$, where $\Delta$ is the maximum degree of the graph, then

$$\gamma_\star \geq \frac{1}{n(3\Delta + 1)}.$$

EXAMPLE 13.3. Consider the Glauber dynamics for the hardcore model at fugacity $\lambda$, introduced in Section 3.3.4. In the proof of Theorem 5.9, for each pair $(x, y)$, a coupling $(X_1, Y_1)$ of $P(x, \cdot)$ with $P(y, \cdot)$ is constructed which satisfies

$$\mathbf{E}\left(\rho(X_1, Y_1)\right) \leq \left(1 - \frac{1}{n}\left[\frac{1 + \lambda(1 - \Delta)}{1 + \lambda}\right]\right)\rho(x, y).$$

Therefore,

$$\gamma_\star \geq \frac{1}{n}\left[\frac{1 + \lambda(1 - \Delta)}{1 + \lambda}\right].$$

EXAMPLE 13.4. Consider again the lazy random walk on the hypercube $\{0, 1\}^n$, taking the metric to be the Hamming distance $\rho(x, y) = \sum_{i=1}^{d} |x_i - y_i|$.

Let $(X_1, Y_1)$ be the coupling which updates the same coordinate in both chains with the same bit. The distance decreases by one if one among the $\rho(x, y)$ disagreeing coordinates is selected and otherwise remains the same. Thus,

$$\begin{aligned}
\mathbf{E}_{x,y}\left(\rho(X_1, Y_1)\right) &= \left(1 - \frac{\rho(x, y)}{n}\right)\rho(x, y) + \frac{\rho(x, y)}{n}(\rho(x, y) - 1) \\
&= \left(1 - \frac{1}{n}\right)\rho(x, y).
\end{aligned}$$

Applying Theorem 13.1 yields the bound $\gamma_\star \geq n^{-1}$. In Example 12.16 it was shown that $\gamma_\star = n^{-1}$, so the bound of Theorem 13.1 is sharp in this case.

REMARK 13.5. Theorem 13.1 can be combined with Theorem 12.4 to get a bound on mixing time when there is a coupling which contracts, in the reversible case. However, we will obtain a better bound by a different method in Corollary 14.8.

**13.2. The Dirichlet Form and the Bottleneck Ratio**

**13.2.1. The Dirichlet form.** Let $P$ be a reversible transition matrix with stationary distribution $\pi$. The ***Dirichlet form*** associated to the pair $(P, \pi)$ is defined for functions $f$ and $h$ on $\mathcal{X}$ by

$$\mathcal{E}(f, h) := \langle (I - P)f, h \rangle_\pi.$$

LEMMA 13.6. *For a reversible transition matrix $P$ with stationary distribution $\pi$, if*

$$\mathcal{E}(f) := \frac{1}{2}\sum_{x,y \in \mathcal{X}} \left[f(x) - f(y)\right]^2 \pi(x)P(x, y), \tag{13.2}$$

*then $\mathcal{E}(f) = \mathcal{E}(f, f)$.*

PROOF. Expanding the square on the right-hand side of (13.2) shows that

$$\begin{aligned}
\mathcal{E}(f) = &\frac{1}{2}\sum_{x,y \in \mathcal{X}} f(x)^2 \pi(x)P(x, y) - \sum_{x,y \in \mathcal{X}} f(x)f(y)\pi(x)P(x, y) \\
&+ \frac{1}{2}\sum_{x,y \in \mathcal{X}} f(y)^2 \pi(x)P(x, y).
\end{aligned}$$

### PDF page 198 (book page 182)

By reversibility, $\pi(x)P(x, y) = \pi(y)P(y, x)$, and the first and last terms above are equal to the common value

$$\frac{1}{2}\sum_{x \in \mathcal{X}} f(x)^2 \pi(x) \sum_{y \in \mathcal{X}} P(x, y) = \frac{1}{2}\sum_{x \in \mathcal{X}} f(x)^2 \pi(x) = \langle f, f \rangle_\pi.$$

Therefore,

$$\mathcal{E}(f) = \langle f, f \rangle_\pi - \langle f, Pf \rangle_\pi = \mathcal{E}(f, f).$$

$\blacksquare$

We write $f \perp_\pi g$ to mean $\langle f, g \rangle_\pi = 0$. Let $\mathbf{1}$ denote the function on $\Omega$ which is identically 1. Observe that $E_\pi(f) = \langle f, \mathbf{1} \rangle_\pi$.

LEMMA 13.7. *Let $P$ be the transition matrix for a reversible Markov chain. The spectral gap $\gamma = 1 - \lambda_2$ satisfies*

$$\gamma = \min_{\substack{f \in \mathbb{R}^{\mathcal{X}} \\ f \perp_\pi \mathbf{1}, \, \|f\|_2 = 1}} \mathcal{E}(f) = \min_{\substack{f \in \mathbb{R}^{\mathcal{X}} \\ f \perp_\pi \mathbf{1}, \, f \not\equiv 0}} \frac{\mathcal{E}(f)}{\|f\|_2^2}. \tag{13.3}$$

Any function $f$ thus gives an upper bound on the gap $\gamma$, a frequently useful technique. See, for example, the proof of the upper bound in Theorem 13.10, and Exercise 15.1.

REMARK 13.8. Since $\mathcal{E}(f) = \mathcal{E}(f + c)$ for any constant $c$, if $f$ is a non-constant function $f : \mathbb{R} \to \mathcal{X}$, then

$$\frac{\mathcal{E}(f)}{\mathrm{Var}_\pi(f)} = \frac{\mathcal{E}(f - E_\pi(f))}{\|f - E_\pi(f)\|_2^2}.$$

Therefore,

$$\gamma = \min_{\substack{f \in \mathbb{R}^{\mathcal{X}} \\ \mathrm{Var}_\pi(f) \neq 0}} \frac{\mathcal{E}(f)}{\mathrm{Var}_\pi(f)}.$$

REMARK 13.9. If $(X_0, X_1)$ is one step of the Markov chain with transition matrix $P$ and initial distribution $\pi$, then

$$\mathcal{E}(f) = \frac{1}{2}\mathbf{E}_\pi(f(X_0) - f(X_1))^2. \tag{13.4}$$

Also if $(X, Y)$ are independent with distribution $\pi$, then

$$\mathrm{Var}_\pi(f) = \frac{1}{2}E_{\pi \times \pi}(f(X) - f(Y))^2. \tag{13.5}$$

PROOF OF LEMMA 13.7. Let $n = |\mathcal{X}|$. As noted in the proof of Lemma 12.2, if $f_1, f_2, \ldots, f_n$ are the eigenfunctions of $P$ associated to the eigenvalues ordered as in (12.7), then $\{f_k\}$ is an orthonormal basis for the inner-product space $(\mathbb{R}^n, \langle \cdot, \cdot \rangle_\pi)$. We can and will always take $f_1 = \mathbf{1}$. Therefore, if $\|f\|_2 = 1$ and $f \perp_\pi \mathbf{1}$. then $f = \sum_{j=2}^{|\mathcal{X}|} a_j f_j$ where $\sum_{j=2}^{|\mathcal{X}|} a_j^2 = 1$. Thus,

$$\langle (I - P)f, f \rangle_\pi = \sum_{j=2}^{|\mathcal{X}|} a_j^2 (1 - \lambda_j) \geq 1 - \lambda_2,$$

from which follows the first equality in (13.3). To obtain the second equality, for $f \in \mathbb{R}^{\mathcal{X}}$ satisfying $f \perp_\pi \mathbf{1}$ and $f \not\equiv 0$, note that $\tilde{f} := f/\|f\|_2$ satisfies $\|\tilde{f}\|_2 = 1$ and $\mathcal{E}(\tilde{f}) = \mathcal{E}f/\|f\|_2^2$. $\blacksquare$

### PDF page 199 (book page 183)

**13.2.2. The bottleneck ratio revisited.** We have already met the bottleneck ratio $\Phi_\star$ in Section 7.2, where we established a lower bound on $t_{\mathrm{mix}}$ directly in terms of $\Phi_\star$.

The following theorem bounds $\gamma$ in terms of the bottleneck ratio:

**Theorem 13.10** (Sinclair and Jerrum (1989), Lawler and Sokal (1988)). *Let $\lambda_2$ be the second largest eigenvalue of a reversible transition matrix $P$, and let $\gamma = 1 - \lambda_2$. Then*

$$ \frac{\Phi_\star^2}{2} \leq \gamma \leq 2\Phi_\star. \tag{13.6} $$

While the lower and upper bounds in Theorem 13.10 look quite different, there exist both examples where the upper bound is the correct order and examples where the lower bound is the correct order. Before proving the theorem, we consider such examples.

**Example 13.11** (Lazy random walk on the $n$-dimensional hypercube). Consider the set $S = \{\boldsymbol{x} : x^1 = 0\}$. Then

$$ \Phi(S) = 2 \sum_{x \in S, y \in S^c} 2^{-n} P(x,y) = 2^{-n+1} 2^{n-1} n^{-1}(1/2) = \frac{1}{2n}. $$

Therefore, $\Phi_\star \leq 1/(2n)$. We know that $\gamma = n^{-1}$ (see Example 12.16), whence applying Theorem 13.10 shows that $\frac{1}{n} \leq 2\Phi_\star$. That is, $2\Phi_\star = n^{-1} = \gamma$, showing that for this example, the upper bound in (13.6) is sharp.

**Example 13.12** (Lazy random walk on the $2n$-cycle). Using the computations in Section 12.3.1 (for the non-lazy chain),

$$ \lambda_2 = \frac{\cos(\pi/n) + 1}{2} = 1 - \frac{\pi^2}{4n^2} + O(n^{-4}). $$

Therefore, $\gamma = \pi^2/(4n^2) + O(n^{-4})$.

For any set $S$,

$$ \Phi(S) = \frac{|\partial S| \left(\frac{1}{4}\right) \left(\frac{1}{2n}\right)}{\frac{|S|}{2n}} $$

where $\partial S = \{(x,y) : x \in S, \; y \notin S\}$. It is clear that the minimum of $\Phi(S)$ over sets $S$ with $\pi(S) \leq 1/2$ is attained at a segment of length $n$, whence $\Phi_\star = 1/(2n)$. The lower bound in (13.6) gives the bound

$$ \gamma \geq \frac{1}{8n^2}, $$

which is of the correct order.

**Proof of the upper bound in Theorem 13.10.** By Lemmas 13.7 and 13.6,

$$ \gamma = \min_{\substack{f \not\equiv 0 \\ E_\pi(f)=0}} \frac{\sum_{x,y \in \mathcal{X}} \pi(x)P(x,y)\,[f(x) - f(y)]^2}{\sum_{x,y \in \mathcal{X}} \pi(x)\pi(y)\,[f(x) - f(y)]^2}. \tag{13.7} $$

For any $S$ with $\pi(S) \leq 1/2$ define the function $f_S$ by

$$ f_S(x) = \begin{cases} -\pi(S^c) & \text{for } x \in S, \\ \pi(S) & \text{for } x \notin S. \end{cases} $$

### PDF page 200 (book page 184)

Since $E_\pi(f_s) = 0$, it follows from (13.7) that

$$ \gamma \leq \frac{2Q(S,S^c)}{2\pi(S)\pi(S^c)} \leq \frac{2Q(S,S^c)}{\pi(S)} \leq 2\Phi(S). $$

Since this holds for all $S$, the upper bound is proved. $\blacksquare$

**13.2.3. Proof of the lower bound in Theorem 13.10\*.** We need the following lemma:

**Lemma 13.13.** *Given a non-negative function $\psi$ defined on $\mathcal{X}$, order $\mathcal{X}$ so that $\psi$ is non-increasing. If $\pi\{\psi > 0\} \leq 1/2$, then*

$$ E_\pi(\psi) \leq \Phi_\star^{-1} \sum_{\substack{x,y \in \mathcal{X} \\ x < y}} [\psi(x) - \psi(y)]\, Q(x,y). $$

*Proof.* Let $S = \{x : \psi(x) > t\}$ with $t > 0$. Recalling that $\Phi_\star$ is defined as a minimum in (7.7), we have

$$ \Phi_\star \leq \frac{Q(S,S^c)}{\pi(S)} = \frac{\sum_{x,y \in \mathcal{X}} Q(x,y)\mathbf{1}_{\{\psi(x)>t\geq\psi(y)\}}}{\pi\{\psi > t\}}. $$

Rearranging and noting that $\psi(x) > \psi(y)$ only for $x < y$,

$$ \pi\{\psi > t\} \leq \Phi_\star^{-1} \sum_{x<y} Q(x,y)\mathbf{1}_{\{\psi(x)>t\geq\psi(y)\}}. $$

Integrating over $t$, noting that $\int_0^\infty \mathbf{1}_{\{\psi(x)>t\geq\psi(y)\}}dt = \psi(x) - \psi(y)$, and using Exercise 13.1 shows that

$$ E_\pi(\psi) \leq \Phi_\star^{-1} \sum_{x<y} [\psi(x) - \psi(y)]\, Q(x,y). $$

$\blacksquare$

To complete the proof of the lower bound in Theorem 13.10, first observe that if $\gamma \geq 1/2$, then there is nothing to prove because $\Phi_\star \leq 1$. Thus we will assume $\gamma < 1/2$. Let $f_2$ be an eigenfunction corresponding to the eigenvalue $\lambda_2$, so that $Pf_2 = \lambda_2 f_2$. Assume that $\pi\{f_2 > 0\} \leq 1/2$. (If not, use $-f_2$ instead.) Defining $f := \max\{f_2, 0\}$,

$$ (I - P)f(x) \leq \gamma f(x) \quad \text{for all } x. \tag{13.8} $$

This is verified separately in the two cases $f(x) = 0$ and $f(x) > 0$. In the former case, (13.8) reduces to $-Pf(x) \leq 0$, which holds because $f$ is non-negative everywhere. In the case $f(x) > 0$, note that since $f \geq f_2$,

$$ (I - P)f(x) = f_2(x) - Pf(x) \leq (I - P)f_2(x) = (1 - \lambda_2)f_2(x) = \gamma f(x). $$

Because $f \geq 0$,

$$ \langle (I - P)f, f \rangle_\pi \leq \gamma \langle f, f \rangle_\pi. $$

Equivalently,

$$ \gamma \geq \frac{\langle (I - P)f, f \rangle_\pi}{\langle f, f \rangle_\pi}. $$

Note there is no contradiction to (13.3) because $E_\pi(f) \neq 0$. Applying Lemma 13.13 with $\psi = f^2$ shows that

$$ \langle f, f \rangle_\pi^2 \leq \Phi_\star^{-2} \left[ \sum_{x<y} \left[ f^2(x) - f^2(y) \right] Q(x,y) \right]^2. $$

### PDF page 201 (book page 185)

By the Cauchy-Schwarz inequality,

$$ \langle f, f \rangle_\pi^2 \leq \Phi_\star^{-2} \left[ \sum_{x<y} [f(x) - f(y)]^2\, Q(x,y) \right] \left[ \sum_{x<y} [f(x) + f(y)]^2\, Q(x,y) \right]. $$

Using the identity (13.2) of Lemma 13.6 and

$$ [f(x) + f(y)]^2 = 2f^2(x) + 2f^2(y) - [f(x) - f(y)]^2, $$

we find that

$$ \langle f, f \rangle_\pi^2 \leq \Phi_\star^{-2} \langle (I - P)f, f \rangle_\pi \left[ 2\langle f, f \rangle_\pi - \langle (I - P)f, f \rangle_\pi \right]. $$

Let $R := \langle (I - P)f, f \rangle_\pi / \langle f, f \rangle_\pi$ and divide by $\langle f, f \rangle_\pi^2$ to show that

$$ \Phi_\star^2 \leq R(2 - R) $$

and

$$ 1 - \Phi_\star^2 \geq 1 - 2R + R^2 = (1 - R)^2 \geq (1 - \gamma)^2. $$

Finally,

$$ \left( 1 - \frac{\Phi_\star^2}{2} \right)^2 \geq 1 - \Phi_\star^2 \geq (1 - \gamma)^2, $$

proving that $\gamma \geq \Phi_\star^2/2$, as required.

**13.3. Simple Comparison of Markov Chains**

If the transition matrix of a chain can be bounded by a constant multiple of the transition matrix for another chain and the stationary distributions of the chains agree, then Lemma 13.7 provides an easy way to compare the spectral gaps. This technique is illustrated by the following example:

**Example 13.14** (Metropolis and Glauber dynamics for Ising). For a graph with vertex set $V$ with $|V| = n$, let $\pi$ be the Ising probability measure on $\{-1, 1\}^V$:

$$ \pi(\sigma) = Z(\beta)^{-1} \exp\left( \beta \sum_{\substack{v,w \in V \\ v \sim w}} \sigma(v)\sigma(w) \right). $$

(See Section 3.3.5.) The Glauber dynamics chain moves by selecting a vertex $v$ at random and placing a positive spin at $v$ with probability

$$ p(\sigma, v) = \frac{e^{\beta S(\sigma,v)}}{e^{\beta S(\sigma,v)} + e^{-\beta S(\sigma,v)}}, $$

where $S(\sigma, w) := \sum_{u \,:\, u \sim w} \sigma(u)$. Therefore, if $P$ denotes the transition matrix for the Glauber chain, then for all configurations $\sigma$ and $\sigma'$ which differ only at the vertex $v$, we have

$$ P(\sigma, \sigma') = \frac{1}{n} \cdot \frac{e^{\beta\sigma'(v)S(\sigma,v)}}{e^{\beta\sigma'(v)S(\sigma,v)} + e^{-\beta\sigma'(v)S(\sigma,v)}} = \frac{1}{n}\left( \frac{r^2}{1 + r^2} \right), \tag{13.9} $$

where $r = e^{\beta\sigma'(v)S(\sigma,v)}$.

We let $\widetilde{P}$ denote the transition matrix for the Metropolis chain using the base chain which selects a vertex $v$ at random and then changes the spin at $v$. If $\sigma$ and $\sigma'$ are two configurations which disagree at the single site $v$, then

$$ \widetilde{P}(\sigma, \sigma') = \frac{1}{n}\left( 1 \wedge e^{2\beta\sigma'(v)S(\sigma,v)} \right) = \frac{1}{n}\left( 1 \wedge r^2 \right). \tag{13.10} $$

### PDF page 202 (book page 186)

(See Section 3.2.)

If $\mathcal{E}$ is the Dirichlet form corresponding to $P$ and $\widetilde{\mathcal{E}}$ is the Dirichlet form corresponding to $\widetilde{P}$, then from (13.9) and (13.10)

$$ \frac{1}{2} \le \frac{\mathcal{E}(f)}{\widetilde{\mathcal{E}}(f)} \le 1. $$

Therefore, the gaps are related by

$$ \gamma \le \widetilde{\gamma} \le 2\gamma. $$

EXAMPLE 13.15 (Induced chains). If $(X_t)$ is a Markov chain with transition matrix $P$, for a non-empty subset $A \subset \mathcal{X}$, the **induced chain on** $A$ is the chain with state space $A$ and transition matrix

$$ P_A(x,y) = \mathbf{P}_x\{X_{\tau_A^+} = y\} $$

for all $x, y \in A$. Intuitively, the induced chain is the original chain, but watched only during the time it spends at states in $A$.

THEOREM 13.16. *Let $(X_t)$ be a reversible Markov chain on $\mathcal{X}$ with stationary measure $\pi$ and spectral gap $\gamma$. Let $A \subset \mathcal{X}$ be non-empty and let $\gamma_A$ be the spectral gap for the chain induced on $A$. Then $\gamma_A \ge \gamma$.*

PROOF.

$$ \pi(x)P_A(x,y) = \pi(y)P_A(y,x), $$

as is seen by summing over paths, so $P_A$ is reversible with respect to the conditional distribution $\pi_A(B) := \pi(A \cap B)/\pi(A)$. By Lemma 13.7, there exists $\varphi : A \to \mathbb{R}$ with $\langle \varphi, \mathbf{1} \rangle_{\pi_A} = 0$ and

$$ \gamma_A = \frac{\mathcal{E}_A(\varphi)}{\|\varphi\|_{\ell^2(\pi_A)}^2}. $$

Let $\psi : \mathcal{X} \to \mathbb{R}$ be the harmonic extension of $\varphi$:

$$ \psi(x) := \mathbf{E}_x[\varphi(X_{\tau_A})]. $$

Observe that for $x \in A$,

$$ P\psi(x) = \sum_{y \in \mathcal{X}} P(x,y)\psi(y) = \sum_{y \in \mathcal{X}} P(x,y)\mathbf{E}_y[\varphi(X_{\tau_A})] = \mathbf{E}_x[\varphi(X_{\tau_A^+})] = P_A\varphi(x). $$

Also, $(I - P)\psi(y) = 0$ for $y \notin A$. Now

$$ \begin{aligned} \mathcal{E}(\psi) = \langle (I-P)\psi, \psi \rangle_\pi &= \sum_{x \in A} [(I-P)\psi(x)]\psi(x)\pi(x) \\ &= \sum_{x \in A} [(I-P_A)\varphi(x)]\varphi(x)\pi(x) = \pi(A)\mathcal{E}_A(\varphi). \end{aligned} $$

Also, writing $\bar{\psi} = \langle \psi, \mathbf{1} \rangle_\pi$, we have

$$ \mathrm{Var}_\pi(\psi) \ge \sum_{x \in A} [\varphi(x) - \bar{\psi}]^2 \pi(x) \ge \pi(A) \sum_{x \in A} \varphi(x)^2 \pi_A(x)\,. $$

Thus

$$ \gamma \le \frac{\mathcal{E}(\psi)}{\mathrm{Var}_\pi(\psi)} \le \frac{\pi(A)\mathcal{E}_A(\varphi)}{\pi(A)\|\varphi\|_{\ell^2(\pi_A)}^2} = \gamma_A. $$

$\blacksquare$

### PDF page 203 (book page 187)

EXAMPLE 13.17. Consider a random walk on a $d$-regular graph. Letting $A = \{a, b\}$, we have

$$ P_A = \begin{pmatrix} 1 - p & p \\ p & 1 - p \end{pmatrix} , $$

where $p = \mathbf{P}_a\{\tau_b < \tau_a^+\}$. Thus,

$$ \frac{2\mathcal{C}(a \leftrightarrow b)}{d} = 2p = \gamma_A \ge \gamma\,. $$

The following gives a general comparison between chains when the ratios of both the Dirichlet forms and the stationary distributions can be bounded by constants.

LEMMA 13.18. *Let $P$ and $\tilde{P}$ be reversible transition matrices with stationary distributions $\pi$ and $\tilde{\pi}$, respectively. If $\tilde{\mathcal{E}}(f) \le \alpha\mathcal{E}(f)$ for all $f$, then*

$$ \tilde{\gamma} \le \left[ \max_{x \in \mathcal{X}} \frac{\pi(x)}{\tilde{\pi}(x)} \right] \alpha\gamma. \tag{13.11} $$

In applications, $P$ is the chain of interest, $\tilde{P}$ is a chain whose gap can be estimated, and Lemma 13.18 is used to obtain a lower bound on $\gamma$.

PROOF. Recall that $m \mapsto E_\pi(f - m)^2$ is minimized at $m = E_\pi(f)$, and the minimum equals $\mathrm{Var}_\pi(f)$. Therefore,

$$ \mathrm{Var}_\pi(f) \le E_\pi(f - E_{\tilde{\pi}}(f))^2 = \sum_{x \in \mathcal{X}} [f(x) - E_{\tilde{\pi}}(f)]^2 \pi(x). $$

If $c(\pi, \tilde{\pi}) := \max_{x \in \mathcal{X}} \pi(x)/\tilde{\pi}(x)$, then the right-hand side above is bounded by

$$ c(\pi, \tilde{\pi}) \sum_{x \in \mathcal{X}} [f(x) - E_{\tilde{\pi}}(f)]^2 \tilde{\pi}(x) = c(\pi, \tilde{\pi})\,\mathrm{Var}_{\tilde{\pi}}(f), $$

whence

$$ \frac{1}{\mathrm{Var}_{\tilde{\pi}}(f)} \le \frac{c(\pi, \tilde{\pi})}{\mathrm{Var}_\pi(f)}. \tag{13.12} $$

By the hypothesis that $\tilde{\mathcal{E}}(f) \le \alpha\mathcal{E}f$ and (13.12) we see that for any $f \in \mathbb{R}^{\mathcal{X}}$ with $\mathrm{Var}_\pi(f) \ne 0$,

$$ \frac{\tilde{\mathcal{E}}(f)}{\mathrm{Var}_{\tilde{\pi}}(f)} \le \alpha \cdot c(\pi, \tilde{\pi}) \cdot \frac{\mathcal{E}(f)}{\mathrm{Var}_\pi(f)}. $$

By Remark 13.8, taking the minimum over all non-constant $f \in \mathbb{R}^{\mathcal{X}}$ on both sides of the above inequality proves (13.11). $\blacksquare$

REMARK 13.19. If the transition probabilities satisfies $\tilde{P}(x,y) \le \beta P(x,y)$, then $\tilde{\mathcal{E}}(f) \le \beta c(\tilde{\pi}, \pi)\mathcal{E}(f)$, and Lemma 13.18 can be applied. In the next section, we will see a more powerful method to verify the hypothesis of the lemma.

**13.4. The Path Method**

Recall that in Section 5.3.3 we used coupling to show that for lazy simple random walk on the $d$-dimensional torus $\mathbb{Z}_n^d$ we have $t_{\mathrm{mix}} \le C_d n^2$. If some edges are removed from the graph (e.g. some subset of the horizontal edges at even heights, see Figure 13.1), then coupling cannot be applied due to the irregular pattern, and the simple comparison criterion of Remark 13.19 does not apply, since the sets of allowable transitions do not coincide. In this section, we show how such perturbations of "nice" chains can be studied via comparison. The technique will

### PDF page 204 (book page 188)

*[Figure: a 5×5 grid of unit squares (a subset of a box in $\mathbb{Z}^2$) with several internal horizontal edges removed at various rows, leaving an irregular lattice.]*

FIGURE 13.1. A subset of a box in $\mathbb{Z}^2$ with some edges removed.

be exploited later when we study site Glauber dynamics via comparison with block dynamics in Section 15.5 and some further shuffling methods in Chapter 16.

The following theorem allows one to compare the behavior of similar reversible chains to achieve bounds on the relaxation time.

For a reversible transition matrix $P$, define $E = \{(x,y) : P(x,y) > 0\}$. An **$E$-path** from $x$ to $y$ is a sequence $\Gamma = (e_1, e_2, \ldots, e_m)$ of edges in $E$ such that $e_1 = (x, x_1)$, $e_2 = (x_1, x_2)$, $\ldots$, $e_m = (x_{m-1}, y)$ for some vertices $x_1, \ldots, x_{m-1} \in \mathcal{X}$. The length of an $E$-path $\Gamma$ is denoted by $|\Gamma|$. As usual, $Q(x,y)$ denotes $\pi(x)P(x,y)$.

Let $P$ and $\tilde{P}$ be two reversible transition matrices with stationary distributions $\pi$ and $\tilde{\pi}$, respectively. Supposing that for each $(x,y) \in \tilde{E}$ there is an $E$-path from $x$ to $y$, choose one and denote it by $\Gamma_{xy}$. Given such a choice of paths, define the **congestion ratio** $B$ by

$$ B := \max_{e \in E} \left( \frac{1}{Q(e)} \sum_{\substack{x,y \\ \Gamma_{xy} \ni e}} \tilde{Q}(x,y)|\Gamma_{xy}| \right). \tag{13.13} $$

THEOREM 13.20 (Comparison via Paths). *Let $P$ and $\tilde{P}$ be reversible transition matrices, with stationary distributions $\pi$ and $\tilde{\pi}$, respectively. If $B$ is the congestion ratio for a choice of $E$-paths, as defined in (13.13), then for all functions $f : \mathcal{X} \to \mathbb{R}$,*

$$ \tilde{\mathcal{E}}(f) \le B\mathcal{E}(f). \tag{13.14} $$

*Consequently,*

$$ \tilde{\gamma} \le \left[ \max_{x \in \mathcal{X}} \frac{\pi(x)}{\tilde{\pi}(x)} \right] B\gamma. \tag{13.15} $$

COROLLARY 13.21 (Method of Canonical Paths). *Let $P$ be a reversible and irreducible transition matrix with stationary distribution $\pi$. Suppose $\Gamma_{xy}$ is a choice of $E$-path for each $x$ and $y$, and let*

$$ B = \max_{e \in E} \frac{1}{Q(e)} \sum_{\substack{x,y \\ \Gamma_{xy} \ni e}} \pi(x)\pi(y)|\Gamma_{xy}|. $$

*Then the spectral gap satisfies $\gamma \ge B^{-1}$.*

### PDF page 205 (book page 189)

*Proof.* Let $\tilde{P}(x,y) = \pi(y)$, and observe that the stationary measure for $\tilde{P}$ is clearly $\tilde{\pi} = \pi$. For $f \in \mathbb{R}^{\mathcal{X}}$ such that $0 = E_\pi(f) = \langle f, \mathbf{1} \rangle_\pi$,

$$ \tilde{\mathcal{E}}(f) = \frac{1}{2} \sum_{x,y \in \mathcal{X}} [f(x) - f(y)]^2 \, \pi(x)\pi(y) = \|f\|_2^2. $$

Applying Theorem 13.20 shows that $\mathcal{E}(f) \geq B^{-1}\|f\|_2^2$. Lemma 13.7 implies that $\gamma \geq B^{-1}$. $\blacksquare$

For an application of this Corollary, see Exercise 13.10.

*Proof of Theorem 13.20.* For a directed edge $e = (z,w)$, we define $\nabla f(e) := f(w) - f(z)$. Observe that

$$ 2\tilde{\mathcal{E}}(f) = \sum_{(x,y) \in \tilde{E}} \tilde{Q}(x,y)[f(x) - f(y)]^2 = \sum_{x,y} \tilde{Q}(x,y) \left[ \sum_{e \in \Gamma_{x,y}} \nabla f(e) \right]^2 . $$

Applying the Cauchy-Schwarz inequality yields

$$ 2\tilde{\mathcal{E}}(f) \leq \sum_{x,y} \tilde{Q}(x,y)|\Gamma_{xy}| \sum_{e \in \Gamma_{x,y}} [\nabla f(e)]^2 = \sum_{e \in E} \left[ \sum_{\Gamma_{xy} \ni e} \tilde{Q}(x,y)|\Gamma_{xy}| \right] [\nabla f(e)]^2 . $$

By the definition of the congestion ratio, the right-hand side is bounded above by

$$ \sum_{(z,w) \in E} BQ(z,w)[f(w) - f(z)]^2 = 2B\mathcal{E}(f), $$

completing the proof of (13.14).

The inequality (13.15) follows from Lemma 13.18. $\blacksquare$

*Example* 13.22 (Comparison for simple random walks on graphs). If two graphs have the same vertex set but different edge sets $E$ and $\tilde{E}$, then

$$ Q(x,y) = \frac{1}{2|E|}\mathbf{1}_{(x,y) \in E} \quad \text{and} \quad \tilde{Q}(x,y) = \frac{1}{2|\tilde{E}|}\mathbf{1}_{(x,y) \in \tilde{E}}. $$

Therefore, the congestion ratio is simply

$$ B = \left( \max_{e \in E} \sum_{\Gamma_{xy} \ni e} |\Gamma_{xy}| \right) \frac{|E|}{|\tilde{E}|}. $$

In our motivating example, we only removed horizontal edges at even heights from the torus. Since all odd-height edges remain, we can take $|\Gamma_{xy}| \leq 3$ since we can traverse any missing edge in the torus by moving upwards, then across the edge of odd height, and then downwards. The horizontal edge in this path would then be used by at most 3 paths $\Gamma$ (including the edge itself). Since we removed at most one quarter of the edges, $B \leq 12$.

Thus the relaxation time for the perturbed torus also satisfies $t_{\rm rel} = O(n^2)$.

Comparison via paths can be combined with the induced chain to compare chains with different state spaces; see Exercise 13.11.

### PDF page 206 (book page 190)

**13.4.1. Averaging over paths.** In Theorem 13.20, for each $e = (x,y) \in \tilde{E}$ we select a single path $\Gamma_{xy}$ from $x$ to $y$ using edges in $E$. Generally there will be many paths between $x$ and $y$ using edges from $E$, and it is often possible to reduce the worst-case congestion by specifying a measure $\nu_{xy}$ on the set $\mathcal{P}_{xy}$ of paths from $x$ to $y$. One can think of this measure as describing how to select a random path between $x$ and $y$.

In this case, the congestion ratio is given by

$$ B := \max_{e \in E} \left( \frac{1}{Q(e)} \sum_{(x,y) \in \tilde{E}} \tilde{Q}(x,y) \sum_{\Gamma : e \in \Gamma \in \mathcal{P}_{xy}} \nu_{xy}(\Gamma)|\Gamma| \right). \tag{13.16} $$

*Corollary* 13.23. *Let $P$ and $\tilde{P}$ be two reversible transition matrices with stationary distributions $\pi$ and $\tilde{\pi}$, respectively. If $B$ is the congestion ratio for a choice of randomized $E$-paths, as defined in (13.16), then*

$$ \tilde{\gamma} \leq \left[ \max_{x \in \mathcal{X}} \frac{\pi(x)}{\tilde{\pi}(x)} \right] B\gamma. \tag{13.17} $$

The proof of Corollary 13.23 is exactly parallel to that of Theorem 13.20. Exercise 13.3 asks you to fill in the details.

**13.4.2. Comparison of random walks on groups.** When the two Markov chains that we are attempting to compare are both random walks on the same group $G$, it is enough to write the support of the increments of one walk in terms of the support of the increments of the other. Then symmetry can be used to get an evenly-distributed collection of paths.

To fix notation, let $\mu$ and $\tilde{\mu}$ be the increment measures of two irreducible and reversible random walks on a finite group $G$. Let $S$ and $\tilde{S}$ be the support sets of $\mu$ and $\tilde{\mu}$, respectively, and, for each $a \in \tilde{S}$, fix an expansion $a = s_1 \ldots s_k$, where $s_i \in S$ for $1 \leq i \leq k$. Write $N(s,a)$ for the number of times $s \in S$ appears in the expansion of $a \in \tilde{S}$, and let $|a| = \sum_{s \in S} N(s,a)$ be the total number of factors in the expansion of $a$.

In this case the appropriate congestion ratio is

$$ B := \max_{s \in S} \frac{1}{\mu(s)} \sum_{a \in \tilde{S}} \tilde{\mu}(a)N(s,a) \, |a|. \tag{13.18} $$

*Corollary* 13.24. *Let $\mu$ and $\tilde{\mu}$ be the increment measures of two irreducible and reversible random walks on a finite group $G$. Let $\gamma$ and $\tilde{\gamma}$ be their spectral gaps, respectively.*

*Then*

$$ \tilde{\gamma} \leq B\gamma, \tag{13.19} $$

*where $B$ is the congestion ratio defined in (13.18).*

*Proof.* Let $P$ and $\tilde{P}$ be the transition matrices of the random walks on $G$ with increment measures $\mu$ and $\tilde{\mu}$, respectively. Let $E = \{(g,h)|P(g,h) > 0\}$. For $e = (g,h) \in E$, we have

$$ Q(e) = Q(g,h) = \frac{P(g,h)}{|G|} = \frac{\mu(hg^{-1})}{|G|}. $$

(Recall that the uniform distribution is stationary for every random walk on $G$.) Define $\tilde{E}$ and $\tilde{Q}$ in a parallel way.

### PDF page 207 (book page 191)

To obtain a path corresponding to an arbitrary edge $(b,c) \in \tilde{E}$, write $c = ab$ where $a \in \tilde{S}$ has generator expansion $s_1 \ldots s_k$. Then

$$ c = s_1 \ldots s_k b $$

determines a path $\Gamma_{bc}$ from $b$ to $c$ using only edges in $E$.

We now estimate the congestion ratio

$$ \max_{e \in E} \left( \frac{1}{Q(e)} \sum_{\substack{g,h \\ \Gamma_{gh} \ni e}} \tilde{Q}(g,h)|\Gamma_{gh}| \right). \tag{13.20} $$

Fix an edge $e = \{b, sb\} \in E$ and $a \in \tilde{S}$. The number of pairs $\{g,h\}$ with $h = ag$ such that the edge $e$ appear in the path $\Gamma_{gh}$ is exactly $N(s,a)$. Hence the congestion ratio simplifies to

$$ B = \max_{e \in E} \left( \frac{|G|}{P(e)} \sum_{\substack{g,h \\ \Gamma_{gh} \ni e}} \frac{\tilde{P}(g,h)}{|G|}|\Gamma_{gh}| \right) = \max_{s \in S} \frac{1}{\mu(s)} \sum_{a \in \tilde{S}} N(s,a)|a|\tilde{\mu}(a). $$

Applying Theorem 13.20 completes the proof. $\blacksquare$

*Remark* 13.25. The generalization to randomized paths goes through in the group case just as it does for general reversible chains (Corollary 13.23). We must now for each generator $a \in \tilde{S}$ specify a measure $\nu_a$ on the set $\mathcal{P}_a = \{(s_1, \ldots, s_k) : s_1 \cdots s_k = a\}$ of expansions of $a$ in terms of elements of $S$. If we let $|\Gamma|$ be the number of elements in an expansion $\Gamma = (s_1, \ldots, s_k)$ and $N(a, \Gamma)$ be the number of times $a$ appears in $\Gamma$, then the appropriate congestion ratio is

$$ B := \max_{s \in S} \frac{1}{\mu(s)} \sum_{a \in \tilde{S}} \tilde{\mu}(a) \sum_{\Gamma \in \mathcal{P}_a} \nu_a(\Gamma)N(s, \Gamma) \, |\Gamma|. \tag{13.21} $$

Exercise 13.4 asks you to fill in the details.

Using randomized paths can be useful, for example, when the generating set $S$ of the "new" walk is much larger than the generating set $\tilde{S}$ of the already-understood walk; in such a case averaging over paths can spread the bottlenecking over all generators, rather than just a few.

Corollary 13.24 is applied to a random walk on the symmetric group in Section 16.2.2.

**13.4.3. Diameter Bound.**

*Theorem* 13.26. *Let $G$ be a transitive graph with vertex degree $d$ and diameter* diam. *For the simple random walk on $G$,*

$$ \frac{1}{\gamma} \leq 2 \cdot d \cdot \operatorname{diam}^2. \tag{13.22} $$

*Proof.* Let $\nu_{xy}$ be the uniform distribution over shortest paths from $x$ to $y$. Comparing the chain to the chain with transition matrix $\tilde{P}(x,y) = \pi(y)$ (for all

### PDF page 208 (book page 192)

$x, y \in \mathcal{X}$), the congestion constant $B$ in Corollary 13.23 is

$$
\begin{aligned}
B &:= \max_{e \in E} \left( \frac{1}{Q(e)} \sum_{(x,y) \in \tilde{E}} \tilde{Q}(x,y) \sum_{\Gamma \in \mathcal{P}_{xy} \,:\, e \in \Gamma} \nu_{xy}(\Gamma)|\Gamma| \right) \\
&= \max_{e \in E} \left( \frac{1}{Q(e)} \sum_{x,y} \pi(x)\pi(y) \sum_{\Gamma \in \mathcal{P}_{xy} \,:\, e \in \Gamma} \nu_{xy}(\Gamma)|\Gamma| \right).
\end{aligned}
$$

Let $\mathcal{P}_{x,y}^{\min}$ be the set of paths of minimum length $\ell(x,y)$ connecting $x$ and $y$, and set $N(x,y) = |\mathcal{P}_{x,y}^{\min}|$. Since, in our case, $Q(e)^{-1} = nd$ and $\pi(x)\pi(y) = n^{-2}$, we have

$$ B = \frac{d}{n} \max_{e \in E} \sum_{x,y} \frac{1}{N(x,y)} \sum_{\Gamma \in \mathcal{P}_{xy}^{\min} \,:\, e \in \Gamma} \ell(x,y) \,. \tag{13.23} $$

We use the simple bound $\ell(x,y) \leq \operatorname{diam}$ to obtain

$$ B \leq \frac{d \cdot \operatorname{diam}}{n} \max_{e \in E} \sum_{x,y} \frac{|\Gamma : e \in \Gamma \in \mathcal{P}_{xy}^{\min}|}{N(x,y)} = \frac{d \cdot \operatorname{diam}}{n} \max_{e \in E} S_e \,, \tag{13.24} $$

where

$$ S_e := \sum_{(x,y) \in E} \frac{|\Gamma \,:\, e \in \Gamma \in \mathcal{P}_{xy}^{\min}|}{N(x,y)} = \sum_{x,y} \frac{1}{N(x,y)} \sum_{\Gamma \in \mathcal{P}_{x,y}^{\min}} \mathbf{1}_{\{\Gamma \ni e\}} \,. $$

Letting $S_z := \sum_{w \,:\, w \sim z} S_{zw}$, by the transitivity of $G$, the value of $S_z$ does not depend on $z$. For $e_0 = z_0 u$,

$$ S_{e_0} \leq S_{z_0} = \frac{1}{n} \sum_{z \in V} \tilde{S}_z = \frac{2}{n} \sum_{e \in E} S_e = \frac{2}{n} \sum_{e \in E} \sum_{x,y} \frac{1}{N(x,y)} \sum_{\Gamma \in \mathcal{P}_{xy}^{\min}} \mathbf{1}_{\{\Gamma \ni e\}} \,. $$

Changing the order of summation,

$$ S_{e_0} = \frac{2}{n} \sum_{x,y} N(x,y)^{-1} \sum_{\Gamma \in \mathcal{P}_{xy}^{\min}} \sum_{e \in E} \mathbf{1}_{\{e \in \Gamma\}} = \frac{2}{n} \sum_{x,y} N(x,y)^{-1} \sum_{\Gamma \in \mathcal{P}_{x,y}^{\min}} \ell(x,y) \,. \tag{13.25} $$

Since for each pair of states $x, y$, the bound $\ell(x,y) \leq \operatorname{diam}$ holds, and there are $n^2$ such pairs, it follows from (13.25) that

$$ S_e \leq \frac{2}{n} \cdot n^2 \cdot \operatorname{diam} = 2 \cdot n \cdot \operatorname{diam} \,. \tag{13.26} $$

Using (13.26) in (13.24), we have $B \leq 2d \cdot \operatorname{diam}^2$. $\blacksquare$

REMARK 13.27. For an edge-transitive graph, $S_{e_0} = \frac{1}{d} S_{z_0}$; thus this proof yields $\gamma^{-1} \leq 2 \cdot \operatorname{diam}^2$ in that case.

## **13.5. Wilson's Method for Lower Bounds**

A general method due to David Wilson (**2004a**) for obtaining a lower bound on mixing time uses an eigenfunction $\Phi$ to construct a distinguishing statistic.

### PDF page 209 (book page 193)

THEOREM 13.28 (Wilson's method). *Let $(X_t)$ be an irreducible aperiodic Markov chain with state space $\mathcal{X}$ and transition matrix $P$. Let $\Phi$ be an eigenfunction of $P$ with real eigenvalue $\lambda$ satisfying $1/2 < \lambda < 1$. Fix $0 < \varepsilon < 1$ and let $R > 0$ satisfy*

$$ \mathbf{E}_x \left( |\Phi(X_1) - \Phi(x)|^2 \right) \leq R \tag{13.27} $$

*for all $x \in \mathcal{X}$. Then for any $x \in \mathcal{X}$*

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{1}{2 \log(1/\lambda)} \left[ \log \left( \frac{(1-\lambda)\Phi(x)^2}{2R} \right) + \log \left( \frac{1-\varepsilon}{\varepsilon} \right) \right] . \tag{13.28} $$

At first glance, Theorem 13.28 appears daunting! Yet it gives sharp lower bounds in many important examples. Let's take a closer look and work through an example, before proceeding with the proof.

REMARK 13.29. In the proof given below, we use Proposition 7.12 instead of applying Chebyshev's Inequality as is done in **Wilson (2004a**, Lemma 5). We note that the $\varepsilon$-dependence (for $\varepsilon$ near 0) of the lower bound in **Wilson (2004a)** is not as sharp as is achieved in (13.28).

REMARK 13.30. In applications, $\varepsilon$ may not be tiny. For instance, when proving a family of chains has a cutoff, we will need to consider all values $0 < \varepsilon < 1$.

REMARK 13.31. Generally $\lambda$ will be taken to be the second largest eigenvalue in situations where $\gamma_\star = \gamma = 1 - \lambda$ is small. Under these circumstances a one-term Taylor expansion yields

$$ \frac{1}{\log(1/\lambda)} = \frac{1}{\gamma_\star + O(\gamma_\star)^2} = t_{\mathrm{rel}}(1 + O(\gamma_\star)). \tag{13.29} $$

According to Theorems 12.4 and 12.5,

$$ \log \left( \frac{1}{2\varepsilon} \right) (t_{\mathrm{rel}} - 1) \leq t_{\mathrm{mix}}(\varepsilon) \leq -\log(\varepsilon \pi_{\min}) t_{\mathrm{rel}}, $$

where $\pi_{\min} = \min_{x \in \mathcal{X}} \pi(x)$. One way to interpret (13.29) is that the denominator of (13.28) gets us up to the relaxation time (ignoring constants, for the moment). The numerator, which depends on the geometry of $\Phi$, determines how much larger a lower bound we can get.

EXAMPLE 13.32. Recall from Example 12.16 that the second-largest eigenvalue of the lazy random walk on the $n$-dimensional hypercube $\{0,1\}^n$ is $1 - \frac{1}{n}$. The corresponding eigenspace has dimension $n$, but a convenient representative to take is

$$ \Phi(\boldsymbol{x}) = W(\boldsymbol{x}) - \frac{n}{2}, $$

where $W(\boldsymbol{x})$ is the Hamming weight (i.e. the number of 1's) in the bitstring $\boldsymbol{x}$. For any bitstring $\boldsymbol{y}$, we have

$$ \mathbf{E}_{\boldsymbol{y}}((\Phi(X_1) - \Phi(\boldsymbol{y}))^2) = \frac{1}{2}(1) + \frac{1}{2}(0) = \frac{1}{2}, $$

since the value changes by exactly 1 whenever the walk actually moves. Now apply Theorem 13.28, taking the initial state to be the all-ones vector $\mathbf{1}$ and $R = 1/2$.

### PDF page 210 (book page 194)

We get

$$
\begin{aligned}
t_{\mathrm{mix}}(\varepsilon) &\geq \frac{1}{-2 \log(1 - n^{-1})} \left\{ \log \left[ n^{-1}(n/2)^2 \right] + \log \left[ (1-\varepsilon)/\varepsilon \right] \right\} \\
&= \frac{n}{2} \left[ 1 + O(n^{-1}) \right] \left[ \log n + \log[(1-\varepsilon)/\varepsilon] - \log 4 \right] \\
&= (1/2)n \log n + (1/2)n[1 + O(n^{-1})] \log[(1-\varepsilon)/\varepsilon] + O(n).
\end{aligned}
$$

Example 12.19 shows that the leading term $(1/2)n \log n$ is sharp. We obtained a similar lower bound in Proposition 7.14, using the Hamming weight directly as a distinguishing statistic. The major difference between the proof of Proposition 7.14 and the argument given here is that the previous proof used the structure of the hypercube walk to bound the variances. Wilson's method can be seen as a natural (in hindsight!) extension of that argument. What makes Theorem 13.28 widely applicable is that the hypothesis (13.27) is often easily checked and yields good bounds on the variance of the distinguishing statistic $\Phi(X_t)$.

PROOF OF THEOREM 13.28. Since

$$ \mathbf{E}(\Phi(X_{t+1})|X_t = z) = \lambda \Phi(z) \tag{13.30} $$

for all $t \geq 0$ and $z \in \mathcal{X}$, we have

$$ \mathbf{E}_x \Phi(X_t) = \lambda^t \Phi(x) \quad \text{for } t \geq 0 \tag{13.31} $$

by induction. Fix a value $t$, let $z = X_t$, and define $D_t = \Phi(X_{t+1}) - \Phi(z)$. By (13.30) and (13.27), respectively, we have

$$ \mathbf{E}_x(D_t \mid X_t = z) = (\lambda - 1)\Phi(z) $$

and

$$ \mathbf{E}_x(D_t^2 \mid X_t = z) \leq R. $$

Hence

$$
\begin{aligned}
\mathbf{E}_x(\Phi(X_{t+1})^2 \mid X_t = z) &= \mathbf{E}_x((\Phi(z) + D_t)^2 \mid X_t = z) \\
&= \Phi(z)^2 + 2\mathbf{E}_x(D_t \Phi(z) \mid X_t = z) + \mathbf{E}_x(D_t^2 \mid X_t = z) \\
&\leq (2\lambda - 1)\Phi(z)^2 + R.
\end{aligned}
$$

Averaging over the possible values of $z \in \mathcal{X}$ with weights $P^t(x,z) = \mathbf{P}_x\{X_t = z\}$ gives

$$ \mathbf{E}_x \Phi(X_{t+1})^2 \leq (2\lambda - 1)\mathbf{E}_x \Phi(X_t)^2 + R. $$

At this point, we could apply this estimate inductively, then sum the resulting geometric series. It is equivalent (and neater) to subtract $R/(2(1-\lambda))$ from both sides, obtaining

$$ \mathbf{E}_x \Phi(X_{t+1})^2 - \frac{R}{2(1-\lambda)} \leq (2\lambda - 1) \left( \mathbf{E}_x \Phi(X_t)^2 - \frac{R}{2(1-\lambda)} \right) . $$

Iterating the above inequality shows that

$$ \mathbf{E}_x \Phi(X_t)^2 - \frac{R}{2(1-\lambda)} \leq (2\lambda - 1)^t \left[ \Phi(x)^2 - \frac{R}{2(1-\lambda)} \right] . $$

### PDF page 211 (book page 195)

Leaving off the non-positive term $-(2\lambda - 1)^t R/[2(1-\lambda)]$ on the right-hand side above shows that

$$ \mathbf{E}_x \Phi(X_t)^2 \leq (2\lambda - 1)^t \Phi(x)^2 + \frac{R}{2(1-\lambda)}. \tag{13.32} $$

Combining (13.31) and (13.32) gives

$$ \operatorname{Var}_x \Phi(X_t) \leq \left[(2\lambda - 1)^t - \lambda^{2t}\right] \Phi(x)^2 + \frac{R}{2(1-\lambda)} < \frac{R}{2(1-\lambda)}, \tag{13.33} $$

since $2\lambda - 1 < \lambda^2$ ensures the first term is negative.

Lemma 12.3 implies that $E_\pi(\Phi) = 0$. Letting $t \to \infty$ in (13.33), the Convergence Theorem (Theorem 4.9) implies that

$$ \operatorname{Var}_\pi(\Phi) \leq \frac{R}{2(1-\lambda)} . $$

Applying Proposition 7.12 with $r^2 = \frac{2(1-\lambda)\lambda^{2t}\Phi(x)^2}{R}$ gives

$$ \left\|P^t(x, \cdot) - \pi\right\|_{\mathrm{TV}} \geq \frac{r^2}{4 + r^2} = \frac{(1-\lambda)\lambda^{2t}\Phi(x)^2}{2R + (1-\lambda)\lambda^{2t}\Phi(x)^2}. \tag{13.34} $$

If $t$ satisfies

$$ (1-\lambda)\lambda^{2t}\Phi(x)^2 > \frac{\varepsilon}{1-\varepsilon}(2R), \tag{13.35} $$

then the right-hand side of (13.34) is strictly greater than $\varepsilon$, whence, $d(t) > \varepsilon$. For any

$$ t < \frac{1}{2\log(1/\lambda)} \left[\log\left(\frac{(1-\lambda)\Phi(x)^2}{2R}\right) + \log\left(\frac{1-\varepsilon}{\varepsilon}\right)\right] , \tag{13.36} $$

the inequality (13.35) holds, so $t_{\mathrm{mix}}(\varepsilon) > t$. Thus $t_{\mathrm{mix}}(\varepsilon)$ is at least the right-hand side of (13.36). $\blacksquare$

REMARK 13.33. The variance estimate of (13.33) may look crude, but only $O(\lambda^{2t})$ is being discarded. In applications this is generally quite small.

EXAMPLE 13.34 (Product chains). Let $P$ be the transition matrix of a fixed Markov chain with state space $\mathcal{X}$, and let $Q_n$ be the transition matrix of the $n$-dimensional product chain on state space $\mathcal{X}^n$, as defined in Section 12.4. At each move, a coordinate is selected at random, and in the chosen coordinate, a transition is made using $P$. Using Wilson's method, we can derive a lower bound on the mixing time of this family in terms of the parameters of the original chain.

Let $\lambda = \max_{i \neq 1} \lambda_i$ be the largest non-trivial eigenvalue of $P$, and let $\gamma = 1 - \lambda$. Let $f : \mathcal{X} \to \mathbb{C}$ be an eigenfunction of $P$ with eigenvalue $\lambda$. By Lemma 12.12, for $1 \leq k \leq n$, the function $\Phi_k : \mathcal{X}^n \to \mathbb{C}$ defined by

$$ \Phi_k(y_1, \ldots, y_n) = f(y_k) $$

is an eigenfunction of $Q_n$ with eigenvalue

$$ \frac{n-1}{n}(1) + \frac{1}{n}(\lambda) = 1 - \frac{\gamma}{n}. $$

Hence $\Phi = \Phi_1 + \cdots + \Phi_n$ is also an eigenfunction with the same eigenvalue.

Let $Y_0, Y_1, Y_2, \ldots$ be a realization of the factor chain, and set

$$ R = \max_{y \in \mathcal{X}} \mathbf{E}_y |f(Y_1) - f(y)|^2. $$

### PDF page 212 (book page 196)

Since the product chain moves by choosing a coordinate uniformly and then using $P$ to update that coordinate, the same value of $R$ bounds the corresponding parameter for the product chain $Q_n$.

Set $m = \max_{y \in \mathcal{X}} |f(y)|$. Then applying Theorem 13.28 to the eigenfunction $\Phi$ of $Q_n$ tells us that for this product chain,

$$ \begin{aligned} t_{\mathrm{mix}}(\varepsilon) &\geq \frac{1}{-2\log\left(1 - \frac{\gamma}{n}\right)} \left\{ \log\left[\frac{(\gamma/n)n^2m^2}{2R}\right] + \log[(1-\varepsilon)/\varepsilon] \right\} \\ &= \frac{n\log n}{2\gamma} + O(n)\log[(1-\varepsilon)/\varepsilon]. \end{aligned} \tag{13.37} $$

**13.6. Expander Graphs\***

When a graph has a narrow bottleneck, the corresponding random walk must mix slowly. How efficiently can a family of graphs avoid bottlenecks? What properties does such an optimal family enjoy?

A family $\{G_n\}$ of graphs is defined to be a $(d, \alpha)$-**expander family** if the following three conditions hold for all $n$:

(i) $\lim_{n \to \infty} |V(G_n)| = \infty$.
(ii) $G_n$ is $d$-regular.
(iii) The bottleneck ratio of simple random walk on $G_n$ satisfies $\Phi_\star(G_n) \geq \alpha$.

PROPOSITION 13.35. *When $\{G_n\}$ is a $(d, \alpha)$-expander family, the lazy random walks on $\{G_n\}$ satisfy $t_{\mathrm{mix}}(G_n) = O(\log |V(G_n)|)$.*

PROOF. Theorem 13.10 implies that for all $G_n$ the spectral gap for the simple random walk satisfies $\gamma \geq \alpha^2/2$. Since each $G_n$ is regular, the stationary distribution of the lazy random walk is uniform, and Theorem 12.4 tells us that for the lazy walk $t_{\mathrm{mix}}(G_n) = O(\log |V(G_n)|)$. $\blacksquare$

REMARK 13.36. Given the diameter lower bound of Section 7.1.2, Proposition 13.35 says that expander families exhibit the fastest possible mixing (up to constant factors) for families of graphs of bounded degree.

It is not at all clear from the definition that families of expanders exist. Below we construct a family of 3-regular expander graphs. This is a version of the first construction of an expander family, due to **Pinsker (1973)**. Our initial construction allows multiple edges; we then describe modifications that yield 3-regular simple graphs.

Let $V(G_n) = \{a_1, \ldots, a_n, b_1, \ldots, b_n\}$. Choose permutations $\sigma_1, \sigma_2 \in \mathcal{S}_n$ uniformly at random and independent of each other, and set

$$ E(G_n) = \{(a_i, b_i), (a_i, b_{\sigma_1(i)}), (a_i, b_{\sigma_2(i)}) : 1 \leq i \leq n\}. \tag{13.38} $$

PROPOSITION 13.37. *For the family $\{G_n\}$ of random multigraphs described in (13.38),*

$$ \lim_{n \to \infty} \mathbf{P}\{\Phi_\star(G_n) > 0.01\} = 1. $$

PROOF. Assume that $\delta < 0.03$. We first show that *with probability tending to 1 as $n \to \infty$, every subset of $A$ of size $k \leq n/2$ has more than $(1 + \delta)k$ neighbors.* Note that every edge in $G_n$ connects a vertex in $A = \{a_1, \ldots, a_n\}$ to a vertex in $B = \{b_1, \ldots, b_n\}$ (that is, $G_n$ is bipartite).

### PDF page 213 (book page 197)

Let $S \subset A$ be a set of size $k \leq n/2$, and let $N(S)$ be the set of neighbors of $S$. We wish to bound the probability that $|N(S)| \leq (1 + \delta)k$. Since $(a_i, b_i)$ is an edge for any $1 \leq i \leq n$, we get immediately that $|N(S)| \geq k$. We can bound the probability that $N(S)$ is small by first enumerating the possibilities for the set of $\delta k$ "surplus" vertices allowed in $N(S)$, then requiring that $\sigma_1(S)$ and $\sigma_2(S)$ fall within the specified set. This argument gives

$$ \mathbf{P}\left\{|N(S)| \leq (1 + \delta)k\right\} \leq \frac{\binom{n}{\delta k}\binom{(1+\delta)k}{k}^2}{\binom{n}{k}^2}, $$

so

$$ \mathbf{P}\left\{\exists S : |S| \leq n/2 \text{ and } |N(S)| \leq (1 + \delta)k\right\} \leq \sum_{k=1}^{n/2} \binom{n}{k} \frac{\binom{n}{\delta k}\binom{(1+\delta)k}{\delta k}^2}{\binom{n}{k}^2}. $$

Exercise 13.5 asks you to show that this sum tends to 0 as $n \to \infty$, provided that $\delta < 0.03$.

We finish by checking that *if every subset of $A$ of size $k \leq n/2$ has more than $(1 + \delta)k$ neighbors, then $\Phi_\star > \delta/2$.* For $S \subset V$ with $|S| \leq n$, let

$$ A' = S \cap A \qquad \text{and} \qquad B' = S \cap B. $$

Without loss of generality we may assume $|A'| \geq |B'|$. If $|A'| \leq n/2$, then by hypothesis $A'$ has more than $(\delta/2)|S|$ neighbors in $B - B'$: all those edges connect elements of $S$ to elements of $S^c$. If $|A'| \geq n/2$, let $A'' \subseteq A'$ be an arbitrary subset of size $\lceil n/2 \rceil$. Since $|B'| \leq n/2$, the set $A''$ must have more than $(\delta/2)|S|$ neighbors in $B - B'$, and all the corresponding edges connect $S$ and $S^c$.

Taking $\delta = 0.02$ completes the proof. $\blacksquare$

COROLLARY 13.38. *There exists a family of $(3, 0.004)$-expanders.*

PROOF. We claim first that we can find a family of (deterministic) 3-regular multigraphs $\{G_n\}$ such that each has no triple edges, at most 3 double edges, and bottleneck ratio at least 0.01. Proposition 13.37 guarantees that asymptotically almost every random graph in the model of (13.38) has the bottleneck ratio at least 0.01. The expected number of triple edges is $1/n$ and the expected number of double edges is at most 3. By Markov's inequality, the probability of having 4 or more double edges is at most $3/4$. Thus the probability that $G_n$ has no triple edges, at most 3 double edges, and $\Phi_\star(G_n) \geq 0.01$ is at least $1/4 - o(1)$ as $n \to \infty$. We select one such graph for each sufficiently large $n$.

We still must repair the double edges. Subdivide each one with a vertex; then connect the two added vertices with an edge (as shown in Figure 13.2). Call the resulting graphs $\{\widetilde{G_n}\}$. The bottleneck ratio can be reduced in the worst case by a factor $5/2$. Thus $\Phi_\star \geq 0.004$ for the modified graph. $\blacksquare$

REMARK 13.39. In fact, as $n$ tends to $\infty$, the probability that $G_n$ is a simple graph tends to $1/e^3$—see **Riordan (1944)**. Verifying this fact (which we will not do here) also suffices to demonstrate the existence of an expander family.

### PDF page 214 (book page 198)

*[Figure: two graph diagrams side by side. Left: two vertices connected by two curved arcs forming a lens shape, with a straight edge extending to the left of the left vertex and to the right of the right vertex. Right: a similar lens shape between a left and right vertex, but with a vertical edge added through the middle connecting a top vertex to a bottom vertex, and horizontal edges extending outward from the left and right vertices.]*

FIGURE 13.2. Modifying a 3-regular multigraph to get a 3-regular graph.

**Exercises**

EXERCISE 13.1. Let $Y$ be a non-negative random variable. Show that

$$ \mathbf{E}(Y) = \int_0^\infty \mathbf{P}\{Y > t\} dt. $$

*Hint*: Write $Y = \int_0^\infty \mathbf{1}_{\{Y > t\}} dt$.

EXERCISE 13.2. Show that for lazy simple random walk on the box $\{1, \ldots, n\}^d$, the parameter $\gamma_\star$ satisfies $\gamma_\star^{-1} = O(n^2)$.

EXERCISE 13.3. Prove Corollary 13.23. *Hint*: follow the outline of the proof of Theorem 13.20.

EXERCISE 13.4. Prove that the statement of Corollary 13.24 remains true in the situation outlined in Remark 13.25.

EXERCISE 13.5. To complete the proof of Proposition 13.37, prove that for $\delta < 0.03$

$$ \lim_{n \to \infty} \sum_{k=1}^{n/2} \frac{\binom{n}{\delta k}\binom{(1+\delta)k}{\delta k}^2}{\binom{n}{k}} = 0. $$

EXERCISE 13.6. Extend the definition of $\mathcal{E}(f)$ and $\mathrm{Var}(f)$ to $f : \mathcal{X} \to \mathbb{R}^d$ by

$$ \mathcal{E}(f) = \frac{1}{2} \sum_{x,y} \pi(x) P(x,y) \|f(x) - f(y)\|^2, $$

$$ \mathrm{Var}_\pi(f) = \frac{1}{2} \sum_{x,y} \pi(x) \pi(y) \|f(x) - f(y)\|^2 . $$

Show that

$$ \gamma = \min\Big\{ \frac{\mathcal{E}(f)}{\mathrm{Var}_\pi(f)} \, : \, f \text{ nonconstant}, \, f : \mathcal{X} \to \mathbb{R}^d \Big\} $$

EXERCISE 13.7. Let $G \subset \mathbb{Z}^d$ be a connected finite subgraph of $\mathbb{Z}^d$ with vertex set $V$, and consider the lazy simple random walk on $G$. Define the average squared distance by

$$ \hat{D}^2 := \sum_{v,w \in V} \pi(v)\pi(w)\|v - w\|^2 . $$

Show that $t_{\mathrm{rel}} \geq 2\hat{D}^2$.

*Note:* The following exercise shows that $\hat{D}$ cannot be replaced by diam.

EXERCISE 13.8. Consider lazy simple random walk on graph consisting of adjacent rectangles of width $k = 2^h$ and with heights which double until reaching $k$, as shown for $h = 2$ below:

### PDF page 215 (book page 199)

*[Figure: a staircase-like arrangement of unit-square grids increasing in height from left to right. The left group is labeled $k = 2^h$ below it, and the tall right group is labeled $k = 2^h$ below it.]*

Show that $t_{\mathrm{rel}}$ is of order $k^2$ and $t_{\mathrm{mix}}$ is of order $k \cdot h$.
*Hint:* Use Corollary 13.21 for an upper bound on $t_{\mathrm{rel}}$.

EXERCISE 13.9. Consider a network along with alternative conductances $\tilde{c}(e)$ such that $1 \leq \frac{c(e)}{\tilde{c}(e)} \leq b$. Show that $b^{-2}\gamma \leq \tilde{\gamma} \leq b^2\gamma$.

EXERCISE 13.10. Suppose that $\mathcal{X} \subset \mathbb{Z}^2$ is such that for any $x, y \in \mathcal{X}$, there is a lattice path inside $\mathcal{X}$ connecting $x$ and $y$ with distance at most 5 from the line segment in the plane connecting $x$ to $y$. Show that $\gamma \geq \frac{c}{\mathrm{diam}(\mathcal{X})^2}$ for simple random walk on $\mathcal{X}$.

EXERCISE 13.11. Let $\mathcal{X}$ be a subset of the $n \times n$ square in $\mathbb{Z}^2$ obtained by removing a subset of the vertices with both coordinates even, and consider simple random walk on $\mathcal{X}$. Show that $\gamma \geq cn^{-2}$.

*Hint:* Combine Theorem 13.20 with Theorem 13.16.

EXERCISE 13.12. Let $X_1, \ldots, X_d$ be independent random variables taking values in a finite set $S$, and let $\pi_i$ be the probability distribution of $X_i$. Consider the chain on $S^d$ which, at each move, picks a coordinate $i$ at random, and updates the value at $i$ with an element of $S$ chosen according to $\pi_i$.

(a) Show that for this chain, $\gamma = 1/n$.
(b) Deduce the Efron-Stein inequality: For $\boldsymbol{X} = (X_1, \ldots, X_d)$, and $\boldsymbol{X}'$ independent and with the same distribution as $\boldsymbol{X}$, let $\hat{\boldsymbol{X}}_i := (X_1, \ldots, X_{i-1}, X_i', \ldots, X_d)$. Then

$$ \mathrm{Var}(f(\boldsymbol{X})) \leq \frac{1}{2} \sum_{i=1}^n \mathbf{E}\left[ (f(\boldsymbol{X}) - f(\hat{\boldsymbol{X}}_i))^2 \right] . $$

**Notes**

The connection between the spectral gap of the Laplace-Beltrami operator on Riemannian manifolds and an isoperimetric constant is due to Cheeger (1970); hence the bottleneck ratio is often called the ***Cheeger constant***. The Cheeger-type inequalities in (13.6) were proved for random walks on graphs by Alon and Milman (1985) and Alon (1986). These bounds were extended to reversible Markov chains by Sinclair and Jerrum (1989) and Lawler and Sokal (1988).

The Method of Canonical Paths (Corollary 13.21) for bounding relaxation time was introduced in Jerrum and Sinclair (1989) and further developed in Diaconis and Stroock (1991).

The bottleneck ratio is also sometimes called ***conductance***, especially in the computer science literature. We avoid this term, because it clashes with our use of "conductance" for electrical networks in Chapter 9.

Theorem 13.16 was first proved by Aldous (1999).

The Comparison Theorem is an extension of the method of canonical paths. A special case appeared in Quastel (1992); the form we give here is from Diaconis and Saloff-Coste (1993a) and Diaconis and Saloff-Coste (1993b). See also Madras and Randall (1996), Randall and Tetali (2000), and Dyer, Goldberg, Jerrum, and Martin (2006). Considering random paths, rather than a

### PDF page 216 (book page 200)

"canonical" path between each pair of states, is sometimes called the method of ***multicommodity flows***. We avoid this term because it clashes (partially) with our use of "flow" in Chapter 9. Here a probability measure on paths for $x$ to $y$ clearly determines a unit flow from $x$ to $y$; however, a flow by itself does not contain enough information to determine the congestion ratio of (13.16).

Wilson's method first appeared in Wilson (2004a). Wilson (2003) extended his lower bound to complex eigenvalues. See Mossel, Peres, and Sinclair (2004) for another variant.

The construction of Proposition 13.37 is due to Pinsker (1973). Bollobás (1988) proved that most $d$-regular graphs are expanders. Expander graphs are used extensively in computer science and communications networks. See Sarnak (2004) for a brief exposition and Hoory, Linial, and Wigderson (2006) or Lubotzky (1994) for a full discussion, including many deterministic constructions.

For more on the Efron-Stein inequality, see, for example, Chapter 3 of Boucheron, Lugosi, and Massart (2013).

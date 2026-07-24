# Chapter 24 — Cesàro Mixing Time, Stationary Times, and Hitting Large Sets
*(PDF pages 351–363; book pages 335–347)*

### PDF page 351 (book page 335)

CHAPTER 24

# Chapter 24 — Cesàro Mixing Time, Stationary Times, and Hitting Large Sets

**24.1. Introduction**

We discuss in this chapter (which follows closely the exposition in **Peres and Sousi (2015a)**) several parameters related to the mixing behavior of chains. These parameters are the *Cesàro mixing time* $t_{\mathrm{Ces}}$ (already discussed in Section 6.6), the *geometric mixing time* $t_{\mathrm{G}}$, the *large-set hitting time* $t_H(\alpha)$, and the *minimum expectation of a stationary time* $t_{\mathrm{stop}}$. The first three are *equivalent* for all chains, while the last is equivalent to the others for reversible chains. For lazy reversible chains,
$$ t_{\mathrm{mix}} \asymp t_{\mathrm{stop}} \asymp t_{\mathrm{G}} \asymp t_H(1/2) \asymp t_{\mathrm{Ces}} \,. $$
We will prove all these inequalities in this chapter, except for $t_{\mathrm{mix}} \lesssim t_{\mathrm{stop}}$.

DEFINITION 24.1. We say that two mixing parameters $s$ and $r$ are ***equivalent*** for a class of Markov chains $\mathcal{M}$ and write $s \asymp r$, if there exist universal positive constants $c$ and $c'$ so that $cs \leq r \leq c's$ for every chain in $\mathcal{M}$. We also write $s \lesssim r$ or $r \gtrsim s$ if there exists a universal positive constants $c$ such that $s \leq cr$.

A natural approach to approximating the stationary distribution of a chain is to average the first $t$ steps. Let $(X_t)$ be a Markov chain with stationary distribution $\pi$. The ***Cesàro mixing time***, introduced by **Lovász and Winkler (1998)** and already encountered in Section 6.6, captures the distance to stationarity of the arithmetic average of the laws of $X_1, X_2, \ldots, X_t$. Let $U_t$ be a random variable, uniform on $\{1, 2 \ldots, t\}$ and independent of the Markov chain $(X_t)$. We have $t^{-1} \sum_{s=1}^{t} P^s(x, \cdot) = \mathbf{P}\{X_{U_t} = \cdot\}$, and recall the definition
$$ t_{\mathrm{Ces}} := \min\left\{ t \geq 0 \,:\, \max_x \|\mathbf{P}_x\{X_{U_t} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \frac{1}{4} \right\} . $$

It turns out to be convenient, instead of taking an arithmetic average law of the first $t$ steps, to take the geometric average (with mean $t$) of the laws of the chain. This motivates the *geometric mixing time*, which we now introduce.

For each $t$, let $Z_t$ be a geometric random variable taking values in $\{1, 2, \ldots\}$ of mean $t$ and thus success probability $t^{-1}$, independent of the Markov chain $(X_t)_{t \geq 0}$. Letting
$$ d_G(t) := \max_x \|\mathbf{P}_x\{X_{Z_t} = \cdot\} - \pi\|_{\mathrm{TV}} \,, $$
the ***geometric mixing time*** is defined as
$$ t_{\mathrm{G}} = t_{\mathrm{G}}(1/4) = \min\{t \geq 1 \,:\, d_G(t) \leq 1/4\}. $$

Exercise 24.2 shows that $d_G(t)$ is monotone decreasing.

### PDF page 352 (book page 336)

The third parameter we consider in this chapter is the ***minimum expectation of a stationary time***, first introduced by Aldous (**1982**) in the continuous time case and later studied in discrete time by Lovász and Winkler (**1995b**, **1998**). It is defined as
$$ t_{\mathrm{stop}} = \max_{x \in \mathcal{X}} \inf\{\mathbf{E}_x(\tau^x) \,:\, \tau^x \text{ is a stopping time with } \mathbf{P}_x\{X_{\tau^x} = \cdot\} = \pi\}. \tag{24.1} $$
Note that the set of stopping times over which the infimum is taken includes stopping times with respect to filtrations larger than the natural filtration.

EXAMPLE 24.2 (Biased Random Walk on Cycle). In Section 5.3.2, we proved that for biased random walk on the $n$-cycle, $t_{\mathrm{mix}} \asymp n^2$.

However, we will now show that $t_{\mathrm{stop}} = O(n)$. Generate a point according to the distribution $\pi$ and independently of the chain, and let $\tau$ be the first time the walk hits this random point. From (10.26), we know that for biased random walk on all of $\mathbb{Z}$, the hitting time from 0 to $k$ equals $\mathbf{E}_0 \tau_k = k/(p - q)$. This is an upper bound on the hitting time $\mathbf{E}_0 \tau_k$ on the $n$-cycle. Consequently, $t_{\mathrm{hit}} \leq n(p - q)^{-1}$. Since $\mathbf{E}_x \tau \leq t_{\mathrm{hit}}$, it follows that $t_{\mathrm{stop}} \leq n/(p - q)$.

Theorem 6.19 and Proposition 24.4 imply that $t_{\mathrm{Ces}} = O(n)$ and $t_{\mathrm{G}} = O(n)$. Finally, applying Remark 7.2 and Exercise 24.4, we conclude that $t_{\mathrm{Ces}} \asymp t_{\mathrm{G}} \asymp t_{\mathrm{stop}} \asymp n$.

Thus, averaging over the first $t$ steps may approximate $\pi$ faster than using the state of the chain at time $t$.

The last parameter considered in this chapter is the maximum hitting time of "big" sets. For $\alpha \in (0, 1)$, set
$$ t_H(\alpha) := \max_{x, A \,:\, \pi(A) \geq \alpha} \mathbf{E}_x(\tau_A) \,, $$
where $\tau_A$ is the first time the chain hits the set $A \subset \mathcal{X}$. The next example illustrates that for $\alpha > 1/2 \geq \alpha'$, the parameter $t_H(\alpha)$ may be of smaller order than $t_H(\alpha')$:

EXAMPLE 24.3. Consider simple random walk on two copies of $K_n$, the complete graph on $n > 2$ vertices, say $K_n$ and $K'_n$, joined by a single edge. See Figure 24.1.

**FIGURE 24.1.** Two copies of $K_{10}$ joined by a single edge. *[Figure: two clusters of densely-interconnected vertices (two copies of the complete graph $K_{10}$) joined by a single edge connecting them.]*

The mixing time satisfies $t_{\mathrm{mix}} = O(n^2)$. (See Exercise 24.5.) If $\alpha > 1/2$, then $t_H(\alpha) \leq n$, but otherwise $t_H(\alpha) \asymp n^2$. (In the first case, each copy of $K_n$ must intersect a set $A$ with $\pi(A) > 1/2$, whence the expected time to hit $A$ is at most $n$. In the case $\alpha \leq 1/2$, there is a set $A$ with $\pi(A) \geq \alpha$ contained entirely on one side. The time to hit such a set from the opposite side is of order $n^2$.)

While the above example shows that $t_H(\alpha)$ and $t_H(\alpha')$ need not be equivalent if $\alpha' > 1/2 \geq \alpha$, Theorem 24.21 shows that $t_H(\alpha)$ are equivalent for all $\alpha \leq 1/2$.

### PDF page 353 (book page 337)

**24.2. Equivalence of $t_{\mathrm{stop}}, t_{\mathrm{Ces}}$ and $t_{\mathrm{G}}$ for reversible chains**

PROPOSITION 24.4. *For all chains we have that*
$$ t_{\mathrm{G}} \leq 4t_{\mathrm{stop}} + 1 \,. \tag{24.2} $$

REMARK 24.5. The analogous statement for $t_{\mathrm{Ces}}$ was already proven in Theorem 6.19.

The proof of this proposition requires the following:

LEMMA 24.6. *Let $Z$ be a discrete random variable with values in $\mathbb{N}$ and satisfying $\mathbf{P}\{Z = j\} \leq c$ for all $j > 0$ for a positive constant $c$, and such that $\mathbf{P}\{Z = j\}$ is decreasing in $j$. Let $\tau$ be an independent random variable with values in $\mathbb{N}$. We have that*
$$ \|\mathbf{P}\{Z + \tau = \cdot\} - \mathbf{P}\{Z = \cdot\}\|_{\mathrm{TV}} \leq c\mathbf{E}(\tau). \tag{24.3} $$

PROOF. Using the definition of total variation distance and the assumption on $Z$ we have for all $k \in \mathbb{N}$
$$ \|\mathbf{P}\{Z + k = \cdot\} - \mathbf{P}\{Z = \cdot\}\|_{\mathrm{TV}} $$
$$ = \sum_{\substack{j \\ \mathbf{P}\{Z=j\} \geq \mathbf{P}\{Z+k=j\}}} (\mathbf{P}\{Z = j\} - \mathbf{P}\{Z + k = j\}) \leq kc. $$
Since $\tau$ is independent of $Z$, we obtain (24.3). $\blacksquare$

PROOF OF PROPOSITION 24.4. We fix $x$. Let $\tau$ be a stationary time, so that the distribution of $X_\tau$ when started from $x$ is $\pi$. Then $\tau + s$ is also a stationary time for all $s \geq 1$. Hence, if $Z_t$ is a geometric random variable independent of $\tau$, then $Z_t + \tau$ is also a stationary time, i.e. $\mathbf{P}_x\{X_{Z_t + \tau} = \cdot\} = \pi$. Since $Z_t$ and $\tau$ are independent, Lemma 24.6 implies
$$ \|\mathbf{P}_x\{Z_t + \tau = \cdot\} - \mathbf{P}_x\{Z_t = \cdot\}\|_{\mathrm{TV}} \leq \frac{\mathbf{E}_x(\tau)}{t}. \tag{24.4} $$
From Exercise 24.3, we obtain
$$ \|\mathbf{P}_x\{X_{Z_t + \tau} = \cdot\} - \mathbf{P}_x\{X_{Z_t} = \cdot\}\|_{\mathrm{TV}} \leq \|\mathbf{P}_x\{Z_t + \tau = \cdot\} - \mathbf{P}_x\{Z_t = \cdot\}\|_{\mathrm{TV}} $$
$$ \leq \frac{\mathbf{E}_x(\tau)}{t}, $$
and since $\mathbf{P}_x\{X_{Z_t + \tau} = \cdot\} = \pi$, taking $t \geq 4\mathbf{E}_x(\tau)$ concludes the proof. $\blacksquare$

An inequality in the other direction from that in Proposition 24.4 is true for reversible chains; see Proposition 24.8. First, we prove:

LEMMA 24.7. *For a reversible chain,*
$$ t_{\mathrm{stop}} \leq 8t_{\mathrm{mix}} \,. \tag{24.5} $$

PROOF. From the proof of Lemma 6.17,
$$ \frac{P^{2t}(x, y)}{\pi(y)} \geq (1 - \bar{d}(t))^2 \,. $$
It follows that, for all $x, y$,
$$ P^{2t_{\mathrm{mix}}}(x, y) \geq \frac{1}{4}\pi(y) \,. $$

### PDF page 354 (book page 338)

Hence, we can write

$$ P^{2t_{\mathrm{mix}}}(x,y) = \frac{1}{4}\pi(y) + \frac{3}{4}Q(x,y), $$

where $Q$ is another transition matrix.

Set $Y_s = X_{2t_{\mathrm{mix}}s}$, so that $(Y_s)$ is a Markov chain with transition matrix $P^{2t_{\mathrm{mix}}}$. Given that $Y_s = x$, we can obtain $Y_{s+1}$ by the following procedure: toss a coin $I_{s+1}$ which lands heads with probability $1/4$; if the coin lands heads, select $Y_{s+1}$ according to $\pi$, and if tails, select according to $Q(x,\cdot)$.

Define $\sigma = \min\{s \geq 1 \,:\, I_s = \text{"heads"}\}$. The time $\sigma$ is a strong stationary time for the chain $(Y_s)$, with $\mathbf{E}_x(\sigma) = 4$. The time $\tau = 2t_{\mathrm{mix}}\sigma$ is a stopping time for $(X_t)$. Since $X_\tau = Y_\sigma$, the law of $X_\tau$ is $\pi$, and $\mathbf{E}_x(\tau) = 8t_{\mathrm{mix}}$. This establishes (24.5). $\blacksquare$

PROPOSITION 24.8. *For reversible chains,*

(i)
$$ t_{\mathrm{stop}} \leq 8t_{\mathrm{G}}\,. $$

(ii)
$$ t_{\mathrm{stop}} \leq 4(t_{\mathrm{Ces}} + 1)\,. $$

Lemma 24.7 and Proposition 24.8 fail for non-reversible chains, see Example 24.20.

PROOF. Consider the chain with transition matrix $R(x,y) = \mathbf{P}_x\{X_G = y\}$, where $G$ is geometric with mean $t$. Set $t = t_{\mathrm{G}}$ so that

$$ \|\mathbf{P}_x\{X_G = \cdot\} - \pi\|_{\mathrm{TV}} \leq \frac{1}{4}\,. $$

That is, if $t_{\mathrm{mix}}(R)$ is the mixing time of the chain with transition matrix $R$, then $t_{\mathrm{mix}}(R) = 1$. By Lemma 24.7, if $t_{\mathrm{stop}}(R)$ is the parameter $t_{\mathrm{stop}}$ for the chain with transition matrix $R$, then $t_{\mathrm{stop}}(R) \leq 8$.

Note that if $G_1, G_2, \ldots$ are i.i.d. geometric variables with mean $t$, then the process $(X_{G_1+\cdots+G_s})_{s\geq 0}$ is a Markov chain with transition matrix $R$.

Since $t_{\mathrm{stop}}(R) \leq 8$, there exists a stationary time $\tau$ for $(X_{G_1+\cdots+G_s})$ satisfying $\mathbf{E}(\tau) \leq 8$. Note that $G_1 + \cdots + G_\tau$ is a stationary time for $(X_t)$, and by Wald's identity (Exercise 6.7),

$$ \mathbf{E}(G_1 + \cdots + G_\tau) = \mathbf{E}(\tau)\mathbf{E}(G_1) \leq 8t\,. $$

We conclude that $t_{\mathrm{stop}} \leq 8t_{\mathrm{G}}$.

The argument for $t_{\mathrm{Ces}}$ is similar. $\blacksquare$

REMARK 24.9. We do not use any specific properties of the geometric distribution in the proof of Proposition 24.8, and any (positive, integer valued) random variable with expectation at most $t$ can be substituted.

The following is immediate from Theorem 6.19, Proposition 24.4 and Proposition 24.8:

PROPOSITION 24.10. *For reversible chains, $t_{\mathrm{G}} \asymp t_{\mathrm{Ces}}$.*

REMARK 24.11. In fact, $t_{\mathrm{G}} \asymp t_{\mathrm{Ces}}$ for all chains (not necessarily reversible). See Exercise 24.4.

### PDF page 355 (book page 339)

**24.3. Halting States and Mean-Optimal Stopping Times**

DEFINITION 24.12. Let $\tau$ be a stopping time for a Markov chain $(X_t)$. A state $z$ is called a **halting** state for the stopping time $\tau$ and the initial distribution $\mu$ if $\mathbf{P}_\mu\{\tau \leq \tau_z\} = 1$, where $\tau_z$ is the first hitting time of state $z$.

We saw in Chapter 6 examples of stationary times with halting states. These were in fact all strong stationary times.

EXAMPLE 24.13. Given a chain $(X_t)$, let $Y$ be chosen according to the stationary distribution $\pi$, and let

$$ \tau = \min\{t \,:\, X_t = Y\}\,. $$

The stopping time $\tau$ is always a stationary time, but is not a strong stationary time provided there is more than one state.

If the chain is a birth-and-death chain on $\{0,1,2,\ldots,n\}$ and started from $0$, then $n$ is a halting state for $\tau$.

The importance of halting states stems from the following theorem:

THEOREM 24.14. *Let $\mu$ be any starting distribution and $\pi$ the stationary distribution for an irreducible Markov chain. Let $\tau$ be a stationary time for $\mu$, that is, a stopping time such that $\mathbf{P}_\mu\{X_\tau = x\} = \pi(x)$ for all $x$. If $\tau$ has a halting state, then it is mean optimal in the sense that*

$$ \mathbf{E}_\mu(\tau) = \min\{\mathbf{E}_\mu(\sigma) \,:\, \sigma \text{ is a stopping time s.t. } \mathbf{P}_\mu\{X_\sigma = \cdot\} = \pi\}\,. $$

PROOF. Consider the mean occupation times

$$ \psi(x) = \mathbf{E}_\mu\Big(\sum_{k=0}^{\tau-1} \mathbf{1}\{X_k = x\}\Big) $$

for all $x$.

By Lemma 10.5,

$$ \psi P = \psi - \mu + \pi\,. \tag{24.6} $$

Let $\sigma$ be another stopping time with $\mathbf{P}_\mu\{X_\sigma = \cdot\} = \pi$ and let $\varphi(x)$ be its corresponding mean occupation times. Then

$$ \varphi P = \varphi - \mu + \pi\,. $$

Therefore,

$$ (\varphi - \psi) = (\varphi - \psi)P\,. $$

Since the kernel of $P - I$ is one dimensional (see Lemma 1.16), $\varphi - \psi$ must be a multiple of the stationary distribution, i.e. for a constant $\alpha$ we have that $(\varphi - \psi) = \alpha\pi$.

Suppose that $\tau$ has a halting state, i.e. there exists a state $z$ such that $\psi(z) = 0$. Therefore we get that $\varphi(z) = \alpha\pi(z)$, and hence $\alpha \geq 0$. Thus $\varphi(x) \geq \psi(x)$ for all $x$ and

$$ \mathbf{E}_\mu(\sigma) = \sum_x \varphi(x) \geq \sum_x \psi(x) = \mathbf{E}_\mu(\tau), $$

proving mean-optimality of $\tau$. $\blacksquare$

### PDF page 356 (book page 340)

EXAMPLE 24.15. Let $(X_t)$ be a simple random walk on a triangle. The optimal stationary time $\tau$ is

$$ \tau = \begin{cases} 0 & \text{with probability } 1/3 \\ 1 & \text{with probability } 2/3\,. \end{cases} $$

Clearly, $\mathbf{E}(\tau) = 2/3$. But any strong stationary time cannot equal $0$ with positive probability. Thus there is no strong stationary time with a halting state; if so, then it would also be an optimal stationary time, and have mean $2/3$.

**24.4. Regularity Properties of Geometric Mixing Times**

Define

$$ \bar{d}_G(t) := \max_{x,y} \|\mathbf{P}_x\{X_{Z_t} = \cdot\} - \mathbf{P}_y\{X_{Z_t} = \cdot\}\|_{\mathrm{TV}}\,. $$

Applying Lemma 4.10 (with $t = 1$) to the chain with transition matrix $Q(x,y) = \mathbf{P}_x\{X_{Z_t} = y\}$ shows that

$$ d_G(t) \leq \bar{d}_G(t) \leq 2d_G(t)\,. \tag{24.7} $$

Recall that $\bar{d}(t)$ is submultiplicative as a function of $t$ (Lemma 4.11). In the following lemma and corollary, which will be used in the proof of Theorem 24.18, we show that $\bar{d}_G$ satisfies a form of submultiplicativity.

LEMMA 24.16. *Let $\beta < 1$ and let $t$ be such that $\bar{d}_G(t) \leq \beta$. Then for all $k \in \mathbb{N}$ we have that*

$$ \bar{d}_G(2^k t) \leq \left(\frac{1+\beta}{2}\right)^k \bar{d}_G(t). $$

PROOF. As in Exercise 24.2, we can write $Z_{2t} = (Z_{2t} - Z_t) + Z_t$, where $Z_{2t} - Z_t$ and $Z_t$ are independent. Hence it is easy to show (similar to the case for deterministic times) that

$$ \bar{d}_G(2t) \leq \bar{d}_G(t) \max_{x,y} \|\mathbf{P}_x\{X_{Z_{2t}-Z_t} = \cdot\} - \mathbf{P}_y\{X_{Z_{2t}-Z_t} = \cdot\}\|_{\mathrm{TV}}. \tag{24.8} $$

By the coupling of $Z_{2t}$ and $Z_t$ it is easy to see that $Z_{2t} - Z_t$ can be expressed as follows:

$$ Z_{2t} - Z_t = \xi G_{2t}, $$

where $\xi$ is a Bernoulli$(\frac{1}{2})$ random variable and $G_{2t}$ is a geometric random variable of mean $2t$ independent of $\xi$. By the triangle inequality we get that

$$ \|\mathbf{P}_x\{X_{Z_{2t}-Z_t} = \cdot\} - \mathbf{P}_y\{X_{Z_{2t}-Z_t} = \cdot\}\|_{\mathrm{TV}} $$
$$ \leq \frac{1}{2} + \frac{1}{2}\|\mathbf{P}_x\{X_{G_{2t}} = \cdot\} - \mathbf{P}_y\{X_{G_{2t}} = \cdot\}\|_{\mathrm{TV}} \leq \frac{1}{2} + \frac{1}{2}\bar{d}_G(2t), $$

and hence (24.8) becomes

$$ \bar{d}_G(2t) \leq \bar{d}_G(t)\left(\frac{1}{2} + \frac{1}{2}\bar{d}_G(2t)\right) \leq \frac{1}{2}\bar{d}_G(t)\left(1 + \bar{d}_G(t)\right), $$

where for the second inequality we used the monotonicity property of $\bar{d}_G$ (same proof as for $d_G(t)$). Thus, since $t$ satisfies $\bar{d}_G(t) \leq \beta$, we get that

$$ \bar{d}_G(2t) \leq \left(\frac{1+\beta}{2}\right)\bar{d}_G(t), $$

and hence iterating we deduce the desired inequality. $\blacksquare$

### PDF page 357 (book page 341)

Combining Lemma 24.16 with (24.7) we get the following:

COROLLARY 24.17. *Let $\beta < 1$. If $t$ is such that $d_G(t) \leq \beta/2$, then for all $k$,*

$$ d_G(2^k t) \leq 2 \left( \frac{1+\beta}{2} \right)^k d_G(t). $$

*Also if $d_G(t) \leq \alpha < 1/2$, then there exists a constant $c = c(\alpha)$ depending only on $\alpha$, such that $d_G(ct) \leq 1/4$.*

**24.5. Equivalence of $t_\mathrm{G}$ and $t_H$**

THEOREM 24.18. *Let $\alpha < 1/2$. For every chain, $t_\mathrm{G} \asymp t_H(\alpha)$. (The implied constants depend on $\alpha$.)*

Theorem 24.21 extends the equivalence to $\alpha \leq 1/2$.

PROOF. We will first show that $t_\mathrm{G} \geq c t_H(\alpha)$. Let $A$ satisfy $\pi(A) \geq \frac{1}{2}$. By Corollary 24.17 there exists $k = k(\alpha)$ so that $d_G(2^k t_\mathrm{G}) \leq \frac{\alpha}{2}$. Let $t = 2^k t_\mathrm{G}$. Then for any starting point $x$ we have that

$$ \mathbf{P}_x\{X_{Z_t} \in A\} \geq \pi(A) - \frac{\alpha}{2} \geq \frac{\alpha}{2} \,. $$

Thus by performing independent experiments, we deduce that $\tau_A$ is stochastically dominated by $\sum_{i=1}^{N} G_i$, where $N$ is a geometric random variable of success probability $\alpha/2$ and the $G_i$'s are independent geometric random variables of success probability $\frac{1}{t}$. Therefore for any starting point $x$ we get that (by Wald's Identity)

$$ \mathbf{E}_x(\tau_A) \leq \frac{2}{\alpha} t, $$

and hence this gives that

$$ \max_{x,A:\pi(A)\geq\alpha} \mathbf{E}_x(\tau_A) \leq \frac{2}{\alpha} 2^k t_\mathrm{G}. $$

In order to show the other direction, let $t' < t_\mathrm{G}$. Then $d_G(t') > 1/4$. For a given $\alpha < 1/2$, we fix $\gamma \in (\alpha, 1/2)$. By Corollary 24.17, there exists a positive constant $c = c(\gamma)$ such that

$$ d_G(ct') > \gamma. $$

Set $t = ct'$. Then there exists a set $A$ and a starting point $x$, which we fix, such that

$$ \pi(A) - \mathbf{P}_x\{X_{Z_t} \in A\} > \gamma, $$

and hence $\pi(A) > \gamma$, or equivalently

$$ \mathbf{P}_x\{X_{Z_t} \in A\} < \pi(A) - \gamma. $$

We now define a set $B$ as follows:

$$ B = \{y \,:\, \mathbf{P}_y\{X_{Z_t} \in A\} \geq \pi(A) - \alpha\} \,. $$

Since $\pi$ is a stationary distribution, we have that

$$ \pi(A) = \sum_{y \in B} \mathbf{P}_y\{X_{Z_t} \in A\}\pi(y) + \sum_{y \notin B} \mathbf{P}_y\{X_{Z_t} \in A\}\pi(y) \leq \pi(B) + \pi(A) - \alpha, $$

and hence rearranging, we get that

$$ \pi(B) \geq \alpha. $$

### PDF page 358 (book page 342)

Our goal is to show, for a constant $\theta$ to be determined later, that

$$ \max_z \mathbf{E}_z(\tau_B) > \theta t \tag{24.9} $$

Indeed, we now show that the assumption

$$ \max_z \mathbf{E}_z(\tau_B) \leq \theta t \tag{24.10} $$

will yield a contradiction. By Markov's inequality, (24.10) implies that

$$ \mathbf{P}_x\{\tau_B \geq 2\theta t\} \leq \frac{1}{2}. \tag{24.11} $$

For any positive integer $M$ we have that

$$ \mathbf{P}_x\{\tau_B \geq 2M\theta t\} = \mathbf{P}_x\{\tau_B \geq 2M\theta t \mid \tau_B \geq 2(M-1)\theta t\}\mathbf{P}_x\{\tau_B \geq 2(M-1)\theta t\}, $$

and hence iterating we get that

$$ \mathbf{P}_x\{\tau_B \geq 2M\theta t\} \leq \frac{1}{2^M}. \tag{24.12} $$

By the memoryless property of the geometric distribution and the strong Markov property applied at the stopping time $\tau_B$, we get that

$$
\begin{aligned}
\mathbf{P}_x\{X_{Z_t} \in A\} &\geq \mathbf{P}_x\{\tau_B \leq 2\theta Mt, \ Z_t \geq \tau_B, \ X_{Z_t} \in A\} \\
&= \mathbf{P}_x\{\tau_B \leq 2\theta Mt, \ Z_t \geq \tau_B\}\mathbf{P}_x\{X_{Z_t} \in A \mid \tau_B \leq 2\theta Mt, \ Z_t \geq \tau_B\} \\
&\geq \mathbf{P}_x\{\tau_B \leq 2\theta Mt\}\mathbf{P}_x\{Z_t \geq \lfloor 2\theta Mt \rfloor\} \left( \inf_{w \in B} \mathbf{P}_w\{X_{Z_t} \in A\} \right),
\end{aligned}
$$

where in the last inequality we used the independence between $Z$ and $\tau_B$. But since $Z_t$ is a geometric random variable, we obtain that

$$ \mathbf{P}_x\{Z_t \geq \lfloor 2\theta Mt \rfloor\} \geq \left( 1 - \frac{1}{t} \right)^{2\theta Mt} . $$

Using the inequality $(1 - u)^p - (1 - up) \geq 0$ for $u \in [0, 1)$ and $p \geq 1$ (the left-hand side is an increasing function of $u$ which vanishes at $u = 0$), shows that for $2\theta Mt > 1$ we have

$$ \mathbf{P}_x\{Z_t \geq \lfloor 2\theta Mt \rfloor\} \geq 1 - 2\theta M. \tag{24.13} $$

(The bound (24.10) implies that $\theta t \geq 1$, so certainly $2\theta Mt > 1$.)

We now set $\theta = \frac{1}{2M 2^M}$. Using (24.12) and (24.13) we deduce that

$$ \mathbf{P}_x\{X_{Z_t} \in A\} \geq \left( 1 - 2^{-M} \right)^2 (\pi(A) - \alpha). $$

Since $\gamma > \alpha$, we can take $M$ large enough so that $\left( 1 - 2^{-M} \right)^2 (\pi(A) - \alpha) > \pi(A) - \gamma$, and we get a contradiction to (24.10).

Thus (24.9) holds; since $\pi(B) \geq \alpha$, this completes the proof. $\blacksquare$

**24.6. Upward Skip-Free Chains**

A chain on a subset of $\mathbb{Z}$ is *upward skip-free* if $P(i, j) = 0$ if $j > i+1$. Examples include birth-and-death chains (Section 2.5), as well as the greasy ladder (discussed below in Example 24.20).

For $Z$ a random variable with distribution $\pi$ and independent of the chain, define

$$ \tau_\pi = \sum_{z \in \mathcal{X}} \tau_z \mathbf{1}_{\{Z=z\}} \,. $$

### PDF page 359 (book page 343)

Recall the definition (10.2) of the target time $t_\odot = \mathbf{E}_a(\tau_\pi)$, and Lemma 10.1, which says that $t_\odot$ does not depend on the starting state $a$.

LEMMA 24.19. *For an upward skip-free chain on $\{1, \ldots, n\}$, the stopping time $\tau_\pi$ is a mean-optimal stationary time from state $1$, and $t_{\mathrm{stop}} = \mathbf{E}_1(\tau_\pi) = t_\odot$.*

PROOF. Starting from $1$, the state $n$ is a halting state for the stopping time $\tau_\pi$. Thus, by Theorem 24.14, $\tau_\pi$ is mean optimal:

$$ \mathbf{E}_1(\tau_\pi) = \min\{\mathbf{E}_1(\sigma) \,:\, \sigma \text{ is a stopping time with } \mathbf{P}_1\{X_\sigma \in \cdot\} = \pi\}. $$

By the random target lemma (Lemma 10.1), $\mathbf{E}_i(\tau_\pi) = \mathbf{E}_1(\tau_\pi)$, for all $i \leq n$. Since for all $i$ we have that

$$ \mathbf{E}_1(\tau_\pi) = \mathbf{E}_i(\tau_\pi) \geq \min\{\mathbf{E}_i(\sigma) \,:\, \sigma \text{ is a stopping time with } \mathbf{P}_i\{X_\sigma \in \cdot\} = \pi\}, $$

it follows that $t_{\mathrm{stop}} \leq \mathbf{E}_1(\tau_\pi)$. But also $\mathbf{E}_1(\tau_\pi) \leq t_{\mathrm{stop}}$, and hence $t_{\mathrm{stop}} = \mathbf{E}_1(\tau_\pi)$. $\blacksquare$

EXAMPLE 24.20 (The greasy ladder). Let $\mathcal{X} = \{1, \ldots, n\}$ and $P(i, i+1) = \frac{1}{2} = 1 - P(i, 1)$ for $i = 1, \ldots, n-1$ and $P(n, 1) = 1$. Then it is easy to check that

$$ \pi(i) = \frac{2^{-i}}{1 - 2^{-n}} $$

is the stationary distribution. Here, $t_{\mathrm{mix}}$ is of order $1$. (See Exercise 24.6.)

Since the chain is upward skip-free, we can use the previous lemma. By straightforward calculations, we get that $\mathbf{E}_1(\tau_i) = 2^i - 2$, for all $i \geq 2$, and hence

$$ t_{\mathrm{stop}} = \mathbf{E}_1(\tau_\pi) = \sum_{i=2}^{n} (2^i - 2)\frac{2^{-i}}{1 - 2^{-n}} = \frac{n}{1 - 2^{-n}} - 2 \,. $$

This example shows that for a non-reversible chain $t_{\mathrm{stop}}$ can be much bigger than $t_{\mathrm{mix}}$; also, see Exercise 6.11, which shows that $t_{\mathrm{Ces}} = O(t_{\mathrm{mix}})$.

**24.7. $t_H(\alpha)$ are comparable for $\alpha \leq 1/2$.**

THEOREM 24.21. *Let $0 < \alpha < \beta$. For any irreducible finite Markov chain,*

$$ t_H(\alpha) \leq t_H(\beta) + \left( \frac{1}{\alpha} - 1 \right) t_H(1 - \beta) \,. \tag{24.14} $$

*If $\alpha \leq \frac{1}{2}$, then*

$$ t_H(\alpha) \leq \frac{t_H(\frac{1}{2})}{\alpha} \,. \tag{24.15} $$

Before we prove this, we need the following proposition. Define, for $H, K \subset \mathcal{X}$,

$$
\begin{aligned}
d^+(H, K) &= \max_{x \in H} \mathbf{E}_x(\tau_K) \\
d^-(H, K) &= \min_{x \in H} \mathbf{E}_x(\tau_K) \,.
\end{aligned}
$$

PROPOSITION 24.22. *Given an irreducible Markov chain $(X_t)$ with finite state space $\mathcal{X}$ and stationary distribution $\pi$, let $A, C \subseteq \mathcal{X}$ with $A \cap C = \varnothing$. Then*

$$ \pi(A) \leq \frac{d^+(A, C)}{d^+(A, C) + d^-(C, A)} \,. $$

### PDF page 360 (book page 344)

*Proof.* Define
$$ \tau = \min\{t > \tau_C \,:\, X_t \in A\} \,. $$
Consider a Markov chain on $A$ defined as follows: for each $x, y \in A$, let $Q(x, y) = \mathbf{P}_x\{X_\tau = y\}$. Let $\mu$ denote a stationary distribution of this new chain, and let $\nu$ be the hitting distribution on $C$ when the original chain is started from $\mu$, i.e. $\nu(y) = \mathbf{P}_\mu\{X_{\tau_C} = y\}$ for each $y \in C$.

Started from the distribution $\mu$, the expected time the chain $(X_t)$ spends in $A$ before it reaches $C$ and returns to $A$ is given by $\mathbf{E}_\mu(\tau)\pi(A)$. (This follows from Lemma 10.5.)

Next, since all visits to $A$ occur before the chain reaches $C$, we have that $\mathbf{E}_\mu(\tau)\pi(A) \leq \mathbf{E}_\mu(\tau_C)$. Since $\mathbf{E}_\mu(\tau) = \mathbf{E}_\mu(\tau_C) + \mathbf{E}_\nu(\tau_A)$, we conclude that
$$ \pi(A) \leq \frac{\mathbf{E}_\mu(\tau_C)}{\mathbf{E}_\mu(\tau_C) + \mathbf{E}_\nu(\tau_A)} \leq \frac{d^+(A, C)}{d^+(A, C) + d^-(C, A)} \,, $$
as required. $\blacksquare$

*Proof of Theorem 24.21.* Fix $x \in \mathcal{X}$ and $A \subset \mathcal{X}$ with $\pi(A) \geq \alpha$. We want to prove that
$$ \mathbf{E}_x(\tau_A) \leq t_H(\beta) + \left(\frac{1}{\alpha} - 1\right) t_H(1 - \beta) \,. $$
Since $x$ and $A$ are arbitrary, this will suffice to prove the theorem. Define the set $C = C_A^\beta$ as follows:
$$ C := \left\{ y \in \mathcal{X} \,:\, \mathbf{E}_y(\tau_A) > \left(\frac{1}{\alpha} - 1\right) t_H(1 - \beta) \right\} \,. $$
We claim that $\pi(C) < 1 - \beta$. Indeed, if $\pi(C) \geq 1 - \beta$, then $d^+(A, C) \leq t_H(1 - \beta)$ while $d^-(C, A) > (\alpha^{-1} - 1)t_H(1 - \beta)$. This would imply, by Proposition 24.22, that $\pi(A) < \alpha$, a contradiction. Thus, letting $B := \mathcal{X} \setminus C$, we have established that $\pi(B) > \beta$. By the Markov property of the chain,
$$ \mathbf{E}_x(\tau_A) \leq \mathbf{E}_x(\tau_B) + d^+(B, A) \,. $$
Combining the bound $\mathbf{E}_x(\tau_B) \leq t_H(\beta)$ (since $\pi(B) \geq \beta$) with the bound $d^+(B, A) \leq (\alpha^{-1} - 1) \cdot t_H(1 - \beta)$ (since $B$ is the complement of $C$), we obtain
$$ \mathbf{E}_x(\tau_A) \leq t_H(\beta) + \left(\frac{1}{\alpha} - 1\right) t_H(1 - \beta) $$
as required. $\blacksquare$

**24.8. An Upper Bound on $t_{\mathrm{rel}}$**

**Proposition 24.23.** *If $P$ is an irreducible transition matrix, then for any positive eigenvalue $\lambda > 0$,*
$$ 1 - \lambda \geq \frac{1}{t_{\mathrm{G}} + 1} \,. $$
*In particular, for reversible lazy chains,*
$$ t_{\mathrm{rel}} \leq t_{\mathrm{G}} + 1 \,. $$

### PDF page 361 (book page 345)

*Proof.* Let $K(x, y) = \mathbf{P}_x\{X_Z = y\}$, where $Z$ is geometric with mean $t = t_{\mathrm{G}}$. Any eigenvalue $\lambda$ of $P$ gives the eigenvalue for the $K$-chain
$$ \tilde{\lambda} = \sum_{k=1}^{\infty} \lambda^k (1 - 1/t)^{k-1}(1/t) = \frac{\lambda}{t - \lambda t + \lambda} \,. $$
Note that from the definition of $t_{\mathrm{G}}$, for the $K$-chain, $d(1) \leq 1/4$. Applying (12.15) for the $K$-chain with $t = 1$,
$$ |\tilde{\lambda}| \leq 2d(1) \leq 1/2 \,. \tag{24.16} $$
Rearranging the above shows that
$$ 1 - \lambda \geq \frac{1}{t + 1} \,. $$
$\blacksquare$

**24.9. Application to Robustness of Mixing**

We include here an application to robustness of mixing when the probability of staying in place changes in a bounded way.

**Proposition 24.24.** *Let $P$ be an irreducible transition matrix on the state space $\mathcal{X}$ and let $\widetilde{P}(x, y) = \theta(x)P(x, y) + (1 - \theta(x))\delta_x(y)$. Assume that $\theta(x) \geq \theta_\star$ for all $x \in \mathcal{X}$. Then*
$$ t_H(\alpha) \leq \widetilde{t_H}(\theta_\star \alpha) \tag{24.17} $$
$$ \widetilde{t_H}(\alpha) \leq \theta_\star^{-1} t_H(\theta_\star \alpha) \,. \tag{24.18} $$

*Proof.* Note that one can construct the $\widetilde{P}$-chain from the $P$-chain $(X_t)$ by repeating the state $X_t$ for $D_t$ steps, where the conditional distribution of $D_t$, given $X_t = x$, is geometric $(\theta(x))$.

Let $A \subset \mathcal{X}$. Fix any state $x$. Recall that the stationary distribution can be written as
$$ \widetilde{\pi}(A) = \frac{\mathbf{E}_x\left(\sum_{t=0}^{\widetilde{\tau}_x^+ - 1} \mathbf{1}\{\widetilde{X}_t \in A\}\right)}{\mathbf{E}_x(\widetilde{\tau}_x^+)} \,. $$
Conditioning on the excursion from $x$ of the base chain $(X_t)$ shows that
$$ \mathbf{E}_x\left(\sum_{t=0}^{\widetilde{\tau}_x^+ - 1} \mathbf{1}\{\widetilde{X}_t \in A\}\right) = \mathbf{E}_x\left(\sum_{t=0}^{\tau_x^+ - 1} D_t \mathbf{1}\{X_t \in A\}\right) \leq \frac{1}{\theta_\star}\mathbf{E}_x\left(\sum_{t=0}^{\tau_x^+ - 1} \mathbf{1}\{X_t \in A\}\right) \,. $$
Similarly,
$$ \mathbf{E}_x\widetilde{\tau}_A \leq \frac{1}{\theta_\star}\mathbf{E}_x\tau_A \quad\text{ and }\quad \mathbf{E}_x\widetilde{\tau}_x^+ \leq \frac{1}{\theta_\star}\mathbf{E}_x\tau_x^+ \,. \tag{24.19} $$

In addition, both the expected hitting time of a set and the expected occupation time cannot be smaller for the $\widetilde{P}$-chain than for the $P$-chain.

Therefore,
$$ \theta_\star\pi(A) \leq \widetilde{\pi}(A) \leq \frac{1}{\theta_\star}\pi(A) \,. \tag{24.20} $$

Combining (24.20) and (24.19) establishes (24.17) and (24.18).
$\blacksquare$

### PDF page 362 (book page 346)

**Exercises**

**Exercise 24.1.** Show that if $T$ and $T'$ are two independent, positive, integer-valued random variables, independent of a Markov chain $(X_t)_{t \geq 0}$ having stationary distribution $\pi$, then
$$ \|\mathbf{P}_x\{X_{T+T'} = \cdot\} - \pi\|_{\mathrm{TV}} \leq \|\mathbf{P}_x\{X_T = \cdot\} - \pi\|_{\mathrm{TV}} \,. $$

**Exercise 24.2.** Show that $d_G$ is decreasing as a function of $t$.
*Hint*: Let $(\xi_t)$ be i.i.d. uniform random variables on $[0, 1]$, and define
$$ Z_t := \min\{i \geq 1 \,:\, \xi_i \leq t^{-1}\} \,. $$
Write $Z_{t+1} = (Z_{t+1} - Z_t) + Z_t$ and use Exercise 24.1.

**Exercise 24.3.** Let $(X_t)$ be a Markov chain and $W$ and $V$ be two random variables with values in $\mathbb{N}$ and independent of the chain. Then
$$ \|\mathbf{P}\{X_W = \cdot\} - \mathbf{P}\{X_V = \cdot\}\|_{\mathrm{TV}} \leq \|\mathbf{P}\{W = \cdot\} - \mathbf{P}\{V = \cdot\}\|_{\mathrm{TV}}. $$

**Exercise 24.4.** Give a direct proof that $t_{\mathrm{Ces}} \asymp t_{\mathrm{G}}$ for all chains, not necessarily reversible.

**Exercise 24.5.** Consider the "dumbbell" graph in Example 24.3, two copies of the complete graph on $n$ vertices, $K_n$, joined by a single edge. Show that $t_{\mathrm{mix}} \asymp n^2$.
*Hint:* For the upper bound, use coupling.

**Exercise 24.6.** For the Greasy Ladder in Example 24.20, show that $t_{\mathrm{mix}} = O(1)$.
*Hint:* Use coupling.

**Exercise 24.7.**
(a) Consider a lazy birth-and-death chain on $\{0, 1, \ldots, n\}$. Recall that $\tau^\star$ is the absorption time for the evolving-set process started at $S_0 = \{0\}$ and conditioned to be absorbed at $\{0, 1, \ldots, n\}$. (This is defined in Corollary 17.24.) Recall also that $t_\odot$ is the target time defined in Section 10.2. Show that $\mathbf{E}(\tau^\star) = t_\odot$.
(b) In the special case where the chain is simple random walk on $\{0, 1, \ldots, n\}$ with self-loops at the endpoints, calculate $t_\odot$ directly and compare with Example 17.25.

**Notes**

Propositions 24.4 and 24.8 (for $t_{\mathrm{Ces}}$) were proven in **Lovász and Winkler (1995b)**. Lemma 24.7 is due to **Aldous (1982)**, who also proved the equivalence of $t_{\mathrm{mix}}$ and $t_{\mathrm{stop}}$ for reversible continuous-time chains.

Theorem 24.14 is from **Lovász and Winkler (1995b)**, who also proved its converse: every mean optimal stationary time must have a halting state.

Sections 24.4 and 24.5 are from **Peres and Sousi (2015a)**, where it was also shown that, for lazy reversible chains,
$$ t_{\mathrm{mix}} \asymp t_{\mathrm{stop}} \asymp t_{\mathrm{G}} \asymp t_{\mathrm{Ces}} \,, $$
following the ideas of **Aldous (1982)**. As noted there, the idea of using $t_{\mathrm{G}}$ in this context is due to O. Schramm. Similar results for continuous-time reversible chains were obtained by **Oliveira (2012)**.

Example 24.20 was presented in **Aldous (1982)**, who wrote that "a rather complicated analysis" shows that $t_{\mathrm{stop}} \sim cn$ for some $c > 0$, but did not include

### PDF page 363 (book page 347)

the argument. Lemma 24.19 enables a simple calculation of $t_{\text{stop}}$ via hitting times. Essentially the same example is discussed by **Lovász and Winkler (1998)** under the name "the winning streak", and can be found in Section 5.3.5.

Theorem 24.21 was proved by **Griffiths, Kang, Imbuzeiro Oliveira, and Patel (2012)**.

Proposition 24.24 answers a question of K. Burdzy; see **Peres and Sousi (2015a)**.

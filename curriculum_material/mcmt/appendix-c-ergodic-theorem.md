# Appendix C — Ergodic Theorem
*(PDF pages 406–407; book pages 390–391)*

### PDF page 406 (book page 390)

APPENDIX C

# Ergodic Theorem

**C.1. Ergodic Theorem\***

The idea of the ergodic theorem for Markov chains is that "time averages equal space averages".

If $f$ is a real-valued function defined on $\mathcal{X}$ and $\mu$ is any probability distribution on $\mathcal{X}$, then we define

$$ E_\mu(f) = \sum_{x \in \mathcal{X}} f(x)\mu(x). $$

THEOREM C.1 (Ergodic Theorem). *Let $f$ be a real-valued function defined on $\mathcal{X}$. If $(X_t)$ is an irreducible Markov chain with stationary distribution $\pi$, then for any starting distribution $\mu$,*

$$ \mathbf{P}_\mu \left\{ \lim_{t \to \infty} \frac{1}{t} \sum_{s=0}^{t-1} f(X_s) = E_\pi(f) \right\} = 1. \tag{C.1} $$

PROOF. Suppose that the chain starts at $x$. Define $\tau_{x,0}^+ := 0$ and

$$ \tau_{x,k}^+ := \min\{t > \tau_{x,(k-1)}^+ \,:\, X_t = x\}. $$

Since the chain "starts afresh" every time it visits $x$, the blocks $X_{\tau_{x,k}^+}, X_{\tau_{x,k}^+ + 1}, \ldots, X_{\tau_{x,(k+1)}^+ - 1}$ are independent of one another. Thus if

$$ Y_k := \sum_{s = \tau_{x,(k-1)}^+}^{\tau_{x,k}^+ - 1} f(X_s), $$

then the sequence $(Y_k)$ is i.i.d. Note that $\mathbf{E}_x \tau_{x,1}^+ < \infty$ (see Lemma 1.13), and since $\mathcal{X}$ is finite, $B := \max_{z \in \mathcal{X}} |f(z)| < \infty$, whence $\mathbf{E}|Y_1| \leq B \mathbf{E}_x \tau_{x,1}^+ < \infty$. If $S_t = \sum_{s=0}^{t-1} f(X_s)$, then $S_{\tau_{x,n}^+} = \sum_{k=1}^{n} Y_k$, and by the Strong Law of Large Numbers (Theorem A.8),

$$ \mathbf{P}_x \left\{ \lim_{n \to \infty} \frac{S_{\tau_{x,n}^+}}{n} = \mathbf{E}_x(Y_1) \right\} = 1. $$

Again by the Strong Law of Large Numbers, since $\tau_{x,n}^+ = \sum_{k=1}^{n} (\tau_{x,k}^+ - \tau_{x,(k-1)}^+)$, writing simply $\tau_x^+$ for $\tau_{x,1}^+$,

$$ \mathbf{P}_x \left\{ \lim_{n \to \infty} \frac{\tau_{x,n}^+}{n} = \mathbf{E}_x(\tau_x^+) \right\} = 1. $$

### PDF page 407 (book page 391)

Thus,

$$ \mathbf{P}_x \left\{ \lim_{n \to \infty} \frac{S_{\tau_{x,n}^+}}{\tau_{x,n}^+} = \frac{\mathbf{E}_x(Y_1)}{\mathbf{E}_x(\tau_x^+)} \right\} = 1. \tag{C.2} $$

Note that

$$ \mathbf{E}_x(Y_1) = \mathbf{E}_x \left( \sum_{s=0}^{\tau_x^+ - 1} f(X_s) \right) $$
$$ = \mathbf{E}_x \left( \sum_{y \in \mathcal{X}} f(y) \sum_{s=0}^{\tau_x^+ - 1} \mathbf{1}_{\{X_s = y\}} \right) = \sum_{y \in \mathcal{X}} f(y) \mathbf{E}_x \left( \sum_{s=0}^{\tau_x^+ - 1} \mathbf{1}_{\{X_s = y\}} \right). $$

Using (1.25) shows that

$$ \mathbf{E}_x(Y_1) = E_\pi(f) \mathbf{E}_x(\tau_x^+). \tag{C.3} $$

Putting together (C.2) and (C.3) shows that

$$ \mathbf{P}_x \left\{ \lim_{n \to \infty} \frac{S_{\tau_{x,n}^+}}{\tau_{x,n}^+} = E_\pi(f) \right\} = 1. $$

Exercise C.1 shows that (C.1) holds when $\mu = \delta_x$, the probability distribution with unit mass at $x$. Averaging over the starting state completes the proof. $\blacksquare$

Taking $f(y) = \delta_x(y) = \mathbf{1}_{\{y=x\}}$ in Theorem C.1 shows that

$$ \mathbf{P}_\mu \left\{ \lim_{t \to \infty} \frac{1}{t} \sum_{s=0}^{t-1} \mathbf{1}_{\{X_s = x\}} = \pi(x) \right\} = 1, $$

so the asymptotic proportion of time the chain spends in state $x$ equals $\pi(x)$.

**Exercise**

EXERCISE C.1. Let $(a_n)$ be a bounded sequence. If, for a sequence of integers $(n_k)$ satisfying $\lim_{k \to \infty} n_k/n_{k+1} = 1$ and $\lim_{k \to \infty} n_k = \infty$, we have

$$ \lim_{k \to \infty} \frac{a_1 + \cdots + a_{n_k}}{n_k} = a, $$

then

$$ \lim_{n \to \infty} \frac{a_1 + \cdots + a_n}{n} = a. $$

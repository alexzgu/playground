# Appendix A — Background Material
*(PDF pages 379–390; book pages 363–374)*

### PDF page 379 (book page 363)

APPENDIX A

# Background Material

> While writing my book I had an argument with Feller. He asserted that everyone said "random variable" and I asserted that everyone said "chance variable." We obviously had to use the same name in our books, so we decided the issue by a stochastic procedure. That is, we tossed for it and he won.
>
> —J. Doob, as quoted in Snell (1997).

**A.1. Probability Spaces and Random Variables**

Modern probability is based on measure theory. For a full account, the reader should consult one of the many textbooks on the subject, e.g. Billingsley (1995) or Durrett (2005). The majority of this book requires only probability on countable spaces, for which Feller (1968) remains the best reference. For the purpose of establishing notation and terminology we record a few definitions here.

Given a set $\Omega$, a $\sigma$**-*algebra*** is a collection $\mathcal{F}$ of subsets satisfying

(i) $\Omega \in \mathcal{F}$,

(ii) if $A_1, A_2, \ldots$ are elements of $\mathcal{F}$, then $\bigcup_{i=1}^{\infty} A_i \in \mathcal{F}$, and

(iii) if $A \in \mathcal{F}$, then $A^c := \Omega \setminus A \in \mathcal{F}$.

Given a collection of sets $\mathcal{A}$, we write $\sigma(\mathcal{A})$ for the smallest $\sigma$-algebra which contains $\mathcal{A}$.

A ***probability space*** is a set $\Omega$ together with a $\sigma$-algebra of subsets, whose elements are called ***events***.

The following are important cases.

EXAMPLE A.1. If a probability space $\Omega$ is a countable set, the $\sigma$-algebra of events is usually taken to be the collection of all subsets of $\Omega$.

EXAMPLE A.2. If $\Omega$ is $\mathbb{R}^d$, then the ***Borel*** $\sigma$***-*algebra*** is the smallest $\sigma$-algebra containing all open sets.

EXAMPLE A.3. When $\Omega$ is the sequence space $\mathcal{X}^{\infty}$ for a countable set $\mathcal{X}$, a set of the form

$$ A_1 \times A_2 \times \cdots \times A_n \times \mathcal{X} \times \mathcal{X} \times \cdots , \quad A_k \subset \mathcal{X} \text{ for all } k = 1, \ldots, n, $$

is called a ***cylinder*** set. The usual $\sigma$-algebra on $\mathcal{X}^{\infty}$ is the smallest $\sigma$-algebra containing the cylinder sets.

Given a probability space, a ***probability measure*** is a non-negative function $\mathbf{P}$ defined on events and satisfying the following:

(i) $\mathbf{P}(\Omega) = 1$,

### PDF page 380 (book page 364)

(ii) for any sequence of events $B_1, B_2, \ldots$ which are disjoint, meaning $B_i \cap B_j = \varnothing$ for $i \neq j$,

$$ \mathbf{P} \left( \bigcup_{i=1}^{\infty} B_i \right) = \sum_{i=1}^{\infty} \mathbf{P}(B_i). $$

If $\Omega$ is a countable set, a ***probability distribution*** (or sometimes simply a ***probability***) on $\Omega$ is a function $p : \Omega \to [0, 1]$ such that $\sum_{\xi \in \Omega} p(\xi) = 1$. We will abuse notation and write, for any subset $A \subset \Omega$,

$$ p(A) = \sum_{\xi \in A} p(\xi). $$

The set function $A \mapsto p(A)$ is a probability measure.

Given a set $\Omega$ with a $\sigma$-algebra $\mathcal{F}$, a function $f : \Omega \to \mathbb{R}$ is called ***measurable*** if $f^{-1}(B)$ is an element of $\mathcal{F}$ for all open sets $B$. If $\Omega = D$ is an open subset of $\mathbb{R}^d$ and $f : D \to [0, \infty)$ is a measurable function satisfying $\int_D f(x)dx = 1$, then $f$ is called a ***density function***. Given a density function, the set function defined for Borel sets $B$ by

$$ \mu_f(B) = \int_B f(x)dx $$

is a probability measure. (Here, the integral is the *Lebesgue* integral. It agrees with the usual Riemann integral wherever the Riemann integral is defined.)

Given a probability space $(\Omega, \mathcal{F})$, a ***random variable*** $X$ is a measurable function defined on $\Omega$. We write $\{X \in A\}$ as shorthand for the set

$$ \{\omega \in \Omega \, : \, X(\omega) \in A\} = X^{-1}(A) \, . $$

The ***distribution*** of a random variable $X$ is the probability measure $\mu_X$ on $\mathbb{R}$ defined for Borel sets $B$ by

$$ \mu_X(B) := \mathbf{P}\{X \in B\} := \mathbf{P}(\{X \in B\}). $$

We call a random variable $X$ ***discrete*** if there is a finite or countable set $S$, called the ***support of*** $X$, such that $\mu_X(S) = 1$. In this case, the function

$$ p_X(a) = \mathbf{P}\{X = a\} $$

is a probability distribution on $S$.

A random variable $X$ is called ***absolutely continuous*** if there is a density function $f$ on $\mathbb{R}$ such that

$$ \mu_X(A) = \int_A f(x)dx. $$

For a *simple* random variable $X$ having the form $X = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}$, where $\{A_i\}$ are disjoint, we define

$$ \mathbf{E}[X] = \sum_{i=1}^{n} a_i \mathbf{P}(A_i) \, . $$

If $X \geq 0$, we can define the simple random variable $X_n$ by

$$ X_n = \sum_{k=0}^{n2^n} X(k2^{-n}) \mathbf{1}_{\{k2^{-n} < X \leq (k+1)2^{-n}\}} \, . $$

It can be shown that $\lim_n \mathbf{E}(X_n)$ exists (although it may be infinite), and we define $\mathbf{E}(X)$ to be this limit. For a general $X$, we write $X = X^+ - X^-$, where $X^+$ and

### PDF page 381 (book page 365)

$X^-$ are non-negative, and define $\mathbf{E}(X) = \mathbf{E}(X^+) - \mathbf{E}(X^-)$ in the case where both are not infinite.

For a discrete random variable $X$, the **_expectation_** $\mathbf{E}(X)$ can be computed by the formula

$$ \mathbf{E}(X) = \sum_{x \in \mathbb{R}} x \mathbf{P}\{X = x\}. $$

(Note that there are at most countably many non-zero summands.) For an absolutely continuous random variable $X$, the expectation is computed by the formula

$$ \mathbf{E}(X) = \int_{\mathbb{R}} x f_X(x) dx. $$

If $X$ is a random variable, $g : \mathbb{R} \to \mathbb{R}$ is a function, and $Y = g(X)$, then the expectation $\mathbf{E}(Y)$ can be computed via the formulas

$$ \mathbf{E}(Y) = \begin{cases} \int g(x) f(x) dx & \text{if } X \text{ is continuous with density } f, \\ \sum_{x \in S} g(x) p_X(x) & \text{if } X \text{ is discrete with support } S. \end{cases} $$

The **_variance_** of a random variable $X$ is defined by

$$ \mathrm{Var}(X) = \mathbf{E}\left( (X - \mathbf{E}(X))^2 \right). $$

Fix a probability space and probability measure $\mathbf{P}$. Two events, $A$ and $B$, are **_independent_** if $\mathbf{P}(A \cap B) = \mathbf{P}(A)\mathbf{P}(B)$. Events $A_1, A_2, \ldots$ are independent if for any $i_1, i_2, \ldots, i_r$,

$$ \mathbf{P}(A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_r}) = \mathbf{P}(A_{i_1})\mathbf{P}(A_{i_2}) \cdots \mathbf{P}(A_{i_r}). $$

Random variables $X_1, X_2, \ldots$ are independent if for all Borel sets $B_1, B_2, \ldots$, the events $\{X_1 \in B_1\}, \{X_2 \in B_2\}, \ldots$ are independent.

**PROPOSITION A.4.** *If $X$ and $Y$ and independent random variables such that $\mathrm{Var}(X)$ and $\mathrm{Var}(Y)$ exists, then $\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)$.*

There are two fundamental inequalities.

**PROPOSITION A.5** (Markov's Inequality). *For a non-negative random variable $X$,*

$$ \mathbf{P}\{X > a\} \leq \frac{\mathbf{E}(X)}{a}. $$

**PROPOSITION A.6** (Chebyshev's Inequality). *For a random variable $X$ with finite expectation $\mathbf{E}(X)$ and finite variance $\mathrm{Var}(X)$,*

$$ \mathbf{P}\{|X - \mathbf{E}(X)| > a\} \leq \frac{\mathrm{Var}(X)}{a^2}. $$

A sequence of random variables $(X_t)$ **_converges in probability_** to a random variable $X$ if

$$ \lim_{t \to \infty} \mathbf{P}\{|X_t - X| > \varepsilon\} = 0, \tag{A.1} $$

for all $\varepsilon$. This is denoted by $X_t \xrightarrow{\mathrm{pr}} X$.

**THEOREM A.7** (Weak Law of Large Numbers). *If $(X_t)$ is a sequence of independent random variables such that $\mathbf{E}(X_t) = \mu$ and $\mathrm{Var}(X_t) = \sigma^2$ for all $t$, then*

$$ \frac{1}{T} \sum_{t=1}^{T} X_t \xrightarrow{\mathrm{pr}} \mu \quad \text{as } T \to \infty. $$

### PDF page 382 (book page 366)

*PROOF.* By linearity of expectation, $\mathbf{E}(T^{-1} \sum_{t=1}^{T} X_t) = \mu$, and by independence, $\mathrm{Var}(T^{-1} \sum_{t=1}^{T} X_t) = \sigma^2/T$. Applying Chebyshev's inequality,

$$ \mathbf{P}\left\{ \left| \frac{1}{T} \sum_{t=1}^{T} X_t - \mu \right| > \varepsilon \right\} \leq \frac{\sigma^2}{T\varepsilon^2}. $$

For every $\varepsilon > 0$ fixed, the right-hand side tends to zero as $T \to \infty$. $\blacksquare$

**THEOREM A.8** (Strong Law of Large Numbers). *Let $Z_1, Z_2, \ldots$ be a sequence of random variables with $\mathbf{E}(Z_s) = 0$ for all $s$ and*

$$ \mathrm{Var}(Z_{s+1} + \cdots + Z_{s+k}) \leq Ck $$

*for all $s$ and $k$. Then*

$$ \mathbf{P}\left\{ \lim_{t \to \infty} \frac{1}{t} \sum_{s=0}^{t-1} Z_s = 0 \right\} = 1. \tag{A.2} $$

*PROOF.* Let $A_t := t^{-1} \sum_{s=0}^{t-1} Z_s$. Then

$$ \mathbf{E}(A_t^2) = \frac{\mathbf{E}\left[ \left( \sum_{s=0}^{t-1} Z_s \right)^2 \right]}{t^2} \leq \frac{C}{t}. $$

Thus, $\mathbf{E}\left( \sum_{m=1}^{\infty} A_{m^2}^2 \right) < \infty$, which in particular implies that

$$ \mathbf{P}\left\{ \sum_{m=1}^{\infty} A_{m^2}^2 < \infty \right\} = 1 \quad \text{and} \quad \mathbf{P}\left\{ \lim_{m \to \infty} A_{m^2} = 0 \right\} = 1. \tag{A.3} $$

For a given $t$, let $m_t$ be such that $m_t^2 \leq t < (m_t + 1)^2$. Then

$$ A_t = \frac{1}{t} \left( m_t^2 A_{m_t^2} + \sum_{s=m_t^2}^{t-1} Z_s \right). \tag{A.4} $$

Since $\lim_{t \to \infty} t^{-1} m_t^2 = 1$, by (A.3),

$$ \mathbf{P}\left\{ \lim_{t \to \infty} t^{-1} m_t^2 A_{m_t^2} = 0 \right\} = 1. \tag{A.5} $$

Defining $B_t := t^{-1} \sum_{s=m_t^2}^{t-1} Z_s$,

$$ \mathbf{E}(B_t^2) = \frac{\mathrm{Var}\left( \sum_{s=m_t^2}^{t-1} Z_s \right)}{t^2} \leq \frac{2Cm_t}{t^2} \leq \frac{2C}{t^{3/2}}. $$

Thus $\mathbf{E}(\sum_{t=0}^{\infty} B_t^2) < \infty$, and

$$ \mathbf{P}\left\{ \lim_{t \to \infty} \frac{\sum_{s=m_t^2+1}^{t} Z_s}{t} = 0 \right\} = 1. \tag{A.6} $$

Putting together (A.5) and (A.6), from (A.4) we conclude that (A.2) holds. $\blacksquare$

Another important result about sums of independent and identically distributed random variables is that their distributions are approximately normal:

### PDF page 383 (book page 367)

**THEOREM A.9** (Central Limit Theorem). *For each $n$, let $X_{n,1}, X_{n,2}, \ldots, X_{n,n}$ be independent random variables, each with the same distribution having expectation $\mu = \mathbf{E}(X_{n,1})$ and variance $\sigma^2 = \mathrm{Var}(X_{n,1})$. Let $S_n = \sum_{i=1}^{n} X_{n,i}$. Then for all $x \in \mathbb{R}$,*

$$ \lim_{n \to \infty} \mathbf{P}\left\{ \frac{S_n - n\mu}{\sqrt{n}\sigma} \leq x \right\} = \Phi(x), $$

*where $\Phi(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx$.*

The following is a *large deviation* inequality due to Hoeffding (**1963**), also known as the Hoeffding-Azuma inequality. We follow the exposition by Steele (**1997**).

**THEOREM A.10.** *Let $\{X_1, \ldots, X_n\}$ be random variables with $|X_i| \leq B_i$ for constants $\{B_i\}$ and such that*

$$ \mathbf{E}\left[ X_{i_1} \cdots X_{i_k} \right] = 0 \qquad \text{for all} \quad 1 \leq i_1 < \ldots < i_k \,. $$

*(For instance, the $\{X_i\}$ are independent variables with zero mean or $X_i = M_k - M_{k-1}$ for a martingale $\{M_k\}$.) Then*

$$ \mathbf{P}\left\{ \sum_{i=1}^{n} X_i \geq L \right\} \leq e^{-L^2 / \left( 2 \sum_{i=1}^{n} B_i^2 \right)} \,. $$

*PROOF.* For any sequences of constants $\{a_i\}$ and $\{b_i\}$, we have

$$ \mathbf{E}\left[ \prod_{i=1}^{n} (a_i + b_i X_i) \right] = \prod_{i=1}^{n} a_i \,. \tag{A.7} $$

By Exercise A.1,

$$ e^{ax} \leq \cosh a + x \sinh a \,. $$

If we now let $x = X_i/B_i$ and $a = tB_i$, then we find that

$$ \exp\left( t \sum_{i=1}^{n} X_i \right) \leq \prod_{i=1}^{n} \left[ \cosh(tB_i) + \frac{X_i}{B_i} \sinh(tB_i) \right] \,. $$

Taking expectations and using (A.7), we have

$$ \mathbf{E}\left[ \exp\left( t \sum_{i=1}^{n} X_i \right) \right] \leq \prod_{i=1}^{n} \cosh(tB_i) \,. $$

So, by the elementary bound $\cosh x = \sum_{k=0}^{\infty} \frac{x^{2k}}{(2k)!} \leq \sum_{k=0}^{\infty} \frac{x^{2k}}{2^k k!} = e^{x^2/2}$, we have

$$ \mathbf{E}\left[ \exp\left( t \sum_{i=1}^{n} X_i \right) \right] \leq \exp\left( \frac{t^2}{2} \sum_{i=1}^{n} B_i^2 \right) \,. $$

By Markov's inequality and the above we have that, for any $t > 0$,

$$ \mathbf{P}\left\{ \sum_{i=1}^{n} X_i \geq L \right\} = \mathbf{P}\left\{ \exp\left( t \sum_{i=1}^{n} X_i \right) \geq e^{Lt} \right\} \leq e^{-Lt} \exp\left( \frac{t^2}{2} \sum_{i=1}^{n} B_i^2 \right) \,. $$

Letting $t = L(\sum_{i=1}^{n} B_i^2)^{-1}$ we obtain the required result. $\blacksquare$

### PDF page 384 (book page 368)

**FIGURE A.1.** A sequence of functions whose integrals do not converge to the integral of the limit. *[Figure: a triangular "tent" function on the horizontal axis; the peak reaches height $n$ (marked on the vertical axis) at the point $1/n$, and the triangle's base runs from the origin to $2/n$ (marked on the horizontal axis), so the triangle has base $2/n$ and height $n$.]*

**A.1.1. Limits of expectations.** We know from calculus that if $(f_n)$ is a sequence of functions defined on an interval $I$, satisfying for every $x \in I$

$$ \lim_{n \to \infty} f_n(x) = f(x) \,, $$

then it is not necessarily the case that

$$ \lim_{n \to \infty} \int_I f_n(x) dx = \int_I f(x) dx \,. $$

As an example, consider the function $g_n$ whose graph is shown in Figure A.1. The integral of this function is always 1, but for each $x \in [0, 1]$, the limit $\lim_{n \to \infty} g_n(x) = 0$. That is,

$$ \int_0^1 \lim_{n \to \infty} g_n(x) dx = 0 \neq 1 = \lim_{n \to \infty} \int_0^1 g_n(x) dx. \tag{A.8} $$

This example can be rephrased using random variables. Let $U$ be a uniform random variable, and let $Y_n = g_n(U)$. Notice that $Y_n \to 0$. We have

$$ \mathbf{E}(Y_n) = \mathbf{E}(g_n(U)) = \int g_n(x) f_U(x) dx = \int_0^1 g_n(x) dx, $$

as the density of $U$ is $f_U = \mathbf{1}_{[0,1]}$. By (A.8),

$$ \lim_{n \to \infty} \mathbf{E}(Y_n) \neq \mathbf{E} \left( \lim_{n \to \infty} Y_n \right). $$

Now that we have seen that we cannot always move a limit inside an expectation, can we ever? The answer is "yes", given some additional assumptions.

PROPOSITION A.11. *Let $Y_n$ be a sequence of random variables and let $Y$ be a random variable such that $\mathbf{P} \{\lim_{n \to \infty} Y_n = Y\} = 1$.*

  (i) *If there is a constant $K$ independent of $n$ such that $|Y_n| < K$ for all $n$, then $\lim_{n \to \infty} \mathbf{E}(Y_n) = \mathbf{E}(Y)$.*
 (ii) *If there is a random variable $Z$ such that $\mathbf{E}(|Z|) < \infty$ and $\mathbf{P} \{ |Y_n| \leq |Z| \} = 1$ for all $n$, then $\lim_{n \to \infty} \mathbf{E}(Y_n) = \mathbf{E}(Y)$.*
(iii) *If $\mathbf{P}\{Y_n \leq Y_{n+1}\} = 1$ for all $n$, then $\lim_{n \to \infty} \mathbf{E}(Y_n) = \mathbf{E}(Y)$ .*

### PDF page 385 (book page 369)

Proposition A.11(i) is called the **Bounded Convergence Theorem**, Proposition A.11(ii) is called the **Dominated Convergence Theorem**, and Proposition A.11(iii) is called the **Monotone Convergence Theorem**.

PROOF OF (I). For any $\varepsilon > 0$,

$$ |Y_n - Y| \leq 2K\mathbf{1}_{\{|Y_n - Y| > \varepsilon/2\}} + \varepsilon/2, $$

and taking expectation above shows that

$$ \begin{aligned} |\mathbf{E}(Y_n) - \mathbf{E}(Y)| &\leq \mathbf{E}\left(|Y_n - Y|\right) \\ &\leq 2K\mathbf{P}\left\{|Y_n - Y| > \varepsilon/2\right\} + \varepsilon/2. \end{aligned} $$

Since $\mathbf{P}\left\{|Y_n - Y| \geq \varepsilon/2\right\} \to 0$, by taking $n$ sufficiently large,

$$ |\mathbf{E}(Y_n) - \mathbf{E}(Y)| \leq \varepsilon. $$

That is, $\lim_{n \to \infty} \mathbf{E}(Y_n) = \mathbf{E}(Y)$. $\blacksquare$

For proofs of (ii) and (iii), see **Billingsley (1995)**.

**A.2. Conditional Expectation**

**A.2.1. Conditioning on a partition.** If $X$ is a random variable defined on a probability space $(\Omega, \mathcal{F}, \mathbf{P})$, and $A$ is an event (so $A \in \mathcal{F}$) with $\mathbf{P}(A) > 0$, then we define the real *number*

$$ \mathbf{E}[X \mid A] := \frac{1}{\mathbf{P}(A)} \mathbf{E}[X\mathbf{1}_A] \,. $$

A countable *partition* $\Pi$ of $\Omega$ is a sequence of disjoint events $\{A_i\}$ such that $\bigcup_i A_i = \Omega$. We will assume that such partitions always have $\mathbf{P}(A_i) > 0$ for all $i$. For example, if $Y$ is a discrete random variable with values $\{y_i\}$, the events $A_i = \{Y = y_i\}$ form a partition. One, and only one, among the events $\{A_i\}$ will occur. For a partition $\Pi$, we let $\mathcal{G} = \mathcal{G}(\Pi)$ be all countable unions of sets from $\Pi$, that is, we set $\mathcal{G} = \left\{ \bigcup_j A_{i_j} \, : \, A_{i_j} \in \Pi \right\}$. If an observer knows which among the elements of $\Pi$ has occurred (and has no other information), then the sets in $\mathcal{G}$ are those sets for which she knows the status (having occurred or not). Informally speaking, we want to define the conditional expectation of $X$ given the knowledge about the status of $\mathcal{G}$-events. In particular, if we know that $A_i$ has occured, this conditional expectation should have the value $\mathbf{E}[X \mid A_i]$. The appropriate definition is

$$ \mathbf{E}[X \mid \mathcal{G}] := \sum_{i=1}^{\infty} \mathbf{E}[X \mid A_i]\mathbf{1}_{A_i} \,. $$

It is important to note that $\mathbf{E}[X \mid \mathcal{G}]$ is a random variable.

EXAMPLE A.12. Let $Y$ be a discrete random variable defined on the same probability space $(\Omega, \mathcal{F}, \mathbf{P})$ as the random variable $X$. Suppose that $Y$ takes values in $\{y_i\}_{i=1}^{\infty}$. The events $\Pi = \{Y = y_i\}_{i=1}^{\infty}$ form a countable partition of $\Omega$, and the "information in $\Pi$" is the knowledge about the value of $Y$. In this case, $\mathbf{E}[X \mid \mathcal{G}]$ is denoted by $\mathbf{E}[X \mid Y]$, and corresponds to the usual elementary definition of conditional expectation given a discrete random variable: On the event $\{Y = y_i\}$, the value of $\mathbf{E}[X \mid Y]$ is $\mathbf{E}[X \mid Y = y_i]$.

### PDF page 386 (book page 370)

**A.2.2. Conditional expectation with respect to a $\sigma$-algebra.** For a countable partition of $\Omega$, the smallest $\sigma$-algebra containing $\Pi$ is exactly the collection of sets $\mathcal{G}$ above, that is, countable unions of elements from $\Pi$. Letting $A \in \mathcal{G}$ and $Y = \mathbf{E}[X \mid \mathcal{G}]$, then

$$ \mathbf{E}[Y\mathbf{1}_A] = \mathbf{E}[X\mathbf{1}_A] \quad \text{ for all } A \in \mathcal{G} \,. \tag{A.9} $$

In the case where $A$ is a single element of $\Pi$, this is immediate; in the more general case where $A$ is a countable union of partition elements, it follows from additivity. In addition, it is elementary to check that $\mathbf{E}[Y \mid \mathcal{G}]$ is measurable with respect to $\mathcal{G}$. This fact together with (A.9) turn out to be the essential properties of conditional expectation.

Let $(\Omega, \mathcal{F}, \mathbf{P})$ be a probability space, and $\mathcal{G} \subset \mathcal{F}$ be a $\sigma$-algebra on $\Omega$, and let $X$ be a random variable on $(\Omega, \mathcal{F})$. The *conditional expectation* of $X$ with respect to $\mathcal{G}$ is defined to be a random variable $Y$ which satisfies

  (i) $Y$ is measurable with respect to $\mathcal{G}$, and
 (ii) For all $G \in \mathcal{G}$,
$$ \mathbf{E}[Y\mathbf{1}_G] = \mathbf{E}[X\mathbf{1}_G] \,. $$

We show below that the conditional expectation always exists when $\mathbf{E}|X| < \infty$, and is essentially unique, that is, if there are two random variables satisfying these properties, then these variables are equal to one another with probability one.

Finally, given an event $A \in \mathcal{F}$ and a $\sigma$-algebra $\mathcal{G}$, we define

$$ \mathbf{P}(A \mid \mathcal{G}) := \mathbf{E}[\mathbf{1}_A \mid \mathcal{G}] \,. $$

Key properties of conditional expectation are

$$ Z\mathbf{E}[Y \mid \mathcal{G}] = \mathbf{E}[ZY \mid \mathcal{G}] \quad \text{ whenever } Z \text{ is } \mathcal{G}\text{-measurable} \,, \tag{A.10} $$

and

$$ \mathbf{E}[\mathbf{E}[Y \mid \mathcal{G}_1] \mid \mathcal{G}_2] = \mathbf{E}[\mathbf{E}[Y \mid \mathcal{G}_2] \mid \mathcal{G}_1] = \mathbf{E}[Y \mid \mathcal{G}_1] \quad \text{ whenever } \mathcal{G}_1 \subset \mathcal{G}_2 \ . \tag{A.11} $$

**A.2.3. Existence of Conditional Expectation.**

LEMMA A.13. *Let $X$ be a random variable on $(\Omega, \mathcal{F}, \mathbf{P})$ such that $\mathbf{E}[X^2] < \infty$. Let $\mathcal{G}$ be a $\sigma$-algebra on $\Omega$. There is a random variable $Y$ satisfying (i) and (ii) in the definition of conditional expectation, and $Y$ is essentially unique.*

PROOF. The space $L^2(\Omega, \mathcal{F}, \mathbf{P})$ consisting of all random variables on $(\Omega, \mathcal{F}, \mathbf{P})$ with finite second moments and with the inner product $\langle X, Y \rangle := \mathbf{E}[XY]$ defines a Hilbert space. The space $S$ of all $\mathcal{G}$-measurable elements of $L^2$ forms a closed subspace. Let $\Pi$ be the projection onto $S$. Consider $Y := \Pi X$. Clearly $Y$ is $\mathcal{G}$-measurable. Let $A \in \mathcal{G}$. The random variable $X - \Pi(X)$ is in the orthogonal compliment [sic] to $S$, so

$$ 0 = \mathbf{E}[(X - \Pi(X))\mathbf{1}_A] = \mathbf{E}[X\mathbf{1}_A] - \mathbf{E}[\Pi(X)\mathbf{1}_A] \,. $$

Thus $Y$ satisifes [sic] (i) and (ii) in the definition of conditional expectation. $\blacksquare$

LEMMA A.14. *If $X$ is an $L^2$ random variable with $X \geq 0$, then $\mathbf{E}[X \mid \mathcal{G}] \geq 0$.*

PROOF. We have that

$$ 0 \geq \int_{\{\mathbf{E}[X\mid\mathcal{G}]<0\}} \mathbf{E}[X \mid \mathcal{G}] d\mathbf{P} = \int_{\{\mathbf{E}[X\mid\mathcal{G}]<0\}} X d\mathbf{P} \geq 0 \,. $$

### PDF page 387 (book page 371)

Therefore, $\int_{\{\mathbf{E}[X|\mathcal{G}]<0\}} X d\mathbf{P} = 0$, and since $X \geq 0$ is integrable, it follows that $\mathbf{P}\{\mathbf{E}[X \mid \mathcal{G}] < 0\} = 0$. $\blacksquare$

LEMMA A.15. *Let $X$ be a random variable on $(\Omega, \mathcal{F}, \mathbf{P})$ with $\mathbf{E}|X| < \infty$, and let $\mathcal{G}$ be a $\sigma$-algebra on $\Omega$. There is a random variable $Y$ such that $Y$ satisfies (i) and (ii) in the definition of conditional expectation.*

PROOF. First assume that $X \geq 0$. Let $X_n = X\mathbf{1}_{\{X<n\}}$. Since $X_n$ is square-integrable, there exists $Y_n$ which is the conditional expectation $\mathbf{E}[X_n \mid \mathcal{G}]$. By the previous lemma, $\mathbf{E}[X_n \mid \mathcal{G}] \uparrow$. Let $Y = \lim_{n\to\infty} Y_n$. We have that

$$ \mathbf{E}\lim_n Y_n \leq \lim_n \mathbf{E}Y_n = \mathbf{E}X < \infty, $$

so $Y_n$ is in $L^1$. (In particular, $Y < \infty$ almost surely.) Also, $Y$ is $\mathcal{G}$-measurable. We have by the Monotone Convergence Theorem that

$$ \mathbf{E}[Y\mathbf{1}_A] = \mathbf{E}[\lim_{n\to\infty} Y_n\mathbf{1}_A] = \lim_{n\to\infty} \mathbf{E}[Y_n\mathbf{1}_A] = \mathbf{E}[X\mathbf{1}_A]. $$

It follows that $Y = \mathbf{E}[X \mid \mathcal{G}]$. Now if $X$ is a (not-necessarily non-negative) element of $L^1$, then $X = X^+ - X^-$ where $X^+$ and $X^-$ are non-negative. We can let $\mathbf{E}[X \mid \mathcal{G}] = \mathbf{E}[X^+ \mid \mathcal{G}] - \mathbf{E}[X^- \mid \mathcal{G}]$. The reader can check that this works. $\blacksquare$

EXAMPLE A.16. Let $X$ and $Y$ be random variables with a positive joint density function $f : \mathbb{R}^2 \to \mathbb{R}$, so that for any Borel set $A$ in the plane,

$$ \mathbf{P}\{(X,Y) \in A\} = \iint_A f(s,t) ds dt. $$

Assume that $\mathbf{E}[|X|] < \infty$. Let $c_t = \left[\int_{-\infty}^{\infty} f(s,t) ds\right]^{-1}$, so that $c_t f(\cdot, t)$ defines a probability density function. Also, Let

$$ \varphi(t) = \int_{-\infty}^{\infty} u c_t f(u,t) du, $$

and consider the random variable $\varphi(Y)$. Clearly it is measurable with respect to $\sigma(Y)$, and for any $a < b$,

$$ \mathbf{E}[\varphi(Y)\mathbf{1}_{\{a<Y\leq b\}}] = \iint \varphi(t)\mathbf{1}_{\{a<t\leq b\}} f(s,t) ds dt $$
$$ = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} u c_t f(u,t)\mathbf{1}_{\{a<t\leq b\}} du f(s,t) ds dt $$

Since $\mathbf{E}|X| < \infty$, we can exchange order of integration above. The right-hand side equals

$$ \iint c_t \left[\int_{-\infty}^{\infty} f(s,t) ds\right] u\mathbf{1}_{\{a<t\leq b\}} f(u,t) du dt $$
$$ = \iint u\mathbf{1}_{\{a<t\leq b\}} f(u,t) du dt = \mathbf{E}[X\mathbf{1}_{\{a<Y<b\}}]. $$

We conclude that $\varphi(Y) = \mathbf{E}[X \mid Y]$.

### PDF page 388 (book page 372)

**A.2.4. Markov property with respect to filtrations.** A *filtration* $\{\mathcal{F}_t\}$ is a non-decreasing family of $\sigma$-algebras. For example, if $\{X_t\}_{t=0}^{\infty}$ is a sequence of random variables, we can let $\mathcal{F}_t = \sigma(X_0, \ldots, X_t)$ be the smallest $\sigma$-algebra with respect to which $X_0, X_1, \ldots, X_t$ are measureable. This is called the *natural* filtration. A sequence of random variables $\{X_t\}$ is *adapted* to a filtration if $\sigma(X_0, \ldots, X_t) \subset \mathcal{F}_t$ for all $t \geq 0$.

Let $\{X_t\}$ be a Markov chain. Assume that $\{X_t\}$ is adapted to $\{\mathcal{F}_t\}$. For the cylinder set

$$ A = A_1 \times A_2 \times \cdots \times A_m \times \mathcal{X}^{\infty}, $$

set

$$ P_x(A) := \mathbf{P}_x((X_0, X_1, \ldots) \in A) $$
$$ = \sum_{(a_0, a_1, \ldots, a_m) \in A_1 \times \cdots A_m} \delta_x(a_0) P(a_0, a_1) \cdots P(a_{m-1}, a_m), \quad \text{(A.12)} $$

the probability that the chain belongs to $A$ when started at $x \in \mathcal{X}$. The set-function $P_x(\cdot)$ can be extended to a measure on the $\sigma$-algebra generated by cylinder sets.

We say that $\{X_t\}$ is ***Markov with respect to the filtration*** $\{\mathcal{F}_t\}$ if

$$ \mathbf{P}_x\{(X_t, X_{t+1}, \ldots) \in A \mid \mathcal{F}_t\} = P_{X_t}(A). $$

Note that if $\{X_t\}$ is Markov with respect to the filtration $\{\mathcal{F}_t\}$, then $\{X_t\}$ is a Markov chain by the earlier definition. (We leave the reader to check.)

EXAMPLE A.17. Let $Z_1, Z_2, \ldots$ be i.i.d. uniform random variables on $[0, 1]$, and let $\mathcal{F}_t = \sigma(Z_1, \ldots, Z_t)$. Let $\{X_t\}$ be the Markov chain constructed in the proof of Proposition 1.5. Then $\{X_t\}$ is adapted to $\{\mathcal{F}_t\}$, and the sequence is Markov with respect to $\{\mathcal{F}_t\}$.

EXAMPLE A.18. Consider the random walk on the $d$-dimensional hypercube, generated by first selecting a coordinate at random, and then tossing a coin to decide the bit at the selected coordinate. Let $\mathcal{F}_t$ be the $\sigma$-field generated by the bit selections and the coin tosses, and let $X_t$ be the state of the walker at time $t$. Then $\{X_t\}$ is a Markov chain with respect to the filtration $\{\mathcal{F}_t\}$. Note that given the history of the chain $(X_s)_{s\leq t}$, it is not possible in general to recover the coordinate selection variables. In particular, when $X_{t+1} = X_t$, it is not possible to determine (from the states of the walker alone) which coordinate was selected.

**A.3. Strong Markov Property**

When bounding the expected time to return to a recurrent state, we implicitly used the *strong Markov property*. Informally, this is usually phrased as "the chain starts afresh at any stopping time". We now convert this to mathematics.

Let $\{X_t\}$ be a Markov chain with respect to the filtration $\{\mathcal{F}_t\}$. A ***stopping time*** $\tau$ is a random variable with values in $\{0, 1, \ldots\} \cup \{\infty\}$ satisfying

$$ \{\tau = t\} \in \mathcal{F}_t \quad \text{for all } t \geq 0. \tag{A.13} $$

For example, if $\tau = \min\{t \geq 0 : X_t \in A\}$ is the first time the chain visits the set $A$, then $\{\tau = t\}$ can be written as $\{X_0 \notin A, \ldots, X_{t-1} \notin A, X_t \in A\}$, which is an element of $\mathcal{F}_t$ since $\{X_t\}$ is adapted to $\{\mathcal{F}_t\}$.

For a stopping time $\tau$, we define

$$ \mathcal{F}_\tau = \{B \in \mathcal{F} : B \cap \{\tau = t\} \in \mathcal{F}_t\}. \tag{A.14} $$

### PDF page 389 (book page 373)

Informally, $\mathcal{F}_\tau$ consists of events which, on the event that the stopping time equals $t$, are determined by the "history up to $t$", i.e. by $\mathcal{F}_t$. We can now state the Strong Markov Property.

PROPOSITION A.19. *For a cylinder set $A$ of the form*

$$ A = A_1 \times A_2 \times \cdots \times A_m \times \mathcal{X}^{\infty}, $$

*and let $P_x(A)$ be as defined in (A.12). Then*

$$ \mathbf{P}_x\{\tau < \infty, \ (X_\tau, X_{\tau+1}, \ldots) \in A \mid \mathcal{F}_\tau\} = P_{X_\tau}(A)\mathbf{1}_{\{\tau<\infty\}}. \tag{A.15} $$

REMARK 1. In fact the above holds for all sets $A$ in the $\sigma$-algebra generated by the cylinder sets.

PROOF. Let $B \in \mathcal{F}_\tau$. Then

$$ \mathbf{E}_x[P_{X_\tau}(A)\mathbf{1}_{\{\tau<\infty\}}\mathbf{1}_B] = \sum_{t=0}^{\infty} \mathbf{E}_x[P_{X_t}(A)\mathbf{1}_{\{\tau=t\}\cap B}]. \tag{A.16} $$

Since $\{\tau = t\} \cap B \in \mathcal{F}_t$, and $P_{X_t}(A)$ equals $\mathbf{P}_x\{(X_t, X_{t+1}, \ldots) \in A \mid \mathcal{F}_t\}$ by the Markov property, the right-hand side equals

$$ \sum_{t=0}^{\infty} \mathbf{P}_x(\{(X_t, X_{t+1}, \ldots) \in A\} \cap B \cap \{\tau = t\}) $$
$$ = \mathbf{P}_x(\{\tau < \infty, \ (X_\tau, X_{\tau+1}, \ldots) \in A\} \cap B). $$

Thus $P_{X_\tau}(A)\mathbf{1}_{\{\tau<\infty\}}$ is a version of

$$ P_x\{\tau < \infty, \ (X_\tau, X_{\tau+1}, \cdots) \in A \mid \mathcal{F}_\tau\}. $$

$\blacksquare$

**A.4. Metric Spaces**

A set $M$ equipped with a function $\rho$ measuring the distance between its elements is called a ***metric space***. In Euclidean space $\mathbb{R}^k$, the distance between vectors is measured by the norm $\|x - y\| = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}$. On a graph, distance can be measured as the length of the shortest path connecting $x$ and $y$. These are examples of metric spaces.

The function $\rho$ must satisfy some properties to reasonably be called a distance. In particular, it should be symmetric, i.e., there should be no difference between measuring from $a$ to $b$ and measuring from $b$ to $a$. Distance should never be negative, and there should be no two distinct elements which have distance zero. Finally, the distance $\rho(a, c)$ from $a$ to $c$ should never be greater than proceeding via a third point $b$ and adding the distances $\rho(a, b) + \rho(b, c)$. For obvious reasons, this last property is called the ***triangle inequality***.

We summarize these properties here:

(i) $\rho(a, b) = \rho(b, a)$ for all $a, b \in M$.
(ii) $\rho(a, b) \geq 0$ for all $a, b \in M$, and $\rho(a, b) = 0$ only if $a = b$.
(iii) For any three elements $a, b, c \in M$,

$$ \rho(a, c) \leq \rho(a, b) + \rho(b, c). \tag{A.17} $$

### PDF page 390 (book page 374)

**A.5. Linear Algebra**

THEOREM A.20 (Spectral Theorem for Symmetric Matrices). *If $M$ is a symmetric $m \times m$ matrix, then there exists a matrix $U$ with $U^T U = I$ and a real diagonal matrix $\Lambda$ such that $M = U^T \Lambda U$.*

(The matrix $U^T$ is the ***transpose*** of $U$, whose entries are given by $U_{i,j}^T := U_{j,i}$.) A proof of Theorem A.20 can be found, for example, in **Horn and Johnson (1990**, Theorem 4.1.5).

Another way of formulating the Spectral Theorem is to say that there is an orthonormal basis of eigenvectors for $M$. The columns of $U^T$ form one such basis, and the eigenvalue associated to the $i$-th column is $\lambda_i = \Lambda_{ii}$.

The variational characterization of the eigenvalues of a symmetric matrix is very useful:

THEOREM A.21 (Rayleigh-Ritz). *Let $M$ be a symmetric matrix with eigenvalues*
$$ \lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n $$
*and associated eigenvectors $x_1, \ldots, x_n$. Then*
$$ \lambda_k = \max_{\substack{x \neq 0 \\ x \perp x_1, \ldots, x_{k-1}}} \frac{\langle x, Ax \rangle}{\langle x, x \rangle}. $$

See **Horn and Johnson (1990**, p. 178) for a discussion.

**A.6. Miscellaneous**

***Stirling's formula*** says that
$$ n! \sim \sqrt{2\pi} e^{-n} n^{n+1/2}, \tag{A.18} $$
where $a_n \sim b_n$ means that $\lim_{n \to \infty} a_n b_n^{-1} = 1$.

More precise results are known, for example,
$$ n! = \sqrt{2\pi} e^{-n} n^{n+1/2} e^{\varepsilon_n}, \qquad \frac{1}{12n+1} \leq \varepsilon_n \leq \frac{1}{12n}. \tag{A.19} $$

**Exercises**

EXERCISE A.1.
(i) Use the fact that the function $f(x) = e^{ax}$ is convex on the interval $[-1, 1]$ to prove that for any $x \in [-1, 1]$ we have $e^{ax} \leq \cosh a + x \sinh a$.
(ii) Prove that $t! \geq (t/e)^t$.

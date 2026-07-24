# Chapter 1 — Martingales in discrete time
*(PDF pages 9–40; book pages 3–34)*

### PDF page 9 (book page 3)

# Chapter 1

# Martingales in discrete time

A martingale is a mathematical model of a fair game. To understand the definition, we need to define *conditional expectation*. The concept of conditional expectation will permeate this book.

**1.1 Conditional expectation**

If $X$ is a random variable, then its expectation, $\mathbb{E}[X]$ can be thought of as the best guess for $X$ given no information about the result of the trial. A conditional expectation can be considered as the best guess given some but not total information.

Let $X_1, X_2, \ldots$ be random variables which we think of as a time series with the data arriving one at a time. At time $n$ we have viewed the values $X_1, \ldots, X_n$. If $Y$ is another random variable, then $E(Y \mid X_1, \ldots, X_n)$ is the best guess for $Y$ given $X_1, \ldots, X_n$. We will assume that $Y$ is an *integrable* random variable which means $\mathbb{E}[|Y|] < \infty$. To save some space we will write $\mathcal{F}_n$ for "the information contained in $X_1, \ldots, X_n$" and $E[Y \mid \mathcal{F}_n]$ for $E[Y \mid X_1, \ldots, X_n]$. We view $\mathcal{F}_0$ as no information. The best guess should satisfy the following properties.

- If we have no information, then the best guess is the expected value. In other words, $E[Y \mid \mathcal{F}_0] = \mathbb{E}[Y]$.

- The conditional expectation $E[Y \mid \mathcal{F}_n]$ should only use the information available at time $n$. In other words, it should be a function of

### PDF page 10 (book page 4)

$$ X_1, \ldots, X_n, $$
$$ E[Y \mid \mathcal{F}_n] = \phi(X_1, \ldots, X_n). $$

We say that $E[Y \mid \mathcal{F}_n]$ is $\mathcal{F}_n$-*measurable*.

---

> The definitions in the last paragraph are certainly vague. We can use measure theory to be precise. We assume that the random variables $Y, X_1, X_2, \ldots$ are defined on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$. Here $\mathcal{F}$ is a $\sigma$-*algebra* or $\sigma$-*field* of subsets of $\Omega$, that is, a collection of subsets satisfying
>
> - $\emptyset \in \mathcal{F}$;
> - $A \in \mathcal{F}$ implies that $\Omega \setminus A \in \mathcal{F}$;
> - $A_1, A_2, \ldots \in \mathcal{F}$ implies that $\bigcup_{n=1}^{\infty} A_n \in \mathcal{F}$.
>
> The information $\mathcal{F}_n$ is the smallest sub $\sigma$-algebra $\mathcal{G}$ of $\mathcal{F}$ such that $X_1, \ldots, X_n$ are $\mathcal{G}$-measurable. The latter statement means that for all $t \in \mathbb{R}$, the event $\{X_j \leq t\} \in \mathcal{F}_n$. The "no information" $\sigma$-algebra $\mathcal{F}_0$ is the trivial $\sigma$-algebra containing only $\emptyset$ and $\Omega$.

---

The definition of conditional expectation is a little tricky, so let us try to motivate it by considering an example from undergraduate probability courses. Suppose that $(X, Y)$ have a joint density

$$ f(x, y), \quad 0 < x, y < \infty, $$

with marginal densities

$$ f(x) = \int_{-\infty}^{\infty} f(x, y) \, dy, \quad g(y) = \int_{-\infty}^{\infty} f(x, y) \, dx. $$

The conditional density $f(y|x)$ is defined by

$$ f(y|x) = \frac{f(x, y)}{f(x)}. $$

This is well defined provided that $f(x) > 0$, and if $f(x) = 0$, then $x$ is an "impossible" value for $X$ to take. We can write

$$ \mathbb{E}[Y \mid X = x] = \int_{-\infty}^{\infty} y \, f(y \mid x) \, dy. $$

### PDF page 11 (book page 5)

We can use this as the definition of conditional expectation in this case,

$$ E[Y \mid X] = \int_{-\infty}^{\infty} y \, f(y \mid X) \, dy = \frac{\int_{-\infty}^{\infty} y \, f(X, y) \, dy}{f(X)}. $$

Note that $E[Y \mid X]$ is a random variable which is determined by the value of the random variable $X$. Since it is a random variable, we can take its expectation

$$
\begin{aligned}
\mathbb{E}\left[E[Y \mid X]\right] &= \int_{-\infty}^{\infty} \mathbb{E}[Y \mid X = x] \, f(x) \, dx \\
&= \int_{-\infty}^{\infty} \left[ \int_{-\infty}^{\infty} y \, f(y \mid x) \, dy \right] f(x) \, dx \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} y \, f(x, y) \, dy \, dx \\
&= \mathbb{E}[Y].
\end{aligned}
$$

This calculation illustrates a basic property of conditional expectation. Suppose we are interested in the value of a random variable $Y$ and we are going to be given data $X_1, \ldots, X_n$. Once we observe the data, we make our best prediction $E[Y \mid X_1, \ldots, X_n]$. If we average our best prediction given $X_1, \ldots, X_n$ over all the possible values of $X_1, \ldots, X_n$, we get the best prediction of $Y$. In other words,

$$ \mathbb{E}[Y] = \mathbb{E}\left[E[Y \mid \mathcal{F}_n]\right]. $$

More generally, suppose that $A$ is an $\mathcal{F}_n$-measurable event, that is to say, if we observe the data $X_1, \ldots, X_n$, then we know whether or not $A$ has occurred. An example of an $\mathcal{F}_4$-measurable event would be

$$ A = \{X_1 \geq X_2, X_4 < 4\}. $$

Let $1_A$ denote the *indicator function* (or *indicator random variable*) associated to the event $A$,

$$ 1_A = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{if } A \text{ does not occur} \end{cases}. $$

Using similar reasoning, we can see that if $A$ is $\mathcal{F}_n$-measurable, then

$$ \mathbb{E}\left[Y \, 1_A\right] = \mathbb{E}\left[E[Y \mid \mathcal{F}_n] \, 1_A\right]. $$

### PDF page 12 (book page 6)

At this point, we have not derived this relation mathematically; in fact, we have not even defined the conditional expectation. Instead, we will use this reasoning to motivate the following definition.

**Definition** The *conditional expectation* $E[Y \mid \mathcal{F}_n]$ is the unique random variable satisfying the following.

- $E[Y \mid \mathcal{F}_n]$ is $\mathcal{F}_n$-measurable.
- For every $\mathcal{F}_n$-measurable event $A$,

$$ \mathbb{E}\left[E[Y \mid \mathcal{F}_n] \, 1_A\right] = \mathbb{E}\left[Y \, 1_A\right]. $$

We have used different fonts for the $E$ of conditional expectation and the $\mathbb{E}$ of usual expectation in order to emphasize that the conditional expectation is a random variable. However, most authors use the same font for both leaving it up to the reader to determine which is being referred to.

---

> Suppose $(\Omega, \mathcal{F}, \mathbb{P})$ is a probability space and $Y$ is an integrable random variable. Suppose $\mathcal{G}$ is a sub $\sigma$-algebra of $\mathcal{F}$. Then $E[Y \mid \mathcal{G}]$ is defined to be the unique (up to an event of measure zero) $\mathcal{G}$-measurable random variable such that if $A \in \mathcal{G}$,
>
> $$ \mathbb{E}\left[Y \, 1_A\right] = \mathbb{E}\left[E[Y \mid \mathcal{G}] \, 1_A\right]. $$
>
> Uniqueness follows from the fact that if $Z_1, Z_2$ are $\mathcal{G}$-measurable random variables with
> $$ \mathbb{E}\left[Z_1 \, 1_A\right] = \mathbb{E}\left[Z_2 \, 1_A\right] $$
> for all $A \in \mathcal{G}$, then $\mathbb{P}\{Z_1 \neq Z_2\} = 0$. Existence of the conditional expectation can be deduced from the Radon-Nikodym theorem. Let $\mu(A) = \mathbb{E}\left[Y 1_A\right]$. Then $\mu$ is a (signed) measure on $(\Omega, \mathcal{G}, \mathbb{P})$ with $\mu \ll \mathbb{P}$, and hence there exists an $L^1$ random variable $Z$ with $\mu(A) = \mathbb{E}\left[Z 1_A\right]$ for all $A \in \mathcal{G}$.

---

Although the definition does not give an immediate way to calculate the conditional expectation, in many cases one can compute it. We will give a number of properties of the conditional expectation most of which follow quickly from the definition.

### PDF page 13 (book page 7)

**Proposition 1.1.1.** *Suppose $X_1, X_2, \ldots$ is a sequence of random variables and $\mathcal{F}_n$ denotes the information at time $n$. The conditional expectation $E[Y \mid \mathcal{F}_n]$ satisfies the following properties.*

- *If $Y$ is $\mathcal{F}_n$-measurable, then $E[Y \mid \mathcal{F}_n] = Y$.*

- *If $A$ is an $\mathcal{F}_n$-measurable event, then $\mathbb{E}\left[E[Y \mid \mathcal{F}_n]\, 1_A\right] = \mathbb{E}\left[Y\, 1_A\right]$. In particular,*
$$ \mathbb{E}\left[E[Y \mid \mathcal{F}_n]\right] = \mathbb{E}[Y]. $$

- *Suppose $X_1, \ldots, X_n$ are independent of $Y$. Then $\mathcal{F}_n$ contains no useful information about $Y$ and hence*
$$ E[Y \mid \mathcal{F}_n] = \mathbb{E}[Y]. $$

- **Linearity**. *If $Y, Z$ are random variables and $a, b$ are constants, then*
$$ E[aY + bZ \mid \mathcal{F}_n] = a\, E[Y \mid \mathcal{F}_n] + b\, E[Z \mid \mathcal{F}_n]. \tag{1.1} $$

- **Projection or Tower Property**. *If $m < n$, then*
$$ E\left[\, E[Y \mid \mathcal{F}_n] \mid \mathcal{F}_m \,\right] = E[Y \mid \mathcal{F}_m]. \tag{1.2} $$

- *If $Z$ is an $\mathcal{F}_n$-measurable random variable, then when conditioning with respect to $\mathcal{F}_n$, $Z$ acts like a constant,*
$$ E[YZ \mid \mathcal{F}_n] = Z\, E[Y \mid \mathcal{F}_n]. \tag{1.3} $$

---

The proof of this proposition is not very difficult given our choice of definition for the conditional expectation. We will discuss only a couple of cases here, leaving the rest for the reader. To prove the linearity property, we know that $a\, E[Y \mid \mathcal{F}_n] + b\, E[Z \mid \mathcal{F}_n]$ is an $\mathcal{F}_n$-measurable random variable. Also if $A \in \mathcal{F}_n$, then linearity of expectation implies that

$$
\begin{aligned}
\mathbb{E}\left[1_A \left(a\, E[Y \mid \mathcal{F}_n] + b\, E[Z \mid \mathcal{F}_n]\right)\right] \\
= \quad & a\mathbb{E}\left[1_A\, E[Y \mid \mathcal{F}_n]\right] + b\, \mathbb{E}\left[1_A\, E[Z \mid \mathcal{F}_n]\right] \\
= \quad & a\mathbb{E}\left[1_A\, Y\right] + b\mathbb{E}\left[1_A\, Z\right] \\
= \quad & \mathbb{E}\left[1_A\left(aY + bZ\right)\right].
\end{aligned}
$$

### PDF page 14 (book page 8)

Uniqueness of the conditional expectation then implies (1.1).

We first show the "constants rule" (1.3) for $Z = 1_A$, $A \in \mathcal{F}_n$, as follows. If $B \in \mathcal{F}_n$, then $A \cap B \in \mathcal{F}_n$ and

$$ \mathbb{E}\left[1_B\, E(YZ \mid \mathcal{F}_n)\right] = \mathbb{E}\left[1_B\, E(1_A Y \mid \mathcal{F}_n)\right] $$

$$ = \mathbb{E}\left[1_B\, 1_A\, Y\right] = \mathbb{E}\left[1_{A \cap B}Y\right] = \mathbb{E}\left[1_{A \cap B}E(Y \mid \mathcal{F}_n)\right] $$

$$ = \mathbb{E}\left[1_B\, 1_A\, E(Y \mid \mathcal{F}_n)\right] = \mathbb{E}\left[1_B\, Z\, E(Y \mid \mathcal{F}_n)\right]. $$

Hence $E(YZ \mid \mathcal{F}_n) = Z\, E(Y \mid \mathcal{F}_n)$ by definition. Using linearity, the rule holds for simple random variables of the form

$$ Z = \sum_{j=1}^{n} a_j\, 1_{A_j}, \quad A_j \in \mathcal{F}_n. $$

We can then prove it for nonnegative $Y$ by approximating from below by nonnegative simple random variables and using the monotone convergence theorem, and then for general $Y$ by writing $Y = Y^+ - Y^-$. These are standard techniques in Lebesgue integration theory.

---

**Example 1.1.1.** Suppose that $X_1, X_2, \ldots$ are independent random variables with $\mathbb{E}[X_j] = \mu$ for each $j$. Let $S_n = X_1 + \cdots + X_n$, and let $\mathcal{F}_n$ denote the information contained in $X_1, \ldots, X_n$. Then if $m < n$,

$$
\begin{aligned}
E[S_n \mid \mathcal{F}_m] \quad &= \quad E[S_m \mid \mathcal{F}_m] + E[S_n - S_m \mid \mathcal{F}_m] \\
&= \quad S_m + \mathbb{E}[S_n - S_m] \\
&= \quad S_m + \mu\, (n - m).
\end{aligned}
$$

**Example 1.1.2.** In the same setup as Example 1.1.1 suppose that $\mu = 0$ and $\mathbb{E}[X_j^2] = \sigma^2$ for each $j$. Then if $m < n$,

$$
\begin{aligned}
E[S_n^2 \mid \mathcal{F}_m] \quad &= \quad E\left([S_m + (S_n - S_m)]^2 \mid \mathcal{F}_m\right) \\
&= \quad E[S_m^2 \mid \mathcal{F}_m] + 2\, E[S_m(S_n - S_m) \mid \mathcal{F}_m] \\
&\qquad + E[(S_n - S_m)^2 \mid \mathcal{F}_m].
\end{aligned}
$$

Since $S_m$ is $\mathcal{F}_m$-measurable and $S_n - S_m$ is independent of $\mathcal{F}_m$,

$$ E[S_m^2 \mid \mathcal{F}_m] = S_m^2, $$

### PDF page 15 (book page 9)

$$ E[S_m(S_n - S_m) \mid \mathcal{F}_m] = S_m\, E[S_n - S_m \mid \mathcal{F}_m] = S_m\, \mathbb{E}[S_n - S_m] = 0, $$

$$ E[(S_n - S_m)^2 \mid \mathcal{F}_m] = \mathbb{E}[(S_n - S_m)^2] = \mathrm{Var}(S_n - S_m) = \sigma^2\, (n - m), $$

and hence,

$$ E[S_n^2 \mid \mathcal{F}_m] = S_m^2 + \sigma^2\, (n - m). $$

**Example 1.1.3.** In the same setup as Example 1.1.1, let us also assume that $X_1, X_2, \ldots$ are identically distributed. We will compute $E[X_1 \mid S_n]$. Note that the information contained in the one data point $S_n$ is less than the information contained in $X_1, \ldots, X_n$. However, since the random variables are identically distributed, it must be the case that

$$ E[X_1 \mid S_n] = E[X_2 \mid S_n] = \cdots = E[X_n \mid S_n]. $$

Linearity implies that

$$ n\, E[X_1 \mid S_n] = \sum_{j=1}^{n} E[X_j \mid S_n] = E[X_1 + \cdots + X_n \mid S_n] = E[S_n \mid S_n] = S_n. $$

Therefore,

$$ E[X_1 \mid S_n] = \frac{S_n}{n}. $$

It may be at first surprising that the answer does not depend on $\mathbb{E}[X_1]$.

**Definition** If $X_1, X_2, \ldots$ is a sequence of random variables, then the associated (discrete time) *filtration* is the collection $\{\mathcal{F}_n\}$ where $\mathcal{F}_n$ denotes the information in $X_1, \ldots, X_n$.

One assumption in the definition of a filtration, which may sometimes not reflect reality, is that information is never lost. If $m < n$, then everything known at time $m$ is still known at time $n$. Sometimes a filtration is given starting at time $n = 1$ and sometimes starting at $n = 0$. If it starts at time $n = 1$, we define $\mathcal{F}_0$ to be "no information".

---

More generally, a *(discrete time) filtration* $\{\mathcal{F}_n\}$ is an increasing sequence of $\sigma$-algebras.

---

### PDF page 16 (book page 10)

**1.2 Martingales**

A martingale is a model of a fair game. Suppose $X_1, X_2, \ldots$ is a sequence of random variables to which we associate the filtration $\{\mathcal{F}_n\}$ where $\mathcal{F}_n$ is the information contained in $X_1, \ldots, X_n$.

**Definition** A sequence of random variables $M_0, M_1, \ldots$ is called a *martingale with respect to the filtration* $\{\mathcal{F}_n\}$ if:

- For each $n$, $M_n$ is an $\mathcal{F}_n$-measurable random variable with $\mathbb{E}[|M_n|] < \infty$.

- If $m < n$, then
$$ E[M_n \mid \mathcal{F}_m] = M_m. \tag{1.4} $$

We can also write (1.4) as
$$ E[M_n - M_m \mid \mathcal{F}_m] = 0. $$

If we think of $M_n$ as the winnings of a game, then this implies that no matter what has happened up to time $m$, the expected winnings in the next $n - m$ games is 0. Sometimes one just says "$M_0, M_1, \ldots$ is a martingale" without reference to the filtration. In this case, the assumed filtration is $\mathcal{F}_n$, the information in $M_0, \ldots, M_n$. In order to establish (1.4) it suffices to show for all $n$,
$$ E[M_{n+1} \mid \mathcal{F}_n] = M_n. \tag{1.5} $$

In order to see this, we can use the tower property (1.2) for conditional expectation to see that
$$ E[M_{n+2} \mid \mathcal{F}_n] = E\left[\, E[M_{n+2} \mid \mathcal{F}_{n+1}] \mid \mathcal{F}_n\right] = E[M_{n+1} \mid \mathcal{F}_n] = M_n, $$

and so forth. Also note that if $M_n$ is a martingale, then
$$ \mathbb{E}[M_n] = \mathbb{E}\left[E[M_n \mid \mathcal{F}_0]\right] = \mathbb{E}[M_0]. $$

**Example 1.2.1.** Suppose $X_1, X_2, \ldots$ are independent random variables with $\mathbb{E}[X_j] = 0$ for each $j$. Let $S_0 = 0$ and $S_n = X_1 + \cdots + X_n$. In the last section we showed that if $m < n$, then $E[S_n \mid \mathcal{F}_m] = S_m$. Hence, $S_n$ is a martingale with respect to $\mathcal{F}_n$, the information in $X_1, \ldots, X_n$.

### PDF page 17 (book page 11)

**Example 1.2.2.** Suppose $X_n, S_n, \mathcal{F}_n$ are as in Example 1.2.1 and also assume $\mathrm{Var}[X_j] = \mathbb{E}[X_j^2] = \sigma_j^2 < \infty$. Let
$$ A_n = \sigma_1^2 + \cdots + \sigma_n^2, $$
$$ M_n = S_n^2 - A_n, $$

where $M_0 = 0$. Then $M_n$ is a martingale with respect to $\mathcal{F}_n$. To see this, we compute as in Example 1.1.2,

$$
\begin{aligned}
E[S_{n+1}^2 \mid \mathcal{F}_n] &= E[(S_n + X_{n+1})^2 \mid \mathcal{F}_n] \\
&= E[S_n^2 \mid \mathcal{F}_n] + 2E[S_n X_{n+1} \mid \mathcal{F}_n] + E[X_{n+1}^2 \mid \mathcal{F}_n] \\
&= S_n^2 + 2S_n\, E[X_{n+1} \mid \mathcal{F}_n] + \mathbb{E}[X_{n+1}^2] \\
&= S_n^2 + 2S_n\, \mathbb{E}[X_{n+1}] + \mathbb{E}[X_{n+1}^2] \\
&= S_n^2 + \sigma_{n+1}^2.
\end{aligned}
$$

Therefore,
$$
\begin{aligned}
E[M_{n+1} \mid \mathcal{F}_n] &= E[S_{n+1}^2 - A_{n+1} \mid \mathcal{F}_n] \\
&= S_n^2 + \sigma_{n+1}^2 - (A_n + \sigma_{n+1}^2) = M_n.
\end{aligned}
$$

There are various ways to view a martingale. One can consider $M_n$ as the price of an asset (although we allow negative values of $M_n$) or as the winnings in a game. We can also consider
$$ \Delta M_n = M_n - M_{n-1} $$

as either the change in the asset price or as the amount won in the game at time $n$. Negative values indicate drops in price or money lost in the game. The basic idea of stochastic integration is to allow one to change one's portfolio (in the asset viewpoint) or change one's bet (in the game viewpoint). However, we are not allowed to see the outcome before betting. We make this precise in the next example.

**Example 1.2.3. Discrete stochastic integral.** Suppose that $M_0, M_1, \ldots$ is a martingale with respect to the filtration $\mathcal{F}_n$. For $n \geq 1$, let $\Delta M_n = M_n - M_{n-1}$. Let $B_j$ denote the "bet" on the $j$th game. We allow negative values of $B_j$ which indicate betting that the price will go down or the game

### PDF page 18 (book page 12)

will be lost. Let $W_n$ denote the winnings in this strategy: $W_0 = 0$ and for $n \geq 1$,
$$ W_n = \sum_{j=1}^{n} B_j\, [M_j - M_{j-1}] = \sum_{j=1}^{n} B_j\, \Delta M_j. $$

Let us assume that for each $n$ there is a number $K_n < \infty$ such that $|B_n| \leq K_n$. We also assume that we cannot see the result of $n$th game before betting. This last assumption can be expressed mathematically by saying that $B_n$ is $\mathcal{F}_{n-1}$-measurable. In other words, we can adjust our bet based on how well we have been doing. We claim that under these assumptions, $W_n$ is a martingale with respect to $\mathcal{F}_n$. It is clear that $W_n$ is measurable with respect to $\mathcal{F}_n$, and integrability follows from the estimate

$$
\begin{aligned}
\mathbb{E}[|W_n|] &\leq \sum_{j=1}^{n} \mathbb{E}[|B_j||M_j - M_{j-1}|] \\
&\leq \sum_{j=1}^{n} K_j\, \left(\mathbb{E}[|M_j|] + \mathbb{E}[|M_{j-1}|]\right) < \infty.
\end{aligned}
$$

Also,
$$
\begin{aligned}
E[W_{n+1} \mid \mathcal{F}_n] &= E[W_n + B_{n+1}(M_{n+1} - M_n) \mid \mathcal{F}_n] \\
&= E[W_n \mid \mathcal{F}_n] + E[B_{n+1}(M_{n+1} - M_n) \mid \mathcal{F}_n].
\end{aligned}
$$

Since $W_n$ is $\mathcal{F}_n$-measurable, $E[W_n \mid \mathcal{F}_n] = W_n$. Also, since $B_{n+1}$ is $\mathcal{F}_n$-measurable and $M$ is a martingale,
$$ E[B_{n+1}(M_{n+1} - M_n) \mid \mathcal{F}_n] = B_{n+1}\, E[M_{n+1} - M_n \mid \mathcal{F}_n] = 0. $$

Therefore,
$$ E[W_{n+1} \mid \mathcal{F}_n] = W_n. $$

Example 1.2.3 demonstrates an important aspect of martingales. One cannot change a discrete-time martingale to a game in one's favor with a betting strategy in a finite amount of time. However, the next example shows that if we are allowed an infinite amount of time we can beat a fair game.

**Example 1.2.4. Martingale betting strategy**. Let $X_1, X_2, \ldots$ be independent random variables with
$$ \mathbb{P}\{X_j = 1\} = \mathbb{P}\{X_j = -1\} = \frac{1}{2}. \tag{1.6} $$

### PDF page 19 (book page 13)

We will refer to such random variables as "coin-tossing" random variables where 1 corresponds to heads and $-1$ corresponds to tails. Let $M_0 = 0$, $M_n = X_1 + \cdots + X_n$. We have seen that $M_n$ is a martingale. We will consider the following betting strategy. We start by betting \$1. If we win, we quit; otherwise, we bet \$2 on the next game. If we win the second game, we quit; otherwise we double our bet to \$4 and play. Each time we lose, we double our bet. At the time that we win, we will be ahead \$1. With probability one, we will eventually win the game, so this strategy is a way to beat a fair game. The winnings in this game can be written as

$$ W_n = \sum_{j=1}^{n} B_j \, \Delta M_j = \sum_{j=1}^{n} B_j \, X_j, $$

where the bet $B_1 = 1$ and for $j > 1$,

$$ B_j = 2^{j-1} \text{ if } X_1 = X_2 = \cdots = X_{j-1} = -1, $$

and otherwise $B_j = 0$. This is an example of a discrete stochastic integral as in the previous example, and hence, we know that $W_n$ must be a martingale. In particular, for each $n$, $\mathbb{E}[W_n] = 0$. We can check this directly by noting that $W_n = 1$ unless $X_1 = X_2 = \cdots = X_n = -1$ in which case

$$ W_n = -1 - 2^1 - 2^2 - \cdots - 2^{n-1} = -[2^n - 1]. $$

This last event happens with probability $(1/2)^n$, and hence

$$ \mathbb{E}[W_n] = 1 \cdot [1 - 2^{-n}] - [2^n - 1] \cdot 2^{-n} = 0. $$

However, we will eventually win which means that with probability one

$$ W_\infty = \lim_{n \to \infty} W_n = 1, $$

and

$$ 1 = \mathbb{E}[W_\infty] > \mathbb{E}[W_0] = 0. $$

We have beaten the game (but it takes an infinite amount of time to guarantee it).

If the condition (1.4) is replaced with

$$ E[M_n \mid \mathcal{F}_m] \geq M_m, $$

### PDF page 20 (book page 14)

then the process is called a *submartingale.* If it is replaced with

$$ E[M_n \mid \mathcal{F}_m] \leq M_m, $$

then it is called a *supermartingale.* In other words, games that are always in one's favor are submartingales and games that are always against one are supermartingales. (At most games in Las Vegas, one's winnings give a supermartingale.) Under this definition, a martingale is both a submartingale and a supermartingale. The terminology may seem backwards at first: submartingales get bigger and supermartingales get smaller. The terminology was set to be consistent with the related notion of subharmonic and superharmonic functions. Martingales are related to harmonic functions.

## 1.3 Optional sampling theorem

Suppose $M_0, M_1, M_2, \ldots$ is a martingale with respect to the filtration $\{\mathcal{F}_n\}$. In the last section we discussed the discrete stochastic integral. Here we will consider a particular case of a betting strategy where one bets 1 up to some time and then one bets 0 afterwards. Let $T$ be the "stopping time" for the strategy. Then the winnings at time $t$ is

$$ M_0 + \sum_{j=1}^{n} B_j \, [M_j - M_{j-1}], $$

where $B_j = 1$ if $j \leq T$ and $B_j = 0$ if $j > T$. We can write this as

$$ M_{n \wedge T}, $$

where $n \wedge T$ is shorthand for $\min\{n, T\}$. The time $T$ is random, but it must satisfy the condition that the betting rule is allowable.

**Definition** A nonnegative integer-valued random variable $T$ is a *stopping time* with respect to the filtration $\{\mathcal{F}_n\}$ if for each $n$ the event $\{T = n\}$ is $\mathcal{F}_n$-measurable.

The following theorem is a special case of the discrete stochastic integral. It restates the fact that one cannot beat a martingale in finite time. We call this the *optional sampling theorem*; it is also called the *optional stopping theorem.*

### PDF page 21 (book page 15)

**Theorem 1.3.1** (Optional Sampling Theorem I)**.** *Suppose $T$ is a stopping time and $M_n$ is a martingale with respect to $\{\mathcal{F}_n\}$. Then $Y_n = M_{n \wedge T}$ is a martingale. In particular, for each $n$,*

$$ \mathbb{E}[M_{n \wedge T}] = \mathbb{E}[M_0]. $$

*If $T$ is bounded, that is, if there exists $k < \infty$ such that $\mathbb{P}\{T \leq k\} = 1$, then*

$$ \mathbb{E}[M_T] = \mathbb{E}[M_0]. \tag{1.7} $$

The final conclusion (1.7) of the theorem holds since $\mathbb{E}[M_{n \wedge T}] = \mathbb{E}[M_T]$ for $n \geq k$. What if the stopping time $T$ is not bounded but $\mathbb{P}\{T < \infty\} = 1$? Then, we cannot conclude (1.7) without further assumptions. To see this we need only consider the martingale betting strategy of the previous section. If we define

$$ T = \min\{n : X_n = 1\} = \min\{n : W_n = 1\}, $$

then with probability one $T < \infty$ and $W_T = 1$. Hence,

$$ 1 = \mathbb{E}[W_T] > \mathbb{E}[W_0] = 0. $$

Often one does want to conclude (1.7) for unbounded stopping times, so it is useful to give conditions under which it holds. Let us try to derive the equality and see what conditions we need to impose. First, we will assume that we stop, $\mathbb{P}\{T < \infty\} = 1$, so that $M_T$ makes sense. For every $n < \infty$, we know that

$$ \mathbb{E}[M_0] = \mathbb{E}[M_{n \wedge T}] = \mathbb{E}[M_T] + \mathbb{E}[M_{n \wedge T} - M_T]. $$

If we can show that

$$ \lim_{n \to \infty} \mathbb{E}\left[|M_{n \wedge T} - M_T|\right] = 0, $$

then we have (1.7). The random variable $M_{n \wedge T} - M_T$ is zero if $n \wedge T = T$, and

$$ M_{n \wedge T} - M_T = 1\{T > n\} \, [M_n - M_T]. $$

If $\mathbb{E}[|M_T|] < \infty$, then one can show that

$$ \lim_{n \to \infty} \mathbb{E}\left[|M_T| \, 1\{T > n\}\right] = 0. $$

In the martingale betting strategy example, this term did not cause a problem since $W_T = 1$ and hence $\mathbb{E}[|W_T|] < \infty$.

### PDF page 22 (book page 16)

If $\mathbb{P}\{T < \infty\} = 1$, then the random variables $X_n = |M_T| \, 1\{T > n\}$ converge to zero with probability one. If $\mathbb{E}\left[|M_T|\right] < \infty$, then we can use the dominated convergence theorem to conclude that

$$ \lim_{n \to \infty} \mathbb{E}[X_n] = 0. $$

Finally, in order to conclude (1.7) we will make the hypothesis that the other term acts nicely.

**Theorem 1.3.2** (Optional Sampling Theorem II)**.** *Suppose $T$ is a stopping time and $M_n$ is a martingale with respect to $\{\mathcal{F}_n\}$. Suppose that $\mathbb{P}\{T < \infty\} = 1, \mathbb{E}\left[|M_T|\right] < \infty$, and for each $n$,*

$$ \lim_{n \to \infty} \mathbb{E}\left[|M_n| \, 1\{T > n\}\right] = 0. \tag{1.8} $$

*Then,*

$$ \mathbb{E}\left[M_T\right] = \mathbb{E}\left[M_0\right]. $$

Let us check that the martingale betting strategy does *not* satisfy the conditions of the theorem (it better not since it does not satisfy the conclusion!) In fact, it does not satisfy (1.8). For this strategy, if $T > n$, then we have lost $n$ times and $W_n = 1 - 2^n$. Also, $\mathbb{P}\{T > n\} = 2^{-n}$. Therefore,

$$ \lim_{n \to \infty} \mathbb{E}\left[|W_n| \, 1\{T > n\}\right] = \lim_{n \to \infty} \left(2^n - 1\right) 2^{-n} = 1 \neq 0. $$

Checking condition (1.8) can be difficult in general. We will give one criterion which is useful.

**Theorem 1.3.3** (Optional Sampling Theorem III)**.** *Suppose $T$ is a stopping time and $M_n$ is a martingale with respect to $\{\mathcal{F}_n\}$. Suppose that $\mathbb{P}\{T < \infty\} = 1, \mathbb{E}\left[|M_T|\right] < \infty$, and that there exists $C < \infty$ such that for each $n$,*

$$ \mathbb{E}\left[|M_{n \wedge T}|^2\right] \leq C. \tag{1.9} $$

*Then,*

$$ \mathbb{E}\left[M_T\right] = \mathbb{E}\left[M_0\right]. $$

### PDF page 23 (book page 17)

To prove this theorem, first note that with probability one,

$$ |M_T|^2 = \lim_{n \to \infty} |M_{T \wedge n}|^2 \, 1\{T \leq n\}, $$

and hence by the Hölder inequality and the monotone convergence theorem,

$$ \mathbb{E}\left[|M_T|\right]^2 \leq \mathbb{E}\left[|M_T|^2\right] = \lim_{n \to \infty} \mathbb{E}\left[|M_{T \wedge n}|^2 \, 1\{T \leq n\}\right] \leq C. $$

We need to show that (1.9) implies (1.8). If $b > 0$, then for every $n$,

$$ \mathbb{E}\left[|M_n| \, 1\{|M_n| \geq b, T > n\}\right] \leq \frac{\mathbb{E}[|M_{n \wedge T}|^2]}{b} \leq \frac{C}{b}. $$

Therefore,

$$ \begin{aligned} \mathbb{E}\left[|M_n| \, 1\{T > n\}\right] &= \mathbb{E}\left[|M_n| \, 1\{T > n, |M_n| \geq b\}\right] \\ &\quad + \mathbb{E}\left[|M_n| \, 1\{T > n, |M_n| < b\}\right] \\ &\leq \frac{C}{b} + b \, \mathbb{P}\{T > n\}. \end{aligned} $$

Hence,

$$ \limsup_{n \to \infty} \mathbb{E}\left[|M_n| \, 1\{T > n\}\right] \leq \frac{C}{b} + b \lim_{n \to \infty} \mathbb{P}\{T > n\} = \frac{C}{b}. $$

Since this holds for every $b > 0$ we get (1.8).

**Example 1.3.1. Gambler's ruin for random walk**. Let $X_1, X_2, \ldots$ be independent, coin-tosses as in (1.6) and let

$$ S_n = 1 + X_1 + \cdots + X_n. $$

$S_n$ is called *simple (symmetric) random walk* starting at 1. We have shown that $S_n$ is a martingale. Let $K > 1$ be a positive integer and let $T$ denote the first time $n$ such that $S_n = 0$ or $S_n = K$. Then $M_n = S_{n \wedge T}$ is a martingale. Also $0 \leq M_n \leq K$ for all $n$, so (1.9) is satisfied. We can apply the optional sampling theorem to deduce that

$$ 1 = M_0 = \mathbb{E}[M_T] = 0 \cdot \mathbb{P}\{M_T = 0\} + K \cdot \mathbb{P}\{M_T = K\}. $$

### PDF page 24 (book page 18)

By solving, we get

$$ \mathbb{P}\{M_T = K\} = \frac{1}{K}. $$

This relation is sometimes called the *gambler's ruin estimate* for the random walk. Note that

$$ \lim_{K \to \infty} \mathbb{P}\{M_T = K\} = 0. $$

If we consider 1 to be the starting stake of a gambler and $K$ to be the amount held by a casino, this shows that with a fair game, the gambler will almost surely lose. If $\tau = \min\{n : S_n = 0\}$, then the last equality implies that $\mathbb{P}\{\tau < \infty\} = 1$. The property that the walk always returns to the origin is called *recurrence*.

**Example 1.3.2.** Let $S_n = X_1 + \cdots + X_n$ be simple random walk starting at 0. We have seen that

$$ M_n = S_n^2 - n $$

is a martingale. Let $J, K$ be positive integers and let

$$ T = \min\{n : S_n = -J \text{ or } S_n = K\}. $$

As in Example 1.3.1, we have

$$ 0 = \mathbb{E}[S_0] = \mathbb{E}[S_T] = [1 - \mathbb{P}\{S_T = K\}] \cdot (-J) + \mathbb{P}\{S_T = K\} \cdot K, $$

and solving gives

$$ \mathbb{P}\{S_T = K\} = \frac{J}{J + K}. $$

In Exercise 1.13 it is shown that there exists $C < \infty$ such that for all $n$ $\mathbb{E}[M_{n \wedge T}^2] \leq C$. Hence we can use Theorem 1.3.3 to conclude that

$$ 0 = \mathbb{E}[M_0] = \mathbb{E}\left[M_T\right] = \mathbb{E}\left[S_T^2\right] - \mathbb{E}\left[T\right]. $$

Moreover,

$$ \begin{aligned} \mathbb{E}\left[S_T^2\right] &= J^2 \, \mathbb{P}\{S_T = -J\} + K^2 \, \mathbb{P}\{S_T = K\} \\ &= J^2 \, \frac{K}{J + K} + K^2 \, \frac{J}{J + K} = JK. \end{aligned} $$

Therefore,

$$ \mathbb{E}[T] = \mathbb{E}\left[S_T^2\right] = JK. $$

In particular, the expected amount of time for the random walker starting at the origin to get distance $K$ from the origin is $K^2$.

### PDF page 25 (book page 19)

**Example 1.3.3.** As in Example 1.3.2, let $S_n = X_1 + \cdots + X_n$ be simple random walk starting at 0. Let

$$ T = \min\{n : S_n = 1\}, \quad T_J = \min\{n : S_n = 1 \text{ or } S_n = -J\}. $$

Note that $T = \lim_{J \to \infty} T_J$ and

$$ \mathbb{P}\{T = \infty\} = \lim_{J \to \infty} \mathbb{P}\left\{S_{T_J} = -J\right\} = \lim_{J \to \infty} \frac{1}{J + 1} = 0. $$

Therefore, $\mathbb{P}\{T < \infty\} = 1$, although Example 1.3.2 shows that for every $J$,

$$ \mathbb{E}[T] \geq \mathbb{E}\left[T_J\right] = J, $$

and hence $\mathbb{E}[T] = \infty$. Also, $S_T = 1$, so we do not have $\mathbb{E}[S_0] = \mathbb{E}[S_T]$. From this we can see that (1.8) and (1.9) are not satisfied by this example.

## 1.4 Martingale convergence theorem

The martingale convergence theorem describes the behavior of a martingale $M_n$ as $n \to \infty$.

**Theorem 1.4.1** (Martingale Convergence Theorem)**.** *Suppose $M_n$ is a martingale with respect to $\{\mathcal{F}_n\}$ and there exists $C < \infty$ such that $\mathbb{E}\left[|M_n|\right] \leq C$ for all $n$. Then there exists a random variable $M_\infty$ such that with probability one*

$$ \lim_{n \to \infty} M_n = M_\infty. $$

It does *not* follow from the theorem that $\mathbb{E}[M_\infty] = \mathbb{E}[M_0]$. For example, the martingale betting strategy satisfies the conditions of the theorem since

$$ \mathbb{E}\left[|W_n|\right] = (1 - 2^{-n}) \cdot 1 + (2^n - 1) \cdot 2^{-n} \leq 2. $$

However, $W_\infty = 1$ and $W_0 = 0$.

---

We will prove the martingale convergence theorem. The proof uses a well-known financial strategy — buy low, sell high. Suppose $M_0, M_1, \ldots$ is a martingale such that

$$ \mathbb{E}\left[|M_n|\right] \leq C < \infty, $$

### PDF page 26 (book page 20)

for all $n$. Suppose $a < b$ are real numbers. We will show that it is impossible for the martingale to fluctuate infinitely often below $a$ and above $b$. Define a sequence of stopping times by

$$ S_1 = \min\{n : M_n \leq a\}, \quad T_1 = \min\{n > S_1 : M_n \geq b\}, $$

and for $j > 1$,

$$ S_j = \min\{n > T_{j-1} : M_n \leq a\}, $$

$$ T_j = \min\{n > S_j : M_n \geq b\}. $$

We set up the discrete stochastic integral

$$ W_n = \sum_{k=0}^{n} B_k \left[M_k - M_{k-1}\right], $$

with $B_n = 0$ if $n - 1 < S_1$ and

$$ B_n = 1 \quad \text{if } S_j \leq n - 1 < T_j, $$

$$ B_n = 0 \quad \text{if } T_j \leq n - 1 < S_{j+1}. $$

In other words, every time the "price" drops below $a$ we buy a unit of the asset and hold onto it until the price goes above $b$ at which time we sell. Let $U_n$ denote the number of times by time $n$ that we have seen a fluctuation; that is,

$$ U_n = j \quad \text{if} \quad T_j < n \leq T_{j+1}. $$

We call $U_n$ the number of *upcrossings* by time $n$. Every upcrossing results in a profit of at least $b - a$. From this we see that

$$ W_n \geq U_n (b - a) + (M_n - a). $$

The term $a - M_n$ represents a possible loss caused by holding a share of the asset at the current time. Since $W_n$ is a martingale, we know that $\mathbb{E}[W_n] = \mathbb{E}[W_0] = 0$, and hence

$$ \mathbb{E}[U_n] \leq \frac{\mathbb{E}[a - M_n]}{b - a} \leq \frac{|a| + \mathbb{E}[|M_n|]}{b - a} \leq \frac{|a| + C}{b - a}. $$

This holds for every $n$, and hence

$$ \mathbb{E}[U_\infty] \leq \frac{|a| + C}{b - a} < \infty. $$

### PDF page 27 (book page 21)

In particular with probability one, $U_\infty < \infty$, and hence there are only a finite number of fluctuations. We now allow $a, b$ to run over all rational numbers to see that with probability one,

$$ \liminf_{n \to \infty} M_n = \limsup_{n \to \infty} M_n. $$

Therefore, the limit

$$ M_\infty = \lim_{n \to \infty} M_n $$

exists. We have not yet ruled out the possibility that $M_\infty$ is $\pm\infty$, but it is not difficult to see that if this occurred with positive probability, then $\mathbb{E}[|M_n|]$ would not be uniformly bounded.

---

To illustrate the martingale convergence theorem, we will consider another example of a martingale called *Polya's urn*. Suppose we have an urn with red and green balls. At time $n = 0$, we start with one red ball and one green ball. At each positive integer time we choose a ball at random from the urn (with each ball equally likely to be chosen), look at the color of the ball, and then put the ball back in with another ball of the same color. Let $R_n, G_n$ denote the number of red and green balls in the urn after the draw at time $n$ so that

$$ R_0 = G_0 = 1, \quad R_n + G_n = n + 2, $$

and let

$$ M_n = \frac{R_n}{R_n + G_n} = \frac{R_n}{n + 2} $$

be the fraction of red balls at this time. Let $\mathcal{F}_n$ denote the information in the data $M_1, \ldots, M_n$, which one can check is the same as the information in $R_1, R_2, \ldots, R_n$. Note that the probability that a red ball is chosen at time $n$ depends only on the number (or fraction) of red balls in the urn before choosing. It does not depend on what order the red and green balls were put in. This is an example of the *Markov property*. This concept will appear a number of times for us, so let us define it.

**Definition** A discrete time process $Y_0, Y_1, Y_2, \ldots$ is called *Markov* if for each $n$, the conditional distribution of

$$ Y_{n+1}, Y_{n+2}, \ldots $$

### PDF page 28 (book page 22)

given $Y_0, Y_1, \ldots, Y_n$ is the same as the conditional distribution given $Y_n$. In other words, the only thing about the past and present that is useful for predicting the future is the current value of the process.

We can describe the rule of Polya's urn by

$$ \mathbb{P}\{R_{n+1} = R_n + 1 \mid \mathcal{F}_n\} = 1 - \mathbb{P}\{R_{n+1} = R_n \mid \mathcal{F}_n\} = $$

$$ \mathbb{P}\{R_{n+1} = R_n + 1 \mid M_n\} = \frac{R_n}{n + 2} = M_n. $$

We claim that $M_n$ is a martingale with respect to $\mathcal{F}_n$. To check this,

$$ \begin{aligned} E\left[M_{n+1} \mid \mathcal{F}_n\right] &= E\left[M_{n+1} \mid M_n\right] \\ &= M_n \frac{R_n + 1}{n + 3} + [1 - M_n] \frac{R_n}{n + 3} \\ &= \frac{R_n(R_n + 1)}{(n + 2)(n + 3)} + \frac{(n + 2 - R_n)R_n}{(n + 2)(n + 3)} \\ &= \frac{R_n(n + 3)}{(n + 2)(n + 3)} = M_n. \end{aligned} $$

Since $\mathbb{E}[|M_n|] = \mathbb{E}[M_n] = \mathbb{E}[M_0] = 1/2$, this martingale satisfies the conditions of the martingale convergence theorem. (In fact, the same argument shows that every martingale that stays nonnegative satisfies the conditions.) Hence, there exists a random variable $M_\infty$ such that with probability one,

$$ \lim_{n\to\infty} M_n = M_\infty. $$

It turns out that the random variable $M_n$ is really random in the sense that it has a nontrivial distribution. In Exercise 1.11 you will show that for each $n$, the distribution of $M_n$ is uniform on

$$ \left\{ \frac{1}{n + 2}, \frac{2}{n + 2}, \ldots, \frac{n + 1}{n + 2} \right\}, $$

and from this it is not hard to see that $M_\infty$ has a uniform distribution on $[0, 1]$. You will also be asked to simulate this process to see what happens. There is a lot of randomness in the first few draws to see what fraction of red balls the urn will settle down to. However, for large $n$ this ratio changes very little; for example, the ratio after 2000 draws is very close to the ratio after 4000 draws.

### PDF page 29 (book page 23)

While Polya's urn seems like a toy model, it arises in a number of places. We will give an example from Bayesian statistics. Suppose that we perform independent trials of an experiment where the probability of success for each experiment is $\theta$ (such trials are called *Bernoulli trials*). Suppose that we do not know the value of $\theta$, but want to try to deduce it by observing trials. Let $X_1, X_2, \ldots$ be independent random variables with

$$ \mathbb{P}\{X_j = 1\} = 1 - \mathbb{P}\{X_j = 0\} = \theta. $$

The (strong) law of large numbers implies that with probability one,

$$ \lim_{n\to\infty} \frac{X_1 + \cdots + X_n}{n} = \theta. \tag{1.10} $$

Hence, if were able to observe infinitely many trials, we could deduce $\theta$ exactly.

Clearly, we cannot deduce $\theta$ with 100% assurance if we see only a finite number of trials. Indeed, if $0 < \theta < 1$, there is always a chance that the first $n$ trials will all be failures and there is a chance they will all be successes. The Bayesian approach to statistics is to assume that $\theta$ is a random variable with a certain *prior distribution*. As we observe the data we update to a *posterior distribution*. We will assume we know nothing initially about the value and choose the prior distribution to the uniform distribution on $[0, 1]$ with density

$$ f_0(\theta) = 1, \quad 0 < \theta < 1. $$

Suppose that after observing $n$ trials, we have had $S_n = X_1 + \cdots + X_n$ successes. If we know $\theta$, then the distribution of $S_n$ is binomial,

$$ \mathbb{P}\{S_n = k \mid \theta\} = \binom{n}{k} \theta^k (1 - \theta)^{n-k}. $$

We use a form of the Bayes rule to update the density

$$ f_{n,k}(\theta) := f_n(\theta \mid S_n = k) = \frac{\mathbb{P}\{S_n = k \mid \theta\}}{\int_0^1 \mathbb{P}\{S_n = k \mid x\} \, dx} = C_{n,k} \, \theta^k (1 - \theta)^{n-k}, $$

where $C_{n,k}$ is the appropriate constant so that $f_{n,k}$ is a probability density. This is the *beta density* with parameters $k+1$ and $n-k+1$. The probability of

### PDF page 30 (book page 24)

a success on the $(n+1)$st trial given that $S_n = k$ is the conditional expectation of $\theta$ given $S_n = k$. A little computation which we omit shows that

$$ \mathbb{E}[\theta \mid S_n = k] = \int_0^1 \theta \, f_{n,k}(\theta) \, d\theta = \frac{k + 1}{n + 2} = \frac{S_n + 1}{n + 2}. $$

These are exactly the transition probabilities for Polya's urn if we view $S_n+1$ as the number of red balls in the urn ($S_n$ is the number of red balls added to the urn). The martingale convergence theorem can now be viewed as the law of large numbers (1.10) for $\theta$. Even though we do not initially know the value of $\theta$ (and hence treat it as a random variable) we know that the conditional value of $\theta$ given $\mathcal{F}_n$ approaches $\theta$.

**Example 1.4.1.** We end with a simple example where the conditions of the martingale convergence theorem do not apply. Let $S_n = X_1 + \cdots + X_n$ be simple symmetric random walk starting at the origin as in the previous section. Then one can easily see that $\mathbb{E}[|S_n|] \to \infty$. For this example, with probability one

$$ \limsup_{n\to\infty} S_n = \infty, $$

$$ \liminf_{n\to\infty} S_n = -\infty. $$

## 1.5 Square integrable martingales

**Definition** A martingale $M_n$ is called *square integrable* if for each $n$, $\mathbb{E}\left[M_n^2\right] < \infty$.

Note that this condition is not as strong as (1.9). We do not require that there exists a $C < \infty$ such that $\mathbb{E}\left[M_n^2\right] \le C$ for each $n$. Random variables $X, Y$ are *orthogonal* if $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$. Independent random variables are orthogonal, but orthogonal random variables need not be independent. If $X_1, \ldots, X_n$ are pairwise orthogonal random variables with mean zero, then $\mathbb{E}[X_j X_k] = 0$ for $j \ne k$ and by expanding the square we can see that

$$ \mathbb{E}\left[(X_1 + \cdots + X_n)^2\right] = \sum_{j=1}^{n} \mathbb{E}[X_j^2]. $$

This can be thought of as a generalization of the Pythagorean theorem $a^2 + b^2 = c^2$ for right triangles. The increments of a martingale are not necessarily

### PDF page 31 (book page 25)

independent, but for square integrable martingales they are orthogonal as we now show.

**Proposition 1.5.1.** *Suppose that $M_n$ is a square integrable martingale with respect to $\{\mathcal{F}_n\}$. Then if $m < n$,*

$$\mathbb{E}\left[(M_{n+1} - M_n)(M_{m+1} - M_m)\right] = 0.$$

*Moreover, for all $n$,*

$$\mathbb{E}[M_n^2] = \mathbb{E}[M_0^2] + \sum_{j=1}^{n} \mathbb{E}\left[(M_j - M_{j-1})^2\right].$$

*Proof.* If $m < n$, then $M_{m+1} - M_m$ is $\mathcal{F}_n$-measurable, and hence

$$E\left[(M_{n+1} - M_n)(M_{m+1} - M_m) \mid \mathcal{F}_n\right]$$
$$= (M_{m+1} - M_m)\, E[M_{n+1} - M_n \mid \mathcal{F}_n] = 0.$$

Hence

$$\mathbb{E}\left[(M_{n+1} - M_n)(M_{m+1} - M_m)\right]$$
$$= \mathbb{E}\left[E\left[(M_{n+1} - M_n)(M_{m+1} - M_m) \mid \mathcal{F}_n\right]\right] = 0.$$

Also, if we set $M_{-1} = 0$,

$$
\begin{aligned}
M_n^2 &= \left[M_0 + \sum_{j=1}^{n}(M_j - M_{j-1})\right]^2 \\
&= M_0^2 + \sum_{j=1}^{n}(M_j - M_{j-1})^2 + \sum_{j \neq k}(M_j - M_{j-1})(M_k - M_{k-1}).
\end{aligned}
$$

Taking expectations of both sides gives the second conclusion. $\square$

---

The natural place to discuss the role of orthogonality in the study of square integrable martingales is $L^2 = L^2(\Omega, \mathcal{F}, \mathbb{P})$, the space of square integrable random variables. This is a (real) Hilbert space under the inner product

$$(X, Y) = \mathbb{E}[XY].$$

### PDF page 32 (book page 26)

Two mean zero random variables are orthogonal if and only if $(X, Y) = 0$. The conditional expectation has a nice interpretation in $L^2$. Suppose $Y$ is a square integrable random variable and $\mathcal{G}$ is a sub-$\sigma$-algebra. Then $L^2(\Omega, \mathcal{G}, \mathbb{P})$ is a closed subspace of $L^2(\Omega, \mathcal{F}, \mathbb{P})$ and the conditional expectation $\mathbb{E}[Y \mid \mathcal{G}]$ is the same as the Hilbert space projection onto the subspace. It can also be characterized as the $\mathcal{G}$-measurable random variable $Z$ that minimizes the mean-squared error

$$\mathbb{E}[(Y - Z)^2].$$

The reason $L^2$ rather than $L^p$ for other values of $p$ is so useful is because of the inner product which gives the idea of orthogonality.

---

## 1.6 Integrals with respect to random walk

Suppose that $X_1, X_2, \ldots$ are independent, identically distributed random variables with mean zero and variance $\sigma^2$. The two main examples we will use are:

- Binomial or coin-tossing random variables,

$$\mathbb{P}\{X_j = 1\} = \mathbb{P}\{X_j = -1\} = \frac{1}{2},$$

  in which case $\sigma^2 = 1$.

- Normal increments where $X_j \sim N(0, \sigma^2)$. We write $Z \sim N(\mu, \sigma^2)$ if $Z$ has a normal distribution with mean $\mu$ and variance $\sigma^2$.

Let $S_n = X_1 + \cdots + X_n$ and let $\{\mathcal{F}_n\}$ denote the filtration generated by $X_1, \ldots, X_n$. A sequence of random variables $J_1, J_2, \ldots$ is called *predictable (with respect to $\{\mathcal{F}_n\}$)* if for each $n$, $J_n$ is $\mathcal{F}_{n-1}$-measurable. Recall that this is the condition that makes $J_n$ allowable "bets" on the martingale in the sense of the discrete stochastic integral.

Suppose $J_1, J_2, \ldots$ is a predictable sequence with $\mathbb{E}[J_n^2] < \infty$ for each $n$. The integral of $J_n$ with respect to $S_n$ is defined by

$$Z_n = \sum_{j=1}^{n} J_j\, X_j = \sum_{j=1}^{n} J_j\, \Delta S_j.$$

There are three important properties that the integral satisfies.

### PDF page 33 (book page 27)

- **Martingale property**. The integral $Z_n$ is a martingale with respect to $\{\mathcal{F}_n\}$. We showed this in Section 1.2.

- **Linearity**. If $J_n, K_n$ are predictable sequences and $a, b$ constants, then $aJ_n + bK_n$ is a predictable sequence and

$$\sum_{j=1}^{n}(aJ_j + bK_j)\, \Delta S_j = a\sum_{j=1}^{n} J_j\, \Delta S_j + b\sum_{j=1}^{n} K_j\, \Delta S_j.$$

  This is immediate.

- **Variance rule**

$$\operatorname{Var}\left[\sum_{j=1}^{n} J_j\, \Delta S_j\right] = \mathbb{E}\left[(\sum_{j=1}^{n} J_j\, \Delta S_j)^2\right] = \sigma^2 \sum_{j=1}^{n} \mathbb{E}\left[J_j^2\right].$$

To see this we first use the orthogonality of martingale increments to write

$$\mathbb{E}\left[(\sum_{j=1}^{n} J_j\, \Delta S_j)^2\right] = \sum_{j=1}^{n} \mathbb{E}\left[J_j^2 X_j^2\right].$$

Since $J_j$ is $\mathcal{F}_{j-1}$-measurable and $X_j$ is independent of $\mathcal{F}_{j-1}$, we can see that

$$
\begin{aligned}
\mathbb{E}\left[J_j^2 X_j^2\right] &= \mathbb{E}\left[E[J_j^2 X_j^2 \mid \mathcal{F}_{j-1}]\right] \\
&= \mathbb{E}\left[J_j^2\, E[X_j^2 \mid \mathcal{F}_{j-1}]\right] \\
&= \mathbb{E}\left[J_j^2\, \mathbb{E}[X_j^2]\right] = \sigma^2\, \mathbb{E}[J_j^2].
\end{aligned}
$$

---

## 1.7 A maximal inequality

There is another result about martingales that we will use.

**Theorem 1.7.1.** *Suppose $Y_n$ is a nonnegative submartingale with respect to $\{\mathcal{F}_n\}$, and*

$$\overline{Y}_n = \max\{Y_0, Y_1, \ldots, Y_n\}.$$

*Then for every $a > 0$,*

$$\mathbb{P}\{\overline{Y}_n \geq a\} \leq a^{-1}\, \mathbb{E}[Y_n].$$

### PDF page 34 (book page 28)

*Proof.* Let $T$ denote the smallest integer $k$ such that $Y_k \geq a$. Then

$$ \{\overline{Y}_n \geq a\} = \bigcup_{k=0}^{n} A_k, \quad A_k = \{T = k\}. $$

Note that $A_k$ is $\mathcal{F}_k$-measurable. Since $Y_n$ is a submartingale,

$$ \mathbb{E}\left[Y_n 1_{A_k}\right] = \mathbb{E}\left[E(Y_n \mid \mathcal{F}_k) \, 1_{A_k}\right] \geq \mathbb{E}\left[Y_k \, 1_{A_k}\right]. $$

By summing over $k$, we see that

$$ \mathbb{E}\left[Y_n\right] \geq \mathbb{E}\left[Y_n \, 1\{\overline{Y}_n \geq a\}\right] = \sum_{k=0}^{n} \mathbb{E}\left[Y_n \, 1_{A_k}\right] $$

$$ \geq \sum_{k=0}^{n} \mathbb{E}\left[Y_k \, 1_{A_k}\right] = \mathbb{E}\left[Y_T \, 1\{\overline{Y}_n \geq a\}\right] \geq a \, \mathbb{P}\{\overline{Y}_n \geq a\}. \quad \square $$

**Corollary 1.7.2.** *If $M_n$ is a square integrable martingale with respect to $\{\mathcal{F}_n\}$ and*
$$ \overline{M}_n = \max\left\{|M_0|, \ldots, |M_n|\right\}, $$
*then for every $a > 0$,*
$$ \mathbb{P}\left\{\overline{M}_n \geq a\right\} \leq a^{-2} \, \mathbb{E}\left[M_n^2\right]. $$

*Proof.* In Exercise 1.15, it is shown that $M_n^2$ is a submartingale, and we can use the previous theorem.

---

## 1.8 Exercises

**Exercise 1.1.** Suppose we roll two dice, a red and a green one, and let $X$ be the value on the red die and $Y$ the value on the green die. Let $Z = XY$.

1. Let $W = E(Z \mid X)$. What are the possible values for $W$? Give the distribution of $W$.

2. Do the same exercise for $U = E(X \mid Z)$.

3. Do the same exercise for $V = E(Y \mid X, Z)$

### PDF page 35 (book page 29)

**Exercise 1.2.** Suppose we roll two dice, a red and a green one, and let $X$ be the value on the red die and $Y$ the value on the green die. Let $Z = X/Y$.

1. Find $E[(X + 2Y)^2 \mid X]$.

2. Find $E[(X + 2Y)^2 \mid X, Z]$.

3. Find $E[X + 2Y \mid Z]$.

4. Let $W = E[Z \mid X]$. What are the possible values for $W$? Give the distribution of $W$.

**Exercise 1.3.** Suppose $X_1, X_2, \ldots$ are independent random variables with
$$ \mathbb{P}\{X_j = 2\} = 1 - \mathbb{P}\{X_j = -1\} = \frac{1}{3}. $$
Let $S_n = X_1 + \cdots + X_n$ and let $\mathcal{F}_n$ denote the information in $X_1, \ldots, X_n$.

1. Find $\mathbb{E}[S_n], \mathbb{E}[S_n^2], \mathbb{E}[S_n^3]$.

2. If $m < n$, find
$$ E[S_n \mid \mathcal{F}_m], \quad E[S_n^2 \mid \mathcal{F}_m], \quad E[S_n^3 \mid \mathcal{F}_m]. $$

3. If $m < n$, find $E[X_m \mid S_n]$.

**Exercise 1.4.** Repeat Exercise 1.3 assuming that
$$ \mathbb{P}\{X_j = 3\} = \mathbb{P}\{X_j = -1\} = \frac{1}{2}. $$

**Exercise 1.5.** Suppose $X_1, X_2, \ldots$ are independent random variables with
$$ \mathbb{P}\{X_j = 1\} = \mathbb{P}\{X_j = -1\} = \frac{1}{2}. $$
Let $S_n = X_1 + \cdots + X_n$. Find
$$ E\left(\sin S_n \mid S_n^2\right). $$

**Exercise 1.6.** In this exercise, we consider simple, nonsymmetric random walk. Suppose $1/2 < q < 1$ and $X_1, X_2, \ldots$ are independent random variables with
$$ \mathbb{P}\{X_j = 1\} = 1 - \mathbb{P}\{X_j = -1\} = q. $$
Let $S_0 = 0$ and $S_n = X_1 + \cdots + X_n$. Let $\mathcal{F}_n$ denote the information contained in $X_1, \ldots, X_n$.

### PDF page 36 (book page 30)

1. Which of these is $S_n$: martingale, submartingale, supermartingale (more than one answer is possible)?

2. For which values of $r$ is $M_n = S_n - rn$ a martingale?

3. Let $\theta = (1 - q)/q$ and let
$$ M_n = \theta^{S_n}. $$
Show that $M_n$ is a martingale.

4. Let $a, b$ be positive integers, and
$$ T_{a,b} = \min\{j : S_j = b \text{ or } S_j = -a\}. $$
Use the optional sampling theorem to determine
$$ \mathbb{P}\left\{S_{T_{a,b}} = b\right\}. $$

5. Let $T_a = T_{a,\infty}$. Find
$$ \mathbb{P}\{T_a < \infty\}. $$

**Exercise 1.7.** Suppose two people want to play a game in which person A has probability $2/3$ of winning. However, the only thing that they have is a fair coin which they can flip as many times as they want. They wish to find a method that requires only a finite number of coin flips.

1. Give one method to use the coins to simulate an experiment with probability $2/3$ of success. The number of flips needed can be random, but it must be finite with probability one.

2. Suppose $K < \infty$. Explain why there is no method such that with probability one we flip the coin at most $K$ times.

**Exercise 1.8.** Repeat the last exercise with $2/3$ replaced by $1/\pi$.

**Exercise 1.9.** Let $X_1, X_2, \ldots$ be independent, identically distributed random variables with
$$ \mathbb{P}\{X_j = 2\} = \frac{1}{3}, \quad \mathbb{P}\{X_j = \frac{1}{2}\} = \frac{2}{3}. $$
Let $M_0 = 1$ and for $n \geq 1$, $M_n = X_1 X_2 \cdots X_n$.

1. Show that $M_n$ is a martingale.

### PDF page 37 (book page 31)

2. Explain why $M_n$ satisfies the conditions of the martingale convergence theorem.

3. Let $M_\infty = \lim_{n\to\infty} M_n$. Explain why $M_\infty = 0$. (Hint: there are at least two ways to show this. One is to consider $\log M_n$ and use the law of large numbers. Another is to note that with probability one $M_{n+1}/M_n$ does not converge.)

4. Use the optional sampling theorem to determine the probability that $M_n$ ever attains a value as large as 64.

5. Does there exist a $C < \infty$ such that $\mathbb{E}[M_n^2] \le C$ for all $n$?

**Exercise 1.10.** Let $X_1, X_2, \ldots$ be independent, identically distributed random variables with

$$ \mathbb{P}\{X_j = 1\} = q, \quad \mathbb{P}\{X_j = -1\} = 1 - q. $$

Let $S_0 = 0$ and for $n \ge 1$, $S_n = X_1 + X_2 + \cdots + X_n$. Let $Y_n = e^{S_n}$.

1. For which value of $q$ is $Y_n$ a martingale?

2. For the remaining parts of this exercise assume $q$ takes the value from part 1. Explain why $Y_n$ satisfies the conditions of the martingale convergence theorem.

3. Let $Y_\infty = \lim_n Y_n$. Explain why $Y_\infty = 0$. (Hint: there are at least two ways to show this. One is to consider $\log Y_n$ and use the law of large numbers. Another is to note that with probability one $Y_{n+1}/Y_n$ does not converge.)

4. Use the optional sampling theorem to determine the probability that $Y_n$ ever attains a value greater than 100.

5. Does there exist a $C < \infty$ such that $\mathbb{E}[Y_n^2] \le C$ for all $n$?

**Exercise 1.11.** This exercise concerns Polya's urn and has a computing/simulation component. Let us start with one red and one green ball as in the lecture and let $M_n$ be the fraction of red balls at the $n$th stage.

### PDF page 38 (book page 32)

1. Show that the distribution of $M_n$ is uniform on the set

$$ \left\{ \frac{1}{n+2}, \frac{2}{n+2}, \ldots, \frac{n+1}{n+2} \right\}. $$

(Use mathematical induction, that is, note that it is obviously true for $n = 0$ and show that if it is true for $n$ then it is true for $n + 1$.)

2. Write a short program that will simulate this urn. Each time you run the program note the fraction of red balls after 600 draws and after 1200 draws. Compare the two fractions. Then, repeat this twenty times.

**Exercise 1.12.** Consider the martingale betting strategy as discussed in Section 1.2. Let $W_n$ be the "winnings" at time $n$, which for positive $n$ equals either 1 or $1 - 2^n$.

1. Is $W_n$ a square integrable martingale?

2. If $\Delta_n = W_n - W_{n-1}$ what is $\mathbb{E}[\Delta_n^2]$?

3. What is $\mathbb{E}[W_n^2]$?

4. What is $E(\Delta_n^2 \mid \mathcal{F}_{n-1})$?

**Exercise 1.13.** Suppose $S_n = X_1 + \cdots + X_n$ is simple random walk starting at 0. For any $K$, let

$$ T = \min\{n : |S_n| = K\}. $$

- Explain why for every $j$,

$$ \mathbb{P}\{T \le j + K \mid T > j\} \ge 2^{-K}. $$

- Show that there exists $c < \infty, \alpha > 0$ such that for all $j$,

$$ \mathbb{P}\{T > j\} \le c\, e^{-\alpha j}. $$

Conclude that $\mathbb{E}[T^r] < \infty$ for every $r > 0$.

- Let $M_n = S_n^2 - n$. Show there exists $C < \infty$ such that for all $n$,

$$ \mathbb{E}\left[ M_{n\wedge T}^2 \right] \le C. $$

### PDF page 39 (book page 33)

**Exercise 1.14.** Suppose that $X_1, X_2, \ldots$ are independent random variables with $\mathbb{E}[X_j] = 0$, $\mathrm{Var}[X_j] = \sigma_j^2$, and suppose that

$$ \sum_{n=1}^{\infty} \sigma_n^2 < \infty. $$

Let $S_0 = 0$ and $S_n = X_1 + \cdots + X_n$ for $n > 0$. Let $\mathcal{F}_n$ denote the information contained in $X_1, \ldots, X_n$.

- Show that $S_n$ is a martingale with respect to $\{\mathcal{F}_n\}$.

- Show that there exists $C < \infty$ such that for all $n$, $\mathbb{E}[S_n^2] \le C$.

- Show that with probability one the limit

$$ S_\infty = \lim_{n\to\infty} S_n, $$

exists.

- Show that

$$ \mathbb{E}[S_\infty] = 0, \quad \mathrm{Var}[S_\infty] = \sum_{n=1}^{\infty} \sigma_n^2. $$

---

**Exercise 1.15.**

- Suppose $Y$ is a random variable and $\phi$ is a convex function, that is, if $0 \le \lambda \le 1$,

$$ \phi(\lambda x + (1 - \lambda)\, y) \le \lambda\, \phi(x) + (1 - \lambda)\, \phi(y). $$

Suppose that $\mathbb{E}[|\phi(Y)|] < \infty$. Show that $E(\phi(Y) \mid X) \ge \phi(E(Y \mid X))$. (Hint: you will need to review Jensen's inequality.)

- Show that if $M_n$ is a martingale with respect to $\{\mathcal{F}_n\}$ and $r \ge 1$, then $Y_n = |M_n|^r$ is a submartingale.

---

All three pages transcribed. Note page 39 has two horizontal rules bracketing Exercise 1.15 (a boxed exercise in the original), which I've preserved with `---`.

### PDF page 40 (book page 34)
*(Blank page.)*

# Chapter 4 — Introduction to Markov Chain Mixing
*(PDF pages 63–75; book pages 47–59)*

### PDF page 63 (book page 47)

# Chapter 4 — Introduction to Markov Chain Mixing

We are now ready to discuss the long-term behavior of finite Markov chains. Since we are interested in quantifying the speed of convergence of families of Markov chains, we need to choose an appropriate metric for measuring the distance between distributions.

First we define ***total variation distance*** and give several characterizations of it, all of which will be useful in our future work. Next we prove the Convergence Theorem (Theorem 4.9), which says that for an irreducible and aperiodic chain the distribution after many steps approaches the chain's stationary distribution, in the sense that the total variation distance between them approaches 0. In the rest of the chapter we examine the effects of the initial distribution on distance from stationarity, define the *mixing time* of a chain, consider circumstances under which related chains can have identical mixing, and prove a version of the Ergodic Theorem (Theorem C.1) for Markov chains.

**4.1. Total Variation Distance**

The ***total variation distance*** between two probability distributions $\mu$ and $\nu$ on $\mathcal{X}$ is defined by

$$ \|\mu - \nu\|_{\mathrm{TV}} = \max_{A \subseteq \mathcal{X}} |\mu(A) - \nu(A)| . \tag{4.1} $$

This definition is explicitly probabilistic: the distance between $\mu$ and $\nu$ is the maximum difference between the probabilities assigned to a single event by the two distributions.

EXAMPLE 4.1. Recall the coin-tossing frog of Example 1.1, who has probability $p$ of jumping from east to west and probability $q$ of jumping from west to east. The transition matrix is $\begin{pmatrix} 1-p & p \\ q & 1-q \end{pmatrix}$ and its stationary distribution is $\pi = \left( \frac{q}{p+q}, \frac{p}{p+q} \right)$. Assume the frog starts at the east pad (that is, $\mu_0 = (1,0)$) and define

$$ \Delta_t = \mu_t(e) - \pi(e). $$

Since there are only two states, there are only four possible events $A \subseteq \mathcal{X}$. Hence it is easy to check (and you should) that

$$ \|\mu_t - \pi\|_{\mathrm{TV}} = |\Delta_t| = |P^t(e,e) - \pi(e)| = |\pi(w) - P^t(e,w)|. $$

We pointed out in Example 1.1 that $\Delta_t = (1 - p - q)^t \Delta_0$. Hence for this two-state chain, the total variation distance decreases exponentially fast as $t$ increases. (Note that $(1 - p - q)$ is an eigenvalue of $P$; we will discuss connections between eigenvalues and mixing in Chapter 12.)

The definition of total variation distance (4.1) is a maximum over *all* subsets of $\mathcal{X}$, so using this definition is not always the most convenient way to estimate

### PDF page 64 (book page 48)

**FIGURE 4.1.** Recall that $B = \{x : \mu(x) \geq \nu(x)\}$. Region I has area $\mu(B) - \nu(B)$. Region II has area $\nu(B^c) - \mu(B^c)$. Since the total area under each of $\mu$ and $\nu$ is 1, regions I and II must have the same area—and that area is $\|\mu - \nu\|_{\mathrm{TV}}$. *[Figure: two overlapping histogram-shaped distributions $\mu$ (left) and $\nu$ (right); the region where $\mu$ exceeds $\nu$ is labeled I, the region where $\nu$ exceeds $\mu$ is labeled II; a horizontal axis below is split into an interval $B$ on the left and $B^c$ on the right.]*

the distance. We now give three extremely useful alternative characterizations. Proposition 4.2 reduces total variation distance to a simple sum over the state space. Proposition 4.7 uses *coupling* to give another probabilistic interpretation: $\|\mu - \nu\|_{\mathrm{TV}}$ measures how close to identical we can force two random variables realizing $\mu$ and $\nu$ to be.

PROPOSITION 4.2. *Let $\mu$ and $\nu$ be two probability distributions on $\mathcal{X}$. Then*

$$\|\mu - \nu\|_{\mathrm{TV}} = \frac{1}{2} \sum_{x \in \mathcal{X}} |\mu(x) - \nu(x)| . \tag{4.2}$$

PROOF. Let $B = \{x : \mu(x) \geq \nu(x)\}$ and let $A \subset \mathcal{X}$ be any event. Then

$$\mu(A) - \nu(A) \leq \mu(A \cap B) - \nu(A \cap B) \leq \mu(B) - \nu(B). \tag{4.3}$$

The first inequality is true because any $x \in A \cap B^c$ satisfies $\mu(x) - \nu(x) < 0$, so the difference in probability cannot decrease when such elements are eliminated. For the second inequality, note that including more elements of $B$ cannot decrease the difference in probability.

By exactly parallel reasoning,

$$\nu(A) - \mu(A) \leq \nu(B^c) - \mu(B^c). \tag{4.4}$$

Fortunately, the upper bounds on the right-hand sides of (4.3) and (4.4) are actually the same (as can be seen by subtracting them; see Figure 4.1). Furthermore, when we take $A = B$ (or $B^c$), then $|\mu(A) - \nu(A)|$ is equal to the upper bound. Thus

$$\|\mu - \nu\|_{\mathrm{TV}} = \frac{1}{2} \left[ \mu(B) - \nu(B) + \nu(B^c) - \mu(B^c) \right] = \frac{1}{2} \sum_{x \in \mathcal{X}} |\mu(x) - \nu(x)|.$$

$\blacksquare$

REMARK 4.3. The proof of Proposition 4.2 also shows that

$$\|\mu - \nu\|_{\mathrm{TV}} = \sum_{\substack{x \in \mathcal{X} \\ \mu(x) \geq \nu(x)}} [\mu(x) - \nu(x)], \tag{4.5}$$

### PDF page 65 (book page 49)

which is a useful identity.

REMARK 4.4. From Proposition 4.2 and the triangle inequality for real numbers, it is easy to see that total variation distance satisfies the triangle inequality: for probability distributions $\mu, \nu$ and $\eta$,

$$\|\mu - \nu\|_{\mathrm{TV}} \leq \|\mu - \eta\|_{\mathrm{TV}} + \|\eta - \nu\|_{\mathrm{TV}} . \tag{4.6}$$

PROPOSITION 4.5. *Let $\mu$ and $\nu$ be two probability distributions on $\mathcal{X}$. Then the total variation distance between them satisfies*

$$\|\mu - \nu\|_{\mathrm{TV}} \;=\; \frac{1}{2} \sup \left\{ \sum_{x \in \mathcal{X}} f(x)\mu(x) - \sum_{x \in \mathcal{X}} f(x)\nu(x) \;\;:\; \max_{x \in \mathcal{X}} |f(x)| \leq 1 \right\}. \tag{4.7}$$

PROOF. If $\max_{x \in \mathcal{X}} |f(x)| \leq 1$, then

$$\frac{1}{2} \left| \sum_{x \in \mathcal{X}} f(x)\mu(x) - \sum_{x \in \mathcal{X}} f(x)\nu(x) \right| \leq \frac{1}{2} \sum_{x \in \mathcal{X}} |\mu(x) - \nu(x)| = \|\mu - \nu\|_{\mathrm{TV}} .$$

Thus, the right-hand side of (4.7) is at most $\|\mu - \nu\|_{\mathrm{TV}}$.

For the other direction, define

$$f^{\star}(x) = \begin{cases} 1 & \text{if } \mu(x) \geq \nu(x), \\ -1 & \text{if } \mu(x) < \nu(x). \end{cases}$$

Then

$$\frac{1}{2} \left[ \sum_{x \in \mathcal{X}} f^{\star}(x)\mu(x) - \sum_{x \in \mathcal{X}} f^{\star}(x)\nu(x) \right] = \frac{1}{2} \sum_{x \in \mathcal{X}} f^{\star}(x)[\mu(x) - \nu(x)]$$

$$= \frac{1}{2} \left[ \sum_{\substack{x \in \mathcal{X} \\ \mu(x) \geq \nu(x)}} [\mu(x) - \nu(x)] + \sum_{\substack{x \in \mathcal{X} \\ \nu(x) > \mu(x)}} [\nu(x) - \mu(x)] \right].$$

Using (4.5) shows that the right-hand side above equals $\|\mu - \nu\|_{\mathrm{TV}}$. Hence the right-hand side of (4.7) is at least $\|\mu - \nu\|_{\mathrm{TV}}$. $\blacksquare$

**4.2. Coupling and Total Variation Distance**

A ***coupling*** of two probability distributions $\mu$ and $\nu$ is a pair of random variables $(X, Y)$ defined on a single probability space such that the marginal distribution of $X$ is $\mu$ and the marginal distribution of $Y$ is $\nu$. That is, a coupling $(X, Y)$ satisfies $\mathbf{P}\{X = x\} = \mu(x)$ and $\mathbf{P}\{Y = y\} = \nu(y)$.

Coupling is a general and powerful technique; it can be applied in many different ways. Indeed, Chapters 5 and 14 use couplings of entire chain trajectories to bound rates of convergence to stationarity. Here, we offer a gentle introduction by showing the close connection between couplings of two random variables and the total variation distance between those variables.

EXAMPLE 4.6. Let $\mu$ and $\nu$ both be the "fair coin" measure giving weight $1/2$ to the elements of $\{0, 1\}$.

(i) One way to couple $\mu$ and $\nu$ is to define $(X, Y)$ to be a pair of independent coins, so that $\mathbf{P}\{X = x, Y = y\} = 1/4$ for all $x, y \in \{0, 1\}$.

### PDF page 66 (book page 50)

(ii) Another way to couple $\mu$ and $\nu$ is to let $X$ be a fair coin toss and define $Y = X$. In this case, $\mathbf{P}\{X = Y = 0\} = 1/2$, $\mathbf{P}\{X = Y = 1\} = 1/2$, and $\mathbf{P}\{X \neq Y\} = 0$.

Given a coupling $(X, Y)$ of $\mu$ and $\nu$, if $q$ is the joint distribution of $(X, Y)$ on $\mathcal{X} \times \mathcal{X}$, meaning that $q(x, y) = \mathbf{P}\{X = x, Y = y\}$, then $q$ satisfies

$$\sum_{y \in \mathcal{X}} q(x, y) = \sum_{y \in \mathcal{X}} \mathbf{P}\{X = x, Y = y\} = \mathbf{P}\{X = x\} = \mu(x)$$

and

$$\sum_{x \in \mathcal{X}} q(x, y) = \sum_{x \in \mathcal{X}} \mathbf{P}\{X = x, Y = y\} = \mathbf{P}\{Y = y\} = \nu(y).$$

Conversely, given a probability distribution $q$ on the product space $\mathcal{X} \times \mathcal{X}$ which satisfies

$$\sum_{y \in \mathcal{X}} q(x, y) = \mu(x) \quad \text{and} \quad \sum_{x \in \mathcal{X}} q(x, y) = \nu(y),$$

there is a pair of random variables $(X, Y)$ having $q$ as their joint distribution – and consequently this pair $(X, Y)$ is a coupling of $\mu$ and $\nu$. In summary, a coupling can be specified either by a pair of random variables $(X, Y)$ defined on a common probability space or by a distribution $q$ on $\mathcal{X} \times \mathcal{X}$.

Returning to Example 4.6, the coupling in part (i) could equivalently be specified by the probability distribution $q_1$ on $\{0, 1\}^2$ given by

$$q_1(x, y) = \frac{1}{4} \quad \text{for all } (x, y) \in \{0, 1\}^2.$$

Likewise, the coupling in part (ii) can be identified with the probability distribution $q_2$ given by

$$q_2(x, y) = \begin{cases} \frac{1}{2} & \text{if } (x, y) = (0, 0), \ (x, y) = (1, 1), \\ 0 & \text{if } (x, y) = (0, 1), \ (x, y) = (1, 0). \end{cases}$$

Any two distributions $\mu$ and $\nu$ have an independent coupling. However, when $\mu$ and $\nu$ are not identical, it will not be possible for $X$ and $Y$ to always have the same value. How close can a coupling get to having $X$ and $Y$ identical? Total variation distance gives the answer.

PROPOSITION 4.7. *Let $\mu$ and $\nu$ be two probability distributions on $\mathcal{X}$. Then*

$$\|\mu - \nu\|_{\mathrm{TV}} = \inf \left\{ \mathbf{P}\{X \neq Y\} \, : \, (X, Y) \text{ is a coupling of } \mu \text{ and } \nu \right\}. \tag{4.8}$$

REMARK 4.8. We will in fact show that there is a coupling $(X, Y)$ which attains the infimum in (4.8). We will call such a coupling ***optimal***.

PROOF. First, we note that for any coupling $(X, Y)$ of $\mu$ and $\nu$ and any event $A \subset \mathcal{X}$,

$$\mu(A) - \nu(A) = \mathbf{P}\{X \in A\} - \mathbf{P}\{Y \in A\} \tag{4.9}$$

$$\leq \mathbf{P}\{X \in A, Y \notin A\} \tag{4.10}$$

$$\leq \mathbf{P}\{X \neq Y\}. \tag{4.11}$$

(Dropping the event $\{X \notin A, Y \in A\}$ from the second term of the difference gives the first inequality.) It immediately follows that

$$\|\mu - \nu\|_{\mathrm{TV}} \leq \inf \left\{ \mathbf{P}\{X \neq Y\} \, : \, (X, Y) \text{ is a coupling of } \mu \text{ and } \nu \right\}. \tag{4.12}$$

### PDF page 67 (book page 51)

*[Figure: a histogram-style plot showing two overlapping step-function distributions $\mu$ and $\nu$. The region where $\mu$ exceeds $\nu$ is labeled **I** (left), the region where $\nu$ exceeds $\mu$ is labeled **II** (right), and the overlap region beneath both is labeled **III** (bottom center). $\mu$ is labeled on the left, $\nu$ on the right.]*

FIGURE 4.2. Since each of regions I and II has area $\|\mu - \nu\|_{\mathrm{TV}}$ and $\mu$ and $\nu$ are probability measures, region III has area $1 - \|\mu - \nu\|_{\mathrm{TV}}$.

It will suffice to construct a coupling for which $\mathbf{P}\{X \neq Y\}$ is exactly equal to $\|\mu - \nu\|_{\mathrm{TV}}$. We will do so by forcing $X$ and $Y$ to be equal as often as they possibly can be. Consider Figure 4.2. Region III, bounded by $\mu(x) \wedge \nu(x) = \min\{\mu(x), \nu(x)\}$, can be seen as the overlap between the two distributions. Informally, our coupling proceeds by choosing a point in the union of regions I and III, and setting $X$ to be the $x$-coordinate of this point. If the point is in III, we set $Y = X$ and if it is in I, then we choose independently a point at random from region II, and set $Y$ to be the $x$-coordinate of the newly selected point. In the second scenario, $X \neq Y$, since the two regions are disjoint.

More formally, we use the following procedure to generate $X$ and $Y$. Let

$$ p = \sum_{x \in \mathcal{X}} \mu(x) \wedge \nu(x). $$

Write

$$ \sum_{x \in \mathcal{X}} \mu(x) \wedge \nu(x) = \sum_{\substack{x \in \mathcal{X}, \\ \mu(x) \leq \nu(x)}} \mu(x) + \sum_{\substack{x \in \mathcal{X}, \\ \mu(x) > \nu(x)}} \nu(x). $$

Adding and subtracting $\sum_{x \,:\, \mu(x) > \nu(x)} \mu(x)$ to the right-hand side above shows that

$$ \sum_{x \in \mathcal{X}} \mu(x) \wedge \nu(x) = 1 - \sum_{\substack{x \in \mathcal{X}, \\ \mu(x) > \nu(x)}} [\mu(x) - \nu(x)]. $$

By equation (4.5) and the immediately preceding equation,

$$ \sum_{x \in \mathcal{X}} \mu(x) \wedge \nu(x) = 1 - \|\mu - \nu\|_{\mathrm{TV}} = p. \tag{4.13} $$

Flip a coin with probability of heads equal to $p$.

(i) If the coin comes up heads, then choose a value $Z$ according to the probability distribution

$$ \gamma_{\mathrm{III}}(x) = \frac{\mu(x) \wedge \nu(x)}{p}, $$

and set $X = Y = Z$.

### PDF page 68 (book page 52)

(ii) If the coin comes up tails, choose $X$ according to the probability distribution

$$ \gamma_{\mathrm{I}}(x) = \begin{cases} \dfrac{\mu(x) - \nu(x)}{\|\mu - \nu\|_{\mathrm{TV}}} & \text{if } \mu(x) > \nu(x), \\ 0 & \text{otherwise,} \end{cases} $$

and independently choose $Y$ according to the probability distribution

$$ \gamma_{\mathrm{II}}(x) = \begin{cases} \dfrac{\nu(x) - \mu(x)}{\|\mu - \nu\|_{\mathrm{TV}}} & \text{if } \nu(x) > \mu(x), \\ 0 & \text{otherwise.} \end{cases} $$

Note that (4.5) ensures that $\gamma_{\mathrm{I}}$ and $\gamma_{\mathrm{II}}$ are probability distributions.

Clearly,

$$ p\gamma_{\mathrm{III}} + (1 - p)\gamma_{\mathrm{I}} = \mu, $$
$$ p\gamma_{\mathrm{III}} + (1 - p)\gamma_{\mathrm{II}} = \nu, $$

so that the distribution of $X$ is $\mu$ and the distribution of $Y$ is $\nu$. Note that in the case that the coin lands tails up, $X \neq Y$ since $\gamma_{\mathrm{I}}$ and $\gamma_{\mathrm{II}}$ are positive on disjoint subsets of $\mathcal{X}$. Thus $X = Y$ if and only if the coin toss is heads. We conclude that

$$ \mathbf{P}\{X \neq Y\} = \|\mu - \nu\|_{\mathrm{TV}}. $$

$\blacksquare$

**4.3. The Convergence Theorem**

We are now ready to prove that irreducible, aperiodic Markov chains converge to their stationary distributions—a key step, as much of the rest of the book will be devoted to estimating the rate at which this convergence occurs. The assumption of aperiodicity is indeed necessary—recall the even $n$-cycle of Example 1.4.

As is often true of such fundamental facts, there are many proofs of the Convergence Theorem. The one given here decomposes the chain into a mixture of repeated independent sampling from the stationary distribution and another Markov chain. See Exercise 5.1 for another proof using two coupled copies of the chain.

THEOREM 4.9 (Convergence Theorem). *Suppose that $P$ is irreducible and aperiodic, with stationary distribution $\pi$. Then there exist constants $\alpha \in (0, 1)$ and $C > 0$ such that*

$$ \max_{x \in \mathcal{X}} \left\| P^t(x, \cdot) - \pi \right\|_{\mathrm{TV}} \leq C\alpha^t. \tag{4.14} $$

PROOF. Since $P$ is irreducible and aperiodic, by Proposition 1.7 there exists an $r$ such that $P^r$ has strictly positive entries. Let $\Pi$ be the matrix with $|\mathcal{X}|$ rows, each of which is the row vector $\pi$. For sufficiently small $\delta > 0$, we have

$$ P^r(x, y) \geq \delta\pi(y) $$

for all $x, y \in \mathcal{X}$. Let $\theta = 1 - \delta$. The equation

$$ P^r = (1 - \theta)\Pi + \theta Q \tag{4.15} $$

defines a stochastic matrix $Q$.

It is a straightforward computation to check that $M\Pi = \Pi$ for any stochastic matrix $M$ and that $\Pi M = \Pi$ for any matrix $M$ such that $\pi M = \pi$.

Next, we use induction to demonstrate that

$$ P^{rk} = \left(1 - \theta^k\right)\Pi + \theta^k Q^k \tag{4.16} $$

### PDF page 69 (book page 53)

for $k \geq 1$. If $k = 1$, this holds by (4.15). Assuming that (4.16) holds for $k = n$,

$$ P^{r(n+1)} = P^{rn}P^r = \left[(1 - \theta^n)\Pi + \theta^n Q^n\right] P^r. \tag{4.17} $$

Distributing and expanding $P^r$ in the second term (using (4.15)) gives

$$ P^{r(n+1)} = [1 - \theta^n]\Pi P^r + (1 - \theta)\theta^n Q^n \Pi + \theta^{n+1} Q^n Q. \tag{4.18} $$

Using that $\Pi P^r = \Pi$ and $Q^n \Pi = \Pi$ shows that

$$ P^{r(n+1)} = \left[1 - \theta^{n+1}\right]\Pi + \theta^{n+1} Q^{n+1}. \tag{4.19} $$

This establishes (4.16) for $k = n + 1$ (assuming it holds for $k = n$), and hence it holds for all $k$.

Multiplying by $P^j$ and rearranging terms now yields

$$ P^{rk+j} - \Pi = \theta^k \left( Q^k P^j - \Pi \right). \tag{4.20} $$

To complete the proof, sum the absolute values of the elements in row $x_0$ on both sides of (4.20) and divide by 2. On the right, the second factor is at most the largest possible total variation distance between distributions, which is 1. Hence for any $x_0$ we have

$$ \left\| P^{rk+j}(x_0, \cdot) - \pi \right\|_{\mathrm{TV}} \leq \theta^k. \tag{4.21} $$

Taking $\alpha = \theta^{1/r}$ and $C = 1/\theta$ finishes the proof. $\blacksquare$

**4.4. Standardizing Distance from Stationarity**

Bounding the maximal distance (over $x_0 \in \mathcal{X}$) between $P^t(x_0, \cdot)$ and $\pi$ is among our primary objectives. It is therefore convenient to define

$$ d(t) := \max_{x \in \mathcal{X}} \left\| P^t(x, \cdot) - \pi \right\|_{\mathrm{TV}}. \tag{4.22} $$

We will see in Chapter 5 that it is often possible to bound $\|P^t(x, \cdot) - P^t(y, \cdot)\|_{\mathrm{TV}}$, uniformly over all pairs of states $(x, y)$. We therefore make the definition

$$ \bar{d}(t) := \max_{x,y \in \mathcal{X}} \left\| P^t(x, \cdot) - P^t(y, \cdot) \right\|_{\mathrm{TV}}. \tag{4.23} $$

The relationship between $d$ and $\bar{d}$ is given below:

LEMMA 4.10. *If $d(t)$ and $\bar{d}(t)$ are as defined in (4.22) and (4.23), respectively, then*

$$ d(t) \leq \bar{d}(t) \leq 2d(t). \tag{4.24} $$

PROOF. It is immediate from the triangle inequality for the total variation distance that $\bar{d}(t) \leq 2d(t)$.

To show that $d(t) \leq \bar{d}(t)$, note first that since $\pi$ is stationary, we have $\pi(A) = \sum_{y \in \mathcal{X}} \pi(y) P^t(y, A)$ for any set $A$. (This is the definition of stationarity if $A$ is a singleton $\{x\}$. To get this for arbitrary $A$, just sum over the elements in $A$.) Using this shows that

$$ |P^t(x, A) - \pi(A)| = \left| \sum_{y \in \mathcal{X}} \pi(y) \left[ P^t(x, A) - P^t(y, A) \right] \right| $$
$$ \leq \sum_{y \in \mathcal{X}} \pi(y) \left\| P^t(x, \cdot) - P^t(y, \cdot) \right\|_{\mathrm{TV}} \leq \bar{d}(t), \tag{4.25} $$

by the triangle inequality and the definition of total variation. Maximizing the left-hand side over $x$ and $A$ yields $d(t) \leq \bar{d}(t)$.

### PDF page 70 (book page 54)

$\blacksquare$

Let $\mathcal{P}$ denote the collection of all probability distributions on $\mathcal{X}$. Exercise 4.1 asks the reader to prove the following equalities:

$$ d(t) = \sup_{\mu \in \mathcal{P}} \left\| \mu P^t - \pi \right\|_{\mathrm{TV}} , $$

$$ \bar{d}(t) = \sup_{\mu, \nu \in \mathcal{P}} \left\| \mu P^t - \nu P^t \right\|_{\mathrm{TV}} . $$

LEMMA 4.11. *The function $\bar{d}$ is submultiplicative: $\bar{d}(s + t) \leq \bar{d}(s)\bar{d}(t)$.*

PROOF. Fix $x, y \in \mathcal{X}$, and let $(X_s, Y_s)$ be the optimal coupling of $P^s(x, \cdot)$ and $P^s(y, \cdot)$ whose existence is guaranteed by Proposition 4.7. Hence

$$ \|P^s(x, \cdot) - P^s(y, \cdot)\|_{\mathrm{TV}} = \mathbf{P}\{X_s \neq Y_s\}. \tag{4.26} $$

We have

$$ P^{s+t}(x, w) = \sum_z \mathbf{P}\{X_s = z\}P^t(z, w) = \mathbf{E}\left(P^t(X_s, w)\right). \tag{4.27} $$

For a set $A$, summing over $w \in A$ shows that

$$ \begin{aligned} P^{s+t}(x, A) - P^{s+t}(y, A) &= \mathbf{E}\left(P^t(X_s, A) - P^t(Y_s, A)\right) \\ &\leq \mathbf{E}\left(\bar{d}(t)\mathbf{1}_{\{X_s \neq Y_s\}}\right) = \mathbf{P}\{X_s \neq Y_s\}\bar{d}(t). \end{aligned} \tag{4.28} $$

By (4.26), the right-hand side is at most $\bar{d}(s)\bar{d}(t)$.

$\blacksquare$

REMARK 4.12. Theorem 4.9 can be deduced from Lemma 4.11. One needs to check that $\bar{d}(s) < 1$ for some $s$; this follows since $P^s$ has all positive entries for some $s$.

Exercise 4.2 implies that $\bar{d}(t)$ is non-increasing in $t$. By Lemma 4.10 and Lemma 4.11, if $c$ and $t$ are positive integers, then

$$ d(ct) \leq \bar{d}(ct) \leq \bar{d}(t)^c. \tag{4.29} $$

**4.5. Mixing Time**

It is useful to introduce a parameter which measures the time required by a Markov chain for the distance to stationarity to be small. The **mixing time** is defined by

$$ t_{\mathrm{mix}}(\varepsilon) := \min\{t \ : \ d(t) \leq \varepsilon\} \tag{4.30} $$

and

$$ t_{\mathrm{mix}} := t_{\mathrm{mix}}(1/4). \tag{4.31} $$

Lemma 4.10 and (4.29) show that when $\ell$ is a positive integer,

$$ d(\ell t_{\mathrm{mix}}(\varepsilon)) \leq \bar{d}(t_{\mathrm{mix}}(\varepsilon))^\ell \leq (2\varepsilon)^\ell. \tag{4.32} $$

In particular, taking $\varepsilon = 1/4$ above yields

$$ d(\ell t_{\mathrm{mix}}) \leq 2^{-\ell} \tag{4.33} $$

and

$$ t_{\mathrm{mix}}(\varepsilon) \leq \left\lceil \log_2 \varepsilon^{-1} \right\rceil t_{\mathrm{mix}}. \tag{4.34} $$

### PDF page 71 (book page 55)

See Exercise 4.3 for a small improvement. Thus, although the choice of $1/4$ is arbitrary in the definition (4.31) of $t_{\mathrm{mix}}$, a value of $\varepsilon$ less than $1/2$ is needed to make the inequality $d(\ell t_{\mathrm{mix}}(\varepsilon)) \leq (2\varepsilon)^\ell$ in (4.32) meaningful and to achieve an inequality of the form (4.34).

Rigorous upper bounds on mixing times lend confidence that simulation studies or randomized algorithms perform as advertised.

**4.6. Mixing and Time Reversal**

For a distribution $\mu$ on a group $G$, the **reversed distribution** $\widehat{\mu}$ is defined by $\widehat{\mu}(g) := \mu(g^{-1})$ for all $g \in G$. Let $P$ be the transition matrix of the random walk with increment distribution $\mu$. Then the random walk with increment distribution $\widehat{\mu}$ is exactly the time reversal $\widehat{P}$ (defined in (1.32)) of $P$.

In Proposition 2.14 we noted that when $\widehat{\mu} = \mu$, the random walk on $G$ with increment distribution $\mu$ is reversible, so that $P = \widehat{P}$. Even when $\mu$ is not a symmetric distribution, however, the forward and reversed walks must be at the same distance from stationarity; we will use this in analyzing card shuffling in Chapters 6 and 8.

LEMMA 4.13. *Let $P$ be the transition matrix of a random walk on a group $G$ with increment distribution $\mu$ and let $\widehat{P}$ be that of the walk on $G$ with increment distribution $\widehat{\mu}$. Let $\pi$ be the uniform distribution on $G$. Then for any $t \geq 0$*

$$ \left\| P^t(\mathrm{id}, \cdot) - \pi \right\|_{\mathrm{TV}} = \left\| \widehat{P}^t(\mathrm{id}, \cdot) - \pi \right\|_{\mathrm{TV}} . $$

PROOF. Let $(X_t) = (\mathrm{id}, X_1, \ldots)$ be a Markov chain with transition matrix $P$ and initial state id. We can write $X_k = g_k g_{k-1} \ldots g_1$, where the random elements $g_1, g_2, \cdots \in G$ are independent choices from the distribution $\mu$. Similarly, let $(Y_t)$ be a chain with transition matrix $\widehat{P}$, with increments $h_1, h_2, \cdots \in G$ chosen independently from $\widehat{\mu}$. For any fixed elements $a_1, \ldots, a_t \in G$,

$$ \mathbf{P}\{g_1 = a_1, \ldots, g_t = a_t\} = \mathbf{P}\{h_1 = a_t^{-1}, \ldots, h_t = a_1^{-1}\}, $$

by the definition of $\widehat{P}$. Summing over all strings such that $a_t a_{t-1} \ldots a_1 = a$ yields

$$ P^t(\mathrm{id}, a) = \widehat{P}^t(\mathrm{id}, a^{-1}). $$

Hence

$$ \sum_{a \in G} \left| P^t(\mathrm{id}, a) - |G|^{-1} \right| = \sum_{a \in G} \left| \widehat{P}^t(\mathrm{id}, a^{-1}) - |G|^{-1} \right| = \sum_{a \in G} \left| \widehat{P}^t(\mathrm{id}, a) - |G|^{-1} \right| $$

which together with Proposition 4.2 implies the desired result.

$\blacksquare$

COROLLARY 4.14. *If $t_{\mathrm{mix}}$ is the mixing time of a random walk on a group and $\widehat{t_{\mathrm{mix}}}$ is the mixing time of the reversed walk, then $t_{\mathrm{mix}} = \widehat{t_{\mathrm{mix}}}$.*

It is also possible for reversing a Markov chain to significantly change the mixing time. The *winning streak* is an example, and is discussed in Section 5.3.5.

### PDF page 72 (book page 56)

**4.7. $\ell^p$ Distance and Mixing**

The material in this section is not used until Chapter 10.

Other distances between distributions are useful. Given a distribution $\pi$ on $\mathcal{X}$ and $1 \leq p \leq \infty$, the $\ell^p(\pi)$ norm of a function $f : \mathcal{X} \to \mathbb{R}$ is defined as

$$ \|f\|_p := \begin{cases} \left[\sum_{y \in \mathcal{X}} |f(y)|^p \pi(y)\right]^{1/p} & 1 \leq p < \infty, \\ \max_{y \in \mathcal{X}} |f(y)| & p = \infty . \end{cases} $$

For functions $f, g : \mathcal{X} \to \mathbb{R}$, define the scalar product

$$ \langle f, g \rangle_\pi := \sum_{x \in \mathcal{X}} f(x)g(x)\pi(x) . $$

For an irreducible transition matrix $P$ on $\mathcal{X}$ with stationary distribution $\pi$, define

$$ q_t(x, y) := \frac{P^t(x, y)}{\pi(y)} , $$

and note that $q_t(x, y) = q_t(y, x)$ when $P$ is reversible with respect to $\pi$. Note also that

$$ \langle q_t(x, \cdot), 1 \rangle_\pi = \sum_y q_t(x, y)\pi(y) = 1 . \tag{4.35} $$

The $\ell^p$-distance $d^{(p)}$ is defined as

$$ d^{(p)}(t) := \max_{x \in \mathcal{X}} \|q_t(x, \cdot) - 1\|_p . \tag{4.36} $$

Proposition 4.2 shows that $d^{(1)}(t) = 2d(t)$. The distance $d^{(p)}$ is submultiplicative:

$$ d^{(p)}(t + s) \leq d^{(p)}(t)d^{(p)}(s) . $$

This is proved in the Notes to this chapter (Lemma 4.18). We mostly focus in this book on the cases $p = 1, 2$ and $p = \infty$. The $\ell^2$ distance is particularly convenient in the reversible case due to the identity given as Lemma 12.18(i).

Since the $\ell^p$ norms are non-decreasing (Exercise 4.5),

$$ 2d(t) = d^{(1)}(t) \leq d^{(2)}(t) \leq d^{(\infty)}(t) . \tag{4.37} $$

Finally, $\ell^2$ and $\ell^\infty$ distances are related as follows for reversible chains:

PROPOSITION 4.15. *For a reversible Markov chain,*

$$ d^{(\infty)}(2t) = [d^{(2)}(t)]^2 = \max_{x \in \mathcal{X}} q_{2t}(x, x) - 1 . \tag{4.38} $$

PROOF. First observe that

$$ P^{2t}(x, y) = \sum_{z \in \mathcal{X}} P^t(x, z)P^t(z, y) . $$

Dividing both sides by $\pi(y)$ and using reversibility yields

$$ q_{2t}(x, y) = \sum_{z \in \mathcal{X}} \frac{P^t(x, z)}{\pi(z)} \frac{P^t(z, y)}{\pi(y)}\pi(z) = \langle q_t(x, \cdot), q_t(y, \cdot) \rangle_\pi . \tag{4.39} $$

Using (4.35), we have

$$ \begin{aligned} \langle q_t(x, \cdot) - 1, q_t(y, \cdot) - 1 \rangle_\pi &= \langle q_t(x, \cdot), q_t(y, \cdot) \rangle_\pi - \langle 1, q_t(y, \cdot) \rangle_\pi - \langle q_t(x, \cdot), 1 \rangle_\pi + 1 \\ &= q_{2t}(x, y) - 1 . \end{aligned} \tag{4.40} $$

### PDF page 73 (book page 57)

In particular, taking $x = y$ shows that

$$ \|q_t(x, \cdot) - 1\|_2^2 = q_{2t}(x, x) - 1 \,. \tag{4.41} $$

Maximizing over $x$ yields the right-hand equality in (4.38). By (4.40) and Cauchy-Schwarz,

$$
\begin{aligned}
|q_{2t}(x, y) - 1| &\leq \|q_t(x, \cdot) - 1\|_2 \cdot \|q_t(y, \cdot) - 1\|_2 \\
&= \sqrt{q_{2t}(x, x) - 1}\sqrt{q_{2t}(y, y) - 1} \,.
\end{aligned}
\tag{4.42}
$$

Thus,

$$ d^{(\infty)}(2t) = \max_{x,y \in \mathcal{X}} |q_{2t}(x, y) - 1| \leq \max_{x \in \mathcal{X}} q_{2t}(x, x) - 1 \,. \tag{4.43} $$

Considering $x = y$ shows that equality holds in (4.43) and proves the proposition. $\blacksquare$

We define the $\ell^p$**-mixing time** as

$$ t_{\mathrm{mix}}^{(p)}(\varepsilon) := \inf\{t \geq 0 \,:\, d^{(p)}(t) \leq \varepsilon\} \,, \qquad t_{\mathrm{mix}}^{(p)} = t_{\mathrm{mix}}^{(p)}\left(\tfrac{1}{2}\right) \,. \tag{4.44} $$

(Since $d^{(1)}(t) = 2d(t)$, using the constant $\frac{1}{2}$ in (4.44) gives $t_{\mathrm{mix}}^{(1)} = t_{\mathrm{mix}}$.) The parameter $t_{\mathrm{mix}}^{(\infty)}$ is often called the **uniform mixing time**.

Similar to $t_{\mathrm{mix}}$, since $d^{(p)}(k t_{\mathrm{mix}}^{(p)}) \leq 2^{-k}$ by submultiplicity (Lemma 4.18),

$$ t_{\mathrm{mix}}^{(p)}(\varepsilon) \leq \lceil \log_2 \varepsilon^{-1} \rceil t_{\mathrm{mix}}^{(p)} \,. $$

**Exercises**

EXERCISE 4.1. Prove that

$$
\begin{aligned}
d(t) &= \sup_{\mu} \left\|\mu P^t - \pi\right\|_{\mathrm{TV}} \,, \\
\bar{d}(t) &= \sup_{\mu,\nu} \left\|\mu P^t - \nu P^t\right\|_{\mathrm{TV}} \,,
\end{aligned}
$$

where $\mu$ and $\nu$ vary over probability distributions on a finite set $\mathcal{X}$.

EXERCISE 4.2. Let $P$ be the transition matrix of a Markov chain with state space $\mathcal{X}$ and let $\mu$ and $\nu$ be any two distributions on $\mathcal{X}$. Prove that

$$ \|\mu P - \nu P\|_{\mathrm{TV}} \leq \|\mu - \nu\|_{\mathrm{TV}} \,. $$

(This in particular shows that $\left\|\mu P^{t+1} - \pi\right\|_{\mathrm{TV}} \leq \|\mu P^t - \pi\|_{\mathrm{TV}}$, that is, advancing the chain can only move it closer to stationarity.)

Deduce that for any $t \geq 0$,

$$ d(t + 1) \leq d(t), \quad \text{and} \quad \bar{d}(t + 1) \leq \bar{d}(t) \,. $$

EXERCISE 4.3. Prove that if $t, s \geq 0$, then $d(t + s) \leq d(t)\bar{d}(s)$. Deduce that if $k \geq 2$, then $t_{\mathrm{mix}}(2^{-k}) \leq (k - 1)t_{\mathrm{mix}}$.

EXERCISE 4.4. For $i = 1, \ldots, n$, let $\mu_i$ and $\nu_i$ be measures on $\mathcal{X}_i$, and define measures $\mu$ and $\nu$ on $\prod_{i=1}^{n} \mathcal{X}_i$ by $\mu := \prod_{i=1}^{n} \mu_i$ and $\nu := \prod_{i=1}^{n} \nu_i$. Show that

$$ \|\mu - \nu\|_{\mathrm{TV}} \leq \sum_{i=1}^{n} \|\mu_i - \nu_i\|_{\mathrm{TV}} \,. $$

EXERCISE 4.5. Show that for any $f : \mathcal{X} \to \mathbb{R}$, the function $p \mapsto \|f\|_p$ is non-decreasing for $p \geq 1$.

### PDF page 74 (book page 58)

**Notes**

Our exposition of the Convergence Theorem follows **Aldous and Diaconis (1986)**. Another approach is to study the eigenvalues of the transition matrix. See, for instance, **Seneta (2006)**. Eigenvalues and eigenfunctions are often useful for bounding mixing times, particularly for reversible chains, and we will study them in Chapters 12 and 13. For convergence theorems for chains on infinite state spaces, see Chapter 21.

**Aldous (1983b**, Lemma 3.5) is a version of our Lemma 4.11 and Exercise 4.2. He says all these results "can probably be traced back to Doeblin."

The winning streak example is taken from **Lovász and Winkler (1998)**.

We emphasize $\ell^p$ distances, especially for $p = 1$, but mixing time can be defined using other distances. The separation distance, defined in Chapter 6, is often used. The **Hellinger distance** $d_H$, defined as

$$ d_H(\mu, \nu) := \sqrt{\sum_{x \in \mathcal{X}} \left(\sqrt{\mu(x)} - \sqrt{\nu(x)}\right)^2} \,, \tag{4.45} $$

behaves well on products (cf. Exercise 20.7). This distance is used in Section 20.4 to obtain a good bound on the mixing time for continuous product chains.

**Further reading. Lovász (1993)** gives the combinatorial view of mixing. **Saloff-Coste (1997)** and **Montenegro and Tetali (2006)** emphasize analytic tools. **Aldous and Fill (1999)** is indispensable. Other references include **Sinclair (1993)**, **Häggström (2002)**, **Jerrum (2003)**, and, for an elementary account of the Convergence Theorem, **Grinstead and Snell (1997**, Chapter 11).

**Complements.** The result of Lemma 4.13 generalizes to transitive Markov chains, which we defined in Section 2.6.2.

LEMMA 4.16. *Let $P$ be the transition matrix of a transitive Markov chain with state space $\mathcal{X}$, let $\widehat{P}$ be its time reversal, and let $\pi$ be the uniform distribution on $\mathcal{X}$. Then*

$$ \left\|\widehat{P}^t(x, \cdot) - \pi\right\|_{\mathrm{TV}} = \left\|P^t(x, \cdot) - \pi\right\|_{\mathrm{TV}} \,. \tag{4.46} $$

PROOF. Since our chain is transitive, for every $x, y \in \mathcal{X}$ there exists a bijection $\varphi_{(x,y)} : \mathcal{X} \to \mathcal{X}$ that carries $x$ to $y$ and preserves transition probabilities.

Now, for any $x, y \in \mathcal{X}$ and any $t$,

$$ \sum_{z \in \mathcal{X}} \left|P^t(x, z) - |\mathcal{X}|^{-1}\right| = \sum_{z \in \mathcal{X}} \left|P^t(\varphi_{(x,y)}(x), \varphi_{(x,y)}(z)) - |\mathcal{X}|^{-1}\right| \tag{4.47} $$

$$ = \sum_{z \in \mathcal{X}} \left|P^t(y, z) - |\mathcal{X}|^{-1}\right| \,. \tag{4.48} $$

Averaging both sides over $y$ yields

$$ \sum_{z \in \mathcal{X}} \left|P^t(x, z) - |\mathcal{X}|^{-1}\right| = \frac{1}{|\mathcal{X}|} \sum_{y \in \mathcal{X}} \sum_{z \in \mathcal{X}} \left|P^t(y, z) - |\mathcal{X}|^{-1}\right| \,. \tag{4.49} $$

Because $\pi$ is uniform, we have $P(y, z) = \widehat{P}(z, y)$, and thus $P^t(y, z) = \widehat{P}^t(z, y)$. It follows that the right-hand side above is equal to

$$ \frac{1}{|\mathcal{X}|} \sum_{y \in \mathcal{X}} \sum_{z \in \mathcal{X}} \left|\widehat{P}^t(z, y) - |\mathcal{X}|^{-1}\right| = \frac{1}{|\mathcal{X}|} \sum_{z \in \mathcal{X}} \sum_{y \in \mathcal{X}} \left|\widehat{P}^t(z, y) - |\mathcal{X}|^{-1}\right| \,. \tag{4.50} $$

### PDF page 75 (book page 59)

By Exercise 2.8, $\widehat{P}$ is also transitive, so (4.49) holds with $\widehat{P}$ replacing $P$ (and $z$ and $y$ interchanging roles). We conclude that

$$ \sum_{z \in \mathcal{X}} \left|P^t(x, z) - |\mathcal{X}|^{-1}\right| = \sum_{y \in \mathcal{X}} \left|\widehat{P}^t(x, y) - |\mathcal{X}|^{-1}\right| \,. \tag{4.51} $$

Dividing by 2 and applying Proposition 4.2 completes the proof. $\blacksquare$

REMARK 4.17. The proof of Lemma 4.13 established an exact correspondence between forward and reversed trajectories, while that of Lemma 4.16 relied on averaging over the state space.

The distances $d^{(p)}$ are all submultiplicative, which diminishes the importance of the constant $\frac{1}{2}$ in the definition (4.44).

LEMMA 4.18. *The distance $d^{(p)}$ is submultiplicative:*

$$ d^{(p)}(s + t) \leq d^{(1)}(s)d^{(p)}(t) \leq d^{(p)}(s)d^{(p)}(t) \,. \tag{4.52} $$

PROOF. Hölder's Inequality implies that if $p$ and $q$ satisfy $1/p + 1/q = 1$, then

$$ \|g\|_p = \max_{\|f\|_q \leq 1} \left| \sum_{x \in \mathcal{X}} f(x)g(x)\pi(x) \right| \,. \tag{4.53} $$

(See, for example, Proposition 6.13 of **Folland (1999)**.) When $p = q = 2$, (4.53) is a consequence of Cauchy-Schwarz, while for $p = \infty, q = 1$ and $p = 1, q = \infty$, this is elementary. From (4.53) and the definition (4.36), it follows that

$$
\begin{aligned}
d^{(p)}(t) &= \max_{x \in \mathcal{X}} \max_{\|f\|_q \leq 1} \left| \sum_{y \in \mathcal{X}} f(y)[q_t(x, y) - 1]\pi(y) \right| \\
&= \max_{x \in \mathcal{X}} \max_{\|f\|_q \leq 1} |P^t f(x) - \pi(f)| = \max_{\|f\|_q \leq 1} \|P^t f - \pi(f)\|_\infty \,.
\end{aligned}
\tag{4.54}
$$

Thus, for every function $g : \mathcal{X} \to \mathbb{R}$,

$$ \|P^s g - \pi(g)\|_\infty = \|P^s(g/\|g\|_q) - \pi(g/\|g\|_q)\|_\infty \cdot \|g\|_q \leq d^{(p)}(s)\|g\|_q \,. $$

Suppose that $\|f\|_q \leq 1$. Applying this inequality with $g = P^t f - \pi(f)$ and $p = 1$, and then applying (4.54), yields

$$ \|P^{t+s} f - \pi(f)\|_\infty \leq d^{(1)}(s)\|P^t f - \pi(f)\|_\infty \leq d^{(1)}(s)d^{(p)}(t) \,. $$

Maximizing over such $f$, using (4.54) with $t + s$ in place of $t$, we obtain (4.52). $\blacksquare$

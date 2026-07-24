# Chapter 5 — Change of measure and Girsanov theorem
*(PDF pages 151–190; book pages 145–184)*

### PDF page 151 (book page 145)

# Chapter 5 — Change of measure and Girsanov theorem

**5.1 Absolutely continuous measures**

In order to state the Girsanov theorem in the next section, we will need to discuss absolute continuity and singularity of measures. For measures on discrete (countable) spaces, this is an elementary idea, but it is more subtle for uncountable spaces. We assume that we have a probability space $(\Omega, \mathcal{F})$ where $\Omega$ is the space of outcomes (sometimes called the *sample space*) and $\mathcal{F}$ is the collection of events. An event is a subset of $\Omega$, and we assume that the set of events forms a $\sigma$-algebra (see Section 1.1). A *(positive) measure* is a function $\mu : \mathcal{F} \to [0, \infty]$ such that $\mu(\emptyset) = 0$ and if $A_1, A_2, \ldots$ are disjoint,

$$ \mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n). $$

The measure $\mu$ is a *probability (measure)* if $\mu(\Omega) = 1$.

**Definition** Suppose $\mu, \nu$ are measures on $(\Omega, \mathcal{F})$.

- $\nu$ is *absolutely continuous* with respect to $\mu$, written $\nu \ll \mu$, if for every $E \in \mathcal{F}$, if $\mu(E) = 0$, then $\nu(E) = 0$.

- $\mu$ and $\nu$ are *mutually absolutely continuous* or *equivalent* measures if $\nu \ll \mu$ and $\mu \ll \nu$.

### PDF page 152 (book page 146)

- $\mu$ and $\nu$ are *singular* measures, written $\mu \perp \nu$, if there exists an event $E \in \mathcal{F}$ with $\mu(E) = 0$ and $\nu(\Omega \setminus E) = 0$.

**Example 5.1.1.** Suppose $\Omega$ is a countable set and $\mathcal{F}$ is the collection of all subsets of $\Omega$. If $p : \Omega \to [0, \infty)$ is a function, then there is a corresponding measure $\mu$ defined by

$$ \mu(E) = \sum_{\omega \in E} p(\omega). $$

Suppose $\nu$ is another measure given by the function $q$. Let

$$ A_\mu = \{\omega : p(\omega) > 0\}, \quad A_\nu = \{\omega : q(\omega) > 0\}. $$

Then $\nu \ll \mu$ if and only if $A_\nu \subset A_\mu$, and

$$ q(\omega) = \frac{d\nu}{d\mu}(\omega)\, p(\omega), \quad \omega \in \Omega, $$

where $d\nu/d\mu$ is defined on $A_\mu$ by

$$ \frac{d\nu}{d\mu}(\omega) = \frac{q(\omega)}{p(\omega)}. $$

Note that for any event $E$,

$$ \nu(E) = \sum_{\omega \in E} \frac{d\nu}{d\mu}(\omega)\, p(\omega). $$

In this case, $\nu$ and $\mu$ are equivalent if $A_\nu = A_\mu$, and $\nu \perp \mu$ if $A_\nu \cap A_\mu = \emptyset$.

**Example 5.1.2.** Suppose $\mu$ denotes Lebesgue measure on $\mathbb{R}$,

$$ \mu(A) = \int_A d\mu = \int_A dx = \text{length}(A), $$

and $X$ is a continuous random variable with density $f$. Let $P_X$ denote the distribution of $X$, that is, the probability measure on $\mathbb{R}$ given by

$$ P_X(A) = \mathbb{P}\{X \in A\} = \int_A f(x)\, dx = \int_A f\, d\mu. $$

Then $P_X \ll \mu$ and we can write

$$ P_X(A) = \int_A \frac{dP_X}{d\mu}\, d\mu \quad \text{where} \quad \frac{dP_X}{d\mu} = f. $$

### PDF page 153 (book page 147)

If $f(x) > 0$ for all $x$, then $P_X(A) > 0$ whenever $\mu(A) > 0$ and hence $\mu \ll P_X$. If $Y$ is another continuous random variable with density $g$, let

$$ A_X = \{x : f(x) > 0\}, \quad A_Y = \{y : g(y) > 0\}. $$

If $A_Y \subset A_X$, then $P_Y \ll P_X$ and we can write

$$ \mathbb{P}\{Y \in A\} = \int_A g\, d\mu = \int_A \frac{g}{f}\, f\, d\mu = \int_A \frac{dP_Y}{dP_X}\, dP_X, $$

where

$$ \frac{dP_Y}{dP_X} = \frac{g}{f}. $$

If $A_X \cap A_Y = \emptyset$, then $P_X \perp P_Y$.

**Example 5.1.3.** Suppose $X$ is a discrete random variable taking values in the countable set $A$ and $Y$ is a continuous random variable with density $g$. If $P_X, P_Y$ denote the distributions, then $P_X \perp P_Y$. Indeed,

$$ P_X(\mathbb{R} \setminus A) = 0, \quad P_Y(A) = 0. $$

These examples demonstrate the following theorem whose proof can be found in any book on measure theory. A measure $\mu$ is *$\sigma$-finite* if we can write

$$ \Omega = \bigcup_{n=1}^{\infty} A_n, $$

where $\mu(A_n) < \infty$ for each $n$.

**Theorem 5.1.1** (Radon-Nikodym Theorem)**.** *Suppose $\mu, \nu$ are $\sigma$-finite measures on $(\Omega, \mathcal{F})$ with $\nu \ll \mu$. Then there exists a function $f$ such that for every $E$,*

$$ \nu(E) = \int_E f\, d\mu. \tag{5.1} $$

The function $f$ is called the *Radon-Nikodym derivative* of $\nu$ with respect to $\mu$ and is denoted

$$ f = \frac{d\nu}{d\mu}. $$

Roughly speaking, the $\nu$ measure of a point $x$ is $(d\nu/d\mu)(x)$ times the $\mu$ measure of $x$. This interpretation is precise in the case of discrete measures,

### PDF page 154 (book page 148)

such as in Example 5.1.1, but does not make precise sense when the point $x$ gets zero measure in both measures. Example 5.1.2 shows that this subtlety is something we are already familiar with. If $\mu$ denotes length, then the density $f = dP_X/d\mu$ of a continuous random variable can be interpreted as saying that the probability of obtaining a value in $[x, x + dx]$ is $f(x)$ times $dx$, the length of $[x, x + dx]$.

If $(\Omega, \mathcal{F}, P)$ is a probability space, and $Q$ is a probability measure with $Q \ll P$, then the Radon-Nikodym derivative

$$ X = \frac{dQ}{dP} $$

is a nonnegative random variable with $\mathbb{E}[X] = 1$. If $E$ is an event, then (5.1) can be written as

$$ Q(E) = \mathbb{E}_P\left[X\,1_E\right]. \tag{5.2} $$

Here $\mathbb{E}_P$ denotes expectation *using the probability measure $P$*. (Up to now, we have been considering a single probability measure $\mathbb{P}$ on a space and using $\mathbb{E}$ to denote expectation with respect to it. Since we are now going to consider different measures on the same space, we adopt the notation $\mathbb{E}_P$ to denote expectations using the measure $P$.) It is not hard to extend the relation (5.2) to give

$$ \mathbb{E}_Q[Y] = \mathbb{E}_P\left[Y\,\frac{dQ}{dP}\right]. $$

**Example 5.1.4.** Suppose $(\Omega, \mathcal{F}, \mathbb{P})$ is a probability space, and $\mathcal{G} \subset \mathcal{F}$ is a sub $\sigma$-algebra. As before, we think of $\mathcal{G}$ as "partial information". Let $X$ be a nonnegative, integrable $\mathcal{F}$-measurable random variable. Then

$$ Q(A) = \mathbb{E}\left[1_A\,X\right], \quad A \in \mathcal{G}, $$

defines a measure on $(\Omega, \mathcal{G})$ that satisfies $Q \ll \mathbb{P}$. Therefore, there exists a $\mathcal{G}$-*measurable* random variable $Y$ such that for all $A \in \mathcal{G}$,

$$ Q(A) = \mathbb{E}\left[1_A\,Y\right]. $$

This random variable $Y$ is the conditional expectation $E(X \mid \mathcal{G})$ as defined in Section 1.1.

**Example 5.1.5.** Let the set of outcomes $\Omega$ be the set of continuous functions $f : [0, 1] \to \mathbb{R}$. If $B_t$ denotes a Brownian motion with drift zero and variance

### PDF page 155 (book page 149)

$\sigma^2$, there is a measure $P_\sigma$ on $\Omega$ called *Wiener measure (with variance $\sigma^2$)*. We think of $P_\sigma$ as the distribution of the "function-valued" random variable $t \mapsto B_t$. If $V$ is a subset of $\Omega$, then $P_\sigma(V)$ is the probability that the function $t \mapsto B_t$ lies in $V$. We claim that if $\sigma \neq \sigma'$, then $P_\sigma \perp P_{\sigma'}$. In order to show this, we need to find an event $E$ such that $P_\sigma(E) = 1, P_{\sigma'}(E) = 0$. Let $E_r$ denote the set of functions $f$ such that

$$ \lim_{n \to \infty} \sum_{j=1}^{2^n} \left[ f\left(\frac{j}{2^n}\right) - f\left(\frac{j-1}{2^n}\right) \right]^2 = r^2. $$

Using what we know about the quadratic variation, we see that

$$ P_\sigma(E_\sigma) = 1, \quad P_{\sigma'}(E_{\sigma'}) = 1. $$

---

Let $\Omega$ denote the set of continuous functions $f : [0, 1] \to \mathbb{C}$ which is a Banach space (complete, normed, metric space) under the norm

$$ \|f\| = \max\{|f(s)| : 0 \le s \le 1\}. $$

Let $\mathcal{F}$ denote the corresponding Borel $\sigma$-algebra, that is, the smallest $\sigma$-algebra under which all the open sets under $\|\cdot\|$ are measurable. The measures $P_\sigma$ are defined on $(\Omega, \mathcal{F})$. It is easy to check that the functions $\Theta_s(f) = f(s)$ are measurable functions on this space, and hence so are the functions

$$ \Psi_n(f) = \sum_{j=1}^{2^n} \left[ f\left(\frac{j}{2^n}\right) - f\left(\frac{j-1}{2^n}\right) \right]^2, $$

and the sets

$$ E_r = \left\{ f : \lim_{n \to \infty} \Psi_n(f) = r^2 \right\}. $$

We proved that $P_\sigma(E_\sigma) = 1$ in Theorem 2.8.2.

One rarely needs to deal with measures that are not $\sigma$-finite, but the Radon-Nikodym derivative does not hold for such measures. For example, if $\mu$ is counting measure and $\nu$ is Lebesgue measure, both on $\mathbb{R}$, then $\nu \ll \mu$, but there is no $f$ such that (5.1) holds.

---

### PDF page 156 (book page 150)

**5.2 Giving drift to a Brownian motion**

As we have already noted, there are two ways to take a fair game and make it unfair or vice versa:

- Play the game and then add a deterministic amount in one direction.

- Change the probabilities of the outcome.

We will consider these methods in the case of a standard Brownian motion $B_t$. For the first method, we can define a Brownian motion with drift $m$, by setting

$$ W_t = mt + B_t. $$

We will now consider the second way by changing the probabilities. We have already motivated this with a binomial approximation in (4.9), but in this section we will transform the game directly using the Brownian motion.

Suppose that $B_t$ is defined on the probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with a filtration $\{\mathcal{F}_t\}$. To change the probability is to consider a different measure $Q$ instead of $\mathbb{P}$. Let

$$ M_t = e^{mB_t - \frac{m^2 t}{2}}. \tag{5.3} $$

We have seen that $M_t$ is a martingale. In fact (see (3.20)), Itô's formula shows that $M_t$ satisfies

$$ dM_t = m\,M_t\,dB_t, \quad M_0 = 1. $$

For each event $V$ that is $\mathcal{F}_t$ measurable, we define

$$ Q_t(V) = \mathbb{E}\left[1_V\,M_t\right]. $$

In other words, on the probability space $(\Omega, \mathcal{F}_t, \mathbb{P})$,

$$ \frac{dQ_t}{d\mathbb{P}} = M_t. $$

If $s < t$ and $V$ is $\mathcal{F}_s$-measurable, then it is also $\mathcal{F}_t$-measurable. In this case, $Q_s(V) = Q_t(V)$ as can be seen in the calculation

$$ Q_t(V) = \mathbb{E}\left[1_V\,M_t\right] = \mathbb{E}\left[E(1_V\,M_t \mid \mathcal{F}_s)\right] $$

$$ = \mathbb{E}\left[1_V\,E(M_t \mid \mathcal{F}_s)\right] = \mathbb{E}\left[1_V\,M_s\right] = Q_s(V). \tag{5.4} $$

Hence we can write just $Q$ for the measure.

We claim that

### PDF page 157 (book page 151)

- The process $t \mapsto B_t$, *under the measure $Q$*, is a Brownian motion with drift $m$ and $\sigma^2 = 1$.

We prove this by showing it satisfies the conditions to be a Brownian motion. The continuity of paths is immediate as well as $B_0 = 0$. To show the rest, it suffices to show that if $s, t \geq 0$, then $B_{t+s} - B_s$ is independent of $\mathcal{F}_s$ with a normal distribution with mean $mt$ and variance $t$. We can establish this by showing it has the (conditional) moment generating function

$$ E_Q \left( \exp\{\lambda(B_{t+s} - B_s)\} \mid \mathcal{F}_s \right) = e^{\lambda mt}\, e^{\lambda^2 t/2}. \tag{5.5} $$

Here we are writing $E_Q$ to denote that the conditional expectation is taken using the measure $Q$. To establish (5.5), we need to show that if $V$ is $\mathcal{F}_s$-measurable, then

$$ \begin{aligned} \mathbb{E}_Q \left[ 1_V \, \exp\{\lambda(B_{t+s} - B_s)\} \right] &= \mathbb{E}_Q \left[ 1_V \, e^{\lambda mt}\, e^{\lambda^2 t/2} \right] \\ &= e^{\lambda mt}\, e^{\lambda^2 t/2}\, Q(V), \end{aligned} $$

or equivalently, by the definition of $\mathbb{E}_Q$,

$$ \mathbb{E} \left[ 1_V \, \exp\{\lambda(B_{t+s} - B_s)\}\, M_{t+s} \right] = e^{\lambda mt}\, e^{\lambda^2 t/2}\, \mathbb{E}[1_V \, M_s]. $$

Note that if $Y = B_{t+s} - B_s$, then $Y$ is independent of $\mathcal{F}_s$ and

$$ \begin{aligned} E \left( e^{\lambda Y}\, M_{t+s} \mid \mathcal{F}_s \right) &= M_s\, e^{-m^2 t/2} E \left( e^{\lambda Y}\, e^{mY} \mid \mathcal{F}_s \right) \\ &= M_s\, e^{-m^2 t/2} \mathbb{E} \left[ e^{(\lambda+m)Y} \right] \\ &= M_s\, e^{-m^2 t/2}\, e^{(\lambda+m)^2 t/2} \\ &= M_s\, e^{\lambda^2 t/2}\, e^{\lambda mt}. \end{aligned} $$

Therefore, if $V$ is $\mathcal{F}_s$-measurable,

$$ \begin{aligned} \mathbb{E} & \left[ 1_V \, \exp\{\lambda(B_{t+s} - B_s)\}\, M_{t+s} \right] \\ &= \mathbb{E} \left[ E(1_V \, \exp\{\lambda(B_{t+s} - B_s)\}\, M_{t+s} \mid \mathcal{F}_s) \right] \\ &= \mathbb{E} \left[ 1_V \, E(\exp\{\lambda(B_{t+s} - B_s)\}\, M_{t+s} \mid \mathcal{F}_s) \right] \\ &= e^{\lambda^2 t/2}\, e^{\lambda mt}\, \mathbb{E}[1_V \, M_s]. \end{aligned} $$

**Example 5.2.1.** Suppose $X_t$ is a geometric Brownian motion satisfying

$$ dX_t = X_t \left[ m\, dt + \sigma\, dB_t \right], $$

### PDF page 158 (book page 152)

where $B_t$ is a standard Brownian motion defined on the probability space $(\Omega, \mathcal{F}, \mathbb{P})$. If $r \in \mathbb{R}$, then we can find a new probability measure $Q$ such that

$$ dB_t = r\, dt + dW_t, $$

where $W_t$ is a Brownian motion with respect to $Q$. Then,

$$ dX_t = X_t \left[ (m + \sigma r)\, dt + \sigma\, dW_t \right]. $$

Hence with respect to $Q$, $X_t$ is a geometric Brownian motion with the same volatility but a new drift. From this we can see that the measures for geometric Brownian motions *with the same $\sigma$* are equivalent.

**Example 5.2.2.** We compute a quantity for Brownian motion with drift by using a standard Brownian motion. Suppose $B_t$ is a standard Brownian motion, $a > 0$, $m \in \mathbb{R}$, and $M_t$ is the martingale in (5.3). Let $T_a = \inf\{t : B_t = a\}$. Then under the new measure $Q$, $B_t$ is a Brownian motion with drift $m$. Note that

$$ Q\{T_a < \infty\} = \mathbb{E} \left[ M_{T_a}\, 1\{T_a < \infty\} \right] = \mathbb{E} \left[ M_{T_a} \right]. $$

Here the expectation $\mathbb{E}$ is with respect to the original measure under which $B$ is a standard Brownian motion; the second equality follows from the fact that $\mathbb{P}\{T_a < \infty\} = 1$. Therefore,

$$ \begin{aligned} Q\{T_a < \infty\} &= \mathbb{E} \left[ \exp\left\{ mB_{T_a} - \frac{m^2\, T_a}{2} \right\} \right] \\ &= e^{am}\, \mathbb{E} \left[ \exp\left\{ -\frac{m^2\, T_a}{2} \right\} \right]. \end{aligned} $$

In Example 2.7.1 we computed the density of $T_a$ for Brownian motion. Given this we could compute the expectation on the right-hand side. However we will choose a different method. We know that driftless Brownian motion will hit the line $y = a$ with probability one, and hence so will Brownian motion with $m > 0$. Therefore, if $m > 0$, $Q\{T_a < \infty\} = 1$ and

$$ \mathbb{E} \left[ \exp\left\{ -\frac{m^2\, T_a}{2} \right\} \right] = e^{-am}. $$

If the Brownian motion has drift $-m$, then

$$ Q\{T_a < \infty\} = e^{-am}\, \mathbb{E} \left[ \exp\left\{ -\frac{m^2\, T_a}{2} \right\} \right] = e^{-2am}. $$

### PDF page 159 (book page 153)

# 5.3 Girsanov theorem

The Girsanov theorem describes the probability measure one obtains by "weighting" or "tilting" the measure of a Brownian motion by a martingale. One example was given in the previous section where the martingale was

$$ M_t = e^{mB_t - (m^2 t/2)}, \tag{5.6} $$

and in the new measure, $B_t$ was a Brownian motion with drift. We will generalize this idea here.

Suppose $M_t$ is a nonnegative martingale satisfying the exponential SDE

$$ dM_t = A_t\, M_t\, dB_t, \qquad M_0 = 1, \tag{5.7} $$

where $B_t$ is a standard Brownian motion. The solution to this equation was given in (3.20),

$$ M_t = e^{Y_t} \quad \text{where} \quad Y_t = \int_0^t A_s\, dB_s - \frac{1}{2} \int_0^t A_s^2\, ds. \tag{5.8} $$

For many applications it suffices to consider the equation (5.7) and not worry about the form of the solution (5.8). Solutions to (5.7) are local martingales, but as we have seen, they might not be martingales. For now we will *assume* that $M_t$ is a martingale. In that case, we can define a probability measure $\mathbb{P}^*$ by saying that if $V$ is an $\mathcal{F}_t$-measurable event, then

$$ \mathbb{P}^*(V) = \mathbb{E} \left[ 1_V \, M_t \right]. \tag{5.9} $$

In other words, if we consider $\mathbb{P}, \mathbb{P}^*$ as being defined on $\mathcal{F}_t$-measurable events,

$$ \frac{d\mathbb{P}^*}{d\mathbb{P}} = M_t. $$

If $s < t$ and $V$ is $\mathcal{F}_s$-measurable, then $V$ is also $\mathcal{F}_t$-measurable. Hence, in order for the above definition to be consistent, we need that for such $V$,

$$ \mathbb{E} \left[ 1_V \, M_s \right] = \mathbb{E} \left[ 1_V \, M_t \right]. $$

Indeed, this holds by the computation (5.4) which only uses the fact that $M$ is a martingale and $V$ is $\mathcal{F}_s$-measurable. We write $\mathbb{E}^*$ for expectations with respect to $\mathbb{P}^*$. If $X$ is $\mathcal{F}_t$-measurable, then

$$ \mathbb{E}^*[X] = \mathbb{E} \left[ X\, M_t \right]. $$

### PDF page 160 (book page 154)

**Theorem 5.3.1** (Girsanov Theorem)**.** *Suppose $M_t$ is a nonnegative martingale satisfying* (5.7)*, and let $\mathbb{P}^*$ be the probability measure defined in* (5.9)*. If*

$$ W_t = B_t - \int_0^t A_s\,ds, $$

*then with respect to the measure $\mathbb{P}^*$, $W_t$ is a standard Brownian motion. In other words,*

$$ dB_t = A_t\,dt + dW_t, $$

*where $W$ is a $\mathbb{P}^*$-Brownian motion.*

In other words, if we weight the probability measure $\mathbb{P}$ by the martingale, then in the new measure $\mathbb{P}^*$, the Brownian motion acquires a drift $A_t$. The example of the previous section is the martingale (5.6) with $A_t \equiv m$ and a constant drift $m$ is obtained.

Let us give a heuristic derivation of Girsanov's theorem using a binomial approximation. Suppose $\Delta t$ is given. In the binomial approximation to $\mathbb{P}$, we are equally likely to go up and down,

$$ \mathbb{P}\left\{ B(t + \Delta t) - B(t) = \pm\sqrt{\Delta t} \mid B(t) \right\} = \frac{1}{2}. $$

The binomial approximation to (5.7) is

$$ \mathbb{P}\left\{ M(t + \Delta t) = M(t) \left[ 1 \pm A(t)\sqrt{\Delta t} \right] \mid B(t) \right\} = \frac{1}{2}. $$

Therefore, in the weighted measure $\mathbb{P}^*$ the probability of a jump of $\pm\sqrt{\Delta}$ should be proportional to $1 \pm A(t)\sqrt{\Delta t}$. Since the sum of the two probabilities equals one, we see that

$$ \mathbb{P}^*\left\{ B(t + \Delta t) - B(t) = \pm\sqrt{\Delta t} \mid B(t) \right\} = \frac{1}{2}\left[ 1 \pm A(t)\sqrt{\Delta t} \right]. $$

As we saw in Section 4.4, this implies that

$$ E^*[B(t + \Delta t) - B(t) \mid B(t)] = A(t)\,\Delta t, $$

that is, in the probability measure $\mathbb{P}^*$, the process obtains a drift of $A(t)$.

The condition that $M_t$ be a martingale (and not just a local martingale) is necessary for Girsanov's theorem as we have stated it. Given only (5.7)

### PDF page 161 (book page 155)

or (5.8), it may be hard to determine if $M_t$ is a martingale, so it is useful to have a version that applies for local martingales. If we do not know $M_t$ is a martingale, we can still use Theorem 5.3.1 if we are careful to stop the process before anything bad happens. To be more precise, suppose $M_t = e^{Y_t}$ satisfies (5.8), and note that

$$ \langle Y \rangle_t = \int_0^t A_s^2\,ds. $$

Let

$$ T_n = \inf\{t : M_t + \langle Y \rangle_t = n\}, $$

and let

$$ A_t^{(n)} = \left\{ \begin{array}{ll} A_t, & t < T_n \\ 0, & t \geq T_n \end{array} \right. . $$

Then

$$ dM_{t \wedge T_n} = A_t^{(n)}\, M_{t \wedge T_n}\, dB_t, $$

which is a square integrable martingale since

$$ \begin{aligned} \mathbb{E}\left[ (M_{t \wedge T_n} - 1)^2 \right] &= \int_0^t \mathbb{E}[A_s^{(n)}\, M_{s \wedge T_n}]^2\,ds \\ &\leq n^2\,\mathbb{E}\int_0^t [A_s^{(n)}]^2\,ds \leq n^3. \end{aligned} $$

There is the corresponding measure, which we might denote by $\mathbb{P}_n^*$, which gives a drift of $A_t$ up to time $T_n$ and then proceeds with drift 0. If $n < m$, then $\mathbb{P}_n^*$ and $\mathbb{P}_m^*$ are the same measure restricted to $t \leq T_n$. Hence we can write $\mathbb{P}^*$ for a measure on $B_t, 0 \leq t < T$, where

$$ T = \lim_{n \to \infty} T_n. $$

This shows how to tilt the measure up to time $T$, There are examples such that $\mathbb{P}^*\{T < \infty\} > 0$. However, if for some fixed $t_0$, $\mathbb{P}^*\{T > t_0\} = 1$, then $M_t, 0 \leq t \leq t_0$ is a martingale. In other words, what prevents a solution to (5.7) from being a martingale is that *with respect to the new measure* $\mathbb{P}^*$, either $M_t$ or $|A_t|$ goes to infinity in finite time. We summarize with a restatement of the Girsanov theorem.

### PDF page 162 (book page 156)

**Theorem 5.3.2** (Girsanov Theorem, local martingale form)**.** *Suppose $M_t = e^{Y_t}$ satisfies* (5.7)–(5.8)*, and let*

$$ T_n = \inf\{t : M_t + |A_t| = n\}, \quad T = T_\infty = \lim_{n \to \infty} T_n. $$

*Let $\mathbb{P}^*$ be the probability measure as above. If*

$$ W_t = B_t - \int_0^t A_s\,ds, \quad 0 \leq t < T, $$

*then with respect to the measure $\mathbb{P}^*$, $W_t, t < T$ is a standard Brownian motion. In other words,*

$$ dB_t = A_t\,dt + dW_t, \quad t < T, $$

*where $W$ is a $\mathbb{P}^*$-Brownian motion. If any one of the following three conditions hold, then $M_s, 0 \leq s \leq t$, is actually a martingale:*

$$ \mathbb{P}^*\{T > t\} = 1, $$

$$ \mathbb{E}[M_t] = 1, $$

$$ \mathbb{E}\left[ \exp\left\{ \frac{\langle Y \rangle_t}{2} \right\} \right] < \infty. \tag{5.10} $$

It is not always easy to see whether or not the local martingale in (5.7) will be a martingale. However, if any one of the three conditions at the end of the theorem hold, then it is a martingale. The first condition uses $\mathbb{P}^*$, the new measure, while the expectation $\mathbb{E}$ in the other two conditions is with respect to the original measure. The relation (5.10) is called the *Novikov condition*.

Even if $M_t$ is not a martingale, since

$$ M_t = \lim_{n \to \infty} M_{t \wedge T_n}, $$

Fatou's lemma implies that

$$ \mathbb{E}\left[M_t\right] = \mathbb{E}\left[ \lim_{n \to \infty} M_{t \wedge T_n} \right] \leq \lim_{n \to \infty} \mathbb{E}[M_{t \wedge T_n}] = \mathbb{E}[M_0] = 1. $$

An extension of this argument shows that nonnegative local martingales are supermartingales, that is, if $s < t$,

$$ E[M_t \mid \mathcal{F}_s] \leq M_s. $$

### PDF page 163 (book page 157)

**Example 5.3.1.** Let $B_t$ be a standard Brownian motion with $B_0 = 1$. Let $\tau = \inf\{t : B_t = 0\}$. Then $M_t = B_{t\wedge\tau}$ is a nonnegative martingale, satisfying

$$ dM_t = dB_t = A_t\, M_t\, dB_t, \quad t < \tau, $$

where

$$ A_t = \frac{1}{M_t} = \frac{1}{B_t}. $$

If we tilt the measure using $M_t$, then

$$ dB_t = A_t\, dt + dW_t = \frac{dt}{B_t} + dW_t, $$

where $W_t$ is a standard Brownian motion in the new measure $\mathbb{P}^*$. Note that this equation gives the Bessel process that we studied in Section 4.2 with $a = 1$. Using properties of the Bessel process, we see that

$$ \mathbb{P}^*\{\tau < \infty\} = 0. $$

In other words, in the new measure the process avoids the origin.

**Example 5.3.2.** Let $B_t$ be a standard Brownian motion with $B_0 = 1$ and $r \in \mathbb{R}$. Let $\tau = \inf\{t : B_t = 0\}$. For $t < \tau$, Itô's formula gives

$$ \begin{aligned} dB_t^r &= r\, B_t^{r-1}\, dB_t + \frac{r(r-1)}{2}\, B_t^{r-2}\, dt \\ &= B_t^r\left[ \frac{r}{B_t}\, dB_t + \frac{r(r-1)}{2B_t^2}\, dt \right]. \end{aligned} $$

Let

$$ M_t = \exp\left\{ -\int_0^t \frac{r(r-1)}{2B_s^2}\, ds \right\} B_t^r. $$

The product rule shows that $M_t$ satisfies the exponential SDE

$$ dM_t = \frac{r}{B_t}\, M_t\, dB_t, \quad t < \tau. $$

Therefore,

$$ dB_t = \frac{r}{B_t}\, dt + dW_t, \quad t < \tau, $$

### PDF page 164 (book page 158)

where $W_t$ is a Brownian motion in the new measure. This equation is the Bessel equation. In particular, if $r \geq 1/2$, then $\mathbb{P}^*\{\tau = \infty\} = 1$, and using this we see that with $\mathbb{P}^*$-probability one

$$ M_t + \int_0^t A_s^2\, ds $$

is finite. Therefore, for $r \geq 1/2$, $M_t$ is a martingale.

**Example 5.3.3.** Suppose that $X_t$ satisfies

$$ dX_t = X_t\left[ m(t, X_t)\, dt + \sigma(t, X_t)\, dB_t \right], $$

where $B_t$ is a standard Brownian motion with respect to the probability measure $\mathbb{P}$. Let us assume that $\sigma(t, x) > 0$ for all $t, x$. Suppose we want to find a probability measure $\mathbb{P}^*$ that is mutually absolutely continuous with respect to $\mathbb{P}$ and such that $X_t$ is a martingale under $\mathbb{P}^*$. Then we would want

$$ dB_t = -\frac{m(t, X_t)}{\sigma(t, X_t)}\, dt + dW_t, $$

where $W_t$ is a standard Brownian motion with respect to $\mathbb{P}^*$. This would give

$$ dX_t = X_t\, \sigma(t, X_t)\, dW_t. $$

The local martingale that we need to consider is $M_t$ satisfying

$$ dM_t = -\frac{m(t, X_t)}{\sigma(t, X_t)}\, M_t\, dB_t, \quad M_0 = 1. $$

In other words,

$$ M_t = \exp\left\{ \int_0^t A_s\, dB_s - \frac{1}{2}\int_0^t A_s^2\, ds \right\}, \quad A_t = -\frac{m(t, X_t)}{\sigma(t, X_t)}. \tag{5.11} $$

While $M_t$ is a local martingale, we cannot say it is a martingale without verifying one of the conditions in Theorem 5.3.2.

**Example 5.3.4.** Suppose $X_t$ is a Bessel process satisfying

$$ dX_t = \frac{1}{X_t}\, dt + dB_t, \quad X_0 = 1, $$

### PDF page 165 (book page 159)

where $B_t$ is a standard Browian [sic] motion. In Section 4.2 it was shown that with probability one, the process $X_t$ will never reach the origin and, in fact, $X_t \to \infty$. Let

$$ M_t = \frac{1}{X_t}. $$

Using Itô's formula, we see that

$$ dM_t = -\frac{1}{X_t^2}\, dX_t + \frac{1}{X_t^3}\, d\langle X\rangle_t = -\frac{1}{X_t}\, M_t\, dB_t. $$

Therefore, $M_t$ is a local martingale with $M_0 = 1$ and we can apply the second form of the Girsanov theorem. We will ask if $M_t$ is a martingale. Indeed, one can see that it is not by noting that $M_t \to 0$ and (with some more work that we omit) $\mathbb{E}[M_t] \to 0$. If $M_t$ were a martingale, we would have $\mathbb{E}[M_t] = 1$ for all $t$. Another way to see that $M_t$ is not a martingale is to consider the measure $\mathbb{P}^*$ given by tilting by the martingale. In this measure,

$$ dB_t = -\frac{1}{X_t}\, dt + dW_t, $$

where $W_t$ is a $\mathbb{P}^*$-Brownian motion. Therefore, $dX_t = dW_t$ which says that the distribution of $X_t$ *in the measure* $\mathbb{P}^*$ is that of a standard Brownian motion. Since the Brownian motion reaches zero, we can see that with respect to $\mathbb{P}^*$, the martingale $M_t$ reaches infinity in finite time.

---

Suppose $M_t$ is a continuous, nonnegative local martingale. To show that $M_t$ is a supermartingale, suppose that $\tau_n$ is an increasing sequence of stopping times such that $M_{t\wedge\tau_n}$ is a martingale. Let $s < t$. Suppose $V$ is an $\mathcal{F}_s$-measurable event and let $V_k = V \cap \{\tau_k > s\}$. Since $M_{t\wedge\tau_n}$ is a martingale, if $n \geq k$,

$$ \mathbb{E}\left[ 1_{V_k}\, M_{t\wedge\tau_n} \right] = \mathbb{E}\left[ 1_{V_k}\, M_{s\wedge\tau_n} \right] = \mathbb{E}\left[ 1_{V_k}\, M_s \right]. $$

Hence Fatou's lemma implies that

$$ \mathbb{E}\left[ 1_{V_k}\, M_t \right] \leq \liminf_{n\to\infty} \mathbb{E}\left[ 1_{V_k}\, M_{t\wedge\tau_n} \right] = \mathbb{E}\left[ 1_{V_k}\, M_s \right]. $$

Since $\mathbb{E}\left[ 1_V\, E(M_t \mid \mathcal{F}_s) \right] = \mathbb{E}\left[ 1_V\, M_t \right]$, by letting $k \to \infty$ and using the monotone convergence theorem, we get

$$ \mathbb{E}\left[ 1_V\, E(M_t \mid \mathcal{F}_s) \right] = \mathbb{E}\left[ 1_V\, M_t \right] \leq \mathbb{E}\left[ 1_V\, M_s \right]. $$

### PDF page 166 (book page 160)

Since this holds for every $\mathcal{F}_s$-measurable event $V$, we have $E(M_t \mid \mathcal{F}_s) \leq M_s$ with probability one. Also, if $V = \{E(M_t \mid \mathcal{F}_s) < M_s\}$ and $\mathbb{P}(V) > 0$, then

$$ \mathbb{E}[M_t] = \mathbb{E}\left[1_V \, M_t\right] + \mathbb{E}\left[1_{V^c} \, M_t\right] < \mathbb{E}\left[1_V \, M_s\right] + \mathbb{E}\left[1_{V^c} \, M_s\right] = \mathbb{E}[M_s]. $$

Conversely, if $\mathbb{E}[M_t] = \mathbb{E}[M_0]$ for all $t$, then $M_t$ must be a martingale. (We emphasize that we are using the fact that $M_t \geq 0$.)

To prove the Girsanov theorem, let us first consider the case when there exists $K < \infty$ such that with probability one $|A_t| \leq K$ and $M_t \leq K$. By Theorem 4.5.2, we need only show that in the measure $\mathbb{P}^*$, $W_t$ is a continuous martingale with quadratic variation $\langle W \rangle_t = t$. Continuity and the quadratic variation calculation are immediate (since they hold with probability one in the measure $\mathbb{P}$), so all we need to show is that $W_t$ is a $\mathbb{P}^*$-martingale, that is, if $s < t$, then

$$ E_{\mathbb{P}^*}(W_t \mid \mathcal{F}_s) = W_s. $$

In other words, if $V$ is $\mathcal{F}_s$-measurable, we need to show that

$$ \mathbb{E}^* \left[1_V \, W_s\right] = \mathbb{E}^* \left[1_V \, W_t\right] , $$

which by definition means

$$ \mathbb{E} \left[1_V \, W_s \, M_s\right] = \mathbb{E} \left[1_V \, W_t \, M_t\right] . $$

In other words, we need to show that $Z_t = W_t \, M_t$ is a martingale with respect to $\mathbb{P}$. Since

$$ dW_t = -A_t \, dt + dB_t, \quad dM_t = A_t \, M_t \, dB_t, $$

the product rule gives

$$ dZ_t = W_t \, dM_t + M_t \, dW_t + d\langle W, M \rangle_t = (A_t \, W_t + 1) \, M_t \, dB_t, $$

which shows that $Z_t$ is a local martingale. Also, since $|W_t| \leq |B_t| + tK$ we see that

$$ \int_0^t \mathbb{E}[(A_s \, W_s + 1)^2 \, M_s^2] \, ds < \infty, $$

and hence $Z_t$ is a square-integrable martingale.

For more general $A_t, M_t$ we use localization with the stopping times $T_n$ as above. Note that

$$ \mathbb{E}[M_t] \geq \lim_{n \to \infty} \mathbb{E} \left[M_t \, 1\{T_n > t\}\right] = \lim_{n \to \infty} \mathbb{P}^*\{T_n > t\} = \mathbb{P}^*\{T > t\}, $$

### PDF page 167 (book page 161)

and hence if $\mathbb{P}^*\{T > t\} = 1$, then $\mathbb{E}[M_t] = 1$ and $M_s, 0 \leq s \leq t$ is a martingale.

We will now show that the Novikov condition (5.10) implies that $M$ is a martingale. For ease let $t = 1$. Let

$$ \tau_r = \inf\{t : \langle Y \rangle_t = r\}. $$

The process

$$ X_r = \int_0^{\tau_r} A_s \, dW_s $$

is a standard Brownian motion with respect to the measure $\mathbb{P}^*$. Also,

$$ Y_r = X_r + \frac{1}{2} \int_0^{\tau_r} A_s \, ds = X_r + \frac{r}{2}. $$

In particular,

$$ \max_{0 \leq s \leq \tau_r} M_s = \max_{0 \leq t \leq r} \exp\left\{ X_t + \frac{t}{2} \right\}. $$

In other words, $T = \lim T_n$ can be defined as

$$ T = \sup\{t : \langle Y \rangle_t < \infty\}. $$

Let $V$ denote the event that $\tau_r \leq 1$ for all $r < \infty$. We need to show that $\mathbb{P}^*(V) = 0$.

Let

$$ \rho_n = \min \left\{m \geq n : X_m \leq 0\right\}. $$

Since $X_m$ is a $\mathbb{P}^*$-local martingale, for each $n$, $\mathbb{P}^*[V \cap \{\rho_n < \infty\}] = \mathbb{P}^*(V)$. Also,

$$ M_{\rho_n} = \exp \left\{Y_{\rho_n}\right\} \leq e^{\rho_n/2}. $$

Let us fix $n$, let $\rho = \rho_n$, and note that

$$ \begin{aligned} \mathbb{P}^*(V) \leq \sum_{m=n}^{\infty} \mathbb{E} \left[M_m \, 1 \left\{\rho = m\right\}\right] \; &\leq \; \sum_{m=n}^{\infty} e^{m/2} \, \mathbb{P}\{\rho = m\} \\ &\leq \; \mathbb{E} \left[ e^{\langle Y \rangle_1/2} \, 1\{\rho = m\} \right]. \end{aligned} $$

We therefore, get

$$ \mathbb{P}^*(V) \leq \mathbb{E} \left[ e^{\langle Y \rangle_1/2} \, 1\{\tau_r < 1\} \right]. $$

### PDF page 168 (book page 162)

The events $\{\tau_r \leq 1\}$ shrink to a $\mathbb{P}$-null set as $r \to \infty$. The condition (5.10) implies that $e^{\langle Y \rangle_1/2}$ is integrable, and hence,

$$ \lim_{r \to \infty} \mathbb{E} \left[ e^{\langle Y \rangle_1/2} \, 1\{\tau_r \leq 1\} \right] = 0. $$

## 5.4 Black-Scholes formula

An *arbitrage* is a system that guarantees that a player (investor) will not lose money while also giving a positive probability of making money. If $P$ and $Q$ are equivalent probability measures, then an arbitrage under probability $P$ is the same as an arbitrage under probability $Q$. This holds since for equivalent probability measures

$$ P(V) = 0 \quad \text{if and only if} \quad Q(V) = 0, $$

$$ P(V) > 0 \quad \text{if and only if} \quad Q(V) > 0. $$

This observation is the main tool for the pricing of options as we now show. We will consider a simple (European) call option for a stock whose price moves according to a geometric Brownian motion.

Suppose that the stock price $S_t$ follows the geometric Brownian motion,

$$ dS_t = S_t \left[m \, dt + \sigma \, dB_t\right], \tag{5.12} $$

and there also exists a risk-free bound $R_t$ satisfying

$$ dR_t = r \, R_t \, dt, \tag{5.13} $$

that is, $R_t = e^{rt} \, R_0$. Let $T$ be a time in the future and suppose we have the option to buy a share of stock at time $T$ for strike price $K$. The value of this option at time $T$ is

$$ F(S_T) = (S_T - K)_+ = \begin{cases} (S_T - K) & \text{if } S_T > K, \\ 0 & \text{if } S_T \leq K. \end{cases} $$

The goal is to find the price $f(t, x)$ of the option at time $t < T$ given $S_t = x$.

One possibility, which is *not* the Black-Scholes solution, is to price the option by the expected value (in time $t$ dollars),

$$ \hat{f}(t, x) = \mathbb{E} \left[ e^{-r(T - t)} \, F(S_T) \mid S_t = x \right] . $$

### PDF page 169 (book page 163)

In (4.7) we showed that this function satisfies the PDE

$$ \partial_t \hat{f}(t,x) = r\,\hat{f}(t,x) - m\,x\,\hat{f}'(t,x) - \frac{\sigma^2\,x^2}{2}\,\hat{f}''(t,x). \tag{5.14} $$

Here and throughout this section we use primes for $x$-derivatives. If one sells an option at this price and uses the money to buy a bond at the current interest rate, then there is a positive probability of losing money.

The Black-Scholes approach to pricing is to let $f(t,x)$ be the value of a portfolio at time $t$, given that $S_t = x$, that can be *hedged* in order to guarantee a portfolio of value $F(S_T)$ at time $T$. By a portfolio, we mean an ordered pair $(a_t, b_t)$ where $a_t, b_t$ denote the number of units of stocks and bonds, respectively. Let $V_t$ be the value of the portfolio at time $t$,

$$ V_t = a_t\,S_t + b_t\,R_t. \tag{5.15} $$

We will manage the portfolio by switching between stocks and bonds so that, no matter how the price of the stock moves, the value at time $T$ will be

$$ V_T = (S_T - K)_+. $$

We assume that the portfolio is *self-financing*, that is, one does not add outside resources to the portfolio. The mathematical consequence of this assumption is that the change of the value of the portfolio is given only by the change of the price of the assets,

$$ dV_t = a_t\,dS_t + b_t\,dR_t. \tag{5.16} $$

It may appear at first that (5.16) is a consequence of (5.15). However, the units of the assets $a_t, b_t$ vary with time and hence we need to use the product rule. If $V_t$ is defined by (5.15), the product rule implies that

$$ d(a_t\,S_t) = a_t\,dS_t + S_t\,da_t + d\langle a, S\rangle_t, $$

$$ d(b_t\,R_t) = b_t\,dR_t + R_t\,db_t. $$

Here we use the fact that $R_t$ is differentiable in $t$ to see that $\langle b, R\rangle_t = 0$. Hence, (5.16) is a strong *assumption* about the portfolio, and we will use it to determine the price and the hedging strategy.

### PDF page 170 (book page 164)

If we assume (5.16) and plug in (5.12) and (5.13), we get

$$
\begin{aligned}
dV_t &= a_t\,S_t\,[m\,dt + \sigma\,dB_t] + b_t\,r\,R_t\,dt \\
&= a_t\,S_t\,[m\,dt + \sigma\,dB_t] + r\,[V_t - a_t\,S_t]\,dt \\
&= [m\,a_t\,S_t + r\,(V_t - a_t\,S_t)]\,dt + \sigma\,a_t\,S_t\,dB_t.
\end{aligned}
\tag{5.17}
$$

Under our definition, $V_t = f(t, S_t)$. Therefore, assuming $f$ is sufficiently differentiable, Itô's formula shows that

$$
\begin{aligned}
dV_t &= df(t, S_t) \\
&= \partial_t f(t, S_t)\,dt + f'(t, S_t)\,dS_t + \frac{1}{2}\,f''(t, S_t)\,d\langle S\rangle_t \\
&= \left[\partial_t f(t, S_t) + m\,S_t\,f'(t, S_t) + \frac{\sigma^2 S_t^2}{2}\,f''(t, S_t)\right]dt \\
&\quad + \sigma\,S_t\,f'(t, S_t)\,dB_t.
\end{aligned}
\tag{5.18}
$$

By equating the $dB_t$ terms in (5.17) and (5.18), we see that that the portfolio is given by

$$ a_t = f'(t, S_t), \qquad b_t = \frac{V_t - a_t\,S_t}{R_t}, \tag{5.19} $$

and then by equating the $dt$ terms we get the Black-Scholes equation

$$ \partial_t f(t, x) = r\,f(t, x) - r\,x\,f'(t, x) - \frac{\sigma^2\,x^2}{2}\,f''(t, x). $$

There are two things to note about this equation.

- The drift term $m$ does not appear. If we think about this, we realize why our assumptions should give us an equation independent of $m$. Our price was based on being able to hedge our portfolio so that with probability one the value at time $T$ is $(S_T - K)_+$. Geometric Brownian motions with the same $\sigma$ but different $m$ are mutually absolutely continuous and hence have the same events of probability one.

- The equation is exactly the same as (5.14) except that $m$ has been replaced with $r$. Therefore, we can write

$$ f(t, x) = \mathbb{E}\left[e^{-r(T-t)}\,F(S_t) \mid S_t = x\right], $$

where $S$ satisfies

$$ dS_t = S_t\,[r\,dt + \sigma\,dB_t]. $$

### PDF page 171 (book page 165)

Using this, one can compute $f(t, x)$ exactly; in the next section we do this and derive the *Black-Scholes formula*

$$
\begin{aligned}
f(T - t, x) = {}& x\,\Phi\!\left(\frac{\log(x/K) + (r + \frac{\sigma^2}{2})t}{\sigma\sqrt{t}}\right) \\
& - K\,e^{-rt}\,\Phi\!\left(\frac{\log(x/K) + (r - \frac{\sigma^2}{2})t}{\sigma\sqrt{t}}\right),
\end{aligned}
\tag{5.20}
$$

where $\Phi$ is the standard normal distribution function. If one knows $r$ and $\sigma$ (which from a practical perspective is a *big* assumption), one can just plug into this formula.

We can easily generalize this to the case where the stock price satisfies

$$ dS_t = S_t\,[m(t, S_t)\,dt + \sigma(t, S_t)\,dB_t], $$

$$ dR_t = r(t, S_t)\,R_t\,dt. $$

Under the assumption of a self-financing portfolio, we again get (5.17) and (5.18), and by equating coefficients we get the Black-Scholes equation

$$ \partial_t f(t, x) = r(t, x)\,f(t, x) - r(t, x)\,x\,f'(t, x) - \frac{\sigma(t, x)^2\,x^2}{2}\,f''(t, x). \tag{5.21} $$

As before, the drift term $m(t, x)$ does not appear in the equation. The function $f$ can be given by

$$ f(t, x) = \mathbb{E}\left[(R_t/R_T)\,F(S_T) \mid S_t = x\right], $$

where $S_t, R_t$ satisfy

$$ dS_t = S_t\,[r(t, S_t)\,dt + \sigma(t, S_t)\,dB_t], $$

$$ dR_t = r(t, S_t)\,R_t\,dt. $$

Mathematical justification of this arguments requires sufficient assumptions on $m$ and $\sigma$ such that the equation (5.21) has a solution. Finding explicit solutions to such equations is often impossible, but one can either solve the PDE numerically or do Monte Carlo simulations of the associated diffusion process $S_t$.

### PDF page 172 (book page 166)

**5.5 Martingale approach to Black-Scholes equation**

We will give a different approach to deriving the Black-Scholes formula. Suppose for the moment that the risk-free bond has rate $r(t,x)$ and that the volatility is given by $\sigma(t,x)$. If $R_t$ denotes the value of the bond at time $t$, then

$$ dR_t = r(t, S_t)\, R_t\, dt, \qquad R_t = R_0 \exp\left\{ \int_0^t r(s, S_s)\, ds \right\}. $$

As explained in the previous section, if we want a strategy to hedge a portfolio so that its value is determined at time $T$, then the strategy must be independent of the drift coefficient $m(t,x)$. For this reason, we may assume that the stock price satisfies

$$ dS_t = S_t \left[ r(t, S_t)\, dt + \sigma(t, S_t)\, dB_t \right], \tag{5.22} $$

and then the value of the portfolio at time $t$ satisfies

$$ V_t = f(t, S_t) = E_Q \left[ (R_t/R_T)\, F(S_T) \mid S_t \right] = E_Q \left[ (R_t/R_T)\, F(S_T) \mid \mathcal{F}_t \right]. $$

We write $\mathbb{E}_Q, E_Q$ to emphasize that the expectations are taken with respect to the measure under which $S_t$ satisfies (5.22).

Let $\tilde{S}_t = S_t/R_t, \tilde{V}_t = V_t/R_t$ be the stock price and portfolio value, respectively, discounted by the bond rate. The product rule shows that $\tilde{S}_t$ satisfies

$$ d\tilde{S}_t = \sigma(t, R_t)\, \tilde{S}_t\, dB_t. $$

In other words (under some growth restrictions on $\sigma$, for example, if $\sigma$ is uniformly bounded), $\tilde{S}_t$ is a martingale. Also,

$$ \tilde{V}_t = V_t/R_t = R_t^{-1}\, E_Q \left( (R_t/R_T)\, F(S_T) \mid \mathcal{F}_t \right) $$

$$ = E_Q \left( R_T^{-1}\, F(S_T) \mid \mathcal{F}_t \right) = E_Q[\tilde{V}_T \mid \mathcal{F}_t]. $$

We have just demonstrated the following principle.

**Theorem 5.5.1.** *Suppose $S_t$ satisfies*

$$ dS_t = S_t \left[ m(t, S_t)\, dt + \sigma(t, S_t)\, dB_t \right], $$

### PDF page 173 (book page 167)

*and a risk-free bond $R_t$ is available at rate $r(t, S_t)$,*

$$ dR_t = r(t, S_t)\, R_t\, dt. $$

*Suppose that the Brownian motion is defined on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ and that there exists a probability measure $Q$ that is mutually absolutely continuous with respect to $\mathbb{P}$ such that under $Q$, the discounted stock price $\tilde{S}_t = S_t/R_t$ is a martingale. Suppose there is an option at time $T$ with value $F(S_T)$ such that $\mathbb{E}_Q[R_T^{-1} \, |F(S_T)|] < \infty$. Then the arbitrage-free price of the option at time $t$ is*

$$ V_t = R_t\, E_Q \left( R_T^{-1}\, F(S_T) \mid \mathcal{F}_t \right). \tag{5.23} $$

A nice thing about this formulation is that $V_T = F(S_T)$ follows directly from the formula. However, unlike the previous approach, we do not immediately get the expression for the portfolio needed to hedge the option.

**Example 5.5.1.** We will derive the Black-Scholes formula leaving some of the calculus calculations to Exercise 5.11. Suppose that $r, \sigma$ are constants and $F(S_T) = (S_T - K)_+$. The discounted values are $\tilde{S}_t = e^{-rt}S_t, \tilde{V}_t = e^{-rt}\, V_t$ and

$$ \tilde{V}_T = e^{-rT}\, F(S_T) = e^{-rT}\, (S_T - K)_+ = (\tilde{S}_T - \tilde{K})_+, $$

where $\tilde{K} = e^{-rT}K$. Under the measure $Q$, $\tilde{S}_t$ satisfies

$$ d\tilde{S}_t = \sigma\, \tilde{S}_t\, dB_t, $$

which implies that

$$ \begin{aligned} \tilde{S}_T &= \tilde{S}_t \exp\left\{ \int_t^T \sigma\, dB_s - \frac{1}{2} \int_t^T \sigma^2\, ds \right\} \\ &= \tilde{S}_t \exp\left\{ \sigma(B_T - B_t) - \frac{\sigma^2(T - t)}{2} \right\}. \end{aligned} $$

In other words, the conditional distribution of $\tilde{S}_T$ given $\tilde{S}_t$ is that of

$$ Z = \exp\left\{ aN + y \right\}, $$

where $a = \sigma\sqrt{T - t}$, $N$ is a standard normal random variable, and

$$ y = \log \tilde{S}_t - \frac{a^2}{2}. $$

### PDF page 174 (book page 168)

Straightforward calculus shows that $Z$ has a density

$$ g(z) = \frac{1}{az}\, \phi\left( \frac{-y + \log z}{a} \right), $$

where $\phi$ is the standard normal density, and hence

$$ \tilde{V}_t = \int_{\tilde{K}}^{\infty} (z - \tilde{K})\, g(z)\, dz. $$

Another computation gives

$$ \tilde{V}_t = \tilde{S}_t\, \Phi\left( \frac{\log(\tilde{S}_t/\tilde{K}) + \frac{a^2}{2}}{a} \right) - \tilde{K}\, \Phi\left( \frac{\log(\tilde{S}_t/\tilde{K}) - \frac{a^2}{2}}{a} \right), $$

which implies that

$$ \begin{aligned} V_t = e^{rt}\, \tilde{V}_t = {}& S_t\, \Phi\left( \frac{\log(S_t/K) + rs + \frac{a^2}{2}}{a} \right) \\ &- e^{-rs}\, K\, \Phi\left( \frac{\log(S_t/K) + rs - \frac{a^2}{2}}{a} \right), \end{aligned} $$

where $s = T - t$. Plugging in $a = \sigma\sqrt{s}$ gives (5.20).

One of the hypotheses in Theorem 5.5.1 is that if $S_t$ satisfies

$$ dS_t = S_t \left[ m(t, S_t)\, dt + \sigma(t, S_t)\, dB_t \right], $$

then there exists a probability measure $Q$ under which

$$ dS_t = S_t \left[ r(t, S_t)\, dt + \sigma(t, S_t)\, dW_t \right], \tag{5.24} $$

where $W_t$ is a $Q$-Brownian motion. Indeed, if $S_t$ satisfies (5.24), then the discounted price $\tilde{S}_t = S_t/R_t$ satisfies

$$ d\tilde{S}_t = \tilde{S}_t\, \sigma(t, S_t)\, dW_t = \tilde{S}_t\, \sigma(t, R_t\, \tilde{S}_t)\, dW_t. \tag{5.25} $$

The Girsanov theorem tells us that the way to obtain $Q$ is to tilt by the local martingale $M_t$ where

$$ dM_t = M_t\, \frac{r(t, S_t) - m(t, S_t)}{\sigma(t, S_t)}\, dB_t, $$

### PDF page 175 (book page 169)

for then in the measure $Q$,

$$ dB_t = \frac{r(t, S_t) - m(t, S_t)}{\sigma(t, S_t)} \, dt + dW_t. $$

In order for the theorem to hold, we need that $M_t$ is actually a martingale and that $\tilde{S}_t$ as given in (5.25) is a martingale. While one can give general conditions when this is true, it is often just as easy to check this in each case. If $|r - m|/\sigma$ is uniformly bounded, these conditions are satisfied.

## 5.6 Martingale approach to pricing

We generalize the discussion in the previous section to the pricing of claims that are functions of the entire history of the prices of an asset. Suppose $S_t$ denotes the price of an asset satisfying

$$ dS_t = S_t \, [m_t \, dt + \sigma_t \, dB_t] \tag{5.26} $$

where $B_t$ is a standard Brownian motion. Let $\mathcal{F}_t$ denote the information in $\{B_s : 0 \le s \le t\}$, and as usual we assume that $m_t, \sigma_t$ are processes adapted to the filtration $\{\mathcal{F}_t\}$. We also assume that there is a risk-free bond $R_t$ satisfying

$$ dR_t = r_t \, R_t \, dt, \quad R_t = R_0 \exp\left\{ \int_0^t r_s \, ds \right\}, $$

where $r_t$ is also adapted.

Let $T$ be a fixed future time and assume that $V$ is an $\mathcal{F}_T$-measurable random variable. We call $V$ a *claim (at time $T$)*. The examples we have seen are of the form $V = F(S_T)$, but other examples are

$$ V = \max_{0 \le t \le T} S_t, \quad V = \frac{1}{T} \int_0^T S_t \, dt. $$

We will start with the following definition.

**Definition, first try** If $V$ is a claim at time $T$, then the *(arbitrage-free) price $V_t, 0 \le t \le T$*, of a claim $V_T$ is the minimum value of a self-financing portfolio that can be hedged to guarantee that its value at time $T$ is $V$.

### PDF page 176 (book page 170)

Our goal is to determine the price $V_t$ and the corresponding portfolio $(a_t, b_t)$, where $a_t$ denotes the number of units of $S$ and $b_t$ the number of units of $R$. This will require some mathematical assumptions that we will make as we need them. Recall that

$$ V_t = a_t \, S_t + b_t \, R_t, $$

and $(a_t, b_t)$ is self-financing if

$$ dV_t = a_t \, dS_t + b_t \, dR_t. $$

We will start by giving two bad, but unrealistic, examples that show that we need to take some care. The two examples are similar. In the first example, we allow the stock price to fluctuate too much. In the second, we choose a very risky portfolio similar to the martingale betting strategy.

**Example 5.6.1.** Suppose for ease that $r_t \equiv 0$ and $R_0 = 1$ so that $R_t \equiv 1$. Let $S_t = e^{Z_t}$ where $Z_t$ is the "martingale betting strategy revisited" in Example 4.1.1. We recall that $Z_t$ satisfies

$$ dZ_t = A_t \, dB_t, \quad Z_0 = 0, $$

and the "bets" $A_t$ are chosen so that with probability one $Z_1 \ge 1$. Itô's formula shows that $S_t$ satisfies

$$ dS_t = S_t \left[ \frac{A_t^2}{2} \, dt + A_t \, dB_t \right]. $$

We cannot find an equivalent measure such that $S_t$ is a martingale. Indeed, we know that with probability one $S_1 > S_0$, and hence this fact must be true in any equivalent measure.

**Example 5.6.2.** Suppose that $R_t \equiv 1$ and $S_t = e^{B_t - (t/2)}$ which satisfies

$$ dS_t = S_t \, dB_t, \quad S_0 = 1. $$

Let $A_t$ be as in Example 5.6.1, and choose a portfolio with $a_t = A_t/S_t$. The value of the portfolio is $V_t = a_t \, S_t + b_t \, R_t = A_t + b_t$. If the portfolio is to be self-financing, we need that

$$ dV_t = a_t \, dS_t + b_t \, dR_t = \frac{A_t}{S_t} \, S_t \, dB_t = A_t \, dB_t. $$

### PDF page 177 (book page 171)

We choose $b_t$ so that this holds (this may require choosing $b_t$ to be negative). Since $V_0 = 1$, we see that $V_t = 1 + Z_t$ where $Z_t$ is as in Example 5.6.1. In particular, $V_1 = 2$, and this portfolio hedges the claim $V \equiv 2$ at time $T = 1$. Similarly for any constant $J$, we can find $A_t$ such that with probability one $Z_t \ge J$. Hence given any $V_0$ (even negative values), we can find a portfolio that hedges the claim $V \equiv 2$. One disadvantage of these portfolios, however, is that they allow the value at times $0 < t < 1$ to be negative. It will turn out that we can eliminate examples like this by restricting to portfolios whose value at all times is nonnegative.

With the bad examples in mind, we now proceed to develop the theory. To start, we will consider discounted prices. Let

$$ \tilde{S}_t = (R_0/R_t) \, S_t, \quad \tilde{V}_t = (R_0/R_t) \, V_t $$

denote the discounted stock price and discounted value, respectively. The portfolio $(a_t, b_t)$ is the same whether or not we are using discounted units and the discounted value $\tilde{V}_t$ is given by

$$ \tilde{V}_t = a_t \, \tilde{S}_t + b_t \, R_0. $$

(Note that the "discounted bond value" is $R_0$.) Using the product formula, we see that

$$ d\tilde{S}_t = \tilde{S}_t \, [(m_t - r_t) \, dt + \sigma_t \, dB_t] . $$

Our goal is to find a self-financing portfolio $(a_t, b_t)$ such that with probability one

$$ \tilde{V}_T = a_T \, \tilde{S}_T + b_T \, R_0 = \tilde{V}. $$

Since this must happen with probability one, we may consider a mutually absolutely continuous measure. We let $Q$ be the probability measure (if it exists) that is mutually absolutely continuous with respect to $\mathbb{P}$ such that under $Q$ the discounted stock price is a martingale. Recalling (5.11), we can see that the Girsanov theorem tells us to choose

$$ dQ = M_t \, d\mathbb{P}, $$

where $M_t$ satisfies

$$ dM_t = \frac{r_t - m_t}{\sigma_t} \, M_t \, dB_t, \quad M_0 = 1. \tag{5.27} $$

### PDF page 178 (book page 172)

The solution to this last equation is a local martingale, but it not necessarily a martingale. If it is not a martingale, then some undesirable conclusions may result as in our examples above. Our first assumption will be that it is a martingale.

- **Assumption 1.** The local martingale defined in (5.27) is actually a martingale.

This assumption implies that $Q$ is mutually absolutely continuous with respect to $\mathbb{P}$. Theorem 5.3.2 gives a number of ways to establish $Q \ll \mathbb{P}$. If $Q \ll \mathbb{P}$, then we also get $\mathbb{P} \ll Q$ if $\mathbb{P}\{M_t > 0\} = 1$. Let

$$ W_t = B_t - \int_0^t \frac{r_s - m_s}{\sigma_s} \, ds, $$

which is a Brownian motion with respect to $Q$. Plugging in we see that

$$ d\tilde{S}_t = \sigma_t \, \tilde{S}_t \, dW_t. \tag{5.28} $$

This shows that $\tilde{S}_t$ is a *local* martingale with respect to $Q$. We will want this to be a martingale, and we make this assumption.

- **Assumption 2.** The $Q$-local martingale $\tilde{S}_t$ satisfying (5.28) is actually a $Q$-martingale.

Again, Theorem 5.3.2 gives some sufficient conditions for establishing that the solution to (5.28) is a $Q$-martingale. We write $\mathbb{E}_Q$ and $E_Q$ for expectations (regular and conditional) with respect to $Q$.

**Definition** A claim $V$ at time $T$ is called a *contingent claim* if $V \geq 0$ and

$$ \mathbb{E}_Q \left[ \tilde{V}^2 \right] < \infty. $$

The *(arbitrage-free) price* $V_t, 0 \leq t \leq T$, of a contingent claim $V_T$ is the minimum value of a self-financing portfolio that can be hedged to guarantee that its value never drops below zero and at time $T$ equals $V$.

Given a contingent claim, we can set

$$ \tilde{V}_t = E_Q \left[ \tilde{V} \mid \mathcal{F}_t \right]. $$

### PDF page 179 (book page 173)

This is a square integrable martingale and $\tilde{V}_T = \tilde{V}$. We would like to find a portfolio $(a_t, b_t)$ satisfying

$$ V_t = a_t \, S_t + b_t \, R_t, $$

that is self-financing,

$$ dV_t = a_t \, dS_t + b_t \, dR_t. $$

Recall that if $A_t$ is an adapted process with

$$ \int_0^t \mathbb{E}_Q[A_s^2] \, ds < \infty, $$

then

$$ Z_t = \int_0^t A_s \, dW_s $$

is a square integrable martingale. Let us assume for the moment that there exists such a process $A_s$ such that

$$ \tilde{V}_t = \tilde{V}_0 + \int_0^t A_s \, dW_s, $$

that is

$$ d\tilde{V}_t = A_t \, dW_t. \tag{5.29} $$

We compute,

$$
\begin{aligned}
dV_t &= R_t \, d\tilde{V}_t + \tilde{V}_t \, dR_t \\
&= R_t \, A_t \, dW_t + \tilde{V}_t \, dR_t \\
&= \frac{A_t}{\sigma_t \, \tilde{S}_t} \, R_t \, d\tilde{S}_t + \tilde{V}_t \, dR_t \\
&= \frac{A_t}{\sigma_t \, \tilde{S}_t} \, [dS_t - \tilde{S}_t \, dR_t] + \tilde{V}_t \, dR_t \\
&= \frac{A_t}{\sigma_t \, \tilde{S}_t} \, dS_t + \left[ \tilde{V}_t - \frac{A_t}{\sigma_t} \right] dR_t.
\end{aligned}
$$

Therefore, if

$$ a_t = \frac{A_t}{\sigma_t \, \tilde{S}_t}, \quad b_t = \tilde{V}_t - \frac{A_t}{\sigma_t}, \tag{5.30} $$

### PDF page 180 (book page 174)

the portfolio is self-financing and

$$ a_t \, S_t + b_t \, R_t = \frac{A_t}{\sigma_t \, \tilde{S}_t} \, \tilde{S}_t \, R_t + \left[ \tilde{V}_t - \frac{A_t}{\sigma_t} \right] R_t = R_t \, \tilde{V}_t = V_t. $$

Along the way we made the assumption that we could write $V_t$ as (5.29). It turns out, as we discuss in the next section, that this can always be done although we cannot guarantee that the process $A_t$ is continuous or piecewise continuous. Knowing existence of the process is not very useful if one cannot find $A_t$. For now we just write as an assumption that the computations work out.

- **Assumption 3**. We can write $\tilde{V}_t$ as (5.29), and if we define $a_t, b_t$ as in (5.30), then the stochastic integral

$$ V_t = \int_0^t a_s \, dS_s + \int_0^t b_s \, dR_s, $$

is well defined.

**Theorem 5.6.1.** *If $V$ is a contingent claim and assumptions 1-3 hold, then the arbitrage-free price is*

$$ V_t = R_t \, E_Q(\tilde{V}_T \mid \mathcal{F}_t). $$

We have done most of the work in proving this theorem. What remains is to show that if $(a_t^*, b_t^*)$ is a self-financing strategy with value

$$ V_t^* = a_t^* \, S_t + b_t^* \, R_t, $$

such that with probability one, $V_t^* \geq 0$ for all $t$ and $V_T^* \geq V$, then for all $t$, with probability one $V_t^* \geq V_t$. When we say "with probability one" this can be with respect to either $\mathbb{P}$ or $Q$ since one of our assumptions is that the two measures are mutually absolutely continuous. Let $\tilde{V}_t^* = V_t^*/R_t$ be the discounted values. The product rule gives

$$ dV_t^* = d(R_t \, \tilde{V}_t^*) = R_t \, d\tilde{V}_t^* + \tilde{V}_t^* \, dR_t = R_t \, d\tilde{V}_t^* + \left[ a_t^* \, \tilde{S}_t + b_t^* \right] dR_t, $$

and the self-financing assumptions implies that

$$ dV_t^* = a_t^* \, dS_t + b_t^* \, dR_t = a_t^* \left[ R_t \, d\tilde{S}_t + \tilde{S}_t \, dR_t \right] + b_t^* \, dR_t. $$

### PDF page 181 (book page 175)

By equating coefficients, we see that

$$ d\tilde{V}_t^* = a_t^* \, d\tilde{S}_t = a_t^* \, \sigma_t \, \tilde{S}_t \, dW_t. $$

In particular, $\tilde{V}_t^*$ is a nonnegative local martingale. We have seen that this implies that $\tilde{V}_t^*$ is a supermartingale and

$$ E_Q\left[\tilde{V}_T^* \mid \mathcal{F}_t\right] \le \tilde{V}_t^*. $$

If $V \le \tilde{V}_T^*$, then

$$ E_Q\left[\tilde{V}_T^* \mid \mathcal{F}_t\right] \ge E_Q\left[V \mid \mathcal{F}_t\right] = V_t. $$

**Example 5.6.3.** We will give another derivation of the Black-Scholes equation. Assume that the stock price is a diffusion satisfying

$$ dS_t = S_t \left[m(t, S_t) \, dt + \sigma(t, S_t) \, dB_t\right], $$

and the bond rate satisfies

$$ dR_t = r(t, S_t) \, R_t \, dt. $$

The product rule implies that the discounted stock price satisfies

$$ d\tilde{S}_t = \tilde{S}_t \left[(m(t, S_t) - r(t, S_t)) \, dt + \sigma(t, S_t) \, dB_t\right]. $$

If $V$ is a claim of the form $V = F(S_T)$, let $\phi$ be the function

$$ \phi(t, x) = E_Q\left[(R_t/R_T) \, V \mid S_t = x\right], $$

and note that

$$ V_t = R_t \, \tilde{V}_t = R_t \, E_Q\left[R_T^{-1} \, V \mid \mathcal{F}_t\right] = \phi(t, S_t). $$

Assuming sufficient smoothness, Itô's formula gives

$$ d\phi(t, S_t) = \partial_t \phi(t, S_t) \, dt + \phi'(t, S_t) \, dS_t + \frac{1}{2} \, \phi''(t, S_t) \, d\langle S \rangle_t. $$

Recalling that

$$ dS_t = S_t \left[r(t, S_t) \, dt + \sigma(t, S_t) \, dW_t\right], $$

### PDF page 182 (book page 176)

we see that

$$ d\tilde{V}_t = d[R_t^{-1} \, \phi(t, S_t)] = J_t \, dt + A_t \, dW_t, $$

where

$$ J_t = R_t^{-1} \left[\partial_t \phi(t, S_t) + \frac{\sigma(t, S_t)^2 \, S_t^2}{2} \, \phi''(t, S_t) \right. $$
$$ \left. + r(t, S_t) \, S_t \, \phi'(t, S_t) - r(t, S_t) \phi(t, S_t)\right], $$
$$ A_t = R_t^{-1} \, S_t \, \sigma(t, S_t) \, \phi'(t, S_t) = \tilde{S}_t \, \sigma(t, S_t) \, \phi'(t, S_t). $$

Since $\tilde{V}_t$ is a $Q$-martingale, $J_t = 0$, giving the Black-Scholes PDE again, and $d\tilde{V}_t = A_t \, dW_t$. Plugging into (5.30), we recover the hedging portfolio,

$$ a_t = \frac{A_t}{\sigma(t, S_t) \, \tilde{S}_t} = \phi'(t, S_t), $$

$$ b_t = \tilde{V}_t - \frac{A_t}{\sigma(t, S_t)} = R_t^{-1} \left[V_t - S_t \, \phi'(t, S_t)\right]. $$

This can be compared to (5.19).

**Example 5.6.4.** Suppose $S_t$ is a geometric Brownian motion

$$ dS_t = S_t \left[m \, dt + \sigma \, dB_t\right], $$

and the bond rate is constant $r$. Suppose that the claim is the average stock price over the interval $[0, T]$,

$$ V = \frac{1}{T} \int_0^T S_t \, dt. $$

In the new measure $Q$, the discounted stock price $\tilde{S}_t = e^{-rt} \, S_t$ satisfies

$$ d\tilde{S}_t = \sigma \, \tilde{S}_t \, dW_t, $$

where $W_t$ is a $Q$-Brownian motion. The discounted value is

$$ \tilde{V}_t = E_Q\left[\frac{e^{-rT}}{T} \int_0^T S_s \, ds \mid \mathcal{F}_t\right]. $$

### PDF page 183 (book page 177)

Since $\int_0^t S_s \, ds$ is $\mathcal{F}_t$-measurable, we get

$$
\begin{aligned}
T \, e^{rT} \, \tilde{V}_t &= \int_0^t S_s \, ds + E_Q\left[\int_t^T S_s \, ds \mid \mathcal{F}_t\right] \\
&= \int_0^t S_s \, ds + \int_t^T E_Q\left[S_s \mid \mathcal{F}_t\right] ds.
\end{aligned}
$$

The second equality uses a form of Fubini's theorem that follows from the linearity of conditional expectation. Since $\tilde{S}_s$ is a $Q$-martingale, if $s > t$,

$$ E_Q\left[S_s \mid \mathcal{F}_t\right] = e^{rs} \, E_Q\left[\tilde{S}_s \mid \mathcal{F}_t\right] = e^{rs} \, \tilde{S}_t = e^{r(s-t)} \, S_t. $$

Therefore,

$$ \int_t^T E_Q\left[S_s \mid \mathcal{F}_t\right] ds = S_t \int_t^T e^{r(s-t)} \, ds = \frac{e^{r(T-t)} - 1}{r} \, S_t, $$

and

$$
\begin{aligned}
\tilde{V}_t &= \frac{e^{-rT}}{T} \int_0^t S_s \, ds + \frac{e^{-rt} - e^{-rT}}{rT} \, S_t \\
&= \frac{e^{-rT}}{T} \int_0^t S_s \, ds + \frac{1 - e^{-r(T-t)}}{rT} \, \tilde{S}_t, \tag{5.31}
\end{aligned}
$$

$$ V_t = e^{rt} \, \tilde{V}_t = \frac{e^{-r(T-t)}}{T} \int_0^t S_s \, ds + \frac{1 - e^{-r(T-t)}}{rT} \, S_t. $$

Note that $V_T = V$ which we needed, and the price at time 0 is

$$ V_0 = \frac{1 - e^{-rT}}{rT} \, S_0. $$

The hedging portfolio can be worked out with a little thought. We will start with all the money in stocks and as time progresses we move money into bonds. Suppose that during time interval $[t, t+\Delta t]$ we convert $u\Delta t$ units of stock into bonds. Then the value of these units of bonds at time $T$ will be about $u \, e^{r(T-t)} \, S_t \, \Delta t$. If we choose $u = e^{r(t-T)}/T$, then the value will be about $S_t \, \Delta t/T$ and hence the value of all our bonds will be about $\frac{1}{T} \int_0^T S_s \, ds$. This gives us

$$ \frac{da_t}{dt} = -\frac{e^{r(t-T)}}{T} $$

### PDF page 184 (book page 178)

and using the terminal condition $a_T = 0$, we get

$$ a_t = \frac{1 - e^{r(t-T)}}{rT}. \tag{5.32} $$

This is a special case where the hedging strategy does not depend on the current stock price $S_t$. If we want to use the formula we derived, we use (5.31) to give

$$ d\tilde{V}_t = \frac{1 - e^{r(t-T)}}{rT}\, d\tilde{S}_t = \frac{1 - e^{r(t-T)}}{rT}\, \sigma\, \tilde{S}_t\, dW_t. $$

Plugging this into (5.30) gives (5.32).

## 5.7 Martingale representation theorem

In the last section we assumed in (5.29) that a continuous martingale could be represented as a stochastic integral. In fact, this is always that case. Suppose $B_t$ is a standard Brownian motion and $\{\mathcal{F}_t\}$ is the filtration given by the Brownian motion. Suppose there is a claim $V$ at time $T$ and let

$$ V_t = \mathbb{E}[V \mid \mathcal{F}_t]. $$

Then there exists an adapted process $A_t$ such that

$$ \mathbb{E}[V \mid \mathcal{F}_t] = \mathbb{E}[V] + \int_0^t A_s\, dB_s. $$

In order to be precise, we need to allow a wider class of processes than those with continuous and piecewise continuous paths. We will not go into detalis [sic] here, but any allowable process can be approximated by continuous and piecewise continuous processes. From practical perspective, knowing that such an $A_s$ exists is not so useful unless one can give it explicitly. In the examples we give the SDE for $V_s$ explicitly.

This theorem states roughly that all of the randomness in the system is given by the Brownian motion $B_t$ and the only way to get martingales with only this information is to vary the "betting strategy" on the Brownian motion. To illustrate this idea, we will derive the representation theorem in the easier case of random walk.

### PDF page 185 (book page 179)

Suppose we have a binomial model with $\Delta t = 1/N$ and $\Delta x = \sqrt{\Delta t} = 1/\sqrt{N}$. We have independent random variables

$$ X_{\Delta t}, X_{2\Delta t}, \ldots $$

each with

$$ \mathbb{P}\{X_{k\Delta t} = \Delta x\} = \mathbb{P}\{X_{k\Delta t} = -\Delta x\} = \frac{1}{2}. $$

Let $\mathcal{F}_{k\Delta t}$ denote the information in $\{X_{\Delta t}, X_{2\Delta t}, , \ldots, X_{k\Delta t}\}$, and assume that $M_{k\Delta t}$ is a martingale with respect to $\mathcal{F}_{k\Delta t}$. The martingale property implies that

$$ E\left[M_{(k+1)\Delta t} \mid \mathcal{F}_{k\Delta t}\right] = M_{k\Delta t}. \tag{5.33} $$

Since $\{M_{(k+1)\Delta t}\}$ is $\mathcal{F}_{(k+1)\Delta t}$-measurable, its value depends on the values of

$$ X_{\Delta t}, X_{2\Delta t}, \ldots, X_{(k+1)\Delta t}. $$

When we take a conditional expectation with respect to $\mathcal{F}_{k\Delta t}$ we are given the value of the vector

$$ \mathbf{X}_{k\Delta} = (X_{\Delta t}, X_{2\Delta t}, \ldots, X_{k\Delta t}). $$

Given a particular value of $\mathbf{X}_{k\Delta t}$, there are only two possible values for $M_{(k+1)\Delta t}$ corresponding to the values when $X_{(k+1)\Delta t} = \Delta x$ and $X_{(k+1)\Delta t} = -\Delta x$, respectively. Let us denote the two values by

$$ [b + a]\,\Delta x, \quad [b - a]\,\Delta x, $$

where $b\,\Delta x$ is the average of the two values. The two numbers $a, b$ depend on $\mathbf{X}_{k\Delta t}$ and hence are $\mathcal{F}_{k\Delta t}$-measurable. The martingale property (5.33) tells us that

$$ b\,\Delta x = M_{k\Delta t}, $$

and hence

$$ M_{(k+1)\Delta t} - M_{k\Delta t} = \pm a\,\Delta x = a\, X_{(k+1)\Delta t}. $$

If we write $J_{(k+1)\Delta t}$ for the number $a$, then $J_{(k+1)\Delta t}$ is $\mathcal{F}_{k\Delta t}$-measurable, and

$$ M_{k\Delta t} = M_0 + \sum_{j=1}^{k} J_{j\Delta t}\, X_{j\Delta t}. $$

This is the form of the stochastic integral with respect to random walk as in Section 1.6.

### PDF page 186 (book page 180)

## 5.8 Exercises

**Exercise 5.1.** For each of the following random variables $X_j$ on $\mathbb{R}$, let $\mu_j$ be the distribution considered as a probability measure on $\mathbb{R}$. For each pair state whether or not $\mu_j \ll \mu_k$. Since there are six random variables, there should be 30 answers.

$$ X_1 \text{ normal mean 2, variance 7} $$

$$ X_2 \text{ binomial with parameters } n = 7, p = .3 $$

$$ X_3 \text{ Poisson with parameter 2} $$

$$ X_4 = e^{X_1} $$

$$ X_5 \text{ uniform on } [0, 1] $$

$$ X_6 = X_1\, X_3 + X_2 \text{ assuming } X_1, X_2, X_3 \text{ independent }. $$

**Exercise 5.2.** Consider the martingale betting strategy from Chapter 1. Let $W_n$ denote the winnings at time $n$ and let

$$ M_n = 1 - W_n, $$

so that at each time $n$, $M_n$ equals 0 or $2^n$. Note that $M_0 = 1$. Let $T = \min\{n : M_n = 0\}$. Let $\mathcal{F}_n$ be the information in $M_0, M_1, \ldots, M_n$.

1. Explain why $M_n$ is a nonnegative martingale.

2. Define a new probability measure $Q_n$ by saying that for any event $V$ that is $\mathcal{F}_n$-measurable,
$$ Q_n(V) = \mathbb{E}\left[M_n\, 1_V\right]. $$
   Show that if $m < n$ and $V$ is $\mathcal{F}_m$-measurable, then $Q_m(V) = Q_n(V)$.

3. Given the last part, we can write $Q$ rather than just $Q_n$. Find the transition probability
$$ Q\left\{M_{n+1} = 2^{n+1} \mid M_n = 2^n\right\}. $$

4. Find the $Q$-probability that $T < \infty$.

5. Is $M_n$ a martingale with respect to the measure $Q$?

### PDF page 187 (book page 181)

**Exercise 5.3.** Suppose $B_t$ is a standard Brownian motion on $(\Omega, \mathbb{P})$. For each of the following choices of $X_t, 0 \leq t \leq 1$, state whether there is an equivalent probability measure $Q$ such that the $X_t$ is a standard Brownian motion in the new measure. If the answer is yes, give $dQ/dP$ at $t = 1$. In all cases assume that $B_0 = 0, X_0 = 0$.

$$ dX_t = 2\,dt + dB_t, $$

$$ dX_t = 2\,dt + 6\,dB_t, $$

$$ dX_t = 2B_t\,dt + dB_t. $$

**Exercise 5.4.** Let $B_t$ be a standard Brownian motion with $B_0 = 0$. Let $m > 0$ and let $X_t = e^{-mB_t^2}$.

1. Find a function $g$ such that

$$ M_t := X_t \exp\left\{ \int_0^t g(X_s)\,ds \right\} $$

   is a local martingale.

2. What SDE does $M_t$ satisfy?

3. Let $Q$ be the probability measure obtained by tilting by $M_t$. Find the SDE for $B_t$ in terms of a $Q$-Brownian motion.

4. Explain why $M_t$ is actually a martingale.

**Exercise 5.5.** Let $B_t$ be a standard Brownian motion with $B_0 = 1$. Let $T = \min\{t : B_t = 0\}$ Let $r > 0$ and let $X_t = B_t^r$.

1. Find a function $g$ such that

$$ M_t := X_t \exp\left\{ \int_0^t g(X_s)\,ds \right\} $$

   is a local martingale for $t < T$. (Do not worry about what happens after time $T$.)

2. What SDE does $M_t$ satisfy?

3. Let $Q$ be the probability measure obtained by tilting by $M_t$. Find the SDE for $B_t$ in terms of a $Q$-Brownian motion.

### PDF page 188 (book page 182)

**Exercise 5.6.** Suppose $a, m > 0$ and $W_t$ is a Brownian motion with drift $m$ and variance 1. Let

$$ T_a = \inf\{t : W_t = a\}. $$

Find the density of $T_a$. Hint: look at Examples 2.7.1 and 5.2.2.

**Exercise 5.7.** Suppose the price of a stock $S_t$ follows a geometric Brownian motion

$$ dS_t = S_t \left[3\,dt + dB_t\right], $$

whee[sic] $B_t$ is a standard Brownian motion with respect to a measure $\mathbb{P}$. Suppose there is a risk-free bond with rate $r = .05$. Let $Q$ be the measure, mutually absolutely continuous with respect to $\mathbb{P}$, under which the discounted stock price $\tilde{S}_t$ is a martingale.

1. Give the SDE for $\tilde{S}_t$ in terms of $W_t$, a standard Brownian motion with respect to $Q$.

2. Suppose there is a claim at time $T = 2$ of $V = S_2^2$. Is this a contingent claim?

3. Find the discounted value $\tilde{V}_t$ of the claim for $0 \leq t \leq 2$.

4. Give the SDE for $\tilde{V}_t$ in terms of the Brownian motion $W$.

5. Find the portfolio $(a_t, b_t)$ that hedges the claim.

6. Find the value $V_t$.

**Exercise 5.8.** Repeat Exercise 5.7 with $V = S_2^3$.

**Exercise 5.9.** Repeat Exercise 5.7 with claim

$$ V = \int_0^2 s\,S_s\,ds. $$

**Exercise 5.10.** Repeat Exercise 5.7 with claim

$$ V = \int_0^2 S_s^2\,ds. $$

**Exercise 5.11.** Here we do the calculus needed to finish the derivation of the Black-Scholes formula in Example 5.5.1.

### PDF page 189 (book page 183)

1. Show that if $N$ has a standard normal distribution and $a \neq 0, y$ are constants, then the density of $Z = \exp\{aN + y\}$ is

$$ g(z) = \frac{1}{az}\phi\left( \frac{-y + \log z}{a} \right), $$

   where $\phi$ denotes the density of $N$.

2. Show that for all $x$,

$$ \int_x^\infty (z - x)\,g(z)\,dz = e^{y+(a^2/2)}\,\Phi\left( \frac{y - \log x + a^2}{a} \right) - x\,\Phi\left( \frac{y - \log x}{a} \right). $$

3. Use these calculations to check the details of Example 5.5.1.

### PDF page 190 (book page 184)

*(Blank page.)*

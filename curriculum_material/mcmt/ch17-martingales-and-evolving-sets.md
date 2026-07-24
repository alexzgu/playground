# Chapter 17 — Martingales and Evolving Sets
*(PDF pages 259–276; book pages 243–260)*

### PDF page 259 (book page 243)

CHAPTER 17

# Martingales and Evolving Sets

**17.1. Definition and Examples**

Let $X_1, X_2, \ldots$ be i.i.d. random variables with $\mathbf{E}(X_t) = 0$ for all $t$, and let $S_t = \sum_{r=1}^t X_r$. The sequence $(S_t)$ is a random walk on $\mathbb{R}$ with increments $(X_t)$. Observe that if $\mathcal{F}_t = \sigma(X_1, \ldots, X_t)$, then

$$ \mathbf{E}[S_{t+1} \mid \mathcal{F}_t] = \mathbf{E}[S_t + X_{t+1} \mid \mathcal{F}_t] = S_t + \mathbf{E}[X_{t+1} \mid \mathcal{F}_t] = S_t \,. \tag{17.1} $$

Thus, the conditional expected location of the walk at time $t + 1$ is the location at time $t$. The equality $\mathbf{E}[S_{t+1} \mid \mathcal{F}_t] = S_t$ in (17.1) is the key property shared by martingales, defined below.

A **martingale with respect to a filtration** $\{\mathcal{F}_t\}$ is a sequence of random variables $(M_t)$ satisfying the following conditions:

(i)  $\mathbf{E}|M_t| < \infty$ for all $t$.
(ii)  $(M_t)$ is adapted to $\{\mathcal{F}_t\}$.
(iii)

$$ \mathbf{E}(M_{t+1} \mid \mathcal{F}_t) = M_t \quad \text{ for all } t \geq 0 \,. $$

Condition (iii) says that given the data in $\mathcal{F}_t$, the best predictor of $M_{t+1}$ is $M_t$.

EXAMPLE 17.1. The unbiased random walk $(S_t)$ defined above is a martingale with respect to $\mathcal{F}_t = \sigma(X_1, \ldots, X_t)$.

A **supermartingale** $(M_t)$ satisfies conditions (i) and (ii) in the definition of a martingale, but instead of (iii), it obeys the inequality

$$ \mathbf{E}(M_{t+1} \mid \mathcal{F}_t) \leq M_t \quad \text{ for all } t \geq 0 \,. \tag{17.2} $$

A **submartingale** $(M_t)$ satisfies (i) and (ii) and

$$ \mathbf{E}(M_{t+1} \mid \mathcal{F}_t) \geq M_t \quad \text{ for all } t \geq 0 \,. \tag{17.3} $$

For a random walk $(S_t)$, the increments $\Delta S_t := S_{t+1} - S_t$ form an independent sequence with $\mathbf{E}(\Delta S_t) = 0$. For a general martingale, the increments also have mean zero, and although not necessarily independent, they are uncorrelated: for $s < t$,

$$ \begin{aligned} \mathbf{E}(\Delta M_t \Delta M_s) &= \mathbf{E}\left(\mathbf{E}\left(\Delta M_t \Delta M_s \mid \mathcal{F}_t\right)\right) \\ &= \mathbf{E}\left(\Delta M_s \mathbf{E}\left(\Delta M_t \mid \mathcal{F}_t\right)\right) \\ &= 0. \end{aligned} \tag{17.4} $$

We have used here the fact, immediate from condition (iii) in the definition of a martingale, that

$$ \mathbf{E}(\Delta M_t \mid \mathcal{F}_t) = 0, \tag{17.5} $$

which is stronger than the statement that $\mathbf{E}(\Delta M_t) = 0$.

### PDF page 260 (book page 244)

A useful property of martingales is that

$$ \mathbf{E}(M_t) = \mathbf{E}(M_0) \quad \text{for all } t \geq 0. $$

EXAMPLE 17.2. Let $(Y_t)$ be a random walk on $\mathbb{Z}$ which moves up one unit with probability $p$ and down one unit with probability $q := 1 - p$, where $p \neq 1/2$. In other words, given $Y_0, \ldots, Y_t$,

$$ \Delta Y_t := Y_{t+1} - Y_t = \begin{cases} 1 & \text{with probability } p, \\ -1 & \text{with probability } q. \end{cases} $$

If $M_t := (q/p)^{Y_t}$, then $(M_t)$ is a martingale with respect to $\mathcal{F}_t = \sigma(Y_1, \ldots, Y_t)$. Condition (ii) is clearly satisfied, and

$$ \begin{aligned} \mathbf{E}\left((q/p)^{Y_{t+1}} \,\Big|\, \mathcal{F}_t\right) &= \mathbf{E}\left((q/p)^{Y_t}(q/p)^{Y_{t+1}-Y_t} \,\Big|\, \mathcal{F}_t\right) \\ &= (q/p)^{Y_t} \left[p(q/p) + q(q/p)^{-1}\right] \\ &= (q/p)^{Y_t}. \end{aligned} $$

EXAMPLE 17.3. Let $(Y_t)$ be as in the previous example, let $\mu := p - q$, and define $M_t := Y_t - \mu t$. The sequence $(M_t)$ is a martingale.

**17.2. Optional Stopping Theorem**

A sequence of random variables $(A_t)$ is called **previsible** with respect to a filtration $\{\mathcal{F}_t\}$ if $A_t \in \mathcal{F}_{t-1}$ for all $t \geq 1$. That is, the random variable $A_t$ is determined by what has occurred strictly before time $t$.

Suppose that $(M_t)$ is a martingale with respect to $\{\mathcal{F}_t\}$ and $(A_t)$ is a previsible sequence with respect to $\{\mathcal{F}_t\}$. Imagine that a gambler can bet on a sequence of games so that he receives $M_t - M_{t-1}$ for each unit bet on the $t$-th game. The interpretation of the martingale property $\mathbf{E}(M_t - M_{t-1} \mid \mathcal{F}_{t-1}) = 0$ is that the games are fair. Let $A_t$ be the amount bet on the $t$-th game; the fact that the player sizes his bet based only on the outcomes of previous games forces $(A_t)$ to be a previsible sequence. At time $t$, the gambler's fortune is

$$ N_t := M_0 + \sum_{s=1}^t A_s(M_s - M_{s-1}). \tag{17.6} $$

Is it possible, by a suitably clever choice of bets $(A_1, A_2, \ldots)$, to generate an advantage for the player? By this, we mean is it possible that $\mathbf{E}(N_t) > 0$ for some $t$? Many gamblers believe so. The next theorem proves that they are wrong.

THEOREM 17.4. *Let $(A_t)$ be a previsible sequence with respect to a filtration $\{\mathcal{F}_t\}$ such that each $A_t$ is a bounded random variable. If $(M_t)$ is a martingale (submartingale) with respect to $\{\mathcal{F}_t\}$, then the sequence of random variables $(N_t)$ defined in (17.6) is also a martingale (submartingale) with respect to $\{\mathcal{F}_t\}$.*

PROOF. We consider the case where $(M_t)$ is a martingale; the proof when $(M_t)$ is a submartingale is similar.

For each $t$ there is a constant $K_t$ such that $|A_t| \leq K_t$, whence

$$ \mathbf{E}|N_t| \leq \mathbf{E}|M_0| + \sum_{s=1}^t K_t \mathbf{E}|M_s - M_{s-1}| < \infty, $$

### PDF page 261 (book page 245)

and therefore the expectation of $N_t$ is defined. Observe that

$$ \mathbf{E}\left(N_{t+1} - N_t \mid \mathcal{F}_t\right) = \mathbf{E}(A_{t+1}(M_{t+1} - M_t) \mid \mathcal{F}_t). $$

Since $A_{t+1}$ is $\mathcal{F}_t$-measurable, the right-hand side equals

$$ A_{t+1}\mathbf{E}(M_{t+1} - M_t \mid \mathcal{F}_t) = 0. $$

$\blacksquare$

Recall from Section 6.2 that a stopping time for $\{\mathcal{F}_t\}$ is a random variable $\tau$ with values in $\{0, 1, \ldots\} \cup \{\infty\}$ such that $\{\tau = t\} \in \mathcal{F}_t$ for all $t$. In other words, the sequence of indicator variables $\{\mathbf{1}_{\{\tau=t\}}\}_{t=0}^{\infty}$ is adapted to the filtration $\{\mathcal{F}_t\}$.

For a martingale, $\mathbf{E}(M_t) = \mathbf{E}(M_0)$ for all *fixed* times $t$. Does this remain valid if we replace $t$ by a random time? In particular, for stopping times $\tau$, is $\mathbf{E}(M_\tau) = \mathbf{E}(M_0)$? Under some additional conditions, the answer is "yes". However, as the next example shows, this does not hold in general.

EXAMPLE 17.5. Let $(X_s)$ be the i.i.d. sequence with

$$ \mathbf{P}\{X_1 = +1\} = \mathbf{P}\{X_1 = -1\} = \frac{1}{2}. $$

As discussed in Example 17.1, the sequence of partial sums $(S_t)$ is a martingale. We suppose that $S_0 = 0$. The first-passage time to 1, defined as

$$ \tau := \min\{t \geq 0 \,:\, S_t = 1\}, $$

is a stopping time, and clearly $\mathbf{E}(M_\tau) = 1 \neq \mathbf{E}(M_0)$.

Note that if $\tau$ is a stopping time, then so is $\tau \wedge t$ for any fixed $t$. (Here, as always, $a \wedge b := \min\{a, b\}$.)

THEOREM 17.6 (Optional Stopping Theorem, Version 1). *If $(M_t)$ is a martingale with respect to the filtration $\{\mathcal{F}_t\}$ and $\tau$ is a stopping time for $\{\mathcal{F}_t\}$, then $(M_{t\wedge\tau})$ is a martingale with respect to $\{\mathcal{F}_t\}$. Consequently, $\mathbf{E}(M_{t\wedge\tau}) = \mathbf{E}(M_0)$.*

COROLLARY 17.7 (Optional Stopping Theorem, Version 2). *Let $(M_t)$ be a martingale with respect to $\{\mathcal{F}_t\}$ and $\tau$ a stopping time for $\{\mathcal{F}_t\}$. If $\mathbf{P}\{\tau < \infty\} = 1$ and $|M_{t\wedge\tau}| \leq K$ for all $t$ and some constant $K$, then $\mathbf{E}(M_\tau) = \mathbf{E}(M_0)$.*

PROOF OF THEOREM 17.6. If $A_t := \mathbf{1}_{\{\tau \geq t\}}$, then

$$ A_t = 1 - \mathbf{1}_{\{\tau \leq t-1\}} \in \mathcal{F}_{t-1}, $$

whence $(A_t)$ is previsible. By Theorem 17.4,

$$ \sum_{s=1}^{t} A_s(M_s - M_{s-1}) = M_{t\wedge\tau} - M_0 $$

defines a martingale. Adding $M_0$ does not destroy the martingale properties, whence $(M_{t\wedge\tau})$ is also a martingale. $\blacksquare$

PROOF OF COROLLARY 17.7. Since $(M_{\tau\wedge t})$ is a martingale, $\mathbf{E}\left(M_{\tau\wedge t}\right) = \mathbf{E}\left(M_0\right)$. Thus

$$ \lim_{t\to\infty} \mathbf{E}(M_{\tau\wedge t}) = \mathbf{E}(M_0). $$

By the Bounded Convergence Theorem, the limit and expectation can be exchanged. Since $\mathbf{P}\{\tau < \infty\} = 1$, we have $\lim_{t\to\infty} M_{\tau\wedge t} = M_\tau$ with probability one, and consequently $\mathbf{E}(M_\tau) = \mathbf{E}(M_0)$. $\blacksquare$

### PDF page 262 (book page 246)

COROLLARY 17.8 (Optional Stopping Theorem, Version 3). *Let $(M_t)$ be a martingale with respect to $\{\mathcal{F}_t\}$ having bounded increments, that is $|M_{t+1} - M_t| \leq B$ for all $t$, where $B$ is a non-random constant. Suppose that $\tau$ is a stopping time for $\{\mathcal{F}_t\}$ with $\mathbf{E}(\tau) < \infty$. Then $\mathbf{E}(M_\tau) = \mathbf{E}(M_0)$.*

PROOF. Note that

$$ |M_{\tau\wedge t}| = \left|\sum_{s=1}^{\tau\wedge t}(M_s - M_{s-1}) + M_0\right| \leq \sum_{s=1}^{\tau\wedge t}|M_s - M_{s-1}| + |M_0| \leq B\tau + |M_0|. $$

Since $\mathbf{E}(B\tau + |M_0|) < \infty$, by the Dominated Convergence Theorem and Theorem 17.6,

$$ \mathbf{E}(M_0) = \lim_{t\to\infty} \mathbf{E}(M_{\tau\wedge t}) = \mathbf{E}(M_\tau). $$

$\blacksquare$

EXAMPLE 17.9. Let $(Y_t)$ be i.i.d. unbiased $\pm 1$'s, and set $M_t = \sum_{s=1}^{t} Y_s$. Consider the previsible sequence defined by $A_1 = 1$ and for $t > 1$,

$$ A_t = \begin{cases} 2^{t-1} & \text{if } Y_1 = Y_2 = \cdots = Y_{t-1} = -1, \\ 0 & \text{if } Y_s = 1 \text{ for some } s < t. \end{cases} $$

View this sequence as wagers on i.i.d. fair games which pay $\pm 1$ per unit bet. The player wagers $2^{t-1}$ on game $t$, provided he has not won a single previous game. At his first win, he stops playing. If $\tau$ is the time of the first win, $\tau$ is a stopping time. The total gain of the player by time $t$ is

$$ N_t := \sum_{s=1}^{t} A_s(M_s - M_{s-1}) = \begin{cases} 0 & \text{if } t = 0, \\ 1 - 2^t & \text{if } 1 \leq t < \tau, \\ 1 & \text{if } t \geq \tau. \end{cases} $$

Since we are assured that $Y_s = 1$ for some $s$ eventually, $\tau < \infty$ and $N_\tau = 1$ with probability 1. Thus $\mathbf{E}(N_\tau) = 1$. But $\mathbf{E}(N_0) = 0$, and $(N_t)$ is a martingale! By doubling our bets every time we lose, we have assured ourselves of a profit. This at first glance seems to contradict Corollary 17.7. But notice that the condition $|N_{\tau\wedge t}| \leq K$ is not satisfied, so we cannot apply the corollary.

**17.3. Applications**

**17.3.1. Gambler's ruin.** Let $(S_t)$ be a random walk on $\mathbb{Z}$ having $\pm 1$ increments. Define for each integer $r$ the stopping time $\tau_r = \inf\{t \geq 0 \,:\, S_t = r\}$. For $k = 0, 1, \ldots, N$, let

$$ \alpha(k) := \mathbf{P}_k\{\tau_0 < \tau_N\} $$

be the probability that the walker started from $k$ visits 0 before hitting $N$. If a gambler is betting a unit amount on a sequence of games and starts with $k$ units, $\alpha(k)$ is the probability that he goes bankrupt before he attains a fortune of $N$ units.

We suppose that $\mathbf{P}\{S_{t+1} - S_t = +1 \mid S_0, \ldots, S_t\} = p$, where $p \neq 1/2$. We use martingales to derive the gambler's ruin formula, which was found previously in Example 9.9 by calculating effective resistance.

In Example 17.2 it was shown that $M_t := (q/p)^{S_t}$ defines a martingale, where $q = 1 - p$. Let $\tau := \tau_0 \wedge \tau_N$ be the first time the walk hits either 0 or $N$; the random

### PDF page 263 (book page 247)

variable $\tau$ is a stopping time. Since $M_{\tau\wedge t}$ is bounded, we can apply Corollary 17.7 to get

$$ (q/p)^k = \mathbf{E}_k\left((q/p)^{S_\tau}\right) = \alpha(k) + (q/p)^N(1 - \alpha(k)). $$

Solving for $\alpha(k)$ yields

$$ \alpha(k) = \frac{(q/p)^k - (q/p)^N}{1 - (q/p)^N}. $$

In the case where $p = q = 1/2$, we can apply the same argument to the martingale $(S_t)$ to show that $\alpha(k) = 1 - k/N$.

Now consider again the unbiased random walk. The expected time-to-ruin formula (2.3), which was derived in Section 2.1 by solving a system of linear equations, can also be found using a martingale argument.

Notice that

$$ \mathbf{E}(S_{t+1}^2 - S_t^2 \mid S_0, \ldots, S_t) = \frac{(S_t + 1)^2}{2} + \frac{(S_t - 1)^2}{2} - S_t^2 = 1 \,, $$

whence $M_t := S_t^2 - t$ defines a martingale. By the Optional Stopping Theorem (Theorem 17.6),

$$ k^2 = \mathbf{E}_k(M_0) = \mathbf{E}_k(M_{\tau\wedge t}) = \mathbf{E}_k(S_{\tau\wedge t}^2) - \mathbf{E}_k(\tau \wedge t). \tag{17.7} $$

Since $(\tau \wedge t) \uparrow \tau$ as $t \to \infty$, the Monotone Convergence Theorem implies that

$$ \lim_{t\to\infty} \mathbf{E}_k(\tau \wedge t) = \mathbf{E}_k(\tau). \tag{17.8} $$

Observe that $S_{\tau\wedge t}^2$ is bounded by $N^2$, so together (17.7) and (17.8) show that

$$ \mathbf{E}_k(\tau) = \lim_{t\to\infty} \mathbf{E}_k\left(S_{\tau\wedge t}^2\right) - k^2 \leq N^2 < \infty. \tag{17.9} $$

Therefore, with probability one, $\lim_{t\to\infty} S_{\tau\wedge t}^2 = S_\tau^2$, so by bounded convergence,

$$ \lim_{t\to\infty} \mathbf{E}_k\left(S_{\tau\wedge t}^2\right) = \mathbf{E}_k\left(S_\tau^2\right). \tag{17.10} $$

Taking limits in (17.7) and using (17.8) and (17.10) shows that

$$ \mathbf{E}_k\tau = \mathbf{E}_k S_\tau^2 - k^2 = [1 - \alpha(k)]N^2 - k^2. $$

Hence we obtain

$$ \mathbf{E}_k(\tau) = k(N - k). \tag{17.11} $$

**17.3.2. Waiting times for patterns in coin tossing.** Let $X_1, X_2, \ldots$ be a sequence of independent fair coin tosses (so that $\mathbf{P}\{X_t = H\} = \mathbf{P}\{X_t = T\} = 1/2$), and define

$$ \tau_{HTH} := \inf\{t \geq 3 \,:\, X_{t-2}X_{t-1}X_t = HTH\}. $$

We wish to determine $\mathbf{E}(\tau_{HTH})$.

Gamblers are allowed to place bets on each individual coin toss. On each bet, the gambler is allowed to pay an entrance fee of $k$ units and is payed in return $2k$ units if the outcome is $H$ or 0 units if the outcome is $T$. The amount $k$ may be negative, which corresponds to a bet on the outcome $T$.

We suppose that at each unit of time until the word $HTH$ first appears, a new gambler enters and employs the following strategy: on his first bet, he wagers 1 unit on the outcome $H$. If he loses, he stops. If he wins and the sequence $HTH$ still has not yet appeared, he wagers his payoff of 2 on $T$. Again, if he loses, he stops playing. As before, if he wins and the sequence $HTH$ has yet to occur, he takes

### PDF page 264 (book page 248)

his payoff (now 4) and wagers on $H$. This is the last bet placed by this particular gambler.

Suppose that $\tau_{HTH} = t$. The gambler who started at $t$ is paid 2 units, the gambler who started at time $t - 2$ is paid 8 units, and every gambler has paid an initial 1 entry fee. At time $\tau_{HTH}$, the net profit to all gamblers is $10 - \tau_{HTH}$. Since the game is fair, the expected winnings must total 0, i.e.,

$$ 10 - \mathbf{E}(\tau_{HTH}) = 0. $$

We conclude that $\mathbf{E}(\tau_{HTH}) = 10$.

We describe the situation a bit more precisely: let $(B_t)$ be an i.i.d. sequence of $\{0, 1\}$-valued random variables, with $\mathbf{E}(B_t) = 1/2$, and define $M_t = \sum_{s=1}^{t}(2B_s - 1)$. Clearly $(M_t)$ is a martingale. Let $\tau_{101} = \inf\{t \geq 3 \, : \, B_{t-2}B_{t-1}B_t = 101\}$, and define

$$ A_t^s = \begin{cases} 1 & t = s, \\ -2 & t = s + 1, \ \tau_{101} > t, \\ 4 & t = s + 2, \ \tau_{101} > t, \\ 0 & \text{otherwise.} \end{cases} $$

The random variable $A_t^s$ is the amount wagered on heads by the $s$-th gambler on the $t$-th game. Define $N_t^s = \sum_{r=1}^{t} A_r^s(M_r - M_{r-1})$, the net profit to gambler $s$ after $t$ games. Note that for $s \leq \tau_{101}$,

$$ N_{\tau_{101}}^s = \begin{cases} 1 & \text{if } s = \tau_{101} - 2 \\ 7 & \text{if } s = \tau_{101} \\ -1 & \text{otherwise.} \end{cases} $$

Therefore, the net profit to all gamblers after the first $t$ games equals $N_t := \sum_{s=1}^{t} N_t^s$, and $N_{\tau_{101}} = 10 - \tau_{101}$. Let $A_r = \sum_{s=1}^{\infty} A_r^s = \sum_{s=r-2}^{r} A_r^s$ be the total amount wagered on heads by all gamblers on game $r$. Observe that $N_t = \sum_{r=1}^{t} A_r(M_r - M_{r-1})$. Since $\tau_{101}/3$ is bounded by a Geometric$(1/8)$ random variable, we have $\mathbf{E}(\tau_{101}) < \infty$. The sequence $(N_t)_{t=0}^{\infty}$ is a martingale with bounded increments (see Theorem 17.4). By the Optional Stopping Theorem (Corollary 17.8),

$$ 0 = \mathbf{E}(N_{\tau_{101}}) = 10 - \mathbf{E}(\tau_{101}) \, . $$

It is (sometimes) surprising to the non-expert that $\mathbf{E}(\tau_{HHH}) > \mathbf{E}(\tau_{HTH})$: modifying the argument above, so that each player bets on the sequence $HHH$, doubling his bet until he loses, the gambler entering at time $\tau - 2$ is paid 8 units, the gambler entering at time $\tau - 1$ is paid 4 units, and the gambler entering at $\tau_{HHH}$ is paid 2. Again, the total outlay is $\tau_{HHH}$, and fairness requires that $\mathbf{E}(\tau_{HHH}) = 8 + 4 + 2 = 14$.

**17.3.3. Exponential martingales and hitting times.** Let $(S_t)$ be a simple random walk on $\mathbb{Z}$. For $\mathcal{F}_t = \sigma(S_0, \ldots, S_t)$,

$$ \mathbf{E}[e^{\lambda S_{t+1}} \mid \mathcal{F}_t] = e^{\lambda S_t} \left( \frac{e^{\lambda} + e^{-\lambda}}{2} \right) = e^{\lambda S_t} \cosh(\lambda) \, , $$

whence $M_t = e^{\lambda S_t}[\cosh(\lambda)]^{-t}$ is a martingale.

### PDF page 265 (book page 249)

Letting $f(\lambda; t, x) := e^{\lambda x}[\cosh(\lambda)]^{-t}$, write the power series representation of $f$ in $\lambda$ as

$$ f(\lambda; t, x) = \sum_{k=0}^{\infty} a_k(t, x)\lambda^k \, . $$

Thus for all $\lambda$,

$$ \sum_{k=0}^{\infty} a_k(t, S_t)\lambda^k = M_t = \mathbf{E}[M_{t+1} \mid \mathcal{F}_t] = \sum_{k=0}^{\infty} \mathbf{E}[a_k(t + 1, S_{t+1}) \mid \mathcal{F}_t]\lambda^k \, . $$

Since the coefficients in the power series representation are unique, $(a_k(t, S_t))_{t=0}^{\infty}$ is a martingale for each $k$.

We have $a_2(t, x) = (x^2 - t)/2$, whence $Y_t = S_t^2 - t$ is a martingale, as already used to derive (17.11). If $\tau = \min\{t \geq 0 \, : \, S_t = \pm L\}$, we can use the martingale $24a_4(t, S_t)$ to find Var$(\tau)$. By Exercise 17.2,

$$ 24 \cdot a_4(t, S_t) = S_t^4 - 6tS_t^2 + 3t^2 + 2t \, . $$

Optional Stopping (together with the Dominated and Monotone Convergence Theorems) yields

$$ 0 = L^4 - 6\mathbf{E}_0(\tau)L^2 + 3\mathbf{E}_0(\tau^2) + 2\mathbf{E}_0(\tau) = -5L^4 + 3\mathbf{E}_0(\tau^2) + 2L^2 \, . $$

Solving for $\mathbf{E}_0(\tau^2)$ gives

$$ \mathbf{E}_0(\tau^2) = (5L^4 - 2L^2)/3 \, , $$

and so (using $\mathbf{E}_0(\tau) = L^2$ from (17.11))

$$ \text{Var}_0(\tau) = (2L^4 - 2L^2)/3 \, . \tag{17.12} $$

The martingale $a_3(t, S_t)$ is similarly exploited in Exercise 17.1.

### **17.4. Evolving Sets**

For a lazy *reversible* Markov chain, combining Theorem 12.4 with Theorem 13.10 shows that

$$ t_{\text{mix}}(\varepsilon) \leq t_{\text{mix}}^{(\infty)}(\varepsilon) \leq \frac{2}{\Phi_\star^2} \log \left( \frac{1}{\varepsilon\pi_{\min}} \right) $$

Here we give a direct proof for the same bound, not requiring reversibility, using evolving sets, a process introduced by Morris and Peres (**2005**) and defined below.

THEOREM 17.10. *Let $P$ be a lazy irreducible transition matrix, so that $P(x, x) \geq 1/2$ for all $x \in \mathcal{X}$, with stationary distribution $\pi$. The mixing time $t_{\text{mix}}(\varepsilon)$ satisfies*

$$ t_{\text{mix}}(\varepsilon) \leq t_{\text{mix}}^{(\infty)}(\varepsilon) \leq \frac{2}{\Phi_\star^2} \log \left( \frac{1}{\varepsilon\pi_{\min}} \right) . $$

REMARK 17.11. Suppose the chain is reversible. Combining the inequality (17.31), derived in the proof of Theorem 17.10, with the inequality (12.15) yields

$$ \frac{|\lambda|^t}{2} \leq d(t) \leq \frac{1}{\pi_{\min}} \left( 1 - \frac{\Phi_\star^2}{2} \right)^t , $$

where $\lambda$ is an eigenvalue of $P$ not equal to 1. Taking the $t$-th root on the left and right sides above and letting $t \to \infty$ shows that

$$ |\lambda| \leq 1 - \frac{\Phi_\star^2}{2}, $$

which yields the lower bound in Theorem 13.10 (but restricted to lazy chains).

### PDF page 266 (book page 250)

The proof proceeds by a series of lemmas. Recall that $Q(x, y) = \pi(x)P(x, y)$ and

$$ Q(A, B) = \sum_{\substack{x \in A \\ y \in B}} Q(x, y). $$

Observe that $Q(\mathcal{X}, y) = \pi(y)$.

The **evolving-set process** is a Markov chain on subsets of $\mathcal{X}$. Suppose the current state is $S \subset \mathcal{X}$. Let $U$ be a random variable which is uniform on $[0, 1]$. The next state of the chain is the set

$$ \tilde{S} = \left\{ y \in \mathcal{X} \, : \, \frac{Q(S, y)}{\pi(y)} \geq U \right\} . \tag{17.13} $$

This defines a Markov chain with state space $2^{\mathcal{X}}$, the collection of all subsets of $\mathcal{X}$. Note that the chain is not irreducible, because $\varnothing$ or $\mathcal{X}$ are absorbing states. From (17.13), it follows that

$$ \mathbf{P}\{y \in S_{t+1} \mid S_t\} = \frac{Q(S_t, y)}{\pi(y)}. \tag{17.14} $$

LEMMA 17.12. *If $(S_t)_{t=0}^{\infty}$ is the evolving-set process associated to the transition matrix $P$, then*

$$ P^t(x, y) = \frac{\pi(y)}{\pi(x)}\mathbf{P}_{\{x\}}\{y \in S_t\}. \tag{17.15} $$

PROOF. We prove this by induction on $t$. When $t = 0$, both sides of (17.15) equal $\mathbf{1}_{\{y=x\}}$.

Assume that (17.15) holds for $t = s$. By conditioning on the position of the chain after $s$ steps and then using the induction hypothesis, we have that

$$ P^{s+1}(x, y) = \sum_{z \in \mathcal{X}} P^s(x, z)P(z, y) = \sum_{z \in \mathcal{X}} \frac{\pi(z)}{\pi(x)}\mathbf{P}_{\{x\}}\{z \in S_s\}P(z, y). \tag{17.16} $$

By switching summation and expectation,

$$ \sum_{z \in \mathcal{X}} \pi(z)\mathbf{P}_{\{x\}}\{z \in S_s\}P(z, y) = \sum_{z \in \mathcal{X}} \mathbf{E}_{\{x\}} \left( \mathbf{1}_{\{z \in S_s\}}\pi(z)P(z, y) \right) $$

$$ = \mathbf{E}_{\{x\}} \left( \sum_{z \in S_s} Q(z, y) \right) = \mathbf{E}_{\{x\}} \left( Q(S_s, y) \right) . \tag{17.17} $$

From (17.14), (17.16), and (17.17),

$$ P^{s+1}(x, y) = \frac{1}{\pi(x)}\mathbf{E}_{\{x\}}(\pi(y)\mathbf{P}\{y \in S_{s+1} \mid S_s\}) = \frac{\pi(y)}{\pi(x)}\mathbf{P}_{\{x\}}\{y \in S_{s+1}\}. $$

Thus, (17.15) is proved for $t = s + 1$, and by induction, it must hold for all $t$. $\blacksquare$

LEMMA 17.13. *The sequence $\{\pi(S_t)\}$ is a martingale.*

PROOF. We have

$$ \mathbf{E}(\pi(S_{t+1}) \mid S_t) = \mathbf{E} \left( \sum_{z \in \mathcal{X}} \mathbf{1}_{\{z \in S_{t+1}\}}\pi(z) \, \Big| \, S_t \right) . $$

### PDF page 267 (book page 251)

By (17.14), the right-hand side above equals

$$ \sum_{z \in \mathcal{X}} \mathbf{P}\{z \in S_{t+1} \mid S_t\}\pi(z) = \sum_{z \in \mathcal{X}} Q(S_t, z) = Q(S_t, \mathcal{X}) = \pi(S_t), $$

which concludes the proof. $\blacksquare$

Recall that $\Phi(S) = Q(S, S^c)/\pi(S)$ is the bottleneck ratio of the set $S$, defined in Section 7.2.

LEMMA 17.14. *Suppose that the Markov chain is lazy, let $R_t = \pi(S_{t+1})/\pi(S_t)$, and let $(U_t)$ be a sequence of independent random variables, each uniform on $[0, 1]$, such that $S_{t+1}$ is generated from $S_t$ using $U_{t+1}$. Then*

$$ \mathbf{E}(R_t \mid U_{t+1} \le 1/2, \, S_t = S) = 1 + 2\Phi(S), \tag{17.18} $$

$$ \mathbf{E}(R_t \mid U_{t+1} > 1/2, \, S_t = S) = 1 - 2\Phi(S). \tag{17.19} $$

PROOF. Since the chain is lazy, $Q(y, y) \ge \pi(y)/2$, so if $y \notin S$, then

$$ \frac{Q(S, y)}{\pi(y)} = \sum_{x \in S} \frac{Q(x, y)}{\pi(y)} \le \sum_{\substack{x \in \mathcal{X} \\ x \ne y}} \frac{Q(x, y)}{\pi(y)} = 1 - \frac{Q(y, y)}{\pi(y)} \le \frac{1}{2}. \tag{17.20} $$

Given $U_{t+1} \le 1/2$, the distribution of $U_{t+1}$ is uniform on $[0, 1/2]$. By (17.20), for $y \notin S$,

$$ \mathbf{P}\left\{ \frac{Q(S, y)}{\pi(y)} \ge U_{t+1} \,\bigg|\, U_{t+1} \le 1/2, \, S_t = S \right\} = 2\frac{Q(S, y)}{\pi(y)}. $$

Since $y \in S_{t+1}$ if and only if $U_{t+1} \le Q(S_t, y)/\pi(y)$,

$$ \mathbf{P}\{y \in S_{t+1} \mid U_{t+1} \le 1/2, \, S_t = S\} = \frac{2Q(S, y)}{\pi(y)} \quad \text{for } y \notin S. \tag{17.21} $$

Also, since $Q(S, y)/\pi(y) \ge Q(y, y)/\pi(y) \ge 1/2$ for $y \in S$, it follows that

$$ \mathbf{P}\{y \in S_{t+1} \mid U_{t+1} \le 1/2, \, S_t = S\} = 1 \quad \text{for } y \in S. \tag{17.22} $$

We have

$$ \mathbf{E}\left(\pi(S_{t+1}) \mid U_{t+1} \le 1/2, \, S_t = S\right) = \mathbf{E}\left( \sum_{y \in \mathcal{X}} \mathbf{1}_{\{y \in S_{t+1}\}}\pi(y) \,\bigg|\, U_{t+1} \le 1/2, S_t = S \right) $$
$$ = \sum_{y \in S} \pi(y)\mathbf{P}\{y \in S_{t+1} \mid U_{t+1} \le 1/2, \, S_t = S\} $$
$$ + \sum_{y \notin S} \pi(y)\mathbf{P}\{y \in S_{t+1} \mid U_{t+1} \le 1/2, \, S_t = S\}. $$

By the above, (17.21), and (17.22),

$$ \mathbf{E}\left(\pi(S_{t+1}) \mid U_{t+1} \le 1/2, \, S_t = S\right) = \pi(S) + 2Q(S, S^c). \tag{17.23} $$

By Lemma 17.13 and (17.23),

$$ \pi(S) = \mathbf{E}(\pi(S_{t+1}) \mid S_t = S) $$
$$ = \frac{1}{2}\mathbf{E}(\pi(S_{t+1}) \mid U_{t+1} \le 1/2, \, S_t = S) + \frac{1}{2}\mathbf{E}(\pi(S_{t+1}) \mid U_{t+1} > 1/2, \, S_t = S) $$
$$ = \frac{\pi(S)}{2} + Q(S, S^c) + \frac{1}{2}\mathbf{E}(\pi(S_{t+1}) \mid U_{t+1} > 1/2, \, S_t = S). $$

### PDF page 268 (book page 252)

Rearranging shows that

$$ \mathbf{E}(\pi(S_{t+1}) \mid U_{t+1} > 1/2, \, S_t = S) = \pi(S) - 2Q(S, S^c). \tag{17.24} $$

Dividing both sides of (17.23) and (17.24) by $\pi(S)$ yields (17.18) and (17.19), respectively. $\blacksquare$

LEMMA 17.15. *For $\alpha \in [0, 1/2]$,*

$$ \frac{\sqrt{1 + 2\alpha} + \sqrt{1 - 2\alpha}}{2} \le \sqrt{1 - \alpha^2} \le 1 - \frac{\alpha^2}{2}. $$

Squaring proves the right-hand inequality, and reduces the left-hand inequality to

$$ \sqrt{1 - 4\alpha^2} \le 1 - 2\alpha^2 \,, $$

which is the right-hand inequality with $2\alpha$ replacing $\alpha$.

LEMMA 17.16. *Let $(S_t)$ be the evolving-set process. If*

$$ S_t^{\sharp} = \begin{cases} S_t & \text{if } \pi(S_t) \le 1/2, \\ S_t^c & \text{otherwise,} \end{cases} \tag{17.25} $$

*then*

$$ \mathbf{E}\left( \sqrt{\pi(S_{t+1}^{\sharp})/\pi(S_t^{\sharp})} \,\bigg|\, S_t \right) \le 1 - \frac{\Phi_\star^2}{2}. \tag{17.26} $$

PROOF. First, letting $R_t := \pi(S_{t+1})/\pi(S_t)$, applying Jensen's inequality shows that

$$ \mathbf{E}\left( \sqrt{R_t} \mid S_t = S \right) = \frac{\mathbf{E}\left(\sqrt{R_t} \,\big|\, U_{t+1} \le 1/2, \, S_t = S\right) + \mathbf{E}\left(\sqrt{R_t} \,\big|\, U_{t+1} > 1/2, \, S_t = S\right)}{2} $$
$$ \le \frac{\sqrt{\mathbf{E}\left(R_t \mid U_{t+1} \le 1/2, \, S_t = S\right)} + \sqrt{\mathbf{E}\left(R_t \mid U_{t+1} > 1/2, \, S_t = S\right)}}{2}. $$

Applying Lemma 17.14 and Lemma 17.15 shows that, for $\pi(S) \le 1/2$,

$$ \mathbf{E}\left( \sqrt{R_t} \,\big|\, S_t = S \right) \le \frac{\sqrt{1 + 2\Phi(S)} + \sqrt{1 - 2\Phi(S)}}{2} \le 1 - \frac{\Phi(S)^2}{2} \le 1 - \frac{\Phi_\star^2}{2}. \tag{17.27} $$

Now assume that $\pi(S_t) \le 1/2$. Then

$$ \sqrt{\pi(S_{t+1}^{\sharp})/\pi(S_t^{\sharp})} = \sqrt{\pi(S_{t+1}^{\sharp})/\pi(S_t)} \le \sqrt{\pi(S_{t+1})/\pi(S_t)}, $$

and (17.26) follows from (17.27). If $\pi(S_t) > 1/2$, then replace $S_t$ by $S_t^c$ in the previous argument. (If $(S_t)$ is an evolving-set process started from $S$, then $(S_t^c)$ is also an evolving-set process started from $S^c$.) $\blacksquare$

PROOF OF THEOREM 17.10. From Lemma 17.16,

$$ \mathbf{E}\left( \sqrt{\pi(S_{t+1}^{\sharp})} \right) \le \mathbf{E}\left( \sqrt{\pi(S_t^{\sharp})} \right) \left( 1 - \frac{\Phi_\star^2}{2} \right). $$

Iterating,

$$ \mathbf{E}_S\left( \sqrt{\pi(S_t^{\sharp})} \right) \le \left( 1 - \frac{\Phi_\star^2}{2} \right)^t \sqrt{\pi(S)}. $$

### PDF page 269 (book page 253)

Since $\sqrt{\pi_{\min}} \, \mathbf{P}_S\{S_t^{\sharp} \ne \varnothing\} \le \mathbf{E}_S\left( \sqrt{\pi(S_t^{\sharp})} \right)$, we have

$$ \mathbf{P}_S\{S_t^{\sharp} \ne \varnothing\} \le \sqrt{\frac{\pi(S)}{\pi_{\min}}} \left( 1 - \frac{\Phi_\star^2}{2} \right)^t. \tag{17.28} $$

Since $\{S_t^{\sharp} \ne \varnothing\} \supset \{S_{t+1}^{\sharp} \ne \varnothing\}$, by (17.28),

$$ \mathbf{P}_S\{S_t^{\sharp} \ne \varnothing \text{ for all } t \ge 0\} = \mathbf{P}_S\left( \bigcap_{t=1}^{\infty} \{S_t^{\sharp} \ne \varnothing\} \right) = \lim_{t \to \infty} \mathbf{P}_S\{S_t^{\sharp} \ne \varnothing\} = 0. $$

That is, $(S_t^{\sharp})$ is eventually absorbed in the state $\varnothing$. Let

$$ \tau = \min\{t \ge 0 \,:\, S_t^{\sharp} = \varnothing\}. $$

We have $S_\tau \in \{\varnothing, \mathcal{X}\}$ and $\pi(S_\tau) = \mathbf{1}_{\{S_\tau = \mathcal{X}\}}$. Note that by Lemma 17.13 and the Optional Stopping Theorem (Corollary 17.7),

$$ \pi(x) = \mathbf{E}_{\{x\}}(\pi(S_0)) = \mathbf{E}_{\{x\}}(\pi(S_\tau)) = \mathbf{P}_{\{x\}}\{S_\tau = \mathcal{X}\}. \tag{17.29} $$

By (17.29) and Lemma 17.12,

$$ |P^t(x, y) - \pi(y)| = \frac{\pi(y)}{\pi(x)} \left| \mathbf{P}_{\{x\}}\{y \in S_t\} - \pi(x) \right| $$
$$ = \frac{\pi(y)}{\pi(x)} \left| \mathbf{P}_{\{x\}}\{y \in S_t\} - \mathbf{P}_{\{x\}}\{S_\tau = \mathcal{X}\} \right|. \tag{17.30} $$

Using the identity

$$ \mathbf{P}_{\{x\}}\{y \in S_t\} = \mathbf{P}_{\{x\}}\{y \in S_t, \, \tau > t\} + \mathbf{P}_{\{x\}}\{y \in S_t, \tau \le t\} $$
$$ = \mathbf{P}_{\{x\}}\{y \in S_t, \, \tau > t\} + \mathbf{P}_{\{x\}}\{S_\tau = \mathcal{X}, \tau \le t\} $$

in (17.30) shows that

$$ |P^t(x, y) - \pi(y)| = \frac{\pi(y)}{\pi(x)} \left| \mathbf{P}_{\{x\}}\{y \in S_t, \, \tau > t\} - \mathbf{P}_{\{x\}}\{S_\tau = \mathcal{X}, \, \tau > t\} \right| $$
$$ \le \frac{\pi(y)}{\pi(x)}\mathbf{P}_{\{x\}}\{\tau > t\}. $$

Combining with (17.28), and recalling the definition of $d^{(\infty)}(t)$ in (4.36),

$$ d(t) \le d^{(\infty)}(t) \le \max_{x, y} \frac{|P^t(x, y) - \pi(y)|}{\pi(y)} \le \frac{1}{\pi_{\min}} \left( 1 - \frac{\Phi_\star^2}{2} \right)^t. \tag{17.31} $$

It follows that if $t \ge \frac{2}{\Phi_\star^2} \log\left( \frac{1}{\varepsilon \pi_{\min}} \right)$, then $d(t) \le d^{(\infty)}(t) \le \varepsilon$. $\blacksquare$

**17.5. A General Bound on Return Probabilities**

The goal in this section is to prove the following:

THEOREM 17.17. *Let $P$ be the transition matrix for a lazy random walk on a graph with maximum degree $\Delta$. Then*

$$ |P^t(x, x) - \pi(x)| \le \frac{3\Delta^{5/2}}{\sqrt{t}}. \tag{17.32} $$

REMARK 17.18. The dependence on $\Delta$ in (17.32) is not the best possible. It can be shown that an upper bound of $\Delta/\sqrt{t}$ holds. See Lemma 3.4 of **Lyons (2005)**.

### PDF page 270 (book page 254)

We will need the following result about martingales, which is itself of independent interest:

**PROPOSITION 17.19.** *Let $(M_t)$ be a non-negative martingale with respect to $\{\mathcal{F}_t\}$, and define*
$$ T_h := \min\{t \geq 0 \,:\, M_t = 0 \text{ or } M_t \geq h\}. $$
*Assume that*

(i) $\mathrm{Var}(M_{t+1} \mid \mathcal{F}_t) \geq \sigma^2$ *for all $t \geq 0$, and*

(ii) *for some $D$ and all $h > 0$, we have $M_{T_h} \leq D \cdot h$.*

*Let $\tau = \min\{t \geq 0 \,:\, M_t = 0\}$. If $M_0$ is a constant, then for all $t \geq 1$,*
$$ \mathbf{P}\{\tau \geq t\} \leq \frac{2M_0}{\sigma}\sqrt{\frac{D}{t}}. \tag{17.33} $$

*PROOF.* For $h \geq M_0$, we have that $\{\tau \geq t\} \subseteq \{T_h \geq t\} \cup \{M_{T_h} \geq h\}$, whence
$$ \mathbf{P}\{\tau \geq t\} \leq \mathbf{P}\{T_h \geq t\} + \mathbf{P}\{M_{T_h} \geq h\}. \tag{17.34} $$
We first bound $\mathbf{P}\{M_{T_h} \geq h\}$. Since $(M_{t \wedge T_h})$ is bounded, by the Optional Stopping Theorem,
$$ M_0 = \mathbf{E}M_{T_h} \geq h\mathbf{P}\{M_{T_h} \geq h\}, $$
whence
$$ \mathbf{P}\{M_{T_h} \geq h\} \leq \frac{M_0}{h}. \tag{17.35} $$
We now bound $\mathbf{P}\{T_h \geq t\}$. Let $G_t := M_t^2 - hM_t - \sigma^2 t$. The sequence $(G_t)$ is a submartingale, by (i). Note that for $t \leq T_h$, the hypothesis (ii) implies that
$$ M_t^2 - hM_t = (M_t - h)M_t \leq (D-1)hM_t; $$
therefore,
$$ \mathbf{E}(M_{t \wedge T_h}^2 - hM_{t \wedge T_h}) \leq (D-1)hM_0. $$
Since $(G_{t \wedge T_h})$ is a submartingale,
$$ \begin{aligned} -hM_0 \leq G_0 \leq \mathbf{E}G_{t \wedge T_h} &= \mathbf{E}(M_{t \wedge T_h}^2 - hM_{t \wedge T_h}) - \sigma^2\mathbf{E}(t \wedge T_h) \\ &\leq (D-1)hM_0 - \sigma^2\mathbf{E}(t \wedge T_h). \end{aligned} $$
We conclude that $\mathbf{E}(t \wedge T_h) \leq \frac{DhM_0}{\sigma^2}$. Letting $t \to \infty$, by the Monotone Convergence Theorem, $\mathbf{E}T_h \leq \frac{DhM_0}{\sigma^2}$. By Markov's inequality,
$$ \mathbf{P}\{T_h \geq t\} \leq \frac{DhM_0}{\sigma^2 t}. $$
Combining the above bound with with [sic] (17.34) and (17.35) shows that
$$ \mathbf{P}\{\tau \geq t\} \leq \frac{M_0}{h} + \frac{DhM_0}{\sigma^2 t}. $$
We may assume that the right-hand side of (17.33) is less than 1. We take $h = \sqrt{t\sigma^2/D} \geq M_0$ to optimize the above bound. This proves the inequality (17.33). $\blacksquare$

Many variants of the above proposition are useful in applications. We state one here.

**PROPOSITION 17.20.** *Let $(Z_t)_{t \geq 0}$ be a non-negative supermartingale with respect to $\{\mathcal{F}_t\}$, and let $\tau$ be a stopping time for $\{\mathcal{F}_t\}$. Suppose that*

(i) $Z_0 = k$,

### PDF page 271 (book page 255)

(ii) *there exists $B$ such that $|Z_{t+1} - Z_t| \leq B$ for all $t \geq 0$,*

(iii) *there exists a constant $\sigma^2 > 0$ such that, for each $t \geq 0$, the inequality $\mathrm{Var}(Z_{t+1} \mid \mathcal{F}_t) \geq \sigma^2$ holds on the event $\{\tau > t\}$.*

*If $u > 12B^2/\sigma^2$, then*
$$ \mathbf{P}_k\{\tau > u\} \leq \frac{4k}{\sigma\sqrt{u}}. $$

The proof follows the same outline as the proof of Proposition 17.19 and is left to the reader in Exercise 17.4.

We now prove the principal result of this section.

*PROOF OF THEOREM 17.17.* Let $(S_t)$ be the evolving-set process associated to the Markov chain with transition matrix $P$, started from $S_0 = \{x\}$. Define
$$ \tau := \min\{t \geq 0 \,:\, S_t \in \{\varnothing, \mathcal{X}\}\}. $$
Observe that, since $\pi(S_t)$ is a martingale,
$$ \pi(x) = \mathbf{E}_{\{x\}}\pi(S_0) = \mathbf{E}_{\{x\}}\pi(S_\tau) = \mathbf{P}_{\{x\}}\{x \in S_\tau\}. $$
By Lemma 17.12, $P^t(x,x) = \mathbf{P}_{\{x\}}\{x \in S_t\}$. Therefore,
$$ |P^t(x,x) - \pi(x)| = |\mathbf{P}_{\{x\}}\{x \in S_t\} - \mathbf{P}_{\{x\}}\{x \in S_\tau\}| \leq \mathbf{P}_{\{x\}}\{\tau > t\}. $$

Since conditioning always reduces variance,
$$ \mathrm{Var}_S(\pi(S_1)) \geq \mathrm{Var}_S\left(\mathbf{E}(\pi(S_1) \mid \mathbf{1}_{\{U_1 \leq 1/2\}})\right). $$
Note that (see Lemma 17.14)
$$ \mathbf{E}_S(\pi(S_1) \mid \mathbf{1}_{\{U_1 \leq 1/2\}}) = \begin{cases} \pi(S) + 2Q(S, S^c) & \text{with probability } 1/2, \\ \pi(S) - 2Q(S, S^c) & \text{with probability } 1/2. \end{cases} $$
Therefore, provided $S \notin \{\varnothing, \mathcal{X}\}$,
$$ \mathrm{Var}_S\left(\mathbf{E}(\pi(S_1) \mid \mathbf{1}_{\{U_1 \leq 1/2\}})\right) = 4Q(S, S^c)^2 \geq \frac{1}{n^2\Delta^2}. $$
The last inequality follows since if $S \notin \{\varnothing, \mathcal{X}\}$, then there exists $z, w$ such that $z \in S$, $w \notin S$ and $P(z,w) > 0$, whence
$$ Q(S, S^c) \geq \pi(z)P(z,w) \geq \frac{\deg(z)}{2E}\frac{1}{2\deg(z)} \geq \frac{1}{4E} \geq \frac{1}{2n\Delta}. $$

Note that $\pi(S_{t+1}) \leq (\Delta + 1)\pi(S_t)$. Therefore, we can apply Proposition 17.19 with $D = \Delta + 1$ and $M_0 \leq \Delta/n$ to obtain the inequality (17.32). $\blacksquare$

**17.6. Harmonic Functions and the Doob $h$-Transform**

Recall that a function $h : \mathcal{X} \to \mathbb{R}$ is harmonic for $P$ if $Ph = h$. The connection between harmonic functions, Markov chains, and martingales is that if $(X_t)$ is a Markov chain with transition matrix $P$ and $h$ is a $P$-harmonic function, then $M_t = h(X_t)$ defines a martingale with respect to the natural filtration $\{\mathcal{F}_t\}$:
$$ \mathbf{E}\left(M_{t+1} \mid \mathcal{F}_t\right) = \mathbf{E}\left(h(X_{t+1}) \mid X_t\right) = Ph(X_t) = h(X_t) = M_t. $$

### PDF page 272 (book page 256)

**17.6.1. Conditioned Markov chains and the Doob transform.** Let $P$ be a Markov chain such that the set $B$ is absorbing: $P(x,x) = 1$ for $x \in B$. Let $h : \mathcal{X} \to [0,\infty)$ be harmonic and positive on $\mathcal{X} \setminus B$, and define, for $x \notin B$ and $y \in \mathcal{X}$,
$$ \check{P}(x,y) := \frac{P(x,y)h(y)}{h(x)}. $$
Note that for $x \notin B$,
$$ \sum_{y \in \mathcal{X}} \check{P}(x,y) = \frac{1}{h(x)}\sum_{y \in \mathcal{X}} h(y)P(x,y) = \frac{Ph(x)}{h(x)} = 1. $$
If $x \in B$, then set $\check{P}(x,x) = 1$. Therefore, $\check{P}$ is a transition matrix, called the **Doob $h$-transform** of $P$.

Let $P$ be a transition matrix, and assume that the states $a$ and $b$ are absorbing. Let $h(x) := \mathbf{P}_x\{\tau_b < \tau_a\}$, and assume that $h(x) > 0$ for $x \neq a$. Since $h(x) = \mathbf{E}_x\mathbf{1}_{\{X_{\tau_a \wedge \tau_b} = b\}}$, Proposition 9.1 shows that $h$ is harmonic on $\mathcal{X} \setminus \{a,b\}$, whence we can define the Doob $h$-transform $\check{P}$ of $P$. Observe that for $x \neq a$,
$$ \begin{aligned} \check{P}(x,y) &= \frac{P(x,y)\mathbf{P}_y\{\tau_b < \tau_a\}}{\mathbf{P}_x\{\tau_b < \tau_a\}} \\ &= \frac{\mathbf{P}_x\{X_1 = y,\ \tau_b < \tau_a\}}{\mathbf{P}_x\{\tau_b < \tau_a\}} \\ &= \mathbf{P}_x\{X_1 = y \mid \tau_b < \tau_a\}, \end{aligned} $$
so the chain with matrix $\check{P}$ is the original chain conditioned to hit $b$ before $a$.

**EXAMPLE 17.21** (Conditioning the evolving-set process). Given a transition matrix $P$ on $\mathcal{X}$, consider the corresponding evolving-set process $(S_t)$. Let $\tau := \min\{t \,:\, S_t \in \{\varnothing, \mathcal{X}\}\}$. Since $\{\pi(S_t)\}$ is a martingale, the Optional Stopping Theorem implies that
$$ \pi(A) = \mathbf{E}_A\pi(S_\tau) = \mathbf{P}_A\{S_\tau = \mathcal{X}\}. $$

If $K$ is the transition matrix of $(S_t)$, then the Doob transform of $(S_t)$ conditioned to be absorbed in $\mathcal{X}$ has transition matrix
$$ \check{K}(A,B) = \frac{\pi(B)}{\pi(A)}K(A,B). \tag{17.36} $$

**EXAMPLE 17.22** (Simple random walk on $\{0,1,\ldots,n\}$). Consider the simple random walk on $\{0,1,\ldots,n\}$ with absorbing states 0 and $n$. Since $\mathbf{P}_k\{\tau_n < \tau_0\} = k/n$, the transition matrix for the process conditioned to absorb at $n$ is
$$ \check{P}(x,y) = \frac{y}{x}P(x,y) \quad \text{ for } 0 < x < n. $$

**17.7. Strong Stationary Times from Evolving Sets**

The goal of this section is to construct a strong stationary time by coupling a Markov chain with the conditioned evolving-set process of Example 17.21. This construction is due to **Diaconis and Fill (1990)**.

The idea is to start with $X_0 = x$ and $S_0 = \{x\}$ and run the Markov chain $(X_t)$ and the evolving-set process $(S_t)$ together, at each stage conditioning on $X_t \in S_t$.

### PDF page 273 (book page 257)

Let $P$ be an irreducible transition matrix, and let $K$ be the transition matrix for the associated evolving-set process. The matrix $\check{K}$ denotes the evolving-set process conditioned to be absorbed in $\mathcal{X}$. (See Example 17.21.)

For $y \in \mathcal{X}$, define the transition matrix on $2^{\mathcal{X}}$ by

$$ J_y(A, B) := \mathbf{P}_A\{S_1 = B \mid y \in S_1\}\mathbf{1}_{\{y \in B\}}. $$

From (17.14) it follows that $J_y(A, B) = K(A, B)\pi(y)\mathbf{1}_{\{y \in B\}}/Q(A, y)$. Define the transition matrix $P^\star$ on $\mathcal{X} \times 2^{\mathcal{X}}$ by

$$ \begin{aligned} P^\star((x, A), (y, B)) &:= P(x, y)J_y(A, B) \\ &= \frac{P(x, y)K(A, B)\pi(y)\mathbf{1}_{\{y \in B\}}}{Q(A, y)}. \end{aligned} $$

Let $\{(X_t, S_t)\}$ be a Markov chain with transition matrix $P^\star$, and let $\mathbf{P}^\star$ denote the probability measure on the space where $\{(X_t, S_t)\}$ is defined.

Observe that

$$ \sum_{B \,:\, y \in B} P^\star\left((x, A), (y, B)\right) = P(x, y)\frac{\pi(y)}{Q(A, y)} \sum_{B \,:\, y \in B} K(A, B). \tag{17.37} $$

The sum $\sum_{B \,:\, y \in B} K(A, B)$ is the probability that the evolving-set process started from $A$ contains $y$ at the next step. By (17.14) this equals $Q(A, y)/\pi(y)$, whence (17.37) says that

$$ \sum_{B \,:\, y \in B} P^\star\left((x, A), (y, B)\right) = P(x, y). \tag{17.38} $$

It follows that $(X_t)$ is a Markov chain with transition matrix $P$.

THEOREM 17.23 (**Diaconis and Fill (1990)**). *We abbreviate* $\mathbf{P}^\star_{x,\{x\}}$ *by* $\mathbf{P}^\star_x$.

(i) *If* $\{(X_t, S_t)\}$ *is a Markov chain with transition matrix* $P^\star$ *started from* $(x, \{x\})$, *then the sequence* $(S_t)$ *is a Markov chain started from* $\{x\}$ *with transition matrix* $\check{K}$.

(ii) *For* $w \in S_t$,

$$ \mathbf{P}^\star_x\{X_t = w \mid S_0, \ldots, S_t\} = \frac{\pi(w)}{\pi(S_t)}. $$

PROOF. We use induction on $t$. When $t = 0$, both (i) and (ii) are obvious. For the induction step, we assume that for some $t \geq 0$, the sequence $(S_j)_{j=0}^t$ is a Markov chain with transition matrix $\check{K}$ and that (ii) holds. Our goal is to verify (i) and (ii) with $t + 1$ in place of $t$.

We write $\boldsymbol{S}_t$ for the vector $(S_0, \ldots, S_t)$. Because the process $(X_t, S_t)$ is a Markov chain with transition matrix $P^\star$, if $\boldsymbol{s}_t = (s_0, s_1, \ldots, s_t)$ and $v \in B$, then

$$ \begin{aligned} \mathbf{P}^\star\{X_{t+1} = v,\, S_{t+1} = B \mid X_t = w,\, \boldsymbol{S}_t = \boldsymbol{s}_t\} &= P^\star\left((w, s_t), (v, B)\right) \\ &= \frac{P(w, v)K(s_t, B)\pi(v)}{Q(S_t, v)}. \end{aligned} \tag{17.39} $$

### PDF page 274 (book page 258)

Summing (17.39) over $w$ and using the induction hypothesis shows that, for $v \in B$,

$$ \begin{aligned} \mathbf{P}^\star_x\{X_{t+1} = v,\, S_{t+1} = B \mid \boldsymbol{S}_t\} &= \sum_{w \in S_t} \frac{P(w, v)K(S_t, B)\pi(v)}{Q(S_t, v)} \frac{\pi(w)}{\pi(S_t)} \\ &= \frac{\pi(v)}{\pi(S_t)} \frac{\sum_{w \in S_t} \pi(w)P(w, v)}{Q(S_t, v)}K(S_t, B) \\ &= \frac{\pi(v)}{\pi(S_t)}K(S_t, B). \end{aligned} \tag{17.40} $$

Summing over $v \in B$ gives

$$ \mathbf{P}^\star_x\{S_{t+1} = B \mid S_0, \ldots, S_t\} = \frac{\pi(B)K(S_t, B)}{\pi(S_t)} \tag{17.41} $$

$$ = \check{K}(S_t, B), \tag{17.42} $$

where (17.42) follows from (17.36). Therefore, $(S_j)_{j=0}^{t+1}$ is a Markov chain with transition matrix $\check{K}$, which verifies (i) with $t + 1$ replacing $t$.

Taking the ratio of (17.40) and (17.41) shows that

$$ \mathbf{P}^\star_x\{X_{t+1} = v \mid \boldsymbol{S}_t,\, S_{t+1} = B\} = \frac{\pi(v)}{\pi(B)}, $$

which completes the induction step. $\blacksquare$

COROLLARY 17.24. *For the process* $\{(X_t, S_t)\}$ *with law* $\mathbf{P}^\star_x$, *consider the absorption time*

$$ \tau^\star := \min\{t \geq 0 \,:\, S_t = \mathcal{X}\}. $$

*Then* $\tau^\star$ *is a strong stationary time for* $(X_t)$.

PROOF. This follows from Theorem 17.23(ii): summing over all sequences of sets $(A_1, \ldots, A_t)$ with $A_i \neq \mathcal{X}$ for $i < t$ and $A_t = \mathcal{X}$,

$$ \begin{aligned} \mathbf{P}^\star_x\{\tau^\star = t,\, X_t = w\} &= \sum \mathbf{P}^\star_x\{(S_1, \ldots, S_t) = (A_1, \ldots, A_t),\, X_t = w\} \\ &= \sum \mathbf{P}^\star_x\{(S_1, \ldots, S_t) = (A_1, \ldots, A_t)\}\pi(w) \\ &= \mathbf{P}^\star\{\tau^\star = t\}\pi(w). \end{aligned} $$

$\blacksquare$

EXAMPLE 17.25. Suppose the base Markov chain is simple random walk on $\{0, 1, \ldots, n\}$ with loops at $0$ and $n$; the stationary distribution $\pi$ is uniform. In this case we have $S_t = [0, Y_t)$, where $(Y_t)$ satisfies

$$ \begin{aligned} \mathbf{P}\{Y_{t+1} = Y_t + 1 \mid Y_t\} &= \mathbf{P}\{Y_t \in S_{t+1} \mid S_t = [0, Y_t)\} \\ &= \frac{1}{2} \\ &= \mathbf{P}\{Y_{t+1} = Y_t - 1 \mid Y_t\}. \end{aligned} $$

Therefore, $(Y_t)$ is a simple random walk on $\{0, \ldots, n + 1\}$ with absorption at endpoints.

### PDF page 275 (book page 259)

We deduce that the absorption time $\tau^\star$ when started from $S_0 = \{0\}$ is the absorption time of the simple random walk $(Y_t)$ conditioned to hit $n + 1$ before $0$ when started at $Y_0 = 1$. Thus, by Exercise 17.1,

$$ \mathbf{E}^\star\tau^\star = \frac{(n + 1)^2 - 1}{3} = \frac{n^2 + 2n}{3}. $$

Since, by Corollary 17.24, $\tau^\star$ is a strong stationary time for $(X_t)$, we conclude that $t_{\text{mix}} = O(n^2)$.

EXAMPLE 17.26. Consider a lazy birth-and-death process on $\{0, 1, \ldots, n\}$, started from $\{0\}$. For the process $(X_t, S_t)$ in 17.23, the process $\{S_t\}$ is always a connected segment. Thus any state with $X_t = n$ is a halting state, and so the time $\tau^\star$ is optimal by Proposition 6.14.

**Exercises**

EXERCISE 17.1. Let $(X_t)$ be the simple random walk on $\mathbb{Z}$.

(a) Show that $M_t = X_t^3 - 3tX_t$ is a martingale.

(b) Let $\tau$ be the time when the walker first visits either $0$ or $n$. Show that for $0 \leq k \leq n$,

$$ \mathbf{E}_k(\tau \mid X_\tau = n) = \frac{n^2 - k^2}{3}. $$

EXERCISE 17.2. Let

$$ e^{\lambda x} \cosh(\lambda)^{-t} = \sum_{k=0}^{\infty} a_k(t, x)\lambda^k \,. $$

Show

(a) $a_2(t, x) = (x^2 - t)/2$,

(b) $a_3(t, x) = x^3/6 - xt/2$ (cf. Exercise 17.1),

(c) $a_4(t, x) = \frac{x^4 - 6tx^2 + 3t^2 + 2t}{24}$.

(The last one completes the derivation of (17.12).)

EXERCISE 17.3. Let $(X_t)$ be a supermartingale. Show that there is a martingale $(M_t)$ and a non-decreasing previsible sequence $(A_t)$ so that $X_t = M_t - A_t$. This is called the ***Doob decomposition*** of $(X_t)$.

EXERCISE 17.4. Prove Proposition 17.20.

*Hint:* Use the Doob decomposition $Z_t = M_t - A_t$ (see Exercise 17.3), and modify the proof of Proposition 17.19 applied to $M_t$.

EXERCISE 17.5. Show that for lazy birth-and-death chains on $\{0, 1, \ldots, n\}$, the evolving-set process started with $S_0 = \{0\}$ always has $S_t = [0, Y_t)$ or $S_t = \varnothing$.

**Notes**

Doob was the first to call processes that satisfy the conditional expectation property

$$ \mathbf{E}(M_{t+1} \mid M_1, \ldots, M_t) = M_t $$

"martingales". The term was used previously by gamblers to describe certain betting schemes.

See **Williams (1991)** for a friendly introduction to martingales and **Doob (1953)** for a detailed history.

For much more on the waiting time for patterns in coin tossing, see **Li (1980)**.

### PDF page 276 (book page 260)

**Evolving sets.** Define $\Phi(r)$ for $r \geq \pi_{\min}$ by

$$ \Phi(r) := \inf \left\{ \Phi(S) \, : \, \pi(S) \leq r \wedge \frac{1}{2} \right\} . \tag{17.43} $$

For reversible, irreducible, and lazy chains, **Lovász and Kannan (1999)** proved that

$$ t_{\mathrm{mix}} \leq 2000 \int_{\pi_{\min}}^{3/4} \frac{du}{u\Phi^2(u)}. \tag{17.44} $$

**Morris and Peres (2005)** sharpened this, using evolving sets, to obtain the following:

THEOREM. *For lazy irreducible Markov chains, if*

$$ t \geq 1 + \int_{4(\pi(x)\wedge\pi(y))}^{4/\varepsilon} \frac{4du}{u\Phi^2(u)}, $$

*then*

$$ \left| \frac{P^t(x,y) - \pi(y)}{\pi(y)} \right| \leq \varepsilon. $$

Note that this theorem does *not* require reversibility.

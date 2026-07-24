# Chapter 3 — Markov Chain Monte Carlo: Metropolis and Glauber Chains
*(PDF pages 54–62; book pages 38–46)*

### PDF page 54 (book page 38)

CHAPTER 3

# Chapter 3 — Markov Chain Monte Carlo: Metropolis and Glauber Chains

**3.1. Introduction**

Given an irreducible transition matrix $P$, there is a unique stationary distribution $\pi$ satisfying $\pi = \pi P$, which we constructed in Section 1.5. We now consider the inverse problem: given a probability distribution $\pi$ on $\mathcal{X}$, can we find a transition matrix $P$ for which $\pi$ is its stationary distribution? The following example illustrates why this is a natural problem to consider.

A ***random sample*** from a finite set $\mathcal{X}$ will mean a random uniform selection from $\mathcal{X}$, i.e., one such that each element has the same chance $1/|\mathcal{X}|$ of being chosen.

Fix a set $\{1, 2, \ldots, q\}$ of *colors*. A ***proper $q$-coloring*** of a graph $G = (V, E)$ is an assignment of colors to the vertices $V$, subject to the constraint that neighboring vertices do not receive the same color. There are (at least) two reasons to look for an efficient method to sample from $\mathcal{X}$, the set of all proper $q$-colorings. If a random sample can be produced, then the size of $\mathcal{X}$ can be estimated (as we discuss in detail in Section 14.4.2). Also, if it is possible to sample from $\mathcal{X}$, then average characteristics of colorings can be studied via simulation.

For some graphs, e.g. trees, there are simple recursive methods for generating a random proper coloring (see Example 14.12). However, for other graphs it can be challenging to directly construct a random sample. One approach is to use Markov chains to sample: suppose that $(X_t)$ is a chain with state space $\mathcal{X}$ and with stationary distribution uniform on $\mathcal{X}$ (in Section 3.3, we will construct one such chain). By the Convergence Theorem (Theorem 4.9, whose proof we have not yet given but have often foreshadowed), $X_t$ is approximately uniformly distributed when $t$ is large.

This method of sampling from a given probability distribution is called ***Markov chain Monte Carlo***. Suppose $\pi$ is a probability distribution on $\mathcal{X}$. If a Markov chain $(X_t)$ with stationary distribution $\pi$ can be constructed, then, for $t$ large enough, the distribution of $X_t$ is close to $\pi$. The focus of this book is to determine how large $t$ must be to obtain a sufficiently close approximation. In this chapter we will focus on the task of finding chains with a given stationary distribution.

**3.2. Metropolis Chains**

Given *some* chain with state space $\mathcal{X}$ and an arbitrary stationary distribution, can the chain be modified so that the new chain has the stationary distribution $\pi$? The Metropolis algorithm accomplishes this.

**3.2.1. Symmetric base chain.** Suppose that $\Psi$ is a symmetric transition matrix. In this case, $\Psi$ is reversible with respect to the uniform distribution on $\mathcal{X}$.

### PDF page 55 (book page 39)

We now show how to modify transitions made according to $\Psi$ to obtain a chain with stationary distribution $\pi$, given an arbitrary probability distribution $\pi$ on $\mathcal{X}$.

The new chain evolves as follows: when at state $x$, a candidate move is generated from the distribution $\Psi(x, \cdot)$. If the proposed new state is $y$, then the move is censored with probability $1 - a(x, y)$. That is, with probability $a(x, y)$, the state $y$ is "accepted" so that the next state of the chain is $y$, and with the remaining probability $1 - a(x, y)$, the chain remains at $x$. Rejecting moves slows the chain and can reduce its computational efficiency but may be necessary to achieve a specific stationary distribution. We will discuss how to choose the acceptance probability $a(x, y)$ below, but for now observe that the transition matrix $P$ of the new chain is

$$ P(x,y) = \begin{cases} \Psi(x,y)a(x,y) & \text{if } y \neq x, \\ 1 - \sum_{z\,:\,z \neq x} \Psi(x,z)a(x,z) & \text{if } y = x. \end{cases} $$

By Proposition 1.20, the transition matrix $P$ has stationary distribution $\pi$ if

$$ \pi(x)\Psi(x,y)a(x,y) = \pi(y)\Psi(y,x)a(y,x) \tag{3.1} $$

for all $x \neq y$. Since we have assumed $\Psi$ is symmetric, equation (3.1) holds if and only if

$$ b(x,y) = b(y,x), \tag{3.2} $$

where $b(x,y) = \pi(x)a(x,y)$. Because $a(x,y)$ is a probability and must satisfy $a(x,y) \leq 1$, the function $b$ must obey the constraints

$$ \begin{aligned} b(x,y) &\leq \pi(x), \\ b(x,y) = b(y,x) &\leq \pi(y). \end{aligned} \tag{3.3} $$

Since rejecting the moves of the original chain $\Psi$ is wasteful, a solution $b$ to (3.2) and (3.3) should be chosen which is as large as possible. Clearly, all solutions are bounded above by $b^*(x,y) := \pi(x) \wedge \pi(y) := \min\{\pi(x), \pi(y)\}$. For this choice, the acceptance probability $a(x,y)$ is equal to $(\pi(y)/\pi(x)) \wedge 1$.

The ***Metropolis chain*** for a probability $\pi$ and a symmetric transition matrix $\Psi$ is defined as

$$ P(x,y) = \begin{cases} \Psi(x,y)\left[1 \wedge \frac{\pi(y)}{\pi(x)}\right] & \text{if } y \neq x, \\ 1 - \sum_{z\,:\,z \neq x} \Psi(x,z)\left[1 \wedge \frac{\pi(z)}{\pi(x)}\right] & \text{if } y = x. \end{cases} $$

Our discussion above shows that $\pi$ is indeed a stationary distribution for the Metropolis chain.

REMARK 3.1. A very important feature of the Metropolis chain is that it only depends on the ratios $\pi(x)/\pi(y)$. In many cases of interest, $\pi(x)$ has the form $h(x)/Z$, where the function $h : \mathcal{X} \to [0, \infty)$ is known and $Z = \sum_{x \in \mathcal{X}} h(x)$ is a normalizing constant. It may be difficult to explicitly compute $Z$, especially if $\mathcal{X}$ is large. Because the Metropolis chain only depends on $h(x)/h(y)$, it is not necessary to compute the constant $Z$ in order to simulate the chain. The optimization chains described below (Example 3.2) are examples of this type.

EXAMPLE 3.2 (Optimization). Let $f$ be a real-valued function defined on the vertex set $\mathcal{X}$ of a graph. In many applications it is desirable to find a vertex $x$ where $f(x)$ is maximal. If the domain $\mathcal{X}$ is very large, then an exhaustive search may be too expensive.

### PDF page 56 (book page 40)

**FIGURE 3.1.** A hill climb algorithm may become trapped at a local maximum. *[Figure: a jagged curve representing $f(x)$ over a horizontal axis, with a tall global peak on the left and a shorter secondary peak on the right; three stick-figure climbers ascend the right (lower) peak toward its local summit, with arrows indicating upward movement, above a marked point $x_0$ on the axis.]*

A ***hill climb*** is an algorithm which attempts to locate the maximum values of $f$ as follows: when at $x$, if there is at least one neighbor $y$ of $x$ satisfying $f(y) > f(x)$, move to a neighbor with the largest value of $f$. The climber may become stranded at local maxima — see Figure 3.1.

One solution is to randomize moves so that instead of always remaining at a local maximum, with some probability the climber moves to lower states.

Suppose for simplicity that $\mathcal{X}$ is a regular graph, so that simple random walk on $\mathcal{X}$ has a symmetric transition matrix. Fix $\lambda \geq 1$ and define

$$ \pi_\lambda(x) = \frac{\lambda^{f(x)}}{Z(\lambda)}, $$

where $Z(\lambda) := \sum_{x \in \mathcal{X}} \lambda^{f(x)}$ is the normalizing constant that makes $\pi_\lambda$ a probability measure (as mentioned in Remark 3.1, running the Metropolis chain does not require computation of $Z(\lambda)$, which may be prohibitively expensive to compute). Since $\pi_\lambda(x)$ is increasing in $f(x)$, the measure $\pi_\lambda$ favors vertices $x$ for which $f(x)$ is large.

If $f(y) < f(x)$, the Metropolis chain accepts a transition $x \to y$ with probability $\lambda^{-[f(x)-f(y)]}$. As $\lambda \to \infty$, the chain more closely resembles the deterministic hill climb.

Define

$$ \mathcal{X}^\star := \left\{ x \in \mathcal{X} \;:\; f(x) = f^\star := \max_{y \in \mathcal{X}} f(y) \right\}. $$

Then

$$ \lim_{\lambda \to \infty} \pi_\lambda(x) = \lim_{\lambda \to \infty} \frac{\lambda^{f(x)}/\lambda^{f^\star}}{|\mathcal{X}^\star| + \sum_{x \in \mathcal{X} \setminus \mathcal{X}^\star} \lambda^{f(x)}/\lambda^{f^\star}} = \frac{\mathbf{1}_{\{x \in \mathcal{X}^\star\}}}{|\mathcal{X}^\star|}. $$

That is, as $\lambda \to \infty$, the stationary distribution $\pi_\lambda$ of this Metropolis chain converges to the uniform distribution over the global maxima of $f$.

**3.2.2. General base chain.** The Metropolis chain can also be defined when the initial transition matrix is not symmetric. For a general (irreducible) transition matrix $\Psi$ and an arbitrary probability distribution $\pi$ on $\mathcal{X}$, the Metropolized chain is executed as follows. When at state $x$, generate a state $y$ from $\Psi(x, \cdot)$. Move to

### PDF page 57 (book page 41)

$y$ with probability

$$ \frac{\pi(y)\Psi(y,x)}{\pi(x)\Psi(x,y)} \wedge 1, \tag{3.4} $$

and remain at $x$ with the complementary probability. The transition matrix $P$ for this chain is

$$ P(x,y) = \begin{cases} \Psi(x,y)\left[\frac{\pi(y)\Psi(y,x)}{\pi(x)\Psi(x,y)} \wedge 1\right] & \text{if } y \neq x, \\ 1 - \sum_{z\,:\,z \neq x} \Psi(x,z)\left[\frac{\pi(z)\Psi(z,x)}{\pi(x)\Psi(x,z)} \wedge 1\right] & \text{if } y = x. \end{cases} \tag{3.5} $$

The reader should check that the transition matrix (3.5) defines a reversible Markov chain with stationary distribution $\pi$ (see Exercise 3.1).

EXAMPLE 3.3. Suppose you know neither the vertex set $V$ nor the edge set $E$ of a graph $G$. However, you are able to perform a simple random walk on $G$. (Many computer and social networks have this form; each vertex knows who its neighbors are, but not the global structure of the graph.) If the graph is not regular, then the stationary distribution is not uniform, so the distribution of the walk will not converge to uniform. You desire a uniform sample from $V$. We can use the Metropolis algorithm to modify the simple random walk and ensure a uniform stationary distribution. The acceptance probability in (3.4) reduces in this case to

$$ \frac{\deg(x)}{\deg(y)} \wedge 1. $$

This biases the walk against moving to higher degree vertices, giving a uniform stationary distribution. Note that it is not necessary to know the size of the vertex set to perform this modification, which can be an important consideration in applications.

**3.3. Glauber Dynamics**

We will study many chains whose state spaces are contained in a set of the form $S^V$, where $V$ is the vertex set of a graph and $S$ is a finite set. The elements of $S^V$, called ***configurations***, are the functions from $V$ to $S$. We visualize a configuration as a labeling of vertices with elements of $S$.

Given a probability distribution $\pi$ on a space of configurations, the Glauber dynamics for $\pi$, to be defined below, is a Markov chain which has stationary distribution $\pi$. This chain is often called the *Gibbs sampler*, especially in statistical contexts.

**3.3.1. Two examples.** As we defined in Section 3.1, a proper $q$-coloring of a graph $G = (V, E)$ is an element $x$ of $\{1, 2, \ldots, q\}^V$, the set of functions from $V$ to $\{1, 2, \ldots, q\}$, such that $x(v) \neq x(w)$ for all edges $\{v, w\}$. We construct here a Markov chain on the set of proper $q$-colorings of $G$.

For a given configuration $x$ and a vertex $v$, call a color $j$ ***allowable*** at $v$ if $j$ is different from all colors assigned to neighbors of $v$. That is, a color is allowable at $v$ if it does *not* belong to the set $\{x(w) : w \sim v\}$. Given a proper $q$-coloring $x$, we can generate a new coloring by

- selecting a vertex $v \in V$ at random,
- selecting a color $j$ uniformly at random from the allowable colors at $v$, and

### PDF page 58 (book page 42)

- re-coloring vertex $v$ with color $j$.

We claim that the resulting chain has uniform stationary distribution: why? Note that transitions are permitted only between colorings differing at a single vertex. If $x$ and $y$ agree everywhere except vertex $v$, then the chance of moving from $x$ to $y$ equals $|V|^{-1}|A_v(x)|^{-1}$, where $A_v(x)$ is the set of allowable colors at $v$ in $x$. Since $A_v(x) = A_v(y)$, this probability equals the probability of moving from $y$ to $x$. Since $P(x, y) = P(y, x)$, the detailed balance equations are satisfied by the uniform distribution.

This chain is called the **Glauber dynamics for proper $q$-colorings**. Note that when a vertex $v$ is updated in coloring $x$, a coloring is chosen from $\pi$ conditioned on the set of colorings agreeing with $x$ at all vertices different from $v$. This is the general rule for defining Glauber dynamics for any set of configurations. Before spelling out the details in the general case, we consider one other specific example.

A **hardcore configuration** is a placement of particles on the vertices $V$ of a graph so that each vertex is occupied by at most one particle and no two particles are adjacent. Formally, a hardcore configuration $x$ is an element of $\{0, 1\}^V$, the set of functions from $V$ to $\{0, 1\}$, satisfying $x(v)x(w) = 0$ whenever $v$ and $w$ are neighbors. The vertices $v$ with $x(v) = 1$ are called **occupied**, and the vertices $v$ with $x(v) = 0$ are called **vacant**.

Consider the following transition rule:

- a vertex $v$ is chosen uniformly at random, and, regardless of the current status of $v$,
- if any neighbor of $v$ is occupied, $v$ is left unoccupied, while if no adjacent vertex is occupied, $v$ is occupied with probability $1/2$ and is vacant with probability $1/2$.

REMARK 3.4. Note that the rule above has the same effect as the following apparently simpler rule: if no neighbor of $v$ is occupied, then, with probability $1/2$, flip the status of $v$. Our original description will be much more convenient when, in the future, we attempt to couple multiple copies of this chain, since it provides a way to ensure that the status at the chosen vertex $v$ is the same in all copies after an update. See Section 5.4.2.

The verification that this chain is reversible with respect to the uniform distribution is similar to the coloring chain just considered and is left to the reader.

**3.3.2. General definition.** In general, let $V$ and $S$ be finite sets, and suppose that $\mathcal{X}$ is a subset of $S^V$ (both the set of proper $q$-colorings and the set of hardcore configurations are of this form). Let $\pi$ be a probability distribution whose support is $\mathcal{X}$. The (single-site) **Glauber dynamics for $\pi$** is a reversible Markov chain with state space $\mathcal{X}$, stationary distribution $\pi$, and the transition probabilities we describe below.

In words, the Glauber chain moves from state $x$ as follows: a vertex $v$ is chosen uniformly at random from $V$, and a new state is chosen according to the measure $\pi$ conditioned on the set of states equal to $x$ at all vertices different from $v$. We give the details now. For $x \in \mathcal{X}$ and $v \in V$, let

$$ \mathcal{X}(x, v) = \{y \in \mathcal{X} \,:\, y(w) = x(w) \text{ for all } w \neq v\} \tag{3.6} $$

### PDF page 59 (book page 43)

be the set of states agreeing with $x$ everywhere except possibly at $v$, and define

$$ \pi^{x,v}(y) = \pi(y \mid \mathcal{X}(x, v)) = \begin{cases} \frac{\pi(y)}{\pi(\mathcal{X}(x,v))} & \text{if } y \in \mathcal{X}(x, v), \\ 0 & \text{if } y \notin \mathcal{X}(x, v) \end{cases} \tag{3.7} $$

to be the distribution $\pi$ conditioned on the set $\mathcal{X}(x, v)$. The rule for updating a configuration $x$ is: pick a vertex $v$ uniformly at random, and choose a new configuration according to $\pi^{x,v}$.

The distribution $\pi$ is always stationary and reversible for the Glauber dynamics (see Exercise 3.2).

**3.3.3. Comparing Glauber dynamics and Metropolis chains.** Suppose now that $\pi$ is a probability distribution on the state space $S^V$, where $S$ is a finite set and $V$ is the vertex set of a graph. We can always define the Glauber chain as just described. Suppose on the other hand that we have a chain which picks a vertex $v$ at random and has *some* mechanism for updating the configuration at $v$. (For example, the chain may pick an element of $S$ at random to update at $v$.) This chain may not have stationary distribution $\pi$, but it can be modified by the Metropolis rule to obtain a chain with stationary distribution $\pi$. This chain can be very similar to the Glauber chain, but may not coincide exactly. We consider our examples.

EXAMPLE 3.5 (Chains on $q$-colorings). Consider the following chain on (not necessarily proper) $q$-colorings: a vertex $v$ is chosen uniformly at random, a color is selected uniformly at random among *all* $q$ colors, and the vertex $v$ is recolored with the chosen color. We apply the Metropolis rule to this chain, where $\pi$ is the probability measure which is uniform over the space of *proper $q$-colorings*. When at a proper coloring, if the color $k$ is proposed to update a vertex, then the Metropolis rule accepts the proposed re-coloring with probability 1 if it yields a proper coloring and rejects otherwise.

The Glauber chain described in Section 3.3.1 is slightly different. Note in particular that the chance of remaining at the same coloring differs for the two chains. If there are $a$ allowable colors at vertex $v$ and this vertex $v$ is selected for updating in the Glauber dynamics, the chance that the coloring remains the same is $1/a$. For the Metropolis chain, if vertex $v$ is selected, the chance of remaining in the current coloring is $(1 + q - a)/q$.

EXAMPLE 3.6 (Hardcore chains). Again identify elements of $\{0, 1\}^V$ with a placement of particles onto the vertex set $V$, and consider the following chain on $\{0, 1\}^V$: a vertex is chosen at random, and a particle is placed at the selected vertex with probability $1/2$. This chain does not live on the space of hardcore configurations, as there is no constraint against placing a particle on a vertex with an occupied neighbor.

We can modify this chain with the Metropolis rule to obtain a chain with stationary distribution $\pi$, where $\pi$ is uniform over hardcore configurations. If $x$ is a hardcore configuration, the move $x \to y$ is rejected if and only if $y$ is not a hardcore configuration. The Metropolis chain and the Glauber dynamics agree in this example.

**3.3.4. Hardcore model with fugacity.** Let $G = (V, E)$ be a graph and let $\mathcal{X}$ be the set of hardcore configurations on $G$. The **hardcore model** with **fugacity**

### PDF page 60 (book page 44)

$\lambda$ is the probability distribution $\pi$ on hardcore configurations $x \in \{0, 1\}^V$ defined by

$$ \pi(x) = \begin{cases} \frac{\lambda^{\sum_{v \in V} x(v)}}{Z(\lambda)} & \text{if } x(v)x(w) = 0 \text{ for all } \{v, w\} \in E, \\ 0 & \text{otherwise.} \end{cases} $$

The factor $Z(\lambda) = \sum_{x \in \mathcal{X}} \lambda^{\sum_{v \in V} x(v)}$ normalizes $\pi$ to have unit total mass.

The Glauber dynamics for the hardcore model updates a configuration $X_t$ to a new configuration $X_{t+1}$ as follows: First, a vertex $w$ is chosen uniformly at random. If there exists a neighbor $w'$ of $w$ such that $X_t(w') = 1$, then set $X_{t+1}(w) := 0$; otherwise, let

$$ X_{t+1}(w) := \begin{cases} 1 & \text{with probability } \lambda/(1 + \lambda), \\ 0 & \text{with probability } 1/(1 + \lambda). \end{cases} $$

Furthermore, set $X_{t+1}(v) = X_t(v)$ for all $v \neq w$.

**3.3.5. The Ising model.** A **spin system** is a probability distribution on $\mathcal{X} = \{-1, 1\}^V$, where $V$ is the vertex set of a graph $G = (V, E)$. The value $\sigma(v)$ is called the **spin** at $v$. The physical interpretation is that magnets, each having one of the two possible orientations represented by $+1$ and $-1$, are placed on the vertices of the graph; a configuration specifies the orientations of these magnets.

The nearest-neighbor **Ising model** is the most widely studied spin system. In this system, the **energy** of a configuration $\sigma$ is defined to be

$$ H(\sigma) = - \sum_{\substack{v, w \in V \\ v \sim w}} \sigma(v)\sigma(w). \tag{3.8} $$

Clearly, the energy increases with the number of pairs of neighbors whose spins disagree.

The **Gibbs distribution** corresponding to the energy $H$ is the probability distribution $\mu$ on $\mathcal{X}$ defined by

$$ \mu(\sigma) = \frac{1}{Z(\beta)} e^{-\beta H(\sigma)}. \tag{3.9} $$

Here the **partition function** $Z(\beta)$ is the normalizing constant required to make $\mu$ a probability distribution:

$$ Z(\beta) := \sum_{\sigma \in \mathcal{X}} e^{-\beta H(\sigma)}. \tag{3.10} $$

The parameter $\beta \geq 0$ determines the influence of the energy function. In the physical interpretation, $\beta$ is the reciprocal of temperature. At infinite temperature ($\beta = 0$), the energy function $H$ plays no role and $\mu$ is the uniform distribution on $\mathcal{X}$. In this case, there is no interaction between the spins at differing vertices and the random variables $\{\sigma(v)\}_{v \in V}$ are independent. As $\beta > 0$ increases, the bias of $\mu$ towards low-energy configurations also increases. See Figure 3.2 for an illustration of the effect of $\beta$ on configurations.

The Glauber dynamics for the Gibbs distribution $\mu$ move from a starting configuration $\sigma$ by picking a vertex $w$ uniformly at random from $V$ and then generating a new configuration according to $\mu$ conditioned on the set of configurations agreeing with $\sigma$ on vertices different from $w$.

### PDF page 61 (book page 45)

**FIGURE 3.2.** The Ising model on the $250 \times 250$ torus at low, critical, and high temperature, respectively. Simulations and graphics courtesy of Raissa D'Souza.

*[Figure: three side-by-side square panels showing black-and-white spin configurations of the Ising model on a $250 \times 250$ torus. Left (low temperature): mostly white with sparse black speckles, nearly all spins aligned. Middle (critical temperature): large connected black and white clusters at many scales. Right (high temperature): fine random salt-and-pepper mixture of black and white, spins essentially uncorrelated.]*

The reader can check that the conditional $\mu$-probability of spin $+1$ at $w$ is

$$ p(\sigma, w) := \frac{e^{\beta S(\sigma,w)}}{e^{\beta S(\sigma,w)} + e^{-\beta S(\sigma,w)}} = \frac{1 + \tanh(\beta S(\sigma,w))}{2}, \tag{3.11} $$

where $S(\sigma, w) := \sum_{u \,:\, u \sim w} \sigma(u)$. Note that $p(\sigma, w)$ depends only on the spins at vertices adjacent to $w$. Therefore, the transition matrix on $\mathcal{X}$ is given by

$$ P(\sigma, \sigma') = \frac{1}{|V|} \sum_{w \in V} \frac{e^{\beta \, \sigma'(w) \, S(\sigma,w)}}{e^{\beta \, \sigma'(w) \, S(\sigma,w)} + e^{-\beta \, \sigma'(w) \, S(\sigma,w)}} \cdot \mathbf{1}_{\{\sigma(v) = \sigma'(v) \text{ for } v \neq w\}}. \tag{3.12} $$

This chain has stationary distribution given by the Gibbs distribution $\mu$.

**Exercises**

EXERCISE 3.1. Let $\Psi$ be an irreducible transition matrix on $\mathcal{X}$, and let $\pi$ be a probability distribution on $\mathcal{X}$. Show that the transition matrix

$$ P(x,y) = \begin{cases} \Psi(x,y) \left[ \frac{\pi(y)\Psi(y,x)}{\pi(x)\Psi(x,y)} \wedge 1 \right] & \text{if } y \neq x, \\ 1 - \displaystyle\sum_{z \,:\, z \neq x} \Psi(x,z) \left[ \frac{\pi(z)\Psi(z,x)}{\pi(x)\Psi(x,z)} \wedge 1 \right] & \text{if } y = x \end{cases} $$

defines a reversible Markov chain with stationary distribution $\pi$.

EXERCISE 3.2. Verify that the Glauber dynamics for $\pi$ is a reversible Markov chain with stationary distribution $\pi$.

**Notes**

The Metropolis chain was introduced in Metropolis, Rosenbluth, Teller, and Teller (**1953**) for a specific stationary distribution. **Hastings (1970)** extended the method to general chains and distributions. The survey by **Diaconis and Saloff-Coste (1998)** contains more on the Metropolis algorithm. The textbook by **Brémaud (1999)** also discusses the use of the Metropolis algorithm for Monte Carlo sampling.

### PDF page 62 (book page 46)

Variations on the randomized hill climb in Example 3.2 used to locate extrema, especially when the parameter $\lambda$ is tuned as the walk progresses, are called *simulated annealing* algorithms. Significant references are **Holley and Stroock (1988)** and **Hajek (1988)**.

We will have much more to say about Glauber dynamics for colorings in Section 14.3 and about Glauber dynamics for the Ising model in Chapter 15.

**Häggström (2007)** proves interesting inequalities using the Markov chains of this chapter.

# Chapter 1 — Introduction to Finite Markov Chains
*(PDF pages 18–36; book pages 2–20)*

### PDF page 18 (book page 2)

CHAPTER 1

# Introduction to Finite Markov Chains

**1.1. Markov Chains**

A Markov chain is a process which moves among the elements of a set $\mathcal{X}$ in the following manner: when at $x \in \mathcal{X}$, the next position is chosen according to a fixed probability distribution $P(x, \cdot)$ depending only on $x$. More precisely, a sequence of random variables $(X_0, X_1, \ldots)$ is a ***Markov chain with state space*** $\mathcal{X}$ ***and transition matrix*** $P$ if for all $x, y \in \mathcal{X}$, all $t \geq 1$, and all events $H_{t-1} = \bigcap_{s=0}^{t-1}\{X_s = x_s\}$ satisfying $\mathbf{P}(H_{t-1} \cap \{X_t = x\}) > 0$, we have

$$ \mathbf{P}\left\{X_{t+1} = y \mid H_{t-1} \cap \{X_t = x\}\right\} = \mathbf{P}\left\{X_{t+1} = y \mid X_t = x\right\} = P(x, y). \tag{1.1} $$

Equation (1.1), often called the ***Markov property***, means that the conditional probability of proceeding from state $x$ to state $y$ is the same, no matter what sequence $x_0, x_1, \ldots, x_{t-1}$ of states precedes the current state $x$. This is exactly why the $|\mathcal{X}| \times |\mathcal{X}|$ matrix $P$ suffices to describe the transitions.

The $x$-th row of $P$ is the distribution $P(x, \cdot)$. Thus $P$ is ***stochastic***, that is, its entries are all non-negative and

$$ \sum_{y \in \mathcal{X}} P(x, y) = 1 \qquad \text{for all } x \in \mathcal{X}. $$

*[Figure: line drawing of a frog sitting on one lily pad, with a fly on that pad and another fly on a second lily pad nearby.]*

FIGURE 1.1. A randomly jumping frog. Whenever he tosses heads, he jumps to the other lily pad.

### PDF page 19 (book page 3)

EXAMPLE 1.1. A certain frog lives in a pond with two lily pads, *east* and *west*. A long time ago, he found two coins at the bottom of the pond and brought one up to each lily pad. Every morning, the frog decides whether to jump by tossing the current lily pad's coin. If the coin lands heads up, the frog jumps to the other lily pad. If the coin lands tails up, he remains where he is.

Let $\mathcal{X} = \{e, w\}$, and let $(X_0, X_1, \dots)$ be the sequence of lily pads occupied by the frog on Sunday, Monday, .... Given the source of the coins, we should not assume that they are fair! Say the coin on the east pad has probability $p$ of landing heads up, while the coin on the west pad has probability $q$ of landing heads up. The frog's rules for jumping imply that if we set

$$ P = \left( \begin{array}{cc} P(e,e) & P(e,w) \\ P(w,e) & P(w,w) \end{array} \right) = \left( \begin{array}{cc} 1-p & p \\ q & 1-q \end{array} \right), \tag{1.2} $$

then $(X_0, X_1, \dots)$ is a Markov chain with transition matrix $P$. Note that the first row of $P$ is the conditional distribution of $X_{t+1}$ given that $X_t = e$, while the second row is the conditional distribution of $X_{t+1}$ given that $X_t = w$.

Assume that the frog spends Sunday on the east pad. When he awakens Monday, he has probability $p$ of moving to the west pad and probability $1-p$ of staying on the east pad. That is,

$$ \mathbf{P}\{X_1 = e \mid X_0 = e\} = 1 - p, \qquad \mathbf{P}\{X_1 = w \mid X_0 = e\} = p. \tag{1.3} $$

What happens Tuesday? By considering the two possibilities for $X_1$, we see that

$$ \mathbf{P}\{X_2 = e \mid X_0 = e\} = (1-p)(1-p) + pq \tag{1.4} $$

and

$$ \mathbf{P}\{X_2 = w \mid X_0 = e\} = (1-p)p + p(1-q). \tag{1.5} $$

While we could keep writing out formulas like (1.4) and (1.5), there is a more systematic approach. We can store our distribution information in a row vector

$$ \mu_t := (\mathbf{P}\{X_t = e \mid X_0 = e\}, \mathbf{P}\{X_t = w \mid X_0 = e\}) . $$

Our assumption that the frog starts on the east pad can now be written as $\mu_0 = (1, 0)$, while (1.3) becomes $\mu_1 = \mu_0 P$.

Multiplying by $P$ on the right updates the distribution by another step:

$$ \mu_t = \mu_{t-1} P \quad \text{for all } t \geq 1. \tag{1.6} $$

Indeed, for any initial distribution $\mu_0$,

$$ \mu_t = \mu_0 P^t \quad \text{for all } t \geq 0. \tag{1.7} $$

How does the distribution $\mu_t$ behave in the long term? Figure 1.2 suggests that $\mu_t$ has a limit $\pi$ (whose value depends on $p$ and $q$) as $t \to \infty$. Any such limit distribution $\pi$ must satisfy

$$ \pi = \pi P, $$

which implies (after a little algebra) that

$$ \pi(e) = \frac{q}{p+q}, \qquad \pi(w) = \frac{p}{p+q}. $$

If we define

$$ \Delta_t = \mu_t(e) - \frac{q}{p+q} \quad \text{for all } t \geq 0, $$

### PDF page 20 (book page 4)

**FIGURE 1.2.** The probability of being on the east pad (started from the east pad) plotted versus time for (a) $p = q = 1/2$, (b) $p = 0.2$ and $q = 0.1$, (c) $p = 0.95$ and $q = 0.7$. The long-term limiting probabilities are $1/2$, $1/3$, and $14/33 \approx 0.42$, respectively. *[Figure: three small line plots labeled (a), (b), (c), each with vertical axis marked at 0.25, 0.5, 0.75, 1 and horizontal axis (time) marked at 0, 10, 20. (a) drops immediately from 1 to a flat line at 0.5; (b) decays smoothly from 1 to a plateau near 1/3; (c) oscillates with decaying amplitude, damping toward about 0.42.]*

then by the definition of $\mu_{t+1}$ the sequence $(\Delta_t)$ satisfies

$$ \Delta_{t+1} = \mu_t(e)(1-p) + (1-\mu_t(e))(q) - \frac{q}{p+q} = (1-p-q)\Delta_t. \tag{1.8} $$

We conclude that when $0 < p < 1$ and $0 < q < 1$,

$$ \lim_{t \to \infty} \mu_t(e) = \frac{q}{p+q} \quad \text{and} \quad \lim_{t \to \infty} \mu_t(w) = \frac{p}{p+q} \tag{1.9} $$

for any initial distribution $\mu_0$. As we suspected, $\mu_t$ approaches $\pi$ as $t \to \infty$.

REMARK 1.2. The traditional theory of finite Markov chains is concerned with convergence statements of the type seen in (1.9), that is, with the rate of convergence as $t \to \infty$ for a *fixed chain*. Note that $1 - p - q$ is an eigenvalue of the frog's transition matrix $P$. Note also that this eigenvalue determines the rate of convergence in (1.9), since by (1.8) we have

$$ \Delta_t = (1-p-q)^t \Delta_0. $$

The computations we just did for a two-state chain generalize to any finite Markov chain. In particular, the distribution at time $t$ can be found by matrix multiplication. Let $(X_0, X_1, \dots)$ be a finite Markov chain with state space $\mathcal{X}$ and transition matrix $P$, and let the row vector $\mu_t$ be the distribution of $X_t$:

$$ \mu_t(x) = \mathbf{P}\{X_t = x\} \quad \text{for all } x \in \mathcal{X}. $$

By conditioning on the possible predecessors of the $(t + 1)$-st state, we see that

$$ \mu_{t+1}(y) = \sum_{x \in \mathcal{X}} \mathbf{P}\{X_t = x\}P(x,y) = \sum_{x \in \mathcal{X}} \mu_t(x)P(x,y) \quad \text{for all } y \in \mathcal{X}. $$

Rewriting this in vector form gives

$$ \mu_{t+1} = \mu_t P \quad \text{for } t \geq 0 $$

and hence

$$ \mu_t = \mu_0 P^t \quad \text{for } t \geq 0. \tag{1.10} $$

Since we will often consider Markov chains with the same transition matrix but different starting distributions, we introduce the notation $\mathbf{P}_\mu$ and $\mathbf{E}_\mu$ for probabilities and expectations given that $\mu_0 = \mu$. Most often, the initial distribution will

### PDF page 21 (book page 5)

be concentrated at a single definite starting state $x$. We denote this distribution by $\delta_x$:

$$ \delta_x(y) = \begin{cases} 1 & \text{if } y = x, \\ 0 & \text{if } y \neq x. \end{cases} $$

We write simply $\mathbf{P}_x$ and $\mathbf{E}_x$ for $\mathbf{P}_{\delta_x}$ and $\mathbf{E}_{\delta_x}$, respectively.

These definitions and (1.10) together imply that

$$ \mathbf{P}_x\{X_t = y\} = (\delta_x P^t)(y) = P^t(x,y). $$

That is, the probability of moving in $t$ steps from $x$ to $y$ is given by the $(x, y)$-th entry of $P^t$. We call these entries the ***t-step transition probabilities***.

NOTATION. A probability distribution $\mu$ on $\mathcal{X}$ will be identified with a row vector. For any event $A \subset \mathcal{X}$, we write

$$ \mu(A) = \sum_{x \in A} \mu(x). $$

For $x \in \mathcal{X}$, the row of $P$ indexed by $x$ will be denoted by $P(x, \cdot)$.

REMARK 1.3. The way we constructed the matrix $P$ has forced us to treat distributions as row vectors. In general, if the chain has distribution $\mu$ at time $t$, then it has distribution $\mu P$ at time $t + 1$. *Multiplying a row vector by $P$ on the right takes you from today's distribution to tomorrow's distribution.*

What if we multiply a column vector $f$ by $P$ on the left? Think of $f$ as a function on the state space $\mathcal{X}$. (For the frog of Example 1.1, we might take $f(x)$ to be the area of the lily pad $x$.) Consider the $x$-th entry of the resulting vector:

$$ Pf(x) = \sum_{y} P(x,y)f(y) = \sum_{y} f(y)\mathbf{P}_x\{X_1 = y\} = \mathbf{E}_x(f(X_1)). $$

That is, the $x$-th entry of $Pf$ tells us the expected value of the function $f$ at tomorrow's state, given that we are at state $x$ today.

**1.2. Random Mapping Representation**

We begin this section with an example.

EXAMPLE 1.4 (Random walk on the $n$-cycle). Let $\mathcal{X} = \mathbb{Z}_n = \{0, 1, \dots, n - 1\}$, the set of remainders modulo $n$. Consider the transition matrix

$$ P(j,k) = \begin{cases} 1/2 & \text{if } k \equiv j + 1 \pmod{n}, \\ 1/2 & \text{if } k \equiv j - 1 \pmod{n}, \\ 0 & \text{otherwise.} \end{cases} \tag{1.11} $$

The associated Markov chain $(X_t)$ is called ***random walk on the $n$-cycle***. The states can be envisioned as equally spaced dots arranged in a circle (see Figure 1.3).

Rather than writing down the transition matrix in (1.11), this chain can be specified simply in words: at each step, a coin is tossed. If the coin lands heads up, the walk moves one step clockwise. If the coin lands tails up, the walk moves one step counterclockwise.

### PDF page 22 (book page 6)

*[Figure: two ring graphs side by side. Left — a 10-vertex cycle ($\mathbb{Z}_{10}$) with vertices alternately filled (black) and open (white), illustrating the two-class (even/odd) structure. Right — a 9-vertex cycle ($\mathbb{Z}_9$) with all vertices filled (black).]*

FIGURE 1.3. Random walk on $\mathbb{Z}_{10}$ is periodic, since every step goes from an even state to an odd state, or vice-versa. Random walk on $\mathbb{Z}_9$ is aperiodic.

More precisely, suppose that $Z$ is a random variable which is equally likely to take on the values $-1$ and $+1$. If the current state of the chain is $j \in \mathbb{Z}_n$, then the next state is $j + Z \bmod n$. For any $k \in \mathbb{Z}_n$,
$$ \mathbf{P}\{(j + Z) \bmod n = k\} = P(j,k). $$
In other words, the distribution of $(j + Z) \bmod n$ equals $P(j,\cdot)$.

A ***random mapping representation*** of a transition matrix $P$ on state space $\mathcal{X}$ is a function $f : \mathcal{X} \times \Lambda \to \mathcal{X}$, along with a $\Lambda$-valued random variable $Z$, satisfying
$$ \mathbf{P}\{f(x,Z) = y\} = P(x,y). $$
The reader should check that if $Z_1, Z_2, \ldots$ is a sequence of independent random variables, each having the same distribution as $Z$, the random variable $X_0$ has distribution $\mu$ and is independent of $(Z_t)_{t \geq 1}$, then the sequence $(X_0, X_1, \ldots)$ defined by
$$ X_n = f(X_{n-1}, Z_n) \quad \text{for } n \geq 1 $$
is a Markov chain with transition matrix $P$ and initial distribution $\mu$.

For the example of the simple random walk on the cycle, setting $\Lambda = \{1, -1\}$, each $Z_i$ uniform on $\Lambda$, and $f(x,z) = x + z \bmod n$ yields a random mapping representation.

PROPOSITION 1.5. *Every transition matrix on a finite state space has a random mapping representation.*

PROOF. Let $P$ be the transition matrix of a Markov chain with state space $\mathcal{X} = \{x_1, \ldots, x_n\}$. Take $\Lambda = [0,1]$; our auxiliary random variables $Z, Z_1, Z_2, \ldots$ will be uniformly chosen in this interval. Set $F_{j,k} = \sum_{i=1}^k P(x_j, x_i)$ and define
$$ f(x_j, z) := x_k \text{ when } F_{j,k-1} < z \leq F_{j,k}. $$
We have
$$ \mathbf{P}\{f(x_j, Z) = x_k\} = \mathbf{P}\{F_{j,k-1} < Z \leq F_{j,k}\} = P(x_j, x_k). $$
$\blacksquare$

Note that, unlike transition matrices, random mapping representations are far from unique. For instance, replacing the function $f(x,z)$ in the proof of Proposition 1.5 with $f(x, 1-z)$ yields a different representation of the same transition matrix.

Random mapping representations are crucial for simulating large chains. They can also be the most convenient way to describe a chain. We will often give rules for how a chain proceeds from state to state, using some extra randomness to determine

### PDF page 23 (book page 7)

where to go next; such discussions are implicit random mapping representations. Finally, random mapping representations provide a way to coordinate two (or more) chain trajectories, as we can simply use the same sequence of auxiliary random variables to determine updates. This technique will be exploited in Chapter 5, on coupling Markov chain trajectories, and elsewhere.

**1.3. Irreducibility and Aperiodicity**

We now make note of two simple properties possessed by most interesting chains. Both will turn out to be necessary for the Convergence Theorem (Theorem 4.9) to be true.

A chain $P$ is called ***irreducible*** if for any two states $x, y \in \mathcal{X}$ there exists an integer $t$ (possibly depending on $x$ and $y$) such that $P^t(x,y) > 0$. This means that it is possible to get from any state to any other state using only transitions of positive probability. We will generally assume that the chains under discussion are irreducible. (Checking that specific chains are irreducible can be quite interesting; see, for instance, Section 2.6 and Example B.5. See Section 1.7 for a discussion of all the ways in which a Markov chain can fail to be irreducible.)

Let $\mathcal{T}(x) := \{t \geq 1 : P^t(x,x) > 0\}$ be the set of times when it is possible for the chain to return to starting position $x$. The ***period*** of state $x$ is defined to be the greatest common divisor of $\mathcal{T}(x)$.

LEMMA 1.6. *If $P$ is irreducible, then $\gcd \mathcal{T}(x) = \gcd \mathcal{T}(y)$ for all $x, y \in \mathcal{X}$.*

PROOF. Fix two states $x$ and $y$. There exist non-negative integers $r$ and $\ell$ such that $P^r(x,y) > 0$ and $P^\ell(y,x) > 0$. Letting $m = r+\ell$, we have $m \in \mathcal{T}(x) \cap \mathcal{T}(y)$ and $\mathcal{T}(x) \subset \mathcal{T}(y) - m$, whence $\gcd \mathcal{T}(y)$ divides all elements of $\mathcal{T}(x)$. We conclude that $\gcd \mathcal{T}(y) \leq \gcd \mathcal{T}(x)$. By an entirely parallel argument, $\gcd \mathcal{T}(x) \leq \gcd \mathcal{T}(y)$. $\blacksquare$

For an irreducible chain, the period of the chain is defined to be the period which is common to all states. The chain will be called ***aperiodic*** if all states have period 1. If a chain is not aperiodic, we call it ***periodic***.

PROPOSITION 1.7. *If $P$ is aperiodic and irreducible, then there is an integer $r_0$ such that $P^r(x,y) > 0$ for all $x, y \in \mathcal{X}$ and $r \geq r_0$.*

PROOF. We use the following number-theoretic fact: any set of non-negative integers which is closed under addition and which has greatest common divisor 1 must contain all but finitely many of the non-negative integers. (See Lemma 1.30 in the Notes of this chapter for a proof.) For $x \in \mathcal{X}$, recall that $\mathcal{T}(x) = \{t \geq 1 : P^t(x,x) > 0\}$. Since the chain is aperiodic, the gcd of $\mathcal{T}(x)$ is 1. The set $\mathcal{T}(x)$ is closed under addition: if $s, t \in \mathcal{T}(x)$, then $P^{s+t}(x,x) \geq P^s(x,x)P^t(x,x) > 0$, and hence $s + t \in \mathcal{T}(x)$. Therefore there exists a $t(x)$ such that $t \geq t(x)$ implies $t \in \mathcal{T}(x)$. By irreducibility we know that for any $y \in \mathcal{X}$ there exists $r = r(x,y)$ such that $P^r(x,y) > 0$. Therefore, for $t \geq t(x) + r$,
$$ P^t(x,y) \geq P^{t-r}(x,x)P^r(x,y) > 0. $$
For $t \geq t'(x) := t(x) + \max_{y \in \mathcal{X}} r(x,y)$, we have $P^t(x,y) > 0$ for all $y \in \mathcal{X}$. Finally, if $t \geq \max_{x \in \mathcal{X}} t'(x)$, then $P^t(x,y) > 0$ for all $x, y \in \mathcal{X}$. $\blacksquare$

Suppose that a chain is irreducible with period two, e.g. the simple random walk on a cycle of even length (see Figure 1.3). The state space $\mathcal{X}$ can be partitioned into

### PDF page 24 (book page 8)

two classes, say ***even*** and ***odd***, such that the chain makes transitions only between states in complementary classes. (Exercise 1.6 examines chains with period $b$.)

Let $P$ have period two, and suppose that $x_0$ is an even state. The probability distribution of the chain after $2t$ steps, $P^{2t}(x_0, \cdot)$, is supported on even states, while the distribution of the chain after $2t + 1$ steps is supported on odd states. It is evident that we cannot expect the distribution $P^t(x_0, \cdot)$ to converge as $t \to \infty$.

Fortunately, a simple modification can repair periodicity problems. Given an arbitrary transition matrix $P$, let $Q = \frac{I+P}{2}$ (here $I$ is the $|\mathcal{X}| \times |\mathcal{X}|$ identity matrix). (One can imagine simulating $Q$ as follows: at each time step, flip a fair coin. If it comes up heads, take a step in $P$; if tails, then stay at the current state.) Since $Q(x,x) > 0$ for all $x \in \mathcal{X}$, the transition matrix $Q$ is aperiodic. We call $Q$ a ***lazy version of*** $P$. It will often be convenient to analyze lazy versions of chains.

EXAMPLE 1.8 (The $n$-cycle, revisited). Recall random walk on the $n$-cycle, defined in Example 1.4. For every $n \geq 1$, random walk on the $n$-cycle is irreducible.

Random walk on any even-length cycle is periodic, since $\gcd\{t : P^t(x,x) > 0\} = 2$ (see Figure 1.3). Random walk on an odd-length cycle is aperiodic.

For $n \geq 3$, the transition matrix $Q$ for lazy random walk on the $n$-cycle is
$$ Q(j,k) = \begin{cases} 1/4 & \text{if } k \equiv j+1 \pmod{n}, \\ 1/2 & \text{if } k \equiv j \pmod{n}, \\ 1/4 & \text{if } k \equiv j-1 \pmod{n}, \\ 0 & \text{otherwise.} \end{cases} \tag{1.12} $$
Lazy random walk on the $n$-cycle is both irreducible and aperiodic for every $n$.

REMARK 1.9. Establishing that a Markov chain is irreducible is not always trivial; see Example B.5, and also **Thurston (1990)**.

**1.4. Random Walks on Graphs**

Random walk on the $n$-cycle, which is shown in Figure 1.3, is a simple case of an important type of Markov chain.

A ***graph*** $G = (V,E)$ consists of a ***vertex set*** $V$ and an ***edge set*** $E$, where the elements of $E$ are unordered pairs of vertices: $E \subset \{\{x,y\} : x, y \in V, x \neq y\}$. We can think of $V$ as a set of dots, where two dots $x$ and $y$ are joined by a line if and only if $\{x,y\}$ is an element of the edge set. When $\{x,y\} \in E$, we write $x \sim y$ and say that $y$ is a ***neighbor*** of $x$ (and also that $x$ is a neighbor of $y$). The ***degree*** $\deg(x)$ of a vertex $x$ is the number of neighbors of $x$.

Given a graph $G = (V,E)$, we can define ***simple random walk on*** $G$ to be the Markov chain with state space $V$ and transition matrix
$$ P(x,y) = \begin{cases} \frac{1}{\deg(x)} & \text{if } y \sim x, \\ 0 & \text{otherwise.} \end{cases} \tag{1.13} $$
That is to say, when the chain is at vertex $x$, it examines all the neighbors of $x$, picks one uniformly at random, and moves to the chosen vertex.

EXAMPLE 1.10. Consider the graph $G$ shown in Figure 1.4. The transition

### PDF page 25 (book page 9)

**FIGURE 1.4.** An example of a graph with vertex set $\{1, 2, 3, 4, 5\}$ and 6 edges. *[Figure: a graph on five black-filled numbered vertices; vertex 2 connects to 1, 3, and 4; vertex 4 connects to 2 and 3; vertex 3 connects to 1, 2, 4, and 5; forming two triangles (1-2-3 and 2-3-4) sharing edge 2-3, with vertex 5 hanging off vertex 3.]*

matrix of simple random walk on $G$ is

$$
P = \begin{pmatrix}
0 & \frac{1}{2} & \frac{1}{2} & 0 & 0 \\
\frac{1}{3} & 0 & \frac{1}{3} & \frac{1}{3} & 0 \\
\frac{1}{4} & \frac{1}{4} & 0 & \frac{1}{4} & \frac{1}{4} \\
0 & \frac{1}{2} & \frac{1}{2} & 0 & 0 \\
0 & 0 & 1 & 0 & 0
\end{pmatrix}.
$$

REMARK 1.11. We have chosen a narrow definition of "graph" for simplicity. It is sometimes useful to allow edges connecting a vertex to itself, called **loops**. It is also sometimes useful to allow multiple edges connecting a single pair of vertices. Loops and multiple edges both contribute to the degree of a vertex and are counted as options when a simple random walk chooses a direction. See Section 6.5.1 for an example.

We will have much more to say about random walks on graphs throughout this book—but especially in Chapter 9.

**1.5. Stationary Distributions**

**1.5.1. Definition.** We saw in Example 1.1 that a distribution $\pi$ on $\mathcal{X}$ satisfying

$$ \pi = \pi P \tag{1.14} $$

can have another interesting property: in that case, $\pi$ was the long-term limiting distribution of the chain. We call a probability $\pi$ satisfying (1.14) a **stationary distribution** of the Markov chain. Clearly, if $\pi$ is a stationary distribution and $\mu_0 = \pi$ (i.e. the chain is started in a stationary distribution), then $\mu_t = \pi$ for all $t \geq 0$.

Note that we can also write (1.14) elementwise. An equivalent formulation is

$$ \pi(y) = \sum_{x \in \mathcal{X}} \pi(x) P(x, y) \quad \text{for all } y \in \mathcal{X}. \tag{1.15} $$

EXAMPLE 1.12. Consider simple random walk on a graph $G = (V, E)$. For any vertex $y \in V$,

$$ \sum_{x \in V} \deg(x) P(x, y) = \sum_{x \sim y} \frac{\deg(x)}{\deg(x)} = \deg(y). \tag{1.16} $$

### PDF page 26 (book page 10)

To get a probability, we simply normalize by $\sum_{y \in V} \deg(y) = 2|E|$ (a fact the reader should check). We conclude that the probability measure

$$ \pi(y) = \frac{\deg(y)}{2|E|} \quad \text{for all } y \in \mathcal{X}, $$

which is proportional to the degrees, is always a stationary distribution for the walk. For the graph in Figure 1.4,

$$ \pi = \left( \tfrac{2}{12}, \tfrac{3}{12}, \tfrac{4}{12}, \tfrac{2}{12}, \tfrac{1}{12} \right). $$

If $G$ has the property that every vertex has the same degree $d$, we call $G$ $d$-**regular**. In this case $2|E| = d|V|$ and the uniform distribution $\pi(y) = 1/|V|$ for every $y \in V$ is stationary.

A central goal of this chapter and of Chapter 4 is to prove a general yet precise version of the statement that "finite Markov chains converge to their stationary distributions." Before we can analyze the time required to be close to stationarity, we must be sure that it is finite! In this section we show that, under mild restrictions, stationary distributions exist and are unique. Our strategy of building a candidate distribution, then verifying that it has the necessary properties, may seem cumbersome. However, the tools we construct here will be applied in many other places. In Section 4.3, we will show that irreducible and aperiodic chains do, in fact, converge to their stationary distributions in a precise sense.

**1.5.2. Hitting and first return times.** Throughout this section, we assume that the Markov chain $(X_0, X_1, \dots)$ under discussion has finite state space $\mathcal{X}$ and transition matrix $P$. For $x \in \mathcal{X}$, define the **hitting time** for $x$ to be

$$ \tau_x := \min\{t \geq 0 : X_t = x\}, $$

the first time at which the chain visits state $x$. For situations where only a visit to $x$ at a positive time will do, we also define

$$ \tau_x^+ := \min\{t \geq 1 \, : \, X_t = x\}. $$

When $X_0 = x$, we call $\tau_x^+$ the **first return time**.

LEMMA 1.13. *For any states $x$ and $y$ of an irreducible chain, $\mathbf{E}_x(\tau_y^+) < \infty$.*

PROOF. The definition of irreducibility implies that there exist an integer $r > 0$ and a real $\varepsilon > 0$ with the following property: for any states $z, w \in \mathcal{X}$, there exists a $j \leq r$ with $P^j(z, w) > \varepsilon$. Thus for any value of $X_t$, the probability of hitting state $y$ at a time between $t$ and $t + r$ is at least $\varepsilon$. Hence for $k > 0$ we have

$$ \mathbf{P}_x\{\tau_y^+ > kr\} \leq (1 - \varepsilon)\mathbf{P}_x\{\tau_y^+ > (k-1)r\}. \tag{1.17} $$

Repeated application of (1.17) yields

$$ \mathbf{P}_x\{\tau_y^+ > kr\} \leq (1 - \varepsilon)^k. \tag{1.18} $$

Recall that when $Y$ is a non-negative integer-valued random variable, we have

$$ \mathbf{E}(Y) = \sum_{t \geq 0} \mathbf{P}\{Y > t\}. $$

### PDF page 27 (book page 11)

Since $\mathbf{P}_x\{\tau_y^+ > t\}$ is a decreasing function of $t$, (1.18) suffices to bound all terms of the corresponding expression for $\mathbf{E}_x(\tau_y^+)$:

$$ \mathbf{E}_x(\tau_y^+) = \sum_{t \geq 0} \mathbf{P}_x\{\tau_y^+ > t\} \leq \sum_{k \geq 0} r\mathbf{P}_x\{\tau_y^+ > kr\} \leq r \sum_{k \geq 0} (1 - \varepsilon)^k < \infty. $$

$\blacksquare$

**1.5.3. Existence of a stationary distribution.** The Convergence Theorem (Theorem 4.9 below) implies that the long-term fraction of time a finite irreducible aperiodic Markov chain spends in each state coincide with the chain's stationary distribution. However, we have not yet demonstrated that stationary distributions exist!

We give an explicit construction of the stationary distribution $\pi$, which in the irreducible case gives the useful identity $\pi(x) = \left[\mathbf{E}_x(\tau_x^+)\right]^{-1}$. We consider a sojourn of the chain from some arbitrary state $z$ back to $z$. Since visits to $z$ break up the trajectory of the chain into identically distributed segments, it should not be surprising that the average fraction of time per segment spent in each state $y$ coincides with the long-term fraction of time spent in $y$.

Let $z \in \mathcal{X}$ be an arbitrary state of the Markov chain. We will closely examine the average time the chain spends at each state in between visits to $z$. To this end, we define

$$
\begin{aligned}
\tilde{\pi}(y) &:= \mathbf{E}_z(\text{number of visits to } y \text{ before returning to } z) \\
&= \sum_{t=0}^{\infty} \mathbf{P}_z\{X_t = y, \tau_z^+ > t\}.
\end{aligned}
\tag{1.19}
$$

PROPOSITION 1.14. *Let $\tilde{\pi}$ be the measure on $\mathcal{X}$ defined by (1.19).*

(i) *If $\mathbf{P}_z\{\tau_z^+ < \infty\} = 1$, then $\tilde{\pi}$ satisfies $\tilde{\pi}P = \tilde{\pi}$.*

(ii) *If $\mathbf{E}_z(\tau_z^+) < \infty$, then $\pi := \frac{\tilde{\pi}}{\mathbf{E}_z(\tau_z^+)}$ is a stationary distribution.*

REMARK 1.15. Recall that Lemma 1.13 shows that if $P$ is irreducible, then $\mathbf{E}_z(\tau_z^+) < \infty$. We will show in Section 1.7 that the assumptions of (i) and (ii) are always equivalent (Corollary 1.27) and there always exists $z$ satisfying both.

PROOF. For any state $y$, we have $\tilde{\pi}(y) \leq \mathbf{E}_z\tau_z^+$. Hence Lemma 1.13 ensures that $\tilde{\pi}(y) < \infty$ for all $y \in \mathcal{X}$. We check that $\tilde{\pi}$ is stationary, starting from the definition:

$$ \sum_{x \in \mathcal{X}} \tilde{\pi}(x) P(x, y) = \sum_{x \in \mathcal{X}} \sum_{t=0}^{\infty} \mathbf{P}_z\{X_t = x, \tau_z^+ > t\} P(x, y). \tag{1.20} $$

Because the event $\{\tau_z^+ \geq t + 1\} = \{\tau_z^+ > t\}$ is determined by $X_0, \dots, X_t$,

$$ \mathbf{P}_z\{X_t = x, \, X_{t+1} = y, \, \tau_z^+ \geq t + 1\} = \mathbf{P}_z\{X_t = x, \, \tau_z^+ \geq t + 1\} P(x, y). \tag{1.21} $$

Reversing the order of summation in (1.20) and using the identity (1.21) shows that

$$
\begin{aligned}
\sum_{x \in \mathcal{X}} \tilde{\pi}(x) P(x, y) &= \sum_{t=0}^{\infty} \mathbf{P}_z\{X_{t+1} = y, \tau_z^+ \geq t + 1\} \\
&= \sum_{t=1}^{\infty} \mathbf{P}_z\{X_t = y, \tau_z^+ \geq t\}.
\end{aligned}
\tag{1.22}
$$

### PDF page 28 (book page 12)

The expression in (1.22) is very similar to (1.19), so we are almost done. In fact,

$$
\begin{aligned}
\sum_{t=1}^{\infty} \mathbf{P}_z\{X_t = y, \tau_z^+ \geq t\} \\
&= \tilde{\pi}(y) - \mathbf{P}_z\{X_0 = y, \tau_z^+ > 0\} + \sum_{t=1}^{\infty} \mathbf{P}_z\{X_t = y, \tau_z^+ = t\} \\
&= \tilde{\pi}(y) - \mathbf{P}_z\{X_0 = y\} + \mathbf{P}_z\{X_{\tau_z^+} = y\}. \tag{1.23} \\
&= \tilde{\pi}(y). \tag{1.24}
\end{aligned}
$$

The equality (1.24) follows by considering two cases:

$y = z$: Since $X_0 = z$ and $X_{\tau_z^+} = z$, the last two terms of (1.23) are both 1, and they cancel each other out.

$y \neq z$: Here both terms of (1.23) are 0.

Therefore, combining (1.22) with (1.24) shows that $\tilde{\pi} = \tilde{\pi}P$.

Finally, to get a probability measure, we normalize by $\sum_x \tilde{\pi}(x) = \mathbf{E}_z(\tau_z^+)$:

$$
\pi(x) = \frac{\tilde{\pi}(x)}{\mathbf{E}_z(\tau_z^+)} \quad \text{satisfies } \pi = \pi P. \tag{1.25}
$$

$\blacksquare$

The computation at the heart of the proof of Proposition 1.14 can be generalized; See Lemma 10.5. Informally speaking, a *stopping time* $\tau$ for $(X_t)$ is a $\{0, 1, \dots, \} \cup \{\infty\}$-valued random variable such that, for each $t$, the event $\{\tau = t\}$ is determined by $X_0, \dots, X_t$. (Stopping times are defined precisely in Section 6.2.) If a stopping time $\tau$ replaces $\tau_z^+$ in the definition (1.19) of $\tilde{\pi}$, then the proof that $\tilde{\pi}$ satisfies $\tilde{\pi} = \tilde{\pi}P$ works, provided that $\tau$ satisfies both $\mathbf{P}_z\{\tau < \infty\} = 1$ and $\mathbf{P}_z\{X_\tau = z\} = 1$.

**1.5.4. Uniqueness of the stationary distribution.** Earlier in this chapter we pointed out the difference between multiplying a row vector by $P$ on the right and a column vector by $P$ on the left: the former advances a distribution by one step of the chain, while the latter gives the expectation of a function on states, one step of the chain later. We call distributions invariant under right multiplication by $P$ **stationary**. What about functions that are invariant under left multiplication?

Call a function $h : \mathcal{X} \to \mathbb{R}$ **harmonic at** $x$ if

$$
h(x) = \sum_{y \in \mathcal{X}} P(x, y)h(y). \tag{1.26}
$$

A function is **harmonic on** $D \subset \mathcal{X}$ if it is harmonic at every state $x \in D$. If $h$ is regarded as a column vector, then a function which is harmonic on all of $\mathcal{X}$ satisfies the matrix equation $Ph = h$.

LEMMA 1.16. *Suppose that $P$ is irreducible. A function $h$ which is harmonic at every point of $\mathcal{X}$ is constant.*

PROOF. Since $\mathcal{X}$ is finite, there must be a state $x_0$ such that $h(x_0) = M$ is maximal. If for some state $z$ such that $P(x_0, z) > 0$ we have $h(z) < M$, then

$$
h(x_0) = P(x_0, z)h(z) + \sum_{y \neq z} P(x_0, y)h(y) < M, \tag{1.27}
$$

a contradiction. It follows that $h(z) = M$ for all states $z$ such that $P(x_0, z) > 0$.

### PDF page 29 (book page 13)

For any $y \in \mathcal{X}$, irreducibility implies that there is a sequence $x_0, x_1, \dots, x_n = y$ with $P(x_i, x_{i+1}) > 0$. Repeating the argument above tells us that $h(y) = h(x_{n-1}) = \cdots = h(x_0) = M$. Thus $h$ is constant. $\blacksquare$

COROLLARY 1.17. *Let $P$ be the transition matrix of an irreducible Markov chain. There exists a unique probability distribution $\pi$ satisfying $\pi = \pi P$.*

PROOF. By Proposition 1.14 there exists at least one such measure. Lemma 1.16 implies that the kernel of $P - I$ has dimension 1, so the column rank of $P - I$ is $|\mathcal{X}| - 1$. Since the row rank of any matrix is equal to its column rank, the row-vector equation $\nu = \nu P$ also has a one-dimensional space of solutions. This space contains only one vector whose entries sum to 1. $\blacksquare$

REMARK 1.18. Another proof of Corollary 1.17 follows from the Convergence Theorem (Theorem 4.9, proved below). Another simple direct proof is suggested in Exercise 1.11.

PROPOSITION 1.19. *If $P$ is an irreducible transition matrix and $\pi$ is the unique probability distribution solving $\pi = \pi P$, then for all states $z$,*

$$
\pi(z) = \frac{1}{\mathbf{E}_z \tau_z^+}. \tag{1.28}
$$

PROOF. Let $\tilde{\pi}_z(y)$ equal $\tilde{\pi}(y)$ as defined in (1.19), and write $\pi_z(y) = \tilde{\pi}_z(y)/\mathbf{E}_z\tau_z^+$. Proposition 1.14 implies that $\pi_z$ is a stationary distribution, so $\pi_z = \pi$. Therefore,

$$
\pi(z) = \pi_z(z) = \frac{\tilde{\pi}_z(z)}{\mathbf{E}_z\tau_z^+} = \frac{1}{\mathbf{E}_z\tau_z^+}.
$$

$\blacksquare$

**1.6. Reversibility and Time Reversals**

Suppose a probability distribution $\pi$ on $\mathcal{X}$ satisfies

$$
\pi(x)P(x, y) = \pi(y)P(y, x) \quad \text{for all } x, y \in \mathcal{X}. \tag{1.29}
$$

The equations (1.29) are called the **detailed balance equations**.

PROPOSITION 1.20. *Let $P$ be the transition matrix of a Markov chain with state space $\mathcal{X}$. Any distribution $\pi$ satisfying the detailed balance equations (1.29) is stationary for $P$.*

PROOF. Sum both sides of (1.29) over all $y$:

$$
\sum_{y \in \mathcal{X}} \pi(y)P(y, x) = \sum_{y \in \mathcal{X}} \pi(x)P(x, y) = \pi(x),
$$

since $P$ is stochastic. $\blacksquare$

Checking detailed balance is often the simplest way to verify that a particular distribution is stationary. Furthermore, when (1.29) holds,

$$
\pi(x_0)P(x_0, x_1) \cdots P(x_{n-1}, x_n) = \pi(x_n)P(x_n, x_{n-1}) \cdots P(x_1, x_0). \tag{1.30}
$$

We can rewrite (1.30) in the following suggestive form:

$$
\mathbf{P}_\pi\{X_0 = x_0, \dots, X_n = x_n\} = \mathbf{P}_\pi\{X_0 = x_n, X_1 = x_{n-1}, \dots, X_n = x_0\}. \tag{1.31}
$$

In other words, if a chain $(X_t)$ satisfies (1.29) and has stationary initial distribution, then the distribution of $(X_0, X_1, \dots, X_n)$ is the same as the distribution of

### PDF page 30 (book page 14)

$(X_n, X_{n-1}, \dots, X_0)$. For this reason, a chain satisfying (1.29) is called **reversible**.

EXAMPLE 1.21. Consider the simple random walk on a graph $G$. We saw in Example 1.12 that the distribution $\pi(x) = \deg(x)/2|E|$ is stationary. Since

$$
\pi(x)P(x, y) = \frac{\deg(x)}{2|E|}\frac{\mathbf{1}_{\{x \sim y\}}}{\deg(x)} = \frac{\mathbf{1}_{\{x \sim y\}}}{2|E|} = \pi(y)P(y, x),
$$

the chain is reversible. (Note: here the notation $\mathbf{1}_A$ represents the **indicator function** of a set $A$, for which $\mathbf{1}_A(a) = 1$ if and only if $a \in A$; otherwise $\mathbf{1}_A(a) = 0$.)

EXAMPLE 1.22. Consider the **biased random walk on the $n$-cycle**: a particle moves clockwise with probability $p$ and moves counterclockwise with probability $q = 1 - p$.

The stationary distribution remains uniform: if $\pi(k) = 1/n$, then

$$
\sum_{j \in \mathbb{Z}_n} \pi(j)P(j, k) = \pi(k - 1)p + \pi(k + 1)q = \frac{1}{n},
$$

whence $\pi$ is the stationary distribution. However, if $p \neq 1/2$, then

$$
\pi(k)P(k, k + 1) = \frac{p}{n} \neq \frac{q}{n} = \pi(k + 1)P(k + 1, k).
$$

The **time reversal** of an irreducible Markov chain with transition matrix $P$ and stationary distribution $\pi$ is the chain with matrix

$$
\widehat{P}(x, y) := \frac{\pi(y)P(y, x)}{\pi(x)}. \tag{1.32}
$$

The stationary equation $\pi = \pi P$ implies that $\widehat{P}$ is a stochastic matrix. Proposition 1.23 shows that the terminology "time reversal" is deserved.

PROPOSITION 1.23. *Let $(X_t)$ be an irreducible Markov chain with transition matrix $P$ and stationary distribution $\pi$. Write $(\widehat{X}_t)$ for the time-reversed chain with transition matrix $\widehat{P}$. Then $\pi$ is stationary for $\widehat{P}$, and for any $x_0, \dots, x_t \in \mathcal{X}$ we have*

$$
\mathbf{P}_\pi\{X_0 = x_0, \dots, X_t = x_t\} = \mathbf{P}_\pi\{\widehat{X}_0 = x_t, \dots, \widehat{X}_t = x_0\}.
$$

PROOF. To check that $\pi$ is stationary for $\widehat{P}$, we simply compute

$$
\sum_{y \in \mathcal{X}} \pi(y)\widehat{P}(y, x) = \sum_{y \in \mathcal{X}} \pi(y)\frac{\pi(x)P(x, y)}{\pi(y)} = \pi(x).
$$

To show the probabilities of the two trajectories are equal, note that

$$
\begin{aligned}
\mathbf{P}_\pi\{X_0 = x_0, \dots, X_n = x_n\} &= \pi(x_0)P(x_0, x_1)P(x_1, x_2) \cdots P(x_{n-1}, x_n) \\
&= \pi(x_n)\widehat{P}(x_n, x_{n-1}) \cdots \widehat{P}(x_2, x_1)\widehat{P}(x_1, x_0) \\
&= \mathbf{P}_\pi\{\hat{X}_0 = x_n, \dots, \hat{X}_n = x_0\},
\end{aligned}
$$

since $P(x_{i-1}, x_i) = \pi(x_i)\widehat{P}(x_i, x_{i-1})/\pi(x_{i-1})$ for each $i$. $\blacksquare$

Observe that if a chain with transition matrix $P$ is reversible, then $\widehat{P} = P$.

### PDF page 31 (book page 15)

**1.7. Classifying the States of a Markov Chain\***

We will occasionally need to study chains which are *not* irreducible—see, for instance, Sections 2.1, 2.2 and 2.4. In this section we describe a way to classify the states of a Markov chain. This classification clarifies what can occur when irreducibility fails.

Let $P$ be the transition matrix of a Markov chain on a finite state space $\mathcal{X}$. Given $x, y \in \mathcal{X}$, we say that $y$ *is accessible from* $x$ and write $x \to y$ if there exists an $r > 0$ such that $P^r(x, y) > 0$. That is, $x \to y$ if it is possible for the chain to move from $x$ to $y$ in a finite number of steps. Note that if $x \to y$ and $y \to z$, then $x \to z$.

A state $x \in \mathcal{X}$ is called *essential* if for all $y$ such that $x \to y$ it is also true that $y \to x$. A state $x \in \mathcal{X}$ is *inessential* if it is not essential.

REMARK 1.24. For finite chains, a state $x$ is essential if and only if

$$\mathbf{P}_x\{\tau_x^+ < \infty\} = 1 \,. \tag{1.33}$$

States satisfying (1.33) are called *recurrent*. For infinite chains, the two properties can be different. For example, for a random walk on $\mathbb{Z}^3$, all states are essential, but none are recurrent. (See Chapter 21.) Note that the classification of a state as essential depends only on the directed graph with vertex set equal to the state space of the chain, that includes the directed edge $(x, y)$ in its edge set iff $P(x, y) > 0$.

We say that $x$ *communicates with* $y$ and write $x \leftrightarrow y$ if and only if $x \to y$ and $y \to x$, or $x = y$. The equivalence classes under $\leftrightarrow$ are called *communicating classes*. For $x \in \mathcal{X}$, the communicating class of $x$ is denoted by $[x]$.

Observe that when $P$ is irreducible, all the states of the chain lie in a single communicating class.

LEMMA 1.25. *If $x$ is an essential state and $x \to y$, then $y$ is essential.*

PROOF. If $y \to z$, then $x \to z$. Therefore, because $x$ is essential, $z \to x$, whence $z \to y$. $\blacksquare$

It follows directly from the above lemma that the states in a single communicating class are either all essential or all inessential. We can therefore classify the communicating classes as either essential or inessential.

If $[x] = \{x\}$ and $x$ is inessential, then once the chain leaves $x$, it never returns. If $[x] = \{x\}$ and $x$ is essential, then the chain never leaves $x$ once it first visits $x$; such states are called *absorbing*.

LEMMA 1.26. *Every finite chain has at least one essential class.*

PROOF. Define inductively a sequence $(y_0, y_1, \ldots)$ as follows: Fix an arbitrary initial state $y_0$. For $k \geq 1$, given $(y_0, \ldots, y_{k-1})$, if $y_{k-1}$ is essential, stop. Otherwise, find $y_k$ such that $y_{k-1} \to y_k$ but $y_k \not\to y_{k-1}$.

There can be no repeated states in this sequence, because if $j < k$ and $y_k \to y_j$, then $y_k \to y_{k-1}$, a contradiction.

Since the state space is finite and the sequence cannot repeat elements, it must eventually terminate in an essential state. $\blacksquare$

Let $P_\mathcal{C} = P_{\mathcal{C} \times \mathcal{C}}$ be the restriction of the matrix $P$ to the set of states $\mathcal{C} \subset \mathcal{X}$. If $\mathcal{C} = [x]$ is an essential class, then $P_\mathcal{C}$ is stochastic. That is, $\sum_{y \in [x]} P(x, y) = 1$, since

### PDF page 32 (book page 16)

FIGURE 1.5. The directed graph associated to a Markov chain. A directed edge is placed between $v$ and $w$ if and only if $P(v, w) > 0$. Here there is one essential class, which consists of the filled vertices. *[Figure: a directed graph of eight vertices; the three vertices on the right are filled (solid black) and form the single essential class, with the remaining five open (unfilled) vertices on the left connected by directed edges leading into that essential class.]*

$P(x, z) = 0$ for $z \notin [x]$. Moreover, $P_\mathcal{C}$ is irreducible by definition of a communicating class.

COROLLARY 1.27. *If $\mathbf{P}_z\{\tau_z^+ < \infty\}$ then $\mathbf{E}_z(\tau_z^+) < \infty$.*

PROOF. If $z$ satisfies $\mathbf{P}_z\{\tau_z^+ < \infty\}$, then $z$ is an essential state. Thus if $\mathcal{C} = [z]$, the restriction $P_\mathcal{C}$ is irreducible. Applying Lemma 1.13 to $P_\mathcal{C}$ shows that $\mathbf{E}_z(\tau_z^+) < \infty$. $\blacksquare$

PROPOSITION 1.28. *If $\pi$ is stationary for the finite transition matrix $P$, then $\pi(y_0) = 0$ for all inessential states $y_0$.*

PROOF. Let $\mathcal{C}$ be an essential communicating class. Then

$$\pi P(\mathcal{C}) = \sum_{z \in \mathcal{C}} (\pi P)(z) = \sum_{z \in \mathcal{C}} \left[ \sum_{y \in \mathcal{C}} \pi(y) P(y, z) + \sum_{y \notin \mathcal{C}} \pi(y) P(y, z) \right].$$

We can interchange the order of summation in the first sum, obtaining

$$\pi P(\mathcal{C}) = \sum_{y \in \mathcal{C}} \pi(y) \sum_{z \in \mathcal{C}} P(y, z) + \sum_{z \in \mathcal{C}} \sum_{y \notin \mathcal{C}} \pi(y) P(y, z).$$

For $y \in \mathcal{C}$ we have $\sum_{z \in \mathcal{C}} P(y, z) = 1$, so

$$\pi P(\mathcal{C}) = \pi(\mathcal{C}) + \sum_{z \in \mathcal{C}} \sum_{y \notin \mathcal{C}} \pi(y) P(y, z). \tag{1.34}$$

Since $\pi$ is invariant, $\pi P(\mathcal{C}) = \pi(\mathcal{C})$. In view of (1.34) we must have $\pi(y) P(y, z) = 0$ for all $y \notin \mathcal{C}$ and $z \in \mathcal{C}$.

Suppose that $y_0$ is inessential. The proof of Lemma 1.26 shows that there is a sequence of states $y_0, y_1, y_2, \ldots, y_r$ satisfying $P(y_{i-1}, y_i) > 0$, the states $y_0, y_1, \ldots, y_{r-1}$ are inessential, and $y_r \in \mathcal{D}$, where $\mathcal{D}$ is an essential communicating class. Since $P(y_{r-1}, y_r) > 0$ and we just proved that $\pi(y_{r-1}) P(y_{r-1}, y_r) = 0$, it follows that $\pi(y_{r-1}) = 0$. If $\pi(y_k) = 0$, then

$$0 = \pi(y_k) = \sum_{y \in \mathcal{X}} \pi(y) P(y, y_k).$$

### PDF page 33 (book page 17)

This implies $\pi(y) P(y, y_k) = 0$ for all $y$. In particular, $\pi(y_{k-1}) = 0$. By induction backwards along the sequence, we find that $\pi(y_0) = 0$. $\blacksquare$

Finally, we conclude with the following proposition:

PROPOSITION 1.29. *The transition matrix $P$ has a unique stationary distribution if and only if there is a unique essential communicating class.*

PROOF. Suppose that there is a unique essential communicating class $\mathcal{C}$. Recall that $P_\mathcal{C}$ is the restriction of the matrix $P$ to the states in $\mathcal{C}$, and that $P_{|\mathcal{C}}$ is a transition matrix, irreducible on $\mathcal{C}$ with a unique stationary distribution $\pi^\mathcal{C}$ for $P_\mathcal{C}$. Let $\pi$ be a probability on $\mathcal{X}$ with $\pi = \pi P$. By Proposition 1.28, $\pi(y) = 0$ for $y \notin \mathcal{C}$, whence $\pi$ is supported on $\mathcal{C}$. Consequently, for $x \in \mathcal{C}$,

$$\pi(x) = \sum_{y \in \mathcal{X}} \pi(y) P(y, x) = \sum_{y \in \mathcal{C}} \pi(y) P(y, x) = \sum_{y \in \mathcal{C}} \pi(y) P_\mathcal{C}(y, x),$$

and $\pi$ restricted to $\mathcal{C}$ is stationary for $P_\mathcal{C}$. By uniqueness of the stationary distribution for $P_\mathcal{C}$, it follows that $\pi(x) = \pi^\mathcal{C}(x)$ for all $x \in \mathcal{C}$. Therefore,

$$\pi(x) = \begin{cases} \pi^\mathcal{C}(x) & \text{if } x \in \mathcal{C}, \\ 0 & \text{if } x \notin \mathcal{C}, \end{cases}$$

and the solution to $\pi = \pi P$ is unique.

Suppose there are distinct essential communicating classes for $P$, say $\mathcal{C}_1$ and $\mathcal{C}_2$. The restriction of $P$ to each of these classes is irreducible. Thus for $i = 1, 2$, there exists a measure $\pi$ supported on $\mathcal{C}_i$ which is stationary for $P_{\mathcal{C}_i}$. Moreover, it is easily verified that each $\pi_i$ is stationary for $P$, and so $P$ has more than one stationary distribution. $\blacksquare$

**Exercises**

EXERCISE 1.1. Let $P$ be the transition matrix of random walk on the $n$-cycle, where $n$ is odd. Find the smallest value of $t$ such that $P^t(x, y) > 0$ for all states $x$ and $y$.

EXERCISE 1.2. A graph $G$ is *connected* when, for two vertices $x$ and $y$ of $G$, there exists a sequence of vertices $x_0, x_1, \ldots, x_k$ such that $x_0 = x$, $x_k = y$, and $x_i \sim x_{i+1}$ for $0 \leq i \leq k-1$. Show that random walk on $G$ is irreducible if and only if $G$ is connected.

EXERCISE 1.3. We define a graph to be a *tree* if it is connected but contains no cycles. Prove that the following statements about a graph $T$ with $n$ vertices and $m$ edges are equivalent:

(a) $T$ is a tree.
(b) $T$ is connected and $m = n - 1$.
(c) $T$ has no cycles and $m = n - 1$.

EXERCISE 1.4. Let $T$ be a finite tree. A *leaf* is a vertex of degree 1.

(a) Prove that $T$ contains a leaf.
(b) Prove that between any two vertices in $T$ there is a unique simple path.
(c) Prove that $T$ has at least 2 leaves.

### PDF page 34 (book page 18)

EXERCISE 1.5. Let $T$ be a tree. Show that the graph whose vertices are proper 3-colorings of $T$ and whose edges are pairs of colorings which differ at only a single vertex is connected.

EXERCISE 1.6. Let $P$ be an irreducible transition matrix of period $b$. Show that $\mathcal{X}$ can be partitioned into $b$ sets $\mathcal{C}_1, \mathcal{C}_2, \ldots, \mathcal{C}_b$ in such a way that $P(x, y) > 0$ only if $x \in \mathcal{C}_i$ and $y \in \mathcal{C}_{i+1}$. (The addition $i + 1$ is modulo $b$.)

EXERCISE 1.7. A transition matrix $P$ is ***symmetric*** if $P(x, y) = P(y, x)$ for all $x, y \in \mathcal{X}$. Show that if $P$ is symmetric, then the uniform distribution on $\mathcal{X}$ is stationary for $P$.

EXERCISE 1.8. Let $P$ be a transition matrix which is reversible with respect to the probability distribution $\pi$ on $\mathcal{X}$. Show that the transition matrix $P^2$ corresponding to two steps of the chain is also reversible with respect to $\pi$.

EXERCISE 1.9. Check carefully that equation (1.19) is true.

EXERCISE 1.10. Let $P$ be the transition matrix of an irreducible Markov chain with state space $\mathcal{X}$. Let $B \subset \mathcal{X}$ be a non-empty subset of the state space, and assume $h : \mathcal{X} \to \mathbb{R}$ is a function harmonic at all states $x \notin B$. Prove that there exists $y \in B$ with $h(y) = \max_{x \in \mathcal{X}} h(x)$.
(This is a discrete version of the ***maximum principle***.)

EXERCISE 1.11. Give a direct proof that the stationary distribution for an irreducible chain is unique.
*Hint:* Given stationary distributions $\pi_1$ and $\pi_2$, consider a state $x$ that minimizes $\pi_1(x)/\pi_2(x)$ and show that all $y$ with $P(y, x) > 0$ have $\pi_1(y)/\pi_2(y) = \pi_1(x)/\pi_2(x)$.

EXERCISE 1.12. Suppose that $P$ is the transition matrix for an irreducible Markov chain. For a subset $A \subset \mathcal{X}$, define $f(x) = \mathbf{E}_x(\tau_A)$. Show that
(a)
$$ f(x) = 0 \quad \text{for } x \in A. \tag{1.35} $$
(b)
$$ f(x) = 1 + \sum_{y \in \mathcal{X}} P(x, y)f(y) \quad \text{for } x \notin A. \tag{1.36} $$
(c) $f$ is uniquely determined by (1.35) and (1.36).

The following exercises concern the material in Section 1.7.

EXERCISE 1.13. Show that $\leftrightarrow$ is an equivalence relation on $\mathcal{X}$.

EXERCISE 1.14. Show that the set of stationary measures for a transition matrix forms a polyhedron with one vertex for each essential communicating class.

**Notes**

Markov first studied the stochastic processes that came to be named after him in **Markov (1906)**. See **Basharin, Langville, and Naumov (2004)** for the early history of Markov chains.

The right-hand side of (1.1) does not depend on $t$. We take this as part of the definition of a Markov chain; note that other authors sometimes regard this as a special case, which they call ***time homogeneous***. (This simply means that

### PDF page 35 (book page 19)

the transition matrix is the same at each step of the chain. It is possible to give a more general definition in which the transition matrix depends on $t$. We will almost always consider time homogenous chains in this book.)

**Aldous and Fill (1999**, Chapter 2, Proposition 4) present a version of the key computation for Proposition 1.14 which requires only that the initial distribution of the chain equals the distribution of the chain when it stops. We have essentially followed their proof.

The standard approach to demonstrating that irreducible aperiodic Markov chains have unique stationary distributions is through the Perron-Frobenius theorem. See, for instance, **Karlin and Taylor (1975)** or **Seneta (2006)**.

See **Feller (1968**, Chapter XV) for the classification of states of Markov chains.

The existence of an infinite sequence $(X_0, X_1, \ldots)$ of random variables which form a Markov chain is implied by the existence of i.i.d. uniform random variables, by the random mapping representation. The existence of i.i.d. uniforms is equivalent to the existence of Lebesgue measure on the unit interval: take the digits in the dyadic expansion of a uniformly chosen element of $[0, 1]$, and obtain countably many such dyadic expansions by writing the integers as a countable disjoint union of infinite sets.

**Complements.**

**1.7.1. Schur Lemma.** The following lemma is needed for the proof of Proposition 1.7. We include a proof here for completeness.

LEMMA 1.30 (Schur). *If $S \subset \mathbb{Z}^+$ has $\gcd(S) = g_S$, then there is some integer $m_S$ such that for all $m \geq m_S$ the product $mg_S$ can be written as a linear combination of elements of $S$ with non-negative integer coefficients.*

REMARK 1.31. The largest integer which cannot be represented as a non-negative integer combination of elements of $S$ is called the *Frobenius number*.

PROOF. *Step 1.* Given $S \subset \mathbb{Z}^+$ nonempty, define $g_S^\star$ as the smallest positive integer which is an integer combination of elements of $S$ (the smallest positive element of the additive group generated by $S$). Then $g_S^\star$ divides every element of $S$ (otherwise, consider the remainder) and $g_S$ must divide $g_S^\star$, so $g_S^\star = g_S$.

*Step 2.* For any set $S$ of positive integers, there is a finite subset $F$ such that $\gcd(S) = \gcd(F)$. Indeed the non-increasing sequence $\gcd(S \cap [1, n])$ can strictly decrease only finitely many times, so there is a last time. Thus it suffices to prove the fact for finite subsets $F$ of $\mathbb{Z}^+$; we start with sets of size 2 (size 1 is a tautology) and then prove the general case by induction on the size of $F$.

*Step 3.* Let $F = \{a, b\} \subset \mathbb{Z}^+$ have $\gcd(F) = g$. Given $m > 0$, write P $mg = ca + db$ for some integers $c, d$. Observe that $c, d$ are not unique since $mg = (c + kb)a + (d - ka)b$ for any $k$. Thus we can write $mg = ca + db$ where $0 \leq c < b$. If $mg > (b - 1)a - b$, then we must have $d \geq 0$ as well. Thus for $F = \{a, b\}$ we can take $m_F = (ab - a - b)/g + 1$.

*Step 4 (The induction step).* Let $F$ be a finite subset of $\mathbb{Z}^+$ with $\gcd(F) = g_F$. Then for any $a \in \mathbb{Z}^+$ the definition of gcd yields that $g := \gcd(\{a\} \cup F) = \gcd(a, g_F)$. Suppose that $n$ satisfies $ng \geq m_{\{a, g_F\}}g + m_F g_F$. Then we can write $ng - m_F g_F = ca + dg_F$ for integers $c, d \geq 0$. Therefore $ng = ca + (d + m_F)g_F = ca + \sum_{f \in F} c_f f$ for some integers $c_f \geq 0$ by the definition of $m_F$. Thus we can take $m_{\{a\} \cup F} = m_{\{a, g_F\}} + m_F g_F/g$. $\blacksquare$

### PDF page 36 (book page 20)

In Proposition 1.7 it is shown that there exists $r_0$ such that for $r \geq r_0$, all the entries of $P^r$ are strictly positive. A bound on smallest $r_0$ for which this holds is given by **Denardo (1977)**.

The following is an alternative direct proof that a stationary distribution exists.

PROPOSITION 1.32. *Let $P$ be any $n \times n$ stochastic matrix (possibly reducible), and let $Q_T := T^{-1} \sum_{t=0}^{T-1} P^t$ be the average of the first $t$ powers of $P$. Let $v$ be any probability vector, and define $v_T := vQ_T$. There is a probability vector $\pi$ such that $\pi P = \pi$ and $\lim_{T \to \infty} v_T = \pi$.*

PROOF. We first show that $\{v_T\}$ has a subsequential limit $\pi$ which satisifies [sic] $\pi = \pi P$.

Let $P$ be any $n \times n$ stochastic matrix (possibly reducible) and set $Q_T := \frac{1}{T} \sum_{t=0}^{T-1} P^t$. Let $\Delta_n$ be the set of all probability vectors, i.e. all $v \in \mathbb{R}^n$ such that $v_i \geq 0$ for all $i$ and $\sum_{i=1}^n v_i = 1$. For any vector $w \in \mathbb{R}^n$, let $\|w\|_1 := \sum_{i=1}^n |w_i|$. Given $v \in \Delta_n$ and $T > 0$, we define $v_T := vQ_T$. Then

$$ \|v_T(I - P)\|_1 = \frac{\|v(I - P^T)\|_1}{T} \leq \frac{2}{T}, $$

so any subsequential limit point $\pi$ of the sequence $\{v_T\}_{T=1}^\infty$ satisfies $\pi = \pi P$. Because the set $\Delta_n \subset \mathbb{R}^n$ is closed and bounded, such a subsequential limit point $\pi$ exists.

Since $\pi$ satisfies $\pi = \pi P$, it also satisfies $\pi = \pi P^t$ for any non-negative integer $t$, i.e., $\pi(y) = \sum_{x \in \mathcal{X}} \pi(x)P^t(x, y)$. Thus if $\pi(x) > 0$ and $P^t(x, y) > 0$, then $\pi(y) > 0$. Thus if $P$ is irreducible and there exists $x$ with $\pi(x) > 0$, then all $y \in \mathcal{X}$ satisfy $\pi(y) > 0$. One such $x$ exists because $\sum_{x \in \mathcal{X}} \pi(x) = 1$.

We now show that in fact the sequence $\{v_T\}$ converges.

With $I - P$ acting on row vectors in $\mathbb{R}^n$ by multiplication from the right, we claim that the kernel and the image of $I - P$ intersect only in 0. Indeed, if $z = w(I - P)$ satisfies $z = zP$, then $z = zQ_T = \frac{1}{T}w(I - P^T)$ must satisfy $\|z\|_1 \leq 2\|w\|_1/T$ for every $T$, so necessarily $z = 0$. Since the dimensions of $\text{Im}(I - P)$ and $\text{Ker}(I - P)$ add up to $n$, it follows that any vector $v \in \mathbb{R}^n$ has a unique representation

$$ v = u + w, \quad \text{with } u \in \text{Im}(I - P) \text{ and } w \in \text{Ker}(I - P). \tag{1.37} $$

Therefore $v_T = vQ_T = uQ_T + w$ , so writing $u = x(I - P)$ we conclude that $\|v_T - \pi\|_1 \leq 2\|x\|_1/T$. If $v \in \Delta_n$ then also $w \in \Delta_n$ due to $w$ being the limit of $v_T$. Thus we can take $\pi = w$. $\blacksquare$

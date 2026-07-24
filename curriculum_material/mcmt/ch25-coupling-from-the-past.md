# Chapter 25 — Coupling from the Past
*(PDF pages 364–374; book pages 348–358)*

### PDF page 364 (book page 348)

CHAPTER 25

# Coupling from the Past

by James G. Propp and David B. Wilson

J.G. Propp (left) and D.B. Wilson (right). *[Figure: photograph of two men standing side by side in front of a colorful abstract painting.]*

**25.1. Introduction**

In Markov chain Monte Carlo studies, one attempts to sample from a probability distribution $\pi$ by running a Markov chain whose unique stationary distribution is $\pi$. Ideally, one has proved a theorem that guarantees that the time for which one plans to run the chain is substantially greater than the mixing time of the chain, so that the distribution $\tilde{\pi}$ that one's procedure actually samples from is known to be close to the desired $\pi$ in variation distance. More often, one merely hopes that this is the case, and the possibility that one's samples are contaminated with substantial initialization bias cannot be ruled out with complete confidence.

The "coupling from the past" (CFTP) procedure introduced by **Propp and Wilson (1996)** provides one way of getting around this problem. Where it is applicable, this method determines on its own how long to run and delivers samples that are governed by $\pi$ itself, rather than $\tilde{\pi}$. Many researchers have found ways to apply the basic idea in a wide variety of settings (see `http://dbwilson.com/exact/` for pointers to this research). Our aim here is to explain the basic method and to give a few of its applications.

It is worth stressing at the outset that CFTP is especially valuable as an alternative to standard Markov chain Monte Carlo when one is working with Markov chains for which one suspects, but has not proved, that rapid mixing occurs. In such cases, the availability of CFTP makes it less urgent that theoreticians obtain bounds on the mixing time, since CFTP (unlike Markov chain Monte Carlo) cleanly separates the issue of efficiency from the issue of quality of output. That is

_______________
Copyright 2008 by James G. Propp and David B. Wilson.

### PDF page 365 (book page 349)

to say, one's samples are guaranteed to be uncontaminated by initialization bias, regardless of how quickly or slowly they are generated.

Before proceeding, we mention that there are other algorithms that may be used for generating perfect samples from the stationary distribution of a Markov chain, including Fill's algorithm (**Fill, 1998**; **Fill, Machida, Murdoch, and Rosenthal, 2000**), "dominated CFTP" (**Kendall and Møller, 2000**), "read-once CFTP" (**Wilson, 2000b**), and the "randomness recycler" (**Fill and Huber, 2000**). Each of these has its merits, but since CFTP is conceptually the simplest of these, it is the one that we shall focus our attention on here.

As a historical aside, we mention that the conceptual ingredients of CFTP were in the air even before the versatility of the method was made clear in **Propp and Wilson (1996)**. Precursors include **Letac (1986)**, **Thorisson (1988)**, and **Borovkov and Foss (1992)**. Even back in the 1970's, one can find foreshadowings in the work of Ted Harris (on the contact process, the exclusion model, random stirrings, and coalescing and annihilating random walks), David Griffeath (on additive and cancellative interacting particle systems), and Richard Arratia (on coalescing Brownian motion). One can even see traces of the idea in the work of **Loynes (1962)** forty-five years ago. See also the survey by **Diaconis and Freedman (1999)**.

**25.2. Monotone CFTP**

The basic idea of coupling from the past is quite simple. Suppose that there is an ergodic Markov chain that has been running either forever or for a very long time, long enough for the Markov chain to have reached (or very nearly reached) its stationary distribution. Then the state that the Markov chain is currently in is a sample from the stationary distribution. If we can figure out what that state is, by looking at the recent randomizing operations of the Markov chain, then we have a sample from its stationary distribution. To illustrate these ideas, we show how to apply them to the Ising model of magnetism (introduced in Section 3.3.5 and studied further in Chapter 15).

Recall that an Ising system consists of a collection of $n$ interacting spins, possibly in the presence of an external field. Each spin may be aligned up or down. Spins that are close to each other prefer to be aligned in the same direction, and all spins prefer to be aligned with the external magnetic field (which sometimes varies from site to site). These preferences are quantified in the total energy $H$ of the system

$$ H(\sigma) = -\sum_{i<j} \alpha_{i,j}\sigma_i\sigma_j - \sum_i B_i\sigma_i, $$

where $B_i$ is the strength of the external field as measured at site $i$, $\sigma_i$ is 1 if spin $i$ is aligned up and $-1$ if it is aligned down, and $\alpha_{i,j} \geq 0$ represents the interaction strength between spins $i$ and $j$. The probability of a given spin configuration is given by $Z^{-1}\exp[-\beta H(\sigma)]$ where $\beta$ is the "inverse temperature" and $Z$ is the "partition function," i.e., the normalizing constant that makes the probabilities add up to 1. Often the $n$ spins are arranged in a two-dimensional or three-dimensional lattice, and $\alpha_{i,j} = 1$ if spins $i$ and $j$ are adjacent in the lattice, and $\alpha_{i,j} = 0$ otherwise. The Ising model has been used to model certain substances such as crystals of FeCl$_2$ and FeCO$_3$ and certain phases of carbon dioxide, xenon, and brass — see **Baxter (1982)** for further background.

### PDF page 366 (book page 350)

**FIGURE 25.1.** The Ising model at three different temperatures (below, at, and above the "critical" temperature). Here the spins lie at the vertices of the triangular lattice and are shown as black or white hexagons. The spins along the upper boundaries were forced to be black and the spins along lower boundaries were forced to be white (using an infinite magnetic field on these boundary spins). *[Figure: three diamond-shaped (rhombus) arrays of hexagonal spins. Left — mostly black in the upper region and white in the lower region with a jagged interface (below critical). Middle — larger intermingled black and white clusters (at critical). Right — a finely speckled salt-and-pepper mix of black and white throughout (above critical).]*

We may use the single-site heat bath algorithm, also known as Glauber dynamics, to sample Ising spin configurations. (Glauber dynamics was introduced in Section 3.3.) A single move of the heat-bath algorithm may be summarized by a pair of numbers $(i, u)$, where $i$ represents a spin site (say that $i$ is a uniformly random site), and $u$ is a uniformly random real number between 0 and 1. The heat-bath algorithm randomizes the alignment of spin $i$, holding all of the remaining magnets fixed, and uses the number $u$ when deciding whether the new spin should be up or down. There are two possible choices for the next state, denoted by $\sigma_\uparrow$ and $\sigma_\downarrow$. We have $\Pr[\sigma_\uparrow]/\Pr[\sigma_\downarrow] = e^{-\beta(H(\sigma_\uparrow)-H(\sigma_\downarrow))} = e^{-\beta(\Delta H)}$. The update rule is that the new spin at site $i$ is up if $u < \Pr[\sigma_\uparrow]/(\Pr[\sigma_\uparrow]+\Pr[\sigma_\downarrow])$, and otherwise the new spin is down. It is easy to check that this defines an ergodic Markov chain with the desired stationary distribution.

Recall our supposition that the randomizing process, in this case the single-site heat bath, has been running for all time. Suppose that someone has recorded all the randomizing operations of the heat bath up until the present time. They have not recorded what the actual spin configurations or Markov chain transitions are, but merely which sites were updated and which random number was used to update the spin at the given site. Given this recorded information, our goal is to determine the state of the Markov chain at the present time (time 0), since, as we have already determined, this state is a sample from the stationary distribution of the Markov chain.

To determine the state at time 0, we make use of a natural partial order with which the Ising model is equipped: we say that two spin-configurations $\sigma$ and $\tau$

### PDF page 367 (book page 351)

satisfy $\sigma \preceq \tau$ when each spin-up site in $\sigma$ is also spin-up in $\tau$. Notice that if $\sigma \preceq \tau$ and we update both $\sigma$ and $\tau$ with the same heat-bath update operation $(i, u)$, then because site $i$ has at least as many spin-up neighbors in $\tau$ as it does in $\sigma$ and because of our assumption that the $\alpha_{i,j}$'s are nonnegative, we have $\Pr[\tau_\uparrow]/\Pr[\tau_\downarrow] \geq \Pr[\sigma_\uparrow]/\Pr[\sigma_\downarrow]$, and so the updated states $\sigma'$ and $\tau'$ also satisfy $\sigma' \preceq \tau'$. (We say that the randomizing operation respects the partial order $\preceq$.) Notice also that the partial order $\preceq$ has a maximum state $\hat{1}$, which is spin-up at every site, and a minimum state $\hat{0}$, which is spin-down at every site.

This partial order enables us to obtain upper and lower bounds on the state at the present time. We can look at the last $T$ randomizing operations, figure out what would happen if the Markov chain were in state $\hat{1}$ at time $-T$, and determine where it would be at time 0. Since the Markov chain is guaranteed to be in a state which is $\preceq \hat{1}$ at time $-T$ and since the randomizing operations respect the partial order, we obtain an upper bound on the state at time 0. Similarly we can obtain a lower bound on the state at time 0 by applying the last $T$ randomizing operations to the state $\hat{0}$. It could be that we are lucky and the upper and lower bounds are equal, in which case we have determined the state at time 0. If we are not so lucky, we could look further back in time, say at the last $2T$ randomizing operations, and obtain better upper and lower bounds on the state at the present time. So long as the upper and lower bounds do not coincide, we can keep looking further and further back in time (see Figure 25.2). Because the Markov chain is ergodic, when it is started in $\hat{1}$ and $T$ is large enough, there is some positive chance that it will reach $\hat{0}$, after which the upper and lower bounds are guaranteed to coincide. In the limit as $T \to \infty$, the probability that the upper and lower bounds agree at time 0 tends to 1, so almost surely we eventually succeed in determining the state at time 0.

The randomizing operation (the heat-bath in the above Ising model example) defines a (grand) coupling of the Markov chain, also sometimes called a *stochastic flow,* since it couples Markov chains started from all the states in the state space. (Grand couplings were discussed in Section 5.4.) For CFTP, the choice of the

**FIGURE 25.2.** Illustration of CFTP in the monotone setting. Shown are the heights of the upper and lower trajectories started at various starting times in the past. When a given epoch is revisited later by the algorithm, it uses the same randomizing operation. *[Figure: a plot of several trajectory heights versus time (progressing left to right). At several starting epochs, pairs of upper trajectories descend from high values and lower trajectories rise from low values; between epochs the trajectories bunch together into a nearly-flat band near mid-height, illustrating coalescence of the upper and lower bounds.]*

### PDF page 368 (book page 352)

coupling is as important as the choice of the Markov chain. To illustrate this, we consider another example, tilings of a regular hexagon by lozenges, which are $60°/120°$ rhombuses (see Figure 25.3). The set of lozenge tilings comes equipped

**FIGURE 25.3.** Tilings of a regular hexagon by lozenges. Alternatively, these tilings may be viewed three-dimensionally, as a collection of little three-dimensional boxes sitting within a larger box. *[Figure: a regular hexagon tiled by three orientations of rhombus lozenges, giving the optical impression of a stack of unit cubes piled into the corner of a large three-dimensional box.]*

with a natural partial order $\preceq$: we say that one tiling lies below another tiling if, when we view the tilings as collections of little three-dimensional boxes contained within a large box, the first collection of boxes is a subset of the other collection of boxes. The minimum configuration $\hat{0}$ is just the empty collection of little boxes, and the maximum configuration $\hat{1}$ is the full collection of little boxes.

A site in the tiling is just a vertex of one of the rhombuses that is contained within the interior of the hexagon. For each possible tiling, these sites form a triangular lattice. If a site is surrounded by exactly three lozenges, then the three lozenges will have three different orientations, one of which is horizontal if the regular hexagon is oriented as shown in Figure 25.3. There are two different ways for a site to be surrounded by three lozenges — the horizontal lozenge will lie either above the site or below it. One possible randomizing operation would with probability $1/2$ do nothing and with probability $1/2$ pick a uniformly random site in the tiling, and if that site is surrounded by three lozenges, rearrange those three lozenges. Another possible randomizing operation would pick a site uniformly at random and then if the site is surrounded by three lozenges, with probability $1/2$ arrange the three lozenges so that the horizontal one is below the site and with probability $1/2$ arrange them so that the horizontal lozenge is above the site. When

### PDF page 369 (book page 353)

the tiling is viewed as a collection of boxes, this second randomizing operation either tries to remove or add (with probability 1/2 each) a little box whose projection into the plane of the tiling is at the site. These attempts to add or remove a little box only succeed when the resulting configuration of little boxes would be stable under gravity; otherwise the randomizing operation leaves the configuration alone. It is straightforward to check that both of these randomizing operations give rise to the same Markov chain, i.e., a given tiling can be updated according to the first randomizing operation or the second randomizing operation, and either way, the distribution of the resulting tiling will be precisely the same. However, for purposes of CFTP the second randomizing operation is much better, because it respects the partial order $\preceq$, whereas the first randomizing operation does not.

With the Ising model and tiling examples in mind, we give pseudocode for "monotone CFTP," which is CFTP when applied to state spaces with a partial order $\preceq$ (with a top state $\hat{1}$ and bottom state $\hat{0}$) that is preserved by the randomizing operation:

$$
\begin{aligned}
&T \leftarrow 1 \\
&\texttt{repeat} \\
&\qquad \text{upper} \leftarrow \hat{1} \\
&\qquad \text{lower} \leftarrow \hat{0} \\
&\qquad \texttt{for } t = -T \texttt{ to } -1 \\
&\qquad\qquad \text{upper} \leftarrow \varphi(\text{upper}, U_t) \\
&\qquad\qquad \text{lower} \leftarrow \varphi(\text{lower}, U_t) \\
&\qquad T \leftarrow 2T \\
&\texttt{until } \text{upper} = \text{lower} \\
&\texttt{return } \text{upper}
\end{aligned}
$$

Here the variables $U_t$ represent the intrinsic randomness used in the randomizing operations. In the Ising model heat-bath example above, $U_t$ consists of a random number representing a site together with a random real number between 0 and 1. In the tiling example, $U_t$ consists of the random site together with the outcome of a coin toss. The procedure $\varphi$ deterministically updates a state according to the random variable $U_t$.

Recall that we are imagining that the randomizing operation has been going on for all time, that someone has recorded the random variables $U_t$ that drive the randomizing operations, and that our goal is to determine the state at time 0. Clearly if we read the random variable $U_t$ more than one time, it would have the same value both times. Therefore, when the random mapping $\varphi(\cdot, U_t)$ is used in one iteration of the repeat loop, for any particular value of $t$, it is essential that the same mapping be used in all subsequent iterations of the loop. We may accomplish this by storing the $U_t$'s; alternatively, if (as is typically the case) our $U_t$'s are given by some pseudo-random number generator, we may simply suitably reset the random number generator to some specified seed $seed(i)$ each time $t$ equals $-2^i$.

REMARK 25.1. Many people ask about different variations of the above procedure, such as what happens if we couple into the future or what happens if we use fresh randomness each time we need to refer to the random variable $U_t$. There is a simple example that rules out the correctness of all such variations that have been suggested. Consider the state space $\{1, 2, 3\}$, where the randomizing operation with probability 1/2 increments the current state by 1 (unless the state is 3) and with probability 1/2 decrements the current state by 1 (unless the state is 1). We leave it as an exercise to verify that this example rules out the correctness of the above two

### PDF page 370 (book page 354)

variants. There are in fact other ways to obtain samples from the stationary distribution of a monotone Markov chain, such as by using Fill's algorithm (**Fill, 1998**) or "read-once CFTP" (**Wilson, 2000b**), but these are not the sort of procedures that one will discover by randomly mutating the above procedure.

It is worth noting that monotone CFTP is efficient whenever the underlying Markov chain is rapidly mixing. **Propp and Wilson (1996)** proved that the number of randomizing operations that monotone CFTP performs before returning a sample is at least $t_{\text{mix}}$ and at most $O(t_{\text{mix}} \log H)$, where $t_{\text{mix}}$ is the mixing time of the Markov chain when measured with the total variation distance and $H$ denotes the length of the longest totally ordered chain of states between $\hat{0}$ and $\hat{1}$.

There are a surprisingly large number of Markov chains for which monotone CFTP may be used (see **Propp and Wilson (1996)** and other articles listed in <http://dbwilson.com/exact/>). In the remainder of this chapter we describe a variety of scenarios in which CFTP has been used even when monotone CFTP cannot be used.

### **25.3. Perfect Sampling via Coupling from the Past**

Computationally, one needs three things in order to be able to implement the CFTP strategy: a way of generating (and representing) certain maps from the state space $\Omega$ to itself; a way of composing these maps; and a way of ascertaining whether *total coalescence* has occurred, i.e., a way of ascertaining whether a certain composite map (obtained by composing many random maps) collapses all of $\Omega$ to a single element.

The first component is what we call the random map procedure; we model it as an oracle that on successive calls returns independent, identically distributed functions $f$ from $\Omega$ to $\Omega$, governed by some selected probability distribution $P$ (typically supported on a very small subset of the set of all maps from $\Omega$ to itself). We use the oracle to choose independent, identically distributed maps $f_{-1}$, $f_{-2}$, $f_{-3}, \ldots, f_{-T}$, where how far into the past we have to go ($T$ steps) is determined during run-time itself. (In the notation of the previous section, $f_t(x) = \varphi(x, U_t)$. These random maps are also known as grand couplings, which were discussed in Section 5.4.) The defining property that $T$ must have is that the composite map

$$
F_{-T}^0 \stackrel{\text{def}}{=} f_{-1} \circ f_{-2} \circ f_{-3} \circ \cdots \circ f_{-T}
$$

must be collapsing. Finding such a $T$ thus requires that we have both a way of composing $f$'s and a way of testing when such a composition is collapsing. (Having the test enables one to find such a $T$, since one can iteratively test ever-larger values of $T$, say by successive doubling, until one finds a $T$ that works. Such a $T$ will be a random variable that is measurable with respect to $f_{-T}, f_{-T+1}, \ldots, f_{-1}$.)

Once a suitable $T$ has been found, the algorithm outputs $F_{-T}^0(x)$ for any $x \in \Omega$ (the result will not depend on $x$, since $F_{-T}^0$ is collapsing). We call this output the CFTP sample. It must be stressed that when one is attempting to determine a usable $T$ by guessing successively larger values and testing them in turn, one must use the *same* respective maps $f_i$ during each test. That is, if we have just tried starting the chain from time $-T_1$ and failed to achieve coalescence, then, as we proceed to try starting the chain from time $-T_2 < -T_1$, we must use the same maps $f_{-T_1}, f_{-T_1+1}, \ldots, f_{-1}$ as in the preceding attempt. This procedure is summarized below:

### PDF page 371 (book page 355)

$$
\begin{aligned}
&T \leftarrow 1 \\
&\texttt{while } f_{-1} \circ \cdots \circ f_{-T} \text{ is not totally coalescent} \\
&\qquad \text{increase } T \\
&\texttt{return } \text{the value to which } f_{-1} \circ \cdots \circ f_{-T} \text{ collapses } \Omega
\end{aligned}
$$

Note that the details of how one increases $T$ affect the computational efficiency of the procedure but not the distribution of the output; in most applications it is most natural to double $T$ when increasing it (as in Sections 25.2 and 25.4), but sometimes it is more natural to increment $T$ when increasing it (as in Section 25.5).

As long as the nature of $P$ guarantees (almost sure) eventual coalescence, and as long as $P$ bears a suitable relationship to the distribution $\pi$, the CFTP sample will be distributed according to $\pi$. Specifically, it is required that $P$ preserve $\pi$ in the sense that if a random state $x$ is chosen in accordance with $\pi$ and a random map $f$ is chosen in accordance with $P$, then the state $f(x)$ will be distributed in accordance with $\pi$. In the next several sections we give examples.

### **25.4. The Hardcore Model**

Recall from Section 3.3.4 that the states of the hardcore model are given by subsets of the vertex set of a finite graph $G$, or equivalently, by $0, 1$-valued functions on the vertex set. We think of 1 and 0 as respectively denoting the presence or absence of a particle. In a legal state, no two adjacent vertices may both be occupied by particles. The probability of a particular legal state is proportional to $\lambda^m$, where $m$ is the number of particles (which depends on the choice of state) and $\lambda$ is some fixed parameter value. We denote this probability distribution by $\pi$. That is, $\pi(\sigma) = \lambda^{|\sigma|}/Z$ where $\sigma$ is a state, $|\sigma|$ is the number of particles in that state, and $Z = \sum_\sigma \lambda^{|\sigma|}$. Figure 25.4 shows some hardcore states for different values of $\lambda$ when the graph $G$ is the toroidal grid.

The natural single-site heat-bath Markov chain for hardcore states would pick a site at random, forget whether or not there is a particle at that site, and then place a particle at the site with probability $\lambda/(\lambda + 1)$ if there are no neighboring particles or with probability 0 if there is a neighboring particle.

For general (non-bipartite) graphs $G$ there is no monotone structure which would allow one to use monotone CFTP. But **Häggström and Nelander (1999)** and **Huber (1998)** proposed the following scheme for using CFTP with the single-site heat-bath Markov chain. One can associate with each *set* of hardcore states a three-valued function on the vertex set, where the value "1" means that all states in the set are known to have a particle at that vertex, the value "0" means that all states in the set are known to have a vacancy at that vertex, and the value "?" means that it is possible that some of the states in the set have a particle there while others have a vacancy. Initially we place a "?" at every site since the Markov chain could be in any state. We can operate directly on this three-valued state-model by means of simple rules that mimic the single-site heat-bath. The randomizing operation picks a random site and proposes to place a particle there with probability $\lambda/(\lambda + 1)$ or proposes to place a vacancy there with probability $1/(\lambda + 1)$. Any proposal to place a vacancy always succeeds for any state in the current set, so in this case a "0" is placed at the site. A proposal to place a particle at the site succeeds only if no neighboring site has a particle, so in this case we place a "1" if all neighboring sites have a "0", and otherwise we place a "?" at the site since the proposal to place a particle there may succeed for some states

### PDF page 372 (book page 356)

**FIGURE 25.4.** Hardcore model on the $40 \times 40$ square grid with periodic boundary conditions, for different values of $\lambda$. Particles are shown as diamonds, and the constraint that no two particles are adjacent is equivalent to the constraint that no two diamonds overlap. Particles on the even sublattice (where the $x$-coordinate and $y$-coordinate have the same parity) are shown in dark gray, and particles on the odd sublattice are shown in light gray. There is a critical value of $\lambda$ above which the hardcore model typically has a majority of particles on one of these two sublattices. CFTP generates random samples for values of $\lambda$ beyond those for which Glauber dynamics is currently known to be rapidly mixing. *[Figure: a 2 × 3 array of square panels, each showing a 40 × 40 grid configuration of the hardcore model. Particles are drawn as small diamonds, colored dark (blue) for the even sublattice and light (orange) for the odd sublattice. The panels are labeled, left to right in the top row, $\lambda = 0.5$, $\lambda = 1$, $\lambda = 2$, and in the bottom row, $\lambda = 3$, $\lambda = 4$, $\lambda = 5$. As $\lambda$ increases the configurations become denser and increasingly dominated by a single sublattice color: the $\lambda = 4$ panel is mostly light and the $\lambda = 5$ panel is mostly dark.]*

in the set and fail for other states. After the update, the "0, 1, ?" configuration describes any possible state that the Markov chain may be in after the single-site heat-bath operation. It is immediate that if the "0, 1, ?" Markov chain, starting from the all-?'s state, ever reaches a state in which there are no ?'s, then the single-site heat-bath chain, using the same random proposals, maps all initial states into the same final state. Hence we might want to call the "0, 1, ?" Markov chain the "certification chain," for it tells us when the stochastic flow of primary interest has achieved coalescence.

One might fear that it would take a long time for the certification chain to certify coalescence, but Häggström and Nelander (1999) show that the number of ?'s tends to shrink to zero exponentially fast provided $\lambda < 1/\Delta$, where $\Delta$ is the maximum degree of the graph. Recall from Theorem 5.9 that the Glauber dynamics Markov chain is rapidly mixing when $\lambda < 1/(\Delta - 1)$ — having the number of ?'s shrink to zero rapidly is a stronger condition than rapid mixing. The best

### PDF page 373 (book page 357)

current bounds for general graphs is that Glauber dynamics is rapidly mixing if $\lambda \le 2/(\Delta - 2)$ (**Vigoda, 2001**; **Dyer and Greenhill, 2000**). For particular graphs of interest, such as the square lattice, in practice the number of ?'s shrinks to zero rapidly for values of $\lambda$ much larger than what these bounds guarantee. Such observations constitute empirical evidence in favor of rapid mixing for larger $\lambda$'s.

**25.5. Random State of an Unknown Markov Chain**

Now we come to a problem that in a sense encompasses all the cases we have discussed so far: the problem of sampling from the stationary distribution $\pi$ of a general Markov chain. Of course, in the absence of further strictures this problem admits a trivial "solution": just solve for the stationary distribution analytically! In the case of the systems studied in Sections 25.2 and 25.4, this is not practical, since the state spaces are large. We now consider what happens if the state space is small but the analytic method of simulation is barred by imposing the constraint that the transition probabilities of the Markov chain are unknown: one merely has access to a black box that simulates the transitions.

It might seem that, under this stipulation, no solution to the problem is possible, but in fact a solution was found by **Asmussen, Glynn, and Thorisson (1992)**. However, their algorithm was not very efficient. Subsequently **Aldous (1995)** and **Lovász and Winkler (1995a)** found faster procedures (although the algorithm of Aldous involves controlled but non-zero error). The CFTP-based solution given below is even faster than that of Lovász and Winkler.

For pictorial concreteness, we envision the Markov chain as a biased random walk on some directed graph $G$ whose arcs are labeled with weights, where the transition probabilities from a given vertex are proportional to the weights of the associated arcs (as in the preceding section). We denote the vertex set of $G$ by $\Omega$, and denote the stationary distribution on $\Omega$ by $\pi$. **Propp and Wilson (1998)** give a CFTP-based algorithm that lets one sample from this distribution $\pi$.

Our goal is to define suitable random maps from $\Omega$ to $\Omega$ in which many states are mapped into a single state. We might therefore define a random map from $\Omega$ to itself by starting at some fixed vertex $r$, walking randomly for some large number $T$ of steps, and mapping all states in $\Omega$ to the particular state $v$ that one has arrived at after $T$ steps. However, $v$ is subject to initialization bias, so this random map procedure typically does not preserve $\pi$ in the sense defined in Section 25.3.

What actually works is a multi-phase scheme of the following sort: start at some vertex $r$ and take a random walk for a *random* amount of time $T_1$, ending at some state $v$; then map every state that has been visited during that walk to $v$. In the second phase, continue walking from $v$ for a further random amount of time $T_2$, ending at some new state $v'$; then map every state that was visited during the second phase but not the first to $v'$. In the third phase, walk from $v'$ for a random time to a new state $v''$, and map every hitherto-unvisited state that was visited during that phase to the state $v''$, and so on. Eventually, every state gets visited, and every state gets mapped to some state. Such maps are easy to compose, and it is easy to recognize when such a composition is coalescent (it maps every state to one particular state).

There are two constraints that our random durations $T_1$, $T_2$, ... must satisfy if we are planning to use this scheme for CFTP. (For convenience we will assume henceforth that the $T_i$'s are i.i.d.) First, the distribution of each $T_i$ should have the

### PDF page 374 (book page 358)

property that, at any point during the walk, the (conditional) expected time until the walk terminates does not depend on where one is or how one got there. This ensures that the stochastic flow determined by these random maps preserves $\pi$. Second, the time for the walk should be neither so short that only a few states get visited by the time the walk ends nor so long that generating even a single random map takes more time than an experimenter is willing to wait. Ideally, the expected duration of the walk should be on the order of the cover time for the random walk. **Propp and Wilson (1998)** show that by using the random walk itself to estimate its own cover time, one gets an algorithm that generates a random state distributed according to $\pi$ in expected time $\leq 15$ times the cover time.

At the beginning of this section, we said that one has access to a black box that simulates the transitions. This is, strictly speaking, ambiguous: does the black box have an “input port” so that we can ask it for a random transition from a specified state? Or are we merely passively observing a Markov chain in which we have no power to intervene? This ambiguity gives rise to two different versions of the problem, of separate interest. Our CFTP algorithm works for both of them.

For the “passive” version of the problem, it is not hard to show that no scheme can work in expected time less than the expected cover time of the walk, so in this setting our algorithm runs in time that is within a constant factor of optimal. It is possible to do better in the active setting, but no good lower bounds are currently known for this case.

**Exercise**

**EXERCISE 25.1.** Show that in the special case where the graph is bipartite, there is a natural partial order on the space of hardcore configurations that is preserved by Glauber dynamics and that in this case monotone CFTP and CFTP with the “0, 1, ?” Markov chain are equivalent.

**Notes**

This chapter is based in part on the expository article “Coupling from the Past: a User's Guide,” which appeared in *Microsurveys in Discrete Probability*, volume 41 of the *DIMACS Series in Discrete Mathematics and Computer Science*, published by the AMS, and contains excerpts from the article “Exact Sampling with Coupled Markov Chains and Applications to Statistical Mechanics,” which appeared in *Random Structures and Algorithms*, volume 9(1&2):223–252, 1996.

For more on perfectly sampling the spanning trees of a graph, see **Anantharam and Tsoucas (1989)**, **Broder (1989)**, and **Aldous (1990)**. For more examples of perfect sampling, see **Häggström and Nelander (1998)**, **Wilson (2000a)**, and the webpage **Wilson (2004b)**.

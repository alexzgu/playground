# Chapter 26 — Open Problems
*(PDF pages 375–378; book pages 359–362)*

### PDF page 375 (book page 359)

CHAPTER 26

# Open Problems

This list of questions is not meant to be either novel or comprehensive. The selection of topics clearly reflects the interests of the authors. **Aldous and Fill (1999)** features open problems throughout the book; several have already been solved. We hope this list will be similarly inspirational. We have included updates to problems listed in the first edition.

**26.1. The Ising Model**

For all of these problems, assume Glauber dynamics is considered unless another transition mechanism is specified.

QUESTION 1 (Positive boundary conditions). Consider the Ising model on the $n \times n$ grid with all plus boundary conditions. Show that at any temperature, the mixing time is at most polynomial in $n$. An upper bound on the relaxation time of $e^{n^{1/2+\varepsilon}}$ was obtained by Martinelli (**1994**). The best upper bounds for $d \geq 3$ were obtained by Sugimine (**2002**).

**Update: Lubetzky, Martinelli, Sly, and Toninelli (2013)** obtain an upper bound of $n^{c \log n}$ at low temperature in dimension 2.

QUESTION 2 (Monotonicity). Is the spectral gap of the Ising model on a graph $G$ monotone increasing in temperature? Is the spectral gap of the Ising model monotone decreasing in the addition of edges?

There is a common generalization of these two questions to the ferromagnetic Ising model with inhomogeneous interaction strengths. If for simplicity we absorb the temperature into the interaction strengths, the Gibbs distribution for this model can be defined by

$$ \mu(\sigma) = \frac{1}{Z} \exp\left( \sum_{\{u,v\} \in E(G)} J_{u,v} \sigma(u) \sigma(v) \right), $$

where $J_{u,v} > 0$ for all edges $\{u, v\}$. In this model, is it true that on any graph the spectral gap is monotone decreasing in each interaction strength $J_{u,v}$? **Nacu (2003)** proved this stronger conjecture for the cycle.

Even more generally, we may ask whether for a fixed graph and fixed $t$ the distance $\bar{d}(t)$ is monotone increasing in the individual interaction strengths $J_{u,v}$. (Corollary 12.7 and Lemma 4.10 ensure that this is, in fact, a generalization.)

QUESTION 3 (Systematic updates vs. random updates). Fix a permutation $\alpha$ of the vertices of an $n$-vertex graph and successively perform Glauber updates at

### PDF page 376 (book page 360)

$\alpha(1), \ldots, \alpha(n)$. Call the transition matrix of the resulting operation $P_\alpha$. That is, $P_\alpha$ corresponds to doing a full sweep of all the vertices. Let $P$ be the transition matrix of ordinary Glauber dynamics.

(i) Does there exist a constant $C$ such that

$$ n t_{\mathrm{mix}}(P_\alpha) \leq C t_{\mathrm{mix}}(P)? $$

(ii) Does there exist a constant $c$ such that

$$ n t_{\mathrm{mix}}(P_\alpha) \geq c \frac{t_{\mathrm{mix}}(P)}{\log n}? $$

Although theorems are generally proved about random updates, in practice systematic updates are often used for running simulations. (Note that at infinite temperature, a single systematic sweep suffices.) See Dyer, Goldberg, and Jerrum (**2006a**) and (**2006b**) for analysis of systematic swap algorithms for colorings.

QUESTION 4 (Ising on transitive graphs). For the Ising model on transitive graphs, is the relaxation time of order $n$ if and only if the mixing time is of order $n \log n$ (as the temperature varies)? This is known to be true for the two-dimensional torus. See **Martinelli (1999)** for more on what is known on lattices.

**26.2. Cutoff**

QUESTION 5 (Transitive graphs of bounded degree). Given a sequence of transitive graphs of degree $\Delta \geq 3$ where the spectral gap is bounded away from zero, must the family of lazy random walks on these graphs have a cutoff?

QUESTION 6 (Card shuffling). Do the following shuffling chains on $n$ cards have cutoff? All are known to have pre-cutoff.

(a) Cyclic-to-random transpositions (see **Mossel, Peres, and Sinclair (2004)**).
(b) Random-to-random insertions. In this shuffle, a card is chosen uniformly at random, removed from the deck, and reinserted into a uniform random position. The other cards retain their original relative order. **Subag (2013)** proved a lower bound of $(3/4 + o(1))(n \log(n))$. Upper bounds of the same order were proved by **Uyemura-Reyes (2002)**, **Saloff-Coste and Zúñiga (2008)** and **Morris and Qin (2014)**.
(c) Card-cyclic to random shuffle (see **Morris, Ning, and Peres (2014)**).

**26.3. Other Problems**

QUESTION 7. Does Glauber dynamics for proper colorings mix in time order $n \log n$ if the number of colors is bigger than $\Delta + 2$, where $\Delta$ bounds the graph degrees? This is known to be polynomial for $q > (11/6)\Delta$—see the Notes to Chapter 14.

### PDF page 377 (book page 361)

QUESTION 8. For lazy simple random walk on a transitive graph $G$ with vertex degree $\Delta$, does there exist a universal constant $c$ such that the mixing time is at most $c \cdot \Delta \cdot \mathrm{diam}^2(G)$? Recall that an upper bound of this order for the relaxation time was proved in Theorem 13.26.

QUESTION 9. Consider the group $GL_n(\mathbb{Z}_2)$ of $n \times n$ invertible matrices with entries in $\mathbb{Z}_2$. Select distinct $i, j$ from $\{1, \ldots, n\}$ (uniformly among all $n(n-1)$ ordered pairs) and add the $i$th row to the $j$th row modulo 2. This chain can be viewed as simple random walk on a graph of degree $n(n-1)$ with order $2^n$ nodes, and this implies the mixing time is at least $cn^2/(\log n)$ for some constant $c$. **Diaconis and Saloff-Coste (1996c)** proved an upper bound of $O(n^4)$ for the mixing time. **Kassabov (2005)** proved the relaxation time for this chain is of order $n$, which yields an improved upper bound of $O(n^3)$ for the mixing time. What is the correct exponent?

**26.4. Update: Previously Open Problems**

Many of the open problems posed in the first edition are now solved.

PREVIOUSLY OPEN PROBLEM 3. (Lower bounds for mixing of Ising) Is it true that on an $n$-vertex graph, the mixing time for the Glauber dynamics for Ising is at least $cn \log n$? This is known for bounded degree families (the constant depends on the maximum degree); see **Hayes and Sinclair (2007)**. We conjecture that on any graph, at any temperature, there is a lower bound of $(1/2 + o(1))n \log n$ on the mixing time.

**Update: Ding and Peres (2011)** prove a lower bound of $(1/4)n \log n$ in their published paper. Subsequently the authors discovered a proof of the $(1/2)n \log n$ lower bound, which is included in arXiv:0909.5162v2

PREVIOUSLY OPEN PROBLEM 4. (Block dynamics vs. single site dynamics) Consider block dynamics for the Ising model on a family of finite graphs. If the block sizes are bounded, are mixing times always comparable for block dynamics and single site dynamics? This is true for the relaxation times, via comparison of Dirichlet forms.

**Update: Peres and Winkler (2013)** show this for monotone systems when started from the all plus configuration, for some block dynamics. This remains open for other spin systems, e.g. Potts model.

PREVIOUSLY OPEN PROBLEM 8.[Cutoff for Ising on transitive graphs] Consider the Ising model on a transitive graph, e.g. a $d$-dimensional torus, at high temperature. Is there a cutoff whenever the mixing time is of order $n \log n$? Is this true, in particular, for the cycle? **Levin, Luczak, and Peres (2010)** showed that the answer is "yes" for the complete graph.

**Updates:** This question has been answered for tori by Lubetzky and Sly (**2013**, **2014a**, **2016**, **2014b**). For general graphs of bounded degree, cutoff at high temperature was established in **Lubetzky and Sly (2014b)**.

### PDF page 378 (book page 362)

PREVIOUSLY OPEN PROBLEM 9(A).(Cutoff for random adjacent transpositions).

**Update:** Lacoin (2016a) shows that random adjacent transpositions on the segment has both total-variation and separation cutoff.

PREVIOUSLY OPEN PROBLEM 10.(Lamplighter on tori) Does the lamplighter on tori of dimension $d \geq 3$ have a cutoff? If there is a total variation cutoff, at what multiple of the cover time of the torus does it occur?

**Update:** Miller and Peres (2012) have shown that there is a cutoff at $(1/2)t_{\mathrm{cov}}$.

PREVIOUSLY OPEN PROBLEM 11. Let $(X_t^{(n)})$ denote a family of irreducible reversible Markov chains, either in continuous-time or in lazy discrete-time. Is it true that there is cutoff *in separation distance* if and only if there is cutoff *in total variation distance*? That this is true for birth-and-death chains follows from combining results in Ding, Lubetzky, and Peres (2010a) and Diaconis and Saloff-Coste (2006). **Update:** For general reversible chains, there is no implication between cutoff in separation and cutoff in total variation. See Hermon, Lacoin, and Peres (2016).

PREVIOUSLY OPEN PROBLEM 12. Place a pebble at each vertex of a graph $G$, and on each edge place an alarm clock that rings at each point of a Poisson process with density 1. When the clock on edge $\{u, v\}$ rings, interchange the pebbles at $u$ and $v$. This process is called the *interchange process* on $G$. Handjani and Jungreis (1996) showed that for trees, the interchange process on $G$ and the continuous-time simple random walk on $G$ have the same spectral gap. Is this true for all graphs? This question was raised by Aldous and Diaconis.

**Update:** This problem was resolved in the affirmative by Caputo, Liggett, and Richthammer (2010). The mixing time is studied in Jonasson (2012).

PREVIOUSLY OPEN PROBLEM 14. (Gaussian elimination chain) Consider the group of $n \times n$ upper triangular matrices with entries in $\mathbb{Z}_2$. Select $k$ uniformly from $\{2, \ldots, n\}$ and add the $k$-th row to the $(k-1)$-st row. The last column of the resulting matrices form a copy of the East model chain. Hence the lower bound of order $n^2$ for the East model (Theorem 7.16) is also a lower bound for the Gaussian elimination chain. Diaconis (personal communication) informed us he has obtained an upper bound of order $n^4$. What is the correct exponent?

**Update:** Peres and Sly (2013) prove an upper bound of $O(n^2)$, which matches the order of the mixing time for a single column. It is an open problem to prove cutoff for this chain. Cutoff for any finite collection of columns was proved by Ganguly and Martinelli (2016).

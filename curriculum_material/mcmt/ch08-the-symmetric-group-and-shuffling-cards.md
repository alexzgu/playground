# Chapter 8 — The Symmetric Group and Shuffling Cards
*(PDF pages 116–131; book pages 100–115)*

### PDF page 116 (book page 100)

CHAPTER 8

# The Symmetric Group and Shuffling Cards

> ...to destroy all organization far more shuffling is necessary than one would naturally suppose; I learned this from experience during a period of addiction, and have since compared notes with others.
>
> —**Littlewood (1948)**.

We introduced the top-to-random shuffle in Section 6.1 and gave upper and lower bounds on its mixing time in Sections 6.5.3 and Section 7.4.1, respectively. Here we describe a general mathematical model for shuffling mechanisms and study two natural methods of shuffling cards.

We will return in Chapter 16 to the subject of shuffling, armed with techniques developed in intervening chapters. While games of chance have motivated probabilists from the founding of the field, there are several other motivations for studying card shuffling: these Markov chains are of intrinsic mathematical interest, they model important physical processes in which the positions of particles are interchanged, and they can also serve as simplified models for large-scale mutations—see Section 16.2.

**8.1. The Symmetric Group**

A permutation of $\{1, 2, \ldots, n\}$ is a bijection from $\{1, 2, \ldots, n\}$ to itself. The set of all permutations forms a group, the symmetric group $\mathcal{S}_n$, under the composition operation. The identity element of $\mathcal{S}_n$ is the identity function $\mathrm{id}(k) = k$. Every $\sigma \in \mathcal{S}_n$ has a well-defined inverse function, which is its inverse in the group.

A probability distribution $\mu$ on the symmetric group describes a mechanism for shuffling cards: apply permutation $\sigma$ to the deck with probability $\mu(\sigma)$. Repeatedly shuffling the deck using this mechanism is equivalent to running the random walk on the group with increment distribution $\mu$. As discussed in Section 2.6, as long as the support of $\mu$ generates all of $\mathcal{S}_n$, the resulting chain is irreducible. If $\mu(\mathrm{id}) > 0$, then it is aperiodic. Every shuffle chain has uniform stationary distribution.

We will consider a permutation as a map from positions to labels. For example the permutation

| $i$ | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|
| $\sigma(i)$ | 3 | 1 | 2 | 4 |

corresponds to placing card 3 into position 1, card 1 into position 2, card 2 into position 3, and card 4 into position 4.

**8.1.1. Cycle notation.** We will often find it convenient to use ***cycle notation*** for permutations. In this notation, $(abc)$ refers to the permutation $\sigma$ for which $b = \sigma(a)$, $c = \sigma(b)$, and $a = \sigma(c)$. When several cycles are written consecutively,

### PDF page 117 (book page 101)

they are performed one at a time, *from right to left* (as is consistent with ordinary function composition). For example,

$$ (13)(12) = (123) \tag{8.1} $$

and

$$ (12)(23)(34)(23)(12) = (14). $$

A cycle of length $n$ is called an $n$-cycle. A ***transposition*** is a 2-cycle.

In card language, (8.1) corresponds to first exchanging the top and second cards and then interchanging the top and third cards. The result is to send the top card to the second position, the second card to the third position, and the third card to the top of the deck.

Every permutation can be written as a product of disjoint cycles. Fixed points correspond to 1-cycles, which are generally omitted from the notation.

**8.1.2. Generating random permutations.** We describe a simple algorithm for generating an *exactly* uniform random permutation. Let $\sigma_0$ be the identity permutation. For $k = 1, 2, \ldots, n-1$ inductively construct $\sigma_k$ from $\sigma_{k-1}$ by swapping the cards at locations $k$ and $J_k$, where $J_k$ is an integer picked uniformly in $\{k, \ldots, n\}$, independently of $\{J_1, \ldots, J_{k-1}\}$. More precisely,

$$ \sigma_k(i) = \begin{cases} \sigma_{k-1}(i) & \text{if } i \neq J_k,\ i \neq k, \\ \sigma_{k-1}(J_k) & \text{if } i = k, \\ \sigma_{k-1}(k) & \text{if } i = J_k. \end{cases} \tag{8.2} $$

That is, $\sigma_k = \sigma_{k-1} \circ (k\, J_k)$. Exercise 8.1 asks you to prove that this generates a uniformly chosen element of $\mathcal{S}_n$.

This method requires $n-1$ steps, which is optimal; see Exercise 8.2. However, this is not how any human being shuffles cards! In Section 8.3 we will examine a model which comes closer to modeling actual human shuffles.

**8.1.3. Parity of permutations.** Given a permutation $\sigma \in \mathcal{S}_n$, consider the sign of the product

$$ M(\sigma) = \prod_{1 \leq i < j \leq n} (\sigma(j) - \sigma(i)) \,. $$

Clearly $M(\mathrm{id}) > 0$, since every term is positive. For every $\sigma \in \mathcal{S}_n$ and every transposition $(ab)$, we have

$$ M(\sigma \circ (ab)) = -M(\sigma). $$

Why? We may assume that $a < b$. Then for every $c$ such that $a < c < b$, two factors change sign (the one that pairs $c$ with $a$ and also the one that pairs $c$ with $b$), while the single factor containing both $a$ and $b$ also changes sign.

Call a permutation $\sigma$ ***even*** if $M(\sigma) > 0$, and otherwise call $\sigma$ ***odd***. Note that a permutation is even (odd) if and only if every way of writing it as a product of transpositions contains an even (odd) number of factors. The set of all even permutations in $\mathcal{S}_n$ forms a subgroup, known as the ***alternating group*** $A_n$.

Note that an $m$-cycle can be written as a product of $m-1$ transpositions:

$$ (a_1 a_2 \ldots a_m) = (a_1 a_2)(a_2 a_3) \ldots (a_{m-1} a_m). $$

Hence an $m$-cycle is odd (even) when $m$ is even (odd), and the sign of any permutation is determined by its disjoint cycle decomposition.

### PDF page 118 (book page 102)

EXAMPLE 8.1 (Random 3-cycles). Let $T$ be the set of all three-cycles in $\mathcal{S}_n$, and let $\mu$ be uniform on $T$. The set $T$ does *not* generate all of $\mathcal{S}_n$, since every permutation in $T$ is even. Hence the random walk with increments $\mu$ is not irreducible. (See Exercise 8.3.)

EXAMPLE 8.2 (Random transpositions, first version). Let $T \subseteq \mathcal{S}_n$ be the set of all transpositions and let $\mu$ be the uniform probability distribution on $T$. In Section 8.1.2, we gave a method for generating a uniform random permutation that started with the identity permutation and used only transpositions. Hence $\langle T \rangle = \mathcal{S}_n$, and our random walk is irreducible.

Every element of the support of $\mu$ is odd. Hence, if this walk is started at the identity, after an even number of steps, its position must be an even permutation. After an odd number of steps, its position must be odd. Hence the walk is periodic.

REMARK 8.3. Periodicity occurs in random walks on groups when the entire support of the increment distribution falls into a single coset of some subgroup. Fortunately, there is a simple way to ensure aperiodicity. If the probability distribution $\mu$ on a group $G$ satisfies $\mu(\mathrm{id}) > 0$, then the random walk with increment distribution $\mu$ is aperiodic, since $\gcd\{t \,:\, P^t(g,g) > 0\} = 1$.

**8.2. Random Transpositions**

To avoid periodicity, the random transposition shuffle is defined as follows: At time $t$, choose two cards, labelled $L_t$ and $R_t$, independently and uniformly at random. If $L_t$ and $R_t$ are different, transpose them. Otherwise, do nothing. The resulting distribution $\mu$ satisfies

$$ \mu(\sigma) = \begin{cases} 1/n & \text{if } \sigma = \mathrm{id}, \\ 2/n^2 & \text{if } \sigma = (ij), \\ 0 & \text{otherwise.} \end{cases} \tag{8.3} $$

As in Example 8.2, this chain is irreducible; aperiodicity follows from Remark 8.3.

Consider the random transposition shuffle started from id. The expected number of fixed points of a uniformly chosen permutation equals 1. However, any card which has not been selected by time $t$ is a fixed point of the permutation obtained at that time. Therefore, a coupon collector argument suggests that the mixing time is at least $(1/2)n \log n$, as two cards are touched in each step. This argument is formalized in Section 8.2.1.

In fact, as **Diaconis and Shahshahani (1981)** proved, the random transpositions shuffle satisfies, for all $\varepsilon > 0$,

$$ t_{\mathrm{mix}}(\varepsilon) = \left( \frac{1}{2} + o(1) \right) n \log n \quad \text{as } n \to \infty \,. $$

They use Fourier analysis on the symmetric group to establish this sharp result, which is an example of the *cutoff phenomenon* (see Chapter 18). In Section 8.2.2, we present two upper bounds on the mixing time: a simple $O(n^2)$ bound via coupling, and an $O(n \log n)$ bound using a strong stationary time.

**8.2.1. Lower bound.**

### PDF page 119 (book page 103)

PROPOSITION 8.4. *Let $0 < \varepsilon < 1$. For the random transposition chain on an $n$-card deck,*

$$ t_{\mathrm{mix}}(\varepsilon) \geq \frac{n-1}{2} \log \left( \frac{1-\varepsilon}{6} n \right) . $$

PROOF. It is well known (and easily proved using indicators) that the expected number of fixed points in a uniform random permutation in $\mathcal{S}_n$ is 1, regardless of the value of $n$.

Let $F(\sigma)$ denote the number of fixed points of the permutation $\sigma$. If $\sigma$ is obtained from the identity by applying $t$ random transpositions, then $F(\sigma)$ is at least as large as the number of cards that were touched by none of the transpositions—no such card has moved, and some moved cards may have returned to their original positions.

Our shuffle chain determines transpositions by choosing pairs of cards independently and uniformly at random. Hence, after $t$ shuffles, the number of untouched cards has the same distribution as the number $R_{2t}$ of uncollected coupon types after $2t$ steps of the coupon collector chain. By Lemma 7.13,

$$ \mu := \mathbf{E}(R_{2t}) = n \left( 1 - \frac{1}{n} \right)^{2t} , $$

and $\mathrm{Var}(R_{2t}) \leq \mu$. Let $A = \{\sigma \,:\, F(\sigma) \geq \mu/2\}$. We will compare the probabilities of $A$ under the uniform distribution $\pi$ and $P^t(\mathrm{id}, \cdot)$. First,

$$ \pi(A) \leq \frac{2}{\mu}, $$

by Markov's inequality. By Chebyshev's inequality,

$$ P^t(\mathrm{id}, A^c) \leq \mathbf{P}\left\{ R_{2t} \leq \mu/2 \right\} \leq \frac{\mu}{(\mu/2)^2} = \frac{4}{\mu}. $$

By the definition (4.1) of total variation distance, we have

$$ \left\| P^t(\mathrm{id}, \cdot) - \pi \right\|_{\mathrm{TV}} \geq 1 - \frac{6}{\mu}. $$

We want to find how small $t$ must be so that $1 - 6/\mu > \varepsilon$, or equivalently,

$$ n \left( 1 - \frac{1}{n} \right)^{2t} = \mu > \frac{6}{1-\varepsilon}. $$

The above holds if and only if

$$ \log \left( \frac{n(1-\varepsilon)}{6} \right) > 2t \log \left( \frac{n}{n-1} \right) . \tag{8.4} $$

Using the inequality $\log(1+x) < x$, we have $\log \left( \frac{n}{n-1} \right) < \frac{1}{n-1}$, so the inequality (8.4) holds provided that

$$ \log \left( \frac{n(1-\varepsilon)}{6} \right) \geq \frac{2t}{n-1}. $$

That is, if $t \leq \frac{n-1}{2} \log \left( \frac{n(1-\varepsilon)}{6} \right)$, then $d(t) \geq 1 - 6/\mu > \varepsilon$. $\blacksquare$

### PDF page 120 (book page 104)

Aligning one card:

$$ \begin{matrix} 2 & 4 & 1 & 3 \\ 3 & 1 & 4 & 2 \end{matrix} \implies \begin{matrix} 1 & 4 & 2 & 3 \\ 1 & 3 & 4 & 2 \end{matrix} $$

Aligning two cards:

$$ \begin{matrix} 2 & 3 & 1 & 4 \\ 3 & 1 & 4 & 2 \end{matrix} \implies \begin{matrix} 1 & 3 & 2 & 4 \\ 1 & 3 & 4 & 2 \end{matrix} $$

Aligning three cards:

$$ \begin{matrix} 2 & 3 & 1 \\ 3 & 1 & 2 \end{matrix} \implies \begin{matrix} 1 & 3 & 2 \\ 1 & 3 & 2 \end{matrix} $$

FIGURE 8.1. Aligning cards using coupled random transpositions. In each example, $X_t = 1$ and $Y_t = 1$, so card 1 is transposed with the card in position 1 in both decks.

*[Figure: three worked examples, each showing a pair of two-row card arrangements (top row = one deck, bottom row = the other deck) transformed by an arrow into a new pair, illustrating how one coupled transposition can align one, two, or three cards between the decks.]*

**8.2.2. Upper bound via coupling.** For the coupling, we take a slightly different view of generating the transpositions. At each time $t$, the shuffler chooses a card with label $X_t \in [n]$ and, independently, a position $Y_t \in [n]$; she then transposes the card labelled $X_t$ with the card in position $Y_t$. Of course, if the card in position $Y_t$ already has the label $X_t$, the deck is left unchanged. Hence this mechanism generates the distribution described in (8.3).

To couple two decks, use the same choices $(X_t)$ and $(Y_t)$ to shuffle both. Let $(\sigma_t)$ and $(\sigma'_t)$ be the two trajectories. What can happen in one step? Let $a_t$ be the number of cards that occupy the same position in both $\sigma_t$ and $\sigma'_t$.

- If the card labelled $X_t$ is in the same position in both decks, then $a_{t+1} = a_t$.
- If $X_t$ is in different positions in the two decks but position $Y_t$ is occupied by the same card, then performing the specified transposition breaks one alignment but also forms a new one. We have $a_{t+1} = a_t$.
- If $X_t$ is in different positions in the two decks and if the cards at position $Y_t$ in the two decks do not match, then at least one new alignment is made—and possibly as many as three. See Figure 8.1.

PROPOSITION 8.5. *Let $\tau$ be the time required for the two decks to coincide. Then, no matter the initial configurations of the two decks, $\mathbf{E}(\tau) < \frac{\pi^2}{6} n^2$.*

PROOF. Decompose

$$ \tau = \tau_1 + \cdots + \tau_n, $$

where $\tau_i$ is the number of transpositions between the first time that $a_t$ is greater than or equal to $i - 1$ and the first time that $a_t$ is greater than or equal to $i$. (Since $a_0$ can be greater than 0 and since $a_t$ can increase by more than 1 in a single transposition, it is possible that many of the $\tau_i$'s are equal to 0.)

When $t$ satisfies $a_t = i$, there are $n - i$ unaligned cards and the probability of increasing the number of alignments is $(n-i)^2/n^2$, since the shuffler must choose a non-aligned card and a non-aligned position. In this situation $\tau_{i+1}$ is a geometric random variable with success probability $(n-i)^2/n^2$. We may conclude that under

### PDF page 121 (book page 105)

these circumstances
$$ \mathbf{E}(\tau_{i+1}|a_t = i) = n^2/(n-i)^2. $$
When no value of $t$ satisfies $a_t = i$, then $\tau_{i+1} = 0$. Hence
$$ \mathbf{E}(\tau) < n^2 \sum_{i=0}^{n-1} \frac{1}{(n-i)^2} < n^2 \sum_{l=1}^{\infty} \frac{1}{l^2}. $$

$\blacksquare$

Markov's inequality and Corollary 5.5 now give an $O(n^2)$ bound on $t_{\mathrm{mix}}$. However, the strong stationary time we are about to discuss does much better.

**8.2.3. Upper bound via strong stationary time.**

PROPOSITION 8.6. *In the random transposition shuffle, let $R_t$ and $L_t$ be the cards chosen by the right and left hands, respectively, at time $t$. Assume that when $t = 0$, no cards have been marked. At time $t$, mark card $R_t$ if both of the following are true:*

- *$R_t$ is unmarked.*
- *Either $L_t$ is a marked card or $L_t = R_t$.*

*Let $\tau$ be the time when every card has been marked. Then $\tau$ is a strong stationary time for this chain.*

Here is a heuristic explanation for why the scheme described above should give a strong stationary time. One way to generate a uniform random permutation is to build a stack of cards, one at a time, inserting each card into a uniformly random position relative to the cards already in the stack. For the stopping time described above, the marked cards are carrying out such a process.

PROOF. It is clear that $\tau$ is a stopping time. To show that it is a strong stationary time, we prove the following subclaim by induction on $t$. Let $V_t \subseteq [n]$ be the set of cards marked at or before time $t$, and let $U_t \subseteq [n]$ be the set of positions occupied by $V_t$ after the $t$-th transposition. We claim that *given $t$, $V_t$, and $U_t$, all possible permutations of the cards in $V_t$ on the positions $U_t$ are equally likely.*

This is clearly true when $t = 1$ (and continues to be true as long as at most one card has been marked).

Now, assume that the subclaim is true for $t$. The shuffler chooses cards $L_{t+1}$ and $R_{t+1}$.

- If no new card is marked, then $V_{t+1} = V_t$. This can happen in three ways:
  - The cards $L_{t+1}$ and $R_{t+1}$ are different and both are unmarked. Then $V_{t+1}$ and $U_{t+1}$ are identical to $V_t$ and $U_t$, respectively.
  - If $L_{t+1}$ and $R_{t+1}$ were both marked at an earlier round, then $U_{t+1} = U_t$ and the shuffler applies a uniform random transposition to the cards in $V_t$. All permutations of $V_t$ remain equiprobable.
  - Otherwise, $L_{t+1}$ is unmarked and $R_{t+1}$ was marked at an earlier round. To obtain the position set $U_{t+1}$, we delete the position (at time $t$) of $R_{t+1}$ and add the position (at time $t$) of $L_{t+1}$. For a fixed set $U_t$, all choices of $R_{t+1} \in U_t$ are equally likely, as are all permutations of $V_t$ on $U_t$. Hence, once the positions added and deleted are specified, all permutations of $V_t$ on $U_{t+1}$ are equally likely.

### PDF page 122 (book page 106)

- If the card $R_{t+1}$ gets marked, then $L_{t+1}$ is equally likely to be any element of $V_{t+1} = V_t \cup \{R_{t+1}\}$, while $U_{t+1}$ consists of $U_t$ along with the position of $R_{t+1}$ (at time $t$). Specifying the permutation of $V_t$ on $U_t$ and the card $L_{t+1}$ uniquely determines the permutation of $V_{t+1}$ on $U_{t+1}$. Hence all such permutations are equally likely.

In every case, the collection of all permutations of the cards $V_t$ on a specified set $U_t$ together make equal contributions to all possible permutations of $V_{t+1}$ on $U_{t+1}$. Hence, to conclude that all possible permutations of a fixed $V_{t+1}$ on a fixed $U_{t+1}$ are equally likely, we simply sum over all possible preceding configurations. $\blacksquare$

REMARK 8.7. In the preceding proof, the two subcases of the inductive step for which no new card is marked are essentially the same as checking that the uniform distribution is stationary for the random transposition shuffle and the random-to-top shuffle, respectively.

REMARK 8.8. As Diaconis (1988a) points out, for random transpositions some simple card-marking rules fail to give strong stationary times. See Exercise 8.9.

LEMMA 8.9. *The stopping time $\tau$ defined in Proposition 8.6 satisfies*
$$ \mathbf{E}(\tau) = 2n(\log n + O(1)) $$
*and*
$$ \mathrm{Var}(\tau) = O(n^2). $$

PROOF. As for the coupon collector time, we can decompose
$$ \tau = \tau_0 + \cdots + \tau_{n-1}, $$
where $\tau_k$ is the number of transpositions after the $k$-th card is marked, up to and including when the $(k+1)$-st card is marked. The rules specified in Proposition 8.6 imply that $\tau_k$ is a geometric random variable with success probability $\frac{(k+1)(n-k)}{n^2}$ and that the $\tau_i$'s are independent of each other. Hence
$$ \mathbf{E}(\tau) = \sum_{k=0}^{n-1} \frac{n^2}{(k+1)(n-k)}. $$
Substituting the partial fraction decomposition
$$ \frac{1}{(k+1)(n-k)} = \frac{1}{n+1} \left( \frac{1}{k+1} + \frac{1}{n-k} \right) $$
and recalling that
$$ \sum_{j=1}^{n} \frac{1}{j} = \log n + O(1) $$
(see Exercise 2.4) completes the estimate.

Now, for the variance. We can immediately write
$$ \mathrm{Var}(\tau) = \sum_{k=0}^{n-1} \frac{1 - \frac{(k+1)(n-k)}{n^2}}{\left( \frac{(k+1)(n-k)}{n^2} \right)^2} < \sum_{k=0}^{n-1} \frac{n^4}{(k+1)^2(n-k)^2}. $$

### PDF page 123 (book page 107)

Split the sum into two pieces:
$$ \mathrm{Var}(\tau) < \sum_{0 \le k < n/2} \frac{n^4}{(k+1)^2(n-k)^2} + \sum_{n/2 \le k < n} \frac{n^4}{(k+1)^2(n-k)^2} $$
$$ < \frac{2n^4}{(n/2)^2} \sum_{0 \le k \le n/2} \frac{1}{(k+1)^2} = O(n^2). $$

$\blacksquare$

COROLLARY 8.10. *For the random transposition chain on an $n$-card deck,*
$$ t_{\mathrm{mix}} \le (2 + o(1))n \log n. $$

PROOF. Let $\tau$ be the Broder stopping time defined in Proposition 8.6, and let $t_0 = \mathbf{E}(\tau) + 2\sqrt{\mathrm{Var}(\tau)}$. By Chebyshev's inequality,
$$ \mathbf{P}\{\tau > t_0\} \le \frac{1}{4}. $$
Lemma 8.9 and Proposition 6.11 now imply the desired inequality. $\blacksquare$

**8.3. Riffle Shuffles**

A method often used to shuffle real decks of 52 cards is the following: first, the shuffler cuts the decks into two piles. Then, the piles are "riffled" together: she successively drops cards from the bottom of each pile to form a new pile. There are two undetermined aspects of this procedure. First, the numbers of cards in each pile after the initial cut can vary. Second, real shufflers drop varying numbers of cards from each stack as the deck is reassembled.

For mathematicians, there is a tractable mathematical model for riffle shuffling. Here are three ways to shuffle a deck of $n$ cards:

(1) Let $M$ be a Binomial$(n, 1/2)$ random variable, and split the deck into its top $M$ cards and its bottom $n - M$ cards. There are $\binom{n}{M}$ ways to riffle these two piles together, preserving the relative order within each pile (first select the positions for the top $M$ cards; then fill in both piles). Choose one of these arrangements uniformly at random.

(2) Let $M$ be a Binomial$(n, 1/2)$ random variable, and split the deck into its top $M$ cards and its bottom $n - M$ cards. The two piles are then held over the table and cards are dropped one by one, forming a single pile once more, according to the following recipe: if at a particular moment, the left pile contains $a$ cards and the right pile contains $b$ cards, then drop the card on the bottom of the left pile with probability $a/(a + b)$ and the card on the bottom of the right pile with probability $b/(a + b)$. Repeat this procedure until all cards have been dropped.

(3) Label the $n$ cards with $n$ independent fairly chosen bits. Pull all the cards labeled 0 to the top of the deck, preserving their relative order.

A ***rising sequence*** of a permutation $\sigma$ is a maximal set of consecutive values that occur in the correct relative order in $\sigma$. (For example, the final permutation in Figure 8.2 has 4 rising sequences: $(1, 2, 3, 4), (5, 6), (7, 8, 9, 10)$, and $(11, 12, 13)$.)

### PDF page 124 (book page 108)

*First, cut the deck:*

| 1 | 2 | 3 | 4 | 5 | 6 |  | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|----|----|----|----|

*Then riffle together.*

| 7 | 1 | 8 | 2 | 3 | 9 | 4 | 10 | 5 | 11 | 12 | 6 | 13 |
|---|---|---|---|---|---|---|----|---|----|----|---|----|

*Now, cut again:*

| 7 | 1 | 8 | 2 | 3 | 9 | 4 | 10 |  | 5 | 11 | 12 | 6 | 13 |
|---|---|---|---|---|---|---|----|---|---|----|----|---|----|

*Riffle again.*

| 5 | 7 | 1 | 8 | 11 | 12 | 2 | 6 | 3 | 13 | 9 | 4 | 10 |
|---|---|---|---|----|----|---|---|---|----|---|---|----|

FIGURE 8.2. Riffle shuffling a 13-card deck, twice.

We claim that *methods* (1) *and* (2) *generate the same distribution Q on permutations, where*

$$ Q(\sigma) = \begin{cases} (n+1)/2^n & \text{if } \sigma = \mathrm{id}, \\ 1/2^n & \text{if } \sigma \text{ has exactly two rising sequences,} \\ 0 & \text{otherwise.} \end{cases} \tag{8.5} $$

It should be clear that method (1) generates $Q$. Next we verify that method (2) also produces $Q$. Given $M$, let $a_i$ (respectively, $b_i$) be the size of the left (right) pile before the $i$-th card is dropped. The probability of a particular interleaving equals

$$ \prod_{i=1}^{n} \frac{c_i}{a_i + b_i} \,, \tag{8.6} $$

where $c_i$ equals $a_i$ or $b_i$ according to whether the $i$-th card comes from the left or right pile. Since $a_i + b_i = n + 1 - i$, the product of the denominators equals $n!$. The $c_i's$ due to the left pile enumerate $1, \ldots, M$, while those from the right pile enumerate $1, \ldots, n - M$. Thus, the product in (8.6) equals $1/\binom{n}{M}$.

Recall from Section 4.6 that for a distribution $R$ on $\mathcal{S}_n$, the **reverse distribution** $\widehat{R}$ satisfies $\widehat{R}(\rho) = R(\rho^{-1})$. We claim that *method* (3) *generates* $\widehat{Q}$. Why? The cards labeled 0 form one increasing sequence in $\rho^{-1}$, and the cards labeled 1 form the other. (Again, there are $n + 1$ ways to get the identity permutation, namely, all strings of the form $00 \ldots 011 \ldots 1$.) Alternatively, the number $M$ of cards labeled 0 has a Binomial$(n, 1/2)$ distribution, and given $M$, the locations of these cards are uniform among the $\binom{n}{M}$ possibilities. Thus, method (3) is indeed the reversal of method (1).

Thanks to Lemma 4.13 (which says that a random walk on a group and its inverse, both started from the identity, have the same distance from uniformity after the same number of steps), it will suffice to analyze method (3).

Consider repeated inverse riffle shuffles using method (3). For the first shuffle, each card is assigned a random bit, and all the 0's are pulled ahead of all the 1's. For the second shuffle, each card is again assigned a random bit, and all the 0's are pulled ahead of all the 1's. Considering both bits (and writing the second bit on the left), we see that cards labeled 00 precede those labeled 01, which precede those labeled 10, which precede those labeled 11 (see Figure 8.3). After $k$ shuffles, each

### PDF page 125 (book page 109)

*Initial order:*

| card | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|------|---|---|---|---|---|---|---|---|---|----|----|----|----|
| round 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| round 2 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |

*After one inverse riffle shuffle:*

| card | 2 | 3 | 7 | 9 | 12 | 13 | 1 | 4 | 5 | 6 | 8 | 10 | 11 |
|------|---|---|---|---|----|----|---|---|---|---|---|----|----|
| round 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| round 2 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |

*After two inverse riffle shuffles:*

| card | 3 | 9 | 12 | 1 | 5 | 10 | 2 | 7 | 13 | 4 | 6 | 8 | 11 |
|------|---|---|----|---|---|----|---|---|----|---|---|---|----|
| round 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| round 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

FIGURE 8.3. When inverse riffle shuffling, we first assign bits for each round, then sort bit by bit.

card will be labeled with a string of $k$ bits, and cards with different labels will be in lexicographic order (cards with the same label will be in their original relative order).

PROPOSITION 8.11. *Let $\tau$ be the number of inverse riffle shuffles required for all cards to have different bitstring labels. Then $\tau$ is a strong stationary time.*

PROOF. Condition on the event that $\tau = t$. Since the bitstrings are generated by independent fair coin flips, every possible assignment[^1] of strings of length $t$ to cards is equally likely. Since the labeling bitstrings are distinct, the permutation is fully determined by the labels. Hence the permutation of the cards at time $\tau$ is uniform, no matter the value of $\tau$. $\blacksquare$

Now we need only estimate the tail probabilities for the strong stationary time. However, our stopping time $\tau$ is an example of the birthday problem, with the slight twist that the number of "people" is fixed, and we wish to choose an appropriate power-of-two "year length" so that all the people will, with high probability, have different birthdays.

PROPOSITION 8.12. *For the riffle shuffle on an $n$-card deck, $t_{\mathrm{mix}} \leq 2 \log_2(4n/3)$ for sufficiently large $n$.*

PROOF. Consider inverse riffle shuffling an $n$-card deck and let $\tau$ be the stopping time defined in Proposition 8.11. If $\tau \leq t$, then different labels have been assigned to all $n$ cards after $t$ inverse riffle shuffles. Hence

$$ \mathbf{P}(\tau \leq t) = \prod_{k=0}^{n-1} \left( 1 - \frac{k}{2^t} \right), $$

[^1]: That is, all cards are assigned distinct strings, but if the last bit is removed from each string, then they are not all distinct.

### PDF page 126 (book page 110)

since there are $2^t$ possible labels. Let $t = 2 \log_2(n/c)$. Then $2^t = n^2/c^2$ and we have

$$ \log \prod_{k=0}^{n-1} \left( 1 - \frac{k}{2^t} \right) = -\sum_{k=0}^{n-1} \left( \frac{c^2 k}{n^2} + O\left( \frac{k}{n^2} \right)^2 \right) $$
$$ = -\frac{c^2 n(n-1)}{2n^2} + O\left( \frac{n^3}{n^4} \right) = -\frac{c^2}{2} + O\left( \frac{1}{n} \right). $$

Hence

$$ \lim_{n \to \infty} \frac{\mathbf{P}(\tau \leq t)}{e^{-c^2/2}} = 1. $$

Taking any value of $c$ such that $c < \sqrt{2 \log(4/3)} \approx 0.7585$ will give a bound on $t_{\mathrm{mix}} = t_{\mathrm{mix}}(1/4)$. A convenient value to use is $3/4$, which, combined with Proposition 6.11, gives the bound stated in the proposition. $\blacksquare$

Applying the counting bound in Section 7.1.1 gives a lower bound of logarithmic order on the mixing time for the riffle shuffle.

PROPOSITION 8.13. *Fix $0 < \varepsilon, \delta < 1$. Consider riffle shuffling an $n$-card deck. For sufficiently large $n$,*

$$ t_{\mathrm{mix}}(\varepsilon) \geq (1 - \delta) \log_2 n. \tag{8.7} $$

PROOF. There are at most $2^n$ possible states accessible in one step of the time-reversed chain, since we can generate a move using $n$ independent unbiased bits. Thus $\log_2 \Delta \leq n$, where $\Delta$ is the maximum out-degree defined in (7.1). The state space has size $n!$, and Stirling's formula shows that $\log_2 n! = [1 + o(1)]n \log_2 n$. Using these estimates in (7.2) shows that for all $\delta > 0$, if $n$ is sufficiently large then (8.7) holds. $\blacksquare$

**Exercises**

EXERCISE 8.1. Let $J_1, \ldots, J_{n-1}$ be independent integers, where $J_k$ is uniform on $\{k, k+1, \ldots, n\}$, and let $\sigma_{n-1}$ be the random permutation obtained by recursively applying (8.2). Show that $\sigma_{n-1}$ is uniformly distributed on $\mathcal{S}_n$.

EXERCISE 8.2. Show that the Cayley graph on the symmetric group determined by all transpositions has diameter $n - 1$.
*Hint:* Consider the identity and the cyclic permutation $\sigma = (12 \cdots n)$.

EXERCISE 8.3.
(a) Show that the alternating group $A_n \subseteq \mathcal{S}_n$ of even permutations has order $n!/2$.
(b) Consider the distribution $\mu$, uniform on the set of 3-cycles in $\mathcal{S}_n$, introduced in Example 8.1. Show that the random walk with increments $\mu$ is an irreducible and aperiodic chain when considered as a walk on $A_n$.

EXERCISE 8.4. The Sam Loyd "fifteen puzzle" is shown in Figure 8.4. It consists of 15 tiles, numbered with the values 1 through 15, sitting in a 4 by 4 grid; one space is left empty. The tiles are in order, except that tiles 14 and 15 have been switched. The only allowed moves are to slide a tile adjacent to the empty space into the empty space.

Is it possible, using only legal moves, to switch the positions of tiles 14 and 15, while leaving the rest of the tiles fixed?

### PDF page 127 (book page 111)

*[Figure: a 4×4 grid of tiles. Rows: (1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 15, 14, [blank]).]*

FIGURE 8.4. The "fifteen puzzle".

(a) Show that the answer is "no."
(b) Describe the set of all configurations of tiles that can be reached using only legal moves.

EXERCISE 8.5. Suppose that a random function $\sigma : [n] \to [n]$ is created by letting $\sigma(i)$ be a random element of $[n]$, independently for each $i = 1, \ldots, n$. If the resulting function $\sigma$ is a permutation, stop, and otherwise begin anew by generating a fresh random function. Use Stirling's formula to estimate the expected number of random functions generated up to and including the first permutation.

EXERCISE 8.6. Consider the following variation of our method for generating random permutations: let $\sigma_0$ be the identity permutation. For $k = 1, 2, \ldots, n$ inductively construct $\sigma_k$ from $\sigma_{k-1}$ by swapping the cards at locations $k$ and $J_k$, where $J_k$ is an integer picked uniformly in $[1, n]$, independently of previous picks.

For which values of $n$ does this variant procedure yield a uniform random permutation?

EXERCISE 8.7. True or false: let $Q$ be a distribution on $\mathcal{S}_n$ such that when $\sigma \in \mathcal{S}_n$ is chosen according to $Q$, we have

$$ \mathbf{P}\{\sigma(i) > \sigma(j)\} = 1/2 $$

for every $i, j \in [n]$. Then $Q$ is uniform on $\mathcal{S}_n$.

EXERCISE 8.8. **Kolata (January 9, 1990**) writes: "By saying that the deck is completely mixed after seven shuffles, Dr. Diaconis and Dr. Bayer mean that every arrangement of the 52 cards is equally likely or that any card is as likely to be in one place as in another."

True or false: let $Q$ be a distribution on $\mathcal{S}_n$ such that when $\sigma \in \mathcal{S}_n$ is chosen according to $Q$, we have

$$ \mathbf{P}\{\sigma(i) = j\} = 1/n $$

for every $i, j \in [n]$. Then $Q$ is uniform on $\mathcal{S}_n$.

EXERCISE 8.9. Consider the random transposition shuffle.

(a) Show that marking both cards of every transposition and proceeding until every card is marked does not yield a strong stationary time.
(b) Show that marking the right-hand card of every transposition and proceeding until every card is marked does not yield a strong stationary time.

EXERCISE 8.10. Here is a way to generalize the inverse riffle shuffle. Let $a$ be a positive integer. To perform an ***inverse $a$-shuffle***, assign independent uniform

### PDF page 128 (book page 112)

random digits chosen from $\{0, 1, \ldots, a - 1\}$ to each card. Then sort according to digit, preserving relative order for cards with the same digit. For example, if $a = 3$ and the digits assigned to cards are

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|----|----|----|
| 2 | 0 | 2 | 1 | 2 | 0 | 1 | 0 | 1 | 0  | 0  | 0  |

then the shuffle will give

$$ 2 \mid 6 \mid 8 \mid 10 \mid 11 \mid 12 \mid 4 \mid 7 \mid 9 \mid 1 \mid 3 \mid 5 \ . $$

(a) Let $a$ and $b$ be positive integers. Show that an inverse $a$-shuffle followed by an inverse $b$-shuffle is the same as an inverse $ab$-shuffle.
(b) Describe how to perform a *forward $a$-shuffle*, and show that its increment distribution gives weight $\binom{a+n-r}{n}/a^n$ to every $\sigma \in \mathcal{S}_n$ with exactly $r$ rising sequences. (This is a generalization of (8.5).)

REMARK 8.14. Exercise 8.10(b), due to **Bayer and Diaconis (1992**), is the key to numerically computing the total variation distance from stationarity. A permutation has $r$ rising sequences if and only if its inverse has $r - 1$ descents. The number of permutations in $\mathcal{S}_n$ with $r - 1$ descents is the ***Eulerian number*** $\left\langle {n \atop r-1} \right\rangle$. The Eulerian numbers satisfy a simple recursion (and are built into modern symbolic computation software); see p. 267 of **Graham, Knuth, and Patashnik (1994**) for details. It follows from Exercise 8.10 that the total variation distance from uniformity after $t$ Gilbert-Shannon-Reeds shuffles of an $n$-card deck is

$$ \sum_{r=1}^{n} \left\langle {n \atop r-1} \right\rangle \left| \frac{\binom{2^t+n-r}{n}}{2^{nt}} - \frac{1}{n!} \right| . $$

See Figure 8.5 for the values when $n = 52$ and $t \leq 12$.

**Notes**

See any undergraduate abstract algebra book, e.g. **Herstein (1975**) or Artin (**1991**), for more on the basic structure of the symmetric group $\mathcal{S}_n$.

**Thorp (1965**) proposed Exercise 8.6 as an "Elementary Problem" in the *American Mathematical Monthly*.

**Random transpositions.** The strong stationary time defined in Proposition 8.6 and used to prove the upper bound on the mixing time for random transpositions (Corollary 8.10) is due to A. Broder (see **Diaconis (1988a**)). This upper bound is off by a factor of 4. **Matthews (1988b**) gives an improved strong stationary time whose upper bound matches the lower bound. Here is how it works: again, let $R_t$ and $L_t$ be the cards chosen by the right and left hands, respectively, at time $t$. Assume that when $t = 0$, no cards have been marked. As long as at most $\lceil n/3 \rceil$ cards have been marked, use this rule: at time $t$, mark card $R_t$ if both $R_t$ and $L_t$ are unmarked. When $k > \lceil n/3 \rceil$ cards have been marked, the rule is more complicated. Let $l_1 < l_2 < \cdots < l_k$ be the marked cards, and enumerate the ordered pairs of marked cards in lexicographic order:

$$ (l_1, l_1), (l_1, l_2), \ldots, (l_1, l_k), (l_2, l_1), \ldots, (l_k, l_k). \tag{8.8} $$

### PDF page 129 (book page 113)

*[Figure: a scatterplot. The horizontal axis is labeled $1$ through $12$; the vertical axis has gridline labels $0.25$, $0.5$, $0.75$, $1$. Twelve points descend in an S-shaped curve: the first four sit at height $1$, then the values drop steadily toward near $0$ by $t = 12$.]*

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9237 | 0.6135 |

| 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|----|----|----|
| 0.3341 | 0.1672 | 0.0854 | 0.0429 | 0.0215 | 0.0108 |

FIGURE 8.5. The total variation distance from stationarity (with 4 digits of precision) after $t$ riffle shuffles of a 52-card deck, for $t = 1, \ldots, 12$.

Also list the unmarked cards in order: $u_1 < u_n < \cdots < u_{n-k}$. At time $t$, if there exists an $i$ such that $1 \leq i \leq n - k$ and one of the three conditions below is satisfied, then mark card $i$.

(i) $L_t = R_t = u_i$.
(ii) Either $L_t = u_i$ and $R_t$ is marked or $R_t = u_i$ and $L_t$ is marked.
(iii) The pair $(L_t, R_t)$ is identical to the $i$-th pair in the list (8.8) of pairs of marked cards.

(Note that at most one card can be marked per transposition; if case (iii) is invoked, the card marked may not be either of the selected cards.) Compared to the Broder time discussed earlier, this procedure marks cards much faster at the beginning and essentially twice as fast at the end. The analysis is similar in spirit to, but more complex than, that presented in Section 8.2.3.

**Semi-random transpositions.** Consider shuffling by transposing cards. However, we allow only one hand (the right) to choose a uniform random card. The left hand picks a card according to some other rule—perhaps deterministic, perhaps randomized—and the two cards are switched. Since only one of the two cards switched is fully random, it is reasonable to call examples of this type shuffles by ***semi-random transpositions***. (Note that for this type of shuffle, the distribution of allowed moves can depend on time.)

One particularly interesting variation first proposed by **Thorp (1965**) and mentioned as an open problem in **Aldous and Diaconis (1986**) is the ***cyclic-to-random*** shuffle: at step $t$, the left hand chooses card $t \pmod{n}$, the right hand chooses a uniform random card, and the two chosen cards are transposed. This chain has the property that every position is given a chance to be randomized once

### PDF page 130 (book page 114)

every $n$ steps. Might that speed randomization? Or does the reduced randomness slow it down? (Note: Exercise 8.6 is about the state of an $n$-card deck after $n$ rounds of cyclic-to-random transpositions.)

**Mironov (2002)** (who was interested in how many steps are needed to do a good job of initializing a standard cryptographic protocol) gives an $O(n \log n)$ upper bound, using a variation of Broder's stopping time for random transpositions. **Mossel, Peres, and Sinclair (2004)** prove a matching (to within a constant) lower bound. Furthermore, the same authors extend the stopping time argument to give an $O(n \log n)$ upper bound for *any* shuffle by semi-random transpositions. This bound was improved by **Ganapathy (2007)** and **Saloff-Coste and Zúñiga (2007)**.

**Riffle shuffles.** The most famous theorem in non-asymptotic Markov chain convergence is what is often, and perhaps unfortunately, called the "seven shuffles suffice" (for mixing a standard 52-card deck) result of **Bayer and Diaconis (1992)**, which was featured in the New York Times (**Kolata, January 9, 1990**). Many elementary expositions of the riffle shuffle have been written. Our account is in debt to **Aldous and Diaconis (1986)**, **Diaconis (1988a)**, and **Mann (1994)**.

The model for riffle shuffling that we have discussed was developed by Gilbert and Shannon at Bell Labs in the 1950's and later independently by Reeds. It is natural to ask whether the Gilbert-Shannon-Reeds (GSR) shuffle is a reasonable model for the way humans riffle cards together. **Diaconis (1988a)** reports that when he and Reeds both shuffled repeatedly, Reeds's shuffles had packet sizes that matched the GSR model well, while Diaconis's shuffles had more small packets. The difference is not surprising, since Diaconis is an expert card magician who can perform perfect shuffles—i.e., ones in which a single card is dropped at a time.

Far more is known about the GSR shuffle than we have discussed. Bayer and Diaconis (**1992**) derived the exact expression for the probability of any particular permutation after $t$ riffle shuffles discussed in Exercise 8.10 and showed that the riffle shuffle has a cutoff (in the sense we discuss in Chapter 18) when $t = \frac{3}{2} n \log n$. **Diaconis, McGrath, and Pitman (1995)** compute exact probabilities of various properties of the resulting permutations and draw beautiful connections with combinatorics and algebra. See **Diaconis (2003)** for a survey of mathematics that has grown out of the analysis of the riffle shuffle.

Is it in fact true that seven shuffles suffice to adequately randomize a 52-card deck? **Bayer and Diaconis (1992)** were the first to give explicit values for the total variation distance from stationarity after various numbers of shuffles; see Figure 8.5. After seven shuffles, the total variation distance from stationarity is approximately 0.3341. That is, after 7 riffle shuffles the probability of a given event can differ by as much as 0.3341 from its value under the uniform distribution. Indeed, Peter Doyle has described a simple solitaire game for which the probability of winning when playing with a uniform random deck is exactly $1/2$, but whose probability of winning with a deck that has been GSR shuffled 7 times from its standard order is 0.801 (as computed in **van Zuylen and Schalekamp (2004)**).

Ultimately, the question of how many shuffles suffice for a 52-card deck is one of opinion, not mathematical fact. However, there exists at least one game playable by human beings for which 7 shuffles clearly do not suffice. A more reasonable level of total variation distance might be around 1 percent, comparable to the

### PDF page 131 (book page 115)

house advantage in casino games. This threshold would suggest 11 or 12 as an appropriate number of shuffles.

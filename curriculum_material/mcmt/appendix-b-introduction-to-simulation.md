# Appendix B — Introduction to Simulation
*(PDF pages 391–405; book pages 375–389)*

### PDF page 391 (book page 375)

APPENDIX B

# Introduction to Simulation

**B.1. What Is Simulation?**

Let $X$ be a random unbiased bit:
$$ \mathbf{P}\{X = 0\} = \mathbf{P}\{X = 1\} = \frac{1}{2}. \tag{B.1} $$
If we assign the value 0 to the "heads" side of a coin and the value 1 to the "tails" side, we can generate a bit which has the same distribution as $X$ by tossing the coin.

Suppose now the bit is biased, so that
$$ \mathbf{P}\{X = 1\} = \frac{1}{4}, \qquad \mathbf{P}\{X = 0\} = \frac{3}{4}. \tag{B.2} $$
Again using only our (fair) coin toss, we are able to easily generate a bit with this distribution: toss the coin twice and assign the value 1 to the result HH and the value 0 to the other three outcomes. Since the coin cannot remember the result of the first toss when it is tossed for the second time, the tosses are independent and the probability of two heads is $1/4$. This recipe for generating observations of a random variable which has the same distribution (B.2) as $X$ is called a ***simulation*** of $X$.

Consider the random variable $U_n$ which is uniform on the finite set
$$ \left\{ 0, \frac{1}{2^n}, \frac{2}{2^n}, \ldots, \frac{2^n - 1}{2^n} \right\}. \tag{B.3} $$
This random variable is a discrete approximation to the uniform distribution on $[0, 1]$. If our only resource is the humble fair coin, we are still able to simulate $U_n$: toss the coin $n$ times to generate independent unbiased bits $X_1, X_2, \ldots, X_n$, and output the value
$$ \sum_{i=1}^{n} \frac{X_i}{2^i}. \tag{B.4} $$
This random variable has the uniform distribution on the set in (B.3). (See Exercise B.1.)

Consequently, a sequence of independent and unbiased bits can be used to simulate a random variable whose distribution is close to uniform on $[0, 1]$. A sufficient number of bits should be used to ensure that the error in the approximation is small enough for any needed application. A computer can store a real number only to finite precision, so if the value of the simulated variable is to be placed in computer memory, it will be rounded to some finite decimal approximation. With this in mind, the discrete variable in (B.4) will be just as useful as a variable uniform on the interval of real numbers $[0, 1]$.

### PDF page 392 (book page 376)

**B.2. Von Neumann Unbiasing***

Suppose you have available an i.i.d. vector of *biased bits*, $X_1, X_2, \ldots, X_n$. That is, each $X_k$ is a $\{0, 1\}$-valued random variable, with $\mathbf{P}\{X_k = 1\} = p \neq 1/2$. Furthermore, suppose that we do not know the value of $p$. Can we convert this random vector into a (possibly shorter) random vector of independent and *unbiased* bits?

This problem was considered by von Neumann (**1951**) in his work on early computers. He described the following procedure: divide the original sequence of bits into pairs, discard pairs having the same value, and for each discordant pair 01 or 10, take the first bit. An example of this procedure is shown in Figure B.1; the extracted bits are shown in the second row.

$$
\begin{array}{lccccccccccccc}
\text{original bits} & 00 & 11 & 01 & 01 & 10 & 00 & 10 & 10 & 11 & 10 & 01 & \cdots \\
\text{extracted unbiased} & \cdot & \cdot & 0 & 0 & 1 & \cdot & 1 & 1 & \cdot & 1 & 0 & \cdots \\
\text{discarded bits} & 0 & 1 & \cdot & \cdot & \cdot & 0 & \cdot & \cdot & 1 & \cdot & \cdot & \cdots \\
\text{XORed bits} & 0 & 0 & 1 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1 & \cdots
\end{array}
\tag{B.5}
$$

**FIGURE B.1.** Extracting unbiased bits from biased bit stream.

*[Figure: a table with four labeled rows — "original bits", "extracted unbiased", "discarded bits", and "XORed bits" — showing how the von Neumann procedure transforms a stream of bit-pairs.]*

Note that the number $L$ of unbiased bits produced from $(X_1, \ldots, X_n)$ is itself a random variable. We denote by $(Y_1, \ldots, Y_L)$ the vector of extracted bits.

It is clear from symmetry that applying von Neumann's procedure to a bitstring $(X_1, \ldots, X_n)$ produces a bitstring $(Y_1, \ldots, Y_L)$ of random length $L$, which conditioned on $L = m$ is uniformly distributed on $\{0, 1\}^m$. In particular, the bits of $(Y_1, \ldots, Y_L)$ are uniformly distributed and independent of each other.

How efficient is this method? For any algorithm for extracting random bits, let $N(n)$ be the number of fair bits generated using the first $n$ of the original bits. The efficiency is measured by the asymptotic ***rate***
$$ r(p) := \limsup_{n \to \infty} \frac{\mathbf{E}(N)}{n}. \tag{B.6} $$
Let $q := 1 - p$. For the von Neumann algorithm, each pair of bits has probability $2pq$ of contributing an extracted bit. Hence $\mathbf{E}(N(n)) = 2 \left\lfloor \frac{n}{2} \right\rfloor pq$ and the efficiency is $r(p) = pq$.

The von Neumann algorithm throws out many of the original bits. These bits still contain some unexploited randomness. By converting the discarded 00's and 11's to 0's and 1's, we obtain a new vector $Z = (Z_1, Z_2, \ldots, Z_{\lfloor n/2 - L \rfloor})$ of bits. In the example shown in Figure B.1, these bits are shown on the third line.

Conditioned on $L = m$, the string $Y = (Y_1, \ldots, Y_L)$ and the string $Z = (Z_1, \ldots, Z_{\lfloor n/2 - L \rfloor})$ are independent, and the bits $Z_1, \ldots, Z_{\lfloor n/2 - L \rfloor}$ are independent of each other. The probability that $Z_i = 1$ is $p' = p^2/(p^2 + q^2)$. We can apply the von Neumann procedure again on the independent bits $Z$. Given that $L = m$, the expected number of fair bits we can extract from $Z$ is
$$ (\text{length of } Z) p' q' = \left\lfloor \frac{n}{2} - m \right\rfloor \left( \frac{p^2}{p^2 + q^2} \right) \left( \frac{q^2}{p^2 + q^2} \right). \tag{B.7} $$

### PDF page 393 (book page 377)

Since $\mathbf{E}L = 2 \left\lfloor \frac{n}{2} \right\rfloor pq$, the expected number of extracted bits is

$$ (n + O(1))[(1/2) - pq] \left( \frac{p^2}{p^2 + q^2} \right) \left( \frac{q^2}{p^2 + q^2} \right). \tag{B.8} $$

Adding these bits to the original extracted bits yields a rate for the modified algorithm of

$$ pq + [(1/2) - pq] \left( \frac{p^2}{p^2 + q^2} \right) \left( \frac{q^2}{p^2 + q^2} \right). \tag{B.9} $$

A third source of bits can be obtained by taking the XOR of adjacent pairs. (The XOR of two bits $a$ and $b$ is 0 if and only if $a = b$.) Call this sequence $U = (U_1, \ldots, U_{n/2})$. This is given on the fourth row in Figure B.1. It turns out that $U$ is independent of $Y$ and $Z$, and applying the algorithm on $U$ yields independent and unbiased bits. It should be noted, however, that given $L = m$, the bits in $U$ are not independent, as it contains exactly $m$ 1's.

Note that when the von Neumann algorithm is applied to the sequence $Z$ of discarded bits and to $U$, it creates a new sequence of discarded bits. The algorithm can be applied again to this sequence, improving the extraction rate.

Indeed, this can be continued indefinitely. This idea is developed in **Peres (1992)**.

**B.3. Simulating Discrete Distributions and Sampling**

A Poisson random variable $X$ with mean $\lambda$ has mass function

$$ p(k) := \frac{e^{-\lambda} \lambda^k}{k!}. $$

The variable $X$ can be simulated using a uniform random variable $U$ as follows: subdivide the unit interval into adjacent subintervals $I_1, I_2, \ldots$ where the length of $I_k$ is $p(k)$. Because the chance that a random point in $[0, 1]$ falls in $I_k$ is $p(k)$, the index $X$ for which $U \in I_X$ is a Poisson random variable with mean $\lambda$.

In principle, any discrete random variable can be simulated from a uniform random variable using this method. To be concrete, suppose $X$ takes on the values $a_1, \ldots, a_N$ with probabilities $p_1, p_2, \ldots, p_N$. Let $F_k := \sum_{j=1}^{k} p_j$ (and $F_0 := 0$), and define $\varphi : [0, 1] \to \{a_1, \ldots, a_N\}$ by

$$ \varphi(u) := a_k \text{ if } F_{k-1} < u \le F_k. \tag{B.10} $$

If $X = \varphi(U)$, where $U$ is uniform on $[0, 1]$, then $\mathbf{P}\{X = a_k\} = p_k$ (Exercise B.2).

One obstacle is that this recipe requires that the probabilities $(p_1, \ldots, p_N)$ are known exactly, while in many applications these are only known up to constant factor. This is a common situation, and many of the central examples treated in this book (such as the Ising model) fall into this category. It is common in applications to desire uniform samples from combinatorial sets whose sizes are not known.

Many problems are defined for a family of structures indexed by *instance size*. The efficiency of solutions is measured by the growth of the time required to run the algorithm as a function of instance size. If the run-time grows exponentially in instance size, the algorithm is considered impractical.

### PDF page 394 (book page 378)

**FIGURE B.2.** $f(x) = 4e^{-4x}$, the exponential probability density function with rate 4. *[Figure: a decreasing exponential curve on axes with horizontal range 0 to about 1.2 (ticks at 0.2, 0.4, 0.6, 0.8, 1, 1.2) and vertical range 0 to 4 (ticks at 1, 2, 3, 4); the curve starts at height 4 at $x = 0$ and decays toward 0.]*

**B.4. Inverse Distribution Function Method**

EXAMPLE B.1. Let $U$ be a uniform random variable on $[0, 1]$, and define $Y = -\lambda^{-1} \log(1 - U)$. The distribution function of $Y$ is

$$ F(t) = \mathbf{P}\{Y \le t\} = \mathbf{P}\{-\lambda^{-1} \log(1 - U) \le t\} = \mathbf{P}\{U \le 1 - e^{-\lambda t}\}. \tag{B.11} $$

As $U$ is uniform, the rightmost probability above equals $1 - e^{-\lambda t}$, the distribution function for an exponential random variable with rate $\lambda$. (The graph of an exponential density with $\lambda = 4$ is shown in Figure B.2.)

This calculation leads to the following algorithm:

(1) Generate $U$.
(2) Output $Y = -\lambda^{-1} \log(1 - U)$.

The algorithm in Example B.1 is a special case of the ***inverse distribution function method*** for simulating a random variable with distribution function $F$, which is practical *provided that $F$ can be inverted efficiently*. Unfortunately, there are not very many examples where this is the case.

Suppose that $F$ is strictly increasing, so that its inverse function $F^{-1} : [0, 1] \to \mathbb{R}$ is defined everywhere. Recall that $F^{-1}$ is the function so that $F^{-1} \circ F(x) = x$ and $F \circ F^{-1}(y) = y$.

We now show how, using a uniform random variable $U$, to simulate $X$ with distribution function $F$. For a uniform $U$, let $X = F^{-1}(U)$. Then

$$ \mathbf{P}\{X \le t\} = \mathbf{P}\{F^{-1}(U) \le t\} = \mathbf{P}\{U \le F(t)\}. \tag{B.12} $$

The last equality follows because $F$ is strictly increasing, so $F^{-1}(U) \le t$ if and only if $F\left(F^{-1}(U)\right) \le F(t)$. Since $U$ is uniform, the probability on the right can be easily evaluated to get

$$ \mathbf{P}\{X \le t\} = F(t). \tag{B.13} $$

That is, the distribution function of $X$ is $F$.

**B.5. Acceptance-Rejection Sampling**

Suppose that we have a black box which on demand produces a uniform sample from a region $R'$ in the plane, but what we really want is to sample from another region $R$ which is contained in $R'$ (see Figure B.3).

If independent points are generated, each uniformly distributed over $R'$, until a point falls in $R$, then this point is a uniform sample from $R$ (Exercise B.5).

### PDF page 395 (book page 379)

**FIGURE B.3.** $R'$ is the diagonally hatched square, and $R$ is the bricked circle. *[Figure: a square filled with a diagonal-line (hatched) pattern, with an inscribed circle filled with a brick pattern; the corners of the square outside the circle remain diagonally hatched.]*

Now we want to use this idea to simulate a random variable $X$ with density function $f$ given that we know how to simulate a random variable $Y$ with density function $g$.

We will suppose that

$$ f(x) \le Cg(x) \text{ for all } x, \tag{B.14} $$

for some constant $C$. We will see that good choices for the density $g$ minimize the constant $C$. Because $f$ and $g$ both integrate to unity, $C \ge 1$.

Here is the algorithm:

(1) Generate a random variable $Y$ having probability density function $g$.
(2) Generate a uniform random variable $U$.
(3) Conditional on $Y = y$, if $Cg(y)U \le f(y)$, output the value $y$ and halt.
(4) Repeat.

We now show that this method generates a random variable with probability density function $f$. Given that $Y = y$, the random variable $U_y := Cg(y)U$ is uniform on $[0, Cg(y)]$. By Exercise B.4, the point $(Y, U_Y)$ is uniform over the region bounded between the graph of $Cg$ and the horizontal axis. We halt the algorithm if and only if this point is also underneath the graph of $f$. By Exercise B.5, in this case, the point is uniformly distributed over the region under $f$. But again by Exercise B.4, the horizontal coordinate of this point has distribution $f$. (See Figure B.4.)

**FIGURE B.4.** The probability density function $f$ lies below the scaled probability density function of $g$. *[Figure: on a set of axes, two humped curves rising from the origin; the upper, larger curve is labeled $Cg(x)$ and the lower curve, lying entirely beneath it, is labeled $f(x)$; both return to the horizontal axis at the right.]*

### PDF page 396 (book page 380)

The value of $C$ determines the efficiency of the algorithm. The probability that the algorithm terminates on any trial, given that $Y = y$, is $f(y)/Cg(y)$. Using the law of total probability, the unconditional probability is $C^{-1}$. The number of trials required is geometric, with success probability $C^{-1}$, and so the expected number of trials before terminating is $C$.

We comment here that there is a version of this method for discrete random variables; the reader should work on the details for herself.

EXAMPLE B.2. Consider the gamma distribution with parameters $\alpha$ and $\lambda$. Its probability density function is

$$ f(x) = \frac{x^{\alpha-1}\lambda^{\alpha}e^{-\lambda x}}{\Gamma(\alpha)}. \tag{B.15} $$

(The function $\Gamma(\alpha)$ in the denominator is defined to normalize the density so that it integrates to unity. It has several interesting properties, most notably that $\Gamma(n) = (n-1)!$ for integers $n$.)

The distribution function does not have a nice closed-form expression, so inverting the distribution function does not provide an easy method of simulation.

We can use the rejection method here, when $\alpha > 1$, bounding the density by a multiple of the exponential density

$$ g(x) = \mu e^{-\mu x}. $$

The constant $C$ depends on $\mu$, and

$$ C = \sup_x \frac{[\Gamma(\alpha)]^{-1}(\lambda x)^{\alpha-1}\lambda e^{-\lambda x}}{\mu e^{-\mu x}}. $$

A bit of calculus shows that the supremum is attained at $x = (\alpha - 1)/(\lambda - \mu)$ and

$$ C = \frac{\lambda^{\alpha}(\alpha-1)^{\alpha-1}e^{1-\alpha}}{\Gamma(\alpha)\mu(\lambda-\mu)^{\alpha-1}}. $$

Some more calculus shows that the constant $C$ is minimized for $\mu = \lambda/\alpha$, in which case

$$ C = \frac{\alpha^{\alpha}e^{1-\alpha}}{\Gamma(\alpha)}. $$

The case of $\alpha = 2$ and $\lambda = 1$ is shown in Figure B.5, where $4e^{-1}\frac{1}{2}e^{-x/2}$ bounds the gamma density.

We end the example by commenting that the exponential is easily simulated by the inverse distribution function method, as the inverse to $1 - e^{-\mu x}$ is $(-1/\mu)\ln(1-u)$.

**B.6. Simulating Normal Random Variables**

Recall that a standard normal random variable has the "bell-shaped" probability density function specified by

$$ f(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^2}. \tag{B.16} $$

The corresponding distribution function $\Phi$ is the integral

$$ \Phi(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}t^2}dt, \tag{B.17} $$

### PDF page 397 (book page 381)

**FIGURE B.5.** The Gamma density for $\alpha = 2$ and $\lambda = 1$, along with $4e^{-1}$ times the exponential density of rate $1/2$. *[Figure: a plot over $x$ from 0 to 6 (y-axis ticks 0.1–0.7) showing two decreasing curves — the exponential-bound curve starting near 0.7 at $x=0$ and decaying monotonically, and the gamma density starting at 0, rising to a peak near $x=1$ around 0.37, then decaying; the two curves nearly coincide for large $x$.]*

**FIGURE B.6.** The standard normal density on the left, and on the right the joint density of two independent standard normal variables. *[Figure: on the left, the standard normal bell curve over $x$ from $-3$ to $3$ (y-axis to about 0.4); on the right, a 3-D surface plot of the joint density of two independent standard normals, a bell-shaped hump over the plane with axes ranging roughly $-2$ to $2$ and height ticks 0.05, 0.1, 0.15.]*

which cannot be evaluated in closed form. The inverse of $\Phi$ likewise cannot be expressed in terms of elementary functions. As a result the inverse distribution function method requires the numerical evaluation of $\Phi^{-1}$. We present here another method of simulating from $\Phi$ which does not require the evaluation of the inverse of $\Phi$.

Let $X$ and $Y$ be independent standard normal random variables. Geometrically, the ordered pair $(X, Y)$ is a random point in the plane. The joint probability density function for $(X, Y)$ is shown in Figure B.6.

We will write $(R, \Theta)$ for the representation of $(X, Y)$ in polar coordinates and define $S := R^2 = X^2 + Y^2$ to be the squared distance of $(X, Y)$ to the origin.

The distribution function of $S$ is

$$ \mathbf{P}\{S \le t\} = \mathbf{P}\{X^2 + Y^2 \le t\} = \iint_{D(\sqrt{t})} \frac{1}{2\pi}e^{-\frac{x^2+y^2}{2}}dxdy, \tag{B.18} $$

where $D(\sqrt{t})$ is the disc of radius $\sqrt{t}$ centered at the origin. Changing to polar coordinates, this equals

$$ \int_0^{\sqrt{t}} \int_0^{2\pi} \frac{1}{2\pi}e^{-\frac{r^2}{2}}rdrd\theta = 1 - e^{-t/2}. \tag{B.19} $$

### PDF page 398 (book page 382)

We conclude that $S$ has an exponential distribution with mean 2.

To summarize, the squared radial part of $(X, Y)$ has an exponential distribution, its angle has a uniform distribution, and these are independent.

Our standing assumption is that we have available independent uniform variables; here we need two, $U_1$ and $U_2$. Define $\Theta := 2\pi U_1$ and $S := -2\log(1 - U_2)$, so that $\Theta$ is uniform on $[0, 2\pi]$ and $S$ is independent of $\Theta$ and has an exponential distribution.

Now let $(X, Y)$ be the Cartesian coordinates of the point with polar representation $(\sqrt{S}, \Theta)$. Our discussion shows that $X$ and $Y$ are independent standard normal variables.

**B.7. Sampling from the Simplex**

Let $\Delta_n$ be the $n - 1$-dimensional simplex:

$$ \Delta_n := \left\{ (x_1, \ldots, x_n) \, : \, x_i \ge 0, \sum_{i=1}^n x_i = 1 \right\}. \tag{B.20} $$

This is the collection of probability vectors of length $n$. We consider here the problem of sampling from $\Delta_n$.

Let $U_1, U_2, \ldots, U_{n-1}$ be i.i.d. uniform variables in $[0, 1]$, and define $U_{(k)}$ to be the $k$-th smallest among these.

Let $T : \mathbb{R}^{n-1} \to \mathbb{R}^n$ be the linear transformation defined by

$$ T(u_1, \ldots, u_{n-1}) = (u_1, u_2 - u_1, \ldots, u_{n-1} - u_{n-2}, 1 - u_{n-1}). $$

Note that $T$ maps the set $A_{n-1} = \{(u_1, \ldots, u_{n-1}) \, : \, u_1 \le u_2 \le \cdots \le u_{n-1} \le 1\}$ linearly to $\Delta_n$, so Exercise B.8 and Exercise B.9 together show that $(X_1, \ldots, X_n) = T(U_{(1)}, \ldots, U_{(n-1)})$ is uniformly distributed on $\Delta_n$.

We can now easily generate a sample from $\Delta_n$: throw down $n - 1$ points uniformly in the unit interval, sort them along with the points 0 and 1, and take the vector of successive distances between the points.

The algorithm described above requires sorting $n$ variables. This sorting can, however, be avoided. See Exercise B.10.

**B.8. About Random Numbers**

Because most computer languages provide a built-in capability for simulating random numbers chosen independently from the uniform density on the unit interval $[0, 1]$, we will assume throughout this book that there is a ready source of independent uniform-$[0, 1]$ random variables.

This assumption requires some further discussion, however. Since computers are finitary machines and can work with numbers of only finite precision, it is in fact impossible for a computer to generate a continuous random variable. Not to worry: a discrete random variable which is uniform on, for example, the set in (B.3) is a very good approximation to the uniform distribution on $[0, 1]$, at least when $n$ is large.

A more serious issue is that computers do not produce truly random numbers at all. Instead, they use deterministic algorithms, called ***pseudorandom number generators***, to produce sequences of numbers that *appear* random. There are many tests which identify features which are unlikely to occur in a sequence of independent and identically distributed random variables. If a sequence produced by

### PDF page 399 (book page 383)

**FIGURE B.7.** A self-avoiding path *[Figure: a self-avoiding lattice path drawn on $\mathbb{Z}^2$, shown as filled dots connected by horizontal and vertical segments in a staircase-like configuration.]*

a pseudorandom number generator can pass a battery of these tests, it is considered an appropriate substitute for random numbers.

One technique for generating pseudorandom numbers is a ***linear congruential sequence*** (LCS). Let $x_0$ be an integer seed value. Given that $x_{n-1}$ has been generated, let

$$ x_n = (ax_{n-1} + b) \mod m. \tag{B.21} $$

Here $a, b$ and $m$ are fixed constants. Clearly, this produces integers in $\{0, 1, \ldots, m\}$; if a number in $[0, 1]$ is desired, divide by $m$.

The properties of $(x_0, x_1, x_2, \ldots)$ vary greatly depending on choices of $a, b$ and $m$, and there is a great deal of art and science behind making judicious choices for the parameters. For example, if $a = 0$, the sequence does not look random at all!

Any linear congruential sequence is eventually periodic (Exercise B.12). The period of a LCS can be much smaller than $m$, the longest possible value.

The goal of any method for generating pseudorandom numbers is to generate output which is difficult to distinguish from truly random numbers using statistical methods. It is an interesting question whether a given pseudorandom number generator is good. We will not enter into this issue here, but the reader should be aware that the "random" numbers produced by today's computers are not in fact random, and sometimes this can lead to inaccurate simulations. For an excellent discussion of these issues, see **Knuth (1997)**.

**B.9. Sampling from Large Sets\***

As discussed in Section 14.4, sampling from a finite set and estimating its size are related problems. Here we discuss the set of self-avoiding paths of length $n$ and also mention domino tilings.

EXAMPLE B.3 (Self-avoiding walks). A self-avoiding walk in $\mathbb{Z}^2$ of length $n$ is a sequence $(z_0, z_1, \ldots, z_n)$ such that $z_0 = (0, 0)$, $|z_i - z_{i-1}| = 1$, and $z_i \neq z_j$ for $i \neq j$. See Figure B.7 for an example of length 6. Let $\Xi_n$ be the collection of all self-avoiding walks of length $n$. Chemical and physical structures such as molecules and polymers are often modeled as "random" self-avoiding walks, that is, as uniform samples from $\Xi_n$.

Unfortunately, no efficient algorithm for finding the size of $\Xi_n$ is known. Nonetheless, we still desire (a practical) method for sampling uniformly from $\Xi_n$. We present a Markov chain in Example B.5 whose state space is the set of all self-avoiding walks of a given length and whose stationary distribution is uniform—but whose mixing time is not known.

EXAMPLE B.4 (Domino tilings). Domino tilings, sometimes also called ***dimer systems***, are another important family of examples for counting and sampling

### PDF page 400 (book page 384)

**FIGURE B.8.** A domino tiling of a $6 \times 6$ checkerboard. *[Figure: a $6 \times 6$ square region tiled by shaded dominoes (each a $2 \times 1$ or $1 \times 2$ rectangle) that partition the checkerboard, with some placed horizontally and some vertically.]*

algorithms. A ***domino*** is a $2 \times 1$ or $1 \times 2$ rectangle, and, informally speaking, a ***domino tiling*** of a subregion of $\mathbb{Z}^2$ is a partition of the region into dominoes, disjoint except along their boundaries (see Figure B.8).

Random domino tilings arise in statistical physics, and it was **Kasteleyn (1961)** who first computed that when $n$ and $m$ are both even, there are

$$ 2^{nm/2} \prod_{i=1}^{n/2} \prod_{j=1}^{m/2} \left( \cos^2 \frac{\pi i}{n+1} + \cos^2 \frac{\pi j}{m+1} \right) $$

domino tilings of an $n \times m$ grid.

The notion of a ***perfect matching*** (a set of disjoint edges together covering all vertices) generalizes domino tiling to arbitrary graphs, and much is known about counting and/or sampling perfect matchings on many families of graphs. See, for example, **Luby, Randall, and Sinclair (1995)** or **Wilson (2004a)**. Section 25.2 discusses lozenge tilings, which correspond to perfect matchings on a hexagonal lattice.

EXAMPLE B.5 (Pivot chain for self-avoiding paths). The space $\Xi_n$ of self-avoiding lattice paths of length $n$ was described in Example B.3. These are paths in $\mathbb{Z}^2$ of length $n$ which never intersect themselves.

Counting the number of self-avoiding paths is an unsolved problem. For more on this topic, see **Madras and Slade (1993)**. **Randall and Sinclair (2000)** give an algorithm for approximately sampling from the uniform distribution on these walks.

We describe now a Markov chain on $\Xi_n$ and show that it is irreducible. If the current state of the chain is the path $(0, v_1, \ldots, v_n) \in \Xi_n$, the next state is chosen by the following:

(1) Pick a value $k$ from $\{0, 1, \ldots, n\}$ uniformly at random.
(2) Pick uniformly at random from the following transformations of $\mathbb{Z}^2$: rotations clockwise by $\pi/2$, $\pi$, $3\pi/2$, reflection across the $x$-axis, and reflection across the $y$-axis.
(3) Take the path from vertex $k$ on, $(v_k, v_{k+1}, \ldots, v_n)$, and apply the transformation chosen in the previous step to this subpath only, taking $v_k$ as the origin.
(4) If the resulting path is self-avoiding, this is the new state. If not, repeat.

An example move is shown in Figure B.9.

### PDF page 401 (book page 385)

**FIGURE B.9.** Example of a single move of pivot chain for self-avoiding walk. *[Figure: two self-avoiding paths side by side, connected by a right arrow "$\rightarrow$". Left path labeled "current path" with a marked vertex "4" and a dashed circular arrow indicating a rotation, with origin "(0,0)" marked. Right path labeled "path after rotating by $\pi$ from vertex 4", with vertex "4" and origin "(0,0)" marked.]*

We now show that this chain is irreducible by proving that any self-avoiding path can be unwound to a straight line by a sequence of possible transitions. Since the four straight paths starting at $(0, 0)$ are rotations of each other and since any transition can also be undone by a dual transition, any self-avoiding path can be transformed into another. The proof below follows **Madras and Slade (1993**, Theorem 9.4.4).

For a path $\xi \in \Xi_n$, put around $\xi$ as small a rectangle as possible, and define $D = D(\xi)$ to be the sum of the length and the width of this rectangle. The left-hand diagram in Figure B.10 shows an example of this bounding rectangle. Define also $A = A(\xi)$ to be the number of interior vertices $v$ of $\xi$ where the two edges incident at $v$ form an angle of $\pi$, that is, which look like either $\longrightarrow\!\!\bullet\!\!\longrightarrow$ or $\begin{array}{c}\bullet\end{array}$ *(a vertical straight-through vertex)*. We first observe that $D(\xi) \leq n$ and $A(\xi) \leq n - 1$ for any $\xi \in \Xi_n$, and $D(\xi) + A(\xi) = 2n - 1$ if and only if $\xi$ is a straight path. We show now that if $\xi$ is any path different from the straight path, we can make a legal move—that is, a move having positive probability—to another path $\xi'$ which has $D(\xi') + A(\xi') > D(\xi) + A(\xi)$.

There are two cases which we will consider separately.

*Case 1.* Suppose that at least one side of the bounding box does not contain either endpoint, 0 or $v_n$, of $\xi = (0, v_1, \ldots, v_n)$. This is the situation for the path on the left-hand side in Figure B.10. Let $k \geq 1$ be the smallest index so that $v_k$ lies on this side. Obtain $\xi'$ by taking $\xi$ and reflecting its tail $(v_k, v_{k+1}, \ldots, v_n)$ across this box side. Figure B.10 shows an example of this transformation. The new path $\xi'$ satisfies $D(\xi') > D(\xi)$ and $A(\xi') = A(\xi)$ (the reader should convince himself this is indeed true!)

*Case 2.* Suppose every side of the bounding box contains an endpoint of $\xi$. This implies that the endpoints are in opposing corners of the box. Let $k$ be the largest index so that the edges incident to $v_k$ form a right angle. The path $\xi$ from $v_k$ to $v_n$ forms a straight line segment and must lie along the edge of the bounding box. Obtain $\xi'$ from $\xi$ by rotating this straight portion of $\xi$ so that it lies outside the original bounding box. See Figure B.11.

### PDF page 402 (book page 386)

**FIGURE B.10.** A SAW without both endpoints in corners of bounding box. *[Figure: Left, a self-avoiding walk (SAW) drawn as a solid path inside a dashed bounding box, with the point (0,0) labeled at the bottom-left corner. An arrow "→" points to the right. Right, the transformed walk after being reflected across the side of the bounding box not containing both endpoints; the original bounding box is shown dashed and the reflected box dotted, with (0,0) labeled at the bottom. Below the right figure: "reflected across side not containing both endpoints".]*

**FIGURE B.11.** A SAW with endpoints in opposing corners. *[Figure: Left, a short self-avoiding walk drawn as a solid path inside a dashed bounding box. An arrow "→" points to the right. Right, the walk after the final straight segment has been rotated outside the box; the dashed box and dotted box indicate the new bounding region. Below the right figure: "rotated final straight segment outside box".]*

This operation reduces one dimension of the bounding box by at most the length of the rotated segment, but increases the other dimension by this length. This shows that $D(\xi') \geq D(\xi)$. Also, we have strictly increased the number of straight angles, so $D(\xi') + A(\xi') > D(\xi) + A(\xi)$.

In either case, $D + A$ is strictly increased by the transformation, so continuing this procedure eventually leads to a straight line segment. This establishes that the pivot Markov chain is irreducible.

It is an open problem to analyze the convergence behavior of the pivot chain on self-avoiding walks. The algorithm of **Randall and Sinclair (2000)** uses a different underlying Markov chain to approximately sample from the uniform distribution on these walks.

**Exercises**

EXERCISE B.1. Check that the random variable in (B.4) has the uniform distribution on the set in (B.3).

### PDF page 403 (book page 387)

EXERCISE B.2. Let $U$ be uniform on $[0,1]$, and let $X$ be the random variable $\varphi(U)$, where $\varphi$ is defined as in (B.10). Show that $X$ takes on the value $a_k$ with probability $p_k$.

EXERCISE B.3. Describe how to use the inverse distribution function method to simulate from the probability density function

$$ f(x) = \begin{cases} 2x & \text{if } 0 < x < 1, \\ 0 & \text{otherwise.} \end{cases} $$

EXERCISE B.4. Show that if $(Y, U_Y)$ is the pair generated in one round of the rejection sampling algorithm, then $(Y, U_Y)$ is uniformly distributed over the region bounded between the graph of $Cg$ and the horizontal axis. Conversely, if $g$ is a density and a point is sampled from the region under the graph of $g$, then the projection of this point onto the $x$-axis has distribution $g$.

EXERCISE B.5. Let $R \subset R' \subset \mathbb{R}^k$. Show that if points uniform in $R'$ are generated until a point falls in $R$, then this point is uniformly distributed over $R$. Recall that this means that the probability of falling in any subregion $B$ of $R$ is equal to $\mathrm{Vol}_k(B)/\mathrm{Vol}_k(R)$.

EXERCISE B.6. This exercise uses the notation in Section B.6. Argue that since the joint density $(2\pi)^{-1} \exp[-(x^2 + y^2)/2]$ is a function of $s = x^2 + y^2$, the distribution of $\Theta$ must be uniform and independent of $S$.

EXERCISE B.7. Find a method for simulating the random variable $Y$ with density

$$ g(x) = e^{-|x|/2}. $$

Then use the rejection method to simulate a random variable $X$ with the standard normal density given in (B.16).

EXERCISE B.8. Show that the vector $(U_{(1)}, \ldots, U_{(n-1)})$ is uniformly distributed over the set $A_{n-1} = \{(u_1, \ldots, u_{n-1}) : u_1 \leq u_2 \leq \cdots \leq u_{n-1} \leq 1\}$.

Let $T : \mathbb{R}^{n-1} \to \mathbb{R}^n$ be the linear transformation defined by

$$ T(u_1, \ldots, u_{n-1}) = (u_1, u_2 - u_1, \ldots, u_{n-1} - u_{n-2}, 1 - u_{n-1}). $$

EXERCISE B.9. Suppose that $X$ is uniformly distributed on a region $A$ of $\mathbb{R}^d$, and the map $T : \mathbb{R}^d \to \mathbb{R}^r, d \leq r$ is a linear transformation. A useful fact is that for a region $R \subset \mathbb{R}^d$,

$$ \mathrm{Volume}_d(TR) = \sqrt{\det(T^t T)}\, \mathrm{Volume}(R), $$

where $\mathrm{Volume}_d(TR)$ is the $d$-dimensional volume of $TR \subset \mathbb{R}^r$. Use this to show that $Y = TX$ is uniformly distributed over $TA$.

EXERCISE B.10. (This exercise requires knowledge of the change-of-variables formula for $d$-dimensional random vectors.) Let $Y_1, \ldots, Y_n$ be i.i.d. exponential variables, and define

$$ X_i = \frac{Y_i}{Y_1 + \cdots + Y_n}. \tag{B.22} $$

Show that $(X_1, \ldots, X_n)$ is uniformly distributed on $\Delta_n$.

### PDF page 404 (book page 388)

**FIGURE B.12.** A proper 3-coloring of a rooted tree. (As is common practice, we have placed the root at the top.) *[Figure: A rooted tree drawn with the root at the top, each vertex a circle containing a color label. The root is labeled 1. It has two children: left child labeled 2 and right child labeled 3. The vertex labeled 2 has two children labeled 3 and 1; the vertex labeled 3 has two children labeled 1 and 2.]*

EXERCISE B.11. Let $U_1, U_2, \ldots, U_n$ be independent random variables, each uniform on the interval $[0,1]$. Let $U_{(k)}$ be the $k$-th **_order statistic_**, the $k$-th smallest among $\{U_1, \ldots, U_n\}$, so that

$$ U_{(1)} < U_{(2)} < \cdots < U_{(n)}. $$

The purpose of this exercise is to give several different arguments that

$$ \mathbf{E}\left(U_{(k)}\right) = \frac{k}{n+1}. \tag{B.23} $$

Fill in the details for the following proofs of (B.23):

(a) Find the density of $U_{(k)}$, and integrate.
(b) Find the density of $U_{(n)}$, and observe that given $U_{(n)}$, the other variables are the order statistics for uniforms on the interval $[0, U_{(n)}]$. Then apply induction.
(c) Let $Y_1, \ldots, Y_n$ be independent and identically distributed exponential variables with mean 1, and let $S_1 = Y_1, S_2 = Y_1 + Y_2, \ldots$ be their partial sums. Show that the random vector

$$ \frac{1}{S_{n+1}} (S_1, S_2, \ldots, S_n) \tag{B.24} $$

has constant density on the simplex

$$ \mathcal{A}_n = \{(x_1, \ldots, x_n) : 0 < x_1 < x_2 < \cdots < x_n < 1\}. $$

Conclude that (B.24) has the same law as the vector of order statistics.

EXERCISE B.12. Show that if $f : \{1, \ldots, m\} \to \{1, \ldots, m\}$ is any function and $x_n = f(x_{n-1})$ for all $n$, then there is an integer $k$ such that $x_n = x_{n+k}$ eventually. That is, the sequence is eventually periodic.

EXERCISE B.13. Consider the following algorithm for sampling proper colorings on a rooted tree (see Figure B.12): choose the color of the root uniformly at random from $\{1, \ldots, q\}$. Given that colors have been assigned to all vertices up to depth $d$, for a vertex at depth $d + 1$, assign a color chosen uniformly at random from

$$ \{1, 2, \ldots, q\} \setminus \{\text{color of parent}\}. \tag{B.25} $$

(a) Verify that the coloring generated is uniformly distributed over all proper colorings.
(b) Similarly extend the sampling algorithms of Exercises 14.6 and 14.7 to the case where the base graph is an arbitrary rooted tree.

### PDF page 405 (book page 389)

EXERCISE B.14. A nearest-neighbor path $0 = v_0, \ldots, v_n$ is ***non-reversing*** if $v_k \neq v_{k-2}$ for $k = 2, \ldots, n$. It is simple to generate a non-reversing path recursively. First choose $v_1$ uniformly at random from $\{(0,1), (1,0), (0,-1), (-1,0)\}$. Given that $v_0, \ldots, v_{k-1}$ is a non-reversing path, choose $v_k$ uniformly from the three sites in $\mathbb{Z}^2$ at distance 1 from $v_{k-1}$ but different from $v_{k-2}$.

Let $\Xi_n^{\mathrm{nr}}$ be the set of non-reversing nearest-neighbor paths of length $n$. Show that the above procedure generates a uniform random sample from $\Xi_n^{\mathrm{nr}}$.

EXERCISE B.15. One way to generate a random self-avoiding path is to generate non-reversing paths until a self-avoiding path is obtained.

(a) Let $c_{n,4}$ be the number of paths in $\mathbb{Z}^2$ which do not contain loops of length 4 at indices $i \equiv 0 \mod 4$. More exactly, these are paths $(0,0) = v_0, v_1, \ldots, v_n$ so that $v_{4i} \neq v_{4(i-1)}$ for $i = 1, \ldots, n/4$. Show that

$$ c_{n,4} \leq \left[4(3^3) - 8\right] \left[3^4 - 6\right]^{\lceil n/4 \rceil - 1}. \tag{B.26} $$

(b) Conclude that the probability that a random non-reversing path of length $n$ is self-avoiding is bounded above by $e^{-\alpha n}$ for some fixed $\alpha > 0$.

Part (b) implies that if we try generating random non-reversing paths until we get a self-avoiding path, the expected number of trials required grows exponentially in the length of the paths.

**Notes**

On random numbers, von Neumann offers the following:

> "Any one who considers arithmetical methods of producing random digits is, of course, in a state of sin" (**von Neumann, 1951**).

Iterating the von Neumann algorithm asymptotically achieves the optimal extraction rate of $-p \log_2 p - (1-p) \log_2(1-p)$, the entropy of a biased random bit (**Peres, 1992**). Earlier, a different optimal algorithm was given by **Elias (1972)**, although the iterative algorithm has some computational advantages.

**Further reading.** For a stimulating and much wider discussion of univariate simulation techniques, **Devroye (1986)** is an excellent reference.

# Chapter 11 — METROPOLIS-HASTINGS SAMPLER
*(PDF pages 122–135; booklet pages 117–130)*


### PDF page 122 (booklet page 117)

*[Margin notes across the top of the page, in the instructor's hand. Left block: "Stochastic process $\to$ a family of random variables $X_t$, $t \in \mathcal{T}$, an index set." with an arrow to "$\mathcal{T} = \{0,1,\dots\}$"(?), then "$\mathcal{T} \to$ discrete" (the word "discrete" hand-underlined) "$\Rightarrow$ Markov chain". Right block: "chain $X_1, X_2, \dots$ discrete time"; "$P(X_t = j \mid X_{t-1} = i) = P_{ij}$"; "$P(X_1(?) = j) = \pi_j$".]*

# Chapter 11 — METROPOLIS-HASTINGS SAMPLER

The Metropolis-Hastings sampler was developed by Metropolis, Rosenbluth, Rosenbluth, Teller, and Teller(1953). It was generalized by Hastings(1970).

(1) Tierney, L.(1994), Markov chains for exploring posterior distributions(with discussions), Annals of statistics, 22, 1701-1762.

(2) Chib, S. and Greenberg, E.(1995), uender-standing [sic] the Metropolis-Hastings algorithm, The American Statistician, 49, 327-335.

**11.1 General Discussion**

*[margin note, right, with a long curved lead-line drawn down to the $\alpha(x,y)$ equation below: "Markov chain possesses a stationary distribution i.e. time invariant (equilibrium probability distribution)"]*

There are three components in the M-H sampler (More powerful than Accept-Rejection Algorithm).

(1) Target density

This is the density we need to draw a sampler from, and we denote it by $\pi(x)$. We do not need to know the normalization constant, only the kernel is required.

(2) Candidate-generating density (proposal)

The process is at $x$, and we generate value $y$ from the proposal density $q(x,y)$ where $\int q(x,y)dy = 1$. Note that $q(x,y)$ does not have to depend on $x$.

(3) Probability of move(jumping probability)

This is the probability that the process(chain) moves from $x$ to $y$, and is denoted by $\alpha(x,y)$. For the M-H sampler

$$\alpha(x,y) = \min\left\{1, \frac{\pi(y)q(y,x)}{\pi(x)q(x,y)}\right\}$$

*[margin note, right of the display: "detailed balance"]*

> ⚠ Check FAILED: The M-H acceptance probability $\alpha(x,y)=\min\{1,\ \pi(y)q(y,x)/(\pi(x)q(x,y))\}$ satisfies detailed balance: $\pi(x)q(x,y)\alpha(x,y) = \pi(y)q(y,x)\alpha(y,x) = \min\{\pi(x)q(x,y),\ \pi(y)q(y,x)\}$. — the stated result did not reproduce (see verification log)

ensures that the chain is reversible. *[the word "reversible" is hand-underlined]*

What is the sampler?

1. Start with $x_0$.

2. Generate $x_1$ from $q(x_0, x_1)$.

3. Compute $\alpha(x_0, x_1) = \min\left\{1, \frac{\pi(x_1)q(x_1,x_0)}{\pi(x_0)q(x_0,x_1)}\right\}$, jumping/accept probability

*[margin note, right, level with step 3: "$j$ = state"]*

117

*[Handwritten notes in the bottom margin. Left: "$\Pr(X_t = i) = \pi_i$". Center, directly beneath the page number: "Transition [illegible] matrix(?)" — heavily struck through and largely obliterated. Right: "$\pi_i P_{ij} = \pi_j P_{ji}$ — reversible" and beneath it "transition probability matrix".]*

### PDF page 123 (booklet page 118)

4. Draw $U \sim \text{Uniform}(0,1)$

If $\mu \le \alpha(x_0, x_1)$ go to $x_1$; otherwise stay at $x_0$. $\text{[sic: the variable drawn in step 4 is } U \text{, not } \mu\text{]}$

Repeat 1-4 to got [sic] a sample. Markov chain

Reversible

Comments:

One can avoid construction of proposal densities. A new area is Hamiltonian Monte Carlo (HMC), used extensively on Stan. HMC also has difficulties for tuning. Need to construct a momentum distribution.

**11.2 Convergence**

Convergence to the target density $\pi(x)$ occurs under mild regularity condition [sic]: The Markov chain must be ergodic.

Ergodic *[the heading "Ergodic" is hand-underlined with a wavy line]*

(1) Irreducible: Let $x_1$ and $x_2$ be any two points in the domain of $\pi(x)$. The chain must go from $x_1 \to x_2$ and $x_2 \to x_1$ with positive probability in a finite number of steps. *[the phrase "finite number of steps" is hand-underlined]*

(2) Aperiodic: The number of moves required to go from $x_1 \to x_2$ is not a multiple of some integer(i.e.,period=1). *[the word "integer" is hand-underlined]*

Generally, the regularity condition is met if $q(x,y)$ has a positive density on the same support as $\pi(x)$.

Special cases *[margin mark: a short unreadable dash (?) in the left margin here]*

(1) Suppose $q(x,y) = q(y)$. Then, the proposed value $y$ is drawn independently of the current value $x$. The chain is then called an independence chain. *[an illegible handwritten mark sits above "proposed" (?)]*

(2) Suppose $q(x,y) = q(y,x)$(i.e., the candidate generating density is symmetric). Then,

$$\alpha(x,y) = \min\left\{1, \frac{\pi(y)q(y,x)}{\pi(x)q(x,y)}\right\} = \min\left\{1, \frac{\pi(y)}{\pi(x)}\right\}$$

*(correction: the printed right-hand side reads $\min\left\{\frac{\pi(y)}{\pi(x)}\right\}$; a handwritten mark above the brace inserts the missing "$1,$" (?))*

> ✔ Verified: For a symmetric candidate density, q(x,y)=q(y,x), the MH acceptance ratio π(y)q(y,x)/(π(x)q(x,y)) equals π(y)/π(x).

Thus, if $\pi(y) \ge \pi(x)$, the chain moves to $x$ surely; otherwise the chain moves to $x$ with probability $\frac{\pi(y)}{\pi(x)}$. $\text{[sic: both occurrences should be } y\text{, the proposed value]}$ This is the original Metropolis sampler(Metropolis 1953).

(3) Suppose $\pi(x) = \phi(x)h(x)$ and $q(x,y) = h(y)$.
Then

$$\alpha(x,y) = \min\left\{\frac{\phi(y)}{\phi(x)}, 1\right\}$$

> ✔ Verified: With π(x)=φ(x)h(x) and proposal q(x,y)=h(y) (an independence chain), the MH ratio equals φ(y)/φ(x), so α(x,y)=min{φ(y)/φ(x), 1}.

This is a Metropolis sampler with an independence chain.

(4) Suppose $q(x,y) = \pi(y|x)$, the conditional density of $y$ given $x$, and $q(y,x) = \pi(x|y)$, the conditional density of $x$ given $y$. Then,

### PDF page 124 (booklet page 119)

$$\alpha(x,y) = \min\left\{1, \frac{\pi(y)q(y,x)}{\pi(x)q(x,y)}\right\} \tag{11.1}$$

$$= \min\left\{1, \frac{\pi(y)\pi(x|y)}{\pi(x)\pi(y|x)}\right\} \tag{11.2}$$

$$= \min\left\{1, \frac{\pi(x,y)}{\pi(x,y)}\right\} \tag{11.3}$$

$$= 1 \tag{11.4}$$

> ✔ Verified: With the Gibbs proposal $q(x,y)=\pi(y|x)$ (so $q(y,x)=\pi(x|y)$), the M-H acceptance ratio $\pi(y)\pi(x|y)/[\pi(x)\pi(y|x)]$ reduces to $\pi(x,y)/\pi(x,y)=1$, hence $\alpha(x,y)=1$.

Where $\pi(x,y) = \pi(y)\pi(x|y) = \pi(x)\pi(y|x)$ is the joint density of $x$ and $y$. Then, the M-H sampler moves with probability one, and the M-H sampler is the Gibbs sampler.

(5) Suppose $q(x,y) = g(x-y)$ (i.e., the proposed value $y = x+z$ where $z$ has pdf $g(.)$.). This is a random walk chain. A simple example is $y|x \sim Normal(x,\sigma^2)$.

> ✔ Verified: For the random walk chain, if $z$ has pdf $g$ = the $Normal(0,\sigma^2)$ density and $y = x + z$, then $q(x,y) = g(x-y)$ coincides with the $Normal(x,\sigma^2)$ density in $y$; the proposal is also symmetric, $q(x,y)=q(y,x)$.

Pratical [sic] Issues

(1) Product of kernels principle

Suppose $x = (x_1, x_2)$ and a sample from $\pi(x)$ is required. Let $\pi(x_1|x_2)$ and $\pi(x_2|x_1)$ be the conditional densities.

*(The booklet writes $x$, $x_1$, $x_2$ with under-tildes to indicate vectors.)*

a. For each $x_1$ draw from $\pi(x_2|x_1)$ until convergence. Iterate the procedure.

b. Draw $x_1$ from $\pi(x_1|x_2)$ and $x_2$ from $\pi(x_2|x_1)$ iteratively until convergence.

(a) is prohibitively expensive and (b) is easy (cheap). In fact (b) is the product of kernels principle. *(correction: the printed word is "kernel"; a handwritten "s" is added at the line end, giving "kernels")* This is enormously important in practice.

(2) Transient stage

A state is transient if the chain will never reenter that state. *(there are two small handwritten marks above this line — one over "reenter", one over "The value": [illegible])* The value at the beginning of the chain are transient.

The draws are regarded as a sample from the target density $\pi(x)$. *(a handwritten slash is drawn after "$\pi(x)$" and another through the "O" of "Only")* Only after the chain has passed the transient stage and the effect of the starting value $x_0$ is ignorable.

As in the Gibbs sampler, an assessment is made by the trace plots. That is, plot $x$ versus its order in the process.

(3) Tuning the M-H sampler

To obtain a random sampler from the M-H sampler after it has gone through the transient stage, we must tuning [sic] it. This is typically a difficult task, obtained by experiment and tested and error [sic: "trial and error"]. By tuning the sampler we can accomplished [sic] two things:

a. Jumping rate

We need to bring the jumping rate down to a value between 25% and 50% *[the line is hand-underlined]* *[margin note: "25 – 75 %" (?) — the second figure is doubtful, possibly "35"]*

b. Autocorrelation

We need to remove the autocorrelation among the iterates: thinning alone may not help. High autocorrelations indicate that the sampler is not working effectively (i.e., the presumed sample is not from $\pi(x)$).

Both (a) and (b) indicate that a better proposal density $q(x,y)$ is needed.

### PDF page 125 (booklet page 120)

**11.3 Spread of the proposal density**

The spread of the proposal density is created [sic] in its performance. *(a hand-drawn caret sits over "created", marking the word as wrong; no replacement is written)*
a. Large spread
Some of the proposed values will be far from the current value. For example, if the current value is the mode, the proposed value could be far away. This will make the ratio of the ordinates small, and consequently the jumping rate low.
b. Small spread
The proposed values will be closed [sic] to the current value. This will impede the chain from moving freely across the support of the target density, and there will be too few samples from regions far from the current value. We need the night [sic] spread of the proposal density.
Choice of candidate generating(proposal) density
Generally, the target density is unimodal, and a normal approximation becomes useful. The mode of target density (Nelder-Mead algorithm) and the negative of the inverse-Hessian matrix (at the mode) can be obtained. So that *[a long hand-drawn line, hooked in the left margin, runs across the whole first line of this sentence — emphasis, not a deletion]*

$$X \overset{\text{app}}{\sim} Normal\{m, \textstyle\sum\}$$

*[margin note, right of the display: "Laplace Approximation"]*

*(The booklet writes $X$, $m$, $\beta$ with under-tildes to indicate vectors.)*

where $m$ is the mode and $\sum$ the covatiance [sic] matrix(i.e.,-inverse-Hessian).
There are two approaches
a. $X \sim$ Normal $(m, k \sum)$ and
b. $X\mid\sigma^2 \sim$ Normal $(m, \sigma^2 \sum)$
$\dfrac{\nu\lambda}{\sigma^2} \sim \chi^2_\nu$, Chi-square on $\nu$ degree of freedom, i.e., $X \sim$ Student's t.

> ✔ Verified: Scale-mixture statement — with $\nu\lambda/\sigma^2\sim\chi^2_\nu$, the marginal of $X\mid\sigma^2\sim N(0,\sigma^2)$ is Student's $t_\nu$ with scale $\sqrt{\lambda}$ (checked exactly at $\nu=3,\lambda=1$)

Here $k, \nu, \lambda$ are tuning constants.
Otherwise, use importance function as proposal densities(i.e., tails of proposal dominate the target).

*[Handwritten note in the gap above the next section heading, two lines, partly legible: "Generalized Linear Model" on the first line; the second line runs from the left margin (entered by a hand-drawn arrow) to mid-page and is closed by a hand-drawn bracket — it is largely `[illegible]`, apparently ending in "… random variables" (?). To the right of it a heavy scribble obliterates a further mark, whose content cannot be recovered. These appear to be lecture notes positioning the following example as a GLM with random effects.]*

**11.4 Example I. Logistic regression model**

$$y_{ij}\mid\beta,\nu_i \sim \text{Bernoulli}\left(\frac{e^{x_{ij}'\beta+\nu_i}}{1+e^{x_{ij}'\beta+\nu_i}}\right), j = 1,\dots,n_i,\dots,N_i \quad i = 1,\dots l$$

*(correction: the printed numerator reads $e^{x_{ij}'\beta}$; a handwritten caret inserts "$+\nu_i$" into the exponent, matching the denominator)*

$$\nu_i\mid\sigma^2 \sim N\left(0,\sigma^2\right)$$

$$\pi\left(\beta,\sigma^2\right) \propto \frac{1}{(1+\sigma^2)^2}$$

*[margin note, right of the prior: "or" — "half Cauchy prior"; below it: "Better not use prior like(?) $\frac{1}{\sigma}$"]*

Need design matrix to be full rank.

### PDF page 126 (booklet page 121)

$$\pi\left(\nu,\beta,\sigma^2\mid y\right) \propto \prod_{i=1}^{l}\prod_{j=1}^{n_i}\left[\frac{e^{x_{ij}'\beta+\nu_i}}{1+e^{x_{ij}'\beta+\nu_i}}\right]^{y_{ij}}\left[\frac{1}{1+e^{x_{ij}'\beta+\nu_i}}\right]^{1-y_{ij}}\;\prod_{i=1}^{l}\left[\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{\nu_i^2}{2\sigma^2}}\right]\times\frac{1}{\left(1+\sigma^2\right)^2}$$

$$=\prod_{i=1}^{l}\left[\frac{e^{\sum_{j=1}^{n_i}x_{ij}'y_{ij}\beta+\Sigma\,\nu_i y_{ij}}}{\prod_{j=1}^{n_i}\left(1+e^{x_{ij}'\beta+\nu_i}\right)}\cdot\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{\nu_i^2}{2\sigma^2}}\right]\frac{1}{\left(1+\sigma^2\right)^2}$$

> ✔ Verified: The Bernoulli logit product collapses to a single exponential over a product of logit denominators.

$$=\prod_{i=1}^{l}\left[\frac{e^{a_i'\beta+b_i\nu_i}}{\prod_{j=1}^{n_i}\left(1+e^{x_{ij}'\beta+\nu_i}\right)}\cdot\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{\nu_i^2}{2\sigma^2}}\right]\frac{1}{\left(1+\sigma^2\right)^2}$$

> ✔ Verified: With a_i = sum_j y_ij x_ij and b_i = sum_j y_ij, the exponent equals a_i'beta + b_i nu_i.

where, $a_i=\sum_{j=1}^{n_i}y_{ij}x_{ij},\qquad b_i=\sum_{j=1}^{n_i}y_{ij}$

Need a Metropolis-Hastings Sampler:

$$\beta\mid\nu,\sigma^2,y$$

$$\nu_i\mid\beta,\sigma^2,y$$

*[a faint hand tick(?) in the left margin beside this line]*

$$\sigma^2\mid\nu,\beta,y$$

Integrate out $\nu_i$ numerically,
Let $z=\frac{\nu_i}{\sigma}$,

$$\propto\frac{1}{\left(1+\sigma^2\right)^2}\prod_{i=1}^{l}\left[\int_{-\infty}^{+\infty}\frac{e^{a_i'\beta+b_i\nu_i}}{\prod_{j=1}^{n_i}\left(1+e^{x_{ij}'\beta+\nu_i}\right)}\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{\nu_i^2}{2\sigma^2}}\,d\nu_i\right]$$

$$\propto\frac{1}{\left(1+\sigma^2\right)^2}\prod_{i=1}^{l}\left[\int_{-\infty}^{+\infty}\frac{e^{a_i'\beta+b_i\sigma z}}{\prod_{j=1}^{n_i}\left(1+e^{x_{ij}'\beta+\sigma z}\right)}\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}\,dz\right]$$

> ⚠ Check FAILED: The substitution z = nu/sigma turns the N(0, sigma^2) density integral into a standard-normal integral. — the stated result did not reproduce (see verification log)

$$\propto\frac{1}{\left(1+\sigma^2\right)^2}\prod_{i=1}^{l}\sum_{r=1}^{R}\left[\frac{e^{a_i'\beta+\sigma b_i\bar{a}_r}}{1+e^{x_{ij}'\beta+\sigma\bar{a}_r}}\right]\left[\Phi\left(a_r\right)-\Phi\left(a_{r-1}\right)\right]$$

$\text{[sic: the denominator has lost the product }\prod_{j=1}^{n_i}\text{ but retains the free index } j \text{ in } x_{ij}'\text{]}$

> ✔ Verified: The weights Phi(a_r) - Phi(a_{r-1}) telescope and sum to 1 over the full real line.

$$\propto\pi\left(\beta,\sigma^2\mid y\right)$$

where, $\bar{a}_r=\frac{a_r+a_{r-1}}{2}$

### PDF page 127 (booklet page 122)

*[Handwritten scratch notes are crowded across the top of the page, over the running header, and down the right margin. Best-effort reading, partly legible: $\prod_i \left\{ \int \prod_j \Phi(\cdot)^{y_{ij}}\big(1-\Phi(\cdot)\big)^{1-y_{ij}} \right\}$ (?) at the top; then, beside and below the Bernoulli display, $\nu_i \sim N(0,\sigma_\nu^2)$ (?), $f(\nu)$ (?), and $y_{ij} \sim \text{Bern}\{\Phi(x'_{ij}\beta)\}$; then, in the right margin, $\prod_i \left\{ \prod_j \big[ I(y_{ij}=1,\, z_{ij}>0) + I(y_{ij}=0,\, z_{ij}<0) \big] \right\}$ (?), $N(x'_{ij}\beta,\, 1)$ (?), and $\pi(\beta)$. These are lecture scratch notes for the Albert–Chib latent-variable augmentation of the probit model: integrating $\nu_i$ out of the marginal likelihood, and the augmented joint density in which $z_{ij} \sim N(x'_{ij}\beta, 1)$ and $y_{ij} = I(z_{ij} > 0)$.]*

**Generalized Linear Model:**

$$y_{ij}\mid \beta, \nu_i \sim \text{ Bernoulli}\left\{ F\left( x'_{ij}\beta + \nu_i \right) \right\}$$

*(The booklet writes $\beta$ with an under-tilde to indicate a vector.)*

$F(\cdot) = \Phi(\cdot)$, link function

By introducing latent variable, we can simplify the computation.
(e.g. Albent [sic] and Chib (1993) JASA)

## 11.5 Example II. Poisson regression model

We have data on chronic *(correction: a handwritten "c" is inserted above the word)* obstructive pulmonary disease for 778 health service areas in the continental US, collected 1988-1992. We choose white males, age 55-64 years.
For the $i^{th}$ HSA, $i = 1, ..., l = 798$ we have
deaths: $d_i$
population: $n_i$

*[sic: the text says 778 health service areas but then sets $l = 798$.]*

$$\textit{covariates} : x_{0i} \equiv 1$$

| | |
|---|---|
| $x_{1i}:$ | white male lung cancer rate |
| $x_{2i}:$ | population density |
| $x_{3i}:$ | elevation |
| $x_{4i}:$ | rain fall |

$x_i = (x_{0i}, x_{1i}, x_{2i}, x_{3i}, x_{4i})'_{p\times 1},\ p = 5$ Objectives:

> ✔ Verified: the covariate vector $x_i=(x_{0i},x_{1i},x_{2i},x_{3i},x_{4i})'$ is $p\times 1$ with $p=5$

a. Relate mortality to covatiates [sic].
b. Map the smooth rates.

Model

*[a hand-drawn downward arrow "↓" points at the model below]*

*[margin note, left of "Model": "Generalize(?) Poisson" written above a heavily struck-through, illegible word]*

$$d_i \mid \lambda_i \; ind \; \text{Poisson}(n_i \lambda_i),\, i = 1, ..., \ell$$

$$\lambda_i \mid \alpha, \beta \; ind \; \text{Gamma}\left(\alpha,\, \alpha e^{-x'_i \beta}\right)$$

*Christiansen and Morris (JASA,1997)*

$$p(\beta) = 1,\, p(\alpha) = \frac{1}{(1+\alpha)^2},\, \alpha > 0$$

> ✔ Verified: $p(\alpha)=1/(1+\alpha)^2$ integrates to 1 over $\alpha>0$ (proper prior)

### PDF page 128 (booklet page 123)

Note: This is not a standard generalized linear model. First two stages in the model are conjugate; inference about the $\lambda_i$ is straight forward.

*[the words "not a standard" are struck through/underlined by hand, emphasizing the negation]*

Joint posterior density

$$\pi(\lambda,\alpha,\beta\mid d) \propto \prod_{i=1}^{\ell}\left\{\frac{(n\lambda_i)^{d_i}e^{-n_i\lambda_i}}{d_i!}\;\frac{(\alpha e^{-x_i'\beta})^{\alpha}\lambda_i^{\alpha-1}e^{-\lambda_i\alpha e^{-x_i'\beta}}}{\Gamma(\alpha)}\right\}\times\frac{1}{(1+\alpha)^2}$$

*(The booklet writes $\lambda$, $\beta$, $d$, $x_i$, $\nu$ with under-tildes to indicate vectors.)*

Fitting the model(Metropolis-Hastings sampler)

$$\lambda_i\mid\alpha,\beta,d \overset{ind}{\sim} \text{Gamma}(d_i+\alpha,\; n_i+\alpha e^{-x_i'\beta})$$

*[handwritten mark over the "$\overset{ind}{\sim}$" symbol, reading "$\gamma^{*}$"(?), with a hand-drawn curl looping back to the conditioning list; apparently emphasizing the conditional independence of the $\lambda_i$]*

> ✔ Verified: The $\lambda_i$-dependent factors of the joint posterior form the kernel of Gamma$(d_i+\alpha,\ n_i+\alpha e^{-x_i'\beta})$ (shape/rate).

$$\pi(\alpha,\beta\mid\lambda,d) \propto \left[\prod_{i=1}^{\ell}\left\{\frac{(\alpha e^{-x_i'\beta})^{\alpha}\lambda_i^{\alpha-1}e^{-\lambda_i\alpha e^{-x_i'\beta}}}{\Gamma(\alpha)}\right\}\right]\times\frac{1}{(1+\alpha)^2}$$

Construction of proposal density $\pi_a(\alpha,\beta\mid\lambda,d)$.

$$\Delta(\alpha,\beta) = \ell\alpha log\alpha - \ell log\Gamma(\alpha) - 2log(1+\alpha) - \alpha\Big\{\sum_{i=1}^{\ell}x_i'\Big\}\beta + (\alpha-1)\sum_{i=1}^{\ell}log\lambda_i - \alpha\sum_{i=1}^{\ell}\lambda_i e^{-x_i'\beta}$$

> ✔ Verified: $\Delta(\alpha,\beta) = \log\pi(\alpha,\beta\mid\lambda,d)$ kernel, i.e. the log of $\prod_i (\alpha e^{-x_i'\beta})^\alpha\lambda_i^{\alpha-1}e^{-\lambda_i\alpha e^{-x_i'\beta}}/\Gamma(\alpha)\times(1+\alpha)^{-2}$.

Two steps:

a. Optimize $\Delta(\alpha,\beta)$ (Nelder-Mead algorithm); mode is as at $(\hat\alpha,\hat\beta)$.

b. Obtain the Hessian matrix at $(\hat\alpha,\hat\beta)$, denoted by $H$.

Approximate posterior density

$$\begin{bmatrix}\alpha\\\beta\end{bmatrix}\Bigg|\lambda,d \sim Normal\left\{\begin{bmatrix}\alpha\\\beta\end{bmatrix},\begin{bmatrix}\sigma^2 & \nu'\\ \nu & \Delta\end{bmatrix}\right\}$$

where

$$\begin{bmatrix}\sigma^2 & \nu'\\ \nu & \Delta\end{bmatrix} = k(-H^{-1})$$

with $k$ a tuning constant.

$$\pi_a(\alpha,\beta\mid\lambda,d) = g_a(\alpha\mid\beta,\lambda,d)\,h_a(\beta\mid\lambda,d)$$

where $g_a(\alpha\mid\beta,\lambda,d)$ and $h_a(\beta\mid\lambda,d)$ are to be determined.

$$\beta\mid\lambda,d \sim \text{Normal}\{\hat\beta,\Delta\} : h_a(\beta\mid\lambda,d)$$

$$\alpha\mid\beta,\lambda,d \sim \text{Normal}\{\hat\alpha+\nu'\Delta^{-1}(\beta-\hat\beta),\;\sigma^2-\nu'\Delta^{-1}\nu\}$$

> ✔ Verified: Partitioned-Normal conditional: $\alpha\mid\beta \sim N(\hat\alpha+\nu'\Delta^{-1}(\beta-\hat\beta),\ \sigma^2-\nu'\Delta^{-1}\nu)$.

### PDF page 129 (booklet page 124)

Instead take

$$\alpha\mid\beta,\lambda,d \sim \text{Gamma}(a,b),\; (g_a(\alpha\mid\beta,\lambda,d))$$

where

$$\frac{a}{b} = \hat{\alpha} + \nu'\Delta^{-1}(\beta - \hat{\beta});\quad \frac{a}{b^2} = \sigma^2 - \nu'\Delta^{-1}\nu$$

Thus, we obtain a Metropolis step for $\alpha,\beta\mid\lambda,d$

Letting

$$\phi(\alpha,\beta) = \frac{\pi(\alpha,\beta\mid\lambda,d)}{\pi_a(\alpha,\beta\mid\lambda,d)}$$

The jumping probability is

$$a_{1,2} = \min\left\{1, \frac{\phi(\alpha^{(2)},\beta^{(2)})}{\phi(\alpha^{(1)},\beta^{(1)})}\right\}$$

Metropolis-Hastings sampler

a. Draw $\lambda_i$ from $\lambda_i\mid\alpha,\beta,\alpha$ (?) $, i = 1,...,\ell.$ *(sic: the third conditioning symbol is printed as $\alpha$ with an under-tilde; from context it should be the data vector $d$)*

b. Draw $\alpha,\beta$ from $\alpha,\beta\mid\lambda,d$, (product of kernels principle).

Tuning is obtaind [sic] by varying the value of $k$. In situations where $k$ is an inflation factor for the variance obtained from the Hessian matrix, start with $k=2$.

How to obtain starting values?

$$\hat{\lambda}_i = \begin{cases} \dfrac{d_i}{n_i}, & d_i > 0 \\[2ex] \dfrac{\bar{d}}{n_i}, & d_i = 0 \end{cases}$$

$\bar{d} = \ell^{-1}\sum_{i=1}^{\ell} d_i$. Here we use $d_i \sim \text{Poisson}(n_i\lambda_i), i = 1,...,\ell.$

$$\lambda_i \; ind \; \text{Gamma}(\alpha, \alpha e^{-x_i'\beta})$$

*(sic: the "$\sim$" is missing — the source typesets only "$ind$" between $\lambda_i$ and Gamma; read as $\lambda_i \overset{ind}{\sim} \text{Gamma}(\alpha, \alpha e^{-x_i'\beta})$)*

$$[CV(\lambda_i)]^2 = \frac{Var(\lambda_i)}{[E(\lambda_i)]^2} = \alpha$$

> ⚠ Check FAILED: For a Gamma with shape $\alpha$ and rate $\alpha e^{-x'\beta}$ (the parameterization implied by mean $=a/b$, variance $=a/b^2$), the squared coefficient of variation $Var/E^2$ equals $\alpha$ as the page prints. — the stated result did not reproduce (see verification log)

$$\bar{x}_\lambda = \ell^{-1}\sum_{i=1}^{\ell}\hat{\lambda}_i;\; s_\lambda^2 = (\ell-1)^{-1}\sum_{i=1}^{\ell}(\hat{\lambda}_i - \bar{x}_\lambda)^2;\; \hat{\alpha} = \frac{s_\lambda^2}{\bar{x}_\lambda}$$

Pretend

$$\log(\hat{\lambda}_i) = -x_i'\beta + e_i,\; e_i \; ind \; N\!\left(0, \frac{1}{n_i\hat{\lambda}_i}\right)$$

*(sic: again the "$\sim$" is missing before $N$; read as $e_i \overset{ind}{\sim} N(0, (n_i\hat{\lambda}_i)^{-1})$)*

> ✔ Verified: If $d_i\sim\text{Poisson}(n_i\lambda_i)$, the delta-method variance of $\log(d_i/n_i)$ is $1/(n_i\lambda_i)$, matching the printed $e_i\sim N(0,(n_i\hat\lambda_i)^{-1})$.

$\hat{\beta}$ is the weighted least square estimator of $\beta$.

Remark(Collapsing)

*[a faint hand-drawn stroke/underline runs beneath this line; no legible text]*

### PDF page 130 (booklet page 125)

It is easy to write the joint posterior density as

$$\pi(\lambda,\alpha,\beta) \propto \left\{\prod_{i=1}^{\ell}\left[\frac{\alpha e^{-x_i'\beta}}{n_i+\alpha e^{-x_i'\beta}}\right]^{\alpha}\left[\frac{n_i}{n_i+\alpha e^{-x_i'\beta}}\right]^{d_i}\right.$$

$$\left.\times\frac{(n_i+\alpha e^{-x_i'\beta})^{\alpha+d_i}\lambda^{\alpha+d_i-1}e^{-(n_i+\alpha e^{-x_i'\beta})\lambda_i}}{\Gamma(\alpha+d_i)}\right\}$$

$$\times\frac{1}{(1+\alpha)^2}$$

*(The booklet writes $\lambda$, $\beta$, $d$ and $x_i$ with under-tildes to indicate vectors.)*
*[sic: the numerator carries $\lambda^{\alpha+d_i-1}$ without the subscript $i$, while the exponent has $\lambda_i$ — it should be $\lambda_i^{\alpha+d_i-1}$.]*

So $\pi(\alpha,\beta\mid d) = \int \pi(\lambda,\alpha,\beta)d\lambda$

And

$$\pi(\alpha,\beta\mid d) \propto \left\{\prod_{i=1}^{\ell}\left[\frac{\alpha e^{-x_i'\beta}}{n_i+\alpha e^{-x_i'\beta}}\right]^{\alpha}\left[\frac{n_i}{n_i+\alpha e^{-x_i'\beta}}\right]^{d_i}\right\}\frac{1}{(1+\alpha)^2}$$

*[margin note, right of this display, dark pen, largely illegible: "It [is] the … [joint(?)] the … to be … $(\beta,\alpha)\mid d)$ … [a(?)] marginal density" — apparently noting that integrating $\lambda$ out leaves the marginal posterior density of $(\alpha,\beta)$ given $d$. Several words are [illegible].]*

> ✔ Verified: The Gamma factor in the joint posterior integrates to 1 over $\lambda_i\in(0,\infty)$, so deleting it yields the stated marginal $\pi(\alpha,\beta\mid d)$.

We can now use just the Metropolis sampler, than the more general Metropolis-Hasting sam-
*[hand mark: a short dash in the left margin beside this turned line]* pler.

$$\pi(\lambda_i\mid\alpha,\beta,d)\,ind\,\text{Gamma}(d_i+\alpha,\;n_i+\alpha e^{-x_i'\beta})$$

*[sic: the booklet prints the italic "ind" with no relation symbol; it should read $\overset{ind}{\sim}$.]*

## 11.6 Rao-Blackwellized estimator

We can obtain iterates $(\alpha^{(h)},\beta^{(h)}), h=1,...,M=1000$ from the M-H sampler.

$$\pi(\lambda_i\mid\alpha,\beta,d)\,ind\,\text{Gamma}(d_i+\alpha,\;n_i+\alpha e^{-x_i'\beta}),\, i=1,...,\ell=798.$$

An estimator of the posterior density is

$$\widehat{\pi(\lambda\mid\alpha)} = M^{-1}\sum_{h=1}^{M}\left\{\frac{(n_i+\alpha e^{-x_i'\beta})^{\alpha+d_i}\lambda^{\alpha+d_i-1}e^{-(n_i+\alpha e^{-x_i'\beta})\lambda_i}}{\Gamma(\alpha+d_i)}\right\}_{(\alpha,\beta)=(\alpha^{(h)},\beta^{(h)})}$$

And the posterior mean is

$$\widehat{E(\lambda_i\mid d)} = M^{-1}\sum_{h=1}^{M}\left[\frac{d_i+\alpha^{(h)}}{n_i+\alpha^{(h)}e^{-x_i'\beta^{(h)}}}\right],\, i=1,...,\ell.$$

> ✔ Verified: The Rao-Blackwellized posterior-mean summand $(d_i+\alpha)/(n_i+\alpha e^{-x_i'\beta})$ equals $E[\lambda_i]$ for $\lambda_i\sim\text{Gamma}(d_i+\alpha,\,n_i+\alpha e^{-x_i'\beta})$ (shape, rate).

### PDF page 131 (booklet page 126)

**11.7 Tuning the Metropolis step**

How to choose $k$?

| $k$ | Jumping rate |
|---|---|
| 5 | 0.011 |
| 3 | 0.028 |
| 2.5 | 0.058 |
| 2.0 | 0.115 |
| 1.8 | 0.151 |
| 1.6 | 0.195 |
| 1.5 | 0.251 |
| 1.4 | 0.314 |
| 1.3 | 0.399 |
| 1.25 | 0.493 |
| 1.18 | 0.600 |
| 1.11 | 0.717 |
| 1.00 | 0.914 |

> ✔ Verified: The jumping rate in the tuning table is strictly decreasing in $k$.

Sample autocorrelation coefficients(ACF's)

| Runs | 2000 | | 6000 | | 11000 | |
|---|---|---|---|---|---|---|
| **Skip** | 1 | | 5 | | 10 | |
| **Lag** | $\alpha$ | $\beta_0$ | $\alpha$ | $\beta_0$ | $\alpha$ | $\beta_0$ |
| 1 | 0.764 | 0.588 | 0.305 | $-$0.040 | 0.130 | 0.043 |
| 2 | 0.509 | 0.282 | 0.149 | 0.050 | $-$0.071 | $-$0.105 |
| 3 | 0.406 | 0.137 | 0.143 | 0.139 | $-$0.026 | 0.010 |
| 4 | 0.293 | 0.037 | $-$0.043 | $-$0.095 | $-$0.012 | $-$0.008 |

A "burn in" of 1000 in each case is used.
The standard error for the sample ACF's are in the range $0.031 - 0.032$

> ✔ Verified: Each (Runs, Skip) setting yields 1000 retained draws after a burn-in of 1000, and the resulting ACF standard error 1/sqrt(1000) falls in the printed range 0.031–0.032.

Posterior means(PM), posterior standard deviations(PSD), numerical standard error(NSE) and 95% credible intervals(CI) for the regression coefficients.

| | PM | PSD | NSE | CI |
|---|---|---|---|---|
| Interecpt [sic] | -8.339 | 0.066 | 0.032 | (-8.476, -8.208) |
| WMLC Ratio | 0.016 | 0.001 | 0.000 | (0.014, 0.017) |
| Population Density | -0.409 | 0.061 | 0.018 | (-0.534, -0.281) |
| Elevation | 0.006 | 0.001 | 0.000 | (0.005, 0.008) |
| Annual Rainfall | -0/141 $\text{[sic: should read }-0.141\text{]}$ | 0.085 | 0.034 | (-0.310, 0.025) |

*[In the row label column: a small hooked hand mark sits against "Interecpt" (?), apparently flagging the transposed letters; "Ratio" in the next row appears to carry a short hand underline (?). Both marks are faint and the readings are uncertain.]*

> ✔ Verified: Every posterior mean lies strictly inside its reported 95% credible interval, including the Annual Rainfall entry read as -0.141.

### PDF page 132 (booklet page 127)

**11.8 Reversible Jump Markov chain Monte Carlo Sampler**

Green,P.J.(1995), Reversible jumping [sic] Markov chain Monte Carlo computation and Bayesian model determination, Biometrika 82, 711-732.

Have many competing models with different parameter spaces(e.g., dimensions). There is uncertainty about the model itself, creating a parameter which indexes the model. All models are fit simultaneously, and the reversible jump sampler jumps over models.

There are four components

1. Indicidual [sic] models

$$y \mid \theta_s \sim f(y \mid \theta_s, M_s)$$

$$\pi(\theta_s \mid M_s)$$

$s = 1, ..., k$ for $k$ distinct models.

*(The booklet writes $y$, $\theta$ and $u$ with under-tildes to indicate vectors.)*

2. Prior probabilities

$$P(M_s) = w_s, s = 1, ..., k$$

All prior densities must be proper

$$P(M_s \mid y) = \frac{w_s \pi(\theta_s \mid M_s) f(y \mid \theta_s, M_s)}{\sum_{r=1}^{k} w_k \int \pi(\theta_s \mid M_s) f(y \mid \theta_s, M_s) d\theta_r}, s = 1, ..., k$$

$\text{[sic: the denominator's weight should be } w_r \text{ and its integrand } \pi(\theta_r \mid M_r) f(y \mid \theta_r, M_r)\text{, to match the differential } d\theta_r\text{]}$

> ✔ Verified: The posterior model probabilities $w_s m_s(y)/\sum_r w_r m_r(y)$ sum to 1 over $s=1,\dots,k$.

$$P(M_S \mid y) = \max P(M_s \mid y), s = 1, ..., k.$$

$M_S$ is the selected model(Model selection)

$$\pi(y^{(p)} \mid y) = \sum_{s=1}^{k} \pi(y^{(p)} \mid y, M_s) P(M_s \mid y); \; \text{predicted } y^{(p)}.$$

> ⚠ Check FAILED: The posterior predictive $\pi(y^{(p)}\mid y)=\sum_s \pi(y^{(p)}\mid y,M_s)P(M_s\mid y)$ integrates to 1 when each component does. — the stated result did not reproduce (see verification log)

3. Transition probabilities

$$P(M_s \mid M_r) = \pi_{rs}; \sum_{s=1}^{k} \pi_{rs} = 1; r = 1, ..., k.$$

These are not a part of the model specifications, but are chosen to provide good moves.

4. Dimension-matching condition

An elegant idea of Green(1995) is to match the dimension of the two model [sic] under consideration.

Suppose $dim(\theta_s) > dim(\theta_r)$. Introduce $(s-r)$ latent variables into $M_r$ to match the dimension of $M_s$, say $u = (u_1, ..., u_{s-r})$. We need a bijection:

$$\theta_s = A \begin{bmatrix} \theta_r \\ u \end{bmatrix}; \quad \begin{bmatrix} \theta_r \\ u \end{bmatrix} = A^{-1} \theta_s$$

> ✔ Verified: $\theta_s = A[\theta_r; u]$ if and only if $[\theta_r; u] = A^{-1}\theta_s$, for invertible $A$ (dimension-matching bijection).

### PDF page 133 (booklet page 128)

Acceptance probability

Let

$$R = \frac{P(M_r, \theta_r \mid y)\,\pi_{r,s}\,q(u)}{P(M_s, \theta_s \mid y)\,\pi_{s,r}}\;\left|\frac{\partial(\theta_r, u)}{\partial \theta_s}\right|$$

*(The booklet writes $\theta_r$, $\theta_s$, $u$, $y$ and $\beta$ with under-tildes to indicate vectors.)*

Where $\left|\dfrac{\partial(\theta_r, u)}{\partial \theta_s}\right|$ is the absolute value of the Jacobian of the bijection.

Then, the acceptance probability for the move $s \to r$ is $a_{s,r} = \min(1, R)$, where draws are made from $\pi(\theta_s \mid y, M_s)$ and transformed to $(\theta_r, u)$. Similarly, the acceptance probability for the move $r \to s$ is $a_{r,s} = \min(1, R^{-1})$, where draws are made from $\pi(\theta_r \mid y, M_r) q(u)$ and transformed to $\theta_s$.

Simple example

$M1$:

$$y_1, ..., y_r \mid \alpha, \sigma^2 \overset{iid}{\sim} \text{Normal}(\alpha, \sigma^2)$$

*(In the scan the "iid" is typeset with its tilde sitting under the final "d" rather than beneath the whole symbol — a compilation artifact of `\overset{iid}{\sim}`. Same for "ind" in $M2$ below.)*

$$\alpha \sim \text{Normal}(\alpha_0, \sigma_0^2), \quad \sigma^{-2} \sim \text{Gamma}\left(\frac{a}{2}, \frac{b}{2}\right)$$

$M2$:

$$y_1, ..., y_r \mid \beta_0, \beta_1, \delta^2 \overset{ind}{\sim} \text{Normal}(\beta_0 + \beta_1 x_i, \delta^2)$$

$$\begin{bmatrix} \beta_1 \\ \beta_1 \end{bmatrix} \sim Normal\{\beta^{(\cdot)}, \triangle^{(\cdot)}\}, \quad \delta^{-2} \sim Gamma\left(\frac{c}{2}, \frac{d}{2}\right)$$

*(the first entry of the vector is printed $\beta_1$ [sic] — it should be $\beta_0$ to match the regression model above)*

$$w_1 = 0.25 = 1 - w_2$$

> ✔ Verified: $w_1 = 0.25 = 1 - w_2$ implies $w_2 = 0.75$ and $w_1 + w_2 = 1$

$$\pi_{11} = 0.60 = 1 - \pi_{12}; \quad \pi_{21} = 0.20 = 1 - \pi_{22}$$

> ✔ Verified: $\pi_{11} = 0.60$, $\pi_{21} = 0.20$ imply $\pi_{12} = 0.40$, $\pi_{22} = 0.80$, rows summing to 1

To satisfy the dimension-matching condition, we need to add one latent variable, say $u$, to $M1$.

What should $u$ be?

Consider $M2$ without the priors.

$$\begin{bmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{bmatrix} \sim Normal\left\{\begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix}, \sigma^2 (x'x)^{-1}\right\}; \quad x = \begin{bmatrix} 1 & x_1 \\ \vdots & \\ n & x_n \end{bmatrix}$$

*(the first column of $x$ is printed $1, \vdots, n$ [sic] — it should be a column of ones, $1, \vdots, 1$)*

> ✔ Verified: OLS in the simple linear model has mean $\beta$ and variance $\sigma^2 (x'x)^{-1}$

$$E(S^2) = \sigma^2; \quad S^2 \text{ is the } MSE$$

> ✔ Verified: $E(S^2) = \sigma^2$ for $S^2 = \text{RSS}/(n-2)$, i.e. $\operatorname{tr}(I - H) = n - 2$

Let $\hat{\sigma_1}^2$ denote the $(2,2)^{th}$ element of $S^2 (X'X)^{-1}$

Choose $u \sim \text{Normal}(\hat{\beta}_1, \hat{\sigma_1}^2)$

Bijection

$$\begin{bmatrix} \beta_0 \\ \beta_1 \\ \delta^2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \tau \end{bmatrix} \begin{bmatrix} \alpha \\ u \\ \sigma^2 \end{bmatrix}; \quad \begin{bmatrix} \alpha \\ u \\ \sigma^2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \tau^{-1} \end{bmatrix} \begin{bmatrix} \beta_0 \\ \beta_1 \\ \delta^2 \end{bmatrix}$$

*(the third entry of the right-hand vector in the first display and of the left-hand vector in the second display is hard to resolve in the scan: it is read as $\sigma^2$ (?), which is what makes the two matrices mutual inverses; both glyphs could also be read as $\delta^2$)*

> ✔ Verified: the bijection matrices are mutual inverses and the Jacobian has absolute value $\tau$

### PDF page 134 (booklet page 129)

Where $\tau$ is a tuning constant.

Acceptance probability

$$\pi(\alpha, u, \sigma^2 \mid y, M_1) \propto \left\{\prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{1}{2\sigma^2}(y_i-\alpha)^2}\right\} \frac{1}{\sqrt{2\pi\hat{\sigma_1}^2}} e^{-\frac{1}{2\hat{\sigma_1}^2}(u-\hat{\beta}_1)^2}$$

$$\times \frac{1}{\sqrt{2\pi\sigma_0^2}} e^{-\frac{1}{2\sigma_0^2}(\alpha-\alpha_0)^2} \left(\frac{b}{2}\right)^{\frac{a}{2}} \left(\frac{1}{\sigma^2}\right)^{\frac{a}{2}+1(?)} e^{-\frac{b}{2\sigma^2}} \Big/ \Gamma\frac{a}{2}$$

*(The booklet writes $y$ and $\beta$ with under-tildes to indicate vectors.)*

$$\pi(\beta_0, \beta_1, \delta^2 \mid y M_2) \propto \left\{\prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\delta^2}} e^{-\frac{1}{2\delta^2}(y_i-\beta_0-\beta_1 x_i)^2}\right\}$$

$\text{[sic: the conditioning list is printed "}\mid y M_2\text{" with no comma between } y \text{ and } M_2\text{]}$

$$\times \frac{1}{(2\pi)|\Delta_0|^{1/2}} e^{-\frac{1}{2}(\beta-\beta_0)'\Delta_1^{-1}(\beta-\beta_0)} \left(\frac{b}{2}\right)^{\frac{d}{2}(?)} \left(\frac{1}{\delta^2}\right)^{\frac{c}{2}+1} e^{-\frac{d}{2\delta^2}} \Big/ \Gamma\frac{c}{2}$$

$\text{[sic: the printed prefactor is }(2\pi)|\Delta_0|^{1/2}\text{, with no power on }2\pi\text{; the quadratic form pairs }\Delta_0\text{ in the determinant with }\Delta_1^{-1}\text{ in the exponent]}$

> ✔ Verified: The printed $\sigma^2$ prior factor $(b/2)^{a/2}(1/\sigma^2)^{a/2+1}e^{-b/(2\sigma^2)}/\Gamma(a/2)$ integrates to 1 over $\sigma^2 \in (0,\infty)$.

$$R = \frac{0.75 \times 0.20\, \pi(\beta_0, \beta_1, \delta^2 \mid y, M_2)\, \tau}{0.25 \times 0.40\, \pi(\alpha, u, \sigma^2 \mid y, M_1)}$$

> ✔ Verified: The numeric prefactor of $R$ equals $3/2$.

$$a_{1,2} = \min(1, R);\; a_{2,1} - \min(1, R^{-1})$$

$\text{[sic: the second relation is printed with a minus sign, "}a_{2,1} - \min(1,R^{-1})\text{"; it should read }a_{2,1} = \min(1,R^{-1})\text{]}$

*(The remainder of the page — roughly the lower two-thirds — is blank.)*

### PDF page 135 (booklet page 130)

*(This page has no typeset content below the running header — the entire body is the instructor's handwritten lecture notes on the Gelman–Rubin potential scale reduction diagnostic. Everything below is handwriting.)*

*[hand-underlined]* **Multiple runs**

*[hand-underlined]* 2-5 runs in parallel

*[hand-underlined]* Potential scale reduction (PSR) factor

use *different* pstarts *[the word "different" is hand-underlined]*

Run each the same(?) way, burn-in(?) etc.

*[Column headings, each with a vertical column of dots beneath, the first two hand-underlined:]*

$$\underline{\text{chain}(1,\cdot)} \qquad \underline{\text{chain}(2,\cdot)} \qquad \cdots \qquad \underline{\text{chain}(d)}$$

*[margin note, left: "Length of chain $M$"]*

[illegible — heavily overwritten symbol] $\qquad \bar{y}_j,\ s_j^2 \qquad\qquad j = 1,\dots,d$

$$\bar{y} = \frac{\sum_{j=1}^{d} \bar{y}_j}{d}$$

$$bss = M\,\frac{\sum_{j=1}^{d}\left(\bar{y}_j - \bar{y}\right)^2}{d-1}$$

$$wss = \frac{\sum_{j=1}^{d} s_j^2}{d}$$

*[margin note, left: "R calculates this for you — extra precaution"]*

$$psr = \sqrt{\left[\left(1 - \frac{1}{M}\right) wss + \frac{1}{M}\, bss\right] \Big/ wss}$$

*[A long hand-drawn pointer line runs from the left of this formula up to the right toward the circled note below.]*

*[right margin, beside the formula: "As $M \to \infty$"]*

> ✔ Verified: As $M \to \infty$, $psr = \sqrt{\big[(1-\tfrac{1}{M})\,wss + \tfrac{1}{M}\,bss\big]/wss} \to 1$ for fixed $bss \ge 0$ and $wss > 0$.

Want
$$\begin{cases} psr \approx 1.000 \\[4pt] Corr(\ \ ) \approx 1.000 \end{cases}$$

*[right margin, top of page — cramped, partly illegible: "$H_0$: all different starting pts [give the same] chains(?)  vs  $H_1$: different sty(?) pts [give] different results(?)". These are scratch notes framing convergence as a hypothesis test.]*

*[right margin, mid-page — best-effort reading: "For each parameter" ... "$\alpha,\ \beta,\ \sigma^2$"(?) ... "$> 0$" ... [heavily scribbled-out word] ... "posterior integral"(?)]*

*[right margin, mid-page: "$\pi(\alpha, \beta, \sigma^2 \mid \text{data})$"(?)]*

*[right margin, mid-page:]*
$$0 < \alpha < 20 \qquad \text{Draw 5 values } \ U(0,20)$$

*[right, lower: a hand-drawn circle enclosing "not quite normal"(?), with a long line drawn down-left toward the numbers below.]*

*[bottom of page, hand-written results:]*

<u>5 chains</u>

| | |
|---|---|
| | 0.99999 |
| | 1.00002 |
| | 0.99997 |

p-vals(?) *[the three values below are enclosed in a hand-drawn circle; the last is written over a scribble]*

| | |
|---|---|
| | .848 |
| | .3054 |
| | .9866 |

$$\left.\begin{matrix} .98 \\ 1.02 \end{matrix}\right\} \ \text{not good.}$$

— p-values will be affected

— use a nonparametric type(?) [test], e.g. Kruskal-Wallis    0.2830

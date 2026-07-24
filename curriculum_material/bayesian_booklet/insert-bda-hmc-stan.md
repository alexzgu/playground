# Reproduced excerpt — Gelman et al., *Bayesian Data Analysis*, pp. 300–309 (HMC and Stan)
*(PDF pages 179–188; source pages 300–309)*


### PDF page 179 (booklet page 300)

*(Editorial note: this page is not booklet-typeset material. It is a photocopy of page 300 of another text — the running header reads "COMPUTATIONALLY EFFICIENT MCMC" and the content is §12.4 of Gelman et al., *Bayesian Data Analysis* — inserted into the booklet and annotated by hand. The printed page number 300 is used in the heading above, per the convention of trusting the number printed on the page.)*

are simulated, one for each density $q_k$ in the ladder. Each chain moves on its own but with occasional flipping of states between chains, with a Metropolis accept-reject rule similar to that in simulated tempering. At convergence, the simulations from chain 0 represent draws from the target distribution.

Other auxiliary variable methods have been developed that are tailored to particular structures of multivariate distributions. For example, highly correlated variables such as arise in spatial statistics can be simulated using *multigrid sampling*, in which computations are done alternately on the original scale and on coarser scales that do not capture the local details of the target distribution but allow faster movement between states.

**Particle filtering, weighting, and genetic algorithms**

*Particle filtering* describes a class of simulation algorithms involving parallel chains, in which existing chains are periodically tested and allowed to die, live, or split, with the rule set up so that chains in lower-probability areas of the posterior distribution are more likely to die and those in higher-probability areas are more likely to split. The idea is that a large number of chains can explore the parameter space, with the birth/death/splitting steps allowing the ensemble of chains to more rapidly converge to the target distribution. The probabilities of the different steps are set up so that the stationary distribution of the entire process is the posterior distribution of interest.

A related idea is *weighting*, in which a simulation is performed that converges to a specified but wrong distribution, $g(\theta)$, and then the final draws are weighted by $p(\theta|y)/g(\theta)$. In more sophisticated implementations, this reweighting can be done throughout the simulation process. It can sometimes be difficult or expensive to sample from $p(\theta|y)$ and faster to work with a good approximation $g$ if available. Weighting can be combined with particle filtering by using the weights in the die/live/split probabilities.

*Genetic algorithms* are similar to particle filtering in having multiple chains that can live or die, but with the elaboration that the updating algorithms themselves can change ('mutate') and combine ('sexual reproduction'). Many of these ideas are borrowed from the numerical analysis literature on optimization but can also be effective in a posterior simulation setting in which the goal is to converge to a distribution rather than to a single best value. *[a hand-drawn wavy line runs under this line]* *[margin note, brace-enclosed, to the right: "posterior (any t(?) densities)"]*

*[a hand-drawn horizontal rule separates this section]*

*[hand-drawn star in the margin beside the section heading]* **12.4 Hamiltonian Monte Carlo** *[margin note, brace-enclosed, to the right of the heading: "Only continuous r.v.'s"]*

*[hand tick in the left margin]* An inherent inefficiency in the Gibbs sampler and Metropolis algorithm is their random walk behavior *[hand-underlined: "random walk behavior"]*—as illustrated in Figures 11.1 and 11.2 on pages 276 and 277, the simulations can take a long time zigging and zagging *[hand-underlined]* while moving through the target distribution. Reparameterization and efficient jumping rules *[hand-underlined]* can improve the situation (see Sections 12.1 and 12.2), *[margin note, left: "blocking"]* but for complicated models this local random walk behavior remains *[hand-underlined]*, especially for high-dimensional target distributions.

*Hamiltonian Monte Carlo* (HMC) borrows an idea from physics to suppress *[hand-underlined]* the local random walk behavior in the Metropolis algorithm *[hand-underlined]*, thus allowing it to move much more rapidly through the target distribution. For each component $\theta_j$ in the target space *[hand-underlined]*, Hamiltonian Monte Carlo adds a 'momentum' variable $\phi_j$ *[hand-underlined]*. *[margin note, left: "Momentum"]* Both $\theta$ and $\phi$ are then updated together in a new *[hand-underlined: "new"]* Metropolis algorithm, in which the jumping distribution for $\theta$ is determined largely by $\phi$ *[hand-underlined]*. Each iteration of HMC proceeds via several steps, during which the position and momentum evolve *[hand-underlined]* based on rules imitating the behavior of position the steps can move rapidly [sic: the photocopy drops text here — the source reads "...the behavior of position and momentum in a physical system in which particles move in a space with varying elevation. In these steps the simulations can move rapidly..."] where possible through the space of $\theta$ and even can turn corners in parameter space to preserve the total 'energy' of the trajectory. Hamiltonian Monte Carlo is also called *hybrid Monte Carlo* *[hand-underlined]* because it combines MCMC *[hand-underlined]* and deterministic simulation methods *[hand-underlined]*. *[a hand-drawn curved line sweeps beneath this line toward the next paragraph]*

In HMC, the posterior density $p(\theta|y)$ (which, as usual, needs only be computed up

### PDF page 180 (booklet page 301)

*(This page is not part of the MA 556 booklet's own typesetting: it is a photocopied handout of page 301 of another text, whose running header reads "HAMILTONIAN MONTE CARLO". The left quarter of the scan is the facing page (300) bleeding in past the gutter shadow; only truncated line fragments of it are legible — e.g. "…loves on its own but…", "…cept-reject rule simila…", "…parallel chains, in whic…", "…m is their random walk…", "…to is also called* hybrid*…" — and it is not transcribed here.)*

*(The page opens mid-sentence; the preceding words fall on the previous page.)*

…multiplicative constant) is augmented by an <u>independent distribution</u> *[hand-underlined]* $p(\phi)$ on the momenta, thus defining a joint distribution, $p(\theta,\phi\mid y) = p(\phi)p(\theta\mid y)$. We simulate from the joint distribution but we are only interested in the simulations of $\theta$; the vector $\phi$ is thus an auxiliary variable, <u>introduced only to enable the algorithm to move faster through the parameter space</u>. *[hand-underlined]* *[hand emphasis strokes in right margin]*

In addition to the posterior density (which, as usual, needs to be computed only up to a multiplicative constant), HMC also requires <u>the gradient of the log-posterior density</u> *[hand-underlined]*. In practice the gradient must be computed <u>analytically; numerical differentiation requires too many function evaluations</u> *[hand-underlined]* to be computationally effective. If $\theta$ has $d$ dimensions, this gradient is $\frac{d\log p(\theta\mid y)}{d\theta} = \left(\frac{d\log p(\theta\mid y)}{d\theta_1},\dots,\frac{d\log p(\theta\mid y)}{d\theta_d}\right)$. For most of the models we consider in this book, this vector is easy to determine analytically and then program. When writing and debugging the program, we recommend also programming the gradient numerically (using finite differences of the log-posterior density) <u>as a check on the programming of the</u> *[hand-underlined]* analytic gradients. *[hand mark in right margin]* If the two subroutines do not <u>return identical results to several decimal</u> *[hand-underlined]* places, there is likely a mistake somewhere. *[hand check-mark]*

*<u>The momentum distribution, $p(\phi)$</u>* *[the heading is hand-underlined]*

It is usual to give $\phi$ a multivariate normal distribution (recall that $\phi$ has the same dimension as $\theta$) with mean 0 and covariance set to a prespecified '<u>mass matrix</u>' *[hand-underlined]* $M$ (so called by analogy to <u>the physical model of Hamiltonian dynamics</u>) *[hand-underlined]*. To keep it simple, we commonly use a diagonal mass matrix, $M$. If so, the components of $\phi$ are independent, with <u>$\phi_j \sim \mathrm{N}(0, M_{jj})$</u> *[hand-underlined]* for each dimension $j = 1,\dots,d$. It can be useful for $M$ to roughly scale with the inverse covariance matrix of the posterior distribution, $(\mathrm{var}(\theta\mid y))^{-1}$, but the algorithm works in any case; better scaling of $M$ will merely make <u>HMC more efficient</u> *[hand-underlined]*.

> ✔ Verified: For $\phi \sim \mathrm{N}_d(0,M)$ with $M$ diagonal and positive, the joint density equals $\prod_j \mathrm{N}(\phi_j \mid 0, M_{jj})$, i.e. the components are independent with $\phi_j \sim \mathrm{N}(0,M_{jj})$.

*[margin notes, right margin beside this paragraph, enclosed by a hand-drawn vertical rule, partly legible: "$\phi \sim$ [illegible]" / "e v [illegible]" / "corr b/w(?) $\theta$, $\phi$(?)". Lecture scratch on the momentum variable.]*

*<u>The three steps of an HMC iteration</u>* *[the heading is hand-underlined]*

HMC proceeds by a series of iterations (as in any Metropolis algorithm), with each iteration having three parts:

*[margin note, right: "Metropolis(?)", with a long hand-drawn arrow running leftward beneath the printed line to point at the words "Metropolis algorithm".]*

1. The iteration begins by updating $\phi$ with a random draw from its posterior distribution—which, as specified, is <u>the same as its prior distribution, $\phi \sim \mathrm{N}(0, M)$</u> *[hand-underlined]*.

2. *[hand-drawn star in margin]* The main part of the <u>Hamiltonian Monte Carlo</u> *[hand-underlined]* iteration is a simultaneous update of $(\theta,\phi)$, conducted in an elaborate but effective fashion via a discrete <u>mimicking of physical dynamics</u> *[hand-underlined]*. This update involves $L$ '<u>leapfrog</u> *[hand-underlined]* steps' (to be defined in a moment), each scaled by a factor $\epsilon$. In a <u>leapfrog</u> *[hand-underlined]* step, both $\theta$ and $\phi$ are changed, each in relation to the other. The $L$ leapfrog steps proceed as follows:

    Repeat the following steps $L$ times:

    (a) <u>Use the gradient (the vector derivative) of the log-posterior density</u> *[hand-underlined]* of $\theta$ to make a <u>half-step</u> *[hand-underlined]* of $\phi$:

    $$\phi \leftarrow \phi + \tfrac{1}{2}\epsilon\,\frac{d\log p(\theta\mid y)}{d\theta}.$$

    *[margin note, right of this equation: "[illegible] (possibly "params"(?))" followed by a large "$\epsilon$", and below it "$\eta$, $L$" — most likely "$\epsilon$, $L$", the two tuning constants.]*

    (b) Use the '<u>momentum</u>' vector $\phi$ *[hand-underlined]* to update the '<u>position</u>' vector $\theta$ *[hand-underlined]*:

    $$\theta \leftarrow \theta + \epsilon M^{-1}\phi.$$

    Again, $M$ is the mass matrix, the <u>covariance of the momentum distribution</u> *[hand-underlined]* $p(\phi)$. If <u>$M$ is diagonal</u> *[hand-underlined]*, the above step amounts to scaling each dimension of the $\theta$ update. (It might seem redundant to include $\epsilon$ in the above expression: why not simply absorb it into $M$, which can itself be set by the user? The reason is <u>that it can be convenient in tuning the algorithm to alter $\epsilon$ while keeping $M$ fixed</u>.) *[hand-underlined]*

*[Handwritten scratch, right margin beside steps 1–2, four or five lines of cursive, almost entirely illegible; the last line reads clearly "$(\theta,\phi)$". Lecture scratch notes on the joint update.]*

*(The page ends here, mid-list — step 3 and the remainder of the leapfrog description continue on the next page.)*

### PDF page 181 (booklet page 302)

*(This page is a photocopied insert from another text — the running header reads "COMPUTATIONALLY EFFICIENT MCMC" and the equation is numbered (12.3). It is not typeset with the rest of the booklet.)*

&nbsp;&nbsp;&nbsp;&nbsp;(c) Again use the gradient of $\theta$ to half-update $\phi$:

$$\phi \leftarrow \phi + \frac{1}{2}\epsilon\,\frac{d\log p(\theta|y)}{d\theta}.$$

Except at the first and last step, updates (c) and (a) above can be performed together. The stepping thus starts with a half-step of $\phi$, then alternates $L-1$ full steps of the parameter vector $\theta$ and the momentum vector $\phi$, and concludes with a half-step of $\phi$. This algorithm (called a 'leapfrog' because of the splitting of the momentum updates into half steps) is a discrete approximation to physical Hamiltonian dynamics in which both position and momentum evolve in continuous time. *[the clause "a discrete approximation to physical Hamiltonian dynamics in which both position and momentum evolve in continuous time" is hand-underlined]*

In the limit of $\epsilon$ near zero, the leapfrog algorithm preserves the joint density $p(\theta,\phi|y)$. We will not give the proof, but here is some intuition. *[this sentence is hand-underlined]* Suppose the current value of $\theta$ is at a flat area of the posterior. Then $\frac{d\log p(\theta|y)}{d\theta}$ will be zero, and in step 2 above, the momentum will remain constant. Thus the leapfrog steps will skate along in $\theta$-space with constant velocity. Now suppose the algorithm moves toward an area of low posterior density. Then $\frac{d\log p(\theta|y)}{d\theta}$ will be negative in this direction, thus in step 2 inducing a decrease in the momentum in the direction of movement. As the leapfrog steps continue to move into an area of lower density in $\theta$-space, the momentum continues to decrease. The decrease in $\log p(\theta|y)$ is matched (in the limit $\epsilon \to 0$, exactly so) *[the phrase "$\epsilon \to 0$, exactly so" is hand-underlined]* by a decrease in the 'kinetic energy,' $\log p(\phi)$. And if iterations continue to move in the direction of decreasing density, the leapfrog steps will slow to zero and then back down or curve around the dip. Now consider the algorithm heading in a direction in which the posterior density is increasing. Then $\frac{d\log p(\theta|y)}{d\theta}$ will be positive in that direction, leading in step 2 to an increase in momentum in that direction. As $\log p(\theta|y)$ increases, $\log p(\phi)$ increases correspondingly until the trajectory eventually moves past or around the mode and then starts to slow down.

For finite $\epsilon$, the joint density $p(\theta,\phi|y)$ does not remain entirely constant during the leapfrog steps but it will vary only slowly if $\epsilon$ is small. *[the phrase "vary only slowly if $\epsilon$ is small" is hand-underlined]* For reasons we do not discuss here, the leapfrog integrator has the pleasant property that combining $L$ steps of error $\delta$ does not produce $L\delta$ error, because the dynamics of the algorithm tend to send the errors weaving back and forth around the exact value that would be obtained by a continuous integration. Keeping the discretization error low is important because of the next part of the HMC algorithm, the accept/reject step. *[the final clause "the accept/reject step." is hand-underlined]*

3. Label $\theta^{t-1}, \phi^{t-1}$ as the value of the parameter and momentum vectors at the start of the leapfrog process and $\theta^*, \phi^*$ as the value after the $L$ steps. *[the clause "leapfrog process and $\theta^*, \phi^*$ as the value after the $L$ steps" is hand-underlined]* In the accept-reject step, we compute *["compute" is hand-underlined]*

$$r = \frac{p(\theta^*|y)\,p(\phi^*)}{p(\theta^{t-1}|y)\,p(\phi^{t-1})}. \tag{12.3}$$

4. Set

$$\begin{pmatrix}\theta^t\\ \phi^t\end{pmatrix} = \begin{cases} \begin{pmatrix}\theta^*\\ \phi^*\end{pmatrix} & \text{with probability } \min(r,1)\\[2mm] \begin{pmatrix}\theta^{t-1}\\ \phi^{t-1}\end{pmatrix} & \text{otherwise.}\end{cases}$$

*(correction: the printed display reads $\theta^t = \begin{cases}\theta^* & \text{with probability } \min(r,1)\\ \theta^{t-1} & \text{otherwise,}\end{cases}$ and the instructor has written "$\phi^t$" beneath the printed $\theta^t$, "$\phi^*$" beside $\theta^*$, and "$\phi^{t-1}$" beside $\theta^{t-1}$, making the update jointly on the pair $(\theta,\phi)$.)*

*[Right margin, level with step 4: a dense handwritten scrawl, written over itself and scribbled through — apparently a first attempt at the paired update $(\theta^t,\phi^t)$ over $(\theta^{t-1},\phi^{t-1})$ (?), then cancelled. Largely [illegible].]*

*[Handwritten work in the bottom-left margin, partly legible: $\begin{pmatrix}\theta^t\\ \phi^t\end{pmatrix} = \begin{pmatrix}\theta^*\\ \phi^*\end{pmatrix}$ ... "w.p.(?) $\min(r,1)$" ... $\begin{pmatrix}\theta^{t-1}\\ \phi^{t-1}\end{pmatrix}$. A long curved line runs from this note rightward to the final paragraph. These are lecture scratch notes restating step 4 as a joint update of the parameter and momentum vectors.]*

Strictly speaking it would be necessary to set $\phi^t$ as well, but since we do not care about $\phi$ in itself, and it gets immediately updated at the beginning of the next iteration (see step 1 above), there is no need to keep track of it after the accept/reject step. *[the phrase "accept/reject step." is hand-underlined]*

As with any other MCMC algorithm, we repeat these iterations until approximate convergence, as assessed by $\hat{R}$ being near 1 and the effective sample size being large enough for all quantities of interest; see Section 11.4. *[the phrase "$\hat{R}$ being near 1 and the effective sample size being large enough" is hand-underlined]*

### PDF page 182 (booklet page 303)

*(Note: this leaf is a photocopied insert from another text — the running head reads "HAMILTONIAN MONTE CARLO" and the printed folio is 303, not a booklet page in the 170s. The left edge of the scan also catches a narrow sliver of the facing page's text ("e", "s", "h", ")", "$\theta$", "e", "h", "r", "a", "e", "n", "e", "r", "2", "s", "n", "$\delta$", "ts", "it", "or", …); those fragments are scan artifacts and are not transcribed.)*

**Restricted parameters and areas of zero posterior density**

HMC is designed to work with all-positive target densities. If at any point during an iteration the algorithm reaches a point of zero posterior density (for example, if the steps go below zero when updating a parameter that is restricted to be positive), we stop the stepping and give up, spending another iteration at the previous value of $\theta$. The resulting algorithm preserves detailed balance and stays in the positive zone. *[the clauses "go below zero when updating a parameter that is restricted to be positive" and "The resulting algorithm preserves detailed balance and stays in the positive zone" are hand-underlined]* *[margin note, bracketed: "detailed balance"]*

An alternative is 'bouncing,' where again the algorithm checks that the density is positive after each step and, if not, changes the sign of the momentum to return to the direction in which it came. This again preserves detailed balance and is typically more efficient than simply rejecting the iteration, for example with a hard boundary for a parameter that is restricted to be positive. *[the phrases "detailed balance" and "hard boundary" are hand-underlined]* *[margin note: "$\log\left(\frac{\cdot-a}{b-a}\right)$" (?), numerator illegible]*

Another way to handle bounded parameters is via transformation, for example taking the logarithm of a parameter constrained to be positive or the logit for a parameter constrained to fall beween [sic] 0 and 1, or more complicated joint transformations for sets of parameters that are constrained (for example, if $\theta_1 < \theta_2 < \theta_3$ or if $\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4 = 1$). One must then work out the Jacobian of the transformation and use it to determine the log posterior density and its gradient in the new space. *[the opening clause "Another way to handle bounded parameters is via transformation" is hand-underlined]*

*[Handwritten work overlapping the last line of this paragraph and filling the band above the next heading: three or four expressions, each deliberately scratched out. Fragments that survive the scribbling read "$\log \phi^{\,\cdot}$" (?) and "$\le e^{\,\cdot}$" (?); the remainder is illegible. These appear to be abandoned lecture scratch notes for the Jacobian rule.]*

**Setting the tuning parameters**

HMC can be tuned in three places: (i) the probability distribution for the momentum variables $\phi$ (which, in our implementation requires specifying the diagonal elements of a covariance matrix, that is, a scale parameter for each of the $d$ dimensions of the parameter vector), (ii) the scaling factor $\epsilon$ of the leapfrog steps, and (iii) the number of leapfrog steps $L$ per iteration. *[the phrases "HMC can be tuned in three places", "covariance matrix", "the scaling factor $\epsilon$ of the leapfrog steps" and "the number of leapfrog steps $L$ per iteration" are hand-underlined]*

*[Handwritten block in the right margin, largely illegible. Discernible fragments: "$\phi \sim$" (?), "$\Sigma$" (?), "$q =$" (?), an "$\epsilon$", and what may be "leapfrog" (?). Lecture scratch notes on the momentum distribution and the leapfrog step.]*

As with the Metropolis algorithm in general, these tuning parameters can be set ahead of time, or they can be altered completely at random (a strategy which can sometimes be helpful in keeping an algorithm from getting stuck), but one has to take care when altering them given information from previous iterations. Except in some special cases, adaptive updating of the tuning parameters alters the algorithm so that it no longer converges to the target distribution. So when we set the tuning parameters, we do so during the warm-up period: that is, we start with some initial settings, then run HMC for a while, then reset the tuning parameters based on the iterations so far, then discard the early iterations that were used for warm-up. This procedure can be repeated if necessary, as long as the saved iterations use only simulations after the last setting of the tuning parameters. *[the phrases "tuning parameters", "an algorithm from getting stuck", "previous iterations", "warm-up period", and the final clause "as long as the saved iterations use only simulations after the last setting of the tuning parameters" are hand-underlined]* *[margin notes: "$\eta, \epsilon, L$" (?, first symbol may be "$M$"); "(warm-up period)"]*

How, then, to set the parameters that govern HMC? We start by setting the scale parameters for the momentum variables to some crude estimate of the scale of the target distribution. (One can also incorporate covariance information but here we will assume a diagonal covariance matrix so that all that is required is the vector of scales.) By default we could simply use the identity matrix. *[hand-written "??" immediately after this sentence]* *[the phrases "covariance information", "so that all that is required is the vector of scales" and "we could simply use the identity matrix" are hand-underlined]*

We then set the product $\epsilon L$ to 1. This roughly calibrates the HMC algorithm to the 'radius' of the target distribution; that is, $L$ steps, each of length $\epsilon$ times the already-chosen scale of $\phi$, should roughly take you from one side of the distribution to the other. A default starting point could be $\epsilon = 0.1, L = 10$. *[the phrases "We then set the product $\epsilon L$ to 1", "should roughly take you from one side of the distribution to the other" and "$\epsilon = 0.1, L = 10$" are hand-underlined]* *[margin notes: "$\epsilon L = 1$", circled; beneath it, "$L$ to determine (?) by $\epsilon$" — partly illegible]*

> ✔ Verified: The default starting point $\epsilon = 0.1$, $L = 10$ satisfies the calibration rule $\epsilon L = 1$.

Finally, theory suggests that HMC is optimally efficient when its acceptance rate is approximately 65% (based on an analysis similar to that which finds an optimal 23% acceptance rate for the multidimensional Metropolis algorithm). The theory is based on all sorts of assumptions but seems like a reasonable guideline for optimization in practice. For now we recommend a simple adaptation in which HMC is [sic: "run" appears to be omitted] with its initial settings and then adapted if the average acceptance probability (as computed from the simulations so far) is not close to 65%. If the average acceptance probability is lower, then the leapfrog jumps *[the phrases "theory suggests that HMC", "approximately 65%", "reasonable guideline for optimization in practice" and "lower, then the leapfrog jumps" are hand-underlined]* *[margin note: "$\simeq 65\%$"]*

### PDF page 183 (booklet page 304)

*(This page is a photocopied insert from another book, not typeset booklet material: the running header reads "COMPUTATIONALLY EFFICIENT MCMC" and the printed folio is 304. Per convention the number printed on the page is used. The scan also catches a narrow vertical strip of the facing page along the right edge; its fragments are recorded at the end.)*

are too ambitious and you should lower $\epsilon$ and correspondingly increase $L$ (so their product remains 1). Conversely, if the average acceptance probability is much higher than 65%, then the steps are too cautious and we recommend raising $\epsilon$ and lowering $L$ (not forgetting that $L$ must be an integer). These rules do not solve all problems, and it should be possible to develop diagnostics to assess the efficiency of HMC to allow for more effective adaptation of the tuning parameters.

*[in the passage above: "so their product remains 1)" and "much higher than 65%" are hand-underlined, with a caret mark in the left margin beside "remains 1)"; a hand stroke crosses the "$L$" in "lowering $L$"; and "do not solve all problems, and it should be possible to develop diagnostics to assess the efficiency of HMC to allow for more effective adaptation of the tuning parameters." is hand-underlined across four lines]*

*Varying the tuning parameters during the run*

As with MCMC tuning more generally, any adaptation can go on during the warm-up period, but adaptation performed later on, during the simulations that will be used for inference, can cause the algorithm to converge to the wrong distribution. For example, suppose we were to increase the step size $\epsilon$ after high-probability jumps and decrease $\epsilon$ when the acceptance probability is low. Such an adaptation seems appealing but would destroy the detailed balance (that is, the property of the algorithm that the flow of probability mass from point A to B is the same as from B to A, for any points A and B in the posterior distribution) that is used to prove that the posterior distribution of interest is the stationary distribution of the Markov chain.

*[hand-underlined: "can cause the algorithm to converge to the wrong distribution"; and "the detailed balance (that is, the property of the algorithm that the flow of probability mass from point A to B is the same as from B to A"]*

Completely random variation of $\epsilon$ and $L$, however, causes no problems with convergence and can be useful. If we randomly vary the tuning parameters (within specified ranges) from iteration to iteration while the simulation is running, the algorithm has a chance to take long tours through the posterior distribution when possible and make short movements where the iterations are stuck in a cramped part of the space. The price for this variation is some potential loss of optimality, as the algorithm will also take short steps where long tours would be feasible and try for long steps where the space is too cramped for such jumps to be accepted.

*[hand-underlined: "Completely random variation of $\epsilon$ and $L$"; "is some potential loss of optimality"]*

*Locally adaptive HMC*

For difficult HMC problems, it would be desirable for the tuning parameters to vary as the algorithm moves through the posterior distribution, with the mass matrix $M$ scaling to the local curvature of the log density, the step size $\epsilon$ getting smaller in areas where the curvature is high, and the number of steps $L$ being large enough for the trajectory to move far through the posterior distribution without being so large that the algorithm circles around and around. To this end, researchers have developed extensions of HMC that adapt without losing detailed balance. These algorithms are more complicated and can require more computations per iteration but can converge more effectively for complicated distributions. We describe two such algorithms here but without giving the details.

*[hand-underlined: "with the mass matrix $M$ scaling to the local curvature of the log density, the step size $\epsilon$"; "researchers have developed extensions of HMC that adapt without losing detailed balance."]*

*The no-U-turn sampler.* In the no-U-turn sampler, the number of steps is determined adaptively at each iteration. Instead of running for a fixed number of steps, $L$, the trajectory in each iteration continues until it turns around (more specifically, until we reach a negative value of the dot product between the momentum variable $\phi$ and the distance traveled from the position $\theta$ at the start of the iteration). This rule essentially sends the trajectory as far as it can go during that iteration. If such a rule is applied alone, the simulations will not converge to the desired target distribution. The full no-U-turn sampler is more complicated, going backward and forward along the trajectory in a way that satisfies detailed balance. Along with this algorithm comes a procedure for adaptively setting the mass matrix $M$ and step size $\epsilon$; these parameters are tuned during the warm-up phase and then held fixed during the later iterations which are kept for the purpose of posterior inference.

*[the run-in heading "The no-U-turn sampler" is hand-underlined with a small arrow pointing to it from the left margin; also hand-underlined: "the number of steps is determined adaptively at each iteration", "until we reach a negative value of the dot product", "mass matrix $M$", and "these parameters are tuned during the warm-up phase and then held fixed during the later iterations which are kept for the purpose of posterior inference."]*

*[Figure, hand-drawn in the left margin beside this paragraph: a closed, curved parallelogram-like loop — a sketch of a trajectory doubling back on itself — with an arrowhead indicating the direction of travel, the symbol $\phi$ written at the left end and $\phi$(?) again at the right end, and an inequality written inside the loop reading roughly $\phi\cdot v > 0$(?) (possibly $\phi\cdot\theta > 0$(?)). This is a lecture scratch sketch of the no-U-turn stopping rule: the trajectory continues while the dot product of the momentum with the displacement stays positive, and stops when it goes negative.]*

*Riemannian adaptation.* Another approach to optimization is Riemannian adaptation, in which the mass matrix $M$ is set to conform with the local curvature of the log posterior

*[the run-in heading "Riemannian adaptation" is hand-underlined, with a small caret/tick in the left margin beside it]*

*(The page ends mid-sentence.)*

---

*[Along the right edge the scan captures a vertical sliver of the facing page (running header "HMC FOR A ..."), cut off after a few characters per line. Legible fragments, top to bottom: "density at each"; "effectively but"; "detailed balanc[e]"; "Neither of t[he]"; "pler is self-tuni[ng]"; "has difficulties"; "ficulties transi[tioning]"; "adaptation ha[s]"; "practical in hi[gh]"; the italic heading "Combining H[MC ...]"; "There are two"; "First, it can"; "or to speed"; "vector $\theta = (\eta$"; "corresponding"; "the posterior"; "this case, eve[n]"; "be more effec[tive]"; "steps, altering"; "at most one"; "be used to fa[...]"; "The secon[d]"; "ing of discrete"; "If some of th[e]"; "dicators for m[...]"; "has a positive"; "more general"; "12.3). The si[...]"; "eters, then a"; "slice updates"; the section heading "12.5  Ham[iltonian ...]"; "We illustrate"; "testing exper[iment]"; "Gibbs sampl[er]"; "efficient mov[es]"; "to understan[d]"; "the algorithm"; "In order"; "Chapter 5)"; "to $\alpha_1,\ldots,\alpha$"; the italic run-in "Gradients o[f]"; "density for"; "the normal". This strip belongs to the next page and is not part of page 304.]*

### PDF page 184 (booklet page 305)

*(This page is a photocopied insert from Gelman, Carlin, Stern, Dunson, Vehtari & Rubin,* Bayesian Data Analysis*, 3rd ed. — its running head reads "HMC FOR A HIERARCHICAL MODEL" and the printed folio is 305. It does not carry a booklet page number of its own; it falls physically within Chapter A — Rstudio.)*

density at each step *[hand-underlined: "each step"]*. Again, the local adaptation allows the sampler to move much more effectively *[hand-underlined: "effectively"]* but the steps of the algorithm need to become more complicated to maintain detailed balance. Riemannian adaptation can be combined with the no-U-turn sampler.

Neither of the above extensions solves all the problems with HMC. The no-U-turn sampler is self-tuning and computationally efficient but, like ordinary Hamiltonian Monte Carlo, has difficulties with very short-tailed and long-tailed *[hand-underlined]* distributions, in both cases having difficulties transitioning from the center to the tails, even in one dimension. Riemannian adaptation handles varying curvature and non-exponentially tailed distributions but is impractical in high dimensions. *[this final sentence is hand-underlined throughout]* *[margin note, top right, with a hand-drawn bracket pointing to this sentence: "Riemannian adaptation"]*

*Combining HMC with Gibbs sampling*

There are two ways *[hand-underlined]* in which ideas of the Gibbs sampler fit into Hamiltonian Monte Carlo. First, *[hand-underlined]* it can make sense to partition variables into blocks *[hand-underlined]*, either to simplify computation or to speed convergence. Consider a hierarchical model with $J$ groups, with parameter vector $\theta = (\eta^{(1)}, \eta^{(2)}, \ldots, \eta^{(J)}, \phi)$, where each of the $\eta^{(j)}$'s is itself a vector of parameters corresponding to the model for group $j$ and $\phi$ is a vector of hyperparameters, and for which the posterior distribution can be factored as, $p(\theta \mid y) \propto p(\phi) \prod_{j=1}^{J} p(\eta^{(j)} \mid \phi) p(y^{(j)} \mid \eta^{(j)})$. In this case, even if it is possible to update the entire vector $\theta$ at once using HMC, it may be more effective—in computation speed or convergence—to cycle through $J + 1$ updating steps, altering each $\eta^{(j)}$ and then $\phi$ during each cycle. This way we only have to work with at most one *[hand-underlined]* of the likelihood factors, $p(y^{(j)} \mid \eta^{(j)})$, at each step. *[hand tick/bracket in the left margin beside this sentence]* Parameter expansion can be used *[a wavy hand underline beneath "be used to"]* to facilitate quicker mixing through the joint distribution.

The second way *[hand-underlined, with a scored stroke over "way"]* in which Gibbs sampler principles can enter HMC is through the updating of discrete variables *[hand-underlined]*. Hamiltonian dynamics are only defined on continuous distributions *[hand-underlined]*. *[margin note, right: "(ii)" (?) — labelling the second of the two ways]* If some of the parameters in a model are defined on discrete spaces (for example, latent indicators for mixture components; or a parameter that follows a continuous distribution but has a positive probability of being exactly zero), they can be updated using Gibbs steps or, more generally, one-dimensional updates such as Metropolis or slice sampling *[hand-underlined]* (see Section 12.3). *[margin note, right: a hand-drawn oval enclosing the cursive word "hybrid" (?)]* The simplest approach is to partition the space into discrete and continuous parameters, then alternate HMC updates on the continuous subspace and Gibbs *[hand-underlined]*, Metropolis, or slice updates on the discrete components. *[a short hand-drawn rule trails below the end of this paragraph, lower left]*

**12.5  Hamiltonian dynamics for a simple hierarchical model**

We illustrate the tuning of Hamiltonian Monte Carlo with the model for the educational testing experiments described in Chapter 5. HMC is not *[hand-underlined: "not"]* necessary in this problem—the Gibbs sampler works just fine, especially after the parameter expansion which allows more efficient movement of the hierarchical variance parameter (see Section 12.1)—but it is helpful to understand the new algorithm in a simple example. Here we go through all the steps of the algorithm. The code appears in Section C.4, starting on page 601.

In order not to overload our notation, we label the eight school effects (defined as $\theta_j$ in Chapter 5) as $\alpha_j$; the full vector of parameters $\theta$ then has $d = 10$ dimensions, corresponding to $\alpha_1, \ldots, \alpha_8, \mu, \tau$.

> ✔ Verified: the parameter vector (α_1,…,α_8, μ, τ) has d = 10 components.

*Gradients of the log posterior density.* *[the run-in heading is hand-underlined]* For HMC we need the gradients of the log posterior density for each of the ten parameters, a set of operations that are easily performed with the normal distributions of this model:

$$\frac{d \log p(\theta \mid y)}{d \alpha_j} \;=\; -\frac{\alpha_j - y_j}{\sigma_j^2} - \frac{\alpha_j - \mu}{\tau^2}, \quad \text{for } j = 1, \ldots, 8,$$

> ✔ Verified: d/dα_j of the eight-schools log posterior equals -(α_j - y_j)/σ_j² - (α_j - μ)/τ².

*(The page ends here, mid-display — the remaining gradients, with respect to $\mu$ and $\tau$, continue on the next page.)*

### PDF page 185 (booklet page 306)

*(This page is a photocopied insert from another text — the running header reads "COMPUTATIONALLY EFFICIENT MCMC" and the printed folio is 306. The right-hand edge of the scan also captures a narrow, mostly cut-off strip of the facing page; it is described at the foot of this transcript rather than transcribed, as its lines are truncated past legibility.)*

$$\frac{d\log p(\theta\mid y)}{d\mu} \;=\; -\sum_{j=1}^{J}\frac{\mu-\alpha_j}{\tau^2},$$

$$\frac{d\log p(\theta\mid y)}{d\tau} \;=\; -\frac{J}{\tau}+\sum_{j=1}^{J}\frac{(\mu-\alpha_j)^2}{\tau^3}.$$

> ✔ Verified: The two displayed gradients are the exact $\mu$- and $\tau$-partials of $\log p(\theta\mid y)=\text{const}-J\log\tau-\sum_j(\alpha_j-\mu)^2/(2\tau^2)$.

As a debugging step we also compute the gradients numerically using finite differences of $\pm 0.0001$ on each component of $\theta$. *[the quantity "$\pm 0.0001$" is circled by hand]* Once we have checked that the two gradient routines yield identical results, we use the analytic gradient in the algorithm as it is faster to compute. *[the final clause, from "identical results" to "faster to compute", carries a hand dotted-underline]*

*The mass matrix for the momentum distribution.* *[the run-in head is hand-underlined]* As noted above, we want to scale the mass matrix to roughly match the posterior distribution. *[this clause is hand-underlined]* *[margin mark: three vertical strokes "|||" in the right margin at this line]* That said, we typically only have a vague idea of the posterior scale before beginning our computation; thus this scaling is primarily intended to forestall the problems that would arise if there are gross disparities in the scaling of different dimensions. *[the clause "there are gross disparities in the scaling of different dimensions" is hand-underlined]* In this case, after looking at the data in Table 5.2 we assign a rough scale of 15 for each of the parameters in the model and crudely set the mass matrix to Diag$(15,\dots,15)$. *[a hand wavy squiggle underlines "Diag$(15,\dots,15)$"]*

*Starting values.* We run 4 chains of HMC with starting values drawn at random to crudely match the scale of the parameter space, in this case following the idea above and drawing the ten parameters in the model from independent N$(0,15^2)$ distributions. *[both "match the scale of the parameter space" and "the ten parameters in the model from independent N$(0,15^2)$ distributions" are hand-underlined]*

*[hand star-mark in margin]* *Tuning $\epsilon$ and $L$.* *[the run-in head is hand-underlined]* To give the algorithm more flexibility, we do not set $\epsilon$ and $L$ to fixed values. Instead we choose central values $\epsilon_0, L_0$ and then at each step draw $\epsilon$ and $L$ independently from uniform distributions on $(0,2\epsilon_0)$ and $[1,2L_0]$, respectively (with the distribution for $L$ being discrete uniform, as $L$ must be an integer). We have no reason to think this particular jittering is ideal; it is just a simple way to vary the tuning parameters in a way that does not interfere with convergence of the algorithm. Following the general advice given above, we start by setting $\epsilon_0 L_0 = 1$ and $L_0 = 10$. We simulate 4 chains for 20 iterations just to check that the program runs without crashing.

*[Handwritten note in the left margin, spanning this paragraph and the next, written at a slant across several lines and largely illegible at the resolution of this scan. Best-effort partial reading: "Might show(?) ... to be(?) ... the prior(?) ... instead of(?) ... this a(?) ... density of the(?) ... $\sigma^2$(?) ... log likelihood(?)". The note appears to be lecture scratch relating the tuning discussion back to the prior/likelihood, but no confident reading is possible; several words are [illegible].]*

We then do some experimentation. *[this sentence is hand-underlined]* We first run 4 chains for 100 iterations and see that the inferences are reasonable (no extreme values, as can sometimes happen when there is poor convergence or a bug in the program) but not yet close to convergence, with several values of $\widehat{R}$ that are more than 2. The average acceptance probabilities of the 4 chains are 0.23, 0.59, 0.02, and 0.57, well below 65%, so we suspect the step size is too large. *[the final clause, "well below 65%, so we suspect the step size is too large.", is hand-underlined]*

> ✔ Verified: The four average acceptance probabilities 0.23, 0.59, 0.02, 0.57 all lie below the stated 65% threshold, as does their mean.

We decrease $\epsilon_0$ to 0.05, increase $L_0$ to 20 (thus keeping $\epsilon_0 L_0$ constant), and rerun the 4 chains for 100 iterations, now getting acceptance rates of 0.72,, [sic: doubled comma] 0.87, 0.33, and 0.55, with chains still far from mixing. At this point we increase the number of simulations to 1000. The simulations now are close to convergence, with $\widehat{R}$ less than 1.2 for all parameters, and average acceptance probabilities are more stable, at 0.52, 0.68, 0.75, and 0.51. We then run 4 chains at 10,000 simulations at these tuning parameters and achieve approximate convergence, with $\widehat{R}$ less than 1.1 for all parameters. *[from "run 4 chains at 10,000 simulations" through "achieve approximate convergence" is hand-underlined]*

> ✔ Verified: $\epsilon_0 L_0 = 1$ with $L_0=10$ gives $\epsilon_0=0.1$, and the revised $(\epsilon_0,L_0)=(0.05,20)$ preserves $\epsilon_0 L_0 = 1$.

> ✔ Verified: The third round's acceptance probabilities (0.52, 0.68, 0.75, 0.51) are strictly "more stable" — smaller spread — than the second round's (0.72, 0.87, 0.33, 0.55), by both variance and range.

In this particular example, HMC is unnecessary, *["HMC is unnecessary" is hand-underlined]* as the Gibbs sampler works fine on an appropriately transformed scale. In larger and more difficult problems, however, Gibbs, and Metropolis can be too slow, *["Gibbs" and "and Metropolis can be too slow" are hand-underlined]* while HMC can move effectively efficiently move through *(correction(?): the printed source reads "can move effectively through"; the scan shows "effectively efficiently move", apparently a handwritten insertion over the printed line — the reading is uncertain and the words are transcribed as they appear)* *["efficiently move through" is hand-underlined]* high-dimensional parameter spaces.

*Transforming to $\log\tau$*

When running HMC on a model with constrained parameters, the algorithm can go outside the boundary, thus wasting some iterations. *["can go outside the boundary, thus wasting some iterations." is hand-underlined]* One remedy is to transform the space to be unconstrained. In this case, the simplest way to handle the constraint $\tau > 0$ is to transform to $\log\tau$. *[a small hand caret/arrow in the bottom left margin points up toward "to $\log\tau$"]* We then must alter the algorithm in the following ways:

*[The page ends here, mid-thought, at the colon.]*

*[Facing-page strip, right edge of scan: a vertical sliver of the next page is caught in the photocopy, cut off after two or three characters per line. Legible fragments only, in order: "STAN:"; a numbered list "1. We …", "2. The … $\log\tau$ …", "3. The … for … grad… Jac…", "4. We … with … in e…", "5. We … ind…"; then "HMC … reason…"; a section number "12.6"; "Hamil… settin… chain…"; "To… progr… given… tation… param… eters… space…"; "W… for ru…"; an italic run-in head "Enter…"; "Each… param… and s… gamm… can… funct… into…"; and a final block "T… that… to co… prog… this… same… reve… any… the…". Not transcribed as content — it belongs to the following page.]*

### PDF page 186 (reproduced source page 307)

*(This page is a photocopied insert from another text — Gelman et al.,* Bayesian Data Analysis, *p. 307. The running header reads "STAN: DEVELOPING A COMPUTING ENVIRONMENT". A narrow strip of the facing page is visible at the left edge of the scan; its lines are truncated past legibility and are not transcribed as content.)*

1. We redefine $\theta$ as $(\alpha_1,\ldots,\alpha_8,\mu,\log\tau)$ and do all jumping on this new space.
2. The (unnormalized) posterior density $p(\theta\mid y)$ is multiplied by the Jacobian, $\tau$, so we add $\log\tau$ to the log posterior density used in the calculations.
3. The gradient of the log posterior density changes in two ways: first, we need to account for the new term added just above; second, the derivative for the last component of the gradient is now with respect to $\log\tau$ rather than $\tau$ and so must be multiplied by the Jacobian, $\tau$:

$$
\frac{d\log p(\theta\mid y)}{d\log\tau}
= -(J-1)+\sum_{j=1}^{J}\frac{(\mu-\alpha_j)^2}{\tau^2}.
$$

> ✔ Verified: Differentiating the transformed log posterior with respect to log τ gives −(J−1)+Σ(μ−αⱼ)²/τ².

4. We change the mass matrix to account for the transformation. We keep $\alpha_1,\ldots,\alpha_8,\mu$ with masses of 15 (roughly corresponding to a posterior distribution with a scale of 15 in each of these dimensions) but set the mass of $\log\tau$ to 1.
5. We correspondingly change the initial values by drawing the first nine parameters from independent N$(0,15^2)$ distributions and $\log\tau$ from N$(0,1)$.

HMC runs as before. Again, we start with $\epsilon=0.1$ and $L=10$ and then adjust to get a reasonable acceptance rate.

**12.6  Stan: developing a computing environment**

Hamiltonian Monte Carlo takes a bit of effort to program and tune. In more complicated settings, though, we have found HMC to be faster and more reliable than basic Markov chain simulation algorithms. *[the clause "HMC to be faster and more reliable than basic Markov chain simulation algorithms" is hand-underlined]*

To mitigate the challenges of programming and tuning, we have developed a computer program, Stan (Sampling through adaptive neighborhoods) *[the parenthetical phrase is hand-underlined]* to automatically apply HMC given a Bayesian model. The key steps of the algorithm are data and model input, computation of the log posterior density (up to an arbitrary constant that cannot depend on the parameters in the model) and its gradients, a warm-up phase in *[the phrase "a warm-up phase in" is hand-underlined]* which the tuning parameters are set, an implementation of the no-U-turn sampler to move through the parameter space, and convergence monitoring and inferential summaries at the end.

We briefly describe how each of these steps is done in Stan. Instructions and examples for running the program appear in Appendix C.

*Entering the data and model*

Each line of a Stan model goes into defining the log probability density of the data and parameters, with code for looping, conditioning, computation of intermediate quantities, and specification of terms of the log joint density. Standard distributions such as the normal, gamma, binomial, Poisson, and so forth, are preprogrammed, and arbitrary distributions can be entered by directly programming the log density. Algebraic manipulations and functions such as exp and logit can also be included in the specification; it is all just sent into C++. *[the clause "it is all just sent into C++" is hand-underlined across the line break]*

To compute gradients, Stan uses automatic analytic differentiation, using an algorithm that parses arbitrary C++ expressions and then applies basic rules of differential calculus to construct a C++ program for the gradient. For computational efficiency, we have preprogrammed the gradients for various standard statistical expressions to make up some of this difference. We use special scalar variable classes that evaluate the function and at the same time construct the full expression tree used to generate the log probability. Then the reverse pass walks backward down the expression tree (visiting every dependent node before any node it depends on), propagating partial derivatives by the chain rule. The walk over the expression tree implicitly employs dynamic programming to minimize the number of

### PDF page 187 (booklet page 308)

*[Editorial note: this page is not part of the MA 556 booklet's own typesetting. It is a photocopy of page 308 of Gelman et al., "Bayesian Data Analysis" (3rd ed.), running header "COMPUTATIONALLY EFFICIENT MCMC", inserted into the booklet. It does not belong to Chapter A — Rstudio, and the printed number is 308, not 182. A vertical sliver of the facing photocopy page (starting "EXE…", with fragments "Geye", "revie", "prob", "(199", "has", "rege", "targ", "algo", "simu", "thos", "meth", "liter", "Gelr", "trod", "2013", "HMC", "Wal", "12.8", "1. E", "2. S", "(a)", "(b)", "(c)", "(d)", "3. F", "4. C") is visible down the right edge of the scan and is not transcribed.]*

calculations. The resulting autodifferentiation is typically much faster than computing the gradient numerically via finite differences. *[the clause "much faster than computing the gradient numerically via finite differences" is hand-underlined]*

In addition to the data, parameters, and model statements, a Stan call also needs the number of chains, the number of iterations per chain, and various control parameters that can be set by default. Starting values can be supplied or else they are generated from preset default random variables. *[the clause "Starting values can be supplied or else they are generated from preset" is hand-underlined]*

*[illegible hand-drawn squiggle in the blank space below this paragraph, at the left]*

*Setting tuning parameters in the warm-up phase*

As noted above, it can be tricky to tune Hamiltonian Monte Carlo for any particular example. The no-U-turn sampler helps with this, as it eliminates the need to assign the number of steps $L$, but we still need to set the mass matrix $M$ and step size $\epsilon$. During a prespecified warm-up phase of the simulation, Stan adaptively alters $M$ and $\epsilon$ using ideas from stochastic optimization in numerical analysis. This adaptation will not always work—for distributions with varying curvature, there will not in general be any single good set of tuning parameters—and *[hand-underlined]* if the simulation is having difficulty converging, it can make sense to look at the values of $M$ and *[hand-underlined]* $\epsilon$ chosen for different chains to better understand what is happening. Convergence can sometimes be improved *[hand-underlined]* by reparameterization. More generally, it could make sense to have different tuning parameters for different areas of the *[hand-underlined]* distribution—this is related to ideas such as Riemannian adaptation, which at the time of this writing we are incorporating into Stan. *[hand-drawn horizontal rule extending into the right margin]*

*No-U-turn sampler*

*[margin note, rotated ~90° in the left margin beside this section, dark pen: two or three characters, possibly "$M$, $\epsilon$" (?) — illegible]*

Stan runs HMC using the no-U-turn sampler, preprocessing where possible by transforming bounded variables to put them on an unconstrained scale. *[the phrase "on an unconstrained scale" is hand-underlined]* For complicated constraints this cannot always be done automatically and then it can make sense for the user to reparameterize in writing the model. While running, Stan keeps track of acceptance probabilities (as well as the simulations themselves), which can be helpful in getting inside the algorithm if there are problems with mixing of the chains.

*Inferences and postprocessing*

Stan produces multiple sequences of simulations. For our posterior inferences we discard the iterations from the warm-up period *[hand-underlined]* (but we save them as possibly of diagnostic use if the algorithm is not mixing well) and compute $\widehat{R}$ and $n_{\text{eff}}$ *[hand-underlined]* as described in Section 11.4.

**12.7  Bibliographic note**

For the relatively simple ways of improving simulation algorithms mentioned in Sections 12.1 and 12.2, Tanner and Wong (1987) discuss data augmentation and auxiliary variables, and Hills and Smith (1992) and Roberts and Sahu (1997) discuss different parameterizations for the Gibbs sampler. Higdon (1998) discusses some more complicated auxiliary variable methods, and Liu and Wu (1999), van Dyk and Meng (2001), and Liu (2003) present different approaches to parameter expansion. The results on acceptance rates for efficient Metropolis jumping rules appear in Gelman, Roberts, and Gilks (1995); more general results for Metropolis-Hastings algorithms appear in Roberts and Rosenthal (2001) and Brooks, Giudici, and Roberts (2003).

Gelfand and Sahu (1994) discuss the difficulties of maintaining convergence to the target distribution when adapting Markov chain simulations, as discussed at the end of Section 12.2. Andrieu and Robert (2001) and Andrieu and Thoms (2008) consider adaptive Markov chain Monte Carlo algorithms.

### PDF page 188 (booklet page 309)

*[Editorial note: this leaf is a photocopy inserted into the booklet, taken from another text (Gelman et al., "Bayesian Data Analysis"). Its running header reads `EXERCISES` / `309`; it carries no booklet page number of its own.]*

Slice sampling is discussed by Neal (2003), and simulated tempering is discussed by Geyer and Thompson (1993) and Neal (1996b). Besag et al. (1995) and Higdon (1998) review several ideas based on auxiliary variables that have been useful in high-dimensional problems arising in genetics and spatial models.

Reversible jump MCMC was introduced by Green (1995); see also Richardson and Green (1997) and Brooks, Giudici, and Roberts (2003) for more on trans-dimensional MCMC.

Mykland, Tierney, and Yu (1994) discuss an approach to MCMC in which the algorithm has regeneration points, or subspaces of $\theta$, so that if a finite sequence starts and ends at a regeneration point, it can be considered as an exact (although dependent) sample from the target distribution. Propp and Wilson (1996) and Fill (1998) introduce a class of MCMC algorithms called perfect simulation in which, after a certain number of iterations, the simulations are known to have exactly converged to the target distribution.

*[a large hand-drawn curly brace in the right margin brackets the HMC portion of the following paragraph]*

The book by Liu (2001) covers a wide range of advanced simulation algorithms including those discussed in this chapter. The monograph by Neal (1993) also overviews many of these methods. *[from here to "Romeel (2011)" the text is hand-underlined across several lines]* Hamiltonian Monte Carlo was introduced by Duane et al. (1987) in the physics literature and Neal (1994) for statistics problems. Neal (2011) reviews HMC, Hoffman and Gelman (2013) introduce the no-U-turn sampler, and Girolami and Calderhead (2011) introduce Riemannian updating; see also Betancourt and Stein (2011) and Betancourt (2012, 2013). Romeel (?) (2011) explains how leapfrog steps tend to reduce discretization error in HMC. Leimkuhler and Reich (2004) discuss the mathematics in more detail. Griewank and Walther (2008) is a standard reference on algorithmic differentiation. *[a small hand caret/arrow (?) points up into this final line]*

**12.8 Exercises**

1. Efficient Metropolis jumping rules: Repeat the computation for Exercise 11.2 using the adaptive algorithm given in Section 12.2.

2. Simulated tempering: Consider the Cauchy model, $y_i \sim \text{Cauchy}(\theta, 1)$, $i = 1, \ldots, n$, with two data points, $y_1 = 1.3, y_2 = 15.0$.

    (a) Graph the posterior density.

    (b) Program the Metropolis algorithm for this problem using a symmetric Cauchy jumping distribution. Tune the scale parameter of the jumping distribution appropriately.

    (c) Program simulated tempering with a ladder of 10 inverse-temperatures, $0.1, \ldots, 1$.

    > ✔ Verified: The inverse-temperature ladder from 0.1 to 1 in steps of 0.1 has exactly 10 rungs, with endpoints 0.1 and 1.

    (d) Compare your answers in (b) and (c) to the graph in (a).

3. Hamiltonian Monte Carlo: Program HMC in R for the bioassay logistic regression example from Chapter 3. *[the continuation line "ample from Chapter 3." carries a hand-drawn line — underline or strikethrough, unclear (?) — and there is a squiggle or check-mark (?) in the left margin beside item 3]*

    (a) Code the gradients analytically and numerically and check that the two programs give the same result.

    (b) Pick reasonable starting values for the mass matrix, step size, and number of steps.

    (c) Tune the algorithm to an approximate 65% acceptance rate.

    (d) Run 4 chains long enough so that each has an effective sample size of at least 100. How many iterations did you need?

    (e) Check that your inferences are consistent with those from the direct approach in Chapter 3.

4. Coverage of intervals and rejection sampling: Consider the following model: $y_j \sim \text{Binomial}(n_j, \theta_j)$, where $\theta_j = \text{logit}^{-1}(\alpha + \beta x_j)$, for $j = 1, \ldots, J$, and with independent prior distributions, $\alpha \sim t_4(0, 2^2)$ and $\beta \sim t_4(0, 1)$. Assume $J = 10$, the $x_j$ values are randomly drawn from a $\text{U}(1,1)$ [sic: a degenerate uniform; presumably $\text{U}(-1,1)$] distribution, and $n_j \sim \text{Poisson}^+(5)$, where $\text{Poisson}^+$ is the Poisson distribution restricted to positive values.

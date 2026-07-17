# Mined Sources — what the textbooks silently assume

Reader's-eye complement to the curriculum mining: for each "clearly / it is easily shown / routine / the reader may verify" and each first-chapter exercise trick, the *actual* micro-skill the author expects you to already own. Quotes are trimmed to ≤1 line. Locations are file line numbers (CB/booklet) or extracted PDF page numbers.

Method note: Casella–Berger `Ch1to5.txt` contains the chapter text twice (constant +423-line offset in Ch.1); I cite the first occurrence. MCMT's PDF font is subsetted and drops most lowercase letters on extraction — its rows are grounded in the structure/equations that *did* survive plus the surviving symbols (transition matrix, `∑_y P(x,y)=1`, eq. 1.1). Lawler, ISLP, Montgomery extracted cleanly.

---

## 1. Casella–Berger, *Statistical Inference*, Ch. 1–5 (PRIMARY)

Hedge-phrase census (Ch.1–5, single copy): `verify` 50, `note that` 48, `recall` 27, `easily` 22, `straightforward` 17, `it follows` 11, `obvious` 10, `it is easy` 6, `clearly` 6, `trivial` 4.

| skill | source:location | the assuming passage | what's actually needed |
|---|---|---|---|
| **Kernel recognition** (the marquee CB trick) | Ch1to5:1442, 2444, 2567, 3590, 3766 | "We now recognize the integrand … as the kernel of another gamma pdf" | know each named density's functional form well enough to read off its normalizer, so `∫kernel = 1/const` without integrating |
| Completing the square in an exponent | Ch1to5:1733 | "We now complete the square in the exponent; that is, we write" | algebra `ax²+bx = a(x+b/2a)² − b²/4a`; recognize the leftover constant factors out of the integral |
| Jacobian / bivariate change of variables | Ch1to5:3569, 3579, 3626, 4055 | "the role played by a derivative … is now played by … the Jacobian" | invert `u=g₁, v=g₂` for `x,y`; build & evaluate the 2×2 (or n×n) determinant of partials; take `|J|` |
| Determine the image set B and check 1-to-1 | Ch1to5:3575 | "as difficult to determine the set B and verify that the transformation is one-to-one" | track how the support region maps; split domain into pieces where g is monotone (many-to-one case) |
| mgf via kernel/Taylor | Ch1to5:1442, 2295 | "The mgf can also be obtained by a straightforward calculation … from the Taylor series of eʸ" | `M(t)=E e^{tX}`; recognize `∑ λˣ/x! = e^λ`, `∑ e^{tx}·pmf` reshuffled into a known series |
| Index-shift substitution `y=x−1` | Ch1to5:1174, 2289, 2191 | "(substitute y = x−1)" then re-sum to 1 | shift a summation index and re-identify the shifted sum as a full pmf/known series summing to 1 |
| Geometric-series & partial-sum recall | Ch1to5:1810, 2382 | "Recall the partial sum of the geometric series" | `∑aⁿ=1/(1−a)`, `∑_{k=0}^{n} = (1−aⁿ⁺¹)/(1−a)` produced from memory |
| Binomial / negative-binomial theorem | Ch1to5:2241, 2348, 3563 | "which bears a striking resemblance to the binomial distribution" | `(x+y)ⁿ=∑C(n,k)xᵏyⁿ⁻ᵏ`, incl. extension to negative exponents |
| Integration by parts with the right `u,dv` | Ch1to5:2463 | "we use the integration by parts substitution u=t^{α−1}, dv=e^{−t/β}dt" | pick `u,dv` so the boundary term vanishes and the residual integral is a lower-order Γ |
| Standardizing substitution `t=(x−μ)/σ` | Ch1to5:2494, 2737 | "(substitute t = (x−μ)/σ)" | linear change of variable in an integral, carrying the `dx=σ dt` factor and reducing to the standard form |
| Symmetry ⇒ halve/zero an integral | Ch1to5:2507, 3819 | "integrand is symmetric around 0, implying the integral over (−∞,0) = … (0,∞)" | recognize even/odd integrands; `∫odd over symmetric range = 0` |
| Indicator-function bookkeeping | Ch1to5:2682, 3367, 3519 | "This is made more obvious by using an indicator function to write" | fold the support into `I_A(x)`; use `E[I_A]=P(A)`, `I_A·I_B = I_{A∩B}` |
| Chebychev via `E[g(X)]≥…` truncation | Ch1to5:2817, 2831 | "its proof is almost trivial … Doing some obvious algebra" | bound an expectation by restricting the integral to the tail event; Markov's inequality as the engine |
| "Doing the obvious"/"×(x/x)" algebra | Ch1to5:1719, 2898 | "where we have multiplied the integrand by x/x" | multiply-by-1 / add-and-subtract to manufacture a recognizable form |
| Differentiate-under-the-integral (Leibniz) | Ch1to5:1605, 1651, 1779 | "interchange of derivative and integral … equates a partial with an ordinary derivative" | conditions for swapping `d/dθ` and `∫`; mean value theorem to bound the difference quotient |
| Exponential-family factoring & support test | Ch1to5:2678, 2690 | "the set … cannot depend on θ in an exponential family" | pattern-match `h(x)c(θ)exp{∑wᵢ(θ)tᵢ(x)}`; know why a θ-dependent support disqualifies it |
| Bivariate-normal conditional read-off | Ch1to5:3905, 3914 | "it is straightforward to verify that the conditional distribution of Y given X=x is" | complete-the-square in two variables / partitioned-Gaussian algebra to extract conditional mean & variance |
| Delta method (Taylor + Slutsky) | Ch1to5:4766, 4816, 4841 | "these rather straightforward approximations are good enough to obtain a CLT" | first-order Taylor of `g(Yₙ)` about `θ`, plus convergence-in-probability of the remainder |
| **Exercise tricks (Ch.1–2):** set-identity containment proofs | Ch1to5:65 | "We first show that A∩(B∪C) ⊂ (A∩B)∪(A∩C)" | double-inclusion (`⊂` both ways) element-chasing; DeMorgan; disjointification `Aᵢ* = Aᵢ\∪_{j<i}Aⱼ` |
| **Exercise tricks:** permutations-with-repetition / double counting | Ch1to5:352 | "there is a bit of double counting here … divide by 2!" | `k!/(k₁!…kₘ!)`; count-then-correct-for-overcount reasoning |
| **Exercise tricks:** sampling-without-replacement counts | Ch1to5:318, 2973 | "Obviously, we are sampling without replacement" | `C(n,k)`, ordered vs unordered, hypergeometric setup |

## 2. Bayesian booklet (lecture notes — bigger jumps)

The scanned notes carry a referee's `> ✔ Verified:` line at each jump, which itself names the assumed skill. That makes the booklet a ready-made catalog of "one line of the notes = one page of hidden work."

| skill | source:location | the assuming passage | what's actually needed |
|---|---|---|---|
| Posterior = likelihood×prior → **kernel read-off** | ch01:244, ch03:310/322/336, ch03:853 | "π(p∣y) ∝ p^{y+α−1}(1−p)^{n+β−y−1}" [Beta kernel, unstated] | drop the normalizer, multiply exponents, recognize the standard family and its updated parameters |
| Complete-the-square in μ ⇒ Normal posterior | ch03:336, ch03:1040 | "Normal likelihood × normal prior is a normal kernel in μ with precision n/σ²+1/δ²" | Gaussian×Gaussian precision-addition; posterior mean = precision-weighted average |
| **Integrate out a nuisance parameter** to a marginal | ch05:37, ch10:292, ch08:819 | "integrating σ² out … leaves a marginal for μ proportional to (1+t²/(n−1))^{−n/2}" | recognize the σ²-integral as an inverse-gamma normalizer; land on the Student-t kernel |
| Sum-of-squares split `∑(yᵢ−μ)² = (n−1)s² + n(ȳ−μ)²` | ch05:37 | stated as a step inside the t-marginal derivation | add-and-subtract ȳ; cross-term vanishes because `∑(yᵢ−ȳ)=0` |
| Jacobian of a reparametrization cancels a factor | ch05:176, ch10:391, ch11:584/640 | "(1+α)^{−2} times the Jacobian |dα/dφ| equals 1" | change of variable in a density, `π_φ(φ)=π_α(α)|dα/dφ|`; verify the algebra actually cancels |
| Laplace approx: `−H`, `|−H|^{1/2}` | ch03:547, ch03:577 | "|−H|^{1/2} = 1/(√2 (σ²)^{3/2})" | second derivative of log-posterior (observed information), determinant of the Hessian, `∝` vs `=` |
| Detailed balance ⇒ stationarity | ch11:39, ch11:41, ch11:55 | "α(x,y)=min{1, π(y)q(y,x)/(π(x)q(x,y))} satisfies detailed balance" | verify `π(x)P(x,y)=π(y)P(y,x)` by the min-symmetry trick; know it implies invariance & reversibility |
| Monte Carlo error / CLT for estimators | ch05:516, ch05:552 | "s/√M is the Monte Carlo error … θ̂_M → E(θ|x) a.s." | SLLN/CLT applied to sample averages; `SE = s/√M` |
| "Proof. Straightforward." | ch08:119 | *Proof.* Straightforward. | the reader supplies the entire (omitted) argument |

## 3. Lawler, *Stochastic Calculus* (Ch. 1–2, measure-lite entry)

| skill | source:PDF pg | the assuming passage | what's actually needed |
|---|---|---|---|
| σ-algebra as "information" | pg 9–10 | "F_n is the smallest sub-σ-algebra … X₁,…,Xₙ are G-measurable" | read `σ(X₁,…,Xₙ)` as a filtration; measurability = "knowable from the data so far" |
| Conditional expectation as a **random variable** | pg 9–11 | "E[Y∣F_n] is F_n-measurable … the unique r.v. satisfying" | shift from `E[Y∣X=x]` (a number) to `E[Y∣F]` (a function of ω); defining property `E[Y·1_A]=E[E[Y∣F]1_A]` |
| Tower / law of total expectation via double integral | pg 10 | "E[E[Y∣X]] = ∫∫ y f(x,y)dy dx = E[Y]" | Fubini swap of the iterated integral; recover the marginal |
| Integrability caveat `E|Y|<∞` | pg 8–9 | "we assume Y is an [integrable] r.v., meaning E[Y]<∞" | know why conditional expectation needs L¹, silently invoked |

## 4. Levin–Peres, *Markov Chains & Mixing Times* (MCMT), Ch. 1

| skill | source:PDF pg | the assuming passage | what's actually needed |
|---|---|---|---|
| Transition matrix / stochastic matrix | pg 17 | "the row-sums of P … ∑_{y∈X} P(x,y)=1 for x∈X" | a matrix whose rows are probability distributions; multiply distributions by P on the right |
| Markov property as a factored conditional | pg 17 (eq 1.1) | "P{X_{t+1}=y ∣ H_{t−1}, X_t=x} = P(x,y)" | conditioning collapses to the last state; history drops out |
| n-step law via matrix powers | pg 17–18 | (implied by transition-matrix framing) | `Pⁿ(x,y)` = (x,y) entry of the matrix power; distribution evolves as `μₙ = μ₀Pⁿ` |
| Stationary distribution as left eigenvector | pg (§1.5, "Stationary Distributions") | section heading + `πP=π` framing | solve `πP=π`, `∑π=1`; eigenvalue-1 left eigenvector |

## 5. James et al., *ISLP*, Ch. 2

| skill | source:PDF pg | the assuming passage | what's actually needed |
|---|---|---|---|
| Reducible/irreducible error split | pg 26 | "depends on two quantities … reducible error and the irreducible error" | `Y=f(X)+ε`; only `f` is estimable, `Var(ε)` is a floor |
| **Bias–variance decomposition** `E(y₀−f̂)² = Var(f̂)+Bias²+Var(ε)` | pg 33–34 | "expected test MSE can never lie below Var(ε)" | expand a squared error, take expectation over training sets, cross-term vanishes; all three pieces ≥0 |
| Expectation over the training-set distribution | pg 33 | "variance … amount by which f̂ would change … using a different training data set" | treat f̂ itself as random; expectations are over the resampled data, not the test point |
| "since the error term averages to zero" | pg 25 | "since the error term averages to zero, we can predict Y using Ŷ=f̂(X)" | `E[ε]=0` used to justify plugging in the mean |

Note: ISLP boasts it "almost completely avoided the use of matrix algebra" (pg 24) — but Ch.3 onward silently needs `(XᵀX)⁻¹XᵀY`, so the matrix-form linear model is a deferred, not removed, prerequisite.

## 6. Montgomery, *Design and Analysis of Experiments* (546), Ch. 2

| skill | source:PDF pg | the assuming passage | what's actually needed |
|---|---|---|---|
| Expand the corrected sum of squares | pg 46–47 | "SS is the corrected sum of squares … S² is an unbiased estimator of σ²" | `∑(yᵢ−ȳ)² = ∑yᵢ²−nȳ²`; take `E[·]` term by term to show `E[S²]=σ²` |
| **Degrees of freedom = independent elements** | pg 47 | "only n−1 of them are independent, because ∑(yᵢ−ȳ)=0" | one linear constraint removes one df; general rule `E[SS]=ν·σ²` |
| `SS/σ² ~ χ²_{n−1}`, and t, F sampling distributions | pg 48–49 | "SS/σ² is distributed as chi-square with n−1 degrees of freedom" | know χ²=sum of squared standard normals, `t=Z/√(χ²/ν)`, `F=(χ²/u)/(χ²/v)` — used, never derived |
| Two-sample pooled-variance t-test | pg 55, 56 (§ pooled) | "Both use Pooled Std. Dev. … Assuming equal variances" | pool `S_p² = [(n₁−1)S₁²+(n₂−1)S₂²]/(n₁+n₂−2)`; form `t₀=(ȳ₁−ȳ₂)/(S_p√(1/n₁+1/n₂))` |
| Variance of a sample mean | pg 12 | "if σ² is the variance … the variance of the sample mean is σ²/n" | `Var(ȳ)=σ²/n` from independence, invoked as background |

---

## Cross-source frequency summary (skills ranked by how many sources lean on them)

| rank | skill | sources that assume it |
|---|---|---|
| 1 | **Recognize a density kernel / normalizer** (drop constants, name the family, read `∫=1`) | CB, booklet — pervasive in both; underpins ISLP's `f` framing too |
| 2 | **Substitution / change of variable in an integral or sum** (index shift, standardize, Jacobian) | CB, booklet, Lawler |
| 3 | **Expand a sum/integral of squares & take term-wise expectation** (cross-term vanishes) | CB, booklet, ISLP, Montgomery |
| 4 | **Completing the square** (1-D exponent and partitioned-Gaussian) | CB, booklet |
| 5 | **Law of total expectation / tower property / Fubini swap** | CB, booklet, Lawler |
| 6 | **Standard-family fluency** (gamma, beta, normal, χ²/t/F forms & interrelations from memory) | CB, booklet, Montgomery |
| 7 | **Geometric / binomial / Taylor series summed to a closed form** | CB, booklet (MC error) |
| 8 | **Indicator-function algebra** (`E[I_A]=P(A)`, support bookkeeping) | CB, booklet |
| 9 | **Proportionality reasoning `∝` vs `=`** (posterior up to a constant; Laplace `|−H|`) | booklet, CB |
| 10 | **Degrees-of-freedom / constraint counting** | Montgomery, CB (χ² df) |

## Skills the SOURCES assume but the curriculum's modules deliberately avoided

These are out of the course's chosen scope (SYLLABUS softens rigor and treats measure theory / MCMT / matrix proofs "by concept"), yet a learner *reading these very textbooks onward* will hit them:

- **Measure-theoretic σ-algebra & conditional expectation as a random variable** — Lawler (pg 9–11) makes it the load-bearing object; the course keeps conditioning at the `E[Y∣X=x]` level (M02) and flags Borel–Kolmogorov only as a cautionary tale. Needed for any martingale/stochastic-calculus reading.
- **Filtrations & martingale property** — Lawler ch.1; the course invokes "posterior is a martingale" (SYLLABUS §M08/optional-stopping) as a *fact* without the discrete-time martingale machinery behind it.
- **Multivariate transformation mechanics (n×n Jacobians, many-to-one partitions)** — CB §4.3/4.6; the course uses reparametrization results (e.g. RJMCMC bijection Jacobians, booklet ch11) but doesn't drill the determinant computation.
- **Sampling-distribution derivations (χ², t, F from normal samples; df bookkeeping)** — Montgomery ch.2 & CB ch.5; the course lives in the Bayesian frame and cites these frequentist pivots (M08 bridge) rather than deriving them.
- **Matrix-form linear model & matrix calculus** (`(XᵀX)⁻¹XᵀY`, `∂/∂β` of a quadratic form) — ISLP defers it and Montgomery's later chapters need it; the course's regression modules (M14–15) present results without the matrix-cookbook identities (`∂(xᵀAx)/∂x = 2Ax`, Woodbury) that the sources assume for onward reading.
- **Combinatorial counting fluency** (permutations-with-repetition, hypergeometric double-counting) — CB ch.1 exercises; the course opens at applied conditioning (M00–02) and doesn't rebuild the counting layer.

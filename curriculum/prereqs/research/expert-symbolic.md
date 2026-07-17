# Symbolic Fluency: The Invisible Wall Inventory

Prerequisite micro-skills for Bayesian statistics & ML, covering **symbolic
fluency** only: (i) algebra of probability densities, (ii) the expectation
operator as a tool, (iii) inequalities & bounding reflexes, (iv)
Taylor/asymptotic reasoning, (v) calculus under the integral sign, (vi)
counting/combinatorial hygiene.

These are *not* concepts. They are the automatic hand-motions that strong CS +
applied-math undergrads are assumed to have but usually don't. A student can
"understand" conjugacy and still be unable to *do* it, because the doing is 90%
kernel-spotting and normalizing-constant bookkeeping. Each record below is a
reflex an expert fires without conscious thought, the textbook line that stalls a
student lacking it, a 5-minute installation drill, and a diagnostic item.

Grades: **GATE** blocks whole topics until acquired; **FRICTION** slows every
derivation but doesn't halt it; **POLISH** is a finish-quality refinement.

Notation: `∝` = "proportional to", `∫` unadorned = over the whole support,
`N(μ,σ²)` = normal with that mean/variance, `1{·}` = indicator.

---

## Area (i): Algebra of Probability Densities

The single richest vein of invisible walls. Conjugate Bayes is *entirely* this
area. If a student cannot manipulate a density as an algebraic object —
separating what depends on the variable from what doesn't — they cannot do
Bayesian inference at all, no matter how well they grasp the philosophy.

### GATE — "Spot the kernel"
- **The reflex:** Given a messy density, instantly split it into `kernel(x) ·
  (stuff that doesn't depend on x)`, and recognize the kernel as belonging to a
  named family, reading off its parameters — without computing any integral.
- **The wall:** "The posterior is proportional to `θ^(a+Σxᵢ−1) (1−θ)^(b+n−Σxᵢ−1)`,
  hence `θ | x ∼ Beta(a+Σxᵢ, b+n−Σxᵢ)`." The student stares: *where did the
  normalizing constant come from? how do we know it's a Beta?* They try to
  integrate and drown.
- **The 5-minute fix:** Write the Beta(α,β) density and cover the
  `1/B(α,β)` with your thumb. What's left is `θ^(α−1)(1−θ)^(β−1)` — *that's the
  kernel, and it alone determines the distribution*. Drill: match kernels to
  families by inspection —
  `x^3 e^(−2x)` → Gamma(shape 4, rate 2);
  `e^(−x²/8)` → Normal(0, 4) (since `−x²/(2σ²)` ⇒ σ²=4);
  `θ^5(1−θ)^2` → Beta(6,3);
  `λ^k e^(−λ)/k!` viewed *as a function of λ* → Gamma kernel `λ^k e^(−λ)`, not
  Poisson. Verify one in scipy: `beta(6,3).pdf(t)` vs `t**5*(1-t)**2` differ only
  by the constant `1/B(6,3)`; `import numpy as np; from scipy.stats import beta;
  t=0.4; print(beta(6,3).pdf(t), (t**5*(1-t)**2)/beta_fn(6,3))` match.
- **Self-test:** A density on `(0,∞)` is proportional to `x^2 e^(−5x)`. Name the
  distribution and its mean. **Answer:** Gamma(shape 3, rate 5), mean 3/5 = 0.6.
- **Grade: GATE.**

### GATE — "∝ in which variable?"
- **The reflex:** Every `∝` silently carries a subscript naming the *one* variable
  it holds; anything not that variable is a constant and gets absorbed. You always
  know which variable you're proportional-in.
- **The wall:** "As a function of θ, `p(x|θ)p(θ) ∝ θ^(Σxᵢ)(1−θ)^(n−Σxᵢ) · θ^(a−1)(1−θ)^(b−1)`
  — the `1/x!` factors and the `B(a,b)` drop out." Student objects that
  `1/(x₁!···xₙ!)` "isn't a constant, it has data in it" and refuses to drop it,
  or conversely drops a `θ`-dependent term thinking it's constant.
- **The 5-minute fix:** State the rule out loud: *in `p(θ|x) ∝ p(x|θ)p(θ)`, the
  proportionality is in θ; the data x are frozen.* So `x!` is a number (a big one,
  but fixed) and vanishes; `θ^x` stays. Drill: for `p(x|θ)=θ^x e^(−θ)/x!` with
  x=3 observed, write "as a function of θ" the kernel: `θ^3 e^(−θ)`. The `1/3!` is
  gone. Now flip it: "as a function of x" (θ frozen), the kernel is `θ^x/x!`.
  Same formula, opposite deletions.
- **Self-test:** In `θ^x (1−θ)^(n−x) · \binom{n}{x}`, treated as a function of θ,
  which factors survive? **Answer:** `θ^x(1−θ)^(n−x)`; the binomial coefficient is
  a θ-constant and drops.
- **Grade: GATE.**

### GATE — "Restore the constant by pattern, not by integrating"
- **The reflex:** Once the kernel is identified, write the full normalized density
  by recalling the family's constant — never by evaluating `∫ kernel dx`.
- **The wall:** "Therefore the normalizing constant is `Γ(α)/λ^α`, and
  `p(x)=λ^α x^(α−1)e^(−λx)/Γ(α)`." Student who doesn't recognize the Gamma tries
  to compute `∫₀^∞ x^(α−1)e^(−λx)dx` from scratch, gets stuck at the Gamma
  integral, and stalls the whole derivation.
- **The 5-minute fix:** Memorize the "kernel → constant" table for the five
  workhorses. Beta kernel `θ^(α−1)(1−θ)^(β−1)` → constant `1/B(α,β)`. Gamma kernel
  `x^(α−1)e^(−λx)` → `λ^α/Γ(α)`. Gaussian kernel `e^(−(x−μ)²/2σ²)` →
  `1/√(2πσ²)`. Poisson kernel `λ^x/x!` → `e^(−λ)`. Then the game is: see kernel,
  *look up* constant. Sanity-check numerically that `∫ kernel = 1/constant`:
  `from scipy.integrate import quad; quad(lambda x: x**2*np.exp(-5*x),0,np.inf)`
  returns ≈ 0.016 = Γ(3)/5³ = 2/125.
- **Self-test:** The kernel `e^(−(x−3)²/8)` integrates to what over ℝ?
  **Answer:** `√(2π·4)=√(8π)≈5.013` (σ²=4).
- **Grade: GATE.**

### GATE — "Product of likelihoods → sum in the exponent"
- **The reflex:** An iid product `∏ᵢ p(xᵢ|θ)` collapses: exponents add, `θ`-powers
  add, and sufficient statistics (`Σxᵢ`, `Σxᵢ²`, `Σlog xᵢ`, `n`) fall out
  mechanically.
- **The wall:** "The likelihood is `∏ᵢ (1/√(2πσ²)) exp(−(xᵢ−μ)²/2σ²) =
  (2πσ²)^(−n/2) exp(−Σ(xᵢ−μ)²/2σ²)`." Student can't see how the product became a
  single exp with a sum, or how the `n/2` power appeared.
- **The 5-minute fix:** Two laws: `∏ e^(aᵢ)=e^(Σaᵢ)` and `∏ c = c^n`. Apply to n=2
  by hand: `e^(a₁)·e^(a₂)=e^(a₁+a₂)`; `c·c=c²`. Then a Bernoulli product:
  `∏ θ^(xᵢ)(1−θ)^(1−xᵢ) = θ^(Σxᵢ)(1−θ)^(n−Σxᵢ)`. The whole n-dimensional dataset
  entered through just `Σxᵢ` and `n` — that's sufficiency appearing for free.
- **Self-test:** For n iid Poisson(λ), the likelihood as a function of λ has
  kernel `λ^? e^(?)`. **Answer:** `λ^(Σxᵢ) e^(−nλ)`.
- **Grade: GATE.**

### GATE — "Complete the square in the exponent"
- **The reflex:** When two Gaussian exponents multiply, gather the `x²` and `x`
  coefficients, complete the square, and read off the new mean and variance —
  discarding the leftover constant into `∝`.
- **The wall:** "Combining prior and likelihood, the posterior precision is
  `1/τ² = 1/σ₀² + n/σ²` and posterior mean is the precision-weighted average."
  Student sees `exp(−(x−μ₀)²/2σ₀² − Σ(xᵢ−x̄)²/2σ² − n(x̄−μ)²/2σ²)` and cannot
  reorganize it into `exp(−(μ−μ_n)²/2τ²)`.
- **The 5-minute fix:** The identity: `a·x² − 2b·x = a(x − b/a)² − b²/a`. Practice
  with numbers: `3x² − 12x = 3(x−2)² − 12`. In a density, `exp(−½(ax²−2bx))` is a
  Gaussian with mean `b/a` and variance `1/a` — the `−b²/a` goes into the
  constant. Drill: multiply `exp(−x²/2)·exp(−(x−4)²/2)`, collect: `−½(2x²−8x)+c
  = −½·2(x−2)²+c'`, so mean 2, variance ½. Confirm: two N with precisions 1,1 →
  posterior precision 2, mean (0+4)/2=2. ✓
- **Self-test:** `exp(−½(4x² − 8x))` is proportional to a Gaussian with what mean
  and variance? **Answer:** mean 1, variance 1/4.
- **Grade: GATE.**

### GATE — "Conditional vs joint density factoring"
- **The reflex:** Read `p(x,y)=p(y|x)p(x)` and its rearrangement
  `p(x|y)=p(x,y)/p(y)=p(y|x)p(x)/∫p(y|x)p(x)dx` as pure algebra you can run in
  either direction, knowing exactly which variable each factor is a density in.
- **The wall:** "Bayes' rule: `p(θ|x)=p(x|θ)p(θ)/p(x)` where
  `p(x)=∫p(x|θ)p(θ)dθ`." Student conflates `p(x|θ)` (a density in x, a likelihood
  in θ) with `p(θ|x)`, and doesn't see the denominator as "the numerator summed
  over θ."
- **The 5-minute fix:** A 2×2 numeric joint table. `p(x,θ)` for x∈{0,1}, θ∈{0,1}:
  [[0.1,0.2],[0.3,0.4]]. Compute `p(θ)` = column sums, `p(x)` = row sums,
  `p(θ|x=1)` = row-1 entries ÷ row-1 sum. Notice `p(θ|x)` and `p(x|θ)` use
  *different* denominators (row vs column sums) — that's why they differ. The
  continuous `∫` denominator is literally this row-sum.
- **Self-test:** With joint `p(x,θ)` as above, is `p(x=1|θ=1)` equal to
  `p(θ=1|x=1)`? Give both. **Answer:** No. `p(x=1|θ=1)=0.4/0.6≈0.667`;
  `p(θ=1|x=1)=0.4/0.7≈0.571`.
- **Grade: GATE.**

### FRICTION — "Change of variables carries a Jacobian"
- **The reflex:** Transforming a density is never just substitution; the `|dx/dy|`
  factor is mandatory, and you write it before you forget.
- **The wall:** "If `Y=g(X)` then `p_Y(y)=p_X(g⁻¹(y))|d g⁻¹/dy|`." Student
  transforms `Y=X²` or `Y=log X` and drops the Jacobian, getting a non-normalizing
  "density."
- **The 5-minute fix:** `X∼Uniform(0,1)`, `Y=−log X`. Then `x=e^(−y)`,
  `|dx/dy|=e^(−y)`, so `p_Y(y)=1·e^(−y)` = Exponential(1). Check in numpy:
  `x=np.random.rand(100000); y=-np.log(x); np.mean(y)` ≈ 1.0, and histogram
  matches `e^(−y)`. Drop the Jacobian and you'd wrongly predict Uniform.
- **Self-test:** `X∼Exp(1)`, `Y=X²`. What is `p_Y(y)` for y>0?
  **Answer:** `p_Y(y)=e^(−√y)/(2√y)`.
- **Grade: FRICTION.** (Blocks reparameterization/diffusion derivations; elsewhere
  survivable.)

### FRICTION — "Marginalize by integrating out the nuisance"
- **The reflex:** To get `p(x)` from `p(x,θ)`, integrate over θ; recognize when the
  inner integral is itself a recognizable normalizing constant so no work is
  needed.
- **The wall:** "The marginal likelihood is `∫ θ^(Σx) (1−θ)^(n−Σx) dθ =
  B(Σx+1, n−Σx+1)`." Student doesn't see that integrating a Beta *kernel* just
  gives back its Beta *constant*.
- **The 5-minute fix:** The trick: `∫ (kernel of a known density) = 1/(its
  constant)`, because the real density integrates to 1. So `∫₀¹ θ^2(1−θ)^3 dθ =
  B(3,4) = Γ(3)Γ(4)/Γ(7) = 2·6/720 = 1/60`. Verify:
  `quad(lambda t:t**2*(1-t)**3,0,1)` ≈ 0.01667 = 1/60.
- **Self-test:** `∫₀^∞ x^4 e^(−3x) dx = ?` **Answer:** `Γ(5)/3⁵ = 24/243 ≈ 0.0988`.
- **Grade: FRICTION.**

### FRICTION — "Indicator/support bookkeeping"
- **The reflex:** Track the support with `1{·}` factors; when you transform or
  condition, update the support, and never let a density leak outside where it
  lives.
- **The wall:** "For `X∼Uniform(0,θ)`, the likelihood is `θ^(−n) 1{θ ≥ max xᵢ}`."
  Student writes `θ^(−n)` and forgets the indicator, then "maximizes" over all θ
  and gets θ→0 nonsense, missing that the constraint θ ≥ max xᵢ is the whole game.
- **The 5-minute fix:** Write `Uniform(0,θ)` density as `(1/θ)1{0≤x≤θ}`. Product
  over n points: `θ^(−n) ∏1{0≤xᵢ≤θ} = θ^(−n)1{θ≥max xᵢ}1{min xᵢ≥0}`. The `max` is
  where all n indicators simultaneously hold. That indicator is exactly why the
  MLE is `max xᵢ`, not something from `d/dθ`.
- **Self-test:** `X₁,...,Xₙ ∼ Uniform(0,θ)`. Where does the likelihood put its
  mass, and where is it maximized? **Answer:** zero for θ<max xᵢ, decreasing
  `θ^(−n)` for θ≥max xᵢ; maximized at θ=max xᵢ.
- **Grade: FRICTION.**

### POLISH — "Log-density is your working form"
- **The reflex:** Reach for `log p` by default — products become sums, exponents
  come down, and the algebra flattens; exponentiate only at the very end.
- **The wall:** "Maximizing the likelihood is equivalent to maximizing the
  log-likelihood." Student keeps differentiating products via the product rule and
  makes errors that logs would erase.
- **The 5-minute fix:** Take `L(θ)=θ^(Σx)(1−θ)^(n−Σx)`, then `ℓ=Σx·logθ +
  (n−Σx)log(1−θ)`, `ℓ'=Σx/θ − (n−Σx)/(1−θ)=0` ⇒ `θ̂=Σx/n` in three lines vs a
  product-rule mess.
- **Self-test:** `log` of `(2πσ²)^(−n/2) exp(−S/2σ²)` is? **Answer:**
  `−(n/2)log(2πσ²) − S/(2σ²)`.
- **Grade: POLISH.**

---

## Area (ii): The Expectation Operator as a Tool

Students treat `E[·]` as "the average, a number you compute at the end."
Experts treat it as a *linear operator you push around* — through sums, out of
constants, into and out of conditioning. The gap between these two stances is
the difference between fluency and paralysis in half of statistics.

### GATE — "Linearity needs no independence"
- **The reflex:** `E[aX+bY+c]=aE[X]+bE[Y]+c`, *always*, correlated or not; you
  split expectations of sums without a second thought and without checking
  independence.
- **The wall:** "By linearity, `E[Σᵢ Xᵢ]=Σᵢ E[Xᵢ]`, even though the Xᵢ are
  dependent." Student hesitates: "don't we need independence?" and refuses to
  split, or wrongly thinks they must model the dependence first.
- **The 5-minute fix:** Contrast the two rules explicitly. Linearity of E: no
  independence needed. Factoring `E[XY]=E[X]E[Y]`: *needs* independence. Prove
  linearity is free with maximally-dependent variables: `X` and `Y=X`,
  `X∼Bernoulli(0.5)`. `E[X+Y]=E[2X]=1=E[X]+E[Y]=0.5+0.5`. ✓ But
  `E[XY]=E[X²]=0.5≠E[X]E[Y]=0.25`. So sums are free, products are not.
- **Self-test:** In a hypergeometric draw (sampling without replacement, so draws
  are dependent), is `E[Σ indicators]=Σ E[indicator]` valid? **Answer:** Yes —
  linearity never needs independence.
- **Grade: GATE.**

### GATE — "Tower / law of total expectation"
- **The reflex:** `E[X]=E[E[X|Y]]` — condition on the convenient variable, take the
  inner expectation, then average over the conditioner. Reach for it whenever a
  distribution is defined hierarchically.
- **The wall:** "By iterated expectation, `E[X]=E_θ[E[X|θ]]` and
  `Var(X)=E[Var(X|θ)]+Var(E[X|θ])`." Student has memorized the slogan but can't
  execute: doesn't know which variable to condition on or how to collapse the two
  layers.
- **The 5-minute fix:** Poisson–Gamma by hand. `X|λ∼Poisson(λ)`, `λ∼Gamma(2,1)`
  (mean 2). Then `E[X]=E[E[X|λ]]=E[λ]=2`. No integral over x needed — just plug
  the inner mean and average. Check by simulation:
  `lam=np.random.gamma(2,1,10**6); x=np.random.poisson(lam); x.mean()` ≈ 2.0.
  Then variance: `E[Var(X|λ)]+Var(E[X|λ])=E[λ]+Var(λ)=2+2=4`; `x.var()`≈4. ✓
- **Self-test:** `N∼Poisson(10)`, and given N, `X∼Binomial(N,0.3)`. Find `E[X]`.
  **Answer:** `E[E[X|N]]=E[0.3N]=0.3·10=3`.
- **Grade: GATE.**

### GATE — "E[g(X)] is LOTUS, not g(E[X])"
- **The reflex:** To get `E[g(X)]`, integrate `g(x)` against the density
  (law of the unconscious statistician); never substitute `E[X]` into g.
- **The wall:** "`E[X²]=∫x²p(x)dx=Var(X)+E[X]²`, which is *not* `E[X]²`." Student
  writes `E[X²]=(E[X])²` and every variance/MGF/entropy computation downstream is
  wrong.
- **The 5-minute fix:** `X∼Uniform(0,1)`: `E[X]=1/2` so `g(E[X])=1/4`. But
  `E[X²]=∫₀¹x²dx=1/3`. `1/3≠1/4`; the gap `1/3−1/4=1/12` is exactly Var(X). The
  operator goes *inside* g's argument only if g is linear.
- **Self-test:** `X∼Exp(1)` (so `E[X]=1`). Is `E[X²]=1`? **Answer:** No;
  `E[X²]=2` (it's `Var+mean²=1+1`).
- **Grade: GATE.**

### GATE — "Why E[1/X] ≠ 1/E[X]"
- **The reflex:** Any nonlinear transform breaks pass-through; for convex g like
  `1/x` you even know the *direction* (`E[1/X] ≥ 1/E[X]`) by Jensen, and you never
  cancel an expectation through a reciprocal.
- **The wall:** "The harmonic-mean / inverse-variance weighting: note
  `E[1/X]>1/E[X]`." Student silently used `E[1/X]=1/E[X]` three steps earlier and
  the estimator is biased.
- **The 5-minute fix:** `X` uniform on {1,2}. `E[X]=1.5`, `1/E[X]=0.667`. But
  `E[1/X]=(1+0.5)/2=0.75 > 0.667`. The reciprocal is convex, so Jensen pushes
  E[1/X] up. Bigger spread ⇒ bigger gap: try {1,10}: `1/E[X]=1/5.5≈0.18` vs
  `E[1/X]=(1+0.1)/2=0.55`. Huge.
- **Self-test:** `X` uniform on {2,4}. Which is larger, `E[1/X]` or `1/E[X]`, and
  by how much? **Answer:** `E[1/X]=0.375 > 1/E[X]=1/3≈0.333`; gap ≈ 0.042.
- **Grade: GATE.**

### FRICTION — "Variance algebra: expand then take E"
- **The reflex:** `Var(X)=E[X²]−E[X]²` and `Var(aX+b)=a²Var(X)` are reflexes;
  `Var(X+Y)=Var X+Var Y+2Cov(X,Y)` with the cross term never forgotten.
- **The wall:** "`Var(X̄)=σ²/n` because `Var(ΣXᵢ)=nσ²` under independence." Student
  forgets `Var` pulls out `a²` (writes `σ²/n²·n²`... or drops the square), or drops
  the covariance term when variables are dependent.
- **The 5-minute fix:** Derive `Var(X̄)`: `Var((1/n)ΣXᵢ)=(1/n²)Var(ΣXᵢ)=(1/n²)·nσ²
  =σ²/n`. The `1/n²` comes from the constant squaring. For the cross term: `X,Y`
  with `Cov=0.5`, `Var X=Var Y=1`: `Var(X+Y)=1+1+2(0.5)=3`, not 2.
- **Self-test:** `Var(3X−2)` when `Var(X)=4`? **Answer:** `9·4=36` (the −2
  vanishes).
- **Grade: FRICTION.**

### FRICTION — "Indicator trick: E[1{A}]=P(A)"
- **The reflex:** Convert probabilities to expectations of indicators to unlock
  linearity — the standard route to expected counts and coverage.
- **The wall:** "Let `Iⱼ=1{ball j in box 1}`; then expected occupancy is
  `E[ΣIⱼ]=ΣP(Iⱼ=1)`." Student doesn't think to represent a count as a sum of
  indicators and gets tangled in the joint distribution.
- **The 5-minute fix:** Expected number of fixed points of a random permutation of
  n. `Iⱼ=1{j maps to j}`, `P(Iⱼ=1)=1/n`, so `E[#fixed]=Σ(1/n)=1` for any n —
  despite the fixed points being dependent. Verify:
  `np.mean([np.sum(np.random.permutation(20)==np.arange(20)) for _ in range(10000)])`
  ≈ 1.0.
- **Self-test:** 5 letters into 5 envelopes at random. Expected number in the
  correct envelope? **Answer:** 1.
- **Grade: FRICTION.**

### FRICTION — "Pull constants and known factors out of E"
- **The reflex:** Inside `E_x[·]`, anything not random in x is a constant and comes
  out front; you factor the integrand before integrating.
- **The wall:** "`E[θ·f(X)|θ]=θ·E[f(X)|θ]` since θ is fixed given the
  conditioning." Student, mid-hierarchical-model, treats θ as still random inside a
  `E[·|θ]` and can't simplify.
- **The 5-minute fix:** State: `E[·|Y]` treats Y as a *known constant*. So
  `E[Y·X|Y]=Y·E[X|Y]`. Numeric: joint over (X,Y); fix Y=y, the conditional mean of
  `yX` is `y` times the conditional mean of X. This is the engine behind pulling
  the inner expectation in the tower rule.
- **Self-test:** `E[σ²·Z²]` where `Z∼N(0,1)` and σ² is a constant?
  **Answer:** `σ²·E[Z²]=σ²`.
- **Grade: FRICTION.**

### POLISH — "Score has mean zero"
- **The reflex:** `E[∂_θ log p(X|θ)] = 0` under the model — a normalization
  identity you invoke to shortcut Fisher-information and EM derivations.
- **The wall:** "Since the score has expectation zero, the Fisher information is
  `Var(score) = −E[∂²_θ log p]`." Student takes this as magic rather than "the
  derivative of `∫p=1` is `∫∂p=0`."
- **The 5-minute fix:** `∫p(x|θ)dx=1` ⇒ differentiate both sides in θ ⇒
  `∫∂_θ p dx=0` ⇒ `∫(∂_θ log p)p dx=0` ⇒ `E[score]=0`. The `∂_θ log p = ∂_θp/p`
  step is the whole trick. (Requires "differentiate under the integral", below.)
- **Self-test:** For `N(μ,1)`, the score in μ is `(x−μ)`. Its expectation under the
  model? **Answer:** 0.
- **Grade: POLISH.**

---

## Area (iii): Inequalities & Bounding Reflexes

The skill here is *directional intuition* — knowing which way a bound points
before you look it up, and reaching for the right inequality for the job. Missing
this doesn't block a single derivation the way kernel-spotting does, but it makes
students unable to read or trust the bounds that pervade ML theory, variational
inference, and concentration.

### GATE — "Which way does Jensen go?"
- **The reflex:** For convex g, `E[g(X)] ≥ g(E[X])`; for concave, reversed. You fix
  the direction by remembering `x²` (convex, `E[X²]≥E[X]²` ✓) and `log` (concave,
  `E[log X]≤log E[X]`), and you can place any new g instantly.
- **The wall:** "By Jensen's inequality, `log E[·] ≥ E[log ·]`, giving the ELBO as
  a lower bound on the log evidence." Student can't tell whether ELBO is an upper
  or lower bound, so can't reason about whether optimizing it is safe.
- **The 5-minute fix:** Anchor on log (concave, the one VI uses). `X` on {1,4}
  equally: `E[log X]=(0+1.386)/2=0.693`; `log E[X]=log 2.5=0.916`. So
  `E[log X] < log E[X]` — concave dips the average below the function of the
  average. That's exactly why `E_q[log(p/q)] ≤ log E_q[p/q]=log(evidence)`: ELBO
  is a *lower* bound. Flip to `x²` to confirm convex goes the other way:
  `E[X²]=8.5 > E[X]²=6.25`.
- **Self-test:** Is `E[√X]` larger or smaller than `√(E[X])`? **Answer:** smaller
  (√ is concave), so `E[√X] ≤ √E[X]`.
- **Grade: GATE.** (Blocks all of variational inference and EM understanding.)

### FRICTION — "Markov → Chebyshev → Chernoff ladder"
- **The reflex:** To bound a tail, climb the ladder by how much you know: Markov
  (mean only, weak), Chebyshev (variance, `1/k²`), Chernoff/MGF (exponential,
  tight) — and you know each buys tightness for more assumptions.
- **The wall:** "By Chebyshev, `P(|X−μ|≥kσ) ≤ 1/k²`; a Chernoff bound gives the
  exponentially smaller `e^(−k²/2)`." Student doesn't see why two bounds on the
  same event differ, or which to trust.
- **The 5-minute fix:** For `X∼N(0,1)`, bound `P(X≥3)`. Markov (on X, needs X≥0,
  cheat with |X|): loose. Chebyshev: `P(|X|≥3)≤1/9≈0.111`. Chernoff:
  `≤e^(−9/2)≈0.011`. Truth: `1−Φ(3)≈0.00135`. See the ladder tighten toward truth
  as assumptions grow. `from scipy.stats import norm; norm.sf(3)` = 0.00135.
- **Self-test:** Chebyshev's bound on `P(|X−μ|≥2σ)`? **Answer:** `1/4`.
- **Grade: FRICTION.**

### FRICTION — "Cauchy–Schwarz / correlation lives in [−1,1]"
- **The reflex:** `|E[XY]| ≤ √(E[X²]E[Y²])`, equivalently `|Cov(X,Y)| ≤ σ_X σ_Y`,
  so correlation is bounded by 1 and equality means linear dependence.
- **The wall:** "By Cauchy–Schwarz, the correlation coefficient satisfies
  `|ρ|≤1`." Student takes `|ρ|≤1` as a definition-fact rather than a consequence
  they could derive, and can't recognize C–S when it appears un-labeled in a
  variance bound.
- **The 5-minute fix:** `Cov(X,Y)=E[XY]−E[X]E[Y]`. C–S on the centered variables:
  `|Cov| ≤ √(Var X · Var Y)`. Divide through: `|ρ|≤1`. Numeric near-equality: let
  `Y=2X+tiny noise`; compute `np.corrcoef` → ≈ 0.999, approaching the C–S
  equality case (exact linear relation).
- **Self-test:** If `Var X=9`, `Var Y=16`, what's the largest `Cov(X,Y)` can be?
  **Answer:** 12.
- **Grade: FRICTION.**

### FRICTION — "AM–GM and log-sum reflexes"
- **The reflex:** Arithmetic mean ≥ geometric mean, with equality iff all equal;
  used to bound products by sums and to see why entropy/KL are ≥ 0.
- **The wall:** "`KL(p‖q) ≥ 0` with equality iff `p=q`, by Gibbs' inequality."
  Student can't connect this to any inequality they know and treats non-negativity
  of KL as an axiom.
- **The 5-minute fix:** AM–GM on two numbers: `(a+b)/2 ≥ √(ab)`; try (1,9):
  5 ≥ 3 ✓. Then Gibbs via Jensen: `KL(p‖q)=E_p[log(p/q)]=−E_p[log(q/p)] ≥
  −log E_p[q/p] = −log Σ q = −log 1 = 0`. The single Jensen step (log concave)
  delivers `KL≥0`. Equality iff `q/p` is constant, i.e. `p=q`.
- **Self-test:** `KL(p‖q)` when `p=q`? **Answer:** exactly 0.
- **Grade: FRICTION.**

### POLISH — "Union bound as the crude first move"
- **The reflex:** `P(∪Aᵢ) ≤ ΣP(Aᵢ)` — your default first bound when events pile up,
  knowing it's loose but always valid.
- **The wall:** "By a union bound over the `m` hypotheses, the family-wise error is
  at most `mα`." Student worries whether independence is needed (it isn't) and
  can't sanity-check the Bonferroni correction.
- **The 5-minute fix:** 20 independent tests at α=0.05. `P(at least one false
  positive) ≤ 20·0.05 = 1`. Exact: `1−0.95²⁰≈0.64`. The union bound (1) is a valid
  but loose ceiling over the truth (0.64). Never needs independence to hold.
- **Self-test:** Union bound on `P(A∪B)` when `P(A)=P(B)=0.3`? **Answer:** `≤0.6`.
- **Grade: POLISH.**

---

## Area (iv): Taylor / Asymptotic Reasoning

This is the machinery behind the Laplace approximation, the delta method,
Bernstein–von Mises, and every "for large n, ≈ Gaussian" statement in the course.
The wall is that students can *state* a Taylor series but can't *use* it as an
approximation tool: they don't know which terms to keep, don't recognize a
quadratic expansion as a Gaussian, and panic at big-O.

### GATE — "Second-order expansion = Gaussian approximation"
- **The reflex:** Expand `log p(θ)` to second order around its mode; the quadratic
  term *is* a Gaussian log-density, so you read off a Normal approximation with
  variance = inverse of the negative second derivative.
- **The wall:** "The Laplace approximation: `log p(θ|x) ≈ log p(θ̂|x) −
  ½(θ−θ̂)ᵀ H (θ−θ̂)`, so `θ|x ≈ N(θ̂, H⁻¹)` where H is the negative Hessian." Student
  sees the Taylor expansion but doesn't recognize that a quadratic in the exponent
  means Gaussian, nor why the linear term vanished.
- **The 5-minute fix:** Two moves. (1) At a mode, the first-derivative term is 0,
  so expansion starts at the quadratic. (2) `exp(−½ a (θ−θ̂)²)` is a Gaussian
  kernel with variance `1/a`. Concrete: approximate a Gamma(3,1) posterior near its
  mode θ̂=2. `log p = 2logθ − θ + c`; `d/dθ=2/θ−1=0`→θ̂=2; `d²/dθ²=−2/θ²=−0.5` at
  θ̂; so `a=0.5`, Laplace says `N(2, 2)`. (True Gamma(3,1) has mean 3, var 3 — the
  approximation is crude for small shape but exact-in-form, and improves as data
  accumulate.)
- **Self-test:** If `−d²/dθ² log p(θ̂|x) = 4` at the mode, the Laplace posterior
  variance is? **Answer:** 1/4.
- **Grade: GATE.**

### GATE — "Keep the right order; know what you drop"
- **The reflex:** `f(x₀+h) ≈ f(x₀)+f'(x₀)h+½f''(x₀)h²`, and you consciously choose
  where to truncate based on what you're computing (mean needs 1st order, variance
  needs 2nd).
- **The wall:** "To first order, `g(X) ≈ g(μ)+g'(μ)(X−μ)`, so `Var(g(X)) ≈
  g'(μ)²Var(X)` — the delta method." Student either keeps too few terms (loses the
  variance) or too many (unusable), not seeing that variance is a first-order
  (in the *deviation*) computation.
- **The 5-minute fix:** Delta method for `g(X)=log X`, `X∼N(10, 1)`. `g'(10)=0.1`,
  so `Var(log X) ≈ 0.1²·1 = 0.01`, `SD ≈ 0.1`. Simulate:
  `np.log(np.random.normal(10,1,10**6)).var()` ≈ 0.0101. ✓ The linear term alone
  nailed the variance.
- **Self-test:** `X∼N(4,0.25)`, `g(X)=√X`. Delta-method Var(√X)?
  **Answer:** `g'(4)=1/(2√4)=0.25`; `Var ≈ 0.25²·0.25 = 0.015625`.
- **Grade: GATE.**

### FRICTION — "e^x, log(1+x), (1+x)^n small-x expansions"
- **The reflex:** `e^x≈1+x+x²/2`, `log(1+x)≈x−x²/2`, `(1+x)^n≈1+nx` for small x —
  instant, used to linearize and to derive limits.
- **The wall:** "For small ε, `log(1+ε) ≈ ε`, hence the log-likelihood ratio is
  approximately..." Student can't approximate and carries exact logs through,
  obscuring the leading behavior.
- **The 5-minute fix:** Show `(1+1/n)^n → e`: `log((1+1/n)^n)=n·log(1+1/n)≈
  n·(1/n)=1`, so the limit is `e¹=e`. Check n=1000:
  `(1+1/1000)**1000` ≈ 2.7169 vs e=2.71828. The `log(1+x)≈x` reflex made the limit
  fall out in one line.
- **Self-test:** Approximate `e^(0.02)` to 2 significant figures without a
  calculator. **Answer:** `≈1.02` (1+0.02).
- **Grade: FRICTION.**

### FRICTION — "Stirling for factorials/Gammas"
- **The reflex:** `log n! ≈ n log n − n` (+ ½log(2πn)); reach for it whenever
  factorials appear in an asymptotic or an exponent.
- **The wall:** "By Stirling, `\binom{n}{k} ≈ 2^(nH(k/n))` for the entropy H."
  Student sees factorials in a large-n limit and has no tool to tame them.
- **The 5-minute fix:** `log 10! `: Stirling `10 log10 − 10 = 23.03−10=13.03`;
  add ½log(20π)=2.07 → 15.10. True `log(3628800)=15.10`. ✓ Two-term Stirling is
  excellent even at n=10.
- **Self-test:** Using `log n!≈n log n − n`, approximate `log 100!` (natural log).
  **Answer:** `≈100·4.605−100=460.5−100=360.5` (true ≈ 363.7).
- **Grade: FRICTION.**

### POLISH — "Big-O / o(·) hygiene"
- **The reflex:** Read `O(1/n)`, `o(1)`, `+ o_p(1)` as size statements you can
  drop or keep deliberately, and never confuse "converges" with "equals."
- **The wall:** "`θ̂ = θ + O_p(n^(−1/2))`, so the estimator is √n-consistent."
  Student can't parse the rate and doesn't see why `n^(−1/2)` (not `n⁻¹`) is the
  canonical statistical rate.
- **The 5-minute fix:** SE of the mean shrinks like `σ/√n`: quadruple n → halve the
  error. Simulate the SD of `X̄` over n∈{25,100,400}:
  ≈ σ/5, σ/10, σ/20. The `n^(−1/2)` rate is visible as the halving.
- **Self-test:** To cut a Monte Carlo standard error in half, multiply the sample
  size by what? **Answer:** 4.
- **Grade: POLISH.**

---

## Area (v): Calculus Under the Integral Sign

Narrow but load-bearing: normalization, moments, MGFs, the EM/score identities,
and Fisher information all depend on moving a derivative or a parameter through an
integral. Students freeze because they were told (correctly, but unhelpfully)
that "you can't always do this," and so never build the reflex for when you can.

### GATE — "Normalization is a global constraint you exploit"
- **The reflex:** `∫p(x|θ)dx=1` for *every* θ is not a fact to prove but a tool: it
  makes normalizing constants recognizable, kills nuisance integrals, and (when
  differentiated) yields the score identity.
- **The wall:** "Since the density integrates to 1 for all θ, differentiating gives
  `∫∂_θ p dx = 0`." Student never thought of "=1" as something you could
  differentiate, and misses the entire family of identities that follow.
- **The 5-minute fix:** Use it as an integral evaluator: to find `∫₀^∞ λe^(−λx)dx`
  just note it's an Exp(λ) density → 1, no work. Then differentiate the constraint
  for `N(μ,1)`: `∫p=1` ⇒ `∫(x−μ)p dx=0` ⇒ `E[X]=μ`. The mean fell out of
  normalization + one derivative.
- **Self-test:** `∫₋∞^∞ (1/√(2π)) e^(−x²/2) dx = ?` (no computation).
  **Answer:** 1.
- **Grade: GATE.**

### GATE — "Differentiate under the integral (Leibniz)"
- **The reflex:** For nice integrands, `d/dθ ∫f(x,θ)dx = ∫∂_θ f(x,θ)dx`; you swap
  freely for the exponential-family densities in this course and know the swap
  generates moments and scores.
- **The wall:** "Differentiating the MGF, `M'(t)=E[X e^(tX)]`, and `M'(0)=E[X]`."
  Student doesn't believe you can move `d/dt` inside `E[·]=∫·p dx` and is stuck
  proving each moment separately.
- **The 5-minute fix:** MGF of Exp(1): `M(t)=∫₀^∞ e^(tx)e^(−x)dx=1/(1−t)` for t<1.
  Then `M'(t)=1/(1−t)²`, `M'(0)=1=E[X]`; `M''(0)=2=E[X²]`. Each derivative pulled
  an extra `x` inside the integral. Verify moments: Exp(1) has mean 1, `E[X²]=2`. ✓
- **Self-test:** From `M(t)=e^(t²/2)` (standard normal MGF), find `E[X²]` via
  `M''(0)`. **Answer:** `M'(t)=t e^(t²/2)`, `M''(0)=1`, so `E[X²]=1`.
- **Grade: GATE.**

### FRICTION — "Moments via ∫ xⁿ p — set up the integral right"
- **The reflex:** `E[Xⁿ]=∫xⁿp(x)dx`; you set the integrand and limits correctly and
  recognize the result as a shifted Gamma/Beta constant rather than grinding.
- **The wall:** "`E[X²]` for Gamma(α,λ) is `α(α+1)/λ²`." Student sets up
  `∫x²·λ^αx^(α−1)e^(−λx)/Γ(α)dx` and doesn't see it as `Γ(α+2)/Γ(α)/λ²`.
- **The 5-minute fix:** The move: `∫x^n · x^(α−1)e^(−λx)dx = ∫x^(α+n−1)e^(−λx)dx =
  Γ(α+n)/λ^(α+n)`. So `E[X^n]=Γ(α+n)/(Γ(α)λ^n)`. For n=1: `Γ(α+1)/Γ(α)/λ=α/λ`. ✓
  Raising the moment just shifts the Gamma's shape parameter.
- **Self-test:** `E[X³]` for Exp(1) (=Gamma(1,1))? **Answer:** `Γ(4)/Γ(1)=3!=6`.
- **Grade: FRICTION.**

### FRICTION — "Fubini: swap the order of integration/summation"
- **The reflex:** For non-negative or absolutely-integrable integrands, swap `∫∫`
  order (or `Σ∫`, `ΣΣ`) to do the easy one first — a routine, licensed move.
- **The wall:** "Interchanging sum and integral, `E[X]=∫₀^∞ P(X>t)dt` for X≥0."
  Student can't see how a double integral got reordered into the survival-function
  formula.
- **The 5-minute fix:** The tail-sum identity: `E[X]=∫₀^∞P(X>t)dt` comes from
  writing `X=∫₀^∞1{X>t}dt` and swapping `E` and `∫`. Check Exp(1):
  `∫₀^∞ e^(−t)dt=1=E[X]`. ✓ For a die: `E=Σ_{t≥1}P(X≥t)=6/6+5/6+...+1/6=21/6=3.5`.
- **Self-test:** `X` = roll of a fair die. Compute `E[X]` as `ΣP(X≥t)`.
  **Answer:** `(6+5+4+3+2+1)/6 = 3.5`.
- **Grade: FRICTION.**

### POLISH — "Gaussian & Gamma integrals as known constants"
- **The reflex:** `∫e^(−ax²)dx=√(π/a)` and `∫₀^∞x^(s−1)e^(−x)dx=Γ(s)` are
  memorized; you never re-derive them mid-problem.
- **The wall:** "Completing the Gaussian integral, `∫e^(−(x−μ)²/2σ²)dx=√(2πσ²)`."
  Student stalls trying to antidifferentiate `e^(−x²)`, which has no elementary
  antiderivative.
- **The 5-minute fix:** `∫₋∞^∞ e^(−ax²)dx=√(π/a)`. Set a=1/(2σ²): get `√(2πσ²)`.
  Memorize the one Gaussian constant and rescale. Check a=1:
  `quad(lambda x:np.exp(-x**2),-np.inf,np.inf)`=√π≈1.7725.
- **Self-test:** `∫₋∞^∞ e^(−3x²)dx = ?` **Answer:** `√(π/3)≈1.023`.
- **Grade: POLISH.**

---

## Area (vi): Counting / Combinatorial Hygiene

The least glamorous, most error-prone area. Discrete models (binomial,
multinomial, Poisson processes, Dirichlet-multinomial, Chinese restaurant
process) all rest on counting, and the Gamma function is the bridge between
discrete factorials and continuous densities. Students who "did combinatorics in
high school" carry systematic sloppiness that surfaces as wrong constants.

### GATE — "Gamma function is the factorial"
- **The reflex:** `Γ(n)=(n−1)!` and `Γ(x+1)=xΓ(x)`; you move between factorials and
  Gammas without a blink, and know Beta/Gamma constants are factorials in disguise.
- **The wall:** "`B(α,β)=Γ(α)Γ(β)/Γ(α+β)`, which for integer args is
  `(α−1)!(β−1)!/(α+β−1)!`." Student sees Γ and treats it as an exotic special
  function, not "factorial with a shift," and can't simplify Beta constants.
- **The 5-minute fix:** The off-by-one: `Γ(5)=4!=24`, `Γ(1)=0!=1`,
  `Γ(1/2)=√π`. Recurrence: `Γ(x+1)=xΓ(x)` mirrors `n!=n·(n−1)!`. Compute `B(2,3)`
  two ways: `Γ(2)Γ(3)/Γ(5)=1·2/24=1/12`; and `1!·2!/4!=2/24=1/12`. ✓
  `from scipy.special import gamma; gamma(5)` = 24.0.
- **Self-test:** `Γ(6)/Γ(4) = ?` **Answer:** `5!/3! = 120/6 = 20`.
- **Grade: GATE.**

### GATE — "Binomial coefficient: choose vs order"
- **The reflex:** `\binom{n}{k}=n!/(k!(n−k)!)` counts *unordered* selections; you
  know when order matters (permutations, `n!/(n−k)!`) versus not, and never
  double-count or under-count by a `k!`.
- **The wall:** "The number of ways to assign is `n!/(n₁!n₂!...n_k!)`, the
  multinomial coefficient." Student can't see this as repeated `\binom` choices and
  can't tell it from a plain factorial.
- **The 5-minute fix:** Count arrangements of "MISSISSIPPI" (11 letters:
  1 M, 4 I, 4 S, 2 P): `11!/(1!4!4!2!)=34650`. Build it as sequential choices:
  `\binom{11}{1}\binom{10}{4}\binom{6}{4}\binom{2}{2}`. Verify:
  `from math import comb, factorial; factorial(11)//(1*24*24*2)` = 34650.
- **Self-test:** How many distinct arrangements of the letters in "LEVEL"?
  **Answer:** `5!/(2!2!1!) = 30`.
- **Grade: GATE.**

### FRICTION — "Sum over configurations = product of sums (factoring)"
- **The reflex:** Recognize when `Σ_configs ∏ᵢ f(xᵢ) = ∏ᵢ (Σ f(xᵢ))` — an
  independent-choices sum factors into a product, and vice versa. The backbone of
  partition-function and normalizing-constant tricks.
- **The wall:** "The partition function `Z=Σ_x ∏ᵢ φ(xᵢ) = ∏ᵢ Σ_{xᵢ} φ(xᵢ)`
  factorizes when there are no interaction terms." Student sees an exponentially
  large sum over all configurations and doesn't realize independence collapses it
  to a small product.
- **The 5-minute fix:** Two binary variables, `Σ_{a,b∈{0,1}} f(a)g(b)`. Expand:
  `f(0)g(0)+f(0)g(1)+f(1)g(0)+f(1)g(1) = (f(0)+f(1))(g(0)+g(1))`. The `2ⁿ`-term sum
  is really an `n`-fold product of 2-term sums. This is exactly why a product of
  independent normalizers multiplies, and why `Σ` and `∏` swap in the ELBO.
- **Self-test:** `Σ_{x₁,x₂,x₃∈{0,1}} 2^(x₁+x₂+x₃)` equals? **Answer:**
  `(1+2)³ = 27`.
- **Grade: FRICTION.**

### FRICTION — "Read Σ and ∫ indices correctly"
- **The reflex:** Instantly identify the bound (dummy) index vs free variables, the
  limits, and whether nested sums are independent or coupled — before manipulating.
- **The wall:** "`Σ_{i=1}^n Σ_{j=1}^i a_{ij}`" — the inner limit depends on the
  outer index. Student treats it as a full `n×n` sum, or swaps the order without
  adjusting limits, and gets the wrong count.
- **The 5-minute fix:** `Σ_{i=1}^3 Σ_{j=1}^i 1` counts pairs with `j≤i`:
  i=1→1, i=2→2, i=3→3, total 6 = `3·4/2`, the triangular number, *not* 9. Swapping
  order requires `Σ_{j=1}^3 Σ_{i=j}^3`. Also drill the dummy-index rule: `Σ_i a_i`
  and `Σ_k a_k` are identical; `i` is not free.
- **Self-test:** `Σ_{i=1}^4 Σ_{j=1}^i 1 = ?` **Answer:** `1+2+3+4 = 10`.
- **Grade: FRICTION.**

### FRICTION — "Expand (a+b)² and multinomial expansions without fear"
- **The reflex:** `(a+b)²=a²+2ab+b²`, `(Σxᵢ)²=Σxᵢ²+2Σ_{i<j}xᵢxⱼ`, and the binomial
  theorem — expanded mechanically, cross-terms never dropped.
- **The wall:** "`E[(ΣXᵢ)²]=ΣE[Xᵢ²]+ΣᵢΣ_{j≠i}E[XᵢXⱼ]`" — the origin of the
  variance-of-a-sum. Student expands `(ΣXᵢ)²` and forgets the `2Σ_{i<j}` cross
  terms, halving or losing the covariance.
- **The 5-minute fix:** Expand `(a+b+c)²` fully: `a²+b²+c²+2ab+2ac+2bc` — 3 squares,
  3 cross-terms, each doubled. Count: `n` squares, `\binom{n}{2}` distinct
  cross-pairs. For `(x₁+x₂)²` with the middle `2x₁x₂`: this `2` is exactly the
  `2Cov` in `Var(X+Y)`.
- **Self-test:** Expand `(a+b)³`. **Answer:** `a³+3a²b+3ab²+b³`.
- **Grade: FRICTION.**

### POLISH — "Empty product = 1, empty sum = 0, 0! = 1"
- **The reflex:** Edge conventions are automatic: `∏` over nothing is 1, `Σ` over
  nothing is 0, `0!=1`, `\binom{n}{0}=1`, `x⁰=1` — so base cases and boundary
  terms never derail you.
- **The wall:** "For k=0, `\binom{n}{0}p⁰(1−p)ⁿ=(1−p)ⁿ`." Student is unsure whether
  `p⁰` and `0!` behave, and mishandles the k=0 (or n=0) term in a recursion or
  normalization check.
- **The 5-minute fix:** Confirm the binomial sums to 1 *including* endpoints:
  `Σ_{k=0}^n \binom{n}{k}p^k(1−p)^(n−k)=(p+(1−p))^n=1`. The k=0 term needs
  `p⁰=1`, `\binom{n}{0}=1`; the k=n term needs `(1−p)⁰=1`. Without the
  conventions the sum wouldn't close.
- **Self-test:** `\binom{5}{0} + \binom{5}{5} = ?` **Answer:** `1+1 = 2`.
- **Grade: POLISH.**

---

## Summary Counts

| Area | GATE | FRICTION | POLISH | Total |
|---|---|---|---|---|
| (i) Density algebra | 6 | 3 | 1 | 10 |
| (ii) Expectation operator | 4 | 3 | 1 | 8 |
| (iii) Inequalities & bounds | 1 | 3 | 1 | 5 |
| (iv) Taylor / asymptotics | 2 | 2 | 1 | 5 |
| (v) Under the integral sign | 2 | 2 | 1 | 5 |
| (vi) Counting / combinatorics | 2 | 3 | 1 | 6 |
| **Total** | **17** | **16** | **6** | **39** |

**Cross-cutting note for the curriculum designers:** the density-algebra GATEs
(kernel-spotting, ∝-discipline, completing the square, restoring the constant)
are the true chokepoint — they appear on nearly every page of conjugate Bayes and
compound with each other. A student missing three of them cannot follow a single
posterior derivation, no matter how well the concept is explained. Diagnose and
remediate these *first*. The expectation-operator GATEs (linearity-without-
independence, tower rule, LOTUS, E[1/X]≠1/E[X]) are the second cluster, gating
hierarchical models and all variance decompositions. "Which way does Jensen go"
single-handedly gates variational inference. The Taylor GATEs gate the Laplace
approximation and delta method. These four clusters, in this order, are the
symbolic spine of the course.

# Expert-Computational Prerequisite Skills

The micro-skills a Bayesian/ML course silently assumes. Scope: **(i) transforms & domain-matching, (ii) the working linear algebra of statistics, (iii) numerical computing craft, (iv) simulation discipline.** These are the reflexes that separate someone who *understands the math* from someone whose sampler actually converges and whose plot is actually right. Density algebra, expectation tools, inequalities, and asymptotics are covered elsewhere; I flag boundary cases but do not develop them.

Learner: CS + applied-math undergrad, numpy/scipy-fluent, 2-CPU box. So the bar is not "can you differentiate" but "is this an automatic habit under time pressure, in the middle of debugging a model." Grades:

- **GATE** — if this is missing, work downstream is *wrong or stuck*, often silently. Must be installed before the course.
- **FRICTION** — slows everything and causes recurring small bugs; install early, reinforce throughout.
- **POLISH** — the mark of fluency; makes code clean and fast, rarely the cause of a wrong answer.

Counts and top GATEs are in the return summary. Records below are grouped by area, GATEs first within each area.

---

## Area I — Transforms & Domain-Matching

The unifying idea the whole course leans on: **optimizers and samplers want to live in unconstrained ℝⁿ.** A parameter with a constrained domain (a variance in (0,∞), a probability in (0,1), a simplex of mixing weights) must be mapped to ℝ, worked on there, and mapped back — and *the density carries a Jacobian toll every time you cross.* Half the "my sampler is broken" tickets are a missing constraint or a missing log|f'|.

### GATE — The domain dictionary

- **The reflex:** See a constrained parameter, and *immediately* know the standard bijection to ℝ and its inverse — before writing any model code.
- **The wall:** You put a `sigma > 0` parameter into a Gaussian random-walk Metropolis proposal. The proposal steps to `sigma = -0.3`, `logpdf` returns `nan`, and every subsequent state is rejected or `nan`-poisoned. The chain flatlines and you blame the step size.
- **The 5-minute fix:** Memorize the four canonical maps and their inverses by typing them once:

  | domain | forward (→ℝ) | inverse (ℝ→domain) |
  |---|---|---|
  | (0,∞) | `y = log(x)` | `x = exp(y)` |
  | (0,1) | `y = logit(x) = log(x/(1-x))` | `x = expit(y) = 1/(1+exp(-y))` |
  | (a,b) | `logit((x-a)/(b-a))` | `a + (b-a)*expit(y)` |
  | simplex Δ_{K} | K−1 free logits, `softmax` back | `x = softmax(y)` (one d.o.f. fixed) |
  | ordered x₁<…<x_K | first + `log` of gaps | `cumsum` of `[x1, exp(δ)...]` |

  ```python
  from scipy.special import expit, logit, softmax
  # sample a positive param in unconstrained space, work, map back
  y = rng.normal(0, 1)         # lives in R, samplers love it
  sigma = np.exp(y)            # always > 0, no rejection ever
  ```
- **Self-test:** A mixture has weights w on the 3-simplex. How many *unconstrained* real coordinates parameterize it, and why not 3? **Answer:** 2 (= K−1); the simplex sums to 1, so it is a 2-D surface in ℝ³ — a softmax over 3 logits is over-parameterized by exactly one shift-invariant direction.

### GATE — The Jacobian price (change-of-variables toll)

- **The reflex:** Every time you transform a random variable, you automatically add `+ log|det J|` (or subtract, depending on direction) to the log-density — writing the correction *in the same keystroke* as the transform.
- **The wall:** You reparameterize σ = exp(y) to sample y ∈ ℝ, but score y with `logpdf_of_sigma(exp(y))` and forget the `+ y` (= log|dσ/dy|). The posterior over y is subtly wrong — biased toward small σ — and nothing errors. You only notice because your credible interval disagrees with a conjugate check. (This is the single most common *silent* transform bug.)
- **The 5-minute fix:** Derive the univariate rule from the CDF in three lines, then instrument it:

  ```
  Y = f(X), f monotone.  F_Y(y) = P(f(X) ≤ y) = F_X(f⁻¹(y))
  p_Y(y) = d/dy F_X(f⁻¹(y)) = p_X(f⁻¹(y)) · |d f⁻¹/dy|
  in logs:  log p_Y(y) = log p_X(x) + log|dx/dy|
  ```
  ```python
  # target: sigma ~ HalfNormal, sample in y = log sigma
  from scipy.stats import halfnorm
  def logp_y(y):
      s = np.exp(y)
      return halfnorm.logpdf(s) + y   # <-- the +y is log|d sigma/d y|
  # drop the +y and the mode/quantiles shift; that's the toll you owe.
  ```
- **Self-test:** X ~ Uniform(0,1), Y = −log X. What is p_Y(y) for y > 0, and what is the |f'| factor? **Answer:** p_Y(y) = e^{−y} (Exponential(1)); |dx/dy| = |−(−e^{−y})|... x = e^{−y}, dx/dy = −e^{−y}, |dx/dy| = e^{−y}, times p_X = 1 ⇒ e^{−y}.

### GATE — Why unconstrained space is where inference lives

- **The reflex:** Before running *any* gradient sampler or optimizer on a constrained model, you transform to ℝⁿ, add the log-Jacobian, and run the algorithm there — and you know PyMC/Stan do this for you (and *why* their reported "sd" of a positive param can look odd).
- **The wall:** You hand-roll HMC on a positivity-constrained target in the original coordinates. Leapfrog momentum kicks the position negative; the potential is `+inf` there; the trajectory reflects chaotically and acceptance craters. Or in ADVI/Laplace you fit a Gaussian to a (0,1) parameter and get mass outside [0,1].
- **The 5-minute fix:** Contrast the two worlds on a one-liner target:

  ```python
  # Gaussian (Laplace/VI) approx to a Beta(2,2) is bad in x, fine in logit-x
  from scipy.stats import beta, norm
  x = np.linspace(1e-3, 1-1e-3, 500)
  # in constrained space: a Normal must spill past 0 and 1  -> mismatch
  # in y = logit(x): the log-posterior is bell-ish -> Normal fits well
  ```
  The takeaway to say out loud: *gradient methods assume the sample space is all of ℝⁿ; make it so, then pay the Jacobian.*
- **Self-test:** Why does a Gaussian variational/Laplace approximation to a positive scale parameter work far better after a `log` transform? **Answer:** in log-space the domain is all of ℝ (no boundary to spill over) and the log-posterior of a scale parameter is much closer to symmetric-quadratic, so the Gaussian's support and shape both match.

### FRICTION — Location–scale as an identity habit

- **The reflex:** You reflexively read any "nice" distribution as `μ + σ·Z` (Z standardized), and standardize/de-standardize without thinking — for sampling, for CDFs, for reparameterization.
- **The wall:** You need N(3, 4) samples but `randn` gives N(0,1); or you compute `norm.cdf(x, loc, scale)` by hand and put σ where σ² belongs. Worse: you write a hierarchical model in "centered" form (`theta ~ N(mu, tau)`) and NUTS gets a divergence-riddled funnel that a non-centered `theta = mu + tau*z, z~N(0,1)` would have dissolved.
- **The 5-minute fix:**

  ```python
  z = rng.standard_normal(10000)
  x = 3 + 2*z                      # N(mean=3, sd=2). sd=2, NOT var=2.
  assert abs(x.mean()-3) < 0.05 and abs(x.std()-2) < 0.05
  # non-centered reparam (the funnel-killer):
  # centered:      theta ~ Normal(mu, tau)
  # non-centered:  z ~ Normal(0,1); theta = mu + tau*z
  ```
- **Self-test:** If Z ~ N(0,1), what are the mean and variance of a + bZ, and which of loc/scale in `scipy.stats.norm` is b? **Answer:** mean a, variance b²; `scale = b` (the sd), not the variance.

### FRICTION — Standardize before you think

- **The reflex:** Before fitting, plotting, or setting a prior, you z-score the data (and know when to un-standardize the results) so that "1 unit" means "1 sd" and priors/condition numbers behave.
- **The wall:** You regress house price (~10⁵) on rooms (~5). The design matrix is wildly ill-conditioned, the optimizer crawls, a N(0,1) prior on the price-coefficient is absurdly tight, and gradient steps that suit one column overshoot the other.
- **The 5-minute fix:**

  ```python
  Xs = (X - X.mean(0)) / X.std(0)   # now every column is O(1)
  # fit in standardized space, then map coefficients back:
  # y = b0 + sum_j bj * (xj - mj)/sj  =>  original slope_j = bj / sj
  ```
  State the payoff: standardization makes priors interpretable, conditions the Hessian, and equalizes step sizes.
- **Self-test:** After standardizing predictor xⱼ (mean mⱼ, sd sⱼ) and fitting slope b̃ⱼ, what is the slope in original units? **Answer:** b̃ⱼ / sⱼ (and the intercept absorbs the −Σ b̃ⱼ mⱼ/sⱼ shift).

### POLISH — The ordered / cumulative transform

- **The reflex:** For an *ordered* vector (cutpoints of an ordinal model, monotone spline, sorted latent) you parameterize the first element freely and the positive gaps via `exp`, reconstructing with `cumsum`.
- **The wall:** You sample K cutpoints independently, the sampler proposes c₃ < c₂, the ordinal likelihood produces a negative category probability, and you get `nan` or a subtly reordered category.
- **The 5-minute fix:**

  ```python
  y = rng.normal(size=5)                       # unconstrained in R^K
  cuts = np.concatenate([y[:1], np.exp(y[1:])]).cumsum()  # strictly increasing
  assert np.all(np.diff(cuts) > 0)
  # Jacobian toll for the gaps: + sum(y[1:])
  ```
- **Self-test:** To keep x₁<x₂<x₃ while sampling in ℝ³, what do you exponentiate? **Answer:** the two gaps (x₂−x₁, x₃−x₂); x₁ stays free, then `cumsum`.

---

## Area II — The Working Linear Algebra of Statistics

Not "can you prove rank-nullity" but the *manipulations you do fifty times a day*: reading a quadratic form as a distance, completing the square in matrix form, switching between covariance and precision, factoring with Cholesky instead of inverting, reasoning about ellipses via eigenvalues. This is where "I know linear algebra" and "I can implement a Gaussian model" diverge.

### GATE — Cholesky is the workhorse; never invert explicitly

- **The reflex:** Whenever you see Σ⁻¹, `solve`, a MVN sample, or a log-det, you reach for `cholesky` + `solve_triangular` — and you *never* type `np.linalg.inv`.
- **The wall:** `np.linalg.inv(Sigma)` on a near-singular kernel matrix returns garbage with huge entries; `x @ inv(S) @ x` is both slower and less accurate than a solve; and `np.linalg.det(S)` underflows to 0.0 for a 500×500 covariance, so `log(det)` = −inf. Your GP log-likelihood is `nan` and you can't tell why.
- **The 5-minute fix:** The three things Cholesky (Σ = L Lᵀ, L lower-triangular) gives you at once:

  ```python
  from scipy.linalg import cho_factor, cho_solve, solve_triangular
  L = np.linalg.cholesky(Sigma)                  # O(n^3/3), once
  # (1) SOLVE  Sigma^{-1} b  without inverting:
  c = cho_solve((L, True), b)
  # (2) LOG-DET  cheaply & stably:
  logdet = 2.0 * np.log(np.diag(L)).sum()
  # (3) SAMPLE  x ~ N(mu, Sigma):
  x = mu + L @ rng.standard_normal(len(mu))
  # quadratic form  b^T Sigma^{-1} b via triangular solve:
  z = solve_triangular(L, b, lower=True); q = z @ z
  ```
- **Self-test:** Given Σ = L Lᵀ, express log det Σ using L, and say why it beats `log(det(Σ))`. **Answer:** 2·Σ log Lᵢᵢ; it sums logs (no under/overflow) whereas det multiplies n eigenvalues and underflows/overflows for large or ill-conditioned Σ.

### GATE — Quadratic forms are (squared) distances

- **The reflex:** You read `(x−μ)ᵀ Σ⁻¹ (x−μ)` on sight as a squared *Mahalanobis* distance — a rescaled/rotated Euclidean distance — not as an opaque scalar.
- **The wall:** You can't tell why a MVN's contours are tilted ellipses; you treat the exponent as a black box and can't debug why one direction is "penalized" more; you compute per-point outlier scores with Euclidean distance and miss that a correlated pair makes an off-axis point far *in Σ⁻¹ metric*.
- **The 5-minute fix:**

  ```python
  # Mahalanobis = Euclidean AFTER whitening by Cholesky
  d = x - mu
  z = solve_triangular(L, d, lower=True)   # L L^T = Sigma
  maha2 = z @ z                            # == d @ inv(Sigma) @ d
  # Sigma^{-1} sets the metric: big eigenvalue of Sigma -> cheap direction
  ```
  The one-liner to internalize: **Σ⁻¹ is a metric; the quadratic form is ‖whitened residual‖².**
- **Self-test:** For Σ = diag(1, 100), which unit-Euclidean direction has the *largest* Mahalanobis distance from the origin, and why? **Answer:** the first axis (variance 1): Σ⁻¹ = diag(1, 0.01), so a step along axis 1 costs 1 vs 0.01 along axis 2 — small-variance directions are "expensive."

### GATE — Covariance ↔ precision, and what conditioning vs marginalizing does

- **The reflex:** You keep both the covariance Σ and precision Λ = Σ⁻¹ views in mind and know the asymmetry cold: **marginalizing is trivial in Σ (slice the block); conditioning is trivial in Λ (slice the block).**
- **The wall:** You need the conditional of a Gaussian block and start inverting big Σ sub-blocks with the Schur-complement formula, making arithmetic errors — when in the precision parameterization the conditional precision is *just the corresponding sub-block of Λ*. Or you claim two variables are independent because a Σ off-diagonal is ~0, forgetting that the *precision* off-diagonal is what encodes conditional independence.
- **The 5-minute fix:** The two facts that make Gaussians easy, stated as a table:

  ```
  Want the marginal p(x_A)?      -> read Sigma_AA         (drop other rows/cols of Σ)
  Want the conditional p(x_A|x_B)? -> precision is Λ_AA   (sub-block of Λ = Σ^{-1})
       conditional mean = μ_A − Λ_AA^{-1} Λ_AB (x_B − μ_B)
  Σ_ij = 0  <=>  marginally independent
  Λ_ij = 0  <=>  conditionally independent given the rest  (Gaussian graphical model)
  ```
- **Self-test:** In a Gaussian, a zero in which matrix means "independent *given all other variables*"? **Answer:** a zero off-diagonal in the **precision** Λ = Σ⁻¹ (that's the graphical-model edge); a zero in Σ means *marginal* independence.

### GATE — Completing the square in matrix form

- **The reflex:** Faced with `exp(−½ xᵀA x + bᵀx)` you instantly read off "Gaussian with precision A, mean A⁻¹b," matching quadratic and linear terms — the engine behind every conjugate Gaussian update.
- **The wall:** Deriving a Gaussian posterior (or the Gaussian conditional, or a Kalman update) you grind through algebra, lose a factor of 2 or a transpose, and land on a "covariance" that isn't symmetric PD. You can't sanity-check because you never isolated the canonical form.
- **The 5-minute fix:** The identity, memorized:

  ```
  −½ xᵀA x + bᵀx  =  −½ (x − A⁻¹b)ᵀ A (x − A⁻¹b)  +  ½ bᵀA⁻¹b
  => distribution is  N(mean = A⁻¹b,  cov = A⁻¹)   [A is the precision]
  ```
  ```python
  # posterior for  y = X beta + noise,  prior beta ~ N(0, tau^2 I), noise var s2:
  A = X.T @ X / s2 + np.eye(p)/tau2     # posterior precision
  b = X.T @ y / s2                      # linear term
  post_mean = np.linalg.solve(A, b)     # = A^{-1} b, via solve not inv
  ```
- **Self-test:** `exp(−½·3·x² + 6x)` (scalar) is proportional to which Gaussian? **Answer:** precision 3 ⇒ variance 1/3, mean = b/A = 6/3 = 2 ⇒ N(2, 1/3).

### FRICTION — Eigen-reasoning for ellipses and positive-definiteness

- **The reflex:** You picture a covariance as an ellipse whose axes are eigenvectors and whose semi-axis lengths scale as √eigenvalue, and you test PD-ness by "does Cholesky succeed / are all eigenvalues > 0."
- **The wall:** A covariance you assembled (e.g. `0.5*(C+C.T)` after some hack, or an empirical Σ from too-few samples) has a tiny negative eigenvalue; `cholesky` throws `LinAlgError: Matrix is not positive definite`, or MVN sampling produces complex numbers. You don't know whether to trust it or fix it.
- **The 5-minute fix:**

  ```python
  w, V = np.linalg.eigh(Sigma)          # eigh: symmetric, real, ascending
  is_pd = np.all(w > 0)
  # "jitter" repair for numerical near-singularity:
  Sigma_pd = Sigma + (1e-8 - min(w.min(),0)) * np.eye(len(Sigma))
  # ellipse: eigenvectors = axes, semi-axis length ∝ sqrt(eigenvalue)
  ```
- **Self-test:** Your empirical covariance from n=5 samples in 20 dimensions — is it PD? **Answer:** No; rank ≤ n−1 = 4 < 20, so it's singular (≥16 zero eigenvalues) — you need shrinkage/regularization before inverting or factoring.

### FRICTION — The hat matrix is a projection

- **The reflex:** You see least squares as *orthogonal projection* onto the column space of X: ŷ = Hy, H = X(XᵀX)⁻¹Xᵀ, and you know H is symmetric idempotent (H² = H) with trace = number of parameters.
- **The wall:** You're confused why residuals are orthogonal to fitted values, why "degrees of freedom" = trace(H) = p, or why leverage hᵢᵢ flags influential points. Effective-df of ridge/smoothers stays mysterious.
- **The 5-minute fix:**

  ```python
  Q, _ = np.linalg.qr(X)         # never form (X^T X)^{-1} explicitly
  H = Q @ Q.T                    # projection onto col(X)
  assert np.allclose(H @ H, H)   # idempotent
  df = np.trace(H)               # = p (rank of X); leverage = np.diag(H)
  # ridge: H_λ = X (X^T X + λI)^{-1} X^T, trace(H_λ) = effective df < p
  ```
- **Self-test:** What is trace(H) for OLS with an intercept and 3 predictors (full rank)? **Answer:** 4 (the number of estimated coefficients = rank of X); it also equals the model degrees of freedom.

### POLISH — log-det vs det (and sign/scale disasters)

- **The reflex:** You never compute a determinant to then take its log; you use `slogdet` or Cholesky diagonals, and you know a determinant is a *volume/scaling factor* that under/overflows fast in high dim.
- **The wall:** `np.linalg.det(Sigma)` on a 200×200 matrix returns `0.0` or `inf`; `log(0.0)` = −inf silently kills your log-likelihood; a negative round-off det makes `log(det)` = `nan`.
- **The 5-minute fix:**

  ```python
  sign, logdet = np.linalg.slogdet(Sigma)   # stable; sign tells you PD-ness
  assert sign > 0
  # or, if you already have Cholesky L:  logdet = 2*np.log(np.diag(L)).sum()
  ```
- **Self-test:** For a 100×100 covariance with every eigenvalue = 0.1, what is det and what is log-det? **Answer:** det = 0.1¹⁰⁰ = 10⁻¹⁰⁰ (underflows toward 0 in float, unusable); log-det = 100·log(0.1) ≈ −230.3 (perfectly fine).

---

## Area III — Numerical Computing Craft

float64 is not ℝ, and numpy's broadcasting is a small language you must actually *speak* rather than pattern-match. This is where the truly *silent* bugs live — the ones that produce a plausible number that is wrong. The brief itself notes a real broadcasting/axis bug shipped in module 16 and was caught only by a cold read; that class of bug is exactly this area.

### GATE — Broadcasting as a mental model (and the axis argument)

- **The reflex:** You predict the output shape of any elementwise op *before running it* by aligning shapes from the right, and you name the axis you reduce over *explicitly and correctly* every time.
- **The wall:** The canonical silent bug: `X - X.mean()` (should be `X.mean(axis=0)`) subtracts a scalar instead of a per-column mean and standardization is quietly wrong. Or `(a[:, None] - b)` where you meant `a - b[:, None]`, producing an (n×m) grid that *broadcasts without error* and poisons a downstream sum. Or `softmax` normalized over the wrong axis so "probabilities" sum to 1 across the batch, not across classes. None of these raise.
- **The 5-minute fix:** Drill shape prediction and axis intent:

  ```python
  a = np.arange(6).reshape(3, 2)      # (3,2)
  # predict THEN check:
  a - a.mean(axis=0)      # (3,2) - (2,)  -> per-column center   ✅
  a - a.mean(axis=1)      # (3,2) - (3,)  -> ValueError!  needs keepdims
  a - a.mean(axis=1, keepdims=True)   # (3,2) - (3,1) -> per-row center ✅
  # rule: align shapes from the RIGHT; dims must be equal or one of them 1
  # habit: for any reduction feeding a broadcast, use keepdims=True
  ```
  Say the rule aloud: *right-align, then each axis must match or be 1; a missing axis is treated as 1.*
- **Self-test:** `x` is shape (100, 3). You write `x / x.sum(axis=1)`. What happens and what did you mean? **Answer:** `ValueError` (100 vs 3 mismatch) if lucky — or a silent wrong broadcast if the numbers happened to align; you meant `x / x.sum(axis=1, keepdims=True)` to normalize each row.

### GATE — logsumexp and the log-domain (never exp a big number)

- **The reflex:** Any sum/normalization of probabilities that live as *logs* goes through `logsumexp`; you compute log-likelihoods and softmaxes in the log domain and never call `exp` on an unshifted large logit.
- **The wall:** A mixture log-likelihood `log(sum(exp(logp)))` with logp ≈ −800 gives `log(0.0)` = −inf (underflow); with logp ≈ +800 gives `exp` = `inf` then `inf/inf` = `nan`. Your EM or importance sampler returns `nan` weights and you can't localize it.
- **The 5-minute fix:** The max-shift trick, then the library call:

  ```
  log Σ exp(a_i) = m + log Σ exp(a_i − m),   m = max a_i   # subtracting m
  ```
  ```python
  from scipy.special import logsumexp, log_softmax
  logZ = logsumexp(logp)                      # stable normalizer
  log_resp = logp - logsumexp(logp)           # responsibilities in log-domain
  # softmax stably: shift by max first (log_softmax does it for you)
  ```
- **Self-test:** `logsumexp([1000, 1000])` — what does it return, and what would naive `log(sum(exp(...)))` give? **Answer:** 1000 + log 2 ≈ 1000.693; naive gives `exp(1000)` = `inf` ⇒ `log(inf)` = `inf` (or overflow warning).

### GATE — float64 truths: cancellation, log1p/expm1, and 1e16+1

- **The reflex:** You reach for `log1p`, `expm1`, and cancellation-safe rearrangements *automatically* near 0 or 1, and you know ~15–16 significant decimal digits is all you get.
- **The wall:** `log(1 + 1e-12)` returns `1.0000...e-12`? No — it loses precision because `1 + 1e-12` rounds. `1 - expit(30)` = `0.0` exactly (should be ~9e-14), so `log(1-p)` = −inf in your Bernoulli likelihood. Computing variance as `E[x²] − E[x]²` gives a *negative* number from catastrophic cancellation. And `1e16 + 1 == 1e16` is `True` — your running counter silently stops incrementing.
- **The 5-minute fix:**

  ```python
  np.log1p(1e-12)      # 1e-12, accurate; np.log(1+1e-12) loses digits
  np.expm1(-1e-10)     # ~ -1e-10, accurate; exp(x)-1 cancels
  1e16 + 1 == 1e16     # True  -> float64 gap exceeds 1 above 2^53
  # variance: use a stable formula, never E[x^2]-E[x]^2
  x = np.array([1e8, 1e8+1, 1e8+2])
  bad = (x**2).mean() - x.mean()**2      # can go negative
  good = x.var()                          # numpy uses a stable two-pass
  # log(1-p) for p=expit(z): use  -log1p(exp(z)) = -softplus, no cancellation
  ```
- **Self-test:** Why can `(x**2).mean() - x.mean()**2` return a negative variance? **Answer:** catastrophic cancellation — for large-mean data both terms are huge and nearly equal, so subtracting them loses all significant digits and round-off can flip the sign.

### FRICTION — Comparing floats (never `==`)

- **The reflex:** You never test float equality with `==`; you use `np.isclose`/`allclose` with tolerances, and you know `0.1 + 0.2 != 0.3`.
- **The wall:** A convergence loop `while loss != prev_loss` never terminates (or terminates by luck); a test `assert result == 0.3` fails mysteriously; `np.arange(0, 1, 0.1)` has 10 or 11 elements depending on round-off and your indexing goes out of bounds.
- **The 5-minute fix:**

  ```python
  0.1 + 0.2 == 0.3                # False !
  np.isclose(0.1 + 0.2, 0.3)      # True
  np.allclose(A @ x, b, atol=1e-8)         # for vectors/matrices
  # convergence: compare relative change, not equality
  while abs(loss - prev) > 1e-8 * (1 + abs(prev)): ...
  # build float ranges with linspace (count is exact), not arange
  np.linspace(0, 1, 11)
  ```
- **Self-test:** How many elements does `np.arange(0, 0.3, 0.1)` produce, and why is that a trap? **Answer:** 3 here but it's fragile — the endpoint inclusion depends on float round-off of `0.3`; use `linspace` when you need an exact count.

### FRICTION — Fancy indexing vs boolean masks (and the copy/view trap)

- **The reflex:** You choose integer-array indexing vs boolean masking deliberately, know both return *copies* (not views), and know boolean-mask assignment writes in place.
- **The wall:** `X[X < 0] = 0` works (in-place clamp), but `X[idx][j] = 0` silently does nothing — `X[idx]` is a fresh copy, so the assignment lands on a temporary and `X` is unchanged. Your "fix negatives" step is a no-op and you chase the bug downstream. Or you index with a float array and get `IndexError`.
- **The 5-minute fix:**

  ```python
  X = rng.normal(size=(4, 4))
  mask = X < 0
  X[mask] = 0.0                 # in-place, works
  idx = np.array([0, 2])
  Y = X[idx]                    # COPY: modifying Y won't touch X
  X[idx, :] = 5.0               # single fancy-index assignment: writes to X
  # trap:  X[idx][:, 0] = 9     # no-op! chained indexing hits a temporary
  ```
- **Self-test:** Does `A[A > 0].sort()` sort the positive entries *inside* A? **Answer:** No — `A[A > 0]` is a boolean-mask *copy*; sorting it leaves A untouched.

### POLISH — Vectorize the reps (kill the Python loop)

- **The reflex:** When you see "repeat N times / for each of M items," you first ask "can this be one array op over an extra axis" before writing a `for` loop — for both speed and clarity.
- **The wall:** A 10⁶-iteration Monte Carlo `for` loop takes minutes and your 2-CPU box makes it worse; or a pairwise-distance double loop is O(n²) in Python and times out the module's 180 s budget.
- **The 5-minute fix:**

  ```python
  # loop version (slow):  s=0.0; for i in range(N): s += f(rng.random())
  # vectorized: draw all reps at once, apply f to the whole array
  u = rng.random(N)                       # one call, N draws
  est = f(u).mean()
  # pairwise squared distances without a loop, via broadcasting:
  D2 = ((A[:, None, :] - B[None, :, :])**2).sum(-1)   # (nA, nB)
  ```
  Note the memory/speed trade: broadcasting an (n,1,d) vs (1,m,d) grid is fast but O(n·m·d) memory — chunk if it blows up.
- **Self-test:** To average f over N Monte Carlo draws, how many RNG calls should you ideally make? **Answer:** one (`rng.random(N)` / a single vectorized draw), then apply f to the array and `.mean()` — not N scalar calls.

### POLISH — Read the dtype (int overflow, int division, silent upcasts)

- **The reflex:** You glance at `.dtype` when arithmetic looks off; you know integer arrays overflow silently and that mixing types can upcast or truncate.
- **The wall:** `np.arange(10)**10` overflows int64 to a negative number with no warning; `counts / counts.sum()` in old-int contexts truncates; an accidental `int32` from a C library overflows at 2·10⁹ in a large factorial or a cumulative count.
- **The 5-minute fix:**

  ```python
  (np.arange(1, 21).astype(np.int64)).prod()   # 20! overflows int64 -> garbage
  from scipy.special import gammaln
  gammaln(21)                                  # log(20!) safely
  a = np.array([2], dtype=np.int32); a**40      # silent overflow, no error
  # cast to float (or use log-gamma) before large multiplicative reductions
  ```
- **Self-test:** `np.array([2], dtype=np.int8) * 100` — result? **Answer:** overflow: 200 wraps around int8 (−128..127) to −56, with no error raised.

---

## Area IV — Simulation Discipline

Monte Carlo is the course's universal verification tool ("predict-then-verify," "simulate the null"). The discipline is: reproducible seeds, honest Monte Carlo error, verifying against known special cases, and using simulation as the arbiter when analysis is uncertain. Sloppiness here means results you can't reproduce or trust.

### GATE — Seeds and generator discipline (`np.random.Generator`, not global)

- **The reflex:** You create an explicit `rng = np.random.default_rng(seed)` and thread it through; you never touch the legacy global `np.random.seed`/`np.random.randn`, and you know how to spawn independent streams for parallel work.
- **The wall:** A "reproducible" result changes between runs because some library called the global RNG in between; two parallel workers seeded the same way produce *identical* "independent" chains (correlated Monte Carlo, understated error); or you can't reproduce a figure because the seed was implicit. On a 2-CPU box the parallel-correlation bug is easy to hit.
- **The 5-minute fix:**

  ```python
  rng = np.random.default_rng(20260717)     # explicit, modern
  a = rng.standard_normal(1000)
  # reproducible: same seed -> same draws
  assert (np.random.default_rng(0).random(3) == np.random.default_rng(0).random(3)).all()
  # INDEPENDENT parallel streams (do NOT reseed with seed+i):
  children = np.random.default_rng(20260717).spawn(4)   # 4 independent RNGs
  ```
  Rule: *one seed at the top, thread the Generator, `.spawn()` for parallelism.*
- **Self-test:** Two workers each do `np.random.default_rng(42)`. Are their draws independent? **Answer:** No — identical streams (perfectly correlated); use `default_rng(42).spawn(2)` (or `SeedSequence`) to get independent substreams.

### GATE — When in doubt, simulate the null

- **The reflex:** Before trusting an analytic p-value, standard error, or "this looks significant," you generate data under the null hypothesis many times and locate your observed statistic in that empirical distribution.
- **The wall:** You apply a t-test's formula to heavy-tailed or tiny-n data and quote p = 0.03 that the assumptions don't support; or you eyeball a "surprising" correlation with no sense of how often noise alone produces it. You have no calibrated sense of the null.
- **The 5-minute fix:**

  ```python
  # observed statistic
  obs = my_stat(data)
  # simulate the null B times (e.g. permute labels, or draw under H0)
  null = np.array([my_stat(simulate_under_H0(rng)) for _ in range(10000)])
  p_emp = (np.abs(null) >= np.abs(obs)).mean()   # two-sided empirical p
  # this needs NO distributional assumption and audits the analytic p
  ```
  Use it as the audit tool the brief calls for: "sampling-distribution calibration as a quality check."
- **Self-test:** You permute the treatment labels 10,000 times and 220 permutations give a mean-difference at least as extreme as observed. What's the (two-sided) permutation p-value? **Answer:** ≈ 220/10000 = 0.022 (often (220+1)/(10000+1) for the unbiased version).

### GATE — Verify against a known special case

- **The reflex:** Every new sampler, estimator, or derivation is *first* run on a case with a known closed-form answer, and you check it matches before trusting it on the real problem.
- **The wall:** You write a Gibbs sampler for a hierarchical model and its posterior mean is 0.6; is that right? You have no idea, because you never checked it reproduces the *conjugate* answer on a reduced version, or recovers a planted parameter from synthetic data. A transposed update or missing Jacobian passes unnoticed for weeks.
- **The 5-minute fix:**

  ```python
  # 1) recover a PLANTED truth from synthetic data:
  true_mu = 2.3
  y = rng.normal(true_mu, 1.0, size=5000)
  assert abs(sampler_posterior_mean(y) - true_mu) < 3*1.0/np.sqrt(5000)
  # 2) match a CLOSED FORM on a special case:
  #    Normal-Normal conjugate posterior mean is analytic -> compare to MCMC mean
  # 3) degenerate limits: prior -> flat should reproduce the MLE
  ```
  The mantra: *a new inference routine is guilty until it reproduces a case you can check by hand.*
- **Self-test:** You wrote a Metropolis sampler for a N(0,1) target. What's the cheapest correctness check? **Answer:** run it and confirm the sample mean ≈ 0, variance ≈ 1 (within Monte Carlo error), and the histogram matches `norm.pdf` — verifying against the known target.

### FRICTION — Report Monte Carlo error (an estimate without ± is unfinished)

- **The reflex:** Every Monte Carlo number comes with its standard error `s/√N` (adjusted for autocorrelation if the draws are a chain), and you size N to hit a target precision.
- **The wall:** You report "P ≈ 0.048" from 1000 draws as if it were exact, when its SE is ~0.007 — so it's indistinguishable from 0.05. You compare two estimates that differ by less than their Monte Carlo noise and declare a winner. For MCMC you quote SE = s/√N ignoring autocorrelation, understating error by 5–10×.
- **The 5-minute fix:**

  ```python
  x = f(rng.random(N))
  est, se = x.mean(), x.std(ddof=1)/np.sqrt(N)     # ± 2*se ≈ 95% band
  # to halve the error, quadruple N (error ∝ 1/sqrt(N))
  # MCMC: effective sample size < N; se = s/sqrt(ESS)  (use arviz.ess)
  ```
- **Self-test:** A Monte Carlo probability estimate is 0.5 from N = 400 draws. Roughly what is its standard error? **Answer:** √(0.5·0.5/400) = √(0.25/400) = 0.025 (so ±0.05 at 2 SE).

### FRICTION — Inverse-CDF / the reparameterization ("standard draw + transform") pattern

- **The reflex:** To sample a distribution you either push a uniform through its inverse-CDF or push a standard normal through a location-scale/Cholesky map — you don't hunt for a bespoke sampler when a transform of a standard draw will do.
- **The wall:** You need Exponential(λ) or a correlated MVN and don't have a canned routine; you write a rejection sampler with a bad envelope that accepts 2% of proposals and crawls. Or you want *reparameterized* gradients (VAE-style) but sample inside the graph in a way that blocks the gradient.
- **The 5-minute fix:**

  ```python
  # inverse-CDF: Exp(lam) from Uniform
  u = rng.random(10000); x = -np.log1p(-u)/lam         # note log1p(-u), stable
  # reparameterization: MVN via Cholesky (differentiable in mu, L)
  z = rng.standard_normal(d); sample = mu + L @ z
  # this "external randomness + deterministic transform" is the reparam trick
  ```
- **Self-test:** Given U ~ Uniform(0,1), how do you produce an Exponential(λ) draw, and why is `−log1p(−U)/λ` preferable to `−log(1−U)/λ`? **Answer:** invert the CDF F(x)=1−e^{−λx} ⇒ x = −log(1−U)/λ; `log1p(−U)` is more accurate when U is near 0 (avoids cancellation in `1−U`).

### POLISH — Common random numbers / variance reduction

- **The reflex:** When comparing two methods or estimating a *difference* by simulation, you reuse the *same* random draws across both arms so shared noise cancels.
- **The wall:** You compare estimator A vs B each on fresh random data; the between-method difference is swamped by sampling noise and you need 10× the reps to see a real gap that common random numbers would have exposed immediately.
- **The 5-minute fix:**

  ```python
  base = np.random.default_rng(0)
  s1, s2 = base.spawn(2)              # or: reuse ONE draw for both arms
  U = np.random.default_rng(1).random(N)   # same U for A and B
  diff = (methodA(U) - methodB(U)).mean()  # variance of diff is reduced
  # antithetic variates: pair U with 1-U to cancel linear trends
  ```
- **Self-test:** Why does using the same random draws for both arms shrink the variance of the *difference* of two Monte Carlo estimates? **Answer:** Var(A−B) = Var A + Var B − 2Cov(A,B); shared randomness makes Cov(A,B) large and positive, so the difference's variance drops.

---

## Boundary notes (straddle skills, developed elsewhere)

- **log-Jacobian ↔ density algebra:** the change-of-variables *mechanics* (Area I) are mine; the *density manipulations* they feed (normalizing constants, conjugacy) belong to the density-algebra agent.
- **logsumexp ↔ expectation tools:** I own the *numerical* stability trick; the *importance-sampling weight theory* it enables is the expectation-tools agent's.
- **Monte Carlo error ↔ asymptotics/CLT:** the s/√N *practice* is mine; the CLT *justification* and Berry–Esseen rates are the asymptotics agent's.
- **Standardization ↔ inequalities:** z-scoring as a *coding habit* is mine; Chebyshev/concentration *bounds* on standardized variables are the inequalities agent's.

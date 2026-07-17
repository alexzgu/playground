# P6. The linear algebra you actually use

> **Spine.** The working linear algebra of statistics is a handful of moves on a Gaussian: read a quadratic form as a squared distance, complete the square to a posterior, factor **once** with Cholesky instead of inverting, and condition via the Schur complement.
> **Which line?** Line 2 (conditioning) and line 3 (prediction) — every Gaussian posterior, predictive band, and kernel model in Part II runs on these reflexes.
> **Promise.** After this module you can see `inv()` in your own code and know why it should almost never be there; read `xᵀΣ⁻¹x`, a Schur complement, and a Cholesky log-det on sight; and compute one MVN conditional three ways that agree to machine precision.
> **Prereqs.** P1 (completing the square, scalar), P3 (precision-weighted mean). **Runtime.** ~6 s.
> **Sources.** Bridges to modules 05 (`gaussian_condition`), 14 (Bayesian regression), 20 (GPs), 21 (Kalman), 24 (partial correlation), 25 (effective parameters); C-B §3.6 (bivariate-normal conditional); expert-computational Area II.

Notation: $\Sigma$ a covariance (SPD), $\Lambda=\Sigma^{-1}$ its **precision**, $L$ the lower-triangular Cholesky factor ($\Sigma=LL^\top$). $N(\mu,\Sigma)$ is a Gaussian with that **covariance** (course convention: the second slot is variance/covariance, never precision). $\odot$ is elementwise.

---

## P6.1 Quadratic forms are squared distances

**Reflex.** You read $(x-\mu)^\top\Sigma^{-1}(x-\mu)$ on sight as a *squared Mahalanobis distance* — Euclidean distance after whitening — and you compute a whole batch of them with one `einsum`, never a Python loop.

**The wall.** Module 14 prints the predictive variance of Bayesian regression as one contraction,
> `epistemic = np.einsum("ij,jk,ik->i", Xg2, Sigma_n, Xg2)     # x*^T Sigma_n x* per row` — modules/14-bayesian-regression.md:128,

and the same batched form is the GP predictive variance at 20:77 and the logistic predictive at 15:337. If you don't read `ij,jk,ik->i` as "$x_i^\top\Sigma x_i$ for every row $i$," you fall back to a loop or a wrong `@` and get the wrong uncertainty band.

**The fix.** $\Sigma^{-1}$ is a *metric*; the quadratic form is $\lVert\text{whitened residual}\rVert^2$. Whiten with a triangular solve, and the einsum does the batch.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "P6-linear-algebra"
FIG = Path("figures") / SLUG
FIG.mkdir(parents=True, exist_ok=True)
SEED = 0
rng = np.random.default_rng(SEED)

plt.rcParams.update({
    "figure.figsize": (7, 4), "figure.dpi": 110, "savefig.dpi": 150,
    "savefig.bbox": "tight", "axes.grid": True, "grid.alpha": 0.3,
    "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 11,
})

def save(fig, name):
    out = FIG / f"{name}.png"
    fig.savefig(out)
    plt.close(fig)
    print(f"[fig] {out}")
```

```python
# --- P6.1 quadratic forms as squared distances ---
from scipy.linalg import solve_triangular, cho_factor, cho_solve

rng_q = np.random.default_rng(1)
A = rng_q.normal(size=(3, 3))
Sigma = A @ A.T + 0.3 * np.eye(3)              # a valid SPD covariance
mu = np.array([1.0, -1.0, 0.5])
L = np.linalg.cholesky(Sigma)                  # Sigma = L L^T -- ONE factorization

# single point: Mahalanobis distance == squared norm of the WHITENED residual
x = np.array([2.0, 0.0, 1.0]); d = x - mu
z = solve_triangular(L, d, lower=True)         # solve L z = d  (whiten)
maha_whiten = z @ z
maha_inv = d @ np.linalg.inv(Sigma) @ d        # the naive route, for comparison
print(f"P6.1 Mahalanobis: whiten={maha_whiten:.6f}  inv={maha_inv:.6f}  diff={abs(maha_whiten-maha_inv):.1e}")

# a BATCH of points, one einsum -- no Python loop
X = rng_q.normal(size=(6, 3)) + mu; D = X - mu
Prec = np.linalg.inv(Sigma)
batched = np.einsum("ij,jk,ik->i", D, Prec, D)         # x_i^T Sigma^{-1} x_i, per row i
loop = np.array([r @ Prec @ r for r in D])
print(f"P6.1 batched einsum vs loop, max|diff| = {np.max(np.abs(batched-loop)):.1e}")
```

The whitened route matches the inverse route to `2.2e-16` — but it never forms $\Sigma^{-1}$, which matters the moment $\Sigma$ is large or ill-conditioned. The einsum reproduces the per-row loop to `1.1e-16`: `ij,jk,ik->i` sums $\sum_{j,k}D_{ij}\,\Sigma^{-1}_{jk}\,D_{ik}$, exactly $x_i^\top\Sigma^{-1}x_i$, holding the row index $i$ free. That single line is how every module in Part II turns a covariance into a per-point uncertainty.

## P6.2 Cholesky is the workhorse — never invert

**Reflex.** The instant you see $\Sigma^{-1}$, `solve`, a log-det, or "draw from $N(\mu,\Sigma)$," you reach for **one** Cholesky factorization and read all three off it. Typing `np.linalg.inv` is a code smell: *when you see `inv()`, ask why.*

**The wall.** The GP log-marginal-likelihood in module 20 is three Cholesky outputs and nothing else:
> `L = np.linalg.cholesky(K)` ... `a = np.linalg.solve(L.T, np.linalg.solve(L, ytr))` (20:262), `complexity = -np.sum(np.log(np.diag(L)))` (20:264, the $-\tfrac12\log|K|$ Occam term); the exam's GP block is identical (EXAM:542–544). Invert instead and a 500×500 kernel matrix gives `det=0.0`, `log(det)=-inf`, and a `nan` likelihood you can't localize.

**The fix.** From $\Sigma=LL^\top$ you get solve, log-det, and sampling — one $O(n^3/3)$ factorization, reused three ways.

```python
# --- P6.2 solve, log-det, and sampling from ONE Cholesky factor ---
b = rng_q.normal(size=3)
sol_chol = cho_solve((L, True), b)                     # (1) Sigma^{-1} b  WITHOUT forming an inverse
sol_inv  = np.linalg.inv(Sigma) @ b
logdet_chol = 2.0 * np.log(np.diag(L)).sum()           # (2) log|Sigma| = 2 sum log diag(L)
_, logdet_slog = np.linalg.slogdet(Sigma)
draws = mu + (L @ rng_q.standard_normal((3, 40000))).T # (3) x = mu + L z ,  z ~ N(0, I)
print(f"P6.2 solve:  chol vs inv max|diff| = {np.max(np.abs(sol_chol-sol_inv)):.1e}")
print(f"P6.2 log-det: cholesky={logdet_chol:.6f}   slogdet={logdet_slog:.6f}")
print(f"P6.2 sample:  empirical cov vs Sigma, max|diff| = {np.max(np.abs(np.cov(draws.T)-Sigma)):.3f}")

# why NEVER det(): a 400x400 covariance with all eigenvalues 0.1 underflows
big = 0.1 * np.eye(400)
print(f"P6.2 det(0.1 * I_400) = {np.linalg.det(big):.3e}  ->  log of that is -inf; "
      f"but slogdet = {np.linalg.slogdet(big)[1]:.2f}")
```

All three checks pass: the solve matches the inverse to `2.2e-16`, the two log-dets agree at `0.270649`, and 40,000 draws of $\mu+Lz$ recover $\Sigma$ to `0.015` (Monte-Carlo noise). The last line is the punchline: $\det(0.1\,I_{400})=0.1^{400}$ underflows to `0.000e+00`, so `log(det)` is $-\infty$ — while `slogdet` (summing logs, like the Cholesky diagonal) reports the correct `-921.03`. **Heuristic** worth saying out loud: a determinant is a *volume*; volumes under/overflow exponentially in dimension, logs don't. Log-det via Cholesky diagonals or `slogdet`, never `log(det(...))`.

## P6.3 Completing the square, in matrix form

**Reflex.** Faced with $\exp(-\tfrac12 x^\top A x + b^\top x)$ you read off "Gaussian, **precision** $A$, mean $A^{-1}b$" — matching the quadratic term to the precision and the linear term to precision·mean. This is the engine behind every conjugate Gaussian update.

**The wall.** Module 14 derives the regression posterior in one sentence:
> "The log-posterior is a sum of two quadratics in $\beta$; completing the square ... gives $\Sigma_n=(\tfrac1{\sigma^2}X^\top X+\tfrac1{\tau^2}I)^{-1}$, $\mu_n=\Sigma_n\tfrac1{\sigma^2}X^\top y$" — modules/14-bayesian-regression.md:94.

The same move builds the NIW scale update (19:126), the Kalman joint (21:135), and the ridge/Bayes equivalence (EXAM:464). Miss it and $\Sigma_n$ is an unmotivated formula.

**The fix.** The identity, once, then verify that "posterior mean" and "ridge estimate" are the *same numbers* — the dictionary $\lambda=\sigma^2/\tau^2$ that modules 14 and 25 lean on.

$$-\tfrac12 x^\top A x + b^\top x = -\tfrac12(x-A^{-1}b)^\top A\,(x-A^{-1}b) + \tfrac12 b^\top A^{-1}b \;\Rightarrow\; N(\text{mean }A^{-1}b,\ \text{cov }A^{-1}).$$

```python
# --- P6.3 completing the square == the Bayesian regression posterior ---
rng_r = np.random.default_rng(3)
n, p = 60, 4
Xd = rng_r.normal(size=(n, p)); beta_true = np.array([1.0, -2.0, 0.5, 0.0])
sig2, tau2 = 0.5, 4.0
y = Xd @ beta_true + np.sqrt(sig2) * rng_r.normal(size=n)

A_prec = Xd.T @ Xd / sig2 + np.eye(p) / tau2           # posterior precision = data + prior (P3: precisions add)
b_lin  = Xd.T @ y / sig2                                # the linear term
post_mean = np.linalg.solve(A_prec, b_lin)             # A^{-1} b  via solve, not inv

lam = sig2 / tau2                                       # module 14/25 dictionary: ridge penalty
ridge = np.linalg.solve(Xd.T @ Xd + lam * np.eye(p), Xd.T @ y)
print(f"P6.3 posterior mean = {np.round(post_mean, 4)}")
print(f"P6.3 ridge(lambda=sig2/tau2) match, max|diff| = {np.max(np.abs(post_mean - ridge)):.1e}")
```

The posterior mean is `[ 1.0221 -1.8616  0.4591  0.068 ]` and the ridge estimate with $\lambda=\sigma^2/\tau^2$ matches it to `0.0e+00`. Ridge regression *is* a Gaussian-prior posterior mean; the penalty strength is a prior precision. That equivalence is the whole "regularization = a prior" thread of module 25, and it is nothing but this one completed square.

## P6.4 Schur complement = conditioning (the marquee, three ways)

**Reflex.** For a jointly Gaussian $(x_1,x_2)$, conditioning on $x_2$ gives mean $\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2)$ and covariance $\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ — the **Schur complement**. You compute $\Sigma_{22}^{-1}(\cdot)$ with `solve`, never `inv`, and you know the conditional covariance is *data-free* (doesn't depend on the observed value).

**The wall.** This IS module 05's `gaussian_condition`, cited as the engine of three later modules:
> `cond_cov = S11 - S12 @ np.linalg.solve(S22, S21)` — modules/05-conjugate-updating.md:420; reused verbatim as the regression posterior (14:58), the GP posterior (20:203–204), and the Kalman update (21:144).

**The marquee.** Compute one conditional three ways — textbook inverse, Schur-with-solve, and the course's `gaussian_condition` — and watch them agree.

> **Predict.** Three algebraically identical routes on a *well-conditioned* $3\times3$ $\Sigma$. Commit: will the conditional variance from the inverse route and the solve route differ by (a) ~$10^{-16}$, (b) ~$10^{-6}$, (c) visibly? *Reason (naive):* "same formula, so identical to machine precision" — true here, but hold that thought for the near-singular case below.

```python
# --- P6.4 the MVN conditional THREE WAYS ---
rng_g = np.random.default_rng(7)
Ag = rng_g.normal(size=(3, 3)); Sig = Ag @ Ag.T + 0.5 * np.eye(3)
mu3 = np.array([1.0, -2.0, 0.5]); x2 = np.array([0.7, -1.3])   # observe dims 1,2 ; infer dim 0
i1, i2 = [0], [1, 2]
S11 = Sig[np.ix_(i1, i1)]; S12 = Sig[np.ix_(i1, i2)]
S22 = Sig[np.ix_(i2, i2)]; S21 = Sig[np.ix_(i2, i1)]

# ROUTE 1 -- textbook formula with an EXPLICIT inverse
S22inv = np.linalg.inv(S22)
cm_inv = mu3[i1] + S12 @ S22inv @ (x2 - mu3[i2]);  cc_inv = S11 - S12 @ S22inv @ S21
# ROUTE 2 -- Schur complement with solve (no inverse ever formed)
cm_schur = mu3[i1] + S12 @ np.linalg.solve(S22, x2 - mu3[i2]); cc_schur = S11 - S12 @ np.linalg.solve(S22, S21)
# ROUTE 3 -- module 05's gaussian_condition, verbatim
def gaussian_condition(mu, Sigma, idx1, idx2, x2):
    S11 = Sigma[np.ix_(idx1, idx1)]; S12 = Sigma[np.ix_(idx1, idx2)]
    S22 = Sigma[np.ix_(idx2, idx2)]; S21 = Sigma[np.ix_(idx2, idx1)]
    return (mu[idx1] + S12 @ np.linalg.solve(S22, x2 - mu[idx2]),
            S11 - S12 @ np.linalg.solve(S22, S21))
cm_gc, cc_gc = gaussian_condition(mu3, Sig, i1, i2, x2)
print(f"P6.4 cond mean:  inv={cm_inv[0]:.6f}  schur={cm_schur[0]:.6f}  gc={cm_gc[0]:.6f}")
print(f"P6.4 cond var :  inv={cc_inv[0,0]:.6f}  schur={cc_schur[0,0]:.6f}  gc={cc_gc[0,0]:.6f}")
print(f"P6.4 three-route max|diff| = {max(abs(cm_inv[0]-cm_gc[0]), abs(cc_inv[0,0]-cc_gc[0,0])):.1e}")
```

All three routes give conditional mean `0.799936` and variance `0.539707`, agreeing to `0.0e+00`. On a well-conditioned $\Sigma$ the inverse route is fine — prediction (a) confirmed. So why the discipline? Timing and near-singular conditioning.

```python
# --- P6.4b why solve, not inv: backward stability (speed argued in prose, not timed) ---
# backward stability: near-singular S22 (condition number ~1e12), MODERATE true solution
U, _ = np.linalg.qr(rng_g.normal(size=(3, 3)))
S22_ill = U @ np.diag([1.0, 1e-6, 1e-12]) @ U.T
x_true = np.array([1.0, -2.0, 0.5]); b_ill = S22_ill @ x_true      # so ||x|| ~ O(1)
x_inv   = np.linalg.inv(S22_ill) @ b_ill
x_solve = np.linalg.solve(S22_ill, b_ill)
r_inv   = np.linalg.norm(S22_ill @ x_inv - b_ill)
r_solve = np.linalg.norm(S22_ill @ x_solve - b_ill)
print(f"P6.4b cond(S22)={np.linalg.cond(S22_ill):.1e}  residual: inv={r_inv:.1e}  solve={r_solve:.1e}")
```

On a large SPD system, solve is typically several-fold faster than invert-then-multiply because inverting does the same $O(n^3)$ elimination work and then pays for a full matrix–vector multiply on top; timings vary run to run, so this module keeps nothing time-derived in its output and rests the speed claim on that FLOP count. The stability payoff is sharper and exactly reproducible: on a matrix with condition number `1.0e+12`, invert-then-multiply leaves residual `5.0e-06` while `solve` leaves `6.9e-18` — about twelve orders of magnitude, because a triangular solve is backward-stable (it returns the exact answer to a slightly perturbed system) and `inv @ rhs` is not (the huge entries of the inverse amplify rounding). **Reconcile:** the naive "same formula, same answer" holds only when $\Sigma$ is well-conditioned. Near singularity — exactly where GP kernel matrices and ill-posed designs live — forming the inverse throws away accuracy the factorization would have kept. That is why the course's helper wraps `solve`.

## P6.5 Covariance ↔ precision: what the zeros mean

**Reflex.** You hold both views at once and know the asymmetry cold: **marginalizing is trivial in $\Sigma$** (slice the block), **conditioning is trivial in $\Lambda=\Sigma^{-1}$** (slice the block). A zero in $\Sigma$ means *marginal* independence; a zero in $\Lambda$ means *conditional* independence given all other variables (the Gaussian-graphical-model edge).

**The wall.** Module 21 reads structure straight off matrix entries — "the position marginal stays a scalar multiple of $I$ ($P[0,0]=P[1,1]$, $P[0,1]=0$)" (21:203) — and module 11's Gibbs sampler reads a conditional variance as a Schur complement of the covariance $\Sigma$ (the scalar $\Sigma_{22}-\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}$, equivalently $1/\Lambda_{22}$) at 11:372. Confuse the two parameterizations and you'll call variables independent from the wrong matrix.

**The fix.** Build a chain $0-1-2$ through a tridiagonal *precision* and watch the two matrices tell different stories.

```python
# --- P6.5 the zero is in a DIFFERENT matrix for marginal vs conditional independence ---
Lam = np.array([[2.0, -1.0,  0.0],
                [-1.0, 2.0, -1.0],
                [0.0, -1.0,  2.0]])          # tridiagonal precision = chain 0 - 1 - 2
Cov = np.linalg.inv(Lam)
print(f"P6.5 Sigma[0,2] = {Cov[0,2]:.4f}  (nonzero -> 0 and 2 are marginally DEPENDENT)")
print(f"P6.5 Lambda[0,2] = {Lam[0,2]:.1f}     (zero    -> 0 and 2 are conditionally indep given 1)")
```

$\Sigma_{02}=0.25\neq0$: marginally, 0 and 2 covary (both are tied to 1). But $\Lambda_{02}=0$: *given* the mediator 1, they are independent — the missing edge in the graph. Same Gaussian, opposite-looking matrices. This is why samplers that exploit conditional independence work in the precision, and why a near-zero $\Sigma$ off-diagonal is not a licence to declare independence.

## P6.6 Gram / kernel matrices via broadcasting

**Reflex.** You build an $n\times n$ pairwise matrix with an outer broadcast `a[:,None] - b[None,:]`, not a double loop, and you add a `1e-8·I` jitter before Cholesky as positive-definiteness insurance.

**The wall.** The exam's GP builds its kernel this way — `d = a[:,None] - b[None,:]; np.exp(-0.5*(d/ell)**2)` (EXAM:536) — and modules 17 and 20 recognize $\Phi\Phi^\top$ / $k(x,x')$ as an $n\times n$ Gram matrix (17:158, 20:46). The jitter appears at 20:159 (`K = kern(...) + jitter*np.eye(...)`): without it, a smooth kernel on close-together points is numerically indefinite and `cholesky` throws.

**The fix.**

```python
# --- P6.6 pairwise Gram matrix by broadcasting; jitter for a PD Cholesky ---
xa = np.linspace(0, 1, 40)
d = xa[:, None] - xa[None, :]                  # (40,40) pairwise differences, no loop
K = np.exp(-0.5 * (d / 0.3) ** 2)              # RBF Gram matrix
print(f"P6.6 K symmetric? {np.allclose(K, K.T)}   diag all 1? {np.allclose(np.diag(K), 1)}"
      f"   min eigenvalue = {np.linalg.eigvalsh(K).min():.2e}")
try:
    np.linalg.cholesky(K); raw = "succeeded"
except np.linalg.LinAlgError:
    raw = "FAILED (indefinite)"
np.linalg.cholesky(K + 1e-8 * np.eye(len(K)))  # jittered: always succeeds
print(f"P6.6 raw Cholesky {raw};  jittered Cholesky succeeded")
```

The RBF Gram matrix is symmetric with unit diagonal, but its smallest eigenvalue is `-3.42e-15` — negative by rounding, because 40 nearby points make the kernel numerically rank-deficient. Raw Cholesky `FAILED (indefinite)`; adding `1e-8·I` lifts every eigenvalue safely positive and it succeeds. **Heuristic:** jitter is not cheating — it is a tiny observation-noise / ridge term that says "no two function values are infinitely correlated," and it is standard in every GP library.

## P6.7 The hat matrix is a projection

**Reflex.** Least squares is *orthogonal projection* onto $\text{col}(X)$: $\hat y=Hy$, $H=X(X^\top X)^{-1}X^\top$, symmetric idempotent ($H^2=H$), with $\text{trace}(H)=$ number of parameters. Residualizing means applying the residual-maker $I-H$, and "effective degrees of freedom" of a regularized fit is $\text{trace}$ of *its* hat matrix.

**The wall.** Module 24 residualizes to get a partial correlation — `ra = a - C @ np.linalg.lstsq(C, a, rcond=None)[0]` (24:163), which is $(I-H)a$ — and module 25 reads effective parameters as a trace: `tr(Φ(ΦᵀΦ+λI)⁻¹Φᵀ)` (25:346), the reason a prior keeps model complexity below $p$.

**The fix.** Trace = params; ridge trace < params; residualize *both* variables on a confounder to wash out a spurious correlation.

```python
# --- P6.7 trace(H) = effective parameters; (I-H) = residual-maker ---
Xh = np.column_stack([np.ones(n), Xd[:, :3]])          # intercept + 3 predictors -> rank 4
Q, _ = np.linalg.qr(Xh); H = Q @ Q.T                   # projection onto col(X); never form (X^T X)^{-1}
print(f"P6.7 H idempotent? {np.allclose(H @ H, H)}   trace(H) = {np.trace(H):.4f}  (= #params)")
Hr = Xh @ np.linalg.solve(Xh.T @ Xh + 5.0 * np.eye(4), Xh.T)   # ridge hat, lambda=5
print(f"P6.7 ridge trace(H_lambda) = {np.trace(Hr):.4f}  (effective params < 4)")

# partial correlation: residualize BOTH on the common cause, then correlate (module 24)
rng_p = np.random.default_rng(11); z = rng_p.normal(size=300)
a = z + 0.4 * rng_p.normal(size=300); b = z + 0.4 * rng_p.normal(size=300)  # a,b share only cause z
C = np.column_stack([np.ones(300), z])
ra = a - C @ np.linalg.lstsq(C, a, rcond=None)[0]      # (I - H) a
rb = b - C @ np.linalg.lstsq(C, b, rcond=None)[0]      # (I - H) b
print(f"P6.7 corr(a,b) = {np.corrcoef(a, b)[0,1]:.3f}  ->  partial corr given z = {np.corrcoef(ra, rb)[0,1]:.3f}")
```

$\text{trace}(H)=4.0000$ — one per estimated coefficient, the model's degrees of freedom. The ridge hat has trace `3.7022`: the prior spends *fewer than 4* effective parameters, the exact mechanism by which regularization buys back complexity in module 25. And the confounded correlation `0.838` collapses to a partial correlation of `0.009` once both variables are pushed through $I-H$ on their shared cause $z$ — residualize twice, and the spurious association is gone. That is module 24's causal adjustment in three lines of projection.

## P6.8 Eigen-reasoning and lstsq vs the normal equations

**Reflex.** You picture a covariance as an ellipse: axes are eigenvectors, semi-axis lengths scale as $\sqrt{\text{eigenvalue}}$; PD $\Leftrightarrow$ all eigenvalues $>0$ $\Leftrightarrow$ Cholesky succeeds. For an underdetermined or rank-deficient system you reach for `lstsq`/`pinv` (the min-norm, stable solution), never the normal equations $X^\top X$.

**The wall.** The Kalman module draws its uncertainty ellipse from eigenvalues — `semi = [np.sqrt(np.linalg.eigvalsh(C)) for C in covs]` (21:180), orientation from the top eigenvector (21:185) — and modules 14/23 start from `np.linalg.lstsq(X, y, rcond=None)` (14:328, 23:57) precisely to avoid inverting a possibly-singular $X^\top X$.

**The fix.**

```python
# --- P6.8 eigen-ellipse geometry; lstsq stability vs the normal equations ---
covE = np.array([[2.0, 1.2], [1.2, 1.0]])
w, V = np.linalg.eigh(covE)                            # ascending eigenvalues, orthonormal eigenvectors
print(f"P6.8 eigenvalues = {np.round(w,4)}  all>0 -> PD={bool(np.all(w>0))};  "
      f"2-sigma semi-axes = {np.round(2*np.sqrt(w),3)}")

# an ILL-CONDITIONED tall design: the normal equations SQUARE the condition number
rng_u = np.random.default_rng(5)
nX, pX = 200, 6
Uq, _ = np.linalg.qr(rng_u.normal(size=(nX, nX)))
Vq, _ = np.linalg.qr(rng_u.normal(size=(pX, pX)))
Xu = Uq[:, :pX] @ np.diag(np.logspace(0, -8, pX)) @ Vq.T    # singular values 1 ... 1e-8
beta_true8 = rng_u.normal(size=pX); yu = Xu @ beta_true8
beta_ls, *_ = np.linalg.lstsq(Xu, yu, rcond=None)          # stable: factors X directly
beta_ne = np.linalg.solve(Xu.T @ Xu, Xu.T @ yu)            # normal equations: condition number gets squared
print(f"P6.8 cond(X)={np.linalg.cond(Xu):.0e}  cond(X^T X)={np.linalg.cond(Xu.T@Xu):.0e}")
print(f"P6.8 recovery error: lstsq={np.linalg.norm(beta_ls-beta_true8):.1e}  "
      f"normal-eqs={np.linalg.norm(beta_ne-beta_true8):.1e}")
```

```python
# --- figure: a covariance IS an ellipse ---
from matplotlib.patches import Ellipse
draws2 = rng_u.multivariate_normal([0, 0], covE, size=2000)
ang = np.degrees(np.arctan2(V[1, -1], V[0, -1]))          # angle of the TOP eigenvector
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(draws2[:, 0], draws2[:, 1], s=6, alpha=0.25, color="C0", label="2000 samples")
for k in (1, 2):
    ax.add_patch(Ellipse([0, 0], 2*k*np.sqrt(w[-1]), 2*k*np.sqrt(w[0]),
                          angle=ang, fill=False, edgecolor="C1", lw=2,
                          label=f"{k}$\\sigma$ ellipse" if k == 1 else None))
ax.set_aspect("equal"); ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
ax.set_title("Covariance ellipse: axes = eigenvectors, semi-axes = $\\sqrt{\\lambda}$")
ax.legend(loc="upper left")
save(fig, "cov-ellipse")
```

![Scatter of 2000 samples from a correlated bivariate Gaussian with 1-sigma and 2-sigma ellipses overlaid; the ellipse axes align with the eigenvectors and stretch as the square root of the eigenvalues.](figures/P6-linear-algebra/cov-ellipse.png)

The eigenvalues `[0.2 2.8]` are both positive (PD), and the ellipse's semi-axes `[0.894 3.347]` (at $2\sigma$) are $2\sqrt{\lambda}$ along the eigenvectors — the figure shows the cloud filling exactly that tilted ellipse. Meanwhile, for an ill-conditioned design with `cond(X)=1e+08`, the normal equations form $X^\top X$ whose condition number is `cond(X^T X)=1e+16` — the square. That squaring is fatal: `lstsq`, which factors $X$ directly, recovers the true coefficients to `1.6e-10`, while the normal-equations solve is off by `6.9e-01` — no correct digits left. **Heuristic:** never assemble $X^\top X$ when you can `lstsq`/`pinv` on $X$; the normal equations double the digits you lose to conditioning.

## Bridge — where these reflexes fire in the course

Every skill here is silent machinery in Part II. The MVN block formula (P6.4) is `gaussian_condition` (module 05), reused verbatim as the Bayesian-regression posterior (14), the GP posterior (20), and the Kalman update (21). Completing the square (P6.3) is the same posterior seen algebraically, and equals ridge with $\lambda=\sigma^2/\tau^2$ (25). Cholesky (P6.2) is the GP likelihood's entire spine (20, EXAM). Batched quadratic forms (P6.1) are every predictive-variance band (14, 15, 20). The hat-matrix trace (P6.7) is effective parameters (25) and the residual-maker is causal adjustment (24). Frequentist least squares, Bayesian conditioning, and kernel methods are the *same* linear algebra in different costumes.

## Pitfalls

- **`np.linalg.inv` in production.** Almost always a bug-in-waiting: slower, less stable, and it hides the factorization you actually wanted. Replace with `solve`, `cho_solve`, or `lstsq`. When you must invert (e.g. reporting a full covariance from a precision), do it once, deliberately, and comment why.
- **`log(det(Σ))`.** Underflows/overflows in high dimension; use `slogdet` or `2·Σ log diag(L)`. A `nan`/`-inf` log-likelihood is usually this.
- **Reading independence off the wrong matrix.** $\Sigma_{ij}=0$ is *marginal* independence; conditional independence is $\Lambda_{ij}=0$. They disagree the moment a mediator or confounder is present.
- **Cholesky on a "covariance" that isn't PD.** An empirical $\Sigma$ from too few samples (rank $\le n-1$) or a hacked-symmetric matrix has non-positive eigenvalues. Check `eigvalsh(...).min()`; add jitter or shrink before factoring.
- **Non-batched quadratic forms.** `X @ Σ @ X.T` gives the full $n\times n$ Gram matrix; you usually want only its diagonal, `einsum("ij,jk,ik->i", X, Σ, X)`. Taking `np.diag` of the full product wastes $O(n^2)$ memory.

## Exercises

**Exercise P6.1 — the einsum shape (ML connection).**
*Setup:* You have `X` of shape `(100, 5)` (100 test points, 5 features) and a posterior covariance `S` of shape `(5, 5)`. You want the epistemic predictive variance $x_i^\top S\,x_i$ at each of the 100 points — the module-14/15 band.
*Predict:* What is the shape of `np.einsum("ij,jk,ik->i", X, S, X)`? A colleague guesses `(100, 100)`; another guesses a scalar. Commit.
*Reason:* the intuition being tested — that repeating an index on the output (`i`) keeps it, while a repeated index only on the input (`j`, `k`) is summed out.
*Run:*
```python
rng_e = np.random.default_rng(21)
Xe = rng_e.normal(size=(100, 5)); Se = np.eye(5)      # S = I gives the checkable answer ||x||^2
v = np.einsum("ij,jk,ik->i", Xe, Se, Xe)
print("shape:", v.shape, " first 3:", np.round(v[:3], 3), " vs ||x||^2:", np.round((Xe[:3]**2).sum(1), 3))
```
<details><summary>Reconcile</summary>

Shape `(100,)` — one variance per point, not a matrix and not a scalar. The `i` index appears on the output, so it is *free* (kept); `j` and `k` appear only on inputs, so they are *contracted* (summed). With $S=I$ the quadratic form is just $\lVert x_i\rVert^2$, and the printout confirms `v[:3]` equals the row sums of squares. The `(100,100)` guess computes the full Gram matrix `X S Xᵀ` and then you'd take its diagonal — same numbers, $100\times$ the memory. The einsum diagonal is the idiom every predictive-band line in the course uses.
</details>

**Exercise P6.2 — inverse vs solve at the edge (surprising).**
*Setup:* A $3\times3$ SPD matrix with eigenvalues $\{1, 10^{-6}, 10^{-12}\}$ (condition number $10^{12}$), and a right-hand side $b$. You solve $Mx=b$ two ways: `inv(M) @ b` and `solve(M, b)`.
*Predict:* Both use the same $M$ and $b$. Will the **residuals** $\lVert Mx-b\rVert$ be (a) essentially equal (~$10^{-16}$), or (b) differ by many orders of magnitude?
*Reason:* the naive intuition — "same linear system, so any correct method gives the same accuracy."
*Run:*
```python
rng_x = np.random.default_rng(3)
U, _ = np.linalg.qr(rng_x.normal(size=(3, 3)))
M = U @ np.diag([1.0, 1e-6, 1e-12]) @ U.T
x_true = np.array([1.0, -2.0, 0.5]); bb = M @ x_true       # moderate solution: residual = backward error
xi = np.linalg.inv(M) @ bb; xs = np.linalg.solve(M, bb)
print("residual inv:", f"{np.linalg.norm(M@xi-bb):.1e}", " solve:", f"{np.linalg.norm(M@xs-bb):.1e}")
```
<details><summary>Reconcile</summary>

They differ by many orders of magnitude: `solve` leaves a residual of `1.1e-16`, the explicit inverse `1.7e-06`. A triangular/LU solve is *backward stable* — it returns the exact solution to a slightly perturbed system, so the residual stays near machine epsilon regardless of conditioning. Forming $M^{-1}$ and multiplying is not backward stable: the huge entries of $M^{-1}$ (order $10^{12}$) amplify rounding, and the product no longer reproduces $b$. The *forward* error is comparable for both (that's the conditioning of $M$ — the near-null direction is genuinely hard to pin down), but the *residual* — what you can actually check — exposes the inverse route. This is why `gaussian_condition` and every GP use `solve`.
</details>

**Exercise P6.3 — precision zero vs covariance zero.**
*Setup:* Three Gaussians tied in a chain $0-1-2$ via the tridiagonal precision from P6.5. You're asked "are variables 0 and 2 independent?"
*Predict:* Is the answer the same whether you look at $\Sigma$ or $\Lambda$? Which matrix has the zero?
*Reason:* the conflation being tested — treating "independent" as one property rather than *marginal* vs *conditional*.
*Run:*
```python
Lam = np.array([[2.,-1.,0.],[-1.,2.,-1.],[0.,-1.,2.]]); Cov = np.linalg.inv(Lam)
print("Sigma[0,2]:", round(Cov[0,2],4), " Lambda[0,2]:", Lam[0,2])
```
<details><summary>Reconcile</summary>

$\Sigma_{02}=0.25\neq0$ but $\Lambda_{02}=0$. The answer *depends on which independence you mean*: 0 and 2 are marginally dependent (both correlate with the mediator 1) yet conditionally independent given 1. The zero lives in the **precision**, not the covariance — that zero is exactly the missing edge $0\!-\!2$ in the Gaussian graphical model. Anyone who checks $\Sigma$ for independence gets the conditional-independence question backwards. Marginalize in $\Sigma$, condition in $\Lambda$.
</details>

## Takeaways

- **When you see `inv()`, ask why.** One Cholesky gives you `solve` ($\Sigma^{-1}b$), log-det ($2\sum\log\text{diag}\,L$), and sampling ($\mu+Lz$) — faster and stable where the inverse is neither.
- **A quadratic form is a squared distance.** $(x-\mu)^\top\Sigma^{-1}(x-\mu)=\lVert$whitened residual$\rVert^2$; a batch of them is one `einsum("ij,jk,ik->i", X, S, X)`.
- **Completing the square in matrix form** turns two quadratics into one Gaussian: precision $A$, mean $A^{-1}b$. This *is* the regression posterior, and it equals ridge with $\lambda=\sigma^2/\tau^2$.
- **Conditioning a Gaussian = the Schur complement**, computed with `solve`. It is one function (`gaussian_condition`) that powers regression, GPs, and the Kalman filter.
- **Two parameterizations, two meanings of zero:** marginalize by slicing $\Sigma$; condition by slicing $\Lambda$. $\Sigma_{ij}=0$ is marginal independence, $\Lambda_{ij}=0$ conditional.
- **Pairwise matrices by broadcasting** (`a[:,None]-b[None,:]`), with `1e-8·I` jitter before Cholesky; a covariance is an ellipse (axes = eigenvectors, semi-axes = $\sqrt\lambda$); PD $\Leftrightarrow$ Cholesky succeeds.
- **`trace(H)` = effective parameters**, and $(I-H)$ residualizes; for rank-deficient designs, `lstsq`/`pinv` (min-norm, stable), never the normal equations.

### Where the course uses this

| Skill | Where it silently fires (module:line) |
|---|---|
| Quadratic form / Mahalanobis / batched einsum | 05:296 · 08:107 · 14:128 · 15:337 · 18:315 · 20:77 |
| Completing the square (matrix) | 14:94 · 19:126 · 21:135 · 23:61 · EXAM:464 |
| Covariance ↔ precision / Schur / conditioning | 05:407 · 11:372 · 14:58 · 20:203 · 21:144 |
| Cholesky: solve / log-det / sample | 11:180 · 14:222 · 20:262 · 21:237 · EXAM:542 |
| Gram / kernel matrix by broadcasting | 17:158 · 20:46 · 20:150 · 23:362 · EXAM:536 |
| Projection / hat matrix / residual-maker | 18:314 · 24:163 · 25:346 |
| Eigen: ellipse / PD / jitter | 13:324 · 20:159 · 21:180 · 21:185 |
| lstsq / pinv vs normal equations | 14:328 · 23:57 · 23:354 · EXAM:393 |

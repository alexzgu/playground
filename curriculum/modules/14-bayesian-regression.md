# 14. Regression I: Bayesian Linear Models

> **Spine.** Regression is a prior over lines conditioned into a posterior over lines; ridge *is* the Gaussian prior ($\lambda = \sigma^2/\tau^2$, exactly), and cross-validating $\lambda$ is empirical Bayes — you were estimating your prior variance all along.
> **Which line?** Lines 2 and 3, in closed form. The posterior over coefficients is *one Gaussian conditioning step* (module 05's toolkit); the predictive interval is the marginalization that OLS's point prediction silently skips.
> **Promise.** After this module you can fit a Bayesian linear model by inspection, draw the posterior over lines, read off why the predictive interval *flares* off-support, prove ridge is a Gaussian-prior posterior mean and cross-validation is empirical Bayes, widen intervals correctly when $\sigma^2$ is unknown (Student-$t$), and make a fit shrug off outliers by marginalizing a latent variance.
> **Prereqs.** Modules 05 (the Gaussian conditioning toolkit, `student_t_predictive`, the precision-weighted mean), 06 (MAP = penalized MLE, the lasso mode-vs-mean honesty), 08 (the coverage-audit habit, empirical Bayes).
> **Runtime.** ~12 s.
> **Sources.** ISLP ch. 3, 6; booklet ch. 8; C-B by concept.

Ordinary least squares hands you *one* line. That is the tell that something has been thrown away: the data do not pin down a single line, they pin down a *distribution* over lines, tight where the data are dense and loose where they are absent. The four lines (module 00): **a model is a joint $p(\text{unknowns},\text{knowns})$; inference is conditioning; prediction is marginalization; a decision minimizes posterior expected loss.** For linear regression the unknowns are the coefficients $\beta$, conditioning gives a Gaussian posterior over $\beta$, and — this is the beat OLS drops — the *predictive* integrates that posterior back out, so its interval knows how far you have wandered from your evidence.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "14-bayesian-regression"          # this module's figure dir
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

## 14.1 A prior over lines, conditioned into a posterior over lines

The model is $y = X\beta + \varepsilon$, $\varepsilon \sim N(0, \sigma^2 I)$, with (for now) $\sigma^2$ known. A Gaussian prior $\beta \sim N(0, \tau^2 I)$ says *before seeing data, plausible coefficient vectors are small*. The joint $p(\beta, y)$ is Gaussian, so the posterior is one conditioning step. Completing the square (two quadratics in $\beta$, expand and collect — the same move as module 05's Normal-Normal) gives
$$\Sigma_n = \Big(\tfrac{1}{\sigma^2}X^\top X + \tfrac{1}{\tau^2}I\Big)^{-1},\qquad \mu_n = \Sigma_n\,\tfrac{1}{\sigma^2}X^\top y,\qquad \beta\mid y \sim N(\mu_n, \Sigma_n).$$
Posterior precision = prior precision + data precision $X^\top X/\sigma^2$; the posterior mean is a precision-weighted blend of the prior mean (0) and the data — **module 05's master shrinkage formula, now in $p$ dimensions.** But there is a second way to get here that makes the "posterior over lines" literal: stack $(\beta, y)$ into one Gaussian and apply module 05's `gaussian_condition` toolkit verbatim. That is not a coincidence to admire — it is the derivation.

```python
# One simple-regression dataset: intercept + slope, so lines are drawable.
n = 15
x = np.sort(rng.uniform(0.0, 4.0, size=n))          # covariate on [0, 4]; "data range" = 4
a_true, b_true, sigma = 1.0, 2.0, 1.0
y = a_true + b_true*x + rng.normal(0, sigma, size=n)
X = np.column_stack([np.ones(n), x])                # design: [1, x]
sigma2, tau2 = sigma**2, 10.0                       # known noise var; prior var per coef

# Route A: the precision-form posterior (Normal-Normal in p dimensions).
def blr_posterior(X, y, sigma2, tau2):
    p = X.shape[1]
    Sigma_n = np.linalg.inv(X.T @ X / sigma2 + np.eye(p) / tau2)
    mu_n = Sigma_n @ (X.T @ y / sigma2)
    return mu_n, Sigma_n
mu_n, Sigma_n = blr_posterior(X, y, sigma2, tau2)

# Route B: module 05's Gaussian toolkit on the joint (beta, y). Cov blocks:
#   Cov(beta)   = tau2 I,   Cov(beta,y) = tau2 X^T,   Cov(y) = tau2 X X^T + sigma2 I
def gaussian_condition(mu, Sigma, idx1, idx2, x2):   # verbatim from module 05
    S11 = Sigma[np.ix_(idx1, idx1)]; S12 = Sigma[np.ix_(idx1, idx2)]
    S22 = Sigma[np.ix_(idx2, idx2)]; S21 = Sigma[np.ix_(idx2, idx1)]
    cond_mean = mu[idx1] + S12 @ np.linalg.solve(S22, x2 - mu[idx2])
    cond_cov  = S11 - S12 @ np.linalg.solve(S22, S21)
    return cond_mean, cond_cov
p = X.shape[1]
mu_joint = np.zeros(p + n)                            # E[beta]=0, E[y]=X*0=0
Cov = np.zeros((p + n, p + n))
Cov[:p, :p] = tau2 * np.eye(p)
Cov[:p, p:] = tau2 * X.T
Cov[p:, :p] = tau2 * X
Cov[p:, p:] = tau2 * X @ X.T + sigma2 * np.eye(n)
mu_B, Sigma_B = gaussian_condition(mu_joint, Cov, list(range(p)), list(range(p, p+n)), y)

print(f"posterior mean  (precision form) = [{mu_n[0]:.4f}, {mu_n[1]:.4f}]")
print(f"posterior mean  (05 toolkit)     = [{mu_B[0]:.4f}, {mu_B[1]:.4f}]")
print(f"max|diff| mean {np.max(np.abs(mu_n-mu_B)):.1e}  cov {np.max(np.abs(Sigma_n-Sigma_B)):.1e}  (machine precision)")
print(f"posterior sd of (intercept, slope) = [{np.sqrt(Sigma_n[0,0]):.4f}, {np.sqrt(Sigma_n[1,1]):.4f}]")
```

The two routes agree to machine precision — Bayesian linear regression *is* the module 05 conditioning formula with $\Sigma$ built from the design. The posterior mean is `0.9677` (intercept) and `2.0084` (slope), close to the truth $(1, 2)$, with posterior standard deviations `0.4685` and `0.1860`. Now make "posterior over lines" visual: draw 30 coefficient vectors from $N(\mu_n, \Sigma_n)$ and plot each as a line.

```python
draws = rng.multivariate_normal(mu_n, Sigma_n, size=30)
xg = np.linspace(0, 4, 100)
fig, ax = plt.subplots()
for a, b in draws:
    ax.plot(xg, a + b*xg, color="C0", alpha=0.20, lw=1)
ax.plot(xg, mu_n[0] + mu_n[1]*xg, color="C1", lw=2.5, label="posterior mean line")
ax.plot(x, y, "ko", ms=5, label="data")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_title("The posterior is a distribution over lines — tight where the data live")
ax.legend()
save(fig, "posterior-over-lines")
```

![Thirty faint blue lines fanning through fifteen data points, tightest in the middle of the data and splaying apart toward the edges, with the orange posterior-mean line down the middle.](figures/14-bayesian-regression/posterior-over-lines.png)

The lines pinch together where the data are dense and splay apart at the edges. That splay is the whole point of the next section: extend it past the data and it becomes a trumpet.

## 14.2 The trumpet: predictive intervals flare off-support  [THE TRUMPET]

Prediction at a new input $x_*$ is line 3 — marginalize the posterior:
$$\tilde y_* = x_*^\top\beta + \varepsilon,\qquad \mathrm{Var}[\tilde y_*\mid y] = \underbrace{x_*^\top \Sigma_n\, x_*}_{\text{epistemic}} \;+\; \underbrace{\sigma^2}_{\text{aleatoric}}.$$
The aleatoric term is the irreducible noise floor — constant everywhere. The epistemic term is a *quadratic form in $x_*$*: near the data it is small, but $\Sigma_n$ has curvature, and as $x_*$ moves away from where the data pinned $\beta$ down, $x_*^\top\Sigma_n x_*$ grows without bound. OLS's point prediction $x_*^\top\hat\beta$ reports none of this — it is a bare line, mute about its own confidence.

**Predict.** The data live on $x\in[0,4]$. Before running, *sketch the half-width of your 95% predictive interval at $x_*=12$ — three times the data range.* Naive linear-model intuition extrapolates the line and carries a roughly constant-width error band along with it. Commit: is the interval half-width at $x_*=12$ about the same as at the center ($x=2$), maybe $2\times$, or far more?

**Reason.** The naive picture treats prediction error as the noise $\sigma$ that you can see scattered around the data — a constant band. That is the aleatoric term *only*; it forgets that off-support you no longer know *which line*.

```python
xg2 = np.linspace(0, 13, 200)
Xg2 = np.column_stack([np.ones_like(xg2), xg2])
pred_mean = Xg2 @ mu_n
epistemic = np.einsum("ij,jk,ik->i", Xg2, Sigma_n, Xg2)     # x*^T Sigma_n x* per row
pred_var = epistemic + sigma2
pred_sd = np.sqrt(pred_var)

def decomp(xv):
    xs = np.array([1.0, xv])
    epi = xs @ Sigma_n @ xs
    return epi, sigma2
for xv in (2.0, 12.0):
    epi, ale = decomp(xv)
    print(f"x*={xv:4.0f}: epistemic var = {epi:7.3f}   aleatoric var = {ale:.3f}   "
          f"predictive sd = {np.sqrt(epi+ale):6.3f}   95% half-width = {1.96*np.sqrt(epi+ale):6.3f}")

from sklearn.linear_model import LinearRegression
ols = LinearRegression().fit(x[:, None], y)                 # the "mute" point predictor

fig, ax = plt.subplots()
ax.fill_between(xg2, pred_mean - 1.96*pred_sd, pred_mean + 1.96*pred_sd,
                color="C0", alpha=0.20, label="95% posterior predictive")
ax.plot(xg2, pred_mean, color="C1", lw=2, label="predictive mean")
ax.plot(xg2, ols.predict(xg2[:, None]), color="C3", ls="--", lw=1.5,
        label="OLS point prediction (no width)")
ax.plot(x, y, "ko", ms=5, label="data")
ax.axvspan(0, 4, color="k", alpha=0.05); ax.text(1.5, ax.get_ylim()[1]*0.92, "data support", fontsize=9)
ax.axvline(12, color="C7", ls=":", lw=1); ax.text(10.3, 3, "x = 3× range", fontsize=9)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_title("The trumpet: the predictive interval flares where the data ran out")
ax.legend(loc="upper left", fontsize=9)
save(fig, "trumpet")
```

![A regression fit whose 95% band is a narrow tube through the data on x in 0 to 4 and then flares open like a trumpet bell out to x=12, while the dashed OLS line marches out with no band at all.](figures/14-bayesian-regression/trumpet.png)

**Reconcile.** At the data center $x=2$ the epistemic variance is `0.067` and the predictive half-width is `2.024` — essentially the noise floor $\sigma=1$. At $x_*=12$ the epistemic variance is `3.455`, three and a half times the aleatoric floor, and the half-width balloons to `4.137` — roughly double the center. The naive constant-band guess was wrong because prediction error is *not* just the scatter you see around the data; off-support the dominant term is not knowing which line, and that term grows quadratically as you extrapolate. OLS's dashed line sails out to $x=12$ reporting nothing. **The trumpet is the model telling you where it is guessing** — the visual signature of honest extrapolation, and the exact continuous analog of module 05's predictive-vs-plug-in widening (2-of-2 conversions, the language model's zero): the plug-in is most overconfident precisely where you have least evidence.

## 14.3 Ridge *is* the Gaussian prior: $\lambda = \sigma^2/\tau^2$, exactly

Module 00 opened the whole course by showing `Ridge(alpha=10)` equals a posterior mean at machine precision (`max|diff| = 4.5e-15`); module 06 named it MAP = penalized MLE. Here is the general identity and the general table. Ridge minimizes $\|y - X\beta\|^2 + \alpha\|\beta\|^2$, solved by $\hat\beta_\lambda = (X^\top X + \alpha I)^{-1}X^\top y$. The posterior mean from §14.1 is $\mu_n = (X^\top X/\sigma^2 + I/\tau^2)^{-1}X^\top y/\sigma^2 = (X^\top X + (\sigma^2/\tau^2)I)^{-1}X^\top y$. These are the *same vector* when
$$\boxed{\ \alpha = \sigma^2/\tau^2\ }$$
— and notice $\sigma^2$ cancels out of the coefficient, so the match holds for *any* noise scale. **The ridge penalty is a prior precision.** A strong penalty (large $\alpha$) is a tight prior (small $\tau^2$): "I believe the coefficients are small." Verify across two decades of $\alpha$:

```python
from sklearn.linear_model import Ridge
rng_r = np.random.default_rng(3)
n_r, p_r = 40, 10
Xr = rng_r.normal(size=(n_r, p_r))
Xr -= Xr.mean(0)                                    # center so no-intercept ridge is fair
beta_r = rng_r.normal(size=p_r)
yr = Xr @ beta_r + rng_r.normal(0, 1.0, n_r)

print(f"{'alpha':>8} {'tau2 = sigma2/alpha':>20} {'max|ridge - posterior mean|':>30}")
sigma2_r = 1.0
for alpha in (0.1, 1.0, 10.0, 100.0):
    tau2_r = sigma2_r / alpha
    mu_ridge_bayes, _ = blr_posterior(Xr, yr, sigma2_r, tau2_r)
    coef_sklearn = Ridge(alpha=alpha, fit_intercept=False).fit(Xr, yr).coef_
    print(f"{alpha:>8.1f} {tau2_r:>20.4f} {np.max(np.abs(coef_sklearn - mu_ridge_bayes)):>30.1e}")
```

Across $\alpha\in\{0.1,1,10,100\}$ the ridge coefficients equal the Gaussian-prior posterior mean to machine precision — worst case `8.9e-16`, the same phenomenon module 00 measured at its opener (max|diff| 4.5e-15). This is not an analogy — every ridge regression you have ever run *was* a Bayesian posterior mean under $\beta\sim N(0,\sigma^2/\alpha\cdot I)$, whether you called it that or not. Which raises the question module 06 flagged and 00 deferred: where does $\alpha$ come from?

## 14.4 Cross-validating $\lambda$ is empirical Bayes

The practitioner picks $\alpha$ by cross-validation: try a grid, keep the value with the smallest held-out error. The Bayesian picks $\tau^2$ by **empirical Bayes** (module 08): maximize the *marginal likelihood* — the evidence — $p(y\mid\tau^2) = N(y\mid 0,\ \tau^2 XX^\top + \sigma^2 I)$, integrating $\beta$ out entirely. These sound like different cultures. They are the same number.

**Predict.** For several datasets from the same generator, we compute $\alpha_{\text{CV}}$ (RidgeCV's choice) and $\alpha_{\text{EB}} = \sigma^2/\hat\tau^2_{\text{EB}}$ (the evidence-maximizer). Will they track each other across replicates — nearly equal every time — or wander independently because "minimize prediction error" and "maximize evidence" are different objectives?

**Reason.** The intuition that says they diverge treats CV as a pure predictive-accuracy tool with no model of where the data came from. But held-out error *is* an estimate of predictive density, and the evidence *is* the leave-none-out predictive density — same target, seen twice.

```python
from sklearn.linear_model import RidgeCV
from scipy.optimize import minimize_scalar

def eb_alpha(X, y, sigma2):
    """Empirical-Bayes alpha = sigma2 / tau2_hat, tau2 maximizing the evidence."""
    n = len(y)
    def neg_log_evidence(log_tau2):
        M = np.exp(log_tau2) * (X @ X.T) + sigma2 * np.eye(n)
        L = np.linalg.cholesky(M)
        alpha_solve = np.linalg.solve(L.T, np.linalg.solve(L, y))
        logdet = 2*np.sum(np.log(np.diag(L)))
        return 0.5*(y @ alpha_solve + logdet + n*np.log(2*np.pi))
    res = minimize_scalar(neg_log_evidence, bounds=(-8, 8), method="bounded")
    return sigma2 / np.exp(res.x)

rng_cv = np.random.default_rng(7)
n_cv, p_cv, sig2 = 50, 8, 1.0
tau2_true = 0.5
grid = np.logspace(-2, 3, 300)                              # fine grid: avoid CV quantization
print(f"true alpha = sigma2/tau2_true = {sig2/tau2_true:.3f}")
print(f"{'rep':>3} {'alpha_CV':>10} {'alpha_EB':>10}")
aCV, aEB = [], []
for rep in range(10):
    beta = rng_cv.normal(0, np.sqrt(tau2_true), size=p_cv)      # coefs ~ the prior
    Xc = rng_cv.normal(size=(n_cv, p_cv)); Xc -= Xc.mean(0)
    yc = Xc @ beta + rng_cv.normal(0, np.sqrt(sig2), n_cv)
    a_cv = RidgeCV(alphas=grid, fit_intercept=False).fit(Xc, yc).alpha_
    a_eb = eb_alpha(Xc, yc, sig2)
    aCV.append(a_cv); aEB.append(a_eb)
    print(f"{rep:>3} {a_cv:>10.3f} {a_eb:>10.3f}")
aCV, aEB = np.array(aCV), np.array(aEB)
print(f"correlation(alpha_CV, alpha_EB) across replicates = {np.corrcoef(aCV, aEB)[0,1]:.3f}")

fig, ax = plt.subplots()
lim = [min(aCV.min(), aEB.min())*0.7, max(aCV.max(), aEB.max())*1.3]
ax.plot(lim, lim, "k--", lw=1, label="y = x")
ax.scatter(aEB, aCV, color="C1", s=60, zorder=3)
ax.axvline(sig2/tau2_true, color="C7", ls=":", lw=1, label="true alpha")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel(r"empirical-Bayes $\alpha = \sigma^2/\hat\tau^2$")
ax.set_ylabel(r"cross-validated $\alpha$")
ax.set_title("Cross-validation and empirical Bayes pick the same regularizer")
ax.legend()
save(fig, "cv-equals-eb")
```

![A log-log scatter of cross-validated alpha against empirical-Bayes alpha, eight points hugging the dashed y=x diagonal near the true alpha = 2.](figures/14-bayesian-regression/cv-equals-eb.png)

The two columns march together: correlation `0.795` across replicates, both clustered around the true $\alpha = \sigma^2/\tau^2_{\text{true}} = $ `2.000`. Tuning the ridge penalty by cross-validation and estimating the prior variance by maximizing the evidence are the *same act* viewed from two cultures — **you were estimating your prior variance all along.** The mild scatter off the diagonal is the honest EB caveat (module 08): both are point estimates of a hyperparameter, and at small $n$ they disagree by sampling noise; the full-Bayes fix is to put a prior on $\tau^2$ and integrate it too (module 16's hierarchical treatment). This is the module's judgment-compression peak: two of the most-used knobs in applied ML and Bayesian statistics are one knob.

## 14.5 Unknown $\sigma^2$: the predictive becomes Student-$t$

Fixing $\sigma^2$ was a convenience. When the noise scale is unknown — which is always — put a conjugate Normal-Inverse-Gamma prior on $(\beta, \sigma^2)$: $\beta\mid\sigma^2\sim N(m_0, \sigma^2 V_0)$, $\sigma^2\sim\mathrm{IG}(a_0, b_0)$. This is module 05's NIG, now with a design matrix. The posterior is NIG$(m_n, V_n, a_n, b_n)$ with
$$V_n = (V_0^{-1} + X^\top X)^{-1},\quad m_n = V_n(V_0^{-1}m_0 + X^\top y),\quad a_n = a_0 + \tfrac n2,\quad b_n = b_0 + \tfrac12\big(m_0^\top V_0^{-1}m_0 + y^\top y - m_n^\top V_n^{-1}m_n\big).$$
Integrating $\sigma^2$ out of the predictive turns the Gaussian into a **Student-$t$** — exactly module 05's `student_t_predictive`, with the scalar case $X\equiv 1$ recovered as a check. At input $x_*$:
$$\tilde y_*\mid y \sim t_{\,\nu}\Big(\text{loc}=x_*^\top m_n,\ \ \text{scale}^2 = \tfrac{b_n}{a_n}\big(1 + x_*^\top V_n x_*\big)\Big),\qquad \nu = 2a_n.$$
Read the scale$^2$: the `1` is aleatoric, the $x_*^\top V_n x_*$ is epistemic — the *same decomposition as the trumpet*, now riding on heavier $t$-tails because you are also unsure of the noise floor. The scale$^2$ formula reduces to module 05's $b_n(\kappa_n+1)/(a_n\kappa_n)$ exactly when $X$ is the intercept-only design (then $x_*^\top V_n x_* = 1/\kappa_n$).

```python
def nig_regression(X, y, m0, V0, a0, b0):
    V0inv = np.linalg.inv(V0)
    Vn = np.linalg.inv(V0inv + X.T @ X)
    mn = Vn @ (V0inv @ m0 + X.T @ y)
    an = a0 + len(y)/2
    bn = b0 + 0.5*(m0 @ V0inv @ m0 + y @ y - mn @ np.linalg.inv(Vn) @ mn)
    return mn, Vn, an, bn

def t_predict(xs, mn, Vn, an, bn):
    df = 2*an
    loc = xs @ mn
    scale = np.sqrt((bn/an) * (1 + xs @ Vn @ xs))
    return df, loc, scale

# Reuse the §14.1 line data; weak NIG prior. Compare t vs known-sigma Gaussian intervals.
m0 = np.zeros(2); V0 = 10.0*np.eye(2); a0, b0 = 1.0, 1.0
mn, Vn, an, bn = nig_regression(X, y, m0, V0, a0, b0)
print(f"posterior: a_n = {an:.1f}  ->  predictive df = {2*an:.0f}   E[sigma^2|y] = b_n/(a_n-1) = {bn/(an-1):.4f}")
# Same scale, different tails: isolate what "unknown sigma^2" costs -> the t multiplier.
for xv in (2.0, 12.0):
    xs = np.array([1.0, xv])
    df, loc, scale = t_predict(xs, mn, Vn, an, bn)
    hw_t = stats.t(df).ppf(0.975) * scale                    # Student-t half-width
    hw_g = stats.norm().ppf(0.975) * scale                   # Gaussian tails, SAME scale
    print(f"x*={xv:4.0f}: scale = {scale:.3f}   t half-width = {hw_t:.3f}   "
          f"Gaussian half-width = {hw_g:.3f}   t/Gaussian = {hw_t/hw_g:.3f}")
print(f"tail factor: t(df={2*an:.0f}) 97.5% quantile = {stats.t(2*an).ppf(0.975):.4f} vs Normal 1.9600; "
      f"at df=5 (small n) it is {stats.t(5).ppf(0.975):.4f}")
```

With $n=15$ the predictive has $\nu = 2a_n = $ `17` degrees of freedom, and the posterior-mean noise variance is $b_n/(a_n-1) = $ `0.6413`. Holding the scale fixed, the Student-$t$ interval is wider than a Gaussian at every $x_*$ by the *same* factor `1.076` — the ratio of the $t_{17}$ 97.5% quantile (`2.1098`) to the Normal's `1.9600` — because this widening is purely a tail effect, independent of $x_*$. The extra width is the tax for not knowing the noise floor, largest at small $n$ (small $\nu$, heaviest tails) and vanishing as $\nu\to\infty$: at $\nu=5$ the multiplier is `2.5706`/1.9600, a 31% inflation where the $t$ prices extreme observations dramatically higher than the Gaussian would (module 05's small-$n$ warning, now attached to every prediction).

## 14.6 Robust regression: a $t$-likelihood is a Gamma scale-mixture

A single gross outlier can swing an OLS line off its hinges, because the Gaussian likelihood's $-\tfrac{1}{2\sigma^2}(y_i - x_i^\top\beta)^2$ penalty grows *quadratically* — a point ten standard deviations out contributes a hundred times the leverage of a typical one, and the fit contorts to appease it. The Bayesian fix is not an outlier-detection heuristic bolted on afterward; it is a *different generative story for the noise*. Give each observation a Student-$t$ likelihood, and use the identity that a $t$ is a **Gamma scale-mixture of Normals**:
$$y_i\mid\beta,\lambda_i \sim N\big(x_i^\top\beta,\ \sigma^2/\lambda_i\big),\qquad \lambda_i \sim \mathrm{Gamma}(\nu/2,\ \nu/2)\ \ \Longrightarrow\ \ y_i\mid\beta \sim t_\nu\big(x_i^\top\beta,\ \sigma^2\big),$$
because $\int N(y\mid m,\sigma^2/\lambda)\,\mathrm{Gamma}(\lambda\mid\nu/2,\nu/2)\,d\lambda = t_\nu(y\mid m,\sigma^2)$ (integrate out $\lambda$; the Gamma is conjugate to the Normal's precision). Each point carries its own latent precision $\lambda_i$: a point that fits well keeps $\lambda_i\approx 1$, an outlier is *explained* by a small $\lambda_i$ (a locally inflated variance) rather than by dragging $\beta$. Inference marginalizes $\lambda_i$, and the posterior weight $\mathbb E[\lambda_i\mid\text{data}]$ down-weights outliers automatically. EM makes this concrete — the E-step *is* that expected precision, the M-step is weighted least squares.

**Predict.** We take 30 clean points on a slope-$0.5$ line and yank three of them (10% of the data) far off. Before running, commit: by what fraction does the *ordinary* least-squares slope move — about 10%, proportional to the contamination — and does the $t$-fit resist?

**Reason.** The naive "perturbation is proportional to the share of bad data" reasons linearly in the count; it ignores *leverage* — that a far-off point contributes its squared residual, so its pull is out of all proportion to its number.

```python
def t_regression_em(X, y, nu=4.0, iters=60):
    """EM for Student-t linear regression (Gamma scale-mixture). Returns beta, sigma2, weights."""
    beta = np.linalg.lstsq(X, y, rcond=None)[0]         # start from OLS
    sigma2 = np.mean((y - X @ beta)**2)
    for _ in range(iters):
        r = y - X @ beta
        w = (nu + 1) / (nu + r**2 / sigma2)             # E-step: E[lambda_i | data]
        WX = X * w[:, None]
        beta = np.linalg.solve(WX.T @ X, WX.T @ y)       # M-step: weighted least squares
        sigma2 = np.mean(w * (y - X @ beta)**2)          # M-step: weighted noise variance
    return beta, sigma2, w

# Clean line, then hijack it with 3 outliers.
rng_o = np.random.default_rng(2)
n_o = 30
xo = np.sort(rng_o.uniform(0, 10, n_o))
yo = 1.0 + 0.5*xo + rng_o.normal(0, 0.7, n_o)
Xo = np.column_stack([np.ones(n_o), xo])
yo_out = yo.copy()
out_idx = [22, 25, 28]
yo_out[out_idx] += np.array([8.0, 9.0, 10.0])           # three high-x points yanked far up

b_ols_clean = np.linalg.lstsq(Xo, yo,     rcond=None)[0]
b_ols_out   = np.linalg.lstsq(Xo, yo_out, rcond=None)[0]
b_t_out, _, w_out = t_regression_em(Xo, yo_out, nu=4.0)
print(f"slope, clean data       (OLS) = {b_ols_clean[1]:.4f}   (truth 0.5)")
print(f"slope, 3 outliers added (OLS) = {b_ols_out[1]:.4f}   <- hijacked")
print(f"slope, 3 outliers added (t)   = {b_t_out[1]:.4f}    <- barely moved")
print(f"learned weights on the 3 outliers = {np.round(w_out[out_idx], 3)}  (vs ~1 elsewhere)")

fig, ax = plt.subplots()
ax.plot(np.delete(xo, out_idx), np.delete(yo_out, out_idx), "ko", ms=5, label="data")
ax.plot(xo[out_idx], yo_out[out_idx], "s", color="C3", ms=9, label="injected outliers")
gx = np.linspace(0, 10, 50)
ax.plot(gx, b_ols_out[0] + b_ols_out[1]*gx, color="C3", lw=2, label=f"OLS (Normal): slope {b_ols_out[1]:.2f}")
ax.plot(gx, b_t_out[0] + b_t_out[1]*gx, color="C0", lw=2, label=f"robust t: slope {b_t_out[1]:.2f}")
ax.plot(gx, b_ols_clean[0] + b_ols_clean[1]*gx, color="k", ls=":", lw=1.5, label="OLS on clean data")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_title("Three outliers hijack the Normal fit; the t-fit shrugs")
ax.legend(fontsize=9)
save(fig, "robust-t")
```

![Scatter with three red square outliers pulled far above a linear trend; the red OLS line tilts up toward them while the blue robust-t line stays down along the clean data, nearly on top of the dotted clean-data OLS line.](figures/14-bayesian-regression/robust-t.png)

**Reconcile.** On clean data OLS recovers slope `0.4942`. Add three outliers and the OLS slope jerks to `0.9109` — an 84% distortion from three points out of thirty, eight times the naive "10%" guess. The $t$-regression slope is `0.5187`, essentially unmoved and nearly identical to the clean-data fit. The mechanism is printed in the weights: the three outliers get $\mathbb E[\lambda_i]$ of `0.062`, `0.044`, and `0.043` — roughly a twentieth of the weight of the ordinary points — the model quietly decided those three came from a high-variance regime and stopped listening to them. **Robustness here is not a heuristic; it is marginalizing a latent variance.** "Down-weight outliers" is a *consequence* of a heavier-tailed generative story, derived, not a rule you tuned. (Fixing $\nu=4$ is a modelling choice; smaller $\nu$ = heavier tails = more aggressive down-weighting. You can also put a prior on $\nu$ and infer it.)

## 14.7 Basis expansion: bias–variance is prior strength

Linearity is in the *coefficients*, not the inputs. Replace $x$ by a feature map $\phi(x) = [1, x, x^2, \dots, x^d]$ (polynomials, or splines) and every formula above carries over with $X$ the matrix of features. This is how a "linear" model fits curves — and it reframes the bias–variance tradeoff as a *prior-strength* dial. With a Gaussian prior $\beta\sim N(0,\tau^2 I)$ on the coefficients, ridge penalty $\alpha=\sigma^2/\tau^2$ (§14.3):

- **Prior too strong** (tiny $\tau^2$, huge $\alpha$): coefficients crushed toward 0, the fit cannot bend to the signal — *underfitting*, high bias.
- **Prior too weak** (huge $\tau^2$, $\alpha\to 0$): coefficients unconstrained, the high-degree terms chase noise — *overfitting*, high variance.
- **Prior matched** to the true coefficient scale: the bias–variance sweet spot — which is exactly the $\alpha$ that §14.4's evidence maximization finds.

```python
rng_b = np.random.default_rng(5)
f_true = lambda t: np.sin(1.5*t)
nb = 25
xb = np.sort(rng_b.uniform(-3, 3, nb))
yb = f_true(xb) + rng_b.normal(0, 0.3, nb)
deg = 12
def poly_features(t, d):
    Phi = np.vander(t, d+1, increasing=True)
    return Phi
Phi = poly_features(xb, deg)
scales = np.abs(Phi).max(0); Phi_s = Phi / scales            # column-scale for conditioning
tg = np.linspace(-3.4, 3.4, 300)
Phig = poly_features(tg, deg) / scales

fig, ax = plt.subplots()
ax.plot(xb, yb, "ko", ms=4, label="data")
ax.plot(tg, f_true(tg), "k:", lw=1.5, label="truth  sin(1.5x)")
for tau2b, name, col in [(1e-3, "strong prior -> underfit", "C0"),
                         (1e0,  "matched prior -> good fit", "C1"),
                         (1e4,  "weak prior -> overfit",    "C3")]:
    mu_b, _ = blr_posterior(Phi_s, yb, 0.3**2, tau2b)
    ax.plot(tg, Phig @ mu_b, color=col, lw=2, label=name)
ax.set_ylim(-2.2, 2.2)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_title("Degree-12 fit: bias-variance is the strength of the coefficient prior")
ax.legend(fontsize=8, loc="lower center")
save(fig, "basis-prior-strength")
print("degree-12 polynomial fit under three prior strengths (tau2 = 1e-3, 1, 1e4)")
```

![A degree-12 polynomial fit to noisy sine data under three prior strengths: the strong-prior curve is nearly flat (underfit), the weak-prior curve wiggles wildly through every point and blows up at the edges (overfit), and the matched-prior curve tracks the true sine.](figures/14-bayesian-regression/basis-prior-strength.png)

Same 12 basis functions, same data, three priors — and the fit ranges from a near-flat underfit through a clean recovery of $\sin(1.5x)$ to a wild overfit that explodes past the data edges (the trumpet's warning, ignored). Model complexity was never really about the *number* of features; with a prior it is about *how much you let the coefficients move*. "How many terms?" becomes "how strong a prior?", a continuous knob the evidence sets for you — the seed of Gaussian processes (module 20: take $d\to\infty$) and of module 17's Occam factor.

## 14.8 Lasso and beyond

Swap the Gaussian prior for a Laplace prior and the MAP is the **lasso** — module 06 derived this and drew the honest line: the lasso *point estimate* is a posterior **mode**, and the $\ell_1$ corner parks it on exact zeros, but the Laplace-prior posterior **mean** is never sparse (module 06's worked cases: mode exactly 0 vs posterior means of 0.1432 and 0.3945). Sparsity is a fact about where the peak sits, not about the posterior. If you want genuine sparsity *with* honest uncertainty — most coefficients tightly at zero, a few free — you need a different prior shape: a global-local shrinkage prior like the **horseshoe**, which module 18 builds and fits at scale. No re-derivation here; the pointer is the content.

## Bridge — ISLP ch. 3/6, and the regularizers you already tune

ISLP teaches linear regression, then ridge and lasso as *penalties* chosen by cross-validation. This module says those are not three topics but one: the penalty is a prior (§14.3, $\alpha=\sigma^2/\tau^2$), cross-validation is empirical Bayes (§14.4), and the object OLS drops — the predictive interval — is the trumpet that tells you where the model is extrapolating (§14.2). Every regularized regression in the ISLP toolkit is a Bayesian posterior mean under some prior; choosing the regularizer is choosing (and then estimating) that prior. The deep-learning reader can read the same sentence with "weight decay" in place of "ridge": weight decay is a Gaussian prior on the weights, its strength a prior precision (module 25 cashes this out). The catch to keep honest, exactly as in module 07: a convenient prior (Gaussian, for the closed form) is not automatically a *defensible* one — the trumpet's off-support flare is only as trustworthy as the linearity assumption generating it.

## Pitfalls

- **Reporting OLS's point prediction off-support.** The bare line $x_*^\top\hat\beta$ is mute about epistemic variance, which *grows quadratically* as you leave the data (§14.2). Extrapolating a point prediction without the trumpet is claiming certainty exactly where you have least.
- **Forgetting $\sigma^2$ is unknown.** Known-$\sigma^2$ Gaussian intervals are too narrow; the honest predictive is Student-$t_{2a_n}$ (§14.5), heaviest-tailed at small $n$. Plugging in $\hat\sigma^2$ and using a Normal repeats module 05's under-coverage in continuous form.
- **Treating $\alpha$ as a free knob divorced from a model.** $\alpha$ *is* $\sigma^2/\tau^2$ — a statement about how large you believe coefficients to be (§14.3). Cross-validation and evidence maximization estimate the same quantity (§14.4); if they disagree wildly, your model or your grid is the problem.
- **Using OLS with outliers present.** The quadratic loss gives a single far point unbounded leverage (§14.6). A $t$-likelihood down-weights it by *marginalizing a latent precision* — reach for it before hand-deleting "bad" points, which is an undocumented, non-reproducible prior.
- **Calling the lasso "sparse Bayes."** The zeros are a property of the *mode*; the posterior mean is never sparse (§14.8, module 06). For sparsity with uncertainty use a horseshoe (module 18), not the lasso's point estimate.

## Exercises

**Exercise 14.1 — How fast does the trumpet flare?**  *(surprising)*
*Setup:* Using the §14.1 posterior (`Sigma_n`, `sigma2`), compare the 95% predictive half-width at the data center $x=2$ against three extrapolation distances: $x=6$, $x=12$, $x=24$ (1×, 3×, and 6× beyond the range's edge).
*Predict:* Doubling the extrapolation distance roughly — doubles the interval width? Quadruples it? Something else?
*Reason:* "Extrapolation error grows with distance" — but *how* is the question; the naive guess is linear growth.
*Run:*
```python
for xv in (2.0, 6.0, 12.0, 24.0):
    xs = np.array([1.0, xv])
    hw = 1.96*np.sqrt(xs @ Sigma_n @ xs + sigma2)
    print(f"x*={xv:5.0f}: 95% half-width = {hw:6.3f}")
```
<details><summary>Reconcile</summary>

Half-widths are about `2.024` (x=2), `2.473` (x=6), `4.137` (x=12), `8.236` (x=24). Once you are well off-support the epistemic term $x_*^\top\Sigma_n x_*$ dominates and grows *quadratically* in $x_*$, so its square root — the interval width — grows *linearly* in the distance, doubling as $x_*$ doubles (4.137 → 8.236). But near the data the noise floor $\sigma$ still contributes, so the growth is slower than linear there (2.024 → 2.473 is far from a doubling). The surprise for the naive "linear everywhere" guess cuts both ways: the width is *super*-linear leaving the data (variance quadratic) and *sub*-linear near it (floored by $\sigma$). The trumpet's bell is a parabola in variance, a cone in width.
</details>

**Exercise 14.2 — Weight decay is a prior.**  *(ML bridge)*
*Setup:* On the §14.3 ridge dataset (`Xr`, `yr`), a deep-learning colleague turns up "weight decay" from $\alpha=1$ to $\alpha=100$. In Bayesian terms that shrinks the prior variance $\tau^2=\sigma^2/\alpha$ by 100×.
*Predict:* The ratio of the fitted coefficient norm $\|\hat\beta\|$ at $\alpha=100$ versus $\alpha=1$ — about 1 (barely changes), about 0.5, or far smaller?
*Reason:* "A stronger penalty shrinks coefficients, but the data still anchor them" — the belief that the likelihood dominates.
*Run:*
```python
for alpha in (1.0, 100.0):
    coef = Ridge(alpha=alpha, fit_intercept=False).fit(Xr, yr).coef_
    print(f"alpha={alpha:6.1f}  ||beta|| = {np.linalg.norm(coef):.4f}")
n1  = np.linalg.norm(Ridge(alpha=1.0,   fit_intercept=False).fit(Xr, yr).coef_)
n100= np.linalg.norm(Ridge(alpha=100.0, fit_intercept=False).fit(Xr, yr).coef_)
print(f"ratio ||beta||_100 / ||beta||_1 = {n100/n1:.4f}")
```
<details><summary>Reconcile</summary>

The norm falls from `3.3016` at $\alpha=1$ to `0.6593` at $\alpha=100$, a ratio of `0.1997` — the coefficients shrink to about a fifth, far more than the "barely changes" intuition expects with only $n=40$ observations and $p=10$. A tight Gaussian prior ($\tau^2$ down 100×) really does pull hard when the data are not overwhelming. This *is* weight decay: the same shrinkage a neural-net optimizer applies every step, readable as a prior precision on the weights (module 25). The likelihood dominates only when $n\gg p$ and the prior is loose; regularization matters exactly when it isn't.
</details>

**Exercise 14.3 — When does the outlier win?**  *(surprising)*
*Setup:* Take the §14.6 clean data and inject a *single* outlier at the high-leverage end ($x\approx 10$), lifted by a growing amount $\Delta\in\{2, 8, 20\}$. Compare how far the OLS slope and the $t$-regression slope move from the clean-data slope `0.4942`.
*Predict:* As $\Delta\to 20$, does the $t$-slope also eventually get dragged (a big enough outlier beats any method), or does it stay put?
*Reason:* "Every estimator has a breakdown point; make the outlier extreme enough and it wins."
*Run:*
```python
xo1 = xo.copy(); j = np.argmax(xo)                       # highest-leverage point
for delta in (2.0, 8.0, 20.0):
    yj = yo.copy(); yj[j] += delta
    b_ols = np.linalg.lstsq(Xo, yj, rcond=None)[0][1]
    b_t   = t_regression_em(Xo, yj, nu=4.0)[0][1]
    print(f"delta={delta:5.1f}:  OLS slope = {b_ols:.4f}   t slope = {b_t:.4f}")
```
<details><summary>Reconcile</summary>

OLS slopes climb steadily with $\Delta$ — `0.5405`, `0.6792`, `0.9567` — because quadratic loss gives an unbounded point unbounded pull; a single outlier can drag the line anywhere. The $t$-slopes stay near the truth — `0.5328`, `0.5166`, `0.5110` — and, counter to the "big enough always wins" intuition, the $t$-fit gets *more* resistant as $\Delta$ grows, because a further-out point earns a *smaller* weight $\mathbb E[\lambda_i]=(\nu+1)/(\nu+r_i^2/\sigma^2)\to 0$. The heavy tail means the influence function is *redescending*: past some distance an outlier's leverage goes to zero rather than to infinity. That is the qualitative gap between a bounded and an unbounded loss — not a tuning difference, a different generative story.
</details>

**Exercise 14.4 — Does more data narrow the whole trumpet?**
*Setup:* Refit the §14.1 model with $n=15$ versus $n=120$ points drawn from the same DGP on $x\in[0,4]$. Compare the predictive half-width at the center ($x=2$) and far off-support ($x=12$).
*Predict:* Quadrupling-plus the data shrinks the center interval a lot. Does it shrink the *off-support* ($x=12$) interval by the same factor, more, or less?
*Reason:* "More data tightens the posterior everywhere, so both intervals shrink by roughly $\sqrt{n}$."
*Run:*
```python
for nn in (15, 120):
    rng_e = np.random.default_rng(0)
    xe = np.sort(rng_e.uniform(0, 4, nn))
    ye = 1.0 + 2.0*xe + rng_e.normal(0, 1.0, nn)
    Xe = np.column_stack([np.ones(nn), xe])
    _, Sig = blr_posterior(Xe, ye, 1.0, 10.0)
    hw2  = 1.96*np.sqrt(np.array([1,2.0])  @ Sig @ np.array([1,2.0])  + 1.0)
    hw12 = 1.96*np.sqrt(np.array([1,12.0]) @ Sig @ np.array([1,12.0]) + 1.0)
    print(f"n={nn:>3}: half-width at x=2 = {hw2:.3f}   at x=12 = {hw12:.3f}")
```
<details><summary>Reconcile</summary>

At the center the half-width barely improves — `2.024` → `1.968` — because on-support the interval is already floored by the *aleatoric* noise $\sigma$, which no amount of data removes. Off-support the epistemic term dominates and *that* shrinks with $n$: `4.137` → `2.433` at $x=12$. So more data narrows the trumpet's *bell* far more than its *throat* — the opposite of the uniform-$\sqrt n$ guess. Data buys you epistemic certainty (which line), never aleatoric certainty (the noise floor); the two terms of §14.2 respond to sample size completely differently. This is why collecting more data helps extrapolation and calibration far more than it helps the fit near the data's center of mass.
</details>

## Takeaways

- **Regression is a posterior over lines.** With $\beta\sim N(0,\tau^2 I)$ the posterior is $N(\mu_n,\Sigma_n)$ — one Gaussian conditioning step (module 05's toolkit, verified to machine precision), $\mu_n$ a precision-weighted blend of prior and data.
- **The trumpet.** The predictive variance is $x_*^\top\Sigma_n x_*$ (epistemic) $+\ \sigma^2$ (aleatoric); the epistemic term grows quadratically off-support, so the interval flares where the data ran out — exactly what OLS's point prediction hides.
- **Ridge is the Gaussian prior, exactly.** $\hat\beta_{\text{ridge}}(\alpha)$ equals the posterior mean under $\beta\sim N(0,\sigma^2/\alpha\cdot I)$ to machine precision, for every $\alpha$; the penalty is a prior precision, $\alpha=\sigma^2/\tau^2$.
- **Cross-validating $\lambda$ is empirical Bayes.** RidgeCV's $\alpha$ and the evidence-maximizing $\sigma^2/\hat\tau^2$ track each other (correlation `0.795`) — tuning the regularizer *is* estimating the prior variance.
- **Unknown $\sigma^2$ ⇒ Student-$t$ predictive.** The NIG posterior gives $\tilde y_*\sim t_{2a_n}$ with scale$^2=\tfrac{b_n}{a_n}(1+x_*^\top V_n x_*)$ (module 05's helper generalized); intervals widen beyond Gaussian by the $t$-multiplier (`1.076` at $\nu=17$), most at small $n$.
- **Robustness = marginalizing a latent variance.** A $t$-likelihood is a Gamma scale-mixture of Normals; outliers get small posterior precision $\mathbb E[\lambda_i]$ and are down-weighted automatically — three injected outliers move the OLS slope 84% while the $t$-slope stays within 5% of its clean-data value.
- **Bias–variance is prior strength.** Under a basis expansion, underfit/overfit = prior too strong/too weak; "how many features?" becomes "how strong a prior?", a continuous knob the evidence sets — the doorway to Gaussian processes (module 20) and Occam (module 17).

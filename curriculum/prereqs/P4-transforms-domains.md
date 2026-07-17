# P4. Transforms, domains, and scale

> **Spine.** Move a variable to where the algorithm lives (unconstrained ℝ, unit scale), and pay the Jacobian toll every time you carry a *density* across — transforming samples is free, transforming densities is not.
> **Which line?** Plumbing for all four: every conditioning step, predictive integral, and decision that runs a sampler or optimizer first reparameterizes, then owes `log|f'|`.
> **Promise.** After this you reparameterize a constrained model without silently biasing its posterior, read any law as `μ + σ·Z`, and never confuse a mean's SE with a prediction's spread.
> **Prereqs.** P1 (density algebra), P3 (precision). **Runtime.** 12 s.
> **Sources.** C-B §2.1 (transformations), §5.5 (order statistics); booklet ch. 4 (Jeffreys); EXAM, M07/M11/M13/M14/M15/M25 walls.

The unifying fact the whole course leans on and never states in one place: **optimizers and samplers want to live in unconstrained ℝⁿ.** A variance in $(0,\infty)$, a probability in $(0,1)$, a simplex of weights — each must be mapped to $\mathbb R$, worked on there, and mapped back. And *the density carries a Jacobian toll every time you cross.* Half of "my sampler is broken" is a missing constraint; the other half is a missing $\log|f'|$.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "P4-transforms-domains"          # this module's figure dir
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

## P4.1 The domain dictionary

**Reflex.** See a constrained parameter, and *before writing model code* know its standard bijection to $\mathbb R$ and the inverse — so the sampler never proposes a $-0.3$ variance.

**The wall.** `M15:47` writes the logistic link `$\sigma(\eta)=\frac1{1+e^{-\eta}}$` as if obvious; `EXAM:230` maps an optimizer's free parameter back with one keystroke, `th = expit(phi)`. Neither pauses to justify why $(0,1)\leftrightarrow\mathbb R$ — because to a fluent reader the four canonical maps are reflex:

| domain | forward $\to\mathbb R$ | inverse $\mathbb R\to$ domain |
|---|---|---|
| $(0,\infty)$ | $y=\log x$ | $x=e^{y}$ |
| $(0,1)$ | $y=\operatorname{logit}x=\log\frac{x}{1-x}$ | $x=\operatorname{expit}y=\frac{1}{1+e^{-y}}$ |
| simplex $\Delta_K$ | $K{-}1$ free logits | $x=\operatorname{softmax}(\text{logits})$, one d.o.f. pinned |
| ordered $x_1<\dots<x_K$ | first free, $\log$ the gaps | `cumsum` of $[x_1,e^{\delta_2},\dots]$ |

The simplex line hides a trap the course fixes at `M25:59`: softmax is **shift-redundant** — $\operatorname{softmax}(z)=\operatorname{softmax}(z+c)$ — so $K$ logits over-parameterize a $K{-}1$-dimensional surface. Pin one logit to $0$ and the model is identified; leave all $K$ free and an optimizer wanders along the flat shift direction forever.

**The fix.**

```python
from scipy.special import expit, logit, softmax
# (0, inf): work in y = log(sigma); map back with exp -> never proposes sigma < 0
y = rng.normal(0, 1, 5); sigma = np.exp(y)
print("exp keeps sigma > 0 always:", bool(np.all(sigma > 0)))
# (0,1): logit/expit round-trip is exact to machine precision
theta = np.array([0.05, 0.5, 0.9])
print("logit->expit round-trip max err:", f"{np.max(np.abs(expit(logit(theta)) - theta)):.1e}")
# simplex: softmax is SHIFT-redundant, so pin one logit to 0 to identify K-1 free d.o.f.
z = np.array([1.3, -0.7, 2.1])
print("softmax(z) == softmax(z + 5):", bool(np.allclose(softmax(z), softmax(z + 5.0))))
w = softmax(np.append([1.3, -0.7], 0.0))              # 2 free logits, last pinned -> 3 weights
print(f"3-simplex from {2} free logits, weights sum = {w.sum():.4f}")
```

**Drill — the ordered transform.**
*Setup:* You need three strictly increasing cutpoints from an unconstrained $\mathbb R^3$ draw.
*Predict:* If you exponentiate all three coordinates and `cumsum`, are the results strictly increasing? What if you exponentiate only the last two?
*Reason:* "Positive steps stay ordered" — but the *first* point can be anywhere.
*Run:*
```python
r = rng.normal(size=3)
cuts = np.concatenate([r[:1], np.exp(r[1:])]).cumsum()   # first free, gaps positive
print("cutpoints:", np.round(cuts, 3), " increasing:", bool(np.all(np.diff(cuts) > 0)))
```
<details><summary>Reconcile</summary>

Only the *gaps* must be positive; the first cutpoint is free. Exponentiating all three would force $x_1>0$ — a silent constraint you never intended (ordinal cutpoints are often negative). The recipe is: first element free, `exp` the $K-1$ gaps, `cumsum`. This is exactly the ordered-logit construction behind `M15:465`'s cumulative link.
</details>

## P4.2 The Jacobian price — the section's #1 gate

**Reflex.** Every time you transform a random variable, you add $+\log|dx/dy|$ to the log-density *in the same keystroke as the transform* — or you consciously note you are moving samples, which owe nothing.

**The wall.** `EXAM:234` scores a logit-space posterior with `ljac = np.log(th) + np.log1p(-th)  # |d theta/d phi| = theta(1-theta)`; `M07:183` shows a "flat" prior is not flat because `p(ψ) = p(θ)|dθ/dψ| = θ(1-θ)`; `M13:126` transforms a Beta density to logit space "with a Jacobian dθ/dφ = θ(1−θ)." Drop that factor and nothing errors — the posterior is just quietly wrong.

The univariate rule, derived from the CDF in three lines (for monotone $f$, $\phi=f(\theta)$):
$$F_\phi(\phi)=P(f(\theta)\le\phi)=F_\theta(f^{-1}(\phi))\ \Rightarrow\ p_\phi(\phi)=p_\theta(f^{-1}(\phi))\left|\frac{d\theta}{d\phi}\right|,\qquad \log p_\phi=\log p_\theta+\log\left|\frac{d\theta}{d\phi}\right|.$$

**Two directions people confuse.** *Transforming samples is free:* draw $\theta$, apply $\phi=\operatorname{logit}\theta$, and the resulting $\phi$-samples are already correctly distributed — no correction, because you moved *points*, not a *formula*. *Transforming a density pays:* if you want the algebraic density $p_\phi$, you multiply by $|d\theta/d\phi|$. Marquee demonstration of both, staged.

*Setup.* Put a **flat** prior on $\theta\in(0,1)$ and look at it on the log-odds scale $\psi=\operatorname{logit}\theta$.
*Predict.* Is the induced density of $\psi$ flat, or peaked, or spread out?
*Reason.* Naive intuition: "uniform is assumption-free, so it stays uniform under a relabeling."

```python
# Transforming SAMPLES is free -- just apply the map:
theta_u = rng.uniform(0, 1, 200_000)
psi = logit(theta_u)                          # correctly distributed already, no Jacobian
# Transforming the DENSITY pays: p_psi = p_theta * |dtheta/dpsi| = 1 * theta(1-theta)
def psi_density(p):
    th = expit(p)
    return th * (1 - th)
print(f"induced density at psi=0: {psi_density(0.0):.4f}   at psi=3: {psi_density(3.0):.4f}")
print(f"even-odds preference ratio: {psi_density(0.0) / psi_density(3.0):.2f}")

g = np.linspace(-6, 6, 400)
fig, ax = plt.subplots()
ax.hist(psi, bins=80, density=True, alpha=0.4, label="logit of flat samples (free)")
ax.plot(g, psi_density(g), "C1", lw=2, label=r"Jacobian density $\theta(1-\theta)$")
ax.set(xlabel=r"$\psi=\mathrm{logit}\,\theta$", ylabel="density",
       title="Flat in $\\theta$ is a logistic bell in log-odds — samples and Jacobian agree")
ax.legend()
save(fig, "flat-isnt-flat")
```

*Reconcile.* Not flat. A uniform on $\theta$ becomes a **logistic** bell on $\psi$, density `0.2500` at $\psi=0$ versus `0.0452` at $\psi=3$ — a `5.53`-fold preference for even odds your "assumption-free" prior never advertised. And the histogram of *transformed samples* lands exactly on the Jacobian curve, confirming the two directions describe the same object: samples were free, the density paid $\theta(1-\theta)$.

![Histogram of logit-transformed uniform samples overlaid with the analytic Jacobian density θ(1−θ); they coincide on a bell peaked at ψ=0.](figures/P4-transforms-domains/flat-isnt-flat.png)

Now the silent bug, quantified. Suppose your posterior in $\theta$ is $\mathrm{Beta}(2,5)$ (mean $2/7$) and you reparameterize to $\phi=\operatorname{logit}\theta$ to sample or optimize in $\mathbb R$. Do it right (with $\log|d\theta/d\phi|$) and the $\phi$-distribution pushes back to $\mathrm{Beta}(2,5)$. **Forget the Jacobian** and you are working with a *different* distribution — one whose pushforward to $\theta$ is $\propto\theta^{1}(1-\theta)^{4}/[\theta(1-\theta)]=(1-\theta)^{3}=\mathrm{Beta}(1,4)$.

*Predict.* Dropping $\log|f'|$ shifts $\mathbb E[\theta]$ toward 0 or toward 1 — which way, and by roughly how much (a nudge in the third decimal, or a move of order $0.05$–$0.10$)? Commit before running.

```python
from scipy.stats import beta as beta_dist
a_post, b_post = 2.0, 5.0
th = np.linspace(1e-4, 1 - 1e-4, 40000); phi = logit(th)
correct = beta_dist(a_post, b_post).pdf(th) * (th * (1 - th))   # WITH Jacobian |dtheta/dphi|
forgot  = beta_dist(a_post, b_post).pdf(th)                     # Jacobian dropped
def mean_theta(phi_density):                # normalize in phi, then E[theta]
    w = phi_density / np.trapezoid(phi_density, phi)
    return np.trapezoid(expit(phi) * w, phi)
m_ok, m_bad = mean_theta(correct), mean_theta(forgot)
print(f"E[theta]: correct={m_ok:.4f}  jacobian-forgotten={m_bad:.4f}  bias={m_bad - m_ok:+.4f}")
print(f"analytic check: Beta(2,5) mean={2/7:.4f}, Beta(1,4) mean={1/5:.4f}")

fig, ax = plt.subplots()
ax.plot(th, beta_dist(2, 5).pdf(th), "C1", lw=2, label="correct posterior Beta(2,5)")
ax.plot(th, beta_dist(1, 4).pdf(th), "C3", lw=2, label="forgotten-Jacobian pushforward Beta(1,4)")
ax.axvline(2/7, color="C1", ls=":"); ax.axvline(1/5, color="C3", ls=":")
ax.set(xlabel=r"$\theta$", ylabel="density",
       title="Dropping $\\log|f'|$ silently shifts the posterior toward 0")
ax.legend()
save(fig, "jacobian-bias")
```

The posterior mean slides from `0.2857` to `0.2001`, a bias of `-0.0856` toward small $\theta$ (the analytic pushforward is exactly $\mathrm{Beta}(1,4)$, mean `0.2000`) — the exact failure the expert file flags as the #1 gate: "reparameterize without $\log|f'|$ and the posterior is silently biased." No exception was raised; only a conjugate cross-check would have caught it.

![Two Beta densities on θ: the correct Beta(2,5) and the Beta(1,4) you get by forgetting the Jacobian, with their means marked — the forgotten version is pulled toward zero.](figures/P4-transforms-domains/jacobian-bias.png)

## P4.3 Location–scale as an identity habit

**Reflex.** Read any "nice" law as $\mu+\sigma Z$ ($Z$ standardized), and remember scipy's `scale` is the **standard deviation**, never the variance.

**The wall.** `M11:107` reconstructs a Student-$t$ scale from Normal–Inverse-Gamma hyperparameters as `t_scale = np.sqrt(bn / (an*kn))`; `EXAM:285` assembles the full predictive as `df, mu_scale = 2*an4, np.sqrt(bn4/(an4*kn))`. If you cannot read location/scale, you conflate scale with SD and the interval is wrong.

**The fix.**

```python
Z = rng.standard_normal(200_000)
X = 3 + 2 * Z                                # N(mean=3, VARIANCE=4): sd=2, NOT var=2
print(f"mu + sigma*Z: mean={X.mean():.3f} (want 3), sd={X.std():.3f} (want 2)")
# Assemble a Student-t marginal from NIG hyperparameters (the M11/EXAM recipe):
an, bn, kn, mn = 4.5, 3.2, 11.0, 0.7
df, loc, t_scale = 2 * an, mn, np.sqrt(bn / (an * kn))    # t_nu(loc, scale) -- scale, not variance
print(f"mu ~ t_{df:.0f}(loc={loc:.3f}, scale={t_scale:.3f})")
```

**The predictive-vs-SE trap.** `EXAM:787` scales a *prediction* interval by `s * np.sqrt(1 + 1/n)`, not the standard error $s\sqrt{1/n}$ of the mean. The extra $1$ is the new observation's own variance. Confuse them and a 95% prediction interval covers far less than 95%.

*Setup:* $n=6$ standard-normal observations. You build a 95% interval for a genuinely **new** draw two ways.
*Predict:* The SE-width interval (scale $s\sqrt{1/n}$) — what fraction of new observations does it actually cover?
*Reason:* "It's a 95% interval, so ~95%." (It is a 95% interval for the *mean*, not for a new point.)

```python
n = 6; reps = 40000
Zd = rng.standard_normal((reps, n))
ybar, s = Zd.mean(1), Zd.std(1, ddof=1)
ynew = rng.standard_normal(reps)             # a brand-new observation ~ N(0,1)
tq = stats.t.ppf(0.975, n - 1)
half_se   = tq * s * np.sqrt(1 / n)          # WRONG for a new obs: spread of the MEAN
half_pred = tq * s * np.sqrt(1 + 1 / n)      # RIGHT: predictive spread
cov_se   = np.mean(np.abs(ynew - ybar) <= half_se)
cov_pred = np.mean(np.abs(ynew - ybar) <= half_pred)
print(f"coverage of a NEW obs: SE-width={cov_se:.4f}   predictive-width={cov_pred:.4f}")
print(f"width ratio sqrt(1+1/n)/sqrt(1/n) = {np.sqrt(1 + 1/n)/np.sqrt(1/n):.3f}")
```
<details><summary>Reconcile</summary>

The SE-width interval covers only `0.6271` of new observations, not 0.95, while the predictive width hits `0.9514`. The SE $s\sqrt{1/n}$ measures how tightly $\bar y$ pins the *mean*; a new draw scatters around that mean with its own unit variance, so the honest spread is $s\sqrt{1+1/n}$ — here `2.646`× wider. This is the same $\sqrt{1+1/n}$ that appears in every conjugate posterior-predictive (M05's `student_t_predictive`): prediction is always wider than estimation.
</details>

## P4.4 Standardize before you think

**Reflex.** Before fitting, plotting, or setting a prior, z-score the data so "1 unit" means "1 SD" — and standardize with **training moments only**, or you leak.

**The wall.** `M25:105` writes `Xtr=(Xtr-mu)/sd; Xval=(Xval-mu)/sd; Xte=(Xte-mu)/sd` with $\mu,\sigma$ from the *training* split; the mined note is blunt — "standardize on TRAINING moments only; using test moments leaks and corrupts the calibration audit." `M14:186` centers so a no-intercept ridge penalty is fair.

**The fix.**

```python
n = 400
x = rng.normal(50, 10, n); y = 2.0 + 0.3 * x + rng.normal(0, 1, n)
xs = (x - x.mean()) / x.std()
b_std = np.polyfit(xs, y, 1)[0]              # slope in standardized units
b_orig = b_std / x.std()                     # un-standardize: original slope = b_std / sd_x
print(f"recovered slope {b_orig:.4f} vs direct fit {np.polyfit(x, y, 1)[0]:.4f}")
# Leakage: standardize val with TRAIN moments (honest) vs its OWN moments (leaked).
xtr, xval = x[:300], x[300:]
mu_tr, sd_tr = xtr.mean(), xtr.std()
honest = (xval - mu_tr) / sd_tr
leaked = (xval - xval.mean()) / xval.std()
print(f"val mean after standardizing: train-moments={honest.mean():+.3f} (!=0, honest) "
      f"vs own-moments={abs(leaked.mean()):+.3f} (==0, leaked)")
```

Recovered and direct slopes match; the leaked path *forces* the validation mean to exactly `0.000`, erasing the very distribution shift a calibration audit exists to detect.

## P4.5 Argmax invariance under monotone maps

**Reflex.** A monotone map never moves the argmax — so maximize the log-likelihood, and know temperature scaling can never flip a decision at $0.5$.

**The wall.** `M25:124` states temperature scaling "cannot change a decision (it never crosses $0.5$)"; `M17:183` selects a model by `max(mean_ev, key=...)` trusting that $\log$ is monotone; `M15:70` minimizes cross-entropy knowing it shares an argmax with the Bernoulli likelihood.

**The fix.**

```python
logits = rng.normal(0, 1.5, (2000, 3))       # 2000 items, 3 classes
def sm(z, T=1.0):
    z = z / T; z = z - z.max(1, keepdims=True); e = np.exp(z)
    return e / e.sum(1, keepdims=True)
base = sm(logits).argmax(1)
flips = max(np.mean(sm(logits, T).argmax(1) != base) for T in [0.2, 0.5, 2.0, 5.0])
print(f"argmax class flips across T in [0.2..5]: {flips:.4f}")
# binary 0.5 threshold = sign test on the logit -> temperature-invariant
lo = logit(expit(rng.normal(0, 2, 5000)))
frac = np.mean((expit(lo / 3.0) > 0.5) != (expit(lo / 1.0) > 0.5))
print(f"0.5-decisions changed by temperature T=3: {frac:.4f}")
# log is monotone: argmax(lik) == argmax(log lik)
lik = rng.random(1000)
print("argmax(lik) == argmax(log lik):", int(np.argmax(lik)) == int(np.argmax(np.log(lik))))
```

Temperature rescales *confidence* but moves no argmax and crosses no threshold; that is why calibration is a separate concern from accuracy. Log-monotonicity is why we always optimize in log-space (P7's home turf): the mode is preserved and the arithmetic is stable.

## P4.6 Order-statistics quantile hygiene

**Reflex.** A finite-sample quantile is an order statistic, and *which* one matters: the conformal band uses the $\lceil (n+1)\alpha\rceil$-th, via `method="higher"`, not the naive interpolated quantile.

**The wall.** `EXAM:799` computes `qhat = np.quantile(cal, np.ceil((200 + 1) * 0.9) / 200, method="higher")`; the mined note warns the naive quantile *undercovers*. `np.quantile`'s default linear interpolation silently disagrees with the guarantee.

*Setup:* $n=20$ calibration scores $|Z|$; you want a band covering $\ge 90\%$ of new scores.
*Predict:* Does the plain `np.quantile(cal, 0.90)` band cover $90\%$ on average, or under?
*Reason:* "The 90th percentile covers 90%." (It does in the limit; at $n=20$ the finite-sample correction bites.)

```python
R, n = 20000, 20
cal  = np.abs(rng.standard_normal((R, n)))
test = np.abs(rng.standard_normal(R))        # one fresh test point per calibration set
alpha = 0.90
q_naive = np.quantile(cal, 0.90, axis=1)                      # default linear interpolation
k = int(np.ceil((n + 1) * alpha))                            # conformal order-statistic index
q_conf = np.sort(cal, axis=1)[:, k - 1]                      # k-th smallest (here also = method="higher" at this level)
print(f"k = ceil((n+1)*alpha) = {k} of n={n}")
print(f"naive np.quantile(.90): coverage={np.mean(test <= q_naive):.4f} (target 0.90)")
print(f"conformal order stat  : coverage={np.mean(test <= q_conf):.4f} (>= 0.90 guaranteed)")
one = cal[0]
print("one cal set, np.quantile @0.90 by method:",
      {m: round(float(np.quantile(one, 0.90, method=m)), 3)
       for m in ["linear", "higher", "lower", "nearest"]})
```
<details><summary>Reconcile</summary>

The naive band covers about `0.8669` — under the target — while the conformal $k=$`19`-th order statistic covers `0.9080`, at or above 0.90 by construction (exchangeability gives coverage $\ge\lceil(n+1)\alpha\rceil/(n+1)$). The four `method=` values for the *same* data differ in the third decimal: a quantile is not a single number until you name the interpolation rule. For finite-sample guarantees, take the order statistic and round *up*.
</details>

## Bridge — where the wall is C-B and the course

C-B §2.1 gives the change-of-variables theorem you just used; §5.5 defines order statistics and their exact distributions, the machinery behind P4.6. The booklet's Jeffreys-prior derivation (ch. 4, and `M07`) is nothing but the Jacobian applied to $\sqrt{\mathcal I(\theta)}$ so the prior is coordinate-free — the same toll, paid on purpose. And the non-centered reparameterization that dissolves hierarchical funnels (`M16:165`, `M18:233`) is location–scale plus a Jacobian: $\theta=\mu+\tau z$, $z\sim N(0,1)$. Every one of these is the same reflex wearing a different hat.

## Pitfalls

- **Reparameterizing a density without $\log|f'|$.** The #1 silent bias (P4.2). If a sampler runs in transformed space but scores in original space, add the Jacobian or expect a mode/quantile shift you'll only catch against a conjugate answer.
- **Confusing "transform samples" with "transform densities."** Samples are free; densities pay. Mapping MCMC draws through $\exp$ needs no correction; writing down the $\exp$-scale density does.
- **`scale` vs variance.** `scipy.stats` `scale` is the SD. `norm(loc, scale=4)` is $N(4,16)$, not $N(4,4)$.
- **SE where you need predictive spread.** $\sqrt{1/n}$ pins the mean; a new observation needs $\sqrt{1+1/n}$. Undercoverage every time (P4.3).
- **Leaky standardization.** Test/validation moments must come from training. Standardizing each split by itself erases the shift your audit is meant to find (P4.4).
- **Naive `np.quantile` for finite-sample bands.** Default interpolation undercovers; conformal needs $\lceil(n+1)\alpha\rceil/n$ with `method="higher"` (P4.6).

## Exercises

**Exercise P4.1 — the reverse Jacobian bites harder.**
*Setup:* A *flat log-odds* prior — uniform on $\psi=\operatorname{logit}\theta\in\mathbb R$ — is pushed back to the $\theta$ scale.
*Predict:* Is the induced $\theta$-prior flat, gently curved, or does it spike? Where?
*Reason:* "Flat in one coordinate is roughly flat in another." (P4.2 already dented this; now the map runs the other way.)
*Run:*
```python
tt = np.linspace(1e-3, 1 - 1e-3, 999)
theta_prior = 1.0 / (tt * (1 - tt))          # p_theta = p_psi * |dpsi/dtheta| = 1/(theta(1-theta))
print(f"density at theta=0.5: {theta_prior[len(tt)//2]:.3f}   at theta=0.01: {theta_prior[0]:.1f}")
print(f"integral over (eps,1-eps): {np.trapezoid(theta_prior, tt):.1f}  (diverges as eps->0)")
```
<details><summary>Reconcile</summary>

It spikes at both ends as $1/[\theta(1-\theta)]$ — the improper **Haldane** prior, non-integrable at $0$ and $1$. Uniform-on-$\psi$ is not a mild relabeling of uniform-on-$\theta$; the two disagree violently, and one of them isn't even a probability distribution. There is no coordinate-free "flat" — always ask *flat in which parameterization, and does it mean anything.* This is the mechanism behind `M07`'s Jeffreys detour.
</details>

**Exercise P4.2 — temperature can't rescue an argmax (ML connection).**
*Setup:* A 3-class classifier outputs logits $[2.0, 1.9, 0.1]$. A colleague argues that raising the softmax temperature will "make class 1 more competitive with class 0 and eventually win."
*Predict:* Across $T\in\{0.1,1,10,100\}$, does the predicted class ever change from class 0?
*Reason:* Temperature "flattens the distribution," so surely it reorders the top two.
*Run:*
```python
zz = np.array([2.0, 1.9, 0.1])
preds = {T: int(np.argmax(zz / T)) for T in [0.1, 1.0, 10.0, 100.0]}
print("argmax by temperature:", preds)
```
<details><summary>Reconcile</summary>

Always class 0. Dividing every logit by $T>0$ is a strictly monotone rescaling; it *cannot* reorder them, so the argmax is frozen. Temperature moves the *probabilities* (the gap between class 0 and 1 shrinks toward a tie but never crosses) while the decision is nailed down. This is why temperature scaling is a pure calibration knob — it fixes overconfident probabilities without touching accuracy, exactly the `M25` claim.
</details>

**Exercise P4.3 — recover a slope through two transforms.**
*Setup:* You fit on standardized $x$ *and* standardized $y$, getting a standardized slope $\tilde b$. You need the original-units slope.
*Predict:* Is the original slope $\tilde b$, $\tilde b\cdot s_y/s_x$, or $\tilde b\cdot s_x/s_y$?
*Reason:* "Standardizing is symmetric, so the corrections cancel."
*Run:*
```python
xx = rng.normal(20, 4, 500); yy = 5 + 1.5 * xx + rng.normal(0, 2, 500)
bt = np.polyfit((xx - xx.mean()) / xx.std(), (yy - yy.mean()) / yy.std(), 1)[0]
b_recovered = bt * yy.std() / xx.std()
print(f"recovered {b_recovered:.4f} vs direct {np.polyfit(xx, yy, 1)[0]:.4f}")
```
<details><summary>Reconcile</summary>

The original slope is $\tilde b\cdot s_y/s_x$: each SD is a Jacobian factor for its own axis, and a slope is $\Delta y/\Delta x$, so the $y$-scale multiplies and the $x$-scale divides. They do *not* cancel unless $s_x=s_y$. (The standardized slope is the correlation coefficient here — a scale-free quantity — which is precisely why you must reintroduce both scales to get back to units.)
</details>

## Where the course uses this

| Skill | Course walls it removes (module:line) |
|---|---|
| Domain dictionary / links | `M15:47`, `M13:125`, `M23:427`, `M24:297`, `M25:130`, `EXAM:230` |
| Jacobian price (change of variables) | `EXAM:234`, `M07:183`, `M13:126`, `M14:314`, `M20:342`, `M21:236` |
| Location–scale identity | `M11:107`, `M14:268`, `M15:242`, `M16:165`, `M21:18`, `EXAM:285` |
| Standardize / no-leak moments | `M25:105`, `M14:186`, `M20:270`, `M22:141`, `M23:302`, `M15:58` |
| Argmax invariance | `M25:124`, `M25:59`, `M15:70`, `M17:183`, `M21:302`, `M22:214` |
| Order-statistic quantiles | `EXAM:799`, `M05:337`, `M09:63`, `M24:315` |

## Takeaways

- **Optimizers and samplers live in unconstrained $\mathbb R^n$.** Know the four maps cold: $\log/\exp$, $\operatorname{logit}/\operatorname{expit}$, softmax (pin one logit), ordered-via-`cumsum`.
- **Transforming samples is free; transforming a density pays $\log|dx/dy|$.** Forget it in a reparameterized model and the posterior is silently biased — the section's #1 gate.
- **There is no coordinate-free "flat."** Flat in $\theta$ is a logistic bell in log-odds; flat in log-odds is the improper Haldane spike in $\theta$.
- **Read every law as $\mu+\sigma Z$**, and remember scipy `scale` is the SD. Prediction spread is $\sqrt{1+1/n}$; the mean's SE is $\sqrt{1/n}$ — never swap them.
- **Standardize with training moments only.** Using each split's own moments leaks and hides the very shift you audit for.
- **Monotone maps never move an argmax.** Optimize the log; temperature rescales confidence, never a $0.5$ decision.
- **A finite-sample quantile is an order statistic** — name the interpolation rule; conformal bands need $\lceil(n+1)\alpha\rceil/n$ with `method="higher"`, or they undercover.

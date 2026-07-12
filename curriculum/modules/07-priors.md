# 07. Priors: What They Are and Aren't

> **Spine.** The prior is part of the model — the same epistemic status as the likelihood (which you also chose); sometimes it matters, often it washes out, and for an unidentified parameter it *never* washes out.
> **Which line?** Line 1 (a model is a joint $p(\text{unknowns},\text{knowns})$). The prior $p(\theta)$ is the marginal factor of that joint; picking it is modeling, not metaphysics.
> **Promise.** After this module you can answer the skeptic's "doesn't the prior just bias the answer?" with a picture, stress-test a prior before seeing data, derive the one prior that ignores your choice of coordinates, spot the improper prior that silently breaks, and name exactly when more data will *not* rescue you.
> **Prereqs.** Modules 00 (four lines), 02 (conditioning), 04 (Fisher information — Jeffreys is built on it); light callbacks to 05 (conjugate Beta updating) and 06 (MAP = penalized MLE).
> **Runtime.** ~7 s.
> **Sources.** Booklet ch. 15 (variance-component priors; quotes verified verbatim, citing Gelman BA 2006); booklet ch. 5 and 7 in passing; BDA3 ch. 2–3 by concept; Jeffreys and Bernardo (reference priors) by concept.

A machine-learning reader arrives at Bayesian inference with one honest objection: *you get to make up the prior, so you can make the answer come out however you like.* The reply: the prior is a modeling choice with the *same status as the likelihood* — you also "made up" the assumption that the data are Bernoulli — and like any modeling choice it is testable, coordinate-dependent, and sometimes decisive, sometimes irrelevant. Which one it is, you can compute.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "07-priors"                       # this module's figure dir
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

## 07.1 The sensitivity fan: does the prior even matter?

**Setup.** One estimand: a success rate $\theta$ (conversion rate, click-through, a coin's bias). Five *defensible* priors, chosen to disagree as much as honest analysts might: `Beta(1,1)` (uniform / Laplace), `Beta(0.5,0.5)` (Jeffreys, §07.4), `Beta(2,2)` (weakly informative, centered at ½), `Beta(8,2)` (informative optimist, prior mean 0.8), `Beta(2,8)` (informative pessimist, prior mean 0.2). We observe the same success rate `0.3` at two sample sizes: 3 of 10, and 3000 of 10000.

**Predict.** Before running: at $n=10$, how far apart are the five posterior means — a spread of about 0.02, 0.10, or 0.30? And at $n=10{,}000$? Commit to two numbers.

**Reason.** The naive ML intuition is "the prior is a bias term; it always shifts the answer by roughly its own strength." If that were true the spread would be similar at both sample sizes.

**Run.** Each posterior is conjugate (module 05): `Beta(a,b)` + $s$ successes, $f$ failures $\Rightarrow$ `Beta(a+s, b+f)`.

```python
# Five defensible priors, one estimand, two sample sizes. Conjugate Beta updates.
priors = {
    "Beta(1,1) uniform":    (1.0, 1.0),
    "Beta(0.5,0.5) Jeffreys":(0.5, 0.5),
    "Beta(2,2) weak":       (2.0, 2.0),
    "Beta(8,2) optimist":   (8.0, 2.0),
    "Beta(2,8) pessimist":  (2.0, 8.0),
}
datasets = {"n=10 (s=3)": (3, 7), "n=10,000 (s=3000)": (3000, 7000)}

for dname, (s, f) in datasets.items():
    means = [(a + s) / (a + s + b + f) for a, b in priors.values()]
    spread = max(means) - min(means)
    print(f"{dname:20s}: means {min(means):.4f}..{max(means):.4f}, "
          f"spread across priors = {spread:.4f}")
```

At $n=10$ the five posterior means fan from `0.2500` (pessimist) to `0.5500` (optimist) — a spread of `0.3000`, half the 0.6 span of the prior means themselves (0.2 to 0.8): ten observations have only begun to close the disagreement. At $n=10{,}000$ the same five priors give means within `0.0006` of one another: the data have overwritten the disagreement. The naive "constant bias" intuition fails because a conjugate prior is worth a *fixed number of pseudo-observations* (module 05's reading: `Beta(a,b)` = $a{+}b$ pseudo-trials), so its weight is $\tfrac{a+b}{a+b+n}$ — decisive at $n=10$, negligible at $n=10{,}000$.

```python
# The two fans, side by side: prior matters at small n, washes out at large n.
grid = np.linspace(1e-3, 1 - 1e-3, 600)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))
for ax, (dname, (s, f)) in zip(axes, datasets.items()):
    for pname, (a, b) in priors.items():
        ax.plot(grid, stats.beta(a + s, b + f).pdf(grid), label=pname, lw=1.8)
    ax.axvline(0.3, ls="--", color="k", lw=1)
    ax.set_title(f"{dname}: posteriors under 5 priors")
    ax.set_xlabel(r"$\theta$"); ax.set_ylabel("posterior density")
axes[0].set_xlim(0, 1); axes[1].set_xlim(0.27, 0.33)
axes[0].legend(fontsize=8)
fig.suptitle("Sensitivity fan — the prior moves the answer only while data are scarce")
fig.tight_layout(rect=(0, 0, 1, 0.94))
save(fig, "sensitivity-fan")
```

![Left: at n=10 the five posteriors are visibly different bumps spanning 0.25–0.55. Right: at n=10,000 the five posteriors are one indistinguishable spike at 0.30.](figures/07-priors/sensitivity-fan.png)

**Reconcile.** The skeptic is right at $n=10$ and wrong at $n=10{,}000$, and now you can tell which regime you are in *before* arguing about it: compute the fan. This is the module's thesis in one figure — the prior is neither harmless nor tyrannical; its influence is a measurable quantity that decays like $1/n$ **for identified parameters**. Section 07.6 finds the parameter for which it never decays at all.

## 07.2 Prior predictive checks: audit the prior before the data arrive

A prior is not an abstract confession of belief; combined with the likelihood it makes *checkable predictions about data*. The **prior predictive distribution** is line 3 (prediction = marginalization) run with the prior in place of the posterior:
$$p(\tilde y) = \int p(\tilde y \mid \theta)\,p(\theta)\,d\theta.$$
Simulate $\theta$ from the prior, push it through the likelihood, and look at the fake datasets. If they are absurd, the prior is absurd — and you learned this for free, before spending any data. Here is the reusable harness.

```python
# Reusable prior-predictive harness: draw theta ~ prior, y-tilde ~ likelihood, summarize.
def prior_predictive(prior_sampler, sim_data, M=40000):
    """prior_sampler(M)->theta[M]; sim_data(theta)->y_tilde[M]. Returns (theta, y_tilde).
    Samplers control their own randomness (close over a generator or seed one)."""
    theta = prior_sampler(M)
    ytilde = sim_data(theta)
    return theta, ytilde
```

**The basketball example.** We model a player's free-throw make-count out of $n=20$ attempts as Binomial$(20,\theta)$. A colleague, reaching for a "vague" prior, proposes $\theta \sim N(0.5, 10^2)$ — "centered at a coin flip, huge variance, surely noninformative." It is a disaster, and the prior predictive says so instantly.

```python
# A Normal(0.5, 10^2) prior on a PROBABILITY puts almost all its mass outside [0,1].
sd_absurd = 10.0
p_below0 = stats.norm(0.5, sd_absurd).cdf(0.0)
p_above1 = stats.norm(0.5, sd_absurd).sf(1.0)
print(f"N(0.5,10^2): P(theta<0)={p_below0:.4f}, P(theta>1)={p_above1:.4f}, "
      f"outside [0,1] = {p_below0 + p_above1:.4f}")

# Prior predictive make-counts. The absurd prior is only usable after clipping theta
# to [0,1] (the likelihood needs a valid probability); the clipping IS the pathology.
def absurd_prior(M):   return np.clip(rng.normal(0.5, sd_absurd, M), 0.0, 1.0)
def sensible_prior(M): return rng.beta(2.0, 2.0, M)          # weakly informative
def sim_makes(theta):  return rng.binomial(20, theta)

_, y_absurd  = prior_predictive(absurd_prior,  sim_makes)
_, y_sensible = prior_predictive(sensible_prior, sim_makes)
tail_absurd  = np.mean((y_absurd == 0) | (y_absurd == 20))
tail_sensible = np.mean((y_sensible == 0) | (y_sensible == 20))
print(f"absurd prior : P(make 0 or all 20 of 20) = {tail_absurd:.4f}")
print(f"sensible prior: P(make 0 or all 20 of 20) = {tail_sensible:.4f}")

fig, ax = plt.subplots()
bins = np.arange(-0.5, 21.5, 1)
ax.hist(y_absurd,  bins=bins, density=True, alpha=0.6, label="N(0.5,10²) prior (clipped)")
ax.hist(y_sensible, bins=bins, density=True, alpha=0.6, label="Beta(2,2) prior")
ax.set_xlabel("prior-predictive free throws made (of 20)")
ax.set_ylabel("probability")
ax.set_title("Prior predictive check: the 'vague' Normal predicts only 0 or 20")
ax.legend()
save(fig, "prior-predictive-ft")
```

![A histogram: the Normal-prior predictive piles almost all mass at 0 and 20 makes; the Beta(2,2) predictive is a smooth mound over the middle range.](figures/07-priors/prior-predictive-ft.png)

The `N(0.5,10^2)` prior places `0.9601` of its mass on *impossible* probabilities outside $[0,1]$. Forced into the valid range by clipping, it predicts that the player makes either 0 or all 20 free throws with probability `0.9653` — a prior that "knows," before any data, that the player is either hopeless or perfect. The `Beta(2,2)` prior predicts the same all-or-nothing outcome only `0.0238` of the time; its fake box scores look like plausible free-throw shooting. "Vague on the real line" and "vague for a probability" are different things, and the prior predictive catches the confusion.

## 07.3 Flat isn't flat: "noninformative" is coordinate-dependent

The colleague's instinct — *flat = ignorant* — has a subtler failure than the wrong support, and this time it will catch you too.

**Setup.** You put `Beta(1,1)` — uniform — on $\theta$, satisfied that you have assumed nothing. A logistic-regression model of the same problem works on the log-odds scale, $\psi = \operatorname{logit}\theta = \log\frac{\theta}{1-\theta}$.

**Predict.** Sketch, before running, the density your uniform prior *induces* on $\psi$: is it flat, or peaked — and if peaked, where?

**Reason.** The reflex being tested is "flat is flat in every coordinate — ignorance doesn't care how you write the parameter." Most readers sketch something flat-ish and wide.

**Run.**

```python
# Push the uniform-on-theta draws through the log-odds transform and look.
theta_u = rng.uniform(0, 1, 200000)
psi = np.log(theta_u / (1 - theta_u))          # log-odds transform
# exact induced density at two points (formula derived in the Reconcile below)
dens0 = 0.25
dens3 = np.exp(3) / (1 + np.exp(3))**2
print(f"Uniform-theta induces on log-odds: p(psi=0)={dens0:.4f}, p(psi=3)={dens3:.4f}, "
      f"ratio={dens0/dens3:.2f}")

fig, ax = plt.subplots(1, 2, figsize=(12, 4.0))
ax[0].hist(theta_u, bins=40, density=True, color="C0")
ax[0].set_title(r"flat in $\theta$"); ax[0].set_xlabel(r"$\theta$"); ax[0].set_ylabel("density")
g = np.linspace(-8, 8, 400)
ax[1].hist(psi, bins=80, density=True, color="C1", alpha=0.7, label="sampled")
ax[1].plot(g, np.exp(g) / (1 + np.exp(g))**2, "k--", lw=1.5, label="logistic pdf")
ax[1].set_title(r"same prior, viewed on $\psi=\mathrm{logit}\,\theta$")
ax[1].set_xlabel(r"$\psi$"); ax[1].legend(fontsize=9)
fig.suptitle('"Noninformative" is coordinate-dependent — always ask: flat in WHAT?')
fig.tight_layout(rect=(0, 0, 1, 0.93))
save(fig, "flat-isnt-flat")
```

![Left panel: a flat histogram over θ on the unit interval. Right panel: the same draws on the log-odds scale form a bell-shaped logistic curve peaked at 0, decidedly not flat.](figures/07-priors/flat-isnt-flat.png)

**Reconcile.** Not flat. Uniform on $\theta$ induces the **logistic** density on the log-odds $\psi$ — a bell curve peaked at $\psi=0$ with `0.2500` there versus `0.0452` at $\psi=3$: a `5.53`-fold preference for even odds that your "assumption-free" prior never advertised. The sketch was wrong because densities carry a Jacobian: $p(\psi) = p(\theta)\left|\frac{d\theta}{d\psi}\right| = \theta(1-\theta)$, and that factor is anything but constant. Run it the other way and it bites harder: uniform on $\psi$ (flat log-odds) corresponds on the $\theta$ scale to $\pi(\theta)\propto\theta^{-1}(1-\theta)^{-1}$, which has *non-integrable spikes* at 0 and 1 — the improper **Haldane** prior of §07.5. There is no coordinate-free "flat." The honest questions are: flat in which parameterization, and does that parameterization mean anything? Two principled answers follow.

## 07.4 The Jeffreys prior, derived two ways

Jeffreys' idea removes the coordinate ambiguity by *building the parameterization-dependence into the prior so it cancels*. Define
$$\pi_J(\theta) \propto \sqrt{\mathcal I(\theta)},$$
where $\mathcal I(\theta)$ is the Fisher information from module 04 — the curvature of the log-likelihood, the sharpness of the data's voice. For one Bernoulli$(\theta)$ observation module 04 established $\mathcal I(\theta) = \tfrac{1}{\theta(1-\theta)}$, so
$$\pi_J(\theta) \propto \theta^{-1/2}(1-\theta)^{-1/2} = \text{Beta}(\tfrac12,\tfrac12)\ \text{kernel}.$$

The reason to prefer it is **invariance**: Jeffreys gives the same posterior no matter which coordinate you compute in. This is not an axiom to accept — it is a fact to verify, by two routes on the same data, $s=7$ successes in $n=10$. **Route A:** apply Jeffreys in $\theta$ directly, giving posterior $\text{Beta}(s+\tfrac12,\,n-s+\tfrac12)$. **Route B:** reparameterize to the log-odds $\psi$, put *Jeffreys-in-$\psi$* there ($\pi_J(\psi)\propto\sqrt{\mathcal I_\psi(\psi)}$, with $\mathcal I_\psi = \mathcal I_\theta(d\theta/d\psi)^2 = \theta(1-\theta)$), condition on the data in $\psi$-space, then transform the posterior *back* to $\theta$. If Jeffreys is genuinely invariant, the two posteriors coincide.

```python
# Route 1: Jeffreys = sqrt(Fisher info). For Bernoulli, I(theta)=1/(theta(1-theta)).
th = np.linspace(1e-4, 1 - 1e-4, 20000)
jeffreys_unnorm = np.sqrt(1.0 / (th * (1 - th)))        # sqrt(I(theta))
beta_half = stats.beta(0.5, 0.5).pdf(th)               # candidate: Beta(1/2,1/2)
scale = beta_half[10000] / jeffreys_unnorm[10000]      # match at theta=0.5
print(f"Jeffreys sqrt(I) vs Beta(1/2,1/2): max|diff| after scaling = "
      f"{np.max(np.abs(scale*jeffreys_unnorm - beta_half)):.2e}")

# Route 2: put Jeffreys on the log-odds psi, do inference there, transform back to theta.
s, n = 7, 10
post_A = stats.beta(s + 0.5, n - s + 0.5).pdf(th)                 # Jeffreys applied in theta
# In psi-coords: prior ∝ sqrt(I_psi) = sqrt(theta(1-theta)); likelihood theta^s(1-theta)^(n-s);
# posterior_psi ∝ product; transform to theta via |dpsi/dtheta| = 1/(theta(1-theta)).
prior_psi = np.sqrt(th * (1 - th))
lik = th**s * (1 - th)**(n - s)
post_psi = lik * prior_psi                     # unnormalized posterior in psi coords
post_B = post_psi / (th * (1 - th))            # Jacobian dpsi/dtheta pushes it back to theta
post_B /= np.trapezoid(post_B, th)             # normalize
print(f"Jeffreys posterior via theta vs via log-odds: max|diff| = "
      f"{np.max(np.abs(post_A - post_B)):.2e}")
```

Two checks land at once. The scaled $\sqrt{\mathcal I(\theta)}$ matches the `Beta(0.5,0.5)` density to `7.11e-15` — Jeffreys for a Bernoulli rate *is* `Beta(½,½)`, the arcsine prior with gentle spikes toward 0 and 1. And the two inference routes agree to `5.64e-12` — a numerical zero: Jeffreys-in-$\theta$ and Jeffreys-in-$\psi$-transformed-back are the *same posterior*; the prior absorbed the coordinate change exactly, which is the whole point. (A flat prior does not: flat-in-$\theta$ and flat-in-$\psi$ give genuinely different posteriors, §07.3.)

```python
fig, ax = plt.subplots()
ax.plot(th, stats.beta(0.5, 0.5).pdf(th), "C0", lw=1.6, label="Jeffreys prior = Beta(½,½)")
ax.plot(th, post_A, "C1", lw=3.0, label="posterior via θ")
ax.plot(th, post_B, "k--", lw=1.4, label="posterior via log-odds (coincides)")
ax.axvline(0.7, ls=":", color="grey", lw=1, label="MLE = 0.7")
ax.set_ylim(0, 4); ax.set_xlabel(r"$\theta$"); ax.set_ylabel("density")
ax.set_title("Jeffreys prior: same posterior in any parameterization")
ax.legend(fontsize=9)
save(fig, "jeffreys-two-ways")
```

![The Beta(½,½) prior rising at both ends; the posterior after 7-of-10 as a single bump near 0.7, with the log-odds-route posterior lying exactly on top of it as a dashed line.](figures/07-priors/jeffreys-two-ways.png)

**Scope (not a free lunch).** Jeffreys is clean for a single parameter. In the multiparameter case the recipe $\pi_J\propto\sqrt{\det \mathcal I(\theta)}$ is *often not recommended as-is* — Jeffreys himself declined it for $N(\mu,\sigma^2)$, preferring the independence prior $\pi(\mu,\sigma^2)\propto 1/\sigma^2$ (which treats location and scale separately) because the joint rule couples them in ways that distort marginal inference. The modern generalization is Bernardo's **reference priors**, which maximize the expected information the data add over the prior (an asymptotic mutual-information argument) and reduce to Jeffreys in one dimension but handle nuisance parameters more sensibly (BDA3 ch. 2, Bernardo by concept). Treat "Jeffreys = $\sqrt{\det\mathcal I}$" as a one-parameter tool, not a universal default.

## 07.5 Improper priors: when the answer diverges

A prior need not integrate to 1 to yield a proper posterior — $\pi(\theta)\propto 1$ on $(0,1)$ is fine because the likelihood makes the product integrable. The danger is that *nothing warns you* when it isn't.

**Setup.** The **Haldane prior** $\text{Beta}(0,0)\propto\theta^{-1}(1-\theta)^{-1}$ is the flat-log-odds prior of §07.3. With $s$ successes and $f$ failures the posterior kernel is $\theta^{s-1}(1-\theta)^{f-1}$ — the $\text{Beta}(s,f)$ shape, and on ordinary data it behaves unremarkably. Now the boundary case: **all $n=10$ trials succeed** ($s=10$, $f=0$), leaving the kernel $\theta^{n-1}(1-\theta)^{-1}$.

**Predict.** Does a posterior distribution even exist here — yes or no? And if yes, where is its mass and roughly what is its mean?

**Reason.** The naive answer: "of course — ten straight successes are maximally informative, so the posterior piles up near $\theta=1$ with mean just below 1." The intuition at work: *data this strong can only sharpen the answer, never destroy it.*

**Run.** Existence is a question about the normalizing constant $\int_0^1 \theta^{n-1}(1-\theta)^{-1}d\theta$: track it on $[0, 1-\epsilon]$ as $\epsilon\to 0$, and plot the kernel.

```python
# Haldane Beta(0,0) with all-successes data: does the posterior kernel normalize?
from scipy.integrate import quad
n = 10                                         # n successes, 0 failures
kernel = lambda t: t**(n - 1) / (1 - t)        # unnormalized posterior kernel
for eps in (1e-2, 1e-4, 1e-6):
    val, _ = quad(kernel, 0, 1 - eps)          # integrate up to 1 - eps
    print(f"integral of posterior kernel on [0, 1-{eps:g}] = {val:.4f}")
print("as eps -> 0 the integral grows like -log(eps): the posterior does NOT normalize")

fig, ax = plt.subplots()
tt = np.linspace(0.01, 0.999, 500)
ax.plot(tt, tt**(n - 1) / (1 - tt), "C3", lw=2)
ax.set_yscale("log")
ax.set_xlabel(r"$\theta$"); ax.set_ylabel(r"posterior kernel $\theta^{n-1}(1-\theta)^{-1}$ (log)")
ax.set_title("Haldane + all-successes: the posterior mass runs off to θ=1 and never returns")
save(fig, "haldane-divergence")
```

![A curve on a log-y axis that rises without bound as θ approaches 1, showing the non-integrable spike.](figures/07-priors/haldane-divergence.png)

**Reconcile.** No — there is no posterior. The normalizing integral over $[0,\,1-\epsilon]$ is `1.8644` at $\epsilon=10^{-2}$, `6.3823` at $\epsilon=10^{-4}$, `10.9866` at $\epsilon=10^{-6}$ — climbing by about $\ln(100)\approx4.6$ every time $\epsilon$ shrinks two decades, exactly the signature of a logarithmic divergence $\int^{1}\!\frac{d\theta}{1-\theta}=\infty$. The naive intuition fails because the likelihood $\theta^{10}$ *cannot* tame the prior's $(1-\theta)^{-1}$ spike at 1: it equals 1 there instead of vanishing. The general rule falls out: the Haldane posterior $\text{Beta}(s,f)$ is proper *iff* $s>0$ **and** $f>0$. And notice the trap's shape — `Beta(0,0)` is perfectly safe on ordinary data and detonates only on the boundary dataset, the kind of input that shows up precisely when an event is rare and every trial so far has gone one way.

**The hierarchical variance trap.** The same failure hides in a place practitioners actually visit: the scale parameter of a hierarchical model. The scale-invariant improper prior $\pi(\sigma)\propto 1/\sigma$ (equivalently $\pi(\sigma^2)\propto 1/\sigma^2$) is a standard "noninformative" choice for a variance, and it is safe for the residual variance of a single regression. But placed on a *group-level* standard deviation — the between-group spread $\tau$ in a hierarchical model — it can produce an improper posterior or pin $\tau$ at 0, because with few groups the likelihood does not constrain $\tau$ away from zero and the $1/\sigma$ spike at the origin wins. The booklet's MCMC-difficulties chapter flags exactly this: "the prior $\pi(\sigma)\propto\frac1\sigma$ is no good," and "priors like $\pi(\sigma^2)\propto\frac{1}{\sigma^2}$ create difficulties deep down in a hierarchical model" (booklet ch. 15, citing Gelman, *Bayesian Analysis* 2006). The recommended fix is a weakly-informative proper prior on $\tau$ — a half-Cauchy or half-Normal — which module 16 uses on the eight-schools model. **Rule of thumb:** an improper prior is safe only when you can prove the posterior integrates; on a variance component deep in a hierarchy, that proof usually fails, so use a proper weakly-informative prior.

## 07.6 Washout and its exception: the parameter data can't touch

Section 07.1 promised that prior influence decays like $1/n$. That promise has a precise precondition — the parameter must be **identified**, meaning the likelihood actually varies with it. When it doesn't, no amount of data washes the prior out.

**Setup.** Observe $y_i = \theta_1 + \theta_2 + \varepsilon_i$ with $\varepsilon_i\sim N(0,1)$. The data see only the *sum* $\theta_1+\theta_2$; the difference $\theta_1-\theta_2$ leaves no fingerprint on the likelihood. Put independent priors $\theta_1,\theta_2\sim N(0,10)$ (so prior SD $=\sqrt{10}\approx 3.16$) and collect $n=10{,}000$ observations.

**Predict.** After ten thousand data points, what is the posterior SD of $\theta_1$? Naive answer: huge $n$, so it collapses toward 0 like any well-behaved parameter. Commit to a number before running.

**Reason.** "More data ⇒ tighter posterior" is true for identified parameters and is exactly the intuition this demo breaks.

**Run.** The model is linear-Gaussian, so the posterior is Gaussian with precision $\Lambda_n = \tfrac{1}{\sigma^2}X^\top X + \Lambda_0$, where each row of $X$ is $[1,1]$.

```python
# y_i = theta1 + theta2 + noise. Only the SUM is identified; the difference is not.
tau2, sigma2 = 10.0, 1.0                        # prior variance, noise variance
theta_true = np.array([2.0, -1.0])              # sum = 1.0 is knowable; split is not
for n in (10, 10_000):
    X = np.ones((n, 2))                          # each observation sees theta1 + theta2
    y = X @ theta_true + rng.normal(0, np.sqrt(sigma2), n)
    Lambda0 = np.eye(2) / tau2                   # prior precision
    Lambda_n = X.T @ X / sigma2 + Lambda0        # posterior precision
    Sigma_n = np.linalg.inv(Lambda_n)
    mu_n = Sigma_n @ (X.T @ y / sigma2)
    sd_theta1 = np.sqrt(Sigma_n[0, 0])
    sd_sum = np.sqrt(np.array([1, 1]) @ Sigma_n @ np.array([1, 1]))
    print(f"n={n:>6}: posterior sd(theta1)={sd_theta1:.4f}   sd(theta1+theta2)={sd_sum:.4f}")
print(f"prior sd(theta1) = {np.sqrt(tau2):.4f}")

# The ridge picture behind the numbers: sample the n=10,000 posterior.
fig, ax = plt.subplots()
n = 10_000
X = np.ones((n, 2)); y = X @ theta_true + rng.normal(0, 1, n)
Sigma_n = np.linalg.inv(X.T @ X / sigma2 + np.eye(2) / tau2)
mu_n = Sigma_n @ (X.T @ y / sigma2)
draws = rng.multivariate_normal(mu_n, Sigma_n, 4000)   # posterior samples
ax.scatter(draws[:, 0], draws[:, 1], s=4, alpha=0.25, color="C1")
lo, hi = -6, 8
ax.plot([lo, hi], [theta_true.sum() - lo, theta_true.sum() - hi], "k--", lw=1,
        label=r"identified ridge $\theta_1+\theta_2=1$")
ax.scatter([theta_true[0]], [theta_true[1]], color="k", zorder=5, label="truth")
ax.set_xlim(lo, hi); ax.set_ylim(-8, 6)
ax.set_xlabel(r"$\theta_1$"); ax.set_ylabel(r"$\theta_2$")
ax.set_title("Nonidentifiability: data pin the sum, never the split (n=10,000)")
ax.legend(fontsize=9)
save(fig, "washout-exception")
```

![A long, thin, diagonal cloud of posterior samples lying along the line θ1+θ2=1, tightly constrained across the line but sprawling along it.](figures/07-priors/washout-exception.png)

At $n=10{,}000$ the posterior SD of the *sum* is `0.0100` — it has concentrated exactly as $1/\sqrt n$ intuition demands. But the posterior SD of $\theta_1$ alone is `2.2361`, essentially unchanged from its value of `2.2416` at $n=10$ — a thousand-fold increase in data moved it by about five thousandths. (It sits below the prior SD `3.1623` only because conditioning on the sum removes variance along *one* direction, a one-time constant-factor drop; the $1/\sqrt n$ machinery never engages on $\theta_1$ at all.)

**Reconcile.** The data pin down $\theta_1+\theta_2$ to a razor's edge but say *nothing* about where along the line $\theta_1+\theta_2=\text{const}$ the truth sits. The posterior — the figure's long thin ridge — has $\theta_1$'s marginal width set by the prior's spread along that ridge, and $1/\sqrt n$ never touches it. Whatever you believed about $\theta_1$ *a priori* is essentially what you still believe — forever.

**Faces of nonidentifiability.** This is one of three flavors the course will keep meeting. (i) *Structural*, as here: two parameters enter only through a function of them — the prior on the unseen direction is load-bearing forever. (ii) *Symmetry*: a likelihood invariant under relabeling, e.g. mixture components (module 19's label-switching — the posterior is genuinely multimodal by construction). (iii) *Weak likelihood*: technically identified but so flat that at finite $n$ the prior dominates anyway (the small-$n$ end of §07.1). The deep-learning reader has met the extreme case without the name: an overparameterized network has vastly more weights than the data can identify, so the "prior" — weight decay, initialization scale, the implicit bias of SGD — is what selects among the flat directions (module 25). Nonidentifiability is not a pathology to avoid; it is a fact to model, and the prior is how you model it.

## 07.7 Bridge — regularization is an implicit prior

Every penalized estimator you have trained is a posterior mode in disguise, because **a penalty is the negative log of a prior density**. Ridge regression minimizes $\|y-X\beta\|^2 + \lambda\|\beta\|^2$; the second term is $-2\sigma^2\log$ of a Gaussian prior $\beta\sim N(0,\,\sigma^2/\lambda\,I)$, so the ridge solution is the MAP estimate — and the posterior *mean* — under that prior (module 00 verified the numbers to machine precision; module 06 framed MAP = penalized MLE). Lasso's $\ell_1$ penalty is a Laplace prior; dropout and early stopping are regularizers with looser, **Heuristic**-level Bayesian readings (cashed out in module 25).

```python
# The correspondence, stated as an equation you can read off: lambda <-> prior variance.
sigma2_noise, lam = 1.0, 5.0
prior_var = sigma2_noise / lam                 # ridge penalty lambda <-> N(0, sigma^2/lambda)
print(f"ridge penalty lambda={lam} with noise var {sigma2_noise} "
      f"== Gaussian prior N(0, {prior_var:.4f})")
print("stronger penalty  <->  tighter prior  <->  more shrinkage toward 0")
```

Penalty $\lambda=5$ at noise variance 1 is precisely a $N(0, 0.2000)$ prior on the weights: a large $\lambda$ is a *confident* prior that the weights are small. Naming this changes what you do. Instead of grid-searching $\lambda$ as a magic knob, you are choosing a prior variance — an interpretable claim about effect sizes you can set from domain knowledge, or estimate from the data as a hyperparameter (empirical Bayes, modules 14 and 18). And the framing is *non-polemical*: calling weight decay "an implicit Gaussian prior" is not a claim that deep learning is secretly Bayesian, only that the regularization dial and the prior-variance dial are the same dial. The practical upshot is **weakly-informative defaults as stability engineering**: a mildly-shrinking proper prior (a $N(0,\text{a-few})$ on standardized coefficients, a half-Normal on a scale) rarely changes a well-identified answer — §07.1 — but it rules out the absurd, keeps samplers away from divergent regions (§07.5), and costs nothing when the data are plentiful. That is the modern default: not "let the data speak" via improper flatness, but a gentle proper prior that speaks only when the data are silent.

## Pitfalls

- **"Flat = noninformative."** Flatness is not coordinate-free (§07.3); a uniform prior on $\theta$ is a logistic prior on the log-odds and the Haldane prior on the log-odds. Ask *flat in what parameterization, and does that parameterization matter?* If you want invariance, use Jeffreys or a reference prior — but only after reading the multiparameter scope note.
- **Vague on the wrong scale.** A "huge-variance" Normal prior on a bounded parameter (a probability, a variance) puts most of its mass on impossible values (§07.2: `0.9601` outside $[0,1]$). Always run a prior predictive check; the fake data expose the mismatch before real data are spent.
- **Assuming the prior always washes out.** It washes out at rate $1/n$ *only for identified parameters* (§07.6). For structurally, symmetrically, or weakly nonidentified parameters the prior is permanent; more data will not save you, and pretending otherwise produces overconfident nonsense on the unidentified directions.
- **Improper priors without a propriety check.** An improper prior can give an improper posterior with no error message (§07.5). Safe on ordinary data, `Beta(0,0)` diverges on all-successes; $\pi(\sigma)\propto1/\sigma$ diverges on hierarchical variance components. Prove integrability or use a proper weakly-informative prior.
- **Treating the prior as the only modeling assumption up for audit.** The likelihood is chosen too. "Sensitivity to the prior" and "sensitivity to the likelihood family" are the same kind of question; a robustness analysis that varies only the prior is half an analysis.

## Exercises

**Exercise 07.1 — Does the prior matter for a rare event?**
*Setup:* You test a new treatment on $n=15$ patients and observe **0** adverse events. Compare three priors for the adverse-event rate $\theta$: uniform `Beta(1,1)`, Jeffreys `Beta(0.5,0.5)`, and Haldane `Beta(0,0)`.
*Predict:* The sample rate is 0. Which posterior means are close, and does any of them do something degenerate?
*Reason:* "Zero events means the rate is basically zero, and the prior barely matters at $n=15$" — the washout intuition from §07.1, applied at a boundary where it is shaky.
*Run:*
```python
for name, (a, b) in [("uniform", (1, 1)), ("Jeffreys", (0.5, 0.5)), ("Haldane", (0, 0))]:
    an, bn = a + 0, b + 15                      # 0 successes, 15 failures
    if an > 0 and bn > 0:
        print(f"{name:9s}: Beta({an},{bn}) mean={an/(an+bn):.4f} "
              f"P(theta>0.1)={stats.beta(an, bn).sf(0.1):.4f}")
    else:
        print(f"{name:9s}: Beta({an},{bn}) is IMPROPER (posterior mass collapses to 0)")
```
<details><summary>Reconcile</summary>

Uniform gives `Beta(1,16)`, mean `0.0588`; Jeffreys gives `Beta(0.5,15.5)`, mean `0.0312`; Haldane gives `Beta(0,15)`, which is **improper** — with zero successes the $\theta^{-1}$ spike at 0 is not tamed, so the "posterior" is a point mass at 0 claiming the event is *impossible* after 15 patients. At a boundary dataset the prior matters a lot: the three "reasonable" defaults disagree by nearly $2\times$ on the mean and one of them fails outright. The lesson: washout is a large-$n$, interior-data statement; rare-event and boundary problems are exactly where prior choice is decisive, and where a proper weakly-informative prior (uniform or Jeffreys, never Haldane) earns its keep. This is why "rule of three" style analyses of zero-event data are genuinely prior-sensitive.
</details>

**Exercise 07.2 — What prior does your weight decay encode?**  *(ML bridge)*
*Setup:* You train a linear model with L2 weight decay, minimizing $\|y-X\beta\|^2 + \lambda\|\beta\|^2$, and your data noise has variance $\sigma^2=4$. You try $\lambda\in\{0.1, 1, 100\}$.
*Predict:* Rank the three settings by how strong a claim they make about the weights. Which $\lambda$ corresponds to a prior standard deviation on each weight of about 0.2?
*Reason:* "$\lambda$ is just a regularization strength I tune by CV" — the reflex that treats the penalty as a dimensionless knob rather than a prior.
*Run:*
```python
sigma2 = 4.0
for lam in (0.1, 1.0, 100.0):
    prior_sd = np.sqrt(sigma2 / lam)           # weight decay lambda <-> N(0, sigma^2/lambda)
    print(f"lambda={lam:6.1f}  <->  prior N(0, {sigma2/lam:.4f})  =>  prior sd = {prior_sd:.4f}")
```
<details><summary>Reconcile</summary>

$\lambda=0.1\to$ prior SD `6.3246` (barely any constraint — weights could be $\pm$several), $\lambda=1\to$ SD `2.0000`, $\lambda=100\to$ SD `0.2000` (a *confident* claim that every weight is within $\approx0.4$ of zero). Bigger $\lambda$ is a tighter prior, and the one that encodes "weights $\approx0.2$-scale" is $\lambda=100$. Cross-validating $\lambda$ is estimating your prior variance from the data — which is empirical Bayes (modules 14, 18), not a departure from the Bayesian frame but a special case of it. Once you see the penalty as $-\log$ prior, "how much regularization?" becomes the answerable question "how big do I believe the weights are?"
</details>

**Exercise 07.3 — How much does the coordinate choice cost?**  *(§07.3 cashed out; surprising)*
*Setup:* §07.3 showed that "flat in $\theta$", Jeffreys, and "flat in log-odds" (the Haldane limit) are three different priors. Here is where that difference stops being aesthetic: you observe **2 successes in 2 trials** — the smallest, most boundary-flavored dataset imaginable — and each analyst reports the posterior mean of $\theta$.
*Predict:* You already know from §07.3 that the priors differ in shape. Commit to magnitudes: do the three posterior means agree to within ~0.02 (shape differences are cosmetic once data arrive), or spread by more than 0.2? And does anything worse than disagreement happen?
*Reason:* "Two coin flips can't distinguish nearly-flat priors, so the answers will basically coincide" — §07.1's washout intuition, misapplied at $n=2$ on boundary data.
*Run:*
```python
# You: flat on theta. Jeffreys: Beta(1/2,1/2). Colleague: flat on log-odds = Haldane Beta(0,0).
you = stats.beta(1 + 2, 1 + 0)                  # Beta(1,1) + 2 successes, 0 failures
jeff = stats.beta(0.5 + 2, 0.5 + 0)             # Beta(1/2,1/2) + 2 successes, 0 failures
print(f"flat-on-theta   posterior mean = {you.mean():.4f}")
print(f"Jeffreys        posterior mean = {jeff.mean():.4f}")
print(f"flat-log-odds: strict Haldane posterior Beta(2,0) is IMPROPER (all successes, "
      f"section 07.5); Beta(eps,eps)-prior posterior means -> 1.0000 as eps -> 0")
```
<details><summary>Reconcile</summary>

Flat-on-$\theta$ gives mean `0.7500` (module 05's rule-of-succession answer — two data points cannot justify certainty). Jeffreys gives `0.8333`, pulled higher because `Beta(½,½)` leans toward the extremes. And the strict flat-log-odds prior does something worse than disagree: with all-successes data its posterior $\text{Beta}(2,0)$ is **improper** (§07.5's rule — proper iff $s>0$ *and* $f>0$); the limit of $\text{Beta}(\epsilon,\epsilon)$-prior posterior means as $\epsilon\to0$ is the degenerate `1.0000`, the plug-in MLE asserting the next flip is certainly a success. So the spread is `0.75` to effectively `1.0` — an 0.25 gap, ten times the "cosmetic" guess — and one of the three "noninformative" defaults has no answer at all. The coordinate choice §07.3 exposed as a shape difference becomes, at small $n$ on boundary data, the *entire* answer. The honest move: state the prior, and at small $n$ report the sensitivity fan.
</details>

**Exercise 07.4 — Can a prior rescue an unidentified parameter?**  *(connects to §07.6)*
*Setup:* In the $y=\theta_1+\theta_2$ model of §07.6, you cannot identify $\theta_1$ from data. Suppose you have side information: a *proper* prior $\theta_1\sim N(2, 0.5^2)$ (SD 0.5), while $\theta_2\sim N(0,10)$ stays vague. Collect $n=10{,}000$ observations.
*Predict:* Two commitments. Will the posterior SD of $\theta_1$ shrink toward 0 as $n$ grows, or stay near its prior SD of 0.5? And $\theta_2$'s posterior SD — near its vague prior width $\sqrt{10}\approx3.16$, or tight?
*Reason:* "The data can't see either parameter individually, so each stays at its own prior width — $\theta_1$ at 0.5, $\theta_2$ at 3.16." Half of this is wrong.
*Run:*
```python
tau1_2, tau2_2, sigma2 = 0.5**2, 10.0, 1.0
n = 10_000
X = np.ones((n, 2)); y = X @ np.array([2.0, -1.0]) + rng.normal(0, 1, n)
Lambda0 = np.diag([1/tau1_2, 1/tau2_2])
Sigma_n = np.linalg.inv(X.T @ X / sigma2 + Lambda0)
print(f"posterior sd(theta1) = {np.sqrt(Sigma_n[0,0]):.4f}  (prior sd 0.5000)")
print(f"posterior sd(theta2) = {np.sqrt(Sigma_n[1,1]):.4f}")
```
<details><summary>Reconcile</summary>

The posterior SD of $\theta_1$ is `0.4939` — essentially the prior SD 0.5, unmoved by 10,000 observations. But $\theta_2$'s posterior SD is *also* `0.4940`, even though its prior was vague: once the data nail the sum $\theta_1+\theta_2$ tightly and the prior nails $\theta_1$ tightly, $\theta_2=(\theta_1+\theta_2)-\theta_1$ inherits both constraints and becomes tightly determined too. So a proper prior on *one* unidentified direction propagates through the identified sum to pin the other — the prior does real inferential work that no amount of data could do alone. This is the constructive side of §07.6: for nonidentified parameters the prior is not a nuisance to wash out but the *only* source of information, and choosing it well is the whole game (hierarchical models, module 16; causal identification, module 24).
</details>

## Takeaways

- The **prior is part of the model**, with the same epistemic status as the likelihood; both are chosen assumptions, and both should be audited (prior predictive checks, sensitivity fans, robustness to the family).
- **Whether the prior matters is computable.** For identified parameters its influence decays like $1/n$ — negligible at large $n$, decisive at small $n$ or on boundary data. Draw the sensitivity fan instead of arguing.
- **"Noninformative" is coordinate-dependent.** Flat in $\theta$ is curved in $\log\frac{\theta}{1-\theta}$. If you want invariance to reparameterization, use the **Jeffreys prior** $\pi_J\propto\sqrt{\mathcal I(\theta)}$ — `Beta(½,½)` for a Bernoulli rate — verified to give the identical posterior through any parameterization; but treat $\sqrt{\det\mathcal I}$ as a one-parameter tool and reach for reference priors in higher dimensions.
- **Improper priors can silently break.** `Beta(0,0)` on all-successes data and $\pi(\sigma)\propto1/\sigma$ on a hierarchical variance both give non-normalizable posteriors with no warning. Prove propriety or use a proper weakly-informative prior.
- **Prior influence never vanishes for unidentified parameters** (structural, symmetric, or weak-likelihood nonidentifiability). There the prior is not noise to average away but the sole carrier of information — and a proper prior on one direction can pin down another through the identified combinations.
- **Regularization is an implicit prior:** ridge = Gaussian, lasso = Laplace; the penalty is $-\log$ prior and $\lambda$ *is* a prior variance. Weakly-informative proper defaults are stability engineering — silent when the data speak, protective when they don't.

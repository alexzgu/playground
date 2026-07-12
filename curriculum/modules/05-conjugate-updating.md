# 05. Conjugate Updating End-to-End  [SIGNATURE S2]

> **Spine.** Every conjugate posterior reads as *prior pseudo-data + real data*, and its mean is a precision-weighted average of the prior mean and the data's estimate — the master shrinkage formula that reappears as ridge, Kalman gain, and partial pooling.
> **Which line?** Lines 2 and 3, done in closed form. When the likelihood and prior are a matched (conjugate) pair, conditioning (line 2) and the predictive integral (line 3) both have pencil-and-paper answers — no sampling required.
> **Promise.** After this module you can update Beta/Normal/Gamma/Dirichlet models by inspection, read any posterior as a precision-weighted blend, compute the *posterior predictive* (never the plug-in) for each, drive an A/B test to a shipping decision, and condition a multivariate Gaussian with the block formulas that power Kalman filters and GPs.
> **Prereqs.** Modules 00 (four lines), 02 (conditioning), 04 (likelihood, exponential families, the `nig_post` helper).
> **Runtime.** ~6 s.
> **Sources.** Booklet ch. 3–5, 8; C-B §7.2 (conjugate families), §3.4 (exponential families).

The four lines (module 00): **a model is a joint $p(\text{unknowns},\text{knowns})$; inference is conditioning; prediction is marginalization; a decision minimizes posterior expected loss.** Conditioning reads $p(\theta\mid y)\propto p(y\mid\theta)\,p(\theta)$. In general that normalizing integral is intractable and you reach for Monte Carlo (module 09 onward). But for a special, load-bearing set of prior/likelihood pairs the posterior stays in the *same family as the prior* — you update by adjusting a few numbers. Those are the **conjugate** pairs, and they are worth mastering not because real problems are always conjugate (they are not) but because every hard-won intuition in the course — shrinkage, pseudo-counts, the predictive-vs-plug-in gap, precision-weighting — is visible here in closed form, then reused everywhere as an approximation or a building block.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "05-conjugate-updating"          # this module's figure dir
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

## 05.1 Two data points, and what the MLE leaves out  [SIGNATURE S2]

Start where the intuition breaks.

**Setup.** A newly launched ad shows twice and converts *both* times: 2 conversions in 2 impressions. Put a $\mathrm{Beta}(1,1)$ (uniform) prior on the conversion rate $\theta$.

**Predict.** The maximum-likelihood estimate is $\hat\theta = 2/2 = 1.0$. Before running anything, commit to two numbers: (a) the posterior *mean* of $\theta$; (b) the posterior-*predictive* probability that the next impression converts. Most guts say $\approx 1.0$ for (b) — the data said 100%.

**Reason.** If you wrote $\approx 1.0$, you are trusting the point estimate and discarding your uncertainty about $\theta$.

**Run.**

```python
# Beta(1,1) prior + 2 successes, 0 failures  ->  Beta(3,1) posterior.
a0, b0, s, f = 1, 1, 2, 0
a_n, b_n = a0 + s, b0 + f
post_mean = a_n / (a_n + b_n)
pred_next = a_n / (a_n + b_n)          # Bernoulli posterior predictive = E[theta]
print(f"MLE           = {s/(s+f):.1f}")
print(f"posterior      = Beta({a_n},{b_n})")
print(f"posterior mean = {post_mean:.4f}")
print(f"P(next converts) = {pred_next:.4f}")

grid = np.linspace(1e-3, 1 - 1e-3, 400)
fig, ax = plt.subplots()
ax.plot(grid, stats.beta(a0, b0).pdf(grid), color="C0", label="prior Beta(1,1)")
ax.plot(grid, stats.beta(a_n, b_n).pdf(grid), color="C1", lw=2, label="posterior Beta(3,1)")
ax.axvline(1.0, ls="--", color="k", lw=1, label="MLE = 1.0")
ax.axvline(post_mean, ls=":", color="C1", lw=1.5, label="posterior mean = 0.75")
ax.set_xlabel(r"$\theta$ (conversion rate)"); ax.set_ylabel("density")
ax.set_title("Two data points don't justify certainty: the MLE says 1.0, the posterior says 0.75")
ax.legend()
save(fig, "s2-overconfident-mle")
```

![Flat Beta(1,1) prior; a Beta(3,1) posterior rising toward 1 but with substantial mass below it; the MLE marked at 1.0 and the posterior mean at 0.75.](figures/05-conjugate-updating/s2-overconfident-mle.png)

**Reconcile.** The posterior is $\mathrm{Beta}(3,1)$, mean $3/4 = $ `0.7500`, and the posterior-predictive probability that the next impression converts is $\mathbb{E}[\theta] = $ `0.7500` — not `1.0`. The MLE's "1.0" claimed *certainty from two data points*: an artifact of plugging in a point estimate and throwing away parameter uncertainty. Read the update as counts: $\mathrm{Beta}(1{+}2,\,1{+}0)$ means **3 effective successes and 1 effective failure**, so $3/4$. The uniform prior was not "no information" — it was worth exactly one pseudo-success and one pseudo-failure, and with only two real data points those pseudo-observations still carry a quarter of the weight.

That sentence — *posterior = prior pseudo-data + real data* — is the whole module. You will meet this correction again as Laplace's rule of succession (module 01's 6/7 = 0.8571), as add-$\alpha$ smoothing in a language model (§05.5), and as the flaring predictive interval of regression (module 14's trumpet). Plug-in prediction is *most* overconfident exactly when you have *least* data.

## 05.2 Why closed forms exist: conjugacy is exponential-family closure

The $\mathrm{Beta}\to\mathrm{Beta}$ update was not luck. Recall the exponential-family skeleton from module 04: in natural form a one-observation likelihood is $p(x\mid\eta) = h(x)\exp\!\big(\eta^\top T(x) - A(\eta)\big)$, and for $n$ iid draws the sufficient statistic $\sum_i T(x_i)$ carries everything. Write a prior in the matching form, indexed by two hyper-parameters $(\tau_0,\ n_0)$ — a pseudo-sufficient-statistic and a pseudo-sample-size:
$$p(\eta\mid \tau_0, n_0) \;\propto\; \exp\!\big(\eta^\top \tau_0 - n_0\,A(\eta)\big).$$
Multiply by the likelihood of data with sufficient statistic $S=\sum_i T(x_i)$ and count $n$:
$$p(\eta\mid x) \;\propto\; \exp\!\Big(\eta^\top (\tau_0 + S) - (n_0+n)\,A(\eta)\Big).$$
Same functional form, updated hyper-parameters $\tau_0 \mapsto \tau_0 + S$, $n_0 \mapsto n_0 + n$. **The posterior is in the prior's family** — that is the definition of a **conjugate prior** (C-B §7.2), and the reason closed-form Bayes exists at all. Conjugate updating is nothing but *adding your data's sufficient statistic to the prior's pseudo-statistic, and your sample size to the prior's pseudo-sample-size.* Every pair below is one instance of this single identity.

Build the small library once — later modules import these patterns by copy, so the names and signatures are deliberately plain.

```python
# --- the conjugate library: five updates, each = "add data's sufficient stat" ---
def beta_binomial_update(a, b, s, f):
    """Beta(a,b) prior + (s successes, f failures) -> Beta(a+s, b+f)."""
    return a + s, b + f

def normal_known_var_update(m0, tau2, sigma2, data):
    """N(m0, tau2) prior on the mean, known obs variance sigma2 -> posterior (mean, var)."""
    n = len(data)
    prec_post = 1.0/tau2 + n/sigma2                      # precisions add
    m_post = (m0/tau2 + data.sum()/sigma2) / prec_post   # precision-weighted mean
    return m_post, 1.0/prec_post

def gamma_poisson_update(a0, b0, y, n_units):
    """Gamma(a0,b0) [b0=rate] prior + counts y over n_units exposures -> Gamma(a0+sum y, b0+n_units)."""
    return a0 + np.sum(y), b0 + n_units

def nig_post(data, mu0=0.0, k0=1.0, a0=1.0, b0=1.0):
    """Normal-Inverse-Gamma update (mean & variance unknown). Copied from module 04."""
    n = len(data); xbar = data.mean(); S = ((data - xbar)**2).sum()
    kn = k0 + n
    mn = (k0*mu0 + n*xbar) / kn
    an = a0 + n/2
    bn = b0 + 0.5*S + (k0*n*(xbar - mu0)**2) / (2*kn)
    return kn, mn, an, bn

def dirichlet_mult_update(alpha, counts):
    """Dirichlet(alpha) prior + category counts -> Dirichlet(alpha + counts)."""
    return np.asarray(alpha, float) + np.asarray(counts, float)

print("conjugate library ready:", 
      [f.__name__ for f in (beta_binomial_update, normal_known_var_update,
                            gamma_poisson_update, nig_post, dirichlet_mult_update)])
```

## 05.3 Beta-Binomial in full — the master shrinkage formula

Bernoulli$(\theta)$ has natural parameter $\eta=\log\frac{\theta}{1-\theta}$ and $T(x)=x$; the conjugate prior in $\theta$-coordinates is $\mathrm{Beta}(a,b)\propto \theta^{a-1}(1-\theta)^{b-1}$. With $s$ successes and $f=n-s$ failures the likelihood is $\theta^{s}(1-\theta)^{f}$, so
$$p(\theta\mid y) \propto \theta^{a-1}(1-\theta)^{b-1}\cdot\theta^{s}(1-\theta)^{f} = \theta^{(a+s)-1}(1-\theta)^{(b+f)-1} = \mathrm{Beta}(a+s,\ b+f).$$
No integral — just add successes to $a$ and failures to $b$. Now read the posterior *mean*, and watch the master formula fall out. With $\kappa = a+b$ (the prior's pseudo-sample-size) and prior mean $m_0 = a/\kappa$:
$$\mathbb{E}[\theta\mid y] = \frac{a+s}{a+b+n} = \underbrace{\frac{\kappa}{\kappa+n}}_{w_{\text{prior}}}\,m_0 \;+\; \underbrace{\frac{n}{\kappa+n}}_{w_{\text{data}}}\,\hat\theta,\qquad \hat\theta = \frac{s}{n}.$$

**The posterior mean is a convex combination of the prior mean and the MLE, weighted by pseudo-counts vs real counts.** The prior is literally *worth $\kappa = a+b$ observations*. When $n \ll \kappa$ the answer sits near the prior; when $n \gg \kappa$ it collapses onto the MLE. Slide $n$ and watch:

```python
# Prior Beta(2,2): mean 0.5, worth kappa = 4 pseudo-trials. True theta = 0.8.
rng_bb = np.random.default_rng(5)
a0, b0 = 2.0, 2.0
kappa = a0 + b0
theta_true = 0.8
stream = rng_bb.binomial(1, theta_true, size=500)   # one long stream; take prefixes

ns = [0, 1, 2, 5, 10, 50, 200, 500]
means, mles = [], []
for n in ns:
    s = int(stream[:n].sum()); f = n - s
    an, bn = beta_binomial_update(a0, b0, s, f)
    pm = an / (an + bn)
    means.append(pm); mles.append(s/n if n else np.nan)
    if n in (0, 2, 10, 50, 500):
        tag = f"{s/n:.3f}" if n else "  -  "
        print(f"n={n:>3}: MLE={tag}  posterior mean={pm:.4f}  w_prior={kappa/(kappa+n):.3f}")
print(f"prior is worth kappa = a+b = {kappa:.1f} pseudo-trials")

fig, ax = plt.subplots()
nn = np.array(ns, float); nn[0] = 0.6                 # place n=0 on log axis
ax.axhline(0.5, ls=":", color="C0", label="prior mean 0.5")
ax.axhline(0.8, ls="--", color="k", label="truth 0.8")
ax.plot(nn, means, "o-", color="C1", label="posterior mean")
ax.plot(nn[1:], mles[1:], "s--", color="C3", alpha=0.7, label="MLE  s/n")
ax.set_xscale("log"); ax.set_xlabel("n (observations)"); ax.set_ylabel(r"estimate of $\theta$")
ax.set_title("Posterior mean slides from prior (0.5) to MLE as data outweigh the pseudo-counts")
ax.legend()
save(fig, "shrinkage-slide")
```

![Posterior-mean curve starting at the prior mean 0.5 at n=0, pulled down by early zeros, then climbing to track the MLE and converging on the truth 0.8 by n=500; the MLE is erratic at small n.](figures/05-conjugate-updating/shrinkage-slide.png)

The first two flips happened to be failures, so at $n=2$ the MLE is `0.000` while the posterior mean is `0.3333` — the mirror image of §05.1's 2-of-2. By $n=10$ the posterior mean is `0.6429` (MLE 0.7), and by $n=500$ it is `0.7956`, essentially the MLE, essentially the truth. The prior's weight $w_{\text{prior}} = \kappa/(\kappa+n)$ falls from 1 to `0.008`. This *precision-weighted average* is the single most reused formula in the course; §05.4 shows it is exactly the Kalman gain and exactly partial pooling.

## 05.4 Normal-Normal (known variance) in full

Now a continuous unknown. The mean $\theta$ of a Normal is unknown, the variance $\sigma^2$ is known, the prior is $\theta\sim N(m_0,\tau^2)$, and we see $y_1,\dots,y_n\sim N(\theta,\sigma^2)$. Work in **precision** $= 1/\text{variance}$, because that is what adds. The log-posterior is a sum of two quadratics in $\theta$; completing the square (expand, collect the $\theta^2$ and $\theta$ terms, and read off the Gaussian) gives
$$\frac{1}{\tau_n^2} = \underbrace{\frac{1}{\tau^2}}_{\text{prior prec}} + \underbrace{\frac{n}{\sigma^2}}_{\text{data prec}},\qquad m_n = \tau_n^2\left(\frac{m_0}{\tau^2} + \frac{n\,\bar y}{\sigma^2}\right) = \frac{\tfrac{1}{\tau^2}\,m_0 + \tfrac{n}{\sigma^2}\,\bar y}{\tfrac{1}{\tau^2} + \tfrac{n}{\sigma^2}}.$$
**Posterior precision = prior precision + data precision. Posterior mean = precision-weighted average of prior mean and the MLE $\bar y$.** Same master formula as Beta-Binomial, now with $\kappa_0 = \sigma^2/\tau^2$ playing the role of the prior's pseudo-sample-size: the prior is worth $\kappa_0$ observations.

```python
# Prior N(10, 4); known obs variance sigma^2 = 9; n = 12 measurements of a true theta = 13.
rng_nn = np.random.default_rng(1)
m0, tau2, sigma2 = 10.0, 4.0, 9.0
data = rng_nn.normal(13.0, np.sqrt(sigma2), size=12)
m_post, var_post = normal_known_var_update(m0, tau2, sigma2, data)
xbar = data.mean(); n = len(data)
w_data = (n/sigma2) / (1/tau2 + n/sigma2)
print(f"prior precision = {1/tau2:.4f}   data precision = {n/sigma2:.4f}   post precision = {1/var_post:.4f}")
print(f"xbar (MLE) = {xbar:.4f}")
print(f"posterior mean = {m_post:.4f}   posterior sd = {np.sqrt(var_post):.4f}")
print(f"weight on data = {w_data:.4f}   weight on prior = {1-w_data:.4f}")
print(f"prior worth kappa0 = sigma2/tau2 = {sigma2/tau2:.2f} observations")

xg = np.linspace(6, 18, 500)
fig, ax = plt.subplots()
ax.plot(xg, stats.norm(m0, np.sqrt(tau2)).pdf(xg), color="C0", label="prior N(10, 4)")
lik = stats.norm(xbar, np.sqrt(sigma2/n)).pdf(xg); lik = lik / lik.max() * stats.norm(m_post, np.sqrt(var_post)).pdf(xg).max()
ax.plot(xg, lik, color="C7", ls="--", label=r"scaled likelihood (peak $\bar y$)")
ax.plot(xg, stats.norm(m_post, np.sqrt(var_post)).pdf(xg), color="C1", lw=2, label="posterior")
ax.axvline(xbar, color="C7", lw=1); ax.axvline(m_post, color="C1", lw=1, ls=":")
ax.set_xlabel(r"$\theta$"); ax.set_ylabel("density")
ax.set_title("Posterior sits between prior and MLE, and is tighter than both")
ax.legend()
save(fig, "normal-normal")
```

![Prior centered at 10, scaled likelihood peaked at the data mean near 13.7, and the posterior peaked at 13.12 between them but visibly narrower than either.](figures/05-conjugate-updating/normal-normal.png)

The data pull hard: with $n=12$ observations at precision $1/9$ each, the data precision `1.3333` swamps the prior precision `0.2500`, so the posterior mean `13.1209` lands `0.8421` of the way from the prior (10) to the MLE `13.7061`, with posterior sd `0.7947` — tighter than the prior sd (2) and the standard error alike. Two callbacks worth stating loudly, because whole later modules are this formula in costume: **the Kalman filter (module 21)** applies exactly this update once per time step, and its "gain" is $w_{\text{data}}$; **hierarchical partial pooling (module 16)** applies it with the population as prior, and its shrinkage weight is $w_{\text{prior}}$. When you meet those, remember you already derived them here.

## 05.5 Same move, new algebra: three more pairs

The pattern is fixed; only the algebra changes. Here are the remaining three workhorse pairs, each with its one *predictive* twist — the honest $p(\tilde y\mid y)$ that integrates out the parameter rather than plugging in a point.

| prior → likelihood | posterior (add sufficient stat) | posterior predictive $p(\tilde y\mid y)$ |
|---|---|---|
| $\mathrm{Beta}(a,b)$ → Bernoulli | $\mathrm{Beta}(a+s,\ b+f)$ | Beta-Binomial (§05.6) |
| $N(m_0,\tau^2)$ → Normal, $\sigma^2$ known | $N(m_n,\tau_n^2)$ | $N(m_n,\ \tau_n^2+\sigma^2)$ |
| $\mathrm{Gamma}(a_0,b_0)$ → Poisson | $\mathrm{Gamma}(a_0+\textstyle\sum y,\ b_0+n)$ | **Negative-Binomial** |
| NIG$(m_0,\kappa_0,a_0,b_0)$ → Normal, both unknown | NIG$(m_n,\kappa_n,a_n,b_n)$ | **Student-$t_{2a_n}$** |
| $\mathrm{Dir}(\alpha)$ → Multinomial | $\mathrm{Dir}(\alpha+\text{counts})$ | **add-$\alpha$ (Dirichlet-Multinomial)** |

**Gamma-Poisson → Negative-Binomial (overdispersion).** With rate $\lambda\sim\mathrm{Gamma}(a,b)$ ($b$ = rate) and Poisson counts, the posterior is $\mathrm{Gamma}(a+\sum y, b+n)$. Marginalizing $\lambda$ out of the predictive turns one Poisson into a **Negative-Binomial** — a Poisson whose rate is itself uncertain, so its variance *exceeds* its mean (overdispersion), unlike the plug-in Poisson where they are equal.

```python
# Prior Gamma(2,1); observe 2 events in 1 exposure period -> posterior Gamma(4,2).
an_g, bn_g = gamma_poisson_update(2.0, 1.0, y=np.array([2]), n_units=1)
r, p = an_g, bn_g / (bn_g + 1.0)                 # predictive NegBin(r, p)
negbin_pred = stats.nbinom(r, p)
print(f"posterior Gamma({an_g:.0f},{bn_g:.0f}): lambda mean = {an_g/bn_g:.1f}")
print(f"predictive NegBin: mean = {negbin_pred.mean():.1f}   variance = {negbin_pred.var():.1f}")
print(f"plug-in Poisson({an_g/bn_g:.1f}): variance = {an_g/bn_g:.1f}  (mean = variance)")
```

The predictive mean is `2.0` either way, but the Negative-Binomial variance is `3.0` against the plug-in Poisson's `2.0`: accounting for uncertainty in $\lambda$ adds 50% to the predictive variance. That extra spread is not a modelling choice; it is what honesty costs.

**NIG → Student-$t$ (both mean and variance unknown).** This is the case that matters for regression (module 14). The Normal-Inverse-Gamma prior is conjugate when *both* $\mu$ and $\sigma^2$ are unknown; `nig_post` gives the update. Integrating $\sigma^2$ out of the predictive yields a **Student-$t$** — Gaussian in the middle, power-law in the tails — with, exactly (booklet ch. 8; verified below),
$$\tilde y \mid y \;\sim\; t_{\,\nu}\big(\text{loc}=m_n,\ \text{scale}^2 = \tfrac{b_n(\kappa_n+1)}{a_n\kappa_n}\big),\qquad \nu = 2a_n.$$

```python
def student_t_predictive(kn, mn, an, bn):
    """Posterior predictive for one new draw under a NIG posterior: Student-t params."""
    df = 2*an
    loc = mn
    scale = np.sqrt(bn*(kn + 1) / (an*kn))
    return df, loc, scale

rng_nig = np.random.default_rng(2)
dat = rng_nig.normal(5.0, 2.0, size=20)
kn, mn, an, bn = nig_post(dat)                      # default weak prior mu0=0,k0=1,a0=1,b0=1
df, loc, scale = student_t_predictive(kn, mn, an, bn)
print(f"posterior NIG: kn={kn:.0f}  mn={mn:.4f}  an={an:.0f}  bn={bn:.4f}")
print(f"predictive t: df={df:.0f}  loc={loc:.4f}  scale={scale:.4f}")

# Monte-Carlo the predictive from its definition and compare to the closed form.
M = 300_000
s2  = stats.invgamma(a=an, scale=bn).rvs(size=M, random_state=rng_nig)   # sigma^2 | y; IG(a,b): scipy scale = b (course convention, STYLE §3)
mu  = rng_nig.normal(mn, np.sqrt(s2/kn))                                  # mu | sigma^2, y
yt  = rng_nig.normal(mu, np.sqrt(s2))                                     # ytilde | mu, sigma^2
tt  = stats.t(df, loc, scale)
print(f"MC predictive mean = {yt.mean():.4f}   closed-form t mean = {tt.mean():.4f}")
print(f"MC predictive sd   = {yt.std():.4f}   closed-form t sd   = {tt.std():.4f}")
print(f"5th pct  MC {np.quantile(yt,0.05):.3f} vs t {tt.ppf(0.05):.3f};  "
      f"95th pct MC {np.quantile(yt,0.95):.3f} vs t {tt.ppf(0.95):.3f}")

xg = np.linspace(-4, 14, 500)
sig_hat = bn/(an - 1)                                # posterior mean of sigma^2 (plug-in)
fig, ax = plt.subplots()
ax.hist(yt, bins=120, range=(-4, 14), density=True, color="C7", alpha=0.5, label="MC predictive")
ax.plot(xg, tt.pdf(xg), color="C1", lw=2, label=f"closed-form $t_{{{df:.0f}}}$")
ax.plot(xg, stats.norm(mn, np.sqrt(sig_hat)).pdf(xg), color="C3", ls="--", label="plug-in Normal")
ax.set_xlabel(r"$\tilde y$"); ax.set_ylabel("density")
ax.set_title("NIG predictive is Student-t: heavier tails than the plug-in Normal")
ax.legend()
save(fig, "nig-student-t")
```

![Monte-Carlo predictive histogram overlaid with the closed-form t_22 density riding exactly on it, and a plug-in Normal that is visibly too thin in the tails.](figures/05-conjugate-updating/nig-student-t.png)

The closed-form $t_{22}$ nails the simulation: predictive mean `4.6672` vs MC `4.6669`, sd `2.1338` vs `2.1329`, and the 5th/95th percentiles agree to `1.174`/`1.176` and `8.161`/`8.163`. The plug-in Normal (dashed) uses the posterior-mean variance and is too thin — it would under-price extreme observations, the same overconfidence as §05.1 in a continuous costume.

**Dirichlet-Multinomial → add-$\alpha$ smoothing.** For $K$ categories with prior $\mathrm{Dir}(\alpha)$ and observed counts $n_k$, the posterior is $\mathrm{Dir}(\alpha+n)$ and the predictive probability of the next token in category $k$ is
$$P(\tilde x = k\mid n) = \frac{\alpha_k + n_k}{\sum_j (\alpha_j + n_j)}.$$
This is **exactly add-$\alpha$ smoothing** — the fix every n-gram language model uses so an unseen word does not get probability zero.

```python
# 4-word vocabulary; word index 1 was never observed. Symmetric prior alpha = 1 each.
alpha = np.array([1., 1., 1., 1.])
counts = np.array([12, 0, 3, 5])
post = dirichlet_mult_update(alpha, counts)
pred_probs = post / post.sum()
mle = counts / counts.sum()
print(f"MLE next-token probs   = {np.round(mle, 4)}")
print(f"add-1 smoothed probs   = {np.round(pred_probs, 4)}")
print(f"unseen word: MLE = {mle[1]:.4f}  ->  smoothed = {pred_probs[1]:.4f}")
```

The MLE assigns the unseen word probability `0.0000`; the add-1 predictive assigns `0.0417`. The Dirichlet prior contributed one pseudo-count per word — the multi-category twin of Beta's one-pseudo-success, one-pseudo-failure. Laplace's rule of succession (module 01), Beta's $+1$, and add-$\alpha$ are the same move at $K=2$, $K=2$, and $K$ categories.

## 05.6 Predictive vs plug-in: the honest interval

The recurring theme deserves a formula. The plug-in predictive freezes $\theta$ at a point estimate and reports $p(\tilde y\mid\hat\theta)$; the posterior predictive integrates, $p(\tilde y\mid y)=\int p(\tilde y\mid\theta)\,p(\theta\mid y)\,d\theta$. The **law of total variance** decomposes the honest predictive variance exactly:
$$\mathrm{Var}[\tilde y\mid y] = \underbrace{\mathbb{E}_{\theta\mid y}\!\big[\mathrm{Var}[\tilde y\mid\theta]\big]}_{\text{aleatoric — irreducible noise}} \;+\; \underbrace{\mathrm{Var}_{\theta\mid y}\!\big[\mathbb{E}[\tilde y\mid\theta]\big]}_{\text{epistemic — parameter uncertainty}}.$$
The plug-in keeps only the first term and discards the second. **In these fixed-dispersion conjugate families the epistemic term is strictly positive whenever the posterior is non-degenerate, so the predictive is strictly wider than the plug-in** — but this is a property of these families, *not* a universal law (in a model where more data can reveal *lower* noise, the honest predictive can be narrower; hence "strictly wider *here*," never "always wider"). Verify the widening on the two discrete cases:

```python
# Beta-Binomial: Beta(5,3) posterior, predict successes in m = 10 future trials.
a, b, m = 5, 3, 10
p = a/(a + b); K = a + b
var_plugin_bb = m*p*(1-p)                              # Binomial(m, p_hat)
var_pred_bb   = m*p*(1-p) * (K + m)/(K + 1)            # Beta-Binomial closed form
print(f"Beta-Binomial: plug-in var = {var_plugin_bb:.2f}   predictive var = {var_pred_bb:.2f}"
      f"   ratio = {var_pred_bb/var_plugin_bb:.1f}")

# Gamma-Poisson from 05.5: plug-in Poisson var 2.0 vs NegBin predictive var 3.0.
print(f"Gamma-Poisson: plug-in var = {an_g/bn_g:.1f}   predictive var = {negbin_pred.var():.1f}")
```

For the Beta-Binomial the epistemic term doubles the variance: plug-in `2.34` against predictive `4.69`. Now the consequence a practitioner actually feels — coverage.

**Predict.** You will simulate many future outcomes whose true $\theta$ is itself drawn from the posterior, and check how often a **plug-in** 90% interval (built from $\hat p = a/(a{+}b)$) actually contains them. Commit to a number: is the realized coverage 90%, or something else?

```python
rng_cov = np.random.default_rng(6)
Ntrial = 400_000
theta = stats.beta(a, b).rvs(size=Ntrial, random_state=rng_cov)   # true theta ~ posterior
y_future = rng_cov.binomial(m, theta)                             # honest future data
# plug-in 90% interval: freeze theta at p_hat
lo_pi, hi_pi = stats.binom(m, p).ppf(0.05), stats.binom(m, p).ppf(0.95)
cov_plugin = np.mean((y_future >= lo_pi) & (y_future <= hi_pi))
# what the interval covers under the plug-in's OWN model (discreteness makes it >90%)
cov_nominal = stats.binom(m, p).cdf(hi_pi) - stats.binom(m, p).cdf(lo_pi - 1)
print(f"plug-in interval's coverage under its own Binomial model = {cov_nominal:.4f}")
# predictive 90% interval: Beta-Binomial quantiles
from scipy.special import betaln, comb
xs = np.arange(m + 1)
bb_pmf = comb(m, xs) * np.exp(betaln(xs + a, m - xs + b) - betaln(a, b))
bb_cdf = np.cumsum(bb_pmf)
lo_pr, hi_pr = xs[np.searchsorted(bb_cdf, 0.05)], xs[np.searchsorted(bb_cdf, 0.95)]
cov_pred = np.mean((y_future >= lo_pr) & (y_future <= hi_pr))
print(f"plug-in 90% interval [{lo_pi:.0f}, {hi_pi:.0f}]: realized coverage = {cov_plugin:.4f}")
print(f"predictive 90% interval [{lo_pr}, {hi_pr}]: realized coverage = {cov_pred:.4f}")

fig, ax = plt.subplots()
w = 0.4
ax.bar(xs - w/2, stats.binom(m, p).pmf(xs), width=w, color="C3", alpha=0.8, label="plug-in Binomial")
ax.bar(xs + w/2, bb_pmf, width=w, color="C1", alpha=0.8, label="predictive Beta-Binomial")
ax.set_xlabel("successes in next 10 trials"); ax.set_ylabel("probability")
ax.set_title("Plug-in (narrow) vs posterior-predictive (wider): the honest interval covers")
ax.legend()
save(fig, "predictive-vs-plugin")
```

![Two overlaid pmfs over 0–10 successes: the plug-in Binomial is tall and concentrated; the Beta-Binomial predictive is lower and more spread, with visibly fatter shoulders.](figures/05-conjugate-updating/predictive-vs-plugin.png)

The plug-in interval covers only `0.8307` of honest future outcomes. The comparison is actually *worse* than "90 vs 83": on the coarse discrete support the interval $[4,9]$ covers `0.9525` under the plug-in's own Binomial model — it is really a ~95% interval — yet honest reality still catches it out at 83%. The epistemic term alone accounts for that twelve-point drop; discreteness worked in the plug-in's favor and it under-covered anyway. The predictive interval $[2,10]$ covers `0.9822` (over-covering slightly, the same discreteness now on the honest side). The naive expectation "a 90% interval covers 90%" fails precisely because the plug-in interval answers the wrong question — it is the interval you would report *if you knew $\theta$*, which you do not.

## 05.7 A/B test, driven to a decision  [line 4]

A posterior is not a deliverable; an *action* is. Two ad variants: A converts 41 of 1000, B converts 57 of 1000. Flat $\mathrm{Beta}(1,1)$ priors give posteriors $\mathrm{Beta}(42,960)$ and $\mathrm{Beta}(58,944)$. Most write-ups stop at $P(\theta_B>\theta_A)$. That is line 2. **Shipping is line 4** — minimize posterior expected loss — and it needs a loss, not just a probability. Take the loss of a decision to be the *regret*: if you ship the worse arm, you lose the conversion-rate difference on every future impression.

**Predict.** Spoiler for one number: $P(\theta_B>\theta_A)$ will come out $\approx 0.95$. Given that, shipping B feels obvious — but *by how much*? Before running, commit to the **ratio of ship-A's expected regret to ship-B's**: roughly 20× (odds of 0.95 to 0.05), or something much larger?

**Reason.** The intuition being used: "a high win-probability *is* the decision — 95% vs 5% means the margin is about 19-to-1." That reads the probability as if it already carried the stakes.

```python
rng_ab = np.random.default_rng(4)
postA = beta_binomial_update(1, 1, s=41, f=1000-41)     # Beta(42, 960)
postB = beta_binomial_update(1, 1, s=57, f=1000-57)     # Beta(58, 944)
M = 200_000
tA = stats.beta(*postA).rvs(size=M, random_state=rng_ab)
tB = stats.beta(*postB).rvs(size=M, random_state=rng_ab)

p_B_beats_A = np.mean(tB > tA)
uplift = np.mean(tB - tA)
loss_ship_B = np.mean(np.maximum(tA - tB, 0.0))   # regret when A was really better
loss_ship_A = np.mean(np.maximum(tB - tA, 0.0))   # regret when B was really better
decision = "B" if loss_ship_B < loss_ship_A else "A"
print(f"P(theta_B > theta_A) = {p_B_beats_A:.4f}")
print(f"E[uplift B - A]      = {uplift:.5f}")
print(f"expected loss | ship B = {loss_ship_B:.6f}")
print(f"expected loss | ship A = {loss_ship_A:.6f}")
print(f"regret ratio ship-A : ship-B = {loss_ship_A/loss_ship_B:.0f}x")
print(f"DECISION: ship {decision}  (minimizes posterior expected loss)")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
tg = np.linspace(0.02, 0.09, 400)
ax[0].plot(tg, stats.beta(*postA).pdf(tg), color="C0", label="A: Beta(42,960)")
ax[0].plot(tg, stats.beta(*postB).pdf(tg), color="C1", label="B: Beta(58,944)")
ax[0].set_xlabel(r"conversion rate $\theta$"); ax[0].set_ylabel("density")
ax[0].set_title("Posterior rates overlap"); ax[0].legend()
d = tB - tA
ax[1].hist(d, bins=80, density=True, color="C7", alpha=0.6)
ax[1].axvline(0, color="k", lw=1)
ax[1].set_xlabel(r"uplift $\theta_B - \theta_A$"); ax[1].set_ylabel("density")
ax[1].set_title(f"P(B>A) = {p_B_beats_A:.3f}; but the decision needs the loss")
save(fig, "ab-test")
```

![Left: two overlapping Beta posteriors for A and B, B shifted right. Right: histogram of the uplift theta_B minus theta_A, mostly positive with a small tail below zero at the P(B>A) boundary.](figures/05-conjugate-updating/ab-test.png)

**Reconcile.** $P(\theta_B>\theta_A) = $ `0.9510`, expected uplift `0.01594` — and the regret ratio is not 19-to-1 but `81`×: shipping B risks `0.000199` in expected regret, shipping A risks `0.016134`. The 19-to-1 guess missed by a factor of four because a probability weighs *worlds*, while a loss weighs *worlds × stakes*. In the 5% of worlds where A is really better, A and B are nearly tied, so being wrong there costs almost nothing; in the worlds where B is better, shipping A forfeits a full point-and-a-half of conversion. The probability alone cannot see that asymmetry — only the expected loss can. **Ship B.** That gap between "which is probably better" and "which should I ship" is line 4 earning its place; module 22 extends it to *when to stop testing* (expected value of sample information).

## 05.8 The Gaussian conditioning toolkit

Everything above conditioned scalars. The multivariate-Gaussian conditioning formulas are the engine behind three later modules, so derive them once and verify them. Partition a joint Gaussian $x=(x_1,x_2)$ with
$$x \sim N\!\left(\begin{bmatrix}\mu_1\\\mu_2\end{bmatrix}, \begin{bmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{bmatrix}\right).$$
Conditioning $x_1$ on an observed $x_2$ keeps the result Gaussian (a Gaussian is closed under conditioning, as it is under marginalization) with
$$\mu_{1\mid 2} = \mu_1 + \Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2),\qquad \Sigma_{1\mid 2} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}.$$
Two things to read off. The conditional mean is *linear* in the observation $x_2$ — that linear map $\Sigma_{12}\Sigma_{22}^{-1}$ is the regression coefficient of $x_1$ on $x_2$, and it is the Kalman gain again. The conditional covariance $\Sigma_{1\mid 2}$ does *not* depend on the observed value $x_2$, only on the covariance structure — observing $x_2$ shrinks your uncertainty about $x_1$ by a fixed amount (the **Schur complement**) no matter what value you see. Verify against brute-force conditional sampling on a 3-d Gaussian:

```python
rng_g = np.random.default_rng(7)
mu = np.array([1.0, -2.0, 0.5])
A = rng_g.normal(size=(3, 3)); Sigma = A @ A.T + 0.5*np.eye(3)      # a valid covariance

def gaussian_condition(mu, Sigma, idx1, idx2, x2):
    """Posterior of block idx1 given block idx2 = x2. Returns (cond_mean, cond_cov)."""
    S11 = Sigma[np.ix_(idx1, idx1)]; S12 = Sigma[np.ix_(idx1, idx2)]
    S22 = Sigma[np.ix_(idx2, idx2)]; S21 = Sigma[np.ix_(idx2, idx1)]
    cond_mean = mu[idx1] + S12 @ np.linalg.solve(S22, x2 - mu[idx2])
    cond_cov  = S11 - S12 @ np.linalg.solve(S22, S21)
    return cond_mean, cond_cov

x2 = np.array([0.7, -1.3])                                          # observe x1, x2 (0-indexed: dims 1,2)
cm, cc = gaussian_condition(mu, Sigma, idx1=[0], idx2=[1, 2], x2=x2)
print(f"block formula: cond mean = {cm[0]:.4f}   cond var = {cc[0,0]:.4f}")

# exact algebraic cross-check via the PRECISION matrix: with Lambda = Sigma^{-1}
# partitioned conformally, Sigma_{1|2} = Lambda_11^{-1} and
# mu_{1|2} = mu_1 - Lambda_11^{-1} Lambda_12 (x2 - mu_2)  — an independent route.
Lam = np.linalg.inv(Sigma)
cc_prec = 1.0 / Lam[0, 0]
cm_prec = mu[0] - cc_prec * (Lam[0, 1:] @ (x2 - mu[1:]))
print(f"precision route: max|diff| mean = {abs(cm_prec - cm[0]):.1e}, "
      f"var = {abs(cc_prec - cc[0,0]):.1e}   (machine precision)")

# brute force: sample the joint, keep draws whose (x1,x2) land near the observed values.
X = rng_g.multivariate_normal(mu, Sigma, size=8_000_000)
keep = (np.abs(X[:, 1] - x2[0]) < 0.1) & (np.abs(X[:, 2] - x2[1]) < 0.1)
sub = X[keep, 0]
print(f"brute force (n={keep.sum()} kept): cond mean = {sub.mean():.4f}   cond var = {sub.var():.4f}")
print(f"max|difference|: mean {abs(sub.mean()-cm[0]):.4f}, var {abs(sub.var()-cc[0,0]):.4f}")

xg = np.linspace(cm[0]-3, cm[0]+3, 300)
fig, ax = plt.subplots()
ax.hist(sub, bins=60, density=True, color="C7", alpha=0.6, label="brute-force conditional")
ax.plot(xg, stats.norm(cm[0], np.sqrt(cc[0,0])).pdf(xg), color="C1", lw=2, label="block-formula Gaussian")
ax.set_xlabel(r"$x_1 \mid x_2$"); ax.set_ylabel("density")
ax.set_title("MVN block formulas reproduce brute-force conditional sampling")
ax.legend()
save(fig, "gaussian-conditioning")
```

![Histogram of brute-force conditioned samples of x1 with the block-formula Gaussian density overlaid, matching in both center and width.](figures/05-conjugate-updating/gaussian-conditioning.png)

The block formula gives conditional mean `0.7999` and variance `0.5397`. Two independent checks confirm it. The *algebraic* one: computing the same conditional through the inverted **precision matrix** ($\Sigma_{1\mid2} = \Lambda_{11}^{-1}$, $\mu_{1\mid2} = \mu_1 - \Lambda_{11}^{-1}\Lambda_{12}(x_2-\mu_2)$ — the Schur complement seen from the other side) agrees to machine precision. The *sampling* one: brute-force rejection (keeping the ~`2831` of 8 million draws that land near the observed $x_2$) returns `0.7904` and `0.5304` — within `0.0096` and `0.0093`, which is Monte-Carlo noise plus a small finite-window bias from conditioning on a neighborhood rather than a point. **These two formulas are load-bearing infrastructure for three later modules:** Bayesian linear regression's posterior over coefficients (module 14) is one conditioning step; the Gaussian-process posterior (module 20) is this formula with $\Sigma$ replaced by a kernel matrix; and the Kalman filter (module 21) alternates the Normal-Normal update of §05.4 with a marginalize-then-condition sweep built from exactly these blocks.

## Bridge — C-B §7.2, and the shrinkage you already use

C-B §7.2 introduces conjugate families as a convenience for computing posteriors; this module reframes them as the place where the course's central *intuition* lives in closed form. Every precision-weighted average you derived here is a named procedure elsewhere. **Ridge regression** (module 00's opener, formalized in module 14) is the Normal-Normal posterior mean with a Gaussian prior — the penalty strength $\lambda$ is the prior precision. **The Kalman gain** is $w_{\text{data}}$ from §05.4. **James-Stein and hierarchical partial pooling** (modules 08, 16) are the same convex combination with a *data-estimated* prior. And **add-$\alpha$ smoothing** in an n-gram model is the Dirichlet-Multinomial predictive. The frequentist and ML worlds rediscovered each of these under other names; conjugacy is where you see they are one formula. The catch to keep honest: conjugate priors are chosen partly for tractability, so always ask whether the convenient prior is also a *defensible* one — module 07 takes that question seriously.

## Pitfalls

- **Reporting the plug-in predictive.** Freezing $\theta$ at $\hat\theta$ and predicting from $p(\tilde y\mid\hat\theta)$ discards the epistemic variance term and under-covers (§05.6: 83% coverage from a nominal 90% interval). The posterior predictive is the honest object; it is *strictly wider* in these fixed-dispersion families.
- **Calling a conjugate prior "objective."** $\mathrm{Beta}(1,1)$ looks like "no information," but it is one pseudo-success and one pseudo-failure and it visibly moves small-$n$ answers (§05.1). The prior's pseudo-sample-size $\kappa$ is exactly how many observations it is worth; state it.
- **Confusing rate and scale in Gamma/Inverse-Gamma.** The course convention is $\mathrm{Gamma}(\alpha,\beta)$ with $\beta$ = *rate*; scipy's `gamma`/`invgamma` take `scale`. `gamma_poisson_update` returns a rate; feed it to scipy as `scale=1/rate`. A silent rate/scale swap corrupts every downstream number.
- **Forgetting the predictive is Student-$t$, not Normal, when $\sigma^2$ is unknown.** Plugging in an estimated variance gives thin Gaussian tails (§05.5) and under-prices outliers — the more so at small $n$, where $\nu=2a_n$ is small and the $t$ is heaviest.
- **Stopping an A/B test at $P(B>A)$.** That is line 2. The shipping decision is line 4 and needs a loss; a high $P(B>A)$ with a tiny expected uplift can still be worth shipping, or not, depending on costs (§05.7).

## Exercises

**Exercise 05.1 — Sequential equals batch.**
*Setup:* You will see 6 successes and 2 failures, starting from a $\mathrm{Beta}(2,2)$ prior. You can update all 8 at once, or one observation at a time, feeding each posterior in as the next prior.
*Predict:* Do the two routes give the same final posterior, a slightly different one (order effects), or a very different one?
*Reason:* The intuition "processing data incrementally accumulates rounding/order effects" — the habit from iterative numerical algorithms.
*Run:*
```python
a, b = 2.0, 2.0
obs = [1,1,0,1,1,1,0,1]                      # 6 successes, 2 failures, in some order
a_seq, b_seq = a, b
for x in obs:
    a_seq, b_seq = beta_binomial_update(a_seq, b_seq, s=x, f=1-x)
a_batch, b_batch = beta_binomial_update(a, b, s=sum(obs), f=len(obs)-sum(obs))
print(f"sequential -> Beta({a_seq:.0f},{b_seq:.0f});  batch -> Beta({a_batch:.0f},{b_batch:.0f})")
```
<details><summary>Reconcile</summary>

Both routes give $\mathrm{Beta}(8,4)$ — identical, and independent of the order of `obs`. Conditioning on data one piece at a time is the same as conditioning once on all of it: $p(\theta\mid y_1,y_2)\propto p(y_2\mid\theta)\,p(y_1\mid\theta)\,p(\theta)$, and multiplication commutes. This is *why* conjugate updating can run online (the Kalman filter, module 21, is this fact on a time axis) and why yesterday's posterior is a valid prior for today. The sufficient statistic $(\sum x_i, n)$ is all that survives, so order is invisible — a direct callback to module 04's sufficiency shuffle test.
</details>

**Exercise 05.2 — The predictive you can't beat by plugging in.**  *(surprising)*
*Setup:* From a $\mathrm{Beta}(8,4)$ posterior, you predict the number of successes in the next 20 trials. A colleague uses the plug-in Binomial(20, $\hat p = 8/12$); you use the Beta-Binomial predictive.
*Predict:* By what factor is the predictive standard deviation larger than the plug-in's — 1.0× (no difference), about 1.1×, or more than 1.3×?
*Reason:* "With a fairly sharp posterior (12 pseudo-trials), the parameter uncertainty is small, so the two should nearly agree."
*Run:*
```python
a, b, m = 8, 4, 20
p = a/(a+b); K = a+b
sd_plugin = np.sqrt(m*p*(1-p))
sd_pred   = np.sqrt(m*p*(1-p) * (K+m)/(K+1))
print(f"plug-in sd = {sd_plugin:.3f}   predictive sd = {sd_pred:.3f}   ratio = {sd_pred/sd_plugin:.3f}")
```
<details><summary>Reconcile</summary>

The ratio is `1.569` — the predictive standard deviation is 57% larger, because the variance-inflation factor $(K+m)/(K+1) = 32/13 \approx 2.46$ is substantial when the horizon $m$ is comparable to the pseudo-sample-size $K$. The naive guess badly underestimates the gap: the epistemic term grows with *how far ahead you predict*. Predicting one step ahead, the inflation is mild; predicting a batch larger than your evidence, it dominates. This is the discrete cousin of the regression trumpet (module 14), where predictive intervals flare as you extrapolate away from where the data pinned the parameters down.
</details>

**Exercise 05.3 — Add-$\alpha$ and the language model's zero.**  *(ML bridge)*
*Setup:* A bigram model has seen the context "San" followed by "Francisco" 40 times, "Diego" 9 times, "Marino" 1 time, and 0 times each for 9,997 other vocabulary words (vocabulary size 10,000). You smooth with a symmetric $\mathrm{Dir}(\alpha)$ prior.
*Predict:* Under add-1 smoothing ($\alpha=1$), what probability does the model assign to the *most frequent* continuation "Francisco" — close to its MLE 40/50 = 0.80, or dramatically lower?
*Reason:* "Smoothing only nudges the unseen words; the common word keeps roughly its MLE probability."
*Run:*
```python
V = 10_000
counts = np.zeros(V); counts[0], counts[1], counts[2] = 40, 9, 1     # Francisco, Diego, Marino
for alpha in (1.0, 0.0001):
    post = counts + alpha
    p_fran = post[0] / post.sum()
    p_unseen = alpha / post.sum()
    print(f"alpha={alpha}: P(Francisco) = {p_fran:.4f}   P(an unseen word) = {p_unseen:.7f}")
```
<details><summary>Reconcile</summary>

With add-1 the denominator becomes $50 + 10{,}000\cdot 1 = 10{,}050$, so P(Francisco) collapses from 0.80 to `0.0041` — the 10,000 pseudo-counts *swamp* the 50 real observations. Add-1 smoothing over a large vocabulary is a wildly overconfident *prior*, worth 10,000 pseudo-observations against your 50 real ones. The fix practitioners actually use is a tiny $\alpha$: only when $\alpha=0.0001$ (pseudo-sample-size $\kappa=\alpha V = 1$) does P(Francisco) climb back to `0.7843`, near the MLE, while unseen words still get a nonzero `0.0000020`. The lesson from §05.3 made quantitative: the prior's pseudo-sample-size $\kappa = \alpha V$ must be *small relative to your data*, or the prior — not the corpus — decides your probabilities. This is exactly why real language models tune the smoothing constant far below 1 rather than defaulting to add-1.
</details>

**Exercise 05.4 — Whose prior wins at n = 5 vs n = 500?**
*Setup:* Two analysts model the same Bernoulli stream (true $\theta=0.3$): one uses a near-flat $\mathrm{Beta}(1,1)$, the other a confident-but-wrong $\mathrm{Beta}(20,2)$ (prior mean $\approx 0.91$). Compare their posterior means at $n=5$ and $n=500$.
*Predict:* At $n=500$, how far apart are the two posterior means — still far (the priors disagreed by 0.6), or essentially equal?
*Reason:* "A strong, wrong prior biases the answer, and bias persists" — the worry that a bad prior poisons everything.
*Run:*
```python
rng_ex = np.random.default_rng(11)
stream = rng_ex.binomial(1, 0.3, size=500)
for n in (5, 500):
    s = int(stream[:n].sum()); f = n - s
    m_flat = (1+s)/(1+1+n)
    m_conf = (20+s)/(20+2+n)
    print(f"n={n:>3}: flat prior mean = {m_flat:.4f}   confident-wrong prior mean = {m_conf:.4f}")
```
<details><summary>Reconcile</summary>

At $n=5$ the two posterior means are far apart (`0.1429` vs `0.7407` — the first five flips all came up 0) — the confident prior, worth $\kappa=22$ pseudo-trials, dominates 5 real ones. At $n=500$ they are `0.2809` and `0.3065`, essentially equal and both near the truth 0.3: 500 observations swamp 22 pseudo-observations, so the prior *washes out*. The bias does not persist; it is diluted at rate $\kappa/(\kappa+n)$. This is the honest answer to the ML skeptic's "priors are just bias": for identified parameters with enough data, any non-dogmatic prior washes out — a preview of module 07, where the exception (unidentified parameters, where it *never* washes out) is the real subtlety.
</details>

## Takeaways

- **Conjugacy is exponential-family closure:** write the prior in the likelihood's natural form and the posterior stays in the family — you update by adding your data's sufficient statistic to the prior's pseudo-statistic and your $n$ to its pseudo-$n$.
- **The master shrinkage formula:** every conjugate posterior mean is a precision-weighted average, $\frac{\kappa}{\kappa+n}\,(\text{prior mean}) + \frac{n}{\kappa+n}\,(\text{MLE})$. The prior is worth $\kappa$ observations; this same formula is ridge, the Kalman gain, and partial pooling.
- **S2 — the overconfident MLE:** 2-of-2 gives MLE 1.0 but posterior mean and predictive `0.75`; plug-in prediction is most overconfident when data are scarcest. Recurs as the rule of succession, add-$\alpha$, and module 14's regression trumpet.
- **Predictive, not plug-in:** the posterior predictive integrates out $\theta$; by the law of total variance it adds an epistemic term and is strictly wider in these families (Beta-Binomial `4.69` vs `2.34`, Gamma-Poisson `3.0` vs `2.0`), so a plug-in 90% interval under-covers (`0.8307`).
- **Five pairs, five predictives:** Beta→Beta, Normal→Normal, Gamma→Gamma (predictive Negative-Binomial, overdispersed), NIG→NIG (predictive Student-$t_{2a_n}$, heavy-tailed), Dirichlet→Dirichlet (predictive add-$\alpha$).
- **Decisions are line 4:** an A/B test ends not at $P(B>A)=$ `0.9510` but at the expected-loss comparison (`0.000199` ship-B vs `0.016134` ship-A) that says *ship B*.
- **The Gaussian conditioning block formulas** $\mu_{1\mid2}=\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2)$, $\Sigma_{1\mid2}=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ are verified infrastructure for Bayesian regression (14), Gaussian processes (20), and the Kalman filter (21).

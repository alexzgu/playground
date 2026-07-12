# 09. Monte Carlo Fundamentals

> **Spine.** Any expectation becomes a sample average carrying a CLT error bar you are obligated to report; importance sampling can fix rare-event and reweighting problems but fails *silently*, and the weight diagnostics are the only alarm.
> **Which line?** The engine for lines 2–4 when the integrals are intractable. Module 05 did conditioning and prediction in closed form; from here on the posterior is a *bag of samples*, and every posterior mean, interval, tail probability, and expected loss is one `mean()` away.
> **Promise.** After this module you can turn any posterior into samples and read off any summary with an honest ±MCSE; estimate a rare-event probability that naive simulation reports as *zero*; recognize importance-sampling failure from its weight histogram and effective sample size before it corrupts an answer; and run a likelihood-free (ABC) inference from scratch.
> **Prereqs.** Modules 00 (four lines), 02 (Monte Carlo standard error, promised there), 03 (heavy tails: Cauchy and Student-$t$), 05 (posterior samples, the Beta(8,4) coin).
> **Runtime.** ~35 s.
> **Sources.** Booklet ch. 3 §3.1, ch. 5 §§5.6–5.11 (quadrature, rejection, importance sampling); C-B §5.6 (generating a random sample); MCMT ch. 1 by concept.

Module 05 left every posterior in closed form: a Beta, a Normal, an Inverse-Gamma. Real models are not conjugate. The posterior $p(\theta\mid y)\propto p(y\mid\theta)\,p(\theta)$ has a normalizing constant you cannot compute and an integral $\mathrm{E}[g(\theta)\mid y]=\int g(\theta)\,p(\theta\mid y)\,d\theta$ you cannot do. The entire rest of the course is *ways to approximate that integral* — and they all start here, with the oldest idea: replace the integral with an average over draws.

The catch, and the reason this module exists, is that "just simulate it" hides two traps. The first is that **an estimate without an error bar is not a result** — module 02 promised we would formalize the Monte Carlo standard error, and we do. The second is subtler: the two techniques that rescue simulation when brute force fails — importance sampling and rejection — can return a confident, precise-looking, *wrong* number, and the only warning you get is in the sample weights. Learn to read the alarm.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "09-monte-carlo"          # this module's figure dir
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

## 09.1 Samples are the lingua franca

Take module 05's coin: a $\mathrm{Beta}(1,1)$ prior updated by 7 heads in 10 tosses gives the posterior $\mathrm{Beta}(8,4)$, with exact mean $8/12 = 0.6667$. Suppose you had *only* draws from it — no formulas. Everything you might want is a sample average.

The justification is one line of undergraduate probability. For iid draws $\theta_1,\dots,\theta_M$ from $p(\theta\mid y)$, the law of large numbers says $\hat\mu_M = \frac1M\sum_i g(\theta_i) \to \mathrm{E}[g(\theta)\mid y]$, and the central limit theorem says the error is asymptotically Normal: $\hat\mu_M - \mathrm{E}[g] \approx \mathcal{N}\!\big(0,\ \sigma_g^2/M\big)$, where $\sigma_g^2 = \mathrm{Var}[g(\theta)\mid y]$. Different questions are just different choices of $g$:

- the **posterior mean** is $g(\theta)=\theta$;
- a **tail probability** $P(\theta>c\mid y)$ is $g(\theta)=\mathbf{1}[\theta>c]$ — an indicator, whose average is a proportion;
- a **credible interval** is a pair of sample quantiles;
- **any transformation** — the odds $\theta/(1-\theta)$, the logit, a downstream utility — is free: transform the draws and average. You never re-derive a distribution; you push samples through a function.

```python
# 09.1 -- one bag of Beta(8,4) draws answers every question (M05 coin posterior)
post = stats.beta(8, 4)
M = 100_000
theta = post.rvs(size=M, random_state=rng)          # the bag of samples

print("quantity            Monte Carlo     exact")
print(f"posterior mean      {theta.mean():.4f}        {post.mean():.4f}")
print(f"P(theta > 0.5)      {(theta > 0.5).mean():.4f}        {post.sf(0.5):.4f}")
lo, hi = np.quantile(theta, [0.05, 0.95])
elo, ehi = post.ppf([0.05, 0.95])
print(f"90% CI low          {lo:.4f}        {elo:.4f}")
print(f"90% CI high         {hi:.4f}        {ehi:.4f}")
odds = theta / (1 - theta)                           # a transformation, for free
print(f"E[odds]             {odds.mean():.4f}        {8/(4-1):.4f}")   # E[theta/(1-theta)] = a/(b-1)
```

The Monte Carlo column recovers the posterior mean to `0.6663` (exact `0.6667`), the tail probability `0.8868` (exact `0.8867`), the 90% credible interval `[0.4345, 0.8649]` against the exact `[0.4356, 0.8649]`, and the posterior mean odds `2.6657` (exact `2.6667`, since $\mathrm{E}[\theta/(1-\theta)] = a/(b-1)$ for a Beta). This is the whole reason MCMC will be worth the trouble: **produce draws, and inference collapses to arithmetic.** The four lines don't change — line 3, the predictive integral, is now literally `g(draws).mean()`.

## 09.2 The error bar is the result

The CLT hands you the error bar for free. Since $\hat\mu_M \approx \mathcal N(\mathrm{E}[g],\ \sigma_g^2/M)$, the standard deviation of your estimate — the **Monte Carlo standard error** — is

$$\mathrm{MCSE} = \frac{\sigma_g}{\sqrt M}\ \approx\ \frac{s}{\sqrt M},\qquad s^2 = \tfrac{1}{M-1}\textstyle\sum_i (g(\theta_i)-\hat\mu_M)^2 .$$

You estimate $\sigma_g$ by the sample standard deviation $s$ of the very draws you already have. Two consequences the beginner misses. First, **precision improves only as $\sqrt M$**: cutting the error bar by 10× costs 100× the draws. Second, the MCSE is itself an estimate — an error bar on the error bar — so the honest test is: does $s/\sqrt M$, computed from *one* run, predict the actual scatter of $\hat\mu_M$ across *many* runs? It does.

```python
# 09.2 -- MCSE = s/sqrt(M) predicts the run-to-run scatter of the estimate
rng_mcse = np.random.default_rng(20)
Msmall, R = 2000, 1000
means = np.empty(R); mcses = np.empty(R)
for r in range(R):
    s = post.rvs(size=Msmall, random_state=rng_mcse)   # one independent MC run
    means[r] = s.mean()                                # its point estimate
    mcses[r] = s.std(ddof=1) / np.sqrt(Msmall)         # its self-reported MCSE
print(f"actual SD of the {R} estimates : {means.std(ddof=1):.5f}")
print(f"mean self-reported MCSE        : {mcses.mean():.5f}")
print(f"exact posterior sd / sqrt(M)   : {post.std()/np.sqrt(Msmall):.5f}")
```

The empirical scatter of the 1,000 point estimates is `0.00294`; the average MCSE that a single run reports about itself is `0.00292`, matching the exact $\sigma/\sqrt M = $ `0.00292`. **The formula on one run tells you how wrong that run is likely to be.** Report it always: a posterior mean quoted without its MCSE is a silent overclaim, exactly the habit module 02 flagged when ten million simulated patients pinned a PPV only to its third digit.

**Estimating a number you can also get by quadrature.** To trust the machinery, point it at a target you can compute another way. Take $\mathrm{E}[\sqrt{|Z|}]$ for $Z\sim\mathcal N(0,1)$ — an integral with no tidy closed form worth memorizing, but one-dimensional and smooth, so deterministic quadrature nails it. Compute *both*, and print the quadrature value rather than trusting a remembered constant.

```python
# 09.2 -- MC estimate of E[sqrt|Z|] checked against deterministic quadrature
from scipy import integrate
quad_val, quad_err = integrate.quad(lambda z: np.sqrt(abs(z)) * stats.norm.pdf(z),
                                    -np.inf, np.inf)
Z = rng.standard_normal(1_000_000)
g = np.sqrt(np.abs(Z))
mc_val = g.mean(); mc_se = g.std(ddof=1) / np.sqrt(Z.size)
print(f"quadrature      : {quad_val:.6f}")
print(f"Monte Carlo     : {mc_val:.6f}  +/- {2*mc_se:.6f}  (2 MCSE)")
print(f"|MC - quad|     : {abs(mc_val - quad_val):.6f}")
```

Quadrature returns `0.822179`; Monte Carlo returns `0.821580` with a two-MCSE band of `0.000698`, and the exact value sits inside it (`|MC − quad| = 0.000599`). The MCSE is doing its job: it is not decoration, it is the claim.

**$\pi$ by darts, and the $1/\sqrt M$ wall.** The canonical toy: throw darts uniformly at the unit square, count the fraction landing inside the quarter circle, multiply by 4. The estimator is a proportion, so its error obeys the CLT — and the RMS error should fall exactly like $1/\sqrt M$. Increasing $M$ by 100× should shrink it by 10×.

```python
# 09.2 -- pi by darts: RMS error falls like 1/sqrt(M)
rng_pi = np.random.default_rng(21)
def pi_rms(M, reps):
    errs = [abs(4 * ((p := rng_pi.random((M, 2)))[:, 0]**2 + p[:, 1]**2 <= 1).mean() - np.pi)
            for _ in range(reps)]
    return np.sqrt(np.mean(np.square(errs)))
grid = [100, 1000, 10_000, 100_000]
rms = [pi_rms(M, 200) for M in grid]
for M, e in zip(grid, rms):
    print(f"M={M:>7}: RMS error {e:.5f}   (theory {np.sqrt(np.pi*(4-np.pi)/M):.5f})")
print(f"error ratio M=1e3 -> 1e5: {rms[1]/rms[3]:.2f}  (expect ~10 for a 100x sample)")
```

The measured RMS errors track the theoretical $\sqrt{\pi(4-\pi)/M}$ within the sampling noise of a 200-replication RMS, and the error ratio from $M=10^3$ to $M=10^5$ is `9.69`, the promised factor of ten. Plotted on log-log axes, the errors fall along a line of slope $-\tfrac12$.

```python
# figure: the 1/sqrt(M) convergence wall
fig, ax = plt.subplots()
ax.loglog(grid, rms, "o-", color="C0", label="measured RMS error (pi by darts)")
ref = rms[0] * np.sqrt(grid[0] / np.array(grid))
ax.loglog(grid, ref, "k--", label=r"$\propto 1/\sqrt{M}$ reference (slope $-1/2$)")
ax.set(xlabel="number of draws M", ylabel="RMS error of the estimate",
       title="Monte Carlo error falls like 1/sqrt(M): 100x the work buys 10x the accuracy")
ax.legend()
save(fig, "sqrtM_wall")
```

![Log-log plot of Monte Carlo RMS error against sample size M for the pi-by-darts estimator, falling along a line of slope minus one-half parallel to the 1-over-root-M reference.](figures/09-monte-carlo/sqrtM_wall.png)

That slope of $-\tfrac12$ is the wall the rest of computational Bayes fights against. It is dimension-free — which sounds wonderful until you meet a problem where the naive average needs $10^{10}$ draws to see the event you care about. That is where importance sampling comes in.

## 09.3 Importance sampling, the success case

**Setup.** Estimate $P(Z>4)$ for $Z\sim\mathcal N(0,1)$. The exact answer is `3.167e-05` — three in a hundred thousand. Naive Monte Carlo draws $Z_i\sim\mathcal N(0,1)$ and averages the indicator $\mathbf1[Z_i>4]$. But the event essentially never happens: in $M=10^4$ draws you expect $0.3$ hits, so most runs see *none at all* and confidently report the probability is `0.0000` — the estimator says the event is impossible.

**Predict.** You run naive Monte Carlo at $M=10^5$ (expected hits $\approx 3.2$) twelve independent times. *How many of the twelve estimates land within 10% of the true $3.167\times10^{-5}$?* The naive intuition — "$10^5$ draws is plenty, they should mostly be close" — says ten or eleven. *Reason:* you are trusting the $1/\sqrt M$ wall without noticing that for a rare event the relevant sample size is the *number of hits*, not the number of draws.

```python
# 09.3 -- naive MC for a rare event is a coarse integer lottery
rng_rare = np.random.default_rng(30)
exact = stats.norm.sf(4)
print(f"exact P(Z>4) = {exact:.3e}")
for Mn in (10_000, 100_000):
    hits = [int((rng_rare.standard_normal(Mn) > 4).sum()) for _ in range(12)]
    ests = np.array(hits) / Mn
    within = int(np.sum(np.abs(ests - exact) / exact <= 0.10))
    print(f"M={Mn:>6}: hit counts {hits}")
    print(f"          zero-hit runs {sum(h == 0 for h in hits)}/12,  within 10% of truth {within}/12")
```

**Run → Reconcile.** At $M=10^4$, all `12`/12 runs see zero hits and report the probability as exactly zero. At $M=10^5$ the estimator can only ever return an integer multiple of $10^{-5}$, so the twelve estimates are a coarse lottery spanning $1\times10^{-5}$ to $6\times10^{-5}$ — a sixfold spread — and only `2`/12 land within 10% of the truth. The prediction of "ten or eleven" is badly wrong. The $1/\sqrt M$ law was never violated; the *relative* error of a rare-event estimate is $\approx 1/\sqrt{Mp}$, and with $Mp\approx 3$ expected hits that is a 50%+ error no matter how large $M$ looks.

**The fix.** Sample where the action is. **Importance sampling** rewrites the target expectation as an expectation under a *proposal* density $q$ we can sample from efficiently, correcting for the mismatch with a weight $w(x)=p(x)/q(x)$:

$$\mathrm{E}_p[h(X)] = \int h(x)\,p(x)\,dx = \int h(x)\,\frac{p(x)}{q(x)}\,q(x)\,dx = \mathrm{E}_q\!\big[h(X)\,w(X)\big].$$

For $P(Z>4)$, put the proposal *on top of the rare region*: $q=\mathcal N(4,1)$. Now half the proposal draws exceed 4, every draw is informative, and the weight $w(x)=\phi(x)/\phi(x-4)$ down-weights them back to the true measure.

```python
# 09.3 -- importance sampling nails the rare event with a shifted proposal
rng_is = np.random.default_rng(31)
Mn = 100_000
q = stats.norm(loc=4, scale=1)                     # proposal sits on the rare region
x = q.rvs(size=Mn, random_state=rng_is)
w = stats.norm.pdf(x) / q.pdf(x)                   # importance weights p/q
contrib = (x > 4) * w                              # h(x) * w(x)
is_est = contrib.mean()
is_se = contrib.std(ddof=1) / np.sqrt(Mn)
print(f"IS estimate  = {is_est:.3e}  +/- {2*is_se:.1e}  (2 SE)")
print(f"exact        = {exact:.3e}")
print(f"relative error {abs(is_est-exact)/exact*100:.2f}%   SE ratio naive/IS ~ "
      f"{np.sqrt(exact*(1-exact)/Mn)/is_se:.0f}x")
```

The same $10^5$ draws now give `3.148e-05` with a two-standard-error band of `4.2e-07` — a relative error of `0.60%`, and a standard error roughly `84`× smaller than naive Monte Carlo would achieve with the identical budget. Same number of draws, a thousandfold better answer, because we spent them where the integrand lives. Importance sampling is not a trick for rare events only; it is the reweighting identity, and it reappears whenever you must answer a question about one distribution using samples from another — off-policy reinforcement learning, covariate shift, marginal-likelihood estimation.

## 09.4 Importance sampling, the silent failure  *(marquee)*

The reweighting identity is exact for *any* proposal $q$ with $q(x)>0$ wherever $p(x)h(x)\neq0$. "Exact in expectation" is a trap: the estimator can have **infinite variance**, in which case it converges — eventually, arbitrarily slowly — while every finite run looks tidy and lies. The alarm is not the estimate. It is the weights.

**The diagnostic: effective sample size.** Weighted draws are worth less than iid draws because the weights are uneven — a few large weights dominate the sum and the rest contribute nothing. Kong's effective sample size makes "how many iid draws is this worth?" precise. For unnormalized weights $w_i = p(x_i)/q(x_i)$,

$$\boxed{\ \mathrm{ESS} = \frac{\big(\sum_i w_i\big)^2}{\sum_i w_i^2} = \frac{M}{1+\mathrm{cv}^2},\quad \mathrm{cv}^2 = \frac{\mathrm{Var}[w]}{\overline w^{\,2}}\ }\qquad \Big(\text{equivalently } \mathrm{ESS}=1\big/\textstyle\sum_i \bar w_i^2,\ \bar w_i = w_i/\!\sum_j w_j\Big),$$

where $\mathrm{cv}^2$ is the squared coefficient of variation of the **unnormalized** weights. Read it directly: equal weights give $\mathrm{cv}^2=0$ and $\mathrm{ESS}=M$; one weight carrying everything gives $\mathrm{ESS}\to1$. It is always true that $\mathrm{ESS}\le M$.

> **Name-collision warning.** The booklet (ch. 4) writes "$\mathrm{ESS}\ge n$" — the *opposite* inequality. That $\mathrm{ESS}$ is a different animal: it is the *prior-augmented sample size* of a conjugate analysis, $n + \sigma^2/\delta^2$, counting the pseudo-observations a proper prior contributes (module 05's $\kappa$). Same three letters, opposite direction. The Monte-Carlo ESS here counts *effective draws from a weighted sample* and can only ever be $\le M$. Do not conflate them.

**Setup.** Target the Student-$t_3$ distribution (module 03's heavy tail: $\nu=3$, so $\mathrm{Var}=\nu/(\nu-2)=3$, and $\mathrm{E}[\theta^2]=3$ is the truth we want). Propose from $q=\mathcal N(0,1)$. Both are unit-ish bells centered at 0; the proposal looks like a perfectly reasonable stand-in.

**Predict.** You draw $M=10^5$ points from $\mathcal N(0,1)$ and weight them toward $t_3$. *Guess the effective sample size of these $10^5$ weighted draws.* The naive read of the two overlaid bells — "they match well, ESS should be most of $10^5$, maybe 80,000" — competes with the cynic's "the tails are wrong, it'll collapse to a handful." *Reason:* both sides are trusting the single-sample ESS as a safety certificate. Commit to a number before running — and notice that whatever number you pick, you are about to treat it as that certificate.

```python
# 09.4 -- N(0,1) proposal for a t3 target: the weights have INFINITE variance
def ess_kong(w):
    return w.sum()**2 / (w**2).sum()

rng_fail = np.random.default_rng(40)
target = stats.t(df=3)
proposal = stats.norm(0, 1)
M = 100_000
x = proposal.rvs(size=M, random_state=rng_fail)
w = target.pdf(x) / proposal.pdf(x)                 # unnormalized weights
cv2 = w.var() / w.mean()**2
wbar = w / w.sum()                                  # normalized weights
est_var = np.sum(wbar * x**2)                       # self-normalized IS estimate of E[theta^2]
print(f"ESS (Kong)        = {ess_kong(w):,.0f}   = {100*ess_kong(w)/M:.1f}% of M")
print(f"M/(1+cv^2)        = {M/(1+cv2):,.0f}   (cv^2 = {cv2:.2f})")
print(f"1/sum(wbar^2)     = {1/np.sum(wbar**2):,.0f}   (three routes agree)")
print(f"max single weight = {wbar.max()*100:.2f}% of total weight")
print(f"SNIS  E[theta^2]  = {est_var:.3f}   (truth 3.000)")
```

**Run.** At $M=10^5$ the three equivalent ESS formulas agree at `34,698` — about `34.7%` of the draws still effective, with the largest single weight carrying only `0.29%` of the total. **The diagnostic looks survivable.** And yet the self-normalized estimate of $\mathrm{E}[\theta^2]$ comes back `1.693` against a truth of 3 — wrong by 44%. Anyone who read "ESS = 35k, a third of our draws, we're fine" just shipped a badly biased number.

**Reconcile.** The variance of these weights is *infinite*. Under $q=\mathcal N(0,1)$, $\mathrm{E}_q[w^2] = \int (t_3(x)/\phi(x))^2\,\phi(x)\,dx = \int t_3(x)^2/\phi(x)\,dx$, and since $t_3$ has polynomial tails ($\sim x^{-4}$) while $\phi$ decays like $e^{-x^2/2}$, the integrand behaves like $x^{-8}e^{x^2/2}\to\infty$ — the integral diverges. The pathology is precisely that the proposal has *lighter tails than the target*: out where $t_3$ still has real mass, $\mathcal N(0,1)$ has essentially none, so the correct weight there is astronomical — but the proposal almost never visits, so a finite sample simply *misses the mass that matters* and reports a calm ESS and a low, confident, wrong answer. The tell is not any single ESS; it is that the **ESS *fraction* collapses as $M$ grows** — absolute ESS still rises, but *sublinearly* — where a healthy estimator accumulates effective samples linearly and holds ESS/$M$ flat.

```python
# 09.4 -- the infinite-variance signature: median ESS fraction COLLAPSES as M grows
rng_sweep = np.random.default_rng(41)
rng_safe = np.random.default_rng(43)
Ms = [10**3, 10**4, 10**5, 10**6]

def median_ess_frac(M, gen, prop_dist, tgt_dist, reps=25):
    fr = []
    for _ in range(reps):                               # replicate: ESS itself is random here
        xr = prop_dist.rvs(size=M, random_state=gen)
        fr.append(100 * ess_kong(tgt_dist.pdf(xr) / prop_dist.pdf(xr)) / M)
    return float(np.median(fr))

fail_fracs = [median_ess_frac(M, rng_sweep, proposal, target) for M in Ms]   # light proposal
safe_fracs = [median_ess_frac(M, rng_safe, target, proposal) for M in Ms]    # heavy proposal
print("median ESS/M over 25 reps:")
for M, f, s in zip(Ms, fail_fracs, safe_fracs):
    print(f"  M={M:>8}: failure (light proposal) {f:6.2f}%   safe (heavy proposal) {s:6.2f}%")
# the SAFE direction also recovers the answer:
xs = target.rvs(size=10**5, random_state=rng_safe)
ws = proposal.pdf(xs) / target.pdf(xs)
print(f"safe-direction SNIS E[theta^2] = {np.sum((ws/ws.sum())*xs**2):.2f} (truth 1.00)")
```

Averaged over replications (a single run's ESS is itself random here), the sweep prints the collapse: the median ESS fraction falls `62.65`% → `44.38`% → `27.76`% → `12.27`% as $M$ climbs from $10^3$ to $10^6$ — the more you sample, the smaller the *fraction* that carries real weight, because a larger sample is more likely to land a draw far out in the tail whose monster weight seizes the sum. Flip the proposal and target — sample from the *heavier* $t_3$ to estimate a Normal expectation — and the weights are bounded, the median ESS holds flat near `92.1`% of $M$ at every scale, and $\mathrm{E}[\theta^2]$ recovers the truth `1.00`. **The rule that survives:** your proposal's tails must be at least as heavy as the target's. Sample from the fat distribution to learn about the thin one, never the reverse.

```python
# figure: the weight histogram and the ESS-collapse signature (reuses the sweep above)
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].hist(np.log10(wbar[wbar > 0] + 1e-300), bins=60, color="C3")
ax[0].set(title="Failure: normalized weights span orders of magnitude",
          xlabel="log10(normalized weight)", ylabel="count of draws")
ax[1].semilogx(Ms, fail_fracs, "o-", color="C3", label="light proposal (fails)")
ax[1].semilogx(Ms, safe_fracs, "s-", color="C0", label="heavy proposal (safe)")
ax[1].set(title="Median ESS fraction collapses with M when weights have infinite variance",
          xlabel="number of draws M", ylabel="median ESS as % of M", ylim=(0, 100))
ax[1].legend()
save(fig, "is_weights")
```

![Left: histogram of log10 normalized importance weights for the t3-target N(0,1)-proposal case, spread across many orders of magnitude. Right: ESS as a percentage of M against M on a log axis, collapsing toward zero for the light proposal while the heavy proposal stays near 90 percent.](figures/09-monte-carlo/is_weights.png)

## 09.5 Rejection sampling: exactness bought by acceptance

Importance sampling reweights; **rejection sampling** instead produces *exact* draws from the target by throwing some proposals away. Find an envelope constant $C$ with $p(x)\le C\,q(x)$ everywhere, draw $x\sim q$, and accept it with probability $p(x)/(C\,q(x))$. Accepted draws are exactly distributed as $p$ — no weights, no bias. The price is stated in one number: the **acceptance probability is $1/C$**, and the number of proposals until one is accepted is Geometric, so you burn $C$ proposals per kept draw on average (booklet ch. 5: $E[\text{trials}]=C$).

```python
# 09.5 -- rejection sampling from Beta(2,5) under a uniform envelope
rng_rej = np.random.default_rng(50)
tgt = stats.beta(2, 5)
mode = (2 - 1) / (2 + 5 - 2)                         # Beta(2,5) mode = 0.2
C = tgt.pdf(mode)                                    # tightest constant envelope over U(0,1)
N = 200_000
x = rng_rej.random(N)                                # proposals ~ U(0,1)
u = rng_rej.random(N)
accept = u <= tgt.pdf(x) / C                         # accept w.p. p(x)/(C*q(x)), q=1
kept = x[accept]
print(f"envelope C = {C:.4f},  theoretical acceptance 1/C = {1/C:.4f}")
print(f"empirical acceptance = {accept.mean():.4f}  ({accept.sum():,} of {N:,})")
print(f"accepted-sample mean {kept.mean():.4f} vs exact {tgt.mean():.4f};  "
      f"KS p-value {stats.kstest(kept, tgt.cdf).pvalue:.3f}")
```

The envelope constant is $C=$ `2.4576`, predicting acceptance $1/C=$ `0.4069`; the run accepts `0.4068` of proposals, the accepted mean `0.2852` matches the exact Beta mean `0.2857`, and a Kolmogorov–Smirnov test finds no discrepancy (p `0.289`). Rejection is beautiful when you can find a tight envelope, and it is the exactness engine inside many samplers — but the acceptance rate is its Achilles heel. A loose envelope (large $C$) wastes almost everything, and in high dimension $C$ grows exponentially: sampling a $d$-ball by rejecting from its bounding cube accepts a vanishing fraction as $d$ climbs (Exercise 09.2). That exponential wall is exactly why the next module abandons independent proposals for a *Markov chain* that walks toward the mass instead of guessing at it.

## 09.6 Likelihood-free inference: rejection-ABC

Sometimes you can *simulate* data from a model but cannot write its likelihood — the forward map is a black box (a physics simulator, a stochastic process, a generative network). Approximate Bayesian Computation turns simulation alone into inference. **The whole idea is one sentence: condition on a neighborhood of the observed data instead of the data itself.** Draw a parameter from the prior, simulate a dataset, and keep the parameter if a summary statistic of the simulation lands within tolerance $\varepsilon$ of the observed summary. Send $\varepsilon\to0$ and you recover the exact posterior; keep it loose and you trade bias for acceptances.

To *see* that it works, use a model where the exact posterior is known: Binomial with a $\mathrm{Beta}(1,1)$ prior. Observe $y=15$ successes in $n=50$ — the exact posterior is $\mathrm{Beta}(16,36)$.

**Predict.** As you shrink $\varepsilon$ from loose to tight, two things move: the ABC posterior's *shape* relative to the exact Beta, and the *acceptance rate*. *Predict the direction of each.* The intuition "tighter tolerance = better answer" is right about the shape; the reason to run it is to feel the cost — *how fast* does acceptance fall? Commit: at $\varepsilon = 0.02$, will you still accept more than 1 in 5 proposals?

```python
# 09.6 -- rejection-ABC for a Binomial theta; exact Beta posterior known for comparison
rng_abc = np.random.default_rng(60)
n_trials, y_obs = 50, 15
exact_post = stats.beta(1 + y_obs, 1 + n_trials - y_obs)      # Beta(16, 36)
Nabc = 200_000
theta_prop = rng_abc.random(Nabc)                            # prior ~ U(0,1)
y_sim = rng_abc.binomial(n_trials, theta_prop)               # simulate the summary stat
print(f"exact posterior Beta(16,36): mean {exact_post.mean():.4f}, sd {exact_post.std():.4f}")
abc_keep = {}
for eps in (0.20, 0.10, 0.02):
    keep = np.abs(y_sim - y_obs) <= eps * n_trials           # accept within a neighborhood
    abc_keep[eps] = theta_prop[keep]
    print(f"eps={eps:.2f}: acceptance {keep.mean():.4f} ({keep.sum():>6,} kept), "
          f"ABC mean {theta_prop[keep].mean():.4f}, ABC sd {theta_prop[keep].std():.4f}")
```

**Run → Reconcile.** The ABC posterior mean is close to the exact `0.3077` at every tolerance — the mean is robust — but the *spread* is the tell. At $\varepsilon=0.20$ the ABC standard deviation is `0.1314`, more than double the exact `0.0634`: a loose neighborhood keeps parameters whose simulations only vaguely resemble the data, inflating the posterior. Tightening to $\varepsilon=0.10$ pulls it to `0.0871`, and $\varepsilon=0.02$ to `0.0653`, essentially the exact width. And the predicted cost arrives: acceptance falls from `0.4096` to `0.2142` to `0.0586` — no, you do *not* still accept 1 in 5 at $\varepsilon=0.02$; you accept about 1 in 17, and driving $\varepsilon$ to zero would collapse acceptance to the probability of simulating $y=15$ exactly. That is the ABC bargain in one figure: accuracy is bought with acceptances, the same exactness-versus-efficiency trade rejection sampling charged in §09.5.

```python
# figure: ABC posterior tightening onto the exact Beta as epsilon shrinks
fig, ax = plt.subplots()
grid = np.linspace(0, 0.7, 300)
for eps, c in zip((0.20, 0.10, 0.02), ("C0", "C2", "C3")):
    ax.hist(abc_keep[eps], bins=40, density=True, histtype="step", lw=2,
            color=c, label=f"ABC eps={eps}")
ax.plot(grid, exact_post.pdf(grid), "k--", lw=2, label="exact Beta(16,36) posterior")
ax.set(xlabel=r"$\theta$", ylabel="posterior density",
       title="ABC converges to the exact posterior as the tolerance shrinks",
       xlim=(0, 0.7))
ax.legend()
save(fig, "abc")
```

![Posterior densities for theta: three ABC histograms at tolerances 0.20, 0.10, 0.02 progressively narrowing onto the black dashed exact Beta(16,36) curve.](figures/09-monte-carlo/abc.png)

Modern likelihood-free inference replaces the reject-on-a-summary step with a neural density estimator trained on simulations (simulation-based inference / neural posterior estimation), sidestepping ABC's curse — as $\varepsilon\to0$ acceptance dies, and with many summary statistics no simulation ever lands inside the neighborhood. We meet neural SBI as a Bayesian lens in module 25; the conditioning-on-a-neighborhood idea is the seed.

## Bridge — importance weighting and averaging are everywhere

Two machine-learning practices are exactly the machinery of this module wearing other clothes.

> **MC-dropout is Monte Carlo integration.** Leaving dropout *on* at test time and averaging $T$ stochastic forward passes, $\hat p(y\mid x)=\frac1T\sum_t p(y\mid x, \text{mask}_t)$, is nothing but a $T$-sample Monte Carlo estimate of a predictive expectation over a distribution on the network's weights (Gal & Ghahramani, by concept; **label: heuristic** — that the induced weight distribution is a genuine posterior is an approximation, formalized in module 25). The MCSE of §09.2 is why more passes give a smoother, better-calibrated predictive, and why a handful of passes is noisy: you are averaging draws, and the error falls like $1/\sqrt T$.

> **Off-policy evaluation is importance sampling.** In reinforcement learning you have trajectories collected under a *behavior* policy $\beta$ but want the expected return of a *target* policy $\pi$. The estimator reweights each trajectory by the policy ratio $\prod_t \pi(a_t\mid s_t)/\beta(a_t\mid s_t)$ — the importance weight of §09.3, one factor per step. And it fails the same way: when $\pi$ and $\beta$ diverge the weights explode, ESS collapses, and the value estimate becomes high-variance and untrustworthy (Exercise 09.3). Practitioners clip or truncate the weights for exactly the reason we diagnose ESS — trading a little bias for survivable variance.

## Pitfalls

- **Reporting an estimate without its MCSE.** A posterior mean, a $P(\theta>c)$, an expected loss — each is a random quantity with error $s/\sqrt M$. Omitting it is a silent overclaim; for rare events, where the relative error is $\approx 1/\sqrt{Mp}$, the "large" $M$ can still mean three effective observations (§09.3).
- **Trusting a single-sample importance-sampling ESS.** When the weights have infinite variance, one finite run reports a calm ESS and a badly biased estimate (§09.4: ESS 35% of $M$, answer wrong by 44%). The robust alarm is the ESS *fraction* collapsing as $M$ grows (ESS rising only sublinearly), plus a weight histogram spanning many orders of magnitude and a max-weight share that is not tiny.
- **A proposal with lighter tails than the target.** This is the cardinal importance-sampling sin: sample from the heavy distribution to learn about the light one, never the reverse. A Normal proposal for a Student-$t$ target has infinite-variance weights; the reverse is fine.
- **Assuming rejection sampling scales.** Acceptance is $1/C$, and the envelope constant $C$ grows exponentially with dimension. What is instant in 1-D is hopeless in 20-D (Exercise 09.2) — the reason module 10 switches to Markov chains.
- **Pushing ABC tolerance to zero without watching acceptance.** Tighter $\varepsilon$ removes bias but collapses acceptance toward the probability of an exact-match simulation; with many summary statistics it collapses to zero. Match $\varepsilon$ to your simulation budget, and reduce the summary's dimension.

## Exercises

**Exercise 09.1 — How many draws to see the rare event? *(surprising)***
*Setup:* You want to estimate $P(Z>4)=$ `3.167e-05` by *naive* Monte Carlo to a relative MCSE of 10% — that is, MCSE $\le 0.1\times p$.
*Predict:* How many draws $M$ does that take — thousands, millions, or hundreds of millions?
*Reason:* You are inclined to think "$10^5$ was almost enough," extrapolating from problems where $p$ is order 1.
*Run:*
```python
p = float(stats.norm.sf(4))
# naive MC variance of the indicator is p(1-p)/M; want sqrt(p(1-p)/M) <= 0.1*p
M_needed = (1 - p) / (0.01 * p)
print(f"M needed for 10% relative MCSE: {M_needed:,.0f}")
```
<details><summary>Reconcile</summary>

You need `3,157,339` draws — about 3.2 million — to pin a probability of $3\times10^{-5}$ to 10%, because naive MC's relative error is $\sqrt{(1-p)/(Mp)}$ and $p$ sits in the denominator. Rarer events cost inversely in draws. Importance sampling (§09.3) reached the same precision with $10^5$ draws, a 30× saving here and unboundedly more as $p$ shrinks. The lesson: the cost of naive Monte Carlo is set by the *rarity of what you're measuring*, not the size of the sample space — and that is precisely when reweighting or a well-placed proposal stops being optional.
</details>

**Exercise 09.2 — Rejection sampling hits the curse of dimensionality. *(surprising, ML)***
*Setup:* Sample uniformly from the unit $d$-ball by rejecting uniform draws from the bounding cube $[-1,1]^d$: accept if $\|x\|\le1$. The acceptance rate is the ball's volume over the cube's, $V_d = \pi^{d/2}/\big(2^d\,\Gamma(d/2+1)\big)$.
*Predict:* At $d=10$, what fraction of proposals are accepted — about 1 in 3, 1 in 50, or 1 in 400?
*Reason:* Low-dimensional intuition ("a ball fills most of its box") — true at $d=2$ (78.5%), and you expect a gentle decline.
*Run:*
```python
from scipy.special import gamma as G
for d in (2, 5, 10, 20):
    vol = np.pi**(d/2) / (2**d * G(d/2 + 1))
    print(f"d={d:>2}: acceptance {vol:.6f}  ->  {1/vol:,.0f} proposals per kept draw")
```
<details><summary>Reconcile</summary>

At $d=10$ acceptance is `0.002490` — about 1 in `402`, far worse than the naive guess; by $d=20$ it is 1 in 40 million. The ball's volume concentrates away from the corners of the cube as $d$ grows, so almost every uniform proposal is rejected — the same high-dimensional emptiness that will define the "typical set" in module 12. Independent proposal-and-reject is doomed in high dimension no matter how you dress it; you must *walk* toward the mass with a Markov chain (module 10) or exploit *geometry* with gradients (module 12). This is the structural reason the course pivots from independent Monte Carlo to MCMC.
</details>

**Exercise 09.3 — Off-policy evaluation and weight collapse. *(ML bridge)***
*Setup:* A behavior policy takes a binary action with $\beta=P(a{=}1)=0.5$; the target policy uses $\pi=P(a{=}1)=0.9$. Over a length-$H$ episode the trajectory importance weight is $\prod_{t=1}^H \pi(a_t)/\beta(a_t)$ with $a_t\sim\beta$.
*Predict:* At horizon $H=20$, over $10^4$ episodes, what is the effective sample size — most of $10^4$, a few hundred, or single digits?
*Reason:* "Only a 0.4 gap in action probability per step — surely the weights stay mild."
*Run:*
```python
rng_ope = np.random.default_rng(70)
beta_p, pi_p, H, N = 0.5, 0.9, 20, 10_000
a = rng_ope.random((N, H)) < beta_p                          # actions ~ behavior policy
ratio = np.where(a, pi_p / beta_p, (1 - pi_p) / (1 - beta_p))
w = ratio.prod(axis=1)                                       # trajectory weights
print(f"ESS = {w.sum()**2 / (w**2).sum():.1f} out of {N}  "
      f"({100*w.sum()**2/(w**2).sum()/N:.2f}%)")
print(f"max single weight share {w.max()/w.sum()*100:.1f}%")
```
<details><summary>Reconcile</summary>

The ESS collapses to about `7.9` out of 10,000 — under a tenth of one percent — and a single dominant trajectory (here one with 18 of 20 target-favored actions, weight $1.8^{18}\cdot0.2^{2}\approx 1{,}574$) hoards `17.5`% of the total weight. The theoretical worst case, an all-1 trajectory, would weigh $1.8^{20}\approx 127{,}000$ — but with probability $0.5^{20}\approx 9.5\times10^{-7}$ under the behavior policy it essentially never occurs in $10^4$ episodes, which is §09.4's pathology restated: the heaviest correct weights sit on trajectories the proposal (behavior policy) almost never produces. Per-step ratios of $1.8$ and $0.2$ compound *multiplicatively* over the horizon, so the weight variance explodes with $H$: this is §09.4's infinite-variance pathology on a conveyor belt. It is why raw off-policy evaluation is unusable at long horizons and why practitioners clip weights, use per-decision or doubly-robust estimators, or keep $\pi$ close to $\beta$. The ESS diagnostic you built for importance sampling is the *same* early-warning system a reinforcement-learning engineer needs.
</details>

**Exercise 09.4 — Antithetic variates help — except when they hurt. *(surprising)***
*Setup:* Antithetic sampling pairs each draw $Z_i$ with its mirror $-Z_i$ and averages $\tfrac12(g(Z_i)+g(-Z_i))$ over $M/2$ pairs — the same number of function evaluations as $M$ independent draws. You apply it to two integrands: $g(z)=e^{z}$ (monotone, truth $e^{1/2}\approx1.6487$) and $g(z)=z^2$ (even, truth $1$).
*Predict:* Does antithetic sampling reduce the variance for *both*, for *one*, or does it make one *worse*?
*Reason:* "Variance reduction is a free lunch — pairing draws can only help." — the assumption that the trick is unconditionally good.
*Run:*
```python
rng_av = np.random.default_rng(80)
M = 1_000_000
def antithetic_reduction(fn):
    z = rng_av.standard_normal(M)
    std_var = fn(z).var(ddof=1) / M                     # variance of the standard-MC mean
    zh = rng_av.standard_normal(M // 2)
    anti = 0.5 * (fn(zh) + fn(-zh))                     # antithetic pairs, same budget
    anti_var = anti.var(ddof=1) / (M // 2)
    return std_var, anti_var, std_var / anti_var
for name, fn in [("e^Z  (monotone)", np.exp), ("Z^2  (even)", lambda z: z**2)]:
    s, a, r = antithetic_reduction(fn)
    print(f"{name}: std var {s:.3e}  anti var {a:.3e}  reduction {r:.2f}x")
```
<details><summary>Reconcile</summary>

For the monotone $e^{Z}$ the variance drops by `1.57`×; for the even $z^2$ it *rises* — reduction `0.50`×, meaning antithetic sampling **doubles** the variance. The mechanism is one line: $\mathrm{Var}\big[\tfrac12(g(Z)+g(-Z))\big]=\tfrac12\mathrm{Var}[g]\,(1+\rho)$ with $\rho=\mathrm{Corr}(g(Z),g(-Z))$, so the reduction factor is $1/(1+\rho)$. A *monotone* $g$ makes the mirror pair negatively correlated ($\rho<0$) — a high draw and its low mirror cancel — and you win. An *even* $g$ makes them identical ($\rho=+1$): the mirror draw is perfectly redundant, so you have halved your independent samples for nothing and doubled the variance. The free lunch is real but conditional: antithetic (and its cousins — control variates, stratification, common random numbers) exploit *structure* in how the integrand depends on the noise. Reach for the MCSE first; it tells you whether a variance-reduction trick actually helped, rather than assuming it did.
</details>

## Takeaways

- **Samples are the lingua franca.** Given draws from a posterior, every summary — mean, tail probability, credible interval, any transformed expectation, any expected loss — is one `mean()` or `quantile()` away. This is why producing draws (MCMC, next) is worth the machinery.
- **The MCSE is the result, not an ornament.** $\mathrm{MCSE}=s/\sqrt M$, computed from the one run you have, predicts that run's scatter; error falls only as $1/\sqrt M$, so 10× precision costs 100× draws. Report it always (module 02's promise, kept).
- **Naive Monte Carlo dies on rare events.** Relative error is $\approx1/\sqrt{Mp}$; at $P(Z{>}4)=$ `3.167e-05` a $10^5$-draw estimate is a coarse integer lottery. Importance sampling with a proposal placed on the event nails it with the same budget.
- **Importance sampling fails silently; the weights are the alarm.** $\mathrm{ESS}=(\sum w_i)^2/\sum w_i^2 = M/(1+\mathrm{cv}^2)\le M$. A single-run ESS can look healthy while the answer is 44% wrong — the true tell is the ESS *fraction* collapsing as $M$ grows (sublinear ESS), the infinite-variance signature.
- **The tail rule:** the proposal's tails must be at least as heavy as the target's. Sample from the fat distribution to learn about the thin one, never the reverse.
- **Rejection sampling buys exactness at acceptance rate $1/C$**, and $C$ grows exponentially with dimension — the wall that forces the move to Markov chains (module 10).
- **ABC is conditioning on a neighborhood:** simulate from the prior, keep parameters whose simulated summary lands within $\varepsilon$; $\varepsilon\to0$ recovers the exact posterior but collapses acceptance — accuracy is paid for in accepted draws. The seed of neural simulation-based inference (module 25).

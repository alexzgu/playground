# 02. Conditioning Is Inference

> **Spine.** Bayes' rule is the ratio of joints; posterior odds = prior odds × likelihood ratio.
> **Which line?** Line 2. This is *the* module for line 2 (inference = conditioning); the enumeration engine below is its most literal implementation, and lines 3–4 ride on top of it.
> **Promise.** After this module you can turn any finite "hypotheses × observables" model into a posterior with one array operation, read evidence off in additive log-odds, and explain why the *protocol* you condition under — not just the event — determines the answer.
> **Prereqs.** Modules 00, 01. **Runtime.** ~5–10 s measured (load-dependent on the 2-CPU box).
> **Sources.** C-B §1.3 (conditional probability, Bayes' rule, Three Prisoners); booklet ch. 2.

## 02.1 One function is the whole chapter

Line 1 says a model is a joint distribution $p(\text{unknowns}, \text{knowns})$. Line 2 says inference is conditioning: $p(\text{unknowns}\mid\text{knowns})$. When the unknowns live in a *finite* set of hypotheses $\{h_1,\dots,h_H\}$ and the data is one observed value $o^\*$ from a finite set of observables, "conditioning" stops being philosophy and becomes arithmetic you can do in three lines: lay out the joint $p(h,o)=p(h)\,p(o\mid h)$ as a table, keep the single column $o=o^\*$ you actually observed, and renormalize that column so it sums to one.

That renormalized column is the posterior. Everything else in this module — a medical test, an enemy tank count, Monty Hall — is this one operation with different tables.

We assume finite discrete probability as a prerequisite: a sample space, $P(A\mid B)=P(A\cap B)/P(B)$ for $P(B)>0$ (C-B Def. 1.3.2), the law of total probability $p(o)=\sum_h p(o\mid h)\,p(h)$, and counting ($\binom{n}{k}$, sampling without replacement). If any of that is rusty, C-B §1.2–1.3 is the half-page refresher; we will not re-derive it. What we *will* do is make the conditioning step mechanical.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "02-conditioning-is-inference"     # this module's figure dir
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

Here is the engine. It is deliberately tiny — arrays in, posterior out — so later modules can quote it verbatim.

```python
def condition(prior, likelihood, obs):
    """Exact discrete Bayes by enumerating the joint over finite hypotheses.

    prior:      shape (H,)    P(h)        -- one probability per hypothesis
    likelihood: shape (H, O)  P(o | h)    -- row h is that hypothesis's
                                             sampling distribution over obs
    obs:        int           index of the observed column o*
    returns:    shape (H,)    P(h | o*)   == the observed column, renormalized

    The denominator col.sum() is the evidence p(o*) = sum_h p(h) p(o*|h);
    we will reuse it as the marginal likelihood for model comparison (M17).
    """
    prior = np.asarray(prior, float)
    joint = prior[:, None] * np.asarray(likelihood, float)   # p(h, o) for every cell
    col = joint[:, obs]                                       # the one column we saw
    return col / col.sum()                                    # divide by p(o*)

# self-check: uniform prior + symmetric likelihood -> posterior still sums to 1
_p = condition([0.5, 0.5], [[0.9, 0.1], [0.2, 0.8]], obs=0)
print(f"engine self-check: posterior {np.round(_p, 4)} sums to {_p.sum():.1f}")
```

The comment names the load-bearing fact: the column sum is the *evidence* $p(o^\*)$, the same number that will grade competing models in module 17. Conditioning and model comparison are the same denominator seen from two angles.

## 02.2 The medical test: a base rate you cannot outvote

Module 00 already caught you here: the 99%-sensitive, 95%-specific test at prevalence $0.001$, the naive "positive means ~0.9" guess, and the deflating truth PPV $=$ `0.0194`. That reveal is spent — you cannot be surprised by the same number twice. So the test returns for two *new* jobs: first as a known answer that certifies the engine (if `condition` cannot reproduce module 00's hand computation, nothing downstream deserves trust), and then as the setting for a question module 00 never asked.

**Predict (commit now).** Keep the test fixed at 99%/95% and let the *prevalence* vary: at what prevalence does a positive result finally mean better-than-even odds of disease — PPV $\ge 0.5$? One in ten thousand? One in a thousand? One in a hundred? Commit to a number before running.

**Reason.** The intuition being tested: "a 20-fold evidence multiplier is a lot, so surely a positive clears 50% well before prevalence reaches a percent." You are extrapolating the strength of the test instead of computing where it balances the base rate.

**Run.** Two hypotheses ($\{\text{disease},\text{healthy}\}$), two observables ($\{+,-\}$). The engine's joint table, the odds form, and the prevalence sweep:

```python
sens, spec, prev = 0.99, 0.95, 0.001
print(f"sens={sens}  spec={spec}  prev={prev}")

prior = np.array([prev, 1 - prev])                 # P(disease), P(healthy)
likelihood = np.array([[sens,     1 - sens],       # P(+|dis), P(-|dis)
                       [1 - spec, spec]])          # P(+|heal), P(-|heal)
post = condition(prior, likelihood, obs=0)         # obs=0 is the "+" column
print(f"PPV via the engine = {post[0]:.4f}   (module 00's hand value: 0.0194)")

# same computation as odds x likelihood ratio
prior_odds = prev / (1 - prev)
LR = sens / (1 - spec)
post_odds = prior_odds * LR
print(f"prior odds = {prev}/{1-prev:.3f} = {prior_odds:.6f}")
print(f"likelihood ratio = {sens}/{1-spec:.2f} = {LR:.1f}")
print(f"posterior odds = {post_odds:.4f}  ->  PPV = {post_odds/(1+post_odds):.4f}")

# where does the test finally become convincing? PPV = 0.5 at prevalence:
p_half = (1 - spec) / (sens + (1 - spec))
print(f"prevalence at which PPV = 0.5 : {p_half:.3f}")

# PPV as a function of prevalence (the base-rate curve)
pv = np.logspace(-4, 0, 400)
ppv_curve = sens * pv / (sens * pv + (1 - spec) * (1 - pv))
fig, ax = plt.subplots()
ax.semilogx(pv, ppv_curve, color="C1", label="PPV(prevalence)")
ax.axvline(prev, color="black", ls="--", lw=1)
ax.plot([prev], [post[0]], "o", color="C3", zorder=5)
ax.annotate(f"prevalence {prev} → PPV {post[0]:.3f}",
            xy=(prev, post[0]), xytext=(prev*3, 0.45),
            arrowprops=dict(arrowstyle="->", color="C3"))
ax.set_xlabel("disease prevalence (log scale)")
ax.set_ylabel("P(disease | positive test)")
ax.set_title("A 99%/95% test is nearly useless at low prevalence")
ax.legend()
save(fig, "ppv_vs_prevalence")
```

The engine reproduces module 00's hand value exactly: `0.0194`, from a two-line joint table instead of a bespoke calculation. The mechanism is worth restating once in counting terms: out of every 100,000 people tested at this prevalence, roughly 100 are sick and 99 of them test positive; but 5% of the 99,900 healthy people — about 4,995 — also test positive. The positives are swamped 50-to-1 by false alarms.

**Reconcile.** The crossover prints at prevalence `0.048` — about **one in 21**. If you guessed a fraction of a percent, your intuition extrapolated the test's strength ("multiplies odds 20-fold") without doing the balance-point arithmetic: PPV $=0.5$ means posterior odds $=1$, which needs prior odds $=1/\text{LR}=1/19.8$, i.e. prevalence $\approx 1/20.8$. The base rate is not a nuisance term you can outvote with a good test — it sets the stage the likelihood performs on, and this test needs the disease to be *twenty times more common than most screening settings* before a positive is even a coin flip. The curve in the figure makes the dependence a shape: PPV stays pinned near zero across the entire low-prevalence range where screening actually happens. Same test, same 99%/95%, wildly different meaning depending on who you screen.

![Positive predictive value as a function of disease prevalence for a 99%-sensitive, 95%-specific test; the curve is pinned near zero across the whole low-prevalence range and reaches 0.5 only near prevalence 0.048, with the operating point (prevalence 0.001, PPV 0.019) marked.](figures/02-conditioning-is-inference/ppv_vs_prevalence.png)

### The odds form: evidence is a multiplier

The odds computation prints the same `0.0194`, and it is worth dwelling on because it is the form you will actually reason with. Writing $O(\cdot)$ for odds and $\text{LR}=p(o^\*\mid h_1)/p(o^\*\mid h_2)$ for the likelihood ratio between two hypotheses,

$$\underbrace{O(\text{disease}\mid +)}_{\text{posterior odds}} \;=\; \underbrace{O(\text{disease})}_{\text{prior odds}} \times \underbrace{\frac{P(+\mid\text{disease})}{P(+\mid\text{healthy})}}_{\text{likelihood ratio}} \;=\; \frac{0.001}{0.999}\cdot\frac{0.99}{0.05}.$$

Prior odds `0.001001`, times a likelihood ratio of `19.8`, gives posterior odds `0.0198` — the same PPV once you convert odds back to probability. The data's entire contribution is that one multiplier, the likelihood ratio: how much more often a positive arises under disease than under health. A likelihood ratio of `19.8` is genuinely strong evidence — it multiplies your odds twentyfold — and it *still* loses, because it started a thousandfold behind. Strong evidence and a strong conclusion are different things; the prior is the other factor.

### The same number from ten million patients

The hand calculation is exact. A simulation is the gut check that we built the table correctly — and, at this prevalence, a lesson in how hard rare events are to estimate.

```python
gen = np.random.default_rng(SEED)         # local generator: reproducible in isolation
N = 10_000_000
has_disease = gen.random(N) < prev
tests_pos = np.where(has_disease,
                     gen.random(N) < sens,          # sick: positive w.p. sensitivity
                     gen.random(N) < (1 - spec))     # healthy: positive w.p. 1-specificity
ppv_sim = has_disease[tests_pos].mean()
n_pos = int(tests_pos.sum())
se = np.sqrt(ppv_sim * (1 - ppv_sim) / n_pos)        # Monte Carlo standard error
print(f"simulated PPV over {N:,} patients = {ppv_sim:.4f}  (2*SE = {2*se:.4f})")
print(f"exact PPV = {post[0]:.4f}  (lands inside the simulation's error bar)")
```

Ten million patients give `0.0197`, with a two-standard-error Monte Carlo band of `0.0004` — the exact `0.0194` sits inside it. Notice how loose that is: ten million draws pin the answer only to about three significant figures, because only ~10,000 of those patients were actually sick, and the PPV is a ratio dominated by that small count. Rare-event estimation is expensive; the error bar on a simulation is not optional bookkeeping, it is the result. We report it here as a habit the course will formalize as Monte Carlo standard error in module 09.

## 02.3 Evidence accumulates: sequential equals batch, and log-odds add

Suppose the patient, still positive, takes the *same* test a second time (assume the two results are conditionally independent given true status). Do we condition on both at once, or feed the first posterior back in as the prior for the second? The two must agree, or the whole framework is incoherent.

**Predict (commit now).** Before the code: how many consecutive positives does it take before this patient is *more likely sick than not* — 2, 3, or 4? Each positive multiplies the odds by the same `19.8`, starting from 1-in-1000.

```python
# route A: condition sequentially -- posterior after test 1 becomes the prior for test 2
post1 = condition(prior, likelihood, obs=0)          # after first +
post_seq = condition(post1, likelihood, obs=0)       # after second +

# route B: condition once on the joint outcome (++), likelihood multiplies
lik_two = np.array([[sens**2], [(1 - spec)**2]])      # P(++ | dis), P(++ | heal)
post_batch = condition(prior, lik_two, obs=0)

print(f"P(disease | + then +)  sequential = {post_seq[0]:.4f}")
print(f"P(disease | ++)        batch      = {post_batch[0]:.4f}")
print(f"max |sequential - batch| = {np.abs(post_seq - post_batch).max():.1e}")

# keep multiplying: when does the patient cross even odds?
odds_k = prior_odds
for k in range(1, 5):
    odds_k *= LR
    print(f"P(disease | {k} positive{'s' if k > 1 else ' '}) = {odds_k/(1+odds_k):.4f}")
```

Sequential and batch both print `0.2818`, agreeing to `1.1e-16` — machine zero. This is not a coincidence to be memorized; it is associativity of multiplication. Conditioning on $o_1$ then $o_2$ multiplies the prior by $p(o_1\mid h)$ then by $p(o_2\mid h)$; conditioning on $(o_1,o_2)$ at once multiplies by $p(o_1,o_2\mid h)=p(o_1\mid h)p(o_2\mid h)$. Same product, same normalizer, same posterior. **Yesterday's posterior is today's prior** — the update is a running product, and order never matters.

And the crossing question: it takes **three** positives. Two independent 99%/95% positives leave the patient at `0.2818` — still less than even odds, because $19.8^2 \approx 392$ applied to prior odds `0.001001` is posterior odds ~0.39. The third positive lands at `0.8860`. If you guessed 2, your intuition multiplied probabilities loosely instead of odds exactly; the clean way to see it is to stop multiplying and start adding — count in log-odds.

A running product is awkward; its logarithm is a running sum. Define the log-odds (the "logit") $\ell = \log O$. Then each observation adds its log-likelihood-ratio:

$$\ell_{\text{posterior}} \;=\; \ell_{\text{prior}} \;+\; \sum_i \log \frac{p(o_i\mid h_1)}{p(o_i\mid h_2)}.$$

Evidence is *additive on the log-odds scale*. This is the reader's loss-summation intuition wearing statistical clothing: a stack of independent evidence contributes a stack of additive scores, exactly the way a linear classifier sums feature weights into a logit before the sigmoid. We make it a picture.

```python
log10_LR = np.log10(LR)
ks = np.arange(0, 7)
log10_odds = np.log10(prior_odds) + ks * log10_LR        # linear in # of positives
probs = 1 / (1 + 10.0**(-log10_odds))                    # sigmoid back to probability

fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 3.6))
a1.plot(ks, log10_odds, "o-", color="C1")
a1.axhline(0, color="black", lw=0.8, ls=":")
a1.set_xlabel("number of positive tests")
a1.set_ylabel("log$_{10}$ posterior odds")
a1.set_title("Log-odds: evidence adds (a straight line)")
a2.plot(ks, probs, "o-", color="C1")
a2.axhline(0.5, color="black", lw=0.8, ls=":")
a2.set_xlabel("number of positive tests")
a2.set_ylabel("P(disease | k positives)")
a2.set_title("Probability: the same evidence, S-curved")
save(fig, "logodds_accumulate")
```

The left panel is a straight line with slope $\log_{10} 19.8 \approx 1.30$: each positive test adds the same quantum of evidence. The right panel is the identical information after the sigmoid $O\mapsto O/(1{+}O)$ — the familiar S-curve, flat-then-steep-then-flat. Linear in log-odds, sigmoidal in probability: this duality is why deep networks carry *logits* internally and apply the sigmoid/softmax only at the end. Adding evidence is linear; the curvature is entirely in the link.

![Two panels versus the number of repeated positive tests. Left: log-base-10 posterior odds rise on an exact straight line of slope ~1.30, one fixed quantum of evidence per test. Right: the same quantity mapped through the sigmoid to P(disease), tracing the flat-steep-flat S-curve.](figures/02-conditioning-is-inference/logodds_accumulate.png)

## 02.4 German tank: a posterior over a thousand hypotheses

Conditioning does not care whether there are two hypotheses or two thousand. In 1943 the Allies wanted to estimate German tank production $N$ from the serial numbers of captured tanks. Model: tanks are numbered $1,\dots,N$; we observe $n$ of them, sampled without replacement; the sufficient statistic is $m=\max$ of the observed serials. The hypotheses are the possible values of $N$; the observable is $m$, with sampling distribution $P(M=m\mid N)=\binom{m-1}{n-1}\big/\binom{N}{n}$ for $n\le m\le N$.

Put a uniform prior on $N\in\{1,\dots,2000\}$ and hand the whole thing to the same engine — the "hypotheses" axis is now a thousand-plus values of $N$, and the likelihood is a single observed column ($m$ fixed at what we saw).

```python
from scipy.special import gammaln
def logC(a, b):                              # log C(a, b), vectorized, 0 outside support
    out = gammaln(a + 1) - gammaln(b + 1) - gammaln(a - b + 1)
    return np.where((b >= 0) & (b <= a), out, -np.inf)

def tank_posterior(m, n, Nmax):
    """Posterior over N in {1..Nmax} given max serial m from n draws, uniform prior."""
    N = np.arange(1, Nmax + 1)
    loglik = np.full(Nmax, -np.inf)                    # P(M=m|N)=0 off the support
    ok = N >= m                                        # a max of m needs N >= m
    loglik[ok] = logC(m - 1, n - 1) - logC(N[ok], n)   # log C(m-1,n-1)/C(N,n)
    lik = np.exp(loglik - loglik[ok].max())            # stabilize; -inf -> weight 0
    post = condition(np.ones(Nmax), lik[:, None], obs=0)   # uniform prior, one column
    return N, post

m_obs, n_obs, Nmax = 60, 5, 2000
N, post = tank_posterior(m_obs, n_obs, Nmax)
post_mean = (N * post).sum()
post_map = N[np.argmax(post)]
umvu = m_obs * (1 + 1 / n_obs) - 1
closed = (m_obs - 1) * (n_obs - 1) / (n_obs - 2)      # E[N|m,n], improper-uniform limit
print(f"observed max m={m_obs} from n={n_obs} serials")
print(f"Bayes posterior mean = {post_mean:.2f}")
print(f"Bayes MAP (posterior mode) = {post_map}")
print(f"closed form (m-1)(n-1)/(n-2) = {closed:.2f}")
print(f"UMVU  m(1+1/n)-1 = {umvu:.1f}")

fig, ax = plt.subplots()
ax.bar(N, post, width=1.0, color="C1", label="posterior P(N | data)")
for x, lab, c in [(m_obs, f"MAP={m_obs}", "C7"),
                  (umvu, f"UMVU={umvu:.0f}", "C0"),
                  (post_mean, f"post. mean={post_mean:.0f}", "C3")]:
    ax.axvline(x, color=c, ls="--", lw=1.4, label=lab)
ax.set_xlim(50, 200)
ax.set_xlabel("N (true number of tanks)")
ax.set_ylabel("posterior probability")
ax.set_title("German tank posterior: skewed right; the MAP is the worst summary")
ax.legend()
save(fig, "tank_posterior")
```

From a single captured max of `60` out of `5` serials, the posterior mean is `78.66` and the frequentist minimum-variance unbiased estimator (UMVU) $m(1+1/n)-1$ is `71.0`. (Unbiasedness we verify by simulation below; the "uniformly minimum variance among unbiased estimators" honorific is the standard completeness argument — $M$ is a complete sufficient statistic and the estimator is a function of it, Lehmann–Scheffé, C-B §7.3 territory, cited by concept.) They are in the same ballpark and both sensible. The MAP, though, is `60` — the posterior mode sits at the smallest feasible $N$, because $P(M=m\mid N)\propto 1/\binom{N}{n}$ decreases in $N$, so the posterior is monotone decreasing on $N\ge m$. The mode is the boundary; it is a terrible estimate (it asserts you have already seen the highest-numbered tank). The posterior mean, out in the skewed right tail, is the summary that respects the shape — and it matches the improper-uniform closed form $(m{-}1)(n{-}1)/(n{-}2)=$ `78.67` to rounding. Point summaries of a skewed posterior disagree by construction; module 06 will show that *which* summary you want is a decision about loss, not a matter of taste.

![Posterior over the number of tanks N given an observed maximum serial of 60 from 5 draws: a right-skewed distribution starting at N=60, with the MAP pinned at the left boundary (60), the UMVU at 71, and the posterior mean at 79 out in the tail.](figures/02-conditioning-is-inference/tank_posterior.png)

### Which estimator wins? A risk curve, and a surprise

**Predict (commit now).** We will simulate: fix the true count and, over many random captures of $n=5$ tanks, compute the mean squared error (MSE) of the UMVU versus the Bayesian posterior mean. The UMVU is *unbiased* and carries the honorific "uniformly minimum variance." So predict: across true counts $N$, which estimator has lower MSE — UMVU always, Bayes always, or does it depend?

**Reason.** Name the intuition you are leaning on before you run: "unbiased" and "uniformly minimum variance" *sound* like they settle the mean-squared-error question — you are trusting the honorifics as a gold standard.

**Run.** We sample the max directly from its known sampling distribution (a fast, exact stand-in for drawing $n$ serials and taking the maximum), then score both estimators against the truth.

```python
def bayes_lookup(n, Nmax):
    """E[N | max=m] for every possible m at once, uniform prior on 1..Nmax."""
    Ns = np.arange(1, Nmax + 1)
    w = np.zeros(Nmax); ok = Ns >= n
    w[ok] = np.exp(-logC(Ns[ok], n))                     # weight 1/C(N,n) on support
    suf_w = np.cumsum(w[::-1])[::-1]                      # sum over N >= m
    suf_Nw = np.cumsum((Ns * w)[::-1])[::-1]
    E = np.zeros(Nmax + 1); E[1:] = suf_Nw / suf_w
    return E                                              # index by observed m

def sample_max(N_true, n, reps, gen):
    m = np.arange(n, N_true + 1)
    p = np.exp(logC(m - 1, n - 1) - logC(N_true, n)); p /= p.sum()
    return m[np.searchsorted(np.cumsum(p), gen.random(reps), side="left").clip(0, len(m)-1)]

n = 5
E_lookup = bayes_lookup(n, Nmax)
# sanity: the max's sampling-distribution mean matches the closed form n(N+1)/(n+1)
m_chk, p_chk = np.arange(n, 1000 + 1), None
p_chk = np.exp(logC(np.arange(n, 1001) - 1, n - 1) - logC(1000, n)); p_chk /= p_chk.sum()
print(f"E[max] at N=1000: pmf {(m_chk*p_chk).sum():.1f} vs formula {n*1001/(n+1):.1f}")

gt = np.random.default_rng(SEED)
# dense points 1000-1300 so the crossover is located, not straddled by the grid
grid = np.array([150, 300, 500, 800, 1000, 1050, 1100, 1150, 1200, 1300, 1600, 1900])
reps = 40000                       # RMSE MC error ~0.4% here; ranking near the
                                   # crossing is stable across seeds at this size
umvu_rmse, bayes_rmse, umvu_mean, bayes_mean = [], [], [], []
for Nt in grid:
    M = sample_max(Nt, n, reps, gt)
    eu, eb = M * (1 + 1/n) - 1, E_lookup[M]
    umvu_rmse.append(np.sqrt(((eu - Nt)**2).mean()))
    bayes_rmse.append(np.sqrt(((eb - Nt)**2).mean()))
    umvu_mean.append(eu.mean()); bayes_mean.append(eb.mean())
umvu_rmse, bayes_rmse = np.array(umvu_rmse), np.array(bayes_rmse)

i1000 = list(grid).index(1000)
print(f"at N=1000:  UMVU mean {umvu_mean[i1000]:.1f} (≈ true 1000, unbiased), "
      f"Bayes mean {bayes_mean[i1000]:.1f} (biased high)")
print(f"at N=1000:  UMVU RMSE {umvu_rmse[i1000]:.1f}  Bayes RMSE {bayes_rmse[i1000]:.1f}")
print(f"at N=1900:  UMVU RMSE {umvu_rmse[-1]:.1f}  Bayes RMSE {bayes_rmse[-1]:.1f}")
bayes_wins = bayes_rmse < umvu_rmse
last_umvu = grid[np.where(~bayes_wins)[0][-1]]
first_bayes = grid[np.where(bayes_wins)[0][0]]
print(f"UMVU wins up to N = {last_umvu}; Bayes wins from N = {first_bayes} on "
      f"(crossing ~= 1075)")

fig, ax = plt.subplots()
ax.plot(grid, umvu_rmse, "o-", color="C0", label="UMVU  m(1+1/n)-1")
ax.plot(grid, bayes_rmse, "s-", color="C1", label="Bayes posterior mean (uniform prior ≤ 2000)")
ax.axvline(0.5 * (last_umvu + first_bayes), color="black", ls=":", lw=1)
ax.set_xlabel("true number of tanks N")
ax.set_ylabel("root mean squared error")
ax.set_title("Neither dominates: the prior ceiling helps Bayes exactly where N is large")
ax.legend()
save(fig, "tank_risk")
```

**Reconcile.** It depends — and the crossover is the lesson. The honorifics were not lying, but they answer a narrower question than you assumed: UMVU minimizes variance only *among unbiased estimators*, and since $\text{MSE}=\text{bias}^2+\text{variance}$, a biased rule that buys enough variance reduction can beat it. Here is where each side pays. The UMVU's simulated mean at $N=1000$ is `999.5`, essentially the truth: unbiased, as advertised. The Bayes posterior mean is `1057.5`, biased high, because with a uniform prior stretching to 2000 the right tail pulls the average up. At $N=1000$ that bias costs it: UMVU RMSE `169.0` beats Bayes RMSE `174.8`, and the naive "unbiased wins" looks vindicated. But push $N$ toward the prior's ceiling and it flips. At $N=1900$ the UMVU's occasional large-$m$ draws send its estimate wildly high — nothing caps it — while the Bayesian estimate *cannot* exceed 2000, so its variance collapses and it wins decisively, RMSE `271.3` versus `320.5`. On this grid UMVU wins up to $N=$ `1050` and Bayes from $N=$ `1100` on; a finer, larger-replicate scan puts the actual crossing near $N\approx$ `1075`.

The prior is not a bias to be ashamed of; it is *information* — "there are at most 2000 tanks" — and it pays off precisely when the truth is near that ceiling and hurts when the truth is far below it. Unbiasedness is one property among several, not a trump card; the honest comparison is a risk curve, and the winner is a function of where the truth sits relative to what you assumed. Module 06 makes this a theorem (Bayes rules and admissibility), and module 08 shows the frequentist crown jewel — Stein's estimator — is itself a prior-shrinkage move.

![Root-mean-squared error versus true tank count N for the two estimators, n=5 serials. The UMVU curve rises steeply and unboundedly with N; the Bayes-posterior-mean curve (uniform prior capped at 2000) rises more slowly, crossing below the UMVU near N≈1075 and winning by a widening margin as N approaches the prior ceiling.](figures/02-conditioning-is-inference/tank_risk.png)

## 02.5 When the event is not enough: the protocol is part of the model

Every likelihood entry above answered a subtle question: *given a hypothesis, how probable is the thing I observed?* For the tank, "I observed max serial 60" was unambiguous. But conditioning events can hide a generative choice, and when they do, the event alone does not determine the posterior — the *protocol* that produced it does.

> **Borel–Kolmogorov, in one box.** Conditioning on an event of probability zero — "a continuous variable equals *exactly* $x$" — is genuinely ambiguous. The conditional distribution you get depends on *which sequence of positive-probability events you shrink down to* the measure-zero one: condition a uniform point on a sphere to "lies on a great circle" and you get different answers for the same circle depending on whether you approached it through lines of longitude or through a rotated coordinate system. There is no paradox and no measure theory needed beyond this sentence: a bare zero-probability event does not carry its own definition of "given"; you must *declare the limiting protocol*, and the protocol is part of the model. Positive-probability events can smuggle in the same ambiguity whenever the event's probability depends on an unstated mechanism — which is exactly what happens next.

C-B Example 1.3.4 tells the Three Prisoners story: A, B, C are on death row, one pardoned uniformly at random; A asks the warden, who truthfully names B as one who will die. A reasons "now it is me or C, so my odds rose to 1/2." A is wrong — his probability stays 1/3 — and the reason is that the warden's *protocol* (he names a prisoner who will die, never the pardoned one) makes "the warden said B" more likely when C is pardoned than when A is. The event "B will die" does not update A; the *protocol-weighted* observation "the warden chose to say B" does. Rename the prisoners doors and the pardon a car and you have Monty Hall, the exercise below — same structure, and the whole answer turns on the host's protocol. Declare the protocol or you have not finished writing the model.

## Bridge — C-B §1.3 and the additive-logit view

C-B introduces conditional probability as *updating the sample space*: once $B$ is known, $B$ becomes the new sample space and $P(\cdot\mid B)$ is calibrated to it (C-B Def. 1.3.2, Example 1.3.3). Our engine is that idea rendered as array arithmetic — "keep the observed column" *is* restricting to $B$ and renormalizing — and Bayes' Rule (C-B eq. 1.3.5) is the identity that lets us compute $P(h\mid o)$ from the modelable direction $P(o\mid h)$. C-B's Three Prisoners (Example 1.3.4) is our protocol-dependence warning; and C-B itself defers conditioning on probability-zero events to its Chapter 4 (treating the Borel paradox in a later Miscellanea) — that deferral is our Borel–Kolmogorov box.

For the ML reader, the load-bearing bridge is §02.3: posterior log-odds $=$ prior log-odds $+\sum_i \log\text{LR}_i$. A stack of conditionally-independent evidence is a *sum of scores*, precisely a linear model in logit space; the sigmoid/softmax only appears when you convert back to probability. When you sum cross-entropy losses over a batch, or accumulate logits across independent features, you are running this update. The naive-Bayes spam classifier is this exact sum of log-likelihood-ratios with a conditional-independence assumption on the features — built and stress-tested in module 15.

## Pitfalls

- **Confusing the inverse.** $P(o\mid h)$ (modelable, forward) is not $P(h\mid o)$ (what you want). The medical test's `0.99` sensitivity and `0.0194` PPV are both correct and both about the same test; swapping them is the single most common probabilistic error in medicine, law, and ML evaluation alike.
- **Forgetting the base rate.** A strong likelihood ratio (`19.8`) can lose to a strong prior (1000-to-1). Screening a rare condition, auditing for rare fraud, detecting a rare failure — the false positives from the vast healthy majority dominate unless specificity is extreme. Always ask "how rare is the thing before the test?"
- **Reporting the MAP of a skewed posterior.** The German tank mode is the boundary `60`; the mean is `78.66`. On skewed or bounded posteriors the mode can be pathological. Know your posterior's shape before you summarize it with one number.
- **Conditioning on an event without its protocol.** "The host opened door 2" and "the warden said B" are not raw events — their likelihoods depend on the rule that generated them. Writing down $p(o\mid h)$ forces you to specify the protocol; conditioning on the bare event does not.
- **Trusting a simulation without its error bar.** Ten million draws pinned the PPV only to `0.0004`. An unreported Monte Carlo standard error is a silent overclaim; the rarer the event, the wider the bar.

## Exercises

**Exercise 02.1 — Monty Hall is a protocol, not a puzzle.**
*Setup:* Three doors; a car is behind one uniformly at random; you pick door 1. The host opens a door showing a goat, and you may switch to the remaining door. Consider two hosts. **Host A** always opens a goat door (and picks uniformly if he has a choice). **Host B** opens one of the other two doors *uniformly at random* and it merely happened to reveal a goat this time; had he revealed the car, the game would be void.
*Predict:* Under each host, is your probability of winning by switching $2/3$, $1/2$, or something else? Commit to two numbers before running.
*Reason:* The intuition "a door opened, two remain, so it's 50-50" ignores that Host A's choice is *informative* (constrained by where the car is) while Host B's is not — the same visible event, two different protocols.
*Run:*
```python
prior3 = np.ones(3) / 3                       # car behind door 1, 2, or 3; you pick door 1
# likelihood that door 2 is the one opened-and-showing-a-goat, per car location:
likA = np.array([[0.5], [0.0], [1.0]])        # A: car@1 -> open 2 or 3 (½); car@2 -> never; car@3 -> must open 2
likB = np.array([[0.5], [0.0], [0.5]])        # B: opens 2 at random (½) AND it's a goat; car@2 makes that impossible
postA = condition(prior3, likA, obs=0)        # P(car location | door 2 opened, goat)
postB = condition(prior3, likB, obs=0)
print(f"Host A:  stay(door1)={postA[0]:.4f}  switch(door3)={postA[2]:.4f}")
print(f"Host B:  stay(door1)={postB[0]:.4f}  switch(door3)={postB[2]:.4f}")

g = np.random.default_rng(SEED); R = 1_000_000
car = g.integers(0, 3, R)                      # you always pick door 0
openedA = np.where(car == 0, np.where(g.random(R) < 0.5, 1, 2), np.where(car == 1, 2, 1))
print(f"sim Host A switch-win = {(3 - openedA == car).mean():.4f}")
openedB = np.where(g.random(R) < 0.5, 1, 2); goat = openedB != car
print(f"sim Host B switch-win = {(3 - openedB == car)[goat].mean():.4f}")
```
<details><summary>Reconcile</summary>

Host A: switching wins with probability `0.6667`, staying `0.3333` — the classic $2/3$, confirmed by simulation at `0.6675`. Host B: `0.5000` each way, simulation `0.5009`. The visible situation is *identical* — you picked door 1, door 2 shows a goat — yet the answer differs because the likelihood of that observation differs. Host A, forced to reveal a goat, opens door 2 with probability 1 when the car is behind door 3 but only ½ when it's behind your door 1; that asymmetry is the information that makes switching pay. Host B opens door 2 with probability ½ regardless, so seeing a goat there tells you nothing about doors 1 vs 3. This is the Three Prisoners paradox restaged, and it carries the same moral as the Borel–Kolmogorov box: **the event does not carry its own likelihood; the protocol supplies it.** Both answers fall out of the same `condition` engine — only the likelihood column changed.
</details>

**Exercise 02.2 — The prosecutor's fallacy.**
*Setup:* A DNA profile matches with random-match probability $10^{-6}$ in the innocent population; the true culprit matches with certainty. A suspect, found by trawling a database, matches. The prosecutor announces: "the chance he is innocent is one in a million."
*Predict:* If the database (all innocent but one) holds 1,000,000 people, what is $P(\text{guilty}\mid\text{match})$? What if it holds 10,000,000?
*Reason:* The prosecutor quotes $P(\text{match}\mid\text{innocent})=10^{-6}$ as if it were $P(\text{innocent}\mid\text{match})$ — the confusion of the inverse again, now with a base rate set by the size of the search pool.
*Run:*
```python
for pool in (1_000_000, 10_000_000):
    prior = np.array([1/pool, 1 - 1/pool])                  # guilty, innocent
    lik = np.array([[1.0, 0.0], [1e-6, 1 - 1e-6]])          # P(match|.), P(no match|.)
    p_guilty = condition(prior, lik, obs=0)[0]
    print(f"pool {pool:>10,}:  P(guilty | match) = {p_guilty:.4f}"
          f"   (prosecutor claims {1 - 1e-6:.6f})")
```
<details><summary>Reconcile</summary>

At a pool of a million, $P(\text{guilty}\mid\text{match})=$ `0.5000`; at ten million, `0.0909` — about a 1-in-11 chance of guilt, not the `0.999999` the prosecutor asserts. In odds: prior odds of guilt are $1{:}(pool-1)$, the likelihood ratio is $10^{6}$, so posterior odds are roughly $10^6/pool$ — which is $1$ (probability ½) at a million and $0.1$ (probability 1/11) at ten million. A "one in a million" match is strong evidence that still loses to a large enough innocent pool, exactly as the disease's `19.8` likelihood ratio lost to prevalence `0.001`. The database trawl *is* the base rate; ignore it and you have inverted the conditional.
</details>

**Exercise 02.3 — Evidence is a sum of logits (an ML connection).**
*Setup:* An email is spam with base rate 0.3. Three conditionally-independent features have likelihood ratios (spam vs ham): contains "free" → LR 6.0; has no reply-to header → LR 2.5; comes from a known contact → LR 0.1. This message shows all three.
*Predict:* After all three features, is $P(\text{spam})$ above or below the 0.3 base rate — and by feel, roughly where?
*Reason:* Two features push toward spam and one strongly against; the pull is a *sum of log-likelihood-ratios*, so intuit it additively in log-odds, not by multiplying probabilities in your head.
*Run:*
```python
base = 0.3
log_odds = np.log(base / (1 - base))
feats = {"contains 'free'": 6.0, "no reply-to": 2.5, "known contact": 0.1}
for name, lr in feats.items():
    log_odds += np.log(lr)                                 # add each logit
    print(f"after {name:<16}: P(spam) = {1/(1+np.exp(-log_odds)):.4f}")
batch = (base/(1-base)) * np.prod(list(feats.values()))    # multiply odds all at once
print(f"batch odds-product P(spam) = {batch/(1+batch):.4f}")
```
<details><summary>Reconcile</summary>

The running probabilities are `0.7200`, `0.8654`, then `0.3913`; the batch odds-product agrees at `0.3913`. The two spam-ward features (log-LRs $+1.79$ and $+0.92$) drove it up, but the "known contact" feature (log-LR $-2.30$, i.e. LR 0.1) more than erased them, landing *below* the 0.3 base rate. The final logit is just prior-logit plus the three feature-logits — a linear score — and sequential-equals-batch holds here for the same associativity reason as the repeated medical test. This additive-logit machine with a conditional-independence assumption on the features *is* the naive-Bayes classifier, and the linear-score-then-sigmoid structure is logistic regression; module 15 builds both and shows where the independence assumption helps and where it lies.
</details>

**Exercise 02.4 — One tank, and the prior you cannot hide.**
*Setup:* You capture a single tank, serial `60` ($n=1$). You want to estimate the total $N$.
*Predict:* The UMVU $m(1+1/n)-1$ gives one clean number. Will the Bayesian posterior mean under a uniform prior agree, and will it depend much on where you cap the prior (say $N\le 200$ vs $N\le 50{,}000$)?
*Reason:* With one observation the likelihood $1/\binom{N}{1}=1/N$ decays slowly, so the posterior's right tail is fat — and a fat tail's mean can be dominated by wherever you truncate it.
*Run:*
```python
m1 = 60
print(f"UMVU (n=1): {m1*(1 + 1/1) - 1:.0f}")
for Nmax in (200, 5000, 50000):
    N = np.arange(1, Nmax + 1)
    w = np.where(N >= m1, 1.0 / N, 0.0); w /= w.sum()      # posterior ∝ 1/N on N>=60
    print(f"Nmax={Nmax:>6}:  Bayes posterior mean = {(N*w).sum():.1f},  MAP = {int(N[np.argmax(w)])}")
```
<details><summary>Reconcile</summary>

The UMVU says `119`, crisply. But the Bayes posterior mean is `116.1` at $N\le200$, `1115.0` at $N\le5000$, and `7416.5` at $N\le50000$ — it grows without bound as the cap rises, because with $n=1$ the posterior $\propto 1/N$ has a mean that diverges logarithmically. (The MAP is `60` throughout — the boundary again.) The lesson is not that the Bayesian answer is broken; it is that with one data point the data barely constrains the tail, so *your prior is doing the estimating* and pretending otherwise is the error. The UMVU hides this by reporting a number regardless; the posterior makes the prior-dependence visible. At $n=5$ the tail was thin enough (the `78.66` mean was stable across caps) that it stopped mattering — more data is exactly what lets the likelihood overrule the prior, the washout you will formalize in module 07.
</details>

## Takeaways

- **Conditioning is one operation.** Build the joint $p(h,o)=p(h)p(o\mid h)$, keep the observed column, renormalize. Two hypotheses or two thousand, it is the same three lines — the `condition` engine — and its denominator is the evidence $p(o)$ that will resurface as the marginal likelihood.
- **Posterior odds = prior odds × likelihood ratio.** The data's whole contribution is the likelihood ratio; the prior is a separate multiplier. Strong evidence (`19.8`) still loses to a strong base rate (`0.001`): PPV `0.0194`.
- **Evidence is additive in log-odds.** $\ell_{\text{post}}=\ell_{\text{prior}}+\sum_i\log\text{LR}_i$. Sequential updating equals batch updating (to `1.1e-16`) because it is a running product; in logits it is a running sum — the linear-score-then-sigmoid shape of every classifier.
- **The base rate is information, not a nuisance.** Confusing $P(o\mid h)$ with $P(h\mid o)$ is the prosecutor's fallacy and the medical-test error; the fix is always to write down the prior explicitly.
- **Summaries of a posterior are choices.** The German tank MAP (`60`) is the boundary and useless; the mean (`78.66`) respects the skew. Which one you report is a decision about loss (module 06).
- **Unbiasedness is not optimality.** The Bayes posterior mean beats the UMVU on MSE once the true $N$ passes $\approx$ `1075` because its prior ceiling cuts variance; neither dominates. Risk is a curve, not a verdict (modules 06, 08).
- **A conditioning event needs a protocol.** Monty Hall, Three Prisoners, and Borel–Kolmogorov are one lesson: the bare event does not carry its likelihood; the generative rule does. Declare it or the model is unfinished.

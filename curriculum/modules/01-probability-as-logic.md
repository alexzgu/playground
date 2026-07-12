# 01. Probability as the Logic of Uncertainty

> **Spine.** Exchangeability, not philosophy, is what makes parameters exist: the empirical frequency of an exchangeable sequence converges to a *random* limit, and that limit is the parameter θ.
> **Which line?** Upstream of line 1. It licenses writing a joint distribution `p(unknowns, knowns)` with a parameter θ in it at all — exchangeability is *why there is a θ*, and a prior over it, to condition on later.
> **Promise.** After this module you can look at a data-generating setup and decide whether a parameter-with-a-prior even exists to infer — by checking exchangeability — and name where that assumption silently fails.
> **Prereqs.** Module 00. **Runtime.** ~5 s (measured).
> **Sources.** Booklet ch. 1–2 (§2.3 exchangeability, §2.5 de Finetti); C-B ch. 1 (§1.2.1 axioms) and Exercise 5.4; de Finetti (1937) and Hewitt–Savage (1955), by concept; Cox, by concept.

A thumbtack, flipped, lands point-up or point-down. Flip it 2,000 times and the running fraction point-up stops wandering and settles — the Law of Large Numbers, as advertised. But settles to *what*? Not to a number you could have written down before the first flip. Buy a fresh tack and the fraction settles somewhere else. The limit exists, and it is itself uncertain. That random limit is the parameter θ, and this module is about the theorem that puts it there. The usual framing — "are you a Bayesian or a frequentist?" — is a distraction. The real content is a representation theorem: assume only that the *order* of your observations carries no information, and a parameter with a prior distribution is forced into existence. No metaphysics required.

## 01.1 Two readings, one calculus

There are two honest answers to "what is P(A)?"

- **Long-run frequency.** P(A) is the fraction of times A occurs if the experiment is replayed forever. It is *evaluated by replaying*: toss the coin 10,000 times and count (the booklet's own empirical view, ch. 2 §2.7.1).
- **Coherent degree of belief.** P(A) is the price you would pay for a ticket worth \$1 if A occurs — your uncertainty made numerical. It is *evaluated by coherence*: a set of prices is legitimate iff no opponent can arrange bets you accept that lose you money no matter what happens.

Treat these as two **evaluation modes**, not two tribes. They compute with the *same* three rules. C-B's Definition 1.2.4 and the booklet's page 2 give the identical Kolmogorov axioms — nonnegativity, P(S)=1, countable additivity — and every downstream identity (Bayes' rule, marginalization) follows from them regardless of what you think P(A) *means*. The disagreement is about interpretation, never about the algebra. That is exactly why this course refuses to tribalize: we will use frequency to *audit* beliefs and beliefs to *organize* frequencies, switching modes as convenient.

**Why the belief reading obeys the axioms at all — the Dutch book.** de Finetti's argument (and Cox's, from different premises) is that *incoherent* prices are not merely distasteful, they are exploitable. Consider three mutually exclusive, exhaustive states of tomorrow's weather — exactly one occurs. A forecaster quotes prices `0.5`, `0.4`, `0.3`, which sum to `1.2` instead of 1. Additivity is violated. Now the opponent sells the forecaster one \$1 ticket on *each* state at those prices; the forecaster pays the three premiums and, since exactly one state occurs, collects exactly \$1 back. The payoff table is printed below: every column — every possible outcome — is negative, a guaranteed loss of `0.2`.

| bet | rain occurs | cloudy occurs | clear occurs |
|---|---|---|---|
| buy ticket on rain (pay 0.5) | +0.50 | −0.50 | −0.50 |
| buy ticket on cloudy (pay 0.4) | −0.40 | +0.60 | −0.40 |
| buy ticket on clear (pay 0.3) | −0.30 | −0.30 | +0.70 |
| **TOTAL** | **−0.20** | **−0.20** | **−0.20** |

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "01-probability-as-logic"          # this module's figure dir
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
# Dutch book: incoherent prices on a partition => a sure loss for the quoter.
events = ["rain", "cloudy", "clear"]
q = np.array([0.5, 0.4, 0.3])                     # quoted prices; sum != 1
print(f"quoted prices: rain={q[0]}, cloudy={q[1]}, clear={q[2]}")
print(f"sum of quoted probabilities = {q.sum():.1f}   (coherence needs 1.0)")

# Opponent makes the quoter BUY a $1 ticket on each state at its price.
# payoff[bet i, outcome j] = (1 if state i occurs) - price_i, netted per outcome.
payoff = np.eye(3) - q[:, None]
coltot = payoff.sum(axis=0)
print("           " + "".join(f"{e:>9}" for e in events))
for i, e in enumerate(events):
    print(f"buy {e:<7}" + "".join(f"{payoff[i, j]:>9.2f}" for j in range(3)))
print("TOTAL     " + "".join(f"{t:>9.2f}" for t in coltot))
print(f"agent's guaranteed loss = {-coltot[0]:.1f} whichever outcome occurs")
```

The only prices immune to this — for *any* book the opponent can build — are prices that obey the axioms. Coherence *is* the axioms — with one scope note: a finite book of bets forces only *finite* additivity; full countable additivity is an extra regularity assumption, and de Finetti himself resisted it (C-B §1.2.1 records that his school replaces Axiom 3 with an Axiom of Finite Additivity). So the degree-of-belief reading is not a soft alternative to "real" probability; it is pinned to the same calculus by the threat of a sure loss. This is the booklet's "coherent scientist" (ch. 1 §1.3), stated as a theorem instead of an admonition.

**Where the two readings meet: calibration.** If your beliefs are any good, they should *match frequencies* — among all the days you say "70% chance of rain," it should rain about 70% of the time. Simulate an honest forecaster who each day picks a probability p and then the outcome really is Bernoulli(p). Bin the forecasts and compare the stated probability to the observed frequency in each bin. A perfectly honest forecaster's points lie on the diagonal; the expected calibration error (ECE, the frequency-weighted average gap between stated probability and observed frequency) is `0.007`, pure sampling noise.

**Predict.** Now an *overconfident* forecaster reports the same days with confidence stretched 1.6× away from 0.5 — says 0.9 when they mean 0.75 — a mild-sounding distortion. Commit before running: relative to the honest `0.007`, does the ECE roughly double, quintuple, or worse?

```python
# Calibration = a degree-of-belief object (a forecast) evaluated by frequency.
Ncal = 20000
p = rng.uniform(0, 1, Ncal)                       # honest forecaster's beliefs
y = (rng.uniform(0, 1, Ncal) < p).astype(int)     # reality: outcome ~ Bernoulli(p)
s = np.clip(0.5 + 1.6 * (p - 0.5), 0, 1)          # overconfident: pushed from 0.5

edges = np.linspace(0, 1, 11)
def bin_stats(f, y):
    idx = np.clip(np.digitize(f, edges) - 1, 0, 9)
    xs, ys, ece = [], [], 0.0
    for b in range(10):
        m = idx == b
        if m.any():
            xs.append(f[m].mean()); ys.append(y[m].mean())
            ece += m.mean() * abs(f[m].mean() - y[m].mean())   # weighted gap
    return np.array(xs), np.array(ys), ece

hx, hy, hece = bin_stats(p, y)
ox, oy, oece = bin_stats(s, y)
print(f"ECE honest       = {hece:.3f}   (beliefs match frequencies)")
print(f"ECE overconfident= {oece:.3f}   (beliefs no longer match)")
print(f"ECE inflation    = {oece / hece:.1f}x   from a 1.6x confidence stretch")

fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1], "--", color="black", lw=1, label="perfect calibration")
ax.plot(hx, hy, "o-", color="C0", label=f"honest (ECE {hece:.3f})")
ax.plot(ox, oy, "s-", color="C1", label=f"overconfident (ECE {oece:.3f})")
ax.set_xlabel("stated probability (a degree of belief)")
ax.set_ylabel("observed frequency (a long-run rate)")
ax.set_title("Calibration is where belief and frequency have to agree")
ax.legend()
save(fig, "calibration")
```

![Reliability diagram: the honest forecaster's stated probabilities fall on the diagonal (belief = frequency); the overconfident forecaster's curve crosses the diagonal near 0.5 — bowing above it for low stated probabilities and below it for high ones.](figures/01-probability-as-logic/calibration.png)

**Reconcile.** The ECE lands at `0.089` — a `13.0`× inflation from a 1.6× stretch. If you guessed "roughly doubles," you scaled the error like the distortion; but ECE measures the *gap* between stated probability and frequency, and the honest gap was near zero — so even a mild stretch is not a small perturbation of the error, it is essentially all of it. The diagonal in the figure is the bridge: a coherent degree of belief, if it is *calibrated*, reproduces long-run frequencies. The two readings are not rivals; one is the other, audited.

## 01.2 The de Finetti trio: where parameters come from

Independence is a strong claim: X₁ tells you nothing about X₂. Most real data are not like that — knowing the first 40 customers converted makes you expect the 41st to convert, because they share an unknown rate. The weaker, right assumption is **exchangeability**: the joint density is invariant to permutations of the indices (booklet §2.3),

$$p(x_1,\dots,x_n) = p(x_{\pi(1)},\dots,x_{\pi(n)}) \quad\text{for every permutation } \pi.$$

Order carries no information; only the multiset of values does. Every iid sequence is exchangeable; the converse is false, and the gap between them is the entire subject of this section. Three demonstrations, each staged `predict → run → reconcile`. All three are **Empirical** — simulated here to exhibit the content of the representation theorem of §01.3, which we cite rather than prove — except the covariance identity Cov[Xᵢ, Xⱼ] = Var[Θ], derived in two lines in (a), which makes (b)'s mixture-impossibility argument a proof.

### (a) A mixture of Bernoullis: the limit is random

**Setup.** Draw a single Θ ~ Beta(2,2), *then* draw X₁,…,Xₙ iid Bernoulli(Θ). This is C-B's Exercise 5.4 with a Beta prior — exchangeable, because the joint depends on the data only through Σxᵢ, but emphatically not iid, because the Xᵢ share Θ.

**Predict.** Run 4,000 independent replicates, each a fresh Θ and a long Bernoulli(Θ) sequence. The naive Law-of-Large-Numbers intuition says every replicate's running frequency marches to *the* probability, 0.5. Commit: do the 4,000 running frequencies converge to one number or many? And is Corr[X₁, X₂] zero (as iid would give) or not?

**Run.** The frequencies fan out to `4,000` *different* limits, and the histogram of those limits is the Beta(2,2) prior itself (terminal-frequency mean `0.496`, variance `0.0503`, matching Beta(2,2)'s 0.5 and `0.05`). Marginally each Xᵢ is Bernoulli(0.5), but the pair is dependent: the empirical pairwise correlation is `0.210` (covariance `0.053`), not zero, and P(X₁=1, X₂=1) is `0.304`, not the `0.25` that independence (0.5 × 0.5) would demand.

**Reconcile.** The LLN never lied — it never promised convergence to the marginal mean, only to the *conditional* mean E[Xᵢ | Θ] = Θ, which is random. And the dependence the naive guess missed is forced, in two lines: conditional on Θ the variables are independent, so E[XᵢXⱼ] = E[ E[Xᵢ | Θ] E[Xⱼ | Θ] ] = E[Θ²], hence

$$\mathrm{Cov}[X_i, X_j] \;=\; \mathrm{E}[\Theta^2] - \mathrm{E}[\Theta]^2 \;=\; \mathrm{Var}[\Theta],$$

the law of total covariance with the conditional-covariance term killed by conditional independence. For Beta(2,2) that gives Var[Θ] = `0.05`, matching the measured covariance `0.053`, and correlation Var[Θ]/0.25 = `0.2`, matching the measured `0.210`. **The random limit Θ is the parameter; its distribution is the prior.** That is the spine, on screen.

```python
# (a) Beta(2,2)-Bernoulli mixture: exchangeable, not iid; freq -> random limit.
a_, b_ = 2, 2
R, Nrep = 4000, 1500
theta = rng.beta(a_, b_, size=R)                       # each replicate's own limit
X = (rng.uniform(size=(R, Nrep)) < theta[:, None]).astype(np.int8)

varT = a_ * b_ / ((a_ + b_) ** 2 * (a_ + b_ + 1))      # Var of Beta(2,2)
corr_th = varT / 0.25                                  # Cov/Var; marginal Var=0.25
corr_emp = np.corrcoef(X[:, 0], X[:, 1])[0, 1]
cov_emp = np.cov(X[:, 0], X[:, 1])[0, 1]
p11 = (X[:, 0] & X[:, 1]).mean()
runfreq = X.cumsum(axis=1, dtype=float) / np.arange(1, Nrep + 1)   # float: no int8 overflow
term = runfreq[:, -1]
print(f"marginal mean E[X_i]    = {X.mean():.3f}  (theory 0.5)")
print(f"Var[theta] = Cov[Xi,Xj] = {varT:.2f}   (analytic, Beta(2,2))")
print(f"covariance empirical    = {cov_emp:.3f}")
print(f"pairwise corr: theory {corr_th:.1f}, empirical {corr_emp:.3f}  (iid would give 0)")
print(f"P(X1=1,X2=1) empirical  = {p11:.3f}   product of marginals = 0.25")
print(f"terminal running freq: mean {term.mean():.3f}, variance {term.var():.4f}")

fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4))
steps = np.arange(1, Nrep + 1)
for r in range(60):                                    # 60 replicates, no rng here
    axL.plot(steps, runfreq[r], lw=0.6, alpha=0.35)
axL.axhline(0.5, color="black", ls="--", lw=1.2, label="marginal mean 0.5")
axL.set_xscale("log")
axL.set_xlabel("number of trials n (log scale)"); axL.set_ylabel("running frequency")
axL.set_title("60 replicates → 60 different limits (not 0.5)"); axL.legend()
grid = np.linspace(0, 1, 200)
axR.hist(term, bins=30, density=True, alpha=0.6, color="C0", label="limits (empirical)")
axR.plot(grid, stats.beta(a_, b_).pdf(grid), color="black", lw=2, label="Beta(2,2) prior")
axR.set_xlabel("terminal running frequency ≈ Θ"); axR.set_ylabel("density")
axR.set_title("the limits' histogram = the mixing prior"); axR.legend()
save(fig, "definetti_fan")
```

![Left: 60 running-frequency curves converge to 60 distinct horizontal levels, not to 0.5. Right: the histogram of those limiting frequencies traces the Beta(2,2) density.](figures/01-probability-as-logic/definetti_fan.png)

### (b) Finite exchangeability ≠ a mixture: negative correlation

**Setup.** An urn holds 10 balls, 5 red and 5 black. Draw all of them *without replacement* and record the color sequence. Every ordering of the 10 balls is equally likely, so the sequence is exchangeable.

**Predict.** Demo (a) found positive correlation. Sampling without replacement: sign of Corr[X₁, X₂]? And — the deeper question — can this exchangeable sequence be written as a Beta-Bernoulli-style mixture, "draw a rate, then flip coins"?

**Run & reconcile.** The correlation is *negative*: empirically `-0.116`, matching the exact `-0.1111` = −1/(N−1), with covariance `-0.0289` ≈ −1/36 = `-0.0278`. A red drawn first leaves fewer reds, so the second draw leans black. And this **cannot** be a mixture, by the identity derived in demo (a): any conditionally-iid sequence has Cov[Xᵢ, Xⱼ] = Var[Θ] ≥ 0. A negative covariance is off-limits to *every* mixture. So finite exchangeable sequences are strictly more general than mixtures of iid — de Finetti's clean representation is simply false at finite n. What rescues it is **infinite** exchangeability: the sequence must extend to an infinitely long exchangeable one. You cannot extend the urn — draw an 11th ball and there is none — which is precisely why no mixture represents it. The figure plots both families: the without-replacement correlation −1/(N−1) climbing toward 0 as the urn grows, and the mixture's flat, positive `0.2`. Larger urns are "more extendable," and their negative correlation vanishes; in the n → ∞ limit the two pictures meet at the mixture. (Exercise 01.2 makes this scaling quantitative.)

```python
# (b) Sampling without replacement: exchangeable with NEGATIVE correlation.
Nurn, K, R2 = 10, 5, 40000
urn = np.array([1] * K + [0] * (Nurn - K))
draws = urn[np.argsort(rng.random((R2, Nurn)), axis=1)]     # each row a shuffle
corr_b = np.corrcoef(draws[:, 0], draws[:, 1])[0, 1]
cov_b = np.cov(draws[:, 0], draws[:, 1])[0, 1]
print(f"without replacement, N=10: mean {draws.mean():.3f}, "
      f"cov {cov_b:.4f} (theory -1/36 = {-1/36:.4f}), "
      f"corr {corr_b:.3f} (theory -1/9 = {-1/9:.4f})")

wor_corr = {}                                               # empirical dots for figure
for Nn in [4, 10, 50, 200]:
    u = np.array([1] * (Nn // 2) + [0] * (Nn - Nn // 2))
    d = u[np.argsort(rng.random((20000, Nn)), axis=1)]
    wor_corr[Nn] = float(np.corrcoef(d[:, 0], d[:, 1])[0, 1])
print("corr vs N: " + ", ".join(f"N={k}:{v:+.4f}" for k, v in wor_corr.items()))

fig, ax = plt.subplots()
Ngrid = np.arange(2, 201)
ax.plot(Ngrid, -1 / (Ngrid - 1), color="C0", label="without replacement:  -1/(N-1)")
ax.scatter(list(wor_corr), list(wor_corr.values()), color="C0", zorder=5)
ax.axhline(corr_th, color="C1", label="Beta(2,2)-Bernoulli mixture:  +0.2")
ax.scatter([2], [corr_emp], color="C1", zorder=5)
ax.axhline(0, color="black", lw=0.8)
ax.set_xscale("log")
ax.set_xlabel("sequence length / urn size N (log scale)")
ax.set_ylabel("pairwise correlation  Corr[Xi, Xj]")
ax.set_title("Mixtures correlate positively; finite urns negatively (→ 0)")
ax.legend()
save(fig, "exchangeable_correlations")
```

![Pairwise correlation versus N: the without-replacement curve is negative and rises toward zero as the urn grows, while the mixture sits at a constant positive 0.2.](figures/01-probability-as-logic/exchangeable_correlations.png)

### (c) The Pólya urn: an exchangeable process that *is* a mixture

**Setup.** Start an urn with a red and b black balls. Draw one at random, return it *plus a new ball of the same color*, and repeat. Success breeds success — a red draw makes red more likely next time. This is the rich-get-richer process that will reappear as the Chinese restaurant process in module 19.

**Predict.** The sequence is exchangeable (we will see the probability of a sequence depends only on its red/black counts). By de Finetti it should be a mixture — but of *what* prior? Guess before running: is the Pólya urn's probability of a specific sequence equal to the Beta(a,b)-Bernoulli predictive probability?

**Run & reconcile.** They are identical to machine precision. For a = 2, b = 3, the sequence [1,1,1] has probability `0.114286` by both the sequential urn product and the closed form B(a+k, b+n−k)/B(a,b); [1,0,1] gives `0.085714` both ways; the maximum discrepancy across the tested sequences is below `1e-12`. The Pólya urn *is* "draw Θ ~ Beta(a,b), then flip Bernoulli(Θ) forever," with the drawn ball encoding a memory of Θ. This is line 3 of module 00's four lines — *Prediction is marginalization: p(new | knowns) = ∫ p(new | unknowns) p(unknowns | knowns)* — running as a physical process: the urn integrates over the unseen rate (the "unknowns" = Θ) for you.

```python
# (c) Polya urn sequence probability == Beta-Binomial predictive probability.
from scipy.special import betaln

def polya_prob(seq, a, b):
    """Probability of an exact color sequence under a Polya urn (a red, b black)."""
    red, tot, logp = a, a + b, 0.0
    for x in seq:
        if x == 1:
            logp += np.log(red / tot); red += 1        # draw red, add a red
        else:
            logp += np.log((tot - red) / tot)          # draw black, add a black
        tot += 1
    return np.exp(logp)

def betabin_pred(seq, a, b):
    """Same sequence under 'draw theta~Beta(a,b), then iid Bernoulli(theta)'."""
    k, n = sum(seq), len(seq)
    return np.exp(betaln(a + k, b + n - k) - betaln(a, b))

aa, bb = 2, 3
seqs = [[1, 1, 1], [1, 0, 1], [0, 0, 1], [1, 1, 0, 0, 1]]
mx = 0.0
for sq in seqs:
    pv, bv = polya_prob(sq, aa, bb), betabin_pred(sq, aa, bb)
    mx = max(mx, abs(pv - bv))
    print(f"seq {sq}: polya {pv:.6f}   beta-binomial {bv:.6f}")
print(f"max |polya - beta-binomial| = {mx:.1e}   (agree to < 1e-12)")
```

## 01.3 de Finetti's representation theorem

The trio's lesson, made a theorem.

> **Theorem (de Finetti, 1937; general form Hewitt–Savage, 1955 — stated here, not proved).** Let X₁, X₂, … be an **infinite** exchangeable sequence of {0,1}-valued random variables. Then (i) the limit Θ := limₙ (1/n) Σᵢ₌₁ⁿ Xᵢ exists almost surely; and (ii) there is a **unique** distribution G on [0,1] — the law of Θ — such that, conditional on Θ, the Xᵢ are iid Bernoulli(Θ); equivalently, for every n,
> $$p(x_1,\dots,x_n) = \int_0^1 \theta^{\sum x_i}(1-\theta)^{\,n-\sum x_i}\, dG(\theta).$$

We do not prove it — the proof is a martingale/moment argument (Hewitt–Savage), and, as demo (b) showed, it is *false* without the word "infinite." What we did instead was watch its content. Read left to right, demo (a) *is* the theorem: pick G = Beta(2,2), and out comes an exchangeable sequence whose frequencies converge to draws from G. The theorem's real force is the **converse**: *every* infinite exchangeable binary sequence arises this way, for a unique G. That is what manufactures a parameter. Θ and its prior G are not modeling luxuries a Bayesian bolts on — they are *forced* by the single assumption that the labels 1, 2, 3, … carry no information.

This is where line 1 of module 00's four lines — *A model is a joint distribution `p(unknowns, knowns)`* — gets its raw material. Exchangeability is the license to write an unknown θ (and a prior over it) into that joint at all. "Random = unknown to you": Θ is random not because it fluctuates from flip to flip — it is a single fixed limit — but because *you* do not know it. Conditioning on data (module 02) will be nothing but narrowing G in light of the Σxᵢ the theorem says is all that matters. The mixing distribution is unique (booklet ch. 2, note after Example 3): the exchangeable joint determines G — there is no freedom in how to split the model into likelihood and prior. Two observers who disagree about the prior are disagreeing about the joint distribution itself, and data plus coherence can adjudicate that.

**Honest scope.** The clean theorem above is the binary case. General exchangeable sequences (real-valued, vector-valued) have their own de Finetti representation as mixtures of iid laws, but the mixing object is a distribution over *distributions* (it lives in module 19's nonparametric world). And the whole apparatus needs infinite exchangeability; finite exchangeable data are only *approximately* mixtures, with the −1/(N−1) correction of demo (b) measuring the gap.

## 01.4 Exchangeability is a modeling assumption, not a law

Because exchangeability does so much — it conjures the parameter — it is worth saying loudly where it can be *wrong*, because when it is, the θ you inferred is answering a question you did not ask.

**The permutation null.** A great deal of classical testing is exchangeability in disguise. Under a null hypothesis of the form "the group labels don't matter" — a treatment has no effect, so a subject's response would have been the same in either arm — the pooled responses are exchangeable across the labels. Every relabeling is then equally probable, which *is* the null distribution of any test statistic: compute the statistic on the real labeling, recompute it on all (or many) permutations, and read off a p-value. No parametric form, no asymptotics — exchangeability under H₀ is the entire content of the test. We build the permutation test in full in module 23; here the point is only that "labels are exchangeable" and "H₀ is true" are frequently the same sentence.

**Bridge — the shared axioms and the benchmark's silent assumption.**

- **C-B ch. 1 (§1.2.1).** Both readings of §01.1 sit on C-B's Definition 1.2.4 (Kolmogorov axioms) — the shared substrate. Cox's theorem derives that same calculus from qualitative desiderata on "degree of plausibility"; de Finetti derives it from "no sure loss." Two roads, one algebra — the reason we teach frequentist results as special cases and audits rather than as an opposing camp.
- **ML: train/test exchangeability is the quiet assumption under every benchmark.** When you report test-set accuracy or a cross-validation score as an estimate of generalization, you are assuming train and test are *exchangeable* draws — that the test point's position in the sequence (it happened to land in the test fold) carries no information about its label. That is the same assumption as "random = unknown to you": the model does not know the test label, so the label is random, and exchangeability says its fold membership is uninformative. Break it — temporal data split at random so the future leaks into the past, grouped data (patients, users) whose members straddle the split, distribution shift between collection and deployment — and the benchmark measures the wrong quantity while looking perfectly rigorous (Exercise 01.3). Conformal prediction (module 26) leans on *exactly and only* this assumption to get finite-sample coverage guarantees with no model of the data at all — the purest cash-out of this module.

## Pitfalls

- **Confusing the marginal mean with the limit.** In an exchangeable-but-not-iid sequence the running frequency converges to Θ, a random draw from the prior — *not* to E[Xᵢ]. One long dataset pins down its own Θ, not the population average. Reporting "the" rate from a single exchangeable stream and treating it as certain is the error module 05 will formalize as ignoring posterior variance.
- **Assuming exchangeability buys you iid.** It does not. Exchangeable variables are identically distributed and equi-correlated but generally dependent (correlation `0.2` in demo (a)). Likelihoods that silently multiply p(xᵢ) as if independent are assuming the *conditional* iid structure — valid only *given* θ, which you must then integrate out.
- **Invoking de Finetti at finite n.** The representation as a mixture of iid is an *infinite*-exchangeability theorem. Finite exchangeable sequences (any without-replacement / permutation setup) can have negative correlation that no mixture reproduces. Ask "does this extend to an infinite exchangeable sequence?" before writing a prior.
- **Randomly shuffling dependent data into train/test.** Time series, spatial data, and grouped records are not exchangeable across a naive split; random K-fold then leaks information and reports optimistic error. The benchmark's validity is an exchangeability assumption, not a formality.
- **Arguing interpretation instead of computing.** "Frequentist vs Bayesian" is rarely the real question. Both obey the same axioms; the operative question is the bookkeeping one — which quantities are you treating as unknown (hence random, hence given a distribution) and which as fixed?

## Exercises

**Exercise 01.1 — The rule of succession.**
*Setup:* A Pólya urn starts with a = 1 red and b = 1 black (equivalently, a uniform prior Θ ~ Beta(1,1)). You draw 5 balls and every one is red.
*Predict:* What is the probability the 6th draw is red? Commit to a number. What about after 50 reds in a row?
*Reason:* The plug-in / maximum-likelihood instinct reads the data as a frequency: 5 of 5 is 100%, so predict 1.0.
*Run:*
```python
# Predictive probability of the next success under Beta(a,b) + Bernoulli.
for a, b, k, n in [(1, 1, 5, 5), (1, 1, 50, 50)]:
    p_next = (a + k) / (a + b + n)                 # = E[theta | data], the Polya fraction
    print(f"a={a}, b={b}: after {k}/{n} reds, P(next red) = {p_next:.4f}")
```
<details><summary>Reconcile</summary>

The answer after 5/5 is `0.8571` = 6/7, not 1.0; after 50/50 it is `0.9808` = 51/52. The predictive probability is the *posterior mean* E[Θ | data] = (a+k)/(a+b+n), which the Pólya urn computes physically (6 reds among 7 balls after the fifth red). Certainty of 1.0 would claim the next ball is red *for sure* on the strength of five draws — the overconfidence the whole course is built to cure. The naive frequency ignores that Θ is still uncertain; the prior's two pseudo-observations pull the estimate off the boundary. This is Laplace's rule of succession, and it returns as add-one smoothing in language models and as the losing plug-in bet in module 00's coin demo.
</details>

**Exercise 01.2 — When is a finite urn "almost" a mixture?**
*Setup:* Sampling k balls without replacement from an urn that is half red is exchangeable with correlation −1/(N−1), where N is the urn size. Consider a tiny urn (N = 4) and a large one (N = 200), both half red.
*Predict:* Which urn's draws behave more like an iid mixture (conditionally-independent flips of a fixed coin) — the small one or the large one? By roughly how much does the correlation differ between them?
*Reason:* "Exchangeable is exchangeable" suggests the two should look about the same.
*Run:*
```python
# Reuse the empirical correlations measured in demo (b)'s figure loop.
for Nn in [4, 200]:
    print(f"N={Nn}: theory {-1/(Nn - 1):+.4f}   empirical {wor_corr[Nn]:+.4f}")
```
<details><summary>Reconcile</summary>

The small urn is strongly non-mixture: N = 4 gives correlation `-0.3333` (empirically `-0.3202`), far from the nonnegative value any mixture allows. The large urn is nearly a mixture: N = 200 gives `-0.0050` (empirically `-0.0101`), a whisker below zero. As N → ∞ the negative correlation vanishes and the finite exchangeable sequence becomes *extendable* to an infinite one — exactly the regime de Finetti needs. The lesson: infinite exchangeability is not a technicality to wave away; it is the limit in which "draw a parameter, then flip independent coins" becomes legitimate, and the −1/(N−1) term is the visible price of finiteness.
</details>

**Exercise 01.3 — Why you cannot shuffle a time series [ML].**
*Setup:* You have two datasets of length 4,000: one iid Gaussian, one an AR(1) series xₜ = 0.8 xₜ₋₁ + εₜ. You plan to estimate out-of-sample error by holding out random points and predicting each from its neighbors.
*Predict:* For which dataset is a random train/test split safe? Will random-split cross-validation over-, under-, or correctly estimate the honest prediction error on the AR(1) series?
*Reason:* Cross-validation "just works" — the folds are interchangeable, so shuffling is harmless.
*Run:*
```python
# Exchangeable data can be shuffled; autocorrelated data cannot.
n, phi = 4000, 0.8
eps = rng.normal(size=n)
ar = np.empty(n); ar[0] = eps[0]
for t in range(1, n):
    ar[t] = phi * ar[t - 1] + eps[t]
iid = rng.normal(size=n)
lag1 = lambda z: np.corrcoef(z[:-1], z[1:])[0, 1]
nbr = np.mean((ar[1:] - ar[:-1]) ** 2)                 # error using a temporal neighbor
rnd = np.mean((ar - rng.permutation(ar)) ** 2)         # error using an unrelated point
print(f"iid   lag-1 autocorr = {lag1(iid):+.3f}")
print(f"AR(1) lag-1 autocorr = {lag1(ar):+.3f}")
print(f"AR(1): neighbor-based error {nbr:.2f}  vs  unrelated-point error {rnd:.2f}")
```
<details><summary>Reconcile</summary>

The iid series has lag-1 autocorrelation `0.011` (essentially zero) — genuinely exchangeable, safe to shuffle. The AR(1) series has autocorrelation `0.779`: a random split leaves each held-out point's temporal neighbors sitting in the training set, and a predictor that copies a neighbor scores error `1.09`, while the *same copy-predictor* applied to an unrelated point scores `5.07` — a nearly fivefold gap. (The copy-vs-copy comparison is deliberate: holding the predictor fixed isolates the leakage itself, not predictor quality.) Random-split CV does not estimate generalization here; it estimates how well you can interpolate between adjacent samples. Exchangeability is the load-bearing assumption under "test error ≈ generalization error," and autocorrelated data violate it. The standard ML fix is to split so that train and test *are* exchangeable given what you condition on: forward-chain (train on the past, predict the future) or hold out contiguous blocks. The temporal-dependence models that make such data tractable — AR processes, state-space filters — are module 21's subject.
</details>

## Takeaways

- Probability has two readings — long-run frequency and coherent degree of belief — but **one calculus**: both obey Kolmogorov's axioms, forced by symmetry (Cox) or by no-sure-loss (Dutch book). Do not tribalize; switch modes.
- **Calibration** is where the readings meet: a coherent belief that is calibrated reproduces frequencies (ECE `0.007` honest vs `0.089` overconfident).
- **Exchangeability** — invariance to reordering — is the weak assumption that replaces iid. Exchangeable variables are identically distributed and equi-correlated but generally dependent.
- **de Finetti (infinite exchangeability):** the empirical frequency converges to a random limit Θ, and the sequence is a mixture of iid Bernoulli(Θ) with a unique mixing distribution G. **Θ is the parameter; G is the prior.** Parameters exist because of exchangeability, not philosophy.
- **Finite exchangeability is weaker:** without-replacement sampling is exchangeable with *negative* correlation −1/(N−1) that no mixture can produce; de Finetti's representation needs the sequence to extend to an infinite one.
- The **Pólya urn** is an exchangeable process that literally *is* the Beta-Bernoulli predictive (matching sequence probabilities to `1e-12`); it seeds the CRP in module 19 and realizes line 3 (prediction = marginalization) as a physical process.
- Exchangeability is an **assumption you can be wrong about**: it is the whole content of the permutation null, and the silent premise under every train/test benchmark — break it (time, groups, shift) and the number lies.

# 22. Decisions and Bandits: Uncertainty You Can Act On

> **Spine.** A posterior is not a deliverable — an *action* is; and when the action feeds back into the data you collect, Thompson sampling (draw $\theta$ from the posterior, act as if it were true) is embarrassingly simple and near-optimal.
> **Which line?** Line 4 — a decision minimizes posterior expected loss — first as a one-shot choice (a treatment threshold, a shipping call), then in its *sequential* form, where the action you take determines the next observation.
> **Promise.** After this module you can turn any calibrated probability into a cost-optimal action threshold (and see why $0.5$ is almost never it), drive an A/B test past "who won" to *ship-or-keep-testing* by pricing information, and implement a three-arm bandit tournament whose winner you can defend from five lines of arithmetic.
> **Prereqs.** Modules 05 (conjugate Beta updates, the A/B decision), 06 (loss → action, the classifier threshold as a Bayes rule), 08 (admissibility / complete-class).
> **Runtime.** ~20 s.
> **Sources.** C-B §8.3.5, §10 (decision sections); booklet ch. 8; Russo et al. *A Tutorial on Thompson Sampling* by concept; Lai–Robbins, Auer et al. (UCB) by concept.

The four lines (module 00): **a model is a joint $p(\text{unknowns},\text{knowns})$; inference is conditioning; prediction is marginalization; a decision minimizes posterior expected loss.** Modules 05–21 built posteriors. This module spends them. A posterior over a conversion rate, a disease probability, a set of arm-rewards is *worth nothing until it moves a hand* — until it picks a threshold, ships a variant, or pulls a lever. Line 4 is the whole of it: enumerate the actions, average the loss of each under the posterior, take the argmin. The twist that makes bandits their own subject is that in a sequential problem the *action changes the posterior you will hold tomorrow* — so acting and learning become the same move.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "22-decisions-bandits"            # this module's figure dir
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

## 22.1 Utility fixes the threshold — and it is almost never 0.5

A screening model reads a patient's data and returns $p = P(\text{disease}\mid \text{data})$. You must act: **treat** or **wait**. Two ways to be wrong carry two different costs. A *false positive* — treating a healthy patient — wastes a course of treatment, cost $C_{\text{FP}}$. A *false negative* — sending home a diseased patient — is the one that kills, cost $C_{\text{FN}}$. Correct actions cost nothing (relative to these). This is a $2\times 2$ loss matrix, and line 4 does the rest.

**Setup.** Take $C_{\text{FN}} = 10\,C_{\text{FP}}$: missing the disease is ten times as bad as an unnecessary treatment. A screening result comes back **88% healthy** — so $p = 0.12$.

**Predict.** Two commitments before any code. (a) Where is the action threshold — the probability $p^\star$ above which you treat? The reflex answer is $0.5$: treat if disease is more likely than not. (b) For *this* 12%-disease patient — 88% likely healthy — treat or send home?

**Reason.** The $0.5$ reflex silently assumes the two errors cost the same. Name it: it is the threshold you would use if a missed cancer and a wasted pill were equally bad.

**Run.** The expected loss of each action under the posterior $p$ is immediate:
$$\rho(\text{treat}) = (1-p)\,C_{\text{FP}}, \qquad \rho(\text{wait}) = p\,C_{\text{FN}}.$$
Treat when $\rho(\text{treat}) < \rho(\text{wait})$, i.e. $(1-p)C_{\text{FP}} < p\,C_{\text{FN}}$, which rearranges to
$$\boxed{\,p > p^\star = \dfrac{C_{\text{FP}}}{C_{\text{FP}} + C_{\text{FN}}}\,}.$$

```python
C_FP, C_FN = 1.0, 10.0                    # false negative 10x worse than false positive
p_star = C_FP / (C_FP + C_FN)             # cost-optimal action threshold
rho_treat = lambda p: (1 - p) * C_FP      # expected loss of treating
rho_wait  = lambda p: p * C_FN            # expected loss of waiting
print(f"threshold p* = C_FP/(C_FP+C_FN) = {p_star:.4f}   (naive default would be 0.5)")
for p in (0.08, p_star, 0.12):
    action = "TREAT" if p > p_star else "wait "
    print(f"  p={p:.4f}:  rho(treat)={rho_treat(p):.3f}  rho(wait)={rho_wait(p):.3f}  -> {action}")

pg = np.linspace(0, 0.30, 400)
fig, ax = plt.subplots()
ax.plot(pg, rho_treat(pg), color="C0", lw=2, label=r"$\rho(\mathrm{treat})=(1-p)\,C_{FP}$")
ax.plot(pg, rho_wait(pg),  color="C1", lw=2, label=r"$\rho(\mathrm{wait})=p\,C_{FN}$")
ax.axvline(p_star, color="k", ls="--", lw=1, label=f"threshold $p^*$ = {p_star:.3f}")
ax.plot(0.12, rho_wait(0.12), "o", color="C1", ms=8)
ax.annotate("88%-healthy patient (p=0.12):\nTREAT — the 0.5 rule\nwould send them home",
            xy=(0.12, rho_wait(0.12)), xytext=(0.16, 0.55),
            arrowprops=dict(arrowstyle="->", color="0.4"), fontsize=9)
ax.set_xlabel(r"$p = P(\mathrm{disease}\mid\mathrm{data})$"); ax.set_ylabel("expected loss")
ax.set_title(r"Two errors, two costs: treat above $p^*=1/11$, not 0.5")
ax.legend(loc="upper center")
save(fig, "threshold")
```

![Two straight expected-loss lines crossing at p=1/11: the treat-loss falls with p, the wait-loss rises with p; below the crossing you wait, above it you treat. The 12%-disease patient sits just right of the crossing — treat, though the 0.5 rule says wait.](figures/22-decisions-bandits/threshold.png)

**Reconcile.** The threshold is $p^\star = 1/11 = $ `0.0909` — the naive default of $0.5$ sits 5.5× above it. And if your part-(b) commitment followed the "12% < 50%, send home" reflex, you were caught: the 88%-healthy patient's expected losses are `0.880` to treat versus `1.200` to wait — the correct action is **TREAT**, and the $0.5$ rule would have sent home a patient the true costs say to treat. Under those costs you treat anyone above **9.1%**, because at 10:1 one missed case costs as much as ten unnecessary treatments — waiting for "more likely than not" spares pills at the price of far costlier misses. A patient at 8%, by contrast, waits — but *only just* (`0.920` to treat vs `0.800` to wait), a whisker below a threshold the naive rule placed 5.5× further out. The lesson compresses to one line the SYLLABUS insisted on: **$0.5$ is almost never the right threshold** — it is the special case $C_{\text{FP}} = C_{\text{FN}}$, and real losses are lopsided.

This is module 06's claim cashed out — "a classifier threshold is a Bayes rule; $0.5$ is optimal only under symmetric costs." Two footnotes worth stating. **ROC in one line:** sweeping $p^\star$ from 0 to 1 traces the ROC curve; the cost ratio picks the operating point where the iso-cost line is tangent to the curve — Bayes-optimal classification is *choosing the point*, never defaulting to the middle. **Calibration poisons or saves it (module 15):** the number $1/11$ only means what it says if $p$ is *calibrated* — feed the rule a model that reports 0.08 when the empirical disease rate among such patients is really 0.15 and the threshold silently mis-triages. A decision is only as trustworthy as the probability feeding it.

## 22.2 The A/B test, driven past "who won" to "ship or keep testing"

Module 05 ran an A/B test to a shipping decision and stopped there; this section adds the third action every practitioner actually faces. Two ad variants: **A** converts 41 of 1000, **B** converts 57 of 1000. Flat $\mathrm{Beta}(1,1)$ priors give posteriors $\mathrm{Beta}(42, 960)$ and $\mathrm{Beta}(58, 944)$. The decision loss is *regret*: ship the worse arm and you forfeit the conversion-rate gap on every future impression.

**Predict.** One spoiler, one commitment. $P(\theta_B>\theta_A)$ will print $\approx 0.95$. From that 95% win-probability alone, guess the **ratio of ship-A's expected regret to ship-B's** — the anchor is 19-to-1 (odds of 0.95 to 0.05). If module 05 already caught you on this, state from memory *why* 19-to-1 is wrong before the code confirms it.

```python
def beta_binomial_update(a, b, s, f):     # module 05's helper
    return a + s, b + f

postA = beta_binomial_update(1, 1, s=41, f=1000-41)      # Beta(42, 960)
postB = beta_binomial_update(1, 1, s=57, f=1000-57)      # Beta(58, 944)

rng_ab = np.random.default_rng(4)
M = 500_000
tA = stats.beta(*postA).rvs(size=M, random_state=rng_ab)
tB = stats.beta(*postB).rvs(size=M, random_state=rng_ab)

p_B_beats_A = np.mean(tB > tA)
loss_ship_B = np.mean(np.maximum(tA - tB, 0.0))   # regret if A was really better
loss_ship_A = np.mean(np.maximum(tB - tA, 0.0))   # regret if B was really better
print(f"P(theta_B > theta_A)         = {p_B_beats_A:.4f}")
print(f"expected regret | ship B     = {loss_ship_B:.6f}  (per future impression)")
print(f"expected regret | ship A     = {loss_ship_A:.6f}")
print(f"regret ratio ship-A : ship-B = {loss_ship_A/loss_ship_B:.0f}x  -> ship B")
```

**Reconcile.** Between the two *terminal* actions, module 05's beat repeats exactly: $P(\theta_B > \theta_A) = $ `0.9510`, but the regret ratio is `81`×, not the anchored 19-to-1 — a probability weighs *worlds*, a loss weighs *worlds × stakes*, and in the 5% of worlds where A wins the two arms are nearly tied, so being wrong there is nearly free. Ship B. But there is a third action — **keep testing** — and it is not free and not worthless. Pricing it is the value of information, and it is what tells you *when to stop*.

## 22.3 The price of information: EVSI and when to stop

Collecting more data can only sharpen a decision — but it costs samples, and past some point the sharpening is not worth the sampling. The **expected value of sample information** (EVSI) is exactly the expected reduction in decision loss from a planned batch of $n$ more observations per arm, computed *before* you collect them by simulating the futures they might produce (the **preposterior** — module 05's posterior predictive, one level up).

The construction is a two-line thought. Right now, ship-B's expected regret over a horizon of $H$ future impressions is $H \cdot \mathbb{E}[\max(\theta_A-\theta_B, 0)]$ — this is also the **expected value of perfect information** (EVPI), the most any amount of data could ever save you, because even an oracle can only stop you from shipping the wrong arm. With $n$ more samples per arm you would update the posteriors and re-decide; the residual regret is smaller. EVSI is the gap. Vectorize it: draw $R$ "true worlds" $(\theta_A,\theta_B)$ from the current posteriors, simulate the future counts in each world at once, re-decide in each, and average.

**Predict.** Take $H = 10^6$ remaining impressions and a per-sample cost of 0.010 conversions. Before running: is collecting **1000 more impressions per arm** worth it — is its EVSI above or below its sampling cost? The reflex, given $P(B>A)$ is only 95% (a real 1-in-20 chance of shipping the wrong arm across a million impressions), is that more data is obviously worth buying.

**Reason.** That reflex prices information by *how uncertain you feel*, ignoring that the value is capped by the EVPI and that a modest batch may not move the decision at all.

```python
R = 200_000
th_A = rng.beta(*postA, size=R)                  # candidate true worlds ~ current posterior
th_B = rng.beta(*postB, size=R)
best = np.maximum(th_A, th_B)
H = 1_000_000                                     # remaining impressions the shipped arm will serve
c_s = 0.010                                       # cost per extra test impression (in conversions)

# No more data: ship B (the current posterior-mean winner). Regret = EVPI.
regret_now = np.mean(best - th_B) * H
EVPI = regret_now
print(f"EVPI = H * E[max(thA-thB,0)] = {EVPI:.1f} conversions  (regret of shipping now)")

# How settled is the race? B's lead in units of the uplift's posterior sd (exact Beta moments).
dA, dB = stats.beta(*postA), stats.beta(*postB)
lead = (dB.mean() - dA.mean()) / np.sqrt(dA.var() + dB.var())
print(f"B's standardized lead = (E[thB]-E[thA]) / sd(thB-thA) = {lead:.2f} sigma")

ns = np.array([250, 500, 1000, 2000, 4000, 8000, 16000, 32000])
aA, bA = postA; aB, bB = postB
evsi, cost = [], []
for n in ns:
    sA = rng.binomial(n, th_A); sB = rng.binomial(n, th_B)     # future successes, per world
    muA = (aA + sA) / (aA + bA + n)                            # updated posterior means
    muB = (aB + sB) / (aB + bB + n)
    chosen = np.where(muA > muB, th_A, th_B)                   # the decision the new data would drive
    regret_after = np.mean(best - chosen) * H
    evsi.append(regret_now - regret_after)
    cost.append(2 * n * c_s)                                   # n per arm, two arms
evsi, cost = np.array(evsi), np.array(cost)

net = evsi - cost
n_star = ns[np.argmax(net)]
for n, v, c in zip(ns, evsi, cost):
    flag = "keep testing" if v > c else "stop & ship "
    print(f"  n={n:>5}/arm: EVSI={v:7.1f}  cost={c:6.1f}  net={v-c:7.1f}  -> {flag}")
print(f"best batch n* = {n_star}/arm (max net value {net.max():.1f} conversions)")

fig, ax = plt.subplots()
ax.plot(ns, evsi, "o-", color="C1", lw=2, label="EVSI(n): value of the data")
ax.plot(ns, cost, "s-", color="C3", lw=2, label=f"cost(n) = 2n x {c_s}")
ax.axhline(EVPI, color="k", ls="--", lw=1, label=f"EVPI = {EVPI:.0f} (perfect info ceiling)")
ax.axvline(n_star, color="0.5", ls=":", lw=1)
ax.set_xscale("log"); ax.set_xlabel("extra samples per arm, n"); ax.set_ylabel("conversions")
ax.set_title("Buy information while value > price; EVSI saturates at EVPI")
ax.legend(loc="center right")
save(fig, "evsi")
```

![EVSI rising and saturating toward the EVPI ceiling as n grows, the linear cost line rising through it; the two cross, and net value peaks at an interior batch size.](figures/22-decisions-bandits/evsi.png)

**Reconcile.** Collecting 1000 more per arm is worth it — but *barely*: EVSI `22.2` against a cost of `20.0`, net `2.2` conversions, nothing like the runaway the "1-in-20 chance, obviously buy" reflex expected. The ceiling explains why. **EVPI = `200.2` conversions** — shipping now, over a million impressions, risks about two hundred conversions, and that is the entire prize on offer: even an oracle could only save you from shipping the wrong arm. EVSI is S-shaped as the batch grows. A tiny 250-per-arm batch adds almost nothing (EVSI `0.0`) because it rarely overturns B's `1.64`$\sigma$ standardized lead (printed above from the exact Beta moments); mid-size batches can (`22.2` at $n{=}1000$); then it saturates toward the ceiling (`148.4` at $n{=}8000$) while cost climbs linearly. Net value is a hump — negative for batches too small to flip the decision and for batches so large that cost overruns the capped value — peaking at $n^\star = $ `4000` per arm, net `27.9` conversions. So the decision at the current state is **keep testing**: a net-positive batch exists, buy it, and by the time it lands the EVSI of *further* data will have fallen below cost and you ship. The one-sentence rule the SYLLABUS asked for: **information has a price and a value; buy while the value exceeds the price, and stop the moment it does not.** Had B converted a more decisive 80 of 1000, the posteriors would barely overlap, EVPI would collapse, and even the first extra sample would not pay — you would ship immediately (Exercise 22.4 makes you predict the collapse). This EVSI machinery is the design bridge to module 23, where you price information *before* the experiment exists.

## 22.4 The bandit tournament: acting and learning are the same move

Everything above was one-shot: decide, done. Now close the loop. You have three ad variants (arms) with unknown conversion rates; on each of $T$ impressions you pull one arm, see a Bernoulli reward, and update. The action determines the next data point, so *exploring* (pulling an uncertain arm to learn) and *exploiting* (pulling the current best to earn) are in tension. The score is **cumulative regret** — total conversions forgone versus an oracle that always pulls the best arm:
$$\text{Regret}(T) = \sum_{t=1}^{T} \big(\theta^\star - \theta_{a_t}\big), \qquad \theta^\star = \max_a \theta_a.$$

Three policies enter. **$\varepsilon$-greedy** ($\varepsilon=0.1$): pull the empirical-best arm, but with probability $\varepsilon$ pull a uniformly random arm — a fixed exploration tax forever. **UCB1**: pull $\arg\max_a \big[\hat\mu_a + \sqrt{2\ln t / n_a}\big]$ — act on an *optimistic upper confidence bound*, so rarely-pulled arms look attractive until proven otherwise (Auer et al.). **Thompson sampling**, derivable in five lines:

1. Each arm's rate has a posterior $\theta_a \mid \text{data} \sim \mathrm{Beta}(\alpha_a, \beta_a)$ (module 05's Beta update, one per arm).
2. You want to pull each arm as often as it is *probably* the best.
3. Draw one sample $\tilde\theta_a \sim \mathrm{Beta}(\alpha_a,\beta_a)$ from every arm's posterior.
4. Pull $a_t = \arg\max_a \tilde\theta_a$.
5. Then $P(\text{pull } a) = P(a \text{ is best}\mid\text{data})$ — *probability matching*, with exploration built in for free: a wide posterior occasionally samples high, an established loser rarely does.

**Predict.** Before running: **rank the three policies by cumulative regret** at $T=10^4$, best (lowest) to worst. The tempting order puts UCB1 first — it is the one with the famous logarithmic-regret proof — then Thompson, then $\varepsilon$-greedy.

**Reason.** The intuition being tested: "the algorithm with the tightest theoretical bound wins in practice, and a dead-simple one-line posterior draw cannot beat a hand-tuned confidence bound."

**Run.** The panel mandates a vectorized simulation: $10^4$ pulls $\times$ 100 independent replications, with the Python loop over *pulls only* — every one of the 100 reps advances simultaneously through numpy on `(reps, arms)`-shaped state, and there is **no per-pull loop over reps**.

```python
rates = np.array([0.3, 0.5, 0.7])         # true arm rates; arm 2 is best (theta* = 0.7)
K = len(rates); best_rate = rates.max()
T, REPS = 10_000, 100

def run_bandit(policy, seed):
    """Vectorized bandit: loop over pulls, all REPS advance at once (no rep loop)."""
    g = np.random.default_rng(seed)
    rows = np.arange(REPS)
    alpha = np.ones((REPS, K)); beta = np.ones((REPS, K))   # Beta(1,1) per rep, per arm
    n = np.zeros((REPS, K)); s = np.zeros((REPS, K))        # counts, successes (freq. policies)
    inst = np.empty(T)                                      # mean instantaneous regret per pull
    for t in range(T):
        if policy in ("ucb1", "egreedy") and t < K:
            arm = np.full(REPS, t)                          # seed each arm once
        elif policy == "thompson":
            arm = g.beta(alpha, beta).argmax(axis=1)        # sample posterior, play the argmax
        elif policy == "egreedy":
            explore = g.random(REPS) < 0.1
            greedy = (s / np.maximum(n, 1)).argmax(axis=1)
            arm = np.where(explore, g.integers(0, K, REPS), greedy)
        elif policy == "ucb1":
            ucb = s / n + np.sqrt(2 * np.log(t + 1) / n)     # n>0 here (all arms seeded)
            arm = ucb.argmax(axis=1)
        reward = (g.random(REPS) < rates[arm]).astype(float)
        alpha[rows, arm] += reward; beta[rows, arm] += 1 - reward
        s[rows, arm] += reward; n[rows, arm] += 1
        inst[t] = np.mean(best_rate - rates[arm])           # regret averaged over reps
    return np.cumsum(inst)

curves = {name: run_bandit(name, seed=100 + i)
          for i, name in enumerate(["thompson", "ucb1", "egreedy"])}
print("cumulative regret at T = 10,000 (mean over 100 reps):")
for name in ["thompson", "ucb1", "egreedy"]:
    print(f"  {name:9s}: {curves[name][-1]:7.1f}")
ranking = sorted(curves, key=lambda k: curves[k][-1])
print("ranking (best first):", " < ".join(ranking))
gap = curves["egreedy"][-1] / curves["thompson"][-1]
print(f"epsilon-greedy regret / Thompson regret = {gap:.1f}x")

fig, ax = plt.subplots()
colors = {"thompson": "C0", "ucb1": "C1", "egreedy": "C3"}
tt = np.arange(1, T + 1)
for name in ["thompson", "ucb1", "egreedy"]:
    ax.plot(tt, curves[name], color=colors[name], lw=2, label=name)
ax.set_xlabel("pull t"); ax.set_ylabel("cumulative regret")
ax.set_title(r"3-arm Bernoulli (0.3/0.5/0.7): Thompson $<$ UCB1 $\ll$ $\varepsilon$-greedy")
ax.legend()
save(fig, "bandit-regret")
```

![Three cumulative-regret curves. Thompson and UCB1 bend over and flatten (logarithmic), Thompson lowest; epsilon-greedy keeps climbing on a near-straight line because it explores 10% forever.](figures/22-decisions-bandits/bandit-regret.png)

**Reconcile.** The ranking is `thompson < ucb1 < egreedy`. Thompson's cumulative regret is `19.6`, UCB1's `99.7`, and $\varepsilon$-greedy's `212.4` — the one-line posterior draw *wins*, and the "clever" confidence bound comes second. The naive ranking that trusted UCB1's proof missed two things. First, the logarithmic bound is a worst-case *guarantee*, not a typical-case ranking; Thompson's Bayesian exploration adapts to the actual posterior and usually explores less wastefully. Second, $\varepsilon$-greedy's curve barely bends: because it spends a fixed 10% of pulls exploring uniformly *forever*, its regret grows **linearly** — `10.8`× Thompson's here and widening without bound as $T\to\infty$, while Thompson and UCB1 flatten toward logarithmic. Constant exploration is the trap; the good policies explore *less* as they learn *more*, which is exactly what acting under a shrinking posterior does automatically.

## 22.5 Exploration is acting under a posterior, not a point

Look at what the three winners have in common: none of them plugs in a point estimate and acts as if it were the truth. $\varepsilon$-greedy hedges with random detours; UCB1 acts on an optimistic bound; Thompson acts on a posterior draw. All three are answers to the same question — *how do you act while $\theta$ is still uncertain?* The plug-in alternative, **pure greedy** (always pull the empirical-best arm, $\varepsilon=0$), is precisely module 05's overconfident MLE in a sequential costume, and it pays for the overconfidence by sometimes locking permanently onto a wrong arm that got lucky early and never gets re-examined (Exercise 22.2). **Exploration is not a bolt-on heuristic; it is what acting under a posterior instead of a point looks like.** This is the Bayesian reading of exploration in reinforcement learning: Thompson sampling generalizes to deep RL as posterior-sampling and bootstrapped/ensemble value functions — sample a plausible world, act optimally in it, observe, update (Russo et al. by concept).

And the deepest reassurance is module 08's complete-class theorem, turned around to point at you. It said: every admissible decision rule is a Bayes rule (or a limit of them) against *some* prior — the risk-set boundary is traced by Bayes rules and nothing else. So whatever undominated procedure you deploy here — a treatment threshold, a stopping rule, a bandit policy — there exists a prior under which it *is* the posterior-expected-loss minimizer. **You were always going to act like a Bayesian; the only question is which prior.** Choosing it in the open, as every section above did, beats having it reverse-engineered from your defaults after the fact.

## Bridge — decision theory is line 4, and the frequentist tools are its audit

C-B develops loss, risk, and admissible rules (§8.3, §10) as a frequentist apparatus; read through the four lines they are one machine. The **Bayes rule** (C-B §7.3.4) is line 4 verbatim — minimize posterior expected loss — and it produced every action in this module: the threshold (a two-action argmin), the ship decision (a three-action argmin), the bandit pull (a $K$-action argmin under a sequential posterior). The **complete-class theorem** (§10, module 08) certifies that no undominated rule escapes this frame. **Regret**, the bandit's frequentist scorecard, is the sequential twin of James–Stein's risk: an unconditional, worst-case-flavored audit of a procedure whose *construction* is Bayesian. The ML reader has met all of this before under other names — a cost-sensitive classifier threshold, an acquisition function in Bayesian optimization, an exploration bonus in RL — and the through-line is that each is line 4 applied to a different action set, with the posterior doing the averaging.

## Pitfalls

- **Defaulting to a 0.5 threshold.** That is optimal only when $C_{\text{FP}} = C_{\text{FN}}$. The Bayes threshold is $C_{\text{FP}}/(C_{\text{FP}}+C_{\text{FN}})$ (§22.1); for a 10:1 cost ratio it is $1/11$, and for a 100:1 ratio it is $1/101$ — routinely an order of magnitude from the middle.
- **Feeding a threshold an uncalibrated probability.** $p^\star$ is only meaningful if $p$ means what it says (module 15). A model that reports 0.08 when the true rate is 0.15 mis-triages at *any* threshold; calibrate first, threshold second.
- **Stopping an A/B test at $P(B>A)$.** That is line 2. The shipping decision is line 4 and needs a loss (§22.2); "keep testing" is a third action to be priced by EVSI, not an afterthought.
- **Constant exploration forever.** A fixed $\varepsilon$ makes regret grow *linearly* (§22.4). Decay $\varepsilon$, or use a policy (UCB1, Thompson) whose exploration shrinks as the posterior sharpens.
- **Pure greedy / plug-in acting in a bandit.** Always pulling the empirical-best arm ($\varepsilon=0$) can lock onto a wrong arm that got a lucky start and never revisit it — the overconfident MLE, sequential edition (Exercise 22.2).

## Exercises

**Exercise 22.1 — The threshold moves an order of magnitude.**
*Setup:* Same screening setup, but now a missed case is *100×* worse than a needless treatment: $C_{\text{FN}} = 100\,C_{\text{FP}}$.
*Predict:* Where does the action threshold land — still near $1/11 \approx 0.09$, or dramatically lower? And what fraction of a calibrated cohort with disease probabilities $\sim \mathrm{Beta}(2, 40)$ (mean $\approx 0.048$) now gets treated?
*Reason:* "A 10× change in one cost nudges the threshold a bit" — treating the threshold as roughly stable.
*Run:*
```python
p_star_10  = 1 / (1 + 10)
p_star_100 = 1 / (1 + 100)
cohort = stats.beta(2, 40).rvs(size=200_000, random_state=np.random.default_rng(7))
frac10  = np.mean(cohort > p_star_10)
frac100 = np.mean(cohort > p_star_100)
print(f"threshold at 10:1  = {p_star_10:.4f},  treated fraction = {frac10:.3f}")
print(f"threshold at 100:1 = {p_star_100:.4f}, treated fraction = {frac100:.3f}")
```
<details><summary>Reconcile</summary>

The threshold drops from `0.0909` to `0.0099` — nearly a full order of magnitude, because $p^\star = C_{\text{FP}}/(C_{\text{FP}}+C_{\text{FN}}) \approx C_{\text{FP}}/C_{\text{FN}}$ once $C_{\text{FN}}$ dominates, so it scales *inversely* with the cost ratio, not additively. The treated fraction jumps from `0.101` to `0.937`: raise the stakes of a miss and the cost-optimal policy treats almost everyone with any material risk. The general lesson — thresholds are set by cost *ratios*, and extreme ratios (fraud, cancer, safety) push the operating point far into a corner of the ROC curve where "accuracy" is a useless metric because you are deliberately accepting many false positives to catch the rare, expensive miss.
</details>

**Exercise 22.2 — Pure greedy locks in.**  *(surprising)*
*Setup:* Drop exploration entirely: a **pure-greedy** bandit ($\varepsilon = 0$) that always pulls the arm with the highest empirical mean, on the same 0.3/0.5/0.7 arms, 100 reps, but a shorter $T=2000$.
*Predict:* Greedy wastes nothing on exploration, so its *mean* regret should beat $\varepsilon$-greedy's. True — or does removing exploration backfire?
*Reason:* "Exploration is pure overhead; a policy that never wastes a pull on a known-worse arm must have lower regret."
*Run:*
```python
def run_greedy(seed, T=2000):
    g = np.random.default_rng(seed); rows = np.arange(REPS)
    s = np.zeros((REPS, K)); n = np.zeros((REPS, K)); inst = np.empty(T)
    for t in range(T):
        if t < K:
            arm = np.full(REPS, t)
        else:
            arm = (s / n).argmax(axis=1)                 # pure exploit, no exploration
        reward = (g.random(REPS) < rates[arm]).astype(float)
        s[rows, arm] += reward; n[rows, arm] += 1
        inst[t] = np.mean(best_rate - rates[arm])
    # per-rep final choice, to expose lock-in
    final_arm = (s / n).argmax(axis=1)
    return np.cumsum(inst)[-1], np.mean(final_arm != 2)   # regret, P(locked on a wrong arm)
reg, wrong = run_greedy(seed=0)
print(f"pure-greedy regret at T=2000 = {reg:.1f};  reps locked on a SUBOPTIMAL arm = {wrong:.2f}")
```
<details><summary>Reconcile</summary>

Pure greedy's regret is `262.6` and — the tell — `0.42` of the 100 reps end **locked onto a suboptimal arm**. Removing exploration backfires badly: that regret is far worse than any *exploring* policy on the same arms, because with no forced re-examination an arm that opens with a lucky streak can hold the lead forever while the truly-best arm, unlucky early, is never pulled again to correct the record. That is *incomplete learning* — the sequential face of module 05's overconfident MLE, which read certainty from two data points. A little exploration is not overhead; it is the premium you pay for the guarantee that the best arm eventually gets a fair hearing. Thompson pays that premium automatically and adaptively, which is why it flattens while greedy risks a linear-regret tail.
</details>

**Exercise 22.3 — The exploration sweet spot is a valley.**
*Setup:* Sweep $\varepsilon$-greedy's exploration rate $\varepsilon \in \{0.01, 0.05, 0.1, 0.2, 0.4\}$ on the same arms, $T=5000$, 100 reps.
*Predict:* Is regret monotone in $\varepsilon$ (more exploration always worse, so $\varepsilon=0.01$ wins), or is there an interior minimum?
*Reason:* "Exploration is a tax, so less is always better" — the same intuition Exercise 22.2 just dented from the other side.
*Run:*
```python
def run_eps(eps, seed, T=5000):
    g = np.random.default_rng(seed); rows = np.arange(REPS)
    s = np.zeros((REPS, K)); n = np.zeros((REPS, K)); inst = np.empty(T)
    for t in range(T):
        if t < K:
            arm = np.full(REPS, t)
        else:
            explore = g.random(REPS) < eps
            arm = np.where(explore, g.integers(0, K, REPS), (s / n).argmax(axis=1))
        reward = (g.random(REPS) < rates[arm]).astype(float)
        s[rows, arm] += reward; n[rows, arm] += 1
        inst[t] = np.mean(best_rate - rates[arm])
    return np.cumsum(inst)[-1]
for eps in (0.01, 0.05, 0.1, 0.2, 0.4):
    print(f"  eps={eps:.2f}: regret at T=5000 = {run_eps(eps, seed=1):.1f}")
```
<details><summary>Reconcile</summary>

Regret is **U-shaped** in $\varepsilon$: `65.1` at 0.01, a shade lower at `64.1` for 0.05, then climbing steeply to `108.8`, `206.3`, `405.8`. Too little exploration and you risk the lock-in of Exercise 22.2 (slow to correct a bad early lead); too much and you pay the linear tax of §22.4 (throwing away pulls on known losers). The optimum is interior — here near $\varepsilon \approx 0.05$, with over-exploration far more punishing than under-exploration at this horizon — and, worse, it depends on the horizon and the arm gaps, so it needs tuning. That fragility is the practical case *for* Thompson and UCB1: they have no exploration knob to mis-set because their exploration is *derived* from the posterior, shrinking on its own at the right rate.
</details>

**Exercise 22.4 — When more data isn't worth buying.**  *(decision / ML bridge)*
*Setup:* Rerun the EVSI logic of §22.3 but for a *decisive* result: B converts **80** of 1000, A still 41 of 1000. Same horizon $H=10^6$, same per-sample cost $c_s=0.01$.
*Predict:* With B now a runaway winner, is the EVPI (the whole prize from any further data) still ~200 conversions, or has it collapsed? Would you buy even 250 more samples per arm?
*Reason:* "There's still uncertainty, so more data still has real value" — treating value-of-information as roughly constant in how separated the arms already are.
*Run:*
```python
pA = beta_binomial_update(1, 1, 41, 959)
pB = beta_binomial_update(1, 1, 80, 920)          # decisive winner
g = np.random.default_rng(3); R = 200_000
a, b = g.beta(*pA, size=R), g.beta(*pB, size=R)
EVPI2 = np.mean(np.maximum(a, b) - b) * 1_000_000
n = 250
sA = g.binomial(n, a); sB = g.binomial(n, b)
muA = (pA[0]+sA)/(pA[0]+pA[1]+n); muB = (pB[0]+sB)/(pB[0]+pB[1]+n)
chosen = np.where(muA > muB, a, b)
EVSI2 = EVPI2 - np.mean(np.maximum(a, b) - chosen) * 1_000_000
print(f"EVPI (80/1000 vs 41/1000) = {EVPI2:.2f} conversions")
print(f"EVSI of 250 more/arm = {EVSI2:.2f}  vs cost {2*250*0.01:.1f}  -> "
      f"{'buy' if EVSI2 > 2*250*0.01 else 'SHIP NOW'}")
```
<details><summary>Reconcile</summary>

EVPI collapses to `0.27` conversions — with B at 80/1000 the posteriors barely overlap ($P(\theta_B>\theta_A)$ is essentially 1), so the entire remaining prize from perfect information is well under one conversion. EVSI of 250 more per arm is `0.00`, dwarfed by the `5.0`-conversion sampling cost: **ship now**. The value of information is not a property of your horizon alone; it scales with how *unresolved* the decision still is. Once the posterior has separated the arms, buying more data is buying certainty you have already effectively purchased — the sequential version of "the interval has stopped moving, stop paying to shrink it." This is the same stopping logic behind early-stopping an experiment and behind an acquisition function going quiet in Bayesian optimization (module 23).
</details>

## Takeaways

- **A posterior is not a deliverable — an action is.** Line 4 (minimize posterior expected loss) turns every posterior in the course into a decision: a threshold, a ship call, a bandit pull.
- **Utility fixes the threshold, and it is almost never 0.5.** Act when $p > C_{\text{FP}}/(C_{\text{FP}}+C_{\text{FN}})$; for a 10:1 cost ratio that is $1/11 \approx$ `0.0909`. The threshold is a cost *ratio*, so extreme stakes push it into a corner of the ROC curve — and it only means what it says on a *calibrated* probability.
- **Ship-or-keep-testing is a three-action decision.** The A/B winner is line-2 ($P(B>A)=$ `0.9510`); the decision is line-4 (regret ratio `81`×, ship B); the third action, keep testing, is priced by EVSI.
- **Information has a price and a value; buy while value > price.** EVSI is the expected loss reduction from a planned batch (preposterior simulation), capped by the EVPI = current expected regret; stop the moment the next batch's value falls below its cost — and note the value collapses once the arms separate.
- **Thompson sampling is five lines and wins.** Draw $\tilde\theta_a$ from each Beta posterior, pull the argmax; this matches $P(a\text{ is best})$ and beats UCB1 and $\varepsilon$-greedy (regret `19.6` < `99.7` < `212.4`) with exploration that shrinks on its own.
- **Constant exploration gives linear regret; plug-in greedy locks in.** A fixed $\varepsilon$ never stops taxing you; $\varepsilon=0$ can freeze onto a lucky-early wrong arm — the overconfident MLE, sequential edition. Good policies explore *less* as the posterior sharpens.
- **You were always going to act like a Bayesian; the only question is which prior.** Module 08's complete-class theorem: every undominated rule is a Bayes rule against some prior, so exploration is not a heuristic — it is acting under a posterior instead of a point.

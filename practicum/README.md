# The Bayesian Practicum

**A beginner's field guide to actually using Bayesian statistics — fourteen
real problems, one workflow, all the code runs.**

Every chapter starts with a decision somebody has to make: take the umbrella or
not, ship the redesign or not, staff four people or six, raise the price or
hold, send the retention offer to whom. It then runs the same seven-step loop on
it, in Python you can execute, and ends with an action and a number in euros or
minutes rather than an interval and a shrug.

## Why this exists

The companion course in [`curriculum/`](../curriculum/) is a rigorous rebuild of
statistical and machine learning on a Bayesian foundation — 27 modules,
theorem-first, referee-verified. It is excellent for *knowing* the subject. It
is not what you reach for when someone hands you a CSV on a Tuesday.

This guide is the other half. It borrows the workflow discipline and the
intuition-building style of McElreath's *Statistical Rethinking* — simulate
before you fit, check what the model can and cannot produce, draw the causal
graph before choosing variables — and applies them to everyday problems,
economic problems, and the machine-learning tools you already use. Where a
chapter needs theory, it points at the module in `curriculum/` that proves it
rather than half-proving it here.

**Who it's for:** you can write Python, you have seen probability, and you have
possibly even taken a statistics course, but you would not currently know how to
turn a dataset into a decision you could defend. No measure theory, no
conjugate-prior tables, no R.

## The loop

Every chapter runs the same seven steps. The one-page version is
[WORKFLOW.md](WORKFLOW.md); print it.

```
   1 QUESTION  ──▶  2 STORY  ──▶  3 MODEL  ──▶  4 PRIOR CHECK
                                                      │
        ┌─────────────────────────────────────────────┘
        ▼
   5 FIT  ──▶  6 CHECK  ──▶  7 DECIDE
        ▲          │
        └──────────┘
```

## The chapters

**Part I — The loop, on everyday problems**

| | | |
|---|---|---|
| [00](chapters/00-draw-the-owl.md) | **Draw the owl** | All seven steps on one small decision: take the umbrella? The threshold is 0.20, not 0.5. |
| [01](chapters/01-counting-the-ways.md) | **Counting the ways** | Posteriors by literally counting paths, then by grid. Where grids die. |
| [02](chapters/02-a-bag-of-numbers.md) | **The posterior is a bag of numbers** | Every question is `np.mean` of something. Intervals, loss-driven estimates, and why most positive tests are false. |
| [03](chapters/03-priors-you-can-defend.md) | **Priors you can defend** | Simulate the data your prior implies. "Uninformative" priors predict 45-hour commutes. |
| [04](chapters/04-lines-with-error-bars.md) | **Lines with error bars** | Regression as a story, and the two intervals people conflate — they differ by 12×. |
| [05](chapters/05-when-the-math-runs-out.md) | **When the math runs out** | Metropolis in fifteen lines, NUTS in NumPyro, and the diagnostics that catch a wrong answer. |
| [06](chapters/06-does-the-golem-fit.md) | **Does the golem fit?** | Posterior predictive checks. A perfectly converged model that would understaff you two days in ten. |

**Part II — Money**

| | | |
|---|---|---|
| [07](chapters/07-the-ab-test-you-can-act-on.md) | **The A/B test you can act on** | Expected loss in euros, and what peeking does and does not break. |
| [08](chapters/08-prices-and-causes.md) | **Prices and causes** | A regression that says raising prices raises sales. Confounders, colliders, instruments. |
| [09](chapters/09-many-small-units.md) | **Many small units** | Why the top of every league table regresses by half, and the model that fixes it. |
| [10](chapters/10-money-is-not-linear.md) | **Money is not linear** | Insurance, the Kelly criterion, and what a study is worth before you commission it. |

**Part III — Learning**

| | | |
|---|---|---|
| [11](chapters/11-regularisation-is-a-prior.md) | **Regularisation is a prior** | Ridge equals a Gaussian prior to 3e-16. "No regularisation" is a claim, and a bad one. |
| [12](chapters/12-which-model-and-how-sure.md) | **Which model, and how sure?** | PSIS-LOO from one fit, and the standard error nobody reports. |
| [13](chapters/13-probabilities-that-mean-something.md) | **Probabilities that mean something** | Calibration you can check, and a threshold that captures 8× the value of the default. |

Then [CAPSTONE.md](CAPSTONE.md): three questions, three datasets, no scaffolding.

## How to use it

- **Read in order.** Later chapters lean on earlier printed numbers and reuse
  the same datasets, so the commute you met in chapter 01 is the commute you
  model in chapter 03.
- **Play the Predict beats honestly.** Exercises are staged *Setup → Predict →
  Run → Reconcile*: commit to a number before running the code. Being caught
  wrong is the mechanism; reading the answer is not.
- **Run everything.** Every block executes in order, deterministically, in
  seconds:
  ```bash
  cd practicum
  python tools/run_chapter.py chapters/04-lines-with-error-bars.md
  python tools/run_chapter.py --all --check      # everything, twice, for determinism
  ```
  Prefer notebooks? [`notebooks/`](notebooks/) has one per chapter, generated
  from the chapter markdown with byte-identical code.
- **Steal the toolbox.** [`bayeskit.py`](bayeskit.py) is ~200 readable lines:
  grid posteriors, HDI, the quadratic approximation, R-hat and ESS, PSIS-LOO,
  calibration. It is meant to be read, and `tools/check_kit.py` is the receipt
  that its diagnostics match ArviZ.

## Setup

Python ≥ 3.10 and:

```bash
pip install numpy scipy matplotlib pandas scikit-learn numpyro jax nbformat
# optional, only for tools/check_kit.py:
pip install arviz
```

No internet, no GPU, no R. Everything runs on a laptop; the slowest chapter
takes about a minute. All data is synthetic and generated by
[`data/make_data.py`](data/make_data.py), which documents the true process
behind every file — so when a chapter asks you to recover a number, you can
check whether you actually did.

## What "verified" means here

`tools/run_chapter.py` enforces three things on every chapter:

1. **It runs.** Every code block executes top to bottom, in order, in one
   namespace, with no manual fixes.
2. **It repeats.** Two runs print byte-identical output (fixed seeds
   everywhere).
3. **The numbers are real.** Every number quoted in prose in `backticks` must
   appear in the printed output of some block. Nothing is hand-typed, and
   nothing is stale.

If you edit a chapter and the numbers stop matching, the harness tells you.

## Where to go next

This guide teaches judgement and workflow. For the mathematics behind any of
it, the companion course goes deeper on every thread:

| If you want | Go to |
|---|---|
| Why conditioning is inference, in full | `curriculum/modules/02-conditioning-is-inference.md` |
| Conjugate updating and the shrinkage formula | `curriculum/modules/05-conjugate-updating.md` |
| Which estimator a loss function implies | `curriculum/modules/06-estimates-are-decisions.md` |
| Where Bayesian and frequentist answers agree and diverge | `curriculum/modules/08-frequentist-bridge.md` |
| MCMC properly: MH, Gibbs, HMC, why geometry wins | `curriculum/modules/09-` … `12-` |
| Hierarchical models in depth (eight schools) | `curriculum/modules/16-hierarchical.md` |
| Marginal likelihood, Bayes factors, Lindley's paradox | `curriculum/modules/17-model-checking.md` |
| Causal identification, potential outcomes, IPW | `curriculum/modules/24-causal.md` |
| Deep learning through Bayesian lenses | `curriculum/modules/25-deep-learning-lenses.md` |

And the source books, in this repository:

- `curriculum_material/statistical_rethinking/` — McElreath, chapters 1–8
  (transcribed). Chapters 2, 3, 4, 5, 6 and 7 are the direct ancestors of this
  guide's chapters 01, 02, 03/04, 08 and 12.
- `curriculum_material/bayesian_booklet/` — the MA 556 lecture notes: conjugate
  inference, hierarchical models, Gibbs, Metropolis–Hastings, nonparametric
  Bayes.
- `curriculum_material/islp/` — *Introduction to Statistical Learning with
  Python*, for the machine-learning side.

Terminology varies wildly between those sources. [GLOSSARY.md](GLOSSARY.md)
maps the words to each other.

---

*14 chapters · 31,600 words of prose · 170 runnable code blocks · 29 generated
figures · 42 worked exercises · every quoted number machine-checked against the
code that printed it · whole suite runs in under three minutes.*

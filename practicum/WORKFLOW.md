# The loop

Every chapter in this guide runs the same seven steps. Print this page. When
you are stuck on a real problem, the useful question is almost never "which
test do I use" — it is "which step am I on, and did I skip one?"

```
   1 QUESTION  ──▶  2 STORY  ──▶  3 MODEL  ──▶  4 PRIOR CHECK
                                                      │
        ┌─────────────────────────────────────────────┘
        ▼
   5 FIT  ──▶  6 CHECK  ──▶  7 DECIDE
        ▲          │
        └──────────┘   (the check sends you back more often than not)
```

### 1. Question — name the decision

Write down what you will *do* differently depending on the answer. "Is the new
checkout better?" is not a question; "should we ship it, given that rolling it
out costs two engineer-weeks?" is. If no action depends on the answer, you are
doing recreational statistics, which is fine, but say so — it changes how much
precision you need.

State the quantity you want in units someone else would recognise: euros per
month, minutes per commute, extra tickets per release. Not "significance".

### 2. Story — how were these numbers produced?

Describe the mechanism that generated your data, in words, then in code. Who
or what varies? What is measured with error? What was *selected* — which
observations never made it into the file?

The test of a story is that you can simulate from it. If you can write a
function that produces a fake dataset that looks like yours, you have a story.
If you cannot, you do not yet know what you are modelling.

### 3. Model — turn the story into a joint distribution

One line per unknown, one line for the data:

```
minutes_i ~ Normal(mu, sigma)        <- how the data arise, given the unknowns
mu        ~ Normal(30, 10)           <- what you knew before, per unknown
sigma     ~ HalfNormal(10)
```

That stack *is* the model: a joint distribution over everything, knowns and
unknowns together. Everything that follows is bookkeeping on it — conditioning
on what you saw, averaging over what you didn't.

### 4. Prior check — simulate before you look

Draw parameters from the priors, push them through the story, and look at the
fake data. Negative commute times? Rents of 40 million? Effects so large the
world would have noticed? Then your priors are not "uninformative", they are
wrong, and they will still be wrong after you see the data.

This step costs four lines and catches more errors than any other.

### 5. Fit — condition on the data

Grid for one or two unknowns, quadratic approximation for smooth unimodal
posteriors, MCMC for everything else. The output is always the same object: a
bag of parameter values that survived contact with your data, in proportion to
how well each explains it. Once you have the bag, every question is answered
by counting.

### 6. Check — does the fitted model reproduce your data?

Simulate new datasets *from the fitted model* and compare them with the real
one on features you actually care about: the spread, the maximum, the zeros,
the fraction above a threshold. A model that cannot reproduce a feature of
your data cannot be trusted to predict it.

A passed check is not proof the model is right — it only says the model is not
obviously self-contradictory. A failed check is decisive: fix the story
(step 2), not the priors.

### 7. Decide — turn the posterior into an action

Losses are asymmetric almost everywhere. Missing a fraud costs 40 times more
than checking a legitimate transaction; running out of stock costs more than
holding it. The action that minimises expected loss under the posterior is
rarely the one you get by plugging in the best estimate, and it is almost
never at "probability > 0.5".

Report three things: the action, the expected cost of being wrong, and what
would change the decision.

---

### The standing question: what would make this wrong?

The loop lives in the small world of your model, where the list of
possibilities is complete and the story is true. You deploy in the large
world, where it isn't. Before you present anything, ask:

- **Selection.** What is missing from this dataset, and why?
- **Measurement.** Is the thing I modelled the thing that was recorded?
- **Cause.** Would this number change if I *intervened*, or only if I *observed*?
- **Drift.** Is the process that made the training data still running?

No amount of correct conditioning saves you from a wrong answer to those four.

---

### What each skipped step costs you

| Skipped | Typical symptom |
|---|---|
| 1 Question | A beautiful posterior nobody can act on. |
| 2 Story | Variables in the regression that should never have been there. |
| 3 Model | "Uninformative" priors that quietly assert absurdities. |
| 4 Prior check | Divergent sampler, or a fit dominated by a prior you never inspected. |
| 5 Fit | A point estimate paraded as if it had no uncertainty. |
| 6 Check | Confident predictions from a model that cannot reproduce the data it was fit on. |
| 7 Decide | A p-value handed to someone who asked what to do on Monday. |

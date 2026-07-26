# Capstone: three questions from a real Tuesday

You have joined **Velo**, a bicycle-repair subscription business: members pay
monthly and get unlimited workshop visits. Twelve cities, one workshop each,
about thirty mechanics.

The COO sends you three questions and no guidance. Nobody will tell you which
chapter each one is from. That is the exercise.

```bash
cd practicum
python data/make_capstone.py       # writes the three CSVs
```

Everything you need is in `bayeskit.py` and the fourteen chapters. Nothing here
requires a technique the guide has not covered.

---

## Question 1 — "Should we roll the price rise out everywhere?"

*Data:* `data/capstone_signups.csv` — 288 city-months: `city`, `month`, `price`,
`marketing_spend`, `signups`.

Twelve months ago the company raised the monthly price in some cities. Head
office wants to know whether to do it everywhere. Signups fell in some cities
and rose in others.

**Deliver:** the price elasticity of signups, with an interval; a recommendation
about the rollout, in euros per month; and an explicit statement of the
assumption your answer depends on.

*Watch out for:* the cities where the price was raised were not chosen at
random. `marketing_spend` is the only thing in the file that carries information
about local demand, and it carries it badly.

*Sanity check before you start:* run the naive regression of `log(signups)` on
`log(price)`. If the coefficient is positive, you have reproduced the trap and
can begin.

---

## Question 2 — "How many mechanics on Saturday?"

*Data:* `data/capstone_jobs.csv` — 280 days at one workshop: `day`, `weekday`
(0 = Monday), `jobs`.

Each mechanic handles about six jobs a day. The COO wants Saturday staffed so
that the workshop is overwhelmed on at most one Saturday in ten, six months from
now.

**Deliver:** a number of mechanics, the probability of overflow it implies, and
evidence that your model can reproduce the kind of days this workshop actually
has.

*Watch out for:* the obvious model for counts is wrong here in a way that will
not show up in any convergence diagnostic, and the error is in exactly the
direction that makes you understaff.

---

## Question 3 — "Which mechanics need retraining?"

*Data:* `data/capstone_mechanics.csv` — 30 mechanics: `mechanic`, `jobs`,
`rework` (repairs that had to be redone).

Retraining costs €800 per mechanic and cuts a mechanic's rework rate by about
40%. Each rework job costs the company €95. A mechanic does roughly 300 jobs a
year.

**Deliver:** the list of mechanics to retrain, the expected saving, and the
probability that the worst mechanic on the raw table is genuinely among the
three worst.

*Watch out for:* the raw league table. Also: the decision rule is not "retrain
everyone above the average".

---

## What a finished answer looks like

For each question, one page. Not a notebook dump — a page someone can act on.

1. **The decision and its costs**, stated first, in the units of the business.
2. **The generative story**, in three or four sentences, and what you assumed
   away.
3. **The model**, as a stack of `~` lines.
4. **Evidence that the priors are not absurd** — one prior predictive plot or
   summary.
5. **The fit**, with R-hat and ESS if you sampled, or a note on why you didn't
   need to.
6. **At least one posterior predictive check** aimed at the feature the decision
   depends on — the tail for Q2, not the mean.
7. **The recommendation**, with the expected cost of being wrong and one
   sentence on what would change it.

## Grade yourself

The true generating process for all three datasets is recorded at the bottom of
`data/make_capstone.py`, under a spoilers banner. Do not read it until you have
written your three pages.

When you do, check these specifically — they are where the marks are:

- **Q1.** Did you get the sign right? Did you say what your adjustment assumes,
  and did you notice that the two available adjustments disagree?
- **Q2.** Did your predictive interval for a future Saturday cover the kind of
  day this workshop actually has, or only the average one?
- **Q3.** How far did your recommended list move away from the raw ranking, and
  did you report the probability that the ranking is real rather than the
  ranking itself?

## If you want a harder version

Every one of these has a natural extension the guide has prepared you for:

- **Q1:** the price rise happened at a specific month. What else changed then?
  Build the model with month effects as well as city effects and see whether the
  answer moves. What would you need in the file to be confident?
- **Q2:** the workshop's jobs are almost certainly correlated across days.
  Chapter 12's warning about LOO on time series applies. Does a
  leave-a-week-out comparison change which model you would use?
- **Q3:** compute the value of information. If you could shadow one mechanic for
  a week (50 more jobs observed), which one, and would it change the retraining
  list often enough to be worth the week?

---

*When you can do these three from a cold start, you can do the job. The
remaining thing to acquire is a library of stories — which is what
`curriculum/` and the source texts are for. See the reading map at the end of
[README.md](README.md).*

# Panel Critique — Pedagogy & Intuition-Building Lens

Auditing `OUTLINE-draft.md` against `BRIEF.md`. Lens: does each module have ONE memorable
spine, keep the learner active, sequence cognitive load, engineer genuine surprise, and
compress judgment (not just procedure) — at a length that fits 2,500–5,000 words?

Headline: the *content* is excellent and the surprises are mostly already chosen well. The
pedagogy gaps are structural: (1) predict-then-verify lives only in the exercises, not in the
demos where the surprises actually happen; (2) four modules are overloaded (03, 17, 22, 23);
(3) the four-line spine is defined once and then goes implicit for ~10 modules.

---

## 1. Prioritized findings

| Sev | Module(s) | Issue | Concrete fix |
|---|---|---|---|
| 1 | 03 | Three modules in a trenchcoat (Poisson-process story + CLT/Cauchy + max-ent + full exponential-family/cumulants/sufficiency/conjugacy), and the exp-family half re-derives C-B ch.3 the learner has *seen* — slow where it should be fast. | Keep 03 = generative stories + heavy-tail surprise + max-ent (all fresh). Relocate exponential-family/log-partition/cumulants/sufficiency/conjugacy to the **front of module 05**, where conjugacy is actually *used*. Lead 03 with what's new so it doesn't feel like re-lecturing C-B. |
| 1 | ALL | Predict-then-verify (brief item 3, non-negotiable) appears only in the exercise apparatus. The *demos* are written "simulate X, show Y" — show-then-tell. The naive wrong guess is never captured before the reveal, so the surprise doesn't land. | Put a **"Predict:"** line before every hero reveal in the prose, not just in exercises. Codify in STYLE.md format contract: each marquee demo = Setup → Predict (commit a number/direction) → Run → Reconcile. |
| 1 | 22 | Genuinely two modules (design: randomization/assurance/optional-stopping/factorial + causal: potential outcomes/backdoor). Neither gets depth. This is open-Q#1's real answer. | **Split** into 22 Design and 23 Causal, OR narrow 22 to the single spine "design gives you the likelihood you think you have (ignorability)" and demote factorial/D-optimal to exercises. Don't ship both halves shallow. |
| 2 | ALL | Four-line spine is stated in 00 then goes implicit through ~10 modules; it won't become automatic (statable a week later). | Add a standing one-sentence header to every module: **"Which line is this?"** placing the module on the four lines (e.g. 10-MH: "line 2 when the line-3 integral is intractable"). Cheap, high-frequency, makes the spine a reflex. |
| 2 | 08 | Structured as an audit-*checklist* — Fisher, CR bound, BvM, Stein, two bootstraps, complete-class each stamped "Bayesian-approved." Reads as a treaty negotiation, not an emotional reframe. | Restructure around **Stein-as-hero**: open with the learner being *wrong* ("MLE is obviously optimal for a Gaussian mean") → JS dominates it everywhere for d≥3 → JS *is* empirical-Bayes shrinkage. Then BvM as the reconciliation. Demote CR bound + complete-class to bridge boxes. Feeling to leave: "their crown jewel is our shrinkage." |
| 2 | 17 | Three sub-themes (checking / comparison / testing): PPC, LOO/WAIC, Bayes factors, Lindley, p-calibration, prior-sensitivity. Overloaded; spine muddled. | Make **PPC the spine** ("a model must be able to predict its own data"). Lighten BF/Lindley and revisit them in 24. Keep 17 before 18 (open-Q#5). |
| 2 | 23 | A passive survey firehose: 8 topics (weight decay, label smoothing, ensembles, VAE, diffusion, LLM, ICL, temperature). Highest risk of "cover, not build." | Anchor on **2 hands-on labs** (ensemble calibration; ICL toy) + the theorem/heuristic/open 3-column ledger as the deliverable. Label the rest explicitly "map, not territory." Set expectation: lens-fitting module, not a build module. |
| 2 | 00 | The orientation reframe is a reframe, not a *surprise* — no hook to make the learner feel the payoff. | End the biased-coin micro-demo with a **plug-in bet that loses money** where the posterior-predictive bet doesn't. Seeds 05/09/21 and gives the course a visceral opening. Convert the 15-procedure table to predict-then-reveal ("which line?"). |
| 2 | 05 | Five fully-worked conjugate pairs + predictive each + A/B → length blowout risk. | Full-derive **two** (Beta-Binomial, Normal-Normal); present the other three as "same move, new algebra" in a compressed table with one predictive twist each. The *repetition of the pattern* is the pedagogy; five full derivations is padding. |
| 2 | 02 | Four full worked examples (medical test, tank, Monty Hall, naive-Bayes spam) — overloaded. | Keep medical-test (base-rate surprise) + tank (estimator surprise) full. Demote **Monty Hall to an exercise** (overexposed, party-trick feel) and naive-Bayes-spam to a forward preview. |
| 3 | 06 | Two-point uniform CI pathology (open-Q#4) is clever but hard to *feel* — the learner must decode U(θ−½,θ+½) and the |X₁−X₂| condition. | **Keep it** (it's the strongest confidence≠credible gut-punch: an interval labeled 50% you *know* is correct) but render it as a **picture** annotated "this specific interval is certainly right." Welch/Jaynes are more obscure, not clearer. Also lead 06 with the loss→estimator derivations (concrete) before the CI philosophy. |
| 3 | 07 | Machinery-first; the ML learner is skeptical priors matter at all. | Lead with the **sensitivity fan** (n=10 vs n=10,000) to answer "does it even matter?" *first*, then teach Jeffreys/weakly-informative/improper. |
| 3 | 24 | Closing ML-zoo table is presented (passive) rather than retrieved. | Make it a **self-test**: blank the "Bayesian reading" column, learner fills before revealing. Retrieval practice = durable consolidation. |
| 3 | 20 | Deliberately "nothing new" → no violate-expectation surprise beyond particle degeneracy. | Acceptable — **lean into it**: make "you already know this" the explicit reveal (spine payoff), let particle-filter weight degeneracy carry the one surprise. |
| 3 | 01–02 (prereq) | Open-Q#2: counting/combinatorics (C-B ch.1–2). Re-teaching it to this learner is the boredom trap. | **Trust as prerequisite.** Fold needed counting into module 02's enumeration engine (counting in service of a joint). Ship a 1-page predict-and-check prerequisite self-diagnostic. Don't spend module 01 real estate. |

---

## 2. Per-module verdict (spine + single best improvement)

- **00 Four-Line Course** — Spine: *the whole subject is four lines; any named procedure is a special case / approximation / audit of them.* → Improve: end the coin demo with a plug-in-bet-loses-money hook; make the 15-procedure table predict-then-reveal.
- **01 Probability as Logic** — Spine: *exchangeability, not philosophy, is what makes a parameter exist — empirical frequency converges to a RANDOM limit = θ.* (Strong, fresh.) → Improve: compress Dutch-book/Cox to a tight box so the de Finetti simulation carries the whole load.
- **02 Conditioning Is Inference** — Spine: *Bayes = ratio of joints; posterior odds = prior odds × likelihood ratio.* → Improve: cut to two full examples (test + tank); Monty Hall → exercise.
- **03 Distributions Are Stories** — Spine (intended): *every distribution is a generative story; match stories to pick families.* → Improve (sev-1): split — relocate the exponential-family machinery to 05; lead with the new material (stories + Cauchy surprise).
- **04 Likelihood: the Data's Voice** — Spine: *identical data → identical likelihood → identical posterior, but different p-values; evidence is the likelihood, not the intention.* (Emotional core of the thesis.) → Improve: capture the "same data → same answer" naive guess *before* the reveal.
- **05 Conjugate Updating** — Spine: *every posterior = prior pseudo-data + real data; posterior mean = precision-weighted average (the master shrinkage formula).* → Improve: full-derive two pairs, compress three; open with the 2-in-2 overconfident-MLE surprise.
- **06 Estimates & Intervals Are Decisions** — Spine: *estimates and intervals are derived from a loss; a confidence interval is not a credible interval.* → Improve: render the two-point CI as an annotated picture; lead with loss→estimator.
- **07 Priors** — Spine: *a prior is part of the model (same status as the likelihood); it sometimes matters, sometimes washes out — but unidentified parameters never do.* → Improve: lead with the sensitivity fan to answer the skeptic first.
- **08 The Frequentist Bridge** — Spine (intended): *frequentist evaluation is an audit Bayesians should pass; admissible = Bayes is a theorem.* → Improve (sev-2): restructure around Stein-as-hero + BvM-as-reconciliation so it stops reading as a treaty.
- **09 Monte Carlo Fundamentals** — Spine: *replace any integral with a sample average + honest CLT error bar; importance sampling fails silently.* → Improve: make the ESS collapse a predict-first ("guess the effective sample size").
- **10 Metropolis–Hastings** — Spine: *a 30-line sampler that provably targets the posterior (detailed balance) + the diagnostics to trust it — necessary, not sufficient.* → Improve: hold MCMT to one figure (open-Q#6); make bimodal-fail-to-mix a predict-first.
- **11 Gibbs & Data Augmentation** — Spine: *sample one full conditional at a time; it crawls as posterior correlation rises; augmentation invents latent data to restore conjugacy.* → Improve: foreground the module-05 exact-agreement audit; make ρ=0.99 ESS-collapse the motivation for HMC.
- **12 HMC & NUTS** — Spine: *random walks die in high-D because the mass is a thin shell (typical set); gradients + momentum give coherent long moves.* (Marquee.) → Improve: stage the donut as an explicit prediction; watch d=1000 runtime.
- **13 Laplace / EM / VI** — Spine: *approximate the posterior with a computable shape; know each failure mode — mean-field VI gets the mean right, the variance too small.* → Improve: organize strictly around the ELBO (three derivations) so three methods feel like one idea; foreground EM = VI-with-point-mass-q.
- **14 Regression I (Bayesian linear)** — Spine: *regression is a prior over lines; predictive intervals flare off-support; ridge/lasso ARE priors (λ↔τ² exactly).* → Improve: make the trumpet flare a predict-first ("sketch the interval far from data").
- **15 Regression II (GLMs)** — Spine: *pick a response story → link = a GLM; cross-entropy IS categorical-GLM MLE; any proper prior cures separation.* → Improve: Poisson regression → exercise; make separable-MLE→∞ a predict-first.
- **16 Hierarchical Models** — Spine: *share strength across groups; partial pooling = precision-weighted blend of group and population — and it beats BOTH extremes out-of-sample.* (Crown jewel; ties 05/08/12 together.) → Improve: make the held-out pooling bake-off a predict-first.
- **17 Model Checking & Comparison** — Spine (muddled): *a model must predict its own data (PPC); evidence has a built-in Occam factor; every comparison tool has a failure mode.* → Improve (sev-2): PPC is the spine; lighten BF/Lindley (revisit in 24); keep before 18.
- **18 Latent Structure (mixtures/DP)** — Spine: *cluster labels are just more unknowns — marginalize them; a DP lets the data choose K.* → Improve: center the emotional beat on EM-hides-label-uncertainty vs Gibbs-reveals-it (predict-first: "how sure are we of the labels?").
- **19 Gaussian Processes** — Spine: *a GP is a prior over functions = basis regression at the infinite limit; kernel = covariance.* → Improve: lead with the two-routes-identical-predictions check; kernel gallery as visual intuition.
- **20 State Space / Kalman** — Spine: *the Kalman filter is 05's Normal-Normal on a conveyor belt: predict = marginalize, update = condition — the four lines, literally.* → Improve: make "nothing new" the explicit reveal; let particle degeneracy carry the surprise.
- **21 Decisions & Bandits** — Spine: *turn a posterior into an action by minimizing expected loss; Thompson sampling = sample the posterior and act greedily (and it's near-optimal).* → Improve: make "is 0.5 the right threshold?" and "which strategy wins?" predict-first.
- **22 Design & Causal** — Spine (intended, but two modules): *design gives you the likelihood you think you have (ignorability); causal inference = inference over missing potential outcomes.* → Improve (sev-1): split, or narrow to the ignorability spine.
- **23 Bayesian Lenses on DL/GenAI** — Spine (survey): *modern ML moves are approximate-Bayesian, sorted into theorem / heuristic / open.* → Improve (sev-2): anchor on 2 labs + the ledger; label the rest "map, not territory."
- **24 One Theory, Two Audits** — Spine: *what's settled, what auditing adds, how practitioners blend — every claim links to a module you ran.* → Improve: make the ML-zoo table a fill-in-first self-test (retrieval).

---

## 3. Five signature experiences (remembered years later)

Each = a staged prediction the naive learner gets **wrong**, then a reveal that reorganizes intuition.

1. **The Donut / typical set (module 12).**
   *Setup:* "Where is most of the probability mass of a 1000-dimensional standard Gaussian?"
   *Predicted-wrong:* "At the mode (the origin) — that's where the density is highest."
   *Reveal:* Simulate ‖x‖ for x∼N(0,I₁₀₀₀); the norms concentrate in a thin shell at √1000 ≈ 31.6. The mode holds essentially none of the mass. This single fact explains why random-walk MCMC and plug-in-at-the-mode both fail in high-D — and motivates all of HMC.

2. **The overconfident MLE (module 05).**
   *Setup:* A user converts on 2 of 2 impressions.
   *Predicted-wrong:* "P(next converts) ≈ 1.0 — the data says 100%."
   *Reveal:* Beta(1,1) prior → Beta(3,1) posterior; posterior-predictive P(next) = 3/4 = 0.75. Certainty from two data points was an artifact of plugging in a point. The prior acted as one pseudo-success + one pseudo-failure — the spine in three integers. Recurs as Laplace's rule of succession, add-α smoothing, and the regression trumpet.

3. **Same data, opposite verdicts (module 04).**
   *Setup:* Two labs each observe 9 successes in 12 trials; one planned n=12, the other planned to stop at the 3rd failure.
   *Predicted-wrong:* "Same data → same conclusion."
   *Reveal:* p-values 0.073 vs 0.033 (one "not significant," one "significant") while the likelihood and posterior are *identical*. The evidence never changed — only the experimenter's unrealized intention did. The emotional core of "it's all bookkeeping."

4. **Stein's paradox (module 08).**
   *Setup:* Estimate three *unrelated* quantities — a batting average, a wheat yield, a car's MPG — each from its own sample mean.
   *Predicted-wrong:* "Each mean is optimal; unrelated quantities can't borrow from each other."
   *Reveal:* James–Stein shrinkage dominates the per-coordinate MLE in total MSE for d≥3, even for unrelated quantities — and JS is *just empirical-Bayes shrinkage*. The frequentist crown jewel is a Bayesian move; the "special case" framing is a theorem, not propaganda.

5. **Occam's razor falls out for free (module 17).**
   *Setup:* Fit polynomials of degree 1…9 to data generated from degree 3.
   *Predicted-wrong:* "Training error only falls with degree, so you *need* a hand-added penalty or cross-validation to find the right complexity."
   *Reveal:* The marginal likelihood (evidence) *peaks at degree 3* and falls after, while train MSE keeps dropping. Complexity control is automatic — the Occam factor — with no CV and no tuned penalty. Integration, not regularization-by-hand.

*Alternates if a sixth is wanted:* Thompson sampling near-optimality (21); partial pooling beats both extremes out-of-sample (16 — but it reprises #4's shrinkage, so don't double-count it as a *distinct* signature).

---

## 4. Recommended exercise template + worked sample (module 05)

**Template — every exercise forces a committed prediction BEFORE any code:**

1. **Setup** — 2–4 sentences, concrete, real numbers, minimal.
2. **Predict** — a specific numeric or directional question the learner answers *before running anything*; choose scenarios where the naive answer is wrong. "Write down your guess. Bigger or smaller? By how much?"
3. **Reason (one line)** — name the intuition you're using, so when it breaks you know *which* intuition to repair.
4. **Run** — the exact code to execute; it prints the settling number.
5. **Reconcile** (`<details>`) — the answer, *why the naive guess missed*, and the general lesson (the compression). Never just "the answer is 0.75."

**Worked sample — Module 05, "The overconfident MLE":**

> **Setup.** A new ad shows twice and converts both times: 2 conversions in 2 impressions. Put a Beta(1,1) (uniform) prior on the conversion rate θ.
>
> **Predict.** The MLE is θ̂ = 2/2 = 1.0. Write down two numbers before coding: (a) the posterior *mean* of θ; (b) the posterior-*predictive* probability that the next impression converts. Most guts say ≈1.0 for (b). Commit to both.
>
> **Reason.** If you wrote ≈1.0, you're trusting the point estimate — "the data said 100%."
>
> **Run.**
> ```python
> from scipy.stats import beta
> a0, b0, s, f = 1, 1, 2, 0
> a, b = a0 + s, b0 + f            # Beta(3, 1) posterior
> post_mean = a / (a + b)          # 0.75
> pred_next = a / (a + b)          # Bernoulli posterior predictive = posterior mean
> print(round(post_mean, 4), round(pred_next, 4))   # -> 0.75 0.75
> ```
>
> <details><summary>Reconcile</summary>
>
> - Posterior is **Beta(3, 1)**: mean = 3/4 = **0.75**, not 1.0.
> - Posterior-predictive P(next converts) = E[θ] = **0.75**. The MLE's "1.0" claimed *certainty from two data points* — an artifact of plugging in a point estimate and discarding parameter uncertainty.
> - Read the update as counts: posterior = Beta(1+2, 1+0) → **3 effective successes, 1 effective failure** → 3/4. That is the module spine — *prior pseudo-data + real data* — in three integers.
> - **Compression (the years-of-experience takeaway):** plug-in prediction is *most* overconfident exactly when you have *least* data. The posterior predictive is the honest number: always pulled toward the prior, always wider than the plug-in. You will meet this same correction again as Laplace's rule of succession, as add-α smoothing in a language model (this module's Dirichlet-Multinomial), and as the flaring predictive interval in regression (module 14).
>
> </details>

*(Follow-on predict-first exercises for 05: sequential = batch — predict whether updating one datum at a time vs all at once changes the posterior, then verify identity; and predictive-wider-than-plug-in — predict the coverage of a plug-in 90% interval, then simulate it undershooting.)*

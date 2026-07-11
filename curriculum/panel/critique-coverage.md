# Panel Critique — Coverage, Fit, and Structure

Reviewer lens: coverage / fit-to-learner / structural soundness. Audited `OUTLINE-draft.md` against `BRIEF.md`, the booklet chapter list, C-B TOC, and confirmed contents of ISLP / Montgomery PDFs.

**Source-availability facts that drive the dispositions below (verified, not assumed):**
- ISLP PDF *does* contain Survival Analysis (ch11) and Multiple Testing + False Discovery Rate (ch13). So survival and FDR each have a local, citable source — omission would be a choice, not a necessity.
- Montgomery PDF contains factorial / fractional-factorial / RSM / blocking / random-effects — enough to source a full design module.
- Booklet has DP + stick-breaking (ch14) and INLA (ch12) but **no** GP, Kalman, VI, EM, survival, FDR, ABC, SMC, misspecification, or label-switching. The draft correctly cites all of these "by concept" — authors must *synthesize* them, not "absorb and supersede" a booklet section that doesn't exist. Flag for authors.
- Booklet is R-heavy (Gibbs/MH in R); brief says **no R anywhere**. The draft's code is Python-only (good) but authors reading source risk leaking R idioms. INLA (booklet ch12) is R-INLA — the draft rightly omits it; keep it omitted.
- `STYLE.md` is referenced by the outline header ("Format contract per module lives in STYLE.md") but does not exist in `curriculum/`. Orchestrator owes authors this file.

Overall verdict up front: the spine is sound, the anti-tribal framing is genuine (not polemical), and ML is **not** ghettoized to module 23. The defects are (1) a load-bearing dependency with no teaching home, (2) two modules that must split, (3) an entirely M-closed worldview that the brief's "compression of experience" bar forbids, and (4) several cheap missing topics that drop out of machinery already present.

---

## 1. Prioritized findings

| Sev | Area / module | Issue | Concrete fix |
|---|---|---|---|
| 1 | 05 → 14,19,20,21 (dependency) | Multivariate-normal conditioning/marginal identities are load-bearing from BLR (14) through GP (19), Kalman (20), decisions (21) but have **no teaching home**. Learner has linear algebra, not the MVN conditioning cheat-sheet. | Add a ~1-page "Gaussian conditioning toolkit" section to 05 (derive the conditional-mean/cov block formulas once, numerically verified); callback from 14/19/20. |
| 1 | 22 (structure + scope + brief) | Design **and** causal in one module both over-budget AND demotes experimental-design, which the brief names co-equal first-class. Cramming Montgomery factorial/RSM + assurance + adaptive + PO + backdoor into ~4k words is infeasible. | **Split**: `Design (Bayesian)` and `Causal Inference (PO + DAGs)`. Answers open-Q1: yes, 22 is too broad. |
| 1 | 17 (scope) | Over-budget as drafted (PPC+LOO/WAIC+BF+Lindley+BF-sensitivity+PSIS+p-cal); required missing topics (FDR, misspecification, EB-at-scale) would blow it apart. | **Split** into `17a Model checking & comparison` (M-closed) and `17b Multiplicity, misspecification & large-scale inference` (M-open + FDR + EB-scale). |
| 1 | Missing: model misspecification / M-open | Draft is entirely **M-closed** (compare models assuming one is true). No sandwich SE, no power/tempered posteriors, no "Bayesian posterior is overconfident under misspecification," no bagging-as-robustness. This is exactly the years-of-judgment content the brief demands. | Dedicate a section in new 17b: sandwich as the frequentist misspecification audit; why the posterior is too narrow off-model; power posteriors / generalized Bayes; bagging as stability. Callback to 08 and 13 (VI underdispersion — same overconfidence theme). |
| 1 | Missing: causal DAGs | Causal is potential-outcomes-**only**. Learner's ML background expects DAGs/backdoor/d-separation; PO-only cannot read half the causal-ML literature. | DAG section in the new causal module: d-separation, backdoor/frontdoor, confounding-as-graph, PO↔DAG correspondence. do-calculus (3 rules) = named pointer, not derived. |
| 2 | 03,04,09,10,11 (brief: ML integration) | Cross-cutting mandate is "≥1 ML bridge box per module," but these foundational modules' drafted examples don't instantiate one — the dry spots that make ML look deferred. (ML *is* well-integrated in 00,02,05–08,12,13,14–16,19,23 — it is **not** ghettoized to 23.) | Name the bridges explicitly: 03 exp-family→softmax/cross-entropy & sufficiency→"minimal statistic = bottleneck"; 04 likelihood→loss, MLE→ERM; 09 MC→MC-dropout, IS→off-policy weighting; 10 MH→simulated annealing; 11 data-augmentation→EM/VAE latents. |
| 2 | 03 / 13 / 17 (connective tissue) | Entropy/KL/cross-entropy are used in 13 (ELBO=logZ−KL), 15 (cross-entropy=NLL), 17 (WAIC) but never defined centrally — "information theory as connective tissue" is assumed, not taught. | Define entropy/KL/cross-entropy **once** in 03 (max-ent already lives there); thread the vocabulary. MDL = one-line mention in 17a (codelength = −log evidence, Occam). |
| 2 | Missing: missing-data / MI | Absent, though the exact machinery is already in the draft (data augmentation = imputation; ignorability in 22). | Section in 11: missing data = latent variables; MI = repeated posterior draws of the missing entries; MCAR/MAR/MNAR = ignorability. Callback from causal module (PO = missing data). |
| 2 | Missing: survival / censoring | Absent; it is the *cleanest* demonstration of "inference = conditioning on exactly what you saw (an interval, not a point)," and ISLP ch11 is available. | Section in 15 (exponential/Weibull survival as a GLM with censored likelihood); seed the censored-likelihood idea as one example in 04. |
| 2 | Missing: multiplicity/FDR + EB-at-scale | Both absent; ISLP ch13 + Efron available; Bayesian reading (hierarchical shrinkage does multiplicity adjustment automatically) is squarely on-thesis. | Two sections in new 17b: BH/FDR + Bayesian-FDR = posterior expected false-discovery proportion; Efron large-scale EB / local-FDR. Cross-ref 16 (shrinkage). |
| 2 | 08 (scope) | Over-budget: MLE-asymptotics + Fisher + Cramér–Rao + BvM + Stein + JS-as-EB + bootstrap + Bayesian-bootstrap + complete-class + admissibility, each "derive+simulate." | Trim (don't split): Cramér–Rao → stated + one numerical check; keep one bootstrap not two; admissibility/complete-class = stated in words; JS derivation stays, 16 only callbacks it (avoid re-derive). |
| 2 | 12,16,18,19,23 (scope) | Each near/over the 2.5–5k-word + 4–10-block budget as specced. | 12: drop the banana **or** energy-boundary demo. 16: one applied dataset (radon *or* batting, not both). 18: ZIP → exercise; show stick-breaking as the single DP construction at depth. 19: NNGP & BayesOpt → one-figure teasers. 23: conformal → move to capstone; diffusion/ICL stay "conceptual figure + cite." |
| 2 | 13 vs 18 (redundancy) | GMM-EM appears in both (13 derives EM on a GMM; 18 does EM-vs-Gibbs on a 2-D GMM). | Full GMM-EM lives in the mixtures module (18/new-19); 13 derives the ELBO reduction on a minimal latent example (2-comp 1-D or missing-data EM). |
| 2 | Missing: time series beyond Kalman | Only Kalman + particle filter; no AR. | AR(p) section in the state-space module: Bayesian AR = conjugate regression-on-lags (reuses 14). GARCH-lite already gestured at via the "stochastic-volatility-lite" PF example — keep as the nonlinear case; one-line volatility-clustering mention. |
| 2 | 16,21,22 (feasibility) | Nested-simulation risk >180s: 16 pooling-spectrum held-out **risk sweep**, 22 optional-stopping **calibration lab**, 21 **bandit tournament** × replications. | Put conjugate/Gibbs (not PyMC/NUTS) *inside* the loops; vectorize the bandit pulls (Beta-Bernoulli is closed-form); cap replications and state the seed/runtime. |
| 3 | 07, 14 (tone) | "regularization is a prior you refuse to name" (appears twice) reads mildly polemical/cute — the one spot that drifts from the brief's no-straw-men tone. | Soften to "regularization is an *implicit* prior." |
| 3 | 06 → 07 (order) | 06 derives ridge/lasso = Gaussian/Laplace-prior MAP before the priors module (07) formalizes priors. | Acceptable (00/05 introduce priors operationally); add a one-line forward-pointer to 07. Not worth a reorder. |
| 3 | 06 | Quantile regression missing but drops out of 06's loss→estimator machinery for free. | Mention: pinball/asymmetric loss → any quantile (median = the 0.5 case already there); asymmetric-Laplace likelihood as the "Bayesian" version. |
| 3 | 15 | Ordinal regression absent. | One-paragraph mention: cumulative-link (ordered logit/probit) as a GLM with cutpoints; optional exercise. |
| 3 | 09 / 23 | ABC / simulation-based inference absent. | Append a ~20-line rejection-ABC demo to 09 (ABC = rejection in summary-stat space; rejection already taught there); neural-SBI = one-line frontier pointer in 23. |
| 3 | 20 / 17b | SMC beyond the PF cameo absent. | Pointer only: PF → SMC-samplers for static posteriors via tempering (state-space module); tempering ↔ power posteriors (17b). No module. |
| 3 | 03 | Extreme-value theory absent (heavy tails themselves are well-threaded: 03 Cauchy, 09 IS-failure, 14 t-robust). | One-line mention in 03: "there is a limit theorem for maxima too" (GEV/Fréchet–Gumbel–Weibull); full EVT/POT = omit (domain specialization). |
| 3 | 12 / 24 | PPL landscape (Stan/PyMC/NumPyro) never oriented. | One bridge box in 12: PyMC primary, NumPyro = "when you need JAX speed" pointer, Stan = the booklet's HMC/Stan insert (read-only, no Stan code). Reading-map entry in capstone. Answers open-Q7. |
| 3 | 07 / 18 / 23 | Nonidentifiability treated in 3 places (07 washout, 12 funnel, 18 label-switching) but never unified; 18's label-switching alone is otherwise adequate. | Add a "faces of nonidentifiability" note in 07 (symmetry / weak-likelihood / structural) + a 23 callback (overparameterized nets are massively nonidentified). |
| 3 | 24 (scope/count) | "no new code" synthesis ledger is a full numbered module. | Demote to a lighter **capstone** (offsets one of the two splits); house the ML-zoo table (add BART, conformal rows) + reading map here. |
| 3 | apparatus | `STYLE.md` referenced but missing; booklet's R source is a leak risk. | Orchestrator writes STYLE.md; author checklist item: no R idioms, no R-INLA. |

---

## 2. Missing-topics disposition

| Topic | Verdict | Where | Why (one line) |
|---|---|---|---|
| Multiple testing & FDR | Section | new 17b | BH + Bayesian-FDR = posterior false-discovery fraction; shrinkage adjusts multiplicity automatically — on-thesis; ISLP ch13 available. |
| Permutation tests | Mention | Design module (randomization inference) + 01 callback | The permutation null *is* exchangeability; one paragraph + 10-line demo, not a section. |
| Survival / censoring | Section | 15 (survival-as-GLM) + seed in 04 | Cleanest "condition on partial observation (an interval)" demo; ISLP ch11 available. |
| Missing data & MI | Section | 11 (augmentation = imputation) | Machinery already present; MI = posterior draws of missing; MAR/ignorability reused by causal module. |
| Model misspecification / M-open | Section (Sev-1) | new 17b | Sandwich / power-posteriors / bagging-as-robustness; the honest counterweight the brief's judgment bar demands. |
| ABC / SBI | Mention→demo | 09 (rejection-ABC) + 23 pointer | ABC = rejection in summary-stat space; ~20 lines given rejection is already taught; neural-SBI = frontier pointer. |
| SMC beyond particle filter | Mention | 20 + 17b | PF→SMC-samplers via tempering; tempering↔power-posteriors. Full SMC theory is graduate-specialist. |
| Ordinal regression | Mention | 15 | Cumulative-link GLM — a one-example extension of the "response story → link" recipe. |
| Robust regression | **Already covered** | 14 (Student-t likelihood) | Keep as-is; good. |
| Quantile regression | Mention | 06 | Pinball loss → any quantile, straight out of the loss→estimator machinery already in 06. |
| BART | Mention | capstone ML-zoo table + 19 pointer | Bayesian sibling of RF/boosting; too heavy to implement, tangential to spine. |
| Causal DAGs / do-calculus | Section (Sev-1) | new causal module | DAGs/backdoor/d-separation at working depth; do-calculus = named pointer. PO-only is insufficient. |
| Time series (AR, GARCH-lite) | Section + mention | state-space module | AR(p) = conjugate regression-on-lags; GARCH-lite = SV example already there. |
| PPL landscape (Stan/PyMC/NumPyro) | Mention | 12 bridge + capstone reading-map | Orient once; PyMC primary. A survey module would be filler. |
| Empirical Bayes at scale (Efron) | Section | new 17b (with FDR) | The bridge between hierarchical (16) and multiplicity; single most practically important missing topic. |
| Information theory (KL/entropy/MDL) | Section (define once) | 03 (with max-ent); MDL mention 17a | Load-bearing connective tissue for 13/15/17; define once, thread. |
| Nonidentifiability / label switching | Mostly adequate + unify | 07 note + keep 18 | 18's label-switching is enough; add a "faces of nonidentifiability" note + DL callback. |
| Heavy tails | **Already threaded** | 03, 09, 14 | Keep. |
| Extreme values (EVT) | Mention→Omit | 03 one-liner | "Limit theorem for maxima too"; full EVT is a domain specialization — omit. |

---

## 3. Answers to the 7 open questions

**Q1 — Module count (25) vs depth; merge 09+10? 20+21? Is 22 too broad?**
Do **not** merge 09+10 (iid Monte Carlo vs Markov-chain machinery — merging blurs the single most important computational distinction and makes a 6k-word module). Do **not** merge 20+21 (sequential *inference* vs sequential *decisions* — thematically distinct). **Yes, 22 is too broad** — split into design + causal. Net: reject the proposed merges, make two justified splits (17, 22). Depth is the brief's stated priority; don't merge to hit a round number.

**Q2 — Counting/combinatorics (C-B ch1–2): module 01 or prerequisite?**
**Prerequisite.** This learner has CS discrete math + undergrad probability; counting-for-its-own-sake is not curriculum-worthy. Module 02 already exercises finite-sample-space enumeration (Monty Hall, medical test) — all the discrete probability the spine needs, taught in context. At most a half-page "assumed facts" pointer in 00.

**Q3 — Nonparametrics beyond DP+GP (BART? quantile regression?): module or mention?**
**Mention, not a module.** DP (18) + GP (19) already cover the two canonical Bayesian-nonparametric priors (over partitions, over functions). Quantile regression = mention in 06 (pinball loss). BART = mention in the capstone ML-zoo table (Bayesian sibling of RF/boosting) + a pointer in the GP module. Neither earns 4k words.

**Q4 — Best conditional-coverage pathology for 06?**
**Keep the two-point uniform U(θ−½,θ+½) as primary** — cleanest ancillary (the range |X₁−X₂| tells you whether the interval is certainly-right or ambiguous), best for a 10-line simulation. **Add Jaynes' truncated-exponential as a short second example/exercise** — it is rhetorically stronger (the confidence interval can sit entirely below every data point / contain impossible values) and ties to the likelihood-conditioning theme. **Drop Welch** (too technical for the payoff).

**Q5 — Model checking (17) before latent structure (18), or after GPs (19)?**
**Keep it early (before 18).** Model checking is a general competency; introduce it the moment the learner has models to check (regression 14/15 + hierarchical 16), then have 18 (mixtures) and 19 (GP) each *end* with a "now check it with 17a's tools" callback. Deferring past 19 would leave 18's cluster-count and 19's kernel-selection without the checking vocabulary they need. (After the 17-split, "17a checking" sits before mixtures — consistent.)

**Q6 — How much MCMT theory (mixing times, spectral gaps) in module 10?**
**Minimal — one computed example + intuition, exactly as drafted.** Full rigor for detailed-balance ⇒ stationarity (it *is* the correctness proof of MH — earns its keep). Mixing time / spectral gap: one small transition matrix where you literally compute the second eigenvalue and watch autocorrelation/ESS track it — the payoff is spectral-gap → ESS (which the learner *uses* via diagnostics). No coupling, conductance, or mixing-bound proofs; cite MCMT "by concept." The learner's algorithms background makes "spectral gap = mixing runtime" land in one paragraph.

**Q7 — PyMC vs NumPyro as the "in practice" library?**
**PyMC primary** (installed per brief, most readable, ArviZ is the shared diagnostics layer). **NumPyro = mention-only** pointer ("when you need JAX/GPU speed"); do **not** dual-implement — that doubles the API-drift verification burden the brief explicitly warns about (pymc 6.1 / arviz 1.2 are new majors; verify idioms by running). Stan appears **only** via the booklet's read-only HMC/Stan insert (no Stan code — not Python). Put the one-time PPL orientation in module 12.

---

## 4. Proposed final module sequence

Legend: **[SPLIT]** **[NEW]** **[TRIM]** **[+sec]** = add section **[+men]** = add mention **[REORDER]** **[DEMOTE]**. Net: 25 → 27 numbered items via two justified splits; module 26 is a sub-budget capstone. Everything else is trim/section, not new modules.

**Part 0 — Orientation**
- **00** The Four-Line Course — unchanged (thesis + notation anchor; keep short).

**Part I — Foundations re-grounded**
- **01** Probability as the Logic of Uncertainty — **[+men]** permutation-null = exchangeability (used later by design module).
- **02** Conditioning Is Inference — unchanged (this *is* the "discrete probability" home; Q2).
- **03** Distributions Are Generative Stories — **[+sec]** define entropy/KL/cross-entropy once (with max-ent); **[+men]** exp-family→softmax/cross-entropy ML bridge; **[+men]** EVT one-liner.
- **04** Likelihood: the Data's Voice — **[+sec]** censored-likelihood example (survival seed); **[+men]** likelihood→loss / MLE→ERM ML bridge.

**Part II — Exact Bayesian inference**
- **05** Conjugate Updating End-to-End — **[+sec]** Gaussian-conditioning toolkit (fixes the Sev-1 dependency).
- **06** Estimates and Intervals Are Decisions — **[+men]** pinball→quantile; keep two-point-uniform CI, **[+sec]** add Jaynes exercise (Q4).
- **07** Priors: What They Are and Aren't — **[+men]** "faces of nonidentifiability"; soften "prior you refuse to name" (tone).
- **08** The Frequentist Bridge — **[TRIM]** CR→stated+1 check; one bootstrap; JS stays, admissibility stated-in-words.

**Part III — Computation**
- **09** Monte Carlo Fundamentals — **[+men]** rejection-ABC demo; MC→MC-dropout bridge.
- **10** Metropolis–Hastings from Scratch — MCMT minimal (Q6); **[+men]** MH→simulated-annealing bridge.
- **11** Gibbs Sampling & Data Augmentation — **[+sec]** missing data & multiple imputation (augmentation = imputation; MAR/ignorability); augmentation→VAE/EM bridge.
- **12** HMC and NUTS — **[TRIM]** drop banana *or* energy-boundary; **[+men]** PPL-landscape bridge (Q7).
- **13** Deterministic Approximations (Laplace, EM, VI) — **[TRIM]** EM on a minimal latent example (full GMM moves to 19); keep Laplace/CAVI/ADVI-vs-NUTS.

**Part IV — Statistical learning, re-founded**
- **14** Regression I: Bayesian Linear Models — MVN-conditioning callback to 05.
- **15** Regression II: GLMs & Classification — **[+sec]** survival-as-GLM (censored likelihood); **[+men]** ordinal (cumulative-link).
- **16** Hierarchical Models — **[TRIM]** one applied dataset; JS callback (no re-derive); conjugate/Gibbs inside the risk-sweep (feasibility).
- **17a** Model Checking & Comparison **[SPLIT]** — PPC, LOO/WAIC, evidence/Occam, Lindley, Bayes factors; **[+men]** MDL.
- **18** Multiplicity, Misspecification & Large-Scale Inference **[NEW / SPLIT from 17]** — BH & Bayesian-FDR (=shrinkage), Efron EB-at-scale/local-FDR, **M-open**: sandwich, power/tempered posteriors, bagging-as-robustness; tempering↔SMC pointer.
- **19** Latent Structure: Mixtures & the Dirichlet Process **[REORDER, was 18]** — full GMM-EM here (dedup); label-switching + nonidentifiability callback; **[TRIM]** ZIP→exercise.
- **20** Gaussian Processes **[REORDER, was 19]** — **[TRIM]** NNGP & BayesOpt → teasers; **[+men]** BART as "another prior over functions."

**Part V — Sequential data and decisions**
- **21** State Space & Filtering **[REORDER, was 20]** — **[+sec]** AR(p) = conjugate regression-on-lags; **[+men]** SMC-samplers via tempering; SV/GARCH-lite as the nonlinear PF case.
- **22** Decisions and Bandits **[REORDER, was 21]** — vectorize the bandit tournament (feasibility).
- **23** Experimental Design (Bayesian) **[SPLIT from 22]** — randomization, assurance = ∫power×prior, factorial-as-hierarchical-regression (Montgomery 2³), adaptive/optional-stopping calibration (conjugate inside the loop — feasibility); **[+men]** permutation/randomization inference.
- **24** Causal Inference **[NEW / SPLIT from 22]** — potential outcomes as missing data (callback to 11) **and** DAGs/backdoor/frontdoor/d-separation; do-calculus = pointer; confound-vs-randomize simulator.

**Part VI — The modern synthesis**
- **25** Bayesian Lenses on Deep Learning & Generative AI **[REORDER, was 23]** — **[TRIM]** conformal → capstone; diffusion/ICL stay conceptual; overparam-nets nonidentifiability callback; neural-SBI pointer.
- **26** Capstone: One Theory, Two Audits **[DEMOTE, was 24]** — lighter than a full module; ML-zoo audit table (add BART, conformal rows), reading map, PPL entry.

**Count verdict:** 27 numbered items (00–26), of which 26 is a sub-budget capstone → effectively **26 full modules + 1 capstone**. The growth is entirely two load-bearing splits (17→17a+18, 22→23+24); the six over-specced modules (08,12,16,19,20,25) are brought to budget by trimming, not splitting. If a hard 25-module cap is mandated, the only acceptable give is to keep 17 whole (accept it runs to the 5k ceiling with dense FDR/misspecification sections) — do **not** un-split 22.

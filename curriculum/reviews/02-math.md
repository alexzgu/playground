# Review — 02-conditioning-is-inference.md (mathematics referee)

**Verdict: REVISE** (1 sev-2). Harness PASS reproduced (exit 0, 9.1 s, deterministic,
zero warnings, numbers-contract clean). All mathematics is correct and every numeric
claim reproduces *exactly* under independent recomputation — with one exception: the
stated risk-curve crossover is a coarse-grid artifact and misstates the true value by ~25%.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| **2** | §02.4 reconcile ("Bayes wins for true N ≥ `1300`"), risk figure caption ("crossing below the UMVU near N=1300"), code L308 `crossover = grid[np.argmax(bayes_rmse < umvu_rmse)]` | The reported crossover **1300** is not the crossover — it is merely the first point of a coarse grid (`…,800,1000,1300,1600,…`) at which Bayes wins, and the grid skips straight from 1000 (UMVU wins) to 1300. Independent sim (6 seeds × 200 000 reps, sampler verified unbiased) puts the true crossover at **N≈1075** (UMVU wins at 1050, Bayes wins from 1075). The caption's "crossing … near N=1300" is simply false; "Bayes wins for N≥1300" is true-but-not-tight (Bayes also wins on [1075,1300)). Semantic mismatch: the *claimed* quantity (crossover location) ≠ the *printed* quantity (first-winning grid point). | Add grid points between 1000 and 1300 (e.g. `1050,1100,1150,1200`); report the crossover as ≈1075–1100 and fix the caption. Or: keep the coarse grid but relabel — call 1300 "the first grid N where Bayes wins," draw no "crossover" line, and state the true crossing is nearer ~1100. |
| 3 | §02.5 ("C-B **§1.3.4** tells the Three Prisoners story") | No section 1.3.4 exists in C-B (§1.3 has no numbered subsections); Three Prisoners is **Example 1.3.4**. The Bridge section already cites it correctly as "Example 1.3.4" — so the module is internally inconsistent. | Change "§1.3.4" → "Example 1.3.4". |
| 3 | Header ("**Runtime.** ~5 s") | Harness-measured runtime is 9.1 s, not ~5 s. STYLE §2 requires the *measured* value. | Update to ~9 s. |
| 3 | §02.4 ("the frequentist minimum-variance unbiased estimator (UMVU) m(1+1/n)−1") | The "UMVU / uniformly minimum variance" honorific — load-bearing for the predict-then-run trap — is asserted with neither derivation nor citation; only *unbiasedness* is verified numerically (`1001.3 ≈ 1000`). | Add a one-line cite/anchor (standard result; C-B §7.3 territory) so "minimum variance among unbiased" is warranted, not just asserted. |
| 3 | §02.5 box ("… 'is deferred to Chapter 4'"); Exercise 02.1 ("the Borel–Kolmogorov box in miniature") | (a) Quotation marks wrap a paraphrase — C-B's actual words are "we will defer these considerations until Chapter 4" (Ch1to5.txt L383); substantively accurate (and C-B even treats the Borel Paradox in Miscellanea 4.9.3), so cosmetic. (b) Monty Hall shares B–K's *moral* (event underdetermines the answer without a protocol) but not its *mechanism* (measure-zero limiting σ-algebra); "in miniature" slightly conflates a positive-probability problem with a measure-zero one. | Drop/loosen the quote marks; soften "in miniature" to "the same moral as the B–K box." |

No sev-1. Only the sev-2 forces the REVISE.

## Required-item checklist (SYLLABUS "02-conditioning-is-inference")

| # | Required | Status |
|---|---|---|
| 1 | Enumeration engine (joint table → condition), reusable; discrete-prob home w/ half-page pointer | ✅ `condition(prior,likelihood,obs)` §02.1; C-B §1.2–1.3 pointer |
| 2 | Medical test, predict-first; hand + 10⁷ sim; PPV `0.0194`; odds = (0.001/0.999)·(0.99/0.05) | ✅ §02.2; exact form present verbatim |
| 3 | German tank: uniform-prior posterior vs UMVU m(1+1/n)−1; predict-first "which wins MSE?"; risk curves | ✅ present — **but crossover misstated (sev-2)** |
| 4 | Sequential = batch, shown numerically | ✅ §02.3 (`0.2818` both, Δ `1.1e-16`) |
| 5 | Borel–Kolmogorov box tied to Monty Hall protocol dependence | ✅ §02.5 (technically correct; see sev-3 on "in miniature") |
| 6 | Monty Hall as exercise, both protocols via the engine | ✅ Ex 02.1 (`0.6667` vs `0.5000`) |
| 7 | Naive-Bayes spam: forward pointer to M15 only | ✅ Ex 02.3 is an additive-logit exercise that only *points* to M15 (does not build the classifier) |
|  | Bridges: additive log-odds; C-B §1.3 | ✅ §02.3 + Bridge |
|  | Sources booklet ch.2 / C-B ch.1; Deps 00,01 | ✅ |

STYLE: skeleton complete (Spine/Which-line/Promise/Prereqs/Runtime/Sources, Bridge,
Pitfalls×5, Exercises×4 predict-then-run w/ `<details>`, Takeaways×7); 4123 prose words
(in 2 500–5 000); notation per §3 (P/p, O(·), ℓ defined at first use); **no R**; setup block
verbatim; randomness via seeded generators only; every figure saved via `save()` and
discussed; all 4 PNGs present. Honesty labels: module carries warrant by
derivation/simulation/citation but uses none of STYLE's literal Theorem/Empirical/Heuristic/Open
tags — **and neither does any sibling module (00–04)**, so this reads as an accepted
house convention, not a module-02 defect.

## Independent recomputations (nothing imported from the module)

| quantity | module claims | my independent value | verdict |
|---|---|---|---|
| PPV (exact fraction) | `0.0194` | 11/566 = 0.019435 → 0.0194 | ✅ |
| prior odds / LR / post odds | 0.001001 / 19.8 / 0.0198 | 0.001001 / 19.8000 / 0.019820 | ✅ |
| prevalence at PPV=0.5 | `0.048` | 0.0481 | ✅ |
| per-100k swamp (TP/FP/ratio) | 99 / 4995 / ~50:1 | 99 / 4995 / 50.5:1 | ✅ |
| two-positive PPV (seq=batch) | `0.2818` | 0.281832 (fraction) | ✅ |
| LR² multiplier | ~392 | 392.0 | ✅ |
| German-tank post. mean (Nmax=2000) | `78.66` | 78.6649 | ✅ |
| closed form (m−1)(n−1)/(n−2) | `78.67` | **derived from scratch** (Beta-fn telescoping) = 236/3 = 78.6667; finite sum → it | ✅ |
| tank MAP | `60` | 60 (posterior ∝ 1/C(N,n), monotone ↓ on N≥m) | ✅ |
| UMVU m(1+1/n)−1 | `71.0` | 71.0; E[UMVU]=N exactly (unbiased) | ✅ |
| **risk crossover** | **near `1300`** | **N≈1075** (6 seeds×200k; UMVU wins ≤1050, Bayes ≥1075) | ❌ **sev-2** |
| E[max] sampling mean @N=1000 | 834.2 = n(N+1)/(n+1) | 834.2 | ✅ |
| Monty Hall A / B (switch) | 0.6667 / 0.5000 | 0.6667 / 0.5000 (exact rational enumeration) | ✅ |
| prosecutor P(guilty\|match) | 0.5000 / 0.0909 | 0.5000 / 0.0909 (exact) | ✅ |
| spam logits | 0.7200 / 0.8654 / 0.3913 | 0.7200 / 0.8654 / 0.3913 | ✅ |
| n=1 tank means | 119 / 116.1 / 1115.0 / 7416.5 | 119 / 116.1 / 1115.0 / 7416.5 | ✅ |

## Engine, Borel–Kolmogorov, citations

- **Engine** (§02.1): correct — conditioning = keep observed column and renormalize
  (`joint = prior[:,None]*lik; col=joint[:,obs]; col/col.sum()`); denominator is the
  evidence p(o*), as the docstring says. Tank code stabilizes the likelihood by
  subtracting `loglik.max()` before `exp` (numerically sound). API matches spec
  (prior (H,), likelihood (H,O), obs int → posterior (H,)).
- **Borel–Kolmogorov box**: technically correct. It (i) locates the ambiguity in the
  *limiting sequence of positive-probability events* / sub-σ-algebra, (ii) gives the
  standard sphere/great-circle example with the longitude-vs-rotated-frame dependence,
  (iii) does not overclaim (explicitly "no measure theory needed beyond this sentence")
  and correctly says the protocol is part of the model. Only nit is the later
  "in miniature" applied to Monty Hall (sev-3 above).
- **Citations verified by opening Ch1to5.txt**: Def 1.3.2 (L366, P(A|B)=P(A∩B)/P(B),
  P(B)>0) ✅; Bayes' Rule = eq. (1.3.5) (L422) ✅; Three Prisoners = **Example 1.3.4**
  (L387) ✅ (module's "§1.3.4" is the sev-3 mislabel); the Ch-4 deferral of
  probability-zero conditioning is real (L383) and C-B indeed treats the Borel Paradox
  in Miscellanea 4.9.3 (L4491) — the box's framing is on point. Booklet ch. 2 exists.

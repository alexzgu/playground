# Pedagogy review — 02-conditioning-is-inference

**Verdict: REVISE (light).** Fundamentally sound: skeleton complete, spine clear, both
required predicts captured, all C-B citations exact, numbers self-consistent, all four
figures referenced+discussed with takeaway captions, Monty Hall exemplary, non-tribal,
Borel–Kolmogorov box well-placed. The revisions below are staging/redundancy craft, not
content defects — but a demanding bar holds on the two marquee demos.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| MED | §02.2 "Predict (commit now)" (L77–79, L138–176) vs `00-four-lines.md` §medical-test (L105–152) | The module's flagship predict-before-reveal re-runs module 00's **identical** reveal — same PPV `0.0194`, same LR `19.8`, same second-positive retest — staged cold as a first encounter with **no callback to M00**, though M00 is a listed prereq. The "you'd guess 0.9" catch is already spent; the reader cannot be caught being wrong twice by the same number. Violates STYLE §1 ("callbacks are explicit and load-bearing") and the brief's compression/no-fluff bar. | Add an explicit callback ("M00 already caught you at 0.9; here we make conditioning mechanical and push past it") and re-aim M02's *Predict* at something M00 did **not** reveal — e.g. "at what prevalence does PPV finally cross 0.5?" or "how many positives to exceed even odds?" or "guess the 10⁷-patient error bar." Keep the genuinely new material (engine generality, MC error bar, log-odds-add figure). |
| MED | §02.4 "Reason" of the risk demo (L264) | On one of the **two required** surprises, the *Reason* step pre-reveals the resolution: "a biased rule that buys enough variance reduction can win." That hands over the answer to the Predict's "UMVU always / Bayes always / depends?" before the reader runs — softening the crossover surprise. Contrast §02.2's *Reason*, which names the flaw ("confusion of the inverse") without debunking it — the correct pattern. | Trim the *Reason* to name the intuition only ("'unbiased' + 'minimum variance' *sound* like they settle MSE"). Let Run + Reconcile deliver `bias²+variance` and the N≥1300 crossover. |
| LOW | Spine header (L3) | ~40-word compound sentence ("…build the joint table…, keep the column…, renormalize — and in odds form…") is overstuffed for the "state a week later" test; the mechanics belong in §02.1 (where they already are). | Tighten to the syllabus's crisp form: "Bayes' rule is the ratio of joints; posterior odds = prior odds × likelihood ratio." Move the build/keep/renormalize verbs into §02.1's prose. |
| LOW | §02.3 "Note also the number itself…" (L176) | The genuinely counterintuitive nugget — two 99%/95% positives still leave you at `0.2818` (< even odds) — is delivered as an un-staged aside, and it also already appears in M00's retest. A missed predict-before-reveal, or redundant. | Either stage it ("Predict: how many positives to exceed 50%?") or cut it as overlap; don't leave it as a decorative aside. |
| NIT | Exercise 02.3 (L397–415) | Syllabus item 7 said "naive-Bayes spam: forward pointer to M15 **only**," but the exercise builds a labeled 3-feature naive-Bayes worked example. Acceptable (toy hand-set LRs, teaches the *required* additive-logit bridge, explicitly defers the real classifier to M15) — but it grazes the scope line. | Keep; it's the module's ML-connected exercise and it forward-points correctly. Just ensure M15 doesn't re-teach the additive-logit identity as new. |
| NIT | Header "Runtime. ~5 s" (L6); code blocks | Optimistic given 10⁷-patient sim + 12,000-rep × 8-point tank grid + 2×10⁶ Monty Hall draws. All numpy-vectorized so plausibly fine, but unverified here. | Defer to `run_module.py`; update the header to the measured value. |
| NIT | §02.1 opening (L10–11) | Opens on the two abstract "lines" before the first concrete real instance (medical test, §02.2); the engine self-check is generic, not a motivating instance. Borderline vs STYLE §1 "lead with the concrete." | Blessed by the spine-callback + engine-first mandate, so optional; a one-line concrete hook before the engine would sharpen it. |

**Counts:** High 0 · Medium 2 · Low 2 · Nit 3.

## Learner's-eye summary (5 lines)

1. I leave with one reusable move — build the joint, keep the column I saw, renormalize — and the odds mantra (prior odds × LR); both are stateable a week later.
2. The medical test lands hard the first time, but I *just did this exact PPV=0.0194 reveal in module 00* — re-asking "guess the PPV (you'll say 0.9)" felt like being quizzed on a punchline I already knew.
3. The tank crossover is the best part — "unbiased isn't optimal" genuinely surprised me — though the *Reason* line half-told me the answer before I committed.
4. Monty Hall as two-hosts-one-engine is the cleanest thing here; the Host-B = 1/2 result reorganized my intuition, and the protocol/Borel–Kolmogorov box arrived exactly when I needed it.
5. Log-odds-add → "this is the logit your classifier carries internally" is the callback that made me feel the ML tie in my hands, not just my notes.

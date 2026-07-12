# Pedagogy review — 24-causal.md

**Verdict: APPROVE** — the four hard goals are all achieved (collider reflex genuinely
*reversed*; Simpson lands as a decision rule not a curiosity; untestable identification is the
sobering close with full weight; IPW = M09 importance weights is a clean "same math, new name"
moment). 7 findings: 0 high, 2 medium, 5 low. One MED (#1) is a one-line code fix I'd want made
before publish — it does not change any prose number.

All prose backtick-numbers cross-checked against `tools/logs/24-causal.out.txt` — the numbers
contract holds (every quoted value is printed at the quoted precision). Skeleton complete
(Spine/Which-line/Promise/Prereqs/Runtime/Sources → §24.1–24.7 → Bridge → 5 Pitfalls → 4
Exercises → 7 Takeaways). Blocks **9 exposition + 4 exercise = 13** (≤16 cap met; matches the
expected 9+4). Figures **6/6** referenced with real captions AND discussed. Prose **4,992 words**
(at cap). Predict-then-reveal present on §24.1, §24.2, §24.3, §24.4, §24.7 and all 4 exercises;
each names the naive intuition. ML-connection exercise (24.2, IPW = RL off-policy evaluation) and
surprising-answer exercises (24.1 collider; 24.4 confounding fully explains the signal) present.

## Findings

| Sev | Location | Issue | Concrete fix |
|-----|----------|-------|--------------|
| **MED** | §24.7 code, line `ate_B = sum(np.mean(UB==u) * (YB[UB==u].mean() - YB[UB==u].mean()) for u in (0,1))` | At the module's climactic "different answer, same data" moment the true ATE for DGP B is a **tautology**: `YB[UB==u].mean() - YB[UB==u].mean()` is `a − a = 0` by construction — it never touches `TB`, so `0.000` is hardcoded, not demonstrated. This violates the module's own ethic (STYLE §6: "the printed agreement IS the pedagogy") precisely where rigor matters most; a code-reading learner sees the sobering number is asserted, not computed. | Compute the genuine within-stratum treated−control difference: `YB[(UB==u)&(TB==1)].mean() - YB[(UB==u)&(TB==0)].mean()`. With Y⊥T\|U by construction it prints ≈`0.000` (± Monte-Carlo noise), now *demonstrating* zero effect rather than writing it. Update the `+0.000` backtick if the honest value rounds differently. |
| **MED** | §24.6 (whole section — the M09 payoff) | The estimator trio and the positivity/ESS collapse are revealed with **no Predict/Reason staging** — the only marquee demo in the module without a captured prediction (STYLE §1: "a surprise shown without a captured prediction is a defect"). The genuine catch is live here: the poor-overlap point estimate `3.427` looks plausible while the ESS silently reads `16.4%`. A reader who isn't first made to commit to "the estimate will look obviously broken" isn't *caught* being wrong. | Add a Predict before the poor-overlap block: "Positivity is broken. Will the damage show in the *point estimate* (obviously off), or only in the ESS?" Reason: names the reflex "a bad estimate announces itself." Reconcile then lands `3.427`-looks-fine / ESS-`16.4%`-betrays — the whole "watch the weights, not the estimate" lesson, now earned. |
| LOW–MED | Exercise 24.1 vs §24.4 reconcile | The exercise's answer — adjust-`{C}`-alone gives `0.216` — is already **spoiled verbatim** in §24.4's reconcile ("Adjusting for $C$ alone gives `0.216`, equally wrecked"). The predict-then-run surprise is pre-revealed, so the exercise re-runs a number the attentive reader already has. | Either drop the parenthetical `0.216` from §24.4 (let the exercise own it), or give 24.1 a genuinely new twist (e.g. adjust for `{C}` *and* a noisy proxy for `U`, showing the collider damage survives a partial confounder fix). |
| LOW | Exercise 24.2 reconcile | Clipping moves the estimate from `3.135` to `3.484` — i.e. *further* from the true `E[Y(1)]=3`, which the exercise never states. The reconcile says "stabilizes at the cost of a little bias" but hides that on this draw clipping visibly *hurt* accuracy. The bias-variance trade is more honest if the reader can see the cost. | Quote both numbers and state the true `E[Y(1)]=3`: "clipping moved the estimate `3.135`→`3.484`, *away* from the true 3 — that visible bias is what you pay to triple the ESS." Makes the trade concrete instead of reassuring. |
| LOW | Bridge (~150 words) | At the 4,992-word cap the flagged compressible fat is the Bridge: it re-states §24.1 (missing-data/50%), §24.6 (IPW/`ess_kong`), and §24.7 (untestable) that the reader just finished. §24.5's density (backdoor + frontdoor + do-calculus + table) is by contrast *earned* — do not cut there. | Keep if the cap tolerates it (the Bridge is mandated). If enforced, trim the Bridge's §24.6 and §24.1 recaps to one clause each; the load-bearing sentence is the closing "four lines run on a joint you had to choose." |
| LOW | §24.1 code, `print(f"units with BOTH ... : {0}")` and `{50.0:.1f}%` | Two "results" are printed as hardcoded literals rather than computed. Definitionally true (one column observed per unit), so far milder than #1, but performative in a module that elsewhere insists on real computation. | Compute for consistency: `int(((T==0)&(T==1)).sum())` (→0) and `100*(1 - Yobs.size/(2*N))` or similar (→50.0). Optional. |
| LOW | §24.5 close + Takeaway 7 | Paradigm-neutrality is stated cleanly (once in §24.5, restated as Takeaway 7 by design) — this is *right*, not a hedge. Only gap: the load-bearing claim "identification is orthogonal to Bayes-vs-frequentist" is asserted, not warranted. | Optional half-sentence: "orthogonal because identification fixes *which* joint you condition on, while the Bayes/frequentist choice is only *how* you summarize the conditioning — lines chosen before line 2 runs." Ties it back to the spine. |

## Learner's-eye summary (5 lines)

1. I came in controlling for everything by reflex; §24.3's collider caught me flat — I committed to
   "partial corr ≈ 0, independence is independence" and watched conditioning *manufacture* corr `-0.503`
   from nothing. §24.4 then broke me operationally: adjust-`{U}` nails `2.001`, add the collider `C`
   and it collapses to `0.504`, *worse than doing nothing*. "A collider you adjust for is a confounder
   you create" is now a reflex, and "throw in every covariate" is dead.
2. Simpson landed as a *rule*, not a party trick: §24.2 showed treatment helping in every stratum
   (`+0.10`) while "hurting" in aggregate (`-0.1428`), and the reconcile refused the word paradox
   ("arithmetic, not paradox") — adjust the fork, and the very next section shows the identical move
   is *wrong* for the collider. The side-by-side four-bar figure IS the decision rule.
3. §24.6's "IPW weights are module 09's importance weights" is the moment the course clicks shut —
   `1/e(X)` is `p/q`, `ess_kong` is verbatim, and positivity failure is a light-tailed proposal
   (ESS `16.4%`, one weight at propensity `0.00006`). "Same math, new name," not a metaphor.
4. §24.7 is the honest ceiling: two DGPs, byte-identical joints (`0.0013` apart), ATEs `0.200` vs
   `0.000` — no test on the data can choose. It closes the module with real weight and retro-justifies
   §24.1's randomization. (One blemish: the DGP-B "true ATE = 0" is a hardcoded `a−a`, not a genuine
   stratified computation — finding #1 — the one place the code doesn't earn its number.)
5. Neutrality held: "neither dialect is more Bayesian," identification happens *before* inference,
   the PO↔DAG table aligns the two languages onto one joint. No tribal victory lap — just "the hard
   part is choosing the joint."

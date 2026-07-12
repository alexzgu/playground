# Pedagogy review — 03-generative-stories

**Verdict: REVISE (light).** Strong module: skeleton complete, spine crisp and
stateable, the Cauchy marquee is staged textbook-perfectly (captured numeric
commitment → refutation → two-line theorem), the information section is genuinely
load-bearing with all three forward threads present, Ex 03.3 delivers the required
Geometric-not-Poisson shock, and it *derives the catalog* instead of reciting C-B
ch. 3. Every prose number matches the run log. One real staging gap on the opening
Poisson demo plus framing nits — no content defects.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| MED | §03.1 (L46 "The surprise is what this structureless placement *implies*"; demo L54–88) | The opening Poisson-process demo is a marquee demonstration and the prose explicitly calls it a **surprise** ("Three quantities … each turn out to have a named law, none of which you put in by hand"), yet it runs Setup → Run with **no captured Predict beat**. STYLE §1 is explicit: "A surprise shown without a captured prediction is a defect." The learner is *told* the crystallization is surprising instead of being *caught* not anticipating it — the exact failure mode the contract targets. This is the module's first demo, so it also sets the staging tone. | Add a one-line Predict before the code: "Before running — you placed points as structurelessly as possible (uniform, given the count). Guess the distribution of the gaps between consecutive arrivals. Most people say 'uniform' or 'no pattern.'" Then let Exp/Gamma/Poisson land as the reveal. Cheap fix, high payoff — it converts an *asserted* surprise into a *felt* one. |
| LOW | §03.2 Predict (L134) vs demo (L149–157) | The marquee Predict frames the horizon as "As n climbs toward **10⁶**," but the running-mean figure caps at `n_show = 200_000` and the IQR table tops out at `n = 100_000`. A reader who commits based on 10⁶ then sees evidence stop at 10⁵ gets a small credibility ding on the module's flagship demo (conclusion is unmistakable regardless). | Change "toward 10⁶" to "toward 10⁵" to match the code, or push `n_show`/the IQR grid to 10⁶ (Cauchy draws are cheap; runtime is only 15 s). Keep prose and sim on the same horizon. |
| LOW | §03.2 Predict (L134) vs payload | The Predict asks a **location** question ("where does X̄ₙ go? Commit to a number") — the learner commits to 0 — but the quoted numeric evidence is the **IQR** of the sample-mean distribution (`2.026 → 1.931`), a *spread*. The direct refutation of "→0" is the wandering-running-mean figure (present and good); the IQR is the quantification of a claim the reader wasn't asked to make. Slight predict/payload mismatch on the signature demo. | Either broaden the Predict to also commit on spread ("…and will the *spread* of X̄ₙ shrink like 1/√n?") so the IQR table settles a captured guess, or foreground the running-mean panels as the reveal and demote the IQR to supporting evidence. Minor — the demo still lands. |
| NIT | §03.2 Reconcile (L160) | "a single draw of size 10⁴ yanks the whole average sideways" reads as "a draw of magnitude ~10⁴"; it actually means one Cauchy draw among the first 10⁴ that is large. Momentarily confusing on the key intuition. | Reword: "a single outsized draw yanks the whole running average sideways, and it never recovers." |
| NIT | Takeaways (L462–470) | Exactly 7 bullets (STYLE cap is ≤7) and each is dense/compound — the "reproduce from memory a week later" bar strains at bullets 4 and 5 (each packs the full entropy/cross-entropy/KL identity *and* the three-role forward map). Not a violation, but at the ceiling. | Optional: split bullet 4 (definition) from bullet 5 (three roles) only if you drop the softmax half of bullet 7 into the exponential-family bullet; or leave as-is — it's compliant. |
| NIT | §03.4 core max-ent demo (L283–319) | Not staged predict-first — correctly, since it *confirms* the derivation just shown, and the genuine surprise (mean-only → Geometric) is properly deferred to Ex 03.3 with full staging and foreshadowed at L319. Noting only to confirm this is the right call, not a defect. | None. Satisfies the task's "check the max-ent demo too" — the surprise is correctly relocated to the exercise. |

**Counts:** High 0 · Medium 1 · Low 2 · Nit 3.

## Learner's-eye summary (5 lines)

1. I leave able to *derive* a family from its mechanism — "Poisson count, then uniform placement" spat out Exp gaps, Gamma waits, and Poisson counts, and I saw the KS statistics confirm it — but §03.1 *told* me that was surprising instead of letting me guess the gaps and be wrong first.
2. The Cauchy demo is the one that reorganized me: I committed to "X̄ₙ → 0," watched the running means wander forever, and the two-line characteristic-function proof (X̄ is *itself* Cauchy) made it stick — heavy tails, not small n, is the disease.
3. Entropy / cross-entropy / KL finally clicked as one object with `H + KL = cross-entropy` printed in front of me, and knowing it's the same thing that becomes M15's training loss, M13's ELBO, and M17's score makes it feel like infrastructure, not a detour.
4. Ex 03.3 got me clean — I said "Poisson(3)" and the answer was Geometric; realizing "counts at rate 3" names *two* families depending on what I actually know is the compression I'll keep.
5. Softmax = max-entropy with temperature as the Lagrange dial tied my ML reflexes to the theory, and "we derived the catalog instead of memorizing C-B ch. 3" is exactly how the whole thing felt.

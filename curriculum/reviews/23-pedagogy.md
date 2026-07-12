# Pedagogy review — 23-experimental-design.md

**Verdict: APPROVE** (polish-level findings only; the hard goal — four claims kept genuinely
separate, non-tribal throughout — is fully achieved). 7 findings: 0 high, 1 medium, 6 low.

All 34 prose numbers cross-checked against `tools/logs/23-experimental-design.out.txt` — the
numbers contract holds (two backtick-rounding exceptions noted below). Skeleton complete
(Spine/line/Promise/Prereqs/Runtime/Sources → 23.1–23.6 → Bridge → 6 Pitfalls → 4 Exercises →
7 Takeaways). Blocks 13 exposition + 4 exercise = 17 (≤16 exposition cap met). Figures 6/6
referenced and discussed. Predict-before-reveal present on all five demos + all four exercises,
each naming the naive intuition. ML-connection exercise (23.3, active-learning=EIG) and
surprising-answer exercise (23.1, peek-doesn't-cost-coverage) both present.

## Findings

| Sev | Location | Issue | Concrete fix |
|-----|----------|-------|--------------|
| **MED** | §23.3c, code line `t10 = typeI_at_looks(10)  # continuous: peek every step, min 10 obs` | The comment is a copy-paste error from the `t_cont` line: `t10` is **ten equally-spaced looks**, not continuous monitoring. In the module's centerpiece lab, a mislabeled comment on the exact line the reader studies to tell "10 looks" from "continuous" undercuts the four-claim separation. | Change comment to `# ten equally-spaced interim looks to N=1000`. (The genuine continuous line, `t_cont`, is correctly commented one line down.) |
| LOW–MED | Ex 23.1 reconcile: "≈0.95 (about `0.95`)"; Ex 23.3 reconcile & §23.5-adjacent: "both ≈`0.1` nats" | Backtick numbers `0.95` and `0.1` are rounded, not printed at that precision (code prints `0.9514`, `0.1065`, `0.1078`). STYLE §4.3/§8.3 wants backtick-numbers to match printed precision; the mechanical grep may flag these (passes only on substring matching). | Quote the printed value in backticks (`0.9514`; `0.1065`/`0.1078`) or drop the backticks and keep the plain "≈0.95"/"≈0.1" as prose approximations. |
| LOW | Whole module (~5,170 words, ~3% over the 5,000 cap) | The overage is *earned* — §23.3's four-claim lab is the room used well and should not be cut. If compression is demanded, the slack is in the **Bridge** (recaps §23.4/23.5 already stated) and **§23.6** (its "design justifies the test" thesis was largely made in §23.1). | Verdict: keep. If forced, trim the Bridge's second half by ~60 words; do **not** touch §23.3. |
| LOW | §23.4 spike-and-slab block: `tau1, w = 80.0, 0.5` | Slab scale 80 and prior P(real)=0.5 appear without justification; inclusion probabilities depend on them, and a textbook-owning reader will ask "why 80?" | Add one clause: slab scale set to the order of the real effects (~hundreds Å/min), and note in prose that inclusion probs are mildly sensitive to the slab width — the *ordering* (A,C,AC in; rest out) is what's robust. |
| LOW | §23.2 reconcile / Pitfall / Takeaway: "power is concave over plausible effects" | Power (sum of two Normal CDFs) is concave only *above* its inflection; below δ≈0.3 it is convex. The Jensen argument holds because the N(0.5,0.2²) prior's bulk sits in the concave region, but the blanket phrasing slightly overstates. | Scope to "concave over the bulk of this prior's support" in at least the first (§23.2) statement. |
| LOW | §23.4: "the $AB$ effect halves, from $-24.9$ to $-15.0$" | Numbers in math mode (not backticks), rounded from printed `-24.875`/`-14.967`; inconsistent with the module's otherwise-backticked convention. | Backtick the printed values, or state "roughly halves" without the two rounded figures. |
| LOW (non-tribalism watch) | §23.2 close + Pitfall: "assurance is the honest number" | The module's non-tribalism is otherwise exemplary (see summary). This lone phrase subtly valorizes the Bayesian quantity — the single line most likely to read as a victory lap, though it *is* scoped fairly ("pricing certainty at a δ nobody has"). | Optional softening: "assurance is the number you can act on" — keeps the point, drops the value word. Not required. |

## Learner's-eye summary (5 lines)

1. I arrived believing the slogan "Bayesians can peek"; I leave able to state **four separate
   claims** — posterior unchanged (a), prior-averaged coverage survives (b), frequentist Type-I
   inflates ~4×/~9× (c), selective reporting breaks *everyone* (d) — and I can say which quantity
   each is about. They no longer blur.
2. §23.1 genuinely caught me: I picked "(iii) the likelihood is deaf to intentions" and the
   confounded posterior sat 17 SDs from the truth — the *Bayesian* model was the confidently-wrong
   one, which is exactly why "indifferent to stopping ≠ indifferent to assignment" landed.
3. The module never gloats: it explicitly refuses "frequentist tests are broken" ("Nothing
   contradicts — they measure different things"), turns the tables on the Bayesian in claim (d)
   and the Bayes-factor caveat, and lands "calibration is a property of the model plus the
   reporting process, not of the paradigm." This is the non-tribalism brief, honored.
4. Power-vs-assurance and EIG both felt *operational*, not like rebrands — Jensen made assurance
   the lower, act-on-able number, and EIG "price where uncertainty is reducible" tied cleanly to
   BayesOpt/active learning and (via the Bridge) M22's EVSI.
5. The one thing that would have tripped me on a careful read: the mislabeled `# continuous`
   comment in the Type-I block (it's actually the 10-look line) — fix that and the lab is airtight.

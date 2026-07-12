# Pedagogy review — 26-capstone.md

**Verdict: APPROVE** — the capstone does the one job that matters: it reads 26 modules
back as a single sentence and hands the learner a *sorting* skill (theorem/approx/heuristic/none)
plus a working decision guide, without tribalizing. The ledger is the standout — every row cites a
number the learner *personally printed*, verified against the module logs (see below), so recall is
genuine ("I ran that"), not a summary someone else wrote. Non-tribalism holds all the way to the
last line. 7 findings: 0 high, 1 medium, 6 low. The one MED is a structural retrieval fix worth
making before publish; it changes no prose number.

**Numbers contract — PASS.** `run_module.py` exits 0 in 27.0 s (3 blocks: setup, ledger, demo);
1 figure referenced with a real caption AND discussed. Every prose backtick-number matches printed
output. I independently traced each ledger row to the cited module's log: `0.2044`/`0.0522`/`0.9494`/
`1.00e-08` → 23-experimental-design; `p=0.0099`/`BF01 1.80→17.93` → 17-model-checking; `0.0739`/
`0.1046` → 18-scale; `0.0207`/`0.0401` → 15-glms; `0.500`/`1.000` → 06-estimates; BvM `0.9499` →
08-frequentist-bridge. All present at quoted precision. The marginalize-vs-profile demo prints
`t cov 0.9508` / `plug-in 0.8942`, width ratio `1.312` — the right final hands-on beat: it closes
the nuisance thread and recompiles the old "z vs t" rule into line-3 marginalization.

**Skeleton / length.** Header spine (Spine/Which-line/Promise/Prereqs/Runtime/Sources) present and
capstone-appropriate ("All four, in retrospect"). §26.1–26.5 → Pitfalls (5) → Exercises (3,
predict-then-run) → Takeaways (6). Prose **2,498 words incl. tables** (1,991 excl.) — at the very
top of the syllabus's 1,500–2,500 capstone exception. Compression is mostly clean; the only dense
run-on is §26.1's six-split recap paragraph (finding #4). Fill-in-first zoo honestly lets the
"none" rows (SVM hinge, boosting) stand — no Bayesian imperialism, which is exactly right.

## Findings

| Sev | Location | Issue | Concrete fix |
|-----|----------|-------|--------------|
| **MED** | §26.2 fill-in-first prompt (the 20-name bulleted list before the `<details>` reveal) | The syllabus mandate is a "**blank column presented first**" self-test; the panel's retrieval-practice requirement is *structural* forcing. As written, the 20 procedures are a single comma-separated blockquote line with a prose instruction to "write down (a)…(b)…". A learner scanning a name-list can skim past without committing per-row — the retrieval is *requested*, not *forced*. This is the one place the module under-delivers on an explicit syllabus item. | Render the 20 as an actual **blank two-column table** (`Procedure | your reading | your status`) with empty cells the eye is compelled to fill, then reveal the filled table. Fund the added table rows (module is at the 2,498 cap) by trimming finding #4's recap paragraph — a clean trade of re-narrated numbers for genuine retrieval structure. |
| LOW | Whole module — no `## Bridge` heading | STYLE §2 mandates ≥1 explicitly labeled Bridge per module; §8.1's skeleton gate checks for it. The capstone omits the heading. Defensible (the entire module is bridge-work — §26.4 calibrated Bayes, the ledger, the zoo are all C-B/booklet/ML tie-ins), but a strict verifier will flag the missing label. | Either add a one-line `## Bridge` that names the module as the course's synthesis bridge (CASI "in book form"; C-B second-pass pointers), or leave a one-clause note that the Bridge mandate is discharged module-wide. Cheap insurance against the skeleton gate. |
| LOW | §26.5 reading map, MacKay line ("Occam-as-evidence (M17)") | The Occam/evidence thread this course actually runs spans M17 *and* M20 (GP marginal likelihood / ML-II is Occam's razor as evidence). Annotating MacKay with M17 alone under-cites the thread the reader lived. | Extend to "Occam-as-evidence (M17), the marginal-likelihood razor behind GP model selection (M20)" — matches the brief's own "extends M17/M20" hint and makes the annotation course-specific rather than generic. |
| LOW | §26.1 six-split recap paragraph (line ~69) | At the cap, this is the one paragraph that becomes a dense recital — six mechanisms in one breath ("θ-independent stopping cancels… diffuse alternative pays an Occam tax… right about a wrong model"). Each clause is warranted (not a list of nouns), so it is *earned* density, but it re-narrates numbers the ledger code just printed. It is the natural budget source for finding #1. | Cut to the 2–3 splits that most need the mechanism spelled out (stopping-rule likelihood cancellation; Lindley's Occam tax), and let the ledger's printed rows carry the rest. Frees words for the blank table. |
| LOW | Exercises 26.1, 26.2 — "Run" steps are "re-read the M23 ledger rows" / "compare against §26.2's reveal" | STYLE §5 wants the Run to be "the exact code — a ≤10-line variation." Two of three exercises have no runnable code; they are recall/self-test prompts. Reasonable for a synthesis chapter (26.3 *does* carry real code, and its reconcile — t-quantile reconstructs the marginal interval because `s²/n` = `bₙ/(aₙκₙ)` — is a genuine, correct catch), but note the deviation. | Acceptable as-is for a capstone; if a verifier enforces §5 literally, give 26.1 a 3-line code stub (recompute the `0.2044` vs `0.9494` split from the M23 idiom) so at least "which audit catches it" is *run*, not only recalled. |
| LOW (nit) | §26.1 Reconcile, "The plug-in interval is `1.312`× narrower" | The printed quantity is width ratio *t/Normal* = `1.312` (t is 1.312× *wider*). "1.312× narrower" inverts the printed ratio colloquially — readable, but technically the plug-in is a factor 1.312 *below* the t width, not 1.312× narrower. | Quote the widths to make it unambiguous: "the plug-in is narrower by a factor `1.312` (width `1.943` vs `2.548`)." |
| LOW (nit) | Ledger code row `("calibration: ECE audit", …, "0.0207 …")` tagged `[M15]` vs prose §26.1 "Calibration (M15/M25)" and Takeaway attribution | The printed row cites M15 only; the prose and stance attribute M15/M25. The `0.0207`/`0.0401` numbers are M15's (15-glms). Minor inconsistency in which module owns the row. | Make the code row `[M15/M25]` to match the prose, or drop /M25 from the prose — pick one so the attribution is single-valued. |

## Learner's-eye summary (5 lines)

1. The ledger is where the course *paid out*: every row was a number I had watched print with my own
   seed — `0.2044` Type-I inflation, `0.9494` credible coverage surviving the same peeking, `17.93`
   Bayes factor climbing *for* the null as `p` rejected. Reading them stacked, "posterior = what to
   believe, sampling distribution = how to check it" stopped being a slogan and became the shape of
   six hard-won splits. This did not read as someone's summary; it read as my own lab notebook.
2. The one new demo caught me exactly as promised: I committed to "n=6 pins σ², plug-in barely
   differs," then watched the plug-in cover `0.8942` while the honest t held `0.9508` — the z-vs-t
   rule I was handed years ago, revealed as line-3 marginalization of a nuisance. Earned, not told.
3. The zoo self-test worked *when I actually did it* — but the comma-list of 20 names let me
   half-skim; a blank table with empty cells would have forced the retrieval the reveal then graded.
   That SVM's hinge loss is allowed to sit at **none** — no forced posterior — is what made me trust
   the rest of the column instead of suspecting a Bayesian sales pitch.
4. The decision guide is the page I will actually reopen: "small-n with nuisances → marginalize,
   audit with prior-averaged coverage" is a move I can execute Monday, not a platitude.
5. The close landed as capability, not commencement: I came in able to *run* ridge and dropout; I
   leave able to say what each *is*, read off its prior, and name the audit that catches it — and,
   for a method I have never seen, sort it into theorem/approx/heuristic/none. "One calculus, two
   audits, run both" leaves me a working statistician, not a partisan.

# PROGRESS.md — living state of the curriculum build

**Resume protocol:** read this file, then BRIEF.md (goals) and STYLE.md (author contract). Continue from "Next actions". Update this file after every completed step.

## State as of 2026-07-11 (session 1)

### Done
- Source library identified and indexed in BRIEF.md (booklet md, C-B ch1–10 txt, ISLP, Montgomery DOE 8e, Levin–Peres MCMT, Lawler stoch. calc — PDFs text-extractable via pypdf; poppler NOT installed).
- Packages: numpy/scipy/matplotlib/pandas/sklearn/statsmodels/arviz/pymc/numpyro/jax installed. **PyTensor C backend broken in this codespace** (static libpython, linker error) — PyMC default sampler unusable (pure-python mode works but too slow for real models). **DECIDED: NumPyro is the course PPL** (8.6 s cold incl. JIT; ArviZ interop verified). Canonical idioms in `tools/ppl_idioms.py` — all smoke-tested green; traps found & encoded: obs arrays must be numpy not jnp; observation sites need explicit plates for Predictive; arviz 1.x plot_* returns PlotCollection (use .savefig); az.loo needs numpy-cast manual log_likelihood.
- `BRIEF.md` (authoritative goals), `OUTLINE-draft.md` (25-module draft v0), `STYLE.md` (author contract: voice, notation table, code contract, exercise format, review gates).
- `tools/run_module.py` (verification harness: runs md code blocks, numbers-contract check, determinism check, stats) — self-tested green via `tools/selftest-module.md`.
- `tools/pymc_idioms.py` written; PyMC C-backend failure discovered by it.
- Outline panel IN FLIGHT: 5 Opus agents → `panel/proposal-ml-first.md`, `panel/proposal-theory-first.md`, `panel/critique-rigor.md`, `panel/critique-pedagogy.md`, `panel/critique-coverage.md`.

### Next actions
1. ~~Panel → SYLLABUS.md~~ **DONE**: all 5 panel outputs in `panel/`; **`SYLLABUS.md` v1 is the binding work order** (27 modules 00–26, six waves; rigor corrections embedded: Kong ESS formula, digamma CRP mean, 0.234-at-d≈50, softened Ng–Jordan, optional-stopping four-claim split, prior-averaged coverage semantics).
2. ~~PPL decision~~ **DONE**: NumPyro; idioms all green in `tools/ppl_idioms.py`.
3. ~~Wave 1 (00–04)~~ **DONE & FINAL**: 5 modules authored → 10 reviews (math+pedagogy per module, all in `reviews/`) → revisions applied → full sweep green (18,589 prose words total, all PASS, zero warnings). SPINE-INDEX canonical. Notable catches fixed in revision: S3 heading-spoiler (04), tank risk-crossover grid artifact 1300→≈1075 (02), scipy nbinom convention trap (04), finite-additivity scope on Dutch book (01), un-staged decision reveal (00).
4. ~~Wave 2 (05–08)~~ **DONE & FINAL**: 4 modules → 8 reviews → revisions → sweep green (17,265 prose words; total course now 35,854 words across 9 modules). Notable: two author spec push-backs formally adjudicated CORRECT by referees (06's midrange-concentration argument; 08's Gamma-BvM choice); recurring defect = missing Predict beats (now pre-warned in author prompts).
5. ~~Wave 3 (09–13)~~ **DONE & FINAL**: 5 modules → 10 reviews → revisions → sweep green (course now 14 modules, ~58k prose words). Notables: NumPyro modules (12, 13) idiom-clean; referee settled the booklet "ESS ≥ n" dispute from source (name-collision, not misprint — SYLLABUS amended); survived a third session-limit interruption (6 agents resumed, zero loss).
6. ~~Wave 4 (14–18)~~ **DONE & FINAL**: 5 modules → 10 reviews → revisions → sweep green (course now 19 modules, ~80k prose words). Notables: two more author-vs-spec adjudications went to the AUTHOR with syllabus amendments (MacKay gap is exactly zero at p=0.5; eight-schools EB τ̂ is exactly 0 at the boundary); a referee's cross-seed analysis caught a cherry-picked-seed EB demo (rebuilt MC-averaged); az.waic confirmed removed in arviz 1.x (hand-WAIC established).
7. ~~Wave 5 (19–23)~~ **DONE & FINAL**: 5 modules → 10 reviews (ZERO sev-1 — cleanest wave; the predict-beat pre-warning worked) → revisions → sweep green (course now 24 modules, ~102k prose words). Notables: CRP digamma correction landed; Montgomery Ex 6.1 reproduced and hand-verified; the four-claim optional-stopping lab (incl. the martingale-coverage construction) referee-verified correct; M04's oldest promise (~4× at 10 looks) cashed exactly; one tautological self-check caught and replaced with genuine two-route verification.
8. ~~Wave 6 (24–26)~~ **DONE & FINAL**: all 27 modules (00–26) authored, dual-refereed (54 reviews total), revised, harness-green — **the full curriculum is written** (~117k prose words + verified deterministic code + ~130 figures). Wave-6 notables: the two-DGPs-same-joint identification example proven analytically; a hardcoded a−a "verification" caught and replaced; a canon-drift in the capstone's cross-module ledger caught against SPINE-INDEX; the triage ledger converted to blank-first practice. Module 25 is 5,694 words (over cap, flagged per STYLE — review-mandated additions).
9. ~~Global consistency pass~~ **DONE — COURSE COMPLETE**: 3 course-level audits (697 cross-module references, 55 helper names, ~20 shared constants, notation sweep, whole-arc read) → 1 sev-1 (module-06 coverage-notation collision → γ(r)) + handful of sev-2/3, all fixed and re-verified; README.md written; **full 27-module determinism sweep: 27/27 PASS, zero warnings**. Arc auditor's verdict: "the course ships — the four-line spine is genuinely load-bearing, non-tribalism holds start to finish, all ten intended judgment-nuggets land."
10. ~~Post-completion iteration round 1~~ **DONE**: (a) OUTLINE-draft retired to panel/; (b) 27 companion notebooks generated + byte-equivalence-verified (tools/make_notebooks.py, notebooks/); (c) **full-course fresh-read** (5 readers, all 27 modules cold, all ~130 figures opened vs prose): found 2 defects every structured review missed — a silent indexing bug distorting 16's radon figure (no printed number touched, hence invisible to the numbers contract) and 21's ellipse beat teaching the wrong resolution (code right, prose wrong — introduced post-review); plus 15's mathematically-identical "three lines" figure, 00's `$1` math-render leak, 23's leaked tool-syntax EOF tags, ~12 sev-3s. ALL FIXED and re-verified (reviews/FINAL-read-{A..E}.md).
11. ~~Iteration round 2~~ DONE: QUICKREF.md (referee-verified, ~110 claims); EXAM.md (12 integrative cross-module problems, referee-verified, P11 retuned); flashcards/deck.tsv (164 Anki cards, 164/164 canon-audited). Committed through `819b1be`.
12. ~~PREREQUISITES section~~ **DONE & FINAL** (user request 2026-07-17): the invisible-skills layer. Research: 5 studies (~940 mined course instances with module:line refs; 71 source rows; 65 expert-graded skills, 30 GATEs) in prereqs/research/. Build: prereqs/SPEC.md → P0 predict-and-check diagnostic (24 items, 9 live traps, routing table — cashes the pedagogy panel's unbuilt suggestion) + P1–P7 drill modules (density algebra / expectation operator / precision thread [six costumes one identity; curvature=precision five ways] / transforms+domains / bounds+approximations / linear algebra / computing craft). QA: 10 referee passes — caught a fabricated wall in P3 (invented "module-16 SE bug") and an inert trap in P0 (det(0.1·I) at n=100 doesn't underflow), both fixed and SECOND-referee certified (28/28 and 24/24 re-keys clean). All 8 files harness-green, byte-deterministic. Wired into README + module 00's assumed-background note. ~21k prose words of drills.
6. After each wave: update this file; coherent `git add -A` commit. (Survived one session-limit interruption mid-Wave-1: all agents resumed via SendMessage with context intact — this is the recovery pattern.)

### Layout
```
curriculum/
  BRIEF.md STYLE.md OUTLINE-draft.md PROGRESS.md   # governance
  SYLLABUS.md                                      # (pending) final spec
  panel/                                           # outline panel outputs
  modules/NN-slug.md                               # (pending) the course
  figures/<slug>/                                  # generated by module code
  data/                                            # small committed CSVs only
  tools/run_module.py                              # verifier (see STYLE.md §8)
  tools/logs/<module>.out.txt                      # captured run output
```

### Standing decisions
- Module numbering NN = 00–24 (may change post-panel; SYLLABUS.md wins once written).
- Verification gates in STYLE.md §8 are mandatory before a module counts as done.
- All temp/scratch work goes to the session scratchpad, not the repo.
- 2-CPU box: one heavy background job at a time; module code <120 s target / 300 s cap.

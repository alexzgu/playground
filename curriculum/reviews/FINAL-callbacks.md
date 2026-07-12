# FINAL cross-module callback & integrity audit

Course-level audit of all 27 modules (00–26) against `modules/SPINE-INDEX.md` (canon).
Scope: every inter-module reference, quoted helper name, quoted cross-module number,
SPINE promise, signature staging, and header prereq/callback line.

## Verdict: essentially CLEAN — 2 findings (0 sev-1, 1 sev-2, 1 sev-3)

No broken references, no wrong numbers, no fabricated-callback survivors. Every quoted
number attributed to another module agrees with canon; every quoted helper name resolves
to a real definition in the cited module. The two findings are a header callback the body
never makes, and one SPINE-INDEX self-description that overstates what a module contains.

## Findings

| sev | module:location | issue | fix |
|-----|-----------------|-------|-----|
| 2 | `24-causal.md:6` (Prereqs/Callbacks header) | Header lists "Callbacks to ... **18 (winner's curse / selection)**", but module 18, "winner's curse", and "selection" appear **nowhere else in M24's body** — the only occurrence of "selection" in the whole file is this header line. The other two callbacks in the same clause *are* delivered as machinery (09 = `ess_kong`/IPW, cashed explicitly; 05 = backdoor-as-conditioning, cashed conceptually), so the reader is primed to find an M18 tie-in and finds none. The target itself is valid (M18 does own winner's curse), so this is misleading-not-broken. | Either cash it — one clause noting that positivity-restricted overlap / collider-conditioning is a *selection* phenomenon of the same family as M18's winner's curse — or drop "18 (winner's curse / selection)" from the header. |
| 3 | `SPINE-INDEX.md:101` (M15) and `SPINE-INDEX.md:77` (M11) | SPINE says M15 established/promises "**Pólya-Gamma named only**" and M11 promises "**Pólya-Gamma → M15**". In fact **M15 never mentions Pólya-Gamma at all** (0 occurrences). The reader-facing text is self-consistent — M11 §348/§551 names Pólya-Gamma and correctly says "*module 15 fits logistic models by NUTS instead*", i.e. it does **not** forward-promise that M15 names PG — so no reader chases a dead pointer. The defect is only in the INDEX's summary of M15/M11. | In SPINE-INDEX, change M15's "Pólya-Gamma named only" and M11's "Pólya-Gamma → M15" to reflect reality: Pólya-Gamma is named and motivated in M11; M15 uses NUTS instead. |

## Verified clean (what was checked)

- **Callback / reference audit:** 701 module-reference tokens grepped (118 `MNN` + 583 `module NN`), 697 of them cross-module (target ≠ source). Reference matrix built source→target; every high-traffic edge spot-checked semantically. All ~120 possessive "`module NN's <claim>`" citations verified against the target's actual content — all accurate (e.g. M14→M05 `student_t_predictive` scale² = bₙ(κₙ+1)/(αₙκₙ); M09→M03 t₃ Var=ν/(ν−2)=3; M22→M08 complete-class; M24→M09 self-normalized IS/`ess_kong`).
- **Helper-name audit:** 55 named helpers checked — each is defined in the module the citations attribute it to, and cited under the same name: `gaussian_condition` (M05 → used M14/M20/M21), `ess_kong` (M09 → M21/M24), `nig_regression` (M14 → M21), `nig_post` (M04 → M05/M11/M13/M17), `ece()` (M15 → M25 verbatim), `normal_known_var_update`, `beta_binomial_update`, `student_t_predictive`, `leapfrog`, `rw_metropolis`, `blr_posterior`, `gp_posterior`, `stick_break`, `bootstrap_pf`, etc. No name mismatches.
- **Number-consistency audit:** every cross-module constant agrees with canon across all occurrences —
  PPV `0.0194` (M00/M02); A/B `0.9510` + regret `81×` (M05→M22/M26); eight-schools 28→`8.23`, μ `6.49`, τ `2.80` (M16, cited by M18); tank crossover `≈1075` (M02, no stale "1300"); acceptance `0.234`/`0.44`/`0.651` (M10/M12); sandwich `0.0739`/`0.1019`/`0.1046` (M18→M26); martingale coverage `0.9494` (M23→M26); Type-I `0.0522`→`0.2044` (M23→M26/M04); Lindley `0.0099`, BF₀₁ `1.80`→`17.93` (M17→M26); ECE `0.0207`/`0.0401` (M15→M26); BvM `0.9499` (M08→M26); CRP digamma E[K₅₀₀] `6.793`/`23.587` (M19); EB width ratio `0.8657`(J=10)→`0.9989`(J=1000) (M18, cites M16's 0.73/J=8); Beta(10,4) mean `0.7143` (M04); plug-in own-coverage `0.9525` (M05); posterior mean `78.66` (M02).
- **Stale-value red-flag sweep (all negative):** no crossover "1300" (1300 appears only as a grid coordinate); no generic EB ratio "0.2778" anywhere; "α·log n / α ln n" appears **only** correctly framed as the *crude approximation that errs in an α-dependent direction* (undercounts 6.21 vs 6.793 at α=1, overcounts 31.07 vs 23.587 at α=5), never as the CRP mean; M21's "ESS falls" is the correct within-filter degeneracy (877.7→1.48 over steps) that explicitly cites M09's ESS-fraction-collapse, not the disallowed "ESS falls as M grows".
- **Signature experiences:** S1 (M12), S2 (M05), S3 (M04), S4 (M08), S5 (M17) — each marked in the module title AND staged in a numbered section; S5 additionally cross-cited correctly by M13 §531 and M20 §299.
- **Promise audit:** SPINE promises sampled across the spine and verified cashed, including the non-obvious ones — M04→M23 stopping-rule "~4×@10 looks" (explicitly "now cashed" at M23:289), M02→M15 naive-Bayes/logistic, M20→M13 inducing-points-as-ELBO + M20→M26 BART map entry, M01→M23 permutation null (explicitly cashed at M23:474), M11→M13/M19 augmentation, M12→M16 funnel/non-centering. Only uncashed item found is the M15 Pólya-Gamma index mismatch (sev-3 above).
- **Prereq-line audit (8+ modules spot-checked against real callbacks):** M14 (05/06/08), M16 (05/08/12), M20 (05/14/17), M21 (05/09/14), M18 (16/17 + 06/08/12), M25 (13/15/18/12 + 01/07), M23 (04/07 + 01/05/17), M24 (11/23 + 09/05/18) — all listed dependencies are real and heavily referenced, with the single exception of M24's uncashed "18" callback (sev-2 above). M23's and M24's "05 (conjugate Gaussian / backdoor = conditioning)" callbacks deliver the concept via the `blr`/backdoor machinery though they do not name module 05 — acceptable.

**Counts:** 697 cross-module references checked · 55 helpers · ~20 shared constants across all occurrences · 5 signatures · 8 prereq lines · ~15 promises sampled. 2 findings (sev-2 ×1, sev-3 ×1).

# P7-computing-craft — combined referee (math + pedagogy)

**Verdict: REVISE** (0 sev-1, 1 sev-2, 6 sev-3). One substantive fix; the rest polish.
Harness: `PASS in 2.3s (2842 prose words, 16 blocks, 1 fig)`, determinism byte-identical, **zero warnings**.

## Findings

| sev | location | issue | fix |
|---|---|---|---|
| **2** | P7.6 capstone, Check 1 (prose ~L345 vs block L336–337) | Prose: "The sampler mean matches the analytic Beta mean **to within the Monte-Carlo standard error**." Printed evidence contradicts it: `|mean diff| 0.0007` **exceeds** `MC-SE 0.0004` (1.75×). In a module whose thesis is numerical honesty and "compare the two printed numbers," the claim is falsified by its own output. The block even comments `# (ignoring autocorrelation)` — the naive SE understates because the Metropolis chain is autocorrelated (ESS ≪ 38 000), which is exactly why the diff can sit at ~1.75× the *naive* SE. | Reword to the honest, richer statement: "the difference (`0.0007`) is comparable to the MC-SE — and note the naive SE (`0.0004`) *understates* the true uncertainty because the chain is autocorrelated (ESS < n, P7.5)." Ties the capstone back to P7.5 and stops overselling "within one SE." |
| 3 | Header L7 | `**Runtime.** ~7 s.` but measured single-run is **2.3 s** (determinism harness). STYLE requires the *measured* runtime. | Change to `~2–3 s`. |
| 3 | P7.1 prose L72 | The `log1p`/`expm1` claim ("near x=0 they keep the digits that `log(1+x)` and `exp(x)-1` throw away") is asserted without a printed warrant, unlike logsumexp/softplus/gammaln, which each print a real `inf`. STYLE §1 warrant rule. Verified true: `log1p(1e-16)=1e-16` vs `log(1+1e-16)=0.0`; same for `expm1`. | Add one printed line to the P7.1 fix block: `log1p(1e-16)` vs `log(1+1e-16)` (→ `0.0`). Closes the only log-domain tool shown by prose alone. |
| 3 | P7.2 marquee, block L98–100 | The marquee spoils its own answer: inline `# WRONG`/`# RIGHT` comments and the true mean `4.0` are given *before* the run, so no prediction is captured. STYLE §1 predict-before-reveal for marquees. (Mitigated: all 6 drills have genuine Predict beats; the SPEC prereq format leans on the drill for prediction.) | Optional: move the RIGHT/WRONG labels below the run, or add a one-line "predict which of A/B/C matches mean 4 before scrolling." |
| 3 | "Where the course uses this" table L375, L380 | Two rows exceed SPEC's "3–6 refs": Log-domain = 7, Verify = 8. (Verify is the #1 skill, 28 hits — arguably justified.) | Trim each to ≤6, or leave Verify and note the overflow is deliberate. |
| 3 | P7.2 marquee L98–99 | The "two wrong ways" (A `rng.gamma(2,0.5)`, B `stats.gamma(a=2,scale=0.5)`) are the *same* conceptual error (rate-passed-as-scale) across two libraries, not two distinct mistakes. Pedagogically fine (shows the trap crosses numpy/scipy) but the reader meets one error twice. | Keep, or make B a genuinely different plausible error; low priority. |
| 3 | Citations L91, L91 | `11:45` comment actually at `11:42` (3-line drift); module-03 `gamma(a=k, scale=1/lam)` idiom at `03:85`/`03:112`, cited as `03:81` (which holds the `expon` idiom). Both within SPEC's "few numbers" drift tolerance. | No action required; noted for completeness. |

## Math / code hat — checklist

- [x] **Determinism + harness:** PASS, 2.3 s, byte-identical, zero warnings.
- [x] **Parameterization table, every row:** numpy `gamma(2,0.5)`→mean 1 (wrong for rate 0.5); `wayC=gamma(2,1/0.5)`→4 ✓. scipy `gamma(a=2,scale=0.5)`→1 ✓. `invgamma(a=3,scale=2)`=b/(a-1)=1 ✓ ≡ `1/gamma(3,1/2)` (both →0.99) ✓. `expon(scale=1/4)`→0.25 ✓. `nbinom(n=5,p=0.3)` mean `r(1-p)/p=11.667` ✓ (ran moment check; scipy counts failures, `p`=success prob = "the other outcome"). Moment-check table prints all 5 with `ok`. Marquee's two wrong ways are the genuine rate-as-scale mistake; moment-check exposes them unambiguously (A/B 1.00, C 4.00).
- [x] **Module-16 bug miniature:** faithful — `u_home[cidx]` is a per-home array indexed by county ids (valid indices 0–4 < 12), silent, **length preserved 12**, wrong slope (`-2.064` vs planted `2.006`). Both catches genuine and correctly scoped: the shape `assert` does **not** fire on the equal-length double-gather (correctly stated) but **does** catch the length-5 sibling `recover(u_cty)` (fired: `shape (5,) != (12,)`); the known-answer check is the *only* thing that catches the double-gather. Discriminates cleanly.
- [x] **Log-domain demos are real failures:** `log(sum(exp([1000,1000])))`→`inf`; `log(1+exp(800))`→`inf`; `comb(2000,1000)`→`inf` (verified), `gammaln` route →`1382.27`. Underflow drill: `exp(-1000)`→`0`→`log(0)=-inf`, logsumexp `-999.8731`. (log1p/expm1 true but un-printed — sev-3 above.)
- [x] **float64 truths:** `1e16+1==1e16` True; `0.1+0.2!=0.3` True; cancellation `E[x²]-E[x]²`→`0.0` vs `np.var`→`0.6667` (true 2/3, honest); `cdf(40)`→1.0→`log(1-p)=-inf`, clip→finite. All correct.
- [x] **Capstone soundness:** MH step 0.05 on Beta(15,29) (sd≈0.07); 38 000 draws, thinned ×10 for KS (p=0.335 > 0.05) — thinning addresses autocorrelation for KS validity ✓. Planted-truth drill (0.35 → conjugate 0.3491) framed correctly. **Rule-of-succession honesty is correct:** flat prior → post mean `(k+1)/(n+2)=0.3333`, held *distinct* from MLE `k/n=0.3250` ("adjacent to," not equal). (Check-1 SE wording = the sev-2.)
- [x] **Seeds/spawn/vectorize:** `default_rng`; `reseed(42)` twice → corr 1.000 (identical); `spawn(2)` independent; `seed+i` trap shown (adjacent corr 0.007, "no guarantee") — matches numpy best practice. `(reps,time,arms)` pattern: `random((R,T,3))<rates` broadcasts correctly, cumsum-along-time / `arange[None,:,None]` shapes right, recovers `[0.30,0.50,0.70]`.
- [x] **6+ wall quotes verified at source:** `15:69`, `25:262`, `21:363`, `10:111`, `03:81`, `14:329`, `16:353`, `EXAM:92/100`, `EXAM:302/321`, `22:196`, `19:141`, `21:79`, `16:70`, plus table refs `17:262`, `EXAM:226`, `22:207`, `14:108`, `23:431`, `25:127`, `01:155`, `08:82` — **all accurate** (~20 checked, zero fabrications; only minor line-drift noted above).

## Pedagogy hat — checklist

- [x] **SPEC drill-room format:** all 6 skills carry Reflex → The wall (real cited line) → The fix (≤15-line install) → Drill (predict-then-run, STYLE §5). 
- [x] **Capstone lands as closing message:** P7.6 (verify-against-known-special-case, the #1 mined skill, 28 hits) explicitly "closes the room"; final takeaway names it "the safety net under every other skill here." Strong.
- [x] **Closing cross-ref table present:** "Where the course uses this," 6 rows, module:line walls (two rows slightly over the 3–6 bound — sev-3).
- [x] **Length/blocks/runtime:** 2842 words (1,800–3,200 ✓); 10 exposition + 6 drill blocks (exposition within 6–14 ✓); 2.3 s (<60 s ✓, header overstates — sev-3).
- [x] **No fluff, reflex tone:** opens on a claim ("float64 is not ℝ…"), imperative reflexes, assumes BRIEF learner. Clean.
- [~] **Predict-first:** genuine in all 6 drills; the P7.2 **marquee** self-spoils via inline WRONG/RIGHT (sev-3).

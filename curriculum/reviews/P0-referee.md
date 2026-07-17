# P0-diagnostic — combined referee (math + staging)

**Verdict: REVISE.** One sev-1 (Q17's ⚠ trap is inert and its premise is false), one sev-2, three sev-3.
Determinism: `python tools/run_module.py prereqs/P0-diagnostic.md --check-determinism` → **PASS in 1.6s, 0 warnings**, 1500 prose words (in-band 1,200–2,000), 9 batched blocks.

## Findings

| sev | item / location | issue | fix |
|---|---|---|---|
| **1** | **Q17** (L150, L159, L165, table row 17) | The ⚠ premise is **false at n=100**. `det(0.1·I₁₀₀)=1e-100` is fully representable — it does **not** underflow, and naive `log(det)` = **−230.26**, *identical* to `slogdet`. So (a) the code comment `# (underflow)` and the bullet "`det=1.0e-100` underflows toward 0 (naive `log(det)`=−∞)" state a falsehood; (b) this is the **one ⚠ item whose naive answer is actually correct** — the trap never fires; (c) it contradicts its own routing target **P6.2**, which deliberately uses `0.1·I₄₀₀` (det=`0.0`, log=−∞, slogdet=−921.03) *because* 100 is too small. A fluent reader who commits "naive→−∞" per the item's framing is told they're right while the true behavior is finite: the diagnostic miskeys the lesson. | Raise the dimension above 323 so the determinant genuinely underflows to `0.0`, e.g. `n=500` → `det=0.0`, `log(det)=-inf`, `slogdet=-1151.29`. Do **not** reuse P6.2's `n=400/−921.03`. Update L150 ("100×100"→"500×500"), the L159 print, the bullet, and table row 17's answer. |
| **2** | Q17 code comment L159 + bullet L165 | Same root cause, staging facet: even if kept, `# (underflow)` mislabels a representable value and the parenthetical "naive `log(det)`=−∞" is wrong. After the n-fix this resolves; flagged separately so the revision verifies the *narrative* now matches output, not just the number. | Covered by the sev-1 fix; re-run and confirm the printed naive path actually yields `inf`/`-inf`. |
| 3 | Q12 (n=20→k=19) vs **P4.6** | Drill duplication: P4.6's worked example is *exactly* n=20, α=0.9, k=19. P0 pre-echoes the routed section's marquee number. (Arithmetic itself is correct.) | Vary the constants, e.g. n=50, α=0.9 → k=⌈51·0.9⌉=46. |
| 3 | Q20 (`rng.gamma(2,0.5)`→mean 1) vs **P7.2** | Drill duplication: P7.2's marquee is the identical call `rng.gamma(2.0,0.5)` with the same "mean 1, not 4" framing. | Use a different pair, e.g. `rng.gamma(3,0.25)` (rate 4 → mean 0.75, trap value 12). |
| 3 | Q14 (10 looks × 0.05 = 0.50) vs **P5.3** | Minor: P5.3's Predict line is 10×0.05=0.50. Only the trivial ceiling is reused (not the simulated 0.20), so low impact. | Optional: change to 8 looks → ceiling 0.40. |

Note: the author *did* de-duplicate Q6 (P0 uses discrete {2,4}; P2.6 uses Gamma(2,1)) and Q2 (Beta(6,3) vs P1.2's Beta(10,4)), so the pattern is inconsistent, not systemic.

## 24-item recomputation tally (independent, by hand/code)

| # | recompute | printed key | verdict |
|---|---|---|---|
| 1 | θ-free const divides out → identical | `8.9e-16` | ✓ |
| 2 | Beta(6,3), mean 6/9 | `0.6667` | ✓ |
| 3 | 5!/3!=120/6 | `20` | ✓ |
| 4 | {10,11,12}=6/36 | `0.1667` | ✓ |
| 5 | E[0.3N]=3 | `2.9989` (sim) | ✓ |
| 6 | (½+¼)/2=.375 > 1/3 | `0.3750`>`0.3333` | ✓ trap |
| 7 | 1/(½+⅓)=6/5 | `1.2000` | ✓ trap |
| 8 | 1/√25 | `0.2000` | ✓ |
| 9 | ×4; ratio (3/10)/(3/20) | `2.0` | ✓ |
| 10 | Exp(1), mean 1 | `0.9975` | ✓ |
| 11 | scale=SD → var 16 | `16.0` | ✓ trap |
| 12 | ⌈21·.9⌉=⌈18.9⌉=19; cov 19/21=.905 | `19` | ✓ trap |
| 13 | .6931 < log2.5=.9163 | `0.6931`<`0.9163` | ✓ trap |
| 14 | 10·.05 | `0.50` | ✓ |
| 15 | (¼)²·.25=.0156 | `0.0156` | ✓ |
| 16 | Σ⁻¹=diag(1,.01); axis1=1 | axis 1 (`1.00`/`0.0100`) | ✓ |
| **17** | **det=1e-100 (NOT underflow); naive log=−230.26 = slogdet** | `1.0e-100`/`-230.3` | **✗ ⚠ premise false — naive works** |
| 18 | A=3,b=6: mean 2, var 1/3 | `2.0`/`0.3333` | ✓ |
| 19 | 1000+log2; exp(1000) overflows→inf | `1000.6931`/`inf` | ✓ trap |
| 20 | shape·scale=2·.5=1 | `1.00` | ✓ trap |
| 21 | 1e16>2^53, ULP=2 | `True` | ✓ trap |
| 22 | 1/5, exact for Gaussian | `0.2000` | ✓ |
| 23 | binom.sf(59,100,.5) | `0.0284` | ✓ |
| 24 | Beta(9,13), 9/22 | `0.4091` | ✓ |

**Tally: 23/24 correct. 1 defect (Q17).** Of the 9 ⚠ items, 8 genuinely trap the naive answer; **Q17 is the lone ⚠ whose naive answer is correct** — precisely matching the "watch the slogdet edge case" flag.

## Other criteria (all PASS)

- **Routing table:** all 24 rows point at real shipped sections (P1.1/1.2/1.6/1.3, P2.1/2.4/2.6, P3.1/3.3/3.4, P4.2/4.3/4.6, P5.1/5.3/5.6, P6.1/6.2/6.3, P7.1/7.2/7.4/7.5/7.6 — verified against each module's headers). Each target teaches the claimed skill (spot-checked P4.3=scale-is-SD for Q11, P4.6=⌈(n+1)α⌉ for Q12, P6.2=slogdet for Q17). The 3 spanning items' dual routes are all real (Q22 P3.3×P5.6, Q23 P2.1×P7.5, Q24 P1.3×P7.6). Calibration line present (0–4/5–10/11+).
- **Item quality:** every Q demands a committed number/direction/choice answerable from general fluency; none require course-internal knowledge (Q12's formula and Q24's conjugacy are self-contained).
- **Format:** 1500 words, batched code blocks, every printed answer backticked in the verdict bullets + table, 5-line intro carries the module-00 pointer, no teaching leakage (Q→run→one-line verdict throughout).
- **Watch-items re-verified individually:** conformal index arithmetic ✓, Jacobian direction (Q10) ✓, delta-method variance (Q15) ✓, curvature=precision numbers (Q8/Q22) ✓ — all clean; only slogdet (Q17) fails.

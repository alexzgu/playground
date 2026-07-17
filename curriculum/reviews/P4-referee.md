# P4-transforms-domains — combined referee (math + pedagogy)

**Verdict: APPROVE.** Determinism PASS, zero warnings, 5.6 s, 2413 prose words, 13 blocks, 2 figs. All numeric claims reproduce; all spot-checked walls exist at (near) cited lines; the Jacobian, predictive-SE, softmax, conformal, and location–scale machinery are correct. No sev-1, no sev-2. Three sev-3 polish notes below.

## Findings

| sev | location | issue | fix |
|---|---|---|---|
| 3 | P4.2, the Jacobian-bias reveal (`0.2857→0.2001`) | The section's #1-gate headline number is shown without its own captured **Predict** step — the reader is caught wrong on the *shape* (flat-isn't-flat) but not on the *bias magnitude/direction*. SPEC sanctions a two-part marquee with a single shape-predict, so this is within the work order, but STYLE §1 ("a surprise shown without a captured prediction is a defect") wants a commitment here too. | Add one line before the bias code: *"Predict: dropping the Jacobian shifts E[θ] toward 0 or toward 1, and by roughly how much?"* Costs two sentences, converts the punchline into a caught-wrong moment. |
| 3 | P4.4 fix, prose "forces the validation mean to exactly `0.000`" | Block prints `own-moments=-0.000` (negative zero). Substring grep still passes (`0.000` ⊂ `-0.000`), so the numbers contract is not violated, but the sign is cosmetically off. | `+ 0.0` before formatting, or quote `-0.000` in prose. |
| 3 | P4.6 fix, inline comment `# k-th smallest == method="higher"` | True for this demo's `(n=20, α=0.90)` — verified `sort[k-1] == np.quantile(·,0.90,method="higher")` — but it is **not** a general identity: the canonical conformal call passes level `⌈(n+1)α⌉/n` (=0.905 here, as EXAM:799 does), not `α`. The two coincide only at these params. The demo itself uses `np.sort[:,k-1]` so the guarantee is airtight regardless. | Soften comment to "k-th smallest (here also = method='higher' at this level)" or pass the `⌈(n+1)α⌉/n` level to mirror EXAM:799. |

## Math hat — checklist

- [x] **Determinism / harness:** PASS, 0 warnings, byte-stable, <60 s, pure numpy/scipy.
- [x] **Jacobian rule** `p_φ(φ)=p_θ(f⁻¹(φ))·|dθ/dφ|`: derived from the CDF for monotone `f`, correct direction, `+log|dθ/dφ|` on the log scale. Absolute value present for generality.
- [x] **Marquee bias:** module reports **means** (not modes) and both are analytically exact — with-Jacobian E[θ]=Beta(2,5) mean `2/7=0.2857`; forgotten-Jacobian pushforward is exactly Beta(1,4) (θ¹(1−θ)⁴÷[θ(1−θ)]=(1−θ)³), mean `1/5=0.2000`≈printed `0.2001`; bias `−0.0856` correct. Direction of the dropped factor (|dφ/dθ|) verified.
- [x] **flat-isn't-flat:** θ(1−θ)∘expit is the standard logistic density; `0.2500` at ψ=0, `0.0452` at ψ=3, ratio `5.53` all reproduce; samples-free/densities-pay distinction correct and prominent.
- [x] **√(1+1/n) vs √(1/n):** Var(yₙₑ𝓌−ȳ)=1+1/n derived (mean uncertainty + fresh unit noise); SE-width undercovers `0.6271`, predictive `0.9514`; width ratio √7=`2.646`. Semantically clean.
- [x] **Softmax shift-redundancy:** softmax(z)=softmax(z+c) invariance and pin-one-logit fix correct; ordered = first-free + exp-gaps + cumsum correct.
- [x] **Conformal:** k=⌈(n+1)α⌉=`19`, coverage guarantee ⌈(n+1)α⌉/(n+1)=19/21=`0.9048`; naive `0.8669` undercovers, order-stat `0.9080` ≥ target; small-n correction genuinely bites. method-sensitivity print honest.
- [x] **Location–scale / NIG→t:** `t_scale=√(bₙ/(aₙκₙ))` is the marginal-on-μ scale, consistent with M11:107 / EXAM:285 (predictive widening handled separately, consistent with M05 canon). scipy `scale`=SD flagged repeatedly.
- [x] **Argmax invariance:** monotone/temperature never moves argmax nor crosses the 0.5 binary threshold (logit sign test); exact, all flip-counts `0.0000`.
- [x] **Slope recovery:** one-transform `b/s_x` (P4.4) and two-transform `b̃·s_y/s_x` (Ex P4.3) both correct.
- [x] **Wall spot-checks (10, target 6):** EXAM:234, EXAM:285, EXAM:787, EXAM:799, M15:47, M07:183, M11:107, M25:105, M25:124 — **exact**. M13:126→127, one-line drift (within SPEC tolerance). M25:59 = pin-one-logit in live use (silent-use wall, apt).

## Pedagogy hat — checklist

- [x] **Drill-room format:** Reflex → Wall (real cited quote) → Fix (≤15-line runnable) → Drill present across P4.1–P4.6; inline drills where they earn it, remainder carried by the Exercises block.
- [x] **Marquee predict-first:** flat-isn't-flat staged Setup→Predict→Reason→Run→Reconcile; predictive-SE and conformal drills likewise. (Bias-reveal predict is the sev-3 above.)
- [x] **Closing cross-ref table:** "Where the course uses this" — 6 skill rows, 4–6 module:line refs each, all in-range against SPINE-INDEX.
- [x] **Drills per §5:** genuinely surprising answers (flat→Haldane spike Ex P4.1; undercoverage P4.6) and an explicit ML connection (Ex P4.2 temperature/classifier; standardization leakage; argmax) both present.
- [x] **Length / blocks / runtime:** 2413 words (1,800–3,200), ≤14 exposition blocks, 12 s (<60 s), no PPL.
- [x] **Fluff / tone:** opens on a claim, no throat-clearing, reflex-installation voice throughout; callbacks (M05 predictive, M07 Jeffreys, M12/M16 non-centering) are load-bearing and real.

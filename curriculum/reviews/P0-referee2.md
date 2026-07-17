# P0-diagnostic — second referee (post-revision, triggered by pass-one sev-1)

**Verdict: CERTIFIED-CLEAN.** 24/24 correctly keyed. The pass-one sev-1 (Q17 inert trap) is fixed and now fires. No new defects, no new duplication.

Determinism: `python tools/run_module.py prereqs/P0-diagnostic.md --check-determinism` → **PASS in 1.7s, 0 warnings**, 1506 prose words (in-band), 9 batched blocks.

## Full 24-item independent re-key

| # | independent recompute | printed key | verdict |
|---|---|---|---|
| 1 | θ-free coeff (120 vs 21) divides out on normalization | `8.9e-16` | ✓ |
| 2 | θ⁵(1−θ)² → Beta(6,3), 6/9 | `0.6667` | ✓ |
| 3 | 5!/3! = 120/6 | `20` | ✓ |
| 4 | {10,11,12} = (3+2+1)/36 = 6/36 | `0.1667` | ✓ |
| 5 | E[0.3N] = 0.3·10 | `2.9989` (sim→3) | ✓ |
| 6 ⚠ | (½+¼)/2 = .375 vs 1/3 = .333 (1/x convex) | `0.3750`>`0.3333` | ✓ fires |
| 7 ⚠ | 1/(½+⅓) = 6/5 (not avg 2.5) | `1.2000` | ✓ fires |
| 8 | 1/√25 | `0.2000` | ✓ |
| 9 | ×4; (3/10)/(3/20) | `2.0` | ✓ |
| 10 | −log U ~ Exp(1), mean 1 | `0.9975` | ✓ |
| 11 ⚠ | scale=SD ⇒ var=4² (not 4) | `16.0` | ✓ fires |
| 12 ⚠ | ⌈51·0.9⌉=⌈45.9⌉=46 (not 45); cov 46/50=.92≥.90 | `46` | ✓ fires |
| 13 ⚠ | (0+ln4)/2=.6931 < ln2.5=.9163 (log concave) | `0.6931`<`0.9163` | ✓ fires |
| 14 | 20·0.01 union ceiling (truth lower — stated honestly) | `0.20` | ✓ |
| 15 | g'(4)²·Var = 0.25²·0.25 = .015625 | `0.0156` | ✓ |
| 16 | Σ⁻¹=diag(1,.01); axis1 cost 1 vs .01 | axis 1 `1.00`/`0.0100` | ✓ |
| 17 ⚠ | 0.1⁵⁰⁰=10⁻⁵⁰⁰ < 5e-324 ⇒ det underflows 0.0; naive log(0)=−inf; slogdet=500·ln0.1=−1151.29 | `0.0e+00`/`-1151.3` | ✓ **fires (fixed)** |
| 18 | A=3,b=6: mean b/A=2, var 1/A=1/3 | `2.0`/`0.3333` | ✓ |
| 19 ⚠ | 1000+ln2=1000.6931; exp(1000) overflows → naive inf | `1000.6931`/`inf` | ✓ fires |
| 20 ⚠ | numpy gamma(shape,scale): 3·0.25=0.75 (rate-read→12) | `0.7497`→0.75 | ✓ fires |
| 21 ⚠ | 1e16 > 2⁵³, ULP=2 ⇒ +1 lost | `True` | ✓ fires |
| 22 | 1/5, exact for Gaussian target | `0.2000` | ✓ |
| 23 | binom.sf(59,100,.5)=.0284 | `0.0286` (sim) | ✓ |
| 24 | Beta(1+8,1+12)=Beta(9,13), 9/22 | `0.4091` | ✓ |

**Tally: 24/24 correct.** All 9 ⚠ traps (Q6, Q7, Q11, Q12, Q13, Q17, Q19, Q20, Q21) verified to genuinely fire — each naive answer differs from the printed correct answer.

## Focused checks on the four changed items

- **Q17 (was inert @ n=100 → now n=500):** the sev-1 is resolved. 10⁻⁵⁰⁰ sits below float64's smallest subnormal (~5e-324, i.e. log10 floor ≈ −323.3; 500 > 324), so `det` genuinely underflows to `0.0e+00`, naive `log(det)` genuinely yields `-inf`, and `slogdet` recovers `-1151.29` (rounds to −1151.3). Narrative now matches output; premise true. No reuse of P6.2's n=400/−921.03.
- **Q12 (n=50, α=0.9):** ⌈(50+1)·0.9⌉ = ⌈45.9⌉ = 46. Coverage 46/50 = 0.92 ≥ 0.90 — guarantee statement consistent. De-duplicated from **P4.6** (n=20 → k=19).
- **Q20 (gamma(3, 0.25)):** scale-read mean 3·0.25 = 0.75 (sim 0.7497); rate-intent 3/0.25 = 12 — both stated correctly. De-duplicated from **P7.2** (gamma(2.0, 0.5), mean 1 vs 4).
- **Q14 (20 looks × 0.01):** union ceiling 0.20; bullet keeps bound-vs-actual honest ("truth is lower, but this is the reflex"). Distinct from **P5.3**'s marquee (10 × 0.05 = 0.50 ceiling); the 0.20 role here is a *bound*, whereas P5.3's 0.2044 is the *simulated actual* — no marquee-number collision.

## Duplication / routing (PASS)

- No new duplication introduced. Q12/Q20/Q14 constants now differ from their routed sections' marquees; the previously de-duplicated Q2/Q6 remain distinct.
- All 24 routing targets exist among the shipped section IDs (P1.1–P7.6 enumerated; every referenced ID present). Q17→**P6.2** (Cholesky / log-det) is the correct home for the slogdet lesson. Rows unchanged from pass one and still valid.
- Calibration line (0–4 / 5–10 / 11+) present.

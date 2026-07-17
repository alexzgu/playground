# P1-density-algebra — combined referee (math + pedagogy)

**Verdict: REVISE** (2 sev-2, 3 sev-3; zero sev-1 → no second referee triggered).
Determinism: `run_module.py … --check-determinism` **PASS in 1.8s, zero warnings**, 14/14 blocks green, 2604 prose words (in 1,800–3,200), 8 exposition blocks (in 6–14), runtime 1.8s (<60s), pure numpy/scipy. The mathematics is correct throughout and every printed number checks; the two sev-2s are contract/verification issues, not computational errors.

## Findings

| sev | location | issue | fix |
|---|---|---|---|
| 2 | P1.2 wall, line 83 | Verbatim CB quote *"We now recognize the integrand as the kernel of a beta(α+n,β) pdf"* (`Ch1to5.txt:2567`) is **unverifiable in this repo** (source material `curriculum_material/` not present) and **conflicts with the one corroborating record**: `prereqs/research/mined-sources.md:15` gives the representative quote for that skill/line-set as *"…the kernel of another **gamma** pdf"*. The `beta(α+n, β)` parameterization is also atypical for CB Ch.1–5, which is pre-Bayesian (Bayes is Ch.7) — a posterior-update parameter there is a red flag. | Reopen CB 2567 and paste the exact text. If 2567 is genuinely a gamma-kernel line, correct the quote to gamma (and pick a real beta-kernel line for the Beta narrative, or drop the family claim). Do not present a paraphrase as a verbatim quotation. |
| 2 | P1.2 fix, line 85; Takeaways line 305 | **Dirichlet kernel absent.** SPEC P1 names the spot-the-kernel families "Beta/Gamma/Normal/**Dirichlet**"; the module teaches five shapes (Beta, Gamma, Normal, Poisson, Gamma-in-λ) with no Dirichlet, so the simplex/multinomial read-off reflex is never installed (M05 `dirichlet_mult_update`, M19 stick-breaking lean on it). | Add a one-line Dirichlet read-off to the "five shapes" list: θ₁^{α₁−1}···θ_k^{α_k−1} → Dirichlet(α), *add 1 to each exponent* — it reinforces the marquee off-by-one theme and is the simplex generalization of Beta. Update Takeaways to say six shapes / name Dirichlet. |
| 3 | Drill P1.6 Reconcile, line 275 | "Γ(500)≈10^1134" is off by ~3 orders: actual log₁₀Γ(500) = **1131.39** (verified). Un-printed approximation, so not a numbers-contract breach, but a stated magnitude that's wrong. | Change to "≈10^1131" (or print it). |
| 3 | Drill P1.3 Run, line 159 | Prose says "All three are `(7, 5)`" but the block prints the raw tuple `(np.int64(7), np.int64(5))` — the clean `(7, 5)` the prose quotes never literally appears. Cosmetic, and ugly for a reflex-installation demo. | `print(f"forward {tuple(map(int, a_fwd))}, …")` (or f-string the two ints) so the printed and quoted forms match. |
| 3 | Cross-ref table, line 285 | Two entries in the "Spot the kernel" row are more complete-the-square / posterior-read-off than kernel-recognition: `14:94` is "completing the square in β", `EXAM:161` is a ∝-posterior-invariance line. Both are real lines, just loosely categorized. | Optional: move `14:94` to the complete-the-square row, or swap for a truer kernel line (e.g. a Beta/Gamma read-off in M14). Not blocking. |

## Math-hat checklist

- [x] **Determinism** re-run: PASS, 1.8s, zero warnings, byte-stable.
- [x] **Kernel table & read-off rules** correct: Beta θ^{α−1}(1−θ)^{β−1}; Gamma x^{α−1}e^{−βx} (shape α, **rate** β, mean α/β = 3/5 verified); Normal exponent; Poisson λ^x/x!; Gamma-in-λ. Rate convention respected with inline comments. *(Dirichlet missing — see sev-2.)*
- [x] **Marquee Beta(10,4) off-by-one TAUGHT**: "add 1 to each exponent", a−1=9 ⇒ a=10, mean 10/14 = 0.7143 exact; kernel↔pdf agree 3.1e-13. The classic slip is explicitly drilled (also "shape − 1 gives shape 5" in Drill P1.2).
- [x] **∝-in-which-variable operationalized**: P1.1 contrasts "in θ" (binomial coeff drops) vs the data-loaded 1/3! trap (Drill P1.1); Drill P1.2 is the same-symbols-different-free-variable case (Poisson-in-x vs Gamma-in-λ). Distinction is genuinely worked, not just asserted.
- [x] **Completing the square (scalar)**: ax²−2bx = a(x−b/a)²−b²/a correct; N(0,1)×N(4,1) → a=2,b=4, mean 2, var 0.5, matches numeric product. Precision-weighted mean falls out correctly.
- [x] **Sum-of-squares decomposition** Σ(x−μ)² = n(x̄−μ)²+S: cross term vanishes (Σ(x−x̄)=0), verified to 2.3e-13; vertex x̄, floor S confirmed (5.0081/116.2375).
- [x] **EXAM:284 NIG variant** b_n = b₀+½S+½·κ₀n/κₙ·(x̄−m₀)²: **algebraically identical** to EXAM.md:284 (`bn4 = b0n + 0.5*Sxx + 0.5*k0*n4/kn*(ybar4-m0)**2`) and to M04 `nig_post` canon (`b0 + 0.5*S + (k0*n*(xbar-mu0)**2)/(2*kappa_n)`) — ½·k₀n/kₙ = k₀n/(2kₙ). Printed b_n=73.2549 reproduced by hand.
- [x] **Gamma/Beta fluency**: Γ(n)=(n−1)!, Γ(½)=√π=1.772454, B(a,b) identity 0.083333 both ways; betaln evidence 0.104895 = brute integral. **Overflow demo honest**: naive Γ·Γ/Γ → `nan`, betaln → 1.480e-302 (I verified B(500,500) from log₁₀Γ values = 10^(2·1131.39−2564.60) ≈ 10^−301.8 ✓).
- [x] **Surprising claims genuine**: λ-kernel trap real (Gamma(5,1), not Poisson); precision-weight coincidence real and correctly explained (naive 1.5 right *only because* prior prec 1/1 = data prec 4/4; σ²=1 → mean 2.4, prec 5.0).
- [x] **Wall quotes spot-checked at source** (6): 04:233 binomial-coeff-proportional ✓; 04:256 `Lg = grid**9*(1-grid)**3` ✓; 05:130 Beta read-off ✓; 05:174 "expand, collect, read off" ✓; 05:487 sufficiency/order-invariance callback ✓; 10:60 evidence-cancels-in-ratio ✓; 01:251 betaln predictive ✓; EXAM:106/226/284 ✓; booklet "Proof. Straightforward." ch08:119 ✓ (via mined-sources:51). **CB 2567 quote NOT verifiable — see sev-2.**
- [x] **Cross-ref line numbers real**: spot-checked 03:281, 07:190, 11:83, 14:94, 19:428, 21:21, 23:374, 25:69, EXAM:161/174, 15:155, 14:179 — all resolve to real, topically-relevant lines.
- [x] **Numbers contract**: every prose backtick number is printed at matching precision (one cosmetic mismatch, sev-3 above).

## Pedagogy-hat checklist

- [x] **SPEC drill-room format complete per skill**: all six skills are Reflex → Wall (cited module:line) → Fix (runnable installer) → Drill (predict-then-run, STYLE §5 format with Setup/Predict/Reason/Run/Reconcile). GATE-first ordering stated and honored (P1.1–P1.3 flagged GATE).
- [x] **Predict-first**: each skill's Drill captures a committed guess before code; the surprising-answer requirement is met (λ-trap, precision coincidence). Marquee (P1.2) predict lives in Drill P1.2 — acceptable under the prereq Fix/Drill split, though the read-off Fix itself is a straight reveal (Spine already states the answer, so nothing to "catch" there).
- [x] **Closing "Where the course uses this" table** present with real, verified cites (the section's differentiating asset holds up).
- [x] **Length/blocks/runtime bounds**: 2604 words, 8 exposition blocks, 1.8s — all within prereq bounds.
- [x] **Fluff scan**: opens "This is a drill room, not a chapter" — no banned throat-clearing; prose is dense, warranted, no padding.
- [x] **Reflex-installation tone**: fast, expert-move framing ("what an expert fires without thinking"), assumes BRIEF learner; not a probability re-teach. Pitfalls + Takeaways are reproduce-from-memory bullets. ✓
- [x] **Notation/callbacks**: N=variance, Gamma=rate honored with inline trap comments; callbacks explicit and load-bearing (P3 precision-weight, P7 log-domain, M05/M21 Kalman, SGD-vs-Bayes ML tie-in in Drill P1.3).

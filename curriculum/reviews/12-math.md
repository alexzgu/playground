# Referee report — modules/12-hmc.md (mathematics + spec)

**Verdict: APPROVE (0 sev-1, 0 sev-2, 8 sev-3 polish items).**
Harness: `PASS in 46.5s`, exit 0 with `--check-determinism`, zero warnings (byte-identical
second run; numbers contract mechanically clean). Every marquee number recomputed
independently and matched. No mathematical error found. The one authorial deviation
(0.651 stated, not swept) is **ACCEPTED** — see ruling below.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | §12.4 stability demo (L254–271) | The "ε = 2.00 → STABLE (bounded)" leg is initial-condition-specific. At exactly εω = 2 the leapfrog one-step matrix is a **defective Jordan block** (double eigenvalue −1, trace −2): I verified numerically that generic momentum p₀ = 0.5 gives *linear* growth (\|q\| ≈ 199 after 200 steps), and the demo's `peak < 1e3` verdict would still print "STABLE". It is bounded here only because p₀ = 0 kills the off-diagonal mode (period-2 orbit (1,0)→(−1,0)). Prose "Below it … bounded; above it … explodes geometrically" is correct; the demo sits *at* the boundary, which is marginal, not stable. | One clause after "Watch it": "(at exactly ε_crit the map is only marginally stable — we start it at p₀ = 0, where it oscillates with period 2; any ε below 2 is bounded for every start)". Keeps the SYLLABUS-mandated 2.00/2.01 contrast intact. |
| 3 | §12.4 (L273) | `0.651` cited (Beskos et al. 2013) without its scope words. It is an asymptotic d→∞, ε ∝ d^(−1/4), product-target result — module 10 was loudly scrupulous about exactly this for 0.234 ("asymptotic-in-d, product-target"; scope words called load-bearing). M12 should mirror one clause for symmetry. | "…is much higher, `0.651` (Beskos et al. 2013 — the same kind of asymptotic-in-d, product-target diffusion-limit result as 0.234; stated, not re-derived here)." |
| 3 | header (L7) | "**Runtime.** ~24 s" vs measured 46.5 s (block timings sum to 46.5; funnel fits alone are 25.4 s). STYLE skeleton says ⟨measured⟩. | Update to "~47 s". |
| 3 | §12.7 title/comment (L367–389) | What is implemented is the **unadjusted Langevin algorithm (ULA)** — exact full gradient, no minibatch — but the code comment and prose call it SGLD outright. The prose does say "swap the exact gradient for a mini-batch estimate and you have the algorithm", so it self-corrects, but the naming lands one paragraph early. | One sentence: "with the exact gradient this is the unadjusted Langevin algorithm; SGLD is this plus the minibatch swap below." |
| 3 | §12.7 (L389) | The 1/(1−ε/4) variance formula is asserted ("Euler–Maruyama theory") and verified by simulation, but never derived — and the derivation is two lines: θ' = (1−ε/2)θ + √ε ξ ⇒ v = (1−ε/2)²v + ε ⇒ v = ε/(ε−ε²/4) = 1/(1−ε/4). BRIEF prefers derived *and* simulated; this is the cheapest derivation in the module. | Add the one-display-line derivation. |
| 3 | §12.2 `iat()` docstring (L94) | "via the initial positive sequence" — Geyer's IPS truncates on *pairwise sums* γ₂ₖ+γ₂ₖ₊₁ going negative; this code truncates at the first negative single-lag ACF. Estimator is fine for the purpose; the name isn't. | Docstring: "truncate the ACF sum at the first negative autocorrelation". |
| 3 | §12.1 (L65) | Prose backtick `500` vs printed `500.0` — letter of the numbers contract says match printed precision (harness passes on substring only). | Print with `:.0f`, or quote `500.0`. |
| 3 | whole module | 17 runnable blocks vs STYLE §2's "4–16". Wave-wide pattern (M09: 18, M10: 21, M11: 17, M13: 18 vs Waves 1–2 all ≤16), so flagged for the orchestrator rather than this module alone. | If desired: merge block 10 (one-line 0.234/0.651 print) into block 9. |

## Deviation ruling — 0.651 stated (cited), not swept: **ACCEPTED**

The author's argument is mathematically sound. The 0.651 optimum (Beskos, Pillai,
Roberts, Sanz-Serna & Stuart 2013, *Bernoulli* — citation, year, and value verified
correct) is a d→∞ scaling-limit result under ε ∝ d^(−1/4). On a 2-D target, HMC's
ESS/iter sits ≈ 1 across the whole stable step range (the module's own run: acceptance
0.981 with exact recovery), so an empirical sweep would show a *plateau*, not an interior
optimum near 0.651 — the sweep would either mislead the reader or require d ~ 10³ runs
with careful ESS estimation, blowing the runtime budget (module already at 46.5 s).
Prose honesty: the value is presented as a cited result, never as demonstrated; the
print block prints the constant only to satisfy the numbers contract. Required polish:
add the asymptotic scope clause (sev-3 row 2) so M12 matches M10's standard of scope
honesty. SYLLABUS's "symmetry with 0.234 ✓" is satisfied — M10 (L222) explicitly
promises "≈0.651 for HMC — module 12", and M12 delivers the callback.

## Required checklist (SYLLABUS 12-hmc)

1. S1 staged donut, predict-first, d ∈ {1,10,100,1000} histogram, mode holds nothing — **PASS** (§12.1; "Commit to that answer" captures the prediction; consequence for MAP-plug-in and RW drawn explicitly).
2. RW-MH ESS vs dimension d ≤ 128, power-law fit, extrapolation, feasibility note — **PASS** (§12.2; "We can afford this only up to d=128" is the feasibility note; one figure).
3. Leapfrog from scratch on correlated 2-D Gaussian; O(ε²) check; **exact** ε_crit = 2/ω with 2.00/2.01 demo; 0.651 vs 0.234 — **PASS** (§12.3–12.4; deviation accepted above; see sev-3 marginal-stability clause).
4. Neal's funnel centered → divergences with scatter at the neck via `diverging` extra-field; LocScaleReparam non-centered; counts printed before/after — **PASS** (§12.5; `13` → `0`).
5. PPL orientation box (NumPyro course PPL + reason; PyMC labeled no-run; Stan read-only; ArviZ shared layer) — **PASS** (§12.6).
6. SGLD teaser, Euler–Maruyama in ~10 lines, stationary law, step-size bias, Lawler bridge, M25 callback — **PASS** (§12.7; see sev-3 ULA-naming + derivation rows).
7. Banana target trimmed — **PASS** (absent).

Skeleton: spine/which-line/promise/prereqs/sources header ✓; Bridge ✓; 5 Pitfalls ✓;
3 exercises in predict-then-run format with one surprising (12.2) and one ML/DL bridge
(12.3) ✓; 7 takeaways ✓; 3735 prose words (budget 2,500–5,000) ✓; 5 figures, all
referenced and discussed ✓.

## NumPyro idiom compliance (vs tools/ppl_idioms.py)

- Plate-wrapped sample sites with explicit size ✓ (funnel `x` in `numpyro.plate("D", D)`).
- Obs-as-numpy rule: vacuous (funnel has no `obs=` — it is a prior); all extracted draws cast via `np.asarray` before matplotlib ✓.
- `MCMC(NUTS(...), num_chains=2, chain_method="sequential", progress_bar=False)` ✓ exact idiom.
- `extra_fields=("diverging",)` + `int(...sum())` ✓ exact idiom; `diverging` aligned with `get_samples()` concatenation across sequential chains ✓.
- `reparam(model, config={"x": LocScaleReparam(0)})` ✓ exact idiom.
- `jax.random.PRNGKey(SEED)` ✓; all numpy randomness through `rng` ✓; no legacy `np.random.*` ✓.
- PyMC block is ```python no-run```, labeled "illustration only; does not run in this environment", API plausible (Normal(name, mu, sigma), pm.sample kwargs) ✓. ArviZ not invoked (orientation mention only) — vacuously compliant.

## Physics/honesty audit

- Hamilton's equations conserve H + preserve volume: classical theorem, warrant adjacent ✓. Leapfrog "symplectic (volume-preserving and reversible)" ✓ true. Exact-invariance credited to the Metropolis correction, not to leapfrog ✓ — the labels never claim leapfrog conserves H (§12.3 opens "Leapfrog does not conserve H exactly").
- O(ε²) presented as verified-by-fit (`2.00`), not asserted ✓. ε_crit = 2/ω stated precisely and verified numerically; "two-line eigenvalue analysis" elided but the numeric verification satisfies STYLE §6 ✓ (trace condition |2−ε²ω²| ≤ 2 confirmed independently).
- Divergence-as-mechanism narrative (curvature outruns ε → integrator unstable → energy blows up → reject → flag) is the correct account ✓.
- HMC-without-momentum-flip is valid here (K symmetric, momentum resampled each iteration) ✓. Leapfrog loop structure (½kick, L drifts, L−1 kicks, ½kick) correct ✓.
- Pitfall "centered better when data-rich" — correct folklore (Betancourt), reasonable unlabeled at pitfall altitude.

## Independent recomputations (all match)

- **Donut:** E‖θ‖ for χ_1000 = √2·Γ(500.5)/Γ(500) = **31.6149** = √(d−½); module prints `31.61` ✓. Var = d − (E‖θ‖)² = 0.4999 ⇒ sd **0.7070** ⇒ `0.71` ✓. Radial-mass peak at r = √(d−1) (maximize r^(d−1)e^(−r²/2)) ✓.
- **Empty center:** P(χ²₁₀₀₀ < 250) = 10^(−139.8) ⇒ `0.0000` from 20k draws honest ✓. Log-density gap at r = √d: r²/2 = d/2 = **500 nats exactly** ✓. Ex 12.2: P(χ²₅₀₀ < 25) = 10^(−223.7) ⇒ `0.000000` ✓, √500 = 22.36 ⇒ `22.4` ✓.
- **RW-MH:** slope −0.94 vs theoretical −1, discrepancy acknowledged ("close to the theoretical 1/d") ✓; 2^(−0.94) = 0.52 ⇒ "each doubling roughly halves" ✓; 1/4.0e-4 = 2492 ✓; 2492 × 1000 ≈ 2.5M ⇒ "two-and-a-half million" ✓; acceptance 0.239 at d=128 → 0.234 ✓.
- **Energy error:** T = 1.6 with ε ∈ {.08,.04,.02,.01,.005} gives exact integer L ∈ {20,40,80,160,320} — fixed-T fit is sound; leapfrog is order-2 symplectic ⇒ slope 2 is the true exponent; fitted `2.00` ✓.
- **Stability:** one-step matrix trace = 2 − ε²ω²; eigenvalues on unit circle iff ε ≤ 2/ω; at ε = 2.01, λ_max = 1.221 (explosive: 1.221²⁰⁰ ≈ 10^17.4, matches printed `1.16e+17` growth scale) ✓; at ε = 2.00 defective Jordan block (see finding 1). Ex 12.1: σ = 0.5 ⇒ ω = 2 ⇒ ε_crit = `1.00` ✓.
- **SGLD/ULA bias:** θ' = (1−ε/2)θ + √ε ξ ⇒ stationary v = ε/(1−(1−ε/2)²) = **1/(1−ε/4) exactly** ✓; 1.0256/1.0811/1.1429 at ε = .1/.3/.5 ✓; empirical 1.0174/1.0796/1.1376 all within MC error (ESS ≈ n·ε/4 ⇒ SE(v̂) ≈ 0.016 at ε=0.1) ✓; formula is O(ε) bias as claimed ✓. Ex 12.3 tempered: v = T/(1−ε/4) = **0.2564**, printed `0.2567` ✓; p^(1/T) Gaussian has variance T ✓.
- **Funnel semantics:** printed `13`/`0` divergences and v-ranges [−1.97, 10.79]/[−10.01, 9.44] mean what prose says (prose quotes min only: "bottoms out at `-1.97`", "down to `-10.01`") ✓; N(0, e^v) with numpyro scale e^(v/2) respects the course variance convention ✓; non-centered (v, z) is exactly jointly Gaussian ⇒ "constant curvature" claim exact ✓.
- **Callbacks:** M10 establishes 0.234, 2.38/√d, and forward-promises 0.651 to M12 (M10 L222) ✓; M11 spine "posterior correlation is the enemy" ✓; M09 ESS ✓; M16 funnel-returns promise matches SYLLABUS 16 item 2 ✓. SPINE-INDEX has no 09–13 entries yet (orchestrator's job post-wave); nothing in M12 contradicts entries 00–08.
- **Citations:** Beskos et al. 2013 (0.651) correct; Roberts–Gelman–Gilks (0.234) correct; Neal by concept ✓; `insert-bda-hmc-stan.md` and `ch15` exist in the booklet ✓; Lawler by concept ✓.

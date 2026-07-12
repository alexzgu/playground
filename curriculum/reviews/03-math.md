# Math review — modules/03-generative-stories.md

**Verdict: APPROVE.** Severity: 0 sev-1, 0 sev-2, 2 sev-3. Every derivation is
correct, every prose number is printed and reproduces on independent
recomputation, every C-B citation opens to exactly what is claimed, the scope
boundary (no exponential-family machinery) holds, and the module ends on the
M04 pointer.

## Harness / determinism

- `python tools/run_module.py modules/03-generative-stories.md --check-determinism`
  → **exit 0, PASS in 20.8s**, 3611 prose words, 14 runnable blocks, 6 figs.
- `--check-determinism` runs the blocks twice and byte-compares (`out1 != out2`
  → warning); **no WARNING lines emitted** → deterministic, numbers-contract
  clean, no banned `np.random.*` / `plt.show()`.
- Prose-stated **Runtime 15 s** vs measured **~20.8 s** (blocks 4+5 alone = 7.2+4.9 s). See F2.

## Required checklist (SYLLABUS "03-generative-stories")

| # | Required item | Status |
|---|---|---|
| 1 | Poisson process from uniform order statistics → Exp gaps, Gamma waits, Poisson counts, all verified vs scipy (KS) | ✓ §03.1; KS 0.0062 / 0.003–0.008 / mean≈var≈10 |
| 2 | CLT + Cauchy failure, predict-first; X̄ never settles; sample mean of Cauchy is Cauchy(0,1); IQR≈2 at every n; heavy-tail gallery; one-line GEV/EVT pointer | ✓ §03.2 (GEV sentence L168) |
| 3 | Info section defined once: entropy, CE, KL; KL≥0 via Jensen (2-line); worked coin numbers; forward threads ELBO(M13)/NLL(M15)/WAIC(M17) | ✓ §03.3, L236–238 |
| 4 | Max-ent: support+mean→Exp, mean+var→Normal; stated derivation + numerical grid check; least-committal framing | ✓ §03.4 |
| 5 | ML bridge: softmax = max-ent under moment constraint; temperature = Lagrange multiplier | ✓ Bridge L338 |
| 6 | Exponential-family **pointer only**; do NOT re-derive C-B ch.3 | ✓ L373, takeaway L470 |
| — | Scope boundary: NO exp-family machinery (natural params / sufficient stats / log-partition-as-cumulants) | ✓ no leakage — `logsumexp` used only as numeric normalizer; T_k framed as moment constraints |
| — | Ends on M04 pointer | ✓ "the engine of module 04" / "which is module 04" |

## Independent recomputation (all reproduce)

| Claim | Prose | Recomputed | ✓ |
|---|---|---|---|
| H(fair coin) | 1.000 bit | 1.0000 | ✓ |
| H(0.9 coin) | 0.469 bits | 0.46900 | ✓ |
| H(biased,fair) cross-ent | 1.000 bit | 1.0000 | ✓ |
| KL(biased‖fair) | 0.531 bits | 0.53100 | ✓ |
| KL(fair‖biased) | 0.737 bits | 0.73697 | ✓ |
| Cauchy IQR = 2·tan(π/4) | 2 exact | 2.0000; quartiles ±1 | ✓ |
| φ_X̄(t)=φ(t/n)ⁿ=e^{−\|t\|} | unchanged in n | correct CF argument | ✓ |
| softmax entropy T=.5/1/2 | 0.822/1.670/2.125 | 0.8222/1.6701/2.1247 | ✓ |
| uniform ceiling log₂5 | 2.322 | 2.32193 | ✓ |
| label entropy H(p) nats | 0.802 | 0.80182 | ✓ |
| CE at q=uniform nats | 1.099 | 1.09861 | ✓ |
| KL(Geometric‖Poisson) | 0.651 nats | 0.65135 | ✓ |
| mean-only max-ent on ℕ = Geometric | claimed | p_k∝e^{λk} → geometric, correct | ✓ |
| Gibbs KL≥0 via Jensen | derivation | −log convex; E_p[q/p]=Σq=1 → ≥0 | ✓ |
| max-ent dual (author deviation) | min logsumexp(θT)−θ·b | grad = E_p[T]−b=0 moment-match; p∝exp(θT) is genuine max-ent; KL to Exp/Normal = 1.3e-16/1.5e-16 | ✓ |
| Poisson thinning/superposition | Poisson(8), Poisson(0.6) | 7.998, 0.600, var/mean≈1 | ✓ |
| Cauchy median IQR ∝1/√n | 0.6597→0.0673→0.0069 | consistent 10×/100× | ✓ |
| CE floor = label entropy | 0.802 nats, not 0 | min CE at q=p = H(p) | ✓ |

C-B citations opened and confirmed: **Thm 3.8.1** = "Poisson Postulates";
**Ex 2.2.4** = Cauchy mean does not exist; **Ex 4.3.6** = ratio of two N(0,1) is
Cauchy; **Ex 5.2.10** = "If Z₁…Zₙ iid Cauchy(0,1), then Z̄ is also Cauchy(0,1)"
— verbatim match to the boxed theorem. §3.3 = Cauchy median. Notation §3
respected; bits vs nats stated at every use (L198, code comments, pitfall L381)
and internally consistent.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | §03.4, L272 vs L274 | Sign inconsistency in the two-step derivation. The stated Euler–Lagrange stationarity `−log p(x) − 1 − λ₀ − Σ_k λ_k T_k(x) = 0` solves literally to `p ∝ exp(−Σ_k λ_k T_k)`, but the boxed Step-2 result (L274) and every downstream use (Exp needs "λ<0", softmax `exp(λs)`) use `p ∝ exp(+Σ_k λ_k T_k)`. A reader who does the one line of algebra gets the opposite sign. No numeric impact (code solves for θ directly; sign is absorbed into λ_k). | Flip the sign of the moment term in the stationarity equation to `−log p(x) − 1 − λ₀ + Σ_k λ_k T_k(x) = 0`, or append "(λ_k absorbs the constraint sign)". |
| 3 | Header L6 | Stated **Runtime 15 s** understates the measured ~20.8 s (blocks 4 and 5 alone are 7.2 s + 4.9 s). STYLE §2 requires the *measured* runtime. | Update to `Runtime. ~21 s` (still well under the 120 s target). |

## Notes (non-defects)

- Labeling C-B *Example* 5.2.10 as a boxed **Theorem** is fine — it is a
  theorem-level result and the citation makes the source explicit.
- §03.1 pools only *internal* gaps (`np.diff`) and conditions waits on N≥k; with
  λT=60 the truncation of {N<5} is numerically negligible, so S_k|N≥k is
  effectively exactly Gamma(k,λ) — KS 0.003–0.008 confirms. Correct as coded.
- Repo note (not this module's defect): sources live at
  `/workspaces/playground/curriculum_material/`, one level above the path the
  BRIEF prints (`curriculum/curriculum_material/`).

# P3-precision-thread — combined referee (math + pedagogy)

**Verdict: REVISE** (1 sev-1, 1 sev-2, 4 sev-3). One sev-1 ⇒ second referee per production protocol.

Harness: `PASS in 1.9s`, 12 blocks (8 exposition + 4 exercise), **zero warnings**, determinism clean, 2668 prose words (within P3's 1,800–3,200 exception), 1 figure, pure numpy/scipy. Runtime 1.9 s ≪ 60 s.

## Findings

| sev | location | issue | fix |
|---|---|---|---|
| **1** | P3.1 "The wall" (L49) + Pitfalls (L262) | **Fabricated wall.** The prose attributes a *"module-16 combined-standard-error bug"* and cites `16-hierarchical.md:55`. But 16:55–59 is *correct* code — `prec = 1/s8**2; mu_cp = Σ(y·prec)/Σprec; se_cp = √(1/Σprec)` (precisions added properly). `grep -i bug 16-hierarchical.md` returns **nothing** — module 16 documents no SE-averaging bug at all. The real "module-16 bug" the SPEC (P7) refers to is the *uranium-indexing* bug (`u_arr[cidx]`), a different thing. A learner sent to 16:55 to "see the bug" finds correct code. This breaks the section's core contract (SPEC: "verify the quote exists"; STYLE §6: never fabricate citations). | Drop the "module-16 bug" framing. Either recast honestly — "module 16 does this correctly at `16:55` by *adding* precisions (`se_cp = √(1/Σprec)`); *averaging* the SEs would be the error" — or cite a real caught-bug location. Fix both the wall and the Pitfalls bullet. |
| **2** | P3.2 costume 5 (L115–120, L135, L141) | Partial-pooling costume uses module 16's *canonical* numbers (μ=6.49, τ=2.80) but prints "the pooled school estimate `7.2143`". SPINE-INDEX canon for the same school is **θ_A = 8.23**. Both are correct but they are *different quantities*: 7.21 is the plug-in conditional on point (μ,τ); 8.23 marginalizes τ (shrinkage is nonlinear in τ, so E[shrink(τ)]≠shrink(E[τ]) — Jensen). Because the module explicitly cross-refs `16:212`, a reader will equate 7.21 with the canonical 8.23 and be confused. | Add a half-sentence: this is the plug-in at (μ,τ)=(6.49, 2.80); the full posterior mean marginalizes τ, giving module 16's `8.23` — the gap is nonlinear shrinkage. (Strengthens the module.) |
| 3 | citations: `05:103`→actual 101; `04:186`→185/188; `EXAM:283`→282; `EXAM:682`→681 | Systematic +1/+2 line drift; every quote text is verbatim-correct at the neighboring line. Within SPEC's "lines may have drifted a few numbers" tolerance, but a batch re-sync would tidy the table + walls. | Bump the four line numbers to the exact anchor lines. |
| 3 | Marquee (L178–205) | Routes 1 & 2 are algebraically identical (`n/σ² ≡ Σ 1/σ²`); only route 3 (finite-difference curvature) is a genuinely independent computation. The "three different computations — surely they only roughly agree" framing slightly oversells routes 1–2. SPEC prescribes exactly these three, so this is design-inherent, not an author error. | Optional: tweak the naive-intuition line to target route 3 (the curvature) as the "surely only roughly agrees" surprise; keep 1–2 as the "same fact, two notations" beat. |
| 3 | P3.2 / P3.3 | The two centerpiece sections don't use the explicit **Reflex → Wall → Fix → Drill** scaffold (walls are embedded as inline citations; drills live in the exercises). Defensible for a synthesis module — P3.1 and P3.4 do carry the full scaffold — but a labeled one-line Reflex atop P3.2 and P3.3 would restore format parity. | Add a one-sentence **Reflex** header to P3.2 and P3.3. |
| 3 | (note, not a defect) | Beta-mean costume frames pseudo-counts a₀+b₀, n as "precisions" — honest (bullet L137 says "the 'precisions' are *counts*"). Spike-and-slab framed as probability-weighted cousin, clearly separated (L142–144, L338). Both correct. | — |

## Math-hat checklist

- **Determinism / harness:** PASS, zero warnings. ✓
- **Six costume reductions (algebraic):** Beta mean (pseudo-counts, honest) ✓; Normal-Normal (canonical) ✓; **ridge exact** — `(Xty/σ²)/(XtX/σ²+1/τ²)` = pw form ✓; **Kalman-gain mapping exact** — `m+K(y−m)=(mr+yP)/(P+r)=(m/P+y/r)/(1/P+1/r)` ✓; partial pooling ✓ (but see sev-2 on the *number*); spike-and-slab probability-weighted cousin, correctly & clearly separated ✓.
- **Curvature=precision, five instances:** (a) Fisher = *expected* curvature E[−ℓ″]=1/(θ(1−θ))=4.7619 ✓; (b) observed −ℓ″(θ̂)=190.48 = n·I(θ̂), expected-vs-observed distinction kept clean ✓; (c) BvM 1/√(nI)=0.0725 vs exact Beta sd 0.0705, "within a few percent at n=40" honest ✓; (d) Laplace Σ=(−∇²)⁻¹ at the mode, exact for Gaussian ✓; (e) HMC ω²=1/v=5.25=precision, ε_crit=2/ω=0.8729, ties to M12's exact 2/ω ✓ — **0.8729 consistent** with curvature 5.25 (2/√5.25). ✓
- **Three-route marquee independence:** routes 1&2 algebraically identical (sev-3); route 3 genuinely independent; all print 0.190476. Partially independent.
- **Wall quotes spot-checked (13):** 12 verbatim-real (05:101, 21:22, 04:164, 04:185, 08:80/83, 12:411, 13:127, 14:102, 16:212, 23:379, 25:66, EXAM:282/620/681); **1 broken** (16:55 — sev-1). SPINE-INDEX numbers match (I(0.3)=4.7619).

## Pedagogy-hat checklist

- Drill-room format: P3.1 & P3.4 full Reflex/Wall/Fix/Drill ✓; P3.2/P3.3 soft (sev-3).
- "Where the course uses this" table present, 5 rows, all cited ✓ (one line-drift, sev-3).
- Predict-before-reveal on the marquee ✓ (Predict + named naive intuition L180).
- Reflex-installation for the BRIEF learner, not re-derivation ✓.
- Length/blocks/runtime bounds ✓; pure numpy/scipy ✓.
- Exercises: 4× Setup/Predict/Reason/Run/Reconcile ✓; surprising one (P3.4, 1/k not ½) ✓; ML connection (P3.2 ridge/weight-decay) ✓.
- Fluff scan: claim-first openers, no banned throat-clearing, dense. ✓

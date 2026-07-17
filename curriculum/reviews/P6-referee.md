# P6-linear-algebra — combined referee (math + pedagogy)

**Verdict: APPROVE.** No sev-1, no sev-2, 3 sev-3. Determinism PASS, zero warnings, 2.7 s,
3056 prose words, 14 blocks (9 exposition + setup + figure + 3 exercise Runs), 1 figure.
All math correct; numbers contract clean; every wall quote and table reference verified at source.

## Findings

| sev | location | issue | fix |
|---|---|---|---|
| 3 | P6.5 wall, "a Schur complement of the precision (11:372)" | The cited code at 11:372 is `cvar = Sig[1,1] - Sig[1,0]**2/Sig[0,0]` — a Schur complement of the **covariance** $\Sigma$ (giving $\mathrm{Var}(Y_2\mid Y_1)$), not of the precision. The description mislabels which matrix. | Say "Schur complement of the covariance" (or "the scalar $\Sigma_{22}-\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}$, equivalently $1/\Lambda_{22}$"). Content of the citation is otherwise sound. |
| 3 | P6.4b, `print(... bool(t_solve < t_inv))` | The printed verdict is derived from wall-clock timing, i.e. latent nondeterminism inside a determinism-graded module. In practice the margin is several-fold (solve reliably wins at 1500×1500) so it prints `True` on both runs and determinism PASSed; author already excludes raw ms. Flagging the residual risk only. | Acceptable as-is given the margin; if you want zero timing dependence, key the claim on FLOP-count reasoning in prose and drop the boolean. Low priority. |
| 3 | Table + P6.7 wall, "24:164" for `ra = a - C @ np.linalg.lstsq(C, a, rcond=None)[0]` | The `ra` line is actually 24:163; 24:164 is the `rb` twin. Off-by-one line drift. | SPEC explicitly tolerates few-line drift and the quoted content exists verbatim — optional to bump to :163. |

## Math hat — checklist

- [x] Determinism `--check-determinism`: **PASS**, zero warnings, 2.7 s.
- [x] Marquee (P6.4) three routes algebraically correct; `0.0e+00` agreement genuine (routes 2/3 are the same solve-based algorithm, route 1 the inv formula — bit-identical on well-conditioned $\Sigma$). Value framed honestly as "course helper == textbook formula"; the real solve-vs-inv lesson lands in P6.4b/Ex P6.2. Matches SPEC's stated three (inv / Schur-solve / gaussian_condition), not a Monte-Carlo ground-truth check — consistent with SPEC wording.
- [x] Near-singular claims precise: residual/backward-error gap real (inv `1.4e-05` vs solve `5.6e-17` at κ=1e12); normal-equations condition-squaring κ(XᵀX)=κ(X)² demonstrated (cond(X)=1e8 → cond(XᵀX)=1e16, lstsq `1.6e-10` vs normal-eqs `6.9e-01`).
- [x] Ex P6.2 forward-error-is-conditioning-limited claim numerically true: forward err inv `2.0e-05`, solve `4.9e-05` — comparable (same order); only the *residual* separates them. Verified independently.
- [x] Cholesky: solve-via-two-triangular-solves, log|K| = 2Σ log diag(L) (factor of 2 correct: det Σ = (∏L_ii)²), MVN μ+Lz (Cov(Lz)=LLᵀ=Σ). All correct.
- [x] "when you see inv(), ask why" scoped honestly — Pitfalls bullet explicitly licenses deliberate inversion ("reporting a full covariance from a precision, once, commented"); not over-policed. Route-1 inv and P6.5 `inv(Lam)` are legitimate small-S uses.
- [x] Completing-the-square identity line-by-line correct (A symmetric ⇒ cross terms give bᵀx); posterior precision = data+prior; ridge equivalence λ=σ²/τ² matches to `0.0e+00`.
- [x] Covariance-vs-precision zeros stated the right way round: Σ_ij=0 ⇒ marginal indep; Λ_ij=0 ⇒ conditional indep given the rest (classic swap correct).
- [x] Hat matrix: trace(H)=4=#params (QR route, never forms (XᵀX)⁻¹); ridge trace 3.7022<4 = effective params; residual-maker I−H; partial correlation via double residualization (0.838→0.009). Correct.
- [x] Eigen-ellipse: axes=eigenvectors, semi-axes=√λ, 2σ semi-axes [0.894 3.347]=2√[0.2,2.8]; consistent with 21:180's √eigvalsh convention. Figure enacts it.
- [x] Jitter framing honest (1e-8·I PD insurance = tiny ridge/observation-noise; raw min-eig −3.42e-15 → raw Cholesky fails, jittered succeeds).
- [x] Six wall quotes spot-checked at source: 14:128 einsum (exact), 14:94 completing-square, 05:420 cond_cov (exact), 20:262/264 GP solve+Occam (exact), 24:163-4 residualize, 25:346 tr(Φ(ΦᵀΦ+λI)⁻¹Φᵀ) (exact), 21:203 P[0,1]=0, 21:180/185 eig ellipse, EXAM:536 broadcast, EXAM:542-544 GP block, 20:203-204 gaussian_condition, 20:159 jitter, 11:372 (see sev-3). All present.
- [x] einsum "ij,jk,ik->i" = Σ_jk D_ij M_jk D_ik = xᵢᵀM xᵢ per free row i — correct for batched xᵀΣx (and xᵀΣ⁻¹x).
- [x] Numbers contract: every prose backtick number matches printed output (spot-checked ~25).

## Pedagogy hat — checklist

- [x] Drill-room format per skill: all 9 SPEC skills get **Reflex / The wall / The fix** (P6.4's "fix" is the marquee; P6.8 fuses eigen + lstsq/normal-eqs). Wall quotes cite real module:line.
- [x] Consolidated-drills deviation acceptable: 3 predict-then-run exercises cover the load-bearing skills (batched einsum, inv-vs-solve stability, precision-vs-covariance zero); marquee carries its own predict-first.
- [x] Marquee predict-first present (P6.4 Predict a/b/c + named naive intuition + Reconcile in prose).
- [x] Closing "Where the course uses this" cross-ref table present, 8 rows, all references verified.
- [x] Length 3056 words (within 1,800–3,200), 9 exposition blocks (within 6–14), runtime 2.7 s (<60 s).
- [x] No fluff; no banned openers; Reflexes are one-sentence expert-behavior statements; callbacks load-bearing (module 05/14/20/21/24/25 named explicitly).

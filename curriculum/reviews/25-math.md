# Referee report — modules/25-deep-learning-lenses.md (mathematics)

**Verdict: REVISE** (1 × sev-2, 4 × sev-3). Harness PASS, determinism byte-identical, every marquee number independently reproduced. One exercise Reconcile contradicts its own printed output; the rest are minor.

## Harness / determinism

`python tools/run_module.py modules/25-deep-learning-lenses.md --check-determinism` → **PASS in 42.4s, zero WARNING lines**, out1 == out2 (byte-identical). 15 runnable blocks, 5 figs referenced, 5150 prose words. No plt.show, no legacy `np.random.*` (all randomness via explicitly-seeded `default_rng`), numbers-contract clean. sklearn ConvergenceWarning suppressed narrowly (scoped `catch_warnings` around each `.fit`, `ConvergenceWarning` only).

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| **2** | Ex 25.2 Reconcile (L438–440) | Prose says the net "stays reasonable near the middle of its training frequency range but drifts at the extreme contexts." The printed run says the **opposite**: at the *middle* frequency `k=20,n=40` (freq 0.5) gap = **0.1166** (large); at the *extreme* frequencies `k=0,n=40` gap 0.0244 and `k=40,n=40` gap 0.0270 (small). The net drifts MOST at the middle, LEAST at the extremes — and that middle point is exactly the one the Predict question flagged. As written the Reconcile misreports the result and defeats the predict-then-run contract (the reader who guessed "it breaks at k=20" was right, but is told the net "stays reasonable near the middle"). | Rewrite: "The net drifts *most* at the balanced long context `k=20,n=40` — gap `0.1166`, the very point the Predict flagged — while the frequency-extreme contexts (`k=0`, `k=40`) happen to land closer. An MLP fits a function on the support it saw (`n≤29`) with no guarantee off it; the Bayesian rule extrapolates by construction, the fitted approximation does not." |
| 3 | header §, prose (L7) | Stated **Runtime "~70 s"** but measured single-run is **42.4 s** (block 3 / LAB-1 training dominates at 9.3 s). Overstated (safe direction). | Change to "~45 s" (or state the measured value). |
| 3 | word count | **5150 prose words** vs BRIEF/STYLE ceiling **5,000** (deviation (a), ~3% over). Largest-mandate module (2 labs + 2 demos + ledger + §25.1 theorems + §25.6 map); STYLE says flag-don't-compress — defensible, but it does breach the hard ceiling. | Optional: trim ~150 words from §25.6 pointer prose (VAE/dropout/SGD paragraphs are the least load-bearing) to land under 5,000. |
| 3 | §25.4 (L295), code L269 | "the only approximation left is the Euler step" slightly understates: the sample gap also carries finite-particle MC error (20 000 draws) and a tiny finite-`Tmax` prior mismatch (start is exact `N(0,1)`, not `p_{T=5}`; `e^{-5}=0.0067` scale, negligible). Also the backward step `x + (x + 2*score)*dt` correctly integrates the drift `-x-2·score` *backward in time* (sign flips because `dt` decreases) — correct, but a one-word comment would forestall a sign query. | Add "(plus small Monte-Carlo error)" and a comment "# backward Euler step: drift −x−2·score, sign flipped for decreasing t". |
| 3 | §25.2 code (L94) | `ece()` labeled "module 15's reliability harness, **verbatim**" — logic is byte-identical to M15's but the `if m.sum():` body is collapsed onto one line (M15 uses a two-line body). Trivially not literally verbatim. | Either restore M15's exact formatting or soften the comment to "module 15's `ece`, unchanged." |

## Recomputation list (all independently reproduced)

- **Theorem 1 (CE = categorical MLE):** BFGS argmin of `−Σ counts·log softmax` = empirical freq `[0.40,0.35,0.25]`, max|diff| `2.35e-08`. Genuine (numerically finds the MLE, compares to counts/n). ✓
- **Theorem 2 (weight decay = Gaussian-MAP):** closed `2.963402` vs BFGS `2.963402`, diff `1.13e-07`, λ=σ²/τ²=`0.5`. The code checks analytic-shrinkage `Σy/(n+λ)` vs numerical minimizer of the *same* penalized loss (calculus half); I independently confirmed the Bayesian half — Normal-Normal posterior mean `(Σy/σ²)/(n/σ²+1/τ²) = 2.963402` equals it. Real theorem, not circular. ✓
- **LAB 1:** single ECE `0.1741`, ensemble `0.1269`; acc `0.8077`→`0.8320`; `T*=7.816` (sanity: val-NLL `1.9081`→`0.4717`, a true minimizer; the large T is an honest confession of ~8× logit inflation from adam driving 70 points to tol 1e-6), ECE→`0.0433`; single high-conf bin predicts `0.998` vs actual `0.851` (n=1769), ensemble `0.996`/`0.886`; disagreement max `0.490`, near-data `0.063`. Reliability semantics hold (high-conf bin far below diagonal). ✓
- **LAB 2 (ICL):** median|diff| `0.0279`, max `0.0825`; empty context net `0.3792` vs prior mean `0.4000`; 8/10 → `0.6882` vs Bayes `0.6667`; de Finetti k=3,n=5 empirical `0.4974` (567 contexts) vs `0.5000`. Open label + bold "Honest limits" box present. The fitted next-token predictor is a 2-feature `(k,n)` MLPClassifier; its agreement with the exact Beta-Bernoulli posterior predictive demonstrates exactly the prose claim (log-loss population minimizer = posterior predictive), no overclaim. ✓
- **Diffusion demo:** true mean/var `0.4500`/`2.8225` (hand-checked: 0.3·(−2)+0.7·1.5=0.45; Σw(v+m²)−mean²=2.8225); reverse `0.4418`/`2.8326`, left-mode frac `0.303` vs `0.300`. Forward flow `N(μₑ⁻ᵗ, ve⁻²ᵗ+(1−e⁻²ᵗ))` hand-derived (OU θ=1,σ²=2 ⇒ var 1−e⁻²ᵗ; Gaussian convolution) ✓; analytic GMM score matches central-difference to `≤6e-11` at three (x,t) ✓; forward-simulated moments at t=2 match the analytic GMM (`0.0644`/`1.028` vs `0.0609`/`1.033`) ✓; Anderson reverse drift `−X−2∇log p` correct, backward Euler step correctly implemented. Gap is discretization-honest — Euler-Maruyama on Langevin over-inflates variance (var slightly high, as M12's ULA 1/(1−ε/4) predicts). ✓
- **Double descent:** ridgeless `4615.1` at p=n=`60`, `0.641` at p=3, `0.538` at p=240; ridge peak `1.001`, `0.497` at p=240. Deviation (b) 20-D **justified**: with d=1 the ReLU feature matrix has **rank 2** for any p (columns are scalings of x±), so no interpolation threshold — 20-D is necessary for a non-degenerate exhibit (verified). M07 flat-prior tie stated honestly as partial (random-features exhibit + ridge cure exact; deep-net generalization explicitly labeled **Open**). ✓

## Deviation rulings (as requested)

- **(a) 5150 words:** technically over the 5,000 ceiling (sev-3); acceptable given the largest mandate, but trimmable. Ruled: not blocking.
- **(b) 20-D input:** JUSTIFIED and correct (1-D degenerate, rank-2 confirmed). Not a defect.
- **(c) Ex 25.1 cached-nets:** SOUND — caches 10 fits, reuses across the M sweep, deterministic; claim holds (M=10 ECE `0.1151` still > temp-scaled `0.0433`, so temperature scaling beats a ten-net ensemble). ✓
- **(d) per-demo local generators:** ALLOWED by STYLE §4.2 ("explicitly seeded local generator"); good practice — each demo is independently reproducible regardless of upstream RNG consumption. ✓

## Ledger labels (15 rows) — audited

All defensible. Theorem rows are genuine identities: weight-decay/CE (proved+verified), ℓ1-MAP (mode identity, with honest "mean never sparse" caveat), softmax-sampling temperature (`softmax(z/T)∝p^{1/T}` is an exact identity), VAE (the **ELBO identity** `log p = ELBO + KL` is exact and the "what it buys" column honestly says encoder = *approx* posterior — internally consistent, so **Theorem** is defensible with that qualifier), diffusion **Theorem/Approx** (exact given score / net approximates score — correctly split). Heuristic (label smoothing, early stopping, ensembles, MC-dropout, SGD-noise) and Open (ICL, cold posteriors) rows correctly labeled. No misclassification.

## Required checklist

- [x] Determinism re-run PASS, zero warnings, byte-identical
- [x] All prose numbers (≥6 spot-checked, in fact all marquee numbers) ⊆ printed output
- [x] Both §25.1 theorem checks real (not circular) — independently confirmed
- [x] LAB 1 ECE arithmetic + T* fit sane; reliability semantics hold
- [x] LAB 2 construction demonstrates the stated claim; Open label + honest-limits box present
- [x] Diffusion forward flow / analytic score / reverse SDE all independently verified; gap discretization-honest
- [x] Double descent reproduced; 1-D degeneracy confirmed; M07 tie honest/partial
- [x] Ledger labels honest (15 rows)
- [x] Scope discipline: only 2 labs + 2 demos + §25.1 theorem checks run; §25.6 is prose + one `no-run` block; "map, not territory" labels present
- [x] Convergence warnings suppressed narrowly
- [x] Notation §3 respected (N(·,·)=variance, KL(q‖p), Beta(a,b))
- [x] Citations by concept, none fabricated (Gal–Ghahramani, Xie, Song, Nakkiran, Anderson, Guo, Lakshminarayanan)
- [x] SPINE-INDEX callbacks accurate (M13 ELBO, M15 ece reuse, M12 ULA/SGLD, M18 power posterior η=1/T, M07 nonidentifiability/improper prior, M14 λ=σ²/τ², M01 de Finetti, M03 softmax temperature)
- [ ] **Ex 25.2 Reconcile factually correct** — FAILS (sev-2 above)

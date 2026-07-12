# FINAL fresh-read B — modules 07, 16, 25

Cold full-text read. Every figure opened and checked against prose; all headline
numbers spot-verified by hand where tractable. Modules are dense and clean; the
one substantive defect is a silent indexing bug in the radon demo.

| sev | module:line | issue | fix |
|---|---|---|---|
| 2 | 16:373 | No-pooling residual uses `u_arr[cidx]`, but `u_arr = df["u"]` is already **per-home** (length ≈ total homes ~600) while `cidx` holds **county ids 0–39**. So `u_arr[cidx]` reads the uranium of the *first 40 homes* in the frame, not each county's uranium. Runs without error (all indices valid), silently miscomputes `resid` → every county's blue "no-pooling" point in `radon.png` is shifted by a county-specific constant `g1·(u[c] − u_arr[c])`. The code contradicts its own comment (line 372: "mean residual from the fixed-effects trend, per county"). | Use `u_arr` directly (already per-home) or `u[cidx]` (per-county array from line 321 indexed by home's county): `resid = y_arr - (g0 + g1 * u_arr + beta * floor_arr)`. |
| 3 | 07:192 vs 195,203 | Naming mismatch: prose names the two invariance checks "**Route A**" / "**Route B**", but the code comments label them "`# Route 1:`" and "`# Route 2:`". A reader mapping prose→code must silently translate A↔1, B↔2. | Rename code comments to "Route A" / "Route B" to match §07.4 prose. |

## Per-module verdicts

- **07-priors** — CLEAN. All 6 figures match prose; hand-checked the load-bearing
  numbers (fan spread 0.30 = ½·0.60; logistic ratio 0.25/0.0452 = 5.53; Haldane
  log-divergence step ≈4.6/two-decades; nonidentif. sd(θ₁)=2.2416→2.2361, sd(sum)=0.01).
  Predict/Reconcile pairs all resolve their own question. Only nit: Route A/B vs 1/2 (sev 3).
- **16-hierarchical** — one real bug (radon `u_arr[cidx]`, sev 2). Everything else verified:
  θ_A 28→8.23, τ=0 check 7.69·0.0603/0.0703≈6.6, bake-off 2.019/1.978/1.691 & λ*=0.5,
  EB 27% too narrow (1−15.96/21.89), mixed-LM corr 1.000, funnel 86→0 div. Figures all match.
- **25-deep-learning-lenses** — CLEAN. All 5 figures match; verified CE=2.35e-8, MAP λ=0.5,
  ECE 0.1741→0.1269/0.0433, T*=7.816, ICL empty-ctx 0.3792→0.4, diffusion mean 0.4418/var
  2.8326, double-descent spike 4615.1 at p=n. Ledger has all 15 rows; every exercise
  reconcile resolves its Predict.

Counts: sev1 = 0 · sev2 = 1 · sev3 = 1.

Worst finding — **16:373**: the radon no-pooling baseline is computed against the wrong
per-home uranium term, silently distorting the blue points (and the shrinkage arrows) in
`radon.png`. No crash, no referee-visible symptom; the narrative point survives but the
figure is quantitatively wrong.

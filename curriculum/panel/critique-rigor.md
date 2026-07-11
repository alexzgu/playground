# Rigor & Technical-Correctness Audit — OUTLINE-draft.md

Lens: mathematical rigor / technical correctness of the *planned* content. Every formula, example, and
simulation named in the draft was checked; where cheap I verified numerically (scripts run under
`numpy/scipy/sklearn`, seeds fixed). Verdicts marked ✓ are vetted — authors can build on them as-is.

Counts: **3 severity-1, 8 severity-2, 13 severity-3** substantive findings, plus ~25 formulas confirmed ✓.

---

## 1. Findings table

Severity 1 = must fix (wrong/contradicts its own demo); 2 = should fix (imprecise/overstated/fragile);
3 = polish. ✓ rows = checked and correct.

| Sev | Module | Issue | Concrete fix (exact statement/formula/example) |
|---|---|---|---|
| **1** | 09 | ESS heuristic written "ESS = n/(1+var of normalized weights)" is **wrong**: normalized weights sum to 1, so their variance → 0 and the formula returns ≈ n always (I ran it: gives 100000 for n=100000). | Use the Kong (1994) identity: `ESS = (Σwᵢ)² / Σwᵢ² = 1/Σ w̄ᵢ²` (w̄ = normalized). Equivalently `ESS = n/(1+cv²)` where **cv² = Var(w)/mean(w)² of the _un_normalized weights**. (If you must phrase it via normalized weights: `n/(1 + n²·Var(w̄))`.) Verified: Kong = n/(1+cv²) = 1/Σw̄² all agree (50004 for exp weights, n=1e5). |
| **1** | 18 | "E[#clusters] ≈ α log n **verified**" — the code will *fail to verify* for α≠1. Exact vs α·ln n: α=5,n=100 → **15.7 vs 23.0** (46% off); α=2,n=100 → 8.4 vs 9.2; even α=1,n=100 → 5.19 vs 4.61 (12% off). | State/verify the **exact** mean: `E[Kₙ] = Σᵢ₌₁ⁿ α/(α+i−1) = α[ψ(α+n)−ψ(α)]` (ψ = digamma). Asymptotics: `α ln(1+n/α)` (matches to <1% at all α,n I tried) — and `≈ α ln n` **only when n ≫ α**. Simulate CRP, overlay the digamma curve, not α ln n. |
| **1** | 10 | Plan shows "the 0.234 lore" via a step-size sweep on a **1-D bimodal target**. 0.234 is a **d→∞** result; in 1-D the ESS-optimal acceptance is **≈0.44**, so the demo prints ~0.44 and contradicts the prose. Verified: 1-D best ESS at accept **0.446**; d=50 best ESS at accept **0.235**. | Run the acceptance-vs-ESS sweep on a **high-dim iid product target (d≈50–100)**; there it lands on 0.234 with optimal step `≈ 2.38/√d` (Roberts–Gelman–Gilks 1997). Keep the 1-D bimodal target *only* for the mode-hopping-failure demo. State 0.234 as the asymptotic product-target optimum, and note 1-D ≈ 0.44. |
| 2 | 15 | "Ng–Jordan crossover simulated: NB wins small-n, logistic wins large-n." **Fragile — I could not reproduce the stated ordering.** Well-specified NB (cond-indep Gaussian) gave the *opposite* (LR better at n=15,30; NB better after). Equicorrelated (mildly misspecified) NB → NB better at *every* n, gap 0.050→0.002. LR never overtook. | Don't promise a clean crossover. Robust, always-visible claim: *"generative (NB) reaches its asymptote in ~O(log d) samples so it wins at small n; discriminative (LR) has equal-or-lower asymptotic error and the gap shrinks with n."* To *force* LR to overtake you need NB **clearly** misspecified **and** (near-)unpenalized LR whose asymptotic error is provably lower — and even then it's delicate on synthetic Gaussian data. Consider framing as "gap shrinks / can reverse," not "logistic wins." |
| 2 | 22 | "p-value error rates inflate 3–4×" under optional stopping — magnitude depends entirely on #looks, unstated. Verified (nominal 0.05): 5 looks→0.13 (2.6×), 10 looks→0.20 (3.9×), **continuous monitoring to N=1000→0.46 (9×)**, →1 as N→∞ (law of iterated logarithm). | Specify the design: "3–4×" ≈ **~10 interim analyses**. If the demo does per-observation monitoring, report the much larger inflation (~9× here) and cite the LIL — don't call it 3–4×. |
| 2 | 22 | "posterior remains valid under optional stopping … what is compromised for the Bayesian: calibration under selective reporting" — conflates **optional stopping** with **selective reporting**. | Separate three claims: (a) the **posterior is unchanged** (likelihood ignores a θ-independent stopping rule) — preserved; (b) **prior-averaged Bayesian calibration is also preserved** under optional stopping (posterior is a martingale) — stopping alone does *not* break it; (c) what breaks: **frequentist** Type-I/coverage at fixed θ, and — separately — **selective reporting** (publish-if-significant) breaks calibration for *both* paradigms. The genuine Bayesian caveat is "sampling to a foregone conclusion" for **point-null Bayes factors with diffuse alternatives**, not credible intervals. |
| 2 | 06 | "credible intervals have exact coverage under a well-specified prior" — must name the sense. | Say **prior-averaged (Bayesian) coverage** is exactly 1−α: `∫ Cov(θ)π(θ)dθ = 1−α`. It is **not** per-θ frequentist coverage. Verified (Normal-Normal, τ=2): prior-averaged **0.9503**, but per-θ = **0.971 at θ=0**, **0.883 at θ=4**. Misspecified prior (true τ=5, model τ=2) → prior-averaged drops to **0.828** — exactly the "graceful degradation" the module promises. Use these numbers. |
| 2 | 09 | ESS-for-MCMC trap: the booklet you supersede prints "**ESS ≥ n**" (ch04 l.116) — backwards. | Ensure the module-10 autocorrelation ESS uses `ESS = n / (1 + 2Σ_{k≥1} ρ_k) ≤ n`. Flag the booklet error explicitly if you cite it. |
| 2 | 05 | "predictive is **always** wider than plug-in (law of total variance)" — not a universal theorem. `Var(ỹ)=E[Var(y|θ)]+Var(E[y|θ])`; the first term vs `Var(y|θ̂)` carries a Jensen sign that can go either way when Var(y|θ) depends on θ. | State it as the **decomposition** (epistemic + aleatoric) and claim strict widening only where it holds: fixed-dispersion families and **all** the module's conjugate cases. Verified wider: Beta-Binomial 4.69 vs 2.34; Gamma-Poisson 3.0 vs 2.0. Say "in these families," not "always." |
| 2 | 08 | BvM "stated with regularity caveats" — make the caveats explicit or it's hand-waving. | Required conditions: well-specified model, **fixed finite-dim identifiable** θ, true θ **interior** (not on boundary), prior density positive & continuous near θ₀, LAN/consistency. Fails for: nonparametric/growing-dim params, **boundary** params (e.g. U(0,θ)), unidentified params, **misspecification** (posterior still concentrates but at the KL-projection with the *wrong* "sandwich" variance ⇒ credible ≠ confidence). |
| 2 | 07 | "improper-prior failure case (posterior fails to normalize)" — pick an example that *actually* fails; a flat prior on a Normal mean gives a **proper** posterior. | Cleanest genuine failures: **Beta(0,0)** (Haldane) prior with all-successes/all-failures data → posterior ∝ θ⁻¹ improper; or hierarchical `π(σ)∝1/σ` → improper posterior at σ=0 (booklet ch15 flags exactly this). Give the divergent integral. |
| 3 | 10 | R̂ "checked against ArviZ" — ArviZ 1.2 `az.rhat` defaults to **rank-normalized split-R̂** (Vehtari et al. 2021), not classic split-R̂. | Compute rank-normalized split-R̂ by hand (rank→normal-score→split→classic formula) so the by-hand value matches ArviZ; or note the small expected discrepancy. Mention rank-R̂ is the modern default and is robust to heavy tails where classic R̂ can be undefined. |
| 3 | 13 | "ELBO = log evidence − KL(q‖p)" — the p here is the **posterior** p(z\|x), not the prior. | Write `log p(x) = ELBO + KL(q(z) ‖ p(z|x))`, so `ELBO = log p(x) − KL(q ‖ p(·|x))`. |
| 3 | 13 | "EM = VI with point-mass q over parameters" — correct, but easy to misread. | Keep it; add: the delta mass is on the **parameters** θ (MAP/ML), while the q over **latent z is the _exact_ conditional** p(z\|x,θ) (E-step), *not* a point mass. That asymmetry is the whole reduction. |
| 3 | 13 | Laplace on a Beta posterior "bad at n=5" — on the raw [0,1] scale a Gaussian is guaranteed poor (support mismatch), which overstates Laplace's weakness. | Do Laplace on the **unconstrained logit scale** (standard practice), transform back. The "bad at small n" point survives; the KL numbers become fair. |
| 3 | 07 | Jeffreys derived only for 1-param Bernoulli — fine, but state the scope. | Add one line: multiparameter Jeffreys = `√det I(θ)`; **often not recommended as-is** (Jeffreys' own Normal(μ,σ) example gives σ⁻² but he preferred the independence prior σ⁻¹); reference priors (Bernardo) resolve this. Keeps you honest about "Jeffreys for invariance." |
| 3 | 17 | "evidence peaks at true polynomial degree while train MSE falls" — for a *single* dataset the evidence peak is noisy, and with improper/vague coefficient priors the marginal likelihood is ill-defined / Lindley-prone. | Use **proper** coefficient priors (fixed prior variance), moderate SNR, and either a clear-signal dataset or average over a few draws so the peak is visibly at the true degree. |
| 3 | 11 | "convergence rate ↔ posterior correlation" — quantify it. | For the bivariate Normal, Gibbs lag-1 autocorrelation is **exactly ρ²** (verified: ρ=.9→0.808, ρ=.99→0.980), so ESS fraction ≈ (1−ρ²)/(1+ρ²) (≈0.01 at ρ=.99). Use ρ² as the geometric rate in the ρ-sweep plot. |
| 3 | 15 | "posterior predictive class prob ≠ plug-in σ(x·ŵ) — integrate" — give the closed form for the check. | MacKay's moderated-probit approximation: `∫σ(xᵀw)N(w;μ,Σ)dw ≈ σ(xᵀμ / √(1+ (π/8) xᵀΣx))`. Pulls probabilities toward 0.5; makes "integrate don't plug" a one-line quantitative check near the boundary. |
| 3 | 12 | Dimension-scaling shootout "RW-MH ESS vs dimension d=1…1000" — running MH to usable ESS at d=1000 is slow on 2 CPUs. | Measure the power law at **d ≤ ~128** (plenty to fit slope −1) and extrapolate; the donut/typical-set norm demo can still go to d=1000 (it's just sampling normals). |
| 3 | 23 | "conformal prediction … coverage without a model" — qualify the guarantee. | Split/inductive conformal gives **finite-sample, distribution-free, _marginal_** coverage `P(Y∈C(X))≥1−α` under **exchangeability** (not iid-specific). It does **not** give conditional coverage given X=x (impossible distribution-free), and breaks under distribution shift. Say "marginal coverage under exchangeability." |
| 3 | 12 | "HMC … momentum + gradient" — optionally state HMC's optimal acceptance to parallel the 0.234 story. | HMC optimal acceptance **≈0.651** (Beskos et al. 2013; the BDA insert says "≈65%"). Nice symmetry with module 10's 0.234. |
| 3 | 04 | "ancillarity teaser" — anchor it. | Concrete Basu instance for the module: for N(θ,1), the complete sufficient x̄ ⊥ the ancillary (x_i−x̄) — a clean, simulable independence. |
| 3 | 08 | Cramér–Rao "verified numerically" — state the bound with its regularity proviso. | `Var(T) ≥ [τ′(θ)]²/(nI(θ))` for unbiased T of τ(θ), **support not depending on θ** (else U(0,θ) "beats" it). Equality ⇔ efficient (e.g. x̄ for Normal). |

### Verified correct ✓ (build on these as-is)

| Module | Confirmed |
|---|---|
| 02 | PPV = **1.943% ≈ 1.9%** (sens .99/spec .95/prev .001) ✓. German-tank UMVU `N̂=m(1+1/n)−1` unbiased (sim mean 1000.2) ✓. Odds form, sequential=batch ✓. |
| 03 | Cauchy sample mean **does not concentrate** (stays Cauchy(0,1), IQR≈2 for all n) ✓. Log-partition `A′=E[T], A″=Var[T]` (Poisson: 3.7/3.696) ✓. Max-ent exp/normal, Poisson-process order-stat construction ✓. |
| 04 | Stopping-rule p-values **0.073 (binomial P(X≥9))** and **0.033 (negbin P(Y≥9), r=3)** — exact to 3 dp ✓. Identical likelihood ∝θ⁹(1−θ)³, identical posterior ✓. |
| 05 | **NIG posterior-predictive is Student-t** with `df=2αₙ, loc=mₙ, scale²=bₙ(κₙ+1)/(αₙκₙ)` — MC matches closed form (mean/var/quantiles) ✓. Precision-weighted mean, Gamma-Poisson→NegBin, Dirichlet-mult add-α ✓. |
| 06 | L2→mean, L1→median, 0-1→mode ✓. **Lasso = Laplace-MAP is a mode** that hits exactly 0 (y=.3,.8→0), posterior **mean never sparse** (0.14, 0.39) — subtlety correctly flagged ✓. Ridge=Gaussian-MAP (mode=mean) ✓. **Two-point uniform CI (X₁,X₂~U(θ−½,θ+½), n=2)**: marginal coverage **0.500**, this *is* the Welch/Berger–Wolpert example and n=2 is the cleanest — **answers open-Q4: keep it** (see §2.1). |
| 07 | Jeffreys Bernoulli = **Beta(½,½)** from √I(θ)∝θ^−½(1−θ)^−½; invariance under logit reparam ✓. |
| 08 | **James–Stein dominates MLE for d≥3** (d=10,‖θ‖=0: MLE 10.0, JS 2.0, JS⁺ 1.26; dominates at all ‖θ‖ tested) ✓. EB derivation `δ=(1−(d−2)/‖X‖²)X` from θ~N(0,τ²) ✓. Bayesian bootstrap = Dirichlet(1,…,1) weights ✓. Complete-class hedge "(a limit of) Bayes" ✓. |
| 10 | Detailed balance ⇒ stationarity (sufficient, not necessary); MH satisfies DB ✓. |
| 11 | Gibbs = componentwise MH with acceptance 1 ✓. Albert–Chib probit truncated-normal augmentation ✓. |
| 12 | Typical set: `‖X‖→√d` for N(0,I_d) ✓. **Leapfrog linear-stability boundary ε_crit=2/ω exact** (N(0,1): ε=2.00 stable, ε=2.01 explodes) ✓. Leapfrog volume-preserving, energy error O(ε²) bounded ✓. |
| 13 | Mean-field Gaussian **underdispersion factor = (1−ρ²)** exact ✓. |
| 17 | **Lindley**: n=10⁴, two-sided p=0.01 (x̄=0.0258) → BF favors H₀ for all priors (BF₀₁ = 1.8, 3.6, 7.3, 18 as τ=0.5→5) ✓. Occam-factor = prior-predictive density ✓. |
| 19 | **GP posterior mean = kernel ridge** with λ=σ_n² — identical to machine precision ✓. NNGP wide-net→GP ✓. |
| 20 | Kalman = recursive Normal-Normal (predict=marginalize, update=condition), gain = shrinkage weight ✓. |
| 21 | Bayes rule minimizes posterior expected loss; Thompson = posterior probability-matching ✓. |
| 23 | Weight decay = Gaussian-prior MAP; cross-entropy = categorical MLE ✓. |

---

## 2. Five high-rigor additions worth their space

**2.1 Exact conditional coverage of the two-point uniform CI (module 06).** Beyond "marginal 50%,"
give the ancillary-conditioned function: with R=|X₁−X₂|, the interval [X₍₁₎,X₍₂₎] has
`Cov(θ | R=r) = r/(1−r) for r<½, and = 1 for r≥½`. Verified: cond. coverage **1.000 when R>½**
(25% of samples), **0.333 averaged over R<½**, and θ is *always* in [max−½, min+½]. Earns its place: it
turns a slogan ("conditioning matters") into an exact, simulable curve and cleanly answers open-Q4 — no
need for Jaynes' truncated-exponential.

**2.2 Prior-averaged coverage as a theorem, with the pointwise foil (modules 06/08).**
`∫Cov(θ)π(θ)dθ = 1−α` exactly under the correct prior (verified 0.9503), while pointwise coverage is
0.97/0.88 and *misspecified* prior gives 0.83. This is the rigorous content behind "credible ≈ confidence"
and the honest boundary of it — the single most clarifying demo for the frequentist/Bayesian bridge.

**2.3 The optimal-scaling law, stated properly (modules 10 & 12).** Not just "0.234 lore": RWM on a
d-product target has ESS-optimal step `ℓ*/√d` with ℓ*≈2.38 and acceptance→**0.234** (d→∞); 1-D optimum
**≈0.44**; **HMC optimum ≈0.651**. Verified both endpoints (1-D accept 0.446, d=50 accept 0.235 at peak
ESS). Earns its place: it is a genuine theorem with a memorable constant and it repairs the sev-1 demo.

**2.4 Leapfrog linear-stability threshold (module 12).** For a Gaussian target of curvature ω²,
leapfrog is stable iff `ε < 2/ω`; past it, energy diverges geometrically and every proposal is rejected
(the mechanism behind "divergences = geometry warnings"). Verified exact at ε_crit=2 for N(0,1). A crisp,
falsifiable number to anchor the step-size/divergence discussion.

**2.5 MacKay's moderated predictive for Bayesian logistic regression (module 15).**
`P(y=1|x,D) = ∫σ(xᵀw)p(w|D)dw ≈ σ(xᵀμ/√(1+(π/8)xᵀΣx))`. Turns "integrate, don't plug σ(x·ŵ)" into a
closed form whose gap from the plug-in is largest near the boundary and at small n — exactly where the
module wants to quantify it, and cheap to verify against MC.

---

## 3. Demos that are infeasible or will underwhelm — with fixes

- **Ng–Jordan crossover (15)** — *likely visually unconvincing.* My two synthetic attempts did **not**
  show discriminative overtaking generative (see sev-2 row). A from-scratch, CPU-cheap Gaussian demo that
  cleanly reverses is genuinely hard. Fix: reframe as "generative wins small-n, gap shrinks" and only claim
  a crossover if you engineer strong NB misspecification + unpenalized LR and *show* the measured curves;
  otherwise soften the promise.
- **0.234 on a 1-D target (10)** — *contradicts its own number* (prints ~0.44). Fix in sev-1 row: move the
  acceptance sweep to d≈50–100.
- **CRP "verify E[K]≈α log n" (18)** — *verification will fail for α≠1.* Fix: verify the digamma form.
- **Dimension-scaling MH shootout to d=1000 (12)** — *runtime risk on 2 CPUs.* Cap RW-MH at d≤128, extrapolate.
- **Polynomial-degree evidence peak (17)** — *noisy for one dataset.* Use proper priors + clear SNR, or average.
- **Laplace-on-Beta KL at n=5 (13)** — *unfairly bad on raw scale.* Do it on the logit scale.

Feasibility of the heavy MCMC/PyMC demos (eight-schools, funnel non-centered fix, probit Gibbs,
truncated-DP, particle filter, ADVI-vs-NUTS) is fine at the sizes implied — all comfortably under 180 s if
draws are kept to a few thousand × 4 chains.

# Math review — modules/13-laplace-em-vi.md

**Verdict: APPROVE.** Determinism harness PASS (exit 0, 28.8 s, 16 blocks, 6 figs, 4592 words), zero warnings on a fresh single run. Every prose backtick-number independently reproduced; all derivations recomputed and correct. No sev-1 / sev-2 findings.

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | header line 6 | `Runtime. ~40 s` overstates the measured 28.8 s (STYLE §2 wants the *measured* value). JAX-JIT variance makes a conservative estimate defensible, but 40 is ~40% high. | change to `~30 s` (or the measured 28.8). |
| 3 | §13.5 line 382 | The reported sd ratio `0.8944` is in fact *exactly* $\sqrt{(a_n-1)/a_n}=\sqrt{0.8}$ (verified 0.79999999999999). Module reports it only as an empirical number — correct and honest, but a clean closed form is available. | optional: note "$=\sqrt{(a_n-1)/a_n}$, the Gaussian-vs-$t$ variance ratio" to convert a magic number into a law. Not required. |
| 3 | §13.6 fig / SYLLABUS §13 item 6 | Spec asked for a "wall-clock vs accuracy **table**"; delivered as an annotated bar figure. | none needed — see deviation ruling (a). Keep as-is; the accuracy half is fully tabulated in the print block. |

## Deviation rulings (all three requested — all UPHELD)

**(a) Wall-clock as figure, not printed table — SOUND.** Printed timings vary run-to-run and would fail the byte-identical determinism gate (STYLE §8.2). The prose quotes no second-count in backticks (only "a fraction of NUTS's time", "an order of magnitude faster"), so the numbers contract is not triggered. Rendering timings into a figure (figures aren't text-diffed) is the correct engineering call. Accept.

**(b) Ex 13.4 uses CAVI sweeps (2 vs 10 000), not SVI steps — FAIR, and pedagogically stronger.** SGD/Adam steps carry non-reproducible stochastic-gradient noise; CAVI sweeps give the *bit-identical* `0.1900 → 0.1900`, which is a cleaner proof that under-dispersion is the exact reverse-KL optimum, not an optimization artifact. The exercise correctly extends the lesson to SVI verbally ("more Adam steps polish the wrong optimum"). Accept.

**(c) Raw-Laplace unfairness quantified by boundary mass `0.1318`, not raw-scale KL — CORRECT.** A Gaussian on $\theta\in\mathbb{R}$ has support not contained in the Beta's $[0,1]$; $\mathrm{KL}(q\|\text{Beta})$ therefore has $\log(q/0)=+\infty$ on $(-\infty,0)\cup(1,\infty)$ and is genuinely infinite/ill-defined. Boundary mass is the well-defined substitute. Accept.

## Required checklist

- [x] Harness `--check-determinism` PASS, exit 0, zero warnings (28.8 s, budget 300 s).
- [x] ELBO identity **as written**: $\log p(x)=\mathrm{ELBO}(q)+\mathrm{KL}(q\|p(\cdot\mid x))$, KL to the **posterior**. Both derivations (insert $p(x,\theta)/p(\theta\mid x)=p(x)$ then split; Jensen with slack = KL) step-correct. Grid check: $\log p(x)=-2.3979$ constant across all three $q$ — independently reproduced ($p(x)=\binom{10}{7}B(8,4)=1/11=0.0909$, $\log=-2.39790$). ✓
- [x] Logit-Laplace: mode $=\alpha/(\alpha+\beta)$, variance $(\alpha+\beta)/(\alpha\beta)$ in $\phi$ re-derived (Jacobian $\theta(1-\theta)$ folded in correctly); $n{=}5$ KL 0.0264, $n{=}200$ KL 0.0022, ratio 11.8×; raw $P(\theta<0)=0.1318$. All reproduced. ✓
- [x] Laplace evidence: $\log p(x)\approx\log p(x,\theta^\star)+\tfrac{d}{2}\log2\pi-\tfrac12\log|H|$; $d=1$, $2\pi$ factor, and $H=a_nb_n/(a_n+b_n)$ (negative Hessian in $\phi$) all correct. −4.6182 vs exact −4.6151, both −4.62. ✓
- [x] EM: monotonicity argument correct (E-step zeroes $\mathrm{KL}(q(z)\|p(z\mid x,\mu))$ ⟹ ELBO $=\log p(x\mid\mu)$; M-step raises ELBO ⟹ incomplete-data loglik climbs); E/M steps for known-variance mixture correct; reduction wording **matches the panel verbatim** — point mass on $\theta$, **exact** conditional on $z$, "the asymmetry is the point." ✓
- [x] CAVI correlated Gaussian: mean-field fixed point $q_j$ mean $=-\Lambda_{jj}^{-1}\sum_{k\ne j}\Lambda_{jk}E[\theta_k]$, variance $1/\Lambda_{jj}$; $\Lambda_{jj}=1/(1-\rho^2)$ ⟹ marginal variance $=1-\rho^2$ **exactly** (0.36 at ρ=0.8, 0.19 at ρ=0.9). KL(q‖p)=0.5108. Reproduced. ✓
- [x] CAVI-NIG vs M05: parameterization matches `nig_post` exactly ($k_n,m_n,a_n,b_n$); exact marginal sd $=\sqrt{b_n/(k_n(a_n-1))}=1.0060$, CAVI sd 0.8998, ratio 0.8944, df $=2a_n=10$. "sd 0.8998 vs 1.0060 semantics" honest (Gaussian-conditions-on-$E[1/\sigma^2]$ vs heavy-$t$-integrates). ✓
- [x] Ex 13.1 reverse-KL mode collapse: reverse-KL global opt $m{=}4.000,\ \mathrm{sd}{=}1.001,\ \mathrm{KL}=\ln 2=0.693$ (verified $=\ln 2$); forward KL $m{=}0,\ \mathrm{sd}=\sqrt{17}=4.123$; local opt at centered init KL 1.851 — all reproduced. ✓
- [x] SVI/AutoNormal semantics: prose is **honest** — explicitly states AutoNormal is mean-field Gaussian in the *unconstrained* space and "reports Gaussian tails in the unconstrained space." sd(σ) ratio 0.700, tail clip 2.282 vs 2.366. ✓
- [x] NumPyro idioms match `tools/ppl_idioms.py` (MCMC/NUTS args, `chain_method="sequential"`, `progress_bar=False`, PRNGKey seeding, AutoNormal+SVI+Adam+Trace_ELBO, `guide.sample_posterior`, obs kept as numpy). ✓
- [x] Notation §3: $N(\mu,\sigma^2)$=variance, KL(q‖p) order, IG convention all respected. ✓
- [x] Citations honest: Laplace 1774, Dempster–Laird–Rubin 1977, variational 1990s, Bishop/BDA3 by concept — no fabricated page numbers. ✓
- [x] SPINE-INDEX / callbacks: M03 KL vocabulary — M03 (lines 236, 381) *does* flag "mode-covering vs mode-seeking (M13)", so the §13.4/Ex13.1 callback is accurate. M05 NIG parameterization matches. M25 VAE forward promise consistent. ✓
- [x] Structure: 12 exposition blocks (4 exercise Run blocks exempt) within the 4–16 cap; 4592 words within 2500–5000; 6 figures all referenced+discussed; predict-then-run staging present in §13.2/13.4/13.6 and all 4 exercises. ✓
- [x] Numbers-contract spot-check (≥6): 13 prose numbers cross-checked against printed output — all match to quoted precision. ✓

## Independent recomputation list

Recomputed from scratch (scipy/numpy, separate script) and matched module output exactly:
1. Evidence $\log p(x)=-2.3979$ two ways ($\binom{n}{s}B(a_n,b_n)/B(a_0,b_0)$ and grid); ELBO+KL sums.
2. Logit-Laplace mode/variance closed forms + KL at $n\in\{5,200\}$ + ratio 11.8; raw curvature $(a{-}1)/\theta^2+(b{-}1)/(1{-}\theta)^2=31.25$ ⟹ var 0.032 ⟹ $P(\theta<0)=0.1318$.
3. Laplace vs exact evidence at $n{=}100$: $-4.6182$ vs $-4.6151$; verified $H=a_nb_n/(a_n+b_n)$ is the $\phi$-space negative Hessian.
4. CAVI marginal variance $=1-\rho^2$ at ρ∈{0.8,0.9,0.95,0.99}; KL(q‖p)=0.5108.
5. NIG exact sd $=\sqrt{b_n/(k_n(a_n-1))}=1.0060$, ratio 0.8944 $=\sqrt{0.8}=\sqrt{(a_n-1)/a_n}$, df 10.
6. Ex 13.1 reverse/forward KL optima; KL $=\ln 2$ and sd $=\sqrt{17}$ confirmed.
7. Ex 13.3 evidence/Occam: M1 0.2051, M2 0.0909, BF 2.256.

Verification script: `/tmp/claude-1000/-workspaces-playground/e87d4e91-9dd6-4c29-a8fb-8499c92a28cf/scratchpad/verify13.py`.

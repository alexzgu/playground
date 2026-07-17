# Mined micro-skills: modules 14–26 + EXAM

Silently-used mathematical/computational moves the text USES WITHOUT TEACHING. The prereq section will teach exactly these. Each row: skill · module:approx-line · the exact step where it is silently used (≤1 line) · what a reader missing the skill experiences.

## Instance table

| skill | module:line | quoted step | what-breaks-without-it |
|---|---|---|---|
| kernel-recognition | 14:94 | "The log-posterior is a sum of two quadratics in β" | Cannot see the posterior is Gaussian; treats it as an opaque product |
| complete-the-square-matrix | 14:94 | "completing the square (expand and collect …) gives Σ_n=(…)⁻¹, μ_n=Σ_n·X⊤y/σ²" | Cannot derive posterior mean/covariance from the two quadratics |
| precision-weighted-mean | 14:96 | "Posterior precision = prior precision + data precision X⊤X/σ²" | Misses shrinkage structure; sees formula as arbitrary |
| precision-vs-covariance | 14:102 | "np.linalg.inv(X.T @ X / sigma2 + np.eye(p) / tau2)" | Adds covariances instead of precisions; wrong posterior |
| schur-woodbury | 14:58 | "cond_cov = S11 - S12 @ np.linalg.solve(S22, S21)" | Cannot recognize the Schur-complement conditioning formula |
| matrix-solve-not-inverse | 14:57 | "S12 @ np.linalg.solve(S22, x2 - mu[idx2])" | Forms explicit inverse; numerically unstable / slow |
| marginalization-integral | 14:121 | "Marginalizing β out of ỹ_*=x_*⊤β+ε decomposes the predictive variance" | Thinks prediction is a plug-in point, not an integral over β |
| law-of-total-variance | 14:122 | "Var[ỹ_*|y] = x_*⊤Σ_n x_* (epistemic) + σ² (aleatoric)" | Cannot split predictive variance into the two sources |
| quadratic-form | 14:122 | "x_*⊤ Σ_n x_*" | Cannot compute/interpret the epistemic term or its quadratic growth |
| vectorization-einsum | 14:128 | "np.einsum(\"ij,jk,ik->i\", Xg2, Sigma_n, Xg2)" | Would loop per-row or misapply matmul; wrong per-point variance |
| expand-and-collect | 14:177 | "(X⊤X/σ²+I/τ²)⁻¹X⊤y/σ² = (X⊤X+(σ²/τ²)I)⁻¹X⊤y" | Cannot show ridge estimator equals posterior mean |
| ∝-discipline | 14:179 | "notice σ² cancels out of the coefficient, so the match holds for any noise scale" | Miscounts the α=σ²/τ² identity; thinks it is σ-dependent |
| cholesky-solve | 14:222 | "L=np.linalg.cholesky(M); solve(L.T, solve(L, y))" | Evidence evaluation is unstable / fails on large n |
| log-det-cholesky | 14:223 | "logdet = 2*np.sum(np.log(np.diag(L)))" | Cannot compute log|Σ| stably; naive det overflows |
| marginalization-integral | 14:203 | "p(y|τ²)=N(y|0, τ²XX⊤+σ²I), integrating β out entirely" | Cannot form the evidence / empirical-Bayes objective |
| log-products-to-sums | 14:208 | "log p(y|τ²)=Σ_i log p(y_i|y_1..y_{i-1},τ²)" | Prequential chain-rule factorization looks like magic |
| gamma-beta-identity | 14:289 | "E[σ²|y] = b_n/(a_n-1)" | Cannot read the inverse-Gamma mean off the posterior |
| sum-of-squares-decomp | 14:266 | "b_n=b_0+½(m_0⊤V_0⁻¹m_0 + y⊤y − m_n⊤V_n⁻¹m_n)" | NIG variance update is an unmotivated string of terms |
| location-scale | 14:268 | "ỹ_*|y ∼ t_ν(loc=x_*⊤m_n, scale²=(b_n/a_n)(1+x_*⊤V_n x_*))" | Cannot read t location/scale; conflates scale with SD |
| verify-special-case | 14:269 | "reduces to module 05's b_n(κ_n+1)/(a_nκ_n) exactly when X is intercept-only" | No habit of checking a derivation against its scalar special case |
| marginalization-integral | 14:314 | "∫ N(y|m,σ²/λ) Gamma(λ|ν/2,ν/2) dλ = t_ν(y|m,σ²)" | Cannot see Student-t as a Gaussian scale mixture |
| change-of-variables-jacobian | 14:314 | "a t is a Gamma scale-mixture of Normals" | Robust-regression mechanism (latent precision) is opaque |
| indicators | 14:315 | "Each point carries its own latent precision λ_i" | Misses the per-observation latent-variable augmentation |
| standardization-centering | 14:186 | "Xr -= Xr.mean(0)  # center so no-intercept ridge is fair" | Intercept leaks into penalty; biased ridge comparison |
| standardization-centering | 14:388 | "scales=np.abs(Phi).max(0); Phi_s = Phi / scales  # column-scale for conditioning" | Vandermonde matrix ill-conditioned; fit blows up |
| broadcasting-fancy-indexing | 14:329 | "WX = X * w[:, None]" | Weight-by-row broadcast silently wrong-shaped; bad WLS |
| broadcasting-fancy-indexing | 14:342 | "yo_out[out_idx] += np.array([8.0, 9.0, 10.0])" | Fancy-index assignment misunderstood; wrong points perturbed |
| pinv-min-norm | 14:328 | "np.linalg.lstsq(X, y, rcond=None)[0]  # start from OLS" | Does not recognize least-squares solve behind lstsq |
| verify-special-case | 14:108 | "precision form vs 05 toolkit: max|diff| … (machine precision)" | No reflex to cross-check two derivations numerically |
| gamma-beta-identity | 14:303 | "norm.ppf(0.975)*np.sqrt(df/(df-2))" | Does not know Var[t_ν]=ν/(ν−2); mis-scales the comparison |
| E[g(X)]≠g(E[X]) | 14:479 | "E[λ_i]=(ν+1)/(ν+r_i²/σ²)→0 … influence is redescending" | Misreads why heavy tails down-weight; expects linear influence |
| sqrt-n-reasoning | 14:461 | "likelihood dominates only when n≫p and the prior is loose" | Cannot reason about when regularization stops mattering |
| precision-weighted-mean | 18:47 | "θ̂_i = A/(A+1)·X_i" | Shrinkage factor meaningless; can't de-bias selection |
| marginalization-integral | 18:47 | "estimated from the marginal variance Var[X]=A+1" | Can't recover prior variance A from data; EB fails |
| add-and-subtract | 18:56 | "A_hat = max(np.mean(X**2) - 1.0, 0.0)" | Wrong A estimate; Var(X)=A+1 decomposition unused |
| law-of-total-variance | 18:56 | "marginal Var(X) = A + 1" | Can't split observed variance into signal+noise |
| broadcasting-fancy-indexing | 18:62 | "sel = np.argsort(-X)[:10]" | Can't select/index the top-k set |
| LOTUS | 18:65 | "X[sel].mean() - theta[sel].mean()" | Selection-inflation computed on wrong population |
| kernel-recognition | 18:99 | "f(z) = π_0 f_0(z) + (1-π_0) f_1(z)" | Two-groups mixture unreadable as null+alt |
| ∝-discipline | 18:101 | "fdr(z) = P(null|z) = π_0 f_0(z)/f(z)" | Posterior null-prob needs normalizing by full marginal |
| marginalization-integral | 18:102 | "estimate the whole marginal f(z) from the observed z-scores" | Local-fdr denominator unavailable without f₁ |
| indicators | 18:125 | "(bh & is_null).sum() / max(bh.sum(), 1)" | False-discovery proportion uncomputable |
| markov-chebyshev | 18:120 | "p = 2 * (1 - stats.norm.cdf(np.abs(z)))" | Two-sided tail area (p-value) mis-formed |
| log-products-to-sums | 18:184 | "loglik = -0.5*(x**2).sum()/(Agrid+1.0) - 0.5*J*np.log(Agrid+1.0)" | Product likelihood over J underflows; sum form needed |
| subtract-max | 18:185 | "w = np.exp(loglik - loglik.max()); w /= w.sum()" | exp overflow; grid posterior over A unnormalizable |
| law-of-total-variance | 18:189 | "fb_sd = np.sqrt((w*(var_c + mean_c**2)).sum() - pm**2)" | Mixture (over A) variance E[var]+Var[mean] miscomputed |
| sqrt-n-reasoning | 18:168 | "standard error going to zero" as J grows | Can't argue EB caveat is a small-J artifact |
| non-centered-reparam | 18:233 | "beta = numpyro.deterministic(\"beta\", z * lam * tau)" | Horseshoe funnel diverges; NUTS geometry collapses |
| stick-breaking | 18:206 | "λ_j ∼ Half-Cauchy(1), τ ∼ Half-Cauchy(1)" | Heavy-tailed global-local scale can't let signal escape shrinkage |
| precision-vs-covariance | 18:334 | "scales the data precision by η … variance is multiplied by 1/η" | Power-posterior widening law inverted |
| quadratic-form | 18:304 | "bhat = XtXi @ Xd.T @ yv" | OLS normal-equations solve breaks |
| matrix-solve-not-inverse | 18:318 | "np.linalg.solve(A.T @ A, A.T @ b)[1]" | Refit-on-fresh-data slope loop numerically fragile |
| projection-hat-matrix | 18:314 | "meat = Xd.T @ (Xd * (resid**2)[:, None])" | Sandwich meat X'diag(e²)X mis-assembled |
| quadratic-form | 18:315 | "sand_sd = np.sqrt((XtXi @ meat @ XtXi)[1,1])" | Sandwich bread-meat-bread quadratic mis-formed |
| broadcasting-fancy-indexing | 18:314 | "Xd * (resid**2)[:, None]" | Per-row residual weighting broadcast fails |
| gamma-beta-identity | 18:312 | "post_sd = np.sqrt(s2 * XtXi[1,1] * df/(df-2))" | Student-t variance df/(df-2) inflation dropped |
| verify-special-case | 18:329 | "For a pure mean (intercept-only) … sandwich and model sd coincide" | Can't isolate where misspecification bites |
| argmax-invariance | 18:346 | "eta_star = (post_sd / sand_sd)**2" | Recalibration knob (variance-ratio) mis-derived |
| precision-weighted-mean | 18:341 | "post_var = 1.0/(eta*n_obs/1.0 + 1.0/tau2)" | Normal-Normal precision addition mis-set |
| logsumexp | 19:79 | "ll = np.logaddexp.reduce(logr, axis=1)" | Incomplete-data log-likelihood log Σ underflows |
| kernel-recognition | 19:76 | "logr = … np.log(pi[k]) + …logpdf(X)" | Responsibilities not recognized as πₖN(x) |
| subtract-max | 19:81 | "r = np.exp(logr - ll[:, None])" | Responsibility normalization overflows |
| ∝-discipline | 19:63 | "r_{ik} ∝ π_k N(x_i;μ_k,Σ_k)" | E-step responsibilities unnormalized |
| indicators | 19:87 | "Nk = r.sum(0)" | Effective per-cluster soft counts unavailable |
| vectorization-einsum | 19:88 | "Sig[k] = (r[:,k,None,None] * (dX[:,:,None]*dX[:,None,:])).sum(0)/Nk[k]" | Weighted covariance outer-product sum breaks |
| complete-the-square-matrix | 19:126 | "Psin = Psi0 + S + (kappa0*nk/kn)*(dm @ dm.T)" | NIW posterior scale update (completing square) wrong |
| precision-weighted-mean | 19:124 | "mn = (kappa0 * m0 + nk * xbar) / kn" | Conjugate posterior mean mis-weighted |
| sum-of-squares-decomp | 19:127 | "S = (Xk - xbar).T @ (Xk - xbar)" | Within-cluster scatter matrix mis-formed |
| precision-vs-covariance | 19:130 | "mu[k] = rng.multivariate_normal(mn, Sig[k] / kn)" | NIW mean scale Σ/κ mis-set |
| gamma-beta-identity | 19:121 | "stats.invwishart(df=nu0, scale=Psi0).rvs(...)" | Σ prior draw (IW) from wrong conjugate family |
| subtract-max | 19:139 | "logp -= logp.max(1, keepdims=True)" | Categorical label sampling overflows |
| broadcasting-fancy-indexing | 19:141 | "z = (np.cumsum(P, 1) > rng.random(n)[:, None]).argmax(1)" | Vectorized categorical inverse-CDF draw fails |
| indicators | 19:151 | "prob_lo_gibbs += (z_tr[t] == lo)" | Posterior label probability un-aggregated |
| argmax-invariance | 19:97 | "o_em = np.argsort(mu_em[:, 0])" | Canonical ordering (relabel) unavailable |
| tower-rule | 19:173 | "Gibbs also averaged over where the boundary might be" | Plug-in vs posterior label-prob gap invisible |
| indicators | 19:206 | "n_swaps = (np.sign(raw0-raw1)[1:] != np.sign(...)[:-1]).sum()" | Label-switch crossings uncounted |
| argmax-invariance | 19:210 | "srt = np.sort(mu_tr[:, :, 0], axis=1)" | Ordering constraint (quotient symmetry) not enforced |
| logsumexp | 19:246 | "return np.logaddexp(c - 0.5*(x+5)**2, c - 0.5*(x-5)**2)" | Two-well log-density underflows in a tail |
| location-scale | 19:246 | "c = -np.log(2) - 0.5*np.log(2*np.pi)" | Gaussian log-normalizing constant dropped |
| log-products-to-sums | 19:257 | "acc = np.log(rng.random(K)) < beta * (lpp - lp)" | MH accept ratio in log-space mis-formed |
| ∝-discipline | 19:261 | "d = (beta[j]-beta[j+1])*(lp[j+1]-lp[j])" | Tempering swap acceptance (density ratio) wrong |
| linearity-of-expectation | 19:306 | "K_n = Σ B_i, B_i ~ Bernoulli(α/(α+i-1))" | E[Kₙ] as sum of independent Bernoullis unusable |
| gamma-beta-identity | 19:310 | "E[K_n] = α[ψ(α+n)-ψ(α)]" | Closed-form digamma mean mis-derived as log |
| log1p-approx | 19:322 | "EK_asymp = a * np.log1p(ns / a)" | Asymptotic α ln(1+n/α) loses precision at small n/a |
| sqrt-n-reasoning | 19:328 | "grows like log n" | Cluster-count growth rate mischaracterized |
| verify-special-case | 19:329 | "max|sim-exact| {np.abs(Kn_sim-EK_exact).max()}" | No check simulation matches digamma formula |
| log-products-to-sums | 19:348 | "logp += np.log(alpha/denom) if c not in counts else np.log(counts[c]/denom)" | CRP sequence probability product underflows |
| gamma-beta-identity | 19:396 | "γ_j ∼ Beta(1 + n_j, α + Σ_{ℓ>j} n_ℓ)" | Stick-weight full conditional (Beta-Bernoulli) wrong |
| stick-breaking | 19:373 | "return v * np.concatenate([[1.0], np.cumprod(1 - v[:-1])])" | Stick weights don't sum to 1; DP mixture broken |
| gamma-beta-identity | 19:373 | "v = rng.beta(1.0, alpha, size=L); v[-1] = 1.0" | Beta(1,α) stick fractions + truncation mis-set |
| broadcasting-fancy-indexing | 19:418 | "sum_gt = counts[::-1].cumsum()[::-1] - counts" | Reverse-cumsum Σ_{l>j} nₗ mis-computed |
| gamma-beta-identity | 19:429 | "s2[j] = 1.0 / rng.gamma(an, 1 / bn)" | InvGamma via reciprocal-Gamma variance draw wrong |
| complete-the-square-scalar | 19:428 | "bn = b0 + 0.5*((yj-yj.mean())**2).sum() + 0.5*kappa0*nj/kn*(yj.mean()-m0)**2" | Normal-InvGamma scale update (completed square) wrong |
| precision-weighted-mean | 19:426 | "mn = (kappa0 * m0 + yj.sum()) / kn" | Conjugate posterior mean mis-weighted |
| indicators | 19:436 | "K_tr[t] = len(np.unique(z))" | #occupied clusters miscounted |
| kernel-gram-matrix | 20:46 | "k(x,x')=φ(x)⊤Σ_w φ(x'), an n×n Gram matrix" | Function-space kernel not built; weights can't be dropped |
| quadratic-form | 20:73 | "Sig_beta = np.linalg.inv(Phi.T @ Phi / sigma_n2 + np.linalg.inv(Sigma_w))" | Weight-space posterior precision mis-assembled |
| precision-vs-covariance | 20:73 | "Phi.T @ Phi / sigma_n2 + np.linalg.inv(Sigma_w)" | Posterior = data precision + prior precision mis-added |
| vectorization-einsum | 20:77 | "var_w = np.einsum(\"ij,jk,ik->i\", Phis, Sig_beta, Phis)" | Per-point predictive variance φΣφᵀ diagonal breaks |
| schur-woodbury | 20:84 | "var_k = np.diag(Kss) - np.einsum(\"ij,jk,ik->i\", Ks.T, Kyi, Ks.T)" | Schur-complement posterior variance mis-formed |
| verify-special-case | 20:86 | "max|mean_w - mean_k| = {…:.2e}" | Two-route agreement (weight vs function) unchecked |
| marginalization-integral | 20:93 | "k(x,x') = A∫ exp(…)exp(…)dc = A h√π exp(…)" | Infinite-basis limit → RBF kernel not derived |
| change-of-variables-jacobian | 20:92 | "give each weight variance σ_w²=A·Δc, and let Δc→0" | Riemann-sum→integral scaling mis-set; limit diverges |
| kernel-recognition | 20:93 | "which is the squared-exponential (RBF) kernel … with ℓ=√2 h" | Gaussian-bump integral not recognized as RBF |
| verify-special-case | 20:111 | "max|k_M - k_RBF| = {…:.3e}" | Finite-sum → RBF convergence unverified |
| cholesky-solve | 20:160 | "L = np.linalg.cholesky(K); return (L @ gen.normal(...)).T" | Prior function draws (L·z) not sampled from N(0,K) |
| jitter-pd | 20:159 | "K = kern(xg, xg) + jitter*np.eye(len(xg))" | Cholesky fails on numerically indefinite kernel |
| floating-point-hygiene | 20:154 | "r = np.sqrt(sqd(ta, tb) + 1e-18)" | sqrt at r=0 gives NaN gradient in Matérn/periodic |
| kernel-gram-matrix | 20:150 | "k_rbf(...): return eta2*np.exp(-0.5*sqd(ta,tb)/ell**2)" | Pairwise squared-distance Gram matrix mis-built |
| broadcasting-fancy-indexing | 20:149 | "(ta[:, None] - tb[None, :])**2" | Pairwise distance matrix broadcast fails |
| schur-woodbury | 20:203 | "cond_mean = mu[idx1] + S12 @ np.linalg.solve(S22, x2 - mu[idx2])" | Gaussian block-conditioning mean mis-derived |
| schur-woodbury | 20:204 | "cond_cov = S11 - S12 @ np.linalg.solve(S22, S21)" | Schur-complement posterior covariance mis-formed |
| jitter-pd | 20:213 | "Sig += jitter*np.eye(nte+ntr)" | Joint covariance non-PD; conditioning fails |
| precision-vs-covariance | 20:212 | "Sig[nte:, nte:] += sn2*np.eye(ntr)" | Noise added to training block only; misplacement breaks fit |
| verify-special-case | 20:226 | "max posterior var at a training point = {…:.2e}" | Band-pinches-to-noise-floor claim unchecked |
| cholesky-solve | 20:262 | "a = np.linalg.solve(L.T, np.linalg.solve(L, ytr))" | Kᵧ⁻¹y via triangular back-substitution unavailable |
| log-det-cholesky | 20:264 | "complexity = -np.sum(np.log(np.diag(L)))" | log|Kᵧ| Occam term uncomputable without Cholesky diag |
| quadratic-form | 20:263 | "fit = -0.5*ytr @ a" | Data-fit term −½yᵀKᵧ⁻¹y mis-formed |
| standardization-centering | 20:270 | "yml = yml - yml.mean()" | Zero-mean GP assumption violated; fit biased |
| argmax-invariance | 20:275 | "best_ell = ells[np.argmax(lml)]" | ML-II optimum lengthscale not selected |
| jensen | 20:252 | "complexity term −½log|K_y| … prices flexibility automatically" | Evidence=fit+complexity tradeoff misread as extra penalty |
| kernel-gram-matrix | 20:308 | "KernelRidge(alpha=lam, kernel=\"rbf\", gamma=1.0/(2*ellk**2))" | KRR gamma↔lengthscale map wrong; GP≠KRR check fails |
| verify-special-case | 20:311 | "max|diff| = {np.max(np.abs(m_gp-pred_krr)):.2e}" | GP-mean = KRR equivalence unverified |
| location-scale | 20:333 | "yc = (Yev - Yev.mean())/(Yev.std() + 1e-9)" | BO GP not on unit scale; kernel hyperparams mismatched |
| change-of-variables-jacobian | 20:342 | "m_orig = m*(Yev.std()+1e-9) + Yev.mean()" | Un-standardizing GP mean/sd back to original units breaks |
| gamma-beta-identity | 20:329 | "(fbest-mu-xi)*stats.norm.cdf(z) + sd*stats.norm.pdf(z)" | Closed-form Expected Improvement mis-derived |
| standardization-centering | 20:335 | "z = (fbest - mu - xi)/sd" | EI standardized improvement z-score mis-formed |
| vectorization-einsum | 20:374 | "return np.einsum(\"nw,nwp->np\", v, H)" | Batched net forward pass Σⱼ vⱼ tanh(...) breaks |
| sqrt-n-reasoning | 20:361 | "Var[v_j]=σ_v²/H … CLT makes … jointly Gaussian" | NNGP width scaling wrong; variance blows up or vanishes |
| linearity-of-expectation | 20:506 | "Cov[f(x),f(x')]=H·(σ_v²/H)E[tanh·tanh] — the H cancels" | Can't see covariance is exact at every width |
| differentiate-under-integral | 20:494 | "nngp_k: sv2*np.sum(np.tanh(W*xa+B)*np.tanh(W*xb+B)*wt)" | NNGP kernel expectation-integral (quadrature) mis-set |
| standardization-centering | 20:492 | "W, B = np.meshgrid(np.sqrt(sw2)*z, np.sqrt(sb2)*z, ...)" | Gauss-Hermite nodes not rescaled to N(0,σ²); integral wrong |
| gamma-beta-identity | 20:491 | "z, wq = hermegauss(npts); wq = wq/np.sqrt(2*np.pi)" | Probabilists' Hermite weights un-normalized for E[g(Z)] |
| sqrt-n-reasoning | 20:409 | "relative cost (n/100)**3" | O(n³) Cholesky scaling not appreciated |
| kernel-recognition | 20:144 | "Linear: σ_b²+σ_v² x x' — Bayesian linear regression is a GP too" | Linear kernel not recognized as BLR-in-disguise |
| taylor-2nd-order | 20:142 | "Matérn-3/2 (1+√3 r/ℓ)exp(−√3 r/ℓ): only once differentiable" | Smoothness-order ↔ kernel form link lost |
| logsumexp | 15:69 | `np.logaddexp(0, z) - y * z` | Computes `log(1+e^z)` naively → overflow for large `z`; loses the stable softplus form of Bernoulli NLL |
| argmax-invariance | 15:70 | `minimize(bce, np.zeros(3), method="BFGS")` | Doesn't see that minimizing mean cross-entropy = maximizing Bernoulli likelihood (loss vs. NLL share an argmax) |
| logit-softmax-domain | 15:47 | `logit` / `$\sigma(\eta)=\frac1{1+e^{-\eta}}$` | Can't see why the link maps `(0,1)↔ℝ`; treats sigmoid as arbitrary rather than the inverse canonical link |
| verify-special-case | 15:50 | `sklearn's logistic regression ... land on the same coefficients` | Misses that `C=inf` = unpenalized = pure MLE; no cross-check that two implementations agree |
| ∝-discipline | 15:155 | `Only the log-posterior is needed, up to a constant` | Thinks the normalizing constant must be computed for MH; can't drop `p(data)` from the acceptance ratio |
| log-products-to-sums | 15:168 | `log_lik = np.sum(yc * z - np.logaddexp(0, z))` | Doesn't convert the product of Bernoulli likelihoods to a sum of log terms |
| subtract-max | 15:185 | `if np.log(gen.random()) < lp - lx` | Compares `log u < log-ratio` instead of exponentiating; without it the ratio under/overflows |
| taylor-2nd-order | 15:153 | `set $\Sigma = H^{-1}$ where $H$ ... is the negative Hessian at the mode` | Laplace = 2nd-order expansion of log-posterior at MAP; without it the Gaussian approximation is unmotivated |
| vectorization-einsum | 15:174 | `H = (Xc.T * (p * (1 - p))) @ Xc + np.eye(d)/tau**2` | Row-scaling `X.T` by weights builds `XᵀWX` without materializing `diag(W)`; a naive loop or full `W` is wrong/huge |
| precision-vs-covariance | 15:175 | `Sigma = np.linalg.inv(H)` | Doesn't recognize `H` is the posterior precision and `Σ=H⁻¹` the covariance — inverts the wrong object |
| jensen | 15:240 | `the average of the sigmoid is not the sigmoid of the average (Jensen)` | Assumes `E[σ(a)]=σ(E[a])`; misses that plug-in is systematically biased and in which direction |
| location-scale | 15:242 | `$a = x_\star^\top\beta$ is Gaussian with mean $m$ ... variance $s^2 = x_\star^\top\Sigma x_\star$` | Doesn't know a linear map of a Gaussian is Gaussian; can't push the coefficient posterior to the logit |
| quadratic-form | 15:250 | `m, s2 = x @ b_map, x @ Sigma @ x` | Predictive variance `xᵀΣx` looks like a mystery scalar; can't compute epistemic uncertainty |
| probit-logistic-approx | 15:243 | `$\sigma\!\left(\frac{m}{\sqrt{1 + \tfrac{\pi}{8}s^2}}\right)$` | Doesn't know the probit-matched Gaussian integral of a logistic; can't get the moderated probability in closed form |
| marginalization-integral | 15:239 | `$\int \sigma(x_\star^\top\beta)\, p(\beta\mid \text{data})\, d\beta$` | Confuses prediction (integrate over β) with plug-in `σ(xᵀβ̂)`; ships overconfident probabilities |
| LOTUS | 15:253 | `np.mean(1 / (1 + np.exp(-draws @ x)))` | Doesn't see the Monte-Carlo mean of `g(β)` estimates `E[g(β)]`; can't validate MacKay numerically |
| vectorization-einsum | 15:337 | `s2 = np.einsum("ij,jk,ik->i", Xe, S, Xe)` | Can't compute a batch of quadratic forms `xᵢᵀΣxᵢ` at once; falls back to a Python loop or a wrong contraction |
| indicators | 15:327 | `m = (p >= edges[i]) & (p < edges[i + 1])` | Boolean bin masks and `y[m].mean()` as bin accuracy are opaque; can't build the reliability/ECE harness |
| mode-vs-mean | 15:234 | `Laplace reports the mode, which for a skewed density is not the mean` | Assumes MAP = posterior mean; can't explain the systematic Laplace offset on skewed posteriors |
| indicators | 15:433 | `failed = (T <= c).astype(float)` then `failed * (...) + (1 - failed) * (...)` | Can't split the log-likelihood into density-vs-survival contributions per unit |
| log-products-to-sums | 15:420 | `$\ell(\beta) = \sum_{i:\ \text{failed}} (...) + \sum_{i:\ \text{censored}} (...)$` | Doesn't turn the censored-data joint likelihood into a sum of per-unit log contributions |
| standardization-centering | 15:58 | `X = np.column_stack([np.ones(n), ...])` | Forgets the intercept column; the linear predictor has no bias term and the fit is silently misspecified |
| cumulative-link | 15:465 | `$P(y\le k) = \sigma(\alpha_k - x^\top\beta)$` | Can't build the ordered-logit from cumulative categories with ordered cut-points |
| precision-weighted-mean | 16:56 | `mu_cp = np.sum(y8 * prec) / np.sum(prec)` | Doesn't recognize complete pooling as the inverse-variance-weighted mean of module 05 |
| precision-vs-covariance | 16:55 | `prec = 1.0 / s8**2` ... `se_cp = np.sqrt(1.0 / np.sum(prec))` | Averages SEs instead of adding precisions; the combined SE comes out wrong |
| non-centered-reparam | 16:165 | `sample $z_j\sim N(0,1)$ and set $\theta_j=\mu+\tau z_j$, via LocScaleReparam` | Fits the centered model, hits the funnel, and gets 86 divergences it may delete rather than fix |
| location-scale | 16:165 | `$\theta_j=\mu+\tau z_j$` | Doesn't see that the affine map of `N(0,1)` reproduces `N(μ,τ²)` — the entire basis of non-centering |
| broadcasting-fancy-indexing | 16:353 | `mu = g0 + g1 * u + eta[cidx] + b * floor` | County-level `eta` must be gathered to home level via `cidx` while `u`/`floor` are already per-home; passing county-length `u` (or a wrong index) silently misaligns and corrupts every likelihood term |
| broadcasting-fancy-indexing | 16:93 | `theta = numpyro.sample("theta", dist.Normal(mu, tau))` inside `plate("J", ...)` | Relies on scalar `mu, tau` broadcasting across the plate of length `J`; without it shapes mismatch |
| marginalization-integral | 16:288 | `v = s8**2 + np.exp(2 * log_tau)   # y_j ~ N(mu, sigma_j^2 + tau^2)` | Doesn't integrate `θ_j` out; can't form the EB marginal likelihood at all |
| location-scale | 16:288 | `v = s8**2 + np.exp(2 * log_tau)` | Misses that variances add for the sum of independent Gaussians (`σ²+τ²`); the marginal spread is wrong |
| unconstrained-reparam | 16:291 | `x0=[8.0, np.log(5.0)]` ... `tau_eb = np.exp(opt.x[1])` | Optimizes `log τ` to keep `τ>0`; without it Nelder–Mead wanders to negative variances |
| moment-matching-variance | 16:249 | `tau2_hat = np.maximum(S / (Jb - 1) - sig**2, 0.0)` | Doesn't see between-group variance = total sample variance − noise variance; the clamp keeps it non-negative |
| precision-weighted-mean | 16:212 | `w = (1/s8**2) / (1/s8**2 + 1/tau_hat**2)` | Can't read the shrinkage weight as own-precision / total-precision; borrowing strength stays a black box |
| broadcasting-fancy-indexing | 16:240 | `ybar = ytr.mean(axis=1, keepdims=True)` | Drops `keepdims`; the `(R,J)−(R,1)` broadcast of the group mean fails or mis-broadcasts |
| vectorization-einsum | 16:243 | `mse = np.array([np.mean((yte - (ybar + lam * (ytr - ybar)))**2) for lam in lams])` | Vectorized shrink-and-score over `(R,J)` at each λ; otherwise loops over 4000 replications |
| tower-rule | 16:220 | `residual gap ... is precisely the effect of marginalizing $\tau$ rather than fixing it` | Doesn't see plug-in-τ mean vs marginalized mean as `E[θ]=E_τ E[θ|τ]`; can't explain the gap |
| law-of-total-variance | 16:308 | `The missing width is the uncertainty in $\tau$ itself` | Misses that full-Bayes variance = within-τ variance + between-τ variance; can't explain why EB intervals are 27% too narrow |
| verify-special-case | 16:70 | `$\tau\to\infty$ recovers no-pooling ... $\tau\to0$ recovers complete-pooling` | Can't sanity-check the hierarchical model by its two limiting regimes |
| sqrt-n-reasoning | 16:310 | `At $J=$ thousands ... the marginal pins $\tau$ down tightly, the plug-in error vanishes` | Doesn't see hyperparameter uncertainty shrinking with the number of groups; can't state the EB scale rule |
| standardization-centering | 16:321 | `u = rng_r.normal(0., 1., size=n_cty)  # county-level uranium (standardized)` | Uses raw-scale covariates; priors like `Normal(0,5)` become mis-scaled |
| marginalization-integral | 17:139 | `$\int p(y\mid\beta)\,p(\beta)\,d\beta = N(y;\ 0,\ \sigma^2 I+\tau^2\Phi\Phi^{\top})$` | Can't reduce the evidence to a closed-form Gaussian in `y`; no exact model comparison |
| complete-the-square-matrix | 17:139 | `Marginalizing $\beta$ out of $N(y;\Phi\beta,\sigma^2 I)\,N(\beta;0,\tau^2 I)$` | The Gaussian×Gaussian → Gaussian marginal needs matrix completing-the-square; otherwise `C_d` is a mystery |
| kernel-gram-matrix | 17:158 | `C = sigma2 * np.eye(n) + tau2 * (Phi @ Phi.T)` | Doesn't recognize `ΦΦᵀ` as the `n×n` Gram matrix (data-space covariance); mis-shapes `C` |
| quadratic-form | 17:160 | `fit = -0.5 * (y @ np.linalg.solve(C, y))` | The Mahalanobis `yᵀC⁻¹y` fit term is opaque; can't split evidence into fit + Occam |
| matrix-solve-not-inverse | 17:160 | `np.linalg.solve(C, y)` | Reaches for `inv(C) @ y`; less stable and needlessly forms the inverse |
| log-det-cholesky | 17:159 | `_, logdet = np.linalg.slogdet(C)` | Computes `log(det(C))` directly → overflow/underflow; loses the stable log-determinant that *is* the Occam term |
| ∝-discipline | 17:143 | `$-\ \tfrac{n}{2}\log 2\pi$` (constant shared by every model) | Doesn't drop the shared additive constant when comparing degrees; clutters or confuses the comparison |
| logsumexp | 17:262 | `lppd = logsumexp(ll_flat, axis=0) - np.log(ll_flat.shape[0])` | Computing `log mean exp(loglik)` naively underflows; the WAIC/LOO pointwise density is garbage |
| LOTUS | 17:262 | `log mean_s p(y_i|theta_s)` | Doesn't see the posterior-predictive density as an average of the likelihood over posterior draws |
| law-of-total-variance | 17:263 | `p_waic = ll_flat.var(axis=0)` | The effective-parameter count = variance of log-lik across draws is unmotivated; can't compute the WAIC penalty |
| precision-weighted-mean | 17:273 | `mn = (k0 * m0 + n * yb) / kn` with `kn = k0 + n` | The NIG posterior mean as a precision-weighted blend of prior and data mean is opaque |
| sum-of-squares-decomp | 17:275 | `bn = b0 + 0.5*np.sum((ys - yb)**2) + 0.5*k0*n*(yb - m0)**2/kn` | The NIG scale update splits into within-sample SS + prior-vs-mean shrinkage term; otherwise a memorized formula |
| gamma-beta-identity | 17:281 | `stats.t.logpdf(y_new, df=2*an, loc=mn, scale=scale)` | Doesn't know the NIG marginal predictive is Student-t; can't get exact LOO in closed form |
| broadcasting-fancy-indexing | 17:76 | `yrep_pois = gen.poisson(lam_post[:, None], size=(S, n_ct))` | The `[:, None]` broadcast of `(S,)` rates into `(S, n_ct)` replicated datasets is load-bearing; without it shapes collide |
| indicators | 17:77 | `p_pois = float(np.mean(T_pois >= T_obs))` | PPC p-value = mean of an indicator over replications is opaque; can't compute a tail probability by simulation |
| sqrt-n-reasoning | 17:302 | `write $s^2=\sigma^2/n$ for the variance of $\bar x$` | Doesn't know the standard error of the mean is `σ/√n`; both the z-test and the Bayes factor are miscomputed |
| location-scale | 17:304 | `$\frac{N(\bar x;0,s^2)}{N(\bar x;0,s^2+\tau^2)}$` | Misses that under `H1` the marginal of `x̄` is `N(0, s²+τ²)` (variances add); BF numerator/denominator wrong |
| dominant-term-asymptotics | 17:434 | `$\sqrt{(s^2+\tau^2)/s^2}$ grows with $\tau$ while the exponential term saturates` | Can't see which factor dominates as `τ→∞`; misses that `BF01` diverges (the Lindley limit) |
| standardization-centering | 17:152 | `Legendre basis ... (orthogonal columns — numerically stable)` | Uses raw monomials; `ΦᵀΦ` becomes ill-conditioned and the evidence is numerically unreliable |
| argmax-invariance | 17:183 | `best = max(mean_ev, key=mean_ev.get)` | Selecting by highest log-evidence relies on log being monotone; confuses evidence with a transformed score |
| indicators | 17:335 | `np.mean(p0 < 0.05)` | Type-I error / power as the mean of a boolean is opaque; can't read the calibration simulation |
| verify-special-case | 17:99 | `conc->inf = Poisson` | Doesn't use the NegBin→Poisson limit as a sanity check that a finite concentration means real overdispersion |
| jensen | 17:262 | `lppd_i = log mean_s ...` (not `mean_s log`) | The deliberate log-of-mean vs mean-of-log distinction hides a Jensen gap that equals `p_waic`; conflating them biases the score |
| precision-vs-covariance | 21:22 | "Precisions add: `1/P_t = 1/P^-_t + 1/r`" | Update must be done in precision space; adding variances gives the wrong posterior |
| precision-weighted-mean | 21:22 | "`m_t = (m^-_t/P^-_t + y_t/r)/(1/P^-_t + 1/r)`" | Posterior mean is precision-weighted, not a plain average; miss it and shrinkage is wrong |
| complete-the-square-scalar | 21:21 | "Gaussian prior `N(m^-,P^-)` ... Gaussian likelihood ... Precisions add" | The Normal-Normal conjugate update is a completed square; without it no closed form |
| algebraic-rearrangement | 21:23 | "Engineers write the same thing with a gain `K_t = P^-_t/(P^-_t+r)`" | Recognizing gain form == precision form requires rearranging the same expression |
| marginalization-integral | 21:17 | "Marginalizing `x_{t-1}` out — a sum of independent Gaussians" | Predict step is integrating out prior state; skip and there's no one-step prior |
| location-scale | 21:18 | "`m^-_t = m_{t-1}, P^-_t = P_{t-1}+q`" | Sum of independent Gaussians adds means/variances; the predict formula depends on it |
| verify-special-case | 21:79 | "`max\|difference\| = 8.9e-16`" — Kalman vs `normal_known_var_update` | Cross-check that gain form equals module-05 route; without it the equivalence is unverified faith |
| kernel-recognition | 21:82 | "the gain `K = P^-/(P^-+r)` is the data's precision over the total precision" | Recognizing K as a precision ratio (not a tuning knob) is the whole conceptual payoff |
| quadratic-form | 21:129 | "`P^- = FPF^T + Q`" | Covariance propagation is a congruence transform `FPF^T`; wrong bracketing gives non-PD garbage |
| matrix-solve-not-inverse | 21:143 | "`mu[idx1] + S12 @ np.linalg.solve(S22, x2 - mu[idx2])`" | Using solve not inv for conditioning; explicit inverse is unstable/slow |
| schur-woodbury | 21:144 | "`cond_cov = S11 - S12 @ np.linalg.solve(S22, S21)`" | Conditional covariance IS the Schur complement of the block matrix |
| complete-the-square-matrix | 21:135 | joint `[[P^-, P^-H^T],[HP^-, S]]` then condition state on obs | Matrix conditioning = block completing-the-square; the whole 2-D update rests on it |
| broadcasting-fancy-indexing | 21:141 | "`Sigma[np.ix_(idx1, idx1)]`" | `np.ix_` selects submatrix blocks; wrong indexing scrambles the partitioned MVN |
| eigen-ellipse | 21:180 | "`semi = [np.sqrt(np.linalg.eigvalsh(C)) for C in covs]`" — 2σ ellipse semi-axes | Ellipse axes are sqrt-eigenvalues of covariance; miss it and you can't read the uncertainty geometry |
| eigen-ellipse | 21:185 | "`vals, vecs = np.linalg.eigh(C); ang = arctan2(vecs[1,-1], vecs[0,-1])`" | Ellipse orientation is the top eigenvector angle; needed to draw covariance correctly |
| quadratic-form | 21:203 | "position marginal stays a scalar multiple of `I` (`P[0,0]=P[1,1], P[0,1]=0`)" | Reading covariance structure (isotropy) from matrix entries explains why no tilt appears |
| precision-vs-covariance | 21:129 | "`K = P^-H^T S^{-1}`, innovation covariance `S = HP^-H^T+R`" | Gain built via innovation covariance; conflating obs/state spaces breaks dimensions |
| verify-special-case | 21:177 | "`Kalman update vs gaussian_condition, max\|diff\| = 1.8e-15`" | Byte-identity check that vectorized update == block MVN formula |
| matrix-solve-not-inverse | 21:169 | "`Kt = P_pred@H.T@np.linalg.inv(S)`" | Uses explicit inv(S) for gain — the one spot the module inverts; S small so OK, but load-bearing choice |
| expand-and-collect | 21:218 | "`bn = b0 + 0.5*(m0@V0inv@m0 + y@y - mn@inv(Vn)@mn)`" | The NIG posterior `b_n` is a collected sum-of-squares; mis-expansion breaks the noise posterior |
| complete-the-square-matrix | 21:217 | "`Vn = inv(V0inv + X.T@X); mn = Vn@(V0inv@m0 + X.T@y)`" | Conjugate regression posterior is matrix completing-the-square in β |
| broadcasting-fancy-indexing | 21:228 | "`X = np.column_stack([series[1:-1], series[:-2]])`" | Building lag design matrix via shifted slices; off-by-one wrecks the AR fit |
| location-scale | 21:237 | "`phi = mn + np.sqrt(sig2)[:,None]*(rng.standard_normal((Sd,2)) @ cholesky(Vn).T)`" | Sampling MVt via location-scale of a standard normal scaled by a Cholesky factor |
| log-det-cholesky | 21:237 | "`np.linalg.cholesky(Vn).T`" — correlate standard normals | Cholesky factor imposes the covariance correlation structure on iid draws |
| change-of-variables-jacobian | 21:236 | "`sig2 = 1.0/rng.gamma(an, 1/bn, Sd)`" — σ²~IG via 1/Gamma | Inverse-Gamma sampled as reciprocal of Gamma; wrong rate/scale convention corrupts it |
| gamma-beta-identity | 21:236 | "`rng.gamma(an, 1/bn)`" — shape/scale vs rate convention | Gamma scale = 1/rate; mixing conventions silently rescales σ² |
| indicators | 21:239 | "`stationary = (p1+p2<1)&(p2-p1<1)&(np.abs(p2)<1)`" | Stationarity fraction = mean of an indicator over posterior draws |
| verify-special-case | 21:279 | "stationary var = 0.1786 ... (empirical 0.1652)" | Sanity-check exact discretization variance against sample variance |
| location-scale | 21:264 | "`x_{t+Δ} = μ + e^{-θΔ}(x_t-μ) + η`" — OU exact transition | OU solved as exact AR(1); Euler discretization would be only approximate |
| log-products-to-sums | 21:288 | "`ll += stats.norm(m_pred, sqrt(S)).logpdf(y[t])`" | Marginal likelihood accumulated as a sum of log one-step predictives, not a product |
| argmax-invariance | 21:302 | "`theta MLE ... = grid[lls.argmax()]`" | Maximizing log marginal likelihood == maximizing likelihood; argmax over log grid |
| marginalization-integral | 21:325 | "`log p(y_{1:n}) = Σ_t log N(y_t; m^-_t, S_t)`" (prediction-error decomposition) | Marginal likelihood is a telescoped chain of one-step marginals; the free-likelihood trick |
| subtract-max | 21:363 | "`w = np.exp(logw - logw.max()); w /= w.sum()`" | Normalize importance weights in log-space via subtract-max or overflow to inf |
| log-products-to-sums | 21:362 | "`logw += stats.norm(0, exp(x/2)).logpdf(y[t])`" | Particle weights accumulate in log-space; multiplying raw likelihoods underflows |
| sqrt-n-reasoning | 21:425 | "`K_inf ≈ sqrt(q/r)` in the small-gain limit" | Steady-state gain is a square-root law, not linear; predicts graceful degradation |
| markov-chebyshev | 21:337 | ESS collapse: "a product of likelihoods is one enormous importance weight" | ESS/N→0 diagnosis is the weight-variance argument; without it degeneracy looks like a bug |
| verify-special-case | 21:105 | "`max\|diff\| over {n} steps = ...`" every step, not just illustrative one | Checking equality at all 60 steps, not one, guards against a lucky coincidence |
| change-of-variables-jacobian | 21:353 | "`x = rng.normal(0, sig/sqrt(1-phi**2), Np)`" — stationary-dist init | Particles initialized from the AR(1) stationary variance `σ²/(1−φ²)` |
| linearity-of-expectation | 22:52 | "`ρ(treat) = (1-p)C_FP, ρ(wait) = p·C_FN`" | Expected loss = probability-weighted sum over the 2×2 loss matrix; LOTUS over the posterior |
| algebraic-rearrangement | 22:53 | "`(1-p)C_FP < p C_FN` rearranges to `p > C_FP/(C_FP+C_FN)`" | Solving the loss-crossover for the threshold; the whole "0.5 is wrong" result |
| LOTUS | 22:106 | "`loss_ship_B = np.mean(np.maximum(tA - tB, 0.0))`" | Expected regret = Monte-Carlo E[g(θ)] under posterior draws, not g(E[θ]) |
| jensen | 22:114 | "a probability weighs worlds, a loss weighs worlds × stakes" | E[max(Δ,0)] ≠ max(E[Δ],0); regret ratio 81× not 19× because loss isn't a function of the win-prob |
| indicators | 22:105 | "`p_B_beats_A = np.mean(tB > tA)`" | P(B best) = mean of an indicator over joint posterior draws |
| broadcasting-fancy-indexing | 22:151 | "`sA = rng.binomial(n, th_A)`" — future successes per world, vectorized | Simulating one future per posterior world in one array op; a per-world loop would be intractable |
| tower-rule | 22:135 | "`regret_now = np.mean(best - th_B) * H`" (EVPI over draws × horizon) | EVSI/EVPI is a nested expectation (preposterior): average over futures of a re-decided loss |
| standardization-centering | 22:141 | "`lead = (dB.mean() - dA.mean()) / np.sqrt(dA.var()+dB.var())`" | Standardized lead in σ units; variance of a difference adds variances |
| law-of-total-variance | 22:141 | "`np.sqrt(dA.var() + dB.var())`" — sd of θB−θA from independent arms | Variance of independent difference is sum of variances; wrong if you forget independence |
| gamma-beta-identity | 22:140 | "`dA.var()`" — exact Beta moments instead of simulating | Uses closed-form Beta variance `ab/((a+b)²(a+b+1))` for the lead; avoids MC noise |
| verify-special-case | 22:141 | "printed above from the exact Beta moments" | Cross-checks the simulated separation against analytic Beta moments |
| argmax-invariance | 22:158 | "`n_star = ns[np.argmax(net)]`" | Optimal batch is argmax of net value; picking the hump requires the argmax move |
| LOTUS | 22:152 | "`chosen = np.where(muA>muB, th_A, th_B); regret_after = np.mean(best - chosen)*H`" | Preposterior: decision under simulated data then averaged loss over true worlds |
| broadcasting-fancy-indexing | 22:207 | "`alpha = np.ones((REPS, K))`" — (reps, arms) state advanced together | Vectorizing 100 reps × K arms; a per-rep loop is 100× slower and the panel forbids it |
| broadcasting-fancy-indexing | 22:223 | "`alpha[rows, arm] += reward`" — fancy-index update per rep | Scatter-update each rep's chosen arm via row/column index arrays |
| argmax-invariance | 22:214 | "`arm = g.beta(alpha, beta).argmax(axis=1)`" — Thompson pull | Thompson = argmax of one posterior draw per arm; probability-matching falls out |
| log-products-to-sums | 22:220 | "`ucb = s/n + np.sqrt(2*np.log(t+1)/n)`" | UCB bonus uses log t; the confidence radius derivation is a Hoeffding/union-bound in log |
| union-triangle-bound | 22:220 | "`np.sqrt(2*np.log(t+1)/n)`" — UCB1 confidence radius | The `2 ln t` bonus comes from a union bound over pulls; wrong constant loses the log-regret guarantee |
| linearity-of-expectation | 22:225 | "`inst[t] = np.mean(best_rate - rates[arm])`; `np.cumsum(inst)`" | Cumulative regret = summed per-pull expected gaps; linearity across dependent pulls |
| sqrt-n-reasoning | 22:251 | "`ε`-greedy ... regret grows linearly ... while others flatten toward logarithmic" | Distinguishing linear vs log regret growth rates; the whole ranking hinges on asymptotic order |
| indicators | 22:311 | "`np.mean(final_arm != 2)`" — P(locked on wrong arm) | Lock-in probability = mean of a mismatch indicator across reps |
| complete-the-square-matrix | 23:61 | "`Sn = np.linalg.inv(np.eye(p)/tau2 + X.T@X/s2); mn = Sn@(X.T@y/s2)`" | Gaussian-prior posterior is completed-square in β; the ridge/BLR formula |
| precision-vs-covariance | 23:61 | "`np.eye(p)/tau2 + X.T@X/s2`" — prior precision + data precision | Posterior precision adds prior and data precision; the whole conjugate update |
| pinv-min-norm | 23:57 | "`b_ols, *_ = np.linalg.lstsq(X, y, rcond=None)`" | Least-squares via lstsq (min-norm/pinv), not normal equations; stable EB plug-in for σ² |
| logit-softmax-domain | 23:71 | "`pT = 1/(1 + np.exp(-1.5*U))`" | Confounded assignment via logistic link; the sigmoid maps severity to treat-probability |
| verify-special-case | 23:104 | "Adjusting the confounded data for U recovers `2.135`" | Oracle fit (adjust for U) confirms confounding is the cause, not the estimator |
| jensen | 23:154 | "Averaging a concave function pulls you below its value at the mean (Jensen)" | Assurance < point-power is exactly Jensen on the concave power curve; the section's core result |
| taylor-2nd-order | 23:110 | "test statistic has non-centrality `δ√(n/2)/σ`" | Two-sample z-test power via noncentrality; wrong √(n/2) misplaces the whole power curve |
| marginalization-integral | 23:115 | "`assurance = ∫ power(δ)π(δ)dδ = E_π[power(δ)]`" | Assurance is prior-averaged power; a quadrature over the unknown effect |
| differentiate-under-integral | 23:132 | "`prior = stats.norm(0.5,0.2).pdf(gd); prior /= prior.sum()`" | Discretize continuous prior to a normalized grid for quadrature; skip normalization and the integral is off |
| kernel-recognition | 23:173 | "`θ^s(1-θ)^{n-s}·(factor free of θ)`" — stopping factor is θ-free | Likelihood is the Beta kernel; the stopping indicator drops out because it carries no θ |
| indicators | 23:173 | "`1{the rule stops here}` ... a CONSTANT in theta, so it cancels" | Stopping rule enters as an indicator that's constant in θ, hence cancels in normalization |
| log-products-to-sums | 23:200 | "`log_lik += np.log(tgrid) if x else np.log(1-tgrid)`" | Sequential likelihood built by adding logs over the stream; product would underflow |
| subtract-max | 23:204 | "`post_grid = np.exp(log_lik - log_lik.max())`" | Grid posterior exponentiated after subtract-max to avoid overflow |
| verify-special-case | 23:214 | "max \|density difference\| between the two routes: `1.00e-08`" | Sequential-with-stopping route vs closed-form Beta must agree; proves the likelihood identity |
| tower-rule | 23:221 | "the posterior is a martingale in the data filtration; optional stopping does not move its prior-averaged calibration" | Coverage-under-stopping proof is the optional-stopping theorem for the posterior martingale |
| broadcasting-fancy-indexing | 23:229 | "`cs = np.cumsum(y, axis=1)`; `m = cs/prec`" — posterior mean at every n | Vectorized cumulative posterior across all stopping times at once |
| precision-vs-covariance | 23:231 | "`prec = 1/tau0**2 + ns`" — posterior precision (σ²=1) | Normal-Normal precision adds; posterior sd = 1/√prec at every n |
| indicators | 23:233 | "`excl0 = np.abs(m) > z*sd`; `first = ...excl0.argmax(1)`" | Stopping time = first index where an indicator fires; argmax of a boolean finds it |
| standardization-centering | 23:261 | "`zstat = np.abs(cum/ns - 0.5)/np.sqrt(0.25/ns)`" | z-statistic standardizes the running proportion by its null sd `√(0.25/n)` |
| union-triangle-bound | 23:265 | "`(zstat[:, looks-1] > z).any(axis=1).mean()`" | Type-I over multiple looks = P(union of rejections); every peek is another chance |
| sqrt-n-reasoning | 23:289 | "by the law of the iterated logarithm this diverges toward 1 as N→∞" | Continuous-monitoring Type-I →1 is the LIL; explains why peeking guarantees rejection |
| tower-rule | 23:314 | "coverage ... collapses to `0.6197`" under publish-if-significant | Selective reporting conditions on a θ-informative event; nested expectation breaks calibration |
| markov-chebyshev | 23:316 | "Ville's inequality caps ... `P(sup_n BF10 ≥ k) ≤ 1/k`" | Ville = Markov's inequality for the nonnegative BF martingale; bounds fake-evidence probability |
| log-det-cholesky | 23:325 | "`logBF = 0.5*(tau2*S1**2/(1+ns*tau2) - np.log(1+ns*tau2))`" | Gaussian BF has a log-determinant Occam penalty `−½log(1+nτ²)`; drop it and BF is uncalibrated |
| complete-the-square-scalar | 23:325 | "`tau2*S1**2/(1+ns*tau2)`" — marginal likelihood of Gaussian mean | Integrating out μ against N(0,τ²) completes the square, giving the BF's data term |
| verify-special-case | 23:327 | "`0.0598`, safely under the `0.1000` bound" | Simulated sup-BF probability checked against the Ville bound |
| quadratic-form | 23:351 | "`rows.append([1, A, B, C, A*B, A*C, B*C, A*B*C])`" | Interaction columns are elementwise products of main-effect columns; the ±1 design matrix |
| pinv-min-norm | 23:354 | "`beta_ols, *_ = np.linalg.lstsq(X, y, rcond=None)`" | Effects via least squares on coded design |
| algebraic-rearrangement | 23:355 | "`effects = 2 * beta_ols`" — Montgomery effect = 2×coef | Coef→effect factor of 2 because ±1 coding moves two units; forget it and effects are halved |
| kernel-gram-matrix | 23:362 | "with an orthogonal ±1 design, `X^T X` is diagonal, so each coefficient is an independent contrast" | Diagonal Gram matrix decouples coefficients; the reason effects == contrasts exactly |
| complete-the-square-scalar | 23:374 | "`m1 = tau1**2/(tau1**2+vj)*bhat`" — slab posterior mean | Each spike/slab component is a scalar Normal-Normal shrinkage; the closed-form update |
| kernel-recognition | 23:376 | "`l1 = (1-w)*stats.norm.pdf(bhat, 0, sqrt(tau1**2+vj))`" | Marginal likelihood of a component is N(0, prior var + like var); inclusion prob needs this kernel |
| precision-weighted-mean | 23:379 | "`(1-p_slab)*m0 + p_slab*m1`" — posterior mixture mean | Two-component posterior mean is inclusion-prob-weighted blend of spike/slab means |
| kernel-gram-matrix | 23:369 | "`v = s2/np.diag(X.T@X)`" — per-coef likelihood variance | Diagonal design makes each coef's variance `s²/(X^TX)_jj`; needed for independent shrinkage |
| log-det-cholesky | 23:411 | "`EIG(d) = H(E_θ[p]) − E_θ[H(p)]`" | Expected info gain = entropy of mean minus mean of entropy; the mutual-information decomposition |
| jensen | 23:412 | "`H(E_θ[p(y)]) − E_θ[H(p(y))]` ≥ 0" | EIG ≥ 0 is Jensen on concave entropy; the two-term structure only makes sense via it |
| floating-point-hygiene | 23:431 | "`p = np.clip(p, 1e-12, 1-1e-12)`" — binary entropy | Clip probabilities before log so `0·log0` doesn't become nan; entropy blows up otherwise |
| LOTUS | 23:435 | "`Hb((W*expit(A2+B2*d)).sum()) - (W*Hb(expit(A2+B2*d))).sum()`" | Both EIG terms are posterior-weighted expectations over the (a,b) grid; E[g(θ)] quadrature |
| logit-softmax-domain | 23:427 | "`p = expit(A2 + B2*d)`" — grid Bayes update on logistic | Dose-response likelihood via sigmoid; each grid update multiplies in `p` or `1−p` |
| log-det-cholesky | 23:457 | "posterior covariance `σ²(X^T X)^{-1}` ... smallest determinant = largest `det(X^T X)`" | D-optimality is minimizing log-det of posterior covariance; the info=−½log\|Σ\| link |
| schur-woodbury | 23:465 | "`np.linalg.det(np.linalg.inv(ofat.T@ofat))`" — covariance det ratio | Design comparison via determinant of `(X^TX)^{-1}`; the generalized-variance criterion |
| verify-special-case | 23:466 | "det(XtX): factorial `64.0`, OFAT `32.0`, ratio `2.000`" | Confirms factorial beats OFAT by the exact determinant ratio |
| indicators | 23:485 | "`p_perm = (np.abs(perm) >= abs(obs)).mean()`" | Permutation p-value = mean of a tail indicator over relabelings |
| broadcasting-fancy-indexing | 23:484 | "`perm = pool[idx[:, nA:]].mean(1) - pool[idx[:, :nA]].mean(1)`" | Vectorized relabeling via fancy-indexed permutation matrix; a per-perm loop is 20000× slower |
| linearity-of-expectation | 23:483 | "`idx = np.array([g.permutation(Ntot) for _ in range(nperm)])`" | Sampling relabelings to approximate the exact permutation distribution's mean-difference |
| standardization-centering | 23:302 | "`ybar = g.normal(theta, sigma/np.sqrt(n_study))`" | Sample mean has sd `σ/√n`; the winner's-curse simulation depends on the correct SE |
| jensen | 23:154 | "prior mass on effects smaller than 0.5 costs more power than the equal mass above buys back" | The asymmetry is the concavity/Jensen gap made concrete; miss it and assurance looks like a bug |
| indicators | 24:59 | `Yobs = np.where(T == 1, Y1, Y0)` | the switch T·Y(1)+(1−T)·Y(0) is an indicator selection; without it the observed-outcome mapping is undefined |
| linearity-of-expectation | 24:56 | `ATE = np.mean(Y1 - Y0)` | E[Y(1)−Y(0)]=E[Y(1)]−E[Y(0)] across dependent columns; average effect = difference of averages though no individual effect is ever seen |
| broadcasting-fancy-indexing | 24:60 | `Yobs[T == 1].mean() - Yobs[T == 0].mean()` | boolean-mask group means; a misaligned mask silently averages the wrong arm |
| tower-rule | 24:90 | ignorability gives `E[Y∣T=1]=E[Y(1)]` | connects conditional group mean to marginal potential outcome; the identification step itself |
| marginalization-integral | 24:123 | `sum(pz[z] * (rate(...) - rate(...)) for z in (0, 1))` | backdoor adjustment averages the within-stratum effect over the confounder's OWN marginal; wrong weighting gives a biased ATE |
| tower-rule | 24:143 | g-formula `E[Y∣do(T=t)]=∑_z E[Y∣T=t,Z=z]P(Z=z)` | condition-then-marginalize is the entire adjustment logic |
| projection-hat-matrix | 24:164 | `ra = a - C @ np.linalg.lstsq(C, a, rcond=None)[0]` | residualizing = applying (I−H); partial correlation requires the residual-maker projection |
| matrix-solve-not-inverse | 24:215 | `return np.linalg.lstsq(Xd, y, rcond=None)[0]` | OLS via a least-squares solve, not an explicit inverse; stability on near-collinear designs |
| expand-and-collect | 24:214 | `Xd = np.column_stack([np.ones_like(y)] + cols)` | intercept column + regressors; dropping the ones column silently removes the intercept |
| logit-softmax-domain | 24:297 | `e = 1 / (1 + np.exp(-a * X))` | sigmoid maps a linear index into (0,1); the propensity must be a probability |
| jitter-pd | 24:305 | `W = p * (1 - p) + 1e-9` | IRLS weights at p≈0/1 would divide by zero; the jitter keeps the solve finite |
| matrix-solve-not-inverse | 24:307 | `b = np.linalg.solve(Xd.T * W @ Xd, Xd.T @ (W * z))` | weighted normal equations solved, not inverted; the Newton/IRLS step |
| quadratic-form | 24:307 | `Xd.T * W @ Xd` | XᵀWX weighted Gram = Fisher information; built by row-scaling with W |
| broadcasting-fancy-indexing | 24:307 | `Xd.T * W` | row-scales the design by the weight vector via broadcasting; wrong axis corrupts silently |
| floating-point-hygiene | 24:315 | `q[0] -= 1e-9; q[-1] += 1e-9` | nudge quantile edges so `digitize` keeps boundary points; otherwise strata lose their endpoints |
| importance-weights | 24:319 | `w1, w0 = T / ehat, (1 - T) / (1 - ehat)` | 1/e(X) is the p/q importance weight correcting a propensity-biased sample to the population |
| self-normalized-IS | 24:320 | `np.sum(w1 * Y) / np.sum(w1)` | dividing by Σw not n = Hájek/self-normalized IS; handles unnormalized weights and cuts variance |
| sqrt-n-reasoning | 24:291 | `return w.sum()**2 / (w**2).sum()` | Kong ESS flags weight collapse; without it IPW fails silently over exploded weights |
| marginalization-integral | 24:288 | `E[Y(1)]=E[T\,Y/e(X)]` | Horvitz–Thompson = the importance-sampling change-of-measure identity; reweights the expectation to the population measure |
| indicators | 24:110 | `Y = (g2.random(M) < base + delta * Tt).astype(int)` | Bernoulli sampling via uniform<p; the simulation primitive throughout |
| tower-rule | 24:499 | `wU_T1 = np.array([(1-pU)*pT_U[0], pU*pT_U[1]]); wU_T1 /= wU_T1.sum()` | Bayes on U given T to get P(U∣T); needed to compute E[Y∣T] under pure confounding |
| LOTUS | 24:501 | `assoc_confounding = wU_T1 @ pY_U - wU_T0 @ pY_U` | E[Y∣T]=Σ_u P(u∣T)E[Y∣u] as a weighted dot product; the sensitivity-analysis number |
| verify-special-case | 24:392 | `max \|JA - JB\| = {np.abs(JA - JB).max():.4f}` | hand/numeric check that both DGP joints land on [0.3,0.2,0.2,0.3]; confirms the observed laws are identical, not merely close |
| indicators | 24:386 | `np.mean((T == t) & (Y == y))` | joint 2×2 cell probabilities as means of boolean ANDs |
| logsumexp | 25:58 | `q = np.exp(z - logsumexp(z))` | stable softmax; naive `exp` of large logits overflows |
| argmax-invariance | 25:59 | `minimize(lambda z: ce(np.append(z, 0.0)), np.zeros(2))` | pinning the last logit to 0 removes the softmax shift-redundancy; else the logits are non-identified and BFGS wanders |
| log-products-to-sums | 25:58 | `-np.sum(counts * np.log(q))` | categorical log-likelihood as a sum of logs; the product form underflows |
| precision-weighted-mean | 25:68 | `map_closed = y.sum() / (len(y) + lam)` | closed-form MAP (nȳ)/(n+λ) is the shrinkage estimate the optimizer is verified against |
| complete-the-square-scalar | 25:69 | `0.5*np.sum((y-m)**2)/s2 + 0.5*lam*m**2/s2` | the penalized quadratic has a closed-form minimizer = Gaussian-prior MAP; the ridge identity |
| precision-vs-covariance | 25:66 | `s2, tau2 = 1.0, 2.0; lam = s2 / tau2` | the λ=σ²/τ² dictionary; regularization strength IS a prior precision ratio |
| standardization-centering | 25:105 | `Xtr = (Xtr - mu) / sd; Xval = (Xval - mu) / sd; Xte = ...` | standardize on TRAINING moments only; using test moments leaks and corrupts the calibration audit |
| marginalization-integral | 25:116 | `p_single, p_ens = P_te[0], P_te.mean(0)` | averaging member probabilities approximates ∫p(y∣x,w)p(w∣D)dw — the posterior predictive |
| logit-softmax-domain | 25:130 | `p = np.clip(1 / (1 + np.exp(-logit_v / T)), 1e-9, 1 - 1e-9)` | temperature scaling lives in logit space; must map prob→log-odds→prob correctly |
| floating-point-hygiene | 25:127 | `np.clip(members[0].predict_proba(Xval)[:, 1], 1e-6, 1 - 1e-6)` | clip before log/logit; log(0) or log-odds of exactly 1 blows up |
| argmax-invariance | 25:124 | temp scaling "cannot change a decision (it never crosses 0.5 ...)" | a monotone logit rescale never moves the argmax; only confidence changes |
| law-of-total-variance | 25:171 | `disag = Pg.std(0).reshape(GX.shape)` | member std over weight draws = the epistemic-variance component, high off-data |
| gamma-beta-identity | 25:193 | `Pr(next=1∣k,n) = (k+a)/(n+a+b)` | the Beta-Bernoulli posterior predictive is the closed-form training target the net must match |
| broadcasting-fancy-indexing | 25:202 | `bits = (g.random((3000, 30)) < theta[:, None]).astype(int)` | `theta[:,None]` broadcasts a per-sequence rate over 30 flips; wrong axis destroys the exchangeable-not-iid structure |
| sum-of-squares-decomp | 25:203 | `csum = np.cumsum(bits, 1)` | the running (k,n) is the sufficient statistic; compresses the whole context to two numbers |
| verify-special-case | 25:226 | `empirical next-bit freq {yf[m].mean():.4f} ... vs exact` | de Finetti check: population next-bit frequency = posterior predictive, verifying the training target |
| location-scale | 25:250 | `N(mu_i e^{-t},\; v_i e^{-2t} + (1-e^{-2t}))` | Gaussian convolution keeps a GMM a GMM under OU flow — mean shrinks, variance interpolates; the whole exact-score construction |
| score-function | 25:263 | `np.sum(r * (-(x[None,:]-mt[:,None]) / vt[:,None]), axis=0)` | ∇log p as the responsibility-weighted component score; the exact reverse-diffusion drift |
| subtract-max | 25:262 | `r = np.exp(logc - logsumexp(logc, axis=0))` | responsibilities via a stabilized softmax over mixture components; raw exp under/overflows in the tails |
| non-centered-reparam | 25:271 | `x = x + (x + 2*score(x, t))*dt + np.sqrt(2*dt)*rdif.normal(0, 1, x.size)` | Euler–Maruyama: injected noise scales as √dt, not dt; wrong scaling breaks the SDE limit |
| law-of-total-variance | 25:274 | `mix_var = np.sum(w*(v0 + m0**2)) - mix_mean**2` | mixture variance = E[within] + Var[between]; naively averaging component variances is wrong |
| pinv-min-norm | 25:320 | `np.linalg.pinv(Phi) @ ytr_dd` | the minimum-norm ridgeless interpolant; the exact object whose norm blowup at p=n produces double descent |
| jitter-pd | 25:321 | `np.linalg.solve(Phi.T@Phi + 1e-1*np.eye(p), Phi.T@ytr_dd)` | λI regularizes the near-singular Gram at p=n; solved, not inverted |
| projection-hat-matrix | 25:346 | `tr(Φ(Φ^⊤Φ+λI)^{-1}Φ^⊤)` | effective number of parameters = trace of the (ridge) hat matrix; explains why the prior keeps complexity below p |
| non-centered-reparam | 25:363 | `z = mu + (0.5*logvar).exp() * randn_like(mu)` | the reparameterization trick — noise outside, scale/shift inside — lets gradients flow through the sampling step |
| sqrt-n-reasoning | 25:311 | `relu_feat = lambda X, W: np.maximum(X @ W, 0) / np.sqrt(W.shape[1])` | 1/√p feature scaling keeps activations O(1) as width grows; else the sweep over p is not comparable |
| logsumexp | 25:477 | `q = np.exp(logits/T - logsumexp(logits/T))` | tempered softmax p^{1/T} computed stably; the T↔1/η tempering identity |
| argmax-invariance | 25:60 | `max\|diff\| = {np.max(np.abs(qhat-counts/n)):.2e}` | verify the CE minimizer equals empirical frequencies to machine precision — the theorem-grade check |
| sum-of-squares-decomp | 26:80 | `S = ((y - xbar) ** 2).sum()` | centered sum of squares is the NIG sufficient statistic feeding the variance posterior |
| gamma-beta-identity | 26:79 | `sigma^2 \| y ~ IG((n-1)/2, S/2)` | the conjugate NIG posterior; without it no closed-form marginal for μ exists |
| marginalization-integral | 26:86 | `mu \| y ~ t_{2an}(mn, bn/(an*kn))` | integrating σ² out turns the Normal into a Student-t; the honest (wider) interval |
| unbiased-variance | 26:92 | `s2 = ((y - mn) ** 2).sum() / (kn - 1)` | the n−1 divisor; dividing by n underestimates σ² and worsens the plug-in undercoverage |
| location-scale | 26:93 | `sd = np.sqrt(s2 / kn)` | SE = σ/√n sets the plug-in interval's scale |
| law-of-total-variance | 26:127 | "the uncertainty *in σ²* feeds first-order into the uncertainty in μ" | profiling discards the σ²-uncertainty component; the total-variance argument for why t must be wider |
| verify-special-case | 26:111 | `ct += lt <= 10.0 <= ht` | the Monte-Carlo coverage replay is the frequentist audit; without it the 0.89-vs-0.95 gap is invisible |
| exchangeability | 26:190 | "calibration and test residuals are exchangeable, so a calibration quantile bounds the test residual" | the sole assumption behind conformal's finite-sample coverage; under shift the guarantee silently voids |
| gamma-beta-identity | EXAM:92 | `lam_i = rng.gamma(2.0, 3.5 / 2.0, n1)` | scale=mean/shape parametrization; can't map "shape 2, mean 3.5" to numpy's scale arg |
| precision-vs-covariance | EXAM:92 | `Gamma(2, 0.5 rate), mean 4` | rate vs scale confusion; numpy gamma takes scale=1/rate, so passing 0.5 gives wrong prior |
| verify-special-case | EXAM:96 | `disp_obs = y1.var(ddof=1) / y1.mean()` | doesn't know var/mean=1 is Poisson's fingerprint, so no diagnostic to test |
| law-of-total-variance | EXAM:91 | `Poisson-Gamma mixture => var/mean > 1` | can't see why the mixture is overdispersed; Var=E[Var]+Var[E] |
| law-of-total-variance | EXAM:88 | `a Poisson cannot manufacture that spread: its variance is locked to its mean` | misses that mixing inflates variance beyond the mean |
| marginalization-integral | EXAM:100 | `lam_pp = rng.gamma(a0, 1 / b0, 40000); y_pp = rng.poisson(lam_pp)` | prior-predictive = integrate likelihood over prior by composing draws; would hunt for a closed form |
| kernel-recognition | EXAM:106 | `an, bn = a0 + y1.sum(), b0 + n1` | conjugate Gamma-Poisson update not read off the likelihood kernel |
| precision-weighted-mean | EXAM:107 | `post_mean = an / bn` | Gamma mean shape/rate not recalled |
| indicators | EXAM:117 | `p_pois = np.mean(disp_rep >= disp_obs)` | PPC p-value as mean of an indicator over replicates not understood |
| gamma-beta-identity | EXAM:112 | `lam_draw = rng.gamma(an, 1 / bn, S)` | rate-to-scale inversion (1/bn); silently wrong-scale draws |
| expand-and-collect | EXAM:124 | `var = mu + mu^2/r  =>  r = mu^2/(var - mu)` | method-of-moments inversion of the NB variance formula not derived |
| precision-vs-covariance | EXAM:127 | `p_succ = r_hat / (r_hat + mu_hat)` | NB (r,p) vs (mean,var) reparametrization; wrong success prob passed to numpy |
| LOTUS | EXAM:137 | `E_excess = pen * np.mean(np.maximum(lam_draw - tol, 0.0))` | expected loss = mean of loss over posterior draws (Monte Carlo LOTUS) not seen |
| indicators | EXAM:137 | `np.maximum(lam_draw - tol, 0.0)` | positive-part / hinge as excess-above-tolerance not recognized |
| kernel-recognition | EXAM:161 | `same likelihood ∝ θ⁹(1−θ)³, so same posterior` | doesn't see binomial and negative-binomial share the same θ-kernel, so misses the identical posterior |
| ∝-discipline | EXAM:174 | `a_post, b_post = 1 + 9, 1 + 3` | Beta-Binomial conjugate update from the kernel not recognized |
| gamma-beta-identity | EXAM:175 | `mean = {a_post/(a_post+b_post)` | Beta mean a/(a+b) not recalled |
| sqrt-n-reasoning | EXAM:191 | `z = (phat - 0.5) / np.sqrt(0.25 / nlook)` | CLT standard error √(p(1−p)/n) not derived; wrong test statistic |
| union-triangle-bound | EXAM:180 | `"ever cross 1.96" is a much larger event than "cross at one fixed look"` | can't reason why P(reject at any of 10 looks) ≫ P(reject at one look) |
| indicators | EXAM:195 | `reject_any \|= sig` | cumulative OR over looks as the "ever significant" indicator not built |
| broadcasting-fancy-indexing | EXAM:186 | `draws = (rng.random((reps, looks[-1])) < 0.5).astype(int)` | vectorized Bernoulli stream via boolean broadcast not constructed |
| vectorization-einsum | EXAM:187 | `cum = np.cumsum(draws, axis=1)` | running success counts via cumsum along an axis; would loop instead |
| change-of-variables-jacobian | EXAM:234 | `ljac = np.log(th) + np.log1p(-th)  # \|d theta/d phi\| = theta(1-theta)` | forgets the Jacobian when moving to the logit scale; wrong unnormalized density and wrong evidence |
| logit-softmax-domain | EXAM:230 | `th = expit(phi)` | doesn't map unconstrained φ back to (0,1) via sigmoid; optimizer fights box constraints |
| log-products-to-sums | EXAM:231 | `ll = (k * np.log(th) + (n - k) * np.log1p(-th) ...)` | binomial log-likelihood as a sum of logs not formed |
| floating-point-hygiene | EXAM:231 | `np.log1p(-th)` | log(1−th) loses precision as th→0; naive log(1-th) is inaccurate |
| floating-point-hygiene | EXAM:226 | `gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)` | log-Gamma for binomial coefficients; direct factorials overflow |
| taylor-2nd-order | EXAM:239 | `H = (neg_log_g(phi_star + h) - 2*neg_log_g(phi_star) + neg_log_g(phi_star - h)) / h**2` | central second-difference as Hessian estimate not recognized |
| taylor-2nd-order | EXAM:240 | `log_ev_lap = g_star + 0.5 * np.log(2 * np.pi / H)` | Laplace evidence formula (Gaussian integral from a 2nd-order expansion at the mode) not known |
| argmax-invariance | EXAM:236 | `res = optimize.minimize_scalar(neg_log_g, ...)` | minimizing negative-log to find the posterior mode (log-scale argmax) not recognized |
| gamma-beta-identity | EXAM:226 | `betaln(a0p + k, b0p + n - k) - betaln(a0p, b0p)` | Beta-Binomial evidence as a ratio of Beta functions not derived |
| change-of-variables-jacobian | EXAM:244 | `p_lap = stats.norm(...).pdf(logit(tt)) / (tt * (1 - tt))` | pushforward density needs division by the Jacobian to compare in θ-space; omitting it mismeasures TV |
| marginalization-integral | EXAM:245 | `tv = 0.5 * np.trapezoid(np.abs(p_true - p_lap), tt)` | TV = ½∫\|p−q\| definition not known; can't compute the distance |
| sqrt-n-reasoning | EXAM:219 | `the classic O(1/√n)` | can't predict that the error shrinks as 1/√n; expects constant error |
| precision-weighted-mean | EXAM:283 | `mn = (k0 * m0 + n4 * ybar4) / kn` | posterior mean as a precision-weighted prior/data average not recognized |
| sum-of-squares-decomp | EXAM:284 | `bn4 = b0n + 0.5*Sxx + 0.5*k0*n4/kn*(ybar4 - m0)**2` | the sum-of-squares decomposition (within-data + prior-shift term) not derived |
| location-scale | EXAM:285 | `df, mu_scale = 2*an4, np.sqrt(bn4/(an4*kn))` | marginal μ is a shifted/scaled Student-t; can't assemble t-parameters from NIG hyperparameters |
| gamma-beta-identity | EXAM:296 | `s2 = 1.0 / rng.gamma(a_s, 1 / b_s)` | Inverse-Gamma sampled as the reciprocal of a Gamma not known |
| kernel-recognition | EXAM:295 | `b_s = b0n + 0.5*np.sum((y4 - mu)**2) + 0.5*k0*(mu - m0)**2` | full conditional for σ² not identified from the joint kernel |
| location-scale | EXAM:297 | `mu = rng.normal(mn, np.sqrt(s2 / kn))` | μ-conditional scale s²/kn not derived |
| verify-special-case | EXAM:302 | `ks_mu = stats.kstest(mu_ch, stats.t(df, mn, mu_scale).cdf).pvalue` | auditing a sampler against the conjugate closed form as ground truth not conceived |
| standardization-centering | EXAM:52 | `x = np.asarray(x, float) - np.mean(x)` | ACF requires mean-centering first; skipping it biases the autocorrelation |
| vectorization-einsum | EXAM:53 | `f = np.fft.rfft(x, 2 * n); a = np.fft.irfft(f * np.conj(f))[:n]` | autocorrelation via FFT (Wiener-Khinchin) not recognized; falls back to an O(n²) loop |
| sqrt-n-reasoning | EXAM:320 | `ess_theory = (1 - rho**2) / (1 + rho**2)` | AR(1) ESS/M formula from summing a geometric ACF not derived |
| kernel-recognition | EXAM:311 | `lag-1 autocorr = rho^2 exactly` | the Gibbs lag-1 = ρ² law not known; can't predict mixing cost |
| verify-special-case | EXAM:321 | `measured lag-1={lag1:.4f} (theory rho^2={rho**2:.4f})` | measured-vs-theory sanity check not performed |
| ∝-discipline | EXAM:353 | `w = target.pdf(x) / prop.pdf(x)` | importance weight = target/proposal density ratio not recognized |
| LOTUS | EXAM:354 | `est = np.sum(w * x ** 2) / np.sum(w)` | self-normalized IS estimator (weighted LOTUS) not constructed |
| gamma-beta-identity | EXAM:348 | `true E[theta^2] = {target.var():.1f} = nu/(nu-2)` | Student-t moment formula unknown; no ground truth to compare against |
| markov-chebyshev | EXAM:344 | `a proposal whose tails are too light for the target` | tail-heaviness → weight-variance-blowup reasoning absent; can't diagnose the collapse |
| sqrt-n-reasoning | EXAM:355 | `ef = ess_kong(w) / M  # module 09 alarm: the FRACTION` | Kong ESS (Σw)²/Σw² and reading the fraction rather than the count not understood |
| quadratic-form | EXAM:393 | `mse_mle = np.mean(np.sum(X ** 2, axis=1))` | risk as E‖θ̂−θ‖², i.e. a summed quadratic form, not framed |
| broadcasting-fancy-indexing | EXAM:394 | `norm2 = np.sum(X ** 2, axis=1, keepdims=True)` | scalar-per-row shrinkage needs keepdims broadcast; shape mismatch otherwise |
| indicators | EXAM:396 | `jsp = np.maximum(1 - (d - 2) / norm2, 0.0) * X` | positive-part truncation of the shrinkage factor not recognized |
| precision-weighted-mean | EXAM:411 | `w = tau2_hat / (tau2_hat + s2)` | shrinkage weight τ²/(τ²+σ²) as a precision blend not derived |
| law-of-total-variance | EXAM:410 | `tau2_hat = max(np.var(y_tr, ddof=1) - s2, 0.0)` | between-group variance = total − noise (variance decomposition, truncated at 0) not seen |
| precision-vs-covariance | EXAM:466 | `prec = Xd.T @ Xd / sig7 ** 2 + np.eye(2) / tau2` | posterior precision = likelihood precision + prior precision not assembled |
| matrix-solve-not-inverse | EXAM:467 | `post_m = np.linalg.solve(prec, Xd.T @ y7 / sig7 ** 2)` | solves the system instead of forming an inverse; naive inversion loses accuracy |
| complete-the-square-matrix | EXAM:464 | `alpha = sig7 ** 2 / tau2` (ridge == posterior mean) | ridge/Bayes equivalence rests on matrix completing-the-square; can't see why they match to machine precision |
| quadratic-form | EXAM:473 | `pred_sd = np.sqrt(np.einsum("ij,jk,ik->i", xs, Sig_n, xs) + sig7 ** 2)` | predictive variance = xᵀΣₙx quadratic form not recognized |
| vectorization-einsum | EXAM:473 | `np.einsum("ij,jk,ik->i", xs, Sig_n, xs)` | batched per-row xᵀΣx via einsum; would loop or misuse matmul |
| location-scale | EXAM:482 | `w = (nu + 1) / (nu + r ** 2 / s2)` | Student-t as a Gaussian scale-mixture → EM/IRLS down-weights not derived |
| matrix-solve-not-inverse | EXAM:484 | `b = np.linalg.solve(X.T @ WX, WX.T @ y)` | weighted normal equations solved, not inverted |
| broadcasting-fancy-indexing | EXAM:483 | `WX = X * w[:, None]` | per-row weight broadcast to scale rows; shape error without `[:, None]` |
| broadcasting-fancy-indexing | EXAM:459 | `y7c[[24, 26, 28]] += 10.0` | fancy-indexed in-place corruption of selected points not constructed |
| kernel-gram-matrix | EXAM:536 | `d = a[:, None] - b[None, :]; np.exp(-0.5 * (d / ell) ** 2)` | pairwise-difference Gram matrix via outer broadcast not built |
| jitter-pd | EXAM:540 | `+ sn ** 2 * np.eye(n8) + 1e-8 * np.eye(n8)` | jitter for positive-definiteness; Cholesky fails without it |
| cholesky-solve | EXAM:542-543 | `L = np.linalg.cholesky(K); a = np.linalg.solve(L.T, np.linalg.solve(L, y8))` | K⁻¹y by two triangular solves not recognized; slow/unstable inverse instead |
| quadratic-form | EXAM:543 | `fit = -0.5 * y8 @ a` | GP data-fit term −½yᵀK⁻¹y not identified |
| log-det-cholesky | EXAM:544 | `occam = -np.sum(np.log(np.diag(L)))  # -0.5 log\|K\|` | log-determinant via sum of log Cholesky diagonals not known; naive det under/overflows |
| log-products-to-sums | EXAM:545 | `return fit + occam - 0.5 * n8 * np.log(2 * np.pi)` | log marginal likelihood as a sum of log-terms not assembled |
| schur-woodbury | EXAM:564 | `Kss - Ks @ Kinv @ Ks.T` | GP posterior covariance = Schur complement of the joint kernel not recognized |
| schur-woodbury | EXAM:70-71 | `K = S12 @ np.linalg.inv(S22); ... S11 - K @ S21` | MVN block conditional (toolkit helper) is a Schur complement; opaque without it |
| precision-weighted-mean | EXAM:618 | `K = prior_var / (prior_var + r9)` | Kalman gain = prior/(prior+noise) shrinkage weight not seen |
| precision-vs-covariance | EXAM:620 | `cj_var = 1 / (1 / prior_var + 1 / r9)  # conjugate: precisions add` | Normal update adds precisions; would wrongly average variances |
| precision-weighted-mean | EXAM:621 | `cj_mean = cj_var * (prior_mean / prior_var + obs / r9)` | precision-weighted posterior mean formula not recalled |
| law-of-total-variance | EXAM:629 | `Pm = P + q9` (predict = marginalize) | variance inflation by process noise q when marginalizing a random-walk step not seen |
| verify-special-case | EXAM:636-640 | `Pss = 1.0; for _ in range(1000): ... Pss = (1 - Kss) * Pm` | steady state by iterating the Riccati recursion to a fixed point not conceived |
| sqrt-n-reasoning | EXAM:669 | `se = np.sqrt(2 * sd_obs ** 2 / n_plan)` | SE of a difference in means = √(2σ²/n) not derived |
| standardization-centering | EXAM:673 | `stats.norm.cdf(delta / se - zc) + stats.norm.cdf(-delta / se - zc)` | two-sided power as two standardized tail probabilities not assembled |
| jensen | EXAM:665 | `Jensen's inequality bites the S-shaped power curve` | can't predict the direction: assurance = E[power(δ)] < power(E[δ]) on the concave shoulder |
| LOTUS | EXAM:677 | `power(ds).mean()  # assurance (power averaged over prior)` | assurance as a Monte Carlo prior-expectation of the power function not conceived |
| indicators | EXAM:681 | `EVPI = np.mean(np.maximum(-ds, 0.0))` | expected opportunity loss as the mean of a positive-part regret not built |
| precision-vs-covariance | EXAM:682 | `post_var = 1 / (1 / s0 ** 2 + 1 / se ** 2)` | posterior precision = prior + data precision not formed |
| precision-weighted-mean | EXAM:684 | `post_mean = post_var * (mu0 / s0 ** 2 + dhat / se ** 2)` | Gaussian posterior mean as a precision-weighted blend not recalled |
| indicators | EXAM:685 | `val_study = np.where(post_mean > 0, ds, 0.0).mean()` | value-of-a-decision as an expectation over the decision indicator not seen |
| logit-softmax-domain | EXAM:717 | `T = (rng.random(n11) < expit(0.8 * U)).astype(float)` | logistic propensity → Bernoulli via sigmoid-thresholded uniform not recognized |
| projection-hat-matrix | EXAM:723-724 | `Xr = np.column_stack([np.ones(n11), T] + extra); ... lstsq(Xr, Y ...)[0][1]` | OLS as a projection with the T-coefficient read off; adding columns changes the projection (collider bias mechanism) |
| ∝-discipline | EXAM:749 | `mu1 = np.sum(Ts * Ys / ps) / np.sum(Ts / ps)  # Hajek self-normalized IPW` | self-normalized inverse-propensity weighting not recognized as SNIS |
| broadcasting-fancy-indexing | EXAM:751 | `ess_tr = ess_kong((Ts / ps)[Ts == 1])` | boolean-mask subsetting to the treated arm before ESS; wrong diagnostic otherwise |
| location-scale | EXAM:787 | `scale = s * np.sqrt(1 + 1 / n12)` | predictive scale √(1+1/n) for a new observation (vs √(1/n) for the mean) not derived |
| standardization-centering | EXAM:790 | `cov_marg = np.mean(np.abs(ynew - ybar) <= tq * scale)` | pivot (ynew−ȳ)/scale being t-distributed not recognized; wrong quantile used |
| marginalization-integral | EXAM:782 | `marginalize sigma^2 (Student-t predictive) vs plug-in normal` | integrating out σ² yields a t, not a normal; plug-in undercoverage not anticipated |
| verify-special-case | EXAM:794 | `(ratio {Wm/Wp:.3f} = t5/z {tq/zq:.3f})` | width inflation = t₅/z quantile-ratio identity not checked |
| order-statistics-quantile | EXAM:799 | `qhat = np.quantile(cal, np.ceil((200 + 1) * 0.9) / 200, method="higher")` | conformal finite-sample level ⌈(n+1)α⌉/n with the higher-order statistic not known; naive quantile undercovers |
| indicators | EXAM:801 | `empirical coverage={np.mean(np.abs(test) <= qhat):.4f}` | coverage as the mean of a containment indicator not built |

## Frequency-ranked summary

Total instances: **462** across 60 distinct skills (modules 14–26 + EXAM).

| rank | skill | count | modules |
|---|---|---|---|
| 1 | verify-special-case | 28 | 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, EXAM |
| 2 | broadcasting-fancy-indexing | 26 | 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, EXAM |
| 3 | indicators | 26 | 14, 15, 17, 18, 19, 21, 22, 23, 24, EXAM |
| 4 | gamma-beta-identity | 21 | 14, 17, 18, 19, 20, 21, 22, 25, 26, EXAM |
| 5 | tower-rule-total-variance | 21 | 14, 16, 17, 18, 19, 22, 23, 24, 25, 26, EXAM |
| 6 | marginalization-integral | 19 | 14, 15, 16, 17, 18, 20, 21, 23, 24, 25, 26, EXAM |
| 7 | precision-vs-covariance | 17 | 14, 15, 16, 18, 19, 20, 21, 23, 25, EXAM |
| 8 | precision-weighted-mean | 17 | 14, 16, 17, 18, 19, 21, 23, 25, EXAM |
| 9 | sqrt-n-reasoning | 17 | 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, EXAM |
| 10 | location-scale | 16 | 14, 15, 16, 17, 19, 20, 21, 25, 26, EXAM |
| 11 | standardization-centering | 15 | 14, 15, 16, 17, 20, 22, 23, 25, EXAM |
| 12 | quadratic-form | 14 | 14, 15, 17, 18, 20, 21, 23, 24, EXAM |
| 13 | argmax-invariance | 13 | 15, 17, 18, 19, 20, 21, 22, 25, EXAM |
| 14 | log-products-to-sums | 13 | 14, 15, 18, 19, 21, 22, 23, 25, EXAM |
| 15 | kernel-recognition | 12 | 14, 18, 19, 20, 21, 23, EXAM |
| 16 | lotus | 10 | 15, 17, 18, 22, 23, 24, EXAM |
| 17 | vectorization-einsum | 10 | 14, 15, 16, 19, 20, EXAM |
| 18 | matrix-solve-not-inverse | 9 | 14, 17, 18, 21, 24, EXAM |
| 19 | ∝-discipline | 9 | 14, 15, 17, 18, 19, EXAM |
| 20 | jensen | 8 | 15, 17, 20, 22, 23, EXAM |
| 21 | log-det-cholesky | 8 | 14, 17, 20, 21, 23, EXAM |
| 22 | schur-woodbury | 8 | 14, 20, 21, 23, EXAM |
| 23 | change-of-variables-jacobian | 7 | 14, 20, 21, EXAM |
| 24 | complete-the-square-matrix | 7 | 14, 17, 19, 21, 23, EXAM |
| 25 | kernel-gram-matrix | 7 | 17, 20, 23, EXAM |
| 26 | logit-softmax-domain | 7 | 15, 23, 24, 25, EXAM |
| 27 | subtract-max | 7 | 15, 18, 19, 21, 23, 25 |
| 28 | floating-point-hygiene | 6 | 20, 23, 24, 25, EXAM |
| 29 | linearity-of-expectation | 6 | 19, 20, 22, 23, 24 |
| 30 | logsumexp | 6 | 15, 17, 19, 25 |
| 31 | sum-of-squares-decomp | 6 | 14, 17, 19, 25, 26, EXAM |
| 32 | complete-the-square-scalar | 5 | 19, 21, 23, 25 |
| 33 | jitter-pd | 5 | 20, 24, 25, EXAM |
| 34 | taylor-2nd-order | 5 | 15, 20, 23, EXAM |
| 35 | cholesky-solve | 4 | 14, 20, EXAM |
| 36 | expand-and-collect | 4 | 14, 21, 24, EXAM |
| 37 | markov-chebyshev | 4 | 18, 21, 23, EXAM |
| 38 | non-centered-reparam | 4 | 16, 18, 25 |
| 39 | pinv-min-norm | 4 | 14, 23, 25 |
| 40 | projection-hat-matrix | 4 | 18, 24, 25, EXAM |
| 41 | algebraic-rearrangement | 3 | 21, 22, 23 |
| 42 | union-triangle-bound | 3 | 22, 23, EXAM |
| 43 | differentiate-under-integral | 2 | 20, 23 |
| 44 | eigen-ellipse | 2 | 21 |
| 45 | stick-breaking | 2 | 18, 19 |
| 46 | add-and-subtract | 1 | 18 |
| 47 | cumulative-link | 1 | 15 |
| 48 | dominant-term-asymptotics | 1 | 17 |
| 49 | exchangeability | 1 | 26 |
| 50 | importance-weights | 1 | 24 |
| 51 | jensen-egx-trap | 1 | 14 |
| 52 | log1p-approx | 1 | 19 |
| 53 | mode-vs-mean | 1 | 15 |
| 54 | moment-matching-variance | 1 | 16 |
| 55 | order-statistics-quantile | 1 | EXAM |
| 56 | probit-logistic-approx | 1 | 15 |
| 57 | score-function | 1 | 25 |
| 58 | self-normalized-is | 1 | 24 |
| 59 | unbiased-variance | 1 | 26 |
| 60 | unconstrained-reparam | 1 | 16 |

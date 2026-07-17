# Mined prerequisites: modules 00–13

Every mathematical/computational micro-skill the text **uses without teaching** in
`modules/00-four-lines.md` … `modules/13-laplace-em-vi.md`. Each row: the skill (short
canonical name), where it is silently used (module:approx-line), the exact step, and what a
reader missing the skill experiences. Line numbers are approximate (from a fixed read of the
2026-07-12 versions). A frequency-ranked summary, with raw skill names normalized into
canonical families, follows the table.

## Instance table

| skill | module:line | quoted step | what-breaks-without-it |
|---|---|---|---|
| precision=1/var | 00:66 | `np.linalg.solve(X.T @ X + alpha * np.eye(p), X.T @ y)` | stuck: why is regularized normal equation the same as a Gaussian posterior mean? |
| complete-the-square (matrix) | 00:69 | `Posterior precision = X'X/sigma^2 + I/tau^2 ; mean solves it against X'y/sigma^2` | stuck: where did "posterior precision = sum of precisions" come from? never derived |
| drop-const-∝ | 00:70 | `With tau^2 = sigma^2 / alpha, the sigma^2 cancels and alpha = sigma^2/tau^2` | stuck: why does σ² cancel so ridge's single α absorbs two parameters? |
| quadratic-form | 00:51 | `(X^T X + 10 I)^{-1} X^T y` | stuck: reading a matrix inverse solve as "minimize a penalized quadratic" |
| MAP=mode-of-Gaussian | 00:92 | `minimizing \|y - X\beta\|^2 + \alpha\|\beta\|^2 is finding the mode (here also the mean)` | stuck: why does an argmin equal a posterior mean? (mean=mode only for Gaussian, unstated) |
| vectorize/broadcast | 00:72 | `X.T @ X / sigma^2 + np.eye(p) / tau2` | stuck: scalar-divides-matrix and identity-add broadcast silently |
| seed-discipline | 00:31 | `rng = np.random.default_rng(SEED)` | non-reproducible output; determinism check fails |
| expectation-of-indicator | 00:112 | `p_pos_D = sens * prev` | stuck: why is P(+,D) just a product? (joint = prior×likelihood, indicator mean = prob) |
| Bayes-as-ratio-of-joints | 00:114 | `PPV = p_pos_D / (p_pos_D + p_pos_notD)` | stuck: denominator is the marginal p(+) via law of total probability, unstated |
| odds×LR (log-odds algebra) | 00:122 | `prior_odds * LR_pos ... = posterior odds` | stuck: why does Bayes reduce to a single multiplication in odds space? |
| inner-product-as-expectation | 00:138 | `E_treat = post @ L["treat"]` | stuck: a dot product is silently E[loss] = Σ p·L |
| LOTUS / marginalize-predictive | 00:149 | `p_T2pos = PPV * sens + (1 - PPV) * (1 - spec)` | stuck: why sum products of posterior×likelihood? (line-3 marginalization unstated) |
| recognize-kernel (Beta) | 00:182 | `posterior is Beta(8,4), mean 8/12` | stuck: how did Beta(1,1)+7/10 heads become Beta(8,4)? conjugacy skipped |
| posterior-mean=predictive | 00:190 | `post_mean = a / (a + b) # posterior predictive P(next head)` | stuck: why is E[θ] the probability of the next head, not the MLE? |
| E[Bernoulli(θ)]=θ then tower | 00:196 | `Averaging over theta IS the posterior predictive (line 3), so E[win] = post_mean` | stuck: E over θ then over flip collapses to E[θ] — tower rule unstated |
| sampling: threshold-uniform | 00:199 | `win = (bet.random(N) < theta).astype(float)` | stuck: why does U<θ simulate Bernoulli(θ)? |
| vectorize/broadcast | 00:198 | `theta = bet.beta(a, b, N)` then elementwise `< theta` | stuck: million draws compared elementwise, no loop |
| normalize-discrete | 00:137 | `post = np.array([PPV, 1 - PPV])` | stuck: posterior must sum to 1; the complement is implicit |
| odds→prob map | 00:143 | `return o / (1 + o)` | stuck: converting odds back to probability, unexplained |
| MSE=bias²+var (implicit) | 00:302 | `does \|\hat\beta\| grow or shrink?` | stuck: shrinkage as bias trade is assumed background |
| Dutch-book / linear-algebra payoff | 01:67 | `payoff = np.eye(3) - q[:, None]` | stuck: identity minus broadcast column encodes "win 1 if state occurs, minus price" |
| vectorize/broadcast | 01:67 | `np.eye(3) - q[:, None]` | stuck: (3,3) minus (3,1) column broadcast is silent |
| column-sum reduction | 01:72 | `coltot = payoff.sum(axis=0)` | stuck: axis=0 sums each outcome column — which axis is which? |
| expectation-of-indicator | 01:86 | `y = (rng.uniform(0, 1, Ncal) < p).astype(int)` | stuck: threshold-uniform makes an outcome ~Bernoulli(p) |
| bin/digitize + weighted-average | 01:97 | `ece += m.mean() * abs(f[m].mean() - y[m].mean())` | stuck: ECE is a frequency-weighted mean gap; the weighting m.mean() is unexplained |
| boolean-mask indexing | 01:96 | `m = idx == b ... f[m].mean()` | stuck: masking a vector to compute per-bin means |
| location-scale stretch | 01:87 | `s = np.clip(0.5 + 1.6 * (p - 0.5), 0, 1)` | stuck: affine "push away from 0.5" as an overconfidence transform |
| Var of Beta (closed form) | 01:150 | `varT = a_ * b_ / ((a_ + b_) ** 2 * (a_ + b_ + 1))` | stuck: memorized Beta variance formula dropped in with no derivation |
| tower-rule / cond. independence | 01:137 | `E[XiXj] = E[ E[Xi|Θ] E[Xj|Θ] ] = E[Θ²]` | stuck: why does conditioning let the product of expectations appear? |
| law-of-total-covariance | 01:139 | `Cov[X_i, X_j] = E[Θ²] - E[Θ]² = Var[Θ]` | stuck: the conditional-covariance term is silently killed by cond. independence |
| Corr=Cov/Var | 01:152 | `corr_th = varT / 0.25 # Cov/Var; marginal Var=0.25` | stuck: where does 0.25 (Var of Bernoulli(1/2)) come from? |
| cumsum → running average | 01:155 | `runfreq = X.cumsum(axis=1, dtype=float) / np.arange(1, Nrep + 1)` | stuck: cumsum divided by index vector is a vectorized running mean |
| float-dtype hygiene | 01:155 | `dtype=float: no int8 overflow` | silent int8 overflow corrupts the cumulative sum |
| broadcast comparison (outer) | 01:148 | `(rng.uniform(size=(R, Nrep)) < theta[:, None])` | stuck: (R,Nrep) array compared to (R,1) column to give per-replicate Bernoulli |
| argsort-as-shuffle | 01:194 | `urn[np.argsort(rng.random((R2, Nurn)), axis=1)]` | stuck: argsort of uniforms is a vectorized row-wise permutation (sampling w/o replacement) |
| bitwise-and on indicators | 01:154 | `p11 = (X[:, 0] & X[:, 1]).mean()` | stuck: & on 0/1 arrays computes P(both=1) as a mean |
| Cov identity sign reasoning | 01:188 | `-1/(N-1) ... any conditionally-iid sequence has Cov = Var[Θ] ≥ 0` | stuck: why is negative covariance a *proof* of non-mixture? |
| log-product→sum | 01:242 | `logp += np.log(red / tot)` accumulating a sequence probability | stuck: why build the probability in log space instead of multiplying? |
| Beta-function normalizer | 01:251 | `np.exp(betaln(a + k, b + n - k) - betaln(a, b))` | stuck: B(a+k,b+n−k)/B(a,b) is the Beta-Binomial marginal, via Gamma/Beta identity |
| logsumexp-style stability (betaln) | 01:251 | `betaln(...) - betaln(...)` then `np.exp` | stuck: why subtract log-Betas before exponentiating? overflow avoidance |
| rule-of-succession (posterior mean) | 01:306 | `p_next = (a + k) / (a + b + n)` | stuck: predictive = (a+k)/(a+b+n) dropped in as "the Pólya fraction" |
| lag-autocorrelation | 01:341 | `lag1 = lambda z: np.corrcoef(z[:-1], z[1:])[0, 1]` | stuck: correlating a series with its shift measures dependence |
| AR(1) recursion | 01:338 | `ar[t] = phi * ar[t - 1] + eps[t]` | stuck: a stateful recurrence, not vectorizable, generates dependence |
| joint = prior×likelihood (outer) | 02:62 | `joint = prior[:, None] * np.asarray(likelihood, float)` | stuck: (H,1)×(H,O) broadcast builds the full joint table |
| condition = slice+renormalize | 02:64 | `col = joint[:, obs]; return col / col.sum()` | stuck: "keep observed column, divide by its sum" IS Bayes' theorem |
| marginal-likelihood=col.sum | 02:64 | `divide by p(o*)` (the column sum) | stuck: the normalizer is the evidence p(o*)=Σ_h p(h)p(o*|h), unstated |
| odds×LR | 02:96 | `post_odds = prior_odds * LR` | stuck: Bayes as one multiplication in odds space |
| solve PPV=0.5 balance point | 02:102 | `p_half = (1 - spec) / (sens + (1 - spec))` | stuck: algebra solving posterior odds = 1 for prevalence, skipped |
| log-space PPV curve (vectorized) | 02:106 | `pv = np.logspace(-4, 0, 400)` then elementwise PPV | stuck: whole curve computed by broadcasting over a log grid |
| Monte Carlo SE | 02:149 | `se = np.sqrt(ppv_sim * (1 - ppv_sim) / n_pos)` | stuck: binomial-proportion standard error formula dropped in |
| np.where vectorized branch | 02:144 | `tests_pos = np.where(has_disease, gen.random(N)<sens, gen.random(N)<(1-spec))` | stuck: branchless per-element conditional sampling |
| sequential=batch (assoc. of ×) | 02:168 | `lik_two = np.array([[sens**2], [(1 - spec)**2]])` | stuck: why does squaring the likelihood equal two updates? cond. independence |
| log-odds add | 02:188 | `ℓ_posterior = ℓ_prior + Σ_i log LR_i` | stuck: products become sums under log; the additive-evidence claim |
| sigmoid = odds→prob | 02:196 | `probs = 1 / (1 + 10.0**(-log10_odds))` | stuck: the inverse-logit link appears without being named as sigmoid |
| linear-in-logits | 02:195 | `log10_odds = np.log10(prior_odds) + ks * log10_LR` | stuck: why is log-odds linear in count of positives? |
| log-C via gammaln | 02:225 | `out = gammaln(a + 1) - gammaln(b + 1) - gammaln(a - b + 1)` | stuck: log binomial coefficient via log-Gamma, no derivation |
| subtract-max-before-exp | 02:234 | `lik = np.exp(loglik - loglik[ok].max())` | stuck: why subtract the max before exp? underflow/overflow hygiene |
| −inf as zero-weight sentinel | 02:232 | `loglik = np.full(Nmax, -np.inf) # P=0 off support` | stuck: −inf exponentiates to 0, encoding support constraints |
| hypergeometric-max likelihood | 02:218 | `P(M=m|N)=binom(m-1,n-1)/binom(N,n)` | stuck: sampling-without-replacement max distribution asserted, not derived |
| posterior mean = Σ N·p | 02:240 | `post_mean = (N * post).sum()` | stuck: E[N|data] as a weighted sum over the discrete posterior |
| suffix-sum via reversed cumsum | 02:283 | `suf_w = np.cumsum(w[::-1])[::-1]` | stuck: reverse-cumsum-reverse computes Σ_{N≥m} in one pass |
| inverse-CDF-sampling | 02:290 | `m[np.searchsorted(np.cumsum(p), gen.random(reps), ...)]` | stuck: searchsorted on a cumulative pmf is discrete inverse-transform sampling |
| normalize-discrete | 02:289 | `p = np.exp(...); p /= p.sum()` | stuck: unnormalized weights turned into a pmf |
| MSE=bias²+variance | 02:335 | `MSE = bias² + variance, a biased rule ... can beat it` | stuck: the decomposition is used as the crux but assumed known |
| RMSE via mean of squares | 02:309 | `np.sqrt(((eu - Nt)**2).mean())` | stuck: root-mean-square error idiom over replicates |
| closed-form E[max] check | 02:297 | `formula {n*1001/(n+1)}` | stuck: E[max]=n(N+1)/(n+1) for uniform order stats, unproven |
| protocol-dependent likelihood | 02:373 | `likA = [[0.5],[0.0],[1.0]]` vs `likB = [[0.5],[0.0],[0.5]]` | stuck: same event, different likelihood column — where do these numbers come from? |
| Poisson-count + uniform order stats | 03:71 | `S = np.sort(rng.uniform(0.0, T, size=N))` | stuck: why does "count then place uniformly" build a Poisson process? |
| diff = inter-arrival gaps | 03:77 | `gaps.append(np.diff(S))` | stuck: np.diff of sorted times gives the gaps whose law is Exp(λ) |
| sum-of-Exp = Gamma | 03:52 | `S_k = (sum of k gaps) is Gamma(k, λ)` | stuck: a sum of k iid Exponentials is Gamma — asserted, not shown |
| marginalize sub-window (line 3) | 03:54 | `p(N_{[0,s]}=m) = Σ_N p(...|N) p(N)` collapses to Poisson(λs) | stuck: the marginalization algebra collapsing to Poisson is skipped |
| Poisson mean=variance signature | 03:87 | `mean 9.986 and variance 10.087 — Poisson signature` | stuck: using mean≈var as a diagnostic assumes the Poisson identity |
| scipy rate↔scale trap | 03:81 | `stats.expon(scale=1 / lam)` / `stats.gamma(a=k, scale=1/lam)` | silent parameterization bug: rate vs scale = 1/rate |
| KS statistic as fit check | 03:81 | `stats.kstest(gaps, ...).statistic` | stuck: KS distance used as "0=perfect match" without definition |
| cumsum → running mean | 03:145 | `return np.cumsum(x) / np.arange(1, x.size + 1)` | stuck: vectorized running average idiom |
| IQR as robust scale | 03:149 | `q3 - q1` used because "scale that survives heavy tails" | stuck: why IQR not variance? tail-robustness assumed |
| characteristic-function argument | 03:168 | `φ_{X̄}(t) = φ(t/n)ⁿ = e^{−|t|}` | stuck: CF of a mean is product of scaled CFs — machinery assumed |
| divergent-integral reasoning | 03:164 | `∫ x/(π(1+x²)) dx diverges` | stuck: why does the Cauchy have no mean? integral-divergence unshown |
| variance of Student-t | 03:170 | `variance is ν/(ν−2), finite only when ν > 2` | stuck: t-variance formula and its finiteness cutoff dropped in |
| ratio-of-normals=Cauchy | 03:134 | `ratio of two independent N(0,1)s` | stuck: change-of-variables giving Cauchy is asserted |
| −Σ p log p (entropy) | 03:212 | `return float(-np.sum(p * np.log2(p)))` | stuck: entropy formula and the p>0 guard, unexplained |
| filter zeros before log | 03:212 | `p = p[p > 0]` | stuck: 0·log0 handled by dropping zeros to avoid nan |
| KL = Xent − H | 03:229 | `entropy_bits(biased) + kl_bits(...) = 1.000` | stuck: the decomposition cross-entropy = entropy + KL as an identity |
| Jensen (which-way) | 03:234 | `KL = E_p[−log(q/p)] ≥ −log E_p[q/p]` | stuck: which direction does Jensen go? convexity of −log unstated |
| collapse E to Σ q(x) | 03:234 | `−log Σ_x p(x)·q(x)/p(x) = −log Σ_x q(x) = −log 1` | stuck: the p(x) cancels and Σq=1 — algebra skipped |
| log base bits/nats | 03:200 | `Base-2 logs give bits; natural logs give nats` | numbers drift by ln2 if base is mixed |
| calculus-of-variations Lagrangian | 03:274 | `functional derivative in p(x), gives −log p(x) − 1 − λ₀ + Σ λ_k T_k(x) = 0` | stuck: differentiating a functional wrt p(x) is assumed known |
| exp-of-linear kernel | 03:276 | `p(x) ∝ exp(Σ_k λ_k T_k(x))` | stuck: recognizing max-ent solutions as exponential-family kernels |
| recognize-kernel (Gaussian) | 03:281 | `exp(λ₁x + λ₂x²) — a quadratic in the exponent, i.e. a Gaussian` | stuck: quadratic-in-exponent ⇒ Normal, completing-the-square implied |
| convex-dual / moment-matching | 03:299 | `dual(theta) = logsumexp(theta @ Tm) - theta @ b` | stuck: why is the log-partition minus ⟨θ,b⟩ the right convex objective? |
| gradient = moment residual | 03:301 | `dual_grad = Tm @ p_of(theta) - b` | stuck: ∇(log-partition) = E[T]; the exp-family moment identity, unstated |
| logsumexp normalization | 03:296 | `np.exp(z - logsumexp(z))` | stuck: subtract logsumexp to normalize stably in log space |
| KL as convergence metric | 03:313 | `KL = {kl_nats(p_exp, exp_target)}` | stuck: KL≈1e-16 read as "identical" assumes KL=0 iff equal |
| softmax = max-ent categorical | 03:349 | `z = s / temp; z -= z.max(); e = np.exp(z); return e / e.sum()` | stuck: softmax derived as constrained max-entropy, temp = 1/multiplier |
| subtract-max-before-exp | 03:347 | `z -= z.max()` inside softmax | stuck: shift-invariance of softmax for overflow safety, unexplained |
| argmax-invariance / T→0 limit | 03:340 | `T → 0 pins all mass on the top score (argmax, zero entropy)` | stuck: why temperature limits give argmax vs uniform |
| Poisson closure (superposition/thinning) | 03:396 | `merged, thinnedA = A + B, rng.binomial(A, 0.2)` | stuck: sum of Poissons is Poisson; binomial-thinned Poisson is Poisson — asserted |
| var/mean=1 diagnostic | 03:397 | `merged.var()/merged.mean() ... (Poisson=1)` | stuck: using dispersion ratio to confirm the family |
| geometric kernel from mean constraint | 03:431 | `geom = (1 - r) * r**kk` with `r = mean/(1+mean)` | stuck: max-ent-on-ℕ ⇒ Geometric p_k∝e^{λk}; the r↔mean map skipped |
| label-entropy = loss floor | 03:457 | `label entropy H(p) ... = min cross-entropy (q=p)` | stuck: why validation loss plateaus above 0 = irreducible H(p), via Xent=H+KL |
| drop-const-∝ | 04:10 | `p(θ∣y)∝p(y∣θ)p(θ)` | doesn't see the normalizer was dropped; "where did the denominator go?" |
| likelihood-as-fn-of-θ | 04:44 | `L(θ∣y) = f(y∣θ)` | reads same formula as a density in y; misses the flipped-variable reading |
| log-product→sum | 04:58 | `loglik = s*np.log(grid) + (n - s)*np.log(1 - grid)` | can't see θ^s(1−θ)^{n−s} became a sum of logs |
| recognize-kernel | 04:47 | `L(θ) = θ^{s}(1-θ)^{n-s}` | stuck: why does the product of Bernoulli terms collapse to this |
| subtract-max-before-exp | 04:59 | `L = np.exp(loglik - loglik.max())` | overflow/why-subtract-max; misses logsumexp-style stabilization |
| 1/√n-width | 04:71 | `the peak *width* shrinks like 1/√n` | can't justify why width scales this way |
| factorization-recognize | 04:78 | `f(y∣θ) = g(T(y)∣θ)h(y)` | doesn't see how the θ-free factor cancels in the posterior |
| drop-const-∝ | 04:79 | `p(θ∣y)∝f(y∣θ)p(θ) ∝ g(T(y)∣θ)p(θ)` | misses that h(y) cancels because it's θ-free |
| sufficient-stat-collect | 04:81 | `f(y∣θ)=θ^{∑y_i}(1-θ)^{n-∑y_i}` already factored with `T=∑y_i` | stuck: why is ∑y_i the whole message |
| vectorize/broadcast | 04:94 | `X = rng.binomial(1, theta, size=(400_000, n_bits))` | can't see the batched-simulation idiom |
| indicator-condition | 04:95 | `keep = X[X.sum(1) == s_fix]` | doesn't read boolean-mask conditioning on the sufficient stat |
| bit-encode-count | 04:96 | `np.unique(keep @ powers, return_counts=True)` | mystified how a dot with `1<<arange` codes each pattern |
| normalize-discrete | 04:97 | `freq = counts / counts.sum()` | doesn't see counts→probabilities |
| sum-of-squares-decomp | 04:111 | `S = ((data - xbar)**2).sum()  # S = Σx² − nx̄²` | can't connect S to Σx², Σx² identity |
| sufficient-stat-collect | 04:110 | `n = len(data); xbar = data.mean(); S = ...` | misses that (n,Σx,Σx²) is all the Normal sees |
| expfam-match | 04:129 | `f(x∣θ) = h(x)c(θ)exp(∑ w_i(θ)t_i(x))` | can't map a density onto the exp-family template |
| expfam-natural-form | 04:131 | `p(x∣η) = h(x)exp(η^⊤T(x) − A(η))` | doesn't recognize canonical form / natural parameter |
| Gamma/Beta-normalizer | 04:131 | `A(η)=log∫ h(x)e^{η^⊤T(x)}dx` | stuck: why the log-partition is the normalizer |
| logit-natural-param | 04:136 | Bernoulli natural parameter `log θ/(1−θ)` | can't derive logit as η from the kernel |
| differentiate-under-∫ | 04:142 | `A'(η) = E[T(X)], A''(η) = Var[T(X)]` | doesn't see cumulants come from differentiating log-partition |
| verify-special-case | 04:150 | `Aprime, Adprime = np.exp(eta), np.exp(eta)` | misses A'=A''=e^η=λ as Poisson mean=var |
| score-as-∂log-lik | 04:162 | `U(θ) = ∂/∂θ log f(X∣θ)` | can't form the score / why slope of log-lik matters |
| differentiate-under-∫ | 04:163 | `differentiate ∫f dx=1 under the integral` | doesn't grasp swap of d/dθ and ∫ giving mean-zero score |
| variance=neg-E-curvature | 04:164 | `I(θ) = Var[U] = −E[∂²/∂θ² log f]` | stuck: why variance-of-slope equals expected negative curvature |
| log-product→sum | 04:165 | `log f = x log θ + (1-x)log(1-θ)` | can't split Bernoulli log-density |
| set-derivative=0-algebra | 04:165 | `a line of algebra gives I(θ)=1/(θ(1-θ))` | can't reproduce the skipped score-variance algebra |
| vectorize/broadcast | 04:171 | `score = xb/theta0 - (1 - xb)/(1 - theta0)` | doesn't read per-draw score computed array-wise |
| info-additive | 04:177 | `their variances add and I_n(θ)=n I(θ)` | why independent scores' variances add |
| log-product→sum | 04:185 | `ll = s*np.log(grid) + (n - s)*np.log(1 - grid)` | can't see log-likelihood as a sum |
| observed-info=−ℓ'' | 04:186 | `obs_info = n / (thhat*(1 - thhat))  # −ℓ''(θ̂) = n·I(θ̂)` | doesn't link curvature to n·I(θ̂) |
| sf-for-tail | 04:220 | `stats.binom(12, theta_null).sf(8)  # P(X ≥ 9)` | why sf(8) gives P(X≥9), off-by-one confusion |
| combinatorial-sum | 04:223 | `sum(comb(12, k) for k in range(9, 13)) / 2**12` | can't hand-derive the binomial tail |
| negbin-tail-hand | 04:224 | `1 - sum(comb(k + 2, 2) * 0.5**k * 0.5**3 ...)` | mystified by the NegBin pmf/complement construction |
| proportional-likelihood | 04:234 | `the two likelihoods are proportional` | doesn't see the binomial coefficients are constants in θ |
| drop-const-∝ | 04:233 | `L_F(θ) = C(12,9)θ^9(1-θ)^3` vs `C(11,9)…` | can't see the coefficient is an irrelevant constant in θ |
| conjugate-add-stat | 04:244 | `a_post, b_post = 1 + 9, 1 + 3` | stuck: why prior params just add successes/failures |
| recognize-kernel | 04:256 | `Lg = grid**9 * (1 - grid)**3` is a Beta kernel | doesn't recognize θ⁹(1−θ)³ as Beta(10,4) |
| censored-likelihood-S(c) | 04:282 | `a censored point contributes S(c∣θ)` | thinks every observation contributes a density |
| log-product→sum | 04:289 | `-(np.sum(np.log(lam) - lam*obs) - lam*c)` | can't read the summed log-lik with the −λc survival term |
| set-derivative=0 | 04:286 | `MLE = #deaths / total time-at-risk` | can't derive the exponential-MLE closed form |
| ancillary-recognize | 04:298 | `residuals x_i−x̄ are ancillary` | doesn't see why shifting θ leaves residuals fixed |
| corr-as-independence-check | 04:303 | `np.corrcoef(xbar, Xs[:, 0] - xbar)[0, 1]` | misses that ≈0 correlation is fingerprint of Basu independence |
| NLL=loss-dictionary | 04:313 | `arg min_θ (1/n)∑[−log p(y_i∣θ)]` | doesn't see MLE as average-negative-log-lik minimization |
| argmin-invariant-under-log | 04:313 | `maximum likelihood is empirical risk minimization under log loss` | can't equate argmax-lik with argmin-NLL |
| set-derivative=0 (numeric) | 04:325 | `minimize_scalar(bce, bounds=..., method="bounded")` | doesn't see optimizer standing in for the MLE derivative |
| Beta-posterior-sd | 04:355 | `stats.beta(a, b).std()` scales like `1/√n` | misses the √10 tightening lesson |
| drop-const-∝ | 05:10 | `p(θ∣y)∝p(y∣θ)p(θ)` | doesn't see the normalizer dropped |
| conjugate-add-stat | 05:57 | `a_n, b_n = a0 + s, b0 + f` | stuck: why updating is just adding counts |
| predictive=E[θ] | 05:58 | `pred_next = a_n / (a_n + b_n)  # posterior predictive = E[theta]` | doesn't see Bernoulli predictive equals posterior mean |
| pseudo-count-reading | 05:78 | `Beta(1+2, 1+0) means 3 effective successes and 1 effective failure` | can't read prior as pseudo-data |
| expfam-conjugacy-derive | 05:85 | `p(η∣τ0,n0) ∝ exp(η^⊤τ0 − n0 A(η))` | mystified how a prior in natural form gives closure |
| conjugate-add-stat | 05:87 | `exp(η^⊤(τ0 + S) − (n0+n)A(η))` | misses that multiplying just adds sufficient stats |
| precision=1/var | 05:102 | `prec_post = 1.0/tau2 + n/sigma2  # precisions add` | doesn't know precisions (not variances) add |
| precision-weighted-avg | 05:103 | `m_post = (m0/tau2 + data.sum()/sigma2) / prec_post` | can't read the precision-weighted mean |
| recognize-kernel | 05:130 | `θ^{(a+s)-1}(1-θ)^{(b+f)-1} = Beta(a+s, b+f)` | stuck: why the product is again a Beta |
| convex-combination-decomp | 05:132 | `(a+s)/(a+b+n) = w_prior·m0 + w_data·θ̂` | can't split the mean into a weighted average |
| pseudo-count-reading | 05:134 | `The prior is literally worth κ = a+b observations` | misses κ as pseudo-sample-size |
| vectorize/broadcast | 05:150 | `s = int(stream[:n].sum())` prefixes | doesn't read the streaming-prefix idiom |
| complete-the-square | 05:174 | `completing the square (expand, collect the θ² and θ terms, and read off the Gaussian)` | can't do the skipped quadratic-collection algebra |
| precision=1/var | 05:175 | `1/τ_n² = 1/τ² + n/σ²` | doesn't know posterior precision is sum of precisions |
| precision-weighted-avg | 05:175 | `m_n = (m0/τ² + n ȳ/σ²)/(1/τ² + n/σ²)` | can't read the weighted-average form |
| pseudo-sample-size-ratio | 05:176 | `κ0 = σ²/τ²` plays role of prior pseudo-sample-size | misses σ²/τ² as pseudo-n |
| marginalize-predictive | 05:221 | `Marginalizing λ out ... turns one Poisson into a Negative-Binomial` | doesn't see integrating out λ gives overdispersion |
| Gamma/Poisson-predictive-params | 05:226 | `r, p = an_g, bn_g / (bn_g + 1.0)` | mystified how Gamma posterior maps to NegBin (r,p) |
| law-of-total-variance | 05:229 | NegBin `variance = 3.0` vs plug-in Poisson `2.0` | doesn't see epistemic variance added |
| marginalize-predictive | 05:235 | `Integrating σ² out of the predictive yields a Student-t` | stuck: why the predictive is t, not Normal |
| Student-t-df=2a_n | 05:236 | `ν = 2a_n`, `scale² = b_n(κ_n+1)/(a_n κ_n)` | can't derive/recall the NIG→t parameter map |
| change-of-vars-Jacobian | 05:256 | `s2 = stats.invgamma(a=an, scale=bn).rvs(...)` course-convention scale | rate/scale swap corrupts the sampling |
| hierarchical-sampling | 05:255 | sample `s2`, then `mu`, then `yt` | doesn't read the ancestral-sampling chain of the predictive |
| conjugate-add-stat | 05:280 | `posterior is Dir(α+n)` | stuck: why Dirichlet just adds counts |
| normalize-discrete | 05:281 | `P(x̃=k∣n) = (α_k+n_k)/∑_j(α_j+n_j)` | doesn't see add-α smoothing as normalized posterior mean |
| law-of-total-variance | 05:301 | `Var[ỹ∣y] = E[Var[ỹ∣θ]] + Var[E[ỹ∣θ]]` | can't decompose predictive variance into aleatoric+epistemic |
| variance-inflation-factor | 05:309 | `var_pred_bb = m*p*(1-p)*(K+m)/(K+1)` | mystified by the Beta-Binomial variance formula |
| Beta-Binomial-pmf | 05:335 | `comb(m,xs)*np.exp(betaln(xs+a, m-xs+b) - betaln(a,b))` | can't build the BB pmf via log-Beta functions |
| logsumexp/log-beta | 05:335 | `np.exp(betaln(...) - betaln(a, b))` | doesn't see log-space evaluation of a Beta ratio |
| cumsum-cdf-quantile | 05:337 | `bb_cdf = np.cumsum(bb_pmf); xs[np.searchsorted(bb_cdf, 0.05)]` | can't get discrete quantiles from cumulative sums |
| indicator-expectation | 05:328 | `cov_plugin = np.mean((y_future >= lo_pi) & (y_future <= hi_pi))` | doesn't read coverage as a mean of indicators |
| decision=min-expected-loss | 05:374 | `loss_ship_B = np.mean(np.maximum(tA - tB, 0.0))` | stuck: why regret is E[max(diff,0)] |
| monte-carlo-probability | 05:372 | `p_B_beats_A = np.mean(tB > tA)` | doesn't read P(B>A) as fraction of joint draws |
| quadratic-form | 05:296 | `sd_sum = np.sqrt([1,1] @ Sigma_n @ [1,1])` | can't read a^⊤Σa as variance of a linear combo |
| block-conditioning-formula | 05:407 | `μ_{1∣2}=μ1+Σ12Σ22⁻¹(x2-μ2)` | stuck: where the Gaussian conditional formulas come from |
| Schur-complement | 05:407 | `Σ_{1∣2}=Σ11-Σ12Σ22⁻¹Σ21` | doesn't recognize the Schur complement / why it's data-free |
| solve-not-invert | 05:419 | `S12 @ np.linalg.solve(S22, x2 - mu[idx2])` | uses explicit inverse; misses numerically-stable solve |
| precision=inverse-covariance | 05:430 | `Lam = np.linalg.inv(Sigma); cc_prec = 1.0 / Lam[0, 0]` | doesn't see Σ_{1|2}=Λ11⁻¹ precision route |
| rejection-conditioning | 05:438 | `keep = (np.abs(X[:,1]-x2[0])<0.1) & ...` | mystified how a neighborhood mask approximates conditioning |
| commutativity-of-updates | 05:487 | `p(θ∣y1,y2)∝p(y2∣θ)p(y1∣θ)p(θ)`, multiplication commutes | doesn't see why sequential=batch/order-invariant |
| pseudo-count-swamping | 05:523 | `denominator becomes 50 + 10000·1 = 10050` | can't see why add-1 over big V destroys the MLE |
| set-derivative=0 | 06:53 | `ρ'(a) = E[-2(θ-a)] = 0 ⇒ a = E[θ∣y]` | can't derive that squared-error gives the mean |
| set-derivative=0 | 06:54 | `ρ'(a) = P(θ<a) - P(θ>a) = 0 ⇒ a = median` | stuck: why absolute loss gives the median |
| taylor-expand-loss | 06:55 | `ρ(a) ≈ 1 - 2ε p(a∣y)` minimized where density largest | can't see the ε-expansion giving the mode |
| Gamma-mode-formula | 06:66 | `mode_hat = (2 - 1) / 1.0  # (alpha-1)/rate` | doesn't recall the Gamma mode |
| LOTUS-quadrature | 06:69 | `def exp_sq(a): return np.sum((g - a)**2 * dens) * dg` | doesn't read E[g(θ)] as ∫g·density on a grid |
| variance=E[(θ-Eθ)²] | 06:93 | `mean's expected squared loss ... is the posterior variance` | misses that E[(θ−Eθ)²]=Var |
| set-derivative=0 | 06:104 | `d/dq E[cost] = (c_u+c_o)F(q) − c_u = 0 ⇒ F(q*)=c_u/(c_u+c_o)` | can't derive the newsvendor critical fractile |
| quantile-of-predictive | 06:115 | `q_star = pred.ppf(crit)` | doesn't see optimal order is a predictive quantile |
| pinball-loss-minimizer | 06:128 | `ρ_τ(u) = u(τ − 1{u<0})`, minimizer is τ-quantile | mystified why quantile regression targets a quantile |
| brute-force-verify | 06:124 | `cost = np.array([np.mean(c_u*np.maximum(draws-q,0)+...) for q in qs])` | doesn't read the simulated expected-cost sweep |
| MAP=penalized-MLE | 06:133 | `arg max[log p(y∣θ)+log p(θ)] = arg min[−log p(y∣θ)+(−log p(θ))]` | can't turn MAP into loss+penalty |
| log-product→sum | 06:133 | `log p(y∣θ) + log p(θ)` | doesn't see product→sum inside the argmax |
| neg-log-Gaussian=ℓ2 | 06:136 | `−log p(β)=‖β‖²/(2τ²)+const` | stuck: why Gaussian prior gives ridge penalty |
| neg-log-Laplace=ℓ1 | 06:137 | `−log p(β)=‖β‖1/b+const` | doesn't see Laplace prior gives lasso |
| penalty=σ²/prior-var | 06:146 | `lam_ridge = sigma2 / tau2` | mystified by the λ↔prior-variance identity |
| precision-weighted-avg | 06:144 | `(y_obs.sum()/sigma2)/(1/tau2 + len(y_obs)/sigma2)` | can't read the precision-weighted posterior mean |
| soft-threshold-derive | 06:158 | `np.sign(z) * max(abs(z) - thr, 0.0)` | doesn't recognize the lasso soft-threshold as the ℓ1 MAP |
| LOTUS-quadrature | 06:162 | `np.trapezoid(t*w, t) / np.trapezoid(w, t)` for `E[θ∣z]` | can't read posterior mean as ∫θ·unnorm/∫unnorm |
| unnormalized-posterior | 06:161 | `w = np.exp(-(z - t)**2/(2*sigma2) - np.abs(t)/b)` | doesn't see likelihood×prior in log-space then exp |
| coverage=indicator-mean | 06:239 | `cover = (lo <= 0) & (hi >= 0); cover.mean()` | can't read coverage as mean of straddle indicators |
| ancillary-recognize | 06:200 | `R = ∣X1−X2∣ is an ancillary statistic` | doesn't see the gap's distribution is θ-free |
| geometric-probability | 06:202 | `X_{(1)} is uniform on [−½, ½−r]; straddles 0 iff X_{(1)}∈[−r,0]` | can't do the length-ratio conditional-coverage geometry |
| case-split-piecewise | 06:205 | `γ(r) = r/(1−r) if r<½ else 1` | mystified by the two-regime coverage formula |
| binned-conditional-estimate | 06:251 | `emp = [cover[(R>=edges[i])&(R<edges[i+1])].mean() ...]` | doesn't read binning as estimating γ(r) |
| Fubini-swap-expectations | 06:282 | `E_θ E_{Y∣θ}[·] = E_Y E_{θ∣Y}[·]` | stuck: why swapping the two expectations is legal |
| indicator-expectation=probability | 06:282 | `E_{θ∣Y}[1{θ∈C(Y)}] = 1−α by construction` | doesn't see the credible-set expectation equals 1−α |
| posterior-mean/var-Normal-Normal | 06:283 | `θ̂ = τ²Y/(τ²+1), v = τ²/(τ²+1)` | can't recall the one-obs Normal-Normal update |
| coverage-at-fixed-θ | 06:298 | `((lo <= theta) & (theta <= hi)).mean()` | doesn't read frequentist pointwise coverage sim |
| pivot-θ-free-distribution | 06:371 | `pivot Ȳ − θ, whose distribution ⅓Gamma(3,1) is θ-free` | mystified how a pivot makes a CI |
| indicator-in-likelihood | 06:389 | `likelihood ∝ e^{−∑(y_i−θ)}1{θ≤min y_i}` | doesn't see the support indicator bounding the posterior |
| HPD-shortest-interval | 06:436 | `minimize_scalar(width, bounds=..., )` for HPD | can't see HPD as the width-minimizing 90% interval |
| cdf-shift-for-interval | 06:435 | `P.ppf(P.cdf(l) + 0.90) - l` | mystified how this gives a 90%-mass interval width |
| conjugate-add-stat | 07:63 | `(a + s) / (a + s + b + f)` | stuck: why posterior mean is this ratio |
| prior-weight=κ/(κ+n) | 07:69 | `its weight is (a+b)/(a+b+n)` | doesn't see prior influence as a pseudo-count fraction |
| marginalize-prior-predictive | 07:95 | `p(ỹ) = ∫ p(ỹ∣θ)p(θ)dθ` | can't read the prior predictive as marginalization |
| ancestral-sim | 07:100 | `theta = prior_sampler(M); ytilde = sim_data(theta)` | doesn't read draw-θ-then-draw-y simulation |
| tail-mass-cdf/sf | 07:114 | `p_below0 = stats.norm(0.5, sd).cdf(0.0)` | can't compute mass outside [0,1] via cdf+sf |
| clip-to-support | 07:120 | `np.clip(rng.normal(0.5, sd_absurd, M), 0.0, 1.0)` | misses that clipping is itself the pathology |
| change-of-vars-Jacobian | 07:183 | `p(ψ) = p(θ)∣dθ/dψ∣ = θ(1-θ)` | stuck: why the transformed density isn't flat |
| logit-transform | 07:161 | `psi = np.log(theta_u / (1 - theta_u))` | doesn't read logit as the log-odds map |
| induced-density-formula | 07:164 | `dens3 = np.exp(3) / (1 + np.exp(3))**2` | can't compute the logistic density the Jacobian induces |
| improper-limit-Haldane | 07:183 | uniform-on-ψ ⇒ `π(θ)∝θ⁻¹(1−θ)⁻¹` | doesn't see reverse Jacobian gives non-integrable spikes |
| Jeffreys=√Fisher | 07:188 | `π_J(θ) ∝ √I(θ)` | mystified where the Jeffreys prior comes from |
| recognize-kernel | 07:190 | `θ^{-1/2}(1-θ)^{-1/2} = Beta(½,½) kernel` | can't recognize the arcsine Beta kernel |
| info-reparam-transform | 07:192 | `I_ψ = I_θ(dθ/dψ)² = θ(1-θ)` | doesn't know Fisher info transforms with the squared Jacobian |
| change-of-vars-Jacobian | 07:211 | `post_B = post_psi / (th * (1 - th))  # Jacobian dpsi/dtheta` | can't push a ψ-posterior back to θ |
| normalize-via-trapezoid | 07:212 | `post_B /= np.trapezoid(post_B, th)` | doesn't see numeric normalization of a kernel |
| verify-invariance | 07:214 | `max|post_A - post_B| = 5.64e-12` | misses that ~0 confirms Jeffreys invariance |
| multiparam-Jeffreys=√det | 07:233 | `π_J∝√det I(θ)` | doesn't know the multivariate generalization / its pitfalls |
| improper-posterior-check | 07:245 | `∫₀¹ θ^{n-1}(1-θ)^{-1}dθ` divergence | stuck: why you must check the normalizing integral |
| log-divergence-signature | 07:255 | `the integral grows like −log(eps)` | can't read the log-divergence from the growing values |
| propriety-rule | 07:268 | `Beta(s,f) is proper iff s>0 and f>0` | doesn't see the boundary-data propriety condition |
| scale-invariant-prior | 07:270 | `π(σ)∝1/σ (equivalently π(σ²)∝1/σ²)` | mystified by the 1/σ ↔ 1/σ² equivalence (a Jacobian) |
| linear-Gaussian-posterior | 07:282 | `Λ_n = (1/σ²)X^⊤X + Λ0` | can't assemble the Gaussian posterior precision |
| quadratic-form | 07:296 | `sd_sum = np.sqrt([1,1] @ Sigma_n @ [1,1])` | can't read variance of θ1+θ2 as a quadratic form |
| identifiability-rank | 07:292 | each row of `X` is `[1,1]` ⇒ only the sum identified | doesn't see the rank-deficiency killing 1/√n shrinkage |
| precision→covariance | 07:293 | `Sigma_n = np.linalg.inv(Lambda_n)` | misses invert-precision-to-get-covariance step |
| neg-log-prior=penalty | 07:329 | `the second term is −2σ²log of a Gaussian prior β∼N(0,σ²/λ I)` | can't map ridge penalty back to a prior variance |
| penalty=σ²/prior-var | 07:333 | `prior_var = sigma2_noise / lam` | mystified by the λ↔prior-variance conversion |
| prior-sd-from-λ | 07:379 | `prior_sd = np.sqrt(sigma2 / lam)` | doesn't see weight-decay strength as a prior SD |
| propriety-at-boundary | 07:364 | `Beta({an},{bn}) is IMPROPER` when `an` or `bn`=0 | can't predict the Haldane collapse on zero-event data |
| constraint-propagation | 07:422 | `θ2=(θ1+θ2)−θ1 inherits both constraints` | doesn't see a prior on one direction pinning the other via the identified sum |
| CLT/standard-error | 08:48 | `√n(θ̂ₙ − θ₀) →d N(0, I(θ₀)⁻¹)` | stuck: why is the sampling law Gaussian with variance I⁻¹/n? |
| sum-of-independent-closes | 08:54 | `sum of n Poisson(lam) is Poisson(n*lam), so draw directly` | stuck: why can you skip drawing n values and draw one? |
| MC-estimator-E≈mean | 08:55 | `rng.poisson(lam0 * n_pois, size=R) / n_pois` | stuck: histogram of x̄ over R datasets *is* the sampling distribution |
| Fisher-info→variance | 08:57 | `sd_asym = np.sqrt(lam0 / n_pois)  # I(lam)=1/lam` | stuck: where does λ/n come from as the variance? |
| KS-goodness-of-fit | 08:58 | `stats.kstest(xbar_pois, stats.norm(...).cdf).statistic` | stuck: what number certifies "matches the Gaussian"? |
| vectorize/broadcast | 08:82 | `rng.normal(mu, ..., size=(R, n_cr)).mean(1)` | stuck: R datasets × n each in one array, mean over axis 1 |
| Cauchy–Schwarz | 08:77 | `The proof is one Cauchy–Schwarz step on Cov[W,score]` | stuck: why does Cov[W,score] bound the variance? |
| quadratic-form-‖·‖² | 08:107 | `sq = (X**2).sum(1, keepdims=True)` | stuck: ‖X‖² as a row-wise sum of squares with keepdims for broadcast |
| broadcast-shrink×X | 08:108 | `js = shrink * X` (shrink is (R,1), X is (R,d)) | stuck: scalar-per-row multiplies each coordinate |
| MC-estimator-E≈mean | 08:110 | `err = lambda est: ((est - theta)**2).sum(1).mean()` | stuck: total risk estimated as mean of per-replication squared error |
| E[1/χ²]=1/(d-2) | 08:166 | `Because E[1/χ²_d]=1/(d-2)` | stuck: the whole (d−2) factor rides on this expectation identity |
| marginalize-out-latent | 08:166 | `Marginally, integrating out θ_i, each X_i ~ N(0,1+τ²)` | stuck: why is the marginal variance 1+τ²? |
| unbiased-estimator | 08:168 | `an unbiased estimate of the shrinkage fraction` | stuck: why does plugging B̂ in "just work"? |
| precision-weighted-blend | 08:165 | `E[θ_i∣X_i] = (τ²/(1+τ²))X_i` | stuck: posterior mean as data-weight × data |
| MC-estimator-E≈mean | 08:176 | `Bhat = ((d - 2) / (X**2).sum(1)).mean()` | stuck: averaging (d−2)/‖X‖² over draws estimates E[·] |
| standardize-to-N(0,1) | 08:91 | `Standardize each so its measurement is X_i ∼ N(θ_i,1)` | stuck: why can three unlike quantities share unit-noise form? |
| BvM-center-and-scale | 08:187 | `p(θ∣y) ≈ N(θ̂ₙ, I_n⁻¹)` | stuck: posterior and sampling law compared only after centering |
| center-before-compare | 08:208 | `center each at its OWN mean, then compare` | stuck: why subtract the mean before the TV distance? |
| running-estimate-from-2pts | 08:249 | `mu_hat = (Xp + Yp) / 2  # MLE of each mu_i` | stuck: why does 2-point mean bias σ² downward? |
| location-scale-draw | 08:235 | `theta * rng.beta(n, 1, size=...)  # max = theta*Beta(n,1)` | stuck: why is max of n U(0,θ) distributed as θ·Beta(n,1)? |
| rescale-to-limit-law | 08:235 | `scaled = n * (theta - mx)  # -> Exponential` | stuck: why multiply the error by n (not √n) here? |
| skewness-as-shape-probe | 08:237 | `skew = {stats.skew(scaled):.2f} (Normal=0)` | stuck: skew≠0 is the tell it is not Gaussian |
| posterior-mean=Bayes-rule | 08:280 | `act = posterior mean of theta at each outcome` | stuck: why is the Bayes rule the posterior mean under sq-loss? |
| expectation-under-pmf | 08:270 | `(pmf[j] * (a - theta[j])**2).sum()` | stuck: risk as a pmf-weighted sum over outcomes (LOTUS) |
| Dirichlet-weights-as-posterior | 08:315 | `w = rng.dirichlet(np.ones(40), size=B); (w * data).sum(1)` | stuck: why do Dirichlet(1..1) weights give a posterior over the mean? |
| resample-with-replacement | 08:314 | `idx = rng.integers(0, 40, size=(B, 40)); data[idx].mean(1)` | stuck: index array as vectorized bootstrap resampling |
| indicator-mean=probability | 08:343 | `cover = ((lo <= theta0) & (theta0 <= hi)).mean()` | stuck: mean of a boolean array is the coverage frequency |
| precision-add | 08:341 | `pv = 1 / (n_ca + 1 / tau2)` | stuck: posterior precision = data precision + prior precision |
| LLN→sample-average | 09:47 | `μ̂_M = (1/M)Σ g(θ_i) → E[g(θ)∣y]` | stuck: why does an average converge to the integral? |
| CLT/standard-error | 09:47 | `μ̂_M − E[g] ≈ N(0, σ_g²/M)` | stuck: why is the MC error Gaussian with variance σ²/M? |
| indicator-mean=probability | 09:50 | `a tail probability P(θ>c) is g(θ)=1[θ>c]` | stuck: a probability is just the mean of an indicator |
| MC-estimator-E≈mean | 09:61 | `theta.mean()` recovers the posterior mean | stuck: one bag of draws answers every question via mean() |
| push-samples-through-g | 09:67 | `odds = theta / (1 - theta)  # a transformation, for free` | stuck: transform draws, don't re-derive a distribution |
| E[θ/(1−θ)]=a/(b−1) | 09:68 | `E[θ/(1−θ)] = a/(b−1) for a Beta` | stuck: closed form used as the "exact" grading truth |
| quantiles-from-samples | 09:63 | `np.quantile(theta, [0.05, 0.95])` | stuck: a credible interval is a pair of sample quantiles |
| MCSE=s/√M | 09:77 | `MCSE = σ_g/√M ≈ s/√M` | stuck: where does the reported error bar come from? |
| sample-var-ddof=1 | 09:89 | `s.std(ddof=1) / np.sqrt(Msmall)` | stuck: why ddof=1 (unbiased sample variance) in the MCSE? |
| 1/√n-error | 09:79 | `precision improves only as √M: 10× costs 100×` | stuck: why does cutting error 10× need 100× draws? |
| verify-against-quadrature | 09:102 | `integrate.quad(...)` checked against MC | stuck: trust the estimate only against an independent computation |
| 2×SE-band | 09:108 | `+/- {2*mc_se:.6f}  (2 MCSE)` | stuck: why report 2×SE as the interval? |
| walrus-in-comprehension | 09:120 | `(p := rng_pi.random((M, 2)))[:, 0]**2 + ...` | stuck: assign-and-use array inside a list comprehension |
| indicator-mean=probability | 09:120 | `4 * (...<= 1).mean()  # fraction inside quarter circle × 4` | stuck: π estimated as 4× a proportion |
| var-of-proportion | 09:126 | `theory sqrt(pi*(4-pi)/M)` | stuck: where does p(1−p)-type variance of a proportion come from? |
| log-log-slope-−½ | 09:137 | `∝ 1/√M reference (slope −1/2)` | stuck: why is 1/√M a straight line of slope −½ on log-log? |
| rare-event-relative-error | 09:167 | `relative error ≈ 1/√(Mp)` | stuck: why does the effective sample size become the hit count? |
| importance-reweight-identity | 09:171 | `E_p[h] = ∫ h (p/q) q dx = E_q[h·w]` | stuck: why can you sample from q and correct with p/q? |
| weight=p/q | 09:182 | `w = stats.norm.pdf(x) / q.pdf(x)  # importance weights p/q` | stuck: what is the weight and why this ratio? |
| SE-ratio-efficiency | 09:187 | `SE ratio naive/IS ~ 84x` | stuck: comparing estimator SEs to quantify the gain |
| infinite-variance-diagnosis | 09:232 | `E_q[w²] = ∫ t3²/φ dx ... diverges` | stuck: why compute ∫w²q to detect blow-up? |
| tail-dominance-argument | 09:232 | `x^{-8} e^{x²/2} → ∞ — the integral diverges` | stuck: comparing polynomial vs Gaussian tails to see divergence |
| ESS=(Σw)²/Σw² | 09:199 | `ESS = (Σw_i)²/Σw_i²` | stuck: what does ESS mean and why this ratio? |
| ESS=M/(1+cv²) | 09:199 | `= M/(1+cv²), cv² = Var[w]/w̄²` | stuck: why does weight-variance set the effective count? |
| self-normalized-IS | 09:222 | `wbar = w / w.sum(); est = Σ wbar·x²` | stuck: why normalize weights when the target is unnormalized? |
| max-weight-share | 09:226 | `max single weight = {wbar.max()*100:.2f}%` | stuck: one weight's share as a domination alarm |
| ESS-fraction-collapse | 09:232 | `ESS *fraction* collapses as M grows` | stuck: why watch ESS/M vs M, not a single ESS? |
| median-over-reps | 09:245 | `float(np.median(fr))  # ESS itself is random` | stuck: why median across replications, not one run? |
| log10-for-spread | 09:263 | `np.log10(wbar[wbar > 0] + 1e-300)` | stuck: log-scale to see weights spanning many orders |
| floating-point-hygiene | 09:263 | `+ 1e-300` before log10 | stuck: guard against log(0) underflow |
| envelope-C≥p/q | 09:279 | `Find an envelope constant C with p(x)≤C q(x)` | stuck: why must C dominate the density ratio everywhere? |
| accept-w.p.-p/(Cq) | 09:290 | `accept = u <= tgt.pdf(x) / C` | stuck: why does this accept rule yield exact target draws? |
| mode-of-Beta | 09:286 | `mode = (2-1)/(2+5-2)  # Beta(2,5) mode = 0.2` | stuck: where does the tightest C=pdf(mode) come from? |
| acceptance=1/C | 09:292 | `theoretical acceptance 1/C` | stuck: why is accept prob the reciprocal of the envelope? |
| geometric-trials-mean=C | 09:279 | `number of proposals until accepted is Geometric ... E=C` | stuck: why does it cost C proposals per kept draw? |
| indicator-mean=probability | 09:293 | `empirical acceptance = accept.mean()` | stuck: acceptance rate as mean of a boolean mask |
| KS-goodness-of-fit | 09:295 | `stats.kstest(kept, tgt.cdf).pvalue` | stuck: p-value certifying the accepted draws match target |
| condition-on-neighborhood | 09:319 | `keep = np.abs(y_sim - y_obs) <= eps * n_trials` | stuck: why keep draws whose sim lands near the data? |
| simulate-summary-stat | 09:315 | `y_sim = rng_abc.binomial(n_trials, theta_prop)` | stuck: vectorized forward simulation of the summary |
| ε→0-recovers-posterior | 09:302 | `Send ε→0 and you recover the exact posterior` | stuck: why does shrinking tolerance converge to the posterior? |
| bias-variance-of-ε | 09:325 | `ABC sd ... inflating the posterior` at loose ε | stuck: why does a loose neighborhood widen the posterior? |
| detailed-balance⇒stationary | 10:48 | `π(θ)P(θ,θ') = π(θ')P(θ',θ)` | stuck: why does a pairwise flow condition give global stationarity? |
| sum-over-destinations=1 | 10:53 | `Σ_θ P(θ',θ) = π(θ')·1` | stuck: why does the remaining transition-row sum to 1? |
| drop-const-∝ | 10:60 | `any unnormalized π̃∝π gives the identical rule` | stuck: why can you ignore the normalizing constant? |
| ratio-cancels-evidence | 10:10 | `p(θ∣y)/p(θ*∣y) cancels the intractable evidence p(y)` | stuck: why does the evidence disappear in MH? |
| symmetric-q-cancels | 10:60 | `for a symmetric proposal ... the q's cancel too` | stuck: why does α reduce to π(θ')/π(θ)? |
| min(1,ratio)-acceptance | 10:59 | `α = min(1, π(θ')q(θ∣θ')/[π(θ)q(θ'∣θ)])` | stuck: why the min and why this exact ratio? |
| stay-on-reject | 10:123 | `chain[t] = x  # record even on reject` | stuck: why does a rejected move still emit a draw? |
| work-in-log-density | 10:111 | `(a-1)*np.log(theta) + (b-1)*np.log1p(-theta)` | stuck: why compute the log-posterior, not the density? |
| log1p-for-precision | 10:111 | `np.log1p(-theta)` instead of `log(1-theta)` | stuck: why log1p near θ→1 for floating-point accuracy |
| log-ratio-not-divide | 10:121 | `if np.log(gen.random()) < lp - lx` | stuck: why subtract log-densities instead of dividing densities? |
| −∞-for-out-of-support | 10:110 | `return -np.inf  # prior support is (0,1)` | stuck: why does −inf log-density auto-reject proposals? |
| min(1,r)-via-log-u | 10:121 | `log(u) < lp - lx ⇔ accept w.p. min(1, ratio)` | stuck: why does comparing log-uniform to log-ratio implement min(1,·)? |
| seed-discipline | 10:126 | `g_bb = np.random.default_rng(SEED + 1)` | stuck: why offset seeds per chain for reproducibility? |
| discard-warmup | 10:128 | `chain = chain[2000:]  # discard warm-up` | stuck: why throw away the first draws? |
| ESS=M/(1+2Σρ) | 10:155 | `ESS = M/(1+2Σ_{k≥1}ρ_k) ≤ M` | stuck: why do positive autocorrelations shrink the effective count? |
| ACF-via-FFT | 10:164 | `f = np.fft.rfft(x, n=2*n); acov = irfft(f*conj(f))` | stuck: why does FFT of zero-padded signal give autocovariance? |
| zero-pad-2n | 10:165 | `np.fft.rfft(x, n=2 * n)` | stuck: why pad to 2n to avoid circular-correlation wraparound? |
| Geyer-initial-positive | 10:176 | `if rho[k] < 0: break  # truncate at first negative` | stuck: why stop summing autocorrelations at the first negative? |
| center-before-acf | 10:165 | `x = x - x.mean()` | stuck: why subtract the mean before autocovariance? |
| 2.38/√d-scaling | 10:200 | `opt_step = 2.38 / np.sqrt(d)` | stuck: where does the √d step-shrink come from? |
| optimal-accept-0.234 | 10:215 | `high-d product: 0.234` | stuck: why is the efficient acceptance rate a fixed 0.234? |
| ESS-per-iteration | 10:155 | `We want the step size that maximizes ESS per iteration` | stuck: why optimize ESS, not acceptance rate? |
| argmax-over-rows | 10:207 | `peak50 = max(rows50, key=lambda r: r[2])` | stuck: pick the step giving max ESS |
| logsumexp | 10:251 | `m = max(a,b); m + np.log(0.5*exp(a-m)+0.5*exp(b-m))` | stuck: why subtract the max before exp in a log-mixture density? |
| subtract-max-before-exp | 10:251 | `np.exp(a - m)` with `m = max(a, b)` | stuck: prevents overflow/underflow when exponentiating log-densities |
| sign-change=crossing | 10:256 | `np.sum(np.abs(np.diff(np.sign(bim))) > 0)` | stuck: counting mode crossings via sign changes of the diff |
| indicator-mean=probability | 10:258 | `np.mean(bim > 0)` estimates P(θ>0) | stuck: posterior mass as mean of a boolean |
| ergodicity-is-asymptotic | 10:281 | `Ergodicity is an asymptotic guarantee` | stuck: why doesn't 40k steps guarantee finding both modes? |
| trapezoid-normalize | 10:273 | `dens /= np.trapezoid(dens, grid)` | stuck: normalize an evaluated density to integrate to 1 |
| between/within-var-decomp | 10:323 | `var̂⁺ = ((N-1)/N)W + (1/N)B` | stuck: what are B and W and why this weighted blend? |
| B=n·Var(chain-means) | 10:328 | `B = n * C.mean(axis=1).var(ddof=1)` | stuck: why scale between-chain variance by n? |
| split-Rhat | 10:323 | `R̂ = √(var̂⁺/W)` | stuck: why does √(inflated-var / within-var) detect non-convergence? |
| split-chains-catch-trend | 10:342 | `S = np.vstack([C[:, :h], C[:, h:2*h]])  # 2m half-chains` | stuck: why split each chain in half before comparing? |
| rho-from-var-decomp | 10:332 | `rho = 1.0 - (W - avg_acov)/var_plus` | stuck: how is combined autocorrelation recovered from B, W, acov? |
| Geyer-initial-pairs | 10:334 | `pair = rho[k]+rho[k+1]; if pair < 0: break` | stuck: why sum autocorrelations in adjacent pairs? |
| rank-normalize-transform | 10:351 | `z = stats.norm.ppf((r - 3/8)/(r.size - 1/4))` | stuck: why replace draws by normal scores of their ranks? |
| MCSE=s/√ESS | 10:489 | `the MCSE s/√ESS` | stuck: why divide by √ESS, not √M, for correlated draws? |
| precision-overstated-√ratio | 10:363 | `overstate ... by roughly √(16000/2300)≈2.6×` | stuck: why √(M/ESS) is the inflation factor? |
| second-eigenvalue-mixing | 10:416 | `λ₂ governs how fast everything else decays` | stuck: why does the 2nd eigenvalue set the mixing rate? |
| relaxation-time=1/gap | 10:416 | `t_rel = 1/(1−λ₂)` | stuck: why is relaxation time the reciprocal of the spectral gap? |
| ACF∼λ₂^k | 10:439 | `theory lam2^k` matches measured ACF | stuck: why does autocorrelation decay geometrically at rate λ₂? |
| eig-of-transition | 10:435 | `np.sort(np.linalg.eigvals(P2).real)[::-1][1]` | stuck: extract the second eigenvalue as the mixing rate |
| λ₂=1−a−b (2-state) | 10:456 | `λ₂ = 1−a−b = 0.800 exactly` | stuck: closed-form 2nd eigenvalue of a 2-state chain |
| stationary-of-2-state | 10:437 | `pi2 = np.array([b/(a+b), a/(a+b)])` | stuck: closed-form stationary law of a 2-state chain |
| integrated-autocorr-time | 10:438 | `tau_int = (1+λ₂)/(1−λ₂)` | stuck: AR(1)-type IAT from the eigenvalue |
| tempering-exp(f/T) | 10:464 | `π_T(θ) ∝ exp(f(θ)/T)` | stuck: why does raising to 1/T flatten/sharpen the target? |
| Metropolis-on-−U/T | 10:478 | `log(u) < -(U(xp)-U(x))/T` | stuck: log-acceptance for a Boltzmann target with temperature |
| geomspace-cooling | 10:476 | `np.geomspace(3.0, 0.02, 4000)  # cooling schedule` | stuck: why geometric (not linear) temperature decay? |
| additive-const-cancels | 10:509 | `max|difference| ... = 0.00e+00` after adding log p(y) | stuck: why does adding any constant to log-target change nothing? |
| same-seed-paired-compare | 10:505 | `g2 = default_rng(SEED + 20)  # SAME seed` | stuck: why reuse the seed to isolate the effect being tested? |
| energy-differences-only | 10:570 | `sampled ... using only energy differences E(θ')−E(θ), never Z` | stuck: why energy-based models dodge the partition function |
| flow=π·P-symmetry | 10:81 | `flow = pi[:, None] * P; max|flow - flow.T|` | stuck: detailed balance checked as symmetry of the flow matrix |
| MH-acceptance-ratio | 11:55 | `α = p(θ',θ)q(θ|θ')/(p(θ,θ)q(θ'|θ))` | stuck: why does this ratio target the joint? |
| factor-joint-chain-rule | 11:57 | `using p(θ_i,θ_{-i}) = p(θ_i|θ_{-i})p(θ_{-i})` | can't see why every factor cancels to 1 |
| drop-const-∝ | 11:80 | `reading off the kernel of the other` | doesn't know you can ignore normalizers when identifying a conditional |
| recognize-kernel | 11:83 | `μ|σ²,y ~ N(...)` read off | stuck: how do you know the conditional is Normal? |
| precision-weighted-mean | 11:82 | `precisions add, mean is precision-weighted` | can't derive the Normal-Normal posterior mean/variance |
| collect-powers-of-var | 11:85 | `Collect every factor of σ² in p(y|μ,σ²)p(μ|σ²)p(σ²)` | can't assemble the IG conditional |
| recognize-kernel (IG) | 11:86 | `the exponent and rate read straight off an inverse-gamma kernel` | stuck: why is σ²|μ,y Inverse-Gamma? |
| count-power-in-IG | 11:86 | `a_0 + (n+1)/2` | can't see where the n+1 shape increment comes from |
| sum-of-squares | 11:86 | `½Σ_i(y_i−μ)² + κ₀/2(μ−μ₀)²` | doesn't recognize the SSE + prior-coupling as the IG rate |
| invgamma-via-gamma-reciprocal | 11:44 | `if X ~ IG(a,b) then 1/X ~ Gamma(shape=a, rate=b)` | can't sample IG without scipy; misreads scale/rate |
| gamma-scale-vs-rate | 11:45 | `numpy's gamma takes scale = 1/rate` | off by inversion; wrong-scale draws |
| standardize-t-marginal | 11:107 | `t_scale = np.sqrt(bn / (an*kn))` | can't reconstruct the Student-t scale from NIG params |
| IG-mean-formula | 11:109 | `E[sigma^2]={bn/(an-1)}` | doesn't know IG mean is b/(a−1) |
| vectorized-SSE | 11:119 | `0.5*np.sum((data - mu_c)**2)` | writes a slow loop; misplaces the ½ |
| cholesky-sample-MVN | 11:180 | `beta_c = m + np.linalg.cholesky(V) @ rng3.normal(size=p)` | stuck: how to draw a correlated Gaussian from a std normal |
| inverse↔precision | 11:178 | `V = np.linalg.inv(XtX / s2_c + np.eye(p) / tau2)` | doesn't see posterior cov = (data precision + prior precision)⁻¹ |
| precision-weighted-mean (matrix) | 11:179 | `m = V @ (Xty / s2_c)` | can't derive the ridge/posterior mean |
| residual-SS-as-quadform | 11:182 | `b0r + 0.5*resid @ resid` | doesn't recognize ‖y−Xβ‖² as the IG rate |
| vague-prior→OLS-limit | 11:207 | `with a vague prior the posterior mean is the OLS solution` | can't explain why Gibbs means match OLS |
| conditional-expectation-chaining | 11:220 | `E[X_{t+1}|X_t] = ρ·ρ X_t = ρ² X_t` | stuck: why lag-1 autocorr is ρ² not ρ |
| AR(1)-autocorr | 11:221 | `AR(1) process with autoregressive coefficient ρ²` | can't map the chain to an AR(1) |
| IAT→ESS-fraction | 11:221 | `integrated autocorrelation time is (1+φ)/(1−φ)` | can't convert autocorrelation to ESS |
| autocorr-via-FFT | 11:236 | `f = np.fft.rfft(x, 2*n); ac = np.fft.irfft(f*np.conj(f))[:n]` | doesn't know Wiener-Khinchin FFT autocorrelation trick |
| zero-pad-FFT | 11:236 | `np.fft.rfft(x, 2*n)` | circular-convolution wraparound corrupts the ACF |
| normalize-by-lag0 | 11:237 | `return ac / ac[0]` | forgets to normalize; ACF not in [−1,1] |
| Geyer-initial-positive-seq | 11:241 | `if pair <= 0: break` | doesn't know why you truncate the ACF sum |
| quadratic-form-exponent | 11:276 | `Q = (GX**2 - 2*rho_z*GX*GY + GY**2)/(1 - rho_z**2)` | can't read the bivariate-normal exponent |
| indicator-thresholded-Gaussian | 11:297 | `y_i = 1[z_i > 0]` reproduces `P(y=1)=Φ(x^Tβ)` | stuck: why does thresholding a Gaussian give a probit |
| density×indicator=truncation | 11:300 | `∝ N(z_i;x_i^Tβ,1) times the indicator that z_i has the sign` | doesn't see conditional as a truncated normal |
| inverse-CDF-sampling | 11:303 | `m + Φ⁻¹(Φ(−m) + u(1−Φ(−m)))` | can't sample a truncated normal without rejection |
| CDF-inversion-vectorized | 11:321 | `mean + ndtri(np.clip(lo + u*(hi - lo), 1e-12, 1 - 1e-12))` | can't vectorize truncated draws; boundary overflow |
| clip-for-fp-hygiene | 11:321 | `np.clip(..., 1e-12, 1 - 1e-12)` | ndtri(0) or ndtri(1) → ±inf |
| where-broadcast-branch | 11:320 | `lo = np.where(positive, ndtr(-mean), 0.0)` | writes a per-element if; can't vectorize the sign branch |
| conditional-Gaussian-formula | 11:374 | `cmean = mu_e[1] + Sig[1,0]/Sig[0,0]*(Y[mask,0] − mu_e[0])` | stuck: E[Y₂|Y₁] formula for a bivariate normal |
| conditional-variance-schur | 11:372 | `cvar = Sig[1,1] − Sig[1,0]**2/Sig[0,0]` | doesn't recognize the Schur-complement conditional variance |
| selection-bias-via-correlation | 11:356 | `deletion selected on Y₁, and Y₁ is correlated with Y₂` | can't see why complete-case is biased under MAR |
| factor-missingness-joint | 11:409 | `p(Y,M|θ,ψ) = p(Y|θ)p(M|Y,ψ)` | can't state when the M-factor drops (ignorability) |
| law-of-total-variance | 11:423 | `Var[g] = E[Var[g|μ]] + Var[E(g|μ)]` | stuck: why Rao-Blackwell reduces variance |
| conditional-mean-as-estimator | 11:440 | `rb.append(b_c/(a_c-1))` | doesn't know to average E[σ²|μ] instead of the draw |
| E[latent]-vs-sample-latent | 11:458 | `Gibbs draws z~p(z|x,θ); EM computes E[z|x,θ]` | misses that EM = Gibbs with sampling replaced by mean |
| typical-set-radius | 12:54 | `mean ||theta|| = 31.61 ... sqrt(1000)` | stuck: why draws sit at radius √d, not 0 |
| mass=density×volume | 12:65 | `Mass is density times volume ... volume ... grows like r^{d−1}` | can't reconcile "mode densest" with "mode empty" |
| radial-density-peak | 12:65 | `∝ r^{d−1}e^{−r²/2}, sharply peaked at r=√(d−1)` | can't find where radial mass concentrates |
| log-density-gap | 12:60 | `log-density advantage of the mode ... = d/2` | doesn't see the e^{d/2} density-vs-mass tradeoff |
| IAT-truncate-first-neg | 12:100 | `if acf[k] < 0: break` | includes noise-dominated tail; ESS wrong |
| symmetric-proposal→RW-MH | 12:113 | `symmetric proposal -> RW-MH` | thinks proposal density must appear in the ratio |
| log-accept-comparison | 12:113 | `np.log(rng.random()) < lpp - lp` | does exp() and overflows instead of comparing in log |
| power-law-loglog-fit | 12:126 | `slope, intercept = np.polyfit(np.log(ds), np.log(essfrac), 1)` | can't extract a power-law exponent |
| optimal-RW-scale | 12:107 | `scale = 2.38/np.sqrt(d)` | doesn't know the d^{−1/2} tuning law |
| U=−logp-potential | 12:155 | `U(q) = −log p(q|y)` | stuck: why negative log-posterior is "energy" |
| Hamilton's-equations | 12:156 | `q̇=∂H/∂p=p, ṗ=−∂H/∂q=−∇U(q)` | can't derive the leapfrog updates |
| grad-of-quadratic | 12:164 | `def grad_U(q): return Prec @ q` | stuck: ∇(½qᵀΛq)=Λq |
| inverse↔precision | 12:162 | `Prec = np.linalg.inv(Sigma) # precision = inverse covariance` | conflates covariance and precision in U |
| symplectic-leapfrog | 12:167 | `half kick / full drift / half kick` | can't see why the split integrator is reversible/volume-preserving |
| Metropolis-on-energy | 12:183 | `np.log(rng.random()) < H(q,p) − H(q_new,p_new)` | doesn't know the accept step uses ΔH |
| momentum-refresh | 12:181 | `p = rng.standard_normal(2) # resample momentum ~ N(0,I)` | stuck: why redraw momentum each iteration |
| energy-error-O(ε²) | 12:231 | `order = np.polyfit(np.log(eps_grid), np.log(dHs), 1)[0]` | can't verify/expect the quadratic error scaling |
| fixed-T-vary-ε | 12:227 | `L = int(round(T / eps))` | changes trajectory length while probing ε; confounds the fit |
| linear-map-eigen-stability | 12:250 | `two-line eigenvalue analysis gives the exact stability threshold` | stuck: why ε_crit=2/ω |
| curvature=frequency | 12:411 | `ω² = 1/σ²` | doesn't connect variance to oscillator frequency |
| change-of-variables-reparam | 12:281 | `x = e^{v/2}z with z~N(0,1)` | stuck: how non-centering keeps the same joint |
| Jacobian/location-scale | 12:302 | `dist.Normal(0.0, jnp.exp(v/2)) # scale = exp(v/2)` | can't relate centered and non-centered scales |
| local-curvature-varies | 12:326 | `neck's curvature grows like e^{−v/2}, so no single ε survives` | can't explain funnel divergences |
| SDE→discretize | 12:373 | `replace dt by ε and dW by √ε ξ` | stuck: Euler-Maruyama for the Langevin SDE |
| grad-log-Gaussian | 12:379 | `grad_logp = lambda th: -th # d/dθ log N(θ;0,1) = −θ` | can't differentiate a log-density |
| AR(1)-stationary-variance | 12:392 | `v=(1−ε/2)²v+ε ⟹ v=1/(1−ε/4)` | can't solve for a stationary variance |
| Brownian-noise-scaling | 12:382 | `np.sqrt(eps) * rng.standard_normal()` | uses ε not √ε for the noise; wrong diffusion |
| insert-q/q-identity | 13:46 | `Write the evidence, insert q/q, and split the log` | stuck: the algebraic trick launching the ELBO identity |
| E_q[const]=const | 13:52 | `E_q[log p(x)] = log p(x)` | doesn't see log p(x) pulls out of the expectation |
| ELBO=E_q[logp−logq] | 13:44 | `E_q[log p(x,θ) − log q(θ)]` | can't write the ELBO from the joint and q |
| ELBO+KL=logp(x) | 13:48 | `= ELBO(q) + KL(q||p(·|x))` | misses the exact decomposition |
| Jensen-for-ELBO | 13:54 | `log E_q[p/q] ≥ E_q[log p/q]` | stuck: which way Jensen bounds the evidence |
| KL≥0→lower-bound | 13:54 | `Since KL≥0, ELBO(q) ≤ log p(x)` | doesn't see the bound follows from Gibbs' inequality |
| grid-normalize-logsumexp | 13:138 | `log_exact -= logsumexp(log_exact + np.log(dphi))` | can't normalize an unnormalized log-density on a grid |
| numeric-KL-on-grid | 13:82 | `kl = np.sum(q*(logq − logpost))*dth` | doesn't know KL is ∫q log(q/p) discretized |
| 2nd-order-Taylor | 13:123 | `second-order Taylor expansion of log p(θ|x) around its peak` | stuck: where the Laplace Gaussian comes from |
| Hessian=precision | 13:123 | `Σ⁻¹ = −∇²log p(θ|x)|θ⋆` | stuck: why the neg-Hessian is the covariance⁻¹ |
| gradient=0-at-mode | 13:126 | `Its log has derivative α−(α+β)θ` (mode where =0) | can't locate the MAP by setting the derivative to 0 |
| Jacobian-change-of-var | 13:126 | `With a Jacobian dθ/dφ = θ(1−θ)` | can't transform the Beta density to logit space |
| logit-unconstrain | 13:125 | `Map θ↦φ=logit(θ)=log θ/(1−θ)∈ℝ` | fits a Gaussian on [0,1] and leaks mass |
| 2nd-deriv=curvature | 13:127 | `second derivative is −(α+β)θ(1−θ), giving Laplace variance` | can't get the Laplace variance from curvature |
| push-density-through-transform | 13:174 | `stats.norm(mu,√var).pdf(phig)/(tg*(1-tg))` | forgets the Jacobian when mapping q back to θ |
| Gaussian-integral→evidence | 13:185 | `log p(x) ≈ log p(x,θ⋆) + d/2 log 2π − ½log|H|` | stuck: the Laplace evidence formula |
| log-det-in-evidence | 13:196 | `− 0.5*np.log(H)` | doesn't recognize the −½log|H| Occam term |
| coordinate-ascent-ELBO | 13:211 | `EM is coordinate ascent on it` | doesn't see E/M steps as alternating ELBO maximization |
| E-step=exact-conditional | 13:211 | `optimum is the exact conditional q(z_i=k)=p(z_i=k|x_i,μ)` | stuck: why responsibilities are the E-step optimum |
| KL=0-tightens-bound | 13:211 | `drives KL(q(z)||p(z|x,μ)) to zero and makes the ELBO equal log p(x|μ)` | can't see why the incomplete-data loglik climbs |
| M-step-weighted-LS | 13:211 | `μ_k = Σ_i q(z_i=k)x_i / Σ_i q(z_i=k)` | can't derive the M-step means |
| logsumexp-marginalize | 13:225 | `denom = np.logaddexp(l0, l1) # log p(x_i|mu)` | overflows marginalizing the latent; can't compute responsibilities |
| responsibility-softmax | 13:227 | `r1 = np.exp(l1 - denom); r0 = 1 - r1` | stuck: normalizing log-weights into responsibilities |
| point-mass-q(θ) | 13:240 | `q(θ,z)=δ(θ−θ̂)∏_i p(z_i|x_i,θ̂)` | doesn't see EM as VI with a Dirac on θ |
| CAVI-update-rule | 13:266 | `log q_j(θ_j)=E_{q_{-j}}[log p(x,θ)]+const` | can't derive a mean-field factor update |
| CAVI-Gaussian-closed-form | 13:272 | `q_j Gaussian with mean −Λ_{jj}⁻¹Σ_{k≠j}Λ_{jk}E[θ_k] and variance 1/Λ_{jj}` | stuck: the exact CAVI update for a Gaussian |
| var=1/precision-diagonal | 13:272 | `Λ_{jj}=1/(1−ρ²), so the mean-field marginal variance is 1−ρ²` | can't get the 1−ρ² deficit |
| reverse-KL-mode-seeking | 13:300 | `CAVI minimizes KL(q||p) — the reverse, mode-seeking KL` | can't explain why mean-field pulls inward |
| KL-between-Gaussians | 13:296 | `kl_qp = 0.5*(np.trace(Lam @ Q) − 2 + np.log(det(Sigma)/det(Q)))` | doesn't know the closed-form Gaussian KL |
| eigen-ellipse-axes | 13:324 | `vals, vecs = np.linalg.eigh(cov); ang = ...arctan2` | can't turn a covariance into ellipse axes/angle |
| marginal-t-from-NIG | 13:341 | `marginal posterior of μ is a Student-t with ν=2a_n` | stuck: why integrating σ² gives a t |
| condition-vs-integrate-σ² | 13:388 | `Gaussian q(μ) conditions on E[1/σ²] where the exact t integrates over σ²` | can't explain the tail-deficit mechanism |
| tail-inflation-ν/(ν−2) | 13:388 | `missing precisely the ν/(ν−2) tail-inflation factor` | can't quantify the CAVI vs exact sd ratio |
| sd-ratio-closed-form | 13:371 | `sqrt((an-1)/an) = 0.8944` | doesn't recognize the deficit as √((aₙ−1)/aₙ) |
| reparam-trick-ELBO-grad | 13:394 | `the reparameterization trick makes ∇_φ ELBO an expectation you can sample` | stuck: how to get a low-variance ELBO gradient |
| unconstrained-guide-space | 13:456 | `AutoNormal factorizes over (μ,σ) and reports Gaussian tails in the unconstrained space` | doesn't see why σ tail is clipped |
| forward-vs-reverse-KL | 13:498 | `Reverse KL is mode-seeking ... forward KL is mode-covering` | can't predict which objective straddles both modes |
| moment-match=forward-KL | 13:491 | `sd_fwd = sqrt(∫x²p dx − m²) # forward KL: moment match` | doesn't know forward-KL optimum is moment matching |
| evidence=prior-predictive | 13:531 | `p(x|M)=∫p(x|θ)p(θ)dθ` | stuck: why the flexible model pays an Occam tax |
| full-cov-q-contains-target | 13:551 | `full-covariance q ... contains the target itself, so its optimum is exact` | thinks more iterations, not a bigger family, fixes under-dispersion |

## Frequency-ranked summary

477 instances total. Raw skill names from the table are normalized into canonical families
(a family = one teachable prereq lesson). The "one-off facts & moves" bucket collects
singleton skills that resist grouping (e.g. characteristic-function argument 03:168,
calculus-of-variations Lagrangian 03:274, Dirichlet-weights-as-Bayesian-bootstrap 08:315,
typical-set radius √d 12:54, hypergeometric-max likelihood 02:218); teach these in situ
or as sidebars rather than as prereq chapters.


| rank | skill family | count | modules |
|---|---|---|---|
| 1 | one-off facts & moves (see table) | 88 | 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13 |
| 2 | autocorrelation / ESS machinery (ACF, FFT, Geyer, IAT, R-hat) | 35 | 01, 08, 09, 10, 11, 12 |
| 3 | vectorize/broadcast idioms (masks, where, outer, axis, cumsum) | 27 | 00, 01, 02, 03, 04, 05, 08, 09, 10, 11 |
| 4 | Monte-Carlo mean≈expectation (incl. P(A)=mean of indicator) | 22 | 00, 01, 02, 05, 06, 08, 09, 10 |
| 5 | log-space arithmetic (products→sums, argmax/argmin invariance, log-ratios) | 19 | 00, 01, 02, 03, 04, 06, 09, 10, 12 |
| 6 | change-of-variables with Jacobian (logit/log transforms) | 16 | 02, 04, 05, 07, 12, 13 |
| 7 | distributional closure facts (sums/thinning/order stats) | 14 | 01, 03, 08, 11 |
| 8 | add-sufficient-statistics conjugate updating | 14 | 01, 04, 05, 07, 11 |
| 9 | 1/√n and CLT / standard-error reasoning | 13 | 04, 08, 09, 10 |
| 10 | MH acceptance-ratio algebra (min(1,r), cancellations, detailed balance) | 13 | 09, 10, 11, 12 |
| 11 | drop-constants-with-∝ / unnormalized densities | 12 | 00, 04, 05, 06, 10, 11 |
| 12 | logsumexp / subtract-max-before-exp | 12 | 01, 02, 03, 04, 05, 10, 13 |
| 13 | KL / entropy identities (Xent=H+KL, KL≥0, Gaussian KL) | 12 | 03, 13 |
| 14 | expectation/moment closed forms invoked from memory | 11 | 01, 02, 03, 04, 05, 06, 08, 09, 11 |
| 15 | recognize-the-kernel (name the family from its shape) | 10 | 00, 03, 04, 05, 07, 11 |
| 16 | set-derivative=0 / gradient=0 at optimum | 10 | 03, 04, 06, 13 |
| 17 | 2nd-order Taylor / curvature = information = precision | 10 | 04, 06, 08, 12, 13 |
| 18 | precision↔variance switching (inverse covariance, precisions add) | 9 | 00, 05, 07, 08, 11, 12, 13 |
| 19 | quadratic forms aᵀΣa and their gradients | 9 | 00, 04, 05, 07, 08, 11, 12 |
| 20 | tower rule / law of total variance-covariance | 9 | 00, 01, 05, 06, 11, 13 |
| 21 | floating-point hygiene (clip, log1p, −inf sentinel, dtype, jitter) | 9 | 01, 02, 03, 05, 07, 09, 10, 11, 13 |
| 22 | marginalize-out (predictive integrals, latent variables) | 9 | 02, 03, 05, 07, 08, 13 |
| 23 | ELBO / variational algebra (insert q/q, E_q, CAVI) | 9 | 03, 13 |
| 24 | MAP↔regularization dictionary (neg-log prior = penalty) | 8 | 00, 06, 07 |
| 25 | LOTUS / expectation as weighted sum-integral | 8 | 00, 02, 06, 08, 09 |
| 26 | normalize-to-1 (discrete grids, trapezoid) | 8 | 00, 02, 04, 05, 07, 10, 11 |
| 27 | precision-weighted average (shrinkage master formula) | 8 | 05, 06, 07, 08, 11 |
| 28 | Gaussian conditioning / Schur complement / block formulas | 7 | 05, 06, 07, 11, 13 |
| 29 | propriety / divergent-integral checks | 6 | 03, 07 |
| 30 | importance weighting (p/q identity, self-normalization) | 6 | 09 |
| 31 | complete-the-square (scalar and matrix) | 4 | 00, 05, 11 |
| 32 | inverse-CDF / cumsum-searchsorted sampling | 4 | 00, 02, 06, 11 |
| 33 | Gamma/Beta-function identities (betaln, gammaln, normalizers) | 4 | 01, 02, 04, 05 |
| 34 | differentiate under the integral / score identities | 4 | 04 |
| 35 | linear algebra craft (Cholesky, solve-not-invert, eigen) | 4 | 05, 11, 12, 13 |
| 36 | seed discipline / paired-seed comparisons | 3 | 00, 10 |
| 37 | odds↔probability conversions and LR multiplication | 3 | 00, 02 |
| 38 | MSE = bias² + variance decomposition | 3 | 00, 02, 09 |
| 39 | rate-vs-scale parameterization traps | 3 | 03, 11 |
| 40 | Jensen's inequality (which way it goes; ELBO) | 2 | 03, 13 |

### Notes for the prereq authors

- The top of the ranking is **craft, not theorems**: numpy vectorization idioms, MC-mean-as-expectation,
  and log-space arithmetic together account for ~70 instances and are never taught anywhere in 00-13.
- **ACF/ESS machinery** ranks #2 but is *partially* taught in module 10; instances in 01, 08, 09, 11, 12
  precede or exceed that treatment (FFT autocovariance, Geyer truncation, IAT are pure incantation).
- Three families are silently load-bearing for the entire second half: **change-of-variables with Jacobian**
  (Jeffreys, Laplace-on-logit, non-centering), **precision↔variance switching**, and
  **2nd-order Taylor / curvature=precision** (Fisher info 04, BvM 08, HMC stability 12, Laplace 13).
- **rate-vs-scale parameterization** (scipy/numpy Gamma-family conventions) appears only 3 times in the
  table but every occurrence is a silent-corruption bug class; teach it with the Gamma/Beta identities.
- **complete-the-square** counts low (4) only because the text says "completing the square" and skips it;
  each occurrence gates a whole module (00 ridge, 05 Normal-Normal, 11 Gibbs conditionals).

# Verification log (machine-checked results)

All checks run in Python (SymPy / fractions / SciPy). ✔ = matches booklet; ⚠ = discrepancy found.

| PDF p. | Result in booklet | Check | Status |
|---|---|---|---|
| 8 | $\frac13+\frac23-\frac1{12}=\frac{11}{12}\ne\frac12$ (incoherent scientist) | exact fractions | ✔ |
| 9 | Factories: $P(F{=}1\mid D)=\frac{(2/10)(1/3)}{(2/10)(1/3)+(1/10)(2/3)}=\frac12$ | exact fractions | ✔ |
| 10 | $\int_0^\infty\frac{dx}{1+x}=\infty$ (improper); standard normal proper | symbolic | ✔ |
| 11 | $\int_0^\infty\frac{dx}{(1+x)^2}=1$ but $E(X)=\infty$ | symbolic | ✔ |
| 11 | Groceries identity: $\frac{(E-G)^2}{\sigma^2}+\frac{(E-\theta)^2}{\delta^2}=\frac{[E-(\lambda G+(1-\lambda)\theta)]^2}{(1-\lambda)\delta^2}+\frac{\lambda}{\delta^2}(G-\theta)^2$, $\lambda=\frac{\delta^2}{\delta^2+\sigma^2}$; posterior $N(\lambda G+(1-\lambda)\theta,(1-\lambda)\delta^2)$ | SymPy: LHS−RHS ≡ 0 | ✔ |
| 11 | Lab test: $P(D\mid +)=0.323$; $P(D\mid -)=0.00025373$ | $0.00475/0.01470=0.32313$; $0.00025/0.98530=0.00025373$ | ✔ |
| 12 | Plane: $P(R_1\mid E)=\frac{\alpha_1}{\alpha_1+2}<\frac13$, $P(R_2\mid E)=P(R_3\mid E)=\frac{1}{\alpha_1+2}>\frac13$ | posteriors sum to 1; inequalities hold iff $\alpha_1<1$ (true for overlook prob.) | ✔ |
| 12 | $E(p\mid y)=\frac{y+\alpha}{n+\alpha+\beta}=\lambda\frac yn+(1-\lambda)\frac{\alpha}{\alpha+\beta}$, $\lambda=\frac{n}{n+\alpha+\beta}$ | SymPy identity | ✔ |
| 12 | $\mathrm{Var}(p\mid y)=\frac{m(1-m)}{n+\alpha+\beta+1}\le\frac{1}{4(n+\alpha+\beta+1)}$, $m=\frac{y+\alpha}{n+\alpha+\beta}$ | SymPy identity + $m(1-m)\le\frac14$ | ✔ |
| 15 | Equi-correlated normal: $\mathrm{Cor}(X_1,X_2)=\frac{\delta^2}{\sigma^2+\delta^2}$ | from stated covariance matrix | ✔ |
| 16 | Laws of total expectation/variance/covariance; mixture moments $E=\theta$, $\mathrm{Var}=\sigma^2+\delta^2$, $\mathrm{Cov}=\delta^2$ | direct application | ✔ |
| 16 | Beta–Bernoulli marginal $=\frac{B(\sum x_i+\alpha,\ n-\sum x_i+\beta)}{B(\alpha,\beta)}$ | SymPy $\int_0^1 y^{a-1}(1-y)^{b-1}dy=B(a,b)$ | ✔ |
| 17 | Gamma–Gamma marginal with $\frac{\Gamma(n\alpha+\alpha_0)}{(\sum x_i+\beta_0)^{n\alpha+\alpha_0}}$ | SymPy $\int_0^\infty\beta^{A-1}e^{-B\beta}d\beta=\Gamma(A)/B^A$ | ✔ |
| 18 | Normal–normal posterior $\mu\mid x\sim N(\lambda\bar x+(1-\lambda)\theta,(1-\lambda)\delta^2)$, $\lambda=\frac{\delta^2}{\delta^2+\sigma^2/n}$; and $\sum(x_i-\mu)^2=(n-1)s^2+n(\bar x-\mu)^2$ | SymPy: both identities ≡ 0 | ✔ |
| 19 | $P(X>120)=4/5$ from data $(120,125,130,160,150)$ | count $>120$ is 4 of 5 | ✔ |
| 23 | The posterior predictive integral equals the normal density with mean $\lambda\bar{x}+(1-\lambda)\theta$ and variance $\sigma^2+(1-\lambda)\delta^2$. | auto (SymPy pipeline) | ⚠ FAILED |
| 23 | $P[Y=1] = \frac{2}{10}\cdot\frac{1}{3} + \frac{1}{10}\cdot\frac{2}{3} = \frac{4}{30} = \frac{8}{60}$. | auto (SymPy pipeline) | ✔ |
| 161 | The stick-breaking weights $p_1=v_1$, $p_\ell=v_\ell\prod_{j=1}^{\ell-1}(1-v_j)$ for $\ell<m$, and $p_m=\prod_{\ell=1}^{m-1}(1-v_\ell)$ sum to one. | auto (SymPy pipeline) | ✔ |
| 161 | With joint $f(y_i, d_i=\ell) = p_\ell\, N(y_i\mid \mu+z_\ell, \sigma^2)$, Bayes' rule gives $P(d_i=\ell\mid y_i,\cdot) = p_\ell N(\mu+z_\ell,\sigma^2) / \sum_{k=1}^{m} p_k N(\mu+z_k,\sigma^2)$, and these probabilities sum to one. | auto (SymPy pipeline) | ✔ |

No numerical errors found on PDF pages 1–22. Handwritten corrections incorporated so far: p. 11 ("In which" → "we assume"), p. 12 ("$R$" → "$p$" in the Beta prior; "iid" struck for the single Binomial observation), plus margin annotations transcribed in place.




Pipeline summary: 4 machine checks on PDF pages ≥ 23; 3 passed, 1 flagged. Details: transcribe/out/verify-results.json

# Chapter 14 — Nonparametric Bayesian Statistics
*(PDF pages 161–161)*


### PDF page 161 (unnumbered insert)

*[This page is a fully handwritten lecture insert, in blue pen on ruled paper, with one red-ink correction. It carries no printed booklet page number.]*

**Stick-breaking Process**  |  MA 556 Spring 2024  |  April 19, 2024
*[all three parts of this heading line are hand-underlined]*

The idea to cluster the data and to add robustness against distributional assumptions (e.g., normality) by using mixtures.

The model,

$$y_1,\ldots,y_n \mid \mu,\sigma^2 \overset{iid}{\sim} N(\mu,\sigma^2)$$
$$\pi(\mu,\sigma^2) \propto \frac{1}{\sigma^2}$$

can be made more flexible and robust as follows

$$y_i \mid \rho,\mu,\sigma^2 \overset{ind}{\sim} \sum_{\ell=1}^{m_0} p_\ell\, N\!\left(\mu + z_\ell,\ \sigma^2\right), \qquad i=1,\ldots,n$$
$$\ell = 1,\ldots,m_0 \le n$$
$$z_\ell \mid \sigma^2,\rho \sim N\!\left(0,\ \sigma^2\,\frac{\rho}{1-\rho}\right) \qquad (m_0 \text{ unknown})$$
$$0 < \rho < 1$$

*(The booklet writes $z$ and $y$ with under-tildes to indicate vectors.)*

**Stick-breaking:** *[the word "Stick-breaking" is hand-underlined]*

$$p_1 = v_1,\quad p_2 = v_2(1-v_1),\quad \ldots,\quad p_m = \prod_{\ell=1}^{m-1}(1-v_\ell)$$

> ⚠ Check could not run (unsafe): The stick-breaking weights $p_1=v_1$, $p_\ell=v_\ell\prod_{j=1}^{\ell-1}(1-v_j)$ for $\ell<m$, and $p_m=\prod_{\ell=1}^{m-1}(1-v_\ell)$ sum to one. — rejected by import guard

*[margin note, boxed, with a bracket pointing at this display: "Two-parameter Pitman–Yor process. We can write $y \sim PY(a,b)$"]*

$$v_\ell \sim \text{Beta}\!\left(1-\delta_1,\ \frac{\delta_2}{1-\delta_2}(?) + (\ell-1)\delta_1\right), \qquad \ell = 1,\ldots,m_0$$
$$0 < \delta_1 < \tfrac{1}{2},\qquad \tfrac{1}{2} < \delta_2 < 1 \qquad \text{(computational stability)}$$

$$\pi\!\left(\mu,\sigma^2,\rho,\delta_1,\delta_2\right) \propto \frac{1}{\sigma^2}$$

Assuming that all pertinent parameters are stated wfg (?) *[reading uncertain — possibly "wlg", i.e. without loss of generality]*, we can write

$(d_i = \ell)$,

$$f\!\left(y, d \mid \rho, \mu, \sigma^2, z, \text{etc.}\right) \;=\; \prod_{\ell=1}^{m} \Big\{\, p_\ell\, N\!\left(\mu + z_\ell,\ \sigma^2\right) \Big\}^{\,I(d_i=\ell)}, \qquad \begin{array}{l}\ell = 1,\ldots,m\\ i = 1,\ldots,n\end{array}$$

We can now sample $d_i$, $i=1,\ldots,n$; $d_i$ tells us which cluster unit $i$ falls in ($d_i$ are latent variables) *(correction: "latent" is inserted in red ink, the red stroke cancelling the blue letter it replaces)*

Therefore,

$$P\!\left(d_i = \ell \mid y, z, \mu, \sigma^2, \text{etc.}\right) \;=\; \frac{p_\ell\, N\!\left(\mu + z_\ell,\ \sigma^2\right)}{\sum_{\ell=1}^{m} p_\ell\, N\!\left(\mu + z_\ell,\ \sigma^2\right)}, \qquad \begin{array}{l}\ell = 1,\ldots,m\\ i = 1,\ldots,n\end{array}$$

> ⚠ Check could not run (unsafe): With joint $f(y_i, d_i=\ell) = p_\ell\, N(y_i\mid \mu+z_\ell, \sigma^2)$, Bayes' rule gives $P(d_i=\ell\mid y_i,\cdot) = p_\ell N(\mu+z_\ell,\sigma^2) / \sum_{k=1}^{m} p_k N(\mu+z_k,\sigma^2)$, and these probabilities sum to one. — rejected by import guard

$\Big[$ Remark: At this point we have $m_0 \le n$; we may need to sample additional $z_\ell$, $v_\ell$; $\ell = m_0+1,\ldots,m$ from their priors. $\Big]$

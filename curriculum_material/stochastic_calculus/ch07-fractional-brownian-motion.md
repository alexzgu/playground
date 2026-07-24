# Chapter 7 — Fractional Brownian motion
*(PDF pages 243–248; book pages 237–242)*

### PDF page 243 (book page 237)

# Chapter 7 — Fractional Brownian motion

**7.1 Definition**

The assumptions of independent, stationary increments along with continuous paths give Brownian motion. In the last chapter we dropped the continuity assumption and obtained Lévy processes. In this chapter we will retain the assumptions of stationary increments and continuous paths, but will allow the increments to be dependent. The process $X_t$ we construct is called *fractional Brownian motion* and depends on a parameter $H \in (0, 1)$ called the *Hurst index*. It measures the correlation of the increments.

- When $H > 1/2$, the increments are positively correlated, that is, if the process has been increasing, then it is more likely to continue increasing.

- When $H < 1/2$, the increments are negatively correlated, that is, if the process has been increasing, then it is more likely to decrease in the future.

- If $H = 1/2$, the increments are uncorrelated and the process is the same as Brownian motion.

We will also assume that the process is self-similar.

- If $a > 0$, then the distribution of

$$ Y_t := a^{-H} X_{at} $$

is the same as that of $X_t$. In particular, $X_t$ has the same distribution as $t^H X_1$.

### PDF page 244 (book page 238)

Our final assumption is that the process is a centered Gaussian process.

- For every $t_1, \ldots, t_k$, the random vector $(X_{t_1}, \ldots, X_{t_k})$ has a joint normal distribution with mean zero.

We normalize so that $\mathrm{Var}(X_1) = \mathbb{E}[X_1^2] = 1$ and hence

$$ \mathrm{Var}(X_t) = \mathrm{Var}(t^H X_1) = t^{2H}\, \mathrm{Var}(X_1) = t^{2H}. $$

**Definition** If $H \in (0, 1)$, the *fractional Brownian motion with Hurst parameter $H$ ($fBm_H$)* is the centered (mean zero) Gaussian process $X_t$ with continuous paths such that for all $s, t$,

$$ \mathbb{E}\left[(X_t - X_s)^2\right] = |t - s|^{2H}. $$

Since

$$ \mathbb{E}\left[(X_t - X_s)^2\right] = \mathbb{E}\left[X_t^2\right] + \mathbb{E}\left[X_s^2\right] - 2\mathbb{E}\left[X_s X_t\right], $$

it follows that

$$ \mathrm{Cov}(X_s, X_t) = \mathbb{E}\left[X_s X_t\right] = \frac{1}{2}\left[s^{2H} + t^{2H} - |s - t|^{2H}\right]. \tag{7.1} $$

If $H = 1/2$, then fractional Brownian motion is the same as usual Brownian motion.

As in the case of Brownian motion, we must show that such a process exists. We will discuss this in the next section, but for now we assume it does exist. If $s < t$, note that

$$ \begin{aligned} \mathbb{E}\left[X_s\left(X_t - X_s\right)\right] &= \mathbb{E}\left[X_s X_t\right] - \mathbb{E}\left[X_s^2\right] \\ &= \frac{1}{2}\left[t^{2H} - s^{2H} - (t - s)^{2H}\right] \\ &\quad \begin{cases} > 0, & H > 1/2 \\ = 0, & H = 1/2 \\ < 0, & H < 1/2 \end{cases} . \end{aligned} $$

Since $X_{t+\delta} - X_t \sim N(0, \delta^{2H})$, we can write roughly

$$ |X_{t+\delta} - X_t| \approx \delta^H. $$

In other words, the Hölder exponent of $fBm_H$ is given by the Hurst index $H$. If $H > 1/2$, the paths are "smoother" than Brownian paths and if $H < 1/2$, the paths are "rougher".

### PDF page 245 (book page 239)

To determine correlations for large $t$, suppose $t$ is large. Then

$$ \begin{aligned} \mathbb{E}[(X_{s+1} - X_s)&(X_{s+t+1} - X_{s+t}] \\ &= \mathbb{E}[X_1\left(X_{t+1} - X_t\right)] \\ &= \mathbb{E}[X_1 X_{t+1}] - \mathbb{E}[X_1 X_t] \\ &= \frac{1}{2}\left[(t + 1)^{2H} + (t - 1)^{2H} - 2t^{2H}\right] \\ &\sim H\left(2H - 1\right) t^{2H-2}. \end{aligned} $$

The coefficient is positive for $H > 1/2$ and negative for $H < 1/2$. As $t$ goes to infinity the size of the correlation goes to zero like a power law.

## 7.2 Stochastic integral representation

We will give an expression for the fractional Brownian motion in terms of a stochastic integral. It will be useful to consider time going from $-\infty$ to $\infty$. Suppose $B_t^1, B_t^2$ are independent standard Brownian motions starting at the origin. If

$$ B_t = \begin{cases} B_t^1, & t \geq 0 \\ B_{-t}^2, & t \leq 0 \end{cases}, $$

then $B_t$ is standard Brownian motion from time $-\infty$ to $\infty$. The centering $B_0 = 0$ is rather arbitrary; we really think of this process as a collection of increments $\{B_t - B_s\}$ for $s < t$. Viewed this way, this is sometimes called *white noise*. We let $\mathcal{F}_t$ denote the information contained in the random variables $\{B_s - B_r : r < s \leq t\}$.

Suppose $f(r, t)$ is a continuous (nonrandom) function, and let

$$ Y_t = \int_{-\infty}^t f(r, t)\, dB_r = \lim_{n \to \infty} \sum f\left(\frac{k}{n}, t\right)\, \Delta B(k, n), $$

where

$$ \Delta B(k, n) = B_{(k+1)/n} - B_{k/n}, $$

and the sum is over all integers (positive and negative) with $(k + 1)/n \leq t$. Then $Y_t$ is a limit of centered normal random variables and hence is mean zero with variance

$$ \mathbb{E}[Y_t^2] = \int_{-\infty}^t f(r, t)^2\, dr. $$

### PDF page 246 (book page 240)

We assume this is finite for each $t$. Moreover if $s < t$, we can write

$$ Y_t - Y_s = \int_{-\infty}^s \left[f(r, t) - f(r, s)\right] dB_r + \int_s^t f(r, t)\, dB_r. $$

The right-hand side is the sum of two independent normal random variables: the first is $\mathcal{F}_s$-measurable and the second is independent of $\mathcal{F}_s$. Hence $Y_t - Y_s$ has a normal distribution. More generally, one can check that $Y_t$ is a Gaussian process whose covariance is given for $s < t$ by

$$ \mathbb{E}\left[Y_s Y_t\right] = \int_{-\infty}^s f(r, s)\, f(r, t)\, dr. $$

If we make the further assumption that $f(r, t) = \phi(t - r)$ for a one-variable function $\phi$, then the process $Y_t$ is stationary and has the form

$$ Y_t = \int_{-\infty}^t \phi(t - r)\, dB_r. \tag{7.2} $$

**Proposition 7.2.1.** *If*

$$ \phi(s) = c\, s^{H - \frac{1}{2}}, $$

*and $Y_t$ is defined as in (7.2), then $X_t = Y_t - Y_0$ is $fBm_H$. Here*

$$ c = c_H = \left[\frac{1}{2H} + \int_0^\infty \left[(1 + r)^{H - \frac{1}{2}} - r^{H - \frac{1}{2}}\right]^2 dr\right]^{-1/2}. $$

*Proof.* By construction, $X_t$ is a Gaussian process with continuous paths. Since $Y_t$ is stationary, the distribution of $X_t - X_s = Y_t - Y_s$ is the same as that of $X_{t-s} = Y_{t-s} - Y_0$. In particular, $\mathbb{E}[(X_t - X_s)^2] = \mathbb{E}[X_{t-s}^2]$. Hence we only need to show that $\mathbb{E}[X_t^2] = t^{2H}$. Note that

$$ X_t = \int_{-\infty}^0 \left[\phi(t - r) - \phi(-r)\right] dB_r + \int_0^t \phi(t - r)\, dB_r. $$

### PDF page 247 (book page 241)

The random variables on the right-hand side are independent and

$$
c^{-2} \operatorname{Var} \left[ \int_{-\infty}^{0} [\phi(t-r) - \phi(-r)] \, dB_r \right]
$$
$$
\begin{aligned}
&= \int_{-\infty}^{0} [(t-r)^{H-\frac{1}{2}} - (-r)^{H-\frac{1}{2}}]^2 \, dr \\
&= \int_{0}^{\infty} [(t+r)^{H-\frac{1}{2}} - r^{H-\frac{1}{2}}]^2 \, dr \\
&= \int_{0}^{\infty} [(t+st)^{H-\frac{1}{2}} - (st)^{H-\frac{1}{2}}]^2 \, t \, ds \\
&= t^{2H} \int_{0}^{\infty} [(1+s)^{H-\frac{1}{2}} - s^{H-\frac{1}{2}}]^2 \, ds,
\end{aligned}
$$
$$
c^{-2} \operatorname{Var} \left[ \int_{0}^{t} \phi(t-r) \, dB_r \right] = \int_{0}^{t} (t-r)^{2H-1} \, dr = \frac{t^{2H}}{2H}.
$$

If we choose $c$ as in (7.3), we get $\mathbb{E}[X_t^2] = t^{2H}$. $\qquad\square$

## 7.3 Simulation

Because the fractional Brownian motion has long range dependence it is not obvious how to do simulations. The stochastic integral represetation [sic] (7.2) is difficult to use because it uses the value of the Brownian motion for all negative times. However, there is a way to do simulations that uses only the fact that $fBm_H$ is a Gaussian process with continuous paths. Let us choose a step size $\Delta t = 1/N$; continuity tells us that it should suffice to sample

$$
Y_1, Y_2, \ldots
$$

where $Y_j = X_{j/N}$. For each $n$, the random vector $(Y_1, \ldots, Y_n)$ has a centered Gaussian distribution with covariance matrix $\Gamma = [\Gamma_{jk}]$. Given $\Gamma$ we claim that we can find numbers $a_{jk}$ with $a_{jk} = 0$ if $k > j$, and independent standard normal random variables $Z_1, Z_2, \ldots$ such that

$$
Y_n = a_{n1} Z_1 + \cdots + a_{nn} Z_n. \tag{7.3}
$$

In matrix notation, $A = [a_{jk}]$ is a lower triangular matrix such that $\Gamma = AA^T$.

### PDF page 248 (book page 242)

This decomposition $\Gamma = AA^T$ is sometimes called the *Cholesky decomposition*. We will now show that it exists by giving an algorithm for finding the matrix. We start by setting

$$
a_{11} = \sqrt{\Gamma_{11}}.
$$

Suppose we have found the first $k-1$ rows of $A$. This is a lower triangular $(k-1) \times (k-1)$ matrix. Suppose $j < k$. Then,

$$
\Gamma_{jk} = \mathbb{E} \left[ Y_j Y_k \right] = \sum_{i=1}^{j} a_{ji} \, a_{ki}.
$$

The coefficients $a_{jk}$ for $j = 1, \ldots, k-1$ can be found by solving these $k-1$ linear equation in $k-1$ unknowns (one uses the fact that $\Gamma$ is nonnegatve [sic] definite to show there is a unique solution), and then one sets

$$
a_{kk} = \sqrt{\Gamma_{kk} - \sum_{i=1}^{k-1} a_{ki}^2}.
$$

We see that this decomposition is unique if we impose the condition $a_{kk} \geq 0$.

¿From a practical perspective, these computations are done with computer packages. Note that one only needs to compute the coefficients $a_{jk}$ once and store them. Then multiple simulations can be done using (7.3).

---

The Cholesky decomposition can be derived from the Gram-Schmidt process. Consider the Hilbert space of mean-zero $L^2$ random variables and let $H_n$ denote the finite dimensonal [sic] subspace spanned by $Y_1, \ldots, Y_n$. Let $P_n$ denote the projection onto $H_n$ which is the same as the conditional expectation,

$$
P_n X = E[X \mid Y_1, \ldots, Y_n].
$$

Then we define

$$
Z_n = \frac{Y_n - P_{n-1} Y_n}{\|Y_n - P_{n-1} Y_n\|_2}.
$$

Since $H_n$ is also the subspace spanned by $Z_1, \ldots, Z_n$, we can write

$$
P_{n-1} Y_n = \sum_{j=1}^{n-1} a_{jn} \, Z_j,
$$

for unique scalars $a_{jn}$, and we set $a_{nn} = \|Y_n - P_{n-1} Y_n\|_2$.

---

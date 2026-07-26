"""bayeskit — the small toolbox this guide builds and then reuses.

Nothing here is magic, and nothing here is long. Every function is one you
write yourself in an early chapter; they live here so later chapters can
import them instead of re-deriving them. Read the source: it is meant to be
read, and it is the honest answer to "what is the library actually doing?"

    from bayeskit import grid_posterior, sample_grid, hdi, summarize

Built in:
  ch01  grid_posterior, sample_grid
  ch02  hdi, pi, summarize, prob_of
  ch04  quap (quadratic / Laplace approximation), hessian_fd
  ch05  rhat, ess, mcmc_summary
  ch12  lppd, waic, psis_loo, gpd_fit
  ch13  ece, calibration_curve
"""

from __future__ import annotations

import numpy as np
from scipy import optimize

__all__ = [
    "midpoint_grid", "grid_posterior", "sample_grid", "hdi", "pi", "summarize",
    "prob_of",
    "quap", "hessian_fd", "rhat", "ess", "mcmc_summary",
    "lppd", "waic", "psis_loo", "gpd_fit", "ece", "calibration_curve",
]


# --------------------------------------------------------------- ch01: grids

def midpoint_grid(lo, hi, k):
    """k evenly spaced cell *centres* on [lo, hi].

    Centres, not edges: the edges of a parameter's range are where likelihoods
    are often exactly zero (a rate of 0 cannot produce a success), and where a
    decision threshold lands ambiguously between two grid points.
    """
    edges = np.linspace(lo, hi, k + 1)
    return 0.5 * (edges[:-1] + edges[1:])


def grid_posterior(log_lik, grid, log_prior=None):
    """Posterior on a 1-D grid, computed in log space.

    log_lik   : callable, log p(data | theta), vectorized over `grid`
    grid      : 1-D array of parameter values
    log_prior : callable, log p(theta); default flat

    Returns an array of probabilities that sums to 1 (a *discrete* posterior:
    each entry is the probability of that grid point, not a density).
    """
    lp = np.zeros_like(grid, dtype=float) if log_prior is None else log_prior(grid)
    log_post = lp + log_lik(grid)
    log_post -= log_post.max()          # subtract the max before exp: no overflow
    post = np.exp(log_post)
    return post / post.sum()


def sample_grid(grid, post, size, rng):
    """Draw `size` posterior samples from a grid posterior (with replacement)."""
    return rng.choice(grid, size=size, p=post)


# ------------------------------------------------------- ch02: summarizing

def hdi(samples, prob=0.89):
    """Narrowest interval containing `prob` of the samples (highest density).

    Scans every window of the right width in the sorted sample and keeps the
    shortest. For a bimodal posterior a single interval is a lie; check the
    histogram before quoting one.
    """
    x = np.sort(np.asarray(samples).ravel())
    n = x.size
    k = max(1, int(np.floor(prob * n)))
    if k >= n:
        return x[0], x[-1]
    widths = x[k:] - x[:n - k]
    i = int(np.argmin(widths))
    return x[i], x[i + k]


def pi(samples, prob=0.89):
    """Percentile interval: equal probability mass cut off each tail."""
    a = (1 - prob) / 2
    lo, hi = np.quantile(np.asarray(samples).ravel(), [a, 1 - a])
    return lo, hi


def prob_of(condition):
    """P(condition) estimated by counting samples. `condition` is a bool array."""
    return float(np.mean(np.asarray(condition, dtype=float)))


def summarize(samples, prob=0.89, names=None):
    """Mean / sd / interval table for a dict (or 2-D array) of samples.

    Returns a pandas DataFrame; import pandas lazily so the light chapters
    don't pay for it.
    """
    import pandas as pd

    if not isinstance(samples, dict):
        arr = np.atleast_2d(np.asarray(samples))
        if arr.shape[0] < arr.shape[1]:
            arr = arr.T
        names = names or [f"x{j}" for j in range(arr.shape[1])]
        samples = {nm: arr[:, j] for j, nm in enumerate(names)}
    rows = []
    for name, s in samples.items():
        s = np.asarray(s).ravel()
        lo, hi = hdi(s, prob)
        rows.append({"param": name, "mean": s.mean(), "sd": s.std(ddof=1),
                     f"{int(prob*100)}% lo": lo, f"{int(prob*100)}% hi": hi})
    return pd.DataFrame(rows).set_index("param")


# ------------------------------------------------- ch04: quadratic approx

def hessian_fd(f, x, eps=None):
    """Hessian of a scalar function by central finite differences."""
    x = np.asarray(x, dtype=float)
    n = x.size
    if eps is None:
        eps = np.maximum(np.abs(x), 1.0) * (np.finfo(float).eps ** (1 / 4))
    eps = np.broadcast_to(np.asarray(eps, dtype=float), (n,)).copy()
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            ei = np.zeros(n); ei[i] = eps[i]
            ej = np.zeros(n); ej[j] = eps[j]
            H[i, j] = H[j, i] = (
                f(x + ei + ej) - f(x + ei - ej) - f(x - ei + ej) + f(x - ei - ej)
            ) / (4 * eps[i] * eps[j])
    return H


class QuapFit:
    """A Gaussian approximation to a posterior: mode + curvature."""

    def __init__(self, names, mode, cov, neg_log_post, success):
        self.names = list(names)
        self.mode = np.asarray(mode, dtype=float)
        self.cov = np.asarray(cov, dtype=float)
        self.sd = np.sqrt(np.diag(self.cov))
        self.neg_log_post = neg_log_post
        self.success = success

    @property
    def mean(self):
        return dict(zip(self.names, self.mode))

    def sample(self, size, rng):
        """Draw from the Gaussian approximation. Returns {name: array}."""
        draws = rng.multivariate_normal(self.mode, self.cov, size=size)
        return {nm: draws[:, j] for j, nm in enumerate(self.names)}

    def corr(self):
        d = np.sqrt(np.diag(self.cov))
        return self.cov / np.outer(d, d)

    def __repr__(self):
        parts = [f"{nm}={m:.3f}±{s:.3f}"
                 for nm, m, s in zip(self.names, self.mode, self.sd)]
        return f"QuapFit({', '.join(parts)})"


def quap(neg_log_post, start, method="BFGS"):
    """Quadratic (Laplace) approximation: fit a Gaussian at the posterior mode.

    neg_log_post : callable taking a 1-D array ordered like `start`
    start        : dict {name: initial value}

    The posterior is approximated by N(mode, H^-1) where H is the Hessian of
    the *negative* log posterior at the mode. Exact when the posterior is
    Gaussian, good when it is unimodal and n is decent, misleading when it is
    skewed or bounded — so put parameters on an unconstrained scale
    (log sigma, not sigma) before handing them over.
    """
    names = list(start)
    x0 = np.array([start[k] for k in names], dtype=float)
    res = optimize.minimize(neg_log_post, x0, method=method)
    H = hessian_fd(neg_log_post, res.x)
    cov = np.linalg.inv(H)
    return QuapFit(names, res.x, cov, neg_log_post, bool(res.success))


# ------------------------------------------------------ ch05: MCMC checks

def _autocov(x):
    """Autocovariance of a 1-D chain via FFT (all lags)."""
    x = np.asarray(x, dtype=float)
    n = x.size
    x = x - x.mean()
    m = 1 << (2 * n - 1).bit_length()
    f = np.fft.rfft(x, m)
    ac = np.fft.irfft(f * np.conjugate(f), m)[:n]
    return ac / n


def _split(chains):
    """Split each chain in half — catches chains that drift."""
    c = np.atleast_2d(np.asarray(chains, dtype=float))
    m, n = c.shape
    h = n // 2
    return np.concatenate([c[:, :h], c[:, h:2 * h]], axis=0)


def rhat(chains):
    """Split R-hat: between-chain spread vs within-chain spread.

    chains: (n_chains, n_draws). Near 1.0 is healthy; > 1.01 means the chains
    disagree about where the posterior is, and you should not use the draws.
    """
    c = _split(chains)
    m, n = c.shape
    W = c.var(axis=1, ddof=1).mean()
    B = n * c.mean(axis=1).var(ddof=1)
    var_plus = ((n - 1) * W + B) / n
    return float(np.sqrt(var_plus / W))


def ess(chains):
    """Effective sample size (Stan/BDA3 recipe, Geyer initial positive seq).

    chains: (n_chains, n_draws). Answers "how many independent draws is this
    correlated chain worth?" Report this, not the number of iterations.
    """
    c = _split(chains)
    m, n = c.shape
    W = c.var(axis=1, ddof=1).mean()
    B = n * c.mean(axis=1).var(ddof=1) if m > 1 else 0.0
    var_plus = ((n - 1) * W + B) / n
    if var_plus <= 0:
        return float(m * n)
    acov = np.mean([_autocov(row) for row in c], axis=0)   # 1/n normalisation
    rho = 1.0 - (W - acov) / var_plus                      # BDA3 (11.7)
    rho[0] = 1.0
    # Geyer's initial positive sequence: sum consecutive pairs of lags while
    # the pair sum stays positive, forcing the sequence to decrease.
    k = (rho.size // 2) * 2
    pair = rho[:k].reshape(-1, 2).sum(axis=1)
    keep = int(np.argmax(pair < 0)) if np.any(pair < 0) else pair.size
    pair = np.minimum.accumulate(pair[:max(keep, 1)])
    tau = -1.0 + 2.0 * pair.sum()
    return float(m * n / max(tau, 1e-12))


def mcmc_summary(samples, prob=0.89):
    """summarize() plus R-hat and ESS. samples: {name: (chains, draws)}."""
    import pandas as pd

    rows = []
    for name, s in samples.items():
        arr = np.atleast_2d(np.asarray(s))
        flat = arr.ravel()
        lo, hi = hdi(flat, prob)
        rows.append({"param": name, "mean": flat.mean(), "sd": flat.std(ddof=1),
                     f"{int(prob*100)}% lo": lo, f"{int(prob*100)}% hi": hi,
                     "ess": round(ess(arr)), "rhat": round(rhat(arr), 3)})
    return pd.DataFrame(rows).set_index("param")


# --------------------------------------------- ch12: out-of-sample scoring

def lppd(log_lik):
    """Pointwise log posterior predictive density. log_lik: (draws, points)."""
    S = log_lik.shape[0]
    from scipy.special import logsumexp
    return logsumexp(log_lik, axis=0) - np.log(S)


def waic(log_lik):
    """WAIC on the elpd scale (higher is better) + its penalty term."""
    l = lppd(log_lik)
    penalty = log_lik.var(axis=0, ddof=1)
    return {"elpd": float((l - penalty).sum()),
            "p_waic": float(penalty.sum()),
            "se": float(np.sqrt(log_lik.shape[1] * np.var(l - penalty, ddof=1)))}


def gpd_fit(x):
    """Fit a generalized Pareto to exceedances (Zhang & Stephens 2009).

    Returns (k, sigma). k is the shape: k > 0.7 means the importance weights
    have a tail so heavy that the estimate is not to be trusted.
    """
    x = np.sort(np.asarray(x, dtype=float))
    n = x.size
    m = 30 + int(np.sqrt(n))
    prior = 3.0
    jj = np.arange(1, m + 1)
    b = 1.0 / x[-1] + (1 - np.sqrt(m / (jj - 0.5))) / (prior * x[int(n / 4 + 0.5) - 1])
    k_j = np.mean(np.log1p(-b[:, None] * x[None, :]), axis=1)
    len_j = n * (np.log(-b / k_j) - k_j - 1)
    weights = 1.0 / np.sum(np.exp(len_j[None, :] - len_j[:, None]), axis=1)
    b_hat = np.sum(b * weights)
    k_hat = float(np.mean(np.log1p(-b_hat * x)))
    sigma = float(-k_hat / b_hat)
    # small-sample bias correction (as in the loo package)
    k_hat = k_hat * n / (n + 10.0) + 10.0 * 0.5 / (n + 10.0)
    return k_hat, sigma


def psis_loo(log_lik):
    """Pareto-smoothed importance sampling LOO. log_lik: (draws, points).

    Estimates the expected log density of a *new* observation, using the fit
    you already have — no refitting. Returns elpd (higher is better), its
    standard error, the effective number of parameters, and the per-point
    Pareto k diagnostics (any k > 0.7 = that point is too influential for the
    approximation; refit without it if you care).
    """
    from scipy.special import logsumexp

    S, N = log_lik.shape
    cutoff = int(min(0.2 * S, 3 * np.sqrt(S)))
    elpd_i = np.empty(N)
    khat = np.empty(N)
    for i in range(N):
        lw = -log_lik[:, i]                     # log raw importance ratios
        lw = lw - lw.max()
        order = np.argsort(lw)
        tail = order[-cutoff:]
        cut = lw[order[-cutoff - 1]]
        exceed = np.exp(lw[tail]) - np.exp(cut)
        k, sigma = gpd_fit(exceed)
        khat[i] = k
        if k < 1.0 and sigma > 0:               # replace the tail by GPD quantiles
            q = (np.arange(cutoff) + 0.5) / cutoff
            fitted = np.exp(cut) + (sigma / k) * (np.power(1 - q, -k) - 1)
            lw[tail] = np.log(np.minimum(fitted, np.exp(lw.max())))
        elpd_i[i] = logsumexp(lw + log_lik[:, i]) - logsumexp(lw)
    return {"elpd": float(elpd_i.sum()),
            "se": float(np.sqrt(N * np.var(elpd_i, ddof=1))),
            "p_loo": float((lppd(log_lik) - elpd_i).sum()),
            "elpd_i": elpd_i, "khat": khat}


# ------------------------------------------------------- ch13: calibration

def calibration_curve(p, y, bins=10):
    """Predicted probability vs observed frequency, in equal-width bins."""
    p, y = np.asarray(p, float), np.asarray(y, float)
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges) - 1, 0, bins - 1)
    out = []
    for b in range(bins):
        m = idx == b
        if m.sum():
            out.append((p[m].mean(), y[m].mean(), int(m.sum())))
    return np.array(out)


def ece(p, y, bins=10):
    """Expected calibration error: average |predicted - observed|, size-weighted."""
    tab = calibration_curve(p, y, bins)
    w = tab[:, 2] / tab[:, 2].sum()
    return float(np.sum(w * np.abs(tab[:, 0] - tab[:, 1])))

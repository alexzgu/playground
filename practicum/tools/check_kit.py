#!/usr/bin/env python3
"""Validate bayeskit's hand-written diagnostics against ArviZ.

The guide implements R-hat, ESS and PSIS-LOO from scratch so the reader can
see what they are. This script is the receipt that the from-scratch versions
agree with the reference implementation. Run from practicum/:

    python tools/check_kit.py
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from bayeskit import ess, rhat, psis_loo, waic, hdi, quap  # noqa: E402

rng = np.random.default_rng(0)
fails = []


def report(name, mine, ref, tol):
    rel = abs(mine - ref) / max(abs(ref), 1e-12)
    ok = rel < tol
    print(f"[{'ok ' if ok else 'XX '}] {name:28s} mine={mine:12.4f} "
          f"ref={ref:12.4f}  rel={rel:.2e}")
    if not ok:
        fails.append(name)


# AR(1) chains with known autocorrelation --------------------------------
def ar1(rho, n, m, rng):
    x = np.zeros((m, n))
    for j in range(m):
        e = rng.normal(0, np.sqrt(1 - rho ** 2), n)
        for t in range(1, n):
            x[j, t] = rho * x[j, t - 1] + e[t]
    return x


import arviz as az  # noqa: E402

for rho in (0.0, 0.5, 0.9):
    ch = ar1(rho, 2000, 4, rng)
    report(f"ess  AR(1) rho={rho}", ess(ch), float(az.ess(ch, method="mean")), 0.05)
    report(f"rhat AR(1) rho={rho}", rhat(ch), float(az.rhat(ch, method="split")), 1e-3)

# hdi ---------------------------------------------------------------------
s = rng.normal(size=20000)
lo, hi = hdi(s, 0.89)
rlo, rhi = az.hdi(s, hdi_prob=0.89)
report("hdi lo", lo, float(rlo), 0.05)
report("hdi hi", hi, float(rhi), 0.05)

# PSIS-LOO / WAIC on a real posterior -------------------------------------
# Conjugate normal model: theta ~ N(0,10^2), y_i ~ N(theta, 1)
y = rng.normal(1.5, 1.0, size=40)
prec = 1 / 100 + len(y)
mn, sdn = y.sum() / prec, np.sqrt(1 / prec)
draws = rng.normal(mn, sdn, size=2000)
ll = -0.5 * np.log(2 * np.pi) - 0.5 * (y[None, :] - draws[:, None]) ** 2

idata = az.from_dict(posterior={"theta": draws.reshape(2, 1000)},
                     log_likelihood={"y": ll.reshape(2, 1000, len(y))})
mine = psis_loo(ll)
ref = az.loo(idata, pointwise=True)
report("psis-loo elpd", mine["elpd"], float(ref.elpd_loo), 2e-3)
report("psis-loo p_loo", mine["p_loo"], float(ref.p_loo), 5e-2)
report("psis-loo se", mine["se"], float(ref.se), 5e-2)
report("max |khat diff|", float(np.max(np.abs(mine["khat"] - ref.pareto_k.values))),
       0.0 + 1e-9, np.inf)  # informational
w = waic(ll)
refw = az.waic(idata)
report("waic elpd", w["elpd"], float(refw.elpd_waic), 2e-3)

# quap against a conjugate posterior --------------------------------------
def nlp(v):
    theta = v[0]
    return -(-0.5 * (theta / 10) ** 2 - 0.5 * np.sum((y - theta) ** 2))


fit = quap(nlp, {"theta": 0.0})
report("quap mean", fit.mode[0], mn, 1e-5)
report("quap sd", fit.sd[0], sdn, 1e-4)

print()
if fails:
    print("FAILED:", fails)
    raise SystemExit(1)
print("all bayeskit diagnostics agree with ArviZ")

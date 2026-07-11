#!/usr/bin/env python3
"""Smoke-tested NumPyro/ArviZ idioms for the installed versions.

This file is BOTH a test and the authoritative API reference for module
authors: if an idiom is not shown passing here, do not use it in a module.
Context: pytensor's C backend is broken in this codespace (static libpython),
so PyMC can only run in slow pure-python mode — NumPyro (JAX, no C compile)
is the course PPL. Run:  python tools/ppl_idioms.py
"""

import os
import time

os.environ.setdefault("MPLBACKEND", "Agg")
t0 = time.perf_counter()
results: list[tuple[str, str]] = []


def check(name: str):
    def deco(fn):
        try:
            fn()
            results.append((name, "PASS"))
        except Exception as e:  # noqa: BLE001
            results.append((name, f"FAIL: {type(e).__name__}: {e}"))
        return fn
    return deco


import numpy as np  # noqa: E402
import jax  # noqa: E402
import jax.numpy as jnp  # noqa: E402
import numpyro  # noqa: E402
import numpyro.distributions as dist  # noqa: E402
from numpyro.infer import MCMC, NUTS, SVI, Predictive, Trace_ELBO  # noqa: E402
from numpyro.infer.autoguide import AutoNormal  # noqa: E402
from numpyro.infer.reparam import LocScaleReparam  # noqa: E402
from numpyro.handlers import reparam  # noqa: E402
import arviz as az  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

print(f"numpyro {numpyro.__version__} | jax {jax.__version__} | arviz {az.__version__}")

SEED = 0
rng = np.random.default_rng(SEED)
# RULE: pass observations as NUMPY arrays (not jnp) — arviz mutates obs-shaped
# buffers internally and jax arrays are immutable.
y_obs = rng.normal(1.0, 2.0, size=50)
N_OBS = 50
STORE: dict = {}


def normal_model(N, y=None):
    # RULE: wrap observation sites in a plate sized by an explicit arg, so
    # Predictive() can generate full-shape prior/posterior predictive draws.
    mu = numpyro.sample("mu", dist.Normal(0.0, 10.0))
    sigma = numpyro.sample("sigma", dist.HalfNormal(5.0))
    with numpyro.plate("N", N):
        numpyro.sample("y", dist.Normal(mu, sigma), obs=y)


@check("NUTS sampling + extra_fields diverging")
def _sample():
    mcmc = MCMC(NUTS(normal_model), num_warmup=400, num_samples=400,
                num_chains=2, chain_method="sequential", progress_bar=False)
    mcmc.run(jax.random.PRNGKey(SEED), N=N_OBS, y=y_obs,
             extra_fields=("diverging", "energy"))
    STORE["mcmc"] = mcmc
    n_div = int(mcmc.get_extra_fields()["diverging"].sum())
    print(f"  mu mean {float(mcmc.get_samples()['mu'].mean()):.3f}, "
          f"divergences {n_div}")


@check("az.from_numpyro -> summary/ess/rhat, ci_prob kwarg")
def _arviz():
    idata = az.from_numpyro(STORE["mcmc"])
    STORE["idata"] = idata
    s = az.summary(idata, ci_prob=0.95)
    print(s.to_string())
    print(f"  ess {float(az.ess(idata)['mu']):.0f} "
          f"rhat {float(az.rhat(idata)['mu']):.4f}")
    assert "diverging" in idata.sample_stats


@check("posterior predictive via Predictive(model, samples)")
def _ppc():
    post = STORE["mcmc"].get_samples()
    pred = Predictive(normal_model, posterior_samples=post)
    yrep = pred(jax.random.PRNGKey(1), N=N_OBS)["y"]   # y omitted -> simulated
    assert yrep.shape == (800, N_OBS)
    print(f"  ppc mean {float(yrep.mean()):.3f}")


@check("prior predictive via Predictive(model, num_samples)")
def _prior():
    pred = Predictive(normal_model, num_samples=500)
    y0 = pred(jax.random.PRNGKey(2), N=N_OBS)["y"]
    assert y0.shape == (500, N_OBS)
    print(f"  prior pred sd {float(y0.std()):.1f}")


@check("SVI AutoNormal (ADVI equivalent) + guide sample")
def _svi():
    guide = AutoNormal(normal_model)
    svi = SVI(normal_model, guide, numpyro.optim.Adam(0.05), Trace_ELBO())
    res = svi.run(jax.random.PRNGKey(SEED), 3000, N=N_OBS, y=y_obs,
                  progress_bar=False)
    post = guide.sample_posterior(jax.random.PRNGKey(3), res.params,
                                  sample_shape=(500,))
    print(f"  svi mu mean {float(post['mu'].mean()):.3f} "
          f"(final elbo loss {float(res.losses[-1]):.1f})")


@check("non-centered via LocScaleReparam handler (8-schools shape)")
def _noncentered():
    J = 8
    sigma_j = jnp.asarray([15., 10., 16., 11., 9., 11., 10., 18.])
    yj = jnp.asarray([28., 8., -3., 7., -1., 1., 18., 12.])

    def schools(y=None):
        mu = numpyro.sample("mu", dist.Normal(0, 5))
        tau = numpyro.sample("tau", dist.HalfCauchy(5))
        with numpyro.plate("J", J):
            theta = numpyro.sample("theta", dist.Normal(mu, tau))
            numpyro.sample("y", dist.Normal(theta, sigma_j), obs=y)

    re = reparam(schools, config={"theta": LocScaleReparam(0)})
    mcmc = MCMC(NUTS(re), num_warmup=400, num_samples=400, num_chains=2,
                chain_method="sequential", progress_bar=False)
    mcmc.run(jax.random.PRNGKey(SEED), y=yj, extra_fields=("diverging",))
    ndiv = int(mcmc.get_extra_fields()["diverging"].sum())
    print(f"  8-schools noncentered: tau mean "
          f"{float(mcmc.get_samples()['tau'].mean()):.2f}, div {ndiv}")


@check("az.plot_trace -> PlotCollection.savefig (arviz 1.x API)")
def _plot():
    # RULE: arviz 1.x plot_* returns a PlotCollection; save via .savefig().
    pc = az.plot_trace(STORE["idata"], var_names=["mu"])
    os.makedirs("tools/logs", exist_ok=True)
    pc.savefig("tools/logs/idiom_trace.png")
    plt.close("all")
    print("  trace plot written")


@check("deterministic sites + manual numpy log_likelihood for az.loo")
def _loo():
    # RULE: az.loo chokes on jax-backed log_likelihood arrays; compute
    # log-lik via numpyro.infer.log_likelihood, cast to NUMPY, attach.
    from numpyro.infer import log_likelihood as np_loglik
    import xarray as xr

    def model_ll(N, y=None):
        mu = numpyro.sample("mu", dist.Normal(0.0, 10.0))
        sigma = numpyro.sample("sigma", dist.HalfNormal(5.0))
        numpyro.deterministic("snr", mu / sigma)
        with numpyro.plate("N", N):
            numpyro.sample("y", dist.Normal(mu, sigma), obs=y)

    mcmc = MCMC(NUTS(model_ll), num_warmup=300, num_samples=300,
                num_chains=2, chain_method="sequential", progress_bar=False)
    mcmc.run(jax.random.PRNGKey(SEED), N=N_OBS, y=y_obs)
    idata = az.from_numpyro(mcmc)
    assert "snr" in idata.posterior
    ll = np.asarray(np_loglik(model_ll, mcmc.get_samples(),
                              N=N_OBS, y=y_obs)["y"])
    idata["log_likelihood"] = xr.Dataset(
        {"y": (("chain", "draw", "y_dim"), ll.reshape(2, 300, N_OBS))})
    loo = az.loo(idata)
    print(f"  elpd_loo {float(loo['elpd']):.1f}")


print(f"\n== idiom results ({time.perf_counter()-t0:.0f}s total) ==")
bad = 0
for name, verdict in results:
    print(f"[{'ok ' if verdict == 'PASS' else 'XX '}] {name}: {verdict}")
    bad += verdict != "PASS"
raise SystemExit(1 if bad else 0)

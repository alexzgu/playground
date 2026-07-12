# 12. HMC and NUTS: Geometry Wins in High Dimension  [SIGNATURE S1]

> **Spine.** In high dimension almost none of the probability mass sits at the mode — it lives in a thin shell called the typical set, and random walks crawl there while gradients-plus-momentum take long coherent strides along it.
> **Which line?** Line 2 (conditioning), the computational engine: when the posterior integral is intractable and the parameter vector is long, this is how you actually draw from $p(\theta\mid y)$.
> **Promise.** After this module you can explain why the mode is the wrong place to look in high dimension, why a well-tuned random walk still dies as dimension grows, how one screen of leapfrog code turns geometry into efficient sampling, and what a *divergence* physically is — the fingerprint you will read for the rest of the course.
> **Prereqs.** Modules 09 (Monte Carlo, ESS), 10 (Metropolis–Hastings, the 0.234 tuning law, detailed balance), 11 (Gibbs, "posterior correlation is the enemy").
> **Runtime.** ~47 s measured (the two JAX/NumPyro funnel fits dominate; JIT compile included).
> **Sources.** Booklet BDA3-HMC/Stan insert and ch. 15; Neal, *MCMC using Hamiltonian dynamics*, by concept; Lawler ch. 3–5 (Langevin/SDE) by concept.

Here is a question with an obvious wrong answer. Draw $\theta$ from a standard Gaussian in $d=1000$ dimensions, $\theta\sim N(0,I_{1000})$. **Where is most of the probability mass?** The density $p(\theta)\propto \exp(-\tfrac12\lVert\theta\rVert^2)$ is largest at the origin and falls off in every direction, so the mode $\theta=0$ is the single most probable point by a colossal margin. The trained reflex — the one behind plug-in-at-the-MAP, behind "initialize the sampler at the mode," behind Laplace approximation — says *the mass is near the mode.* Commit to that answer. It is wrong, and the size of the error is the reason this module exists.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "12-hmc"                          # this module's figure dir
FIG = Path("figures") / SLUG
FIG.mkdir(parents=True, exist_ok=True)
SEED = 0
rng = np.random.default_rng(SEED)

plt.rcParams.update({
    "figure.figsize": (7, 4), "figure.dpi": 110, "savefig.dpi": 150,
    "savefig.bbox": "tight", "axes.grid": True, "grid.alpha": 0.3,
    "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 11,
})

def save(fig, name):
    out = FIG / f"{name}.png"
    fig.savefig(out)
    plt.close(fig)
    print(f"[fig] {out}")
```

## 12.1 The donut: where the mass actually lives  [SIGNATURE S1]

**Run** the experiment. For each dimension $d$ draw a cloud of standard Gaussians and look at their *radii* $\lVert\theta\rVert$ — the distance from the mode.

```python
# Where is the mass of N(0, I_d)? Look at the distance from the mode.
dims = (1, 10, 100, 1000)
norm_samples = {}
print(f"sqrt(1000) = {np.sqrt(1000):.1f}")
for d in dims:
    X = rng.standard_normal(size=(20000, d))
    r = np.sqrt((X ** 2).sum(1))            # ||theta|| = distance from the mode 0
    norm_samples[d] = r
    print(f"d={d:>4}:  mean ||theta|| = {r.mean():5.2f}   sd = {r.std():.2f}   sqrt(d) = {np.sqrt(d):5.1f}")

r1000 = norm_samples[1000]
half = np.sqrt(1000) / 2
frac_near = (r1000 < half).mean()
print(f"fraction of N(0,I_1000) within {half:.1f} of the mode = {frac_near:.4f}")
print(f"log-density advantage of the mode over the shell = d/2 = {1000/2:.0f} nats")
```

The radii do not sit near zero. They pile up around $\sqrt d$: at $d=1000$ the mean distance from the mode is `31.61`, essentially $\sqrt{1000}=$ `31.6`, with a standard deviation of only `0.71`. Not one of the 20,000 draws in 1000 dimensions lands within half that radius of the mode — the fraction inside is `0.0000`. **The mode is in a desert.**

**Reconcile.** Both facts are true at once: the mode has the highest *density*, and the mode has essentially no *mass*. Mass is density times volume, and in $d$ dimensions the volume of a thin shell at radius $r$ grows like $r^{d-1}$ — astronomically fast. The density at radius $r$ falls like $\exp(-r^2/2)$. Their product, the radial mass, is $\propto r^{d-1}e^{-r^2/2}$, sharply peaked at $r=\sqrt{d-1}\approx\sqrt d$. A single point at the shell is fantastically less probable than the mode — the log-density gap is exactly $d/2=$ `500` nats, so the mode is $e^{500}$ times denser per unit volume — and yet there is so much *more room* out at radius $\sqrt d$ that the shell wins in aggregate, overwhelmingly. This shell is the **typical set**. In $d=2$ it is a fuzzy donut you can see; in $d=1000$ it is a razor-thin spherical crust holding all the probability, with the "most probable point" stranded uselessly at its empty center.

```python
# Figure: the radius distribution concentrates on a shell at sqrt(d).
fig, ax = plt.subplots()
colors = ["C0", "C1", "C2", "C3"]
for d, c in zip(dims, colors):
    r = norm_samples[d]
    ax.hist(r, bins=80, density=True, histtype="step", lw=2, color=c,
            label=f"d={d}")
    ax.axvline(np.sqrt(d), color=c, ls=":", lw=1)
ax.set_xlabel(r"distance from the mode  $\|\theta\|$")
ax.set_ylabel("density")
ax.set_title("The typical set: mass concentrates on a shell at radius √d")
ax.legend(title="dimension")
save(fig, "typical-set")
```

![Radius histograms for d=1,10,100,1000; each (for d ≥ 10) is a narrow bump centered on √d (dotted line), marching rightward and staying the same width as dimension grows — d=1 is the degenerate case, a half-normal pressed against 0 rather than a bump.](figures/12-hmc/typical-set.png)

Two procedures die on contact with this picture. **Plug-in-at-the-mode** (report $p(\theta_{\text{MAP}})$ as if it summarized the posterior) describes a point where the model spends none of its time — the MAP is not a typical parameter. And a **random walk** that proposes small isotropic steps must stay *on the shell*: a step outward or inward off the crust lands in near-zero density and is rejected, so the walker can only shuffle tangentially, and the shell's surface area is exponentially large. To move a useful distance it needs exponentially many tiny steps. That is the wall module 10's Metropolis sampler hits, and we can measure exactly how fast it hits it.

## 12.2 Random-walk Metropolis dies as dimension grows

Take the friendliest possible target — $N(0,I_d)$, no correlation, unit scale — and run the random-walk Metropolis sampler of module 10 on it, tuned optimally at each dimension. Module 10's tuning law says the proposal scale should be $\approx 2.38/\sqrt d$, giving an acceptance rate that settles toward the Roberts–Gelman–Gilks optimum of `0.234` as $d$ grows. Even perfectly tuned, watch the effective sample size per iteration collapse. We can afford this only up to $d=128$; the trend then extrapolates.

```python
# Effective sample size per iteration of optimally-tuned RW-Metropolis on N(0,I_d).
def iat(x):
    """Integrated autocorrelation time; ACF sum truncated at the first negative lag."""
    x = x - x.mean(); n = len(x)
    f = np.fft.rfft(x, n=2 * n)
    acf = np.fft.irfft(f * np.conj(f))[:n].real
    acf /= acf[0]
    tau = 1.0
    for k in range(1, n):
        if acf[k] < 0:
            break
        tau += 2 * acf[k]
    return tau

def rwm_normal(d, n=40000):
    scale = 2.38 / np.sqrt(d)               # module 10's optimal RW scale
    q = np.zeros(d); lp = -0.5 * q @ q
    trace0 = np.empty(n); acc = 0
    for i in range(n):
        prop = q + scale * rng.standard_normal(d)
        lpp = -0.5 * prop @ prop
        if np.log(rng.random()) < lpp - lp:  # symmetric proposal -> RW-MH
            q, lp = prop, lpp; acc += 1
        trace0[i] = q[0]                      # track one coordinate
    return acc / n, 1.0 / iat(trace0)        # acceptance, ESS-per-iteration

ds = np.array([2, 4, 8, 16, 32, 64, 128])
accs, essfrac = [], []
print("RW-MH tuned to scale 2.38/sqrt(d), target N(0,I_d):")
for d in ds:
    a, ef = rwm_normal(int(d))
    accs.append(a); essfrac.append(ef)
    print(f"  d={d:>3}:  acceptance = {a:.3f}   ESS/iter = {ef:.5f}")
essfrac = np.array(essfrac)
slope, intercept = np.polyfit(np.log(ds), np.log(essfrac), 1)
pred1000 = np.exp(intercept) * 1000.0 ** slope
print(f"power law: ESS/iter ~ d^{slope:.2f}")
print(f"extrapolate to d=1000: ESS/iter = {pred1000:.1e}  "
      f"-> ~{1/pred1000:.0f} iterations per independent draw")
print(f"Roberts-Gelman-Gilks optimal acceptance = 0.234")
```

The acceptance rate does drift toward `0.234` as promised (`0.239` at $d=128$), confirming the tuning is right — this is not a badly-configured sampler. Yet the efficiency craters. The ESS-per-iteration follows a clean power law `d^-0.94`, close to the theoretical $1/d$: each doubling of dimension roughly halves the information per step. Extrapolated to $d=1000$ the sampler yields about `2492` iterations *per independent draw*. Want 1000 effective samples in a thousand dimensions? Budget two-and-a-half million random-walk steps, and that is on the *easiest* target in existence — spherical, uncorrelated. Add module 11's posterior correlation and it is worse. Random walks and high dimension do not mix.

```python
# Figure: ESS/iter vs dimension on log-log, with the power-law fit and extrapolation.
fig, ax = plt.subplots()
ax.loglog(ds, essfrac, "o", color="C0", ms=8, label="measured (d ≤ 128)")
dd = np.array([2, 1000])
ax.loglog(dd, np.exp(intercept) * dd ** slope, "k--", lw=1.5,
          label=f"fit  ESS/iter ∝ d^{slope:.2f}")
ax.loglog([1000], [pred1000], "s", color="C3", ms=10, label="extrapolated d=1000")
ax.set_xlabel("dimension d"); ax.set_ylabel("ESS per iteration")
ax.set_title("RW-Metropolis efficiency decays like 1/d")
ax.legend()
save(fig, "rwm-decay")
```

![Log-log plot of ESS-per-iteration against dimension: seven measured points fall on a straight line of slope about −0.94, extended by a dashed fit to the extrapolated d=1000 point near 4e-4.](figures/12-hmc/rwm-decay.png)

## 12.3 Leapfrog HMC from scratch

The fix is to stop proposing blind random steps and instead *follow the geometry*. Hamiltonian Monte Carlo gives the parameter $\theta$ (now called position $q$) a **momentum** $p$ and rolls the pair along the contours of the posterior like a frictionless puck on a hillside. Define a potential energy equal to the negative log posterior and a kinetic energy for the momentum,
$$U(q) = -\log p(q\mid y), \qquad K(p) = \tfrac12 p^\top p, \qquad H(q,p) = U(q) + K(p).$$
Hamilton's equations $\dot q = \partial H/\partial p = p$ and $\dot p = -\partial H/\partial q = -\nabla U(q)$ conserve $H$ and preserve volume, so if we could integrate them exactly, the proposal would be accepted with probability one and would glide a long way along the typical set in a single move. We cannot integrate exactly, but the **leapfrog** integrator — a half momentum kick, a full position drift, a half momentum kick — is symplectic (volume-preserving and reversible), so its small energy error can be corrected by one Metropolis accept/reject at the end. That correction is what keeps the target *exactly* invariant. Here is the entire sampler, on a correlated 2-D Gaussian (the correlation is what broke Gibbs in module 11):

```python
# Leapfrog HMC from scratch on a correlated 2-D Gaussian target.
rho = 0.9
Sigma = np.array([[1.0, rho], [rho, 1.0]])
Prec = np.linalg.inv(Sigma)                 # precision = inverse covariance
def U(q):      return 0.5 * q @ Prec @ q    # potential = -log density (up to const)
def grad_U(q): return Prec @ q              # gradient of the potential
def H(q, p):   return U(q) + 0.5 * p @ p    # total energy

def leapfrog(q, p, eps, L):
    q, p = q.copy(), p.copy()
    p -= 0.5 * eps * grad_U(q)              # half kick
    for _ in range(L - 1):
        q += eps * p                        # full drift
        p -= eps * grad_U(q)                # full kick
    q += eps * p                            # last full drift
    p -= 0.5 * eps * grad_U(q)              # half kick
    return q, p

def hmc(eps, L, n=4000):
    q = np.zeros(2); chain = np.empty((n, 2)); acc = 0
    for i in range(n):
        p = rng.standard_normal(2)          # resample momentum ~ N(0, I)
        q_new, p_new = leapfrog(q, p, eps, L)
        # Metropolis correction on the ENERGY error (exact-target guarantee):
        if np.log(rng.random()) < H(q, p) - H(q_new, p_new):
            q = q_new; acc += 1
        chain[i] = q
    return chain, acc / n

chain, acc = hmc(eps=0.25, L=12)
cov = np.cov(chain.T)
print(f"HMC on correlated Gaussian (rho={rho}):  acceptance = {acc:.3f}")
print(f"  recovered corr = {cov[0,1]/np.sqrt(cov[0,0]*cov[1,1]):.3f}  (true {rho})")
print(f"  recovered marginal sds = {np.sqrt(cov[0,0]):.3f}, {np.sqrt(cov[1,1]):.3f}  (true 1)")
```

With acceptance `0.981` the sampler recovers the correlation `0.910` and unit marginals from a standing start — no per-dimension tuning of the shape, because the momentum refresh plus gradient flow discover it automatically. The reason it works is visible if we draw one leapfrog trajectory over the target's contours: it does not shuffle, it *arcs*.

```python
# Figure: one leapfrog trajectory arcs coherently along the target's contours.
q0 = np.array([-2.0, -2.0]); p0 = np.array([1.4, -0.4])
q, p = q0.copy(), p0.copy(); traj = [q.copy()]
for _ in range(40):
    q, p = leapfrog(q, p, 0.18, 1); traj.append(q.copy())
traj = np.array(traj)
gx = np.linspace(-3.2, 3.2, 200)
G1, G2 = np.meshgrid(gx, gx)
dens = stats.multivariate_normal([0, 0], Sigma).pdf(np.dstack([G1, G2]))
fig, ax = plt.subplots(figsize=(5.2, 5))
ax.contour(G1, G2, dens, levels=6, colors="C7", linewidths=1)
ax.plot(traj[:, 0], traj[:, 1], "-o", color="C1", ms=3, lw=1.5, label="leapfrog path")
ax.plot(*q0, "ks", ms=8, label="start"); ax.plot(*traj[-1], "C3*", ms=15, label="end")
ax.set_xlabel(r"$q_1$"); ax.set_ylabel(r"$q_2$"); ax.set_aspect("equal")
ax.set_title("One HMC proposal: a long coherent glide along the ridge")
ax.legend(fontsize=9)
save(fig, "leapfrog-trajectory")
```

![Elliptical contours of the correlated Gaussian with a leapfrog trajectory that sweeps in a long coherent arc along the ridge from the lower-left corner up to the far corner, U-turns, and glides back to end near where it began — a single proposal that traverses the length of the distribution and returns, covering ground a random walk would need many tiny steps to cross.](figures/12-hmc/leapfrog-trajectory.png)

**The energy error is $O(\varepsilon^2)$.** Leapfrog does not conserve $H$ exactly; its error per trajectory shrinks quadratically in the step size $\varepsilon$. That quadratic — not linear — decay is why HMC can take fairly large steps and still accept: halving $\varepsilon$ quarters the energy error. Verify the exponent by integrating a fixed trajectory-length at shrinking $\varepsilon$ and fitting the slope on log-log axes.

```python
# Energy error of leapfrog scales as eps^2 (fixed trajectory length T = eps*L).
q0 = np.array([1.0, 1.0]); p0 = np.array([0.5, -0.5]); T = 1.6
eps_grid = np.array([0.08, 0.04, 0.02, 0.01, 0.005])
dHs = []
for eps in eps_grid:
    L = int(round(T / eps))
    qL, pL = leapfrog(q0, p0, eps, L)
    dHs.append(abs(H(qL, pL) - H(q0, p0)))
dHs = np.array(dHs)
order = np.polyfit(np.log(eps_grid), np.log(dHs), 1)[0]
print(f"energy-error scaling: |dH| ~ eps^{order:.2f}")

fig, ax = plt.subplots()
ax.loglog(eps_grid, dHs, "o-", color="C0", label="leapfrog |ΔH|")
ax.loglog(eps_grid, dHs[-1] * (eps_grid / eps_grid[-1]) ** 2, "k--",
          label="slope-2 reference")
ax.set_xlabel("step size ε"); ax.set_ylabel("energy error |ΔH|")
ax.set_title("Leapfrog energy error is O(ε²)")
ax.legend()
save(fig, "energy-error")
```

![Log-log plot of energy error against step size: five points on a line of slope exactly 2, matching the dashed reference.](figures/12-hmc/energy-error.png)

The fitted exponent is `2.00`. But the "fairly large steps" have a hard ceiling, and crossing it is the mechanism behind every divergence you will ever debug.

## 12.4 The stability cliff, and what a divergence *is*

Leapfrog is stable only up to a critical step size. For a one-dimensional Gaussian target $N(0,1/\omega^2)$ — potential $U(q)=\tfrac12\omega^2 q^2$, a harmonic oscillator of angular frequency $\omega$ — the leapfrog map is linear, and a two-line eigenvalue analysis gives the **exact stability threshold**
$$\varepsilon_{\text{crit}} = \frac{2}{\omega}.$$
Below it the integrator oscillates forever with bounded energy; above it the map has an eigenvalue outside the unit circle and the trajectory blows up geometrically. For the standard normal $N(0,1)$ we have $\omega=1$, so the knife-edge sits at $\varepsilon=2$. Before running, commit: does exceeding the threshold by half a percent degrade the trajectory *gracefully* — a bit more energy error — or *catastrophically*? (At exactly $\varepsilon_{\text{crit}}$ the map is only marginally stable — a double eigenvalue at $-1$ — and stays bounded here because we start at $p_0=0$, a period-2 orbit; generic starts grow linearly at the threshold, and any $\varepsilon$ strictly below 2 is bounded for every start.)

```python
# Exact stability cliff: N(0,1) has omega=1, so eps_crit = 2/omega = 2.
def leapfrog_1d(eps, steps, q0=1.0, p0=0.0, omega=1.0):
    q, p = q0, p0; peak = abs(q)
    for _ in range(steps):
        p -= 0.5 * eps * omega**2 * q
        q += eps * p
        p -= 0.5 * eps * omega**2 * q
        peak = max(peak, abs(q))
    return peak

for eps in (2.00, 2.01):
    peak = leapfrog_1d(eps, steps=200)
    verdict = "STABLE (bounded)" if peak < 1e3 else "EXPLODES"
    print(f"eps = {eps:.2f}  (eps_crit = 2.00):  max|q| over 200 steps = {peak:.2e}  -> {verdict}")

print("optimal acceptance:  RW-Metropolis = 0.234  vs  HMC = 0.651")
```

At $\varepsilon=$ `2.00` the trajectory stays bounded (max $|q|$ equal to its starting value); at $\varepsilon=$ `2.01`, a mere 0.5% larger, it explodes to $\sim 10^{17}$ within 200 steps. There is no gentle degradation — it is a cliff. **This is precisely what a divergence is.** In a real HMC run the curvature $\omega$ varies from place to place (the posterior is not a single harmonic oscillator), so a step size that is safe in a broad, low-curvature region exceeds $2/\omega$ when the sampler wanders into a narrow, high-curvature one. The leapfrog integrator goes unstable, the energy $H$ shoots to infinity, the Metropolis correction rejects, and NUTS flags the transition as **diverging**. A divergence is not a mysterious warning; it is this exact mechanism firing — the integrator hitting the stability cliff because the local curvature outran the step size. When you see divergences, some region of your posterior has curvature too sharp for your $\varepsilon$, and §12.5 shows the canonical culprit.

One more asymmetry worth banking, printed by the block above. Module 10 found the random walk's optimal acceptance rate is `0.234`; the corresponding optimum for HMC is much higher, `0.651` (Beskos et al. 2013 — the same kind of asymptotic result as 0.234: a $d\to\infty$ diffusion limit on product targets, with $\varepsilon\propto d^{-1/4}$; stated and cited, not re-derived here). Because a leapfrog proposal travels a long coherent distance rather than a timid step, you *want* to accept most of them — a low HMC acceptance means your step size is near the cliff and you are wasting the geometry.

**NUTS in one paragraph.** Two knobs remain: the step size $\varepsilon$ and the number of leapfrog steps $L$. Set $L$ too small and you barely move; too large and the trajectory makes a U-turn and wastes gradients curving back toward where it started. The **No-U-Turn Sampler** removes the knob: it doubles the trajectory outward until it detects the path turning back on itself, then samples a state from the built trajectory. Combined with warmup-phase adaptation of $\varepsilon$ (targeting that 0.651 acceptance) and of a diagonal mass matrix, NUTS is what "the sampler" means in NumPyro, Stan, and PyMC. We now hand the driving to it.

## 12.5 Neal's funnel: divergences you can see

**Setup.** **Neal's funnel** is the minimal instance of varying curvature: a scale parameter $v\sim N(0,3^2)$ and, conditional on it, a vector $x\sim N(0,\,e^{v})$. Where $v$ is large the $x$'s are broad; where $v$ is very negative they are crushed into a needle-thin neck. No data — this is a *prior*, and it is the shape lurking inside every hierarchical model (module 16's eight schools is this funnel wearing data). We will sample it twice: once as written (**centered**), and once after the change of variables $x = e^{v/2}z$ with $z\sim N(0,1)$ (**non-centered** — the identical joint distribution in different coordinates, applied by `LocScaleReparam`).

**Predict.** Both runs use NUTS with warmup-adapted step size, and both target the same distribution. Commit before running: does the coordinate change even matter? If it does, *which* version reaches the bottom of the neck (large negative $v$), and which throws divergences — and roughly how many? The tempting intuition: "NUTS adapts $\varepsilon$ automatically, so two parameterizations of one distribution should sample about the same."

**Run.** In NumPyro, capturing the `diverging` flag exactly as `tools/ppl_idioms.py` prescribes.

```python
# Neal's funnel in NumPyro, centered parameterization (as written above).
import jax
import jax.numpy as jnp
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
from numpyro.infer.reparam import LocScaleReparam
from numpyro.handlers import reparam

D = 9
def funnel(D=9):
    v = numpyro.sample("v", dist.Normal(0.0, 3.0))
    with numpyro.plate("D", D):
        numpyro.sample("x", dist.Normal(0.0, jnp.exp(v / 2)))   # scale = exp(v/2)

def run_funnel(model):
    mcmc = MCMC(NUTS(model), num_warmup=1000, num_samples=1000, num_chains=2,
                chain_method="sequential", progress_bar=False)
    mcmc.run(jax.random.PRNGKey(SEED), D=D, extra_fields=("diverging",))
    div = np.asarray(mcmc.get_extra_fields()["diverging"])
    samples = mcmc.get_samples()
    v = np.asarray(samples["v"])
    x0 = np.asarray(samples["x"][:, 0])          # first coordinate of the vector x
    return v, div, x0

v_c, div_c, x0_c = run_funnel(funnel)
print(f"CENTERED funnel:     divergences = {int(div_c.sum())};  "
      f"v explored in [{v_c.min():.2f}, {v_c.max():.2f}]")
```

```python
# Non-centered reparameterization: x = exp(v/2) * z with z ~ N(0,1), via LocScaleReparam.
funnel_nc = reparam(funnel, config={"x": LocScaleReparam(0)})
v_nc, div_nc, x0_nc = run_funnel(funnel_nc)
print(f"NON-CENTERED funnel: divergences = {int(div_nc.sum())};  "
      f"v explored in [{v_nc.min():.2f}, {v_nc.max():.2f}]")
```

**Reconcile.** The coordinate change matters enormously. The centered run logs `13` divergences and — the deeper symptom — **cannot descend into the neck**: its $v$ bottoms out at `-1.97`, because the neck's curvature grows like $e^{-v/2}$, so no single adapted $\varepsilon$ survives both the wide mouth and the deep neck — §12.4's cliff, hit locally. The non-centered run logs `0` divergences and reaches all the way down to $v=$ `-10.01`. In the new coordinates $z$ and $v$ are *a priori* independent and the geometry is a benign, roughly-spherical bowl with constant curvature — no neck, no cliff, one $\varepsilon$ fits everywhere. The "NUTS adapts" intuition fails because adaptation picks *one global* step size, and the centered funnel has no value that works everywhere. Note what the divergences did for you: they are the sampler reporting its own pathology — "there is a region here I could not survive" — which is why you read them and reparameterize rather than delete them. This is the single most important practical move in hierarchical modeling, and module 16 will reach for it by reflex.

```python
# Figure: the funnel, plotting the log-scale v against one coordinate x_0,
# with centered divergences (red) stranded at the top of the neck.
fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), sharey=True)
panels = [(v_c, div_c, x0_c, "centered"), (v_nc, div_nc, x0_nc, "non-centered")]
for ax, (v, div, x0, ttl) in zip(axes, panels):
    ok = div == 0
    ax.plot(x0[ok], v[ok], ".", color="C0", ms=2, alpha=0.4, label="accepted")
    if div.sum() > 0:
        ax.plot(x0[div == 1], v[div == 1], "x", color="C3", ms=7, label="divergence")
    ax.set_xlabel(r"coordinate $x_0$"); ax.set_title(f"{ttl}: {int(div.sum())} divergences")
    ax.set_ylim(-11, 11); ax.legend(fontsize=9, loc="upper left")
axes[0].set_ylabel("log-scale  v")
fig.suptitle("Neal's funnel: centered chain stalls above the neck; non-centered reaches it")
fig.tight_layout(rect=(0, 0, 1, 0.94))
save(fig, "funnel")
```

![Two panels of draws plotted against the log-scale v; the centered panel's points stop around v=−2 with red divergence crosses clustered at its lower edge, while the non-centered panel's points extend smoothly down to v=−10 with no divergences.](figures/12-hmc/funnel.png)

## 12.6 Which tool, and why NumPyro here

You will meet four names; keep their roles straight.

- **NumPyro is the course PPL.** Every runnable sampler in these modules is NumPyro because it compiles the model to JAX and needs no C toolchain; PyTensor's C backend is broken in this environment, which is the plain reason PyMC cannot sample here at usable speed. NumPyro's `MCMC(NUTS(...))` is what actually produced the funnel draws above.
- **PyMC is the mainstream API** most Python practitioners write, and the model reads almost identically. Shown here for orientation only — it does not run in this environment:

```python no-run
# PyMC — the mainstream API (illustration only; does not run in this environment).
import pymc as pm
with pm.Model() as funnel:
    v = pm.Normal("v", 0.0, 3.0)
    x = pm.Normal("x", 0.0, pm.math.exp(v / 2), shape=9)   # centered
    idata = pm.sample(1000, tune=1000, chains=2, target_accept=0.9)
# non-centering in PyMC is the same change of variables, written by hand:
#   z = pm.Normal("z", 0, 1, shape=9);  x = pm.Deterministic("x", pm.math.exp(v/2) * z)
```

- **Stan** is the older, compiled modeling language the booklet's BDA3 insert uses; its `model` block declares the same log density and its NUTS is the reference implementation the others descend from. We read it there, but write none in this course.
- **ArviZ is the shared diagnostics layer.** `az.from_numpyro(mcmc)` converts any of these into one common object carrying the `diverging` flags, $\hat R$, and ESS — the vocabulary of module 10, now reused for every sampler.

## 12.7 SGLD: when the gradient is all you can afford

HMC needs the *exact* gradient of the log posterior over the whole dataset at every leapfrog step. For a dataset of millions that is too expensive, and the deep-learning-scale answer is to drop the Metropolis correction and inject the right amount of noise instead. The **overdamped Langevin diffusion**
$$d\theta = \tfrac12\,\nabla\log p(\theta)\,dt + dW$$
(Lawler's stochastic-calculus bridge: a gradient drift plus Brownian motion $dW$) has the target as its exact stationary law. Discretize it with Euler–Maruyama at step $\varepsilon$ — replace $dt$ by $\varepsilon$ and $dW$ by $\sqrt\varepsilon\,\xi$, $\xi\sim N(0,I)$. With the exact gradient, as coded below, this is the **unadjusted Langevin algorithm (ULA)**; swap in a mini-batch gradient estimate and it becomes **Stochastic Gradient Langevin Dynamics (SGLD)** — same ten lines, cheaper gradient. The price of dropping the accept/reject step is a bias that scales with $\varepsilon$.

```python
# ULA on a N(0,1) target: gradient drift + calibrated noise, no Metropolis step.
# (SGLD = this recursion with a mini-batch gradient in place of grad_logp.)
def sgld(eps, n=300000):
    grad_logp = lambda th: -th               # d/dtheta log N(theta;0,1) = -theta
    th = 0.0; draws = np.empty(n)
    for i in range(n):
        th = th + 0.5 * eps * grad_logp(th) + np.sqrt(eps) * rng.standard_normal()
        draws[i] = th
    return draws

print("SGLD stationary variance vs step size (target variance = 1):")
for eps in (0.1, 0.3, 0.5):
    v = sgld(eps).var()
    print(f"  eps={eps:.1f}:  empirical var = {v:.4f}   Euler-Maruyama theory 1/(1-eps/4) = {1/(1-eps/4):.4f}")
```

The discretization inflates the stationary variance to $1/(1-\varepsilon/4)$ instead of the true `1`, and the formula is a two-line derivation: for the $N(0,1)$ target the recursion is the AR(1) process $\theta' = (1-\varepsilon/2)\theta + \sqrt\varepsilon\,\xi$, so its stationary variance $v$ solves
$$v = (1-\varepsilon/2)^2 v + \varepsilon \quad\Longrightarrow\quad v = \frac{\varepsilon}{\varepsilon - \varepsilon^2/4} = \frac{1}{1-\varepsilon/4}.$$
The simulation agrees: at $\varepsilon=0.1$ the chain's variance is `1.0174` against the predicted `1.0256` (within Monte-Carlo error), and at $\varepsilon=0.5$ it is `1.1376` against `1.1429` — the Euler–Maruyama bias, growing with the step, exactly as derived. Shrinking $\varepsilon$ removes the bias but also slows mixing to a crawl, the same tension as always. Swap the exact gradient for a mini-batch estimate and you have the algorithm that connects SGD-with-noise to Bayesian sampling; module 25 cashes this out as "why the noise in stochastic gradient descent is doing approximate posterior inference."

## Bridge — the booklet's HMC/Stan insert, re-read

The booklet's BDA3 insert introduces HMC operationally: momentum, leapfrog, Stan. Read through the four lines, it is line 2's engine. The typical-set argument (§12.1) is *why* the insert insists you never trust the mode; the energy-error and stability analysis (§12.3–12.4) is *why* it warns about divergences and step-size adaptation; the funnel (§12.5) is *why* it teaches non-centering. And the through-line to module 09: HMC and SGLD are both ways of manufacturing a Markov chain whose stationary law is the posterior, judged by the same ESS and $\hat R$ diagnostics — HMC pays for exactness with full-data gradients and a Metropolis correction, SGLD trades a controllable bias for scalability. Same goal, different points on the accuracy-versus-cost frontier.

## Pitfalls

- **Initializing or summarizing at the mode.** In high dimension the MAP is in the empty center of the donut, not a typical draw. Report posterior means, quantiles, and intervals from typical-set samples; never a single "most probable" parameter as if it stood in for the posterior.
- **Ignoring divergences, or averaging over them.** A divergence means the integrator hit the stability cliff in some region — usually a funnel neck the chain therefore *failed to explore*. The posterior you keep is biased toward the wide part. Reparameterize (non-center) or lower the step size; do not just delete the flagged draws and move on.
- **Non-centering everything reflexively.** Non-centering fixes funnels caused by *weak* data (the neck is prior-dominated). When a group is *data-rich*, the centered parameterization is actually the better-conditioned one. Match the parameterization to where the information is; module 16 returns to this.
- **Reading a low HMC acceptance as "fine, it still moves."** HMC wants acceptance near `0.651`; a rate far below it means $\varepsilon$ is near the cliff and divergences are imminent. Low acceptance in HMC is an alarm, not the healthy 0.234 of a random walk.
- **Trusting SGLD's uncertainty at a usable step size.** The stationary distribution is the target only as $\varepsilon\to0$; at any practical step it is over-dispersed (and mini-batch gradients add more noise still). Fine for point predictions, not for calibrated tail probabilities.

## Exercises

**Exercise 12.1 — Curvature sets the cliff.**
*Setup:* The stability threshold for a Gaussian target $N(0,\sigma^2)$ is $\varepsilon_{\text{crit}}=2/\omega$ where $\omega$ is the potential's frequency, and $\omega^2 = 1/\sigma^2$. For the standard normal ($\sigma=1$, $\omega=1$) the cliff was at $\varepsilon=2$.
*Predict:* A narrower target, $N(0,0.25)$ so $\sigma=0.5$: does its stability cliff sit at a *larger* or *smaller* step size than 2, and at what value?
*Reason:* The intuition "smaller variance is just a rescaling, the sampler shouldn't care" — testing whether curvature, not spread, is what the integrator feels.
*Run:*
```python
sigma = 0.5; omega = 1 / sigma           # frequency of N(0, sigma^2)
eps_crit = 2 / omega
for eps in (eps_crit - 0.01, eps_crit + 0.01):
    peak = leapfrog_1d(eps, 200, omega=omega)
    print(f"sigma={sigma}, eps_crit={eps_crit:.2f}: eps={eps:.2f} -> max|q|={peak:.2e}")
```
<details><summary>Reconcile</summary>

The cliff moves to $\varepsilon_{\text{crit}}=2/\omega=2/2=$ `1.00`, half of the standard normal's. A target four times narrower has twice the curvature ($\omega$ doubles), so it tolerates only half the step size. This is the whole reason a *single* step size cannot serve a posterior whose curvature varies across regions — the funnel of §12.5 is this exercise with $\omega$ ranging continuously from tiny (wide mouth) to enormous (neck), so no global $\varepsilon$ is simultaneously below every local $2/\omega$. Curvature, not spread per se, is what leapfrog feels; and non-centering works precisely by flattening that curvature to a constant.
</details>

**Exercise 12.2 — How empty is the center?**  *(surprising)*
*Setup:* A standard Gaussian in $d=500$ dimensions. You reason that the mode is the most probable point and its neighborhood should therefore hold a healthy chunk of the mass.
*Predict:* What fraction of the mass of $N(0,I_{500})$ lies within Euclidean distance 5 of the mode? (The typical radius is $\sqrt{500}\approx22.4$, for reference.) Guess before running: 1%? 10%? Something larger?
*Reason:* "High density near the mode implies substantial mass near the mode" — the plug-in-at-the-MAP reflex, one last time.
*Run:*
```python
X = rng.standard_normal(size=(100000, 500))
r = np.sqrt((X ** 2).sum(1))
print(f"typical radius sqrt(500) = {np.sqrt(500):.1f}")
print(f"fraction within distance 5 of the mode = {(r < 5).mean():.6f}")
```
<details><summary>Reconcile</summary>

The fraction is `0.000000` — not one draw in a hundred thousand lands within distance 5 of the mode, even though 5 is a generous ball and the mode is the single densest point in the space. The mass sits in a shell at radius `22.4`, and a ball of radius 5 around the origin is a vanishing speck of the volume out there. This is why "the network's most likely weights" or "the posterior mode" is not a summary of a high-dimensional posterior — it describes a location the model essentially never visits. Uncertainty in high dimension is not a small correction around a point estimate; the point estimate is in the wrong place entirely.
</details>

**Exercise 12.3 — SGD as an approximate sampler.**  *(ML/DL bridge)*
*Setup:* SGLD is gradient descent plus calibrated noise, and its stationary spread depends on the step size. Consider a "colder" chain that scales the injected noise down by a factor $\sqrt T$ with $T=0.25$ — i.e. use noise $\sqrt{\varepsilon T}\,\xi$ instead of $\sqrt\varepsilon\,\xi$, at $\varepsilon=0.1$.
*Predict:* Does the reduced noise make the chain's stationary variance larger or smaller than the target's 1, and roughly by how much? Does it still sample $N(0,1)$?
*Reason:* "Less noise means a tighter, more accurate posterior" — the tempting reading of noise as pure nuisance, rather than as the thing that *creates* the correct spread.
*Run:*
```python
eps, T = 0.1, 0.25
th = 0.0; draws = np.empty(200000)
for i in range(200000):
    th = th - 0.5 * eps * th + np.sqrt(eps * T) * rng.standard_normal()
    draws[i] = th
print(f"tempered SGLD (T={T}): empirical var = {draws.var():.4f}  (target 1)")
```
<details><summary>Reconcile</summary>

The variance collapses to `0.2567`, roughly $T$ times the target — the chain now samples a *tempered* posterior $p(\theta)^{1/T}$, sharply concentrated, not $N(0,1)$ at all. Turning the noise down did not make inference "more accurate"; it changed which distribution you sample, trading the true posterior for an overconfident caricature. This is the exact lens module 25 puts on stochastic gradient descent: the ratio of learning rate to mini-batch noise sets an effective temperature, and plain SGD with too little noise behaves like a sampler from a too-cold posterior — one reason a trained network's single weight vector is overconfident about itself. Noise in a sampler is not a defect to minimize; calibrated to the gradient, it is what makes the samples *be* the posterior.
</details>

## Takeaways

- **The typical set (S1):** the mass of a high-dimensional distribution lives in a thin shell at radius $\approx\sqrt d$ from the mode, not at the mode. The mode has the highest density and essentially zero mass — plug-in-at-the-MAP and random walks both fail there. At $d=1000$ the mean distance from the mode is `31.61` and no draw lands within half that of the mode.
- **Random walks die like $1/d$:** even optimally tuned (acceptance `0.234`, scale $2.38/\sqrt d$), RW-Metropolis ESS-per-iteration decays as `d^-0.94`, needing $\sim$`2492` iterations per independent draw at $d=1000$ on the easiest possible target.
- **HMC follows the geometry:** give the parameter momentum and roll along the contours with leapfrog (half-kick, drift, half-kick); one Metropolis correction on the energy keeps the target exact. Energy error is `2.00` (order $\varepsilon^2$), so steps can be long and coherent.
- **Divergences are the stability cliff firing:** leapfrog is stable only for $\varepsilon < 2/\omega$; cross it (as at $\varepsilon=$ `2.01` for $\omega=1$) and the trajectory explodes. In practice a fixed $\varepsilon$ exceeds $2/\omega$ wherever local curvature spikes — that is a divergence, and it means an unexplored region.
- **Funnels are the canonical trap:** the centered Neal funnel diverges at the neck (`13` divergences, $v$ stuck above `-1.97`); non-centering via `LocScaleReparam` flattens the curvature to a constant and fixes it (`0` divergences, $v$ down to `-10.01`). This is the reflex for hierarchical models (module 16).
- **NUTS** auto-tunes trajectory length (stop at the U-turn) and step size (target acceptance `0.651`, higher than the random walk's 0.234); it is what "the sampler" means in NumPyro/Stan/PyMC, with ArviZ as the shared diagnostics layer.
- **SGLD** discretizes the overdamped Langevin SDE — gradient drift plus Brownian noise — to sample without a Metropolis step, at the price of an $O(\varepsilon)$ bias (variance inflated to $1/(1-\varepsilon/4)$); it is the bridge from HMC to stochastic-gradient deep learning (module 25).

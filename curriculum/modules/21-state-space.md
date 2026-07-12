# 21. State Space: Filtering Is Bayes on a Conveyor Belt

> **Spine.** The Kalman filter is module 05's Normal-Normal update on repeat — *predict* marginalizes the transition, *update* conditions on the new datum, and the Kalman gain is the master shrinkage weight; when linear-Gaussian breaks, carry the posterior as weighted particles.
> **Which line?** Lines 2 and 3 on a moving target: a posterior over a *hidden state* that you alternately push forward in time (marginalize, line 3) and sharpen against data (condition, line 2), forever.
> **Promise.** After this module you can derive the Kalman filter from scratch as two conjugate moves, fit a Bayesian AR(p) as lag regression, filter a noisy diffusion, and run a bootstrap particle filter — and you will recognize when its weights are quietly dying.
> **Prereqs.** Modules 05 (Normal-Normal update, `gaussian_condition`, the master shrinkage formula), 09 (`ess_kong` and the ESS-fraction-collapse diagnostic), 14 (Bayesian regression, `nig_regression`). **Runtime.** ~10 s.
> **Sources.** Lawler (OU discretization) by concept; Särkkä *Bayesian Filtering and Smoothing* by concept; booklet ch. 8 framing.

## 21.1 The conveyor belt: predict = marginalize, update = condition

A hidden thing moves; you get noisy glimpses. A satellite's position drifts and you ping it; an asset's log-volatility wanders and you see its returns; a latent signal diffuses and your sensor is dirty. In every case the object is a **state** $x_t$ evolving in time, and you observe $y_t$, a corrupted function of it. The **filtering** question is line 2 with a clock attached: given everything seen so far, what is $p(x_t \mid y_{1:t})$?

The simplest instance — the *local level* model, a random walk watched through noise:
$$x_t = x_{t-1} + w_t,\quad w_t\sim N(0,q);\qquad y_t = x_t + v_t,\quad v_t\sim N(0,r).$$
Suppose at time $t-1$ you already hold the posterior $x_{t-1}\mid y_{1:t-1}\sim N(m_{t-1}, P_{t-1})$. Two moves carry you one tick forward.

**Predict (line 3, marginalize the transition).** You don't know $x_t$, but you know $x_t = x_{t-1}+w_t$ and the law of $x_{t-1}$. Marginalizing $x_{t-1}$ out — a sum of independent Gaussians — gives the *one-step-ahead prior*
$$x_t\mid y_{1:t-1}\sim N(m^-_t, P^-_t),\qquad m^-_t = m_{t-1},\quad P^-_t = P_{t-1}+q.$$
Uncertainty grew by the process noise $q$: time passing without data makes you less sure.

**Update (line 2, condition on $y_t$).** Now $y_t$ arrives. You have a Gaussian prior $N(m^-_t,P^-_t)$ on $x_t$ and a Gaussian likelihood $y_t\mid x_t\sim N(x_t, r)$. **This is exactly the Normal-Normal update of module 05 — one observation, known variance $r$.** Precisions add:
$$\frac{1}{P_t} = \frac{1}{P^-_t} + \frac{1}{r},\qquad m_t = \frac{m^-_t/P^-_t + y_t/r}{1/P^-_t + 1/r}.$$
Engineers write the same thing with a **gain** $K_t = P^-_t/(P^-_t+r)$:
$$m_t = m^-_t + K_t\,(y_t - m^-_t),\qquad P_t = (1-K_t)\,P^-_t.$$

Before we run anything, commit. Here is a predicted state $N(m^-=2, P^-=3)$, a fresh observation $y=5$, noise $r=1$.

**Predict.** Two commitments, the second more important than the first. First: what is the updated posterior mean? Second, the meta-question — *can you even compute it with only module 05's `normal_known_var_update`, a tool that has never heard of filtering?* Commit to yes or no before touching the code. *Reason:* the intuition on trial is that "the Kalman filter" is a specialized engineering algorithm you have not yet learned — that between you and it stands new machinery. If you answered "no, I need the filtering chapter first," that is the intuition about to be caught. What you should expect to feel when the numbers land is not surprise but *recognition* — the anticlimax is the lesson.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from scipy import stats

SLUG = "21-state-space"
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

```python
# 21.1 -- the "nothing new" reveal: the Kalman update IS the Normal-Normal update
# module 05's Normal-Normal update, verbatim
def normal_known_var_update(m0, tau2, sigma2, data):
    """N(m0, tau2) prior on the mean, known obs variance sigma2 -> (mean, var)."""
    n = len(data)
    prec_post = 1.0/tau2 + n/sigma2
    m_post = (m0/tau2 + data.sum()/sigma2) / prec_post
    return m_post, 1.0/prec_post

# The Kalman UPDATE, spelled in gain form
m_pred, P_pred, r, y = 2.0, 3.0, 1.0, 5.0
K = P_pred / (P_pred + r)
m_kf, P_kf = m_pred + K*(y - m_pred), (1 - K)*P_pred

# The SAME thing via module 05
m_05, v_05 = normal_known_var_update(m_pred, P_pred, r, np.array([y]))
print(f"Kalman gain form : K = {K:.2f}   post mean = {m_kf:.2f}   post var = {P_kf:.2f}")
print(f"module 05 route  : post mean = {m_05:.2f}   post var = {v_05:.2f}")
print(f"max|difference|  = {max(abs(m_kf-m_05), abs(P_kf-v_05)):.1e}")
```

**Reveal.** The gain is $K=$ `0.75`, the posterior mean is `4.25`, and the two routes agree to `8.9e-16` — machine zero. There is nothing to learn because there is nothing new. The "Kalman update" is the Normal-Normal update; the gain $K = P^-/(P^-+r)$ is the **data's precision over the total precision** — module 05's data weight, wearing a control-theory costume. Read it against the shrinkage formula the spine index records verbatim: *posterior mean = (κ/(κ+n))·prior + (n/(κ+n))·MLE — the master shrinkage formula*. Here the "prior" is the prediction $m^-$, the "MLE" is the raw observation $y$, and $K$ is the $n/(κ+n)$ weight: $m_t = (1-K)m^- + K\,y$. When the sensor is sharp ($r\to0$) the gain $\to1$ and you believe the data; when the state is well-pinned ($P^-\to0$) the gain $\to0$ and you keep your prediction. That the gain here is exactly `0.75` — the prediction is worth one-third of the observation's precision — is the same `0.75` that has haunted the course since module 05's two-conversion predictive. The most famous algorithm in engineering is a conveyor belt carrying module 05 past a window, applying it once per tick.

Run it as a loop and the belt turns. At each step: predict (add $q$), update (Normal-Normal). Cross-check *every* update against `normal_known_var_update` — the equality must hold at all 60 steps, not just the illustrative one.

```python
# 21.1 -- the local-level Kalman filter is normal_known_var_update on a loop
rng_ll = np.random.default_rng(0)
q1, r1, n = 0.5, 2.0, 60
x_true = np.zeros(n)
for t in range(1, n):
    x_true[t] = x_true[t-1] + rng_ll.normal(0, np.sqrt(q1))     # random-walk state
y_obs = x_true + rng_ll.normal(0, np.sqrt(r1), n)              # noisy observations

m, P = 0.0, 10.0                                              # diffuse prior on x_0
ms, Ps, gains, max_diff = np.zeros(n), np.zeros(n), np.zeros(n), 0.0
for t in range(n):
    m_pred, P_pred = m, P + q1                                # PREDICT (marginalize)
    Kt = P_pred / (P_pred + r1)                               # UPDATE (condition):
    m, P = m_pred + Kt*(y_obs[t]-m_pred), (1-Kt)*P_pred       #   the Kalman gain form
    m_ref, P_ref = normal_known_var_update(m_pred, P_pred, r1, y_obs[t:t+1])
    max_diff = max(max_diff, abs(m-m_ref), abs(P-P_ref))      #   ... == module 05
    ms[t], Ps[t], gains[t] = m, P, Kt

print(f"KF-update vs normal_known_var_update, max|diff| over {n} steps = {max_diff:.1e}")
print(f"gain converges to steady state K_inf = {gains[-1]:.4f}, P_inf = {Ps[-1]:.4f}")
print(f"RMSE: filtered {np.sqrt(np.mean((ms-x_true)**2)):.3f}  vs  raw obs "
      f"{np.sqrt(np.mean((y_obs-x_true)**2)):.3f}")

fig, ax = plt.subplots()
ax.plot(x_true, color="k", ls="--", lw=1.5, label="true state $x_t$")
ax.scatter(range(n), y_obs, s=14, color="C7", alpha=0.6, label="noisy obs $y_t$")
ax.plot(ms, color="C1", lw=2, label="filter mean $m_t$")
ax.fill_between(range(n), ms-2*np.sqrt(Ps), ms+2*np.sqrt(Ps),
                color="C1", alpha=0.2, label=r"$m_t\pm2\sqrt{P_t}$")
ax.set_xlabel("time $t$"); ax.set_ylabel("state")
ax.set_title("Local-level Kalman filter: Normal-Normal update, once per tick")
ax.legend(ncol=2, fontsize=9)
save(fig, "kalman-1d")
```

![True random-walk state (black dashed), scattered noisy observations, and the filter's mean track with a 2-sigma band that hugs the truth far more tightly than the raw observations.](figures/21-state-space/kalman-1d.png)

The update matches module 05 to `8.9e-16` at every one of the 60 steps. The gain does *not* stay at its start value — it converges to a steady state `0.3904`, and the posterior variance to `0.7808`. This fixed point is the solution of the algebraic Riccati equation $P = (1-\frac{P+q}{P+q+r})(P+q)$; a filter run long enough on a time-invariant model becomes the constant-gain **Wiener filter**, an exponential smoother whose one tunable knob is the signal-to-noise ratio $q/r$. Filtering cut the tracking error from `1.421` (believe each raw ping) to `1.008` (believe the belt): borrowing strength across time, which is module 16's partial pooling with the "groups" being *time steps* and $\tau^2$ replaced by the process noise $q$.

## 21.2 Tracking in two dimensions: the same two moves, vectorized

Nothing above used scalars in an essential way. Promote $x_t$ to a vector, the transition to a matrix $F$, the observation map to a matrix $H$, and the noise variances to the **process-noise covariance** $Q$ and **observation-noise covariance** $R$ — the matrix analogues of §21.1's $q$ and $r$ — and the two moves become the matrix Kalman filter:
$$\text{predict:}\quad m^-=Fm,\ \ P^-=FPF^\top+Q;\qquad \text{update:}\quad K=P^-H^\top S^{-1},\ \ m=m^-+K(y-Hm^-),\ \ P=(I-KH)P^-,$$
with innovation covariance $S = HP^-H^\top + R$. Track a body in the plane with a **constant-velocity** model: state $x=(p_x,p_y,v_x,v_y)$, observe position only. The classic radar problem.

**Predict.** One commitment before running: the filter will report a $2\sigma$ uncertainty ellipse around each estimated position. Will that ellipse be elongated *along* the direction of motion or *across* it? *Reason:* the naive picture says the sensor noise $R$ is isotropic, so the position uncertainty should be a circle — direction of travel shouldn't matter.

The update is *still* just conditioning — and now it is literally module 05's `gaussian_condition`. The predicted state and its would-be observation form a joint Gaussian
$$\begin{bmatrix}x_t\\ y_t\end{bmatrix}\ \Big|\ y_{1:t-1}\ \sim\ N\!\left(\begin{bmatrix}m^-\\ Hm^-\end{bmatrix},\ \begin{bmatrix}P^- & P^-H^\top\\ HP^- & S\end{bmatrix}\right),$$
and conditioning the state block on the observed $y_t$ with the MVN block formulas *is* the Kalman update. We verify the two are byte-identical.

```python
# 21.2 -- 2-D constant-velocity tracking; the update == gaussian_condition (module 05)
def gaussian_condition(mu, Sigma, idx1, idx2, x2):        # verbatim from module 05
    S11 = Sigma[np.ix_(idx1, idx1)]; S12 = Sigma[np.ix_(idx1, idx2)]
    S22 = Sigma[np.ix_(idx2, idx2)]; S21 = Sigma[np.ix_(idx2, idx1)]
    cond_mean = mu[idx1] + S12 @ np.linalg.solve(S22, x2 - mu[idx2])
    cond_cov  = S11 - S12 @ np.linalg.solve(S22, S21)
    return cond_mean, cond_cov

rng_2d = np.random.default_rng(1)
dt = 1.0
F = np.array([[1,0,dt,0],[0,1,0,dt],[0,0,1,0],[0,0,0,1]], float)
H = np.array([[1,0,0,0],[0,1,0,0]], float)
qa, rr, N = 0.05, 4.0, 40
Qax = np.array([[dt**3/3, dt**2/2],[dt**2/2, dt]])        # continuous-accel process noise
Q = np.zeros((4,4))
for ip, iv in [(0,2),(1,3)]:                              # couple each position with its velocity
    Q[np.ix_([ip,iv],[ip,iv])] = qa*Qax
R = rr*np.eye(2)

x = np.array([0.,0.,1.,0.5]); states = np.zeros((N,4)); obs = np.zeros((N,2))
for t in range(N):
    x = F@x + rng_2d.multivariate_normal(np.zeros(4), Q)
    states[t] = x
    obs[t] = H@x + rng_2d.multivariate_normal(np.zeros(2), R)

m, P = np.zeros(4), np.eye(4)*10.0
filt, covs, gc_diff = np.zeros((N,4)), np.zeros((N,4,4)), 0.0
for t in range(N):
    m_pred, P_pred = F@m, F@P@F.T + Q
    S = H@P_pred@H.T + R
    Kt = P_pred@H.T@np.linalg.inv(S)
    m, P = m_pred + Kt@(obs[t]-H@m_pred), (np.eye(4)-Kt@H)@P_pred
    mu_j = np.concatenate([m_pred, H@m_pred])             # the joint (state, obs) ...
    Sig_j = np.block([[P_pred, P_pred@H.T],[H@P_pred, S]])
    cm, cc = gaussian_condition(mu_j, Sig_j, [0,1,2,3], [4,5], obs[t])  # ... conditioned
    gc_diff = max(gc_diff, np.max(np.abs(cm-m)), np.max(np.abs(cc-P)))
    filt[t], covs[t] = m, P

print(f"Kalman update vs gaussian_condition, max|diff| = {gc_diff:.1e}")
print(f"position RMSE: filtered {np.sqrt(np.mean(np.sum((filt[:,:2]-states[:,:2])**2,1))):.3f}"
      f"  vs raw obs {np.sqrt(np.mean(np.sum((obs-states[:,:2])**2,1))):.3f}")

def ellipse(ax, mu, C, nsig=2, **kw):
    vals, vecs = np.linalg.eigh(C)
    ang = np.degrees(np.arctan2(vecs[1,-1], vecs[0,-1]))
    w, h = 2*nsig*np.sqrt(vals[::-1])
    ax.add_patch(Ellipse(mu, w, h, angle=ang, fill=False, **kw))

fig, ax = plt.subplots(figsize=(6.5, 5.2))
ax.plot(states[:,0], states[:,1], "k--", lw=1.4, label="true path")
ax.scatter(obs[:,0], obs[:,1], s=18, color="C7", alpha=0.6, label="noisy position obs")
ax.plot(filt[:,0], filt[:,1], color="C1", lw=2, label="filter mean")
for t in range(3, N, 7):
    ellipse(ax, filt[t,:2], covs[t,:2,:2], nsig=2, color="C1", alpha=0.7)
ax.set_xlabel("$p_x$"); ax.set_ylabel("$p_y$")
ax.set_title(r"2-D tracking: filter track with $2\sigma$ position-uncertainty ellipses")
ax.legend(fontsize=9); ax.set_aspect("equal", "datalim")
save(fig, "tracking-2d")
```

![A curved true trajectory in the plane, a cloud of noisy position observations around it, and a smooth filter track threading through, annotated with tilted 2-sigma covariance ellipses that shrink and orient along the direction of travel.](figures/21-state-space/tracking-2d.png)

The Kalman update reproduces `gaussian_condition` to `1.8e-15`: the filter is the MVN block formula from module 05, iterated. Tracking halves the position error, from `2.616` (raw pings) to `1.424` (filtered). **Reconcile the ellipse commitment:** the circles the isotropic-$R$ intuition predicted are not what the figure shows. The ellipses are the position marginal $P_t[{:}2,{:}2]$, and they *tilt along the direction of motion* — the sensor noise is isotropic, but the *state* uncertainty is not, because position and velocity are correlated through $F$: an error in the (never-observed) velocity smears the position estimate forward along the track, so a moving target is more uncertain *ahead* than *across*. They also shrink after each update as conditioning removes variance — the geometric face of $P = (I-KH)P^-$. The velocity you never observe is inferred *entirely* through its coupling to position in $F$ and $Q$: the off-diagonal blocks do the work, exactly as `gaussian_condition` infers an unobserved block from an observed one.

## 21.3 AR(p): conjugate regression on lags

A hidden state you never see directly is one way to model a time series; another is to let the *observed* series depend on its own past. The autoregression $\mathrm{AR}(2)$,
$$y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \varepsilon_t,\qquad \varepsilon_t\sim N(0,\sigma^2),$$
is — read it directly — a **linear regression of $y_t$ on its two lags**. This observed-lag view and the hidden-state view are the *same model class* seen from two angles: stack the last $p$ values into a state vector and an AR($p$) is a linear-Gaussian state space (we close that loop at the end of the section), so this beat sits on the same conveyor belt — it just happens that the state is fully observed, which makes exact conjugate regression available. There is nothing new to build: it is module 14's machinery with the design matrix's columns being shifted copies of the series. Stack the rows $(y_{t-1}, y_{t-2})$ into $X$, the targets $y_t$ into the response, and hand it to `nig_regression` (unknown $\sigma^2$, so the coefficient posterior is a multivariate Student-$t$, the noise an inverse-Gamma).

```python
# 21.3 -- Bayesian AR(2) = conjugate lag regression (module 14's nig_regression, verbatim)
def nig_regression(X, y, m0, V0, a0, b0):                # verbatim from module 14
    V0inv = np.linalg.inv(V0)
    Vn = np.linalg.inv(V0inv + X.T @ X)
    mn = Vn @ (V0inv @ m0 + X.T @ y)
    an = a0 + len(y)/2
    bn = b0 + 0.5*(m0 @ V0inv @ m0 + y @ y - mn @ np.linalg.inv(Vn) @ mn)
    return mn, Vn, an, bn

rng_ar = np.random.default_rng(2)
phi_true, sig_true, nT = np.array([0.5, 0.3]), 1.0, 300
s = np.zeros(nT+2)
for t in range(2, nT+2):
    s[t] = phi_true[0]*s[t-1] + phi_true[1]*s[t-2] + rng_ar.normal(0, sig_true)
series = s[2:]
resp = series[2:]                                        # y_t
X = np.column_stack([series[1:-1], series[:-2]])         # [y_{t-1}, y_{t-2}]
mn, Vn, an, bn = nig_regression(X, resp, np.zeros(2), 10*np.eye(2), 1.0, 1.0)
print(f"posterior mean phi = ({mn[0]:.4f}, {mn[1]:.4f})   true (0.5, 0.3)")
print(f"predictive df = {2*an:.0f},  E[sigma^2|y] = {bn/(an-1):.4f}")

# stationarity of the POSTERIOR DRAWS: AR(2) is stationary iff (phi1+phi2<1, phi2-phi1<1, |phi2|<1)
rng_draw = np.random.default_rng(22)
Sd = 20000
sig2 = 1.0/rng_draw.gamma(an, 1/bn, Sd)                  # sigma^2 ~ IG(a_n, b_n)
phi = mn + np.sqrt(sig2)[:,None]*(rng_draw.standard_normal((Sd,2)) @ np.linalg.cholesky(Vn).T)
p1, p2 = phi[:,0], phi[:,1]
stationary = (p1+p2 < 1) & (p2-p1 < 1) & (np.abs(p2) < 1)
print(f"fraction of posterior draws that are stationary = {stationary.mean():.3f}")

fig, ax = plt.subplots(figsize=(5.6, 5.0))
ax.scatter(p1[:3000], p2[:3000], s=5, alpha=0.25, color="C1", label="posterior draws")
g = np.linspace(-1.2, 2.2, 200)
ax.plot(g, 1-g, "k-", lw=1); ax.plot(g, g-1, "k-", lw=1); ax.axhline(-1, color="k", lw=1)
ax.axhline(1, color="k", ls=":", lw=1)
ax.scatter(*phi_true, color="k", marker="*", s=180, zorder=5, label="truth")
ax.set_xlim(-0.2, 1.0); ax.set_ylim(-0.4, 0.8)
ax.set_xlabel(r"$\phi_1$"); ax.set_ylabel(r"$\phi_2$")
ax.set_title("AR(2) posterior sits inside the stationarity triangle")
ax.legend(fontsize=9)
save(fig, "ar2-posterior")
```

![A tight cloud of posterior draws for the two AR coefficients centered near (0.5, 0.3), sitting well inside the triangular stationarity region bounded by the two diagonal lines and the horizontal floor.](figures/21-state-space/ar2-posterior.png)

The posterior mean recovers the coefficients — `0.4471` and `0.2726` — with predictive degrees of freedom $2a_n =$ `300` and $\mathbb{E}[\sigma^2\mid y]=$ `1.0388`. Two things worth naming. First, **the stationarity check** is not a property of a point estimate but of the *whole posterior*: `1.000` of the draws fall inside the stationarity triangle $\{\phi_1+\phi_2<1,\ \phi_2-\phi_1<1,\ |\phi_2|<1\}$, so the model is confident the process does not explode. When that fraction is *not* near one — short series, near-unit-root dynamics — you have a posterior placing real mass on explosive parameters, and reporting the mean $\hat\phi$ alone would hide it. Second, the loop promised at the top: writing the state as $(y_t, y_{t-1})$ with transition $F=\left(\begin{smallmatrix}\phi_1&\phi_2\\1&0\end{smallmatrix}\right)$ *is* the state-space form, so the Kalman filter of §21.1 can compute an AR($p$)'s likelihood and handle missing observations — useful the moment your series has holes or your "observation" of $y_t$ is itself noisy, which is exactly §21.4's setting.

## 21.4 Ornstein–Uhlenbeck: a diffusion is an AR(1) in disguise

Continuous-time state spaces close the loop to the stochastic calculus you have seen. The **Ornstein–Uhlenbeck** process — mean-reverting Brownian motion, the Langevin dynamics of module 12 with a quadratic potential —
$$dx = -\theta\,(x-\mu)\,dt + \sigma\,dW,$$
does not need Euler discretization. Its transition density is *exactly* Gaussian (Lawler, by concept: solve the linear SDE with an integrating factor and the increment is a stochastic integral of a deterministic function, hence Gaussian). Over a step $\Delta$,
$$x_{t+\Delta} = \mu + e^{-\theta\Delta}\,(x_t-\mu) + \eta_t,\qquad \eta_t\sim N\!\Big(0,\ \tfrac{\sigma^2}{2\theta}\big(1-e^{-2\theta\Delta}\big)\Big).$$
This is an **AR(1)** with coefficient $a=e^{-\theta\Delta}$ and stationary variance $\sigma^2/(2\theta)$ — exact, not approximate, at *any* step size. Sampling the belt and filtering noisy observations is now the general-$a$ version of §21.1's loop.

```python
# 21.4 -- OU = exact AR(1); filter noisy observations, then infer theta from the same filter
rng_ou = np.random.default_rng(3)
theta, mu_ou, sig_ou, Delta, r_ou, nO = 0.7, 1.0, 0.5, 0.25, 0.05, 250
a  = np.exp(-theta*Delta)                                # exact AR(1) coefficient
s2 = sig_ou**2*(1-np.exp(-2*theta*Delta))/(2*theta)      # exact innovation variance
stat_var = sig_ou**2/(2*theta)                           # stationary variance = s2/(1-a^2)
x = np.zeros(nO); x[0] = mu_ou + rng_ou.normal(0, np.sqrt(stat_var))
for t in range(1, nO):
    x[t] = mu_ou + a*(x[t-1]-mu_ou) + rng_ou.normal(0, np.sqrt(s2))
y_ou = x + rng_ou.normal(0, np.sqrt(r_ou), nO)
print(f"AR(1) coef a = {a:.4f}, innovation var s2 = {s2:.4f}, "
      f"stationary var = {stat_var:.4f} (empirical {x.var():.4f})")

def ou_filter(y, a, mu, s2, r):
    """General 1-D Kalman filter; also returns the log marginal likelihood."""
    m, P, ll = mu, s2/(1-a**2), 0.0
    ms, Ps = np.zeros(len(y)), np.zeros(len(y))
    for t in range(len(y)):
        m_pred, P_pred = mu + a*(m-mu), a**2*P + s2       # predict (general a)
        S = P_pred + r                                    # innovation variance
        ll += stats.norm(m_pred, np.sqrt(S)).logpdf(y[t]) # one-step predictive: FREE likelihood
        Kt = P_pred/S
        m, P = m_pred + Kt*(y[t]-m_pred), (1-Kt)*P_pred    # update (condition)
        ms[t], Ps[t] = m, P
    return ms, Ps, ll

ms_ou, Ps_ou, _ = ou_filter(y_ou, a, mu_ou, s2, r_ou)
print(f"state RMSE: filtered {np.sqrt(np.mean((ms_ou-x)**2)):.3f}  vs raw obs "
      f"{np.sqrt(np.mean((y_ou-x)**2)):.3f}")

# PARAMETER inference (a different job): maximize the filter's marginal likelihood over theta
grid = np.linspace(0.2, 2.0, 60)
lls = np.array([ou_filter(y_ou, np.exp(-th*Delta),
                mu_ou, sig_ou**2*(1-np.exp(-2*th*Delta))/(2*th), r_ou)[2] for th in grid])
print(f"theta MLE from marginal likelihood = {grid[lls.argmax()]:.3f}  (true 0.7)")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4))
tt = np.arange(nO)
a1.plot(tt, x, "k--", lw=1.2, label="latent OU $x_t$")
a1.scatter(tt, y_ou, s=8, color="C7", alpha=0.4, label="noisy obs")
a1.plot(tt, ms_ou, color="C1", lw=1.6, label="filter mean")
a1.fill_between(tt, ms_ou-2*np.sqrt(Ps_ou), ms_ou+2*np.sqrt(Ps_ou), color="C1", alpha=0.2)
a1.set_xlabel("time step"); a1.set_ylabel("$x$"); a1.set_title("State inference: filter the OU path")
a1.legend(fontsize=8)
a2.plot(grid, lls, color="C0")
a2.axvline(theta, color="k", ls="--", label="true $\\theta$")
a2.axvline(grid[lls.argmax()], color="C1", label="MLE")
a2.set_xlabel(r"$\theta$"); a2.set_ylabel("log marginal likelihood")
a2.set_title("Parameter inference: maximize the filter's likelihood")
a2.legend(fontsize=8)
save(fig, "ou-filter")
```

![Left: the latent OU path in black dashed, dense noisy observations as grey dots, and the filter mean with a 2-sigma band tracking the reversion to the mean. Right: the log marginal likelihood as a function of theta, a smooth concave curve peaking near the true value 0.7.](figures/21-state-space/ou-filter.png)

The exact discretization gives $a=$ `0.8395`, innovation variance `0.0527`, and stationary variance `0.1786`, closely tracked by the 250-step path's empirical variance `0.1652` (the ~7% gap is finite-sample noise on a strongly autocorrelated series). Filtering the noisy diffusion cuts the state error from `0.221` to `0.168`.

> **State inference vs. parameter inference — two different jobs.** The left panel *filters the state*: given the parameters $(\theta,\mu,\sigma,r)$, infer the hidden path $x_t$. That is what the Kalman recursion does, and $x_t$ is a fresh unknown at every tick. The right panel *infers a parameter*: $\theta$ is a single unknown fixed across all time, and to learn it you need the likelihood of the whole series, $p(y_{1:n}\mid\theta)$. The filter hands you this **for free** — its one-step-ahead predictive densities multiply to the marginal likelihood (the prediction-error decomposition, $\log p(y_{1:n})=\sum_t \log N(y_t;\,m^-_t, S_t)$, accumulated in `ll` above). Here the grid MLE lands at `0.749`, near the true `0.7`; a full Bayesian treatment would put a prior on $\theta$ and multiply. The reflex to keep: *filtering is line 2 for the state at fixed parameters; learning the parameters is line 2 one level up, and the filter's byproduct is exactly the likelihood that job needs.*

## 21.5 When linear-Gaussian breaks: the bootstrap particle filter

Every filter so far was exact because everything was linear and Gaussian, so every predict/update kept the posterior Gaussian. Break either and the posterior leaves the Gaussian family — no closed form, no `gaussian_condition`. Under *mild* nonlinearity practitioners do not jump to Monte Carlo: the **extended Kalman filter** (EKF, linearize $F$ and $H$ about the current mean) or the **unscented Kalman filter** (UKF, push a few deterministic sigma-points through the exact nonlinearity and refit a Gaussian) keep the cheap Gaussian recursion alive, and are the standard first reach. Particles are for when those break — strong nonlinearity or a multimodal filtering posterior that no single Gaussian can represent. Then the fallback is module 09's Monte Carlo: represent the filtering distribution by *weighted particles* and push them through the same two moves.

Take **stochastic-volatility-lite**: a latent log-variance follows an AR(1), and the observation is Gaussian with a variance that is the *exponential* of the state.
$$x_t = \phi\,x_{t-1} + w_t,\ \ w_t\sim N(0,\sigma^2);\qquad y_t\mid x_t \sim N\!\big(0,\ e^{x_t}\big).$$
The observation depends nonlinearly on $x_t$, so filtering is non-Gaussian. The **bootstrap particle filter** is three lines of idea: (1) *predict* — push each particle through the transition $x_t^i \sim N(\phi x_{t-1}^i, \sigma^2)$ (sampling from the prior is line 3 by Monte Carlo); (2) *update* — weight each particle by the likelihood $w^i \propto p(y_t\mid x_t^i)$ (line 2 as importance reweighting); (3) *resample* — occasionally draw particles in proportion to their weights, killing the starved and cloning the fat.

Leave out step 3 and watch what module 09 warned you about. Every update multiplies the weights by another likelihood; the products spread across orders of magnitude, and the normalized weights concentrate on a single lucky particle.

**Predict.** You run $N=2000$ particles with **no resampling** for 100 steps. *What is the effective sample size after 50 steps?* Commit to a number. *Reason:* the intuition is that 2000 particles is a comfortable cushion — you expect to still have hundreds of effective particles late in the run. Module 09's importance-sampling failure is the same mechanism (a product of likelihoods is one enormous importance weight over a 100-dimensional latent path); recall how its `ess_kong` fraction collapsed as the problem grew.

```python
# 21.5 -- bootstrap particle filter on stochastic volatility; degeneracy vs. resampling
def ess_kong(w):                                          # module 09, verbatim
    return w.sum()**2 / (w**2).sum()

rng_sv = np.random.default_rng(4)
phi_sv, sig_sv, nS = 0.95, 0.25, 100
x_sv = np.zeros(nS); x_sv[0] = rng_sv.normal(0, sig_sv/np.sqrt(1-phi_sv**2))
for t in range(1, nS):
    x_sv[t] = phi_sv*x_sv[t-1] + rng_sv.normal(0, sig_sv)
y_sv = rng_sv.normal(0, 1, nS)*np.exp(x_sv/2)             # returns with time-varying volatility

def bootstrap_pf(y, phi, sig, Np, resample, rng):
    n = len(y)
    x = rng.normal(0, sig/np.sqrt(1-phi**2), Np)          # particles ~ stationary prior
    logw = np.zeros(Np)
    ess, cover = np.zeros(n), np.zeros(n, bool)
    for t in range(n):
        if t > 0:
            x = phi*x + rng.normal(0, sig, Np)            # PREDICT: sample the transition
        y_pred = rng.normal(0, 1, Np)*np.exp(x/2)         # one-step-ahead predictive draws
        lo, hi = np.percentile(y_pred, [2.5, 97.5])
        cover[t] = lo <= y[t] <= hi                       # calibration check (before weighting)
        logw += stats.norm(0, np.exp(x/2)).logpdf(y[t])   # UPDATE: reweight by the likelihood
        w = np.exp(logw - logw.max()); w /= w.sum()
        ess[t] = ess_kong(w)
        if resample and ess[t] < Np/2:                    # RESAMPLE only when ESS drops
            x = x[rng.choice(Np, Np, p=w)]; logw = np.zeros(Np)
    return ess, cover

Np = 2000
ess_no, _     = bootstrap_pf(y_sv, phi_sv, sig_sv, Np, False, np.random.default_rng(40))
ess_yes, cover = bootstrap_pf(y_sv, phi_sv, sig_sv, Np, True,  np.random.default_rng(41))
print(f"NO resampling  -- ESS at t=10/30/50/99: "
      f"{ess_no[10]:.1f} / {ess_no[30]:.1f} / {ess_no[50]:.1f} / {ess_no[99]:.2f}")
print(f"WITH resampling -- ESS min {ess_yes.min():.0f}, median {np.median(ess_yes):.0f}")
print(f"one-step-ahead 95% predictive coverage = {cover.mean():.2f}")

fig, ax = plt.subplots()
ax.plot(ess_no,  color="C3", lw=2, label="no resampling (degenerates)")
ax.plot(ess_yes, color="C0", lw=2, label="resample when ESS < N/2")
ax.axhline(Np, color="k", ls=":", lw=1, label=f"N = {Np} particles")
ax.set_yscale("log"); ax.set_xlabel("time step"); ax.set_ylabel("effective sample size")
ax.set_title("Particle degeneracy: ESS collapses to ~1 without resampling")
ax.legend(fontsize=9)
save(fig, "pf-ess")
```

![Two ESS traces on a log scale. The no-resampling line plunges from near 2000 down to about 1 by the end of the run; the resampling line stays in the high hundreds to low thousands, sawtoothing gently as it resets.](figures/21-state-space/pf-ess.png)

**Reconcile.** The no-resampling ESS falls from `877.7` at step 10 to `43.7` at step 50 and `1.48` at step 99, the last — a single particle holds essentially all the weight, and 1999 others are dead computation. This is *not* a bug; it is module 09's theorem restated on a conveyor belt. Filtering a 100-step path is importance sampling in a 100-dimensional space where the proposal is the *blind* transition prior (it never looks at $y_t$), so the weight variance compounds every step and the ESS fraction collapses — exactly the signature that flagged the $t_3$-from-$N(0,1)$ failure. The naive "2000 is plenty" prediction missed because sample size is no cushion when the weights have (near-)infinite variance; only the *ratio* ESS/$N$ tells the truth, and it goes to zero.

Resampling is the fix and it is cheap: whenever ESS drops below $N/2$, redraw particles proportional to their weights and reset them to equal. The weight variance is periodically annihilated, and ESS stays healthy — minimum `577`, median `1390`. Resampling trades the silent death of importance weights for a controlled, diagnosable refresh; the price is *sample impoverishment* (repeated ancestors reduce diversity of the past), which is why you resample only when you must, not every step. The one-step-ahead predictive is calibrated too — `0.96` of observations land inside their 95% predictive interval, formed before each $y_t$ was seen — the filter's honest self-audit that it is tracking the volatility, not just fitting it.

**RTS smoothing, in one paragraph.** Filtering gives $p(x_t\mid y_{1:t})$ — the state given the *past*. Often you want $p(x_t\mid y_{1:n})$ — the state given *all* the data, past and future — for offline reconstruction. The **Rauch–Tung–Striebel smoother** is a second, backward pass: run the Kalman filter forward, then sweep $t=n{-}1,\dots,1$ correcting each filtered estimate with a gain built from the *next* step's prediction, $m^s_t = m_t + C_t(m^s_{t+1}-m^-_{t+1})$ with $C_t = P_t F^\top (P^-_{t+1})^{-1}$. It is the same two Gaussian moves run in reverse, and it tightens every band by folding in the future. Its particle analogue is backward-simulation smoothing.

## Bridge — the same conditioning, now with a clock

Nothing in this module is new machinery; it is the exact-inference toolkit of Part II set in motion. The Kalman filter's update is module 05's Normal-Normal / `gaussian_condition` (§21.1–2, verified to machine precision); its predict is line 3 marginalization of a Gaussian transition. The gain is the master shrinkage weight, so filtering is partial pooling across time (module 16) with the process noise $q$ playing $\tau^2$. AR(p) is module 14's `nig_regression` on lagged columns (§21.3). The particle filter is module 09's importance sampling with the transition prior as proposal, and its degeneracy is module 09's ESS-fraction collapse (§21.5). And the thread runs on: **tempering** a posterior by raising the likelihood to a power (module 18's $p_\eta$) turns a static inference problem into a synthetic "time" axis, so that **sequential Monte Carlo samplers** filter a sequence of *distributions* — from prior to posterior — using the very resampling machinery here; that is the bridge to the DP/mixture SMC of module 19 and the large-scale tempered posteriors of module 18. Filtering is Bayes on a conveyor belt; SMC is the conveyor belt pointed at a *fixed* target you approach by annealing.

## Pitfalls

- **Confusing process noise with observation noise.** $q$ is how fast the *truth* moves; $r$ is how noisy your *sensor* is. Their ratio sets the steady-state gain. Swapping them, or setting $q=0$ on a genuinely moving state, makes the filter over-trust its prediction and drift off the data — a stuck filter that ignores every observation.
- **Reporting the filtered state when you meant the smoothed one.** Filtering conditions on the past only; for offline analysis you almost always want the RTS smoother, whose bands are strictly tighter. Publishing filter bands as if they used all the data overstates late-time uncertainty and understates early-time uncertainty.
- **Trusting a particle filter by its particle count.** $N=10^5$ particles with ESS $=2$ is two particles with expensive overhead. Always monitor ESS/$N$ over time (module 09); a collapsing fraction is the alarm, and resampling is the response.
- **Resampling every single step.** It controls weight variance but destroys particle diversity in the ancestral path (sample impoverishment), crippling any smoothing estimate. Resample on a threshold (ESS $< N/2$), not reflexively.
- **Filtering with plugged-in parameters and calling it Bayesian.** The Kalman recursion assumes $(F,H,Q,R)$ or $(\theta,\sigma,\dots)$ known. Estimating them is a separate inference on the marginal likelihood the filter produces (§21.4); ignoring that uncertainty gives over-confident state intervals.

## Exercises

**Exercise 21.1 — The gain the sensor deserves.**
*Setup:* In the local-level filter, the steady-state gain solves the Riccati fixed point and depends only on the ratio $q/r$. The §21.1 run used $q=0.5$, $r=2.0$ and converged to `0.3904`.
*Predict:* Make the sensor 10× *noisier* ($r=20$, same $q=0.5$). Does the steady-state gain roughly divide by 10, divide by a bit more than 3, or barely move?
*Reason:* "Gain scales inversely with noise" — treating the map from $r$ to $K$ as linear.
*Run:*
```python
def steady_gain(q, r, iters=500):
    P = r
    for _ in range(iters):
        Pm = P + q; K = Pm/(Pm+r); P = (1-K)*Pm
    return K
for r_ in (2.0, 20.0):
    print(f"r={r_:5.1f}: steady-state gain = {steady_gain(0.5, r_):.4f}")
```
<details><summary>Reconcile</summary>

The gain falls from `0.3904` to `0.1461` — a factor of about 2.7, not 10. The steady-state gain is $K_\infty = P_\infty/(P_\infty+r)$ where $P_\infty$ itself grows with $r$ (a noisier sensor lets more prior uncertainty survive), so the two $r$-dependencies partly cancel. Solving the Riccati equation, $K_\infty \approx \sqrt{q/r}$ in the *small-gain limit* $q/r \to 0$ — a *square-root* law, under which a 10× noisier sensor is discounted by only $\sqrt{10}\approx3.2\times$, because you also become correspondingly less sure of your own prediction. The observed 2.7 is not 3.2 because $r=2$ is not yet in that limit (a gain of 0.39 is far from small); the asymptote is the direction of the law, the finite-$r$ Riccati solution the exact value. Either way the filter degrades gracefully, not linearly — the same square-root-information scaling that governs how fast posteriors concentrate everywhere in the course.
</details>

**Exercise 21.2 — Does a smoother always beat a filter?**
*Setup:* On the §21.1 local-level data, compare the filter's estimate at the *last* time step $t=n{-}1$ with an estimate that also uses future data. At the final step there *is* no future.
*Predict:* Will an RTS smoother improve the estimate at the very last time step $t=n{-}1$, or leave it unchanged?
*Reason:* "Smoothing uses more data, so it always helps" — assuming the future is always available.
*Run:*
```python
# The smoother's backward pass starts from the last filtered value unchanged;
# only earlier steps get corrected by future data.
print(f"filter var at last step P[n-1] = {Ps[-1]:.4f}")
print("smoother var at last step  = same value (no future data exists yet)")
```
<details><summary>Reconcile</summary>

At $t=n{-}1$ the smoother and filter agree exactly — `0.7808` — because the RTS backward pass is *initialized* at the final filtered estimate and only earlier steps receive a correction from later observations. Smoothing helps most in the *middle* of the series, where a step has the most future to borrow from, and not at all at the right edge. This is the temporal face of a general truth: conditioning on more data tightens a posterior, but only data that actually exists. The real-time filter and the retrospective smoother agree at the present moment and diverge as you look backward — which is exactly why online tracking uses the filter and offline reconstruction uses the smoother.
</details>

**Exercise 21.3 — When resampling can't save you.**  *(surprising)*
*Setup:* The bootstrap PF proposes from the *transition prior*, blind to $y_t$. Push the observation noise the other way: make the likelihood extremely sharp (an almost-noiseless sensor) so that only a razor-thin slice of proposed particles has non-negligible weight. Emulate this by shrinking the SV observation to near-deterministic and checking one-step ESS *before* any resampling.
*Predict:* With a very sharp likelihood, does raising the particle count from 2,000 to 20,000 keep per-step ESS comfortably high, or does ESS stay tiny regardless?
*Reason:* "More particles always buys more effective samples" — the cushion intuition again.
*Run:*
```python
def one_step_ess(Np, obs_scale, rng):
    x = rng.normal(0, 1, Np)                       # prior particles
    y = 0.3                                         # a fixed sharp observation
    logw = stats.norm(y, obs_scale).logpdf(x)       # sharp likelihood -> spiky weights
    w = np.exp(logw-logw.max()); w /= w.sum()
    return ess_kong(w)
for Np_ in (2000, 20000):
    e = one_step_ess(Np_, 0.02, np.random.default_rng(7))
    print(f"N={Np_:6d}: one-step ESS = {e:.1f}  ({100*e/Np_:.2f}% of N)")
```
<details><summary>Reconcile</summary>

ESS stays a tiny *fraction* — around `52.6` at N=2,000 (`2.63`% of the particles) and `553.2` at N=20,000 (`2.77`%), essentially the same share either way. Ten times the particles buys ten times the absolute ESS but the *fraction* is stuck, because a blind proposal drops the same vanishing share of particles into the likelihood's narrow slice regardless of how many you throw. Resampling cannot help *within* a step — it only rescues you *across* steps. This is why a sharp likelihood (a precise sensor) is paradoxically *harder* for a bootstrap filter, and why better filters (auxiliary, guided, or the ensemble Kalman filter) build proposals that *look at $y_t$* before proposing. The lesson is module 09's verbatim: fix the proposal, not the sample size.
</details>

**Exercise 21.4 — AR(1) is a discretized diffusion.**  *(ML bridge)*
*Setup:* An AR(1) process $x_t = a\,x_{t-1} + \eta_t$ with $|a|<1$ is the exact discretization of an OU/Langevin diffusion — the same dynamics behind SGLD (module 12) and the forward process of a diffusion model (module 25). Its stationary variance is $\mathrm{Var}_\infty = \sigma_\eta^2/(1-a^2)$.
*Predict:* You want a stationary process with variance 1. If you set $a=0.99$ (very persistent), what innovation standard deviation $\sigma_\eta$ do you need — about 1, about 0.5, or about 0.14?
*Reason:* "The innovation sets the scale, so $\sigma_\eta\approx1$ for unit variance" — ignoring the persistence amplification.
*Run:*
```python
for a_ in (0.0, 0.5, 0.99):
    sig_eta = np.sqrt(1 - a_**2)                    # solve Var_inf = 1
    print(f"a={a_:.2f}: sigma_eta = {sig_eta:.4f}  ->  stationary var "
          f"{sig_eta**2/(1-a_**2):.3f}")
```
<details><summary>Reconcile</summary>

You need $\sigma_\eta=\sqrt{1-a^2}=$ `0.1411` at $a=0.99$ — a *tiny* innovation. A persistent process integrates its own past, so each small kick is amplified by the long memory into a large stationary spread; to hold the variance fixed you must inject less noise per step as $a\to1$. At $a=0$ (no memory, white noise) you need the full $\sigma_\eta=1$. This is exactly the scaling a diffusion model's forward noise schedule must respect, and the reason SGLD's step size and its injected-noise variance are locked together (module 12): the discretization coefficient and the noise are not free knobs — fixing the stationary law ties them. Persistence is amplification; noise must shrink to compensate.
</details>

## Takeaways

- **The Kalman filter is two conjugate moves on a clock:** *predict* marginalizes the Gaussian transition (line 3, uncertainty grows by $q$), *update* is module 05's Normal-Normal conditioning (line 2, uncertainty shrinks). Verified byte-identical to `normal_known_var_update` and `gaussian_condition`.
- **The Kalman gain is the master shrinkage weight** $K = P^-/(P^-+r)$ = data precision / total precision — module 05's formula, module 16's partial pooling, now across time with $q$ in the role of $\tau^2$. Nothing new.
- **AR(p) is conjugate regression on lagged columns** — module 14's `nig_regression` verbatim; check stationarity across the *whole posterior*, not just the mean.
- **An OU diffusion is an AR(1) exactly** (not by Euler): coefficient $e^{-\theta\Delta}$, and the filter's one-step predictive densities multiply to the marginal likelihood you need for parameter inference.
- **State inference and parameter inference are different jobs:** the filter infers the moving state at fixed parameters; learning the parameters is line 2 one level up, fed by the likelihood the filter emits for free.
- **When linear-Gaussian breaks, carry the posterior as weighted particles** — the bootstrap particle filter is importance sampling on a conveyor belt.
- **Particle weights die silently:** ESS collapses to ~1 within tens of steps (module 09's fraction-collapse, `1.48` by the run's last step), and $N$ is no cushion. Monitor ESS/$N$; resample on a threshold; fix the proposal, not the particle count.

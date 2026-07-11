# Selftest module (not part of the curriculum)

Exercises the runner: shared namespace, figure helper, numbers contract,
no-run skipping. The posterior mean below should be `0.7500`.

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "selftest"
FIG = Path("figures") / SLUG
FIG.mkdir(parents=True, exist_ok=True)
SEED = 0
rng = np.random.default_rng(SEED)

def save(fig, name):
    out = FIG / f"{name}.png"
    fig.savefig(out)
    plt.close(fig)
    print(f"[fig] {out}")
```

Beta(3,1) posterior mean:

```python
a, b = 3, 1
print(f"posterior mean = {a/(a+b):.4f}")
fig, ax = plt.subplots()
th = np.linspace(0, 1, 200)
ax.plot(th, stats.beta(a, b).pdf(th))
save(fig, "beta")
```

This block must be skipped (it would crash):

```python no-run
raise RuntimeError("runner failed to skip no-run block")
```

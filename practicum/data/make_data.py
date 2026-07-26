#!/usr/bin/env python3
"""Generate every CSV this guide uses. Run from practicum/:  python data/make_data.py

All data here is synthetic. That is a feature: the true generating process is
written down below, so when a chapter asks you to recover a number you can
check whether you actually got it. Real data would be more interesting and
much less honest — you would never know whether the method worked.

Peeking at the truth before you fit is allowed. Predicting first is better.
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(20260726)


def write(df, name):
    path = OUT / name
    df.to_csv(path, index=False)
    print(f"{name:16s} {len(df):5d} rows  {path.stat().st_size/1024:6.1f} KB  "
          f"cols: {', '.join(df.columns)}")


# 1. commutes -------------------------------------------------------------
# 60 workday commutes. Two ways in: the bus is faster on average but much
# more variable; the bike is slower but dependable. Rain slows both.
# TRUTH: bike ~ Normal(30 + 5*rain, 4);  bus ~ Normal(26 + 4*rain, 9)
# "late" means the trip took more than 35 minutes (the 9:00 stand-up).
n = 60
mode = rng.choice(["bike", "bus"], size=n, p=[0.5, 0.5])
rain = rng.binomial(1, 0.3, size=n)
mu = np.where(mode == "bike", 30 + 5 * rain, 26 + 4 * rain)
sd = np.where(mode == "bike", 4.0, 9.0)
minutes = np.round(rng.normal(mu, sd), 1)
commutes = pd.DataFrame({
    "day": np.arange(1, n + 1),
    "mode": mode,
    "rain": rain,
    "minutes": minutes,
    "late": (minutes > 35).astype(int),
})
write(commutes, "commutes.csv")

# 2. rents ----------------------------------------------------------------
# 180 flats in a mid-sized city. TRUTH:
#   rent = 250 + 11.0*sqm + district_effect + 40*elevator + Normal(0, 90)
#   district effects: centre +180, ring +0, outer -120
districts = rng.choice(["centre", "ring", "outer"], size=180, p=[0.3, 0.45, 0.25])
sqm = np.round(rng.gamma(shape=12, scale=5.5, size=180) + 18).clip(20, 160)
elevator = rng.binomial(1, np.where(districts == "centre", 0.6, 0.3))
d_eff = pd.Series(districts).map({"centre": 180.0, "ring": 0.0, "outer": -120.0}).values
rent = 250 + 11.0 * sqm + d_eff + 40 * elevator + rng.normal(0, 90, 180)
rents = pd.DataFrame({
    "sqm": sqm.astype(int),
    "rooms": np.clip(np.round(sqm / 32), 1, 5).astype(int),
    "district": districts,
    "elevator": elevator,
    "rent": np.round(rent, -1).astype(int),
})
write(rents, "rents.csv")

# 3. tickets --------------------------------------------------------------
# 120 days of support tickets. TRUTH: negative binomial around a mean of
# 18 on weekdays / 7 at weekends, times 1.9 in the week after a release.
# The extra-Poisson spread is the whole point: dispersion parameter 6.
day = np.arange(120)
weekend = ((day % 7) >= 5).astype(int)
release = ((day // 7) % 4 == 0).astype(int)
mean = np.where(weekend, 7.0, 18.0) * np.where(release, 1.9, 1.0)
phi = 6.0                                   # NB dispersion (smaller = wilder)
tickets = rng.negative_binomial(phi, phi / (phi + mean))
write(pd.DataFrame({"day": day, "weekend": weekend, "release": release,
                    "tickets": tickets}), "tickets.csv")

# 4. checkout A/B test ----------------------------------------------------
# TRUTH: A converts at 4.10%, B at 4.85%. Revenue per conversion ~ 62 EUR.
nA, nB = 4_800, 4_800
convA = rng.binomial(1, 0.0410, nA)
convB = rng.binomial(1, 0.0485, nB)
ab = pd.DataFrame({
    "variant": ["A"] * nA + ["B"] * nB,
    "converted": np.concatenate([convA, convB]),
})
ab["order_value"] = np.where(
    ab["converted"] == 1, np.round(rng.gamma(6, 62 / 6, len(ab)), 2), 0.0)
write(ab, "ab_test.csv")

# 5. stores ---------------------------------------------------------------
# 24 branches, wildly different traffic. TRUTH: each branch's true conversion
# rate is drawn from Beta(mean 0.052, concentration 90) — real spread, but far
# less than the raw rates will suggest for the small branches.
# Branch sizes are deliberately skewed (a few flagship stores, many small
# ones) because that is what makes raw league tables lie.
S = 24
true_p = rng.beta(0.052 * 90, (1 - 0.052) * 90, size=S)
visits = np.round(np.exp(rng.normal(5.6, 1.0, size=S))).clip(30, 1500).astype(int)
purchases = rng.binomial(visits, true_p)
write(pd.DataFrame({
    "store": [f"S{i:02d}" for i in range(1, S + 1)],
    "visits": visits, "purchases": purchases}), "stores.csv")

# 6. churn ----------------------------------------------------------------
# 900 subscribers observed for one month. TRUTH (log-odds):
#   -1.15 - 0.055*(tenure-12) + 0.030*(fee-45) + 0.42*tickets
N = 900
tenure = rng.integers(1, 48, N)
fee = np.round(rng.normal(45, 12, N).clip(15, 95), 2)
sup = rng.poisson(0.8, N)
logit = -1.15 - 0.055 * (tenure - 12) + 0.030 * (fee - 45) + 0.42 * sup
churn = rng.binomial(1, 1 / (1 + np.exp(-logit)))
write(pd.DataFrame({"tenure_months": tenure, "monthly_fee": fee,
                    "support_tickets": sup, "churned": churn}), "churn.csv")

print("\nquick sanity checks")
print(f"  commutes: first 20 days, {int(commutes.late[:20].sum())} late of 20")
print(f"  tickets:  mean {tickets.mean():.1f}, variance {tickets.var(ddof=1):.1f}")
print(f"  A/B:      A {convA.mean():.4f}  B {convB.mean():.4f}")
print(f"  stores:   raw best {(purchases/visits).max():.3f} "
      f"(n={visits[np.argmax(purchases/visits)]}), true best {true_p.max():.3f}")
print(f"  churn:    {churn.mean():.3f} churned")

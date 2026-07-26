#!/usr/bin/env python3
"""Generate the capstone datasets.  Run from practicum/:

    python data/make_capstone.py

Three files, three questions, one fictional business (see CAPSTONE.md).

DO NOT read past the SPOILERS banner at the bottom until you have finished the
capstone. The generating parameters are recorded there so you can grade
yourself; reading them first turns the exercise into a reading exercise.
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(31415)

CITIES = ["Aalen", "Brugge", "Cesena", "Delft", "Espoo", "Ferrara",
          "Gouda", "Herning", "Ipswich", "Jena", "Kortrijk", "Lund"]


def write(df, name):
    df.to_csv(OUT / name, index=False)
    print(f"{name:26s} {len(df):5d} rows   cols: {', '.join(df.columns)}")


# ---------------------------------------------------------------- Q1: pricing
# 12 cities x 24 months. Each city has an underlying demand level that head
# office can see but that is NOT in the file except as a noisy proxy
# (local_marketing_spend). Prices were raised in the strong cities, from month 12.
months = np.arange(24)
rows = []
for city in CITIES:
    level = rng.normal(0, 0.5)                      # unrecorded city demand level
    raises = level > 0.0                            # head office raised prices here
    for m in months:
        season = 0.25 * np.sin(m / 12 * 2 * np.pi)
        raised = 1.0 if (raises and m >= 12) else 0.0
        log_price = np.log(19.0) + 0.18 * raised + 0.03 * rng.normal()
        marketing = 400 + 260 * level + rng.normal(0, 120)      # noisy proxy for level
        log_signups = (4.2 - 1.35 * (log_price - np.log(19.0))
                       + 1.10 * level + season + rng.normal(0, 0.10))
        rows.append(dict(city=city, month=int(m),
                         price=round(float(np.exp(log_price)), 2),
                         marketing_spend=round(float(marketing)),
                         signups=int(round(np.exp(log_signups)))))
write(pd.DataFrame(rows), "capstone_signups.csv")

# --------------------------------------------------------------- Q2: capacity
# 40 weeks of daily job counts at one workshop. Overdispersed; Saturdays busy;
# a slow build over the year.
days = np.arange(280)
weekday = days % 7
saturday = (weekday == 5).astype(float)
sunday = (weekday == 6).astype(float)
mean_jobs = np.exp(2.55 + 0.42 * saturday - 1.30 * sunday + 0.0016 * days)
phi = 8.0
jobs = rng.negative_binomial(phi, phi / (phi + mean_jobs))
write(pd.DataFrame({"day": days, "weekday": weekday, "jobs": jobs}),
      "capstone_jobs.csv")

# -------------------------------------------------------------- Q3: mechanics
# 30 mechanics, very different job counts, small true differences in the rate
# at which a repair has to be redone.
M = 30
true_rate = rng.beta(0.06 * 60, 0.94 * 60, size=M)
n_jobs = np.round(np.exp(rng.normal(4.4, 0.95, M))).clip(12, 900).astype(int)
rework = rng.binomial(n_jobs, true_rate)
write(pd.DataFrame({"mechanic": [f"M{i:02d}" for i in range(1, M + 1)],
                    "jobs": n_jobs, "rework": rework}), "capstone_mechanics.csv")

print("\nquick look")
print(f"  signups:   price levels {sorted(set(pd.DataFrame(rows).price.round(0)))[:3]}...")
print(f"  jobs:      mean {jobs.mean():.1f}, variance {jobs.var(ddof=1):.1f}")
print(f"  mechanics: raw rework rate {(rework/n_jobs).min():.3f} to "
      f"{(rework/n_jobs).max():.3f}, pooled {rework.sum()/n_jobs.sum():.3f}")

# =============================================================================
#  S P O I L E R S  —  the true generating parameters. Do not read until done.
# =============================================================================
TRUTH = """
Q1  price elasticity of signups          -1.35
    city demand level -> signups          +1.10 per unit of the unrecorded level
    marketing_spend is a NOISY PROXY for that level: 400 + 260*level + N(0,120).
    Prices were raised by 18% in cities with level > 0, from month 12 onward.
    A naive regression of log(signups) on log(price) is confounded upward and
    gets the SIGN WRONG. One intercept per city (an index variable, ch 04/09)
    blocks the back door and recovers the elasticity from within-city variation.
    Adjusting for the marketing proxy instead helps but does not even fix the
    sign, because the proxy is measured with error. Honest answers say which
    of the two adjustments they trust, and why.

Q2  log mean jobs = 2.55 + 0.42*saturday - 1.30*sunday + 0.0016*day
    negative binomial dispersion phi = 8.0 (a Poisson fit will fail its checks)
    Saturday mean at day 280 is exp(2.55+0.42+0.448) = about 32 jobs.

Q3  true rework rates ~ Beta(3.6, 56.4): mean 0.060, sd about 0.031
    30 mechanics, job counts from 12 to 900.
    The worst raw rate belongs to a low-volume mechanic and shrinks a long way.
"""

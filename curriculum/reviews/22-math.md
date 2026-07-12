# Math review — modules/22-decisions-bandits.md

Referee: mathematical-statistics verification pass. Verdict: **APPROVE** (no sev-1/sev-2; three sev-3 nitpicks).

## Findings

| sev | location | issue | concrete fix |
|---|---|---|---|
| 3 | §22.1 Reconcile | "a factor of 5.5× too low" and, one clause later, "a threshold that the naive rule placed **six times** further away" describe the *same* comparison (0.5 vs 1/11 = 5.5×) with two different multipliers. | Make both read 5.5× (or "about six times" in both), so the reader isn't left reconciling 5.5 vs 6. |
| 3 | §22.1 Run prose | "waiting for 'more likely than not' would let **ten** treatable cases slip through to spare **one** unnecessary pill" inverts the marginal trade: at the 10:1 ratio, one miss costs as much as ten pills (1 miss ↔ 10 pills), not ten misses ↔ one pill. Rhetorical, but the numbers are transposed. | Reword to "…let a treatable case slip through to spare ten unnecessary pills' worth of cost," or drop the specific counts. |
| 3 | §22.3 Reconcile | "B's 1.6-standard-deviation lead" — the standardized gap is (0.0579−0.0419)/0.0097 ≈ **1.65σ**. Rounds to 1.6 or 1.7; not backticked so outside the numbers contract, but 1.7 is the nearer round. | Optional: change to "≈1.7σ" or "over-1.5σ". Harmless as is. |

No sev-1 or sev-2 defects. Derivations, EVSI/EVPI construction, A/B reuse, and the bandit implementation are all correct.

## Required checklist

- [x] **Determinism / harness.** `run_module.py --check-determinism` → PASS in ~15 s (well under budget), exit 0, **zero WARNING lines**, byte-identical two-run output (harness compares out1==out2). Numbers-contract grep clean; no `plt.show`; no legacy `np.random.*`.
- [x] **Deviation (a) — rates 0.3/0.5/0.7 vs syllabus "e.g. 0.35/0.45/0.55": APPROVED.** Verified by independent sim: at gap 0.1 (0.35/0.45/0.55, T=10⁴, 100 reps) UCB1 regret **148.3 > ε-greedy 131.2**, so the clean pedagogical ranking thompson<ucb1<egreedy *would break* — UCB1's loose 8/Δ·lnT constant genuinely makes it trail ε-greedy at small gaps. The author's stated justification is real and documented; "e.g." grants latitude. My reproduction at 0.3/0.5/0.7 matched the module's 19.6/99.7/212.4 exactly.
- [x] **Deviation (b) — S-shaped (non-concave) EVSI explained not tuned away: APPROVED.** Preposterior construction is textbook-correct: draw (θ_A,θ_B) from *current* posteriors → simulate future counts s~Binom(n,θ) per world → recompute the Bayes ship decision from updated posterior *means* (correct: linear regret ⇒ ship higher posterior mean) → evaluate true loss under the *same* drawn θ → average. EVSI = regret_now − regret_after = H·E[chosen−θ_B] ≥ 0, capped by EVPI (185.0 < 200.2 at n=32k). First differences 3.8/18.4/39.6/46.1/40.5/23.6/13.0 are convex-then-concave ⇒ genuine S. Small-batch flatness (EVSI 0.0 at 250/arm) is the real "rarely overturns a 1.6σ lead" effect, not a defect.
- [x] **Vectorization mandate.** Read all three sim functions (`run_bandit`, `run_greedy`, `run_eps`): each loops `for t in range(T)` over **pulls only**; all 100 reps advance simultaneously on `(REPS,K)` arrays. No per-rep Python loop anywhere. Fancy-index Beta update `alpha[rows,arm]+=reward` (rows=arange(REPS), arm shape (REPS,)) is correct — one arm per rep ⇒ no duplicate-index collision ⇒ safe simultaneous per-rep-arm update.
- [x] **Citations.** All external by concept (Russo et al., Lai–Robbins, Auer et al./UCB, C-B §8.3.5/§10, booklet ch.8). No fabricated page numbers. BRIEF-compliant.
- [x] **Notation §3.** θ, p(·), P(·), Beta(α,β), N(μ,σ²) consistent; ρ(·) for expected loss defined at use. No R.
- [x] **SPINE-INDEX consistency.** M05 A/B numbers **exact**: P(B>A)=`0.9510`, regret ratio `81`× (SPINE line 40). M06 callback ("classifier threshold = Bayes rule; 0.5 only under symmetric costs") consistent with M06's loss→action role. M08 complete-class theorem (dep) correctly invoked. M15 (`15-glms-classification`) covers calibration/ECE (SPINE line 100, ECE 0.0207 vs 0.0401) and *explicitly promises* "thresholds ≠ 0.5 (M22)" — the M15↔M22 cross-reference is mutually consistent.
- [x] **Numbers contract spot-check (≥6, all match printed).** p*=`0.0909`; `0.9510`; `81`×; EVPI `200.2`; EVSI `22.2`@n=1000, `148.4`@n=8000; n*=`4000`; regret `19.6`/`99.7`/`212.4`; `10.8`×; greedy `262.6`, lock-in `0.42`; U-shape `65.1`/`64.1`/`108.8`/`206.3`/`405.8`; Ex22.4 EVPI `0.27`, EVSI `0.00`; thresholds `0.0909`/`0.0099`, fracs `0.101`/`0.937`; ρ `0.920`/`0.800`/`0.880`/`1.200`. All reproduced.

## Recomputation list (independently verified)

1. **Threshold.** (1−p)C_FP < p·C_FN ⇒ p > C_FP/(C_FP+C_FN). 10:1 ⇒ 1/11=0.0909; 100:1 ⇒ 1/101=0.0099. ✓ ρ(treat)/ρ(wait) at p=0.08 → 0.920/0.800 (wait); p=0.12 → 0.880/1.200 (treat). ✓
2. **Expected-loss curve semantics.** ρ(treat)=(1−p)C_FP falls in p; ρ(wait)=p·C_FN rises in p; cross at p*. ✓
3. **A/B posteriors.** Beta(1+41,1+959)=Beta(42,960); Beta(1+57,1+943)=Beta(58,944). ✓ P(θ_B>θ_A)=0.9510; loss_ship_A/loss_ship_B = 0.016177/0.000199 = 81×; naive "19-to-1" = 0.951/0.049=19.4. ✓
4. **EVPI = current expected regret.** = H·E[max(θ_A,θ_B)−θ_B] = H·E[max(θ_A−θ_B,0)] = 200.2. Equivalent to E[loss(ship B)] − E[min-loss-per-world]=0 (oracle regret 0). Definition correct. ✓
5. **EVSI(1000)=22.2** vs cost 2·1000·0.01=20 ⇒ net +2.2, keep testing. n*=4000 (net 27.9) is the interior net-value max. ✓
6. **Thompson tournament.** Regret(T)=Σ(θ*−θ_{a_t}), θ*=0.7; inst[t]=mean_reps(best_rate−rates[arm]); cumsum. UCB1 bonus = √(2 ln(t+1)/n_i) — standard √(2 ln t/nᵢ) with the +1 only to avoid ln 0 after seeding. Reproduced 19.6/99.7/212.4; ratio 10.8×. Magnitudes sane: ε-greedy ≈ 0.1·10⁴·0.2 = 200 explore-regret ≈ 212.4. ✓
7. **Pure-greedy lock-in.** regret 262.6 at T=2000; 0.42 of reps end on a suboptimal arm — reproduced-plausible (no forced re-examination). ✓
8. **ε-greedy U-shape.** 65.1/64.1/108.8/206.3/405.8 (seed 1). Checked robustness over seeds 1–5: ε=0.05 < ε=0.01 in **all** five (often by 20–50 conversions); seed=1 is the *most conservative* illustration. Interior minimum genuine, not MC noise. ✓
9. **Ex 22.1.** Beta(2,40) cohort: P(>0.0909)=0.101, P(>0.0099)=0.937. ✓
10. **Ex 22.4 collapse.** B at 80/1000 ⇒ EVPI 0.27, EVSI(250)=0.00 < cost 5.0 ⇒ ship now. ✓

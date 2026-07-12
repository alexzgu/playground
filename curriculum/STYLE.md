# STYLE.md — the author contract

Binding for every module author, reviser, and verifier. A module that violates this file is defective even if its content is brilliant.

## 1. Voice

- No throat-clearing. Banned openers: "In this module we will…", "Before we begin…", "It is important to note…". Start with a claim, a question, or a concrete situation.
- Lead with the concrete instance, then name the abstraction. Never the reverse.
- Every claim carries its warrant nearby: a derivation, a simulation the reader just ran, or a citation. When the warrant is adjacent and unambiguous, no tag is needed; but claims that are NOT theorems must be labeled explicitly:
  - **Heuristic** — practitioner folklore without proof; say so.
  - **Open** — genuinely unsettled; say what's known.
  - (**Theorem** / **Empirical** tags are available and encouraged for marquee results, e.g. stated-not-proved theorems like de Finetti.)
- Callbacks are explicit and load-bearing: "this is module 05's precision-weighted shrinkage formula wearing a Kalman costume", not vague "as we saw earlier".
- The four-line spine (model = joint; inference = conditioning; prediction = marginalization; decision = expected loss) is quoted wherever it does real work — the reader should finish the course with it as a reflex.
- Direct address ("you") is fine. Humor is fine if dry and rare. Padding is a defect.
- **Predict before reveal (demos, not just exercises).** Every marquee demonstration is staged Setup → **Predict** (the reader commits to a number or direction; name the naive intuition being used) → Run → Reconcile (why the naive guess missed). A surprise shown without a captured prediction is a defect — the reader must be *caught* being wrong for the intuition to reorganize.

## 2. Module skeleton (mandatory)

```markdown
# NN. Title

> **Spine.** ⟨ONE sentence a reader should be able to state a week later⟩.
> **Which line?** ⟨where this module sits on the four lines: model / conditioning /
>   prediction / decision — e.g. "line 2, for when the line-3 integral is intractable"⟩.
> **Promise.** After this module you can ⟨capability, not topic⟩.
> **Prereqs.** Modules ⟨list⟩. **Runtime.** ⟨measured⟩ s.
> **Sources.** ⟨bridge list: C-B §, booklet ch., book by concept⟩.

⟨sections: ## NN.1 …, ## NN.2 …⟩

## Bridge — ⟨C-B / booklet / ML-practice tie-in⟩   (≥1 per module, may be a subsection)

## Pitfalls
⟨the 3–5 mistakes practitioners actually make here⟩

## Exercises
⟨3–6, predict-then-run format, solutions in <details>⟩

## Takeaways
⟨≤7 bullets a reader should be able to reproduce from memory a week later⟩
```

Length: 2,500–5,000 words of prose (code excluded). If you can't fit, the module is mis-scoped — flag it, don't compress into un-clarity.

## 3. Notation (course-wide, loud)

| Object | Notation | Convention |
|---|---|---|
| Densities / pmfs | p(·) | generic; subscripts only when ambiguous |
| Event probability | P(·) | |
| Unknowns/parameters | θ, φ, λ, μ, σ² … | anything unknown is a random variable |
| Observed data | y (response), x (covariates, conditioned on) | D = {(xᵢ, yᵢ)}ⁿᵢ₌₁ |
| Future data | ỹ | posterior predictive p(ỹ \| y) |
| Normal | N(μ, σ²) | **second argument is the VARIANCE** |
| Gamma | Gamma(α, β) | **β is the RATE**; scipy: `gamma(a=α, scale=1/β)` |
| Exponential | Exp(λ) | rate; scipy: `expon(scale=1/λ)` |
| Inverse-Gamma | IG(α, β) | scipy: `invgamma(a=α, scale=β)` |
| Student-t | t_ν(μ, σ²) | location–scale; scipy: `t(df=ν, loc=μ, scale=σ)` |
| Beta, Binomial, Poisson, Dirichlet, Multinomial | standard | |
| KL divergence | KL(q ‖ p) | = E_q[log q − log p] |
| Expectation/Variance | E[·], Var[·], Cov[·, ·] | subscript the measure when ambiguous: E_{θ\|y}[·] |
| Proportionality | ∝ | drop constants not involving the target variable |

State the variance/rate conventions in module 00 and never re-litigate them. When a scipy call embodies a convention trap (Gamma rate/scale!), comment it inline.

LaTeX: inline `$…$`, display `$$…$$`. Define every symbol at first use in each module (modules are re-readable standalone).

## 4. Code contract

Blocks run **in order, in one shared namespace**, with cwd = `curriculum/`, via `tools/run_module.py`. Rules:

1. **Block 1 of every module is exactly this setup block** (adjust only `SLUG`):

```python
# --- setup ---
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

SLUG = "05-conjugate-updating"          # this module's figure dir
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

2. Randomness ONLY through `rng` (or an explicitly seeded local generator). Never `np.random.*` legacy calls, never unseeded anything. PyMC: pass `random_seed=SEED` to `pm.sample`.
3. **The numbers contract:** every numeric claim in prose is `print`ed by a block, and the prose quotes it in backticks matching the printed precision (e.g. prose says "PPV = `0.0194`", a block prints `PPV = 0.0194`). Verifiers cross-check mechanically; an unprinted prose number is a defect.
4. Figures: only via `save(fig, "name")`; never `plt.show()`. Reference in prose as `![caption](figures/<slug>/name.png)` with a real caption. Every figure is *discussed* — an unreferenced figure is a defect.
5. Illustrative-only code (pseudocode, API sketches) goes in ```` ```python no-run ```` blocks — the runner skips them. Everything else must run.
6. Runtime: **target <120 s, hard cap 300 s per module** on 2 CPUs. Size MCMC accordingly (e.g. 2 chains × 2,000 draws is usually plenty for demos; prefer analytic overlays to brute force). Print nothing gigantic (no dumping arrays > ~20 elements).
7. Libraries: numpy / scipy / matplotlib / pandas / sklearn / statsmodels freely. **The course PPL is NumPyro** (+ ArviZ for diagnostics) — pytensor's C backend is broken in this environment, so PyMC cannot sample at usable speed; PyMC may appear only in ```python no-run``` illustration blocks, clearly labeled. NumPyro/ArviZ usage must copy idioms from `tools/ppl_idioms.py` (smoke-tested against installed versions — do not trust remembered APIs; arviz here is 1.x with e.g. `ci_prob=` in `az.summary`). No seaborn. No internet. No file writes outside `figures/` and `data/`.
8. Data: synthesize with `rng`, or read a small committed CSV under `data/` (<100 KB). No downloads.
9. Style: numpy-vectorized where natural; comment density like good library code — explain the *statistics*, not the syntax; functions for anything reused; no classes unless they pay rent.

## 5. Exercises — predict-then-run (mandatory format)

```markdown
**Exercise NN.k — ⟨name⟩.**
*Setup:* ⟨2–4 sentences, concrete, real numbers⟩
*Predict:* ⟨question forcing a committed guess BEFORE any code: a number, a
  ranking, a direction. Choose scenarios where the naive answer is wrong.⟩
*Reason:* ⟨one line: name the intuition being used — so when it breaks, the
  reader knows WHICH intuition to repair⟩
*Run:* ⟨the exact code — usually a ≤10-line variation of module code⟩
<details><summary>Reconcile</summary>

⟨the actual numbers; WHY the naive prediction missed; the general lesson —
the compression. Never just "the answer is 0.75."⟩
</details>
```

At least one exercise per module must have a genuinely surprising answer (naive prediction fails). At least one must connect to the learner's ML/DL background.

## 6. Rigor etiquette

- Derivations: show the two or three real steps, elide arithmetic with "expand and collect", never elide the conceptual step. If a proof is beyond scope, state the theorem precisely, cite, and *verify numerically*.
- Regularity conditions: name them when they can actually fail in practice (BvM and mixture posteriors; CLT and heavy tails), footnote-level otherwise.
- Never fabricate citations, page numbers, or numeric results. Cite local sources by section (verify by opening them); external books by concept ("BDA3 ch. 5").
- **R-leak caution:** the booklet's code is R (and its ch. 12 leans on R-INLA). Absorb its *statistics*, never its idioms; the curriculum contains no R and no R-package dependencies, not even in asides.
- When a claim is checked by comparing two routes (analytic vs simulated), print both and their difference — that printed agreement IS the pedagogy.

## 7. Figures

- Every figure earns its place: it must show something prose can't (a shape, a collapse, a divergence). Axis labels with units/meaning, title stating the takeaway (not just the topic), legend when >1 series.
- Colors: matplotlib default cycle; consistent meaning across a module (e.g. prior always C0, posterior always C1, truth always black dashed).
- One idea per figure. Small multiples over overloaded axes.

## 8. Review gates (what verifiers will do to your module)

1. `python tools/run_module.py modules/NN-slug.md` exits 0 within budget.
2. Determinism: two runs produce byte-identical printed output.
3. Numbers contract grep: prose backtick-numbers ⊆ printed output.
4. Math review: derivations correct, labels (Theorem/Empirical/Heuristic/Open) honest.
5. Pedagogy review: spine stateable in one sentence; predict-then-run exercises genuine; no fluff.
6. Consistency: notation table respected; callbacks point at real content.

#!/usr/bin/env python3
"""Verification harness for curriculum modules.

Extracts ```python fenced blocks from a module markdown file and executes
them in order in one shared namespace, with cwd = curriculum root. Blocks
tagged ```python no-run are skipped. See STYLE.md §4 for the code contract.

Usage:
  python tools/run_module.py modules/05-conjugate-updating.md
  python tools/run_module.py modules/05-*.md --check-determinism
  python tools/run_module.py modules/05-*.md --stats     # no execution
  python tools/run_module.py modules/05-*.md --list      # show blocks

Exit codes: 0 = all blocks ran (warnings allowed), 1 = a block raised,
2 = usage/parse error, 3 = hard time cap exceeded.
"""

from __future__ import annotations

import argparse
import io
import os
import re
import sys
import time
import traceback
from contextlib import redirect_stdout
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

CURRICULUM_ROOT = Path(__file__).resolve().parent.parent
HARD_CAP_S = 300.0
TARGET_S = 120.0

FENCE_RE = re.compile(r"^```python([^\n]*)\n(.*?)^```[ \t]*$", re.M | re.S)


def extract_blocks(text: str) -> list[tuple[int, str, bool]]:
    """Return [(start_line, code, runnable), ...] for each python fence."""
    blocks = []
    for m in FENCE_RE.finditer(text):
        tag = m.group(1).strip().lower()
        runnable = "no-run" not in tag
        start_line = text[: m.start()].count("\n") + 2  # first code line
        blocks.append((start_line, m.group(2), runnable))
    return blocks


def prose_stats(text: str) -> dict:
    """Word count of prose (code fences stripped), plus block counts."""
    stripped = FENCE_RE.sub("", text)
    stripped = re.sub(r"```.*?```", "", stripped, flags=re.S)  # other fences
    words = len(stripped.split())
    blocks = extract_blocks(text)
    return {
        "prose_words": words,
        "blocks_total": len(blocks),
        "blocks_runnable": sum(1 for *_, r in blocks if r),
        "figures_referenced": len(re.findall(r"!\[[^\]]*\]\(figures/", text)),
        "details_solutions": len(re.findall(r"<details>", text)),
    }


def run_blocks(path: Path, blocks, quiet: bool = False) -> tuple[bool, str, float]:
    """Execute runnable blocks in one namespace. Returns (ok, output, secs)."""
    ns: dict = {"__name__": "__main__", "__file__": str(path)}
    pieces: list[str] = []
    t0 = time.perf_counter()
    ok = True
    for i, (line, code, runnable) in enumerate(blocks, 1):
        if not runnable:
            continue
        buf = io.StringIO()
        tb = time.perf_counter()
        try:
            with redirect_stdout(buf):
                exec(compile(code, f"{path.name}:block{i}@L{line}", "exec"), ns)
        except Exception:
            pieces.append(buf.getvalue())
            pieces.append(f"\n### BLOCK {i} (line {line}) RAISED ###\n")
            pieces.append(traceback.format_exc())
            ok = False
            break
        dt = time.perf_counter() - tb
        pieces.append(buf.getvalue())
        if not quiet:
            print(f"  block {i:>2} (L{line:>4}) ok in {dt:6.1f}s", file=sys.stderr)
    total = time.perf_counter() - t0
    return ok, "".join(pieces), total


def check_numbers_contract(text: str, output: str) -> list[str]:
    """Backtick-quoted numerics in prose should appear in printed output."""
    prose = FENCE_RE.sub("", text)
    quoted = re.findall(r"`(-?\d+(?:\.\d+)?(?:e-?\d+)?)`", prose)
    missing = sorted({q for q in quoted if q not in output})
    return missing


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("module", type=Path)
    ap.add_argument("--check-determinism", action="store_true")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--hard-cap", type=float, default=HARD_CAP_S)
    args = ap.parse_args()

    path = args.module if args.module.is_absolute() else CURRICULUM_ROOT / args.module
    if not path.exists():
        print(f"no such module: {path}", file=sys.stderr)
        return 2
    text = path.read_text()
    blocks = extract_blocks(text)

    if args.list:
        for i, (line, code, runnable) in enumerate(blocks, 1):
            flag = "run " if runnable else "SKIP"
            head = code.strip().splitlines()[0] if code.strip() else "(empty)"
            print(f"block {i:>2} L{line:>4} [{flag}] {head[:70]}")
        return 0

    stats = prose_stats(text)
    if args.stats:
        for k, v in stats.items():
            print(f"{k}: {v}")
        return 0

    os.chdir(CURRICULUM_ROOT)
    print(f"== {path.name}: {stats['blocks_runnable']} runnable blocks ==",
          file=sys.stderr)
    ok, out1, t1 = run_blocks(path, blocks)

    logdir = CURRICULUM_ROOT / "tools" / "logs"
    logdir.mkdir(exist_ok=True)
    (logdir / f"{path.stem}.out.txt").write_text(out1)
    print(out1)

    warnings: list[str] = []
    if not ok:
        print(f"FAIL after {t1:.1f}s (output logged)", file=sys.stderr)
        return 1
    if t1 > args.hard_cap:
        print(f"HARD CAP EXCEEDED: {t1:.1f}s > {args.hard_cap}s", file=sys.stderr)
        return 3
    if t1 > TARGET_S:
        warnings.append(f"runtime {t1:.1f}s exceeds {TARGET_S}s target")
    if "plt.show(" in text:
        warnings.append("plt.show() present (banned; see STYLE.md)")
    if re.search(r"np\.random\.(?!default_rng)", text):
        warnings.append("legacy np.random.* call (banned; use default_rng)")
    missing = check_numbers_contract(text, out1)
    if missing:
        warnings.append(f"prose numbers not in printed output: {missing[:10]}")

    if args.check_determinism:
        ok2, out2, t2 = run_blocks(path, blocks, quiet=True)
        if not ok2:
            print("FAIL on second (determinism) run", file=sys.stderr)
            return 1
        if out1 != out2:
            warnings.append("NON-DETERMINISTIC: printed output differs between runs")

    print(f"PASS in {t1:.1f}s "
          f"({stats['prose_words']} prose words, "
          f"{stats['blocks_runnable']} blocks, "
          f"{stats['figures_referenced']} figs referenced)", file=sys.stderr)
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

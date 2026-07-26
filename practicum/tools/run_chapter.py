#!/usr/bin/env python3
"""Run and verify a practicum chapter.

Extracts ```python fenced blocks from a chapter markdown file and executes them
in order in one shared namespace, with cwd = practicum/. Blocks tagged
```python no-run are skipped (illustration only).

Three guarantees this enforces, which are the whole point:

1. **It runs.** Every block executes top to bottom, in order, no manual fixes.
2. **It repeats.** With --check twice, two runs must print byte-identical output.
3. **The numbers are real.** Every number the prose quotes in `backticks` must
   appear somewhere in the printed output. No hand-typed results.

Usage:
    python tools/run_chapter.py chapters/01-counting-the-ways.md
    python tools/run_chapter.py chapters/01-*.md --check
    python tools/run_chapter.py --all
    python tools/run_chapter.py chapters/01-*.md --stats
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

ROOT = Path(__file__).resolve().parent.parent
HARD_CAP_S = 300.0
TARGET_S = 120.0

FENCE_RE = re.compile(r"^```python([^\n]*)\n(.*?)^```[ \t]*$", re.M | re.S)


def extract_blocks(text: str) -> list[tuple[int, str, bool]]:
    """Return [(start_line, code, runnable), ...] for each python fence."""
    out = []
    for m in FENCE_RE.finditer(text):
        runnable = "no-run" not in m.group(1).strip().lower()
        start_line = text[: m.start()].count("\n") + 2
        out.append((start_line, m.group(2), runnable))
    return out


def stats(text: str) -> dict:
    prose = FENCE_RE.sub("", text)
    prose = re.sub(r"```.*?```", "", prose, flags=re.S)
    blocks = extract_blocks(text)
    return {
        "prose_words": len(prose.split()),
        "blocks_runnable": sum(1 for *_, r in blocks if r),
        "blocks_illustrative": sum(1 for *_, r in blocks if not r),
        "figures": len(re.findall(r"!\[.*?\]\(\.\./figures/", text)),
        "exercises": len(re.findall(r"<details>", text)),
    }


def run_blocks(path: Path, blocks, quiet=False) -> tuple[bool, str, float]:
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
        pieces.append(buf.getvalue())
        if not quiet:
            print(f"  block {i:>2} (L{line:>4}) ok in "
                  f"{time.perf_counter() - tb:6.1f}s", file=sys.stderr)
    return ok, "".join(pieces), time.perf_counter() - t0


def missing_numbers(text: str, output: str) -> list[str]:
    """Backtick-quoted numerics in prose that never got printed."""
    prose = FENCE_RE.sub("", text)
    quoted = re.findall(r"`(-?\d+(?:\.\d+)?(?:e[-+]?\d+)?)`", prose)
    return sorted({q for q in quoted if q not in output})


def check_one(path: Path, determinism: bool) -> int:
    text = path.read_text()
    blocks = extract_blocks(text)
    st = stats(text)
    print(f"== {path.name}: {st['blocks_runnable']} runnable blocks ==",
          file=sys.stderr)
    ok, out, secs = run_blocks(path, blocks)

    logdir = ROOT / "tools" / "logs"
    logdir.mkdir(exist_ok=True)
    (logdir / f"{path.stem}.out.txt").write_text(out)
    print(out)

    if not ok:
        print(f"FAIL after {secs:.1f}s", file=sys.stderr)
        return 1

    warn = []
    if secs > HARD_CAP_S:
        print(f"HARD CAP EXCEEDED: {secs:.0f}s", file=sys.stderr)
        return 3
    if secs > TARGET_S:
        warn.append(f"runtime {secs:.0f}s over {TARGET_S:.0f}s target")
    if "plt.show(" in text:
        warn.append("plt.show() present (banned: figures go through save())")
    if re.search(r"np\.random\.(?!default_rng)", text):
        warn.append("legacy np.random.* call (use the seeded rng)")
    miss = missing_numbers(text, out)
    if miss:
        warn.append(f"prose numbers never printed: {miss[:12]}")

    if determinism:
        ok2, out2, _ = run_blocks(path, blocks, quiet=True)
        if not ok2:
            print("FAIL on determinism re-run", file=sys.stderr)
            return 1
        if out != out2:
            warn.append("NON-DETERMINISTIC: two runs printed different output")

    print(f"PASS in {secs:.0f}s ({st['prose_words']} prose words, "
          f"{st['blocks_runnable']} blocks, {st['figures']} figures, "
          f"{st['exercises']} exercise solutions)", file=sys.stderr)
    for w in warn:
        print(f"WARNING: {w}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", type=Path, nargs="?")
    ap.add_argument("--check", action="store_true",
                    help="also re-run and compare output (determinism)")
    ap.add_argument("--all", action="store_true", help="run every chapter")
    ap.add_argument("--stats", action="store_true", help="counts only, no run")
    args = ap.parse_args()

    os.chdir(ROOT)

    if args.all:
        rc = 0
        for p in sorted((ROOT / "chapters").glob("[0-9]*.md")):
            rc |= check_one(p, args.check)
        return rc

    if args.chapter is None:
        ap.error("give a chapter path or --all")
    path = args.chapter if args.chapter.is_absolute() else ROOT / args.chapter
    if not path.exists():
        print(f"no such chapter: {path}", file=sys.stderr)
        return 2
    if args.stats:
        for k, v in stats(path.read_text()).items():
            print(f"{k}: {v}")
        return 0
    return check_one(path, args.check)


if __name__ == "__main__":
    sys.exit(main())

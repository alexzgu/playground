#!/usr/bin/env python3
"""Generate companion Jupyter notebooks from the curriculum modules.

Format-only conversion: markdown between code fences becomes markdown cells;
runnable ```python fences become code cells; ```python no-run fences stay as
markdown (fenced, non-executable). The notebook's concatenated code is
verified byte-identical to what tools/run_module.py executes, so the
notebooks inherit the modules' verification without re-running anything.

Usage:  python tools/make_notebooks.py          # writes notebooks/*.ipynb
        python tools/make_notebooks.py --check  # equivalence check only
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_module import FENCE_RE, extract_blocks  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "notebooks"

HEADER = (
    "> **Companion notebook** — generated from `modules/{name}` "
    "(the canonical, harness-verified text; regenerate with "
    "`python tools/make_notebooks.py`). Run cells top-to-bottom from the "
    "`curriculum/` directory so `figures/...` paths resolve. Cells marked "
    "*illustration only* are intentionally not executable."
)


def md_cell(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {},
            "source": source.splitlines(keepends=True)}


def code_cell(source: str) -> dict:
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": source.rstrip("\n").splitlines(keepends=True)}


def convert(path: Path) -> dict:
    text = path.read_text()
    cells = [md_cell(HEADER.format(name=path.name))]
    pos = 0
    for m in FENCE_RE.finditer(text):
        before = text[pos:m.start()].strip("\n")
        if before.strip():
            cells.append(md_cell(before))
        tag = m.group(1).strip().lower()
        code = m.group(2)
        if "no-run" in tag:
            cells.append(md_cell("*Illustration only (not executable):*\n\n"
                                 "```python\n" + code.rstrip("\n") + "\n```"))
        else:
            cells.append(code_cell(code))
        pos = m.end()
    tail = text[pos:].strip("\n")
    if tail.strip():
        cells.append(md_cell(tail))
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python",
                           "name": "python3"},
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def notebook_code(nb: dict) -> str:
    return "\n".join("".join(c["source"]) for c in nb["cells"]
                     if c["cell_type"] == "code")


def module_code(path: Path) -> str:
    return "\n".join(code.rstrip("\n") for _, code, runnable
                     in extract_blocks(path.read_text()) if runnable)


def main() -> int:
    check_only = "--check" in sys.argv
    OUT.mkdir(exist_ok=True)
    modules = sorted(ROOT.glob("modules/[0-2][0-9]-*.md"))
    bad = 0
    for mod in modules:
        nb = convert(mod)
        want = module_code(mod)
        got = notebook_code(nb)
        ok = want == got
        bad += not ok
        target = OUT / (mod.stem + ".ipynb")
        if not check_only:
            target.write_text(json.dumps(nb, ensure_ascii=False, indent=1))
        n_code = sum(c["cell_type"] == "code" for c in nb["cells"])
        print(f"{mod.stem}: {len(nb['cells'])} cells ({n_code} code) "
              f"equivalence={'OK' if ok else 'MISMATCH'}")
    print(f"\n{len(modules)} notebooks, {bad} mismatches")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

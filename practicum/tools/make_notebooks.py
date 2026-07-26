#!/usr/bin/env python3
"""Generate a Jupyter notebook for each chapter, from the chapter markdown.

The code is copied byte-for-byte, so a notebook and its chapter cannot drift.
Prose becomes markdown cells; ```python no-run blocks become markdown too, so
nothing in a notebook fails when you run it top to bottom.

    python tools/make_notebooks.py
"""
from __future__ import annotations

import re
from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"^```python([^\n]*)\n(.*?)^```[ \t]*$", re.M | re.S)

BOOTSTRAP = '''\
# Run from anywhere: this puts us in practicum/ so data/ and figures/ resolve.
import os, sys
if os.path.basename(os.getcwd()) == "notebooks":
    os.chdir("..")
sys.path.insert(0, os.getcwd())
print("working directory:", os.getcwd())
'''


def build(path: Path) -> nbf.NotebookNode:
    text = path.read_text()
    nb = nbf.v4.new_notebook()
    cells = [nbf.v4.new_code_cell(BOOTSTRAP)]

    pos = 0
    for m in FENCE.finditer(text):
        prose = text[pos:m.start()].strip()
        if prose:
            cells.append(nbf.v4.new_markdown_cell(prose))
        code = m.group(2).rstrip()
        if "no-run" in m.group(1).lower():
            cells.append(nbf.v4.new_markdown_cell(f"```python\n{code}\n```"))
        else:
            cells.append(nbf.v4.new_code_cell(code))
        pos = m.end()
    tail = text[pos:].strip()
    if tail:
        cells.append(nbf.v4.new_markdown_cell(tail))

    nb["cells"] = cells
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python",
                       "name": "python3"},
        "language_info": {"name": "python"},
    }
    return nb


def main() -> None:
    out_dir = ROOT / "notebooks"
    out_dir.mkdir(exist_ok=True)
    for chapter in sorted((ROOT / "chapters").glob("[0-9]*.md")):
        nb = build(chapter)
        target = out_dir / f"{chapter.stem}.ipynb"
        nbf.write(nb, target)
        n_code = sum(c["cell_type"] == "code" for c in nb["cells"])
        print(f"{target.relative_to(ROOT)}  ({n_code} code cells)")


if __name__ == "__main__":
    main()

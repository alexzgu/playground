#!/usr/bin/env python3
"""Build a text-faithful manual baseline for Statistical Rethinking pp. 211-240.

The source PDF has a clean text layer.  This script removes only running
headers/footers, rejoins words split solely by a typesetting line break, and
adds the repository's required page heading.  Page-specific visual structure
(math, code, tables, figures, and section/box headings) is applied in a
subsequent reviewed pass.
"""

from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
BASE = HERE / "books" / "statistical_rethinking"
TEXT = BASE / "text"
PAGES = BASE / "out" / "pages"


def body_lines(page: int) -> list[str]:
    lines = (TEXT / f"p-{page:04d}.txt").read_text().splitlines()
    if page == 211:
        if lines and lines[-1].strip() == "195":
            lines.pop()
    else:
        # The first two extracted lines are the printed page number and running
        # header, in alternating order on recto/verso pages.
        lines = lines[2:]

    # Rejoin words split by a typesetting line break, while preserving all
    # remaining source line boundaries for the visual-formatting pass.
    joined: list[str] = []
    for line in lines:
        line = line.rstrip()
        if joined and joined[-1].endswith("-") and re.match(r"^[a-z]", line.lstrip()):
            joined[-1] = joined[-1][:-1] + line.lstrip()
        else:
            joined.append(line)
    return joined


def main() -> None:
    PAGES.mkdir(parents=True, exist_ok=True)
    for page in range(211, 241):
        printed = page - 16
        content = "\n".join(body_lines(page)).strip()
        rendered = f"### PDF page {page} (book page {printed})\n\n{content}\n"
        (PAGES / f"p-{page:04d}.md").write_text(rendered)


if __name__ == "__main__":
    main()

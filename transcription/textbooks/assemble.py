#!/usr/bin/env python3
"""Stitch per-page transcripts into chapter files under curriculum_material/<key>/.

Chapter membership is by PDF page number against the ranges in books.json (these
are digital PDFs — the PDF page <-> content mapping is fixed, unlike the scanned
booklet). Idempotent; safe to run while transcription is still in progress
(chapter files carry a completeness note until all their pages exist).

Usage: python3 assemble.py [--book KEY]
"""
import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CM = HERE.parent.parent / "curriculum_material"
DONE = ("transcribed", "transcribed-lowqa")


def slug(title: str, maxlen: int = 44) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:maxlen].rstrip("-")


def units_for(book: dict) -> list[dict]:
    """Ordered (filename, header, pdf range) units covering PDF pages 1..npages."""
    chs = sorted(book["chapters"], key=lambda c: c["pdf_start"])
    units = []
    if chs and chs[0]["pdf_start"] > 1:
        units.append({"fname": "ch00-front-matter.md", "header": "# Front matter",
                      "start": 1, "end": chs[0]["pdf_start"] - 1})
    for i, c in enumerate(chs):
        end = (chs[i + 1]["pdf_start"] - 1) if i + 1 < len(chs) else book["npages"]
        num = c["num"]
        if num and num.isdigit():
            fname = f"ch{int(num):02d}-{slug(c['title'])}.md"
            header = f"# Chapter {num} — {c['title']}"
        elif num:  # appendix letter
            fname = f"appendix-{num.lower()}-{slug(c['title'])}.md"
            header = f"# Appendix {num} — {c['title']}"
        else:      # named front/back matter (Preface, Contents, Index)
            fname = f"{slug(c['title'])}.md"
            header = f"# {c['title']}"
        units.append({"fname": fname, "header": header, "start": c["pdf_start"], "end": end})
    return units


def ranges(nums: list[int]) -> str:
    if not nums:
        return "none"
    spans, a = [], nums[0]
    for x, y in zip(nums, nums[1:] + [None]):
        if y != x + 1:
            spans.append(f"{a}–{x}" if a != x else f"{x}")
            a = y
    return ", ".join(spans)


def assemble_book(book: dict) -> None:
    key = book["key"]
    out = HERE / "books" / key / "out"
    dest = CM / key
    dest.mkdir(exist_ok=True)
    manifest = json.loads((out / "manifest.json").read_text()) if (out / "manifest.json").exists() else {}

    done_pages = {}
    for name, entry in manifest.items():
        p = int(name.split("-")[1])
        f = out / "pages" / f"p-{p:04d}.md"
        if entry.get("status") in DONE and f.exists():
            done_pages[p] = (entry, f)

    written = 0
    for u in units_for(book):
        have = sorted(p for p in done_pages if u["start"] <= p <= u["end"])
        if not have:
            continue
        total = u["end"] - u["start"] + 1
        printed = [done_pages[p][0].get("printed_page") for p in have]
        printed = [x for x in printed if x]
        span = f"*(PDF pages {u['start']}–{u['end']}"
        if printed:
            span += f"; book pages {printed[0]}–{printed[-1]}"
        span += ")*"
        parts = [u["header"] + "\n" + span]
        if len(have) < total:
            missing = [p for p in range(u["start"], u["end"] + 1) if p not in done_pages]
            parts.append(f"*⚠ In progress: {len(have)} of {total} pages transcribed; "
                         f"missing PDF pages {ranges(missing)}.*")
        parts += [done_pages[p][1].read_text().strip() for p in have]
        (dest / u["fname"]).write_text("\n\n".join(parts).rstrip() + "\n")
        written += 1

    write_readme(book, dest, manifest, done_pages)
    n = len(done_pages)
    print(f"{key}: {written} chapter files, {n}/{book['npages']} pages", flush=True)


def write_readme(book, dest, manifest, done_pages):
    n, N = len(done_pages), book["npages"]
    missing = [p for p in range(1, N + 1) if p not in done_pages]
    lowqa = sorted(int(k.split("-")[1]) for k, v in manifest.items()
                   if v.get("status") == "transcribed-lowqa")
    provenance_counts = {}
    for entry, _ in done_pages.values():
        model = entry.get("model")
        if model:
            key = (model, entry.get("effort"))
            provenance_counts[key] = provenance_counts.get(key, 0) + 1
    if provenance_counts:
        provenance = "; ".join(
            f"`{model}`"
            + (f" at {effort} effort" if effort else "")
            + f" ({count} page{'s' if count != 1 else ''})"
            for (model, effort), count in sorted(
                provenance_counts.items(), key=lambda item: (-item[1], item[0])
            )
        )
        model_line = (
            f"- Page transcription provenance: {provenance}. Per-page provenance "
            "is recorded in the pipeline manifest"
        )
    else:
        model_line = (
            "- Transcribed from page images by "
            f"`{book.get('transcription_model', 'claude-opus-4-8')}`"
        )
    lines = [
        f"# {book['title']} — Transcript",
        "",
        f"Source: `{book['pdf']}` — {book['author']}. {N} PDF pages, typeset digital PDF.",
        "",
        "**Conventions**",
        "- One markdown file per chapter; every page appears under a heading "
        "`### PDF page N (book page M)`.",
        "- Math in LaTeX (`$...$` / `$$...$$`), equation numbers as `\\tag{}`; tables as "
        "markdown tables; figures as verbatim captions plus an italic description; "
        "code in fenced blocks.",
        model_line
        + (", cross-checked against the PDF text layer (per-page QA score in the "
           "pipeline manifest)." if not book["text_layer"].startswith("unusable")
           else "; this book's PDF text layer is unusable (cipher fonts), so pages were "
                "transcribed from the images alone."),
        "- Unlike `bayesian_booklet`, quantitative results are **not** SymPy-verified.",
        "",
        "## STATUS OF THIS TRANSCRIPT",
        "",
    ]
    if not missing:
        lines.append(f"**Complete:** all {N} PDF pages transcribed.")
    else:
        lines.append(f"**Transcribed:** {n}/{N} PDF pages ({ranges(sorted(done_pages))}). "
                     f"**Missing:** {ranges(missing)}.")
    if lowqa:
        lines.append(f"\nPages whose text-layer cross-check scored low (worth a "
                     f"spot-check): {ranges(lowqa)}.")
    lines += ["", "Produced by the pipeline in `transcription/textbooks/` "
                  "(see its README)."]
    (dest / "README.md").write_text("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--book", help="book key (default: all with any pages done)")
    args = ap.parse_args()
    for book in json.loads((HERE / "books.json").read_text()):
        if args.book and book["key"] != args.book:
            continue
        if not args.book and not (HERE / "books" / book["key"] / "out" / "manifest.json").exists():
            continue
        assemble_book(book)


if __name__ == "__main__":
    main()

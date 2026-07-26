#!/usr/bin/env python3
"""Recover a repeatedly filtered page through smaller Opus 5 image fragments."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

from PIL import Image

from transcribe_books import (
    HERE,
    book_dirs,
    find_claude,
    load_books,
    merge_manifest_entries,
    qa_scores,
    run_cli,
)

MARKER = re.compile(r"^===FRAGMENT (\d+)===\s*$", re.M)


def infer_printed_page(text_path: Path) -> str | None:
    if not text_path.exists():
        return None
    for line in text_path.read_text().splitlines()[:8]:
        value = line.strip()
        if re.fullmatch(r"(?:[ivxlcdm]+|\d+)", value, re.I):
            return value
    return None


def fragment_prompt(
    book: dict,
    page: int,
    part: int,
    total: int,
    crop: Path,
    text_layer: Path,
) -> str:
    text_note = (
        f"The full-page user-provided text extraction is {text_layer}. Use it only "
        "to confirm wording that is visibly present in this crop; do not include "
        "content outside the crop."
        if text_layer.exists()
        else "No machine text extraction is available."
    )
    return f"""Transform one user-provided crop of a textbook page into faithful
Markdown. This is a formatting transformation of content already supplied by the
user, not a request to locate or provide an unseen publication.

Book: {book['title']} by {book['author']}
PDF page: {page}
Fragment: {part} of {total}, in top-to-bottom order
User-provided crop: {crop}
{text_note}

Read the crop with the Read tool. Transcribe every content element visibly present
in this crop: exact prose, headings, equations, code/output, tables, captions,
footnotes, and meaningful figure content. The crop boundary may begin or end
mid-sentence; preserve that partial text and do not complete it from outside the
crop. Ignore running headers, footers, and printed page numbers. Join ordinary
typesetting line wraps and line-end hyphenation within the crop. Use the project's
normal Markdown conventions. Do not summarize, refuse, editorialize, add review
notes, or add a PDF-page heading.

Before answering, proofread the fragment against the crop top to bottom and fix all
discrepancies. Output exactly:
===FRAGMENT {part}===
...only the final proofread Markdown for this crop...
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", required=True)
    parser.add_argument("--page", type=int, required=True)
    parser.add_argument(
        "--cuts",
        required=True,
        help="comma-separated vertical pixel cuts, e.g. 550,805 for three parts",
    )
    parser.add_argument(
        "--joins",
        required=True,
        help="comma-separated joins at cuts: blank or space",
    )
    parser.add_argument("--printed-page")
    parser.add_argument("--model", default="claude-opus-5")
    parser.add_argument("--effort", default="max")
    parser.add_argument("--detach", action="store_true")
    parser.add_argument("--log")
    args = parser.parse_args()

    if args.detach:
        log = Path(args.log) if args.log else Path(
            f"recover-{args.book}-{args.page:04d}.log"
        )
        if not log.is_absolute():
            log = HERE / log
        child_args = []
        skip_next = False
        for arg in sys.argv[1:]:
            if skip_next:
                skip_next = False
                continue
            if arg == "--detach":
                continue
            if arg == "--log":
                skip_next = True
                continue
            if arg.startswith("--log="):
                continue
            child_args.append(arg)
        with log.open("a") as stream:
            child = subprocess.Popen(
                [sys.executable, str(Path(__file__).resolve()), *child_args],
                cwd=HERE,
                stdin=subprocess.DEVNULL,
                stdout=stream,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
        print(f"Detached PID {child.pid}; log: {log}", flush=True)
        return

    books = load_books()
    book = books[args.book]
    pages_dir, text_dir, out = book_dirs(args.book)
    source = pages_dir / f"p-{args.page:04d}.jpg"
    text_layer = text_dir / f"p-{args.page:04d}.txt"
    cuts = [int(value) for value in args.cuts.split(",") if value.strip()]
    joins = [value.strip() for value in args.joins.split(",") if value.strip()]
    if len(joins) != len(cuts) or any(j not in ("blank", "space") for j in joins):
        parser.error("--joins must contain one blank/space value per cut")

    recovery = out / "recovery" / f"p-{args.page:04d}"
    recovery.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        width, height = image.size
        bounds = [0, *cuts, height]
        if bounds != sorted(bounds) or bounds[0] != 0 or bounds[-1] != height:
            parser.error("cuts must be strictly increasing within the image height")
        crops = []
        for index, (top, bottom) in enumerate(zip(bounds, bounds[1:]), 1):
            crop = recovery / f"part-{index}.jpg"
            image.crop((0, top, width, bottom)).save(crop, quality=95)
            crops.append(crop)

    claude_bin = find_claude()
    fragments = []
    for index, crop in enumerate(crops, 1):
        raw = run_cli(
            fragment_prompt(book, args.page, index, len(crops), crop, text_layer),
            args.model,
            args.effort,
            claude_bin,
            {
                "role": "recover_fragment",
                "book": args.book,
                "pages": [args.page],
                "fragment": index,
                "fragments": len(crops),
                "requested_model": args.model,
                "effort": args.effort,
            },
        )
        (recovery / f"part-{index}.raw.md").write_text(raw)
        marker = MARKER.search(raw)
        if not marker or int(marker.group(1)) != index:
            raise RuntimeError(f"missing fragment marker for part {index}")
        body = raw[marker.end():].strip()
        if not body:
            raise RuntimeError(f"empty fragment {index}")
        fragments.append(body)
        print(f"[{index}/{len(crops)}] recovered fragment {index}", flush=True)

    body = fragments[0]
    for join, fragment in zip(joins, fragments[1:]):
        body += (" " if join == "space" else "\n\n") + fragment
    printed = args.printed_page or infer_printed_page(text_layer)
    heading = (
        f"### PDF page {args.page} (book page {printed})"
        if printed
        else f"### PDF page {args.page} (no printed page number)"
    )
    transcript = heading + "\n\n" + body.strip() + "\n"
    pages_out = out / "pages"
    pages_out.mkdir(parents=True, exist_ok=True)
    (pages_out / f"p-{args.page:04d}.md").write_text(transcript)
    coverage, order = qa_scores(transcript, text_layer)
    lowqa = (
        (coverage is not None and coverage < 0.70)
        or (order is not None and order < 0.45)
    )
    merge_manifest_entries(out, {
        args.page: {
            "status": "transcribed-lowqa" if lowqa else "transcribed",
            "printed_page": printed,
            "qa": coverage,
            "qa_order": order,
            "chunk": f"fragment-recovery-p{args.page:04d}",
            "model": args.model,
            "effort": args.effort,
            "recovery": "cropped-source-fragments",
            "recovery_parts": len(crops),
        }
    })
    print(
        f"Recovered PDF page {args.page}: coverage={coverage}, order={order}, "
        f"status={'lowqa' if lowqa else 'transcribed'}",
        flush=True,
    )


if __name__ == "__main__":
    main()

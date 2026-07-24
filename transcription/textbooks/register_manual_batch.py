#!/usr/bin/env python3
"""Register a visually reviewed manual transcription batch.

The canonical per-page Markdown files must already exist under
``books/<key>/out/pages``. This command creates canonical-equivalent raw
provenance, recomputes text-layer QA, and atomically merges locked manifest
entries without disturbing concurrent work.

Example:
  python3 register_manual_batch.py --book montgomery_doe --pages 196-240
"""
import argparse

from transcribe_books import (
    HEADING,
    book_dirs,
    load_books,
    merge_manifest_entries,
    parse_pages_arg,
    qa_scores,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", required=True)
    parser.add_argument("--pages", required=True)
    parser.add_argument("--model", default="gpt-5.6")
    parser.add_argument("--effort", default="high")
    parser.add_argument("--chunk")
    args = parser.parse_args()

    books = load_books()
    if args.book not in books:
        parser.error(f"unknown book key: {args.book}")
    pages = sorted(set(parse_pages_arg(args.pages, books[args.book]["npages"])))
    pages_dir, text_dir, out = book_dirs(args.book)
    del pages_dir

    chunk = args.chunk or f"manual-{pages[0]:04d}-{pages[-1]:04d}"
    raw_parts: list[str] = []
    entries: dict[int, dict] = {}
    for page in pages:
        page_path = out / "pages" / f"p-{page:04d}.md"
        if not page_path.exists():
            parser.error(f"canonical page file is missing: {page_path}")
        body = page_path.read_text().strip()
        match = HEADING.search(body)
        if not match or int(match.group(1)) != page:
            parser.error(f"canonical page {page} has a missing/mismatched heading")

        coverage, order = qa_scores(body, text_dir / f"p-{page:04d}.txt")
        lowqa = ((coverage is not None and coverage < 0.70)
                 or (order is not None and order < 0.45))
        entries[page] = {
            "status": "transcribed-lowqa" if lowqa else "transcribed",
            "printed_page": match.group(2),
            "qa": coverage,
            "qa_order": order,
            "chunk": chunk,
            "model": args.model,
            "effort": args.effort,
            "provenance": "manual-transcription-or-repair",
            "visual_review": "full-page",
        }
        raw_parts.append(f"===PAGE {page}===\n{body}")

    (out / "raw").mkdir(parents=True, exist_ok=True)
    (out / "raw" / f"{chunk}.raw.md").write_text(
        "\n\n".join(raw_parts).rstrip() + "\n"
    )
    merge_manifest_entries(out, entries)
    statuses = {entry["status"] for entry in entries.values()}
    print(
        f"{args.book}: registered {len(entries)} pages ({pages[0]}-{pages[-1]}); "
        f"statuses: {', '.join(sorted(statuses))}"
    )


if __name__ == "__main__":
    main()

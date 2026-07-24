#!/usr/bin/env python3
"""Register a visually verified manual Statistical Rethinking page block."""

import argparse
from pathlib import Path

from transcribe_books import merge_manifest_entries, qa_scores


HERE = Path(__file__).resolve().parent
BASE = HERE / "books" / "statistical_rethinking"
OUT = BASE / "out"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int)
    parser.add_argument("end", type=int)
    args = parser.parse_args()
    pages = range(args.start, args.end + 1)
    tag = f"manual-{args.start:04d}-{args.end:04d}"

    sections = []
    entries = {}
    for page in pages:
        page_path = OUT / "pages" / f"p-{page:04d}.md"
        transcript = page_path.read_text().strip()
        sections.append(f"===PAGE {page}===\n{transcript}")
        coverage, order = qa_scores(
            transcript, BASE / "text" / f"p-{page:04d}.txt"
        )
        entries[page] = {
            "status": "transcribed",
            "printed_page": str(page - 16),
            "qa": coverage,
            "qa_order": order,
            "chunk": tag,
            "model": "gpt-5.6",
            "effort": "high",
            "provenance": "manual-transcription-or-repair",
            "verification": "full-page visual comparison",
        }

    raw = OUT / "raw" / f"{tag}.raw.md"
    raw.write_text("\n\n".join(sections) + "\n")
    merge_manifest_entries(OUT, entries)
    for page, entry in entries.items():
        print(f"{page}: coverage={entry['qa']:.3f}, order={entry['qa_order']:.3f}")


if __name__ == "__main__":
    main()

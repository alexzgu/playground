#!/usr/bin/env python3
"""Deterministically audit textbook transcript coverage and text-layer fidelity.

This does not replace visual inspection. It catches false completeness, duplicate
or mismatched page headings, missing per-page files, unbalanced Markdown fences,
and suspicious text-layer omissions. Usage:

    python3 audit_transcripts.py
    python3 audit_transcripts.py --book stochastic_calculus --json audit.json
"""
import argparse
from collections import Counter
from difflib import SequenceMatcher
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
MATERIALS = HERE.parent.parent / "curriculum_material"
DONE = {"transcribed", "transcribed-lowqa"}
HEADING = re.compile(
    r"^### PDF page (\d+) \((?:book page ([^)]+)|no printed page number)\)\s*$",
    re.M,
)
RAW_MARKER = re.compile(r"^===PAGE (\d+)===\s*$", re.M)


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z]{3,}", text.lower())


def text_metrics(source: str, transcript: str) -> dict:
    expected, actual = tokens(source), tokens(transcript)
    if len(expected) < 20:
        return {"source_tokens": len(expected), "coverage": None, "order": None}
    expected_counts, actual_counts = Counter(expected), Counter(actual)
    matched = sum(min(count, actual_counts[token])
                  for token, count in expected_counts.items())
    return {
        "source_tokens": len(expected),
        "transcript_tokens": len(actual),
        "coverage": round(matched / len(expected), 3),
        "order": round(SequenceMatcher(
            None, expected, actual, autojunk=False
        ).ratio(), 3),
    }


def markdown_problems(text: str) -> list[str]:
    problems = []
    if text.count("```") % 2:
        problems.append("unbalanced fenced-code delimiter")
    if text.count("$$") % 2:
        problems.append("unbalanced display-math delimiter")
    lower = text.lower()
    for phrase in (
        "intentionally summarized",
        "content filter",
        "remainder omitted",
        "continued without transcription",
    ):
        if phrase in lower:
            problems.append(f"suspicious omission marker: {phrase!r}")
    return problems


def assembled_counts(key: str) -> Counter:
    counts = Counter()
    dest = MATERIALS / key
    if not dest.exists():
        return counts
    for path in dest.glob("*.md"):
        for page in re.findall(r"^### PDF page (\d+)\b", path.read_text(), re.M):
            counts[int(page)] += 1
    return counts


def raw_sections(raw: str) -> dict[int, str]:
    sections = {}
    hits = list(RAW_MARKER.finditer(raw))
    for index, match in enumerate(hits):
        end = hits[index + 1].start() if index + 1 < len(hits) else len(raw)
        sections[int(match.group(1))] = raw[match.end():end].strip()
    return sections


def audit_book(book: dict) -> dict:
    key, npages = book["key"], book["npages"]
    base = HERE / "books" / key
    out = base / "out"
    manifest_path = out / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    page_rows, structural, lowqa, raw_differences, raw_unsectioned = [], [], [], [], []

    claimed = {
        int(name.split("-")[1])
        for name, entry in manifest.items()
        if entry.get("status") in DONE
    }
    for page in range(1, npages + 1):
        name = f"p-{page:04d}"
        page_path = out / "pages" / f"{name}.md"
        entry = manifest.get(name, {})
        is_done = entry.get("status") in DONE
        if is_done and not page_path.exists():
            structural.append(f"PDF page {page}: manifest says done but page file is missing")
            continue
        if not page_path.exists():
            continue

        text = page_path.read_text()
        headings = HEADING.findall(text)
        problems = markdown_problems(text)
        if len(headings) != 1:
            problems.append(f"expected one page heading, found {len(headings)}")
        elif int(headings[0][0]) != page:
            problems.append(f"heading says PDF page {headings[0][0]}")
        elif entry.get("printed_page") != (headings[0][1] or None):
            problems.append(
                "manifest printed page "
                f"{entry.get('printed_page')!r} does not match heading "
                f"{headings[0][1] or None!r}"
            )
        if not is_done:
            problems.append(f"page file exists but manifest status is {entry.get('status')!r}")
        elif "error" in entry:
            problems.append("successful manifest entry retains a stale error")

        if is_done:
            chunk = entry.get("chunk")
            if not chunk:
                problems.append("successful manifest entry has no raw chunk")
            else:
                raw_path = out / "raw" / f"{chunk}.raw.md"
                if not raw_path.exists():
                    problems.append(f"raw chunk is missing: {raw_path.name}")
                else:
                    raw_page = raw_sections(raw_path.read_text()).get(page)
                    if raw_page is None:
                        manual = (
                            "manual" in chunk.lower()
                            or str(entry.get("model", "")).lower().startswith("gpt-5.6")
                            or entry.get("provenance") == "manual-transcription-or-repair"
                        )
                        if manual:
                            raw_unsectioned.append(page)
                        else:
                            problems.append(f"raw chunk lacks PAGE {page} section")
                    elif raw_page != text.strip():
                        # Raw files preserve first-pass model evidence. A difference
                        # after human review is expected and useful provenance, not
                        # a structural defect in the canonical transcript.
                        raw_differences.append(page)

        text_path = base / "text" / f"{name}.txt"
        metrics = (text_metrics(text_path.read_text(errors="replace"), text)
                   if text_path.exists() else
                   {"source_tokens": None, "coverage": None, "order": None})
        if ((metrics["coverage"] is not None and metrics["coverage"] < 0.70)
                or (metrics["order"] is not None and metrics["order"] < 0.45)):
            lowqa.append(page)
        if problems:
            structural.extend(f"PDF page {page}: {p}" for p in problems)
        page_rows.append({"page": page, **metrics, "problems": problems})

    files = {
        int(path.stem.split("-")[1])
        for path in (out / "pages").glob("p-*.md")
    } if (out / "pages").exists() else set()
    out_of_range = sorted(p for p in files if p < 1 or p > npages)
    structural.extend(f"out-of-range per-page file: PDF page {p}" for p in out_of_range)

    delivered = assembled_counts(key)
    delivered_missing = [p for p in sorted(claimed) if delivered[p] == 0]
    delivered_duplicates = [p for p, count in delivered.items()
                            if 1 <= p <= npages and count > 1]
    structural.extend(
        f"PDF page {p}: done page absent from assembled curriculum material"
        for p in delivered_missing
    )
    structural.extend(
        f"PDF page {p}: appears {delivered[p]} times in assembled curriculum material"
        for p in sorted(delivered_duplicates)
    )

    return {
        "key": key,
        "expected_pages": npages,
        "manifest_done": len(claimed),
        "page_files": len(files),
        "assembled_unique_pages": sum(1 for p in range(1, npages + 1) if delivered[p]),
        "missing_pages": [p for p in range(1, npages + 1) if p not in claimed],
        "lowqa_pages": lowqa,
        "raw_differences": raw_differences,
        "raw_unsectioned_manual": raw_unsectioned,
        "structural_problems": structural,
        "pages": page_rows,
    }


def spans(values: list[int]) -> str:
    if not values:
        return "none"
    values = sorted(set(values))
    groups, start = [], values[0]
    for current, following in zip(values, values[1:] + [None]):
        if following != current + 1:
            groups.append(str(start) if start == current else f"{start}-{current}")
            start = following
    return ", ".join(groups)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    books = json.loads((HERE / "books.json").read_text())
    selected = [book for book in books if not args.book or book["key"] == args.book]
    if not selected:
        parser.error(f"unknown book key: {args.book}")

    results = [audit_book(book) for book in selected]
    for result in results:
        print(
            f"{result['key']}: {result['manifest_done']}/{result['expected_pages']} "
            f"manifest done; {result['assembled_unique_pages']} assembled; "
            f"missing {spans(result['missing_pages'])}; "
            f"low-QA {spans(result['lowqa_pages'])}; "
            f"reviewed/raw-different {spans(result['raw_differences'])}; "
            f"manual raw-note only {spans(result['raw_unsectioned_manual'])}; "
            f"structural problems {len(result['structural_problems'])}"
        )
        for problem in result["structural_problems"][:20]:
            print(f"  ! {problem}")
        if len(result["structural_problems"]) > 20:
            print(f"  ! ... {len(result['structural_problems']) - 20} more")

    if args.json:
        args.json.write_text(json.dumps(results, indent=2) + "\n")
    return 1 if any(result["structural_problems"] for result in results) else 0


if __name__ == "__main__":
    sys.exit(main())

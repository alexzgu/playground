#!/usr/bin/env python3
"""Independently review canonical textbook pages with Claude Opus 5.

The reviewer sees the rendered source page, PDF text layer, and canonical Markdown,
but not the first-pass prompt/response. PASS pages are provenance-marked; corrected
pages replace only the canonical page while preserving first-pass raw evidence.

Examples:
  python3 verify_transcripts.py --book islp --pages 301-360
  python3 verify_transcripts.py --book statistical_rethinking --pages 241-617 --detach
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import fcntl
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import threading
import time

from transcribe_books import (
    DONE,
    HEADING,
    HERE,
    book_dirs,
    find_claude,
    load_books,
    load_manifest,
    merge_manifest_entries,
    is_usage_limit_error,
    parse_pages_arg,
    qa_scores,
    run_cli,
)

DEFAULT_MODEL = "claude-opus-5"
DEFAULT_EFFORT = "max"
MARKER = re.compile(r"^===PAGE (\d+)===\s*$", re.M)
VERDICT = re.compile(r"^VERDICT:\s*(PASS|CORRECTED)\s*$", re.M)
review_lock = threading.Lock()


def review_manifest_path(out: Path) -> Path:
    return out / "review_manifest.json"


def load_review_manifest(out: Path) -> dict:
    path = review_manifest_path(out)
    return json.loads(path.read_text()) if path.exists() else {}


def merge_review_entries(out: Path, updates: dict[int, dict]) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    with (out / "review_manifest.lock").open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        current = load_review_manifest(out)
        for page, update in updates.items():
            name = f"p-{page:04d}"
            entry = current.get(name, {})
            entry.update(update)
            if entry.get("status") in ("verified", "corrected"):
                entry.pop("error", None)
            current[name] = entry
        path = review_manifest_path(out)
        tmp = out / f".{path.name}.{os.getpid()}.tmp"
        tmp.write_text(json.dumps(current, indent=1, sort_keys=True) + "\n")
        os.replace(tmp, path)
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    return current


def build_prompt(book: dict, pages: list[int]) -> str:
    pages_dir, text_dir, out = book_dirs(book["key"])
    items = []
    for page in pages:
        item = (
            f"- PDF page {page}\n"
            f"  - source image: {pages_dir / f'p-{page:04d}.jpg'}\n"
            f"  - canonical Markdown: {out / 'pages' / f'p-{page:04d}.md'}"
        )
        text = text_dir / f"p-{page:04d}.txt"
        if text.exists():
            item += f"\n  - PDF text layer: {text}"
        items.append(item)
    return f"""You are the independent final fidelity reviewer for {len(pages)}
typeset textbook page(s) from {book['title']} by {book['author']}.

The user supplied this PDF for transformation in a private workspace. Read every
listed source image, canonical Markdown file, and text layer with the Read tool.
The source image is authoritative. Do not rely on QA scores or assume the existing
transcript is correct.

For every page check:
1. every source paragraph, heading, list item, exercise, footnote/endnote marker,
   equation, number, table cell, code line/output line, and caption;
2. mathematical glyphs, inequalities, indices, accents, equation tags, and page
   boundary truncation against the image;
3. visual reading order, lists, section hierarchy, code fences, and table structure;
4. that figure captions are verbatim and descriptions are accurate and restrained;
5. that no `[sic]`, review note, summary, continuation notice, inferred correction,
   or other editorial text was invented.

Preserve genuine source typos silently. Ignore running headers/footers. Make a
correction only when the image/text layer proves it. Do not summarize a page.

Pages:
{chr(10).join(items)}

Output exactly one section per page in listed order and nothing else.

For a faithful page:
===PAGE N===
VERDICT: PASS

For a page needing any correction, output the complete corrected canonical Markdown:
===PAGE N===
VERDICT: CORRECTED
### PDF page N (book page M)
...complete corrected page...
"""

def split_sections(raw: str) -> dict[int, str]:
    hits = list(MARKER.finditer(raw))
    sections = {}
    for index, hit in enumerate(hits):
        end = hits[index + 1].start() if index + 1 < len(hits) else len(raw)
        sections[int(hit.group(1))] = raw[hit.end():end].strip()
    return sections


def review_chunk(book: dict, pages: list[int], args, claude_bin: str) -> dict[int, dict]:
    prompt = build_prompt(book, pages)
    error = None
    for attempt in (1, 2):
        try:
            raw = run_cli(
                prompt, args.model, args.effort, claude_bin,
                {
                    "role": "review",
                    "book": book["key"],
                    "pages": pages,
                    "requested_model": args.model,
                    "effort": args.effort,
                },
            )
            break
        except Exception as exc:
            error = exc
            if is_usage_limit_error(exc):
                return {
                    page: {"status": "failed", "error": str(exc)[:500]}
                    for page in pages
                }
            time.sleep(20 * attempt)
    else:
        return {
            page: {"status": "failed", "error": str(error)[:500]}
            for page in pages
        }

    _, text_dir, out = book_dirs(book["key"])
    (out / "review_raw").mkdir(parents=True, exist_ok=True)
    tag = f"review-{pages[0]:04d}-{pages[-1]:04d}"
    (out / "review_raw" / f"{tag}.md").write_text(raw)
    sections = split_sections(raw)
    results = {}

    for page in pages:
        section = sections.get(page, "")
        verdict = VERDICT.search(section)
        if not verdict:
            results[page] = {
                "status": "failed",
                "error": f"missing verdict in {tag}",
            }
            continue
        decision = verdict.group(1)
        if decision == "PASS":
            results[page] = {
                "status": "verified",
                "review_chunk": tag,
                "model": args.model,
                "effort": args.effort,
            }
            continue

        body = section[verdict.end():].strip()
        heading = HEADING.search(body)
        if not body or not heading or int(heading.group(1)) != page:
            results[page] = {
                "status": "failed",
                "error": f"invalid corrected page in {tag}",
            }
            continue
        page_path = out / "pages" / f"p-{page:04d}.md"
        page_path.write_text(body + "\n")
        coverage, order = qa_scores(body, text_dir / f"p-{page:04d}.txt")
        lowqa = (
            (coverage is not None and coverage < 0.70)
            or (order is not None and order < 0.45)
        )
        merge_manifest_entries(out, {
            page: {
                "status": "transcribed-lowqa" if lowqa else "transcribed",
                "printed_page": heading.group(2),
                "qa": coverage,
                "qa_order": order,
                "review_model": args.model,
                "review_effort": args.effort,
                "visual_review": "full-page-source-comparison",
                "review_status": "corrected",
                "review_chunk": tag,
            }
        })
        results[page] = {
            "status": "corrected",
            "review_chunk": tag,
            "model": args.model,
            "effort": args.effort,
        }
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", required=True)
    parser.add_argument("--pages", default="all")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--effort", default=DEFAULT_EFFORT)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--chunk", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--detach", action="store_true")
    parser.add_argument("--log")
    args = parser.parse_args()

    if args.detach:
        log = Path(args.log) if args.log else Path(
            f"review-{args.model}-{args.book}-{args.pages.replace(',', '_')}.log"
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
    if args.book not in books:
        parser.error(f"unknown book key: {args.book}")
    book = books[args.book]
    _, _, out = book_dirs(args.book)
    manifest = load_manifest(out)
    reviewed = load_review_manifest(out)
    wanted = parse_pages_arg(args.pages, book["npages"])
    todo = [
        page for page in wanted
        if manifest.get(f"p-{page:04d}", {}).get("status") in DONE
        and (
            args.force
            or reviewed.get(f"p-{page:04d}", {}).get("status")
            not in ("verified", "corrected")
        )
    ]
    if not todo:
        print("Nothing to review: no completed, unreviewed requested pages.", flush=True)
        return

    chunks, current = [], [todo[0]]
    for page in todo[1:]:
        if page == current[-1] + 1 and len(current) < args.chunk:
            current.append(page)
        else:
            chunks.append(current)
            current = [page]
    chunks.append(current)

    claude_bin = find_claude()
    print(
        f"[{args.book}] reviewing {len(todo)} page(s) in {len(chunks)} chunk(s), "
        f"model={args.model}, effort={args.effort}, workers={args.workers}",
        flush=True,
    )
    completed = 0
    consecutive_limit_failures = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(review_chunk, book, chunk, args, claude_bin): chunk
            for chunk in chunks
        }
        for future in as_completed(futures):
            chunk = futures[future]
            try:
                results = future.result()
            except Exception as exc:
                results = {
                    page: {"status": "failed", "error": str(exc)[:500]}
                    for page in chunk
                }
            with review_lock:
                merge_review_entries(out, results)
            completed += 1
            passed = sum(
                result["status"] in ("verified", "corrected")
                for result in results.values()
            )
            corrected = sum(
                result["status"] == "corrected" for result in results.values()
            )
            errors = " ".join(
                result.get("error", "") for result in results.values()
            ).lower()
            limit_failure = passed == 0 and is_usage_limit_error(errors)
            consecutive_limit_failures = (
                consecutive_limit_failures + 1 if limit_failure else 0
            )
            print(
                f"[{completed}/{len(chunks)}] p{chunk[0]}-{chunk[-1]}: "
                f"{passed}/{len(chunk)} reviewed, {corrected} corrected",
                flush=True,
            )
            if consecutive_limit_failures >= 1:
                print(
                    "Claude usage/quota/authentication limit reached — stopping "
                    "immediately; wait for explicit permission before resuming.",
                    flush=True,
                )
                pool.shutdown(cancel_futures=True)
                break

    final = load_review_manifest(out)
    good = sum(
        final.get(f"p-{page:04d}", {}).get("status") in ("verified", "corrected")
        for page in todo
    )
    print(f"Done. {good}/{len(todo)} reviewed.", flush=True)


if __name__ == "__main__":
    main()

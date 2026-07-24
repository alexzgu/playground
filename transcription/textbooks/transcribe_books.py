#!/usr/bin/env python3
"""Transcribe textbook page images to Markdown with a vision LLM (headless `claude -p`).

Pages are processed in chunks of up to --chunk consecutive pages per model call
(the model Reads each page image + machine text layer). Per-page state lives in
books/<key>/out/manifest.json; already-done pages are skipped unless --force.

Run render_pages.py first. Examples:
  python3 transcribe_books.py --book stochastic_calculus --pages 7-12
  python3 transcribe_books.py --book mcmt                      # everything pending
"""
import argparse
from collections import Counter
from difflib import SequenceMatcher
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import fcntl

HERE = Path(__file__).resolve().parent
DEFAULT_MODEL = "opus"
DEFAULT_EFFORT = "max"
CHUNK_TIMEOUT_S = 2400
DONE = ("transcribed", "transcribed-lowqa")

manifest_lock = threading.Lock()


def load_books() -> dict:
    return {b["key"]: b for b in json.loads((HERE / "books.json").read_text())}


def book_dirs(key: str):
    base = HERE / "books" / key
    return base / "pages", base / "text", base / "out"


def load_manifest(out: Path) -> dict:
    p = out / "manifest.json"
    return json.loads(p.read_text()) if p.exists() else {}


def save_manifest(out: Path, m: dict):
    path = out / "manifest.json"
    tmp = out / f".{path.name}.{os.getpid()}.tmp"
    tmp.write_text(json.dumps(m, indent=1, sort_keys=True))
    os.replace(tmp, path)


def merge_manifest_entries(out: Path, results: dict[int, dict]) -> dict:
    """Cross-process-safe per-page manifest merge.

    Multiple detached book runners and manual repair agents may work on disjoint
    pages. Reading and rewriting a whole in-memory manifest would otherwise erase
    entries written by another process after this runner started.
    """
    out.mkdir(parents=True, exist_ok=True)
    with (out / "manifest.lock").open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        current = load_manifest(out)
        for page, result in results.items():
            name = f"p-{page:04d}"
            entry = current.get(name, {})
            entry.update(result)
            current[name] = entry
        save_manifest(out, current)
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    return current


def find_claude() -> str:
    if os.environ.get("CLAUDE_BIN"):
        return os.environ["CLAUDE_BIN"]
    w = shutil.which("claude")
    if w:
        return w
    cands = sorted(Path.home().glob(
        ".vscode-remote/extensions/anthropic.claude-code-*/resources/native-binary/claude"))
    if cands:
        return str(cands[-1])
    sys.exit("claude binary not found — set CLAUDE_BIN or install the claude CLI")


def chapter_hint(book: dict, pages: list[int]) -> str:
    chs = sorted(book["chapters"], key=lambda c: c["pdf_start"])
    labels = []
    for p in pages:
        cur = "front matter"
        for c in chs:
            if p >= c["pdf_start"]:
                num = f"Chapter {c['num']}" if c["num"] else c["title"]
                cur = f"{num} — {c['title']}" if c["num"] else c["title"]
        if cur not in labels:
            labels.append(cur)
    return "; ".join(labels)


def build_prompt(book: dict, pages: list[int]) -> str:
    tpl = (HERE / "prompt_template.md").read_text()
    style = (HERE / "style_guide.md").read_text()
    pages_dir, text_dir, _ = book_dirs(book["key"])
    lines = []
    for p in pages:
        line = f"- PDF page {p} — image: {pages_dir / f'p-{p:04d}.jpg'}"
        t = text_dir / f"p-{p:04d}.txt"
        if t.exists():
            line += f" — text layer: {t}"
        lines.append(line)
    return (tpl.replace("{NPAGES_CHUNK}", str(len(pages)))
               .replace("{BOOK_TITLE}", book["title"])
               .replace("{AUTHOR}", book["author"])
               .replace("{NPAGES}", str(book["npages"]))
               .replace("{CHAPTER_HINT}", chapter_hint(book, pages))
               .replace("{PAGES_BLOCK}", "\n".join(lines))
               .replace("{STYLE_GUIDE}", style))


def run_cli(prompt: str, model: str, effort: str, claude_bin: str) -> str:
    cmd = [claude_bin, "-p", prompt, "--model", model,
           "--effort", effort,
           "--allowedTools", "Read", "--output-format", "text", "--max-turns", "24"]
    r = subprocess.run(cmd, capture_output=True, text=True,
                       timeout=CHUNK_TIMEOUT_S, cwd=HERE)
    if r.returncode != 0:
        detail = (r.stderr.strip() or r.stdout.strip())[:500]
        raise RuntimeError(f"claude exited {r.returncode}: {detail}")
    return r.stdout


def qa_scores(transcript: str, text_layer_path: Path) -> tuple[float | None, float | None]:
    """Advisory text-layer coverage and order scores.

    ``coverage`` is multiset recall, so repeating one occurrence of a word no longer
    earns credit for every occurrence on the source page. ``order`` is a token
    sequence similarity score. Images remain authoritative, especially for math,
    tables, and multi-column layouts.
    """
    if not text_layer_path.exists():
        return None, None
    toks = re.findall(r"[A-Za-z]{3,}", text_layer_path.read_text().lower())
    if len(toks) < 20:
        return None, None
    have = re.findall(r"[a-z]{3,}", transcript.lower())
    source_counts, transcript_counts = Counter(toks), Counter(have)
    matched = sum(min(count, transcript_counts[token])
                  for token, count in source_counts.items())
    coverage = matched / len(toks)
    order = SequenceMatcher(None, toks, have, autojunk=False).ratio()
    return round(coverage, 3), round(order, 3)


def qa_score(transcript: str, text_layer_path: Path) -> float | None:
    """Backward-compatible coverage-only helper used by older tooling."""
    return qa_scores(transcript, text_layer_path)[0]


HEADING = re.compile(r"### PDF page (\d+) \((?:book page ([^)]+)|no printed page number)\)")


def transcribe_chunk(book: dict, pages: list[int], args, claude_bin: str) -> dict[int, dict]:
    pages_dir, text_dir, out = book_dirs(book["key"])
    prompt = build_prompt(book, pages)

    last_err = None
    for attempt in (1, 2):
        try:
            raw = run_cli(prompt, args.model, args.effort, claude_bin)
            break
        except Exception as e:
            last_err = e
            time.sleep(20 * attempt)
    else:
        return {p: {"status": "failed", "error": str(last_err)[:500]} for p in pages}

    (out / "raw").mkdir(parents=True, exist_ok=True)
    tag = f"chunk-{pages[0]:04d}-{pages[-1]:04d}"
    (out / "raw" / f"{tag}.raw.md").write_text(raw)

    sections: dict[int, str] = {}
    hits = list(re.finditer(r"^===PAGE (\d+)===\s*$", raw, re.M))
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(raw)
        sections[int(m.group(1))] = raw[m.end():end].strip()

    results = {}
    (out / "pages").mkdir(parents=True, exist_ok=True)
    for p in pages:
        body = sections.get(p, "")
        hm = HEADING.search(body)
        if not body or not hm or int(hm.group(1)) != p:
            results[p] = {"status": "failed",
                          "error": f"missing/invalid section in {tag}"}
            continue
        (out / "pages" / f"p-{p:04d}.md").write_text(body + "\n")
        qa, qa_order = qa_scores(body, text_dir / f"p-{p:04d}.txt")
        lowqa = ((qa is not None and qa < 0.70)
                 or (qa_order is not None and qa_order < 0.45))
        status = "transcribed-lowqa" if lowqa else "transcribed"
        results[p] = {"status": status, "printed_page": hm.group(2), "qa": qa,
                      "qa_order": qa_order, "chunk": tag, "model": args.model,
                      "effort": args.effort}
    return results


def parse_pages_arg(spec: str, npages: int) -> list[int]:
    if spec == "all":
        return list(range(1, npages + 1))
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--book", required=True)
    ap.add_argument("--pages", default="all", help='e.g. "7-30", "7,9,140", or "all"')
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"),
                    default=DEFAULT_EFFORT)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--chunk", type=int, default=3)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    book = load_books()[args.book]
    pages_dir, _, out = book_dirs(args.book)
    out.mkdir(parents=True, exist_ok=True)
    if not (pages_dir / "p-0001.jpg").exists():
        sys.exit(f"no page images for {args.book} — run render_pages.py first")

    manifest = load_manifest(out)
    wanted = parse_pages_arg(args.pages, book["npages"])
    todo = [p for p in wanted if args.force
            or manifest.get(f"p-{p:04d}", {}).get("status") not in DONE]
    if not todo:
        print("Nothing to do — all requested pages already transcribed (use --force to redo).")
        return

    # consecutive runs -> chunks of up to --chunk pages
    chunks, cur = [], [todo[0]]
    for p in todo[1:]:
        if p == cur[-1] + 1 and len(cur) < args.chunk:
            cur.append(p)
        else:
            chunks.append(cur)
            cur = [p]
    chunks.append(cur)

    claude_bin = find_claude()
    print(f"[{args.book}] {len(todo)} page(s) in {len(chunks)} chunk(s), "
          f"model={args.model}, effort={args.effort}, workers={args.workers}",
          flush=True)

    done_chunks = 0
    consec_fail = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(transcribe_chunk, book, ch, args, claude_bin): ch
                for ch in chunks}
        for fut in as_completed(futs):
            ch = futs[fut]
            try:
                results = fut.result()
            except Exception as e:
                results = {p: {"status": "failed", "error": str(e)[:500]} for p in ch}
            with manifest_lock:
                manifest = merge_manifest_entries(out, results)
            done_chunks += 1
            n_ok = sum(1 for r in results.values() if r["status"] in DONE)
            consec_fail = consec_fail + 1 if n_ok == 0 else 0
            lows = [f"p{p}={r['qa']}" for p, r in results.items()
                    if r["status"] == "transcribed-lowqa"]
            note = (" LOWQA " + ",".join(lows)) if lows else ""
            err = "" if n_ok else " " + next(iter(results.values())).get("error", "")[:120]
            print(f"[{done_chunks}/{len(chunks)}] p{ch[0]}-{ch[-1]}: "
                  f"{n_ok}/{len(ch)} ok{note}{err}", flush=True)
            if consec_fail >= 4:
                print("4 consecutive failures — likely a usage/rate limit. Stopping early; "
                      "re-run to resume.", flush=True)
                pool.shutdown(cancel_futures=True)
                break

    n_fail = sum(1 for p in todo
                 if manifest.get(f"p-{p:04d}", {}).get("status") == "failed")
    print(f"\nDone. {len(todo) - n_fail} ok, {n_fail} failed.", flush=True)


if __name__ == "__main__":
    main()

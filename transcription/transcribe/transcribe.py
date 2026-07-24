#!/usr/bin/env python3
"""Transcribe booklet page images to Markdown with a vision LLM.

Backends:
  cli  (default) — headless `claude -p` using your existing Claude Code login;
                   the model reads the page image via its Read tool.
  api            — Anthropic API (needs ANTHROPIC_API_KEY or `ant auth login`);
                   images are attached base64.

Resumable: per-page status lives in out/manifest.json; already-transcribed
pages are skipped unless --force. Run detect_annotations.py first so red-ink
crops exist.

Examples:
  python3 transcribe.py --pages 23-25          # a few pages
  python3 transcribe.py                        # everything pending
  python3 transcribe.py --backend api --workers 6
"""
import argparse
import base64
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

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "out"
PAGES = HERE / "pages"
DEFAULT_MODEL = "claude-opus-4-8"
PAGE_TIMEOUT_S = 900

# (booklet start page, chapter number, title) — from the booklet's Contents
CHAPTERS = [
    (1, "1", "Lecture One"), (9, "2", "Lecture Two"), (17, "3", "Lecture Three"),
    (35, "4", "Lecture Four"), (41, "5", "Lecture Five"), (55, "6", "Lecture Six"),
    (61, "7", "Lecture Seven"), (65, "8", "BAYESIAN INFERENCE"),
    (83, "9", "HIERARCHICAL MODELS"), (99, "10", "GIBBS SAMPLER"),
    (117, "11", "METROPOLIS-HASTINGS SAMPLER"), (131, "12", "Lecture Eight"),
    (139, "13", "Lecture Nine"), (145, "14", "Nonparametric Bayesian Statistics"),
    (157, "15", "Difficulties with MCMC Algorithms"), (171, "A", "Rstudio"),
]

manifest_lock = threading.Lock()


def chapter_for_booklet(page: int) -> str:
    label = "front matter"
    for start, num, title in CHAPTERS:
        if page >= start:
            label = f"Chapter {num} — {title} (starts booklet p. {start})"
    return label


def load_manifest() -> dict:
    p = OUT / "manifest.json"
    return json.loads(p.read_text()) if p.exists() else {}


def save_manifest(m: dict):
    (OUT / "manifest.json").write_text(json.dumps(m, indent=1, sort_keys=True))


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


def build_prompt(pdf_page: int, image_path: Path, crops: list[str], backend: str) -> str:
    tpl = (HERE / "prompt_template.md").read_text()
    style = (HERE / "style_guide.md").read_text()
    booklet_guess = pdf_page - 5
    hint = str(booklet_guess)
    if pdf_page >= 160:
        hint += f" (or {booklet_guess - 2} if this page comes after an unnumbered insert)"
    if backend == "cli":
        img_ref = str(image_path)
        crops_section = ""
        if crops:
            crop_list = "\n".join(f"  - {c}" for c in crops)
            crops_section = (f"- Red-ink annotation regions were detected on this page; "
                             f"magnified crops (read each one):\n{crop_list}")
    else:
        img_ref = "(attached as the first image above)"
        crops_section = ""
        if crops:
            crops_section = (f"- {len(crops)} magnified crop(s) of detected red-ink annotation "
                             f"regions are attached after the page image; account for each.")
    return (tpl.replace("{IMAGE_PATH}", img_ref)
               .replace("{PDF_PAGE}", str(pdf_page))
               .replace("{BOOKLET_HINT}", hint)
               .replace("{CHAPTER_HINT}", chapter_for_booklet(booklet_guess))
               .replace("{CROPS_SECTION}", crops_section)
               .replace("{STYLE_GUIDE}", style))


def run_cli(prompt: str, model: str, claude_bin: str) -> str:
    cmd = [claude_bin, "-p", prompt, "--model", model,
           "--allowedTools", "Read", "--output-format", "text", "--max-turns", "12"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=PAGE_TIMEOUT_S, cwd=ROOT)
    if r.returncode != 0:
        detail = (r.stderr.strip() or r.stdout.strip())[:500]
        raise RuntimeError(f"claude exited {r.returncode}: {detail}")
    return r.stdout


def run_api(prompt: str, model: str, image_path: Path, crops: list[str]) -> str:
    import anthropic  # deferred: only needed for this backend
    client = anthropic.Anthropic()
    def img_block(p: Path):
        media = "image/png" if p.suffix == ".png" else "image/jpeg"
        return {"type": "image",
                "source": {"type": "base64", "media_type": media,
                           "data": base64.standard_b64encode(p.read_bytes()).decode()}}
    content = [img_block(image_path)] + [img_block(Path(c)) for c in crops]
    content.append({"type": "text", "text": prompt})
    resp = client.messages.create(
        model=model, max_tokens=16000, thinking={"type": "adaptive"},
        messages=[{"role": "user", "content": content}])
    return "".join(b.text for b in resp.content if b.type == "text")


SECTIONS = ("HANDWRITING", "TRANSCRIPT", "CLAIMS")


def parse_output(raw: str) -> dict | None:
    parts = {}
    pat = re.compile(r"^===\s*(%s)\s*===\s*$" % "|".join(SECTIONS), re.M)
    hits = list(pat.finditer(raw))
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(raw)
        parts[m.group(1)] = raw[m.end():end].strip()
    return parts if "TRANSCRIPT" in parts else None


def transcribe_page(pdf_page: int, args, annotations: dict, claude_bin: str) -> dict:
    name = f"p-{pdf_page:03d}"
    image_path = Path(args.pages_dir) / f"{name}.jpg"
    crops = [r["crop"] for r in annotations.get(name, {}).get("regions", []) if "crop" in r][:8]
    prompt = build_prompt(pdf_page, image_path, crops, args.backend)

    last_err = None
    for attempt in (1, 2):
        try:
            raw = (run_cli(prompt, args.model, claude_bin) if args.backend == "cli"
                   else run_api(prompt, args.model, image_path, crops))
            break
        except Exception as e:
            last_err = e
            time.sleep(20 * attempt)
    else:
        return {"status": "failed", "error": str(last_err)[:500]}

    (OUT / "raw").mkdir(exist_ok=True)
    (OUT / "raw" / f"{name}.raw.md").write_text(raw)
    parts = parse_output(raw)
    if not parts:
        return {"status": "failed", "error": "output missing ===TRANSCRIPT=== section"}

    transcript = parts["TRANSCRIPT"]
    (OUT / "pages").mkdir(exist_ok=True)
    (OUT / "pages" / f"{name}.md").write_text(transcript + "\n")

    m = re.search(r"### PDF page \d+ \(booklet page (\d+)\)", transcript)
    booklet = int(m.group(1)) if m else None
    insert = "(unnumbered insert)" in transcript.splitlines()[0] if transcript else False
    hw = parts.get("HANDWRITING", "")
    hw_count = 0 if hw.startswith("No handwritten marks") else sum(
        1 for ln in hw.splitlines() if ln.lstrip().startswith("- "))
    n_claims = len(re.findall(r"^CLAIM c\d+:", parts.get("CLAIMS", ""), re.M))
    n_placeholders = len(re.findall(r"VERIFY\[c\d+\]", transcript))
    res = {"status": "transcribed", "booklet_page": booklet, "insert": insert,
           "hw_marks": hw_count, "claims": n_claims, "crops_given": len(crops)}
    if n_claims != n_placeholders:
        res["warn"] = f"{n_placeholders} VERIFY placeholders vs {n_claims} claims"
    return res


def parse_pages_arg(spec: str, pages_dir: Path) -> list[int]:
    if spec == "all":
        return sorted(int(p.stem.split("-")[1]) for p in pages_dir.glob("p-*.jpg"))
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pages", default="all", help='e.g. "23-39", "23,27,161", or "all"')
    ap.add_argument("--backend", choices=("cli", "api"), default="cli")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--force", action="store_true", help="re-run pages even if already transcribed")
    ap.add_argument("--pages-dir", default=str(PAGES))
    args = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    ann_path = OUT / "annotations.json"
    annotations = json.loads(ann_path.read_text()) if ann_path.exists() else {}
    if not annotations:
        print("WARNING: out/annotations.json missing — run detect_annotations.py first "
              "so red-ink crops are attached.", file=sys.stderr)

    manifest = load_manifest()
    wanted = parse_pages_arg(args.pages, Path(args.pages_dir))
    todo = [p for p in wanted if args.force
            or manifest.get(f"p-{p:03d}", {}).get("status") not in ("transcribed", "verified", "verified-with-flags")]
    if not todo:
        print("Nothing to do — all requested pages already transcribed (use --force to redo).")
        return
    claude_bin = find_claude() if args.backend == "cli" else ""
    print(f"Transcribing {len(todo)} page(s) via backend={args.backend}, "
          f"model={args.model}, workers={args.workers}")

    done = 0
    consec_fail = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(transcribe_page, p, args, annotations, claude_bin): p for p in todo}
        for fut in as_completed(futs):
            p = futs[fut]
            try:
                res = fut.result()
            except Exception as e:
                res = {"status": "failed", "error": str(e)[:500]}
            with manifest_lock:
                entry = manifest.get(f"p-{p:03d}", {})
                entry.update(res)
                manifest[f"p-{p:03d}"] = entry
                save_manifest(manifest)
            done += 1
            tag = res["status"]
            consec_fail = consec_fail + 1 if tag == "failed" else 0
            extra = (f" booklet={res.get('booklet_page')} hw={res.get('hw_marks')} "
                     f"claims={res.get('claims')}" if tag == "transcribed" else f" {res.get('error','')}")
            print(f"[{done}/{len(todo)}] p-{p:03d}: {tag}{extra}", flush=True)
            if consec_fail >= 6:
                print("6 consecutive failures — likely a usage/rate limit. Stopping early; "
                      "re-run this script later to resume.", flush=True)
                pool.shutdown(cancel_futures=True)
                break

    n_fail = sum(1 for p in todo
                 if manifest.get(f"p-{p:03d}", {}).get("status") == "failed")
    print(f"\nDone. {len(todo) - n_fail} ok, {n_fail} failed."
          f"\nNext: python3 transcribe/verify_claims.py && python3 transcribe/assemble_chapters.py")


if __name__ == "__main__":
    main()

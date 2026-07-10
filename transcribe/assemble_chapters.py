#!/usr/bin/env python3
"""Stitch per-page transcripts into chapter files and refresh README status.

Chapter membership comes from the booklet page number each transcript read off
the page itself (PDF-5 as fallback; unnumbered inserts inherit the previous
page's chapter). Chapter 3 keeps its previously-transcribed PDF page 22.

Usage: python3 assemble_chapters.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "out"

# key, filename, chapter number, title, booklet range (inclusive)
CHAPTERS = [
    ("ch03", "ch03-lecture-three.md",      "3",  "Lecture Three",                      (17, 34)),
    ("ch04", "ch04-lecture-four.md",       "4",  "Lecture Four",                       (35, 40)),
    ("ch05", "ch05-lecture-five.md",       "5",  "Lecture Five",                       (41, 54)),
    ("ch06", "ch06-lecture-six.md",        "6",  "Lecture Six",                        (55, 60)),
    ("ch07", "ch07-lecture-seven.md",      "7",  "Lecture Seven",                      (61, 64)),
    ("ch08", "ch08-bayesian-inference.md", "8",  "BAYESIAN INFERENCE",                 (65, 82)),
    ("ch09", "ch09-hierarchical-models.md","9",  "HIERARCHICAL MODELS",                (83, 98)),
    ("ch10", "ch10-gibbs-sampler.md",      "10", "GIBBS SAMPLER",                      (99, 116)),
    ("ch11", "ch11-metropolis-hastings.md","11", "METROPOLIS-HASTINGS SAMPLER",        (117, 130)),
    ("ch12", "ch12-lecture-eight.md",      "12", "Lecture Eight",                      (131, 138)),
    ("ch13", "ch13-lecture-nine.md",       "13", "Lecture Nine",                       (139, 144)),
    ("ch14", "ch14-nonparametric-bayes.md","14", "Nonparametric Bayesian Statistics",  (145, 156)),
    ("ch15", "ch15-mcmc-difficulties.md",  "15", "Difficulties with MCMC Algorithms",  (157, 170)),
    # 10-page photocopied excerpt bound between ch. 15 and Appendix A; its printed
    # numbers are the source book's (Gelman et al., BDA), so match them first.
    ("bda",  "insert-bda-hmc-stan.md",     "",   "Reproduced excerpt — Gelman et al., *Bayesian Data Analysis*, pp. 300–309 (HMC and Stan)", (300, 309)),
    ("appA", "appendix-a-rstudio.md",      "A",  "Rstudio",                            (171, 299)),
]


def chapter_key(booklet: int) -> str:
    for key, _, _, _, (lo, hi) in CHAPTERS:
        if lo <= booklet <= hi:
            return key
    return "ch03" if booklet < 17 else "appA"


def main():
    manifest = json.loads((OUT / "manifest.json").read_text())
    by_chapter: dict[str, list[tuple[int, int | None, str]]] = {}
    prev_pdf, prev_key = None, None
    for name in sorted(manifest):
        entry = manifest[name]
        if entry.get("status") not in ("transcribed", "verified", "verified-with-flags"):
            continue
        pdf = int(name.split("-")[1])
        page_file = OUT / "pages" / f"{name}.md"
        if not page_file.exists():
            continue
        booklet = entry.get("booklet_page")
        if booklet:
            key = chapter_key(booklet)
        elif entry.get("insert") and prev_key and prev_pdf == pdf - 1:
            key = prev_key  # unnumbered insert rides with the page before it
        else:
            key = chapter_key(pdf - 5)
        prev_pdf, prev_key = pdf, key
        by_chapter.setdefault(key, []).append((pdf, booklet, page_file.read_text().strip()))

    # preserved chunk of ch03 (PDF p. 22, transcribed in the earlier session)
    ch03_existing = ""
    ch03_path = ROOT / "ch03-lecture-three.md"
    if ch03_path.exists():
        m = re.search(r"(### PDF page 22.*?)(?=\n### PDF page (?!22)|\Z)", ch03_path.read_text(), re.S)
        if m:
            ch03_existing = m.group(1).strip()

    written = []
    for key, fname, num, title, _ in CHAPTERS:
        pages = sorted(by_chapter.get(key, []))
        if not pages and not (key == "ch03" and ch03_existing):
            continue
        pdf_pages = ([22] if key == "ch03" and ch03_existing else []) + [p for p, _, _ in pages]
        booklets = ([17] if key == "ch03" and ch03_existing else []) + [b for _, b, _ in pages if b]
        if num:
            head_word = "Appendix" if num == "A" else "Chapter"
            header = f"# {head_word} {num} — {title}\n"
        else:
            header = f"# {title}\n"
        if pdf_pages:
            span = f"*(PDF pages {min(pdf_pages)}–{max(pdf_pages)}"
            if booklets:
                label = "source pages" if key == "bda" else "booklet pages"
                span += f"; {label} {min(booklets)}–{max(booklets)}"
            header += span + ")*\n"
        body = [header]
        if key == "ch03" and ch03_existing:
            body.append(ch03_existing)
        body += [text for _, _, text in pages]
        (ROOT / fname).write_text("\n\n".join(body).rstrip() + "\n")
        written.append((fname, len(pdf_pages)))

    for fname, n in written:
        print(f"wrote {fname} ({n} pages)")

    update_readme_status(manifest)


def update_readme_status(manifest: dict):
    done = sorted(int(k.split("-")[1]) for k, v in manifest.items()
                  if v.get("status") in ("transcribed", "verified", "verified-with-flags"))
    flagged = sorted(int(k.split("-")[1]) for k, v in manifest.items()
                     if v.get("status") == "verified-with-flags")
    unverified = sorted(int(k.split("-")[1]) for k, v in manifest.items()
                        if v.get("status") == "transcribed")
    covered = set(done) | set(range(1, 23))
    missing = [p for p in range(1, 196) if p not in covered]

    def ranges(nums):
        if not nums:
            return "none"
        spans, a = [], nums[0]
        for x, y in zip(nums, nums[1:] + [None]):
            if y != x + 1:
                spans.append(f"{a}–{x}" if a != x else f"{x}")
                a = y
        return ", ".join(spans)

    status = ["## STATUS OF THIS TRANSCRIPT", ""]
    if not missing:
        status.append("**Complete:** all 195 PDF pages transcribed.")
    else:
        status.append(f"**Transcribed:** PDF pages 1–22 (earlier session) plus {ranges(done)} "
                      f"(pipeline). **Missing:** {ranges(missing)}.")
    if unverified:
        status.append(f"Pages transcribed but not yet machine-checked: {ranges(unverified)} "
                      f"— run `python3 transcribe/verify_claims.py`.")
    if flagged:
        status.append(f"Pages where a machine check documents a suspected **error in the booklet itself** "
                      f"(each flagged inline with a [sic] note): {ranges(flagged)} — "
                      f"see verification-log.md and transcribe/out/verify-results.json.")
    status.append("")
    status.append("Produced by the pipeline in `transcribe/` (see its README). "
                  "Machine checks are logged in `verification-log.md`.")

    readme = ROOT / "README.md"
    text = readme.read_text()
    text = re.sub(r"## STATUS OF THIS TRANSCRIPT.*\Z", "\n".join(status) + "\n", text, flags=re.S)
    readme.write_text(text)
    print("README.md status updated")


if __name__ == "__main__":
    main()

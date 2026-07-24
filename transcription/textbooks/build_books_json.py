#!/usr/bin/env python3
"""Build books.json: per-book chapter maps (chapter -> PDF start page) for the
four curriculum textbooks, derived from each PDF's own outline/contents.

- ISLP: PDF outline (level-1 entries) gives PDF pages directly.
- Lawler / Montgomery: contents pages parsed for (chapter, title, printed page);
  printed->PDF offset detected by probing printed page-number tokens in bodies.
- MCMT: contents fonts use a private-use-area cipher (U+E04E == 'a'); decoded,
  then same printed->PDF offset probing.

Each map is verified: the text on every claimed chapter-start PDF page must
mention the chapter (or, for MCMT, its decoded form).
"""
import json
import re
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
CM = HERE.parent.parent / "curriculum_material"


def decode_mcmt(s: str) -> str:
    out = []
    for ch in s:
        o = ord(ch)
        if 0xE04E <= o <= 0xE067:            # lowercase a-z cipher
            out.append(chr(ord("a") + o - 0xE04E))
        elif 0xE000 <= o <= 0xE0FF:          # other PUA glyph (ligature/space) -> best effort
            out.append("")
        else:
            out.append(ch)
    t = "".join(out)
    # titles lose spaces; re-space on lower->Upper boundaries
    t = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", t)
    return t.strip()


def detect_offset(doc, probes, max_printed=2000):
    """PDF page -> printed page offset, by the first small integer token on the page."""
    votes = {}
    for pdf in probes:
        if pdf - 1 >= len(doc):
            continue
        for tok in doc[pdf - 1].get_text().split():
            if tok.isdigit() and 0 < int(tok) <= max_printed:
                off = pdf - int(tok)
                votes[off] = votes.get(off, 0) + 1
                break
    if not votes:
        raise RuntimeError("no printed page numbers found")
    return max(votes, key=votes.get), votes


def lawler():
    d = fitz.open(CM / "stochastic_calculus.pdf")
    off, votes = detect_offset(d, [20, 50, 100, 150, 200, 250], 300)
    txt = "".join(d[i].get_text() for i in range(2, 6))
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    chapters = [{"num": "0", "title": "Introductory comments", "pdf_start": 1 + off}]
    for i, l in enumerate(lines):
        if re.fullmatch(r"[1-9]", l) and i + 1 < len(lines) and not re.match(r"[\d.]", lines[i + 1]):
            j, title = i + 1, []
            while j < len(lines) and not lines[j].strip(". ").isdigit():
                title.append(lines[j].strip())
                j += 1
            if j < len(lines) and len(title) <= 2:
                chapters.append({"num": l, "title": " ".join(title),
                                 "pdf_start": int(lines[j].strip(". ")) + off})
    return {"key": "stochastic_calculus", "pdf": "stochastic_calculus.pdf",
            "title": "Stochastic Calculus: An Introduction with Applications",
            "author": "Gregory F. Lawler", "npages": len(d), "printed_offset": off,
            "text_layer": "good", "chapters": chapters,
            "front_matter_end": chapters[0]["pdf_start"] - 1}


def mcmt():
    d = fitz.open(CM / "MCMT.pdf")
    off, votes = detect_offset(d, [30, 80, 150, 250, 350, 430], 500)
    txt = "".join(d[i].get_text() for i in range(2, 11))
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    chapters = []
    for i, l in enumerate(lines):
        m = re.match(r"^C\s*(\d+)\.$", l) or \
            re.match(r"^A\s*([A-D])\.$", l)
        if m and i + 2 < len(lines) and lines[i + 2].isdigit():
            chapters.append({"num": m.group(1), "title": decode_mcmt(lines[i + 1]),
                             "pdf_start": int(lines[i + 2]) + off})
    # Chapter 24's printed page is glued to its title line in the contents; add by hand
    # (printed 335 + offset), keeping chapter order. Titles lose spaces and fi/ff/ffl
    # ligatures in the cipher decode — override with the book's actual titles.
    chapters.append({"num": "24", "title": "", "pdf_start": 335 + off})
    chapters.sort(key=lambda c: c["pdf_start"])
    titles = {
        "1": "Introduction to Finite Markov Chains",
        "2": "Classical (and Useful) Markov Chains",
        "3": "Markov Chain Monte Carlo: Metropolis and Glauber Chains",
        "4": "Introduction to Markov Chain Mixing", "5": "Coupling",
        "6": "Strong Stationary Times", "7": "Lower Bounds on Mixing Times",
        "8": "The Symmetric Group and Shuffling Cards", "9": "Random Walks on Networks",
        "10": "Hitting Times", "11": "Cover Times", "12": "Eigenvalues",
        "13": "Eigenfunctions and Comparison of Chains",
        "14": "The Transportation Metric and Path Coupling", "15": "The Ising Model",
        "16": "From Shuffling Cards to Shuffling Genes",
        "17": "Martingales and Evolving Sets", "18": "The Cutoff Phenomenon",
        "19": "Lamplighter Walks", "20": "Continuous-Time Chains*",
        "21": "Countable State Space Chains*", "22": "Monotone Chains",
        "23": "The Exclusion Process",
        "24": "Cesàro Mixing Time, Stationary Times, and Hitting Large Sets",
        "25": "Coupling from the Past", "26": "Open Problems",
        "A": "Background Material", "B": "Introduction to Simulation",
        "C": "Ergodic Theorem", "D": "Solutions to Selected Exercises",
    }
    for c in chapters:
        c["title"] = titles.get(c["num"], c["title"])
    return {"key": "mcmt", "pdf": "MCMT.pdf",
            "title": "Markov Chains and Mixing Times (2nd ed.)",
            "author": "David A. Levin, Yuval Peres", "npages": len(d), "printed_offset": off,
            "text_layer": "unusable (private-use-area fonts)", "chapters": chapters,
            "front_matter_end": chapters[0]["pdf_start"] - 1 if chapters else 0}


def islp():
    d = fitz.open(CM / "ISLP_Textbook.pdf")
    chapters = []
    for lvl, title, page in d.get_toc():
        if lvl == 1:
            m = re.match(r"^(\d+)\s+(.*)", title)
            num, t = (m.group(1), m.group(2)) if m else ("", title)
            chapters.append({"num": num, "title": t, "pdf_start": page})
    body = [c for c in chapters if c["num"]]
    return {"key": "islp", "pdf": "ISLP_Textbook.pdf",
            "title": "An Introduction to Statistical Learning with Applications in Python",
            "author": "James, Witten, Hastie, Tibshirani, Taylor", "npages": len(d),
            "printed_offset": None, "text_layer": "good", "chapters": chapters,
            "front_matter_end": body[0]["pdf_start"] - 1 if body else 0}


def montgomery():
    d = fitz.open(CM / "546_textbook.pdf")
    off, votes = detect_offset(d, [40, 120, 250, 400, 550, 700], 800)
    txt = "".join(d[i].get_text() for i in range(9, 18))
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    chapters = []
    for i, l in enumerate(lines):
        if re.fullmatch(r"1[0-5]|[1-9]", l) and i + 1 < len(lines) and re.match(r"[A-Z]", lines[i + 1]):
            j, title = i + 1, []
            while j < len(lines) and not lines[j].isdigit() and len(title) < 3:
                title.append(lines[j])
                j += 1
            if j < len(lines) and lines[j].isdigit():
                want = int(l)
                have = max([int(c["num"]) for c in chapters if c["num"].isdigit()], default=0)
                if want == have + 1:  # contents lists chapters in order; skip section noise
                    chapters.append({"num": l, "title": " ".join(title),
                                     "pdf_start": int(lines[j]) + off})
        elif l == "Appendix" and i + 1 < len(lines) and lines[i + 1].isdigit():
            chapters.append({"num": "A", "title": "Appendix (Statistical Tables)",
                             "pdf_start": int(lines[i + 1]) + off})
    return {"key": "montgomery_doe", "pdf": "546_textbook.pdf",
            "title": "Design and Analysis of Experiments (8th ed.)",
            "author": "Douglas C. Montgomery", "npages": len(d), "printed_offset": off,
            "text_layer": "usable (ligatures fi/ff/fl dropped)", "chapters": chapters,
            "front_matter_end": chapters[0]["pdf_start"] - 1 if chapters else 0}


def verify(book):
    d = fitz.open(CM / book["pdf"])
    problems = []
    for ch in book["chapters"]:
        p = ch["pdf_start"]
        if not (1 <= p <= book["npages"]):
            problems.append(f"ch {ch['num']} start {p} out of range")
            continue
        t = d[p - 1].get_text()
        hay = decode_mcmt(t) if book["key"] == "mcmt" else t
        first_words = " ".join(ch["title"].split()[:2])
        if ch["num"] and not (re.search(rf"(?i)chapter\s*{re.escape(ch['num'])}\b", hay)
                              or first_words.lower() in hay.lower()
                              or ch["title"].split()[0].lower() in hay.lower()):
            problems.append(f"ch {ch['num']} '{ch['title']}' not found on PDF p.{p}: {hay[:90]!r}")
    return problems


def main():
    books = [lawler(), mcmt(), islp(), montgomery()]
    for b in books:
        probs = verify(b)
        status = "OK" if not probs else f"{len(probs)} PROBLEM(S)"
        print(f"== {b['key']}: {len(b['chapters'])} chapters, offset={b['printed_offset']}, {status}")
        for c in b["chapters"]:
            print(f"   ch {c['num'] or '-':>2} @ PDF {c['pdf_start']:4d}  {c['title']}")
        for p in probs:
            print(f"   !! {p}")
    (HERE / "books.json").write_text(json.dumps(books, indent=1))
    print(f"\nwrote {HERE / 'books.json'}")


if __name__ == "__main__":
    main()

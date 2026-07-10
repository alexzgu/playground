#!/usr/bin/env python3
"""Machine-check every claim extracted during transcription.

For each transcribed page: pull the CLAIM blocks from out/raw/, execute each
check in a subprocess (sympy/numpy/scipy/math/fractions only; a crude import
guard rejects anything else), then

  * replace `> ⏳ VERIFY[ck]: ...` placeholders in out/pages/p-NNN.md with
    `> ✔ Verified: ...` / `> ⚠ Check FAILED: ...`,
  * record results in out/verify-results.json and the manifest,
  * regenerate the pipeline-managed rows (PDF p. >= 23) of verification-log.md.

Usage: python3 verify_claims.py [--pages 23-39] [--rerun]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "out"
LOG = ROOT / "verification-log.md"
CHECK_TIMEOUT_S = 90

IMPORT_WHITELIST = {"sympy", "numpy", "scipy", "math", "fractions", "mpmath",
                    "itertools", "functools", "statistics", "decimal", "collections"}
BAD_CALLS = re.compile(r"__import__|open\s*\(|exec\s*\(|eval\s*\(|compile\s*\("
                       r"|subprocess|socket|os\.system|os\.popen")

CLAIM_RE = re.compile(r"^CLAIM (c\d+):\s*(.+?)\s*\n```python\n(.*?)```", re.M | re.S)


def guard(code: str) -> str | None:
    for m in re.finditer(r"^\s*(?:from\s+([\w.]+)\s+import|import\s+(.+))", code, re.M):
        roots = ([m.group(1).split(".")[0]] if m.group(1) else
                 [seg.strip().split(".")[0].split(" ")[0] for seg in m.group(2).split(",")])
        for r in roots:
            if r and r not in IMPORT_WHITELIST:
                return f"disallowed import: {r}"
    if BAD_CALLS.search(code):
        return "disallowed call"
    return None


def run_check(code: str) -> tuple[str, str]:
    reason = guard(code)
    if reason:
        return "unsafe", reason
    try:
        r = subprocess.run([sys.executable, "-c", code], capture_output=True,
                           text=True, timeout=CHECK_TIMEOUT_S)
    except subprocess.TimeoutExpired:
        return "error", f"timed out after {CHECK_TIMEOUT_S}s"
    if r.returncode == 0:
        return "pass", ""
    tail = (r.stderr.strip().splitlines() or [""])[-1]
    return ("fail" if "AssertionError" in r.stderr else "error"), tail[:300]


def verify_page(name: str) -> dict:
    raw = (OUT / "raw" / f"{name}.raw.md").read_text()
    page_path = OUT / "pages" / f"{name}.md"
    # rebuild the page from the raw TRANSCRIPT section so re-verification is idempotent
    m = re.search(r"^===\s*TRANSCRIPT\s*===\s*$(.*?)(?=^===\s*CLAIMS\s*===\s*$|\Z)", raw, re.M | re.S)
    text = (m.group(1).strip() + "\n") if m else page_path.read_text()
    text = "\n".join(ln for ln in text.splitlines()
                     if not ln.startswith("*Running header:")) + "\n"
    results = {}
    for cid, desc, code in CLAIM_RE.findall(raw):
        verdict, detail = run_check(code)
        results[cid] = {"desc": desc, "verdict": verdict, "detail": detail}
        marker = re.compile(r"> ⏳ VERIFY\[%s\]:.*" % cid)
        if verdict == "pass":
            repl = f"> ✔ Verified: {desc}"
        elif verdict == "fail":
            repl = f"> ⚠ Check FAILED: {desc} — the stated result did not reproduce (see verification log)"
        else:
            repl = f"> ⚠ Check could not run ({verdict}): {desc} — {detail}"
        text, n = marker.subn(lambda _m: repl, text)  # literal repl: descriptions carry LaTeX backslashes
        if n == 0:
            results[cid]["detail"] += " [no matching placeholder in transcript]"
    # any leftover placeholders had no claim block
    text = re.sub(r"> ⏳ VERIFY\[(c\d+)\]: (.*)",
                  r"> ⚠ Unchecked: \2 (no claim code was produced)", text)
    page_path.write_text(text)
    return results


def rebuild_log(all_results: dict, manifest: dict):
    lines = LOG.read_text().splitlines()
    # keep everything up to and including the last hand-written row (PDF p. < 23)
    kept, in_table = [], False
    for ln in lines:
        m = re.match(r"\|\s*(\d+)\s*\|", ln)
        if m and int(m.group(1)) >= 23:
            in_table = True
            continue  # drop pipeline-managed rows; they get regenerated
        if ln.startswith("Pipeline summary:"):
            continue
        kept.append(ln)
    # find insertion point: after the last table row
    last_row = max(i for i, ln in enumerate(kept) if ln.startswith("|"))
    new_rows, n_pass = [], 0
    for name in sorted(all_results):
        pdf = int(name.split("-")[1])
        for cid in sorted(all_results[name], key=lambda c: int(c[1:])):
            r = all_results[name][cid]
            mark = {"pass": "✔", "fail": "⚠ FAILED"}.get(r["verdict"], f"⚠ {r['verdict']}")
            n_pass += r["verdict"] == "pass"
            desc = r["desc"].replace("|", "\\|")
            new_rows.append(f"| {pdf} | {desc} | auto (SymPy pipeline) | {mark} |")
    out = kept[:last_row + 1] + new_rows + kept[last_row + 1:]
    n_total = sum(len(v) for v in all_results.values())
    out.append("")
    out.append(f"Pipeline summary: {n_total} machine checks on PDF pages ≥ 23; "
               f"{n_pass} passed, {n_total - n_pass} flagged. Details: transcribe/out/verify-results.json")
    LOG.write_text("\n".join(out).rstrip() + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", default="all")
    ap.add_argument("--rerun", action="store_true", help="re-check pages already verified")
    args = ap.parse_args()

    manifest = json.loads((OUT / "manifest.json").read_text())
    results_path = OUT / "verify-results.json"
    all_results = json.loads(results_path.read_text()) if results_path.exists() else {}

    wanted = None
    if args.pages != "all":
        wanted = set()
        for part in args.pages.split(","):
            if "-" in part:
                a, b = part.split("-")
                wanted.update(range(int(a), int(b) + 1))
            else:
                wanted.add(int(part))

    for name, entry in sorted(manifest.items()):
        pdf = int(name.split("-")[1])
        if wanted and pdf not in wanted:
            continue
        if entry.get("status") not in ("transcribed",) and not args.rerun:
            continue
        res = verify_page(name)
        all_results[name] = res
        verdicts = [r["verdict"] for r in res.values()]
        entry["verified"] = {"pass": verdicts.count("pass"),
                             "fail": verdicts.count("fail"),
                             "other": len(verdicts) - verdicts.count("pass") - verdicts.count("fail")}
        entry["status"] = "verified" if all(v == "pass" for v in verdicts) else "verified-with-flags"
        flag = "" if entry["status"] == "verified" else "  <-- review"
        print(f"{name}: {len(verdicts)} checks, {verdicts.count('pass')} pass{flag}")

    results_path.write_text(json.dumps(all_results, indent=1, sort_keys=True))
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=1, sort_keys=True))
    rebuild_log(all_results, manifest)
    print(f"\nverification-log.md updated; details in {results_path}")


if __name__ == "__main__":
    main()

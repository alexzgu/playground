# Curriculum transcription status

Audit date: 2026-07-24

The current round stopped at the requested boundaries. No transcription runner or
Claude child process remains active. Canonical curriculum files were rebuilt after
the final manual repairs.

| Material | Verified coverage | Status / remaining source pages |
|---|---:|---|
| Bayesian booklet | 195/195 | Complete; every PDF page appears exactly once. Pages 23–195 retain pipeline verification and quantitative checks; pages 186 and 189–195 were repaired/reintegrated during this audit. |
| Stochastic Calculus | 260/260 | Complete. Four low text-layer scores (13, 94, 115, 179) were visually verified. |
| Markov Chains and Mixing Times | 461/461 | Complete; no missing or low-QA pages. |
| ISLP | 300/613 | Verified contiguous PDF pages 1–300. Remaining: 301–613. |
| Statistical Rethinking | 240/617 | Verified contiguous PDF pages 1–240. Remaining: 241–617. |
| Montgomery DOE | 243/757 | Verified PDF pages 1–240 and the earlier pages 362–364. Remaining: 241–361 and 365–757. |
| Casella–Berger derivatives | unverified | The exact source PDF/edition is absent. The two legacy text derivatives cannot be certified page by page; see `curriculum_material/casella_berger/README.md`. |

## Verification result

`FINAL_AUDIT.json` is the machine-readable final audit for the five textbook-pipeline
books. All five currently report:

- manifest/page-file/assembled coverage in agreement;
- exactly one valid PDF-page heading per delivered page;
- no stale failure errors on successful entries;
- no missing raw provenance;
- balanced fenced-code and display-math delimiters;
- zero structural problems.

Every page added or accepted in this round was compared with its full rendered JPEG
and, where usable, its PDF text layer. Pages rejected by Claude's content policy or
left after the Claude usage limit were manually transcribed and visually reviewed by
GPT-5.6. Low text-layer scores caused by figures, tables, or column order were not
accepted until visual review.

The review caught and repaired errors that token QA did not catch, including wrong
Greek symbols, a wrong inequality, wrong table values and contrast equations,
missing denominators, unresolved endnotes, flattened list/section structure, and
model-invented `[sic]`, review notes, continuation notes, and figure explanations.

## Tooling changes

- `transcribe_books.py` now uses locked, atomic cross-process manifest merges,
  records model/effort provenance, computes multiset recall plus token-order QA,
  supports session-independent `--detach --log`, clears stale errors after repair,
  distinguishes content-policy failures from real quota/rate failures, and reports
  pending pages honestly.
- `register_manual_batch.py` safely registers visually reviewed manual page batches.
- `audit_transcripts.py` checks canonical, manifest, raw-provenance, assembled, QA,
  heading, delimiter, and stale-error consistency. Raw/canonical differences after
  human correction are reported informationally rather than treated as defects.
- The transcription prompt now forbids invented editorial markers or review notes.

## Work remaining after this stop

- ISLP: 313 pages (301–613).
- Statistical Rethinking: 377 pages (241–617).
- Montgomery DOE: 514 pages (241–361 and 365–757).
- Casella–Berger: obtain the exact source PDF/edition before replacing the legacy
  derivatives with a verified page-by-page transcript.
- Optional consistency cleanup: 75 legacy `[sic]` annotations remain across 58
  pre-existing page files in MCMT, Stochastic Calculus, early Rethinking, and early
  Montgomery. They reflect the former style rule for visibly apparent source typos;
  new/repaired pages preserve typos silently. Removing them safely requires checking
  the few annotations that also contain inferred corrections, not a blind replace.


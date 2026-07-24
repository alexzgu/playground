# MA 556, Applied Bayesian Statistics — Booklet Transcript (Fall 2025)

Source: `transcription/Bayesian-Booklet-Fa2025.pdf` — 195 scanned pages (typeset LaTeX booklet with handwritten lecture annotations), MA 556, Applied Bayesian Statistics, Balgobin Nandram, WPI, Fall 2025.

**Conventions**
- One markdown file per chapter (chapters follow the booklet's own Contents: "Lecture One", "Lecture Two", …, plus the named chapters and Appendix A).
- Every page appears under a heading `### PDF page N (booklet page M)`. Blank pages are recorded as blank.
- Math is set in LaTeX (`$...$` inline, `$$...$$` display). Under-tilde vector notation in the booklet is rendered as bold or plain symbols.
- Handwritten annotations and corrections on the pages are **incorporated**: corrections are applied to the text and flagged *(correction: …)*; explanatory margin notes appear as *[margin note: …]*; illegible scribbles are flagged as such.
- Every quantitative result is machine-checked. A `> ✔ Verified: …` note (or `> ⚠ …` for a discrepancy) follows each result. All computations are logged in `verification-log.md`.
- Obvious typos in the source are transcribed faithfully with `[sic]` where meaningful.

## Provenance

- PDF pages 1–22 were transcribed by hand in the initial session.
- PDF pages 23–195 were produced by the page-image pipeline in `transcription/transcribe/`; quantitative checks and per-page state are retained there.
- During the 2026-07-23 audit, PDF page 186 was faithfully re-transcribed from the source scan to replace an earlier content-filter summary, and Appendix A (PDF pages 189–195) was restored to the curriculum-material deliverable from the verified per-page outputs. The appendix scans were visually rechecked; this corrected the R assignment on PDF page 191 and a false lowercase-`l` reading of “Import” on PDF page 192.

## STATUS OF THIS TRANSCRIPT

**Complete:** all 195 PDF pages are represented exactly once in `curriculum_material/bayesian_booklet/`.
Pages where a machine check documents a suspected **error in the booklet itself** (each flagged inline with a [sic] note): 48, 74–75, 79–80, 85–86, 129, 173 — see verification-log.md and transcribe/out/verify-results.json.
PDF page 186 was manually re-transcribed from the source scan during the 2026-07-23 audit, replacing an earlier content-filter summary. Appendix A (PDF pages 189–195) was reintegrated from the pipeline's verified page outputs.

Produced by the pipeline in `transcribe/` (see its README). Machine checks are logged in `verification-log.md`.

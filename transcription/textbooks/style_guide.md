# Transcription conventions (all textbooks)

These transcripts are the permanent markdown record of each book's pages, in the same
spirit as the completed `bayesian_booklet` transcript. Source pages are **typeset,
digitally-produced PDFs** (no handwriting).

## Page structure
- Every page begins with the heading `### PDF page {N} (book page {M})`, where M is the
  page number **printed on the page itself** (arabic or roman, e.g. `vii`). If no page
  number is printed, use `### PDF page {N} (no printed page number)`.
- Blank pages: after the heading, write exactly `*(Blank page.)*` and nothing else.
- Do **not** transcribe running headers/footers (page number, chapter/section running
  titles) — the page heading already records the page identity.
- Chapter opening pages repeat the chapter title as content: `# Chapter {N} — {Title}`
  (`# Appendix {X} — {Title}` for appendices).
- Section headers are bold, keeping the book's numbering: `**3.2 The Analysis of
  Variance**`; subsections `**2.4.1 Hypothesis Testing**`. Unnumbered sidebars/boxes
  keep their heading in bold.

## Math
- Inline math in `$...$`, displayed equations in `$$...$$`. Preserve the book's own
  notation and equation numbers: put the printed tag at the end of the display, e.g.
  `$$ ... \tag{3.5} $$`.
- Preserve theorem/lemma/definition/example structure: `**Theorem 5.2.** *statement...*`
  followed by the proof (`*Proof.*` ... `$\blacksquare$`/`□` as printed).

## Figures and tables
- Tables: reproduce as markdown tables, **all rows and columns**, numbers exactly as
  printed (cross-check against the machine text layer when provided). Very wide tables
  may be split into stacked markdown tables; say so in an italic note.
- Figures/plots: do not skip. Transcribe the full printed caption verbatim, then a
  concise italic description of what the figure shows:
  `**FIGURE 3.1** caption text... *[Figure: two side-by-side scatterplots of ... ]*`
- Statistical appendix tables (percentage points etc.): transcribe fully as markdown
  tables, using the machine text layer to get every number exact.

## Code
- Code listings (Python in ISLP, R elsewhere) in fenced blocks with the right language
  tag; transcribe code and printed output exactly, output in a separate ```` ``` ````
  block (no language tag) when the book shows it.

## Fidelity
- Transcribe faithfully, typos included, flagging with `[sic]`. Do not "improve"
  wording, reorder content, or complete truncated sentences — pages may begin or end
  mid-sentence; leave them so.
- Footnotes: transcribe at the bottom of the page as `[^N]: ...` with the reference
  marker `[^N]` in the text.
- Exercises/problems: transcribe fully, keeping their numbering.
- Marginal labels the book uses (e.g. ISLP's blue margin keywords) become italic
  bracketed notes: `*[margin: cross-validation]*` — only when they add information not
  already in the text.

## Machine text layer (when provided)
A machine text extraction of the page accompanies the image. Use it to confirm exact
wording, numbers, and table entries. But **trust the image** for structure: reading
order, column layout, math (the extraction mangles sub/superscripts and symbols), and
missing glyphs — some books drop the ligatures fi/ff/fl/ffl from the extraction
("benet" → "benefit"), and one book's extraction is garbled ciphertext and is not
provided at all.

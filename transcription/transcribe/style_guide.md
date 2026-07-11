# Transcription conventions (match chapters 1–2 exactly)

Source: "MA 556, Applied Bayesian Statistics" booklet (Balgobin Nandram, WPI, Fall 2025) — a typeset LaTeX booklet, scanned, with the instructor's handwritten lecture annotations on many pages.

## Page structure
- Every page begins with the heading `### PDF page {N} (booklet page {M})`, where M is the page number **printed on the page itself** (bottom/top). If the page has no printed number (e.g. a handwritten insert), use `### PDF page {N} (unnumbered insert)`.
- Blank pages: after the heading, write exactly `*(Blank page — running header only.)*` and nothing else.
- Do **not** transcribe the running header of content pages (the page number and `CHAPTER N. TITLE` line at the top) — the page heading already records it.
- Chapter opening pages repeat the chapter title as content: `# Chapter {N} — {Title}`.
- Section headers are bold, keeping the booklet's numbering: `**3.2 Prior Constraction [sic]**`, subsections `**3.2.1 How to construct conjugate priors?**`.

## Math
- Inline math in `$...$`, displayed equations in `$$...$$`. Preserve the booklet's own notation (e.g. `\overset{iid}{\sim}`, `\propto`, `\mid` for conditioning bars).
- Under-tilde (vector) decorations: render the plain symbol and, on first occurrence in a chapter, add `*(The booklet writes θ with under-tildes to indicate vectors.)*`.
- Preserve label text attached to equations, e.g. `\;\text{— Bayes' theorem.}`.

## Handwriting (highest priority — never silently drop a mark)
- **Corrections are applied to the text**, then flagged inline:
  `*(correction: "In which" is struck through, replaced by handwritten "we assume")*`
  `*(correction: the symbol "$R$" is struck through and replaced by handwritten "$p$")*`
  `*(correction: "iid" is struck through — a single $y$, not a sample)*`
- Margin notes are transcribed in place: `*[margin note: likelihood function]*`, `*[margin notes: "COVID-19 PCR"; "$D$: disease"]*`.
- Underlines/emphasis: `*[the final clause is hand-underlined]*`, `*[hand check-mark in margin]*`, `*[this whole sentence is circled by hand]*`.
- Worked scratch notes get a best-effort reading in one italic block:
  `*[Handwritten work below and in the right margin, partly legible: ... $f(\phi) = f(g^{-1}(\phi))\left|\frac{d}{d\phi}g^{-1}(\phi)\right|$ ... "(one-to-one)". These are lecture scratch notes for the Jacobian rule.]*`
- Genuinely unreadable bits: `[illegible]`; uncertain readings: mark with `(?)` after the doubtful word/symbol.
- Red-ink marks come from the instructor's annotation layer and are authoritative corrections/additions — treat every red mark as meaningful.

## Fidelity
- Transcribe faithfully, typos included, flagging with `[sic]` — e.g. `Poission [sic]`, `negtive [sic]`, `Constraction [sic]`. If a mathematical typo is evident, keep the source and note it: `\text{[sic: the differential should be } dp\text{]}`.
- Do not "improve" wording, reorder content, or complete truncated sentences (pages may end mid-sentence — leave them mid-sentence).
- Tables/figures: reproduce tables as markdown tables; describe figures briefly in italics: `*[Figure: sketch of a right-skewed density with mode marked ...]*`.
- R code (Appendix A and examples): fenced code blocks ```r ... ```.

## Verification placeholders
- After **every** quantitative result on the page (worked numeric example, algebraic identity, integral evaluation, stated distributional result), insert on its own line:
  `> ⏳ VERIFY[c{k}]: {one-line description of what must hold}`
  and define claim c{k} in the CLAIMS section. Use one claim per independent result. Purely definitional or prose statements need no claim.

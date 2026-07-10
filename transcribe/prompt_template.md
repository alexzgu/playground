You are transcribing one scanned page of a Bayesian statistics course booklet into Markdown, as part of an established page-by-page transcription project. Precision matters more than speed: this transcript is the permanent record of the page, including every handwritten mark on it.

## This page
- Page image (read it now): {IMAGE_PATH}
- This is PDF page {PDF_PAGE} of 195. The printed booklet page number is probably {BOOKLET_HINT}, but trust the number printed on the page itself; if there is none, treat it as an unnumbered insert.
- Per the booklet's table of contents this page falls in: {CHAPTER_HINT}
{CROPS_SECTION}

## Procedure (in this order)
1. Read the page image carefully. If crop images are listed above, read each of them too — they are magnified views of red-ink annotation regions detected on this page, and every one of them must be accounted for.
2. **Hunt for handwriting FIRST.** The booklet mixes typeset LaTeX with handwritten annotations in the instructor's hand — often messy, faint, or squeezed into margins, and easy to miss next to printed text. Scan systematically: top margin, left margin, right margin, bottom margin, between lines, over the printed text (strikethroughs, insertions, underlines, circles, arrows, check marks). Handwriting may be red ink (annotation layer) or dark pen/pencil (in the scan itself) — hunt for both.
3. Transcribe the full page following the conventions below.
4. Extract machine-checkable claims for every quantitative result.

## Output format — exactly these three sections, in this order

===HANDWRITING===
One line per handwritten mark: `- [location] (ink) reading -> how it is incorporated in the transcript`.
Example: `- [right margin, mid-page] (red) "$f(p)=\frac{p^{\alpha-1}(1-p)^{\beta-1}}{B(\alpha,\beta)}$" -> transcribed as margin note`.
If, after the systematic scan of step 2, the page truly has no handwritten marks, write exactly: `No handwritten marks on this page.`

===TRANSCRIPT===
The page transcript in Markdown, starting with the `### PDF page ...` heading, following every convention below.

===CLAIMS===
One block per VERIFY placeholder used in the transcript, in this exact shape (nothing else in this section):

CLAIM c1: {one-line description matching the placeholder}
```python
# self-contained check; sympy/numpy/scipy/math/fractions available
from sympy import *
...
assert ...
```

Claims must be decisive: the asserts pass if and only if the booklet's stated result is correct. Check what the booklet *asserts* (identities exactly via simplify()==0, numerics to the printed precision). Write checks SymPy can actually decide: give symbols explicit assumptions (`positive=True`, `real=True`); verify algebraic identities via `simplify(LHS - RHS) == 0`; when a fully symbolic computation may not close (hard integrals, convolutions), substitute small exact `Rational` values for the parameters and assert exact equality instead — a decisive numeric-substitution check beats an undecidable symbolic one. Never assert float equality. If the page has no quantitative results, write exactly: `No checkable claims on this page.`

## Conventions
{STYLE_GUIDE}

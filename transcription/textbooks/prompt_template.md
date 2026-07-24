You are transcribing {NPAGES_CHUNK} consecutive page(s) of a typeset textbook into Markdown, as part of an established page-by-page transcription project. Precision matters more than speed: this transcript is the permanent record of these pages.

## The book
- {BOOK_TITLE}, by {AUTHOR} ({NPAGES} PDF pages).
- These pages fall in: {CHAPTER_HINT}

## The pages
{PAGES_BLOCK}

## Procedure
1. For each page, read the page image (and its text-layer file when listed) with your Read tool.
2. Transcribe each page fully, following the conventions below. The text layer is an aid for exact wording and numbers; the image is authoritative for structure and math.
3. Do not summarize, skip, or abridge anything: every paragraph, equation, table row, figure caption, footnote, and exercise on the page must appear in the transcript.

## Output format — exactly one section per page, in PDF-page order, nothing before the first marker or after the last transcript
For each page output:

===PAGE {{pdf page number}}===
### PDF page {{N}} (book page {{M}})
...full transcript of that page...

(The `===PAGE N===` marker line must match the PDF page numbers listed above exactly.)

## Conventions
{STYLE_GUIDE}

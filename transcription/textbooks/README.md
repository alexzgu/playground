# Textbook transcription pipeline

Automates page-by-page markdown transcription of the four remaining curriculum
textbooks (the Bayesian booklet was done earlier by the sibling pipeline in
`../transcribe/`). Output chapter files land in `curriculum_material/<key>/`.

| key | source PDF | book | pages |
|---|---|---|---|
| `stochastic_calculus` | stochastic_calculus.pdf | Lawler, *Stochastic Calculus: An Introduction with Applications* | 260 |
| `mcmt` | MCMT.pdf | Levin & Peres, *Markov Chains and Mixing Times* (2nd ed.) | 461 |
| `islp` | ISLP_Textbook.pdf | James et al., *An Introduction to Statistical Learning with Applications in Python* | 613 |
| `montgomery_doe` | 546_textbook.pdf | Montgomery, *Design and Analysis of Experiments* (8th ed.) | 757 |

## How it differs from the booklet pipeline
- **Digital PDFs, not scans**: no handwriting hunt, no annotation detection.
- **Text-layer assist**: three of the books have a usable PDF text layer; it is
  dumped per page and handed to the model alongside the image to nail exact wording
  and table numbers. (MCMT's text layer is ciphertext — its fonts map glyphs into the
  Unicode private-use area — so MCMT is transcribed from images alone.) A per-page QA
  score (fraction of text-layer words recovered in the transcript) is stored in the
  manifest; pages under 0.55 get status `transcribed-lowqa` and are listed in the
  book's README for spot-checking.
- **Chunked calls**: up to 3 consecutive pages per `claude -p` call (~3× throughput).
- **No SymPy verification stage** (the booklet had one): at ~2,100 pages, coverage was
  prioritized over machine-checking. The text-layer QA is the safety net.
- **Chapter maps are precomputed** (`books.json`, built by `build_books_json.py` from
  each PDF's outline/contents, chapter-start pages verified against page text) — the
  assembler groups by PDF page number, which is stable for digital PDFs.

## Run it

```bash
python3 render_pages.py                          # once — page JPEGs + text layers
python3 transcribe_books.py --book <key>         # all pending pages (resumable)
python3 assemble.py --book <key>                 # rebuild curriculum_material/<key>/
./supervisor.sh                                  # or: drive all four books end-to-end
```

Useful variations:

```bash
python3 transcribe_books.py --book islp --pages 78-143      # one chapter's worth
python3 transcribe_books.py --book mcmt --pages 231 --force # redo a page
```

The supervisor processes books smallest-first (stochastic_calculus → mcmt → islp →
montgomery_doe) so complete books accumulate; it backs off 30 min on usage-limit
breaker trips, re-assembles chapter files after every runner pass, and drops
`books/<key>/out/COMPLETE` markers. Launch it detached to survive session teardown:
`setsid nohup ./supervisor.sh &`.

## State & outputs
- `books/<key>/pages/p-NNNN.jpg`, `books/<key>/text/p-NNNN.txt` — inputs.
- `books/<key>/out/manifest.json` — per-page status / printed page / QA score.
  Delete an entry (or `--force`) to redo a page.
- `books/<key>/out/raw/chunk-*.raw.md` — full model output per chunk.
- `books/<key>/out/pages/p-NNNN.md` — per-page transcripts.
- `curriculum_material/<key>/chNN-*.md` + `README.md` — assembled chapters (chapter
  files carry an "in progress" banner until their page range is fully transcribed).
- `supervisor.log`, `run.log`, `render.log` — pipeline logs.

## Reviewing quality
Check each book README's low-QA list, spot-check those pages against
`books/<key>/pages/p-NNNN.jpg`. For MCMT (no QA), sample a few pages per chapter.

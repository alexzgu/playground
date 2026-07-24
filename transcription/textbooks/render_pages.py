#!/usr/bin/env python3
"""Render every page of each textbook to JPEG + dump its text layer.

Outputs, per book key from books.json:
  books/<key>/pages/p-NNNN.jpg   page image, long side ~1560 px (vision-API cap)
  books/<key>/text/p-NNNN.txt    machine text layer (skipped where unusable)

Idempotent: existing files are kept unless --force.
Usage: python3 render_pages.py [--book KEY] [--force]
"""
import argparse
import json
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
CM = HERE.parent.parent / "curriculum_material"
TARGET_PX = 1560  # Claude vision downsamples past ~1568 px on the long side


def render_book(book: dict, force: bool):
    key = book["key"]
    pages_dir = HERE / "books" / key / "pages"
    text_dir = HERE / "books" / key / "text"
    pages_dir.mkdir(parents=True, exist_ok=True)
    want_text = not book["text_layer"].startswith("unusable")
    if want_text:
        text_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(CM / book["pdf"])
    n_img = n_txt = 0
    for i, page in enumerate(doc):
        n = i + 1
        img = pages_dir / f"p-{n:04d}.jpg"
        if force or not img.exists():
            zoom = TARGET_PX / max(page.rect.width, page.rect.height)
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
            pix.save(img, jpg_quality=80)
            n_img += 1
        if want_text:
            txt = text_dir / f"p-{n:04d}.txt"
            if force or not txt.exists():
                # ligatures may still be dropped by the PDF's own encoding; noted in prompt
                txt.write_text(page.get_text())
                n_txt += 1
    print(f"{key}: rendered {n_img} images, {n_txt} text dumps "
          f"({len(doc)} pages total)", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--book", help="book key (default: all)")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    books = json.loads((HERE / "books.json").read_text())
    for b in books:
        if not args.book or b["key"] == args.book:
            render_book(b, args.force)


if __name__ == "__main__":
    main()

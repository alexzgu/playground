#!/usr/bin/env python3
"""Detect red-ink annotation regions on booklet page images.

The PDF's red-ink annotation layer was burned into the page renders. Red is
color-separable from the black print, so we can deterministically find those
regions, save zoomed crops for the transcriber, and rank pages by annotation
density. (Dark-pen handwriting in the original scans is NOT color-separable —
the transcription prompt handles that case.)

Usage: python3 detect_annotations.py [--pages-dir ../pages] [--out out]
Writes: out/annotations.json, out/crops/p-NNN/crop-K.png
"""
import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

MIN_REGION_PX = 40        # ignore specks
PAD = 60                  # context padding around each region, in px
ZOOM = 2                  # crop upscale factor


def red_mask(img: Image.Image) -> np.ndarray:
    a = np.asarray(img.convert("RGB"), dtype=np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (r > 120) & (r - g > 50) & (r - b > 50)


def detect_page(path: Path, crops_dir: Path) -> dict:
    img = Image.open(path)
    mask = red_mask(img)
    total = int(mask.sum())
    regions = []
    if total >= MIN_REGION_PX:
        # dilate so nearby strokes merge into one region
        fat = ndimage.binary_dilation(mask, iterations=15)
        labels, n = ndimage.label(fat)
        for sl in ndimage.find_objects(labels):
            region_px = int(mask[sl].sum())
            if region_px < MIN_REGION_PX:
                continue
            y0, y1 = sl[0].start, sl[0].stop
            x0, x1 = sl[1].start, sl[1].stop
            regions.append({"box": [int(x0), int(y0), int(x1), int(y1)], "red_px": region_px})
        regions.sort(key=lambda r: -r["red_px"])
        crops_dir.mkdir(parents=True, exist_ok=True)
        for i, reg in enumerate(regions):
            x0, y0, x1, y1 = reg["box"]
            x0, y0 = max(0, x0 - PAD), max(0, y0 - PAD)
            x1, y1 = min(img.width, x1 + PAD), min(img.height, y1 + PAD)
            crop = img.crop((x0, y0, x1, y1))
            crop = crop.resize((crop.width * ZOOM, crop.height * ZOOM), Image.LANCZOS)
            crop_path = crops_dir / f"crop-{i}.png"
            crop.save(crop_path)
            reg["crop"] = str(crop_path)
    return {"red_px": total, "regions": regions}


def main():
    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    ap.add_argument("--pages-dir", default=str(here.parent / "pages"))
    ap.add_argument("--out", default=str(here / "out"))
    args = ap.parse_args()

    pages_dir, out_dir = Path(args.pages_dir), Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for path in sorted(pages_dir.glob("p-*.jpg")):
        name = path.stem
        results[name] = detect_page(path, out_dir / "crops" / name)
        if results[name]["red_px"]:
            print(f"{name}: {results[name]['red_px']} red px, {len(results[name]['regions'])} regions")
    (out_dir / "annotations.json").write_text(json.dumps(results, indent=1))
    marked = sum(1 for v in results.values() if v["regions"])
    print(f"\n{len(results)} pages scanned, {marked} with red-ink regions -> {out_dir/'annotations.json'}")


if __name__ == "__main__":
    main()

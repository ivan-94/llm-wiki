#!/usr/bin/env python3
"""Resize and compress a generated podcast infographic for Obsidian."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", help="Input image from imagegen")
    parser.add_argument("--output", required=True, help="Output .webp path")
    parser.add_argument("--max-width", type=int, default=1600, help="Maximum output width")
    parser.add_argument("--quality", type=int, default=82, help="Initial WebP quality")
    parser.add_argument("--max-bytes", type=int, default=3_000_000, help="Target hard size ceiling")
    parser.add_argument("--no-install", action="store_true", help="Do not install Pillow when missing")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    return parser.parse_args()


def ensure_pillow(no_install: bool) -> Any:
    try:
        from PIL import Image

        return Image
    except ImportError:
        if no_install:
            raise SystemExit("Missing Pillow and --no-install was provided.")
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", "-U", "pillow"], check=True)
        from PIL import Image

        return Image


def flatten_for_webp(image: Any, image_module: Any) -> Any:
    if image.mode in {"RGBA", "LA"}:
        background = image_module.new("RGBA", image.size, (255, 255, 255, 255))
        background.alpha_composite(image.convert("RGBA"))
        return background.convert("RGB")
    if image.mode != "RGB":
        return image.convert("RGB")
    return image


def resized(image: Any, max_width: int) -> Any:
    if image.width <= max_width:
        return image
    height = round(image.height * (max_width / image.width))
    return image.resize((max_width, height))


def save_webp(image: Any, output: Path, quality: int) -> None:
    image.save(output, "WEBP", quality=quality, method=6)


def main() -> None:
    args = parse_args()
    input_path = Path(args.image).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    if not input_path.is_file():
        raise SystemExit(f"Input image does not exist: {input_path}")
    if output_path.suffix.lower() != ".webp":
        raise SystemExit("Output path must end in .webp")
    if args.max_width < 640:
        raise SystemExit("--max-width must be at least 640")
    if not (20 <= args.quality <= 100):
        raise SystemExit("--quality must be between 20 and 100")

    Image = ensure_pillow(args.no_install)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    source = Image.open(input_path)
    image = flatten_for_webp(resized(source, args.max_width), Image)

    quality = args.quality
    width = image.width
    attempts: list[dict[str, int]] = []
    while True:
        candidate = resized(image, width)
        save_webp(candidate, output_path, quality)
        size = output_path.stat().st_size
        attempts.append({"width": candidate.width, "height": candidate.height, "quality": quality, "bytes": size})
        if size <= args.max_bytes:
            break
        if quality > 60:
            quality -= 8
            continue
        if width > 900:
            width = round(width * 0.85)
            quality = args.quality
            continue
        break

    payload = {
        "input": str(input_path),
        "output": str(output_path),
        "output_bytes": output_path.stat().st_size,
        "max_bytes": args.max_bytes,
        "attempts": attempts,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Compressed infographic: {output_path} ({payload['output_bytes']} bytes)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)

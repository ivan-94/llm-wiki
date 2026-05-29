from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


SCRIPT = Path(__file__).with_name("render_pdf_preview.py")


def create_pdf(path: Path, page_count: int) -> None:
    pages = []
    for _ in range(page_count):
        image = Image.new("RGB", (240, 320), color=(255, 255, 255))
        pages.append(image)
    first, rest = pages[0], pages[1:]
    first.save(path, save_all=True, append_images=rest)


class PdfPreviewHelperTest(unittest.TestCase):
    def test_outputs_first_three_pages_as_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            raw_root = tmp_path / "raw"
            wiki_root = tmp_path / "wiki"
            pdf_path = raw_root / "LLM" / "Long PDF.pdf"
            output_dir = wiki_root / "tmp" / "pdf-preview"
            pdf_path.parent.mkdir(parents=True)
            wiki_root.mkdir()
            create_pdf(pdf_path, page_count=5)

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(pdf_path),
                    "--raw-root",
                    str(raw_root),
                    "--wiki-root",
                    str(wiki_root),
                    "--output-dir",
                    str(output_dir),
                    "--json",
                ],
                check=True,
                text=True,
                capture_output=True,
            )

            payload = json.loads(result.stdout)
            self.assertEqual(payload["source_relpath"], "LLM/Long PDF.pdf")
            self.assertEqual(
                payload["target_source_note"],
                str((wiki_root / "sources/LLM/Long PDF.pdf.md").resolve()),
            )
            self.assertEqual(payload["target_source_note_relpath"], "sources/LLM/Long PDF.pdf.md")
            self.assertEqual(payload["page_count"], 5)
            self.assertEqual(payload["processed_pages"], [1, 2, 3])
            self.assertGreater(payload["raw_size"], 0)
            self.assertTrue(payload["raw_fingerprint"].startswith("size="))
            self.assertEqual(len(payload["rendered_pages"]), 3)
            for page in payload["rendered_pages"]:
                self.assertTrue(Path(page["image_path"]).is_file())


if __name__ == "__main__":
    unittest.main()

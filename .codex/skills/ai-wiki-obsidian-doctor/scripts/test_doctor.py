#!/usr/bin/env python3
import json
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("doctor.py")
SPEC = importlib.util.spec_from_file_location("doctor", SCRIPT)
doctor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(doctor)


def write_minimal_wiki(root: Path) -> None:
    (root / "index.md").write_text(
        "\n".join(
            [
                "# AI Wiki Index",
                "",
                "## Recently Updated",
                "",
                "## Source Coverage",
                "",
                "## Concepts",
                "",
                "## Entities",
                "",
                "## Synthesis",
                "",
                "## Maps",
                "",
                "## Questions",
                "",
                "## Outputs",
                "",
                "## Review Queue",
                "",
                "## Needs Attention",
                "",
            ]
        )
    )
    (root / "log.md").write_text(
        "## [2026-06-01] maintenance | doctor fixture — created fixture; issues: none\n"
    )


def run_doctor(root: Path, *args: str) -> dict:
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--wiki-root",
            str(root),
            "--skip-obsidian",
            "--json",
            *args,
        ],
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(result.stdout)


class ObsidianDoctorTests(unittest.TestCase):
    def test_clean_minimal_wiki_has_no_local_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_wiki(root)

            payload = run_doctor(root)

        self.assertEqual(payload["summary"], {"P0": 0, "P1": 0, "P2": 0, "total": 0})

    def test_reports_missing_index_sections_and_malformed_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.md").write_text("# AI Wiki Index\n\n## Concepts\n")
            (root / "log.md").write_text("## [2026-06-01] bad entry\n")

            payload = run_doctor(root)

        messages = [item["message"] for item in payload["findings"]]
        self.assertIn("缺少章节：Recently Updated", messages)
        self.assertIn("append-only log 记录格式错误", messages)
        self.assertEqual(payload["summary"]["P1"], 10)

    def test_reports_broken_path_style_wikilinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_wiki(root)
            (root / "concepts").mkdir()
            (root / "concepts" / "A.md").write_text("[[concepts/Missing]]\n[[Plain Name]]\n")

            payload = run_doctor(root)

        findings = payload["findings"]
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["severity"], "P1")
        self.assertEqual(findings[0]["category"], "wikilink")
        self.assertIn("[[concepts/Missing]]", findings[0]["message"])

    def test_noncanonical_broken_path_link_is_p2(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_wiki(root)
            (root / "human" / "inbox").mkdir(parents=True)
            (root / "human" / "inbox" / "draft.md").write_text("[[missing/thing]]\n")

            payload = run_doctor(root)

        self.assertEqual(payload["findings"][0]["severity"], "P2")

    def test_resolves_source_note_extension_mapping_and_ignores_placeholders(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_wiki(root)
            (root / "sources" / "Agent").mkdir(parents=True)
            (root / "sources" / "Agent" / "Map.xmind.md").write_text("# Map\n")
            (root / "concepts").mkdir()
            (root / "concepts" / "A.md").write_text(
                "[[sources/Agent/Map.xmind]]\n[[sources/<placeholder>]]\n"
            )

            payload = run_doctor(root)

        self.assertEqual(payload["findings"], [])

    def test_empty_obsidian_cli_messages_do_not_create_findings(self):
        results = [
            {"command": ["unresolved"], "ok": True, "stdout": "No unresolved links found.", "stderr": ""},
            {"command": ["orphans"], "ok": True, "stdout": "No orphan files found.", "stderr": ""},
            {"command": ["deadends"], "ok": True, "stdout": "No dead-end files found.", "stderr": ""},
        ]
        findings = []
        for result in results:
            stdout = result["stdout"].strip()
            if result["command"][0] == "unresolved" and stdout and stdout not in ("[]", "{}") and stdout not in doctor.EMPTY_CLI_MESSAGES:
                findings.append(result)
            if result["command"][0] in {"orphans", "deadends"} and stdout and stdout not in doctor.EMPTY_CLI_MESSAGES:
                findings.append(result)

        self.assertEqual(findings, [])

    def test_filters_noncanonical_cli_orphan_deadend_lines(self):
        stdout = "\n".join(
            [
                "_quickadd/scripts/inbox-workflow.js",
                "human/inbox/draft.md",
                "concepts/Useful Concept.md",
                "maps/Study Map.md",
            ]
        )

        self.assertEqual(
            doctor.canonical_cli_lines(stdout),
            ["concepts/Useful Concept.md", "maps/Study Map.md"],
        )


if __name__ == "__main__":
    unittest.main()

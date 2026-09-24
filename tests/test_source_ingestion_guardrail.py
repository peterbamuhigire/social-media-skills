from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_guardrail():
    path = ROOT / "scripts" / "source_ingestion_guardrail.py"
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SourceIngestionGuardrailTests(unittest.TestCase):
    def test_small_book_extraction_file_is_rejected(self):
        guardrail = load_guardrail()
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "book-extractions" / "short-summary.md"
            target.parent.mkdir(parents=True)
            target.write_text("A short book summary.", encoding="utf-8")
            codes = {finding.code for finding in guardrail.scan(Path(tmp))}
        self.assertIn("book-extraction-stored", codes)

    def test_skill_reference_is_allowed(self):
        guardrail = load_guardrail()
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "skills" / "advertising" / "media-planning" / "references" / "media-math.md"
            target.parent.mkdir(parents=True)
            target.write_text("Reach and frequency procedure.", encoding="utf-8")
            self.assertEqual([], guardrail.scan(Path(tmp)))

    def test_repository_holds_no_book_extractions(self):
        self.assertFalse((ROOT / "book-extractions").exists())


if __name__ == "__main__":
    unittest.main()

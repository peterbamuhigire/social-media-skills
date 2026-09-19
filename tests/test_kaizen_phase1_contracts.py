from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_runner():
    path = ROOT / "scripts" / "kaizen_phase1_contracts.py"
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class KaizenPhase1ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = load_runner()
        cls.fixture = json.loads((ROOT / "tests" / "fixtures" / "kaizen-phase1-contracts.json").read_text(encoding="utf-8"))

    def test_fixture_is_synthetic_and_all_cases_match(self):
        self.assertTrue(self.fixture["fixture_label"].startswith("FICTIONAL TEST DATA"))
        results = self.runner.run_fixture(ROOT / "tests" / "fixtures" / "kaizen-phase1-contracts.json")
        self.assertTrue(all(result["fixture_match"] for result in results), results)

    def test_unsupported_claim_is_blocked(self):
        result = self.runner.validate_content_unit(self.fixture["content_units"][1])
        self.assertEqual("BLOCKED", result["verdict"])
        self.assertTrue(any("unresolved" in issue for issue in result["issues"]))

    def test_missing_rights_is_blocked(self):
        result = self.runner.validate_content_unit(self.fixture["content_units"][2])
        self.assertEqual("BLOCKED", result["verdict"])
        self.assertTrue(any("not cleared" in issue for issue in result["issues"]))

    def test_display_name_and_locale_only_passes_with_native_review(self):
        result = self.runner.validate_identity(self.fixture["identities"][0])
        self.assertEqual("PASS", result["verdict"])
        self.assertEqual({"display_name", "locale"}, set(self.fixture["identities"][0]["identity"]))

    def test_missing_native_review_is_not_assessed(self):
        result = self.runner.validate_identity(self.fixture["identities"][1])
        self.assertEqual("NOT_ASSESSED", result["verdict"])

    def test_destination_mismatch_is_blocked(self):
        result = self.runner.validate_content_unit(self.fixture["content_units"][3])
        self.assertEqual("BLOCKED", result["verdict"])
        self.assertTrue(any("destination" in issue.lower() for issue in result["issues"]))

    def test_customer_voice_requires_denominator(self):
        result = self.runner.validate_experiment(self.fixture["experiments"][1])
        self.assertEqual("NOT_ASSESSED", result["verdict"])
        self.assertIn("sample denominator", result["not_assessed"])


if __name__ == "__main__":
    unittest.main()

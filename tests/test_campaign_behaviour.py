from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CampaignBehaviourTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads((ROOT / "tests" / "fixtures" / "campaign-behaviour.json").read_text(encoding="utf-8"))
        cls.runner = load_script("campaign_behaviour.py")

    def test_fixture_is_explicitly_fictional(self):
        self.assertTrue(self.fixture["fixture_label"].startswith("FICTIONAL TEST DATA"))
        self.assertEqual("brief -> calendar -> approval -> evidence -> report", self.fixture["workflow"])

    def test_complete_case_traces_each_stage(self):
        result = self.runner.evaluate_case(self.fixture["cases"][0])
        self.assertEqual("PASS", result["verdict"])
        self.assertTrue(result["fixture_match"])
        self.assertEqual({stage: "pass" for stage in self.runner.STAGES}, result["stage_results"])

    def test_missing_approval_blocks_report(self):
        result = self.runner.evaluate_case(self.fixture["cases"][1])
        self.assertEqual("BLOCKED", result["verdict"])
        self.assertTrue(result["fixture_match"])
        self.assertEqual("blocked", result["stage_results"]["approval"])
        self.assertEqual("blocked", result["stage_results"]["report"])
        self.assertFalse(self.fixture["cases"][1]["report"]["publish_authority"])
        self.assertIn("Approval evidence and any publication decision", self.fixture["cases"][1]["report"]["not_assessed"])

    def _mutated_complete_case(self):
        case = copy.deepcopy(self.fixture["cases"][0])
        case["expected_verdict"] = "BLOCKED"
        return case

    def test_missing_evidence_blocks_at_evidence_gate(self):
        case = self._mutated_complete_case()
        case["evidence"]["source_records"] = []
        case["evidence"]["metrics"] = []

        result = self.runner.evaluate_case(case)

        self.assertEqual("BLOCKED", result["verdict"])
        self.assertTrue(result["fixture_match"])
        self.assertEqual(["missing-evidence"], result["blocking_reasons"])
        self.assertEqual("blocked", result["stage_results"]["evidence"])
        self.assertEqual("blocked", result["stage_results"]["report"])
        self.assertTrue(any("source_records" in issue for issue in result["issues"]))

    def test_approval_campaign_mismatch_blocks_at_approval_gate(self):
        case = self._mutated_complete_case()
        case["approval"]["campaign_id"] = "TEST-CAMPAIGN-WRONG"

        result = self.runner.evaluate_case(case)

        self.assertEqual("BLOCKED", result["verdict"])
        self.assertTrue(result["fixture_match"])
        self.assertEqual(["approval-campaign-mismatch"], result["blocking_reasons"])
        self.assertEqual("blocked", result["stage_results"]["approval"])
        self.assertEqual("blocked", result["stage_results"]["report"])
        self.assertTrue(any("approval.campaign_id" in issue for issue in result["issues"]))

    def test_report_calendar_mismatch_blocks_at_report_gate(self):
        case = self._mutated_complete_case()
        case["report"]["calendar_entry_ids"] = ["TEST-POST-001"]

        result = self.runner.evaluate_case(case)

        self.assertEqual("BLOCKED", result["verdict"])
        self.assertTrue(result["fixture_match"])
        self.assertEqual(["report-calendar-inconsistency"], result["blocking_reasons"])
        self.assertEqual("blocked", result["stage_results"]["report"])
        self.assertTrue(any("calendar_entry_ids" in issue for issue in result["issues"]))

    def test_malformed_brief_does_not_crash_and_is_blocked(self):
        case = self._mutated_complete_case()
        case["brief"] = None

        result = self.runner.evaluate_case(case)

        self.assertEqual("BLOCKED", result["verdict"])
        self.assertEqual("blocked", result["stage_results"]["brief"])
        self.assertIn("missing-stage", result["blocking_reasons"])


if __name__ == "__main__":
    unittest.main()

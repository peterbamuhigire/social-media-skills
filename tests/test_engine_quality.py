from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


class EngineQualityTests(unittest.TestCase):
    def test_zero_debt_baseline_has_no_waivers(self):
        baseline = json.loads((ROOT / "quality-baseline.json").read_text(encoding="utf-8"))
        self.assertEqual({}, baseline["failure_counts"])
        self.assertEqual(176, baseline["active_skill_count"])

    def test_fixture_types_cover_release_paths(self):
        fixtures = json.loads((ROOT / "tests" / "routing-fixtures.json").read_text(encoding="utf-8"))["fixtures"]
        types = {fixture["type"] for fixture in fixtures}
        self.assertTrue({"positive", "collision", "limited-capability", "failure-path"}.issubset(types))

    def test_router_catalogue_matches_active_catalogue(self):
        routing = load_script("routing_smoke_test.py")
        active = list((ROOT / "skills").rglob("SKILL.md"))
        self.assertEqual(len(active), len(routing.catalogue()))


if __name__ == "__main__":
    unittest.main()

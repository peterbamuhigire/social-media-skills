from __future__ import annotations

import importlib.util
import json
import re
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
        self.assertEqual(177, baseline["active_skill_count"])

    def test_fixture_types_cover_release_paths(self):
        fixtures = json.loads((ROOT / "tests" / "routing-fixtures.json").read_text(encoding="utf-8"))["fixtures"]
        types = {fixture["type"] for fixture in fixtures}
        self.assertTrue({"positive", "collision", "limited-capability", "failure-path"}.issubset(types))

    def test_router_catalogue_matches_active_catalogue(self):
        routing = load_script("routing_smoke_test.py")
        active = list((ROOT / "skills").rglob("SKILL.md"))
        self.assertEqual(len(active), len(routing.catalogue()))

    def test_source_register_is_current_at_release_date(self):
        freshness = load_script("check_source_freshness.py")
        from datetime import date
        errors = freshness.validate(
            ROOT / "docs" / "source-registers" / "source-register.json",
            date(2026, 7, 13),
        )
        self.assertEqual([], errors)

    def test_source_register_rejects_overdue_records(self):
        freshness = load_script("check_source_freshness.py")
        from datetime import date
        errors = freshness.validate(
            ROOT / "docs" / "source-registers" / "source-register.json",
            date(2026, 9, 18),
        )
        self.assertTrue(any("overdue" in error for error in errors))

    def test_capability_assets_cover_the_closed_gaps(self):
        expected = (
            "docs/source-registers/source-register.json",
            "docs/quality-gates/creative-review-gate.md",
            "docs/quality-gates/legal-market-release-gate.md",
            "docs/evidence-packs/measurement-proof-pack.md",
            "docs/world-class-exemplars/campaign-exemplars.md",
        )
        for relative in expected:
            path = ROOT / relative
            self.assertTrue(path.is_file(), relative)
            self.assertGreater(len(path.read_text(encoding="utf-8").strip()), 500, relative)

        campaigns = (ROOT / "docs/world-class-exemplars/campaign-exemplars.md").read_text(encoding="utf-8")
        for sector in ("B2B", "NGO", "Retail", "Public sector", "Creator"):
            self.assertIn(sector, campaigns)

    def test_active_routes_do_not_advertise_absent_deck_taxonomy(self):
        active_sources = [ROOT / name for name in ("AGENTS.md", "CLAUDE.md", "README.md")]
        active_sources.extend(ROOT.joinpath("skills").rglob("SKILL.md"))
        active_text = "\n".join(path.read_text(encoding="utf-8") for path in active_sources)
        self.assertNotRegex(active_text, r"\bdeck-[a-z0-9-]+\b")
        self.assertNotIn("skills/decks/", active_text)

    def test_all_repository_markdown_links_resolve_or_are_external(self):
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        schemes = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts or "__pycache__" in path.parts:
                continue
            for target in link_pattern.findall(path.read_text(encoding="utf-8")):
                target = target.split("#", 1)[0].strip()
                if not target or target.startswith("//") or schemes.match(target):
                    continue
                self.assertTrue(
                    (path.parent / target).resolve().exists(),
                    f"broken local link in {path.relative_to(ROOT)}: {target}",
                )


if __name__ == "__main__":
    unittest.main()

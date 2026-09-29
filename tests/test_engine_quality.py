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

    def test_active_count_agrees_and_respects_cap(self):
        # S01-T09: the count is no longer hard-coded. quality-baseline.json, the alias
        # registry and the filesystem must agree, and the count must be within hard_cap
        # unless the registry declares the consolidation window (removed in S07).
        import yaml
        baseline = json.loads((ROOT / "quality-baseline.json").read_text(encoding="utf-8"))
        registry = yaml.safe_load((ROOT / "docs" / "skill-aliases.yml").read_text(encoding="utf-8"))
        policy = registry["active_skill_policy"]
        active = len(list((ROOT / "skills").rglob("SKILL.md")))
        self.assertEqual(active, baseline["active_skill_count"])
        self.assertEqual(active, policy["current_active_skill_count"])
        if active > policy["hard_cap"]:
            self.assertTrue(policy.get("consolidation_until"), "active count exceeds hard_cap outside a consolidation window")

    def test_validator_flags_alias_links_and_cap(self):
        # S01-T07 synthetic negatives: links to a retired alias, and a cap breach.
        import subprocess
        import sys
        import tempfile
        import yaml
        validator = load_script("validate_skill_engine.py")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            owner = root / "skills" / "cat" / "owner"
            retired = root / "skills" / "cat" / "retired"
            owner.mkdir(parents=True)
            retired.mkdir(parents=True)
            (retired / "ALIAS.md").write_text("---\nname: retired\n---\n\n> Inactive alias.\n", encoding="utf-8")
            (retired / "notes.md").write_text("old\n", encoding="utf-8")
            linked = owner / "SKILL.md"
            folders = validator.retired_dirs(root, ["skills"])
            linked.write_text("# Owner\n\n[old](../retired/ALIAS.md)\n", encoding="utf-8")
            self.assertTrue(validator.links_to_alias(linked, root, folders))
            linked.write_text("# Owner\n\n[notes](../retired/notes.md)\n", encoding="utf-8")
            self.assertTrue(validator.links_to_alias(linked, root, folders))
            linked.write_text("# Owner\n\nNo retired links.\n", encoding="utf-8")
            self.assertFalse(validator.links_to_alias(linked, root, folders))
            # S03-T08: a category-level alias keeps its active child skills and shared references live.
            category = root / "skills" / "cat"
            (owner / "SKILL.md").write_text("---\nname: owner\n---\n", encoding="utf-8")
            (category / "ALIAS.md").write_text("---\nname: cat\n---\n\n> Inactive alias.\n", encoding="utf-8")
            (category / "references").mkdir()
            (category / "references" / "shared.md").write_text("shared\n", encoding="utf-8")
            folders = validator.retired_dirs(root, ["skills"])
            self.assertNotIn(category.resolve(), folders)
            self.assertIn(retired.resolve(), folders)
            linked.write_text("# Owner\n\n[shared](../references/shared.md)\n", encoding="utf-8")
            self.assertFalse(validator.links_to_alias(linked, root, folders))
            linked.write_text("# Owner\n\n[category](../ALIAS.md)\n", encoding="utf-8")
            self.assertTrue(validator.links_to_alias(linked, root, folders))
            linked.write_text("# Owner\n\n[notes](../retired/notes.md)\n", encoding="utf-8")
            self.assertTrue(validator.links_to_alias(linked, root, folders))
            (category / "ALIAS.md").unlink()
            (root / "docs").mkdir()
            registry = root / "docs" / "skill-aliases.yml"
            registry.write_text(yaml.safe_dump({"active_skill_policy": {"hard_cap": 0}}), encoding="utf-8")
            command = [sys.executable, "-X", "utf8", str(ROOT / "scripts" / "validate_skill_engine.py"), "--root", str(root), "--json"]
            payload = json.loads(subprocess.run(command, capture_output=True, text=True, encoding="utf-8").stdout)
            self.assertIn("catalogue_cap_exceeded", payload)
            registry.write_text(yaml.safe_dump({"active_skill_policy": {"hard_cap": 0, "consolidation_until": "S07"}}), encoding="utf-8")
            payload = json.loads(subprocess.run(command, capture_output=True, text=True, encoding="utf-8").stdout)
            self.assertNotIn("catalogue_cap_exceeded", payload)
            self.assertIn("catalogue_cap", payload)

    def test_fixture_types_cover_release_paths(self):
        fixtures = json.loads((ROOT / "tests" / "routing-fixtures.json").read_text(encoding="utf-8"))["fixtures"]
        types = {fixture["type"] for fixture in fixtures}
        self.assertTrue({"positive", "collision", "limited-capability", "failure-path"}.issubset(types))

    def test_router_catalogue_matches_active_catalogue(self):
        routing = load_script("routing_smoke_test.py")
        active = list((ROOT / "skills").rglob("SKILL.md"))
        self.assertEqual(len(active), len(routing.catalogue()))

    def test_source_register_window_at_observed_audit_date(self):
        freshness = load_script("check_source_freshness.py")
        from datetime import date
        errors = freshness.validate(
            ROOT / "docs" / "source-registers" / "source-register.json",
            # The mutable register now includes verifications through the
            # current audit date.
            # Separate synthetic tests reject future-dated verification.
            date(2026, 9, 29),
        )
        self.assertEqual([], errors)

    def test_source_register_rejects_overdue_records(self):
        freshness = load_script("check_source_freshness.py")
        from datetime import date
        errors = freshness.validate(
            ROOT / "docs" / "source-registers" / "source-register.json",
            date(2026, 10, 20),
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
            # Vendored dependency trees are third-party content, not engine documentation.
            if {".git", "__pycache__", "node_modules"} & set(path.parts):
                continue
            # Retired aliases keep their historical text verbatim (D-SK-03); their old
            # references/ links move to the owner, so they are not live navigation.
            if path.name == "ALIAS.md":
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

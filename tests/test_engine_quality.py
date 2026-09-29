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



def count_surface_findings(root: Path) -> list[str]:
    """S12-T07: README, marketplace and plugin surfaces must state the filesystem catalogue.

    Portfolio precedent: test_current_active_count_matches_filesystem_and_documented_surfaces.
    """
    import yaml
    findings: list[str] = []
    active = sorted(path.parent for path in (root / "skills").rglob("SKILL.md"))
    total = len(active)
    readme = (root / "README.md").read_text(encoding="utf-8")
    if f"{total} active `SKILL.md` files" not in readme:
        findings.append(f"README capability sentence does not state {total} active skills")
    if f"| **Total** | **{total}** |" not in readme:
        findings.append(f"README category table total is not {total}")
    for category, size in sorted({p.parent.name: 0 for p in active}.items()):
        size = sum(1 for p in active if p.parent.name == category)
        if f"| `{category}` | {size} |" not in readme:
            findings.append(f"README category row for {category} is not {size}")
    if f"library of {total} routed skills" not in readme:
        findings.append(f"README executive summary does not state {total} routed skills")
    listed = set(re.findall(r"^\| `([^`/]+)` \| `([^`/]+)` \| ", readme, re.M))
    expected = {(p.parent.name, p.name) for p in active}
    if listed != expected:
        findings.append(f"README skill table differs from the filesystem: {sorted(listed ^ expected)}")
    routes = (yaml.safe_load((root / "docs" / "skill-aliases.yml").read_text(encoding="utf-8")) or {}).get("inactive_skill_aliases") or {}
    wanted = {(src.replace("skills/", "", 1), dst.replace("skills/", "", 1)) for src, dst in routes.items()}
    retired = set()
    for source, owner in re.findall(r"^\| `([^`]+)`(?: \(former category standards file\))? \| `([^`]+/[^`]+)` \|$", readme, re.M):
        retired.add((source, owner))
    if retired != wanted:
        findings.append(f"README retired-route table differs from docs/skill-aliases.yml: {sorted(retired ^ wanted)}")
    marketplace = json.loads((root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    description = marketplace["plugins"][0]["description"]
    if not description.startswith(f"{total} skills "):
        findings.append(f"marketplace description does not start with '{total} skills'")
    plugin = json.loads((root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    declared = {entry.strip("./").rstrip("/") for entry in plugin["skills"]}
    if declared != {path.relative_to(root).as_posix() for path in active}:
        findings.append("plugin.json skills list differs from the active catalogue")
    return findings


class EngineQualityTests(unittest.TestCase):
    def test_zero_debt_baseline_has_no_waivers(self):
        baseline = json.loads((ROOT / "quality-baseline.json").read_text(encoding="utf-8"))
        self.assertEqual({}, baseline["failure_counts"])

    def test_active_count_agrees_and_respects_cap(self):
        # S01-T09: the count is no longer hard-coded. quality-baseline.json, the alias
        # registry and the filesystem must agree, and the count must be within hard_cap
        # strictly: the S02-S07 consolidation window was removed in S07 (S07-T-CAP).
        import yaml
        baseline = json.loads((ROOT / "quality-baseline.json").read_text(encoding="utf-8"))
        registry = yaml.safe_load((ROOT / "docs" / "skill-aliases.yml").read_text(encoding="utf-8"))
        policy = registry["active_skill_policy"]
        active = len(list((ROOT / "skills").rglob("SKILL.md")))
        self.assertEqual(active, baseline["active_skill_count"])
        self.assertEqual(active, policy["current_active_skill_count"])
        # S07-T-CAP: the consolidation window is closed; the cap is enforced strictly.
        self.assertNotIn("consolidation_until", policy, "the S02-S07 consolidation window closed in S07")
        self.assertLessEqual(active, policy["hard_cap"], "active count exceeds hard_cap")

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
            # S08: the dormant `consolidation_until` branch was removed; a re-added key no longer
            # tolerates a cap breach.
            registry.write_text(yaml.safe_dump({"active_skill_policy": {"hard_cap": 0, "consolidation_until": "S07"}}), encoding="utf-8")
            payload = json.loads(subprocess.run(command, capture_output=True, text=True, encoding="utf-8").stdout)
            self.assertIn("catalogue_cap_exceeded", payload)
            self.assertNotIn("catalogue_cap", payload)

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

    def test_current_active_count_matches_filesystem_and_documented_surfaces(self):
        # S12-T07 (portfolio precedent of the same name): README tables, the retired-route table,
        # the marketplace description and plugin.json must state the filesystem catalogue.
        self.assertEqual([], count_surface_findings(ROOT))

    def test_count_surface_check_fails_on_a_mutated_count(self):
        import shutil
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "skills", root / "skills", ignore=shutil.ignore_patterns("references", "scripts", "assets"))
            (root / "docs").mkdir()
            shutil.copy2(ROOT / "docs" / "skill-aliases.yml", root / "docs" / "skill-aliases.yml")
            shutil.copytree(ROOT / ".claude-plugin", root / ".claude-plugin")
            readme = (ROOT / "README.md").read_text(encoding="utf-8")
            (root / "README.md").write_text(readme, encoding="utf-8")
            self.assertEqual([], count_surface_findings(root))
            active = len(list((ROOT / "skills").rglob("SKILL.md")))
            mutated = readme.replace(f"| **Total** | **{active}** |", f"| **Total** | **{active + 1}** |")
            (root / "README.md").write_text(mutated, encoding="utf-8")
            self.assertTrue(any("category table total" in f for f in count_surface_findings(root)))
            (root / "README.md").write_text(readme, encoding="utf-8")
            marketplace = root / ".claude-plugin" / "marketplace.json"
            marketplace.write_text(marketplace.read_text(encoding="utf-8").replace(f'"{active} skills ', f'"{active - 1} skills '), encoding="utf-8")
            self.assertTrue(any("marketplace" in f for f in count_surface_findings(root)))


if __name__ == "__main__":
    unittest.main()

"""Tests for scripts/check_skill_aliases.py (Social Kaizen 2026-09-29, S01-T06).

One positive case and one synthetic negative case per finding, each built in a temporary
directory so the live catalogue is never touched.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_skill_aliases", ROOT / "scripts" / "check_skill_aliases.py")
aliases = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = aliases  # dataclasses resolve the module by name
SPEC.loader.exec_module(aliases)

FRONT = "---\nname: {name}\ndescription: Use when testing.\n---\n"


class AliasCheckerTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for name in ("owner", "retired"):
            self.skill(name)
        self.retire("retired", "skills/cat/owner")
        self.routes = {"skills/cat/retired": "skills/cat/owner"}
        self.policy = {"active_roots": ["skills"], "hard_cap": 5, "current_active_skill_count": 1}
        self.write_registry()
        self.write_baseline(1)

    def tearDown(self):
        self._tmp.cleanup()

    def skill(self, name: str) -> Path:
        folder = self.root / "skills" / "cat" / name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "SKILL.md").write_text(FRONT.format(name=name) + "# Title\n", encoding="utf-8")
        return folder

    def retire(self, name: str, target: str, banner: bool = True) -> None:
        folder = self.root / "skills" / "cat" / name
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        (folder / "SKILL.md").unlink()
        head, body = text.split("---\n# ", 1)
        line = f"> Inactive alias. Route to {target} through docs/skill-aliases.yml.\n\n" if banner else ""
        (folder / "ALIAS.md").write_text(head + "---\n\n" + line + "# " + body, encoding="utf-8")

    def write_registry(self) -> None:
        path = self.root / "docs" / "skill-aliases.yml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump({
            "version": 1,
            "active_skill_policy": self.policy,
            "inactive_alias_file": "ALIAS.md",
            "inactive_skill_aliases": self.routes,
        }), encoding="utf-8")

    def write_baseline(self, count: int) -> None:
        (self.root / "quality-baseline.json").write_text(json.dumps({"active_skill_count": count}), encoding="utf-8")

    def codes(self) -> set[str]:
        findings, _ = aliases.check(self.root)
        return {finding.code for finding in findings}

    def test_positive_routed_alias_is_clean(self):
        self.assertEqual(set(), self.codes())

    def test_live_catalogue_is_clean(self):
        findings, stats = aliases.check(ROOT)
        self.assertEqual([], findings)
        self.assertEqual(120, stats["cap"])

    def test_unrouted_alias(self):
        self.routes = {}
        self.write_registry()
        self.assertIn("alias-unrouted", self.codes())

    def test_stale_route(self):
        self.routes["skills/cat/ghost"] = "skills/cat/owner"
        self.write_registry()
        self.assertIn("alias-stale", self.codes())

    def test_dangling_target(self):
        self.routes["skills/cat/retired"] = "skills/cat/missing"
        self.write_registry()
        self.assertIn("alias-dangling", self.codes())

    def test_chain_target(self):
        self.skill("middle")
        self.retire("middle", "skills/cat/owner")
        self.routes["skills/cat/middle"] = "skills/cat/owner"
        self.routes["skills/cat/retired"] = "skills/cat/middle"
        self.write_registry()
        self.assertIn("alias-chain", self.codes())

    def test_banner_missing(self):
        self.skill("quiet")
        self.retire("quiet", "skills/cat/owner", banner=False)
        self.routes["skills/cat/quiet"] = "skills/cat/owner"
        self.write_registry()
        self.assertIn("alias-banner-missing", self.codes())

    def test_banner_naming_a_different_target(self):
        self.skill("owner-x")
        self.skill("misnamed")
        self.retire("misnamed", "skills/cat/owner-x")
        self.routes["skills/cat/misnamed"] = "skills/cat/owner"
        self.policy["current_active_skill_count"] = 2
        self.write_registry()
        self.write_baseline(2)
        self.assertIn("alias-banner-missing", self.codes())

    def test_cap_exceeded_outside_window(self):
        self.policy["hard_cap"] = 1
        for name in ("extra-a", "extra-b"):
            self.skill(name)
        self.policy["current_active_skill_count"] = 3
        self.write_registry()
        self.write_baseline(3)
        self.assertIn("cap-exceeded", self.codes())

    def test_removed_consolidation_window_no_longer_relaxes_the_cap(self):
        # S08: the S02-S07 `consolidation_until` branch was removed; a re-added key is ignored.
        self.policy.update(hard_cap=1, consolidation_until="S07", current_active_skill_count=3)
        for name in ("extra-a", "extra-b"):
            self.skill(name)
        self.write_registry()
        self.write_baseline(3)
        self.assertIn("cap-exceeded", self.codes())
        _, stats = aliases.check(self.root)
        self.assertNotIn("window", stats)

    def test_count_mismatch(self):
        self.write_baseline(2)
        self.assertIn("count-mismatch", self.codes())

    def test_active_conflict(self):
        (self.root / "skills" / "cat" / "retired" / "SKILL.md").write_text(FRONT.format(name="retired"), encoding="utf-8")
        self.policy["current_active_skill_count"] = 2
        self.write_registry()
        self.write_baseline(2)
        self.assertIn("alias-active-conflict", self.codes())

    def test_missing_registry(self):
        (self.root / "docs" / "skill-aliases.yml").unlink()
        self.assertEqual({"alias-registry"}, self.codes())


if __name__ == "__main__":
    unittest.main()

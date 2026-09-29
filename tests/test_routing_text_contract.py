"""S08 routing-text contract (Social Kaizen 2026-09-29).

Covers the validator findings `description_template`, `description_formula` and
`use_when_template`, the fixture lint for slug leaks and routing-text copies, and the live
fixture coverage rule: every active skill has a positive fixture and an owned negative that
proves its description's "not for" clause.
"""

from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_script("validate_skill_engine.py")
ROUTING = load_script("routing_smoke_test.py")

GOOD_DESCRIPTION = (
    "Use when an approved brief needs publish-ready social captions and hashtags; produces caption sets "
    "with alt text; not for paid ad headlines or hooks (use `ad-copy-and-hook-lab`)."
)
GOOD_USE_WHEN = "- We need captions for next week's posts.\n- Our hashtags are random.\n- The client wants alt text.\n"
GOOD_DO_NOT = "- `ad-copy-and-hook-lab` for paid ad lines.\n- `email-copywriter` for emails.\n- Stop before publishing.\n"


class TemplateFindingTests(unittest.TestCase):
    def test_formula_compliant_text_is_clean(self):
        self.assertEqual([], VALIDATOR.template_findings(GOOD_DESCRIPTION, GOOD_USE_WHEN, GOOD_DO_NOT))

    def test_description_template_fires_on_each_template(self):
        for template in (
            "Use when Caption Writer is needed to produce a publication-ready copy; produces x; not for y (use `z`).",
            "Use when designing or improving a Crisis operating playbook with roles, ordered actions; produces x; not for y (use `z`).",
            "Use when creating a Instagram channel plan covering account setup; produces x; not for y (use `z`).",
            "Use when the main deliverable concerns healthcare trust; produces x; not for y (use `z`).",
        ):
            self.assertIn("description_template", VALIDATOR.template_findings(template, GOOD_USE_WHEN, GOOD_DO_NOT), template)

    def test_description_formula_needs_artefact_and_neighbour(self):
        self.assertIn("description_formula", VALIDATOR.template_findings("Use when writing captions.", GOOD_USE_WHEN, GOOD_DO_NOT))
        self.assertIn("description_formula", VALIDATOR.template_findings(
            "Use when writing captions; produces captions; use email-copywriter for email.", GOOD_USE_WHEN, GOOD_DO_NOT))

    def test_use_when_template_fires(self):
        templated = (
            "- Use this skill when the requested outcome is specifically a **publication-ready copy**.\n"
            "- Build or improve a repeatable PR workflow.\n- Another trigger.\n"
        )
        self.assertIn("use_when_template", VALIDATOR.template_findings(GOOD_DESCRIPTION, templated, GOOD_DO_NOT))
        too_few = "- Only one trigger.\n"
        self.assertIn("use_when_template", VALIDATOR.template_findings(GOOD_DESCRIPTION, too_few, GOOD_DO_NOT))
        one_neighbour = "- `ad-copy-and-hook-lab` for paid ad lines.\n- Stop before publishing.\n"
        self.assertIn("use_when_template", VALIDATOR.template_findings(GOOD_DESCRIPTION, GOOD_USE_WHEN, one_neighbour))
        generic = "- The task is a single-channel presence plan; use the closest `platform-*` skill.\n- `a-b` x.\n- `c-d` y.\n"
        self.assertIn("use_when_template", VALIDATOR.template_findings(GOOD_DESCRIPTION, GOOD_USE_WHEN, generic))


class NeighbourFindingTests(unittest.TestCase):
    def test_unknown_neighbours_are_flagged(self):
        import subprocess
        import sys
        import tempfile

        skill = (
            "---\nname: {name}\ndescription: 'Use when x; produces y; not for z (use `{neighbour}`).'\n---\n# T\n\n"
            "## Use When\n- a\n- b\n- c\n\n## Do Not Use When\n- `{neighbour}` for z.\n- `{other}` for w.\n- `website-skills` builds sites.\n- Stop.\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, neighbour, other in (("alpha-one", "beta-two", "beta-two"), ("beta-two", "gamma-gone", "delta-gone")):
                folder = root / "skills" / "cat" / name
                folder.mkdir(parents=True)
                (folder / "SKILL.md").write_text(skill.format(name=name, neighbour=neighbour, other=other), encoding="utf-8")
            command = [sys.executable, "-X", "utf8", str(ROOT / "scripts" / "validate_skill_engine.py"), "--root", str(root), "--json"]
            results = json.loads(subprocess.run(command, capture_output=True, text=True, encoding="utf-8").stdout)["results"]
        alpha = results.get("skills/cat/alpha-one/SKILL.md", [])
        beta = results.get("skills/cat/beta-two/SKILL.md", [])
        self.assertNotIn("description_neighbour_unknown", alpha)
        self.assertNotIn("do_not_use_neighbour_unknown", alpha)  # engine ids such as `website-skills` are skipped
        self.assertIn("description_neighbour_unknown", beta)
        self.assertIn("do_not_use_neighbour_unknown", beta)


class FixtureLintTests(unittest.TestCase):
    def test_slug_in_prompt_is_flagged(self):
        findings = ROUTING.prompt_leaks("Use the caption writer to draft three captions", "caption-writer", GOOD_DESCRIPTION)
        self.assertTrue(any(f.startswith("slug-in-prompt") for f in findings))
        findings = ROUTING.prompt_leaks("Build our content calendar for March", "11-content-calendar", "")
        self.assertTrue(any(f.startswith("slug-in-prompt") for f in findings))

    def test_routing_text_copy_is_flagged(self):
        copied = "an approved brief needs publish-ready social captions and hashtags"
        self.assertTrue(any("copy" in f for f in ROUTING.prompt_leaks(copied, "caption-writer", GOOD_DESCRIPTION)))

    def test_natural_prompt_is_clean(self):
        natural = "We post on Instagram and TikTok every day; write next week's posts with a strong first line"
        self.assertEqual([], ROUTING.prompt_leaks(natural, "caption-writer", GOOD_DESCRIPTION))


class LiveFixtureCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "tests" / "routing-fixtures.json").read_text(encoding="utf-8"))
        cls.fixtures = cls.data["fixtures"]
        cls.descriptions = {}
        for path in (ROOT / "skills").rglob("SKILL.md"):
            front = yaml.safe_load(re.match(r"(?s)^---\n(.*?)\n---\n", path.read_text(encoding="utf-8")).group(1))
            cls.descriptions[front["name"]] = front["description"]

    def test_size_and_collision_floor(self):
        self.assertGreaterEqual(len(self.fixtures), 150)
        self.assertGreaterEqual(sum(f["type"] == "collision" for f in self.fixtures), 40)

    def test_every_active_skill_has_a_positive_fixture(self):
        covered = {f["expected"] for f in self.fixtures if f["type"] != "collision"}
        self.assertEqual([], sorted(set(self.descriptions) - covered))

    def test_every_not_for_clause_has_an_owned_negative(self):
        owned = {(f.get("negative_for"), f["expected"]) for f in self.fixtures if f.get("negative_for")}
        missing = []
        for name, description in self.descriptions.items():
            neighbour = VALIDATOR.DESCRIPTION_NEIGHBOUR.search(description)
            if not neighbour or (name, neighbour.group(1)) not in owned:
                missing.append(name)
        self.assertEqual([], sorted(missing))

    def test_floor_is_registered(self):
        self.assertGreaterEqual(self.data["p1_floor"], 0.92)


if __name__ == "__main__":
    unittest.main()

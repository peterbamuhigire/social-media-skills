from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AntiSlopOverlayTests(unittest.TestCase):
    def test_machine_error_and_accessibility_ids_are_at_skill_entrypoint(self):
        skill = (ROOT / "skills/ai-marketing/anti-ai-slop/SKILL.md").read_text(encoding="utf-8")
        reference = (ROOT / "skills/ai-marketing/anti-ai-slop/references/guardrails-and-overlays.md").read_text(encoding="utf-8")
        for identifier in [*(f"| ME{number} |" for number in range(1, 8)),
                           *(f"| AS{number} |" for number in range(1, 8))]:
            with self.subTest(identifier=identifier):
                self.assertIn(identifier, skill)
                self.assertIn(identifier, reference)
        self.assertIn("NOT_ASSESSED", skill)
        self.assertIn("reduced motion", skill)


if __name__ == "__main__":
    unittest.main()

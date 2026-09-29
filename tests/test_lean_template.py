"""S09 lean-template contract (Social Kaizen 2026-09-29, D-SK-06).

Covers the `line_budget` validator finding (300 lines), a lean skill written to the template
passing every validator contract, the shared-line meter (`scripts/measure_skill_scaffolding.py`),
and the live budgets: every active skill at or below 300 lines, a median at or below 200 and a
gated shared-line median at or below 12 %.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_script("validate_skill_engine.py")
METER = load_script("measure_skill_scaffolding.py")

CAPABILITY = METER.CANONICAL_SENTENCES[0]

LEAN_SKILL = f"""---
name: lean-sample
description: 'Use when a client needs dated posts for next quarter; produces the 90-day calendar; not for the weekly production workflow (use `other-skill`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Lean Sample

Plans the quarter's posts for the client lead.

<!-- dual-compat-start -->
## Use When

- The client wants next quarter's posts dated.
- Holidays must be in the plan.
- Campaign weeks need blocking out.

## Do Not Use When

- `other-skill` for the weekly production workflow.
- `third-skill` for website articles.
- Stop before scheduling posts in a live tool.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Approved pillars | Client sign-off | Yes | Stop and ask for them. |

## Workflow

1. Confirm the pillars; stop if they are not approved.
2. Place campaign and holiday weeks first.
3. Sample rows, correct any systematic error and rerun the sample.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| 90-day calendar | Client lead | Every row has a specific headline. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Sampling record | Table | A clean round is recorded. |

## Capability and Permission Boundaries

{CAPABILITY}

## Degraded Mode

Without approved pillars, return the narrowest qualified result and mark the affected checks `not assessed`. A dated grid can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A campaign overlaps always-on posts | Let the campaign lead | Mixed messages |

## Quality Standards

- No placeholder rows.

## Anti-Patterns

- Generic observance posts. Fix: write to the occasion.
- Reusing last year's dates. Fix: confirm this year's dates.
- Pasting one caption everywhere. Fix: vary per platform.
- Sampling one month only. Fix: spread the sample.
- Scheduling in a live tool. Fix: hand over for approval.

## References

- [Build method](references/build-method.md): read when laying out the tables.
<!-- dual-compat-end -->
"""


class LineBudgetTests(unittest.TestCase):
    def write_skill(self, root: Path, text: str) -> Path:
        folder = root / "skills" / "cat" / "lean-sample"
        (folder / "references").mkdir(parents=True)
        (folder / "references" / "build-method.md").write_text("# Build method\n", encoding="utf-8")
        path = folder / "SKILL.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_lean_skill_passes_every_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_skill(Path(tmp), LEAN_SKILL)
            self.assertEqual([], VALIDATOR.assess(path, Path(tmp)))

    def test_line_budget_fires_above_300_lines_only(self):
        body_lines = len(LEAN_SKILL.splitlines())
        at_budget = LEAN_SKILL + "\n" * (VALIDATOR.LINE_BUDGET - body_lines)
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_skill(Path(tmp), at_budget)
            self.assertNotIn("line_budget", VALIDATOR.assess(path, Path(tmp)))
            path.write_text(at_budget + "\n", encoding="utf-8")
            self.assertIn("line_budget", VALIDATOR.assess(path, Path(tmp)))

    def test_budget_is_300(self):
        self.assertEqual(300, VALIDATOR.LINE_BUDGET)


class ScaffoldingMeterTests(unittest.TestCase):
    def build(self, root: Path, shared_in: int, total: int) -> None:
        for index in range(total):
            folder = root / "skills" / "cat" / f"skill-{index}"
            folder.mkdir(parents=True)
            lines = ["---", f"name: skill-{index}", "---", "## Use When", CAPABILITY, f"unique line {index} a", f"unique line {index} b"]
            if index < shared_in:
                lines.append("Apply the domain method in the core sections below.")
            (folder / "SKILL.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def test_allow_listed_lines_do_not_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.build(Path(tmp), shared_in=0, total=20)
            report = METER.measure(Path(tmp))
            self.assertEqual(0.0, report["gated_median_pct"])
            self.assertGreater(report["raw_median_pct"], 0.0)

    def test_repeated_prose_counts_and_budget_exit_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.build(Path(tmp), shared_in=20, total=20)
            report = METER.measure(Path(tmp))
            # 1 shared line out of 3 gated lines per skill.
            self.assertEqual(33.3, report["gated_median_pct"])
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(1, METER.main(["--root", tmp, "--max-median", "12"]))
                self.assertEqual(0, METER.main(["--root", tmp, "--max-median", "40"]))

    def test_canonical_degraded_sentence_pattern(self):
        line = "Without verified dates, return the narrowest qualified result and mark the affected checks `not assessed`. A grid can still ship."
        self.assertTrue(METER.allow_listed(line))
        self.assertFalse(METER.allow_listed("Apply the domain method in the core sections below."))


class LiveBudgetTests(unittest.TestCase):
    def test_live_catalogue_meets_the_lean_budgets(self):
        report = METER.measure(ROOT)
        over = [path for path, value in report["skills"].items() if value["lines"] > VALIDATOR.LINE_BUDGET]
        self.assertEqual([], over)
        self.assertLessEqual(report["median_lines"], 200)
        self.assertLessEqual(report["gated_median_pct"], 12.0)


if __name__ == "__main__":
    unittest.main()

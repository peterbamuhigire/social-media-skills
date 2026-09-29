#!/usr/bin/env python3
"""Measure repeated scaffolding across active skills (Social Kaizen S09-T02).

A line is *shared* when, after whitespace normalisation, it appears verbatim in 5 % or more
of the active SKILL.md files. Each skill's shared-line ratio is its shared non-blank lines
divided by its non-blank lines. Two figures are reported:

raw       every non-blank line counts, frontmatter included. This is the plan-time method
          (01-baseline.md section 3): it gives 30.5 % on the S01 commit (191 skills).
gated     the same, but allow-listed lines are excluded from both numerator and denominator:
          the canonical sentences named in docs/standards/skill-authoring-standard.md and the
          structural lines the validator requires (frontmatter keys, the dual-compat markers,
          headings, table separator rows and the four contract table header rows). The
          lean-template budget (D-SK-06) applies to the gated median: <= 12 %.

Usage:
    python -X utf8 scripts/measure_skill_scaffolding.py            # summary
    python -X utf8 scripts/measure_skill_scaffolding.py --json     # full per-skill report
    python -X utf8 scripts/measure_skill_scaffolding.py --max-median 12   # exit 1 above budget
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARE_THRESHOLD = 0.05

# The canonical sentences of the lean template (roadmap section 7). They are allowed verbatim in
# every skill, so they never count as scaffolding.
CANONICAL_SENTENCES = (
    "Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach "
    "and personal-data processing need explicit, action-specific client authority.",
)
# The canonical degraded-mode sentence carries one domain clause, so it is matched by pattern.
CANONICAL_PATTERNS = (
    re.compile(r"^Without .+, return the narrowest qualified result and mark the affected checks `not assessed`\..*$"),
)
FRONTMATTER_LINE = re.compile(r"^(?:name|description|license|allowed-tools|metadata|portable|compatible_with):|^- (?:claude-code|codex)$")
TABLE_SEPARATOR = re.compile(r"^\|?[\s:|-]+\|[\s:|-]*$")
CONTRACT_TABLE_HEADERS = {
    "| Artefact | Source/provider | Required? | If absent |",
    "| Artefact | Consumer | Acceptance condition |",
    "| Evidence | Format | Acceptance condition |",
    "| Condition | Action | Failure or risk avoided |",
}
STRUCTURAL = {"---", "<!-- dual-compat-start -->", "<!-- dual-compat-end -->"}


def normalise(line: str) -> str:
    return " ".join(line.split())


def skill_lines(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    return [normalised for normalised in (normalise(line) for line in text.split("\n")) if normalised]


def allow_listed(line: str) -> bool:
    if line in CANONICAL_SENTENCES or line in STRUCTURAL or line in CONTRACT_TABLE_HEADERS:
        return True
    if line.startswith("#") or TABLE_SEPARATOR.match(line) or FRONTMATTER_LINE.match(line):
        return True
    return any(pattern.match(line) for pattern in CANONICAL_PATTERNS)


def measure(root: Path) -> dict:
    files = sorted((root / "skills").rglob("SKILL.md"))
    lines = {path: skill_lines(path) for path in files}
    frequency: Counter[str] = Counter()
    for values in lines.values():
        frequency.update(set(values))
    # At least two skills must share a line; in a catalogue of 40 or more this is the 5 % rule.
    threshold = max(2, SHARE_THRESHOLD * len(files))
    shared = {line for line, count in frequency.items() if count >= threshold}
    per_skill = {}
    for path, values in lines.items():
        gated = [line for line in values if not allow_listed(line)]
        per_skill[path.relative_to(root).as_posix()] = {
            "lines": len(path.read_text(encoding="utf-8", errors="replace").splitlines()),
            "raw_ratio": round(100 * sum(line in shared for line in values) / len(values), 1) if values else 0.0,
            "gated_ratio": round(100 * sum(line in shared for line in gated) / len(gated), 1) if gated else 0.0,
        }
    raw = [value["raw_ratio"] for value in per_skill.values()]
    gated = [value["gated_ratio"] for value in per_skill.values()]
    counts = [value["lines"] for value in per_skill.values()]
    top = sorted(((count, line) for line, count in frequency.items() if line in shared and not allow_listed(line)), reverse=True)
    return {
        "method": "line shared when verbatim (whitespace-normalised) in >= 5 % of active SKILL.md files",
        "active_skill_count": len(files),
        "raw_median_pct": round(statistics.median(raw), 1) if raw else 0.0,
        "gated_median_pct": round(statistics.median(gated), 1) if gated else 0.0,
        "median_lines": statistics.median(counts) if counts else 0,
        "over_300_lines": sum(count > 300 for count in counts),
        "top_shared_lines": [{"skills": count, "line": line} for count, line in top[:25]],
        "skills": per_skill,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--max-median", type=float, help="fail when the gated median exceeds this percentage")
    options = parser.parse_args(argv)
    report = measure(options.root.resolve())
    if options.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"skills={report['active_skill_count']} raw_median={report['raw_median_pct']}% "
              f"gated_median={report['gated_median_pct']}% median_lines={report['median_lines']} "
              f"over_300={report['over_300_lines']}")
    if options.max_median is not None and report["gated_median_pct"] > options.max_median:
        if not options.json:
            print(f"scaffolding budget exceeded: gated median {report['gated_median_pct']}% > {options.max_median}%")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

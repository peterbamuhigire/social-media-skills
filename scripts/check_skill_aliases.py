#!/usr/bin/env python3
"""Keep retired-skill aliases, the alias registry, the active count and the cap in lockstep.

A retired skill keeps its folder: its SKILL.md is renamed ALIAS.md in place, a banner is
inserted below the frontmatter, and docs/skill-aliases.yml routes it to an active owner
(decision D-SK-03, Social Kaizen 2026-09-29). Parity with the dev engine's
`check_alias_integrity`, extended with chain, banner, cap and count checks.

Findings (exit 1 on any):
  alias-registry        registry missing, unreadable or malformed
  alias-unrouted        ALIAS.md on disk with no route in the registry
  alias-stale           route with no ALIAS.md on disk
  alias-dangling        route target has no active SKILL.md
  alias-chain           route target is itself a retired alias
  alias-active-conflict a directory holds both SKILL.md and ALIAS.md
  alias-banner-missing  ALIAS.md lacks the "> Inactive alias." banner naming its target
  cap-exceeded          active SKILL.md count above hard_cap (strict since S07; the S02-S07
                        `consolidation_until` window was removed in S08 and is ignored if re-added)
  count-mismatch        registry count, filesystem count and quality-baseline.json disagree
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path("docs/skill-aliases.yml")
BASELINE = Path("quality-baseline.json")
FM_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
BANNER = "> Inactive alias."


@dataclass
class Finding:
    code: str
    path: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def banner_line(alias_file: Path) -> str | None:
    raw = alias_file.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    match = FM_RE.match(raw)
    body = raw[match.end():] if match else raw
    for line in body.splitlines():
        if line.strip():
            return line.strip()
    return None


def check(root: Path) -> tuple[list[Finding], dict]:
    findings: list[Finding] = []
    registry_path = root / REGISTRY
    stats: dict = {"routes": 0, "active": 0, "cap": None}
    if not registry_path.is_file():
        return [Finding("alias-registry", REGISTRY.as_posix(), "alias registry is missing")], stats
    try:
        registry = yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        return [Finding("alias-registry", REGISTRY.as_posix(), f"invalid YAML: {exc}")], stats
    policy = registry.get("active_skill_policy") if isinstance(registry, dict) else None
    routes = registry.get("inactive_skill_aliases") if isinstance(registry, dict) else None
    if not isinstance(policy, dict) or not isinstance(routes, dict) or registry.get("inactive_alias_file") != "ALIAS.md":
        return [Finding("alias-registry", REGISTRY.as_posix(),
                        "registry needs active_skill_policy (mapping), inactive_alias_file: ALIAS.md and inactive_skill_aliases (mapping)")], stats
    hard_cap = policy.get("hard_cap")
    if type(hard_cap) is not int or hard_cap < 1:
        return [Finding("alias-registry", REGISTRY.as_posix(), "active_skill_policy.hard_cap must be a positive integer")], stats

    active_roots = policy.get("active_roots") or ["skills"]
    skill_dirs: set[str] = set()
    alias_dirs: set[str] = set()
    for active_root in active_roots:
        base = root / active_root
        if not base.is_dir():
            continue
        skill_dirs.update(p.parent.relative_to(root).as_posix() for p in base.rglob("SKILL.md"))
        alias_dirs.update(p.parent.relative_to(root).as_posix() for p in base.rglob("ALIAS.md"))
    routes = {str(k).strip().rstrip("/"): str(v).strip().rstrip("/") for k, v in routes.items()}
    stats.update(routes=len(routes), active=len(skill_dirs), cap=hard_cap)

    for both in sorted(skill_dirs & alias_dirs):
        findings.append(Finding("alias-active-conflict", both, "directory holds both SKILL.md and ALIAS.md"))
    for orphan in sorted(alias_dirs - set(routes)):
        findings.append(Finding("alias-unrouted", orphan, "ALIAS.md exists but has no route in docs/skill-aliases.yml"))
    for source, target in sorted(routes.items()):
        if source not in alias_dirs:
            findings.append(Finding("alias-stale", source, "registry route has no ALIAS.md on disk"))
        if target in alias_dirs or target in routes:
            findings.append(Finding("alias-chain", source, f"routes to `{target}`, which is itself a retired alias"))
        elif target not in skill_dirs:
            findings.append(Finding("alias-dangling", source, f"routes to `{target}`, which has no active SKILL.md"))
        if source in alias_dirs:
            line = banner_line(root / source / "ALIAS.md") or ""
            if not line.startswith(BANNER) or not re.search(rf"(?<![\w/-]){re.escape(target)}(?![\w-])", line):
                findings.append(Finding("alias-banner-missing", source,
                                        f"first body line must start with '{BANNER}' and name `{target}`"))

    if len(skill_dirs) > hard_cap:
        findings.append(Finding("cap-exceeded", "skills", f"{len(skill_dirs)} active skills exceed hard_cap {hard_cap}"))

    counts = {"filesystem": len(skill_dirs), "registry": policy.get("current_active_skill_count")}
    baseline_path = root / BASELINE
    if baseline_path.is_file():
        try:
            counts["quality-baseline.json"] = json.loads(baseline_path.read_text(encoding="utf-8")).get("active_skill_count")
        except json.JSONDecodeError:
            counts["quality-baseline.json"] = None
    else:
        counts["quality-baseline.json"] = None
    if len(set(counts.values())) != 1:
        findings.append(Finding("count-mismatch", REGISTRY.as_posix(),
                                "active counts disagree: " + ", ".join(f"{k}={v}" for k, v in counts.items())))
    return findings, stats


def main() -> int:
    options = parse_args()
    findings, stats = check(options.root.resolve())
    if options.json:
        print(json.dumps({**stats, "findings": [asdict(f) for f in findings]}, indent=2))
    else:
        print(f"skill aliases: routes={stats['routes']} findings={len(findings)} active={stats['active']} cap={stats['cap']}")
        for finding in findings:
            print(f"- {finding.code}: {finding.path}: {finding.message}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate the social-media skill engine against the July 2026 local contract."""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}
COMPATIBLE = ["claude-code", "codex"]
REQUIRED_HEADINGS = (
    "Use When", "Do Not Use When", "Required Inputs", "Workflow", "Outputs",
    "Evidence Produced", "Capability", "Degraded Mode", "Decision", "Quality Standards",
    "Anti-Patterns", "References",
)
MOJIBAKE = ("Ã", "Â", "â€", "â†", "âœ", "ðŸ", "\ufffd")
RUNNER_SPECIFIC = ("chat.customAgentInSubagent.enabled", "latest VS Code Insiders build", ".github/copilot-instructions.md")
AUDIT_TOKENS = ("audit", "review", "analysis", "diagnostic", "assessment", "evaluation")
MANDATORY = (
    "skills/ai-marketing/anti-ai-slop/SKILL.md",
    "skills/ai-marketing/ai-slop-audit/SKILL.md",
    "skills/meta-utility/skill-writing/SKILL.md",
    "skills/meta-utility/skill-safety-audit/SKILL.md",
    "docs/standards/skill-authoring-standard.md",
    "docs/templates/SKILL.template.md",
    "tests/routing-fixtures.json",
    "scripts/routing_smoke_test.py",
    "docs/source-registers/source-register.json",
    "docs/source-registers/README.md",
    "scripts/check_source_freshness.py",
    "docs/quality-gates/creative-review-gate.md",
    "docs/quality-gates/legal-market-release-gate.md",
    "docs/evidence-packs/measurement-proof-pack.md",
    "docs/world-class-exemplars/campaign-exemplars.md",
)
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
# S09 (Social Kaizen 2026-09-29, D-SK-06): the lean-template ceiling. It replaces the July 2026
# 500-line `line_limit`; the catalogue median (target <= 200) is reported as `median_skill_lines`.
LINE_BUDGET = 300

# S08 (Social Kaizen 2026-09-29): templated routing text carries no routing signal, because the
# routing harness scores exactly the name, description and `Use When`. These phrases come from the
# four description templates and the generated `Use When` / `Do Not Use When` bodies measured at
# baseline (01-baseline.md section 2). Enforced from S08-T11.
DESCRIPTION_TEMPLATES = (
    "is needed to produce",
    "operating playbook with roles, ordered actions",
    "channel plan covering account setup",
    "main deliverable concerns",
    "when its narrower outcome is requested",
    "neighbouring contract",
    "neighbouring workflow",
)
USE_WHEN_TEMPLATES = (
    re.compile(r"requested outcome is specifically a", re.I),
    re.compile(r"build or improve a repeatable", re.I),
    re.compile(r"requested deliverable needs the domain decisions", re.I),
    re.compile(r"turn an approved objective into roles, controls, handoffs", re.I),
    re.compile(r"translate a confirmed audience, offer and objective into channel decisions", re.I),
    re.compile(r"create or revise an? \S+-specific presence", re.I),
    re.compile(r"is not the closer route", re.I),
    re.compile(r"(?m)^\s*[-*]\s+use this skill (?:for|when)\b", re.I),
    re.compile(r"when its narrower output is the real deliverable", re.I),
    re.compile(r"use the closest `(?:playbook|platform|strategy)-\*` skill", re.I),
)
# Description formula (S08 section 5): "Use when <trigger>; produces <artefact>; not for <job> (use `<id>`)."
DESCRIPTION_NEIGHBOUR = re.compile(r"not for\b.*\(use `([a-z0-9][a-z0-9-]*)`", re.I | re.S)
BACKTICK_ID = re.compile(r"`([a-z0-9][a-z0-9-]*[a-z0-9])`")
ENGINE_ID_SUFFIXES = ("-skills", "-engine", "-doctrine", "-agents")


def template_findings(description: str, use_when: str, do_not_use: str) -> list[str]:
    """Return the S08 routing-text findings for one skill.

    description_template  a description template phrase is present
    description_formula   no "produces" or no "not for ... (use `<id>`)" clause
    use_when_template     a generated `Use When` / `Do Not Use When` phrase is present, `Use When`
                          has fewer than 3 or more than 6 bullets, or `Do Not Use When` names fewer
                          than 2 neighbour ids
    """
    findings: list[str] = []
    lowered = description.lower()
    if any(phrase in lowered for phrase in DESCRIPTION_TEMPLATES):
        findings.append("description_template")
    if not DESCRIPTION_NEIGHBOUR.search(description) or "produces" not in lowered:
        findings.append("description_formula")
    use_bullets = re.findall(r"(?m)^\s*[-*]\s+\S", use_when)
    neighbours = set(BACKTICK_ID.findall(do_not_use))
    if (any(pattern.search(use_when) or pattern.search(do_not_use) for pattern in USE_WHEN_TEMPLATES)
            or not 3 <= len(use_bullets) <= 6 or len(neighbours) < 2):
        findings.append("use_when_template")
    return findings


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--active-root", action="append", default=["skills"])
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def section(body: str, pattern: str) -> str | None:
    match = re.search(rf"(?ims)^##\s+[^\n]*(?:{pattern})[^\n]*\s*$\n(.*?)(?=^##\s+|\Z)", body)
    return match.group(1).strip() if match else None


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


# Portable-link rule: CI checks out one repository, so a link that is host-absolute
# (C:/..., /C:/..., file:) or that climbs out of the repository to a sibling engine
# resolves only on the author's machine. Such links count as broken locally too, so a
# local pass predicts the CI result; link to other engines by their GitHub URL instead.
HOST_ABSOLUTE_LINK = re.compile(r"^(?:file:|/?[A-Za-z]:[\\/])", re.I)


def portable_link_target(base: Path, root: Path, target: str) -> Path | None:
    """Resolve a local link target, or return None when it is not portable."""
    if HOST_ABSOLUTE_LINK.match(target):
        return None
    resolved = (base / target).resolve()
    return resolved if resolved.is_relative_to(root.resolve()) else None


def local_link_exists(skill: Path, target: str, root: Path) -> bool:
    target = target.split("#", 1)[0]
    if HOST_ABSOLUTE_LINK.match(target):
        return False
    if not target or "://" in target or target.startswith(("mailto:", "#")):
        return True
    resolved = portable_link_target(skill.parent, root, target)
    return resolved is not None and resolved.exists()


def retired_dirs(root: Path, active_roots: list[str]) -> set[Path]:
    """Skill folders retired as inactive aliases (SKILL.md renamed ALIAS.md, decision D-SK-03).

    A category-level alias (for example skills/content-writing/ALIAS.md, S03-T08) sits above active
    skills and a shared references/ folder that stay live, so its folder is not treated as retired;
    a link to the ALIAS.md file itself is still an alias_link.
    """
    folders = {p.parent.resolve() for active in active_roots if (root / active).is_dir() for p in (root / active).rglob("ALIAS.md")}
    return {folder for folder in folders if not any((child / "SKILL.md").is_file() for child in folder.iterdir() if child.is_dir())}


def links_to_alias(path: Path, root: Path, retired: set[Path]) -> bool:
    """True when an active skill links to an ALIAS.md or into a retired skill folder.

    Retired skills route through docs/skill-aliases.yml; active skills must link to the owner
    (and its references) instead, so a merge cannot leave a live route pointing at an alias.
    """
    body = path.read_text(encoding="utf-8", errors="replace")
    for target in markdown_links(body):
        target = target.split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        if target.replace("\\", "/").endswith("/ALIAS.md") or target == "ALIAS.md":
            return True
        resolved = portable_link_target(path.parent, root, target)
        if resolved is not None and any(resolved == folder or folder in resolved.parents for folder in retired):
            return True
    return False


def alias_policy(root: Path) -> dict:
    registry = root / "docs" / "skill-aliases.yml"
    if not registry.is_file():
        return {}
    try:
        data = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return {}
    policy = data.get("active_skill_policy") if isinstance(data, dict) else None
    return policy if isinstance(policy, dict) else {}


def assess(path: Path, root: Path) -> list[str]:
    findings: list[str] = []
    raw = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    match = FM_RE.match(raw)
    if not match:
        return ["frontmatter"]
    try:
        front = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return ["frontmatter_yaml"]
    if not isinstance(front, dict):
        return ["frontmatter_type"]
    body = raw[match.end():]
    if not re.search(r"(?m)^#\s+\S", body):
        findings.append("missing_title")
    if set(front) - ALLOWED_FRONTMATTER:
        findings.append("unsupported_frontmatter")
    if front.get("name") != path.parent.name:
        findings.append("name_mismatch")
    desc = front.get("description")
    desc_line = next((line for line in match.group(1).splitlines() if line.startswith("description:")), "")
    if not isinstance(desc, str) or not desc.startswith("Use when") or len(desc) > 350 or desc_line.strip() in {"description: >", "description: |"}:
        findings.append("description_contract")
    metadata = front.get("metadata")
    if not isinstance(metadata, dict) or metadata.get("portable") is not True or metadata.get("compatible_with") != COMPATIBLE:
        findings.append("portable_metadata")
    if "<!-- dual-compat-start -->" not in body or "<!-- dual-compat-end -->" not in body:
        findings.append("portable_markers")
    aliases = {
        "Use When": "Use When", "Do Not Use When": "Do Not Use When",
        "Required Inputs": "(?:Required )?Inputs", "Workflow": "Workflow",
        "Outputs": "Outputs", "Evidence Produced": "Evidence Produced",
        "Capability": "Capability|Permission Boundaries", "Degraded Mode": "Degraded Mode",
        "Decision": "Decision", "Quality Standards": "Quality Standards",
        "Anti-Patterns": "Anti-Patterns", "References": "References",
    }
    sections = {name: section(body, pattern) for name, pattern in aliases.items()}
    for name in REQUIRED_HEADINGS:
        if sections[name] is None or not sections[name].strip():
            findings.append("missing_" + re.sub(r"\W+", "_", name.lower()).strip("_"))
    if isinstance(desc, str):
        findings.extend(template_findings(desc, sections.get("Use When") or "", sections.get("Do Not Use When") or ""))
    inputs = sections.get("Required Inputs") or ""
    if "|" not in inputs or not re.search(r"source|provider|produced by", inputs, re.I) or not re.search(r"absent|missing|fallback|if unavailable", inputs, re.I):
        findings.append("input_contract")
    outputs = sections.get("Outputs") or ""
    if "|" not in outputs or not re.search(r"consumer|consumed by", outputs, re.I) or not re.search(r"accept", outputs, re.I):
        findings.append("output_contract")
    evidence = sections.get("Evidence Produced") or ""
    if "|" not in evidence or not re.search(r"accept|evidence|format", evidence, re.I):
        findings.append("evidence_contract")
    capability = sections.get("Capability") or ""
    if not re.search(r"read|search", capability, re.I) or not re.search(r"authori[sz]|permission|explicit", capability, re.I):
        findings.append("capability_contract")
    if any(token in path.parent.name for token in AUDIT_TOKENS) and "read-only" not in capability.lower():
        findings.append("audit_not_read_only")
    degraded = sections.get("Degraded Mode") or ""
    if not re.search(r"not assessed|unavailable|narrowest|qualified", degraded, re.I):
        findings.append("degraded_mode_contract")
    decision = sections.get("Decision") or ""
    if "|" not in decision or not re.search(r"failure|risk|wrong", decision, re.I):
        findings.append("decision_contract")
    workflow = sections.get("Workflow") or ""
    if len(re.findall(r"(?m)^\s*\d+\.\s+", workflow)) < 3 or not re.search(r"stop|pause|withhold", workflow, re.I) or not re.search(r"recover|rerun|correct|retry|fallback", workflow, re.I):
        findings.append("workflow_contract")
    anti = sections.get("Anti-Patterns") or ""
    bullets = re.findall(r"(?m)^\s*[-*]\s+(.+)", anti)
    if len(bullets) < 5 or any(not re.search(r"\bfix\s*:", bullet, re.I) for bullet in bullets[:5]):
        findings.append("anti_pattern_contract")
    refs = sections.get("References") or ""
    links = markdown_links(refs)
    if not links:
        findings.append("reference_contract")
    if any(not local_link_exists(path, target, root) for target in markdown_links(body)):
        findings.append("broken_relative_link")
    if len(raw.splitlines()) > LINE_BUDGET:
        findings.append("line_budget")
    if any(marker in raw for marker in MOJIBAKE):
        findings.append("encoding_noise")
    if any(snippet in body for snippet in RUNNER_SPECIFIC):
        findings.append("runner_specific_body")
    if re.search(r"(?im)^##\s+Worked Examples?\s*$", body) and not section(body, "Worked Examples?"):
        findings.append("empty_worked_examples")
    return sorted(set(findings))


def main() -> int:
    options = args()
    root = options.root.resolve()
    files = sorted({path for active in options.active_root for path in (root / active).rglob("SKILL.md")})
    results = {path.relative_to(root).as_posix(): assess(path, root) for path in files}
    retired = retired_dirs(root, options.active_root)
    if retired:
        for path in files:
            if links_to_alias(path, root, retired):
                relative = path.relative_to(root).as_posix()
                results[relative] = sorted(set(results[relative] + ["alias_link"]))
    names: defaultdict[str, list[str]] = defaultdict(list)
    for relative in results:
        path = root / relative
        match = FM_RE.match(path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n"))
        if match:
            try:
                data = yaml.safe_load(match.group(1)) or {}
                if isinstance(data.get("name"), str):
                    names[data["name"]].append(relative)
            except yaml.YAMLError:
                pass
    for paths in names.values():
        if len(paths) > 1:
            for relative in paths:
                results[relative] = sorted(set(results[relative] + ["duplicate_name"]))
    # S08: the neighbour named in a description's "not for ... (use `<id>`)" clause must be an active skill.
    for relative in list(results):
        if relative.startswith("@engine/"):
            continue
        match = FM_RE.match((root / relative).read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n"))
        try:
            description = (yaml.safe_load(match.group(1)) or {}).get("description", "") if match else ""
        except (yaml.YAMLError, AttributeError):
            continue
        neighbour = DESCRIPTION_NEIGHBOUR.search(description) if isinstance(description, str) else None
        if neighbour and neighbour.group(1) not in names:
            results[relative] = sorted(set(results[relative] + ["description_neighbour_unknown"]))
        # Every skill id named in `Do Not Use When` must also be active, so a merge must re-point it.
        # Engine ids (`*-skills`, `*-engine`, `*-doctrine`) name other repositories and are skipped.
        body = (root / relative).read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")[match.end():] if match else ""
        named = BACKTICK_ID.findall(section(body, "Do Not Use When") or "")
        if any(ident not in names for ident in named if not ident.endswith(ENGINE_ID_SUFFIXES)):
            results[relative] = sorted(set(results[relative] + ["do_not_use_neighbour_unknown"]))
    for required in MANDATORY:
        if not (root / required).exists():
            results[f"@engine/{required}"] = ["missing_mandatory_resource"]
    counts = Counter(finding for findings in results.values() for finding in findings)
    line_counts = [len(path.read_text(encoding="utf-8", errors="replace").splitlines()) for path in files]
    payload = {
        "standard": "july-2026-zero-debt",
        "active_roots": options.active_root,
        "active_skill_count": len(files),
        "template_count": len(list((root / "docs" / "templates").glob("*.md"))) if (root / "docs" / "templates").exists() else 0,
        "fully_compliant": sum(not value for value in results.values()),
        "line_budget": LINE_BUDGET,
        "median_skill_lines": statistics.median(line_counts) if line_counts else 0,
        "failure_counts": dict(sorted(counts.items())),
        "results": {key: value for key, value in results.items() if value},
    }
    policy = alias_policy(root)
    cap = policy.get("hard_cap")
    # The cap is strict: the S02-S07 `consolidation_until` window closed in S07 and its branch was
    # removed in S08, so the key is ignored if it is ever re-added.
    if type(cap) is int and len(files) > cap:
        payload["catalogue_cap_exceeded"] = {"hard_cap": cap, "actual": len(files)}
    if options.baseline:
        baseline = json.loads(options.baseline.read_text(encoding="utf-8"))
        expected = baseline.get("failure_counts", {})
        if expected:
            payload["baseline_error"] = "Baseline contains waivers; zero-debt requires an empty failure_counts object."
        if payload["failure_counts"] != expected:
            payload["baseline_mismatch"] = {"expected": expected, "actual": payload["failure_counts"]}
        if baseline.get("active_skill_count") != len(files):
            payload["catalogue_count_mismatch"] = {"expected": baseline.get("active_skill_count"), "actual": len(files)}
    print(json.dumps(payload, indent=2) if options.json else f"skills={len(files)} compliant={payload['fully_compliant']} failures={sum(counts.values())} median_lines={payload['median_skill_lines']}\n" + "\n".join(f"{name}: {count}" for name, count in sorted(counts.items())))
    if "catalogue_cap_exceeded" in payload and not options.json:
        print(f"catalogue_cap_exceeded: {payload['catalogue_cap_exceeded']['actual']} active > hard_cap {payload['catalogue_cap_exceeded']['hard_cap']} (docs/skill-aliases.yml)")
    return 1 if counts or "baseline_error" in payload or "baseline_mismatch" in payload or "catalogue_count_mismatch" in payload or "catalogue_cap_exceeded" in payload else 0


if __name__ == "__main__":
    sys.exit(main())

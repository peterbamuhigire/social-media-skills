#!/usr/bin/env python3
"""Validate the social-media skill engine against the July 2026 local contract."""

from __future__ import annotations

import argparse
import json
import re
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
)
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


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


def local_link_exists(skill: Path, target: str) -> bool:
    target = target.split("#", 1)[0]
    if not target or "://" in target or target.startswith(("mailto:", "#")):
        return True
    return (skill.parent / target).resolve().exists()


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
    if any(not local_link_exists(path, target) for target in markdown_links(body)):
        findings.append("broken_relative_link")
    if len(raw.splitlines()) > 500:
        findings.append("line_limit")
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
    for required in MANDATORY:
        if not (root / required).exists():
            results[f"@engine/{required}"] = ["missing_mandatory_resource"]
    counts = Counter(finding for findings in results.values() for finding in findings)
    payload = {
        "standard": "july-2026-zero-debt",
        "active_roots": options.active_root,
        "active_skill_count": len(files),
        "template_count": len(list((root / "docs" / "templates").glob("*.md"))) if (root / "docs" / "templates").exists() else 0,
        "fully_compliant": sum(not value for value in results.values()),
        "failure_counts": dict(sorted(counts.items())),
        "results": {key: value for key, value in results.items() if value},
    }
    if options.baseline:
        baseline = json.loads(options.baseline.read_text(encoding="utf-8"))
        expected = baseline.get("failure_counts", {})
        if expected:
            payload["baseline_error"] = "Baseline contains waivers; zero-debt requires an empty failure_counts object."
        if payload["failure_counts"] != expected:
            payload["baseline_mismatch"] = {"expected": expected, "actual": payload["failure_counts"]}
        if baseline.get("active_skill_count") != len(files):
            payload["catalogue_count_mismatch"] = {"expected": baseline.get("active_skill_count"), "actual": len(files)}
    print(json.dumps(payload, indent=2) if options.json else f"skills={len(files)} compliant={payload['fully_compliant']} failures={sum(counts.values())}\n" + "\n".join(f"{name}: {count}" for name, count in sorted(counts.items())))
    return 1 if counts or "baseline_error" in payload or "baseline_mismatch" in payload or "catalogue_count_mismatch" in payload else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Fail closed on plugin identity, skill-path drift, and the portfolio file ceiling."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


HARD_LIMIT = 5000
PACKAGE_EXCLUDES = {".git", ".cache", ".venv", "venv", "__pycache__", ".pytest_cache", "node_modules"}


def count_entries(root: Path, *, package: bool = False) -> int:
    """Count file and symlink entries without traversing symlinks; unreadable trees fail closed."""
    count = 0

    def fail(error: OSError) -> None:
        raise error

    for current, directories, files in os.walk(root, followlinks=False, onerror=fail):
        kept: list[str] = []
        for name in directories:
            if package and name in PACKAGE_EXCLUDES:
                continue
            path = Path(current) / name
            if path.is_symlink():
                count += 1
            else:
                kept.append(name)
        directories[:] = kept
        count += len(files)
    return count


def _load_object(path: Path, label: str, errors: list[str]) -> dict | None:
    if path.is_symlink():
        errors.append(f"{label} must not be a symlink")
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{label} cannot be read: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label} must be a JSON object")
        return None
    return value


def validate_manifests(root: Path) -> list[str]:
    errors: list[str] = []
    plugin = _load_object(root / ".claude-plugin" / "plugin.json", "plugin manifest", errors)
    marketplace = _load_object(root / ".claude-plugin" / "marketplace.json", "marketplace manifest", errors)
    if plugin is None or marketplace is None:
        return errors

    plugin_name = plugin.get("name")
    version = plugin.get("version")
    if not isinstance(plugin_name, str) or not plugin_name.strip():
        errors.append("plugin manifest requires a non-empty name")
    if not isinstance(version, str) or not version.strip():
        errors.append("plugin manifest requires a non-empty version")
    market_name = marketplace.get("name")
    entries = marketplace.get("plugins")
    if not isinstance(market_name, str) or not market_name.strip():
        errors.append("marketplace manifest requires a non-empty name")
    if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
        errors.append("marketplace must declare exactly one plugin object")
        entries = []
    if entries:
        entry = entries[0]
        if entry.get("source") not in (".", "./"):
            errors.append("marketplace plugin source must be this local repository")
        if isinstance(plugin_name, str) and entry.get("name") != plugin_name:
            errors.append("marketplace plugin name differs from plugin manifest")
        if isinstance(version, str) and entry.get("version") != version:
            errors.append("marketplace plugin version differs from plugin manifest")

    configured = plugin.get("skills")
    if not isinstance(configured, list) or any(not isinstance(item, str) for item in configured):
        errors.append("plugin manifest skills must be an array of relative directories")
        configured = []

    declared: set[Path] = set()
    for item in configured:
        candidate = root / item
        try:
            relative = candidate.relative_to(root)
        except (OSError, ValueError):
            errors.append(f"skill path is missing or escapes repository: {item}")
            continue
        cursor = root
        linked = False
        for part in relative.parts:
            cursor = cursor / part
            if cursor.is_symlink():
                linked = True
                break
        skill_file = candidate / "SKILL.md"
        if linked or skill_file.is_symlink():
            errors.append(f"skill path contains a symlink: {item}")
            continue
        try:
            resolved = candidate.resolve(strict=True)
            resolved.relative_to(root.resolve(strict=True))
        except (OSError, ValueError):
            errors.append(f"skill path is missing or escapes repository: {item}")
            continue
        if not skill_file.is_file():
            errors.append(f"skill path has no regular SKILL.md: {item}")
            continue
        if resolved in declared:
            errors.append(f"duplicate skill path: {item}")
        declared.add(resolved)

    actual: set[Path] = set()
    skills_root = root / "skills"
    if not skills_root.is_dir():
        errors.append("skills directory is missing")
    else:
        def fail_walk(error: OSError) -> None:
            raise error

        try:
            for current, directories, files in os.walk(skills_root, followlinks=False, onerror=fail_walk):
                current_path = Path(current)
                linked_dirs = [name for name in directories if (current_path / name).is_symlink()]
                if linked_dirs:
                    errors.append(f"symlinked directories under skills: {current_path.relative_to(root)}")
                directories[:] = [name for name in directories if name not in linked_dirs]
                if "SKILL.md" in files:
                    skill = current_path / "SKILL.md"
                    if skill.is_symlink():
                        errors.append(f"active skill file is a symlink: {skill.relative_to(root)}")
                    else:
                        actual.add(current_path.resolve())
        except OSError as exc:
            errors.append(f"skill inventory unavailable: {exc}")
    if declared != actual:
        missing = sorted(path.relative_to(root.resolve()).as_posix() for path in actual - declared)
        extra = sorted(path.relative_to(root.resolve()).as_posix() for path in declared - actual)
        errors.append(f"declared skill paths differ from filesystem (missing={missing}; extra={extra})")
    return errors


def capacity_findings(checkout: int, package: int, *, limit: int = HARD_LIMIT) -> list[str]:
    return [f"{label} file entries {count} exceed hard limit {limit}"
            for label, count in (("checkout", checkout), ("package", package)) if count > limit]


def audit_repository(root: Path, *, limit: int = HARD_LIMIT) -> tuple[list[str], dict[str, int]]:
    if type(limit) is not int or limit < 1 or limit > HARD_LIMIT:
        raise ValueError(f"test limit must be an integer from 1 through {HARD_LIMIT}")
    root = root.resolve(strict=True)
    counts = {"checkout": count_entries(root), "package": count_entries(root, package=True)}
    errors = capacity_findings(counts["checkout"], counts["package"], limit=limit)
    errors.extend(validate_manifests(root))
    return errors, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--limit", type=int, default=HARD_LIMIT,
                        help="lower test boundary only; values above the fixed hard limit are rejected")
    options = parser.parse_args()
    try:
        errors, counts = audit_repository(options.root, limit=options.limit)
    except (OSError, ValueError) as exc:
        print(f"package integrity: FAIL; inventory unavailable: {exc}")
        return 1
    print(f"package integrity: checkout={counts['checkout']} package={counts['package']} hard_limit={options.limit} findings={len(errors)}")
    for error in errors:
        print(f"- {error}")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())

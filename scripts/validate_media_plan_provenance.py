#!/usr/bin/env python3
"""Validate the evidence origin attached to numeric media-plan inputs."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


NUMERIC_FIELDS = ("budget_ugx", "cpm_ugx", "frequency")
ALLOWED_ORIGINS = {"observed", "client_input", "synthetic_assumption"}


def validate_rows(rows: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(rows, list) or not rows:
        return ["rows must be a non-empty array"]
    for index, row in enumerate(rows, 1):
        label = row.get("channel", f"row {index}") if isinstance(row, dict) else f"row {index}"
        if not isinstance(row, dict):
            errors.append(f"{label}: row must be an object")
            continue
        if not isinstance(row.get("channel"), str) or not row["channel"].strip():
            errors.append(f"row {index}: non-empty channel is required")
        for field in NUMERIC_FIELDS:
            record = row.get(field)
            if not isinstance(record, dict):
                errors.append(f"{label}: {field} must include value, origin and source")
                continue
            value = record.get("value")
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(value) or value <= 0):
                errors.append(f"{label}: {field}.value must be a finite positive number")
            origin = record.get("origin")
            if origin not in ALLOWED_ORIGINS:
                errors.append(f"{label}: {field}.origin must be observed, client_input or synthetic_assumption")
            source = record.get("source")
            if not isinstance(source, str) or not source.strip():
                errors.append(f"{label}: {field}.source must identify its evidence or assumption")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    options = parser.parse_args()
    try:
        payload = json.loads(options.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"media-plan provenance: FAIL; cannot read input: {exc}")
        return 1
    errors = validate_rows(payload.get("rows") if isinstance(payload, dict) else None)
    if errors:
        print(f"media-plan provenance: FAIL ({len(errors)} finding(s))")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"media-plan provenance: PASS ({len(payload['rows'])} rows; numeric origins and references present)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

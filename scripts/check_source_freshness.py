#!/usr/bin/env python3
"""Fail when the engine's changing-source register is incomplete, inconsistent or stale."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "id", "domain", "jurisdiction", "title", "publisher", "tier", "url",
    "verified_on", "review_every_days", "next_review", "use_for", "verification_note",
}
DOMAINS = {"legal", "platform", "market"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=ROOT / "docs/source-registers/source-register.json")
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    return parser.parse_args()


def validate(register: Path, as_of: date) -> list[str]:
    payload = json.loads(register.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        return ["register: records must be a non-empty list"]
    errors: list[str] = []
    seen: set[str] = set()
    present_domains: set[str] = set()
    for index, record in enumerate(records, 1):
        label = record.get("id", f"record-{index}") if isinstance(record, dict) else f"record-{index}"
        if not isinstance(record, dict):
            errors.append(f"{label}: record must be an object")
            continue
        missing = sorted(REQUIRED - set(record))
        if missing:
            errors.append(f"{label}: missing {', '.join(missing)}")
            continue
        if label in seen:
            errors.append(f"{label}: duplicate id")
        seen.add(label)
        present_domains.add(record["domain"])
        if record["domain"] not in DOMAINS:
            errors.append(f"{label}: unsupported domain {record['domain']!r}")
        if record["tier"] not in (1, 2, 3):
            errors.append(f"{label}: tier must be 1, 2 or 3")
        if not isinstance(record["use_for"], list) or not record["use_for"]:
            errors.append(f"{label}: use_for must be a non-empty list")
        parsed = urlparse(record["url"])
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{label}: url must be an absolute HTTPS URL")
        try:
            verified = date.fromisoformat(record["verified_on"])
            review = date.fromisoformat(record["next_review"])
            interval = int(record["review_every_days"])
        except (TypeError, ValueError):
            errors.append(f"{label}: invalid date or review interval")
            continue
        if interval < 1 or review != verified + timedelta(days=interval):
            errors.append(f"{label}: next_review must equal verified_on plus review_every_days")
        if review < as_of:
            errors.append(f"{label}: overdue since {review.isoformat()}")
    missing_domains = sorted(DOMAINS - present_domains)
    if missing_domains:
        errors.append(f"register: missing domains {', '.join(missing_domains)}")
    return errors


def main() -> int:
    options = parse_args()
    errors = validate(options.register, options.as_of)
    if errors:
        print("source freshness: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    count = len(json.loads(options.register.read_text(encoding="utf-8"))["records"])
    print(f"source freshness: PASS ({count} current records; as of {options.as_of.isoformat()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

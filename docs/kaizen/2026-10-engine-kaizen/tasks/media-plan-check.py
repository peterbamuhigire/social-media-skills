#!/usr/bin/env python3
"""Reproduce explicitly synthetic media-plan arithmetic; no market forecast."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_media_plan_provenance import validate_rows

assumptions = [
    {"channel": "LinkedIn", "budget_ugx": 4_000_000, "cpm_ugx": 25_000, "frequency": 2.5},
    {"channel": "Instagram / Meta", "budget_ugx": 5_000_000, "cpm_ugx": 10_000, "frequency": 3},
    {"channel": "TikTok", "budget_ugx": 3_000_000, "cpm_ugx": 8_000, "frequency": 3},
]
rows_input = [{
    "channel": row["channel"],
    "budget_ugx": {"value": row["budget_ugx"], "origin": "synthetic_assumption", "source": "scenario assumption; no client brief supplied"},
    "cpm_ugx": {"value": row["cpm_ugx"], "origin": "synthetic_assumption", "source": "scenario assumption; not a market rate"},
    "frequency": {"value": row["frequency"], "origin": "synthetic_assumption", "source": "scenario assumption; not a platform control"},
} for row in assumptions]
errors = validate_rows(rows_input)
if errors:
    raise SystemExit("invalid media-plan inputs: " + "; ".join(errors))
rows = []
for row in rows_input:
    budget, cpm, frequency = (row[k]["value"] for k in ("budget_ugx", "cpm_ugx", "frequency"))
    imps = budget / cpm * 1_000
    rows.append({**row, "impressions": imps, "gross_reach_at_assumed_frequency": imps / frequency})
result = {
    "status": "synthetic assumptions only; not an inventory forecast or market rate",
    "method": "impressions = spend / assumed CPM * 1000; implied gross reach = impressions / assumed frequency",
    "platform_reach_is_deduplicated": False,
    "rows": rows,
    "total_budget_ugx": sum(r["budget_ugx"]["value"] for r in rows),
    "total_impressions": sum(r["impressions"] for r in rows),
    "sum_of_platform_gross_reach": sum(r["gross_reach_at_assumed_frequency"] for r in rows),
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

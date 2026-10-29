#!/usr/bin/env python3
"""Reproduce the explicitly synthetic media-plan arithmetic; no market forecast."""
import json
from pathlib import Path

assumptions = [
    {"channel": "LinkedIn", "budget_ugx": 4_000_000, "assumed_cpm_ugx": 25_000, "assumed_frequency": 2.5},
    {"channel": "Instagram / Meta", "budget_ugx": 5_000_000, "assumed_cpm_ugx": 10_000, "assumed_frequency": 3},
    {"channel": "TikTok", "budget_ugx": 3_000_000, "assumed_cpm_ugx": 8_000, "assumed_frequency": 3},
]
rows = []
for row in assumptions:
    imps = row["budget_ugx"] / row["assumed_cpm_ugx"] * 1_000
    rows.append({**row, "impressions": imps, "gross_reach_at_assumed_frequency": imps / row["assumed_frequency"]})
result = {
    "status": "synthetic assumptions only; not an inventory forecast or market rate",
    "method": "impressions = spend / assumed CPM * 1000; implied gross reach = impressions / assumed frequency",
    "platform_reach_is_deduplicated": False,
    "rows": rows,
    "total_budget_ugx": sum(r["budget_ugx"] for r in rows),
    "total_impressions": sum(r["impressions"] for r in rows),
    "sum_of_platform_gross_reach": sum(r["gross_reach_at_assumed_frequency"] for r in rows),
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

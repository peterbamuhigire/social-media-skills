"""S13-T01 routing measures on the live engine tree (lexical proxy). Read-only.

Usage: python -X utf8 measure_routing.py <engine-root> [--ranks]
"""
import json, sys, collections, importlib.util
from pathlib import Path

root = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("r", root / "scripts" / "routing_smoke_test.py")
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
docs = r.catalogue()
fx = json.loads((root / "tests" / "routing-fixtures.json").read_text(encoding="utf-8"))["fixtures"]
pos, neg = collections.Counter(), collections.Counter()
types = collections.Counter(f.get("type") for f in fx)
bands = collections.Counter(); rows = []
for f in fx:
    if f.get("type") == "positive":  # S13 review finding 1: collision fixtures are not positives
        pos[f["expected"]] += 1
    if f.get("negative_for"):
        neg[f["negative_for"]] += 1
        full = r.rank(f["prompt"], docs)
        c = full.index(f["negative_for"]) + 1; e = full.index(f["expected"]) + 1
        bands["competitor in top 3" if c <= 3 else "ranks 4-10" if c <= 10 else "below rank 10"] += 1
        rows.append((c, e, f["id"]))
full_cov = sorted(s for s in docs if pos[s] >= 3 and neg[s] >= 2)
hold = json.loads((root / "docs/kaizen/consolidation-2026-09-29/evidence/S08/holdout-prompts.json").read_text(encoding="utf-8"))["prompts"]
h1 = h3 = 0
for h in hold:
    rk = r.rank(h["prompt"], docs)
    h1 += rk[0] == h["expected"]; h3 += h["expected"] in rk[:3]
out = {"fixtures": len(fx), "types": dict(types), "distinct_expected": len({f['expected'] for f in fx}),
       "active": len(docs), "skills_not_expected_by_any_fixture": sorted(set(docs) - {f['expected'] for f in fx}),
       "alias_fixtures": sum(1 for f in fx if f.get("alias_of")),
       "owned_negatives": sum(neg.values()), "skills_owning_negatives": len(neg),
       "competitor_bands": dict(bands), "t2_cov_ge3pos_ge2neg": len(full_cov), "t2_cov": round(len(full_cov) / len(docs), 4),
       "holdout": {"n": len(hold), "p1": h1, "top3": h3}}
print(json.dumps(out, indent=1))
if "--ranks" in sys.argv:
    for c, e, i in sorted(rows, reverse=True):
        print(f"competitor rank {c:3d}  expected rank {e}  {i}")

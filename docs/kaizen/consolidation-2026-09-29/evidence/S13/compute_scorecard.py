"""Recompute the S13 scorecard from scorecard-inputs.json (deterministic; reads nothing else).
Usage: python -X utf8 compute_scorecard.py"""
import json, pathlib
d = json.loads((pathlib.Path(__file__).parent / "scorecard-inputs.json").read_text(encoding="utf-8"))
c = d["readiness"]["close"]
t1 = c["T1"]["passed"] / c["T1"]["declared"]
p1 = c["T2_p1"]["hits"] / c["T2_p1"]["total"]
neg = c["T2_neg"]["pass"] / c["T2_neg"]["total"]
cov = c["T2_cov"]["skills"] / c["T2_cov"]["active"]
clean = 1.0 if c["T2_clean"]["in_scan"] and not c["T2_clean"]["pairs_ge_0_75"] else 1 - c["T2_clean"]["undeclared"] / c["T2_clean"]["pairs_ge_0_75"]
t3 = 0.0  # NOT_ASSESSED = 0
t2 = (p1 + neg + cov + clean) / 4
ready = round(30 * t1 + 40 * t2 + 30 * t3, 1)
w, j = d["weights"], d["judged"]
def overall(routing):
    hyg = (j["redundancy"] + routing + j["safety"]) / 3
    return round(w["output"] * j["output"] + w["depth"] * j["depth"] + w["standards"] * j["standards"]
                 + w["taxonomy"] * j["taxonomy"] + w["doctrine"] * j["doctrine"] + w["hygiene"] * hyg, 1), round(hyg, 2)
raw, h_raw = overall(j["routing"])
mc, h_mc = overall(ready)
pub = min(mc, d["published_cap"])
print(f"slots T1={t1:.4f} p1={p1:.4f} neg={neg:.4f} cov={cov:.4f} clean={clean:.4f} T3={t3}")
print(f"points T1={30*t1:.2f} T2={40*t2:.2f} T3=0.00 -> Readiness={ready}")
print(f"raw={raw} (hygiene {h_raw}); measured-constrained={mc} (hygiene {h_mc}); published={pub}")

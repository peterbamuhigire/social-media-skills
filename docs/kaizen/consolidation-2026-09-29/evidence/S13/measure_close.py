"""S13-T01 close measures for one tree (base or close). Read-only.

Usage: python -X utf8 measure_close.py <tree-root> <engine-root-for-tooling>
Prints JSON: counts, lines, template findings (current validator classifier), unique-text near-duplicate pairs.
"""
import json, math, re, statistics, sys, collections, importlib.util
from pathlib import Path
import yaml

tree = Path(sys.argv[1]); tool = Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("v", tool / "scripts" / "validate_skill_engine.py")
v = importlib.util.module_from_spec(spec); sys.path.insert(0, str(tool / "scripts")); spec.loader.exec_module(v)

files = sorted((tree / "skills").rglob("SKILL.md"))
by_cat = collections.Counter(p.relative_to(tree / "skills").parts[0] for p in files)
lines = {str(p.relative_to(tree)).replace("\\", "/"): len(p.read_text(encoding="utf-8").splitlines()) for p in files}
vals = list(lines.values())

def section(raw, name):
    m = re.search(rf"(?ims)^##\s+{re.escape(name)}\s*$\n(.*?)(?=^##\s+|\Z)", raw)
    return m.group(1) if m else ""

tmpl = collections.Counter(); desc_t = []; uw_t = []
texts = {}
for p in files:
    raw = p.read_text(encoding="utf-8")
    m = re.match(r"(?s)^---\n(.*?)\n---\n?", raw)
    front = yaml.safe_load(m.group(1)) if m else {}
    desc = str(front.get("description", ""))
    f = v.template_findings(desc, section(raw, "Use When"), section(raw, "Do Not Use When"))
    key = str(p.parent.relative_to(tree / "skills")).replace("\\", "/")
    for x in f:
        tmpl[x] += 1
    # strict template-phrase-only counts (no formula/bullet-count rule), comparable to 01's classes
    if any(ph in desc.lower() for ph in v.DESCRIPTION_TEMPLATES):
        desc_t.append(key)
    uw = section(raw, "Use When") + section(raw, "Do Not Use When")
    if any(pt.search(uw) for pt in v.USE_WHEN_TEMPLATES):
        uw_t.append(key)
    body = raw[m.end():] if m else raw
    texts[key] = [re.sub(r"\s+", " ", ln).strip().lower() for ln in body.splitlines() if ln.strip()]

# unique-text cosine (01-baseline section 3 method): drop lines present in >= 5 % of skills, TF-IDF cosine
n = len(texts)
line_df = collections.Counter()
for ls in texts.values():
    for ln in set(ls):
        line_df[ln] += 1
shared = {ln for ln, c in line_df.items() if c >= 0.05 * n}
TOK = re.compile(r"[a-z][a-z0-9]+")
docs = {k: collections.Counter(t for ln in ls if ln not in shared for t in TOK.findall(ln)) for k, ls in texts.items()}
df = collections.Counter()
for c in docs.values():
    for t in c:
        df[t] += 1
vec = {}
for k, c in docs.items():
    w = {t: (1 + math.log(tf)) * (math.log((1 + n) / (1 + df[t])) + 1) for t, tf in c.items()}
    norm = math.sqrt(sum(x * x for x in w.values())) or 1
    vec[k] = {t: x / norm for t, x in w.items()}
keys = sorted(vec); pairs = []
for i, a in enumerate(keys):
    va = vec[a]
    for b in keys[i + 1:]:
        vb = vec[b]
        small, big = (va, vb) if len(va) < len(vb) else (vb, va)
        s = sum(x * big.get(t, 0.0) for t, x in small.items())
        if s > 0.45:
            pairs.append((round(s, 3), a, b))
pairs.sort(reverse=True)
print(json.dumps({
    "active_skill_md": len(files), "by_category": dict(sorted(by_cat.items())),
    "lines": {"total": sum(vals), "median": statistics.median(vals), "over_300": sum(x > 300 for x in vals),
              "over_400": sum(x > 400 for x in vals), "max": max(vals)},
    "validator_template_findings": dict(tmpl),
    "description_template_phrase": len(desc_t), "use_when_template_phrase": len(uw_t),
    "unique_text_pairs_gt_0_45": [{"score": s, "a": a, "b": b} for s, a, b in pairs],
}, indent=1))

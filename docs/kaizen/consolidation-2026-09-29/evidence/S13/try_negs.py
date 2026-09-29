"""Try candidate prompts for owned negatives. Usage: try_negs.py candidates.json"""
import json, sys, importlib.util
from pathlib import Path
root = Path(".")  # run from the engine root
spec = importlib.util.spec_from_file_location("r", root / "scripts" / "routing_smoke_test.py")
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
docs = r.catalogue(); texts = r.routing_texts()
fx = {f["id"]: f for f in json.loads((root / "tests/routing-fixtures.json").read_text(encoding="utf-8"))["fixtures"]}
cands = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
for fid, prompt in cands.items():
    f = fx[fid]
    def ranks(p):
        full = r.rank(p, docs)
        return full.index(f["negative_for"]) + 1, full.index(f["expected"]) + 1, full[0]
    cb, eb, _ = ranks(f["prompt"]); ca, ea, top = ranks(prompt)
    ok = ea <= 3 and ea < ca
    lint = r.prompt_leaks(prompt, f["expected"], texts[f["expected"]])
    print(f"{'OK ' if ok and not lint else 'BAD'} {fid}: comp {cb}->{ca} exp {eb}->{ea} top={top} {lint}")

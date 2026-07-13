#!/usr/bin/env python3
"""Dependency-light lexical routing smoke test for active social-media skills."""

from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"[a-z0-9]+")
STOP = {"a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from", "i", "in", "is", "it", "not", "of", "on", "or", "our", "that", "the", "this", "to", "use", "when", "with"}


def terms(text: str) -> list[str]:
    return [term for term in TOKEN.findall(text.lower().replace("e-commerce", "ecommerce")) if term not in STOP and len(term) > 1]


def catalogue() -> dict[str, Counter[str]]:
    docs = {}
    for path in sorted((ROOT / "skills").rglob("SKILL.md")):
        raw = path.read_text(encoding="utf-8")
        match = re.match(r"(?s)^---\n(.*?)\n---\n?", raw)
        if not match:
            continue
        front = yaml.safe_load(match.group(1)) or {}
        name = front.get("name")
        description = front.get("description", "")
        use_when = re.search(r"(?ims)^##\s+Use When\s*$\n(.*?)(?=^##\s+|\Z)", raw)
        searchable = f"{name} {name} {description} {use_when.group(1) if use_when else ''}"
        docs[name] = Counter(terms(searchable))
    return docs


def rank(prompt: str, docs: dict[str, Counter[str]]) -> list[str]:
    query = Counter(terms(prompt))
    document_frequency = defaultdict(int)
    for vector in docs.values():
        for term in vector:
            document_frequency[term] += 1
    scored = []
    for name, vector in docs.items():
        score = 0.0
        for term, q_count in query.items():
            if term in vector:
                idf = math.log((1 + len(docs)) / (1 + document_frequency[term])) + 1
                score += q_count * (1 + math.log(vector[term])) * idf
        phrase_bonus = sum(3 for part in name.split("-") if len(part) > 3 and part in prompt.lower())
        scored.append((score + phrase_bonus, name))
    return [name for _, name in sorted(scored, key=lambda item: (-item[0], item[1]))]


def main() -> int:
    fixture_data = json.loads((ROOT / "tests" / "routing-fixtures.json").read_text(encoding="utf-8"))
    docs = catalogue()
    top_k = fixture_data["top_k"]
    passed = 0
    failures = []
    for fixture in fixture_data["fixtures"]:
        ranked = rank(fixture["prompt"], docs)[:top_k]
        ok = fixture["expected"] in ranked
        passed += int(ok)
        if not ok:
            failures.append({"id": fixture["id"], "expected": fixture["expected"], "actual_top": ranked})
    total = len(fixture_data["fixtures"])
    precision = passed / total if total else 0.0
    print(f"routing fixtures={total} passed={passed} top_{top_k}_precision={precision:.3f} threshold={fixture_data['threshold']:.3f}")
    for failure in failures:
        print(f"FAIL {failure['id']}: expected={failure['expected']} actual={','.join(failure['actual_top'])}")
    return 0 if precision >= fixture_data["threshold"] and not failures else 1


if __name__ == "__main__":
    sys.exit(main())

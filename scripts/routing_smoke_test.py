#!/usr/bin/env python3
"""Dependency-light lexical routing smoke test for active social-media skills.

Reports top-k precision (gated by the fixture file's threshold) and precision@1.
Options (portfolio parity with the M10-03 routing ratchet):
  --min-rank1 PCT    fail when precision@1 (percent) falls below PCT. Without the flag the
                     registered floor `p1_floor` in tests/routing-fixtures.json (fraction)
                     applies, so the floor has one source of truth.
  --lint-fixtures    also fail on duplicate fixture ids, an `expected` skill that is not in
                     the active catalogue, an `expected` that is a retired alias, an
                     `alias_of` that is not a registered alias routed to `expected`, a
                     `negative_for` that is not another active skill, and (S08; portfolio
                     parity with M10-03-T05) a prompt that contains its expected skill's slug
                     as a phrase or copies the expected skill's routing text (word-trigram
                     overlap with its description + `Use When` of TRIGRAM_LIMIT or more).
Optional fixture fields:
  `alias_of`      the retired skill (directory name or path) whose old job the prompt
                  describes; the fixture then proves the alias still reaches its owner.
  `negative_for`  the skill whose description names `expected` in its "not for" clause. The
                  fixture is that skill's owned negative (S08): it passes only when `expected`
                  is in the top k AND ranks above the `negative_for` skill.
"""

from __future__ import annotations

import argparse
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


TRIGRAM_LIMIT = 0.4


def routing_texts() -> dict[str, str]:
    """Description + `Use When` text per active skill (the text a fixture must not copy)."""
    texts = {}
    for path in sorted((ROOT / "skills").rglob("SKILL.md")):
        raw = path.read_text(encoding="utf-8")
        match = re.match(r"(?s)^---\n(.*?)\n---\n?", raw)
        if not match:
            continue
        front = yaml.safe_load(match.group(1)) or {}
        use_when = re.search(r"(?ims)^##\s+Use When\s*$\n(.*?)(?=^##\s+|\Z)", raw)
        texts[front.get("name")] = f"{front.get('description', '')}\n{use_when.group(1) if use_when else ''}"
    return texts


def word_trigrams(text: str) -> set[tuple[str, ...]]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {tuple(words[i : i + 3]) for i in range(len(words) - 2)}


def prompt_leaks(prompt: str, slug: str, routing_text: str) -> list[str]:
    """Slug-in-prompt and routing-text copy findings (adapted from the portfolio M10-03-T05 lint)."""
    findings: list[str] = []
    normal = " " + re.sub(r"[^a-z0-9]+", " ", prompt.lower()).strip() + " "
    phrase = re.sub(r"^\d+-", "", slug.lower()).replace("-", " ").strip()
    if phrase and f" {phrase} " in normal:
        findings.append(f"slug-in-prompt '{phrase}'")
    grams = word_trigrams(prompt)
    if grams:
        overlap = len(grams & word_trigrams(routing_text)) / len(grams)
        if overlap >= TRIGRAM_LIMIT:
            findings.append(f"routing-text copy (trigram overlap {overlap:.2f})")
    return findings


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


def alias_routes() -> dict[str, str]:
    """Registered retired-skill routes keyed by alias directory name -> owner directory name."""
    registry = ROOT / "docs" / "skill-aliases.yml"
    if not registry.is_file():
        return {}
    data = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
    routes = data.get("inactive_skill_aliases") or {}
    return {Path(str(src)).name: Path(str(dst)).name for src, dst in routes.items()}


def lint_fixtures(fixtures: list[dict], docs: dict[str, Counter[str]]) -> list[str]:
    findings: list[str] = []
    routes = alias_routes()
    texts = routing_texts()
    seen: set[str] = set()
    for fixture in fixtures:
        if fixture.get("expected") in texts:
            for leak in prompt_leaks(fixture.get("prompt", ""), fixture["expected"], texts[fixture["expected"]]):
                findings.append(f"LINT {fixture.get('id')}: {leak}")
        negative_for = fixture.get("negative_for")
        if negative_for is not None and (negative_for not in docs or negative_for == fixture.get("expected")):
            findings.append(f"LINT {fixture.get('id')}: negative_for `{negative_for}` must be another active skill")
        fid, expected = fixture.get("id"), fixture.get("expected")
        if fid in seen:
            findings.append(f"LINT {fid}: duplicate fixture id")
        seen.add(fid)
        if expected in routes:
            findings.append(f"LINT {fid}: expected `{expected}` is a retired alias; expect its owner `{routes[expected]}`")
        elif expected not in docs:
            findings.append(f"LINT {fid}: expected `{expected}` is not an active skill")
        alias_of = fixture.get("alias_of")
        if alias_of is not None:
            alias_name = Path(str(alias_of)).name
            if routes.get(alias_name) != expected:
                findings.append(f"LINT {fid}: alias_of `{alias_of}` is not a registered alias routed to `{expected}`")
    return findings


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--min-rank1", type=float, default=None, help="Fail when precision@1 (percent) is below this floor.")
    parser.add_argument("--lint-fixtures", action="store_true", help="Fail on fixture ids, expected skills or alias_of fields that do not resolve.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    options = parse_args(argv)
    fixture_data = json.loads((ROOT / "tests" / "routing-fixtures.json").read_text(encoding="utf-8"))
    docs = catalogue()
    top_k = fixture_data["top_k"]
    passed = 0
    rank1 = 0
    failures = []
    negatives = negatives_passed = 0
    negative_failures = []
    for fixture in fixture_data["fixtures"]:
        full = rank(fixture["prompt"], docs)
        ranked = full[:top_k]
        ok = fixture["expected"] in ranked
        passed += int(ok)
        rank1 += int(bool(ranked) and ranked[0] == fixture["expected"])
        if not ok:
            failures.append({"id": fixture["id"], "expected": fixture["expected"], "actual_top": ranked})
        negative_for = fixture.get("negative_for")
        if negative_for in docs and fixture["expected"] in docs:
            negatives += 1
            if ok and full.index(fixture["expected"]) < full.index(negative_for):
                negatives_passed += 1
            else:
                negative_failures.append(f"FAIL owned negative {fixture['id']}: `{fixture['expected']}` must rank above `{negative_for}` (actual={','.join(ranked)})")
    total = len(fixture_data["fixtures"])
    precision = passed / total if total else 0.0
    p_at_1 = rank1 / total if total else 0.0
    print(f"routing fixtures={total} passed={passed} top_{top_k}_precision={precision:.3f} threshold={fixture_data['threshold']:.3f}")
    floor = fixture_data.get("p1_floor")
    floor_text = f" registered_floor={floor * 100:.1f}%" if isinstance(floor, (int, float)) else ""
    print(f"precision@1={rank1}/{total} ({p_at_1 * 100:.1f}%){floor_text} (lexical proxy, not live routing)")
    print(f"owned negatives={negatives} passed={negatives_passed} failed={negatives - negatives_passed}")
    for failure in failures:
        print(f"FAIL {failure['id']}: expected={failure['expected']} actual={','.join(failure['actual_top'])}")
    for failure in negative_failures:
        print(failure)
    exit_code = 0 if precision >= fixture_data["threshold"] and not failures and not negative_failures else 1
    min_rank1 = options.min_rank1
    if min_rank1 is None and isinstance(floor, (int, float)):
        min_rank1 = floor * 100  # the registered floor applies even without the flag
    if min_rank1 is not None and p_at_1 * 100 < min_rank1:
        print(f"FAIL precision@1 {p_at_1 * 100:.1f}% is below the floor {min_rank1:g}%")
        exit_code = 1
    if options.lint_fixtures:
        lint = lint_fixtures(fixture_data["fixtures"], docs)
        print(f"fixture lint: {len(lint)} finding(s)")
        for finding in lint:
            print(finding)
        if lint:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())

# Social Kaizen 2026-09-29: close snapshot diff (S13-T01)

- **Before:** [baseline-snapshot.json](baseline-snapshot.json), start commit `38b6c9a` (191 active skills).
- **After:** [close-snapshot.json](close-snapshot.json), HEAD `e7d68fd` plus the uncommitted S13 working tree (112 active skills), measured 29 Sep 2026.
- **Method:** the structural measures were run with the same code on both trees ([measure_close.py](evidence/S13/measure_close.py) on a `git archive` of `38b6c9a` and on the close tree; `scripts/measure_skill_scaffolding.py --root` for both). Routing figures come from `scripts/routing_smoke_test.py` and [measure_routing.py](evidence/S13/measure_routing.py). The collision figures come from the chwezi-engine-agents union scan. Gate output: [gate-block-2026-09-29.txt](evidence/S13/gate-block-2026-09-29.txt).
- **Limits:** every routing figure is a lexical proxy, not live routing. Tier 3 (model-executed behaviour) is `NOT_ASSESSED (zero-spend rule)`.

## Before and after (roadmap §9 success measures, plus extra close measures)

| Measure | Baseline (S01, 191) | Close (S13, 112) | Target | Met? |
|---|---|---|---|---|
| Active `SKILL.md` | 191 | **112** (83 inactive `ALIAS.md` routes; cap 120) | 112, cap 120 | yes |
| Median SKILL.md lines | 287 (288 in plan 01, which counted a trailing line) | **121** | ≤ 200 | yes |
| SKILL.md files over 300 / over 400 / maximum | 84 / 27 / 500 | **0 / 0 / 162** | 0 over 300 | yes |
| SKILL.md lines, total | 55,210 | 13,742 | — | depth moved to references |
| Reference files / lines | 145 / 14,708 | 369 / 51,424 | — | knowledge kept in `references/` |
| Templated descriptions, plan 01 hand classification | 105 | **0** | 0 | yes |
| Templated descriptions, validator phrase list (same classifier on both trees) | 170 | **0** | 0 | yes |
| Templated `Use When` bodies, plan 01 / validator phrase list | 117 / 170 | **0 / 0** | 0 | yes |
| Validator routing-text findings (`description_template`, `description_formula`, `use_when_template`) | 170 / 191 / 181 (not enforced then) | **0 / 0 / 0** (enforced) | 0 | yes |
| Shared-line ratio, gated median (D-SK-10a meter) | 14.5 % | **1.4 %** | ≤ 12 % | yes on the gated measure ratified in D-SK-10(a); the roadmap's baseline figure (30.5 %) used the raw measure, which is 30.9 % at close (next row) |
| Shared-line ratio, raw median (plan-time method) | 30.5 % | 30.9 % | — | not a target: raw counts the structural lines the validator requires, which now form a larger share of shorter files (D-SK-10a) |
| Near-duplicate pairs, unique-text cosine > 0.45 (same method on both trees) | 12 (plan 01 reported 6 with a slightly different tokenisation) | **1** (`ai-generative-search-optimisation` / `seo-geo-optimisation`, 0.58; different jobs, declared neighbours) | — | reduced |
| Within-engine lexical pairs ≥ 0.75 | 9 | **0** | 0 | yes |
| Cross-engine pairs ≥ 0.75 involving social / undeclared | 7 (all declared) / 0 | **0 / 0** | 0 undeclared | yes |
| Routing fixtures | 56 | **392** (240 positive, 142 collision, 6 failure-path, 4 limited-capability; 83 alias fixtures) | ≥ 150 | yes |
| Skills named as expected by a fixture | 44 of 191 | **112 of 112** | 112 of 112 | yes |
| Routing top-3 | 1.000 | **1.000** | 1.000 | yes |
| Routing p@1 (lexical proxy) | 51/56 = 91.1 % (unreported by the harness then) | **373/392 = 95.2 %** | ≥ 92 %, floor registered | yes (floor 92 in `tests/routing-fixtures.json` and chwezi-engine-agents `evals/routing/baseline.json`) |
| Owned-negative fixtures (`negative_for`) | 0 (20 collision fixtures without an owner) | **121**, 121 pass | ≥ 40 | yes |
| Owned negatives with the competitor in the top 3 / ranks 4–10 / below 10 | — | 73 / 47 / 1 (S11 close: 36 / 34 / 51) | — | sharpened in S13 |
| Independent 60-prompt holdout p@1 / top-3 | not built | 48/60 (80.0 %) / 54/60 (90.0 %) | — | measured |
| Skills with ≥ 3 `positive`-type fixtures and ≥ 2 owned negatives (T2_cov) | 0 of 191 | 4 of 112 (3.6 %; 6 if collision fixtures count as positives) | — | weak; next opportunity |
| Benchmark matrix STRONG / THIN / GAP (133 rows) | 44 / 54 / 35 | **129 / 4 / 0** | 0 GAP; THIN only where `NOT_ASSESSED` | yes |
| East Africa rows STRONG / THIN / GAP / DEFECT (23) | 5 / 13 / 3 / 2 | **16 / 7 / 0 / 0** | 0 defects | yes |
| Source-register records within review windows | 63 | 179 | — | — |
| Engine Eval Readiness (M10-14 formula) | 40.0 | **59.9** | — | see [scorecard.md](scorecard.md) |
| Tier-3 behavioural evidence | none | `NOT_ASSESSED (zero-spend rule)` | stated as such | yes |
| Validator / alias check / tests | 191 compliant; aliases 0 routes; 48 tests | 112 compliant; 83 routes, 0 findings; 70 tests + 18 subtests | green | yes |

Every roadmap §9 row has a measured value. The two rows that are not improvements, the raw shared-line median and T2 coverage, are explained above and carried to the record's "Next opportunities".

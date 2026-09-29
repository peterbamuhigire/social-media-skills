# Social Kaizen 2026-09-29: close scorecard (S13-T05)

- **Engine:** `social-media-skills` at HEAD `e7d68fd` plus the S13 working tree; 112 active skills.
- **Rubric:** chwezi-dev-engine `skills/sdlc-meta/skill-engine-audit` (`references/scoring-rubric.md`, including "Engine Eval Readiness (measured)", and `references/eval-readiness-worked-example.md`), portfolio rule AO-14 (my-10-kaizen M10-14): `NOT_ASSESSED` = 0; routing is capped at 50 without harness output; with harness output the routing dimension is the Readiness score; published = `min(measured-constrained, 65)`.
- **Bar:** the top 0.1 % of full-service digital marketing and advertising agencies. Default band 45–65; no dimension is scored 70 or above.
- **Recompute:** `python -X utf8 evidence/S13/compute_scorecard.py` reads only [scorecard-inputs.json](evidence/S13/scorecard-inputs.json) and prints every number below.
- **Limits:** T2 figures are a lexical drift guard, not proof of live routing. Tier 3 is `NOT_ASSESSED (zero-spend rule)`: no `grading.json` exists for this engine.

## 1. Engine Eval Readiness (measured)

| Slot | Measured input | Fraction | Source |
|---|---|---|---|
| T1 | 4 of 4 declared validators pass (`validate_skill_engine.py --baseline`, `routing_smoke_test.py --lint-fixtures`, `check_source_freshness.py`, `check_skill_aliases.py`) | 1.0000 | `catalog/engines.yaml` list; [gate block](evidence/S13/gate-block-2026-09-29.txt) |
| T2_p1 | 373 / 392 | 0.9515 | routing smoke test |
| T2_neg | 121 / 121 owned negatives pass | 1.0000 | routing smoke test |
| T2_cov | 4 / 112 skills have ≥ 3 `positive`-type fixtures expecting them and ≥ 2 owned negatives naming them in `negative_for` (collision fixtures are not counted as positives; counting them gives 6 / 112) | 0.0357 | [measure_routing.py](evidence/S13/measure_routing.py) |
| T2_clean | 0 cross-engine pairs ≥ 0.75 involving social (engine in the union scan) | 1.0000 | `validate-runtime-skill-budget.py --collisions` |
| T3 | 0 executed; every planned run `NOT_ASSESSED (zero-spend rule)` | 0 | — |

- T1 points = 30 × 1.0000 = **30.00**
- T2 mean = (0.9515 + 1.0000 + 0.0357 + 1.0000) ÷ 4 = 0.7468; T2 points = 40 × 0.7468 = **29.87**
- T3 points = **0.00** (the slot stays in the formula)
- **Readiness = 59.9 / 100** (M10-14 baseline for this engine: **40.0**, when p@1 was unreported and there were no owned negatives). While T3 is unexecuted the Readiness ceiling is 70.

## 2. Judged dimensions (strict)

| Dimension (weight) | Score | Kind | Justification: named deficiencies |
|---|---|---|---|
| Output-type readiness and coverage (30 %) | 58 | judged | Every service line in the 133-row benchmark now has an owner and 129 rows are STRONG, but readiness is coverage of guidance, not proven output: no worked client deliverable has been executed and graded (Tier 3 0). Four matrix and seven East Africa rows stay THIN on `NOT_ASSESSED` evidence (Gartner CMO spend, IAB CTV, CIM competencies, Uganda UCC advertising standard, Kenya gambling directive, Tanzania data and online-content law, Uganda data tax). Visual execution is correctly delegated to the design engine, so finished creative is outside this engine. |
| Skill depth and worked examples (25 %) | 55 | judged | The lean template moved depth into 369 reference files (51,424 lines), and most references carry procedures and East African illustrations. However: worked examples are uneven and mostly illustrative prose, not before/after artefacts; the S10 "internal contradictions" backlog (posting frequency, RAG thresholds, MQL scores, confidence levels, email cadence and others; `citation-backlog.md` §4) is unresolved; 18 citations are marked "verify" or "verify at use" and 6 are `NOT_ASSESSED`. |
| Standards currency (15 %) | 62 | judged | 179 register records within review windows (63 at baseline); legal-currency defects fixed; WhatsApp pricing read live with the 1 Oct 2026 change; MMM, programmatic, consent and AI-disclosure standards registered. Deductions: eleven `NOT_ASSESSED` legal/market texts; legacy short labels (`AD-08`, `KE-01`, `UG-01` and others) in four files are not register IDs (S13 benchmark finding); pricing and UI-path claims are marked "verify at use" rather than registered. |
| Taxonomy and structure (10 %) | 62 | judged | 112 skills in 15 categories with no grab-bag; `frameworks/` now aliases only. Deductions: `policies` (1) and `sectors`/`seo-discovery` (2 each) are thin groups; `meta-analytics-ops` (13) and `playbooks` (17) are broad; the numbered pipeline mixes intake and strategy stages. |
| Doctrine and philosophy (10 %) | 63 | judged | Clear cap, lean template, authority boundary sentence, currentness gate, design-authority rule and no-book-extraction rule, all enforced by validators. Deduction: the doctrine of effectiveness (brand-building science, 60:40, triangulated measurement) is new in S10 and not yet threaded through the older playbooks. |
| Redundancy and hygiene (third of 10 %) | 64 | judged | 0 within-engine and 0 cross-engine pairs ≥ 0.75; 1 unique-text pair above 0.45 (12 at baseline); 83 retired skills are inactive routes with preservation maps (39 audited in S13, 0 dropped). Deduction: 83 verbatim `ALIAS.md` files remain on disk by decision D-SK-11. |
| Discovery and routing (third of 10 %) | 62 judged; **59.9 measured** | measured | See §1. The measured Readiness replaces the judged score in the measured-constrained number. Weakest input: T2 coverage 3.6 %. |
| Safety and integrity (third of 10 %) | 60 | judged | Authority boundary on every skill; source-ingestion guardrail 0; no book extractions; the Verma catalogue was rewritten in the engine's words in S13. The 3 NEW skills were safety-audited as Safe in S10 (read-only). Deductions: the safety gate was not re-run on the 110 S09-rewritten skills; several claims are marked "verify" rather than verified; legacy unregistered source labels remain in four files. |

## 3. Three published numbers

Weighting (rubric default): output 30 %, depth 25 %, standards 15 %, taxonomy 10 %, doctrine 10 %, hygiene 10 % (hygiene = mean of redundancy, routing and safety).

| Number | Hygiene | Overall |
|---|---|---|
| **Raw** (routing judged 62) | (64 + 62 + 60) ÷ 3 = 62.00 | 17.40 + 13.75 + 9.30 + 6.20 + 6.30 + 6.20 = **59.2** |
| **Measured-constrained** (routing = Readiness 59.9) | (64 + 59.9 + 60) ÷ 3 = 61.30 | 17.40 + 13.75 + 9.30 + 6.20 + 6.30 + 6.13 = **59.1** |
| **Published** (`min(59.1, 65)`) | — | **59.1 / 100** |

Headline with the three numbers: **raw 59.2, measured-constrained 59.1, published 59.1; Engine Eval Readiness 59.9 (Tier 3 0 of 30).** There is no judged score for the 191-skill baseline to compare against: the only baseline score is the measured Readiness of 40.0 (M10-14). The judged scores above are this audit's first strict scores for the engine and are the reference for the next re-audit.

## 4. `NOT_ASSESSED` list (each scores 0 or is excluded from any claim)

1. T3 behavioural runs: `NOT_ASSESSED (zero-spend rule)`, 30 Readiness points.
2. Live routing (all T2 figures are lexical).
3. Output quality of any deliverable in a live session.
4. The 11 THIN benchmark rows' evidence gaps (listed in [benchmark-rescore.md](evidence/S13/benchmark-rescore.md)).
5. The six citations left `NOT_ASSESSED` and 18 marked "verify" in [citation-backlog.md](evidence/S13/citation-backlog.md) (web search budget exhausted; Open Library only).
6. Paraphrase quality of the 44 preservation maps not sampled in S13 (39 of 83 audited).

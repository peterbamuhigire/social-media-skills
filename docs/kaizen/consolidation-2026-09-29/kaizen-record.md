# Kaizen record: Social Kaizen 2026-09-29, consolidation and world-class quality (S01–S13)

Append-only after acceptance. Corrections are dated addenda at the end.

## 1. Scope

- **Engine:** `social-media-skills`, the Chwezi digital marketing and advertising engine.
- **Order (Peter, 29 Sep 2026):** a hard maximum of 120 active skills, and quality, not only count: "we better be the best social media / digital marketing agency in the world with this". Zero spend. British English. No book extractions.
- **Plan:** Social Kaizen 2026-09-29 (13 phases, S01–S13), held outside the repository. Decisions: [decisions.md](decisions.md) (D-SK-01 to D-SK-11). Phase log: [execution-log.md](execution-log.md). Runbook: [merge-runbook.md](merge-runbook.md).
- **Dates:** planned, executed and closed on 29 September 2026.
- **Authority:** Peter's full approval to implement the plan, exercised by the orchestrator. Every decision is recorded as "ratified by orchestrator under Peter's delegated authority" unless Peter's own order is cited.
- **Cross-engine scope:** chwezi-engine-agents (ownership row D-SK-07, routing floor and oracles in S11, marketplace text, catalogue alias gate, engine tours and skill graph in S12, the operations record in S13).

## 2. Baseline

[baseline-snapshot.json](baseline-snapshot.json) at start commit `38b6c9a`:

- 191 active `SKILL.md` (190 task skills + the `content-writing` category file);
- median 287 lines, 84 files over 300;
- 105 templated descriptions and 117 templated `Use When` bodies (plan hand classification);
- gated shared-line median 14.5 % (raw 30.5 %);
- 56 routing fixtures naming 44 skills; p@1 91.1 % (unreported); no owned negatives;
- 9 within-engine and 7 cross-engine lexical pairs ≥ 0.75 (all cross pairs declared);
- benchmark 44 STRONG / 54 THIN / 35 GAP; East Africa 2 legal-currency defects;
- Engine Eval Readiness 40.0 (M10-14).

## 3. Findings that shaped the work

1. The near-duplicate scores were mostly shared scaffolding: on unique text only a handful of pairs overlapped. Merges were therefore decided on job overlap and usage (D-SK-04), and scaffolding was fixed separately by the lean template (D-SK-06).
2. Templating covered the routing text itself, so the 91 % p@1 rested on skill names.
3. Three service lines a leading agency sells were missing (brand-building science, MMM with calibrated incrementality, programmatic/CTV/DOOH with brand safety), and privacy-safe tracking was fragmented.
4. Live legal-currency defects: the void Uganda Computer Misuse (Amendment) Act 2022 was cited as law, and Facebook's status in Uganda was stale.

## 4. Changes (commits per phase)

| Phase | Change | Active | Commit |
|---|---|---|---|
| S01 | Alias registry `docs/skill-aliases.yml`, `scripts/check_skill_aliases.py`, cap and p@1 gates, baseline snapshot, decisions | 191 | `008896a` |
| S10-T01 | Legal currency (D-SK-02, pushed early): Computer Misuse ruling, Facebook status, shutdown contingency, EAC register rows | 191 | `7c60138` |
| S02 | 15 AI marketing, governance and automation merges into 8 owners | 176 | `26028ad` |
| S03 | 14 content, creative and prompt-library merges into 10 owners; ownership row re-pointed (D-SK-07) | 162 | `8eacccb` |
| S04 | 12 measurement and analytics merges into 8 owners; NEW `measurement-tracking-plan` | 151 | `dfdb35a` |
| S05 | 19 pipeline, audience, lifecycle and channel merges into 13 owners | 132 | `ce3299a` |
| S06 | 15 community, reputation, PR, selling and commerce merges into 10 owners | 117 | `f8aa1e7` |
| S07 | 7 business-development and training merges; cap enforced strictly | 110 | `b3d0ac2` |
| S08 | 110 descriptions and `Use When` rewritten to the formula; owned negatives; floor 92 | 110 | `9a7ec76` |
| S09 | Lean template and 300-line ceiling; `line_budget` and shared-line meter | 110 | `3416d0b` |
| S10 | NEW `brand-strategy-and-distinctive-assets` (offset by merging `ecommerce-brand-differentiation`), `marketing-mix-modelling`, `programmatic-and-brand-safety`; gap-fill references; 91 register records | 112 | `973e1af` |
| S11 | Routing and collision re-baseline; social floor in the portfolio ratchet | 112 | `55f66b4` |
| S12 | README catalogue and 83 retired routes from the filesystem; router text; manifest gates; count-surface test | 112 | `e7d68fd` |
| S13 | Close re-audit; Verma catalogue rewritten in the engine's words; 50 owned negatives sharpened; citation backlog; plan benchmark text corrected; D-SK-11; records | 112 | set by the orchestrator |

In total: 83 skills retired as inactive `ALIAS.md` routes, each with a preservation map; 4 NEW skills; 110 skills rewritten to the lean template.

## 5. Commands and results (final run, 29 Sep 2026)

Full output: [evidence/S13/gate-block-2026-09-29.txt](evidence/S13/gate-block-2026-09-29.txt).

| Command (engine root unless stated) | Result |
|---|---|
| `python -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json` | skills=112 compliant=112 failures=0 median_lines=121.0 |
| `python -X utf8 scripts/routing_smoke_test.py --min-rank1 92 --lint-fixtures` | 392/392 top-3 (1.000); p@1 373/392 (95.2 %); owned negatives 121/121; lint 0 |
| `python -X utf8 scripts/check_skill_aliases.py` | routes=83 findings=0 active=112 cap=120 |
| `python -X utf8 scripts/check_source_freshness.py` | PASS, 179 records within review windows |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | findings 0 |
| `python -X utf8 scripts/measure_skill_scaffolding.py --max-median 12` | gated median 1.4 %, 0 files over 300 |
| `python -X utf8 -B -m pytest -q tests`; `python -X utf8 -m unittest discover -s tests -p "test_*.py"` | 70 passed + 18 subtests; 70 OK |
| `git diff --check` | clean |
| chwezi-engine-agents: `render_host_files.py --check` (1 and 12 repositories) | findings 0 |
| chwezi-engine-agents: `validate-runtime-skill-budget.py --collisions --ownership evals/routing/ownership.yaml`; `lexical_routing.py --collisions` | PASS, 0 undeclared ≥ 0.75; exit 0 |
| chwezi-engine-agents: `validate-routing-baseline.py`; `validate-no-book-extractions.py` | PASS; roots=12 findings=0 |
| chwezi-engine-agents: `node scripts/generate-plugin-manifest.js --check-marketplace --workspace-root ..` | 23 ok, 0 drift |

## 6. Before and after

Full table: [close-snapshot-diff.md](close-snapshot-diff.md).

| Measure | Before (191) | After (112) |
|---|---|---|
| Active skills (cap 120) | 191 | **112** |
| Median SKILL.md lines / files over 300 | 287 / 84 | **121 / 0** |
| Templated descriptions (plan / validator phrase list) | 105 / 170 | **0 / 0** |
| Templated `Use When` bodies (plan / validator phrase list) | 117 / 170 | **0 / 0** |
| Shared-line ratio, gated median (raw) | 14.5 % (30.5 %) | **1.4 %** (30.9 %); the ≤ 12 % target is met on the gated measure ratified in D-SK-10(a), not on the raw measure the roadmap baseline used |
| Near-duplicate pairs: unique text > 0.45 / within-engine lexical ≥ 0.75 | 12 / 9 | **1 / 0** |
| Cross-engine pairs ≥ 0.75 (undeclared) | 7 (0) | **0 (0)** |
| Routing fixtures / skills expected by a fixture | 56 / 44 | **392 / 112** |
| Routing p@1 / top-3 (lexical proxy) | 91.1 % / 1.000 | **95.2 % / 1.000** |
| Owned negatives (pass) | 0 | **121 (121)**; competitor top 3 / 4–10 / below 10 = 73 / 47 / 1 |
| Holdout p@1 / top-3 (60 prompts, never tuned on) | — | 80.0 % / 90.0 % |
| Benchmark STRONG / THIN / GAP (133 rows) | 44 / 54 / 35 | **129 / 4 / 0** |
| East Africa STRONG / THIN / GAP / DEFECT (23 rows) | 5 / 13 / 3 / 2 | **16 / 7 / 0 / 0** |
| Source-register records within review windows | 63 | 179 |
| Engine Eval Readiness | 40.0 | **59.9** |
| Published score (raw / measured-constrained / published) | not scored | **59.2 / 59.1 / 59.1** ([scorecard.md](scorecard.md)) |

Preservation: 39 of 83 maps audited in S13 (all 19 whose source had reads, plus 20 stratified by phase), 0 dropped items ([preservation-audit.md](evidence/S13/preservation-audit.md)).

## 7. NOT_ASSESSED items and evidence limits

1. Tier 3 behavioural runs: `NOT_ASSESSED (zero-spend rule)`; they cost 30 of 100 Readiness points and cap Readiness at 70.
2. Live routing: every routing figure is a lexical proxy. Some sharpened negatives state a client fact that rules out the competitor; a lexical ranker cannot read that, so they measure resistance to vocabulary, not true discrimination.
3. Output quality of deliverables in a live session.
4. Evidence gaps behind the 11 THIN benchmark rows (4 matrix, 7 East Africa), listed in [benchmark-rescore.md](evidence/S13/benchmark-rescore.md).
5. Citations: 18 marked "verify", 6 `NOT_ASSESSED` ([citation-backlog.md](evidence/S13/citation-backlog.md)); the session's web-search allowance ran out, so checks used Open Library only.
6. Paraphrase quality of the 44 preservation maps not sampled in S13.
7. Usage figures come from the local August–September 2026 scan and were evidence only.

## 8. Rollback

- Programme start (last pre-Kaizen commit): `38b6c9a`. Each phase is one commit (table in §4); revert in reverse order.
- Retired skills are recoverable without a revert: each `ALIAS.md` keeps its verbatim text (D-SK-11), its route in `docs/skill-aliases.yml`, and a preservation map naming where each item went.
- S13 itself changes records, fixture prompts, one skill's reference text and citation lines; `git revert` of the S13 commit restores the S12 state.
- chwezi-engine-agents changes are separate commits (S03 ownership row, S10 marketplace count, S11 floor and oracles, S12 marketplace text and tours, S13 operations record).

## 9. Next opportunities

| # | Item | Owner | Trigger |
|---|---|---|---|
| N1 | Tier-3 behavioural runs for a sample of social skills (the only route above Readiness 70) | Peter (spend approval), then the orchestrator | Peter approves model-run spend |
| N2 | T2 coverage: raise skills with ≥ 3 fixtures and ≥ 2 owned negatives from 4 to at least 56 of 112 | next social routing pass | next social Kaizen or any routing-text change |
| N3 | Raise the social p@1 floor from 92 to 93 (measured 95.2 % minus 2, rounded down) and refresh the social block in `evals/routing/baseline.json` | orchestrator (workflow-routing) | next ratchet review |
| N4 | `kaizen-improvement-system-not-single-draft`: tune `anti-ai-slop` routing text so an honest negative can bring the competitor into range | next routing pass | same as N2 |
| N5 | Internal contradictions of doctrine (posting frequency, RAG thresholds, MQL scores, confidence levels, email cadence, SLA and timing tables and others; [citation-backlog.md](evidence/S13/citation-backlog.md) §4) | social engine maintainer | next social content Kaizen |
| N6 | Close the 18 "verify" and 6 `NOT_ASSESSED` citations with a web-enabled pass | social engine maintainer with the digital-research-engine | next session with search budget |
| N7 | Research wave for the 11 THIN benchmark rows (UCC advertising standard, Kenya gambling directive, Tanzania laws, Uganda data tax, Gartner CMO spend, IAB CTV, CIM competencies) | digital-research-engine wave | review dates on the register rows, or a client campaign in the jurisdiction |
| N8 | Replace legacy short source labels (`AD-08/09/10`, `KE-01`, `UG-01/03`, `TZ-01`, `KE-07`–`09`, `MK-02`) in four files with register IDs | social engine maintainer | next currency pass |
| N9 | Review dates of the 179 register records (WhatsApp pricing is quarterly; re-read after 1 Oct 2026) | `check_source_freshness.py` (automatic) | a record's review date passes |
| N10 | Full preservation audit of the remaining 44 maps, then decide whether to trim `ALIAS.md` bodies (D-SK-11 review) | next social Kaizen | next social Kaizen |
| N11 | Re-run the dev `skill-safety-gate` across the 110 lean-template rewrites | orchestrator | next portfolio safety sweep |

## 10. Review

Independent review: [evidence/S13/independent-review.md](evidence/S13/independent-review.md), verdict `ACCEPT_WITH_DOCUMENTED_LIMITATIONS` (no blocking finding; 7 minor findings, 6 fixed and 1 observation; responses in [S13-evidence.md](evidence/S13/S13-evidence.md)). Each earlier phase's verdict is in [execution-log.md](execution-log.md). Record-path note: this record sits beside the scorecard at the path the orchestrator's S13 brief named, not at the phase file's `docs/kaizen/kaizen-2026-09-29-social-consolidation.md`.

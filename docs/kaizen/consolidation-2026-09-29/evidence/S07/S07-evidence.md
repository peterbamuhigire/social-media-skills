# S07 evidence: agency business development and training merges; consolidation window closed

- **Date:** 29 September 2026.
- **Executor:** Claude (Opus 5.5) under the Social Kaizen executor brief; the orchestrator commits. Four merge workers did steps 1–6 of the [merge runbook](../../merge-runbook.md) for seven target clusters; the coordinator did steps 7–10 and S07-T-CAP.
- **Start state:** HEAD `ce3299a` plus the uncommitted S06 changes (S06 saved as git tree `69cca10` with `git add -A && git write-tree` followed by `git reset -q`, index only; the orchestrator commits S06 separately, before this phase). Rollback: revert the S07 commit.
- **Active skills:** 117 → **110** (7 MERGE-INTO). The S02–S07 consolidation window is closed: the hard cap of 120 is now enforced strictly.
- **Authority:** decisions ratified by orchestrator under Peter's delegated authority, 29 Sep 2026 (D-SK-01, D-SK-03, D-SK-04; see [decisions.md](../../decisions.md)).
- **Git:** no commit or `git mv`; plain renames and moves. The orchestrator should stage each `SKILL.md` deletion with its new `ALIAS.md`, and the moved training references with their destinations, so git records renames.

## Tasks

| Task | Target | Sources → reference | Status |
|---|---|---|---|
| S07-T01 | `biz-dev-credentials` | `biz-dev-case-study` → `case-study-method.md` (its `proposal-frameworks.md` is byte-identical to the target's copy and stays in the alias folder) | DONE |
| S07-T02 | `biz-dev-lawful-prospecting-outreach` | `biz-dev-video-outreach` → `personalised-video-outreach.md` | DONE |
| S07-T03 | `biz-dev-positioning` | `biz-dev-practitioner-positioning` → `practitioner-positioning.md` | DONE |
| S07-T04 | `biz-dev-pricing-menu` | `biz-dev-beyond-agency-offer` → `risk-reversed-entry-offer.md` | DONE |
| S07-T05 | `playbook-agency-operations` | `playbook-white-label-partnerships` → `white-label-and-partner-delivery.md` | DONE |
| S07-T06 | `training-ai-foundations` | `training-ai-prompt-writing` → `prompt-writing-module.md` (+ moved `copy-frameworks-and-practice.md`, `prompt-foundations-and-structure.md`) | DONE |
| S07-T07 | `training-client-team` | `training-diy-content` → moved and extended `diy-content-handbook.md` | DONE |
| S07-T08 | fixtures | 7 alias-routing fixtures; `outreach-collision` re-pointed from `biz-dev-video-outreach` to `biz-dev-lawful-prospecting-outreach` | DONE: all 7 and the re-pointed fixture rank 1 |
| S07-T09 | count and registry | `quality-baseline.json` and `docs/skill-aliases.yml` = 110; 7 routes added (82 cumulative) | DONE |
| S07-T-CAP | close the consolidation window | `consolidation_until` removed from `docs/skill-aliases.yml`; `tests/test_engine_quality.py` now asserts the key is absent and active ≤ `hard_cap` | DONE: in a scratch copy with 11 synthetic skills (121 active, counts in lockstep), `check_skill_aliases.py` exit 1 (`cap-exceeded`), `validate_skill_engine.py` exit 1 (`catalogue_cap_exceeded`), and `test_active_count_agrees_and_respects_cap` fails; the copy was then deleted |

## Merges

| Source | Target | Reference | Preservation map (rows; rows containing `DROPPED`) | Gates | Commit |
|---|---|---|---|---|---|
| `biz-dev-case-study` | `biz-dev-credentials` | `case-study-method.md` | [25; 3](../../preservation/biz-dev-case-study.md) | green | set by the orchestrator |
| `biz-dev-video-outreach` | `biz-dev-lawful-prospecting-outreach` | `personalised-video-outreach.md` | [28; 2](../../preservation/biz-dev-video-outreach.md) | green | set by the orchestrator |
| `biz-dev-practitioner-positioning` | `biz-dev-positioning` | `practitioner-positioning.md` | [35; 2](../../preservation/biz-dev-practitioner-positioning.md) | green | set by the orchestrator |
| `biz-dev-beyond-agency-offer` | `biz-dev-pricing-menu` | `risk-reversed-entry-offer.md` | [25; 2](../../preservation/biz-dev-beyond-agency-offer.md) | green | set by the orchestrator |
| `playbook-white-label-partnerships` | `playbook-agency-operations` | `white-label-and-partner-delivery.md` | [28; 2](../../preservation/playbook-white-label-partnerships.md) | green | set by the orchestrator |
| `training-ai-prompt-writing` | `training-ai-foundations` | `prompt-writing-module.md`, moved `copy-frameworks-and-practice.md`, `prompt-foundations-and-structure.md` | [19; 1](../../preservation/training-ai-prompt-writing.md) | green | set by the orchestrator |
| `training-diy-content` | `training-client-team` | moved `diy-content-handbook.md` | [13; 1](../../preservation/training-diy-content.md) | green | set by the orchestrator |

Every dropped row names the equivalent target text (shared contract scaffolding, duplicated References blocks, and the byte-identical `proposal-frameworks.md`). Target sizes (all ≤ 500): `biz-dev-credentials` 247, `biz-dev-lawful-prospecting-outreach` 112, `biz-dev-positioning` 198, `biz-dev-pricing-menu` 286, `playbook-agency-operations` 447, `training-ai-foundations` 201, `training-client-team` 456. Moved files carry provenance lines; the two emptied training `references/` folders were removed. In `prompt-foundations-and-structure.md` the book locator "Chapter 3" was removed from the Upadhyay (2024) citation under the no-book-numbering rule (the reviewer accepted this; the locator stays in git history).

## Referrers re-pointed (live files)

`AGENTS.md` (training prefix row), `README.md` (counts 117 → 110, 7 rows removed), `.claude-plugin/plugin.json` (regenerated, 110), `.claude-plugin/marketplace.json` (count text), `tests/routing-fixtures.json` (`outreach-collision`), `skills/strategy/strategy-video-content/references/ai-avatar-and-personalised-video.md` (link now to `personalised-video-outreach.md`), `skills/strategy/marketing-foundations-stp-positioning/SKILL.md`, `skills/strategy/strategy-personal-brand/SKILL.md` (description, `Do Not Use When`, Workflow step 1). Targets re-pointed their own mentions (`biz-dev-lawful-prospecting-outreach`: description, `Do Not Use When`, Required Inputs, Workflow step 6, References; `training-ai-foundations`: description, `Do Not Use When`, Workflow step 1, related skills). Left as historical: `projects/2026-05-21-chwezi-facebook-followers-campaign/facebook-follower-ad-plan.md` (a delivered campaign plan that lists `biz-dev-practitioner-positioning` by name) and the pre-consolidation docs listed in the phase file §5.1.

Phase check (`grep -rn "<source>/SKILL.md" skills AGENTS.md README.md docs/quality-gates`, excluding `ALIAS.md`): no output for all 7 sources. Broken/alias/host-absolute link scan over live markdown: 348 files, 0 findings.

## Currentness

- No source moved an overdue register claim; no new register record. Workers applied UG-DPPA-2019, UG-DPPA-S26-DIRECT-MARKETING-2026, KE-ODPC-DIRECT-MARKETING-2026, WHATSAPP-BUSINESS-POLICY, UG-FACEBOOK-ACCESS-2026, UG-MOBILE-SPEED-2026, FTC-ENDORSEMENTS-REVIEWS-2026 and META-SIEP-AD-LIBRARY-2026 (freshness NOT_ASSESSED; UG-DPPA-2019 review due 11 October 2026) and marked rates, fees, platform specifications and response-rate claims "verify before stating (no register record)". The fixed USD conversion in the DIY handbook was replaced with a check-the-rate note.
- Additions beyond the sources, labelled: the fee-at-risk guarantee rule and lawful-basis checks in `risk-reversed-entry-offer.md` (reviewer: consistent with the source's intent and the pricing menu's walk-away rule); the white-label late-payment conflict (1.5 % a week in the source, 1.5 % a month in the target's contracts) is kept and sent to counsel.

## Alias fixtures

All 7 `alias-<source>` fixtures rank 1, as does the re-pointed `outreach-collision`. `mf-collision` now ranks 1 (its competitor `biz-dev-practitioner-positioning` is retired). Four fixtures rank 2, all outside S07 (`blog-positive`, `ai-slop`, `geo-page`, `beginner-training`).

## Gate block (merge runbook, `--min-rank1 91`)

Full output: [gate-block-2026-09-29.txt](gate-block-2026-09-29.txt).

| Check | After S06 | After S07 |
|---|---|---|
| `validate_skill_engine.py --baseline quality-baseline.json` | 117 compliant, 0 failures | **110 compliant, 0 failures** |
| `routing_smoke_test.py --min-rank1 91 --lint-fixtures` | 132/132; p@1 127/132 (96.2 %) | **139/139 top-3 = 1.000; p@1 135/139 (97.1 %)**; lint 0 |
| `check_skill_aliases.py` | routes 75, window open until S07 | **routes 82, findings 0, active 110, cap 120, no window** |
| `pytest -q tests` / `unittest discover` | 49 passed / OK | 49 passed / OK |
| `check_source_freshness.py` | PASS (91) | PASS (91) |
| `source_ingestion_guardrail.py` | 0 findings | 0 findings |
| `git diff --check` | clean | clean |
| `render_host_files.py --check` (engine and workspace) | findings 0 | findings 0 |
| `generate-plugin-manifest.js --check-marketplace` | 23 ok, 0 drift | 23 ok, 0 drift |
| `validate-runtime-skill-budget.py --collisions` | PASS (skills 1095) | PASS, 0 undeclared ≥ 0.75 (skills 1088) |
| `validate-routing-baseline.py` | PASS | PASS |
| `validate-no-book-extractions.py` | roots 12, findings 0 | roots 12, findings 0 |
| `lexical_routing.py --collisions` | exit 0 | exit 0 |

Routing figures are a lexical proxy, not live routing. Model-executed behavioural runs: `NOT_ASSESSED (zero-spend rule)`. The alias prompts echo the new "(formerly …)" `Use When` bullets, which flatters lexical p@1; S08 rewrites descriptions and adds owned-negative fixtures.

## Open items and limitations

- **Dormant window code (reviewer finding 6):** `scripts/check_skill_aliases.py` and `scripts/validate_skill_engine.py` still honour `consolidation_until` if the key were re-added; only the pytest assertion guards against that. Recommended for S08 or S11: remove the window branch from both scripts.
- `training-client-team` SKILL.md is at 456 lines and `playbook-agency-operations` at 447; S09 trims both.
- **Citation backlog (S09/S13):** Sant (2012), Hatton (2007) and Bodnar and Cohen (2012) publishers added at merge, marked verify.
- `docs/engine-tours/social-media-skills.{json,md}` in `chwezi-engine-agents` still state 191; S12 regenerates them.

## Independent review

Reviewer: independent review agent (Claude Opus 5.5, read-only), 29 Sep 2026. **Phase verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`**, no blocking finding. All 7 `ALIAS.md` files are the original text plus the banner; every §5.2 seed heading is mapped; every DROPPED row names existing target text; moved references differ from the originals only by provenance, link fixes and the citation change; all cited register IDs exist; no currentness regression; T-CAP verified. Per source: 4 `ACCEPT` (`biz-dev-practitioner-positioning`, `playbook-white-label-partnerships`, `training-ai-prompt-writing`, `training-diy-content`); 3 `ACCEPT_WITH_DOCUMENTED_LIMITATIONS` (`biz-dev-case-study`, `biz-dev-video-outreach`, `biz-dev-beyond-agency-offer`). All 7 maps are signed.

Findings fixed after review (29 Sep 2026):

| # | Finding | Fix |
|---|---|---|
| 1 | Publishers added at merge without a note (`case-study-method.md`) | Marked "publisher added at merge; verify" |
| 2 | Long scripts read as quotations from Fihn (2025) (`personalised-video-outreach.md` ×2, `risk-reversed-entry-offer.md` ×3, `practitioner-positioning.md`) | Labelled engine house wording / house template |
| 3 | Two merge additions unflagged (finance-engine tax check; agency-as-processor) | Labelled "added at merge" in the reference and recorded in map row 23 |
| 4 | UGX 50,000–100,000 boost budget unqualified | Labelled house starting guidance, not a platform minimum |
| 5 | Evidence folder, log entry and map signatures missing | This file, the gate-block output, the execution-log row; maps signed |

Recorded rather than changed: finding 6 (dormant window code, above) and finding 7 (stage deletions with the new `ALIAS.md` files and moved references so git records renames; for the orchestrator).

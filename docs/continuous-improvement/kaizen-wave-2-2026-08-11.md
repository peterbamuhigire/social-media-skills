# social-media-skills — Kaizen Wave 2 report

Date: 2026-08-11
Repository: `C:\wamp64\www\social-media-skills`
Worker scope: this repository only
Git policy: no commit, push, fetch, pull, reset, publish, or sibling-repository edit

## Result at a glance

Wave 2 challenged the Wave 1 campaign fixture with independent in-memory
mutations. The challenge found three defects in the fixture validator:

- removing evidence returned a generic `FAIL` rather than blocking the evidence
  and report stages;
- changing the approval campaign identity returned a generic `FAIL` rather than
  blocking at approval; and
- removing the report's calendar trace was accepted as `PASS`.

The validator now records stage-level `blocking_reasons`, returns `BLOCKED` for
recognised release-gate defects, propagates an upstream block to the report, and
requires the report to preserve the exact calendar entry IDs and metric lineage.
The fixture remains fictional and read-only. No platform, account, scheduler,
analytics export, customer data, publication, or spend was used.

The Wave 1 exercise-published score remains `55/100`; Wave 2 does not invent a
new raw score because the repository-local Wave 1 report records the post-change
overall raw score as `NOT ASSESSED` rather than retaining a reproducible
per-dimension table. See the [Wave 1 report](kaizen-wave-1-2026-08-11.md) for
the score adapter and permanent repository cap distinction.

## Fresh re-audit and Wave 1 challenge

### Wave 1 gates rerun before the correction

The Wave 1 structural and fixture gates were green before the mutation audit:

| Evidence class | Command | Exit | Result |
| --- | ---: | ---: | --- |
| Structural contract | `python -X utf8 scripts\validate_skill_engine.py --baseline quality-baseline.json` | 0 | 177 skills, 177 compliant, zero failures |
| Current-source register | `python -X utf8 scripts\check_source_freshness.py` | 0 | 17 current records as of 2026-08-11 |
| Structural routing | `python -X utf8 scripts\routing_smoke_test.py` | 0 | 26 fixtures passed; top-three precision 1.000 |
| Source-ingestion safety | `python -X utf8 scripts\source_ingestion_guardrail.py` | 0 | zero findings |
| Behaviour fixture | `python -X utf8 scripts\campaign_behaviour.py` | 0 | 2 cases: 1 `PASS`, 1 intended `BLOCKED`, 0 failed |
| Repository tests | `python -X utf8 -m unittest discover -s tests -p "test_*.py"` | 0 | 11 tests passed before Wave 2; 15 after the correction |

The catalogue, route, source-register, and test counts above are command
outputs, not claims about live campaign performance. The corresponding Wave 1
baseline and six-to-eleven test transition are recorded in the
[Wave 1 repository report](kaizen-wave-1-2026-08-11.md).

### Adversarial challenge

The original positive case was copied in memory and mutated one gate at a time;
the source JSON was not weakened. Each mutated case set its expected outcome to
`BLOCKED` so that the test checked the intended degraded state rather than
silently accepting the original `PASS` expectation.

| Mutation | Wave 1 observed result | Wave 2 required result | Wave 2 evidence |
| --- | --- | --- | --- |
| Clear `evidence.source_records` and `evidence.metrics` | Generic `FAIL`; report remained `pass` in the fresh pre-correction probe | `BLOCKED` at `evidence`, then `report`; reason `missing-evidence` | `test_missing_evidence_blocks_at_evidence_gate` |
| Change `approval.campaign_id` | Generic `FAIL`; approval stage remained `pass` in the fresh pre-correction probe | `BLOCKED` at `approval`, then `report`; reason `approval-campaign-mismatch` | `test_approval_campaign_mismatch_blocks_at_approval_gate` |
| Remove one report `calendar_entry_ids` value | `PASS` because no report/calendar relationship was checked | `BLOCKED` at `report`; reason `report-calendar-inconsistency` | `test_report_calendar_mismatch_blocks_at_report_gate` |
| Replace the brief with `None` | Not covered by the Wave 1 fixture tests | `BLOCKED` without an exception; reason includes `missing-stage` | `test_malformed_brief_does_not_crash_and_is_blocked` |

The first two Wave 1 observations are retained as fresh audit evidence from the
pre-correction mutation probe. The third is a direct negative control against
the old acceptance surface: the old evaluator did not read a report calendar
trace. This table is a comparison of local validator behaviour, not a platform
integration result (synthesis).

## Exact Wave 2 files

Wave 2 changed only these repository-local files:

- [`scripts/campaign_behaviour.py`](../../scripts/campaign_behaviour.py)
- [`tests/fixtures/campaign-behaviour.json`](../../tests/fixtures/campaign-behaviour.json)
- [`tests/test_campaign_behaviour.py`](../../tests/test_campaign_behaviour.py)
- [`docs/continuous-improvement/kaizen-wave-2-2026-08-11.md`](kaizen-wave-2-2026-08-11.md)

No Wave 1 controller, route-repair, or previously changed skill file was
rewritten. The Wave 1 files remain uncommitted user work and were preserved.

## Improvement actions

### W2-CAMPAIGN-01 — missing evidence must block the release path

- Gap: behavioural evidence did not prove that an empty evidence record stops a
  campaign handoff. In the fresh pre-correction mutation, the evidence stage was
  marked `blocked` but the case verdict was `FAIL`, and the complete report was
  not forced into a blocked state.
- Root cause: the runner recorded some local validation messages but had no
  distinction between a recognised release-gate block and malformed fixture
  failure. Downstream report state was checked only against approval status.
- Change: [`scripts/campaign_behaviour.py`](../../scripts/campaign_behaviour.py)
  adds the `missing-evidence` blocking reason, and the fixture test mutates both
  source records and metric rows to exercise the missing-evidence gate. The
  report is required to remain blocked when an upstream evidence gate is
  blocked.
- Hypothesis: a named evidence block will prevent a complete report from being
  mistaken for an accepted handoff when source records or metric rows are
  absent.
- Owner: social-media-skills repository maintainer.
- Measure: the mutation returns `BLOCKED`, stage results identify `evidence` and
  `report` as blocked, and the reason list contains only the intended
  `missing-evidence` gate for this mutation.
- Risk: downstream consumers that treated `FAIL` as the only stop signal may
  need to read the explicit verdict and reason fields. The fixture remains
  local, so it does not prove a host adapter interprets them.
- Rollback: revert only the W2 changes in the evaluator, fixture, and focused
  tests; retain the Wave 1 fixture and restore the prior test expectation only
  through a reviewed replacement that preserves a missing-evidence negative
  control.
- Acceptance evidence: `test_missing_evidence_blocks_at_evidence_gate` passes;
  the campaign runner still exits 0 with 1 `PASS`, 1 intended `BLOCKED`, and 0
  failed fixture cases.
- Standardisation: future campaign cases must label missing source, metric, or
  approval evidence as a stage block and keep the downstream report blocked;
  `blocking_reasons` is the machine-readable reason surface.
- Re-audit: 2026-08-25.

### W2-CAMPAIGN-02 — approval identity mismatch must block approval

- Gap: changing the approval campaign ID produced a generic failure but did not
  mark the approval stage or the report as blocked.
- Root cause: approval identity was appended to an undifferentiated issue list;
  the runner did not model approval identity as a release-gate dependency.
- Change: [`scripts/campaign_behaviour.py`](../../scripts/campaign_behaviour.py)
  maps an approval campaign mismatch to `approval-campaign-mismatch` and
  propagates the block to a report that still says `complete`.
- Hypothesis: an approval record from another campaign cannot be treated as
  evidence for the current calendar when the campaign identity is compared at
  the approval boundary.
- Owner: social-media-skills repository maintainer.
- Measure: the mutated case returns `BLOCKED`, the approval and report stages
  are blocked, and the reason is `approval-campaign-mismatch`.
- Risk: identity checks can expose previously tolerated private fixture shapes;
  no live campaign adapter is authorised or exercised by this repository test.
- Rollback: revert the reason mapping and focused test only after a replacement
  validator retains an approval-identity negative control.
- Acceptance evidence: `test_approval_campaign_mismatch_blocks_at_approval_gate`
  passes in the focused and full suites.
- Standardisation: approval fixtures must carry the same `campaign_id` as the
  brief, and a mismatch is a block rather than a publishable failure recovery.
- Re-audit: 2026-08-25.

### W2-CAMPAIGN-03 — report must reconcile the calendar

- Gap: the report had evidence IDs and metric rows but no required relationship
  to the calendar entries. Deleting one calendar reference from the report was
  therefore accepted as `PASS`.
- Root cause: Wave 1 checked brief/calendar/approval continuity and evidence
  lineage but omitted a report-level calendar reconciliation field.
- Change: [`tests/fixtures/campaign-behaviour.json`](../../tests/fixtures/campaign-behaviour.json)
  now carries `calendar_entry_ids` in both cases. The evaluator requires an
  exact ordered match with the calendar entry IDs and validates approved report
  metric rows against evidence metric names and source IDs. The focused test
  mutates the report calendar trace.
- Hypothesis: a report cannot be treated as complete when it does not identify
  exactly which scheduled entries its decision covers.
- Owner: social-media-skills repository maintainer.
- Measure: a missing report entry ID returns `BLOCKED` at `report` with
  `report-calendar-inconsistency`; the complete and approval-blocked base cases
  retain their intended verdicts.
- Risk: calendar reordering becomes observable because the contract preserves
  ordered IDs. That is deliberate for this fixture, but a future adapter must
  either preserve the order or define a documented canonical sort.
- Rollback: revert the new fixture field and report check together only if the
  replacement contract retains a report-to-calendar reconciliation test.
- Acceptance evidence: `test_report_calendar_mismatch_blocks_at_report_gate`,
  the campaign runner, and the full unittest suite pass.
- Standardisation: campaign reports must include exact calendar entry IDs and
  source-linked metric rows; unresolved mismatches remain `BLOCKED` and never
  become a production or publishing pass.
- Re-audit: 2026-08-25.

### W2-ROUTES-LINKS — fresh re-audit of Wave 1 repairs

- Gap: Wave 1 repaired 14 recorded local Markdown-link misses and removed
  absent `deck-*` route declarations. Wave 2 needed an independent check that
  the repair did not regress while the fixture changed.
- Root cause: route and link declarations are repeated across controllers,
  skill bodies, and historical notes; the risk is drift after the repair.
- Change: no new route or link edit was needed. The existing route/link tests
  and an independent read-only Markdown scan were rerun.
- Hypothesis: the Wave 1 repair remains discoverable and filesystem-backed after
  the Wave 2 test changes.
- Owner: social-media-skills repository maintainer.
- Measure: `routing_smoke_test.py` returned 26/26; the independent link scan
  returned `TOTAL_MISSES=0`; the active-route test passed.
- Risk: route precision and local link resolution remain structural evidence;
  they do not prove that a host selects the best skill for every natural-language
  prompt.
- Rollback: no rollback applies because this action made no route or link edit.
- Acceptance evidence: `test_active_routes_do_not_advertise_absent_deck_taxonomy`,
  `test_all_repository_markdown_links_resolve_or_are_external`, and the
  independent scan all passed.
- Standardisation: keep route and link checks in the normal suite; classify
  illustrative external or site-relative examples instead of presenting them
  as repository-local targets.
- Re-audit: 2026-08-25.

### W2-LONG-SKILLS — measure before any progressive disclosure

- Gap: 31 active `SKILL.md` files remain at or above the repository's 400-line
  review threshold. This is a retrieval-risk signal, not proof that every file
  needs splitting.
- Root cause: the catalogue contains long contracts with no deterministic local
  measure that connects line count to a routing or retrieval failure.
- Change: no long skill was split. The filesystem measurement was rerun after
  Wave 2. `meta-testing-framework` remains a high-risk review candidate at 459
  lines and 24,913 UTF-8 bytes, but no progressive-disclosure edit was justified
  by the available evidence.
- Hypothesis: measuring a stable burden signal before editing avoids a
  catalogue-wide split that adds reference hops without improving use.
- Owner: social-media-skills repository maintainer.
- Measure: the deterministic measure returned `long_skill_count=31`; the full
  list and byte counts are retained in the audit command output. No routing
  fixture or quality gate failed because of one named long skill.
- Risk: a genuinely hard-to-retrieve long skill may remain unchanged. The next
  review should add a deterministic retrieval or section-load measure before
  selecting one file.
- Rollback: no file rollback applies because no progressive-disclosure change
  was made.
- Acceptance evidence: the 31-file measure, 177/177 contract gate, 26/26 route
  gate, and 15-test suite pass with no catalogue split.
- Standardisation: do not split by line count alone. Select at most one file
  only when a deterministic retrieval, routing, or reference-hop measure shows
  a real burden and the split can retain the root contract.
- Re-audit: 2026-11-11, or earlier if a named retrieval failure is reproduced.

## Before / Wave 1 / Wave 2 measures

| Measure | Before Wave 1 | Wave 1 | Wave 2 |
| --- | --- | --- | --- |
| Active skill contracts | 177 active skills recorded in the portfolio assessment | 177/177 compliant | 177/177 compliant; no skill changed in Wave 2 |
| Routing fixtures | 26 fixtures recorded in the Wave 1 baseline | 26/26 passed | 26/26 passed |
| Local Markdown links | 14 misses recorded in the Wave 1 baseline | 0 after repair | 0 in independent scan and suite |
| Campaign fixture | No executable campaign behaviour fixture | 2 cases: 1 `PASS`, 1 intended `BLOCKED` | Same 2 base cases plus 4 deterministic mutation tests |
| Campaign release gates | Missing evidence, approval mismatch, and report/calendar mutation not all covered | Missing approval blocked; other mutations unproven | Missing evidence, approval mismatch, report/calendar mismatch, and malformed brief block for named reasons |
| Long skills | 31 at or above 400 lines recorded in Wave 1 | 31 | 31; no speculative split |
| Exercise-published score | 55/100 adapter | 55/100; post-change raw score `NOT ASSESSED` | 55/100 retained; no unsupported re-score |

The Wave 1 counts in this table are local report values. Wave 2 command counts
are shown in the validation record below; the campaign mutation count is the
number of focused test methods in `tests/test_campaign_behaviour.py` and is not
an outcome count.

## Validation record and expected negative exits

All commands ran from the assigned repository root.

| Command | Exit | Evidence |
| --- | ---: | --- |
| `python -X utf8 scripts\validate_skill_engine.py --baseline quality-baseline.json` | 0 | 177/177 compliant, zero failures |
| `python -X utf8 scripts\check_source_freshness.py` | 0 | 17 current records as of 2026-08-11 |
| `python -X utf8 scripts\routing_smoke_test.py` | 0 | 26/26 routing fixtures passed; top-three precision 1.000 |
| `python -X utf8 scripts\source_ingestion_guardrail.py` | 0 | zero findings |
| `python -X utf8 scripts\campaign_behaviour.py` | 0 | 2 cases: 1 pass, 1 intended blocked, 0 failed |
| `python -X utf8 -m unittest discover -s tests -p "test_*.py"` | 0 | 15 tests passed |
| `python -X utf8 -m unittest tests.test_campaign_behaviour tests.test_engine_quality -v` | 0 | 15 focused quality/campaign tests passed |
| Independent Markdown-link scan | 0 | `TOTAL_MISSES=0` |
| Deterministic long-skill measure | 0 | `long_skill_count=31` |
| `python -X utf8 scripts\check_source_freshness.py --as-of 2026-08-13` | 1 (expected) | Existing negative control reports five overdue records; this is not a release pass |
| `git diff --check` | 0 | No whitespace errors; line-ending warnings are working-copy normalisation notices |

The expected non-zero freshness command is retained as evidence that the
overdue-source gate still fails when evaluated after the registered review date.
The normal release-date freshness command remains the pass gate. No test was
skipped, weakened, deleted, or changed to manufacture a pass.

## Evidence classes

| Evidence class | Wave 2 state | Boundary |
| --- | --- | --- |
| Structural | `PASS`: 177 contracts, 26 route fixtures, source guardrail, active-route test, link scan | Proves declared shape and local consistency only |
| Behavioural | `PASS` for the complete fictional case; intended `BLOCKED` for missing approval; four mutation tests block at named stages | Proves the pure fixture evaluator's state rules, not a live platform |
| Render | `NOT ASSESSED` | No PPTX, DOCX, PDF, image, audio, or rendered creative was generated or inspected |
| System/integration | `NOT ASSESSED` | No native hook host, command adapter, scheduler, analytics export, CRM, or platform API was exercised |
| Production/live publishing | `NOT ASSESSED` and not authorised | No account mutation, publication, paid spend, customer-data processing, or external message was attempted |
| Current-source freshness | `PASS` for the 17-record local register at the release date; the future-date negative control exits 1 | Freshness does not prove semantic support for every campaign claim |

## Safety and anti-slop findings

### Safety audit

Safety scope was the three Wave 2 implementation surfaces: the campaign
validator, the campaign fixture, and its focused tests. Static review found no
remote installer, shell download, package-install instruction, credential or
secret request, exfiltration path, privileged action, or hidden network call.
The changed Python uses the standard library only and reads local JSON. The
targeted safety-pattern scan returned no matches and exit 0. The fixture keeps
the explicit fictional label and `publish_authority: false` boundary.

Safety status: **Safe for the changed local surfaces**, with live adapter and
host-execution behaviour remaining `NOT ASSESSED`.

### Anti-slop review

The Wave 2 report and fixture use named files, test IDs, exact verdicts, and
qualified evidence boundaries. No client name, organisation, URL, platform
result, benchmark, statistic, or quote was invented. Numeric results are tied to
the command or repository file at the point they appear. The report states the
unexecuted render, system, and production checks instead of turning declarations
into proof. No generated social copy or client-facing campaign asset was
produced, so the repository's creative ship gate was not converted into a
fictional content pass.

## Portability

- **Claude:** [`CLAUDE.md`](../../CLAUDE.md) remains the thin project entrypoint;
  no vendor-specific campaign logic was added to it.
- **Codex:** [`AGENTS.md`](../../AGENTS.md) remains the model-neutral project
  guide; the evaluator and JSON fixture use ordinary Python and repository
  paths.
- **Generic agents:** a runner with local file access can load the relevant
  `SKILL.md`, execute `python -X utf8 scripts\campaign_behaviour.py`, and run
  the standard unittest command. No vendor command or model name is required by
  the canonical fixture contract.
- Automatic discovery behaviour for every present or future agent remains
  `NOT ASSESSED`; this Wave 2 change does not claim a host integration.

## Residual risks and backlog

### P0

No new P0 defect was found in the assigned repository during Wave 2. The
campaign fixture now blocks the three challenged integrity failures for named
reasons. This does not close live publishing or host-execution risk.

### P1

- Native hook and thin-command declarations still have no host observation;
  `preflight`, `before_write`, `after_write`, `release`, and `stop` remain
  `NOT ASSESSED`.
- Live platform API behaviour, publication, scheduling, analytics ingestion,
  and campaign performance remain `NOT ASSESSED`.
- Semantic truth of source records and metric values remains `NOT ASSESSED` by
  the pure fixture evaluator; source IDs prove linkage, not truth.
- Render and accessibility checks for finished creative remain `NOT ASSESSED`.

### P2

- 31 long skills remain at or above the 400-line review threshold. No split is
  justified by the current deterministic evidence; add a retrieval measure
  before selecting one file.
- The empty `skills/strategy-personal-brand/references` directory remains the
  Wave 1 classification item; no ownership evidence was found in this audit.
- Source-register freshness passes at the release date but future platform,
  legal, and market changes require the existing review process.

## Re-audit plan

Re-run the structural gates, route/link scan, campaign base cases, and all four
mutation tests on 2026-08-25. Keep platform, render, system, and production
states `NOT ASSESSED` until named evidence exists. Revisit progressive disclosure
on 2026-11-11 only after a deterministic retrieval or reference-hop measure
identifies one high-risk file.

Wave 2 is complete for the bounded repository scope. The engine is not
certified production-ready, publication-ready, or fully mature by this report.

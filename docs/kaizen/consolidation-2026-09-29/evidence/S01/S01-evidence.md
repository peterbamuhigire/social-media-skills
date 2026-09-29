# S01 evidence: governance, alias mechanism, gates and baseline snapshot

- **Date:** 29 September 2026.
- **Executor:** Claude (Opus 5.5) under the Social Kaizen executor brief; the orchestrator commits.
- **Start commit (rollback point):** `38b6c9a`. The worktree was clean at start.
- **Active skills:** 191 → 191. No skill content changed in S01.
- **Authority:** decisions ratified by orchestrator under Peter's delegated authority, 29 Sep 2026 ([decisions.md](../../decisions.md)).

## Tasks

| Task | Status | Files | Evidence |
|---|---|---|---|
| S01-T01 clean worktree, rollback point | DONE | none | `git status --short` empty at start; HEAD `38b6c9a`, recorded in the execution log |
| S01-T02 baseline snapshot | DONE_WITH_LIMITATIONS | `docs/kaizen/consolidation-2026-09-29/baseline-snapshot.json` | SHA-256 (LF-normalised) `5a6457847229ecf7b69bb0242ccfd59fde01bf438738e6fe17341b9d9d36a26e`. Matches 01 §1–2 for count (191), category counts, description classes (59 specific; 105 fully templated = 52 T-generic/UW-T + 1 T-generic + 38 T-playbook + 12 T-platform + 2 T-policy; 27 semi), fixtures (56; 44 skills), p@1 51/56 and 84 files over 300 lines. Limitations below. |
| S01-T03 decision record | DONE | `docs/kaizen/consolidation-2026-09-29/decisions.md` | D-SK-01..07 recorded with authority and date; all ratified (none PENDING), so S02 is not blocked. D-SK-08 records the CI decision. |
| S01-T04 alias registry | DONE | `docs/skill-aliases.yml` | Loads as YAML; `hard_cap: 120`, `target_range: 110-118`, `current_active_skill_count: 191` equals the validator count; `consolidation_until: S07` |
| S01-T05 alias checker | DONE | `scripts/check_skill_aliases.py` | `skill aliases: routes=0 findings=0 active=191 cap=120 window=open-until-S07`, exit 0. Findings: `alias-unrouted`, `alias-stale`, `alias-dangling`, `alias-chain`, `alias-banner-missing`, `cap-exceeded`, `count-mismatch`, plus `alias-active-conflict` and `alias-registry` |
| S01-T06 checker tests | DONE | `tests/test_skill_aliases.py` | 13 tests pass: 1 synthetic positive, the live catalogue, 7 required negatives (one per finding), a banner naming a different target, the in-window cap tolerance, `alias-active-conflict` and a missing registry |
| S01-T07 validator extensions | DONE | `scripts/validate_skill_engine.py`, `tests/test_engine_quality.py` | `alias_link` finding (link to `ALIAS.md` or into a retired folder); cap read from `docs/skill-aliases.yml`, `catalogue_cap_exceeded` fails outside the consolidation window. HEAD: `skills=191 compliant=191 failures=0`. Synthetic negatives in `test_validator_flags_alias_links_and_cap` |
| S01-T08 routing harness | DONE | `scripts/routing_smoke_test.py`, `tests/routing-fixtures.json` | Prints `precision@1=51/56 (91.1%) registered_floor=91.0%`; `--min-rank1 91 --lint-fixtures` exit 0 with 0 lint findings; seeded `--min-rank1 92` exits 1. Without the flag the registered `p1_floor` applies (one source of truth for the floor). Optional fixture field `alias_of` linted against the registry. `p1_floor: 0.91` added |
| S01-T09 count assertion | DONE | `tests/test_engine_quality.py` | Hard-coded 191 removed; `test_active_count_agrees_and_respects_cap` asserts baseline = registry = filesystem, and count ≤ cap unless `consolidation_until` is declared |
| S01-T10 CI step | DONE (decision flagged) | `.github/workflows/skill-engine-quality.yml` | Adds `check_skill_aliases.py` and `routing_smoke_test.py --min-rank1 91 --lint-fixtures`. Runtime-configuration: decided by orchestrator under Peter's delegated authority as the plan's recommended option (D-SK-08). "Workflow green on push" is `NOT_ASSESSED` until the orchestrator pushes |
| S01-T11 runbook and template | DONE | `docs/kaizen/consolidation-2026-09-29/merge-runbook.md`, `preservation-map-template.md` | Roadmap §6/§8 copied and adjusted to the S01 tooling (banner format the checker enforces, `alias_of` fixtures, count updates in registry and baseline) |
| S01-T12 execution log | DONE | `docs/kaizen/consolidation-2026-09-29/execution-log.md` | Change-class matrix, verdict vocabulary, rollback point and the S01 row |
| S01-T13 router note | DONE | `AGENTS.md` ("Retired skill routes" under Routing Rules) | `render_host_files.py --check` findings 0; `CLAUDE.md` unchanged (thin bridge) |

## Cross-engine change (coordination package)

`chwezi-engine-agents/catalog/shared-assets.yaml`: the registered-variant hash for `social-media-skills/scripts/routing_smoke_test.py` was updated to `596d9bfa95ce8a05f99bbc62732c3f739c3d90a64b236a9e29ada1d81fdcd2b6` (reason line extended with S01-T08). Without it the workspace-wide `render_host_files.py --check --workspace-root C:\wamp64\www` reported one `shared-asset-unregistered-variant` finding; after it, findings 0.

## Gate block (roadmap §5, with `--min-rank1 91`)

Full output: [gate-block-2026-09-29.txt](gate-block-2026-09-29.txt). The run covers the combined worktree (S01 plus the S10-T01 legal-currency edits, which change no skill count, route or fixture).

| Check | Result |
|---|---|
| `validate_skill_engine.py --baseline quality-baseline.json` | `skills=191 compliant=191 failures=0`, exit 0 |
| `routing_smoke_test.py --min-rank1 91 --lint-fixtures` | 56/56 top-3 = 1.000; p@1 51/56 = 91.1 %; lint 0; exit 0 |
| `check_skill_aliases.py` | routes 0, findings 0, active 191, cap 120, window open until S07; exit 0 |
| `pytest -q tests` | 49 passed |
| `unittest discover` (CI form) | 49 tests OK |
| `check_source_freshness.py` | PASS (76 records as of 2026-09-29) |
| `source_ingestion_guardrail.py` | findings 0 |
| `git diff --check` | clean (new files checked separately for trailing whitespace) |
| `render_host_files.py --check --engine ..\social-media-skills` | findings 0 |
| `render_host_files.py --check --workspace-root C:\wamp64\www` (brief) | 12 repositories, findings 0 (after the shared-asset hash update) |
| `generate-plugin-manifest.js --check-marketplace` | 23 ok, 0 drift |
| `validate-runtime-skill-budget.py --collisions --ownership evals\routing\ownership.yaml` | PASS; undeclared ≥ 0.75: 0 |
| `validate-routing-baseline.py` | PASS (5 engines + portfolio; social floor lands in S11) |
| `validate-no-book-extractions.py` | roots 12, findings 0 |
| `lexical_routing.py --collisions` (brief) | exit 0, no output: the module is a library; the collision scan it powers is the `validate-runtime-skill-budget.py --collisions` row above |

## Limitations and open items

1. **Line measurement method.** The snapshot counts lines with `splitlines()` (the validator's method): total 55,210, median 287, 27 files over 400, maximum 500. Plan 01 reported 55,401 / 288 / 28 / 501; the difference is exactly one line per file (191), so 01 counted a trailing empty line. Files over 300: 84 in both.
2. **Collision drift since plan time.** Social cross-engine pairs ≥ 0.75 are now 7 (01 recorded 8): `proposal-skills/blog-idea-generator` fell to 0.7496 because another engine changed. All social pairs ≥ 0.75 are declared; within-engine pairs ≥ 0.75: 9 (unchanged).
3. **CI green on push:** `NOT_ASSESSED` until the orchestrator pushes. D-SK-08 is flagged in case the orchestrator wants Peter's direct approval for the workflow edit.
4. **Tier-3 behavioural evidence:** `NOT_ASSESSED (zero-spend rule)`. Routing figures are a lexical proxy.
5. **Check coverage.** The validator's `alias_link` scans active `SKILL.md` files only; links from `references/*.md` to a retired folder are caught only when they break (repository link test). `--lint-fixtures` matches `alias_of` by folder name, so two retired folders with the same name in different categories would be ambiguous (none exist today).
6. **Pre-existing manifest drift.** `node scripts/generate-plugin-manifest.js --engine ..\social-media-skills --check` reports `plugin.json is stale (191 skills on disk)` at HEAD `38b6c9a` too (checked on an archive of HEAD), so S01 did not cause it. S12 regenerates `plugin.json`; the marketplace count check stays green.

## Reviewer verdict

Independent reviewer (read-only code-review agent, 29 Sep 2026), first pass: **REJECT**, on two blocking findings, both fixed and re-verified:

| # | Finding | Resolution |
|---|---|---|
| 1 | Execution log linked to a not-yet-written evidence file, so the repository link test failed | Evidence file written; unittest 49 OK |
| 2 | A merge done as written would break the link test, because `ALIAS.md` keeps verbatim text whose `references/` links move away | Link test skips `ALIAS.md`; the exception is recorded in D-SK-03 and in runbook step 6 |
| 3 | Runbook step 7's `git grep` could never return nothing (historical inventories name every path) | Grep scoped to live files; historical records named as exempt |
| 4 | Runbook missed the plugin manifest and the README and marketplace counts | New step 9: regenerate the manifest (`--engine`, then `--check`) and update the counts |
| 5 | Snapshot line figures differ from plan 01 | Measurement-method note added to the snapshot (see limitation 1) |
| 6 | CI approval is the orchestrator's, not Peter's | Kept as limitation 3 (D-SK-08 flagged) |
| 7 | The 91 % floor was stored in three places | The harness applies `p1_floor` by default |
| 8 | Banner check was a substring test | Boundary-anchored match plus a new negative test |
| 9 | `alias_link` scans active `SKILL.md` only; `alias_of` matches by folder name | Recorded as limitation 5 |

Post-fix status: every blocking finding is resolved, and the gate block is green (re-run below). Executor's proposed verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`. The orchestrator confirms it.

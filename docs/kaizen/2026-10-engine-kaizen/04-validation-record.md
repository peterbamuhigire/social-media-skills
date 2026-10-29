# Validation record — 2026-10-29

Commands were run from the repository root after the kept changes. Baseline outputs remain under `logs/`; final outputs are retained beside them. All routing statistics are lexical-fixture measures, not behavioural routing. Currentness intentionally remains blocked while unresolved records are quarantined.

## Registered release checks

| Command | Exit | Final result | Evidence |
|---|---:|---|---|
| `python -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json` | 0 | 112 skills compliant; 0 failures; median 121 lines. | [`validate-final.txt`](logs/validate-final.txt) |
| `python -X utf8 scripts/routing_smoke_test.py --lint-fixtures` | 0 | 396/396 fixtures pass; top-3 1.000; p@1 377/396 = 95.2%; 123/123 owned negatives; fixture lint 0. | [`routing-final.txt`](logs/routing-final.txt) |
| `python -X utf8 scripts/check_source_freshness.py` | 1 | 10 overdue records remain quarantined and `NOT_ASSESSED`; the gate correctly remains a release blocker. Thirteen other records received scoped content review; quarantine is not a pass. | [`freshness-final.txt`](logs/freshness-final.txt), [currentness review](03-currentness.md) |
| `python -X utf8 scripts/check_skill_aliases.py` | 0 | 83 routes; 0 findings; 112 active skills; cap 120. | [`aliases-final.txt`](logs/aliases-final.txt) |
| `python -X utf8 scripts/check_package_integrity.py` | 0 | Full checkout 1,091 entries; package-oriented tree 915 entries; hard limit 5,000 each; 0 findings. | [`package-final.txt`](logs/package-final.txt) |
| `python -X utf8 -m unittest discover -s tests -p 'test_*.py'` | 0 | 92 tests pass, including local-link, package-boundary, symlink/unreadable-walk, manifest identity/path-set, source quarantine, overlay-index and media-provenance checks. | [`unittest-final.txt`](logs/unittest-final.txt) |

The 5,000-entry ceiling is the user's task requirement. The registered package checker enforces it on both the full checkout, including `.git` and caches, and the package-oriented tree. Its unit tests exercise the 5,000/5,001 boundaries, lower-only test overrides, manifest and skill symlink refusal, incomplete-walk refusal, and plugin name/version/path-set mismatch refusal; see [`test-package-integrity.txt`](logs/test-package-integrity.txt). Current measured counts are below the ceiling.

## Independent acceptance follow-up

Review found that a quarantined source could pass if its review date were still in the future, because the first implementation only reported quarantine inside the overdue branch. The checker now blocks every `quarantined: true` record, validates its boolean flag, NOT_ASSESSED status, reason and quarantine date, and still reports overdue timing. Negative fixtures prove quarantine blocks even within the review window, malformed flags fail closed, and future quarantine dates are refused. Review also added a failure case for a symlinked `.claude-plugin` manifest directory, which could otherwise resolve files outside the checkout. The live register still exits 1 with ten overdue quarantined records; none were refreshed or represented as current. This follow-up preserves the 58.5 raw score and its cap presentations.

The same review corrected a duplicate `6.` in the media-planning workflow numbering and added a sequential-number regression. The final acceptance rerun reports 112 compliant skills, 396/396 routing fixtures (377 first-rank, 123/123 owned negatives), 83 alias routes, 92 passing tests, and package counts of 1,138 checkout / 915 package entries. The package gate passes under the fixed 5,000-entry cap. Final rerun logs are linked above; the source-currentness failure remains an explicit release blocker.

## Re-measured task evidence

- The four-week calendar, channel copy and fictional outage sequence remain in [`00-scope-and-evidence.md`](00-scope-and-evidence.md). These are synthetic, review-only outputs; no account, product or release facts were supplied.
- The media arithmetic is reproducible with `python -X utf8 docs/kaizen/2026-10-engine-kaizen/tasks/media-plan-check.py`. Inputs now carry a value, origin and evidence/assumption source; [`media-plan-check.json`](tasks/media-plan-check.json) preserves those labels. The calculation is not a market forecast, and deduplicated cross-platform reach remains NOT_ASSESSED.
- The provenance negative path is exercised by `python -B -X utf8 -m unittest discover -s tests -p 'test_media_plan_provenance.py' -v`: seven tests pass, including missing/invalid origin, missing source, non-positive/non-finite frequency, invalid-input refusal and sequential workflow numbering. See [`test-media-plan-provenance.txt`](logs/test-media-plan-provenance.txt).
- Routing coverage under the unchanged S13 rule (at least 3 `positive` fixtures plus 2 owned negatives) increased from 4/112 (3.6%) to 7/112 (6.25%). The three task routes now each meet the fixture-count threshold: `11-content-calendar` 3 positives/2 owned negatives; `media-planning` 3/3; `playbook-crisis-communications` 3/2. Reproduce with `python docs/kaizen/consolidation-2026-09-29/evidence/S13/measure_routing.py <engine-root>`; summary: [`routing-coverage-final.json`](logs/routing-coverage-final.json). This does not establish model-selected routing.
- Same-cycle offline native install checks passed for Claude and Codex, and final Codex prompt-input discovery found all 112 expected skill paths, 0 missing, exit 0, network disabled and 0 model calls. See [`native-final-summary.txt`](logs/native-final-summary.txt). This is plugin loading evidence, not behavioural quality, account entitlement or Claude prompt-input discovery.

## NOT_ASSESSED and blockers

- The source freshness gate still exits 1 for 10 quarantined records. Their current legal, platform or market support remains NOT_ASSESSED; do not use them as verified claims.
- Tier 3 model behaviour, live campaign/account forecasts, actual CPM or frequency controls, deduplicated reach, account eligibility, and client product/rights/consent/release facts.
- Rendered accessibility, working assets, full broken-link and machine-specific-link scan, complete dangling cross-engine reference scan, and independent worked-example depth inventory.
- The broader claim-level support audit remains incomplete. See [next-cycle findings](06-next-cycle.md).

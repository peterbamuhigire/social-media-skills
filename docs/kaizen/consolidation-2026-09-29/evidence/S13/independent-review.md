# S13 independent review: close-out re-audit, scoring and record

- **Reviewer:** independent review agent (Claude), read-only. Not involved in executing any Social Kaizen phase. The only file written is this one. No staging, no commit, zero spend.
- **Date:** 29 September 2026.
- **Tree reviewed:** HEAD `e7d68fd` (S12) plus the uncommitted S13 working tree (52 modified files, 15 new files).
- **Read:** the S13 phase file and roadmap §9 (plan folder); the dev `skill-engine-audit` rubric (`references/scoring-rubric.md`, `references/eval-readiness-worked-example.md`); `close-snapshot.json`, `close-snapshot-diff.md`, `scorecard.md`, `kaizen-record.md`, `execution-log.md` (S13 row and close), `decisions.md` (D-SK-10, D-SK-11); every file in `evidence/S13/`; the plan's `02-world-class-benchmark.md` corrections addendum; the chwezi-engine-agents operations record `docs/operations/kaizen-2026-09-29-social-consolidation.md`.

## 1. Commands re-run (engine root)

| Command | Result | Matches the records? |
|---|---|---|
| `python -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json` | skills=112 compliant=112 failures=0 median_lines=121.0 | yes |
| `python -X utf8 scripts/routing_smoke_test.py --min-rank1 92 --lint-fixtures` | 392/392 top-3 1.000; p@1 373/392 (95.2 %), floor 92.0 %; owned negatives 121/121; lint 0 | yes |
| `python -X utf8 scripts/check_skill_aliases.py` | routes=83 findings=0 active=112 cap=120 | yes |
| `python -X utf8 scripts/check_source_freshness.py` | PASS, 179 records within review windows | yes |
| `python -X utf8 scripts/measure_skill_scaffolding.py --max-median 12` | raw 30.9 %, gated 1.4 %, median 121, 0 over 300 | yes |
| `python -X utf8 -B -m pytest -q tests` | before this file existed: 69 passed, 1 failed (`test_all_repository_markdown_links_resolve_or_are_external`: the only broken link was `execution-log.md` → `evidence/S13/independent-review.md`, i.e. this file); re-run after writing it: see §5 | yes, once this file exists |
| `python -X utf8 docs/kaizen/consolidation-2026-09-29/evidence/S13/compute_scorecard.py` | T1 30.00, T2 30.05, T3 0.00, Readiness 60.1; raw 59.2 (hygiene 62.0); measured-constrained 59.1 (hygiene 61.37); published 59.1 | yes |
| `python -X utf8 docs/kaizen/consolidation-2026-09-29/evidence/S13/measure_routing.py .` | 392 fixtures (240 / 142 / 4 / 6); 112 of 112 expected; 121 owned negatives; bands 73 / 47 / 1; T2_cov 6/112 = 0.0536; holdout 48/60, 54/60 | yes (also matches `close-snapshot.json`) |

## 2. Checks against the brief

1. **Numbers.** Every figure in `close-snapshot-diff.md`, `scorecard.md`, `kaizen-record.md` §5–§6, the execution-log S13 row and the operations record matches the re-run output above.
2. **Scorecard against the rubric.** The Readiness formula is `30 × T1 + 40 × mean(T2_p1, T2_neg, T2_cov, T2_clean) + 30 × T3`, as the rubric requires. T3 is stated as `NOT_ASSESSED (zero-spend rule)` = 0 and kept in the formula, and the ceiling of 70 is stated. Three numbers are published and the 65 cap is applied (`min(59.1, 65)`). Every judged score falls in 55–64, inside the 45–65 band, and each names its deficiencies. Hand arithmetic agrees: raw 17.40 + 13.75 + 9.30 + 6.20 + 6.30 + 6.20 = 59.15 → 59.2; measured-constrained hygiene 61.37, overall 59.09 → 59.1. The T2_cov counting rule is broader than the rubric's wording (finding 1), but it does not change the published score.
3. **Roadmap §9.** Every row has a measured value in `close-snapshot-diff.md`. All targets are met. The shared-line row is met on the D-SK-10(a) gated meter, and the raw figure (30.9 %) is shown beside it. Weak measures that are not §9 targets (T2 coverage 5.4 %, holdout p@1 80 %) are shown and carried to the next opportunities.
4. **Verma rewrite.** Sections 1–2 and the packaging paragraph in `ecommerce-differentiation-method.md` are now in the engine's own words:
   - the nine types are a selection table (claim, proof, East African illustration, risk) with a three-question selection rule;
   - the book's US case examples (TOMS, Casper, Rothy's, Stitch Fix and others) are gone, and so are the second-hand percentages;
   - attribution is Verma (2019) *Checkout*.

   Knowledge is preserved: all nine types, the story structure, the capital-and-competition quadrant and the East African illustrations survive, and the preservation map carries a dated addendum. Sections 3, 4 and 6 still carry inline "(Verma, 2019)" attributions, but they are procedural text written for the engine, not a digest. Accepted.
5. **Owned negatives, sample of 8.** Reviewed old against new prompts for `ad-testing-and-scaling-not-stats`, `meta-content-repurposing-not-performance-review`, `hospitality-hotel-restaurant-not-retail-launch`, `04-brand-voice-intake-not-distinct`, `playbook-agency-operations-not-retainer`, `ecommerce-export-marketing-advisory-not-local-shop`, `biz-dev-credentials-not-proposal` and `advertising-attribution-and-measurement-not-mmm`.
   - In all 8, the expected skill is still the genuine owner. The added clause brings in the competitor's vocabulary while a client fact rules the competitor out.
   - No `expected` or `negative_for` value changed, and no positive fixture changed (all 50 edited lines are `collision`).
   - The only p@1 gain is one fixture (372 → 373).
   - Honest, not gamed. The record already states that a lexical ranker cannot read the ruling-out clause (kaizen-record §7 item 2).
6. **Citation corrections, sample of 8.** The sampled corrections are plausible and each is backed by an Open Library row in `citation-backlog.md`. Unconfirmed items carry "verify" or `NOT_ASSESSED`.

   | Correction | Assessment |
   |---|---|
   | Kelley and Sheehan (c. 2021–22) → (2021) | Plausible (5th edn, Routledge) |
   | Upadhyay S. → M. (2024) | Plausible (Malay Upadhyay) |
   | Handley → Handley and Chapman (2012) | Correct for *Content Rules* |
   | Macarthy 2023 → 2022, 6th edn | Plausible |
   | Hanlon and Tuten → *The SAGE Handbook of Social Media Marketing* | Correct |
   | Nelson (2019) → independently published | Plausible |
   | Westergaard and Sheridan titles | Correct |
   | Dietrich (2020) | Marked verify |

   Also checked: Hahn (2003) 3rd edn Wiley is marked verify for the contributor, and Raaz is marked unverified. The UGX/USD "equivalent" error is corrected and labelled a house heuristic.

   `git diff --stat` shows no `SKILL.md` among the changed files, and no description or `Use When` line changed.
7. **Records.**
   - `kaizen-record.md` has scope, baseline, findings, changes, commands and results, before and after, `NOT_ASSESSED`, rollback, and next opportunities N1–N11, each with an owner and a trigger.
   - No host-absolute path (`C:\`, `C:/`) or `file:` link appears in any file changed or added by S13. The only match, "profile:" in `credentials-build-method.md`, is a false positive. Earlier phases' evidence files contain such paths, but they are outside S13's change set.
8. **Language.** British spelling throughout; no AI-slop vocabulary found in the S13 files ("delve" appears only as a quoted item in the citation backlog).

## 3. Findings

| # | Severity | Finding | File | Recommended fix |
|---|---|---|---|---|
| 1 | MINOR | T2_cov counts every fixture whose `expected` is the skill, including `collision` and alias fixtures, as a "positive". The rubric says "at least 3 positive fixtures". Counting only `type: positive` gives 4/112 (0.0357), not 6/112. Readiness then becomes 59.9, not 60.1, and measured-constrained becomes 59.08 → 59.1, so the published score is unchanged. The rule is disclosed in `scorecard-inputs.json`, but the scorecard says "≥ 3 fixtures expecting them" without flagging the difference. | `scorecard.md` §1; `evidence/S13/measure_routing.py` | Add one line to the scorecard stating the counting rule and the strict figure (4/112, Readiness 59.9), or switch to the strict rule. Align with the portfolio `fixture_coverage.py` follow-up. |
| 2 | MINOR | The depth row says "6 citations remain 'verify'". The backlog records 18 marked verify and 6 `NOT_ASSESSED` (as `scorecard.md` §4 and the record say). | `scorecard.md` §2 (depth row) | Change to "18 citations marked 'verify' and 6 `NOT_ASSESSED`". |
| 3 | MINOR | S13-T07 names the engine record `docs/kaizen/kaizen-2026-09-29-social-consolidation.md`. It was written as `docs/kaizen/consolidation-2026-09-29/kaizen-record.md`, and the deviation is not recorded. | `evidence/S13/S13-evidence.md` (T07 row) | Note the path deviation and its reason (records kept together with the evidence). |
| 4 | MINOR | Recomputability gaps: `bench_verify.py` (benchmark re-score) and `try_negs.py` (negative sharpening) stay in the executor's scratchpad, so T04 cannot be recomputed from repo inputs. The T02 preservation audit was run by an executor fork, not by "the reviewer" as the phase file words it. The fork's checks are independent of the maps' own ticks, but the auditor was not independent of execution. | `evidence/S13/benchmark-rescore.md`, `evidence/S13/preservation-audit.md` | Either commit `bench_verify.py` beside the other S13 scripts or list the gap as a limitation. State in the preservation audit that the auditor was an execution fork. |
| 5 | MINOR | The §9 shared-line row is marked "yes" on the D-SK-10(a) gated meter (14.5 % → 1.4 %). Roadmap §9's baseline of 30.5 % was the raw meter, which has not improved (30.9 %). This is disclosed, but the "Met?" cell reads as unqualified. | `close-snapshot-diff.md` (shared-line rows) | Qualify the cell: "yes on the D-SK-10(a) gated meter; the plan-time raw target was superseded by D-SK-10(a)". |
| 6 | MINOR | The new citation text "as cited in the 07 references" is plan-internal shorthand that an engine user cannot follow. | `skills/business-development/biz-dev-credentials/references/credentials-build-method.md` | Replace it with the engine file that cites Bly, R.W. (2018) *The Digital Marketing Handbook*, keeping "verify". |
| 7 | MINOR (observation) | The operations record links to the engine record on GitHub `main`, so the link resolves only after the S13 push (T09). | chwezi-engine-agents `docs/operations/kaizen-2026-09-29-social-consolidation.md` | None needed if T09 goes ahead; otherwise note it. |

No BLOCKING finding.

## 4. Verdict

**ACCEPT_WITH_DOCUMENTED_LIMITATIONS**

The measured close is real and every number reproduces: 112 active skills (cap 120), templating 0, median 121 lines, p@1 95.2 %, 121/121 owned negatives, benchmark 0 GAP, Readiness 60.1, published 59.1 under the 65 cap. The scorecard follows the rubric, and the `NOT_ASSESSED` items (Tier 3, live routing, output quality, THIN evidence gaps, citations) are stated rather than hidden. The seven minor findings are wording, traceability and recomputability issues. None changes a published number. Fix them, or list them as limitations, before the S13 commit.

## 5. Post-write check

The pytest suite is re-run after this file was written. Result: 70 passed, 18 subtests passed (the link test now resolves).

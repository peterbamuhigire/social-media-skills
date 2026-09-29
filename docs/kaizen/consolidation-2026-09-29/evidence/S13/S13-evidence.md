# S13 evidence: close-out re-audit, scoring and record

- **Date:** 29 September 2026. Start: HEAD `e7d68fd` (S01–S12 committed and pushed), clean worktree, 112 active skills.
- **Executor:** S13 executor (Claude Opus 5.5) with four forked workers for independent sub-tasks (citations, preservation audit, owned negatives, benchmark re-score). One writer per file.
- **Authority:** Peter's delegated approval to implement the plan, exercised by the orchestrator (29 Sep 2026). Decisions taken under delegation are marked so.
- **Limits:** zero spend; routing figures are a lexical proxy; Tier 3 is `NOT_ASSESSED (zero-spend rule)`. The session's web-search allowance ran out during S13, so citation checks used the Open Library catalogue only; anything it could not confirm is marked "verify".

## Tasks

| Task | Status | Evidence |
|---|---|---|
| T01 close snapshot and diff | DONE | [close-snapshot.json](../../close-snapshot.json), [close-snapshot-diff.md](../../close-snapshot-diff.md); scripts [measure_close.py](measure_close.py), [measure_routing.py](measure_routing.py); the benchmark verifier [bench_verify.py](bench_verify.py) and the negative-sharpening trial script [try_negs.py](try_negs.py) are stored beside them (run from the engine root). Every roadmap §9 row has a measured value. |
| T02 preservation audit | DONE_WITH_LIMITATIONS | [preservation-audit.md](preservation-audit.md): 39 of 83 maps (all 19 with reads above 0, plus 20 stratified by phase), 1,102 item rows and 3,989 alias lines checked, **0 dropped**. Limit: the phase file asks for the reviewer to run it; it was run by an S13 worker (a fork of the executor that did not write the maps), and the independent reviewer checked its method and sample rather than re-running it. |
| T03 `ALIAS.md` content decision | DONE | D-SK-11 in [decisions.md](../../decisions.md): keep the verbatim historical text until the next Kaizen (plan's recommended option; decided by orchestrator under Peter's delegated authority, 29 Sep 2026). The S11 cosmetic item (retired names inside alias bodies) is closed as not needed under that decision. |
| T04 benchmark re-score | DONE | [benchmark-rescore.md](benchmark-rescore.md): matrix 129 STRONG / 4 THIN / 0 GAP; East Africa 16 / 7 / 0 / 0 DEFECT; every THIN names its `NOT_ASSESSED` gap; all "carried" rows checked against files. No rating changed. |
| T05 scorecard | DONE | [scorecard.md](../../scorecard.md), [scorecard-inputs.json](scorecard-inputs.json), [compute_scorecard.py](compute_scorecard.py): Readiness 59.9 (baseline 40.0); raw 59.2, measured-constrained 59.1, published 59.1. |
| T06 independent review | DONE | [independent-review.md](independent-review.md): `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`, no blocking finding, 7 minor findings (6 fixed, 1 observation); see "Review findings and responses" below |
| T07 records | DONE (documented path deviation) | [kaizen-record.md](../../kaizen-record.md) is at `docs/kaizen/consolidation-2026-09-29/kaizen-record.md`, the path the orchestrator's S13 brief named, beside the scorecard and snapshot, instead of the phase file's `docs/kaizen/kaizen-2026-09-29-social-consolidation.md`; execution log closed; chwezi-engine-agents operations record; plan README "Execution status"; Claude memory updated |
| T08 next opportunities | DONE | kaizen-record §9, each with owner and trigger |
| T09 final push | NOT DONE (external-release) | orchestrator and Peter |

## Carry-forwards from S10–S12

| Item | Status | Evidence |
|---|---|---|
| Verma (2019) "nine intangibles" catalogue close to a digest (S10 review finding 1) | DONE | `brand-strategy-and-distinctive-assets/references/ecommerce-differentiation-method.md` Sections 1–2 rewritten as an engine-voice selection table (claim, proof, East African illustration, risk) and a three-question selection rule; the book's company case examples removed; second-hand survey percentages removed from Sections 1 and 5 and from `ecommerce-differentiation.md`; citation now Author (Year) *Title* with "verify" on initial, subtitle and publisher. Addendum on the [preservation map](../../preservation/ecommerce-brand-differentiation.md). |
| Benchmark text corrections (WhatsApp window up to 7 days via click-to-WhatsApp ads; 1 Oct 2026 service-reply pricing; CIPR "ramp-up"; clean-room source) | DONE | The engine text was already correct (`platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md`, `playbook-crisis-communications/references/crisis-response-procedures.md`, register `IAB-TECHLAB-CLEAN-ROOM`). The plan package's `02-world-class-benchmark.md` (rows SL13-C2, SL21-C6, the WhatsApp economics row, gap 7, source S13, plus a dated corrections addendum) and `00-README.md` gap 7 were corrected. The plan package is outside the repository. |
| Citation and edition backlog (S03–S10) | DONE_WITH_LIMITATIONS | [citation-backlog.md](citation-backlog.md): 21 rows corrected, 18 marked "verify" or "verify at use", 14 already correct, 6 `NOT_ASSESSED`, across 46 reference files. Engine-name drift: `peterbamuhigire/digital-research-skills` still exists on GitHub and `digital-research-engine` does not, so the links stay. Internal-contradiction items are listed there (§4) as next opportunities. |
| 51 owned negatives with the competitor below rank 10 | DONE | [owned-negatives.md](owned-negatives.md), [owned-negative-ranks.txt](owned-negative-ranks.txt): 50 sharpened with "already agreed / settled" framing; bands 36 / 34 / 51 → **73 / 47 / 1**; 121/121 pass; p@1 372 → 373 of 392; holdout unchanged (48/60, 54/60). One left unchanged (`kaizen-improvement-system-not-single-draft`): no honest wording kept `anti-ai-slop` in the top 3 without changing routing text. |
| `ALIAS.md` retired-name cosmetics | NOT NEEDED | Closed by D-SK-11 (verbatim history kept); no check fails on them. |
| Companion register pairs | ALREADY DONE | Folded in S11. |

## Gate block

[gate-block-2026-09-29.txt](gate-block-2026-09-29.txt), run after all S13 edits: validator 112/112, 0 failures, median 121; routing 392/392 top-3, p@1 373/392 (95.2 %) with `--min-rank1 92`, owned negatives 121/121, lint 0; aliases routes=83 findings=0 active=112 cap=120; freshness PASS (179); ingestion guardrail 0; scaffolding gated median 1.4 % (`--max-median 12` passes); pytest 70 passed + 18 subtests; unittest 70 OK; `git diff --check` clean. Coordination package: render check 0 findings (1 and 12 repositories); union collisions PASS, 0 undeclared ≥ 0.75; `lexical_routing.py --collisions` exit 0; routing ratchet PASS; book-extraction check 0 findings; marketplace 23 ok, 0 drift.

## Open items for the orchestrator

- The chwezi-engine-agents `evals/routing/baseline.json` social block still records p@1 94.9 % from S11; the measured value is now 95.2 %. The floor (92) is unchanged and the ratchet passes. Raising the floor is left to the next routing pass (next opportunity N3).
- The final push (T09) and any tag are external-release.

## Review findings and responses

| # | Finding (independent review) | Response |
|---|---|---|
| 1 | T2_cov counted collision fixtures as positives (6 / 112) | Fixed: positives are now `positive`-type fixtures only, giving 4 / 112 (0.0357); Readiness 60.1 → **59.9**; the published 59.1 is unchanged. `measure_routing.py`, `scorecard-inputs.json`, the scorecard, snapshot, diff, record, execution log, portfolio record, plan README and memory updated. |
| 2 | Scorecard depth row miscounted citations | Fixed: 18 "verify" / "verify at use" and 6 `NOT_ASSESSED`. |
| 3 | Kaizen record path differs from the phase file, unrecorded | Recorded as a documented deviation in the T07 row above. |
| 4 | Benchmark and negative-trial scripts not in the repository; preservation audit run by a worker, not the reviewer | Scripts stored in this folder with host paths removed (`bench_verify.py` re-run: 156 rows, 0 missing files). The audit's authorship is recorded as a limitation in the T02 row. |
| 5 | Shared-line target shown as met without qualification | Qualified in the diff and the record: met on the D-SK-10(a) gated measure; raw is 30.9 %. |
| 6 | "as cited in the 07 references" shorthand in `credentials-build-method.md` | Fixed: names `07-email-marketing-strategy`. |
| 7 | Portfolio record links to GitHub `main` (resolves after the push) | Observation accepted: portable-links rule requires GitHub URLs; they resolve once S13-T09 is pushed. |

# S09 evidence: boilerplate reduction with the lean skill template

- **Phase:** Social Kaizen 2026-09-29, S09 (plan `04-phases/S09-boilerplate-reduction-lean-template.md`).
- **Date:** 29 September 2026.
- **Start commit:** `0e0af8a` (S08 plus the portfolio rename commit); worktree clean at start.
- **Active skills:** 110 → 110.
- **Change classes:** doctrine (lean template, authoring standard, 300-line rule; D-SK-06 ratified by orchestrator under Peter's delegated authority); workflow-routing (validator `line_budget` finding); metadata (evidence, meter, shared-asset hashes, citations).
- **Limits:** routing figures are a lexical proxy, not live routing. Model-executed behavioural runs are `NOT_ASSESSED (zero-spend rule)`.

## Headline results

| Measure | Before (`0e0af8a`) | After S09 | Target |
|---|---|---|---|
| Median `SKILL.md` lines | 278 | **120** | ≤ 200 |
| Files over 300 lines | 50 | **0** | 0 (`line_budget` enforced) |
| Longest `SKILL.md` | 500 (`language-standards`) | 162 (`anti-ai-slop`) | ≤ 300 |
| Total `SKILL.md` lines | 31,232 | 13,419 | — |
| Shared-line ratio, gated median | 12.8 % | **1.4 %** (max 3.6 %) | ≤ 12 % |
| Shared-line ratio, raw median (every line) | 28.1 % | 31.2 % | reported only (see D-SK-10a) |
| Validator | 110 compliant, 0 failures | 110 compliant, 0 failures | 0 |
| Routing (359 fixtures) | top-3 100 %, p@1 93.9 % | top-3 100 %, p@1 93.9 %, owned negatives 110/110 | top-3 100 %; p@1 ≥ 92 |
| Frontmatter, `Use When`, `Do Not Use When` changed | — | 0 of 110 | 0 |

Per-skill figures: [lines.csv](lines.csv). Meter output: [scaffolding.json](scaffolding.json) (after) and [scaffolding-before-0e0af8a.json](scaffolding-before-0e0af8a.json).

The raw median rises because the ~30 structural lines the validator requires (frontmatter keys, markers, twelve headings, table header and separator rows) are a larger share of a shorter file. The raw method reproduces the plan's 30.5 % on the S01 commit `008896a` (191 skills) and gives 28.1 % on `0e0af8a`; the plan's "29–30.5 %" is therefore reproduced at S01 and slightly lower after S08 rewrote the routing text. Excluding only the two canonical sentences, as the plan's wording says, the after-figure is 31.5 %, which no 120–220-line skill can bring under 12 %. The gated figure (D-SK-10a) excludes the validator-required structural lines as well, and is the one the budget applies to; it fell from 12.8 % to 1.4 %, which is the measure of repeated prose actually removed. **D-SK-10a needs Peter's ratification, or roadmap §7 reworded to "gated median"** (reviewer finding 5).

## Task status

| Task | Status | Evidence |
|---|---|---|
| S09-T01 lean template and standard | DONE | `docs/templates/SKILL.template.md` rewritten to roadmap §7 (placeholders written without link syntax so the repository link test passes); `docs/standards/skill-authoring-standard.md` gains the budgets table and the canonical-sentence allow-list. The template was tested against the validator: `tests/test_lean_template.py::test_lean_skill_passes_every_contract`. The 500-line rule becomes 300 in `AGENTS.md`, `CONTRIBUTING.md`, `rules/common/core.md` and the merge runbook. D-SK-06 was already ratified by orchestrator under Peter's delegated authority. |
| S09-T02 shared-line meter | DONE | `scripts/measure_skill_scaffolding.py` (`--json`, `--max-median`, `--root`) + tests. Reproduces 30.5 % raw on `008896a` and 28.1 % on `0e0af8a`. |
| S09-T03..T10 apply the template | DONE (as 16 parallel batches plus a pilot, not 8 sequential batch commits) | 110 of 110 skills. Preservation logs: [preservation/](preservation/) B00–B16, one row per non-scaffolding HEAD block, with the factcheck, linecheck and validator result per skill. 107 new reference files; 61 existing reference files edited (pointer re-links, appended location notes, citation fixes). |
| S09-T11 `line_budget` finding and median | DONE | `scripts/validate_skill_engine.py`: `LINE_BUDGET = 300`, finding `line_budget` replaces the July 2026 `line_limit` (> 500); JSON reports `line_budget` and `median_skill_lines`; summary line prints `median_lines`. Tests: boundary 300/301 and the live budgets. |
| S09-T12 routing re-run | DONE | Unchanged: 359/359 top-3, 337/359 p@1 (93.9 %), owned negatives 110/110. Routing text was frozen, so no `Use When` tuning was needed. |
| Hand-off: S06/S07 trims | DONE | `playbook-social-selling` 494 → 130, `training-client-team` 459 → 113, `playbook-agency-operations` 451 → 119; all moved text is in named references. |
| Hand-off: citation conflicts | DONE | [citation-verification.md](citation-verification.md). Ching, V. and Mothi, D. everywhere; *Co-Intelligence* re-attributed to Mollick (2024, Portfolio); Farri and Rosani's HBR guide verified; the unfound Farri/Rosani and Nayebi H./M. titles and Ltifi's *AI and Social Media Marketing* marked verify; all live "Chaffey (2024)" citations become Chaffey and Ellis-Chadwick (2022), 8th edn, Pearson; Ltifi (ed.) *Advances…* cited as 2024 (first publication, Crossref; ©2025 recorded). `ALIAS.md` files, client folders and historical records are not edited. |
| Hand-off: competing email cadence | DONE | `07-email-marketing-strategy` Decision Rules: weeks 1–12 two a week (Bly, 2018); steady-state B2C 1–2 a month, B2B at most 2 a month (`owned-media-assets.md`), rising towards the list-size ceiling (weekly under 500 subscribers, `email-funnel-build-sequence.md`) only when opens hold above 25 % and capacity exists. All three figures kept. |
| Hand-off: other competing figures (S04/S05) | DONE (scoped, none deleted) | RAG 15 % report vs 10 % dashboard (`meta-reporting` row); NSS band sets by report type (`meta-social-listening` row); MQL 50 starter vs 60/40 full model (`meta-sales-marketing-alignment` row); CLV vs TLV (`meta-budget-planner` row); GBP photo floors 8/9/10 (`platform-google-business-profile` row); WhatsApp segment line, broadcast ceiling, pricing and thumbnail (`platform-whatsapp` row, thumbnail to verify against official help). Posting-frequency tables stay scoped by the existing `meta-algorithm-guide` row (EA baseline only under 90 days of data). |
| Hand-off: S03 backlog | DONE | `content-ideas`: the missing `headline-mastery.md` pointer now links to `ad-copy-and-hook-lab/references/headline-and-hook-families.md` (SKILL.md and `ideation-frameworks.md`); "61 categories" marked as a source figure not carried into the engine; `playbook-viral-content-design` has one References section. |
| Stale "SKILL.md §" pointers | DONE | 72 pointers in 36 existing reference files re-linked to where the moved sections now live (a separate pass after the batches). |

## Method

1. **Pilot.** The executor rewrote `11-content-calendar` (278 → 110 lines) as the worked example and wrote the worker spec (lean template, canonical sentences, exact contract headers, move rules, preservation-log format).
2. **Batches.** Sixteen workers, each on a disjoint set of skill folders, rewrote the other 109 skills. `skill-writing`, a hashed pointer stub, was edited by the executor only (line rule and lean-template delta) and its variant hash re-registered.
3. **Nets run per skill:**
   - `routecheck`: frontmatter, `Use When` and `Do Not Use When` byte-identical to HEAD (0 changes across 110);
   - `factcheck`: every year, figure-with-unit, currency amount, register ID, URL, citation and skill id in the HEAD `SKILL.md` still appears in the skill folder. Result: 0 missing, except 12 intentional "Chaffey (2024)" corrections;
   - `linecheck`: every non-scaffolding HEAD line whose content words are poorly covered (< 0.6 recall) by any line of the folder, triaged by the worker as scaffolding, paraphrased (located) or lost (restored). 559 flagged; 414 after template filtering went to the reviewer.
4. **Content rules.** Only generated contract scaffolding was deleted. Domain sections moved to `references/` with a provenance line ("Moved from `SKILL.md` in Social Kaizen S09 …"), mostly word for word. Decision rows, quality checks and anti-patterns stay in `SKILL.md`. Competing figures and doubtful claims were not changed by workers; each batch log lists them under "Noticed, not changed".

## Independent review

Reviewer: independent review agent (Claude Opus 5.5, read-only), 29 Sep 2026. **Phase verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`.** No material loss of domain knowledge; every gate green. The reviewer read 31 skills in full against HEAD (including `language-standards`, `policy-ai-content-ethics`, `anti-ai-slop`, `ai-slop-audit`, `playbook-social-selling`, `playbook-agency-operations`, `training-client-team`, `strategy-personal-brand`, `prompt-engineering-library`, `meta-testing-framework`, `07-email-marketing-strategy`, `platform-whatsapp`, `healthcare`) and triaged all 414 candidate lines: about 305 scaffolding, 65 scaffolding-shaped with the routes still present, 43 content lines all present. Mandatory-gate citations (Merriam-Webster 2025, Kommers et al., Spracklen et al., Veracode) are byte-identical to HEAD.

Findings and disposition:

| # | Severity | Finding | Disposition |
|---|---|---|---|
| 1 | MINOR | Ltifi in-text years in `policy-ai-content-ethics` changed to 2024 but point at the 2025 title | Fixed: five in-text citations restored to 2025 (they cite the unverified 2025 title, now marked verify) |
| 2 | MINOR | `ai-readiness-diagnostic` lost "choose the lowest viable automation level and define its human approval gate" | Fixed: added to its scoring row; the same rule, found earlier by the pointer pass in `ai-use-case-mapping`, is merged into its Q2 row (keeps 8 rows) |
| 3 | MINOR | `ai-generative-search-optimisation` degraded mode narrower | Fixed: native-language and rights review restored as triggers |
| 4 | MINOR | `playbook-viral-content-design` quality bullets softened | Fixed: "all six viral structures" and "all four primary EA platforms" restored |
| 5 | MINOR | Meter method differs from the plan wording | Documented (D-SK-10a); for Peter's ratification |
| 6 | MINOR | README source list lacks verify markers; Ltifi year missing | Fixed |
| 7 | MINOR | Reviewer-style instructions left in `ai-automation-recipes.md` | Fixed: neutral notes pointing to the S13 citation backlog |
| 8 | MINOR | Provenance lines understate citation fixes | Fixed in four files (the fifth, `policy-intake-and-template.md`, no longer carries a corrected citation after finding 1) |
| 9 | MINOR | Stale baseline pointer and "Ellis-Chadwick to confirm" in the GBP location reference | Fixed |
| 10 | MINOR | Three scope rows could be sharper | Fixed (NSS by report type; WhatsApp thumbnail to verify; GBP 8/9/10) |
| 11 | MINOR | Template conformance: 9 decision rows in `ai-use-case-mapping`; `skill-writing` stub exempt; unlinked `kaizen-improvement-system` reference | Fixed (rows merged to 8; portfolio standard linked by GitHub URL); `skill-writing` recorded as an exempt pointer stub |
| 12 | MINOR | `content-ideas` headline pointer only in references | Fixed: added to SKILL.md References |

A test failure the reviewer met mid-review (`deck-outline` in a new reference filename tripped `test_active_routes_do_not_advertise_absent_deck_taxonomy`) was fixed before the gate block by renaming the new file to `audit-method-and-presentation-outline.md`.

## Gate block

[gate-block-2026-09-29.txt](gate-block-2026-09-29.txt): all green. Validator 110/110, 0 failures, median 120; routing 359/359 top-3, p@1 93.9 % (floor 92), owned negatives 110/110; aliases 82 routes, 0 findings, cap 120; pytest 68 passed; unittest OK; freshness PASS; ingestion guardrail 0; scaffolding gated median 1.4 % (≤ 12); `git diff --check` clean. Coordination package: render check 0 findings (12 repositories); marketplace 23 ok, 0 drift; collisions PASS, 0 undeclared ≥ 0.75; routing ratchet PASS; book-extraction check 0 findings.

## Cross-engine changes (`chwezi-engine-agents`)

- `catalog/shared-assets.yaml`: re-registered two social variants with S09 reasons: `skill-writing` `SKILL.md` (sha256 `87fec38a…`) and `rules/common/core.md` (sha256 `3cf47392…`, the 500 → 300 rule).

## Open items and limitations

- **D-SK-10a** (gated shared-line figure) needs Peter's ratification, or the roadmap §7 budget row reworded to "gated median".
- **Skills under 120 lines:** about 40 skills are 111–119 lines. The spec forbade padding; the 120-line floor in roadmap §7 is a target band, not a gate.
- **Appended location notes:** several existing references keep a short "where the SKILL.md sections now live" note added in S09; all links resolve. The pointers themselves were re-linked in place.
- **"Noticed, not changed" backlog for S10/S13:** each batch log lists undated or unsourced figures, internal contradictions (for example response-time targets, NPS timing, completion targets, email KPI benchmarks) and doubtful citations (Stutts publisher, Kim and Mauborgne 2005 vs 2015, Dietrich 2020, Handley and Chapman, Nelson 2018/2019, Kelley and Sheehan, Raaz). None were changed in S09.
- **Citation backlog (S13):** Rageh (Ed.) (2026); Raymond and Johnston (2021) title; Hietaniemi, Walsh Phillips, Sant, Hatton, Johnson, Funk, Gladwell, Kotler et al. publishers; Westergaard title (*Get Scrappy*, 2016, AMACOM, partly verified); Macarthy edition; the in-text "Farri and Rosani, 2025" and "Nayebi, 2025" in `ai-automation-recipes.md` are not yet matched to a verified title.
- **Index hygiene:** two workers briefly used `git add -N` / `git reset -q --` / `git rm --cached` on their own untracked files to run `git diff --check`; the index was left unchanged (nothing staged).
- `docs/engine-tours/social-media-skills.{json,md}` in `chwezi-engine-agents` still state 191; S12 regenerates them.
- Working copies use CRLF under `core.autocrlf=true`; git stores LF.

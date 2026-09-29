# S03 evidence: content, creative and prompt-library merges

- **Date:** 29 September 2026.
- **Executor:** Claude (Opus 5.5) under the Social Kaizen executor brief; the orchestrator commits. One merge worker per target cluster did steps 1–5 of the [merge runbook](../../merge-runbook.md); the coordinator did steps 6–9 and 11.
- **Start state:** HEAD `7c60138` plus the uncommitted S02 changes (S02 is committed separately by the orchestrator, before this phase). Rollback: revert the S03 commit.
- **Active skills:** 176 → **162** (14 MERGE-INTO, including the `content-writing` category file).
- **Authority:** decisions ratified by orchestrator under Peter's delegated authority, 29 Sep 2026 (D-SK-03, D-SK-04, D-SK-07; see [decisions.md](../../decisions.md)).
- **Git:** no commit, stage or `git mv`; plain renames and moves, which `git add -A` records as renames.

## Tasks

| Task | Target | Sources → reference | Status |
|---|---|---|---|
| S03-T01 | `blog-writer` | `content-whitepaper-ebook` → `whitepaper-and-ebook-structure.md` | DONE |
| S03-T02 | `caption-writer` | `hashtag-strategy` → `hashtag-and-keyword-tagging.md` | DONE |
| S03-T03 | `content-ideas` | `blog-idea-generator` → `blog-and-article-topic-briefs.md` (+ moved `content-formats.md`, `idea-sources-and-series.md`, `ideation-frameworks.md`) | DONE |
| S03-T04 | `direct-response-funnel-copy` | `direct-mail-writer` → `direct-mail-letters-and-packs.md` (+ moved `galletti-27-points.md`; checked: a 26-point grouped checklist from several sources, not a single-book digest) | DONE |
| S03-T05 | `meta-content-repurposing` | `ai-content-recycling-pipeline` → `ai-assisted-recycling-pipeline.md`; `meta-evergreen-content-strategy` → `evergreen-register-and-rotation.md` | DONE |
| S03-T06 | `playbook-content-production` | `playbook-ai-content-workflow` → `ai-assisted-production-workflow.md` | DONE |
| S03-T07 | `playbook-viral-content-design` | `playbook-audacious-content` → `bold-idea-risk-screen.md` | DONE |
| S03-T08 | `premium-commercial-writing` | category file `skills/content-writing/SKILL.md` → `content-writing-standards.md`; `copywriting-brochure` → `brochure-copy.md` | DONE (documented deviation below) |
| S03-T09 | `prompt-engineering-library` | `image-prompt-engineer` → `image-prompt-patterns.md`; `prompt-library-image-audio-video` → `image-audio-video-prompt-library.md` | DONE (target 467 lines) |
| S03-T10 | `strategy-video-content` | `ai-avatar-personalised-video` → `ai-avatar-and-personalised-video.md`; `platform-podcast-strategy` → `podcast-and-audio-series.md` | DONE |
| S03-T11 | fixtures | 14 alias-routing fixtures (`alias_of`) | DONE: all 14 rank 1 |
| S03-T12 | count and registry | `quality-baseline.json` and `docs/skill-aliases.yml` = 162 | DONE |
| S03-T-X1 | cross-engine owner | `chwezi-engine-agents/evals/routing/ownership.yaml`: blog-ideation group member and `owner` → `social-media-skills/content-ideas`; `follow_up` kept; reason line records the alias | DONE; collision scan PASS, 0 undeclared ≥ 0.75; one expected `stale-declaration` warning: `social-media-skills/content-ideas <-> website-skills/blog-idea-generator now scores 0.586 < 0.6` (recorded; the row stays until S11) |

## Merges

| Source | Target | Reference | Preservation map (rows; rows containing `DROPPED`) | Gates | Commit |
|---|---|---|---|---|---|
| `content-whitepaper-ebook` | `blog-writer` | `whitepaper-and-ebook-structure.md` | [42; 4](../../preservation/content-whitepaper-ebook.md) | green | set by the orchestrator |
| `hashtag-strategy` | `caption-writer` | `hashtag-and-keyword-tagging.md` | [20; 3](../../preservation/hashtag-strategy.md) | green | set by the orchestrator |
| `blog-idea-generator` | `content-ideas` | `blog-and-article-topic-briefs.md` | [32; 5](../../preservation/blog-idea-generator.md) | green | set by the orchestrator |
| `direct-mail-writer` | `direct-response-funnel-copy` | `direct-mail-letters-and-packs.md` | [20; 2](../../preservation/direct-mail-writer.md) | green | set by the orchestrator |
| `ai-content-recycling-pipeline` | `meta-content-repurposing` | `ai-assisted-recycling-pipeline.md` | [37; 3](../../preservation/ai-content-recycling-pipeline.md) | green | set by the orchestrator |
| `meta-evergreen-content-strategy` | `meta-content-repurposing` | `evergreen-register-and-rotation.md` | [33; 6](../../preservation/meta-evergreen-content-strategy.md) | green | set by the orchestrator |
| `playbook-ai-content-workflow` | `playbook-content-production` | `ai-assisted-production-workflow.md` | [41; 4](../../preservation/playbook-ai-content-workflow.md) | green | set by the orchestrator |
| `playbook-audacious-content` | `playbook-viral-content-design` | `bold-idea-risk-screen.md` | [26; 6](../../preservation/playbook-audacious-content.md) | green | set by the orchestrator |
| category `content-writing` | `premium-commercial-writing` | `content-writing-standards.md` | [41; 3](../../preservation/content-writing-category.md) | green | set by the orchestrator |
| `copywriting-brochure` | `premium-commercial-writing` | `brochure-copy.md` | [16; 3](../../preservation/copywriting-brochure.md) | green | set by the orchestrator |
| `image-prompt-engineer` | `prompt-engineering-library` | `image-prompt-patterns.md` | [23; 3](../../preservation/image-prompt-engineer.md) | green | set by the orchestrator |
| `prompt-library-image-audio-video` | `prompt-engineering-library` | `image-audio-video-prompt-library.md` | [25; 3](../../preservation/prompt-library-image-audio-video.md) | green | set by the orchestrator |
| `ai-avatar-personalised-video` | `strategy-video-content` | `ai-avatar-and-personalised-video.md` | [35; 2](../../preservation/ai-avatar-personalised-video.md) | green | set by the orchestrator |
| `platform-podcast-strategy` | `strategy-video-content` | `podcast-and-audio-series.md` | [35; 2](../../preservation/platform-podcast-strategy.md) | green | set by the orchestrator |

Every dropped row names the equivalent target text (in practice the shared contract scaffolding, the templated decision rows, the generic anti-patterns and the duplicated References bullets). No source cites a source-register ID; the shared ethics filter keeps its AD-09 and PL-01–04 rows in place.

## S03-T08: category file (documented deviation)

- The task row says the shared `skills/content-writing/references/` folder stays in place because many skills link to it; the §5.2 seed says "Reference files to move". The task row was followed. The four shared files (`business-vocabulary.md`, `direct-marketing-ethics-filter.md`, `human-professional-phrase-bank.md`, `reader-empathy-and-voc.md`) stay live and are linked from `content-writing-standards.md`; map rows 38–41 record "STAYS IN PLACE".
- Registry route `skills/content-writing: skills/content-writing/premium-commercial-writing`; banner in `skills/content-writing/ALIAS.md`.
- **Validator change** (`scripts/validate_skill_engine.py`, `retired_dirs`): a folder holding `ALIAS.md` that still contains active `SKILL.md` descendants (the category folder) is not treated as retired, so links to its active child skills and to its shared `references/` stay legal; a link to the `ALIAS.md` file itself is still an `alias_link`, and ordinary retired folders are unaffected. Without it all seven remaining content-writing skills would fail `alias_link`. Test: `tests/test_engine_quality.py::test_validator_flags_alias_links_and_cap` gained the category-alias case (shared reference allowed, category `ALIAS.md` link flagged, ordinary retired folder still flagged).
- `AGENTS.md` updated: the "documented exception" sentence now names the alias and the new standards reference; the Default Context row for `content-writing` now points at `premium-commercial-writing/references/content-writing-standards.md`.

## Referrers re-pointed (live files)

`AGENTS.md` (category exception, Default Context rows for `content-writing` and `blog-idea-generator`, scope list and naming table naming `hashtag-strategy`), `README.md` (counts, 14 rows removed, summary sentence), `.claude-plugin/plugin.json` (regenerated, 162), `.claude-plugin/marketplace.json` (count text), `projects/tech-guy-peter/README.md`, and these skill files: `advertising/direct-response-economics/SKILL.md` (two links), `ai-readiness-diagnostic/references/ai-marketing-canvas-scoring.md` (two links), `ai-use-case-mapping/SKILL.md`, `biz-dev-practitioner-positioning/SKILL.md` (two mentions), `blog-writer/references/writing-craft.md`, `content-ideas/references/content-formats.md` and `ideation-frameworks.md` (moved files naming the old skill), `premium-commercial-writing/SKILL.md`, `meta-tools-stack-evaluation/SKILL.md`, `playbook-marketing-automation/references/ai-automation-recipes.md` (two), `policy-ai-content-ethics/SKILL.md`, `strategy/owned-media-strategy/SKILL.md`.

Phase check over live paths (runbook step 7 list plus `projects/`): no `<source>/SKILL.md` or `<source>/references` path remains for any of the 14 sources outside `ALIAS.md`, provenance lines and "formerly" notes. Historical records keep the old names.

## Routing widening (minimal, S08 finalises)

Each target gained one `Use When` bullet per source in the old job's words, ending "(formerly `<source>`)". Before the bullets, 7 of 14 alias fixtures missed the top 3.

## Alias fixtures

| Fixture id | Expected | Rank |
|---|---|---|
| `alias-content-whitepaper-ebook` | `blog-writer` | 1 |
| `alias-hashtag-strategy` | `caption-writer` | 1 |
| `alias-blog-idea-generator` | `content-ideas` | 1 |
| `alias-direct-mail-writer` | `direct-response-funnel-copy` | 1 |
| `alias-ai-content-recycling-pipeline` | `meta-content-repurposing` | 1 |
| `alias-meta-evergreen-content-strategy` | `meta-content-repurposing` | 1 |
| `alias-playbook-ai-content-workflow` | `playbook-content-production` | 1 |
| `alias-playbook-audacious-content` | `playbook-viral-content-design` | 1 |
| `alias-content-writing` | `premium-commercial-writing` | 1 |
| `alias-copywriting-brochure` | `premium-commercial-writing` | 1 |
| `alias-image-prompt-engineer` | `prompt-engineering-library` | 1 |
| `alias-prompt-library-image-audio-video` | `prompt-engineering-library` | 1 |
| `alias-ai-avatar-personalised-video` | `strategy-video-content` | 1 |
| `alias-platform-podcast-strategy` | `strategy-video-content` | 1 |

No existing fixture had a source as `expected`. Rank changes in existing fixtures: `blog-positive` rose from 3 to 2 (the retired `blog-idea-generator` no longer outranks it); `geo-page` fell from 1 to 2 (`ai-generative-search-optimisation` now edges `seo-geo-optimisation`, an IDF shift from the smaller catalogue; both are outside S03, still top 3; S08 owns description work).

## Gate block (merge runbook, `--min-rank1 91`)

Full output: [gate-block-2026-09-29.txt](gate-block-2026-09-29.txt).

| Check | After S02 | After S03 |
|---|---|---|
| `validate_skill_engine.py --baseline quality-baseline.json` | 176 compliant, 0 failures | **162 compliant, 0 failures** |
| `routing_smoke_test.py --min-rank1 91 --lint-fixtures` | 71/71; p@1 66/71 (93.0 %) | **85/85 top-3 = 1.000; p@1 79/85 (92.9 %)**; lint 0 |
| `check_skill_aliases.py` | routes 15 | **routes 29, findings 0, active 162** |
| `pytest -q tests` / `unittest discover` | 49 passed / OK | 49 passed / OK |
| `check_source_freshness.py` | PASS (76) | PASS (76) |
| `source_ingestion_guardrail.py` | 0 findings | 0 findings |
| `git diff --check` | clean | clean |
| `render_host_files.py --check` (engine and workspace) | findings 0 | findings 0 |
| `generate-plugin-manifest.js --check-marketplace` | 23 ok, 0 drift | 23 ok, 0 drift |
| `validate-runtime-skill-budget.py --collisions` | PASS | PASS, 0 undeclared ≥ 0.75 (skills 1140); 1 `stale-declaration` warning (above) |
| `validate-routing-baseline.py` | PASS | PASS |
| `validate-no-book-extractions.py` | roots 12, findings 0 | roots 12, findings 0 |
| `lexical_routing.py --collisions` | exit 0 | exit 0 |

Routing figures are a lexical proxy, not live routing. Model-executed behavioural runs: `NOT_ASSESSED (zero-spend rule)`.

## Open items and limitations

- **EU AI Act Article 4 versus Article 50:** the image/audio/video prompt library and the AI-avatar reference carry the sources' "Article 4" disclosure claim with a verification note (transparency duties sit in Article 50 of Regulation (EU) 2024/1689). Correction is S10 gap-fill work (benchmark gap 10).
- **Additions beyond the sources**, each marked in the reference or map: verify-before-quoting notes on tool prices and platform limits (Mailchimp, Brevo, Midjourney parameters); "ConvertKit now trades as Kit"; FCDO (formerly DFID); a note that 12 biweekly podcast episodes span about 24 weeks, not 6; the 75 %/40 % personalised-video figures labelled as source-reported; fuller citation details for Ogilvy, Cialdini, Ariely, Schwartz, Gunning and Edwards, Edwards and Douglas.
- **Names without folders:** `sales-copywriting/references/headline-mastery.md` (cited in the moved ideation files, plain text) and `page-builder`, `seo`, `brand-alignment`, `sector-strategies` (category-file integration list) do not exist in this engine; kept as text and flagged.
- `docs/engine-tours/social-media-skills.{json,md}` in `chwezi-engine-agents` still state 191; S12 regenerates them.
- **ALIAS.md text:** five aliases (`content-whitepaper-ebook`, `meta-evergreen-content-strategy`, `playbook-ai-content-workflow`, `playbook-audacious-content`, the `content-writing` category file) carry the S02 re-points of retired skill names, because S02 edited those live files before S03 retired them; their maps say "@ 7c60138 + S02 working-tree re-points". Working copies use CRLF under `core.autocrlf=true`; git stores LF.
- **Validator tightening (after review):** `retired_dirs` exempts a folder only when a direct child directory holds a `SKILL.md`, so a retired skill with a stray nested `SKILL.md` stays retired.
- **Citation backlog (S09/S13):** Chaffey (2024) "8th edition" is probably Chaffey and Ellis-Chadwick (2022); Ching and Mothi initials vary across the engine; the `headline-mastery.md` pointer and "61 categories" in the moved ideation files; a duplicate `## References` heading in `playbook-viral-content-design`.

## Independent review

Reviewer: independent review agent (Claude Opus 5.5, read-only), 29 Sep 2026. **Phase verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`.** No blocking finding and no substantive loss; the reviewer checked at least five specific facts per source, the validator change and the `ownership.yaml` edit. Per source: 6 `ACCEPT` (`hashtag-strategy`, `direct-mail-writer`, `ai-content-recycling-pipeline`, `copywriting-brochure`, `image-prompt-engineer`, `prompt-library-image-audio-video`); 8 `ACCEPT_WITH_DOCUMENTED_LIMITATIONS` (limitations named in each map's reviewer line). All 14 maps are ticked and signed.

Findings fixed after review (29 Sep 2026):

| Finding | Fix |
|---|---|
| Evidence linked a gate-block file not yet written | Written after the final gate run |
| Cialdini (1984) cited with the 1993 revised-edition subtitle in `content-writing-standards.md` | Now "(1993) *Influence: The Psychology of Persuasion* (revised edition; first published 1984 as *Influence: How and Why People Agree to Things*)" |
| One-sentence edits in the moved `content-formats.md` and `ideation-frameworks.md` not recorded | Recorded in blog-idea-generator map rows 29 and 31 |
| Companion skills re-pointed early to their later owners (`biz-dev-video-outreach`, `owned-media-strategy` are still active) | Both old and new companions listed |
| Map source lines said "@ 7c60138" for aliases carrying S02 re-points | Source lines amended |
| "Cowen" expanded to "Tyler Cowen" from memory | Reverted to the source's "Cowen" |
| Ching/Mothi initials inconsistent | Reconcile note added in `ai-assisted-production-workflow.md` |
| Validator exemption could hide a nested `SKILL.md` | Tightened to direct child directories |

# S05 evidence: client pipeline, audience, lifecycle and channel merges

- **Date:** 29 September 2026.
- **Executor:** Claude (Opus 5.5) under the Social Kaizen executor brief; the orchestrator commits. Six merge workers did steps 1–6 of the [merge runbook](../../merge-runbook.md) for thirteen target clusters; the coordinator did steps 7–10 (registry, referrers, fixtures, counts, README, AGENTS, plugin and marketplace, gates, evidence).
- **Start state:** HEAD `8eacccb` plus the uncommitted S04 changes (S04 saved as git tree `cda737c`; the orchestrator commits S04 separately, before this phase). Rollback: revert the S05 commit.
- **Active skills:** 151 → **132** (19 MERGE-INTO).
- **Authority:** decisions ratified by orchestrator under Peter's delegated authority, 29 Sep 2026 (D-SK-03, D-SK-04; see [decisions.md](../../decisions.md)).
- **Git:** no commit or `git mv`; plain renames and moves. The S04 tree was captured with `git add -A && git write-tree` followed by `git reset -q` (index only).

## Tasks

| Task | Target | Sources → reference | Status |
|---|---|---|---|
| S05-T01 | `01-client-brief` | `00-client-intake` → `intake-question-bank.md` | DONE |
| S05-T02 | `02-platform-audit` | `biz-dev-social-media-audit-offer` → `audit-as-lead-offer.md` (+ moved `proposal-frameworks.md`); `playbook-profile-optimisation` → `profile-optimisation-fixes.md` | DONE |
| S05-T03 | `03-audience-personas` | `ai-synthetic-personas` → `synthetic-persona-hypotheses.md`; `strategy-multigenerational-digital` → `generational-segment-lens.md` | DONE |
| S05-T04 | `04-brand-voice-intake` | `playbook-social-media-brand-style-guide` → `social-brand-style-guide.md` | DONE |
| S05-T05 | `07-email-marketing-strategy` | `biz-dev-reactivation-campaign` → `win-back-and-reactivation.md`; `playbook-email-funnel` → `email-funnel-build-sequence.md` (+ moved `launch-sequence-operations.md`); `playbook-lead-magnet-system` → `lead-magnets-and-list-building.md` | DONE |
| S05-T06 | `08-influencer-marketing-strategy` | `ai-influencer-strategy` → `ai-assisted-influencer-discovery-and-virtual-creators.md`; `playbook-ugc-strategy` → `ugc-creator-and-customer-content.md` | DONE |
| S05-T07 | `09-campaign-strategy` | `playbook-social-media-contests` → `contests-promotions-and-gaming-rules.md` | DONE |
| S05-T08 | `12-website-content-plan` | `playbook-question-engine` → `buyer-question-content-plan.md` | DONE |
| S05-T09 | `peso-integrated-strategy` | `owned-media-strategy` → `owned-media-assets.md` | DONE |
| S05-T10 | `platform-google-business-profile` | `playbook-location-based-marketing` → `location-based-and-proximity-marketing.md` | DONE |
| S05-T11 | `platform-instagram` | `platform-instagram-growth` → `growth-diagnosis-and-experiments.md`; `platform-instagram-visual-system` → `grid-and-visual-system.md` | DONE |
| S05-T12 | `platform-linkedin` | `platform-linkedin-company-pages` → `company-pages-showcase-and-events.md` | DONE |
| S05-T13 | `platform-whatsapp` | `playbook-whatsapp-business` → `whatsapp-business-app-operations.md` | DONE |
| S05-T14 | fixtures | 19 alias-routing fixtures; `instagram-growth-collision` re-pointed to `platform-instagram` | DONE: all 19 and the re-pointed fixture rank 1 |
| S05-T15 | count and registry | `quality-baseline.json` and `docs/skill-aliases.yml` = 132; 19 routes added (60 cumulative) | DONE |

## Merges

| Source | Target | Reference | Preservation map (rows; rows containing `DROPPED`) | Gates | Commit |
|---|---|---|---|---|---|
| `00-client-intake` | `01-client-brief` | `intake-question-bank.md` | [19; 3](../../preservation/00-client-intake.md) | green | set by the orchestrator |
| `biz-dev-social-media-audit-offer` | `02-platform-audit` | `audit-as-lead-offer.md`, moved `proposal-frameworks.md` | [29; 2](../../preservation/biz-dev-social-media-audit-offer.md) | green | set by the orchestrator |
| `playbook-profile-optimisation` | `02-platform-audit` | `profile-optimisation-fixes.md` | [29; 2](../../preservation/playbook-profile-optimisation.md) | green | set by the orchestrator |
| `ai-synthetic-personas` | `03-audience-personas` | `synthetic-persona-hypotheses.md` | [23; 2](../../preservation/ai-synthetic-personas.md) | green | set by the orchestrator |
| `strategy-multigenerational-digital` | `03-audience-personas` | `generational-segment-lens.md` | [18; 2](../../preservation/strategy-multigenerational-digital.md) | green | set by the orchestrator |
| `playbook-social-media-brand-style-guide` | `04-brand-voice-intake` | `social-brand-style-guide.md` | [43; 2](../../preservation/playbook-social-media-brand-style-guide.md) | green | set by the orchestrator |
| `biz-dev-reactivation-campaign` | `07-email-marketing-strategy` | `win-back-and-reactivation.md` | [22; 2](../../preservation/biz-dev-reactivation-campaign.md) | green | set by the orchestrator |
| `playbook-email-funnel` | `07-email-marketing-strategy` | `email-funnel-build-sequence.md`, moved `launch-sequence-operations.md` | [18; 2](../../preservation/playbook-email-funnel.md) | green | set by the orchestrator |
| `playbook-lead-magnet-system` | `07-email-marketing-strategy` | `lead-magnets-and-list-building.md` | [15; 2](../../preservation/playbook-lead-magnet-system.md) | green | set by the orchestrator |
| `ai-influencer-strategy` | `08-influencer-marketing-strategy` | `ai-assisted-influencer-discovery-and-virtual-creators.md` | [27; 2](../../preservation/ai-influencer-strategy.md) | green | set by the orchestrator |
| `playbook-ugc-strategy` | `08-influencer-marketing-strategy` | `ugc-creator-and-customer-content.md` | [24; 1](../../preservation/playbook-ugc-strategy.md) | green | set by the orchestrator |
| `playbook-social-media-contests` | `09-campaign-strategy` | `contests-promotions-and-gaming-rules.md` | [29; 1](../../preservation/playbook-social-media-contests.md) | green | set by the orchestrator |
| `playbook-question-engine` | `12-website-content-plan` | `buyer-question-content-plan.md` | [30; 1](../../preservation/playbook-question-engine.md) | green | set by the orchestrator |
| `owned-media-strategy` | `peso-integrated-strategy` | `owned-media-assets.md` | [36; 2](../../preservation/owned-media-strategy.md) | green | set by the orchestrator |
| `playbook-location-based-marketing` | `platform-google-business-profile` | `location-based-and-proximity-marketing.md` | [34; 2](../../preservation/playbook-location-based-marketing.md) | green | set by the orchestrator |
| `platform-instagram-growth` | `platform-instagram` | `growth-diagnosis-and-experiments.md` | [50; 2](../../preservation/platform-instagram-growth.md) | green | set by the orchestrator |
| `platform-instagram-visual-system` | `platform-instagram` | `grid-and-visual-system.md` | [25; 2](../../preservation/platform-instagram-visual-system.md) | green | set by the orchestrator |
| `platform-linkedin-company-pages` | `platform-linkedin` | `company-pages-showcase-and-events.md` | [43; 2](../../preservation/platform-linkedin-company-pages.md) | green | set by the orchestrator |
| `playbook-whatsapp-business` | `platform-whatsapp` | `whatsapp-business-app-operations.md` | [25; 2](../../preservation/playbook-whatsapp-business.md) | green | set by the orchestrator |

Every dropped row names the equivalent target text (the shared contract scaffolding and duplicated References / AGENTS.md / anti-slop links). Target sizes (all ≤ 500): `01-client-brief` 383, `02-platform-audit` 352, `03-audience-personas` 351, `04-brand-voice-intake` 393, `07-email-marketing-strategy` 444, `08-influencer-marketing-strategy` 418, `09-campaign-strategy` 435, `12-website-content-plan` 270, `peso-integrated-strategy` 301, `platform-google-business-profile` 427, `platform-instagram` 152, `platform-linkedin` 182, `platform-whatsapp` 383. Moved reference files: `02-platform-audit/references/proposal-frameworks.md` and `07-email-marketing-strategy/references/launch-sequence-operations.md` (plain moves with provenance lines; empty source `references/` folders removed).

## Referrers re-pointed (live files)

`AGENTS.md` (strategy category row; the `platform-linkedin-company-pages` row in the skill table now names `platform-linkedin`), `README.md` (counts 151 → 132, category table, 19 rows removed), `.claude-plugin/plugin.json` (regenerated, 132), `.claude-plugin/marketplace.json` (count text), `docs/quality-gates/legal-market-release-gate.md` (UGC link), `tests/routing-fixtures.json` (`instagram-growth-collision`), and these skill files: `biz-dev-lawful-prospecting-outreach/SKILL.md` (description, `Do Not Use When`, References link), `blog-writer/references/whitepaper-and-ebook-structure.md`, `direct-response-funnel-copy/SKILL.md` and `references/funnel-architecture-and-scripts.md`, `framework-community-trust/SKILL.md`, `meta-social-listening/references/listening-operations-playbook.md` (UGC workflow link, completing S04 review finding 9), `meta-social-proof-system/SKILL.md` (two), `05-social-media-strategy/SKILL.md`, `playbook-marketing-automation/SKILL.md`, `playbook-word-of-mouth-strategy/SKILL.md` (two), `strategy-channel-architecture/SKILL.md`, `strategy-video-content/references/podcast-and-audio-series.md`. Targets re-pointed their own mentions (for example `01-client-brief` named `00-client-intake` ten times; `03-audience-personas/references/persona-discipline.md`).

Phase check over live paths: no live file names or links any of the 19 sources outside `ALIAS.md`, provenance lines, "formerly" and "absorbed" notes. Broken/alias/host-absolute link scan over live markdown: 0 findings. The repository link test passes (one relative link in the new `owned-media-strategy` map was corrected).

## Currentness

- No source moved an overdue register claim. Workers cited existing records (for example WHATSAPP-BUSINESS-POLICY, WHATSAPP-USAGE-EA-2026, KE-BCLB-GAMBLING-ADS-2025, TZ-ONLINE-CONTENT-2020, UG-DPPA-2019, UG-DPPA-S26-DIRECT-MARKETING-2026, META-CREATIVE-SPECS-2026, MELTWATER-LINKEDIN-REPORT-2026) and marked every other benchmark, limit and platform behaviour "verify before stating (no register record)".
- **New register record:** INSTAGRAM-HASHTAG-LIMIT-2025 (Social Media Today, 18 Dec 2025, reporting Instagram's statement that captions on posts and Reels will gradually be capped at five hashtags; tier 3, partial; read live 29 Sep 2026). Cited in `social-brand-style-guide.md`. Follow-up: the S03 `caption-writer` hashtag reference still recommends 5–10 Instagram tags (S08/S10).
- Citation details added from general knowledge (flagged in the maps or references, to be confirmed in S09/S13): Wiley for Bodnar and Cohen (2012), Sheridan (2019) and Butow and Walker (2025); AMACOM for Westergaard (2016); Pearson for Chaffey and Kotler. Ltifi (Ed.) (2024) was confirmed live as CRC Press.

## Alias fixtures

All 19 `alias-<source>` fixtures (one per source, `alias_of` set, expected = target) rank 1, as does the re-pointed `instagram-growth-collision` (`platform-instagram`). The six fixtures below rank 1 are the same six as after S03 and S04 (all rank 2, all outside S05).

## Gate block (merge runbook, `--min-rank1 91`)

Full output: [gate-block-2026-09-29.txt](gate-block-2026-09-29.txt).

| Check | After S04 | After S05 |
|---|---|---|
| `validate_skill_engine.py --baseline quality-baseline.json` | 151 compliant, 0 failures | **132 compliant, 0 failures** |
| `routing_smoke_test.py --min-rank1 91 --lint-fixtures` | 98/98; p@1 92/98 (93.9 %) | **117/117 top-3 = 1.000; p@1 111/117 (94.9 %)**; lint 0 |
| `check_skill_aliases.py` | routes 41 | **routes 60, findings 0, active 132** |
| `pytest -q tests` / `unittest discover` | 49 passed / OK | 49 passed / OK |
| `check_source_freshness.py` | PASS (90) | PASS (91) |
| `source_ingestion_guardrail.py` | 0 findings | 0 findings |
| `git diff --check` | clean | clean |
| `render_host_files.py --check` (engine and workspace) | findings 0 | findings 0 |
| `generate-plugin-manifest.js --check-marketplace` | 23 ok, 0 drift | 23 ok, 0 drift |
| `validate-runtime-skill-budget.py --collisions` | PASS (skills 1129) | PASS, 0 undeclared ≥ 0.75 (skills 1110) |
| `validate-routing-baseline.py` | PASS | PASS |
| `validate-no-book-extractions.py` | roots 12, findings 0 | roots 12, findings 0 |
| `lexical_routing.py --collisions` | exit 0 | exit 0 |

Routing figures are a lexical proxy, not live routing. Model-executed behavioural runs: `NOT_ASSESSED (zero-spend rule)`.

## Open items and limitations

- **Competing figures kept side by side** (S09 reconciles): WhatsApp active/lapsed line 90 versus 60 days, promotional broadcasts 2 versus 3 a week, pricing never blank versus "contact for pricing", thumbnail 48 versus 50 px; GBP photo minimum 10 (location reference) versus 8 (target score); the audit-offer score "out of 50" where four scored areas give 40 (reference tells the user to state the base); the location source's superlative GBP description example (kept with a note that the target bans superlatives in that field).
- **Legal points without a register record** (verify before stating): Uganda and Kenya permits for chance-based prize draws; Uganda prize withholding tax.
- **Citation backlog:** Rageh (Ed.) (2026) editor initials and publisher; Raymond and Johnston (2021) title; Hietaniemi (2020) and Walsh Phillips (2023) publishers; Walker's *Launch* year and publisher; Johnson (2023), Sant (2012), Hatton (2007) publishers.
- **Wording edit in a template:** "what this unlocks" became "what this answer settles" in the intake Phase 2 template (recorded in the `00-client-intake` map row 12).
- `docs/engine-tours/social-media-skills.{json,md}` in `chwezi-engine-agents` still state 191; S12 regenerates them.

## Independent review

Reviewer: independent review agent (Claude Opus 5.5, read-only), 29 Sep 2026. **Phase verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`**, conditional on two blocking findings, both fixed below. No source was rejected; every §5.2 seed heading is mapped, every DROPPED row names existing target text, all 19 `ALIAS.md` files are the original text plus the banner, every cited register ID exists, and at least five facts per source were confirmed in the destination. Per source: 7 `ACCEPT` (`00-client-intake`, `playbook-profile-optimisation`, `ai-synthetic-personas`, `strategy-multigenerational-digital`, `biz-dev-reactivation-campaign`, `playbook-whatsapp-business`, `platform-instagram-visual-system`); 12 `ACCEPT_WITH_DOCUMENTED_LIMITATIONS` (named in each map's reviewer line). All 19 maps are signed.

Findings fixed after review (29 Sep 2026):

| # | Finding | Fix |
|---|---|---|
| 1 (blocking) | `growth-diagnosis-and-experiments.md` required 15–25 hashtags and kept 8–15 per post, contradicting the five-tag register record | Checklist now "sets of at most five tags per post"; current-cap note added; the thirty-tag sentence labelled legacy |
| 2 (blocking) | Evidence linked a gate-block file not yet written (repository link test failed) | Written after the final gate run |
| 3–4 | Style-guide Instagram hashtag row (5–10 / 30) and Stories safe zone contradicted the register | Row now 3–5 / 5 with the register ID; safe zone 14 % top, 35 % bottom, 6 % sides (META-CREATIVE-SPECS-2026) |
| 5 | 55-word transition script of unclear origin | Labelled a house script, not a quotation |
| 6–7 | WhatsApp opt-in and "saved number" rules stated as fact | Qualified with verify notes |
| 8 | Bly (2018) marked "title not recorded" though the engine holds the full citation | Full citation used |
| 10 | UGX income bands read as statistics | Labelled engine house bands; check against UBOS-NSI-2026 |
| 12 | Unsupported "highest-converting" claim; unverified "Add Post to Story" feature | Labelled |
| 13 | Contest timeline pointed at step 7 (legal) instead of step 9 (follow-up) | Corrected |
| 14 | Publishers and titles added from memory | Marked "added at merge; verify"; Chaffey co-author noted |
| 15 | Unsourced asides (retired 20 % text rule; Spark AR) | Verify notes; Spark AR treated as unavailable unless confirmed live |
| 16 | Map accuracy (hashtag-cap date and registration; "line 88"; one MOVED row) | Corrected |
| 17 | Map footers still pending | Signed with verdicts; the tick column is recorded as the worker's self-check confirmed by the reviewer |

Recorded as limitations rather than changed: finding 9, competing email cadence figures (`owned-media-assets.md` B2C 1–2 a month; `07-email-marketing-strategy` SKILL.md two a week in weeks 1–12; `email-funnel-build-sequence.md` weekly under 500 subscribers), for S09 to reconcile; finding 11, Ltifi (2024) here versus 2025 in five other engine files (citation backlog, S09/S13).

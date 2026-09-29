# S04 evidence: measurement, analytics and tracking merges (with NEW `measurement-tracking-plan`)

- **Date:** 29 September 2026.
- **Executor:** Claude (Opus 5.5) under the Social Kaizen executor brief; the orchestrator commits. Five merge workers did steps 1–6 of the [merge runbook](../../merge-runbook.md) for seven target clusters; the coordinator built the NEW skill, did S04-T03 and steps 7–10 (registry, referrers, fixtures, counts, README, plugin and marketplace, gates, evidence).
- **Start state:** HEAD `8eacccb` (S03 committed), clean worktree. Rollback: revert the S04 commit.
- **Active skills:** 162 → **151** (12 MERGE-INTO, 1 NEW).
- **Authority:** decisions ratified by orchestrator under Peter's delegated authority, 29 Sep 2026 (D-SK-03, D-SK-04, D-SK-05 for the NEW skill G04, D-SK-06 lean template; see [decisions.md](../../decisions.md)).
- **Git:** no commit, stage or `git mv`; plain renames and moves, which `git add -A` records as renames.

## Tasks

| Task | Target | Sources → reference | Status |
|---|---|---|---|
| S04-T01 | `measurement-tracking-plan` (NEW, G04) | built from the lean template (00-roadmap §7): SKILL.md 109 lines + 4 new references (`event-taxonomy-and-tracking-plan.md`, `consent-mode-and-cmp.md`, `server-side-capi-and-enhanced-conversions.md`, `ga4-bigquery-export.md`); owns SL05-C2, SL06-C3, SL06-C4, SL09-C5, SL10-C4, SL14-C4, SL15-C1..C4; collision fixture `tracking-plan-vs-attribution` added (rank 1) | DONE |
| S04-T02 | `ad-testing-and-scaling` | `strategy-organic-paid-hybrid` → `organic-to-paid-amplification.md` | DONE |
| S04-T03 | `measurement-tracking-plan` | `meta-analytics-privacy` → `consent-retention-and-sharing-review.md`; `meta-utm-tracking` → `utm-convention-and-campaign-register.md` | DONE (two source claims corrected, see below) |
| S04-T04 | `meta-algorithm-guide` | `meta-posting-optimisation` → `posting-time-and-frequency-tests.md` | DONE |
| S04-T05 | `meta-budget-planner` | `meta-revenue-planning` → `bottom-up-revenue-plan.md` | DONE |
| S04-T06 | `meta-reporting` | `meta-dashboard-design` → `dashboard-specification.md`; `meta-social-marketing-mix-review` → `quarterly-marketing-mix-review.md` | DONE |
| S04-T07 | `meta-roi-framework` | `meta-cohort-analysis` → `retention-cohorts-and-ltv.md`; `meta-social-media-roi-business-case` → `investment-business-case.md` | DONE |
| S04-T08 | `meta-sales-marketing-alignment` | `meta-lead-scoring` → `lead-scoring-model.md` | DONE |
| S04-T09 | `meta-social-listening` | `meta-sentiment-analysis` → `sentiment-and-share-of-voice-method.md`; `playbook-sentiment-listening` → `listening-operations-playbook.md` | DONE |
| S04-T10 | fixtures | 12 alias-routing fixtures (`alias_of`) + 1 collision fixture | DONE: all 13 rank 1 |
| S04-T11 | count and registry | `quality-baseline.json` and `docs/skill-aliases.yml` = 151; 12 routes added (41 cumulative) | DONE |

No source had a `references/` folder, so no reference files were moved.

## NEW skill: `measurement-tracking-plan` (G04)

- **Contract:** lean template (00-roadmap §7): two-sentence purpose; `Use When` in client words (six bullets, two of them "(formerly …)" for the merged sources); `Do Not Use When` names `advertising-attribution-and-measurement`, `meta-reporting`, `meta-social-metrics-framework`, `ad-to-site-journey-handoff` and the legal stop; six input rows; eight workflow steps with a stop and a rerun; eight decision rows; the canonical capability and degraded-mode sentences. Description 349 characters.
- **Neighbour split:** `advertising-attribution-and-measurement` keeps models, economics, incrementality and reconciliation; its description and `Do Not Use When` now send the tracking plan (events, Consent Mode v2, CAPI/enhanced conversions, UTM, BigQuery export) to the new skill. Collision fixture `tracking-plan-vs-attribution` ranks the new skill first, attribution second.
- **Currentness (digital-research-engine `source-evaluation` / `source-verification`; kaizen currentness gate):** every changed platform or legal claim was read live on 29 Sep 2026 from the primary page and entered in `docs/source-registers/source-register.json` with scope, publication date, access date, freshness class, review date and status (14 new records, 76 → 90):

| Register ID | Source (benchmark code) | Claim carried |
|---|---|---|
| GOOGLE-CONSENT-MODE-PARAMS-2026 | Google Ads Help 13802165 (S08) | four Consent Mode v2 parameters and denied-state behaviour |
| GOOGLE-CONSENT-MODE-DEV-2026 | Google for Developers consent-mode overview | basic versus advanced mode; modelling type |
| GA4-CONSENT-MODELLING-2026 | Analytics Help 11161109 | modelling thresholds (1,000 events/day denied for 7 days; 1,000 daily users granted 7 of 28 days; Blended identity) |
| GOOGLE-ENHANCED-CONVERSIONS-2026 | Google Ads Help 9888656 (S09) | SHA-256 hashing, normalisation, web and leads |
| META-CAPI-DEDUP-2026 | Meta for Developers dedup page (S10) | event_id/eventID + event name; 48-hour window; fbp/external_id limits |
| META-CAPI-PARAMETERS-2026 | Meta server-event and customer-information parameters | 7-day event_time; action_source values; hash / never-hash fields |
| GOOGLE-SGTM-2026 | Google server-side tagging overview (S11) | Cloud Run; USD 30–50 per server; 3 instances; HttpOnly first-party cookies |
| GA4-BIGQUERY-EXPORT-2026 | Analytics Help 9358801 (S12) | 1M events/day standard; 20B 360; streaming USD 0.05/GB, no completeness SLO; fresh daily 360 only |
| GA4-DATA-RETENTION-2026 | Analytics Help 7667196 | 2 or 14 months; explorations and funnels only |
| GA4-IP-2026 | Analytics Help 2763052 | GA4 does not log or store IP addresses |
| GA4-UTM-PARAMETERS-2026 | Analytics Help 10917952 | nine UTM parameters; utm_id and utm_source_platform recommended |
| GA4-ENGAGED-SESSION-2026 | Analytics Help 12195621 | engaged-session definition |
| GOOGLE-CMP-TCF-2026 | AdSense Help 13554116 (primary for S71) | certified CMP + IAB TCF: EEA/UK 16 Jan 2024; CH 31 Jul 2024 |
| UG-PDPO-OFFSHORE-2025 | DLA Piper report of the PDPO decision of 18 Jul 2025 (E15; partial, tier 3) | registration of offshore handlers; cross-border transfer records |

- **Corrections to merged source content:** (1) `meta-analytics-privacy` told consultants to switch on GA4 IP redaction; GA4 does not log or store IP addresses (GA4-IP-2026), so the step is recorded as "not applicable in GA4" and replaced by a no-personal-data-in-URLs check. (2) The five-parameter UTM table gains `utm_id` and `utm_source_platform`; "Conversions" appears as key events; Universal Analytics is treated as archive only. Both are recorded in the maps.
- **Carried as verify-at-use (no register record):** CCPA thresholds, CookieYes/Usercentrics plans, GA4 menu paths, recommended-event names, the default channel grouping of custom mediums, the 40–60 % → 20 % dark-social range, BigQuery storage and query pricing.
- **Skill safety audit (read-only, `skill-safety-audit` checklist):** Safety Status **Safe**. Findings: no install or execute commands, no credential requests, no network or system actions, no bundled scripts; third-party tools are named, never installed; the skill forbids tag publishing, uploads and consent changes without action-specific authority. Required actions: accept.

## Merges

| Source | Target | Reference | Preservation map (rows; rows containing `DROPPED`) | Gates | Commit |
|---|---|---|---|---|---|
| `strategy-organic-paid-hybrid` | `ad-testing-and-scaling` | `organic-to-paid-amplification.md` | [26; 1](../../preservation/strategy-organic-paid-hybrid.md) | green | set by the orchestrator |
| `meta-analytics-privacy` | `measurement-tracking-plan` | `consent-retention-and-sharing-review.md` | [30; 3](../../preservation/meta-analytics-privacy.md) | green | set by the orchestrator |
| `meta-utm-tracking` | `measurement-tracking-plan` | `utm-convention-and-campaign-register.md` | [23; 3](../../preservation/meta-utm-tracking.md) | green | set by the orchestrator |
| `meta-posting-optimisation` | `meta-algorithm-guide` | `posting-time-and-frequency-tests.md` | [23; 2](../../preservation/meta-posting-optimisation.md) | green | set by the orchestrator |
| `meta-revenue-planning` | `meta-budget-planner` | `bottom-up-revenue-plan.md` | [22; 2](../../preservation/meta-revenue-planning.md) | green | set by the orchestrator |
| `meta-dashboard-design` | `meta-reporting` | `dashboard-specification.md` | [16; 3](../../preservation/meta-dashboard-design.md) | green | set by the orchestrator |
| `meta-social-marketing-mix-review` | `meta-reporting` | `quarterly-marketing-mix-review.md` | [19; 2](../../preservation/meta-social-marketing-mix-review.md) | green | set by the orchestrator |
| `meta-cohort-analysis` | `meta-roi-framework` | `retention-cohorts-and-ltv.md` | [18; 3](../../preservation/meta-cohort-analysis.md) | green | set by the orchestrator |
| `meta-social-media-roi-business-case` | `meta-roi-framework` | `investment-business-case.md` | [19; 2](../../preservation/meta-social-media-roi-business-case.md) | green | set by the orchestrator |
| `meta-lead-scoring` | `meta-sales-marketing-alignment` | `lead-scoring-model.md` | [18; 3](../../preservation/meta-lead-scoring.md) | green | set by the orchestrator |
| `meta-sentiment-analysis` | `meta-social-listening` | `sentiment-and-share-of-voice-method.md` | [27; 2](../../preservation/meta-sentiment-analysis.md) | green | set by the orchestrator |
| `playbook-sentiment-listening` | `meta-social-listening` | `listening-operations-playbook.md` | [36; 3](../../preservation/playbook-sentiment-listening.md) | green | set by the orchestrator |

Every dropped row names the equivalent target text (the shared contract scaffolding, templated routing rows to a neighbour that is now the same owner, and duplicated Read next / References bullets). Target sizes after the merge (all ≤ 500): `ad-testing-and-scaling` 160, `meta-algorithm-guide` 438, `meta-budget-planner` 334, `meta-reporting` 378, `meta-roi-framework` 392, `meta-sales-marketing-alignment` 247, `meta-social-listening` 421, `measurement-tracking-plan` 109.

## Referrers re-pointed (live files)

`README.md` (counts 162 → 151, category table, 12 rows removed, `measurement-tracking-plan` row added), `.claude-plugin/plugin.json` (regenerated, 151), `.claude-plugin/marketplace.json` (count text), `docs/quality-gates/legal-market-release-gate.md` (analytics-privacy link), `docs/continuous-improvement/kaizen-wave-1-2026-08-11.md` (three links now point at the historical `ALIAS.md` files so the repository link test passes; the record keeps the old names), and these skill files: `advertising-attribution-and-measurement/SKILL.md` (description, two `Do Not Use When` rows, input row), `ad-to-site-journey-handoff/SKILL.md` (two) and its `references/measurement-and-ownership-spec.md` and `references/ux-engagement-diagnostics.md`, `ad-copy-and-hook-lab/references/format-copy-fitting.md`, `media-planning/references/scheduling-weighting-and-post-buy.md`, `paid-search-advertising/SKILL.md` and `references/search-build-specification.md`, `ai-influencer-strategy/SKILL.md`, `ai-use-case-mapping/references/predictive-analytics-use-cases.md` (two), `meta-social-metrics-framework/SKILL.md` (two), `meta-testing-framework/SKILL.md` (seven: neighbour now `meta-algorithm-guide`), `01-client-brief/references/ux-strategy-and-product-lenses.md`, `06-digital-marketing-strategy/references/digital-planning-lenses.md`, `playbook-paid-social-advertising/SKILL.md` (three), `playbook-post-click-strategy/SKILL.md`, `playbook-word-of-mouth-strategy/SKILL.md` (two), `strategy-b2b-customer-community/SKILL.md`. Targets re-pointed their own neighbour mentions of retired names (for example `meta-reporting` → `05-social-media-strategy`, `meta-roi-framework` → `meta-budget-planner`, `meta-social-listening` → `meta-competitor-analysis`, `meta-budget-planner` and `meta-sales-marketing-alignment` → `meta-roi-framework`).

Phase check over live paths (`skills/` excluding `ALIAS.md`, `AGENTS.md`, `README.md`, `docs/quality-gates`, `docs/evidence-packs`): no `<source>/SKILL.md` link or name remains for any of the 12 sources outside `ALIAS.md`, provenance lines and "formerly" notes. A broken/alias/host-absolute link scan over 349 live markdown files returned 0 findings. Historical records (plans, gap analyses, engine-upgrade inventories) keep the old names.

## Alias fixtures

| Fixture id | Expected | Rank |
|---|---|---|
| `tracking-plan-vs-attribution` (collision) | `measurement-tracking-plan` | 1 |
| `alias-strategy-organic-paid-hybrid` | `ad-testing-and-scaling` | 1 |
| `alias-meta-analytics-privacy` | `measurement-tracking-plan` | 1 |
| `alias-meta-utm-tracking` | `measurement-tracking-plan` | 1 |
| `alias-meta-posting-optimisation` | `meta-algorithm-guide` | 1 |
| `alias-meta-revenue-planning` | `meta-budget-planner` | 1 |
| `alias-meta-dashboard-design` | `meta-reporting` | 1 |
| `alias-meta-social-marketing-mix-review` | `meta-reporting` | 1 |
| `alias-meta-cohort-analysis` | `meta-roi-framework` | 1 |
| `alias-meta-social-media-roi-business-case` | `meta-roi-framework` | 1 |
| `alias-meta-lead-scoring` | `meta-sales-marketing-alignment` | 1 |
| `alias-meta-sentiment-analysis` | `meta-social-listening` | 1 |
| `alias-playbook-sentiment-listening` | `meta-social-listening` | 1 |

No existing fixture had a source as `expected`. The six fixtures below rank 1 are the same six as after S03 (`blog-positive`, `ai-slop`, `geo-page`, `beginner-training`, `mf-collision`, `b2b-collision`; all rank 2, all outside S04).

## Gate block (merge runbook, `--min-rank1 91`)

Full output: [gate-block-2026-09-29.txt](gate-block-2026-09-29.txt).

| Check | After S03 | After S04 |
|---|---|---|
| `validate_skill_engine.py --baseline quality-baseline.json` | 162 compliant, 0 failures | **151 compliant, 0 failures** |
| `routing_smoke_test.py --min-rank1 91 --lint-fixtures` | 85/85; p@1 79/85 (92.9 %) | **98/98 top-3 = 1.000; p@1 92/98 (93.9 %)**; lint 0 |
| `check_skill_aliases.py` | routes 29 | **routes 41, findings 0, active 151** |
| `pytest -q tests` / `unittest discover` | 49 passed / OK | 49 passed / OK |
| `check_source_freshness.py` | PASS (76) | PASS (90) |
| `source_ingestion_guardrail.py` | 0 findings | 0 findings |
| `git diff --check` | clean | clean |
| `render_host_files.py --check` (engine and workspace) | findings 0 | findings 0 |
| `generate-plugin-manifest.js --check-marketplace` | 23 ok, 0 drift | 23 ok, 0 drift |
| `validate-runtime-skill-budget.py --collisions` | PASS | PASS, 0 undeclared ≥ 0.75 (skills 1129) |
| `validate-routing-baseline.py` | PASS | PASS |
| `validate-no-book-extractions.py` | roots 12, findings 0 | roots 12, findings 0 |
| `lexical_routing.py --collisions` | exit 0 | exit 0 |

Routing figures are a lexical proxy, not live routing. Model-executed behavioural runs: `NOT_ASSESSED (zero-spend rule)`.

## Open items and limitations

- **Competing figures kept side by side** (S09 reconciles): lead-scoring MQL thresholds (existing 50 points versus merged 60 B2B / 40 EA starter); two lifetime-value formulas in `meta-budget-planner`; RAG amber threshold 10 % (dashboard) versus 15 % (monthly report); two net-sentiment-score band sets (EA service-business bands versus Johnsen (2024) weekly bands); posting-frequency tables in `meta-algorithm-guide` §5–§6.1 versus the merged EA baseline windows.
- **Neighbour names chosen under the merge** (S08 finalises descriptions): `meta-sales-marketing-alignment` now names `meta-roi-framework` as its neighbour (weak fit); `meta-reporting` names `05-social-media-strategy`.
- **Unverified tool claims** carried with "verify before stating (no register record)": MonkeyLearn figures (the service may no longer exist), Looker Studio connector claims, UGX reach and CPM bands, Kahan (2022) funnel benchmarks.
- **Citation backlog (S09/S13):** Chaffey (2024) edition unstated in `organic-to-paid-amplification.md`; Raaz (c.2023) *Web Analytics Blueprint* publisher unknown.
- `docs/engine-tours/social-media-skills.{json,md}` in `chwezi-engine-agents` still state 191; S12 regenerates them.
- Working copies use CRLF under `core.autocrlf=true`; git stores LF.

## Independent review

Reviewer: independent review agent (Claude Opus 5.5, read-only), 29 Sep 2026. **Phase verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`**, conditional on two blocking findings, both fixed below. The reviewer confirmed at least five facts per source in the destination, re-read six live platform pages (all matched the register), found all 24 cited register IDs present, and rated the NEW skill `ACCEPT_WITH_DOCUMENTED_LIMITATIONS` (skill-safety audit: Safe). Per source: 7 `ACCEPT` (`meta-utm-tracking`, `meta-revenue-planning`, `meta-dashboard-design`, `meta-social-marketing-mix-review`, `meta-cohort-analysis`, `meta-social-media-roi-business-case`, `meta-sentiment-analysis`); 5 `ACCEPT_WITH_DOCUMENTED_LIMITATIONS` (named in each map's reviewer line). All 12 maps are ticked and signed.

Findings fixed after review (29 Sep 2026):

| # | Finding | Fix |
|---|---|---|
| 1 (blocking) | `meta-lead-scoring` map row 1 dropped the "historical lead outcomes, CRM fields" input with no equivalent | Input row added to `lead-scoring-model.md` § Inputs; map row 1 annotated |
| 2 (blocking) | 48-hour opt-out attributed to the DPPA s.26 record (which records a written request and a 14-day response) | Reworded as a house standard stricter than the statute, citing the 14-day response |
| 3 | Consent banner stated as a legal requirement "under local law" in three places | Reworded: consent treated as required where cookies or identifiers collect personal data; confirm with counsel; KE-ODPC record added |
| 4 | Unsourced "increasingly scrutinised under the DPPA" | Labelled as the original skill's claim, verify before stating |
| 5 | GDPR DPO trigger oversimplified | Replaced with the core-activities / special-category / public-authority test (verify) |
| 6 | "Native analytics need no extra consent" doubtful for EU Page Insights | Limited to outside the EEA/UK; joint-controllership note added |
| 7 | Pre-CPRA CCPA thresholds shown as current | Labelled as the original skill's figures; verify current values |
| 8 | PII policy and snake_case convention without register IDs | "verify at use; no register record" added |
| 9 | UGC link pointed at content that arrives only in S05 | Link kept on the still-active `playbook-ugc-strategy`; re-point listed for S05-T06 |
| 10–12 | Three map rows named imprecise equivalents | Rows annotated with the exact equivalent; anti-slop gate links added to `measurement-tracking-plan` § References |
| 14 | "IP addresses truncated" wording | Now "Ads products truncate IP addresses at collection", as on the live page |
| 15 | Attribution description opened "defining conversion events", overlapping the event map | Now "deciding which conversions count for credit" |
| SL10-C4, SL14-C4 thin | No procedure for consent-aware experiment measurement or first-party data activation | Five-step procedures added to `server-side-capi-and-enhanced-conversions.md` and `consent-mode-and-cmp.md` |
| 19 | `meta-posting-optimisation` map line count | 364 |

Left for later phases, as the reviewer allowed: finding 13 (`meta-sales-marketing-alignment` templated neighbour, S08), 16 (link text in the historical kaizen-wave-1 record, accepted under the S03 precedent), 17 (canonical capability and degraded-mode sentences reworded; S09 restores them verbatim). Note for finding 19: regenerating `plugin.json` with the existing `scripts/generate-plugin-manifest.js` also refreshed its hooks description text; this came from the generator, not from an S04 edit.

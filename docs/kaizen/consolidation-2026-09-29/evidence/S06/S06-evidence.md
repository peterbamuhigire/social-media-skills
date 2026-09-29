# S06 evidence: community, reputation, PR, selling, commerce and operations merges

- **Date:** 29 September 2026.
- **Executor:** Claude (Opus 5.5) under the Social Kaizen executor brief; the orchestrator commits. Five merge workers did steps 1–6 of the [merge runbook](../../merge-runbook.md) for ten target clusters; the coordinator did steps 7–10 (retirement, registry, referrers, fixtures, counts, README, AGENTS, plugin and marketplace, gates, evidence).
- **Start state:** HEAD `ce3299a` (S05 committed), clean worktree. Rollback: revert the S06 commit.
- **Active skills:** 132 → **117** (15 MERGE-INTO). `frameworks/` now holds only inactive aliases.
- **Authority:** decisions ratified by orchestrator under Peter's delegated authority, 29 Sep 2026 (D-SK-03, D-SK-04; see [decisions.md](../../decisions.md)).
- **Git:** no commit or `git mv`; plain renames and moves. The orchestrator should stage each `SKILL.md` deletion with its new `ALIAS.md` so git records the renames.

## Tasks

| Task | Target | Sources → reference | Status |
|---|---|---|---|
| S06-T01 | `playbook-community-management` | `framework-community-trust` → `community-trust-framework.md`; `playbook-social-customer-service` → `social-customer-care.md`; `strategy-micro-communities` → `micro-community-design.md` | DONE |
| S06-T02 | `playbook-daily-operations-routine` | `strategy-pdca-workflow-design` → `pdca-review-cadence.md` | DONE |
| S06-T03 | `playbook-post-click-strategy` | `ecommerce-conversion-optimisation` → `ecommerce-and-whatsapp-conversion-diagnosis.md` | DONE |
| S06-T04 | `playbook-pr-publicity` | `playbook-geo-newsjacking` → `newsjacking-and-ai-citation.md`; `playbook-pr-media-integration` → `pr-media-integration.md` | DONE |
| S06-T05 | `playbook-social-media-policy` | `playbook-social-media-governance` → `governance-roles-access-and-approvals.md` | DONE |
| S06-T06 | `playbook-social-selling` | `playbook-employee-advocacy` → `employee-advocacy-programme.md`; `premium-social-selling` → `high-value-social-selling.md` (+ moved `premium-social-selling-gate.md`) | DONE |
| S06-T07 | `social-commerce-strategy` | `playbook-instagram-dm-sales` → `dm-conversation-selling.md` | DONE |
| S06-T08 | `strategy-csr-purpose-communications` | `framework-digital-transparency` → `digital-transparency-framework.md` | DONE |
| S06-T09 | `strategy-ewom-reviews` | `meta-social-proof-system` → `social-proof-asset-register.md`; `playbook-word-of-mouth-strategy` → `word-of-mouth-and-referral-design.md` | DONE |
| S06-T10 | `strategy-experiential-marketing` | `playbook-webinars-live-events` → `webinars-and-virtual-events.md` | DONE |
| S06-T11 | fixtures | 15 alias-routing fixtures (one per source, `alias_of` set) | DONE: all 15 rank 1 |
| S06-T12 | count and registry | `quality-baseline.json` and `docs/skill-aliases.yml` = 117; 15 routes added (75 cumulative) | DONE |

## Merges

| Source | Target | Reference | Preservation map (rows; rows containing `DROPPED`) | Gates | Commit |
|---|---|---|---|---|---|
| `framework-community-trust` | `playbook-community-management` | `community-trust-framework.md` | [22; 1](../../preservation/framework-community-trust.md) | green | set by the orchestrator |
| `playbook-social-customer-service` | `playbook-community-management` | `social-customer-care.md` | [19; 2](../../preservation/playbook-social-customer-service.md) | green | set by the orchestrator |
| `strategy-micro-communities` | `playbook-community-management` | `micro-community-design.md` | [21; 2](../../preservation/strategy-micro-communities.md) | green | set by the orchestrator |
| `strategy-pdca-workflow-design` | `playbook-daily-operations-routine` | `pdca-review-cadence.md` | [28; 2](../../preservation/strategy-pdca-workflow-design.md) | green | set by the orchestrator |
| `ecommerce-conversion-optimisation` | `playbook-post-click-strategy` | `ecommerce-and-whatsapp-conversion-diagnosis.md` | [30; 2](../../preservation/ecommerce-conversion-optimisation.md) | green | set by the orchestrator |
| `playbook-geo-newsjacking` | `playbook-pr-publicity` | `newsjacking-and-ai-citation.md` | [26; 2](../../preservation/playbook-geo-newsjacking.md) | green | set by the orchestrator |
| `playbook-pr-media-integration` | `playbook-pr-publicity` | `pr-media-integration.md` | [19; 2](../../preservation/playbook-pr-media-integration.md) | green | set by the orchestrator |
| `playbook-social-media-governance` | `playbook-social-media-policy` | `governance-roles-access-and-approvals.md` | [33; 2](../../preservation/playbook-social-media-governance.md) | green | set by the orchestrator |
| `playbook-employee-advocacy` | `playbook-social-selling` | `employee-advocacy-programme.md` | [20; 2](../../preservation/playbook-employee-advocacy.md) | green | set by the orchestrator |
| `premium-social-selling` | `playbook-social-selling` | `high-value-social-selling.md`, moved `premium-social-selling-gate.md` | [14; 2](../../preservation/premium-social-selling.md) | green | set by the orchestrator |
| `playbook-instagram-dm-sales` | `social-commerce-strategy` | `dm-conversation-selling.md` | [17; 2](../../preservation/playbook-instagram-dm-sales.md) | green | set by the orchestrator |
| `framework-digital-transparency` | `strategy-csr-purpose-communications` | `digital-transparency-framework.md` | [21; 2](../../preservation/framework-digital-transparency.md) | green | set by the orchestrator |
| `meta-social-proof-system` | `strategy-ewom-reviews` | `social-proof-asset-register.md` | [26; 1](../../preservation/meta-social-proof-system.md) | green | set by the orchestrator |
| `playbook-word-of-mouth-strategy` | `strategy-ewom-reviews` | `word-of-mouth-and-referral-design.md` | [38; 1](../../preservation/playbook-word-of-mouth-strategy.md) | green | set by the orchestrator |
| `playbook-webinars-live-events` | `strategy-experiential-marketing` | `webinars-and-virtual-events.md` | [30; 1](../../preservation/playbook-webinars-live-events.md) | green | set by the orchestrator |

Every dropped row names the equivalent target text (shared contract scaffolding and duplicated References blocks). Target sizes (all ≤ 500): `playbook-community-management` 258, `playbook-daily-operations-routine` 306, `playbook-post-click-strategy` 423, `playbook-pr-publicity` 229, `playbook-social-media-policy` 289, `playbook-social-selling` 491, `social-commerce-strategy` 388, `strategy-csr-purpose-communications` 226, `strategy-ewom-reviews` 248, `strategy-experiential-marketing` 250. Moved reference file: `playbook-social-selling/references/premium-social-selling-gate.md` (plain move with provenance line; the empty source `references/` folder was removed).

## Referrers re-pointed (live files)

`AGENTS.md` (strategy row drops `premium-social-selling`; `frameworks/` row now says inactive aliases only), `README.md` (counts 132 → 117, 15 rows removed, `frameworks` 0 with note, 15 active category folders), `.claude-plugin/plugin.json` (regenerated, 117), `.claude-plugin/marketplace.json` (count text), `docs/continuous-improvement/kaizen-wave-1-2026-08-11.md` (link to the retired PDCA skill now targets its `ALIAS.md`, as in S05), and these skill files: `ecommerce-brand-differentiation/SKILL.md` (description, `Do Not Use When`, Workflow step 1, reference line), `premium-commercial-writing/SKILL.md`, `strategy-creator-monetisation/SKILL.md` (description, `Do Not Use When`, Workflow step 1), `06-digital-marketing-strategy/SKILL.md`, `strategy-personal-brand/references/reputation-authority-and-network-system.md`, `platform-linkedin/references/company-pages-showcase-and-events.md`, `08-influencer-marketing-strategy/references/ai-assisted-influencer-discovery-and-virtual-creators.md`, `playbook-viral-content-design/references/bold-idea-risk-screen.md` (two). Targets re-pointed their own mentions (`playbook-daily-operations-routine` two; `social-commerce-strategy` neighbour now `playbook-social-selling`; `strategy-csr-purpose-communications` neighbour now `playbook-reputation-management`; `strategy-experiential-marketing` neighbour now `strategy-video-content`).

Phase check (`grep -rn "<source>/SKILL.md" skills AGENTS.md README.md docs/quality-gates`, excluding `ALIAS.md`): no output for all 15 sources. Broken/alias/host-absolute link scan over live markdown: 349 files, 0 findings. The repository link test passes.

## Currentness

- No source moved an overdue register claim. Workers applied existing records (UG-FACEBOOK-ACCESS-2026, WHATSAPP-BUSINESS-POLICY, WHATSAPP-USAGE-EA-2026, UG-CMA-2022-VOID-2026, UG-CMA-SECTIONS-STRUCK-2026, UG-DPPA-2019, UG-DPPR-2021, UG-PDPO-ORG, UG-DPPA-S26-DIRECT-MARKETING-2026, KE-DP-GENERAL-2021, KE-ODPC-DIRECT-MARKETING-2026, META-CAPI-DEDUP-2026, GOOGLE-AI-SEARCH-GUIDE-2026, PREMIUM-LI-POLICY-2026, PREMIUM-LI-AGREEMENT-2026, FTC-ENDORSEMENTS-REVIEWS-2026, UG-KE-INFLUENCER-DISCLOSURE-2026, UG-MOBILE-SPEED-2026, META-CREATIVE-SPECS-2026, DATAREPORTAL-UG-KE-2026) and marked every other benchmark, limit, price and platform behaviour "verify before stating (no register record)". The reviewer confirmed all 33 cited IDs exist.
- The governance source's Computer Misuse module is carried as void law (UG-CMA-2022-VOID-2026). No new register record this phase. UG-DPPA-2019 is due for review on 11 October 2026.

## Alias fixtures

All 15 `alias-<source>` fixtures (expected = target, `alias_of` set) rank 1. Five fixtures rank 2, all outside S06 (`blog-positive`, `ai-slop`, `geo-page`, `beginner-training`, `mf-collision`); after S05 there were six.

## Gate block (merge runbook, `--min-rank1 91`)

Full output: [gate-block-2026-09-29.txt](gate-block-2026-09-29.txt).

| Check | After S05 | After S06 |
|---|---|---|
| `validate_skill_engine.py --baseline quality-baseline.json` | 132 compliant, 0 failures | **117 compliant, 0 failures** |
| `routing_smoke_test.py --min-rank1 91 --lint-fixtures` | 117/117; p@1 111/117 (94.9 %) | **132/132 top-3 = 1.000; p@1 127/132 (96.2 %)**; lint 0 |
| `check_skill_aliases.py` | routes 60 | **routes 75, findings 0, active 117** |
| `pytest -q tests` / `unittest discover` | 49 passed / OK | 49 passed / OK |
| `check_source_freshness.py` | PASS (91) | PASS (91) |
| `source_ingestion_guardrail.py` | 0 findings | 0 findings |
| `git diff --check` | clean | clean |
| `render_host_files.py --check` (engine and workspace) | findings 0 | findings 0 |
| `generate-plugin-manifest.js --check-marketplace` | 23 ok, 0 drift | 23 ok, 0 drift |
| `validate-runtime-skill-budget.py --collisions` | PASS (skills 1110) | PASS, 0 undeclared ≥ 0.75 (skills 1095) |
| `validate-routing-baseline.py` | PASS | PASS |
| `validate-no-book-extractions.py` | roots 12, findings 0 | roots 12, findings 0 |
| `lexical_routing.py --collisions` | exit 0 | exit 0 |

Routing figures are a lexical proxy, not live routing. Model-executed behavioural runs: `NOT_ASSESSED (zero-spend rule)`. The alias prompts echo the new "(formerly …)" `Use When` bullets, which flatters lexical p@1; S08 rewrites descriptions and adds owned-negative fixtures.

## Open items and limitations

- `playbook-social-selling` SKILL.md is at 491 of 500 lines: S09 must trim it before any further addition.
- Left as "verify": the Facebook "Very responsive" badge rule; Macarthy 2022 versus 2023 edition; the WhatsApp 1,024-member group limit; all conversion benchmarks in the e-commerce reference; outlet contact addresses.
- **Citation backlog (S09/S13):** Chaffey (2024), cited as 8th edn, Pearson, lacks co-author Ellis-Chadwick and the edition/year is doubtful (`employee-advocacy-programme.md`, `newsjacking-and-ai-citation.md`, `pr-media-integration.md`); publishers added at merge for Funk (2011), Gladwell (2000) and Kotler et al. (2023) are marked verify; Rageh and Westergaard completed from other engine citations.
- Source oddities recorded, not changed: the PR amplification "7-step" checklist lists 8 steps (all kept); exclusives 48 hours (source) versus 48–72 hours (target).
- `docs/engine-tours/social-media-skills.{json,md}` in `chwezi-engine-agents` still state 191; S12 regenerates them.

## Independent review

Reviewer: independent review agent (Claude Opus 5.5, read-only), 29 Sep 2026. **Phase verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`**, no blocking finding. All 15 `ALIAS.md` files are the original text plus the banner; every §5.2 seed heading is mapped; every DROPPED row names existing target text; at least five facts per source were confirmed in the destination; all cited register IDs exist; no currentness regression. Per source: 5 `ACCEPT` (`framework-community-trust`, `strategy-pdca-workflow-design`, `playbook-geo-newsjacking`, `playbook-employee-advocacy`, `playbook-instagram-dm-sales`); 10 `ACCEPT_WITH_DOCUMENTED_LIMITATIONS` (named in each map's reviewer line). All 15 maps are signed.

Findings fixed after review (29 Sep 2026):

| # | Finding | Fix |
|---|---|---|
| 1, 2, 4 | Long quoted scripts and examples read as quotations (`social-customer-care.md`, `micro-community-design.md`, `dm-conversation-selling.md` ×2, `social-proof-asset-register.md`) | Labelled engine house wording / house template, not quotations |
| 3 | Minimum test-run rule (2 weeks or 200 impressions) stated without caution | Qualified: 200 impressions rarely supports a significance test; use decision rule 3 |
| 5 | Bodnar and Cohen (2012) cited without a title in the governance reference | Full citation; map row 32 updated |
| 6 | Two premium-selling scaffolding items dropped against weak equivalents | Contradictory-evidence decision row and the ai-slop-audit F-grade release block moved into `high-value-social-selling.md`; map row 1 updated |
| 7 | PR pitch threshold tightened from "tick at least three" to "at least three strong" | Source wording restored |
| 11 | Facebook Live recommendation unqualified in the transparency reference | UG-FACEBOOK-ACCESS-2026 qualifier added |
| 12 | Hybrid event default was Facebook Live | Conditional on confirmed access, with YouTube Live as the alternative |
| 13 | Target `strategy-ewom-reviews` stated the 80 % response-drop figure as fact | Marked legacy, no register record, verify |
| 14 | Publishers added at merge without a note | Marked "publisher added at merge; verify" |
| 15 | `social-commerce-strategy` pointed at the post-click SKILL.md for detail held in the new reference | Re-pointed to `ecommerce-and-whatsapp-conversion-diagnosis.md` |
| 17, 18 | Maps unsigned; three maps named dropped anti-patterns only by number | Maps signed; equivalent target anti-patterns quoted by their first words |
| 19 | Evidence folder missing | This file and the gate-block output |

Recorded as limitations rather than changed: findings 8–10 (Chaffey citation, Facebook badge rule, Macarthy edition), 16 (491-line target), 20a (alias prompts echo the new bullets; S08). Finding 20b (stage deletions with the new `ALIAS.md` files so git records renames) is for the orchestrator.

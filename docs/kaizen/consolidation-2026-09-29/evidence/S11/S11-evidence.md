# S11 evidence: routing and collision re-baseline

- **Phase:** Social Kaizen 2026-09-29, S11 (plan `04-phases/S11-routing-and-collision-rebaseline.md`).
- **Date:** 29 September 2026. **Start commit:** `973e1af` (S10); worktree clean at start (`git status --short` empty in both repositories).
- **Active skills:** 112 → 112.
- **Change classes:** workflow-routing (four skills' routing text, fixtures, the social floor, `ownership.yaml` notes, two oracle targets); metadata (baseline JSON, register fold, evidence). No route moved between engines, so no Peter-level approval was needed. Decisions D-SK-01 to D-SK-07 stand as ratified by orchestrator under Peter's delegated authority.
- **Limits:** every routing figure is a lexical proxy, not live routing. Behavioural (Tier 3) routing for social is `NOT_ASSESSED (zero-spend rule)` (S11-T07); the S13 scorecard must say so rather than imply it.

## Task status

| Task | Status | Evidence |
|---|---|---|
| T01 union collision scan at warn 0.50 | DONE | [collisions.json](collisions.json) (union of 1,090 skills: PASS; cross-engine ≥ 0.75: 15; cross ≥ 0.50: 155; within-engine ≥ 0.75: 16; undeclared ≥ 0.75: 0). Social-only extract with within-engine pairs: [social-pairs-ge-050.json](social-pairs-ge-050.json) |
| T02 social pairs ≥ 0.75 | DONE | **0** social cross-engine pairs at 0.75 or above (8 at the Social Kaizen baseline, all declared). Rows naming retired social skills: none left in `ownership.yaml` (the `blog-idea-generator` row was re-pointed in S03). Two declared rows now report stale social members and were annotated, not removed (see "Ownership register" below) |
| T03 within-engine pairs ≥ 0.75 | DONE | **0** social within-engine pairs at 0.75 or above (9 at baseline; all removed by the S02–S07 merges). The 16 portfolio within-engine pairs are all in other engines |
| T04 review of 0.60–0.75 pairs | DONE | Review table below: no NEW skill reaches 0.50 against anything; six merged-owner pairs each have an owned negative in both directions; three undeclared cross pairs need no action |
| T05 social engine block in `baseline.json` | DONE | `p_at_1` 94.9, `p_at_3` 100.0, owned negatives 121/121, coverage 112/112, fixtures 392, floor **92** (94.9 − 2 = 92.9, rounded down), `floor_history` first entry "social consolidation S11" with `ledger_ref` RC-018; command `python -X utf8 scripts/routing_smoke_test.py --min-rank1 92 --lint-fixtures`. `validate-routing-baseline.py`: PASS (6 engines + portfolio) |
| T06 portfolio block | DONE | Pair counts re-measured: cross ≥ 0.75 21 → 15, cross ≥ 0.50 200 → 155, within ≥ 0.75 26 → 16 (social contributes 0 to each; the totals also include other engines' edits since M10-03, stated in `pair_counts_note`). `oracle_primary_at_1` 76.9 → 79.5 after the oracle re-point. Portfolio floor **not raised** (stays 74): the gain comes from fixing stale oracles, not better routing; no `floor_history` entry appended |
| T07 behavioural routing | NOT_ASSESSED (zero-spend rule) | Stated here and in the ledger; carried to S13 |
| Extra: oracles 044 and 057 | DONE | Re-pointed from retired aliases to owners (prompts unchanged): 044 `blog-idea-generator` → `content-ideas` (rank 6 behind the three other-engine copies; stays a `later-wave` known defect), 057 `meta-social-media-roi-business-case` → `meta-roi-framework` (rank 1). Oracle primary@1 30/39 → 31/39. Ledger RC-019 |
| Extra: honest client prompts that missed | DONE | Five prompts written and frozen before any tuning; routing text tuned with client vocabulary; prompts not edited (table below) |
| Extra: fold three companion register pairs | DONE | Register 182 → 179 records (details below) |
| Extra: retired-skill links inside inactive `ALIAS.md` | NOT NEEDED | No check fails on them (validator, alias check, portable-link and pytest suites green); the aliases stay verbatim history per D-SK-03. Carried to S13 as cosmetic |
| Extra: sharpen the weakest owned negatives | DONE | 14 of the 15 weakest rewritten; one draft rejected (table below) |

## Honest prompts (tuned on routing text, never on the prompt)

The S10 hand-off named four misses but did not record the prompts, so five prompts were written in client language and frozen before looking at the routing text. They are now fixtures (`s11-*`). The before and after ranks are reproducible: [honest-prompt-ranks.txt](honest-prompt-ranks.txt) ranks the same prompts on a `git archive` of the S10 tree (`973e1af`) and on the S11 tree.

| Fixture | Owner | Rank before → after | Routing-text change |
|---|---|---|---|
| `s11-deepfake-whatsapp-scam` | `playbook-crisis-communications` | 85 → 1 | Description adds "a deepfake or impersonation scam"; a `Use When` bullet on impersonation scams (a faked clip or cloned voice note of the CEO, a copycat page, forwarded payment requests), backed by `references/synthetic-media-and-deepfake-protocol.md`. Two old bullets merged to stay within six |
| `s11-agency-audit-rights` | `playbook-agency-operations` | 17 → 1 | Description adds "team roles and certifications" and "client audits of media billing"; one `Use When` bullet on inspection of media bills, rebates and principal-media deals, and lapsing certificates. The content already existed in `references/commercial-governance-and-contracts.md` and `references/certification-and-competency-register.md` |
| `s11-agency-expiring-certifications` | `playbook-agency-operations` | 11 → 1 | Same bullet |
| `s11-podcast-downloads` | `strategy-video-content` | 3 → 1 | `Use When` bullet on honest listener numbers (what counts as a download, bot and repeat filtering); content in `references/podcast-and-audio-series.md` |
| `s11-whatsapp-split-test` (collision, `negative_for` `ad-testing-and-scaling`) | `meta-testing-framework` | 55 → 1 | Description adds "message version"; `Use When` bullet on splitting a WhatsApp broadcast, SMS or email list between two message versions with a balance check, backed by `references/trustworthy-experiments-srm-power-holdouts.md` |

All five pass the fixture lint (no slug leak; trigram overlap with the owner's routing text under 0.4). Descriptions stay within 350 characters (`validate_skill_engine.py`: 112 compliant).

## Owned negatives sharpened

S08 found that most owned negatives passed without the competitor in contention. Measured on the S10 tree (120 owned negatives): competitor in the top 3 for 26, ranks 4–10 for 30, below rank 10 for 64. Full before and after ranks: [owned-negative-ranks.txt](owned-negative-ranks.txt). The 15 weakest (competitor ranked 55–85) were rewritten so the prompt names or brushes against the competitor's job while the expected skill still owns it (for example "Our brand positioning and distinctive assets are already agreed. Before the agency writes any scripts…").

| Fixture | Competitor rank before → after | Expected rank after |
|---|---|---|
| `brand-strategy-vs-brand-voice` | 85 → 9 | 1 |
| `eac-call-for-applications-campaign-not-launch` | 83 → 2 | 1 |
| `brand-strategy-vs-creative-brief` | 82 → 2 | 1 |
| `skill-writing-not-safety-check` | 73 → 2 | 1 |
| `paid-search-advertising-not-social` | 72 → 4 | 1 |
| `traction-channel-bullseye-not-roles` | 69 → 16 | 1 |
| `meta-content-audit-not-profile-review` | 63 → 7 | 1 |
| `strategy-experiential-marketing-not-campaign` | 63 → 2 | 1 |
| `social-commerce-strategy-not-conversion` | 62 → 2 | 1 |
| `ai-slop-audit-not-drafting` | 61 → 2 | 1 |
| `playbook-crisis-communications-not-reputation` | 57 → 2 | 1 |
| `meta-social-metrics-framework-not-monthly-writeup` | 57 → 17 | 1 |
| `strategy-video-content-not-filming-skills` | 56 → 2 | 1 |
| `advertising-attribution-and-measurement-not-roi` | 54 → 4 | 1 |
| `hospitality-hotel-restaurant-not-retail-launch` | 75 → unchanged | **Rejected draft:** naming "hotel and restaurant fridges" (and a "not a hotel or restaurant" disclaimer) made the competitor win, because the lexical ranker cannot read negation. The original prompt stays; recorded in RC-018 |

After (121 owned negatives, including the new WhatsApp one): competitor in the top 3 for 36, ranks 4–10 for 34, below rank 10 for 51. All 121 pass. The remaining 51 are the S13 backlog.

**Limit (review finding 4).** About eight of the sharpened prompts carry fixture-author disclaimers ("It is a product launch, not a call for applications", "I don't need a slop score on finished text", "no crisis, nothing viral"). The expected skill is still the right owner in each, but a lexical ranker cannot read negation, so these fixtures measure resistance to the competitor's vocabulary rather than true discrimination. S13 should prefer "already agreed / settled" framing (as in `brand-strategy-vs-brand-voice`) over explicit disclaimers.

## Routing figures (social local harness, lexical proxy)

| Measure | S10 close | S11 close |
|---|---|---|
| Fixtures | 387 | 392 |
| Top-3 | 387/387 (100 %) | 392/392 (100 %) |
| p@1 | 366/387 (94.6 %) | 372/392 (94.9 %) |
| Owned negatives | 120/120 | 121/121 |
| Skills named as `expected` by a positive fixture | 112/112 | 112/112 |
| S08 independent holdout (60 prompts, never tuned on) p@1 / top-3 | 47/60 / 54/60 (re-measured on the S10 tree) | 48/60 / 54/60 |
| Registered floor | 92 (local `p1_floor`) | 92 (local) and 92 in `baseline.json` |

## Collision review (T04): pairs between 0.60 and 0.75

No NEW skill (`brand-strategy-and-distinctive-assets`, `marketing-mix-modelling`, `programmatic-and-brand-safety`, `measurement-tracking-plan`) reaches 0.50 against any skill in the union.

| Pair | Score | Scope | Decision |
|---|---|---|---|
| `proposal-skills/hospitality-hotel-restaurant` ↔ social `hospitality-hotel-restaurant` | 0.740 | cross | No action: declared `mirrored_domain_pack` |
| `chwezi-design-engine/hospitality-hotel-restaurant` ↔ social | 0.726 | cross | No action: same declared pack |
| `platform-whatsapp` ↔ `playbook-sms-whatsapp-marketing` | 0.722 | within | No action: owned negatives both ways (`platform-whatsapp-not-bulk`, `playbook-sms-whatsapp-marketing-not-whatsapp`) |
| `business-plan-skills/east-african-english` ↔ social `east-african-english` | 0.701 | cross | No action: declared `mirrored_domain_pack` |
| `07-email-marketing-strategy` ↔ `email-copywriter` | 0.685 | within | No action: owned negatives both ways |
| `chwezi-dev-engine/hospitality-hotel-restaurant-systems` ↔ social | 0.658 | cross | No action: declared pack |
| `biz-dev-positioning` ↔ `marketing-foundations-stp-positioning` | 0.652 | within | No action: owned negatives both ways |
| `paid-search-advertising` ↔ `playbook-paid-social-advertising` | 0.652 | within | No action: owned negatives both ways (one sharpened in S11) |
| `business-plan-skills/hospitality-hotel-restaurant` ↔ social | 0.649 | cross | No action: declared pack |
| `proposal-skills/east-african-english` ↔ social | 0.645 | cross | No action: declared pack |
| social `french-native-copy` ↔ `website-skills/french-native-copy` | 0.630 | cross | No action: undeclared but below 0.75; each copy serves its own artefact (posts and ads vs website pages). Declare if it ever crosses 0.75 |
| `business-plan-skills/east-african-english` ↔ social `language-standards` | 0.629 | cross | No action: below 0.75; the social skill is the cross-language policy, not an English register |
| `ai-generative-search-optimisation` ↔ `seo-geo-optimisation` | 0.628 | within | No action: owned negatives both ways |
| `chwezi-dev-engine/ai-prompt-engineering` ↔ social `prompt-engineering-library` | 0.620 | cross | No action: below 0.75; dev owns prompt engineering for software, social owns the marketing prompt library |
| `strategy-video-content` ↔ `training-smartphone-video-production` | 0.614 | within | No action: owned negatives both ways (one sharpened in S11) |

## Ownership register (`chwezi-engine-agents/evals/routing/ownership.yaml`)

- **Blog-ideation row** (owner `social-media-skills/content-ideas`): the S11 scan reports its three social pairs as stale (below 0.50). Kept and annotated: the row names the owner while the business-plan, proposal and website copies still collide at 0.76–0.83. Oracle 044 is recorded against the new owner.
- **East African English row:** social ↔ website now 0.58 (reported stale below 0.60); kept, annotated with the S11 scores (0.70, 0.64, 0.58), because the pack is mirrored by design.
- No new rows: no social pair reaches 0.75.

## Register fold (three companion pairs, S10 review finding 9)

| Surviving record | Folded record | Citations re-pointed |
|---|---|---|
| `IAB-AI-DISCLOSURE-V2-2026` (verified, 42-page PDF) | `IAB-AI-DISCLOSURE-2026` (v1 landing page, partial) | `ai-transparency-and-provenance.md` (2) |
| `ICC-CODE-2024-TEXT` (full code text, verified) | `PREMIUM-ICC-2026` (landing page) | `06-digital-marketing-strategy`, `policy-ai-content-ethics` and three of its references, the influencer term-sheet reference (8) |
| `INSTAGRAM-HASHTAG-LIMIT-PRIMARY` (@creators statement, verified) | `INSTAGRAM-HASHTAG-LIMIT-2025` (Social Media Today, partial) | caption-writer hashtag reference, brand style guide, Instagram growth reference (2), prompt-writing module, DIY content handbook (2) |

Each survivor gains a `folded_ids` field, the folded record's title, publisher, URL, date and status in its `verification_note`, and the folded record's uses in `use_for`. Each folded record's tier and review cadence are kept in the survivor's note. The ICC survivor's `use_for` and `uncertainty` now state that its responsibility-section and Art. 5 uses were cited to the landing-page record without a recorded check of those sections and are `NOT_ASSESSED`; `ai-transparency-and-provenance.md` §2 says the same where it cites them. This was already thin before S11 (not a regression). Historical evidence and preservation maps keep the old IDs as history. `check_source_freshness.py`: PASS (179 records).

## Gate block

[gate-block-2026-09-29.txt](gate-block-2026-09-29.txt): validator 112/112, 0 failures; routing 392/392 top-3, p@1 94.9 %, owned negatives 121/121, lint 0; aliases 83 routes, 0 findings, cap 120; pytest 68 passed; unittest OK; freshness PASS (179); ingestion guardrail 0; scaffolding gated median 1.4 %, 0 files over 300; `git diff --check` clean. Coordination package: render check 0 findings (social; also 12 repositories with the full workspace root); marketplace 23 ok, 0 drift; collisions PASS, 0 undeclared ≥ 0.75; routing ratchet PASS (6 engines + portfolio); book-extraction check 0 findings; chwezi-engine-agents pytest 162 passed.

## Cross-engine change (`chwezi-engine-agents`)

- `evals/routing/baseline.json`: social engine block; portfolio pair counts, `oracle_primary_at_1` and `pair_counts_note`.
- `evals/routing/ownership.yaml`: S11 notes on the blog-ideation and East African English rows.
- `evals/routing/rejected-changes.md`: RC-018 (social S11 routing changes, including the rejected sharpening draft) and RC-019 (oracle re-point).
- `evals/cases/044-route-blog-ideas.yaml`, `evals/cases/057-route-social-roi-mirror.yaml` and their `evals/fixtures/*/expected.yaml` and `task.md`.

## Open items

- 51 owned negatives still have the competitor below rank 10 (S13 backlog).
- Oracle 044 stays a later-wave known defect until the business-plan, proposal and website blog-idea copies become aliases (other engines; out of scope).
- Portfolio floor left at 74 although oracle primary@1 now measures 79.5: raising it is a portfolio decision for the orchestrator.
- Retired-skill names inside inactive `ALIAS.md` files: cosmetic, S13.

## Reviewer verdict

Independent review (general-purpose agent, 29 Sep 2026): **ACCEPT_WITH_DOCUMENTED_LIMITATIONS**, no blocking finding, five minor findings. Every figure it could rerun matched (routing 392/392, p@1 94.9 %, owned negatives 121/121, collisions 15 / 155 / 0 undeclared, ratchet PASS, oracles 31/39 = 79.5 %, validator 112/112).

| # | Finding | Disposition |
|---|---|---|
| 1 | ICC fold implied a check of the responsibility section and Art. 5 that never happened | Fixed: `use_for` and `uncertainty` mark those uses `NOT_ASSESSED`; the citing reference says so |
| 2 | Folded records' tier and review cadence lost | Fixed: kept in each survivor's `verification_note` |
| 3 | Testing bullet went beyond its reference and echoed the prompt; crisis bullet opened like its prompt | Fixed: both bullets reworded (split-list test with a balance check; "Impersonation scams: …"); all five prompts still rank 1 |
| 4 | Some sharpened negatives use fixture-author disclaimers | Recorded as a limit above; S13 guidance given |
| 5 | "Frozen before tuning" had no artefact; agency bullet mixed "them"/"our" | Fixed: reproducible before/after rank files stored; bullet reworded |

Carried limits: portfolio floor stays 74 against a measured 79.5; oracle 044 stays a later-wave known defect (rank 6); 51 owned negatives with the competitor below rank 10; Tier 3 behavioural routing `NOT_ASSESSED (zero-spend rule)`.

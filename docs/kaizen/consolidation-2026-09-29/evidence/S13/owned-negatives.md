# S13 owned-negative sharpening (S11 carry-forward)

- **Date:** 29 September 2026. Tree: `e7d68fd` (S12) plus this change to `tests/routing-fixtures.json` (prompt text only; ids, `expected` and `negative_for` unchanged; no `SKILL.md` routing text touched).
- **Scope:** the 51 owned negatives whose competitor (`negative_for`) ranked below 10 after S11, so they measured little discrimination.
- **Method:** each prompt was rewritten so it brushes against the competitor's job and vocabulary (read from the competitor's description and `Use When`) while the expected skill stays the genuine owner. The S11 finding-4 guidance was followed: "already agreed / settled / signed off / can wait" framing, not fixture-author disclaimers such as "this is not an X". Every candidate was checked with the engine's own `catalogue()` / `rank()` (scratch script `try_negs.py`) for: expected in the top 3, expected ranked above the competitor, and no `--lint-fixtures` leak (slug phrase or trigram copy of routing text). Ranks are a lexical proxy, not live routing.
- **Full rank lists:** [owned-negative-ranks.txt](owned-negative-ranks.txt) (before and after, all 121 owned negatives).

## Result

| Competitor band (121 owned negatives) | Before (S12) | After (S13) |
|---|---|---|
| Competitor in the top 3 | 36 | **73** |
| Competitor at ranks 4–10 | 34 | **47** |
| Competitor below rank 10 | 51 | **1** |
| Owned negatives passing | 121 / 121 | 121 / 121 |

Smoke test after: `routing fixtures=392 passed=392 top_3_precision=1.000`; `precision@1=373/392 (95.2%)` (was 372/392, 94.9 %; `meta-content-repurposing-not-performance-review` moved from expected rank 2 to 1); `owned negatives=121 passed=121`; `fixture lint: 0 finding(s)`. S08 holdout unchanged: 48/60 p@1, 54/60 top-3.

## Changed fixtures (50)

| Fixture | Competitor rank before → after | Expected rank before → after |
|---|---|---|
| `hospitality-hotel-restaurant-not-retail-launch` | 75 → 3 | 1 → 1 |
| `strategy-creator-monetisation-not-reputation` | 53 → 3 | 1 → 1 |
| `meta-reporting-not-kpi-choice` | 51 → 2 | 1 → 1 |
| `training-social-media-fundamentals-not-handover` | 48 → 5 | 1 → 1 |
| `premium-commercial-writing-not-funnel` | 48 → 2 | 1 → 1 |
| `playbook-client-retainer-management-not-b2b` | 48 → 7 | 1 → 1 |
| `meta-competitor-analysis-not-own-profiles` | 47 → 9 | 1 → 1 |
| `meta-social-listening-not-complaint-response` | 46 → 2 | 1 → 1 |
| `04-brand-voice-intake-not-distinct` | 45 → 2 | 1 → 1 |
| `playbook-community-management-not-reputation` | 44 → 2 | 1 → 1 |
| `meta-sales-marketing-alignment-not-prospecting` | 39 → 9 | 1 → 1 |
| `playbook-marketing-automation-not-chatbot` | 37 → 8 | 1 → 1 |
| `strategy-personal-brand-not-practice` | 34 → 3 | 1 → 1 |
| `03-audience-personas-not-stp` | 29 → 3 | 1 → 1 |
| `platform-facebook-not-ads` | 28 → 2 | 1 → 1 |
| `marketing-mix-modelling-not-ad-credit` | 28 → 3 | 1 → 1 |
| `blog-writer-not-ideas` | 27 → 3 | 1 → 1 |
| `09-campaign-strategy-not-handover` | 27 → 3 | 1 → 1 |
| `media-planning-not-total-budget` | 23 → 3 | 1 → 1 |
| `06-digital-marketing-strategy-not-social` | 23 → 2 | 1 → 1 |
| `training-client-team-not-beginners` | 21 → 2 | 1 → 1 |
| `playbook-agency-operations-not-retainer` | 21 → 2 | 1 → 1 |
| `marketing-foundations-stp-positioning-not-agency` | 21 → 9 | 1 → 1 |
| `seo-geo-optimisation-not-brand-programme` | 20 → 2 | 1 → 1 |
| `playbook-chatbot-strategy-not-whatsapp` | 20 → 2 | 1 → 1 |
| `11-content-calendar-not-workflow` | 20 → 2 | 1 → 1 |
| `strategy-ewom-reviews-not-complaints` | 19 → 2 | 1 → 1 |
| `skill-safety-audit-not-authoring` | 19 → 2 | 1 → 1 |
| `biz-dev-credentials-not-proposal` | 19 → 2 | 1 → 1 |
| `playbook-post-click-strategy-not-handoff` | 18 → 3 | 1 → 1 |
| `biz-dev-proposal-not-credentials` | 18 → 4 | 1 → 1 |
| `ad-testing-and-scaling-not-stats` | 18 → 5 | 1 → 1 |
| `05-social-media-strategy-not-digital` | 18 → 5 | 1 → 1 |
| `02-platform-audit-not-rivals` | 18 → 3 | 1 → 1 |
| `demand-forecasting-not-marketing-split` | 18 → 4 | 1 → 1 |
| `meta-content-repurposing-not-performance-review` | 17 → 3 | 2 → 1 |
| `programmatic-and-brand-safety-not-plan` | 17 → 3 | 1 → 1 |
| `meta-social-metrics-framework-not-monthly-writeup` | 17 → 3 | 1 → 1 |
| `direct-response-economics-not-attribution` | 17 → 3 | 1 → 1 |
| `biz-dev-lawful-prospecting-outreach-not-advocacy` | 17 → 3 | 1 → 1 |
| `measurement-tracking-plan-not-credit-model` | 17 → 4 | 3 → 3 |
| `traction-channel-bullseye-not-roles` | 16 → 4 | 1 → 1 |
| `01-client-brief-not-handover` | 16 → 2 | 1 → 1 |
| `prompt-engineering-library-not-training` | 15 → 2 | 1 → 1 |
| `media-planning-not-programmatic` | 15 → 3 | 1 → 1 |
| `ecommerce-export-marketing-advisory-not-local-shop` | 15 → 4 | 1 → 1 |
| `content-ideas-not-calendar` | 13 → 2 | 1 → 1 |
| `advertising-attribution-and-measurement-not-mmm` | 13 → 3 | 1 → 1 |
| `programmatic-vs-media-plan-screens` | 13 → 2 | 1 → 1 |
| `brand-voice-ai-training-not-intake` | 12 → 3 | 1 → 1 |
## Left unchanged (1)

| Fixture | Reason |
|---|---|
| `kaizen-improvement-system-not-single-draft` (`anti-ai-slop` vs `kaizen-improvement-system`) | The expected skill already ranks only 3rd on the current prompt. Every honest wording that brought in the competitor's vocabulary (review, content system, campaign) pushed `anti-ai-slop` out of the top 3 (ranks 6–11) or put the competitor first. Tuning `anti-ai-slop` routing text is out of scope, so the prompt stays and the weakness is recorded for the next routing pass. |

## Honesty notes

- Some rewrites state a real client fact that settles the neighbouring job, for example "it bundles no third-party scripts or installers" (`skill-safety-audit-not-authoring`) or "brand deals, rate cards and sponsorships are off the table" (`strategy-creator-monetisation-not-reputation`). These are client circumstances, not instructions to the router, but a lexical ranker cannot read negation. The fixtures therefore still measure resistance to the competitor's vocabulary rather than semantic discrimination; live routing stays `NOT_ASSESSED (zero-spend rule)`.
- Expected ranks: 48 of the 50 changed fixtures keep the expected skill at rank 1; `measurement-tracking-plan-not-credit-model` keeps it at rank 3, as before the change. One fixture improved (`meta-content-repurposing-not-performance-review`, 2 → 1).

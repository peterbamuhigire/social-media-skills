---
name: 02-platform-audit
description: Use when a client's social profiles need reviewing before strategy, a free audit is offered to win a prospect, or bios, covers, handles and links need fixing; produces the scored platform audit, rival benchmark and prioritised quick wins; not for a deep study of rivals' content and positioning (use `meta-competitor-analysis`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Platform Audit Generator

Scores each of the client's social profiles, benchmarks them against three named competitors and sets ten first-week quick wins plus a 6-slide deck outline, from public profile data and the completed client brief. Apply the `east-african-english` skill for tone throughout.

<!-- dual-compat-start -->
## Use When

- We need to know how complete, active and on-brand each of the client's social profiles is before we write strategy.
- The client wants a side-by-side benchmark of their pages against two or three named competitors, with estimates flagged.
- The agency wants to offer a prospect a free 30-minute social audit as a lead offer, scored across five areas out of 50, with a wins-and-gaps one-pager and a path to a paid retainer.
- Every profile needs tidying: bio rewrites using WHO-WHAT-WHO-CTA, cover images, handles, link in bio and the WhatsApp button, on a 48-hour, one-week and one-month fix plan.

## Do Not Use When

- `meta-competitor-analysis` for a deeper study of rivals' content, messaging and positioning gaps.
- `meta-content-audit` for a keep, stop or test review of the client's own past posts.
- `01-client-brief` when the client has not yet completed intake.
- Stop before logging into, editing or publishing to a live profile without the client's written permission; deliver the fix list for approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry and completed `01-client-brief` | `01-client-brief` output | Yes (brief as context if available) | Note the brief gaps in the audit; route to `01-client-brief` when intake has not started. |
| Active platforms with the exact handle or URL for each | Client brief or client | Yes | Search public profiles and confirm each handle with the client before scoring. |
| Three named competitors with handles on each relevant platform | Client | Yes | Ask for them before proceeding; the competitive benchmarking section cannot be completed without them. |
| Native insights, Meta Business Suite or Google Analytics access | Client | Optional | Estimate engagement with the formula below and label it *(estimated — no account access)*. |
| Country / city | Client brief | Yes | Default to Kampala, Uganda. |

## Workflow

1. Confirm the audit type: a paid pre-strategy audit, or a free lead-offer audit for an unsigned prospect (route to [audit-as-lead-offer](references/audit-as-lead-offer.md)); stop and ask for competitor handles if they are missing.
2. Collect data from the listed sources (manual profile review, Meta Ad Library, native insights, SimilarWeb free tier, Google Analytics / Meta Business Suite) and note the source against each data point.
3. Fill one audit table per active platform; score profile completeness (1–10) and content quality (1–10) with the scoring guides, and justify every score with a specific observation.
4. Build one competitive benchmarking table per major platform, followed by the three-point commentary: where the client leads, where the client lags, visible gap to exploit.
5. Write exactly 10 quick wins for the first week, sequenced from easiest/fastest to more involved and covering all four categories; for element-level fixes use [profile-optimisation-fixes](references/profile-optimisation-fixes.md).
6. Write the 6-slide deck outline with Headline, Bullets, Speaker Notes and Visual Direction for every slide.
7. Check every estimate is labelled and every score is evidenced; correct any unlabelled estimate or unsupported score and rerun the affected table and slide before hand-off.
8. Run the anti-slop ship gate and hand the audit to the strategy skills (`05-social-media-strategy`); deliver profile fixes as an approval list, never as live edits.

## Scoring bands and engagement formula

- **Estimated engagement rate = (total likes + comments on last 10 posts) ÷ (follower count × 10) × 100**; label all estimates *(estimated — no account access)*.
- Profile completeness (one point per element, ten elements): 7–10 = strong; 4–6 = needs attention; below 4 = significant gaps.
- Content quality (five dimensions, 2 points each): 8–10 = strong; 5–7 = developing; below 5 = requires urgent improvement.
- Full scoring guides, table layouts and the deck template: [audit-method-and-presentation-outline](references/audit-method-and-presentation-outline.md).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Platform audit tables (one per active platform) | Client lead; `05-social-media-strategy` | Every active platform has a completed table or a stated reason for skipping; scores carry observations. |
| Competitive benchmarking tables with three-point commentary | Client lead; strategy skills | At least one concrete gap the client can exploit is named. |
| Quick wins list | Client; account team | Exactly 10 items, each with action, platform(s), effort, impact and category; all four categories covered. |
| 6-slide deck outline | Client presentation | All four fields completed for every slide. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Data-source notes per data point | Source column or note beside each figure, with review date | No claim is presented as measured fact unless account access was provided. |
| Engagement-rate calculation record | Formula, inputs (last 10 posts, follower count) and result | Every estimate labelled and reproducible. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. The audit is read-only by default: inspect and report without changing profiles, accounts or campaigns, and do not log into or edit a live profile without the client's written permission.

## Degraded Mode

Without account access or competitor handles, return the narrowest qualified result and mark the affected checks `not assessed`. Public-profile audit tables with labelled engagement estimates can still be delivered; the benchmark waits for the handles.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The prospect has not signed and the audit is a free lead offer | Run the five-area, 30-minute audit and findings one-pager in [audit-as-lead-offer](references/audit-as-lead-offer.md), then hand over to `biz-dev-proposal`. | Giving the full paid audit away, or a pitch with no scripted route to paid work. |
| Profile-completeness gaps need element-level fixes and paste-ready bios | Apply the platform checklists and three-tier plan in [profile-optimisation-fixes](references/profile-optimisation-fixes.md). | Vague "improve your bio" advice and arbitrary priorities. |
| No account access is available | Use the estimated engagement formula and label each figure *(estimated — no account access)*. | Presenting inferred data as measured fact. |
| Competitor handles are missing | Ask for them before proceeding; do not guess handles. | A benchmark against the wrong accounts. |
| The client is not active on a minor platform | Combine minor platforms into a single summary row in the benchmark. | Padding the benchmark with empty tables. |
| Competitor data comes only from public profiles and Meta Ad Library | Treat follower counts and engagement as point-in-time observations; do not infer strategy or revenue from public data alone. | Unfounded claims about rivals. |
| The requested outcome is a keep/stop/test review of past posts | Route to `meta-content-audit` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- Every active platform has a completed audit table; no platform is skipped without an explanation.
- Profile completeness and content quality scores are justified with specific observations, not assigned without evidence.
- Competitor benchmarking identifies at least one concrete gap the client can exploit, not a generic observation.
- Quick wins list contains exactly 10 items, sequenced by effort and impact, covering all four categories.
- Deck outline follows the exact format from CLAUDE.md with all five fields (Headline, Bullets, Speaker Notes, Visual Direction) completed for every slide.
- Estimated engagement rates are clearly labelled as estimates; the calculation method is documented.
- Data sources are noted throughout; no claim is presented as measured fact unless account access was provided.
- British English spelling throughout; tone follows the `east-african-english` skill.

## Anti-Patterns

- Presenting estimated engagement as measured fact. Fix: label it *(estimated — no account access)* and document the formula.
- Scoring profiles without observations. Fix: list the missing elements and the specific content notes behind each score.
- Treating follower count as the headline result. Fix: note it is a vanity metric and compare engagement and content quality (Bodnar and Cohen, 2012).
- Generic quick wins ("post more"). Fix: tie each to a platform, effort, impact and category, and use peak Uganda/EA times where posting rhythm is the gap.
- Editing a client's live profile during the audit. Fix: deliver the fix list for approval; editing needs written permission.
- Absorbing a deep competitor content study or a past-post review. Fix: route to `meta-competitor-analysis` or `meta-content-audit`.

## References

- [Audit method, scoring guides and deck outline](references/audit-method-and-presentation-outline.md): read when collecting inputs, choosing data sources, filling the audit and benchmark tables, scoring, writing quick wins or drafting the six slides.
- [audit-as-lead-offer](references/audit-as-lead-offer.md): read when a free audit is used to win a prospect before any brief exists.
- [proposal-frameworks](references/proposal-frameworks.md): read when writing the audit offer or findings persuasively (NOSE, Primacy Principle, Go/No-Go).
- [profile-optimisation-fixes](references/profile-optimisation-fixes.md): read when profile gaps need a per-platform checklist, bio rewrites and a prioritised fix plan.
- [`meta-content-audit`](../../meta-analytics-ops/meta-content-audit/SKILL.md): read when the job is a review of the client's own past posts.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

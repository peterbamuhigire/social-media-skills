---
name: strategy-customer-value-journey
description: Use when followers never become buyers or repeat customers and posts need mapping to each stage from first awareness to purchase, return and referral; produces the customer value journey map with entry offers and stage metrics; not for the brand's standing themes (use `10-content-pillars`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Customer Value Journey Strategy

Maps a client's social content onto the eight-stage Customer Value Journey (Deiss / DigitalMarketer) so East African SMEs move people from first sight to referral, with WhatsApp as the main Subscribe and Convert channel.

<!-- dual-compat-start -->
## Use When

- We get likes and followers but few enquiries, sign-ups or sales.
- We need a lead magnet or low-price entry offer and a path to bigger purchases (ascension offers).
- Customers buy once and disappear; we need retention and referral content.
- Map where WhatsApp, email and social each sit in the funnel from awareness to advocacy, including an experience map or user journey.
- Audit current content by funnel stage, fill the gaps and set a measure for each stage.

## Do Not Use When

- `10-content-pillars` for the three to five recurring themes content returns to.
- `11-content-calendar` for scheduling approved content across 90 days.
- `strategy-ewom-reviews` for review, testimonial and referral programmes.
- Stop when there is no offer or sales data to map against; return the intake gap instead of inventing stages.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry/sector, country/city and primary goal (sales, WhatsApp list growth, repeat purchases) | Client | Yes | Default to Uganda / Kampala; ask for the goal before choosing where to weight content. |
| Current platforms, approximate followers and the last 30 posts | Client; platform pages | Yes | Mark the stage distribution `not assessed` and classify the failure mode from the client's description only, labelled provisional. |
| Existing entry-point and ascension offers | Client | Yes | Design both, labelled as proposals for client pricing sign-off. |
| Approximate customer lifetime value | Client sales records | Yes | Keep the entry-point offer free or low-cost and flag the calibration as unassessed. |
| Offer or sales data to map against | Client | Yes | Stop and return the intake gap instead of inventing stages. |
| Existing mechanisms: WhatsApp opt-in, post-purchase welcome, referral tracking | Client | If any | Treat each as absent (No) in the mechanism audit. |

## Workflow

1. Confirm the request is a full-funnel journey plan, not pillar themes (`10-content-pillars`) or a review programme (`strategy-ewom-reviews`); run the intake questions in the [CVJ method](references/cvj-method.md).
2. Audit the last 30 posts: categorise each by CVJ stage, express the distribution as percentages and flag stages at 0 % or under 10 %; stop when there is no offer or sales data to map against.
3. Run the mechanism audit (Subscribe opt-in, Convert offer, Excite welcome sequence, Promote referral) and classify the client as Failure Mode 1 (all promotional), Failure Mode 2 (all awareness) or Mixed.
4. Design or confirm the entry-point offer (Stage 4) and the ascension offer (Stage 6), with ascension pitched only after Excite is confirmed.
5. Set the content share by journey zone, adjusting it to the audit with a stated rationale, then for each gap stage write three to five industry-specific content ideas, the platform and format, the CTA to the next stage and the WhatsApp integration point.
6. Design the referral loop (enable Advocate, activate Promote) and map primary, secondary and vanity metrics to each stage; use the [experience map layout](references/experience-map-and-journey-layout.md) when the client needs the journey drawn.
7. Check every stage has two to three touchpoints before its CTA advances the customer; correct any single-post Aware-to-Convert jump and rerun the check, then run the anti-slop gate and hand over.

## Content share by journey zone

Starting ratio; adjust to audit results (large Aware/Engage deficit → weight the top; low conversion → weight Convert and Excite).

| Journey Zone | Stages | Recommended Content Share |
|---|---|---|
| Top of journey | Aware + Engage | 40% |
| Opt-in | Subscribe | 15% |
| Conversion | Convert | 15% |
| Retention and growth | Excite + Ascend | 20% |
| Referral | Advocate + Promote | 10% |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| CVJ audit: stage distribution, mechanism audit and failure-mode classification | Client lead | Based on the last 30 posts, with 0 % and under-10 % stages named. |
| CVJ content plan by stage with content ideas, platform, format, CTA and WhatsApp point | Content team; `11-content-calendar` | Three to five industry-specific ideas per gap stage; ratio deviations explained. |
| Entry-point and ascension offer outlines and WhatsApp message outlines | Client lead; sales owner | Ascension follows Excite; message outlines only, no automation. |
| Referral loop design and stage metric map | Client lead; analytics owner | Incentivised Promote steps with source tracking; each stage names its vanity-metric trap. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| 30-post stage inventory | Table: post, platform, stage | Every post has one stage and the percentages sum to 100. |
| Mechanism audit | Yes/No table per mechanism | Each answer is observed on the live profile or marked `not assessed`. |
| Offer and lifetime-value assumptions | Register | Each price or CLV figure names its source or is labelled an assumption. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. WhatsApp broadcast management (scheduling, list hygiene, automation tools) is out of scope; this skill produces the content strategy and message outlines only.

## Degraded Mode

Without the client's recent posts and offer or sales data, return the narrowest qualified result and mark the affected checks `not assessed`. The eight-stage map, a provisional failure-mode diagnosis and offer and referral outlines can still be delivered for client confirmation.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Content is concentrated at one funnel stage | Map the missing stage, CTA, channel, and metric before adding volume. | More posts reproduce the same funnel gap. |
| The client posts discounts, product shots and price lists only (Failure Mode 1) | Add Aware and Engage content that builds trust before any ask. | Every post asking for money before trust is established. |
| Engagement looks healthy but sales do not follow (Failure Mode 2) | Add a Subscribe mechanism (WhatsApp opt-in) and a Convert offer. | An audience that consumes content and moves on. |
| A first-time buyer has not yet had a positive experience | Hold the ascension offer until Stage 5 (Excite) is confirmed. | Buyer's remorse and lost Ascend and Advocate potential. |
| The customer arrives as a warm referral (Stage 8 — Promote) | Let them enter at Subscribe or Convert directly. | Needless nurture delaying a ready buyer. |
| A stage is measured by a vanity metric (for example likes as a measure of conversion) | Replace it with the stage's primary metric from the metric map. | Reporting activity as progress. |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source. | Confident advice built on an unresolved premise. |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist. | Unauthorised publication, spend, outreach, or data use. |

## Quality Standards

- Correctly attributes the CVJ framework to Ryan Deiss / DigitalMarketer and does not conflate it with the RACE framework or other funnel models.
- Diagnoses the failure mode before prescribing content — the plan is specific to whether the client is over-indexed on promotional or awareness content, or has specific stage gaps.
- Integrates WhatsApp as a primary channel at Subscribe, Convert, and Excite stages, not as an optional add-on; reflects the EA market reality.
- Provides actionable content ideas for each gap stage, matched to the client's industry and platform mix — not generic descriptions of content types.
- Includes a referral mechanism with specific, incentivised steps for Advocate and Promote stages; does not treat referrals as organic and unmanageable.
- Maps metrics to stages correctly and explicitly identifies which metrics are vanity metrics at the wrong stage (e.g. likes as a measure of conversion).
- Respects the content ratio as a starting point and adjusts it to the client's audit results with a clear rationale for any deviation.
- Stays within scope — this skill produces content strategy and message outlines; it does not produce graphic design briefs, paid ad campaign structures, or WhatsApp automation code.

## Anti-Patterns

- Treating social media as a single-stage activity. Fix: map content across all eight CVJ stages.
- A cheap-feeling entry-point offer. Fix: make it deliver genuine value so Excite happens naturally.
- Replying to WhatsApp enquiries after hours or days. Fix: respond within two hours; send the post-purchase welcome within 24 hours and follow up at Day 3 and Day 7.
- Asking for testimonials weeks after the result. Fix: ask at the moment of highest satisfaction and give a forwardable WhatsApp message.
- Assuming customers will refer without being asked. Fix: announce the referral programme clearly and repeatedly, with a monthly WhatsApp reminder.
- Inventing a client metric, price or offer. Fix: verify it or label the decision provisional.

## References

- [CVJ method](references/cvj-method.md): read when running the intake, explaining the eight stages, designing offers, mapping content and WhatsApp to stages, running the audit, building the plan, designing the referral loop, choosing stage metrics or citing the sources.
- [Experience map and journey layout](references/experience-map-and-journey-layout.md): read when mapping scope level, experience phases, a user journey or the suspect-to-reference funnel matrix.
- [Book-driven campaign learning and retention](../../meta-utility/references/book-driven-campaign-learning-and-retention.md): read when applying the durable synthesis and the current platform-policy gate.
- [`strategy-ewom-reviews`](../strategy-ewom-reviews/SKILL.md): read when the Advocate and Promote stages need a full review, testimonial or referral programme.
- [AGENTS.md](../../../AGENTS.md): read when routing to a neighbour skill or engine.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting content ideas and WhatsApp message outlines.
<!-- dual-compat-end -->

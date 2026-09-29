---
name: hospitality-hotel-restaurant
description: Use when a hotel, lodge, resort, guest house, restaurant, bar, café, venue or caterer needs social content, campaigns, review replies or more direct bookings; produces the hospitality social plan with guest-journey pillars, review playbook and booking measurement; not for a campaign for a non-hospitality brand (use `09-campaign-strategy`).
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Hospitality Hotel And Restaurant Social
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

A commercial operating overlay for hotels, lodges, restaurants, venues and caterers, routed through the strategy, audience, campaign, content calendar, platform, website-content, analytics, review and anti-slop skills. It does not create permission to publish, spend, contact guests, or use their likeness.

<!-- dual-compat-start -->
## Use When

- A hotel, lodge or guest house wants more direct bookings and fewer OTA commissions from social and WhatsApp.
- A restaurant, bar or café needs posts about menus, food, events and offers that drive reservations or orders.
- A venue or caterer is selling weddings, meetings or conference packages online.
- Guest reviews on Google, TripAdvisor or booking sites need replies and a reputation routine.
- Menus, prices, location and policies must match across the website, Google Business Profile and social profiles.

## Do Not Use When

- `09-campaign-strategy` for a single launch or offer campaign for a brand outside hospitality.
- `platform-google-business-profile` for setting up or fixing the listing itself.
- `strategy-ewom-reviews` for a review-generation or referral programme outside hospitality.
- Stop before posting guest photos or UGC without documented rights, or quoting prices and availability the operator has not confirmed.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business type, demand occasion, primary outcome, audience, offer and dates | Client brief or approved records | Yes | Stop the affected decision and log a gap. |
| Owned destination and staffed response path (booking engine, reservation line, WhatsApp, menu/order page) with agreed response SLA | Operator | Yes | Plan awareness content only and mark conversion `NOT_ASSESSED`. |
| Current property/outlet facts: menus, prices, location, policies, availability | Operator; website as canonical source | Conditional | Mark claims `NOT_ASSESSED`; never quote prices or availability the operator has not confirmed. |
| Media rights and consent for guest photos, UGC, children and staff | Operator's rights register | Conditional | Exclude the asset or obtain permission. |
| Channels, budget and permissions | Owner | Conditional | Deliver an organic plan; spend stays a separate approved action. |
| Booking, reservation, POS, PMS or CRM data | Operator systems | Conditional | Report platform metrics as diagnostics and mark attribution `NOT_ASSESSED`. |

## Workflow

1. Classify the business and demand occasion (accommodation, leisure/resort, business travel, dining, delivery, celebration, meetings/events, catering, local community or recruitment) and map the guest journey: Discover, Trust, Choose, Act, Experience and return.
2. Set one primary business outcome per campaign and connect it to a staffed owned destination.
3. Build pillars, formats, rights, moderation, escalation and measurement from the [hospitality social method](references/hospitality-social-method.md).
4. Check that entity facts, location, contact, policies and offer conditions match across website, Google Business Profile, social profiles, OTA/partner pages and messaging.
5. Verify current platform/legal/offer facts against the source register and run the anti-slop review; correct any unverified claim and rerun the check.
6. Produce the approved plan; stop on material rights/safety/evidence gaps and recover by narrowing the campaign; publishing and spend remain separate actions.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Hospitality social strategy with guest-journey pillars and campaign/calendar inputs | Owner and content team | Objective, audience, offer, rights and staffed destination are explicit for every campaign. |
| Reputation playbook (review replies, escalation routes) | Operator and front-of-house | Every material review gets empathy, facts and an owner; escalation categories named. |
| Measurement plan with UTM/offer map | Owner and analyst | Qualified actions reconciled with booking, reservation, POS or CRM evidence; attribution gaps marked. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Source, approval and rights register | Table: claim or asset, source, approval, expiry, usage period | Claims, permissions and unresolved checks are visible. |
| Platform check and entity-fact consistency record | Checklist across website, GBP, social, OTA pages and messaging | Every mismatch listed with an owner. |
| Escalation record | Log of safety, privacy and complaint escalations | Each escalated matter has an accountable operator. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Messaging guests, using guest data or likeness and contracting creators need the same explicit approval.

## Degraded Mode

Without verified account, offer, rights, platform, audience or conversion data, return the narrowest qualified result and mark the affected checks `not assessed`. A qualified strategy with guest-journey pillars and an evidence request can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Offer and destination are verified | Build the campaign. | Broken fulfilment. |
| Guest media rights are missing | Exclude or obtain permission. | Rights breach. |
| Safety/privacy complaint appears (food safety, injury, discrimination, security, payment, privacy, allegation, crisis or regulator matter) | Escalate privately to the accountable operator and preserve the incident path. | Harmful public response. |
| A material review arrives | Reply with empathy, facts and an owner; move private data and unresolved complaints to a secure channel. | Public argument and exposed guest identity. |
| A price, availability or booking term is volatile | Point to the website as the canonical source. | Stale prices across social and OTA pages. |
| A sponsorship, creator partnership or gifted stay is posted | Label it and retain rights and usage period for every asset. | Undisclosed endorsement. |
| Someone proposes boosting AI or search visibility with forum mentions, reviews, followers or "citations" | Refuse; optimise profile completeness, consistent entity facts, captions, alt text and searchable menus/FAQs instead. | Manufactured consensus and platform penalties. |

## Quality Standards

- Specific: each asset serves a guest job and one clear CTA.
- Accessible: captions/transcripts, descriptive alt text and accessible video.
- Culturally fit and rights-safe: no guest, child or staff content without documented consent.
- Platform-aware: cadence and posting times treated as experiments, not universal truths.
- Evidence-led: no invented scarcity, awards, reviews, hygiene claims or influencer results.
- Measured against qualified actions rather than reach alone; platform-reported metrics kept separate from verified booking/POS/PMS outcomes.

## Anti-Patterns

- Posting attractive rooms or dishes without an occasion, proof or next action. Fix: connect each asset to a guest job and staffed destination.
- Inventing scarcity, awards, reviews, hygiene claims or influencer results. Fix: require source, approval and expiry.
- Reposting guest photos or staff stories without documented rights. Fix: obtain consent and record usage boundaries.
- Treating reach as revenue. Fix: reconcile qualified actions and fulfilment with booking, reservation, POS or CRM evidence.
- Responding to a food-safety, privacy or injury complaint as ordinary content. Fix: escalate privately to the accountable operator and preserve the incident path.
- Making medical or allergen guarantees, or promising an outcome the property cannot deliver. Fix: state exact conditions and route dietary questions to staff.

## References

- [Hospitality social method](references/hospitality-social-method.md): read when classifying the business and guest journey, choosing content pillars, working on search and AI discoverability, setting reputation rules, measuring or planning a restaurant launch.
- [Social source-register rules](../../../docs/source-registers/README.md): read when verifying platform, legal or offer facts.
- [Digital Research source evaluation](https://github.com/peterbamuhigire/digital-research-skills/blob/main/skills/source-evaluation/SKILL.md): read when a current fact needs source evaluation.
- [`platform-google-business-profile`](../../platforms/platform-google-business-profile/SKILL.md): read when the listing itself needs setting up or fixing.
- [`strategy-ewom-reviews`](../../strategy/strategy-ewom-reviews/SKILL.md): read when a review-generation or referral programme is needed.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting captions and review replies.
<!-- dual-compat-end -->

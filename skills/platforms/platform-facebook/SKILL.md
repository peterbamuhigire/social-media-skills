---
name: platform-facebook
description: Use when a business wants Facebook to bring real enquiries rather than empty likes, across its Page, Facebook groups and Messenger; produces the Facebook channel plan with page set-up, post and community choices, enquiry handling and a pilot review; not for building paid Meta ad campaigns (use `playbook-paid-social-advertising`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Facebook Presence Plan

Plans a Facebook Page, groups and Messenger around real enquiries the team can serve, for the client owner and delivery team.

<!-- dual-compat-start -->
## Use When
- Followers react to posts but few send messages, call or order, and the client wants a plan that turns followers into enquiries.
- Page posts, Facebook groups, Reels and Messenger need clear roles, formats and a posting rhythm for a Ugandan or East African audience.
- Enquiries from comments and Messenger need a handover to sales or WhatsApp with agreed response times.
- The client wants a short pilot to prove what works on Facebook before any money goes into boosting.

## Do Not Use When
- `playbook-paid-social-advertising` for Meta ad campaigns, audiences, budgets and tracking.
- `strategy-channel-architecture` for deciding whether Facebook should be a priority channel.
- `playbook-community-management` for day-to-day moderation and replies across channels.
- Stop before posting, boosting or changing Page settings without the client's authority; deliver the plan and changes for approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, service area, offer and buying path | Approved brief or client interview | Yes | Stop; do not infer platform penetration or customer behaviour from a regional stereotype. |
| Page export, insights or screenshots and existing assets | Page admin or supplied audit | Conditional | Mark the Page baseline `not assessed` and return a set-up plan with labelled assumptions. |
| Team capacity, working hours and response owner | Client operations lead | Yes | Cap the plan at one reviewable learning cycle and name the gap. |
| Current Page controls, CTA options and connected messaging (Messenger, WhatsApp) | Official Facebook help or the Page itself | Conditional | Omit dimensions and feature claims or flag them for live verification. |
| Uganda access status on the campaign date | Register UG-FACEBOOK-ACCESS-2026 and a same-day check | If the plan targets Uganda | Treat access as unstable and route time-critical messages to WhatsApp, Instagram or SMS. |

## Workflow

1. Confirm objective, market, decision owner and permission boundary; stop if the objective or owner is missing, or if the job is paid Meta campaigns.
2. Review the Page description, contact and service details, proof assets and primary next step against the account evidence; preserve working assets.
3. Choose formats and decide whether a group is justified, using the [Page, community and enquiry method](references/facebook-page-community-and-enquiry-method.md) and [the channel creative and service lab](../../pipeline/06-digital-marketing-strategy/references/channel-creative-and-service-lab.md).
4. Design the enquiry route (website, telephone, Messenger or WhatsApp) with recipient, confirmation, failure recovery, working hours, response commitment and a response decision tree; test it end to end.
5. For a Uganda plan, verify access on the campaign date against UG-FACEBOOK-ACCESS-2026 and name the fallback channel for every time-critical message.
6. Build the thirty-day pilot to agreed capacity: each unit's audience question, source, format, creative direction, owner, destination and review date.
7. Check paid readiness (objective, audience, offer, policy, tracking, destination, budget authority, sales/service readiness) before any boost is proposed.
8. Run the quality and anti-slop gates; correct any failed check and rerun it before handing the plan over for approval.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Facebook channel plan: Page review, format and group choices, posting rhythm | Client owner and delivery team | Each choice ties to the named audience, objective and account evidence; no fixed content ratio or reach guarantee. |
| Enquiry and service handoff map with response decision tree | Sales or service lead | Route tested end to end; recipient, hours, response commitment and escalation named. |
| Thirty-day pilot and paid-readiness checklist | Client owner; `playbook-paid-social-advertising` | Every unit has an owner, destination and review date; paid items list the unmet readiness conditions. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Platform verification log (feature, source, date, Uganda access check) | Table in the plan | Every volatile control or access claim has a dated source or is marked `not assessed`. |
| Enquiry-route test record | Checklist with test date and result | Shows the message reached the named recipient and the confirmation fired. |
| Pilot review record | Table: qualified enquiries, service outcomes, accepted opportunities, contribution, reach | Attention and sales outcomes reported separately. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Unpublishing a live Page, boosting and changing Page settings are never routine set-up steps.

## Degraded Mode

Without Page evidence or a confirmed response owner, return the narrowest qualified result and mark the affected checks `not assessed`. A set-up plan, enquiry-route design and pilot template can still be delivered with assumptions labelled.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A peer-to-peer community is the primary need | Use a Group with named moderation rules; retain the Page as the official identity | Mixing official notices with unmanaged member discussion |
| No Page exists or admin access is unavailable | Produce a Page set-up plan with assumptions labelled | False optimisation against invented history |
| Page evidence shows an established audience | Prioritise measured gaps and retain what already works | Destructive reset of working assets |
| A Page control, CTA, dimension or messaging feature is time-sensitive | Verify it against official Facebook help before stating it | Stale platform advice |
| The plan targets Uganda | State Facebook's status as unstable and verify access on the campaign date; keep a WhatsApp, Instagram or SMS fallback for any time-critical message (register UG-FACEBOOK-ACCESS-2026: access reported restored on 13 Jun 2026 after the January 2021 block, no UCC statement found) | Asserting that Facebook is either blocked or open on stale evidence |
| Posts produce messages the team cannot answer accurately (stock, delivery, price) | Repair catalogue/service information and response ownership before increasing reach | Paying for attention the operation cannot convert |
| A complaint, safety, legal or reputational issue arrives | Acknowledge and investigate; protect private details; escalate; moderate abuse and spam consistently | Public mishandling and synthetic-warmth replies |
| The content plan reposts other people's photos, videos or text, or recycles clips with only a watermark, border or speed change | Replace it with original posts or clearly transformed ones (own commentary, voiceover or creative edit) with rights cleared; Meta cuts distribution and monetisation for accounts that repeatedly repost unoriginal content (July 2025, register `META-UNORIGINAL-CONTENT-2025`; March 2026 follow-up, register `PREMIUM-META-ORIGINAL-2026`) | Page reach loss and demonetisation |
| Boosting is proposed | Verify every paid-readiness condition and separate a creative test from an offer test | Spend before the offer and service are ready |

## Quality Standards

- Page review covers description, contact/service information, proof assets and primary next step, with each change sourced.
- Format and group choices state the reader's job they serve; no fixed content ratio, reach ceiling or universal link penalty appears.
- Any group has membership, privacy, topics, promotion rules, escalation and a named moderator.
- The enquiry route records recipient, confirmation, failure recovery, working hours and response commitment, and collects only necessary information.
- Posting times come from account evidence or a bounded test; no weekly quota is presented as an algorithm requirement.
- Uganda plans cite UG-FACEBOOK-ACCESS-2026 and name a fallback channel for time-critical messages.
- Reports separate qualified enquiries, service outcomes, accepted opportunities and contribution from reach and interactions.
- British English; worked examples are labelled scenarios, not client evidence.

## Anti-Patterns

- Treating group membership as a prospect list. Fix: participate within each group's rules and invite people to the Page or enquiry route.
- Removing legitimate criticism because it mentions a competitor. Fix: moderate only abuse and spam, consistently and by published rules.
- Claiming a message came from the post it followed. Fix: report the enquiry as observed and state the attribution limit.
- Choosing a scheduling tool on assumed reach penalties. Fix: require current authorised integration evidence.
- Stating that Facebook is blocked or open in Uganda from memory. Fix: check UG-FACEBOOK-ACCESS-2026 and verify on the campaign date.
- Forcing humour or a comment prompt into every caption. Fix: give the context the content needs and stop.

## References

- [Facebook Page, community and enquiry method](references/facebook-page-community-and-enquiry-method.md): read when reviewing the Page, choosing formats or groups, designing the enquiry handoff, or building the pilot and paid-readiness check.
- [Channel creative and service lab](../../pipeline/06-digital-marketing-strategy/references/channel-creative-and-service-lab.md): read when planning production, creators, community, paid readiness and commercial measurement.
- [`playbook-paid-social-advertising`](../../playbooks/playbook-paid-social-advertising/SKILL.md): read when the plan moves to paid Meta campaigns.
- [`platform-whatsapp`](../platform-whatsapp/SKILL.md): read when WhatsApp is the enquiry handoff or the Uganda fallback channel.
- [Legal, privacy and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when the plan states Facebook's access status in Uganda.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting captions and replies.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting reply tone and spelling.
<!-- dual-compat-end -->

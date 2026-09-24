---
name: biz-dev-lawful-prospecting-outreach
description: Use when an agency or client needs a lawful B2B prospecting system covering sourcing and cleaning contact lists, consent and objection handling, cold and warm outreach sequences, speed-to-lead and partner introductions; use biz-dev-video-outreach for personalised video audits and biz-dev-reactivation-campaign for past customers.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Lawful Prospecting and Outreach

Design an outreach system that fills the pipeline without breaking data-protection law, platform policy or premium positioning: lawful lists, plain personal messages, a short value-adding cadence, fast responses and warm introductions.

<!-- dual-compat-start -->
## Use When

- An agency or B2B client wants to start or fix cold or warm outreach by email, phone, LinkedIn or WhatsApp.
- A plan proposes buying, scraping or "borrowing" contact lists.
- Leads reply but are not called back quickly, or follow-up relies on guilt and pressure.
- A joint-venture or referral partner could introduce the business to its audience.

## Do Not Use When

- The deliverable is a personalised video audit for a named prospect; use `biz-dev-video-outreach`.
- The contacts are past customers to win back; use `biz-dev-reactivation-campaign`.
- The work is consented marketing to an opted-in list (newsletters, broadcasts); use `07-email-marketing-strategy` or `playbook-sms-whatsapp-marketing`.
- The request is to send messages now; this skill plans and drafts. Sending needs explicit authority.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Target niche and ideal-customer criteria | Agency or client owner; `biz-dev-practitioner-positioning` | Yes | Stop; agree the niche first |
| Proposed list sources and how each was collected | Client or list owner | Yes | Treat every unknown source as unusable |
| Data-protection status (registration, lawful basis, privacy notice) | Client data-protection owner | Yes before any sending | Draft the plan only; mark compliance `not assessed` |
| Proof assets (verified results, case studies, content offer) | Client, with consent records | Conditional | Use the content-offer play only; no result claims |
| Sales capacity (who calls back, response window) | Delivery owner | Yes | Do not design a sequence faster than the team can answer |

## Workflow

1. Confirm niche, offer, markets and who approves outreach; stop if any market's data-protection position is unknown and unassessable.
2. Map each list source to a lawful basis and jurisdiction using the reference checks; drop sources that fail, and stop scraping or bought-list plans.
3. Clean the list through at least five fit filters; split roles so one person researches and another calls.
4. Choose the play sequence (High-value-job question → One-company-per-area only if the policy is real → Content offer) and draft plain-text messages with opt-out wording.
5. Set the cadence: at most three value-adding touches, across at least three of four channels where lawful, with suppression after an objection.
6. Define speed-to-lead: who answers, within what window, and the screen-video fallback.
7. Review drafts against the ethics filter and anti-slop gate; correct any fake scarcity, guilt or unverified claim and rerun.
8. Hand over the plan, message library, suppression process and weekly tracking sheet.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| List-governance sheet | Data-protection owner and researcher | Every source has a jurisdiction, lawful basis and keep/drop decision |
| Outreach play library | Sales or business-development lead | Plain-text messages with opt-out line; no invented results |
| Cadence and speed-to-lead plan | Delivery team | Touch limit, response window, owner and suppression rule stated |
| Weekly tracking sheet | Owner | Sends, replies, bookings, held meetings, wins, opt-outs, complaints |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Compliance check record | Table per market | Cites the source-register entry or marks the item `not assessed` |
| Suppression and objection log | Register | Every objection actioned within the stated window |

## Capability and Permission Boundaries

Read and search supplied lists, policies and evidence. Planning and drafting are read-only. Collecting, matching or storing personal data, sending any message, placing calls or registering accounts needs explicit client authority, a lawful basis and, where required, data-protection registration. This skill screens and escalates; it does not give legal advice.

## Degraded Mode

If the legal position for a market is unconfirmed, deliver the plan for business-address, opted-in and referral routes only, mark the rest `not assessed`, and list the checks a qualified adviser must complete.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Plan relies on scraped or bought personal contact data | Replace with association directories, public business registries, events and referrals, subject to lawful basis | Data-protection breach and reputational damage |
| A person objects or asks to stop | Suppress immediately and confirm within the legal window | Breach of objection rights |
| "One partner per area" is proposed | Use it only if the agency truly enforces territorial exclusivity | Fake scarcity |
| Replies arrive faster than the team can call back | Slow sends or add capacity | Wasted interest and poor first impressions |
| WhatsApp is proposed for first contact | Check current WhatsApp Business policy on business-initiated messages and opt-in first | Account restriction and complaints |
| A claim cites a client result | Require a verified record and client consent | Fabricated or unauthorised proof |

## Quality Standards

- Messages read like a personal note from a real person: short, specific, no HTML banners.
- Every message identifies the sender and gives a free, simple way to opt out.
- No guilt, pressure or fabricated third-party prompts.
- Legal statements cite the source register with the check date; unverified points stay as checks.

## Anti-Patterns

- Scraping personal contact details and blasting them. Fix: lawful business sources, fit filters, opt-out and suppression.
- Daily "probing" follow-ups or one-word "Well?" messages. Fix: three value-adding touches, then stop.
- Claiming territorial exclusivity that is not enforced. Fix: offer it only as a real, written policy.
- Handing all research, writing and calling to one freelancer. Fix: separate researcher and caller roles.
- Sending material before a conversation. Fix: call first, then send only what helps.
- Treating Uganda's Act as requiring opt-in for all marketing. Fix: state the consent and objection rules exactly as registered.

## References

- [Outreach plays, cadence and scripts](references/outreach-plays-and-scripts.md) — read when drafting messages, sequences and partner approaches.
- [Data-protection and platform checks for outreach](references/data-protection-checks-for-outreach.md) — read before any list is used or message sent.
- [Direct marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md) — release check for every message.
- [Personalised video outreach](../biz-dev-video-outreach/SKILL.md) — neighbour route.
- [Reactivation campaign](../biz-dev-reactivation-campaign/SKILL.md) — neighbour route for past customers.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md)
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

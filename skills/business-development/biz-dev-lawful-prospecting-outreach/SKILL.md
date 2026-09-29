---
name: biz-dev-lawful-prospecting-outreach
description: Use when an agency or B2B firm wants to start or fix cold and warm outreach by email, phone, LinkedIn or WhatsApp, or is tempted to buy or scrape contact lists; produces a list-governance sheet, outreach scripts and cadence, video-audit outreach and a speed-to-lead plan; not for staff LinkedIn advocacy (use `playbook-social-selling`).
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

- We want to start cold or warm outreach to businesses by email, phone, LinkedIn or WhatsApp and need the scripts and a follow-up sequence.
- Someone has proposed buying, scraping or borrowing a contact list and we need to know whether it is lawful under Uganda's DPPA 2019, Kenya's Data Protection Act or GDPR.
- Leads reply but nobody calls them back quickly, or our follow-ups rely on guilt and pressure.
- A referral or joint-venture partner could introduce us to their customers and we need the approach and the ask.
- A consultant wants to record a personalised video audit (a short screen recording, for example on Loom) of one prospect's website, Facebook Page or Instagram and send it with follow-ups to book a sales call.

## Do Not Use When

- `playbook-social-selling` for staff LinkedIn profiles, employee advocacy and executive social presence.
- `07-email-marketing-strategy` for win-back of past customers or newsletters to an opted-in list.
- `playbook-sms-whatsapp-marketing` for broadcasts to contacts who have already opted in.
- Stop if any contact source has no lawful basis or no opt-out route and drop it; draft only, because sending needs explicit client authority.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Target niche and ideal-customer criteria | Agency or client owner; `biz-dev-positioning` | Yes | Stop; agree the niche first |
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
6. Define speed-to-lead: who answers, within what window, and the screen-video fallback. For a personalised video audit of a named prospect, follow the video outreach reference: 2–3 observations, permission before WhatsApp, at most two follow-ups.
7. Review drafts against the ethics filter and anti-slop gate; correct any fake scarcity, guilt or unverified claim and rerun.
8. Hand over the plan, message library, suppression process and weekly tracking sheet.

## Outputs

| Artefact | Consumer | Acceptance condition |
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

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Collecting, matching or storing personal data, sending any message, placing calls or registering accounts also needs a lawful basis and, where required, data-protection registration; this skill screens and escalates and does not give legal advice.

## Degraded Mode

Without a confirmed data-protection position for each target market, return the narrowest qualified result and mark the affected checks `not assessed`. The plan for business-address, opted-in and referral routes can still be delivered, with the checks a qualified adviser must complete listed for the rest.

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

- [Outreach plays, cadence and scripts](references/outreach-plays-and-scripts.md): read when drafting messages, sequences and partner approaches.
- [Data-protection and platform checks for outreach](references/data-protection-checks-for-outreach.md): read before any list is used or message sent.
- [Direct marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md): read when running the release check on every message.
- [Personalised video outreach](references/personalised-video-outreach.md): read when recording a video audit of one named prospect and writing its message and follow-ups.
- [Win-back and reactivation](../../pipeline/07-email-marketing-strategy/references/win-back-and-reactivation.md): read when the contacts are past customers (neighbour route).
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when a message or plan states a legal or market-specific claim.
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

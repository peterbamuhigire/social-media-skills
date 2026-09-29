---
name: playbook-community-management
description: 'Use when a brand''s comments, DMs and groups need looking after: response times, reply templates, social customer service, Like-Know-Trust content, or a WhatsApp or Facebook Group community; produces the response guide, saved replies and community health scorecard; not for repairing a damaged rating (use `playbook-reputation-management`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Community Management Playbook

Produces a client's community response guide: platform SLAs, ready reply templates, escalation to the client, negative-review handling, proactive engagement and a monthly community health scorecard, with Uganda and East African defaults.

<!-- dual-compat-start -->
## Use When
- Response-time targets and reply templates for enquiries, complaints, delivery problems, abusive comments and reviews on the brand's pages.
- Customer service in WhatsApp, Messenger and comment inboxes: triage, complaint scripts, saved replies and staff training.
- Followers like posts but never enquire; find where they sit on Like-Know-Trust and plan a 10-4-1 content mix to build trust.
- Launch a niche group on WhatsApp, a Facebook Group or LinkedIn with house rules, founding members and a reason for members to stay.
- A monthly scorecard for engagement and conversation quality, with clear rules on when to escalate to the client.

## Do Not Use When
- `playbook-reputation-management` for a reputation audit, review generation and recovery once ratings have been damaged.
- `playbook-crisis-communications` when a post has gone viral for the wrong reasons or the media are calling.
- `playbook-chatbot-strategy` for automated inbox replies and bot flows.
- Stop before deleting comments, banning members or replying publicly to a sensitive complaint without the client's approval; escalate and deliver a draft reply.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, business type (product, service or both) and country/city | Client | Yes | Default to Uganda/East Africa and ask for the business type before writing templates. |
| Platforms managed | Client or account list | Yes | Populate the SLA table for Facebook, Instagram and WhatsApp Business only and mark the rest `not assessed`. |
| Business hours (days and times, EAT) | Client | Yes | Use Monday–Friday 08:00–17:30 EAT as a labelled placeholder until confirmed. |
| WhatsApp Business number and client escalation contact (name, title, channel) | Client | Yes | Leave the escalation step unassigned and return it as a blocking gap; do not reply publicly to Level 2+ issues. |
| Brand tone | `04-brand-voice-intake` output | Yes | Ask for three adjectives (for example warm, professional, direct). |
| Follower count and last month's platform data | Platform exports | For the scorecard | Leave targets blank and mark the scorecard ratings `not assessed`. |

## Workflow

1. Run the intake in the [community response guide](references/community-response-guide.md); stop if there is no escalation contact, because Level 2+ issues cannot be routed.
2. Populate the response-time SLA table with the client's hours and platforms, including the X/Twitter trending exception and out-of-hours acknowledgement.
3. Adapt the nine scenario templates (positive comment, enquiry, complaint, delivery complaint, abusive comment, competitor comment, media enquiry, positive review, negative review) to the brand tone and contact details.
4. Write the escalation protocol with the named client contact and the 30-minute screenshot-and-hold process, plus the four-step negative-review process and the conversation classification ladder.
5. Where the inbox is a customer-service operation, add triage, SLAs by business size, scripts and training from [social customer care](references/social-customer-care.md); where followers engage but never enquire, run the [Like-Know-Trust diagnostic](references/community-trust-framework.md); for a new group, design it with [micro-community design](references/micro-community-design.md).
6. Plan proactive engagement: 10 industry question ideas, 5–10 engagement partners, pinned content and milestones.
7. Set the monthly community health scorecard targets from current follower count and platform mix; check every template against the quality standards, correct gaps and rerun the check before handing the guide to the client for approval.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Response-time SLA table | Social media manager and client | Uses the client's actual hours and platforms, not the defaults. |
| Reply template set and saved replies | Social media manager | Every template ready to paste; no "[write something here]" placeholders; British English; brand tone applied. |
| Escalation protocol and negative-review process | Social media manager and client contact | Names the actual client contact and channel; states the 30-minute trigger and hold-until-directed rule. |
| Proactive engagement plan | Social media manager | At least 10 question ideas tailored to the client's industry and Ugandan/EA market. |
| Monthly community health scorecard | Client via `meta-reporting` | Targets suit the client's follower count and platform mix; G/A/R key applied. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Incident log | Scorecard row per escalation | Each escalation has a screenshot, timestamp, level and the client's direction. |
| Moderation record | Table: comment, action, reason, screenshot | Nothing hidden or deleted without a screenshot first and a documented reason. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Deleting comments, banning members and public replies to sensitive complaints wait for the client's approval.

## Degraded Mode

Without the client's escalation contact and business hours, return the narrowest qualified result and mark the affected checks `not assessed`. Draft templates, the SLA table with labelled defaults and the negative-review process can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A comment creates safety, legal or credible crisis risk | Preserve evidence and escalate under the response matrix. | Casual replies that worsen harm. |
| A comment names a staff member negatively, mentions legal action, comes from media, raises safety, or passes 50+ negative reactions | Screenshot, send to the client within 30 minutes and hold all public replies until directed. | An unapproved public reply to a Level 2+ issue. |
| Page has reach and engagement but few enquiries, or the brand is new or recovering its reputation | Run the Like-Know-Trust diagnostic and sequencing in [community-trust-framework](references/community-trust-framework.md). | Selling to an audience that has no proof to act on. |
| The social inbox is a customer-service operation run by untrained or junior staff | Apply the triage, SLAs by business size, scripts, training and monthly review in [social-customer-care](references/social-customer-care.md). | Inconsistent replies and complaints going viral through mishandling. |
| Client wants to build or relaunch a niche group or private community around member value | Design it with [micro-community-design](references/micro-community-design.md) before recruiting. | An unmanaged broadcast group that dies or fills with spam. |
| A negative review arrives | Acknowledge, empathise, take offline, never argue; prioritise it over positive reviews. | Losing prospective customers who read the exchange. |
| Abusive comment with personal abuse, hate speech or profanity | Respond, screenshot, then hide; delete only for egregious platform-standard breaches and document it. | Censorship claims or lost evidence. |
| A public exchange needs personal details | Acknowledge without repeating them and move to the official private route with a response time. | Exposing customer data in public. |

## Quality Standards

- Every response template is complete and ready to copy-paste, with no generic filler or placeholders left unfilled.
- The SLA table uses the client's actual business hours and platforms.
- The escalation protocol names the actual client contact and channel.
- The four-step negative-review process is explained with its rationale, not only the steps.
- The engagement section has at least 10 question ideas tailored to the client's industry and Ugandan/EA market.
- Scorecard targets reflect the client's current follower count and platform mix.
- All templates use British English and the brand tone adjectives; no American spellings.
- No out-of-scope elements appear (no graphic design, paid ad guidance or influencer contracts).

## Anti-Patterns

- Arguing with or contradicting a reviewer in public. Fix: acknowledge, empathise and take it offline; the audience is every future customer.
- Deleting a legitimate complaint. Fix: reply publicly, move details to DM or WhatsApp and log it.
- Treating disagreement as trolling. Fix: classify the exchange first and use the response ladder before moderating.
- Engaging a competitor's comment publicly. Fix: screenshot and forward to the client; delete only clear promotional spam.
- Leaving customers without acknowledgement overnight. Fix: set away messages confirming the next business-day response time in EAT.
- Conditioning service on a positive review. Fix: invite an honest review only after the experience has been put right.
- Community work that is only reactive. Fix: schedule conversation starters twice a week and review engagement partners monthly.

## References

- [Community response guide](references/community-response-guide.md): read when running intake, filling the SLA table, adapting templates, escalating, handling negative reviews, planning engagement or completing the scorecard.
- [Social customer care](references/social-customer-care.md): read when the work is customer service in social inboxes: triage, complaint scripts, saved replies, staff training.
- [Community trust framework](references/community-trust-framework.md): read when diagnosing an audience's Like-Know-Trust stage or planning trust-building content.
- [Micro-community design](references/micro-community-design.md): read when designing, launching or monetising a WhatsApp, Facebook Group, LinkedIn Group or private community.
- [`playbook-crisis-communications`](../playbook-crisis-communications/SKILL.md): read when a Level 2 or Level 3 crisis threshold is reached.
- [`playbook-reputation-management`](../playbook-reputation-management/SKILL.md): read when ratings are already damaged.
- [`meta-reporting`](../../meta-analytics-ops/meta-reporting/SKILL.md): read when sharing the scorecard in the monthly report.
- [`04-brand-voice-intake`](../../pipeline/04-brand-voice-intake/SKILL.md): read when the brand tone is missing.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when writing templates and replies.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and spelling.
<!-- dual-compat-end -->

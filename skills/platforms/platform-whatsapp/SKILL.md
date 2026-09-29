---
name: platform-whatsapp
description: 'Use when a business wants to run WhatsApp Business well: profile, catalogue, greeting and away messages, broadcast lists, Status, groups, opt-in and a service rota; produces the WhatsApp channel plan with a 30-day broadcast calendar and message templates; not for bulk SMS or API messaging campaigns (use `playbook-sms-whatsapp-marketing`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# WhatsApp Business Strategy

Plans WhatsApp Business as a permission-based direct channel, not a conventional social platform: every message must be high-value, relevant and earn its place in the recipient's inbox, because spam destroys trust faster here than on any other channel.

<!-- dual-compat-start -->
## Use When
- The client wants WhatsApp to be a trusted direct channel and needs its role, opt-in and opt-out rules agreed.
- WhatsApp Business needs setting up: profile, greeting and away messages, quick replies, broadcast lists, catalogue, a customer service protocol, escalation and a team rota.
- The client wants a 30-day broadcast calendar, a Status plan and ready-to-send message templates.
- Customer groups or communities on WhatsApp need rules, moderation and a clear purpose.

## Do Not Use When
- `playbook-sms-whatsapp-marketing` for bulk SMS and WhatsApp Business API campaigns.
- `playbook-chatbot-strategy` for automated chat flows and bots.
- `playbook-community-management` for community management across several channels.
- Stop before messaging anyone who has not opted in or sending broadcasts without client authority; Uganda DPPA 2019 consent rules apply.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client and trading name, industry, products/services, country/city and primary goal | Approved brief or client interview | Yes | Stop the goal decision; default the market to Uganda/East Africa and label it. |
| WhatsApp Business number and current usage (personal number, Business app or Platform API) | Client operations lead | Yes | Plan a new Business app set-up and mark the migration path `not assessed`. |
| Contact list size, how existing broadcast lists or groups were built, and opt-in records | Client; contact export | Yes | Treat every contact without an opt-in record as not opted in; plan fresh opt-in capture before any broadcast. |
| Key customer segments and average purchase value (UGX or USD) | Client sales records | Conditional | Use the four default segments and state the chosen active/lapsed line as provisional. |
| Business hours, team size and response owner | Client operations lead | Yes | Write the away message and SLA as drafts and name the missing owner. |

## Workflow

1. Confirm goal, owner and permission boundary; stop if any contact lacks opt-in or if the job is bulk SMS or API campaigns (`playbook-sms-whatsapp-marketing`). Uganda DPPA 2019 consent rules apply.
2. Set up the profile, catalogue, greeting and away messages, quick replies and labels from the [channel playbook](references/whatsapp-channel-playbook.md) §1; where structured customer service is needed, set labels, templates, SLA, escalation and the team rota with [app operations](references/whatsapp-business-app-operations.md) first.
3. Segment broadcast lists (Prospects, Active, Lapsed, VIP) and choose one active/lapsed line for the client from its purchase cycle.
4. Apply the broadcast content rules: value first, frequency ceiling, under 150 words, personal tone, STOP opt-out line on every broadcast.
5. Plan Status, and groups only where a community purpose and a second admin exist; write the community rules.
6. Build the opt-in capture methods and opt-out etiquette, then the 30-day calendar with the 12 templates; for launches use the [campaign and broadcast sequences](references/campaign-and-broadcast-sequences.md).
7. Set the KPI tracker within Business app analytics limits.
8. Run the legal, quality and anti-slop gates; correct any failed check and rerun it before handing over. Drafting messages does not authorise sending them.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| WhatsApp channel plan: profile, catalogue, automated messages, quick replies and labels | Client operations lead | Every field written out; no placeholders left for the client to invent. |
| Segmentation and broadcast rules | Staff sending broadcasts | Client can categorise existing contacts immediately using the label system. |
| 30-day broadcast calendar with 12 full templates | Client owner | Every entry names segment, message type and template; each template is under 150 words with an opt-out line. |
| Status and group plan with community rules | Community admin | Groups named by purpose, with rules, pinned welcome message and a second admin. |
| KPI tracker | Client owner | Only metrics available natively or by spreadsheet are claimed. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Opt-in and opt-out log | Table: contact, method, date, staff member, status | Every broadcast recipient has a logged opt-in; STOP removals recorded, contacts not deleted. |
| Automated-message test record | Checklist with test date | Greeting, away message and quick replies tested from a personal number before the number is promoted. |
| Monthly KPI sheet | Spreadsheet | Opt-out rate, reply rate, enquiry volume and conversion recorded per broadcast or month. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Messaging follows the WhatsApp Business Messaging Policy (register WHATSAPP-BUSINESS-POLICY) and Uganda DPPA 2019 consent rules.

## Degraded Mode

Without opt-in records for the contact list, return the narrowest qualified result and mark the affected checks `not assessed`. The set-up checklist, opt-in capture plan and templates can still be delivered, with no broadcast scheduled until consent is logged.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Recipients need privacy and one-way updates | Use an opted-in broadcast, not a group | Exposed phone numbers and unwanted discussion |
| No Business account exists or the app cannot be inspected | Produce a set-up plan with assumptions labelled | False optimisation against invented history |
| The account is established with working lists | Prioritise measured gaps and keep what already works | Destructive reset of working assets |
| An app limit, field length, image size or API eligibility figure is time-sensitive | Verify it against official WhatsApp help before stating it | Stale platform advice |
| The client needs day-to-day WhatsApp Business operations or structured customer service | Set up labels, templates, SLA and escalation with [app operations](references/whatsapp-business-app-operations.md) before any broadcast | Marketing noise overwhelming customer care |
| A contact replies STOP | Remove immediately from every list, reply once, do not ask why, label as removed; never message from another list without fresh consent | Consent breach and complaints |
| The playbook and the operations reference give different figures (segment line, broadcast ceiling, catalogue price display, thumbnail) | Pick the segment line, broadcast ceiling and catalogue price-display rule ("contact for pricing" or price always shown) per client from its purchase cycle and policy, and state them in the plan; verify the catalogue thumbnail size (about 48 or 50 px) against official WhatsApp Business help before stating it | Inconsistent rules across staff |
| The plan uses the WhatsApp Business Platform (API) or costs messages | Cost it from [Platform pricing and templates](references/whatsapp-platform-pricing-and-templates.md), the single source for message pricing: per-message since 1 Jul 2025, East Africa in "Rest of Africa", service replies chargeable after 1,000 a month per number from 1 Oct 2026, free entry point window up to 7 days from click-to-WhatsApp ads (register `WHATSAPP-PRICING-2025`) | Budgets built on the retired conversation model or on "replies are always free" |
| A complaint arrives in a group | Move it to a private direct conversation within one message | Public escalation |

## Quality Standards

- All eight playbook sections are covered with no placeholders; every template contains complete, ready-to-use text.
- Broadcast templates are personalised, conversational and under 150 words, each with an opt-out instruction.
- Segmentation lets the client categorise existing contacts immediately using the label system.
- The 30-day calendar specifies segment, message type and template reference for every entry.
- Opt-in methods suit the Ugandan/EA market (QR codes, click-to-WhatsApp, verbal opt-in at point of sale).
- KPIs are realistic for the WhatsApp Business app; no claim is made about data that is not available natively.
- The permission-based, value-first rule is applied across all broadcast and group guidance.
- No message reads like a newsletter, email blast or social media post.

## Anti-Patterns

- Adding contacts to a broadcast list without explicit permission. Fix: capture opt-in by QR code, click-to-WhatsApp link, keyword or logged verbal consent.
- "Just checking in" broadcasts. Fix: give a tip, update, offer, reminder or useful information every time.
- Forwarding chain messages, viral content or news articles, or sending the same message twice. Fix: write original, purposeful messages.
- Sending promotional messages without a prior relationship. Fix: start prospects on educational and proof content.
- Letting a group run without rules or cover. Fix: pin the rules, set admin-only posting for announcements and appoint a second admin.
- Reporting open rates as measured data. Fix: use reply rate as the proxy and state the app's analytics limits.

## References

- [WhatsApp channel playbook](references/whatsapp-channel-playbook.md): read when collecting the intake, setting up the app, segmenting lists, writing broadcasts, Status and group content, capturing opt-in, building the 30-day calendar and templates, or setting KPIs.
- [WhatsApp Business app operations](references/whatsapp-business-app-operations.md): read when setting up the profile, automated messages, catalogue, service protocol, escalation or team rota.
- [Campaign and broadcast sequences](references/campaign-and-broadcast-sequences.md): read when WhatsApp is part of a launch, event push or timed campaign.
- [Platform pricing and templates](references/whatsapp-platform-pricing-and-templates.md): read when costing Platform (API) messages, choosing template categories, using the service or free entry point windows, or wording opt-in that names the business.
- [Current-source register](../../../docs/source-registers/README.md): read when checking WHATSAPP-BUSINESS-POLICY or other register records.
- [Legal, privacy and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read before any plan that processes contact data or schedules broadcasts.
- [`playbook-sms-whatsapp-marketing`](../../playbooks/playbook-sms-whatsapp-marketing/SKILL.md): read when the job is bulk SMS or WhatsApp Business API campaigns.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting broadcasts, Status and templates.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and spelling.
<!-- dual-compat-end -->

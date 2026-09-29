---
name: playbook-sms-whatsapp-marketing
description: 'Use when a business wants to send offers and reminders to opted-in customers by WhatsApp broadcast or SMS: campaign calendars, templates, automated sequences, catalogue promotion, opt-in and opt-out, delivery metrics; produces the broadcast and SMS campaign plan with message copy; not for setting up WhatsApp Business (use `platform-whatsapp`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# SMS and WhatsApp Marketing Playbook

Plans opted-in WhatsApp broadcast, WhatsApp Business API sequence and SMS campaigns for Ugandan and East African businesses, with copy, consent handling and monthly metrics. It assumes the WhatsApp Business account is fully configured: if not, complete `platform-whatsapp` first (app setup, catalogue configuration, broadcast list creation, opt-in capture and the 30-day broadcast calendar); this playbook extends that foundation into campaign strategy, automated sequences and SMS marketing.

<!-- dual-compat-start -->
## Use When
- Choose between SMS and WhatsApp for a promotion and decide which suits each kind of message.
- Plan a month of WhatsApp broadcast campaigns using the five-part message formula, for example for a Kampala retail shop.
- Write welcome, abandoned-enquiry and re-engagement sequences on the WhatsApp Business API.
- Write short SMS promotions and reminders sent through Africa's Talking or another bulk gateway.
- Collect opt-ins, honour STOP requests and report delivery, reads, replies and sales each month.

## Do Not Use When
- `platform-whatsapp` for the WhatsApp Business account, profile, catalogue and channel plan.
- `playbook-chatbot-strategy` for inbound bot replies.
- `07-email-marketing-strategy` for the email programme.
- Stop before sending to any number without recorded opt-in under the Uganda DPPA 2019 or the client's approval of the message and send date.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry, country/city and primary objective (sales / appointments / awareness / retention) | Client | Yes | Default the market to Uganda/East Africa; stop if the objective is not chosen. |
| Contact list size, WhatsApp and SMS counted separately | Client CRM or phone exports | Yes | Assume under 256 contacts and recommend the WhatsApp Business app, labelled provisional. |
| Current opt-in process and consent records | Client data owner | Yes | Treat the list as unconsented: plan opt-in capture first and hold every send. |
| WhatsApp Business account type: app (free) or API (paid, via a BSP) | Client; `platform-whatsapp` output | Yes | Route to `platform-whatsapp` if the account is not set up. |
| Monthly SMS gateway budget (UGX or USD) and telecom operators used by the audience (MTN Uganda / Airtel Uganda / other) | Client | For SMS | Plan WhatsApp only and mark the SMS plan `not assessed`. |
| Message approver and send-date sign-off | Client lead | For sending | Deliver copy and calendar as drafts only. |

## Workflow

1. Collect the intake details and confirm the WhatsApp Business account is configured; stop and route to `platform-whatsapp` if it is not.
2. Confirm documented opt-in for every list; stop any send to a number without recorded consent under the Uganda Data Protection and Privacy Act 2019.
3. Choose channels with the decision framework (app, API, SMS or all three) by list size, automation need and audience type.
4. Build the 4-week broadcast calendar with days, times in EAT, segments and campaign types, writing every message with the 5-part formula.
5. For API clients, write the welcome, abandoned-enquiry and re-engagement sequences as pre-approved templates.
6. Set catalogue entries and seasonal updates, then write SMS templates within 160 characters, with the business name and an opt-out line in each.
7. Set the opt-out process, quarterly list hygiene and the metric targets with the monthly reporting template.
8. Check every template against the quality standards and the anti-slop gate; correct failures and rerun the check before hand-off.

The full procedure, calendar, sequences, templates and metric tables are in [the campaign method](references/sms-whatsapp-campaign-method.md).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Channel decision and 4-week broadcast calendar | Client marketing lead | Specific days, EAT times, segments and message types; frequency caps respected. |
| WhatsApp sequences and SMS templates | Client sender or BSP operator | Ready to use with only name, date and product substitutions; each carries one CTA and an opt-out line. |
| Opt-in, opt-out and list-hygiene procedure | Client data owner | Names the Uganda Data Protection and Privacy Act 2019 and applies to both WhatsApp and SMS. |
| Metric targets and monthly reporting template | Client lead | Every metric has a numerical target. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Consent log (date, staff member, customer name, method) | Table or CRM field | Every contact on a send list has a logged opt-in; opted-out contacts are labelled, not deleted. |
| SMS character-count check | Column beside each template | Each template shows its count; any over 160 is flagged as two-message billing. |
| Monthly campaign report | Reporting template table | Sends, delivered, read/opened, replied, converted, cost (UGX) and cost per conversion recorded per campaign. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Sending a broadcast, SMS or sequence, uploading contacts to a gateway or BSP, and registering a sender ID each need that authority.

## Degraded Mode

Without documented opt-in records, return the narrowest qualified result and mark the affected checks `not assessed`. Message copy, the calendar and the opt-in capture plan can still be delivered as drafts, with no send dates confirmed.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Consent, sender identity or opt-out handling is missing | Do not send | Intrusive messaging and compliance exposure |
| List under 256 contacts, manual sending, no automation needed | Use the WhatsApp Business app (free, no technical setup) | Paying for an API the client does not need |
| List over 256, or automation, triggers or CRM integration required | Use the WhatsApp Business API via a BSP with pre-approved templates | Hitting the 256 broadcast cap or sending unapproved templates |
| Non-smartphone users, transactional alerts or guaranteed delivery needed | Use SMS through a gateway such as Africa's Talking with a branded sender ID | Missing contacts outside WhatsApp |
| Highest-value campaign | Run all three in parallel: API for opted-in WhatsApp contacts, SMS as fallback | Reach lost to a single channel |
| Promotional frequency would exceed 2× per week (4× in a campaign fortnight) | Replace with educational or loyalty messages | Opt-outs from over-selling |
| A contact replies STOP | Remove from all lists in the same session, acknowledge, label "Opted Out" and never re-add without fresh consent | Breach of consent and trust |
| An API campaign needs a cost estimate or template category | Cost each delivered marketing, utility or authentication template from the East Africa ("Rest of Africa") rate card and add BSP fees; the opt-in must name the business (register `WHATSAPP-PRICING-2025`, `WHATSAPP-BUSINESS-POLICY`) | Budgets on the retired conversation model; templates recategorised as marketing |
| An SMS runs past 160 characters | Cut it or accept two-message billing knowingly | Doubled cost per send |

## Quality Standards

- Every message template is complete and ready to use, needing only name, date and product substitutions, with no placeholder descriptions left.
- The Uganda Data Protection and Privacy Act 2019 is named in the opt-in/opt-out section and consent requirements are linked to both WhatsApp and SMS.
- Africa's Talking is named as the recommended SMS gateway for Uganda and East Africa with its rationale (EA pricing, local support, API quality, sender ID registration).
- The 4-week broadcast calendar gives specific days, times in EAT, segment targets and message types, not a list of content categories.
- The decision framework clearly separates WhatsApp Business app, WhatsApp Business API and SMS by list size, automation need and audience type.
- Every metric carries a numerical target; no metric appears without a benchmark figure.
- `platform-whatsapp` is referenced as the setup foundation and its account configuration or basic broadcast content is not duplicated.
- British English throughout (organisation, catalogue, programme, behaviour, enquiry, recognise, analyse), with no American spellings.

## Anti-Patterns

- Two CTAs in one message. Fix: keep one unambiguous action, such as "Reply YES" or "Call us on [number]".
- Dropping the opt-out line from a broadcast or SMS. Fix: end every message with "Reply STOP to unsubscribe" or "Reply STOP to opt out"; no exceptions.
- Abbreviations such as "u", "ur" and "2moro" in business messages. Fix: write in full; professionalism outweighs the saved characters.
- Omitting the business name from an SMS. Fix: include it in every message, because recipients rarely save business numbers.
- Long raw URLs in SMS. Fix: use bit.ly or Africa's Talking short links so links fit and can be tracked.
- Deleting opted-out contacts. Fix: label them "Opted Out" so they are never re-added without fresh, documented consent.
- Stating false stock urgency in abandoned-enquiry messages. Fix: mention remaining stock only when it is genuine.

## References

- [SMS and WhatsApp campaign method](references/sms-whatsapp-campaign-method.md): read when comparing channels, building the calendar, writing sequences, catalogue entries or SMS templates, setting opt-in and opt-out, or reporting metrics.
- [`platform-whatsapp`](../../platforms/platform-whatsapp/SKILL.md): read when the WhatsApp Business account, catalogue or broadcast lists are not yet set up.
- [WhatsApp Platform pricing and templates](../../platforms/platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md): read when costing API sends, choosing template categories, checking per-user marketing limits or wording opt-in.
- [`playbook-chatbot-strategy`](../playbook-chatbot-strategy/SKILL.md): read when the need is inbound bot replies.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when consent, data-protection or pricing claims appear in messages.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting broadcast, sequence and SMS copy.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone for messages.
<!-- dual-compat-end -->

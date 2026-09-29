# WhatsApp Business App Operations

Merged from skills/playbooks/playbook-whatsapp-business on 2026-09-29 at cda737c (S04 tree); preservation map: [playbook-whatsapp-business.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/playbook-whatsapp-business.md)

## When to use this reference

Read this reference when the client needs the day-to-day operating set-up for WhatsApp Business rather than the channel strategy: profile copy, greeting and away messages, a quick-reply library, broadcast-list rules, catalogue standards, a customer-service protocol with escalation, and a team rota. The parent [SKILL.md](../SKILL.md) owns channel role, segmentation, Status, groups, opt-in and the 30-day broadcast calendar; this reference turns them into a working operation.

Where a workflow needs structured customer service rather than promotion, set up labels, templates and escalation before any broadcast; otherwise marketing noise overwhelms customer care. Drafting messages does not authorise sending them.

Evidence status. Messaging permission rules follow the WhatsApp Business Messaging Policy (register WHATSAPP-BUSINESS-POLICY, verified 2026-09-19: keep opt-in provenance, honour on- and off-platform opt-outs, use approved templates outside the 24-hour customer-service window, and give automation an escalation path). App limits, field lengths, image sizes and API eligibility below are legacy figures with no register record: verify before stating.

## Why WhatsApp Business matters in East Africa

WhatsApp is the dominant messaging channel in East Africa and the main channel for enquiries, order confirmations, appointment booking and repeat purchase. No source measures WhatsApp's share of smartphone users in Uganda, Kenya, Tanzania or Rwanda, so state no percentage unless it is a named, dated figure with its base, and check the client's own audience data. The best-attributed figures are Pew's 2023 adult survey (8-country median 73%, Kenya inferred below 90%) and Yazi's unattributed estimates of about 95% of internet users in Kenya and Uganda (register WHATSAPP-USAGE-EA-2026, Kaizen items WA-01, WA-02, WA-04). Businesses that run WhatsApp professionally, with consistent branding, fast responses and a structured catalogue, outperform those using a personal number informally (legacy claim; verify before stating).

## Inputs

| # | Input | Notes |
|---|---|---|
| 1 | Business name | Trading name |
| 2 | Industry | Sector and niche, for example retail / women's fashion; professional services / accounting |
| 3 | Country / city | Default Uganda/East Africa |
| 4 | Primary goal | Increase sales, reduce response time, manage enquiries or build a loyal customer base |
| 5 | Current WhatsApp usage | Personal number used for business, WhatsApp Business app, or WhatsApp Business Platform (API) |
| 6 | Team size | People who will answer messages |
| 7 | Catalogue | List or description of what the business sells |

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| One or two people answer messages | WhatsApp Business app (free) | Paying for tooling the volume does not need |
| Automation at scale, or three or more people answering | WhatsApp Business Platform (API) through a verified business and an approved Business Solution Provider, with a multi-agent inbox (legacy threshold; verify eligibility and pricing) | Shared-phone bottlenecks and missed messages |
| More than one person but staying on the app | Shared device run by a designated daily lead | Unowned conversations |
| Number about to be promoted anywhere | Configure greeting, away message and quick replies, and test them first | Unanswered first contact |
| Number about to be publicised | Document the service protocol first | Inconsistent, missed and delayed responses |
| Contact has not opted in or initiated contact | Do not add to any broadcast list | Unsolicited messaging; policy breach (WHATSAPP-BUSINESS-POLICY) |
| Complaint arrives | Move it to a private direct conversation within one message; never handle a dispute in a group | Public escalation |
| Price changes | Update the catalogue within 24 hours | Lost trust and time spent correcting prices in chats |
| Refund, payment dispute or legal issue | Escalate per the table in § Customer service protocol | Substantive engagement on matters that need a person or management |

## Procedure

### 1. Account set-up

Complete every field; an incomplete profile signals an untrustworthy operator.

| Field | Standard |
|---|---|
| Business name | Full legal or trading name, no abbreviations |
| Category | Most accurate available category |
| Description | Under 256 characters (verify current limit); primary service and location, for example "Kampala-based accounting firm specialising in SME tax returns and bookkeeping. Mon–Fri, 8am–6pm EAT." |
| Website URL | Business website or link-in-bio page |
| Email address | Business, not personal |
| Physical address | If there is a walk-in location |
| Business hours | Accurate; update as soon as they change |

Profile photo: at least 640×640px; logo on a clean background with no text overlay or promotional messaging; recognisable at thumbnail size (about 48×48px in the chat list per this source; the parent skill gives 50×50px; verify); consistent with other platforms.

### 2. Automated messages

Configure all three before promoting the number, then test each by messaging the business number from a personal number.

- **Greeting** (first message from any new contact): introduce the business, confirm receipt, set a response-time expectation.
  > Welcome to [Business Name]! Thank you for reaching out. Our team responds within 2 hours during business hours (Monday–Friday, 8am–6pm EAT). How can we help you today?

  Adapt by sector: a clinic adds "If this is a medical emergency, please call [number] or visit the nearest hospital immediately."
- **Away message** (outside business hours): acknowledge, say when the reply will come, offer self-service where possible.
  > Thank you for contacting [Business Name]. Our office is currently closed. We respond to all enquiries by [time] on the next working day. For immediate information about our services, visit [website/link-in-bio]. We look forward to speaking with you.
- **Quick replies**: at least 10, each with a keyboard shortcut. This source's library extends the parent skill's 5–8-shortcut set with `/catalogue`, `/return` and `/social`.

  | Trigger | Reply content |
  |---|---|
  | /price | Pricing or catalogue link |
  | /location | Physical address and Google Maps link |
  | /hours | Business hours |
  | /order | How to place an order |
  | /delivery | Delivery areas and timeframes |
  | /pay | Payment methods (mobile money, bank, cash) |
  | /contact | Alternative contact details |
  | /catalogue | Catalogue or price-list link |
  | /return | Returns and refund policy |
  | /social | Links to other social profiles |

### 3. Broadcast lists

Each recipient gets the broadcast as an individual message and cannot see other recipients.

- Legacy app limit: 256 contacts per broadcast list (verify before stating).
- A contact receives broadcasts only if the business number is saved in their phone.
- All broadcasts are opt-in: get explicit consent before adding anyone; never add a contact who has not first initiated contact. Keep opt-in records (WHATSAPP-BUSINESS-POLICY).

| List | Criteria |
|---|---|
| Leads | Enquired, not yet purchased |
| Active Customers | Purchased within the past 90 days |
| Lapsed Customers | Last purchase more than 90 days ago |
| VIP / High Value | Repeat or high-spend customers |
| Location: [City] | Contacts in one area, for event or delivery messages |

This source draws the active/lapsed line at 90 days; the parent skill's segments use 60 days. Pick one per client from its purchase cycle and state it.

Frequency and mix: at most 2 promotional broadcasts a week (stricter than the parent skill's ceiling of 3); no limit on transactional messages (order confirmations, appointment reminders, delivery updates); content ratio 70% value (tips, product education, news, community updates) to 30% promotional (offers, new products, invitations to buy), tracked each month. Outside the 24-hour customer-service window, Platform (API) messages need approved templates (WHATSAPP-BUSINESS-POLICY).

### 4. Catalogue

The catalogue is a browsable listing reachable from the profile and shareable in chats.

| Field | Standard |
|---|---|
| Name | Clear, searchable product or service name |
| Description | Under 256 characters (verify); key specifications or differentiators |
| Price | Local currency (UGX, KES, TZS, etc.); never blank |
| Product code | A code for quick reference in conversation |
| Image | High-quality photograph, at least 640×640px, product only, no busy background |

This source says never leave a price blank; the parent skill allows "contact for pricing" where prices are not public. Record the client's choice. Update within 24 hours of any price change. Share the catalogue link in the profile, in every new enquiry conversation and in broadcasts to the Leads list.

### 5. Customer service protocol

- Response SLA: in business hours, first response within 2 hours and resolution or escalation within 4 hours; out of hours, the away message promises a next-day reply and the team honours it.

| Enquiry type | On WhatsApp | Escalate to |
|---|---|---|
| Product/pricing enquiry | Resolve | — |
| Order confirmation | Resolve | — |
| Delivery complaint | Attempt; escalate if unresolved in one exchange | Phone call |
| Refund or payment dispute | Begin, then escalate immediately | Phone call or in person |
| Legal or regulatory issue | Acknowledge only; do not engage on substance | Management |

Complaint rule: move to a private direct conversation within one message; acknowledge, empathise and offer a specific resolution, not a generic apology.

### 6. Team management

For more than one person on WhatsApp, use the app on a shared device run by a designated team member, or move to the Platform (API) with a multi-agent inbox. Name one daily WhatsApp lead accountable for response times; rotate the lead weekly for teams of two or more; log every unresolved enquiry in a shared tracker (a simple Google Sheet works for most EA SMEs) before handover.

## Output: WhatsApp Business set-up brief

1. **Business profile copy**: description, category and hours, written to the character limit.
2. **Automated messages**: greeting, away message and a library of 10 quick replies.
3. **Broadcast list structure**: list names, criteria and a 4-week broadcast calendar (use the 30-day calendar and templates in [whatsapp-channel-playbook.md § 7](whatsapp-channel-playbook.md)).
4. **Catalogue entry template**: blank, with every required field for the client to fill.
5. **Customer service protocol**: SLA, escalation path and complaint rule.
6. **Team rota template**: if more than one person manages WhatsApp.

## Release checklist

- [ ] Profile complete (name, description, hours, website, email, photo); no field blank or approximate.
- [ ] All three automated messages configured and tested from a personal number before any promotion.
- [ ] Broadcast lists segmented with documented opt-in records; every contact initiated contact or consented.
- [ ] Catalogue complete and current, each item priced (or the client's recorded "contact for pricing" choice) with an image, before marketing drives traffic.
- [ ] SLA defined, told to every team member and checked weekly, not assumed.
- [ ] Escalation path documented; the team knows which cases leave WhatsApp at once.
- [ ] 70/30 value-to-promotion ratio tracked each calendar month.
- [ ] App limits and API eligibility verified or labelled; policy points traced to WHATSAPP-BUSINESS-POLICY.

## Sources

- Pidsley, R. (2023) *Social Media Marketing for Business: Scaling an Integrated Social Media Strategy Across Your Organisation*, Kogan Page.
- Registers: WHATSAPP-BUSINESS-POLICY; WHATSAPP-USAGE-EA-2026.

## Where the parent skill's figures now live

Added in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`). The "parent skill" figures compared above (60-day segments, the ceiling of 3 broadcasts a week, "contact for pricing", the 50×50px thumbnail, the 5–8 quick replies, the 30-day calendar and templates) moved, text unchanged, from `SKILL.md` to [whatsapp-channel-playbook.md](whatsapp-channel-playbook.md).

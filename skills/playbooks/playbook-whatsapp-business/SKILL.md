---
name: playbook-whatsapp-business
description: Use when designing or improving a Whatsapp Business operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# WhatsApp Business Operations Playbook

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Whatsapp Business workflow for a client or delivery team.
- Turn an approved objective into roles, controls, handoffs and measurable actions.

## Do Not Use When
- The task is a single-channel presence plan; use the closest `platform-*` skill.
- The task is upstream positioning or channel choice; use the closest `strategy-*` skill.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience and success measure | Approved client brief or accountable owner | Yes | Stop and request the missing decision |
| Current workflow, assets and performance evidence | Team records, platform exports or supplied artefacts | Conditional | Label the baseline unassessed and use a minimum viable workflow |
| Roles, budget, timing and approval limits | Delivery owner | Yes for execution | Produce a draft only; do not schedule, spend or publish |

## Capability and Permission Boundaries
Read supplied artefacts and search relevant evidence. Treat review, audit and planning as read-only. Editing the requested draft is allowed; publishing, messaging, production changes, personal-data processing, spending, destructive actions and certification claims require explicit authority. Use network access only for authorised verification.

## Degraded Mode
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Whatsapp Business playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A workflow needs structured service rather than promotion | Use labels, templates and escalation before broadcasts | Marketing noise overwhelming customer care |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Whatsapp Business playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Whatsapp Business playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
| Assumption and gap register | Approver or next workflow | Every missing source, unassessed check and required approval has an owner or next action |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and verification record | Inline table or appendix | Each material choice traces to an input, source or labelled assumption |
| Release-gate result | Completed checklist | No blocking policy, factual, permission or anti-slop finding remains |

## Quality Standards
Use British English and the specified market context. Recommendations must be executable with the stated capacity, current claims must be verified or qualified, and acceptance conditions must be observable. A worked example must use a labelled scenario, not fabricated client evidence.

## Anti-Patterns
- Inventing a client fact, benchmark, budget or approval. Fix: cite the source or label the assumption and its effect.
- Copying one channel or client pattern unchanged. Fix: tie each choice to the named audience, objective and evidence.
- Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim.
- Treating an inaccessible account, file or metric as healthy. Fix: mark it `not assessed` and bound the conclusion.
- Publishing, spending, messaging or changing production state from planning authority. Fix: obtain explicit action authority.
- Delivering actions without owner, timing or acceptance. Fix: assign all three or return the item as an unresolved gap.

## References
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- [East African English standard](../../language/east-african-english/SKILL.md)
- Use the directly cited sources and companion skills in the domain guidance below; verify time-sensitive claims before use.
<!-- dual-compat-end -->

## Required Inputs

Ask for the following before generating any output:

1. **Business name** — trading name of the client
2. **Industry** — sector and niche (e.g. retail / women's fashion; professional services / accounting)
3. **Country / city** — default is Uganda/East Africa
4. **Primary goal** — what WhatsApp Business must achieve (increase sales, reduce response time, manage enquiries, build a loyal customer base)
5. **Current WhatsApp usage** — personal number used for business, existing WhatsApp Business account, or WhatsApp Business API
6. **Team size** — number of people who will manage WhatsApp responses
7. **Product or service catalogue** — list or description of what the business sells

---

## Why WhatsApp Business Matters for East Africa

WhatsApp is used by 90%+ of smartphone users in Uganda and across East Africa. It is the primary channel for customer enquiries, order confirmations, appointment booking, and repeat purchase. Businesses that manage WhatsApp professionally — with consistent branding, fast response times, and a structured catalogue — consistently outperform those using it informally from a personal number.

The WhatsApp Business app (free) is suitable for businesses with one or two team members managing conversations. The WhatsApp Business API (requires a verified business and an approved Business Solution Provider) is required for automation at scale and for teams of three or more.

---

## Account Setup

Complete every field. An incomplete business profile signals an untrustworthy operator to new contacts.

**Business profile requirements:**

| Field | Standard |
|---|---|
| Business name | Full legal or trading name — no abbreviations |
| Category | Select the most accurate available category |
| Description | Under 256 characters; include the primary service and location (e.g. "Kampala-based accounting firm specialising in SME tax returns and bookkeeping. Mon–Fri, 8am–6pm EAT.") |
| Website URL | Link to the business website or link-in-bio page |
| Email address | Business email, not personal |
| Physical address | Include if the business has a walk-in location |
| Business hours | Set accurate hours; update immediately when hours change |

**Profile photo:**
- Minimum 640×640px
- Logo on a clean background — no text overlay, no promotional messaging
- Recognisable at thumbnail size (approximately 48×48px in the chat list)
- Consistent with branding on all other platforms

---

## Automated Messaging Configuration

Configure all three automated message types before promoting the WhatsApp number on any platform.

### Greeting Message
Sent to any new contact on their very first message. Must do three things: introduce the business, confirm receipt, and set response time expectations.

**Template:**
> Welcome to [Business Name]! Thank you for reaching out. Our team responds within 2 hours during business hours (Monday–Friday, 8am–6pm EAT). How can we help you today?

Customise for industry — a clinic might add: "If this is a medical emergency, please call [number] or visit the nearest hospital immediately."

### Away Message
Activated automatically outside business hours. Must acknowledge the enquiry, state when the customer will receive a response, and provide a self-service option where available.

**Template:**
> Thank you for contacting [Business Name]. Our office is currently closed. We respond to all enquiries by [time] on the next working day. For immediate information about our services, visit [website/link-in-bio]. We look forward to speaking with you.

### Quick Replies
Set up a minimum of 10 quick replies for the most common enquiries. Assign a keyboard shortcut trigger to each (e.g. /price, /location, /hours, /order, /delivery).

**Recommended quick replies for most EA businesses:**

| Trigger | Reply Content |
|---|---|
| /price | Pricing information or link to catalogue |
| /location | Physical address and Google Maps link |
| /hours | Business hours |
| /order | How to place an order |
| /delivery | Delivery areas and timeframes |
| /pay | Payment methods accepted (mobile money, bank, cash) |
| /contact | Alternative contact details |
| /catalogue | Link to product catalogue or price list |
| /return | Returns and refund policy |
| /social | Links to other social media profiles |

---

## Broadcast Lists

Broadcast lists allow a message to be sent to multiple contacts simultaneously. Each recipient receives it as an individual message — they do not see other recipients.

**Key constraints:**
- Maximum 256 contacts per broadcast list (WhatsApp Business app limit)
- A contact must have the business number saved in their phone to receive broadcasts — they will not receive the message if the business number is not in their contacts
- All broadcasts must be opt-in. Obtain explicit consent before adding any contact to a broadcast list. Never add a contact who has not initiated contact first.

**Segmentation model:**

| List Name | Criteria |
|---|---|
| Leads | Enquired but not yet purchased |
| Active Customers | Purchased within the past 90 days |
| Lapsed Customers | Last purchase more than 90 days ago |
| VIP / High Value | Repeat purchasers or high-spend customers |
| Location: [City] | Contacts in a specific geographic area (for event or delivery comms) |

**Broadcast frequency and content ratio:**
- Maximum 2 broadcasts per week for promotional content
- No limit on transactional broadcasts (order confirmations, appointment reminders, delivery updates)
- Content ratio: 70% value (tips, product education, news, community updates), 30% promotional (offers, new products, invitations to purchase)

---

## Product Catalogue

The WhatsApp Business catalogue is a browsable product or service listing accessible directly from the business profile and shareable in individual conversations.

**Catalogue entry requirements:**

| Field | Standard |
|---|---|
| Name | Clear, searchable product or service name |
| Description | Under 256 characters; include key specifications or differentiators |
| Price | Display in local currency (UGX, KES, TZS, etc.); never leave price blank |
| Product code | Assign a code for easy reference in conversation |
| Image | High-quality photograph; minimum 640×640px; product only, no busy backgrounds |

**Maintenance rule:** Update the catalogue within 24 hours of any price change. Out-of-date pricing displayed in the catalogue destroys trust and wastes the sales team's time managing corrections in individual conversations.

Share the catalogue link in:
- The business profile bio
- Every new enquiry conversation
- Broadcast messages to the Leads segment

---

## Customer Service Protocol

Define and document the service protocol before the WhatsApp number is publicised. A number without a protocol becomes a source of inconsistent, missed, and delayed responses.

**Response time SLA:**
- During business hours: first response within 2 hours; resolution or escalation within 4 hours
- Out of hours: away message confirms next-day response; honour the commitment

**Escalation path:**

| Enquiry Type | WhatsApp Resolution | Escalate To |
|---|---|---|
| Product/pricing enquiry | Resolve via WhatsApp | — |
| Order confirmation | Resolve via WhatsApp | — |
| Delivery complaint | Attempt via WhatsApp; escalate if unresolved in one exchange | Phone call |
| Refund or payment dispute | Begin via WhatsApp; escalate immediately | Phone call or in-person |
| Legal or regulatory issue | Acknowledge via WhatsApp; do not engage substantively | Management |

**Complaint resolution rule:** Move any complaint to a private, direct conversation within one message. Never attempt to resolve a dispute in a group chat. Acknowledge, empathise, and offer a specific resolution — not a generic apology.

---

## Team Management

For businesses with more than one person managing WhatsApp, use WhatsApp Business on a shared device managed by a designated team member, or upgrade to the WhatsApp Business API with a multi-agent inbox tool.

**Team protocol:**
- Assign one person as the daily WhatsApp lead responsible for response time compliance
- Rotate the WhatsApp lead on a weekly schedule for teams of two or more
- Log any unresolved enquiry in a shared tracker (a simple Google Sheet works for most EA SMEs) before handing over to the next team member

---

## Output: WhatsApp Business Setup Brief

Generate the following for the client:

1. **Business profile copy** — description, category, and hours pre-written to the character limit
2. **Three automated messages** — greeting, away, and a library of 10 quick replies
3. **Broadcast list structure** — segment names, criteria, and a 4-week broadcast content calendar
4. **Catalogue entry template** — a blank template with all required fields for the client to populate
5. **Customer service protocol** — response time SLA, escalation path, and complaint handling rule
6. **Team rota template** — if the client has more than one team member managing WhatsApp

---

## Quality Criteria

Output meets the standard when:

1. Business profile is fully completed — name, description, hours, website, email, profile photo — with no field left blank or approximate
2. All three automated messages are configured, tested by sending a message from a personal number to the business number, and confirmed as triggering correctly before any promotion begins
3. Broadcast lists are segmented by audience type with documented opt-in records — every contact on every list has explicitly initiated contact or provided consent
4. Product catalogue is complete and up to date — every product or service is listed with a price and image before any marketing activity drives traffic to the WhatsApp number
5. Response time SLA is defined, communicated to every team member, and monitored weekly — not assumed to be happening
6. Escalation path is documented for complaints and complex enquiries — the team knows which situations must move off WhatsApp immediately
7. Broadcast content ratio is maintained at 70% value, 30% promotional — tracked across each calendar month

---

## Reference

Pidsley, R. (2023) *Social Media Marketing for Business: Scaling an Integrated Social Media Strategy Across Your Organisation*. Kogan Page.

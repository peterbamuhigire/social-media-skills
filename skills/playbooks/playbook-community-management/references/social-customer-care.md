# Social Customer Care

Merged from skills/playbooks/playbook-social-customer-service on 2026-09-29 at ce3299a; preservation map: [playbook-social-customer-service.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/playbook-social-customer-service.md)

## When to use this reference

Read this reference when the community-management work is mainly a customer-service operation run through social inboxes: WhatsApp, Messenger and public comments used for complaints, enquiries and bookings, often handled by junior staff or interns without formal training. It adds SLAs by business size, three service metrics, a five-way query triage, a public-to-private escalation protocol, complaint scripts, a saved-replies library, an empathy language guide, out-of-hours cover, staff training and a monthly service review. [community-response-guide.md](community-response-guide.md) keeps the platform SLA table, scenario templates, client escalation protocol, negative-review process and community health scorecard; where both give a figure, use the stricter one unless the client sets its own.

Where an issue needs personal or transaction data, move it to an approved private channel and collect the minimum needed; public disclosure of customer data is the failure to avoid. Drafting scripts does not authorise sending them.

Evidence status. SLA times and business-hours defaults are internal service targets set by the client, not platform rules. Platform response badges and their thresholds change: verify before stating (no register record). WhatsApp messaging follows the WhatsApp Business Messaging Policy (register WHATSAPP-BUSINESS-POLICY: keep opt-in provenance, honour opt-outs, approved templates outside the 24-hour customer-service window, escalation paths for automation).

## Context: customer service on social in Uganda and East Africa

In Uganda and across East Africa, customers use WhatsApp, Facebook Messenger and public Facebook/Instagram comments as primary channels for complaints, enquiries and bookings; email and formal telephone support are secondary. Volume is high, turnaround expectations are short, and poor responses are routinely screenshotted and shared publicly. Many clients hand social inboxes to junior staff or interns without training; this reference closes that gap with processes, ready scripts and an escalation structure. Facebook availability in Uganda: follow register UG-FACEBOOK-ACCESS-2026 (reported unblocked from 13 June 2026, official status not assessed); check the client's own channel data rather than asserting Facebook reach.

## Inputs

| # | Input | Notes |
|---|---|---|
| 1 | Client business name | Trading name as it appears on social media |
| 2 | Industry | For example retail, F&B, logistics, hospitality, professional services |
| 3 | Country / city | Default Uganda |
| 4 | Primary goal | Reduce complaint escalations, reduce response time, train new staff, or build a saved-replies library |
| 5 | Business size | Small (1–2 staff on socials), medium (3–10), large (dedicated customer-service team) |
| 6 | Active channels | Which of WhatsApp, Facebook Page, Instagram, Messenger, X/Twitter are in use |
| 7 | Current pain points | For example slow replies, staff not knowing what to say, public complaints unanswered, abusive customers |

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| Message arrives | Classify with the triage table before typing | Wrong response path |
| Unsure whether Complaint or Crisis-trigger | Treat as Crisis-trigger until a manager confirms otherwise | Under-reacting to a crisis |
| Crisis-trigger (harm allegation, food safety, viral negative post, legal threat) | Stop; no response without management sign-off; hand to [playbook-crisis-communications](../../playbook-crisis-communications/SKILL.md) | Casual reply that worsens harm |
| Investigation needed before an answer | Send a holding reply within SLA; resolve second | Silence read as indifference |
| Complaint unanswered beyond double the SLA | Escalate to a supervisor before responding | A careless late reply |
| Personal details, investigation, rising emotion, or refund/compensation/policy exception | Move from public to DM or WhatsApp after a public acknowledgement | Data exposure; public escalation |
| Abuse continues after one firm-close reply and one further attempt | Document, block or restrict, stop responding, log in the monthly tracker | Endless public argument |
| Staff member cannot find the answer within 10 minutes | Escalate to management | Guessing |
| Same customer complains more than twice about the same issue | Escalate to management | Repeat failure |

## Procedure

### 1. Set response SLAs by platform and business size

Define and publish SLAs internally; post expected response times in the Page bio or WhatsApp Business profile.

| Platform | Small business | Medium business | Large business |
|---|---|---|---|
| WhatsApp | Within 1 hour (business hours) | Within 1 hour | Within 30 minutes |
| Facebook Messenger | Within 2 hours | Within 2 hours | Within 1 hour |
| Public comments (Facebook/Instagram) | Within 3 hours | Within 2 hours | Within 1 hour |
| X/Twitter mentions | Within 4 hours | Within 3 hours | Within 2 hours |

Business-hours default (Uganda): Monday–Friday 08:00–18:00 EAT; Saturday 08:00–14:00 EAT. (The parent SKILL.md example uses Monday–Friday 08:00–17:30; use the client's actual hours.)

Rules:
- Acknowledge first, resolve second. A holding reply within SLA beats silence while you investigate.
- Weekends and public holidays: set auto-replies and nominate one on-call staff member for urgent complaints.
- If a complaint has gone unanswered beyond double the SLA, escalate to a supervisor before responding; the response now needs more care.

### 2. Track three core service metrics

Source: Macarthy (2023) *500 Social Media Marketing Tips*. Track monthly for every active channel:

1. **Queries by channel (volume tracker).** Count incoming messages and comments by platform and by query type (triage below). Shows where volume is highest and where to focus training or automation.
2. **Speed of first reply.** Average time from message received to first response sent. Some platforms display a public responsiveness badge; the source cites Facebook's "Very responsive" badge as 90%+ of messages answered within 15 minutes, reachable with an auto-reply (verify the current badge rule before stating; no register record).
3. **Resolution rate.** Percentage of queries fully resolved without the customer needing to follow up. Log outcomes as Resolved / Escalated / Unresolved / No response needed. A low rate signals script gaps or staff knowledge deficits.

Record them in a simple monthly spreadsheet tracker and review at the monthly customer-service meeting.

### 3. Triage every incoming message

| Type | Definition | Response path |
|---|---|---|
| **Enquiry** | Product information, pricing, availability, booking, operating hours | Answer directly; use a saved reply where one applies |
| **Complaint** | Negative experience with product, delivery, staff or service | Acknowledge, apologise, investigate, resolve; escalate if unresolved |
| **Compliment** | Positive feedback, praise, thanks | Acknowledge warmly; amplify where appropriate (script 5) |
| **Abuse** | Threatening, discriminatory or deliberately disruptive messages | Firm-close script; do not engage further; document and block if repeated |
| **Crisis-trigger** | Allegation of harm, food-safety issue, viral negative post, legal threat | Stop. No response without management sign-off. Hand to playbook-crisis-communications immediately |

### 4. Escalate from public to private without appearing defensive

Move a public comment to DM or WhatsApp when:
- the customer is sharing personal information (order number, phone number, address);
- the complaint needs investigation that one reply cannot resolve;
- emotion is escalating and continued public exchange risks amplifying the situation;
- the resolution involves compensation, a refund or an exception to policy.

Post a brief, empathetic public reply first; never disappear into DM without acknowledging publicly:

> "Thank you for reaching out, [Name]. We are sorry to hear about your experience. We want to look into this properly for you — please send us a direct message / WhatsApp us on [number] with your order details so we can resolve this as quickly as possible."

This shows other readers that the business has responded and is taking the matter seriously, does not admit fault, and moves the detail off the public thread.

Never:
- delete a legitimate complaint comment (screenshotting is immediate);
- ask a customer to "email us" — they will not, and in the East African context it reads as dismissive;
- move to private without any public acknowledgement.

### 5. Use the complaint-handling scripts

The scripts and templates below are engine house wording, not quotations; adapt before use. Adapt every script to the brand voice. Use "we" throughout, never "the company" or third-person references to the team.

**Script 1 — Product complaint (public comment)**
> "We are sorry to hear this, [Name] — this is not the experience we want for you at all. Please send us a direct message with your contact details and a brief description of what happened, and we will sort this out for you right away. Thank you for letting us know."

**Script 2 — Delivery/order complaint (Messenger or WhatsApp)**
> "Hello [Name], thank you for getting in touch. We sincerely apologise for the delay/issue with your order. Could you please share your order number or the phone number used to place the order? We will investigate immediately and get back to you within [X hours] with an update. We appreciate your patience."

After investigation:
> "Hello [Name], we have looked into your order and [explain what happened briefly and honestly]. We [state resolution: resend / refund / discount / apology]. We are truly sorry for the inconvenience. Please let us know if there is anything else we can do."

**Script 3 — Unresolved repeat complaint** (customer returns with the same issue unresolved)
> "Hello [Name], we are very sorry that this issue has not yet been fully resolved — you should not have had to come back to us about this. I am personally escalating your case to our [manager/supervisor] right now. You will receive a direct call/message from us within [X hours]. Thank you for your continued patience, and we will make this right."

**Script 4 — Unreasonable or abusive customer (firm close).** Do not match the customer's tone; respond once, clearly and professionally.
> "Hello [Name], we understand you are frustrated and we take all feedback seriously. However, we are not able to continue this conversation while it includes [threatening/offensive language]. We are still happy to assist you respectfully — please message us again and a member of our team will respond. Thank you."

If abuse continues after one further attempt: document the exchange, block or restrict the account, stop responding and note it in the monthly tracker.

**Script 5 — Positive feedback (acknowledge and amplify)**
> "Thank you so much, [Name] — this genuinely made our day! We are so glad you [enjoyed the product / had a great experience / loved the service]. We will pass this on to the team. We look forward to seeing you again soon!"

Amplify only with the customer's permission, for example as a testimonial on Stories or the feed. Ask: "We would love to share your kind words — are you happy for us to repost this?"

### 6. Build the saved-replies library

Cover the 10 most common query types for the client, stored in WhatsApp Business, Facebook Business Suite (now Meta Business Suite) or a shared Google Doc for staff to copy quickly. Adapt to the industry:

1. Pricing / quotation request
2. Product availability / stock check
3. Delivery timeframe and area
4. Order status update
5. Returns / refund policy
6. Booking / reservation confirmation
7. Operating hours and location
8. Complaint acknowledgement (holding reply)
9. Out-of-stock / waitlist notification
10. General "thank you for your message" acknowledgement

Worked examples (labelled scenario; replace hours, areas and couriers with the client's facts):

- **Operating hours:** "Hello! Thank you for your message. We are open Monday to Friday, 8am–6pm, and Saturday 8am–2pm. We are closed on Sundays and public holidays. Feel free to place your order or ask your question here and we will respond as soon as we open. Thank you!"
- **Delivery timeframe:** "Hello [Name]! Thank you for your order. We deliver within Kampala within 24–48 hours of order confirmation. Orders outside Kampala are dispatched within 48 hours via [courier name]. We will send you a confirmation message once your order is on its way. Thank you for shopping with us!"
- **Complaint acknowledgement (holding reply):** "Hello [Name], thank you for getting in touch. We are sorry to hear about your experience and we want to resolve this as quickly as possible. Could you please share your order number / booking reference? We are looking into this now and will update you within [2 hours]. We appreciate your patience."

### 7. Apply the empathy language guide (East African context)

Ugandan and East African customers respond well to warmth, directness and respect; corporate coldness, deflection and over-formal language read as dismissive.

| Use | Not |
|---|---|
| "We are sorry" | "We apologise for any inconvenience caused" |
| "We will sort this out for you" | "Your query has been escalated to the relevant department" |
| "Thank you for telling us" | "We note your feedback" |
| "We understand this is frustrating" | "We regret any perceived service failure" |

Also use first names where known, and "we" throughout (you are the business, not a separate entity).

Avoid: passive voice that hides responsibility ("mistakes were made"); jargon or policy-speak ("as per our terms and conditions"); promises you cannot keep ("this will never happen again"); over-apologising without a resolution ("So sorry! So sorry! So sorry!"); emojis in complaint handling (acceptable in compliment replies, not in apologies).

Tone calibration: warm and competent — a trusted person helping a neighbour, not a call-centre script.

### 8. Cover out-of-hours

Configure an auto-reply on WhatsApp Business and Facebook that confirms receipt, states business hours, gives an expected response time and provides an emergency contact for genuinely urgent matters (for example a perishable delivery or a safety issue).

> "Hello! Thank you for messaging [Business Name]. Our team is currently offline — we are available Monday–Friday, 8am–6pm, and Saturday, 8am–2pm EAT. We will respond to your message as soon as we open. If your matter is urgent, please call [number]. Thank you for your patience!"

Urgent out-of-hours complaints:
- Nominate one on-call staff member per week for urgent messages only.
- Define "urgent" as a complaint that, if not acknowledged, will generate public escalation before morning (for example a public comment gaining traction, or an undelivered order for a vulnerable customer).
- On-call staff send a brief holding reply only; no investigation or resolution out of hours unless they have the authority and information to resolve it.

### 9. Train staff

Brief new team members on five points:
1. **Triage first** — classify before you type, using the five categories.
2. **Never delete a legitimate complaint** — hide the comment if necessary while you investigate (the source notes that a hidden comment is no longer visible to the public; verify current platform behaviour), but do not delete. Screenshot before hiding.
3. **Never argue publicly** — if a customer is wrong, correct gently and privately.
4. **Know your escalation trigger** — any mention of illness, injury, legal action, or a post gaining rapid shares goes to a manager immediately; do not resolve it alone.
5. **Stay in role** — personal opinions, humour and off-script language do not belong in the service inbox; when in doubt, use a saved reply.

Staff must never say, in any channel or format:
- "That is not our fault" / "You should have…" / "Read the terms and conditions";
- "I cannot help you with that" without offering an alternative;
- anything implying the customer is lying;
- information about internal processes, staff names or supplier details;
- any commitment to a refund or compensation without manager authorisation.

Escalate to management when: the complaint involves a potential health or safety issue; the customer threatens legal action or a media complaint; a post is gaining shares or comments at an unusual rate; the staff member cannot find the answer within 10 minutes; or the same customer has complained more than twice about the same issue.

### 10. Run the monthly customer-service review

Hold a 30-minute review at month end, using the three core metrics as baseline.

Track:
- total query volume by channel and by type (Enquiry / Complaint / Compliment / Abuse / Crisis-trigger);
- average speed of first reply per channel;
- resolution rate (percentage fully resolved at first contact);
- number of escalations to management;
- number of repeat complaints (same customer, same issue);
- any complaints that went public or were shared before resolution.

Identify recurring issues: which product, service or process generated most complaints; any pattern (same day, time, delivery route or product); query types staff are consistently unsure about (add a saved reply).

Feed insights back: share recurring complaint themes with product, operations or service delivery as diagnostic data, not blame; update saved replies for new common query types; update staff training for recurring staff errors; adjust SLAs if volume has outgrown capacity.

Output: a one-page summary with the top three complaint themes, average response time against SLA, resolution rate, and one recommended process improvement for the next month. Feed the headline figures into the [community-response-guide.md § 6. Monthly Community Health Scorecard](community-response-guide.md).

## Release checklist

1. **Immediately operational** — a junior staff member with no prior training can follow the triage, pick the right script and handle the common query types without extra guidance.
2. **Reflects East African channel reality** — WhatsApp and Facebook are treated as primary service channels, with scripts and SLAs calibrated to them (subject to the register note on Facebook in Uganda).
3. **Warm, direct language** — scripts read as human, respectful and on-brand; no corporate deflection, passive voice or empty apology loops.
4. **Clear escalation paths** — the boundary between what a junior staff member handles and what goes to management is unambiguous at every point.
5. **Full triage spectrum** — Enquiry, Complaint, Compliment, Abuse and Crisis-trigger each have a defined path.
6. **Measurable** — the three core metrics are defined, tracked and reviewed monthly so the client can show improvement.
7. **Protects the brand publicly** — the public-to-private protocol and the never-delete rule are applied consistently.
8. **Feeds insight upstream** — recurring service issues reach product or operations, not only the social media manager.

## Sources

- Macarthy, A. (2023) *500 Social Media Marketing Tips* (year as given in the source skill; the engine elsewhere cites the 2022 6th edition — verify edition before citing; publisher not recorded).
- WhatsApp Business Messaging Policy — register WHATSAPP-BUSINESS-POLICY.
- Facebook access in Uganda — register UG-FACEBOOK-ACCESS-2026.

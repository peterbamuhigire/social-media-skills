---
name: playbook-sms-whatsapp-marketing
description: Generates a complete narrowcast marketing playbook covering WhatsApp campaign strategy (broadcast lists, automated sequences, catalogue marketing) and SMS marketing — the two highest open-rate direct communication channels in East Africa. Invoke when a client needs structured campaign plans, automated message sequences, SMS gateway setup, or a performance framework for WhatsApp or SMS marketing. Builds on platform-whatsapp (app setup and basic broadcast strategy) — read that skill first for the account configuration foundation.
---

# SMS and WhatsApp Marketing Playbook

> **Foundation:** This playbook assumes the WhatsApp Business account is fully configured. If the account is not yet set up, complete the `platform-whatsapp` skill first. That skill covers app setup, catalogue configuration, broadcast list creation, opt-in capture, and the 30-day broadcast calendar. This playbook extends that foundation into campaign strategy, automated sequences, and SMS marketing.

---

## Required Input

Collect the following before generating any campaign deliverable:

- **Client name** and industry
- **Country/city** (default: Uganda/East Africa)
- **Primary campaign objective** — sales / appointments / awareness / retention
- **Contact list size** — WhatsApp and SMS counts separately
- **Current opt-in process** — how contacts are currently added (or "none yet")
- **WhatsApp Business account type** — app (free) or API (paid, via a BSP)
- **Monthly SMS gateway budget** (in UGX or USD)
- **Telecom operators** used by the target audience — MTN Uganda / Airtel Uganda / other

---

## 1. Channel Comparison and Decision Framework

| Channel | Open rate | Best for | Cost | Limitation |
|---|---|---|---|---|
| WhatsApp Broadcast (app) | 85–98% | Existing customers, value content, offers, relationship maintenance | Free (WhatsApp Business app) | Only reaches contacts who have saved the business number; list cap of 256 per broadcast |
| WhatsApp Business API | 85–98% | Automated sequences, lists over 256, CRM integration, triggered messages | Paid — per message, via a Business Solution Provider (BSP) | Requires pre-approved message templates for outbound messages |
| SMS | 90%+ within 3 minutes | Non-smartphone users, transactional alerts, wider reach, guaranteed delivery | Paid — telecom rates in UGX via a gateway provider | 160-character limit per message; no images; no native click tracking |

**Decision framework — apply in order:**

1. List under 256 contacts, manual sending, no automation needed → **WhatsApp Business app** (free, no technical setup).
2. List over 256, or automation and triggers required, or CRM integration needed → **WhatsApp Business API** via a BSP.
3. Reaching non-smartphone users, sending transactional alerts, or needing guaranteed delivery regardless of WhatsApp account status → **SMS**.
4. For highest-value campaigns, use all three in parallel: API for opted-in WhatsApp contacts, SMS as a fallback for non-smartphone or non-WhatsApp contacts.

---

## 2. WhatsApp Broadcast Campaign Strategy

### Campaign Types

| Type | Purpose | Frequency |
|---|---|---|
| Promotional | Limited-time offers, flash sales, seasonal promotions | Max 2× per week; max 4× during a campaign fortnight |
| Educational | Tips, guides, how-to content — value-first, builds trust and list retention | 1–2× per week |
| Transactional | Order confirmations, appointment reminders, payment receipts | Triggered; not counted against broadcast frequency |
| Re-engagement | Win-back messages for contacts silent 60+ days | 3-message sequence, once per quarter per lapsed contact |
| Loyalty | VIP early access, exclusive content, personal thank-you messages | 2× per month for VIP segment |

### The 5-Part Campaign Message Formula

Apply this structure to every broadcast:

1. **Greeting + personalisation** — "Hi [Name]," — always open with the recipient's first name.
2. **Value hook** — lead with the benefit to the recipient, not the brand name. One sentence.
3. **Offer or content** — specific, clear, and limited if promotional. State the price, the saving, or the tip plainly.
4. **One CTA** — a single, unambiguous action: "Reply YES", "Click the link", "Show this message", or "Call us on [number]". Never include two CTAs in one message.
5. **Opt-out line** — "Reply STOP to unsubscribe." Always include. No exceptions.

### 4-Week Broadcast Calendar — Kampala Retail Business

| Week | Day | Time (EAT) | Segment | Type | Message brief |
|---|---|---|---|---|---|
| 1 | Mon | 7am | Prospects | Educational | Tip: how to identify authentic [product category] — positions the brand as a trusted expert |
| 1 | Wed | 12pm | Active Customers | Promotional | Mid-week offer — 15% off a specific product line, valid 48 hours; include catalogue link |
| 1 | Fri | 6pm | VIP | Loyalty | Weekend early-access preview of new stock arriving Monday; reply YES to reserve |
| 2 | Mon | 7am | All | Educational | Industry tip relevant to the audience's daily life — no selling |
| 2 | Wed | 12pm | Prospects | Social proof | One customer result or testimonial (2–3 sentences, first name only); CTA: reply TELL ME MORE |
| 2 | Fri | 6pm | Lapsed | Re-engagement | Message 1: warm re-introduction, one new development, no pressure CTA |
| 3 | Tue | 12pm | Active Customers | Promotional | Back-to-school or seasonal promotion (Jan/Aug); specific product, specific saving, deadline |
| 3 | Thu | 7am | Prospects | Educational | FAQ: answer the single most common objection; CTA: reply for more information |
| 3 | Sat | 10am | All | Seasonal | Weekend greeting tied to a local moment (e.g. Independence Day, Eid, Christmas) — no hard sell |
| 4 | Mon | 7am | Lapsed | Re-engagement | Message 2: exclusive returning-customer offer with a clear expiry date |
| 4 | Wed | 12pm | VIP | Loyalty | Personal thank-you message; loyalty reward (discount or free item) valid until end of month |
| 4 | Fri | 6pm | Active Customers | Promotional | End-of-month flash sale — clear urgency, specific stock level if applicable |

**Timing rationale:** 7am catches the morning commute; 12pm catches lunch; 6pm catches post-work. These three windows produce the highest read rates in the EAT timezone.

---

## 3. WhatsApp Automated Sequences (API)

For clients on WhatsApp Business API via a BSP — recommended EA providers: WATI, Interakt, and Twilio (Twilio has EA-specific pricing). All outbound messages require pre-approved templates.

### Welcome Sequence
*Trigger: new contact sends first message or saves the business number.*

| Message | Timing | Content |
|---|---|---|
| 1 | Immediate | "Hi [Name], welcome to [Business Name]! I'm [Name]. We help [target customer] with [key benefit]. You'll hear from us [frequency] with [content type]. Reply any time — I read every message. Reply STOP to unsubscribe." |
| 2 | Day 2 | "Hi [Name], here's the most useful tip we share with new customers: [one specific, actionable tip]. Save this number so you don't miss future updates. Reply STOP to unsubscribe." |
| 3 | Day 5 | "Hi [Name], [Customer first name] from [city] came to us with [problem]. After [solution], they [result]. If that sounds familiar, reply 'TELL ME MORE' and I'll share exactly how we can help you. Reply STOP to unsubscribe." |
| 4 | Day 7 | "Hi [Name], we'd love to help you with [key offer]. [Specific invitation — e.g. 'Book a free consultation', 'Visit us this week', 'Order online at [link]']. No obligation. Reply STOP to unsubscribe." |

### Abandoned Enquiry Sequence
*Trigger: contact enquired about a product or service but did not purchase within 4 hours.*

| Message | Timing | Content |
|---|---|---|
| 1 | 4 hours after enquiry | "Hi [Name], just checking in — did you get all the information you needed about [product/service]? Happy to answer any questions. Reply STOP to unsubscribe." |
| 2 | Day 2 | "Hi [Name], one thing we hear a lot about [product/service]: '[most common objection].' Here's the honest answer: [2–3 sentence direct response]. Still interested? Reply 'YES' and I'll sort you out. Reply STOP to unsubscribe." |
| 3 | Day 5 | "Hi [Name], [number] people ordered [product/service] this week — it's been popular. [If genuine stock urgency: 'We have [N] remaining.'] If you'd like yours, reply 'ORDER' and I'll walk you through it. Reply STOP to unsubscribe." |

### Re-engagement Sequence
*Trigger: contact has been silent for 60+ days.*

| Message | Timing | Content |
|---|---|---|
| 1 | Day 1 | "Hi [Name], it has been a while — I hope all is well! A lot has changed at [Business Name] recently: [one new development or improvement]. Reply 'HELLO' if you'd like to reconnect. Reply STOP to unsubscribe." |
| 2 | Day 3 | "Hi [Name], as a thank-you for coming back, here's an exclusive offer just for returning customers: [specific offer with expiry date]. Reply 'BACK' to claim it. Reply STOP to unsubscribe." |
| 3 | Day 7 | "Hi [Name], we do not want to fill your inbox unnecessarily. If you'd prefer not to hear from us, reply STOP and we'll remove you immediately — no hard feelings. Otherwise, we'd love to keep in touch. [Business Name]." |

---

## 4. WhatsApp Catalogue Marketing

The catalogue is the WhatsApp Business equivalent of a product page. Use it as a sales tool, not just a reference.

**Catalogue entry setup — required fields for each item:**
- Product or service name (clear, searchable)
- Description: under 200 characters — state the key benefit and one differentiator
- Price (or "Contact us for pricing" if pricing is dynamic)
- Photo: 800×800px, well-lit, clean background, product filling 80% of the frame
- Link: direct URL to a product page, booking form, or ordering mechanism

**How to share the catalogue:**
- In broadcast messages: "Browse our full range here: [catalogue link]"
- In replies to product enquiries: share the specific catalogue item, not just the link
- As a pinned message in customer groups
- Via WhatsApp Status with a swipe-up link (if the account is linked to a Meta Business page)
- In the business profile — the catalogue is the first thing new contacts see when they view the profile

**Seasonal catalogue updates — key EA shopping periods:**

| Period | Timing | Action |
|---|---|---|
| Back-to-school | January and August | Update with school-season relevant products; add seasonal pricing |
| Eid al-Fitr | Varies (lunar calendar) | Highlight gifting options, festive products, special packages |
| Christmas / New Year | December | Festive products, gift bundles, end-of-year promotions |
| Uganda Independence Day | 9 October | National pride promotions; local-angle messaging |
| Valentine's Day | February | Gifting and experiences |

**Catalogue metrics:** check monthly in WhatsApp Business → Business Tools → Catalogue → View stats. Track catalogue views month-on-month; target 10% monthly growth after the first three months.

---

## 5. SMS Marketing Campaign Strategy

SMS reaches non-smartphone users, delivers to any mobile number, and achieves 90%+ open rates within three minutes of sending. Use it for wider reach and guaranteed delivery.

**Recommended gateway for Uganda and East Africa: Africa's Talking** — competitive per-SMS rates for MTN Uganda and Airtel Uganda, a simple API, a USSD module, local support team, and a free sandbox for testing. Alternatives: Beem Africa, Onfon Media, and Twilio (international rates apply).

**Register a branded sender ID** with the telecom operator (e.g. "KampalaSpa" or "ShopABC" rather than a random number). Available from MTN Uganda and Airtel Uganda through their bulk SMS business portals, or automatically through Africa's Talking's sender ID registration process. A branded sender ID increases open rates and prevents messages being marked as spam.

### SMS Message Templates

**Promotional:**
"Hi [Name], [saving or offer in plain language] at [Business Name] this [day/period]. [Product/service] at UGX [price]. Book now: [bit.ly link]. Reply STOP to opt out. [Business Name]"
*(Check character count: keep under 160 for one-message billing.)*

**Appointment reminder:**
"Reminder: Your appointment at [Business Name] is tomorrow, [date] at [time]. Reply YES to confirm or call [number] to reschedule. See you then!"

**Payment reminder:**
"Dear [Name], invoice #[N] of UGX [amount] is due [date]. Pay via MTN MoMo [number] or Airtel Money [number]. Ref: [client name]. Thank you. [Business Name]"

**Flash sale alert:**
"FLASH SALE — [duration, e.g. '3 hours only']. [Product] at UGX [price]. Only [N] remaining. Reply ORDER or call [number]. [Business Name]. Reply STOP to opt out."

**Post-purchase follow-up:**
"Hi [Name], thank you for your purchase from [Business Name]! Your [product/order] is [status]. Questions? Reply here or call [number]. We appreciate your business."

### SMS Writing Rules

- **160 characters** = one SMS, billed as one message. 161–306 characters = two messages, billed as two. Always check the character count before sending.
- Include the **business name in every message** — recipients often do not save business numbers and will not recognise a number-only sender.
- Never abbreviate in a way that reduces professionalism. "u", "ur", and "2moro" are not acceptable in business communications.
- Always include an **opt-out instruction** — "Reply STOP to opt out." This is both ethical practice and a requirement under the Uganda Data Protection and Privacy Act 2019.
- Use a **URL shortener** (bit.ly or Africa's Talking short links) for any links — long URLs consume most of the character allowance and cannot be tracked.

---

## 6. Opt-in and Opt-out Management

**Legal foundation:** Uganda's Data Protection and Privacy Act 2019 requires informed consent before sending marketing communications. Sending marketing messages to individuals without consent is a breach of this Act. Apply these standards to both WhatsApp and SMS lists.

**Opt-in methods:**

| Method | Channel | How to implement |
|---|---|---|
| WhatsApp message opt-in | WhatsApp | "Reply YES to receive our updates." The act of replying is documented consent. |
| QR code at point of sale | WhatsApp + SMS | WhatsApp QR from Business Settings; for SMS, a QR linking to a form |
| Verbal consent at purchase | Both | "May I add you to our updates list? You can unsubscribe any time by replying STOP." Log: date, staff member, customer name. |
| Lead magnet keyword | Both | "Send 'GUIDE' to [number] to receive our free [resource]." The keyword send is the opt-in. |
| Website or landing page form | Both | Form collects name, number, and explicit consent checkbox ("I agree to receive marketing messages") |

**Opt-out process — apply immediately:**
1. Remove the contact from all active lists — same session if possible.
2. Acknowledge: "You have been unsubscribed. You will not receive further messages from us. [Business Name]."
3. Label the contact as "Opted Out" in the system — do not delete the record.
4. Do not re-add the contact to any list without fresh, documented consent.

**List hygiene — quarterly review:**
- Remove all opted-out contacts from every active list.
- Remove numbers that have bounced or shown as undeliverable for 60+ days.
- Move contacts with no opens or responses in six months to a final re-engagement sequence before removing them.

---

## 7. Campaign Performance Metrics

### WhatsApp Metrics (WhatsApp Business app)

| Metric | How to measure | Target |
|---|---|---|
| Delivery rate | Sent ÷ delivered (two grey ticks = delivered) | 95%+ |
| Estimated open rate | Read ÷ delivered × 100 (two blue ticks = read) | 85%+ |
| Reply rate | Replies ÷ sends × 100 | 5–15% for well-targeted broadcasts |
| Conversion rate | Purchases or enquiries ÷ broadcast size × 100 | 2–5% |
| Opt-out rate | STOP replies ÷ sends × 100 | Under 2% per broadcast |
| Catalogue views | Monthly from WhatsApp Business Insights tab | 10% month-on-month growth after Month 3 |

### SMS Metrics (Africa's Talking or gateway dashboard)

| Metric | How to measure | Target |
|---|---|---|
| Delivery rate | Delivered ÷ sent × 100 — visible in gateway dashboard | 95%+ |
| Click rate | Clicks on short link ÷ sends × 100 — use bit.ly or Africa's Talking short links | 2–8% depending on offer relevance |
| Reply rate | Replies ÷ sends × 100 — for interactive SMS campaigns | 1–5% |
| Conversion rate | Attributed purchases or enquiries ÷ SMS recipients × 100 | 1–3% for cold lists; 3–8% for warm lists |
| Cost per conversion | Total gateway spend ÷ conversions | Set a target in Month 1; reduce by 10% per quarter |

### Monthly Reporting Template

Record the following for every campaign:

| Campaign | Channel | Sends | Delivered | Read/Opened | Replied | Converted | Cost (UGX) | Cost per conversion |
|---|---|---|---|---|---|---|---|---|
| [Campaign name] | WhatsApp | — | — | — | — | — | 0 | — |
| [Campaign name] | SMS | — | — | — | — | — | — | — |

---

## Quality Criteria

Output from this skill meets the standard when it:

- Contains complete, ready-to-use message templates — every template requires only name, date, and product substitutions with no placeholder descriptions left in place
- References the Uganda Data Protection and Privacy Act 2019 by name in the opt-in/opt-out section and links consent requirements to both WhatsApp and SMS practices
- Names Africa's Talking as the recommended SMS gateway for Uganda and East Africa with a clear rationale (EA pricing, local support, API quality, sender ID registration)
- Presents the 4-week broadcast calendar with specific days, times in EAT, segment targets, and message types — not just a list of content categories
- Provides a clear, actionable decision framework distinguishing WhatsApp Business app, WhatsApp Business API, and SMS by list size, automation need, and audience type
- Assigns a numerical target to every metric in Section 7 — no metric appears without a benchmark figure
- References `platform-whatsapp` explicitly as the setup foundation and does not duplicate the account configuration or basic broadcast content covered in that skill
- Uses British English throughout — organisation, catalogue, programme, behaviour, enquiry, recognise, analyse — with no American spellings

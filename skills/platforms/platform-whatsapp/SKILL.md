---
name: platform-whatsapp
description: Use when creating a Whatsapp channel plan covering account setup, content, community and measurement for Uganda or East Africa. Use a playbook for cross-channel operations and a strategy skill for channel selection.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# WhatsApp Business Strategy

> **Important:** WhatsApp is not a social media platform in the conventional sense — it is a direct communication channel. All content must be high-value, highly relevant, and permission-based. Spam on WhatsApp destroys trust faster than any other channel. Every message sent must earn its place in the recipient's inbox.

<!-- dual-compat-start -->
## Use When
- Create or revise a Whatsapp-specific presence, growth or publishing plan.
- Translate a confirmed audience, offer and objective into channel decisions.

## Do Not Use When
- The task is cross-channel operating procedure; use the closest `playbook-*` skill.
- The task is choosing channels or business direction; use `strategy-channel-architecture`.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client objective, audience and offer | Approved brief or client interview | Yes | Stop and request the missing decision; do not invent it |
| Current account and content evidence | Native account export, screenshots or supplied audit | Conditional | Mark the account baseline unassessed and qualify recommendations |
| Current platform rules and feature limits | Official Whatsapp help or policy source | Conditional | Omit volatile specifications or flag them for live verification |

## Capability and Permission Boundaries
Read supplied artefacts and search relevant evidence. Treat review, audit and planning as read-only. Editing the requested draft is allowed; publishing, messaging, production changes, personal-data processing, spending, destructive actions and certification claims require explicit authority. Use network access only for authorised verification.

## Degraded Mode
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Whatsapp channel plan plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| Recipients need privacy and one-way updates | Use an opted-in broadcast, not a group | Exposed phone numbers and unwanted discussion |
| Account is absent or not accessible | Produce a setup plan with assumptions labelled | False optimisation against invented history |
| Evidence shows an established account | Prioritise measured gaps and retained strengths | Destructive reset of working assets |
| A rule, limit or feature is time-sensitive | Verify against the official platform source before stating it | Stale platform advice |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Whatsapp channel plan.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Whatsapp channel plan | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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
- [Current-source register](../../../docs/source-registers/README.md)
- [Legal, privacy and market release gate](../../../docs/quality-gates/legal-market-release-gate.md)
- Use the directly cited sources and companion skills in the domain guidance below; verify time-sensitive claims before use.
<!-- dual-compat-end -->

## Required Input

Before generating this strategy, collect the following from the client:

- **Client name** and trading name (if different)
- **Industry** and primary products/services sold
- **Country/city** (default: Uganda/East Africa)
- **Primary goal** (e.g. increase sales, reduce inbound support volume, retain customers)
- **WhatsApp Business number** (existing or new)
- **Current contact list size** (approximate — even a rough range is useful)
- **Average customer purchase value** (UGX or USD)
- **Key customer segments** as the client currently understands them
- **Any existing broadcast lists or groups** (names, sizes, how they were built)
- **Business hours** (for away message and response time commitments)

---

## 1. WhatsApp Business App Setup Checklist

Complete every item before sending the first broadcast.

**Business Profile**
- Display name: match the brand name exactly as it appears on other platforms and physical materials
- Business category: select the closest match from WhatsApp's category list
- Description: maximum 256 characters — state what the business does, who it serves, and one differentiator
- Website: add the primary website URL or a WhatsApp-friendly landing page link
- Email: add a monitored business email address
- Location: add if the business has a physical premises customers visit

**Profile Photo**
- Use a clear logo or founder photo at 640×640px
- Ensure the image is legible at small sizes — WhatsApp displays profile photos at 50×50px in chat lists

**Product/Service Catalogue**
- Set up a catalogue with a minimum of 3–5 items even if the full range is larger — it signals legitimacy
- Each entry: product/service name, price (mark as "contact for pricing" if price is not public), description (2–3 sentences), and a link to more detail or to order
- Update the catalogue whenever prices or offerings change

**Greeting Message**
- Auto-sent when a new contact messages for the first time
- Template: "Hello [Name], welcome to [Business Name]! We're glad you reached out. We help [value proposition in one sentence]. Expect a reply within [X hours/by end of business]. In the meantime, browse our catalogue: [link]."

**Away Message**
- Sent outside business hours
- Template: "Hi [Name], thanks for your message. We're currently closed but will reply by [time tomorrow / Monday morning]. For urgent matters, call [number]. We look forward to helping you."

**Quick Replies**
Set up 5–8 saved responses for the most common enquiries. Suggested shortcuts:

| Shortcut | Purpose |
|---|---|
| /price | Price enquiry response with catalogue link |
| /order | How to place an order — steps |
| /hours | Opening hours and days |
| /location | Physical address and Google Maps link |
| /pay | Accepted payment methods (MTN Mobile Money, Airtel Money, bank transfer, cash) |
| /delivery | Delivery areas, times, and costs |
| /contact | Full contact details |

**Labels**
Use labels to segment contacts from the first interaction:
- Lead (enquired, not yet purchased)
- New Customer (purchased once, within 30 days)
- Active Customer (purchased in last 60 days)
- Returning Customer (2+ purchases)
- VIP (top customers by spend or frequency — define the threshold)
- Supplier
- Staff

**Status Updates**
Enable Status updates — this is the daily broadcast to all contacts who have saved the business number. Treat it as a daily content channel.

---

## 2. Broadcast List Strategy and Segmentation

**What a broadcast list is**
A broadcast list sends a single message to multiple contacts simultaneously. Each recipient sees the message as a personal, one-to-one message — not a group message. Recipients must have the sender's number saved in their phone to receive the broadcast. This is the key distinction from a group: no recipient sees other recipients.

**Recommended segments**

| Segment | Definition | Content approach |
|---|---|---|
| Prospects | Have enquired but not purchased | Educational content, product value demonstrations, social proof, gentle nudges. No hard sell. |
| Active Customers | Purchased in last 60 days | Product updates, complementary offers, loyalty rewards, event invites. Maintain the relationship. |
| Lapsed Customers | No purchase in 60+ days | Re-engagement: acknowledge the gap, offer a reason to return (discount, new product, new service). |
| VIP Clients | Top customers by value or frequency | Exclusives: early access to new products, special pricing, personal check-ins, behind-the-scenes content. |

**Building the lists**
- Never add someone to a broadcast list without their explicit permission (verbal, written, or via opt-in mechanism)
- Label contacts correctly from the first interaction so segmentation is automatic
- Review and update segment membership monthly — a lapsed customer who re-purchases moves back to Active

---

## 3. Broadcast Content Guidelines

Apply these rules to every message sent from any broadcast list.

**Value first**
Every broadcast must give the recipient something useful: a tip, an update, an exclusive offer, a reminder, or useful information. "Just checking in" messages are not acceptable — they waste the recipient's time.

**Frequency**
- Maximum 3 broadcasts per week to any single segment
- 2 per week is safer and produces less opt-out pressure
- During campaigns or promotions, 4 per week is acceptable for a maximum of 2 consecutive weeks

**Length**
Under 150 words. Most recipients read on a smartphone while doing other things. Break messages into short paragraphs of 2–3 lines maximum. Use line breaks generously.

**Personal tone**
Use first names where the contact's name is saved. WhatsApp is a personal channel — a message that reads like a newsletter has failed before it is opened. Write as if addressing one person, not an audience.

**Opt-out**
Every broadcast must end with: *"Reply STOP to be removed from this list."* Remove anyone who replies STOP immediately, without question, and without further contact from any other list. Acknowledge: "Removed! No problem. Have a great day."

**Content to avoid**
- Forwarded messages (chain messages, viral content, news articles)
- The same message sent twice
- Messages with no clear purpose or value
- Promotional messages without prior relationship

---

## 4. WhatsApp Status Content Plan

**Frequency**
1–3 Status updates per day. Status disappears after 24 hours — post fresh content daily to maintain presence.

**Content types**

| Content type | Description |
|---|---|
| Behind-the-scenes | Production, preparation, team at work — builds trust |
| Product/service showcase | A single product or service per Status — short description, price if public |
| Quick tip | One practical tip relevant to the client's industry |
| Customer testimonial quote | Screenshot or typed quote from a real customer (with permission) |
| Daily greeting | Morning greeting with one piece of useful information |
| Countdown | Days remaining to an offer expiry, event, or product launch |
| Poll image | Screenshot a poll graphic — WhatsApp Status does not have native polling |

**Best posting times (EAT)**
- 7–8am: morning commute and school run
- 12–1pm: lunch break
- 6–8pm: evening, post-work

**Reach note**
Status is visible only to contacts who have saved the business number. Growing the contact list directly grows Status reach — every new saved contact is a new Status viewer.

---

## 5. WhatsApp Groups Strategy

**Groups vs. broadcast lists**

| | Group | Broadcast List |
|---|---|---|
| Recipients see each other | Yes | No |
| Recipients can reply to everyone | Yes | No (replies go only to sender) |
| Best for | Community, discussion | One-to-many messaging |
| Recipient must have number saved | No | Yes |

**When to create a group**
- Loyalty community (e.g. "VIP Customers Club")
- Event attendees (pre-event coordination, post-event follow-up)
- Team coordination (internal)
- Supplier relations
- Local community or neighbourhood group

**Group setup checklist**
- Name: clear and purpose-driven (e.g. "[Brand] VIP Club" not "Group 1")
- Description: state the group's purpose and rules in 3–4 sentences
- Pinned message: welcome message + community rules

**Community rules template (adapt for each group)**
1. Stay on topic — this group is for [purpose]
2. No spam — no promotional posts unless you are an admin
3. Be respectful — no hate speech, harassment, or personal attacks
4. No sharing of other members' personal information outside this group
5. Admins reserve the right to remove members who violate these rules

**Moderation**
- Set admin-only posting for announcement groups
- For community groups, allow open discussion but moderate actively
- Appoint a second admin to cover when the primary admin is unavailable

**Content rhythm for community groups**
- 3–5 posts per week
- Mix: 2 educational/tips posts, 1 exclusive offer or update, 1–2 discussion prompts or questions
- Respond to every comment within 24 hours

---

## 6. Opt-in Capture Methods and Opt-out Etiquette

**Opt-in methods**

- **WhatsApp QR code:** Generate from WhatsApp Business Settings → Business Tools → Short Link. Display in-store, on business cards, on receipts, in email signatures, and on packaging.
- **Click-to-WhatsApp link:** A direct link (wa.me/[number]?text=[pre-filled message]) shared on Facebook, Instagram, website, or email. No Meta Ads account required for basic link sharing.
- **Lead magnet:** "Send 'GUIDE' to [number] to receive our free [resource]." The action of sending the keyword is the opt-in.
- **Website widget:** A simple WhatsApp link button on the website (link only — no plugin required). Label it clearly: "Chat with us on WhatsApp."
- **Verbal opt-in at point of sale:** "May I add you to our customer updates list? I'll share tips and exclusive offers — you can opt out at any time by replying STOP." Log verbal opt-ins with date and staff member.

**Opt-out etiquette**
- Remove the contact immediately — same session if possible
- Reply: "Removed! No problem at all." Do not ask why. Do not attempt to re-add.
- Mark as removed in the contact label system — do not delete the contact
- Never remove someone from one list and continue messaging them from another without fresh consent

---

## 7. 30-Day Broadcast Message Calendar

### Week-by-Week Plan

| Week | Day | Segment | Message type | Message brief | CTA |
|---|---|---|---|---|---|
| 1 | Mon | Prospects | Welcome/introduction | Introduce the brand, state what value the customer will receive from being on the list | Reply to ask a question |
| 1 | Wed | Active | Product update | Highlight one product or service, state one practical benefit | View catalogue link |
| 1 | Fri | Lapsed | Re-engagement | Acknowledge they haven't heard from you in a while, offer a reason to return | Reply "BACK" for a welcome offer |
| 2 | Mon | All | Educational tip | One actionable tip related to the client's industry | Save this number to see daily tips |
| 2 | Wed | VIP | Exclusive offer | Early access to a new product, service, or price reduction | Reply "YES" to claim |
| 2 | Fri | Prospects | Social proof | One customer success story or testimonial (2–3 sentences) | View more on [platform] |
| 3 | Tue | Active | Loyalty reminder | Acknowledge their loyalty, introduce a loyalty benefit or reward | Reply to find out your status |
| 3 | Thu | Prospects | FAQ | Answer the single most common objection or question the client hears | Reply for more information |
| 3 | Sat | All | Weekend tip | A practical tip they can apply over the weekend | Share with someone who needs this |
| 4 | Mon | Lapsed | Final re-engagement | Last message in the re-engagement sequence — clear offer with deadline | Reply "YES" by [date] |
| 4 | Wed | Active | Event/offer | Promote an upcoming event, offer, or seasonal moment | Confirm attendance / place order |
| 4 | Fri | VIP | Personal check-in | Short personal message — thank them, share what's coming next month | Reply with feedback or questions |

### 12 Full Message Templates

**1. Welcome Sequence (Prospects)**
"Hi [Name]! Welcome to the [Business Name] community. I'm [Founder Name] and we help [target customer] with [key benefit]. Over the next few weeks I'll be sharing [type of content]. You'll get tips, updates, and the occasional exclusive offer. Reply to this message any time — I read every reply personally. To stop receiving messages, reply STOP."

**2. Product Highlight (Active Customers)**
"Hi [Name], have you tried our [product name] yet? It's one of our most popular items because [key benefit in one sentence]. Currently available at [price / 'contact us for pricing']. Reply 'INFO' and I'll send you full details. Reply STOP to unsubscribe."

**3. Customer Tip (All Segments)**
"Quick tip from [Business Name]: [One practical, specific tip relevant to the industry — e.g. 'If you're storing [product], keep it away from direct sunlight to extend shelf life by up to 40%.']. Hope that's useful! Reply STOP to stop receiving tips."

**4. Exclusive Offer (VIP)**
"Hi [Name], as one of our best customers I wanted you to see this first. We're launching [new product/service] on [date] and you can order 48 hours before everyone else at [price/discount]. Reply 'VIP YES' to secure yours. This offer is only going to our VIP list. Reply STOP to unsubscribe."

**5. Re-engagement (Lapsed)**
"Hi [Name], it's been a while since we last spoke — I hope all is well! A lot has changed at [Business Name] recently: [one new development]. If you'd like to reconnect, reply 'HELLO' and I'll send you what's new. No pressure at all. Reply STOP if you'd prefer not to hear from us."

**6. Event Reminder (Active Customers)**
"Hi [Name], just a reminder that our [event name] is happening on [date] at [time]. [One sentence on what they'll experience or gain.] Places are limited — reply 'RSVP' to confirm your spot and I'll send you all the details. Reply STOP to unsubscribe."

**7. Seasonal Greeting (All Segments)**
"Hi [Name], wishing you a wonderful [occasion — e.g. Eid Mubarak / Happy New Year / Happy Independence Day] from everyone at [Business Name]! [One genuine, warm sentence.] We're grateful for your support this year. Reply STOP to unsubscribe."

**8. Social Proof (Prospects)**
"Hi [Name], I wanted to share a quick story. [Customer first name] came to us with [problem]. After [solution], they [result in one sentence]. If you're dealing with something similar, reply 'TELL ME MORE' and I'll share exactly how we can help you. Reply STOP to unsubscribe."

**9. Educational Value (Prospects)**
"Quick insight from [Business Name]: Most people in [industry] don't know that [surprising or counterintuitive fact]. This means [implication]. We've helped [number or type of customer] use this to their advantage. Want to know how? Reply 'YES'. Reply STOP to unsubscribe."

**10. Loyalty Reward (Active/VIP)**
"Hi [Name]! You've been a customer for [time period / number of purchases] and we want to say thank you properly. As a thank-you, we're giving you [specific reward — discount, free item, upgrade] on your next order. Just mention this message when you order. Valid until [date]. Reply STOP to unsubscribe."

**11. FAQ / Objection Handler (Prospects)**
"We get asked a lot: '[Common question or objection].' The honest answer is: [Direct, transparent answer in 2–3 sentences]. If you have other questions, reply here — I'm happy to answer. View our catalogue for full details: [link]. Reply STOP to unsubscribe."

**12. Final Re-engagement (Lapsed)**
"Hi [Name], this is the last message I'll send you for a while. If you'd like to stay connected, reply 'STAY' and I'll keep you on the list. If not, no hard feelings — you'll be removed automatically in 48 hours. Either way, thank you for your past support. [Business Name]."

---

## 8. WhatsApp-specific KPIs

Note: WhatsApp Business (non-API version) has limited built-in analytics. Track the following metrics using a simple spreadsheet alongside the app's native stats.

| KPI | Target / Benchmark | How to measure |
|---|---|---|
| Estimated open rate | 85–98% (WhatsApp messages are opened within 24 hours in almost all cases) | Use reply rate as a proxy — a message with no replies has likely still been read |
| Catalogue views | Track monthly increase | WhatsApp Business → Business Tools → Catalogue → View stats |
| Enquiry volume | Set a baseline in Month 1, target 10–20% monthly growth | Count messages received per week in a spreadsheet |
| Enquiry-to-purchase conversion rate | Target 20–40% depending on industry | Track via labels: Lead → Customer. Divide converted leads by total leads per month |
| Status view count | Track weekly; target 5–10% increase per month | WhatsApp Status → Eye icon (visible for 14 days) |
| Response time | Under 2 hours during business hours | Note response times manually or use WhatsApp Business dashboard |
| Opt-out rate | Under 2% per broadcast | Count STOP replies per broadcast; divide by list size |
| Broadcast reply rate | Target 5–15% per broadcast | Count replies per broadcast |

---

## Quality Criteria

Output from this skill meets the standard when it:

- Covers all eight sections with no placeholders — every template contains complete, ready-to-use text, not descriptions of what text should say
- Broadcast message templates are personalised, conversational, and under 150 words each, with an opt-out instruction included
- Segmentation logic is clear and actionable — the client can immediately categorise their existing contacts using the label system provided
- The 30-day calendar specifies segment, message type, and full template reference for every entry
- Opt-in methods are appropriate for the Ugandan/EA market (QR codes, click-to-WhatsApp, verbal opt-in at point of sale)
- KPIs are realistic given WhatsApp Business app limitations — no claims are made about data that is not available natively
- The permission-based and value-first philosophy is clearly stated and consistently applied across all broadcast and group content guidance
- All content reflects the direct, personal nature of WhatsApp — no message reads like a newsletter, email blast, or social media post

---
name: playbook-chatbot-strategy
description: Use when designing or improving a Chatbot Strategy operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Chatbot Strategy Playbook

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Chatbot Strategy workflow for a client or delivery team.
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
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Chatbot Strategy playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| The user asks for a sensitive, disputed or out-of-scope decision | Hand off to a named human route | Confident automated harm |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Chatbot Strategy playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Chatbot Strategy playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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

## Required Input

Before generating any output, ask for the following:

1. **Client business name and industry** — e.g., "Kampala Threads — women's fashion retail"
2. **Country and city** — defaults to Uganda/Kampala if not specified
3. **Primary platform for the chatbot** — Facebook Messenger, Instagram DMs, or WhatsApp Business (pick one to start)
4. **Volume of inbound messages per week** — approximate number of messages received on the chosen platform
5. **Top 5 questions or requests customers send repeatedly** — exact wording where possible
6. **Client's technical capacity** — can they navigate ManyChat or Tidio independently, or do they need a manual quick-replies template?
7. **Budget tier** — free tools only, or open to a paid automation platform (ManyChat paid, Africa's Talking API)?

---

## Section 1 — Do You Need a Chatbot?

Apply this decision framework before recommending any automation tool.

### Decision Threshold

- If the client receives **50 or more repetitive messages per week** on a single platform, automation is worth the setup time and ongoing maintenance.
- Below 50 messages per week, a manual quick-replies setup is faster to implement and carries no risk of misconfiguration.

### When Automation Makes Sense

- The same 5–10 questions account for the majority of inbound messages.
- The client or their team cannot respond within 30 minutes during business hours.
- The business has clear, factual answers that do not change frequently.
- The client wants to capture leads (name, phone, email) at scale.

### When a Human Is Better

- Questions require judgement, empathy, or context (complaints, refunds, custom orders).
- Answers vary per customer (pricing negotiation, bespoke services).
- The client's audience is older or less familiar with chatbot interactions — a bot that confuses customers is worse than a slow human reply.
- The client cannot commit to checking escalations at least twice per day.

### Warning

A badly configured chatbot frustrates customers and damages brand trust. Only automate what can be answered accurately and consistently. If the client cannot maintain the bot, do not build it.

### Minimum Viable Alternative

For small clients or those new to automation, recommend this first: **Saved Replies / Quick Replies in Facebook Business Suite**. It is free, takes 15 minutes to set up, and requires no technical knowledge. Cover this option before proposing any paid tool.

---

## Section 2 — Platform Automation Options

For each platform, present the free built-in option first. Only recommend paid tools if the client's volume or goals justify the cost.

### Facebook Messenger

**Free — Facebook Business Suite:**
- **Instant Reply** — sends an automatic response when the Page is offline or slow to respond. Set in Business Suite → Inbox → Automations → Instant Reply.
- **FAQ Shortcuts** — pre-written answers to common questions, selectable from the reply composer.
- **Saved Replies** — full-length templated responses triggered by typing a shortcut keyword in the inbox.

**Paid — ManyChat (free tier: up to 1,000 contacts):**
- Keyword triggers — a customer types "price" and receives an automated price list message.
- Flow builder — visual drag-and-drop conversation designer; no coding required.
- Lead capture sequences — collect name, phone number, or email via Messenger before routing to a human.
- Upgrade to ManyChat Pro (approx. USD 15/month) for unlimited contacts and advanced conditions.

### Instagram DMs

**Free — Instagram Business:**
- **Quick Replies** — saved message templates accessible from the DM reply box via the "/" shortcut.
- **Frequently Asked Questions (FAQ button)** — up to four pinned FAQ buttons displayed on the business profile's message screen; customers tap to send the question and receive an instant answer.

**Paid — ManyChat (Instagram channel):**
- **Story mention automation** — automatically DM anyone who mentions the client's account in their Story.
- **Comment-to-DM flows** — when a customer comments a keyword on a post, they receive an automatic DM with more information or a link.
- Connect the same ManyChat account to both Facebook and Instagram to manage both from one dashboard.

### WhatsApp Business

**Free — WhatsApp Business App:**
- **Greeting Message** — sent automatically to customers who message the business for the first time or after 14 days of inactivity.
- **Away Message** — sent automatically outside business hours. Include expected response time in EAT (East Africa Time).
- **Quick Replies** — up to 50 saved message templates triggered by typing "/" in the chat.

**Paid — WhatsApp Business API:**
- Enables proper multi-step chatbot flows, broadcast lists to opted-in contacts, and a multi-agent shared inbox.
- **Africa's Talking** (recommended for Uganda) — Uganda-based provider, UGX pricing, local support team, USSD and SMS integration also available. See [africastalking.com](https://africastalking.com).
- **Twilio** — international option, USD pricing, more complex setup; suitable for clients with a developer on staff.
- WhatsApp Business API requires business verification — allow 2–4 weeks for approval.

---

## Section 3 — Flow Design

Use this framework to design a basic FAQ chatbot flow regardless of platform.

### Step 1 — Map the Conversation Tree

- List the top 5 questions customers ask (use the client's input from Required Input item 5).
- For each question, write the single best answer in a maximum of 3 sentences. Avoid jargon.
- Identify where the conversation must hand off to a human. Escalate automatically for: complaints, refunds, custom orders, pricing negotiation, delivery problems, and any question involving sensitive personal information.

Present the map in this format:

| Customer Message / Keyword | Automated Response | Hand Off to Human? |
|---|---|---|
| "What are your prices?" | [Answer in 3 sentences] | No — unless negotiation begins |
| "Where are you located?" | [Address + map link] | No |
| "I have a complaint" | [Acknowledgement + escalation] | Yes — immediately |
| "Can I get a discount?" | [Standard response + escalation] | Yes |
| "How do I order?" | [Step-by-step + link] | No |

### Step 2 — Write the Welcome Message

Use this template and adapt to the client's tone:

> Hello! Thank you for messaging [Business Name]. We are here to help. Please choose from the options below or type your question and we will respond shortly.
> 1. Prices and products
> 2. Location and opening hours
> 3. Place an order
> 4. Speak to a team member

Adapt for an East African friendly tone — warm and direct, but not sycophantic. Avoid "Dear Esteemed Customer" and excessive exclamation marks. If the client serves a predominantly local Ugandan audience, add a brief Luganda greeting option:

> Nkulamusizza! / Welcome! — choose your preferred language: [English] | [Luganda]

Keep the welcome message under 160 characters where possible to ensure it loads on slow mobile data connections.

### Step 3 — Write FAQ Responses

Write one response per common question. Apply this structure for each:

- **Answer:** 2–3 sentences maximum. Be specific — include prices, addresses, and links where available.
- **Next action:** tell the customer exactly what to do next. Example: "To place an order, send us your name and delivery address." or "Type AGENT to speak to a team member."

Keep all automated responses under 300 characters. Long messages may not load reliably on low-bandwidth mobile connections common across Uganda and East Africa.

### Step 4 — Design the Human Handoff Trigger

- Reserve the keywords **AGENT**, **HUMAN**, and **HELP** to always route the conversation to a team member. Configure these in ManyChat (Automation → Keywords) or document them in the manual quick-replies guide for WhatsApp.
- Set clear response hours in every handoff message: "Our team responds between 8am–6pm EAT, Monday to Friday. Outside these hours, we will reply first thing the next working day."
- Never leave a customer in a loop. Every automated flow must offer a clear exit — either a direct answer, a link, or a route to a human. If no answer exists, say so and escalate.

---

## Section 4 — ManyChat Setup Guide (Free Tier, Facebook Messenger)

Follow these steps in order. Complete setup before going live.

1. Create an account at [manychat.com](https://manychat.com) and connect it to the client's Facebook Page. Grant ManyChat the required Page permissions when prompted.
2. Go to **Automation → Keywords** and create a keyword trigger for each of the top 5 FAQ keywords (e.g., "price", "location", "order", "hours", "contact").
3. Build the **Welcome Flow**: set the trigger to "First interaction" → send the welcome message → display a menu of buttons matching the top 5 options.
4. Build individual **FAQ flows**: keyword trigger → send the pre-written answer → add a "Was this helpful?" Yes/No button. If No, route to the AGENT keyword flow.
5. Build the **AGENT flow**: triggered by keywords AGENT, HUMAN, HELP → send a message confirming a human will follow up → notify the Page inbox. Ensure the client has the ManyChat mobile app installed to receive notifications.
6. Add a **Growth Tool**: go to Growth Tools → Add a Messenger Button to the client's Facebook Page so visitors can start a conversation directly.
7. **Test before launching**: send a test message to the Page from a personal Facebook account. Test every menu option, every FAQ keyword, and one off-script message to confirm the handoff trigger works.

---

## Section 5 — WhatsApp Business Quick Wins (No Budget)

For clients who cannot afford WhatsApp Business API or ManyChat. Complete all six steps.

1. Download the **WhatsApp Business** app (free, available on Android and iOS) and register with the business phone number. Note: this number cannot also be used on the standard WhatsApp app.
2. Set up the **Business Profile**: add the business name, category, description (max 256 characters), address, opening hours, email, and website.
3. Go to **Business Tools → Away Message**: write a professional away message. Example: "Thank you for your message. Our team is currently unavailable. We respond between 8am–6pm EAT, Monday to Friday. We will reply to you shortly." Toggle on and set the schedule to outside business hours.
4. Go to **Business Tools → Greeting Message**: write a warm welcome for first-time contacts. Example: "Hello! Welcome to [Business Name]. How can we help you today? Reply with one of the following: PRICES | LOCATION | ORDER | HELP."
5. Go to **Business Tools → Quick Replies**: add shortcuts for the top 5 FAQs. Type "/" in any chat to trigger. Set up: /prices, /location, /order, /hours, /returns. Each shortcut holds a full pre-written response.
6. Set up a **Product Catalogue**: go to Business Tools → Catalogue → add products or services with names, descriptions, prices, and images. Share catalogue items directly in chat to reduce repetitive product enquiries.

---

## Section 6 — Quality Control Checklist

Verify every item before going live. Do not skip this step.

- [ ] Welcome message is warm, clear, grammatically correct, and under 160 characters
- [ ] Every menu option has a working, tested automated response
- [ ] Human handoff keywords (AGENT, HUMAN, HELP) route correctly to the live inbox
- [ ] Away message specifies response time in EAT and days of the week
- [ ] Tested with at least 5 different message types, including one off-script message that no flow covers
- [ ] Client knows how to access the inbox, respond to escalations, and silence or pause the bot if needed
- [ ] All automated messages load correctly on a standard Ugandan mobile data connection (test on 3G if possible)

---

## EA-Specific Considerations

Apply these by default for all Uganda and East Africa clients.

- **WhatsApp Business (free app)** is sufficient for most Uganda SME clients starting out. Do not oversell API solutions to clients who receive fewer than 50 messages per week.
- **Africa's Talking** is the recommended WhatsApp Business API provider for Uganda — UGX pricing, a local support team in Nairobi and Kampala, and integration with USSD and SMS for clients who want multi-channel automation. Prioritise this over Twilio for EA clients.
- **Pricing conversations** — many East African customers will attempt to negotiate price via chatbot or DM. Include an explicit handoff for any pricing discussion: "For pricing questions and special requests, type AGENT to speak with our team directly."
- **Luganda greeting** — if the client serves a local Ugandan audience rather than an expatriate or regional market, include a Luganda greeting option in the welcome message: "Nkulamusizza!" (I welcome you) as an alternative to the English greeting.
- **Network reliability** — keep all automated messages short. Long messages (300+ characters) may not load reliably on slow or intermittent mobile data, which is common outside Kampala and in many urban areas during peak hours. Break long answers into two shorter messages rather than one long block.
- **Business hours framing** — always reference EAT (East Africa Time, UTC+3) in away messages and handoff notices. Do not use GMT or UTC without converting.

---

## Quality Criteria

Output from this skill meets the standard when:

- The decision framework in Section 1 is applied and a clear recommendation is made — chatbot, quick replies, or no automation — with justification based on the client's message volume and technical capacity.
- The platform tool recommended (free or paid) is appropriate for the client's platform, budget, and Uganda/EA market context.
- A conversation tree is mapped with the client's actual top 5 questions, not generic placeholders.
- A human handoff trigger is defined with specific keywords, response hours in EAT, and a clear exit from every flow.
- A welcome message template is included, adapted to the client's name, tone, and audience (including Luganda option where relevant).
- WhatsApp Business free setup steps are documented in full for clients with no budget, covering all six steps in Section 5.
- EA-specific considerations are applied: Africa's Talking referenced for API, pricing handoff included, message length adapted for low-bandwidth conditions.

---

## References

Consult these related skills when building the full client engagement:

- `playbook-community-management/SKILL.md` — for managing the human side of inbox responses, tone guidelines, and escalation protocols alongside automated flows.
- `platform-whatsapp/SKILL.md` — for the full WhatsApp channel strategy including broadcast content, catalogue, and status updates beyond automation.
- `playbook-sms-whatsapp-marketing/SKILL.md` — for outbound messaging campaigns via WhatsApp broadcast lists and SMS, which complement inbound chatbot flows.

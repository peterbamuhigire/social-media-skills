---
name: playbook-chatbot-strategy
description: Use when a business wants automated replies in WhatsApp, Messenger or Instagram DMs, or an AI chatbot that answers customers in local languages; produces the go/no-go decision, conversation flows, FAQ replies and human-handoff rules; not for running the WhatsApp Business channel itself (use `platform-whatsapp`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Chatbot Strategy Playbook

Decides whether a client needs a chatbot, quick replies or no automation, then designs the flows, FAQ replies and human handoff for Messenger, Instagram DMs or WhatsApp, with Uganda and East African defaults.

<!-- dual-compat-start -->
## Use When
- The inbox fills with the same questions every day: is a chatbot worth it, or will saved replies do?
- Design a Messenger or Instagram DM bot in ManyChat: welcome message, conversation tree, FAQ answers and quick-reply buttons.
- WhatsApp Business automation, from greeting and away messages to flows on the WhatsApp Business API.
- Build a WhatsApp chatbot that uses an LLM to answer customers in Luganda, Swahili or English from a knowledge base and passes complaints to a person.
- Write the human-handoff triggers, escalation rules and a pre-launch quality checklist for the bot.

## Do Not Use When
- `platform-whatsapp` for the WhatsApp Business channel plan: profile, catalogue, Status and broadcast calendar.
- `playbook-marketing-automation` for triggered email, SMS and WhatsApp sequences across the customer lifecycle.
- `playbook-community-management` for how staff answer comments, reviews and inbox complaints by hand.
- Stop before switching on a live bot, connecting customer data or messaging customers without the client's written approval and a Uganda DPPA 2019 consent check; deliver the flows for sign-off.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry, country and city | Client | Yes | Default to Uganda/Kampala and ask for the business details before writing replies. |
| Primary platform (Messenger, Instagram DMs or WhatsApp Business; one to start) | Client | Yes | Start with the platform that receives most messages; label the choice provisional. |
| Weekly inbound message volume on that platform | Client inbox or platform export | Yes | Recommend free saved or quick replies only; the 50-per-week threshold cannot be tested. |
| Top 5 repeated questions, in customers' own words (top 10 for an LLM build) | Client support team | Yes | Stop the conversation tree; request the list rather than writing generic placeholders. |
| Technical capacity and budget tier (free only, or ManyChat paid / Africa's Talking API) | Client | Yes | Assume free tools and a manual quick-replies template. |
| Consent basis and data handling for customer data | Client, Uganda DPPA 2019 check | If data is collected or stored | Design flows without data capture; mark the consent check `not assessed`. |

## Workflow

1. Run the intake questions in the [chatbot build guide](references/chatbot-build-guide.md) and confirm the owner who will check escalations.
2. Apply the go/no-go test (Section 1 of the guide): 50 or more repetitive messages per week, answers that rarely change and an owner who checks escalations at least twice a day. Stop and recommend saved or quick replies when the test fails.
3. Choose the tool, free built-in option first, for the chosen platform (Section 2); for an LLM WhatsApp bot, use the three-layer design in [WhatsApp chatbot design](references/whatsapp-chatbot-design.md).
4. Map the conversation tree, write the welcome message (under 160 characters, Luganda option where relevant) and FAQ replies (under 300 characters, 2–3 sentences plus a next action).
5. Define the handoff: AGENT, HUMAN and HELP keywords, response hours in EAT, automatic escalation for complaints, refunds, custom orders, pricing negotiation, delivery problems and sensitive personal information, and an exit from every flow.
6. Write the set-up steps (ManyChat free tier, or the six WhatsApp Business quick wins) and apply the East African considerations.
7. Run the pre-launch quality checklist; correct any failed item and rerun the tests before handing the flows to the client for written sign-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Go/no-go recommendation (chatbot, quick replies or no automation) | Client owner | Justified by the client's weekly volume, technical capacity and budget. |
| Conversation tree, welcome message and FAQ replies | Client and set-up owner | Uses the client's actual top questions; character limits met; every row states whether it hands off. |
| Handoff and escalation rules | Client inbox staff | Keywords, EAT response hours and escalation triggers stated; no flow ends in a loop. |
| Set-up guide for the chosen tool | Client or delivery team | Steps in order for ManyChat or all six WhatsApp Business steps; paid options only where justified. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Pre-launch test record | Completed checklist | At least 5 message types tested, including one off-script message, with handoff confirmed. |
| Tool and price check | Table with source and date | Every tool price or approval time is checked on the vendor's current site or labelled approximate. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Switching a bot live or connecting customer data also needs a Uganda DPPA 2019 consent check.

## Degraded Mode

Without the client's weekly message volume and top questions, return the narrowest qualified result and mark the affected checks `not assessed`. The free saved-reply and away-message set-up with EAT hours and handoff keywords can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Fewer than 50 repetitive messages per week on one platform | Recommend Saved Replies / Quick Replies in Facebook Business Suite or the free WhatsApp Business app; do not sell an API. | Paying for automation that a 15-minute set-up would cover. |
| The client cannot check escalations at least twice per day, or cannot maintain the bot | Do not build it. | A badly configured bot that damages brand trust. |
| The user asks for a sensitive, disputed or out-of-scope decision (complaint, refund, custom order, pricing negotiation) | Hand off to a named human route. | Confident automated harm. |
| The bot runs on WhatsApp and must answer open-ended questions with an LLM | Apply the three-layer design (rules, LLM, human escalation) in [whatsapp-chatbot-design](references/whatsapp-chatbot-design.md). | Ungrounded LLM answers and missing human handoff. |
| A WhatsApp Business API provider is needed for a Uganda client | Prefer Africa's Talking over Twilio; allow 2–4 weeks for business verification. | USD billing, no local support and a missed launch date. |
| The bot answers on the WhatsApp Business Platform (API) | Keep bot replies inside the 24-hour customer service window the user opened; send only approved templates after it closes, and from 1 Oct 2026 budget for service replies above 1,000 a month per number (register `WHATSAPP-PRICING-2025`) | A bot that cannot reply after 24 hours, or an unbudgeted message bill |
| An answer runs past 300 characters | Split it into two shorter messages. | Messages that fail to load on slow mobile data. |

## Quality Standards

- The Section 1 decision framework is applied and a clear recommendation is made with volume and capacity justification.
- The recommended tool suits the client's platform, budget and Uganda/EA context.
- The conversation tree uses the client's actual top 5 questions, not placeholders.
- Handoff keywords, response hours in EAT and a clear exit from every flow are defined.
- The welcome message is adapted to the client's name, tone and audience, including a Luganda option where relevant.
- For no-budget clients, all six WhatsApp Business free set-up steps are documented.
- EA considerations are applied: Africa's Talking for API, a pricing handoff, short messages for low bandwidth.

## Anti-Patterns

- Building a bot for a client with under 50 repetitive messages a week. Fix: set up quick replies first and revisit when volume grows.
- Leaving a customer in a loop with no answer. Fix: give every flow a direct answer, a link or a route to a human; if no answer exists, say so and escalate.
- Letting the bot negotiate price. Fix: add an explicit pricing handoff ("type AGENT to speak with our team directly").
- Opening with "Dear Esteemed Customer" or "Please select from the following options:". Fix: warm, direct wording with local greetings where the audience is local.
- Quoting hours in GMT or UTC. Fix: always state EAT (UTC+3) in away and handoff messages.
- Going live without an off-script test. Fix: test at least 5 message types, including one no flow covers, on a 3G connection where possible.

## References

- [Chatbot build guide](references/chatbot-build-guide.md): read when running intake, the go/no-go test, choosing tools, designing flows and handoff, setting up ManyChat or WhatsApp Business, or running the pre-launch checklist.
- [WhatsApp chatbot design](references/whatsapp-chatbot-design.md): read when designing a WhatsApp chatbot with an LLM layer, social presence cues, HITL escalation triggers, a knowledge-base input and containment KPIs.
- [`playbook-community-management`](../playbook-community-management/SKILL.md): read when setting the human side of inbox replies, tone and escalation alongside automated flows.
- [`platform-whatsapp`](../../platforms/platform-whatsapp/SKILL.md): read when the full WhatsApp channel strategy (broadcasts, catalogue, Status) is needed beyond automation.
- [WhatsApp Platform pricing and templates](../../platforms/platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md): read when setting the customer service window, template use after it closes, or message costs for an API bot.
- [`playbook-sms-whatsapp-marketing`](../playbook-sms-whatsapp-marketing/SKILL.md): read when planning outbound broadcast and SMS campaigns that complement inbound flows.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when writing welcome, FAQ and handoff copy.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and greetings for East African customers.
<!-- dual-compat-end -->

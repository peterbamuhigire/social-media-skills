# WhatsApp chatbot design with an LLM layer

Merged from skills/ai-marketing/ai-whatsapp-chatbot-design on 2026-09-29 at 7c60138; preservation map: [ai-whatsapp-chatbot-design.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/ai-whatsapp-chatbot-design.md)

## When to use this reference

Use it when the chatbot runs on WhatsApp (Business API or a WhatsApp chatbot platform) and must answer open-ended questions through a large language model (LLM), not only fixed menus. For a free WhatsApp Business app set-up, a quick-replies bot or a Messenger/Instagram flow, [chatbot-build-guide.md § Sections 1–5](chatbot-build-guide.md) is enough. Apply the [chatbot-build-guide.md § Section 1](chatbot-build-guide.md) threshold first: an LLM layer is only worth building once rule-based automation is justified.

## Inputs

Collect these in addition to the playbook's Required Input:

| Input | Notes |
|---|---|
| Primary goal | Customer service, sales enquiries, appointment booking or FAQ handling |
| Approximate monthly WhatsApp message volume | Monthly, to size the platform plan and escalation staffing |
| Languages customers write in | English, Luganda, Kiswahili or other; the bot replies in the customer's language |
| Human support team size and availability hours | Sets escalation capacity and the handoff wait time quoted to customers |

Country and city default to Uganda unless the requester names another market.

## Why WhatsApp plus an LLM in East Africa

WhatsApp is the dominant messaging channel in East Africa. No source measures WhatsApp's share of smartphone users in Uganda, Kenya, Tanzania or Rwanda, so state no percentage unless it is a named, dated figure with its base, and check the client's own audience data (register WA-01, 2026-09-24; register row `WHATSAPP-USAGE-EA-2026`).

Combined with an LLM, a WhatsApp business number becomes a 24/7 sales and support agent that speaks the customer's language, remembers context, and escalates to a human when needed (Boustany, 2024; Ltifi, 2024). The competitive advantage is not automation for its own sake: it is availability and responsiveness at a cost most East African businesses can afford.

## Decision rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Choosing the operating level: data readiness, AI maturity and risk support it | Choose the lowest viable automation level (rules before LLM) and define its human approval gate | Automating an unsafe or unevaluable marketing process |
| Query is structured and predictable (hours, pricing, location, how to order) | Route to Layer 1 rule-based flow | Paying for and risking LLM answers where a fixed answer is correct |
| Query is open-ended and falls outside the decision tree | Route to Layer 2 LLM, grounded in the brand knowledge base | Cold dead-end menus |
| Complaint, frustrated customer, low LLM confidence, money, contracts or sensitive personal data | Route to Layer 3 human escalation | Confident automated harm |

## Three-layer architecture

| Layer | Handles | Notes |
|---|---|---|
| 1 — Rule-based flows (decision trees) | Structured, predictable queries: business hours, pricing, location, how to place an order | Fast, reliable, zero AI cost |
| 2 — LLM responses | Open-ended, conversational queries outside the decision tree | The LLM uses the brand knowledge base (see [brand-voice-ai-training](../../../ai-marketing/brand-voice-ai-training/SKILL.md) and its brand knowledge-base / RAG reference) to generate accurate, on-brand responses |
| 3 — Human escalation | Live agent handoff | Triggered when the query is a complaint, the customer is frustrated, LLM confidence is low, or the query involves money, contracts or sensitive personal data |

## Social presence principles

Research reported in Ltifi (2024) finds that East African consumers respond significantly better to chatbots that show social presence: warmth, responsiveness and human-like interaction cues. Build these into every bot message:

- **Greet by name** where possible: "Hello Nakato! How can I help you today?"
- **Offer local greetings** for an informal register: "Oli otya?" (Luganda) / "Habari?" (Kiswahili). The "Nkulamusizza!" welcome option in [chatbot-build-guide.md § Section 3](chatbot-build-guide.md) also applies.
- **Acknowledge emotional context:** "I understand this is frustrating — let me help you sort this out."
- **Avoid corporate coldness:** never open with "Please select from the following options:".
- **Mirror the customer's register:** formal for formal, casual for casual.
- **Disclose the AI nature when directly asked.** Transparency builds trust; note the Uganda Data Protection and Privacy Act, 2019 obligations for any personal data the bot collects.

## Procedure

### Step 1 — Map the top 10 customer queries

Interview the client's human support team and list the 10 most common questions received on WhatsApp in the past month. These become the backbone of the Layer 1 decision trees. (The [chatbot-build-guide.md § Section 3](chatbot-build-guide.md) top-5 map is the minimum for a simple FAQ bot; an LLM build uses the top 10.)

### Step 2 — Design the decision tree

Map the response path for each query type, for example:

```
Customer: "What are your prices?"
→ Bot: "Our packages start from UGX [X]. Which are you interested in?
   [Option A] [Option B] [Option C]"
→ If Option A: "Great choice! Here's what's included: [details].
   Ready to book? Reply YES or speak to our team."
```

### Step 3 — Define the LLM boundary and system prompt

Specify which query types go to the LLM layer: open-ended product questions, complaint context gathering and multi-turn sales conversations. Write the system prompt:

```
You are [Brand Name]'s friendly customer service assistant on WhatsApp.
You help customers in Uganda with [core services].
Always be warm, helpful, and honest.
If you do not know something, say so and offer to connect the customer with a human.
Never make up prices, availability, or delivery timelines.
Respond in the same language the customer uses.
```

### Step 4 — Define human-in-the-loop (HITL) escalation triggers

Hand off to a human agent when:

- the customer uses words such as "complaint", "refund", "legal", "manager", "angry" or "cheated";
- the same issue is raised more than twice without resolution;
- the query involves a transaction above a defined value threshold;
- the customer explicitly asks for a human (the playbook's AGENT / HUMAN / HELP keywords also apply);
- LLM confidence falls below the agreed threshold.

Handoff message template: "I'm connecting you to one of our team members now. They'll be with you shortly — usually within [X] minutes during business hours." State business hours in EAT, as the playbook requires.

### Step 5 — Build the knowledge-base input

Compile the brand knowledge base (see [brand knowledge base (RAG)](../../../ai-marketing/brand-voice-ai-training/references/brand-knowledge-base-rag.md)):

- full product/service catalogue with prices in UGX;
- FAQs with approved answers;
- policies: returns, delivery, payment methods;
- business hours and location(s);
- team names and roles for escalation routing.

## Tool options

Prices are approximate starting points recorded in the source skill; verify current pricing and East African availability on the vendor's site before quoting them to a client.

| Tool | Best for | East African accessibility | Approx. cost |
|---|---|---|---|
| WATI | WhatsApp Business API plus chatbot builder | Yes | From USD 49/month |
| Respond.io | Multi-channel plus WhatsApp plus LLM integration | Yes | From USD 79/month |
| Interakt | Africa/India-focused WhatsApp tool | Yes | From USD 15/month |
| Twilio | Developer-friendly WhatsApp API | Requires a developer | Pay-per-message |
| Meta Cloud API | Maximum control | Requires a developer | Pay-per-message |

Match the recommendation to the client's budget and technical capacity; [chatbot-build-guide.md § Section 2](chatbot-build-guide.md) covers Africa's Talking and the free WhatsApp Business app.

## Measurement framework

Track monthly:

| KPI | Definition | Target |
|---|---|---|
| Containment rate | % of conversations resolved without human escalation | 60–80% for a mature bot |
| First response time | Customer message to first bot reply | Under 30 seconds |
| CSAT score | Asked after resolution: "How satisfied were you? Reply 1–5" | Set with the client |
| Escalation rate | % of conversations handed to a human; spikes show bot gaps | Track trend |
| Conversion rate | Sales bots: % of conversations ending in a purchase or booking | Set with the client |

## Checklist

- [ ] Conversation flows are mapped for the top 10 customer query types.
- [ ] Social presence principles are built into all bot messages; no cold or corporate language.
- [ ] HITL escalation triggers are explicitly defined, with a handoff message template.
- [ ] The LLM system prompt is written, stating brand voice and knowledge boundaries.
- [ ] The knowledge-base input document is compiled and ready for upload.
- [ ] The tool recommendation fits the client's budget and technical capacity.
- [ ] The measurement framework has at least 4 KPIs, each with a target agreed with the client.
- [ ] Uganda Data Protection and Privacy Act, 2019 compliance is noted.

## Sources

- Boustany, S. (2024) *Generative AI for Social Media Marketing*.
- Ltifi, M. (ed.) (2024) *Advances in Digital Marketing in the Era of Artificial Intelligence*, CRC Press.
- Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn, Mercury Learning.
- Uganda Data Protection and Privacy Act, 2019.
- Source register row `WHATSAPP-USAGE-EA-2026` (Kaizen register WA-01).

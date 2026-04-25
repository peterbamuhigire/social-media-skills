---
name: ai-whatsapp-chatbot-design
description: >
  Design WhatsApp LLM chatbots for East African markets: conversation flows,
  social presence principles, trust-building, local language registers, and
  human escalation protocols. Invoke when a client wants to automate WhatsApp
  customer service, sales enquiries, or support using AI.
---
# AI WhatsApp Chatbot Design

<!-- dual-compat:start -->
## Use when
- Design WhatsApp LLM chatbots for East African markets: conversation flows, social presence principles, trust-building, local language registers, and human escalation protocols. Invoke when a client wants to automate WhatsApp customer service, sales enquiries, or support using AI.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask for:
- Client business name and industry
- Country/city (default: Uganda)
- Primary goal: customer service / sales enquiries / appointment booking / FAQ handling
- Approximate monthly WhatsApp message volume
- Languages customers communicate in (English, Luganda, Kiswahili, other)
- Existing human support team size and availability hours

## Why WhatsApp + LLM for East Africa

WhatsApp penetration exceeds 90% among smartphone users in Uganda and across East Africa. Combined with a large language model, a WhatsApp business number becomes a 24/7 sales and support agent that speaks the customer's language, remembers context, and escalates intelligently to humans when needed (Boustany, 2024; Ltifi, 2025).

The competitive advantage is not automation for its own sake — it is *availability and responsiveness* at a cost most EA businesses can afford.

## Architecture: Three Layers

**Layer 1 — Rule-based flows (decision trees):**
Handle structured, predictable queries: business hours, pricing, location, how to place an order. Fast, reliable, zero AI cost.

**Layer 2 — LLM responses:**
Handle open-ended, conversational queries that fall outside the decision tree. The LLM uses the brand knowledge base (see `ai-rag-brand-knowledge-base`) to generate accurate, on-brand responses.

**Layer 3 — Human escalation:**
Trigger a live agent handoff when: the query is a complaint, the customer is frustrated, the LLM confidence is low, or the query involves money, contracts, or sensitive personal data.

## Social Presence Principles (Ltifi, 2025)

Research confirms that East African consumers respond significantly better to chatbots that exhibit social presence — warmth, responsiveness, and human-like interaction cues. Apply these principles:

- **Greet by name** where possible: "Hello Nakato! How can I help you today?"
- **Use local greetings** as an option: "Oli otya?" / "Habari?" for informal register
- **Acknowledge emotional context:** "I understand this is frustrating — let me help you sort this out."
- **Avoid corporate coldness:** Never open with "Please select from the following options:"
- **Mirror the customer's register:** If they write formally, respond formally. If casually, match it.
- **Disclose AI nature** when directly asked — transparency builds trust (Uganda Data Protection and Privacy Act, 2019)

## Conversation Flow Design

### Step 1: Map the top 10 customer queries

Interview the client's human support team. List the 10 most common questions received via WhatsApp in the past month. These become the backbone of the Layer 1 decision trees.

### Step 2: Design the decision tree

For each query type, map the response path:

```
Customer: "What are your prices?"
→ Bot: "Our packages start from UGX [X]. Which are you interested in?
   [Option A] [Option B] [Option C]"
→ If Option A: "Great choice! Here's what's included: [details].
   Ready to book? Reply YES or speak to our team."
```

### Step 3: Define the LLM boundary

Specify which query types go to the LLM layer — open-ended product questions, complaint context gathering, multi-turn sales conversations. Write the system prompt:

```
You are [Brand Name]'s friendly customer service assistant on WhatsApp.
You help customers in Uganda with [core services].
Always be warm, helpful, and honest.
If you do not know something, say so and offer to connect the customer with a human.
Never make up prices, availability, or delivery timelines.
Respond in the same language the customer uses.
```

### Step 4: Define HITL escalation triggers

Hand off to a human agent when:
- Customer uses words: "complaint", "refund", "legal", "manager", "angry", "cheated"
- Same issue raised more than twice without resolution
- Query involves a transaction above a defined value threshold
- Customer explicitly requests a human
- LLM confidence falls below acceptable threshold

Handoff message: "I'm connecting you to one of our team members now. They'll be with you shortly — usually within [X] minutes during business hours."

### Step 5: Build the knowledge base input

Compile the brand knowledge base (see `ai-rag-brand-knowledge-base`):
- Full product/service catalogue with prices in UGX
- FAQs with approved answers
- Policies: returns, delivery, payment methods
- Business hours and location(s)
- Team names and roles for escalation routing

## Tool Options

| Tool | Best for | EA accessibility | Approx. cost |
|---|---|---|---|
| WATI | WhatsApp Business API + chatbot builder | Yes | From $49/month USD |
| Respond.io | Multi-channel + WhatsApp + LLM integration | Yes | From $79/month USD |
| Interakt | Africa/India-focused WhatsApp tool | Yes | From $15/month USD |
| Twilio | Developer-friendly WhatsApp API | Requires developer | Pay-per-message |
| Meta Cloud API | Maximum control | Requires developer | Pay-per-message |

## Measurement Framework

Track monthly:
- **Containment rate:** % of conversations resolved without human escalation (target: 60–80% for a mature bot)
- **First response time:** Customer message to first bot reply (target: under 30 seconds)
- **CSAT score:** Ask after resolution — "How satisfied were you? Reply 1–5"
- **Escalation rate:** % of conversations handed to a human (spikes indicate bot gaps)
- **Conversion rate:** For sales bots — % of conversations resulting in a purchase or booking

## Quality Criteria

- Conversation flows are mapped for the top 10 customer query types
- Social presence principles are embedded in all bot messages — no cold or corporate language
- HITL escalation triggers are explicitly defined with a handoff message template
- LLM system prompt is written, specifying brand voice and knowledge boundaries
- Knowledge base input document is compiled and ready for upload
- Tool recommendation is specific to client budget and technical capacity
- Measurement framework includes at least 4 KPIs with targets
- Uganda Data Protection and Privacy Act (2019) compliance noted

## References

- Boustany, S. (2024) *Generative AI for Social Media Marketing*.
- Ltifi, M. (ed.) (2025) *Advances in Digital Marketing in the Era of Artificial Intelligence*. CRC Press.
- Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn. Mercury Learning.

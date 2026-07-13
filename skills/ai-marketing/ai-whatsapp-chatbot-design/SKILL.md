---
name: ai-whatsapp-chatbot-design
description: Use when AI WhatsApp Chatbot Design is needed to produce a AI whatsapp chatbot design deliverable for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI WhatsApp Chatbot Design

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **AI whatsapp chatbot design deliverable** and the supplied brief falls within ai whatsapp chatbot design.

## Do Not Use When
- Use `ai-readiness-diagnostic` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| AI marketing use-case brief, intended human control point and success measure | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified AI whatsapp chatbot design deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact AI whatsapp chatbot design deliverable, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete AI whatsapp chatbot design deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Ai whatsapp chatbot design deliverable | Requester, client reviewer or delivery team | The AI whatsapp chatbot design deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source/assumption register and completed release checklist | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested AI whatsapp chatbot design deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

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

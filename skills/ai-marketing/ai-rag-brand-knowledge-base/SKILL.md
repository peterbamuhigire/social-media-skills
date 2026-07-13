---
name: ai-rag-brand-knowledge-base
description: Use when AI RAG Brand Knowledge Base is needed to produce a AI rag brand knowledge base deliverable for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI RAG Brand Knowledge Base

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **AI rag brand knowledge base deliverable** and the supplied brief falls within ai rag brand knowledge base.

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
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified AI rag brand knowledge base deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact AI rag brand knowledge base deliverable, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete AI rag brand knowledge base deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Ai rag brand knowledge base deliverable | Requester, client reviewer or delivery team | The AI rag brand knowledge base deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested AI rag brand knowledge base deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## Required Input
Ask for the following before proceeding:

1. **Client business name** — the trading name as it appears on communications
2. **Industry** — e.g. retail, financial services, hospitality, healthcare, agribusiness
3. **Country/city** — default is Uganda/Kampala unless stated otherwise
4. **Primary AI use case** — select one or more:
   - Content creation (captions, blog posts, email copy)
   - Customer service (chatbot or AI-assisted responses)
   - Strategy and planning (briefing, reporting, ideation)
5. **Existing documents available** — check which the client can supply:
   - Brand guide (logo usage, colours, typography, tone of voice)
   - Product or service catalogue
   - Past campaign files (briefs, reports, post-mortems)
   - Audience personas or customer research
   - Competitor analysis or market notes
   - Policy documents (returns, delivery, payment, warranties)

## What Is RAG and Why It Matters
Standard AI language models generate outputs from patterns learned across the internet. They do not
know a client's brand name, product range, pricing, tone of voice, or customer context unless that
information is provided in every prompt. The result: AI outputs that are generic, factually
unreliable, and off-brand.

Retrieval-Augmented Generation (RAG) solves this by connecting an LLM to a client-specific document
library. When a team member submits a query, the AI retrieves the relevant documents from the
library first, then generates a response grounded in those documents. The output is no longer drawn
from generic internet knowledge — it is drawn from the client's actual brand, products, and market
context (Sweenor and Mulkers, 2024).

**Practical effect for a content team:**

- Captions reference the correct product names, prices in UGX, and brand tone automatically
- Customer service AI gives accurate answers about delivery times, payment options, and policies
- Strategy documents reflect the client's actual audience, not a generic East African consumer

RAG does not require technical infrastructure beyond a paid subscription to a tool such as Claude
Projects or ChatGPT Projects. The investment is in document preparation, not engineering.

## What to Include in the Knowledge Base
Organise documents into seven categories. Each category should be a separate file or section — do
not combine unrelated content in a single document.

### 1. Brand Identity
- Logo usage rules (when to use full logo vs icon, clear-space requirements)
- Colour palette with hex codes and named colours
- Typography: primary and secondary fonts, use cases
- Tone-of-voice guide: 3–5 adjectives describing the brand voice, with written examples
- Taglines and brand statements — both current and retired (label retired items clearly)
- Words and phrases the brand always uses and those it never uses

### 2. Audience
- Customer personas: name, age range, occupation, income level, platform use, goals, pain points
- Customer segments with behavioural notes (e.g. "price-sensitive first-time buyers" vs
  "loyal repeat customers who respond to exclusivity")
- Language preferences: formal vs informal register, English vs Luganda phrases, vocabulary level
- Common objections and how the brand addresses them

### 3. Products and Services
- Full catalogue with current names, descriptions, prices in UGX (and USD where relevant)
- Key features and benefits per product — written from the customer's perspective
- FAQs: the questions customers actually ask, with the brand's approved answers
- Bundles, promotions, and seasonal offers — date-stamped and updated when they change
- Discontinued products listed separately so AI does not reference them

### 4. Past Campaigns
- Campaign name, dates, objective, key messages, and target audience
- What worked: highest-performing content formats, hooks, calls to action
- What did not work: formats or messages that underperformed and why
- Audience responses: notable comments, sentiment shifts, verbatim customer quotes
- Lessons applied to future campaigns

### 5. Competitor Notes
- Named local competitors with their positioning statements
- Key differentiators: where the client is stronger, where competitors have an edge
- Competitor claims to avoid repeating (to prevent the AI from inadvertently echoing them)
- Market context: who leads the category and why

### 6. Policies
- Returns and refund policy (exact terms, not paraphrased)
- Delivery: areas covered, lead times, costs — specific to Kampala, upcountry, and international
- Payment methods accepted (mobile money, card, cash, BNPL, instalments)
- Warranties and guarantees
- Data handling note: reference Uganda Data Protection and Privacy Act (2019) compliance for
  any document containing customer data

### 7. Local Market Context
- Ugandan public holidays relevant to the business with dates (e.g. Independence Day 9 Oct,
  Christmas, Eid al-Adha, Martyrs' Day 3 June)
- Cultural events: Kampala City Festival, end-of-year school cycle, agricultural seasons
- Seasonal buying patterns specific to the business
- Regional language notes: English register standard in formal communications; common Luganda
  greetings and phrases appropriate for informal content
- Economic context: notes on price sensitivity, mobile-first purchasing behaviour, and
  WhatsApp as the primary customer channel

## How to Structure Documents for LLM Retrieval
The quality of AI outputs depends directly on the quality of documents in the knowledge base.
Apply these rules to every document before adding it to the base.

**Use clear headings and subheadings.** LLMs interpret structure. A document with headings such
as "Delivery — Kampala" and "Delivery — Upcountry" retrieves more accurately than unstructured
paragraphs. Use H2 and H3 headings consistently.

**One topic per document.** Do not mix the brand guide with product pricing. Do not add policy
terms into a tone-of-voice document. Separate files improve retrieval precision.

**State facts explicitly.** Write "Our standard delivery time is 2–3 business days within Kampala"
not "we deliver quickly." Write "The price of [Product X] is UGX 85,000" not "competitively
priced." Vague language produces vague AI outputs.

**Avoid ambiguous pronouns.** Use the brand name throughout, not "we" or "they." Write "Karibu
Foods ships orders on Monday, Wednesday, and Friday" not "we ship three days a week."

**Date-stamp every document.** Add "Updated [Month Year]" to the header of every file. Example:
"Updated March 2026." This prevents team members from loading outdated versions.

**Remove outdated information.** Stale data degrades output quality more than missing data.
A discontinued product still in the knowledge base will appear in AI-generated captions. Delete
or archive it. If archiving, label the file clearly: "ARCHIVED — do not load."

## Tool Options
Select the tool that matches the client's budget, technical capacity, and primary use case.

| Tool | Best for | EA accessibility | Approx. cost |
|---|---|---|---|
| Claude Projects | Persistent document context per project; best for strategy, writing, and planning | Yes — browser-based, no install | Included in Claude Pro (~$20/month USD) |
| ChatGPT Projects | Same functionality for OpenAI users; strong for content creation | Yes — browser-based | Included in ChatGPT Plus (~$20/month USD) |
| CustomGPT.ai | Custom-branded knowledge base with shareable link and API access | Yes — cloud-based | From $49/month USD |
| Notion AI | RAG within an existing Notion workspace; suits teams already using Notion | Yes — cloud-based | From $10/month USD per member |
| Mem.ai | AI knowledge management with auto-organisation; suits smaller teams | Yes — free tier available | Free tier; paid from $14.99/month USD |

**Recommendation for most Ugandan SME clients:** Claude Projects or ChatGPT Projects. Both are
accessible on standard internet connections, require no technical setup, and cost under $25/month.
Recommend clients start here before investing in a dedicated platform.

## Query Workflow for Content Creators
Document this workflow and share it with every team member who uses the knowledge base.

**Step 1 — Open the knowledge base tool.**
Open the designated project in Claude Projects, ChatGPT Projects, or the chosen platform. Confirm
the correct project is active (not a generic session without documents loaded).

**Step 2 — State the task with explicit brand context.**
Structure every query as: "Using our [document name], [task description] for [product/service]
targeting [persona name]."

Example: "Using our brand guide and product catalogue, write an Instagram caption for the Deluxe
Mattress targeting the Young Professional persona. Include the UGX price and a call to action
linking to the website."

The more specific the query, the more grounded the output.

**Step 3 — Review output against brand standards before publishing.**
Check: correct product name and price, brand tone matches the voice guide, no unverified claims,
culturally appropriate for the target audience. Do not publish without this review.

**Step 4 — If output is off-brand, update the knowledge base — do not just re-prompt.**
Re-prompting without fixing the source document produces the same error next time. Identify which
document was missing or unclear, update it, date-stamp it, and reload it into the project. This is
the maintenance discipline that compounds knowledge base quality over time.

## Maintenance Protocol
Schedule a quarterly review. Assign a named owner — this is typically the social media manager or
content lead.

**Quarterly review checklist:**

1. Open every document and verify: prices are current, product names are correct, no discontinued
   items remain, campaign references are up to date
2. Remove any document labelled ARCHIVED that has not been referenced in the past six months
3. Add new personas, products, seasonal context, or market notes gathered since the last review
4. Update public holiday and cultural events calendar for the coming quarter
5. Run five common queries against the updated base — e.g. "Write a caption for [current product]",
   "Answer a customer question about delivery to Jinja", "Suggest a content idea for [upcoming
   holiday]"
6. Compare output quality to the previous quarter's baseline and note improvements or regressions
7. Brief the content team on any changes to documents or approved language

**Trigger an unscheduled review when:**
- A product is launched, discontinued, or repriced
- A campaign launches or concludes
- A competitor makes a significant move
- The brand refreshes its tone of voice or visual identity
- A new team member joins who will use the knowledge base

## EA Calibration
Prioritise these local market context documents for Ugandan and East African clients. They are the
most common gap between generic AI output and locally relevant content.

**Ugandan public holidays and cultural events.** Load a calendar document covering the current year.
Include Independence Day (9 October), Liberation Day (26 January), Martyrs' Day (3 June), Heroes'
Day (9 June), Christmas, Eid al-Fitr, Eid al-Adha, and any business-relevant trade fairs,
festivals, or academic events.

**Local pricing context.** All prices must appear in UGX first. Where USD is used (e.g. imported
goods, software subscriptions), include the UGX equivalent at current rate with the date of
conversion noted. AI models that only see USD pricing produce captions and copy that alienate
local audiences.

**Regional language preferences.** Document the client's approved register: formal written English
for professional sectors; relaxed English mixed with Luganda greetings for consumer brands.
Include approved Luganda phrases (e.g. "Webale nnyo" for "thank you very much", "Nsanyuse" for
"I am pleased/welcome") and note where each is appropriate.

**Local competitor names and positioning.** Name the actual Ugandan or EA competitors — not generic
global ones. AI models can otherwise generate competitive comparisons referencing irrelevant
international brands. Ground the comparison in the real local market.

## Quality Criteria
- Knowledge base covers all seven document types: brand identity, audience, products/services,
  past campaigns, competitor notes, policies, and local market context
- Every document is structured with clear headings, explicit factual statements, the brand name
  used in place of pronouns, and a date stamp
- Tool recommendation is matched to the client's budget, technical capacity, and primary use case
  — not defaulted to the most expensive option
- Query workflow is documented in writing and shared with all content team members before
  handover — not assumed knowledge
- Maintenance protocol is scheduled (quarterly minimum) with a named owner and a written checklist
- EA market context documents — public holidays, UGX pricing, language register, local competitors
  — are present and current at the time of handover
- At least five test queries are run against the completed knowledge base before handover, with
  outputs reviewed against brand standards
- Uganda Data Protection and Privacy Act (2019) compliance is noted on any document containing
  customer data (personas, customer quotes, contact information)

## References
Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn. Mercury Learning.

Sweenor, D.E. and Mulkers, Y. (2024) *Generative AI Business Applications*. TinyTechMedia.

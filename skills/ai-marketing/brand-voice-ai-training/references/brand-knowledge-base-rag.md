# Brand Knowledge Base for Retrieval-Augmented Generation (RAG)

Merged from skills/ai-marketing/ai-rag-brand-knowledge-base on 2026-09-29 at 7c60138; preservation map: [ai-rag-brand-knowledge-base.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/ai-rag-brand-knowledge-base.md)

## When to use this reference

Use it when the client needs more than a Brand Context Block: a document library that an AI tool retrieves from before it writes, so that captions, customer-service answers and strategy drafts use the client's real product names, UGX prices, policies, audience and local context. The Brand Context Block ([brand-context-block-method.md](brand-context-block-method.md) Steps 1–6) fixes *how* the brand sounds; the knowledge base fixes *what* the AI knows. Most clients need both: the block is loaded as one document inside the knowledge base, and the knowledge base supplies the facts the block cannot hold.

Typical triggers: the client uses AI for content creation, customer service (chatbot or AI-assisted replies) or strategy and planning, and outputs are generic, factually unreliable or off-brand.

## Why RAG matters

Standard AI language models generate outputs from patterns learned across the internet. They do not know a client's brand name, product range, pricing, tone of voice or customer context unless that information is supplied in every prompt. The result is output that is generic, factually unreliable and off-brand.

Retrieval-Augmented Generation (RAG) connects a large language model (LLM) to a client-specific document library. When a team member submits a query, the AI first retrieves the relevant documents from the library, then generates a response grounded in them. The output is drawn from the client's actual brand, products and market context rather than from generic internet knowledge (Sweenor and Mulkers, 2024).

Practical effect for a content team:

- Captions reference the correct product names, prices in UGX and brand tone automatically.
- Customer-service AI gives accurate answers about delivery times, payment options and policies.
- Strategy documents reflect the client's actual audience, not a generic East African consumer.

RAG needs no technical infrastructure beyond a paid subscription to a tool such as Claude Projects or ChatGPT Projects. The investment is in document preparation, not engineering.

## Inputs

Ask for the following before building the knowledge base (pull shared answers from the Brand Context Block inputs where already collected):

1. **Client business name** — the trading name as it appears on communications.
2. **Industry** — for example retail, financial services, hospitality, healthcare, agribusiness.
3. **Country/city** — default is Uganda/Kampala unless stated otherwise.
4. **Primary AI use case** — one or more of:
   - content creation (captions, blog posts, email copy);
   - customer service (chatbot or AI-assisted responses);
   - strategy and planning (briefing, reporting, ideation).
5. **Existing documents available** — check which the client can supply:
   - brand guide (logo usage, colours, typography, tone of voice);
   - product or service catalogue;
   - past campaign files (briefs, reports, post-mortems);
   - audience personas or customer research;
   - competitor analysis or market notes;
   - policy documents (returns, delivery, payment, warranties).

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| Client needs consistent voice only, few facts change | Brand Context Block alone ([brand-context-block-method.md](brand-context-block-method.md) Step 3) | Over-building a library nobody maintains |
| AI output repeats wrong prices, products or policies | Build the knowledge base; load the Brand Context Block as one of its documents | Factually wrong captions and customer answers |
| Choosing a tool | Match budget, technical capacity and primary use case; default most Ugandan SMEs to Claude Projects or ChatGPT Projects | Defaulting to the most expensive platform |
| Output is off-brand after a query | Fix and re-date the source document, then reload it; do not just re-prompt | The same error recurring next session |
| A document is outdated | Delete or archive it with the label "ARCHIVED — do not load" | Stale data, which degrades output more than missing data |
| A document holds customer data | Note Uganda Data Protection and Privacy Act (2019) compliance on it | Unlawful handling of personal data |

## What to include: seven document categories

Organise documents into seven categories. Each category is a separate file or section; do not combine unrelated content in a single document.

### 1. Brand identity
- Logo usage rules (when to use full logo vs icon; clear-space requirements).
- Colour palette with hex codes and named colours.
- Typography: primary and secondary fonts and their use cases.
- Tone-of-voice guide: 3–5 adjectives describing the brand voice, with written examples (the Brand Context Block serves here).
- Taglines and brand statements, current and retired (label retired items clearly).
- Words and phrases the brand always uses and those it never uses.

### 2. Audience
- Customer personas: name, age range, occupation, income level, platform use, goals, pain points.
- Customer segments with behavioural notes (for example "price-sensitive first-time buyers" vs "loyal repeat customers who respond to exclusivity").
- Language preferences: formal vs informal register, English vs Luganda phrases, vocabulary level.
- Common objections and how the brand addresses them.

### 3. Products and services
- Full catalogue with current names, descriptions, prices in UGX (and USD where relevant).
- Key features and benefits per product, written from the customer's perspective.
- FAQs: the questions customers actually ask, with the brand's approved answers.
- Bundles, promotions and seasonal offers, date-stamped and updated when they change.
- Discontinued products listed separately so the AI does not reference them.

### 4. Past campaigns
- Campaign name, dates, objective, key messages and target audience.
- What worked: highest-performing content formats, hooks, calls to action.
- What did not work: formats or messages that underperformed, and why.
- Audience responses: notable comments, sentiment shifts, verbatim customer quotes.
- Lessons applied to future campaigns.

### 5. Competitor notes
- Named local competitors with their positioning statements.
- Key differentiators: where the client is stronger, where competitors have an edge.
- Competitor claims to avoid repeating (so the AI does not inadvertently echo them).
- Market context: who leads the category and why.

### 6. Policies
- Returns and refund policy (exact terms, not paraphrased).
- Delivery: areas covered, lead times and costs — specific to Kampala, upcountry and international.
- Payment methods accepted (mobile money, card, cash, BNPL, instalments).
- Warranties and guarantees.
- Data handling note: reference Uganda Data Protection and Privacy Act (2019) compliance for any document containing customer data.

### 7. Local market context
- Ugandan public holidays relevant to the business, with dates (for example Independence Day 9 October, Christmas, Eid al-Adha, Martyrs' Day 3 June).
- Cultural events: Kampala City Festival, end-of-year school cycle, agricultural seasons.
- Seasonal buying patterns specific to the business.
- Regional language notes: English register standard in formal communications; common Luganda greetings and phrases appropriate for informal content.
- Economic context: price sensitivity, mobile-first purchasing behaviour, and WhatsApp as the primary customer channel.

## Procedure

### Step A — Structure every document for LLM retrieval

Output quality depends directly on document quality. Apply these rules to every document before adding it to the base:

- **Use clear headings and subheadings.** LLMs interpret structure. Headings such as "Delivery — Kampala" and "Delivery — Upcountry" retrieve more accurately than unstructured paragraphs. Use H2 and H3 headings consistently.
- **One topic per document.** Do not mix the brand guide with product pricing, or add policy terms to a tone-of-voice document. Separate files improve retrieval precision.
- **State facts explicitly.** Write "Our standard delivery time is 2–3 business days within Kampala", not "we deliver quickly". Write "The price of [Product X] is UGX 85,000", not "competitively priced". Vague language produces vague AI outputs.
- **Avoid ambiguous pronouns.** Use the brand name throughout, not "we" or "they". Write "Karibu Foods ships orders on Monday, Wednesday and Friday", not "we ship three days a week".
- **Date-stamp every document.** Add "Updated [Month Year]" to the header of every file (for example "Updated March 2026") so team members do not load outdated versions.
- **Remove outdated information.** Stale data degrades output quality more than missing data; a discontinued product left in the base will appear in AI-generated captions. Delete or archive it; if archiving, label the file "ARCHIVED — do not load".

### Step B — Choose the tool

Select the tool that matches the client's budget, technical capacity and primary use case.

| Tool | Best for | EA accessibility | Approx. cost |
|---|---|---|---|
| Claude Projects | Persistent document context per project; best for strategy, writing and planning | Yes — browser-based, no install | Included in Claude Pro (~USD 20/month) |
| ChatGPT Projects | Same functionality for OpenAI users; strong for content creation | Yes — browser-based | Included in ChatGPT Plus (~USD 20/month) |
| CustomGPT.ai | Custom-branded knowledge base with shareable link and API access | Yes — cloud-based | From USD 49/month |
| Notion AI | RAG within an existing Notion workspace; suits teams already using Notion | Yes — cloud-based | From USD 10/month per member |
| Mem.ai | AI knowledge management with auto-organisation; suits smaller teams | Yes — free tier available | Free tier; paid from USD 14.99/month |

Prices were recorded at the time the source skill was written; verify current pricing before quoting it to a client.

**Recommendation for most Ugandan SME clients:** Claude Projects or ChatGPT Projects. Both work on standard internet connections, need no technical setup and cost under USD 25/month. Recommend clients start here before investing in a dedicated platform.

### Step C — Load East Africa calibration documents

Prioritise these local-context documents for Ugandan and East African clients; they are the most common gap between generic AI output and locally relevant content.

- **Ugandan public holidays and cultural events.** Load a calendar covering the current year: Independence Day (9 October), Liberation Day (26 January), Martyrs' Day (3 June), Heroes' Day (9 June), Christmas, Eid al-Fitr, Eid al-Adha, and any business-relevant trade fairs, festivals or academic events.
- **Local pricing context.** All prices appear in UGX first. Where USD is used (for example imported goods, software subscriptions), include the UGX equivalent at the current rate with the conversion date noted. AI models that see only USD pricing produce copy that alienates local audiences.
- **Regional language preferences.** Document the client's approved register: formal written English for professional sectors; relaxed English mixed with Luganda greetings for consumer brands. Include approved Luganda phrases (for example "Webale nnyo" for "thank you very much", "Nsanyuse" for "I am pleased/welcome") and note where each is appropriate.
- **Local competitor names and positioning.** Name the actual Ugandan or East African competitors, not generic global ones. Otherwise the AI can generate comparisons with irrelevant international brands.

### Step D — Document the query workflow for content creators

Write this workflow down and share it with every team member who uses the knowledge base.

1. **Open the knowledge base tool.** Open the designated project in Claude Projects, ChatGPT Projects or the chosen platform. Confirm the correct project is active (not a generic session without documents loaded).
2. **State the task with explicit brand context.** Structure every query as: "Using our [document name], [task description] for [product/service] targeting [persona name]." Example: "Using our brand guide and product catalogue, write an Instagram caption for the Deluxe Mattress targeting the Young Professional persona. Include the UGX price and a call to action linking to the website." The more specific the query, the more grounded the output.
3. **Review output against brand standards before publishing.** Check the product name and price are correct, the tone matches the voice guide, there are no unverified claims, and the content is culturally appropriate for the target audience. Do not publish without this review.
4. **If output is off-brand, update the knowledge base — do not just re-prompt.** Re-prompting without fixing the source document produces the same error next time. Identify which document was missing or unclear, update it, date-stamp it and reload it into the project. This maintenance discipline compounds knowledge base quality over time.

### Step E — Maintain the knowledge base

Schedule a quarterly review with a named owner, typically the social media manager or content lead. Align it with the Brand Context Block review ([brand-context-block-method.md](brand-context-block-method.md) Step 6).

Quarterly review checklist:

1. Open every document and verify: prices are current, product names are correct, no discontinued items remain, campaign references are up to date.
2. Remove any document labelled ARCHIVED that has not been referenced in the past six months.
3. Add new personas, products, seasonal context or market notes gathered since the last review.
4. Update the public holiday and cultural events calendar for the coming quarter.
5. Run five common queries against the updated base — for example "Write a caption for [current product]", "Answer a customer question about delivery to Jinja", "Suggest a content idea for [upcoming holiday]".
6. Compare output quality with the previous quarter's baseline and note improvements or regressions.
7. Brief the content team on any changes to documents or approved language.

Trigger an unscheduled review when:

- a product is launched, discontinued or repriced;
- a campaign launches or concludes;
- a competitor makes a significant move;
- the brand refreshes its tone of voice or visual identity;
- a new team member who will use the knowledge base joins.

## Handover checklist (quality criteria)

- [ ] The knowledge base covers all seven document types: brand identity, audience, products/services, past campaigns, competitor notes, policies and local market context.
- [ ] Every document has clear headings, explicit factual statements, the brand name in place of pronouns, and a date stamp.
- [ ] The tool recommendation matches the client's budget, technical capacity and primary use case — not defaulted to the most expensive option.
- [ ] The query workflow is documented in writing and shared with all content team members before handover — not assumed knowledge.
- [ ] The maintenance protocol is scheduled (quarterly minimum) with a named owner and a written checklist.
- [ ] East African market context documents — public holidays, UGX pricing, language register, local competitors — are present and current at handover.
- [ ] At least five test queries have been run against the completed base before handover, with outputs reviewed against brand standards.
- [ ] Uganda Data Protection and Privacy Act (2019) compliance is noted on any document containing customer data (personas, customer quotes, contact information).

## Sources

- Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn. Mercury Learning.
- Sweenor, D.E. and Mulkers, Y. (2024) *Generative AI Business Applications*. TinyTechMedia.

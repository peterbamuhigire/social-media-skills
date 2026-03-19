# AI Skills Enhancement — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Strengthen 7 existing AI skills and create 9 new ones using frameworks extracted from 12 books on AI in marketing and business management.

**Architecture:** Three sequential batches of SKILL.md edits and creations. Each skill file lives in its own folder (`skill-name/SKILL.md`). No code, no tests — quality verification is a manual read-through against the checklist. Commit after each batch.

**Tech Stack:** Markdown, YAML frontmatter, British English, Uganda/East Africa defaults. All conventions from `CLAUDE.md`. Design doc at `docs/plans/2026-03-19-ai-skills-enhancement-design.md`.

---

## Reference: Quality Checklist (run before every commit)

For every SKILL.md touched in a task, verify:
- [ ] Frontmatter has `name` and `description` only
- [ ] `description` states what the skill does AND when to invoke it
- [ ] Has **Required Input** section (client name, industry, country/city, primary goal + skill-specific inputs)
- [ ] Has **Quality Criteria** section (5–8 bullets)
- [ ] British English throughout (organisation, colour, programme, analyse, recognise)
- [ ] Imperative language ("Ask for…", "Generate…", "Apply…")
- [ ] Under 500 lines
- [ ] Uganda/East Africa default market applied where relevant
- [ ] At least 2 source books cited in body

---

## BATCH 1: Strengthen Existing Skills

---

### Task 1: Strengthen `ai-readiness-diagnostic`

**Files:**
- Modify: `ai-readiness-diagnostic/SKILL.md`

**Step 1: Read the existing file**

Read `ai-readiness-diagnostic/SKILL.md` in full. Note current structure and line count.

**Step 2: Add Venkatesan's 2×2 Use Case Matrix**

After the existing diagnostic items, insert a new section:

```markdown
## AI Use Case Matrix (Venkatesan and Lecinski, 2026)

Once the diagnostic score is known, map the client's AI readiness to the 2×2 Use Case Matrix:

|  | **Internal** | **External** |
|---|---|---|
| **Productivity** | Automate internal workflows: reporting, content briefs, data analysis | Scale customer-facing functions: chatbots, FAQs, WhatsApp automation |
| **Growth** | Build proprietary data and algorithmic advantages | Deliver personalised customer experiences at scale |

**Recommendation by score:**
- Score 0–25%: Start in Internal/Productivity quadrant only
- Score 26–50%: Internal/Productivity + begin External/Productivity pilot
- Score 51–75%: All four quadrants in scope; prioritise highest-ROI cell
- Score 76–100%: Full AI transformation; consider Monetisation (Canvas Step 5)
```

**Step 3: Add Nayebi's Three-Wave Maturity Labels**

Insert after the Use Case Matrix:

```markdown
## AI Maturity Wave Assessment (Nayebi, 2025)

Identify which wave the client currently operates in:

- **Wave 1 — Automation:** Rules-based workflows, scheduled posts, canned responses, basic chatbots. Most EA SMEs are here.
- **Wave 2 — Predictive ML:** Customer segmentation, engagement prediction, A/B test optimisation, sentiment analysis. Achievable for EA mid-market clients.
- **Wave 3 — Agentic AI:** Autonomous agents that perceive, reason, act, and learn without human prompts. Horizon planning for EA; immediate for multinational clients.

Ask the client: "Which wave best describes your current AI marketing activity?" Use their answer to calibrate the roadmap in the final section.
```

**Step 4: Verify quality checklist**

Run the checklist above. Fix any issues.

**Step 5: Commit**

```bash
git add ai-readiness-diagnostic/SKILL.md
git commit -m "Strengthen ai-readiness-diagnostic: add 2x2 use case matrix + 3-wave maturity (Venkatesan, Nayebi)"
```

---

### Task 2: Strengthen `ai-marketing-canvas-assessment`

**Files:**
- Modify: `ai-marketing-canvas-assessment/SKILL.md`

**Step 1: Read the existing file**

Read in full. Note where Step 4 ends so Step 5 additions slot in cleanly.

**Step 2: Add Canvas Step 5 — Monetisation**

Find the Step 4 section and insert Step 5 after it:

```markdown
### Step 5 — Monetisation

At this stage, AI capabilities become a source of competitive advantage and new revenue:
- AI-powered products or services sold to customers (e.g. personalisation engine licensed to partners)
- Proprietary audience data monetised through partnerships
- AI-driven efficiency gains reinvested into market expansion
- Brand reputation as an AI-first organisation attracts premium clients and talent

**Consultancy note:** Most EA clients will not reach Step 5 within a 12-month engagement. Frame it as a 3–5 year horizon goal and use it to demonstrate the long-term value of starting the Canvas journey now.
```

**Step 3: Add Agile Sprint Methodology**

Add a new section near the end:

```markdown
## Agile Sprint Approach (Venkatesan and Lecinski, 2026)

AI marketing initiatives fail when treated as annual strategic plans. Recommend monthly sprint cycles:

1. **Sprint planning (Day 1):** Select one AI use case to test this month
2. **Pilot execution (Days 2–20):** Run the experiment with a defined audience segment
3. **Measurement (Days 21–25):** Compare AI-assisted results vs human-led baseline
4. **Review (Days 26–28):** Replicate, iterate, or abandon
5. **Next sprint (Day 30):** Select next use case based on learnings

KPI for each sprint: measure lift vs human-led control. A 10% improvement justifies scaling.
```

**Step 4: Add AI-to-AI Marketing section**

```markdown
## AI-to-AI Marketing Readiness

As consumers increasingly use AI agents (ChatGPT, Perplexity, Google Gemini) to research, compare, and purchase, brands must be readable by machines, not just humans. Assess:

- Are product pages structured with clear, machine-parseable pricing and features?
- Are brand values explicitly stated in accessible, factual language?
- Is content well-sourced and factually accurate (LLMs avoid citing inaccurate sources)?
- Does the website use structured data markup (Schema.org)?

This is a 2–5 year horizon for most EA markets but should inform content architecture decisions now.
```

**Step 5: Verify quality checklist, then commit**

```bash
git add ai-marketing-canvas-assessment/SKILL.md
git commit -m "Strengthen ai-marketing-canvas-assessment: add Step 5 monetisation, agile sprints, AI-to-AI marketing"
```

---

### Task 3: Strengthen `prompt-engineering-library`

**Files:**
- Modify: `prompt-engineering-library/SKILL.md`

**Step 1: Read the existing file**

Note current prompt frameworks so additions are additive, not duplicative.

**Step 2: Add Erné's 5-Step Perfect Prompt**

```markdown
## The 5-Step Perfect Prompt (Erné, 2024)

The single most impactful prompting improvement is always Step 1 — assigning a role:

1. **Role:** "You are a senior social media strategist specialising in East African consumer markets…"
2. **Context:** "The client is [name], a [industry] business in [city], targeting [audience]…"
3. **Task:** "Write a 90-day content calendar for their Instagram account…"
4. **Format:** "Output as a table with columns: Week, Theme, Post Type, Caption Draft, Hashtags"
5. **Constraints:** "Keep captions under 150 words. Use British English. Reference local events where relevant."

**EA calibration tip:** Always include Uganda/East Africa explicitly in the Role and Context steps. Generic AI outputs default to Western market assumptions.
```

**Step 3: Add Roth's 8 Golden Rules**

```markdown
## 8 Golden Rules of Prompting (Roth and neuroflash, 2024)

1. Be precise and specific — vague prompts produce generic outputs
2. Define the target audience explicitly
3. Use a clear instruction verb: Create / Write / Describe / Analyse / List
4. Set the desired tone and style ("professional but warm", "conversational", "authoritative")
5. Avoid ambiguities — if two interpretations are possible, the AI will pick the wrong one
6. Focus on essentials — one task per prompt
7. Use positive phrasing — state what to do, not what to avoid
8. Add context — platform, format, purpose, audience size

**Quick test:** Before sending any prompt, check it against all 8 rules. If it fails 3 or more, rewrite.
```

**Step 4: Add MVOSSTE Prompting Workflow**

```markdown
## MVOSSTE Prompting Workflow (Randazzo, 2024)

Use this sequence when developing full marketing strategies with AI assistance:

| Step | Prompt focus |
|---|---|
| **Mission** | "Draft 3 mission statement options for [client] that reflect [values]…" |
| **Vision** | "Write a 5-year vision statement assuming [growth scenario]…" |
| **Objective** | "Generate 5 SMART marketing objectives for [goal] in [timeframe]…" |
| **Situation** | "Conduct a SWOT analysis for [client] in [industry] in [market]…" |
| **Strategy** | "Suggest 3 strategic options for achieving [objective], with trade-offs…" |
| **Tactics** | "List 10 specific social media tactics for [strategy] with [budget] budget…" |
| **Execution** | "Create a 30-day action plan with weekly milestones for [tactic]…" |

**Professional practice:** Footnote every AI-generated output with the prompt used. This enables clients to audit, reproduce, and modify outputs.
```

**Step 5: Verify quality checklist, then commit**

```bash
git add prompt-engineering-library/SKILL.md
git commit -m "Strengthen prompt-engineering-library: add 5-step perfect prompt, 8 golden rules, MVOSSTE workflow"
```

---

### Task 4: Strengthen `ai-content-humaniser`

**Files:**
- Modify: `ai-content-humaniser/SKILL.md`

**Step 1: Read the existing file**

**Step 2: Add Content Recycling Pipeline**

```markdown
## Content Recycling Pipeline (Roth and neuroflash, 2024)

One well-researched piece of content can become 10 platform-ready assets in under 60 minutes:

| Step | Output | AI Tool |
|---|---|---|
| 1. Master content (blog/article) | 800–1,200 word source piece | Claude/ChatGPT |
| 2. Extract 5 key points | Bullet summary | Claude/ChatGPT |
| 3. Facebook caption | 100–150 words, conversational | Claude/ChatGPT |
| 4. Instagram caption | 50–80 words + hashtags | Claude/ChatGPT |
| 5. LinkedIn post | 150–200 words, professional | Claude/ChatGPT |
| 6. TikTok/Reels script | 30-second spoken script | Claude/ChatGPT |
| 7. X/Twitter post | Under 280 characters | Claude/ChatGPT |
| 8. Carousel outline | 5-slide structure with headlines | Claude/ChatGPT |
| 9. Email snippet | 80-word newsletter paragraph | Claude/ChatGPT |
| 10. Quote card text | Single compelling sentence | Claude/ChatGPT |

**Platform adaptation checklist:**
- Facebook: conversational, question or call-to-action, link preview works
- Instagram: emotional hook first, hashtags at end or in comment, no clickable links in caption
- LinkedIn: insight or lesson first, professional register, invite discussion
- TikTok/Reels: hook in first 3 seconds, spoken register, trending audio suggestion
- WhatsApp Status: under 700 characters, image-first, direct CTA

**Quality gate:** Every variant must pass the content humaniser checklist before publishing. Volume without quality is worse than no content.
```

**Step 3: Add AI spam detection awareness**

```markdown
## The Rising Quality Bar

Platform algorithms increasingly detect and suppress low-quality AI-generated content (Roth and neuroflash, 2024). The human layer — strategic direction, local cultural context, brand voice — becomes more valuable, not less, as AI content volume increases.

Signs that AI content will be flagged or underperform:
- Generic phrasing with no specific local context
- No genuine point of view or opinion
- Repetitive sentence structures
- Missing cultural references or local events
- Tone inconsistency across a single post

The content humaniser exists precisely to prevent these failure modes.
```

**Step 4: Verify quality checklist, then commit**

```bash
git add ai-content-humaniser/SKILL.md
git commit -m "Strengthen ai-content-humaniser: add content recycling pipeline + quality bar section"
```

---

### Task 5: Strengthen `playbook-ai-automation-workflow`

**Files:**
- Modify: `playbook-ai-automation-workflow/SKILL.md`

**Step 1: Read the existing file**

**Step 2: Add Zapier/Make.com no-code stack**

```markdown
## No-Code Automation Stack (Erné, 2024)

Combine AI intelligence with workflow automation using two layers:

**Layer 1 — Automation (Zapier or Make.com):**
- Connect data sources: Google Sheets, Meta Business Suite, WhatsApp Business, Mailchimp, Airtable
- Trigger actions: "When new lead form submitted → add to CRM → send welcome WhatsApp → notify account manager"
- Both tools have free tiers accessible to EA clients

**Layer 2 — Intelligence (Claude or ChatGPT API):**
- Analyse data: "Summarise this month's engagement data and identify 3 actionable insights"
- Generate content: "Draft a WhatsApp follow-up message for a lead who enquired about [service]"
- Route decisions: "Classify this customer complaint as urgent/standard/low-priority"

**Combining both:** Zapier/Make handles the plumbing (moving data between tools); Claude/ChatGPT handles the thinking (analysis and generation). Together they form a low-code AI consultancy engine.

**EA-accessible starter stack:**
- Zapier Free (5 Zaps) + Google Sheets + Gmail + WhatsApp Business API (Twilio or WATI)
- Estimated monthly cost: $0–$50 USD depending on volume
```

**Step 3: Add Multi-Agent Architecture primer**

```markdown
## Multi-Agent Architecture (HBR; Nayebi, 2025)

Rather than one general-purpose AI chatbot, advanced marketing operations use multiple specialised agents working in concert:

| Agent | Role | Tools |
|---|---|---|
| Research agent | Monitors trends, competitor activity, brand mentions | Perplexity, Brandwatch, Google Alerts |
| Copywriting agent | Drafts captions, emails, scripts from brief | Claude/ChatGPT with brand context |
| Analytics agent | Pulls performance data and generates insights | Meta Business Suite API, GA4 |
| Scheduling agent | Publishes approved content at optimal times | Buffer, Hootsuite, Later |

**Coordination:** A human consultant acts as the orchestrator — reviewing outputs from each agent, resolving conflicts, and making strategic decisions that require local knowledge or client relationship context.

**Implementation path:** Start with one agent (typically copywriting). Add agents one at a time as confidence grows.
```

**Step 4: Add HITL Escalation Protocol**

```markdown
## Human-in-the-Loop (HITL) Escalation Protocol (Nayebi, 2025)

Define clear thresholds so automation handles routine decisions and humans handle high-stakes ones:

| Decision type | AI handles | Human handles |
|---|---|---|
| Caption drafting | ✓ Draft | ✓ Final approval |
| Community management | ✓ Routine queries, FAQs | ✓ Complaints, crises, sensitive topics |
| Performance reporting | ✓ Data pull + narrative draft | ✓ Strategic commentary + client presentation |
| Campaign optimisation | ✓ A/B test suggestions | ✓ Budget reallocation decisions |
| Crisis response | ✗ Do not automate | ✓ Human-only, use crisis playbook |

**Protocol:** Every automated workflow must have a defined escalation trigger. When the trigger fires, a human receives an alert with full context and a recommended action. The human approves, modifies, or overrides.
```

**Step 5: Verify quality checklist, then commit**

```bash
git add playbook-ai-automation-workflow/SKILL.md
git commit -m "Strengthen playbook-ai-automation-workflow: add Zapier/Make stack, multi-agent architecture, HITL protocol"
```

---

### Task 6: Strengthen `ai-vendor-evaluation`

**Files:**
- Modify: `ai-vendor-evaluation/SKILL.md`

**Step 1: Read the existing file**

Note existing tool categories to ensure new categories are additive.

**Step 2: Add RAG tools category**

```markdown
### Category 9: RAG (Retrieval-Augmented Generation) Tools

Tools that connect LLMs to client-specific knowledge bases for accurate, on-brand output:

| Tool | Description | EA Accessibility | Approx. Cost |
|---|---|---|---|
| Claude Projects | Upload docs; persistent context per project | Yes — browser-based | Included in Claude Pro |
| ChatGPT Projects | Same as above for OpenAI | Yes — browser-based | Included in ChatGPT Plus |
| CustomGPT.ai | Build custom knowledge bases, API access | Yes — cloud-based | From $49/month USD |
| Notion AI | RAG within Notion workspace | Yes — cloud-based | From $10/month USD |
| Mem.ai | AI-powered knowledge management | Yes — cloud-based | Free tier available |

**Evaluation criteria:** How easily can client documents be uploaded? Does the tool maintain source attribution? Can multiple team members access the same knowledge base?
```

**Step 3: Add Synthetic Research Tools category**

```markdown
### Category 10: Synthetic Research and Persona Tools

Tools for generating AI-simulated audience research when primary fieldwork is unavailable:

| Tool | Description | EA Accessibility | Approx. Cost |
|---|---|---|---|
| Supernatural AI | Synthetic user personas for brand research | Limited — US-focused | Enterprise pricing |
| Glimpse | AI consumer research and audience analysis | Yes — cloud-based | From $99/month USD |
| Synthetic Users | Simulated user testing and focus groups | Yes — cloud-based | From $29/month USD |
| Claude/ChatGPT (prompted) | Structured persona generation via prompts | Yes | Included in existing subscription |

**EA note:** For most Ugandan SME clients, prompted persona generation via Claude/ChatGPT is the most accessible option. Supernatural AI and Glimpse are better suited to multinational clients with larger research budgets.
```

**Step 4: Add Agentic AI Tools category**

```markdown
### Category 11: Agentic AI and Automation Tools

Tools for building autonomous or semi-autonomous marketing agents:

| Tool | Description | EA Accessibility | Approx. Cost |
|---|---|---|---|
| Persado | AI language optimisation for copy and ads | Limited — enterprise | Enterprise pricing |
| OfferFit | AI experimentation for retention campaigns | Limited — enterprise | Enterprise pricing |
| Braze | AI-powered customer engagement platform | Yes — cloud-based | Enterprise pricing |
| n8n | Open-source workflow automation (self-hostable) | Yes — can self-host | Free (self-hosted) |
| Zapier AI | AI-enhanced workflow automation | Yes — cloud-based | Free tier; from $19.99/month |
| Make.com | Visual workflow builder with AI steps | Yes — cloud-based | Free tier; from $9/month |
| Claude API | Build custom agents and automations | Yes — API access | Pay-per-token |

**EA recommendation:** n8n (self-hosted on a local server) + Claude API is the most cost-effective agentic stack for EA-based consultancies. Zapier is the most accessible for clients with no technical resources.
```

**Step 5: Verify quality checklist, then commit**

```bash
git add ai-vendor-evaluation/SKILL.md
git commit -m "Strengthen ai-vendor-evaluation: add RAG tools, synthetic research tools, agentic AI tools categories"
```

---

### Task 7: Strengthen `training-ai-foundations`

**Files:**
- Modify: `training-ai-foundations/SKILL.md`

**Step 1: Read the existing file**

**Step 2: Add Co-Pilot vs Co-Thinker distinction**

```markdown
## Co-Pilot vs Co-Thinker (Farri and Rosani, 2025)

The most important distinction for any marketing team new to AI:

**Co-Pilot mode** — AI handles speed tasks:
- Summarising documents and reports
- Drafting first versions of captions, emails, briefs
- Generating slide content from bullet points
- Taking notes in meetings
- Formatting data into tables

**Co-Thinker mode** — AI acts as a thought partner for reflection-heavy work:
- Pressure-testing campaign strategy logic
- Mapping stakeholder perspectives the team may have overlooked
- Identifying assumptions in a brief that should be validated
- Framing the client's core marketing challenge as a solvable "quest"
- Generating alternative strategic options for evaluation

**When to use which:** Co-Pilot when you know what you want and need it done faster. Co-Thinker when you are not yet sure what the right answer is. Most marketing teams default to Co-Pilot only — they are leaving the most valuable AI capability unused.
```

**Step 3: Add Three-Wave Evolution Framework**

```markdown
## The Three Waves of AI in Marketing (Nayebi, 2025)

Help participants understand where they and their clients currently sit:

**Wave 1 — Automation (Most EA businesses today):**
Rules-based tools that follow fixed instructions. Examples: scheduled social posts, auto-reply chatbots, email drip sequences. No learning or adaptation. Reliable but rigid.

**Wave 2 — Predictive ML (Growing in EA):**
Systems that learn from data and predict future behaviour. Examples: audience segmentation models, engagement rate prediction, A/B test optimisation, sentiment analysis. Requires data. Improves over time.

**Wave 3 — Agentic AI (Horizon for EA):**
Autonomous agents that perceive their environment, reason about it, decide on actions, and learn from outcomes — without waiting for a human prompt. Examples: a content agent that monitors trending topics and drafts posts for approval; a campaign agent that detects low engagement and triggers a response campaign automatically.

**Exercise:** Ask participants to identify one marketing activity in their business at each wave level. Where is the gap between Wave 1 and Wave 2?
```

**Step 4: Verify quality checklist, then commit**

```bash
git add training-ai-foundations/SKILL.md
git commit -m "Strengthen training-ai-foundations: add Co-Pilot vs Co-Thinker, three-wave evolution framework"
```

---

## BATCH 2: New Operational Skills

---

### Task 8: Create `ai-whatsapp-chatbot-design`

**Files:**
- Create: `ai-whatsapp-chatbot-design/SKILL.md`

**Step 1: Create the folder and SKILL.md**

Write the complete file:

```markdown
---
name: ai-whatsapp-chatbot-design
description: >
  Design WhatsApp LLM chatbots for East African markets: conversation flows,
  social presence principles, trust-building, local language registers, and
  human escalation protocols. Invoke when a client wants to automate WhatsApp
  customer service, sales enquiries, or support using AI.
---

# AI WhatsApp Chatbot Design

## Required Input

Ask for:
- Client business name and industry
- Country/city (default: Uganda)
- Primary goal (customer service / sales enquiries / appointment booking / FAQ handling)
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
- **Avoid corporate coldness:** Never start with "Please select from the following options:"
- **Mirror the customer's register:** If they write formally, respond formally. If casually, match it.
- **Disclose AI nature** when directly asked — this builds trust, not erodes it (Uganda Data Protection and Privacy Act, 2019 requires transparency in automated data processing)

## Conversation Flow Design

### Step 1: Map the top 10 customer queries

Interview the client's human support team. List the 10 most common questions received via WhatsApp in the past month. These become the backbone of Layer 1 decision trees.

### Step 2: Design the decision tree

For each query type:
```
Customer: "What are your prices?"
→ Bot: "Our [service/product] packages start from UGX [X]. Which are you interested in?
   [Option A] [Option B] [Option C]"
→ If Option A selected: "Great choice! Here's what's included: [details].
   Ready to book? Reply YES or speak to our team."
```

### Step 3: Define LLM boundary

Specify which queries go to the LLM layer: open-ended product questions, complaint context gathering, multi-turn sales conversations. Write the system prompt for the LLM:

```
You are [Brand Name]'s friendly customer service assistant on WhatsApp.
You help customers in Uganda with [core services].
Always be warm, helpful, and honest.
If you do not know something, say so and offer to connect the customer with a human.
Never make up prices, availability, or delivery timelines.
Respond in the same language the customer uses.
```

### Step 4: Define HITL escalation triggers

The bot must hand off to a human agent when:
- Customer uses words: "complaint", "refund", "legal", "manager", "angry", "cheated"
- Same issue raised more than twice without resolution
- Query involves a specific order or transaction amount over [threshold]
- Customer explicitly requests a human
- LLM confidence score falls below threshold (if using API with confidence output)

Handoff message: "I'm connecting you to one of our team members now. They'll be with you shortly — usually within [X] minutes during business hours."

### Step 5: Build the knowledge base input

Compile the brand knowledge base document (see `ai-rag-brand-knowledge-base`):
- Full product/service catalogue with prices in UGX
- FAQs with approved answers
- Policies: returns, delivery, payment methods
- Business hours and location(s)
- Team names and roles for escalation routing

## Tool Options

| Tool | Best for | EA Accessibility | Cost |
|---|---|---|---|
| WATI | WhatsApp Business API + chatbot builder | Yes | From $49/month USD |
| Respond.io | Multi-channel + WhatsApp + LLM integration | Yes | From $79/month USD |
| Twilio | Developer-friendly WhatsApp API | Requires technical resource | Pay-per-message |
| Meta Cloud API (direct) | Maximum control, requires developer | Requires technical resource | Pay-per-message |
| Interakt | India/Africa focused WhatsApp tool | Yes | From $15/month USD |

## Measurement Framework

Track monthly:
- **Containment rate:** % of conversations resolved without human escalation (target: 60–80% for a mature bot)
- **First response time:** Time from customer message to first bot reply (target: under 30 seconds)
- **CSAT score:** Ask customers after resolution: "How satisfied were you? Reply 1–5"
- **Escalation rate:** % of conversations handed to a human (watch for spikes — indicates bot gaps)
- **Conversation-to-conversion rate:** For sales bots — % of conversations that result in a purchase or booking

## Quality Criteria

- Conversation flows are mapped for the top 10 customer query types
- Social presence principles are embedded in all bot messages — no cold, corporate language
- HITL escalation triggers are explicitly defined with a handoff message template
- LLM system prompt is written, specifying brand voice and boundaries
- Knowledge base input document is compiled and ready for upload
- Tool recommendation is specific to client budget and technical capacity
- Measurement framework includes at least 4 KPIs with targets
- Uganda Data Protection and Privacy Act (2019) compliance noted where relevant
```

**Step 2: Verify quality checklist**

Count lines (must be under 500). Confirm all required sections present.

**Step 3: Commit**

```bash
git add ai-whatsapp-chatbot-design/SKILL.md
git commit -m "Add ai-whatsapp-chatbot-design: WhatsApp LLM chatbot design for EA markets"
```

---

### Task 9: Create `ai-content-recycling-pipeline`

**Files:**
- Create: `ai-content-recycling-pipeline/SKILL.md`

**Step 1: Write the complete file**

```markdown
---
name: ai-content-recycling-pipeline
description: >
  Transform one piece of long-form content into 10 platform-ready assets using
  AI tools. Solves the content creation bottleneck for resource-constrained East
  African marketing teams. Invoke when a client needs more content output from
  their existing content investment.
---

# AI Content Recycling Pipeline

## Required Input

Ask for:
- Client business name and industry
- Country/city (default: Uganda)
- Source content (paste the blog post, article, or video transcript)
- Active social platforms (Facebook, Instagram, LinkedIn, TikTok, X, WhatsApp, YouTube)
- Brand voice description (formal/casual, warm/authoritative, etc.)
- Any topics or phrases to avoid

## The Core Principle

Most East African marketing teams create content once and publish it once. This wastes the research, thinking, and writing invested in each piece. AI makes it practical to extract 10 distinct, platform-optimised assets from a single source in under 60 minutes — without the output feeling repetitive (Roth and neuroflash, 2024).

The constraint is not content creation — it is content *extraction and reformatting*. AI removes that constraint.

## The 10-Asset Pipeline

### Source: One long-form piece (800–1,500 words)
A blog post, article, interview transcript, or video script.

---

**Asset 1 — Facebook post (100–150 words)**
Prompt: *"Extract the most surprising or counterintuitive insight from this article. Write a Facebook post that opens with that insight as a hook, explains it in 2–3 sentences, and ends with a discussion question. Warm, conversational tone. No hashtags."*

**Asset 2 — Instagram caption (50–80 words + hashtags)**
Prompt: *"Write an Instagram caption based on this article. Start with an emotional hook (not a question). Keep it under 80 words. Add 10 relevant hashtags at the end — a mix of branded, niche, and community tags for [industry] in Uganda."*

**Asset 3 — LinkedIn post (150–200 words)**
Prompt: *"Write a LinkedIn post based on this article. Start with a professional insight or data point. Use a short paragraph structure. End by inviting peers to share their experience. No hashtags. Professional but not stiff."*

**Asset 4 — TikTok / Reels script (30-second spoken)**
Prompt: *"Write a 30-second TikTok script based on this article. Hook in the first 3 seconds (bold statement or question). 3 punchy points. Strong CTA at the end ('Follow for more', 'Comment your answer'). Written to be spoken aloud — conversational, energetic."*

**Asset 5 — X / Twitter post (under 280 characters)**
Prompt: *"Extract the single most quotable sentence or statistic from this article. Rewrite it as a standalone X post under 280 characters. Add 2 relevant hashtags."*

**Asset 6 — Instagram carousel outline (5 slides)**
Prompt: *"Structure this article as a 5-slide Instagram carousel. Slide 1: Bold hook/title. Slides 2–4: One key point each with a 10-word headline and 15-word supporting line. Slide 5: Summary + CTA. Output as a slide-by-slide outline."*

**Asset 7 — WhatsApp Status / broadcast message (under 700 characters)**
Prompt: *"Write a WhatsApp broadcast message based on this article. Under 700 characters. Start with the most useful takeaway. One clear CTA at the end (visit link / reply for more / book now)."*

**Asset 8 — Email newsletter paragraph (80–100 words)**
Prompt: *"Write an 80-word paragraph for a client email newsletter based on this article. Professional, warm tone. Include a 'Read more' link placeholder. The paragraph should make the reader curious enough to click."*

**Asset 9 — Quote card text (one sentence)**
Prompt: *"Extract or craft the single most shareable, standalone sentence from this article — something that works as an inspirational or thought-provoking quote card. Under 20 words."*

**Asset 10 — Audio / podcast outline (3-minute spoken)**
Prompt: *"Structure this article as a 3-minute podcast segment outline: 30-second intro (hook + what we'll cover), 4 x 30-second points, 30-second outro (summary + CTA). Written for spoken delivery."*

---

## Platform Adaptation Rules

| Platform | Character limit | Tone | Key rule |
|---|---|---|---|
| Facebook | 63,206 (practical: 150) | Conversational | End with question or CTA |
| Instagram | 2,200 (practical: 80) | Emotional, visual | Hook in first line; hashtags last |
| LinkedIn | 3,000 (practical: 200) | Professional insight | Invite discussion |
| TikTok | 2,200 | Energetic, direct | Hook in 3 seconds |
| X / Twitter | 280 | Punchy, opinionated | One idea only |
| WhatsApp | 700 | Direct, warm | CTA must be actionable |
| Email | No limit (practical: 100) | Helpful, personal | Drive to one action |

## Quality Gate

Before publishing any asset, check:
- [ ] Does it make sense as a standalone piece — no context needed from other assets?
- [ ] Does the tone match the client's brand voice?
- [ ] Is there a local/Uganda reference or relevance where appropriate?
- [ ] Has it been read aloud (for spoken-word assets: TikTok, WhatsApp, podcast)?
- [ ] Are hashtags relevant and not overused?
- [ ] Has a human reviewed and approved — not published straight from AI output?

## Time Benchmarks

- Source content: existing (0 minutes)
- Running all 10 prompts: 15–20 minutes
- Human review and light editing: 30–40 minutes
- **Total: under 60 minutes for 10 platform-ready assets**

## Quality Criteria

- All 10 asset types are generated from the source content
- Each asset is platform-specific — not a copy-paste of the same text
- Platform adaptation rules are applied (character limits, tone, format)
- Quality gate checklist is completed before any asset is published
- Time benchmark is achieved (under 60 minutes total)
- Brand voice is consistent across all 10 assets
- Output is organised clearly by asset type for client handover
- At least one asset references a local Uganda/EA context, event, or example
```

**Step 2: Verify quality checklist, count lines**

**Step 3: Commit**

```bash
git add ai-content-recycling-pipeline/SKILL.md
git commit -m "Add ai-content-recycling-pipeline: 1 content asset → 10 platform variants via AI"
```

---

### Task 10: Create `ai-rag-brand-knowledge-base`

**Files:**
- Create: `ai-rag-brand-knowledge-base/SKILL.md`

**Step 1: Write the complete file**

Content must cover:
- What RAG is and why it matters (Sweenor and Mulkers, 2024)
- What to include in the knowledge base (brand guide, personas, past campaigns, product info, tone-of-voice examples, competitor notes)
- How to structure documents for LLM retrieval (chunking, clear headings, no ambiguity)
- Tool options: Claude Projects, ChatGPT Projects, CustomGPT, Notion AI, Mem.ai
- Query workflow for content creators
- Maintenance protocol: quarterly review
- EA calibration: local market context documents to include
- Required Input section
- Quality Criteria section (5–8 bullets)

**Step 2: Verify quality checklist, count lines**

**Step 3: Commit**

```bash
git add ai-rag-brand-knowledge-base/SKILL.md
git commit -m "Add ai-rag-brand-knowledge-base: RAG knowledge base design for brand-consistent AI output"
```

---

### Task 11: Create `ai-synthetic-personas`

**Files:**
- Create: `ai-synthetic-personas/SKILL.md`

**Step 1: Write the complete file**

Content must cover:
- When synthetic personas are appropriate vs primary research (Venkatesan and Lecinski, 2026; HBR)
- Structured prompt template with all required layers (demographics, income in UGX, platform behaviour, pain points, goals, media habits, language preferences)
- Uganda/EA calibration: default demographic bands, platform usage norms, income tiers in UGX
- 3-persona output format: Name, Archetype, Day in the Life, Content Preferences, Messaging Triggers, Platforms, Barriers
- Synthetic focus group technique: simulating audience reactions to campaign concepts
- Validation checklist: cross-reference with available secondary data
- Citation standard: always disclose synthetic origin in deliverables
- Required Input section
- Quality Criteria section (5–8 bullets)

**Step 2: Verify quality checklist, count lines**

**Step 3: Commit**

```bash
git add ai-synthetic-personas/SKILL.md
git commit -m "Add ai-synthetic-personas: AI-generated audience personas for EA markets without primary research"
```

---

### Task 12: Create `ai-strategy-co-thinker`

**Files:**
- Create: `ai-strategy-co-thinker/SKILL.md`

**Step 1: Write the complete file**

Content must cover:
- Co-Pilot vs Co-Thinker distinction (Farri and Rosani, 2025): when to use each
- Multi-step dialogue sequence for brand strategy development (5-step: context → stakeholder map → pain point table → red flags → options)
- MVOSSTE workflow with AI at each stage (Randazzo, 2024): full prompt template for each step
- Job-to-be-Done framing: prompt template for "what job is our audience hiring this content to do?"
- Campaign risk mapping: list assumptions → prioritise critical ones → design rapid tests (McGrath and MacMillan via HBR)
- Prompt footnoting as a professional practice: how to document and cite AI-generated outputs
- Quality gate: AI generates options, human consultant selects and refines
- Required Input section
- Quality Criteria section (5–8 bullets)

**Step 2: Verify quality checklist, count lines**

**Step 3: Commit**

```bash
git add ai-strategy-co-thinker/SKILL.md
git commit -m "Add ai-strategy-co-thinker: AI as strategic thought partner using MVOSSTE + HBR Co-Thinker model"
```

---

## BATCH 3: New Frontier Skills

---

### Task 13: Create `ai-agentic-marketing-workflows`

**Files:**
- Create: `ai-agentic-marketing-workflows/SKILL.md`

**Step 1: Write the complete file**

Content must cover:
- Agentic vs generative AI: agentic is proactive; generative is reactive (Nayebi, 2025)
- PRAL loop: Perceive → Reason → Act → Learn (foundational architecture)
- BDI model for marketing: Beliefs (audience data) = inputs; Desires (business goals) = objectives; Intentions (campaign tactics) = outputs
- OODA cycle: Observe → Orient → Decide → Act — applied to real-time content decisions
- Three-wave maturity roadmap with EA context
- Five agentic workflow templates:
  1. Content pipeline agent (monitors trends → drafts → human approval → publishes → measures)
  2. Sentiment monitoring agent (scans mentions → classifies → alerts → suggests response)
  3. Proactive campaign agent (detects engagement drop → triggers response → reports)
  4. Multi-agent reporting system (data agent → analysis agent → draft report → human review)
  5. Dynamic WhatsApp response agent (classifies inbound → routes to tree/LLM/human)
- HITL safeguard design: decision thresholds, escalation protocols, override mechanisms
- Tool options: Claude API, ChatGPT Assistants API, AutoGen, n8n, Zapier AI
- EA implementation realism: Wave 1–2 achievable now; Wave 3 requires investment
- Required Input section
- Quality Criteria section (5–8 bullets)

**Step 2: Verify quality checklist, count lines (may need references/ subfolder if approaching 500 lines)**

**Step 3: Commit**

```bash
git add ai-agentic-marketing-workflows/SKILL.md
git commit -m "Add ai-agentic-marketing-workflows: PRAL/BDI/OODA frameworks + 5 agentic workflow templates"
```

---

### Task 14: Create `ai-generative-search-optimisation`

**Files:**
- Create: `ai-generative-search-optimisation/SKILL.md`

**Step 1: Write the complete file**

Content must cover:
- GEO vs SEO: what changes when AI-native search (ChatGPT, Perplexity, Google AI Overviews) becomes a discovery channel (Roth and neuroflash, 2024)
- How LLMs decide what to cite: factual accuracy, clear attribution, well-structured prose, concise definitions, authoritative sources
- Content structure for LLM citation: headers, bullet summaries, FAQ sections, clear definitions, numbered lists
- Machine-readable brand content: structured data markup, explicit brand values, clear pricing, parseable product information (Venkatesan and Lecinski, 2026)
- AI-to-AI marketing: when consumers' AI agents filter brand content before humans ever see it
- GEO content audit framework: 10-point checklist for assessing existing content's LLM-readability
- Content creation guidelines for GEO: tone, structure, sourcing, accuracy standards
- Manual monitoring protocol: how to track brand mentions in AI-generated search results
- EA relevance: forward-looking but growing — position as a 2-year horizon investment
- Required Input section
- Quality Criteria section (5–8 bullets)

**Step 2: Verify quality checklist, count lines**

**Step 3: Commit**

```bash
git add ai-generative-search-optimisation/SKILL.md
git commit -m "Add ai-generative-search-optimisation: GEO framework for AI-native search optimisation"
```

---

### Task 15: Create `ai-predictive-analytics-social`

**Files:**
- Create: `ai-predictive-analytics-social/SKILL.md`

**Step 1: Write the complete file**

Content must cover:
- Five predictive use cases for social media (Johnsen, 2024; Lamplugh, 2024):
  1. Follower churn prediction — identify disengaging followers before they leave
  2. Content performance prediction — forecast which post types will drive highest engagement
  3. Audience personalisation — tailor content mix to distinct audience segments
  4. Social commerce forecasting — project revenue from social-driven campaigns
  5. Cross-sell/upsell identification — identify which followers are most likely to convert
- RFM analysis (Recency, Frequency, Monetary) applied to social audiences: how to score and segment
- CLV (Customer Lifetime Value) modelling: formula and social media application
- AutoML for segmentation: tools accessible to non-data-science teams (Obviously AI, Akkio, Pecan AI, Google AutoML)
- Predictive content calendar: use historical engagement data to build data-driven posting strategy
- Five-step data science workflow: Collect → Clean → Analyse → Implement → Monitor
- Personalisation ROI measurement: 7-step framework
- Data sources available in Uganda/EA: Meta Business Suite insights, Google Analytics 4, WhatsApp Business statistics, email platform analytics
- Required Input section
- Quality Criteria section (5–8 bullets)

**Step 2: Verify quality checklist, count lines**

**Step 3: Commit**

```bash
git add ai-predictive-analytics-social/SKILL.md
git commit -m "Add ai-predictive-analytics-social: predictive analytics for social media using RFM, CLV, AutoML"
```

---

### Task 16: Create `ai-data-foundation-audit`

**Files:**
- Create: `ai-data-foundation-audit/SKILL.md`

**Step 1: Write the complete file**

Content must cover:
- Why data quality is Step 1 before any AI investment (Venkatesan and Lecinski, 2026; Lamplugh, 2024; Ltifi, 2025 — all three books converge on this)
- EA client reality: data typically fragmented across WhatsApp chat exports, Facebook Page insights, email lists, and Excel spreadsheets
- Data hygiene checklist (20 items): duplicates, missing fields, format inconsistencies, encoding issues, stale records, unlabelled segments, etc.
- Data mapping framework: identify all customer data sources → map fields → consolidate into unified customer profile structure
- Governance framework: data owner, access controls, retention periods, Uganda Data Protection and Privacy Act (2019) compliance requirements
- 30-day remediation plan template: prioritised action list with owner and deadline columns
- Tool options accessible to EA clients: Google Sheets (starter), Airtable, HubSpot Free CRM, Notion
- Handoff section: how to connect cleaned data to AI tools — RAG knowledge base, chatbot knowledge base, segmentation tools
- Required Input section
- Quality Criteria section (5–8 bullets)

**Step 2: Verify quality checklist, count lines**

**Step 3: Commit**

```bash
git add ai-data-foundation-audit/SKILL.md
git commit -m "Add ai-data-foundation-audit: data quality audit for AI marketing readiness in EA markets"
```

---

## Final Step: Batch Review and Summary Commit

After all 16 tasks are complete:

**Step 1: Count all modified/created SKILL.md files**

```bash
git log --oneline | head -20
```

**Step 2: Verify no temp files are present**

```bash
git status
```

If any `_temp_*` files appear, delete them before the final commit.

**Step 3: Final summary commit (if any loose files remain)**

```bash
git add .
git commit -m "Complete AI skills enhancement: 7 strengthened + 9 new skills from 12-book synthesis"
```

---

## Success Criteria

- All 7 existing skills show measurable additions (new sections, frameworks, tools)
- All 9 new skills exist as complete SKILL.md files in their own folders
- Every skill cites at least 2 of the 12 source books
- No skill exceeds 500 lines
- All skills use British English, imperative language, and EA defaults
- All skills have Required Input and Quality Criteria sections
- No duplicate skills — each new skill has a distinct, non-overlapping scope
- A Ugandan marketing consultant would find every skill immediately actionable

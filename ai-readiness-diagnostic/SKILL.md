---
name: ai-readiness-diagnostic
description: >
  Conducts a 41-item diagnostic to assess a client's AI marketing maturity,
  identify their current AI Marketing Canvas step (1–5), and produce a scored
  maturity profile with a prioritised action plan. Invoke this skill when a
  client wants to understand where they stand on AI adoption, before beginning
  any AI strategy, tool selection, or training investment. Based on Venkatesan
  and Lecinski (2026) The AI Marketing Canvas, 2nd edition, Stanford Business
  Books.
---

# AI Readiness Diagnostic

## Purpose

Assess a client's current AI marketing maturity across five domains, calculate
their AI Marketing Canvas step, and produce a practical, prioritised action plan
that reflects their actual starting point. Output is structured for a
non-technical business owner to read and act on immediately.

After completing this diagnostic, refer the client to the sister skill
`ai-marketing-canvas-assessment` for full canvas completion and strategic
roadmap development.

---

## Required Inputs

Ask for the following before beginning:

- **Business name** — trading name of the client organisation
- **Industry** — sector and nature of the business
- **Country / city** — primary operating location (default: Uganda/East Africa)
- **Primary marketing goal** — what the client most wants marketing to achieve
- **Team size** — approximate number of people in the marketing function

Then walk through all 41 diagnostic questions together with the client,
recording Y (Yes) or N (No) for each item. Do not skip questions. If the client
is genuinely uncertain, default to N and note it for follow-up.

---

## The 41-Item Diagnostic

### Domain 1: Data Foundation (8 items)

1. Do you have a single, centralised customer database?
2. Is customer data cleaned and deduplicated at least quarterly?
3. Do you track customer behaviour across more than one channel?
4. Do you have explicit customer consent for data collection and use?
5. Can you segment your customers by behaviour, not just demographics?
6. Do you have a named person responsible for data quality?
7. Do you have a documented data governance policy?
8. Can you link online and offline customer data?

### Domain 2: Technology Stack (8 items)

9. Do you have a CRM system in active use?
10. Do you use a social media scheduling tool?
11. Do you use an email marketing platform?
12. Do you have website analytics in place (GA4 or similar)?
13. Do you use any AI-powered content creation tools?
14. Do you use any marketing automation (Zapier, Make, or similar)?
15. Do you use any AI analytics or reporting tools?
16. Do you have a documented tech stack with assigned owners?

### Domain 3: Team Capability (8 items)

17. Has your marketing team used ChatGPT or a similar LLM in the last 30 days?
18. Does anyone on your team understand prompt engineering basics?
19. Has your team received any AI tools training in the last 12 months?
20. Do you have a documented AI use policy for staff?
21. Is there a senior leader who champions AI adoption?
22. Does your team feel comfortable experimenting with new tools?
23. Do you regularly review how AI tools are being used?
24. Does your team know the difference between AI-generated and human-created content?

### Domain 4: AI Deployment (9 items)

25. Do you use AI for any content creation (captions, blogs, emails)?
26. Do you use AI for social media scheduling or posting?
27. Do you use AI for customer segmentation or targeting?
28. Do you use AI-powered chatbots or automated messaging?
29. Do you use AI for sentiment analysis or social listening?
30. Do you use AI for paid advertising optimisation?
31. Do you use AI for performance reporting or forecasting?
32. Do you have real-time personalisation in any marketing channel?
33. Has AI changed how you make budget or strategy decisions?

### Domain 5: Business Impact (8 items)

34. Has AI reduced time spent on content creation by at least 25%?
35. Have AI experiments produced measurable ROI?
36. Has AI improved audience targeting or engagement rates?
37. Has AI enabled you to produce more content at the same cost?
38. Has AI created new revenue streams or business models?
39. Do you have AI-specific KPIs in your marketing plan?
40. Do senior stakeholders receive regular AI performance updates?
41. Has AI changed your competitive position in your market?

---

## Scoring

### Step 1: Calculate domain scores

Count the number of YES answers in each domain:

| Domain | Items | Max Score |
|---|---|---|
| 1. Data Foundation | 1–8 | 8 |
| 2. Technology Stack | 9–16 | 8 |
| 3. Team Capability | 17–24 | 8 |
| 4. AI Deployment | 25–33 | 9 |
| 5. Business Impact | 34–41 | 8 |
| **Total** | 1–41 | **41** |

### Step 2: Identify the AI Marketing Canvas step

| Total Score | Canvas Step |
|---|---|
| 0–8 | Step 1 — Foundation |
| 9–16 | Step 2 — Experimentation |
| 17–24 | Step 3 — Expansion |
| 25–32 | Step 4 — Transformation |
| 33–41 | Step 5 — Reinvention |

### Step 3: Interpret domain scores

Apply these thresholds to identify specific gap areas:

| Domain | Score | Interpretation |
|---|---|---|
| Data Foundation | 0–3 | Critical gap — no AI programme can succeed without this |
| Technology Stack | 0–3 | Tool gaps limit what AI can do |
| Team Capability | 0–3 | Training is the priority before any tool investment |
| AI Deployment | 0–4 | Experimentation is the immediate priority |
| Business Impact | 0–3 | Either early stage or AI is not yet being measured |

---

## Output Structure

Produce the following five sections in order.

---

### Section 1: Score Summary Table

Present a clean table showing:

- Each domain name
- Domain score (e.g., 3/8)
- A one-word status: **Strong**, **Developing**, or **Critical**
- Total score and Canvas step

Example format:

| Domain | Score | Status |
|---|---|---|
| Data Foundation | 3/8 | Critical |
| Technology Stack | 5/8 | Developing |
| Team Capability | 4/8 | Developing |
| AI Deployment | 2/9 | Critical |
| Business Impact | 1/8 | Critical |
| **Total** | **15/41** | **Step 2 — Experimentation** |

---

### Section 2: Canvas Step Diagnosis

Write one paragraph in plain English explaining:

- Which step the client is at and what that means in practice
- What characterises organisations at this step
- What is typically holding them back
- What the realistic next step looks like

Be honest. If the client is at Step 1, say so directly and explain what that
means without softening the message into vagueness.

Source: Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*,
2nd edn. Stanford Business Books.

---

### Section 3: Top 3 Priority Gaps

Identify the three most urgent gaps based on domain scores and individual
question responses. Rank them most urgent first. For each gap:

- **Gap title** — name the specific weakness
- **Why it matters** — one sentence on the business consequence
- **What is missing** — the specific Y/N items that are N
- **First action** — the single most important thing to do about it

---

### Section 4: 90-Day Action Plan

Structure three 30-day blocks. Include exactly three named, specific actions
per block. Actions must be concrete (name a tool, name a process, name a
person or role).

**Days 1–30: Stabilise the Foundation**

- Action 1
- Action 2
- Action 3

**Days 31–60: Build Capability**

- Action 1
- Action 2
- Action 3

**Days 61–90: Begin Deployment**

- Action 1
- Action 2
- Action 3

Calibrate ambition to the client's step. A Step 1 client's 90-day plan is about
getting basic data and tools in place — not deploying AI-powered personalisation.

---

### Section 5: Recommended Tools

Recommend tools appropriate to the client's current Canvas step and the East
African market. Prioritise:

1. Free tiers before paid subscriptions
2. Tools accessible from Uganda without VPN or restricted payment
3. UGX pricing or USD pricing with local payment options where available

**Step 1–2 tool recommendations to consider:**

| Need | Tool | Tier |
|---|---|---|
| CRM | HubSpot CRM | Free |
| Email marketing | Mailchimp | Free up to 500 contacts |
| Social scheduling | Buffer | Free (3 channels) |
| Website analytics | Google Analytics 4 | Free |
| AI content creation | ChatGPT (GPT-4o) | Free / Plus at ~UGX 130,000/month |
| AI content creation | Gemini | Free |
| Automation | Zapier | Free (5 zaps) |
| WhatsApp automation | Africa's Talking | Pay-as-you-go, UGX-compatible |
| SMS automation | Africa's Talking | Pay-as-you-go |

**Step 3–4 tool recommendations to consider:**

| Need | Tool | Tier |
|---|---|---|
| CRM with automation | HubSpot Starter | From ~USD 20/month |
| AI writing at scale | Jasper or Copy.ai | From ~USD 39/month |
| Social listening | Brandwatch Lite or Mention | From ~USD 29/month |
| Reporting | Looker Studio | Free |
| AI analytics | Polymer or Akkio | From ~USD 20/month |
| Chatbot | Tidio or Landbot | Free tier available |

Note the WhatsApp advantage: if the client is already using WhatsApp for
customer communications, this counts toward the Technology Stack domain
and can be formalised quickly via Africa's Talking or similar APIs.

---

## East African Market Context

Most Ugandan and East African SMEs score between 4 and 12 on this diagnostic,
placing them at Step 1 or early Step 2. This is not a failure — it reflects
the market's current stage of AI adoption.

Common patterns to look for:

- **No CRM**: Customer contacts held in Excel spreadsheets or WhatsApp groups.
  Recommend HubSpot Free as the immediate priority.
- **WhatsApp already in use**: Formalise this into the tech stack. Africa's
  Talking enables automated WhatsApp and SMS flows at low cost.
- **Team capability gap**: Many teams have experimented with ChatGPT informally
  but have no policy, no training, and no structured prompting practice.
  The `training-client-team` skill provides a structured training programme.
- **Budget sensitivity**: Lead with free tiers. Demonstrate value before
  recommending any paid subscription.

---

## AI Use Case Matrix (Venkatesan and Lecinski, 2026)

Once the diagnostic score is known, map the client's AI readiness to the 2×2 Use Case Matrix:

|  | **Internal** | **External** |
|---|---|---|
| **Productivity** | Automate internal workflows: reporting, content briefs, data analysis | Scale customer-facing functions: chatbots, FAQs, WhatsApp automation |
| **Growth** | Build proprietary data and algorithmic advantages | Deliver personalised customer experiences at scale |

**Recommendation by score:** (Convert raw score to percentage: total ÷ 41 × 100)
- Score 0–25%: Start in Internal/Productivity quadrant only
- Score 26–50%: Internal/Productivity + begin External/Productivity pilot
- Score 51–75%: All four quadrants in scope; prioritise highest-ROI cell
- Score 76–100%: Full AI transformation; consider Monetisation (Canvas Step 5)

---

## AI Maturity Wave Assessment (Nayebi, 2025)

Identify which wave the client currently operates in:

- **Wave 1 — Automation:** Rules-based workflows, scheduled posts, canned responses, basic chatbots. Most EA SMEs are here.
- **Wave 2 — Predictive ML:** Customer segmentation, engagement prediction, A/B test optimisation, sentiment analysis. Achievable for EA mid-market clients.
- **Wave 3 — Agentic AI:** Autonomous agents that perceive, reason, act, and learn without human prompts. Horizon planning for EA; immediate for multinational clients.

Ask the client: "Which wave best describes your current AI marketing activity?" Use their answer to calibrate the roadmap in the final section.

---

## Quality Criteria

- All 41 items are addressed — no question is skipped or estimated without a
  reason recorded
- The total score is calculated accurately and the Canvas step is stated clearly
- Domain breakdown reveals specific gap areas and is not reduced to a single
  total score
- The 90-day plan contains specific, named actions — not generic advice such
  as "improve data quality"
- Tool recommendations match the client's step and are accessible in the East
  African market, with free tiers prioritised
- Language is honest: if the client is at Step 1, the diagnosis says so clearly
  and explains what that means in practical terms
- Output is structured so a non-technical business owner can read it without
  a consultant present and know exactly what to do next
- The score summary table is the first thing the client sees — context and
  explanation follow the data

---

## References

Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn.
Stanford Business Books.

Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*.
Pearson.

Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.

Nayebi, F. (2025) *Foundations of Agentic AI for Retail*. Gradient Divergence.

---

*For full canvas completion and strategic roadmap development, use the sister
skill `ai-marketing-canvas-assessment` after completing this diagnostic.*

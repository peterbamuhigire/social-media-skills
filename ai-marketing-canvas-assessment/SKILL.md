---
name: ai-marketing-canvas-assessment
description: >
  Generates a completed AI Marketing Canvas for a client based on Venkatesan & Lecinski's
  five-step framework (The AI Marketing Canvas, 2nd ed., Stanford Business Books, 2026).
  Diagnoses the client's current step (1–5), maps AI readiness across the four customer moments
  (acquisition, retention, growth, advocacy), and produces a concrete 12-month roadmap. Invoke
  when a client wants to understand where they stand on AI adoption in marketing and what to do
  next — particularly useful at strategy kick-off, annual planning, or following an AI audit.
---
# AI Marketing Canvas Assessment

<!-- dual-compat:start -->
## Use when
- Generates a completed AI Marketing Canvas for a client based on Venkatesan & Lecinski's five-step framework (The AI Marketing Canvas, 2nd ed., Stanford Business Books, 2026). Diagnoses the client's current step (1–5), maps AI readiness across the four customer moments (acquisition, retention, growth, advocacy), and produces a concrete 12-month roadmap. Invoke when a client wants to understand where they stand on AI adoption in marketing and what to do next — particularly useful at strategy kick-off, annual planning, or following an AI audit.
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

## Purpose

Most businesses talk about AI in marketing without knowing where they actually stand or what
"progress" looks like for their size and context. This skill produces a completed AI Marketing
Canvas — a structured diagnostic and roadmap grounded in Venkatesan and Lecinski's (2026)
five-step model — that tells a client exactly what step they are on, what they should do in each
of the four customer moments, and what their next 12 months should look like.

For the full 41-item AI readiness diagnostic, use the sister skill `ai-readiness-diagnostic`.
This skill focuses on canvas completion and roadmap output.

**Framework source:** Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd ed.
Stanford Business Books.

---

## Required Input

Before generating any output, ask for the following:

1. **Client business name** — the trading name used in all deliverables.
2. **Industry** — what sector is the client in (e.g., retail, hospitality, financial services, NGO)?
3. **Country / city** — where is the business based and where is its primary audience?
   (Default: Uganda / East Africa)
4. **Primary marketing goal** — what is the single most important marketing outcome this year?
5. **Current tools in use** — list any CRM, content tools, scheduling platforms, and analytics
   tools currently in use. If none, say so.
6. **Team size** — solo operator, 2–5, 6–20, or 20+ people in the marketing function.
7. **Monthly marketing budget range (UGX)** — approximate band: under 500k, 500k–2M, 2M–10M,
   10M+. If a different currency applies, note it.

---

## Step 1 — Run the Canvas Diagnostic

Ask the client the following nine questions. Record yes/no answers.

| # | Diagnostic Question | Step Indicator |
|---|---|---|
| 1 | Does the client have a centralised customer database (CRM or equivalent)? | Step 1 |
| 2 | Is there a named person responsible for data and analytics? | Step 1 |
| 3 | Has the client used any AI tools for content creation, scheduling, or analytics? | Step 2 |
| 4 | Have any AI experiments shown measurable results (e.g., time saved, engagement lift)? | Step 3 |
| 5 | Is AI integrated into more than two marketing functions? | Step 3 |
| 6 | Does the client have a documented AI use policy? | Step 3 |
| 7 | Is there real-time personalisation in any channel? | Step 4 |
| 8 | Does AI inform budget decisions or campaign strategy? | Step 4 |
| 9 | Are any revenue streams enabled or substantially transformed by AI? | Step 5 |

**Diagnosis logic — count total yes answers:**

| Yes count | Current Step | Label |
|---|---|---|
| 0 | Step 1 | Foundation |
| 1–2 | Step 2 | Experimentation |
| 3–5 | Step 3 | Expansion |
| 6–7 | Step 4 | Transformation |
| 8–9 | Step 5 | Reinvention |

State the diagnosed step clearly at the top of the canvas output. Be honest: most East African
SMEs will land at Step 1 or Step 2. Do not inflate the diagnosis.

---

## Step 2 — Complete the AI Marketing Canvas

The canvas has five steps (rows) and four customer moments (columns), producing 20 cells.
Populate every cell for the client's **current step** and **next step** in full. Summarise the
remaining steps in one sentence each.

### The Five Steps

**Step 1 — Foundation**
AI is not yet deployed. The focus is data infrastructure and organisational readiness.

**Step 2 — Experimentation**
Small, low-risk AI experiments begin. Content tools, basic scheduling automation, simple chatbots.

**Step 3 — Expansion**
Successful experiments are scaled. AI is integrated into three or more marketing functions.
An AI use policy is in place.

**Step 4 — Transformation**
AI is core to the marketing operating model. Personalisation at scale. AI informs strategy and
budget allocation.

**Step 5 — Reinvention**
AI enables new business models and entirely new customer value propositions.

### The Four Customer Moments (Columns)

- **Acquisition** — attracting new customers: awareness, consideration, trial.
- **Retention** — keeping customers engaged: satisfaction, loyalty, repeat purchase.
- **Growth** — increasing customer value: upsell, cross-sell, referral.
- **Advocacy** — turning customers into brand promoters: UGC, referral, word-of-mouth.

### Canvas Cell Content

For each cell at the client's current and next step, include:
- **AI capability** — what AI tool or technique is deployed here.
- **Data required** — what data the client needs to make this work.
- **Expected result** — what measurable outcome this produces.

### Reference Cell Content by Step and Moment

Use the following as the basis for populating cells, adapted to the client's context.

**Step 1 — Foundation**

| Moment | AI Capability | Data Required | Expected Result |
|---|---|---|---|
| Acquisition | None yet. Audit existing channels and content performance. | Website analytics, social reach data | Baseline understanding of what is working |
| Retention | None yet. Map the customer journey manually. | Purchase records, complaint logs | Identification of retention gaps |
| Growth | None yet. Document referral and upsell patterns. | Sales data, customer records | Understanding of natural growth triggers |
| Advocacy | None yet. Monitor brand mentions manually. | Social mentions, customer feedback | Baseline sentiment score |

**Step 2 — Experimentation**

| Moment | AI Capability | Data Required | Expected Result |
|---|---|---|---|
| Acquisition | AI caption writing (ChatGPT, Claude); AI image generation for social ads | Content calendar, audience demographics | Faster content production; 20–30% time saving |
| Retention | WhatsApp broadcast automation for follow-up messages | Customer contact list, purchase history | Improved response rate; reduced churn |
| Growth | AI-generated blog briefs and SEO content for organic discovery | Keyword data, topic clusters | Increased organic traffic over 3–6 months |
| Advocacy | Sentiment monitoring via free tools (e.g., Google Alerts, Mention free tier) | Brand name, product keywords | Early detection of negative sentiment |

**Step 3 — Expansion**

| Moment | AI Capability | Data Required | Expected Result |
|---|---|---|---|
| Acquisition | AI-assisted audience segmentation; lookalike targeting on Facebook | CRM export, pixel data | Reduced cost per acquisition |
| Retention | WhatsApp automation via Africa's Talking or similar; triggered re-engagement sequences | Customer segments, purchase recency | Measurable retention improvement; reduced churn rate |
| Growth | AI-powered cross-sell recommendations in email or WhatsApp | Purchase history, product catalogue | Increased average order value |
| Advocacy | Social listening with AI sentiment tagging; UGC identification and repurposing | Branded hashtag data, review platforms | Higher volume of curated UGC |

**Step 4 — Transformation**

| Moment | AI Capability | Data Required | Expected Result |
|---|---|---|---|
| Acquisition | Predictive lead scoring; AI-optimised ad creative testing | CRM data, ad performance data | Higher quality leads at lower CPL |
| Retention | Personalised mobile money promotions; SMS segmentation by behaviour | Transaction data, behavioural data | Improved retention rate and lifetime value |
| Growth | Dynamic pricing signals; AI-informed upsell timing | Purchase patterns, customer lifetime value scores | Measurable revenue lift from existing customers |
| Advocacy | Automated referral programme management; AI-generated personalised referral prompts | Advocate profiles, referral history | Scalable word-of-mouth growth |

**Step 5 — Reinvention**

| Moment | AI Capability | Data Required | Expected Result |
|---|---|---|---|
| Acquisition | AI-native product discovery (conversational commerce, AI search) | Full customer data graph | New acquisition channels; reduced dependency on paid media |
| Retention | Predictive churn prevention; hyper-personalised experience | Real-time behavioural data | Near-zero preventable churn |
| Growth | AI identifies and creates new revenue streams from existing customer relationships | Full data platform | New business model lines |
| Advocacy | Community AI — AI tools that advocates use to create and share content | Community platform data | Advocate-led growth at scale |

---

## Step 3 — Produce the 12-Month Roadmap

Structure the roadmap by quarter. Every action must include a named tool or channel, a named metric,
and a Q assignment.

**Standard roadmap template — adapt to client's diagnosed step and context:**

**Q1 — Diagnose and Establish**
- Confirm current step based on diagnostic results.
- Complete a data audit: identify where customer data lives, who owns it, and what is missing.
- Set up or clean the customer contact list (CRM, spreadsheet minimum standard).
- Launch 1–2 low-risk AI experiments appropriate to current step (e.g., AI caption writing in
  ChatGPT, scheduling via FeedHive or Buffer).
- Metric: baseline content output volume, time spent on content creation per week.

**Q2 — Measure and Scale One Experiment**
- Review Q1 experiment results against baseline.
- Select the single most successful experiment and scale it (increase frequency, apply to more
  channels, or expand to a second content type).
- Begin mapping the customer journey for the retention moment.
- Metric: time saving from AI tools, engagement rate change, WhatsApp open or reply rate.

**Q3 — Integrate and Expand**
- Integrate AI into one additional marketing function beyond content creation.
- For EA context: consider WhatsApp automation for retention or sentiment monitoring for advocacy.
- Draft and publish an internal AI use policy (see `playbook-ai-content-workflow` for guidance).
- Metric: functions using AI (target: 3+), policy in place (yes/no).

**Q4 — Review Canvas Progress and Set Year 2 Targets**
- Re-run the nine-question diagnostic to check step progression.
- Update the canvas: complete the next step's cells for any moment where Q1–Q3 work is confirmed.
- Set SMART objectives for Year 2 based on confirmed capabilities.
- Metric: step movement (did the client advance one step?), Year 2 AI investment recommendation
  in UGX.

---

## Step 4 — Write the Plain-Language Summary

After the canvas and roadmap, produce a section titled **"What This Means for Your Business"**.

This section must:
- State the diagnosed step in plain language ("You are at Step 2 — Experimentation").
- Explain what that means in one paragraph without jargon.
- Name the single highest-impact action the client can take in the next 30 days.
- Be honest about the gap between current state and transformation — do not promise shortcuts.
- Be written as if speaking directly to a business owner, not a marketing professional.

---

## Step 5 — Monetisation

At this stage, AI capabilities become a source of competitive advantage and new revenue:
- AI-powered products or services sold to customers (e.g. a personalisation engine licensed to partners)
- Proprietary audience data monetised through partnerships
- AI-driven efficiency gains reinvested into market expansion
- Brand reputation as an AI-first organisation attracts premium clients and talent

**Consultancy note:** Most EA clients will not reach Step 5 within a 12-month engagement. Frame it as a 3–5 year horizon goal and use it to demonstrate the long-term value of starting the Canvas journey now.

---

## East Africa Context Notes

Apply these adaptations throughout the canvas and roadmap:

- **Data scarcity** — most EA SMEs have no CRM; customer data lives in WhatsApp groups,
  spreadsheets, or paper records. Step 1 must address this before any AI deployment.
- **WhatsApp first** — WhatsApp is the primary channel for retention and advocacy in Uganda and
  across East Africa. Prioritise WhatsApp automation at Step 2–3 over email sequences.
- **Mobile Money** — MTN Mobile Money and Airtel Money are transaction platforms; personalised
  promotions tied to Mobile Money behaviour are a Step 4 opportunity.
- **Step 2 tools for EA context** — ChatGPT or Claude for captions and blog briefs; FeedHive or
  Buffer for scheduling; Canva Magic Write for short-form copy; Google Alerts for brand monitoring.
- **Step 3 tools for EA context** — Africa's Talking for WhatsApp and SMS automation; Hootsuite
  Insights or Brandwatch (if budget allows) for sentiment monitoring.
- **Most EA SMEs are at Step 1–2** — calibrate ambition accordingly. A Step 2 roadmap executed
  well is more valuable than a Step 4 roadmap that cannot be implemented.

---

## Agile Sprint Approach (Venkatesan and Lecinski, 2026)

AI marketing initiatives fail when treated as annual strategic plans. Recommend monthly sprint cycles:

1. **Sprint planning (Day 1):** Select one AI use case to test this month
2. **Pilot execution (Days 2–20):** Run the experiment with a defined audience segment
3. **Measurement (Days 21–25):** Compare AI-assisted results vs human-led baseline
4. **Review (Days 26–28):** Replicate, iterate, or abandon based on results
5. **Next sprint (Day 30):** Select next use case based on learnings

KPI for each sprint: measure lift vs human-led control. A 10% improvement justifies scaling.

---

## AI-to-AI Marketing Readiness (Venkatesan and Lecinski, 2026)

As consumers increasingly use AI agents (ChatGPT, Perplexity, Google Gemini) to research, compare, and purchase, brands must be readable by machines as well as humans. Assess:

- Are product pages structured with clear, machine-parseable pricing and features?
- Are brand values explicitly stated in factual, accessible language?
- Is content well-sourced and factually accurate (LLMs avoid citing inaccurate sources)?
- Does the website use structured data markup (Schema.org)?

This is a 2–5 year horizon for most EA markets but should inform content architecture decisions now. Brands that are not AI-readable risk becoming invisible as AI-native search and AI shopping agents become mainstream.

---

## Quality Criteria

Output meets standard when it:

- Diagnoses the client's step based on evidence from the nine questions, not aspiration or
  optimism — step inflation is a failure mode.
- Addresses all four customer moments for both the current step and the next step in full, with
  named AI capabilities, required data, and expected results.
- Produces a roadmap that is concrete: every action names a tool, a channel, and a metric.
- Reflects East African context throughout — WhatsApp, Mobile Money, and data scarcity are noted
  where they affect the recommended approach.
- Assigns every roadmap action to a specific quarter (Q1, Q2, Q3, or Q4).
- Includes a plain-language "What This Means for Your Business" summary written for a business
  owner, not a marketing specialist.
- Is honest about step progression — a realistic Step 1–2 plan is better than an inflated Step 4
  plan the client cannot execute.
- Cites Venkatesan and Lecinski (2026) on first use of the framework.

---

## References

- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd ed. Stanford Business Books.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.

**Related skills:**
- `ai-readiness-diagnostic` — the full 41-item AI readiness diagnostic; run this before or
  alongside the canvas assessment for a more detailed organisational audit.
- `playbook-ai-content-workflow` — execution playbook for AI-assisted content production.
- `playbook-ai-automation-workflow` — automation and tool integration guidance.
- `05-social-media-strategy` — full social media strategy; the canvas roadmap feeds into this.

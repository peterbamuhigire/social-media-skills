---
name: ai-use-case-mapping
description: >
  Maps a client's marketing activities against the 2×2 AI Use Case Framework
  (Venkatesan & Lecinski, 2026) — Productivity/Growth × Internal/External —
  to identify the highest-priority AI opportunities across all four quadrants
  and produce a prioritised implementation shortlist with a 90-day action
  sequence. Invoke when a client wants to know where AI can add the most value
  to their marketing operations, or as the diagnostic step before building an
  AI-assisted workflow (see also: playbook-ai-automation-workflow).
---
# AI Use Case Mapping

<!-- dual-compat:start -->
## Use when
- Maps a client's marketing activities against the 2×2 AI Use Case Framework (Venkatesan & Lecinski, 2026) — Productivity/Growth × Internal/External — to identify the highest-priority AI opportunities across all four quadrants and produce a prioritised implementation shortlist with a 90-day action sequence. Invoke when a client wants to know where AI can add the most value to their marketing operations, or as the diagnostic step before building an AI-assisted workflow (see also: playbook-ai-automation-workflow).
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

Produce a structured, evidence-based map of AI opportunities for a client's
marketing activities using the 2×2 AI Use Case Framework. The output moves the
client from a vague awareness that "AI could help" to a concrete, prioritised
shortlist of use cases they can begin implementing within 90 days.

Source framework: Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing
Canvas* (2nd ed.). Stanford Business Books.

---

## Required Input

Before generating any deliverable, ask the client for:

1. **Business name** — exact trading name of the organisation
2. **Industry** — sector and sub-sector (e.g. retail FMCG, professional
   services, NGO, hospitality)
3. **Country / city** — location and primary market (defaults to Uganda/Kampala)
4. **Primary marketing goal** — the single most important objective for the
   next 6 months (e.g. grow WhatsApp enquiries, improve content consistency,
   reduce reporting time)
5. **Current marketing activities** — list every recurring marketing task the
   team performs. If the client cannot provide a list, apply the standard
   12-activity starter list in Step 1.
6. **Current AI tools in use** — list any AI tools already in use, even
   informally (e.g. ChatGPT for captions, Canva Magic Write). If none, record
   as zero.
7. **Team size and technical comfort level** — number of people managing
   marketing; rate their comfort with new software as Low / Medium / High.

---

## The 2×2 AI Use Case Framework

Source: Venkatesan and Lecinski (2026).

The framework classifies every AI use case on two axes:

- **Vertical axis — Value type:**
  - **Productivity** — efficiency, cost reduction, speed, volume handling
  - **Growth** — revenue, engagement, new capability, competitive advantage
- **Horizontal axis — Audience:**
  - **Internal** — staff, operations, workflows, team processes
  - **External** — customers, prospects, public-facing communications

This produces four quadrants:

| | **Internal** | **External** |
|---|---|---|
| **Productivity** | Q1 — Internal Productivity | Q2 — External Productivity |
| **Growth** | Q3 — Internal Growth | Q4 — External Growth |

### Quadrant 1 — Internal Productivity

AI used to make internal marketing operations faster and cheaper.

Examples:
- AI-generated first drafts (briefs, captions, email copy)
- Automated reporting and dashboard summaries
- AI-powered content repurposing (one post → multiple formats)
- Meeting notes and action-item extraction
- Competitor monitoring alerts
- Prompt libraries for team-wide use

### Quadrant 2 — External Productivity

AI used to make customer interactions more efficient at scale.

Examples:
- AI chatbots for FAQs (Messenger, WhatsApp)
- Automated response templates for comments and DMs
- Personalised email sequences triggered by behaviour
- WhatsApp broadcast automation with audience segmentation
- SMS reminders and follow-ups via Africa's Talking

### Quadrant 3 — Internal Growth

AI used to grow capability, insight, or competitive advantage internally.

Examples:
- AI-powered audience segmentation from CRM data
- Sentiment analysis to inform content strategy
- Predictive analytics for campaign planning
- AI-assisted A/B test design
- Competitive intelligence aggregation

### Quadrant 4 — External Growth

AI used to drive revenue and engagement directly with customers.

Examples:
- Personalised content recommendations
- Dynamic ad creative testing
- AI influencer matching and brief generation
- Real-time personalisation on landing pages
- Loyalty programme personalisation

---

## Step 1 — Establish the Activity List

If the client provides a full activity list, use it. If not, apply the standard
12-activity starter list:

1. Content creation (captions, blogs, emails)
2. Content scheduling and publishing
3. Community management and response
4. Customer service (comments, DMs, complaints)
5. Campaign planning and briefing
6. Audience research and persona development
7. Competitor monitoring
8. Performance reporting
9. Paid advertising management
10. Influencer identification and briefing
11. Email marketing
12. WhatsApp / SMS communications

Add any client-specific activities not covered by the list. Remove any
activities the client does not perform.

---

## Step 2 — Map Each Activity to a Quadrant

For each activity, assign it to the quadrant that best describes its primary AI
opportunity. Note that a single activity may have opportunities in more than one
quadrant — if so, create a separate row per quadrant opportunity.

Quadrant assignment rules:
- Ask: does this AI application help internal operations, or does it face the
  customer directly?
- Ask: does it save time/cost (Productivity), or does it generate new revenue
  or capability (Growth)?
- When an activity spans two quadrants, assign it to the quadrant where the
  highest-value AI opportunity sits.

---

## Step 3 — Score Each Activity

Rate each activity on two dimensions:

**Current AI Use (0–2):**
- 0 = No AI in use for this activity
- 1 = Partial AI use (e.g. occasional ChatGPT, one automated step)
- 2 = Full AI integration (systematic, consistent AI throughout this activity)

**Opportunity Score (1–5):**
Assess based on these four factors — sum them, then divide by four and round:
- **Volume** — how many times per week/month does this task occur? (1 = rare,
  5 = daily or multiple times daily)
- **Repetition** — how standardised is the task? (1 = highly variable,
  5 = near-identical every time)
- **Data availability** — does the client have data to feed an AI tool?
  (1 = no data, 5 = rich, structured data available)
- **Time cost** — how many hours per week does this task consume?
  (1 = under 30 minutes, 5 = over 5 hours)

**Priority:**
- **High** — Opportunity Score 4–5 AND Current AI Use 0
- **Medium** — Opportunity Score 3–4 OR Current AI Use 1
- **Low** — Opportunity Score 1–2 OR Current AI Use 2

---

## Step 4 — Build the Priority Matrix

Output the completed matrix in this format:

| Activity | Quadrant | Current AI Use | Opportunity Score | Priority |
|---|---|---|---|---|
| [activity name] | [Q1 / Q2 / Q3 / Q4] | [0 / 1 / 2] | [1–5] | [High / Med / Low] |

Ensure all four quadrants are represented. If the client's activity list
produces an empty quadrant, add at least one standard example activity from
that quadrant and mark it as a suggested addition.

---

## Step 5 — Quadrant Summary

After the matrix, produce a one-paragraph summary per quadrant:

- State how many activities fall in each quadrant.
- Identify which quadrant has the most High-priority opportunities.
- Note any quadrant that is notably underdeveloped (few or no High-priority
  items) — this may indicate a strategic blind spot.
- Recommend which quadrant to address first, with a one-line rationale.

---

## Step 6 — Top 5 Priority Use Cases

Select the five activities rated High priority. Present each in this format:

**Use Case [N]: [Activity Name] — [Quadrant]**

- **Why now:** [One sentence on the business case — what is being lost by not
  doing this today]
- **What to do:** [Specific AI application — name the action, not just the
  category]
- **Recommended tool:** [Named tool available and accessible in East Africa —
  include free/paid tier and approximate cost in UGX or USD]
- **Expected result:** [Measurable outcome achievable within 4 weeks — state
  the metric]
- **Effort to implement:** Low / Medium / High

Quick wins must be achievable within 4 weeks using free or low-cost tools
(under UGX 100,000/month). Flag any use case that requires a paid tool above
this threshold clearly.

---

## Step 7 — 3 Use Cases to Defer

Identify three activities that score High on Opportunity but are not suitable
for immediate implementation. For each, provide:

- **Activity:** [Name]
- **Reason for deferral:** [One of: technical complexity, data not yet available,
  team skill gap, tool cost not yet justified, requires a prior workflow to be
  in place first]
- **When to revisit:** [Milestone or timeframe — e.g. "After 90-day quick wins
  are embedded" or "When CRM data reaches 1,000+ contacts"]

---

## Step 8 — 90-Day Implementation Sequence

Sequence the Top 5 priority use cases into a realistic 90-day plan. Use the
following structure:

**Days 1–30 — Foundation (Quick Wins)**
- Implement use cases that require no new tools or only free-tier tools.
- Focus on Q1 (Internal Productivity) first — these build team confidence
  and reduce daily friction without customer-facing risk.

**Days 31–60 — External Activation**
- Implement Q2 (External Productivity) use cases — chatbots, auto-responses,
  WhatsApp automation.
- Require that Q1 foundations are in place before customer-facing AI is activated.

**Days 61–90 — Growth Layer**
- Begin Q3 and Q4 use cases that require data, testing, or higher tool investment.
- Review Days 1–60 performance before committing budget to Growth-quadrant tools.

State clearly which team member owns each action and what the success metric is
for each 30-day phase.

---

## EA-Specific Opportunities

Apply these as default suggestions for East African clients unless the client's
context makes them irrelevant:

- **WhatsApp broadcast automation (Q2 — High priority for most EA clients):**
  Most EA businesses manage broadcasts manually. Automation via ManyChat or
  Africa's Talking saves 3–5 hours per week and improves segmentation.
- **AI caption writing (Q1 — virtually universal gap):** Nearly every client
  writes captions manually. A structured prompt library (see:
  `prompt-engineering-library`) with a Brand Context Block reduces caption
  production time by 60–80%.
- **Automated comment responses in Luganda / Swahili (Q2 — emerging opportunity):**
  AI-assisted response templates in local languages improve response rates and
  audience trust. Flag the need for human review of all AI-generated local-
  language responses before publishing.
- **Mobile Money payment confirmation messages (Q2):** Automated SMS or
  WhatsApp confirmations via Africa's Talking reduce customer service volume
  and increase trust at point of payment.
- **AI-generated market research summaries (Q3):** Where local quantitative
  data is scarce, AI can synthesise qualitative signals — social listening,
  review aggregation, WhatsApp conversation patterns — into usable audience
  insight. Flag data scarcity explicitly; do not present AI-synthesised insight
  as equivalent to primary research.

---

## Quality Criteria

Output from this skill meets the standard when:

1. **All four quadrants are populated** — no quadrant is left empty; if the
   client's activity list does not cover a quadrant, at least one suggested
   activity is added and marked as such.
2. **Priority ranking is evidence-based** — every High, Medium, and Low rating
   is derived from the Opportunity Score formula, not intuition or assumption.
3. **Quick wins are genuinely quick** — all Top 5 use cases are achievable
   within 4 weeks and use free or sub-UGX 100,000/month tools; any exception
   is flagged and justified.
4. **EA context is reflected throughout** — WhatsApp features as the primary
   customer channel; Africa's Talking is cited for SMS/WhatsApp API use;
   Mobile Money is acknowledged as a payment and communications touchpoint;
   data scarcity in local markets is not ignored.
5. **Deferred items include a clear reason and a revisit trigger** — no use
   case is dismissed without explanation; deferral is always time-bound or
   milestone-bound.
6. **Tool recommendations are named and EA-accessible** — every tool cited
   has a free tier or is payable via Visa, Mastercard, or MTN Mobile Money
   via Payoneer; no tool is recommended without a cost indication.
7. **Output is actionable by a non-technical marketing manager** — no
   assumption of developer skills, API access, or data science knowledge
   unless the client's team profile explicitly supports it.
8. **The 90-day sequence is owned and measurable** — every phase names a
   responsible person and a success metric; the plan is a working document,
   not a wish list.

---

## Cross-References

- **`ai-marketing-canvas-assessment`** — use for full AI marketing maturity
  assessment and strategic canvas before or after this use case mapping exercise.
- **`prompt-engineering-library`** — use for ready-made, client-specific prompts
  to activate Q1 (Internal Productivity) quick wins immediately.
- **`playbook-ai-automation-workflow`** — use for detailed workflow automation
  planning once Q2 (External Productivity) use cases are approved.
- **`playbook-ai-content-workflow`** — use for content production automation
  planning, particularly for Q1 caption and blog use cases.

---

## References

- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas* (2nd ed.).
  Stanford Business Books. [2×2 AI Use Case Framework — cited in Steps 2–8]
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*.
  Pearson. [RACE framework; channel strategy context]
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.
  [ROI formula: (TLV − COCA) ÷ COCA — apply when calculating expected return
  on AI tool investment]

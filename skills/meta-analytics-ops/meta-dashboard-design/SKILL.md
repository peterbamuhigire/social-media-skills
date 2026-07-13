---
name: meta-dashboard-design
description: "Use when specifying a decision-led marketing dashboard, metric hierarchy and mobile reporting layout. Produces dashboard specification and metric-to-decision map; use `meta-reporting` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Marketing Dashboard Design Standards

**Source:** Raaz (c.2023) *Web Analytics Blueprint*

---


<!-- dual-compat-start -->
## Use When

- Use this skill for specifying a decision-led marketing dashboard, metric hierarchy and mobile reporting layout.
- Confirm that `meta-reporting` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-reporting` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Metric definitions, data sources, refresh cadence and user decisions | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Dashboard specification and metric-to-decision map | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified dashboard specification and metric-to-decision map. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Metric definitions, data sources, refresh cadence and user decisions is current and attributable | Produce the full dashboard specification and metric-to-decision map and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-reporting` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-reporting` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the dashboard specification and metric-to-decision map, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the dashboard specification and metric-to-decision map without metric definitions. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-reporting` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified metric definitions, the skill produces a dashboard specification and metric-to-decision map with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-reporting`](../meta-reporting/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Inputs

Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry**
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. demonstrate monthly ROI, track lead volume, monitor brand awareness)
5. **Reporting tool in use** (Google Looker Studio, Google Sheets, Meta Business Suite, or other)
6. **Audience for the dashboard** (business owner only; marketing manager; full management team)
7. **Reporting cadence** (weekly, monthly, quarterly)
8. **Platforms and data sources connected** (GA4, Search Console, Meta Ads, Google Ads, Sheets, etc.)

---

## The Design Principle

A dashboard is not a data dump. It is a decision-making tool. Every element on a client dashboard must answer one of three questions:

1. **What is happening?** (current performance)
2. **Why is it happening?** (context and diagnosis)
3. **What should we do next?** (recommendation)

Remove any chart, metric, or table that does not answer one of these three questions.

---

## Data Storytelling Structure

Every report section must follow the **Insight → Context → Recommendation** sequence:

- **Insight:** The single most important thing this data tells us.
  *Example: "Engagement rate dropped 22% in Week 3."*
- **Context:** Why this happened or what it means.
  *Example: "This coincides with the public holiday — reduced posting frequency and lower audience online time."*
- **Recommendation:** The specific action to take.
  *Example: "Maintain 3 posts/week during public holidays; schedule for Thursday–Friday rather than Monday–Tuesday."*

Apply this structure to every section of the dashboard narrative — not just the summary.

---

## Chart Type Selection Guide

| Data type | Correct chart type | Never use |
|---|---|---|
| Trends over time | Line chart | Pie chart |
| Comparisons between channels or campaigns | Horizontal bar chart (many items) or vertical bar (fewer than 6) | 3D charts of any kind |
| Proportions of a whole | Donut chart (maximum 5 segments) | Pie chart with more than 5 segments |
| User behaviour on a page | Heatmap | Table |
| Funnel performance | Funnel chart | Bar chart |
| Geographic distribution | Map | Table |
| Single key metric vs. target | Scorecard with RAG (Red/Amber/Green) status | Gauge chart |

**Default rule:** When in doubt, use a line chart for time-series data and a horizontal bar chart for comparisons. These are the two most universally readable chart types across all audience literacy levels.

---

## Mobile-First Design (Critical for EA)

In Uganda and East Africa, the majority of clients access dashboards on smartphones — not desktop computers. Design every dashboard for mobile first.

**Mobile design rules:**

- **Single-column layout** — no side-by-side charts; they become unreadably small on mobile screens
- **Font sizes:** body text minimum 14px; metric values minimum 18px; headings minimum 22px
- **Maximum 6 charts per dashboard view** — more than 6 causes scroll fatigue and reduces the likelihood the client reads the full report
- **Contrasting colours** — ensure chart colours are distinguishable on lower-quality Android screens in bright outdoor light (avoid light grey on white)
- **Test before delivering** — open the dashboard on an Android mid-range smartphone before sending to the client; do not test on an iPhone or desktop only

---

## Recommended Tool for EA Clients

**Google Looker Studio** (free, Google-integrated, mobile-accessible).

Connect directly to: GA4, Google Search Console, Google Ads, and Google Sheets. Sufficient for 90% of EA client reporting needs without paid tool costs. Shareable via a link — no software installation required for the client.

**Alternative for non-Google environments:** A structured Google Sheets dashboard with conditional formatting for RAG status. Less visual but universally accessible and free.

Avoid recommending paid dashboard tools (Tableau, Power BI, Databox) unless the client has an existing enterprise IT budget and a dedicated analyst.

---

## Dashboard Structure

Build every client dashboard in this order:

**1. Summary Scorecard (top section)**
Display 4–6 key metrics for this period vs. the previous period. Apply traffic-light (RAG) status to each:
- Green: at or above target
- Amber: within 10% below target
- Red: more than 10% below target

Include: metric name, current value, previous period value, percentage change, RAG status.

**2. Trend Charts (middle section)**
Two or three line charts showing weekly performance over the past 12 weeks. Suggested metrics: total reach or sessions; engagement rate or goal completion rate; lead volume or revenue.

**3. Channel Breakdown (middle section)**
One horizontal bar chart comparing performance by traffic source or platform. This answers: "Which channel is working hardest this month?"

**4. Key Insight and Recommendation (bottom section)**
Two sentences written in plain language:
- Sentence 1: What the data shows this month in summary.
- Sentence 2: The single most important action to take next month.

This section is the most important — it is the section the client is most likely to read. Write it last, after reviewing all the data.

---

## What to Exclude

Remove the following from all client dashboards unless specifically requested:

- Raw impression counts without engagement context
- Follower count without growth rate context
- Data the client has never asked about or acted on
- Metrics that cannot be influenced by the actions available to the client
- Technical metrics (bounce rate, pages/session) without plain-language explanation

**The less-is-more principle:** A dashboard with 6 clear metrics the client understands and acts on is worth more than a dashboard with 40 metrics the client ignores.

---

## Vanity Metric Flag

Flag any of the following if they appear as primary metrics in a client dashboard — they are vanity metrics that can mislead without context:

- Total impressions (without reach or frequency)
- Total followers (without engagement rate)
- Total post count (without performance per post)
- Total clicks (without conversion rate)
- Total video views (without watch time or completion rate)

Vanity metrics are acceptable as secondary data in a supporting table. They must never appear as headline scorecard metrics.

---

## Quality Criteria

Output meets the standard for this skill if:

- Every dashboard section follows the Insight → Context → Recommendation structure
- Chart types match the data storytelling purpose — no pie charts for trend data, no tables for geographic data
- The dashboard passes a mobile-first test: single-column layout, minimum font sizes observed, maximum 6 charts
- The summary scorecard uses RAG (Red/Amber/Green) status for each metric against a defined target
- Google Looker Studio is recommended as the default tool for EA clients, with rationale
- Vanity metrics are either excluded or demoted to secondary data with plain-language context
- The Key Insight and Recommendation section is written in plain language — no jargon, no analytics terminology without explanation
- Language is British English throughout; imperative in all instructional sections

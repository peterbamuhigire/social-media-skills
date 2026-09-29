# Dashboard Specification

Merged from skills/meta-analytics-ops/meta-dashboard-design on 2026-09-29 at 8eacccb; preservation map: [meta-dashboard-design.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-dashboard-design.md)

## When to use this reference

Read this reference when the client wants a standing marketing dashboard rather than, or alongside, the written monthly report: a dashboard specification, a metric hierarchy, a metric-to-decision map or a mobile reporting layout. The written report in the SKILL.md stays the narrative deliverable; the dashboard is the screen the client checks between reports. Method source: Raaz (c.2023) *Web Analytics Blueprint*.

A dashboard is not a data dump. It is a decision-making tool. Every element must answer one of three questions:

1. **What is happening?** (current performance)
2. **Why is it happening?** (context and diagnosis)
3. **What should we do next?** (recommendation)

Remove any chart, metric or table that does not answer one of these three questions.

## Inputs

Ask for the following before specifying the dashboard:

| Input | What to capture |
|---|---|
| Client business name | Trading name |
| Industry | Sector |
| Country / city | Defaults to Uganda / East Africa |
| Primary goal | For example: demonstrate monthly ROI, track lead volume, monitor brand awareness |
| Reporting tool in use | Google Looker Studio, Google Sheets, Meta Business Suite, or other |
| Audience for the dashboard | Business owner only; marketing manager; full management team |
| Reporting cadence | Weekly, monthly or quarterly |
| Platforms and data sources connected | GA4, Search Console, Meta Ads, Google Ads, Sheets, etc. |

Also confirm metric definitions, data sources, refresh cadence and the decisions each user makes from the dashboard. If metric definitions are missing, stop the affected part of the specification or issue a clearly bounded partial output.

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| A chart, metric or table answers none of the three questions | Remove it. | Data dump nobody acts on. |
| Data is a trend over time | Line chart; never a pie chart. | Unreadable trend. |
| Comparing channels or campaigns | Horizontal bar chart (many items) or vertical bar (fewer than 6); never 3D charts of any kind. | Distorted comparison. |
| Showing proportions of a whole | Donut chart, maximum 5 segments; never a pie chart with more than 5 segments. | Unreadable slices. |
| Showing user behaviour on a page | Heatmap, not a table. | Hidden behaviour pattern. |
| Showing funnel performance | Funnel chart, not a bar chart. | Lost stage-to-stage drop-off. |
| Showing geographic distribution | Map, not a table. | Hidden location pattern. |
| Showing a single key metric against target | Scorecard with RAG (Red/Amber/Green) status; not a gauge chart. | Decorative gauge with no clear status. |
| In doubt about chart type | Line chart for time series; horizontal bar chart for comparisons (the two most readable across all audience literacy levels). | Chart chosen by preference. |
| Client is in a Google environment (East Africa default) | Recommend Google Looker Studio. | Paid tool cost the client cannot sustain. |
| Client is in a non-Google environment | Structured Google Sheets dashboard with conditional formatting for RAG status. | No accessible free option. |
| Paid tool (Tableau, Power BI, Databox) proposed | Recommend only if the client has an existing enterprise IT budget and a dedicated analyst. | Tool cost with no one to run it. |
| A vanity metric appears as a headline scorecard metric | Flag it and demote it to secondary data in a supporting table, with context. | Misleading headline figure. |

## Procedure

### 1. Apply the data storytelling structure

Every report section and every section of the dashboard narrative (not just the summary) follows **Insight → Context → Recommendation**:

- **Insight:** the single most important thing this data tells us. *Example: "Engagement rate dropped 22% in Week 3."*
- **Context:** why this happened or what it means. *Example: "This coincides with the public holiday: reduced posting frequency and lower audience online time."*
- **Recommendation:** the specific action to take. *Example: "Maintain 3 posts/week during public holidays; schedule for Thursday–Friday rather than Monday–Tuesday."*

### 2. Design mobile-first (critical for East Africa)

In Uganda and East Africa, the majority of clients access dashboards on smartphones, not desktop computers. Design every dashboard for mobile first:

- **Single-column layout:** no side-by-side charts; they become unreadably small on mobile screens.
- **Font sizes:** body text minimum 14px; metric values minimum 18px; headings minimum 22px.
- **Maximum 6 charts per dashboard view:** more than 6 causes scroll fatigue and reduces the likelihood that the client reads the full report.
- **Contrasting colours:** chart colours must be distinguishable on lower-quality Android screens in bright outdoor light (avoid light grey on white).
- **Test before delivering:** open the dashboard on a mid-range Android smartphone before sending it to the client; do not test on an iPhone or desktop only.

For typeface and colour choices beyond these minimums, hand over to the design engine (https://github.com/peterbamuhigire/design-system-skills).

### 3. Choose the tool

**Google Looker Studio** is the default for East Africa clients: free, Google-integrated and mobile-accessible. It connects directly to GA4, Google Search Console, Google Ads and Google Sheets, is sufficient for about 90% of EA client reporting needs without paid tool costs, and is shared by link with no software installation for the client. State this rationale in the specification.

Alternative for non-Google environments: a structured Google Sheets dashboard with conditional formatting for RAG status; less visual but universally accessible and free. Tool features and pricing change: verify before stating (no register record).

### 4. Build the dashboard in this order

1. **Summary scorecard (top section).** 4–6 key metrics for this period against the previous period, each with RAG status:
   - Green: at or above target
   - Amber: within 10% below target
   - Red: more than 10% below target

   Show metric name, current value, previous period value, percentage change and RAG status. Note: the written monthly report in the SKILL.md uses a 15% amber band; state which threshold applies in each deliverable and keep the dashboard and report consistent for the same client.
2. **Trend charts (middle section).** Two or three line charts showing weekly performance over the past 12 weeks. Suggested metrics: total reach or sessions; engagement rate or goal completion rate; lead volume or revenue.
3. **Channel breakdown (middle section).** One horizontal bar chart comparing performance by traffic source or platform. It answers: "Which channel is working hardest this month?"
4. **Key insight and recommendation (bottom section).** Two sentences in plain language: sentence 1, what the data shows this month in summary; sentence 2, the single most important action to take next month. This is the section the client is most likely to read. Write it last, after reviewing all the data.

For the hero-tile pattern (one metric that matters with its line in the sand and trend, three to five guard-rails, everything else as drill-down), read [OMTM hero tile and guard-rails](../../meta-social-metrics-framework/references/omtm-lines-in-the-sand-and-stage-metrics.md).

### 5. Exclude and flag

Remove from all client dashboards unless specifically requested:

- Raw impression counts without engagement context
- Follower count without growth-rate context
- Data the client has never asked about or acted on
- Metrics that cannot be influenced by the actions available to the client
- Technical metrics (bounce rate, pages/session) without plain-language explanation

**Less is more:** a dashboard with 6 clear metrics the client understands and acts on is worth more than one with 40 metrics the client ignores.

**Vanity metric flag.** Flag these if they appear as primary metrics; they mislead without context:

| Vanity metric | Context it needs |
|---|---|
| Total impressions | Reach or frequency |
| Total followers | Engagement rate |
| Total post count | Performance per post |
| Total clicks | Conversion rate |
| Total video views | Watch time or completion rate |

Vanity metrics are acceptable as secondary data in a supporting table. They must never appear as headline scorecard metrics.

## Output template

**Dashboard specification and metric-to-decision map**

| Section | Metric / chart | Chart type | Data source | Refresh | Target and RAG rule | Decision it informs | Owner |
|---|---|---|---|---|---|---|---|
| Summary scorecard | | Scorecard + RAG | | | Green ≥ target; Amber ≤10% below; Red >10% below | | |
| Trend | | Line (12 weeks, weekly) | | | | | |
| Channel breakdown | | Horizontal bar | | | | | |
| Key insight and recommendation | Two plain-language sentences | Text | | | n/a | | |

Add a decision and source register: each material claim records its source and date or is labelled unverified; unassessed checks are marked `not assessed`, never passed.

## Checklist

- [ ] Every dashboard section follows Insight → Context → Recommendation.
- [ ] Chart types match the storytelling purpose: no pie charts for trend data, no tables for geographic data.
- [ ] Mobile-first test passed: single-column layout, minimum font sizes observed, maximum 6 charts.
- [ ] Summary scorecard uses RAG status for each metric against a defined target.
- [ ] Google Looker Studio recommended as the default for EA clients, with rationale.
- [ ] Vanity metrics excluded or demoted to secondary data with plain-language context.
- [ ] Key insight and recommendation written in plain language: no jargon, no analytics terminology without explanation.
- [ ] British English throughout; imperative in all instructional sections.
- [ ] No publishing, spend or live-account edits without separate explicit authority.

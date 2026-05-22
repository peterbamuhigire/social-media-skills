---
name: meta-reporting
description: Generates a complete written monthly social media performance report — the document version sent to clients by email between formal presentations. Covers platform KPIs, top content, what worked, what did not, testing plans, paid performance, and next-month recommendations. Invoke this skill at the end of each calendar month to produce the written report. Use the deck-monthly-report skill for the presentation version of the same data; both cover the same month, but this document goes by email and the deck is for meetings.
---
# Monthly Social Media Performance Report (Written Document)

> **Note:** This is the written document version of the monthly report. Use `deck-monthly-report` for the presentation version. Both cover the same month's data. This document is sent by email; the deck is used in client meetings. Do not duplicate — produce one of each per month, not both from this skill.

---

<!-- dual-compat:start -->
## Use when
- Generates a complete written monthly social media performance report — the document version sent to clients by email between formal presentations. Covers platform KPIs, top content, what worked, what did not, testing plans, paid performance, and next-month recommendations. Invoke this skill at the end of each calendar month to produce the written report. Use the deck-monthly-report skill for the presentation version of the same data; both cover the same month, but this document goes by email and the deck is for meetings.
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
- A structured audit, report, model, or analytical framework in markdown, with decisions and recommendations tied to evidence.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Before generating the report, collect the following from the consultant:

- **Client name** and trading name (if different)
- **Industry** and sector
- **Country / city** (default: Uganda / Kampala)
- **Primary goal** (from the strategy document)
- **Report period** (e.g., March 2026 — specify the full month)
- **Consultant name** (for the report header)
- **Platform metrics for the month** — for every active platform, provide:
  - This month's figures for all tracked KPIs (see Section 2 for the full metric list per platform)
  - Last month's figures for comparison
  - Agreed targets (from the strategy document or agreed with the client)
- **Paid ad data** (if applicable): spend, reach, cost per result, best-performing ad description
- **Notable events or issues this month:** Anything that influenced performance — a product launch, a public holiday, a crisis, a viral post, a platform outage, a boost campaign
- **Top posts:** Links or descriptions of the 3 highest-performing posts this month across all platforms

---

## Reporting Principles

**Data storytelling structure:** Every section of any report must follow the sequence Insight → Context → Recommendation. Presenting raw metric tables without interpretation is not acceptable. State what the data shows, explain what caused it, then recommend what to do next. This applies at section level and at individual metric level.

**Chart type selection (Raaz, c.2023):** Select chart types by data relationship — not by preference. Trends → line chart; comparisons → bar chart; proportions → donut chart; user behaviour patterns → heatmap; conversion stages → funnel chart. Never use 3D charts — they distort proportions and reduce legibility.

**Real-time monitoring tier:** For clients running active campaigns, add a live dashboard layer providing same-day visibility of: ad spend pacing, campaign reach, and conversion events. Metrics warranting real-time monitoring: ad spend vs. daily budget (real-time), campaign reach and frequency (same day), conversion events (same day). Metrics suitable for weekly reporting: engagement rates, follower growth, content performance. Metrics suitable for monthly reporting: ROI, COCA, CLV by cohort.

**Mobile-responsive design standard:** All client dashboards must be readable on a mid-range Android smartphone without zooming or horizontal scrolling. Recommend Google Looker Studio for EA clients — free, Google-integrated, and mobile-accessible. Apply: single-column layout; minimum 14px body text; maximum 6 charts per dashboard view.

**Funnel CVR benchmarks (Kahan, 2022):** Use these as standing reference benchmarks in monthly reports to assess client performance against industry norms.

| Funnel Stage | Benchmark CVR |
|---|---|
| Visitor-to-lead | >5% |
| Inquiry-to-lead | ~3% |
| Lead-to-opportunity | ~25% |
| Opportunity-to-deal | ~40% |

**Revenue sourced by channel (first-touch):** Include in quarterly reports a table showing what percentage of revenue each channel sourced on a first-touch attribution basis. Columns: Channel | Inquiries sourced | % of total inquiries | Revenue attributed | % of total revenue. This prevents sales from absorbing credit for marketing-generated opportunities and provides the evidence base for budget allocation decisions (Kahan, 2022).

**Monthly data quality audit:** Build a monthly data integrity check into the reporting workflow before producing any report. Verify: spam filter exclusions applied in GA4; bot traffic exclusions active; tracking tag firing confirmed via GA4 DebugView; UTM coverage rate (percentage of links using UTM parameters). A report built on corrupted data is worse than no report (Raaz, c.2023).

**Lead score distribution chart:** For clients using lead scoring, include a lead quality distribution chart in monthly reports — showing the percentage of leads at high, medium, and low score bands. This is a leading indicator of campaign quality, not just campaign volume. Declining scores in the high band indicate targeting drift before it appears in revenue figures (Kahan, 2022).

---

## Output: Complete Monthly Report

Generate a complete, client-ready document using the structure below. Write in British English. Use a professional but accessible tone — this document is read by business owners, not digital marketing specialists.

---

### Report Header

**[CLIENT NAME] — Social Media Performance Report**
**Report period:** [Month Year]
**Prepared by:** [Consultant name]
**Date submitted:** [Date]
**Prepared for:** [Client contact name and title, if known]

---

### 1. Period Summary

Write three paragraphs. Each paragraph serves a specific function:

**Paragraph 1 — What happened this month**
Summarise the overall performance direction: up / stable / down. Name the platforms that drove the most activity. Reference total reach or total engagement if available. Set the tone — this paragraph tells the client immediately whether it was a good month or a challenging one, without requiring them to read the tables.

**Paragraph 2 — Most significant achievement or challenge**
Identify the single most noteworthy thing from the month. If it was a strong month: what was the standout win and why does it matter? If it was a challenging month: what was the main difficulty and what caused it? Be specific — name the platform, the metric, and the magnitude.

**Paragraph 3 — Strategic implication**
Explain what this month's performance means for the strategy going forward. Does it confirm the current approach is working? Does it suggest a pivot is needed? Link back to the client's primary goal. Keep this forward-facing — the client should finish the summary knowing what to expect or do next.

---

### 2. Platform-by-Platform KPI Table

Produce one table per active platform. Use the traffic light system:
- ✅ On target
- 🟡 Slightly below target (within 15% of target)
- 🔴 Below target (more than 15% below target)

Include a one-sentence commentary below each platform table noting the most important trend.

---

**Facebook**

| Metric | Last month | This month | Target | Status | Change % |
|---|---|---|---|---|---|
| Page likes / followers | | | | | |
| Post reach (total) | | | | | |
| Engagement rate (avg) | | | | | |
| Messages received | | | | | |

---

**Instagram**

| Metric | Last month | This month | Target | Status | Change % |
|---|---|---|---|---|---|
| Followers | | | | | |
| Reach (total) | | | | | |
| Engagement rate (avg) | | | | | |
| Saves (total) | | | | | |
| Reel views (total) | | | | | |

---

**LinkedIn**

| Metric | Last month | This month | Target | Status | Change % |
|---|---|---|---|---|---|
| Page followers | | | | | |
| Impressions (total) | | | | | |
| Engagement rate (avg) | | | | | |
| Post link clicks | | | | | |

---

**WhatsApp**

| Metric | Last month | This month | Target | Status | Change % |
|---|---|---|---|---|---|
| Broadcasts sent | | | | | |
| Estimated open rate | | | | | |
| Enquiries received via WhatsApp | | | | | |
| Catalogue views (if applicable) | | | | | |

*Note: WhatsApp Business Analytics are limited. Open rate is an estimate based on read receipts where visible. Enquiry tracking requires the client to log incoming messages by source.*

---

**TikTok**

| Metric | Last month | This month | Target | Status | Change % |
|---|---|---|---|---|---|
| Followers | | | | | |
| Total video views | | | | | |
| Average video completion rate | | | | | |
| Total shares | | | | | |

---

**YouTube**

| Metric | Last month | This month | Target | Status | Change % |
|---|---|---|---|---|---|
| Subscribers | | | | | |
| Total views | | | | | |
| Watch time (hours) | | | | | |
| Average view duration | | | | | |

---

**X / Twitter**

| Metric | Last month | This month | Target | Status | Change % |
|---|---|---|---|---|---|
| Followers | | | | | |
| Impressions (total) | | | | | |
| Engagement rate (avg) | | | | | |

---

Only include tables for platforms the client is active on. Remove unused platform tables from the final document.

---

### 3. Top 3 Posts This Month

For each of the three highest-performing posts:

**Post [N] — [Platform], [Date]**
- **Content type:** [Image / Video / Carousel / Reel / Text]
- **Key metric:** [Reach: X / Engagement rate: X%]
- **Analysis:** Two sentences. Sentence one: describe what the content was and what it said. Sentence two: explain specifically why it performed well — format, hook, topic relevance, timing, emotional pull, or audience fit.

---

### 4. What Worked This Month

Three bullets. Each bullet must be specific — name the platform, the tactic, and the result. Avoid generic statements such as "video content performed well." Write instead: "Instagram Reels posted on Tuesday and Thursday mornings achieved an average engagement rate of 6.2%, above our 4% target, driven by the behind-the-scenes production content series."

- [Specific win 1]
- [Specific win 2]
- [Specific win 3]

---

### 5. What Did Not Work This Month

Two bullets. Be honest. Name the platform, the tactic, and the likely cause of underperformance. Include a proposed fix — what will change next month as a result.

- [What underperformed] → [Proposed fix]
- [What underperformed] → [Proposed fix]

---

### 6. What We Are Testing Next Month

List 2–3 experiments planned for the coming month. For each, state:
- What the test is (specific tactic or format)
- The hypothesis (why this might work)
- How success will be measured

This section demonstrates strategic thinking and keeps the client informed of the approach before it is executed.

---

### 7. Paid Social Performance

*Include this section only if paid ads were running this month. If no paid activity occurred, replace this section with a single sentence: "No paid social activity this month."*

| Metric | Value |
|---|---|
| Total spend this month | UGX / USD [amount] |
| Total paid reach | |
| Cost per result | UGX / USD [amount] per [result type] |
| Best-performing ad | [Brief description — format, audience, offer] |

**Recommendation for next month's paid activity:**
One paragraph. Should the spend increase, decrease, or stay the same? Which audience or format should be prioritised? What should be changed in the creative or targeting?

---

### 8. Recommendations for Next Month

Produce 3–5 specific recommendations. Each must follow this format:

**[N]. [Title]**
- **What to do:** Specific action
- **Why:** Evidence from this month's data that supports the recommendation
- **Expected outcome:** What should improve and by how much (or by when)

Ensure recommendations are grounded in the data from this report — not generic best practices unconnected to the client's actual results.

---

### Report Footer

**Next report date:** [First week of following month — specify date]
**Prepared by:** [Consultant name] | [Consultant email or contact]
**Data sources:** Platform native analytics (Meta Business Suite, LinkedIn Analytics, TikTok Business Centre, YouTube Studio, X Analytics). All metrics are platform-reported. WhatsApp metrics are partially estimated due to platform limitations.

---

## Quality Criteria

Output meets the standard if it:

- Period summary paragraphs are written in plain English, readable by a business owner without digital marketing expertise
- Every KPI table uses traffic light status correctly — green is only assigned when the target is met or exceeded
- Top posts analysis explains *why* each post worked — not merely what the post was
- "What did not work" section is honest and includes a proposed fix for each item, not just an observation
- Recommendations are each linked to specific data from the report — no generic advice
- Paid social section (where applicable) includes a clear spend-versus-result assessment and a forward recommendation
- Report footer specifies the next report date and data sources
- British English throughout — no American spellings

---

## Framework Reference

Apply the **RACE framework** (Chaffey, 2024) when interpreting platform data: metrics map to Reach (awareness), Act (engagement, clicks), Convert (enquiries, sales), and Engage (loyalty, repeat engagement). Note which stages are strong and which need attention.

*Chaffey, D. (2024) Digital Marketing: Strategy, Implementation and Practice. 8th edn. Harlow: Pearson.*
*Bodnar, K. and Cohen, J. (2012) The B2B Social Media Book. Hoboken: Wiley.*

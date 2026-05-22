---
name: ai-predictive-analytics-social
description: >
  Apply predictive analytics to social media strategy and content decisions.
  Invoke when a client wants to move beyond vanity metrics to data-driven
  forecasting of audience behaviour, content performance, and campaign ROI on
  social media platforms. Based on Johnsen (2024) and Lamplugh (2024).
---
# AI Predictive Analytics for Social Media

<!-- dual-compat:start -->
## Use when
- Apply predictive analytics to social media strategy and content decisions. Invoke when a client wants to move beyond vanity metrics to data-driven forecasting of audience behaviour, content performance, and campaign ROI on social media platforms. Based on Johnsen (2024) and Lamplugh (2024).
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

Transform a client's existing social media data into forward-looking
forecasts: which content will perform, which audience segments are at risk of
disengaging, and what revenue social campaigns are likely to generate.

Most social media analytics is descriptive — it tells you what happened.
Predictive analytics tells you what is likely to happen next, enabling
proactive decisions rather than reactive responses (Johnsen, 2024; Lamplugh,
2024). This skill bridges the gap between a client's raw platform exports and
actionable forecasting, without requiring a data science team.

After completing this skill, refer the client to `meta-roi-framework` to
build the financial case for continued investment, or to
`ai-data-foundation-plan` if data quality gaps prevent effective prediction.

---

## Required Inputs

Ask for the following before generating any output:

1. **Client business name** — trading name and legal entity if different
2. **Industry** — retail, financial services, NGO, hospitality, education,
   professional services, etc.
3. **Country and city** — defaults to Uganda/Kampala if not specified
4. **Active social platforms** — Facebook, Instagram, WhatsApp, TikTok,
   LinkedIn, YouTube, X/Twitter (list all in active use)
5. **Available data sources** — Meta Business Suite, Google Analytics 4,
   email platform (Mailchimp, Brevo, etc.), CRM, sales data — specify which
   are accessible and in what format (dashboard only / exportable to Excel)
6. **Data history available** — how many months of post-performance data
   exist; minimum threshold for meaningful prediction is 3 months
7. **Primary prediction goal** — select one:
   - Audience retention (reduce follower churn and disengagement)
   - Content performance (forecast which posts will achieve highest reach
     and engagement)
   - Campaign ROI (project revenue from a planned social campaign)
   - Customer segmentation (identify highest-value audience groups)

---

## From Descriptive to Predictive Analytics

Establish clearly which stage of analytics the client is currently at before
proposing predictive methods.

| Stage | Question answered | Example |
|---|---|---|
| **Descriptive** | What happened? | "Our reach dropped 30% last month" |
| **Diagnostic** | Why did it happen? | "Reach dropped because we posted 40% less frequently" |
| **Predictive** | What is likely to happen next? | "Based on 6 months of data, reach typically drops in this period — increase posting frequency 2 weeks before" |
| **Prescriptive** | What should we do about it? | "Publish 4 video posts per week on Tuesdays and Thursdays to maintain reach above the 3-month average" |

Most EA clients with 3+ months of Meta Business Suite data are ready to move
from descriptive to predictive. Prescriptive recommendations follow naturally
once predictions are validated against actual outcomes.

---

## Five Predictive Use Cases for Social Media

Match the use case to the client's stated primary prediction goal. Address
the highest-priority use case in full; summarise the remaining four briefly.

---

### 1. Follower Churn Prediction

**What it predicts:** Identifies follower segments or subscriber groups
likely to disengage before they leave — enabling pre-emptive content
intervention.

**Data needed:** Engagement history per follower segment (age, gender,
location), posting frequency over time, content type performance by segment.

**EA feasibility:** Medium — requires 3+ months of audience engagement data
from Meta Business Suite. Segment-level engagement data is available from
the Insights export; per-follower data requires third-party tools.

**Example output:**
> "The 18–24 segment has shown declining engagement for 6 consecutive weeks.
> Shift content mix toward video and interactive formats (polls, questions)
> for this segment over the next 30 days and measure re-engagement rate."

---

### 2. Content Performance Prediction

**What it predicts:** Forecasts which content types, topics, and formats will
drive highest engagement in the next 30 days based on historical patterns.

**Data needed:** 6+ months of post performance exported from Meta Business
Suite — reach, engagement rate, and click-through rate sorted by: format
(video / image / carousel / text), topic (product / education /
entertainment / community), posting time, and day of week.

**EA feasibility:** High — all required data is available directly from the
Meta Business Suite insights export at no additional cost.

**Example output:**
> "Video posts published Tuesday 7–9 pm achieve 2.3× average reach compared
> to all other format/time combinations. Schedule a minimum of 4 video posts
> per week in this slot. Carousel posts on Saturday mornings are the
> second-highest performer for the education topic category."

---

### 3. Audience Personalisation

**What it predicts:** Which content variant each audience segment is most
likely to engage with — enabling a segmented content calendar rather than
a single feed.

**Data needed:** Demographic segment breakdown from Meta Business Suite,
past content preferences by segment (which post types each age/gender group
engages with most), platform behaviour differences across segments.

**EA feasibility:** Medium — requires audience segmentation data available
from the platform. Personalisation at scale requires a scheduling tool with
segmentation capability (e.g., Hootsuite, Buffer, or Meta's native targeting
tools for organic posts).

**Example output:**
> Content calendar with segment-specific post variants for the top 3
> audience groups: (a) 25–34 urban women — aspirational lifestyle and
> behind-the-scenes content; (b) 35–44 professional men — product
> performance and business outcomes; (c) 18–24 students — entertainment,
> humour, and community challenges.

---

### 4. Social Commerce Forecasting

**What it predicts:** Projects the revenue contribution from a planned
social-driven campaign before it launches, based on historical campaign
performance data.

**Data needed:** Past campaign performance (reach, clicks, conversion rate),
link click-to-purchase conversion rates (from GA4 or manual tracking),
average order value (UGX), seasonal purchasing patterns.

**EA feasibility:** Low to Medium — requires UTM tracking to be in place
(see `meta-utm-tracking`) and e-commerce or sales data linkage. Many EA
SMEs maintain sales data in Excel, which is sufficient if UTM data is also
recorded.

**Example output:**
> "This WhatsApp broadcast campaign is projected to generate UGX 12–18
> million based on historical conversion rates (2.8%) applied to the
> expected reach of 4,500 contacts. This assumes offer parity with the
> March 2024 campaign. Revenue forecast confidence is medium — validate
> against actual outcome and update the model."

---

### 5. Cross-Sell and Upsell Identification

**What it predicts:** Identifies which audience members are most likely to
purchase additional products or upgrade from their current product tier.

**Data needed:** Purchase history linked to social media identity, social
engagement patterns per customer, content interaction history (which product
posts a customer has engaged with over time).

**EA feasibility:** Low — requires CRM integrated with social media data.
Suitable for clients with a functional CRM and a dedicated social media
audience (e.g., SACCO members, repeat retail customers, subscription
service clients).

**Example output:**
> "A segment of 340 followers has engaged with product posts 3 or more times
> in the past 90 days but has not purchased the premium tier. Create a
> dedicated WhatsApp broadcast or Facebook retargeting message with an
> introductory offer. Estimated conversion rate based on past similar
> segments: 8–12%."

---

## RFM Analysis for Social Audiences

RFM (Recency, Frequency, Monetary) is a customer segmentation model
originally used in direct marketing (Johnsen, 2024). Apply it to social
media audiences to prioritise where to invest content resources.

**Definitions applied to social media:**

| Dimension | Definition | Measurement |
|---|---|---|
| **Recency** | When did this follower last engage with content? | Last 7 days / 8–30 days / 31–90 days / Inactive (90+ days) |
| **Frequency** | How often do they engage? | Daily / Weekly / Occasional / Rare |
| **Monetary** | What is their actual or estimated customer value? | High / Medium / Low / Unknown |

**Apply RFM to create four actionable segments:**

| Segment | Profile | Strategy |
|---|---|---|
| **VIP** | High R, High F, High M | Reward with exclusive content, early access, direct personal engagement via WhatsApp DM |
| **Loyal** | Medium–High R, High F, Medium M | Nurture with consistency; invite to generate UGC; recognise publicly |
| **At-Risk** | Low R, Any F, Any M | Reactivation campaign; try a new content format; send a direct re-engagement message |
| **Dormant** | Inactive R, Low F, Unknown M | Low investment; occasional broad-reach post only; accept natural attrition |

For most EA clients using Meta Business Suite, RFM scoring is approximate —
use audience segment engagement trends rather than per-follower data. A
spreadsheet-based manual RFM score is sufficient for clients without
specialist tools.

---

## Predictive Content Calendar

Use historical engagement data to build a data-driven posting strategy for
the next 30 days. Follow these five steps exactly:

**Step 1 — Export data.**
Export 6 months of post performance from Meta Business Suite: reach,
engagement rate, clicks, and saves — one row per post. Include the post
date, time, format, and a brief topic label.

**Step 2 — Categorise posts.**
Add three classification columns to the export:
- Format: Video / Image / Carousel / Text / Story / Reel
- Topic: Product / Education / Entertainment / Community / Promotion
- Time slot: Morning (6–10 am) / Midday (11 am–2 pm) / Evening (6–9 pm)
  / Late night (9 pm+)

**Step 3 — Analyse with AI.**
Upload the labelled export to Claude or ChatGPT and prompt:
> "Identify which combinations of format, topic, and posting time achieve
> the highest engagement rate. Rank the top 5 combinations. Identify any
> formats or topics that consistently underperform. Suggest a weekly
> posting schedule based on these patterns."

**Step 4 — Build the calendar.**
Construct next month's content calendar prioritising the top-performing
combinations. Allocate at least 60% of posts to proven formats; reserve
40% for testing new formats and topics.

**Step 5 — Review and update.**
At the end of each month, compare actual post performance against the
predictions. Update the export and re-run the analysis. Each iteration
improves accuracy.

---

## Five-Step Data Science Workflow

Apply this workflow to any predictive analytics engagement
(Lamplugh, 2024):

1. **Collect** — Identify all available data sources: Meta Business Suite,
   GA4, WhatsApp Business statistics, email platform analytics (open rates,
   click rates), and sales data. For each source, confirm whether it is
   exportable to Excel or CSV.

2. **Clean** — Remove incomplete records (posts with missing engagement
   data), standardise date and time formats across sources, ensure topic
   and format labels are consistent. Flag records where data is missing and
   do not include them in the model.

3. **Analyse** — Identify patterns, correlations, and anomalies. Use AI
   tools (Claude, ChatGPT) to accelerate pattern identification on uploaded
   exports. Document the top 3 findings with supporting data.

4. **Implement** — Translate insights into concrete content decisions:
   which formats to prioritise, which time slots to use, which segments to
   target. Update the content calendar and briefing document.

5. **Monitor** — Track whether predictions were accurate. After each
   campaign or monthly posting cycle, compare predicted engagement against
   actual outcomes. Record the accuracy rate. Use discrepancies to refine
   the next model iteration.

---

## Tool Options for Non-Data-Science Teams

Recommend tools based on the client's technical capacity and budget. Do not
recommend enterprise tools to SME clients without budget and technical
support.

| Tool | What it does | EA accessibility | Approx. cost |
|---|---|---|---|
| Meta Business Suite Insights | Social media analytics and basic trend data | Yes — built-in | Free |
| Google Analytics 4 | Web traffic, referral sources, and conversion analytics | Yes — free | Free |
| Claude / ChatGPT (with data export) | Pattern analysis on uploaded spreadsheet data | Yes — cloud-based | Included in subscription |
| Akkio | AutoML for non-technical business teams | Yes — cloud-based | From $49/month USD |
| Obviously AI | No-code predictive analytics for marketers | Yes — cloud-based | From $75/month USD |
| Pecan AI | Predictive analytics for marketing and revenue | Limited EA adoption | Enterprise pricing |

**Selection guidance:**
- Clients with no analytics budget: Meta Business Suite + Claude/ChatGPT
  with manual export — sufficient for content performance prediction.
- Clients with a small analytics budget (under $100/month): Akkio for
  structured prediction on clean data exports.
- Clients with a dedicated analyst: Obviously AI for self-serve model
  building without coding.
- Enterprise clients: evaluate Pecan AI alongside CRM-native analytics
  tools via `ai-vendor-evaluation`.

---

## EA Data Sources Reference

Available data sources for Ugandan businesses that do not have enterprise
analytics tools:

- **Meta Business Suite** — page insights, post performance by format and
  time, audience demographics, exportable to Excel. The primary data source
  for most EA social media predictions.
- **WhatsApp Business** — message statistics (sent, delivered, read rate)
  for broadcast campaigns. Limited but useful for measuring campaign reach
  and reactivation rate.
- **Google Analytics 4** — website traffic, social referral sources,
  conversion events. Free and available to any client with a website.
  Requires UTM parameters to attribute social traffic accurately (see
  `meta-utm-tracking`).
- **Email platform analytics** — open rates, click rates, unsubscribes.
  Available from Mailchimp, Brevo, and similar tools. Useful for
  cross-channel audience behaviour modelling.
- **Sales records** — transaction data manually maintained in Excel or
  accounting software (QuickBooks, Wave). Can be combined with social data
  manually to calculate social commerce conversion rates without specialist
  tools.

---

## Quality Criteria

Assess the output against these criteria before delivering to the client:

- Primary prediction goal is identified and matched explicitly to one of the
  five use cases; the output addresses that use case in full with a concrete
  example output in the client's industry context.
- Data inventory is completed — all available EA data sources listed, each
  assessed for exportability and months of history available; gaps that
  prevent prediction are flagged with a recommended remediation action.
- RFM segmentation is applied to the client's social audience — at least
  three segments (VIP, Loyal, At-Risk or equivalent) are identified with
  specific content strategies per segment.
- Predictive content calendar is built using the five-step process and
  grounded in actual historical engagement data from the client's platforms;
  it is not a generic posting schedule.
- Five-step data science workflow is documented with specific actions for
  the client's named platforms and data sources — not described in
  generalities.
- Tool recommendation is matched to the client's stated technical capacity
  and budget; enterprise tools are not recommended to clients without the
  budget or support to implement them.
- At least one prediction is identified for testing in the next 30-day
  cycle, with a clear mechanism for comparing the predicted outcome against
  actual performance.

---

## References

- Johnsen, M. (2024) *AI in Digital Marketing*. Mercury Learning.
- Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn. Mercury
  Learning.
- Ltifi, M. (ed.) (2025) *Advances in Digital Marketing in the Era of
  Artificial Intelligence*. CRC Press.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and
  Practice*. Pearson.

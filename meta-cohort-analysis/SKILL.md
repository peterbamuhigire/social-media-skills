---
name: meta-cohort-analysis
description: >
  Builds time-based and behaviour-based user cohorts in GA4, tracks retention
  and lifetime value by cohort, and translates cohort data into client-language
  statements that demonstrate campaign durability — not just reach. Invoke when
  a client asks which campaigns produce repeat customers, when aggregate metrics
  are masking poor retention, or when preparing a report that must show long-term
  campaign value.
---

# Cohort Analysis for Client Reporting

**Source:** Raaz (c.2023) *Web Analytics Blueprint*

---

## Required Inputs

Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry** (e-commerce, services, B2B SaaS, hospitality, etc.)
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. demonstrate campaign ROI, identify best acquisition channel, justify budget reallocation)
5. **GA4 access level** (Admin / Editor / Viewer — determines which steps are available)
6. **Reporting period** (weekly or monthly cohorts; 12-week or 12-month window)
7. **Acquisition channels in use** (organic search, paid social, direct, referral, email, WhatsApp, etc.)

---

## What a Cohort Is

A cohort is a group of users who share a defining characteristic within a defined time period. Common cohort definitions:

- All users whose **first session** occurred in a given week or month (acquisition cohort)
- All users who completed a **specific action** — made a purchase, downloaded a lead magnet, subscribed to an email list — in a given period (behaviour cohort)

Aggregate metrics (total sessions, total revenue) hide the difference between campaigns that bring one-time buyers and campaigns that build loyal, repeat customers. Cohort analysis reveals which acquisition channels produce high-LTV customers versus one-transaction visitors.

---

## Two Cohort Types

### Acquisition Cohorts
Users grouped by when they first arrived (Week 1, Week 2, etc.).

**Track:** What percentage of Week 1 users returned in Week 2, Week 3, Week 4?

Use for: retention analysis, identifying which channels produce loyal audiences.

### Behaviour Cohorts
Users grouped by an action they took (first purchase, webinar attendance, lead magnet download).

**Track:** What percentage converted to the next funnel stage?

Use for: funnel optimisation, identifying where drop-off occurs after a specific action.

---

## Building Cohorts in GA4

1. In GA4: **Explore → Cohort Exploration**
2. Set cohort type:
   - *Acquisition date* — groups by first session date
   - *Event-based* — groups by a named event (e.g. `purchase`, `sign_up`, `generate_lead`)
3. Set cohort granularity: **weekly** (for fast-moving campaigns) or **monthly** (for longer sales cycles)
4. Set metric: active users, revenue, conversions, or goal completions
5. Set time window: 12-week or 12-month
6. Apply channel filter: segment by **Session default channel group** to compare organic vs. paid vs. referral vs. WhatsApp cohorts

**Permission note:** Cohort Exploration requires at minimum Viewer access to GA4. To create custom segments by channel, Editor access is required.

---

## Key Insights to Extract

For each cohort analysis, extract and report the following:

| Insight | How to read it |
|---|---|
| **Week-4 retention rate** | What percentage of Week 1 users are still active 4 weeks later? Under 10% is typical for cold traffic; above 30% indicates a loyal audience |
| **Channel comparison** | Which acquisition channel produces the highest Week-4 retention rate? |
| **Revenue by cohort** | Which cohort contributes the most total revenue over 6 months? |
| **Decay curve shape** | Slow decay = loyal audience building. Steep drop after Week 1 = one-time curiosity traffic — review content and offer alignment |

---

## Translating Cohort Data for Clients

Do not present raw cohort tables to clients — they cannot interpret colour-coded retention grids without guidance. Translate every cohort analysis into three plain-language client statements:

**Statement 1 — Retention:**
"Of every 100 people who found you through [channel] in [month], [X] were still engaging with your brand 4 weeks later."

**Statement 2 — Channel comparison:**
"Your [channel A] audience retains twice as well as your [channel B] audience — meaning [channel A] produces more durable customers at the same acquisition cost."

**Statement 3 — Cohort revenue:**
"Your [month] cohort is your most valuable — they have generated [X]% more revenue per customer than the [earlier month] cohort."

Pair each statement with a single clear chart (line chart showing retention decay by channel). See `meta-dashboard-design` for chart selection and mobile-first design rules.

---

## Cohort Reporting Output Format

Generate a cohort analysis report structured as follows:

**Section 1 — Executive Summary (3 sentences)**
What the cohort data shows at a glance. Which channel or period is performing best. The single recommended action.

**Section 2 — Acquisition Cohort Table**
Present a simplified cohort table (Week 0 through Week 8 maximum) with the top 3 acquisition channels compared. Highlight the Week-4 retention row.

**Section 3 — Behaviour Cohort Funnel**
If behaviour cohort data is available: show the conversion percentage from acquisition action to next funnel stage for each cohort period.

**Section 4 — Channel Comparison Summary**
A ranked list of channels by Week-4 retention rate. One sentence interpretation per channel.

**Section 5 — Recommendations**
Three SMART actions derived from the cohort data. Format each as:
- **Recommendation:** [action]
- **Rationale:** [what the cohort data shows]
- **Success metric:** [how to measure the outcome]

---

## EA-Specific Considerations

- **WhatsApp as an acquisition channel:** GA4 does not automatically track WhatsApp referrals. Advise the client to use UTM parameters on all WhatsApp links (e.g. `?utm_source=whatsapp&utm_medium=social&utm_campaign=[name]`). See `meta-utm-tracking` for UTM setup.
- **Mobile-first data:** In Uganda/EA, the majority of sessions originate from mobile devices. Cohort analysis should always segment by device type to identify whether mobile vs. desktop users retain differently.
- **Short purchase cycles:** For EA e-commerce and service businesses, use weekly cohorts rather than monthly — the typical EA purchase decision cycle is shorter than in Western markets, and monthly cohorts lose resolution.

---

## Quality Criteria

Output meets the standard for this skill if:

- Every cohort insight is translated into a plain-language client statement — no raw data tables presented without interpretation
- The report distinguishes between acquisition cohorts and behaviour cohorts and uses the correct type for the client's stated goal
- Channel comparison is included, with at least two channels compared by retention rate
- At least three SMART recommendations are derived directly from the cohort data — not generic analytics advice
- WhatsApp is addressed as an acquisition channel if the client uses it for customer acquisition
- The Week-4 retention rate is calculated and contextualised against the 10% (cold traffic) and 30% (loyal audience) benchmarks
- All monetary values use the client's local currency (UGX for Uganda; KES for Kenya) unless otherwise specified
- Language is British English throughout; imperative in all instructional sections

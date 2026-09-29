# Retention Cohorts and LTV

Merged from skills/meta-analytics-ops/meta-cohort-analysis on 2026-09-29 at 8eacccb; preservation map: [meta-cohort-analysis.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-cohort-analysis.md)

## When to use this reference

Read this reference when the ROI question needs more than one average customer value: the client wants to know which acquisition channel brings back repeat customers, whether a campaign produced one-time buyers or a loyal base, or which month's intake has earned the most per customer. Aggregate totals (total sessions, total revenue) hide that difference; a cohort analysis shows which channels produce high-LTV customers and which produce one-transaction visitors. Feed the per-channel results into the `CLV by Acquisition Cohort` step in [roi-model-method.md](roi-model-method.md) and the TLV:COCA ratio.

Method source: Raaz (c.2023) *Web Analytics Blueprint* (author initials and publisher unverified: not found in Open Library, 29 Sep 2026). Before building the table or choosing a churn formula, read § Reading cohorts in [OMTM, lines in the sand and stage metrics](../../meta-social-metrics-framework/references/omtm-lines-in-the-sand-and-stage-metrics.md) (the three-view cohort reveal and churn denominators).

## Inputs

Ask for the following before producing the cohort report:

| Input | What to capture |
|---|---|
| Client business name | Trading name |
| Industry | E-commerce, services, B2B SaaS, hospitality, etc. |
| Country / city | Defaults to Uganda / East Africa |
| Primary goal | For example: demonstrate campaign ROI, identify the best acquisition channel, justify a budget reallocation |
| GA4 access level | Admin / Editor / Viewer — decides which build steps are available |
| Reporting period | Weekly or monthly cohorts; 12-week or 12-month window |
| Acquisition channels in use | Organic search, paid social, direct, referral, email, WhatsApp, etc. |
| Event-level cohort data, date range and cohort definition | Dated export from the client's approved systems; without it, stop the cohort decision and issue a bounded partial output |

## Decision rules

| Situation | Action | Failure or risk avoided |
|---|---|---|
| The goal is retention, or "which channel builds a loyal audience" | Use an acquisition cohort (grouped by first-arrival week or month) | Answering a loyalty question with funnel data |
| The goal is funnel optimisation or drop-off after a named action | Use a behaviour cohort (grouped by the action taken) | Missing where drop-off happens after the action |
| Fast-moving campaign, or an EA e-commerce or service business | Use weekly granularity; the typical EA purchase decision cycle is shorter than in Western markets, so monthly cohorts lose resolution | Averaging away the signal |
| Long sales cycle | Use monthly granularity | Noisy, near-empty weekly cells |
| The client acquires customers through WhatsApp | Require UTM parameters on every WhatsApp link before reading channel cohorts; see [measurement-tracking-plan](../../measurement-tracking-plan/SKILL.md) | WhatsApp traffic lost in Direct, because GA4 does not track WhatsApp referrals automatically |
| Viewer access only | Run Cohort Exploration; request Editor access before building custom channel segments | Promising a channel split the access level cannot produce |

## Procedure

### 1. Define the cohort

A cohort is a group of users who share a defining characteristic within a defined time period. Two common definitions:

- **Acquisition cohort** — all users whose first session fell in a given week or month (Week 1, Week 2, and so on). Track: what percentage of Week 1 users returned in Week 2, Week 3, Week 4? Use for retention analysis and for finding which channels produce loyal audiences.
- **Behaviour cohort** — all users who completed a specific action (made a purchase, attended a webinar, downloaded a lead magnet, subscribed to an email list) in a given period. Track: what percentage converted to the next funnel stage? Use for funnel optimisation and for locating drop-off after that action.

### 2. Build the cohort in GA4

1. Open **Explore → Cohort Exploration**.
2. Set the cohort type: *Acquisition date* (groups by first session date) or *Event-based* (groups by a named event, for example `purchase`, `sign_up`, `generate_lead`).
3. Set granularity: **weekly** for fast-moving campaigns, **monthly** for longer sales cycles.
4. Set the metric: active users, revenue, conversions or goal completions.
5. Set the time window: 12 weeks or 12 months.
6. Apply a channel filter: segment by **Session default channel group** to compare organic, paid, referral and WhatsApp cohorts.
7. Segment by device type as well. In Uganda and East Africa most sessions come from mobile devices; check whether mobile and desktop users retain differently.

Permission note: Cohort Exploration needs at least Viewer access to GA4; custom segments by channel need Editor access. GA4 menu names and access rules can change — verify before stating (no register record).

WhatsApp link tagging example: `?utm_source=whatsapp&utm_medium=social&utm_campaign=[name]`.

### 3. Extract the insights

| Insight | How to read it |
|---|---|
| **Week-4 retention rate** | What percentage of Week 1 users are still active 4 weeks later? Under 10% is typical for cold traffic; above 30% indicates a loyal audience |
| **Channel comparison** | Which acquisition channel produces the highest Week-4 retention rate? |
| **Revenue by cohort** | Which cohort contributes the most total revenue over 6 months? |
| **Decay curve shape** | Slow decay = a loyal audience is building. A steep drop after Week 1 = one-time curiosity traffic; review content and offer alignment |

The 10% and 30% bands are undated comparators from the method source: label them as provisional benchmarks, not as the client's result (verify before stating; no register record).

### 4. Carry the result into CLV and ROI

Calculate CLV separately for the customers each channel acquired (organic social, paid social, referral, email, events, WhatsApp) and use the per-channel figure in the TLV:COCA ratio in the SKILL.md. A channel with a lower COCA but a steep Week-1 drop may be worth less than a costlier channel whose cohort keeps buying.

### 5. Translate for the client

Do not hand raw cohort tables to clients; they cannot read colour-coded retention grids without guidance. Turn every analysis into three plain-language statements:

1. **Retention:** "Of every 100 people who found you through [channel] in [month], [X] were still engaging with your brand 4 weeks later."
2. **Channel comparison:** "Your [channel A] audience retains twice as well as your [channel B] audience — meaning [channel A] produces more durable customers at the same acquisition cost."
3. **Cohort revenue:** "Your [month] cohort is your most valuable — they have generated [X]% more revenue per customer than the [earlier month] cohort."

Pair each statement with one clear chart: a line chart showing retention decay by channel. For chart selection and mobile-first dashboard rules, use [meta-reporting](../../meta-reporting/SKILL.md).

## Template — cohort analysis report

**Section 1 — Executive summary (3 sentences).** What the cohort data shows at a glance; which channel or period performs best; the single recommended action.

**Section 2 — Acquisition cohort table.** A simplified table from Week 0 to Week 8 at most, comparing the top 3 acquisition channels. Highlight the Week-4 retention row.

**Section 3 — Behaviour cohort funnel.** Where behaviour cohort data exists: the conversion percentage from the acquisition action to the next funnel stage for each cohort period.

**Section 4 — Channel comparison summary.** Channels ranked by Week-4 retention rate, with one sentence of interpretation per channel.

**Section 5 — Recommendations.** Three SMART actions derived from the cohort data, each written as:

- **Recommendation:** [action]
- **Rationale:** [what the cohort data shows]
- **Success metric:** [how to measure the outcome]

## Release checklist

- [ ] Every cohort insight is translated into a plain-language client statement; no raw table is shown without interpretation.
- [ ] The report distinguishes acquisition cohorts from behaviour cohorts and uses the type that fits the client's stated goal.
- [ ] At least two channels are compared by retention rate.
- [ ] At least three SMART recommendations come directly from the cohort data, not generic analytics advice.
- [ ] WhatsApp is addressed as an acquisition channel wherever the client uses it for acquisition.
- [ ] The Week-4 retention rate is calculated and set against the 10% (cold traffic) and 30% (loyal audience) comparators, labelled as provisional.
- [ ] Device-type split is shown or marked `not assessed`.
- [ ] Monetary values use the client's local currency (UGX for Uganda; KES for Kenya) unless otherwise specified.
- [ ] British English throughout; instructional sections in the imperative.

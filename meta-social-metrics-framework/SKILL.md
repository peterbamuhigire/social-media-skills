---
name: meta-social-metrics-framework
description: >
  Produces a three-tier social media metrics framework aligned to business objectives —
  defining primary metrics (tied to business goals), secondary metrics (channel health
  indicators), and comparative metrics (benchmarks and share of voice). Distinguishes
  vanity metrics from business metrics, defines what to report to whom, and generates
  SMART targets per metric tier. Invoke when a client is only tracking followers and
  likes, when setting up a new reporting system, when selecting metrics for a monthly
  report, or when a client challenges the value of social media and the consultant
  needs to build a business-linked measurement case. Based on Neal Schaffer,
  Maximize Your Social (Wiley, 2013).
---

# Social Media Metrics Framework

## Required Input

Ask the client for the following before generating the framework:

1. **Business name** — trading name and any sub-brands
2. **Industry** — sector and type of business (B2C retail, B2B services, NGO, etc.)
3. **Country/city** — defaults to Uganda / East Africa if not specified
4. **Primary business goal** — select one: generate leads/enquiries, drive website traffic, drive sales, grow email/WhatsApp list, drive footfall, build brand awareness, grow community
5. **Current metrics being tracked** — list what the client reports now (paste their current dashboard or describe it)
6. **Analytics access** — confirm which platforms the client can access: GA4, Meta Business Suite, TikTok Analytics, LinkedIn Analytics, YouTube Studio, other
7. **Report audience** — who receives reports: business owner only / marketing team / board / all three
8. **Reporting cadence** — how often reports are produced: weekly / monthly / quarterly

---

## The Core Problem (Schaffer, 2013)

Most social media accounts track vanity metrics — followers, likes, impressions — because they are easy to see and tend to move upward. But vanity metrics do not connect to business outcomes. A brand with 50,000 followers that generates zero enquiries has a measurement problem: it is optimising for the wrong thing.

This framework connects every metric to a business objective. Present this to the client before building the framework:

> "The question is not how many people liked your post. The question is: how many people enquired, bought, visited, or subscribed because of your social media activity?"

---

## Section 1 — The Three-Tier Framework

Apply Schaffer's three-tier hierarchy. Every metric must sit in exactly one tier.

---

### Tier 1 — Primary Metrics (Business Outcomes)

Primary metrics are tied directly to the client's named business goal. These are the only metrics that justify the social media investment to a business owner or board.

Select the row that matches the client's primary goal:

| Business Goal | Primary Metric | How to Track |
|---|---|---|
| Generate leads/enquiries | Number of enquiries from social per month | Ask every new enquiry: "How did you hear about us?"; UTM parameters on links |
| Drive website traffic | Sessions from social (GA4 → Acquisition → Traffic acquisition → Social) | GA4 + UTM parameters on all links |
| Drive sales | Revenue attributed to social | GA4 e-commerce tracking or payment platform (Pesapal, Flutterwave, etc.) with UTM |
| Grow email/WhatsApp list | New subscribers from social per month | Mailchimp / Brevo source tracking; WhatsApp opt-in form source field |
| Drive footfall (retail/restaurant) | Google Business Profile Directions clicks + calls from social | GBP Insights; ask customers at point of sale |
| Build brand awareness | Aided brand recall (survey) or unprompted mentions per month | Quarterly brand tracking survey; social listening tool |
| Grow community | Group or community member growth rate (net new per month) | Facebook Groups Insights; WhatsApp Community admin stats |

**Instruction:** Generate the primary metric for the client's stated goal. Define the baseline value (current month or last 3 months average) before setting any targets.

---

### Tier 2 — Secondary Metrics (Channel Health)

Secondary metrics indicate whether the content and platform strategy is working. They explain why primary metrics move up or down. Track secondary metrics per platform the client is active on.

| Platform | Secondary Metrics to Track |
|---|---|
| Facebook | Reach, engagement rate (ER), video completion rate, page follows and unfollows net |
| Instagram | Reach, ER, saves, profile visits, link-in-bio clicks |
| TikTok | Views, completion rate, shares, profile visits |
| LinkedIn | Impressions, ER, follower growth, post reposts |
| WhatsApp | Broadcast open rate (estimated), reply rate, opt-out rate |
| YouTube | Views, watch time (hours), subscribers gained/lost, thumbnail CTR |
| Email | Open rate, click rate, unsubscribe rate |

**Engagement Rate formula (apply to Facebook, Instagram, LinkedIn, TikTok):**

```
ER = (Likes + Comments + Shares + Saves) ÷ Reach × 100
```

**East Africa ER benchmarks (SME accounts):**

| Platform | Strong ER for EA SMEs |
|---|---|
| Facebook | 2–5% |
| Instagram | 3–6% |
| TikTok | 5–10% (higher due to smaller follower bases) |
| LinkedIn | 1–3% (company pages) |

Use these benchmarks when the client has no historical baseline. State benchmarks numerically; do not say "industry average" without a figure.

---

### Tier 3 — Comparative Metrics (Benchmarks and Context)

Comparative metrics give primary and secondary metrics meaning by placing them in context — against past performance, competitors, or industry standards.

| Comparative Metric | What It Tells You |
|---|---|
| Month-on-month ER change | Whether content quality is improving or declining |
| Year-on-year follower growth | Whether audience is growing at a sustainable rate |
| Net Sentiment Score (NSS) | Whether audience perception is positive, neutral, or negative overall |
| Share of Voice (SOV) vs. named competitors | Whether the brand is growing its presence relative to competitors |
| Cost per result (boosted posts only) | Whether the investment in paid promotion is efficient |

**Share of Voice formula:**

```
SOV = Brand Mentions ÷ Total Market Mentions (brand + all tracked competitors) × 100
```

**Net Sentiment Score formula:**

```
NSS = (Positive Mentions − Negative Mentions) ÷ Total Mentions × 100
```

Cross-reference `meta-sentiment-analysis` for full NSS methodology and `meta-social-listening` for tools to track mentions and SOV in the EA market.

---

## Section 2 — Vanity vs Business Metrics

Produce this table for the client. Present it at the start of any reporting setup engagement to reframe what they should care about.

| Vanity Metric | Why It Misleads | Business Metric to Use Instead |
|---|---|---|
| Follower count | Can be inflated by bots; no demonstrated correlation with revenue | New enquiries from social per month |
| Post likes | Passive and easy to give; no purchase or enquiry intent | Saves and shares (indicate higher intent and content value) |
| Impressions | Counts every view including repeat views of the same person | Unique reach |
| Page views | Counts all visits including bounces; no quality signal | Time on site combined with enquiry form submissions |
| Video views | Platform-defined as low as 3 seconds on most platforms | 50%+ video completion rate |

**Instruction:** When presenting to a client, ask them to identify which column their current reporting falls into. Do not lead with criticism; lead with curiosity — "Which of these are you currently tracking?"

---

## Section 3 — What to Report to Whom

Different audiences need different metrics. Produce a report template for each audience the client serves.

---

### Client / Business Owner — Monthly Report (5 minutes to read)

Include only:

- Enquiries/leads from social this month (vs. last month)
- Revenue or sales attributed to social (if trackable)
- Net Sentiment Score (positive / neutral / negative direction)
- One notable content win — highest performing post with ER and reach
- One priority action for next month

Format: one page. Use plain language. No platform jargon. No graphs unless the client requests them.

---

### Marketing Team / Social Media Manager — Weekly Review (Operational)

Include:

- Posts published vs planned (execution rate as a percentage)
- Engagement rate per post this week
- Follower growth this week (net)
- Any spikes in comments or mentions — flag positive and negative
- Content planned and approved for next week

Format: a brief dashboard or structured table. Reviewed in a weekly team check-in.

---

### Board / Senior Leadership — Quarterly Report (Strategic)

Include:

- ROI calculation using the Bodnar and Cohen (2012) formula: **(TLV − COCA) ÷ COCA**
  - TLV = Total Lifetime Value of customers acquired via social
  - COCA = Cost of Customer Acquisition via social (time + spend)
- Share of Voice trend (3-month rolling)
- Brand awareness indicators — NSS trend over the quarter
- Year-on-year comparison on primary metrics
- Budget vs results — planned spend vs actual spend vs outcomes

Cross-reference `meta-roi-framework` for the full ROI calculation methodology and `deck-quarterly-review` for the slide format when presenting to a board.

---

## Section 4 — Setting SMART Targets

Every metric requires a SMART target before it can be meaningfully tracked. Generate SMART targets for the client's primary and secondary metrics using this structure:

- **Specific:** State the exact metric and direction — not "increase engagement" but "increase Instagram ER from 2.1% to 3.5%"
- **Measurable:** The number must be trackable in a named analytics platform
- **Achievable:** Based on the current baseline and comparable EA benchmarks above
- **Relevant:** Connected to a named business outcome the client cares about
- **Time-bound:** Monthly or quarterly target — not open-ended

**Target-setting rule:** The first 3 months of working with a new client are baseline-building months, not target-hitting months. Do not set performance targets until 3 months of comparable data are available. State this clearly to the client at onboarding.

**Sample SMART target (adapt to client context):**

> "Increase the number of WhatsApp enquiries attributed to Instagram from 4 per month (January baseline) to 10 per month by 30 April 2026, tracked via the source question in the enquiry intake form."

---

## Output Structure

Generate the following sections in order, customised to the client's inputs:

1. **Measurement Problem Statement** — one paragraph summarising what the client is currently measuring and why it is insufficient
2. **Tier 1 — Primary Metric** — the single primary metric matched to the client's business goal, with baseline and tracking method
3. **Tier 2 — Secondary Metrics** — a table of secondary metrics per active platform, with current benchmark ranges
4. **Tier 3 — Comparative Metrics** — which comparative metrics apply given the client's context (not all will be relevant)
5. **Vanity vs Business Metrics table** — presented as a client-facing reframe
6. **Report templates** — one template per audience (owner / marketing team / board), only for audiences the client has identified
7. **SMART targets** — drafted targets for primary and secondary metrics, with the 3-month baseline note if the client is new

---

## Quality Criteria

- All three tiers are defined with specific named metrics, not generic categories
- Primary metrics are linked to the client's named business goal — not generic "brand awareness"
- Vanity vs business metrics table includes at least five pairs, each with an explanation of why the vanity metric misleads
- EA-specific ER benchmarks are stated numerically (e.g. "2–5% for EA SMEs on Facebook") — not vaguely
- Report format is matched to audience — owner, marketing team, and board outputs are distinct in length, language, and content
- SMART target guidance includes the 3-month baseline rule, stated explicitly
- ROI formula (Bodnar and Cohen, 2012) is referenced for board-level reporting with formula components defined
- NSS and SOV formulas are stated explicitly so the client can calculate them without additional tools

---

## Cross-References

- `meta-reporting` — monthly report structure and template
- `meta-roi-framework` — full ROI calculation, TLV and COCA definitions
- `meta-sentiment-analysis` — NSS methodology and sentiment tracking tools
- `meta-social-listening` — tools for tracking SOV and mentions in East Africa
- `deck-quarterly-review` — slide format for presenting metrics to a board or senior leadership

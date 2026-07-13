---
name: meta-sentiment-analysis
description: "Use when scoring supplied conversation data for sentiment, themes and share of voice. Produces sentiment analysis with method, confidence and implications; use `meta-social-listening` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Sentiment Analysis Methodology

> **Scope distinction:** This skill covers the analytical methodology — how to score, calculate, and interpret sentiment data, and how to translate findings into strategic decisions. Use `playbook-sentiment-listening` for the operational setup that generates the raw data. The two skills are complementary: listening provides the data; this skill provides the analysis.

---


<!-- dual-compat-start -->
## Use When

- Use this skill for scoring supplied conversation data for sentiment, themes and share of voice.
- Confirm that `meta-social-listening` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-social-listening` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Dated listening dataset, query taxonomy and sampling method | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Sentiment analysis with method, confidence and implications | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. This is read-only by default: inspect and report without changing source records, accounts, skills or campaigns. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified sentiment analysis with method, confidence and implications. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Dated listening dataset, query taxonomy and sampling method is current and attributable | Produce the full sentiment analysis with method, confidence and implications and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-social-listening` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-social-listening` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the sentiment analysis with method, confidence and implications, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the sentiment analysis with method, confidence and implications without dated listening dataset. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-social-listening` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified dated listening dataset, the skill produces a sentiment analysis with method, confidence and implications with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-social-listening`](../meta-social-listening/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Collect the following before generating any deliverable:

- **Client business name**, industry (e.g., "Kigali Fresh Bakery — food and beverage")
- **Country/city** — defaults to Uganda/Kampala if not specified
- **Primary goal** — select one: brand health tracking / competitor benchmarking / campaign evaluation / crisis response debrief
- **Platforms to analyse** — select all that apply: Facebook / Instagram / TikTok / YouTube / WhatsApp / X/Twitter / LinkedIn
- **Budget for sentiment tools** — select one: none (manual only) / USD 0–30/month / USD 30–100/month / enterprise
- **Languages spoken by audience** — select all that apply: English only / English + Luganda / English + Swahili / other (specify)
- **Competitors to include in share-of-voice** — up to 3 brand names with social handles if known
- **Access to native platform analytics** — yes / no / partial

---

## Section 1: Manual vs. Automated Sentiment Scoring

Choose the scoring method based on the client's tool budget and audience language mix. The hybrid approach is recommended for most East African clients.

### Manual Scoring (for clients without tool budget)

Manual scoring is appropriate when the client has no budget for sentiment tools, when the audience writes primarily in Luganda or Swahili, or when monthly mention volume is below 500 across all platforms.

**Process:**
1. Export or screenshot the last 100 comments, DMs, and mentions per platform
2. Enter each item into a shared Google Sheet or Airtable tracker
3. Classify each item using the four-category scheme below
4. Sub-classify all negative items using the five negative categories
5. Total the counts and calculate NSS (see Section 2)

**Four-category classification scheme:**
- **Positive (P)** — affirming, recommending, praising, sharing with approval
- **Neutral (N)** — informational, questions, factual statements with no clear valence
- **Negative (Neg)** — complaint, criticism, disappointment, detraction
- **Mixed (M)** — contains both positive and negative elements in a single comment

**Five negative sub-categories:**
- Product complaint — quality, features, availability
- Service complaint — staff, communication, responsiveness
- Pricing objection — "too expensive", unfavourable comparison to competitors
- Delivery/fulfilment issue — late, wrong item, logistics failure
- Brand criticism — values, ethics, reputation, public behaviour

**Time required:** 30–45 minutes per platform per month. Budget this time into the monthly reporting cycle.

### Automated Scoring (for clients with tool budget)

Automated scoring is appropriate when English-language mention volume exceeds 500 per month per platform, or when real-time monitoring is required.

**Recommended tools by budget tier:**

| Budget | Tool | Notes |
|---|---|---|
| Free | MonkeyLearn (basic API) | 300 queries/month free; sufficient for small accounts |
| USD 0–30/month | Mention (Starter) | English NLP; basic dashboard |
| USD 30–100/month | Sprout Social / Hootsuite Insights | Integrated with scheduling; stronger reporting |
| Enterprise | Brandwatch | Full NLP suite; social listening + analytics |

**NLP language limitation — critical for EA clients:** English NLP models from all major tools are reliable for standard sentiment detection. Luganda and Swahili NLP is unreliable across all commercial tools as of 2025 — sentiment scores for non-English content will be inaccurate, sometimes inverted. Always manually review Luganda and Swahili comments regardless of tool used.

### Hybrid Approach (Recommended for Most EA Clients)

- Automate English-language monitoring on high-volume platforms (Facebook, Instagram)
- Manually review all WhatsApp conversations, Luganda/Swahili comments, and any active complaint threads
- Feed manual scores into the same tracking sheet as automated scores so NSS is calculated across the full dataset

---

## Section 2: Net Sentiment Score (NSS)

The Net Sentiment Score expresses brand health as a single number, calculated monthly and tracked as a trend. Based on methodology in Funk (2013).

**Formula:**

```
NSS = (Positive mentions − Negative mentions) ÷ Total mentions × 100
```

Mixed comments are excluded from the numerator. Neutral and Mixed comments are included in the denominator (total mentions).

**Worked example:**
- 85 positive comments, 12 negative comments, 43 neutral = 140 total mentions
- NSS = (85 − 12) ÷ 140 × 100 = **52.1**

Express NSS as a number (e.g., 52.1). Never express it as a word (e.g., "good" or "positive").

**NSS benchmarks for EA service businesses:**

| Score | Assessment |
|---|---|
| +60 or above | Strong — brand advocates outweigh detractors significantly |
| +40 to +59 | Healthy — majority positive; address recurring negatives |
| +20 to +39 | Developing — equal parts positive and neutral; negatives need attention |
| 0 to +19 | Concerning — negatives approaching parity with positives; investigate root causes |
| Below 0 | Crisis territory — negatives outweigh positives; trigger `playbook-crisis-communications` |

**Tracking NSS over time:** Report NSS as a monthly trend, not a single snapshot. A trend line is more meaningful than any individual score.

Example trend report: Month 1: +45 → Month 2: +48 → Month 3: +52 (improving, +7 over quarter)

**Tip:** A stable score in the +40s is a better signal than an improving score that started at +15. Always contextualise the number against the trend and the starting baseline.

---

## Section 3: Share of Voice (SOV)

Share of Voice measures the client's portion of the total brand conversation in their competitive set. Based on methodology in Schaffer (2013).

**Formula:**

```
SOV = Client brand mentions ÷ (Client + Competitor A + Competitor B + ...) × 100
```

**Worked example:**
- Client: 240 mentions, Competitor A: 180 mentions, Competitor B: 95 mentions
- SOV = 240 ÷ (240 + 180 + 95) × 100 = **46.2%**

### Gathering SOV Data in the EA Market

Automated monitoring tools are ideal but not always available. Use the following methods in order of preference:

1. **Brandwatch or Mention** — automated if budget allows; most accurate
2. **Google Alerts** — free; captures news articles, blogs, and indexed web content for brand names
3. **Meta Business Suite search** — search competitor brand names in the Facebook search bar to find public posts mentioning them; count manually
4. **Manual search** — search brand names on Facebook, Instagram, TikTok, and YouTube weekly; log counts in a spreadsheet

Record raw mention counts weekly and sum to a monthly total for SOV calculation.

### Competitor Selection Rules

- Select 2–3 direct competitors: same city or region, same price tier, same target audience
- Do not include national or international brands as competitors for local SMEs — the scale difference distorts the metric and produces an SOV figure that is not actionable
- Review the competitor set every quarter; new entrants may need to be added

### SOV Targets and Strategic Responses

| SOV | Assessment | Recommended Action |
|---|---|---|
| Below 25% | Low share — below competitive threshold | Increase content volume; generate more PR moments; consider UGC campaign |
| 25–40% | Competitive — in the conversation | Focus on quality and differentiation; aim to win on NSS while building SOV |
| Above 40% | Dominant — leading the conversation | Maintain quality; deepen community trust; protect position from challengers |

---

## Section 4: Conversation Theme Extraction

NSS and SOV are summary metrics. Theme extraction explains what is driving those numbers. Perform this analysis monthly alongside NSS calculation.

### Extracting Positive Themes

Positive themes reveal what the audience genuinely values about the brand — and what content to amplify.

Ask the following questions of the positive comment set:
- What do people mention most positively? (Product quality, staff, price, speed, convenience, trust)
- What do they compare favourably to competitors?
- What do they share or recommend to others?

These themes are content pillars hiding in plain sight. Use them as future content topics, social proof copy, and campaign angles. Refer to `10-content-pillars` when translating positive themes into a content framework.

### Extracting Negative Themes

Negative themes reveal operational and product problems that marketing cannot solve — and should not be asked to solve.

Ask the following questions of the negative comment set:
- What do people complain about most frequently?
- Is the complaint about the product, the service, the price, or the communication?
- Are complaints growing month on month or declining?

Recurring negative themes are product and service improvement briefs, not marketing problems. Escalate to operations when a theme appears 5 or more times in a month.

### Theme Extraction Process (Manual)

1. List all negative comments from the last 30 days in a spreadsheet
2. Group comments by theme using colour-coding (one colour per theme)
3. Count the number of instances of each theme
4. Rank themes by frequency (highest to lowest)
5. Identify the top 3 themes — these become "Priority Issues" in the monthly report

Apply the same process to positive comments to produce "Top Positive Themes".

This process takes approximately 20–30 minutes per platform once the comment export is complete.

---

## Section 5: Translating Sentiment Into Strategy

Sentiment data has no value unless it drives a decision (Funk, 2013). Every monthly sentiment report must conclude with at least one named strategic action. Use the following decision table to identify the correct response to each type of finding.

| Finding | Strategic Action |
|---|---|
| NSS declining 3 months in a row | Audit content quality and community management response times; identify whether the cause is content failure or service failure |
| One negative theme appearing 5+ times per month | Treat as a product/service improvement brief — escalate to the client's operations team; do not attempt to resolve through marketing |
| Competitor NSS significantly higher | Analyse their top-performing positive content for insight into what their audience values; apply learnings to content planning |
| SOV declining | Increase content frequency or launch a PR/UGC campaign to generate more brand-attributable mentions |
| Positive theme emerging organically | Build a content series around this theme immediately; document it as a content pillar in `10-content-pillars` |
| NSS spike after a campaign | Campaign worked — document the content type, timing, and audience response; replicate in future campaigns |
| NSS drop after a campaign | Campaign content may have missed the mark — review content, tone, and targeting; debrief with client before next campaign |
| SOV above 40% with declining NSS | Volume is high but quality is suffering; reduce content frequency and invest in quality; community management may be under-resourced |

Each action must have a named owner (consultant, client, operations) and a deadline. Data without an owner and a deadline does not produce change.

---

## Section 6: Monthly Sentiment Report Template

Produce this report monthly. Deliver it to the client alongside the written monthly report (`meta-reporting`) or as a section within the presentation deck (`deck-monthly-report`). Do not produce it as a standalone document unless the client has requested a dedicated sentiment briefing.

```
MONTHLY SENTIMENT REPORT — [Client Name] — [Month, Year]

NSS this month:      [score]   |   Last month: [score]   |   Trend: [improving / stable / declining]
SOV this month:      [%]       |   Competitor A: [%]     |   Competitor B: [%]

Top 3 positive themes this month:
  1. [Theme 1] — [X mentions]
  2. [Theme 2] — [X mentions]
  3. [Theme 3] — [X mentions]

Top 3 negative themes this month:
  1. [Theme 1] — [X mentions] — [Product / Service / Price / Fulfilment / Brand]
  2. [Theme 2] — [X mentions] — [Category]
  3. [Theme 3] — [X mentions] — [Category]

NSS 3-month trend:   Month 1: [score] → Month 2: [score] → Month 3: [score]
SOV 3-month trend:   Month 1: [%]     → Month 2: [%]     → Month 3: [%]

Recommended action this month:
  [One specific strategic action — what, who, by when]
```

Populate all fields from the NSS calculation, SOV calculation, and theme extraction outputs produced in this session. Do not leave fields blank; if data is unavailable, note the reason and the plan to collect it next month.

---

## Quality Criteria

- NSS formula is applied correctly and the result is expressed as a number (e.g., 52.1), never as a word (e.g., "healthy" or "good")
- NSS benchmarks used are specific to EA service businesses, not global averages
- SOV calculation includes at least 2 direct competitors and is recalculated monthly from fresh data
- Competitor selection for SOV excludes national or international brands when the client is a local SME
- Conversation theme extraction produces a ranked list of named themes with instance counts, not a general narrative observation
- The sentiment-to-strategy table maps specific findings to specific actions with named owners and deadlines
- Luganda and Swahili NLP limitations are explicitly noted and manual review of non-English comments is included in the recommended workflow
- The monthly sentiment report template is completed and included in every output — not offered as an optional add-on

---

## Key References

- Funk, T. (2013) *Advanced Social Media Marketing*. Apress.
- Schaffer, N. (2013) *Maximize Your Social*. Wiley.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.

---

## Related Skills

- `playbook-sentiment-listening` — operational setup: tools, keyword lists, dashboards, weekly monitoring routines (produces the raw data this skill analyses)
- `meta-reporting` — monthly written performance report; integrate the sentiment report template into the reporting section
- `meta-competitor-analysis` — full competitor benchmarking; SOV from this skill feeds into the competitive landscape section
- `playbook-crisis-communications` — invoke immediately when NSS falls below 0
- `10-content-pillars` — use positive theme extraction outputs to define or refresh content pillars

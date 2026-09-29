# Sentiment and Share-of-Voice Method

Merged from skills/meta-analytics-ops/meta-sentiment-analysis on 2026-09-29 at 8eacccb; preservation map: [meta-sentiment-analysis.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-sentiment-analysis.md)

## When to use this reference

Read this reference when the client already has, or has supplied, conversation data (comments, DMs, mentions, reviews, exports) and wants it scored: sentiment classification, a Net Sentiment Score (NSS), share of voice (SOV) against named competitors, ranked conversation themes, and a monthly sentiment report that ends in a named strategic action. Typical goals are brand health tracking, competitor benchmarking, campaign evaluation and a crisis response debrief.

This is the analytical half of listening. The listening programme in the parent [SKILL.md](../SKILL.md) and the operating routine in [listening-operations-playbook.md](listening-operations-playbook.md) produce the raw data; this reference says how to score, calculate and interpret it and how to turn the findings into decisions. The two are complementary, not alternatives.

## Inputs

Collect the following before producing any deliverable:

| Input | What to capture |
|---|---|
| Client business name and industry | For example "Kigali Fresh Bakery — food and beverage" |
| Country / city | Defaults to Uganda / Kampala if not specified |
| Primary goal (select one) | Brand health tracking / competitor benchmarking / campaign evaluation / crisis response debrief |
| Platforms to analyse (all that apply) | Facebook / Instagram / TikTok / YouTube / WhatsApp / X/Twitter / LinkedIn |
| Budget for sentiment tools (select one) | None (manual only) / USD 0–30 per month / USD 30–100 per month / enterprise |
| Languages spoken by the audience (all that apply) | English only / English + Luganda / English + Swahili / other (specify) |
| Competitors for share of voice | Up to 3 brand names, with social handles if known |
| Access to native platform analytics | Yes / no / partial |
| Dated dataset, query taxonomy and sampling method | From the listening log or dated platform exports; if absent, stop the affected calculation and mark it `not assessed` |

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| No tool budget, audience writes mainly in Luganda or Swahili, or fewer than 500 mentions per month across all platforms | Score manually (Step 1a) | Paying for automated scores that misread local-language content |
| English-language volume above 500 mentions per month per platform, or real-time monitoring required | Score automatically (Step 1b), still reviewing non-English content by hand | Manual workload that cannot keep up with volume |
| Most East African clients (mixed language, mixed volume) | Use the hybrid approach (Step 1c) and pool all scores in one sheet | NSS calculated on only the English part of the conversation |
| Any Luganda or Swahili comment in the dataset | Review it manually whatever tool is used | Inaccurate or inverted automated sentiment |
| Client is a local SME | Pick 2–3 direct competitors (same city/region, price tier and audience); exclude national or international brands | A scale-distorted SOV figure that no one can act on |
| NSS below 0 | Trigger [playbook-crisis-communications](../../../playbooks/playbook-crisis-communications/SKILL.md) immediately | A reputational threat reported as a routine number |
| A negative theme appears 5 or more times in a month | Escalate it to the client's operations team as a product or service improvement brief | Asking marketing to fix an operational problem |
| Any finding in the monthly report | End with at least one named strategic action with owner and deadline (Step 5) | Data that changes nothing |

## Procedure

### Step 1 — Choose the scoring method

Choose by tool budget and audience language mix. The hybrid approach is recommended for most East African clients.

**1a. Manual scoring (no tool budget).** Suitable when there is no tool budget, when the audience writes mainly in Luganda or Swahili, or when monthly mention volume is below 500 across all platforms.

1. Export or screenshot the last 100 comments, DMs and mentions per platform.
2. Enter each item into a shared Google Sheet or Airtable tracker.
3. Classify each item with the four-category scheme below.
4. Sub-classify every negative item with the five negative sub-categories.
5. Total the counts and calculate NSS (Step 2).

Allow 30–45 minutes per platform per month and budget that time into the monthly reporting cycle.

| Category | Code | Meaning |
|---|---|---|
| Positive | P | Affirming, recommending, praising, sharing with approval |
| Neutral | N | Informational, questions, factual statements with no clear valence |
| Negative | Neg | Complaint, criticism, disappointment, detraction |
| Mixed | M | Both positive and negative elements in one comment |

| Negative sub-category | Covers | Report label |
|---|---|---|
| Product complaint | Quality, features, availability | Product |
| Service complaint | Staff, communication, responsiveness | Service |
| Pricing objection | "Too expensive", unfavourable comparison with competitors | Price |
| Delivery / fulfilment issue | Late, wrong item, logistics failure | Fulfilment |
| Brand criticism | Values, ethics, reputation, public behaviour | Brand |

**1b. Automated scoring (tool budget available).** Suitable when English-language mention volume exceeds 500 per month per platform, or when real-time monitoring is required. Tool tiers recorded in the source (verify current plans, quotas and prices before stating; no register record):

| Budget | Tool | Notes |
|---|---|---|
| Free | MonkeyLearn (basic API) | 300 queries per month free; enough for small accounts |
| USD 0–30 per month | Mention (Starter) | English NLP; basic dashboard |
| USD 30–100 per month | Sprout Social / Hootsuite Insights | Integrated with scheduling; stronger reporting |
| Enterprise | Brandwatch | Full NLP suite; social listening plus analytics |

Language limitation, critical for East African clients: English NLP in the major tools is reliable for standard sentiment detection, but the source records Luganda and Swahili NLP as unreliable across all commercial tools as of 2025 — scores for non-English content can be wrong and sometimes inverted (verify before stating; no register record). Always review Luganda and Swahili comments by hand, whatever tool is used.

**1c. Hybrid approach (recommended for most EA clients).**

- Automate English-language monitoring on the high-volume platforms (Facebook, Instagram).
- Review by hand all WhatsApp conversations, Luganda and Swahili comments, and any active complaint thread.
- Feed manual scores into the same tracking sheet as automated scores so that NSS is calculated on the full dataset.

### Step 2 — Calculate the Net Sentiment Score

NSS expresses brand health as one number, calculated monthly and tracked as a trend (method after Funk, 2013).

```
NSS = (Positive mentions − Negative mentions) ÷ Total mentions × 100
```

Mixed comments are left out of the numerator; Neutral and Mixed comments count in the denominator (total mentions).

Worked example: 85 positive, 12 negative and 43 neutral = 140 total mentions. NSS = (85 − 12) ÷ 140 × 100 = **52.1**.

Express NSS as a number (for example 52.1), never as a word such as "good" or "positive".

NSS bands for East African service businesses (this method's bands; the weekly operating bands after Johnsen, 2024, are in [listening-operations-playbook.md](listening-operations-playbook.md) — state which set a report uses):

| Score | Assessment |
|---|---|
| +60 or above | Strong — advocates clearly outweigh detractors |
| +40 to +59 | Healthy — majority positive; address recurring negatives |
| +20 to +39 | Developing — positive and neutral in roughly equal parts; negatives need attention |
| 0 to +19 | Concerning — negatives approaching parity with positives; investigate root causes |
| Below 0 | Crisis territory — negatives outweigh positives; trigger playbook-crisis-communications |

Report NSS as a monthly trend, not a single snapshot; the trend line means more than any one score. Example: Month 1: +45 → Month 2: +48 → Month 3: +52 (improving, +7 over the quarter). A stable score in the +40s is a better signal than an improving score that started at +15, so always read the number against the trend and the starting baseline.

### Step 3 — Calculate share of voice

SOV is the client's portion of the total brand conversation in its competitive set (method after Schaffer, 2013).

```
SOV = Client brand mentions ÷ (Client + Competitor A + Competitor B + ...) × 100
```

Worked example: client 240 mentions, Competitor A 180, Competitor B 95. SOV = 240 ÷ (240 + 180 + 95) × 100 = **46.2%**.

Gathering SOV data in the EA market, in order of preference (automated tools are best but not always available):

1. Brandwatch or Mention — automated if budget allows; most accurate.
2. Google Alerts — free; captures news articles, blogs and indexed web content for brand names.
3. Meta Business Suite search — search competitor brand names in the Facebook search bar to find public posts mentioning them; count by hand.
4. Manual search — search brand names on Facebook, Instagram, TikTok and YouTube weekly; log counts in a spreadsheet.

Record raw mention counts weekly and sum them to a monthly total for the SOV calculation.

Competitor selection rules:

- Select 2–3 direct competitors: same city or region, same price tier, same target audience.
- Do not include national or international brands as competitors for local SMEs; the scale difference distorts the metric and produces an SOV figure that is not actionable.
- Review the competitor set every quarter; new entrants may need adding.

| SOV | Assessment | Recommended action |
|---|---|---|
| Below 25% | Low share — below competitive threshold | Increase content volume; generate more PR moments; consider a UGC campaign |
| 25–40% | Competitive — in the conversation | Focus on quality and differentiation; aim to win on NSS while building SOV |
| Above 40% | Dominant — leading the conversation | Maintain quality; deepen community trust; protect the position from challengers |

### Step 4 — Extract conversation themes

NSS and SOV are summary metrics; themes explain what drives them. Do this monthly alongside the NSS calculation.

Positive themes show what the audience values and what content to amplify. Ask of the positive set: what do people mention most positively (product quality, staff, price, speed, convenience, trust)? What do they compare favourably with competitors? What do they share or recommend to others? These themes are content pillars already in plain view: use them as content topics, social-proof copy and campaign angles, and take them into [10-content-pillars](../../../pipeline/10-content-pillars/SKILL.md) when building a content framework.

Negative themes show operational and product problems that marketing cannot solve and should not be asked to solve. Ask of the negative set: what do people complain about most often? Is the complaint about the product, the service, the price or the communication? Are complaints growing or falling month on month? Recurring negative themes are product and service improvement briefs; escalate to operations when a theme appears 5 or more times in a month.

Manual extraction process:

1. List all negative comments from the last 30 days in a spreadsheet.
2. Group comments by theme with colour-coding (one colour per theme).
3. Count the instances of each theme.
4. Rank themes by frequency, highest first.
5. Name the top 3 themes as "Priority Issues" in the monthly report.

Apply the same process to positive comments to produce "Top Positive Themes". Allow roughly 20–30 minutes per platform once the comment export is complete.

### Step 5 — Translate sentiment into strategy

Sentiment data has no value unless it drives a decision (Funk, 2013). Every monthly sentiment report must end with at least one named strategic action.

| Finding | Strategic action |
|---|---|
| NSS declining 3 months in a row | Audit content quality and community-management response times; establish whether the cause is content failure or service failure |
| One negative theme appearing 5+ times per month | Treat it as a product/service improvement brief; escalate to the client's operations team; do not try to resolve it through marketing |
| Competitor NSS significantly higher | Analyse their top-performing positive content for what their audience values; apply the learning to content planning |
| SOV declining | Increase content frequency or launch a PR/UGC campaign to generate more brand-attributable mentions |
| Positive theme emerging organically | Build a content series around it immediately; document it as a content pillar in 10-content-pillars |
| NSS spike after a campaign | The campaign worked; document content type, timing and audience response; replicate in future campaigns |
| NSS drop after a campaign | The content may have missed the mark; review content, tone and targeting; debrief with the client before the next campaign |
| SOV above 40% with declining NSS | Volume is high but quality is suffering; reduce frequency and invest in quality; community management may be under-resourced |

Each action needs a named owner (consultant, client or operations) and a deadline. Data without an owner and a deadline does not produce change.

## Template — monthly sentiment report

Produce monthly. Deliver it with the written monthly report from [meta-reporting](../../meta-reporting/SKILL.md), or include it in the evidence handoff to the design engine (design-system-skills) when a presentation is commissioned. Do not claim a local deck route, and do not produce it as a standalone document unless the client has asked for a dedicated sentiment briefing.

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

Populate every field from the NSS, SOV and theme outputs of the same session. Do not leave fields blank; if data is unavailable, state the reason and the plan to collect it next month.

## Onward use

- SOV from this method feeds the competitive landscape section of [meta-competitor-analysis](../../meta-competitor-analysis/SKILL.md).
- The monthly sentiment report sits inside the reporting section of [meta-reporting](../../meta-reporting/SKILL.md).
- NSS below 0 invokes [playbook-crisis-communications](../../../playbooks/playbook-crisis-communications/SKILL.md) immediately.
- Positive themes define or refresh [10-content-pillars](../../../pipeline/10-content-pillars/SKILL.md).

## Checklist

- [ ] NSS formula applied correctly and the result expressed as a number (for example 52.1), never as a word such as "healthy" or "good".
- [ ] NSS bands used are the East African service-business bands (or the stated operating bands), not global averages.
- [ ] SOV includes at least 2 direct competitors and is recalculated monthly from fresh data.
- [ ] Competitor set excludes national or international brands when the client is a local SME.
- [ ] Theme extraction produces a ranked list of named themes with instance counts, not a general narrative.
- [ ] The sentiment-to-strategy table maps specific findings to specific actions with named owners and deadlines.
- [ ] Luganda and Swahili NLP limits are stated and manual review of non-English comments is in the workflow.
- [ ] The monthly sentiment report template is completed in every output, not offered as an optional extra.

## Sources

- Funk, T. (2013) *Advanced Social Media Marketing*. Apress.
- Schaffer, N. (2013) *Maximize Your Social*. Wiley.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.

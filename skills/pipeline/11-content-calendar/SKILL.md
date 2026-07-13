---
name: 11-content-calendar
description: "Use when scheduling approved pillars and campaigns across a 90-day period. Produces 90-day content calendar with owners and production cues; use `10-content-pillars` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# 90-Day Content Calendar Generator

Produce a 90-day master content calendar across three monthly tables. Each table covers one calendar month. Apply the `east-african-english` skill for tone throughout. Do not generate the calendar until all Required Input has been confirmed.


<!-- dual-compat-start -->
## Use When

- Use this skill for scheduling approved pillars and campaigns across a 90-day period.
- Confirm that `10-content-pillars` is not the closer route before proceeding.

## Do Not Use When

- Use `10-content-pillars` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Approved pillars, channel plan, campaign dates, capacity and verified observances | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| 90-day content calendar with owners and production cues | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified 90-day content calendar with owners and production cues. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Approved pillars, channel plan, campaign dates, capacity and verified observances is current and attributable | Produce the full 90-day content calendar with owners and production cues and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `10-content-pillars` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `10-content-pillars` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the 90-day content calendar with owners and production cues, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the 90-day content calendar with owners and production cues without approved pillars. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `10-content-pillars` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified approved pillars, the skill produces a 90-day content calendar with owners and production cues with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`10-content-pillars`](../10-content-pillars/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Ask for the following before generating:

- **Client name** — trading name of the business
- **Platforms in scope** — list all active platforms (default: Facebook, Instagram, WhatsApp)
- **Content pillars** — names and percentages from `10-content-pillars`
- **Posting frequency per platform** — how many times per week per platform (e.g., Facebook: 5×/week, Instagram: 3×/week)
- **Campaign dates** — any confirmed campaign windows from `09-campaign-strategy` (name and date range)
- **3 high-revenue seasons** — the three periods in the year when this client's business earns most or has highest demand
- **Calendar start date** — the Monday the calendar begins
- **Country/city** — defaults to Kampala, Uganda

---

## Calendar Table Format

Use this column structure for every row. Produce one row per content piece per week (summarised by week, not by individual day — daily scheduling happens in the weekly workflow):

| Week | Date Range | Platform | Content Type | Pillar | Topic / Headline | 2-Sentence Content Brief | Notes |
|---|---|---|---|---|---|---|---|

**Column definitions:**
- **Week** — W1, W2, W3 … W13
- **Date Range** — e.g., 24–28 Mar 2026
- **Platform** — Facebook / Instagram / WhatsApp / LinkedIn / TikTok / X (use one row per platform per week per pillar)
- **Content Type** — post, carousel, reel, story, broadcast, article, video (choose the dominant format for that week's theme)
- **Pillar** — the content pillar name from `10-content-pillars`
- **Topic / Headline** — specific working title or topic (not generic — "How we helped a Kampala salon double bookings" not "Case study")
- **2-Sentence Content Brief** — sentence 1: what the post covers; sentence 2: what the audience should feel or do after seeing it
- **Notes** — flag observances, campaign windows, cross-platform tie-ins, or anything requiring advance preparation

---

## Section 1: Ugandan and East African Observances

Include the following observances in the calendar. When an observance falls in the 90-day window, add a content row for the relevant platform(s) in the week it falls. Adjust tone and content brief to suit the occasion.

**Fixed-date observances:**
- 1 January — New Year's Day
- 14 February — Valentine's Day (relevant for consumer brands; use with restraint for B2B)
- 8 March — International Women's Day (IWD) — amplify women's voices; do not reduce to a single post if the client works in sectors affecting women
- 3 June — Uganda Martyrs Day — tone: solemn; for most brands, acknowledge rather than promote
- 9 June — Uganda Heroes Day — tone: celebratory, patriotic
- 9 October — Uganda Independence Day — tone: pride, national identity; strong for Ugandan consumer brands
- 25 December — Christmas Day

**Variable-date observances (check current year):**
- **Eid al-Fitr** — end of Ramadan; date varies by lunar calendar — confirm the year's date before generating
- **Eid al-Adha** — approximately 70 days after Eid al-Fitr; confirm the year's date before generating
- **Ramadan** — the full month of fasting; note the start and end weeks in the calendar. For Muslim-majority or mixed audiences, shift content tone during Ramadan: reduce overt promotional content, increase value-led and community content, avoid posting food imagery during daylight hours if relevant to the brand

**Instruction:** When any of these observances falls within the 90-day window, insert a dedicated content row marked [OBSERVANCE] in the Notes column. Write a brief that is appropriate to the occasion — do not insert a generic post and claim it is culturally relevant.

---

## Section 2: International Awareness Days

The following 20 awareness days are commonly relevant across industries. Select 6–10 most relevant for the client's industry and insert them into the calendar. State which ones were selected and why, before producing the tables.

| Awareness Day | Date | Relevant for |
|---|---|---|
| World Health Day | 7 April | Healthcare, wellness, fitness, food |
| Earth Day | 22 April | Environment, agriculture, sustainability, FMCG |
| World Press Freedom Day | 3 May | Media, NGOs, public sector |
| Africa Day | 25 May | Pan-African brands, culture, education |
| World Environment Day | 5 June | Agriculture, construction, hospitality |
| World Food Safety Day | 7 June | Food and beverage, hospitality, retail |
| World Youth Skills Day | 15 July | Education, training, NGOs, employment |
| International Youth Day | 12 August | Education, retail, consumer brands targeting youth |
| World Literacy Day | 8 September | Education, publishing, NGOs |
| World Mental Health Day | 10 October | Healthcare, wellness, HR, corporate |
| World Food Day | 16 October | Agriculture, food and beverage, retail |
| World Savings Day | 31 October | Financial services, SACCOs, microfinance |
| World Children's Day | 20 November | Education, healthcare, retail, FMCG |
| World AIDS Day | 1 December | Healthcare, NGOs, public sector |
| International Day of Persons with Disabilities | 3 December | NGOs, healthcare, inclusive employers |
| World Entrepreneurship Day | 16 November | Business services, finance, training |
| International Day of Education | 24 January | Education, NGOs, government |
| World Tourism Day | 27 September | Hospitality, tourism, transport |
| World Photography Day | 19 August | Any brand using visual content |
| World Customer Service Week | First week of October | Retail, financial services, hospitality, telecoms |

---

## Section 3: Industry Seasonal Hooks

Ask the consultant: "Name the three periods in the year when your client's business earns most revenue or has highest customer demand. Give each a name and an approximate date range."

Once confirmed, mark those three windows in the calendar as [HIGH SEASON] in the Notes column and increase posting frequency by 20–30% in those weeks. Produce a brief for at least two seasonal-themed posts per platform during each high-season window.

---

## Section 4: Campaign Windows

If campaign dates have been provided from `09-campaign-strategy`, reserve those weeks as [CAMPAIGN] in the calendar. Reduce standard pillar content in campaign weeks to avoid audience confusion — allow the campaign to lead. Suggest 1 supporting organic post per platform per campaign week that reinforces the campaign message without duplicating paid content.

---

## Section 5: Cross-Platform Consistency

Show how the same weekly theme appears across platforms in the same week. For each week, identify the core theme and show a brief cross-platform content plan. Use this format under each monthly table:

**Week [N] Cross-Platform Theme: [Theme title]**
- Facebook: [Post format and brief — Monday or Tuesday]
- Instagram: [Post format and brief — Wednesday or Thursday]
- WhatsApp: [Broadcast brief — Friday afternoon]
- LinkedIn *(if in scope)*: [Article or post brief — Monday]
- TikTok *(if in scope)*: [Reel brief — any day with high engagement]

---

## Section 6: Weekly Rhythm Template

Include this repeating template at the start of the calendar, before Month 1. The team uses this as the default pattern each week unless a campaign or observance requires adjustment.

**Standard Weekly Rhythm — [Client Name]**

| Day | Platform | Content Type | Pillar (rotate) |
|---|---|---|---|
| Monday | Facebook | Value post or article share | [Pillar A] |
| Tuesday | Instagram | Carousel or single image | [Pillar B] |
| Wednesday | Facebook + Instagram | Repost or UGC or community content | [Pillar C] |
| Thursday | LinkedIn *(if in scope)* | Thought leadership post | [Pillar A or B] |
| Friday | WhatsApp broadcast | Weekly update or offer reminder | [Promotional pillar] |
| Friday | Instagram Stories | Behind-the-scenes or poll | [Pillar C] |
| Weekend | TikTok *(if in scope)* | Entertainment or trend content | [Pillar B or C] |

Adjust the template based on the client's platforms and posting frequency.

---

## Three Monthly Tables

Produce Month 1, Month 2, and Month 3 tables in sequence. Each table covers approximately 4–5 weeks. Before each table, write a one-paragraph overview of the month's strategic focus: what the main themes are, which observances or campaigns fall in this month, and what the tone should be.

Apply the 10-4-1 rule (Bodnar and Cohen, 2012) across each month: check that approximately 10 out of every 15 rows are value or sharing content, 4 are original brand content, and 1 is promotional. Note the ratio at the end of each monthly table.

---

## Consultant Guidance Note

> **This calendar is a planning tool — not a locked schedule.** Review and adjust every Friday for the following week. Check: (1) Are there any breaking news or local events that require a reactive post? (2) Did last week's top-performing post suggest a follow-up? (3) Are approval timelines on track for the week ahead? Adjust the calendar before beginning content production for the next week. Major changes to monthly themes should be flagged to the client before execution begins.

---

## Quality Criteria

- All three monthly tables are produced; no month is skipped or abbreviated
- Every row in the calendar has a specific topic or headline — no row contains a placeholder such as "TBC" or "educational post"
- Ugandan and East African observances falling within the 90-day window are identified and included with appropriate tone guidance
- 6–10 international awareness days are selected with a stated reason for their relevance to the client's industry
- Campaign windows from `09-campaign-strategy` are marked and content in those weeks defers to the campaign
- Cross-platform content for each week shows a clear thematic connection across platforms without being identical copy
- The 10-4-1 ratio is checked per month and the result is noted — the calendar must not be predominantly promotional
- British English spelling is used throughout; dates in day-month-year format (e.g., 7 April 2026)

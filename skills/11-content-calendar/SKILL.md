---
name: 11-content-calendar
description: Generates a 90-day master content calendar (month-by-month, week-by-week) showing what gets posted, on which platform, and in which week — including Ugandan and East African observances, international awareness days, and campaign windows. Invoke after completing 10-content-pillars and before beginning content production.
---
# 90-Day Content Calendar Generator

Produce a 90-day master content calendar across three monthly tables. Each table covers one calendar month. Apply the `east-african-english` skill for tone throughout. Do not generate the calendar until all Required Input has been confirmed.

<!-- dual-compat:start -->
## Use when
- Generates a 90-day master content calendar (month-by-month, week-by-week) showing what gets posted, on which platform, and in which week — including Ugandan and East African observances, international awareness days, and campaign windows. Invoke after completing 10-content-pillars and before beginning content production.
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
- A structured onboarding, strategy, or planning document in markdown, ready to hand off to the next skill in the workflow.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

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

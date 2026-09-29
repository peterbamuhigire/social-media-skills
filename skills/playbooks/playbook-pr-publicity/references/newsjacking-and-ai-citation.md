# Newsjacking and AI-Search Citation

Merged from skills/playbooks/playbook-geo-newsjacking on 2026-09-29 at ce3299a; preservation map: [playbook-geo-newsjacking.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/playbook-geo-newsjacking.md)

## When to use this reference

Read this reference when the client wants rapid-response expert commentary on breaking news: the alert set-up that spots a story, the triage that decides whether to respond, the production prompt, the article structure that helps AI search features cite it, the distribution sequence and an East African trigger calendar. The parent [SKILL.md](../SKILL.md) owns planned publicity (releases, publicity kit, query letters, calendar, tracking); this reference is its real-time layer. The system is sized for a two-person marketing team or one account manager working with AI assistance.

Drafting an article or broadcast does not authorise publishing or sending it. Where a story involves harm, uncertainty or political sensitivity, stop and obtain editorial and risk approval before anything is drafted for release.

Evidence status. The GEO rationales below (freshness, question structure, FAQ yield, page speed) are the source playbook's claims, attributed to Roth and neuroflash Team (2024/2025). Google's own guidance says core SEO remains relevant and that no special AI markup, artificial chunking or `llms.txt` is required (register GOOGLE-AI-SEARCH-GUIDE-2026, verified 2026-09-08; Google Search only, not other AI services). Treat the checklist as a house editorial standard, not as a guaranteed citation mechanism. Tool settings, free tiers, character limits and institutional meeting schedules have no register record: verify before stating.

## Inputs

| # | Input | Notes |
|---|---|---|
| 1 | Client business name and industry | |
| 2 | Country and city | Default Uganda / Kampala |
| 3 | Primary goal | Thought leadership, organic search traffic, lead generation or brand awareness |
| 4 | Target audience | Who reads the content and what decisions they make |
| 5 | Expertise area | The specific domain where the client can comment with genuine authority, for example East African tax law, agri-finance, logistics |
| 6 | Publishing platform | Where the client publishes long-form content now: WordPress, LinkedIn Articles, Medium, or none yet |

## Why newsjacking works

**Core mechanism.** Newsjacking connects a brand's expertise to a breaking story and publishes quickly enough to be indexed before most competitors. The window is about 2–6 hours after a major story breaks. David Meerman Scott, who coined the term, observed that journalists and audiences search heavily in the first few hours; brands that publish credible expert commentary in that window inherit the attention, and those publishing the next day find it closed.

**The GEO-era argument (source claim).** In traditional search, newsjacking content ranked for a few days and decayed. The source argues that GEO-optimised newsjacking content can be cited in AI search summaries for weeks, sometimes permanently, because:

- **Freshness:** recently published or updated content is surfaced preferentially, and a newsjacking article carries a strong freshness signal from its publication date.
- **Conversational structure:** newsjacking content naturally takes the question-and-answer shape that AI search extracts; "What does the Bank of Uganda rate decision mean for SMEs?" is the kind of query that generates a citation.
- **EEAT:** expert commentary on a real, current, attributable event earns Experience, Expertise, Authoritativeness and Trustworthiness signals.

Roth and neuroflash Team (2024/2025) summarise it as AI search prioritising content that is fresh, structured as expert answers and attributed to credible named authors. Qualify this with the register note above before presenting it to a client.

**East African advantage.** Most Ugandan and East African businesses do not produce rapid-response content, so the competitive window is wider than in the UK or US, where hundreds of publishers respond within minutes. A Ugandan financial services firm that publishes expert commentary on a Bank of Uganda rate decision within two hours faces little competition for that query (source judgement; check the live results for the client's query).

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| The event involves harm, uncertainty or political sensitivity | Pause; require editorial and risk approval before drafting for release | Exploiting a crisis or spreading falsehoods |
| An alert fires | Apply the four-question triage (Procedure 2); produce only if all four pass | Commentary without expertise, relevance or a citable source |
| Priority 1 trigger: Bank of Uganda or Central Bank of Kenya rate decision, major URA or KRA tax change, direct regulatory action on the client's sector | Respond within 2 hours | Missing the indexing window |
| Priority 2 trigger: UBOS economic data, EAC trade announcement, major East African corporate news | Respond within 6 hours | Late, low-value commentary |
| Priority 3 trigger: platform updates, international macro events with indirect East African relevance, industry conference outcomes | Respond within 24 hours | Spending rapid-response effort on low-stakes stories |
| A WhatsApp contact has not opted in to the client's messages | Do not broadcast to them | Unsolicited messaging; WhatsApp policy breach (WHATSAPP-BUSINESS-POLICY) |
| Commentary would go beyond the client's documented expertise | Cut the claim or hand it to a qualified author | Unsupported expert claims |

## Procedure

### 1. Alert infrastructure (one-time set-up, about 45 minutes)

**Google Alerts.** Log in to Google Alerts with the client's or agency's Google account and create an alert per trigger category. Settings per alert (verify the current option names): frequency "As it happens" (not a daily digest); source "News"; language English; region the client's primary market.

| Category | Alert terms |
|---|---|
| Regulatory (Uganda) | "Bank of Uganda", "Uganda Revenue Authority", "NITA-U", "Financial Intelligence Authority Uganda" |
| Regulatory (Kenya) | "Central Bank of Kenya", "Kenya Revenue Authority", "Communications Authority Kenya" |
| Regional | "East African Community trade", "EAC", "East Africa investment" |
| Industry-specific | The client's top three industry terms (ask at intake) |
| Competitor | Up to three competitor names |

**IFTTT applet.** Route alerts to a dedicated Slack channel through IFTTT's free tier (verify that the free tier and the Google Alerts trigger are still offered; this playbook assumes zero spend):

1. Create a free IFTTT account.
2. Create an applet: "If Google Alert fires → then post to Slack channel".
3. Name the channel `#news-triggers` or equivalent.
4. Post the alert headline, source URL and timestamp.

If the client does not use Slack, send the alerts to a dedicated address (for example alerts@clientdomain.com) that the account manager monitors.

### 2. Triage when an alert fires

Answer four questions:

1. Does the story affect the client's target audience directly?
2. Can the client comment with genuine expertise, not just opinion?
3. Is the story from a credible, citable source?
4. Has the client commented on a similar story in the last 30 days? If yes, proceed only if this story is materially different.

If all four pass, start production immediately.

### 3. Production (target 20–40 minutes)

Complete the master prompt and paste it into the AI assistant with the breaking news appended.

```
You are a digital marketing expert writing for [CLIENT NAME], a [INDUSTRY]
business in [COUNTRY]. A breaking news story has just been published:

[PASTE NEWS HEADLINE AND FIRST 2–3 PARAGRAPHS HERE]

Write a 600-word expert commentary article that:

1. Opens with a 50-word direct answer to the question:
   "What does this news mean for [TARGET AUDIENCE] in [COUNTRY]?"
   — this must be the first paragraph, no preamble.

2. Explains what the news means for [TARGET AUDIENCE] in [COUNTRY] in
   plain, specific terms — no generalities.

3. Provides [CLIENT NAME]'s perspective, drawing on their expertise in
   [SPECIFIC EXPERTISE AREA]. Include at least one concrete example,
   data point, or case reference.

4. Closes with a clear, single action recommendation for the reader.

5. Uses British English throughout.

6. Avoids marketing language ("world-class", "cutting-edge", "solutions",
   "leverage") — the tone is expert and factual, not promotional.

7. Includes at least two H2 headings phrased as questions
   (e.g. "What does this mean for Ugandan SMEs?").

8. Ends with a FAQ section containing exactly three questions and answers.
   Each question must be phrased as a reader would type it into a search engine.

9. The byline is: [AUTHOR NAME], [TITLE], [COMPANY NAME].

Cite the original news source at the end in this format:
Source: [Publication name] ([Date]). "[Article headline]". [URL]
```

Customise `[SPECIFIC EXPERTISE AREA]` by use case:

| Client and trigger | Expertise-area text |
|---|---|
| Financial services, Bank of Uganda rate decision | "SME lending, mobile money credit products, and the cost of borrowing for Ugandan businesses" |
| Technology, NITA-U regulation | "digital infrastructure, data compliance for Ugandan businesses, and practical implementation of technology regulation" |
| Logistics, EAC trade announcement | "cross-border freight, last-mile delivery in East Africa, and the operational impact of trade corridor policy on ground logistics" |

The AI draft is a starting point: a named expert checks every fact and claim before publication.

### 4. GEO optimisation checklist (every article, before publishing)

This applies the standards of [seo-geo-optimisation](../../../seo-discovery/seo-geo-optimisation/SKILL.md) at rapid-response speed. Rationales are the source's claims (see Evidence status).

- [ ] **Direct answer in paragraph 1** — the first 50 words answer the core reader question; AI search tends to extract the first substantive paragraph as the snippet.
- [ ] **Author name and credentials visible** — full name, title and company in the byline or author box; anonymous content earns no EEAT signal.
- [ ] **Original news source cited with date** — cross-checkable sources raise citation probability.
- [ ] **H2 headings phrased as questions** — at least two, matching conversational queries.
- [ ] **FAQ of three questions at the end** — each phrased as a reader would type it; the source rates this the highest-yield element per unit of effort.
- [ ] **Publication date visible** — "Published [date]" in the header or metadata; freshness is treated as a live signal.
- [ ] **Page load under 3 seconds** — test with PageSpeed Insights before distributing (threshold is the source's; verify).
- [ ] **500–800 words** — substantive but quick to index and read; do not pad.

### 5. Distribution sequence (target: all five steps within 60 minutes of publishing)

Publish the long-form article on the client's website or blog first so it is the canonical source, then distribute.

| Step | Timing | Channel | Actions |
|---|---|---|---|
| 1 | Publish + 5 min | LinkedIn | Post the article's first three paragraphs plus "Full article: [link]"; tag organisations or people in the story where appropriate; 3–5 hashtags, industry plus geography (for example `#UgandaBusiness`, `#EastAfrica`, `#FinancialServices`); post from the company page and ask the author to share from their personal profile within 30 minutes |
| 2 | Publish + 15 min | Facebook | 100–120 words: headline, the single most useful insight, link; pose it as a question ("The Bank of Uganda has cut rates. What does this mean for your loan repayments? Here is our take: [link]"); post to the Page and share to relevant Groups the client belongs to. Facebook access in Uganda is unstable: check status at the campaign date (UG-FACEBOOK-ACCESS-2026) |
| 3 | Publish + 30 min | Instagram | Pull the most quotable statistic or insight; make a branded quote card (for example in Canva); caption of one-sentence context plus "Full analysis in bio link"; update the bio link; add to Stories with a link sticker |
| 4 | Publish + 45 min | WhatsApp broadcast | Opted-in contacts only, never cold contacts (WHATSAPP-BUSINESS-POLICY); template below; keep the text before the link under 200 characters because previews truncate and the hook must be in line one (preview length: verify) |
| 5 | Publish + 60 min | X | The key insight as a single post (source gives a 280-character limit; verify) with the article link; tag the regulator or outlet if active on X. In Uganda, X is used mainly by journalists, opinion leaders and public-sector officials, and expert, non-promotional insight performs well with them (source observation) |

WhatsApp broadcast template:

```
Seen this? [NEWS HEADLINE — one sentence summary]

Here is what it means for [INDUSTRY] businesses in [COUNTRY]: [LINK]

— [CLIENT NAME] team
```

The source cites Chaffey and Ellis-Chadwick's (2022) RACE framework as the basis for this sequencing.

### 6. East African trigger calendar

At the start of each quarter, add scheduled triggers to the client's editorial calendar and set the reactive watch list. Meeting frequencies are the source's; confirm each institution's published calendar before scheduling.

| Recurring trigger | Frequency (verify) | Lead institution |
|---|---|---|
| Bank of Uganda Monetary Policy Committee | Every 2 months (Feb, Apr, Jun, Aug, Oct, Dec) | Bank of Uganda |
| Central Bank of Kenya MPC | Every 2 months | Central Bank of Kenya |
| Uganda Revenue Authority budget circulars | Quarterly, plus annual budget (June) | URA |
| Kenya Revenue Authority tax notices | As issued; peaks January and June | KRA |
| Tanzania Revenue Authority announcements | Quarterly | TRA |
| Uganda Bureau of Statistics economic releases | Monthly (CPI); quarterly (GDP) | UBOS |
| EAC Council of Ministers meetings | Twice yearly | East African Community |
| NITA-U regulatory notices | As issued | NITA-U |
| Meta algorithm updates | As announced | Meta Newsroom |
| WhatsApp Business policy changes | As announced | WhatsApp Business Blog |

Reactive triggers (monitor continuously):

- Major East African corporate announcements: acquisitions, IPOs, regulatory sanctions.
- Global platform changes with East African relevance, such as TikTok regulatory actions or LinkedIn algorithm updates.
- Macroeconomic events: IMF or World Bank assessments of East African economies; dollar exchange-rate movements above 5% in a week.
- Any government white paper or gazette notice affecting the client's sector.

Classify each trigger Priority 1, 2 or 3 using the decision rules above.

## Release checklist

1. The alert set-up names real alert terms for the client's industry and market; no generic placeholders remain at delivery.
2. The production prompt is customised with the client's name, industry, audience, expertise area and country before handover.
3. Every article passes all eight GEO checklist items before publication.
4. Distribution follows the five steps and finishes within 60 minutes; any deviation is noted and justified.
5. The trigger calendar holds at least six scheduled triggers for the coming quarter, with dates, institutions and priority classes.
6. WhatsApp broadcasts go only to opted-in contacts, and this is recorded in the client's workflow notes.
7. Commentary stays within the client's documented expertise.
8. Every article is bylined with the author's full name and title; nothing anonymous is published.
9. Sensitive-event stories carry a recorded editorial and risk approval.

## Related skills

- [seo-geo-optimisation](../../../seo-discovery/seo-geo-optimisation/SKILL.md) — the full GEO content strategy; newsjacking is its rapid-response execution layer.
- [blog-writer](../../../content-writing/blog-writer/SKILL.md) — planned long-form content that complements reactive articles.
- [playbook-content-production](../../playbook-content-production/SKILL.md) — the wider content workflow and scheduling system newsjacking feeds into.
- [meta-social-listening](../../../meta-analytics-ops/meta-social-listening/SKILL.md) — broader monitoring that surfaces triggers beyond Google Alerts.
- [pr-media-integration](pr-media-integration.md) — pitching the same story to journalists and amplifying resulting coverage.

## Sources

- Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing Teams*. neuroflash. (GEO freshness signals; AI search citation dynamics.)
- Chaffey, D. and Ellis-Chadwick, F. (2022) *Digital Marketing: Strategy, Implementation and Practice*. 8th edn. Harlow: Pearson. (RACE framework applied to distribution sequencing.)
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley. (Content publication and distribution principles.)
- David Meerman Scott is credited with coining "newsjacking" (attribution as given in the source; no work cited).
- Register: GOOGLE-AI-SEARCH-GUIDE-2026, UG-FACEBOOK-ACCESS-2026, WHATSAPP-BUSINESS-POLICY in [source-register.json](../../../../docs/source-registers/source-register.json).

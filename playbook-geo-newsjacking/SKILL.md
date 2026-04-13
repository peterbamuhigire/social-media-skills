---
name: playbook-geo-newsjacking
description: >
  Generates an operational newsjacking playbook that combines Generative Engine
  Optimisation (GEO) with real-time content production — setting up automated
  news alerts, producing GEO-optimised expert commentary within minutes of a
  breaking story, and distributing across channels to capture AI search citation
  and organic social traffic simultaneously. Invoke when a client wants to build
  a thought-leadership content system, when a client is underrepresented in AI
  search results, when a regulatory or market event is approaching, or when a
  rapid-response content capability needs to be built from scratch.
---
# Playbook: GEO Newsjacking

<!-- dual-compat:start -->
## Use when
- Generates an operational newsjacking playbook that combines Generative Engine Optimisation (GEO) with real-time content production — setting up automated news alerts, producing GEO-optimised expert commentary within minutes of a breaking story, and distributing across channels to capture AI search citation and organic social traffic simultaneously. Invoke when a client wants to build a thought-leadership content system, when a client is underrepresented in AI search results, when a regulatory or market event is approaching, or when a rapid-response content capability needs to be built from scratch.
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
- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Purpose

Produce a complete newsjacking system: alert infrastructure, production
workflows, GEO-optimised article structure, distribution sequence, and an
EA-specific trigger calendar. Every component is designed for a two-person
marketing team or a solo account manager with AI assistance.

> Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing
> Teams*. neuroflash. [GEO and AI search citation dynamics cited below]
> Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*.
> Pearson. [RACE framework for content distribution sequencing]

---

## Required Input

Before generating any deliverable, ask for:

1. **Client business name** and industry
2. **Country and city** (default: Uganda / Kampala)
3. **Primary goal** — thought leadership, organic search traffic, lead
   generation, or brand awareness
4. **Target audience** — who reads the content and what decisions do they make?
5. **Expertise area** — the specific domain on which the client can comment
   with genuine authority (e.g. East African tax law, agri-finance, logistics)
6. **Publishing platform** — where does the client currently publish long-form
   content? (WordPress, LinkedIn Articles, Medium, or none yet)

---

## Section 1 — What Newsjacking Is and Why It Works

### The Core Mechanism

Newsjacking is the practice of connecting a brand's expertise to a breaking
news story, published quickly enough to be indexed before most competitors.
The window is 2–6 hours after a major story breaks.

David Meerman Scott, who coined the term, observed that search journalists and
audiences flood a story in the first few hours. Brands that publish credible
expert commentary in that window inherit the traffic. Those that publish the
next day find the window closed.

### Why Newsjacking Is More Powerful in the GEO Era

In traditional search, newsjacking content ranked for a few days then decayed.
In the GEO era, newsjacking content that is also GEO-optimised gets cited in
AI search summaries for weeks — and sometimes permanently — because:

- **AI search engines favour freshness:** Content updated or published recently
  is surfaced preferentially. A newsjacking article carries a strong freshness
  signal from its publication date.
- **Conversational structure:** Newsjacking content naturally produces the
  question-and-answer structure that AI search engines extract for citation.
  "What does the Bank of Uganda rate decision mean for SMEs?" is precisely the
  query format that generates AI citation.
- **EEAT signals:** Expert commentary on topical events earns Experience,
  Expertise, Authoritativeness, and Trustworthiness signals organically.
  The author is commenting on something real, current, and attributable.

Source: Roth and neuroflash Team (2024/2025) — AI search engines prioritise
content that is fresh, structured as expert answers, and attributed to credible
named authors.

### EA Market Advantage

Most Ugandan and East African businesses do not produce rapid-response content.
The competitive window for newsjacking in the EA market is wider than in the
UK or US, where hundreds of publishers respond to the same story within minutes.
A Ugandan financial services firm that publishes an expert commentary on a Bank
of Uganda rate decision within two hours faces minimal competition for that
search query.

---

## Section 2 — The IFTTT + AI Automated Alert Workflow

### Infrastructure Setup (One-Time, 45 Minutes)

**Step 1 — Google Alerts**

Set up Google Alerts for each of the following trigger categories. Log in to
alerts.google.com with the client's or agency's Google account.

For each alert:
- Set frequency to "As it happens" (not daily digest)
- Set source to "News"
- Set language to English
- Set region to the client's primary market

Suggested alert terms for EA clients:

| Category | Alert terms to set |
|---|---|
| Regulatory (Uganda) | "Bank of Uganda", "Uganda Revenue Authority", "NITA-U", "Financial Intelligence Authority Uganda" |
| Regulatory (Kenya) | "Central Bank of Kenya", "Kenya Revenue Authority", "Communications Authority Kenya" |
| Regional | "East African Community trade", "EAC", "East Africa investment" |
| Industry-specific | [Insert client's top 3 industry terms — ask at intake] |
| Competitor | [Insert up to 3 competitor names] |

**Step 2 — IFTTT Applet**

Connect Google Alerts to a dedicated Slack channel using IFTTT (free tier):

1. Create a free IFTTT account at ifttt.com.
2. Create a new applet: "If Google Alert fires → Then post to Slack channel."
3. Name the Slack channel `#news-triggers` or equivalent.
4. Set the IFTTT applet to post the alert headline, source URL, and timestamp.

Alternative if the client does not use Slack: direct the Google Alert to a
dedicated email address (e.g. alerts@clientdomain.com) that the account
manager monitors.

**Step 3 — Triage Rule**

Not every alert warrants a newsjacking article. Apply this triage filter when
an alert fires:

- Does the story affect the client's target audience directly? (Yes = proceed)
- Can the client comment with genuine expertise, not just opinion? (Yes = proceed)
- Is the story from a credible, citable source? (Yes = proceed)
- Has the client commented on a similar story in the last 30 days? (If yes,
  proceed only if this story is materially different)

If all four answers are yes, activate the production workflow immediately.

**Step 4 — Production (Target: 20–40 Minutes)**

Run the Newsjacking Production Prompt (Section 3) in Claude or ChatGPT.
Apply the GEO Optimisation Checklist (Section 4). Publish. Distribute.

**Step 5 — Distribution (Target: 15 Minutes)**

Follow the distribution sequence in Section 5 immediately after publishing.

---

## Section 3 — Newsjacking Production Prompt

### Master Prompt Template

Copy and complete this prompt. Paste it into Claude or ChatGPT with the
breaking news content appended.

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

### Prompt Customisation by Use Case

**For a financial services client commenting on a Bank of Uganda rate decision:**

Replace `[SPECIFIC EXPERTISE AREA]` with:
"SME lending, mobile money credit products, and the cost of borrowing for
Ugandan businesses"

**For a technology client commenting on a NITA-U regulation:**

Replace `[SPECIFIC EXPERTISE AREA]` with:
"digital infrastructure, data compliance for Ugandan businesses, and
practical implementation of technology regulation"

**For a logistics client commenting on an EAC trade announcement:**

Replace `[SPECIFIC EXPERTISE AREA]` with:
"cross-border freight, last-mile delivery in East Africa, and the operational
impact of trade corridor policy on ground logistics"

---

## Section 4 — GEO Optimisation Checklist

Apply this checklist to every newsjacking article before publishing. This
checklist implements the GEO standards from the `seo-geo-optimisation` skill
in a rapid-response context.

- [ ] **Direct answer in paragraph 1:** The first 50 words answer the core
  reader question. AI search engines extract the first substantive paragraph
  as the citation snippet.
- [ ] **Author name and credentials visible:** Full name, title, and company
  must appear in the byline or author box. Anonymous content does not earn
  EEAT signals.
- [ ] **Original news source cited with date:** AI search engines assess
  factual accuracy by cross-referencing sources. A cited source increases
  citation probability.
- [ ] **H2 headings phrased as questions:** At least two question-format H2s.
  These match the conversational query format of AI search.
- [ ] **FAQ section with 3 questions at the end:** Each question phrased as
  a reader would type it. This is the highest-yield GEO element per unit of
  writing effort.
- [ ] **Publication date visible on the page:** "Published [date]" must appear
  in the article header or metadata. Freshness is a live GEO ranking signal.
- [ ] **Page load time under 3 seconds:** Slow pages are deprioritised by
  AI search crawlers. Test with PageSpeed Insights before distributing.
- [ ] **Word count 500–800 words:** Long enough to be substantive; short
  enough to be indexed and read quickly. Newsjacking content should not
  be padded.

---

## Section 5 — Distribution Sequence

Publish the long-form article to the client's website or blog first. This
establishes the canonical source before social distribution begins.

**Target: complete all five distribution steps within 60 minutes of publishing.**

### Step 1 — LinkedIn (Publish + 5 minutes)

- Copy the opening three paragraphs of the article as a LinkedIn post.
- Add: "Full article: [link]"
- Tag any organisation or person mentioned in the news story (where appropriate).
- Add 3–5 relevant hashtags: industry-specific + geographic (e.g.
  `#UgandaBusiness`, `#EastAfrica`, `#FinancialServices`).
- If the client has a company page, post from the company page and ask the
  author to share from their personal profile within 30 minutes.

### Step 2 — Facebook (Publish + 15 minutes)

- Write a shorter version (100–120 words): headline + the most impactful
  single insight from the article + link.
- Pose the insight as a question to prompt comments:
  "The Bank of Uganda has cut rates. What does this mean for your loan
  repayments? Here is our take: [link]"
- Post to the client's Facebook Page; share to any relevant Facebook Groups
  the client is a member of.

### Step 3 — Instagram (Publish + 30 minutes)

- Pull the single most quotable statistic or insight from the article.
- Format as a quote card in Canva (branded template).
- Caption: one-sentence context + "Full analysis in bio link."
- Update the link in bio to point to the new article.
- Add to Stories as a link sticker post.

### Step 4 — WhatsApp Broadcast (Publish + 45 minutes)

Compose a WhatsApp broadcast message for the client's opted-in contacts list:

Template:
```
Seen this? [NEWS HEADLINE — one sentence summary]

Here is what it means for [INDUSTRY] businesses in [COUNTRY]: [LINK]

— [CLIENT NAME] team
```

Keep the message under 200 characters before the link. Long messages are
truncated in WhatsApp preview; the hook must be in the first line.

Send only to contacts who have opted in to communications from the client.
Do not broadcast to cold contacts.

### Step 5 — X/Twitter (Publish + 60 minutes)

- Post the key insight as a single tweet (max 280 characters) with the article
  link.
- Tag the regulatory body or news outlet if they are active on X.
- EA note: X/Twitter in Uganda is primarily used by journalists, opinion
  leaders, and public-sector officials. Newsjacking content performs strongly
  in this audience if the insight is genuinely expert and not promotional.

---

## Section 6 — EA Newsjacking Trigger Calendar

High-value newsjacking triggers for East African clients. Add these dates
and recurring events to the client's editorial calendar at the start of each
quarter.

### Recurring Triggers (Schedule in Advance)

| Trigger | Frequency | Lead institution |
|---|---|---|
| Bank of Uganda Monetary Policy Committee | Every 2 months (Feb, Apr, Jun, Aug, Oct, Dec) | Bank of Uganda |
| Central Bank of Kenya MPC | Every 2 months | Central Bank of Kenya |
| Uganda Revenue Authority budget circulars | Quarterly + annual budget (June) | URA |
| Kenya Revenue Authority tax notices | As issued; peak January and June | KRA |
| Tanzania Revenue Authority announcements | Quarterly | TRA |
| Uganda Bureau of Statistics economic releases | Monthly (CPI); quarterly (GDP) | UBOS |
| EAC Council of Ministers meetings | Twice yearly | East African Community |
| NITA-U regulatory notices | As issued | NITA-U |
| Meta algorithm updates | As announced | Meta Newsroom |
| WhatsApp Business policy changes | As announced | WhatsApp Business Blog |

### Reactive Triggers (Monitor Continuously)

- Major EA corporate announcements (acquisitions, IPOs, regulatory sanctions)
- Global platform changes with EA relevance (TikTok regulatory actions,
  LinkedIn algorithm updates)
- Macroeconomic events: IMF/World Bank assessments of EA economies, dollar
  exchange rate movements above 5% in a week
- Industry-specific: any government white paper or gazette notice affecting
  the client's sector

### Trigger Severity Classification

Assign each trigger a severity level to guide production prioritisation:

- **Priority 1 (respond within 2 hours):** Bank of Uganda or CBK rate decisions;
  major URA/KRA tax changes; direct regulatory action affecting the client's
  sector
- **Priority 2 (respond within 6 hours):** UBOS economic data; EAC trade
  announcements; major EA corporate news
- **Priority 3 (respond within 24 hours):** Platform updates; international
  macroeconomic events with indirect EA relevance; industry conference outcomes

---

## Quality Criteria

- The alert infrastructure (Google Alerts + IFTTT) is fully specified with
  named alert terms relevant to the client's industry and market; generic
  placeholders are replaced with actual terms before delivery
- The Newsjacking Production Prompt is customised with the client's name,
  industry, target audience, expertise area, and country before being handed
  to the client or account manager
- Every article produced passes all eight items on the GEO Optimisation
  Checklist before it is published
- Distribution follows the five-step sequence and is completed within 60
  minutes of publication; deviation from the sequence is noted and justified
- The EA Trigger Calendar includes at least six scheduled triggers for the
  coming quarter with dates, institutions, and priority classifications
- WhatsApp broadcast messages are sent only to opted-in contacts; this
  confirmation is documented in the client's workflow notes
- The expert commentary in every article is grounded in the client's stated
  expertise area; no article makes claims beyond the client's documented
  competence
- Every article is bylined with the author's full name and title; anonymous
  content is not published under this playbook

---

## Related Skills

- **`seo-geo-optimisation`** — use for the full GEO content strategy that
  newsjacking feeds into; this playbook is the rapid-response execution layer
  of the broader GEO programme
- **`blog-writer`** — use for planned long-form content production that
  complements the reactive newsjacking articles
- **`playbook-content-production`** — use for the full content workflow and
  scheduling system that newsjacking content integrates with
- **`meta-social-listening`** — use for setting up the broader social
  monitoring infrastructure that surfaces newsjacking triggers beyond
  Google Alerts

---

## References

- Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing
  Teams*. neuroflash. [GEO freshness signals; AI search citation dynamics]
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*.
  Pearson. [RACE framework applied to distribution sequencing]
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.
  [Content publication and distribution principles]

---
name: 12-website-content-plan
description: Generates a 90-day blog and website content plan — including 12 article briefs, an editorial calendar, an internal linking structure, and lead magnet ideas. Invoke after completing audience personas and brand voice intake, and before commissioning article writing with the blog-writer skill. This skill produces content strategy only — no web design, technical SEO audit, or page building.
---

# Website Content Plan Generator

Produce four outputs: (1) 12 blog post briefs, (2) an editorial calendar table, (3) an internal linking structure, and (4) lead magnet ideas. This skill covers content strategy and planning only. It does not produce finished articles — use the `blog-writer` skill to generate article text from these briefs. Apply the `east-african-english` skill for tone throughout.

## Required Input

Ask for the following before generating:

- **Client name** — trading name of the business
- **Industry** — sector the business operates in
- **Audience personas** — the named personas from `03-audience-personas` (minimum two)
- **3–5 primary topic areas** — the subjects the business wants to be known for; these become the thematic clusters for articles
- **Target customer journey stage** — Awareness / Consideration / Decision (choose the dominant stage; the content plan will be weighted accordingly)
- **Blog publication frequency** — 1 per week or 2 per month
- **Campaign dates to coordinate with** — any confirmed campaign windows from `09-campaign-strategy` or `11-content-calendar`
- **Country/city** — defaults to Kampala, Uganda

---

## Section 1: 12 Blog Post Briefs

Generate one brief per article. Number each brief clearly (Article 1 of 12 through Article 12 of 12). Distribute articles across the 3–5 primary topic areas proportionally. Do not cluster all articles in one topic.

For each article, produce all nine elements:

### 1. Article Title
Write an SEO-optimised title under 60 characters. The title must be specific and informative — it tells the reader exactly what they will learn. Avoid clickbait. Use the client's industry language and, where appropriate, Ugandan/EA context (e.g., reference Kampala, East Africa, or relevant local conditions).

### 2. Target Reader Persona
State the persona name from `03-audience-personas` this article is primarily written for. Explain in one sentence what specific question or need this article answers for that persona.

### 3. Search Intent
Classify as one of:
- **Informational** — the reader wants to understand something
- **Navigational** — the reader is looking for a specific brand or resource
- **Commercial** — the reader is comparing options before deciding
- **Transactional** — the reader is ready to act and wants to buy, book, or sign up

State the intent and explain in one sentence how the article's structure reflects it.

### 4. Primary Keyword Theme
State the core topic or keyword theme the article should be centred on. Do not generate specific keyword data (keyword tools are outside this skill's scope) — instead state the thematic territory: e.g., "savings accounts for young professionals in Uganda", "how to register a business in Kampala".

### 5. Five Key Questions the Post Must Answer
List the five most important questions a reader has when they arrive at this article. These become the structural backbone. Write them as genuine reader questions, not as headings.

### 6. Suggested Article Structure
List 4–6 H2 headings in logical order. These headings must directly address the five key questions. Do not use headings like "Introduction" or "Conclusion" — every heading must carry information value.

### 7. Word Count Guide
- Informational articles: 800–1,200 words
- How-to guides and step-by-step articles: 1,500–2,000 words
- Comparison and decision-support articles: 1,200–1,500 words

State the recommended word count and the rationale.

### 8. Recommended Call to Action
State one specific CTA that fits the article's intent and the reader's journey stage. Examples:
- Awareness stage: "Share this article with a colleague who is starting a business"
- Consideration stage: "Download our free checklist to compare your options"
- Decision stage: "Book a free 30-minute consultation"

The CTA must align with the client's primary business goal.

### 9. Content Upgrade Idea
Suggest one lead magnet tied to this article. A content upgrade is a free resource the reader can access in exchange for their contact details. It must be directly relevant to the article's topic — not a generic newsletter sign-up.

Format: **[Title of lead magnet]** — [Format: PDF guide / checklist / template / calculator / swipe file] — [Delivery: email opt-in / WhatsApp opt-in]

Example: **"The Uganda Business Registration Checklist"** — PDF checklist — email opt-in

---

## Section 2: Editorial Calendar

Produce a table showing all 12 articles sequenced across the 90-day period, aligned to the client's publication frequency.

| # | Title | Week to Publish | Persona Targeted | Intent | Primary Keyword Theme | CTA |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| … | | | | | | |
| 12 | | | | | | |

**Sequencing rules:**
- Begin with Awareness-stage articles in Weeks 1–4 to build organic traffic
- Move to Consideration-stage articles in Weeks 5–8
- Place Decision-stage articles in Weeks 9–12, aligned to any campaign windows
- Do not publish two articles on the same topic area in consecutive weeks
- If a campaign window falls in the plan, align one article to support the campaign theme in the week before the campaign launches

---

## Section 3: Internal Linking Structure

Internal linking strengthens content authority and guides readers through the site. Map the links between articles and to key service pages.

Show links in this format:

**[Article title]** → links to → **[Article title]** (anchor text: "[suggested anchor text]") + **[Service page name]** (anchor text: "[suggested anchor text]")

Produce a link map for all 12 articles. Each article should link to at least 2 other articles and 1 service page. Where a natural link does not exist, note: "No strong link from this article — do not force an unnatural anchor."

**Note to consultant:** Internal links should be added during the editing stage when using the `blog-writer` skill. Pass this link map to the writer as part of the brief. Do not add more than 5 internal links per article — over-linking reduces usability.

---

## Section 4: Content Upgrade and Lead Magnet Ideas

Identify the 4 articles with the highest potential to attract organic traffic (based on search intent and topic breadth). For each, develop a specific lead magnet.

For each lead magnet, provide:

**Lead Magnet [N]: [Title]**
- **Attached to article:** [Article title]
- **Format:** [PDF guide / checklist / template / calculator / swipe file]
- **Delivery mechanism:** [Email opt-in form on the article page / WhatsApp opt-in via a link in the article / Both]
- **What it contains:** 3–4 bullet points describing the contents of the lead magnet (specific enough to brief a writer)
- **Why a reader would want it:** One sentence explaining the value exchange from the reader's perspective

**Guidance on lead magnet formats for Uganda/EA:**
- Prefer WhatsApp opt-in for audiences primarily on mobile; email opt-in suits B2B and formal sector audiences
- PDF checklists and templates download and use well on low-bandwidth connections
- Calculators and interactive tools require a website developer — flag this if a calculator is recommended
- Keep PDF lead magnets under 8 pages; concise and practical wins over comprehensive and academic in the EA market

---

## Coordination Note

> **Using this plan with other skills:** This content plan is designed to work alongside the `11-content-calendar` — align article publish dates with the relevant pillar themes in the calendar. When articles are ready to write, pass each brief from Section 1 to the `blog-writer` skill. When lead magnets are ready to write, pass the content upgrade details from Section 4 to the `blog-writer` skill with the instruction to produce a lead magnet document, not a blog post.

---

## Quality Criteria

- All 12 article briefs are complete; no element within any brief is left blank or marked TBC
- Articles are distributed across the 3–5 primary topic areas — no single topic receives more than 40% of articles unless specifically justified
- Search intent is correctly classified and the article structure reflects it — a transactional brief looks different from an informational brief
- The editorial calendar sequences articles in awareness-to-decision order unless a specific reason (campaign alignment, seasonal hook) justifies reordering
- Internal link suggestions use natural anchor text — no keyword-stuffed anchor text; no links forced where a natural connection does not exist
- Lead magnets are specific to the client's industry and persona; no generic "download our newsletter" suggestions
- Word count guidance is differentiated by article type — informational posts are not assigned the same word count as step-by-step guides
- British English spelling is used throughout; Ugandan and East African context is applied to examples, titles, and persona references

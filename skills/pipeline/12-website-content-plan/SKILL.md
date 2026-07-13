---
name: 12-website-content-plan
description: "Use when planning 90 days of website and blog content without designing or building the site. Produces website content plan, article briefs and internal-link map; use `11-content-calendar` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Website Content Plan Generator

Produce four outputs: (1) 12 blog post briefs, (2) an editorial calendar table, (3) an internal linking structure, and (4) lead magnet ideas. This skill covers content strategy and planning only. It does not produce finished articles — use the `blog-writer` skill to generate article text from these briefs. Apply the `east-african-english` skill for tone throughout.


<!-- dual-compat-start -->
## Use When

- Use this skill for planning 90 days of website and blog content without designing or building the site.
- Confirm that `11-content-calendar` is not the closer route before proceeding.

## Do Not Use When

- Use `11-content-calendar` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Approved personas, voice guide, business priorities and current content inventory | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Website content plan, article briefs and internal-link map | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified website content plan, article briefs and internal-link map. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Approved personas, voice guide, business priorities and current content inventory is current and attributable | Produce the full website content plan, article briefs and internal-link map and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `11-content-calendar` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `11-content-calendar` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the website content plan, article briefs and internal-link map, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the website content plan, article briefs and internal-link map without approved personas. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `11-content-calendar` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified approved personas, the skill produces a website content plan, article briefs and internal-link map with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`11-content-calendar`](../11-content-calendar/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

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

## Pre-Requisite: The 7 Website Content Priorities (Sheridan, 2019)

Before generating blog briefs, confirm the client's website addresses these seven priorities in order. Content plan effectiveness is severely limited if the website itself fails to convert visitors.

**Priority 1 — Homepage Design and Messaging**
The homepage must lead with the buyer's problem, not the brand. Audit the you:we ratio: count how many times the homepage says "we", "us", and "our" versus "you" and "your". A ratio below 5:1 (you:we) means the homepage is about the brand, not the buyer. Rewrite accordingly. The primary purpose of the homepage is to move the visitor to the next page — it is not to explain everything the business does.

**Priority 2 — Honest Education (The Big 5 on the site)**
Audit the website against the Big 5 question categories: Pricing and Cost, Problems and Limitations, Comparisons, Reviews, and Best in Class. If the site does not address all five, the content plan must prioritise filling these gaps before any other blog content. These are the questions buyers ask before they ever contact the business; unanswered, they result in lost sales.

**Priority 3 — Premium Education (Lead Magnets)**
Beyond blog posts, the website must offer at least one premium content asset behind an opt-in: a buying guide, checklist, template, webinar, or ebook. Premium content converts readers into leads. A site with no opt-in mechanism allows traffic to arrive, consume, and leave — with no ongoing relationship established. The content plan must include at least one premium asset per cluster of related articles.

**Priority 4 — Equal Mix of Text and Visual Content**
Every major topic should have both a written article and a video. Buyers have different consumption preferences; a text-only or video-only site fails half of its potential audience. Where video production is not yet possible, use infographics, images, or embedded social media content.

**Priority 5 — Self-Selection Tools**
Interactive tools on the website that guide buyers through decisions without requiring contact with the business. Examples: a pricing calculator, a product recommendation questionnaire, an eligibility checker, a comparison tool. Consumer searches using "for me" and "should I" phrasing increased 120% in recent years (Sheridan, 2019) — buyers want to self-select, not be sold to. Identify one self-selection tool the client can create and include it in the content plan.

**Priority 6 — Social Proof**
Customer testimonials, journey videos, reviews, Net Promoter Scores, and case studies must be visible throughout the website — not only on a dedicated testimonials page that few visitors find. Include social proof near every CTA, pricing disclosure, and service description. The content plan must include at least two customer journey stories per quarter.

**Priority 7 — Site Speed**
40% of visitors abandon a website that takes more than 3 seconds to load (Sheridan, 2019). The average business website loads in 8–12 seconds. Before producing content, confirm the client's site loads within 3 seconds. If it does not, flag this as a prerequisite action. Slow sites make all content investment less effective: high traffic + high bounce rate = low return.

Use this checklist to brief the client before commencing content production. Do not attempt to drive traffic to a site that fails Priorities 1, 2, or 7.

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

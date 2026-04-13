---
name: 05-social-media-strategy
description: Generates the master social media strategy document — the primary deliverable for strategy-only client engagements. Applies the POEM model and RACE framework as structural backbones. Invoke when a client has completed onboarding (01-client-brief, 02-platform-audit, 03-audience-personas, 04-brand-voice-intake) and needs a comprehensive, board-ready social media strategy document.
---
# Social Media Strategy Generator

Produce the master social media strategy document. This is the primary deliverable for a strategy engagement. Every section must be populated with client-specific content — no generic filler. Apply British English throughout. Default to Uganda/East Africa context unless the client specifies otherwise.

Apply the POEM model (Paid/Owned/Earned) to classify channels. Apply the RACE framework (Reach/Act/Convert/Engage) to structure the KPI section. Reference Bodnar and Cohen (2012), Chaffey (2024), and Kotler et al. (2023) where indicated.

---

### ARM Content Testing Lens

Before approving any content plan or campaign, apply the ARM framework to verify balanced coverage:
*(Hahn, 2003)*

| Letter | Objective | Test Question |
|---|---|---|
| **A — Attract** | Bring in new audiences and prospects | Does this content reach people who do not yet know us? |
| **R — Retain** | Keep existing followers engaged and loyal | Does this content reward people who already follow us? |
| **M — Motivate** | Drive existing audiences to act, buy, or refer | Does this content give existing customers a reason to do something now? |

A healthy content plan addresses all three. A plan heavy on M (promotional) without A or R will shrink its audience over time. A plan heavy on A without M will grow an audience that never converts.

---

<!-- dual-compat:start -->
## Use when
- Generates the master social media strategy document — the primary deliverable for strategy-only client engagements. Applies the POEM model and RACE framework as structural backbones. Invoke when a client has completed onboarding (01-client-brief, 02-platform-audit, 03-audience-personas, 04-brand-voice-intake) and needs a comprehensive, board-ready social media strategy document.
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

Ask for all of the following before generating the strategy document:

- **Client business name** — trading name as it appears on social media
- **Industry and sub-sector** — e.g. "retail — women's fashion", "NGO — maternal health"
- **Country/city** — defaults to Kampala, Uganda if not specified
- **Primary business goal** — one sentence: what success looks like for this client in 12 months
- **Budget band for paid social** — none / low (under UGX 500K/month) / medium (UGX 500K–2M/month) / high (above UGX 2M/month)
- **Outputs from 01-client-brief** — paste or summarise key findings
- **Outputs from 02-platform-audit** — paste or summarise current platform performance data
- **Outputs from 03-audience-personas** — paste or summarise the 2–3 primary personas
- **Outputs from 04-brand-voice-intake** — paste brand voice summary if available
- **Website ownership** — does the client already own a website? If yes, provide the URL. This determines whether a Website and Blog Strategy section is generated.

If any onboarding documents are unavailable, note this explicitly and generate the relevant section with stated assumptions.

---

## Document Structure

Generate all ten sections in order. Use markdown headings. Do not omit any section.

### 1. Situation Analysis

Summarise where the client stands today. Cover four areas:

**Market context:** 2–3 sentences on the industry landscape in the client's geography. Note relevant digital trends in East Africa (e.g. mobile-first audiences, WhatsApp as a primary customer channel, rising TikTok penetration among under-30s).

**Key competitors:** Identify 2–3 competitors. For each, note which platforms they are active on, approximate posting frequency, and one observable strength or weakness. Draw from 02-platform-audit if available; otherwise ask the client to name competitors.

**Current digital presence summary:** Summarise the client's existing social media footprint — platforms active, follower counts, average engagement rate, content quality assessment. Draw directly from 02-platform-audit findings. State clearly where the biggest gaps or opportunities lie.

**Audience overview:** Summarise the 2–3 primary personas from 03-audience-personas. For each persona, note the platform they use most, what motivates them to engage, and what they want from this brand.

---

### 2. Strategy Statement

Write one paragraph (4–6 sentences). State clearly:
- What the social media presence will achieve (link to primary business goal)
- For whom (reference primary personas by name)
- Why this approach is the right one for this client at this time
- The overarching positioning the brand will hold in the social media space

Cite Kotler et al. (2023) on the role of digital brand positioning where relevant.

---

### 3. Platform Selection Rationale

Identify which platforms to prioritise, which to maintain at low effort, and which to deprioritise or exit. Present as a structured list or table.

For each platform in scope, provide:
- **Priority level:** Primary / Secondary / Exit
- **Rationale:** Why this decision was made — link to persona data and business goals
- **POEM classification:**
  - Owned: the brand's organic profile and content
  - Earned: UGC, shares, mentions, PR coverage, word of mouth
  - Paid: boosted posts, paid campaigns, sponsored placements
- **Platform role in the strategy:** what this platform is expected to do (e.g. "Facebook — primary community and customer service channel; broad demographic reach")

Apply EA platform defaults: Facebook for broad reach, Instagram for urban 18–35 aspirational content, TikTok for under-30 entertainment, WhatsApp for direct customer communication, LinkedIn for B2B or professional services, YouTube for long-form tutorials or brand storytelling.

---

### 3b. Website and Blog Content Strategy *(include only if client owns a website)*

The website is the only owned channel the brand fully controls — no algorithm, no terms-of-service risk, no platform changes. Social media drives traffic; the website captures it and converts it. If the client owns a website, this section is mandatory.

**Website as the content hub:** Apply the Hero/Hub/Hygiene content model. The website blog is the Hygiene layer — always-on, searchable, SEO-indexed content that answers the questions the audience is already asking. Social media distributes that content to audiences who are not yet searching.

**Blog strategy:** Define a blog cadence and topic structure aligned to the content pillars in Section 5. Each blog post should:
- Target one specific search query or audience pain point
- Be 600–1,200 words minimum for indexability
- Include one clear CTA (book a demo, download a resource, start a trial)
- End with a summary or key takeaways block — this becomes the basis for social recycling

**Blog-to-social recycling plan:** Every blog post generates at minimum four social assets:
1. **LinkedIn text post** — the argument or insight from the blog, written as a standalone post (no "I wrote a blog" phrasing — the post is the content; the link is in comments)
2. **Instagram carousel** — the key points from the blog as a swipeable carousel (5–7 slides); no need to read the blog to get value
3. **Facebook post** — a single punchy question or statistic from the blog with the article link; optimised for shares and link clicks
4. **X/Twitter thread** — the blog's main argument broken into 4–6 tweets with a link to read the full piece at the end

Optional additions where platforms are in scope:
- WhatsApp broadcast: a one-paragraph summary with a link — personal, direct tone
- TikTok/Reels: talking-head video or screencast version of the blog's main idea

**Content calendar integration:** The blog publishing date anchors a social distribution window. Publish the blog on Monday. LinkedIn post on Tuesday. Instagram carousel on Wednesday. Facebook post on Thursday. X thread on Friday. This stretches one piece of work across five touchpoints in one week.

**SEO note:** The website blog builds search visibility that social media cannot — indexed pages rank; social posts do not. The blog compounds over time; a post published in Month 1 still drives traffic in Month 6. This makes the blog the highest long-term ROI content investment in the mix.

---

### 4. Brand Voice Summary

Write 3–4 sentences summarising the brand's voice and tone for social media. Draw from 04-brand-voice-intake if available. Cover:
- Personality traits (e.g. warm, authoritative, playful, professional)
- Language register (formal / conversational / educational)
- What the brand would and would not say
- How tone shifts across platforms (e.g. more formal on LinkedIn; more relaxed on Instagram Stories)

---

### 5. Content Pillars

Define 3–5 content pillars. Apply the 10-4-1 rule (Bodnar and Cohen, 2012): for every 15 pieces of content, 10 should share relevant third-party or educational content, 4 should be original brand content, and 1 should be directly promotional.

For each pillar, provide:

**Pillar name:** [Short, memorable name]
**Purpose:** One sentence — what this pillar does for the audience and for the brand
**Example post types:** 3–4 specific examples (e.g. "customer spotlight quote graphic", "behind-the-scenes Reel", "tip carousel")
**% of content mix:** Percentage allocation across all pillars must total 100%
**Platforms it suits best:** List the 1–2 platforms where this pillar performs most effectively

Ensure the 10-4-1 rule is honoured in the aggregate percentage allocations — promotional content should not exceed 10–15% of total volume.

---

### 6. Posting Frequency and Content Mix by Platform

Present as a table. Include only the platforms designated as Primary or Secondary in Section 3.

| Platform | Posts/week | Content types | Best posting times (EAT, UTC+3) |
|---|---|---|---|
| Facebook | | | |
| Instagram | | | |
| TikTok | | | |
| WhatsApp (broadcast) | | | |
| LinkedIn | | | |
| YouTube | | | |
| X/Twitter | | | |

Populate only rows relevant to this client. For EAT posting times, apply EA-specific guidance: peak times are typically 07:00–09:00 (commute), 12:00–13:00 (lunch), and 19:00–21:00 (evening). Facebook tends to peak earlier in the day; Instagram and TikTok peak in evenings.

---

### 7. Community Management Principles

Define 4–6 principles that govern how the brand engages with its audience across all platforms. Each principle has a short title and 2–3 sentences of guidance.

Include principles covering:
- **Response time SLAs** — e.g. comments within 4 business hours; DMs within 24 hours; complaints within 2 hours
- **Tone in responses** — how to maintain brand voice in reactive situations
- **Escalation protocol** — what types of enquiries or complaints get escalated, to whom, and how
- **Negative comment policy** — when to respond publicly, when to move to DMs, when to delete (only clear violations of community standards)
- **UGC and mentions** — how to handle and celebrate user-generated content
- **Crisis response** — brief trigger definition; note that the playbook-crisis-communications skill handles full crisis planning

---

### 8. Paid Social Integration

Provide brief guidance on when to boost posts versus when to run structured campaigns. This section is not a campaign plan — it provides strategic guardrails.

Cover:
- **Post boosting:** criteria for deciding a post is worth boosting (high organic engagement, commercial message, event promotion, time-sensitive offer). Minimum budget recommendation per boost.
- **Campaign structure:** when to move from ad-hoc boosting to a structured campaign (use 09-campaign-strategy for full campaign planning)
- **Budget band guidance:** match to the client's stated budget band:
  - None: organic-only; note that organic reach on Facebook is limited (typically 2–5% without paid support)
  - Low: selective boosting of 2–3 posts/month on Facebook and Instagram
  - Medium: monthly always-on boosting plus 1 structured campaign per quarter
  - High: always-on paid social plus multiple campaign flights; recommend engaging 09-campaign-strategy

---

### 9. KPI Framework

Apply the RACE framework (Chaffey, 2024) to organise KPIs across four stages of the customer journey.

Present as a table:

| RACE Stage | KPI | Platform | Current Baseline | 90-Day Target | How to Measure |
|---|---|---|---|---|---|
| Reach | Total impressions | | | | Native analytics |
| Reach | Total reach (unique) | | | | Native analytics |
| Reach | Follower growth rate | | | | Native analytics |
| Act | Engagement rate | | | | Engagements ÷ reach |
| Act | Link clicks | | | | Link-in-bio / UTM |
| Act | Profile visits | | | | Native analytics |
| Convert | Website sessions from social | | | | Google Analytics |
| Convert | Enquiries / DMs / form fills | | | | CRM or manual count |
| Convert | Conversions attributed to social | | | | UTM + CRM |
| Engage | Repeat engagement rate | | | | Native analytics |
| Engage | Community growth (group/broadcast) | | | | Manual count |
| Engage | Sentiment (positive/negative ratio) | | | | Manual review |

Populate Current Baseline from 02-platform-audit data. Set 90-Day Targets as SMART improvements over baseline. Remove rows for KPIs not applicable to this client.

---

### 10. 90-Day Milestone Roadmap

Structure into three months. Each month has a theme, 4–6 specific actions, and a clear milestone (what will be true at the end of the month).

**Month 1 — Foundations and Quick Wins**
Theme: establish the brand's consistent presence, set up systems, and generate early momentum.
- Actions: [list 4–6 specific actions, e.g. "Finalise brand templates and tone guide for content team", "Publish content calendar for Month 1", "Set up WhatsApp Business profile and auto-replies"]
- Milestone: [what success looks like at Day 30]

**Month 2 — Growth and Consistency**
Theme: build on foundations, grow the audience, test content formats.
- Actions: [list 4–6 specific actions, e.g. "Launch first UGC campaign or community challenge", "Begin boosting top-performing organic posts"]
- Milestone: [what success looks like at Day 60]

**Month 3 — Optimisation and Expansion**
Theme: use data to improve performance; introduce new formats or channels if readiness exists.
- Actions: [list 4–6 specific actions, e.g. "Review Month 1–2 analytics and adjust content mix", "Produce first monthly performance report using meta-reporting skill"]
- Milestone: [what success looks like at Day 90]

---

## Quality Criteria

- Situation analysis is client-specific — no generic observations that could apply to any brand
- Strategy statement clearly links the social media approach to the client's primary business goal
- Platform selection rationale explicitly applies the POEM model and justifies deprioritisation decisions
- Content pillars honour the 10-4-1 rule (Bodnar and Cohen, 2012) in aggregate percentage allocations
- KPI table is populated with baselines drawn from 02-platform-audit and targets that are SMART
- RACE framework (Chaffey, 2024) is applied correctly across the four KPI stages
- Community management principles include specific SLA timeframes, not vague commitments
- 90-day roadmap contains specific, named actions — not abstract phases or generic tasks
- British English spelling throughout; EAT timezone applied to all scheduling references
- Paid social guidance is calibrated to the client's stated budget band
- If the client owns a website, Section 3b is included with a blog cadence, recycling plan, and content calendar integration instructions

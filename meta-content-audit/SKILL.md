---
name: meta-content-audit
description: Audits the client's existing social media content history to identify what worked, what did not, and where to improve. Produces a data-driven performance summary, top and bottom content analysis, content pillar coverage review, tone and consistency ratings, and a 30-day improvement plan. Invoke this skill at the start of a new client engagement, after 3–6 months of managed content, or whenever a client questions whether their content strategy is working.
---
# Content Audit

<!-- dual-compat:start -->
## Use when
- Audits the client's existing social media content history to identify what worked, what did not, and where to improve. Produces a data-driven performance summary, top and bottom content analysis, content pillar coverage review, tone and consistency ratings, and a 30-day improvement plan. Invoke this skill at the start of a new client engagement, after 3–6 months of managed content, or whenever a client questions whether their content strategy is working.
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
- A structured audit, report, model, or analytical framework in markdown, with decisions and recommendations tied to evidence.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Before generating the audit output, collect the following from the consultant:

- **Client name** and trading name (if different)
- **Industry** and sub-sector
- **Country / city** (default: Uganda / Kampala)
- **Primary goal** (e.g., increase enquiries, grow brand awareness, improve engagement)
- **Platforms to audit** (select all that apply: Facebook, Instagram, LinkedIn, TikTok, YouTube, X/Twitter, WhatsApp)
- **Content data collected** using the template in Section 1 below — do not proceed without this data
- **Content pillars** (if already established — from `10-content-pillars` skill if available)
- **Brand voice guide** (from `04-brand-voice-intake` skill if available)
- **Audit period:** default is the last 3 months of published content

---

## Step 1: Data Collection Template

Before running the audit, ask the consultant to collect data from each platform's native analytics. Provide this template to complete for every post in the audit period.

**Recommended minimum sample:** last 3 months of content, all posts. A minimum of 30 posts per platform is required for meaningful pattern analysis. If the client has fewer than 30 posts on a platform in 3 months, extend the period to 6 months.

---

**Post-Level Data Template**

For each post, record:

| Field | What to enter |
|---|---|
| Post date | DD/MM/YYYY |
| Platform | Facebook / Instagram / LinkedIn / TikTok / YouTube / X / WhatsApp |
| Content type | Image / Video / Carousel / Text / Story / Reel / Short / Broadcast |
| Content pillar | Enter pillar name if known; leave blank if not yet established |
| Topic / theme | 2–4 words describing the subject |
| Reach / Impressions | Number from platform analytics |
| Engagement | Total: likes + comments + shares + saves |
| Engagement rate | Engagement ÷ Reach × 100 (%) |
| Paid boost? | Yes / No |
| Notable comments or reactions | Any comment worth noting (praise, criticism, question, complaint) |
| Consultant note | Why do you think this post worked or underperformed? |

**Where to find this data per platform:**
- **Facebook / Instagram:** Meta Business Suite > Insights > Content
- **LinkedIn:** Company page > Analytics > Content
- **TikTok:** TikTok Business Centre > Analytics > Content
- **YouTube:** YouTube Studio > Analytics > Content
- **X/Twitter:** X Analytics > Tweets

Export data as a spreadsheet where possible. Sort by engagement rate descending before handing to the audit process.

---

## Output Structure

Generate all seven sections below in order, using the data provided.

---

### 2. Content Performance Summary by Platform

For each platform in scope, produce the following summary table:

**[Platform Name]**

| Metric | Value |
|---|---|
| Total posts audited | |
| Audit period | |
| Average engagement rate | |
| Above-average posts | Count and % of total |
| Below-average posts | Count and % of total |
| Top-performing content type | |
| Worst-performing content type | |
| Highest single engagement rate | |
| Lowest single engagement rate | |

**Benchmark guidance for Uganda / East Africa:**
- Facebook: 1–3% engagement rate is average; above 3% is strong
- Instagram: 2–4% is average; above 5% is strong
- LinkedIn: 0.5–2% is average; above 2% is strong
- TikTok: 4–8% is average; above 10% is strong
- YouTube: measure by watch-time completion % and click-through rate, not engagement rate alone

Note where the client sits relative to these benchmarks. If performance is below benchmark, flag it clearly.

---

### 3. Top-Performing Content Analysis

Identify the top 5 posts across all platforms (ranked by engagement rate; where rates are equal, rank by absolute reach).

For each of the top 5 posts:

**Post [N] — [Platform], [Date]**
- **What the post was:** One sentence describing the content (topic, format, visual approach)
- **Key metric:** Engagement rate and absolute engagement number
- **Why it worked — 3 factors:** Select from: format fit, strong hook, timely topic, emotional resonance, audience relevance, clear call to action, paid amplification, comment engagement, shareability, visual quality
- **What to replicate:** One specific and actionable instruction the team can apply to future content

---

### 4. Worst-Performing Content Analysis

Identify the bottom 3 posts across all platforms (ranked by engagement rate ascending; exclude posts with zero reach, as these indicate a technical issue rather than content failure).

For each of the bottom 3 posts:

**Post [N] — [Platform], [Date]**
- **What the post was:** One sentence describing the content
- **Key metric:** Engagement rate
- **Why it underperformed — honest assessment:** Identify the likely cause. Common causes: wrong format for platform, no clear hook, topic irrelevant to audience, posted at poor time, overly promotional, no visual, confusing call to action, or content was simply not interesting to this audience.
- **What to change or avoid:** One specific instruction

Do not soften this section. Honest diagnosis prevents repeated mistakes.

---

### 5. Content Pillar Coverage Analysis

**If content pillars are established:**

List each pillar and calculate the percentage of audited posts assigned to it.

| Content pillar | Posts assigned | % of total | Status |
|---|---|---|---|
| Pillar 1 | | | Over-represented / Balanced / Under-represented |
| Pillar 2 | | | |
| Pillar 3 | | | |
| Pillar 4 | | | |
| Promotional (if tracked separately) | | | |

A balanced content mix follows the **10-4-1 rule** (Bodnar and Cohen, 2012): for every 10 pieces of shared or educational content, 4 original posts, and 1 promotional post. Flag any pillar that exceeds 40% of the mix (over-reliance) or falls below 10% (neglected).

**If no content pillars exist:**

Cluster the audited posts by topic. Identify 3–5 natural categories that emerge from the data. These become the foundation for establishing pillars. Recommend these clusters as draft pillars to the client.

---

### 6. Tone and Consistency Rating

Rate the client's content on three dimensions, each on a 1–10 scale. Provide a one-sentence justification for each score.

| Dimension | Score (1–10) | Justification |
|---|---|---|
| **Visual consistency** | | Do the posts look like they come from the same brand? (Colours, fonts, image style, logo placement) |
| **Tone consistency** | | Do the posts sound like the same brand? (Vocabulary, sentence length, formality level, use of humour) |
| **Posting consistency** | | Are posts distributed evenly across the period, or clustered in bursts with gaps? |

**Scoring guide:**
- 8–10: Strong and consistent — maintain
- 5–7: Inconsistencies present but brand is recognisable — improve
- 1–4: Significant inconsistency — address before investing further in content production

---

### 7. Priority Improvements — First 30 Days

Produce exactly 5 specific changes the client should make immediately, drawn from the audit findings. Use this format for each:

---

**Improvement [N]: [Title]**

- **What to change:** Specific, actionable instruction (not a general principle)
- **Why:** The specific finding from this audit that supports this change (reference a post, a metric, or a pattern)
- **Expected impact:** What should improve if this change is made consistently over 30 days

---

Prioritise the improvements by likely impact: highest impact first. At least one improvement must address content format or type, at least one must address consistency, and at least one must address content pillar balance.

---

## Quality Criteria

Output meets the standard if it:

- Uses only data provided by the consultant — does not invent metrics or estimate engagement rates without a stated basis
- Platform performance summaries include a comparison against Uganda / EA benchmarks, not just internal averages
- Top and bottom post analysis identifies *specific* and *distinct* reasons for performance — not the same generic factors repeated across every post
- Content pillar coverage section flags imbalances clearly with reference to the 10-4-1 rule
- Tone and consistency ratings are justified with evidence from the content — not assigned arbitrarily
- 30-day improvements are genuinely prioritised (most impactful first) and each is traceable to a specific audit finding
- Output is direct and honest — underperformance is named, not softened

---

## Framework Reference

Apply the **10-4-1 rule** (Bodnar and Cohen, 2012) when assessing content pillar balance. Apply the **RACE framework** (Chaffey, 2024) when interpreting whether content is serving the right stage of the customer journey (Reach / Act / Convert / Engage).

*Bodnar, K. and Cohen, J. (2012) The B2B Social Media Book. Hoboken: Wiley.*
*Chaffey, D. (2024) Digital Marketing: Strategy, Implementation and Practice. 8th edn. Harlow: Pearson.*

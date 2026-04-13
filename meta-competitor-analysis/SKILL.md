---
name: meta-competitor-analysis
description: Analyses 3–5 competitors' social media and digital marketing presence to produce a structured comparison table, content style breakdown, paid ad activity notes, gap analysis, and strategic recommendations. Invoke this skill when a client wants to understand how they compare to their competition, when entering a new market, when launching a new service, or when building a social media strategy from scratch.
---
# Competitor Analysis

<!-- dual-compat:start -->
## Use when
- Analyses 3–5 competitors' social media and digital marketing presence to produce a structured comparison table, content style breakdown, paid ad activity notes, gap analysis, and strategic recommendations. Invoke this skill when a client wants to understand how they compare to their competition, when entering a new market, when launching a new service, or when building a social media strategy from scratch.
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

Before generating this analysis, collect the following from the consultant:

- **Client name** and trading name (if different)
- **Industry** and sub-sector (e.g., hospitality > restaurant; financial services > microfinance)
- **Country / city** (default: Uganda / Kampala)
- **Primary goal** (e.g., grow brand awareness, increase enquiries, defend market position)
- **Client's own platform stats** for direct comparison:
  - Platforms active on
  - Follower counts per platform
  - Estimated engagement rate (average likes + comments ÷ reach × 100)
  - Posting frequency (posts per week per platform)
  - Whether paid ads are currently running
- **Competitor list** (3–5 competitors):
  - Business name
  - Social media handles per platform (Facebook page name, Instagram handle, TikTok handle, LinkedIn page, etc.)
  - Any known context (direct competitor / aspirational benchmark / indirect competitor)

---

## Output Structure

Generate all five sections below in order.

---

### 1. Competitor Comparison Table

Include one row for the client at the top, labelled **[CLIENT — FOR COMPARISON]**, before listing competitors. This allows direct visual benchmarking.

| Competitor | Platforms active on | Follower counts (per platform) | Posting frequency | Content style | Avg engagement rate est. | Paid ad activity visible | Key strengths | Key weaknesses | Notes |
|---|---|---|---|---|---|---|---|---|---|
| [CLIENT — FOR COMPARISON] | | | | | | | | | |
| Competitor 1 | | | | | | | | | |
| Competitor 2 | | | | | | | | | |
| Competitor 3 | | | | | | | | | |
| Competitor 4 (if applicable) | | | | | | | | | |
| Competitor 5 (if applicable) | | | | | | | | | |

**Column guidance:**

- **Content style:** 2–3 words (e.g., "polished, branded", "casual, humorous", "educational, text-heavy")
- **Avg engagement rate est.:** Use visible likes and comments on the last 10 posts ÷ follower count × 100. Note this is an estimate, not platform-reported data.
- **Paid ad activity visible:** Yes / No / Unknown. See Section 3 for how to check.
- **Notes:** Anything notable — recent rebrand, viral post, account dormancy, verified status.

---

### 2. Content Style Analysis Per Competitor

For each competitor (and the client), produce the following breakdown:

**[Competitor Name]**

- **Most-used content type:** Video / Image / Carousel / Text / Reel / Story (select the dominant format observed)
- **Tone and voice:** Formal / Casual / Humorous / Educational / Inspirational / Promotional (select the predominant tone)
- **Visual style:** Polished / Authentic / Branded / Minimal / User-generated (select the predominant style)
- **Topics they dominate (3–4 themes):** List the subject areas that appear most frequently in their content
- **What they do not talk about (gaps):** Identify topics, audiences, or formats conspicuously absent from their content

Repeat this block for every competitor, then include the client's own content style for comparison.

---

### 3. Paid Ad Activity Note

**How to find competitor ad data (free tools):**

- **Meta Ad Library** (facebook.com/ads/library): Search by competitor page name. Shows all currently active Facebook and Instagram ads. No account required. Filter by country (select Uganda or the relevant market).
- **TikTok Creative Center** (ads.tiktok.com/business/creativecenter): Shows top-performing ads by category and region. Useful for spotting competitors running TikTok paid activity.
- **LinkedIn Ad Library**: Available via any LinkedIn company page under "Posts > Ads". Shows active sponsored content.
- **Google Display Network**: Search "[competitor name] ad" in Google Images to surface display banner ads. For traffic intelligence, use SimilarWeb free tier (similarweb.com) to estimate referral sources.

**Important caveat:** Data from these sources is indicative, not exact. Ad spend figures are not disclosed. The presence or absence of ads confirms activity only — it does not reveal budget, targeting, or performance.

For each competitor, note:
- **Facebook/Instagram ads:** Active / Not active / Unknown
- **TikTok ads:** Active / Not active / Unknown
- **LinkedIn ads:** Active / Not active / Unknown
- **Observation:** Any notable ad formats, themes, or calls to action visible in the ad library

---

### 4. Gap Analysis

Identify where the client can win against the field. Produce 3–5 specific opportunities drawn from the comparison data. Structure each gap as follows:

**Gap type — [title]**
What the gap is, which competitor(s) it applies to, and why the client is positioned to exploit it.

Use the following gap categories as a framework (not all will apply to every client):

- **Platform gap:** A platform where competitors are absent or under-active. If all competitors are focused on Facebook but no one is building a LinkedIn presence, the client can own that space in the industry.
- **Content gap:** A topic, format, or audience segment that competitors are not serving. In Uganda/EA, common gaps include: local-language content (Luganda, Swahili), SME-focused educational content, and behind-the-scenes / process content.
- **Tone gap:** If all competitors use formal, corporate language, authentic and conversational content will stand out. The reverse is also true in professional sectors.
- **Community gap:** If no competitor actively responds to comments, engages in discussions, or recognises their audience publicly, a client who does this consistently builds disproportionate loyalty.
- **Speed gap:** If competitors post 2–3 times per week and the client can consistently post 5–7 times per week with quality content, frequency becomes the differentiator.

---

### 5. Strategic Recommendations

Produce exactly 5 specific recommendations. Each recommendation must link back to a named gap or insight from the analysis. Use this format for each:

---

**Recommendation [N]: [Title]**

- **What to do:** Specific action (e.g., "Publish two Instagram Reels per week showcasing the production process")
- **Why:** The gap or finding that makes this the right move (cite the specific competitor or gap)
- **Platform:** Which platform(s) this applies to
- **Expected benefit:** The measurable or observable outcome if executed consistently for 90 days

---

Ensure recommendations span at least 3 different platforms and cover a mix of organic and (if relevant) paid tactics.

---

## Quality Criteria

Output meets the standard if it:

- Includes a client row at the top of the comparison table for direct benchmarking
- Covers every competitor provided, with no placeholder or skipped rows
- Content style analysis identifies genuine absences (what competitors do *not* cover) — not just what they do
- Paid ad activity section directs the consultant to free tools with specific navigation instructions, not generic advice
- Gap analysis identifies gaps that are *actionable* for the specific client — not generic observations that could apply to any business
- Strategic recommendations are each tied to a specific gap or competitor insight from the analysis
- Recommendations span multiple platforms and include a realistic timeframe for expected benefit
- All output defaults to Uganda / East Africa context unless otherwise specified

---

## Framework Reference

Apply the **POEM model** (Paid / Owned / Earned) when categorising competitor activity. Earned media (shares, press, organic viral) is often the hardest to observe but most valuable — note any evidence of it in the competitor profiles.

*Bodnar, K. and Cohen, J. (2012) The B2B Social Media Book. Hoboken: Wiley.*
*Chaffey, D. (2024) Digital Marketing: Strategy, Implementation and Practice. 8th edn. Harlow: Pearson.*

---
name: meta-competitor-analysis
description: "Use when comparing named competitors to find evidence-backed positioning and content gaps. Produces competitor comparison and opportunity register; use `02-platform-audit` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Competitor Analysis


<!-- dual-compat-start -->
## Use When

- Use this skill for comparing named competitors to find evidence-backed positioning and content gaps.
- Confirm that `02-platform-audit` is not the closer route before proceeding.

## Do Not Use When

- Use `02-platform-audit` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Named competitors, market boundary and dated public evidence | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Competitor comparison and opportunity register | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. This is read-only by default: inspect and report without changing source records, accounts, skills or campaigns. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified competitor comparison and opportunity register. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Named competitors, market boundary and dated public evidence is current and attributable | Produce the full competitor comparison and opportunity register and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `02-platform-audit` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `02-platform-audit` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the competitor comparison and opportunity register, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the competitor comparison and opportunity register without named competitors. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `02-platform-audit` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified named competitors, the skill produces a competitor comparison and opportunity register with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`02-platform-audit`](../../pipeline/02-platform-audit/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

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

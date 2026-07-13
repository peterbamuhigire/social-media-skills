---
name: meta-content-audit
description: "Use when reviewing an existing content history to decide what to keep, stop, test or improve. Produces content audit and prioritised improvement plan; use `meta-competitor-analysis` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Content Audit


<!-- dual-compat-start -->
## Use When

- Use this skill for reviewing an existing content history to decide what to keep, stop, test or improve.
- Confirm that `meta-competitor-analysis` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-competitor-analysis` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Content inventory and platform performance exports for a stated period | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Content audit and prioritised improvement plan | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. This is read-only by default: inspect and report without changing source records, accounts, skills or campaigns. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified content audit and prioritised improvement plan. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Content inventory and platform performance exports for a stated period is current and attributable | Produce the full content audit and prioritised improvement plan and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-competitor-analysis` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-competitor-analysis` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the content audit and prioritised improvement plan, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the content audit and prioritised improvement plan without content inventory and platform performance exports for a stated period. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-competitor-analysis` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified content inventory and platform performance exports for a stated period, the skill produces a content audit and prioritised improvement plan with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-competitor-analysis`](../meta-competitor-analysis/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

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

---
name: meta-evergreen-content-strategy
description: "Use when identifying, refreshing and scheduling durable content from an existing library. Produces evergreen content register and 90-day rotation; use `meta-content-repurposing` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Evergreen Content Lifecycle Management System

*Source framework: Macarthy, A. (2022) 500 Social Media Marketing Tips. 6th edn.*

---


<!-- dual-compat-start -->
## Use When

- Use this skill for identifying, refreshing and scheduling durable content from an existing library.
- Confirm that `meta-content-repurposing` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-content-repurposing` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Content inventory, performance history and expiry constraints | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Evergreen content register and 90-day rotation | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified evergreen content register and 90-day rotation. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Content inventory, performance history and expiry constraints is current and attributable | Produce the full evergreen content register and 90-day rotation and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-content-repurposing` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-content-repurposing` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the evergreen content register and 90-day rotation, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the evergreen content register and 90-day rotation without content inventory. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-content-repurposing` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified content inventory, the skill produces a evergreen content register and 90-day rotation with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-content-repurposing`](../meta-content-repurposing/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Before generating the evergreen content system, ask for the following:

- **Client business name** and trading name (if different)
- **Industry** and sub-sector
- **Country / city** (default: Uganda / Kampala)
- **Platforms in scope** (select all that apply: Facebook, Instagram, LinkedIn, TikTok, YouTube, WhatsApp, X/Twitter)
- **Existing content archive** — can the consultant share the last 12 months of posts, or are they auditing from scratch? If from scratch, state this clearly; the audit steps will guide data collection.
- **Current posting frequency** per platform (e.g., Facebook: 5×/week, Instagram: 3×/week)
- **Number of evergreen candidates identified** in the initial review (or "unknown — running the full audit now")
- **Primary content goal** — select one: awareness / education / trust-building / conversion

Do not generate the rotation plan or calendar until these inputs are confirmed.

---

## What Is Evergreen Content?

Evergreen content remains relevant and valuable regardless of when it is consumed. It answers questions that do not change: how-to guides, explanations of industry fundamentals, step-by-step processes, lists of resources, and FAQs.

It contrasts with time-sensitive content — news announcements, promotions, event posts, and seasonal campaigns — which has a short shelf life and should not enter the evergreen rotation.

**Why evergreen content matters for EA SMEs:**

- Limited production capacity makes constant-new-content models unsustainable for most small businesses
- Trust-building content (how-to, why, what to expect) is consumed repeatedly in East African markets, where buyers conduct extensive research before purchasing
- WhatsApp shares extend the reach of evergreen posts beyond the algorithm window, circulating content in groups and broadcast lists long after the original post date
- A well-maintained evergreen library reduces the monthly content production burden by 30–40%

---

## Step 1: Identify Evergreen Candidates

Run this audit on the client's existing content (last 12 months minimum). Apply the same data collection approach as `meta-content-audit` if a full audit has not yet been completed.

For each post, ask four screening questions:

1. **Would this post be just as useful to a reader in 6 months as it is today?** Yes = evergreen candidate. No = time-sensitive; exclude.
2. **Does it reference a specific date, promotion, event, or news story?** Yes = time-sensitive; exclude.
3. **Has it generated saves, shares, or link clicks — not just likes?** Yes = high-value candidate. Saves and shares are stronger signals of durable value than likes.
4. **Is it a how-to, FAQ, process guide, list, or explanation?** Yes = likely evergreen by format.

A post must pass questions 1 and 4 to advance to the scoring stage. Questions 2 and 3 are filters: question 2 removes time-sensitive content; question 3 ranks candidates.

**Evergreen content types for EA SMEs:**

- "How to [do something your customer needs to do]"
- "What to look for when choosing [your product/service category]"
- "5 things most people don't know about [your industry]"
- "[Industry] mistakes and how to avoid them"
- "Step-by-step guide to [relevant process]"
- "Why [common belief in your market] is wrong"
- Explainer posts about the client's core product or service
- FAQs drawn from WhatsApp or in-person customer enquiries

---

## Step 2: Score Evergreen Value

Score each candidate on 3 dimensions (1–5 each, maximum 15). Apply this scoring table to every post that passed the Step 1 filters.

| Dimension | Score 1 | Score 3 | Score 5 |
|---|---|---|---|
| **Relevance durability** | Likely outdated in 3 months | Relevant for 12 months | Relevant for 2+ years |
| **Audience value** | Low engagement; few saves or shares | Average engagement; some saves | High saves/shares; multiple meaningful comments |
| **Production investment** | Quick text post or single image | Moderate effort — original copy with visual | Long-form, high-effort content (carousel, video script, detailed guide) |

**Score interpretation:**

| Total score | Classification | Action |
|---|---|---|
| 12–15 | **Tier 1 — Priority evergreen** | Include in rotation immediately; refresh before first republication |
| 8–11 | **Tier 2 — Conditional evergreen** | Refresh before republishing; review annually |
| Below 8 | **Time-sensitive or low-value** | Do not include in rotation |

Record each post's tier in a simple spreadsheet with columns: Post title / Platform / Original date / Score / Tier / Last republished / Refresh needed.

---

## Step 3: Refresh Protocol

A refreshed evergreen post is not a copy-paste republication. It is an updated version that serves the same durable purpose with current context. Repeat audiences need a new entry point; new audiences need accuracy.

Apply this checklist before republishing any evergreen post:

- [ ] Update any statistics, prices, or data points that may have changed since the original publication date
- [ ] Remove or replace any references to specific dates, past promotions, or expired events
- [ ] Check that all linked URLs still work — website pages, WhatsApp numbers, booking links
- [ ] Update the opening hook — write a new first sentence or headline that creates a fresh entry point for repeat viewers
- [ ] Add one current local reference (a recent EA news item, a current Ugandan cultural moment, or a relevant seasonal hook) to signal that the content is fresh
- [ ] If the original post used stock imagery or a dated visual, consider replacing with original photography or an updated graphic
- [ ] If the original was AI-assisted, run it through the `ai-content-humaniser` skill before republishing

A refresh should take 20–30 minutes per post for Tier 1 content and 30–45 minutes for Tier 2 content (which requires more substantial updating).

---

## Step 4: Build the Evergreen Rotation

### Recommended content ratio

Apply the following default ratio across the full content schedule:

**40% evergreen (refreshed) / 40% new original / 20% timely or promotional**

This ratio serves clients with limited production capacity while maintaining audience trust through new content and commercial viability through promotional posts. It aligns with the **10-4-1 rule** (Bodnar and Cohen, 2012): evergreen posts fill the recurring value-content slots; new original content fills original posts; promotional content fills the 1-in-15 promotional slot.

Adjust the ratio if the client's primary goal is conversion (shift to 30/30/40) or awareness (shift to 50/40/10).

**Example — 5-posts/week Instagram account:**

| Weekly slot | Type | Count |
|---|---|---|
| Evergreen rotation (refreshed) | 40% | 2 posts/week |
| New original content | 40% | 2 posts/week |
| Timely / promotional | 20% | 1 post/week |

### Republication cadence

- **Tier 1 evergreen (score 12–15):** Republish every **60–90 days**
- **Tier 2 evergreen (score 8–11):** Republish every **90–120 days**, after completing the refresh protocol
- Do not republish the same post more than once per 60 days on any single platform, regardless of tier

### Platform-specific evergreen guidance

**Facebook:** Evergreen performs well — the algorithm continues to show posts to new audiences over time. Republish with updated copy; do not simply reshare the original. Pin the top-performing evergreen post to the top of the Page to maximise new-visitor exposure.

**Instagram:** Feed posts lose algorithmic reach after 48–72 hours, but Stories can be saved to Highlights permanently. Save top evergreen posts to Highlights organised by category (e.g., "How To", "About Us", "FAQs"). Reels with evergreen topics continue to surface through discovery for weeks after posting — prioritise evergreen topics for Reels production.

**WhatsApp Broadcast:** Evergreen content is ideal for broadcast lists because it provides information that helps recipients rather than merely promoting. Rotate evergreen how-to and FAQ content monthly to subscriber lists. Keep broadcasts concise: 2–4 sentences with a link or a clear CTA to reply or call.

**LinkedIn:** Evergreen performs exceptionally well — posts circulate via shares for weeks and appear in search results. Republish evergreen posts every 60 days with a new opening sentence. Archive the original rather than deleting it; LinkedIn's algorithm does not penalise for similar topics posted months apart.

**YouTube:** Evergreen is the dominant content type on YouTube — a tutorial video posted in 2022 may still drive views and subscribers in 2026. Prioritise evergreen topics for all YouTube production. Update video descriptions and pinned comments when information changes rather than deleting and re-uploading.

**TikTok:** Lower inherent evergreen value due to the trend-driven algorithm. However, how-to and "did you know" content has a longer shelf life than trend-based content. Test 1–2 evergreen TikToks per month — if a how-to video sustains views after 2 weeks, it qualifies for the evergreen library.

**X/Twitter:** Content decays quickly, but threads on durable topics (industry explanations, frameworks, lists of tools) attract ongoing engagement via search and retweets. Republish high-performing evergreen threads every 90 days with a new opening tweet.

---

## Step 5: Evergreen Content Calendar

Produce a 90-day rotation plan using the table format below. Work from the scored and tiered inventory established in Steps 1 and 2. Integrate the evergreen rotation into the master content calendar produced by `11-content-calendar` — evergreen slots replace, not add to, the existing posting schedule.

**Instructions:**

- Assign Tier 1 posts to the earliest available slots in the rotation
- Space republications so the same post does not appear within 60 days on the same platform
- Mark "Refresh needed" as Yes for any post being republished for the first time, or for any post last refreshed more than 90 days ago
- Coordinate with `meta-content-repurposing` to ensure evergreen posts are also entered into the repurposing chain — a refreshed evergreen blog post, for example, can seed a carousel and a WhatsApp broadcast in the same week

**90-Day Evergreen Rotation Table:**

| Week | Platform | Post Type | Evergreen Topic | Tier | Last Published | Refresh Needed? |
|---|---|---|---|---|---|---|
| 1 | Instagram | Carousel | [Client-specific topic] | 1 | [DD/MM/YYYY] | Yes |
| 1 | Facebook | Post | [Client-specific topic] | 1 | [DD/MM/YYYY] | Yes |
| 1 | WhatsApp | Broadcast | [Client-specific topic] | 1 | [DD/MM/YYYY] | Yes |
| 2 | LinkedIn | Post | [Client-specific topic] | 1 | [DD/MM/YYYY] | Yes |
| 2 | Instagram | Reel | [Client-specific topic] | 2 | [DD/MM/YYYY] | Yes |
| 3 | Facebook | Post | [Client-specific topic] | 1 | [DD/MM/YYYY] | No |
| 3 | YouTube | Video | [Client-specific topic] | 1 | [DD/MM/YYYY] | No |
| ... | | | | | | |

Populate all 13 weeks. Each week should contain at least 2 evergreen slots (matching the 40% ratio). Generate the full table with the client's actual evergreen topics drawn from the inventory.

---

## Quality Criteria

Output meets the standard if it:

- Evergreen identification uses the 3-dimension scoring system with explicit numerical scores — not a subjective or qualitative judgement
- Refresh protocol includes at least 6 specific checks before any post is republished, with an estimated time per post
- Rotation ratio is stated explicitly as a percentage split (default 40/40/20, or adapted to the client's frequency with a stated reason for the adjustment)
- Platform-specific notes cover at least 5 platforms with meaningfully different evergreen strategies — not minor paraphrasing of the same advice
- 90-day rotation calendar is produced in table format with all required columns populated using the client's actual content topics
- Tier 1 and Tier 2 republication cadences are stated numerically in days (60–90 days and 90–120 days respectively) — not vaguely as "regularly" or "periodically"
- WhatsApp Broadcast is included as a named evergreen distribution channel with specific guidance on message length and content type
- Output integrates with `11-content-calendar` (rotation slots align with the master schedule), `meta-content-repurposing` (evergreen posts enter the repurposing chain), and `meta-content-audit` (audit data informs the scoring)

---

## Framework Reference

Apply the **10-4-1 rule** (Bodnar and Cohen, 2012) when calibrating the evergreen ratio within the full content mix. Apply the **Hero/Hub/Hygiene** model (YouTube/Google) to classify evergreen content: Hygiene content (FAQ, how-to, explainer) maps directly to the evergreen library; Hub content (regular series) may have partial evergreen value; Hero content (campaigns, announcements) is time-sensitive and should not enter the evergreen rotation.

Use the **RACE framework** (Chaffey, 2024) to ensure the evergreen library covers all customer journey stages: Reach (awareness posts), Act (educational and how-to posts), Convert (process guides, what to expect posts), and Engage (community and trust-building posts).

*Bodnar, K. and Cohen, J. (2012) The B2B Social Media Book. Hoboken: Wiley.*
*Chaffey, D. (2024) Digital Marketing: Strategy, Implementation and Practice. 8th edn. Harlow: Pearson.*
*Macarthy, A. (2022) 500 Social Media Marketing Tips. 6th edn.*

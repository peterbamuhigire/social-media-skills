---
name: 02-platform-audit
description: "Use when auditing active social profiles and named competitors before strategy work. Produces platform audit, benchmark and prioritised quick wins; use `meta-content-audit` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Platform Audit Generator

Produce three sections of audit output followed by a 6-slide deck outline. Base all findings on public profile data, the completed client brief, and the data sources listed below. Apply the `east-african-english` skill for tone throughout. Flag all estimates clearly — do not present inferred data as measured fact.


<!-- dual-compat-start -->
## Use When

- Use this skill for auditing active social profiles and named competitors before strategy work.
- Confirm that `meta-content-audit` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-content-audit` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Approved client brief, platform access or exports, and named competitors | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Platform audit, benchmark and prioritised quick wins | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. This is read-only by default: inspect and report without changing source records, accounts, skills or campaigns. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified platform audit, benchmark and prioritised quick wins. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Approved client brief, platform access or exports, and named competitors is current and attributable | Produce the full platform audit, benchmark and prioritised quick wins and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-content-audit` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-content-audit` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the platform audit, benchmark and prioritised quick wins, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the platform audit, benchmark and prioritised quick wins without approved client brief. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-content-audit` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified approved client brief, the skill produces a platform audit, benchmark and prioritised quick wins with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-content-audit`](../../meta-analytics-ops/meta-content-audit/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Ask for the following before generating any audit content:

- **Client name and industry** — as recorded in the 01-client-brief
- **Active platforms** — list each platform the client uses, with the exact handle or URL for each
- **Competitor names and handles** — 3 named competitors with their social media handles on each relevant platform
- **Completed 01-client-brief** — provide as context if available; note any gaps if it is not available
- **Country / city** — defaults to Kampala, Uganda if not specified

If competitor handles are missing, ask for them before proceeding. The competitive benchmarking section cannot be completed without them.

---

## Data Sources

Use the following sources for all audit data. Note the source against each data point.

| Source | What it provides | Cost |
|---|---|---|
| Manual profile review | Follower count, bio completeness, posting frequency, last post date, content quality | Free |
| Meta Ad Library (adslibrary.facebook.com) | Whether the client or competitor is running paid ads; ad creative visible | Free |
| Facebook / Instagram native insights | Engagement data — only accessible if the consultant has account access | Free (requires access) |
| SimilarWeb free tier (similarweb.com) | Website traffic estimates and referral source context | Free (limited) |
| Google Analytics / Meta Business Suite | Owned data — only if client shares access | Free (requires access) |

Where account access is not available, estimate engagement rate using the formula:
**Estimated engagement rate = (total likes + comments on last 10 posts) ÷ (follower count × 10) × 100**

Label all estimates as *(estimated — no account access)*.

---

## Section 1: Platform Audit Tables

Generate one table per active platform. Use the exact column structure below.

**Instructions:**
- Complete one table per platform the client is active on
- Score profile completeness and content quality using the scoring guides beneath the table
- Add a Notes column for any qualitative observations not captured by the scores

---

**Platform: [Platform Name]**
**Client handle:** [handle]
**Date of review:** [date]

| Metric | Finding |
|---|---|
| Follower count | |
| Posting frequency | *(posts per week, based on last 30 days)* |
| Date of last post | |
| Estimated engagement rate | *(formula above; note if exact data available)* |
| Profile completeness score | *(1–10 — see scoring guide)* |
| Profile completeness gaps | *(list missing elements)* |
| Content quality rating | *(1–10 — see scoring guide)* |
| Content quality notes | *(specific observations)* |
| Paid ad activity | *(Yes / No / Unknown — check Meta Ad Library)* |

Repeat this table for every active platform.

---

### Profile Completeness Scoring Guide

Score out of 10. Award one point for each element present:

1. Profile photo — clear, on-brand, correctly sized for the platform
2. Cover image or header — on-brand, current (not a default or outdated image)
3. Bio or About section — written, includes relevant keywords, not generic
4. Website link — present and working
5. CTA button — enabled and correctly configured (e.g. "Contact Us", "Book Now", "Shop Now")
6. Contact information — phone number, email, or address where platform allows
7. Pinned post — present and relevant (not outdated)
8. Highlights or featured content — Instagram Highlights, LinkedIn Featured, Facebook pinned post
9. Username / handle — professional, consistent with other platforms, easy to find
10. Category or page type — correctly set (e.g. "Local Business", "Product/Service")

A score of 7–10 = strong; 4–6 = needs attention; below 4 = significant gaps.

---

### Content Quality Rating Guide

Score out of 10 across five dimensions (2 points each):

1. **Visual consistency** — Images, graphics, and video use consistent colours, fonts, and style. Brand is recognisable across posts. *(0 = inconsistent, 1 = partially consistent, 2 = fully consistent)*
2. **Caption quality** — Captions are grammatically correct, purposeful, and appropriate length for the platform. Not just a string of hashtags. *(0 = poor, 1 = acceptable, 2 = strong)*
3. **Platform feature usage** — Uses native features: Stories, Reels, Polls, LinkedIn Articles, TikTok trends. *(0 = none, 1 = occasional, 2 = regular)*
4. **Audience interaction** — Responds to comments and messages; asks questions; runs polls or interactive content. *(0 = no interaction, 1 = occasional, 2 = consistent)*
5. **Content variety** — Mix of content types: educational, promotional, behind-the-scenes, user-generated, seasonal. Not all promotional. *(0 = single type, 1 = some variety, 2 = good mix)*

A score of 8–10 = strong; 5–7 = developing; below 5 = requires urgent improvement.

---

## Section 2: Competitive Benchmarking Table

Generate one benchmarking table per major platform (combine minor platforms into a single summary row if the client is not active there).

**Platform: [Platform Name]**

| Metric | [Client Name] | [Competitor 1] | [Competitor 2] | [Competitor 3] |
|---|---|---|---|---|
| Follower count | | | | |
| Posting frequency (per week) | | | | |
| Estimated engagement rate | | | | |
| Profile completeness score | | | | |
| Content quality rating | | | | |
| Paid ad activity | | | | |
| Standout content type | | | | |

After each table, add a three-point commentary:

- **Where the client leads:** *(specific metric or quality where the client outperforms competitors)*
- **Where the client lags:** *(specific metric or quality where competitors are ahead)*
- **Visible gap to exploit:** *(an area where all competitors are weak that the client could own)*

**Data source note:** All competitor data is collected via manual public profile review and Meta Ad Library. Follower counts and engagement rates are point-in-time observations. Engagement rates are estimated using the formula above unless native data is available. Do not infer strategy or revenue from public data alone.

---

## Section 3: Quick Wins List

Generate a prioritised list of exactly 10 actions the client can take in the first week of engagement. Sequence from easiest/fastest to more involved. For each item:

- **Action** — one clear sentence describing what to do
- **Platform(s)** — which platform(s) this applies to
- **Effort** — Low / Medium
- **Impact** — High / Medium
- **Category** — Profile / Content / Posting rhythm / Community management

---

**Quick wins structure — use these categories as a guide:**

**Profile improvements (Low effort, immediate impact — aim for 3–4 items):**
- Update bio with keywords relevant to the client's industry and location
- Replace outdated cover image with current, on-brand artwork
- Enable and configure the correct CTA button for the business goal
- Add website link and contact information where missing
- Set profile photo to consistent, correctly sized brand image across all platforms

**Content gaps to fill (Medium effort, High impact — aim for 2–3 items):**
- Identify the most under-represented content type from the quality audit and schedule two pieces
- Create a pinned post that explains who the business is and what action visitors should take
- Post the first piece of user-generated or community-focused content if none exists

**Posting rhythm corrections (Low effort, Medium impact — aim for 1–2 items):**
- Set a minimum posting schedule per platform and stick to it for 30 days
- Schedule posts for peak Uganda/EA usage times: 7–9 am (commute), 12–2 pm (lunch), 7–9 pm (evening)

**Community management fixes (Low effort, High impact — aim for 1–2 items):**
- Respond to all unanswered comments and messages that are less than 30 days old
- Set up a saved reply or auto-response for common enquiries on WhatsApp Business

---

## Output 4: 6-Slide Deck Outline

Generate immediately after the quick wins list. Use the exact deck format from CLAUDE.md.

---

**Slide 1 — Audit Overview**
**Headline:** [Client name]'s social media: where things stand today
**Bullets:**
- Platforms reviewed: [list]
- Competitors analysed: [list]
- Audit date: [date]
- Headline finding: [one sentence summarising the most important finding]
**Speaker Notes:** Set the context. Explain the audit methodology — manual review, Meta Ad Library, estimated engagement formula. Acknowledge that data is a point-in-time snapshot.
**Visual Direction:** Clean title slide with client logo, audit date, and a simple summary stat (e.g. "4 platforms reviewed / 3 competitors benchmarked").

---

**Slide 2 — Platform-by-Platform Findings**
**Headline:** [Strongest platform] is the most developed; [weakest platform] needs immediate attention
**Bullets:**
- [Platform 1]: Score X/10 completeness, X/10 content quality — [one-line finding]
- [Platform 2]: Score X/10 completeness, X/10 content quality — [one-line finding]
- [Platform 3]: Score X/10 completeness, X/10 content quality — [one-line finding]
*(Add one bullet per additional platform if more than 3 — condense minor platforms)*
**Speaker Notes:** Walk through each platform score. Highlight the most significant gap. Note if the client has strong content quality but weak posting rhythm, or strong presence but low engagement.
**Visual Direction:** Table or scorecard layout. Use a simple colour coding: green (7–10), amber (4–6), red (below 4).

---

**Slide 3 — Competitive Comparison: Presence and Reach**
**Headline:** [Competitor name] leads on reach; [client name] can compete on engagement
**Bullets:**
- Follower counts: client vs. competitors
- Posting frequency comparison
- Profile completeness comparison
- Where the client currently leads
**Speaker Notes:** Emphasise that follower count is a vanity metric. A smaller, more engaged audience is more valuable than a large disengaged one. Reference Bodnar and Cohen (2012) on quality over quantity.
**Visual Direction:** Side-by-side comparison table or bar chart. Client column highlighted.

---

**Slide 4 — Competitive Comparison: Content and Engagement**
**Headline:** Content quality is where the real gap exists — and where the client can win
**Bullets:**
- Content quality scores: client vs. competitors
- Engagement rate comparison (estimated)
- Paid ad activity: who is spending vs. who is not
- The gap no competitor is currently exploiting
**Speaker Notes:** Name the specific content gap identified in the audit. If a competitor is running paid ads and the client is not, flag this. If no competitor is using a particular platform feature (e.g. Instagram Reels), note this as an opportunity.
**Visual Direction:** Comparison table continuing from Slide 3. Add a callout box for "The gap to exploit".

---

**Slide 5 — Key Gaps and Opportunities**
**Headline:** Three gaps to close; one opportunity to own
**Bullets:**
- Gap 1: [specific finding]
- Gap 2: [specific finding]
- Gap 3: [specific finding]
- Opportunity: [one area where the client can establish a clear lead]
**Speaker Notes:** Frame gaps as opportunities, not failures. Each gap should connect to a specific recommended action. The opportunity should be grounded in competitive analysis — not generic advice.
**Visual Direction:** Four-box layout: three gaps and one opportunity, each with a short label and one supporting metric.

---

**Slide 6 — Quick Wins and 30-Day Priorities**
**Headline:** Ten actions this week; measurable results within 30 days
**Bullets:**
- Profile: [top 2 profile quick wins]
- Content: [top 2 content quick wins]
- Community: [top quick win for community management]
- 30-day target: [one measurable metric to improve — e.g. engagement rate from X% to Y%]
**Speaker Notes:** Emphasise that quick wins are low-cost and executable without additional budget. Set a 30-day check-in to review progress. Reference the SMART objectives framework (Chaffey, 2024) — the 30-day target should be specific and measurable.
**Visual Direction:** Prioritised checklist layout. Use a simple table: Action / Platform / Effort / Impact.

---

## Quality Criteria

- Every active platform has a completed audit table; no platform is skipped without an explanation
- Profile completeness and content quality scores are justified with specific observations, not assigned without evidence
- Competitor benchmarking identifies at least one concrete gap the client can exploit — not a generic observation
- Quick wins list contains exactly 10 items, sequenced by effort and impact, covering all four categories
- Deck outline follows the exact format from CLAUDE.md with all five fields (Headline, Bullets, Speaker Notes, Visual Direction) completed for every slide
- Estimated engagement rates are clearly labelled as estimates; the calculation method is documented
- Data sources are noted throughout; no claim is presented as measured fact unless account access was provided
- British English spelling throughout; tone follows the `east-african-english` skill

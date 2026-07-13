---
name: 10-content-pillars
description: "Use when defining three to five audience-linked themes before calendar production. Produces content pillar map and reference card; use `11-content-calendar` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Content Pillars Generator

Produce two outputs: (1) a full content pillar set with detailed guidance per pillar, and (2) a one-page content pillar reference card for the social media manager. Apply the `east-african-english` skill for tone throughout. Do not generate pillar content until all Required Input has been confirmed.


<!-- dual-compat-start -->
## Use When

- Use this skill for defining three to five audience-linked themes before calendar production.
- Confirm that `11-content-calendar` is not the closer route before proceeding.

## Do Not Use When

- Use `11-content-calendar` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Approved personas, voice guide, objectives and content evidence | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Content pillar map and reference card | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified content pillar map and reference card. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Approved personas, voice guide, objectives and content evidence is current and attributable | Produce the full content pillar map and reference card and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `11-content-calendar` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `11-content-calendar` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the content pillar map and reference card, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the content pillar map and reference card without approved personas. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `11-content-calendar` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified approved personas, the skill produces a content pillar map and reference card with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

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
- **Primary business goal** — the single most important business outcome for the next 90 days
- **Platforms in scope** — list all active platforms (default: Facebook, Instagram, WhatsApp)
- **Brand tone** — the three tone words confirmed in `04-brand-voice-intake`
- **Country/city** — defaults to Kampala, Uganda

---

## Frameworks to Apply

Apply both frameworks to every pillar. Cite on first use.

**10-4-1 Rule** (Bodnar and Cohen, 2012): For every 15 posts across all pillars, 10 must share others' content or provide general value with no brand agenda, 4 must share original brand content, and 1 must be a direct promotional post. This ratio applies across the full content mix — not per pillar individually.

**Hero / Hub / Hygiene Model** (YouTube/Google): Assign each pillar its dominant content tier:
- **Hero** — high-effort, high-reach content: campaign launches, major announcements, brand films, milestone celebrations
- **Hub** — regular, expected content that builds community: weekly series, recurring formats, Q&A, behind-the-scenes
- **Hygiene** — always-on, search-driven content: FAQs, how-to posts, product information, price lists, service explainers

Most pillars will contain a mix of tiers. Assign the tier that represents the majority of content within that pillar.

---

## Content Type Taxonomy (Handley, 2012)

Within each pillar, use these five content types to vary the tone and purpose of posts. Apply at least three of the five within any pillar to prevent the content from feeling monotonous.

| Type | Metaphor | What it is | When to use |
|---|---|---|---|
| **Raisin Bran** | The everyday staple | Practical, useful, how-to content the audience reaches for regularly | Daily tips, FAQs, product info, process guides — the backbone of the content mix |
| **Spinach** | Good for you, earns respect | Thought leadership; authoritative, substantive content that positions the brand as the expert | In-depth guides, data-driven posts, opinion pieces, industry analysis |
| **Roasts** | Takes effort, worth it | Major research projects, reports, case studies, or in-depth content requiring real investment | Quarterly; anchor pieces that drive shares, press mentions, and backlinks |
| **Tabasco** | Fires up a reaction | Deliberately controversial or provocative content designed to generate debate | Sparingly — when a clear, defensible position exists on a real industry debate |
| **Chocolate Cake** | Irresistible and shareable | Fun, light, entertaining content the audience shares for joy — memes, behind-the-scenes, celebrations | Weekly or fortnightly; essential for maintaining audience affection alongside serious content |

**Rule of thumb:** Most content calendars should be 50% Raisin Bran (useful daily), 25% Spinach (authoritative), 15% Chocolate Cake (entertaining), and 10% split between Roasts and Tabasco.

---

## Step 1: Determine the Number of Pillars

Recommend 3 pillars for small businesses posting 3–4 times per week; 4 pillars for medium businesses posting 5–7 times per week; 5 pillars for brands with a full content team or agency support. Explain the recommendation briefly before listing the pillars.

---

## Step 2: Generate Each Pillar

For each pillar, produce all eight elements below. Use the pillar name as the section heading.

### 1. Pillar Name
2–4 words. Make it memorable and specific to the client's brand — not generic (avoid names like "Education" or "Tips"). Use the client's industry language.

### 2. Purpose Statement
One sentence. State why this pillar exists for this specific client — what audience need it meets and how it supports the primary business goal.

### 3. Hero / Hub / Hygiene Tier Assignment
State the dominant tier and explain in one sentence why most content in this pillar falls there. Note whether the pillar also draws on a secondary tier.

### 4. Example Post Types
List 5 specific post formats that sit within this pillar. Be precise: do not write "educational posts" — write "a three-slide carousel explaining the difference between [Product A] and [Product B]".

### 5. Percentage of Content Mix
State the percentage of total posts this pillar should represent. All pillars must total exactly 100%. Explain the weighting logic briefly (e.g., "This pillar carries 35% because the primary goal is lead generation and this pillar drives the most direct enquiries.").

### 6. Platforms It Suits Best
List 2–3 platforms from the client's active set and explain in one sentence per platform why this pillar works there. Reference Uganda/EA platform behaviour where relevant.

### 7. Ten Starter Content Ideas
List 10 specific, ready-to-brief content ideas within this pillar. Each idea must include: the format (post, reel, carousel, story, WhatsApp broadcast, etc.), the subject, and the intended action or feeling it creates. These must be specific to the client's industry and audience — not reusable across any client.

### 8. What NOT to Post
List 4–5 clear boundaries that keep this pillar focused and on-brand. Examples: "Do not turn this pillar into a sales channel — no pricing or CTAs", "Do not share content that has not been fact-checked even if it is topical."

---

## Step 3: Content Pillar Map

After all individual pillar sections, produce a summary table:

| Pillar Name | Dominant Tier | % of Mix | Best Platforms | Primary Purpose |
|---|---|---|---|---|
| [Name] | Hero / Hub / Hygiene | [%] | [Platforms] | [One sentence] |

All percentages must total 100%.

---

## Step 4: Content Pillar Reference Card

Generate immediately after the pillar map. This is a one-page summary formatted for daily use by the social media manager. Include:

**[Client Name] — Content Pillar Reference Card**

| Pillar | % | 3 Key Content Ideas | Tier |
|---|---|---|---|
| [Pillar 1 name] | [%] | Idea 1 / Idea 2 / Idea 3 | Hub |
| [Pillar 2 name] | [%] | Idea 1 / Idea 2 / Idea 3 | Hygiene |
| [Pillar 3 name] | [%] | Idea 1 / Idea 2 / Idea 3 | Hero |

**Posting ratio reminder (10-4-1 rule):** For every 15 posts — 10 share value or others' content, 4 are original brand content, 1 is promotional. Check your mix weekly.

**Brand voice reminder:** [Tone word 1] · [Tone word 2] · [Tone word 3]

**Platforms in scope:** [List with primary use note per platform]

**This week's check:** Before publishing any post, ask: Which pillar does this belong to? Does it match the correct tone? Does it serve the audience, not just the brand?

---

> **Consultant note — 10-4-1 rule in practice:** The 10-4-1 rule is a ratio, not a rigid weekly schedule. If the client posts 5 times per week, they will not hit 10:4:1 in a single week — the ratio applies across a rolling two-to-three week period. Track it monthly. In Uganda/EA markets, audiences respond strongly to value-first content; skewing toward the "10" (shared value) builds trust faster than promotional content. Reserve the "1" promotional post for the highest-impact offer or announcement that week.

---

## The 8 Imprints Rule — Why Frequency Matters

*Pinskey (1997)*

A prospect typically needs to encounter a brand or business name **8 times** before they will take action.

This is why content pillars and content frequency are not cosmetic — they are the engine of conversion.

**What counts as an imprint:**
- A social media post seen and processed
- A direct message received
- A referral conversation heard
- A brochure read
- An email opened
- A website visited
- A sign or poster noticed
- A face-to-face meeting held

**Implication for content pillars:** A single pillar producing once-monthly content is generating roughly 12 imprints per year — just above the minimum threshold. Content pillars that produce weekly content generate 52 imprints per year — making conversion significantly more likely.

**When presenting content pillars to a client:** use the 8 Imprints Rule to justify frequency recommendations. Posting three times per week is not vanity — it is the minimum required to reliably cross the threshold from awareness to action.

**Compatible reference:** The 10-4-1 rule (Bodnar and Cohen, 2012) defines the *type* of content across 15 posts; the 8 Imprints Rule explains *why* those 15 posts are necessary.

---

## Quality Criteria

- All pillar percentages total exactly 100% — no rounding errors or unexplained gaps
- Every starter content idea is specific to the client's industry and audience; no idea could belong to a different client unchanged
- The 10-4-1 ratio is applied to the full content mix and the consultant note explaining it is included and contextualised for Uganda/EA
- Hero/Hub/Hygiene tier is assigned to each pillar with a one-sentence rationale — not just labelled
- Platform suitability notes reference Uganda/EA platform behaviour (e.g., WhatsApp for trust-building, Facebook for reach, Instagram for aspirational audiences)
- The reference card fits a single page and is immediately usable without reading the full pillar set
- British English spelling is used throughout; no American spellings (programme not program, colour not color, organise not organize)
- What NOT to post boundaries are specific and actionable — not generic advice the team will ignore

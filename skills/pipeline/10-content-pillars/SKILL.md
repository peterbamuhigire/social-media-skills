---
name: 10-content-pillars
description: Use when a brand's feed lacks direction and it needs three to five standing themes linked to audience needs and business goals, with each theme's percentage of the mix; produces the content pillar map and one-page reference card; not for scheduling posts across the coming months (use `11-content-calendar`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Content Pillars Generator

Produces two outputs: a full content pillar set with detailed guidance per pillar, and a one-page content pillar reference card for the social media manager. Apply the `east-african-english` skill for tone throughout.

<!-- dual-compat-start -->
## Use When

- Posting feels random and the client wants a few recurring themes that link audience needs to business goals.
- The team needs to know what percentage of output each theme takes and which platforms suit it best.
- Each theme needs hero, hub and hygiene roles, example post types, starter ideas and what not to post.
- The social manager wants a one-page reference card to check every post against.

## Do Not Use When

- `11-content-calendar` for dated posts across the next 90 days.
- `content-ideas` for a large bank of individual post ideas.
- `05-social-media-strategy` when platforms and goals are not yet decided.
- Stop before setting themes while the audience or brand voice is unapproved; list what must be confirmed first.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry and country/city | Client brief or `01-client-brief` | Yes | Default the location to Kampala, Uganda; ask for the rest. |
| Named audience personas (minimum two) | `03-audience-personas` | Yes | Stop; list the personas that must be approved before themes are set. |
| Primary business goal for the next 90 days | Client lead | Yes | Ask for the single most important outcome; do not weight pillars without it. |
| Platforms in scope | Channel plan or client | Yes | Default to Facebook, Instagram and WhatsApp and label them provisional. |
| Three confirmed brand tone words | `04-brand-voice-intake` | Yes | Stop the reference card's voice line; route to `04-brand-voice-intake`. |
| Posting frequency and team capacity | Client lead | Yes | Recommend 3 pillars and state the assumption. |

## Workflow

1. Confirm the intake answers in [pillar-build-method](references/pillar-build-method.md) § Intake questions; stop while the personas or brand voice are unapproved and list what must be confirmed first.
2. Recommend the number of pillars from posting frequency and team size, and explain the recommendation briefly.
3. Write each pillar with all eight elements: name, purpose statement, Hero/Hub/Hygiene tier, five example post types, percentage of the mix, best platforms, ten starter ideas and what not to post.
4. Vary each pillar across at least three of Handley's five content types, and apply the 10-4-1 ratio (Bodnar and Cohen, 2012) across the full mix, not per pillar.
5. Build the content pillar map; check the percentages total exactly 100%.
6. Produce the one-page reference card with the 10-4-1 reminder, brand voice line, platforms and the pre-publish check, plus the consultant note on the ratio; use the 8 Imprints Rule (Pinskey, 1997) to justify frequency.
7. Check against the quality standards; correct any failing pillar and rerun the check.
8. Run the anti-slop ship gate and hand the pillars to `11-content-calendar` and the client lead for approval.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Full content pillar set (eight elements per pillar) | Client lead; `11-content-calendar` | Every pillar has all eight elements, specific to the client's industry and audience. |
| Content pillar map | `11-content-calendar`; `09-campaign-strategy` | One row per pillar with tier, % of mix, best platforms and purpose; percentages total 100%. |
| One-page content pillar reference card | Social media manager | Fits a single page and is usable without reading the full pillar set. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Input trace | Table: persona, goal, tone words and platforms, with source and approval date | Each pillar's purpose names the persona need and goal it serves; unapproved inputs are marked `not assessed`. |
| Mix arithmetic | Pillar map total and 10-4-1 note | Percentages sum to exactly 100% and the ratio is stated for the full mix. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority.

## Degraded Mode

Without approved personas or the confirmed brand voice, return the narrowest qualified result and mark the affected checks `not assessed`. A recommended pillar count and draft pillar names and purposes can still be delivered, labelled as awaiting approval.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Small business posting 3–4 times per week | Recommend 3 pillars. | Themes spread too thin to sustain. |
| Medium business posting 5–7 times per week | Recommend 4 pillars. | Too few themes for the volume. |
| Brand with a full content team or agency support | Recommend 5 pillars. | Under-using production capacity. |
| A pillar mixes Hero, Hub and Hygiene content | Assign the tier that represents the majority of its content and note any secondary tier. | A label with no production meaning. |
| The client posts 5 times per week and cannot hit 10:4:1 in a week | Apply the ratio across a rolling two-to-three week period and track it monthly. | False failures and a rigid schedule. |
| The mix skews promotional in a Uganda/EA market | Skew toward the "10" (shared value) and reserve the "1" for the week's highest-impact offer. | Slower trust-building with value-first audiences. |
| The work is dated posts or a large idea bank | Route to `11-content-calendar` or `content-ideas` and hand over the approved pillars. | Neighbour collision and duplicated work. |

## Quality Standards

- All pillar percentages total exactly 100%, with no rounding errors or unexplained gaps.
- Every starter content idea is specific to the client's industry and audience; no idea could belong to a different client unchanged.
- The 10-4-1 ratio is applied to the full content mix and the consultant note explaining it is included and contextualised for Uganda/EA.
- The Hero/Hub/Hygiene tier is assigned to each pillar with a one-sentence rationale, not just labelled.
- Platform suitability notes reference Uganda/EA platform behaviour (e.g., WhatsApp for trust-building, Facebook for reach, Instagram for aspirational audiences).
- The reference card fits a single page and is immediately usable without reading the full pillar set.
- British English spelling is used throughout; no American spellings (programme not program, colour not color, organise not organize).
- What NOT to post boundaries are specific and actionable, not generic advice the team will ignore.

## Anti-Patterns

- Naming pillars "Education" or "Tips". Fix: use 2–4 memorable words in the client's industry language.
- Writing "educational posts" as a post type. Fix: name the format and subject, for example a three-slide carousel comparing two products.
- Filling a pillar with one content type. Fix: use at least three of the five types (Raisin Bran, Spinach, Roasts, Tabasco, Chocolate Cake).
- Using Tabasco content without a defensible position. Fix: use it sparingly, only on a real industry debate.
- Treating posting frequency as vanity. Fix: explain with the 8 Imprints Rule that three posts a week is the minimum to cross from awareness to action.
- Setting themes before the audience or voice is approved. Fix: list what must be confirmed and stop.

## References

- [Content pillar build method](references/pillar-build-method.md): read when asking the intake questions, applying the frameworks and content-type taxonomy, writing the eight pillar elements, or building the pillar map, reference card and 8 Imprints justification.
- [`11-content-calendar`](../11-content-calendar/SKILL.md): read when the approved pillars need turning into dated posts.
- [`content-ideas`](../../content-writing/content-ideas/SKILL.md): read when a large bank of individual post ideas is needed.
- [`05-social-media-strategy`](../05-social-media-strategy/SKILL.md): read when platforms and goals are not yet decided.
- [`03-audience-personas`](../03-audience-personas/SKILL.md) and [`04-brand-voice-intake`](../04-brand-voice-intake/SKILL.md): read when personas or tone words are missing.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

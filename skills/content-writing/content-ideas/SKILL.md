---
name: content-ideas
description: Use when a brand is stuck on what to post or write about and wants fresh angles; produces a prioritised bank of 30 post ideas with platform, format and pillar, recurring evergreen series, and blog or article topic briefs with keywords and buyer stage; not for scheduling ideas across dates (use `11-content-calendar`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Content Ideas Generator

Generates a bank of 30 specific content ideas mapped to the client's pillars and platforms, plus 5 evergreen series, or a blog topic list with briefs. Ideas must be specific to the client's industry and audience, not generic social media advice restated.

<!-- dual-compat-start -->
## Use When
- We have run out of things to post and need a bank of ideas mapped to our pillars and platforms.
- We want a few recurring series the team can repeat every week without starting from scratch.
- The client needs blog or article topics with short briefs, a target keyword and buyer stage, sorted into SEO drivers, authority builders and thought leadership.
- A slow month, launch or season needs new angles from ideation frameworks rather than recycled posts.

## Do Not Use When
- `11-content-calendar` for putting approved ideas on dates with owners and production cues.
- `blog-writer` for writing a chosen article in full.
- `playbook-viral-content-design` for engineering a single piece for shareability.
- Stop before presenting trends, statistics or competitor examples as fact without a source; mark unsourced ideas as hypotheses.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry, country/city and primary goal (awareness, community, sales, recruitment) | Client brief | Yes | Default the market to Uganda/East Africa; ask for the goal before generating. |
| Target audience (demographics, interests, location, key concerns) | Client or audience research | Yes | Stop and ask; ideas without an audience situation are generic. |
| Active platforms | Client or channel plan | Yes | Ask; platform minimums cannot be set without them. |
| Content pillars with percentages | `10-content-pillars` output | Yes | Route to `10-content-pillars`; label any working mix provisional. |
| Brand tone (3 words) | `04-brand-voice-intake` | No | Take tone from the client's recent posts and flag it as assumed. |
| Upcoming campaigns, launches and seasonal dates; any trend, statistic or competitor example used | Client; traceable source | Conditional | Use the Uganda/EA seasonal hooks; mark unsourced trend ideas as hypotheses. |

The full intake list is in the [social idea build method](references/social-idea-build-method.md#required-input).

## Workflow

1. Confirm whether the brief is for social post ideas or a blog/article programme; for 15–25 blog topic ideas with 200-word hybrid summaries saved to `docs/blogs/topics.md`, follow [blog and article topic briefs](references/blog-and-article-topic-briefs.md) instead of the 30-idea social table. Route to `caption-writer` if finished copy is wanted.
2. Inventory the supplied facts, pillars, platforms and sources; stop if the goal, audience or active platforms are unknowable.
3. Apply all 8 idea generation frameworks from the [social idea build method](references/social-idea-build-method.md#8-idea-generation-frameworks), each contributing at least 2–3 ideas.
4. Fill the 30-idea table (number, idea title, platform, content type, pillar, 2-sentence brief) against the platform, content-type, pillar and category distribution rules.
5. For each idea, name the audience situation, narrative job, emotional or practical tension, proof/source need, choice or CTA, format/readability risk, and the learning signal it can generate.
6. Build 5 evergreen series (name, concept, frequency, posting day, first episode idea) tailored to the client's industry, platform mix and tone.
7. Check the set against the quality standards and the `anti-ai-slop` gate; correct any generic, unsourced or mis-distributed idea and rerun the distribution count.
8. Deliver the table and series with the source register, hypotheses and the next approval step for `11-content-calendar`.

## Distribution minimums

| Rule | Minimum |
|---|---|
| Ideas per platform | Facebook 5; Instagram 5; LinkedIn 4 (if active); WhatsApp 3 (broadcast or Status); TikTok 4 (if active); YouTube 2 (if active). With fewer than 5 platforms, redistribute so every active platform has at least 4. |
| Content types | At least one each of image post, short-form video, carousel, Story or Status, poll or question, text post, WhatsApp broadcast, Reel or TikTok. |
| Pillars | Proportional to the percentages: in 30 ideas a 40% pillar gets about 12, a 20% pillar about 6. |
| Categories | Educational, entertaining or relatable, promotional, behind the scenes, social proof, community, seasonal or cultural hook, UGC prompt. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| 30-idea table | Client lead; `11-content-calendar` | Every row has a specific, vivid title and a 2-sentence brief saying what the content looks like and why it will work for this audience; minimums met. |
| 5 evergreen series | Client lead; production team | Each has a brandable name, 2-sentence concept, frequency, posting day and a fully described first episode. |
| Blog topic list with briefs, when requested | `blog-writer`; `12-website-content-plan` | Built with the blog topic-brief procedure; each topic carries keyword and buyer stage. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Idea-to-source register | Inline table | Every trend, statistic and competitor example traces to a dated source or is labelled a hypothesis. |
| Distribution count | Table: platform, content type, pillar, category, framework | Shows each minimum met, or the gap named. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Featuring a customer, partner or influencer idea needs their consent before production.

## Degraded Mode

Without confirmed pillars, audience or active platforms, return the narrowest qualified result and mark the affected checks `not assessed`. A framework-led idea bank for the known platforms can still be delivered, labelled provisional until the pillars are approved.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The brief asks for blog or article topics rather than social posts | Switch to the blog topic-brief procedure and its companion references. | Forcing article topics into a social post table. |
| A client uses fewer than 5 platforms | Redistribute proportionally so every active platform has at least 4 ideas. | Thin coverage on the platforms the client actually uses. |
| A cultural or religious occasion does not genuinely connect to what the client does | Leave it out; handle Martyrs Day (3 June) respectfully and never promotionally. | Forced, inauthentic or offensive seasonal content. |
| A seasonal date varies (Eid al-Fitr, Eid al-Adha, harvests) | Confirm the year's date before briefing, or mark it `not assessed`. | Greetings on the wrong day. |
| An idea rests on a trend, statistic or competitor example without a source | Label it a hypothesis and name the evidence needed. | Presenting unsourced claims as fact. |
| An idea features a customer, story or result | Use only real, consented material; never invent customer stories, results, permissions, cultural facts or platform behaviour. | Fabricated social proof. |

## Quality Standards

- All 30 ideas are specific to the client's industry, audience and location; no generic filler or restated social media advice.
- Every active platform receives its minimum allocation and all content types are represented across the 30.
- All 8 idea generation frameworks contribute at least 2 ideas each.
- Pillar distribution reflects the percentages provided in the content pillars input.
- Seasonal hooks use Uganda/EA dates, not US/UK calendar defaults.
- Evergreen series are named, specific and immediately actionable, with the first episode fully described.
- British English throughout; the set passes the `anti-ai-slop` ship gate, and a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns

- Generating a list of hooks without a job, audience situation, proof or next action. Fix: add the missing narrative and measurement fields or narrow the idea set.
- Writing ideas before the goal and audience are known. Fix: stop and obtain the missing brief fields.
- Using US/UK calendar defaults for seasonal hooks. Fix: use the Uganda/EA occasions table and confirm variable dates.
- Restating generic series formats such as "Ask [Brand Name]" unchanged. Fix: tailor all 5 series to the client's industry, platform mix and tone.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. Fix: verify it or qualify/remove it.
- Chasing a trend directly. Fix: show what the trend means for the audience, keeping the brand current without being reactive or superficial.

## References

- [Social idea build method](references/social-idea-build-method.md): read when asking the intake questions, applying the 8 frameworks and seasonal hooks table, laying out the table or building evergreen series.
- [Blog and article topic briefs](references/blog-and-article-topic-briefs.md): read when the client needs blog or article topic ideas and briefs rather than social post ideas.
- [Ideation frameworks](references/ideation-frameworks.md): read when the blog topic-brief procedure selects its 5–7 methods.
- [Content formats](references/content-formats.md): read when choosing the format for a blog topic.
- [Idea sources and series](references/idea-sources-and-series.md): read when blog ideation should produce clusters and repeatable series.
- [Source buckets and series](references/source-buckets-and-series.md): read when platform ideas must feel fresh without becoming random.
- [Headline and hook families](../../advertising/ad-copy-and-hook-lab/references/headline-and-hook-families.md): read when writing headlines for blog topics (replaces the missing `headline-mastery.md` pointer).
- [`caption-writer`](../caption-writer/SKILL.md): read when routing is unclear; it is the nearest neighbour.
- [`10-content-pillars`](../../pipeline/10-content-pillars/SKILL.md): read when pillars are missing or disputed.
- [`11-content-calendar`](../../pipeline/11-content-calendar/SKILL.md): read when the approved ideas need dates and owners.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when writing idea titles and briefs.
<!-- dual-compat-end -->

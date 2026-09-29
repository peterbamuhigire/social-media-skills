---
name: caption-writer
description: Use when an approved brief needs publish-ready social captions, first lines and hashtags for Instagram, Facebook, TikTok, LinkedIn, X or WhatsApp; produces caption sets in three lengths and a hashtag strategy with tags to avoid; not for paid ad headlines or hooks (use `ad-copy-and-hook-lab`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Caption Writer

Writes organic social captions in three labelled variations (Short, Medium, Long) with distinct hooks, one call to action and platform-correct hashtags, for client approval before scheduling. Apply British English and `east-african-english` throughout.

<!-- dual-compat-start -->
## Use When
- The post, photo or video is approved and we need the organic post copy written for this week on Instagram, Facebook, TikTok, LinkedIn, X or a WhatsApp broadcast, not paid ads.
- We want short, medium and long options with different opening lines so the client can choose.
- Our posts need a hashtag strategy: branded, niche, community and location tags per platform, how many to use and which banned or risky tags to avoid.
- Our captions come out generic or AI-sounding and need rewriting in the brand voice with a clear call to action.

## Do Not Use When
- `ad-copy-and-hook-lab` for paid ad headlines, primary text and hooks.
- `email-copywriter` for newsletters and promotional emails.
- `content-ideas` for deciding what to post in the first place.
- Stop before posting or scheduling to a live account; deliver the drafts for client approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client or brand name, industry and country/city | Client brief | Yes | Default the market to Uganda/East Africa; ask for the brand and industry before writing. |
| Platform and content type (photo, video, carousel, text post, Reel, Story, broadcast) | Content calendar or account manager | Yes | Stop and ask; conventions differ too much by platform to guess. |
| Topic, key message (one sentence each), primary goal and one CTA | Approved post brief or `11-content-calendar` row | Yes | Draft the key message from the brief, state the assumed CTA in the post notes and ask for confirmation before scheduling. |
| Tone, mandatory keywords, product names or campaign lines, and banned vocabulary | `04-brand-voice-intake` or client | No | Use the brand's published posts as the tone sample and apply the engine's banned-word list. |
| Visual, offer facts, prices, results and permissions | Client source pack or authorised owner | Conditional | Hold the claim or visual; never invent names, prices, results or consent. |
| Standing hashtag set for the client | [Hashtag and keyword tagging](references/hashtag-and-keyword-tagging.md) output | No | Build the set from the East African community lists for this post and recommend a full strategy. |

The full intake list is in the [caption build method](references/caption-build-method.md#required-input).

## Workflow

1. Confirm the platform, content type, goal and approval boundary; route to `email-copywriter` for email or to `ad-copy-and-hook-lab` for paid ads.
2. Inventory the supplied facts, visuals, permissions and missing inputs; stop if the goal, audience or authority to post is unknowable.
3. Apply the chosen platform's conventions from the [caption build method](references/caption-build-method.md#platform-specific-rules); do not blend conventions across platforms.
4. Write three variations (Short, Medium, Long), each with a distinct hook strategy (for example bold statement, question-led, story-led), one CTA and a platform-appropriate hashtag set drawn from the client's standard set or the East African community lists.
5. For premium, executive, high-ticket or trust-sensitive posts apply `premium-commercial-writing`; for persuasion-led posts also apply its buyer-psychology reference (belief sequence, proof rules, readiness-matched CTA).
6. Check each caption against the audience's situation, narrative job, first-line information hierarchy, readability, one-action CTA, accessibility needs (alternative description) and the factual and permission register; correct any failure and rerun the check.
7. Run the `anti-ai-slop` humanising passes and the direct-marketing ethics filter for selling captions, then deliver in the output format with post notes (placement, timing, ambiguities to confirm before scheduling).

## Platform conventions at a glance

| Platform | Length | Hashtags | Key rule |
|---|---|---|---|
| Instagram | 125–150 characters for reach; up to 300 words for education or story | Up to 5, in the caption (Instagram cap, register `INSTAGRAM-HASHTAG-LIMIT-PRIMARY`) | Hook inside the first 125 characters; no more than 2 emojis in the hook line. |
| Facebook | 40–80 characters for reach; up to 250 words for story or event | 1–3 maximum | Warm, neighbourly; put any link in the caption text. |
| LinkedIn | 150–300 words for engagement; 50–100 words for reach | 3–5, industry-relevant | First 2 lines carry the post; 0–2 purposeful emojis. |
| TikTok | 100–150 characters | 3–5 (niche, trending or broad, branded) | CTA drives comments. |
| WhatsApp broadcast | Under 150 words | None | Warm personal greeting; one action only. |
| X / Twitter | 240–280 characters; thread for longer (1/, 2/) | 1–2, woven into the text | Open with a take or observation, not an announcement. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Three labelled caption variations (Short, Medium, Long) per request | Client approver; scheduler | Each differs in length and hook strategy; one CTA each; hashtag count and placement match the platform. |
| Post notes | Client approver | Placement, timing and every assumption (for example an assumed CTA) are listed for confirmation before scheduling. |
| Standing hashtag strategy document, when requested | Social team | Built with the hashtag reference: tiered sets, tags to avoid and a monthly review. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Claim, visual and permission register | Inline table | Every price, result, quotation and visual has a source or permission status, or is held. |
| Release checklist | Checklist against the quality standards | Unavailable checks (native-language review, alternative description) are marked `not assessed`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Drafting is permitted within the supplied brief; posting or scheduling to a live account needs separate approval.

## Degraded Mode

Without a confirmed platform, key message or CTA, return the narrowest qualified result and mark the affected checks `not assessed`. Hook options and a draft caption for the most likely platform can still be delivered, with every assumption listed in the post notes.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The platform and content type are confirmed | Apply only that platform's length, hook, hashtag and emoji rules. | Copy that could be pasted unchanged onto any channel or brand. |
| The client needs a standing hashtag strategy (branded, niche, community and awareness tiers, tags to avoid, monthly review) rather than one caption's tags | Build it with [hashtag-and-keyword-tagging](references/hashtag-and-keyword-tagging.md), then draw each caption's set from its standard set. | Generic, untargeted tag lists pasted under every post. |
| The brief omits the CTA or contains an ambiguity | Assume the most likely single action, flag it in the post notes and ask for confirmation before scheduling. | A post scheduled with an action the client never chose. |
| A price, result, quotation or visual lacks a source or permission | Hold that element or leave a visible placeholder in the register. | Fabricated claims or unauthorised use of an image or person. |
| The post supports a premium offer, executive audience, high-ticket service or trust-sensitive category | Apply `premium-commercial-writing`: create value, show proof or judgement, and ask for a next step without sounding desperate or discount-led. | Discount-led copy that cheapens the offer. |
| The caption sells | Use readiness-matched CTAs and run the direct-marketing ethics filter; never use fake scarcity, fabricated consensus or unsupported "brain" claims. | Manipulative copy and downstream refunds or complaints. |
| The post uses AI-generated content | Route it through the disclosure and human-review rules. | Undisclosed AI content and platform or regulatory action. |

## Quality Standards

- Each variation genuinely differs in length and approach; three different hook strategies, not three versions of one opener, and the hook works as a standalone sentence.
- One CTA per caption, clear and specific, matching platform convention.
- Hashtag count and placement match the platform rules.
- British English (organisation, colour, programme, behaviour, analyse, recognise, centre, enquiry); active voice; no banned vocabulary or filler phrases from the [caption quality standards](references/caption-build-method.md#caption-quality-standards).
- Tone matches the brand descriptor, or `04-brand-voice-intake` where provided; names, figures, quotations and platform rules are verified before use.
- Premium or high-ticket captions show specificity, proof and value before asking for action; the sequence runs hook, proof, choice, consequence in plain language rather than decorative persuasion.
- Output follows the labelled format, ready to copy, and passes the `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns

- Treating a strong hook as sufficient when the audience cannot understand the offer or next step. Fix: rewrite the information hierarchy and test the CTA on the target mobile format.
- Using a visual or claim without permission, alternative description or source status. Fix: stop the post or supply the missing evidence.
- Reusing the same hook across the three variations, or padding one caption into three lengths. Fix: give each variation its own structure and tone.
- Blending platform conventions (LinkedIn buzzwords, stacked hashtags on X, hashtags on WhatsApp). Fix: apply only the chosen platform's rules.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. Fix: verify it or qualify/remove it.
- Publishing, scheduling or changing a live account from drafting authority alone. Fix: obtain explicit action-specific authority and retain the approval record.

## References

- [Caption build method](references/caption-build-method.md): read when asking the intake questions, applying full platform rules, picking East African hashtag communities, laying out the output or reviewing the Nakibuuka Kitchen worked example.
- [Hashtag and keyword tagging](references/hashtag-and-keyword-tagging.md): read when the client needs a full hashtag strategy document, tiered tag sets, a tags-to-avoid list or a monthly hashtag performance review.
- [CTA and platform hooks](references/cta-and-platform-hooks.md): read when caption performance depends on stronger openers, cleaner hooks or better CTA wording.
- [Human, professional phrase bank](../references/human-professional-phrase-bank.md): read when shaping post and ad sentence patterns (three-line power paragraph).
- [Direct-marketing ethics filter](../references/direct-marketing-ethics-filter.md): read before releasing any selling caption or ad; the screen is mandatory.
- [Buyer psychology and social selling](../premium-commercial-writing/references/buyer-psychology-and-social-selling.md): read when the post is persuasion-led.
- [`premium-commercial-writing`](../premium-commercial-writing/SKILL.md): read when the post supports a premium, executive, high-ticket or trust-sensitive offer.
- [`email-copywriter`](../email-copywriter/SKILL.md): read when routing is unclear; it is the nearest neighbour.
- [`east-african-english`](../../language/east-african-english/SKILL.md): read when calibrating tone and British spelling for East African audiences.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting and before client delivery.
<!-- dual-compat-end -->

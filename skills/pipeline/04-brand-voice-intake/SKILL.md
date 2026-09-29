---
name: 04-brand-voice-intake
description: Use when a brand needs to sound and look consistent on social, from tone and vocabulary to emoji, hashtag and image rules, or the team wants a social media style guide; produces the brand voice guide, visual identity brief and style guide; not for defining what makes the brand distinct (use `ecommerce-brand-differentiation`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Brand Voice and Visual Identity Brief Generator

Produces the definitive tone and identity reference for the client account: written voice, platform adjustments, vocabulary, emoji and hashtag policy, and visual identity direction for briefing a designer. Apply the `east-african-english` skill to this document's own prose.

<!-- dual-compat-start -->
## Use When

- Every writer on the team uses a different register and the client wants one agreed tone with words to use and avoid.
- Tone needs adjusting per platform, for example warmer on Instagram and more formal on LinkedIn, without losing the brand.
- A designer needs a visual direction brief covering colours, imagery, typography cues and what the brand must never look like.
- Several people post for the brand and each does it differently: the team needs a social media style guide or rulebook covering emojis, hashtags, photo and video standards, who approves posts, when to pause posting after bad news, and grammar, UGX and date formats.

## Do Not Use When

- `ecommerce-brand-differentiation` for positioning, naming and what sets the brand apart from rivals.
- `03-audience-personas` when the audience is not yet understood.
- `brand-voice-ai-training` for turning the approved voice into prompts and context blocks for AI tools.
- Stop before inventing brand values, logos or claims the client has not confirmed; mark them for approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Three brand tone adjectives (the client's own words) | Section 6 of the `01-client-brief` | Yes | Do not proceed; they are the foundation of all voice decisions. Ask for them. |
| Client name, industry, country / city | `01-client-brief` | Yes | Ask; city defaults to Kampala, Uganda if not specified. |
| Brand colours and fonts | `01-client-brief` Section 7 | Yes | Accept descriptive answers ("dark green and gold", "a bold sans-serif") and mark hex codes and font names as to confirm. |
| Brands admired (2–3) and brands not to sound like (3), each with a note | `01-client-brief` Section 6 | Yes | Ask; without them the avoid-list relies on industry clichés only and must say so. |
| Completed `03-audience-personas` | `03-audience-personas` output | If available | Draft tone without persona alignment and flag it for review once personas exist. |
| `brand-voice-ai-training` analysis note (ranked-source corpus, "what the author never does") | Prior run for this client | If available | Derive tone from the adjectives alone and label the Right/Wrong examples as inferred. |

## Workflow

1. Collect the inputs; stop if the three tone adjectives are missing and ask for them.
2. If `brand-voice-ai-training` has already been run for this client, pull its analysis note rather than re-deriving tone from adjectives alone.
3. Write Section 1: 4–6 tone attributes derived from the three adjectives, each with a definition and two Right and two Wrong examples, then the 5–7 sentence voice summary paragraph.
4. Write Section 2: platform tone adjustments for every platform the client is active on or has confirmed plans to use, rewriting the same sample announcement for each.
5. Write Sections 3–5: vocabulary to use and to avoid (10–15 items each), the platform-by-platform emoji policy, and 1–3 branded hashtags plus community and discovery hashtag guidance.
6. Write Section 6, the visual identity brief for a designer: photography direction, colour palette usage, typography guidance and image do's and don'ts. It does not produce design files.
7. Test the draft against the quality standards; correct any attribute that cannot be traced to an adjective or any example pair that differs only by an emoji, and rerun the affected sections.
8. Run the anti-slop ship gate and hand the guide to `05-social-media-strategy` and the content team; produce the operational style guide only when the client asks for it.

Section templates and wording: [voice-guide-section-templates](references/voice-guide-section-templates.md).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Brand voice guide (tone attributes, summary paragraph, platform adjustments, vocabulary, emoji policy, hashtags) | Everyone writing for the account; `05-social-media-strategy` | The definitive tone reference: client-specific, traceable to the three adjectives, actionable without further discussion. |
| Visual identity brief | The client's graphic designer or photographer | A practical written brief covering photography, colour roles, typography and image do's and don'ts. |
| Operational social brand style guide (on request) | Whoever runs the client's accounts | The nine sections in [social-brand-style-guide](references/social-brand-style-guide.md), reusing this skill's voice outputs. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Adjective-to-attribute trace | Table or note: adjective, derived attributes | A reader can trace each attribute to a client adjective. |
| Hashtag availability note | Note per branded hashtag | Records that the client was advised to search Instagram and TikTok before publishing. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. The guide's own prose follows `east-african-english`, but the brand voice being defined may differ from EA standard if the client specifies a different style.

## Degraded Mode

Without the client's three tone adjectives, return the narrowest qualified result and mark the affected checks `not assessed`. The input request, platform tone norms and the standard EA avoid list can still be delivered; tone attributes wait for the adjectives.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client needs an operational style guide for whoever runs its accounts, not only a voice guide and designer brief | Produce the nine-section guide in [social-brand-style-guide](references/social-brand-style-guide.md), reusing this skill's voice outputs. | Operators publishing without approval, pause or formatting rules. |
| A `brand-voice-ai-training` analysis note exists | Feed its ranked-source corpus and "what the author never does" finding into the Section 1 Right/Wrong examples and the Section 3 avoid-list. | Inferred opposites in place of real, source-derived material. |
| The client works in a professional sector | Make at least one attribute address the tension between the professional sector and the warmth expected in EA communication. | A voice that is either cold or unprofessional for the market. |
| The brand is "professional and authoritative" rather than "warm and approachable" | Use fewer emojis; state permitted, limited or not permitted for functional, expressive and decorative types per platform. | Ambiguous "use occasionally" policies. |
| A platform is not active or planned | Omit it from the platform adjustments and emoji table. | Padding the guide with irrelevant platforms. |
| The audience is not yet understood | Route to `03-audience-personas` and hand over the verified inputs already collected. | Tone decisions misaligned with persona messaging. |

## Quality Standards

- Tone attributes are derived logically from the client's three adjectives; a reader can trace the connection.
- Each attribute's "Right" and "Wrong" examples are distinct and clearly illustrate the difference, not variations on the same sentence.
- The brand voice summary paragraph is specific to this client; it cannot be applied to another client without rewriting.
- Platform tone adjustments show a genuine tonal shift between platforms using the same source message, not the same message with a different emoji.
- Vocabulary lists contain at least 3 items specific to the client's industry; generic EA professional vocabulary does not fill the list.
- Emoji policy is specific enough to act on without further discussion; ambiguous entries such as "use occasionally" are not acceptable.
- Visual identity brief is written as a practical designer brief, not as abstract brand theory; social graphics use a minimum 24px font size for mobile legibility.
- British English spelling throughout; tone of this document's own prose follows the `east-african-english` skill.

The branded-hashtag check is in the [section templates checklist](references/voice-guide-section-templates.md) (§ Checklist).

## Anti-Patterns

- Tone attributes that are synonyms of the adjectives ("Bold: bold"). Fix: write nuanced phrases such as "Bold in opinion, not in self-promotion".
- A voice summary that could fit any client. Fix: use the person-walking-into-a-room analogy with client-specific detail.
- Using hype words from the standard EA avoid list ("groundbreaking", "revolutionary", "game-changing", "amazing", "awesome", "unleash", "skyrocket"). Fix: include them in the avoid table and use plain, evidenced language.
- A WhatsApp message that opens with a promotional hook. Fix: lead with context and value, end with one call to action, maximum 3 sentences.
- Branded hashtags already in wide use. Fix: advise the client to search Instagram and TikTok before publishing, and keep the hashtag short, specific and consistent across platforms.
- Treating the visual brief as design output. Fix: write guidance for the designer; do not produce design files.

## References

- [Voice guide section templates](references/voice-guide-section-templates.md): read when writing any of the six sections, the Right/Wrong format, the platform rules or the colour and typography tables.
- [social-brand-style-guide](references/social-brand-style-guide.md): read when the client wants a complete social media style guide with approval workflow, content pause protocol, emoji, hashtag, media and grammar rules.
- [`03-audience-personas`](../03-audience-personas/SKILL.md): read when personas are missing or tone must align with persona messaging notes.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the example phrasing and vocabulary lists.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

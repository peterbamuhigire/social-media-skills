---
name: 04-brand-voice-intake
description: Develops the client's social media brand voice guide and visual identity brief — a single standalone document covering tone attributes, platform tone adjustments, vocabulary, emoji policy, hashtag identity, and photography and design direction. Invoke after the 01-client-brief and 03-audience-personas are complete, and before any content writing, caption writing, or platform playbook work begins. This document is the tone reference every team member reads before writing anything for the client.
---
# Brand Voice and Visual Identity Brief Generator

Produce one standalone brand document. This is the definitive tone and identity reference for the client account. It covers written voice, platform adjustments, vocabulary, emoji and hashtag policy, and visual identity direction for briefing a designer. Apply the `east-african-english` skill for tone throughout this document's own prose — but note that the brand voice being defined may differ from EA standard if the client specifies a different style.

<!-- dual-compat:start -->
## Use when
- Develops the client's social media brand voice guide and visual identity brief — a single standalone document covering tone attributes, platform tone adjustments, vocabulary, emoji policy, hashtag identity, and photography and design direction. Invoke after the 01-client-brief and 03-audience-personas are complete, and before any content writing, caption writing, or platform playbook work begins. This document is the tone reference every team member reads before writing anything for the client.
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
- A structured onboarding, strategy, or planning document in markdown, ready to hand off to the next skill in the workflow.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask for the following before generating anything:

- **Client name and industry** — as recorded in the 01-client-brief
- **Three brand tone adjectives** — from Section 6 of the 01-client-brief; these are the client's own words
- **Brand colours and fonts** — hex codes and font names if available; descriptive if not (e.g. "dark green and gold", "a bold sans-serif")
- **Brands the client admires** — 2–3 brands with a note on what the client likes about each
- **Brands the client does NOT want to sound like** — 3 brands with a note on what to avoid
- **Country / city** — defaults to Kampala, Uganda if not specified
- **Completed 03-audience-personas** — provide as context if available; tone decisions should align with persona messaging notes

If the three tone adjectives are missing, do not proceed — they are the foundation of all voice decisions. Ask for them.

---

## Section 1: Brand Voice Guide

### Tone Attributes

Derive 4–6 tone attributes from the three client adjectives. Each attribute is a nuanced phrase that clarifies how the adjective applies in practice — not a synonym.

**Format for each attribute:**

---

**Attribute [N]: [Attribute phrase — e.g. "Warm but professional"]**

*Definition:* One sentence explaining what this means in practice for this brand. Be specific — do not write a dictionary definition.

*Right:*
- [Example phrasing that embodies this attribute — a real sentence or caption style]
- [Second example]

*Wrong:*
- [Example phrasing that violates this attribute — show where a writer could go astray]
- [Second example]

---

Repeat for all 4–6 attributes.

**Guidance on deriving attributes from adjectives:**
- A single adjective like "Bold" generates attributes such as "Bold in opinion, not in self-promotion" and "Confident without being aggressive"
- "Friendly" might generate "Friendly in tone, formal in grammar" for a professional services brand
- "Innovative" in an EA context might become "Forward-looking, but grounded in practical local reality"
- Ensure at least one attribute addresses the tension between the brand's professional sector and the warmth expected in EA communication

---

### Brand Voice Summary Paragraph

Write one paragraph (5–7 sentences) that the entire team reads before writing anything for this client. Synthesise all tone attributes into a coherent description of who this brand sounds like. Use the analogy of a person: if this brand were a person walking into a room, who would they be? What would they say? What would they never say?

This paragraph must be client-specific — it should be impossible to copy it to a different client without rewriting.

> *Example register:* "[Client name] sounds like a trusted colleague who has genuinely useful advice — never a salesperson, never an academic. The brand speaks plainly, uses real-world examples, and treats the audience as intelligent adults who have seen enough marketing to recognise when they are being sold to. It is warm but efficient: it respects the reader's time. It does not shout to be heard. On the rare occasions it celebrates an achievement, it is brief and backs it up with evidence. It never uses the word 'groundbreaking'."

---

## Section 2: Platform Tone Adjustments

The brand voice is consistent across all platforms. The tone adjusts to match platform norms. Generate a platform adjustment for every platform the client is active on, plus any the client plans to use.

For each platform, provide:
- A one-sentence tone description for that platform
- 2 platform-specific tone rules
- One worked example using the sample message below

---

**Sample message for worked examples:**
Use a product or service announcement relevant to the client's industry. If no specific announcement is available, use: *"[Client name] is pleased to introduce [new product/service], now available at [location/online]."*

Rewrite this announcement in the correct tone and format for each platform:

---

**LinkedIn**
- Tone: Formal, evidence-based, peer-to-peer professional. Write as though publishing a short industry insight.
- Rules: Lead with a relevant industry observation or data point before the announcement. Use full sentences. No more than one emoji if used at all.
- Example: *[Rewritten announcement for LinkedIn]*

---

**Facebook**
- Tone: Warm, conversational, community-focused. Write as though addressing a neighbourhood group.
- Rules: Use a question or invitation to open. Keep paragraphs short. A friendly emoji or two is appropriate.
- Example: *[Rewritten announcement for Facebook]*

---

**Instagram**
- Tone: Visual-first, aspirational or relatable depending on the client's personas. Caption supports the image — it is not the main event.
- Rules: Open with a strong hook (first line must work without the "more" button). Keep it short. Hashtags go at the end or in a comment.
- Example: *[Rewritten announcement for Instagram]*

---

**WhatsApp**
- Tone: Direct, personal, and value-led. This is a private channel — treat it as a one-to-one message, not a broadcast.
- Rules: Never open with a promotional hook. Lead with context and value. End with a clear, single call to action. Maximum 3 sentences.
- Example: *[Rewritten announcement for WhatsApp]*

---

**TikTok**
- Tone: Informal, energetic, hook-first. The first second of video and first word of caption must earn attention.
- Rules: Write the caption as a teaser, not a summary. Use the vocabulary and phrasing the persona actually uses. Trends and sounds are fair game.
- Example: *[Rewritten announcement for TikTok — caption and video hook line]*

---

**X / Twitter**
- Tone: Punchy, opinion-led, topical. One strong idea per post.
- Rules: Cut every word that is not working. If the post can be said in 10 words, do not use 20. A question or a take — not a press release.
- Example: *[Rewritten announcement for X/Twitter]*

---

Only include platforms the client is active on or has confirmed plans to use. If a platform is not relevant, omit it.

---

## Section 3: Vocabulary List

### Words and Phrases to Use

Generate 10–15 brand-specific terms, preferred vocabulary, and power words. Draw from:
- The client's three tone adjectives
- The industry vocabulary appropriate to the client's sector
- The EA professional register from the `east-african-english` skill
- The language used by the admired brands the client identified

Format as a list with a one-line note on why each term fits the brand:

| Word / Phrase | Why it fits |
|---|---|
| [Term] | [One-line rationale] |

---

### Words and Phrases to Avoid

Generate 10–15 items — jargon, competitor terms, off-brand language, and anything that conflicts with the tone attributes. Include:
- At least 3 items specific to the client's industry (common jargon or clichés)
- At least 2 items that reflect what the "brands to avoid" use
- The standard EA avoid list: "groundbreaking", "revolutionary", "game-changing", "amazing", "awesome", "unleash", "skyrocket"

Format as a list with a one-line note on why each term is off-brand:

| Word / Phrase | Why to avoid |
|---|---|
| [Term] | [One-line rationale] |

---

## Section 4: Emoji Policy

State the emoji policy for this brand clearly. Decisions should align with the tone attributes — a "professional and authoritative" brand uses fewer emojis than a "warm and approachable" brand.

**Platform-by-platform emoji usage:**

| Platform | Emojis used? | Frequency | Types appropriate | Notes |
|---|---|---|---|---|
| LinkedIn | Yes / No / Sparingly | *(e.g. max 1–2 per post)* | Functional ✅ only | |
| Facebook | | | | |
| Instagram | | | | |
| WhatsApp | | | | |
| TikTok | | | | |
| X / Twitter | | | | |

**Emoji types — define the policy:**
- **Functional emojis** — used to organise or direct (✅ ➡️ 📌 🔗): permitted / not permitted
- **Expressive emojis** — convey emotion or tone (😊 🙌 💙): permitted / limited / not permitted
- **Decorative emojis** — pure decoration, no semantic value (🌟 ✨ 💫): permitted / not permitted

**Emojis to avoid** — list 5–8 emojis that are off-brand for this client with a brief note on why. Common candidates: 🔥 (overused), 💯 (informal/aggressive), 😂 (too casual for professional brands), 🚀 (startup cliché).

---

## Section 5: Hashtag Brand Identity

### Branded Hashtags

Generate 1–3 branded hashtags unique to this client. Requirements:
- Not already in widespread use (advise the client to search on Instagram and TikTok before publishing)
- Short enough to be memorable and typeable on a mobile keyboard
- Specific enough to be brand-owned — not a generic industry term
- Consistent across platforms

For each hashtag:

**#[Hashtag]**
- *Purpose:* [What this hashtag is for — e.g. all organic content / campaign-specific / community UGC]
- *Platforms:* [Which platforms to use it on]
- *Usage rule:* [All posts / Campaigns only / Specific content types]
- *How to encourage audience use:* [One-line instruction for growing hashtag adoption]

---

### Community and Discovery Hashtags

Provide guidance on supplementary hashtags — not branded, but relevant for reach:

- **Industry hashtags** (2–3 examples relevant to the client's sector)
- **Location hashtags** (2–3 examples for Uganda/EA or the client's specific city, e.g. #Kampala #UgandaBusiness)
- **Platform-specific trending hashtags** — note that these change weekly; the content team should review weekly

State clearly: branded hashtags are permanent; community hashtags rotate; trending hashtags are time-limited.

---

## Section 6: Visual Identity Brief (For Designer Briefing)

This section is guidance for briefing a graphic designer or photographer. It does not produce design files. The output is a written brief the client can hand to their designer.

---

### Photography Style Direction

State clearly and briefly:

- **Subject matter:** [What should appear in photos — people, products, environments, combinations]
- **People in images:** Yes or No; if yes — clients, staff, models, or user-generated; posed or candid; demographic alignment with personas
- **Setting:** Indoor / Outdoor / Both; specific settings that work for this brand (e.g. "office environments", "market settings", "outdoor lifestyle")
- **Mood:** [Choose: Warm / Neutral / Bold / Calm / Energetic] — and one sentence on what this looks like in practice
- **Professional vs. authentic:** [Highly produced / Balanced / Raw and authentic] — state the dial position and why it matches the personas
- **Stock photography policy:** Permitted with conditions / Avoid entirely / Permitted for specific platforms only — state the rule and the reason

---

### Colour Palette Usage

Using colours from the 01-client-brief (hex codes if provided):

| Colour role | Colour (hex or description) | When to use |
|---|---|---|
| Primary | | Main brand colour — dominant in all content |
| Secondary | | Supporting colour — used for accents and contrast |
| Accent | | Highlight colour — used sparingly for CTAs |
| Background | | Default background for graphics |
| Text on dark | | Colour used for text overlays on dark images |
| Text on light | | Colour used for text overlays on light images |

Note any colours to avoid — especially colours associated with competitors or that clash with brand colours.

---

### Typography Guidance

Using fonts from the 01-client-brief:

- **Heading font:** [Name] — *personality note:* [e.g. "Serif — conveys tradition and authority"; "Bold sans-serif — modern and direct"]
- **Body font:** [Name] — *personality note:*
- **On social media graphics:** [Which font to use for headlines on posts; which for captions/subtext]
- **Font size guidance:** Minimum 24px for mobile legibility on social graphics
- **Fonts to avoid:** [Any typefaces that conflict with brand personality — e.g. "No Comic Sans, no script fonts that are difficult to read at small sizes"]

---

### Image Do's and Don'ts

**Do:**
- [Specific instruction, e.g. "Use images that feature real staff and real customers where possible"]
- [Specific instruction]
- [Specific instruction]
- [Specific instruction]

**Do not:**
- [Specific instruction, e.g. "Do not use stock images of people who do not reflect the EA demographic of the client's audience"]
- [Specific instruction]
- [Specific instruction]
- [Specific instruction]

---

## Quality Criteria

- Tone attributes are derived logically from the client's three adjectives — a reader can trace the connection
- Each attribute's "Right" and "Wrong" examples are distinct and clearly illustrate the difference — not variations on the same sentence
- The brand voice summary paragraph is specific to this client; it cannot be applied to another client without rewriting
- Platform tone adjustments show a genuine tonal shift between platforms using the same source message — not the same message with a different emoji
- Vocabulary lists contain at least 3 items specific to the client's industry; generic EA professional vocabulary does not fill the list
- Emoji policy is specific enough to act on without further discussion — ambiguous entries such as "use occasionally" are not acceptable
- Branded hashtags are distinct, searchable, and accompanied by a usage rule
- Visual identity brief is written as a practical designer brief — not as abstract brand theory
- British English spelling throughout; tone of this document's own prose follows the `east-african-english` skill

---
name: ai-content-recycling-pipeline
description: >
  Transform one piece of long-form content into 10 platform-ready assets using
  AI tools. Solves the content creation bottleneck for resource-constrained East
  African marketing teams. Invoke when a client needs more content output from
  their existing content investment.
---
# AI Content Recycling Pipeline

<!-- dual-compat:start -->
## Use when
- Transform one piece of long-form content into 10 platform-ready assets using AI tools. Solves the content creation bottleneck for resource-constrained East African marketing teams. Invoke when a client needs more content output from their existing content investment.
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
- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask for:
- Client business name and industry
- Country/city (default: Uganda)
- Source content (paste the blog post, article, or video transcript — minimum 500 words)
- Active social platforms (Facebook, Instagram, LinkedIn, TikTok, X, WhatsApp, YouTube)
- Brand voice description (formal/casual, warm/authoritative, local/international)
- Any topics or phrases to avoid

## The Core Principle

Most East African marketing teams create content once and publish it once. This wastes the research, thinking, and writing invested in each piece. AI makes it practical to extract 10 distinct, platform-optimised assets from a single source in under 60 minutes — without the output feeling repetitive (Roth and neuroflash, 2024).

The constraint is not content creation — it is content *extraction and reformatting*. AI removes that constraint.

## The 10-Asset Pipeline

### Source: One long-form piece (500–1,500 words)
A blog post, article, interview transcript, or video script.

---

**Asset 1 — Facebook post (100–150 words)**

Prompt:
```
Extract the most surprising or counterintuitive insight from this article. Write a Facebook post that opens with that insight as a hook, explains it in 2–3 sentences, and ends with a discussion question. Warm, conversational tone. No hashtags.
```

**Asset 2 — Instagram caption (50–80 words + hashtags)**

Prompt:
```
Write an Instagram caption based on this article. Start with an emotional hook (not a question). Keep it under 80 words. Add 10 relevant hashtags at the end — a mix of branded, niche, and community tags for [industry] in Uganda.
```

**Asset 3 — LinkedIn post (150–200 words)**

Prompt:
```
Write a LinkedIn post based on this article. Start with a professional insight or data point. Use short paragraphs. End by inviting peers to share their experience. No hashtags. Professional but not stiff.
```

**Asset 4 — TikTok / Reels script (30-second spoken)**

Prompt:
```
Write a 30-second TikTok script based on this article. Hook in the first 3 seconds (bold statement or question). 3 punchy points. Strong CTA at the end. Written to be spoken aloud — conversational and energetic.
```

**Asset 5 — X / Twitter post (under 280 characters)**

Prompt:
```
Extract the single most quotable sentence or statistic from this article. Rewrite it as a standalone X post under 280 characters. Add 2 relevant hashtags.
```

**Asset 6 — Instagram carousel outline (5 slides)**

Prompt:
```
Structure this article as a 5-slide Instagram carousel. Slide 1: bold hook/title. Slides 2–4: one key point each with a 10-word headline and 15-word supporting line. Slide 5: summary + CTA. Output slide-by-slide.
```

**Asset 7 — WhatsApp broadcast message (under 700 characters)**

Prompt:
```
Write a WhatsApp broadcast message based on this article. Under 700 characters. Start with the most useful takeaway. One clear CTA at the end (visit link / reply for more / book now).
```

**Asset 8 — Email newsletter paragraph (80–100 words)**

Prompt:
```
Write an 80-word paragraph for a client email newsletter based on this article. Professional, warm tone. Include a 'Read more' link placeholder. Make the reader curious enough to click.
```

**Asset 9 — Quote card text (one sentence)**

Prompt:
```
Extract or craft the single most shareable, standalone sentence from this article — something that works as a quote card. Under 20 words.
```

**Asset 10 — Podcast / audio outline (3-minute spoken)**

Prompt:
```
Structure this article as a 3-minute podcast segment outline: 30-second intro (hook + what we'll cover), 4 x 30-second points, 30-second outro (summary + CTA). Written for spoken delivery.
```

---

## Platform Adaptation Rules

| Platform | Practical limit | Tone | Key rule |
|---|---|---|---|
| Facebook | 150 words | Conversational | End with question or CTA |
| Instagram | 80 words + hashtags | Emotional, visual | Hook in first line |
| LinkedIn | 200 words | Professional insight | Invite discussion |
| TikTok / Reels | 30-second script | Energetic, direct | Hook in 3 seconds |
| X / Twitter | 280 characters | Punchy, opinionated | One idea only |
| WhatsApp | 700 characters | Direct, warm | Actionable CTA |
| Email | 80–100 words | Helpful, personal | Drive to one action |

## Quality Gate

Before publishing any asset, check:
- Does it make sense as a standalone piece — no context needed from other assets?
- Does the tone match the client's brand voice?
- Is there a local Uganda/EA reference or example where appropriate?
- Has it been read aloud (for spoken-word assets: TikTok, WhatsApp, podcast)?
- Are hashtags relevant and not overused?
- Has a human reviewed and approved — not published directly from AI output?

## Time Benchmark

- Running all 10 prompts: 15–20 minutes
- Human review and light editing: 30–40 minutes
- **Total: under 60 minutes for 10 platform-ready assets**

## Quality Criteria

- All 10 asset types are generated from the source content
- Each asset is platform-specific — not a copy-paste of the same text with minor edits
- Platform adaptation rules are applied (character limits, tone, format)
- Quality gate checklist is completed before any asset is published
- Time benchmark is achieved (under 60 minutes total)
- Brand voice is consistent across all 10 assets
- Output is organised by asset type for clear client handover
- At least one asset references a local Uganda/EA context, event, or example

## References

- Roth, H. and neuroflash (2024) *AI Strategy 2025 for Marketing Teams*.
- Sweenor, D.E. and Mulkers, Y. (2024) *Generative AI Business Applications*. TinyTechMedia.

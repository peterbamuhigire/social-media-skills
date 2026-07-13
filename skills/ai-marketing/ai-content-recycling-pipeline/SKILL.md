---
name: ai-content-recycling-pipeline
description: Use when AI Content Recycling Pipeline is needed to produce an operating pipeline specification for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Content Recycling Pipeline

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **operating pipeline specification** and the supplied brief falls within ai content recycling pipeline.

## Do Not Use When
- Use `ai-readiness-diagnostic` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| AI marketing use-case brief, intended human control point and success measure | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified operating pipeline specification; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact operating pipeline specification, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete operating pipeline specification; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Operating pipeline specification | Requester, client reviewer or delivery team | The operating pipeline specification addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source/assumption register and completed release checklist | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested operating pipeline specification, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

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

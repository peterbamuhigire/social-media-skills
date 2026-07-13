---
name: prompt-library-image-audio-video
description: Use when AI Prompt Library — Image, Audio, and Video is needed to produce a reusable prompt library for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Prompt Library — Image, Audio, and Video

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **reusable prompt library** and the supplied brief falls within ai prompt library — image, audio, and video.

## Do Not Use When
- Use `caption-writer` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Content brief, channel, audience, message, format and call to action | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified reusable prompt library; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Channel, format and audience commitment level are known | Choose the hook, structure and call to action native to that context. | Copy that could be pasted unchanged onto any channel or brand. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact reusable prompt library, consumer, market, channel and approval boundary; route to `caption-writer` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete reusable prompt library; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Reusable prompt library | Requester, client reviewer or delivery team | The reusable prompt library addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested reusable prompt library, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [caption-writer](../caption-writer/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## Required Input
Ask for the following before generating any AI media prompts:

1. **Client business name** — the exact trading name used publicly
2. **Industry** — e.g. hospitality, financial services, retail, professional services
3. **Country/city** — default: Uganda/Kampala
4. **Primary goal** — what the asset is for: social media post, explainer video, voice-over, podcast, outreach video, background music
5. **Medium** — select one or more: image / voice-over / avatar video / podcast audio / background music
6. **Platform or tool** — specify the AI tool to be used (e.g. Midjourney, ElevenLabs, HeyGen, Suno AI)
7. **Brand voice anchors** — tone (warm/authoritative/conversational), visual palette, and any existing style references

## The Multi-Medium Golden Rule
Every AI-generated asset — image, audio, or video — must meet the same standard: it must look, sound, and feel as though it was produced by a skilled human creative. The failure signatures differ by medium:

- **Image:** uncanny skin texture, slightly off proportions, hyperrealistic fantasy-realist lighting
- **Audio:** robotic prosody, unnatural word stress, monotone delivery
- **Video:** jerky avatar motion, stilted pacing, mismatched lip sync
- **Music:** technically proficient but emotionally thin — what Cowen describes as lacking the "ineffable something" of human composition (Ching and Mothi, 2025)

Each medium has its own prompt structure to prevent these failures.

## Medium 1 — AI Image Generation
See `image-prompt-engineer` for the full Eight-Layer Prompt Anatomy, negative prompt library, platform technical parameters, and cultural accuracy review protocol.

**Summary for this skill:**
- Specify all eight layers: Subject, Environment, Lighting, Colours, Mood, Composition, Style, Technical Parameters
- Always include a negative prompt
- Always review images of East African subjects with a human reviewer who has direct cultural knowledge before client delivery
- Document the seed number for every approved image to maintain campaign consistency

Cross-reference `image-prompt-engineer` for full platform syntax (Midjourney, DALL-E 3, Stable Diffusion, Flux, Adobe Firefly).

## Medium 2 — AI Audio (Text-to-Speech and Voice Generation)
**Tools:** ElevenLabs, Murf, Resemble AI, Descript, NotebookLM (podcast-style audio)

### What Makes AI Audio Sound Human
Four factors cause AI audio to sound robotic. Address each before generating:

**1. Sentence length.** AI voices stumble on sentences over 25 words. Break long sentences before entering text into a TTS tool.

**2. Punctuation as prosody.** Commas create micro-pauses; em dashes create dramatic pauses; ellipses suggest hesitation. Use punctuation deliberately to shape the spoken rhythm of the script — not just for grammar.

**3. Consonant clustering.** Consecutive words starting with the same consonant produce robotic, over-emphasised stress. Rewrite alliterative sequences before generating.

**4. Speaking style selection.** Choose a speaking style explicitly in platform settings — "conversational," "authoritative," "warm and friendly" — never default to the neutral tone.

### Voice-Over Script Prompt Template
```
Script for [platform: LinkedIn video / Instagram Reel / explainer video / podcast]
Duration target: [X seconds / X minutes]
Speaking style: [conversational and warm / authoritative and clear / enthusiastic and energetic]
Audience: [describe the target listener — role, location, primary concern]
Core message: [one sentence — the single thing the listener must remember]
CTA at end: [specific instruction — WhatsApp number, website URL, or next step]
[Script text — write in spoken register, not written register.
Short sentences. Active voice. No jargon. One idea per sentence.]
```

**Spoken register rules:** Write "you can" not "one may." Write "let's" not "let us." Write "here's what that means" not "the following section describes." Read the script aloud before generating — if it sounds unnatural when spoken, rewrite it.

### NotebookLM Podcast Production
Upload source documents (a strategy report, blog post series, or research summary); NotebookLM generates a conversational two-host podcast episode.

Best use: internal knowledge-sharing, client education, thought leadership audio.

**Important:** Always review and edit the generated transcript before producing the final audio. The AI hosts occasionally add incorrect context, misattribute sources, or insert inaccurate statistics. The transcript is the editorial record — treat it as a draft.

## Medium 3 — AI Avatar and Video Generation
**Tools:** HeyGen, Synthesia, D-ID, Runway, Pika Labs

### Avatar Video Script Rules
- Write all scripts in spoken register — as if speaking aloud, not writing
- Maximum 150 words per minute — AI avatars cannot deliver fast speech naturally
- One idea per sentence — compound sentences cause pacing and lip-sync errors
- Avoid contractions if the avatar uses a non-native English accent setting — they often distort
- Avoid idioms that may not translate to neutral delivery ("hit the ground running," "low-hanging fruit")

### AI Avatar Video Script Template
```
[Opening — 5 seconds]
Hook. One sentence that names the viewer's problem or goal.
Example: "If you're losing customers to competitors and you don't know why, this is for you."

[Body — 60–90 seconds]
Three key points. One sentence per point. Transition word between each.
Point 1: [specific insight or fact]
Transition: "And there's more —" / "Here's why that matters —" / "But here's the part most people miss:"
Point 2: [specific insight or fact]
Transition: [as above]
Point 3: [specific insight or fact]

[CTA — 10 seconds]
One specific instruction. Include the contact method.
Example: "Send us a WhatsApp message on [number] today — we'll respond within the hour."

Total word count: under 250 words for a 90-second video.
```

### Personalised Video Outreach
Personalised video achieves 75% open rates and 40% response rates in B2B outreach (Roth and neuroflash Team, 2024/2025). Use HeyGen or Tavus for campaign-scale personalised video.

**Prompt structure:** Write one master script with placeholder variables:
- `{{first_name}}` — recipient's first name
- `{{company_name}}` — recipient's company
- `{{specific_detail}}` — one personalised observation about their business

The AI renders a unique video per recipient with the avatar appearing to speak directly to them. Review the master script carefully — all placeholder replacements are machine-generated at scale.

## Medium 4 — AI Music and Sound
**Tools:** Suno AI, Udio, Soundraw, AIVA, Beatoven.ai

### Background Music Prompt Template
```
Style: [genre: warm acoustic / energetic Afrobeats / calm ambient / professional corporate]
Mood: [emotional register: motivating / relaxing / celebratory / trustworthy / urgent]
Tempo: [slow / medium / upbeat]
Instruments: [specify if required: piano and strings / guitar and percussion / synths only]
Duration: [X seconds]
Use: [social media background / explainer video / podcast intro / presentation background]
```

### The Human Quality Standard for AI Music
Ching and Mothi (2025) document that AI-generated music — even when technically proficient — frequently lacks the emotional depth and cultural resonance of human-composed music. Suno AI tracks were found to be technically acceptable but thin in emotional weight.

The test: after generating a track, ask a human reviewer with musical knowledge — "Does this music feel right for this moment, or is it merely technically acceptable?" If the answer is the latter, regenerate with a more specific mood and instrument brief, or commission a human musician.

All AI-generated music for client use must pass this review before deployment.

## Disclosure Requirements
Under the EU AI Act (Article 4) and emerging global standards, AI-generated audio and video must be disclosed where the content is presented as a real person or used commercially.

Apply the following to every AI media asset:

| Asset type | Disclosure requirement |
|---|---|
| AI voice-over | Disclose in the production record; inform the client |
| AI avatar video (brand character) | No disclosure required if clearly a brand avatar, not a real person |
| AI avatar video (presented as real person) | Disclose to the end audience |
| AI-generated music (commercial distribution) | Disclose in metadata |
| AI-generated images (commercial use) | Confirm Adobe Firefly or equivalent for licensing-safe output |

**SynthID** (Google/DeepMind) is the current standard for watermarking AI-generated audio; equivalent tools exist for images and video. Apply SynthID watermarking to all AI audio produced for commercial client distribution.

## Campaign Consistency Protocol
Maintain consistency across all AI-generated assets in a single campaign:

1. **Image:** document seed number and full prompt for every approved image — reuse the same seed for all campaign assets
2. **Voice:** use the same voice ID, speaking style, and speed setting throughout the campaign — document these in the production record
3. **Video:** use the same avatar, background, and script structure across all campaign videos
4. **Music:** use the same generated track (or the same generation parameters) across all videos in a campaign

Note the production record fields: Asset ID | Tool | Prompt or Script | Seed/Voice ID | Style Settings | Date Generated | Human Reviewer | Approved (Y/N).

## Quality Criteria
Good output from this skill meets all of the following standards:

- All AI-generated audio reviewed for prosody and natural rhythm — no robotic stress patterns, unnatural pauses, or monotone delivery before client delivery
- All AI-generated video scripts written in spoken register, at no more than 150 words per minute, with one idea per sentence
- All AI-generated images reviewed against the Eight-Layer quality standard and cultural accuracy protocol — cross-reference `image-prompt-engineer`
- All AI-generated music reviewed by a human with musical knowledge before deployment — the "ineffable something" test applied
- Disclosure recorded for every AI-generated media asset in the production record, with client informed
- Placeholder variables used in all video scripts intended for personalised outreach — no manual personalisation at scale
- Brand consistency maintained across all assets in a campaign — same seed, same voice ID, same style parameters documented and applied throughout

## References
- Ching, C. and Mothi, N. (2025) *AI for Creatives*. Referenced for the "ineffable something" AI music quality finding.
- Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing Teams*. Referenced for personalised video outreach performance data.
- LetsEnhance (2024) *How to Write AI Image Prompts — From Basic to Pro*. Referenced for image prompt anatomy.
- EU AI Act, Article 4 (2024) — AI-generated content disclosure requirements.

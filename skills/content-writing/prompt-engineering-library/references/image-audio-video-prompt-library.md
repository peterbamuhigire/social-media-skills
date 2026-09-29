# Image, Audio and Video Prompt Library

Merged from skills/content-writing/prompt-library-image-audio-video on 2026-09-29 at 7c60138; preservation map: [prompt-library-image-audio-video.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/prompt-library-image-audio-video.md)

## When to use this reference

Use it when the client's prompt library must cover AI media beyond text: images, voice-over and text-to-speech, podcast audio, avatar and personalised video, and background music. It extends the text-prompt formula in `SKILL.md` with a prompt structure per medium, a disclosure table and a campaign production record. Full image-prompt detail lives in [image-prompt-patterns.md](image-prompt-patterns.md). Video strategy, avatar programme design and personalised-video campaign planning belong to [strategy-video-content](../../../strategy/strategy-video-content/SKILL.md); this reference supplies only the prompts and scripts.

## Inputs to collect before any AI media prompt

1. **Client business name** — the exact trading name used publicly.
2. **Industry** — for example hospitality, financial services, retail, professional services.
3. **Country/city** — default Uganda/Kampala.
4. **Primary goal** — what the asset is for: social media post, explainer video, voice-over, podcast, outreach video, background music.
5. **Medium** — one or more of: image / voice-over / avatar video / podcast audio / background music.
6. **Platform or tool** — the AI tool to be used (for example Midjourney, ElevenLabs, HeyGen, Suno AI).
7. **Brand voice anchors** — tone (warm/authoritative/conversational), visual palette and any existing style references.

## The multi-medium Golden Rule

Every AI-generated asset — image, audio or video — must look, sound and feel as though a skilled human creative produced it. The failure signatures differ by medium:

| Medium | Failure signature |
|---|---|
| Image | Uncanny skin texture, slightly off proportions, hyperrealistic fantasy-realist lighting |
| Audio | Robotic prosody, unnatural word stress, monotone delivery |
| Video | Jerky avatar motion, stilted pacing, mismatched lip sync |
| Music | Technically proficient but emotionally thin — lacking what Cowen calls the "ineffable something" of human composition (cited in Ching and Mothi, 2025) |

Each medium below has its own prompt structure to prevent these failures.

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| Medium is an image | Apply the eight-layer anatomy, negative prompt, cultural review and seed record in [image-prompt-patterns.md](image-prompt-patterns.md). | Generic AI imagery; inaccurate depiction of East African subjects. |
| A TTS script has sentences over 25 words | Break them before entering text into the tool. | Voice stumbling and robotic stress. |
| A script is written in written register | Rewrite in spoken register and read it aloud before generating. | Unnatural, stilted delivery. |
| An avatar script runs faster than 150 words per minute | Cut it to 150 words per minute or fewer. | Unnatural fast speech, pacing and lip-sync errors. |
| Outreach video must be personalised at scale | Use one master script with `{{placeholder}}` variables; never personalise by hand at scale. | Inconsistent or error-prone manual personalisation. |
| NotebookLM (or similar) generates a podcast | Treat the transcript as a draft; review and edit before producing final audio. | Invented context, misattributed sources, inaccurate statistics. |
| AI music is technically acceptable but feels thin | Regenerate with a more specific mood and instrument brief, or commission a human musician. | Deploying emotionally flat music. |
| Any AI media asset is produced for a client | Record disclosure in the production record and inform the client, per the disclosure table. | Undisclosed synthetic media. |

## Medium 1 — AI image generation

Summary for library builders (full method in [image-prompt-patterns.md](image-prompt-patterns.md)):

- Specify all eight layers: Subject, Environment, Lighting, Colours, Mood, Composition, Style, Technical Parameters.
- Always include a negative prompt.
- Always have images of East African subjects reviewed by a human with direct cultural knowledge before client delivery.
- Record the seed number of every approved image to keep the campaign consistent.
- Platform syntax covered there: Midjourney, DALL-E 3, Stable Diffusion, Flux, Adobe Firefly.

## Medium 2 — AI audio (text-to-speech and voice generation)

**Tools:** ElevenLabs, Murf, Resemble AI, Descript, NotebookLM (podcast-style audio).

### What makes AI audio sound human

Four factors make AI audio sound robotic. Address each before generating:

1. **Sentence length.** AI voices stumble on sentences over 25 words; break long sentences before entering text into a TTS tool.
2. **Punctuation as prosody.** Commas create micro-pauses, em dashes create dramatic pauses, ellipses suggest hesitation. Use punctuation to shape the spoken rhythm, not only for grammar.
3. **Consonant clustering.** Consecutive words starting with the same consonant produce robotic, over-emphasised stress; rewrite alliterative runs before generating.
4. **Speaking style selection.** Choose a speaking style explicitly in platform settings — "conversational", "authoritative", "warm and friendly" — never leave the neutral default.

### Voice-over script prompt template

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

**Spoken-register rules:** write "you can", not "one may"; "let's", not "let us"; "here's what that means", not "the following section describes". Read the script aloud before generating; if it sounds unnatural spoken, rewrite it.

### NotebookLM podcast production

Upload source documents (a strategy report, blog post series or research summary); NotebookLM generates a conversational two-host podcast episode. Best uses: internal knowledge-sharing, client education, thought-leadership audio.

Always review and edit the generated transcript before producing the final audio. The AI hosts occasionally add incorrect context, misattribute sources or insert inaccurate statistics. The transcript is the editorial record — treat it as a draft.

## Medium 3 — AI avatar and video generation

**Tools:** HeyGen, Synthesia, D-ID, Runway, Pika Labs.

### Avatar video script rules

- Write every script in spoken register — as if speaking aloud, not writing.
- Maximum 150 words per minute; AI avatars cannot deliver fast speech naturally.
- One idea per sentence; compound sentences cause pacing and lip-sync errors.
- Avoid contractions if the avatar uses a non-native English accent setting; they often distort.
- Avoid idioms that do not carry in neutral delivery ("hit the ground running", "low-hanging fruit").

### AI avatar video script template

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

### Personalised video outreach prompts

Roth and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing Teams* report 75% open rates and 40% response rates for personalised video in B2B outreach; treat these as source-reported figures, not a forecast for a client. HeyGen or Tavus can render campaign-scale personalised video.

**Prompt structure:** write one master script with placeholder variables:

- `{{first_name}}` — recipient's first name
- `{{company_name}}` — recipient's company
- `{{specific_detail}}` — one personalised observation about their business

The tool renders a unique video per recipient, with the avatar appearing to speak directly to them. Review the master script carefully: every placeholder replacement is machine-generated at scale. Campaign design, consent and programme governance for avatar and personalised video sit with [strategy-video-content](../../../strategy/strategy-video-content/SKILL.md).

## Medium 4 — AI music and sound

**Tools:** Suno AI, Udio, Soundraw, AIVA, Beatoven.ai.

### Background music prompt template

```
Style: [genre: warm acoustic / energetic Afrobeats / calm ambient / professional corporate]
Mood: [emotional register: motivating / relaxing / celebratory / trustworthy / urgent]
Tempo: [slow / medium / upbeat]
Instruments: [specify if required: piano and strings / guitar and percussion / synths only]
Duration: [X seconds]
Use: [social media background / explainer video / podcast intro / presentation background]
```

### The human quality standard for AI music

Ching and Mothi (2025) *AI for Creatives* document that AI-generated music, even when technically proficient, often lacks the emotional depth and cultural resonance of human-composed music; the Suno AI tracks they discuss were technically acceptable but thin in emotional weight.

The test: after generating a track, ask a human reviewer with musical knowledge, "Does this music feel right for this moment, or is it merely technically acceptable?" If the latter, regenerate with a more specific mood and instrument brief, or commission a human musician. All AI-generated music for client use passes this review before deployment.

## Disclosure requirements

The source skill cited the EU AI Act (Article 4) and emerging global standards for disclosing AI-generated audio and video where content is presented as a real person or used commercially. Article 4 of the EU AI Act concerns AI literacy; the transparency duties for synthetic and deep-fake content sit in Article 50. Verify the current article, its application date and any local rule (for example Uganda's Data Protection and Privacy Act 2019 where a real person's likeness or voice is used) before citing either to a client; otherwise mark the legal basis `NOT_ASSESSED`.

Apply this table to every AI media asset:

| Asset type | Disclosure requirement |
|---|---|
| AI voice-over | Disclose in the production record; inform the client |
| AI avatar video (brand character) | No disclosure required if clearly a brand avatar, not a real person |
| AI avatar video (presented as real person) | Disclose to the end audience |
| AI-generated music (commercial distribution) | Disclose in metadata |
| AI-generated images (commercial use) | Confirm Adobe Firefly or equivalent for licensing-safe output |

**SynthID** (Google DeepMind) was named in the source as the current standard for watermarking AI-generated audio, with equivalent tools for images and video. Apply SynthID or an equivalent watermark to all AI audio produced for commercial client distribution, and confirm current tool availability before promising it.

## Campaign consistency protocol

Keep every AI-generated asset in one campaign consistent:

1. **Image:** record the seed number and full prompt for every approved image; reuse the same seed across campaign assets.
2. **Voice:** use the same voice ID, speaking style and speed setting throughout; record them in the production record.
3. **Video:** use the same avatar, background and script structure across all campaign videos.
4. **Music:** use the same generated track (or the same generation parameters) across all videos in a campaign.

### Production record template

| Asset ID | Tool | Prompt or Script | Seed/Voice ID | Style Settings | Date Generated | Human Reviewer | Approved (Y/N) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Release checklist for AI media prompts

- [ ] All AI audio reviewed for prosody and natural rhythm — no robotic stress, unnatural pauses or monotone delivery — before client delivery.
- [ ] All video scripts in spoken register, at no more than 150 words per minute, one idea per sentence.
- [ ] All images reviewed against the eight-layer standard and the cultural accuracy protocol in [image-prompt-patterns.md](image-prompt-patterns.md).
- [ ] All AI music reviewed by a human with musical knowledge before deployment; the "ineffable something" test applied.
- [ ] Disclosure recorded for every AI media asset in the production record, with the client informed.
- [ ] Placeholder variables used in every video script meant for personalised outreach; no manual personalisation at scale.
- [ ] Brand consistency held across the campaign: same seed, voice ID and style parameters recorded and applied throughout.

## Sources

- Ching, C. and Mothi, N. (2025) *AI for Creatives* — the "ineffable something" AI music quality finding (citing Cowen).
- Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing Teams* — personalised video outreach performance data.
- LetsEnhance (2024) *How to Write AI Image Prompts — From Basic to Pro*, LetsEnhance.io — image prompt anatomy.
- European Union (2024) Artificial Intelligence Act — cited in the source as Article 4 for AI-generated content disclosure; transparency obligations are in Article 50 (verify before use).

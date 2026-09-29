# Image Prompt Patterns

Merged from skills/content-writing/image-prompt-engineer on 2026-09-29 at 7c60138; preservation map: [image-prompt-engineer.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/image-prompt-engineer.md)

## When to use this reference

Use it when the prompt library must include still-image prompts for an AI image tool (Midjourney, DALL-E 3, Stable Diffusion, Flux, Adobe Firefly): social posts, website heroes, campaign visuals or product showcases. It adds the image-specific layer to the text-prompt structure in `SKILL.md`. For voice, avatar video and music prompts, read [image-audio-video-prompt-library.md](image-audio-video-prompt-library.md). Visual identity decisions themselves (palette, type, layout) belong to the design engine; this reference only translates an approved identity into prompt language.

## Inputs to collect before any image prompt

1. **Client business name** — the exact trading name used publicly.
2. **Industry** — for example financial services, hospitality, retail, professional services.
3. **Country/city** — default Uganda/Kampala.
4. **Primary goal** — what the image is for: social media post, website hero, campaign visual, product showcase.
5. **Platform** — the AI image tool to be used: Midjourney, DALL-E 3, Stable Diffusion, Flux or Adobe Firefly.
6. **Brand visual anchors** — primary colour palette, photographic tone (warm/cool/neutral), and whether the brand is people-centric, product-centric or environment-centric.
7. **Subject matter** — who or what should be in the image, including nationality, age, setting and any required cultural context.

## The Golden Rule

AI images carry a recognisable aesthetic: over-smooth skin, slightly off proportions, hyperrealistic fantasy-realist lighting and symmetrical perfection. The aim is an image that looks art-directed, stylistically intentional and culturally accurate — not AI-generated.

That calls for precision, not volume. One precisely constructed prompt that addresses all eight layers produces better output than ten vague attempts.

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| Any layer is left unspecified | Fill it before generating; a layer left at default produces the generic AI aesthetic. | Stock-looking, obviously synthetic output. |
| Subject is described only as "African" | Name the country, city and contemporary context (e.g. "Ugandan business context", "East African urban professional"). | Western default appearance or pan-African stereotype. |
| Traditional dress is not explicitly requested | State contemporary urban or professional clothing. | Culturally inaccurate dress applied by the model. |
| People appear in the image | Add the people-specific negative prompt and route the image to a human reviewer with direct cultural knowledge before client delivery. | Stereotyped or inaccurate representation reaching the client. |
| An image shows culturally inaccurate representation | Reject and re-prompt, whatever its other qualities. | Shipping a polished but offensive or wrong image. |
| A style reference is wanted | Describe the visual language (e.g. "high-end African fashion editorial photography"); never name a specific photographer. | Copyright and imitation risk. |
| The image is for commercial use and licensing matters | Prefer Adobe Firefly or an equivalent licensing-safe tool. | Unclear commercial rights. |
| An image is approved | Record the seed number (or reference image) and the full prompt. | Losing campaign visual consistency. |
| The output still looks generically AI-generated | Reject and re-prompt against the Golden Rule. | Delivering the AI aesthetic the brief was meant to avoid. |

## Procedure — the eight-layer image prompt anatomy

After LetsEnhance (2024) *How to Write AI Image Prompts — From Basic to Pro*, LetsEnhance.io. Every prompt addresses all eight layers.

1. **Subject** — the primary focus, stated specifically. Not "a woman" but "a Ugandan businesswoman in her late 30s, wearing a tailored navy suit, standing confidently at a modern office window." For East African clients always name nationality, city and context: models default to Western settings and Western physical appearance, and "African" is not sufficient.
2. **Environment** — where the scene is set. Not "office" but "a glass-walled conference room in a Kampala high-rise building, late afternoon, city skyline visible." State contemporary urban or professional clothing unless traditional dress is specifically required.
3. **Lighting** — the single most powerful element for photographic realism; always give both quality and direction.
   - Quality options: natural window light, golden hour, overcast diffused light, dramatic side lighting, studio soft box, practical lamp light.
   - Direction options: from the left, from behind, from above, front-lit, rim-lit.
   - Example: "soft natural light from a large window to the left, creating gentle shadows on the right side."
4. **Colours** — the palette: warm earthy tones, desaturated pastels, bold primary colours, monochromatic blue-grey, high-contrast black and white. Translate the client's brand palette directly into this layer. For East African subjects, specify "true-to-life skin tones for East African subjects" to reduce the tendency to over-lighten or over-darken skin.
5. **Mood** — an atmosphere, not a feeling: confident and aspirational, intimate and warm, urgent and dynamic, calm and authoritative, celebratory and energetic. Mood steers expression, posture and colour saturation, so state it explicitly.
6. **Composition** — camera framing: close-up portrait, wide establishing shot, overhead flat lay, rule-of-thirds framing, Dutch angle, eye-level perspective, over-the-shoulder shot. For social media, state the aspect-ratio context: portrait 9:16 for Stories/Reels, square 1:1 for grid posts, landscape 16:9 for covers.
7. **Style** — the visual aesthetic: a photography style (editorial fashion, documentary street, clean product photography), a medium (digital illustration, watercolour, pencil sketch, 3D render), or a known visual language without naming a specific photographer. Write "the visual aesthetic of high-end African fashion editorial photography", not "shot in the style of [photographer's name]".
8. **Technical parameters** — platform-specific settings:

| Platform | Key parameters |
|---|---|
| Midjourney | `--ar 9:16` (aspect ratio), `--v 6` (version), `--seed 12345` (reproducibility), `--style raw` (less AI-filtered output) |
| DALL-E 3 | "photorealistic, ultra-high resolution, DSLR photograph" — describe the full scene in a clear sentence |
| Stable Diffusion | Negative prompt field essential; ControlNet for pose and composition control; attention weighting for emphasis |
| Flux | Specify camera type and lens; token-efficient prompts; detail and realism engine |
| Adobe Firefly | Built-in commercial use rights; include "Adobe Stock style" for clean, licensable outputs |

Platform parameters and version numbers change; confirm current syntax against the tool's own documentation before a library is issued, and label unchecked parameters `NOT_ASSESSED`.

## Negative prompt library

Include exclusion language to suppress the AI aesthetic on every platform that supports it.

**Universal negative prompt:**
`blurry, distorted proportions, extra fingers, deformed hands, uncanny valley effect, overly smooth skin, plastic appearance, wax figure aesthetic, AI-generated aesthetic, overexposed highlights, neon oversaturation, fantasy lighting, watermark, signature, text overlay, low resolution, jpeg artifacts`

**Add for images of people:**
`emotionless expression, doll-like features, exaggerated proportions, inappropriate cultural stereotypes, culturally inaccurate dress, Western default appearance`

**How to apply by platform:**
- Midjourney: append `--no [list]` at the end of the prompt.
- Stable Diffusion: paste into the dedicated negative prompt field.
- DALL-E 3: write the exclusions as "avoid" instructions in the scene description.
- Flux: include them as explicit exclusions in the prompt text.

## Brand visual identity translation protocol

1. Identify the brand's three visual anchors: primary colour palette, photographic tone (warm/cool/neutral) and subject type (people-centric / product-centric / environment-centric).
2. Map each anchor to its layer: colours → Layer 4; photographic tone → Layer 7; subject type → Layer 1.
3. Use seed numbers (Midjourney `--seed`) to keep visual consistency across a campaign.
4. Record the seed number and full prompt for every approved image; this is the campaign's visual consistency record.

## Cultural accuracy in East African image prompts

BuzzFeed (2023) reported an AI "Barbie" series that produced culturally stereotyped and racially inaccurate images even with an explicit diversity brief. For East African clients:

- Name nationality, context and setting explicitly in Layers 1 and 2; never rely on "African" as a descriptor.
- State contemporary urban or professional clothing unless traditional dress is specifically required.
- Write "East African urban professional" or "Ugandan business context", not generic "African business".
- Have a human reviewer with direct cultural knowledge review every image of people before client delivery.
- Reject and re-prompt any image with culturally inaccurate representation, whatever its other quality.

## Worked example — full prompt construction

**Brief:** a social media post for a Kampala financial services firm, showing a professional consultation scene.

**Constructed prompt (Midjourney):**

```
A Ugandan male financial advisor in his early 40s, wearing a well-fitted charcoal grey suit,
seated across a desk from a Ugandan woman client in her 30s wearing a smart yellow dress,
in a clean modern office in Kampala, glass-walled, city view in the background,
soft natural light from large windows to the left, warm golden tones,
mood: trustworthy and professional, eye-level medium shot, rule of thirds,
editorial corporate photography style, true-to-life East African skin tones,
sharp focus, high detail --ar 4:5 --v 6 --seed 44821 --style raw
--no blurry, plastic skin, fantasy lighting, Western default appearance, text overlay, watermark
```

## Platform quick reference

| Platform | Strength | Key syntax |
|---|---|---|
| Midjourney | Artistic quality, style range | `--ar`, `--v 6`, `--seed`, `--style raw` |
| DALL-E 3 | Natural language, accuracy | Full scene description; include "photorealistic" for photos |
| Stable Diffusion | Control, customisation | Negative prompt field essential; ControlNet for pose control |
| Flux | Detail and realism | Specify camera type and lens; token-efficient prompts |
| Adobe Firefly | Commercial licensing | Built-in commercial use rights; "Adobe Stock style" for clean outputs |

## Release checklist for image prompts

- [ ] All eight layers addressed; none left at default or unspecified.
- [ ] Negative prompt included wherever the platform supports it: the universal library plus the people-specific exclusions when people appear.
- [ ] Cultural accuracy review completed by a human reviewer with direct knowledge of the depicted community before client delivery.
- [ ] Seed number or reference image recorded for every approved image, so the campaign stays consistent across assets.
- [ ] Image checked against the brand's three visual anchors (colour palette, photographic tone, subject type) before delivery.
- [ ] Aspect ratio and technical parameters correct for the platform and the intended placement.
- [ ] Output checked against the Golden Rule; anything that looks generically AI-generated is rejected and re-prompted.

## Sources

- LetsEnhance (2024) *How to Write AI Image Prompts — From Basic to Pro*, LetsEnhance.io — eight-layer prompt anatomy.
- BuzzFeed (2023) — AI image cultural accuracy study: "Barbie" diversity brief findings.

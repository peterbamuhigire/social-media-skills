# Anti-slop guardrails, domain blocks and overlays

Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`); text unchanged except that the slop definition, seven guardrails, banned vocabulary and ship gate stay verbatim in `SKILL.md`, as noted under their headings. Read when briefing writers or sub-agents with the drop-in guardrail block, applying a domain avoidance block (EN, FR, image/video, campaign), running the ME1-ME7 or AS1-AS7 overlays, or checking the full ship gate and quality criteria.

## Machine-error editorial gate (cross-engine Kaizen)

Apply Digital Research's `docs/continuous-improvement/machine-errors-editorial-gate-2026-09-03.md`
to captions, carousels, campaign briefs, image prompts, and community replies:

| ID | Social-media adaptation |
|---|---|
| ME1 | Does each post or slide add a distinct point rather than repeat the previous card? |
| ME2 | Is the hook/contrast real, or a repeated content template? |
| ME3 | Can the audience act without another restatement or CTA recap? |
| ME4 | Does urgency match the verified event, offer, or risk? |
| ME5 | Is the place, person, price, or example real and approved? |
| ME6 | Has the same hook, triplet, emoji, or CTA become a mannerism? |
| ME7 | Does the asset earn attention with a useful claim, instruction, or decision? |

### Impeccable-derived AS overlay

Use AS1-AS7 for social visuals, campaign decks, landing-page handoffs, and short-form copy. In
visual campaigns, purple gradients, glassmorphism, neon glow, AI-beige defaults, decorative
editorial scaffolding, and decorative motion are no-ship choices. Functional status, accessibility,
data, or approved brand reasons must be explicit.

| ID | Social-media overlay test |
|---|---|
| AS1 | Is the visual/copy template chosen for this audience and campaign rather than generator default? |
| AS2 | Do badges, chips, icon tiles, metrics, or numbered labels clarify the message or decorate it? |
| AS3 | Do carousel cards and spacing distinguish ideas, or repeat one card template? |
| AS4 | Does motion or glow communicate a state, message, or task and respect reduced motion? |
| AS5 | Are imagery, examples, icons, and claims purposeful, approved, and traceable? |
| AS6 | Are buzzwords, em-dash cadence, aphoristic contrasts, and theatrical framing recurring? |
| AS7 | Is the rendered post readable, contrasted, complete, and free of clipped or missing content? |

Record `cli`, `browser`, `llm_only`, or `human_review`; unavailable evidence is `NOT_ASSESSED`.

Cut carousel slides that only paraphrase earlier slides. Preserve repetition required by an approved
accessibility, safety, legal, or campaign-frequency requirement and record the reason.

The guardrail every social output passes before it ships. Detection lives in the companion `ai-slop-audit` skill; this skill governs **production** — writing the caption, planning the campaign, briefing the image so slop never appears in the first place.

## Real-time application (this is a LIVE constraint, not only a final gate)
Apply these rules **continuously, as you write** — to every caption, post, slide, line, and image-brief sentence at the moment it is drafted, not only in one pass at the end. The moment you reach for a banned word, a generic placeholder, an unverified figure, brand, or price, or a template default, stop and correct it in place. The ship-gate checklist at the end is the final confirmation, not the first time these rules are consulted. If you are mid-draft and notice slop accumulating — every caption opening the same way, a UGX figure you have not verified, a carousel where each slide restates the last — fix it then; do not defer to a cleanup pass.

## What "AI slop" is (so you know what you are preventing)

Kept verbatim in the parent [`SKILL.md`](../SKILL.md) so there is one copy; read it there.

## The seven universal guardrails (apply to EVERY output)

Kept verbatim in the parent [`SKILL.md`](../SKILL.md) so there is one copy; read it there.

## Banned / high-risk vocabulary (the lexical tells)

Kept verbatim in the parent [`SKILL.md`](../SKILL.md) so there is one copy; read it there.

## Drop-in guardrail block (inherit in dependent skills and sub-agent briefs)
```
ANTI-SLOP GUARDRAIL (inherit in every output):
1. SPECIFICITY FLOOR — every post / slide / section carries >=1 concrete, named,
   market-specific element. No tool defaults, no placeholder copy.
2. VERIFY-BEFORE-EMIT — no statistic, citation, quote, named brand, platform
   figure, or price ships unverified; cite at point of claim; flag uncertainty.
3. AUTHORED VOICE — state a point of view / recommendation; no relentless
   positivity, no sycophancy; allow trade-offs.
4. COVER THE HARD PARTS — objections, edge cases, the audience that won't buy,
   risks, the negative-comment / crisis response.
5. BREAK THE TEMPLATE — vary rhythm and structure; forbid default aesthetics and
   the banned-vocabulary list above.
```

## Domain-specific avoidance (load the relevant block for the output type)
- **Written content — EN (captions, posts, threads, carousels, ad copy, email, blog):** no focal-word clusters; vary sentence length (mix 3–10-word lines with 20–35-word lines for burstiness); ≤1 em-dash per paragraph; no "in conclusion"; one specific local detail per piece (a Kampala neighbourhood, a named local brand, a UGX price, a dated platform figure); a stated point of view, not false balance; a direct CTA tied to the real channel ("Send a WhatsApp to 0700 000 000 before Friday", not "Learn more"); first line earns the tap to expand. Carousels: each slide must add a distinct point, not restate the previous one.
- **Written content — FR (Francophone Africa):** never raw-translate from English; write natively per `language/french-native-copy`; avoid the French banned list above; match register and idiom to the target Francophone market, not metropolitan-France defaults.
- **Image/video briefs for social:** describe real, culturally accurate specimens — named setting, real local context, specific wardrobe and lighting, not generic "African" placeholders; check the brief forces anatomy/text/physics correctness (hands, eyes, teeth, legible on-pack text, plausible geometry); avoid the "AI sheen" (over-smooth skin, plastic bokeh, symmetrical everything); for video, flag lip-sync, "boiling", and frame-to-frame drift; require provenance/disclosure (C2PA / SynthID labelling and a specific "AI-generated [element], art-directed by [team]" line) where it matters, per `policy-ai-content-ethics` (AI IP and copyright policy) and `ai-cultural-bias-audit`.
- **Campaign / strategy text:** add a genuine strategic choice (where to play / how to win), not generic "raise awareness and drive engagement"; transparent, real numbers; no deceptive AI-capability or reach claims; plan the objection and the crisis path.

## Ship gate (run before delivering or publishing ANY output)

Kept verbatim in the parent [`SKILL.md`](../SKILL.md) so there is one copy; read it there.

## Required Input
Before applying the guardrail, confirm:

1. **Client business name** — whose brand voice does this output carry?
2. **Industry** — what sector?
3. **Country / city** — where is the audience? (Default: Uganda / East Africa)
4. **Primary goal** — what is this output meant to achieve?
5. **Output type** — caption, post, thread, carousel, campaign, ad copy, email, deck outline, or image/video brief?
6. **Language** — English, French, or Kiswahili? (Route FR through `language/french-native-copy`, Kiswahili through `language/swahili-native-copy`.)

## Quality Criteria
The output meets the standard when:

1. **Specificity floor met** — every post, slide, or section carries at least one concrete, named, market-specific element no template could produce.
2. **No fabrication** — every statistic, citation, brand, platform figure, and price is verified against a named source; nothing is invented to sound authoritative.
3. **Banned vocabulary absent** — a word-search confirms no list item appears as filler register, in EN or FR.
4. **Authored voice present** — the piece states a clear point of view or recommendation, not false balance or relentless positivity.
5. **Hard parts covered** — objections, edge cases, risks, and the negative-comment / crisis path are addressed, not only the launch happy-path.
6. **Burstiness present** — sentence length and structure vary; no rule-of-three reflex, no antithesis formula, no em-dash flood.
7. **Localised** — UGX, Mobile Money, WhatsApp-first, and real local references are used for the default Uganda / East Africa market (or the named market's equivalents).
8. **Ship gate passed** — every box above is ticked before delivery.

## See also
- `ai-slop-audit` — the detection / evaluation / audit companion (analyse any artefact for slop).
- [humanising-rewrite-passes](humanising-rewrite-passes.md) — the humanisation QC process (formerly `ai-content-humaniser`); its banned list is merged here.
- `language/east-african-english`, `language/language-standards`, `language/french-native-copy`, `language/swahili-native-copy` — apply house style and native-language standards on top.
- `policy-ai-content-ethics` ([AI IP and copyright policy](../../../policies/policy-ai-content-ethics/references/ai-ip-and-copyright-policy.md), [cultural bias audit protocol](../../../policies/policy-ai-content-ethics/references/cultural-bias-audit-protocol.md)) — provenance, disclosure, and bias checks for image/video output.

## Responsibility overlay

Treat the 25 signs as channel-aware editing prompts, not AI-authorship evidence. Every post,
carousel, ad, and CTA must have a named audience, channel job, supported promise, source/date when
needed, and an honest next action. Label hypothetical customers and generated scenarios; never
invent testimonials, urgency, platform rules, engagement results, or cultural insight. Apply ME1-ME7
across the sequence, audit visual choices separately, and mark missing evidence `NOT_ASSESSED`.

- Shared standard: [`AI-slop responsible publishing`](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/references/ai-slop-responsible-publishing-standard-2026-09-11.md)

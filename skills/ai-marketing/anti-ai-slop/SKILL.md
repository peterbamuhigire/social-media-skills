---
name: anti-ai-slop
description: NON-NEGOTIABLE pre-ship guardrail. Run on EVERY generated social output — caption, post, thread, carousel, campaign, ad copy, blog draft, email, deck outline, image/video brief — before it reaches a client or goes live, so the output cannot be recognised as "AI slop". Carries the verified definition, the seven universal slop markers each paired with an avoidance rule, the merged banned-vocabulary list (EN and FR), and a ship-gate checklist. Load first; it overrides stylistic preferences. Pairs with ai-slop-audit (the detector).
---

# Anti AI Slop

<!-- dual-compat:start -->
## Use when
- Run on every AI-assisted social output — caption, post, thread, carousel, campaign, ad copy, blog draft, email, deck outline, image/video brief — before client delivery or publishing. This is the production-side guardrail: write, plan, and brief so slop never appears in the first place.
- Use this skill alongside the main deliverable skill, not instead of it. It governs how the output is made, not what kind of output it is.

## Do not use when
- Do not use this skill to detect or grade slop in finished work — that is the `ai-slop-audit` companion.
- Do not treat it as out-of-scope production: this repository produces text deliverables and image/video briefs only, never code, web builds, graphic design, or video editing.

## Workflow
1. Identify the output type (written content EN/FR, image/video brief, deck outline) and load the matching domain block below.
2. Apply the seven universal guardrails (U1–U7) and the drop-in guardrail block while drafting — not as an afterthought.
3. Run the ship gate before delivery. If any box is unticked, the output is not ready. When in doubt, run `ai-slop-audit` on the draft.

## Anti-Patterns
- Do not pad a caption or post to a word count; one sharp line beats three hollow ones.
- Do not reach for the banned vocabulary as default register; a word from the list is allowed only when it is the genuinely precise term.
- Do not invent statistics, brand names, prices, or "studies show" claims to sound authoritative.

## Outputs
- A social deliverable that carries concrete, named, market-specific substance, an authored point of view, and no AI tells — ready for the ship gate.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as deeper source material and keep this `SKILL.md` execution-focused.
<!-- dual-compat:end -->

The guardrail every social output passes before it ships. Detection lives in the companion `ai-slop-audit` skill; this skill governs **production** — writing the caption, planning the campaign, briefing the image so slop never appears in the first place.

## Real-time application (this is a LIVE constraint, not only a final gate)

Apply these rules **continuously, as you write** — to every caption, post, slide, line, and image-brief sentence at the moment it is drafted, not only in one pass at the end. The moment you reach for a banned word, a generic placeholder, an unverified figure, brand, or price, or a template default, stop and correct it in place. The ship-gate checklist at the end is the final confirmation, not the first time these rules are consulted. If you are mid-draft and notice slop accumulating — every caption opening the same way, a UGX figure you have not verified, a carousel where each slide restates the last — fix it then; do not defer to a cleanup pass.

## What "AI slop" is (so you know what you are preventing)

**AI slop** is low-quality content produced in quantity by generative AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Its three diagnostic properties (Kommers et al., *"Why Slop Matters"*, arXiv 2601.06060, verified):

1. **Superficial competence** — looks fine on the surface, no substance underneath.
2. **Asymmetric effort** — cheap to produce, costly for a human to read, review, or fix.
3. **Mass producibility** — generated at volume.

The human tell named in every domain studied: **absence of intent** — the sense that no one *meant* anything by it. A caption that could belong to any brand in any market has no intent. The job of this skill is to re-internalise effort — specificity, verification, authored choices — before the post reaches a feed.

On social specifically: slop is the engagement-bait carousel with five identical "tips", the LinkedIn post that opens "In today's fast-paced digital landscape", the ad that promises to "elevate your brand", the AI image with seven-fingered hands. Audiences scroll past it. Platform algorithms increasingly suppress it.

## The seven universal guardrails (apply to EVERY output)

| # | Marker to prevent | Avoidance rule you MUST follow |
|---|---|---|
| **U1** | Genericness / averaging | Every post, slide, or section carries ≥1 concrete, named, market-specific element — a real local example, a UGX price, a named place, a dated figure, a stated decision — that a generic template could not produce. Forbid tool defaults. |
| **U2** | Superficial competence | Enforce a substance floor: include a claim, example, number, or recommendation the piece could not exist without. If you cannot, it is filler — cut or replace it. |
| **U3** | Confident wrongness / hallucination | Verify every statistic, citation, quote, named brand, platform figure, and price before publishing. Cite at the point of claim. Flag uncertainty rather than inventing. |
| **U4** | Volume over substance | Prefer one substantive caption over three hollow ones; one strong carousel slide over five padded ones. Do not pad to length or to a posting quota. |
| **U5** | Absence of authored voice / intent | State a point of view, rationale, or named recommendation. Ban relentless positivity and sycophancy. Allow trade-offs and a real opinion. |
| **U6** | Skipping the hard parts | Cover the objection, the edge case, the audience that will not buy, the risk — not just the happy path. In a campaign, plan the negative-comment and crisis response, not only the launch post. |
| **U7** | Mechanical uniformity | Vary sentence length and structure. No rule-of-three reflex, no "it's not X, it's Y" formula, no em-dash flood, no every-caption-the-same-shape carousel. |

## Banned / high-risk vocabulary (the lexical tells)

These words and constructions are statistically over-produced by LLMs (FSU/COLING-2025; PubMed "delve" +400%). **Do not use them as default register.** A word here is allowed only when it is the genuinely precise term, never as filler. This list merges the canonical anti-slop lexicon with the repository's existing `ai-content-humaniser` banned list — both apply.

- **Words:** delve, tapestry, realm, landscape (as metaphor), navigate (as metaphor), leverage, foster, harness, synergy, embark, robust, vibrant, holistic, seamless / seamlessly, intricate, commendable, meticulous, pivotal, underscore, testament, resonate, elevate, paramount, unwavering, multifaceted, comprehensive, revolutionary, groundbreaking, game-changer, beacon, crucial, vital, cutting-edge, innovative, empower, unlock, journey (as metaphor), dynamic.
- **Phrases:** "in today's fast-paced world", "in today's digital age", "in the ever-evolving landscape of", "in the ever-evolving", "it is important to note that", "it is worth noting that", "it's worth mentioning", "it goes without saying", "with that being said", "let's dive in", "here's the kicker", "at the end of the day", "moving forward", "take your business to the next level", "one-stop shop", "in conclusion", "studies show" (without a named study).
- **Over-smooth connectors (rewrite or cut):** "Furthermore," "Moreover," "In addition to the above," "Building on this,".
- **Weak hedges (strengthen or cut):** "may potentially", "could possibly", "one might consider", "it could be argued that", "in some cases".
- **Constructions:** the "it's not just X, it's Y" antithesis; reflexive rule-of-three lists; em-dash used to manufacture drama; relentless triplet adjectives ("robust, scalable, and reliable"); the engagement-bait opener ("Unpopular opinion:", "Let that sink in").
- **French equivalents** (for Francophone Africa output, see `language/french-native-copy`): "plongeons dans", "il est important de noter que", "force est de constater", "dans un monde en constante évolution", "par ailleurs / de plus / en outre" as filler connectors, "au cœur de", "pierre angulaire", "incontournable" as default praise.

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
- **Image/video briefs for social:** describe real, culturally accurate specimens — named setting, real local context, specific wardrobe and lighting, not generic "African" placeholders; check the brief forces anatomy/text/physics correctness (hands, eyes, teeth, legible on-pack text, plausible geometry); avoid the "AI sheen" (over-smooth skin, plastic bokeh, symmetrical everything); for video, flag lip-sync, "boiling", and frame-to-frame drift; require provenance/disclosure (C2PA / SynthID labelling and a specific "AI-generated [element], art-directed by [team]" line) where it matters, per `policy-ai-ip-and-copyright` and `ai-cultural-bias-audit`.
- **Campaign / strategy text:** add a genuine strategic choice (where to play / how to win), not generic "raise awareness and drive engagement"; transparent, real numbers; no deceptive AI-capability or reach claims; plan the objection and the crisis path.

## Ship gate (run before delivering or publishing ANY output)

- [ ] Every post / slide / section has ≥1 concrete, named, market-specific element (U1/U2).
- [ ] Every stat, quote, citation, named brand, platform figure, price verified against a named source (U3).
- [ ] No banned vocabulary used as filler; word-searched the output against the list above.
- [ ] The output states a point of view / recommendation; no sycophancy (U5).
- [ ] Objection / edge case / risk / negative-comment-and-crisis path addressed (U6).
- [ ] Sentence length and structure varied; no rule-of-three reflex, no "it's not X, it's Y", no em-dash flood, no identical-shape carousel (U7).
- [ ] The output type's domain block applied (EN / FR / image-video / campaign).
- [ ] Cultural localisation done (UGX, Mobile Money, WhatsApp-first, real local references) per the market — default Uganda / East Africa.
- [ ] When in doubt, run `ai-slop-audit` on the draft.

If any box is unticked, the output is not ready to ship.

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
- `ai-content-humaniser` — the broader humanisation QC process; its banned list is merged here.
- `language/east-african-english`, `language/language-standards`, `language/french-native-copy`, `language/swahili-native-copy` — apply house style and native-language standards on top.
- `policy-ai-ip-and-copyright`, `ai-cultural-bias-audit` — provenance, disclosure, and bias checks for image/video output.

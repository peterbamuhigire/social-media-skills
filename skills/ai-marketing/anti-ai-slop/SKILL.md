---
name: anti-ai-slop
description: Use when Anti AI Slop is needed to produce a anti AI slop deliverable for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Anti AI Slop

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **anti AI slop deliverable** and the supplied brief falls within anti ai slop.

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
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified anti AI slop deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact anti AI slop deliverable, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete anti AI slop deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Anti ai slop deliverable | Requester, client reviewer or delivery team | The anti AI slop deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested anti AI slop deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

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

---
name: anti-ai-slop
description: Use when social or marketing copy is being drafted with AI help and must read human and local, or an AI-written caption, email, blog or proposal needs humanising; produces the drafted or rewritten copy with the ship-gate checklist; not for grading finished work (use `ai-slop-audit`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Anti AI Slop

The guardrail every social output passes before it ships. Detection lives in the companion `ai-slop-audit` skill; this skill governs **production**: writing the caption, planning the campaign and briefing the image so slop never appears in the first place.

<!-- dual-compat-start -->
## Use When
- Keep our posts, captions, slides and image briefs free of stock AI phrases while they are being written.
- ChatGPT wrote these captions, emails, blogs or proposals; rewrite them so a real local copywriter could have written them before the client sees them.
- Give writers or sub-agents a drop-in guardrail block and the banned vocabulary list to follow on every brief.
- Localise AI drafts with real market detail: UGX prices, Mobile Money, WhatsApp-first habits and named local references.
- Run the ship-gate checklist on a draft before delivering or publishing it.

## Do Not Use When
- `ai-slop-audit` for a scored audit report on finished work.
- `brand-voice-ai-training` for teaching an AI tool the brand's own voice.
- `east-african-english` for regional English usage and spelling.
- Stop when a statistic, price, brand or quote cannot be verified against a named source; flag it rather than let it ship.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name and industry (whose brand voice the output carries) | Brief or client source pack | Yes | Stop; a caption that could belong to any brand has no intent. |
| Country/city of the audience | Brief | Yes | Default to Uganda / East Africa and state the default. |
| Primary goal of the output | Brief | Yes | Ask; without it no real CTA can be tied to a real channel. |
| Output type: caption, post, thread, carousel, campaign, ad copy, email, deck outline, or image/video brief | Requester | Yes | Classify from the request and load that domain block. |
| Language: English, French or Kiswahili | Brief | Yes | Default to English; route FR through `language/french-native-copy` and Kiswahili through `language/swahili-native-copy`. |
| Verified facts: statistics, prices, named brands, quotes, platform figures, each with a named source | Client source pack or cited source | Conditional | Flag the claim and hold it out of the draft; never invent a figure to fill the gap. |

## Workflow

1. Confirm the inputs; route FR and Kiswahili output to the native-copy skills and load the domain avoidance block for the output type from the [guardrails reference](references/guardrails-and-overlays.md).
2. Select one post, asset or content unit (not a calendar as one opaque batch), record the material decision behind it and inspect the surrounding brand, campaign, source, rights and channel context; then draft it, applying the seven guardrails and the banned list continuously: the moment a banned word, generic placeholder, unverified figure, brand or price, or template default appears, fix it in place.
3. Verify every statistic, citation, quote, named brand, platform figure and price against a named source and cite it at the point of claim; stop the claim if it cannot be verified and flag it rather than let it ship.
4. For an existing AI draft, run the humanising rewrite passes (quality risks, uncanny valley, Human Voice Checklist, content-type edits, East Africa localisation, Proof of Human, sign-off).
5. Apply ME1-ME7 across the sequence and AS1-AS7 to visuals, decks and short-form copy, recording the evidence mode.
6. Test the unit against the decision rules, moderation risk and the ship gate; make one concrete refinement, and if any box is unticked, correct the draft and rerun the gate until every box is ticked.
7. Deliver the unit with sources, assumptions, unassessed checks and the approval boundary; run `ai-slop-audit` at the checkpoint, and an F blocks the next asset.

## Slop definition and the seven universal guardrails

**AI slop** is low-quality content produced in quantity by generative AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Its three diagnostic properties (Kommers et al., *"Why Slop Matters"*, arXiv 2601.06060, verified):

1. **Superficial competence** — looks fine on the surface, no substance underneath.
2. **Asymmetric effort** — cheap to produce, costly for a human to read, review, or fix.
3. **Mass producibility** — generated at volume.

The human tell named in every domain studied: **absence of intent** — the sense that no one *meant* anything by it. A caption that could belong to any brand in any market has no intent. The job of this skill is to re-internalise effort — specificity, verification, authored choices — before the post reaches a feed.

On social specifically: slop is the engagement-bait carousel with five identical "tips", the LinkedIn post that opens "In today's fast-paced digital landscape", the ad that promises to "elevate your brand", the AI image with seven-fingered hands. Audiences scroll past it. Platform algorithms increasingly suppress it.

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

These words and constructions are statistically over-produced by LLMs (FSU/COLING-2025; PubMed "delve" +400%). **Do not use them as default register.** A word here is allowed only when it is the genuinely precise term, never as filler. This list merges the canonical anti-slop lexicon with the former `ai-content-humaniser` banned list; [humanising-rewrite-passes](references/humanising-rewrite-passes.md) uses it for its vocabulary sweep.

- **Words:** delve, tapestry, realm, landscape (as metaphor), navigate (as metaphor), leverage, foster, harness, synergy, embark, robust, vibrant, holistic, seamless / seamlessly, intricate, commendable, meticulous, pivotal, underscore, testament, resonate, elevate, paramount, unwavering, multifaceted, comprehensive, revolutionary, groundbreaking, game-changer, beacon, crucial, vital, cutting-edge, innovative, empower, unlock, journey (as metaphor), dynamic.
- **Phrases:** "in today's fast-paced world", "in today's digital age", "in the ever-evolving landscape of", "in the ever-evolving", "it is important to note that", "it is worth noting that", "it's worth mentioning", "it goes without saying", "with that being said", "let's dive in", "here's the kicker", "at the end of the day", "moving forward", "take your business to the next level", "one-stop shop", "in conclusion", "studies show" (without a named study).
- **Over-smooth connectors (rewrite or cut):** "Furthermore," "Moreover," "In addition to the above," "Building on this,".
- **Weak hedges (strengthen or cut):** "may potentially", "could possibly", "one might consider", "it could be argued that", "in some cases".
- **Constructions:** the "it's not just X, it's Y" antithesis; reflexive rule-of-three lists; em-dash used to manufacture drama; relentless triplet adjectives ("robust, scalable, and reliable"); the engagement-bait opener ("Unpopular opinion:", "Let that sink in").
- **French equivalents** (for Francophone Africa output, see `language/french-native-copy`): "plongeons dans", "il est important de noter que", "force est de constater", "dans un monde en constante évolution", "par ailleurs / de plus / en outre" as filler connectors, "au cœur de", "pierre angulaire", "incontournable" as default praise.

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

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Drafted or humanised copy or brief (caption, post, thread, carousel, campaign, ad, email, deck outline, image/video brief) | Client reviewer or publishing owner | Carries ≥1 concrete, named, market-specific element per unit, a point of view and a real CTA tied to a real channel. |
| Completed ship-gate checklist | Delivery lead and `ai-slop-audit` | Every box ticked; any unticked box holds the output back. |
| Source and flag note | Approver | Every stat, price, brand and quote has a named source or is flagged as unverified and held out. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Ship-gate record | Ticked checklist per unit | No unticked box on delivered output. |
| Claim source register | Table: claim, source, date | Each verified claim cites its source at the point of claim. |
| Overlay record | ME1-ME7 and AS1-AS7 rows with evidence mode (`cli`, `browser`, `llm_only`, `human_review`) | Unavailable evidence is `NOT_ASSESSED`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Drafting and rewriting within the supplied brief are permitted; delivery to the client or a live channel is not publication authority.

## Degraded Mode

Without verified facts for the claims in the brief, return the narrowest qualified result and mark the affected checks `not assessed`. The draft can still be delivered with those claims held out and flagged, the guardrails applied and the ship gate showing which boxes remain open.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A banned word is the genuinely precise term | Allow it once, never as filler; otherwise rewrite directly rather than swap in a synonym from the same register. | Lexical tells or mangled precision. |
| A statistic, price, brand or quote cannot be verified against a named source | Stop that claim and flag it; do not let it ship. | Confident wrongness (U3). |
| An AI-assisted draft already exists and must be humanised before client delivery | Run the humanising rewrite passes (quality risks, uncanny valley, Human Voice Checklist, content-type edits, East Africa localisation, Proof of Human, sign-off) in [humanising-rewrite-passes](references/humanising-rewrite-passes.md). | Light polish that leaves AI fingerprints, unverified claims or Western defaults. |
| Output is for Francophone Africa | Write natively per `language/french-native-copy`; never raw-translate from English; match the target market, not metropolitan-France defaults. | Translation artefacts and the French tells. |
| An image or video brief is requested | Describe real, culturally accurate specimens and require provenance/disclosure (C2PA / SynthID labelling and a specific "AI-generated [element], art-directed by [team]" line) per `policy-ai-content-ethics` and `ai-cultural-bias-audit`. | Generic "African" placeholders and undisclosed AI imagery. |
| A visual uses purple gradients, glassmorphism, neon glow, AI-beige defaults, decorative editorial scaffolding or decorative motion | Treat it as no-ship unless a functional status, accessibility, data or approved brand reason is explicit. | Generator-default visuals. |
| A carousel slide only paraphrases an earlier slide | Cut it, unless an approved accessibility, safety, legal or campaign-frequency requirement needs the repetition; record the reason. | Padded, repetitive carousels. |
| A hypothetical customer or generated scenario is used | Label it; never invent testimonials, urgency, platform rules, engagement results or cultural insight. | Deceptive social proof. |

## Quality Standards

- Specificity floor met: every post, slide or section carries at least one concrete, named, market-specific element no template could produce.
- No fabrication: every statistic, citation, brand, platform figure and price is verified against a named source; nothing is invented to sound authoritative.
- Banned vocabulary absent: a word-search confirms no list item appears as filler register, in EN or FR.
- Authored voice present: the piece states a clear point of view or recommendation, not false balance or relentless positivity.
- Hard parts covered: objections, edge cases, risks and the negative-comment / crisis path are addressed, not only the launch happy path.
- Burstiness present: sentence length and structure vary; no rule-of-three reflex, no antithesis formula, no em-dash flood.
- Localised: UGX, Mobile Money, WhatsApp-first and real local references are used for the default Uganda / East Africa market (or the named market's equivalents).
- Ship gate passed: every box is ticked before delivery.

## Anti-Patterns

- Deferring slop to a final clean-up pass. Fix: correct each banned word, placeholder or unverified figure the moment it appears.
- Treating the 25 signs as proof a human did not write it. Fix: use them as channel-aware editing prompts, not AI-authorship evidence.
- Swapping a banned word for a synonym from the same register. Fix: rewrite the sentence to be direct.
- A generic "Learn more" CTA. Fix: tie it to the real channel ("Send a WhatsApp to 0700 000 000 before Friday").
- Generic "African" placeholders in image briefs. Fix: name the setting, wardrobe, lighting and real local context, and force anatomy, text and physics correctness.
- Filling a calendar as one opaque batch. Fix: draft and gate one unit at a time.
- Relentless positivity with no trade-off. Fix: state a recommendation and the audience that will not buy.

## References

- [Guardrails, domain blocks and overlays](references/guardrails-and-overlays.md): read when applying real-time rules, the drop-in guardrail block for sub-agent briefs, the EN, FR, image/video or campaign avoidance block, the ME1-ME7 and AS1-AS7 overlays, the responsibility overlay or the see-also routes.
- [humanising-rewrite-passes](references/humanising-rewrite-passes.md): read when reviewing and rewriting an existing AI draft (caption, blog, email, strategy document, proposal) for human voice, localisation and sign-off.
- [`ai-slop-audit`](../ai-slop-audit/SKILL.md): read at each checkpoint and when a graded audit of finished work is needed.
- [AI IP and copyright policy](../../policies/policy-ai-content-ethics/references/ai-ip-and-copyright-policy.md) and [cultural bias audit protocol](../../policies/policy-ai-content-ethics/references/cultural-bias-audit-protocol.md): read when briefing image or video output.
- [AI-slop responsible publishing standard](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/references/ai-slop-responsible-publishing-standard-2026-09-11.md): read when a claim, testimonial or scenario may be deceptive.
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md): read when the request is about AI maturity rather than copy.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

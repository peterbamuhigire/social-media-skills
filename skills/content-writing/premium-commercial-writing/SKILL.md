---
name: premium-commercial-writing
description: Use when copy must read as expert and worth a premium fee, or the team needs house editorial rules or brochure copy; produces premium rewrites or critiques of pages, articles and offers, content writing standards (headlines, lede, Fog Index, you/we ratio) and panel-by-panel brochure copy; not for sales funnels (use `direct-response-funnel-copy`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Premium Commercial Writing

A cross-cutting writing layer applied alongside the primary deliverable skill: it raises ordinary content into premium commercial writing with clearer positioning, stronger proof, better buyer psychology, cleaner search structure and more confident sales argumentation.

<!-- dual-compat-start -->
## Use When
- A web page, profile, proposal or article reads cheap, generic or wordy and needs lifting so a high-value buyer finds it credible.
- We want a margin-note critique of a draft with proof gaps, weak claims and vague benefits marked.
- The team needs house writing rules for web and article copy: headlines, the lede, Fog Index readability, you/we ratio, features against benefits and scannable layout.
- We need brochure copy, such as a trifold panel by panel, with a benefit headline on the cover and one call to action.

## Do Not Use When
- `direct-response-funnel-copy` for sales pages, launch sequences and offer ladders that must convert.
- `anti-ai-slop` for stripping AI tells out of a draft.
- `seo-geo-optimisation` for page-level generative-search citation readiness.
- Stop before adding proof, awards, prices or results the client has not supplied; flag the gap rather than inflate the claim.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry, location and market context; target reader, buyer role, awareness level and platform behaviour | Client brief or the paired skill's intake | Yes | Default to British English and East African market defaults; flag the missing reader before writing. |
| Commercial job (attention, trust, lead generation, sale, price defence, search visibility, retention, referral, or investor/donor confidence) and the offer, product, service or argument | Brief or paired skill | Yes | Stop; premium copy cannot be built without a job and an offer. |
| Proof available: data, testimonials, case results, credentials, process evidence, named clients, media, awards or first-hand experience | Client source pack | Yes | Flag the gap; qualify or cut claims rather than inflate them. |
| Likely objections or risks, desired next step and post-click destination | Client or sales lead | Yes | Infer the likeliest objection, mark it assumed and ask for the destination. |
| Brand voice rules, banned vocabulary and compliance limits | `04-brand-voice-intake`; client legal | Conditional | Apply the engine's banned-word list and hold regulated claims. |
| The draft to lift or critique, when rewriting | Client or paired skill | Conditional | Build a message spine first and return it for approval. |

## Workflow

1. Classify the asset: social attention, education, authority, nurture, conversion, search discovery or sales enablement.
2. Choose the paired skill: use the most specific skill first, then apply this skill as the premium writing layer; stop if proof, offer, reader or next step is missing and flag the gap before writing.
3. Apply the editorial base from [content writing standards](references/content-writing-standards.md) (headline, lede, Fog Index readability, formatting, you/we ratio, awareness stage), or [brochure copy](references/brochure-copy.md) for print collateral.
4. Build the message spine: reader, moment, pain, desired outcome, point of view, mechanism, proof, objection, next step.
5. Select the format gate in [format-specific gates](references/format-specific-gates.md) and add the search and authority layer (direct answers, semantic depth, author and proof signals, FAQs where the format allows).
6. Run the premium edit: cut generic claims, weak modifiers, unsupported superlatives, cheap urgency and copy any competitor could publish; load the English collocation overlay before final polish.
7. Check commercial integrity (the CTA matches the reader's readiness; the offer supports the price or positioning), run the premium writing tests, correct any failure and rerun the tests before delivery.

## Five jobs of a premium asset

Premium commercial writing is not ornate language. It is disciplined, buyer-centred, specific and commercially useful. Every premium asset must:

1. **Position:** make clear who the client is for, what they solve, and why they are not interchangeable.
2. **Diagnose:** name the reader's situation better than a generic competitor would.
3. **Prove:** support claims with concrete evidence, not adjectives.
4. **Guide:** make the next step feel obvious, valuable and appropriately low-friction.
5. **Compound:** improve search, trust, sales follow-up and future repurposing value.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Premium rewrite of the asset, or upgraded hooks, headlines, CTAs, proof blocks or offer framing | Client reviewer; the paired skill | Passes the six premium writing tests with no invented proof. |
| Margin-note critique with recommended edits | Client or copywriter | Marks proof gaps, weak claims and vague benefits with a specific fix each. |
| Message spine before drafting | Paired skill; client approver | All nine spine fields filled or flagged. |
| Content writing standards or premium quality gate checklist | In-house writing team | Covers headlines, lede, Fog Index, you/we ratio, features against benefits and scannable layout. |
| Brochure copy panel by panel, or a search/GEO-ready long-form structure | Designer; web editor | Brochure has a benefit headline on the cover and one call to action; long-form exposes an extractable main answer. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Proof register | Inline table: claim, evidence, source | Every important claim has evidence, example, mechanism or source, or is qualified or cut. |
| Premium test record | Checklist of the six tests | Each test shows pass, or the rewrite made. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Adding awards, prices, named clients or results the client has not supplied is out of scope.

## Degraded Mode

Without supplied proof and a defined reader, return the narrowest qualified result and mark the affected checks `not assessed`. A message spine and a margin-note critique naming the missing proof can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Any page, post, article or email needs the editorial basics (headline, lede, readability, formatting, you/we ratio, awareness stage) | Apply [content writing standards](references/content-writing-standards.md) before the premium layer. | Premium polish on copy that fails basic readability and reader focus. |
| The asset is a brochure, trifold, booklet or print leave-behind | Follow [brochure copy](references/brochure-copy.md): single purpose, eight elements, panel plan, designer brief. | A company-history brochure with no benefit headline, proof or next step. |
| Proof, offer, reader or next step is missing | Flag the gap before writing; never inflate a claim to fill it. | Premium-sounding copy built on vague claims. |
| A competitor could use the copy unchanged | Rewrite with the client's specific mechanism, proof and point of view. | Interchangeable, commodity positioning. |
| The copy relies on discounts or cheap urgency to sell | Rebuild value with [value, proof and offer architecture](references/value-proof-and-offer-architecture.md). | Price erosion and a discount-dependent brand. |
| The deliverable is a sales page, launch sequence or high-ticket funnel | Route to `direct-response-funnel-copy` and apply this skill as the premium layer. | Brand copy that never converts. |
| Copy persuades a buyer to act | Use the ethical choice architecture and conversion guardrails in [buyer psychology and social selling](references/buyer-psychology-and-social-selling.md) and the ethics filter. | Manipulation and unsupported claims. |

## Quality Standards

- The copy has one clear reader, commercial job, message and next step.
- The opening earns attention without hype, vague trend language or throat-clearing.
- Benefits are tied to a mechanism and proof, not stated as unsupported promises; every important claim passes the proof test.
- The asset contains a distinct point of view or diagnostic insight and passes the specificity test.
- The reader gains useful insight before being asked to act, and the copy increases perceived value without discount dependency.
- SEO/GEO structure is applied where the format supports it, so a human or AI system can extract the main answer quickly.
- Price, value, risk or effort objections are addressed directly when relevant.
- British English and East African market defaults apply unless the brief says otherwise; the piece sounds like a skilled human expert wrote it for a specific audience and passes the `anti-ai-slop` gate.

## Anti-Patterns

- Mistaking ornate language for premium writing. Fix: write disciplined, buyer-centred, specific copy.
- Stating benefits as adjectives without evidence. Fix: attach a mechanism, example or source, or cut the claim.
- Adding a price, award, result or quotation without a traceable source. Fix: verify it or qualify/remove it.
- Cheap urgency or unsupported superlatives in premium copy. Fix: remove them in the premium edit and let proof carry the argument.
- Applying the premium layer before the specific paired skill. Fix: run the most specific skill first, then this layer.
- Publishing or sending from drafting authority alone. Fix: obtain explicit action-specific authority and retain the approval record.

## References

- [Premium operating standard](references/premium-operating-standard.md): read when asking the full intake questions, applying the premium writing tests, choosing an output option or pairing this skill with another.
- [Premium writing system](references/premium-writing-system.md): read when a draft is accurate but ordinary, vague, cheap-sounding, too corporate or commercially weak.
- [Content writing standards](references/content-writing-standards.md): read when writing or editing any page, post, article or email and you need the editorial base rules (headlines, ledes, readability, scannable formatting, templates, pre-publication checklist).
- [Format-specific gates](references/format-specific-gates.md): read before delivering copy in a given format.
- [Search and authority layer](references/search-and-authority-layer.md): read when writing must support SEO, Generative Engine Optimisation, thought leadership or AI-search citation.
- [Value, proof and offer architecture](references/value-proof-and-offer-architecture.md): read when copy must justify a premium price, sell a high-ticket offer, support a proposal or move buyers away from price comparison.
- [Buyer psychology and social selling](references/buyer-psychology-and-social-selling.md): read when working on ethical choice architecture, proof, memory cues, channel adaptation and conversion guardrails.
- [Brochure copy](references/brochure-copy.md): read when the deliverable is a brochure, trifold, booklet or other print sales collateral.
- [English collocations and lexical precision](../../language/language-standards/references/english-collocations-and-lexical-precision-2026-09-02.md): read before final polish; use precise, channel-native language with evidence-calibrated claims and no forced hype or slang.
- [Human, professional phrase bank](../references/human-professional-phrase-bank.md): read when shaping sentence patterns for posts, ads, emails, pages, rate cards and plans.
- [Direct-marketing ethics filter](../references/direct-marketing-ethics-filter.md): read before releasing any selling copy; the screen is mandatory.
- [`direct-response-funnel-copy`](../direct-response-funnel-copy/SKILL.md): read when the asset must convert through a funnel.
- [`caption-writer`](../caption-writer/SKILL.md): read when routing is unclear; it is the nearest neighbour.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when stripping AI tells and before client delivery.
- [Repository agent guide](../../../AGENTS.md): read when a premium claim touches the engine-wide market or safety gates.
<!-- dual-compat-end -->

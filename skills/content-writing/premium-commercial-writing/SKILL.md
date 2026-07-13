---
name: premium-commercial-writing
description: Use when Premium Commercial Writing is needed to produce a premium commercial writing deliverable for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Premium Commercial Writing

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **premium commercial writing deliverable** and the supplied brief falls within premium commercial writing.

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
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified premium commercial writing deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Channel, format and audience commitment level are known | Choose the hook, structure and call to action native to that context. | Copy that could be pasted unchanged onto any channel or brand. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact premium commercial writing deliverable, consumer, market, channel and approval boundary; route to `caption-writer` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete premium commercial writing deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Premium commercial writing deliverable | Requester, client reviewer or delivery team | The premium commercial writing deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested premium commercial writing deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [caption-writer](../caption-writer/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Use this as a cross-cutting writing layer alongside the primary deliverable skill. It raises ordinary content into premium commercial writing: clearer positioning, stronger proof, better buyer psychology, cleaner search structure, and more confident sales argumentation.

## Required Input
Ask for or infer these before upgrading copy:

- Client name, industry, location, and market context.
- Target reader, buyer role, awareness level, and platform behaviour.
- Commercial job: attention, trust, lead generation, sale, price defence, search visibility, retention, referral, or investor/donor confidence.
- Offer, product, service, or argument being promoted.
- Proof available: data, testimonials, case results, credentials, process evidence, named clients, media, awards, or first-hand experience.
- Objections or risks the reader is likely to have.
- Desired next step and post-click destination.
- Brand voice rules, banned vocabulary, and compliance limits.

If proof, offer, reader, or next step is missing, flag the gap before writing. Premium copy cannot be built from vague claims.

## Operating Standard
Premium commercial writing is not ornate language. It is disciplined, buyer-centred, specific, and commercially useful.

Every premium asset must do five jobs:

1. **Position:** make clear who the client is for, what they solve, and why they are not interchangeable.
2. **Diagnose:** name the reader's situation better than a generic competitor would.
3. **Prove:** support claims with concrete evidence, not adjectives.
4. **Guide:** make the next step feel obvious, valuable, and appropriately low-friction.
5. **Compound:** improve search, trust, sales follow-up, and future repurposing value.

## Workflow
1. **Classify the asset.** Identify whether the piece is primarily for social attention, education, authority, nurture, conversion, search discovery, or sales enablement.
2. **Choose the paired skill.** Use the most specific skill first, then apply this skill as the premium writing layer.
3. **Build the message spine:** reader, moment, pain, desired outcome, point of view, mechanism, proof, objection, next step.
4. **Select the format gate.** Use `references/format-specific-gates.md` for the relevant asset type.
5. **Add the search and authority layer.** Use direct answers, semantic depth, author/proof signals, and FAQs where the format allows.
6. **Run the premium edit.** Cut generic claims, weak modifiers, unsupported superlatives, cheap urgency, and copy that sounds like any competitor could publish it.
7. **Check commercial integrity.** Confirm the CTA matches the reader's readiness and the offer supports the price or positioning.

## Premium Writing Tests
- **Specificity test:** Could a competitor use the same copy unchanged? If yes, rewrite.
- **Proof test:** Does every important claim have evidence, example, mechanism, or source? If not, qualify or cut.
- **Reader value test:** Does the reader gain useful insight before being asked to act?
- **Price integrity test:** Does the copy increase perceived value without discount dependency?
- **Search answer test:** Can a human or AI system extract the main answer, offer, or expertise quickly?
- **Human voice test:** Does it sound like a skilled person with judgement, not a neutral content machine?

## Output Options
Depending on the request, deliver one of:

- a premium rewrite of the asset
- a margin-note critique with recommended edits
- a message spine before drafting
- a premium quality gate checklist
- upgraded hooks, headlines, CTAs, proof blocks, or offer framing
- a search/GEO-ready structure for long-form content

## Integration
Use this skill alongside:

- `content-writing` for readability and broad editorial standards.
- `caption-writer` for social captions and post copy.
- `blog-writer` for articles and thought leadership.
- `content-whitepaper-ebook` for long-form lead magnets and expert documents.
- `copywriting-brochure` for sales collateral.
- `email-copywriter` and `platform-whatsapp` for owned-audience nurture.
- `09-campaign-strategy` and `13-campaign-brief` for campaign message architecture.
- `direct-response-funnel-copy` for sales pages, launch sequences, and high-ticket funnels.
- `seo-geo-optimisation` and `ai-generative-search-optimisation` for AI-search visibility.
- `premium-social-selling` for executive, affluent, enterprise, and high-ticket buyers.

## Quality Criteria
- [ ] The copy has one clear reader, commercial job, message, and next step.
- [ ] The opening earns attention without hype, vague trend language, or throat-clearing.
- [ ] Benefits are tied to a mechanism and proof, not stated as unsupported promises.
- [ ] The asset contains a distinct point of view or diagnostic insight.
- [ ] SEO/GEO structure is applied where the format supports it.
- [ ] Price, value, risk, or effort objections are addressed directly when relevant.
- [ ] British English and East African market defaults are applied unless the brief says otherwise.
- [ ] The piece sounds like a skilled human expert wrote it for a specific audience.

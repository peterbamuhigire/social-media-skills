---
name: french-native-copy
description: Use when French Native Copy (Social) is needed to produce a publication-ready copy for social-media or digital-marketing work; use `east-african-english` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# French Native Copy (Social)

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **publication-ready copy** and the supplied brief falls within french native copy (social).

## Do Not Use When
- Use `east-african-english` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Source copy, target language or register, market, audience and protected terminology | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified publication-ready copy; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Market, language variety and audience register are confirmed | Use the named regional standard and preserve meaning, terminology and voice. | Literal or culturally misplaced copy presented as native-quality language. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact publication-ready copy, consumer, market, channel and approval boundary; route to `east-african-english` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete publication-ready copy; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Publication-ready copy | Requester, client reviewer or delivery team | The publication-ready copy addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested publication-ready copy, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [east-african-english](../east-african-english/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

This is the French execution layer for the social engine. It owns *how French reads*; `language-standards` owns the cross-language tone policy. For website/long-form French, the sister skill lives in the website engine (`content-copy/french-native-copy`).

## Required Input
- The source material the French copy must convey: approved English caption/brief, the brand voice, or raw client facts.
- The audience and market: France, Francophone Africa (and which country), Canada, or mixed. This sets vocabulary, register defaults, currency/date conventions.
- The register decision: `vous` (default) or `tu` (youth/lifestyle). The platform and post type (caption, hook, ad, bio).

## Quality standards
- A French native reader finds nothing that signals translation: no calques, no anglicisms, no English word order or punctuation spacing.
- Register is consistent across the post and its replies; every verb, pronoun, possessive agrees with the chosen `tu`/`vous`.
- Every adjective agrees in gender and number; partitives correct and collapse to `de` after negation/quantity.
- Typography follows French rules; prices read `12 500 FCFA` or `1 250,00 €`, not `€1,250.00`.
- Hashtags and discovery phrases are what a French speaker actually searches, not transposed English.
- The copy passes the back-translation test: French → English reproduces the intended meaning without distortion.

## Notes
- Francophone Africa is the default French market: target `Afrique francophone` broadly (Côte d'Ivoire, Sénégal, Cameroun, RDC, Guinée, Mali, Burkina, Gabon, Bénin, Togo…), `FCFA` currency, OHADA/SYSCOHADA frameworks where relevant — not France-centric or Québécois vocabulary. See `language-standards` for the full geographic policy.
- Source material distilled from: Annie Heminway, *Practice Makes Perfect — Complete French Grammar*; Boulares & Frérot, *Grammaire progressive du français — Niveau avancé*; *Learn French II — Parallel Text*; and the *French–English Bilingual Visual Dictionary* (DK). See `book-extractions/french-language-books-extraction-2026.md`.

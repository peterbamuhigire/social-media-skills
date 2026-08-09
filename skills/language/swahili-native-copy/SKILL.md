---
name: swahili-native-copy
description: Use when Swahili Native Copy (Social) is needed to produce a publication-ready copy for social-media or digital-marketing work; use `east-african-english` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Swahili Native Copy (Social)

## Target Markets (Standard)

Kiswahili content from this engine targets East and Central Africa. Primary: Kenya, Tanzania. Secondary: DR Congo. Tertiary: Uganda (limited), Rwanda, Burundi.

The reader is an educated professional with advanced Kiswahili comprehension. Use respectful Kiswahili sanifu — no Sheng, no Mombasa dialect, no Zanzibari variants. Default to terms most widely understood across Kenya and Tanzania.

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **publication-ready copy** and the supplied brief falls within swahili native copy (social).

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

This is the Kiswahili execution layer for the social engine. It owns *how Kiswahili reads*; `language-standards` owns the cross-language tone policy. For website/long-form Kiswahili, the sister skill lives in the website engine (`content-copy/swahili-native-copy`).

## Required Input
- The source material the Kiswahili copy must convey: approved English caption/brief, the brand voice, or raw client facts.
- The audience and market: Tanzania, Kenya, or wider East African/regional. This sets vocabulary depth, code-switching tolerance, and trust conventions.
- The register: standard respectful `Kiswahili sanifu` (default) or a warmer/youthful voice. The platform and post type.

## Quality standards
- Concord is correct everywhere: `huduma bora`, `bidhaa zetu`, `mteja wetu` agree by class, with no English-word-order or default-class errors.
- Register is respectful and consistent; greetings, address, and CTAs match `Kiswahili sanifu`; no accidental slip into slang or another dialect mid-post.
- Loanwords follow native norms: integrated Arabic loans used freely; modern terms in their Swahili forms (`barua pepe`, `tovuti`, `mtandaoni`); bare English avoided.
- Spelling is standard: correct `ng'`, `ny`, `ch`, `dh`, `gh`, `th`; no English-influenced spellings.
- The Swahili clock is converted correctly for any time/opening-hours copy.
- The copy passes the back-translation test: Swahili → English reproduces the intended meaning without distortion.

## Notes
- Relationship before the transaction: open warm (`Karibu`), lead with respect (`heshima`), then the offer. Inclusive `tu-` framing (`Tujenge pamoja`) resonates more than commands. See `language-standards` for the cross-language policy.
- Source material distilled from: Peter M. Wilson, *Simplified Swahili*; *Rough Guide Phrasebook — Swahili* (Lexus); John M. Mugane, *The Story of Swahili*; Derek Nurse & Thomas Spear, *The Swahili*; Johannes Fabian, *Language and Colonial Power*; *Authentic East African Swahili Cuisine* (Malaquias); and the *Trilingual Story Book* (Aames). See `book-extractions/swahili-language-books-extraction-2026.md`.

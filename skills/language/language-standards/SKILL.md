---
name: language-standards
description: 'Use when an agency or brand needs one tone and grammar rulebook for social and ad copy across English, French and Kiswahili: spelling, dates, numbers, courtesy, words to avoid and CTAs; produces the multilingual copy style specification; not for editing English posts for East African readers (use `east-african-english`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Language Standards — Multi-Language Tone & Grammar

Cross-cutting tone and grammar policy for English, French and Kiswahili copy: every caption, CTA, description and microcopy line follows the standard for its language, and native execution belongs to the dedicated native-copy skills.

<!-- dual-compat-start -->
## Use When
- Writers produce English, French and Kiswahili (Swahili) posts in different styles and the client wants one set of rules for all three.
- A new market launch needs agreed spelling, date and number formats and call-to-action button wording in each language.
- The team keeps using hype and AI-sounding phrases in every language and needs a banned-words and redundant-phrase list.
- Translated campaign copy needs checking for register, text expansion and whether an in-country reviewer is required.

## Do Not Use When
- `east-african-english` for editing English posts and ads for East African readers.
- `french-native-copy` or `swahili-native-copy` for writing the French or Kiswahili campaign copy itself.
- Stop short of certifying translation accuracy, publishing or spending; name the in-country reviewer still required and return the draft for client approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Source text or deliverable brief | Requester or approved brief | Yes | Stop; a style specification needs real copy or a brief to apply to. |
| Target language(s) and market(s) | Client or brief | Yes | If the target language is unclear, stop and establish it; if only the market is unclear, use the default audiences below. |
| Channel and copy types (captions, ads, CTAs, microcopy, email) | Brief | Yes | Cover captions and CTAs and mark other copy types `not assessed`. |
| Brand voice, protected terms and client vocabulary | Client source pack | Conditional | Apply the neutral professional register for each language and list the terms still to confirm. |
| In-country reviewer per non-English language | Client or agency | Yes before release | Name the reviewer profile still required (target-market francophone; East African Kiswahili speaker) and return the draft for approval. |

## Workflow

1. Confirm the source text, languages, markets, channel and approval owner; route single-language execution to `east-african-english`, `french-native-copy` or `swahili-native-copy`, and stop if the target language is unclear.
2. Fix the audience per language from the default table below, departing from it only where the brief explicitly names different markets.
3. Set the per-language rules for spelling, dates, numbers, currency, courtesy, register and CTAs from the [English](references/english-en-standard.md), [French](references/french-fr-standard.md) and [Kiswahili](references/kiswahili-sw-standard.md) standards.
4. Add the banned-word tiers, banned phrases, structural patterns and redundant-phrase list from [AI language and redundancy](references/ai-language-and-redundancy.md), and the English craft layer from the [human English craft standard](references/human-english-craft-standard.md).
5. Plan text expansion for layouts (French 1.3x, Kiswahili 1.2x) and note the in-country reviewer each language needs.
6. Test sample copy in each language against the quality checks; where a check fails, correct the rule or the sample and rerun the check.
7. Run the `anti-ai-slop` ship gate and return the specification with the reviewers still required; stop short of certifying translation accuracy, publishing or spending.

## Default audiences by language

| Locale | Primary Markets | Secondary Markets | Register |
|--------|----------------|-------------------|----------|
| **English** | East Africa (Uganda, Kenya, Tanzania, Rwanda) | All English-speaking Africa and global English speakers | British-influenced East African professional English; clear, direct, respectful; globally readable |
| **French** | DRC, Congo-Brazzaville, Burundi, Senegal, Mali, Côte d'Ivoire, Togo, Cameroon, Gabon, Madagascar | All francophone Africa (Bénin, Burkina Faso, Niger, Guinea, Djibouti, Comoros, Chad, Central African Republic) | Formal vous; francophone African professional French; never France-centric, never Québécois |
| **Kiswahili** | Kenya, Tanzania, DR Congo | Uganda (limited), Rwanda, Burundi, Mozambique (Kiswahili speakers) | Respectful Kiswahili sanifu; no slang, no Sheng, no regional dialect drift |

Readers in every language are educated professionals with advanced comprehension (often L2/L3): do not simplify, over-explain or patronise. Core principles for all languages: clear and direct, formal and respectful, no excessive marketing language, professionally indirect, measured confidence, culturally authentic. Full reader profiles and rules: [target audiences and scope](references/target-audiences-and-scope.md).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Multilingual copy style specification (per-language spelling, dates, numbers, currency, courtesy, register, vocabulary and CTAs) | Client lead; writers in each language | Each enabled language has its own section; every rule matches the language standard or records a brief-approved departure. |
| Banned-word and redundant-phrase list | Writers; `anti-ai-slop` reviewer | Tier 1–3 words, banned phrases and structural patterns are listed with the replacements. |
| Reviewer and expansion note | Designer; approver | Names the in-country reviewer each language needs and the layout expansion factor. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Per-language check record | Checklist per language with sample lines | Each quality check is marked pass, fail or `not assessed`; none is silently passed. |
| Reviewer register | Table: language, market, reviewer, date | Unreviewed French or Kiswahili is recorded as awaiting review. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. This skill does not certify translation accuracy; that needs a named in-country reviewer.

## Degraded Mode

Without a confirmed target language or an in-country reviewer, return the narrowest qualified result and mark the affected checks `not assessed`. The English specification and the cross-language banned-word list can still be delivered, with French and Kiswahili sections marked awaiting review.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Brief does not name markets | Use the default audiences table; do not deviate unless the brief explicitly names different markets. | Copy positioned for the wrong readers. |
| French content for a Uganda-based client | English pages serve the Ugandan/East African audience; French targets francophone Africa broadly ("Afrique francophone", OHADA, BCEAO/BEAC, FCFA), never Uganda or East Africa only. | French pages that reach no francophone market. |
| Kiswahili content is requested | Target Kenya and Tanzania first, DR Congo second; do not assume Ugandan readers. | Misjudged readership for Swahili content. |
| French or Kiswahili copy must be produced | Route to `french-native-copy` or `swahili-native-copy`; never raw-translate from English. | Copy that reads as translated rather than authored. |
| French or Kiswahili copy is ready for release | Send it to a native reviewer from the target market before publishing. | Unreviewed regional errors going live. |
| Strings with apostrophes go into Astro JSX template expressions | Use double-quoted strings or template literals; never `’` escapes or `\'` in template JSX. | A broken site build from French `d'` or Swahili `ng'`. |
| A required fact or approval is missing | Stop that claim; request it or leave an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |

## Quality Standards

- English: British spelling, East African tone, day-month-year dates, no marketing hype.
- French: formal French, `vous` throughout, francophone African vocabulary, correct diacritics and agreement, reviewed by a francophone from the target market.
- Kiswahili: standard Kiswahili, formal register, no slang or Sheng, reviewed by an East African native speaker.
- All languages: no truncation or text overflow; layouts allow French 1.3x and Kiswahili 1.2x expansion.
- All languages: grammatically correct, properly punctuated and culturally appropriate.
- All languages: CTAs use respectful, inviting language, not aggressive.
- No Tier 1 banned words or banned phrases; at most one Tier 3 word per paragraph; the `anti-ai-slop` ship gate is passed.
- Names, figures, quotations and platform rules are verified before use.

## Anti-Patterns

- Writing one language by translating another word for word. Fix: author each language from meaning, through its native-copy skill.
- Positioning French for Paris or for East Africa only. Fix: use "Afrique francophone" and West and Central African institutions and examples.
- Using American dates or thousands separators in French and Kiswahili. Fix: apply each language's date and number rules from its standard.
- Letting AI-tell vocabulary through in any language. Fix: screen against the tier lists, banned phrases and structural patterns.
- Designing buttons for English label length only. Fix: allow 1.3x for French and 1.2x for Kiswahili.
- Treating missing native-language review as approval. Fix: mark the check `not assessed` and name the reviewer still required.
- Publishing, sending or spending from drafting authority alone. Fix: obtain explicit action-specific authority and keep the approval record.

## References

- [Target audiences and scope](references/target-audiences-and-scope.md): read when confirming default markets, reader profiles, core principles or which skill executes the copy.
- [English (en) standard](references/english-en-standard.md): read when setting English spelling, dates, country tone, courteous phrases, vocabulary or CTAs.
- [French (fr) standard](references/french-fr-standard.md): read when setting French grammar, dates, registers, vocabulary, CTAs, expansion or the francophone Africa geographic scope.
- [Kiswahili (sw) standard](references/kiswahili-sw-standard.md): read when setting Kiswahili grammar, register, dates, courtesy, vocabulary, CTAs or dialect rules.
- [AI language and redundancy](references/ai-language-and-redundancy.md): read when screening any language for AI-tell words, banned phrases or redundant constructions.
- [Human English craft standard](references/human-english-craft-standard.md): read before drafting English and again at the proof pass.
- [English collocations and lexical precision](references/english-collocations-and-lexical-precision-2026-09-02.md): read when checking English collocations, register and word choice.
- [Business English advanced](references/business-english-advanced.md): read when phrase banks, ESL grammar checks, register switching or anti-jargon rewrites are needed.
- [`east-african-english`](../east-african-english/SKILL.md), [`french-native-copy`](../french-native-copy/SKILL.md), [`swahili-native-copy`](../swahili-native-copy/SKILL.md): read when executing copy in one language.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read before release.
- [Repository agent guide](../../../AGENTS.md): read when the engine-wide market, safety and anti-slop gates apply.
<!-- dual-compat-end -->

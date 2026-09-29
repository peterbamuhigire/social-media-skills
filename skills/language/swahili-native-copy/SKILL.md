---
name: swahili-native-copy
description: Use when social posts, ads, captions or WhatsApp messages must be written in Kiswahili for Kenya, Tanzania or eastern DRC in respectful standard Kiswahili, not Sheng; produces publish-ready Kiswahili copy with a native-review note; not for the multilingual tone policy (use `language-standards`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Swahili Native Copy (Social)

Kiswahili execution layer for the social engine: it owns how Kiswahili reads for East and Central African readers, while `language-standards` owns the cross-language tone policy. The reader is an educated professional with advanced Kiswahili comprehension.

<!-- dual-compat-start -->
## Use When
- A campaign in Kenya or Tanzania needs Kiswahili posts, captions or ad lines that read naturally, not as a literal translation.
- Copy must use Kiswahili sanifu understood across Nairobi and Dar es Salaam, avoiding Sheng and coastal dialects.
- Booking, price, signage, food or farming messages need the right Kiswahili terms and shilling formats.
- A Kiswahili draft needs a native reviewer's check before the client approves it.

## Do Not Use When
- `language-standards` for the cross-language tone and grammar rulebook.
- `east-african-english` when the copy is in English.
- `french-native-copy` when the audience is francophone Africa.
- Stop before publishing Kiswahili copy without native review; deliver it marked as awaiting review.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Source material the Kiswahili must convey: approved English caption or brief, brand voice, or raw client facts | Requester or approved brief | Yes | Stop; do not adapt an English caption the client has not approved. |
| Audience and market: Tanzania, Kenya, or wider East African/regional; this sets vocabulary depth, code-switching tolerance and trust conventions | Client or brief | Yes | Default to terms most widely understood across Kenya and Tanzania and record the market as unconfirmed. |
| Register: standard respectful `Kiswahili sanifu` (default) or a warmer/youthful voice | Brief or brand voice | Yes | Use respectful `Kiswahili sanifu`; no Sheng, no Mombasa dialect, no Zanzibari variants. |
| Platform and post type (caption, hook, ad, bio, WhatsApp message) | Brief | Yes | Draft a caption-length version and mark platform limits `not assessed`. |
| Offer facts, prices, opening hours and protected terminology | Client source pack or authorised owner | Conditional | Use a visible placeholder such as `[BEI]`; never invent a price, time or result. |
| Fluent Kiswahili reviewer | Client or agency | Yes before release | Deliver the copy marked awaiting native review. |

## Workflow

1. Confirm the source material, market, register, platform and approval owner; route to `east-african-english` or `french-native-copy` if the copy should not be in Kiswahili, and stop if the objective or audience is unknowable.
2. Set the register and openings with [register and greetings](references/register-and-greetings.md): relationship before the transaction, open warm (`Karibu`), lead with respect (`heshima`), then the offer.
3. Draft with correct concord from [noun classes and concord](references/noun-classes-and-concord.md) and verbs, moods and CTAs from [verb system and politeness](references/verb-system-and-politeness.md); prefer inclusive `tu-` framing (`Tujenge pamoja`) to commands.
4. Replace bare English with established Swahili forms using [loanwords and anglicisms](references/loanwords-and-anglicisms.md) and sector terms from [service and sector vocabulary](references/service-and-sector-vocabulary.md).
5. Convert every time, price and date with [numbers, time and hooks](references/numbers-time-and-hooks.md), including the six-hour Swahili clock offset.
6. Add hooks, collocations and hashtags from [idiom and hooks](references/idiom-and-hooks.md), then run the back-translation test (Swahili to English); where meaning drifts, correct the Kiswahili and rerun the test until it holds.
7. Run the `anti-ai-slop` ship gate and hand over the copy with its native-review state; stop before publication while review is outstanding.

## Market standard and sources

- Target markets (standard): East and Central Africa. Primary: Kenya, Tanzania. Secondary: DR Congo. Tertiary: Uganda (limited), Rwanda, Burundi.
- Website and long-form Kiswahili live in the website engine's sister skill (`content-copy/swahili-native-copy`).
- Source material distilled from: Peter M. Wilson, *Simplified Swahili*; *Rough Guide Phrasebook — Swahili* (Lexus); John M. Mugane, *The Story of Swahili*; Derek Nurse & Thomas Spear, *The Swahili*; Johannes Fabian, *Language and Colonial Power*; *Authentic East African Swahili Cuisine* (Malaquias); and the *Trilingual Story Book* (Aames).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Publish-ready Kiswahili copy per platform and post type | Client reviewer; community manager | Concord, register, spelling, loanwords and clock conversions pass the checks below; no invented facts. |
| Native-review note | Approver | Names the market, register, reviewer and review date, or states the review is `not assessed`. |
| Adaptation note | Client reviewer | Lists placeholders, adapted idioms and any claim still awaiting a source or authority. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Back-translation check | Kiswahili line beside its English back-translation | Meaning matches the approved source without distortion. |
| Time and price conversion log | Table: Western time or figure, Swahili rendering | Every opening hour and price in the copy appears with its conversion. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Drafting Kiswahili copy within the supplied brief is permitted; certifying native quality is not.

## Degraded Mode

Without a fluent Kiswahili reviewer or a confirmed market, return the narrowest qualified result and mark the affected checks `not assessed`. A `Kiswahili sanifu` draft with placeholders, clock conversions and a back-translation can still be delivered, marked awaiting review.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Market not named, or mixed Kenya and Tanzania | Use the terms most widely understood across both; mark (K) and (T) variants where usage differs. | Copy that reads as foreign in one of the two main markets. |
| Brief asks for a youthful voice | Warm the tone within `Kiswahili sanifu`; do not switch to Sheng or a coastal dialect. | Slang that excludes or offends the professional reader. |
| Copy states opening hours or a deadline | Convert to the Swahili clock (9 am–5 pm becomes `saa tatu asubuhi hadi saa kumi na moja jioni`); pair it with international time for urban or mixed audiences. | The most common factual error in Swahili copy. |
| A modern or technology term appears | Use the established Swahili form (`barua pepe`, `tovuti`, `mtandaoni`); keep integrated Arabic loans. | Bare-English calques that mark translated copy. |
| A price, result or approval is missing | Stop that claim; request it or leave a visible placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| No fluent reviewer is available | Deliver as awaiting review and mark native review `not assessed`. | Treating unreviewed copy as native quality. |

## Quality Standards

- Concord is correct everywhere: `huduma bora`, `bidhaa zetu`, `mteja wetu` agree by class, with no English-word-order or default-class errors.
- Register is respectful and consistent; greetings, address and CTAs match `Kiswahili sanifu`; no accidental slip into slang or another dialect mid-post.
- Loanwords follow native norms: integrated Arabic loans used freely; modern terms in their Swahili forms (`barua pepe`, `tovuti`, `mtandaoni`); bare English avoided.
- Spelling is standard: correct `ng'`, `ny`, `ch`, `dh`, `gh`, `th`; no English-influenced spellings.
- The Swahili clock is converted correctly for any time or opening-hours copy.
- The copy passes the back-translation test: Swahili to English reproduces the intended meaning without distortion.
- Names, figures, quotations and platform rules are verified before use; notes to the client are in British English.
- The `anti-ai-slop` ship gate is run; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns

- Translating the English caption word for word. Fix: rebuild the hook and CTA with native collocations and `tu-` framing.
- Writing `saa tisa hadi saa tano` for 9 am–5 pm. Fix: convert with the six-hour offset and pair with international time where the audience is mixed.
- Number-noun concord errors such as `vikombe mbili`. Fix: agree the number with the noun class (`vikombe viwili`).
- Opening with the offer. Fix: greet and show respect first, then present the offer.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. Fix: verify it, or qualify or remove it.
- Treating missing native-language review as approval. Fix: mark the check `not assessed` and deliver the copy as awaiting review.
- Publishing, sending or changing a live account from drafting authority alone. Fix: obtain explicit action-specific authority and keep the approval record.

## References

- [Register and greetings](references/register-and-greetings.md): read when choosing the brand voice, openings and forms of address.
- [Noun classes and concord](references/noun-classes-and-concord.md): read when any phrase has a noun with an adjective, possessive, number or verb.
- [Verb system and politeness](references/verb-system-and-politeness.md): read when writing CTAs, instructions, offers or negatives.
- [Loanwords and anglicisms](references/loanwords-and-anglicisms.md): read when the copy carries technology, business or modern-life terms.
- [Numbers, time and hooks](references/numbers-time-and-hooks.md): read when writing prices, opening hours, dates or deadlines.
- [Idiom and hooks](references/idiom-and-hooks.md): read when the Kiswahili is correct but flat, or when drafting hooks, proverbs and hashtags.
- [Service and sector vocabulary](references/service-and-sector-vocabulary.md): read for booking, signage, price and food/agriculture copy.
- [`language-standards`](../language-standards/SKILL.md): read when the cross-language tone policy is in question.
- [`east-african-english`](../east-african-english/SKILL.md): read when the copy should stay in English.
- [`french-native-copy`](../french-native-copy/SKILL.md): read when the audience is francophone Africa.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read before release.
- [Repository agent guide](../../../AGENTS.md): read when the engine-wide market, safety and anti-slop gates apply.
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

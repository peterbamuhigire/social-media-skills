---
name: french-native-copy
description: Use when social posts, ads or captions must be written or adapted in French for francophone Africa (DRC, Senegal, Côte d'Ivoire, Cameroon) in a formal vous register with FCFA and OHADA context; produces publish-ready French copy with a native-review note; not for the multilingual tone policy (use `language-standards`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# French Native Copy (Social)

French execution layer for the social engine: it owns how French reads for **francophone Africa**, not France, while `language-standards` owns the cross-language tone policy. The reader is an educated professional with advanced French comprehension; never assume the reader is in Paris.

<!-- dual-compat-start -->
## Use When
- A campaign needs French posts, captions or ad lines for Kinshasa, Dakar, Abidjan, Douala or Bujumbura, not for readers in France.
- English social copy must be adapted into natural French rather than translated word for word, keeping the formal vous register.
- Prices, dates and institutions must follow francophone African usage: FCFA, BCEAO or BEAC, OHADA and local mobile money names.
- A French draft needs a native reviewer's check on grammar, gender agreement and identity details before the client sees it.

## Do Not Use When
- `language-standards` for the cross-language tone and grammar rulebook.
- `east-african-english` when the copy stays in English for East African readers.
- `swahili-native-copy` when the target language is Kiswahili.
- Stop before publishing French copy that no native reviewer has checked; deliver it marked as awaiting review.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Source material the French must convey: approved English caption or brief, brand voice, or raw client facts | Requester or approved brief | Yes | Stop; do not adapt an English caption the client has not approved. |
| Audience and market: France, francophone Africa (and which country), Canada or mixed; this sets vocabulary, register defaults and currency/date conventions | Client or brief | Yes | Default to francophone Africa broadly (FCFA, OHADA) and record the country as unconfirmed. |
| Register decision: `vous` (default) or `tu` (youth/lifestyle) | Brief or brand voice | Yes | Use formal `vous` and hold it across the post and its replies. |
| Platform and post type (caption, hook, ad, bio) | Brief | Yes | Draft a caption-length version and mark platform limits `not assessed`. |
| Offer facts, prices, names and protected terminology | Client source pack or authorised owner | Conditional | Use a visible placeholder such as `[PRIX]`; never invent a price, result or name. |
| Fluent French reviewer | Client or agency | Yes before release | Deliver the copy marked awaiting review, with `native_review: not-assessed`. |

## Workflow

1. Confirm the source material, market, register, platform and approval owner; route to `east-african-english` or `swahili-native-copy` if the copy should not be in French, and stop if the objective or audience is unknowable.
2. Fix the market conventions before drafting: francophone Africa by default (formal `vous`; OHADA, BCEAO/BEAC, FCFA and local mobile money names, not France-specific institutions), or the market the requester names.
3. Choose `vous` or `tu` with [register and address](references/register-and-address.md) and record the choice.
4. Adapt, do not translate: rebuild hooks, connectors and CTAs with [idiom and hooks](references/idiom-and-hooks.md) and sector terms with [vocabulary by theme](references/vocabulary-by-theme.md).
5. Proofread against [grammar pitfalls](references/grammar-pitfalls.md), [anglicisms to avoid](references/anglicisms-to-avoid.md) and [typography and formatting](references/typography-and-formatting.md): agreement, partitives, spacing, prices and dates.
6. Run the back-translation test (French to English); where meaning drifts, correct the French and rerun the test until it holds.
7. Run the `anti-ai-slop` ship gate, complete the [identity and register review](references/identity-and-register-review.md) record, and hand over the copy with its native-review state; stop before publication while review is outstanding.

## Market standard and sources

- Primary markets (standard): DRC, Congo-Brazzaville, Burundi, Senegal, Mali, Côte d'Ivoire, Togo, Cameroon, Gabon, Madagascar, Bénin, Burkina Faso, Niger, Guinea, Djibouti, Comoros. Target `Afrique francophone` broadly (Côte d'Ivoire, Sénégal, Cameroun, RDC, Guinée, Mali, Burkina, Gabon, Bénin, Togo…) with `FCFA` currency and OHADA/SYSCOHADA frameworks where relevant, not France-centric or Québécois vocabulary; `language-standards` holds the full geographic policy.
- Website and long-form French live in the website engine's sister skill (`content-copy/french-native-copy`).
- Source material distilled from: Annie Heminway, *Practice Makes Perfect — Complete French Grammar*; Boulares & Frérot, *Grammaire progressive du français — Niveau avancé*; *Learn French II — Parallel Text*; and the *French–English Bilingual Visual Dictionary* (DK).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Publish-ready French copy per platform and post type | Client reviewer; community manager | Register, agreement, typography and market conventions pass the checks below; no invented facts. |
| Native-review note (identity and register record) | Approver | Names the market, `vous`/`tu` choice, reviewer and review date, or states `not-assessed`. |
| Adaptation note | Client reviewer | Lists placeholders, adapted idioms and any claim still awaiting a source or authority. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Back-translation check | French line beside its English back-translation | Meaning matches the approved source without distortion. |
| Native-review record | YAML record from the identity and register review | Missing reviewer or date is recorded as `NOT_ASSESSED`, never as a pass. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Drafting French copy within the supplied brief is permitted; certifying native quality is not.

## Degraded Mode

Without a fluent French reviewer or a confirmed market, return the narrowest qualified result and mark the affected checks `not assessed`. A francophone-Africa `vous` draft with placeholders and a back-translation can still be delivered, marked awaiting review.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Market not named, or named as francophone Africa | Use `vous`, FCFA, BCEAO/BEAC and OHADA references; no France-specific institutions. | Paris-centric copy that African readers reject. |
| Requester names France, Canada or another market | Replace the default market guidance with that market's conventions and record the change. | Imposing African defaults on a different audience. |
| Youth or lifestyle brand and the client approves `tu` | Use `tu` and make every verb, pronoun and possessive agree with it throughout the post and replies. | Mixed register that reads as careless translation. |
| English source relies on an idiom or pun | Rebuild the idea in native French rather than calque it. | Literal or culturally misplaced copy presented as native-quality language. |
| A price, result or approval is missing | Stop that claim; request it or leave a visible placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Copy names a person, organisation or community | Keep the minimum identity record; add legal name or pronunciation only when purpose and consent require it. | Collecting identity data without need. |

## Quality Standards

- A French native reader finds nothing that signals translation: no calques, no anglicisms, no English word order or punctuation spacing.
- Register is consistent across the post and its replies; every verb, pronoun and possessive agrees with the chosen `tu`/`vous`.
- Every adjective agrees in gender and number; partitives are correct and collapse to `de` after negation or quantity.
- Typography follows French rules; prices read `12 500 FCFA` or `1 250,00 €`, not `€1,250.00`.
- Hashtags and discovery phrases are what a French speaker actually searches, not transposed English.
- The copy passes the back-translation test: French to English reproduces the intended meaning without distortion.
- Names, figures, quotations and platform rules are verified before use; notes to the client are in British English.
- The `anti-ai-slop` ship gate is run; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns

- Translating the English caption word for word. Fix: adapt the hook, connectors and CTA with the idiom reference.
- Switching between `tu` and `vous` inside a post or its replies. Fix: record the register choice first and check every verb and possessive against it.
- Formatting prices the English way (`€1,250.00`). Fix: use French spacing and decimal commas (`12 500 FCFA`, `1 250,00 €`).
- Referencing Paris institutions for an Abidjan or Kinshasa audience. Fix: use FCFA, BCEAO/BEAC, OHADA and local mobile money names.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. Fix: verify it, or qualify or remove it.
- Treating missing native-language review as approval. Fix: mark the check `not assessed` and deliver the copy as awaiting review.
- Publishing, sending or changing a live account from drafting authority alone. Fix: obtain explicit action-specific authority and keep the approval record.

## References

- [Register and address](references/register-and-address.md): read when fixing `tu`/`vous`, softening requests or setting a formal-but-warm tone.
- [Idiom and hooks](references/idiom-and-hooks.md): read when the French is correct but flat, or when drafting hooks, CTAs and hashtags.
- [Grammar pitfalls](references/grammar-pitfalls.md): read when proofreading articles, agreement, negation, pronouns or verb constructions.
- [Anglicisms to avoid](references/anglicisms-to-avoid.md): read when French feels off without an obvious grammar error.
- [Typography and formatting](references/typography-and-formatting.md): read when finalising spacing, punctuation, prices and dates.
- [Vocabulary by theme](references/vocabulary-by-theme.md): read when a sector term and its gender are needed.
- [Identity and register review](references/identity-and-register-review.md): read when the copy names a person, organisation or community, or when recording native review.
- [`language-standards`](../language-standards/SKILL.md): read when the cross-language tone policy or the full geographic policy is in question.
- [`east-african-english`](../east-african-english/SKILL.md): read when the copy should stay in English for East African readers.
- [`swahili-native-copy`](../swahili-native-copy/SKILL.md): read when the target language is Kiswahili.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read before release.
- [Repository agent guide](../../../AGENTS.md): read when the engine-wide market, safety and anti-slop gates apply.
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

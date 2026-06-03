---
name: french-native-copy
description: Native-quality French copywriting standard for the social-media engine. Produces French captions, hooks, hashtags, ad copy, bios, and short-form posts that read as if written by an educated native speaker for a Francophone African audience — correct register (tu/vous), idiomatic phrasing, French typography, and zero machine-translation artefacts. Use whenever French social copy is written, adapted, or reviewed; never raw-translate English source copy.
---

# French Native Copy (Social)
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

This is the French execution layer for the social engine. It owns *how French reads*; `language-standards` owns the cross-language tone policy. For website/long-form French, the sister skill lives in the website engine (`content-copy/french-native-copy`).

<!-- dual-compat:start -->
## Use when
- Writing any French caption, hook, hashtag set, ad, bio, profile, story, carousel, or short-form post the engine produces.
- Adapting approved English social copy into French where the French must stand on its own as native copy, not a translation.
- Reviewing French social copy (human, translated, or AI-generated) for register, idiom, grammar, and typography before it ships.

## Do not use when
- The copy is English or Kiswahili. For Kiswahili use `swahili-native-copy`; for English use `east-african-english`.
- The task is the cross-language tone policy or three-language consistency — that belongs to `language-standards`.
- The task is graphic design, video production, or platform scheduling rather than the words themselves.

## Workflow
1. Fix register and audience first: `vous` (default for brands/commerce/services) or `tu` (youth, lifestyle, peer brands). Hold it across the whole post and the comment voice. See `references/register-and-address.md`.
2. Write the French from the meaning, not the English words — frame the idea as a French speaker would, then check it carries every fact and the CTA. See `references/anglicisms-to-avoid.md`.
3. Apply the grammar machine translation gets wrong: partitives, gender/agreement, negation, pronouns, verb-preposition collocations. See `references/grammar-pitfalls.md`.
4. Raise it to native and punchy for short-form: idiomatic hooks, French CTA verbs (infinitive), rhythm that survives truncation. See `references/idiom-and-hooks.md`.
5. Apply French typography even in captions: narrow non-breaking space before `; : ! ?`, guillemets `« »`, decimal comma, `€`/`FCFA` after the number, lowercase days/months. See `references/typography-and-formatting.md`.
6. Localise hashtags and SEO/discovery terms in French — research them natively, don't transpose. See `references/idiom-and-hooks.md`.

## Anti-Patterns
- Running English captions through translation and lightly editing the output — write from meaning.
- Mixing `tu` and `vous`, or switching gender of address mid-thread.
- Calques such as `Nous offrons des solutions`, `Cliquez le lien dans la bio` (prefer `Lien en bio` / `Le lien est dans la bio`), `pour plus d'informations`.
- English punctuation spacing (`Génial!` with no space, straight quotes, `€50`), and English-style Title Case on French words.
- Hype adjectives banned by `glossary` in their French equivalents; emoji or hashtag spam in place of a real hook.

## Outputs
- Native-quality French social copy for the requested artefact (caption, hook, hashtags, ad, bio, thread), plus a one-line register-and-audience note so downstream posts stay consistent.
- Review findings with concrete corrections when the task is a review.

## References
- `references/register-and-address.md` — tu vs vous for social, brand voice, comment-reply register, conditional softening.
- `references/grammar-pitfalls.md` — partitives, gender/agreement, negation, pronouns, relative pronouns, verb-preposition collocations, subjunctive triggers, country prepositions.
- `references/vocabulary-by-theme.md` — native business, tech, hospitality, retail, food vocabulary with gender, and calque traps.
- `references/idiom-and-hooks.md` — connectors, native craft tells, hook patterns, CTA verbs, hashtag and discovery conventions.
- `references/anglicisms-to-avoid.md` — calques and false friends with native French alternatives.
- `references/typography-and-formatting.md` — spacing, guillemets, numbers, currency (€/FCFA), dates, capitalisation for captions.
<!-- dual-compat:end -->

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

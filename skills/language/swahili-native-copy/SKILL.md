---
name: swahili-native-copy
description: Native-quality Kiswahili copywriting standard for the social-media engine. Produces Swahili captions, hooks, hashtags, ad copy, bios, and short-form posts that read as if written by an educated East African native speaker — correct noun-class concord, idiomatic phrasing, respectful Kiswahili sanifu register, and zero machine-translation artefacts. Use whenever Kiswahili social copy is written, adapted, or reviewed; never raw-translate English source copy.
---

# Swahili Native Copy (Social)
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

This is the Kiswahili execution layer for the social engine. It owns *how Kiswahili reads*; `language-standards` owns the cross-language tone policy. For website/long-form Kiswahili, the sister skill lives in the website engine (`content-copy/swahili-native-copy`).

<!-- dual-compat:start -->
## Use when
- Writing any Kiswahili caption, hook, hashtag set, ad, bio, profile, story, carousel, or short-form post the engine produces.
- Adapting approved English social copy into Kiswahili where the Swahili must stand on its own as native copy, not a translation.
- Reviewing Kiswahili social copy (human, translated, or AI-generated) for concord, register, idiom, and spelling before it ships.

## Do not use when
- The copy is English or French. For French use `french-native-copy`; for English use `east-african-english`.
- The task is the cross-language tone policy or three-language consistency — that belongs to `language-standards`.
- The task is graphic design, video production, or platform scheduling rather than the words themselves.

## Workflow
1. Write in `Kiswahili sanifu` (standard, respectful, formal-but-warm). Reserve `Sheng` for Kenyan youth/lifestyle/telecom briefs only. Calibrate by market (Tanzania = richer Swahili; Kenya = bilingual-friendly). See `references/register-and-greetings.md`.
2. Write from meaning, not English words — frame the idea as an East African speaker would, then check it carries every fact and the CTA. See `references/loanwords-and-anglicisms.md`.
3. Get noun-class concord right as you write — adjective, possessive, demonstrative, number, and verb agreement must match the noun's class (`ngeli`). This is the single biggest failure of machine translation. See `references/noun-classes-and-concord.md`.
4. Build verbs and choose mood correctly: subjunctive (`-e`) with `tafadhali` for soft CTAs, imperative for direct ones, correct negatives. See `references/verb-system-and-politeness.md`.
5. Raise it to native and punchy for short-form: warm greetings, respectful address, a well-placed `methali` (proverb) or kanga-style one-liner, natural collocations. See `references/idiom-and-hooks.md`.
6. Localise numbers, prices, the Swahili clock (the 6-hour offset!), hashtags, and discovery terms natively. See `references/numbers-time-and-hooks.md`.

## Anti-Patterns
- Translating English word-for-word and producing broken concord (`kubwa nyumba` for `nyumba kubwa`; `letu duka` for `duka letu`).
- Default-class agreement: forcing human (M-/WA-) concord onto non-human nouns; wrong pronoun for products (`wao` instead of `zi-`).
- Tourist/Hollywood Swahili to locals (`Jambo`, `Hakuna matata` as your headline flavour, `Simba`, `Rafiki`); barked colonial-pidgin commands (bare uninflected verbs); slur/hierarchy words (`shenzi`).
- Calques such as `Karibu kwa tovuti`, `Wasiliana sisi` (→ `Wasiliana nasi`), bare `email`/`online`/`link in bio` left untranslated.
- Mishandling the Swahili clock so opening hours are six hours off; misquoted proverbs; reduplication assumed to mean "very".

## Outputs
- Native-quality Kiswahili social copy for the requested artefact (caption, hook, hashtags, ad, bio, thread), plus a one-line market-and-voice note (Tanzania/Kenya/regional) so downstream posts stay consistent.
- Review findings with concrete corrections when the task is a review.

## References
- `references/noun-classes-and-concord.md` — the `ngeli` system and agreement across adjectives, possessives, demonstratives, numbers, and verbs.
- `references/verb-system-and-politeness.md` — verb structure, tenses, negatives, imperative and subjunctive, `tafadhali`, polite requests.
- `references/register-and-greetings.md` — `Kiswahili sanifu`, greetings by register, honorifics, plural-of-respect, variety/prestige and Sheng lines.
- `references/idiom-and-hooks.md` — collocations, trust language, value words, `methali`, kanga-style one-liners, hook patterns, hashtags, and cautions.
- `references/loanwords-and-anglicisms.md` — Arabic loans, English handling (native vs bare), calques to avoid, Tanzania vs Kenya usage.
- `references/numbers-time-and-hooks.md` — numbers with concord, the Swahili clock, dates, currency, and how to write them in short-form.
<!-- dual-compat:end -->

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

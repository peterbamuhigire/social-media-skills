---
name: east-african-english
description: Use when English social posts, ads, captions or campaign copy for Uganda, Kenya, Tanzania or Rwanda must read warm, courteous and globally clear in British spelling; produces the edited copy with a tone note per country; not for the tone policy spanning English, French and Kiswahili (use `language-standards`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# East African English — Language & Tone Skill

English content targets East Africa primarily (Uganda, Kenya, Tanzania, Rwanda) but must be **globally readable**: a business professional in London, Lagos, Nairobi, or Kigali must understand every sentence without confusion. The reader is an educated professional with advanced English comprehension, often reading English as L2 or L3; use East African warmth and courtesy but avoid local slang or references only one country's readers would understand.

<!-- dual-compat-start -->
## Use When
- Our English posts or ads sound too American, cold, stiff or salesy and should read friendly and polite, like a courteous East African business, in British spelling.
- One campaign runs for Ugandan, Kenyan and Tanzanian customers and the wording must suit each country without slang that only one market follows.
- Captions, calls to action, WhatsApp broadcasts or landing microcopy need checking for dates, spelling and phrases a reader in Nairobi or Kigali would find odd.
- A reviewer wants the English tightened: precise verbs, natural collocations, balanced sentences and no hype.

## Do Not Use When
- `language-standards` for the tone and grammar rulebook that governs English, French and Kiswahili together.
- `swahili-native-copy` when the copy must be written in Kiswahili.
- `caption-writer` when new captions must be drafted from a brief rather than existing English fixed.
- Stop before publishing or sending the edited copy; return it with the tone note for client approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| The draft or brief being written | Requester or approved brief | Yes | Stop; this skill edits existing English and routes new captions to `caption-writer`. |
| Target country (Uganda, Kenya, Tanzania, Rwanda) | Client or brief | Recommended | Apply neutral East African business English, a balanced blend of the three country tones. |
| Channel and copy type (caption, CTA, WhatsApp broadcast, landing microcopy, email) | Brief | Yes | Edit as a social caption and flag channel-specific limits `not assessed`. |
| Brand voice, offer facts, protected terms and approvals | Client source pack or authorised owner | Conditional | Keep the client's facts unchanged; never invent names, prices, dates or results. |

## Workflow

1. Confirm the draft, target country, channel and approval owner; route to `language-standards` for a multilingual policy question, `swahili-native-copy` for Kiswahili, and stop if there is no draft or brief.
2. Apply British spelling and day-month-year dates from the [style guide](references/east-african-english-style-guide.md) (17 February 2026, never February 17, 2026).
3. Set the tone by country: Uganda warm and relational, Kenya confident and business-oriented, Tanzania calm and measured; neutral East African style when no country is named.
4. Soften directives and CTAs to the courteous East African form, and replace hype words with measured professional vocabulary.
5. Check collocations and lexical precision with the [English collocation overlay](../language-standards/references/english-collocations-and-lexical-precision-2026-09-02.md): preserve genuine local detail and warmth, but never manufacture dialect, slang, intimacy or mistakes, and check each phrase in its channel and audience context.
6. Read the result against the benchmark paragraph and the quality checks; correct any sentence a reader in London, Lagos, Nairobi or Kigali would stumble on and rerun the read-through.
7. Run the `anti-ai-slop` ship gate and return the edited copy with a tone note per country; stop before publishing or sending.

## Core characteristics

1. **Clear and direct.** Sentences are straightforward, grammatically careful and logically structured. No slang in professional communication.
2. **Formal and respectful.** Politeness is essential. Communication shows courtesy and humility.
3. **British English spelling.** organisation, programme, centre, colour, travelling (double "l").
4. **Professionally indirect.** Avoid bluntness. Soften directives with courteous phrasing.
5. **Measured confidence.** Confident without arrogance. No dramatic or exaggerated language.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Edited English copy | Client reviewer; community manager | British spelling, day-month-year dates, courteous CTAs and no hype words or slang. |
| Tone note per country | Client reviewer | States the country tone applied (or neutral East African style) and the main edits made. |
| Open-items note | Approver | Lists facts, dates or claims the editor could not verify and any action needing authority. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Before-and-after edit log | Table: original phrase, edited phrase, rule applied | Every hype word, American spelling, blunt directive and date format change is traceable to a rule. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Editing English copy within the supplied brief is permitted; sending it is not.

## Degraded Mode

Without a confirmed target country or brand voice, return the narrowest qualified result and mark the affected checks `not assessed`. Copy edited to neutral East African business English, with spelling, dates and CTAs corrected, can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Client is based in Uganda | Very polite and appreciative; frequent "kindly"; emphasis on harmony and goodwill. | Copy that reads cold to a Ugandan customer. |
| Client is based in Kenya | Efficient and practical; clear timelines and expectations; professional firmness. | Vague copy that Kenyan business readers find evasive. |
| Client is based in Tanzania | Formal and slightly conservative; respectful, patient rhythm influenced by Swahili sentence structure. | Abrupt copy that reads as disrespectful. |
| No country is indicated, or one campaign covers several | Use the neutral East African style, a balanced blend of all three; drop slang only one market follows. | Wording that suits one country and confuses the others. |
| A directive or CTA sounds blunt ("Send the report today", "Buy Now") | Rewrite in the courteous form ("Kindly submit the report by close of business today", "Place Your Order"). | Pushy tone that damages the relationship. |
| A required fact or approval is missing | Stop that claim; request it or leave an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |

## Quality Standards

- British English spelling is consistent throughout the deliverable; dates are day-month-year.
- Tone stays professional, respectful and recognisably East African rather than American, slang-heavy or globally generic.
- CTAs, directives and service language remain courteous without becoming weak or vague.
- Every sentence is understandable to a business professional in London, Lagos, Nairobi or Kigali.
- No exaggerated marketing words, American abbreviations (FYI, ASAP, BTW), excessive exclamation marks or telegram-style fragments.
- Collocations are natural and precise; no manufactured dialect, slang, intimacy or mistakes.
- Names, figures, quotations and platform rules are verified before use, and the `anti-ai-slop` ship gate is passed; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns

- Using month-first American dates (February 17, 2026). Fix: write 17 February 2026.
- Leaving hype words such as groundbreaking, game-changing or skyrocket. Fix: swap them for the measured word in the style guide's avoid list.
- Writing "Buy Now" or "Sign Up" CTAs. Fix: use inviting forms such as "Place Your Order" or "Register Today".
- Adding local slang to sound authentic. Fix: keep genuine local detail and warmth only; never manufacture dialect.
- Writing fragments or telegram-style copy. Fix: use full, balanced sentences with clear subject-verb-object order.
- Adding a price, result, quotation or cultural claim without a traceable source. Fix: verify it, or qualify or remove it.
- Publishing or sending the edited copy from editing authority alone. Fix: return it with the tone note for client approval.

## References

- [East African English style guide](references/east-african-english-style-guide.md): read when checking spelling, dates, country tone examples, courteous phrases, the vocabulary avoid list, sentence style, CTAs, letter openings and closings, or the benchmark paragraph.
- [English collocation and lexical-precision overlay](../language-standards/references/english-collocations-and-lexical-precision-2026-09-02.md): read when tightening verbs, collocations and word choice.
- [`language-standards`](../language-standards/SKILL.md): read when the tone and grammar policy spans English, French and Kiswahili.
- [`swahili-native-copy`](../swahili-native-copy/SKILL.md): read when the copy must be written in Kiswahili.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read before release.
- [Repository agent guide](../../../AGENTS.md): read when the engine-wide market, safety and anti-slop gates apply.
<!-- dual-compat-end -->

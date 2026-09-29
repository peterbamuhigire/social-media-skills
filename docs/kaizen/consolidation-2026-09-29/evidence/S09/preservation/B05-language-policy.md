# S09 preservation log — B05-language-policy

Worker: Claude (S09 worker agent), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. Before gated ratios are from the S09 baseline measurement (`m0.json`).

## east-african-english — 275 → 115 lines (gated shared ratio 13.9 % → 0.0 %)

Only this copy was rewritten; mirrored copies in other engines are untouched.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Target Audience (Standard)" (intro paragraph) | CONDENSED-IN-PLACE | SKILL.md intro (every fact kept: four countries, globally readable, L2/L3 reader, London/Lagos/Nairobi/Kigali test, no one-country slang) |
| 2 | Generated contract prose (generic Required Inputs rows, Capability, Degraded, 3 generic decision rows, 6-step generic workflow, generic Outputs/Evidence, 4 generic quality bullets, 5 generic anti-patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections; the verification and anti-slop gate facts kept in Quality Standards and Anti-Patterns |
| 3 | Line "All website copy, headings, calls to action…foundational language standard" | MOVED | references/east-african-english-style-guide.md (intro paragraph) |
| 4 | "## Required Input" | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs (draft or brief; target country; neutral East African default) |
| 5 | "## Core Characteristics" (5 items) | KEPT (and MOVED copy) | SKILL.md § Core characteristics; also references/east-african-english-style-guide.md § Core Characteristics |
| 6 | "## British English Standards" (spelling table, dates) | MOVED | references/east-african-english-style-guide.md § British English Standards; date rule also in SKILL.md Workflow step 2 and Anti-Patterns |
| 7 | "## Tone by Country Context" (Uganda, Kenya, Tanzania, neutral, with examples) | MOVED + MERGED-INTO-CONTRACT | references/east-african-english-style-guide.md § Tone by Country Context; markers in SKILL.md § Decision Rules rows 1–4 |
| 8 | "## Courteous Phrases to Use" | MOVED | references/east-african-english-style-guide.md § Courteous Phrases to Use |
| 9 | "## Vocabulary Standards" (preferred words, avoid table, also-avoid list) | MOVED | references/east-african-english-style-guide.md § Vocabulary Standards; summary in SKILL.md Quality Standards and Anti-Patterns |
| 10 | "## Sentence Style" (balanced sentences, indirectness table, CTA table) | MOVED | references/east-african-english-style-guide.md § Sentence Style; examples in SKILL.md Decision Rules row 5 |
| 11 | "## Openings and Closings" | MOVED | references/east-african-english-style-guide.md § Openings and Closings |
| 12 | "## Reference Paragraph — Neutral East African Business Style" | MOVED | references/east-african-english-style-guide.md § Reference Paragraph |
| 13 | Lower "## Quality Standards" (3 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards bullets 1–3 |
| 14 | "## When This Skill Applies" (5 bullets + design-system sentence) | MOVED | references/east-african-english-style-guide.md § When This Skill Applies |
| 15 | "## English collocation and lexical-precision overlay" | MERGED-INTO-CONTRACT | SKILL.md Workflow step 5, Quality Standards, References |

Checks: factcheck 0 missing; linecheck 8 flagged → 7 scaffolding, 1 paraphrased, 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: "[language-standards] is the nearest routing comparison" → SKILL.md § References (`language-standards` link with read-when).
Noticed, not changed: the moved style guide scopes itself to "All website copy" and "All visible website text" although this is the social engine; the CTA table recommends "Begin Your Journey", a phrase the anti-slop gate may flag.

## french-native-copy — 108 → 125 lines (gated shared ratio 48.1 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Target Markets (Standard)" | CONDENSED-IN-PLACE | SKILL.md intro, Workflow step 2 and § Market standard and sources (full country list kept) |
| 2 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, generic workflow, Outputs, Evidence, 4 generic quality bullets, 5 generic anti-patterns) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections; source-traceability, native-review and authority anti-patterns kept as domain bullets |
| 3 | "## References" (3 links) | MERGED-INTO-CONTRACT | SKILL.md § References (all 7 references now listed) |
| 4 | Acknowledgement line | KEPT | SKILL.md after the dual-compat block |
| 5 | Paragraph "French execution layer…sister skill…" | CONDENSED-IN-PLACE | SKILL.md intro and § Market standard and sources |
| 6 | "## Required Input" (3 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs rows 1–4 |
| 7 | "## Quality standards" (6 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards bullets 1–6 (verbatim) |
| 8 | "## Notes" (francophone default; source books) | KEPT | SKILL.md § Market standard and sources |

Checks: factcheck 0 missing; linecheck 6 flagged → 4 scaffolding, 2 paraphrased, 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: "The reader is an educated professional…not France-specific institutions" → SKILL.md intro and Workflow step 2; "[east-african-english] is the nearest routing comparison" → SKILL.md § References.
Noticed, not changed: the Target Markets standard says French targets francophone Africa "not France", while the old Required Input offers France, Canada or mixed markets and a `tu` register; both kept (default Africa, other markets only when the requester names them).

## language-standards — 500 → 125 lines (gated shared ratio 6.9 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, generic workflow, Outputs, Evidence, 4 generic quality bullets, 5 generic anti-patterns) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## References" (3 links) | MERGED-INTO-CONTRACT | SKILL.md § References (all 8 references listed) |
| 3 | Intro line "All website copy…Cross-cutting standard" | MOVED | references/target-audiences-and-scope.md; condensed in SKILL.md intro |
| 4 | "## Target Audiences (Standard)" (table + 5 rules) | MOVED + CONDENSED-IN-PLACE | references/target-audiences-and-scope.md § Target Audiences; SKILL.md § Default audiences by language and Decision Rules rows 1–4 |
| 5 | "## Required Input" | MOVED + MERGED-INTO-CONTRACT | references/target-audiences-and-scope.md § Required Input; SKILL.md § Required Inputs rows 1–2 |
| 6 | "## Core Principles (All Languages)" | MOVED + CONDENSED-IN-PLACE | references/target-audiences-and-scope.md; SKILL.md § Default audiences (principles sentence) |
| 7 | "# ENGLISH (en)" (core characteristics, spelling, dates/numbers, country tone, courteous phrases, vocabulary, CTAs) | MOVED | references/english-en-standard.md |
| 8 | "### AI Language Avoidance (All Languages)" and "## Redundant Phrases (All Languages)" | MOVED | references/ai-language-and-redundancy.md; tier rule summarised in SKILL.md Quality Standards |
| 9 | "# FRENCH (fr)" (all subsections incl. Astro JSX apostrophes, text expansion, geographic scope) | MOVED | references/french-fr-standard.md; decision-time rules in SKILL.md Decision Rules rows 2, 5, 6 and Workflow step 5 |
| 10 | "# KISWAHILI (sw)" (all subsections) | MOVED | references/kiswahili-sw-standard.md; decision-time rules in SKILL.md Decision Rules rows 3, 5 |
| 11 | "# When This Skill Applies" and "## Integration with Other Skills" | MOVED + MERGED-INTO-CONTRACT | references/target-audiences-and-scope.md; SKILL.md Workflow step 1, Decision Rules row 4, References |
| 12 | Lower "## Quality Standards" (6-item pre-publish checklist) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards bullets 1–6 |

Checks: factcheck 0 missing; linecheck 9 flagged → 7 scaffolding, 2 paraphrased, 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: "[Human English and reader-centred craft] governs the English reader…" → SKILL.md § References (Human English craft standard); "Before publishing any page, verify:" → SKILL.md § Quality Standards.
Noticed, not changed: Kiswahili date format is given as "Februari 17, 2026 (or 17 Februari 2026)", month-first, against the day-month-year rule elsewhere; French date line repeats "17 février 2026 (or 17 février 2026)"; the Tier 2 list repeats six Tier 1 words (seamless, holistic, curate, resonate, underscore, showcase); Kiswahili glosses such as "Kusaada", "Kupatiana", "Tukikubali" and "maChinwali" look doubtful and should go to a native reviewer; "Progressive tense preference" heads a rule that actually prefers simple tenses; the English and Kiswahili reviewer rules differ on whether Uganda counts as a target market for Kiswahili review.

## swahili-native-copy — 108 → 125 lines (gated shared ratio 48.1 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Target Markets (Standard)" | CONDENSED-IN-PLACE | SKILL.md intro, Required Inputs rows 2–3 and § Market standard and sources |
| 2 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, generic workflow, Outputs, Evidence, 4 generic quality bullets, 5 generic anti-patterns) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | "## References" (3 links) | MERGED-INTO-CONTRACT | SKILL.md § References (all 7 references now listed) |
| 4 | Acknowledgement line | KEPT | SKILL.md after the dual-compat block |
| 5 | Paragraph "Kiswahili execution layer…sister skill…" | CONDENSED-IN-PLACE | SKILL.md intro and § Market standard and sources |
| 6 | "## Required Input" (3 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs rows 1–4 |
| 7 | "## Quality standards" (6 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards bullets 1–6 |
| 8 | "## Notes" (relationship before transaction; source books) | KEPT | SKILL.md Workflow steps 2–3 and § Market standard and sources |

Checks: factcheck 0 missing; linecheck 5 flagged → 4 scaffolding, 1 paraphrased, 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: "[east-african-english] is the nearest routing comparison" → SKILL.md § References.
Noticed, not changed: none.

## policy-ai-content-ethics — 476 → 136 lines (gated shared ratio 5.2 % → 1.4 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (Capability, Degraded, generic workflow, Outputs, Evidence, generic Quality paragraph, 6 generic anti-patterns) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections; "verify volatile legal details" anti-pattern kept |
| 2 | Contract "## Required Inputs" (3 rows) | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs rows 1, 4, 5 (fallbacks kept) |
| 3 | Contract "## Decision Rules" (5 rows) | KEPT / MERGED | SKILL.md § Decision Rules rows 1–2 verbatim; rows "law, contract or platform terms" and "exception could expose people" merged into row 8; "internal operating choice → name owner" into Workflow step 3 |
| 4 | Contract "## References" (6 links) | KEPT | SKILL.md § References |
| 5 | Lower "## Required Inputs" (8 intake questions, regulatory list) | MOVED + MERGED-INTO-CONTRACT | references/policy-intake-and-template.md § Required Inputs (intake questions); SKILL.md § Required Inputs rows 1–6 |
| 6 | "## Section 1 — Why an AI Ethics Policy Matters" (3 paragraphs) | MOVED | references/policy-intake-and-template.md § Section 1; SKILL.md Workflow step 2 |
| 7 | "### The Five Ethical Principles" (table) | KEPT (and MOVED copy) | SKILL.md § The five ethical principles; references/policy-intake-and-template.md |
| 8 | "## Section 2 — AI Content Ethics Policy Template" (clauses 1–9, signature) | MOVED | references/policy-intake-and-template.md § Section 2 (influencer-disclosure path given one extra `../`) |
| 9 | "## Section 2A — AI Attribution and Disclosure Standard" | MOVED | references/policy-clauses-and-checklists.md; SKILL.md Decision Rules row 3 |
| 10 | "## Section 2B — Intellectual Property and Copyright" | MOVED | references/policy-clauses-and-checklists.md |
| 11 | "## Section 2C — SynthID and AI Content Watermarking" | MOVED | references/policy-clauses-and-checklists.md; SKILL.md Evidence (watermark log) |
| 12 | "## Section 2D — Training Data Bias Risk Register" | MOVED | references/policy-clauses-and-checklists.md; SKILL.md Decision Rules row 1 |
| 13 | "## Section 2E — EU AI Act Cross-Border Compliance Note" (Article 4, Article 28b(4), Regulation (EU) 2024/1689 Article 50 note) | MOVED (verbatim) | references/policy-clauses-and-checklists.md; SKILL.md Decision Rules row 5 |
| 14 | "## Section 2A — Additional Ethical Requirements" (Ltifi 2024, GDPR Art. 22, UDPPA s.25, Johnsen 2024 Ch.28, Tanzania PDPA 2022 with `TZ-PDPA` / PL-04, data minimisation) | MOVED (verbatim) | references/policy-clauses-and-checklists.md; SKILL.md Decision Rules row 7 |
| 15 | "## Section 3 — Consultant's Internal AI Ethics Checklist" | MOVED | references/policy-clauses-and-checklists.md; SKILL.md Outputs row 2 |
| 16 | "## Section 4 — Sector-Specific Guidance" (pointer) | MOVED | references/policy-clauses-and-checklists.md; SKILL.md Workflow step 4, Decision Rules row 6 |
| 17 | "## Section 5 — East Africa-Specific Considerations" | MOVED | references/policy-clauses-and-checklists.md; SKILL.md Anti-Patterns (vernacular, local facts, PII) |
| 18 | "## Quality Criteria" (10 bullets) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Quality Standards (8 kept, 2 merged); full list verbatim in references/policy-clauses-and-checklists.md § Quality Criteria |
| 19 | Lower "## References" (3 skills) and "Key citations" | MOVED + MERGED-INTO-CONTRACT | references/policy-clauses-and-checklists.md § Related skills and key citations; SKILL.md § References |

Checks: factcheck 0 missing; linecheck 4 flagged → 3 scaffolding, 1 paraphrased, 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: "| Rule is an internal operating choice | Draft the control and name its owner |" → SKILL.md Workflow step 3.
Noticed, not changed: two sections are both labelled "Section 2A" (attribution standard and additional ethical requirements); Ltifi is cited as both 2024 and 2025; the EU AI Act note keeps draft numbering (Article 4 labelling, Article 28b(4)) alongside the verification note that Article 50 holds the transparency duty in Regulation (EU) 2024/1689; the IAB register ID and the Uganda Computer Misuse (Amendment) Act 2022 (void, 17 March 2026) text named in the batch brief do not appear anywhere in this skill folder at `0e0af8a`, so there was nothing to keep; C2PA appears only in references/ai-ip-and-copyright-policy.md, which was not edited. Moved text in references/policy-clauses-and-checklists.md had blank lines added around `---` rules so a paragraph no longer renders as a setext heading.

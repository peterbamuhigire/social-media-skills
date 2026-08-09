---
name: language-standards
description: Use when Language Standards — Multi-Language Tone & Grammar is needed to produce a language quality specification for social-media or digital-marketing work; use `east-african-english` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Language Standards — Multi-Language Tone & Grammar

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **language quality specification** and the supplied brief falls within language standards — multi-language tone & grammar.

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
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified language quality specification; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Market, language variety and audience register are confirmed | Use the named regional standard and preserve meaning, terminology and voice. | Literal or culturally misplaced copy presented as native-quality language. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact language quality specification, consumer, market, channel and approval boundary; route to `east-african-english` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete language quality specification; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Language quality specification | Requester, client reviewer or delivery team | The language quality specification addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested language quality specification, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [east-african-english](../east-african-english/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

All website copy, headings, CTAs, descriptions, and microcopy must follow this style guide for their respective language. Cross-cutting standard — applied throughout every content-writing step.

## Target Audiences (Standard)

Every multilingual output from this engine targets these audiences. Do not deviate unless the project brief explicitly names different markets.

| Locale | Primary Markets | Secondary Markets | Reader Profile | Register |
|--------|----------------|-------------------|----------------|----------|
| **English** | East Africa (Uganda, Kenya, Tanzania, Rwanda) | All English-speaking Africa and global English speakers | Advanced comprehension; educated professionals reading fluently in English (often L2/L3) | British-influenced East African professional English; clear, direct, respectful; globally readable |
| **French** | DRC, Congo-Brazzaville, Burundi, Senegal, Mali, Côte d'Ivoire, Togo, Cameroon, Gabon, Madagascar | All francophone Africa (Bénin, Burkina Faso, Niger, Guinea, Djibouti, Comoros, Chad, Central African Republic) | Advanced comprehension; educated professionals reading fluently in French (often L2/L3) | Formal vous; francophone African professional French; never France-centric, never Québécois |
| **Kiswahili** | Kenya, Tanzania, DR Congo | Uganda (limited), Rwanda, Burundi, Mozambique (Kiswahili speakers) | Advanced comprehension; educated professionals reading standard Kiswahili | Respectful Kiswahili sanifu; no slang, no Sheng, no regional dialect drift |

### Rules
1. **English must be globally readable.** An English speaker in London, Lagos, or Nairobi must understand every sentence. Use East African warmth and courtesy but avoid local slang or references only Ugandans would understand.
2. **French targets francophone Africa, not France.** Reference OHADA, BCEAO/BEAC, FCFA, and institutions relevant across West and Central Africa. Never assume the reader is in Paris.
3. **Kiswahili targets Kenya and Tanzania first.** DR Congo is the secondary growth market. Uganda has limited Kiswahili readership — do not assume Ugandan readers for Swahili content.
4. **Advanced reader assumption.** Do not simplify vocabulary, over-explain concepts, or use patronising language. The audience reads at an advanced level in their chosen language.
5. **No raw translation.** Each language is authored from meaning. The French and Kiswahili outputs must read as if originally written in that language by a professional from the target market.

## Required Input
Start with the source text or deliverable brief, then confirm the target language and market. If the target language is unclear, stop and establish it before applying this skill.

## Core Principles (All Languages)
1. **Clear and direct.** Sentences are straightforward, grammatically careful, logically structured.
2. **Formal and respectful.** Politeness is essential. Communication shows courtesy and humility.
3. **No excessive marketing language.** Avoid drama, exaggeration, slang.
4. **Professionally indirect.** Soften directives with courteous phrasing.
5. **Measured confidence.** Confident without arrogance.
6. **Culturally authentic.** Respect regional norms, preferences, sensitivities.

# ENGLISH (en) — British English, East African Professional Standard

## Core Characteristics
1. **British English spelling** throughout.
2. **East African tone** — formal, respectful, professionally courteous (Uganda, Kenya, Tanzania blend).
3. **Measured and confident** without arrogance or dramatic language.
4. **Logical sentence structure** — no fragments or telegram-style copy.
5. **Progressive tense preference** — use simple present or past over continuous tenses. "The company plans to expand" not "The company is planning to expand." Simple tenses are more direct and authoritative.
6. **Consistent verb tense** — do not switch tenses within a section. If you begin in present, stay present throughout that block. Mixing past and present within the same thought signals uncertainty.

## British English Spelling
Always use British spelling:

| Correct (British) | Incorrect (American) |
|-------------------|----------------------|
| organisation | organization |
| programme | program |
| centre | center |
| colour | color |
| travelling | traveling |
| specialise | specialize |
| honour | honor |
| favourite | favorite |
| analyse | analyze |
| defence | defense |
| licence (noun) | license (noun) |
| catalogue | catalog |
| enquiry | inquiry |

## Dates and Numbers
- **Date format**: 17 February 2026 (or 17th February 2026)
- **Never**: February 17, 2026 (American format)
- **Numbers**: Use commas for thousands: 1,000; 100,000
- **Currency**: £ for GBP, $ for USD, €, or regional (specify in design-tokens.md)

## Tone by East African Country Context
Adjust tone slightly based on client location. Use Neutral East African when no country is specified.

| Country | Tone | Key marker |
|---------|------|------------|
| **Uganda** | Warm, relational, appreciative | Frequent "kindly", emphasis on harmony: "We highly appreciate your support. Kindly be informed…" |
| **Kenya** | Confident, business-oriented, efficient | Clear timelines, professional firmness: "Please share the signed agreement by Friday, 21 February 2026." |
| **Tanzania** | Calm, measured, conservative | Patient rhythm, influenced by Kiswahili patterns: "We kindly request your guidance. We shall revert shortly." |
| **Neutral (default)** | Balanced blend | Use when no country is specified |

## Courteous Phrases (English)
Natural and expected in East African business English:

- Kindly find attached…
- We kindly request…
- Please be advised that…
- We would like to inform you…
- Thank you for your continued support.
- We look forward to your response.
- We appreciate your partnership.
- Should you require any further clarification, please do not hesitate to contact us.
- Yours faithfully, / Yours sincerely,

## Vocabulary Standards (English)
### Preferred Professional Words
- facilitate, implement, undertake, liaise, coordinate
- engage, support, enhance, review, confirm
- advise, revert (widely accepted in East Africa, meaning "respond")
- significant, important, strategic, beneficial, valuable

### Words to Avoid
Never use exaggerated marketing language:

| Avoid | Use Instead |
|-------|-------------|
| groundbreaking | significant |
| revolutionary | innovative |
| game-changing | strategic |
| amazing | commendable |
| awesome | excellent |
| incredible | remarkable |
| unleash | enable |
| skyrocket | improve significantly |
| supercharge | strengthen |

Also avoid: American slang (FYI, ASAP, BTW), dramatic emotional tone, excessive exclamation marks.

Instead of abbreviations, write in full: "Please respond as soon as possible."

### AI Language Avoidance (All Languages)
AI-generated text has recognisable vocabulary and patterns. Every piece of content must pass as entirely human-written.

**Tier 1 — Banned words (instant AI tells):** delve, tapestry, landscape (as metaphor), multifaceted, testament, realm, harness, leverage, synergy, embark, navigate (as metaphor), foster, beacon, forge, unleash, pivotal, paramount, robust, vibrant, bolster, seamless, holistic, curate, resonate, underscore, showcase

**Tier 2 — Overused by AI (use sparingly, never in headlines):** compelling, captivating, cutting-edge, game-changer, revolutionary, transformative, innovative, streamline, empower, unparalleled, elevate, ignite, safeguard, enduring, seamless, holistic, curate, resonate, underscore, showcase

**Tier 3 — Flagged in combination (fine alone, AI-tell together):** crucial, facilitate, enhance, ensure, enable, encourage, essential, navigate, compelling, drive, embodies, emphasises. Rule: no more than one Tier 3 word per paragraph.

**Banned phrases:** "In today's fast-paced world", "It's important to note", "In the realm of", "Embark on a journey", "Game-changer", "Treasure trove", "Digital landscape", "Ever-evolving", "Not only X but also Y" (overused), "X isn't just Y; it's Z", "From X to Y, [subject] has..." (listicle pattern), "Whether you're [X] or [Y]..." (false inclusivity)

**Banned structural patterns:** Uniform sentence lengths (vary deliberately), "Furthermore/Moreover/Additionally" as paragraph openers, excessive em dashes (max 2 per article), three-item lists in every paragraph, present participial openers ("Leveraging our...", "Fostering an environment...")

**Required human markers:** Vary sentence length (mix 4-word and 30-word sentences), take clear positions ("I recommend" not "One might consider"), use the client's own vocabulary from their docs, include strategic contractions (2-4 per 500 words in English)

See `blog-writer/references/human-voice-standards.md` for the full blacklist with replacements, detailed techniques, and Voice DNA extraction process.

## Redundant Phrases (All Languages)
Delete constructions where one word does the full job: *close proximity* → proximity, *consensus of opinion* → consensus, *free gift* → gift, *end result* → result, *future plans* → plans, *past history* → history, *refer back* → refer, *revert back* → revert, *advance warning* → warning, *repeat again* → repeat, *exact same* → same. Full list in `blog-writer/references/editorial-standards.md`.

## English CTAs and Button Text
Apply respectful tone to buttons and UI text:

| Generic/Aggressive | East African Style |
|--------------------|-------------------|
| Buy Now | Place Your Order |
| Sign Up | Register Today |
| Get Started | Begin Your Journey |
| Learn More | Find Out More |
| Contact Us | Get in Touch |
| Download | Download the Brochure |

# FRENCH (fr) — Francophone African Professional Standard

## Core Characteristics
1. **Formal francophone African French** — not Québécois, not Belgian variants.
2. **Respectful and courteous** — professionalism with warmth.
3. **Standard French grammar and conventions**.
4. **Vous (formal)** throughout all professional communication — never "tu".
5. **Culturally appropriate** for Côte d'Ivoire, Cameroon, Senegal, DRC, Gabon.

## French Spelling and Grammar
Use standard French orthography:
- Accent marks required: é, è, ê, ë, à, ù, ç, œ, æ
- Double-check diacritical marks (many African translators omit them)
- UTF-8 encoding mandatory

### Apostrophes in Astro JSX Templates (French, Swahili, all languages)
**CRITICAL:** Single-quoted JS strings inside Astro JSX expressions (`.astro` template section) CANNOT contain straight apostrophes (`'`). This breaks the build because the apostrophe terminates the string early.

**Rules for any text containing apostrophes (e.g. French `d'`, `l'`, `n'`, `qu'`; Swahili `ng'`):**
1. **Use double-quoted strings** for any JS string literal that contains an apostrophe: `"d'excellence"` not `'d\'excellence'`
2. **Never use `\u2019` escape sequences** — Astro's template compiler may not handle them correctly
3. **Never use backslash-escaped apostrophes** (`\'`) in JSX template expressions — they work in frontmatter JS but fail in template JSX
4. **HTML text content is fine** — apostrophes in regular HTML `<p>d'excellence</p>` work without escaping
5. For JSX expression strings that need both `"` and `'`, use template literals: `` `string with ' and "` ``

### Verb Conjugation
- Use **vous** for all formal communication (not tu)
- Example: "Veuillez remplir le formulaire" (not "Remplis le formulaire")
- Imperative form: "Veuillez" + infinitive for politeness

### Gender Agreement
All adjectives and past participles must agree with gender:
- "La page est complétée" (feminine)
- "Le service est complété" (masculine)
- "Les pages sont complétées" (feminine plural)

## French Dates and Numbers
- **Date format**: 17 février 2026 (or 17 février 2026)
- **Month names**: Lowercase (février, not Février)
- **Numbers**: Use space or period for thousands: 1 000 or 1.000 (not 1,000)
- **Decimal separator**: Comma (not period): 3,14 (not 3.14)
- **Currency**: Franc CFA (FCFA), Euro (€), or specified in design-tokens.md

## Formal Registers and Politeness
### Standard Openings
- Madame, Monsieur,
- Chère Madame, Cher Monsieur,
- Greetings,

### Standard Closings
- Cordialement, (warm, professional)
- Respectueusement, (respectful)
- Avec mes meilleures salutations,
- Veuillez agréer l'expression de nos salutations distinguées.

### Courtesy Phrases (French)
- Nous vous prions de…
- Veuillez… (imperative form with "vous")
- Merci de votre attention.
- Nous apprécions votre partenariat.
- N'hésitez pas à nous contacter.
- Nous vous remercions de votre soutien continu.
- Nous attendons avec intérêt votre réponse.
- Si vous avez besoin de précisions supplémentaires, veuillez nous contacter.

## French Vocabulary Standards
### Preferred Professional Terms
- Faciliter, mettre en œuvre, entreprendre, coordonner
- Engager, soutenir, améliorer, examiner, confirmer
- Conseiller, informer, communiquer
- Significatif, important, stratégique, bénéfique, précieux

### Words to Avoid (Marketing Hype)
| Avoid | Use Instead |
|-------|-------------|
| révolutionnaire | innovant |
| "game-changing" | stratégique |
| incroyable | remarquable |
| génial | excellent |
| dingue | étonnant |
| Libérez le pouvoir | Activez la capacité |

### Francophone African Terminology
Use terms understood across francophone Africa (not Canada-specific, not France-specific):
- Budget (not "subvention")
- Entreprise (company, not "compagnie")
- Personnel (staff, not "employés" alone)
- Client (customer/client, standard everywhere)
- Formation (training, widely used)

## French CTAs and Button Text
| English | French (Formal) |
|---------|-----------------|
| Sign Up | S'inscrire |
| Register | Créer un compte |
| Contact Us | Nous contacter |
| Learn More | En savoir plus |
| Submit | Soumettre |
| Download | Télécharger |
| Place Your Order | Passer votre commande |
| Get Started | Commencer maintenant |

## French-Specific Considerations
### In-Country Reviewer Required
All French content must be reviewed by a native francophone speaker from the target market (Côte d'Ivoire, Cameroon, Senegal, DRC, Gabon). Send for review before publishing.

### Text Expansion
French is typically 20–40% longer than English. Design for 1.3x expansion:
- Buttons must accommodate longer labels
- Navigation items must wrap gracefully
- Form labels must not overlap fields

### Regional Variations
Avoid country-specific terms unless relevant:
- Use neutral francophone African vocabulary
- Avoid France-centric references
- Avoid Canadian (Québécois) terminology

### Francophone Africa Geographic Scope
**CRITICAL RULE:** French content must target Francophone Africa broadly — NOT just East Africa or Uganda.

The French language version of any website should be written and positioned for the entire Francophone African market:

**Target countries (examples, not exhaustive):**
Côte d'Ivoire, Cameroun, Sénégal, RDC (Congo-Kinshasa), Guinée, Mali, Burkina Faso, Gabon, Niger, Bénin, Togo, Madagascar, Mauritanie, Djibouti, Comores

**Financial institutions to reference (where relevant):**
- BCEAO (Banque Centrale des États de l'Afrique de l'Ouest) — West Africa
- BEAC (Banque des États de l'Afrique Centrale) — Central Africa
- Ecobank, BOA (Bank of Africa), UBA, Orabank, BGFI
- BNI (Côte d'Ivoire), Société Générale Afrique
- BOAD (IFD Ouest-africaine), AFC (Africa Finance Corporation)

**Business regulatory frameworks to use:**
- OHADA (Organisation pour l'Harmonisation en Afrique du Droit des Affaires)
- SYSCOHADA (accounting standards)
- FCFA currency (BCEAO/BEAC zone)

**What to AVOID in French content:**
- Ugandan-specific references: UDB, Centenary Bank, Stanbic Uganda, DFCU
- East Africa-only phrasing: "Afrique de l'Est" as the primary qualifier
- Assuming the French reader is in Uganda or East Africa

**What to DO:**
- Use "Afrique francophone" as the geographic qualifier
- Reference institutions and frameworks relevant across West and Central Africa
- Use examples from Côte d'Ivoire, Sénégal, Cameroun, DRC, Guinée
- SEO: target "plan d'affaires Côte d'Ivoire", "consultant Sénégal", "financement entreprise Cameroun", "business plan Afrique francophone"

**When a client is specifically in East Africa:**
If the client is Uganda-based, English pages handle the Ugandan/East African audience. The French pages reach the francophone African audience — these are different markets.

# KISWAHILI (sw) — East African Standard

## Core Characteristics
1. **Standard East African Kiswahili** — not regional dialects (Mombasa, Zanzibar variants).
2. **Formal/respectful register** throughout professional communication.
3. **Humble and relationship-focused** — Swahili culture emphasizes harmony.
4. **UTF-8 encoding** for proper character rendering.
5. **Simple sentence structure** — Kiswahili clarity values straightforward expression.

## Kiswahili Grammar and Structure
### Standard Kiswahili Conventions
- **Subject prefixes**: Proper noun classes (m-/ba, ki-/vi, n-, li-)
- **Verb conjugation**: Tense markers (-li-, -na-, -ta-, -ki-, -a)
- **Adjective agreement**: Must agree with noun class
- **No gender distinction** in pronouns (yeye = he/she)

### Formal Register (Habari Rasmi)
Use formal register in all professional communication:
- Avoid slang (sheng, Nairobi street language)
- Use full words (hakuna = do not have, not "hakuna matata")
- Respectful pronouns and address forms

### Tense Selection
- **Present habitual**: -na- (Anataka = He/she wants)
- **Near future**: -ta- (Atakuja = He/she will come)
- **Past completed**: -li- (Alifika = He/she arrived)
- **Conditional**: -ki-, -ngali (Akija = if he/she comes)

## Kiswahili Dates and Numbers
- **Date format**: Februari 17, 2026 (or 17 Februari 2026)
- **Month names**: English borrowed (Januari, Februari) — no Kiswahili equivalents universally understood
- **Day of week**: Jumapili (Sunday), Jumatatu (Monday), Jumanne (Tuesday), etc.
- **Numbers**: Use spaces for thousands: 1 000 (not 1,000)
- **Currency**: Shilingi (Sh, KES for Kenya), or specified in design-tokens.md

## Kiswahili Courtesy and Formality
### Standard Openings (Business)
- Habari yako?  (How are you? — formal)
- Tunataka kuwashukuru…  (We want to thank you…)
- Tunakuomba… (We kindly request…)

### Respectful Phrases (Kiswahili)
- **Tafadhali** (please — polite request)
- **Asante sana** (thank you very much)
- **Karibu sana** (welcome, you're welcome)
- **Pole pole** (take it easy, go slowly — suggests respect/patience)
- **Haba na haba hujaza kibaba** (little by little fills the measure — patience/humility)
- **Tunataka kuwajua** (We want to know / We would like to learn)
- **Tutakurejea** (We will respond to you)
- **Tukikubali** (If we may, with your permission)

### Closings
- **Kwa heshima** (with respect)
- **Wakati mwingine** (another time / we hope to hear from you)
- **Tunatumaini kuongea nayo upya** (We hope to speak with you again)

## Kiswahili Vocabulary Standards
### Preferred Professional Terms
- **Kusimamia** (to manage, oversee)
- **Kutekeleza** (to implement, execute)
- **Kushiriki** (to participate, engage)
- **Kusaada** (to help, support)
- **Kuboresha** (to improve, enhance)
- **Kupatiana** (to agree, coordinate)
- **Kuhakiki** (to verify, confirm)
- **Kuarifu** (to inform, notify)
- **Kujifunza** (to learn)
- **Muhimu** (important, significant)
- **Faida** (benefit, advantage)
- **Lengo** (goal, objective)

### Words to Avoid (Too Colloquial)
- Slang/sheng — use formal Kiswahili
- Hyperbolic marketing words
- English insertions without Kiswahili alternative available

## Kiswahili CTAs and Button Text
| English | Kiswahili (Formal) |
|---------|-------------------|
| Sign Up | Jisajili |
| Register | Andika Jina |
| Contact Us | Wasiliana Nasi |
| Learn More | Jua Zaidi |
| Submit | Tuma |
| Download | Pakua |
| Place Your Order | Agiza Bidhaa |
| Get Started | Anza Sasa |

## Kiswahili-Specific Considerations
### In-Country Reviewer Required
All Kiswahili content must be reviewed by a native Kiswahili speaker from East Africa (Kenya, Tanzania, or Uganda). Regional variants exist; ensure reviewer is from target market.

### Text Expansion
Kiswahili is typically 10–30% longer than English. Design for 1.2x expansion:
- Buttons must flex for longer labels
- Navigation items must wrap gracefully
- Form labels must have clear spacing

### No Dialects
- Use standard East African Kiswahili
- Avoid Mombasa Swahili (maChinwali features)
- Avoid Zanzibari Swahili (historical variants)
- Avoid regional slang or sheng (Nairobi street language)

### Relationships and Harmony
Kiswahili communication culture emphasizes relationships:
- Lead with greetings and acknowledgment
- Use plural forms to show respect (sisi = we, kuambia mtu = speak to a person)
- Avoid direct criticism or bluntness
- Always acknowledge the relationship before asking for action

# When This Skill Applies

**Cross-cutting** — applies to all visible website text, meta descriptions, alt text, form labels, error messages, email templates, and microcopy in all enabled languages.

**Extended reference:** `references/business-english-advanced.md` — phrase banks (meetings, presentations, apologies, formal correspondence), 80 ESL grammar rules, register-switching guidance, and anti-jargon rewrites.

## Integration with Other Skills
- **Native-copy execution skills (mandatory for French & Kiswahili)**: this skill owns the cross-language tone policy, but native-quality execution belongs to the dedicated skills. Route to **`french-native-copy`** for any French caption/ad/bio and **`swahili-native-copy`** for any Kiswahili one; use **`east-african-english`** for English. Do not produce French or Kiswahili copy by raw translation — the native-copy skills are required for those languages and carry the deeper grammar, idiom, register, and typography references.
- **i18n**: Determines which language versions are built
- **page-builder**: Applies language standards when creating content
- **seo**: Uses language standards for meta tags, titles, descriptions
- **sector-strategies**: Industry-specific tone within language standards

## Quality Standards
Before publishing any page, verify:

- [ ] **English pages**: British spelling, East African tone, no marketing hype
- [ ] **French pages**: Formal French, vous throughout, francophone African vocabulary, reviewed by francophone
- [ ] **Kiswahili pages**: Standard Kiswahili, formal register, no slang, reviewed by East African native speaker
- [ ] **All pages**: No truncation or text overflow in any language
- [ ] **All pages**: Grammatically correct, properly punctuated, culturally appropriate
- [ ] **All pages**: CTAs use respectful, inviting language (not aggressive)

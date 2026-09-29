# French (fr) standard

Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`); text unchanged. Read when writing or reviewing French: spelling and grammar, Astro JSX apostrophes, dates and numbers, registers, vocabulary, CTAs, text expansion and francophone Africa scope.

## FRENCH (fr) — Francophone African Professional Standard

### Core Characteristics
1. **Formal francophone African French** — not Québécois, not Belgian variants.
2. **Respectful and courteous** — professionalism with warmth.
3. **Standard French grammar and conventions**.
4. **Vous (formal)** throughout all professional communication — never "tu".
5. **Culturally appropriate** for Côte d'Ivoire, Cameroon, Senegal, DRC, Gabon.

### French Spelling and Grammar
Use standard French orthography:
- Accent marks required: é, è, ê, ë, à, ù, ç, œ, æ
- Double-check diacritical marks (many African translators omit them)
- UTF-8 encoding mandatory

#### Apostrophes in Astro JSX Templates (French, Swahili, all languages)
**CRITICAL:** Single-quoted JS strings inside Astro JSX expressions (`.astro` template section) CANNOT contain straight apostrophes (`'`). This breaks the build because the apostrophe terminates the string early.

**Rules for any text containing apostrophes (e.g. French `d'`, `l'`, `n'`, `qu'`; Swahili `ng'`):**
1. **Use double-quoted strings** for any JS string literal that contains an apostrophe: `"d'excellence"` not `'d\'excellence'`
2. **Never use `\u2019` escape sequences** — Astro's template compiler may not handle them correctly
3. **Never use backslash-escaped apostrophes** (`\'`) in JSX template expressions — they work in frontmatter JS but fail in template JSX
4. **HTML text content is fine** — apostrophes in regular HTML `<p>d'excellence</p>` work without escaping
5. For JSX expression strings that need both `"` and `'`, use template literals: `` `string with ' and "` ``

#### Verb Conjugation
- Use **vous** for all formal communication (not tu)
- Example: "Veuillez remplir le formulaire" (not "Remplis le formulaire")
- Imperative form: "Veuillez" + infinitive for politeness

#### Gender Agreement
All adjectives and past participles must agree with gender:
- "La page est complétée" (feminine)
- "Le service est complété" (masculine)
- "Les pages sont complétées" (feminine plural)

### French Dates and Numbers
- **Date format**: 17 février 2026 (or 17 février 2026)
- **Month names**: Lowercase (février, not Février)
- **Numbers**: Use space or period for thousands: 1 000 or 1.000 (not 1,000)
- **Decimal separator**: Comma (not period): 3,14 (not 3.14)
- **Currency**: Franc CFA (FCFA), Euro (€), or specified in design-tokens.md

### Formal Registers and Politeness
#### Standard Openings
- Madame, Monsieur,
- Chère Madame, Cher Monsieur,
- Greetings,

#### Standard Closings
- Cordialement, (warm, professional)
- Respectueusement, (respectful)
- Avec mes meilleures salutations,
- Veuillez agréer l'expression de nos salutations distinguées.

#### Courtesy Phrases (French)
- Nous vous prions de…
- Veuillez… (imperative form with "vous")
- Merci de votre attention.
- Nous apprécions votre partenariat.
- N'hésitez pas à nous contacter.
- Nous vous remercions de votre soutien continu.
- Nous attendons avec intérêt votre réponse.
- Si vous avez besoin de précisions supplémentaires, veuillez nous contacter.

### French Vocabulary Standards
#### Preferred Professional Terms
- Faciliter, mettre en œuvre, entreprendre, coordonner
- Engager, soutenir, améliorer, examiner, confirmer
- Conseiller, informer, communiquer
- Significatif, important, stratégique, bénéfique, précieux

#### Words to Avoid (Marketing Hype)
| Avoid | Use Instead |
|-------|-------------|
| révolutionnaire | innovant |
| "game-changing" | stratégique |
| incroyable | remarquable |
| génial | excellent |
| dingue | étonnant |
| Libérez le pouvoir | Activez la capacité |

#### Francophone African Terminology
Use terms understood across francophone Africa (not Canada-specific, not France-specific):
- Budget (not "subvention")
- Entreprise (company, not "compagnie")
- Personnel (staff, not "employés" alone)
- Client (customer/client, standard everywhere)
- Formation (training, widely used)

### French CTAs and Button Text
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

### French-Specific Considerations
#### In-Country Reviewer Required
All French content must be reviewed by a native francophone speaker from the target market (Côte d'Ivoire, Cameroon, Senegal, DRC, Gabon). Send for review before publishing.

#### Text Expansion
French is typically 20–40% longer than English. Design for 1.3x expansion:
- Buttons must accommodate longer labels
- Navigation items must wrap gracefully
- Form labels must not overlap fields

#### Regional Variations
Avoid country-specific terms unless relevant:
- Use neutral francophone African vocabulary
- Avoid France-centric references
- Avoid Canadian (Québécois) terminology

#### Francophone Africa Geographic Scope
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

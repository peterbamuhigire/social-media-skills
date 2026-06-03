# French Typography and Formatting

**Purpose**: Apply the French typographic rules that differ from English. Wrong spacing and punctuation are an instant, visible signal of non-native or translated copy, independent of how good the words are.

**Read this when**: You are finalising French copy, building components that render French strings, or reviewing a page for typographic correctness.

## Spacing before two-part punctuation

French puts a space before the "high" punctuation marks `;` `:` `!` `?` and inside `« »`. English does not.

- Correct: `Vous hésitez ?`, `Une seule promesse : la qualité.`, `Bravo !`
- The correct character is a **narrow non-breaking space** (U+202F), or a non-breaking space (U+00A0) as a fallback, so the mark never wraps to the next line. A normal space is a typographic error here; no space is an English habit.
- In HTML, use `&#8239;` (narrow NBSP) or `&nbsp;` before `; : ! ?` and after `«` / before `»`. In a CMS that strips these, document the convention for the build.
- The comma `,` and full stop `.` take **no** space before, like English.

## Quotation marks

- French uses guillemets `« … »` with a non-breaking space inside both: `« Un travail remarquable »`.
- Nested quotation uses English double curly quotes inside guillemets: `« Il a dit "oui" sans hésiter »`.
- Never use straight quotes `"..."` in published copy. For apostrophes use the curly `'` (`l'équipe`, `aujourd'hui`), not the straight `'`.

## Numbers

- **Decimal separator is a comma**: `3,50`, `12,99 %`. A full stop as decimal is an English error.
- **Thousands separator is a non-breaking space**, not a comma or full stop: `1 250`, `10 000`, `1 000 000`.
- Percentage: a non-breaking space before `%`: `20 %`, not `20%`.
- Ordinals: `1er` (premier), `1re` (première), `2e`, `3e` — not `1st`/`2nd`. `N°` or `n°` for "number" (`n° 12`).

## Currency

- The symbol follows the number, after a non-breaking space: `50 €`, `1 250,00 €`. `€50` is an English/US habit.
- Francophone Africa: the CFA franc is written `FCFA` or `F CFA` after the amount: `25 000 FCFA`. Confirm which franc zone (XOF West / XAF Central) for the audience.
- Canada: dollar is `50 $` (symbol after, Québec convention), or `50 CAD` in formal contexts.

## Dates and time

- Order is day–month–year, month lowercase: `le 14 juillet 2026`, `mardi 5 mai`. Numeric: `14/07/2026`.
- No ordinal on the day except the first: `le 1er mai`, then `le 2 mai`, `le 3 mai`.
- Time uses `h` as separator, 24-hour clock: `14 h 30`, `9 h`, `18 h 00`. Not `2:30 PM`.
- Opening hours: `du lundi au vendredi, de 9 h à 18 h`.

## Capitalisation (French capitalises less than English)

- Days and months are lowercase: `lundi`, `janvier`.
- Languages and nationalities as adjectives are lowercase: `un client français`, `le marché allemand`. As a noun for the people, capitalise: `les Français`.
- Titles and headings use **sentence case**, not Title Case: `Nos services de conseil`, not `Nos Services De Conseil`. Capitalising every word is an English convention and looks wrong in French.
- In a title, only the first word (and proper nouns) take a capital.
- Accents on capitals are required in correct French: `À propos`, `Établissement`, `É`, `È`, `Ç`. Dropping them (`A propos`) is a common but real error — keep them.

## Accents and special characters

- Always render accents: `é è ê ë à â ä ù û ü ô ö î ï ç œ`. `œ` is a real ligature (`cœur`, `œuvre`, `sœur`), not `oe`.
- Ensure the page declares UTF-8 and fonts include full Latin-1/accent coverage, or accented characters break — a frequent production bug on French pages.

## Abbreviations

- `M.` (Monsieur), `Mme` (Madame, no full stop), `Mlle` (Mademoiselle — dated; prefer `Madame`), `Dr` (no full stop), `etc.` (never `…etc`), `c.-à-d.` (that is), `p. ex.` (for example), `cf.`.
- Phone numbers group in pairs: `+33 1 23 45 67 89`; in Africa, group per local convention but keep the international `+` format for the web.

## Quick render checklist

- Space before `; : ! ?` and inside `« »` (narrow NBSP).
- Decimal comma, space thousands, space before `%`, `€` after the amount.
- Sentence-case headings, lowercase days/months/nationalities, accents on capitals.
- Curly apostrophes and guillemets, never straight quotes.
- UTF-8 declared and font covers all accents.

## For social / short-form

- Captions are plain Unicode text, so use the real characters directly: curly apostrophe `'` (`l'offre`, `aujourd'hui`), guillemets `« »`, `é è à ç œ`, decimal comma, `FCFA`/`€` after the amount. Type them; most platforms accept and render them.
- The narrow non-breaking space before `; : ! ?` is correct but some platforms collapse it — a normal space before these marks is an acceptable fallback in captions, never *no* space (`Bravo !`, not `Bravo!`).
- Hashtags don't take internal spaces or punctuation; use CamelCase for multi-word tags (`#AfriqueFrancophone`) and keep accents (`#CôteDIvoire`). 
- Prices in captions: `25 000 FCFA`, `1 250 € `— symbol/currency after the number, space before `%` (`-20 %`).
- Sentence case for the brand's display text and bios; don't Title-Case French words.

## Source

French typographic conventions per standard French usage (Imprimerie nationale rules), confirmed against examples in *Read & Think French, Premium* (Think French magazine) and *French Grammar in 44 Lessons* (Sylvie Poisson-Quinton); short-form notes for the social engine.

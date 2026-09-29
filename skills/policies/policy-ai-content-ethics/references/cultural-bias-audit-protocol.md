# Cultural Bias Audit Protocol

Merged from skills/ai-marketing/ai-cultural-bias-audit on 2026-09-29 at 7c60138; preservation map: [ai-cultural-bias-audit.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/ai-cultural-bias-audit.md)

## When to use this reference

Use it when the policy's Training Data Bias control (Section 2D of the skill) must be run as an actual pre-delivery audit: a structured, signed report that identifies and corrects cultural bias in AI-generated content before it reaches the client. It draws on documented failure cases and the IBM AI Fairness 360 framework to give a systematic review process.

- **Default context:** Uganda and East Africa. All examples, checks and correction guidance apply the East African market as the baseline unless another jurisdiction is specified.
- **Output:** an evidence-backed audit report with findings per checklist item, a named and qualified reviewer, a corrective action per issue, and a signed, dated record for the agency's production file.
- **Nearest routing comparison:** `ai-readiness-diagnostic` (skills/ai-marketing) when the real deliverable is an AI readiness or maturity assessment rather than a bias audit.
- **Principal source:** Ching, V. and Mothi, D. (2025) *AI for Creatives: Unlocking Expressive Digital Potential*, CRC Press.

## Inputs

Ask for the following before running the audit:

1. **Client business name** — the organisation for whom content was produced.
2. **Industry** — sector and primary audience description.
3. **Country / city** — the specific East African (or other) market the content is intended for.
4. **Primary goal** — the campaign or deliverable objective.
5. **Content type** — which apply: social media copy, blog post, visual asset descriptions, audience personas, campaign concept, product description, or other.
6. **AI tools used** — which generative AI systems produced the content under review.
7. **Reviewer identity** — who will conduct the cultural review, with confirmation that they have direct first-hand knowledge of the target community (see Reviewer qualification standard).

## Decision rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate | Automating an unsafe or unevaluable marketing process |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder | Fabricated facts, implied consent or unauthorised publication |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step | Treating an unassessed requirement as passed |
| No reviewer meets the qualification standard | Do not sign off; record the check `not assessed` and source a qualified reviewer | Approval by someone without direct cultural knowledge |
| Bias is structural and pervasive | Reject and regenerate rather than patch | Localised captions on Western-default outputs |

## Why AI has systematic cultural bias

### The training data problem

Generative AI models are trained predominantly on English-language, Western-origin internet data. This creates systematic defaults:

- **Aesthetic defaults:** human subjects generated without explicit instruction default to Western physical features, clothing and settings.
- **Naming defaults:** AI-generated names default to Anglo-American or broadly European names.
- **Behavioural defaults:** consumer behaviour patterns, shopping habits, commuting patterns and social norms reflect Western market assumptions.
- **Economic defaults:** pricing references, product categories and aspirational markers default to Western economic contexts.
- **Geographic defaults:** "urban professional" imagery defaults to generic Western city environments.

These are not occasional errors. They are structural properties of models trained on Western-dominated datasets, and they persist even when a diversity brief is explicitly provided.

### The uncanny valley of cultural representation

Content that is almost-but-not-quite culturally accurate is more damaging than content that is openly generic Western. An audience in Kampala or Nairobi immediately recognises:

- a Ugandan name that no Ugandan family would actually use;
- a market scene that looks like a Western film set's idea of Africa;
- copy that mentions "popping to the shops" or "the school run" in an East African context;
- depicted infrastructure (roads, buildings, transport) that bears no resemblance to the actual city.

This partial representation signals that the brand does not understand its audience. It erodes trust more effectively than using no localisation at all.

## Documented failure cases

### Primary case — BuzzFeed Barbie (2023)

In 2023 BuzzFeed used AI image generation to create Barbie doll representations for different countries as part of a viral content series. Despite an explicit diversity and cultural accuracy brief, the outputs showed:

- racial stereotyping inconsistent with the actual populations of the depicted countries;
- culturally inaccurate costumes — a Western imagination of "traditional dress" rather than actual cultural garments;
- settings and aesthetics that defaulted to Western representations of non-Western environments.

The failure occurred because the model's Western training data dominated the output even when the prompt specified non-Western subjects. The explicit diversity brief was not enough to override the model's structural defaults.

**Lesson:** an explicit brief for cultural accuracy does not guarantee cultural accuracy. A structured human review by someone with direct cultural knowledge is mandatory.

### Secondary case — DeepVogue

The DeepVogue AI fashion generation system showed similar defaults: AI-generated "global" fashion content defaulted to Western body standards, Western aesthetic frameworks and Western interpretations of non-Western fashion traditions. Models depicting non-Western cultural dress frequently blended or confused distinct cultural traditions (documented in Ching and Mothi, 2025).

**Lesson:** AI systems cannot reliably distinguish between specific cultural traditions within a region. "East African" is not a single aesthetic. Ugandan, Kenyan and Tanzanian professional and cultural aesthetics are distinct and must be reviewed separately.

## Evaluative standard — IBM AI Fairness 360

IBM AI Fairness 360 (AIF360) is an open-source toolkit for evaluating algorithmic fairness across protected attributes including race, gender and national origin. Apply it as a conceptual framework for content audits:

- **Individual fairness:** would a person from the specific target community see themselves accurately reflected?
- **Group fairness:** does the content represent the demographic composition of the actual target community, or a distorted version of it?
- **Counterfactual fairness:** if the same brief had been run for a Western audience, would the output have received the same level of cultural accuracy and specificity?

For practical content review, these principles translate into the checklist below.

## Procedure

1. Confirm the exact audit report, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Confirm the reviewer meets the qualification standard before review begins.
4. Run the pre-delivery checklist (4A visual, 4B copy, 4C persona — whichever apply) and record the reviewer's name, date and finding for each item.
5. Apply the correction protocol to every failed item and re-run the affected checklist items.
6. Deliver the signed audit record with evidence, assumptions, unassessed checks and the next approval or verification step.

## Pre-delivery bias checklist

Run it on every AI-assisted deliverable before client submission. Record the reviewer's name, date and findings for each item.

### 4A — Visual content

Apply to all AI-generated images, image briefs, stock photo selections and visual descriptions:

- [ ] Does the depicted person or group reflect the actual demographic and physical characteristics of the target community — not a generic or stereotyped representation?
- [ ] Are clothing and styling consistent with how people in this specific community actually present in the relevant professional or social context?
- [ ] Are depicted settings (buildings, roads, transport, landscapes) consistent with the actual physical environment of the specified city or region?
- [ ] Does the depicted technology (mobile phones, laptops, vehicles, payment methods) reflect what is actually used in this market?
- [ ] Has the content been reviewed by someone with direct, first-hand knowledge of this community — not merely geographic proximity or general "African" knowledge?
- [ ] Does the image avoid conflating distinct East African national or ethnic identities under a single generic representation?

### 4B — Copy and text

Apply to all AI-generated social media captions, body copy, headlines, scripts and descriptions:

- [ ] Are all idioms, expressions and colloquialisms consistent with the professional register used in this specific market? (Flag any expression that reads as British, American or generic "international English".)
- [ ] Are all pricing references, product examples and economic assumptions consistent with the actual purchasing power and consumer behaviour of this market?
- [ ] Are all food, transport and lifestyle references accurate for this community? (Flag "grabbing a coffee", "the commute", "the school run", "the weekly shop" or equivalent Western defaults.)
- [ ] Are any named individuals, brands or locations accurate references for this market, not generic Western substitutions?
- [ ] Does the copy assume digital infrastructure (broadband speed, device ownership, payment systems) inconsistent with the actual East African context?
- [ ] Is the tone and register consistent with how professionals in this specific community communicate — not a Western approximation of "African" informality or formality?

### 4C — Audience personas

Apply to all AI-generated audience personas, customer profiles and market segment descriptions:

- [ ] Are the persona's name, family structure and social context consistent with naming conventions and family norms in the specific country and community (not generic "African" names)?
- [ ] Is the persona's income level, occupation and consumption behaviour consistent with verified market data for this segment in this country?
- [ ] Does the persona's media consumption reflect actual East African platform usage (WhatsApp primary, Facebook dominant, mobile-first, data-cost sensitivity) rather than Western defaults?
- [ ] Does the persona's decision-making process reflect actual purchasing and trust-building patterns in this community (community referrals, church/mosque networks, extended family input) rather than Western individualist consumer models?
- [ ] Has the persona been reviewed by someone who is a member of, or has direct professional experience working with, the described community?

## Reviewer qualification standard

Every AI cultural bias audit must be signed off by a human reviewer who meets this standard.

**Minimum qualification — direct, first-hand knowledge of the target community.** The reviewer:

- has lived in the specific country or city being targeted; or
- has substantial direct professional experience serving clients from that community; or
- is a member of the cultural or ethnic community represented in the content.

**Not sufficient:**

- general knowledge of "Africa" or "East Africa" as a region;
- having visited the country once or twice;
- reading about the culture or community without direct lived experience;
- being from a neighbouring country (Kenyan market knowledge does not substitute for Ugandan market knowledge).

### Sign-off record template

> *Reviewed by: [Name] | Qualification: [Direct knowledge basis] | Date: [Date] | Finding: [Pass / Requires correction / Reject and regenerate]*

## Correction protocol

When the audit identifies bias or inaccuracy, apply corrections in this order:

1. **Reject and regenerate** — if the bias is structural and pervasive, do not patch the AI output; regenerate with a more specific, culturally grounded prompt.
2. **Human rewrite** — for copy, have a human writer with knowledge of the target market rewrite from the AI draft, treating it as raw material only.
3. **Targeted edit** — for isolated errors (a single wrong name, a single Western idiom), apply a direct targeted edit and re-run the relevant checklist item.
4. **Visual brief revision** — for image briefs or visual descriptions, revise the brief with explicit cultural markers and regenerate; do not use a Western-default image with a localised caption.

### Prompt improvement for the East African context

When regenerating AI content for East African markets, include this specificity in every prompt:

- Name the specific country (Uganda, Kenya, Tanzania) — never "Africa" or "East Africa" alone.
- Name the specific city where the target audience lives.
- Specify the actual demographic (age range, occupation, income bracket in local-currency context).
- Specify the language register (formal Ugandan English, Swahili-influenced Kenyan professional English, and so on).
- Include the explicit instruction: *"Do not default to Western aesthetics, Western naming conventions, or Western consumer behaviour patterns."*

## Acceptance checklist for the audit report

- [ ] Identifies specific instances of bias with precise reference to the checklist item failed, not vague general observations.
- [ ] Distinguishes visual, copy and persona bias and gives separate findings for each.
- [ ] Names the human reviewer and documents their qualification to assess the specific community.
- [ ] Recommends a specific corrective action (reject and regenerate, human rewrite, targeted edit, visual brief revision) for each issue.
- [ ] References the BuzzFeed Barbie failure case where relevant, to show why explicit diversity briefs alone are insufficient.
- [ ] Treats "East African" as multiple distinct cultures — findings are country- and community-specific.
- [ ] Applies individual, group and counterfactual fairness (AIF360) as the evaluative standard.
- [ ] Produces a signed, dated audit record for the agency's production file.
- [ ] Marks unavailable checks (missing files, network, platform data, language review) `not assessed`; never converts them into a pass.

## Sources

- Ching, V. and Mothi, D. (2025) *AI for Creatives: Unlocking Expressive Digital Potential*. CRC Press.
- IBM Research (2018–present) *AI Fairness 360 (AIF360)* — open-source fairness toolkit. Available at: aif360.mybluemix.net (verify the current URL before citing).
- BuzzFeed (2023) — AI Barbie series (documented failure case; original publication and subsequent critical analysis).
- DeepVogue — AI fashion generation bias documentation (Ching and Mothi, 2025).

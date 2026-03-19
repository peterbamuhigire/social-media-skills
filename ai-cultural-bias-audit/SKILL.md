---
name: ai-cultural-bias-audit
description: >
  Runs a structured pre-delivery audit of AI-generated content — copy, images, and personas — for cultural bias,
  Western default assumptions, and inaccurate cultural representation, with specific attention to East African
  and non-Western contexts. Invoke before any AI-assisted deliverable is sent to a client, whenever AI tools have
  generated content depicting people, communities, or cultural settings, or when an internal review flags that
  content feels generically "Western" or generically "African" rather than accurately localised.
---

# AI Cultural Bias Audit Protocol

## Purpose

This skill produces a structured pre-delivery audit report that identifies and corrects cultural bias in AI-generated content before it reaches the client. It draws on documented failure cases and the IBM AI Fairness 360 framework to provide a systematic review process.

> **Default context:** Uganda and East Africa. All examples, checks, and correction guidance apply the EA market as the baseline unless another jurisdiction is specified.

**Source:** Ching, V. and Mothi, D. (2025) *AI for Creatives: Unlocking Expressive Digital Potential*. CRC Press.

---

## Required Inputs

Ask for the following before running the audit:

1. **Client business name** — the organisation for whom content was produced
2. **Industry** — sector and primary audience description
3. **Country / city** — the specific East African (or other) market the content is intended for
4. **Primary goal** — the campaign or deliverable objective
5. **Content type** — specify which of the following apply: social media copy, blog post, visual asset descriptions, audience personas, campaign concept, product description, or other
6. **AI tools used** — which generative AI systems produced the content under review
7. **Reviewer identity** — who will conduct the cultural review, and confirm they have direct first-hand knowledge of the target community (see Part 5)

---

## Part 1: Why AI Has Systematic Cultural Bias

### The Training Data Problem

Generative AI models are trained predominantly on English-language, Western-origin internet data. This creates systematic defaults:

- **Aesthetic defaults:** Human subjects generated without explicit instruction default to Western physical features, clothing, and settings
- **Naming defaults:** AI-generated names default to Anglo-American or broadly European names
- **Behavioural defaults:** Consumer behaviour patterns, shopping habits, commuting patterns, and social norms in AI outputs reflect Western market assumptions
- **Economic defaults:** Pricing references, product categories, and aspirational markers default to Western economic contexts
- **Geographic defaults:** "Urban professional" imagery defaults to generic Western city environments

These are not occasional errors. They are structural properties of models trained on Western-dominated datasets. They persist even when a diversity brief is explicitly provided.

### The Uncanny Valley of Cultural Representation

Content that is almost-but-not-quite culturally accurate is more damaging than content that is openly generic Western. An audience in Kampala or Nairobi immediately recognises:

- A Ugandan name that no Ugandan family would actually use
- A market scene that looks like a Western film set's idea of Africa
- Copy that mentions "popping to the shops" or "the school run" in an EA context
- Depicted infrastructure (roads, buildings, transport) that bears no resemblance to the actual city

This partial representation signals that the brand does not understand its audience. It erodes trust more effectively than simply using no localisation at all.

---

## Part 2: Documented Failure Cases

### Primary Case — BuzzFeed Barbie (2023)

In 2023, BuzzFeed used AI image generation to create Barbie doll representations for different countries as part of a viral content series. Despite an explicit diversity and cultural accuracy brief, the outputs exhibited:

- Racial stereotyping inconsistent with the actual populations of the depicted countries
- Costumes that were culturally inaccurate — representing a Western imagination of "traditional dress" rather than actual cultural garments
- Settings and aesthetics that defaulted to Western representations of non-Western environments

The failure occurred because the AI model's Western training data dominated the output even when the prompt specified non-Western subjects. The explicit diversity brief was not sufficient to override the model's structural defaults.

**Lesson:** An explicit brief for cultural accuracy does not guarantee cultural accuracy. A structured human review by someone with direct cultural knowledge is mandatory.

### Secondary Case — DeepVogue

The DeepVogue AI fashion generation system demonstrated similar defaults in fashion imagery: AI-generated "global" fashion content defaulted to Western body standards, Western aesthetic frameworks, and Western interpretations of non-Western fashion traditions. Models depicting non-Western cultural dress frequently blended or confused distinct cultural traditions.

**Lesson:** AI systems cannot reliably distinguish between specific cultural traditions within a region. "East African" is not a single aesthetic. Ugandan, Kenyan, and Tanzanian professional and cultural aesthetics are distinct and must be reviewed separately.

---

## Part 3: IBM AI Fairness 360

IBM AI Fairness 360 (AIF360) is an open-source toolkit for evaluating algorithmic fairness across protected attributes including race, gender, and national origin. Apply it as a conceptual framework for content audits:

- **Individual fairness:** Would a person from the specific target community see themselves accurately reflected?
- **Group fairness:** Does the content represent the demographic composition of the actual target community, or a distorted version of it?
- **Counterfactual fairness:** If the same brief had been run for a Western audience, would the output have received the same level of cultural accuracy and specificity?

For practical content review, translate these principles into the checklist in Part 4.

---

## Part 4: Pre-Delivery Bias Checklist

Run this checklist on every AI-assisted deliverable before client submission. Record the reviewer's name, date, and findings for each item.

### 4A — Visual Content Checklist

Apply to all AI-generated images, image briefs, stock photo selections, and visual descriptions:

- [ ] Does the depicted person or group reflect the actual demographic and physical characteristics of the target community — not a generic or stereotyped representation?
- [ ] Are clothing and styling consistent with how people in this specific community actually present in the relevant professional or social context?
- [ ] Are depicted settings (buildings, roads, transport, landscapes) consistent with the actual physical environment of the specified city or region?
- [ ] Does the depicted technology (mobile phones, laptops, vehicles, payment methods) reflect what is actually used in this market?
- [ ] Has the content been reviewed by someone with direct, first-hand knowledge of this community — not merely geographic proximity or general "African" knowledge?
- [ ] Does the image avoid conflating distinct East African national or ethnic identities under a single generic representation?

### 4B — Copy and Text Checklist

Apply to all AI-generated social media captions, body copy, headlines, scripts, and descriptions:

- [ ] Are all idioms, expressions, and colloquialisms consistent with the professional register used in this specific market? (Flag any expressions that read as British, American, or generic "international English")
- [ ] Are all pricing references, product examples, and economic assumptions consistent with the actual purchasing power and consumer behaviour of this market?
- [ ] Are all food, transport, and lifestyle references accurate for this community? (Flag "grabbing a coffee," "the commute," "the school run," "the weekly shop," or equivalent Western defaults)
- [ ] Are any named individuals, brands, or locations accurate references for this market, not generic Western substitutions?
- [ ] Does the copy assume digital infrastructure (broadband speed, device ownership, payment systems) that is inconsistent with the actual EA context?
- [ ] Is the tone and register consistent with how professionals in this specific community communicate — not a Western approximation of "African" informality or formality?

### 4C — Audience Persona Checklist

Apply to all AI-generated audience personas, customer profiles, and market segment descriptions:

- [ ] Are the persona's name, family structure, and social context consistent with naming conventions and family norms in the specific country and community (not generic "African" names)?
- [ ] Is the persona's described income level, occupation, and consumption behaviour consistent with verified market data for this segment in this country?
- [ ] Does the persona's media consumption pattern reflect actual EA platform usage (WhatsApp primary, Facebook dominant, mobile-first, data cost sensitivity) rather than Western defaults?
- [ ] Does the persona's described decision-making process reflect actual purchasing and trust-building patterns in this community (community referrals, church/mosque networks, extended family input) rather than Western individualist consumer models?
- [ ] Has the persona been reviewed by someone who is actually a member of, or has direct professional experience working with, the described community?

---

## Part 5: Reviewer Qualification Standard

### The Mandatory Human Reviewer

Every AI cultural bias audit must be signed off by a human reviewer who meets the following standard:

**Minimum qualification:** Direct, first-hand knowledge of the target community. This means:
- Has lived in the specific country or city being targeted, or
- Has substantial direct professional experience serving clients from that community, or
- Is a member of the cultural or ethnic community being represented in the content

**Not sufficient:**
- General knowledge of "Africa" or "East Africa" as a region
- Having visited the country once or twice
- Reading about the culture or community without direct lived experience
- Being from a neighbouring country (Kenyan market knowledge does not substitute for Ugandan market knowledge)

### Reviewer Sign-Off

The audit report must record:

> *Reviewed by: [Name] | Qualification: [Direct knowledge basis] | Date: [Date] | Finding: [Pass / Requires correction / Reject and regenerate]*

---

## Part 6: Correction Protocol

When the audit identifies bias or inaccuracy, apply corrections in the following order:

1. **Reject and regenerate** — if the bias is structural and pervasive, do not attempt to patch the AI output; regenerate with a more specific, culturally grounded prompt
2. **Human rewrite** — for copy, have a human writer with knowledge of the target market rewrite from the AI draft, treating it as raw material only
3. **Targeted edit** — for isolated errors (a single wrong name, a single Western idiom), apply a direct targeted edit and re-run the relevant checklist item
4. **Visual brief revision** — for image briefs or visual descriptions, revise the brief with explicit cultural markers and regenerate; do not use a Western-default image with a localised caption

### Prompt Improvement for EA Context

When regenerating AI content for East African markets, include the following specificity in every prompt:

- Name the specific country (Uganda, Kenya, Tanzania) — never "Africa" or "East Africa" alone
- Name the specific city where the target audience lives
- Specify the actual demographic (age range, occupation, income bracket in local currency context)
- Specify the language register (formal Ugandan English, Swahili-influenced Kenyan professional English, etc.)
- Include explicit instruction: *"Do not default to Western aesthetics, Western naming conventions, or Western consumer behaviour patterns"*

---

## Quality Criteria

A well-produced cultural bias audit under this skill:

- Identifies specific instances of bias with precise reference to the checklist item failed, not vague general observations
- Distinguishes between different categories of bias — visual, copy, persona — and provides separate findings for each
- Names the human reviewer and documents their qualification to assess the specific community
- Recommends a specific corrective action (reject and regenerate, human rewrite, targeted edit) for each identified issue
- References the BuzzFeed Barbie failure case where relevant to illustrate why explicit diversity briefs alone are insufficient
- Treats "East African" as multiple distinct cultures, not a single category — findings must be country- and community-specific
- Applies the IBM AI Fairness 360 principles of individual fairness, group fairness, and counterfactual fairness as the evaluative standard
- Produces a signed, dated audit record suitable for the agency's production file

---

## References

- Ching, V. and Mothi, D. (2025) *AI for Creatives: Unlocking Expressive Digital Potential*. CRC Press.
- IBM Research (2018–present) *AI Fairness 360 (AIF360)* — open-source fairness toolkit. Available at: aif360.mybluemix.net
- BuzzFeed (2023) — AI Barbie series (documented failure case; original publication and subsequent critical analysis)
- DeepVogue — AI fashion generation bias documentation (Ching and Mothi, 2025)

# Synthetic Persona Hypotheses

Merged from skills/ai-marketing/ai-synthetic-personas on 2026-09-29 at cda737c (S04 tree); preservation map: [ai-synthetic-personas.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/ai-synthetic-personas.md)

## When to use this reference

Read this reference when primary audience research is not available and the client still needs personas: AI-assisted synthesis from secondary data and East African market knowledge, a synthetic focus group to test a campaign concept, or rapid validation of hypotheses before fieldwork is commissioned. Personas produced this way are informed hypotheses grounded in secondary data, not primary research findings, and every deliverable that uses them carries the disclosure in [Disclosure standard](#disclosure-standard).

Apply the `east-african-english` skill for tone throughout. Where the client can commission primary research, use the research-grounded method in the parent [SKILL.md](../SKILL.md) and return here only for supplementary rapid-validation work.

## Inputs

Ask for the following before generating any persona:

| Input | What to capture |
|---|---|
| Client business name | The trading name as used publicly |
| Industry | Be specific, for example "private healthcare clinic", "SME accounting software", "mid-range restaurant chain" |
| Country / city | Defaults to Kampala, Uganda; adjust East African norms for Kenya or Tanzania where relevant |
| Target audience description | Age range, income band, location (urban, peri-urban or rural) and any known sub-segments |
| Primary goal | Choose one: strategy development, messaging validation, content planning or campaign targeting |
| Available secondary data | Existing research, sales data, customer feedback or Meta Audience Insights the client can share; record "none available" if there is nothing |

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| Budget for primary research is unavailable, the timeline is under two weeks, hypotheses need rapid validation before fieldwork, or the client has secondary data (sales records, CRM data, website analytics) to anchor the output | Use synthetic personas, disclosed as hypotheses. | Stalling strategy work for want of fieldwork. |
| A new product is launching in an unfamiliar market where AI training data is likely thin | Commission primary research instead. | Personas invented from thin model knowledge. |
| The decision at stake is above UGX 50 million in campaign or product investment | Commission primary research instead. | A high-value decision resting on hypotheses. |
| AI training data probably under-represents the audience (rural low-income segments, elderly populations, niche occupational groups) | Commission primary research instead. | Systematic bias against the least-documented groups. |
| The client has had prior strategy failures suggesting existing assumptions are wrong | Commission primary research instead. | Regenerating the assumptions that already failed. |
| Any synthetic persona is used | Disclose its synthetic origin, flag every assumption not cross-referenced against secondary data, and treat it as a starting point, not a conclusion. | Hypotheses presented as findings. |
| The synthetic output cannot satisfy the three discipline caveats below | Do not ship; return to primary research through the parent SKILL.md or rerun with stronger constraints. | Releasing personas that mirror the operator. |

## Uganda / East Africa calibration

Apply this demographic and behavioural context when building prompts, adjusted for the client's country and city. It overlaps with the parent SKILL.md section "Uganda / East Africa Consumer Behaviour"; the income bands and the trust and language notes are specific to synthetic prompting.

**Income bands (UGX per month; engine house bands, not a UBOS statistic; check against UBOS-NSI-2026 before quoting):**

| Band | Monthly income |
|---|---|
| Low income | Under UGX 500,000 |
| Lower-middle income | UGX 500,000 – 1,500,000 |
| Middle income | UGX 1,500,000 – 5,000,000 |
| Upper-middle income | Above UGX 5,000,000 |

**Platform norms:**

- **WhatsApp** — primary communication channel across all income levels; business enquiries, referrals and purchase decisions often happen in WhatsApp groups and direct messages.
- **Facebook** — broadest reach; urban and peri-urban, 18–55+, all income levels.
- **TikTok** — fast-growing, urban youth 16–30, entertainment-first.
- **LinkedIn** — formal-sector professionals, NGO workers, senior management, B2B audiences.
- **YouTube** — research, tutorials and long-form; watched when users have Wi-Fi access.

Platform reach claims change: verify at use; see register WHATSAPP-USAGE-EA-2026 and DATAREPORTAL-UG-KE-2026. Facebook access in Uganda has been unstable (blocked from January 2021, reported accessible from 13 June 2026); verify at the campaign date; see register UG-FACEBOOK-ACCESS-2026.

**Trust conditions:**

- Word-of-mouth and community recommendations carry high weight; many segments view formal advertising with scepticism.
- Social proof from peers and WhatsApp group endorsements consistently outperforms broadcast advertising.
- Localisation — local language, local place names, local events — drives markedly higher engagement than generic international content.

**Language:**

- Most urban Ugandans code-switch between English and Luganda; formal communication defaults to English.
- Luganda phrases in captions or calls to action can make Kampala mass-market content more relatable.
- Kiswahili is the local-language calibration for Kenya and Tanzania.

## Procedure

1. Confirm the inputs and apply the decision rules above; record which condition justifies synthetic work.
2. Name each intended persona's pain points **before** generation (see the discipline caveats), so the model cannot simply mirror the operator.
3. Run the persona prompt once per persona, adding the calibration data above for Ugandan clients to anchor the output in realistic local context.
4. Shape the three outputs into the 3-persona format and the side-by-side summary.
5. Run the synthetic focus group for at least one campaign concept.
6. Complete the validation checklist, add bracketed risk notes and the disclosure footnote, then declare the Essential Persona.

### Persona prompt template

Replace every bracketed placeholder with the client's details before running. Run once per persona.

```
You are a market researcher specialising in Uganda/East Africa consumer behaviour.

Generate a detailed audience persona for a [industry] business targeting
[audience description] in [location].

Include:
- Name and age
- Occupation and income range (in UGX)
- Education level
- Primary social media platforms used and how (passive/active, time of day)
- WhatsApp usage (personal/business, groups joined, typical message patterns)
- Daily routine (morning to evening — brief)
- Top 3 pain points related to [product/service category]
- Top 3 goals or aspirations related to [product/service category]
- Barriers to purchase or engagement
- Preferred content format (video, text, image, audio)
- Language and register preferences (formal English, casual English, Luganda, Kiswahili)
- Trusted information sources (family, WhatsApp groups, Facebook, radio, newspaper)
- A direct quote that captures their attitude toward [brand/product category]
```

### 3-persona output format

Generate three distinct personas per engagement. Do not build all three on the same demographic profile; vary income, age or use case in a meaningful way.

- **Primary persona** — the highest-value or most common customer segment; the person the strategy is mainly built around.
- **Secondary persona** — the second-priority segment; often a different demographic or a distinct use case (for example a gifter rather than an end user, or a B2B decision-maker alongside a B2C buyer).
- **Edge persona** — a segment the client may be overlooking: a future growth opportunity, an underserved demographic or a non-obvious use case. State explicitly that this persona is a growth hypothesis.

| Field | Detail |
|---|---|
| **Name** | Realistic East African name (for example Harriet, Brian, Fatuma, Ronald, Aisha) |
| **Archetype label** | A specific label for this client's context (for example "The Growth-Minded SME Owner") |
| **Day in the life** | Three sentences — morning, workday, evening — grounded in this persona's circumstances |
| **Content preferences** | Two to three specific formats, with examples relevant to the client's category |
| **Messaging triggers** | Three specific reasons this persona would engage with or buy from the client |
| **Primary platforms** | The one or two platforms where this persona is most reachable and most likely to act |
| **Key barriers** | Two to three specific obstacles to purchase or engagement |

After the three persona cards, produce a **side-by-side summary table** using the same fields for quick team reference.

### Synthetic focus group

Use this to simulate audience reactions to campaign concepts before paying for creative production, for messaging validation and campaign-brief development. Run the prompt for each of the three personas:

```
You are [Persona Name], a [description — occupation, age, income, location].

The brand [Client Name] is about to launch [campaign concept — one sentence].

Answer the following:
1. What is your first reaction to this campaign?
2. What would make you engage with it (like, comment, share, visit, buy)?
3. What would put you off or make you scroll past?
4. What would you tell a friend about this brand after seeing this campaign?
```

Analyse the three responses for:

- **Universal appeal** — elements that matter to all three personas.
- **Segment-specific messaging** — elements that work for one persona but not the others.
- **Red flags** — anything that alienates more than one persona.
- **Gaps** — something the campaign does not address that several personas care about.

Record the findings as a table — Persona | Reaction | Engage trigger | Turn-off | Verdict — and include it in the strategy or campaign brief alongside the disclosure footnote.

| Persona | Reaction | Engage trigger | Turn-off | Verdict |
|---|---|---|---|---|
| | | | | |

## Validation checklist

Complete before synthetic personas appear in any client-facing strategy. Record each outcome as **Validated**, **Partially validated** or **Unvalidated — assumption retained**.

- [ ] Cross-reference age and income assumptions against Uganda Bureau of Statistics household survey data, or the equivalent national statistics authority for the country (see register UBOS-NSI-2026 for the current UBOS framework; use the named source year).
- [ ] Check platform-usage assumptions against the GSMA *Mobile Economy Sub-Saharan Africa* report, most recent edition (verify before stating; no register record).
- [ ] If the client has a Facebook Page, run Meta Audience Insights for Uganda and compare its age, gender and location breakdowns with the persona assumptions (tool availability: verify at use; no register record).
- [ ] Hold at least one real interview or WhatsApp conversation with a person matching each persona profile; even one conversation per persona adds substantial validation. Recruit with consent (see [persona discipline](persona-discipline.md) § 5).
- [ ] List every assumption that could not be validated and flag it explicitly as a risk in the strategy document.

For each unvalidated assumption add a bracketed risk note in the strategy: *[Assumption: [description]. Validate before campaign launch.]*

## Disclosure standard

Include this footnote verbatim in every client-facing deliverable that uses synthetic personas:

> Audience personas were generated using AI (Claude/ChatGPT) based on secondary data and market knowledge. They represent informed hypotheses, not primary research findings. Assumptions that could not be cross-referenced against secondary data are flagged within the document.

Further rules:

- Never present synthetic personas as "research findings" in a proposal or strategy without the disclosure footnote.
- In presentation decks, put the disclosure in the slide footer or speaker notes of every slide that refers to a persona.
- If the client asks for the disclosure to be removed, explain the professional and reputational risk and decline; if they insist, record the removal in the project file.

## Discipline caveats for synthetic personas

Synthetic personas pass the same discipline gate as research-grounded ones ([persona discipline](persona-discipline.md); summary in [docs/ux-foundations.md](../../../../docs/ux-foundations.md) Section 1). The disclosure above stays in place; these caveats add discipline, not transparency. The source guidance (added 2026-05-04) draws on Branson, S. (2020) *UX/UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*.

- **Stronger "designing for themselves" risk.** AI generation tends to reflect the operator's stated assumptions back. Mitigation: name the persona's pain points before generation, and reject any synthetic persona whose pain points reduce to "agrees with the operator".
- **Essential Persona declaration is mandatory**, even for synthetic work. Pick one persona as the canonical target and document why it was chosen over the others. Never deliver four synthetic personas without naming which is Essential.
- **Edge-case discipline still applies.** Synthetic personas are no licence to design for everyone. The answer "Sorry, but Noah won't need X" holds whether Noah is real or synthetic.

If the output cannot satisfy all three caveats, it is not ready to ship: return to primary research through the parent [SKILL.md](../SKILL.md), or rerun with stronger constraints.

## Release checklist

- [ ] Three distinct personas — primary, secondary and edge — with meaningfully different demographics or use cases.
- [ ] Each persona uses the full output format with every field completed; no field is blank without explanation.
- [ ] Uganda/East Africa calibration applied: income in UGX, platform norms accurate for the target city, language preferences noted.
- [ ] Synthetic focus group run for at least one campaign concept, with the completed analysis table.
- [ ] Validation checklist completed with an explicit outcome for each item.
- [ ] Every unvalidated assumption flagged with a bracketed risk note in the deliverable.
- [ ] Disclosure footnote included verbatim in every client-facing document.
- [ ] At least one secondary data source (UBOS, GSMA, Meta Audience Insights) cross-referenced and cited.
- [ ] Essential Persona declared and the three discipline caveats met.

## Sources

- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn. Stanford University Press.
- Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers*. Harvard Business Review Press.
- Randazzo, G.W. (2024) *Winning Marketing Strategies Using Generative AI*. Business Expert Press.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.
- Branson, S. (2020) *UX/UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience* (discipline caveats; full note in [persona discipline](persona-discipline.md)).

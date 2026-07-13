---
name: ai-synthetic-personas
description: Use when AI Synthetic Personas is needed to produce a AI synthetic personas deliverable for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Synthetic Personas

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **AI synthetic personas deliverable** and the supplied brief falls within ai synthetic personas.

## Do Not Use When
- Use `ai-readiness-diagnostic` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| AI marketing use-case brief, intended human control point and success measure | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified AI synthetic personas deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact AI synthetic personas deliverable, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete AI synthetic personas deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Ai synthetic personas deliverable | Requester, client reviewer or delivery team | The AI synthetic personas deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested AI synthetic personas deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Generate structured audience personas using AI-assisted synthesis when primary research is unavailable. Personas produced by this skill are informed hypotheses grounded in secondary data and East African market knowledge — not primary research findings. Every deliverable produced using this skill must carry the disclosure specified in the Citation Standard section below.

Apply the `east-african-english` skill for tone throughout. For clients who can commission primary research, use `03-audience-personas` instead and return to this skill only for supplementary rapid-validation work.

## Required Input
Ask for the following before generating any personas:

- **Client business name** — the trading name as used publicly
- **Industry** — be specific (e.g. "private healthcare clinic", "SME accounting software", "mid-range restaurant chain")
- **Country / city** — defaults to Kampala, Uganda if not specified; adjust EA norms for Kenya or Tanzania if relevant
- **Target audience description** — age range, income band, location (urban/peri-urban/rural), and any known sub-segments
- **Primary goal** — choose one: strategy development / messaging validation / content planning / campaign targeting
- **Available secondary data** — note any existing research, sales data, customer feedback, or Meta Audience Insights the client can share; state "none available" if there is nothing

## When to Use Synthetic vs Primary Research
### Use synthetic personas when:
- Budget for primary research is unavailable
- The project timeline is under two weeks
- Preliminary hypotheses need rapid validation before commissioning fieldwork
- The client has existing secondary data (sales records, CRM data, website analytics) that can anchor the AI output

### Commission primary research instead when:
- Launching a new product in an unfamiliar market where AI training data is likely thin
- The decision at stake is high-value — above UGX 50 million in campaign or product investment
- There is reason to believe AI training data underrepresents the target audience (e.g. rural low-income segments, elderly populations, niche occupational groups)
- The client has had prior strategy failures that suggest existing assumptions are wrong

### Always:
- Disclose the synthetic origin of personas in all deliverables (see Citation Standard)
- Flag every assumption that could not be cross-referenced against secondary data
- Treat synthetic personas as a starting point, not a conclusion

## Uganda / East Africa Calibration
Apply this demographic and behavioural context when constructing prompts. Adjust for the specific country and city provided by the client.

**Income bands (UGX per month):**

| Band | Monthly Income |
|---|---|
| Low income | Under UGX 500,000 |
| Lower-middle income | UGX 500,000 – 1,500,000 |
| Middle income | UGX 1,500,000 – 5,000,000 |
| Upper-middle income | Above UGX 5,000,000 |

**Platform norms:**

- **WhatsApp** — primary communication channel across all income levels; business enquiries, referrals, and purchase decisions frequently happen via WhatsApp groups and DMs
- **Facebook** — broadest reach; urban and peri-urban, 18–55+, all income levels
- **TikTok** — fast-growing, urban youth 16–30, entertainment-first
- **LinkedIn** — formal sector professionals, NGO workers, senior management, B2B audiences
- **YouTube** — research, tutorials, long-form; consumed when users have Wi-Fi access

**Trust conditions:**

- Word-of-mouth and community recommendations carry high weight; formal advertising is viewed with scepticism by many segments
- Social proof from peers and WhatsApp group endorsements consistently outperforms broadcast advertising
- Localisation — local language, local place names, local events — drives significantly higher engagement than generic international content

**Language:**

- Most urban Ugandans code-switch between English and Luganda; formal communications default to English
- Luganda phrases in captions or CTAs can increase relatability for Kampala-based mass-market audiences
- Kiswahili is the appropriate local language calibration for Kenya and Tanzania

## Structured Prompt Template
Use this prompt to generate one persona. Replace all bracketed placeholders with the client's specific details before running. Run the prompt once per persona.

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

Add the Uganda/EA Calibration data above to the prompt when working on Ugandan clients to anchor the AI output in realistic local context.

## 3-Persona Output Format
Generate three distinct personas per engagement. Do not generate all three using the same demographic profile — vary income, age, or use case meaningfully.

**Primary persona** — the highest-value or most common customer segment; the person the strategy is primarily built around.

**Secondary persona** — the second priority segment; often a different demographic or a distinct use case (e.g. a gifter rather than an end user, or a B2B decision-maker alongside a B2C buyer).

**Edge persona** — a segment the client may be overlooking; often a future growth opportunity, an underserved demographic, or a non-obvious use case. Flag explicitly that this persona represents a growth hypothesis.

### Output structure for each persona:
| Field | Detail |
|---|---|
| **Name** | Realistic EA name (e.g. Harriet, Brian, Fatuma, Ronald, Aisha) |
| **Archetype label** | A specific label for this client's context (e.g. "The Growth-Minded SME Owner") |
| **Day in the Life** | Three sentences: morning, workday, evening — grounded in this persona's specific circumstances |
| **Content preferences** | Two to three specific formats with examples relevant to the client's category |
| **Messaging triggers** | Three specific reasons this persona would engage with or buy from the client |
| **Primary platforms** | The one or two platforms where this persona is most reachable and most likely to act |
| **Key barriers** | Two to three specific obstacles to purchase or engagement |

After the three persona cards, produce a **side-by-side summary table** using the fields above for quick team reference.

## Synthetic Focus Group Technique
Simulate audience reactions to campaign concepts before investing in creative production. Use this technique for messaging validation and campaign brief development.

**Run this prompt for each of the three personas:**

```
You are [Persona Name], a [description — occupation, age, income, location].

The brand [Client Name] is about to launch [campaign concept — one sentence].

Answer the following:
1. What is your first reaction to this campaign?
2. What would make you engage with it (like, comment, share, visit, buy)?
3. What would put you off or make you scroll past?
4. What would you tell a friend about this brand after seeing this campaign?
```

**Analyse the three responses to identify:**

- Universal appeal — elements that matter across all three personas
- Segment-specific messaging — elements that work for one persona but not others
- Red flags — anything that alienates more than one persona
- Gaps — something the campaign does not address that multiple personas care about

Document the synthetic focus group findings as a table: Persona | Reaction | Engage trigger | Turn-off | Verdict. Include this table in the strategy or campaign brief alongside the disclosure footnote.

## Validation Checklist
Complete this checklist before using synthetic personas in any client-facing strategy document. Record the outcome of each check as: Validated / Partially validated / Unvalidated — assumption retained.

- [ ] Cross-reference age and income assumptions against Uganda Bureau of Statistics household survey data or equivalent national statistics authority for the relevant country
- [ ] Check platform usage assumptions against GSMA Mobile Economy Sub-Saharan Africa report (most recent edition)
- [ ] If the client has a Facebook Page, run Meta Audience Insights for Uganda to check age, gender, and location breakdowns against persona assumptions
- [ ] Run at least one real interview or WhatsApp conversation with a person who matches each persona profile — even one conversation per persona adds significant validation
- [ ] Note any assumptions that could not be validated and flag these explicitly as risks in the strategy document

For each unvalidated assumption, add a bracketed risk note in the strategy: *[Assumption: [description]. Validate before campaign launch.]*

## Citation Standard
**In every client-facing deliverable that uses synthetic personas, include the following footnote verbatim:**

> Audience personas were generated using AI (Claude/ChatGPT) based on secondary data and market knowledge. They represent informed hypotheses, not primary research findings. Assumptions that could not be cross-referenced against secondary data are flagged within the document.

**Additional rules:**

- Never present synthetic personas as "research findings" in a proposal or strategy without the disclosure footnote
- In presentation decks, add the disclosure to the slide footer or speaker notes of every slide that references a persona
- If the client requests that the disclosure be removed, explain the professional and reputational risk and decline; if they insist, note the removal in the project file

## Quality Criteria
- Three distinct personas generated — primary, secondary, and edge — with meaningfully different demographics or use cases
- Each persona uses the full structured output format with all fields completed; no field left blank without explanation
- Uganda/EA calibration applied — income expressed in UGX, platform norms accurate for the target city, language preferences noted
- Synthetic focus group run for at least one campaign concept with a completed four-column analysis table
- Validation checklist completed with an explicit outcome recorded for each item
- All unvalidated assumptions flagged with bracketed risk notes in the deliverable
- Citation standard applied — synthetic origin disclosure included verbatim in every client-facing document
- At least one secondary data source (UBOS, GSMA, Meta Audience Insights) cross-referenced and cited

## References
- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn. Stanford University Press.
- Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers*. Harvard Business Review Press.
- Randazzo, G.W. (2024) *Winning Marketing Strategies Using Generative AI*. Business Expert Press.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.

## Persona discipline applied to synthetic (added 2026-05-04 from Branson)
Canonical reference: `docs/ux-foundations.md` Section 1.

Synthetic personas pass the same Branson discipline gate as research-grounded personas. The disclosure already required by this skill stays in place; this section adds discipline, not transparency.

Three caveats specific to AI-generated personas:

- **Stronger "designing for themselves" risk.** AI generation tends to mirror the operator's stated assumptions back at them. **Mitigation:** name the persona's pain points *before* generation; reject any synthetic persona whose pain points reduce to "agrees with the operator."
- **Essential Persona declaration is mandatory** even for synthetic work. Pick one persona as the canonical target; document why it was chosen over the others. Do not produce 4 synthetic personas without naming which is Essential.
- **Edge-case discipline still applies.** Synthetic personas are not licence to design for everyone. The "Sorry, but Noah won't need X" answer holds whether Noah is a real or synthetic persona.

If the synthetic persona output cannot satisfy these three caveats, the deliverable is not ready to ship. Either return to primary research (use `03-audience-personas` instead) or rerun with stronger constraints.

---
name: biz-dev-positioning
description: Use when Business Development — Positioning is needed to produce a positioning statement and proof architecture for social-media or digital-marketing work; use `biz-dev-proposal` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Business Development — Positioning

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **positioning statement and proof architecture** and the supplied brief falls within business development — positioning.

## Do Not Use When
- Use `biz-dev-proposal` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Commercial brief, target buyer, offer, proof and requested next step | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Issue a qualified finding and identify the evidence needed. |

## Capability and Permission Boundaries
Default to read-only: inspect supplied material and report findings. Editing, publishing, contacting people, spending, or changing live systems requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified positioning statement and proof architecture; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Buyer problem, proof strength and commercial objective align | Choose the offer and proof sequence that supports the requested buying decision. | A generic sales asset with unsupported claims or the wrong ask. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact positioning statement and proof architecture, consumer, market, channel and approval boundary; route to `biz-dev-proposal` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete positioning statement and proof architecture; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Positioning statement and proof architecture | Requester, client reviewer or delivery team | The positioning statement and proof architecture addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Finding-to-source register and unassessed-check list | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested positioning statement and proof architecture, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [biz-dev-proposal](../biz-dev-proposal/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## Required Input
Before generating any deliverable, ask for:
- Business name
- Industry / sector
- Country or city (default: Uganda / East Africa)
- Current positioning (how they currently describe themselves, if at all)
- Primary competitor(s) — named or described
- Primary client type they want to attract
- What they most want to be known for

## Part 1 — The Differentiating Promise (USP)
The USP (unique selling proposition, Rosser Reeves) is the one specific thing that sets a business, product or personal brand apart from every alternative the target client could choose.

**Procedure:**
1. List every service or product.
2. Beside each, write the concrete outcomes clients get.
3. Choose the outcome that is both most valuable to the target client and least offered by competitors.
4. Rewrite it in the client's own words, not internal jargon.
5. **Competitor test:** could a direct competitor say the same sentence truthfully? If yes, sharpen it.

**Formula:**
> "We [specific action] for [specific client type] so that [specific outcome] — without [the obstacle or pain competitors leave in place]."

**Example (illustrative):**
- Weak: "We provide social media management services."
- Strong: "We run social media for Ugandan food and beverage brands so their Facebook and WhatsApp communities bring in walk-in customers — without the owner spending an hour a week on content."

## Part 2 — The Short Spoken Pitch
The spoken form of the USP for events, introductions and discovery calls.

**Structure:** what we do + for whom + the result they get + why us. Two or three sentences, under 15 seconds.

**Preparation:** draft from the formula → say it aloud → rewrite until it sounds like conversation, not a brochure → try it at one event and note the questions it prompts.

**Failure checks:** opens with a job title; describes inputs ("we post three times a week") instead of outcomes; too broad ("we help businesses grow"); runs past 20 seconds.

## Part 3 — Defining the Niche
Specialisation is usually the strongest position for an independent firm. A niche must be small enough to reach and lead within the firm's time and budget, and large enough to carry the revenue the firm needs.

**Selection grid** — score each candidate client type:

| Question | Evidence |
|---|---|
| Which clients bring the most revenue per engagement? | Invoices |
| Which clients refer others most? | Referral log |
| Which work do we do best and enjoy most? | Delivery reviews, team view |
| Where is competition thinnest? | Competitor scan |

Choose where the answers overlap.

**Narrow in layers** (illustrative):

| Layer | Example |
|---|---|
| Sector | Healthcare |
| Sub-sector | Private hospitals and clinics |
| Buyer role | Marketing leads in private hospitals |
| Geography | Kampala and Nairobi |
| Outcome | Patient bookings through Facebook and WhatsApp |

A well-defined niche states what it excludes as well as what it includes.

## Part 4 — Mission and Vision
**Mission** — what the firm does, for whom and the value, in the present tense.
Formula: "We [verb] [service or output] for [client type] so that [outcome]."
Example: "We design and run social media strategies for East African SMEs so their online audiences become paying customers."

**Vision** — where the firm is going, specific and dated.
Formula: "To be [position] in [market] by [year]."
Example: "To be the leading social media consultancy for East Africa's food and beverage sector by 2028."

**Checks:** the vision is where the mission leads; both are specific enough to know when they are achieved; plain English; short enough for every staff member to remember.

## Part 5 — Strategic Positioning Checks
Before finalising, test the positioning against five questions (a synthesis of long-standing advice for independent professionals, including Edwards, Edwards and Douglas, 1991):

| Check | Pass condition | If it fails |
|---|---|---|
| Pull | The offer, visibility and delivery are strong enough that clients seek the firm out | Tighten the offer; fix delivery before marketing |
| Focus | The firm is the obvious specialist for one client type and problem | Return to Part 3 |
| Access | Named gatekeepers already trusted by the ideal client are in the plan | Build the gatekeeper list in [playbook-networking](../../playbooks/playbook-networking/SKILL.md) |
| Standing | There is a route to recognised expertise (Part 6) | Choose a preeminence route |
| Marketing craft | The firm uses ordinary tools unusually well — specific, consistent, audience-led — not routine ads and mailings | Rework the channel plan with the audience's evidence |

## Part 6 — Preeminence Routes
For clients, or the consultancy itself, aiming to be seen as the leading expert in their category. Pick one or two routes and commit for 12–36 months; preeminence is an investment, not a campaign.

| Route | Specific actions |
|---|---|
| **Publish** | Monthly newsletter, LinkedIn articles, trade-press column, annual sector report |
| **Speak** | Sector conferences, chamber of commerce events, university guest lectures |
| **Research** | An annual survey of the sector's clients or practitioners, published (consent and data-protection compliant) |
| **Lead** | A leadership role in a trade or professional association, or chairing a conference |
| **Recognise** | A sector award or ranking (for example a customer-service award in Ugandan banking), judged and published transparently |
| **Pioneer** | Be first to name a new problem, trend or method in the category, then own it |

## Part 7 — Deliverables This Skill Can Generate
1. **USP statement** — one or two sentences that pass the competitor test
2. **Short spoken pitch** — natural spoken version of the USP
3. **Niche definition** — sector, sub-sector, buyer role, geography and outcome
4. **Mission statement** — one or two sentences
5. **Vision statement** — one or two sentences
6. **Positioning brief** — one page combining the above for proposals and credentials
7. **Preeminence action plan** — a 12-month visibility programme

## Quality Criteria
Good output from this skill:
1. The USP passes the competitor test — a direct competitor could not say the same sentence
2. The spoken pitch sounds natural aloud, not like marketing copy
3. The niche states what it excludes, not only what it includes
4. The mission has a subject, a verb, a client type and an outcome
5. The vision names a position, a market and a date
6. The preeminence plan names specific publications, events and organisations
7. Content reflects the East African market where relevant

## References
- Edwards, P., Edwards, S. and Douglas, L.C. (1991) *Getting Business to Come to You*. Los Angeles: Tarcher.
- Reeves, R. (1961) *Reality in Advertising*. New York: Knopf. (Origin of the USP concept.)
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.

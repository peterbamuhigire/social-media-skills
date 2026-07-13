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

## Part 1 — The USP (Unique Selling Proposition)
The USP is the one specific thing that distinguishes a business, product, or personal brand from every alternative available to the target client.

*Original concept: Rosser Reeves (1950s). Applied here via Pinskey (1997).*

**The USP development process:**

1. List every service or product the business offers
2. For each service, list the specific, tangible outcomes it delivers to clients
3. Identify the one outcome that is both the most valuable to the target client AND the most differentiated from competitors
4. Express it in the language the ideal client would use — not internal jargon
5. Apply the test: **Could a direct competitor say this exact sentence?** If yes, it is not a USP. Refine.

**The USP formula:**

> "We [specific action] for [specific client type] so that [specific outcome] — without [key obstacle or pain the competition imposes]."

**Examples:**
- Weak: "We provide social media management services."
- Strong: "We manage social media for Ugandan food and beverage brands so that their Facebook and WhatsApp communities generate walk-in customers — without the owner spending a single hour on content."

## Part 2 — The 15-Second Pitch
The spoken version of the USP — used at networking events, in introductions, and in discovery calls.

**Structure:**
> "[What I/we do] + [for whom] + [the specific result they get] + [why us, not someone else]"

**Length:** 2–3 sentences. Delivered in under 15 seconds.

**Preparation process:**
1. Draft the pitch using the USP formula above
2. Say it aloud — does it sound natural, or like a brochure?
3. Revise until it sounds like something you would say in a casual conversation
4. Test it: deliver it at one networking event and note what follow-up questions it triggers

**Common mistakes:**
- Starting with a job title ("I'm a social media manager") — labels, not value
- Describing inputs ("We post three times a week") — outputs are what clients want
- Being too broad ("We help businesses grow") — no differentiation
- Being too long — if it takes more than 20 seconds, it is a sales pitch, not a pitch

## Part 3 — Niche Definition
*"For the self-employed individual, finding a niche is somewhat like establishing job security."* — Edwards, Edwards and Douglas (1991)

The most successful independent service businesses are highly specialised. A niche must be:
- **Small enough** to avoid heavy competition and be reachable within the business's time and budget
- **Large enough** to sustain the revenue the business requires

**Niche definition exercise:**

Answer these four questions:
1. Which type of client produces the most revenue per engagement?
2. Which type of client produces the most referrals?
3. Which type of work do you do best and find most interesting?
4. Where is competition least intense?

The intersection of all four answers is the natural niche.

**Niche levels (from broad to specific):**

| Level | Example |
|---|---|
| Sector | Healthcare |
| Sub-sector | Private hospitals and clinics |
| Role within sub-sector | Marketing teams in private hospitals |
| Geography | Kampala and Nairobi |
| Specific outcome | Patient acquisition through Facebook and WhatsApp |

The more specific, the more powerful the positioning.

## Part 4 — Mission and Vision Statements
**Mission Statement** — what the business does, for whom, and the value it delivers. Present tense. Action-oriented.

Formula: *"We [verb] [specific service or output] for [specific client type] so that [specific outcome]."*

Example: "We design and manage social media strategies for East African SMEs so that their online presence converts audiences into paying customers."

**Vision Statement** — where the business is heading. Future-tense. Aspirational but specific.

Formula: *"To be [specific position] in [specific market] by [specific timeframe]."*

Example: "To be the leading social media consultancy for the food and beverage sector across East Africa by 2028."

**Rules:**
- Mission and vision must be internally consistent — the vision is where the mission leads
- Both must be specific enough that you could describe what achieving them looks like
- Both should be written in plain English — not corporate jargon
- Both must be short enough to be memorised by every person in the business

## Part 5 — The Five Lessons of Successful Independents
*(Edwards, Edwards and Douglas, 1991 — synthesised from research into $100,000+ independent businesses)*

These five principles distinguish the most successful independent service businesses from the rest:

**Lesson 1 — Get people to beat a path to your door**
Build such a strong reputation for delivering a specific result that clients come to you, rather than you chasing them. Requires: a clearly defined offer, consistent visibility, and exceptional delivery.

**Lesson 2 — Establish a niche**
Specialise to the point where you are the obvious expert for a specific type of client with a specific problem. Generalists struggle; specialists dominate.

**Lesson 3 — Gain entrance through gatekeepers**
Identify the professionals and institutions that already have trusted relationships with your ideal clients — and build deliberate relationships with those gatekeepers. See `playbook-networking` for the gatekeeper cultivation process.

**Lesson 4 — Position yourself as preeminent in your field**
Three routes to preeminence:
- Further the knowledge in your field (publish, research, speak, teach)
- Assume a leadership role (association president, conference chair, award creator)
- Pioneer a new approach or methodology (be first, name it, own it)

**Lesson 5 — Become a premier marketeer**
Do not take out run-of-the-mill ads. Do not send customary mailings. Premier marketeers use the same tools as everyone else — but more creatively, more consistently, and with more understanding of what their specific audience responds to.

## Part 6 — Preeminence Strategy
For clients or the consultancy who want to be seen as the leading expert in their category:

| Route | Specific Actions |
|---|---|
| **Publish** | Monthly newsletter, LinkedIn articles, trade press column, annual industry report |
| **Speak** | Industry conferences, Chamber of Commerce events, university guest lectures |
| **Research** | Annual survey of your sector's clients or practitioners; publish the data |
| **Lead** | Volunteer for a leadership role in a trade or professional association |
| **Award** | Create a sector award (e.g., "Best Customer Service in Ugandan Banking") — judge and publish |
| **First** | Be the first to name a new problem, trend, or methodology in your category |

Preeminence is built over 12–36 months. It is an investment, not a campaign.

## Part 7 — Deliverables This Skill Can Generate
1. **USP statement** — one or two sentences, tested against the competitor test
2. **15-second pitch** — natural, spoken version of the USP
3. **Niche definition** — sector, sub-sector, role, geography, and specific outcome
4. **Mission statement** — 1–2 sentences
5. **Vision statement** — 1–2 sentences
6. **Positioning brief** — 1-page document combining all of the above for use in proposals and credentials
7. **Preeminence action plan** — 12-month visibility building programme

## Quality Criteria
Good output from this skill:
1. The USP fails the "competitor test" — a direct competitor could NOT say the same sentence
2. The 15-second pitch sounds natural when spoken aloud — not like marketing copy
3. The niche is specific enough to describe what it excludes, not just what it includes
4. The mission statement contains a subject, a verb, a client type, and an outcome
5. The vision statement names a specific position in a specific market with a specific timeframe
6. The preeminence plan names specific publications, events, and organisations — not generic categories
7. All content reflects the East African market context where relevant

## References
- Edwards, P., Edwards, S. and Douglas, L.C. (1991) *Getting Business to Come to You*. Los Angeles: Tarcher.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.

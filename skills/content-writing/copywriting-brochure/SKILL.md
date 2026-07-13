---
name: copywriting-brochure
description: Use when Copywriting — Brochure is needed to produce a publication-ready copy for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Copywriting — Brochure

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **publication-ready copy** and the supplied brief falls within copywriting — brochure.

## Do Not Use When
- Use `caption-writer` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Content brief, channel, audience, message, format and call to action | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified publication-ready copy; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Channel, format and audience commitment level are known | Choose the hook, structure and call to action native to that context. | Copy that could be pasted unchanged onto any channel or brand. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact publication-ready copy, consumer, market, channel and approval boundary; route to `caption-writer` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete publication-ready copy; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Publication-ready copy | Requester, client reviewer or delivery team | The publication-ready copy addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested publication-ready copy, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [caption-writer](../caption-writer/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## Required Input
Before generating any deliverable, ask for:
- Client business name
- Industry / sector
- Country or city (default: Uganda / East Africa)
- Purpose of the brochure (what should the reader do after reading it?)
- Target audience (who will receive this brochure and in what context?)
- Format (trifold, A4 booklet, digital PDF, etc.)
- Services or products to be featured
- Any existing testimonials, case studies, or statistics available

## Part 1 — Purpose Before Writing
Define the single purpose of the brochure before writing a word.

**Ask:** What is the one action the reader should take after reading this?

| Answer | How It Changes the Copy |
|---|---|
| Call us for a consultation | Lead with the problem and the transformation; end with the call |
| Visit our website | Build curiosity — give enough to compel a visit, not enough to satisfy it |
| Approve us as a supplier | Lead with credentials, case studies, and proof |
| Buy at the point of sale | Lead with the offer and price — transactional, immediate |
| Refer us to someone else | Make it easy to understand who benefits and why |

If the client cannot define a single action, help them choose one. A brochure trying to do five things does none of them.

## Part 2 — The Eight Imprints Rule
*Adapted from Pinskey (1997)*

A prospect typically needs to encounter a brand or business name **eight times** before they will act.

The brochure is one imprint. It does not work as a standalone piece — it must be part of a system:
- Meeting (imprint 1) → Business card (2) → Brochure (3) → Follow-up email (4) → Article or post seen online (5) → Referral conversation (6) → Proposal (7) → Second meeting (8)

**Implication:** Design brochure copy to move the prospect to the *next step*, not to close the sale. The brochure's job is not to sell — it is to maintain and deepen interest.

## Part 3 — The Eight Elements Every Brochure Must Contain
1. **A headline that states the primary benefit** — not the company name, not the service category
2. **A clear description of who you serve** — the reader must immediately recognise themselves
3. **The problem you solve** — stated in the reader's language, not the business's
4. **Your solution (services)** — described in terms of outcomes, not processes
5. **Proof** — at least one testimonial, case result, or named client reference
6. **A clear call to action** — the single next step, stated explicitly
7. **Contact details** — minimum two channels (phone + email or WhatsApp)
8. **A reason to act now (if applicable)** — a deadline, limited availability, or bonus offer

## Part 4 — Features vs Benefits
*"Features instruct. Benefits sell."* — Hahn (2003)

Every service or product listed in the brochure must be translated from feature to benefit before it appears in copy.

**The translation process:**
- Feature: "We post 12 times per month across three platforms."
- Benefit: "Your brand stays in front of your audience every three days — without you lifting a finger."

**The test:** After every claim, ask: "So what does that mean for the reader?" The answer is the benefit.

**In a brochure, features are supporting evidence. Benefits are the message.**

## Part 5 — The Biggest Brochure Mistakes
1. **Leading with the company name and history** — the reader does not care yet; earn their interest first
2. **Featuring the company, not the client's outcomes** — "We were founded in 2015 and have 12 staff" is not a benefit
3. **No call to action** — a brochure without a next step is a pamphlet
4. **Listing services without outcomes** — "Social Media Management" tells the reader nothing; "More enquiries, more sales" tells them everything
5. **Jargon and industry terms** — write for the reader, not for peers
6. **No testimonials or proof** — claims without evidence are ignored
7. **Burying the headline** — the cover must state the most powerful benefit, not just the business name
8. **Trying to include everything** — a brochure with 12 services and 6 sections is unread

## Part 6 — Panel-by-Panel Structure (Trifold)
For a standard trifold brochure:

| Panel | Position | Content |
|---|---|---|
| **Cover** | Outside front | Headline (primary benefit) + business name + visual. Nothing else. |
| **Back** | Outside back | Contact details + brief boilerplate + secondary CTA |
| **Inside left** | First seen on opening | The problem — stated in the reader's language |
| **Inside centre** | Central panel | The solution — your services, outcome-led |
| **Inside right** | Third inside panel | Proof — testimonials, case results, credentials |
| **Back left flap** | Inside back | Call to action + contact details repeated |

**Rule:** Design the cover as the most powerful panel. It is the only panel the prospect sees if they are not yet interested.

## Part 7 — Design Instructions to Include
When briefing a designer, include these content-level design notes:

- Maximum two font families
- Body copy minimum 10pt for print; 14px for digital
- White space is deliberate — do not fill it with more copy or decorative elements
- Photography must show real results, real environments, or real clients — not generic stock
- Every image must serve a specific purpose (illustrate a benefit, provide social proof, or convey scale)
- The call to action must be visually distinct — boxed, coloured, or enlarged
- Separate editorial decisions from design decisions: write the full copy first, then brief the designer

## Quality Criteria
Good output from this skill:
1. The brochure has a single, clearly defined purpose and a single call to action
2. The cover headline states a primary benefit — not the company name alone
3. Every service is described in terms of outcomes, not processes or inputs
4. At least one proof element (testimonial, case result, statistic) appears inside
5. The copy avoids the eight most common brochure mistakes listed above
6. The panel-by-panel structure follows a logical journey from problem to solution to proof to action
7. All copy is written in British English using the register defined in `east-african-english`

## References
- Hahn, F.E. (2003) *Do-It-Yourself Advertising and Promotion*, 3rd edn. Hoboken: Wiley.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.
- `premium-commercial-writing/SKILL.md` - companion layer for premium value, proof, offer framing, and sales-collateral polish.

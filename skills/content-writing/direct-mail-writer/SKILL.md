---
name: direct-mail-writer
description: Use when Direct Mail Writer is needed to produce a publication-ready copy for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Direct Mail Writer

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **publication-ready copy** and the supplied brief falls within direct mail writer.

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
- The specific offer being made (product, service, free consultation, etc.)
- The target audience (existing customers, prospects, a specific segment)
- The desired response action (phone call, website visit, WhatsApp message, in-store visit)
- Budget context (affects format recommendations)

## Part 1 — The Four Prerequisites
Before writing a word of copy, confirm all four conditions are met:
*(Adapted from Edwards, Edwards and Douglas, 1991)*

| # | Prerequisite | What to Verify |
|---|---|---|
| 1 | **The right list** | Is the audience targeted, current, and relevant? A mediocre piece to a great list outperforms a great piece to a poor list. |
| 2 | **The right offer** | Is the offer clear, compelling, and risk-reducing? A weak offer cannot be rescued by strong copy. |
| 3 | **The right copy** | Is the message benefit-led, action-oriented, and reader-focused? |
| 4 | **The right timing** | Does the mailing align with seasonal need, budget cycles, or purchasing windows? |

If any prerequisite is absent, resolve it before proceeding to copy.

## Part 2 — The Two-List Pre-Writing Process
Before writing, build two lists:

**List 1 — Features**
Every factual attribute of the product or service.

**List 2 — Benefits**
For each feature, ask: "What does this mean to the specific reader receiving this letter?"

Write the letter from **List 2 only**. Use List 1 as supporting evidence, never as the lead.

*"Features instruct. Benefits sell."* — Hahn (2003)

## Part 3 — The Three Tells
Every direct mail letter must address three questions — in the first paragraph AND again in the P.S.:

1. **What** are you offering?
2. **Why** should they want it?
3. **How** do they get it? (the response mechanism)

If any of the three is absent, the letter is incomplete.

## Part 4 — Letter Structure
    [HEADLINE or opening hook — strongest benefit or most important fact]

    [Opening paragraph: State the problem the reader has. Paint it vividly.
    Then pivot: "There is a solution."]

    [Second paragraph: Introduce the offer. State it clearly. Lead with the outcome,
    not the features. Use specifics — not "great results" but "34% more enquiries
    in the first month."]

    [Third paragraph: Build credibility. Testimonial, case study, statistic,
    or credential. One proof point is enough here; more can follow.]

    [Fourth paragraph: Address the most likely objection. Do not wait for the reader
    to think it — raise it and answer it.]

    [Fifth paragraph: The offer in full. State exactly what they receive, what they
    pay (or don't pay), and any time limitation or bonus.]

    [Closing paragraph: The call to action. Exact next step. Make it frictionless.
    State the deadline if applicable.]

    [Signature — handwritten name, full title]

    [P.S. — Restate the single strongest benefit and the call to action.
    The P.S. is the second-most-read element after the headline. Never waste it.]

## Part 5 — The 27 Copywriting Points
See `references/galletti-27-points.md` for the full Galletti checklist. Apply before finalising any copy.

**The five most critical points:**
1. Move the best, most powerful thing you can say to the very beginning
2. Write to one specific person — not "our valued customers"
3. Use "you" and "your" far more than "I," "we," or "our"
4. Make the offer risk-free — a guarantee, a trial, or a free first step
5. Test the headline before anything else — if the headline fails, nothing else matters

## Part 6 — List Strategy and the FRAT Formula
When advising on mailing lists, apply the FRAT formula to prioritise who to contact first:
*(Adapted from Hahn, 2003)*

| Letter | Factor | Question |
|---|---|---|
| F | **Frequency** | How often has this contact bought or enquired? |
| R | **Recency** | How recently did they buy or enquire? |
| A | **Amount** | What is their average transaction value? |
| T | **Type** | What type of products or services do they purchase? |

Score each contact on all four criteria. Mail the highest-FRAT contacts first, most often, and with the most premium formats.

**For rented or purchased lists:**
- Require recency of contact within 90 days
- Match list demographics to the offer's target buyer
- Test with a small cell (minimum 500 pieces) before rolling out

## Part 7 — Budget Viability — The $20 Rule
*(Hahn, 2003)*

Before committing to a mailing programme:

> For every UGX 20,000 (or USD $20) of projected revenue per transaction, the client can reasonably invest up to UGX 1,000 (or USD $1) per piece in mailing costs.

If projected revenue per transaction is UGX 100,000 → affordable cost per piece = UGX 5,000.
If projected revenue per transaction is UGX 500,000 → affordable cost per piece = UGX 25,000.

Use this to guide format decisions: a UGX 5,000 budget points to a postcard or simple letter; UGX 25,000 allows for a folded brochure insert.

## Part 8 — Format Options
| Format | Best For | Cost Tier |
|---|---|---|
| Single A4 letter | Professional services, B2B offers, relationship selling | Low |
| Postcard (A5) | Event invitations, short offers, reminders | Low |
| Letter + insert | Product launches, complex offers with supporting evidence | Medium |
| Self-mailer (folded brochure) | Retail promotions, multiple products | Medium |
| Email (cold or warm list) | Digital-first audiences; fastest test vehicle | Very low |
| WhatsApp broadcast | Known contacts only; EA primary channel | Very low |

## Part 9 — Testing Methodology
- **Test one variable at a time only** — headline vs headline, offer vs offer, list A vs list B
- **Minimum test size:** 500 pieces per cell for digital; 2,000+ for print
- **Code every response mechanism:** different phone number, URL parameter, promo code, or reply address per test cell
- **Track:** response rate, cost per response, conversion rate, revenue per piece mailed
- **Never roll out without a test** — even a 50-piece email test beats no data

## Quality Criteria
Good output from this skill:
1. Copy leads with the strongest benefit — never the company name or "We are pleased to offer…"
2. The Three Tells appear in both the opening paragraph and the P.S.
3. "You" and "your" outnumber "we," "our," and "I" throughout the letter
4. The offer is specific and risk-reducing — not vague
5. At least one proof point (testimonial, statistic, case reference) appears in the letter
6. The call to action is a single, unambiguous instruction with a response mechanism
7. The P.S. restates the strongest benefit and the call to action
8. The $20 Rule has been checked before recommending any format

## References
- Hahn, F.E. (2003) *Do-It-Yourself Advertising and Promotion*, 3rd edn. Hoboken: Wiley.
- Edwards, P., Edwards, S. and Douglas, L.C. (1991) *Getting Business to Come to You*. Los Angeles: Tarcher.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.

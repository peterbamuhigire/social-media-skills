---
name: biz-dev-proposal
description: Use when Service Proposal and Statement of Work Generator is needed to produce a client proposal for social-media or digital-marketing work; use `biz-dev-positioning` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Service Proposal and Statement of Work Generator

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **client proposal** and the supplied brief falls within service proposal and statement of work generator.

## Do Not Use When
- Use `biz-dev-positioning` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Commercial brief, target buyer, offer, proof and requested next step | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified client proposal; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Buyer problem, proof strength and commercial objective align | Choose the offer and proof sequence that supports the requested buying decision. | A generic sales asset with unsupported claims or the wrong ask. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact client proposal, consumer, market, channel and approval boundary; route to `biz-dev-positioning` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete client proposal; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Client proposal | Requester, client reviewer or delivery team | The client proposal addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested client proposal, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [biz-dev-positioning](../biz-dev-positioning/SKILL.md) is the nearest routing comparison for this skill.
- [Agency client acquisition system](references/agency-client-acquisition-system.md) — read for assets, outreach plays, the consultative sale and proposal follow-up.
- [Lawful prospecting and outreach](../biz-dev-lawful-prospecting-outreach/SKILL.md) — required for any list building or cold outreach.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Produce a complete, professional proposal document. Output must be polished enough to send directly to a client. Apply East African English throughout. Structure the document so sections flow logically from context to commitment.

## Required Input
Ask for the following before generating:

- **Consultant/agency name** — who is issuing the proposal
- **Client name and industry** — company name and sector
- **Client contact name and title** — the person the proposal is addressed to
- **Client's stated goals** — what the client said they want to achieve (quote directly where possible)
- **Scope discussed** — what services or activities were discussed; include any specifics raised in the discovery conversation
- **Timeline** — proposed start date, duration, key milestones if known
- **Pricing** — agreed figures, or ranges to propose; specify currency (default: UGX with USD equivalent)
- **Country/city** — defaults to Kampala, Uganda

If pricing has not been agreed, generate a tiered investment table (see Section 7). If timeline is vague, use placeholder weeks (e.g., "Week 1–2: Discovery").

## Document Structure
Generate all nine sections in order. Each section is clearly headed. Do not omit any section.

### 1. Cover Letter
Format as a formal business letter. Include:
- Letterhead line: [Agency Name] | [City] | [Date in day-month-year format]
- Recipient: [Client Contact Name, Title, Company Name]
- Opening: "Dear [Title/Name],"
- Body (3 paragraphs):
  - Paragraph 1: Thank the client for the conversation and confirm the purpose of the proposal.
  - Paragraph 2: Briefly restate the client's situation and what the proposal addresses.
  - Paragraph 3: Warm close — invite them to discuss further, provide contact details.
- Closing: "Yours sincerely," followed by consultant name and title.

Tone: warm but professional. Not sales-heavy. The letter should feel like it was written by a person, not generated.

### 2. Executive Summary
3–4 sentences. State:
- What the engagement is
- What the client will receive
- What outcome is expected
- When it begins

Write this as a standalone paragraph a senior decision-maker could read in 30 seconds to understand the full engagement.

### 3. Understanding of the Client's Situation
Demonstrate that the consultant has listened. Include:
- The client's current situation (2–3 sentences)
- The specific challenges or gaps identified (2–3 bullet points)
- The goals the client expressed (restate in the client's own language where possible)

Do not pad this section with generic industry observations. Use only what the client provided.

### 4. Recommended Scope of Work
Structure in phases where the engagement is complex or multi-month. For each phase:

**Phase [N]: [Phase Name]** (e.g., "Phase 1: Discovery and Strategy")
- Duration: [e.g., Weeks 1–3]
- Activities: [bulleted list of what will be done]
- Output: [what the client receives at the end of this phase]

If the engagement is straightforward, a single-phase scope is acceptable.

### 5. Deliverables List
Bullet list. Each deliverable has:
- **[Deliverable name]** — one sentence describing exactly what it is and what format it takes.

Be specific. "Social media strategy document" is acceptable. "Strategy" is not. Include report formats, content volumes, meeting cadences, and any tangible documents.

### 6. Timeline and Milestones
Present as a table:

| Milestone | Deliverable | Week |
|---|---|---|
| [Milestone name] | [What is delivered] | [Week number or date] |

Include at least 4 rows. If the timeline is unknown, use relative weeks (Week 1, Week 2, etc.).

### 7. Investment
Present as a pricing table with 2–3 options where appropriate. Use tier names relevant to the engagement:
- For retainers: **Starter / Growth / Premium**
- For projects: **Basic / Full / Comprehensive**
- If only one price was agreed, present as a single table with line items.

Table format:

| Package | What's Included | Monthly Investment |
|---|---|---|
| [Tier name] | [Bullet summary] | [UGX X,XXX,XXX (approx. USD X,XXX)] |

Below the table, note: "Pricing is quoted in Ugandan Shillings. USD equivalent is indicative based on prevailing exchange rates and may vary."

If a one-off project: use a line-item cost breakdown instead of tiers.

### 8. Terms and Conditions
Insert the following placeholder block exactly:

*Standard terms apply — insert agency T&Cs here.*

*Key terms typically covered: payment schedule (50% on signing, 50% on completion or monthly in advance for retainers), revision rounds, intellectual property assignment, confidentiality, notice period for retainer termination (typically 30 days in writing).*

Note to consultant: Replace this section with your signed standard terms before sending.

### 9. Next Steps
Include:
- A numbered list of 3–4 specific next steps (e.g., "1. Review this proposal and share any questions by [date].")
- A proposed decision deadline (e.g., "Kindly confirm acceptance by [date] to secure the proposed start date.")
- Contact details for questions.

Tone: clear, specific, professional. Not pushy.

## Formatting Rules
- Use markdown headings (##, ###) for all sections
- Tables must be properly formatted markdown tables
- Dates in day-month-year format (e.g., 17 March 2026)
- Currency: UGX first, USD in brackets. Do not use $ symbol alone.
- British English throughout
- Cover letter in full prose; remaining sections use a mix of prose and structured lists

## Proposal Strengthening Frameworks
### Kahan's Marketing Agency Scorecard (Kahan, 2022)
Kahan's scorecard evaluates agencies across six dimensions. Apply this as a self-assessment lens before writing any proposal — document how the consultancy scores on each dimension and what evidence supports the score.

| Dimension | Self-Assessment Question | Evidence to Include in Proposal |
|---|---|---|
| Digital demand generation expertise | Do we understand how to generate measurable leads and revenue through digital channels? | Case study results showing inquiry volumes and conversion rates |
| Knowledge of the client's business | Have we demonstrated genuine understanding of their industry, competitors, and customers? | Section 3 — Understanding the Client's Situation |
| Campaign planning for all audience segments | Can we reach every relevant segment, not just the easiest one? | Persona references from 03-audience-personas |
| Campaign planning for all prospect touchpoints | Do we cover the full buyer journey, not just awareness? | Scope of work covering awareness through conversion |
| Provable revenue contribution | Can we show that prior work generated revenue, not just impressions? | Specific results with currency values or percentage uplifts |
| Agency integrity | Do we keep commitments, communicate proactively, and act in the client's interest? | Testimonials that speak to process, not just outcomes |

### Social Proof Taxonomy (Bly, 2018)
Every proposal should incorporate multiple social proof sources. Multiple sources outperform a single strong testimonial. Include the following in every proposal where evidence exists:

- **Named client testimonials** — include name, organisation, and specific outcome ("Since working with [Agency], our WhatsApp enquiries increased from 12 to 40 per month — David Ochieng, Ochieng Tiles")
- **Specific measurable results** — numbers, percentages, currency values from prior engagements
- **Crowd proof** — total number of clients served, total campaigns run, years in business
- **Expert endorsements** — referrals from recognised professionals, media mentions, speaking engagements
- **Certification badges** — professional memberships, platform certifications, industry affiliations

### The Free Diagnostic Offer (Bly, 2018)
Including a lead magnet equivalent in a proposal — a free social media audit, a free campaign diagnostic, a free content gap analysis — reduces the commitment threshold and increases proposal conversion rate. As the default proposal close, offer: "If you are not yet ready to proceed with the full engagement, we can begin with a complimentary [30-minute social media audit / content gap review / platform performance diagnostic] at no charge and with no obligation. This gives you a concrete sample of our thinking before any commitment is required."

Use the free diagnostic to demonstrate analytical depth, build trust, and surface client-specific problems that make the full proposal more compelling on follow-up.

## Client Acquisition Frameworks

Detailed procedures, scripts and the corrected Nelson material are in [`references/agency-client-acquisition-system.md`](references/agency-client-acquisition-system.md); read it when the proposal depends on how the prospect was sourced, qualified or will be followed up. List building and cold outreach must follow [`biz-dev-lawful-prospecting-outreach`](../biz-dev-lawful-prospecting-outreach/SKILL.md). Summary:

- **Positioning assets before pitching (Nelson, 2019):** at minimum verified case studies, one niche guide and a niche-specific page. Build the keynote first; other assets derive from it.
- **Three outreach plays (Nelson, 2019):** "Can you handle an additional X this month?" (lead with the niche's highest-value job), "One company in your area" (only where territorial exclusivity is a real, enforced policy) and "Content offer" (deliver the guide by phone). Nelson's volumes and close rates are one practitioner's 2019 US experience, not benchmarks.
- **Four-step consultative sale:** short first call that books a review → pre-meeting research → review meeting (praise first, then gaps, then the solution narrative) → ask, with a decide-by date.
- **Offer presentation order:** problem → its cost to the client's profit → the solution → price. Exception: if size signals show the prospect probably cannot afford the programme, state the range early ("our programmes run from [UGX X] to [UGX Y] a month; is that within range?").
- **The proposal is a follow-up, not the close:** before sending, book a walk-through meeting and agree a decide-by date. Present two or three options and use a choice close ("Which of these two fits you better?").
- **No manufactured urgency:** a capacity or exclusivity deadline appears only when it is true and documented.

### Hell Yes or Hell No Principle (Wardrope, 2024)
Do not pursue lukewarm prospects. A client who requires extensive convincing is likely to be a high-maintenance, low-margin relationship that drains delivery capacity.

**Qualifying criteria — accept only if all three apply:**
1. The prospect clearly understands and acknowledges the problem you are solving
2. The prospect is ready to invest at or above the minimum viable retainer level
3. The prospect respects the agency's process and does not demand unreasonable customisation before signing

Reject any prospect who fails on criterion 2 or 3. Freeing that capacity for the right client generates more revenue and better work.

## Persuasion Frameworks
Apply frameworks from `references/proposal-frameworks.md` when generating this proposal.

Key principles for service proposals:
- Open with the client's problem — never the agency's history, credentials, or service menu (Sant: Primacy Principle)
- Structure the document as Need → Outcome → Solution → Evidence — not Introduction → Features → Price (Sant: NOSE)
- The executive summary must pass the client-name test: the client's name appears 2–3× more than the agency's name (Sant)
- Eliminate Fluff, Guff, Geek, and Weasel from every draft before sending — read the document as if you are the client (Sant)
- The proposal document itself is physical evidence of service quality — formatting, precision, and correct spelling signal professional delivery standards (Hatton: Competitive Advantage Equation)
- Apply Go/No-Go criteria before investing time in a full proposal — a proposal written for the wrong client wastes capacity that belongs to the right one (Hatton)

Read `references/proposal-frameworks.md` for the full NOSE structure, Seven Magic Questions, and Persuasion Sandwich guide.

## Quality Criteria
- Cover letter reads as a genuine, professionally written letter — not a template with fields swapped
- Executive summary can stand alone as a complete description of the engagement
- Scope of work is specific enough that both parties know exactly what is and is not included
- Deliverables list contains no vague items — every deliverable is named and described
- Timeline table has at least 4 milestones with realistic sequencing
- Investment table is clearly formatted with UGX pricing and USD equivalent noted
- T&Cs section includes the standard placeholder exactly as specified
- Next steps are actionable, dated where possible, and include a clear decision prompt
- When generating a proposal for a high-value prospect, verify that at least 3 of the 9 Positioning Assets (Nelson, 2019) exist before sending — name them in the Notes to Consultant section
- The proposal walk-through meeting and decide-by date are booked before the document is sent; any scarcity or exclusivity statement is true and documented

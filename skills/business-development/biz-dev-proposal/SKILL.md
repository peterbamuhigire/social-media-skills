---
name: biz-dev-proposal
description: Use when a prospect has shared a brief or had a discovery call and wants to know what you will do, by when and for how much; produces a send-ready service proposal and statement of work with scope, deliverables, timeline, investment and terms; not for a general agency profile (use `biz-dev-credentials`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Service Proposal and Statement of Work Generator

Turns a discovery call or brief into a send-ready proposal and statement of work in nine sections, from cover letter to next steps, priced in UGX with a USD equivalent by default. The proposal is a follow-up to a booked walk-through, not the close.

<!-- dual-compat-start -->
## Use When
- A prospect liked the discovery call and wants a written proposal for social media or digital marketing work.
- We need a statement of work that fixes scope, deliverables, timeline, milestones and payment terms before we start.
- A retainer renewal or upsell needs a fresh scope and investment section.
- Our proposals go unanswered and we want a sharper executive summary, stronger proof, clear next steps and a follow-up plan.

## Do Not Use When
- `biz-dev-credentials` for an agency profile or case studies sent before any brief.
- `biz-dev-pricing-menu` for the standard packages and rates the proposal quotes from.
- `biz-dev-lawful-prospecting-outreach` for finding and contacting prospects before a brief exists.
- Stop before inventing client facts, prices or terms the agency has not confirmed; formal government or donor tenders and EOIs go to the proposal-skills engine.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Consultant or agency name; client name, industry, contact name and title | Consultant; discovery notes | Yes | Ask; never address a proposal to an unnamed contact. |
| Client's stated goals, quoted directly where possible | Discovery call notes or brief | Yes | Stop; the Understanding section may use only what the client provided. |
| Scope discussed, with specifics raised in discovery | Discovery notes | Yes | Ask; do not pad scope with generic services. |
| Timeline: start date, duration, known milestones | Client or consultant | Yes | Use placeholder relative weeks (for example "Week 1–2: Discovery"). |
| Pricing: agreed figures or ranges, and currency | Consultant; `biz-dev-pricing-menu` | Yes | Generate a tiered investment table; currency defaults to UGX with USD equivalent. |
| Country/city | Consultant | Yes | Default to Kampala, Uganda. |

## Workflow

1. Qualify before writing: apply Hell Yes or Hell No (Wardrope, 2024) and Hatton's Go/No-Go criteria; stop and decline to write a full proposal for a prospect who fails criterion 2 or 3.
2. Ask the intake questions in the [build method](references/proposal-build-method.md#required-input); stop until the goals, scope and contact are known.
3. Score the consultancy on Kahan's six-dimension scorecard and gather social proof (Bly, 2018); check that at least 3 of the 9 Positioning Assets (Nelson, 2019) exist for a high-value prospect.
4. Write all nine sections in order (cover letter, executive summary, understanding, scope, deliverables, timeline, investment, terms, next steps), structured as Need → Outcome → Solution → Evidence and opening with the client's problem.
5. Add the free diagnostic offer as the default close and two or three options for a choice close.
6. Read the draft as the client: run the client-name test and the Fluff/Guff/Geek/Weasel Test, then correct each failing passage and rerun both tests.
7. Book the walk-through meeting and agree a decide-by date before sending; run the `anti-ai-slop` ship gate and hand the proposal over for the consultant's approval to send.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Nine-section proposal and statement of work | Client contact and decision-maker | All nine sections present in order; dates in day-month-year form; UGX first, USD in brackets. |
| Investment table (tiers or line items) | Client decision-maker | Starter / Growth / Premium for retainers or Basic / Full / Comprehensive for projects; exchange-rate note below. |
| Notes to Consultant | Consultant | Names the Positioning Assets verified, open placeholders and the booked walk-through and decide-by date. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Qualification record | Hell Yes or Hell No and Go/No-Go checklist | All three Wardrope criteria answered before drafting. |
| Kahan scorecard self-assessment | Six-row table with evidence | Each dimension scored with the evidence the proposal will cite. |
| Proof and claim log | Table: claim, source, consent | Every testimonial, result and badge traces to a record; scarcity or exclusivity statements are documented. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Sending the proposal and committing to prices or terms needs the consultant's approval; formal government or donor tenders and EOIs route to the proposal-skills engine.

## Degraded Mode

Without the client's stated goals and agreed scope, return the narrowest qualified result and mark the affected checks `not assessed`. A proposal skeleton with the cover letter, placeholder timeline, tiered investment table and terms placeholder can still be delivered for completion after discovery.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Pricing has not been agreed | Generate a tiered investment table with 2–3 options. | A single take-it-or-leave-it price. |
| The engagement is a one-off project | Use a line-item cost breakdown instead of tiers. | Retainer tiers that do not fit the work. |
| The timeline is vague | Use relative weeks (Week 1, Week 2) with at least 4 milestone rows. | Invented dates the agency cannot keep. |
| Size signals show the prospect probably cannot afford the programme | State the range early ("our programmes run from [UGX X] to [UGX Y] a month; is that within range?"); otherwise go problem → cost to profit → solution → price. | A full proposal for a buyer who cannot pay. |
| A prospect fails Wardrope criterion 2 (investment) or 3 (respects the process) | Reject; free the capacity for the right client. | A high-maintenance, low-margin relationship. |
| The prospect is not ready for the full engagement | Offer the complimentary diagnostic (30-minute social media audit, content gap review or platform performance diagnostic) with no obligation (Bly, 2018). | Losing a warm prospect at the commitment threshold. |
| A capacity or exclusivity deadline is proposed | Use it only when true and documented. | Manufactured urgency. |
| The proposal depends on list building or cold outreach | Route through `biz-dev-lawful-prospecting-outreach` first. | Contacting prospects without a lawful basis. |

## Quality Standards

- Executive summary can stand alone as a complete description of the engagement.
- Scope of work is specific enough that both parties know exactly what is and is not included.
- Deliverables list contains no vague items; every deliverable is named and described.
- Timeline table has at least 4 milestones with realistic sequencing.
- Investment table is clearly formatted with UGX pricing and USD equivalent noted.
- Next steps are actionable, dated where possible, and include a clear decision prompt.
- When generating a proposal for a high-value prospect, verify that at least 3 of the 9 Positioning Assets (Nelson, 2019) exist before sending; name them in the Notes to Consultant section.
- The proposal walk-through meeting and decide-by date are booked before the document is sent; any scarcity or exclusivity statement is true and documented.

Two more release checks (cover letter, T&Cs placeholder) are in the [build method](references/proposal-build-method.md#additional-release-checks).

## Anti-Patterns

- Opening with the agency's history, credentials or service menu. Fix: open with the client's problem (Sant: Primacy Principle).
- Structuring as Introduction → Features → Price. Fix: Need → Outcome → Solution → Evidence (Sant: NOSE).
- The agency's name outnumbering the client's in the executive summary. Fix: the client's name appears 2–3× more than the agency's (Sant).
- Padding the Understanding section with generic industry observations. Fix: use only what the client provided, in their own language.
- Treating the sent proposal as the close. Fix: book the walk-through, present two or three options and use a choice close.
- Quoting Nelson's volumes and close rates as benchmarks. Fix: treat them as one practitioner's 2019 US experience.
- Sloppy formatting or spelling. Fix: the proposal is physical evidence of service quality (Hatton: Competitive Advantage Equation); proofread before sending.

## References

- [Proposal build method](references/proposal-build-method.md): read when writing the nine sections, applying the formatting rules, Kahan's scorecard, the social proof taxonomy, the free diagnostic offer, the client acquisition summary, Hell Yes or Hell No or the persuasion principles.
- [Proposal frameworks](references/proposal-frameworks.md): read when applying NOSE, the Seven Magic Questions, the Persuasion Sandwich or Go/No-Go criteria.
- [Agency client acquisition system](references/agency-client-acquisition-system.md): read for assets, outreach plays, the consultative sale and proposal follow-up.
- [`biz-dev-lawful-prospecting-outreach`](../biz-dev-lawful-prospecting-outreach/SKILL.md): read before any list building or cold outreach.
- [`biz-dev-pricing-menu`](../biz-dev-pricing-menu/SKILL.md): read when the standard packages and rates are needed.
- [`biz-dev-positioning`](../biz-dev-positioning/SKILL.md): read when the niche and promise behind the proposal are unsettled.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the cover letter and executive summary.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

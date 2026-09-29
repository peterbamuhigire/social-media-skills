---
name: ai-readiness-diagnostic
description: Use when a client asks how ready they are for AI in marketing, or their customer data is too messy for AI; produces a scored 41-item readiness diagnostic, a data foundation audit and 90-day plan with Uganda DPPA 2019 consent, and an AI Marketing Canvas roadmap; not for choosing which tasks AI should do (use `ai-use-case-mapping`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Readiness Diagnostic

Scores a client's AI marketing maturity across five domains with 41 yes/no items, places them on a step of the AI Marketing Canvas (Venkatesan and Lecinski, 2026) and gives a prioritised 90-day plan a non-technical business owner can act on.

<!-- dual-compat-start -->
## Use When
- Are we ready for AI? Score our marketing maturity across data, team, tools and processes before we buy anything.
- Our customer data sits in WhatsApp chats, Facebook DMs, Excel sheets and an old CRM; run the hygiene checklist and a 30-day clean-up plan before connecting AI tools.
- A larger client needs a 90-day data foundation plan: data asset inventory, quality scorecard, minimum viable customer schema and Uganda Data Protection and Privacy Act 2019 consent.
- Complete the AI Marketing Canvas across acquisition, retention, growth and advocacy and turn it into a 12-month quarterly AI roadmap.

## Do Not Use When
- `ai-use-case-mapping` for deciding which marketing tasks AI should take on and in what order.
- `meta-tools-stack-evaluation` for comparing and scoring specific AI tools or vendors.
- `training-ai-foundations` for teaching the team to use AI.
- Stop before any AI tool is connected to customer data that lacks a lawful basis, consent or an accountable owner; deliver the remediation plan instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry, country/city, primary marketing goal and marketing team size | Client or approved brief | Yes | Ask before starting; default the location to Uganda/East Africa only when it is not stated. |
| Answers to all 41 diagnostic questions, recorded Y or N | Walk-through with the client | Yes | Where the client is genuinely uncertain, record N and note it for follow-up; never skip or estimate an item without a recorded reason. |
| The client's answer to "Which wave best describes your current AI marketing activity?" | Client | Conditional | Infer the wave from the AI Deployment answers and label it an inference. |
| Customer-data sources, owners and consent records | Client CRM, spreadsheets, WhatsApp and Facebook exports | Conditional (Data Foundation 0–3 or a data audit request) | Deliver the hygiene checklist as questions and mark consent and lawful basis `not assessed`. |
| Tool budget, payment options and current subscriptions | Client finance or marketing lead | Conditional | Recommend free tiers only and flag any paid tool as unpriced. |

## Workflow

1. Confirm the business profile and the decision the diagnostic serves; route to `ai-use-case-mapping` if the client already knows its maturity and only needs task priorities.
2. Walk through all 41 items with the client, recording Y or N; stop and complete the intake before scoring if any item is unanswered, using the [diagnostic method](references/readiness-diagnostic-method.md).
3. Score each domain, total the score, set the Canvas step and apply the domain gap thresholds below; convert the total to a percentage (total ÷ 41 × 100) for the Use Case Matrix.
4. Ask the maturity-wave question (Nayebi, 2025) and use the answer to calibrate the roadmap.
5. Write the five report sections in order: score summary table first, Canvas step diagnosis, top 3 priority gaps, 90-day action plan (three named actions per 30-day block) and recommended tools calibrated to the step.
6. Where Data Foundation scores 0–3 or the client asks for a data audit, add the hygiene audit or the 90-day data foundation plan; where the client wants the full canvas, add the canvas and 12-month roadmap.
7. Check the report against the Quality Standards; correct any miscounted score, generic action or out-of-market tool and rerun the check before delivery.
8. Deliver with the unassessed items, follow-up list for uncertain answers and the next approval or verification step.

## Scoring bands

| Total score | Canvas step |
|---|---|
| 0–8 | Step 1 — Foundation |
| 9–16 | Step 2 — Experimentation |
| 17–24 | Step 3 — Expansion |
| 25–32 | Step 4 — Transformation |
| 33–41 | Step 5 — Reinvention |

Domain maxima: Data Foundation 8 (items 1–8), Technology Stack 8 (9–16), Team Capability 8 (17–24), AI Deployment 9 (25–33), Business Impact 8 (34–41); total 41. Gap thresholds: Data Foundation 0–3, Technology Stack 0–3, Team Capability 0–3, AI Deployment 0–4, Business Impact 0–3. Most Ugandan and East African SMEs score between 4 and 12 (Step 1 or early Step 2); this reflects the market's stage of AI adoption, not a failure.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Scored diagnostic report (score summary, Canvas step diagnosis, top 3 gaps, 90-day plan, tools) | Non-technical business owner | Readable without a consultant present; the score table comes first and each gap names its N items and first action. |
| Data foundation audit or 90-day data foundation plan (when triggered) | Client data owner | Hygiene checklist, data map and remediation plan, or inventory, RAG quality scorecard, customer schema and DPA 2019 consent, are complete. |
| AI Marketing Canvas and 12-month quarterly roadmap (when requested) | Client leadership | Four customer moments completed and the roadmap is calibrated to the diagnosed step. |
| Gap and follow-up note | Consultant and `ai-use-case-mapping` | Uncertain answers, unassessed checks and actions needing authority are listed with owners. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| 41-item answer sheet | Table: item, domain, Y/N, note | Every item answered; each uncertain N carries a follow-up note. |
| Score calculation | Table: domain score, total, percentage, Canvas step, matrix quadrant | Domain sums, total and step reconcile with the answer sheet. |
| Tool recommendation register | Table: need, tool, tier, price source and date | Every tool has a tier and a dated price or is flagged unpriced. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. The diagnostic never connects an AI tool to customer data; that needs a lawful basis, consent and an accountable owner first.

## Degraded Mode

Without the client's own answers to the 41 items, return the narrowest qualified result and mark the affected checks `not assessed`. A blank answer sheet, the scoring bands and the East African starting-point context can still be delivered, but no step or score is stated.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client is unsure how to answer an item | Record N and note it for follow-up. | An inflated score and a roadmap the client cannot execute. |
| The total places the client at Step 1 | Say so directly and explain what that means in practice; the 90-day plan is about basic data and tools, not AI-powered personalisation. | Softened, vague advice that hides the real starting point. |
| Data Foundation scores 0–3, or the client asks for a customer-data hygiene audit before buying AI tools | Run the 20-item hygiene checklist, data map and 30-day remediation plan in [data-foundation-audit.md](references/data-foundation-audit.md). | Connecting AI tools to fragmented, duplicated or non-consented data. |
| The client needs a 90-day data foundation build (inventory, RAG quality scorecard, customer schema, DPA 2019 consent) | Produce the plan in [data-foundation-plan.md](references/data-foundation-plan.md). | A generic schema or vague plan that never reaches a measurable data health score. |
| The client wants the completed AI Marketing Canvas and a 12-month roadmap, not only the score | Place them with the nine-question canvas diagnostic and build the canvas and roadmap in [ai-marketing-canvas-scoring.md](references/ai-marketing-canvas-scoring.md). | Step inflation and a roadmap the client cannot execute. |
| Score percentage is 0–25 %, 26–50 %, 51–75 % or 76–100 % | Scope the Use Case Matrix: Internal/Productivity only; add an External/Productivity pilot; all four quadrants with the highest-ROI cell first; full transformation with Monetisation (Canvas Step 5). For every use case, choose the lowest viable automation level that data readiness, AI maturity and risk support, and define its human approval gate. | Deploying growth-quadrant AI before the basics exist. |
| The client asks whether its AI use is governed to a recognised standard (ISO/IEC 42001, NIST AI 600-1) or the diagnostic shows no AI policy, reviewer or provenance log | Score governance as a gap and route the fix to `policy-ai-content-ethics`, using its [management-system alignment](../../policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md#9-management-system-alignment) (registers `ISO-IEC-42001-2023` partial, `NIST-AI-600-1`); ISO clause mapping and certification stay `NOT_ASSESSED` here. | A readiness score that ignores AI governance, or a claimed ISO alignment with no evidence. |
| A tool is recommended | Prefer free tiers, tools accessible from Uganda without VPN or restricted payment, and UGX or USD pricing with local payment options. | Tools the client cannot pay for or reach. |
| The client already uses WhatsApp for customer communication | Count it toward the Technology Stack domain and formalise it via Africa's Talking or similar APIs. | Ignoring the client's strongest existing channel. |

## Quality Standards

- All 41 items are addressed; no question is skipped or estimated without a reason recorded.
- The total score is calculated accurately and the Canvas step is stated clearly.
- The domain breakdown reveals specific gap areas and is not reduced to a single total score.
- The 90-day plan contains specific, named actions (a tool, a process, a person or role), not generic advice such as "improve data quality".
- Tool recommendations match the client's step and are accessible in the East African market, with free tiers prioritised.
- Language is honest: if the client is at Step 1, the diagnosis says so clearly and explains what that means in practical terms.
- The output is structured so a non-technical business owner can read it without a consultant present and know exactly what to do next.
- The score summary table is the first thing the client sees; context and explanation follow the data.

## Anti-Patterns

- Reporting only the total score. Fix: show each domain score with a Strong, Developing or Critical status.
- Recommending AI-powered personalisation to a Step 1 client. Fix: calibrate the 90-day plan to getting basic data and tools in place.
- Filling uncertain answers with Y to be encouraging. Fix: record N and list the item for follow-up.
- Recommending paid tools first or tools that need a VPN or foreign card. Fix: lead with free tiers and demonstrate value before any paid subscription.
- Quoting a tool price as current without a date. Fix: record the price source and date or flag it unpriced.
- Ignoring the informal ChatGPT use most teams already have. Fix: record it under Team Capability and route policy and training to `training-client-team`.

## References

- [Readiness diagnostic method](references/readiness-diagnostic-method.md): read when running the 41 questions, scoring, writing the five report sections, recommending tools, or applying the Use Case Matrix and maturity waves.
- [data-foundation-audit](references/data-foundation-audit.md): read when auditing fragmented customer data (hygiene checklist, data map, 30-day remediation) before any AI tool is connected.
- [data-foundation-plan](references/data-foundation-plan.md): read when a larger client needs a 90-day data foundation plan with customer schema and Uganda DPA 2019 consent.
- [data-product-and-ai-foundation-principles](references/data-product-and-ai-foundation-principles.md): read when the plan must cover data-product ownership, lineage, freshness, audience boundaries or AI marketing controls.
- [ai-marketing-canvas-scoring](references/ai-marketing-canvas-scoring.md): read when completing the AI Marketing Canvas, four customer moments and 12-month roadmap after scoring.
- [AI transparency and provenance](../../policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md): read when the roadmap needs AI governance aligned to ISO/IEC 42001 or NIST AI 600-1, or a disclosure and provenance control.
- [ai-use-case-mapping](../ai-use-case-mapping/SKILL.md): read when the client needs task-level AI priorities after the diagnostic.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
- [Anti-AI slop production gate](../anti-ai-slop/SKILL.md): read when writing the diagnosis and action plan text.
<!-- dual-compat-end -->

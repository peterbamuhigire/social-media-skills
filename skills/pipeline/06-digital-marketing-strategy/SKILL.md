---
name: 06-digital-marketing-strategy
description: "Use when integrating social, email, search, web, influencer and paid channels into one plan. Produces board-ready digital marketing strategy and 12-month roadmap; use `05-social-media-strategy` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Digital Marketing Strategy Generator

Produce the boardroom-level digital marketing strategy document. This is the broadest strategy deliverable in the suite — it integrates all digital channels into a unified plan. Every section must be populated with client-specific content. Apply British English throughout. Default to Uganda/East Africa context unless the client specifies otherwise.

Use paid, owned and earned media and the customer journey as organising lenses where helpful. Framework labels never substitute for customer evidence, a channel investment decision or a delivery plan.

Add Kennedy's systems lens before selecting tactics:

- avoid dependence on a single platform or traffic source
- distinguish acquisition, conversion, retention, and referral mechanisms
- define the lead-generation offer separately from the core sale
- treat the website, email list, and customer database as strategic assets, not optional extras
- when the client sells premium, high-ticket, luxury/affluent, executive, or enterprise offers, load `skills/strategy/premium-social-selling/SKILL.md` before finalising positioning, content, lead generation, outreach, email nurture, or conversion strategy

---
<!-- dual-compat-start -->
## Use When
- Use this skill for integrating social, email, search, web, influencer and paid channels into one plan.
- Confirm that `05-social-media-strategy` is not the closer route before proceeding.

## Do Not Use When
- Use `05-social-media-strategy` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Approved brief, channel evidence, revenue model, objectives and budget | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Board-ready digital marketing strategy and 12-month roadmap | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary
Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode
If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified board-ready digital marketing strategy and 12-month roadmap. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Approved brief, channel evidence, revenue model, objectives and budget is current and attributable | Produce the full board-ready digital marketing strategy and 12-month roadmap and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `05-social-media-strategy` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `05-social-media-strategy` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply [the premium growth operating contract](references/premium-growth-operating-contract.md): customer research, offer, channel choices, creative, website/CRM handoff, economics, experiments and service review. Follow the decision table when evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the board-ready digital marketing strategy and 12-month roadmap, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the board-ready digital marketing strategy and 12-month roadmap without approved brief. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `05-social-media-strategy` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified approved brief, the skill produces a board-ready digital marketing strategy and 12-month roadmap with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`05-social-media-strategy`](../05-social-media-strategy/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- [Social operating system and pragmatics reference](references/social-operating-system-and-pragmatics.md)
- [Channel creative and service lab](references/channel-creative-and-service-lab.md) — native production, community, rights and measurable outcomes across Facebook, Instagram and TikTok.

## Integrated marketing deliverable

Read [premium growth operating contract](references/premium-growth-operating-contract.md)
before choosing tactics or promising returns. This engine owns the integrated
digital-marketing strategy, including search, paid media, social, email,
permissioned messaging, content, conversion, CRM, retention and referral.
Route website builds, visual production and finance review to their canonical engines.

Produce a decision-ready pack:

1. Executive decision and customer evidence, including contradictory findings.
2. Positioning, offer, proof and credible alternatives, including internal/AI-assisted delivery.
3. Journey diagnosis from discovery through delivery and retention.
4. Selected/deferred channel portfolio with evidence, costs, capacity and owners.
5. Native creative briefs and rights/accessibility/approval workflow.
6. Website, CRM, sales and service handoff with observable acceptance.
7. Contribution-based economics, attribution limitations and reconciled budgets.
8. Bounded experiments, stop rules, first implementation cycle and conditional roadmap.
9. Applicable standards/policies, unresolved evidence and release decision.

Scale the horizon to the brief. A twelve-month roadmap is conditional, with
regular evidence reviews; it does not promise a fixed month for search rankings,
leads or revenue. Select content cadence, budget split and nurture frequency
from audience need and team capacity. Do not prescribe universal percentages.

## Economics and evidence checks

Use contribution and matching cohorts for acquisition economics. Separate ROAS,
attributed contribution, incremental ROI, lifetime contribution and cash payback.
Do not equate annual revenue with lifetime profit, combine inconsistent periods,
sum duplicated platform conversions, or claim incrementality from attribution.
The reference contains a reproducible synthetic loss case despite positive ROAS.

## AI and service quality

For each AI use, name the task, permitted inputs, reviewer, expected improvement,
failure mode, evaluation and fallback. Measure useful output and correction time;
do not promise that an AI tool produces superior commercial results. Customer
data, copyrighted assets and confidential work require authorised handling.

Sell inspectable value: customer insight, a considered choice, distinctive
creative, reliable implementation, measurement and learning. Premium fees require
a credible delivery scope and buyer evidence; luxury language is not proof.

## Quality criteria

- Every selected channel has a buyer job, destination, owner, cost and decision measure.
- Budget includes production, labour, fees, tools and media without double counting.
- Forecasts reconcile with sales capacity, fulfilment and the finance model.
- Current platform mechanics are sourced, account-checked or explicitly withheld.
- Each creative unit passes specificity, evidence, rights, accessibility and native-format review.
- Client-account actions require explicit execution authority.
- The service review states what to change, stop, retain and investigate next.

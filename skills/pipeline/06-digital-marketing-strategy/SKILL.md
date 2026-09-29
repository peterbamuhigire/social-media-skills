---
name: 06-digital-marketing-strategy
description: Use when a client wants a single integrated plan for all its online marketing, bringing together social, website, SEO, email, influencers and paid media; produces the board-ready digital marketing strategy with a 12-month roadmap and channel budget; not for a plan covering social channels only (use `05-social-media-strategy`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Digital Marketing Strategy Generator

Produces the boardroom-level digital marketing strategy, the broadest strategy deliverable in the suite, integrating all digital channels into a unified plan with every section populated with client-specific content. Apply British English throughout and default to Uganda/East Africa context unless the client specifies otherwise.

<!-- dual-compat-start -->
## Use When
- Marketing is spread across social, website, email, search and ads with no single plan tying them to business goals.
- The board wants a twelve-month roadmap with budget, lifecycle coverage and the order in which channels are built.
- A B2B client needs a demand-generation sequence across LinkedIn, website content, email nurture and paid search.
- The annual channel-mix review is due and the client needs scenarios for what to cut, keep or grow.

## Do Not Use When
- `05-social-media-strategy` when the plan covers social channels only.
- `peso-integrated-strategy` for coordinating paid, earned, shared and owned media.
- `advertising-strategy-and-budget` for the paid media plan and budget split.
- Stop before quoting channel costs, reach or return figures that have not been verified; flag them as estimates.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Approved client brief with business goals and revenue model | `01-client-brief`; client finance lead | Yes | Stop channel selection; return the goal and revenue-model questions. |
| Customer evidence, including contradictory findings | Personas, CRM, sales and service records, research | Yes | Label the positioning provisional and propose a bounded research step before scaling spend. |
| Current channel evidence (social, website, email, search, paid) with dates | `02-platform-audit`; account exports; analytics | Yes | Mark the channel `not assessed`; do not quote reach, cost or return for it. |
| Budget covering production, labour, fees, tools and media | Client | Yes | Present conditional scenarios instead of a fixed budget split. |
| Sales capacity, fulfilment limits and the finance model | Client operations and finance | Yes | Withhold forecasts and state the reconciliation still needed. |
| Offer tier (premium, high-ticket, luxury/affluent, executive or enterprise) | Client brief | If applicable | Treat as standard; load the high-value social selling reference once the tier is confirmed. |

## Workflow

1. Confirm the decision, consumer, market and period; stop and route to `05-social-media-strategy` when the plan covers social channels only, or to `peso-integrated-strategy` or `advertising-strategy-and-budget` when those contracts are closer.
2. Read the [premium growth operating contract](references/premium-growth-operating-contract.md) before choosing tactics or promising returns: customer research, offer, channel choices, creative, website/CRM handoff, economics, experiments and service review.
3. Apply Kennedy's systems lens before selecting tactics: avoid dependence on a single platform or traffic source; distinguish acquisition, conversion, retention and referral mechanisms; define the lead-generation offer separately from the core sale; treat the website, email list and customer database as strategic assets, not optional extras.
4. For premium, high-ticket, luxury/affluent, executive or enterprise offers, load `skills/playbooks/playbook-social-selling/references/high-value-social-selling.md` (formerly `premium-social-selling`) before finalising positioning, content, lead generation, outreach, email nurture or conversion strategy.
5. Use paid, owned and earned media and the customer journey as organising lenses where helpful, with [digital planning lenses](references/digital-planning-lenses.md) for lifecycle coverage, scenarios and the B2B demand-generation sequence; framework labels never substitute for customer evidence, a channel investment decision or a delivery plan.
6. Build the nine-part strategy pack below and run the economics and evidence checks; correct any unreconciled budget, duplicated conversion or unsourced platform mechanic and rerun the affected section.
7. Run the anti-slop ship gate; route website builds, visual production and finance review to their canonical engines, and withhold release while a blocking factual, permission or evidence defect remains.

## Strategy pack contents

This engine owns the integrated digital-marketing strategy, including search, paid media, social, email, permissioned messaging, content, conversion, CRM, retention and referral. Produce a decision-ready pack:

1. Executive decision and customer evidence, including contradictory findings.
2. Positioning, offer, proof and credible alternatives, including internal/AI-assisted delivery.
3. Journey diagnosis from discovery through delivery and retention.
4. Selected/deferred channel portfolio with evidence, costs, capacity and owners.
5. Native creative briefs and rights/accessibility/approval workflow.
6. Website, CRM, sales and service handoff with observable acceptance.
7. Contribution-based economics, attribution limitations and reconciled budgets.
8. Bounded experiments, stop rules, first implementation cycle and conditional roadmap.
9. Applicable standards/policies, unresolved evidence and release decision.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Boardroom-level digital marketing strategy pack (nine parts) | Client board; `05-social-media-strategy`; `07-email-marketing-strategy`; `09-campaign-strategy` | Every section client-specific; every selected channel has a buyer job, destination, owner, cost and decision measure. |
| Conditional roadmap (twelve months where the brief warrants it) | Client lead; delivery team | Scaled to the brief, with regular evidence reviews; no fixed month promised for search rankings, leads or revenue. |
| Service review | Client lead | States what to change, stop, retain and investigate next. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Economics workbook | Table: ROAS, attributed contribution, incremental ROI, lifetime contribution, cash payback, by matching cohort and period | Measures kept separate; periods consistent; no duplicated platform conversions summed. |
| Channel evidence register | Table: channel, source, date, account-checked or withheld | Current platform mechanics are sourced, account-checked or explicitly withheld. |
| AI-use register | Table: task, permitted inputs, reviewer, expected improvement, failure mode, evaluation, fallback | Every AI use listed with useful output and correction time measured. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Customer data, copyrighted assets and confidential work require authorised handling.

## Degraded Mode

Without verified channel evidence and a revenue model, return the narrowest qualified result and mark the affected checks `not assessed`. A journey diagnosis, a selected/deferred channel shortlist and a bounded first experiment can still be delivered, with every cost, reach or return figure flagged as an estimate.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Acquisition economics are being judged | Use contribution and matching cohorts; separate ROAS, attributed contribution, incremental ROI, lifetime contribution and cash payback. | Positive ROAS hiding a loss (the reference contains a reproducible synthetic loss case). |
| Revenue, periods or conversions come from different sources | Do not equate annual revenue with lifetime profit, combine inconsistent periods, sum duplicated platform conversions, or claim incrementality from attribution. | Inflated returns shown to the board. |
| Content cadence, budget split or nurture frequency is needed | Select from audience need and team capacity; do not prescribe universal percentages. | A plan the team cannot deliver. |
| An AI tool is proposed for a task | Name the task, permitted inputs, reviewer, expected improvement, failure mode, evaluation and fallback; do not promise that an AI tool produces superior commercial results. | Unmeasured AI claims and data leakage. |
| The client asks for premium fees or premium positioning | Require a credible delivery scope and buyer evidence; sell inspectable value (customer insight, a considered choice, distinctive creative, reliable implementation, measurement and learning). Luxury language is not proof. | A premium promise the service cannot support. |
| Channel costs, reach or return figures are unverified | Flag them as estimates or withhold them. | Fabricated precision in the board pack. |
| The plan covers social channels only | Route to `05-social-media-strategy` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- Every selected channel has a buyer job, destination, owner, cost and decision measure.
- Budget includes production, labour, fees, tools and media without double counting.
- Forecasts reconcile with sales capacity, fulfilment and the finance model.
- Current platform mechanics are sourced, account-checked or explicitly withheld.
- Each creative unit passes specificity, evidence, rights, accessibility and native-format review.
- Client-account actions require explicit execution authority.
- The service review states what to change, stop, retain and investigate next.
- British English throughout; Uganda/East Africa context by default unless the client specifies otherwise.

## Anti-Patterns

- Treating every channel as an acquisition tool. Fix: map acquisition, conversion, retention and referral mechanisms separately.
- Building the plan on one platform or traffic source. Fix: make the website, email list and customer database the strategic assets.
- A fixed-date roadmap that promises rankings, leads or revenue by a set month. Fix: make it conditional with regular evidence reviews.
- Summing platform-reported conversions across channels. Fix: de-duplicate and state the attribution limitations.
- Letting a framework label stand in for a decision. Fix: tie each lens to customer evidence, a channel investment decision or a delivery plan.
- Promising that AI tooling beats human work commercially. Fix: measure useful output and correction time and name the fallback.

## References

- [Premium growth operating contract](references/premium-growth-operating-contract.md): read before choosing tactics or promising returns, and for the synthetic loss case.
- [Digital planning lenses](references/digital-planning-lenses.md): read when drafting diagnosis and channel sections: lifecycle coverage, impact-before-budget, scenario planning, the B2B demand-generation sequence and the annual channel-mix review.
- [Channel creative and service lab](references/channel-creative-and-service-lab.md): read when planning native production, community, rights and measurable outcomes across Facebook, Instagram and TikTok.
- [Social operating system and pragmatics reference](references/social-operating-system-and-pragmatics.md): read when the social layer needs affordance cards and conversation controls.
- [Demand generation and social operating system](references/demand-generation-and-social-operating-system.md): read when the strategy needs practical demand creation rather than a list of channels.
- [High-value social selling](../../playbooks/playbook-social-selling/references/high-value-social-selling.md): read when the offer is premium, high-ticket, luxury/affluent, executive or enterprise.
- [`05-social-media-strategy`](../05-social-media-strategy/SKILL.md): read when the plan covers social channels only.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

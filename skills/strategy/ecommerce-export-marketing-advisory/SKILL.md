---
name: ecommerce-export-marketing-advisory
description: Use when the main deliverable concerns export-market selection, cross-border trust, channel conversion, partnerships, and CAC-bounded campaigns; use ecommerce-brand-differentiation when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# E-Commerce Export Marketing Advisory

<!-- dual-compat-start -->
## Use When

- Use this skill for export-market selection, cross-border trust, channel conversion, partnerships, and CAC-bounded campaigns.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `ecommerce-brand-differentiation` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to export-market selection, cross-border trust, channel conversion, partnerships, and CAC-bounded campaigns | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `ecommerce-brand-differentiation`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Export-market selection, cross-border trust, channel conversion, partnerships, and cac-bounded campaigns deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
| Decision and risk record | Reviewer or implementer | Links each recommendation to supplied evidence or labels it as an assumption |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Input and assumption register | Table or annotated brief | Missing and unverified items are visible, not treated as passed |
| Release check | Completed quality checklist | All blocking findings are fixed or the deliverable is explicitly withheld |

## Capability and Permission Boundaries

Read and search are the minimum capabilities. Analysis and planning remain read-only. Edit only files placed in scope; publishing, outreach, spend, personal-data processing, production changes, and certification claims require explicit authority and evidence of success.

## Degraded Mode

If files, tools, network, current evidence, rendering, or authorised access are unavailable, return the narrowest useful qualified deliverable. Mark each unavailable check `not assessed`; never convert it into a pass or invent market facts.

## Decision Rules

| Choice condition | Action | Failure or risk avoided |
|---|---|---|
| Market, fulfilment, compliance, or unit-economics evidence is missing | Return a qualified readiness gap and stop before claiming market viability | Spending on acquisition before the export offer can be fulfilled profitably |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source | Confident advice built on an unresolved premise |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist | Unauthorised publication, spend, outreach, or data use |

## Quality Standards

- Keep Uganda/East Africa, British English, EAT, UGX, and WhatsApp-first assumptions explicit where they apply.
- Tie recommendations to observed evidence, a named assumption, or a verification action.
- Give the next operator enough detail to execute without guessing ownership, sequence, or acceptance.
- Apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Inventing a client metric, audience fact, price, partner, or platform rule. Fix: verify it or label the decision provisional.
- Treating a missing tool, source, render, or approval as a passed check. Fix: mark it `not assessed` and narrow the output.
- Producing channel tactics before defining the decision and consumer. Fix: state the required outcome and handoff first.
- Copying a global template without adapting Uganda/East Africa access, language, payment, or trust conditions. Fix: record which local assumptions apply.
- Recommending publication, outreach, spend, data collection, or a regulated claim without authority. Fix: stop at an approval-ready draft.
- Reporting activity as success without an acceptance condition. Fix: name the observable result and evidence source.

## References

- [export-marketing-plan-template.md](references/export-marketing-plan-template.md)
- [trust-and-conversion-review.md](references/trust-and-conversion-review.md)
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Overview

Use this skill to turn an e-commerce diagnostic and unit-economics model into a practical export-marketing plan. It focuses on market-specific messaging, cross-border trust, proof, localised channels, conversion improvements, partnership outreach, and budgets tied to CAC guardrails.

## Use When

- A company wants to enter or grow in another EAC market or export market through digital channels.
- You need an export marketing plan, campaign outline, conversion review, trust/proof checklist, or partner outreach pack.
- The marketing recommendation must fit the company's margin, CAC, logistics, and payment reality.

## Do Not Use When

- No target market is named.
- Unit economics are unknown and the recommendation involves paid acquisition or discounting.
- The task is only a domestic social-media content calendar.

## Required Inputs

- Company diagnostic, target market, current channels, product/category, customer evidence, analytics, and conversion data.
- Unit-economics guardrails: acceptable CAC, contribution margin, discount limits, and route viability.
- Payment, logistics, returns, compliance, language, and customer-support constraints.

## Workflow

1. Define the target-market buyer and cross-border trust problem.
2. Build customer personas around evidence: need, proof required, buying objections, payment preference, delivery expectations, language, and support expectations.
3. Design the trust-and-proof layer: reviews, secure-payment signals, delivery promises, returns policy, authenticity proof, certifications, local partner cues, and customer support route.
4. Review conversion leaks in the digital journey: mobile UX, product pages, checkout, payment options, shipping clarity, proof, support, and remarketing.
5. Write market-entry messaging and value propositions localised to country, language, currency, and norms.
6. Plan channels and campaigns within CAC and margin guardrails.
7. Draft partnership outreach for marketplaces, logistics firms, payment providers, local agents, sector bodies, and influencers only where they fit the route economics.
8. Define KPIs the company can actually track.

## Quality Bar

- The plan is specific to one target market or clearly separated by market.
- Trust signals match known buyer objections and route risks.
- Campaign budget respects CAC and contribution-margin guardrails.
- Channel recommendations are measurable with the company's actual tools.
- Any channel penetration, market-size, or platform statistic is sourced and dated.

## Anti-Patterns

- Generic regional expansion advice.
- Paid campaigns without CAC limits.
- Ignoring delivery, returns, payment, and trust barriers.
- Copy that is not localised for language, currency, proof, or norms.
- KPIs the company has no way to measure.

## Outputs

- Export marketing plan.
- Cross-border customer personas.
- Trust-and-proof checklist.
- Digital-channel conversion review.
- CAC-bounded campaign outline.
- Partnership outreach messages.
- KPI and implementation tracker.

## References

- [references/export-marketing-plan-template.md](references/export-marketing-plan-template.md): Plan sections, personas, channel plan, budget, and KPIs.
- [references/trust-and-conversion-review.md](references/trust-and-conversion-review.md): Trust signals and conversion-review checklist.

---
name: demand-forecasting
description: Use when the main deliverable concerns demand forecasts, stockout timing, reorder decisions, and duplicate-safe operational-data analysis; use meta-budget-planner when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Demand Forecasting

<!-- dual-compat-start -->
## Use When

- Use this skill for demand forecasts, stockout timing, reorder decisions, and duplicate-safe operational-data analysis.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `meta-budget-planner` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to demand forecasts, stockout timing, reorder decisions, and duplicate-safe operational-data analysis | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `meta-budget-planner`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Demand forecasts, stockout timing, reorder decisions, and duplicate-safe operational-data analysis deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
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
| Data has duplicate joins, gaps, or too little history | Reconcile grain and return ranges with limitations instead of a point forecast | False precision and inventory decisions based on double-counted demand |
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

- [AGENTS.md](../../../AGENTS.md)
<!-- dual-compat-end -->

## Overview

Use this skill to turn sales, inventory, branch, and operational signals into demand forecasts and replenishment recommendations. It is especially relevant when fixing SQL joins that duplicate products, deriving days until stockout, or documenting demand-driven planning assumptions.

## Workflow

1. Define the reporting grain first: usually one row per product per shop, branch, outlet, or warehouse for the forecast horizon.
2. Aggregate sales and stock movements before joining product, branch, and stock-balance tables. Do not join raw sales lines directly to item master or stock balances when the output expects one product row.
3. Exclude or separately flag voided sales, returns, internal transfers, stockout days, and one-off events that would distort demand.
4. Normalize demand to a daily rate. Use 7, 30, and 90 day windows when available, and explain which window drives the forecast.
5. Derive days until stockout as `current_stock / daily_demand`. If demand is zero, report "no active demand" rather than hiding the value as an unexplained N/A.
6. Calculate forecast consumption as `daily_demand * horizon_days`.
7. Calculate reorder point as `daily_demand * lead_time_days + safety_stock`.
8. Calculate suggested order as `max(0, forecast_consumption + safety_stock - current_stock - inbound_qty)`.
9. Backtest against historical periods using WAPE/MAPE, bias, and missed-stockout counts.

## Join Guardrails

- Use CTEs or subqueries for `sales_by_product_branch`, `stock_by_product_branch`, and `inbound_by_product_branch`.
- Group every CTE by the same business key before joining: product id plus branch/shop/outlet/warehouse id.
- Join product and branch names once, after aggregation.
- Assert that the final result has no duplicate product plus branch rows.
- If the UI needs one product row per selected branch, collapse variants after filtering by branch, not across all branches.

## References

Load `references/demand_forecasting.md` for SQL templates, stockout formulas, and demand-driven planning notes.

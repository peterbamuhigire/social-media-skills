---
name: demand-forecasting
description: Use when a retailer, pharmacy or distributor needs to know how fast stock sells, when items run out and what to reorder, or a sales-and-stock report duplicates products; produces the forecast by product and branch, stockout dates, reorder points and suggested orders; not for splitting the marketing budget (use `meta-budget-planner`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Demand Forecasting

Turns sales, inventory, branch and operational signals into demand forecasts and replenishment recommendations for the owner, buyer or branch manager. It is especially relevant when fixing SQL joins that duplicate products, deriving days until stockout, or documenting demand-driven planning assumptions.

<!-- dual-compat-start -->
## Use When

- The owner asks how many days each product has before it runs out, per shop or branch.
- Reorder points, safety stock and suggested order quantities are needed from sales and stock data.
- A sales and stock query or report shows the same product several times because tables are joined before aggregation.
- Promotions, returns, voids or stockout days are distorting the demand figures.
- The forecast needs back-testing with WAPE, bias and missed stockouts before anyone trusts it.

## Do Not Use When

- `meta-budget-planner` for dividing the marketing budget and working back from a revenue target.
- `social-commerce-strategy` for catalogue, WhatsApp ordering and fulfilment content.
- Stop when sales or stock history is missing or duplicated; flag the gap instead of guessing demand.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| The decision and horizon (stockout watch, reorder list, branch comparison) and the reporting grain | Owner, buyer or branch manager | Yes | Default to one row per product per branch for the stated horizon and confirm before reporting. |
| Sales lines with dates, branch and status (voided, refunded, cancelled, returns, internal transfers) | POS, ERP or supplied export | Yes | Stop and flag the gap; do not estimate demand from stock movements alone. |
| Stock balances and inbound quantities by product and branch | Inventory system or stock count | Yes | Report daily demand only; mark days until stockout and suggested orders `not assessed`. |
| Supplier lead times and the service goal for safety stock | Buyer or procurement lead | Conditional | Show reorder points without safety stock and label them provisional. |
| Stockout days, promotions and one-off events in the window | Branch managers, promotion calendar | Conditional | Flag the window as possibly distorted and prefer the longer averaging window. |
| Product, variant and branch master data | ERP or product catalogue | Yes | Report by id only and list unmatched keys. |

## Workflow

1. Define the reporting grain first: usually one row per product per shop, branch, outlet or warehouse for the forecast horizon. Stop when sales or stock history is missing or duplicated; flag the gap instead of guessing demand.
2. Aggregate sales and stock movements before joining product, branch and stock-balance tables (see the join guardrails below). Do not join raw sales lines directly to item master or stock balances when the output expects one product row.
3. Exclude or separately flag voided sales, returns, internal transfers, stockout days and one-off events that would distort demand.
4. Normalise demand to a daily rate. Use 7, 30 and 90 day windows when available, and explain which window drives the forecast.
5. Derive days until stockout as `current_stock / daily_demand`. If demand is zero, report "no active demand" rather than hiding the value as an unexplained N/A.
6. Calculate forecast consumption as `daily_demand * horizon_days`, reorder point as `daily_demand * lead_time_days + safety_stock`, and suggested order as `max(0, forecast_consumption + safety_stock - current_stock - inbound_qty)` ([formulas and SQL pattern](references/demand_forecasting.md)).
7. Run the cardinality check; if any product plus branch appears more than once, correct the grain or join and rerun before anything is reported.
8. Backtest against historical periods using WAPE/MAPE, bias and missed-stockout counts; return ranges with limitations where history is short.
9. Hand the forecast, reorder list, assumptions and unresolved data gaps to the named buyer or branch manager as recommendations; placing orders stays with them.

## Join Guardrails

- Use CTEs or subqueries for `sales_by_product_branch`, `stock_by_product_branch` and `inbound_by_product_branch`.
- Group every CTE by the same business key before joining: product id plus branch/shop/outlet/warehouse id.
- Join product and branch names once, after aggregation.
- Assert that the final result has no duplicate product plus branch rows.
- If the UI needs one product row per selected branch, collapse variants after filtering by branch, not across all branches.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Forecast table by product and branch (daily demand by window, days until stockout, forecast consumption) | Owner, branch manager | One row per product plus branch; the driving window is named; zero demand reads "no active demand". |
| Reorder list (reorder point, safety stock, suggested order quantity) | Buyer or procurement lead | Every quantity shows its lead time, inbound quantity and service assumption, or is labelled provisional. |
| Duplicate-safe query or report fix | Developer or report owner | Aggregates before joining; the cardinality check returns zero rows. |
| Backtest summary | Owner, analyst | WAPE/MAPE, bias and missed-stockout counts stated for a named historical period. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Cardinality check result | Query and row count | Zero duplicate product plus branch rows before the report is accepted. |
| Exclusion and distortion log | Table: rule, rows affected, window | Voids, returns, transfers, stockout days and one-off events are counted, not silently dropped. |
| Input and assumption register | Table | Lead times, service level, windows and missing data are visible, not treated as passed. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Queries run against supplied exports or read-only replicas; placing purchase orders, changing stock records or editing production reports needs the owner's authority.

## Degraded Mode

Without complete, de-duplicated sales and stock history, return the narrowest qualified result and mark the affected checks `not assessed`. Daily demand ranges by available window, with the gaps listed, can still be delivered instead of a point forecast.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Data has duplicate joins, gaps, or too little history | Reconcile grain and return ranges with limitations instead of a point forecast | False precision and inventory decisions based on double-counted demand |
| Sales, stock or inbound figures contradict each other or are materially incomplete | Pause the affected product or branch recommendation and request the accountable source | Confident reorder advice built on an unresolved premise |
| `daily_demand <= 0` | Report no active demand and keep stockout risk low unless an expiry, commitment or minimum-stock rule applies | Unexplained N/A values or false stockout alarms |
| The item was out of stock for part of the window | Compute `daily_demand = units_sold / in_stock_days`, not over calendar days | Understating demand for items that sold out |
| Promotions or one-off events sit inside the window | Flag them separately and explain which window drives the forecast | A spike treated as the new baseline |
| The UI needs one product row per selected branch | Collapse variants after filtering by branch, not across all branches | Mixing other branches' stock into the selected branch |
| Authority is limited to analysis or planning | Deliver a read-only reorder recommendation and approval checklist | Unauthorised orders or changes to live stock records |

## Quality Standards

- One row per product per branch, confirmed by the cardinality check.
- Every forecast names its window (7, 30 or 90 days) and every reorder figure its lead time and safety-stock basis.
- Voids, refunds, cancellations, returns, transfers and stockout days are excluded or flagged, with counts.
- Zero or negative demand reads "no active demand", never a blank or unexplained N/A.
- The forecast is backtested (WAPE/MAPE, bias, missed stockouts) before anyone relies on it.
- Keep Uganda/East Africa, British English, EAT, UGX and WhatsApp-first assumptions explicit where they apply.
- Give the next operator enough detail to execute without guessing ownership, sequence or acceptance.
- Apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Joining raw sales lines to the item master and stock balances in one query. Fix: aggregate each source to product plus branch first, then join names once.
- Averaging demand over calendar days when the item was out of stock. Fix: divide by in-stock days and flag stockout days.
- Treating a promotion week as normal demand. Fix: flag one-off events and compare the 7, 30 and 90 day windows.
- Hiding zero demand as N/A. Fix: report "no active demand" and apply any expiry or minimum-stock rule separately.
- Collapsing variants across all branches before filtering. Fix: filter by branch first, then collapse.
- Handing over reorder quantities without a backtest. Fix: report WAPE/MAPE, bias and missed-stockout counts for a named period.

## References

- [Demand forecasting formulas and SQL pattern](references/demand_forecasting.md): read when you need SQL templates, stockout formulas, safety stock and reorder points, demand-driven planning notes, or the cardinality check.
- [`meta-budget-planner`](../../meta-analytics-ops/meta-budget-planner/SKILL.md): read when the request is really about the marketing budget or a revenue target.
- [`social-commerce-strategy`](../../strategy/social-commerce-strategy/SKILL.md): read when the question is catalogue, WhatsApp ordering or fulfilment content.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md) and [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read when drafting the client-facing report and at the release check.
- [Repository agent guide](../../../AGENTS.md): read when unsure how this engine's skills are routed.
<!-- dual-compat-end -->

---
name: advertising-strategy-and-budget
description: Use when a client asks how much to spend on advertising, on what, and how success will be judged; covers objectives, a triangulated budget with floor and ceiling, phased allocation, decision memos and agency terms; produces an advertising budget recommendation; not for splitting a total marketing budget (use `meta-budget-planner`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Advertising Strategy and Budget

Turns a business problem into an advertising strategy the client can approve: one objective hierarchy, one measurement architecture, a budget that three methods agree on, and clear governance for the agency–client relationship. The skill plans and recommends; it never spends money or changes a live account.

<!-- dual-compat-start -->
## Use When

- How much should we spend on advertising, on what, and how will we know it worked?
- We need an annual advertising budget, a launch budget or money to answer a competitor's push.
- A budget cut, a rival's heavy spend or a campaign pivot needs a short decision memo the MD can approve quickly.
- The agency relationship needs terms: account planning, briefing rules, who decides what, fees or commission, and how the agency is reviewed.

## Do Not Use When

- `meta-budget-planner` for splitting a confirmed total marketing budget across content, tools and staff.
- `media-planning` for schedules, weights, reach and frequency.
- `advertising-attribution-and-measurement` for attribution design or reading results; full business plans go to business-plan-skills and VAT or accounting treatment of ad spend to chwezi-accounting-doctrine.
- Stop if no one with budget authority is named; return a draft only.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business objective, product, market and period | Client brief or accountable owner | Yes | Stop and ask; do not invent an objective |
| Revenue, forecast sales and gross margin | Client finance owner | Yes for % of sales and break-even | Use objective-and-task only; label the % method `not assessed` |
| Customer, category and competitor evidence (share, spend, ad activity) | Client data, Meta Ad Library, media monitoring, research | Conditional | Mark share-of-voice `not assessed`; state the evidence to collect |
| Cost assumptions (CPM, CPL, production quotes) | Client history, rate cards, supplier quotes | Conditional | Use labelled ranges from the client's own history; never market "benchmarks" from memory |
| Approval limits and decision owner | Client | Yes for execution | Draft only; no booking, spend or account change |

## Workflow

1. Frame the decision: write the purpose line (problem, market, deadline) and confirm the decision owner. Stop if the owner or objective is missing.
2. Build the objective hierarchy: business objective → marketing objective → advertising (communication and behaviour) objective, each SMART and location-specific (see [objectives and measurement](references/objectives-and-measurement-architecture.md)).
3. Write the four-level measurement plan (message, communication, media, business) and name the operations-readiness checks that isolate advertising from operational failure.
4. Triangulate the budget with three methods, set a minimum-effective floor and a diminishing-returns ceiling, then reconcile (see [budget triangulation](references/budget-triangulation-and-allocation.md)). If the methods disagree by more than the client can explain, stop and present the gap rather than averaging it away.
5. Allocate in two phases: by activity (media, production, research, contingency with a stated purpose), then by segment, geography, timing and test cells.
6. Prepare the answers to the three budget questions: what do we get, what if we add X%, what if we cut X%.
7. If a decision is needed, write the six-part decision memo (see [decision memo and governance](references/decision-memo-and-agency-governance.md)).
8. Define governance: briefing rules, one decision-maker, compensation model, review cadence, agency evaluation.
9. Run the quality gates and the anti-slop gate; correct failures and rerun before handoff. Withhold any figure that has no source.

## Budget in one table

Present every recommendation like this (illustrative figures):

| Method | Logic | Figure (UGX m/yr) |
|---|---|---|
| % of forecast sales | Forecast 2,400m × assumed 4% (client history, labelled) | 96 |
| Objective-and-task | Reach and leads needed × cost assumptions + production + research + contingency | 118 |
| Share-of-voice check | Estimated category spend × target SOV | 110 |
| **Recommended** | Objective-and-task, phased; floor 80, ceiling 140 | **115** |

Floor = the minimum effective level below which the plan concentrates rather than spreads. Ceiling = the point past which extra spend buys mostly repeat exposure to the same people.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Advertising strategy and budget recommendation | Client decision-maker | Objective hierarchy, three-method budget table, floor, ceiling, two-phase allocation and answers to the three budget questions are present |
| Four-level measurement plan | Client, analyst, media team | Every level has a metric, source, baseline or `not assessed`, and a decision rule |
| Decision memo (when requested) | Senior approver | Six parts, three markedly different options including do-nothing, committed recommendation, action plan with UGX, dates and approvals |
| Governance and compensation note | Client and agency leads | Decision rights, briefing and approval rules, compensation basis and review cadence are explicit |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Assumption and source register | Table | Each cost, share and revenue figure has a source and date or is labelled an assumption |
| Budget reconciliation table | Table | Shows each method's figure, the gap and the reason for the chosen number |
| Release checklist | Checklist | Anti-slop, legal/market gate (where applicable) and approval status recorded |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Booking media, contacting suppliers or signing agreements needs the same authority, and legal, tax and accounting conclusions are out of scope; route them.

## Degraded Mode

Without sales, margin, competitor or cost data, return the narrowest qualified result and mark the affected checks `not assessed`. An objective-and-task budget with labelled assumptions, the floor/ceiling logic and a list of the evidence needed can still be delivered; never convert an unavailable method or metric into a pass.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Budget is below the minimum-effective level for the full scope | Concentrate on fewer markets, audiences or months | Spreading a sub-threshold budget so nothing registers |
| The three methods disagree widely | Show the gap and the assumption that drives it; ask the owner to choose | False precision from averaging |
| Growth objective and share of voice below share of market | Flag the SOV gap; test the higher-spend case in a cell | Expecting growth while under-weighted |
| Website, stock or response capacity not ready | Delay launch or add an operations fix to the plan | Advertising blamed for operational failure |
| Client asks for "more research" instead of a decision | Recommend at 60–80% confidence with a test and contingency | Paralysis and missed windows |
| A figure has no source | Label it assumption or remove it | Invented benchmarks in a client document |

## Quality Standards

- Objectives are SMART, name the place (district, town, county) and a baseline with source and date.
- Budget shows three methods, a floor, a ceiling and a purposeful contingency; currency UGX (or the named market's) with the FX date for any conversion.
- Measurement covers all four levels and includes operations readiness and stakeholder side-effects.
- Recommendations commit; options are markedly different; the status-quo option is always present.
- British English, plain language, no hype. Every benchmark is the client's own or sourced.
- The readiness checklist before recommending spend ([core method and handoffs](references/core-method-and-handoffs.md)) is complete, including the legal/market release gate for regulated categories.

## Anti-Patterns

- Budgeting by habit ("what we spent last year"). Fix: triangulate three methods and state floor and ceiling.
- Spreading a small budget across every district and month. Fix: concentrate until the minimum-effective level is met.
- Crediting or blaming advertising for a website crash or stock-out. Fix: add operations-readiness checks and holdouts.
- Options that are variations of one idea. Fix: present three markedly different options, one of them hold/monitor.
- Media chosen for the chief executive's hobby. Fix: choose from audience evidence with a written rationale.
- Treating a US category advertising-to-sales ratio as a local fact. Fix: label it an assumption or use the client's own history.

## References

- [Objectives and measurement architecture](references/objectives-and-measurement-architecture.md): read when writing objectives or the measurement plan.
- [Budget triangulation and allocation](references/budget-triangulation-and-allocation.md): read when any budget figure is about to be proposed.
- [Decision memo and agency governance](references/decision-memo-and-agency-governance.md): read when writing memos or setting compensation models and agency–client rules.
- [Core method, worked example and handoffs](references/core-method-and-handoffs.md): read when building the objective hierarchy, handing outputs to neighbour skills, drafting client sentences or running the readiness checklist.
- [Media planning](../media-planning/SKILL.md), [attribution and measurement](../advertising-attribution-and-measurement/SKILL.md), [direct-response economics](../direct-response-economics/SKILL.md) and [creative brief and big idea](../creative-brief-and-big-idea/SKILL.md): read when handing the budget, measurement plan or single message downstream.
- [Marketing budget planner](../../meta-analytics-ops/meta-budget-planner/SKILL.md): read when the question is the whole marketing budget; [legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when the category is regulated.
<!-- dual-compat-end -->

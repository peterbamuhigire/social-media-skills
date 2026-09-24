---
name: advertising-strategy-and-budget
description: Use when setting advertising objectives, a four-level measurement plan, a triangulated budget with floor and ceiling, allocation phases, a decision memo or agency governance terms; use media-planning for schedules and weights, meta-budget-planner for whole-marketing allocation.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Advertising Strategy and Budget

Turn a business problem into an advertising strategy the client can approve: one objective hierarchy, one measurement architecture, a budget that three methods agree on, and clear governance for the agency–client relationship. The skill plans and recommends. It never spends money or changes a live account.

<!-- dual-compat-start -->
## Use When

- A client asks "how much should we spend on advertising, on what, and how will we know it worked?"
- An advertising plan, annual media budget, launch budget or competitive-response budget is needed.
- A budget change, competitive intrusion or campaign pivot needs a decision memo the client can approve quickly.
- The agency–client arrangement needs defining: account planning, briefing rules, decision rights, compensation model and agency evaluation.

## Do Not Use When

- The job is splitting a confirmed total marketing budget across all functions (content, tools, staff); use [meta-budget-planner](../../meta-analytics-ops/meta-budget-planner/SKILL.md).
- The job is scheduling, weights, reach and frequency; use [media-planning](../media-planning/SKILL.md).
- The job is attribution design or reading results; use [advertising-attribution-and-measurement](../advertising-attribution-and-measurement/SKILL.md).
- The job is a full business or marketing plan document; route to business-plan-skills. Tax, VAT and accounting treatment of ad spend route to chwezi-accounting-doctrine.
- Stop if no one with budget authority is named: return a draft only.

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

## Outputs

| Artefact | Consumer | Observable acceptance condition |
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

Read and search supplied files and authorised evidence. Planning and analysis are read-only. Booking media, spending, changing ad accounts, contacting suppliers or signing agreements requires explicit, action-specific authority from the client. Legal, tax and accounting conclusions are out of scope; route them.

## Degraded Mode

If sales, margin, competitor or cost data are unavailable, return the narrowest qualified plan: objective-and-task budget with labelled assumptions, the floor/ceiling logic, and a list of the evidence needed. Mark each unavailable method or metric `not assessed`; never convert it into a pass.

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

## Anti-Patterns

- Budgeting by habit ("what we spent last year"). Fix: triangulate three methods and state floor and ceiling.
- Spreading a small budget across every district and month. Fix: concentrate until the minimum-effective level is met.
- Crediting or blaming advertising for a website crash or stock-out. Fix: add operations-readiness checks and holdouts.
- Options that are variations of one idea. Fix: present three markedly different options, one of them hold/monitor.
- Media chosen for the chief executive's hobby. Fix: choose from audience evidence with a written rationale.
- Treating a US category advertising-to-sales ratio as a local fact. Fix: label it an assumption or use the client's own history.

## References

- [Objectives and measurement architecture](references/objectives-and-measurement-architecture.md) — read when writing objectives or the measurement plan.
- [Budget triangulation and allocation](references/budget-triangulation-and-allocation.md) — read before any budget figure is proposed.
- [Decision memo and agency governance](references/decision-memo-and-agency-governance.md) — read for memos, compensation models and agency–client rules.
- [Media planning](../media-planning/SKILL.md), [attribution and measurement](../advertising-attribution-and-measurement/SKILL.md), [direct-response economics](../direct-response-economics/SKILL.md), [creative brief and big idea](../creative-brief-and-big-idea/SKILL.md).
- [Marketing budget planner](../../meta-analytics-ops/meta-budget-planner/SKILL.md); [legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md).
<!-- dual-compat-end -->

## Core method

### 1. The objective hierarchy

Advertising cannot fix a price, product or distribution problem. State which problem advertising is being asked to solve before any spend.

| Level | Question | Example (illustrative, Kampala) |
|---|---|---|
| Business | What must change in revenue, margin or share? | Grow weekday covers at a Kololo restaurant from 60 to 90 a day by 31 March |
| Marketing | Which customer behaviour produces that? | Office workers within 3 km book weekday lunch |
| Advertising – communication | What must they know, feel or believe? | "Lunch here takes 40 minutes, door to door" |
| Advertising – behaviour | What must they do? | Book via WhatsApp or the booking link |

Slot template: "Increase [metric] from [baseline, date, source] to [target] among [segment] in [place] by [date], through [2–3 value themes] delivered via [channels], within [UGX budget], measured by [method]."

### 2. The four-level measurement architecture

Adapted from Kelley and Sheehan (c. 2021–22) *Advertising Management in a Digital Environment*, Routledge. A campaign cannot win on one level and lose on another and still be called a success.

| Level | What to measure | Typical sources |
|---|---|---|
| Message | Is the message built on a real insight; do people play back the key message and link it to the brand? | Pre-test, directional split test, intercepts |
| Communication | Awareness (unaided, aided), consideration, attribute change, by demographic | Tracking waves, polls, brand-lift studies where available |
| Media | Delivery vs plan: impressions, reach, frequency, CPM, clicks, engagement, earned reach | Platform exports, post-buy, monitoring |
| Business | Trial, repeat, basket, margin, pricing power, incremental sales vs control | CRM, POS, mobile-money records, holdouts |

Add operations readiness (site uptime, stock, response time) and stakeholder side-effects (staff, dealers). Test message separately from execution.

### 3. Budget in one table

Present every recommendation like this (illustrative figures):

| Method | Logic | Figure (UGX m/yr) |
|---|---|---|
| % of forecast sales | Forecast 2,400m × assumed 4% (client history, labelled) | 96 |
| Objective-and-task | Reach and leads needed × cost assumptions + production + research + contingency | 118 |
| Share-of-voice check | Estimated category spend × target SOV | 110 |
| **Recommended** | Objective-and-task, phased; floor 80, ceiling 140 | **115** |

Floor = the minimum effective level below which the plan concentrates rather than spreads. Ceiling = the point past which extra spend buys mostly repeat exposure to the same people.

### 4. Governance in brief

- One accountable decision-maker attends the briefing and each key review.
- The brief is an agency–client agreement; mid-stream changes are renegotiated in writing.
- Compensation basis is explicit (see reference); media spend passes through and is not agency revenue.
- Review cadence: monthly performance, quarterly strategy, annual agency evaluation both ways.

## Worked example (illustrative, not client evidence)

A Mukono secondary school wants 120 more Senior 1 boarding applications for Term 1. Objective-and-task: 120 completed applications ÷ assumed 20% application-to-enquiry rate = 600 enquiries; at an assumed UGX 12,000 cost per enquiry from the school's last intake = UGX 7.2m media, plus UGX 2.5m production, UGX 0.5m research (parent intercept poll), 5% contingency for an opportunistic radio deal. % of sales cross-check: 120 × annual fee margin × the school's historic marketing share. Floor: one district and two stations with enough weight to be heard; if the budget falls below it, drop the second district. Measurement: enquiries by coded WhatsApp keyword and radio mention code; completed applications from the admissions register; parent awareness poll at open day.

## Handoffs

| Output | Goes to | What is handed over |
|---|---|---|
| Objective hierarchy and budget floor | [media-planning](../media-planning/SKILL.md) | Target audience, period, budget by phase, delivery goal |
| Single message and insight | [creative-brief-and-big-idea](../creative-brief-and-big-idea/SKILL.md) | Objective, audience mindset, current perception, proof |
| Measurement plan | [advertising-attribution-and-measurement](../advertising-attribution-and-measurement/SKILL.md) | Value event, economics inputs, test cells |
| Landing and conversion needs | [ad-to-site-journey-handoff](../ad-to-site-journey-handoff/SKILL.md) | Offer, message, conversion events, owners |
| Tax, VAT, accounting treatment of spend | chwezi-accounting-doctrine (via the engine routing table) | Budget table and invoice sources |
| Full marketing or business plan document | business-plan-skills | Advertising section and assumptions |

## Sentence bank for client documents

- "The plan asks advertising to do one job: [communication or behaviour objective]. Price, product and distribution issues sit outside it and are listed in the risks."
- "We will judge the campaign at four levels. If people like the advertising but cannot say what it offered or who it was from, we will fix the message before adding weight."
- "Below UGX [floor] a month the plan is concentrated on [scope]; above UGX [ceiling] extra spend mostly repeats exposure to people already reached."
- "The three budget questions, answered: for UGX [x] you get [delivery and expected result range]; at +20% we add [element]; at −20% we drop [element] first."
- "We recommend [option]. If [trigger] happens by [date], we will [action] within [days]."

## Readiness checklist before recommending spend

- [ ] Decision owner and approval limits named.
- [ ] Objective hierarchy written; each level SMART and located.
- [ ] Three budget methods computed; floor and ceiling stated.
- [ ] Operations readiness checked (site, stock, response capacity).
- [ ] Measurement plan covers four levels with sources.
- [ ] Compensation basis and pass-through of media spend stated.
- [ ] Legal/market release gate run for regulated categories (alcohol, betting, medicines, financial products, children, political).

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

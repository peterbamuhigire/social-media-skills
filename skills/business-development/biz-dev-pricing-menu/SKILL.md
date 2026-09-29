---
name: biz-dev-pricing-menu
description: Use when an agency must decide what to charge or how to package its services, or a wary prospect needs a low-risk first engagement; produces a tiered service menu with add-ons, a private pricing rationale and objection guide, and a risk-reversed test offer; not for one client's full scope and terms (use `biz-dev-proposal`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Services and Pricing Menu Generator

Produces two documents from one set of inputs: a client-facing services menu (three tiers, add-ons, pricing notes) and a consultant-only pricing rationale guide, plus a risk-reversed test offer when a prospect will not yet sign a retainer. Prices default to UGX with a USD equivalent.

<!-- dual-compat-start -->
## Use When
- We don't know what to charge and want Starter, Growth and Premium packages with clear inclusions and add-ons, priced in UGX or KES.
- We need a private rationale for our rates: cost to serve, how to justify them, answers to price objections and when to walk away.
- Clients keep choosing the cheapest tier and we want a path to move them up.
- A prospect will not sign a retainer and we want a risk-free test campaign offer: result guarantee, pay-per-appointment, revenue share or deferred fee, with a one-page offer and an expectations sign-off.

## Do Not Use When
- `biz-dev-proposal` for a full proposal and statement of work for one named client.
- `direct-response-economics` for break-even, margin and allowable cost-per-acquisition maths on a client's product.
- `biz-dev-positioning` for the niche and promise the prices should reflect.
- Stop before publishing prices or guarantees the consultant has not approved; never promise a result the offer terms cannot back.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Consultant name (personalises Document 2) | Consultant | Yes | Ask; leave `[Consultant Name]` visible until supplied. |
| Country, for pricing currency | Consultant | Yes | Default to Uganda: UGX pricing with USD equivalent. |
| Services the consultant actually provides | Consultant | Yes | Ask; do not list a service the consultant does not deliver. |
| Current client load (number of active clients) | Consultant | Yes | Omit capacity notes and flag the gap. |
| Years of experience | Consultant | Yes | Write the rate justification without experience claims. |
| Cost-to-serve sheet, approved price ranges and any guarantee terms | Consultant; `playbook-agency-operations` growth roadmap; finance engine margin check | Conditional | Show the indicative ranges as unapproved drafts and mark margin `not assessed`. |

## Workflow

1. Confirm who the menu is for and the approval boundary; route a one-client scope to `biz-dev-proposal`, product break-even maths to `direct-response-economics`, and an unsettled niche to `biz-dev-positioning`.
2. Ask the intake questions in the [build method](references/pricing-menu-build-method.md#required-input); stop until the services and country are confirmed.
3. Draft Document 1: introductory paragraph, the Starter, Growth and Premium tiers with inclusions, exclusions and monthly investment, the add-on list and the pricing notes.
4. Apply the menu design rules before publishing Document 1: at most three core programmes, aligned rows, buyer-situation tier names, one true badge, a named contact and WhatsApp route below the table.
5. Price from the cost-to-serve sheet and value delivered, then check margin with the finance engine; pair each programme's fast-signal component with a slow-compounding one.
6. Draft Document 2 (internal only): rate justification, the five objection responses, the Starter-to-Growth path and the walk-away signals.
7. If the prospect will not commit to a retainer, build the 7–10-day [risk-reversed entry offer](references/risk-reversed-entry-offer.md) instead of discounting.
8. Check both documents against the Quality Standards and the `anti-ai-slop` gate; correct any unsourced salary or market figure, untrue badge or unbacked guarantee and rerun the check. Stop before publishing prices or guarantees the consultant has not approved.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Document 1: `# Services Menu — [Agency Name]` (three tiers, add-ons, pricing notes) | Prospects and clients | A client can self-select without a conversation; exclusions are specific; exchange-rate caveat present. |
| Document 2: `# Pricing Rationale Guide — For [Consultant Name]` | Consultant only | Marked internal-use only; five objections, upgrade path and walk-away signals present. |
| Risk-reversed test offer: one-page offer and expectations sign-off (when needed) | Wary prospect | One of five structures chosen; the fee, not an outcome promise, carries the risk. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Price basis note | Table: tier or add-on, cost to serve, value rationale, margin check | Every price traces to the cost-to-serve sheet or is labelled indicative and unapproved. |
| Figure source log | Table: figure, source, date | Salary, exchange-rate and market figures carry a current, dated source or are removed. |
| Menu design check | Checklist | The six menu design rules marked pass or fail. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Prices and guarantees go out only after the consultant approves them.

## Degraded Mode

Without the consultant's approved price ranges and cost to serve, return the narrowest qualified result and mark the affected checks `not assessed`. The tier structure, inclusions, exclusions and Document 2 guidance can still be delivered, with the indicative UGX ranges labelled as unapproved.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A new prospect will not yet commit to a retainer | Build a 7–10-day risk-reversed test offer from the risk-reversed entry offer reference (one of five structures, one-page offer, expectations sign-off), then move a successful test onto a menu programme. | Discounting the menu to win a sceptical first client, or promising outcomes instead of putting the fee at risk. |
| Pushed on price | Explore scope reduction first ("start with the Starter package and add platforms once we have proven the results"); if discounting, trade term length, prepayment or case-study rights and show old price, new price and saving with the real reason. | Eroding the rate card with silent discounts. |
| More than three core programmes, or unrelated items in one table | Keep three core programmes (Nelson, 2019); move audits, training and add-ons to a separate list or tab. | A menu the buyer cannot compare. |
| A badge or "most chosen" claim is proposed | Use one badge only, and only if literally true. | A false claim on the price page. |
| Justifying the rate against an in-house hire | Use a current, dated local salary source plus training, management time and tools; if none is available, ask the client what the role would cost. | Quoting a remembered salary range. |
| The client has sales data | Use Bodnar and Cohen's (2012) ROI formula: (Total Lead Value − Cost of Customer Acquisition) ÷ Cost of Customer Acquisition. | Arguing on cost instead of value. |
| The enquiry shows a walk-away signal (guaranteed follower or sales numbers, daily promotional posts only, three agencies in 12 months, constant same-day demands, no agreement or deposit) | Decline or disengage. | A future dispute and reputational damage. |
| The client proposes payment by results, commission on media or a "results only" fee, or the pay model is under review | Choose the model with [remuneration models and evidence](references/remuneration-models-evidence.md): base fee covering cost-to-serve plus a capped, measurable bonus; cite ISBA 2024 (27% said PBR improved agency performance, register `ISBA-REMUNERATION-2024`) as a caution, not a benchmark. | Cash-flow risk from fees tied to outcomes the agency does not control. |
| A Starter client reaches month 3 | Present a results summary, name one gap Growth would close, and offer a 90-day Growth trial. | A generic upsell or an open-ended ask. |

## Quality Standards

- All three tiers are clearly differentiated in scope, volume, and price; a client can self-select without a conversation.
- "What is NOT included" sections are honest and specific, not defensive in tone.
- Add-ons are priced individually so clients can build their own package.
- Pricing notes include the exchange rate caveat as specified.
- Objection responses are conversational, confident, and non-defensive, not scripts to be read verbatim.
- Red flags list is practical and actionable; each item has a clear reason.
- Document 2 is clearly marked as internal-use only.
- The menu has no more than three core programmes, aligned rows, one true badge, a contact route under the table and no unsourced salary or market figures.

The ninth release check (Starter-to-Growth upsell guidance) is in the [build method](references/pricing-menu-build-method.md#additional-release-check).

## Anti-Patterns

- Showing a single option or naming tiers "Basic/Pro". Fix: three aligned options named by the buyer's situation or outcome, with the preferred programme in the middle.
- Burying the price where the buyer expects it. Fix: in conversation go problem, cost to profit, solution, price; on a premium site show ranges on an "Investment" page.
- Treating Nelson's anecdote that clients chose his top package unprompted as a planning rate. Fix: plan from cost to serve and value; treat it as one agency's anecdote.
- Treating "leading with the dearest plan raises revenue per visitor" as a rule. Fix: test it as a hypothesis (Wiebe, 2011).
- Promising guaranteed follower counts or sales. Fix: put the fee at risk through a risk-reversed offer, never the outcome.
- Accepting a one-month trial of the full retainer. Fix: recommend a three-month minimum with clear milestones.

## References

- [Pricing menu build method](references/pricing-menu-build-method.md): read when writing the tiers, add-ons, pricing notes, menu design rules, rate justification, objection responses, upgrade path or walk-away signals.
- [Risk-reversed entry offer](references/risk-reversed-entry-offer.md): read when a prospect needs a low-risk first engagement (result guarantee, pay-per-appointment, revenue share or deferred fee) before any retainer.
- [Remuneration models and evidence](references/remuneration-models-evidence.md): read when choosing between retainer, fixed fee, unit, commission, payment-by-results, value-based or hybrid pay, or reviewing a pay model at renewal.
- [Agency growth roadmap](../../playbooks/playbook-agency-operations/references/agency-growth-roadmap.md): read for the paths table, cost-to-serve sheet and programme design behind the prices.
- [`biz-dev-positioning`](../biz-dev-positioning/SKILL.md): read when the niche and promise the prices reflect are not settled.
- [`biz-dev-proposal`](../biz-dev-proposal/SKILL.md): read when one named client needs a full scope and terms.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the client-facing menu copy.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

---
name: direct-response-economics
description: Use when a client asks whether a flyer, SMS, WhatsApp broadcast, lead-ad, catalogue or direct-mail campaign will pay; produces a campaign P&L with orders-per-thousand break-even, a list and test plan, a roll-out ladder and a lead requirement; not for multi-channel attribution or incrementality (use `advertising-attribution-and-measurement`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Direct-Response Economics

Proves, before spending, that a response campaign can make money: what each order is worth after every variable cost, how many orders per thousand contacts are needed to break even, which lists and media are worth testing, and how to move from a small test to a full roll-out. Method adapted from Stockwell and Shaw (1994) *Direct Marketing Checklists*, NTC Business Books, rebuilt for mobile money, WhatsApp, SMS and lead ads, with a data-protection overlay the book lacked.

<!-- dual-compat-start -->
## Use When

- We plan a flyer drop, SMS blast, WhatsApp broadcast, lead-ad, catalogue or direct-mail pack; will it pay?
- The test came back; decide whether to retest, extend, balance or roll out to the full list.
- Our sales team can handle so many calls a week; how many leads and how much media reach do we need?
- Plan how enquiries are handled, what goes in with the order and which back-end offers follow.
- Rate which contact lists and media are worth testing first.

## Do Not Use When

- `advertising-attribution-and-measurement` for multi-channel attribution or incrementality.
- `direct-response-funnel-copy` or `ad-copy-and-hook-lab` for the letter, message or ad copy itself; company pricing, margins and accounting go to chwezi-accounting-doctrine.
- Stop if the contact list has no lawful basis for marketing under Uganda DPPA 2019 or the local equivalent; fix consent before any send or spend.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Offer, price, discounts and payment terms | Client | Yes | Stop; request them |
| Cost of goods, handling, delivery, premium, overhead share | Client finance or operations owner | Yes | Label each as an assumption; show sensitivity |
| Returns, refusals (cash on delivery, failed mobile-money collection) and bad-debt history | Client records | Conditional | Use a conservative labelled assumption; mark `not assessed` |
| Cost per thousand contacts by medium | Supplier quotes, platform history | Yes | Compute break-even for two or three cost scenarios |
| List or audience source and consent evidence | Client data owner | Yes for owned-list campaigns | Stop the list activity; plan consented list-building instead |

## Workflow

1. Confirm offer, audience, medium and goal hierarchy (Goal 1 profit, Goal 2 support goals, Goal 3 by-products); stop if management goals conflict and are unranked.
2. Screen product suitability for direct response (see [P&L and break-even](references/campaign-pnl-and-break-even.md)).
3. Build the pro-forma P&L per order: price, cost of sales, overhead, returns, bad debt → net profit per order.
4. Compute orders per thousand contacts needed to break even for each medium's cost per thousand.
5. Rate each list or audience (1–10) and confirm lawful basis; drop any list without it (see [lists, testing and roll-out](references/lists-testing-and-rollout.md)).
6. Design the test: smallest readable cells, one variable, coded response, read horizon.
7. Decide per cell: retest, extend, balance, roll out or stop, using cost per order and selling cost %.
8. Plan inquiry handling and back-end revenue (see [inquiries and back end](references/inquiries-back-end-and-formats.md)).
9. Run the quality, legal/market and anti-slop gates; correct and rerun. Withhold the plan if the list is unlawful or the break-even is unrealistic.

## Break-even in one line

Orders per thousand to break even = marketing cost per thousand contacts ÷ net profit per order. A worked UGX example is in [worked example, goal hierarchy and handoffs](references/worked-example-goals-and-handoffs.md).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Campaign P&L and break-even sheet | Client owner, finance | Net profit per order and orders per thousand to break even shown for each medium |
| List and medium test plan | Client and campaign team | Cells, sizes, codes, read horizon and decision ladder defined |
| Lead requirement model | Sales manager | Capacity-to-leads-to-reach arithmetic with sources |
| Inquiry and back-end plan | Operations and sales | Response kit per inquiry type and back-end offers listed |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Cost and rate assumption register | Table | Each input sourced or labelled |
| Lawful-basis record for each list | Table | Source, collection date, consent or basis, opt-out handling |
| Test log with decisions | Table | Result, cost per order, selling cost %, decision and reason |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Sending messages, buying or renting lists or uploading customer data to platforms also needs a lawful basis; legal conclusions route to counsel and tax to the finance engine.

## Degraded Mode

Without cost or response-history data, return the narrowest qualified result and mark the affected checks `not assessed`. The P&L template with labelled assumptions and a sensitivity table (break-even at low, expected and high cost) can still be delivered; never present a break-even based on invented costs as a forecast.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| List has no lawful basis for marketing (bought, scraped, rented without consent) | Do not use it; build a consented list or partner-mailed offer | Breach of Uganda DPPA or Kenya DPA duties (register PL-01, PL-02) |
| Break-even response exceeds any plausible rate for the medium | Change offer, price, cost or medium before testing | Testing a campaign that cannot pay |
| Test result near break-even | Retest the same size before extending | Rolling out on noise |
| Tailoring a segment costs more than its likely incremental sales | Merge or drop the segment | Unprofitable segmentation |
| Returns or refusals above assumption | Recompute net profit per order; tighten qualification | Hidden losses |
| Sales capacity is the bottleneck | Add qualifying friction to lead capture | Flooding sales with low-intent leads |

## Quality Standards

- Every campaign has a P&L with returns, bad debt and premiums costed.
- Break-even is stated as orders per thousand and as a percentage.
- Tests are coded per list and medium; decisions follow the ladder.
- Lawful basis and opt-out handling are recorded for every owned or partner list.
- Figures in UGX or the named currency; illustrative figures labelled.
- The readiness checklist before any send or spend ([worked example, goal hierarchy and handoffs](references/worked-example-goals-and-handoffs.md)) is complete, including ranked goals and the legal/market gate for regulated offers.

## Anti-Patterns

- Judging a campaign on response rate alone. Fix: compare cost per order with net profit per order.
- Renting or buying contact lists "because competitors do". Fix: consented list-building or partner co-marketing to the partner's own opted-in list.
- Testing the worst list first to "save the good names". Fix: test the best list first; if it fails there, it fails everywhere.
- Rolling out after one good test. Fix: retest, then extend in steps.
- Counting zero-effort leads as success. Fix: value qualified leads and match friction to sales capacity.
- No plan for enquiries. Fix: prepare the response kit before launch.

## References

- [Campaign P&L and break-even](references/campaign-pnl-and-break-even.md): read when a response campaign is about to be approved.
- [Lists, testing and roll-out](references/lists-testing-and-rollout.md): read when choosing lists or reading tests.
- [Inquiries, back end and formats](references/inquiries-back-end-and-formats.md): read when planning response handling, fulfilment inserts or format choice.
- [Worked example, goal hierarchy and handoffs](references/worked-example-goals-and-handoffs.md): read when working the arithmetic, ranking goals, running the readiness checklist or handing over to copy, testing or finance.
- [Advertising strategy and budget](../advertising-strategy-and-budget/SKILL.md) and [media planning](../media-planning/SKILL.md): read when the budget or media plan is the question; [direct-marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md): read when offers, deadlines or list use are drafted.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when the offer is regulated or list consent is in doubt.
<!-- dual-compat-end -->

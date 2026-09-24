---
name: direct-response-economics
description: Use when a response campaign (flyer, SMS, WhatsApp, lead ads, direct mail, catalogue) needs a pro-forma P&L, orders-per-thousand break-even, list rating, roll-out ladder, lead requirement or inquiry economics; use advertising-attribution-and-measurement for attribution and incrementality.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Direct-Response Economics

Prove, before spending, that a response campaign can make money: what each order is worth after every variable cost, how many orders per thousand contacts are needed to break even, which lists and media are worth testing, and how to move from a small test to a full roll-out. Method adapted from Stockwell and Shaw (1994) *Direct Marketing Checklists*, NTC Business Books, rebuilt for mobile money, WhatsApp, SMS and lead ads, with a data-protection overlay the book lacked.

<!-- dual-compat-start -->
## Use When

- A client plans a flyer, SMS, WhatsApp broadcast, lead-ad, catalogue or direct-mail campaign and asks "will it pay?"
- A test result must be turned into retest, extend, balance or roll-out decisions.
- Sales capacity needs converting into a lead requirement and media reach.
- A campaign must decide how to handle enquiries and what to put in outgoing orders (back end).

## Do Not Use When

- The question is multi-channel attribution or incrementality; use [advertising-attribution-and-measurement](../advertising-attribution-and-measurement/SKILL.md).
- The copy itself is needed; use [direct-mail-writer](../../content-writing/direct-mail-writer/SKILL.md) or [ad-copy-and-hook-lab](../ad-copy-and-hook-lab/SKILL.md).
- Company-level pricing, margins or accounting treatment are in question; route to chwezi-accounting-doctrine.
- Stop if the contact list has no lawful basis for marketing use (see Decision Rules).

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

## Outputs

| Artefact | Consumer | Observable acceptance condition |
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

Read and search supplied data. Analysis is read-only. Sending messages, buying or renting lists, uploading customer data to platforms, or processing personal data requires explicit authority and a lawful basis. Legal conclusions route to counsel; tax to the finance engine.

## Degraded Mode

If cost or history data is missing, return the P&L template with labelled assumptions and a sensitivity table (break-even at low, expected and high cost). Mark missing inputs `not assessed`. Never present a break-even based on invented costs as a forecast.

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

## Anti-Patterns

- Judging a campaign on response rate alone. Fix: compare cost per order with net profit per order.
- Renting or buying contact lists "because competitors do". Fix: consented list-building or partner co-marketing to the partner's own opted-in list.
- Testing the worst list first to "save the good names". Fix: test the best list first; if it fails there, it fails everywhere.
- Rolling out after one good test. Fix: retest, then extend in steps.
- Counting zero-effort leads as success. Fix: value qualified leads and match friction to sales capacity.
- No plan for enquiries. Fix: prepare the response kit before launch.

## References

- [Campaign P&L and break-even](references/campaign-pnl-and-break-even.md) — read before any response campaign is approved.
- [Lists, testing and roll-out](references/lists-testing-and-rollout.md) — read when choosing lists or reading tests.
- [Inquiries, back end and formats](references/inquiries-back-end-and-formats.md) — read when planning response handling, fulfilment inserts or format choice.
- [Advertising strategy and budget](../advertising-strategy-and-budget/SKILL.md); [media planning](../media-planning/SKILL.md); [direct-marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md).
<!-- dual-compat-end -->

## Break-even in one line

Orders per thousand to break even = marketing cost per thousand contacts ÷ net profit per order.

## Worked example (illustrative figures, UGX)

Home water-filter kit, price 150,000.
- Cost of sales: goods 40,000 + handling 5,000 + delivery 10,000 + free spare cartridge 5,000 = 60,000.
- Overhead 10% of price = 15,000.
- Returns 5%: return handling (delivery back + handling = 15,000) + refurbishing (12.5% of goods = 5,000) = 20,000; chargeable 5% × 20,000 = 1,000.
- Bad debt or cash-on-delivery refusal 3% × 150,000 = 4,500.
- Total variable cost = 80,500. Unit profit after variable costs = 69,500; × 95% return factor = 66,025; + credit for returned goods (5% × 40,000 = 2,000) → net profit per order ≈ 68,000.
- A5 flyer with estate door-drop ≈ 1,200 per piece → 1,200,000 per thousand → break-even ≈ 17.6 orders per thousand (1.76%).
- Opted-in SMS at an assumed 35 per message → 35,000 per thousand → break-even ≈ 0.5 orders per thousand. Cheap media lower the break-even line, but list quality and consent decide whether the response comes.

## Goal hierarchy (agree before spend)

| Tier | Meaning | Example |
|---|---|---|
| Goal 1 | The big problem management must solve | Direct-response profit at or above company margin |
| Goal 2 | Important supporting goals | Support upcountry agents; cheaper new-product testing |
| Goal 3 | Useful by-products | Build an opted-in WhatsApp list; capture area data on order forms |

Each goal becomes an objective with a value, a date and an approver: "Build an opted-in list of 3,000 Wakiso customers by 30 June, generating UGX 20m in repeat sales within six months, approved by the managing director."

## Readiness checklist before any send or spend

- [ ] Goals ranked and approved (Goal 1, 2, 3).
- [ ] Product suitability screen passed.
- [ ] P&L complete with returns, refusals, bad debt and premium.
- [ ] Break-even orders per thousand computed for each medium.
- [ ] Lawful basis recorded for every list; opt-out route in every message.
- [ ] Test cells coded; read horizon set.
- [ ] Inquiry response kit ready; back-end offer planned.
- [ ] Legal/market gate run for regulated offers.

## Handoffs

| Output | Goes to | What is handed over |
|---|---|---|
| Offer, break-even and response codes | [ad-copy-and-hook-lab](../ad-copy-and-hook-lab/SKILL.md) or [direct-mail-writer](../../content-writing/direct-mail-writer/SKILL.md) | Main benefit, offer terms, deadline and its true reason, codes |
| Test results | [ad-testing-and-scaling](../ad-testing-and-scaling/SKILL.md) | Cell results and ladder decisions |
| Margin and pricing questions | chwezi-accounting-doctrine (via the routing table) | P&L assumptions |

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

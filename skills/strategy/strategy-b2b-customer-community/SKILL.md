---
name: strategy-b2b-customer-community
description: Use when a B2B client or the agency itself needs a retention-first customer strategy covering grading accounts by value, affordable contact plans, account penetration, at-risk alerts, lead handling and key-account plans; use playbook-client-retainer-management for day-to-day retainer delivery.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# B2B Customer Community and Key Accounts

Build a business-to-business marketing system that keeps and grows the best customers first, then acquires look-alikes, with every contact carrying value the customer asked for (Hunter & Tietyen, 1997). Key accounts receive dedicated plans (Marcos, Guesalaga, Hough & Vincent, c. 2025).

<!-- dual-compat-start -->
## Use When

- A B2B client (manufacturer, distributor, professional firm, insurer, SACCO, school group) needs a customer-management section for its marketing plan.
- The agency needs to grade its own retainer clients and decide how much senior attention each can afford.
- Growth must come from existing accounts: more service lines, more buyer groups, more sites.
- A small, knowable target universe (licensed insurers, banks, private hospitals, registered manufacturers) needs a named-account programme.
- A strategic client needs a key-account plan, relationship review or renewal negotiation plan.

## Do Not Use When

- The task is scope, change requests and monthly check-ins for an existing retainer; use `playbook-client-retainer-management`.
- The task is lead scoring rules or sales–marketing service levels only; use `meta-lead-scoring` or `meta-sales-marketing-alignment`.
- The deliverable is a formal tender response; hand over to proposal-skills.
- The client has no customers yet; use `marketing-foundations-stp-positioning` and `traction-channel-bullseye`.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Customer list with 12–24 months of transactions | Client CRM, accounts or sales records | Yes | Build a manual list first; mark grading `not assessed` |
| Written definition of an active customer | Client owner (drafted with this skill) | Yes | Draft one and obtain approval before grading |
| Gross margin and cost to serve (visits, calls, reports) | Client finance; chwezi-accounting-doctrine for method | Yes for contact economics | Use labelled assumptions; withhold the contact matrix as final |
| Customer interview or survey evidence | Client-approved research | Conditional | Plan the value workshop and new-buyer calls |
| Consent and lawful-basis status of contact data | Client data-protection owner | Yes before any outreach | Stop outreach design; route to `biz-dev-lawful-prospecting-outreach` |

## Workflow

1. Write and approve the active-customer definition (time plus money); classify every record as active, at risk, lapsed or former. Stop if the client cannot supply transactions.
2. Find why customers buy: new-buyer calls, defector interviews and a feature-set profile against competitors; keep the four to seven attributes that drive choice.
3. Grade buyer groups by expected value into AA/A/B/C/D, set a sales-expense-to-revenue ceiling per grade and build the contact matrix; recover by shifting visits to calls and digital contact until each grade fits its ceiling.
4. Run a value-based contact workshop (or collect answers in routine calls) to fix content, frequency and channel per grade.
5. Plan penetration with the account cube, assimilation for new customers, early-warning triggers and a market-at-risk calculation.
6. For strategic accounts, build the one-page key-account plan from the reference; withhold any value claim without a baseline and measurement method.
7. Design acquisition last: look-alikes of the best customers, allowable cost per lead, captive-universe lists and closed-loop lead handling.
8. Review quarterly; rerun grading when revenue mix or cost to serve changes.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Active-customer definition and base classification | Client owner, finance | Definition approved; counts per status reconcile to the source list |
| Grade and contact matrix | Sales, account and marketing leads | Each grade's contact cost is within its expense-to-revenue ceiling |
| Retention and penetration plan | Account managers | Cube cells, triggers and owners are named |
| Key-account plan(s) | Account lead and executive sponsor | One page per account with baseline, joint KPIs and decisions required |
| Acquisition plan | Marketing lead | Allowable cost per lead derived from lifetime profit |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Grading workbook | Table or spreadsheet | Grades trace to transaction data or labelled estimates |
| Market-at-risk calculation | Worked table | Uses the client's own problem and repurchase data |
| Research record | Interview and survey log | Named, consented, transaction-linked responses |

## Capability and Permission Boundaries

Read and search supplied customer data and evidence. Analysis and planning are read-only. Contacting customers, surveys, list matching or CRM changes need explicit authority, a lawful basis and registration where the law requires it. Commercial offers to clients need approver sign-off.

## Degraded Mode

Without transaction data, deliver the definition draft, grading method, workshop design and a key-account plan template with every value marked `not assessed`. Never invent revenue or margin per account.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Acquisition is requested before retention is understood | Grade and profile current customers first | Replacing churn with ever more expensive new customers |
| A grade's contact cost breaks its ceiling | Move content from visits to calls and digital, or re-price | Unprofitable service that looks like good relationships |
| A low-revenue account shows high-grade traits | Promote it for a test period | Starving tomorrow's best customers |
| Complaints are rare | Make complaining easy and ask after each delivery | Silent defection |
| A key account supplies over a set share of revenue | Diversify and raise switching value honestly | Dependency and squeeze |
| Value claim has no baseline | Agree the baseline in the first 30 days before claiming results | Unprovable renewal case |

## Quality Standards

- Speak of people and their business problems, never "targets", in client-facing copy.
- Every contact carries value the customer defined; "just checking in" is banned.
- Loyalty is measured by behaviour (recency, frequency, amount, referrals), not liking scores.
- Unsourced statistics from any book (including uncited figures in the KAM literature) never enter deliverables.

## Anti-Patterns

- Lumping retention and acquisition costs together. Fix: budget, staff and measure them separately.
- Grading on last year's sales alone. Fix: grade on expected value and promote under-served look-alikes.
- Multiplying field visits because "clients want face time". Fix: make each visit count with prior calls and digital content.
- Anonymous satisfaction surveys of current clients. Fix: named, transaction-linked questions about repurchase and referral.
- Passing unqualified leads to the field. Fix: call first, qualify buying mode and timing, then send.
- Calling large customers "key" without dedicated investment. Fix: name them large accounts or fund a real plan.

## References

- [Customer grading, contact economics and lifecycle](references/customer-grading-and-contact-economics.md) — read for definitions, grading, contact matrix, cube, market-at-risk, assimilation and acquisition waterfall.
- [Key-account planning and negotiation](references/key-account-planning-and-negotiation.md) — read for strategic accounts, relationship reviews, sponsors and renewal negotiation.
- [Client retainer management](../../playbooks/playbook-client-retainer-management/SKILL.md) — neighbour for retainer delivery.
- [Lawful prospecting and outreach](../../business-development/biz-dev-lawful-prospecting-outreach/SKILL.md) — consent rules for any contact list.
- [Attribution and measurement](../../advertising/advertising-attribution-and-measurement/SKILL.md) — cost-per-lead and allowable-cost links.
<!-- dual-compat-end -->

## Seven self-diagnostic questions (open every B2B plan with these)

1. Have we written down who counts as a customer?
2. Have we segmented on needs and behaviour?
3. Do we know why each segment buys from us?
4. Do we know each customer's economic value?
5. Is there a value-based contact plan per grade?
6. What share of customers defect each year?
7. What product and buyer penetration do we have per account, and how many referrals came last quarter?

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

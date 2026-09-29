---
name: advertising-attribution-and-measurement
description: Use when a client asks which ads really work, disputes platform results or needs proof advertising caused sales; covers attribution models, holdout and geo lift tests, break-even ROAS and allowable CPA; produces a measurement plan, economics sheet and reconciliation report; not for a marketing mix model (use `marketing-mix-modelling`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Advertising Attribution and Measurement

Decides what counts as a result, how credit is assigned across channels, how to prove that advertising caused the change, and what the business can afford to pay for each result. The skill designs and reads measurement; installing tags, changing tracking or processing customer data needs explicit authority.

<!-- dual-compat-start -->
## Use When

- Before launch, agree which conversions count, how each is defined and who owns the data.
- Which channel is actually working? The platforms' numbers do not match our CRM or till.
- Design or read an incrementality test: a holdout group, a geo split or a platform lift study.
- Set the most we can pay per sale or lead: allowable CPA, break-even ROAS and cost-per-lead ceilings.
- Connect offline, shop-floor or WhatsApp sales back to the advertising, including halo effects on other channels.

## Do Not Use When

- `meta-roi-framework` for a full ROI business case or investment justification.
- `marketing-mix-modelling` for a multi-year model of every channel's contribution, Meridian or Robyn, and cross-channel budget allocation.
- `measurement-tracking-plan` for the event map, Consent Mode v2, Conversions API, UTM naming and BigQuery export.
- `meta-reporting` for dashboard layout and the monthly report.
- Stop if customer data would be matched or processed without a lawful basis and client authority.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business objective and the action that creates value | Approved brief | Yes | Stop; request it |
| Gross margin, average order value, repeat rate or lifetime value | Client finance owner | Yes for allowable CPA and break-even ROAS | Label the economics `not assessed`; report cost per result only |
| Tracking inventory (tags, pixels, conversion APIs, CRM fields, WhatsApp labels, POS codes) | Client web or analytics owner | Conditional | List gaps; recommend fixes via [ad-to-site-journey-handoff](../ad-to-site-journey-handoff/SKILL.md) |
| Platform and analytics exports | Client-authorised accounts | Conditional | Mark channel results `not assessed` |
| Consent and privacy position (markets served, CMP, privacy notice) | Client legal or data owner | Yes when EEA/UK/CH traffic or personal data is involved | Flag and route to [measurement-tracking-plan](../../meta-analytics-ops/measurement-tracking-plan/references/consent-mode-and-cmp.md) |

## Workflow

1. Define the value event and its proxies: primary conversion, micro-conversions and the offline or WhatsApp steps (see [conversion events and models](references/conversion-events-and-attribution-models.md)). Stop if the value event cannot be observed at all; recommend the minimum tracking fix first.
2. Audit tracking: what fires, where, deduplication across pixel and server events, consent handling, CRM matching. Record gaps.
3. Set the economics: break-even ROAS, allowable CPA and the lead-cost waterfall (see [economics and incrementality](references/economics-and-incrementality.md)).
4. Choose an attribution view for day-to-day optimisation and state its bias; never present one model as the truth.
5. Choose an incrementality method for the causal question: holdout, geo test, platform lift study or time-series read; rank it on the IAB causal-strength ladder, power the design and choose markets (see [geo power and incrementality hierarchy](references/geo-power-and-incrementality-hierarchy.md)).
6. Plan reconciliation: platform-reported vs analytics vs CRM or POS, with the expected gaps explained.
7. Build the reporting rules: denominators, windows, what is modelled, what is observed.
8. Run the quality and anti-slop gates; correct and rerun. Withhold any claimed result without attributable evidence.

## Core formulas

| Measure | Formula | Note |
|---|---|---|
| ROAS | Attributable revenue ÷ ad spend | State the attribution view |
| Break-even ROAS | 1 ÷ gross margin % | 40% margin → 2.5 |
| Allowable CPA | Gross margin per sale (or chosen share of LTV) ÷ target return multiple | Agree the share of LTV with finance |
| CPA | CPC ÷ conversion rate | UGX 1,500 CPC at 5% → UGX 30,000 (illustrative) |
| Lifetime value (simple) | Average order value × purchases per year × years retained × margin | Use cohorts where possible |
| Time to customer break-even | CAC ÷ monthly contribution per customer | Cash planning |
| Effective CAC with referral | Paid spend ÷ (paid customers ÷ (1 − K)) for K below 1 | K = invitations per user × acceptance rate |
| Echo effect % | Incremental untraced sales ÷ traced campaign sales | Needs a baseline period |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Measurement plan | Client analyst, media team, web owner | Conversion events defined with trigger, source, owner and deduplication rule |
| Economics sheet | Client decision-maker | Break-even ROAS, allowable CPA and cost-per-lead ceilings shown with inputs |
| Incrementality test design | Client and agency | Hypothesis, test and control, duration, primary metric, guard-rail and decision rule |
| Reconciliation report | Client | Platform, analytics and CRM/POS figures side by side with explained variance |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Tracking audit | Table | Each event: fires yes/no/`not assessed`, source of proof, owner |
| Assumption register | Table | Margin, LTV, conversion rates and windows sourced or labelled |
| Test log | Table | Pre-registered line in the sand and result recorded before interpretation |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Installing or changing tags, enabling server-side tracking, uploading customer lists or changing attribution settings also needs a lawful basis, and legal conclusions route to qualified counsel.

## Degraded Mode

Without access to ad accounts or CRM data, return the narrowest qualified result and mark the affected checks `not assessed`. The measurement design, the economics template and a data request can still be delivered; never report platform-claimed conversions as business results without reconciliation.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Platform-reported conversions exceed CRM or POS sales | Report both; investigate windows, view-through credit and duplicates | Over-crediting advertising |
| Most sales close on WhatsApp or offline | Add keywords, codes, "how did you hear" fields and a holdout | Last-click blindness to real sales |
| EEA, UK or Swiss users are targeted with Google tags | Require Consent Mode v2 via a consent platform (register CW-10) | Audience exclusion and non-compliant measurement |
| A channel looks strong only under last-click | Run an incrementality test before scaling | Paying for sales that would happen anyway |
| First-order CPA exceeds first-order margin | Check lifetime value and repeat rate before stopping | Killing a profitable acquisition channel |
| Margin or LTV unknown | Report cost per result only; mark economics `not assessed` | Invented profitability claims |

## Quality Standards

- Every metric has a definition, denominator, window and source.
- Observed and modelled figures are labelled separately.
- Attribution views are described with their bias; causal claims come only from incrementality evidence.
- Offline and WhatsApp outcomes are measured, not assumed.
- Consent and privacy requirements are stated for each market served.
- British English; no benchmark without source and date.

## Anti-Patterns

- Treating platform-reported ROAS as business profit. Fix: reconcile to CRM or POS and use gross margin.
- Declaring the winning channel from last-click data. Fix: state the model's bias and run a holdout or geo test.
- Judging B2B thought leadership on last-click. Fix: add content-influenced conversations and pipeline measures.
- Ignoring halo effects on untraced sales. Fix: estimate the echo effect against a baseline.
- Scaling acquisition while repeat purchase is falling. Fix: pair acquisition metrics with repeat rate and lifetime value.
- Moving the target after the result arrives. Fix: pre-register the line in the sand and the action.

## References

- [Conversion events and attribution models](references/conversion-events-and-attribution-models.md): read when defining events or choosing a model.
- [Economics and incrementality](references/economics-and-incrementality.md): read when setting allowable costs or designing tests.
- [Geo power and incrementality hierarchy](references/geo-power-and-incrementality-hierarchy.md): read when powering a geo test, choosing markets or disclosing a lift result's assumptions.
- [Results reconciliation](references/results-reconciliation.md): read when writing any results summary.
- [Worked example, test template and sentence bank](references/worked-example-and-templates.md): read when pre-registering a test, working an illustrative example or wording a results caveat.
- [Advertising strategy and budget](../advertising-strategy-and-budget/SKILL.md), [media planning](../media-planning/SKILL.md), [direct-response economics](../direct-response-economics/SKILL.md) and [ad-to-site journey handoff](../ad-to-site-journey-handoff/SKILL.md): read when the budget, plan, P&L or landing-page tracking is the real question.
- [Measurement proof pack](../../../docs/evidence-packs/measurement-proof-pack.md): read when assembling evidence for a results claim.
<!-- dual-compat-end -->

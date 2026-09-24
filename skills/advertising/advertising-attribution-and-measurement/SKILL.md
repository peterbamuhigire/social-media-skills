---
name: advertising-attribution-and-measurement
description: Use when defining conversion events, choosing an attribution model, designing holdout or geo incrementality tests, setting break-even ROAS and allowable CPA, or reconciling advertising results; use meta-roi-framework for full ROI business cases and meta-utm-tracking for naming.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Advertising Attribution and Measurement

Decide what counts as a result, how credit is assigned across channels, how to prove that advertising caused the change, and what the business can afford to pay for each result. The skill designs and reads measurement; installing tags, changing tracking or processing customer data needs explicit authority.

<!-- dual-compat-start -->
## Use When

- A campaign needs conversion events, definitions and a measurement plan before launch.
- A client asks "which channel is working?" or disputes platform-reported results.
- An incrementality test (holdout, geo, lift study) must be designed or read.
- Allowable cost per acquisition, break-even ROAS or cost-per-lead ceilings are needed.
- Offline or WhatsApp sales must be connected to advertising, including halo effects.

## Do Not Use When

- The task is a full ROI business case or investment justification; use [meta-roi-framework](../../meta-analytics-ops/meta-roi-framework/SKILL.md).
- The task is UTM naming and campaign register governance; use [meta-utm-tracking](../../meta-analytics-ops/meta-utm-tracking/SKILL.md).
- The task is dashboard layout; use [meta-dashboard-design](../../meta-analytics-ops/meta-dashboard-design/SKILL.md).
- The task is statistical test design for creative variants; use [ad-testing-and-scaling](../ad-testing-and-scaling/SKILL.md) and [meta-testing-framework](../../meta-analytics-ops/meta-testing-framework/SKILL.md).
- Stop if personal data would be processed without a lawful basis and authority.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business objective and the action that creates value | Approved brief | Yes | Stop; request it |
| Gross margin, average order value, repeat rate or lifetime value | Client finance owner | Yes for allowable CPA and break-even ROAS | Label the economics `not assessed`; report cost per result only |
| Tracking inventory (tags, pixels, conversion APIs, CRM fields, WhatsApp labels, POS codes) | Client web or analytics owner | Conditional | List gaps; recommend fixes via [ad-to-site-journey-handoff](../ad-to-site-journey-handoff/SKILL.md) |
| Platform and analytics exports | Client-authorised accounts | Conditional | Mark channel results `not assessed` |
| Consent and privacy position (markets served, CMP, privacy notice) | Client legal or data owner | Yes when EEA/UK/CH traffic or personal data is involved | Flag and route to [meta-analytics-privacy](../../meta-analytics-ops/meta-analytics-privacy/SKILL.md) |

## Workflow

1. Define the value event and its proxies: primary conversion, micro-conversions and the offline or WhatsApp steps (see [conversion events and models](references/conversion-events-and-attribution-models.md)). Stop if the value event cannot be observed at all; recommend the minimum tracking fix first.
2. Audit tracking: what fires, where, deduplication across pixel and server events, consent handling, CRM matching. Record gaps.
3. Set the economics: break-even ROAS, allowable CPA and the lead-cost waterfall (see [economics and incrementality](references/economics-and-incrementality.md)).
4. Choose an attribution view for day-to-day optimisation and state its bias; never present one model as the truth.
5. Choose an incrementality method for the causal question: holdout, geo test, platform lift study or time-series read.
6. Plan reconciliation: platform-reported vs analytics vs CRM or POS, with the expected gaps explained.
7. Build the reporting rules: denominators, windows, what is modelled, what is observed.
8. Run the quality and anti-slop gates; correct and rerun. Withhold any claimed result without attributable evidence.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
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

Read and search authorised exports and documents. Analysis is read-only. Installing or changing tags, enabling server-side tracking, uploading customer lists, changing attribution settings or processing personal data requires explicit authority and a lawful basis. Legal conclusions route to qualified counsel.

## Degraded Mode

Without access to accounts or CRM data, return the measurement design, the economics template and a data request. Mark every result `not assessed`. Never report platform-claimed conversions as business results without reconciliation.

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

- [Conversion events and attribution models](references/conversion-events-and-attribution-models.md) — read when defining events or choosing a model.
- [Economics and incrementality](references/economics-and-incrementality.md) — read when setting allowable costs or designing tests.
- [Results reconciliation](references/results-reconciliation.md) — read before any results summary.
- [Advertising strategy and budget](../advertising-strategy-and-budget/SKILL.md); [media planning](../media-planning/SKILL.md); [direct-response economics](../direct-response-economics/SKILL.md); [ad-to-site journey handoff](../ad-to-site-journey-handoff/SKILL.md).
- [Measurement proof pack](../../../docs/evidence-packs/measurement-proof-pack.md).
<!-- dual-compat-end -->

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

## Worked example (illustrative figures)

A Nairobi bakery sells cakes by WhatsApp. Average order KES 2,400, gross margin 45%, customers reorder about four times a year and stay about two years. Break-even ROAS = 1 ÷ 0.45 ≈ 2.2. First-order margin KES 1,080; lifetime margin about KES 8,600. The team sets an allowable first-order CPA of KES 1,500 (above first-order margin, justified by lifetime value and approved by the owner). Measurement: each ad uses a keyword ("CAKE-TT" for TikTok, "CAKE-FB" for Facebook); staff label WhatsApp chats; a two-week holdout pauses ads in one delivery zone to read the incremental difference.

## Test pre-registration template

| Field | Entry |
|---|---|
| Question | Does [channel/change] cause more [value event] in [segment]? |
| Hypothesis | [Change] will raise [metric] by at least [x] over [period] |
| Design | Holdout / geo / lift study / time series |
| Test and control | [areas or audiences]; how matched |
| Primary metric and source | [metric], [system of record] |
| Guard-rail | [e.g. complaint rate, refund rate, response time] |
| Line in the sand | [target] — source: model maths / client history / own trend |
| Action if hit / missed | [scale] / [stop or redesign] |
| Duration and read date | [dates] |

## Sentence bank

- "This result is correlation, not proof; the geo test starting [date] will separate the advertising effect from the season."
- "Break-even ROAS for this product is [x] because gross margin is [y]%; any channel above it is paying for itself on first order."
- "Platforms each claim the same sale; we report the CRM count as the business result."

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

---
name: marketing-mix-modelling
description: Use when a client wants econometric evidence of what radio, TV, outdoor and digital contributed to sales across years of weekly data, or asks for Meridian or Robyn; produces a marketing mix model specification, calibration plan and governance note; not for day-to-day ad credit or one lift test (use `advertising-attribution-and-measurement`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Marketing Mix Modelling

Decides whether a marketing mix model (MMM) is worth building, specifies the data, the open-source tool (Google Meridian or Meta Robyn) and the experiments that calibrate it, and sets which evidence source governs which budget decision. It serves marketing directors, finance leads and analysts who must move money between channels on evidence that survives a board question.

<!-- dual-compat-start -->
## Use When

- Radio, billboards, TV and online advertising all run together, and finance wants econometrics on which channel drove sales across two or three years of weekly data.
- The annual channel budget should be reallocated on modelled contribution, not on platform-reported conversions.
- An analyst or agency proposes Meridian or Robyn: check data readiness, adstock, saturation and seasonality controls before anything is built.
- A geo test or lift study has finished and its result should calibrate the mix model's priors.
- Platform dashboards, the CRM and the econometric model disagree on channel contribution; set which source governs which budget decision.

## Do Not Use When

- `advertising-attribution-and-measurement` for day-to-day credit models, allowable CPA, reconciliation and the design of a single holdout or geo test.
- `meta-roi-framework` for the board ROI business case, lifetime value and payback of social media.
- `measurement-tracking-plan` for tags, events, Consent Mode v2, Conversions API and UTM naming.
- `advertising-strategy-and-budget` for turning the model's findings into the approved paid-media budget and release phases.
- Stop when the client cannot supply weekly spend and outcomes by channel for the data floor below; return an experiment plan instead and label the MMM `NOT_ASSESSED`.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Weekly (or daily) outcome series: sales, revenue, orders or leads, by geography where available | Client finance, POS, CRM, distributor returns | Yes | Stop the model; return the experiment plan |
| Weekly spend and exposure by channel (spend plus impressions, GRPs, spots, reach and frequency) | Media agency, radio and outdoor invoices, platform exports | Yes | Rebuild from invoices and flighting plans; mark unrecoverable channels `not assessed` |
| Price, promotion, distribution and stock history | Client commercial and supply teams | Yes | List as an omitted-variable risk; widen stated uncertainty |
| External events calendar (holidays, school terms, elections, outages, weather or harvest) | Client, public calendars, register sources | Yes | Build the draft calendar from the reference; client confirms |
| Prior experiment results (geo tests, lift studies) with dates and populations | Client analyst, platform or agency | Conditional | Plan experiments for the largest channels first |
| Authorised data-science route (named analyst, compute, tool licence position) | Client or approved partner | Only for running a model | Deliver the specification and plan only |

## Workflow

1. Frame the decision: which budget, which channels, which horizon and which outcome. Record who will act on the result and what change is in scope (see [triangulation and decision governance](references/triangulation-and-decision-governance.md)).
2. Audit data readiness against the floor: Meridian's documents ask for at least two years of weekly data for a geo model and three for a national model, and at least three years if only monthly data exists (register `GOOGLE-MERIDIAN-COLLECT-DATA`); Robyn's guide asks for at least two years of weekly data (register `META-ROBYN-ANALYST-GUIDE`). Count data points per parameter (register `GOOGLE-MERIDIAN-DATA-AMOUNT`; see [data readiness and specification](references/data-readiness-and-specification.md)).
3. Stop condition: below the floor, or when the major channels cannot be reconstructed week by week, do not specify a model. Return a geo holdout, matched-market or on-off test plan for the largest channel, label MMM `NOT_ASSESSED` and set the date when data will reach the floor.
4. Lock the data specification: one currency (UGX by default) and one exchange-rate method, real or nominal stated, spend net or gross of tax stated, channel grouping, geography list, control variables and the events calendar, including internet shutdowns (register `UG-INTERNET-SHUTDOWN-2026`).
5. Choose the tool and the model form: Meridian (Bayesian, geo-level or national, reach and frequency, ROI priors) or Robyn (ridge regression with Nevergrad hyperparameter search, R production and a beta Python port); record the reason (see [Meridian and Robyn choice](references/meridian-and-robyn-choice.md)).
6. Plan calibration: list which experiment results become priors or calibration targets, check each for recency, duration, granularity, population and estimand fit, and schedule new tests with power analysis and market selection (see [calibration and geo experiments](references/calibration-and-geo-experiments.md)).
7. Set validation and reading rules before any result exists: out-of-sample fit, stability across refits, priors against posteriors, plausible ROI ranges, and what would make the model unfit for budget decisions.
8. Write the governance note: MMM for cross-channel allocation, experiments for causal validation and priors, platform attribution for in-flight optimisation; disclose every assumption. Route budget changes to `advertising-strategy-and-budget`.
9. Review against the quality standards; when a check fails (a missing control, an unexplained ROI, a prior with no source), correct the specification and rerun the readiness and validation checks before hand-over.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| MMM readiness verdict | Client decision-maker | Weeks, geographies, channels and data points per parameter counted; verdict is go, go-with-limits or `NOT_ASSESSED` with a date |
| Data specification | Analyst or data-science partner | Every series has source, unit, currency, grain, owner and gap treatment |
| Calibration and experiment plan | Analyst, media team | Each prior traced to an experiment or stated judgement; each new test has hypothesis, markets, power and duration |
| Validation and reading rules | Analyst, finance | Pass and fail thresholds written before results; ROI ranges and stability checks named |
| Decision-governance note | Marketing and finance leads | Each budget decision mapped to the evidence source that governs it, with assumptions disclosed |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Data inventory and gap log | Table per series | Weeks present, weeks missing, reconstruction method and residual risk |
| Assumption register | Table | Currency, FX, deflator, adstock and saturation choices, priors and controls, each sourced or labelled judgement |
| Source currentness note | List of register IDs | Tool versions and documentation claims dated and cited |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. The engine plans and specifies models and experiments as text deliverables; running Meridian, Robyn or GeoLift code, pulling account data or moving budget is outside that scope unless the client authorises a named data-science route, and finance or accounting treatment routes to the [Chwezi accounting doctrine](https://github.com/peterbamuhigire/chwezi-accounting-doctrine).

## Degraded Mode

Without two or more years of weekly spend and outcomes by channel, return the narrowest qualified result and mark the affected checks `not assessed`. The deliverable becomes an experiment plan (geo holdout, matched-market or on-off test) plus a data-collection specification that reaches the floor, with MMM labelled `NOT_ASSESSED`.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Less than the tool's documented data floor, or data points per parameter well below the tool's guide | Do not specify a model; return the experiment plan and a data-collection timetable | A model that fits noise and misdirects the budget |
| Radio or outdoor spend exists only as annual contracts | Rebuild weekly exposure from flighting plans and invoices; if impossible, treat as a control, not a modelled channel | Crediting radio's effect to digital channels |
| Only one or two clean geographies (for example Kampala and the rest of Uganda) | Prefer a national model with experiments for calibration; do not claim geo-level precision | False precision from too few geos |
| Two channels always move together | Group them, or run an experiment that separates them before modelling | Unstable, swapped ROI estimates from collinearity |
| An experiment result differs from the MMM estimate | Check estimand, timing and population before calibrating; state both figures | Silent overwriting of one source by the other |
| A modelled ROI falls outside the plausible range agreed before results | Treat the model as unfit for that channel until explained; do not reallocate on it | Budget moves on an artefact of the model |
| The client asks for campaign-level answers | Keep MMM at channel level; route campaign questions to experiments or attribution | Lost adstock memory and misleading campaign ROI |

## Quality Standards

- The readiness verdict states weeks, geographies, channels and data points per parameter, with the source of each floor cited.
- One currency, one FX method and a real-or-nominal choice are written in the specification.
- Every control variable has a reason it affects both sales and media timing; outages and holidays are in the events calendar.
- Adstock and saturation are explained in plain words in the client version.
- Each prior names its experiment or judgement, date and fit to the MMM estimand.
- Validation thresholds and plausible ROI ranges were set before any result was read.
- The governance note names the evidence source for each budget decision and lists every assumption.

## Anti-Patterns

- Presenting MMM ROI as proof of causation. Fix: say it is a model estimate and calibrate the main channels with experiments.
- Modelling with digital spend only because radio and outdoor are hard to log. Fix: reconstruct offline exposure or name it as an omitted driver.
- Mixing USD platform invoices and UGX radio invoices without a rule. Fix: lock one currency and one exchange-rate method before building series.
- Choosing the model with the best fit and the most flattering ROI. Fix: select on pre-agreed validation, stability and plausibility rules.
- Treating an internet shutdown week as a collapse in digital effectiveness. Fix: flag outage weeks as events or controls.
- Reallocating the whole budget from one model run. Fix: move money in tested steps and re-check with experiments.
- Promising an MMM to a client with a year of patchy data. Fix: sell the experiment plan and the data-collection work first.

## References

- [Data readiness and specification](references/data-readiness-and-specification.md): read when auditing data, locking the currency or listing controls, and for East Africa data constraints.
- [Meridian and Robyn choice](references/meridian-and-robyn-choice.md): read when choosing the tool, the model form and the validation rules.
- [Calibration and geo experiments](references/calibration-and-geo-experiments.md): read when turning experiments into priors or planning a geo test with power analysis and market selection.
- [Triangulation and decision governance](references/triangulation-and-decision-governance.md): read when deciding which evidence governs which decision and writing assumptions for the client.
- [Advertising attribution and measurement](../advertising-attribution-and-measurement/SKILL.md): read when a single test design, allowable CPA or reconciliation is the real question.
- [Advertising strategy and budget](../advertising-strategy-and-budget/SKILL.md): read when the model's findings must become an approved budget.
<!-- dual-compat-end -->

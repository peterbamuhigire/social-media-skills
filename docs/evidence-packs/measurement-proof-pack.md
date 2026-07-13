# Measurement proof pack

This pack turns a campaign report into reviewable evidence. Use one pack per reporting period or material test. Never substitute platform screenshots for definitions, raw exports or outcome evidence.

## 1. Decision header

| Field | Entry |
|---|---|
| Campaign / period / timezone | |
| Business decision this pack supports | Continue, stop, reallocate, revise or learn |
| Accountable owner and approver | |
| Data cut-off and extraction time | |
| Known limitations | |

## 2. KPI dictionary

| KPI | Funnel stage | Exact formula | Source system/export | Owner | Target/guardrail | Decision use |
|---|---|---|---|---|---|---|
| | | | | | | |

Do not mix platform-defined reach, impressions, views, clicks or engagements without recording each definition. Currency, tax treatment and attribution window must be explicit.

## 3. Evidence ledger

| Evidence ID | Artefact | Provider | Period/version | Storage/reference | Integrity check | Limitation |
|---|---|---|---|---|---|---|
| | Platform export, CRM extract, order ledger, invoice, survey, call log or approval | | | | Row count, totals, checksum or reviewer | |

## 4. Reconciliation

| Control | Expected | Observed | Variance | Status | Resolution |
|---|---:|---:|---:|---|---|
| Spend: platform vs invoice/finance | | | | | |
| Leads: platform vs CRM captured | | | | | |
| Conversions: CRM/orders vs fulfilled/paid | | | | | |
| Revenue: order ledger vs finance-recognised | | | | | |
| UTM/event coverage | | | | | |

Status is `pass`, `fail`, or `not assessed`. State tolerances before seeing the result.

## 5. Calculation table

| Metric | Numerator | Denominator | Calculation | Result | Evidence IDs | Confidence |
|---|---:|---:|---|---:|---|---|
| CTR | Link clicks | Impressions | clicks / impressions | | | |
| Lead CVR | Valid leads | Landing-page sessions or clicks, as defined | leads / denominator | | | |
| CPL | Attributable spend | Valid leads | spend / leads | | | |
| Fulfilment CVR | Paid/fulfilled outcomes | Valid leads | outcomes / leads | | | |
| ROAS | Attributed revenue | Attributable ad spend | revenue / spend | | | |
| ROI | Incremental contribution less campaign cost | Campaign cost | net return / cost | | | |

Use contribution or margin—not gross revenue—when the decision is profitability. If incrementality is not established, label ROAS as attributed, not causal ROI.

## 6. Findings and decisions

| Finding | Evidence | Alternative explanation | Confidence | Decision | Owner/date |
|---|---|---|---|---|---|
| | | | High / medium / low | | |

## 7. Data-quality gate

- Scope, dates, timezone, currency and attribution window match.
- Duplicate, test, spam, cancelled and unpaid records are treated consistently.
- Missingness and late-arriving conversions are quantified.
- Platform totals reconcile to exports; CRM/order totals reconcile to accountable records.
- No personally identifiable data is exposed unnecessarily in the pack.
- Calculations were independently rerun or formula-reviewed.
- Causal language appears only where experiment or credible counterfactual evidence supports it.

If any decision-critical source is unavailable, return the supported calculations, mark the rest `not assessed`, explain the bias and request the exact export or ledger needed.

## Worked example: labelled synthetic data

The figures below demonstrate the proof chain; they are not benchmarks or client results.

Assume evidence `AD-01` records UGX 3,000,000 spend, 1,200,000 impressions and 18,000 link clicks; `CRM-01` records 540 valid leads; `ORD-01` records 81 paid and fulfilled orders worth UGX 12,150,000; `FIN-01` confirms revenue and a 40% contribution margin.

| Metric | Calculation | Result | Evidence | Interpretation |
|---|---|---:|---|---|
| CTR | 18,000 / 1,200,000 | 1.50% | AD-01 | Descriptive platform response only |
| Lead CVR | 540 / 18,000 | 3.00% | AD-01 + CRM-01 | Valid leads per recorded click |
| CPL | 3,000,000 / 540 | UGX 5,556 | AD-01 + CRM-01 | Rounded to nearest shilling |
| Fulfilment CVR | 81 / 540 | 15.00% | CRM-01 + ORD-01 | Paid/fulfilled outcome per valid lead |
| Attributed ROAS | 12,150,000 / 3,000,000 | 4.05× | AD-01 + ORD-01 | Attribution, not incrementality |
| Contribution after ad spend | (12,150,000 × 40%) − 3,000,000 | UGX 1,860,000 | ORD-01 + FIN-01 | Excludes unlisted operating costs |

A release-ready finding would say: “The recorded funnel returned UGX 1.86m contribution after ad spend under the stated 40% margin assumption; incrementality and unlisted operating costs were not assessed.” It would not say “the ads generated UGX 12.15m profit.”

Parent routes: [reporting](../../skills/meta-analytics-ops/meta-reporting/SKILL.md), [metrics framework](../../skills/meta-analytics-ops/meta-social-metrics-framework/SKILL.md), and [ROI framework](../../skills/meta-analytics-ops/meta-roi-framework/SKILL.md).

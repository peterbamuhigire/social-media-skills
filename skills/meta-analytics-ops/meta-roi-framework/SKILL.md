---
name: meta-roi-framework
description: 'Use when a board, finance director or funder asks whether social media pays: return by channel, lifetime value, acquisition cost, retention cohorts and an investment case; produces the ROI model with break-even analysis or the executive business case; not for ad attribution or holdout tests (use `advertising-attribution-and-measurement`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# ROI Framework

Builds the social media ROI model (lifetime value, acquisition cost by channel, break-even and a 12-month projection) or the board business case, in the client's currency (default UGX for Uganda).

<!-- dual-compat-start -->
## Use When

- Finance wants the return per campaign or channel from attributable value and acquisition cost, with a 12-month projection.
- Do customers who came through TikTok, Facebook or Google stay and buy again for longer? Group them by channel and month joined: Week-4 retention, decay curves and lifetime value from GA4 Cohort Exploration.
- Directors or a sceptical board think social media is a waste of money and want the business case for investing: revenue lost to growing competitors, follower value, an A&U study, NPS and budget tiers.
- The team asks when content spend breaks even and whether customer value covers acquisition cost.

## Do Not Use When

- `advertising-attribution-and-measurement` for credit models, allowable CPA and holdout or geo tests on ads.
- `meta-budget-planner` for dividing the budget across channels.
- `marketing-mix-modelling` for a multi-year model of each channel's contribution to sales and cross-channel budget allocation (Meridian or Robyn).
- `meta-reporting` for the periodic performance report.
- Stop when attributable revenue or cost data is missing; state the assumption and never present projections as results.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Average transaction value, transactions per year and relationship length (per segment where values differ) | Client CRM or finance; consultant intake | Yes | Use a conservative single-transaction value as TLV and state that it understates the return. |
| Monthly investment split: retainer, content production, paid ad spend, total | Client finance or agency invoices | Yes | Stop the COCA and break-even steps; request the figures. |
| New customers per month by digital channel, or enquiry volume and conversion rate | CRM records, enquiry log or GA4 | Yes | Use blended COCA, or COCA per enquiry times conversion rate, labelled an estimate; recommend enquiry source tracking. |
| Gross margin % | Client finance | Yes | Mark the break-even step `not assessed`; do not assume a margin. |
| Channel attribution data and chosen attribution model | Enquiry log, UTM reports, client | If channel COCA is wanted | Report blended COCA only and set up the three-step attribution method. |
| Client name, industry, country/city, goal and currency | Client brief | Yes | Default to Uganda / Kampala and UGX; ask for the goal before framing the retainer. |

The full intake list is in [ROI model method](references/roi-model-method.md) § Required Input.

## Workflow

1. Collect the intake; if revenue, cost or customer data is missing, get a reasonable estimate and log it as an assumption. Stop and route to `advertising-attribution-and-measurement`, `meta-budget-planner` or `meta-reporting` when the request is attribution modelling, allocation or a periodic report.
2. Calculate TLV (Bodnar and Cohen, 2012) step by step with the client's figures, per segment where high- and low-value customers differ; use per-channel cohort CLV from [retention-cohorts-and-ltv](references/retention-cohorts-and-ltv.md) when channels retain differently.
3. Calculate COCA per channel (blended where attribution is missing), test the CAC Cap Rule and read the TLV:COCA ratio against the bands below.
4. Set up or check the attribution method (enquiry source log, UTM links, monthly source report) and fix the attribution model before the campaign starts.
5. Calculate break-even customers per month, build the 12-month projection and, where the client forecasts pipeline, the bottom-up model with stage weighting and deal velocity.
6. Write the talking points for the client's actual ratio; for a board that has not yet agreed to fund social media, build the eight-section case in [investment-business-case](references/investment-business-case.md).
7. Check every formula against its inputs and label projections as estimates; correct any mismatch and rerun the affected sections, then run the anti-slop gate before release.

Section templates, worked examples, FRAT scoring and the $20 Rule are in [ROI model method](references/roi-model-method.md).

## Formulas and ratio bands

- TLV = average transaction value × transactions per year × relationship length (years) (Bodnar and Cohen, 2012).
- COCA = monthly social media spend ÷ new customers acquired per month via that channel.
- ROI = (TLV − COCA) ÷ COCA (Bodnar and Cohen, 2012).
- Break-even customers = monthly investment ÷ (TLV × gross margin %), rounded up.
- Monthly ROI = (TLV × customers acquired − monthly investment) ÷ monthly investment × 100.
- CAC Cap Rule (Kahan, 2022): CAC ≤ (CLV × 0.25).

| TLV:COCA | Interpretation | Action |
|---|---|---|
| 10:1 or above | Excellent | Scale the best-performing channel. |
| 5:1 to 9:1 | Healthy and sustainable | Maintain; optimise underperforming channels. |
| 3:1 to 4:1 | Borderline viable | Cut spend on the highest-COCA channel; improve conversion. |
| Below 3:1 | Acquisition cost too high | Grow TLV (price, upsell, retention) or reduce COCA (targeting, funnel). |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Seven-section ROI model (TLV, COCA by channel, ratio, attribution method, break-even, 12-month projection, talking points) | Consultant and client finance lead | Every calculation is shown step by step with the client's figures and every assumption is listed. |
| Break-even statement in plain language | Client decision-maker | Reads "If social media brings in just [X] new customers per month, the investment pays for itself" with the client's numbers. |
| Per-channel cohort CLV or retention report | Consultant; `meta-budget-planner` | Built with the retention reference; Week-4 comparators labelled provisional. |
| Eight-section investment business case | Board, finance committee or funder | Follows the template order and shows conservative and realistic ROI scenarios. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Assumption register | Table: input, value, source, estimate or measured | Every estimated figure (customers, margin, relationship length) is named as an assumption. |
| Attribution method record | Enquiry source log fields and UTM parameters used | The model named is the one fixed before the campaign; blended COCA is labelled an estimate. |
| Calculation workings | Step-by-step tables per section | A reviewer can recompute TLV, COCA, ratio and break-even from the inputs shown. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Using a customer list for FRAT scoring, NPS broadcasts or direct campaigns needs a lawful basis and consent records (register UG-DPPA-2019).

## Degraded Mode

Without attributable revenue or lifetime value and complete costs, return the narrowest qualified result and mark the affected checks `not assessed`. The attribution method, intake assumptions and a break-even target at a stated margin can still be delivered, labelled as projections and never as results.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Channel-level attribution is not available | Use total monthly investment ÷ total new digital customers as blended COCA, label it an estimate and recommend enquiry source tracking. | A per-channel figure the data cannot support. |
| New customer numbers are unknown | Use enquiry volume as a proxy (COCA per enquiry) and apply the client's conversion rate; state every assumption. | Invented customer counts. |
| CAC exceeds 25% of CLV | Treat the programme as structurally unprofitable regardless of gross revenue and say so in the recommendation. | Scaling a programme that loses money on each customer. |
| TLV cannot be calculated (relationship length unknown) | Use a conservative single-transaction value and note that it understates the true return; recommend retention tracking. | An inflated TLV. |
| The client needs per-channel retention or cohort LTV before the ratio can be trusted | Build acquisition or behaviour cohorts with [retention-cohorts-and-ltv](references/retention-cohorts-and-ltv.md) and use per-channel CLV in the TLV:COCA ratio. | A single average CLV hiding one-time-buyer channels. |
| Leadership has not yet agreed to fund social media and asks for a business case | Build the eight-section case with [investment-business-case](references/investment-business-case.md), using this skill's ROI formula for its two scenarios. | An ROI model presented to a board that first needs the risk and investment argument. |
| COCA is above the benchmark | Acknowledge it and name the specific action (grow TLV, improve enquiry-to-sale conversion, or move spend from the underperforming channel). | Deflection that loses the client's trust. |
| The requested outcome is budget allocation or a periodic report | Route to `meta-budget-planner` or `meta-reporting` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- Uses the correct Bodnar and Cohen (2012) formula: ROI = (TLV − COCA) ÷ COCA.
- All calculations are shown step by step with the client's actual figures, not only the final result.
- COCA is calculated per channel where attribution data exists; blended COCA is used and labelled as an estimate where it does not.
- Ratio interpretation names the specific action required at the client's ratio level, not generic advice.
- The attribution section gives the client a practical tracking system to implement, not a conceptual explanation.
- Break-even is expressed in plain language the client can use in a conversation.
- The 12-month projection table is populated with the client's figures and carries a clear caveat about projection assumptions.
- Talking points are specific to the client's ratio and figures, not a generic script; currency follows [ROI model method](references/roi-model-method.md) § Quality criterion kept from the HEAD checklist.

## Anti-Patterns

- Presenting projections as results. Fix: label every forward figure an estimate and revisit the projection quarterly with actual acquisition data.
- Choosing or switching the attribution model after the campaign has run. Fix: select it before launch and apply it consistently for the strategy period (Hanlon and Tuten, 2022).
- Presenting the retainer as a standalone cost. Fix: set it against TLV and the break-even customer count.
- Using one average CLV for every channel. Fix: calculate CLV per acquisition cohort so one-transaction channels show up.
- Counting all pipeline at full value. Fix: weight opportunities by stage (10%, 30%, 60%, 85%, 100%) before forecasting.
- Claiming accounting-level precision from social attribution. Fix: state that the method gives directional understanding, because social content influences sales tracked to other channels.
- Absorbing budget allocation (`meta-budget-planner`) or periodic reporting (`meta-reporting`) into this workflow. Fix: route the neighbouring output and hand over verified inputs.

## References

- [ROI model method](references/roi-model-method.md): read when collecting the intake, building any of the seven sections, modelling revenue bottom-up, or applying FRAT and the $20 Rule.
- [retention-cohorts-and-ltv](references/retention-cohorts-and-ltv.md): read when comparing acquisition or behaviour cohorts, Week-4 retention or LTV by channel.
- [investment-business-case](references/investment-business-case.md): read when a board or funder needs a business case for social media investment.
- [`meta-budget-planner`](../meta-budget-planner/SKILL.md): read when the question becomes spend allocation or the bottom-up revenue plan.
- [`meta-reporting`](../meta-reporting/SKILL.md): read when the output is periodic performance reporting.
- [Measurement proof pack](../../../docs/evidence-packs/measurement-proof-pack.md): read when assembling measurement evidence for release.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting talking points and the business case.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

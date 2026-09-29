---
name: meta-reporting
description: Use when a client needs the monthly performance write-up, a Looker Studio dashboard specification or a quarterly 7 Ps review of social's contribution from verified data; produces the written report, dashboard spec or scored mix review with actions and caveats; not for choosing which KPIs to track (use `meta-social-metrics-framework`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Monthly Social Media Performance Report (Written Document)

Produces the written monthly report a business owner can read without digital marketing expertise, plus dashboard specifications and quarterly 7 Ps reviews through its references. This repository has no active standalone deck skill: if a presentation is required, hand the verified measurement proof pack to `chwezi-design-engine` and do not claim that this engine produced a deck.

<!-- dual-compat-start -->
## Use When

- At month end the client wants a written account of results by platform, top posts, what worked, what did not, paid results and next month's tests.
- The managing director wants a dashboard layout: metric hierarchy, RAG scorecard, chart choices and a phone-friendly view in Looker Studio.
- Every quarter, score how social media supports each of the 7 Ps (product, price, place, promotion, people, process, physical evidence) on a one-page summary out of 35.
- A new account needs a baseline, or a fall in results needs a cause-of-decline review.

## Do Not Use When

- `meta-social-metrics-framework` for deciding which KPIs to track, their owners and targets.
- `05-social-media-strategy` when the client wants the strategy rewritten.
- `meta-roi-framework` when the question is return on investment or a business case.
- Stop when platform data is unverified or missing; label the gaps rather than filling them.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| This month's and last month's figures for every tracked KPI per active platform | Platform native analytics exports (Meta Business Suite, LinkedIn Analytics, TikTok Business Centre, YouTube Studio, X Analytics) | Yes | Stop; label the platform `not assessed` rather than estimating figures. |
| Agreed targets and the primary goal | Strategy document or client agreement | Yes | Report direction of change only and mark every RAG status `not assessed`. |
| Paid ad data: spend, reach, cost per result, best ad | Ad manager exports | If paid ran | State "No paid social activity this month." |
| Notable events or issues (launch, holiday, crisis, viral post, outage, boost) | Client and consultant | Yes | Ask before writing the summary; do not invent causes. |
| Top 3 posts across all platforms | Consultant or analytics export | Yes | Rank from the export by engagement rate and state the basis. |
| Client name, sector, country/city, report period and consultant name | Client brief | Yes | Default to Uganda / Kampala; leave header fields as named placeholders. |

## Workflow

1. Collect the intake ([monthly report template](references/monthly-report-template.md) § Intake questions); route to `05-social-media-strategy` if the client wants the strategy rewritten, and stop on any platform whose data is unverified.
2. Run the monthly data quality audit before writing: GA4 spam and bot exclusions, tag firing in GA4 DebugView and UTM coverage rate.
3. Build one KPI table per active platform with last month, this month, target, RAG status and change %, removing tables for inactive platforms.
4. Write the period summary (what happened, the most significant achievement or challenge, the strategic implication), following Insight → Context → Recommendation in every section.
5. Write top 3 posts, what worked (3 bullets), what did not work (2 bullets with fixes), next month's tests (2–3) and paid performance, then 3–5 recommendations tied to this month's data.
6. For a standing dashboard use [dashboard specification](references/dashboard-specification.md); for a quarterly review, baseline or decline diagnosis use [quarterly marketing mix review](references/quarterly-marketing-mix-review.md).
7. Run the quality standards and the anti-slop gate; correct any RAG status, unsupported recommendation or missing footer and rerun the check. Withhold the report while it rests on corrupted or unverified data.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Written monthly report (header, 8 sections, footer) | Client business owner | Plain English; every section follows Insight → Context → Recommendation; footer names next report date and data sources. |
| Platform KPI tables with RAG status | Client business owner; `meta-social-metrics-framework` owner | Green only when the target is met or exceeded; one-sentence commentary per table. |
| Dashboard specification | Managing director; analyst | Phone-readable single-column layout; RAG threshold stated. |
| Quarterly 7 Ps summary (score out of 35) | Client leadership | Each P scored with evidence. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Data quality audit record | Checklist: spam/bot exclusions, tag firing, UTM coverage rate | Completed before the report is written; failures stated in the report. |
| Measurement proof pack | Per [measurement proof pack](../../../docs/evidence-packs/measurement-proof-pack.md) | Every figure traces to a dated export; WhatsApp estimates labelled as estimates. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. The report recommends paid changes; it never changes budgets or campaigns.

## Degraded Mode

Without verified platform exports and agreed targets, return the narrowest qualified result and mark the affected checks `not assessed`. The report structure, direction-of-change commentary for the platforms with data, and a data request for the rest can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client wants a standing dashboard, metric hierarchy or mobile reporting layout | Specify it with [dashboard-specification](references/dashboard-specification.md). | Data-dump dashboards, vanity headline metrics and unreadable mobile views. |
| A quarterly review, new-account baseline or cause-of-decline diagnosis is requested | Score the 7 Ps with [quarterly-marketing-mix-review](references/quarterly-marketing-mix-review.md). | Monthly metrics mistaken for a diagnosis of the whole mix. |
| The requested outcome is a new or rewritten strategy | Route to `05-social-media-strategy` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |
| Assigning RAG status in the written monthly report | Green on target; Amber slightly below (within 15% of target); Red more than 15% below. The dashboard specification uses a 10% band: state which threshold applies in each deliverable. | Inconsistent status between report and dashboard. |
| The client runs active campaigns | Add a real-time tier: ad spend vs daily budget (real-time), reach and frequency and conversion events (same day). | Overspend found only at month end. |
| Choosing a chart | Trends → line; comparisons → bar; proportions → donut; behaviour patterns → heatmap; conversion stages → funnel; never 3D (Raaz, c.2023). | Charts that distort proportions. |
| The data quality audit fails | Fix the data or state the defect before any figure is reported. | A report built on corrupted data, which is worse than no report. |
| No paid activity this month | Replace section 7 with "No paid social activity this month." | An empty paid table read as zero results. |

## Quality Standards

- Period summary paragraphs are written in plain English, readable by a business owner without digital marketing expertise.
- Every KPI table uses traffic-light status correctly: green only when the target is met or exceeded.
- Top posts analysis explains *why* each post worked, not merely what it was.
- "What did not work" is honest and gives a proposed fix for each item, not just an observation.
- Each recommendation links to specific data from the report; no generic advice.
- The paid section (where applicable) gives a clear spend-versus-result assessment and a forward recommendation.
- The footer specifies the next report date and data sources.
- British English throughout; no American spellings.

## Anti-Patterns

- Raw metric tables without interpretation. Fix: follow Insight → Context → Recommendation for every section and metric.
- Generic wins ("video content performed well"). Fix: name the platform, the tactic and the result, with figures against target.
- Marking a metric green when it is below target. Fix: apply the stated RAG thresholds exactly.
- Presenting WhatsApp open rates as platform-reported. Fix: label them estimates from read receipts and log enquiries by source.
- Using 3D charts or more than 6 charts per dashboard view. Fix: choose charts by data relationship and keep a single-column mobile layout.
- Reporting volume without quality. Fix: include the lead score distribution chart for clients using lead scoring.
- Claiming this engine produced a presentation deck. Fix: hand the proof pack to `chwezi-design-engine`.

## References

- [Monthly report template](references/monthly-report-template.md): read when collecting intake, applying the reporting principles (Kahan (2022) funnel CVR benchmarks, first-touch revenue by channel, mobile standard), writing the report sections, platform tables, footer, or the RACE framework (Chaffey and Ellis-Chadwick, 2022).
- [Dashboard specification](references/dashboard-specification.md): read when specifying a client dashboard: chart choice, mobile-first layout, RAG scorecard, tool choice, vanity-metric flags.
- [Quarterly marketing mix review](references/quarterly-marketing-mix-review.md): read when running a quarterly 7 Ps diagnostic, new-account baseline or cause-of-decline review.
- [Measurement proof pack](../../../docs/evidence-packs/measurement-proof-pack.md): read when assembling the evidence behind the report or handing over for a deck.
- [`meta-social-metrics-framework`](../meta-social-metrics-framework/SKILL.md): read when KPIs, owners or targets are not yet agreed.
- [`05-social-media-strategy`](../../pipeline/05-social-media-strategy/SKILL.md): read when the review shows the strategy needs rewriting.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the report.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

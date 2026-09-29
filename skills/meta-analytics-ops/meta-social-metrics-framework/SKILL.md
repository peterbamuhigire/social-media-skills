---
name: meta-social-metrics-framework
description: 'Use when a client does not know which numbers matter or reports vanity metrics: choose business, channel-health and benchmark KPIs with owners, targets and who sees what; produces the social metrics framework and KPI dictionary; not for the monthly performance write-up (use `meta-reporting`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Media Metrics Framework

Connects every social media metric to a business objective through a three-tier framework (Schaffer, 2013), with audience-specific reports, SMART targets and funnel velocity for East African clients.

<!-- dual-compat-start -->
## Use When

- The team reports likes and followers but leadership wants measures tied to sales, leads or enquiries.
- Each KPI needs a definition, owner, data source, target and the decision it informs.
- Reporting must differ by audience: weekly for the team, monthly for the owner, quarterly for the board.
- A retainer needs a measurement plan with one metric that matters, lines in the sand and stage metrics.
- Funnel conversion rates and velocity should be added to show where leads stall.

## Do Not Use When

- `meta-reporting` for the monthly written report, dashboard spec or quarterly review.
- `measurement-tracking-plan` for the events, tags and consent set-up that feed the KPIs.
- `meta-roi-framework` for return on investment and business cases.
- Stop before setting a target with no baseline data; mark it provisional.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Primary business goal (leads/enquiries, website traffic, sales, email/WhatsApp list, footfall, brand awareness or community) | Client owner | Yes | Stop; the primary metric depends on it. Ask the client to pick one. |
| Current metrics tracked (dashboard or description) | Client | Yes | Treat the account as starting from nothing and open with the vanity versus business metrics table. |
| Analytics access: GA4, Meta Business Suite, TikTok Analytics, LinkedIn Analytics, YouTube Studio, other | Client | Yes | Choose metrics trackable with the confirmed access; mark the rest `not assessed`. |
| Baseline values (current month or last 3 months average) | Analytics exports | For targets | Label targets provisional and declare the first 3 months as baseline-building. |
| Report audience (owner, marketing team, board) and cadence (weekly, monthly, quarterly) | Client | Yes | Produce the owner monthly template only and ask who else receives reports. |
| Business name, industry, country/city | Client brief | Yes | Default to Uganda / East Africa. |

The intake list is in [metrics framework method](references/metrics-framework-method.md) § Required Input.

## Workflow

1. Confirm the goal and intake; stop and route to `meta-reporting`, `measurement-tracking-plan` or `meta-roi-framework` when the request is the written report, tracking set-up or an ROI case.
2. Write the measurement problem statement and present the vanity versus business metrics table (at least five pairs) to reframe what the client should care about.
3. Choose the one Tier 1 primary metric for the stated goal with its baseline and tracking method, and place a guardrail beside it with denominator, threshold, owner and action.
4. Add Tier 2 secondary metrics per active platform (with ER and the EA benchmarks) and the Tier 3 comparative metrics that fit the client's context (ER change, follower growth, NSS, SOV, cost per result).
5. Add velocity and funnel CVR diagnostics where a CRM or enquiry log exists; for a retainer, declare the business stage and one focus metric with [OMTM, lines in the sand and stage metrics](references/omtm-lines-in-the-sand-and-stage-metrics.md).
6. Produce one report template per identified audience and draft SMART targets, applying the 3-month baseline rule for new clients.
7. Check every metric against the quality standards; correct any metric without a tier, source or decision and rerun the target set before hand-off.

Tier tables, benchmarks, formulas, report contents, the SMART structure and the funnel decision tree are in [metrics framework method](references/metrics-framework-method.md).

## Formulas and benchmarks

- ER = (Likes + Comments + Shares + Saves) ÷ Reach × 100 (Facebook, Instagram, LinkedIn, TikTok).
- SOV = Brand Mentions ÷ Total Market Mentions (brand + all tracked competitors) × 100.
- NSS = (Positive Mentions − Negative Mentions) ÷ Total Mentions × 100; full method in `meta-social-listening`.
- ROI = (TLV − COCA) ÷ COCA (Bodnar and Cohen, 2012) for board reporting.
- Strong ER for EA SMEs: Facebook 2–5%, Instagram 3–6%, TikTok 5–10%, LinkedIn 1–3% (company pages).
- Funnel CVR benchmarks (Kahan, 2022): visitor-to-lead >5%, inquiry-to-lead ~3%, lead-to-opportunity ~25%, opportunity-to-deal ~40%.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Seven-section metrics framework (problem statement, Tier 1–3, vanity table, report templates, SMART targets) | Client owner and marketing lead | Every metric sits in exactly one tier and is traceable to a named platform. |
| KPI dictionary | Marketing team; `meta-reporting` | Each KPI has definition, owner, data source, target or baseline note, and the decision it informs. |
| Report templates per audience | Owner (monthly), team (weekly), board (quarterly) | Distinct in length, language and content; owner report is one page in plain language. |
| SMART targets | Client owner | Each names metric, baseline, number, platform and date, or carries the 3-month baseline note. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Baseline register | Table: metric, value, period, source | Every target traces to a dated baseline or is marked provisional. |
| Guardrail record | Table: guardrail, denominator, threshold, owner, action | At least one guardrail is complete or marked `not assessed` with the conclusion narrowed. |
| Funnel diagnostic record | Stage CVRs against benchmark with flags | Any stage more than 20% below benchmark is flagged for review. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. For a board presentation, hand the verified metrics to `chwezi-design-engine`; no quarterly deck route is active here.

## Degraded Mode

Without a confirmed business goal and analytics access, return the narrowest qualified result and mark the affected checks `not assessed`. The vanity versus business metrics reframe, a draft tier structure and the baseline plan can still be delivered, with targets held until 3 months of data exist.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client is new or has under 3 months of comparable data | Treat the first 3 months as baseline-building; set no performance targets and say so at onboarding. | Targets set against no baseline. |
| The client has no historical ER baseline | Use the EA SME ER benchmarks, stated numerically, never "industry average" without a figure. | Vague benchmarks nobody can check. |
| The guardrail cannot be measured | Mark it `not assessed` and narrow the conclusion; engagement is evidence to interpret, not proof of value. | Claiming value from engagement alone. |
| A funnel stage falls more than 20% below benchmark | Run the diagnostic: inquiry-to-lead points to content and targeting; lead-to-opportunity to scoring threshold and response SLA; opportunity-to-deal to sales process. | Blaming marketing for a commercial conversation problem. |
| The client wants to track everything | Admit a metric only if it compares, is a rate, and changes a decision; choose one focus metric per quarter with the OMTM reference. | Dashboards of totals nobody acts on. |
| Board reporting is requested | Include ROI with TLV and COCA defined, SOV trend, NSS trend, year-on-year primary metrics, budget versus results and velocity. | A board report built on vanity metrics. |
| The requested outcome belongs to `meta-reporting` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- All three tiers are defined with specific named metrics, not generic categories.
- At least one trust, attention, privacy or safety guardrail has a denominator, threshold, owner and decision rule, or is marked `not assessed`.
- Primary metrics are linked to the client's named business goal, not generic "brand awareness".
- The vanity versus business metrics table includes at least five pairs, each explaining why the vanity metric misleads.
- EA-specific ER benchmarks are stated numerically (for example "2–5% for EA SMEs on Facebook"), not vaguely.
- Report format is matched to audience: owner, marketing team and board outputs are distinct in length, language and content.
- SMART target guidance includes the 3-month baseline rule, stated explicitly.
- The ROI formula (Bodnar and Cohen, 2012) is referenced for board-level reporting with its components defined; NSS and SOV formulas are stated per [metrics framework method](references/metrics-framework-method.md) § Quality criterion kept from the HEAD checklist.

## Anti-Patterns

- Optimising for vanity metrics (followers, likes, impressions) because they move upward. Fix: tie every metric to a business objective (Schaffer, 2013).
- Leading the reframe with criticism. Fix: ask "Which of these are you currently tracking?".
- Counting 3-second video views. Fix: report 50%+ video completion rate.
- Sending the owner a platform-jargon dashboard. Fix: one page, plain language, no graphs unless requested.
- Treating velocity as a secondary indicator. Fix: set velocity targets alongside cost targets and report them to the board with COCA and TLV.
- Reporting a lead-to-opportunity drop without checking response time. Fix: check the response SLA; leads that wait more than 24 hours convert at significantly lower rates.
- Absorbing `meta-reporting` into this workflow. Fix: route the neighbouring output and hand over verified inputs.

## References

- [Metrics framework method](references/metrics-framework-method.md): read when building the tiers, vanity table, report templates, SMART targets or funnel diagnostics.
- [OMTM, lines in the sand and stage metrics](references/omtm-lines-in-the-sand-and-stage-metrics.md): read when selecting KPIs, setting targets, declaring the business stage or writing a retainer measurement plan.
- [Brand metrics across the customer journey](references/brand-metrics-customer-journey.md): read when linking social reporting to journey-stage brand metrics or reading brand-health patterns.
- [`meta-reporting`](../meta-reporting/SKILL.md): read for the monthly report structure and template.
- [`meta-roi-framework`](../meta-roi-framework/SKILL.md): read for the full ROI calculation, TLV and COCA definitions.
- [`meta-social-listening`](../meta-social-listening/SKILL.md): read for NSS methodology, sentiment tracking and tools for SOV and mentions in East Africa.
- [Measurement proof pack](../../../docs/evidence-packs/measurement-proof-pack.md): read when assembling measurement evidence for release.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the problem statement and templates; [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

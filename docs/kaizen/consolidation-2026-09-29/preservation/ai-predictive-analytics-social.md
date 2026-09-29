# Preservation map — ai-predictive-analytics-social → ai-use-case-mapping

Filled from [preservation-map-template.md](../preservation-map-template.md) (Social Kaizen 2026-09-29, S02-T02). See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/ai-marketing/ai-predictive-analytics-social/SKILL.md @ 7c60138 (396 lines; reads Aug–Sep 2026: 0; fan-in 1)
Destination reference: skills/ai-marketing/ai-use-case-mapping/references/predictive-analytics-use-cases.md

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding (dual-compat block: Use When / Do Not Use When boilerplate, Required Inputs table, Capability and Permission Boundaries, Degraded Mode, generic Decision Rules rows, generic Workflow 1–6, Outputs, Evidence Produced, Quality Standards, generic Anti-Patterns, References to `ai-readiness-diagnostic` and AGENTS.md) | ai-use-case-mapping/SKILL.md dual-compat block | shared contract scaffolding — DROPPED-DUPLICATE-OF target SKILL.md § Use When … § References (identical generic rows, e.g. "Deliver a qualified draft with gaps and the next verification step.") | ticked |
| 2 | Purpose (forecast content performance, at-risk segments, campaign revenue; descriptive vs predictive; no data science team needed; Johnsen 2024, Lamplugh 2024) | references/predictive-analytics-use-cases.md § When to use this reference | MOVED | ticked |
| 3 | Purpose hand-offs: `meta-roi-framework` (financial case), `ai-data-foundation-plan` (data quality gaps) | references/predictive-analytics-use-cases.md § When to use this reference (hand-offs) | MOVED (skill names kept; coordinator re-points `ai-data-foundation-plan` to its S02 target) | ticked |
| 4 | Required Inputs 1–7 (business name, industry, country/city default Uganda/Kampala, platforms, data sources and format, data history with 3-month minimum, primary prediction goal with 4 options) | references/predictive-analytics-use-cases.md § Inputs | MOVED | ticked |
| 5 | From Descriptive to Predictive Analytics — 4-stage table (Descriptive, Diagnostic, Predictive, Prescriptive with examples) | references/predictive-analytics-use-cases.md § Decision rule 1 | MOVED | ticked |
| 6 | EA note: 3+ months Meta Business Suite data → ready for predictive; prescriptive follows validation | references/predictive-analytics-use-cases.md § Decision rule 1 | MOVED | ticked |
| 7 | Five Predictive Use Cases — matching rule (address highest-priority in full, summarise other four) | references/predictive-analytics-use-cases.md § Decision rule 2 | MOVED | ticked |
| 8 | Use case 1 Follower Churn Prediction (predicts, data, EA feasibility Medium, example output 18–24 segment 6 weeks) | references/predictive-analytics-use-cases.md § Decision rule 2 row 1 + Example outputs 1 | MOVED | ticked |
| 9 | Use case 2 Content Performance Prediction (6+ months, format/topic/time/day; feasibility High; example Tuesday 7–9 pm 2.3×, 4 video posts, Saturday carousels) | § Decision rule 2 row 2 + Example outputs 2 | MOVED | ticked |
| 10 | Use case 3 Audience Personalisation (segment data; feasibility Medium; Hootsuite, Buffer, Meta native targeting; example 3 segments 25–34 / 35–44 / 18–24) | § Decision rule 2 row 3 + Example outputs 3 | MOVED | ticked |
| 11 | Use case 4 Social Commerce Forecasting (past campaigns, GA4, AOV UGX, seasonality; feasibility Low–Medium; UTM via `meta-utm-tracking`; Excel sales data; example UGX 12–18 million, 2.8%, 4,500 contacts, March 2024 parity, medium confidence) | § Decision rule 2 row 4 + Example outputs 4 | MOVED | ticked |
| 12 | Use case 5 Cross-Sell and Upsell Identification (purchase history, engagement, interaction history; feasibility Low; SACCO members, repeat retail, subscriptions; example 340 followers, 3+ engagements in 90 days, 8–12%) | § Decision rule 2 row 5 + Example outputs 5 | MOVED | ticked |
| 13 | RFM Analysis — origin in direct marketing (Johnsen, 2024) | references/predictive-analytics-use-cases.md § Procedure A | MOVED | ticked |
| 14 | RFM dimension table (Recency 7 / 8–30 / 31–90 / 90+ days; Frequency Daily/Weekly/Occasional/Rare; Monetary High/Medium/Low/Unknown) | § Procedure A | MOVED | ticked |
| 15 | RFM segment table (VIP, Loyal, At-Risk, Dormant with profile and strategy) | § Procedure A | MOVED | ticked |
| 16 | RFM EA note (approximate scoring from segment trends; spreadsheet manual RFM sufficient) | § Procedure A | MOVED | ticked |
| 17 | Predictive Content Calendar Step 1 Export data (6 months, reach, engagement rate, clicks, saves, one row per post) | references/predictive-analytics-use-cases.md § Procedure B step 1 | MOVED | ticked |
| 18 | Step 2 Categorise posts (Format 6 values; Topic 5 values; Time slot 4 bands) | § Procedure B step 2 | MOVED | ticked |
| 19 | Step 3 Analyse with AI (Claude/ChatGPT prompt text, 49 words — kept as the engine's own prompt template, not a third-party quotation) | § Procedure B step 3 | MOVED | ticked |
| 20 | Step 4 Build the calendar (60% proven / 40% testing) | § Procedure B step 4 | MOVED | ticked |
| 21 | Step 5 Review and update (monthly comparison, re-run) | § Procedure B step 5 | MOVED | ticked |
| 22 | Five-Step Data Science Workflow (Lamplugh, 2024): Collect, Clean, Analyse, Implement, Monitor with all sub-actions | references/predictive-analytics-use-cases.md § Procedure C | MOVED | ticked |
| 23 | Tool Options table (Meta Business Suite Insights, GA4, Claude/ChatGPT, Akkio from $49/month, Obviously AI from $75/month, Pecan AI enterprise) + "no enterprise tools to SMEs" rule | references/predictive-analytics-use-cases.md § Decision rule 3 | MOVED (price freshness note added) | ticked |
| 24 | Tool selection guidance (4 tiers: no budget, under $100/month, dedicated analyst, enterprise via `ai-vendor-evaluation`) | § Decision rule 3 | MOVED (skill name kept; coordinator re-points `ai-vendor-evaluation`) | ticked |
| 25 | EA Data Sources Reference (Meta Business Suite, WhatsApp Business, GA4 + `meta-utm-tracking`, email platform analytics, sales records in Excel/QuickBooks/Wave) | references/predictive-analytics-use-cases.md § EA data sources reference | MOVED | ticked |
| 26 | Quality Criteria (7 items) | references/predictive-analytics-use-cases.md § Quality checklist | MOVED | ticked |
| 27 | Citation — Johnsen, M. (2024) *AI in Digital Marketing*. Mercury Learning. | § Sources | MOVED | ticked |
| 28 | Citation — Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn. Mercury Learning. | § Sources | MOVED | ticked |
| 29 | Citation — Ltifi, M. (ed.) (2025) *Advances in Digital Marketing in the Era of Artificial Intelligence*. CRC Press. | § Sources | MOVED | ticked |
| 30 | Citation — Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley. | § Sources (also already in target SKILL.md § References) | MOVED | ticked |
| 31 | Citation — Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson. | § Sources (also already in target SKILL.md § References) | MOVED | ticked |
| 32 | Reference files | — | none (source has no `references/` directory) | ticked |
Unique facts with register IDs carried: none (source cites no register IDs) (freshness re-checked: NOT_ASSESSED)
Items dropped as duplicates (must name the equivalent target text): 1 (row 1, shared contract scaffolding)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S02 review) — verdict ACCEPT — 2026-09-29

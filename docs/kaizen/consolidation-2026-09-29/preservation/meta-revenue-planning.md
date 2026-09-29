# Preservation map — meta-revenue-planning → meta-budget-planner

Filled from [preservation-map-template.md](../preservation-map-template.md) for Social Kaizen S04-T05. See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/meta-analytics-ops/meta-revenue-planning/SKILL.md @ 8eacccb (302 lines; reads Aug–Sep 2026: 0; fan-in 2)
Destination reference: skills/meta-analytics-ops/meta-budget-planner/references/bottom-up-revenue-plan.md (abbreviated `BURP` below)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When, Do Not Use When, Required Inputs table (2 rows), Outputs, Evidence Produced, Capability and permission boundary, Degraded mode, Decision rules (3 generic rows), Workflow steps 1–6, Quality Standards, Anti-Patterns bullets 1–5, Worked example | meta-budget-planner/SKILL.md same-named sections | DROPPED-DUPLICATE-OF target SKILL.md `Use When` … `Worked example` (identical templated text, differing only in the deliverable name "revenue plan and weighted pipeline model" vs "marketing budget plan and allocation rationale" and the key input "revenue target" vs "approved budget ceiling"; the read-only/no-spend boundary is verbatim in the target's `Capability and permission boundary`) | ticked |
| 2 | Read next (links to meta-roi-framework, anti-ai-slop, ai-slop-audit) and References (anti-slop gate; verify platform/price/legal claims) | meta-budget-planner/SKILL.md § Read next and § References | DROPPED-DUPLICATE-OF target § Read next (anti-ai-slop and ai-slop-audit links present verbatim) and § References (`meta-roi-framework/SKILL.md` listed; "Verify current platform, price, legal and regulatory claims before use." present verbatim) | ticked |
| 3 | Required Inputs (8 items: business name, industry, country/city, primary goal = revenue target quarterly/annual, average deal value in UGX, historical conversion data or Kahan benchmarks, current channel mix, sales team capacity) | BURP § Inputs (table) | MOVED | ticked |
| 4 | The Problem This Solves (activity goals with examples; not connected to revenue; work backwards; evaluate every activity against required lead volume, else deprioritise) | BURP § When to use this reference (paragraph 2) | MOVED | ticked |
| 5 | The Bottom-Up Revenue Model (Kahan, 2022) — intro (six steps in sequence, do not skip) | BURP § Procedure (intro) | MOVED | ticked |
| 6 | Step 1 State the Revenue Target (UGX 120,000,000 Q1 2026 example) | BURP § Procedure step 1 | MOVED | ticked |
| 7 | Step 2 New Clients Required (formula; UGX 120m ÷ UGX 6m = 20; multi-product blended average or separate calculations) | BURP § Procedure step 2 + § Decision rules row 3 | MOVED | ticked |
| 8 | Step 3 Opportunities Required (formula; ~40% benchmark; 20 ÷ 0.40 = 50; definition of opportunity) | BURP § Procedure step 3 + § Inputs "Definitions" | MOVED | ticked |
| 9 | Step 4 Qualified Leads Required (formula; ~25%; 50 ÷ 0.25 = 200; definition of qualified lead) | BURP § Procedure step 4 + § Inputs "Definitions" | MOVED | ticked |
| 10 | Step 5 Total Inquiries Required (formula; ~3%; 200 ÷ 0.03 = 6,667 per quarter; definition of contact incl. first WhatsApp message) | BURP § Procedure step 5 + § Inputs "Definitions" | MOVED | ticked |
| 11 | Step 6 Allocate Inquiries by Channel (historical basis or estimates; 6-row example table: Facebook 30%/2,000, WhatsApp referral 25%/1,667, Email 20%/1,333, LinkedIn 15%/1,000, Events and referrals 10%/667, Total 6,667) | BURP § Procedure step 6 + example table | MOVED | ticked |
| 12 | Funnel Conversion Rate Benchmarks (Kahan, 2022) — 4-row table (visitor-to-lead over 5%, inquiry-to-lead ~3%, lead-to-opportunity ~25%, opportunity-to-deal ~40%); use client data first, flag actuals vs benchmarks; below-benchmark gap as explicit client choice | BURP § Funnel conversion benchmarks + § Decision rules rows 1–2 | MOVED | ticked |
| 13 | Customer Acquisition Cost Cap — CAC ≤ CLV × 0.25 (Kahan, 2022); 4-step application (CLV = revenue × transactions × lifespan years; ceiling; actual CAC = quarterly budget ÷ new clients; confirm before presenting); over-cap → improve conversion or reduce target, not spend more | BURP § Customer acquisition cost cap + § Decision rules row 4 | MOVED (new to target; target § Section 6 — ROI Tracking uses the separate Bodnar and Cohen (2012) ROI formula, cross-referenced in BURP) | ticked |
| 14 | Pipeline Stage Weighting — 5-row table (10/30/60/85/100%) with stage definitions; weighted pipeline formula; present monthly; gap to target = lead volume marketing must fill | BURP § Weighted pipeline | MOVED | ticked |
| 15 | Deal Velocity Targets — 3-row table (48 hours; 14 days; 60 days); faster conversion = more revenue without more budget; slow stage = process bottleneck, fix before volume | BURP § Deal velocity targets + § Decision rules row 5 | MOVED | ticked |
| 16 | Monthly Review Protocol — every funnel stage not only revenue; 7-row review table; top-of-funnel shortfall = marketing response, mid-funnel = sales process response | BURP § Monthly review + § Decision rules rows 6–7 | MOVED | ticked |
| 17 | Output: Revenue Planning Document (6 items) | BURP § Output: revenue planning document | MOVED | ticked |
| 18 | Quality Criteria (7 items) | BURP § Release checklist | MOVED | ticked |
| 19 | Decision row (contract): route to `meta-roi-framework` when that contract is closer | meta-budget-planner/SKILL.md § Decision rules row 3 and § Workflow step 1 | MERGED-WITH-EXISTING (target neighbour route re-pointed from `meta-revenue-planning` to `meta-roi-framework` during this merge) | ticked |
| 20 | Anti-pattern (contract): using an undated benchmark as the client's result | BURP § Decision rules footnote (Kahan benchmarks as provisional comparators) | MERGED-WITH-EXISTING (same bullet also verbatim in target § Anti-Patterns bullet 1) | ticked |
| 21 | Citation: Kahan, R. (2022) *High-Velocity Digital Marketing …*, Amplify Publishing | BURP § Source | MOVED | ticked |
| 22 | Reference files (`references/`) | none — source has no `references/` folder | n/a | ticked |
Unique facts with register IDs carried: none (source cites no source-register IDs; freshness re-checked: NOT_ASSESSED). BURP adds a "verify before stating (no register record)" note on the Kahan benchmarks, CAC ratio, pipeline weights and velocity targets.
Items dropped as duplicates (must name the equivalent target text): 2
Reviewer: independent review agent (Claude Opus 5.5, read-only, S04 review) — verdict ACCEPT — 2026-09-29

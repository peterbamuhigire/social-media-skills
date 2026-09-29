# Preservation map — meta-ai-tools-audit → meta-tools-stack-evaluation

Filled from [preservation-map-template.md](../preservation-map-template.md) (Social Kaizen S02-T05). See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/meta-analytics-ops/meta-ai-tools-audit/SKILL.md @ 7c60138 (349 lines; reads Aug–Sep 2026: 0; fan-in 2)
Destination reference: skills/meta-analytics-ops/meta-tools-stack-evaluation/references/ai-tool-fit-access-cost-governance.md
Source reference files: none (the source had no `references/` folder).

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When, Do Not Use When, Required Inputs table, Outputs, Evidence Produced, Capability and permission boundary, Degraded mode, Workflow (6 steps), Quality Standards, Worked example | target SKILL.md | DROPPED-DUPLICATE-OF target SKILL.md § Use When / Do Not Use When / Required Inputs / Outputs / Evidence Produced / Capability and permission boundary / Degraded mode / Workflow / Quality Standards / Worked example (word-for-word the same template with "martech stack recommendation" in place of "AI tool assessment") | ticked |
| 2 | Decision rules (3 rows: current evidence; missing input; route to meta-tools-stack-evaluation) | target SKILL.md § Decision rules | DROPPED-DUPLICATE-OF target § Decision rules rows 1–2 (identical wording); row 3 obsolete after merge (target now carries the AI-audit row pointing to the reference) | ticked |
| 3 | Anti-patterns (5: undated benchmark; no inventory; missing access as pass; absorbing neighbour; live-account action) | target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns (same five items, neighbour name aside) | ticked |
| 4 | Purpose (EA-calibrated AI tool evaluation, by function, EA accessibility, stack by budget profile; Johnsen 2024, Upadhyay 2024) | ai-tool-fit-access-cost-governance.md § When to use this reference | MOVED | ticked |
| 5 | Read next (meta-tools-stack-evaluation; anti-ai-slop; ai-slop-audit) | § When to use; § Related skills | MOVED (self-link to target dropped as now the parent skill) | ticked |
| 6 | References (dual-compat block: anti-AI slop gate; verify current claims) | § Related skills; target SKILL.md § References | MERGED-WITH-EXISTING (target already lists the anti-slop gate and the verify-before-use sentence) | ticked |
| 7 | Required Input (six items; budget bands Starter/Growth/Scale; comfort levels None/Basic/Intermediate/Advanced; channel list) + "do not generate" rule | § Inputs | MOVED | ticked |
| 8 | Section 1 — AI Tool Evaluation Framework (five questions incl. EA payment detail: EA-issued Visa/Mastercard, MTN/Airtel Mobile Money; PayPal/US-billing exclusion; DPA under Uganda DPPA 2019) | § Decision rules: the five-question AI tool test | MOVED (the target's own non-AI five-question test in SKILL.md § Section 4 is kept; this AI version differs in Q2 payment access) | ticked |
| 9 | Section 2 — rating definitions (Recommended / Conditional / Defer) | § Decision rules (ratings list) | MOVED | ticked |
| 10 | Category 1 Content creation table (ChatGPT, Claude, Gemini, Jasper, Copy.ai, Canva AI) + EA note | § Tool evaluation tables › 1 | MOVED | ticked |
| 11 | Category 2 SEO table (Surfer, SEMrush, Ahrefs, RankMath) + EA note | § Tool evaluation tables › 2 | MOVED | ticked |
| 12 | Category 3 Social media management table (FeedHive, Buffer, Hootsuite, Later, Metricool) + EA note | § Tool evaluation tables › 3 | MOVED (partly overlaps target SKILL.md § Section 2 social table for Buffer/Hootsuite/Later; AI-capability columns are unique, so kept whole) | ticked |
| 13 | Category 4 Email marketing table (Mailchimp, Brevo, ActiveCampaign, ConvertKit) + EA note | § Tool evaluation tables › 4 | MOVED (Mailchimp/Brevo overlap target email table; AI columns unique) | ticked |
| 14 | Category 5 Marketing automation table (Zapier, Make, Africa's Talking ~UGX 30–60/SMS, ManyChat) + EA note | § Tool evaluation tables › 5 | MOVED (playbook-ai-automation-workflow link re-pointed to playbook-marketing-automation, its S02-T07 target) | ticked |
| 15 | Category 6 Analytics table (GA4, Meta Business Suite Insights, Brandwatch, MonkeyLearn, Sprout Social) + EA note | § Tool evaluation tables › 6 | MOVED | ticked |
| 16 | Category 7 Paid advertising table (Meta Advantage+, Performance Max, TikTok Smart+) + EA note and scope line | § Tool evaluation tables › 7 | MOVED | ticked |
| 17 | Category 8 Influencer table (Modash, HypeAuditor, Upfluence) + EA note | § Tool evaluation tables › 8 | MOVED | ticked |
| 18 | Section 3 — Budget Profile A Starter table + total + one-quarter rule | § Recommended AI stacks › Profile A | MOVED | ticked |
| 19 | Budget Profile B Growth table + total UGX 345,000–500,000 | § Profile B | MOVED | ticked |
| 20 | Budget Profile C Scale table + price-conversion note | § Profile C; section intro | MOVED (SEO row range "450,000–380,000" re-expressed per tool, original wording quoted) | ticked |
| 21 | Section 4 — Output Structure (7 items) | § Deliverable structure | MOVED | ticked |
| 22 | Quality Criteria (8 items) | § Acceptance checklist | MOVED | ticked |
| 23 | Related Skills (playbook-ai-automation-workflow, ai-use-case-mapping, meta-tools-stack-evaluation, 08-influencer-marketing-strategy, playbook-paid-social-advertising) | § Related skills; § When to use | MOVED (meta-tools-stack-evaluation self-reference dropped; automation link re-pointed as row 14) | ticked |
| 24 | Citation: Johnsen, M. (2024) *AI in Digital Marketing*. Mercury Learning | § Sources | MOVED | ticked |
| 25 | Citation: Upadhyay, M. A. (2024) *Generative AI for Marketing*. Packt | § Sources | MOVED | ticked |
| 26 | Citation: Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice* (RACE framework) | § Sources; target SKILL.md § References | MERGED-WITH-EXISTING | ticked |
| 27 | Citation: Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book* — ROI formula (TLV − COCA) ÷ COCA | § Sources (formula kept) | MERGED-WITH-EXISTING (target cites the book; formula is new to the target) | ticked |
| 28 | Uganda Data Protection and Privacy Act 2019 | § Sources; target SKILL.md § References | MERGED-WITH-EXISTING | ticked |
| 29 | Routing: target SKILL.md entry point; target description, Use When, Do Not Use When, Decision rules, Workflow, Anti-Patterns and Read next previously named `meta-ai-tools-audit` as neighbour | target SKILL.md § Decision rules (AI audit row), § Use When bullet, § Read next, § References bullet; neighbour re-pointed to `meta-budget-planner` | MOVED | ticked |
Unique facts with register IDs carried: none — the source cites no source-register IDs (grep of `docs/source-registers/source-register.json` for the skill name returned nothing) (freshness re-checked: NOT_ASSESSED)
Items dropped as duplicates (must name the equivalent target text): 3 (rows 1, 2, 3)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S02 review) — verdict ACCEPT — 2026-09-29

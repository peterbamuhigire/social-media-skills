# Preservation map — ai-vendor-evaluation → meta-tools-stack-evaluation

Filled from [preservation-map-template.md](../preservation-map-template.md) (Social Kaizen S02-T05). See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/ai-marketing/ai-vendor-evaluation/SKILL.md @ 7c60138 (432 lines; reads Aug–Sep 2026: 0; fan-in 2)
Destination reference: skills/meta-analytics-ops/meta-tools-stack-evaluation/references/ai-vendor-due-diligence.md
Source reference files: none (the source had no `references/` folder).

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When, Do Not Use When, Required Inputs table, Capability and Permission Boundaries, Degraded Mode, Workflow (6 generic steps), Outputs, Evidence Produced, Quality Standards, `dual-compat` References (ai-readiness-diagnostic, AGENTS.md) | target SKILL.md | DROPPED-DUPLICATE-OF target SKILL.md § Use When / Do Not Use When / Required Inputs / Capability and permission boundary / Degraded mode / Workflow / Outputs / Evidence Produced / Quality Standards (same generic contract: read-only default, `not assessed` never a pass, anti-slop ship gate, British English) | ticked |
| 2 | Generic anti-patterns (writing before objective known; reusing neighbour template; untraced price/claim; missing access treated as approval; publishing from drafting authority) | target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns ("Treating missing access or data as a successful check…", "Publishing, spending or editing a live account…", "Using an undated benchmark…"; the ai-readiness routing is kept in ai-vendor-due-diligence.md § When to use) | ticked |
| 3 | Decision row "Data readiness, AI maturity and risk support the proposed operating level → lowest viable automation level + human approval gate" | ai-vendor-due-diligence.md § Decision rules (row 1) | MOVED | ticked |
| 4 | Decision rows "required fact or approval missing" and "evidence partial → qualified draft" | target SKILL.md § Decision rules | DROPPED-DUPLICATE-OF target § Decision rules row "A material input is missing or contradictory → Stop that decision, request clarification, or issue a labelled partial result" | ticked |
| 5 | Framework line: Venkatesan and Lecinski (2026) *The AI Marketing Canvas* | ai-vendor-due-diligence.md § When to use; § Sources | MOVED | ticked |
| 6 | Position in the Canvas (Step 2 Experimentation; shortlist via meta-ai-tools-audit; hand-off to playbook-ai-automation-workflow) | ai-vendor-due-diligence.md § When to use this reference | MOVED (links re-pointed: meta-ai-tools-audit → ai-tool-fit-access-cost-governance.md; playbook-ai-automation-workflow → playbook-marketing-automation, its S02-T07 target) | ticked |
| 7 | Required Input (nine items incl. examples and team-level scale) + "do not proceed" rule | ai-vendor-due-diligence.md § Inputs | MOVED | ticked |
| 8 | Evaluation Framework — 8 Factors (apply all 8; 1–5 each; /40) | ai-vendor-due-diligence.md § Procedure; § The eight factors | MOVED | ticked |
| 9 | Factor 1 Use Case Fit table (5 rows) + all-in-one red flag | § The eight factors › Factor 1; § Decision rules row 2 | MOVED | ticked |
| 10 | Factor 2 Data Requirements table (5 rows) + PDPA 2019 flag (personal data, third-party sharing, cross-border transfer, automated profiling) | § Factor 2; § Decision rules row 3 | MOVED | ticked |
| 11 | Factor 3 Integration Compatibility table (5 rows) + Africa's Talking check | § Factor 3; § Decision rules row 4 | MOVED | ticked |
| 12 | Factor 4 EA Market Accessibility table (5 rows; USD card, MTN MoMo, Airtel Money) + UGX conversion + EAT (UTC+3) support note | § Factor 4 | MOVED | ticked |
| 13 | Factor 5 Team Capability Match table (5 rows) | § Factor 5 | MOVED | ticked |
| 14 | Factor 6 Output Quality table (5 rows) + humaniser standard + no-trial limitation | § Factor 6; § Decision rules row 7 | MOVED (`ai-content-humaniser` reference re-pointed to `anti-ai-slop`, its S02-T03 target) | ticked |
| 15 | Factor 7 Vendor Stability table (5 rows) + score 1–2 rule | § Factor 7; § Decision rules row 6 | MOVED | ticked |
| 16 | Factor 8 Total Cost of Ownership table (UGX 500,000 / 1,000,000 / 2,500,000 bands) + itemisation list | § Factor 8 | MOVED | ticked |
| 17 | Scoring and Decision Rules (32–40 / 24–31 / below 24) + deferred reason-and-alternative rule | § Scoring thresholds | MOVED | ticked |
| 18 | Output Structure — five sections | § Output sections | MOVED | ticked |
| 19 | Section 1 scorecard template ("## [Tool Name]" block incl. PDPA flag) | § Output sections › Section 1 (verbatim template) | MOVED | ticked |
| 20 | Section 2 Recommended Shortlist; Section 3 Deferred Tools | § Section 2; § Section 3 | MOVED | ticked |
| 21 | Section 4 "30-Day Experiment Brief — [Tool Name]" template (hypothesis, baseline, SMART success metric, Weeks 1–4, Go/No-Go) | § Section 4 (verbatim template) | MOVED | ticked |
| 22 | Section 5 Budget Summary table + rate, budget and single-tool-first rules | § Section 5 | MOVED | ticked |
| 23 | EA-Specific Evaluation Notes (6 bullets: free tiers, Africa's Talking, developer flag, bandwidth/offline, UGX conversion, Factor 4 gate) | § East African evaluation rules; § Decision rules rows 4, 5, 8, 9 | MOVED | ticked |
| 24 | Cross-References table (ai-readiness-diagnostic, meta-ai-tools-audit, ai-content-humaniser, playbook-ai-automation-workflow) | § Hand-offs | MOVED (re-pointed as in rows 6 and 14) | ticked |
| 25 | Tool Categories Reference intro | § Tool categories for building a shortlist | MOVED | ticked |
| 26 | Category 1 RAG tools table (Claude Projects, ChatGPT Projects, CustomGPT.ai, Notion AI, Mem.ai) + evaluation criteria | § Tool categories › RAG | MOVED | ticked |
| 27 | Category 2 Synthetic research table (Supernatural AI, Glimpse, Synthetic Users, prompted Claude/ChatGPT) + EA note | § Tool categories › Synthetic research | MOVED | ticked |
| 28 | Category 3 Agentic AI table (Persado, OfferFit, Braze, n8n, Zapier AI, Make.com, Claude API) + EA recommendation (n8n + Claude API; Zapier) | § Tool categories › Agentic AI | MOVED | ticked |
| 29 | Quality Criteria (8 items) | § Acceptance checklist | MOVED | ticked |
| 30 | Citation: Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd ed. Stanford Business Books | § Sources | MOVED | ticked |
| 31 | Citation: Sweenor, D. and Mulkers, T. (2024) *AI-Powered Business Intelligence*. O'Reilly Media | § Sources | MOVED | ticked |
| 32 | Citation: Nayebi, H. (2025) *Generative AI for Product and Marketing Teams*. Packt Publishing | § Sources | MOVED | ticked |
| 33 | Citation: Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley | § Sources; also target SKILL.md § References | MERGED-WITH-EXISTING | ticked |
| 34 | Citation: Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson | § Sources; also target SKILL.md § References | MERGED-WITH-EXISTING | ticked |
| 35 | Uganda Data Protection and Privacy Act 2019 (cited in body) | § Sources; also target SKILL.md § References | MERGED-WITH-EXISTING | ticked |
| 36 | Routing: target SKILL.md entry point | target SKILL.md § Decision rules (row "shortlist of up to four named AI tools…"), § Use When bullet, § References bullet | MOVED | ticked |
Unique facts with register IDs carried: none — the source cites no source-register IDs (grep of `docs/source-registers/source-register.json` for the skill name returned nothing) (freshness re-checked: NOT_ASSESSED)
Items dropped as duplicates (must name the equivalent target text): 3 (rows 1, 2, 4)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S02 review) — verdict ACCEPT — 2026-09-29

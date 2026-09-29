# Preservation map — playbook-ai-automation-workflow → playbook-marketing-automation

Filled from [preservation-map-template.md](../preservation-map-template.md) (Social Kaizen S02, task S02-T07). See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/playbooks/playbook-ai-automation-workflow/SKILL.md @ 7c60138 (417 lines; reads Aug–Sep 2026: 0; fan-in 5)
Destination reference: skills/playbooks/playbook-marketing-automation/references/ai-automation-recipes.md (abbreviated below as `AAR`)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When / Do Not Use When, Required Inputs contract table, Capability and Permission Boundaries, Degraded Mode, Workflow steps 1–5, Outputs, Evidence Produced, Quality Standards, anti-AI-slop and East African English links (identical to the target's own contract block apart from the job name) | Target SKILL.md dual-compat block | DROPPED-DUPLICATE-OF target SKILL.md § Capability and Permission Boundaries, § Degraded Mode, § Workflow and § References (identical wording, "Marketing Automation" in place of "Ai Automation Workflow") | ticked |
| 2 | Decision row: "An automated step can publish, spend or expose data → insert human approval and an auditable rollback point" | AAR § Decision rules row 1 | MOVED | ticked |
| 3 | Decision rows: "Inputs and authority are complete…", "Evidence or tooling is incomplete…", "Action publishes, spends, contacts people…" | Target SKILL.md § Decision Rules | DROPPED-DUPLICATE-OF target § Decision Rules rows 2–4 (identical text) | ticked |
| 4 | Anti-patterns (6 bullets: inventing facts; copying patterns; volatile details from memory; inaccessible account treated as healthy; acting from planning authority; actions without owner/timing/acceptance) | Target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns (identical six bullets) | ticked |
| 5 | § Purpose (realistic, affordable roadmap; most EA clients Stage 1; save 5–10 hours/week; Stage 3 within 60–90 days; Upadhyay 2024 source framework) | AAR § When to use this reference | MOVED | ticked |
| 6 | § Required Input (8 items; items 1–5 overlap the target's Required Inputs; team size/technical comfort, monthly tool budget in UGX/USD and biggest pain point are unique) | AAR § Inputs (all 8 kept, examples preserved) | MERGED-WITH-EXISTING (target § Required Inputs items 1–4 and 7) | ticked |
| 7 | § Step 1 — Assess the Client's Automation Maturity Stage (4-stage table; target Stage 3; no Stage 4 without dedicated digital team and budget above UGX 500,000; state and justify stage) | AAR § Procedure Step 1; § Decision rules row 6 | MOVED | ticked |
| 8 | § Step 2 — Qualify Each Task for Automation (8 factors with rules; pass at least 6 of 8; flag borderline) | AAR § Procedure Step 2; § Decision rules row 2 | MOVED | ticked |
| 9 | § Step 3 — Apply the 4 Feasibility Tests (repeatability, predictability, criticality, intuitiveness; fallback for Tests 3/4) | AAR § Procedure Step 3; § Decision rules rows 3–4 | MOVED | ticked |
| 10 | § Step 4 — Build the Automation Priority Matrix (2×2; no low/low tasks in first 90 days) | AAR § Procedure Step 4; § Decision rules row 5 | MOVED | ticked |
| 11 | § Step 5 — Recommend the Appropriate Tool Stack (free tier UGX 0; starter UGX 50,000–150,000; growth UGX 150,000–500,000; 12 tool rows; Uganda payment rule incl. MTN Mobile Money via Payoneer) | AAR § Procedure Step 5; § Decision rules rows 7–8 | MOVED | ticked |
| 12 | § Step 6 — The Automation Build Plan (Week 1 scheduling; Week 1 WhatsApp auto-reply; Week 2 3-email welcome sequence; Week 3 listening alert; Week 4 report; Month 2 chatbot FAQ with 2-hour escalation copy and 30-day review) | AAR § Procedure Step 6 (link to `11-content-calendar` made a live relative link) | MOVED | ticked |
| 13 | § Step 7 — What Must Stay Human (7 categories; "Human only — do not automate" flag) | AAR § Procedure Step 7; § Decision rules row 9 | MOVED | ticked |
| 14 | § Step 8 — Automation Maintenance Schedule (weekly 15 min, monthly 1 hour, quarterly 2–3 hours) | AAR § Procedure Step 8 (table form, all tasks kept) | MOVED | ticked |
| 15 | § No-Code Automation Stack (Erné, 2024) (two layers; example prompts; EA starter stack Zapier Free 5 Zaps + Sheets + Gmail + WhatsApp API via Twilio or WATI; $0–$50/month) | AAR § Recipe: two-layer no-code automation stack | MOVED | ticked |
| 16 | § Multi-Agent Architecture (Farri and Rosani, 2025; Nayebi, 2025) (4-agent table; human orchestrator; start with copywriting agent) | AAR § Recipe: multi-agent architecture | MOVED | ticked |
| 17 | § Human-in-the-Loop (HITL) Escalation Protocol (Nayebi, 2025) (5-row table; escalation-trigger protocol) | AAR § Recipe: HITL escalation protocol | MOVED | ticked |
| 18 | § Quality Criteria (8 items incl. scope limit to operational automation) | AAR § Acceptance checklist; § When to use this reference (scope limits) | MOVED | ticked |
| 19 | Citation: Upadhyay, N. (2024) *Generative AI for Marketing*. Kogan Page. | AAR § Sources | MOVED | ticked |
| 20 | Citation: Erné, R. (2024) *AI-Powered Marketing*. | AAR § Sources | MOVED | ticked |
| 21 | Citation: Farri, O. and Rosani, M. (2025) *Multi-Agent Systems for Marketing* | AAR § Sources (kept as cited, with a reconcile note against Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers* cited by the sibling source) | MOVED | ticked |
| 22 | Citation: Nayebi, M. (2025) *Human-in-the-Loop AI* | AAR § Sources (kept as cited, with a reconcile note against Nayebi, F. (2025) *Foundations of Agentic AI for Retail*) | MOVED | ticked |
| 23 | Citation: Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson. | AAR § Sources | MOVED | ticked |
| 24 | Citation: Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley. | AAR § Sources | MOVED | ticked |
| 25 | Reference files | none (source has no `references/` directory) | n/a | ticked |
Unique facts with register IDs carried: none (the source cites no `docs/source-registers/source-register.json` ID; freshness re-checked: NOT_ASSESSED)
Items dropped as duplicates (must name the equivalent target text): 3 (rows 1, 3, 4)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S02 review) — verdict ACCEPT_WITH_DOCUMENTED_LIMITATIONS (Farri/Rosani and Nayebi citation forms conflict with the sibling source; flagged, unresolved) — 2026-09-29

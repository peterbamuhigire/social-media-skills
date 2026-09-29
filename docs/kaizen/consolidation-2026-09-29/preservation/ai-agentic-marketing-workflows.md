# Preservation map — ai-agentic-marketing-workflows → playbook-marketing-automation

Filled from [preservation-map-template.md](../preservation-map-template.md) (Social Kaizen S02, task S02-T07). See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/ai-marketing/ai-agentic-marketing-workflows/SKILL.md @ 7c60138 (329 lines; reads Aug–Sep 2026: 0; fan-in 1)
Destination reference: skills/playbooks/playbook-marketing-automation/references/agentic-workflows-and-human-checkpoints.md (abbreviated below as `AWHC`)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When / Do Not Use When boilerplate, Capability and Permission Boundaries, Degraded Mode, Outputs table, Evidence Produced table, generic Quality Standards bullets 1–4, Workflow steps 2–6, repository agent guide link | Target SKILL.md § Use When, § Capability and Permission Boundaries, § Degraded Mode, § Outputs, § Evidence Produced, § Quality Standards, § Workflow | DROPPED-DUPLICATE-OF target SKILL.md § Capability and Permission Boundaries ("publishing, messaging, production changes, personal-data processing, spending … require explicit authority") and § Degraded Mode ("Mark each unavailable check `not assessed`; never convert it into a pass") | ticked |
| 2 | Do Not Use When: route to `ai-readiness-diagnostic` when its narrower output is the deliverable (routing link) | AWHC § When to use this reference (bullet 1, link to ai-readiness-diagnostic) | MOVED | ticked |
| 3 | Required Inputs table rows: use-case brief with human control point and success measure; brand voice/offer facts/approvals; performance/platform/research evidence | AWHC § Inputs rows 7–9 | MOVED | ticked |
| 4 | Decision row: "Data readiness, AI maturity and risk support the proposed operating level → choose the lowest viable automation level and define its human approval gate" | AWHC § Decision rules row 1 | MOVED | ticked |
| 5 | Decision row: "A required fact or approval is missing → stop that claim or action" | Target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns "Inventing a client fact, benchmark, budget or approval. Fix: cite the source or label the assumption and its effect." | ticked |
| 6 | Decision row: "Evidence is partial but a useful draft is possible → qualified draft with gaps" | Target SKILL.md § Decision Rules | DROPPED-DUPLICATE-OF target § Decision Rules "Evidence or tooling is incomplete → Produce the narrowest qualified draft and a gap list" | ticked |
| 7 | Workflow step 1 (confirm workflow specification; route to `ai-readiness-diagnostic` if closer) | AWHC § When to use this reference | MERGED-WITH-EXISTING (target Workflow step 1 covers consumer/objective/owner) | ticked |
| 8 | Workflow step 7: apply trust/control/drift reference before recommending any rollout or learning loop | AWHC § When to use this reference (bullet 3) | MOVED | ticked |
| 9 | Quality Standards bullet 5: separate model, surrounding system, inputs, inferred inputs, outputs, human reviewer, external action; require disclosure, correction, escalation, drift monitoring, non-AI fallback | AWHC § Procedure step 8 and § Acceptance checklist item 9 | MOVED | ticked |
| 10 | Anti-pattern: writing before objective and audience are known | Target SKILL.md § Workflow step 1 | DROPPED-DUPLICATE-OF target § Workflow step 1 "stop if the objective or owner is missing" | ticked |
| 11 | Anti-pattern: reusing a neighbouring skill's template because headings look similar | Target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns "Copying one channel or client pattern unchanged. Fix: tie each choice to the named audience, objective and evidence." | ticked |
| 12 | Anti-pattern: adding a price, result, quotation, platform limit or cultural claim without a traceable source | Target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns "Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim." | ticked |
| 13 | Anti-pattern: treating missing access, evidence or native-language review as approval | Target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns "Treating an inaccessible account, file or metric, or a missing native-language review, as healthy or approved. Fix: mark it `not assessed` and bound the conclusion." (native-language wording added to the target on review, 29 Sep 2026) | ticked |
| 14 | Anti-pattern: publishing, sending, spending or changing a live account from drafting authority | Target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns "Publishing, spending, messaging or changing production state from planning authority. Fix: obtain explicit action authority." | ticked |
| 15 | Anti-pattern: describing an AI workflow as autonomous without decision boundary, escalation, correction path, audit trail or rollback | AWHC § Decision rules row 7 | MOVED | ticked |
| 16 | § Purpose (autonomous agents that perceive, reason, act, learn; architecture spec + template + wave plan; assumes `ai-readiness-diagnostic` wave score; no Wave 3 for Wave 1 without phased roadmap) | AWHC § When to use this reference | MOVED | ticked |
| 17 | § Required Inputs (6 items: business name, industry, country/city default Uganda, AI maturity wave, target workflow, technical resources) | AWHC § Inputs rows 1–6 | MOVED | ticked |
| 18 | § Agentic vs Generative AI: The Critical Distinction (reactive vs proactive; Wave guidance 1/2/3; EA businesses reach Wave 2 with 3+ months clean data first) | AWHC § Procedure step 1; § Decision rules rows 2–6 and closing note | MOVED | ticked |
| 19 | § The PRAL Loop (4-stage table, label oversight points) | AWHC § Procedure step 2; § PRAL loop template | MOVED | ticked |
| 20 | § The BDI Model for Marketing Agents (3-row table; client prompt; document before tool selection) | AWHC § Procedure step 3; § BDI decision-boundary template | MOVED | ticked |
| 21 | § The OODA Cycle for Real-Time Decisions (Boyd 1976; social listening agent example; OODA complements PRAL) | AWHC § OODA cycle for real-time decisions | MOVED | ticked |
| 22 | § Five Agentic Workflow Templates — 1 Content Pipeline Agent | AWHC § Five agentic workflow templates § 1 | MOVED | ticked |
| 23 | § Five Agentic Workflow Templates — 2 Sentiment Monitoring Agent (threshold 3+ negative mentions/hour) | AWHC § Five agentic workflow templates § 2 | MOVED | ticked |
| 24 | § Five Agentic Workflow Templates — 3 Proactive Campaign Agent (7-step actions, 7-day report) | AWHC § Five agentic workflow templates § 3 | MOVED | ticked |
| 25 | § Five Agentic Workflow Templates — 4 Multi-Agent Reporting System | AWHC § Five agentic workflow templates § 4 | MOVED | ticked |
| 26 | § Five Agentic Workflow Templates — 5 WhatsApp Response Agent | AWHC § Five agentic workflow templates § 5 | MOVED | ticked |
| 27 | § HITL Safeguard Design (decision boundary, escalation triggers incl. UGX 500,000 threshold, escalation mechanism, audit trail) | AWHC § HITL safeguard design | MOVED | ticked |
| 28 | § Three-Wave Implementation Roadmap (readiness, build, effort 1–2 days / 1–2 weeks / 4–8 weeks) | AWHC § Three-wave implementation roadmap | MOVED | ticked |
| 29 | § Tool Stack Options (7-tool table with costs; Wave 1 and Wave 3 stack recommendations) | AWHC § Tool stack options (verify-before-quoting note added) | MOVED | ticked |
| 30 | § Quality Criteria (8 bullets) | AWHC § Acceptance checklist items 1–8 | MOVED | ticked |
| 31 | Citation: Nayebi, F. (2025) *Foundations of Agentic AI for Retail*. Gradient Divergence. | AWHC § Sources | MOVED | ticked |
| 32 | Citation: Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn. Stanford University Press. | AWHC § Sources | MOVED | ticked |
| 33 | Citation: Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers*. Harvard Business Review Press. | AWHC § Sources | MOVED | ticked |
| 34 | Citation: Boyd (1976), OODA loop (in-text) | AWHC § Procedure step 4; § OODA cycle; § Sources | MOVED | ticked |
| 35 | Reference file: references/agentic-marketing-operating-model.md (autonomy ladder, workflow selection, tool gating, brand memory, 30-case eval, deployment stages, hardening checklist) | skills/playbooks/playbook-marketing-automation/references/agentic-marketing-operating-model.md (provenance line added) | MOVED | ticked |
| 36 | Reference file: references/ai-campaign-trust-control-correction-drift.md (Sadr, *Designing for AI*, early-release Chapters 1–3 basis; required workflow fields; stop conditions) | skills/playbooks/playbook-marketing-automation/references/ai-campaign-trust-control-correction-drift.md (provenance line added; `../SKILL.md` now resolves to the target) | MOVED | ticked |
Unique facts with register IDs carried: none (the source cites no `docs/source-registers/source-register.json` ID; freshness re-checked: NOT_ASSESSED)
Items dropped as duplicates (must name the equivalent target text): 8 (rows 1, 5, 6, 10, 11, 12, 13, 14; row 1 groups the shared contract scaffolding)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S02 review) — verdict ACCEPT — 2026-09-29

Note for the reviewer: `skills/ai-marketing/ai-content-humaniser/SKILL.md` links to the old path of the moved trust/drift reference and must be re-pointed by the coordinator.

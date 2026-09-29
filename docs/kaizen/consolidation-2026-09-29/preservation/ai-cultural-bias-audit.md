# Preservation map — ai-cultural-bias-audit → policy-ai-content-ethics

Filled from [preservation-map-template.md](../preservation-map-template.md) (Social Kaizen S02-T08). See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/ai-marketing/ai-cultural-bias-audit/SKILL.md @ 7c60138 (229 lines; reads Aug–Sep 2026: 0; fan-in 2)
Destination reference: skills/policies/policy-ai-content-ethics/references/cultural-bias-audit-protocol.md

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding (Use When, Do Not Use When, Required Inputs table, Capability and Permission Boundaries, Degraded Mode, Workflow boilerplate, Outputs, Evidence Produced, Quality Standards, generic Anti-Patterns, dual-compat References) | target SKILL.md § Use When … § Anti-Patterns | shared contract scaffolding — DROPPED-DUPLICATE-OF target SKILL.md dual-compat block (same sections; the "mark it `not assessed`" rule is kept in reference § Acceptance checklist) | ticked |
| 2 | Routing comparison `ai-readiness-diagnostic` (Do Not Use When / Workflow step 1) | reference § When to use this reference; § Procedure step 1 | MOVED | ticked |
| 3 | Decision row: data readiness / lowest viable automation level + human approval gate | reference § Decision rules | MOVED | ticked |
| 4 | Decision row: required fact or approval missing → stop / placeholder | reference § Decision rules | MOVED (also MERGED-WITH-EXISTING target § Anti-Patterns "Inventing a client fact…") | ticked |
| 5 | Decision row: partial evidence → qualified draft with gaps | reference § Decision rules | MOVED | ticked |
| 6 | Anti-pattern: reusing a neighbouring skill's template because headings look similar | reference § Procedure step 1 (route to closer match) | MERGED-WITH-EXISTING target § Anti-Patterns "Copying one channel or client pattern unchanged" | ticked |
| 7 | Anti-pattern: treating missing native-language review as approval | reference § Acceptance checklist (last item) | MOVED | ticked |
| 8 | ## Purpose (pre-delivery audit report; documented failure cases + AIF360) and default-context note (Uganda/EA baseline) | reference § When to use this reference | MOVED | ticked |
| 9 | ## Required Inputs (7 numbered items incl. AI tools used, reviewer identity) | reference § Inputs | MOVED | ticked |
| 10 | Part 1: Why AI Has Systematic Cultural Bias — The Training Data Problem (5 defaults; persist despite diversity brief) | reference § Why AI has systematic cultural bias | MOVED | ticked |
| 11 | Part 1 — The Uncanny Valley of Cultural Representation (4 recognisable errors; erodes trust more than no localisation) | reference § The uncanny valley of cultural representation | MOVED | ticked |
| 12 | Part 2: Documented Failure Cases — BuzzFeed Barbie (2023): 3 failures and lesson | reference § Primary case — BuzzFeed Barbie (2023) | MOVED (target § 2D names it only as a precedent) | ticked |
| 13 | Part 2 — DeepVogue secondary case and lesson ("East African" is not one aesthetic) | reference § Secondary case — DeepVogue | MOVED | ticked |
| 14 | Part 3: IBM AI Fairness 360 (individual, group, counterfactual fairness) | reference § Evaluative standard — IBM AI Fairness 360 | MOVED | ticked |
| 15 | Part 4: Pre-Delivery Bias Checklist — intro (every deliverable; record name/date/findings) | reference § Pre-delivery bias checklist | MOVED | ticked |
| 16 | Part 4 — 4A Visual Content Checklist (6 items) | reference § 4A — Visual content | MOVED | ticked |
| 17 | Part 4 — 4B Copy and Text Checklist (6 items incl. Western-default phrases) | reference § 4B — Copy and text | MOVED | ticked |
| 18 | Part 4 — 4C Audience Persona Checklist (5 items incl. WhatsApp/Facebook, church/mosque networks) | reference § 4C — Audience personas | MOVED | ticked |
| 19 | Part 5: Reviewer Qualification Standard — minimum qualification (3 routes) and "not sufficient" (4 items) | reference § Reviewer qualification standard | MOVED (extends target § 2D "reviewer with direct cultural knowledge") | ticked |
| 20 | Part 5 — Reviewer Sign-Off record line | reference § Sign-off record template | MOVED | ticked |
| 21 | Part 6: Correction Protocol (4 ordered actions) | reference § Correction protocol | MOVED | ticked |
| 22 | Part 6 — Prompt Improvement for EA Context (5 prompt specifications incl. quoted instruction) | reference § Prompt improvement for the East African context | MOVED | ticked |
| 23 | ## Quality Criteria (8 criteria) | reference § Acceptance checklist for the audit report | MOVED | ticked |
| 24 | Citation: Ching, V. and Mothi, D. (2025) *AI for Creatives: Unlocking Expressive Digital Potential*, CRC Press | reference § When to use; § Sources | MOVED (target cites "Ching, J. and Mothi, N. (2025)" — initials differ; flagged for reviewer) | ticked |
| 25 | Citation: IBM Research (2018–present) *AI Fairness 360 (AIF360)*, aif360.mybluemix.net | reference § Sources (URL flagged for verification) | MOVED | ticked |
| 26 | Citation: BuzzFeed (2023) AI Barbie series | reference § Sources | MOVED | ticked |
| 27 | Citation: DeepVogue — AI fashion generation bias documentation (Ching and Mothi, 2025) | reference § Sources | MOVED | ticked |
| 28 | Reference files | none (source has no references/ directory) | n/a | ticked |
Unique facts with register IDs carried: none (source cites no source-register IDs) (freshness re-checked: NOT_ASSESSED)
Items dropped as duplicates (must name the equivalent target text): 1 (row 1, shared contract scaffolding — equivalent: target SKILL.md dual-compat block §§ Use When to Anti-Patterns)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S02 review) — verdict ACCEPT_WITH_DOCUMENTED_LIMITATIONS (Ching/Mothi initials aligned to the sources' V./D. form in the target; external verification NOT_ASSESSED; a boilerplate automation row in the reference is left for S09) — 2026-09-29

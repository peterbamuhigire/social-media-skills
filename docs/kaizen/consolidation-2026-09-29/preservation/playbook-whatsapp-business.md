# Preservation map — playbook-whatsapp-business → platform-whatsapp

Filled from [preservation-map-template.md](../preservation-map-template.md) for Social Kaizen S05-T13. See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/playbooks/playbook-whatsapp-business/SKILL.md @ 8eacccb + S04 working tree (tree cda737c) (273 lines; reads Aug–Sep 2026: 2; fan-in 1)
Destination reference: skills/platforms/platform-whatsapp/references/whatsapp-business-app-operations.md (abbreviated `WBO` below)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When, Do Not Use When, Required Inputs table, Capability and Permission Boundaries, Degraded Mode, Decision Rules rows 2–4 (inputs complete; evidence incomplete; action publishes/spends/contacts), Workflow steps 1–5, Outputs, Evidence Produced, Quality Standards, Anti-Patterns bullets 1–6 | platform-whatsapp/SKILL.md same-named sections | DROPPED-DUPLICATE-OF target SKILL.md `Use When` … `Anti-Patterns` (same templated playbook/platform contract; the source's approval row is covered by the target's Capability and Permission Boundaries "publishing, messaging … require explicit authority" and Anti-Patterns bullet 5, and its gap-list row by the target's Degraded Mode) | ticked |
| 2 | References block (anti-AI-slop, East African English, cited-sources line) | platform-whatsapp/SKILL.md § References | DROPPED-DUPLICATE-OF target § References (same lines; target adds register and release-gate links) | ticked |
| 3 | Decision Rules row 1 (structured service rather than promotion → labels, templates and escalation before broadcasts) | WBO § When to use this reference paragraph 2 + target SKILL.md new Decision Rules row | MOVED | ticked |
| 4 | Required Inputs (7 items, incl. current usage: personal number / app / API; team size) | WBO § Inputs | MOVED | ticked |
| 5 | Why WhatsApp Business Matters for EA (dominant channel; no smartphone-share figure; Pew 2023 median 73%, Kenya < 90%; Yazi ~95%; register WA-01, WA-02, WA-04; professional vs informal use) | WBO § Why WhatsApp Business matters in East Africa (register WHATSAPP-USAGE-EA-2026) | MOVED | ticked |
| 6 | App (1–2 people) vs API (verified business, approved BSP; automation; 3+ people) | WBO § Decision rules rows 1–2 | MOVED (verify-eligibility note) | ticked |
| 7 | Account Setup — business profile table (7 fields, 256-character description with Kampala example) | WBO § Procedure 1 table | MERGED-WITH-EXISTING (target § 1 Business Profile has 6 of the fields; business-hours row, "no abbreviations" and example carried in WBO) | ticked |
| 8 | Profile photo (640×640 min; clean background, no text; ~48×48 thumbnail; consistent branding) | WBO § Procedure 1 (profile photo paragraph) | MERGED-WITH-EXISTING (target § 1 Profile Photo gives 640×640 and 50×50; difference recorded in WBO) | ticked |
| 9 | Automated Messaging — configure all three before promoting | WBO § Procedure 2 intro + § Decision rules row 4 | MOVED | ticked |
| 10 | Greeting message (3 jobs; template; clinic emergency adaptation) | WBO § Procedure 2 greeting bullet | MOVED (template differs from target § 1 Greeting Message; both kept) | ticked |
| 11 | Away message (3 jobs; template) | WBO § Procedure 2 away bullet | MOVED (template differs from target § 1 Away Message; both kept) | ticked |
| 12 | Quick replies (minimum 10; 10-row trigger table) | WBO § Procedure 2 quick-replies table | MERGED-WITH-EXISTING (7 shortcuts overlap target § 1 Quick Replies; /catalogue, /return, /social and the minimum of 10 carried in WBO) | ticked |
| 13 | Broadcast Lists — definition; 256-contact limit; number must be saved; opt-in only, never add a contact who has not initiated | WBO § Procedure 3 bullets + § Decision rules row 6 | MERGED-WITH-EXISTING (definition and saved-number rule also in target § 2; 256 limit and initiation rule carried in WBO with WHATSAPP-BUSINESS-POLICY) | ticked |
| 14 | Segmentation model (5 lists; 90-day active/lapsed line; Location: [City]) | WBO § Procedure 3 table + reconciliation note (target uses 60 days) | MOVED | ticked |
| 15 | Broadcast frequency and ratio (max 2 promotional/week; transactional unlimited; 70/30 value/promotion) | WBO § Procedure 3 "Frequency and mix" | MOVED (difference from target's ceiling of 3 recorded) | ticked |
| 16 | Product Catalogue — definition; 5-field entry table (price never blank; product code; 640×640 image) | WBO § Procedure 4 table + reconciliation note on "contact for pricing" | MOVED | ticked |
| 17 | Catalogue maintenance rule (update within 24 hours of price change) + where to share the catalogue link (3 places) | WBO § Procedure 4 + § Decision rules row 8 | MOVED | ticked |
| 18 | Customer Service Protocol — define before publicising; SLA (2 h first response, 4 h resolution/escalation; out-of-hours promise) | WBO § Procedure 5 + § Decision rules row 5 | MOVED | ticked |
| 19 | Escalation path table (5 enquiry types) | WBO § Procedure 5 table + § Decision rules row 9 | MOVED | ticked |
| 20 | Complaint resolution rule (private within one message; never in a group; specific resolution) | WBO § Procedure 5 complaint rule + § Decision rules row 7 | MOVED | ticked |
| 21 | Team Management (shared device or API multi-agent inbox; daily lead; weekly rotation; shared tracker such as a Google Sheet) | WBO § Procedure 6 + § Decision rules row 3 | MOVED | ticked |
| 22 | Output: WhatsApp Business Setup Brief (6 deliverables) | WBO § Output | MOVED (4-week calendar pointed at target § 7 calendar) | ticked |
| 23 | Quality Criteria (7 items incl. testing automated messages from a personal number; opt-in records; weekly SLA monitoring; 70/30 tracking) | WBO § Release checklist items 1–7 (item 8 added for verification) | MOVED | ticked |
| 24 | Citation: Pidsley, R. (2023) *Social Media Marketing for Business…*, Kogan Page | WBO § Sources | MOVED | ticked |
| 25 | Reference files (`references/`) | none — source has no `references/` folder | n/a | ticked |

Unique facts with register IDs carried: WHATSAPP-USAGE-EA-2026 (source's WA-01/WA-02/WA-04 wording); WHATSAPP-BUSINESS-POLICY applied to opt-in, opt-out, templates and escalation (freshness re-checked: NOT_ASSESSED — register dates relied on). App limits (256 contacts, 256 characters, image sizes) and API thresholds marked "verify before stating (no register record)".
Items dropped as duplicates (must name the equivalent target text): 2
Reviewer: independent review agent (Claude Opus 5.5, read-only, S05 review) — verdict ACCEPT — 2026-09-29. The "ticked" column records the merge worker's self-check; the reviewer confirmed the rows.

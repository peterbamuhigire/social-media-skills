# Preservation map — meta-utm-tracking → measurement-tracking-plan

Filled from [preservation-map-template.md](../preservation-map-template.md) for Social Kaizen S04-T03. See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/meta-analytics-ops/meta-utm-tracking/SKILL.md @ 8eacccb (318 lines; reads Aug–Sep 2026: 0; fan-in 14)
Destination reference: skills/meta-analytics-ops/measurement-tracking-plan/references/utm-convention-and-campaign-register.md (abbreviated `UCR` below)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When (2 templated bullets), Do Not Use When, Capability and permission boundary, Degraded mode, Workflow steps 1–6, Quality Standards paragraph | measurement-tracking-plan/SKILL.md same-named sections | DROPPED-DUPLICATE-OF target SKILL.md `Do Not Use When`, `Capability and Permission Boundaries`, `Degraded Mode`, `Workflow`, `Quality Standards` (engine template text; job words carried by the Use When bullet "(formerly `meta-utm-tracking`)") | ticked |
| 2 | Purpose (set up once, client operates; explain plainly to EA SMEs; without UTM tags meta-roi-framework cannot attribute) | UCR § When to use this reference | MOVED | ticked |
| 3 | Required Inputs table (channel taxonomy, campaign names, destination URLs, analytics access; purpose/approval) | UCR § Inputs (last row) + SKILL.md § Required Inputs row 6 | MOVED | ticked |
| 4 | Outputs: UTM convention, campaign register and QA checklist + acceptance condition | UCR § When to use (output paragraph) | MOVED | ticked |
| 5 | Evidence Produced: decision and source register | SKILL.md § Evidence Produced row 1 | MERGED-WITH-EXISTING | ticked |
| 6 | Decision rules rows 1–2 (current inputs → full output; missing input → stop/partial) | UCR § Decision rules rows 4–5 | MOVED | ticked |
| 7 | Decision rules row 3 (route to `meta-analytics-privacy`) | — | DROPPED-DUPLICATE-OF target SKILL.md § References bullet "Consent, retention and sharing review" (neighbour now internal) | ticked |
| 8 | Anti-patterns 1–3, 5 | UCR § Anti-patterns (4 bullets) | MOVED | ticked |
| 9 | Anti-pattern 4 (absorbing `meta-analytics-privacy`) | — | DROPPED-DUPLICATE-OF target SKILL.md § References (both jobs now one owner) | ticked |
| 10 | Worked example (verified taxonomy → convention with dates; no access → supported sections + recovery list) | SKILL.md § Degraded Mode ("target-state plan … data request … not assessed") and UCR § Decision rules row 5 | MERGED-WITH-EXISTING | ticked |
| 11 | Read next / References (meta-analytics-privacy, anti-ai-slop, ai-slop-audit) | SKILL.md § References and Workflow step 8 (anti-slop gates) | MERGED-WITH-EXISTING (Review fix: both gates now linked in SKILL.md § References.) | ticked |
| 12 | Required Input list (6 items: client name, website URL, platforms, monthly visitors, GA4 installed?, campaign start date) | UCR § Inputs rows 1–6 | MOVED | ticked |
| 13 | Section 1 — What UTM Parameters Are (three paragraphs: what, why, what they look like; Akacia Kampala default URL; `?` and `&` explanation) | UCR § Section 1 | MOVED | ticked |
| 14 | Section 2 — The 5 UTM Parameters table + note (source/medium/campaign always; utm_content essential for multiple creatives) | UCR § Section 2 | MOVED + UPDATED (utm_id and utm_source_platform added; nine GA4 parameters noted; register GA4-UTM-PARAMETERS-2026) | ticked |
| 15 | Section 3 — Naming Convention Rules 1–6 (lowercase; hyphens; specific not verbose; match calendar; utm_content = post ID; never deviate) | UCR § Section 3 | MOVED | ticked |
| 16 | Section 4 — Naming Convention Reference Table (9 sources; 9 mediums; 5 campaign patterns) | UCR § Section 4 | MOVED (channel-grouping check added, marked verify) | ticked |
| 17 | Section 5 — UTM Link Builder (Google Campaign URL Builder URL; 7 steps; shortening guidance 3 bullets) | UCR § Section 5 | MOVED | ticked |
| 18 | Section 6 — Campaign Tracking Spreadsheet Template (7 columns; 3 Akacia example rows; 3 notes: unique short URL per platform, brief notes, archive monthly) | UCR § Section 6 | MOVED (utm_id column note added) | ticked |
| 19 | Section 7 — Reading Attribution in GA4 (UA flag; source/medium steps 1–4; campaign steps 1–3; metrics table 5 rows; monthly routine 6 steps) | UCR § Section 7 | MOVED + UPDATED (UA now shut down → archive only; "Conversions" shown as key events; engaged-session definition cited to GA4-ENGAGED-SESSION-2026; monthly report linked to meta-reporting) | ticked |
| 20 | Section 8 — WhatsApp and Dark Social (what, why, 4 actions, 40–60 % → ≤ 20 % target, record baseline and report reduction) | UCR § Section 8 | MOVED (WhatsApp role tagged WHATSAPP-USAGE-EA-2026; target range labelled the source's planning range) | ticked |
| 21 | Quality Criteria (8 items) | UCR § QA checklist (9 items; channel-group mapping added) | MOVED | ticked |
| 22 | Citations / author-year sources | none in source | n/a | ticked |
| 23 | Reference files (`references/`) | none — source has no `references/` folder | n/a | ticked |

Unique facts with register IDs carried: WHATSAPP-USAGE-EA-2026 (existing, not re-verified); GA4-UTM-PARAMETERS-2026 and GA4-ENGAGED-SESSION-2026 (new, read live 2026-09-29; freshness re-checked: yes).
Items dropped as duplicates (must name the equivalent target text): 3 (rows 1, 7, 9)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S04 review) — verdict ACCEPT — 2026-09-29

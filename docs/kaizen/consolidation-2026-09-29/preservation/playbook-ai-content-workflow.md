# Preservation map — playbook-ai-content-workflow → playbook-content-production

Filled from [preservation-map-template.md](../preservation-map-template.md) (Social Kaizen S03, task S03-T06). See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/playbooks/playbook-ai-content-workflow/SKILL.md @ 7c60138 + S02 working-tree re-points (retired S02 skill names replaced by their owners; the ALIAS.md keeps that text) (461 lines; reads Aug–Sep 2026: 0; fan-in 5)
Destination reference: skills/playbooks/playbook-content-production/references/ai-assisted-production-workflow.md (abbreviated below as `AAPW`)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When / Do Not Use When, Required Inputs contract table, Capability and Permission Boundaries, Degraded Mode, Workflow steps 1–5, Outputs, Evidence Produced, Quality Standards, anti-AI-slop and East African English reference links (identical to the target's contract block apart from the job name) | Target SKILL.md dual-compat block | DROPPED-DUPLICATE-OF target SKILL.md § Use When, § Capability and Permission Boundaries, § Degraded Mode, § Workflow, § Outputs, § Evidence Produced, § Quality Standards and § References (identical wording, "Content Production" in place of "Ai Content Workflow") | ticked |
| 2 | Decision row: "AI output contains an unsupported claim or generic filler → Return it to evidence and editorial review → Fast production of misleading content" | AAPW § Decision rules row 1; target SKILL.md § Decision Rules (new AI row) | MOVED | ticked |
| 3 | Decision rows: "Inputs and authority are complete…", "Evidence or tooling is incomplete…", "Action publishes, spends, contacts people…" | Target SKILL.md § Decision Rules | DROPPED-DUPLICATE-OF target § Decision Rules rows 2–4 (identical text) | ticked |
| 4 | Anti-patterns (6 bullets: inventing facts; copying patterns; volatile details from memory; inaccessible account treated as healthy; acting from planning authority; actions without owner/timing/acceptance) | Target SKILL.md § Anti-Patterns | DROPPED-DUPLICATE-OF target § Anti-Patterns (identical six bullets) | ticked |
| 5 | § Required Input (7 items: client/industry; 3 tone words from 04-brand-voice-intake; vocabulary avoid list; pillars from 10-content-pillars; platforms in scope; team size solo / 2–5 / 6+; country/city default Uganda/EA) | AAPW § Inputs (all 7 kept; skill names made live links) | MOVED | ticked |
| 6 | § 1. AI Tool Overview (EA-Accessible) (start with ChatGPT + Canva; 14-row tool table with EA access; starting recommendation; Grammarly week two) | AAPW § Procedure Step 2; § Decision rules row 4 | MOVED | ticked |
| 7 | Content pruning note (Roth & neuroflash 2024/2025; Frase.io or manual audits quarterly; library without pruning accumulates liability) | AAPW § Procedure Step 2 (Content pruning) | MOVED | ticked |
| 8 | § 2. Brand Voice Calibration (Step 0) incl. Step 0 — Formal Brand Voice Capture (brand-voice-ai-training 6-step process) | AAPW § Procedure Step 3; § Decision rules row 2 | MOVED | ticked |
| 9 | § The Brand Context Block (verbatim prompt prefix with 12 banned words) | AAPW § Procedure Step 3 (code block verbatim) | MOVED | ticked |
| 10 | § Saving and Reusing the Brand Context Block (ChatGPT Custom Instructions; session-start paste via Google Doc / WhatsApp Saved Messages; team WhatsApp group) | AAPW § Procedure Step 3 (Saving and reusing) | MOVED | ticked |
| 11 | § Refining the Brand Context Block Over Time (after four weeks; 3 adjustment rules; date each version) | AAPW § Procedure Step 3 (Refining) | MOVED | ticked |
| 12 | § 3. Prompt Library — Core Templates: Prompt Structure Alpha-Beta-Gamma-Delta-Epsilon (5-row table, Upadhyay 2024); PAS/AIDA default; 7 frameworks pointer; British English rule | AAPW § Procedure Step 4 | MOVED | ticked |
| 13 | Prompts 1–3 (Captions: short <100 chars; medium 100–200 chars; carousel/thread 5–7) | AAPW § Procedure Step 4 (Captions), verbatim | MOVED | ticked |
| 14 | Prompts 4–5 (Content Ideas: 30 monthly ideas from pillars; 10 seasonal/campaign ideas incl. Eid) | AAPW § Procedure Step 4 (Content ideas), verbatim | MOVED | ticked |
| 15 | Prompt 6 (Hashtags: 15 = 3 broad >1M, 6 mid 100k–1M, 6 niche <100k; ≥2 Uganda/EA) | AAPW § Procedure Step 4 (Hashtags), verbatim | MOVED | ticked |
| 16 | Prompts 7–8 (Repurposing long content → 3 captions of 100–150 words; complaint response under 80 words, no legal liability, resolve via WhatsApp/DM) and pointer to prompt-engineering-library for the full set | AAPW § Procedure Step 4 (Repurposing and community management), verbatim | MOVED | ticked |
| 17 | § 4. Quality Control Protocol (6 checks: brand voice, British English with spelling pairs, banned vocabulary incl. 17-word blacklist, accuracy, human touch, cultural localisation) | AAPW § Procedure Step 5 (checklist) | MOVED | ticked |
| 18 | § Proof of Human (High-Stakes Content) (Schaefer 2025; 3 methods; apply to claims of authority) | AAPW § Procedure Step 5 (Proof of Human); § Decision rules row 7 | MOVED | ticked |
| 19 | Humaniser pointer ("For AI humanisation … invoke anti-ai-slop (humanising rewrite passes)"; `ai-content-humaniser` at 7c60138) | AAPW § Procedure Step 5 (Human Authenticity Gate) and § Companion skills, linked to anti-ai-slop references/humanising-rewrite-passes.md | MERGED-WITH-EXISTING (anti-ai-slop references/humanising-rewrite-passes.md) | ticked |
| 20 | § 5. Workflow Integration: Weekly AI-Assisted Content Workflow (Monday drafting 10 min, review 30 min, scheduling 20 min; total 60 min; schedule not auto-publish) | AAPW § Procedure Step 6 (table) | MOVED | ticked |
| 21 | § Time Saving Calculation — 5-Post Instagram Account (6-row table: 110 vs 65 min/week; 7.3 vs 4.3 h/month; 3 h/client; 15 h/month for five clients) | AAPW § Procedure Step 6 (all figures kept; labelled as planning scenario) | MOVED | ticked |
| 22 | Advanced automation pointer (`playbook-ai-automation-workflow` at 7c60138) | AAPW § When to use this reference, § Procedure Step 6, § Companion skills → playbook-marketing-automation references/ai-automation-recipes.md | MERGED-WITH-EXISTING (playbook-marketing-automation references/ai-automation-recipes.md) | ticked |
| 23 | § 6. Content Maturity Model (4-stage table; Upadhyay 2024; name stage in introduction; no Stage 4 tools for Stage 1) | AAPW § Procedure Step 1; § Decision rules row 3 | MOVED | ticked |
| 24 | § 7. What AI Cannot Do (Schaefer 2025; 5 structural limitations) | AAPW § Limits (What AI cannot do) | MOVED | ticked |
| 25 | § 8. What NOT to Use AI For (6 prohibitions) | AAPW § Limits (What NOT to use AI for); § Decision rules row 6 | MOVED | ticked |
| 26 | § 9. AI Disclosure Policy (required / best practice / not required; when in doubt disclose; policy-ai-content-ethics pointer) | AAPW § Procedure Step 8 (disclosure table); § Decision rules row 8 | MOVED | ticked |
| 27 | § 10. Platform-Specific AI Tips (LinkedIn, TikTok, WhatsApp, Instagram, Email) | AAPW § Procedure Step 7 (table; "Prompt 8 from prompt-engineering-library" re-pointed to its § Email Subject Line and Preview Text) | MOVED | ticked |
| 28 | § 11. Iterative AI Model Improvement Protocol (Ching & Mothi 2025; 4 triggers; versioning; sharing; quarterly review; 12-month asset) | AAPW § Procedure Step 8 (Iterative prompt improvement); § Decision rules row 10 | MOVED | ticked |
| 29 | § 12. Hallucination Management Gate (Mizrahi 2024; Evelyn 2025; web-search instruction quote; independent verification; difference from Accuracy Check) | AAPW § Procedure Step 5 (Hallucination Management Gate); § Decision rules row 5 | MOVED | ticked |
| 30 | § 13. Contextual Continuity Notes (Evelyn 2025; re-paste block; 8–10 exchanges; team hand-over) | AAPW § Procedure Step 8 (Contextual continuity) | MOVED | ticked |
| 31 | § 14. AI Content Watermarking (Ching & Mothi 2025; SynthID audio; images/video; production record; chain of custody) | AAPW § Procedure Step 8 (AI content watermarking) | MOVED | ticked |
| 32 | § Related Skills (6-row table) | AAPW § Companion skills (6 rows, live links; retired names re-pointed as in rows 19 and 22) | MOVED | ticked |
| 33 | § Human Authenticity Gate (mandatory before client delivery; Golden Rule) | AAPW § Procedure Step 5 (Human Authenticity Gate); § Acceptance checklist last item | MOVED | ticked |
| 34 | § Quality Criteria (10 items) | AAPW § Acceptance checklist (all 10 kept, plus the authenticity gate) | MOVED | ticked |
| 35 | Citation: Upadhyay (2024) [*Generative AI for Marketing*] | AAPW § Sources (with reconcile note on author initials and publisher) | MOVED | ticked |
| 36 | Citation: Schaefer (2025) | AAPW § Sources (with reconcile note against *Audacious* (2025) and *Belonging to the Brand* (2023)) | MOVED | ticked |
| 37 | Citation: Roth & neuroflash (2024/2025) | AAPW § Sources as Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing Teams* | MOVED | ticked |
| 38 | Citation: Ching & Mothi (2025) | AAPW § Sources as Ching, V. and Mothi, D. (2025) *AI for Creatives*, CRC Press | MOVED | ticked |
| 39 | Citation: Mizrahi (2024) | AAPW § Sources | MOVED | ticked |
| 40 | Citation: Evelyn (2025) | AAPW § Sources | MOVED | ticked |
| 41 | Reference files | none (source has no `references/` directory) | n/a | ticked |
Unique facts with register IDs carried: none (the source cites no `docs/source-registers/source-register.json` ID; freshness re-checked: NOT_ASSESSED)
Items dropped as duplicates (must name the equivalent target text): 3 (rows 1, 3, 4)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S03 review) — verdict ACCEPT_WITH_DOCUMENTED_LIMITATIONS (Ching/Mothi initials inconsistent across the engine (reconcile note added); ALIAS.md carries S02 re-points) — 2026-09-29

# Preservation map — image-prompt-engineer → prompt-engineering-library

Filled from [preservation-map-template.md](../preservation-map-template.md) for Social Kaizen S03-T09. See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/content-writing/image-prompt-engineer/SKILL.md @ 7c60138 (214 lines; reads Aug–Sep 2026: 0; fan-in 1)
Destination reference: skills/content-writing/prompt-engineering-library/references/image-prompt-patterns.md (abbreviated `IPP` below)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When, Do Not Use When, Required Inputs table, Capability and Permission Boundaries, Degraded Mode, Decision Rules (3 generic rows), Workflow steps 1–6, Outputs, Evidence Produced, Quality Standards bullets 1–4, Anti-Patterns bullets 1–5 | prompt-engineering-library/SKILL.md same-named sections | DROPPED-DUPLICATE-OF target SKILL.md `Use When` … `Anti-Patterns` (identical templated text, differing only in the deliverable name "image prompt engineer deliverable" vs "reusable prompt library") | ticked |
| 2 | References: link to caption-writer; link to AGENTS.md | prompt-engineering-library/SKILL.md § References | DROPPED-DUPLICATE-OF target § References (same two bullets: caption-writer "is the nearest routing comparison for this skill" and "Repository agent guide … defines the engine-wide market, safety and anti-slop gates") | ticked |
| 3 | Required Input (7 items: business name, industry, country/city default Uganda/Kampala, primary goal, platform, brand visual anchors, subject matter) | IPP § Inputs to collect before any image prompt | MOVED | ticked |
| 4 | The Golden Rule (AI aesthetic signs; one eight-layer prompt beats ten vague attempts) | IPP § The Golden Rule | MOVED | ticked |
| 5 | The Eight-Layer Image Prompt Anatomy (intro: all eight layers; default layer produces generic aesthetic) | IPP § Procedure — the eight-layer image prompt anatomy + § Decision rules row 1 | MOVED | ticked |
| 6 | Layer 1 — Subject (specific example; EA nationality/city/context; "African" insufficient) | IPP § Procedure step 1 | MOVED | ticked |
| 7 | Layer 2 — Environment (Kampala high-rise example; contemporary dress unless traditional required) | IPP § Procedure step 2 + § Decision rules row 3 | MOVED | ticked |
| 8 | Layer 3 — Lighting (6 quality options, 5 direction options, window-light example) | IPP § Procedure step 3 | MOVED | ticked |
| 9 | Layer 4 — Colours (5 palette options; brand palette; true-to-life East African skin tones) | IPP § Procedure step 4 | MOVED | ticked |
| 10 | Layer 5 — Mood (5 registers; mood steers expression, posture, saturation) | IPP § Procedure step 5 | MOVED | ticked |
| 11 | Layer 6 — Composition (7 framings; 9:16, 1:1, 16:9 aspect ratios) | IPP § Procedure step 6 | MOVED | ticked |
| 12 | Layer 7 — Style (photography styles, media, no named photographer; editorial example) | IPP § Procedure step 7 + § Decision rules row 6 | MOVED | ticked |
| 13 | Layer 8 — Technical Parameters table (Midjourney, DALL-E 3, Stable Diffusion, Flux, Adobe Firefly; 5 rows) | IPP § Procedure step 8 table (plus a currency note) | MOVED | ticked |
| 14 | The Negative Prompt Library (universal list, people list, 4 platform application rules) | IPP § Negative prompt library | MOVED | ticked |
| 15 | Brand Visual Identity Translation Protocol (4 steps) | IPP § Brand visual identity translation protocol | MOVED | ticked |
| 16 | Cultural Accuracy in East African Image Prompts (BuzzFeed 2023 study; 5 rules) | IPP § Cultural accuracy in East African image prompts + § Decision rules rows 2–5 | MOVED | ticked |
| 17 | Full Prompt Construction Example (Kampala financial services brief; full Midjourney prompt with `--ar 4:5 --v 6 --seed 44821 --style raw --no …`) | IPP § Worked example — full prompt construction | MOVED | ticked |
| 18 | Platform-Specific Quick Reference (5-row strength/syntax table) | IPP § Platform quick reference | MOVED | ticked |
| 19 | Quality Criteria (7 standards) | IPP § Release checklist for image prompts (7 items) + § Decision rules rows 8–9 | MOVED | ticked |
| 20 | Citation: LetsEnhance (2024) *How to Write AI Image Prompts — From Basic to Pro*, LetsEnhance.io | IPP § Procedure attribution + § Sources | MOVED | ticked |
| 21 | Citation: BuzzFeed (2023) AI "Barbie" diversity brief findings | IPP § Cultural accuracy + § Sources | MOVED | ticked |
| 22 | Reference files | — | None exist in the source (no `references/` folder) | ticked |
| 23 | Routing: when image prompts are needed | prompt-engineering-library/SKILL.md § Decision Rules (new row) and § References (new bullet) | MOVED | ticked |
Unique facts with register IDs carried: none — the source cites no source-register IDs (freshness re-checked: NOT_ASSESSED; a platform-syntax currency note was added to IPP step 8)
Items dropped as duplicates (must name the equivalent target text): 2
Reviewer: independent review agent (Claude Opus 5.5, read-only, S03 review) — verdict ACCEPT — 2026-09-29

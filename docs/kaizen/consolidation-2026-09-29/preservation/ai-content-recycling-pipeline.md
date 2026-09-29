# Preservation map — ai-content-recycling-pipeline → meta-content-repurposing

Filled from [preservation-map-template.md](../preservation-map-template.md) for Social Kaizen S03-T05. See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/ai-marketing/ai-content-recycling-pipeline/SKILL.md @ 7c60138 (203 lines; reads Aug–Sep 2026: 0; fan-in 0)
Destination reference: skills/meta-analytics-ops/meta-content-repurposing/references/ai-assisted-recycling-pipeline.md (abbreviated `AARP` below)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Do Not Use When bullet 2 (no publish/spend/live change/unsupported claims), Capability and Permission Boundaries, Degraded Mode, Outputs row 1, Evidence Produced, Quality Standards bullets 1–3, Workflow steps 1–6 (generic confirm / inventory / select / produce / test / deliver) | meta-content-repurposing/SKILL.md same-purpose sections | DROPPED-DUPLICATE-OF target SKILL.md `Do Not Use When` bullet 2, `Capability and permission boundary`, `Degraded mode`, `Outputs`, `Evidence Produced`, `Quality Standards`, `Workflow` steps 1–6 (same templated text: "Do not publish, spend, change a live account…", "publishing … require separate explicit authority", "return the narrowest useful qualified …", "Each material claim records its source/date…", confirm / inventory / apply / verify / produce / anti-slop sequence) | ticked |
| 2 | Use When: deliverable is an operating pipeline specification | AARP § 1 When to use | MOVED | ticked |
| 3 | Do Not Use When bullet 1 / Workflow step 1: route to `ai-readiness-diagnostic` for the narrower output | AARP § 1 When to use (third bullet, linked) | MOVED | ticked |
| 4 | Required Inputs row 1: AI marketing use-case brief, intended human control point and success measure | AARP § 2 Inputs | MOVED | ticked |
| 5 | Required Inputs row 2: brand voice, offer facts, constraints and approvals — do not invent names, prices, results or approvals | AARP § 2 Inputs | MOVED | ticked |
| 6 | Required Inputs row 3: performance/platform/research evidence — narrowest reviewable version, flag missing evidence | AARP § 2 Inputs | MOVED | ticked |
| 7 | Decision row: data readiness, AI maturity and risk → lowest viable automation level with human approval gate | AARP § 4 Decision rules row 1 | MOVED | ticked |
| 8 | Decision row: required fact or approval missing → stop claim, request it or use placeholder | AARP § 4 Decision rules row 3 | MOVED | ticked |
| 9 | Decision row: evidence partial but useful draft possible → qualified draft with gaps and next verification step | meta-content-repurposing/SKILL.md § Decision rules row 2 | DROPPED-DUPLICATE-OF target § Decision rules row 2 "A material input is missing or contradictory — Stop that decision, request clarification, or issue a labelled partial result." | ticked |
| 10 | Quality Standards bullet 4: run `anti-ai-slop` ship gate; blocking factual/cultural/safety/permission defect stops release | AARP § 7 Quality gate (last item) | MERGED-WITH-EXISTING (target § Workflow step 6 states the same gate) | ticked |
| 11 | Anti-pattern: writing before objective and audience are known | AARP § 10 Anti-patterns bullet 1 | MOVED | ticked |
| 12 | Anti-pattern: reusing a neighbouring skill's template because headings look similar | AARP § 10 Anti-patterns bullet 2 | MOVED | ticked |
| 13 | Anti-pattern: price/result/quotation/platform limit/cultural claim without traceable source | AARP § 10 Anti-patterns bullet 3 | MOVED | ticked |
| 14 | Anti-pattern: missing access/evidence/native-language review treated as approval | AARP § 10 Anti-patterns bullet 4 | MOVED | ticked |
| 15 | Anti-pattern: publishing/sending/spending/changing live account from drafting authority | AARP § 10 Anti-patterns bullet 5 | MOVED | ticked |
| 16 | Outputs row 2: Decision and gap note (route, evidence, unresolved inputs, authority) | AARP § 9 Acceptance checklist (last item) | MOVED | ticked |
| 17 | References: link to ai-readiness-diagnostic; link to AGENTS.md | AARP § 1 (ai-readiness-diagnostic link); engine gate already in target § Workflow step 6 | MERGED-WITH-EXISTING | ticked |
| 18 | Required Input (6 items: business and industry, country default Uganda, source ≥500 words, active platforms, brand voice, topics to avoid) | AARP § 2 Inputs | MOVED | ticked |
| 19 | The Core Principle (create once / publish once waste; 10 assets in under 60 minutes; Roth and neuroflash 2024; constraint is extraction and reformatting) | AARP § 3 Core principle | MOVED | ticked |
| 20 | The 10-Asset Pipeline — Source: one long-form piece (500–1,500 words) | AARP § 5 Procedure (Source paragraph) | MOVED | ticked |
| 21 | Asset 1 — Facebook post (100–150 words) + prompt | AARP § 5 Asset 1 (prompt verbatim) | MOVED | ticked |
| 22 | Asset 2 — Instagram caption (50–80 words + 10 hashtags) + prompt | AARP § 5 Asset 2 (prompt verbatim) | MOVED | ticked |
| 23 | Asset 3 — LinkedIn post (150–200 words) + prompt | AARP § 5 Asset 3 (prompt verbatim) | MOVED | ticked |
| 24 | Asset 4 — TikTok / Reels script (30 seconds) + prompt | AARP § 5 Asset 4 (prompt verbatim) | MOVED | ticked |
| 25 | Asset 5 — X / Twitter post (under 280 characters) + prompt | AARP § 5 Asset 5 (prompt verbatim) | MOVED | ticked |
| 26 | Asset 6 — Instagram carousel outline (5 slides) + prompt | AARP § 5 Asset 6 (prompt verbatim) | MOVED | ticked |
| 27 | Asset 7 — WhatsApp broadcast (under 700 characters) + prompt | AARP § 5 Asset 7 (prompt verbatim) | MOVED | ticked |
| 28 | Asset 8 — Email newsletter paragraph (80–100 words) + prompt | AARP § 5 Asset 8 (prompt verbatim) | MOVED | ticked |
| 29 | Asset 9 — Quote card text (under 20 words) + prompt | AARP § 5 Asset 9 (prompt verbatim) | MOVED | ticked |
| 30 | Asset 10 — Podcast / audio outline (3 minutes) + prompt | AARP § 5 Asset 10 (prompt verbatim) | MOVED | ticked |
| 31 | Platform Adaptation Rules table (7 rows: Facebook, Instagram, LinkedIn, TikTok/Reels, X/Twitter, WhatsApp, Email) | AARP § 6 (all 7 rows) | MOVED | ticked |
| 32 | Quality Gate (6 checks: standalone, brand voice, local Uganda/EA reference, read aloud, hashtags, human approval) | AARP § 7 (all 6 checks) | MOVED | ticked |
| 33 | Time Benchmark (prompts 15–20 min; review 30–40 min; total under 60 min) | AARP § 8 | MOVED | ticked |
| 34 | Quality Criteria (8 bullets) | AARP § 9 Acceptance checklist (all 8 bullets) | MOVED | ticked |
| 35 | Citation: Roth, H. and neuroflash (2024) *AI Strategy 2025 for Marketing Teams* | AARP § 3 and § Sources | MOVED | ticked |
| 36 | Citation: Sweenor, D.E. and Mulkers, Y. (2024) *Generative AI Business Applications*. TinyTechMedia | AARP § Sources | MOVED | ticked |
| 37 | Reference files in skills/ai-marketing/ai-content-recycling-pipeline/references/ | — | None exist (no references/ folder) | ticked |
Unique facts with register IDs carried: none (source cites no source-register IDs; freshness re-checked: NOT_ASSESSED)
Items dropped as duplicates (must name the equivalent target text): 2 (rows 1, 9)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S03 review) — verdict ACCEPT — 2026-09-29

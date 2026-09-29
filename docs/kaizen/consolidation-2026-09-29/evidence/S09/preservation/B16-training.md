# S09 preservation log — B16-training

Worker: S09 B16 worker (Claude Opus 5.5), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10.

## training-ai-foundations — 204 → 118 lines (gated shared ratio 27.8 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic Required Inputs rows, generic Workflow steps 2–4 and 6, generic Outputs/Evidence rows, Capability, Degraded, 2 generic decision rows, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections (domain inputs, workflow, outputs, evidence, 4 new domain decision rows, 6 domain anti-patterns) |
| 2 | Decision rows "Learners lack a shared AI mental model" and "Learners understand basic AI limits…" | KEPT | SKILL.md § Decision Rules |
| 3 | Workflow step 1 (foundations vs prompt-writing module) and step 5 (correct and rerun) | CONDENSED-IN-PLACE | SKILL.md § Workflow steps 1, 7 |
| 4 | Quality bullets "Keep Uganda/East Africa, British English, EAT, UGX, WhatsApp-first…" and "Apply anti-ai-slop… block release on an F" | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards bullet 8; § Workflow step 7 |
| 5 | "## How to Use This Skill" (facilitator-ready document, not a slide deck; `chwezi-design-engine` hand-off) | MOVED | references/training-guide-plan.md § How to use the guide |
| 6 | "## Required Input" (8 intake items) | MOVED | references/training-guide-plan.md § Intake questions; key items folded into SKILL.md § Required Inputs |
| 7 | "## Output: Complete Training Guide" (four modules, plain English, tone) | MOVED | references/training-guide-plan.md § How to use the guide |
| 8 | "## Training Overview" (programme, 150 minutes, four primary sources) | MOVED | references/training-guide-plan.md § Training Overview template |
| 9 | "## Foundations and limits curriculum" / "## Tools and human-review curriculum" (pointer lines) | MERGED-INTO-CONTRACT | SKILL.md § Workflow steps 3–5 and § References |
| 10 | "## Related Skills" (5 items) | MERGED-INTO-CONTRACT | SKILL.md § References (each with read-when line) |
| 11 | "## Co-Pilot vs Co-Thinker (Farri and Rosani, 2025)" | MOVED | references/training-guide-plan.md § Co-Pilot vs Co-Thinker |
| 12 | "## The Three Waves of AI in Marketing (Nayebi, 2025)" | MOVED | references/training-guide-plan.md § The Three Waves |
| 13 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 14 | References: AGENTS.md, prompt-writing-module.md | KEPT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 4 flagged → 2 scaffolding, 2 paraphrased (listed below), 0 lost; validator clean; routecheck 0 changed.
Paraphrased lines: "Load foundations-and-limits.md for this part…" and "Load tools-and-human-review.md for this part…" → SKILL.md § Workflow steps 3–5 and § References.
Noticed, not changed: none.

## training-client-team — 459 → 113 lines (gated shared ratio 12.9 % → 0.0 %)

S07 hand-off (trim curricula and session plans into references) completed: all seven modules, cover page and exercises now live in `references/handover-workbook-modules.md`.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic Required Inputs rows, Workflow steps 1–4 and 6, Outputs/Evidence rows, Capability, Degraded, 2 generic decision rows, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections (domain inputs, workflow, outputs, evidence, 4 new domain decision rows, 6 domain anti-patterns) |
| 2 | Decision rows "A strategy exists and staff need assigned operating competence" and "The client will work independently after handover" | KEPT | SKILL.md § Decision Rules |
| 3 | Quality bullets "Keep Uganda/East Africa…" and "Apply anti-ai-slop…" | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards bullet 7; § Workflow step 7 |
| 4 | "## How to Use This Skill" (printable workbook, 2-hour in-person, not slides) | MOVED | references/handover-workbook-modules.md § How to use this workbook; fact also in SKILL.md intro |
| 5 | "## Required Input" (11 intake items) | MOVED | references/handover-workbook-modules.md § Intake questions; folded into SKILL.md § Required Inputs |
| 6 | "## Output: Complete Training Workbook" | MOVED | references/handover-workbook-modules.md § Workbook content |
| 7 | "### Cover Page" | MOVED | references/handover-workbook-modules.md § Cover Page |
| 8 | "### Module 1: Our Social Media Strategy" (20 minutes) | MOVED | references/handover-workbook-modules.md § Module 1 |
| 9 | "### Module 2: What Each Team Member Can and Cannot Post" (15 minutes) | MOVED | references/handover-workbook-modules.md § Module 2 |
| 10 | "### Module 3: How to Take Good Photos and Videos on a Smartphone" (25 minutes) | MOVED | references/handover-workbook-modules.md § Module 3 |
| 11 | "### Module 4: How to Use [Scheduling Tool]" (20 minutes, Buffer steps) | MOVED | references/handover-workbook-modules.md § Module 4 |
| 12 | "### Module 5: The Approval Workflow" (10 minutes) | MOVED | references/handover-workbook-modules.md § Module 5 |
| 13 | "### Module 6: How to Respond to Customer Messages" (15 minutes, 3 standard messages, escalation) | MOVED | references/handover-workbook-modules.md § Module 6; escalation also in SKILL.md § Decision Rules |
| 14 | "### Module 7: How to Report Performance" (10 minutes, weekly template) | MOVED | references/handover-workbook-modules.md § Module 7 |
| 15 | "### Workshop Exercises Summary" (3 exercises) | MOVED | references/handover-workbook-modules.md § Workshop Exercises Summary |
| 16 | "## Quality Criteria" (8 checklist items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 17 | References: AGENTS.md, diy-content-handbook.md | KEPT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding (generic evidence input row, generic workflow step 1, generic output row), 0 paraphrased, 0 lost; validator clean; routecheck 0 changed.
Paraphrased lines: none flagged.
Noticed, not changed: `## Use When` names Meta Business Suite, while the HEAD Module 4 intake offered only Buffer / Hootsuite / other; left as is (routing frozen, reference text unchanged).

## training-smartphone-video-production — 348 → 113 lines (gated shared ratio 13.8 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic Required Inputs rows, Workflow steps 1–4 and 6, Outputs/Evidence rows, Capability, Degraded, 2 generic decision rows, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections (domain inputs, workflow, outputs, evidence, 6 new domain decision rows, 6 domain anti-patterns) |
| 2 | Decision row "Learners need production competence with available phones and field conditions" | KEPT | SKILL.md § Decision Rules |
| 3 | Quality bullets "Keep Uganda/East Africa…" and "Apply anti-ai-slop…" | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards bullets 1 and 7; § Workflow step 7 |
| 4 | "## Required Input" (7 intake items) | MOVED | references/phone-video-training-guide.md § Intake questions; folded into SKILL.md § Required Inputs |
| 5 | "## Context: East African Field Conditions" | MOVED | references/phone-video-training-guide.md § Context; summarised in SKILL.md intro |
| 6 | "## Section 1 — Equipment" (UGX prices) | MOVED | references/phone-video-training-guide.md § Section 1; lapel-mic price also in SKILL.md § Decision Rules |
| 7 | "## Section 2 — Lighting" | MOVED | references/phone-video-training-guide.md § Section 2; golden-hour rule also in § Decision Rules |
| 8 | "## Section 3 — Audio" | MOVED | references/phone-video-training-guide.md § Section 3 |
| 9 | "## Section 4 — Framing and Composition" | MOVED | references/phone-video-training-guide.md § Section 4 |
| 10 | "## Section 5 — Camera Settings" | MOVED | references/phone-video-training-guide.md § Section 5 |
| 11 | "## Section 6 — Shooting for Platform Formats" (table, hook rule) | MOVED | references/phone-video-training-guide.md § Section 6 |
| 12 | "## Section 7 — Simple Editing on Your Phone" | MOVED | references/phone-video-training-guide.md § Section 7 |
| 13 | "## Section 8 — Uploading on Low Bandwidth" | MOVED | references/phone-video-training-guide.md § Section 8 |
| 14 | "## Section 9 — Common Mistakes to Avoid" (7 mistakes) | MOVED | references/phone-video-training-guide.md § Section 9; 5 also in SKILL.md § Anti-Patterns |
| 15 | "## Quality Criteria" (intro line + 8 criteria) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 16 | References: AGENTS.md | KEPT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 4 flagged → 3 scaffolding (generic evidence input row, generic workflow step 1, generic output row), 1 paraphrased (listed below), 0 lost; validator clean; routecheck 0 changed.
Paraphrased lines: "Good output from this skill meets all of the following standards:" → SKILL.md § Quality Standards heading.
Noticed, not changed: the Section 6 platform table gives TikTok 15–60 sec and Reels 15–90 sec targets, WhatsApp Status 30 sec and under 16MB, with no register ID or date; kept as house guidance.

## training-social-media-fundamentals — 435 → 114 lines (gated shared ratio 12.1 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic Required Inputs rows, Workflow steps 1–4 and 6, Outputs/Evidence rows, Capability, Degraded, 2 generic decision rows, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections (domain inputs, workflow, outputs, evidence, 6 new domain decision rows, 7 domain anti-patterns) |
| 2 | Decision row "Learners need conceptual foundations before operational handover" | KEPT | SKILL.md § Decision Rules |
| 3 | Quality bullets "Keep Uganda/East Africa…" and "Apply anti-ai-slop…" | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards; § Workflow step 6 |
| 4 | "## How to Use This Skill" (warm plain English, standalone document) | MOVED | references/fundamentals-guide-sections.md § How to use this guide; summarised in SKILL.md intro |
| 5 | "## Required Input" (7 intake items) | MOVED | references/fundamentals-guide-sections.md § Intake questions; folded into SKILL.md § Required Inputs |
| 6 | "## Output: Social Media Fundamentals Training Guide" | MOVED | references/fundamentals-guide-sections.md § Guide content |
| 7 | "### Cover Page" | MOVED | references/fundamentals-guide-sections.md § Cover Page |
| 8 | "### Section 1: What Social Media Marketing Actually Is" | MOVED | references/fundamentals-guide-sections.md § Section 1 |
| 9 | "### Section 2: Why Social Media Matters… in Uganda" (numbers incl. register WA-01, 2026-09-24) | MOVED | references/fundamentals-guide-sections.md § Section 2; WA-01 also in SKILL.md § Required Inputs |
| 10 | "### Section 3: Platform Primer" (table, 2-platform focus rule) | MOVED | references/fundamentals-guide-sections.md § Section 3; rule also in § Decision Rules |
| 11 | "### Section 4: How Algorithms Work" | MOVED | references/fundamentals-guide-sections.md § Section 4 |
| 12 | "### Section 5: The 80/20 Content Rule" (self-audit, example table) | MOVED | references/fundamentals-guide-sections.md § Section 5; audit threshold also in § Decision Rules |
| 13 | "### Section 6: Followers vs. Engagement" (formula, 3–5 % / 1 % thresholds) | MOVED | references/fundamentals-guide-sections.md § Section 6; 1 % threshold also in § Decision Rules |
| 14 | "### Section 7: The Content Basics" (hook, value, CTA, photo basics, posting frequency) | MOVED | references/fundamentals-guide-sections.md § Section 7 |
| 15 | "### Section 8: What to Track and Why" | MOVED | references/fundamentals-guide-sections.md § Section 8 |
| 16 | "### Section 9: The Most Common Mistakes" (7 mistakes) | MOVED | references/fundamentals-guide-sections.md § Section 9; all 7 also in SKILL.md § Anti-Patterns |
| 17 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 18 | References: AGENTS.md | KEPT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding (generic evidence input row, generic workflow step 1, generic output row), 0 paraphrased, 0 lost; validator clean; routecheck 0 changed.
Paraphrased lines: none flagged.
Noticed, not changed: Section 2 states "Facebook: approximately 3.2 million users in Uganda" with no source or date, while other skills cite register UG-FACEBOOK-ACCESS-2026 (Facebook access unstable in Uganda); kept as written. `## Use When` promises online safety (scams, account security, what not to post), but the HEAD guide has no safety section; routing frozen, gap left for a later content pass.

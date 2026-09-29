# S09 preservation log — B02-ai-marketing

Worker: S09 B02 worker agent (Claude), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10.

Frontmatter, H1, `## Use When` and `## Do Not Use When` are byte-identical to HEAD in all six skills (`routecheck.py`: routing sections changed 0). Generated contract scaffolding (the generic "AI marketing use-case brief…" and "Performance, platform or research evidence…" input rows, the generic capability and "Fallback: if files, network access…" degraded paragraphs, the three generic decision rows starting "Data readiness, AI maturity and risk…", "A required fact or approval is missing…" and "Evidence is partial…", the six-step generic workflow, the generic Outputs/Evidence rows, the four generic Quality Standards bullets, the five generic anti-patterns and the "nearest routing comparison" line) is shown as REPLACED-BY-CANONICAL in each table.

## ai-generative-search-optimisation — 178 → 137 lines (gated shared ratio 1.8 % → 1.4 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro: acknowledgement line and planning/audit-route sentences | CONDENSED-IN-PLACE | SKILL.md intro (acknowledgement kept verbatim) |
| 2 | Intro: "Load the AI search and social discovery rules (LinkedIn citation section)…" | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules (LinkedIn/citation findings row) and § References |
| 3 | "## Required Inputs" (4 domain rows) | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs (5 rows; baseline sources split out, robots/WAF added to stop list) |
| 4 | "## Capability and Permission Boundaries" (skill-specific wording) | REPLACED-BY-CANONICAL / domain sentence | SKILL.md § Capability (maintainer edits, production changes, certification kept in the domain sentence) |
| 5 | "## Degraded Mode" | REPLACED-BY-CANONICAL / domain clause | SKILL.md § Degraded Mode ("never convert a missing check into a pass" kept) |
| 6 | "## Decision Rules" (5 domain rows) | KEPT | SKILL.md § Decision Rules (5 kept + 2 domain rows from the intro and the robots/WAF paragraph) |
| 7 | "## Evidence-checked optimisation model — 2026-09-13" (intro, 5-row table, Google/ChatGPT/Perplexity paragraph) | KEPT | SKILL.md § SEO, AEO, GEO, AIO and SXO disposition (evidence-checked 2026-09-13), table verbatim |
| 8 | "## Workflow" (9 steps) | KEPT | SKILL.md § Workflow (stop rule made explicit in step 4) |
| 9 | Paragraph after workflow (customer-language bank, real-time bridge, three checks, books not platform authority) | MERGED-INTO-CONTRACT | SKILL.md § Workflow steps 5, 6 and 8 |
| 10 | "## Outputs" (4 rows) | KEPT | SKILL.md § Outputs (header set to the canonical form) |
| 11 | "## Evidence Produced" (4 rows) | KEPT | SKILL.md § Evidence Produced |
| 12 | "## Quality Standards" (5 bullets) | KEPT | SKILL.md § Quality Standards (6 bullets; one measurement bullet added) |
| 13 | "## Anti-Patterns" (7 bullets) | KEPT | SKILL.md § Anti-Patterns |
| 14 | "## References" (9 links) | KEPT | SKILL.md § References (each with "read when"; legal-market release gate added) |

Checks: factcheck 0 missing; linecheck 2 flagged → 0 scaffolding, 2 paraphrased, 0 lost; validator clean; SKILL.md 137 lines.
Paraphrased lines: "Read and search are the minimum capabilities. Planning and audit are read-only." → § Capability canonical sentence; "…or measurement data is unavailable, return the narrowest useful plan and label…" → § Degraded Mode.
Noticed, not changed: none.

## ai-readiness-diagnostic — 374 → 128 lines (gated shared ratio 7.7 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, capability, degraded, 3 generic decision rows, 6-step workflow, generic outputs/evidence, 4 QS bullets, 5 anti-patterns, routing line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" 3 domain rows (Data Foundation 0–3 audit; 90-day plan; canvas and roadmap) | KEPT | SKILL.md § Decision Rules (verbatim) + 5 domain rows from the body |
| 3 | "## References" (4 reference links + AGENTS.md) | KEPT | SKILL.md § References with "read when" |
| 4 | "## Purpose" | MOVED | references/readiness-diagnostic-method.md § Purpose; gist in SKILL.md intro |
| 5 | "## Required Inputs" (5 intake items, Y/N walk-through, uncertain = N) | MOVED + MERGED-INTO-CONTRACT | references/readiness-diagnostic-method.md § Required Inputs; SKILL.md § Required Inputs and Decision Rules |
| 6 | "## The 41-Item Diagnostic" (5 domain sub-sections, 41 questions) | MOVED | references/readiness-diagnostic-method.md § The 41-Item Diagnostic |
| 7 | "## Scoring" (Step 1 domain maxima, Step 2 Canvas bands, Step 3 thresholds) | MOVED + KEPT | references/readiness-diagnostic-method.md § Scoring; bands, maxima and thresholds also in SKILL.md § Scoring bands |
| 8 | "## Output Structure" (Sections 1–5, example table, 90-day blocks, tool tables, WhatsApp note) | MOVED | references/readiness-diagnostic-method.md § Output Structure; order in SKILL.md § Workflow step 5 |
| 9 | "## East African Market Context" | MOVED | references/readiness-diagnostic-method.md; 4–12 score range in SKILL.md § Scoring bands, patterns in Decision Rules/Anti-Patterns |
| 10 | "## AI Use Case Matrix (Venkatesan and Lecinski, 2026)" | MOVED | references/readiness-diagnostic-method.md; percentage bands in SKILL.md § Decision Rules |
| 11 | "## AI Maturity Wave Assessment (Nayebi, 2025)" | MOVED | references/readiness-diagnostic-method.md; question in SKILL.md § Workflow step 4 |
| 12 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |
| 13 | "## References" (4 citations and closing canvas pointer) | MOVED | references/readiness-diagnostic-method.md § References |

Checks: factcheck 0 missing; linecheck 11 flagged → 10 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "[ai-use-case-mapping] is the nearest routing comparison" → SKILL.md § References.
Noticed, not changed: the frontmatter description says "Uganda DPPA 2019" while the body and references say "DPA 2019" / "Data Protection and Privacy Act 2019" (same Act, two abbreviations); tool prices (ChatGPT Plus ~UGX 130,000/month, HubSpot Starter ~USD 20/month and others) are undated.

## ai-slop-audit — 224 → 138 lines (gated shared ratio 16.8 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, capability, degraded, 3 generic decision rows, 6-step workflow, generic outputs/evidence, 4 QS bullets, 5 anti-patterns, routing line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Responsibility audit" (paragraph + shared-standard link) | MOVED + MERGED-INTO-CONTRACT | references/audit-method.md § Responsibility audit (verbatim); rules in SKILL.md § Decision Rules rows 2 and 8 |
| 3 | "## References" (2 lines) | KEPT | SKILL.md § References |
| 4 | "## Machine-error audit extension" and "### Impeccable-derived overlay audit" | MOVED | references/audit-method.md (verbatim); SKILL.md § Workflow step 5 and Decision Rules rows 3–4 |
| 5 | Detector paragraph ("The detector. Given any social artefact…") | CONDENSED-IN-PLACE | SKILL.md intro; full text in references/audit-method.md |
| 6 | "## When this runs" (cadence, auto-run triggers) | MOVED | references/audit-method.md § When this runs; SKILL.md § Workflow steps 7–8 and Anti-Patterns |
| 7 | "## What slop is (the yardstick)" (Merriam-Webster 2025, Kommers et al.) | KEPT (verbatim) | SKILL.md § Yardstick and verified evidence |
| 8 | "## Audit method" Steps 1–4 (written, image, video gates; genericness score; human review; per-artefact checks) | MOVED | references/audit-method.md § Audit method (verbatim); summary in SKILL.md § Workflow steps 1–4 |
| 9 | "## Scoring & verdict" (grade table) | KEPT (verbatim, "Slopy" spelling kept) | SKILL.md § Grades |
| 10 | "## Output format (the audit report)" template | MOVED | references/audit-method.md § Output format |
| 11 | "## Discipline (anti-hallucination)" (3 bullets) | MOVED + MERGED-INTO-CONTRACT | references/audit-method.md; SKILL.md § Evidence Produced, Decision Rules ("clean" row) and Anti-Patterns |
| 12 | "## Why slop is a real risk worth auditing" (Spracklen et al., Veracode) | KEPT (verbatim) | SKILL.md § Yardstick and verified evidence |
| 13 | "## Required Input" (5 items) | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs (5 rows + evidence row); original list in references/audit-method.md |
| 14 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8; item 8 citation wording kept verbatim in references/audit-method.md) |
| 15 | "## See also" (4 routes) | MOVED | references/audit-method.md § See also; `anti-ai-slop` also in SKILL.md § References |

Checks: factcheck 0 missing; linecheck 11 flagged → 10 scaffolding, 1 paraphrased, 0 lost; validator clean. Verbatim check: every HEAD line containing Merriam-Webster, Kommers, Spracklen or Veracode, and every line of the yardstick, grade table and evidence sections, is present in the skill folder; the reference keeps a pointer under each heading kept in `SKILL.md`.
Paraphrased lines: "[ai-readiness-diagnostic] is the nearest routing comparison" → SKILL.md § References.
Noticed, not changed: grade C label reads "Slopy" (single p) in HEAD; kept as is.

## ai-use-case-mapping — 373 → 125 lines (gated shared ratio 7.6 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, capability, degraded, 3 generic decision rows, 6-step workflow, generic outputs/evidence, 4 QS bullets, 5 anti-patterns, routing line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" 3 domain rows (growth system; predictive analytics; co-thinking) | KEPT | SKILL.md § Decision Rules (verbatim) + 5 domain rows from the body |
| 3 | "## References" (3 reference links + AGENTS.md) | KEPT | SKILL.md § References with "read when" |
| 4 | "## Purpose" | MOVED | references/use-case-mapping-method.md; gist in SKILL.md intro |
| 5 | "## Required Input" (7 items) | MOVED + MERGED-INTO-CONTRACT | references/use-case-mapping-method.md; SKILL.md § Required Inputs (5 rows) |
| 6 | "## The 2×2 AI Use Case Framework" (axes, quadrant table, Q1–Q4 examples) | MOVED | references/use-case-mapping-method.md |
| 7 | "## Step 1" – "## Step 8" (activity list, mapping, scoring, matrix, summary, Top 5, defer, 90-day sequence) | MOVED | references/use-case-mapping-method.md; scoring rules also in SKILL.md § Priority scoring, sequence in Workflow and Decision Rules |
| 8 | "## EA-Specific Opportunities" (5 defaults) | MOVED | references/use-case-mapping-method.md; local-language review and data-scarcity rules in SKILL.md § Decision Rules |
| 9 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |
| 10 | "## Cross-References" (4 routes) | MOVED | references/use-case-mapping-method.md; three routes also in SKILL.md § References |
| 11 | "## References" (3 citations incl. ROI formula) | MOVED | references/use-case-mapping-method.md; ROI formula also in SKILL.md § Priority scoring |

Checks: factcheck 0 missing; linecheck 10 flagged → 9 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "[ai-readiness-diagnostic] is the nearest routing comparison" → SKILL.md § References.
Noticed, not changed: Step 3 priority bands overlap (Opportunity 4 with Current AI Use 0 fits both High and Medium; Opportunity 3–4 "OR" Current AI Use 1 vs Low "OR" Current AI Use 2); kept as written.

## anti-ai-slop — 230 → 162 lines (gated shared ratio 14.8 % → 1.1 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic input rows, capability, degraded, 3 generic decision rows, generic outputs/evidence, 4 QS bullets, 5 anti-patterns, routing line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" humanising row | KEPT | SKILL.md § Decision Rules (verbatim) + 7 domain rows |
| 3 | "## Workflow" steps 3–5 (one unit at a time, record decision, inspect context, moderation risk, one refinement) | MERGED-INTO-CONTRACT | SKILL.md § Workflow steps 2 and 6 |
| 4 | "## Responsibility overlay" (25 signs, hypothetical customers, shared standard) | MOVED + MERGED-INTO-CONTRACT | references/guardrails-and-overlays.md § Responsibility overlay (verbatim); SKILL.md § Decision Rules and Anti-Patterns |
| 5 | "## References" (humanising link, AGENTS.md) | KEPT | SKILL.md § References |
| 6 | "## Machine-error editorial gate" (ME1–ME7 table) and "### Impeccable-derived AS overlay" (AS1–AS7 table, evidence modes, carousel rule) | MOVED | references/guardrails-and-overlays.md (verbatim); SKILL.md § Workflow step 5 and Decision Rules |
| 7 | Guardrail intro paragraph ("The guardrail every social output passes…") | CONDENSED-IN-PLACE | SKILL.md intro |
| 8 | "## Real-time application" | MOVED | references/guardrails-and-overlays.md (verbatim); SKILL.md § Workflow step 2 and Anti-Patterns |
| 9 | "## What "AI slop" is" (Merriam-Webster 2025, Kommers et al., three properties, absence of intent, social examples) | KEPT (verbatim) | SKILL.md § Slop definition and the seven universal guardrails |
| 10 | "## The seven universal guardrails" (U1–U7 table) | KEPT (verbatim) | SKILL.md § Slop definition and the seven universal guardrails |
| 11 | "## Banned / high-risk vocabulary (the lexical tells)" | KEPT (verbatim, same heading, so the humanising reference pointer still resolves) | SKILL.md § Banned / high-risk vocabulary |
| 12 | "## Drop-in guardrail block" | MOVED | references/guardrails-and-overlays.md (verbatim) |
| 13 | "## Domain-specific avoidance" (EN, FR, image/video, campaign blocks) | MOVED | references/guardrails-and-overlays.md (verbatim); FR, image-brief and CTA rules also in SKILL.md § Decision Rules and Anti-Patterns |
| 14 | "## Ship gate" (9 boxes + rule) | KEPT (verbatim) | SKILL.md § Ship gate |
| 15 | "## Required Input" (6 items) | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs (6 rows); original list in references/guardrails-and-overlays.md |
| 16 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8); original list in references/guardrails-and-overlays.md |
| 17 | "## See also" (4 routes) | MOVED | references/guardrails-and-overlays.md; routes also in SKILL.md § References |

Checks: factcheck 0 missing; linecheck 9 flagged → 6 scaffolding, 3 paraphrased, 0 lost; validator clean. Verbatim check: every HEAD line of the slop definition, U1–U7 table, banned vocabulary and ship gate, and every line with Merriam-Webster, Kommers, Spracklen or Veracode, is present in `SKILL.md`; the reference keeps a pointer under each heading kept in `SKILL.md`.
Paraphrased lines: old workflow step 4 ("Inspect the surrounding brand, campaign, source, rights, and channel context…") → § Workflow step 2; old step 5 ("Test the unit against … moderation risk … one concrete refinement") → § Workflow step 6; "[ai-readiness-diagnostic] is the nearest routing comparison" → SKILL.md § References.
Noticed, not changed: the banned list cites "FSU/COLING-2025; PubMed "delve" +400%" without a full reference; kept as is.

## brand-voice-ai-training — 328 → 115 lines (gated shared ratio 12.8 % → 1.7 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic input rows, capability, degraded, 3 generic decision rows, 6-step workflow, generic outputs/evidence, 4 QS bullets, 5 anti-patterns, routing line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" RAG knowledge-base row | KEPT | SKILL.md § Decision Rules (verbatim) + 6 domain rows |
| 3 | "## References" (RAG link, AGENTS.md) | KEPT | SKILL.md § References |
| 4 | "## Why This Matters" | MOVED + CONDENSED-IN-PLACE | references/brand-context-block-method.md (verbatim); gist in SKILL.md intro |
| 5 | "## Required Inputs" (13-row input table) | MOVED + MERGED-INTO-CONTRACT | references/brand-context-block-method.md; SKILL.md § Required Inputs (6 grouped rows) |
| 6 | "## Step 1 — Capture the Voice Inputs" (ranked source priority, thin corpus, cultural references, tone scale) | MOVED | references/brand-context-block-method.md; rules in SKILL.md § Workflow step 1 and Decision Rules |
| 7 | "## Step 2 — Analyse the Sample Content" | MOVED | references/brand-context-block-method.md; SKILL.md § Workflow step 2 |
| 8 | "## Step 3 — Build the Brand Context Block" (template, standard ban list, critical notes, minimum three examples) and "### Character-Voice Differentiation" | MOVED | references/brand-context-block-method.md (verbatim) |
| 9 | "## Step 4 — Few-Shot Examples by Content Type" | MOVED | references/brand-context-block-method.md; SKILL.md § Workflow step 5 |
| 10 | "## Step 5 — Quality Test the Block" and "### Voice Replication Comparison Test" | MOVED | references/brand-context-block-method.md; SKILL.md § Workflow step 6 and Evidence Produced |
| 11 | "## Step 6 — Maintain and Update the Block" | MOVED | references/brand-context-block-method.md; SKILL.md § Workflow step 8 and Decision Rules |
| 12 | "## Quality Criteria" (11 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 bullets covering all 11); full list in references/brand-context-block-method.md § Quality Criteria |

Also edited: `references/brand-knowledge-base-rag.md` — three pointers "SKILL.md Steps 1–6 / Step 3 / Step 6" now link to `brand-context-block-method.md`, where those steps moved.

Checks: factcheck 0 missing; linecheck 8 flagged → 7 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "[ai-readiness-diagnostic] is the nearest routing comparison" → SKILL.md § References.
Noticed, not changed: the "Ranked source priority" rule is sourced to an "ECC `brand-voice` skill" rather than a published source; kept as is.

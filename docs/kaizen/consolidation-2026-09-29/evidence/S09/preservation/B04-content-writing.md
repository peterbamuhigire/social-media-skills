# S09 preservation log — B04-content-writing

Worker: Claude (S09 worker, Opus 5.5), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. The shared folder `skills/content-writing/references/` and `skills/content-writing/ALIAS.md` were not touched. Frontmatter, `## Use When` and `## Do Not Use When` were copied byte for byte from HEAD by script.

## blog-writer — 177 → 126 lines (gated shared ratio 25.5 % → 1.4 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (Required Inputs 3 generic rows, Capability, Degraded, Workflow steps 1–2, 4–7, Outputs 2 generic rows, Evidence row, Quality Standards 4 generic bullets, 5 generic anti-patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections (domain input rows, 8-step workflow, domain outputs and evidence) |
| 2 | "## Decision Rules" (3 generic rows + whitepaper/eBook row) | KEPT (whitepaper row verbatim; 3 generic rows rewritten with blog-specific conditions) + 2 domain rows added (nut paragraph, premium layer) | SKILL.md § Decision Rules |
| 3 | Workflow step 3 (three-wave SEO/SERP study, 3–7 intent clusters, top five results, `UNASSESSED`) | KEPT | SKILL.md § Workflow step 3 |
| 4 | Anti-pattern "Drafting from a keyword list or a single search result" and the 5 generic anti-patterns | KEPT (Fix format normalised) | SKILL.md § Anti-Patterns |
| 5 | Intro paragraph "Generate a complete, professional blog post…" | CONDENSED-IN-PLACE; full text MOVED | SKILL.md intro; references/article-build-method.md (top) |
| 6 | "## Required Input" (9 numbered questions, defaults) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (6 rows); references/article-build-method.md § Required Input |
| 7 | "## Article Structure" (### Frontmatter block, ### Article body 1–5) | MOVED (frontmatter limits also in Outputs; body order in Workflow step 5) | references/article-build-method.md § Article Structure |
| 8 | "## Writing Standards" (10 bullets + premium paragraph) | MOVED; key thresholds in Quality Standards; premium paragraph also in Decision Rules | references/article-build-method.md § Writing Standards |
| 9 | "## SEO Requirements" (4 bullets) | MOVED; condensed in Workflow step 6 and Quality Standards | references/article-build-method.md § SEO Requirements |
| 10 | "## Platform Adaptation Notes" (social cut-downs) | MOVED; summarised in Outputs row 4 | references/article-build-method.md § Platform Adaptation Notes |
| 11 | "## Human Authenticity Gate" | MOVED; gate kept in Workflow step 7 and Quality Standards | references/article-build-method.md § Human Authenticity Gate |
| 12 | "## Quality Criteria" (9 items) | MERGED-INTO-CONTRACT (7 bullets) + full list MOVED | SKILL.md § Quality Standards; references/article-build-method.md § Quality Criteria (full list) |
| 13 | "## References" table (5 rows) | MERGED-INTO-CONTRACT | SKILL.md § References (all 11 existing reference files + new one linked) |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding (generic workflow steps 1, 5, 6), 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: `references/storytelling.md` and `references/content-strategy.md` are written for one named consultant ("a Ugandan IT consultant with 15 years…", "Peter's b…") rather than any client; left as is.

## caption-writer — 278 → 128 lines (gated shared ratio 16.5 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded, Workflow steps 1–6, 2 generic output rows, evidence row, 4 generic quality bullets, 3 generic anti-patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" hashtag-strategy row | KEPT verbatim; 6 domain rows added (platform, CTA ambiguity, permission, premium, selling/ethics, AI disclosure) | SKILL.md § Decision Rules |
| 3 | Workflow step 7 (audience situation, narrative job, first-line hierarchy, readability, one CTA, accessibility, register) | KEPT | SKILL.md § Workflow step 6 |
| 4 | Quality bullet "Prefer concrete audience context… If the post uses AI, route through its disclosure and human-review rules" | CONDENSED-IN-PLACE | SKILL.md § Quality Standards bullet 6; § Decision Rules (AI row) |
| 5 | Anti-patterns "strong hook as sufficient", "visual or claim without permission" + 2 generic retained | KEPT | SKILL.md § Anti-Patterns |
| 6 | References (hashtag, phrase bank, ethics filter, AGENTS) | KEPT with "read when" | SKILL.md § References |
| 7 | "## How to Use This Skill" (3 paragraphs incl. premium and buyer-psychology rules) | MOVED; rules also in Workflow steps 4–5 and Decision Rules | references/caption-build-method.md § How to Use This Skill (buyer-psychology path adjusted one level) |
| 8 | "## Required Input" (12 bullets) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; references/caption-build-method.md § Required Input |
| 9 | "## Platform-Specific Rules" (### Instagram, Facebook, LinkedIn, TikTok, WhatsApp Broadcast, X / Twitter) | MOVED; lengths, hashtag counts and key rule summarised | references/caption-build-method.md § Platform-Specific Rules; SKILL.md § Platform conventions at a glance |
| 10 | "## Caption Quality Standards" (7 bullets) | MOVED; folded into Quality Standards | references/caption-build-method.md § Caption Quality Standards |
| 11 | "## EA-Specific Hashtag Communities" (3 tag lists + selection rule) | MOVED | references/caption-build-method.md § EA-Specific Hashtag Communities |
| 12 | "## Output Format" (Short/Medium/Long template + notes) | MOVED; summarised in Outputs | references/caption-build-method.md § Output Format |
| 13 | "## Example Application (Uganda — Food and Beverage)" (Nakibuuka Kitchen) | MOVED | references/caption-build-method.md § Example Application |
| 14 | "## Human Authenticity Gate" | MOVED; gate in Workflow step 7 and Quality Standards | references/caption-build-method.md § Human Authenticity Gate |
| 15 | "## Quality Criteria" (9 items) | MERGED-INTO-CONTRACT (7 bullets) + full list MOVED | SKILL.md § Quality Standards; references/caption-build-method.md § Quality Criteria (full list) |

Checks: factcheck 0 missing; linecheck 3 flagged → 2 scaffolding (generic workflow steps 1, 4), 1 paraphrased, 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: "Prefer concrete audience context, a purposeful sequence of hook/proof/choice/consequence… If the post uses AI…" → SKILL.md § Quality Standards bullet 6 and § Decision Rules "The post uses AI-generated content".
Noticed, not changed: `references/hashtag-and-keyword-tagging.md` § When to use this reference still points to "the SKILL.md `Platform-Specific Rules` and the `EA-Specific Hashtag Communities` list"; those sections now live in `references/caption-build-method.md` (same headings). Posting-time claim "Post between 7–9pm EAT for highest Facebook reach among Kampala audiences" is an unsourced example in the output template.

## content-ideas — 248 → 126 lines (gated shared ratio 14.3 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, Workflow steps 1–6, 2 generic output rows, evidence row, 4 generic quality bullets, 5 generic anti-patterns) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Workflow step 7 (per-idea narrative and learning fields) | KEPT | SKILL.md § Workflow step 5 |
| 3 | Workflow step 8 (blog programme: 15–25 topics, 200-word summaries, `docs/blogs/topics.md`) | KEPT | SKILL.md § Workflow step 1; § Decision Rules row 1 |
| 4 | Quality bullet "Use story structure… do not invent customer stories, results, permissions, cultural facts, or platform behaviour" | CONDENSED-IN-PLACE | SKILL.md § Decision Rules (customer story row) |
| 5 | Anti-pattern "Generating a list of hooks without a job…" | KEPT | SKILL.md § Anti-Patterns |
| 6 | References (blog topic briefs + companions, AGENTS) | KEPT with "read when"; source-buckets-and-series.md added | SKILL.md § References |
| 7 | "## How to Use This Skill" | CONDENSED-IN-PLACE (intro) + MOVED | SKILL.md intro; references/social-idea-build-method.md |
| 8 | "## Required Input" (9 bullets) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; references/social-idea-build-method.md § Required Input |
| 9 | "## Output Format" (30-idea table) | MOVED; summarised in Workflow step 4 and Outputs | references/social-idea-build-method.md § Output Format |
| 10 | "## Distribution Rules" (platform minimums, content types, pillar maths, categories) | CONDENSED-IN-PLACE + MOVED | SKILL.md § Distribution minimums; references/social-idea-build-method.md § Distribution Rules |
| 11 | "## 8 Idea Generation Frameworks" (Frameworks 1–8 incl. Uganda/EA seasonal table) | MOVED; Martyrs Day, variable Eid dates and authenticity note also in Decision Rules | references/social-idea-build-method.md § 8 Idea Generation Frameworks |
| 12 | "## Output: 30 Content Ideas" (matoke example row) | MOVED | references/social-idea-build-method.md § Output: 30 Content Ideas |
| 13 | "## Evergreen Content Series" (fields + 5 example formats) | MOVED; fields in Workflow step 6 and Outputs | references/social-idea-build-method.md § Evergreen Content Series |
| 14 | "## Human Authenticity Gate" | MOVED | references/social-idea-build-method.md § Human Authenticity Gate |
| 15 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT (7 bullets) + full list MOVED | SKILL.md § Quality Standards; references/social-idea-build-method.md § Quality Criteria (full list) |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding (generic input row, capability, degraded, workflow 1 and 4, output row, evidence row, generic anti-pattern), 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: HEAD requires "All 8 frameworks contribute at least 2–3 ideas" (How to Use / frameworks intro) while the Quality Criteria say "at least 2 ideas each"; both kept.

## direct-response-funnel-copy — 216 → 127 lines (gated shared ratio 19.7 % → 1.4 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, generic Workflow 1–6, 2 generic output rows, evidence row, 4 generic quality bullets, 5 generic anti-patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "direct-mail letter, postcard, self-mailer…" (FRAT, $20 Rule) | KEPT verbatim | SKILL.md § Decision Rules |
| 3 | "## Overview" (Brunson, Kennedy; conversion-economics) | CONDENSED-IN-PLACE + MOVED | SKILL.md intro; references/funnel-method-and-toolkit.md § Overview |
| 4 | Body "## Use When" / "## Do Not Use When" (duplicate scope lists) | MOVED (renamed "Scope: use when" / "Scope: do not use when"); hard-sell voice conflict and regulated-claims stop also in Decision Rules | references/funnel-method-and-toolkit.md |
| 5 | Body "## Required Inputs" (6 bullets) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (6 rows); references/funnel-method-and-toolkit.md § Intake answers |
| 6 | Body "## Workflow" (11 steps) | CONDENSED-IN-PLACE (8 steps) + full text MOVED | SKILL.md § Workflow; references/funnel-method-and-toolkit.md § Full eleven-step method |
| 7 | "## Script Toolkit (choose by job)" (8 rows) | MOVED; B2B follow-up and consultative rows also in Decision Rules | references/funnel-method-and-toolkit.md § Script Toolkit |
| 8 | "## Offer and Trust Layer" (5 bullets) | MOVED; honest concession in Anti-Patterns | references/funnel-method-and-toolkit.md § Offer and Trust Layer |
| 9 | "## Honest Urgency" (5 mechanics) | MOVED; rule in Decision Rules and Quality Standards | references/funnel-method-and-toolkit.md § Honest Urgency |
| 10 | "## Integration With Other Skills" (8 rows) | MOVED; consumers named in Outputs | references/funnel-method-and-toolkit.md § Integration With Other Skills |
| 11 | "## Quality Bar" (11 items) | MERGED-INTO-CONTRACT (all 11 folded into 8 bullets) + MOVED | SKILL.md § Quality Standards; references/funnel-method-and-toolkit.md § Quality Bar |
| 12 | "## Common Failures" (8 items) | MERGED-INTO-CONTRACT (all 8 in 7 bullets with Fix) + MOVED | SKILL.md § Anti-Patterns; references/funnel-method-and-toolkit.md § Common Failures |
| 13 | "## Deliverables" (11 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Outputs (5 rows); references/funnel-method-and-toolkit.md § Deliverable list |
| 14 | "## References" (8 entries) | KEPT with "read when" + MOVED copy | SKILL.md § References; references/funnel-method-and-toolkit.md § Reference map (links adjusted one level) |
| 15 | "## Uganda / East Africa Notes" (7 bullets) | MOVED; WhatsApp opt-in in Workflow step 3, test-before-scale in Decision Rules | references/funnel-method-and-toolkit.md § Uganda / East Africa Notes |

Checks: factcheck 0 missing; linecheck 2 flagged → 2 scaffolding (generic workflow steps 1, 4), 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: HEAD East Africa note labels "WhatsApp opt-in lists often outperform email" as "an unverified practitioner heuristic"; kept with its qualification.

## email-copywriter — 266 → 118 lines (gated shared ratio 16.6 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, Workflow 1–6, 2 generic output rows, evidence row, 4 generic quality bullets, 4 generic anti-patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | References (phrase bank, ethics filter, AGENTS) | KEPT with "read when"; launch-and-sequence-copy.md added | SKILL.md § References |
| 3 | "## How to Use This Skill" (core principle) | CONDENSED-IN-PLACE + MOVED | SKILL.md intro; references/email-type-templates.md |
| 4 | "## Required Input" (11 bullets) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; references/email-type-templates.md § Required Input |
| 5 | "## Writing Standards (All Email Types)" (10 bullets) | MOVED; summarised in Workflow step 6, Quality Standards and Anti-Patterns | references/email-type-templates.md § Writing Standards |
| 6 | "## Email Type 1: Newsletter" | MOVED; newsletter CTA rule in Decision Rules | references/email-type-templates.md § Email Type 1 |
| 7 | "## Email Type 2: Promotional Email" | MOVED; urgency and proof rules in Decision Rules | references/email-type-templates.md § Email Type 2 |
| 8 | "## Email Type 3: Welcome Email (Single Email)" | MOVED | references/email-type-templates.md § Email Type 3 |
| 9 | "## Email Type 4: Reactivation Email" (60 or more days) | MOVED; 60-day rule and opt-out in Decision Rules | references/email-type-templates.md § Email Type 4 |
| 10 | "## 12 Subject Line Formulas" (table) | MOVED | references/email-type-templates.md § 12 Subject Line Formulas |
| 11 | "## Human Authenticity Gate" | MOVED | references/email-type-templates.md § Human Authenticity Gate |
| 12 | "## Quality Criteria" (9 items) | MERGED-INTO-CONTRACT (all 9 in 8 bullets) + MOVED | SKILL.md § Quality Standards; references/email-type-templates.md § Quality Criteria (full list) |

Checks: factcheck 0 missing; linecheck 2 flagged → 2 scaffolding (generic workflow steps 1, 4), 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: PS "is consistently the second most-read element of an email" is unsourced; subject-line example "3 ways Kampala retailers are cutting delivery costs in 2025" carries a dated year; "127 Kampala businesses…" is an illustrative figure, not a client fact.

## premium-commercial-writing — 168 → 132 lines (gated shared ratio 24.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, Workflow 1–6, 2 generic output rows, evidence row, 4 generic quality bullets, 5 generic anti-patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows (content writing standards; brochure copy) | KEPT verbatim; 5 domain rows added | SKILL.md § Decision Rules |
| 3 | References (phrase bank, ethics filter, content writing standards, brochure, buyer psychology, AGENTS) | KEPT with "read when"; premium-writing-system, format-specific-gates, search-and-authority-layer, value-proof-and-offer-architecture and the new reference added | SKILL.md § References |
| 4 | Intro "Use this as a cross-cutting writing layer…" | CONDENSED-IN-PLACE + MOVED | SKILL.md intro; references/premium-operating-standard.md |
| 5 | "## Required Input" (8 bullets + gap rule) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; references/premium-operating-standard.md § Required Input |
| 6 | "## Operating Standard" (five jobs) | KEPT (retained domain section) + MOVED copy | SKILL.md § Five jobs of a premium asset; references/premium-operating-standard.md § Operating Standard |
| 7 | Body "## Workflow" (7 steps) | KEPT as SKILL.md workflow + MOVED copy | SKILL.md § Workflow; references/premium-operating-standard.md § Seven-step premium method |
| 8 | "## Premium Writing Tests" (6 tests) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Quality Standards and Decision Rules; references/premium-operating-standard.md § Premium Writing Tests |
| 9 | "## Output Options" (6 options) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Outputs; references/premium-operating-standard.md § Output Options |
| 10 | "## Integration" (10 bullets) | MOVED; key pairings in References and Decision Rules | references/premium-operating-standard.md § Integration |
| 11 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT (all 8) + MOVED | SKILL.md § Quality Standards; references/premium-operating-standard.md § Quality Criteria (full list) |
| 12 | "## English collocation and lexical-precision overlay" | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Workflow step 6 and § References; references/premium-operating-standard.md (link adjusted one level) |

Checks: factcheck 0 missing; linecheck 5 flagged → 5 scaffolding (generic degraded line, workflow 1 and 4, output row, generic anti-pattern), 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: none.

## prompt-engineering-library — 470 → 134 lines (gated shared ratio 21.9 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, Workflow 1–6, 2 generic output rows, evidence row, 4 generic quality bullets, 5 generic anti-patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows (image prompts; voice/avatar/music prompts) | KEPT verbatim; 5 domain rows added | SKILL.md § Decision Rules |
| 3 | References (role packs, image-prompt-patterns, image-audio-video library, AGENTS) | KEPT with "read when"; team-prompt-operating-system and both new references added | SKILL.md § References |
| 4 | "## Evidence-first prompt standard" | CONDENSED-IN-PLACE + MOVED | SKILL.md § Master formula at a glance (last paragraph), Workflow steps 6–7; references/prompt-formula-components-and-techniques.md |
| 5 | "## Required Input" (7 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; references/prompt-formula-components-and-techniques.md § Required Input |
| 6 | "## The Master Prompt Formula" (Upadhyay 2024) | KEPT (formula block) + MOVED (element notes) | SKILL.md § Master formula at a glance; references/prompt-formula-components-and-techniques.md |
| 7 | "## The 10 Prompt Components" | MOVED | references/prompt-formula-components-and-techniques.md |
| 8 | "## Copywriting Style Frameworks" (7 frameworks) | MOVED; names in Workflow step 3 | references/prompt-formula-components-and-techniques.md |
| 9 | "## Prompt Library — Templates by Task" (### 1–7) | MOVED | references/text-prompt-templates-by-task.md |
| 10 | "## PAO Matrix — Pre-Prompt Checklist" | MOVED; step in Workflow 2 and Anti-Patterns | references/prompt-formula-components-and-techniques.md |
| 11 | "## Prompt Anatomy Reference" (GPT Penguin) | MOVED | references/prompt-formula-components-and-techniques.md |
| 12 | "## Copywriting Formula Prompt Activation" (Mizrahi) | MOVED; rule in Anti-Patterns | references/prompt-formula-components-and-techniques.md |
| 13 | "## Emotional Resonance Pattern" | MOVED; in Workflow step 4 and Anti-Patterns | references/prompt-formula-components-and-techniques.md |
| 14 | "## Placeholder Variable Syntax" (Wright 2025) | MOVED; in Workflow step 4 and Anti-Patterns | references/prompt-formula-components-and-techniques.md |
| 15 | "## Hallucination Management Gate" (Evelyn 2025, p.51) | MOVED; in Decision Rules and Anti-Patterns | references/prompt-formula-components-and-techniques.md |
| 16 | "## ### Separator Syntax" | MOVED (heading renamed "Separator Syntax (`###`)"); in Decision Rules | references/prompt-formula-components-and-techniques.md |
| 17 | "## Prompting Techniques" (### Evidence-first qualification + 5 techniques) | MOVED; qualification in Decision Rules | references/prompt-formula-components-and-techniques.md |
| 18 | "## MVOSSTE Prompting Workflow (Randazzo, 2024)" + footnote practice | MOVED; footnote practice in Quality Standards | references/prompt-formula-components-and-techniques.md |
| 19 | "## Sales Funnel Stage-Specific Prompts" | MOVED | references/text-prompt-templates-by-task.md |
| 20 | "## Before/After Prompt Comparison — Social Caption" (Chavaux 2025) | MOVED | references/text-prompt-templates-by-task.md |
| 21 | "## Forward-Reasoning Strategy Prompt" | MOVED | references/prompt-formula-components-and-techniques.md |
| 22 | "## Curiosity Gap Technique" | MOVED | references/prompt-formula-components-and-techniques.md |
| 23 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT (all 8) + MOVED | SKILL.md § Quality Standards; references/prompt-formula-components-and-techniques.md § Quality Criteria (full list) |
| 24 | Body "## References" (12 citations) | MOVED (heading renamed "Sources") | references/prompt-formula-components-and-techniques.md § Sources |

Checks: factcheck 0 missing; linecheck 5 flagged → 5 scaffolding (generic degraded line, workflow 1 and 4, output row, generic anti-pattern), 0 lost; validator clean; routecheck unchanged.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: "Chain-of-thought" technique asks the AI to "walk through its reasoning" while the evidence-first qualification asks for concise assumptions "rather than requiring private chain-of-thought disclosure" (both kept); Erné (2024), Roth and neuroflash (2024) and Bodnar and Cohen (2012) are listed as sources but no body content uses them; Joseph is dated "c.2023–2024"; the Upadhyay entry has a stray full stop after the title.

## Batch-wide checks

- `scripts/validate_skill_engine.py --json`: no findings for any B04 skill.
- `routecheck.py`: the repository-wide script aborts on a SKILL.md outside this batch that has no HEAD version (another worker's new file); run restricted to `skills/content-writing/*/SKILL.md`: 0 routing sections changed.
- `factcheck.py content-writing/`: 0 missing fact tokens.
- `measure_skill_scaffolding.py`: every B04 gated ratio ≤ 1.5 %.
- Line counts 118–134 (all ≤ 220).
- Markdown link test passes; a local link scan of all B04 SKILL.md and reference files finds 0 broken, non-portable or ALIAS links. `git diff --check` clean (only CRLF conversion warnings).

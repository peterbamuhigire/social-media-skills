# S09 preservation log — B00-pilot

Worker: S09 executor (orchestrating agent), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. This skill is the worked example given to the batch workers.

## 11-content-calendar — 278 → 110 lines (gated shared ratio 12.9 % → 0.0 %; raw 31.3 % → 34.1 %, the raw figure rises because structural lines are a larger share of a shorter file)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph (three monthly tables; `east-african-english`; do not generate before inputs are confirmed) | CONDENSED-IN-PLACE | SKILL.md intro; the "confirm inputs first" rule is Workflow step 1 |
| 2 | Generated contract prose: generic input rows, output row, evidence row, capability paragraph, degraded paragraph, 3 generic decision rows, generic workflow steps 1–5 and 7, 5 generic anti-patterns, generic worked example, "Read next", generic References line | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections (canonical capability and degraded sentences; domain inputs, outputs, evidence, decisions, anti-patterns) |
| 3 | "## Required Input" (8 intake items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (six domain rows with fallbacks); full list → references/calendar-build-method.md § Intake questions |
| 4 | "## Calendar Table Format" (columns and definitions) | MOVED | references/calendar-build-method.md § Calendar table format |
| 5 | "## Section 1: Ugandan and East African Observances" (7 fixed dates, 3 variable, tone notes, `[OBSERVANCE]` rule) | MOVED | references/calendar-build-method.md § Ugandan and East African observances; tone rule also SKILL.md § Decision Rules row 3 and Anti-Patterns 1–2 |
| 6 | "## Section 2: International Awareness Days" (20-row table; pick 6–10 with reasons) | MOVED | references/calendar-build-method.md § International awareness days; selection rule also Workflow step 3 and Quality Standards |
| 7 | "## Section 3: Industry Seasonal Hooks" (question; `[HIGH SEASON]`; +20–30 %; two seasonal posts per platform) | MOVED | references/calendar-build-method.md § Industry seasonal hooks; rule also Decision Rules row 2 |
| 8 | "## Section 4: Campaign Windows" (`[CAMPAIGN]`; campaign leads; one supporting organic post) | MOVED | references/calendar-build-method.md § Campaign windows; rule also Decision Rules row 1 |
| 9 | "## Section 5: Cross-Platform Consistency" (format) | MOVED | references/calendar-build-method.md § Cross-platform consistency |
| 10 | "## Section 6: Weekly Rhythm Template" (7-row table) | MOVED | references/calendar-build-method.md § Weekly rhythm template |
| 11 | "## Section 7: Pre-Publish QC — Stratified Sampling" (6-step procedure; santa-method attribution; 15–20 % cost, over 90 % catch) | MOVED | references/calendar-build-method.md § Pre-publish QC; gate kept as Workflow step 6, Decision Rules row 6, Evidence row 2 |
| 12 | "## Three Monthly Tables" (monthly overview paragraph; 10-4-1 rule, Bodnar and Cohen 2012) | MOVED + KEPT | references/calendar-build-method.md § Three monthly tables; 10-4-1 also Decision Rules row 5 |
| 13 | "## Consultant Guidance Note" (Friday review, three questions) | MOVED | references/calendar-build-method.md § Consultant guidance note; also Anti-Patterns 5 |
| 14 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 bullets; the observance and awareness-day bullets combined) |

Checks: factcheck 0 missing; linecheck 20 flagged → 11 generated scaffolding, 9 paraphrased (observance and variable-date headings, the Eid al-Adha line, the campaign-window heading, sampling rubric lines and three quality bullets, all in `references/calendar-build-method.md` or SKILL.md § Quality Standards), 0 lost; validator clean.
Noticed, not changed: none.

## skill-writing — 76 → 77 lines (pointer stub; registered shared-asset variant)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Quality Standards bullet "`SKILL.md` stays within 500 lines…" | CONDENSED-IN-PLACE (rule updated to the 300-line `line_budget`, lean template and "read when" links) | SKILL.md § Quality Standards |
| 2 | Engine-Local Delta | KEPT; one bullet added pointing to the lean template and the scaffolding meter | SKILL.md § Engine-Local Delta |
| 3 | Every other block | KEPT unchanged | SKILL.md |

The body stays a pointer stub to the canonical dev standard, so the canonical sentences were not imposed. Its `sha256` variant was re-registered in `chwezi-engine-agents/catalog/shared-assets.yaml` (S09 reason added).

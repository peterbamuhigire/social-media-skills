# S09 preservation log — B03-bizdev-utility-sectors

Worker: S09 worker agent (Claude), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. Frontmatter, H1, `## Use When` and `## Do Not Use When` copied byte for byte from HEAD in every skill (routecheck: 0 changed). Gated ratios measured with `scripts/measure_skill_scaffolding.py` against a `git archive 0e0af8a` export (before) and the working tree (after).

## biz-dev-credentials — 251 → 114 lines (gated shared ratio 14.5 % → 1.7 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic Required Inputs rows, Capability, Degraded Mode, 3 generic decision rows, generic Workflow, generic Outputs/Evidence rows, generic Quality Standards, 5 generic anti-patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "One client result needs its own standalone case study…" | KEPT | SKILL.md § Decision Rules |
| 3 | Intro "Produce two outputs from a single set of inputs…" | MOVED | references/credentials-build-method.md (opening paragraph); gist in SKILL.md intro |
| 4 | "## Required Input" (7 items) | MOVED + MERGED-INTO-CONTRACT | references/credentials-build-method.md § Required Input; SKILL.md § Required Inputs (6 rows) |
| 5 | "## Output 1: Written Credentials Document" (§§ 1–6, example register) | MOVED | references/credentials-build-method.md § Output 1 |
| 6 | "## Output 2: 8-Slide Deck Outline" + "### Slide Structure" | MOVED | references/credentials-build-method.md § Output 2 |
| 7 | "## Formatting Rules" (5 bullets) | MOVED | references/credentials-build-method.md § Formatting Rules |
| 8 | "## Social Proof Standards" / "### Social Proof Taxonomy (Bly, 2018)" (table + four-of-six rule) | MOVED | references/credentials-build-method.md § Social Proof Standards; four-of-six rule also SKILL.md § Decision Rules and § Evidence Produced |
| 9 | "## Brand Asset Scorecard" (Killian in Hahn 2003, 16 criteria, scoring bands) | MOVED | references/credentials-build-method.md § Brand Asset Scorecard; bands also in SKILL.md § Evidence Produced |
| 10 | "## Persuasion Frameworks" (5 key principles) | MOVED | references/credentials-build-method.md § Persuasion Frameworks (link path fixed to sibling file); principles also as SKILL.md decision rows and anti-patterns |
| 11 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 12 | References: case-study-method, AGENTS.md | KEPT | SKILL.md § References (with `: read when`) |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: "Use the exact slide format from CLAUDE.md" and the Quality criterion "Deck outline follows the exact format specified in CLAUDE.md" point to a runner file that may not carry a slide format; "Killian, B., in Hahn (2003)" has no title or publisher; RACE cited as Chaffey (2024) with no title.

## biz-dev-lawful-prospecting-outreach — 113 → 113 lines (gated shared ratio 3.6 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Outputs header "Observable acceptance condition" | REPLACED-BY-CANONICAL | SKILL.md § Outputs (header `Acceptance condition`) |
| 2 | "## Capability and Permission Boundaries" paragraph | CONDENSED-IN-PLACE | Canonical first sentence + one domain sentence keeping personal-data, calls, account registration, lawful basis, DP registration and "does not give legal advice" |
| 3 | "## Degraded Mode" paragraph | CONDENSED-IN-PLACE | Canonical sentence + business-address, opted-in and referral routes and adviser checks |
| 4 | "## References" (6 links with em-dash descriptions; last without description) | CONDENSED-IN-PLACE | `: read when` added to every link |
| 5 | All other sections (Required Inputs, Workflow, Decision Rules, Quality Standards, Anti-Patterns, acknowledgement) | KEPT | SKILL.md, unchanged |

Checks: factcheck 0 missing; linecheck 0 flagged; validator clean.
Paraphrased lines: none flagged.
Noticed, not changed: none.

## biz-dev-positioning — 202 → 123 lines (gated shared ratio 15.8 % → 1.6 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded Mode, 3 generic decision rows, generic Workflow/Outputs/Evidence/Quality/Anti-Patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "The subject is the consultant's own practice…" | KEPT | SKILL.md § Decision Rules |
| 3 | "## Required Input" (7 items) | MOVED + MERGED-INTO-CONTRACT | references/positioning-method.md § Required Input; SKILL.md § Required Inputs |
| 4 | "## Part 1 — The Differentiating Promise (USP)" | MOVED | references/positioning-method.md § Part 1; formula also SKILL.md § Statement Formulas; competitor test as decision row |
| 5 | "## Part 2 — The Short Spoken Pitch" | MOVED | references/positioning-method.md § Part 2; structure in § Statement Formulas; failure checks as decision row |
| 6 | "## Part 3 — Defining the Niche" (grid, layers) | MOVED | references/positioning-method.md § Part 3; Workflow step 3 |
| 7 | "## Part 4 — Mission and Vision" | MOVED | references/positioning-method.md § Part 4; formulas in § Statement Formulas |
| 8 | "## Part 5 — Strategic Positioning Checks" (5-row table) | MOVED | references/positioning-method.md § Part 5 (playbook-networking link given one more `../`); Pull/Focus/Access rows also SKILL.md § Decision Rules |
| 9 | "## Part 6 — Preeminence Routes" | MOVED | references/positioning-method.md § Part 6 |
| 10 | "## Part 7 — Deliverables This Skill Can Generate" | MOVED + MERGED-INTO-CONTRACT | references/positioning-method.md § Part 7; SKILL.md § Outputs |
| 11 | "## Quality Criteria" (7 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 7 kept) |
| 12 | Lower "## References" (Edwards et al. 1991, Reeves 1961, Pinskey 1997) | MOVED | references/positioning-method.md § Sources |

Checks: factcheck 0 missing; linecheck 11 flagged → 11 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: the example vision "To be the leading social media consultancy…" uses "leading", which `biz-dev-credentials` bans as a superlative; kept as the illustrative example.

## biz-dev-pricing-menu — 290 → 117 lines (gated shared ratio 12.8 % → 1.7 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded Mode, 3 generic decision rows, generic Workflow/Outputs/Evidence/Quality/Anti-Patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "A new prospect will not yet commit to a retainer…" | KEPT | SKILL.md § Decision Rules |
| 3 | Intro "Produce two separate, clearly labelled documents…" | MOVED | references/pricing-menu-build-method.md (opening paragraph); gist in SKILL.md intro |
| 4 | "## Required Input" (5 items) | MOVED + MERGED-INTO-CONTRACT | references/pricing-menu-build-method.md § Required Input; SKILL.md § Required Inputs |
| 5 | "## Document 1" (intro, Starter/Growth/Premium tiers with UGX/USD figures, Add-On Services, Pricing Notes) | MOVED | references/pricing-menu-build-method.md § Document 1 |
| 6 | "### Menu Design Rules" (6 bullets, Nelson 2019, Wiebe 2011) | MOVED | references/pricing-menu-build-method.md § Menu Design Rules (roadmap link given one more `../`); rules also SKILL.md decision rows, anti-patterns and Workflow step 4 |
| 7 | "## Document 2" (rate justification, ROI formula, 5 objections, Starter-to-Growth, walk-away list) | MOVED | references/pricing-menu-build-method.md § Document 2; ROI, walk-away and upgrade rules also SKILL.md § Decision Rules |
| 8 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept; 1 → references/pricing-menu-build-method.md § Additional release check) |
| 9 | References: agency growth roadmap, risk-reversed entry offer, AGENTS.md | KEPT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: UGX→USD equivalents imply a fixed, undated exchange rate (about 3,700); the menu ranges are indicative and undated.

## biz-dev-proposal — 270 → 118 lines (gated shared ratio 14.6 % → 1.6 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded Mode, 3 generic decision rows, generic Workflow/Outputs/Evidence/Quality/Anti-Patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Intro "Produce a complete, professional proposal document…" | MOVED | references/proposal-build-method.md (opening paragraph); gist in SKILL.md intro |
| 3 | "## Required Input" (8 items + pricing/timeline fallbacks) | MOVED + MERGED-INTO-CONTRACT | references/proposal-build-method.md § Required Input; SKILL.md § Required Inputs and decision rows |
| 4 | "## Document Structure" §§ 1–9 (cover letter … next steps, T&C placeholder) | MOVED | references/proposal-build-method.md § Document Structure; Workflow step 4 |
| 5 | "## Formatting Rules" | MOVED | references/proposal-build-method.md § Formatting Rules; key rules in SKILL.md § Outputs |
| 6 | "## Proposal Strengthening Frameworks" (Kahan 2022 scorecard, Bly 2018 social proof, free diagnostic) | MOVED | references/proposal-build-method.md; Kahan and diagnostic also in SKILL.md Workflow, Evidence and decision rows |
| 7 | "## Client Acquisition Frameworks" (Nelson 2019 summary) + "### Hell Yes or Hell No Principle (Wardrope, 2024)" | MOVED | references/proposal-build-method.md (links re-pathed); qualification and price-order rules also SKILL.md § Decision Rules |
| 8 | "## Persuasion Frameworks" (6 principles) | MOVED | references/proposal-build-method.md § Persuasion Frameworks; principles also SKILL.md § Anti-Patterns |
| 9 | "## Quality Criteria" (10 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept; 2 → references/proposal-build-method.md § Additional release checks) |
| 10 | References: acquisition system, lawful prospecting, AGENTS.md | KEPT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: "at least 3 of the 9 Positioning Assets (Nelson, 2019)" — the nine assets are not listed in this skill; the acquisition reference notes older engine citations dated Nelson 2018.

## eac-call-for-applications-campaign — 137 → 113 lines (gated shared ratio 30.7 % → 3.6 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded Mode, 3 generic decision rows, generic Workflow/Outputs/Evidence/Quality/Anti-Patterns, "nearest routing comparison" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections (`biz-dev-positioning` kept as a References entry) |
| 2 | "## Overview" (2 paragraphs, default assumptions) | CONDENSED-IN-PLACE | SKILL.md intro (2 sentences, every item kept) |
| 3 | Body "## Use When" (3 bullets) | DROPPED-DUPLICATE-OF SKILL.md § Use When bullets 1–4 and § Outputs rows 1–5 | — |
| 4 | Body "## Do Not Use When" (3 bullets) | DROPPED-DUPLICATE-OF SKILL.md § Do Not Use When bullets 1 and 4 | — |
| 5 | Body "## Required Inputs" (4 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs (5 rows) |
| 6 | Body "## Workflow" (7 steps) | MERGED-INTO-CONTRACT | SKILL.md § Workflow steps 2–8 |
| 7 | "## Quality Bar" (5 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 5 kept + 1 from fairness checklist) |
| 8 | Body "## Anti-Patterns" (5 bullets, no Fix) | MERGED-INTO-CONTRACT | SKILL.md § Anti-Patterns (Fix added to each) |
| 9 | Body "## Outputs" (5 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Outputs (5 rows) |
| 10 | Body "## References" (2 files) + AGENTS.md | KEPT | SKILL.md § References |
| 11 | Acknowledgement line | KEPT | after the dual-compat end marker |

Checks: factcheck 0 missing; linecheck 9 flagged → 8 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "Creating applicant guidelines, FAQs, channel copy, partner kits, dissemination logs, and query-response protocols" → SKILL.md § Use When and § Outputs.
Noticed, not changed: acknowledgement carries a personal phone number.

## kaizen-improvement-system — 126 → 122 lines (gated shared ratio 1.7 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Required Inputs" (one 5-column row) | CONDENSED-IN-PLACE | SKILL.md § Required Inputs (4 rows, canonical header; "Purpose" folded into the artefact column) |
| 2 | "## Workflow" (7 steps) | KEPT | SKILL.md § Workflow (step 1 now starts with the currentness gate; step 4 links the adapters) |
| 3 | "## Outputs" / "## Evidence Produced" (one row each) | CONDENSED-IN-PLACE | Split into 3 output rows and 2 evidence rows, same items |
| 4 | "## Two-level product contract" | KEPT | SKILL.md § Two-Level Product Contract |
| 5 | "## Capability" | REPLACED-BY-CANONICAL | Canonical sentence + domain sentence (routes to Digital Research and chwezi-design-engine kept) |
| 6 | "## Degraded Mode" | CONDENSED-IN-PLACE | Canonical form, same inputs, release readiness withheld |
| 7 | "## Decision" (3 rows) | KEPT | SKILL.md § Decision Rules (+3 domain rows) |
| 8 | "## Quality Standards" (1 paragraph) | CONDENSED-IN-PLACE | SKILL.md § Quality Standards bullets 1 and 6 |
| 9 | "## Mandatory 65-to-95 gate" | KEPT | SKILL.md § Mandatory 65-to-95 Gate |
| 10 | "## Anti-Patterns" (5) | KEPT | SKILL.md § Anti-Patterns |
| 11 | "## Worked Example" (short-form video) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules row 4 |
| 12 | "## Mandatory Digital Research currentness gate" | KEPT | SKILL.md § Mandatory Digital Research Currentness Gate |
| 13 | "## References" (6 items) | KEPT | SKILL.md § References (`: read when` added; backticked skill paths turned into links) |

Checks: factcheck 0 missing; linecheck 1 flagged → 0 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "Do not invent platform benchmarks… Use British English and East African defaults…" → SKILL.md § Quality Standards bullets 1 and 6.
Noticed, not changed: the skill names the research engine `digital-research-engine`, while other skills link GitHub `digital-research-skills` (the older name).

## skill-safety-audit — 223 → 161 lines (gated shared ratio 17.0 % → 1.4 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (2 generic input rows, generic Outputs/Evidence rows, Capability paragraph, Degraded mode, 3 generic decision rows, generic Workflow, generic Quality paragraph, 5 generic anti-patterns, Worked example, Read next, generic References line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections; capability keeps "read-only" and "never run, install or execute" |
| 2 | "## Required Input" | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs rows 1–2 |
| 3 | "## Overview" | MOVED | references/safe-patterns-and-review-example.md § Overview; gist in SKILL.md intro and § Core Rule |
| 4 | "## When to Use" (3 bullets) | MOVED | references/safe-patterns-and-review-example.md § When to Use |
| 5 | "## Core Rule (Mandatory)" | KEPT | SKILL.md § Core Rule (Mandatory) |
| 6 | "## What to Scan For" (categories 1–5, every item) | KEPT | SKILL.md § What to Scan For (verbatim) |
| 7 | "## Allowed Instructions (Safe Patterns)" | MOVED | references/safe-patterns-and-review-example.md; also SKILL.md decision row 6 |
| 8 | "## Audit Workflow (Required)" (7 steps, 3 outcomes) | MERGED-INTO-CONTRACT | SKILL.md § Workflow steps 1–7 (bold step titles verbatim) |
| 9 | "## Red Flags Checklist" (5) | MOVED | references/safe-patterns-and-review-example.md § Red Flags Checklist |
| 10 | "## Quality Standards" (3 bullets) | KEPT | SKILL.md § Quality Standards bullets 1–3 |
| 11 | "## Required Output" (status, findings, actions) | MERGED-INTO-CONTRACT | SKILL.md § Outputs row 1 |
| 12 | "## Example Review Summary" | MOVED | references/safe-patterns-and-review-example.md |
| 13 | "## Notes" | MOVED | references/safe-patterns-and-review-example.md § Notes; also SKILL.md intro and anti-pattern 5 |
| 14 | Read next: skill-writing, anti-ai-slop, ai-slop-audit | MERGED-INTO-CONTRACT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 11 flagged → 11 scaffolding, 0 paraphrased, 0 lost; validator clean (no `audit_not_read_only`).
Paraphrased lines: none.
Noticed, not changed: heading "Unauthorized Network or System Actions" uses US spelling (kept verbatim to keep the checks intact); safe pattern "Use standard VS Code features" is editor-specific.

## healthcare — 351 → 124 lines (gated shared ratio 13.3 % → 1.6 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, generic Workflow, generic Outputs/Evidence rows, Capability, Degraded Mode, 2 generic decision rows, 3 generic quality bullets, 5 generic anti-patterns) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows "Clinical or reputational risk…" and "Evidence is contradictory…" | KEPT | SKILL.md § Decision Rules |
| 3 | Quality bullets "Keep Uganda/East Africa… explicit" and "Apply `ai-marketing/anti-ai-slop`…" | KEPT | SKILL.md § Quality Standards closing paragraph |
| 4 | Anti-pattern "Copying a global template without adapting…" | KEPT | SKILL.md § Anti-Patterns |
| 5 | "## Book-derived additions" | MERGED-INTO-CONTRACT | SKILL.md § References (infodemic reference) |
| 6 | "## Required Input" (8 questions) | MOVED + MERGED-INTO-CONTRACT | references/health-sector-strategy-method.md § Required Input; SKILL.md § Required Inputs |
| 7 | "## Section 1" – "## Section 5" (complexity model, stakeholder table, TTR, Rogers strategies, platform strategy, Trust Triangle, curation standards, 7 red flags, content calendar) | MOVED | references/health-sector-strategy-method.md §§ 1–5 |
| 8 | "## Section 6" – "## Section 8" (DPPA, de-identification, 4-component policy, boundary rules, complaint protocol, troll table, crisis window, prerequisites, holding statement, what not to do, Virginia Tech Principle) | MOVED | references/health-compliance-complaints-crisis.md §§ 6–8; key rules also SKILL.md decision rows and anti-patterns |
| 9 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 bullets; last two criteria combined into bullet 8) |
| 10 | Lower "## References" (Parsons 2009, Stukus et al. 2019, Rogers 2011, DPPA 2019, three skill pointers) | MOVED | references/health-sector-strategy-method.md § Sources |

Checks: factcheck 0 missing; linecheck 4 flagged → 3 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "Output from this skill meets the standard if it:" → SKILL.md § Quality Standards (lead-in dropped).
Noticed, not changed: "Only 12% of US adults are health-literate" has no citation; "1,200% more shares" for healthcare video, "increases content effectiveness by 60%" and "hashtags double engagement" are attributed to Stukus et al. (2019) and look doubtful; "80% of internet users search online for health information" is a US figure applied to East Africa; the Uganda Medical and Dental Practitioners Act is cited without a year; Parsons (2009) and Stukus et al. (2019) lack publishers.

## hospitality-hotel-restaurant — 170 → 112 lines (gated shared ratio 1.0 % → 1.8 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Required Inputs" (2 rows, "Source" header) | CONDENSED-IN-PLACE | SKILL.md § Required Inputs (6 rows, canonical header, same items) |
| 2 | "## Workflow" (5 steps) | KEPT | SKILL.md § Workflow (6 steps; entity-fact consistency step added) |
| 3 | "## Outputs" / "## Evidence Produced" (1 row each) | CONDENSED-IN-PLACE | 3 output rows and 3 evidence rows, same items |
| 4 | "## Capability and Permission Boundaries" | REPLACED-BY-CANONICAL | Canonical sentence + messaging, guest data/likeness and creator contracting |
| 5 | "## Degraded Mode" | CONDENSED-IN-PLACE | Canonical form, same data list |
| 6 | "## Decision Rules" (3 rows) | KEPT | SKILL.md § Decision Rules (+4 rows from Reputation and safety, Search and AI) |
| 7 | "## Quality Standards" (1 sentence) | CONDENSED-IN-PLACE | SKILL.md § Quality Standards (6 bullets, one per adjective) |
| 8 | Overlay paragraph "Route this overlay through…" | CONDENSED-IN-PLACE | SKILL.md intro |
| 9 | "## Strategy spine", "## Content pillars", "## Search and AI discoverability", "## Reputation and safety", "## Measurement" | MOVED | references/hospitality-social-method.md (same headings) |
| 10 | "## Anti-patterns" (5) | KEPT | SKILL.md § Anti-Patterns (+1 from Reputation and safety) |
| 11 | "## Worked example" (restaurant launch) | MOVED | references/hospitality-social-method.md § Restaurant launch example |
| 12 | "## References" (2 links) | KEPT | SKILL.md § References (+ method, neighbours, anti-slop) |

Checks: factcheck 0 missing; linecheck 1 flagged → 0 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "Planning and drafting are read-only by default. Posting, spending, messaging, guest-data use and creator contracting require explicit approval." → SKILL.md § Capability and Permission Boundaries (canonical + domain sentence).
Noticed, not changed: the Digital Research link uses the GitHub repo name `digital-research-skills`; frontmatter uses the inline `compatible_with: [claude-code, codex]` form (kept byte for byte).

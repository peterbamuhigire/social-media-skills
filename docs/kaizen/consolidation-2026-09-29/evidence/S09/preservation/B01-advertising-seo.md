# S09 preservation log — B01-advertising-seo

Worker: S09 batch worker B01 (Claude agent), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10.

The nine advertising skills already carried domain-specific contract sections at HEAD, so their contract text was kept and only re-shaped: exact `Outputs` header, the canonical Capability first line and Degraded Mode sentence (each followed by the skill's own domain sentence), `: read when` References, and every section moved inside the dual-compat markers. The blocks that sat after `<!-- dual-compat-end -->` moved to a new reference file per skill (relative links given one more `../`). `demand-forecasting` was the only skill with generated contract scaffolding; it was rebuilt from its own domain workflow and join guardrails.

Common rows for all nine advertising skills (numbered A–E and not repeated below):

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| A | "## Required Inputs", "## Workflow", "## Evidence Produced", "## Decision Rules", "## Quality Standards", "## Anti-Patterns" | KEPT | SKILL.md, same sections (only changes noted per skill) |
| B | "## Outputs" (header "Observable acceptance condition") | KEPT | SKILL.md § Outputs; header now `Acceptance condition`, rows unchanged |
| C | "## Capability and Permission Boundaries" (domain paragraph) | CONDENSED-IN-PLACE | SKILL.md § Capability: canonical first line + one sentence keeping every skill-specific action, register ID and consent rule |
| D | "## Degraded Mode" (domain paragraph) | CONDENSED-IN-PLACE | SKILL.md § Degraded Mode: canonical sentence naming the critical input + the domain deliverable and "never" rule |
| E | "## References" (em-dash "read for/before" lines) | KEPT | SKILL.md § References, reworded to `: read when …`; new reference file and gate links added |

## ad-copy-and-hook-lab — 157 → 121 lines (gated shared ratio 1.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph | CONDENSED-IN-PLACE | SKILL.md intro (one sentence, all elements kept) |
| 2 | "## Craft notes" with "### Awareness-matched openings", "### Choosing the first thing the reader meets", "### Reading-path devices…", "### Premium register adjustment", "### East Africa notes" | MOVED | references/craft-notes-and-sources.md (same sub-headings, text unchanged) |
| 3 | "## Sources" (Serling 2002; Wiebe 2011; Stutts 2021) | MOVED | references/craft-notes-and-sources.md § Sources |
| 4 | References: added anti-ai-slop and legal/market release gate links | KEPT + extended | SKILL.md § References |

## ad-testing-and-scaling — 160 → 121 lines (gated shared ratio 1.2 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | "## Method summary" with "### Message-angle matrix (Stutts 2021)", "### Test card (Weinberg & Mares 2014, adapted)", "### 100-visitor funnel check", "### Retest → extend → balance → roll out (Stockwell & Shaw 1994)", "### East Africa notes" (PL-01 14 days, PL-02, checked 2026-09-23) | MOVED | references/method-notes-and-sources.md (text unchanged) |
| 3 | "## Sources" (Stutts; Weinberg and Mares; Croll and Yoskovitz; Stockwell and Shaw) | MOVED | references/method-notes-and-sources.md § Sources |

## ad-to-site-journey-handoff — 143 → 118 lines (gated shared ratio 1.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | "## Handoff package to website-skills" (7-row table + design/code split) | MOVED | references/handoff-package-and-brand-slice.md |
| 3 | "## Brand-slice audit (Stutts 2021)" | MOVED | references/handoff-package-and-brand-slice.md; audit also remains in Workflow step 6 and Anti-Patterns 5 |
| 4 | "## Sources" (Levy 2015; Branson 2020; Deacon 2020; Fekeshazi c. 2017; Synechron 2018; Stutts 2021; Wiebe 2011; register CW-01, CW-04, CW-05, CW-10, MK-04) | MOVED | references/handoff-package-and-brand-slice.md § Sources |

## advertising-attribution-and-measurement — 152 → 127 lines (gated shared ratio 2.5 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | "## Core formulas" (8-row table) | KEPT | SKILL.md § Core formulas (retained decision-time section, after Workflow) |
| 3 | "## Worked example (illustrative figures)" (Nairobi bakery) | MOVED | references/worked-example-and-templates.md |
| 4 | "## Test pre-registration template" | MOVED | references/worked-example-and-templates.md |
| 5 | "## Sentence bank" + acknowledgement line | MOVED | references/worked-example-and-templates.md |

## advertising-strategy-and-budget — 195 → 127 lines (gated shared ratio 2.0 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | "## Core method" with "### 1. The objective hierarchy", "### 2. The four-level measurement architecture" (Kelley and Sheehan), "### 4. Governance in brief" | MOVED | references/core-method-and-handoffs.md |
| 3 | "### 3. Budget in one table" | KEPT + MOVED | SKILL.md § Budget in one table (retained); full copy also in references/core-method-and-handoffs.md |
| 4 | "## Worked example" (Mukono school), "## Handoffs", "## Sentence bank for client documents" | MOVED | references/core-method-and-handoffs.md |
| 5 | "## Readiness checklist before recommending spend" (7 items) | MOVED + MERGED-INTO-CONTRACT | references/core-method-and-handoffs.md; Quality Standards bullet 6 requires it complete |

## creative-brief-and-big-idea — 158 → 126 lines (gated shared ratio 1.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | "## Core method in brief" with "### The brief (Kelley & Sheehan)", "### The idea", "### East Africa adaptation", "### Worked scenario" | MOVED | references/core-method-in-brief.md |
| 3 | "### The screen" (seven-point scale, Landa 2022) | KEPT + MOVED | SKILL.md § Seven-point creative effectiveness scale (retained); full copy in references/core-method-in-brief.md |
| 4 | "## Sources" (Landa 2022; Kelley and Sheehan c. 2021–22; Wallas 1926; Young 1940) | MOVED | references/core-method-in-brief.md § Sources |
| 5 | References: added anti-ai-slop link (Quality Standards already required it) | KEPT + extended | SKILL.md § References |

## direct-response-economics — 157 → 118 lines (gated shared ratio 2.5 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph (Stockwell and Shaw (1994) citation) | CONDENSED-IN-PLACE | SKILL.md intro (citation kept verbatim) |
| 2 | "## Break-even in one line" | KEPT + MOVED | SKILL.md § Break-even in one line (retained); copy in references/worked-example-goals-and-handoffs.md |
| 3 | "## Worked example (illustrative figures, UGX)", "## Goal hierarchy (agree before spend)", "## Handoffs" + acknowledgement | MOVED | references/worked-example-goals-and-handoffs.md |
| 4 | "## Readiness checklist before any send or spend" (8 items) | MOVED + MERGED-INTO-CONTRACT | references/worked-example-goals-and-handoffs.md; Quality Standards bullet 6 requires it complete |

## media-planning — 169 → 129 lines (gated shared ratio 2.2 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | "## Workflow" (10 steps) | CONDENSED-IN-PLACE | SKILL.md § Workflow (9 steps: old steps 8 and 9 merged, wording kept) |
| 3 | "## Core concepts at a glance" (9-row formula table) | KEPT | SKILL.md § Core concepts at a glance (retained, after Workflow) |
| 4 | "## Planning sequence in one page", "## Worked example", "## Handoffs", "## Sentence bank" + acknowledgement | MOVED | references/planning-sequence-and-handoffs.md |
| 5 | "## Plan acceptance checklist" (7 items) | MOVED + MERGED-INTO-CONTRACT | references/planning-sequence-and-handoffs.md; Quality Standards bullet 5 requires it complete |

## paid-search-advertising — 140 → 118 lines (gated shared ratio 1.4 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | "## Campaign-type guide (register AD-05, checked 2026-09-23)" | MOVED | references/campaign-types-and-east-africa.md; campaign-type choice also in Workflow step 3 and Decision Rules rows 3–4 |
| 3 | "## Using search to test before building" (Weinberg & Mares 2014) | MOVED | references/campaign-types-and-east-africa.md |
| 4 | "## East Africa adaptation" (CW-04, MK-04, NET-05, PL-05, 18% VAT) | MOVED | references/campaign-types-and-east-africa.md |
| 5 | "## Sources" | MOVED | references/campaign-types-and-east-africa.md § Sources |

## demand-forecasting — 122 → 125 lines (gated shared ratio 49.1 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose: 3 generic input rows, 6 generic workflow steps, 2 generic output rows, 2 generic evidence rows, capability and degraded paragraphs, 2 generic decision rows ("evidence contradictory", "authority limited"), 6 generic anti-patterns | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections: 6 domain input rows, 4 domain outputs, 3 evidence rows, canonical capability and degraded sentences, 7 decision rows (the two generic rows rewritten for stock data), 6 domain anti-patterns |
| 2 | Decision row "Data has duplicate joins, gaps, or too little history" | KEPT | SKILL.md § Decision Rules row 1 (verbatim) |
| 3 | "## Quality Standards" (4 bullets: Uganda/EAT/UGX assumptions, evidence tie, next-operator detail, anti-slop/ai-slop-audit F block) | KEPT | SKILL.md § Quality Standards bullets 6–8 (the evidence-tie bullet folded into the assumption-register evidence row); 5 domain bullets added |
| 4 | "## Overview" | MERGED-INTO-CONTRACT | SKILL.md intro (two sentences, wording kept) |
| 5 | "## Workflow" (second, domain: 9 steps with formulas and backtest) | MERGED-INTO-CONTRACT | SKILL.md § Workflow steps 1–8 (steps 6–8 merged into step 6; cardinality stop/rerun step 7 added from the reference) |
| 6 | "## Join Guardrails" (5 bullets) | KEPT | SKILL.md § Join Guardrails (retained section) |
| 7 | "## References" (AGENTS.md link; "Load `references/demand_forecasting.md`…") | KEPT | SKILL.md § References (both links, with `: read when`) |

## seo-geo-optimisation — 169 → 117 lines (gated shared ratio 1.8 % → 1.7 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Title, acknowledgement line (phone number) and intro | KEPT | SKILL.md head (intro unwrapped) |
| 2 | "## Required Inputs" (4 rows; `---:` alignment) | KEPT | SKILL.md § Required Inputs (alignment marker normalised) |
| 3 | "## Capability and Permission Boundaries" | CONDENSED-IN-PLACE | canonical first line + maintainer-editing and Search Console sentence |
| 4 | "## Degraded Mode" ("Fallback:" paragraph) | CONDENSED-IN-PLACE | canonical sentence + "do not claim indexing, citation, rich-result eligibility, or performance improvement" |
| 5 | "## Decision Rules" (5 rows) | KEPT | SKILL.md § Decision Rules (moved after Degraded Mode) |
| 6 | "## Workflow" preamble: SaaS handoff paragraph | MERGED-INTO-CONTRACT | SKILL.md § Workflow step 1 |
| 7 | "## Workflow" preamble: mandatory three-wave SERP study paragraph | MOVED | references/serp-study-and-editorial-lens.md § Mandatory three-wave SERP study; pointer in Workflow step 1 |
| 8 | "## Workflow" steps 1–10 | CONDENSED-IN-PLACE | SKILL.md § Workflow steps 1–9 (old 6 and 7 merged; wording kept; step 8 adds "rerun") |
| 9 | Customer-language and voice lens paragraph | MOVED | references/serp-study-and-editorial-lens.md § Customer-language and voice lens; pointer in Workflow step 3 |
| 10 | "## Outputs", "## Evidence Produced", "## Quality Standards", "## Anti-Patterns" | KEPT | SKILL.md, same sections (Outputs header now `Acceptance condition`) |
| 11 | "## References" (8 links, no situations) | KEPT | SKILL.md § References with `: read when`; two new reference links added |

Checks: factcheck 0 missing for all 11 skills; routecheck 0 changed; validator: no findings for any B01 skill; measure_skill_scaffolding gated ratio 0.0 % for ten skills and 1.7 % for seo-geo-optimisation; linecheck (THR 0.6) 3 flagged, all in demand-forecasting → 3 scaffolding, 0 paraphrased, 0 lost; all B01 relative links resolve; `git diff --check` clean. (The repo-wide `markdown_links` pytest fails only on `docs/templates/SKILL.template.md` placeholder `references/<topic>.md`, which is not a B01 file.)
Paraphrased lines: none flagged. Scaffolding lines flagged: demand-forecasting generic input row "Existing channel, content, commercial, or performance evidence…", generic workflow step "Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `meta-budget-planner`" (the neighbour routing survives in Do Not Use When and References), generic output row "Demand forecasts, stockout timing, reorder decisions, and duplicate-safe operational-data analysis deliverable".
Noticed, not changed:
- Stutts (2021) *The Undefeated Marketing System* has three publisher attributions across this batch: "Scribe" (ad-copy-and-hook-lab craft notes), "Lioncrest" (ad-copy headline-and-hook-families reference) and "Scribe/Lioncrest" (ad-testing-and-scaling, ad-to-site-journey-handoff).
- Kelley and Sheehan *Advertising Management in a Digital Environment* is dated "c. 2021–22" (creative-brief, advertising-strategy); Fekeshazi *Product Managers' Guide to UX Design* "c. 2017" (ad-to-site). Undated citations left as found.
- seo-geo-optimisation links to `github.com/peterbamuhigire/digital-research-skills/...`; the engine is now registered as `digital-research-engine`. URLs kept unchanged.
- paid-search-advertising: Uganda 18% VAT on non-resident digital services is marked "PL-05, partial" at HEAD; kept as partial.

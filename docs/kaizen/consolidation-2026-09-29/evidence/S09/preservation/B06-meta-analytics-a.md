# S09 preservation log — B06-meta-analytics-a

Worker: S09 batch worker B06 (Claude agent), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. Gated ratios measured with `scripts/measure_skill_scaffolding.py` on a `git archive 0e0af8a` snapshot (before) and the working tree (after).

## measurement-tracking-plan — 110 → 116 lines (gated shared ratio 0.0 % → 0.0 %)

Already lean (new in S04); only the canonical sentences and exact reference format were applied. No content moved.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Capability and Permission Boundaries" (tag or container publishing, uploading customer data, changing consent settings, personal-data processing need authority; legal conclusions to counsel) | REPLACED-BY-CANONICAL + KEPT | SKILL.md § Capability and Permission Boundaries: canonical first sentence, then one domain sentence carrying tag/container publishing, customer-data upload, consent settings and counsel |
| 2 | "## Degraded Mode" (target-state plan, consent design, data request; never report a tag as firing without a test) | CONDENSED-IN-PLACE | SKILL.md § Degraded Mode: canonical first sentence + the same deliverables and the "never report" rule |
| 3 | "## References" (6 reference bullets with " — read when"; 3 bullets each holding several links) | CONDENSED-IN-PLACE | SKILL.md § References: every link now on its own bullet with ": read when …" |
| 4 | All other sections (intro, Required Inputs, Workflow, Outputs, Evidence, Decision Rules, Quality Standards, Anti-Patterns) | KEPT | SKILL.md unchanged |

Checks: factcheck 0 missing; linecheck 0 flagged; validator clean.
Paraphrased lines: none.
Noticed, not changed: none.

## meta-algorithm-guide — 443 → 115 lines (gated shared ratio 7.0 % → 1.8 %)

New reference: `references/platform-ranking-reference.md` (text unchanged; original section numbers kept so "Section 6.1" and "Section 8" cross-references resolve). Existing `references/posting-time-and-frequency-tests.md`: one sentence re-pointed from "SKILL.md §5 … §6.1" to the new reference (figures untouched).

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro scope blockquote (operational not strategy; six EA platforms; use Section 8 checklist before every post; `platform-*` for strategy) | CONDENSED-IN-PLACE + MOVED | SKILL.md intro (2 sentences); full wording → references/platform-ranking-reference.md scope paragraph |
| 2 | Generated contract prose: generic input rows, output row, evidence row, capability paragraph, degraded paragraph, 2 generic decision rows, generic workflow steps 1–6, 4 generic anti-patterns, worked example, "Read next", generic References lines | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision row "client-specific posting time and frequency schedule" and anti-pattern "Recommending posting times from global benchmark articles" | KEPT | SKILL.md § Decision Rules row 2; § Anti-Patterns 1 |
| 4 | "## Required Input" (8 intake items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (5 domain rows); full list → references/platform-ranking-reference.md § Intake questions (Required Input) |
| 5 | "## 1. How Social Media Algorithms Work" (universal signals table, principle) | MOVED | references/platform-ranking-reference.md § 1 |
| 6 | "## 2. Per-Platform Algorithm Ranking Signals" with "### 2.1 Facebook" … "### 2.6 X / Twitter" | MOVED | references/platform-ranking-reference.md § 2.1–2.6; outbound-link rule also SKILL.md § Decision Rules row 4 |
| 7 | "## 3. Engagement Window Reference" | MOVED | references/platform-ranking-reference.md § 3; respond-early rule also SKILL.md § Anti-Patterns 5 |
| 8 | "## 4. Favoured Content Formats by Platform" (table, native-upload universal rule) | MOVED | references/platform-ranking-reference.md § 4; native rule also Decision Rules row 5 |
| 9 | "## 5. Posting Frequency Benchmarks" (table; consistency beats volume) | MOVED | references/platform-ranking-reference.md § 5; consistency rule also Decision Rules row 8 |
| 10 | "## 6. EA-Specific Considerations" with "### 6.1 Peak Activity Times", "### 6.2 Data Costs and Video Consumption", "### 6.3 WhatsApp as a Near-Zero-Cost Distribution Channel" | MOVED | references/platform-ranking-reference.md § 6.1–6.3; video-length and WhatsApp rules also Decision Rules rows 6–7 |
| 11 | "## 7. Algorithm-Penalised Behaviours" (9-row table) | MOVED | references/platform-ranking-reference.md § 7; engagement bait and hashtag stuffing also SKILL.md § Anti-Patterns 3–4 |
| 12 | "## 8. Pre-Publication Checklist" (5 groups) | MOVED | references/platform-ranking-reference.md § 8; named as an Output and Workflow step 6 |
| 13 | "## Quality Criteria" (8 numbered criteria) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept as bullets) |

Checks: factcheck 0 missing; linecheck 9 flagged → 9 scaffolding (generic input/output/decision rows, degraded paragraph, generic workflow steps 1 and 5, generic anti-pattern, worked example, "Output produced by this skill meets the standard when:" lead-in), 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none flagged (quality criteria 3, 4 and 7 reworded in SKILL.md § Quality Standards and now pass the threshold).
Noticed, not changed:
- Competing posting-frequency figures: references/platform-ranking-reference.md § 5 (for example Facebook maximum "1–2× per day", TikTok recommended "5–7× per week", YouTube recommended "2× per week") vs references/posting-time-and-frequency-tests.md Step 3 (Facebook maximum 7/week, TikTok optimal 5/week, YouTube optimal 1–2/week, maximum 3/week).
- Competing EAT windows: references/platform-ranking-reference.md § 6.1 (for example Instagram 07:00–08:30, 12:00–13:30, 20:00–22:00; X 07:00–09:00, 12:00–14:00, 20:00–22:00) vs posting-time-and-frequency-tests.md Step 2 EA baseline windows (Instagram 12:00–14:00, 19:00–21:00; X 07:00–10:00, 17:00–19:00). The existing reference already says the client's own test decides where they differ.
- Doubtful or unregistered platform claims left as written: LinkedIn "Creator Mode" as a ranking signal; Instagram "3 Rs" as published Feed criteria; "Instagram reduced hashtag weight significantly in 2024"; "1 GB … UGX 3,000–5,000 … (2026 rates)"; TikTok test cohort "300–500 users".

## meta-budget-planner — 337 → 119 lines (gated shared ratio 10.1 % → 1.6 %)

New reference: `references/budget-tiers-and-allocation.md` (text unchanged).

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose: generic input rows, output row, evidence row, capability, degraded, 3 generic decision rows, generic workflow, 4 generic anti-patterns, worked example, "Read next", generic References lines | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "budget derived from a revenue target … CAC ≤ CLV × 0.25" and route row to `meta-roi-framework` | KEPT | SKILL.md § Decision Rules rows 1–2 |
| 3 | "## Required Input" (7 intake items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (6 rows); full list → references/budget-tiers-and-allocation.md § Intake questions (Required Input) |
| 4 | "## Section 1 — Budget Planning Principles" with "### Principle 1" … "### Principle 5" | MOVED | references/budget-tiers-and-allocation.md § Section 1; test-before-scaling figures also Decision Rules row 3; owned-before-paid and content-first also Anti-Patterns 2–3 and Quality Standards |
| 5 | "## Section 2 — Budget Tier Templates" with "### Tier 1 — Starter", "### Tier 2 — Growth", "### Tier 3 — Scale" (tables, notes, UGX 3,700 = USD 1) | MOVED | references/budget-tiers-and-allocation.md § Section 2; Starter one-platform rule also Decision Rules row 5; Google Ads and influencer notes also Anti-Patterns 5–6; exchange rate also Evidence row 2 |
| 6 | "## Section 3 — Channel Allocation Decision Framework" (4 steps; 70 %; no more than three channels) | MOVED | references/budget-tiers-and-allocation.md § Section 3; rule also Decision Rules row 4 |
| 7 | "## Section 4 — Content Production Budget Guide" (rate table, guidance) | MOVED | references/budget-tiers-and-allocation.md § Section 4 |
| 8 | "## Section 5 — Budget Review Cadence" (monthly 15 % overspend trigger; quarterly; annual; 90 days) | MOVED | references/budget-tiers-and-allocation.md § Section 5; triggers also Decision Rules rows 6 and 8; annual reset also Anti-Patterns 4 |
| 9 | "## Section 6 — ROI Tracking" (ROI = (TLV − COCA) ÷ COCA; TLV and COCA definitions; worked figures; interpretation bands) | MOVED | references/budget-tiers-and-allocation.md § Section 6; bands also Decision Rules row 7 |
| 10 | "## Quality Criteria" (7 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (7 kept + CAC-ceiling check from the revenue-plan reference) |
| 11 | "## References" (5 linked skills) and closing italic calibration note | MERGED-INTO-CONTRACT + MOVED | SKILL.md § References (all 5 kept with ": read when"); calibration note → SKILL.md intro and references/budget-tiers-and-allocation.md (verbatim, last line) |

Checks: factcheck 0 missing; linecheck 11 flagged → 11 scaffolding (generic rows and paragraphs, generic workflow steps 1 and 5, 2 generic anti-patterns including "Absorbing `meta-roi-framework`…", which is now Decision Rules row 2, worked example, "Good output from this skill…" and "Consult these linked skills…" lead-ins), 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none beyond the scaffolding noted.
Noticed, not changed:
- Two lifetime-value formulas: TLV = "average revenue per customer × average customer lifespan in months/years" (references/budget-tiers-and-allocation.md § Section 6, Bodnar and Cohen 2012) vs CLV = "average revenue per client × average number of transactions × average client lifespan in years" (references/bottom-up-revenue-plan.md, CAC cap section, Kahan 2022). SKILL.md § References names both locations without reconciling them.
- Tier 1 table totals UGX 1,200,000 although the tier range is UGX 500,000–1,500,000; Tier 2 totals 3,470,000; Tier 3 totals 11,000,000 (arithmetic and percentages checked and consistent).

## meta-competitor-analysis — 242 → 113 lines (gated shared ratio 17.7 % → 1.8 %)

New reference: `references/five-section-analysis-template.md` (text unchanged).

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose: generic input rows, output row, evidence row, capability, degraded, 2 generic decision rows, generic workflow, 4 generic anti-patterns, worked example, "Read next", generic References line | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Route row to `02-platform-audit`; reference link to the competitive matrix | KEPT | SKILL.md § Decision Rules row 1; § References |
| 3 | "## Required Input" (client details, client stats, 3–5 competitors with handles and type) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (5 rows); full list → references/five-section-analysis-template.md § Intake questions (Required Input) |
| 4 | "## Output Structure" and "### 1. Competitor Comparison Table" (client row, 10 columns, column guidance, engagement estimate formula) | MOVED | references/five-section-analysis-template.md § 1; client row also Workflow step 2; estimate formula also Decision Rules row 2 |
| 5 | "### 2. Content Style Analysis Per Competitor" | MOVED | references/five-section-analysis-template.md § 2; absences also Workflow step 3 and Anti-Patterns 3 |
| 6 | "### 3. Paid Ad Activity Note" (4 free tools with URLs; caveat) | MOVED | references/five-section-analysis-template.md § 3; caveat also Decision Rules row 3 and Anti-Patterns 2 |
| 7 | "### 4. Gap Analysis" (5 gap categories incl. Luganda/Swahili content) | MOVED | references/five-section-analysis-template.md § 4; platform gap also Decision Rules row 4 |
| 8 | "### 5. Strategic Recommendations" (exactly 5; format; 3+ platforms) | MOVED | references/five-section-analysis-template.md § 5; also Workflow step 6 and Outputs row 3 |
| 9 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept; the two recommendation bullets combined, POEM earned-media check added from the Framework Reference) |
| 10 | "## Framework Reference" (POEM; Bodnar and Cohen 2012; Chaffey 2024) | MOVED | references/five-section-analysis-template.md § Framework Reference; POEM also Workflow step 5 |

Checks: factcheck 0 missing; linecheck 9 flagged → 9 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: "LinkedIn Ad Library: Available via any LinkedIn company page under 'Posts > Ads'" may be out of date (doubtful interface claim).

## meta-content-audit — 299 → 116 lines (gated shared ratio 13.1 % → 1.7 %)

New reference: `references/audit-data-and-output-template.md` (text unchanged). Audit skill: SKILL.md § Capability and Permission Boundaries keeps "read-only".

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose: generic input rows, output row, evidence row, capability, degraded, 2 generic decision rows, generic workflow steps 1–6, generic Quality Standards sentence, 4 generic anti-patterns, worked example, "Read next", generic References line | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Workflow step 7 (narrative reference; capped audit; 95/100 plan); Quality Standards domain sentence (empathy, narrative, hierarchy, readability, evidence, permissions, AI transparency, learning value); 2 domain anti-patterns (high engagement but unclear offer; missing render treated as pass); route row to `meta-competitor-analysis` | KEPT | SKILL.md § Workflow step 6; § Quality Standards bullet 8; § Anti-Patterns 4–5; § Decision Rules rows 1 and 6 |
| 3 | "## Required Input" (9 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (6 rows); full list → references/audit-data-and-output-template.md § Intake questions (Required Input) |
| 4 | "## Step 1: Data Collection Template" (30 posts, 3→6 months, 11 fields, data locations per platform) | MOVED | references/audit-data-and-output-template.md § Step 1; sample rules also Required Inputs row 1 and Decision Rules row 2 |
| 5 | "## Output Structure" and "### 2. Content Performance Summary by Platform" (table; Uganda / EA benchmarks) | MOVED | references/audit-data-and-output-template.md § 2; YouTube rule also Anti-Patterns 6 |
| 6 | "### 3. Top-Performing Content Analysis" | MOVED | references/audit-data-and-output-template.md § 3; also Workflow step 3 |
| 7 | "### 4. Worst-Performing Content Analysis" (exclude zero reach; do not soften) | MOVED | references/audit-data-and-output-template.md § 4; also Decision Rules row 3 and Anti-Patterns 3 |
| 8 | "### 5. Content Pillar Coverage Analysis" (10-4-1; 40 % / 10 %; draft pillars) | MOVED | references/audit-data-and-output-template.md § 5; also Decision Rules row 4 and Required Inputs row 4 |
| 9 | "### 6. Tone and Consistency Rating" (3 dimensions; scoring guide) | MOVED | references/audit-data-and-output-template.md § 6; 1–4 band also Decision Rules row 5 |
| 10 | "### 7. Priority Improvements — First 30 Days" | MOVED | references/audit-data-and-output-template.md § 7; also Workflow step 7 |
| 11 | "## Quality Criteria" (7 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards bullets 1–7 |
| 12 | "## Framework Reference" (10-4-1; RACE; citations) | MOVED | references/audit-data-and-output-template.md § Framework Reference |

Checks: factcheck 0 missing; linecheck 11 flagged → 10 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "30-day improvements are genuinely prioritised (most impactful first) and each is traceable to a specific audit finding" → SKILL.md § Quality Standards bullet 6.
Noticed, not changed: the Uganda / EA engagement-rate benchmarks (Facebook 1–3 %, Instagram 2–4 %, LinkedIn 0.5–2 %, TikTok 4–8 %) carry no source or date; "Generate all seven sections" counts Step 1 plus sections 2–7.

## meta-content-repurposing — 360 → 116 lines (gated shared ratio 11.0 % → 1.7 %)

New reference: `references/content-factory-and-repurposing-chains.md` (text unchanged; one relative link to the evergreen reference adjusted to resolve from `references/`).

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose: generic input rows, output row, evidence row, capability, degraded, 2 generic decision rows, generic workflow, 3 generic anti-patterns, worked example, "Read next", generic References line | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows (evergreen register; AI-assisted ten-asset pipeline); anti-pattern "Recycling an evergreen post without the refresh protocol"; References to capture, pipeline and evergreen references | KEPT | SKILL.md § Decision Rules rows 1–2; § Anti-Patterns 2; § References |
| 3 | "## Required Input" (7 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (6 rows); full list → references/content-factory-and-repurposing-chains.md § Intake questions (Required Input) |
| 4 | "## Key Principle" (60–70 %; 7–10 slots; Repurposing Chain, Nemo 2017; never post identical content cross-platform; 1-7-30-4-2-1, Handley 2012) | MOVED + KEPT | references/content-factory-and-repurposing-chains.md § Key Principle; 60–70 % and 7–10 slots in SKILL.md intro; identical-content rule in Decision Rules row 3, Quality Standards and Anti-Patterns 1; video-first rule in Decision Rules row 6 |
| 5 | "## 1. The Content Factory Model" (three tiers, diagram, 10 slots) | MOVED | references/content-factory-and-repurposing-chains.md § 1 |
| 6 | "## 2. Platform Repurposing Matrix" (table; audiogram) | MOVED | references/content-factory-and-repurposing-chains.md § 2 |
| 7 | "## 3. Ten Worked Repurposing Examples" (examples 1–5; 6–10 instruction) | MOVED | references/content-factory-and-repurposing-chains.md § 3 |
| 8 | "## 4. Weekly Content Repurposing Workflow" (Monday–Friday steps) | MOVED | references/content-factory-and-repurposing-chains.md § 4; highest-performer fallback also Decision Rules row 5 |
| 9 | "## 5. What Not to Repurpose" (5 criteria) | MOVED | references/content-factory-and-repurposing-chains.md § 5; also Workflow step 5, Decision Rules rows 4 and 7, Anti-Patterns 3 |
| 10 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 bullets; "what not to repurpose" and the 60–70 % bullet combined) |
| 11 | "## Framework Reference" (Hero/Hub/Hygiene; Meerman Scott 2022; 5 citations) | MOVED | references/content-factory-and-repurposing-chains.md § Framework Reference |
| 12 | Unlinked existing reference `references/repurposing-for-launch-and-clusters.md` | KEPT | now linked from SKILL.md Workflow step 2 and § References |

Checks: factcheck 0 missing; linecheck 6 flagged → 5 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: HEAD Workflow step 1 (branch to evergreen or AI pipeline reference) → SKILL.md § Workflow step 2.
Noticed, not changed:
- Example 4, Output 3 (Facebook post) contains the skill's old description text ("Generates a content repurposing plan … Invoke this skill when …") in place of post copy; left verbatim in references/content-factory-and-repurposing-chains.md § 3.
- HEAD quality criterion says non-viable combinations are marked "❌" but the matrix uses "No"; SKILL.md now says "marked honestly".
- Handley (2012) is cited in text for the 1-7-30-4-2-1 cadence while the bibliography lists Handley and Chapman (2012) *Content Rules*; the cadence attribution was not checked.

## meta-reporting — 380 → 118 lines (gated shared ratio 11.3 % → 1.7 %)

New reference: `references/monthly-report-template.md` (text unchanged). Existing `references/dashboard-specification.md`: one note re-pointed from "the written monthly report in the SKILL.md" to the new template (15 % figure untouched).

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro note (written report; no deck skill; hand proof pack to `chwezi-design-engine`) | CONDENSED-IN-PLACE | SKILL.md intro; also Anti-Patterns 7 |
| 2 | Generated contract prose: generic input rows, output row, evidence row, capability, degraded, 2 generic decision rows, generic workflow, 4 generic anti-patterns, worked example, "Read next", generic References line | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows (dashboard spec; quarterly 7 Ps; route to `05-social-media-strategy`); References to proof pack, dashboard and quarterly references | KEPT | SKILL.md § Decision Rules rows 1–3; § References |
| 4 | "## Required Input" (intake list) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs (6 rows); full list → references/monthly-report-template.md § Intake questions (Required Input) |
| 5 | "## Reporting Principles" (storytelling; chart choice, Raaz c.2023; real-time tier; mobile standard; Kahan 2022 CVR benchmarks; first-touch revenue; data quality audit; lead score chart) | MOVED | references/monthly-report-template.md § Reporting Principles; storytelling, audit, chart, real-time rules also SKILL.md Workflow steps 2 and 4, Decision Rules rows 5–7, Anti-Patterns 1, 5, 6 |
| 6 | "## Output: Complete Monthly Report" with "### Report Header" and "### 1. Period Summary" | MOVED | references/monthly-report-template.md; also Workflow step 4 |
| 7 | "### 2. Platform-by-Platform KPI Table" (RAG 15 % band; 7 platform tables; WhatsApp note) | MOVED | references/monthly-report-template.md § 2; RAG band also SKILL.md § Decision Rules row 4; WhatsApp estimate also Anti-Patterns 4 |
| 8 | "### 3. Top 3 Posts", "### 4. What Worked", "### 5. What Did Not Work", "### 6. What We Are Testing", "### 7. Paid Social Performance", "### 8. Recommendations", "### Report Footer" | MOVED | references/monthly-report-template.md §§ 3–8 and footer; counts also Workflow step 5; no-paid sentence also Decision Rules row 8 |
| 9 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 10 | "## Framework Reference" (RACE; Chaffey 2024; Bodnar and Cohen 2012) | MOVED | references/monthly-report-template.md § Framework Reference |

Checks: factcheck 0 missing; linecheck 8 flagged → 7 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: HEAD Workflow step 1 (route to `05-social-media-strategy`) → SKILL.md § Workflow step 1 and Decision Rules row 3.
Noticed, not changed:
- RAG amber threshold: 15 % in the written monthly report (references/monthly-report-template.md § 2 and SKILL.md § Decision Rules row 4) vs 10 % in references/dashboard-specification.md (§ scorecard and wireframe row). The dashboard reference already asks each deliverable to state its threshold; not reconciled.
- "Raaz, c.2023" is cited without title or publisher (incomplete citation).

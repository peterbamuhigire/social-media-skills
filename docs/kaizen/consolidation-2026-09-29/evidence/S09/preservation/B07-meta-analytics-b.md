# S09 preservation log — B07-meta-analytics-b

Worker: S09 worker agent (Claude), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10.

Common to all six skills: the generated contract prose (generic Required Inputs rows, generic Outputs and Evidence rows, "Capability and permission boundary" paragraph, "Degraded mode" paragraph, generic decision rows for "input is current and attributable" and "material input missing", generic Workflow steps 1–6, generic Quality Standards paragraph, the three generic anti-patterns, "Worked example" paragraph, "Read next" and "Follow the directly linked…" lines) is REPLACED-BY-CANONICAL / domain rows. Domain decision rows, anti-patterns and links that sat in those sections were kept.

## meta-roi-framework — 394 → 139 lines (gated shared ratio 9.3 % → 1.4 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see common note) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows: cohort LTV → retention reference; business case → investment reference; route to budget planner or reporting | KEPT | SKILL.md § Decision Rules |
| 3 | Anti-pattern "Absorbing budget allocation … or periodic reporting" | KEPT | SKILL.md § Anti-Patterns |
| 4 | "## Read next" / "## References" links (budget planner, reporting, anti-ai-slop, ai-slop-audit, measurement proof pack, two references) | MERGED-INTO-CONTRACT | SKILL.md § References |
| 5 | "## Required Input" (intake list, 12 items) | MOVED | references/roi-model-method.md § Required Input; summarised in SKILL.md § Required Inputs |
| 6 | "## Output Structure" and "### 1. TLV", "### 2. COCA by Channel", CAC Cap Rule, "### 3. COCA:TLV Ratio Interpretation" | MOVED | references/roi-model-method.md (same headings); formulas, CAC cap and ratio bands also in SKILL.md § Formulas and ratio bands and § Decision Rules |
| 7 | "## Bottom-Up Revenue Modelling" (steps, stage weighting, deal velocity, cohort CLV, attribution model note) | MOVED | references/roi-model-method.md § Bottom-Up Revenue Modelling; stage weighting and attribution timing in SKILL.md § Anti-Patterns |
| 8 | "### 4. Attribution Methodology" | MOVED | references/roi-model-method.md § 4; summarised in SKILL.md § Workflow step 4 and § Evidence Produced |
| 9 | "### 5. Break-Even Analysis", "### 6. 12-Month ROI Projection Table", "### 7. Talking Points" | MOVED | references/roi-model-method.md (same headings); formulas in SKILL.md § Formulas and ratio bands |
| 10 | "## FRAT — Customer List Prioritisation Formula", "## The $20 Rule" (Hahn, 2003) | MOVED | references/roi-model-method.md (same headings) |
| 11 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept); currency bullet → references/roi-model-method.md § Quality criterion kept from the HEAD checklist |
| 12 | "## Framework Reference" (ROI formula, POEM model, Bodnar and Cohen 2012, Chaffey 2024 citations) | MOVED | references/roi-model-method.md § Framework Reference |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: HEAD "When COCA is above the benchmark" talking point refers to "the 5:1 benchmark" while the ratio table calls 3:1 to 4:1 "borderline viable" (kept as written). The $20 Rule equates UGX 20,000 with USD $20 (kept as written).

## meta-sales-marketing-alignment — 250 → 133 lines (gated shared ratio 20.7 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro "**Source:** Kahan (2022) *High-Velocity Digital Marketing*" | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | Generated contract prose (see common note) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows: full lead-scoring design → lead-scoring-model; route to `meta-roi-framework` | KEPT | SKILL.md § Decision Rules |
| 4 | "## Read next" / "## References" links | MERGED-INTO-CONTRACT | SKILL.md § References |
| 5 | "## Required Inputs" (8 intake items, second section of that name) | MOVED | references/alignment-method.md § Required Inputs; summarised in SKILL.md § Required Inputs |
| 6 | "## The Core Problem" | MOVED | references/alignment-method.md § The Core Problem; SKILL.md § Workflow step 1 |
| 7 | "## KPI Ownership Map" (marketing, sales, joint KPIs; 3–4× pipeline coverage; ROI formula) | MOVED | references/alignment-method.md § KPI Ownership Map; SKILL.md § Workflow step 2 and § Decision Rules |
| 8 | "## CRM as Single Source of Truth" (three conditions; Zoho 3 users, HubSpot free; 30-day spreadsheet rule) | MOVED | references/alignment-method.md (same heading); SKILL.md § Required Inputs row 1 and § Decision Rules row 1 |
| 9 | "## Lead Handover SLA" (table, 4-hour rule, escalation protocol) | MOVED | references/alignment-method.md (same heading); table and escalation also in SKILL.md § Handover SLA and starter score and § Decision Rules |
| 10 | "## Lead Scoring Foundation" (fit and intent points, 50-point MQL threshold, 20% rule, WhatsApp +15/+20) | MOVED | references/alignment-method.md (same heading); threshold, 20% rule and WhatsApp points also in SKILL.md |
| 11 | "## Monthly Joint Review Meeting" (60 minutes, six items, 24-hour write-up) | MOVED | references/alignment-method.md (same heading); SKILL.md § Workflow step 6 and § Outputs |
| 12 | "## EA-Specific Context: Owner-Managed Businesses" | MOVED | references/alignment-method.md (same heading); SKILL.md § Decision Rules |
| 13 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 14 | lead-scoring-model.md pointers to SKILL.md sections | Appended § Section locations after S09 | references/lead-scoring-model.md |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: competing MQL thresholds, kept both sides exactly: the existing 50-point starter threshold (references/alignment-method.md § Lead Scoring Foundation, summarised in SKILL.md § Handover SLA and starter score) versus the merged 60-point B2B and 40-point EA starter thresholds (references/lead-scoring-model.md § Threshold calibration with sales and § East Africa starter model). The two point tables also differ (for example pricing page +20 here, +25 there; demo or quote +25 here, +40 there). SKILL.md names both sets without reconciling them.

## meta-social-listening — 424 → 125 lines (gated shared ratio 8.3 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see common note) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows: scoring → sentiment method; weekly operation → operations playbook | KEPT | SKILL.md § Decision Rules |
| 3 | Anti-pattern "Reporting sentiment as a word or without volume and driving theme" | KEPT | SKILL.md § Anti-Patterns |
| 4 | "## Read next" / "## References" links | MERGED-INTO-CONTRACT | SKILL.md § References |
| 5 | "## Required Input" (11 items) | MOVED | references/listening-programme-method.md § Required Input; summarised in SKILL.md § Required Inputs |
| 6 | "## What Social Listening Is (and Is Not)" | MOVED | references/listening-programme-method.md (same heading); SKILL.md § Anti-Patterns 1–2 |
| 7 | "## 1. Keyword Taxonomy" (Categories 1–5 tables) | MOVED | references/listening-programme-method.md § 1 |
| 8 | "## 2. Tool Setup" (Google Alerts, native search, Brand24/Mention, GBP reviews) | MOVED | references/listening-programme-method.md § 2 |
| 9 | "## 3. Listening Cadence" (daily, weekly, monthly) | MOVED | references/listening-programme-method.md § 3; SKILL.md § Workflow step 4 |
| 10 | "## 4. Intelligence Extraction Protocol" (5 weekly questions) and listening entry fields paragraph | MOVED | references/listening-programme-method.md § 4; fields also in SKILL.md § Evidence Produced |
| 11 | "## 5. Listening Log Template" | MOVED | references/listening-programme-method.md § 5 |
| 12 | "## 6. Converting Listening Into Strategy" (Level 1 crisis trigger, 48-hour window) | MOVED | references/listening-programme-method.md § 6; SKILL.md § Decision Rules |
| 13 | "## 7. EA-Specific Considerations" | MOVED | references/listening-programme-method.md § 7; SKILL.md § Decision Rules and § Anti-Patterns |
| 14 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 15 | Customer-voice experiment card paragraph | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules, § Evidence Produced, § References |
| 16 | Parent-SKILL pointers in two existing references | Appended § Section locations after S09 | references/listening-operations-playbook.md; references/sentiment-and-share-of-voice-method.md |

Checks: factcheck 0 missing; linecheck 9 flagged → 8 scaffolding, 1 paraphrased (listed below), 0 lost; validator clean.
Paraphrased lines: "decision rule, owner and knowledge link explicit; sentiment or activity alone" → SKILL.md § Evidence Produced (experiment card row) and § Decision Rules (last row).
Noticed, not changed: two net-sentiment-score band sets, kept both exactly: the EA service-business bands (+60 strong, +40 to +59 healthy, +20 to +39 developing, 0 to +19 concerning, below 0 crisis) in references/sentiment-and-share-of-voice-method.md § Step 2, and the Johnsen (2024) weekly operating bands (above +40 healthy, +20 to +40 attention, below +20 crisis territory, below 0 active threat) in references/listening-operations-playbook.md § 3. SKILL.md § Decision Rules only requires each report to name the set used. HEAD Brand24 price "$49 per month (approximately UGX 180,000)" is undated (kept).

## meta-social-metrics-framework — 372 → 132 lines (gated shared ratio 13.6 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see common note) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row: route to `meta-reporting` | KEPT | SKILL.md § Decision Rules |
| 3 | "## Read next" / "## References" links | MERGED-INTO-CONTRACT | SKILL.md § References (brand-metrics reference now linked too) |
| 4 | "## Required Input" (8 items) | MOVED | references/metrics-framework-method.md § Required Input; summarised in SKILL.md § Required Inputs |
| 5 | "## The Core Problem (Schaffer, 2013)" and guardrail paragraph | MOVED | references/metrics-framework-method.md (same heading); guardrail also in SKILL.md § Workflow step 3, § Evidence Produced, § Decision Rules |
| 6 | "## Section 1 — The Three-Tier Framework" (Tier 1–3 tables, ER formula, EA ER benchmarks, SOV and NSS formulas) | MOVED | references/metrics-framework-method.md § Section 1; formulas and benchmarks also in SKILL.md § Formulas and benchmarks |
| 7 | "## Section 2 — Vanity vs Business Metrics" | MOVED | references/metrics-framework-method.md § Section 2 |
| 8 | "## Section 3 — What to Report to Whom" (owner, team, board; design-engine hand-off) | MOVED | references/metrics-framework-method.md § Section 3; hand-off also in SKILL.md § Capability and Permission Boundaries |
| 9 | "## Section 4 — Setting SMART Targets" (3-month baseline rule, sample target) | MOVED | references/metrics-framework-method.md § Section 4; rule in SKILL.md § Decision Rules |
| 10 | "## Output Structure" (7 sections) | MOVED | references/metrics-framework-method.md § Output Structure; SKILL.md § Outputs |
| 11 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept); NSS/SOV formula bullet → references/metrics-framework-method.md § Quality criterion kept from the HEAD checklist |
| 12 | "## Section 5 — Velocity and Funnel Diagnostics" (velocity table, CVR benchmarks, decision tree, 20% flag) | MOVED | references/metrics-framework-method.md § Section 5; benchmarks and tree also in SKILL.md |
| 13 | "## Cross-References" (5 items) | MERGED-INTO-CONTRACT | SKILL.md § References and § Capability and Permission Boundaries |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: the EA ER benchmarks and funnel CVR benchmarks are undated with no register record (kept as written).

## meta-testing-framework — 464 → 141 lines (gated shared ratio 8.8 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | H1 intro (two lines) | CONDENSED-IN-PLACE | SKILL.md intro (one line, same words) |
| 2 | Generated contract prose (see common note) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision row: route to `meta-algorithm-guide` | KEPT | SKILL.md § Decision Rules |
| 4 | Workflow step 7 (Kaizen campaign learning loop) | KEPT | SKILL.md § Workflow step 8 |
| 5 | Quality Standards domain sentence (audience empathy … one clear action) | KEPT | SKILL.md § Quality Standards bullet 8 |
| 6 | Anti-patterns: metric lift with worse guardrails; clever hook without audience problem | KEPT | SKILL.md § Anti-Patterns |
| 7 | "## Read next" / "## References" links (algorithm guide, Kaizen loop, narrative audit, anti-slop) | MERGED-INTO-CONTRACT | SKILL.md § References |
| 8 | "## Required Inputs" (8 intake items) | MOVED | references/testing-method.md § Required Inputs; summarised in SKILL.md § Required Inputs |
| 9 | "## Section 1 — Testing Principles" (one variable, statistical and practical significance, duration) | MOVED | references/testing-method.md § Section 1; thresholds in SKILL.md § Thresholds and blackout periods and § Decision Rules |
| 10 | "## Section 2 — What to Test (Priority Order)" | MOVED | references/testing-method.md § Section 2; SKILL.md § Workflow step 3 |
| 11 | "## Section 3 — Test Design Templates" (A, B, C) | MOVED | references/testing-method.md § Section 3 |
| 12 | "## Section 4 — Tracking Sheet" | MOVED | references/testing-method.md § Section 4; SKILL.md § Evidence Produced |
| 13 | "## Section 5 — Reading Results" (Ads Manager, organic, common mistakes) | MOVED | references/testing-method.md § Section 5; mistakes also in SKILL.md § Anti-Patterns |
| 14 | "## Section 6 — Building a Testing Calendar" (cadence, periods to avoid, negative results) | MOVED | references/testing-method.md § Section 6; blackout table also in SKILL.md |
| 15 | "## EA-Specific Considerations" (budget, platform priority, small accounts, mobile-first) | MOVED | references/testing-method.md (same heading); SKILL.md § Decision Rules and § Workflow step 5 |
| 16 | "## Quality Criteria" (7 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 7 kept) |
| 17 | "## References" (meta-reporting, meta-roi-framework, 09-campaign-strategy; Bodnar and Cohen 2012, Chaffey 2024, Kotler et al. 2023) | MERGED-INTO-CONTRACT / MOVED | SKILL.md § References (skills); references/testing-method.md § Sources (citations) |

Checks: factcheck 0 missing; linecheck 11 flagged → 10 scaffolding, 1 paraphrased (listed below), 0 lost; validator clean.
Paraphrased lines: "campaign strategy decisions or when structuring a test within a broader campaign architecture" → SKILL.md § References (`09-campaign-strategy` entry).
Noticed, not changed: paid-test threshold "90% confidence" versus Meta's default display threshold "95%" (both kept as written, they describe different things). "95%+ of East African users view social media content on mobile" is undated with no register record (kept).

## meta-tools-stack-evaluation — 301 → 134 lines (gated shared ratio 13.2 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Purpose" paragraph | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | Generated contract prose (see common note) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows: AI tool audit → ai-tool-fit reference; AI shortlist → vendor due diligence; route to `meta-budget-planner` | KEPT | SKILL.md § Decision Rules |
| 4 | "## Read next" / "## References" links | MERGED-INTO-CONTRACT | SKILL.md § References |
| 5 | "## Required Input" (7 items, "do not proceed until all seven") | MOVED | references/core-tools-and-budget-stacks.md § Required Input; summarised in SKILL.md § Required Inputs |
| 6 | "## Section 1 — Tool Stack Principles" (5 principles) | MOVED | references/core-tools-and-budget-stacks.md § Section 1; SKILL.md § Decision Rules |
| 7 | "## Section 2 — Core Tools Reference Table" (6 category tables) | MOVED | references/core-tools-and-budget-stacks.md § Section 2 |
| 8 | "## Section 3 — Recommended Stacks by Budget" | MOVED | references/core-tools-and-budget-stacks.md § Section 3; summary table in SKILL.md § Budget stacks and the five-question test |
| 9 | "## Section 4 — Tool Evaluation Framework" | MOVED | references/core-tools-and-budget-stacks.md § Section 4; test and rule also in SKILL.md |
| 10 | "## Output Format" (6 sections) | MOVED | references/core-tools-and-budget-stacks.md § Output Format; SKILL.md § Outputs |
| 11 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 12 | "## Related Skills" (4 items incl. AI-assisted production workflow link) | MERGED-INTO-CONTRACT | SKILL.md § References |
| 13 | "## References" (Chaffey 2024, Bodnar and Cohen 2012, Uganda DPA 2019) | MOVED | references/core-tools-and-budget-stacks.md § Sources; DPA also in SKILL.md § Decision Rules |
| 14 | ai-tool-fit reference pointer to "core tables in the parent `SKILL.md`" | Appended § Section locations after S09 | references/ai-tool-fit-access-cost-governance.md |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: USD list prices (Buffer $6, Hootsuite $99, Sprout Social $249, etc.) and the UGX stack totals are undated with no register record (kept). ai-tool-fit reference uses different budget tiers (Starter under UGX 500,000) from this skill's Starter stack (UGX 50,000–150,000) (both kept).

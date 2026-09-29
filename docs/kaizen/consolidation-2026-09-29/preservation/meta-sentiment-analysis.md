# Preservation map — meta-sentiment-analysis → meta-social-listening

Filled from [preservation-map-template.md](../preservation-map-template.md) for Social Kaizen S04-T09. See [merge-runbook.md](../merge-runbook.md), step 2.

Source: skills/meta-analytics-ops/meta-sentiment-analysis/SKILL.md @ 8eacccb (363 lines; reads Aug–Sep 2026: 0; fan-in 2)
Destination reference: skills/meta-analytics-ops/meta-social-listening/references/sentiment-and-share-of-voice-method.md (abbreviated `SSV` below)

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding: Use When, Do Not Use When, Required Inputs table, Outputs, Evidence Produced, Capability and permission boundary, Degraded mode, Decision rules (3 generic rows), Workflow steps 1–6, Quality Standards, Anti-Patterns bullets 1–5, Worked example | meta-social-listening/SKILL.md same-named sections | DROPPED-DUPLICATE-OF target SKILL.md `Use When` … `Worked example` (identical templated text, differing only in the deliverable name "sentiment analysis with method, confidence and implications" vs "social listening plan, query set and intelligence log" and the key input "dated listening dataset" vs "brand terms"; the neighbour-routing rows that named each other are replaced in the target by the two new Decision rules rows pointing at SSV and the listening-operations reference; the "dated listening dataset, query taxonomy and sampling method" input is carried as SSV § Inputs last row) | ticked |
| 2 | Read next / References: links to meta-social-listening, anti-ai-slop, ai-slop-audit, AGENTS-style verification note | meta-social-listening/SKILL.md § Read next and § References | DROPPED-DUPLICATE-OF target § Read next (`anti-ai-slop` "during production", `ai-slop-audit` "at the release checkpoint" present verbatim) and target § References ("Verify current platform, price, legal and regulatory claims before use." present verbatim); the link to meta-social-listening is the target itself | ticked |
| 3 | Scope distinction note (analytical methodology; listening provides the data, this skill the analysis; complementary) | SSV § When to use this reference (paragraph 2) | MOVED (re-pointed from playbook-sentiment-listening to the parent SKILL.md and listening-operations-playbook.md) | ticked |
| 4 | Required Input (8 items: client name + industry example "Kigali Fresh Bakery", country/city default Uganda/Kampala, primary goal 4 options, platforms 7, tool budget 4 tiers, languages 4, up to 3 competitors, native analytics access) | SSV § Inputs (table) | MOVED | ticked |
| 5 | Section 1: Manual vs Automated Sentiment Scoring — intro (hybrid recommended for most EA clients) | SSV § Procedure › Step 1 intro + § Decision rules row 3 | MOVED | ticked |
| 6 | Manual Scoring — when (no budget, Luganda/Swahili, < 500 mentions/month), 5-step process (last 100 items per platform, Google Sheet/Airtable), four-category scheme P/N/Neg/M, five negative sub-categories, 30–45 min per platform per month | SSV § Step 1a (process list + two tables) + § Decision rules row 1 | MOVED | ticked |
| 7 | Automated Scoring — when (> 500 English mentions/month/platform or real-time); 4-row tool-by-budget table (MonkeyLearn 300 queries free; Mention Starter; Sprout Social / Hootsuite Insights; Brandwatch) | SSV § Step 1b (table, verify-before-stating note) + § Decision rules row 2 | MOVED | ticked |
| 8 | NLP language limitation: English reliable; Luganda and Swahili unreliable across all commercial tools as of 2025, sometimes inverted; always review manually | SSV § Step 1b paragraph + § Decision rules row 4 | MOVED (verify-before-stating note added; no register record) | ticked |
| 9 | Hybrid Approach (3 bullets: automate English on Facebook/Instagram; manual WhatsApp, Luganda/Swahili, complaint threads; one sheet for NSS) | SSV § Step 1c | MOVED | ticked |
| 10 | Section 2: Net Sentiment Score — formula, Mixed excluded from numerator, Neutral+Mixed in denominator, worked example 85/12/43 = 52.1, express as number never word | SSV § Step 2 | MOVED | ticked |
| 11 | NSS benchmarks for EA service businesses (5 bands: +60, +40–59, +20–39, 0–19, below 0 → crisis playbook) | SSV § Step 2 table + § Decision rules row 6 | MOVED (note added that the operating bands after Johnsen (2024) differ and live in listening-operations-playbook.md § 3) | ticked |
| 12 | Tracking NSS over time (trend not snapshot; +45 → +48 → +52 example; tip: stable +40s beats improving from +15) | SSV § Step 2 closing paragraph | MOVED | ticked |
| 13 | Section 3: Share of Voice — formula, worked example 240/180/95 = 46.2% | SSV § Step 3 | MOVED | ticked |
| 14 | Gathering SOV Data in the EA Market (4 methods in preference order; weekly counts summed monthly) | SSV § Step 3 numbered list | MOVED | ticked |
| 15 | Competitor Selection Rules (2–3 direct competitors; exclude national/international brands for local SMEs; quarterly review) | SSV § Step 3 bullets + § Decision rules row 5 | MOVED | ticked |
| 16 | SOV Targets and Strategic Responses (3-row table: < 25%, 25–40%, > 40%) | SSV § Step 3 table | MOVED | ticked |
| 17 | Section 4: Conversation Theme Extraction — positive themes (3 questions; content pillars in plain sight; 10-content-pillars) | SSV § Step 4 paragraph 2 | MOVED (link to skills/pipeline/10-content-pillars) | ticked |
| 18 | Negative themes (3 questions; improvement briefs not marketing problems; escalate at 5+ per month) | SSV § Step 4 paragraph 3 + § Decision rules row 7 | MOVED | ticked |
| 19 | Theme Extraction Process (Manual) — 5 steps, "Priority Issues", "Top Positive Themes", 20–30 min per platform | SSV § Step 4 numbered list | MOVED | ticked |
| 20 | Section 5: Translating Sentiment Into Strategy — 8-row finding → action table; owner and deadline rule (Funk, 2013) | SSV § Step 5 + § Decision rules row 8 | MOVED | ticked |
| 21 | Section 6: Monthly Sentiment Report Template — delivery rule (with meta-reporting or design-system-skills handoff; no local deck route; not standalone unless requested), code-block template, populate-all-fields rule | SSV § Template — monthly sentiment report | MOVED (design engine named in plain text) | ticked |
| 22 | Quality Criteria (8 items) | SSV § Checklist (8 items) | MOVED | ticked |
| 23 | Citation: Funk, T. (2013) *Advanced Social Media Marketing*. Apress. | SSV § Sources; cited in Step 2 and Step 5 | MOVED | ticked |
| 24 | Citation: Schaffer, N. (2013) *Maximize Your Social*. Wiley. | SSV § Sources; cited in Step 3 | MOVED | ticked |
| 25 | Citation: Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson. | SSV § Sources | MOVED | ticked |
| 26 | Related Skills (playbook-sentiment-listening, meta-reporting, meta-competitor-analysis, playbook-crisis-communications, 10-content-pillars) | SSV § Onward use (4 links) + § When to use (listening-operations-playbook.md replaces the retired playbook-sentiment-listening) | MOVED | ticked |
| 27 | Reference files (`references/`) | none — source has no `references/` folder | n/a | ticked |
Unique facts with register IDs carried: none (source cites no source-register IDs; freshness re-checked: NOT_ASSESSED). SSV adds verify-before-stating notes (no register record) for the tool tiers/quotas and the 2025 Luganda/Swahili NLP reliability claim.
Items dropped as duplicates (must name the equivalent target text): 2
Reviewer: independent review agent (Claude Opus 5.5, read-only, S04 review) — verdict ACCEPT (MonkeyLearn availability carried with a verify note) — 2026-09-29

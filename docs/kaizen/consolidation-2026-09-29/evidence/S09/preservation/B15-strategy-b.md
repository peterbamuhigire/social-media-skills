# S09 preservation log — B15-strategy-b

Worker: S09 worker agent (Claude), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. Frontmatter, `## Use When` and `## Do Not Use When` copied verbatim from HEAD (routecheck clean). Every moved block is copied from `git show 0e0af8a:<path>` without rewording.

## strategy-creator-monetisation — 300 → 119 lines (gated shared ratio 19.1 % → 1.6 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic Required Inputs rows, generic Workflow, Outputs, Evidence, Capability, Degraded, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" (3 rows) | KEPT | SKILL.md § Decision Rules (3 kept + 5 domain rows drawn from Sections 4–6) |
| 3 | "## References" (3 links) | KEPT | SKILL.md § References (reformatted to `: read when`; 3 links added) |
| 4 | "*Based on Dallas, M. (2022)…*" attribution line | MOVED | references/creator-monetisation-method.md (head) |
| 5 | "## Required Input" (7 intake questions) | MOVED; MERGED-INTO-CONTRACT | references/creator-monetisation-method.md § Required Input; SKILL.md § Required Inputs |
| 6 | "## Section 1: EA Creator Monetisation Landscape" incl. "### Income and job-claim safety" | MOVED | references/creator-monetisation-method.md § Section 1 |
| 7 | "## Section 2: YouTube Partner Programme (YPP)" (eligibility check, revenue expectations, path-to-1,000 table, niche note) | MOVED | references/creator-monetisation-method.md § Section 2 |
| 8 | "## Section 3: TikTok Creator Monetisation" | MOVED | references/creator-monetisation-method.md § Section 3 |
| 9 | "## Section 4: Affiliate Marketing" (programmes table, fit criteria, disclosure with register IDs, earnings estimate) | MOVED (backticked 08 path given one extra `../`) | references/creator-monetisation-method.md § Section 4 |
| 10 | "## Section 5: Digital Products" (product and channel tables, recommendation logic) | MOVED | references/creator-monetisation-method.md § Section 5 |
| 11 | "## Section 6: Brand Partnerships" (deal types, distribution + talent fee, triage and declines, pitch template) | MOVED | references/creator-monetisation-method.md § Section 6 |
| 12 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 9 kept; bullets 1+9 and 4+5 combined) |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding (generic input row, generic workflow step 1, generic output row, "Output is of professional standard…" lead-in), 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none flagged.
Noticed, not changed: the description names "TikTok eligibility" while Section 3 says the original Creator Fund may no longer exist (kept both). Section 1 says "five streams below" but the sections list YPP, TikTok, affiliate, digital products and brand partnerships; the workflow now names those five.

## strategy-csr-purpose-communications — 230 → 120 lines (gated shared ratio 23.9 % → 3.2 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic inputs, workflow, outputs, evidence, capability, degraded, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" (4 rows incl. digital-transparency row) | KEPT | SKILL.md § Decision Rules (4 kept + 4 domain rows) |
| 3 | "## Required Input" (7 questions) | MOVED; MERGED-INTO-CONTRACT | references/csr-communication-method.md § Required Input; SKILL.md § Required Inputs |
| 4 | "## Section 1 — Purpose vs CSR vs Greenwashing" | MOVED | references/csr-communication-method.md § Section 1 |
| 5 | "## Section 2 — CSR Audit" (table) | MOVED | references/csr-communication-method.md § Section 2 |
| 6 | "## Section 3 — Content Strategy for CSR" (4 content types, examples) | MOVED | references/csr-communication-method.md § Section 3 |
| 7 | "## Section 4 — Messaging Framework" (5 principles) | MOVED | references/csr-communication-method.md § Section 4 |
| 8 | "## Section 5 — East Africa-Specific Considerations" (incl. children's consent rule, platform table) | MOVED | references/csr-communication-method.md § Section 5 |
| 9 | "## Quality Criteria" (7 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (7 kept verbatim + 1 release-gate bullet) |
| 10 | Second "## References" (4 "See …" lines) and first References list | MERGED-INTO-CONTRACT | SKILL.md § References (as links with `: read when`) |

Checks: factcheck 0 missing; linecheck 5 flagged → 4 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "See `05-social-media-strategy/SKILL.md` for the broader social media strategy framework…" → SKILL.md § References (`05-social-media-strategy` link).
Noticed, not changed: "Uganda's Children Act (Cap. 59)" citation not re-verified; the Monitor, Observer and NBS scepticism claims are unsourced.

## strategy-customer-value-journey — 390 → 129 lines (gated shared ratio 11.8 % → 3.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic inputs, workflow, outputs, evidence, capability, degraded, 6 generic anti-patterns, 4 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" (3 rows) | KEPT | SKILL.md § Decision Rules (3 kept + 5 domain rows) |
| 3 | "## Framework Attribution" | MOVED | references/cvj-method.md § Framework Attribution |
| 4 | "## Required Input" (8 questions) | MOVED; MERGED-INTO-CONTRACT | references/cvj-method.md § Required Input; SKILL.md § Required Inputs |
| 5 | "## The Two Most Common EA SME Failure Modes" | MOVED | references/cvj-method.md (same heading); decision rows in SKILL.md |
| 6 | "## The 8 Stages of the Customer Value Journey" | MOVED | references/cvj-method.md (same heading) |
| 7 | "## Entry-Point Offers vs. Ascension Offers" | MOVED | references/cvj-method.md (same heading) |
| 8 | "## Mapping Social Media Content to the CVJ" (table) | MOVED | references/cvj-method.md (same heading) |
| 9 | "## WhatsApp in the CVJ" (incl. boundary line) | MOVED | references/cvj-method.md; boundary also in SKILL.md § Capability and Permission Boundaries |
| 10 | "## CVJ Audit" (5 steps) | MOVED | references/cvj-method.md; summarised in SKILL.md § Workflow 2–3 |
| 11 | "## Building the CVJ Content Plan" (ratio table, per-gap outputs, sequencing rule) | MOVED; ratio table also KEPT | references/cvj-method.md; SKILL.md § Content share by journey zone |
| 12 | "## Referral Loop Design" | MOVED | references/cvj-method.md (same heading) |
| 13 | "## Metrics Per CVJ Stage" (table) | MOVED | references/cvj-method.md (same heading) |
| 14 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |
| 15 | Final "## References" (4 citations + book-driven link) | MOVED / KEPT | citations → references/cvj-method.md § Sources; link → SKILL.md § References |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none flagged.
Noticed, not changed: "respond to enquiries within two hours" and "Hi [name] … increases open rates" carry no source.

## strategy-ewom-reviews — 250 → 119 lines (gated shared ratio 23.5 % → 3.3 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic inputs, workflow, outputs, evidence, capability, degraded, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" (5 rows incl. two reference rows) | KEPT | SKILL.md § Decision Rules (5 kept + 3 domain rows) |
| 3 | "**Source:** Hanlon and Tuten (2022)" line | MOVED | references/ewom-programme-method.md (head) |
| 4 | Second "## Required Inputs" (8 questions) | MOVED; MERGED-INTO-CONTRACT | references/ewom-programme-method.md § Required Inputs; SKILL.md § Required Inputs |
| 5 | "## eWOM vs. Reputation Management" | MOVED | references/ewom-programme-method.md (same heading) |
| 6 | "## The GST Framework (Hanlon and Tuten, 2022)" | MOVED | references/ewom-programme-method.md (same heading) |
| 7 | "## Identifying eWOM Transmitters" | MOVED | references/ewom-programme-method.md (same heading) |
| 8 | "## Activation Tactics" (peak moments, template, incentives) | MOVED | references/ewom-programme-method.md (same heading) |
| 9 | "## The Objectivity Principle" | MOVED | references/ewom-programme-method.md (same heading) |
| 10 | "## eWOM Measurement Framework" (6 metrics) | MOVED | references/ewom-programme-method.md (same heading) |
| 11 | "## Platform Priority for EA Clients" | MOVED | references/ewom-programme-method.md (same heading) |
| 12 | "## eWOM Programme Build Sequence" (7 steps) | MOVED | references/ewom-programme-method.md (same heading) |
| 13 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none flagged.
Noticed, not changed: "Response rates drop by approximately 80% after 48 hours" is already marked a legacy figure with no register record. Negative reviews: "respond within 24 hours" vs the build sequence's weekly check-and-respond routine (both kept). "The counterintuitive evidence is robust (Rageh, 2026)" kept verbatim in the reference (HEAD wording).

## strategy-experiential-marketing — 254 → 117 lines (gated shared ratio 21.2 % → 3.4 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic inputs, workflow, outputs, evidence, capability, degraded, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" (4 rows incl. webinar row) | KEPT | SKILL.md § Decision Rules (4 kept + 4 domain rows) |
| 3 | "**Sources:** Hanlon and Tuten (2022) … Schmitt (1999) and Pine and Gilmore (1998)" | MOVED | references/experiential-marketing-method.md (head) |
| 4 | Second "## Required Inputs" (8 questions) | MOVED; MERGED-INTO-CONTRACT | references/experiential-marketing-method.md § Required Inputs; SKILL.md § Required Inputs |
| 5 | "## Why Experiential Marketing Matters" (Experience Economy table, UGX figures) | MOVED | references/experiential-marketing-method.md (same heading) |
| 6 | "## Schmitt's ExM Framework — Four Distinguishing Features" | MOVED | references/experiential-marketing-method.md (same heading) |
| 7 | "## Experience Design Principles" (sensory, participation, shareable, pre/post) | MOVED | references/experiential-marketing-method.md (same heading) |
| 8 | "## Digital and Hybrid ExM for EA Clients" | MOVED | references/experiential-marketing-method.md (same heading) |
| 9 | "## ExM Measurement Framework" (7 metrics) | MOVED | references/experiential-marketing-method.md (same heading) |
| 10 | "## EA-Specific Considerations" | MOVED | references/experiential-marketing-method.md (same heading); decision rows in SKILL.md |
| 11 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none flagged.
Noticed, not changed: post-event NPS is "within 48 hours" in the follow-up list but "Within 24 hours" in the measurement table (both kept). "Open rates on WhatsApp in EA are significantly higher" and "viewers leave within 30 seconds" have no source.

## strategy-personal-brand — 472 → 126 lines (gated shared ratio 11.2 % → 1.5 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic inputs, workflow, outputs, evidence, capability, degraded, 6 generic anti-patterns, 4 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" (3 rows) | KEPT | SKILL.md § Decision Rules (row 1 kept; generic authority and evidence rows combined into the last row; 6 domain rows) |
| 3 | "## Required Input" (10 questions) | MOVED; MERGED-INTO-CONTRACT | references/personal-brand-method.md § Required Input; SKILL.md § Required Inputs |
| 4 | "## Section 1 — Personal Brand Foundation" (1.1–1.6: Three-Strand Test, Sheahan's Wall, KNOWN, BPS, DCPR, pillars, attributes, four levers) | MOVED | references/personal-brand-method.md § Section 1 |
| 5 | "## Section 2 — Client Type Platform Guide" (table, VCP) | MOVED | references/personal-brand-method.md § Section 2 |
| 6 | "## Section 3 — Platform Strategy" (LinkedIn, Facebook, X, WhatsApp Status) | MOVED | references/personal-brand-method.md § Section 3 |
| 7 | "## Section 4 — Content Strategy" (3.1–3.3, workflows, 10-4-1) | MOVED | references/personal-brand-method.md § Section 4 |
| 8 | "## Section 5 — Consistency System" | MOVED | references/personal-brand-method.md § Section 5 |
| 9 | "## Section 6 — Authority Building Beyond Content" (bio, speaking, media, peers, op-eds, PBA) | MOVED (PBA link re-pointed to the sibling file) | references/personal-brand-method.md § Section 6 |
| 10 | "## Section 7 — Monetisation Pathways (P.A.I.D.S.)" | MOVED | references/personal-brand-method.md § Section 7 |
| 11 | "## Section 8 — Measurement" (6-month table) | MOVED | references/personal-brand-method.md § Section 8 |
| 12 | "## Section 9 — Blog Post Angles" (10 titles) | MOVED | references/personal-brand-method.md § Section 9 |
| 13 | "## Quality Criteria" (10 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 bullets covering all 10; full list → references/personal-brand-method.md § Quality checklist (full)) |
| 14 | Second "## References" (related-skills table, reference-files table) | MOVED; MERGED-INTO-CONTRACT | references/personal-brand-method.md § Related skills and reference files; SKILL.md § References (as links) |
| 15 | British English footer line | MOVED | references/personal-brand-method.md (end); SKILL.md § Quality Standards |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none flagged.
Noticed, not changed: internal cross-references are misnumbered in HEAD ("positioning statement from Section 1.1" is 1.2; "three pillars from Section 1.2" are 1.4; Section 4 sub-headings numbered 3.x). "PBA … kept separate from any personal board" reads as self-contradictory. Unsourced figures: "Personal profile reaches 10× more than company page", "3%+ is healthy", P.A.I.D.S. start thresholds "500+" and "5K+", the 70/30 sponsored ratio.

## strategy-video-content — 418 → 120 lines (gated shared ratio 15.3 % → 1.6 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic inputs, workflow, outputs, evidence, capability, degraded, 6 generic anti-patterns, 3 generic quality bullets) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "## Decision Rules" (5 rows incl. AI-avatar and podcast rows) | KEPT | SKILL.md § Decision Rules (rows 1, 4, 5 kept; generic authority and evidence rows combined; 4 domain rows) |
| 3 | "## Required Input" (8 bullets) | MOVED; MERGED-INTO-CONTRACT | references/organic-video-method.md § Required Input; SKILL.md § Required Inputs |
| 4 | "## Strategic Foundation" (three laws) | MOVED | references/organic-video-method.md (same heading) |
| 5 | "## The WILMA Test (Waters, 2019)" | MOVED | references/organic-video-method.md (same heading) |
| 6 | "## Platform-by-Platform Video Blueprint" (TikTok, Reels, YouTube, Facebook, WhatsApp Status) | MOVED | references/organic-video-method.md (same heading) |
| 7 | "## Hook Writing Framework" | MOVED | references/organic-video-method.md (same heading) |
| 8 | "## Video Script Templates" | MOVED | references/organic-video-method.md (same heading) |
| 9 | "## The Selling 7 — Sales-Enabling Video Framework (Sheridan, 2019)" | MOVED | references/organic-video-method.md (same heading) |
| 10 | "## On-Camera Performance Rules (Sheridan, 2019)" | MOVED | references/organic-video-method.md (same heading) |
| 11 | "## Video Content Calendar Logic" (Hero/Hub/Hygiene, repurposing chain) | MOVED | references/organic-video-method.md (same heading) |
| 12 | "## Analytics and Optimisation" (metrics, 14-day rule) | MOVED | references/organic-video-method.md (same heading); 14-day rule also in SKILL.md § Decision Rules |
| 13 | "## Six Story Characteristics (Handley, 2012)" | MOVED | references/organic-video-method.md (same heading) |
| 14 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 kept) |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none flagged.
Noticed, not changed: completion-rate targets compete (TikTok "70%+ … pushed to new audiences" vs analytics "60–70% for short-form"). The quality criterion says "five key metrics" but the analytics table lists six. Unsourced or book-only figures kept as they are: "80% of clicks come from the thumbnail", "85% … without sound (Waters, 2019)", "shortening the sales cycle by 30–50%", "up to 80% (Sheridan, 2019)", "20–40%", "25–30 additional profile views". "Vidyard Goboard" may be a garbled product name.

## traction-channel-bullseye — 120 → 112 lines (gated shared ratio 3.6 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro, Required Inputs, Decision Rules, Quality Standards, Anti-Patterns, Evidence Produced | KEPT | SKILL.md (unchanged) |
| 2 | "## Workflow" step 7 (re-run triggers) | CONDENSED-IN-PLACE | SKILL.md § Workflow 7 (now names correct and rerun) |
| 3 | "## Outputs" header "Observable acceptance condition" | CONDENSED-IN-PLACE | SKILL.md § Outputs (canonical header; 4 rows kept) |
| 4 | "## Capability and Permission Boundaries" | REPLACED-BY-CANONICAL (domain facts kept) | SKILL.md: canonical sentence + lawful basis, named owner, supplied data |
| 5 | "## Degraded Mode" | REPLACED-BY-CANONICAL (domain facts kept) | SKILL.md: canonical sentence + idea sheet, draft test cards, tracking list, no focus channel |
| 6 | "## References" (5 links with dashes) | KEPT | SKILL.md § References (`: read when`; `media-planning` neighbour added) |
| 7 | "## Plan section slot template" | MOVED | references/bullseye-channels-and-test-cards.md § Plan section wording |
| 8 | "## Before and after" | MOVED | references/bullseye-channels-and-test-cards.md § Plan section wording |
| 9 | Acknowledgement line | KEPT | SKILL.md (end, after the marker) |

Checks: factcheck 0 missing; linecheck 0 flagged; validator clean.
Paraphrased lines: none.
Noticed, not changed: none.

## Batch checks

- `validate_skill_engine.py --json`: no findings for any B15 skill (the one remaining `line_budget` finding belongs to another batch).
- `routecheck.py`: nothing `CHANGED` for B15 skills.
- `factcheck.py` over all 8 skills: 0 missing fact tokens.
- `measure_skill_scaffolding.py`: gated ratio 0.0–3.4 % for every B15 skill.
- `pytest -k markdown_links`: passed. `git diff --check` on B15 paths: clean.

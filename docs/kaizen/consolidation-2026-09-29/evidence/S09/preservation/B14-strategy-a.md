# S09 preservation log — B14-strategy-a

Worker: S09 worker agent (Claude), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10.

## ecommerce-brand-differentiation — 329 → 131 lines (gated shared ratio 16.8 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Frontmatter, H1, "## Use When", "## Do Not Use When" | KEPT | SKILL.md (byte for byte) |
| 2 | Generated contract prose (3 generic input rows, 6 generic workflow steps, 2 generic output rows, generic evidence rows, Capability, Degraded, 2 generic decision rows, 3 generic quality bullets, 6 generic anti-patterns, AGENTS.md link) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision row "price-led sameness rather than checkout friction" | KEPT | SKILL.md § Decision Rules row 1 |
| 4 | Quality bullets "Uganda/East Africa, British English… WhatsApp-first" and anti-slop gate | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (last bullet); § References (anti-slop, ai-slop-audit) |
| 5 | "## Required Input" (8 intake questions) | MOVED | references/differentiation-method.md § Intake questions; folded into SKILL.md § Required Inputs |
| 6 | "## Section 1 — Why Brand Differentiation Matters" (25% figure, Soleness, Option Planning Quadrant Matrix) | MOVED (text unchanged) + quadrant table KEPT | references/differentiation-method.md § Section 1; SKILL.md § Option Planning Quadrant; 25% figure in intro |
| 7 | "## Section 2 — The 9 Intangible Brand Types" (9 sub-sections) | MOVED | references/differentiation-method.md § Section 2 |
| 8 | "## Section 3 — Competitive Positioning" (Soleness statement + 5 tests, positioning map, Blue Ocean four actions, category creation) | MOVED | references/differentiation-method.md § Section 3; decision rules in SKILL.md |
| 9 | "## Section 4 — Brand Naming" (six types, 5 characteristics) | MOVED | references/differentiation-method.md § Section 4 |
| 10 | "## Section 5 — Visual Identity Direction" (colour table, typography, packaging stats and checklist) | MOVED | references/differentiation-method.md § Section 5; Uganda batch/expiry rule also SKILL.md § Decision Rules |
| 11 | "## Section 6 — Community Building" (1,000 True Fans, tactics table, platform fit) | MOVED | references/differentiation-method.md § Section 6; cash-perk rule also SKILL.md § Decision Rules |
| 12 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 bullets, two pairs combined); full list verbatim in references/differentiation-method.md § Full quality checklist |
| 13 | "## References" (4 citations, 2 skill pointers) | MOVED | references/differentiation-method.md § Sources (skill pointers converted to relative links); SKILL.md § References |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: Blue Ocean cited as Kim and Mauborgne 2005 in Section 3 but 2015 in the references list (same split in social-commerce-strategy). The Verma (2019) source line names "7C Canvas" and "Brand Benefits Pyramid", which this skill does not describe (the Pyramid is in social-commerce-strategy). Packaging statistics (33%, 52%, 40%, 74%) are attributed to Verma (2019) with no primary source. Scheduled S10 merge into a new skill still pending.

## ecommerce-export-marketing-advisory — 162 → 117 lines (gated shared ratio 34.2 % → 1.8 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Frontmatter, H1, first "## Use When", first "## Do Not Use When" | KEPT | SKILL.md |
| 2 | Generated contract prose (generic input rows, workflow, outputs, evidence, Capability, Degraded, 2 generic decision rows, generic quality bullets and anti-patterns) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision row "Market, fulfilment, compliance, or unit-economics evidence is missing" | KEPT | SKILL.md § Decision Rules row 2 |
| 4 | "Acknowledgement" line | KEPT | SKILL.md after end marker |
| 5 | "## Overview" | CONDENSED-IN-PLACE | SKILL.md intro |
| 6 | Second "## Use When" (3 bullets, outside markers) | MERGED-INTO-CONTRACT | SKILL.md intro (EAC/export via digital channels; margin, CAC, logistics, payment reality); § Outputs (plan, outline, review, checklist, outreach pack) |
| 7 | Second "## Do Not Use When" (3 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules rows 1, 3, 4; § Required Inputs row 1 and 3 |
| 8 | "## Required Inputs" (3 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Required Inputs rows 2–4 |
| 9 | "## Workflow" (8 steps) | KEPT (tightened, stop and rerun added) | SKILL.md § Workflow steps 2–8 |
| 10 | "## Quality Bar" (5 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 5 kept) |
| 11 | "## Anti-Patterns" (5 bullets) | KEPT, each with Fix | SKILL.md § Anti-Patterns |
| 12 | "## Outputs" (7 items) | MERGED-INTO-CONTRACT | SKILL.md § Outputs (5 rows covering all 7) |
| 13 | "## References" (2 links) | KEPT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 5 flagged → 3 scaffolding, 2 paraphrased, 0 lost; validator clean.
Paraphrased lines: "enter or grow in another EAC market…through digital channels" and "must fit the company's margin, CAC, logistics, and payment reality" → SKILL.md intro (now above threshold).
Noticed, not changed: HEAD carried duplicate Use When / Do Not Use When sections outside the markers; only the routed pair remains as headings.

## marketing-foundations-stp-positioning — 132 → 114 lines (gated shared ratio 3.0 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Frontmatter, H1, intro, Use When, Do Not Use When, Required Inputs, Workflow, Decision Rules, Quality Standards, Anti-Patterns | KEPT | SKILL.md |
| 2 | Outputs header "Observable acceptance condition" | CONDENSED-IN-PLACE | SKILL.md § Outputs (canonical header) |
| 3 | Capability paragraph | REPLACED-BY-CANONICAL + domain sentence | SKILL.md § Capability and Permission Boundaries (surveys, interviews, list matching need lawful basis kept) |
| 4 | Degraded Mode | REPLACED-BY-CANONICAL + domain sentence | SKILL.md § Degraded Mode (provisional sheet, sprint plan, re-test date, never validated kept) |
| 5 | "## References" (6 links) | KEPT, reformatted to "read when"; anti-slop added | SKILL.md § References |
| 6 | "## Foundation sheet (one page)" (table) | MOVED | references/foundation-sheet-and-worked-example.md |
| 7 | "## Worked example (labelled scenario…)" | MOVED | references/foundation-sheet-and-worked-example.md |
| 8 | Acknowledgement line | KEPT | SKILL.md after end marker |

Checks: factcheck 0 missing; linecheck 0 flagged; validator clean.
Paraphrased lines: none.
Noticed, not changed: Kelley and Sheehan dated "c. 2021–22" and Abrams / Wheelen and Hunger undated in references/positioning-and-mix-toolkit.md (pre-existing).

## peso-integrated-strategy — 305 → 129 lines (gated shared ratio 18.0 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Frontmatter, H1, Use When, Do Not Use When | KEPT | SKILL.md |
| 2 | Generated contract prose (generic inputs, workflow, outputs, evidence, Capability, Degraded, 2 generic decision rows, generic quality and anti-patterns, AGENTS.md link) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows "cross-channel orchestration" and "Owned pillar… under 500 email subscribers" | KEPT | SKILL.md § Decision Rules rows 1–2 |
| 4 | Reference link owned-media-assets | KEPT | SKILL.md § References |
| 5 | "## Required Input" (7 questions) | MOVED | references/peso-method.md § Intake questions; folded into SKILL.md § Required Inputs |
| 6 | "## Section 1 — PESO Explained" | MOVED | references/peso-method.md § Section 1; key insight in SKILL.md intro |
| 7 | "## Section 2 — PESO Channel Map" (18-row table, guidance) | MOVED | references/peso-method.md § Section 2; "three to five channels" also SKILL.md § Decision Rules |
| 8 | "## Section 3 — PESO Integration Principles" (6) | MOVED + condensed summary KEPT | references/peso-method.md § Section 3; SKILL.md § PESO integration principles |
| 9 | "## Section 4 — PESO Strategy Output" (template in code block) | MOVED (text unchanged, separators inside the block kept) | references/peso-method.md § Section 4 |
| 10 | "## Section 5 — EA-Specific Guidance" (6 items) | MOVED | references/peso-method.md § Section 5; boost threshold, SMS, Shared-pause and Earned-voices rules also in SKILL.md § Decision Rules / Anti-Patterns |
| 11 | "## Quality Criteria" (7 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 7); verbatim in references/peso-method.md § Full quality checklist |
| 12 | "## References" (4 skill pointers, Dietrich, Chaffey, Bodnar and Cohen) | MOVED | references/peso-method.md § Related skills and sources (pointers now relative links); key skills also SKILL.md § References |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: Dietrich (2020) *Spin Sucks: PR in the Digital Age*, Que Publishing — date and subtitle look doubtful (the book first appeared in 2014). Principle 6 says "Launch Owned before Earned and Shared before Paid" while its sequence reads Owned → Shared → Earned → Paid. references/owned-media-assets.md still points to "SKILL.md Section 3 principle 1" and "Section 5 EA guidance"; those sections now live in references/peso-method.md (pointer not edited).

## social-commerce-strategy — 392 → 122 lines (gated shared ratio 13.0 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Frontmatter, H1, Use When, Do Not Use When | KEPT | SKILL.md |
| 2 | Generated contract prose (generic inputs, workflow, outputs, evidence, Capability, Degraded, 2 generic decision rows, generic quality and anti-patterns, AGENTS.md link) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows "order-to-payment workflow" and "Instagram DMs… 5-stage DM sequence" | KEPT | SKILL.md § Decision Rules rows 1–2 |
| 4 | Reference link dm-conversation-selling | KEPT | SKILL.md § References |
| 5 | "## Required Input" (8 questions) | MOVED | references/social-shop-setup-and-operations.md § Intake questions; folded into SKILL.md § Required Inputs |
| 6 | "## Section 1 — Social Commerce in East Africa" (conversation-led model, RACE) | MOVED | references/social-shop-setup-and-operations.md § Section 1; SKILL.md intro and Workflow step 2 |
| 7 | "## Section 2 — Platform Commerce Setup" (Facebook, Instagram, WhatsApp, TikTok) | MOVED | references/social-shop-setup-and-operations.md § Section 2; checkout and TikTok Shop limits also SKILL.md § Decision Rules |
| 8 | "## Section 3 — Payment Infrastructure" (table, recommendation, 6-step workflow) | MOVED | references/social-shop-setup-and-operations.md § Section 3; COD rule in SKILL.md § Decision Rules |
| 9 | "## Section 4 — Content Strategy for Social Commerce" (frequency, 6 types, 10-4-1 / 5-3-2) | MOVED | references/social-shop-setup-and-operations.md § Section 4 |
| 10 | "## Section 5 — Order Management System" (columns, 20/day trigger, tools) | MOVED | references/social-shop-setup-and-operations.md § Section 5; trigger in SKILL.md § Decision Rules |
| 11 | "## Section 6 — EA-Specific Considerations" (Mobile Money, delivery partners, VAT UGX 150 million, scams, tone) | MOVED | references/social-shop-setup-and-operations.md § Section 6; VAT and trust rules also SKILL.md |
| 12 | "## Section 7 — Product Pricing and Margin Management" | MOVED | references/pricing-conversion-and-differentiation.md § Section 7; 3X / UGX 90,000 rule in SKILL.md § Decision Rules |
| 13 | "## Section 8 — Conversion Optimisation" | MOVED | references/pricing-conversion-and-differentiation.md § Section 8 |
| 14 | "## Section 9 — Customer Data Intelligence" | MOVED | references/pricing-conversion-and-differentiation.md § Section 9; 80/20 in SKILL.md § Anti-Patterns |
| 15 | "## Section 10 — Brand Differentiation" | MOVED | references/pricing-conversion-and-differentiation.md § Section 10 |
| 16 | "## Quality Criteria" (11 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 bullets covering all 11); verbatim in references/pricing-conversion-and-differentiation.md § Full quality checklist |
| 17 | "## References" (6 skill pointers, key sources) | MOVED | platform pointers → references/social-shop-setup-and-operations.md § Platform skills…; CRO, differentiation pointers and key sources → references/pricing-conversion-and-differentiation.md § Related skills and sources; main links in SKILL.md § References |

Checks: factcheck 0 missing; linecheck 4 flagged → 3 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: "These platform-specific and strategy skills provide deeper implementation guidance:" → heading "## Platform skills for deeper implementation" in references/social-shop-setup-and-operations.md.
Noticed, not changed: Payment fees (~1.5%, 2.5–3.5%, 1.4%) and the UGX 150 million VAT threshold are undated; "85%+ of EA social commerce traffic is mobile" is uncited; "TikTok Shop is not available in Uganda as of 2026" needs a dated check; Blue Ocean dated 2005 in Section 10 and 2015 in key sources.

## strategy-b2b-customer-community — 124 → 125 lines (gated shared ratio 3.2 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Frontmatter, H1, intro, Use When, Do Not Use When, Required Inputs, Workflow, Evidence, Decision Rules, Quality Standards, Anti-Patterns | KEPT | SKILL.md |
| 2 | Outputs header "Observable acceptance condition" | CONDENSED-IN-PLACE | SKILL.md § Outputs (canonical header) |
| 3 | Capability paragraph | REPLACED-BY-CANONICAL + domain sentence | SKILL.md § Capability (lawful basis, registration, approver sign-off kept) |
| 4 | Degraded Mode | REPLACED-BY-CANONICAL + domain sentence | SKILL.md § Degraded Mode (deliverables and never-invent rule kept) |
| 5 | "## References" (5 links) | KEPT, reformatted to "read when"; anti-slop added | SKILL.md § References |
| 6 | "## Seven self-diagnostic questions" (outside markers) | KEPT, moved inside markers after Workflow | SKILL.md § Seven self-diagnostic questions |
| 7 | Acknowledgement line | KEPT | SKILL.md after end marker |

Checks: factcheck 0 missing; linecheck 0 flagged; validator clean.
Paraphrased lines: none.
Noticed, not changed: Marcos et al. dated "c. 2025" (pre-existing).

## strategy-channel-architecture — 336 → 129 lines (gated shared ratio 19.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Frontmatter, H1, Use When, Do Not Use When | KEPT | SKILL.md |
| 2 | Generated contract prose (generic inputs, workflow, outputs, evidence, Capability, Degraded, 2 generic decision rows, generic quality and anti-patterns, AGENTS.md link) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows "spread thinly" and "traction-channel-bullseye gate (19 channels, three capped tests)" | KEPT | SKILL.md § Decision Rules rows 1–2 |
| 4 | Intro paragraph after markers (Schaffer 2013) and cross-reference line | MOVED | SKILL.md intro (condensed); references/channel-architecture-method.md top (verbatim, links added) |
| 5 | "## Required Input" (8 questions) | MOVED | references/channel-architecture-method.md § Intake questions; folded into SKILL.md § Required Inputs |
| 6 | "## Output Structure" / "### Section 1 — Hub Definition" (hub priority table, EA note, format) | MOVED | references/channel-architecture-method.md; stale-website rule in SKILL.md § Decision Rules |
| 7 | "### Section 2 — Current Channel Audit" | MOVED | references/channel-architecture-method.md |
| 8 | "### Section 3 — Platform Role Assignment" (role table) | MOVED + role table KEPT | references/channel-architecture-method.md; SKILL.md § Platform roles (Schaffer, 2013) |
| 9 | "### Section 4 — Traffic Flow Map" (diagram, 3 EA examples) | MOVED | references/channel-architecture-method.md |
| 10 | "### Section 5 — Effort Allocation Table" and "### Participation, affordance and privacy check" | MOVED | references/channel-architecture-method.md; three-platform cap and participation card in SKILL.md |
| 11 | "### Section 6 — Content Flow Map" (three tiers, diagram) | MOVED | references/channel-architecture-method.md |
| 12 | "## EA-Specific Platform Notes" (7 items) | MOVED | references/channel-architecture-method.md; TikTok, YouTube, X and Group rules also SKILL.md |
| 13 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8); verbatim in references/channel-architecture-method.md § Full quality checklist |
| 14 | "## References" (4 citations) | MOVED | references/channel-architecture-method.md § Sources |
| 15 | Existing references/launch-channel-sequencing.md (unlinked in HEAD) | KEPT, now linked | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding, 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none.
Noticed, not changed: the intake says "Do not proceed until all six inputs are provided" but lists eight. "TikTok… fastest-growing discovery channel for 16–30 audiences in Uganda as of 2025" is undated evidence. Sobia Publication (2022) is cited but not used in the body.

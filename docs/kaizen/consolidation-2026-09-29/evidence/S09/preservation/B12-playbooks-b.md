# S09 preservation log — B12-playbooks-b

Worker: S09 worker agent (Claude Opus 5.5), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10.

## playbook-daily-operations-routine — 310 → 122 lines (gated shared ratio 14.0 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro paragraph (operating manual; PDCA sits above) | CONDENSED-IN-PLACE | SKILL.md intro; full wording in references/daily-routine-method.md opening |
| 2 | Generated contract prose (generic Required Inputs rows, Capability, Degraded, 3 generic decision rows, 5-step generic Workflow, generic Outputs/Evidence, Quality paragraph, 5 generic anti-patterns, "Use the directly cited sources" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows "urgent but not material" and "PDCA review cadence" | KEPT | SKILL.md § Decision Rules |
| 4 | Anti-pattern "Treating an inaccessible account… as healthy" | MERGED-INTO-CONTRACT | SKILL.md § Degraded Mode |
| 5 | "## Required Inputs" (5 intake questions) | MOVED + MERGED-INTO-CONTRACT | references/daily-routine-method.md § Intake questions; SKILL.md § Required Inputs rows |
| 6 | "## Section 1: Client Load Capacity Planning" (table, load limits, 20% reserve) | MOVED | references/daily-routine-method.md § Section 1; limits also in SKILL.md § Capacity limits for a solo consultant; 20% rule in Workflow 2 and Decision Rules |
| 7 | "## Section 2: Morning Monitoring Block" (incident check, response queue, EA note, analytics) | MOVED | references/daily-routine-method.md § Section 2; response order and crisis trigger also in SKILL.md § Decision Rules |
| 8 | "## Section 3: Content Production Block" (production order, scheduling discipline) | MOVED | references/daily-routine-method.md § Section 3; key items also in SKILL.md § Anti-Patterns |
| 9 | "## Section 4: Client Communication Block" (communication types, WhatsApp norms) | MOVED | references/daily-routine-method.md § Section 4 |
| 10 | "## Section 5: Afternoon and Weekly Rhythm" | MOVED | references/daily-routine-method.md § Section 5 |
| 11 | "## Section 6: Tools Stack" (table) | MOVED | references/daily-routine-method.md § Section 6 |
| 12 | "## Output Format" (7 manual sections, timing adjustment) | MOVED + MERGED-INTO-CONTRACT | references/daily-routine-method.md § Operating manual format; SKILL.md § Outputs and Workflow 7 |
| 13 | "## Cross-References" (6 items) | MERGED-INTO-CONTRACT | SKILL.md § References (all six linked with read-when) |
| 14 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept) |

## playbook-marketing-automation — 261 → 117 lines (gated shared ratio 17.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic input rows, Capability, Degraded, 3 generic decision rows, generic Workflow/Outputs/Evidence/Quality, 4 generic anti-patterns, "Use the directly cited sources" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows (ambiguous trigger; automation roadmap; AI agent) | KEPT | SKILL.md § Decision Rules |
| 3 | Anti-patterns "inaccessible account… native-language review" and "volatile platform details" | KEPT | SKILL.md § Anti-Patterns |
| 4 | "## Required Inputs" (8 intake questions) | MOVED + MERGED-INTO-CONTRACT | references/trigger-and-sequence-design.md § Intake questions; SKILL.md § Required Inputs |
| 5 | "## What Marketing Automation Is" | MOVED | references/trigger-and-sequence-design.md § What marketing automation is; gist in SKILL.md intro |
| 6 | "## The Four Trigger Categories" (4 tables) | MOVED | references/trigger-and-sequence-design.md § The four trigger categories |
| 7 | "## Sequence Architecture" (timing table) | MOVED | references/trigger-and-sequence-design.md § Sequence architecture; timing in SKILL.md Workflow 3 |
| 8 | "## WhatsApp Automation for EA Clients" | MOVED | references/trigger-and-sequence-design.md § WhatsApp automation; API rule also in SKILL.md § Decision Rules |
| 9 | "## Message Timing Rules" (3 rules) | MOVED | references/trigger-and-sequence-design.md § Message timing rules; all three also in SKILL.md § Decision Rules |
| 10 | "## Personalisation Tokens" (incl. Zahay et al., 2024 figure) | MOVED | references/trigger-and-sequence-design.md § Personalisation tokens |
| 11 | "## Quarterly Sequence Review" | MOVED | references/trigger-and-sequence-design.md § Quarterly sequence review |
| 12 | "## Output: Marketing Automation Brief" (6 items) | MOVED + MERGED-INTO-CONTRACT | references/trigger-and-sequence-design.md § brief format; SKILL.md § Outputs |
| 13 | "## Quality Criteria" (7 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (7 kept) |
| 14 | "## References" (Hanlon and Tuten 2022; Pidsley 2023; Zahay et al. 2024) | MOVED | references/trigger-and-sequence-design.md § Sources |
| 15 | References list links (4 items) | KEPT | SKILL.md § References (plus the two unlinked existing references) |

## playbook-networking — 228 → 121 lines (gated shared ratio 19.8 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic input rows, Capability, Degraded, 3 generic decision rows, generic Workflow/Outputs/Evidence/Quality, 6 generic anti-patterns, "Use the directly cited sources" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "no mutual relevance or permission" | KEPT | SKILL.md § Decision Rules |
| 3 | "## Required Input" (6 intake items) | MOVED + MERGED-INTO-CONTRACT | references/networking-and-referral-method.md § Intake questions; SKILL.md § Required Inputs |
| 4 | "## Part 1 — Decide Whether Networking Leads the Plan" (incl. Edwards et al., 1991) | MOVED | references/networking-and-referral-method.md § Part 1; table also in SKILL.md § Channel mix by client resources |
| 5 | "## Part 2 — Event Routine" | MOVED | references/networking-and-referral-method.md § Part 2 (links re-levelled) |
| 6 | "## Part 3 — Activating Referrals" (A, B, C routes) | MOVED | references/networking-and-referral-method.md § Part 3 |
| 7 | "## Part 4 — Designing a Referral Group" | MOVED | references/networking-and-referral-method.md § Part 4 |
| 8 | "## Part 5 — Follow-Up System" | MOVED | references/networking-and-referral-method.md § Part 5; timings also in SKILL.md § Decision Rules |
| 9 | "## Part 6 — Network Operating System and Connector Strategy" (incl. Maltz et al., 1998) | MOVED | references/networking-and-referral-method.md § Part 6; procurement and social-contact rules also in SKILL.md § Decision Rules |
| 10 | "## Part 7 — Deliverables" (7 items) | MOVED + MERGED-INTO-CONTRACT | references/networking-and-referral-method.md § Part 7; SKILL.md § Outputs |
| 11 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept) |
| 12 | "## References" (Edwards et al. 1991; Brown 2016; Maltz et al. 1998) | MOVED | references/networking-and-referral-method.md § Sources |
| 13 | References list links (reputation system, lawful prospecting) | KEPT | SKILL.md § References |

## playbook-paid-social-advertising — 181 → 119 lines (gated shared ratio 1.0 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro, Required Inputs, Workflow, Decision Rules, Quality Standards, Anti-Patterns | KEPT | SKILL.md (unchanged) |
| 2 | Outputs header "Observable acceptance condition" | CONDENSED-IN-PLACE | SKILL.md § Outputs (header "Acceptance condition"; rows unchanged) |
| 3 | "## Capability and Permission Boundaries" | CONDENSED-IN-PLACE | SKILL.md: canonical first line + every domain item (PL-01, PL-02, named operator, readable sources) |
| 4 | "## Degraded Mode" | CONDENSED-IN-PLACE | SKILL.md: canonical first sentence + discovery list and no-thresholds-from-memory rule kept |
| 5 | "## References" (6 lines) | CONDENSED-IN-PLACE | SKILL.md § References (all links kept, read-when added, new reference added) |
| 6 | "## Required Input (intake questions)" (8 items) | MOVED | references/paid-social-planning-method.md § Intake questions |
| 7 | "## Section 1 — Objective selection" | MOVED | references/paid-social-planning-method.md § Section 1 |
| 8 | "## Section 2 — Audience temperature and starting split" | MOVED | references/paid-social-planning-method.md § Section 2 |
| 9 | "## Section 3 — Budget and pacing" | MOVED | references/paid-social-planning-method.md § Section 3 |
| 10 | "## Section 4 — Click-to-WhatsApp ads (East Africa)" | MOVED | references/paid-social-planning-method.md § Section 4 |
| 11 | "## Section 5 — Monthly report structure" | MOVED | references/paid-social-planning-method.md § Section 5 |
| 12 | "## Sources" (Cooper 2019; Marshall 2024; register list) | MOVED | references/paid-social-planning-method.md § Sources |

## playbook-post-click-strategy — 428 → 127 lines (gated shared ratio 12.2 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic input rows, Capability, Degraded, 3 generic decision rows, generic Workflow/Outputs/Evidence/Quality, 6 generic anti-patterns, "Use the directly cited sources" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows (message match; conversion diagnosis) | KEPT | SKILL.md § Decision Rules |
| 3 | "## Required Input" (8 intake items) | MOVED + MERGED-INTO-CONTRACT | references/post-click-path-method.md § Intake questions; SKILL.md § Required Inputs |
| 4 | "## 1. The Post-Click Gap" (broken paths, friction factors) | MOVED | references/post-click-path-method.md § 1; broken paths also as SKILL.md § Anti-Patterns; gap definition in intro |
| 5 | "## 2. Link-in-Bio Strategy" (tools, table, caption formula, example) | MOVED | references/post-click-path-method.md § 2; two table rows also in SKILL.md § Decision Rules |
| 6 | "## 3. WhatsApp as the Primary Conversion Channel" (wa.me format, pre-filled message, 3-message sequence, Business setup) | MOVED | references/post-click-path-method.md § 3 |
| 7 | "## 4. Lead Magnet Delivery via Social" | MOVED | references/post-click-path-method.md § 4 |
| 8 | "## 5. Landing Page Principles for the EA Context" (requirements, structure, builder table with UGX 50,000/mo, USD 5/mo, USD 19/yr) | MOVED | references/post-click-path-method.md § 5 |
| 9 | "## 6. Post-Click Measurement" (UTM, WhatsApp tracking, events, report items) | MOVED | references/post-click-path-method.md § 6; 50+ enquiries/API rule also in SKILL.md § Decision Rules |
| 10 | "## 7. Platform-Specific Conversion Paths" (Instagram, Facebook, TikTok, WhatsApp Status, YouTube) | MOVED | references/post-click-path-method.md § 7; TikTok 1,000-follower rule also in SKILL.md § Decision Rules |
| 11 | "## 8. Conversion Path Audit" (audit steps, 10-item friction checklist, 7 priority fixes) | MOVED | references/post-click-path-method.md § 8; priority fixes also in SKILL.md § Priority fix order; audit in Workflow 2–3 |
| 12 | "## Quality Criteria" (8 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept) |
| 13 | References list link (conversion diagnosis) | KEPT | SKILL.md § References |

## playbook-pr-publicity — 232 → 115 lines (gated shared ratio 20.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (generic input rows, Capability, Degraded, 3 generic decision rows, generic Workflow/Outputs/Evidence/Quality, 6 generic anti-patterns, "Use the directly cited sources" line) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows (promotional story; breaking story; named outlets) | KEPT | SKILL.md § Decision Rules |
| 3 | "## Required Input" (5 intake items) | MOVED + MERGED-INTO-CONTRACT | references/publicity-kit-and-release-method.md § Intake questions; SKILL.md § Required Inputs |
| 4 | "## Part 1 — What Counts as News" | MOVED | references/publicity-kit-and-release-method.md § Part 1; filter in Workflow 2 |
| 5 | "## Part 2 — The Standard News Release" (template, rules) | MOVED | references/publicity-kit-and-release-method.md § Part 2; rules also in SKILL.md Workflow 3 and Anti-Patterns |
| 6 | "## Part 3 — The Publicity Kit" (8 components, delivery) | MOVED | references/publicity-kit-and-release-method.md § Part 3 |
| 7 | "## Part 4 — Pitching Journalists" (query letter, media-relations checklist with Hahn 2003, Pinskey 1997, Edwards et al. 1991) | MOVED | references/publicity-kit-and-release-method.md § Part 4; exclusive, deadline and follow-up rules also in SKILL.md § Decision Rules |
| 8 | "## Part 5 — Publicity Calendar" | MOVED | references/publicity-kit-and-release-method.md § Part 5 |
| 9 | "## Part 6 — Earned Media Tracking" (log, three formulas) | MOVED | references/publicity-kit-and-release-method.md § Part 6; AVE rule also in SKILL.md § Decision Rules |
| 10 | "## Quality Criteria" (7 items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (7 kept) |
| 11 | "## References" (Hahn 2003; Edwards et al. 1991; Pinskey 1997) | MOVED | references/publicity-kit-and-release-method.md § Sources |
| 12 | References list links (newsjacking, PR media integration) | KEPT | SKILL.md § References |

Checks: factcheck 0 missing (all six skills); linecheck 21 flagged → 15 scaffolding, 6 paraphrased (listed below), 0 lost; validator clean for all six skills; routecheck no CHANGED for these skills; own markdown links resolve (repo-wide pytest link test currently fails only on `docs/templates/SKILL.template.md`, not in this batch); `git diff --check` clean; gated ratio 0.0 % for all six.
Paraphrased lines: marketing-automation Quality Criteria 5 "Manual handover protocol… before the first sequence goes live" → SKILL.md § Quality Standards bullet 5; networking "Good output from this skill:" (lead-in) → SKILL.md § Quality Standards; post-click Quality Criteria 1 "Addresses the client's actual conversion gap" and 7 "Delivers a clear audit checklist" → SKILL.md § Quality Standards bullets 1 and 7; post-click "Output for this skill meets the standard when it:" (lead-in) → SKILL.md § Quality Standards; paid-social "## Required Input (intake questions)" heading → references/paid-social-planning-method.md § Intake questions.
Noticed, not changed: post-click audit step 6 says "assess it against the five-point page structure above", but the landing-page structure lists four points (headline, three benefits, social proof, single CTA); kept as written in references/post-click-path-method.md § 8. Marketing-automation WhatsApp sequence (Day 1, 3, 7, 14) runs faster than the general sequence architecture (Day 1–3, 4–7, 8–14, 15–30); both kept. Daily-operations response target for DM enquiries (purchasing enquiries within 1 hour) sits alongside post-click's "within 1 business hour"; not reconciled.

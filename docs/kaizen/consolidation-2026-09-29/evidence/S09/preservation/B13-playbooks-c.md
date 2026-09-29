# S09 preservation log — B13-playbooks-c

Worker: S09 B13 worker (Claude Opus 5.5), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. Moved blocks were copied from `git show 0e0af8a` byte for byte (text unchanged), so every sub-heading, table, template, figure and citation survives in the named reference file. Gated ratios "before" were measured with `scripts/measure_skill_scaffolding.py --root <HEAD copy>`.

## playbook-reputation-management — 370 → 129 lines (gated shared ratio 14.4 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (3 generic input rows, Capability, Degraded, 3 generic decision rows, 5-step generic workflow, generic output/evidence rows, one-paragraph Quality Standards, 6 generic anti-patterns, "Use the directly cited sources…") | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "A damaging claim is credible and unresolved" | KEPT | SKILL.md § Decision Rules row 1 |
| 3 | "## Required Input" (6 intake questions) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; text → references/reputation-audit-and-recovery-method.md § Required Input |
| 4 | "## Section 1 — Reputation Audit" (### 1.1 audit checklist, ### 1.2 score weights 50/30/20 and bands, ### 1.3 red flags) | MOVED (text unchanged) + KEPT | references/reputation-audit-and-recovery-method.md § Section 1; weights → SKILL.md § Workflow step 3; bands → SKILL.md § Score bands |
| 5 | "## Section 2 — Proactive Reputation Building" (### 2.1 review generation, ### 2.2 positive responses, ### 2.3 GBP authority, ### 2.4 content strategy, POEM, Chaffey 2024) | MOVED (text unchanged) | references/reputation-audit-and-recovery-method.md § Section 2; incentive ban and 24–48 hour timing also SKILL.md § Anti-Patterns 6 |
| 6 | "## Section 3 — Reactive Reputation Defence" (### 3.1 decision tree, ### 3.2 negative-review protocol, ### 3.3 suppression, ### 3.4 escalation, ### 3.5 do-not-do list) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | reference § Section 3; 2-hour/24-hour tree, suppression 60–120 days, legal/defamation, coordinated attack, media crisis → SKILL.md § Decision Rules rows 2, 4–7; do-not-do list (5 items) → SKILL.md § Anti-Patterns 1–5 |
| 7 | "## Section 4 — Reputation Recovery Plan" (### Week 1–2, ### Week 3–4, ### Month 2, ### Month 3) | MOVED (text unchanged) | reference § Section 4; trigger (below 3.9) → SKILL.md § Decision Rules row 3, § Workflow step 6 |
| 8 | "## Section 5 — EA-Specific Considerations" (### 5.1 Uganda DPA 2019, ### 5.2 WhatsApp channel, ### 5.3 Facebook vs Google, ### 5.4 offline word-of-mouth, ### 5.5 local press list) | MOVED (text unchanged) | reference § Section 5; DPA check → SKILL.md § Decision Rules row 8, § Required Inputs row 5 |
| 9 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |
| 10 | "## References" (crisis, listening, GBP skills; Chaffey 2024; Bodnar and Cohen 2012) | KEPT + MOVED | Skills → SKILL.md § References as links with "read when"; citations → reference § Sources |

Checks: factcheck 0 missing; linecheck 5 flagged → 4 scaffolding (generic degraded line, generic workflow step 3, generic output row, "Output produced using this skill meets the standard when it:" lead-in), 1 paraphrased, 0 lost; validator clean; routing unchanged.
Paraphrased lines: "Produces action items that are specific and assignable…" → SKILL.md § Quality Standards bullet 8.
Noticed, not changed: `## Use When` says "Uganda DPPA 2019" while the body says "Uganda DPA 2019" (both kept); "Uganda's emerging consumer protection standards" is uncited; Bodnar and Cohen (2012) is cited for "ROI formula, content ratios" that the skill does not use.

## playbook-sms-whatsapp-marketing — 336 → 119 lines (gated shared ratio 15.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "> Foundation" blockquote (account must be configured; `platform-whatsapp` covers app setup, catalogue, broadcast lists, opt-in capture, 30-day calendar) | CONDENSED-IN-PLACE | SKILL.md intro (all facts kept) |
| 2 | Generated contract prose (generic rows, Capability, Degraded, 3 generic decision rows, generic workflow, output/evidence rows, Quality paragraph, 6 generic anti-patterns, References filler) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision row "Consent, sender identity or opt-out handling is missing → Do not send" | KEPT | SKILL.md § Decision Rules row 1 |
| 4 | "## Required Input" (8 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; text → references/sms-whatsapp-campaign-method.md § Required Input |
| 5 | "## 1. Channel Comparison and Decision Framework" (table, 4-step framework) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | reference § 1; framework steps → SKILL.md § Decision Rules rows 2–5 |
| 6 | "## 2. WhatsApp Broadcast Campaign Strategy" (### Campaign Types, ### 5-Part Formula, ### 4-Week Calendar, timing rationale) | MOVED (text unchanged) | reference § 2; frequency cap → SKILL.md § Decision Rules row 6; one-CTA and opt-out rules → § Anti-Patterns 1–2 |
| 7 | "## 3. WhatsApp Automated Sequences (API)" (BSPs; ### Welcome, ### Abandoned Enquiry, ### Re-engagement) | MOVED (text unchanged) | reference § 3 |
| 8 | "## 4. WhatsApp Catalogue Marketing" (fields, sharing, seasonal table, metrics) | MOVED (text unchanged) | reference § 4 |
| 9 | "## 5. SMS Marketing Campaign Strategy" (Africa's Talking, sender ID, ### SMS Message Templates, ### SMS Writing Rules) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | reference § 5; 160-character rule → SKILL.md § Decision Rules row 8; writing rules → § Anti-Patterns 3–5 |
| 10 | "## 6. Opt-in and Opt-out Management" (legal foundation, opt-in table, opt-out steps, list hygiene) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | reference § 6; opt-out steps → SKILL.md § Decision Rules row 7, § Anti-Patterns 6, § Evidence Produced row 1 |
| 11 | "## 7. Campaign Performance Metrics" (### WhatsApp Metrics, ### SMS Metrics, ### Monthly Reporting Template) | MOVED (text unchanged) | reference § 7; report fields → SKILL.md § Evidence Produced row 3 |
| 12 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |
| 13 | "## References" (anti-ai-slop, east-african-english) | KEPT | SKILL.md § References with "read when" |

Checks: factcheck 0 missing; linecheck 4 flagged → 3 scaffolding, 1 paraphrased, 0 lost; validator clean; routing unchanged.
Paraphrased lines: "References `platform-whatsapp` explicitly as the setup foundation and does not duplicate…" → SKILL.md § Quality Standards bullet 7.
Noticed, not changed: WhatsApp delivery rate is defined as "Sent ÷ delivered" while SMS uses "Delivered ÷ sent × 100" (the WhatsApp formula looks inverted); "Twilio has EA-specific pricing" and the WhatsApp Status "swipe-up link" are unverified platform claims; `## Do Not Use When` says "Uganda DPPA 2019" while the body spells out "Data Protection and Privacy Act 2019" (consistent in substance).

## playbook-social-media-policy — 292 → 117 lines (gated shared ratio 20.9 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "> Consultant note" (not legal advice; counsel review; Computer Misuse Act 2011 after 17 March 2026 ruling; UG-CMA-2022-VOID-2026; ULII; EA sector regulations) | KEPT (verbatim) | SKILL.md § Legal standing of the template; also § Decision Rules row 3, § Evidence Produced row 1 |
| 2 | Generated contract prose (generic rows, Capability, Degraded, 3 generic decision rows, generic workflow, output/evidence rows, Quality paragraph, 6 generic anti-patterns, References filler) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows "clause depends on law…" and "No one owns a high-risk account… governance reference" | KEPT | SKILL.md § Decision Rules rows 1–2 |
| 4 | "## Required Input" (6 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; text → references/staff-policy-template.md § Required Input |
| 5 | "## [COMPANY NAME] SOCIAL MEDIA POLICY" header block and "## 1. Purpose and Scope" (### Purpose, ### Who This Policy Applies To, ### What This Policy Covers) | MOVED (text unchanged) | references/staff-policy-template.md; lawful-opinion limit also SKILL.md § Anti-Patterns 3 |
| 6 | "## 2. Encouraged Behaviours" | MOVED (text unchanged) | references/staff-policy-template.md § 2 |
| 7 | "## 3. Prohibited Activities" (8 ### subsections) | MOVED (text unchanged) | references/staff-policy-template.md § 3; also SKILL.md § Anti-Patterns 2 |
| 8 | "## 4. Handling Customer Enquiries via Personal Channels" (5 steps, boundary rule) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | reference § 4; SKILL.md § Decision Rules row 5, § Anti-Patterns 4 |
| 9 | "## 5. Disclosure Requirements" (KE-01, UG-01, TZ-01 register, 2026-09-24; examples; false-review ban) | MOVED (text unchanged apart from one `../` added to the backticked 08-influencer path) + MERGED | reference § 5; SKILL.md § Decision Rules row 4, § Anti-Patterns 5, § References (register link) |
| 10 | "## 6. Approval Process for Employee-Generated Content" (24/48 hours) | MOVED (text unchanged) | reference § 6; SKILL.md § Decision Rules row 6 |
| 11 | "## 7. Consequences of Policy Violations" (severity table) | MOVED (text unchanged) | reference § 7; SKILL.md § Decision Rules row 7, § Anti-Patterns 6 |
| 12 | "## 8. Policy Review" and "## Employee Acknowledgement" | MOVED (text unchanged) | reference § 8 and § Employee Acknowledgement; SKILL.md § Outputs row 2 |
| 13 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |
| 14 | "## References" (anti-ai-slop, east-african-english, governance reference) | KEPT | SKILL.md § References with "read when" |
| 15 | Existing references/governance-roles-access-and-approvals.md cites "parent § 5" and "§ 8" | EXTENDED (appended pointer section; no existing text changed) | governance reference § Where the parent section numbers now live |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding (3 generic contract lines, "Output meets production standard when it satisfies all of the following:" lead-in), 0 paraphrased, 0 lost; validator clean; routing unchanged.
Noticed, not changed: "in many jurisdictions, constitutes consumer fraud" (false reviews) is uncited; the governance reference cites a second register (UG-CMA-SECTIONS-STRUCK-2026) that SKILL.md does not, which is consistent rather than conflicting.

## playbook-social-selling — 494 → 130 lines (gated shared ratio 10.2 % → 0.0 %)

S06 hand-off honoured: all procedures moved to references.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "> The core problem this playbook solves" blockquote | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | Kennedy market-message-offer / Wiebe voice-of-customer paragraph (4 bullets) | KEPT (verbatim) | SKILL.md § Market, message and offer discipline |
| 3 | Generated contract prose (generic rows, Capability, Degraded, 3 generic decision rows, generic workflow, output/evidence rows, Quality paragraph, 6 generic anti-patterns, References filler) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 4 | Decision rows (no relevant need → stop; staff sharing → advocacy reference; senior/high-ticket → high-value reference) | KEPT | SKILL.md § Decision Rules rows 1–3 |
| 5 | "## Required Input" (10 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; text → references/social-selling-sequence-and-scripts.md § Required Input |
| 6 | "## 1. The Authority-First Model" (Trust Ladder, authority markers, 80/20) | MOVED (text unchanged) | references/social-selling-sequence-and-scripts.md § 1; 80/20 → SKILL.md § Workflow step 3 |
| 7 | "## 2. Platform Selection Logic" (table; two-platform rule) | MOVED (text unchanged) | reference § 2; SKILL.md § Workflow step 2 |
| 8 | "## 3. The 5-Step Social Selling Sequence" (### Steps 1–5, wa.me format, real-urgency rule) | MOVED (text unchanged) | reference § 3; SKILL.md § Decision Rules rows 4–6, § Outputs row 1 |
| 9 | "## 4. Soft CTA Techniques in Detail" | MOVED (text unchanged) | reference § 4 |
| 10 | "## 5. Handling Enquiries and DMs" (script, qualifying questions, VOC banks, objection table) | MOVED (text unchanged) | reference § 5; VOC banks → SKILL.md § Evidence Produced row 2 |
| 11 | "## 6. Social Proof Mechanics" | MOVED (text unchanged) | reference § 6; permission → SKILL.md § Evidence Produced row 1 |
| 12 | "## 7. Conversion Rate Benchmarks" (table, 15–35 %) | MOVED (text unchanged) | reference § 7; SKILL.md § Decision Rules row 7, § Evidence Produced row 3 |
| 13 | "## 8. WhatsApp Conversion Path" (3 messages, etiquette) | MOVED (text unchanged) | reference § 8; two-follow-up limit → SKILL.md § Decision Rules row 8 |
| 14 | "## 9. What NOT to Do" (8 items) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | reference § 9 (all 8); SKILL.md § Anti-Patterns 1–7 (the "skip to hard CTA" item → § Decision Rules row 4) |
| 15 | "## 10. LinkedIn Outreach Message Sequence" (4 messages, 15 trigger events; Dodaro 2019, Shanks 2016) | MOVED (text unchanged) | references/linkedin-outreach-and-daily-routine.md § 10 |
| 16 | "## 11. Daily Social Selling Routine" (FEED, Boolean search, Law of Familiarity; Blount 2015, Dodaro 2019, Shanks 2016 citations) | MOVED (text unchanged) | references/linkedin-outreach-and-daily-routine.md § 11 |
| 17 | "## Quality Criteria" (8 numbered items) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |
| 18 | "## References" (anti-ai-slop, east-african-english, 3 existing references) | KEPT | SKILL.md § References with "read when" |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding, 0 paraphrased, 0 lost; validator clean; routing unchanged.
Noticed, not changed: Kennedy and Wiebe are named without a cited work; the benchmark table and the "20–40 DMs" claim are unsourced; Jill Rowley's "every deal, every day" is a secondary citation via Shanks (2016).

## playbook-viral-content-design — 399 → 118 lines (gated shared ratio 12.4 % → 0.0 %)

Duplicate `## References` resolved: the generated block and the domain block are merged into one SKILL.md § References; every link kept (anti-ai-slop, east-african-english, bold-idea-risk-screen, and the four backticked skills now as live links); the academic citations moved to the new reference § Sources.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro (two paragraphs: structured not accidental; earned reach; paid outside; POEM, Chaffey 2024) | CONDENSED-IN-PLACE | SKILL.md intro (all facts kept) |
| 2 | Generated contract prose (generic rows, Capability, Degraded, 3 generic decision rows, generic workflow, output/evidence rows, Quality paragraph, 6 generic anti-patterns) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows (deception/outrage → reject; bold brief → risk screen) | KEPT | SKILL.md § Decision Rules rows 1–2 |
| 4 | First "## References" (generated: anti-ai-slop, east-african-english, filler line) | MERGED-INTO-CONTRACT | SKILL.md § References (single section) |
| 5 | "## Required Input" (7 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; text → references/viral-structures-and-platform-method.md § Required Input |
| 6 | "## Section 1 — What Makes Content Spread" (sharer benefit, emotions, utility, Hero/Hub/Hygiene, Bodnar and Cohen 2012) | MOVED (text unchanged) | reference § Section 1; SKILL.md § Workflow step 2 |
| 7 | "## Section 2 — The Six Viral Content Structures" (### 1–6 with formula, template, EA example) | MOVED (text unchanged) | reference § Section 2; one-structure rule → SKILL.md § Decision Rules row 3; hot-take rule → row 4 |
| 8 | "## Section 3 — Platform-Specific Virality" (### TikTok, ### Facebook, ### Instagram Reels, ### WhatsApp) | MOVED (text unchanged) + MERGED | reference § Section 3; SKILL.md § Decision Rules rows 6–7, § Anti-Patterns 3–7 |
| 9 | "## Section 4 — Content Brief for Viral Design" (template) | MOVED (text unchanged) | reference § Section 4; SKILL.md § Workflow step 4, § Outputs row 1 |
| 10 | "## Section 5 — EA-Specific Viral Triggers" | MOVED (text unchanged) | reference § Section 5; exposé verification → SKILL.md § Decision Rules row 5 |
| 11 | "## Section 6 — Ethical Boundaries" (4 items) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | reference § Section 6; SKILL.md § Decision Rules rows 4, 5, 8, § Anti-Patterns 1–2, § Evidence Produced rows 1–2 |
| 12 | "## Quality Criteria" (7 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 7) |
| 13 | Second "## References" (11-content-calendar, caption-writer, platform-tiktok, meta-testing-framework, bold-idea-risk-screen; Bodnar and Cohen 2012, Chaffey 2024, Kotler et al. 2023) | MERGED-INTO-CONTRACT + MOVED | Skills → SKILL.md § References as links; citations → reference § Sources |
| 14 | Existing references/bold-idea-risk-screen.md cites parent Sections 1, 4, 5 and 6 | EXTENDED (appended pointer section; no existing text changed) | bold-idea-risk-screen.md § Where the parent section numbers now live |

Checks: factcheck 0 missing; linecheck 5 flagged → 4 scaffolding (3 generic contract lines, "Good output from this skill meets all of the following standards:" lead-in), 1 paraphrased, 0 lost; validator clean; routing unchanged.
Paraphrased lines: "Read these skills before producing platform-specific output or integrating this playbook…" → SKILL.md § References "read when" lines.
Noticed, not changed: the Hero/Hub/Hygiene model is attributed to Bodnar and Cohen (2012), an attribution worth checking; Kotler et al. (2023) is listed but not used in the body; "Facebook Pages are dying in Uganda" is an example hot take, not a verified claim.

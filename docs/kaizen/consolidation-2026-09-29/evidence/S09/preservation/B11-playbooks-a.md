# S09 preservation log — B11-playbooks-a

Worker: S09 worker agent (Claude Opus 5.5), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10.

Move method: domain sections after `<!-- dual-compat-end -->` were copied line-for-line from `git show 0e0af8a:<path>` into the new reference (horizontal rules dropped; relative links re-based one level: `references/x.md` → `x.md`, `../` → `../../`). New SKILL.md contract sections were written from the domain content.

## playbook-agency-operations — 451 → 119 lines (gated shared ratio 10.1 % → 0.0 %)

New reference files: references/agency-operating-procedures.md (new), references/ai-revenue-and-seven-figure-model.md (new). Existing reference files unchanged.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Use When" (HEAD line 13) | KEPT | SKILL.md § Use When (byte-identical) |
| 2 | "## Do Not Use When" (HEAD line 20) | KEPT | SKILL.md § Do Not Use When (byte-identical) |
| 3 | "## Required Inputs" (HEAD line 26) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Required Inputs (3 generic rows replaced by domain rows folded from "Required Input") |
| 4 | "## Capability and Permission Boundaries" (HEAD line 33) | REPLACED-BY-CANONICAL | SKILL.md § Capability and Permission Boundaries (canonical sentence + one domain sentence) |
| 5 | "## Degraded Mode" (HEAD line 36) | REPLACED-BY-CANONICAL | SKILL.md § Degraded Mode |
| 6 | "## Decision Rules" (HEAD line 39) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules (every domain row kept; 3 generic rows (inputs complete / evidence incomplete / action needs approval) replaced by domain rows) |
| 7 | "## Workflow" (HEAD line 48) | REPLACED-BY-CANONICAL / domain steps | SKILL.md § Workflow (generic 5 steps replaced by 7 domain steps with stop and rerun) |
| 8 | "## Outputs" (HEAD line 55) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Outputs |
| 9 | "## Evidence Produced" (HEAD line 61) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Evidence Produced |
| 10 | "## Quality Standards" (HEAD line 67) | REPLACED-BY-CANONICAL | SKILL.md § Quality Standards (generic paragraph replaced by domain checks from Quality Criteria) |
| 11 | "## Anti-Patterns" (HEAD line 70) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Anti-Patterns (6 generic bullets replaced by domain bullets with Fix:) |
| 12 | "## References" (HEAD line 78) | MERGED-INTO-CONTRACT | SKILL.md § References (every link kept, each with "read when"; generic "Use the directly cited sources…" line removed) |
| 13 | "## Required Input" (HEAD line 84) | MOVED + MERGED-INTO-CONTRACT | references/agency-operating-procedures.md § Required Input (verbatim); SKILL.md § Required Inputs rows |
| 14 | "## Section 1 — Client Onboarding Checklist" (HEAD line 99) | MOVED | references/agency-operating-procedures.md § Section 1 — Client Onboarding Checklist |
| 15 | "### Day 1–3: Foundations" (HEAD line 103) | MOVED | references/agency-operating-procedures.md § Day 1–3: Foundations |
| 16 | "### Day 4–7: Communication Setup" (HEAD line 112) | MOVED | references/agency-operating-procedures.md § Day 4–7: Communication Setup |
| 17 | "### Day 8–14: Strategy and Planning" (HEAD line 122) | MOVED | references/agency-operating-procedures.md § Day 8–14: Strategy and Planning |
| 18 | "### Day 15–30: First Publishing Cycle" (HEAD line 129) | MOVED | references/agency-operating-procedures.md § Day 15–30: First Publishing Cycle |
| 19 | "## Section 2 — Retainer Structure" (HEAD line 138) | MOVED | references/agency-operating-procedures.md § Section 2 — Retainer Structure |
| 20 | "### Billing Protocol" (HEAD line 151) | MOVED | references/agency-operating-procedures.md § Billing Protocol |
| 21 | "### Contract Essentials" (HEAD line 158) | MOVED | references/agency-operating-procedures.md § Contract Essentials |
| 22 | "## Section 3 — Project Management System" (HEAD line 172) | MOVED | references/agency-operating-procedures.md § Section 3 — Project Management System |
| 23 | "### Tool Selection by Team Size" (HEAD line 174) | MOVED | references/agency-operating-procedures.md § Tool Selection by Team Size |
| 24 | "### Weekly Workflow Template" (HEAD line 182) | MOVED | references/agency-operating-procedures.md § Weekly Workflow Template |
| 25 | "### Content Approval Protocol" (HEAD line 194) | MOVED | references/agency-operating-procedures.md § Content Approval Protocol |
| 26 | "## Section 4 — Invoicing and Cash Flow" (HEAD line 203) | MOVED | references/agency-operating-procedures.md § Section 4 — Invoicing and Cash Flow |
| 27 | "### Recommended Invoicing Tools" (HEAD line 205) | MOVED | references/agency-operating-procedures.md § Recommended Invoicing Tools |
| 28 | "### Invoice Contents (Mandatory)" (HEAD line 211) | MOVED | references/agency-operating-procedures.md § Invoice Contents (Mandatory) |
| 29 | "### Cash Flow Rules" (HEAD line 225) | MOVED | references/agency-operating-procedures.md § Cash Flow Rules |
| 30 | "### Tax Obligations (check, do not assume)" (HEAD line 235) | MOVED | references/agency-operating-procedures.md § Tax Obligations (check, do not assume) |
| 31 | "## Section 5 — Quality Control Checklist" (HEAD line 244) | MOVED | references/agency-operating-procedures.md § Section 5 — Quality Control Checklist |
| 32 | "## Section 6 — Client Reporting Rhythm" (HEAD line 260) | MOVED | references/agency-operating-procedures.md § Section 6 — Client Reporting Rhythm |
| 33 | "### Reporting Standards" (HEAD line 271) | MOVED | references/agency-operating-procedures.md § Reporting Standards |
| 34 | "## Section 7 — Team Management (2–10 People)" (HEAD line 280) | MOVED | references/agency-operating-procedures.md § Section 7 — Team Management (2–10 People) |
| 35 | "### Role Definitions (Minimum Viable Team)" (HEAD line 284) | MOVED | references/agency-operating-procedures.md § Role Definitions (Minimum Viable Team) |
| 36 | "### Delegation Rules" (HEAD line 293) | MOVED | references/agency-operating-procedures.md § Delegation Rules |
| 37 | "### Performance Standards" (HEAD line 300) | MOVED | references/agency-operating-procedures.md § Performance Standards |
| 38 | "## Section 8 — AI Revenue Models: Database Reactivation and Android Upsell Stack" (HEAD line 310) | MOVED | references/ai-revenue-and-seven-figure-model.md § Section 8 — AI Revenue Models: Database Reactivation and Android Upsell Stack |
| 39 | "### The Database Reactivation (DBR) Model" (HEAD line 314) | MOVED | references/ai-revenue-and-seven-figure-model.md § The Database Reactivation (DBR) Model |
| 40 | "### AI Upsell Stack (Escalation Sequence)" (HEAD line 335) | MOVED | references/ai-revenue-and-seven-figure-model.md § AI Upsell Stack (Escalation Sequence) |
| 41 | "### Deal Structures (Wardrope, 2024)" (HEAD line 345) | MOVED | references/ai-revenue-and-seven-figure-model.md § Deal Structures (Wardrope, 2024) |
| 42 | "### 5 Selling Principles (Wardrope, 2024)" (HEAD line 359) | MOVED | references/ai-revenue-and-seven-figure-model.md § 5 Selling Principles (Wardrope, 2024) |
| 43 | "## Section 9 — Seven-Figure Agency Model: Growth, Retention and Scale" (HEAD line 371) | MOVED | references/ai-revenue-and-seven-figure-model.md § Section 9 — Seven-Figure Agency Model: Growth, Retention and Scale |
| 44 | "### Rule of Five Ones (Nelson, 2019, credited by him to Taki Moore and Clay Collins)" (HEAD line 375) | MOVED | references/ai-revenue-and-seven-figure-model.md § Rule of Five Ones (Nelson, 2019, credited by him to Taki Moore and Clay Collins) |
| 45 | "### Client Retention — Kickoff, Rhythm, Seed the Vision (Nelson, 2019)" (HEAD line 387) | MOVED | references/ai-revenue-and-seven-figure-model.md § Client Retention — Kickoff, Rhythm, Seed the Vision (Nelson, 2019) |
| 46 | "### Organisational Structure" (HEAD line 399) | MOVED | references/ai-revenue-and-seven-figure-model.md § Organisational Structure |
| 47 | "### Agency Value Proposition in the AI Era (Vallaeys, 2019)" (HEAD line 411) | MOVED | references/ai-revenue-and-seven-figure-model.md § Agency Value Proposition in the AI Era (Vallaeys, 2019) |
| 48 | "## Quality Criteria" (HEAD line 423) | MOVED + MERGED-INTO-CONTRACT | references/agency-operating-procedures.md § Quality Criteria (verbatim); SKILL.md § Quality Standards |
| 49 | "## References" (HEAD line 440) | MERGED-INTO-CONTRACT | SKILL.md § References (every link kept, each with "read when"; generic "Use the directly cited sources…" line removed) |

Quality criteria: Quality Criteria (10 bullets) → 7 folded into SKILL.md § Quality Standards; all 10 kept verbatim in references/agency-operating-procedures.md § Quality Criteria. S07 hand-off met: 451 → 119 lines, all procedures moved to references.

Checks: factcheck 0 missing; linecheck 4 flagged → 3 scaffolding (generic Degraded Mode sentence, generic Workflow step 3, generic Outputs row), 1 paraphrased, 0 lost; validator clean; routecheck unchanged; gated ratio 0.0 %; all local links resolve.
Paraphrased lines: "Link to these related skills when producing output. Read the linked skill before cross-referencing…" (References intro) → SKILL.md § References "read when" clauses.
Noticed, not changed: (1) references/white-label-and-partner-delivery.md line 125 says "parent § Section 5"; Section 5 (QC checklist) now lives in references/agency-operating-procedures.md; pointer not edited. (2) Retainer tier prices, the UGX 30,000 revision fee, the 1.5%/month late-payment rate and the 15% month-to-month premium carry no register ID. (3) The Vallaeys (2019) quotation uses "leverage"; kept verbatim as a quotation. (4) "Chunky Retainer" figure "$5K–$25K equivalent" is USD, sourced only to Wardrope (2024). (5) CRR: Nelson reports about 97% and 5–8% attrition; engine policy 95% target / 90% floor; both kept as labelled.

## playbook-chatbot-strategy — 302 → 112 lines (gated shared ratio 16.1 % → 0.0 %)

New reference files: references/chatbot-build-guide.md (new). Existing reference files unchanged.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Use When" (HEAD line 13) | KEPT | SKILL.md § Use When (byte-identical) |
| 2 | "## Do Not Use When" (HEAD line 20) | KEPT | SKILL.md § Do Not Use When (byte-identical) |
| 3 | "## Required Inputs" (HEAD line 26) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Required Inputs (3 generic rows replaced by domain rows folded from "Required Input") |
| 4 | "## Capability and Permission Boundaries" (HEAD line 33) | REPLACED-BY-CANONICAL | SKILL.md § Capability and Permission Boundaries (canonical sentence + one domain sentence) |
| 5 | "## Degraded Mode" (HEAD line 36) | REPLACED-BY-CANONICAL | SKILL.md § Degraded Mode |
| 6 | "## Decision Rules" (HEAD line 39) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules (every domain row kept; 3 generic rows (inputs complete / evidence incomplete / action needs approval) replaced by domain rows) |
| 7 | "## Workflow" (HEAD line 48) | REPLACED-BY-CANONICAL / domain steps | SKILL.md § Workflow (generic 5 steps replaced by 7 domain steps with stop and rerun) |
| 8 | "## Outputs" (HEAD line 55) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Outputs |
| 9 | "## Evidence Produced" (HEAD line 61) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Evidence Produced |
| 10 | "## Quality Standards" (HEAD line 67) | REPLACED-BY-CANONICAL | SKILL.md § Quality Standards (generic paragraph replaced by domain checks from Quality Criteria) |
| 11 | "## Anti-Patterns" (HEAD line 70) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Anti-Patterns (6 generic bullets replaced by domain bullets with Fix:) |
| 12 | "## References" (HEAD line 78) | MERGED-INTO-CONTRACT | SKILL.md § References (every link kept, each with "read when"; generic "Use the directly cited sources…" line removed) |
| 13 | "## Required Input" (HEAD line 85) | MOVED + MERGED-INTO-CONTRACT | references/chatbot-build-guide.md § Required Input (verbatim); SKILL.md § Required Inputs rows |
| 14 | "## Section 1 — Do You Need a Chatbot?" (HEAD line 99) | MOVED | references/chatbot-build-guide.md § Section 1 — Do You Need a Chatbot? |
| 15 | "### Decision Threshold" (HEAD line 103) | MOVED | references/chatbot-build-guide.md § Decision Threshold |
| 16 | "### When Automation Makes Sense" (HEAD line 108) | MOVED | references/chatbot-build-guide.md § When Automation Makes Sense |
| 17 | "### When a Human Is Better" (HEAD line 115) | MOVED | references/chatbot-build-guide.md § When a Human Is Better |
| 18 | "### Warning" (HEAD line 122) | MOVED | references/chatbot-build-guide.md § Warning |
| 19 | "### Minimum Viable Alternative" (HEAD line 126) | MOVED | references/chatbot-build-guide.md § Minimum Viable Alternative |
| 20 | "## Section 2 — Platform Automation Options" (HEAD line 132) | MOVED | references/chatbot-build-guide.md § Section 2 — Platform Automation Options |
| 21 | "### Facebook Messenger" (HEAD line 136) | MOVED | references/chatbot-build-guide.md § Facebook Messenger |
| 22 | "### Instagram DMs" (HEAD line 149) | MOVED | references/chatbot-build-guide.md § Instagram DMs |
| 23 | "### WhatsApp Business" (HEAD line 160) | MOVED | references/chatbot-build-guide.md § WhatsApp Business |
| 24 | "## Section 3 — Flow Design" (HEAD line 175) | MOVED | references/chatbot-build-guide.md § Section 3 — Flow Design |
| 25 | "### Step 1 — Map the Conversation Tree" (HEAD line 179) | MOVED | references/chatbot-build-guide.md § Step 1 — Map the Conversation Tree |
| 26 | "### Step 2 — Write the Welcome Message" (HEAD line 195) | MOVED | references/chatbot-build-guide.md § Step 2 — Write the Welcome Message |
| 27 | "### Step 3 — Write FAQ Responses" (HEAD line 211) | MOVED | references/chatbot-build-guide.md § Step 3 — Write FAQ Responses |
| 28 | "### Step 4 — Design the Human Handoff Trigger" (HEAD line 220) | MOVED | references/chatbot-build-guide.md § Step 4 — Design the Human Handoff Trigger |
| 29 | "## Section 4 — ManyChat Setup Guide (Free Tier, Facebook Messenger)" (HEAD line 228) | MOVED | references/chatbot-build-guide.md § Section 4 — ManyChat Setup Guide (Free Tier, Facebook Messenger) |
| 30 | "## Section 5 — WhatsApp Business Quick Wins (No Budget)" (HEAD line 242) | MOVED | references/chatbot-build-guide.md § Section 5 — WhatsApp Business Quick Wins (No Budget) |
| 31 | "## Section 6 — Quality Control Checklist" (HEAD line 255) | MOVED | references/chatbot-build-guide.md § Section 6 — Quality Control Checklist |
| 32 | "## EA-Specific Considerations" (HEAD line 269) | MOVED | references/chatbot-build-guide.md § EA-Specific Considerations |
| 33 | "## Quality Criteria" (HEAD line 282) | MOVED + MERGED-INTO-CONTRACT | references/chatbot-build-guide.md § Quality Criteria (verbatim); SKILL.md § Quality Standards |
| 34 | "## References" (HEAD line 296) | MERGED-INTO-CONTRACT | SKILL.md § References (every link kept, each with "read when"; generic "Use the directly cited sources…" line removed) |

Quality criteria: Quality Criteria (7 bullets) → all 7 folded into SKILL.md § Quality Standards; kept verbatim in the guide.

Checks: factcheck 0 missing; linecheck 4 flagged → 3 scaffolding (generic Degraded Mode sentence, generic Workflow step 3, generic Outputs row), 1 paraphrased, 0 lost; validator clean; routecheck unchanged; gated ratio 0.0 %; all local links resolve.
Paraphrased lines: "Consult these related skills when building the full client engagement:" → SKILL.md § References (the three skills now linked with "read when").
Noticed, not changed: (1) references/whatsapp-chatbot-design.md refers to "the playbook's Section 1/2/3"; those sections now live in references/chatbot-build-guide.md; pointer not edited. (2) ManyChat Pro approx. USD 15/month, ManyChat free tier 1,000 contacts, Business API approval 2–4 weeks, up to four Instagram FAQ buttons, up to 50 WhatsApp quick replies and the 256-character description are unregistered platform facts. (3) Africa's Talking is called "Uganda-based" in Section 2 but given "a local support team in Nairobi and Kampala" in the EA considerations; both kept.

## playbook-client-retainer-management — 359 → 115 lines (gated shared ratio 12.2 % → 0.0 %)

New reference files: references/retainer-operating-procedures.md (new). Existing reference files unchanged.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Use When" (HEAD line 23) | KEPT | SKILL.md § Use When (byte-identical) |
| 2 | "## Do Not Use When" (HEAD line 30) | KEPT | SKILL.md § Do Not Use When (byte-identical) |
| 3 | "## Required Inputs" (HEAD line 36) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Required Inputs (3 generic rows replaced by domain rows folded from "Required Input") |
| 4 | "## Capability and Permission Boundaries" (HEAD line 43) | REPLACED-BY-CANONICAL | SKILL.md § Capability and Permission Boundaries (canonical sentence + one domain sentence) |
| 5 | "## Degraded Mode" (HEAD line 46) | REPLACED-BY-CANONICAL | SKILL.md § Degraded Mode |
| 6 | "## Decision Rules" (HEAD line 49) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules (every domain row kept; 3 generic rows (inputs complete / evidence incomplete / action needs approval) replaced by domain rows) |
| 7 | "## Workflow" (HEAD line 57) | REPLACED-BY-CANONICAL / domain steps | SKILL.md § Workflow (generic 5 steps replaced by 7 domain steps with stop and rerun) |
| 8 | "## Outputs" (HEAD line 64) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Outputs |
| 9 | "## Evidence Produced" (HEAD line 70) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Evidence Produced |
| 10 | "## Quality Standards" (HEAD line 76) | REPLACED-BY-CANONICAL | SKILL.md § Quality Standards (generic paragraph replaced by domain checks from Quality Criteria) |
| 11 | "## Anti-Patterns" (HEAD line 79) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Anti-Patterns (6 generic bullets replaced by domain bullets with Fix:) |
| 12 | "## References" (HEAD line 87) | MERGED-INTO-CONTRACT | SKILL.md § References (every link kept, each with "read when"; generic "Use the directly cited sources…" line removed) |
| 13 | "## Required Input" (HEAD line 95) | MOVED + MERGED-INTO-CONTRACT | references/retainer-operating-procedures.md § Required Input (verbatim); SKILL.md § Required Inputs rows |
| 14 | "## Section 1: Defining Scope Before Work Begins" (HEAD line 112) | MOVED | references/retainer-operating-procedures.md § Section 1: Defining Scope Before Work Begins |
| 15 | "### 1. Deliverables List" (HEAD line 119) | MOVED | references/retainer-operating-procedures.md § 1. Deliverables List |
| 16 | "### 2. Platform List" (HEAD line 126) | MOVED | references/retainer-operating-procedures.md § 2. Platform List |
| 17 | "### 3. Revision Rounds" (HEAD line 130) | MOVED | references/retainer-operating-procedures.md § 3. Revision Rounds |
| 18 | "### 4. Response Time" (HEAD line 134) | MOVED | references/retainer-operating-procedures.md § 4. Response Time |
| 19 | "### 5. Approval Process" (HEAD line 139) | MOVED | references/retainer-operating-procedures.md § 5. Approval Process |
| 20 | "### 6. Exclusions" (HEAD line 145) | MOVED | references/retainer-operating-procedures.md § 6. Exclusions |
| 21 | "## Section 2: Scope Creep Recognition" (HEAD line 156) | MOVED | references/retainer-operating-procedures.md § Section 2: Scope Creep Recognition |
| 22 | "## Section 3: Change Request Protocol" (HEAD line 184) | MOVED | references/retainer-operating-procedures.md § Section 3: Change Request Protocol |
| 23 | "### Step 1: Acknowledge the request positively" (HEAD line 190) | MOVED | references/retainer-operating-procedures.md § Step 1: Acknowledge the request positively |
| 24 | "### Step 2: Never say the following" (HEAD line 200) | MOVED | references/retainer-operating-procedures.md § Step 2: Never say the following |
| 25 | "### Step 3: Document every approved change request in writing" (HEAD line 206) | MOVED | references/retainer-operating-procedures.md § Step 3: Document every approved change request in writing |
| 26 | "## Section 4: Monthly Check-In Structure" (HEAD line 220) | MOVED | references/retainer-operating-procedures.md § Section 4: Monthly Check-In Structure |
| 27 | "## Section 5: Performance Review Triggers" (HEAD line 244) | MOVED | references/retainer-operating-procedures.md § Section 5: Performance Review Triggers |
| 28 | "## Section 6: Retainer Renewal" (HEAD line 270) | MOVED | references/retainer-operating-procedures.md § Section 6: Retainer Renewal |
| 29 | "### Renewal Preparation (4 Weeks Before End Date)" (HEAD line 275) | MOVED | references/retainer-operating-procedures.md § Renewal Preparation (4 Weeks Before End Date) |
| 30 | "### Pricing at Renewal" (HEAD line 293) | MOVED | references/retainer-operating-procedures.md § Pricing at Renewal |
| 31 | "### Value-First Renewal Negotiation" (HEAD line 306) | MOVED | references/retainer-operating-procedures.md § Value-First Renewal Negotiation |
| 32 | "### Renewal Conversation Script" (HEAD line 310) | MOVED | references/retainer-operating-procedures.md § Renewal Conversation Script |
| 33 | "### If the Client Does Not Renew" (HEAD line 319) | MOVED | references/retainer-operating-procedures.md § If the Client Does Not Renew |
| 34 | "## Quality Criteria" (HEAD line 341) | MOVED + MERGED-INTO-CONTRACT | references/retainer-operating-procedures.md § Quality Criteria (verbatim); SKILL.md § Quality Standards |

Quality criteria: Quality Criteria (9 bullets) → 7 in SKILL.md § Quality Standards (the last bullet points to the full list); all 9 kept verbatim in the procedures reference.

Checks: factcheck 0 missing; linecheck 4 flagged → 3 scaffolding (generic Degraded Mode sentence, generic Workflow step 3, generic Outputs row), 1 paraphrased, 0 lost; validator clean; routecheck unchanged; gated ratio 0.0 %; all local links resolve.
Paraphrased lines: Intro "A practical operating guide for managing retainer-based client relationships…" (three causes of retainer loss) → SKILL.md intro; "**Cross-reference:**" line (biz-dev-proposal, playbook-agency-operations, playbook-daily-operations-routine) → SKILL.md § References.
Noticed, not changed: (1) Approval window: this skill recommends 24 hours with a publish-after-silence default; playbook-agency-operations uses a 48-hour approval rule; both kept in their skills. (2) Sample change-request fees (UGX 350,000/month; UGX 80,000 one-off) are illustrative log rows without a source.

## playbook-community-management — 260 → 120 lines (gated shared ratio 18.8 % → 1.6 %)

New reference files: references/community-response-guide.md (new). Existing reference files unchanged.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Use When" (HEAD line 13) | KEPT | SKILL.md § Use When (byte-identical) |
| 2 | "## Do Not Use When" (HEAD line 20) | KEPT | SKILL.md § Do Not Use When (byte-identical) |
| 3 | "## Required Inputs" (HEAD line 26) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Required Inputs (3 generic rows replaced by domain rows folded from "Required Input") |
| 4 | "## Capability and Permission Boundaries" (HEAD line 33) | REPLACED-BY-CANONICAL | SKILL.md § Capability and Permission Boundaries (canonical sentence + one domain sentence) |
| 5 | "## Degraded Mode" (HEAD line 36) | REPLACED-BY-CANONICAL | SKILL.md § Degraded Mode |
| 6 | "## Decision Rules" (HEAD line 39) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules (every domain row kept; 3 generic rows (inputs complete / evidence incomplete / action needs approval) replaced by domain rows) |
| 7 | "## Workflow" (HEAD line 50) | REPLACED-BY-CANONICAL / domain steps | SKILL.md § Workflow (generic 5 steps replaced by 7 domain steps with stop and rerun) |
| 8 | "## Outputs" (HEAD line 57) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Outputs |
| 9 | "## Evidence Produced" (HEAD line 63) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Evidence Produced |
| 10 | "## Quality Standards" (HEAD line 69) | REPLACED-BY-CANONICAL | SKILL.md § Quality Standards (generic paragraph replaced by domain checks from Quality Criteria) |
| 11 | "## Anti-Patterns" (HEAD line 72) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Anti-Patterns (6 generic bullets replaced by domain bullets with Fix:) |
| 12 | "## References" (HEAD line 80) | MERGED-INTO-CONTRACT | SKILL.md § References (every link kept, each with "read when"; generic "Use the directly cited sources…" line removed) |
| 13 | "## Required Input" (HEAD line 89) | MOVED + MERGED-INTO-CONTRACT | references/community-response-guide.md § Required Input (verbatim); SKILL.md § Required Inputs rows |
| 14 | "## 1. Response Time SLAs by Platform" (HEAD line 103) | MOVED | references/community-response-guide.md § 1. Response Time SLAs by Platform |
| 15 | "## 2. Response Templates by Scenario" (HEAD line 123) | MOVED | references/community-response-guide.md § 2. Response Templates by Scenario |
| 16 | "### a. Positive Comment or Compliment" (HEAD line 127) | MOVED | references/community-response-guide.md § a. Positive Comment or Compliment |
| 17 | "### b. Product or Service Enquiry" (HEAD line 130) | MOVED | references/community-response-guide.md § b. Product or Service Enquiry |
| 18 | "### c. General Complaint (Product or Service)" (HEAD line 133) | MOVED | references/community-response-guide.md § c. General Complaint (Product or Service) |
| 19 | "### d. Shipping or Delivery Complaint" (HEAD line 136) | MOVED | references/community-response-guide.md § d. Shipping or Delivery Complaint |
| 20 | "### e. Offensive or Abusive Comment" (HEAD line 139) | MOVED | references/community-response-guide.md § e. Offensive or Abusive Comment |
| 21 | "### f. Comment from a Competitor" (HEAD line 143) | MOVED | references/community-response-guide.md § f. Comment from a Competitor |
| 22 | "### g. Media or Press Enquiry" (HEAD line 146) | MOVED | references/community-response-guide.md § g. Media or Press Enquiry |
| 23 | "### h. Positive Review (Google / Facebook)" (HEAD line 150) | MOVED | references/community-response-guide.md § h. Positive Review (Google / Facebook) |
| 24 | "### i. Negative Review (Google / Facebook)" (HEAD line 153) | MOVED | references/community-response-guide.md § i. Negative Review (Google / Facebook) |
| 25 | "## 3. Escalation Protocol" (HEAD line 159) | MOVED | references/community-response-guide.md § 3. Escalation Protocol |
| 26 | "### When to Escalate to the Client Directly" (HEAD line 161) | MOVED | references/community-response-guide.md § When to Escalate to the Client Directly |
| 27 | "### Escalation Process" (HEAD line 172) | MOVED | references/community-response-guide.md § Escalation Process |
| 28 | "## 4. Handling Negative Reviews: Four-Step Process" (HEAD line 182) | MOVED | references/community-response-guide.md § 4. Handling Negative Reviews: Four-Step Process |
| 29 | "## 4A. Conversation classification and repair" (HEAD line 200) | MOVED | references/community-response-guide.md § 4A. Conversation classification and repair |
| 30 | "## 5. Growing Community Engagement (Proactive Management)" (HEAD line 208) | MOVED | references/community-response-guide.md § 5. Growing Community Engagement (Proactive Management) |
| 31 | "### Conversation Starters" (HEAD line 212) | MOVED | references/community-response-guide.md § Conversation Starters |
| 32 | "### Engagement Relationships" (HEAD line 215) | MOVED | references/community-response-guide.md § Engagement Relationships |
| 33 | "### Pinned Content" (HEAD line 218) | MOVED | references/community-response-guide.md § Pinned Content |
| 34 | "### Community Milestones" (HEAD line 221) | MOVED | references/community-response-guide.md § Community Milestones |
| 35 | "## 6. Monthly Community Health Scorecard" (HEAD line 226) | MOVED | references/community-response-guide.md § 6. Monthly Community Health Scorecard |
| 36 | "## Quality Criteria" (HEAD line 249) | MOVED + MERGED-INTO-CONTRACT | references/community-response-guide.md § Quality Criteria (verbatim); SKILL.md § Quality Standards |

Quality criteria: Quality Criteria (8 bullets) → all 8 in SKILL.md § Quality Standards; kept verbatim in the guide.

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding (generic Degraded Mode sentence, generic Workflow step 3, generic Outputs row), 0 paraphrased, 0 lost; validator clean; routecheck unchanged; gated ratio 1.6 %; all local links resolve.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: (1) Competing SLAs: the platform SLA table (Facebook comments 2 hours, Instagram 3 hours, X/Twitter 2 hours) differs from references/social-customer-care.md (public comments 3/2/1 hours by business size, X 4/3/2 hours); both kept; that reference already says use the stricter. (2) social-customer-care.md says "The parent SKILL.md keeps the platform SLA table…"; that content now sits in references/community-response-guide.md; pointer not edited. (3) Scorecard "≥3% (EA benchmark)" engagement rate has no source or register ID. (4) Business hours example 08:00–17:30 vs the social-customer-care default 08:00–18:00; both kept.

## playbook-content-production — 348 → 117 lines (gated shared ratio 12.2 % → 0.0 %)

New reference files: references/production-briefs-and-batch-shoot.md (new). Existing reference files unchanged.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Use When" (HEAD line 13) | KEPT | SKILL.md § Use When (byte-identical) |
| 2 | "## Do Not Use When" (HEAD line 21) | KEPT | SKILL.md § Do Not Use When (byte-identical) |
| 3 | "## Required Inputs" (HEAD line 27) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Required Inputs (3 generic rows replaced by domain rows folded from "Required Input") |
| 4 | "## Capability and Permission Boundaries" (HEAD line 34) | REPLACED-BY-CANONICAL | SKILL.md § Capability and Permission Boundaries (canonical sentence + one domain sentence) |
| 5 | "## Degraded Mode" (HEAD line 37) | REPLACED-BY-CANONICAL | SKILL.md § Degraded Mode |
| 6 | "## Decision Rules" (HEAD line 40) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules (every domain row kept; 3 generic rows (inputs complete / evidence incomplete / action needs approval) replaced by domain rows) |
| 7 | "## Workflow" (HEAD line 49) | REPLACED-BY-CANONICAL / domain steps | SKILL.md § Workflow (generic 5 steps replaced by 7 domain steps with stop and rerun) |
| 8 | "## Outputs" (HEAD line 56) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Outputs |
| 9 | "## Evidence Produced" (HEAD line 62) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Evidence Produced |
| 10 | "## Quality Standards" (HEAD line 68) | REPLACED-BY-CANONICAL | SKILL.md § Quality Standards (generic paragraph replaced by domain checks from Quality Criteria) |
| 11 | "## Anti-Patterns" (HEAD line 71) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Anti-Patterns (6 generic bullets replaced by domain bullets with Fix:) |
| 12 | "## References" (HEAD line 79) | MERGED-INTO-CONTRACT | SKILL.md § References (every link kept, each with "read when"; generic "Use the directly cited sources…" line removed) |
| 13 | "## Required Input" (HEAD line 87) | MOVED + MERGED-INTO-CONTRACT | references/production-briefs-and-batch-shoot.md § Required Input (verbatim); SKILL.md § Required Inputs rows |
| 14 | "## 1. Photography Brief Template" (HEAD line 103) | MOVED | references/production-briefs-and-batch-shoot.md § 1. Photography Brief Template |
| 15 | "### Scene Descriptions" (HEAD line 112) | MOVED | references/production-briefs-and-batch-shoot.md § Scene Descriptions |
| 16 | "### Required Shots List (8–12 per shoot)" (HEAD line 115) | MOVED | references/production-briefs-and-batch-shoot.md § Required Shots List (8–12 per shoot) |
| 17 | "### Lighting Guidance" (HEAD line 132) | MOVED | references/production-briefs-and-batch-shoot.md § Lighting Guidance |
| 18 | "### Photography Do's" (HEAD line 138) | MOVED | references/production-briefs-and-batch-shoot.md § Photography Do's |
| 19 | "### Photography Don'ts" (HEAD line 145) | MOVED | references/production-briefs-and-batch-shoot.md § Photography Don'ts |
| 20 | "## 2. Video Brief Template" (HEAD line 153) | MOVED | references/production-briefs-and-batch-shoot.md § 2. Video Brief Template |
| 21 | "### Duration Targets by Platform" (HEAD line 162) | MOVED | references/production-briefs-and-batch-shoot.md § Duration Targets by Platform |
| 22 | "### Scene and Setting Description" (HEAD line 174) | MOVED | references/production-briefs-and-batch-shoot.md § Scene and Setting Description |
| 23 | "### Dialogue or Voiceover Plan" (HEAD line 177) | MOVED | references/production-briefs-and-batch-shoot.md § Dialogue or Voiceover Plan |
| 24 | "### B-Roll List (Supporting Footage)" (HEAD line 182) | MOVED | references/production-briefs-and-batch-shoot.md § B-Roll List (Supporting Footage) |
| 25 | "### Captions" (HEAD line 192) | MOVED | references/production-briefs-and-batch-shoot.md § Captions |
| 26 | "### Call to Action" (HEAD line 195) | MOVED | references/production-briefs-and-batch-shoot.md § Call to Action |
| 27 | "### Branding" (HEAD line 198) | MOVED | references/production-briefs-and-batch-shoot.md § Branding |
| 28 | "## 3. Graphic Design Brief Template" (HEAD line 206) | MOVED | references/production-briefs-and-batch-shoot.md § 3. Graphic Design Brief Template |
| 29 | "### Standard Dimensions by Platform" (HEAD line 214) | MOVED | references/production-briefs-and-batch-shoot.md § Standard Dimensions by Platform |
| 30 | "### Key Message" (HEAD line 228) | MOVED | references/production-briefs-and-batch-shoot.md § Key Message |
| 31 | "### Brand Elements" (HEAD line 233) | MOVED | references/production-briefs-and-batch-shoot.md § Brand Elements |
| 32 | "### Image Guidance" (HEAD line 240) | MOVED | references/production-briefs-and-batch-shoot.md § Image Guidance |
| 33 | "### Text Hierarchy" (HEAD line 243) | MOVED | references/production-briefs-and-batch-shoot.md § Text Hierarchy |
| 34 | "### Design Do's and Don'ts" (HEAD line 249) | MOVED | references/production-briefs-and-batch-shoot.md § Design Do's and Don'ts |
| 35 | "## 4. Batch Production Workflow" (HEAD line 259) | MOVED | references/production-briefs-and-batch-shoot.md § 4. Batch Production Workflow |
| 36 | "### Step 1 — Prepare (Day Before the Shoot)" (HEAD line 263) | MOVED | references/production-briefs-and-batch-shoot.md § Step 1 — Prepare (Day Before the Shoot) |
| 37 | "### Step 2 — Morning Session (Approximately 2 Hours)" (HEAD line 272) | MOVED | references/production-briefs-and-batch-shoot.md § Step 2 — Morning Session (Approximately 2 Hours) |
| 38 | "### Step 3 — Midday Session (Approximately 1 Hour)" (HEAD line 275) | MOVED | references/production-briefs-and-batch-shoot.md § Step 3 — Midday Session (Approximately 1 Hour) |
| 39 | "### Step 4 — Afternoon Session (Approximately 1 Hour)" (HEAD line 278) | MOVED | references/production-briefs-and-batch-shoot.md § Step 4 — Afternoon Session (Approximately 1 Hour) |
| 40 | "### Step 5 — Post-Shoot Review (30 Minutes)" (HEAD line 281) | MOVED | references/production-briefs-and-batch-shoot.md § Step 5 — Post-Shoot Review (30 Minutes) |
| 41 | "### Step 6 — Editing and Scheduling (2–3 Days After the Shoot)" (HEAD line 284) | MOVED | references/production-briefs-and-batch-shoot.md § Step 6 — Editing and Scheduling (2–3 Days After the Shoot) |
| 42 | "## 5. Content Shoot Checklist" (HEAD line 289) | MOVED | references/production-briefs-and-batch-shoot.md § 5. Content Shoot Checklist |
| 43 | "## 6. Content Quality Standard" (HEAD line 316) | MOVED | references/production-briefs-and-batch-shoot.md § 6. Content Quality Standard |
| 44 | "## Quality Criteria" (HEAD line 337) | MOVED + MERGED-INTO-CONTRACT | references/production-briefs-and-batch-shoot.md § Quality Criteria (verbatim); SKILL.md § Quality Standards |

Quality criteria: Quality Criteria (8 bullets) → all 8 in SKILL.md § Quality Standards; kept verbatim in the reference.

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding (generic Degraded Mode sentence, generic Workflow step 3, generic Outputs row), 0 paraphrased, 0 lost; validator clean; routecheck unchanged; gated ratio 0.0 %; all local links resolve.
Paraphrased lines: References line "Real-time content bridge… for the listen/verify/adapt/approve/publish/measure bridge, intent-led language, and distinctive voice" → SKILL.md § References (same terms, "read when" form).
Noticed, not changed: (1) The graphic dimensions table (for example Facebook feed 1200 × 630 px, WhatsApp broadcast 800 × 800 px) has no register ID, while playbook-agency-operations cites register AD-08 (4:5 feed, 9:16 Stories/Reels) for Meta paid placements. (2) "Batch production reduces content creation cost by 60–80%" is unsourced. (3) "the majority of social video is watched without sound in the EA market" is unsourced. (4) Video duration targets are unregistered.

## playbook-crisis-communications — 336 → 120 lines (gated shared ratio 14.7 % → 1.6 %)

New reference files: references/crisis-response-procedures.md (new). Existing reference files unchanged.

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | "## Use When" (HEAD line 13) | KEPT | SKILL.md § Use When (byte-identical) |
| 2 | "## Do Not Use When" (HEAD line 21) | KEPT | SKILL.md § Do Not Use When (byte-identical) |
| 3 | "## Required Inputs" (HEAD line 27) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Required Inputs (3 generic rows replaced by domain rows folded from "Required Input") |
| 4 | "## Capability and Permission Boundaries" (HEAD line 34) | REPLACED-BY-CANONICAL | SKILL.md § Capability and Permission Boundaries (canonical sentence + one domain sentence) |
| 5 | "## Degraded Mode" (HEAD line 37) | REPLACED-BY-CANONICAL | SKILL.md § Degraded Mode |
| 6 | "## Decision Rules" (HEAD line 40) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules (every domain row kept; 3 generic rows (inputs complete / evidence incomplete / action needs approval) replaced by domain rows) |
| 7 | "## Workflow" (HEAD line 49) | REPLACED-BY-CANONICAL / domain steps | SKILL.md § Workflow (generic 5 steps replaced by 7 domain steps with stop and rerun) |
| 8 | "## Outputs" (HEAD line 56) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Outputs |
| 9 | "## Evidence Produced" (HEAD line 62) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Evidence Produced |
| 10 | "## Quality Standards" (HEAD line 68) | REPLACED-BY-CANONICAL | SKILL.md § Quality Standards (generic paragraph replaced by domain checks from Quality Criteria) |
| 11 | "## Anti-Patterns" (HEAD line 71) | REPLACED-BY-CANONICAL / domain rows | SKILL.md § Anti-Patterns (6 generic bullets replaced by domain bullets with Fix:) |
| 12 | "## Book-derived additions" (HEAD line 79) | MERGED-INTO-CONTRACT | SKILL.md § Decision Rules (infodemic row) and § References (same link) |
| 13 | "## References" (HEAD line 84) | MERGED-INTO-CONTRACT | SKILL.md § References (every link kept, each with "read when"; generic "Use the directly cited sources…" line removed) |
| 14 | "## Required Input" (HEAD line 91) | MOVED + MERGED-INTO-CONTRACT | references/crisis-response-procedures.md § Required Input (verbatim); SKILL.md § Required Inputs rows |
| 15 | "## Foundational Principle" (HEAD line 105) | MOVED | references/crisis-response-procedures.md § Foundational Principle |
| 16 | "## 1. Crisis Severity Classification" (HEAD line 111) | MOVED | references/crisis-response-procedures.md § 1. Crisis Severity Classification |
| 17 | "### Level 1 — Minor Complaint or Negative Post" (HEAD line 113) | MOVED | references/crisis-response-procedures.md § Level 1 — Minor Complaint or Negative Post |
| 18 | "### Level 2 — Viral Negative Post or Media Attention" (HEAD line 123) | MOVED | references/crisis-response-procedures.md § Level 2 — Viral Negative Post or Media Attention |
| 19 | "### Level 3 — Major Reputational Threat" (HEAD line 133) | MOVED | references/crisis-response-procedures.md § Level 3 — Major Reputational Threat |
| 20 | "## 2. Response Protocol by Level" (HEAD line 143) | MOVED | references/crisis-response-procedures.md § 2. Response Protocol by Level |
| 21 | "### Level 1 Response Timeline" (HEAD line 145) | MOVED | references/crisis-response-procedures.md § Level 1 Response Timeline |
| 22 | "### Level 2 Response Timeline" (HEAD line 165) | MOVED | references/crisis-response-procedures.md § Level 2 Response Timeline |
| 23 | "### Level 3 Response Timeline" (HEAD line 188) | MOVED | references/crisis-response-procedures.md § Level 3 Response Timeline |
| 24 | "## 3. Holding Statement Templates" (HEAD line 210) | MOVED | references/crisis-response-procedures.md § 3. Holding Statement Templates |
| 25 | "### Level 1 Holding Statement" (HEAD line 212) | MOVED | references/crisis-response-procedures.md § Level 1 Holding Statement |
| 26 | "### Level 2 Holding Statement" (HEAD line 215) | MOVED | references/crisis-response-procedures.md § Level 2 Holding Statement |
| 27 | "### Level 3 Holding Statement" (HEAD line 218) | MOVED | references/crisis-response-procedures.md § Level 3 Holding Statement |
| 28 | "## 4. What NOT to Do in a Crisis" (HEAD line 225) | MOVED | references/crisis-response-procedures.md § 4. What NOT to Do in a Crisis |
| 29 | "## 5. Platform-Specific Crisis Actions" (HEAD line 239) | MOVED | references/crisis-response-procedures.md § 5. Platform-Specific Crisis Actions |
| 30 | "### All Platforms" (HEAD line 241) | MOVED | references/crisis-response-procedures.md § All Platforms |
| 31 | "### Facebook" (HEAD line 244) | MOVED | references/crisis-response-procedures.md § Facebook |
| 32 | "### Instagram" (HEAD line 247) | MOVED | references/crisis-response-procedures.md § Instagram |
| 33 | "### WhatsApp Business" (HEAD line 250) | MOVED | references/crisis-response-procedures.md § WhatsApp Business |
| 34 | "### X / Twitter" (HEAD line 253) | MOVED | references/crisis-response-procedures.md § X / Twitter |
| 35 | "### LinkedIn" (HEAD line 256) | MOVED | references/crisis-response-procedures.md § LinkedIn |
| 36 | "## 6. Post-Crisis Review" (HEAD line 261) | MOVED | references/crisis-response-procedures.md § 6. Post-Crisis Review |
| 37 | "## 7. One-Page Crisis Quick Card" (HEAD line 279) | MOVED | references/crisis-response-procedures.md § 7. One-Page Crisis Quick Card |
| 38 | "### Crisis Levels at a Glance" (HEAD line 287) | MOVED | references/crisis-response-procedures.md § Crisis Levels at a Glance |
| 39 | "### First 30-Minute Checklist (Level 2 / 3)" (HEAD line 295) | MOVED | references/crisis-response-procedures.md § First 30-Minute Checklist (Level 2 / 3) |
| 40 | "### Holding Statements (Ready to Use)" (HEAD line 302) | MOVED | references/crisis-response-procedures.md § Holding Statements (Ready to Use) |
| 41 | "### Escalation Contacts" (HEAD line 308) | MOVED | references/crisis-response-procedures.md § Escalation Contacts |
| 42 | "### What NOT to Do" (HEAD line 316) | MOVED | references/crisis-response-procedures.md § What NOT to Do |
| 43 | "## Quality Criteria" (HEAD line 325) | MOVED + MERGED-INTO-CONTRACT | references/crisis-response-procedures.md § Quality Criteria (verbatim); SKILL.md § Quality Standards |

Quality criteria: Quality Criteria (8 bullets) → all 8 in SKILL.md § Quality Standards; kept verbatim in the reference. The horizontal rules (---) framing the quick card were not carried over; the card keeps its heading and every line.

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding (generic Degraded Mode sentence, generic Workflow step 3, generic Outputs row), 0 paraphrased, 0 lost; validator clean; routecheck unchanged; gated ratio 1.6 %; all local links resolve.
Paraphrased lines: "## Foundational Principle" (acknowledge → investigate → update cadence) → kept verbatim in the reference and summarised in the SKILL.md intro and Workflow step 3.
Noticed, not changed: (1) The Level 2 holding statement suggests an update in "4–6 hours" while the foundational cadence puts the second response at "4–8 hours"; both kept. (2) Level 1 says notify the client "within 4 hours" in the definition but lists the notification under "First 24 hours" in the timeline; both kept. (3) Facebook profanity-filter and Instagram Hidden Words menu paths are unregistered UI paths.

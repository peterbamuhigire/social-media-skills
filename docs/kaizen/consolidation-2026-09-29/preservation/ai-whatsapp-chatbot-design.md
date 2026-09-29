# Preservation map — ai-whatsapp-chatbot-design → playbook-chatbot-strategy

Filled from [preservation-map-template.md](../preservation-map-template.md) for Social Kaizen S02-T06 (see [merge-runbook.md](../merge-runbook.md), step 2).

Source: skills/ai-marketing/ai-whatsapp-chatbot-design/SKILL.md @ 7c60138 (187 lines; reads Aug–Sep 2026: 2; fan-in 2)
Destination reference: skills/playbooks/playbook-chatbot-strategy/references/whatsapp-chatbot-design.md

Abbreviation: REF = `skills/playbooks/playbook-chatbot-strategy/references/whatsapp-chatbot-design.md`; TGT = `skills/playbooks/playbook-chatbot-strategy/SKILL.md`.

| # | Source item (heading / decision row / anti-pattern / citation / reference file) | Destination (file § section) | Status (MOVED / MERGED-WITH-EXISTING / DROPPED-DUPLICATE-OF <target §>) | Reviewer tick |
|---|---|---|---|---|
| 1 | Shared contract scaffolding (frontmatter description, Use When, Do Not Use When, Required Inputs table, Capability and Permission Boundaries, Degraded Mode, Workflow steps 1–6, Outputs, Evidence Produced, Quality Standards, References to `ai-readiness-diagnostic` and `AGENTS.md`) | TGT § Use When … § Quality Standards | DROPPED-DUPLICATE-OF TGT contract sections: "Required Inputs" table, "Capability and Permission Boundaries" ("publishing, messaging, production changes, personal-data processing, spending … require explicit authority"), "Degraded Mode" ("Mark each unavailable check `not assessed`; never convert it into a pass"), Workflow 1–5, Outputs, Evidence Produced, Quality Standards | ticked |
| 2 | Decision row: "Data readiness, AI maturity and risk support the proposed operating level → choose the lowest viable automation level and define its human approval gate" | REF § Decision rules (row "Choosing the operating level") | MOVED | ticked |
| 3 | Decision row: "A required fact or approval is missing → stop that claim or action; request it or use an explicit placeholder" | TGT § Decision Rules | DROPPED-DUPLICATE-OF TGT § Decision Rules row "Evidence or tooling is incomplete → Produce the narrowest qualified draft and a gap list" and § Anti-Patterns "Inventing a client fact, benchmark, budget or approval. Fix: cite the source or label the assumption" | ticked |
| 4 | Decision row: "Evidence is partial but a useful draft is possible → deliver a qualified draft with gaps and the next verification step" | TGT § Decision Rules | DROPPED-DUPLICATE-OF TGT § Decision Rules row "Evidence or tooling is incomplete → Produce the narrowest qualified draft and a gap list" | ticked |
| 5 | Anti-pattern: writing before objective and audience are known | TGT § Workflow step 1 | DROPPED-DUPLICATE-OF TGT § Workflow 1 "Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing" | ticked |
| 6 | Anti-pattern: reusing a neighbouring skill's template because headings look similar | TGT § Anti-Patterns | DROPPED-DUPLICATE-OF TGT § Anti-Patterns "Copying one channel or client pattern unchanged. Fix: tie each choice to the named audience, objective and evidence" | ticked |
| 7 | Anti-pattern: adding a price, result, quotation, platform limit or cultural claim without a traceable source | TGT § Anti-Patterns | DROPPED-DUPLICATE-OF TGT § Anti-Patterns "Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim" | ticked |
| 8 | Anti-pattern: treating missing access, evidence or native-language review as approval | TGT § Anti-Patterns | DROPPED-DUPLICATE-OF TGT § Anti-Patterns "Treating an inaccessible account, file or metric as healthy. Fix: mark it `not assessed`" | ticked |
| 9 | Anti-pattern: publishing, sending, spending or changing a live account from drafting authority | TGT § Anti-Patterns | DROPPED-DUPLICATE-OF TGT § Anti-Patterns "Publishing, spending, messaging or changing production state from planning authority. Fix: obtain explicit action authority" | ticked |
| 10 | Heading: Required Input (business name/industry; country/city default Uganda; primary goal: customer service / sales enquiries / appointment booking / FAQ handling; monthly WhatsApp message volume; languages English, Luganda, Kiswahili, other; human support team size and hours) | REF § Inputs | MERGED-WITH-EXISTING (TGT § Required Input covers name/industry, country/city, volume, platform; the goal, monthly volume, languages and team size/hours rows MOVED into REF § Inputs) | ticked |
| 11 | Heading: Why WhatsApp + LLM for East Africa (dominance statement with WA-01 caveat; 24/7 sales and support agent that speaks the customer's language, remembers context, escalates; availability and responsiveness at affordable cost) | REF § Why WhatsApp plus an LLM in East Africa | MOVED | ticked |
| 12 | Heading: Architecture: Three Layers — Layer 1 rule-based flows (hours, pricing, location, ordering; fast, reliable, zero AI cost) | REF § Three-layer architecture, row Layer 1 | MOVED | ticked |
| 13 | Layer 2 LLM responses (open-ended queries outside the tree; grounded in brand knowledge base) | REF § Three-layer architecture, row Layer 2 | MOVED (knowledge-base pointer re-pointed from `ai-rag-brand-knowledge-base` to `brand-voice-ai-training`, which absorbs it in S02-T04) | ticked |
| 14 | Layer 3 human escalation triggers (complaint, frustration, low LLM confidence, money, contracts, sensitive personal data) | REF § Three-layer architecture, row Layer 3 | MOVED | ticked |
| 15 | Heading: Social Presence Principles (Ltifi, 2025) — warmth, responsiveness, human-like cues | REF § Social presence principles | MOVED | ticked |
| 16 | Principle: greet by name ("Hello Nakato! How can I help you today?") | REF § Social presence principles | MOVED | ticked |
| 17 | Principle: local greetings as an option ("Oli otya?" / "Habari?") for informal register | REF § Social presence principles | MERGED-WITH-EXISTING (TGT § EA-Specific Considerations has the Luganda "Nkulamusizza!" welcome; the Luganda/Kiswahili informal greetings MOVED to REF) | ticked |
| 18 | Principle: acknowledge emotional context (example line) | REF § Social presence principles | MOVED | ticked |
| 19 | Principle: avoid corporate coldness — never open with "Please select from the following options:" | REF § Social presence principles | MOVED | ticked |
| 20 | Principle: mirror the customer's register | REF § Social presence principles | MOVED | ticked |
| 21 | Principle: disclose AI nature when asked (Uganda Data Protection and Privacy Act, 2019) | REF § Social presence principles and § Checklist | MOVED | ticked |
| 22 | Heading: Conversation Flow Design — Step 1 map the top 10 customer queries by interviewing the support team (past month) | REF § Procedure step 1 | MERGED-WITH-EXISTING (TGT § Section 3 Step 1 maps top 5 for FAQ bots; REF keeps top 10 for the LLM build) | ticked |
| 23 | Step 2 design the decision tree (UGX price-options example with Option A/B/C and YES reply) | REF § Procedure step 2 | MOVED | ticked |
| 24 | Step 3 define the LLM boundary and system prompt template (6-line prompt) | REF § Procedure step 3 | MOVED | ticked |
| 25 | Step 4 HITL escalation triggers (keywords complaint/refund/legal/manager/angry/cheated; same issue > 2 times; transaction above threshold; explicit request; low confidence) and handoff message template | REF § Procedure step 4 | MERGED-WITH-EXISTING (TGT § Section 3 Step 4 has AGENT/HUMAN/HELP keywords and EAT hours; REF keeps the LLM-specific triggers and "[X] minutes" handoff template) | ticked |
| 26 | Step 5 knowledge base input (catalogue with UGX prices; approved FAQs; returns, delivery, payment policies; hours and locations; team names and roles for escalation) | REF § Procedure step 5 | MOVED | ticked |
| 27 | Heading: Tool Options table (WATI from USD 49/month; Respond.io from USD 79/month; Interakt from USD 15/month; Twilio pay-per-message, developer; Meta Cloud API pay-per-message, developer) | REF § Tool options | MERGED-WITH-EXISTING (Twilio also in TGT § Section 2; all five rows kept in REF with a verify-before-quoting note) | ticked |
| 28 | Heading: Measurement Framework (containment 60–80% mature; first response < 30 s; CSAT 1–5; escalation rate; conversion rate) | REF § Measurement framework | MOVED | ticked |
| 29 | Heading: Quality Criteria (8 items: top-10 flows; social presence; HITL triggers + handoff template; system prompt; knowledge-base document; tool fit to budget/capacity; ≥ 4 KPIs with targets; DPPA 2019 noted) | REF § Checklist | MOVED | ticked |
| 30 | Citation: Boustany, S. (2024) *Generative AI for Social Media Marketing* | REF § Sources | MOVED | ticked |
| 31 | Citation: Ltifi, M. (ed.) (2025) *Advances in Digital Marketing in the Era of Artificial Intelligence*, CRC Press | REF § Sources | MOVED | ticked |
| 32 | Citation: Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn, Mercury Learning | REF § Sources | MOVED | ticked |
| 33 | Legal citation: Uganda Data Protection and Privacy Act, 2019 | REF § Social presence principles, § Checklist, § Sources | MOVED | ticked |
| 34 | Source-register ID: WA-01 (register row `WHATSAPP-USAGE-EA-2026`, 2026-09-24) | REF § Why WhatsApp plus an LLM in East Africa | MOVED | ticked |
| 35 | Cross-skill pointer: `ai-rag-brand-knowledge-base` (Layer 2 and Step 5) | REF § Three-layer architecture and § Procedure step 5 | MOVED (re-pointed to `brand-voice-ai-training`, the S02-T04 target) | ticked |
| 36 | Reference files in `references/` | — | None: the source has no `references/` directory | ticked |
Unique facts with register IDs carried: WA-01 / `WHATSAPP-USAGE-EA-2026` (freshness re-checked: yes — `docs/source-registers/source-register.json` verified_on 2026-09-25, next_review 2026-12-25, support_status partial)
Items dropped as duplicates (must name the equivalent target text): 8 (rows 1, 3–9)
Reviewer: independent review agent (Claude Opus 5.5, read-only, S02 review) — verdict ACCEPT — 2026-09-29

A status of `DROPPED` without an equivalent target section is a `REJECT`.

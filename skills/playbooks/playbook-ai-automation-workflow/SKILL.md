---
name: playbook-ai-automation-workflow
description: Use when designing or improving a Ai Automation Workflow operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Playbook — AI & Automation Workflow

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Ai Automation Workflow workflow for a client or delivery team.
- Turn an approved objective into roles, controls, handoffs and measurable actions.

## Do Not Use When
- The task is a single-channel presence plan; use the closest `platform-*` skill.
- The task is upstream positioning or channel choice; use the closest `strategy-*` skill.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience and success measure | Approved client brief or accountable owner | Yes | Stop and request the missing decision |
| Current workflow, assets and performance evidence | Team records, platform exports or supplied artefacts | Conditional | Label the baseline unassessed and use a minimum viable workflow |
| Roles, budget, timing and approval limits | Delivery owner | Yes for execution | Produce a draft only; do not schedule, spend or publish |

## Capability and Permission Boundaries
Read supplied artefacts and search relevant evidence. Treat review, audit and planning as read-only. Editing the requested draft is allowed; publishing, messaging, production changes, personal-data processing, spending, destructive actions and certification claims require explicit authority. Use network access only for authorised verification.

## Degraded Mode
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Ai Automation Workflow playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| An automated step can publish, spend or expose data | Insert human approval and an auditable rollback point | Unsupervised high-impact automation |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Ai Automation Workflow playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Ai Automation Workflow playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
| Assumption and gap register | Approver or next workflow | Every missing source, unassessed check and required approval has an owner or next action |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and verification record | Inline table or appendix | Each material choice traces to an input, source or labelled assumption |
| Release-gate result | Completed checklist | No blocking policy, factual, permission or anti-slop finding remains |

## Quality Standards
Use British English and the specified market context. Recommendations must be executable with the stated capacity, current claims must be verified or qualified, and acceptance conditions must be observable. A worked example must use a labelled scenario, not fabricated client evidence.

## Anti-Patterns
- Inventing a client fact, benchmark, budget or approval. Fix: cite the source or label the assumption and its effect.
- Copying one channel or client pattern unchanged. Fix: tie each choice to the named audience, objective and evidence.
- Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim.
- Treating an inaccessible account, file or metric as healthy. Fix: mark it `not assessed` and bound the conclusion.
- Publishing, spending, messaging or changing production state from planning authority. Fix: obtain explicit action authority.
- Delivering actions without owner, timing or acceptance. Fix: assign all three or return the item as an unresolved gap.

## References
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- [East African English standard](../../language/east-african-english/SKILL.md)
- Use the directly cited sources and companion skills in the domain guidance below; verify time-sensitive claims before use.
<!-- dual-compat-end -->

## Purpose

Produce a realistic, affordable automation roadmap for a client's marketing operations.
Most East African clients are at Stage 1 (manual, disconnected). The goal is a practical
sequence that saves 5–10 hours per week and improves consistency — not enterprise-grade
automation, but a structured build that reaches Stage 3 within 60–90 days.

Source framework: Upadhyay, N. (2024) *Generative AI for Marketing* — 10-step automation
workflow and 8 task qualification factors.

---

## Required Input

Before generating any deliverable, ask the client for:

1. **Business name** — trading name of the organisation
2. **Industry** — sector (e.g. retail, hospitality, professional services, NGO)
3. **Country / city** — location and primary market
4. **Primary goal** — what does the client most want automation to achieve?
   (e.g. "stop missing enquiries after hours", "post consistently without daily effort",
   "send follow-up emails automatically")
5. **Current tools** — list every tool already in use (schedulers, email platforms, CRMs,
   WhatsApp Business or standard, website platform)
6. **Team size and technical comfort** — how many people manage marketing, and how
   comfortable are they with new software?
7. **Monthly budget for tools** — approximate range in UGX or USD
8. **Biggest pain point** — where does the most time get lost in the current workflow?

---

## Step 1 — Assess the Client's Automation Maturity Stage

Classify the client against the four stages (Upadhyay 2024):

| Stage | Label | Characteristics |
|---|---|---|
| **1** | Basic | Manual everything; no scheduling; ad hoc posting; enquiries answered individually |
| **2** | Aligned | Scheduled posts; basic email automation; at least one connected tool |
| **3** | Multichannel | Content pipeline connected across platforms; auto-reporting; chatbot for FAQs |
| **4** | Automated | AI-generated content variants; behavioural triggers; continuous optimisation loops |

Design the roadmap to move the client from their current stage to **Stage 3**.
Do not propose Stage 4 unless the client has a dedicated digital team and a monthly tool
budget above UGX 500,000.

State the client's current stage explicitly at the top of the roadmap and justify the
classification using evidence from the Required Input responses.

---

## Step 2 — Qualify Each Task for Automation

Before recommending automation for any specific task, apply the **8 qualification factors**
(Upadhyay 2024). For each candidate task, answer:

1. **Cost** — is the automation cheaper than the human time it replaces? (Include tool cost
   and setup time, not just the monthly subscription.)
2. **Resources** — do we have the tools and skills to maintain this automation reliably?
3. **Skillset** — does the team know how to set it up, or is training required first?
4. **Competitive position** — does this automation create a meaningful advantage, or is it
   simply hygiene?
5. **Sustainability** — will this keep working without constant maintenance? (Rule: if it
   needs weekly manual intervention to function, it is not truly automated.)
6. **Stack compatibility** — does it integrate with the tools the client already uses?
7. **Workforce support** — does the team accept the automation, or is there resistance?
   (Automation that the team works around fails within weeks.)
8. **Collateral impact** — does automating this task break anything else in the workflow?
   (e.g. auto-scheduling posts that then trigger manual reporting processes)

Only recommend automation for tasks that pass at least 6 of the 8 factors.
Flag borderline tasks with a note on the risk.

---

## Step 3 — Apply the 4 Feasibility Tests

Before adding any task to the build plan, verify:

1. **Repeatability** — is the task identical every time? If the task varies by context,
   client, or tone, automation will produce inconsistencies. Flag it as human-led.
2. **Predictability** — can you define the trigger and the desired outcome in advance?
   (e.g. "when someone submits a contact form → send welcome email" is predictable;
   "when a follower seems unhappy → respond with empathy" is not.)
3. **Criticality** — what happens when the automation fails? High-criticality tasks
   (e.g. complaint handling, crisis response) must retain a human fallback at every step.
4. **Intuitiveness** — can a non-technical team member manage the automation day-to-day
   without calling a developer? If not, document the dependency and plan for it.

Tasks that fail Feasibility Test 3 or 4 require a human fallback protocol alongside the
automation — document both.

---

## Step 4 — Build the Automation Priority Matrix

Plot candidate tasks on a 2×2 matrix before sequencing the build plan:

|  | **High Time Cost** | **Low Time Cost** |
|---|---|---|
| **High Frequency** | Automate first — highest ROI | Automate second — consistency gain |
| **Low Frequency** | Automate third — strategic value | Automate last — low priority |

Use the matrix to sequence the build plan. Do not propose automating low-frequency,
low-time-cost tasks in the first 90 days.

---

## Step 5 — Recommend the Appropriate Tool Stack

Match the tool recommendation to the client's budget. Default to free-tier tools for
Stage 1–2 clients unless the budget explicitly supports paid tools.

### Free Tier — Stage 2 Baseline (UGX 0/month)

| Function | Tool | Notes |
|---|---|---|
| Social scheduling | Meta Business Suite | Schedules Facebook and Instagram; free; available in Uganda |
| WhatsApp auto-reply | WhatsApp Business app | Free greeting and away messages; up to 50 Quick Replies |
| Email marketing | Mailchimp (free plan) | Up to 500 contacts; 1,000 sends/month |
| Reporting | Meta Insights + Google Sheets | Pull data manually into a monthly template |

### Starter Paid Tier (~ UGX 50,000–150,000/month)

| Function | Tool | Notes |
|---|---|---|
| Social scheduling | Buffer Essentials or Hootsuite Professional | Multi-platform; analytics included |
| Email marketing | Mailchimp Essentials or Brevo Starter | Higher send limits; automation sequences |
| WhatsApp chatbot | ManyChat Pro | WhatsApp automation flows; FAQ bots |
| Analytics dashboard | Notion or Google Sheets | Connected to platform exports |

### Growth Tier (~ UGX 150,000–500,000/month)

| Function | Tool | Notes |
|---|---|---|
| CRM + email | HubSpot Starter | CRM, email, forms, and pipeline in one platform |
| Social management | Sprout Social or Hootsuite Business | Full scheduling, listening, and reporting |
| Chatbot + integrations | ManyChat Pro + Zapier | Cross-tool automation flows |
| Reporting | Google Looker Studio (free) | Connects to all sources; builds live dashboards |

Recommend only tools with a documented free tier or a local payment method accessible
in Uganda (e.g. Visa, Mastercard, or MTN Mobile Money via Payoneer).

---

## Step 6 — The Automation Build Plan

Deliver the build plan as a prioritised, week-by-week sequence. Adjust timing based on
the client's maturity stage — compress for Stage 2 clients, expand for Stage 1 clients
who need training first.

### Week 1 — Content Scheduling

- Set up Meta Business Suite and connect both the Facebook Page and Instagram account.
- Schedule a minimum of two weeks of content in advance before going live.
- Establish a weekly scheduling session (e.g. every Monday, 1 hour) as a standing
  calendar appointment.
- Confirm the content source: does content come from the client, a content plan
  document, or the `11-content-calendar` skill output?

### Week 1 — WhatsApp Auto-Reply

- Switch from WhatsApp standard to WhatsApp Business if not already done.
- Write and activate a greeting message (sent to new contacts on first message).
- Write and activate an away message (sent outside business hours — define the hours).
- Create 5 Quick Replies for the most common enquiries (identify these from the
  client's message history).
- Test all messages by sending from a personal number.

### Week 2 — Email Welcome Sequence

- Set up Mailchimp (or the agreed email platform).
- Build a 3-email welcome sequence triggered automatically by a form opt-in:
  - Email 1 (immediate): Thank you and what to expect
  - Email 2 (Day 3): Most useful resource or offer
  - Email 3 (Day 7): Invitation to engage (reply, book, visit)
- Connect the opt-in form to the client's website or a Google Form if no website exists.
- Test the full sequence end-to-end before publishing.

### Week 3 — Social Listening Alert

- Set up Google Alerts for: brand name, key product or service names, top 2 competitors.
- Configure alerts to arrive as a daily email digest (not real-time — reduces noise).
- Assign one team member to review the digest each morning and flag anything requiring
  a response.

### Week 4 — Monthly Report Automation

- Build a Google Sheets reporting template with tabs for: Facebook, Instagram, WhatsApp
  (manual), Email (Mailchimp export), and a Summary tab.
- Pre-fill the formulas for reach, engagement rate, follower growth, and email open rate.
- Set a recurring monthly calendar reminder (first Monday of each month) to populate
  and send the report.
- This is semi-automated, not fully automated — note the manual steps clearly.

### Month 2 — Chatbot FAQ Automation

- Extract the 10 most common questions received via WhatsApp Messenger over the past
  90 days (ask the client to review their message history).
- Set up ManyChat flows for each question, including a clear escalation path to a
  human agent for anything the bot cannot resolve.
- Write escalation copy that acknowledges the limit of the bot and sets a response
  time expectation ("Our team will reply within 2 hours during business hours").
- Test every flow from end to end, including failure paths.
- Review bot performance at 30 days and update flows based on missed conversations.

---

## Step 7 — What Must Stay Human

Do not automate the following tasks under any circumstances:

- **Complaint responses** — require empathy, judgement, and accountability
- **Crisis communications** — require speed, authority, and brand decision-making
- **Any message with emotional content** — condolences, difficult news, conflict resolution
- **Content strategy decisions** — platform mix, campaign themes, brand direction
- **Client relationship conversations** — proposals, negotiations, renewals
- **Community management in sensitive contexts** — political, cultural, or religious topics
- **Any response requiring local knowledge** — cultural references, local events, current affairs

Flag these clearly in the roadmap with the instruction: *Human only — do not automate.*

---

## Step 8 — Automation Maintenance Schedule

Automation is not set-and-forget. Include this maintenance schedule in every roadmap.

**Weekly (15 minutes):**
- Check the scheduling queue is populated at least two weeks ahead.
- Review chatbot missed conversations (ManyChat "Unhandled" folder or equivalent).
- Check Google Alerts digest for anything requiring a response.

**Monthly (1 hour):**
- Review auto-reply messages for accuracy (prices, hours, offers may have changed).
- Review email sequence performance: open rate, click rate, unsubscribes.
- Pull and complete the Google Sheets monthly report.
- Check tool billing — confirm free tier limits have not been exceeded.

**Quarterly (2–3 hours):**
- Full automation audit: what is working, what is not, what has broken silently.
- Retire automations that are no longer relevant.
- Review the tool stack against the client's current budget and upgrade where justified.
- Reassess maturity stage and plan the next stage of the roadmap.

---

## No-Code Automation Stack (Erné, 2024)

Combine AI intelligence with workflow automation using two layers:

**Layer 1 — Automation (Zapier or Make.com):**
- Connect data sources: Google Sheets, Meta Business Suite, WhatsApp Business, Mailchimp, Airtable
- Trigger actions: "When new lead form submitted → add to CRM → send welcome WhatsApp → notify account manager"
- Both tools have free tiers accessible to EA clients

**Layer 2 — Intelligence (Claude or ChatGPT API):**
- Analyse data: "Summarise this month's engagement data and identify 3 actionable insights"
- Generate content: "Draft a WhatsApp follow-up message for a lead who enquired about [service]"
- Route decisions: "Classify this customer complaint as urgent/standard/low-priority"

**Combining both layers:** Zapier/Make handles the plumbing (moving data between tools); Claude/ChatGPT provides the intelligence (analysis and generation). Together they form a low-code AI consultancy engine.

**EA-accessible starter stack:**
- Zapier Free (5 Zaps) + Google Sheets + Gmail + WhatsApp Business API (Twilio or WATI)
- Estimated monthly cost: $0–$50 USD depending on message volume

---

## Multi-Agent Architecture (Farri and Rosani, 2025; Nayebi, 2025)

Rather than one general-purpose AI chatbot, advanced marketing operations use multiple specialised agents working in concert:

| Agent | Role | Example tools |
|---|---|---|
| Research agent | Monitors trends, competitor activity, brand mentions | Perplexity, Brandwatch, Google Alerts |
| Copywriting agent | Drafts captions, emails, scripts from brief | Claude/ChatGPT with brand context |
| Analytics agent | Pulls performance data and generates insights | Meta Business Suite API, GA4 |
| Scheduling agent | Publishes approved content at optimal times | Buffer, Hootsuite, Later |

**Coordination:** A human consultant acts as the orchestrator — reviewing outputs from each agent, resolving conflicts, and making strategic decisions that require local knowledge or client relationship context.

**Implementation path:** Start with one agent (typically the copywriting agent). Add agents one at a time as confidence grows.

---

## Human-in-the-Loop (HITL) Escalation Protocol (Nayebi, 2025)

Define clear thresholds so automation handles routine decisions and humans handle high-stakes ones:

| Decision type | AI handles | Human handles |
|---|---|---|
| Caption drafting | ✓ Draft | ✓ Final approval |
| Community management | ✓ Routine queries, FAQs | ✓ Complaints, crises, sensitive topics |
| Performance reporting | ✓ Data pull + narrative draft | ✓ Strategic commentary + client presentation |
| Campaign optimisation | ✓ A/B test suggestions | ✓ Budget reallocation decisions |
| Crisis response | ✗ Do not automate | ✓ Human-only — use crisis playbook |

**Protocol:** Every automated workflow must have a defined escalation trigger. When the trigger fires, a human receives an alert with full context and a recommended action. The human approves, modifies, or overrides. The AI never acts autonomously on sensitive decisions.

---

## Quality Criteria

Output meets the standard for this skill if it:

1. **Classifies the client's current maturity stage** accurately with evidence from the
   intake responses, and states a clear target stage for the 90-day roadmap.
2. **Applies the 8 qualification factors** to at least the top 3 candidate automation tasks,
   with a pass/fail or flag outcome for each.
3. **Sequences the build plan** by priority (high-frequency, high-time-cost tasks first),
   with realistic week-by-week milestones that a Stage 1–2 client can actually execute.
4. **Recommends tools matched to the client's budget**, defaulting to free-tier options
   and noting any tool that requires payment in USD with a local payment workaround.
5. **Distinguishes clearly between automated, semi-automated, and human-only tasks**,
   with no ambiguity about which tasks require human intervention.
6. **Includes the maintenance schedule** as a standalone, actionable section — not buried
   in the build plan.
7. **Stays culturally and operationally grounded** in the East African context: references
   WhatsApp as the primary customer communication channel; acknowledges intermittent
   connectivity; avoids tools unavailable or unaffordable in Uganda.
8. **Avoids scope creep** — this skill covers operational automation only; content
   production automation belongs to `playbook-ai-content-workflow`; paid advertising
   automation is out of scope entirely.

---

## References

- Upadhyay, N. (2024) *Generative AI for Marketing*. Kogan Page. [10-step automation
  workflow; 8 task qualification factors — cited in Steps 1, 2, and 4 above]
- Erné, R. (2024) *AI-Powered Marketing*. [No-code automation stack; Zapier/Make +
  Claude/ChatGPT two-layer model — cited in No-Code Automation Stack section]
- Farri, O. and Rosani, M. (2025) *Multi-Agent Systems for Marketing*. [Multi-agent
  architecture patterns — cited in Multi-Agent Architecture section]
- Nayebi, M. (2025) *Human-in-the-Loop AI*. [HITL escalation protocols and agent
  orchestration — cited in Multi-Agent Architecture and HITL sections]
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.

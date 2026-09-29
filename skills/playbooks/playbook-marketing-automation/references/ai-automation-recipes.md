# AI Automation Recipes

Merged from skills/playbooks/playbook-ai-automation-workflow on 2026-09-29 at 7c60138; preservation map: [playbook-ai-automation-workflow.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/playbook-ai-automation-workflow.md)

## When to use this reference

Use it when the client needs an **operational automation roadmap** for their marketing operations (scheduling, WhatsApp auto-replies, welcome emails, listening alerts, reporting, FAQ chatbots) rather than, or before, a single nurture sequence. It produces a realistic, affordable roadmap. Most East African clients are at Stage 1 (manual, disconnected); the goal is a practical sequence that saves 5–10 hours per week and improves consistency. This is not enterprise-grade automation but a structured build that reaches Stage 3 within 60–90 days.

Scope limits:

- Operational automation only. Content production automation belongs to [`playbook-content-production` AI-assisted production workflow](../../playbook-content-production/references/ai-assisted-production-workflow.md); paid advertising automation is out of scope entirely.
- Autonomous agents (PRAL/BDI architecture, Wave 3 agents): use [agentic-workflows-and-human-checkpoints.md](agentic-workflows-and-human-checkpoints.md).
- Trigger maps and nurture sequence timing stay in [trigger-and-sequence-design.md](trigger-and-sequence-design.md).

Source framework: Upadhyay (2024) *Generative AI for Marketing*, Kogan Page — a 10-step automation workflow and 8 task qualification factors.

## Inputs

Before generating any deliverable, ask the client for:

| # | Input | Notes |
|---|---|---|
| 1 | Business name | Trading name of the organisation |
| 2 | Industry | Sector (e.g. retail, hospitality, professional services, NGO) |
| 3 | Country / city | Location and primary market |
| 4 | Primary goal | What the client most wants automation to achieve (e.g. "stop missing enquiries after hours", "post consistently without daily effort", "send follow-up emails automatically") |
| 5 | Current tools | Every tool already in use: schedulers, email platforms, CRMs, WhatsApp Business or standard, website platform |
| 6 | Team size and technical comfort | How many people manage marketing, and how comfortable they are with new software |
| 7 | Monthly budget for tools | Approximate range in UGX or USD |
| 8 | Biggest pain point | Where the most time is lost in the current workflow |

## Decision rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| An automated step can publish, spend or expose data | Insert human approval and an auditable rollback point | Unsupervised high-impact automation |
| Candidate task passes fewer than 6 of the 8 qualification factors | Do not recommend automating it; flag borderline tasks with a risk note | Automation that costs more than it saves |
| Task fails Feasibility Test 3 (criticality) or 4 (intuitiveness) | Document a human fallback protocol alongside the automation | Silent failure on a critical task |
| Task varies by context, client or tone (fails repeatability) | Flag it as human-led | Inconsistent automated output |
| Low-frequency, low-time-cost task | Do not automate in the first 90 days | Effort spent on low-return builds |
| Client lacks a dedicated digital team or a monthly tool budget above UGX 500,000 | Target Stage 3; do not propose Stage 4 | Over-built, unmaintained automation |
| Stage 1–2 client with no explicit paid-tool budget | Default to free-tier tools | Tool spend the client cannot sustain |
| Tool has no documented free tier and no local payment method usable in Uganda | Do not recommend it | Tool the client cannot pay for |
| Task appears on the "must stay human" list | Mark it *Human only — do not automate* | Automated harm in sensitive situations |

## Procedure

### Step 1: Assess the automation maturity stage

Classify the client against the four stages (Upadhyay, 2024):

| Stage | Label | Characteristics |
|---|---|---|
| **1** | Basic | Manual everything; no scheduling; ad hoc posting; enquiries answered individually |
| **2** | Aligned | Scheduled posts; basic email automation; at least one connected tool |
| **3** | Multichannel | Content pipeline connected across platforms; auto-reporting; chatbot for FAQs |
| **4** | Automated | AI-generated content variants; behavioural triggers; continuous optimisation loops |

Design the roadmap to move the client from their current stage to **Stage 3**. State the current stage explicitly at the top of the roadmap and justify it with evidence from the input responses.

### Step 2: Qualify each task for automation

Apply the **8 qualification factors** (Upadhyay, 2024) to every candidate task:

1. **Cost**: is the automation cheaper than the human time it replaces? Include tool cost and set-up time, not just the monthly subscription.
2. **Resources**: do we have the tools and skills to maintain it reliably?
3. **Skillset**: does the team know how to set it up, or is training required first?
4. **Competitive position**: does it create a meaningful advantage, or is it simply hygiene?
5. **Sustainability**: will it keep working without constant maintenance? Rule: if it needs weekly manual intervention to function, it is not truly automated.
6. **Stack compatibility**: does it integrate with the tools the client already uses?
7. **Workforce support**: does the team accept it, or is there resistance? Automation that the team works around fails within weeks.
8. **Collateral impact**: does automating this task break anything else in the workflow? (e.g. auto-scheduling posts that then trigger manual reporting processes)

Recommend automation only for tasks that pass at least 6 of the 8. Flag borderline tasks with a note on the risk.

### Step 3: Apply the 4 feasibility tests

Before adding any task to the build plan, verify:

1. **Repeatability**: is the task identical every time? If it varies by context, client or tone, automation will produce inconsistencies; flag it as human-led.
2. **Predictability**: can the trigger and the desired outcome be defined in advance? "When someone submits a contact form → send welcome email" is predictable; "when a follower seems unhappy → respond with empathy" is not.
3. **Criticality**: what happens when the automation fails? High-criticality tasks (e.g. complaint handling, crisis response) must retain a human fallback at every step.
4. **Intuitiveness**: can a non-technical team member manage it day to day without calling a developer? If not, document the dependency and plan for it.

Tasks that fail Test 3 or 4 need a human fallback protocol alongside the automation; document both.

### Step 4: Build the automation priority matrix

Plot candidate tasks on a 2×2 matrix before sequencing the build plan:

|  | **High time cost** | **Low time cost** |
|---|---|---|
| **High frequency** | Automate first: highest ROI | Automate second: consistency gain |
| **Low frequency** | Automate third: strategic value | Automate last: low priority |

Use the matrix to sequence the build plan. Do not propose automating low-frequency, low-time-cost tasks in the first 90 days.

### Step 5: Recommend the tool stack

Match tools to the client's budget; default to free tier for Stage 1–2 clients unless the budget explicitly supports paid tools. Recommend only tools with a documented free tier or a local payment method accessible in Uganda (e.g. Visa, Mastercard, or MTN Mobile Money via Payoneer). Tool limits and prices below are as recorded in the source; verify current vendor terms before quoting.

**Free tier: Stage 2 baseline (UGX 0/month)**

| Function | Tool | Notes |
|---|---|---|
| Social scheduling | Meta Business Suite | Schedules Facebook and Instagram; free; available in Uganda |
| WhatsApp auto-reply | WhatsApp Business app | Free greeting and away messages; up to 50 Quick Replies |
| Email marketing | Mailchimp (free plan) | Up to 500 contacts; 1,000 sends/month |
| Reporting | Meta Insights + Google Sheets | Pull data manually into a monthly template |

**Starter paid tier (~UGX 50,000–150,000/month)**

| Function | Tool | Notes |
|---|---|---|
| Social scheduling | Buffer Essentials or Hootsuite Professional | Multi-platform; analytics included |
| Email marketing | Mailchimp Essentials or Brevo Starter | Higher send limits; automation sequences |
| WhatsApp chatbot | ManyChat Pro | WhatsApp automation flows; FAQ bots |
| Analytics dashboard | Notion or Google Sheets | Connected to platform exports |

**Growth tier (~UGX 150,000–500,000/month)**

| Function | Tool | Notes |
|---|---|---|
| CRM + email | HubSpot Starter | CRM, email, forms and pipeline in one platform |
| Social management | Sprout Social or Hootsuite Business | Full scheduling, listening and reporting |
| Chatbot + integrations | ManyChat Pro + Zapier | Cross-tool automation flows |
| Reporting | Google Looker Studio (free) | Connects to all sources; builds live dashboards |

### Step 6: Write the build plan

Deliver a prioritised, week-by-week sequence. Compress timing for Stage 2 clients; expand it for Stage 1 clients who need training first.

**Week 1: content scheduling**

- Set up Meta Business Suite and connect both the Facebook Page and the Instagram account.
- Schedule at least two weeks of content in advance before going live.
- Establish a weekly scheduling session (e.g. every Monday, 1 hour) as a standing calendar appointment.
- Confirm the content source: the client, a content plan document, or the [`11-content-calendar`](../../../pipeline/11-content-calendar/SKILL.md) output.

**Week 1: WhatsApp auto-reply**

- Switch from WhatsApp standard to WhatsApp Business if not already done.
- Write and activate a greeting message (sent to new contacts on first message).
- Write and activate an away message (sent outside business hours; define the hours).
- Create 5 Quick Replies for the most common enquiries, identified from the client's message history.
- Test all messages by sending from a personal number.

**Week 2: email welcome sequence**

- Set up Mailchimp (or the agreed email platform).
- Build a 3-email welcome sequence triggered automatically by a form opt-in:
  - Email 1 (immediate): thank you and what to expect.
  - Email 2 (Day 3): most useful resource or offer.
  - Email 3 (Day 7): invitation to engage (reply, book, visit).
- Connect the opt-in form to the client's website, or a Google Form if no website exists.
- Test the full sequence end to end before publishing.

**Week 3: social listening alert**

- Set up Google Alerts for the brand name, key product or service names and the top 2 competitors.
- Deliver alerts as a daily email digest (not real time, to reduce noise).
- Assign one team member to review the digest each morning and flag anything requiring a response.

**Week 4: monthly report automation**

- Build a Google Sheets reporting template with tabs for Facebook, Instagram, WhatsApp (manual), Email (Mailchimp export) and a Summary tab.
- Pre-fill formulas for reach, engagement rate, follower growth and email open rate.
- Set a recurring monthly calendar reminder (first Monday of each month) to populate and send the report.
- This is semi-automated, not fully automated; note the manual steps clearly.

**Month 2: chatbot FAQ automation**

- Extract the 10 most common questions received via WhatsApp Messenger over the past 90 days (ask the client to review their message history).
- Set up ManyChat flows for each question, with a clear escalation path to a human agent for anything the bot cannot resolve.
- Write escalation copy that acknowledges the bot's limit and sets a response-time expectation ("Our team will reply within 2 hours during business hours").
- Test every flow end to end, including failure paths.
- Review bot performance at 30 days and update flows based on missed conversations.

### Step 7: Mark what must stay human

Never automate these tasks. Flag them in the roadmap with the instruction *Human only — do not automate*:

- **Complaint responses**: need empathy, judgement and accountability.
- **Crisis communications**: need speed, authority and brand decision-making (see [`playbook-crisis-communications`](../../playbook-crisis-communications/SKILL.md)).
- **Any message with emotional content**: condolences, difficult news, conflict resolution.
- **Content strategy decisions**: platform mix, campaign themes, brand direction.
- **Client relationship conversations**: proposals, negotiations, renewals.
- **Community management in sensitive contexts**: political, cultural or religious topics.
- **Any response requiring local knowledge**: cultural references, local events, current affairs.

### Step 8: Add the maintenance schedule

Automation is not set-and-forget. Include this schedule in every roadmap as a standalone section.

| Cadence | Time | Tasks |
|---|---|---|
| Weekly | 15 minutes | Check the scheduling queue is populated at least two weeks ahead · Review chatbot missed conversations (ManyChat "Unhandled" folder or equivalent) · Check the Google Alerts digest for anything requiring a response |
| Monthly | 1 hour | Review auto-reply messages for accuracy (prices, hours and offers may have changed) · Review email sequence performance: open rate, click rate, unsubscribes · Pull and complete the Google Sheets monthly report · Check tool billing and confirm free-tier limits have not been exceeded |
| Quarterly | 2–3 hours | Full automation audit: what is working, what is not, what has broken silently · Retire automations that are no longer relevant · Review the tool stack against the current budget and upgrade where justified · Reassess the maturity stage and plan the next stage of the roadmap |

## Recipe: two-layer no-code automation stack

Combine AI with workflow automation in two layers (Erné, 2024):

- **Layer 1, automation (Zapier or Make.com)**: connects data sources (Google Sheets, Meta Business Suite, WhatsApp Business, Mailchimp, Airtable) and triggers actions, e.g. "When new lead form submitted → add to CRM → send welcome WhatsApp → notify account manager". Both tools have free tiers accessible to East African clients.
- **Layer 2, intelligence (Claude or ChatGPT API)**: analyses data ("Summarise this month's engagement data and identify 3 actionable insights"), generates content ("Draft a WhatsApp follow-up message for a lead who enquired about [service]") and routes decisions ("Classify this customer complaint as urgent/standard/low-priority").
- **Combined**: Zapier/Make handles the plumbing (moving data between tools); Claude/ChatGPT provides the intelligence (analysis and generation). Together they form a low-code AI consultancy engine.
- **East Africa-accessible starter stack**: Zapier Free (5 Zaps) + Google Sheets + Gmail + WhatsApp Business API (Twilio or WATI). Estimated monthly cost as recorded: $0–$50 USD depending on message volume; verify current plan limits.

## Recipe: multi-agent architecture

Rather than one general-purpose chatbot, advanced marketing operations use several specialised agents working in concert (Farri and Rosani, 2025; Nayebi, 2025):

| Agent | Role | Example tools |
|---|---|---|
| Research agent | Monitors trends, competitor activity, brand mentions | Perplexity, Brandwatch, Google Alerts |
| Copywriting agent | Drafts captions, emails, scripts from brief | Claude/ChatGPT with brand context |
| Analytics agent | Pulls performance data and generates insights | Meta Business Suite API, GA4 |
| Scheduling agent | Publishes approved content at optimal times | Buffer, Hootsuite, Later |

- **Coordination**: a human consultant is the orchestrator, reviewing each agent's outputs, resolving conflicts and making strategic decisions that need local knowledge or client-relationship context.
- **Implementation path**: start with one agent (typically the copywriting agent) and add agents one at a time as confidence grows.

## Recipe: HITL escalation protocol

Define thresholds so automation handles routine decisions and humans handle high-stakes ones (Nayebi, 2025):

| Decision type | AI handles | Human handles |
|---|---|---|
| Caption drafting | Draft | Final approval |
| Community management | Routine queries, FAQs | Complaints, crises, sensitive topics |
| Performance reporting | Data pull + narrative draft | Strategic commentary + client presentation |
| Campaign optimisation | A/B test suggestions | Budget reallocation decisions |
| Crisis response | Do not automate | Human only; use the crisis playbook |

Protocol: every automated workflow must have a defined escalation trigger. When the trigger fires, a human receives an alert with full context and a recommended action, and approves, modifies or overrides it. The AI never acts autonomously on sensitive decisions.

## Acceptance checklist

The roadmap meets the standard when it:

- [ ] Classifies the client's current maturity stage with evidence from the intake responses and states a clear target stage for the 90-day roadmap.
- [ ] Applies the 8 qualification factors to at least the top 3 candidate tasks, with a pass/fail or flag outcome for each.
- [ ] Sequences the build plan by priority (high-frequency, high-time-cost tasks first), with realistic week-by-week milestones a Stage 1–2 client can execute.
- [ ] Recommends tools matched to the client's budget, defaulting to free tiers and noting any tool payable only in USD with a local payment workaround.
- [ ] Distinguishes automated, semi-automated and human-only tasks, with no ambiguity about which need human intervention.
- [ ] Includes the maintenance schedule as a standalone, actionable section, not buried in the build plan.
- [ ] Stays culturally and operationally grounded in East Africa: WhatsApp as the primary customer channel, intermittent connectivity acknowledged, no tools unavailable or unaffordable in Uganda.
- [ ] Avoids scope creep: operational automation only; content production automation goes to `playbook-content-production` (AI-assisted production workflow); paid advertising automation is out of scope.

## Sources

- Upadhyay, N. (2024) *Generative AI for Marketing*. Kogan Page. Maturity stages, 8 task qualification factors and the 10-step automation workflow (Steps 1, 2 and 4).
- Erné, R. (2024) *AI-Powered Marketing* (verify: not found in Open Library, 29 Sep 2026). Two-layer no-code stack (Zapier/Make + Claude/ChatGPT).
- Farri, O. and Rosani, M. (2025) *Multi-Agent Systems for Marketing* (verify: not found in publisher or library catalogues, 29 Sep 2026), as cited in the retired source. Multi-agent architecture patterns. Note: [agentic-workflows-and-human-checkpoints.md](agentic-workflows-and-human-checkpoints.md) cites Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers*, Harvard Business Review Press (verified 29 Sep 2026). The in-text "Farri and Rosani, 2025" is not yet matched to a verified title (S13 citation backlog).
- Nayebi, M. (2025) *Human-in-the-Loop AI* (verify: not found in publisher or library catalogues, 29 Sep 2026), as cited in the retired source. HITL escalation protocols and agent orchestration. Note: the agentic reference cites Nayebi, F. (2025) *Foundations of Agentic AI for Retail*, Gradient Divergence (partly verified 29 Sep 2026: author Fatih Nayebi). The in-text "Nayebi, 2025" is not yet matched to a verified title (S13 citation backlog).
- Chaffey, D. and Ellis-Chadwick, F. (2022) *Digital Marketing: Strategy, Implementation and Practice*. 8th edn. Harlow: Pearson.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.

---
name: ai-agentic-marketing-workflows
description: Use when AI Agentic Marketing Workflows is needed to produce a workflow specification for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Agentic Marketing Workflows

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **workflow specification** and the supplied brief falls within ai agentic marketing workflows.

## Do Not Use When
- Use `ai-readiness-diagnostic` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| AI marketing use-case brief, intended human control point and success measure | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified workflow specification; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact workflow specification, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete workflow specification; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.
7. Apply [AI campaign trust, control, correction, and drift](references/ai-campaign-trust-control-correction-drift.md) before recommending any rollout or learning loop.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Workflow specification | Requester, client reviewer or delivery team | The workflow specification addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source/assumption register and completed release checklist | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.
- Separate the model, surrounding system, inputs, inferred inputs, outputs, human reviewer, and external action. Require specific disclosure, correction, escalation, drift monitoring, and a non-AI fallback.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested workflow specification, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.
- Describing an AI workflow as autonomous without a decision boundary, human escalation, correction path, audit trail, or rollback. **Fix:** complete the trust/control/drift reference or withhold the rollout recommendation.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [AI campaign trust, control, correction, and drift](references/ai-campaign-trust-control-correction-drift.md)
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## Purpose
Design and document autonomous AI marketing agent systems that perceive their
environment, reason about what action to take, act without human prompting, and
learn from outcomes. Output is an architecture specification, a chosen workflow
template with full HITL safeguards, and a wave-appropriate implementation plan.

This skill assumes the client has completed `ai-readiness-diagnostic` and has
an AI maturity wave score (1, 2, or 3). Do not recommend Wave 3 architecture
to a Wave 1 client without a phased roadmap.

## Required Inputs
Ask for all of the following before generating any output:

1. **Client business name** — trading name and legal entity if different
2. **Industry** — sector, product or service type
3. **Country / city** — defaults to Uganda if not specified
4. **Current AI maturity wave** — Wave 1, 2, or 3 (from `ai-readiness-diagnostic`; estimate if not available)
5. **Target workflow to automate** — select one primary: content / sentiment monitoring / reporting / customer service / campaign optimisation
6. **Available technical resources** — none / basic (can use no-code tools) / developer (can call APIs and self-host)

## Agentic vs Generative AI: The Critical Distinction
*Source: Nayebi (2025)*

Most clients conflate generative AI with agentic AI. Clarify the distinction
before designing any architecture.

**Generative AI is reactive.**
It waits for a human prompt, generates output, then stops. Every action
requires a human to initiate the cycle. This is Wave 1 and Wave 2 behaviour.

**Agentic AI is proactive.**
It monitors its environment continuously, reasons about what action to take,
executes that action, and updates its behaviour based on outcomes — without
waiting for a human prompt. This is Wave 3 behaviour.

This distinction determines the architecture, the tools, the data requirements,
and the risk controls needed. A business without clean engagement data or
developer resource is not ready for a full agentic stack.

**Wave guidance:**
- Wave 1 clients → rule-based automation (Zapier / Make.com triggers)
- Wave 2 clients → performance-triggered AI actions using analytics data
- Wave 3 clients → full PRAL agents with continuous monitoring and learning

Most East African businesses should reach Wave 2 (Predictive ML, with 3+ months
of clean data) before building Wave 3 agents.

## The PRAL Loop
*Source: Nayebi (2025)*

Every agentic system is built on the PRAL loop:
**Perceive → Reason → Act → Learn**

Map the client's chosen workflow to each stage before recommending tools.

| Stage | What the agent does | Marketing example |
|---|---|---|
| **Perceive** | Gathers data from its environment | Scans social mentions, reads engagement metrics, receives inbound WhatsApp messages |
| **Reason** | Processes data and decides what to do — using an LLM or rule-based logic | Classifies sentiment, identifies a content gap, detects a campaign underperforming |
| **Act** | Executes the decision | Drafts content, sends an alert, triggers a campaign boost, routes a message to a human |
| **Learn** | Updates its behaviour based on outcomes | Feeds performance data back into the next Perceive cycle; adjusts thresholds and templates |

Apply the PRAL loop explicitly when designing each workflow template. Label
each step so the client can see where human oversight sits.

## The BDI Model for Marketing Agents
*Source: Nayebi (2025)*

The BDI model — **Beliefs, Desires, Intentions** — maps naturally to marketing
strategy and is the clearest way to define an agent's decision boundary.

| Component | Definition | Marketing application |
|---|---|---|
| **Beliefs** | What the agent knows | Audience data, engagement history, brand guidelines, competitor positions, product catalogue |
| **Desires** | What the agent is trying to achieve | Business goals — leads, awareness, retention, revenue — expressed as KPIs |
| **Intentions** | How the agent plans to act | Campaign tactics, content formats, channel choices, timing rules, escalation thresholds |

**Prompt to use with client:**
> "Specify your agent's Beliefs (what data it has access to), Desires (what KPI
> it optimises for), and Intentions (what actions it can take). This defines the
> agent's decision boundary."

Document the BDI model before selecting any tool. An agent without a defined
decision boundary will act unpredictably.

## The OODA Cycle for Real-Time Decisions
Borrowed from military strategy (Boyd, 1976), OODA is the fastest decision loop
applicable to marketing agents operating in real-time social media environments.

**Observe → Orient → Decide → Act**

Faster OODA cycles = competitive advantage in fast-moving social media
environments where a delayed crisis response or missed trend costs engagement.

**Social listening agent example:**

- **Observe** — scan all mentions of the brand across Facebook, Instagram, X/Twitter, and Google every hour
- **Orient** — classify each mention by sentiment (positive / neutral / negative / crisis) and topic category
- **Decide** — apply rules: respond autonomously to positive enquiries; escalate negative mentions; flag crisis keywords immediately
- **Act** — post pre-approved response template, or send alert to human via WhatsApp/email with full context

OODA complements PRAL: PRAL describes the agent's architecture; OODA describes
the speed and logic of its decision-making in a single cycle.

## Five Agentic Workflow Templates
Select the template that matches the client's target workflow. Fully specify
the chosen template before recommending tools.

### 1. Content Pipeline Agent
**What it does:** Automates the content creation and publishing pipeline from
trend detection to post-performance feedback.

| Element | Detail |
|---|---|
| **Trigger** | Scheduled (daily/weekly) or event-driven (trending topic detected) |
| **Actions** | 1. Monitor trending topics and competitor content · 2. Generate draft content (caption, hashtags, image brief) · 3. Route draft to human for approval · 4. Publish approved content at optimal time · 5. Monitor post performance for 48 hours |
| **HITL point** | Human approves every draft before publishing — no autonomous publishing without review |
| **Learn step** | Performance data (reach, engagement rate, saves) fed back to refine future prompts and posting times |
| **Tools** | Claude API (drafting) + n8n or Make.com (orchestration) + Buffer/Hootsuite (scheduling) |
| **EA feasibility** | High — Wave 2 clients can implement with no-code tools |

### 2. Sentiment Monitoring Agent
**What it does:** Continuously scans social mentions, classifies sentiment, and
alerts the team when a threshold is crossed.

| Element | Detail |
|---|---|
| **Trigger** | Continuous (hourly scan) or keyword-event (brand name mentioned) |
| **Actions** | 1. Scan Facebook, Instagram, X/Twitter, Google reviews for brand mentions · 2. Classify mention: positive / neutral / negative / crisis · 3. Log all mentions in dashboard · 4. Alert team when negative threshold crossed (e.g., 3+ negative mentions in one hour) · 5. Suggest pre-approved response options |
| **HITL point** | Human selects and sends response — agent does not post responses autonomously |
| **Learn step** | Mis-classifications flagged by human; agent updates sentiment rules |
| **Tools** | Mention.com or Google Alerts (listening) + Claude API (classification) + n8n (routing) + WhatsApp Business API (alert delivery) |
| **EA feasibility** | High — Google Alerts + Claude API is accessible and low-cost |

### 3. Proactive Campaign Agent
**What it does:** Monitors engagement metrics and triggers a targeted response
campaign when performance drops below threshold.

| Element | Detail |
|---|---|
| **Trigger** | Metric threshold (engagement rate drops below X%, or follower growth stalls for N days) |
| **Actions** | 1. Pull platform analytics daily · 2. Compare against baseline benchmarks · 3. Detect underperformance · 4. Generate campaign response options (content boost, new format, re-engagement post) · 5. Present options to human for approval · 6. Execute approved option · 7. Report results after 7 days |
| **HITL point** | Human approves the campaign response before any content is published |
| **Learn step** | Successful response tactics stored; agent prioritises them in future recommendations |
| **Tools** | Platform analytics API + Claude API (analysis and drafting) + Make.com (orchestration) + Buffer (publishing) |
| **EA feasibility** | Medium — requires Wave 2 data maturity and API access to platform analytics |

### 4. Multi-Agent Reporting System
**What it does:** A team of specialised agents collaborates to produce the
monthly performance report with minimal human effort.

| Element | Detail |
|---|---|
| **Trigger** | Scheduled (last day of the month) |
| **Actions** | 1. **Data agent** — pulls platform statistics from all active channels · 2. **Analysis agent** — identifies patterns, anomalies, and top-performing content · 3. **Writing agent** — drafts narrative report with insights and recommendations · 4. **Human consultant** — reviews, edits, and presents to client |
| **HITL point** | Human reviews the full draft before delivery; no automated client-facing report |
| **Learn step** | Human edits tracked; writing agent refines its narrative style and recommendation quality |
| **Tools** | Platform APIs (data) + Claude API (analysis and writing) + n8n (orchestration) + Google Docs / Notion (output) |
| **EA feasibility** | Medium — high value but requires API access and developer setup for data pulls |

### 5. WhatsApp Response Agent
**What it does:** Classifies inbound WhatsApp messages, routes them to the
correct response path, and handles routine enquiries autonomously.

| Element | Detail |
|---|---|
| **Trigger** | Inbound WhatsApp Business message received |
| **Actions** | 1. Receive and classify message (enquiry / complaint / order / other) · 2. Route to: decision tree (simple FAQ) / Claude API (nuanced enquiry) / human agent (complaint or high value) · 3. Respond or escalate · 4. Log interaction with timestamp and classification |
| **HITL point** | All complaints and high-value sales enquiries routed to human immediately; agent does not resolve complaints autonomously |
| **Learn step** | Mis-routed messages flagged; classification rules updated monthly |
| **Tools** | WhatsApp Business API + Claude API (classification and response drafting) + n8n (routing logic) |
| **EA feasibility** | High — WhatsApp penetration in EA makes this the highest-ROI agentic workflow for most clients |

## HITL Safeguard Design
*Source: Nayebi (2025)*

Every agentic workflow must define four safeguard components before going live.
Include this section in every workflow specification delivered to the client.

**1. Autonomous decision boundary**
Define what the agent can decide and act on without human review. Limit this to
decisions that are: low-risk, routine, reversible, and within a defined value
threshold (e.g., scheduling a post, classifying a mention, logging a message).

**2. Escalation triggers**
Define what forces the agent to stop and wait for a human. Escalation is
mandatory when a decision is: high-risk, irreversible (e.g., publishing to
public), sensitive (crisis keywords, complaints, legal mentions), or above a
value threshold (e.g., enquiry worth over UGX 500,000).

**3. Escalation mechanism**
Specify: how the human is alerted (WhatsApp message, email, Slack), what
information they receive (full context, agent's recommended options), the
expected response time, and the override protocol if no response is received.

**4. Audit trail**
Every agent action must be logged with: timestamp, action taken, data that
triggered the action, reasoning or rule applied, and outcome. This log is
reviewed monthly to improve agent performance and demonstrate accountability.

## Three-Wave Implementation Roadmap
Match the roadmap recommendation to the client's current wave.

| Wave | Readiness criteria | What to build | Effort |
|---|---|---|---|
| **Wave 1** — Automation | No analytics data required; any technical level | Zapier or Make.com automations that trigger AI content drafts on a schedule. Rule-based, no learning, no API calls. | 1–2 days setup |
| **Wave 2** — Performance-triggered | 3+ months of clean engagement data; basic technical resource | Connect analytics data to AI for performance-triggered actions (e.g., engagement drop → draft new content). Requires platform data export or basic API access. | 1–2 weeks setup |
| **Wave 3** — Full agentic | Clean data, developer resource, HITL safeguards in place | Full PRAL agents with continuous monitoring, LLM reasoning, and feedback loops. Requires API access, self-hosted orchestration (n8n), and ongoing maintenance. | 4–8 weeks minimum |

Do not propose Wave 3 to a Wave 1 client without a phased roadmap that moves
them through Wave 2 first.

## Tool Stack Options
Recommend tools based on the client's technical resources and budget.

| Tool | Role in agentic stack | EA accessibility | Approx. cost |
|---|---|---|---|
| Claude API | LLM reasoning layer — classification, drafting, analysis | Yes — API account required | Pay-per-token |
| n8n | Workflow orchestration (self-hostable, open source) | Yes — developer resource needed for self-hosting | Free (self-hosted); from $20/month (cloud) |
| Zapier AI | No-code workflow automation with AI steps | Yes — browser only, no dev required | Free tier; from $19.99/month |
| Make.com | Visual no-code workflow builder | Yes — browser only, no dev required | Free tier; from $9/month |
| Hootsuite / Buffer | Publishing and scheduling layer | Yes — widely used in EA | From $15/month |
| Brandwatch / Mention | Social listening layer for sentiment monitoring | Limited — pricing is a barrier for small clients | From $99/month |
| WhatsApp Business API | Inbound message routing and response | Yes — high EA penetration; via Meta or third-party | From $0 (first 1,000 conversations/month free) |

For Wave 1 clients with no technical resource: Zapier or Make.com + Claude
(via ChatGPT or Claude.ai interface, not API) is the most accessible entry point.

For Wave 3 clients with developer resource: n8n (self-hosted) + Claude API is
the recommended EA-feasible stack.

## Quality Criteria
Output meets standard when it satisfies all of the following:

- Client's current AI maturity wave is identified and a wave-appropriate architecture is recommended — no Wave 3 proposal for a Wave 1 client without a phased roadmap
- At least one agentic workflow template is selected and fully specified: trigger, PRAL mapping, actions, HITL point, learn step, and tools
- The PRAL loop is explicitly mapped for the chosen workflow — each stage labelled
- The BDI model is documented: Beliefs (data sources), Desires (KPI optimised), and Intentions (actions the agent can take)
- HITL safeguards are defined: autonomous decision boundary, escalation triggers, escalation mechanism, and audit trail
- Tool stack is recommended based on the client's technical resources and budget with EA accessibility noted
- EA feasibility is assessed — WhatsApp-based and no-code workflows prioritised for clients without developer resource
- Autonomy level, allowed-action table, eval set, run logging fields, and kill-switch owner are defined before any autonomous action is recommended

## References
- Nayebi, F. (2025) *Foundations of Agentic AI for Retail*. Gradient Divergence.
- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn. Stanford University Press.
- Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers*. Harvard Business Review Press.
- `references/agentic-marketing-operating-model.md` - source-synthesised hardening rules for production marketing agents.

# Agentic Workflows and Human Checkpoints

Merged from skills/ai-marketing/ai-agentic-marketing-workflows on 2026-09-29 at 7c60138; preservation map: [ai-agentic-marketing-workflows.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/ai-agentic-marketing-workflows.md)

## When to use this reference

Use it when the automation brief goes beyond trigger-and-sequence automation: the client wants an AI agent that perceives its environment, reasons about what to do, acts without a human prompt and learns from outcomes. The deliverable is a **workflow specification**: an architecture description, one fully specified workflow template with human-in-the-loop (HITL) safeguards, and an implementation plan matched to the client's AI maturity wave.

- It assumes the client has completed [`ai-readiness-diagnostic`](../../../ai-marketing/ai-readiness-diagnostic/SKILL.md) and has a maturity wave score (1, 2 or 3). If the real deliverable is the readiness score itself, route there instead.
- Do not recommend Wave 3 architecture to a Wave 1 client without a phased roadmap.
- Before recommending any rollout or learning loop, apply [AI campaign trust, control, correction, and drift](ai-campaign-trust-control-correction-drift.md). For autonomy levels, tool gating, brand memory, evaluation and deployment stages, read [agentic-marketing-operating-model.md](agentic-marketing-operating-model.md).
- Rule-based sequences, trigger maps and the task-by-task automation roadmap stay in the main playbook and [ai-automation-recipes.md](ai-automation-recipes.md).

## Inputs

Ask for all of the following before generating any output:

| # | Input | Notes |
|---|---|---|
| 1 | Client business name | Trading name, and legal entity if different |
| 2 | Industry | Sector, product or service type |
| 3 | Country / city | Defaults to Uganda if not specified |
| 4 | Current AI maturity wave | Wave 1, 2 or 3 from `ai-readiness-diagnostic`; estimate if not available and label the estimate |
| 5 | Target workflow to automate | Select one primary: content / sentiment monitoring / reporting / customer service / campaign optimisation |
| 6 | Available technical resources | None / basic (can use no-code tools) / developer (can call APIs and self-host) |
| 7 | Intended human control point and success measure | From the use-case brief; stop and request it if missing |
| 8 | Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner; state assumptions, never invent names, prices, results or approvals |
| 9 | Evidence behind any performance, platform or research claim | Traceable export, URL, document or named source; otherwise draft the narrowest reviewable version and flag the gap |

## Decision rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the **lowest viable automation level** and define its human approval gate | Automating an unsafe or unevaluable marketing process |
| Client is Wave 1 | Rule-based automation (Zapier / Make.com triggers) | Agent built on data that does not exist |
| Client is Wave 2 | Performance-triggered AI actions using analytics data | Over-building before data supports learning |
| Client is Wave 3 | Full PRAL agents with continuous monitoring and learning | Under-using proven data and developer capacity |
| Wave 3 proposed for a Wave 1 client | Only with a phased roadmap that moves the client through Wave 2 first | Skipping the data-maturity stage |
| No clean engagement data or no developer resource | Not ready for a full agentic stack; stay at Wave 1–2 | Unmaintainable agent |
| A workflow is described as autonomous without decision boundary, escalation, correction path, audit trail or rollback | Complete the trust/control/drift reference or withhold the rollout recommendation | Unaccountable autonomy |
| Autonomy level, allowed-action table, eval set, run-logging fields or kill-switch owner undefined | Do not recommend any autonomous action | Autonomy granted before it is earned |

Most East African businesses should reach Wave 2 (predictive machine learning, with 3+ months of clean data) before building Wave 3 agents.

## Procedure

1. **Separate generative from agentic AI with the client.** Most clients conflate the two (Nayebi, 2025).
   - *Generative AI is reactive.* It waits for a human prompt, generates output, then stops; every action needs a human to start the cycle. This is Wave 1 and Wave 2 behaviour.
   - *Agentic AI is proactive.* It monitors its environment continuously, reasons about what action to take, executes that action and updates its behaviour from outcomes without waiting for a prompt. This is Wave 3 behaviour.
   - The distinction sets the architecture, tools, data requirements and risk controls.
2. **Map the chosen workflow to the PRAL loop** (Perceive → Reason → Act → Learn; Nayebi, 2025) before recommending tools. Label each step so the client can see where human oversight sits.
3. **Document the BDI model** (Beliefs, Desires, Intentions; Nayebi, 2025) before selecting any tool. An agent without a defined decision boundary will act unpredictably.
4. **Where the workflow runs in real time, specify its OODA cycle** (Observe → Orient → Decide → Act; Boyd, 1976).
5. **Select one of the five workflow templates** and fully specify it (trigger, PRAL mapping, actions, HITL point, learn step, tools) before recommending tools.
6. **Define the four HITL safeguards** and include them in every workflow specification delivered to the client.
7. **Choose the wave-appropriate roadmap** and the tool stack that fits the client's technical resources and budget, noting East African accessibility.
8. **Separate the parts of the system** in the specification: model, surrounding system, inputs, inferred inputs, outputs, human reviewer and external action. Require specific disclosure, correction, escalation, drift monitoring and a non-AI fallback.
9. **Test and deliver.** Check against the decision rules, the checklist below and the `anti-ai-slop` gate; narrow or qualify unsupported portions. Deliver with evidence, assumptions, unassessed checks and the next approval or verification step.

## PRAL loop template

| Stage | What the agent does | Marketing example |
|---|---|---|
| **Perceive** | Gathers data from its environment | Scans social mentions, reads engagement metrics, receives inbound WhatsApp messages |
| **Reason** | Processes data and decides what to do, using an LLM or rule-based logic | Classifies sentiment, identifies a content gap, detects a campaign underperforming |
| **Act** | Executes the decision | Drafts content, sends an alert, triggers a campaign boost, routes a message to a human |
| **Learn** | Updates its behaviour based on outcomes | Feeds performance data back into the next Perceive cycle; adjusts thresholds and templates |

## BDI decision-boundary template

The BDI model maps naturally to marketing strategy and is the clearest way to define an agent's decision boundary.

| Component | Definition | Marketing application |
|---|---|---|
| **Beliefs** | What the agent knows | Audience data, engagement history, brand guidelines, competitor positions, product catalogue |
| **Desires** | What the agent is trying to achieve | Business goals (leads, awareness, retention, revenue) expressed as KPIs |
| **Intentions** | How the agent plans to act | Campaign tactics, content formats, channel choices, timing rules, escalation thresholds |

Prompt to use with the client: *Specify your agent's Beliefs (what data it has access to), Desires (what KPI it optimises for) and Intentions (what actions it can take). This defines the agent's decision boundary.*

## OODA cycle for real-time decisions

Borrowed from military strategy (Boyd, 1976), OODA is the fastest decision loop that applies to marketing agents in real-time social media. Faster OODA cycles give a competitive advantage where a delayed crisis response or a missed trend costs engagement. PRAL describes the agent's architecture; OODA describes the speed and logic of its decision-making in a single cycle.

Social listening agent example:

- **Observe**: scan all brand mentions across Facebook, Instagram, X/Twitter and Google every hour.
- **Orient**: classify each mention by sentiment (positive / neutral / negative / crisis) and topic category.
- **Decide**: apply rules; respond autonomously to positive enquiries, escalate negative mentions, flag crisis keywords immediately.
- **Act**: post a pre-approved response template, or send an alert to a human via WhatsApp/email with full context.

## Five agentic workflow templates

### 1. Content pipeline agent

Automates content creation and publishing from trend detection to post-performance feedback.

| Element | Detail |
|---|---|
| Trigger | Scheduled (daily/weekly) or event-driven (trending topic detected) |
| Actions | 1. Monitor trending topics and competitor content · 2. Generate draft content (caption, hashtags, image brief) · 3. Route draft to human for approval · 4. Publish approved content at optimal time · 5. Monitor post performance for 48 hours |
| HITL point | Human approves every draft before publishing; no autonomous publishing without review |
| Learn step | Performance data (reach, engagement rate, saves) fed back to refine future prompts and posting times |
| Tools | Claude API (drafting) + n8n or Make.com (orchestration) + Buffer/Hootsuite (scheduling) |
| EA feasibility | High: Wave 2 clients can implement with no-code tools |

### 2. Sentiment monitoring agent

Continuously scans social mentions, classifies sentiment and alerts the team when a threshold is crossed.

| Element | Detail |
|---|---|
| Trigger | Continuous (hourly scan) or keyword event (brand name mentioned) |
| Actions | 1. Scan Facebook, Instagram, X/Twitter and Google reviews for brand mentions · 2. Classify mention: positive / neutral / negative / crisis · 3. Log all mentions in a dashboard · 4. Alert team when the negative threshold is crossed (e.g. 3+ negative mentions in one hour) · 5. Suggest pre-approved response options |
| HITL point | Human selects and sends the response; the agent does not post responses autonomously |
| Learn step | Misclassifications flagged by a human; agent updates sentiment rules |
| Tools | Mention.com or Google Alerts (listening) + Claude API (classification) + n8n (routing) + WhatsApp Business API (alert delivery) |
| EA feasibility | High: Google Alerts + Claude API is accessible and low-cost |

### 3. Proactive campaign agent

Monitors engagement metrics and triggers a targeted response campaign when performance drops below threshold.

| Element | Detail |
|---|---|
| Trigger | Metric threshold (engagement rate drops below X%, or follower growth stalls for N days) |
| Actions | 1. Pull platform analytics daily · 2. Compare against baseline benchmarks · 3. Detect underperformance · 4. Generate campaign response options (content boost, new format, re-engagement post) · 5. Present options to human for approval · 6. Execute approved option · 7. Report results after 7 days |
| HITL point | Human approves the campaign response before any content is published |
| Learn step | Successful response tactics stored; agent prioritises them in future recommendations |
| Tools | Platform analytics API + Claude API (analysis and drafting) + Make.com (orchestration) + Buffer (publishing) |
| EA feasibility | Medium: requires Wave 2 data maturity and API access to platform analytics |

### 4. Multi-agent reporting system

A team of specialised agents produces the monthly performance report with minimal human effort.

| Element | Detail |
|---|---|
| Trigger | Scheduled (last day of the month) |
| Actions | 1. **Data agent** pulls platform statistics from all active channels · 2. **Analysis agent** identifies patterns, anomalies and top-performing content · 3. **Writing agent** drafts the narrative report with insights and recommendations · 4. **Human consultant** reviews, edits and presents to the client |
| HITL point | Human reviews the full draft before delivery; no automated client-facing report |
| Learn step | Human edits tracked; writing agent refines its narrative style and recommendation quality |
| Tools | Platform APIs (data) + Claude API (analysis and writing) + n8n (orchestration) + Google Docs / Notion (output) |
| EA feasibility | Medium: high value but requires API access and developer set-up for data pulls |

### 5. WhatsApp response agent

Classifies inbound WhatsApp messages, routes them to the correct response path and handles routine enquiries autonomously.

| Element | Detail |
|---|---|
| Trigger | Inbound WhatsApp Business message received |
| Actions | 1. Receive and classify message (enquiry / complaint / order / other) · 2. Route to: decision tree (simple FAQ) / Claude API (nuanced enquiry) / human agent (complaint or high value) · 3. Respond or escalate · 4. Log interaction with timestamp and classification |
| HITL point | All complaints and high-value sales enquiries routed to a human immediately; the agent does not resolve complaints autonomously |
| Learn step | Misrouted messages flagged; classification rules updated monthly |
| Tools | WhatsApp Business API + Claude API (classification and response drafting) + n8n (routing logic) |
| EA feasibility | High: WhatsApp penetration in East Africa makes this the highest-ROI agentic workflow for most clients |

## HITL safeguard design

Every agentic workflow must define four safeguard components before going live (Nayebi, 2025).

| Safeguard | What to specify |
|---|---|
| 1. Autonomous decision boundary | What the agent can decide and act on without human review. Limit it to decisions that are low-risk, routine, reversible and within a defined value threshold (e.g. scheduling a post, classifying a mention, logging a message). |
| 2. Escalation triggers | What forces the agent to stop and wait for a human. Escalation is mandatory when a decision is high-risk, irreversible (e.g. publishing to public), sensitive (crisis keywords, complaints, legal mentions) or above a value threshold (e.g. an enquiry worth over UGX 500,000). |
| 3. Escalation mechanism | How the human is alerted (WhatsApp message, email, Slack), what information they receive (full context, the agent's recommended options), the expected response time, and the override protocol if no response is received. |
| 4. Audit trail | Every agent action logged with timestamp, action taken, data that triggered the action, reasoning or rule applied, and outcome. Review the log monthly to improve agent performance and demonstrate accountability. |

## Three-wave implementation roadmap

Match the roadmap to the client's current wave.

| Wave | Readiness criteria | What to build | Effort |
|---|---|---|---|
| **Wave 1**: Automation | No analytics data required; any technical level | Zapier or Make.com automations that trigger AI content drafts on a schedule. Rule-based, no learning, no API calls. | 1–2 days set-up |
| **Wave 2**: Performance-triggered | 3+ months of clean engagement data; basic technical resource | Connect analytics data to AI for performance-triggered actions (e.g. engagement drop → draft new content). Requires platform data export or basic API access. | 1–2 weeks set-up |
| **Wave 3**: Full agentic | Clean data, developer resource, HITL safeguards in place | Full PRAL agents with continuous monitoring, LLM reasoning and feedback loops. Requires API access, self-hosted orchestration (n8n) and ongoing maintenance. | 4–8 weeks minimum |

Do not propose Wave 3 to a Wave 1 client without a phased roadmap that moves them through Wave 2 first.

## Tool stack options

Recommend tools by the client's technical resources and budget. Prices and free-tier limits are volatile: verify on the vendor's current pricing page before quoting them to a client.

| Tool | Role in agentic stack | EA accessibility | Approx. cost (as recorded in the source) |
|---|---|---|---|
| Claude API | LLM reasoning layer: classification, drafting, analysis | Yes; API account required | Pay-per-token |
| n8n | Workflow orchestration (self-hostable, open source) | Yes; developer resource needed for self-hosting | Free (self-hosted); from $20/month (cloud) |
| Zapier AI | No-code workflow automation with AI steps | Yes; browser only, no developer required | Free tier; from $19.99/month |
| Make.com | Visual no-code workflow builder | Yes; browser only, no developer required | Free tier; from $9/month |
| Hootsuite / Buffer | Publishing and scheduling layer | Yes; widely used in East Africa | From $15/month |
| Brandwatch / Mention | Social listening layer for sentiment monitoring | Limited; pricing is a barrier for small clients | From $99/month |
| WhatsApp Business API | Inbound message routing and response | Yes; high East African penetration; via Meta or a third party | From $0 (first 1,000 conversations/month free, as recorded; verify Meta's current pricing model before quoting) |

- Wave 1 clients with no technical resource: Zapier or Make.com + Claude (through the ChatGPT or Claude.ai interface, not the API) is the most accessible entry point.
- Wave 3 clients with developer resource: n8n (self-hosted) + Claude API is the recommended East Africa-feasible stack.

## Acceptance checklist

The workflow specification meets the standard when:

- [ ] The client's current AI maturity wave is identified and a wave-appropriate architecture is recommended; no Wave 3 proposal for a Wave 1 client without a phased roadmap.
- [ ] At least one agentic workflow template is selected and fully specified: trigger, PRAL mapping, actions, HITL point, learn step and tools.
- [ ] The PRAL loop is explicitly mapped for the chosen workflow, each stage labelled.
- [ ] The BDI model is documented: Beliefs (data sources), Desires (KPI optimised) and Intentions (actions the agent can take).
- [ ] HITL safeguards are defined: autonomous decision boundary, escalation triggers, escalation mechanism and audit trail.
- [ ] The tool stack matches the client's technical resources and budget, with East African accessibility noted.
- [ ] East African feasibility is assessed; WhatsApp-based and no-code workflows are prioritised for clients without developer resource.
- [ ] Autonomy level, allowed-action table, eval set, run-logging fields and kill-switch owner are defined before any autonomous action is recommended.
- [ ] Model, surrounding system, inputs, inferred inputs, outputs, human reviewer and external action are separated, with disclosure, correction, escalation, drift monitoring and a non-AI fallback.

## Sources

- Boyd, J. (1976) OODA decision cycle, as applied to real-time marketing agents.
- Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers*. Harvard Business Review Press.
- Nayebi, F. (2025) *Foundations of Agentic AI for Retail*. Gradient Divergence.
- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn. Stanford University Press.
- [agentic-marketing-operating-model.md](agentic-marketing-operating-model.md): source-synthesised hardening rules for production marketing agents.
- [ai-campaign-trust-control-correction-drift.md](ai-campaign-trust-control-correction-drift.md): trust, control, correction and drift fields.

# Agentic Marketing Operating Model

Self-contained synthesis prepared from supplied agentic AI, AI shift, and prompt source material. Use it to harden marketing-agent designs beyond demo workflows.

## Table Of Contents

- Autonomy ladder for marketing
- Agentic workflow selection
- Tool and action gating
- Memory, brand knowledge, and retrieval
- Evaluation and observability
- Deployment stages

## Autonomy Ladder For Marketing

| Level | Marketing authority | Examples | Required control |
|---|---|---|---|
| 0 Draft-only | Produces drafts and analysis | Captions, reports, reply drafts | Human publishes/sends |
| 1 Recommend | Recommends actions | Boost recommendation, content gap, lead priority | Human approves action |
| 2 Supervised act | Acts in low-risk systems | Tag CRM lead, schedule draft, send internal alert | Approval for external messages/spend |
| 3 Conditional autonomy | Acts within pre-approved limits | Pause weak ad, route FAQ, create report | Budget cap, escalation, daily sampling |
| 4 Managed autonomy | Owns an outcome | Always-on lead triage or campaign optimisation | Audit cadence, kill switch, incident drill |

Do not jump from prompt use to autonomous publishing or paid-spend control. Autonomy must be earned through measured performance.

## Agentic Workflow Selection

Use agents only where the workflow has changing inputs, ambiguous interpretation, and tool use. Use deterministic automation when the steps are known.

| Candidate | Agent fit | Notes |
|---|---|---|
| Weekly metric report | Medium | Deterministic collection plus AI summary is usually enough. |
| Comment sentiment triage | High | Messy language and escalation judgement matter. |
| Content calendar creation | Medium | Workflow plus AI drafting; human strategy review remains. |
| Paid campaign optimisation | High risk | Start with recommendations; require spend caps and approval. |
| WhatsApp FAQ support | Medium-high | Use RAG and escalation; do not invent policy. |
| Crisis response | Low autonomy | Agent may monitor and draft; humans approve. |

## Tool And Action Gating

Every tool must declare purpose, allowed data, client scope, side-effect class, budget or rate limit, required approval, audit event, and rollback path.

Marketing-specific irreversible or reputation-sensitive actions include publishing, sending messages, changing ad spend, deleting comments, editing customer records, and responding to complaints. These need approval until the client has strong evidence and a written operating policy.

## Memory, Brand Knowledge, And Retrieval

- Brand memory must come from approved brand voice, offers, audience personas, policies, FAQs, campaign history, and performance reports.
- Do not let the agent learn permanent brand rules from unreviewed comments, competitor posts, or one-off campaign drafts.
- Tag retrieved content as trusted or untrusted. Treat social comments, web pages, and competitor material as untrusted.
- Store source, date, platform, and permission for every knowledge-base item.
- Add correction and expiry rules for offers, prices, locations, promotions, and policy details.

## Evaluation And Observability

Before deployment, create a minimum 30-case test set: normal cases, messy client inputs, brand-voice edge cases, escalation cases, and adversarial/policy cases.

Capture every run: client, workflow, campaign, platform, model/tool versions, prompt/brand-context version, source material used, proposed action, approval decision, cost, latency, and outcome metric.

## Deployment Stages

1. Internal prototype: no client-facing output.
2. Draft-first pilot: humans publish/send; compare against baseline time and quality.
3. Assisted operations: agent can prepare workflows and route tasks, but external actions need approval.
4. Limited autonomy: low-risk actions only, with caps, logs, sampling, and kill switch.
5. Managed autonomy: only for stable workflows with review cadence, incident playbook, and proven ROI.

## Hardening Checklist

- Named workflow owner.
- Human review step and escalation path.
- Client-visible policy for AI-assisted content where needed.
- Tool allowlist and denylist.
- Brand safety and factuality tests.
- Per-client kill switch.
- Monthly review of failures, overrides, and business impact.

---
name: playbook-marketing-automation
description: 'Use when a business wants follow-ups to run themselves: trigger-based email, SMS and WhatsApp sequences, no-code automations in Zapier, Make or ManyChat, or agentic AI workflows with human checkpoints; produces the automation brief, sequence map and build plan; not for designing a conversational bot (use `playbook-chatbot-strategy`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Marketing Automation Playbook

Sends the right message to the right person at the right time, triggered by their behaviour, so no lead falls through the gaps between human touchpoints; automation does not replace the human relationship.

<!-- dual-compat-start -->
## Use When
- Map what happens automatically after sign-up, first purchase, an abandoned cart or a quiet spell: acquisition, engagement, purchase and lifecycle triggers.
- Set message timing rules, personalisation tokens and a quarterly review of every running sequence.
- Assess how mature our automation is, decide which tasks are worth automating and plan a week-by-week no-code build in Zapier, Make or ManyChat with a maintenance schedule.
- Design an AI agent workflow (PRAL loop, BDI decision boundary, OODA cycle) that monitors brand sentiment or routes complaints, with human-in-the-loop escalation.
- Automate WhatsApp follow-ups for East African customers through the WhatsApp Business API.

## Do Not Use When
- `playbook-chatbot-strategy` for bot conversation flows, FAQ answers and human handoff in the inbox.
- `07-email-marketing-strategy` for the email programme, list building and lifecycle strategy.
- `meta-tools-stack-evaluation` for choosing or replacing the software stack.
- Stop before switching on live sequences, connecting customer lists or letting an agent act without a human checkpoint and the client's written approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry and country/city | Client brief | Yes | Default the market to Uganda/East Africa; ask for name and sector. |
| Primary goal (convert leads, nurture to first purchase, re-engage lapsed customers, onboard clients) | Client owner | Yes | Stop; sequences cannot be scoped without the goal. |
| Current follow-up method and sales cycle length | Sales or client team | Yes | Assume nothing formal is in place and label the timing model provisional. |
| Primary channel: email, WhatsApp or both | Client | Yes | Design both paths for EA clients and let contacts self-select. |
| Technology in use (CRM, email platform, automation tool, WhatsApp App or API) | Client or delivery owner | Yes | Recommend one tool with setup notes and mark integration checks `not assessed`. |
| Automation maturity, task list and AI-agent brief | Delivery owner | For roadmap or agent work | Use the maturity and qualification steps in the AI recipes before recommending any agent. |

## Workflow

1. Ask the intake questions in [trigger and sequence design](references/trigger-and-sequence-design.md) and confirm the owner and approval boundary; stop if the goal or owner is missing.
2. Map all four trigger categories (acquisition, engagement, purchase, lifecycle) against the business model and mark which are in scope for the first phase.
3. Write one sequence per in-scope trigger on the fixed timing model (immediate, Day 1–3, 4–7, 8–14, 15–30, Day 31 onwards), plus a parallel WhatsApp path for EA clients.
4. Apply the message timing rules and human-handover protocol, then list the personalisation tokens and check which the sign-up flow captures.
5. For a no-code or AI roadmap, qualify tasks with [AI automation recipes](references/ai-automation-recipes.md); for an agent, specify it at the lowest viable wave with [agentic workflows and human checkpoints](references/agentic-workflows-and-human-checkpoints.md).
6. Recommend one platform and book the first four quarterly reviews.
7. Run the quality checks and the anti-slop gate; correct any failed item and rerun before handover. Nothing goes live without written client approval.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Trigger map across the four categories | Client owner | Every category assessed; first-phase triggers marked. |
| Written sequences and parallel WhatsApp sequence | Delivery team | Each follows the timing model, 24-hour gap and 8am–8pm EAT window; WhatsApp messages are 50–150 words with one CTA. |
| Personalisation token list and platform recommendation | Delivery team | Tokens tested in the chosen platform; one tool named with setup notes. |
| Quarterly review schedule | Client owner | Dates set for the first four reviews. |
| Automation roadmap or agent specification (when requested) | Client owner and approver | Human-only tasks stay manual; every agent action has a HITL checkpoint. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Token and trigger test record | Table per sequence | Each token and trigger is tested in the platform or marked `not assessed`. |
| Human handover protocol | Short procedure in the brief | Names who takes replies and the 2-hour assignment target before the first sequence goes live. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Switching on sequences, importing customer lists and giving an agent action rights each need written client approval.

## Degraded Mode

Without the primary goal and channel, return the narrowest qualified result and mark the affected checks `not assessed`. A generic trigger map and the timing model can still be delivered, with sequence copy held until the goal is confirmed.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A journey trigger is ambiguous or untested | Keep the step manual until the trigger and rollback are proven. | Wrong-message automation. |
| A contact replies to any automated message | Remove them from the sequence at once and assign a human within 2 hours. | Automation that feels disrespectful and robotic. |
| A message would land outside 8am–8pm local time or within 24 hours of the previous one | Requeue it inside the window and after the gap. | Intrusive messages and higher opt-outs. |
| The client needs scheduled broadcasts or sequences on WhatsApp | Use the WhatsApp Business API via an approved Business Solution Provider; the free App supports only greeting, away and quick replies. | A plan the chosen tool cannot run. |
| The client needs an operational automation roadmap (maturity stage, task qualification, tool tiers, build plan, maintenance) | Apply the AI automation recipes; keep human-only tasks manual. | Automating tasks that fail qualification or must stay human. |
| The brief asks for an AI agent that acts or learns without a human prompt | Specify it with the agentic workflows reference at the lowest viable wave, with HITL safeguards. | Unbounded agent autonomy. |
| An action publishes, spends, contacts people or changes production state | Require explicit approval before action. | Unauthorised external impact. |

## Quality Standards

- Trigger events are fully mapped before sequence content is written; the automation logic is confirmed before a single message is drafted.
- All four trigger categories are assessed for relevance; sequences are designed only for triggers actually in use.
- A WhatsApp path is designed alongside email for every EA client; no email-only default.
- All automated messages are timed for delivery within local business hours (8am–8pm EAT).
- The manual handover protocol for replies is in place before the first sequence goes live.
- Personalisation tokens are tested and confirmed functional in the chosen platform before any sequence is activated.
- The quarterly review schedule is booked and confirmed; sequences without a review date decay and go stale.

## Anti-Patterns

- Drafting messages before the trigger map. Fix: map all four categories and confirm the logic first.
- Addressing a contact as "Hello there" when the first name is captured. Fix: use the first-name token in every message.
- Letting a sequence continue after the contact replies. Fix: pull them out and hand over to a human within 2 hours.
- Treating sequences as "set and forget". Fix: run the quarterly review of offers, case studies, links, open and click rates, and conversion.
- Promising WhatsApp broadcasts on the free Business App. Fix: specify the Business API through a provider such as Twilio, Vonage, 360dialog or Brevo.
- Treating an inaccessible account, file or metric, or a missing native-language review, as healthy or approved. Fix: mark it `not assessed` and bound the conclusion.
- Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim.

## References

- [Trigger and sequence design](references/trigger-and-sequence-design.md): read when asking intake questions, filling the trigger tables, writing sequences, the WhatsApp path, tokens, the quarterly review, the brief format or the Hanlon and Tuten (2022), Pidsley (2023) and Zahay et al. (2024) sources.
- [AI automation recipes](references/ai-automation-recipes.md): read when building an AI or no-code automation roadmap: maturity stage, 8 qualification factors, feasibility tests, tool tiers, week-by-week build plan, what stays human and maintenance.
- [Agentic workflows and human checkpoints](references/agentic-workflows-and-human-checkpoints.md): read when specifying an agentic AI workflow (PRAL, BDI, OODA, five templates, HITL safeguards, three-wave roadmap).
- [Agentic marketing operating model](references/agentic-marketing-operating-model.md): read when setting the autonomy ladder, tool gating, memory, evaluation and deployment stages for an agent.
- [AI campaign trust, control, correction and drift](references/ai-campaign-trust-control-correction-drift.md): read when defining stop conditions and drift checks for a running AI workflow.
- [`07-email-marketing-strategy`](../../pipeline/07-email-marketing-strategy/SKILL.md): read when planning steady-state email after Day 31.
- [`playbook-chatbot-strategy`](../playbook-chatbot-strategy/SKILL.md): read when the need is a conversational bot rather than a sequence.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when writing sequence copy.
- [East African English standard](../../language/east-african-english/SKILL.md): read when checking tone for EA recipients.
<!-- dual-compat-end -->

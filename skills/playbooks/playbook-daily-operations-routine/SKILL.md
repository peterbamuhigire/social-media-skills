---
name: playbook-daily-operations-routine
description: 'Use when a social media manager handling several clients needs a working day and week: client load, morning monitoring, production and client-contact blocks, tools, and weekly and monthly Plan-Do-Check-Act reviews; produces the daily and weekly routine and PDCA log; not for running the agency business (use `playbook-agency-operations`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Playbook: Daily Operations Routine

A personalised operating manual for managing multiple social media clients without losing quality, responsiveness, or sanity: the hour-by-hour routine here, with the Plan/Do/Check/Act cycle above it in [PDCA review cadence](references/pdca-review-cadence.md).

<!-- dual-compat-start -->
## Use When
- One manager looks after several client accounts: how many can be carried, and how should the day be split?
- Set a morning monitoring block: incident check, response queue and a quick analytics look before production starts.
- A weekly day-by-day priority list and a tools stack for scheduling and monitoring many accounts.
- A weekly and monthly Plan-Do-Check-Act review with optimisation triggers and a PDCA log of every change.
- Agree WhatsApp norms for talking with clients during working hours in East Africa.

## Do Not Use When
- `playbook-agency-operations` for agency onboarding, invoicing, team structure and partner delivery.
- `11-content-calendar` for the schedule of posts itself.
- `meta-reporting` for the monthly performance report to the client.
- Stop when the client load exceeds the capacity limit in the plan; flag the overload to the account owner instead of scheduling more work.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Number of clients now (or target when fully operational) | Consultant | Yes | Stop; capacity cannot be judged without it. |
| Client mix: active, light, campaign or monthly retainer | Consultant or retainer list | Yes | Treat every client as active management and label the verdict provisional. |
| Current tools (scheduling, analytics, project management, communication) | Consultant | Yes | Recommend the free-tier minimum stack and mark tool gaps `not assessed`. |
| Working pattern: full-time, part-time, freelance evenings and weekends | Consultant | Yes | Use the 08:00–17:30 EAT weekday blocks and state that clock times shift with the pattern. |
| Primary pain point: too reactive, disorganised, slow to produce, or poor client communication | Consultant | Yes | Ask; do not guess which block needs most attention. |
| Performance baseline and review records for the PDCA cycle | Platform exports or team log | For PDCA | Start the PDCA log from today and mark prior trends `not assessed`. |

## Workflow

1. Ask the intake questions in [daily routine method](references/daily-routine-method.md) and confirm the owner and permission boundary.
2. Total weekly hours per client type from the capacity table; subtract 20% of available hours for administration, learning and unexpected requests.
3. If projected client hours exceed available capacity, stop and recommend reducing the load or reclassifying clients before designing the routine.
4. Lay out the morning monitoring block (incident check, response queue, quick analytics), the client-batched production block, the single client-communication block and the afternoon deep-work block.
5. Set the weekly day-by-day priority table and the minimum viable tools stack.
6. Add the weekly and monthly PDCA reviews, triggers and log from [PDCA review cadence](references/pdca-review-cadence.md).
7. Adjust clock times for part-time, other time zones, or evening and weekend work; the logic stays, only the times shift.
8. Run the quality checks and the anti-slop gate; correct any failed item and rerun before handing the manual over.

## Capacity limits for a solo consultant

Uganda context, with AI assistance: 5–6 active management clients is sustainable with good systems; 8–10 light management clients is possible but requires excellent scheduling tools; beyond 10 clients quality drops, so consider hiring a junior content assistant.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Capacity summary with sustainability verdict | Consultant or account owner | Hours per client type, total hours and available capacity are shown before the routine. |
| Time-blocked daily routine, response priority order and per-client production checklist | Consultant | Every block has clock times and named tasks fitted to the stated client mix and working pattern. |
| Client communication protocol and WhatsApp norms | Consultant and clients | Approval window, reporting day, response time and after-hours rule are stated. |
| Weekly rhythm table and recommended tools stack | Consultant | Each weekday has one primary task; each tool has a purpose and free-tier status. |
| PDCA review routine and log | Consultant or account owner | Weekly and monthly reviews have triggers and every change is logged. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Capacity calculation | Table in the manual | Hours per client type, 20% reserve and verdict can be recomputed from the inputs. |
| PDCA log entries | Log table from the PDCA reference | Each change records trigger, action, date and result, or is marked `not assessed`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Loading posts into a scheduler or publishing without an approval reply follows the retainer agreement, not this plan.

## Degraded Mode

Without the client count and mix, return the narrowest qualified result and mark the affected checks `not assessed`. A generic time-blocked day, response priority order and weekly rhythm can still be delivered with the capacity verdict left open.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Projected client hours exceed available capacity after the 20% reserve | Recommend reducing or reclassifying clients before producing the routine. | A routine that cannot be kept and quality that drops. |
| The morning incident check finds a crisis indicator | Pause all other work and activate `playbook-crisis-communications`. | A crisis growing while routine work continues. |
| Several responses are waiting | Complaints (within 2 hours) before purchasing enquiries (within 1 hour) before personal replies (2–4 hours) before positive comments (batched daily); hide or delete spam at once. | Lost sales and unresolved complaints. |
| A client asks for work outside scope | Do not respond in the moment; log it for the next monthly review via `playbook-client-retainer-management`. | Unpaid scope creep. |
| An approval request gets no reply in 24 hours | Follow up once, then publish as planned where the retainer allows. | A stalled content queue. |
| A task is urgent but not material to an agreed objective | Batch or defer it. | Reactive work displacing priority delivery. |
| The team needs triggers, reviews and a learning record, not only a task list | Apply the PDCA review cadence: triggers, review routine and PDCA log. | A routine that repeats activity without changing underperformance. |

## Quality Standards

- Client load capacity is calculated with specific hours per client type, producing a clear sustainability verdict before the routine is designed.
- The morning block names the response priority order: complaints before purchasing enquiries before general comments before spam.
- The production process names AI drafting tools and a brand voice quality-control step; AI output is never published unreviewed.
- Client communication is batched into one daily block; WhatsApp professional norms are stated for the EA context.
- The weekly rhythm assigns a named primary task to each day of the week.
- EA notes cover the overnight comment backlog (20:00–23:00 data hour) and the WhatsApp voice-note preference.
- The tools stack lists each tool with its purpose and confirms free-tier availability for the Ugandan market.
- The output is a complete operating manual tailored to the consultant's actual client mix and working pattern, not a generic checklist.

## Anti-Patterns

- Designing the routine before calculating capacity. Fix: produce the capacity summary and verdict first.
- Batching production by task type across clients. Fix: finish all content for Client A before Client B; each switch wastes 15–20 minutes.
- Answering client WhatsApps as they arrive. Fix: hold one communication block and publish working hours in the status message.
- Replying to work WhatsApps after 19:00 EAT. Fix: keep the stated working hours; late replies set an unsustainable precedent.
- Letting the scheduling queue run empty. Fix: keep 3–5 days scheduled ahead and batch-schedule the week on Monday.
- Publishing FeedHive or other AI suggestions unedited. Fix: run the brand-voice edit and cultural localisation check first.
- Adding more tools than the team can maintain. Fix: pick the minimum viable stack for scheduling, tasks and client communication.

## References

- [Daily routine method](references/daily-routine-method.md): read when asking the intake questions, filling the capacity table, laying out time blocks, communication norms, the weekly rhythm, the tools stack or the manual format.
- [PDCA review cadence](references/pdca-review-cadence.md): read when the client needs the weekly and monthly PDCA reviews, optimisation triggers, the PDCA log or a single-account daily routine.
- [`playbook-crisis-communications`](../playbook-crisis-communications/SKILL.md): read when the morning incident check reveals a crisis indicator.
- [`playbook-client-retainer-management`](../playbook-client-retainer-management/SKILL.md): read when handling scope creep and retainer boundaries.
- [`playbook-agency-operations`](../playbook-agency-operations/SKILL.md): read when scaling from solo consultant to team operations.
- [`prompt-engineering-library`](../../content-writing/prompt-engineering-library/SKILL.md): read when drafting with AI in the production block.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when running the humanising rewrite passes on AI first drafts.
- [East African English standard](../../language/east-african-english/SKILL.md): read when checking tone and local references.
<!-- dual-compat-end -->

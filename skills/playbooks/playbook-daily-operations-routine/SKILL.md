---
name: playbook-daily-operations-routine
description: Use when designing or improving a Daily Operations Routine operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Playbook: Daily Operations Routine

A personalised operating manual for managing multiple social media clients without losing quality,
responsiveness, or sanity. This playbook differs from `strategy-pdca-workflow-design`, which covers
the analytical improvement cycle (Plan/Do/Check/Act). This skill covers the physical daily routine —
the specific tasks a social media manager executes hour by hour.

---

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Daily Operations Routine workflow for a client or delivery team.
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
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Daily Operations Routine playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A task is urgent but not material to an agreed objective | Batch or defer it | Reactive work displacing priority delivery |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Daily Operations Routine playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Daily Operations Routine playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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

## Required Inputs

Ask for the following before generating the operating manual:

1. **Number of clients** currently managed, or target number when fully operational
2. **Client mix** — how many are active management, light management, campaign, or monthly retainer
3. **Current tools** in use (scheduling, analytics, project management, communication)
4. **Working pattern** — full-time, part-time, freelance evenings and weekends
5. **Primary pain point** — too reactive, disorganised, slow to produce content, or poor client communication

---

## Section 1: Client Load Capacity Planning

Before designing the routine, calculate capacity honestly. Use the table below to total the daily
and weekly hours required across the current client mix.

**Time allocation per client per day:**

| Client Type | Daily Time | Weekly Time |
|---|---|---|
| Active management (3–5 posts/week, community management, reporting) | 45–60 min | 5–6 hours |
| Light management (2–3 posts/week, response monitoring) | 20–30 min | 2–3 hours |
| Campaign period (active campaign with paid ads and daily optimisation) | 90–120 min | 10–12 hours |
| Monthly retainer (content only, no community management) | 15 min/day | 1–2 hours |

**Maximum sustainable load for a solo consultant (Uganda context, with AI assistance):**

- 5–6 active management clients: sustainable with good systems
- 8–10 light management clients: possible but requires excellent scheduling tools
- Beyond 10 clients: quality drops; consider hiring a junior content assistant

Calculate the consultant's total weekly hours available. Subtract 20% for administration, learning,
and unexpected requests. If projected client hours exceed available capacity, recommend reducing the
client load or reclassifying clients before producing the routine.

---

## Section 2: The Morning Monitoring Block (08:00–09:30 EAT)

This block happens before any content creation. You cannot create well without knowing what happened
overnight.

### Step 1 — Incident Check (10 minutes)

For each client account, check:

- Any negative mentions, complaints, or crisis indicators overnight?
- Any urgent DMs requiring immediate response?
- Any post that significantly over- or under-performed overnight?
- Any scheduled posts that failed to publish (tool errors are common on low-bandwidth connections)?

If a crisis indicator is found: pause all other work and activate `playbook-crisis-communications`.

### Step 2 — Response Queue (20–30 minutes)

Prioritise responses in this order:

1. Customer complaints — resolve or escalate within 2 hours of discovery
2. Purchasing enquiries — respond within 1 hour
3. Genuine comments requiring a personal reply — respond within 2–4 hours
4. General positive comments — batch-respond once per day
5. Spam and irrelevant comments — delete or hide immediately

**EA response note:** In Uganda, many comments arrive overnight (20:00–23:00) when data costs are
lower. Check for overnight comment backlog every morning before assessing the day's priority level.

### Step 3 — Quick Analytics Review (10 minutes)

For each active client, note:

- Best-performing post from yesterday (screenshot for the weekly report)
- Any content anomalies: sudden reach drop, unusual engagement spike
- Scheduled content for today — confirm it is queued and ready to publish

---

## Section 3: Content Production Block (10:00–13:00 EAT)

Batch content production by client, not by task type. Produce all content for Client A before
moving to Client B. Context-switching between clients mid-task wastes 15–20 minutes per switch.

### Content Production Order Within a Client

1. AI-assisted first draft — use ChatGPT or Claude (reference `prompt-engineering-library`)
2. Brand voice edit — apply the client's voice guidelines (reference `ai-content-humaniser`)
3. Cultural localisation check — confirm EA context, Ugandan references where appropriate
4. Image selection or briefing — identify what visual accompanies each post
5. Load into scheduling tool — Buffer, FeedHive, or Hootsuite
6. Set for client approval or direct publish — per the retainer agreement

### Scheduling Tool Discipline

- Never leave the content queue empty — always maintain 3–5 days of content scheduled ahead
- Use batch scheduling: schedule the full week's content for all clients on Monday
- If using FeedHive, use the AI content calendar feature to identify gaps; always edit AI
  suggestions before publishing — never publish unreviewed AI output
- Flag any post that requires a real-time hook (news event, trending topic) to be produced same-day

---

## Section 4: Client Communication Block (13:30–14:30 EAT)

All client communication happens in one dedicated block — not scattered throughout the day.
Responding to WhatsApp messages as they arrive fractures concentration and trains clients to
expect instant responses, which is unsustainable.

### Communication Types and How to Handle

- **Content approval requests:** Send via WhatsApp or the client portal; give a 24-hour approval
  window; if no reply, follow up once, then publish as planned
- **Weekly reporting updates:** Prepare and send every Friday; no more than 5 minutes per client
- **Reactive updates:** If something significant happened on a client account — a post going viral,
  a complaint, a campaign spike — brief the client the same day, not at the end of the week
- **Scope creep requests:** Do not respond in the moment; log the request and address it in the
  next monthly review (reference `playbook-client-retainer-management`)

### WhatsApp Professional Norms for East Africa

- Set a WhatsApp Business status message stating working hours, e.g.:
  _"Working hours: Mon–Fri, 8am–6pm EAT. I respond within 2 hours during these times."_
- Respond to client WhatsApps within 2 hours during working hours
- Do not respond to work WhatsApps after 19:00 EAT — late responses set an unsustainable precedent
- Use voice notes for complex explanations — EA clients prefer voice notes to long text messages
- Use WhatsApp Business labels to tag conversations by client and urgency

---

## Section 5: Afternoon and Weekly Rhythm

### Afternoon Block (14:30–17:30 EAT)

Allocate this block to deeper work that requires uninterrupted thinking:

- Strategy and planning work: content calendars, strategy documents, gap analysis
- New client onboarding tasks (reference `01-client-brief` through `04-brand-voice-intake`)
- Reporting preparation: compiling screenshots, metrics, and commentary
- Learning and skill development — minimum 30 minutes per day

### Weekly Day-by-Day Priority

| Day | Primary Task |
|---|---|
| Monday | Weekly monitoring review; schedule full week's content for all clients; client check-ins |
| Tuesday | Content creation day — batch production for the following week |
| Wednesday | Mid-week analytics check; community management focus; respond to pending approvals |
| Thursday | Client reporting and feedback; campaign optimisation if a campaign is live |
| Friday | End-of-week review; prepare next week's content plan; send weekly performance updates |

---

## Section 6: Tools Stack for Multi-Client Operations

| Tool | Purpose | EA Accessibility |
|---|---|---|
| FeedHive or Buffer | Multi-account scheduling | Yes — both have free tiers |
| Google Sheets or Notion | Client content calendar and tracking | Yes — free |
| Trello or Asana | Task management across clients | Yes — free tiers |
| WhatsApp Business | Client communication | Yes — essential in Uganda |
| ChatGPT / Claude | Content drafting and ideation | Yes — free tiers |
| Canva | Graphics production | Yes — free tier |
| Meta Business Suite | Facebook/Instagram analytics and scheduling | Yes — free |
| Google Analytics 4 | Website traffic attribution from social | Yes — free |

Select the minimum viable tools stack that covers scheduling, task management, and client
communication. Adding more tools than the team can maintain consistently reduces efficiency.

---

## Output Format

Produce the operating manual as a structured document with these sections:

1. **Capacity summary** — total clients, hours per week per client type, total hours, available
   capacity, and a clear sustainability verdict
2. **Daily routine schedule** — time-blocked day with named tasks, tailored to the consultant's
   working pattern and client mix
3. **Response priority order** — named list for the morning response queue
4. **Content production checklist** — per-client production steps
5. **Client communication protocol** — how and when to communicate with each client type
6. **Weekly rhythm table** — day-by-day priority tasks
7. **Recommended tools stack** — based on current tools and gaps identified

Adjust all timings if the consultant works part-time or in a different time zone. If the consultant
works evenings and weekends, restructure the blocks accordingly — the logic remains the same; only
the clock times shift.

---

## Cross-References

- `strategy-pdca-workflow-design` — for the analytical improvement cycle (Plan/Do/Check/Act),
  which sits above and around this daily routine
- `playbook-client-retainer-management` — for handling scope creep and retainer boundaries
- `playbook-agency-operations` — for scaling from solo consultant to team operations
- `playbook-crisis-communications` — activate immediately if the morning incident check reveals
  a crisis indicator
- `prompt-engineering-library` — for AI-assisted content drafting in the production block
- `ai-content-humaniser` — for brand voice editing after AI first drafts

---

## Quality Criteria

- Client load capacity is calculated with specific hours per client type, producing a clear
  sustainability verdict before the routine is designed
- Morning block specifies a named priority order for responses: complaints before purchasing
  enquiries before general comments before spam
- Content production process references AI drafting tools and a brand voice quality control step
  explicitly — AI output is never published unreviewed
- Client communication is batched into one daily block, not scattered; WhatsApp professional norms
  are stated clearly for the EA context
- Weekly rhythm assigns a named primary task to each day of the week
- EA-specific notes cover overnight comment backlog (20:00–23:00 data hour) and WhatsApp voice
  note preference
- Tools stack lists each tool with its purpose and confirms free-tier availability for the Ugandan
  market
- Output is a complete operating manual, not a generic checklist — timings and structures are
  tailored to the consultant's actual client mix and working pattern

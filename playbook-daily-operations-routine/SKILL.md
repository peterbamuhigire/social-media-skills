---
name: playbook-daily-operations-routine
description: >
  Produces a structured daily task framework for a social media manager or consultant managing
  multiple clients — covering morning monitoring, response queue management, content scheduling
  workflow, and client reporting rhythm. Output is a personalised operating manual. Invoke when
  a consultant is taking on additional clients and needs to structure their day, when setting up
  systems for a newly hired social media manager, or when a client wants to understand how their
  account is managed day-to-day. Based on Johnson, J. (2023) How to Become a Social Media Manager.
---

# Playbook: Daily Operations Routine

A personalised operating manual for managing multiple social media clients without losing quality,
responsiveness, or sanity. This playbook differs from `strategy-pdca-workflow-design`, which covers
the analytical improvement cycle (Plan/Do/Check/Act). This skill covers the physical daily routine —
the specific tasks a social media manager executes hour by hour.

---

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

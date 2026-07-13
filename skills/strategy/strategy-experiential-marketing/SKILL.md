---
name: strategy-experiential-marketing
description: Use when the main deliverable concerns strategic live and hybrid experiences for launches, activations, events, and pop-ups; use playbook-webinars-live-events when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Experiential Marketing Strategy

<!-- dual-compat-start -->
## Use When

- Use this skill for strategic live and hybrid experiences for launches, activations, events, and pop-ups.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `playbook-webinars-live-events` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to strategic live and hybrid experiences for launches, activations, events, and pop-ups | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `playbook-webinars-live-events`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Strategic live and hybrid experiences for launches, activations, events, and pop-ups deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
| Decision and risk record | Reviewer or implementer | Links each recommendation to supplied evidence or labels it as an assumption |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Input and assumption register | Table or annotated brief | Missing and unverified items are visible, not treated as passed |
| Release check | Completed quality checklist | All blocking findings are fixed or the deliverable is explicitly withheld |

## Capability and Permission Boundaries

Read and search are the minimum capabilities. Analysis and planning remain read-only. Edit only files placed in scope; publishing, outreach, spend, personal-data processing, production changes, and certification claims require explicit authority and evidence of success.

## Degraded Mode

If files, tools, network, current evidence, rendering, or authorised access are unavailable, return the narrowest useful qualified deliverable. Mark each unavailable check `not assessed`; never convert it into a pass or invent market facts.

## Decision Rules

| Choice condition | Action | Failure or risk avoided |
|---|---|---|
| The client needs an experience concept and behaviour outcome | Define the experience promise and evidence path before logistics | A run-of-show is mistaken for an experiential strategy |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source | Confident advice built on an unresolved premise |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist | Unauthorised publication, spend, outreach, or data use |

## Quality Standards

- Keep Uganda/East Africa, British English, EAT, UGX, and WhatsApp-first assumptions explicit where they apply.
- Tie recommendations to observed evidence, a named assumption, or a verification action.
- Give the next operator enough detail to execute without guessing ownership, sequence, or acceptance.
- Apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Inventing a client metric, audience fact, price, partner, or platform rule. Fix: verify it or label the decision provisional.
- Treating a missing tool, source, render, or approval as a passed check. Fix: mark it `not assessed` and narrow the output.
- Producing channel tactics before defining the decision and consumer. Fix: state the required outcome and handoff first.
- Copying a global template without adapting Uganda/East Africa access, language, payment, or trust conditions. Fix: record which local assumptions apply.
- Recommending publication, outreach, spend, data collection, or a regulated claim without authority. Fix: stop at an approval-ready draft.
- Reporting activity as success without an acceptance condition. Fix: name the observable result and evidence source.

## References

- [AGENTS.md](../../../AGENTS.md)
<!-- dual-compat-end -->

**Sources:** Hanlon and Tuten (2022) *The SAGE Handbook of Digital Marketing*, citing Schmitt (1999) and Pine and Gilmore (1998)

---


## Required Inputs

Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry**
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. product launch, brand awareness, community building, sales conversion at event)
5. **Event format** (in-person only; hybrid in-person + live stream; digital/virtual only)
6. **Target audience for the event** (generational profile; B2C or B2B; geographic reach)
7. **Budget range** (determines scale, production quality, and tool recommendations)
8. **Date and venue constraints** (if known — affects pre-event timeline)

---

## Why Experiential Marketing Matters

Social media content creates awareness and engagement. Experiential marketing creates **memory and emotional commitment** — the kind that drives word-of-mouth, repeat purchase, and brand advocacy.

The Experience Economy (Pine and Gilmore, 1998) demonstrates that consumers pay a premium for experiences over commodities:

| Stage | Example | Approximate value |
|---|---|---|
| Commodity | Raw coffee beans | UGX 500 |
| Product | Packaged ground coffee | UGX 3,000 |
| Service | A cup of coffee at a café | UGX 8,000 |
| Experience | Coffee at a branded, designed environment | UGX 25,000–40,000 |

The physical, emotional, and sensory staging creates the value premium — not the product itself. Apply this logic to every client event: the staging is not decoration; it is the pricing mechanism.

---

## Schmitt's ExM Framework — Four Distinguishing Features

Schmitt (1999) distinguishes experiential marketing from conventional event management on four dimensions:

1. **Focus on customer experiences** — the goal is the cognitive, emotional, behavioural, and relational response to the encounter with the brand, not the product features or the logistics of the event
2. **Consumption as a holistic experience** — the experience begins with the invitation and continues with the follow-up; budget content and attention for before, during, and after the event
3. **Customers as rational and emotional beings** — emotional design is not secondary to functional design; a beautifully staged event that runs badly on logistics fails; a logistically smooth event that creates no emotional memory also fails
4. **Eclectic methods** — ExM does not have a single toolkit; the right combination of sensory, affective, behavioural, and social elements varies by brand, audience, and context

---

## Experience Design Principles

### Multi-Sensory Design
Engage sight, sound, touch, smell, and taste where relevant to the brand context. A product launch with curated background music and scented displays is more memorable than one that only engages sight. Map every sensory touchpoint:

- **Sight:** venue design, lighting, branded materials, staff uniforms
- **Sound:** music selection and volume (ambient, not intrusive); MC voice and pacing; sound system quality
- **Touch:** product samples, interactive stations, texture of printed materials
- **Smell:** signature scent in venue (relevant for food, beauty, hospitality clients); clean air in enclosed spaces
- **Taste:** branded food and drink where appropriate — the most memorable sensory touchpoint

### Participation Over Spectacle
Experiences where attendees **do something** — make, build, vote, taste, test, create — generate stronger and more durable memories than passive observation. Design at least one participatory element into every event:

- Product tasting or testing stations
- A live demo where an attendee is the subject
- A co-creation activity (voting on product names, contributing to a mural, writing on a feedback wall)
- A challenge or competition with a visible result
- A guided experience with the brand founder or a key team member

### Shareable Moments (Earned Social Media)
Design at least one "selfie-worthy" element into every activation — a distinct visual moment that attendees naturally want to photograph and share:

- A branded photo backdrop with strong visual identity
- An unusual or impressive product display
- An interactive installation that changes with participation
- A moment of spectacle (a live performance, an unexpected reveal, a countdown)

Social media amplification from attendees during and after the event is earned media. Design for it — do not hope for it.

### Pre-Event Anticipation and Post-Event Follow-Up
The experience does not begin when the doors open. Budget time, content, and team effort for:

**Pre-event (2–4 weeks before):**
- Teaser content on social media — partial reveals, countdown posts, behind-the-scenes preparation
- WhatsApp event community: create a dedicated group for registered attendees; share anticipation content and practical logistics
- Email or WhatsApp confirmation sequence with clear calls to action (register, confirm attendance, invite a colleague)

**Post-event (within 48 hours):**
- Thank-you message via WhatsApp with a photo from the event
- NPS survey — single question: "How likely are you to recommend [brand] to a friend or colleague? 0–10"
- A follow-up offer or next step — do not let the emotional energy dissipate without a conversion action
- Publish event highlights on social media within 24 hours; tag attendees where possible

---

## Digital and Hybrid ExM for EA Clients

For clients with geographically dispersed audiences or limited venue budgets:

**Instagram Live and YouTube Live:**
- Product launches, Q&A sessions, and behind-the-scenes reveals are well-suited to live streaming
- Interactive features (comments, questions, polls) replicate participation elements
- Promote the stream 7 days, 3 days, and 1 hour before it begins

**Hybrid events:**
- Live in-person experience with simultaneous streaming for remote audiences
- **Audio investment rule:** Invest in good audio before good video. Poor audio destroys digital participation; poor video is tolerable but poor sound causes viewers to leave within 30 seconds
- Assign a dedicated digital host to manage the online stream — the in-room MC cannot simultaneously manage both audiences effectively

**WhatsApp event community:**
- Create a dedicated WhatsApp group for event attendees
- Pre-event: practical logistics + anticipation content
- During event: real-time updates for remote participants + polls and questions
- Post-event: highlights, photos, follow-up offers
- Archive the group 30 days after the event; download and save the content before archiving

---

## ExM Measurement Framework

Measure the following for every event:

| Metric | Definition | When to measure |
|---|---|---|
| Attendance rate | Actual attendees ÷ registered attendees | Day of event |
| Social media mentions | Organic brand mentions during event + 48 hours after | During and post-event |
| Earned media reach | Total reach of organic attendee posts mentioning the brand | 48–72 hours post-event |
| Post-event NPS | Net Promoter Score from WhatsApp survey | Within 24 hours |
| 30-day conversion rate | % of attendees who made a purchase or enquiry within 30 days | 30 days post-event |
| Press and influencer coverage | Number of media or influencer mentions generated | 7 days post-event |
| Cost per attendee | Total event cost ÷ number of attendees | Post-event |

Include ExM measurement results in the next monthly or quarterly report using `meta-reporting` or `deck-monthly-report`.

---

## EA-Specific Considerations

- **Venue logistics matter more in EA:** Power supply reliability, parking, public transport access, and security affect attendance. Include a venue logistics checklist in the event plan.
- **WhatsApp is the primary event communication tool:** Use WhatsApp Broadcast for confirmations, reminders, and post-event follow-up — not email. Open rates on WhatsApp in EA are significantly higher.
- **Public holidays and sporting events:** Check the Ugandan/EA public holiday calendar and major sporting events calendar before confirming the event date. Attendance is significantly affected by public holidays and major international football fixtures.
- **Catering is a trust signal in EA:** Food and refreshments at an event signal that the host values the guests. A no-catering event is often interpreted as a poorly resourced or disrespectful host. Budget for at minimum light refreshments.
- **Photography as content:** Hire a photographer or assign a dedicated content creator for every event — event content is one of the most effective organic social media assets, and poor-quality event photos undermine the brand more than no photos at all.

---

## Quality Criteria

Output meets the standard for this skill if:

- Pine and Gilmore's Experience Economy pricing rationale is applied — the strategy explains why the staging creates value, not just what to include
- All four Schmitt ExM principles are addressed in the design
- At least one participatory element, one shareable moment, and one multi-sensory touchpoint are specified
- Pre-event and post-event experience are planned — not just the event day
- Hybrid and digital options are addressed for EA clients who cannot support a fully in-person event
- The measurement framework includes 30-day conversion rate — not just attendance and social mentions
- EA-specific considerations (WhatsApp, catering, power supply, photography) are addressed
- Language is British English throughout; imperative in all instructional sections

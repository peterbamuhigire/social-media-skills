---
name: strategy-experiential-marketing
description: 'Use when a brand wants people to experience it in person or online: launch events, activations, pop-ups, sampling, webinars, Facebook Live or Zoom sessions and hybrid broadcasts; produces the experience plan with run sheet, promotion calendar and follow-up; not for a whole multi-channel campaign (use `09-campaign-strategy`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Experiential Marketing Strategy

Designs launches, activations, pop-ups and live or hybrid events that create memory and word of mouth for East African brands, drawing on Schmitt (1999) and Pine and Gilmore (1998), and measures impact beyond attendance.

<!-- dual-compat-start -->
## Use When

- We are launching a product and want a pop-up, roadshow, sampling or activation that people photograph and share.
- An event needs designing for the senses and for participation, with buzz beforehand and follow-up afterwards.
- We are running a webinar, Facebook Live, YouTube Live or Zoom webinar and need a promotion calendar, run sheet, technical checklist for power and data cuts, and replay follow-up.
- A hybrid event must serve people in the room and those watching online.
- We must show event impact beyond attendance: leads, shares, sentiment and sales.

## Do Not Use When

- `09-campaign-strategy` for planning a full campaign where an event is only one part.
- `strategy-video-content` for recorded video or podcast content rather than a live experience.
- `playbook-pr-publicity` for media coverage of the event.
- Stop before booking venues, paying suppliers or going live without explicit client authority, permits and a safety check.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry, country/city and primary goal (launch, awareness, community, sales at the event) | Client | Yes | Default to Uganda / East Africa; ask for the goal before choosing the format. |
| Event format (in-person only; hybrid in-person + live stream; digital/virtual only) | Client | Yes | Plan in-person with a hybrid option and mark streaming costs `not assessed`. |
| Target audience (generational profile, B2C or B2B, geographic reach) | Client lead | Yes | Design for the client's existing customer base and label the profile an assumption. |
| Budget range | Client | Yes | Present scale options (light refreshments minimum) without committing production quality or tools. |
| Date and venue constraints | Client | If known | Check the Ugandan/EA public holiday and major sporting calendars before proposing dates; hold the venue checklist open. |
| Permits, safety check and supplier authority | Client owner; venue | Before any booking | Stop before booking venues, paying suppliers or going live. |

## Workflow

1. Confirm the request is a live or hybrid experience, not a full campaign (`09-campaign-strategy`) or recorded video (`strategy-video-content`); run the intake in the [experiential marketing method](references/experiential-marketing-method.md), and for a webinar, live stream or virtual event apply [webinars-and-virtual-events.md](references/webinars-and-virtual-events.md).
2. Define the experience promise and the behaviour outcome, using the Experience Economy logic (Pine and Gilmore, 1998) to show why the staging creates value.
3. Design against Schmitt's four ExM features: map every sensory touchpoint and include at least one participatory element and one shareable moment.
4. Plan the pre-event run-up (2–4 weeks: teasers, WhatsApp event community, confirmation sequence) and post-event follow-up (thank-you, NPS, follow-up offer, highlights within 24 hours).
5. For dispersed audiences or limited budgets, add the live or hybrid layer: promotion at 7 days, 3 days and 1 hour, audio before video, and a dedicated digital host.
6. Apply the East African checks (venue logistics, power, holidays and fixtures, catering, photographer) and stop before booking, paying suppliers or going live without authority, permits and a safety check.
7. Set the seven ExM metrics with timing; correct any plan that measures attendance and mentions only and rerun the check, then run the anti-slop gate and hand the plan to the event owner.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Experience concept with the Experience Economy rationale and Schmitt design map | Client lead | States why the staging creates value; all four Schmitt features addressed. |
| Sensory, participation and shareable-moment design | Event producer | At least one participatory element, one shareable moment and one multi-sensory touchpoint named. |
| Pre-event and post-event plan, including the WhatsApp event community | Client marketing team | Timings stated (2–4 weeks before; within 48 hours after); a conversion action follows the event. |
| Hybrid or digital layer (and webinar pack when virtual) | Digital host; technical owner | Audio, host, backup and moderation owners named. |
| Event measurement plan | Client lead; `meta-reporting` | All seven metrics, including 30-day conversion rate and cost per attendee. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Venue logistics checklist | Checklist | Power, parking, public transport, security and catering each checked or marked `not assessed`. |
| Date-clash check | Table | Public holidays and major fixtures checked against a dated calendar. |
| Post-event results record | Table of the seven metrics | Each metric sourced and timed as specified; no attendance figure reported as impact alone. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Booking venues, paying suppliers, going live and recording attendees also need permits, a safety check and recording consent.

## Degraded Mode

Without a confirmed budget, format and date, return the narrowest qualified result and mark the affected checks `not assessed`. The experience concept, sensory and participation design, and a measurement plan can still be delivered as options for the client to choose between.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client needs an experience concept and behaviour outcome | Define the experience promise and evidence path before logistics. | A run-of-show is mistaken for an experiential strategy. |
| The experience is a webinar, live stream or virtual session | Apply [webinars-and-virtual-events.md](references/webinars-and-virtual-events.md); do not go live until moderation, recording consent and a failure backup have owners. | A live session that fails on connectivity, power or moderation. |
| The event is hybrid | Invest in audio before video and assign a dedicated digital host separate from the in-room MC. | Remote viewers leaving within 30 seconds of poor sound. |
| The proposed date falls on a public holiday or major international football fixture | Move the date or plan for lower attendance. | Empty rooms. |
| The budget cannot cover full catering | Budget at minimum light refreshments. | A host read as poorly resourced or disrespectful. |
| No photographer or content creator is assigned | Hire one or assign a dedicated creator. | Poor event photos that harm the brand more than none. |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source. | Confident advice built on an unresolved premise. |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist. | Unauthorised publication, spend, outreach, or data use. |

## Quality Standards

- Pine and Gilmore's Experience Economy pricing rationale is applied — the strategy explains why the staging creates value, not just what to include.
- All four Schmitt ExM principles are addressed in the design.
- At least one participatory element, one shareable moment, and one multi-sensory touchpoint are specified.
- Pre-event and post-event experience are planned — not just the event day.
- Hybrid and digital options are addressed for EA clients who cannot support a fully in-person event.
- The measurement framework includes 30-day conversion rate — not just attendance and social mentions.
- EA-specific considerations (WhatsApp, catering, power supply, photography) are addressed.
- Language is British English throughout; imperative in all instructional sections; `ai-marketing/anti-ai-slop` is applied during drafting and release is blocked on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Treating staging as decoration. Fix: treat it as the pricing mechanism and design it to the experience promise.
- A passive spectacle with nothing for attendees to do. Fix: add tasting, a live demo, co-creation, a challenge or a guided founder experience.
- Hoping attendees will post. Fix: design at least one selfie-worthy element into every activation.
- Letting the energy fade after the event. Fix: send a WhatsApp thank-you, NPS question and follow-up offer within 48 hours.
- Relying on email for confirmations and reminders. Fix: use WhatsApp Broadcast and a dedicated event group, archived 30 days after the event once content is saved.
- Reporting attendance as impact. Fix: report leads, shares, sentiment, NPS and 30-day conversion.

## References

- [Experiential marketing method](references/experiential-marketing-method.md): read when running the intake, explaining the Experience Economy table, applying Schmitt's features, designing sensory and participatory elements, planning pre- and post-event activity, designing hybrid formats, setting metrics or checking East African considerations.
- [Webinars and virtual events](references/webinars-and-virtual-events.md): read when planning or running a webinar, live stream, Zoom or Google Meet session, or a hybrid broadcast.
- [`meta-reporting`](../../meta-analytics-ops/meta-reporting/SKILL.md): read when adding ExM results to the next monthly or quarterly report.
- [AGENTS.md](../../../AGENTS.md): read when routing to a neighbour skill or engine.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting teasers, invitations and follow-up messages.
<!-- dual-compat-end -->

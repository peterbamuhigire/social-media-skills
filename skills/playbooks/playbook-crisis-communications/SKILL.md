---
name: playbook-crisis-communications
description: Use when something has gone wrong in public (a viral complaint, media attention, a scandal, a platform blocked at election time) and the brand must respond fast; produces severity levels, holding statements, response timelines, a one-page crisis card and post-crisis review; not for slow review repair (use `playbook-reputation-management`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Crisis Communications Playbook

Produces a client's social media crisis plan: three severity levels with quantified triggers, response timelines, holding statements, platform actions, a printable quick card and the post-crisis review, built on the acknowledge → investigate → update cadence.

<!-- dual-compat-start -->
## Use When
- A customer's video or post is spreading fast and a reporter wants a comment: how serious is it and who responds in the first hour?
- A damaging news story is about to air or print and a statement is needed today.
- Write holding statements and a first-30-minute checklist before anything goes wrong.
- Platform actions on Facebook, Instagram, WhatsApp, X and LinkedIn during an incident, and what must not be done.
- Prepare for an internet shutdown or platform block around an election or national event.
- The storm has passed and a post-crisis review with lessons learned is due.

## Do Not Use When
- `playbook-reputation-management` for rebuilding ratings, reviews and search results over weeks.
- `playbook-community-management` for routine complaints handled within normal response times.
- `playbook-pr-publicity` for proactive press releases and media pitching.
- Stop before publishing any statement, deleting posts or naming individuals without legal and client sign-off; deliver the draft holding statement and the approval request.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name and business type; country/city | Client | Yes | Default to Uganda/East Africa and ask for the business type. |
| Social media manager (name, WhatsApp/phone) | Agency or client | Yes | Leave the role unassigned on the quick card and return it as a blocking gap. |
| Client approver (name, title, WhatsApp/phone) who approves every public statement | Client | Yes | Stop: no Level 2 or 3 statement can be issued; deliver drafts only. |
| PR or legal contact | Client | Yes for Level 3 | Note "not appointed" and advise the client to identify one before a crisis occurs. |
| WhatsApp number for crisis-related customer contact | Client | Yes | Use the main business number and label it for confirmation. |
| Platforms in scope and the market's election or national-event calendar | Client; register entries for shutdowns | Yes | Cover Facebook, Instagram and WhatsApp only; mark shutdown risk `not assessed`. |

## Workflow

1. Run the intake in [crisis response procedures](references/crisis-response-procedures.md); stop if there is no client approver, because no Level 2 or 3 statement may go out without one.
2. Define the three severity levels with quantified triggers (Level 1 under 50 interactions, Level 2 at 200+ interactions or media involvement, Level 3 national media, legal, safety, public figure or criminal allegation).
3. Write the tick-box timelines per level for the first 30 minutes, first 2 hours and first 24 hours, applying the acknowledge (first response), investigate (4–8 hours) and update (within 24 hours) cadence.
4. Customise the three holding statements with client details and confirm no placeholder text remains.
5. Write the what-not-to-do rules with their rationale and the platform actions for the platforms in scope only; omit unused platforms.
6. Where an election, national event or platform block falls in the plan window, add the [internet shutdown contingency](references/internet-shutdown-contingency.md); for health or NGO misinformation or impersonation, add the infodemic guidance.
7. Build the one-page crisis quick card and the 48–72-hour post-crisis review questions; check the plan against the quality standards, correct any vague trigger or placeholder and rerun the check before sending it to the client approver for sign-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Severity classification and per-level response timelines | Social media manager and client approver | Every trigger is quantified; every timeline is a tick-box checklist. |
| Holding statements (Levels 1–3) | Client approver; counsel at Level 3 | Complete, customised, no visible placeholder text before delivery. |
| What-not-to-do rules and platform actions | Social media manager | Rationale given for each rule; only platforms in scope included. |
| One-page crisis quick card | Client team (printed) | Standalone and printable with real names and contacts filled in. |
| Post-crisis review template | Client approver | Seven specific questions producing a one-page incident report. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Timestamped incident log | Live log with screenshots | Every post, share, comment, action and approval recorded with time and actor. |
| Statement approval record | Table: statement, level, approver, time | Every Level 2 and 3 statement has the approver's sign-off before publishing. |
| Outage record (if a shutdown occurs) | Source, start and end time, regions | Outage-window figures marked `not assessed`, not a result. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. At Level 2 and 3 the social media manager executes only approved responses and never acts independently.

## Degraded Mode

Without a named client approver, return the narrowest qualified result and mark the affected checks `not assessed`. Severity levels, draft holding statements, the what-not-to-do rules and a quick card with blank contact rows can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Facts are incomplete during a live incident | Issue a verified holding statement and set the next update time. | Speculation under pressure. |
| Level 1: under 50 interactions, no media | Community team replies within 2 hours with the standard complaint template, takes it offline and notifies the client within 4 hours. | Over-reacting to one complaint. |
| Level 2: 200+ interactions or a journalist, outlet or public figure involved | Pause scheduled posts, alert the client within 30 minutes and agree a holding statement within 1 hour; the client leads responses. | A manager improvising the brand's public line. |
| Level 3: national media, legal, safety, public figure or criminal allegation | Pause all activity, phone the approver, involve PR or legal counsel, issue the holding statement within 2 hours and monitor for 24 hours. | Legal exposure from an unreviewed statement. |
| Media involvement grows during a Level 2 event | Re-classify to Level 3. | Under-resourcing an escalating crisis. |
| The market faces an election, national event or platform block (for example Uganda) | Add the shutdown contingency: offline holding statements, an SMS or radio fallback and a paid-media pause rule (see [internet shutdown contingency](references/internet-shutdown-contingency.md)). | Going silent when mobile internet or social media is suspended. |
| A health or NGO crisis involves misinformation, impersonation or account targeting | Load [institutional health communication and infodemic response](../../sectors/healthcare/references/institutional-health-communication-and-infodemic-response.md). | Treating an infodemic as an ordinary complaint. |
| A fake video, cloned voice note, AI image or impersonating account about the client or its leaders is circulating | Run the [synthetic media and deepfake protocol](references/synthetic-media-and-deepfake-protocol.md): detect, verify provenance before any statement, respond, report to platforms, escalate to counsel; treat as Level 3 if it names a person, alleges a crime or touches an election. | Amplifying the fake, or calling genuine content fake. |
| Comments turn abusive or coordinated | Hide (Instagram Hidden Words) or turn off comments on that post; delete only clear hate speech or harassment and document each action. | A Streisand effect from deleting legitimate criticism. |

## Quality Standards

- All three levels have clear, quantified triggers; no "significant" without a threshold.
- Each level has a distinct tick-box timeline, not prose instructions.
- All three holding statements are complete, customised and free of visible placeholder text.
- The what-not-to-do section gives the rationale for each prohibition.
- Platform actions cover only the platforms listed at intake.
- The quick card is a genuinely standalone, printable section, not a summary.
- Post-crisis review questions are specific enough to produce a usable incident report.
- All content uses British English; no American spellings.

## Anti-Patterns

- Deleting negative comments. Fix: screenshot first; delete only hate speech or harassment and document it.
- Going silent while facts are gathered. Fix: issue a holding statement and state the next update time.
- Posting scheduled promotional content during a controversy. Fix: pause (draft mode, not delete) and resume only with client approval.
- Several people replying with different messages. Fix: agree one voice and one message before any statement goes out.
- Promising "we will fix this today" without certainty. Fix: commit to resolving and to regular updates instead.
- Deactivating the X/Twitter account under pressure. Fix: keep it live, mute the viral post and monitor brand-name search.
- Using humour in a Level 2 or 3 event. Fix: keep the tone serious until the review is closed.

## References

- [Crisis response procedures](references/crisis-response-procedures.md): read when running intake, following a level's timeline, adapting holding statements, applying platform actions, running the post-crisis review or building the quick card.
- [Internet shutdown and platform-block contingency](references/internet-shutdown-contingency.md): read when the plan covers an election period, a national event or a platform that may be blocked.
- [Synthetic media and deepfake protocol](references/synthetic-media-and-deepfake-protocol.md): read when a deepfake, cloned voice, AI-generated image or impersonation is circulating, or the client's own AI content is challenged.
- [CIPR crisis phases benchmark](references/crisis-response-procedures.md#8-benchmark-cipr-crisis-phases): read when checking the plan against the CIPR *Crisis Communication and Social Media* guide (2024; register `CIPR-CRISIS-SOCIAL-2024`).
- [Institutional health communication and infodemic response](../../sectors/healthcare/references/institutional-health-communication-and-infodemic-response.md): read when a health or NGO crisis involves misinformation, impersonation or account targeting.
- [`playbook-community-management`](../playbook-community-management/SKILL.md): read when using the standard complaint template at Level 1.
- [`playbook-reputation-management`](../playbook-reputation-management/SKILL.md): read after the crisis when ratings and search results need rebuilding.
- [`playbook-pr-publicity`](../playbook-pr-publicity/SKILL.md): read when proactive media work follows the review.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting statements.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and spelling.
<!-- dual-compat-end -->

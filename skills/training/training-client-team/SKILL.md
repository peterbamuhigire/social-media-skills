---
name: training-client-team
description: 'Use when the agency hands social media to the client''s own staff: a two-hour workshop on who posts what, approvals, replies and reporting, or a DIY handbook for making Canva and CapCut posts alone; produces the handover workbook or DIY content handbook; not for beginners'' lessons (use `training-social-media-fundamentals`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Media Team Training Workbook

Produces a printable participant workbook for a 2-hour in-person handover workshop (cover page, seven modules, three exercises), or a keep-forever DIY content handbook when the client will work alone. Not slide content.

<!-- dual-compat-start -->
## Use When

- Our engagement is ending and the client team must run the approved strategy themselves.
- Staff need to know what they can and cannot post, the approval workflow and how to reply to customer messages.
- The team needs the basics of the scheduling tool (Meta Business Suite, Buffer) and how to report performance each month.
- A client wants a keep-forever DIY content handbook: plan, design in Canva, edit in CapCut, write captions, boost posts and read analytics without the consultant.

## Do Not Use When

- `training-social-media-fundamentals` for beginners learning how social media marketing works.
- `training-smartphone-video-production` for hands-on phone filming and editing skills.
- `playbook-social-media-policy` for the formal governance policy, roles and escalation.
- Stop before transferring admin access, passwords or ad accounts without written authorisation from the account owner.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry, country/city, primary goal, team size and workshop date | Client lead | Yes | Default to Uganda/East Africa; hold the cover page and Module 1 until goal and team size are confirmed. |
| Approved strategy: platforms used, persona and content pillars | Strategy deliverables or client sign-off | Yes | List only confirmed platforms; mark pillar rows draft and ask the client to confirm. |
| SM Manager name and approval workflow contacts (WhatsApp group, email, turnaround hours) | Client lead | Yes | Leave the workbook in draft with the contact fields listed as missing; never invent contacts. |
| Scheduling tool (Buffer, Hootsuite, Meta Business Suite or other) | Client lead | Yes | Write Module 4 for Buffer and flag it for adaptation once the tool is named. |
| Restricted areas and confidentiality concerns; escalation owner (Client Owner / Director) | Client owner | Yes | Keep the generic "Not Allowed" list and ask for site-specific restricted areas before print. |
| For the DIY handbook: brand voice words, banned vocabulary, hashtag set, calendar location, consultant contacts | Brand voice guide, hashtag strategy, consultant | If DIY | Keep the handbook in draft and list the missing items. |

## Workflow

1. Confirm the route: facilitated handover workshop, independent DIY handbook, or both (workbook first, handbook as the take-away); route beginners to `training-social-media-fundamentals`.
2. Run the intake in [handover-workbook-modules.md](references/handover-workbook-modules.md) (or the DIY inputs in [diy-content-handbook.md](references/diy-content-handbook.md)); stop the affected module while approver contacts, turnaround or restricted areas are missing.
3. Write the cover page and Module 1 from the approved strategy in plain English: why we are on social media, platform table, persona, content themes, what good engagement looks like.
4. Write Modules 2–5: posting rules, smartphone photo and video tips, scheduling-tool basics for the named tool, and the approval workflow with submission contents and turnaround.
5. Write Modules 6–7: acknowledgement messages, what not to say, escalation path, and the weekly reporting template; add the three workshop exercises.
6. For an independent client, generate the DIY handbook from [diy-content-handbook.md](references/diy-content-handbook.md) with checks that need no facilitator.
7. Check module durations total 115 minutes plus 5 minutes intro and close, run the Quality Standards and `anti-ai-slop`, block release on an F from `ai-slop-audit`; correct any failing module and rerun the check before hand-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Printable participant workbook: cover page, Modules 1–7, three exercises | Client team and SM Manager | Every placeholder filled with the client's details; durations fit the 2-hour workshop. |
| DIY content handbook (when the client works alone) | Business owner and staff | Self-contained: templates, calendar location, caption checklist and when to call the consultant. |
| Weekly reporting template and approval workflow | SM Manager | Names the real approver, channel and turnaround hours. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Placeholder and contact register | Table: field, value, source, confirmed by | No bracketed placeholder or invented contact remains in the release copy. |
| Platform-rule check | List of sizes, lengths and tool steps with date checked | Each is verified at handover or marked `not assessed`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Admin access, passwords and ad-account transfer need written authorisation from the account owner.

## Degraded Mode

Without confirmed approver contacts and the approved strategy, return the narrowest qualified result and mark the affected checks `not assessed`. Modules 2, 3 and the exercises can still be delivered as a draft, with Modules 1, 5 and 6 held until the contacts and strategy are confirmed.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A strategy exists and staff need assigned operating competence | Train against the real workflow, roles, and escalation routes | Generic training cannot be applied after the workshop |
| The client will work independently after handover | Produce the DIY handbook in [diy-content-handbook.md](references/diy-content-handbook.md) with repeatable checks that need no facilitator | A workshop outline is delivered as an unusable handbook |
| The scheduling tool is not Buffer | Adapt Module 4 steps to the named tool (Hootsuite, Meta Business Suite or other) | Staff follow menu steps that do not exist |
| A customer message is a complaint or abusive | Acknowledge with the standard message, resolve nothing, escalate to the SM Manager then the Client Owner / Director | Unauthorised refunds, prices or promises |
| Strategy documents and the client lead disagree on platforms, pillars or approver | Pause the affected module and ask the client owner to confirm | Staff trained on a workflow nobody runs |
| The client asks the workbook to include logins or to hand over account access | Leave credentials out; list access transfer as an owner-authorised step | Passwords in a printed workbook |

## Quality Standards

- All bracketed placeholders are replaced with the client's specific details; no generic text remains.
- Platform table in Module 1 lists only the platforms the client actually uses.
- Approval workflow in Module 5 reflects the client's actual contacts and turnaround times.
- Acknowledgement messages in Module 6 include the correct business name, WhatsApp number, and response times.
- Module 4 instructions match the scheduling tool specified (Buffer / Hootsuite / other).
- Language is plain and jargon-free throughout, appropriate for non-marketing staff.
- British English spelling throughout; Uganda/East Africa, EAT, UGX and WhatsApp-first assumptions stated where they apply.
- Workbook fits within a 2-hour workshop structure (module durations total 115 minutes, leaving 5 minutes for intro and close).

## Anti-Patterns

- Handing over a workbook with "[SM Manager Name]" or "[X hours]" still in it. Fix: fill every placeholder or keep the workbook in draft with a missing-items list.
- Teaching generic social media theory in a handover. Fix: train against the client's real workflow, approver and escalation route.
- Letting staff paraphrase acknowledgement messages or quote prices. Fix: copy the standard messages exactly and escalate anything beyond acknowledgement.
- Showing "Share Now" as a normal step in the scheduling tool. Fix: schedule only approved posts and keep immediate publishing for the SM Manager's instruction.
- Treating the workshop as the whole handover for a client working alone. Fix: add the DIY handbook as the take-away.
- Sharing admin passwords in the workbook. Fix: route access through the SM Manager with the account owner's written authorisation.

## References

- [handover-workbook-modules.md](references/handover-workbook-modules.md): read when running the workshop intake or writing the cover page, Modules 1–7, the reporting template and the exercises.
- [diy-content-handbook.md](references/diy-content-handbook.md): read when the client will create and publish content without the consultant after handover (Canva, CapCut, calendar, captions, boosting, analytics, when to call the consultant).
- [`training-smartphone-video-production`](../training-smartphone-video-production/SKILL.md): read when staff need a full phone filming and editing session beyond Module 3.
- [`playbook-social-media-policy`](../../playbooks/playbook-social-media-policy/SKILL.md): read when the posting rules must become a formal governance policy.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting module copy and acknowledgement messages.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read when scoring the finished workbook or handbook before release.
- [AGENTS.md](../../../AGENTS.md): read when checking repository-wide doctrine.
<!-- dual-compat-end -->

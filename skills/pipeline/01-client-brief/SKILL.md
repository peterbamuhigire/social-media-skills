---
name: 01-client-brief
description: Use when a new client is signing on and you need the intake questions, a discovery-call guide and a written picture of their business, goals and gaps; produces the approved client brief and one-page client card; not for the production handover of an approved campaign (use `13-campaign-brief`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Client Brief Generator

Produces the full client brief and a one-page at-a-glance card from a questionnaire that doubles as a fillable client form and a discovery-call guide. Apply the `east-african-english` skill for tone throughout.

<!-- dual-compat-start -->
## Use When

- A new client has signed and we need to know their business, audience, competitors, goals, tone and budget before any strategy work.
- The consultant needs a ten-question kickstart intake to send as a form or use as a discovery-call guide.
- Discovery answers are in but patchy, so the brief must mark [TO CONFIRM] gaps and list targeted follow-up questions.
- The account team wants a one-page at-a-glance card that sums up the client for everyone working on the account.

## Do Not Use When

- `13-campaign-brief` for the execution brief of a single approved campaign.
- `02-platform-audit` once intake is approved and the next job is reviewing profiles and competitors.
- `04-brand-voice-intake` for the full voice guide and visual direction.
- Stop before drafting strategy or content while core intake answers are missing; return the questionnaire and the gap list instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Completed intake answers (ten-question bank or Part A questionnaire) | Client, or the consultant on the client's behalf | Yes | This skill generates the questionnaire itself; send it or run the two-phase kickstart, pre-fill what is known and flag the gaps. |
| Unresolved follow-up responses for [TO CONFIRM] gaps | Client after the draft brief | Before approval | Keep the [TO CONFIRM] markers and list targeted follow-up questions in Consultant Notes. |
| Current platform handles, follower counts and last-post dates | Client; public profiles | Yes | Record the platform row as unknown; do not estimate follower counts. |
| Approver name, role and turnaround time | Client | Yes | Leave the approval field open and flag it; no content goes live without a named approver. |
| Paid-social budget band and intended use | Client | Yes | Record "Not sure yet" and offer guidance on an appropriate band. |
| Validated user research, or a plan to acquire it | Client | For execution pricing | Mark the brief "speculative" and scope a discovery engagement first. |

## Workflow

1. Choose the intake route: the ten-question kickstart for a new or form-averse client, or the full Part A questionnaire (12 sections, questions 1–43 plus the positioning questions) sent as a form or used as a discovery-call guide; use the exact question wording.
2. Pre-fill anything the consultant already knows and mark every remaining gap [TO CONFIRM]; stop before drafting strategy or content while core intake answers are missing, and return the questionnaire and gap list instead.
3. Apply the three pre-brief filters before scoping or pricing: the brief-screening check, the Three Levels of UX Scope declaration and the Field-of-Dreams flag; record the result under "Brief filters applied".
4. Write the full client brief in the twelve sections of Output 1, using full sentences where appropriate and tables for structured data; compare the client's posting expectation with the recommended starting frequencies.
5. Generate the one-page at-a-glance card from the same answers, including the UX scope level and Consultant Notes.
6. Cross-check brief and card for contradictions; correct any mismatch at source and rerun both outputs from the corrected answers.
7. Run the anti-slop ship gate, then hand the approved brief to `02-platform-audit` and the tone adjectives to `04-brand-voice-intake`; positioning answers go to `biz-dev-positioning`.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Full client brief (twelve sections) | Client lead; `02-platform-audit`; strategy skills | All twelve sections covered; an empty section carries a note explaining why; gaps marked [TO CONFIRM]. |
| Client at-a-glance card | Everyone working on the account | Fits one page; fields match the brief; Consultant Notes lists at least one follow-up item. |
| Positioning answers (USP, mission, vision, niche) | `biz-dev-positioning`; client file | Recorded verbatim at intake and stored in the client file. |
| "Brief filters applied" record | Client lead; pricing | Screening result, UX scope level and speculative or execution-ready status stated. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Intake source log | Table: question, answer, source (form, call, consultant pre-fill), date | Every pre-filled answer is attributed; unconfirmed answers stay [TO CONFIRM]. |
| Risk acceptance note | Written record | Present whenever the client refuses discovery on a speculative brief and the work proceeds. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Report recipients' names and email addresses are personal data; hold them in the client file only.

## Degraded Mode

Without completed intake answers, return the narrowest qualified result and mark the affected checks `not assessed`. The questionnaire, a draft brief with [TO CONFIRM] markers and a targeted follow-up question list can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The engagement is new and no intake answers exist yet, or the client will not complete the full questionnaire | Run the two-phase kickstart in [intake-question-bank](references/intake-question-bank.md): ten standard questions, an immediate draft brief with [TO CONFIRM] markers, then ready-frontier follow-up questions. | A stalled engagement or a brief built on unconfirmed gaps. |
| The client's posting expectation is unrealistic | Flag it professionally against Uganda/EA starting frequencies: Facebook 4–5 posts per week, Instagram 3–4, LinkedIn 2–3, TikTok 3–5 short videos, WhatsApp 1–2 broadcast messages per week (not daily). | Promising a volume the team cannot sustain. |
| The request fails the brief-screening check ("killer Instagram strategy", "viral content", "posts that look like [trending brand]") | Turn each "no" into an intake question before scoping: what result it must move and for whom, which persona should do what, what promise only this client can make. | Scoping an idea that is not yet a strategy. |
| The brief has no validated user research and no plan to acquire it | Mark it "speculative", not "execution-ready", and price it as a discovery engagement first. | Delivery pricing on a speculative brief. |
| The client refuses discovery and demands execution-priced delivery on a speculative brief | Decline the work or document the risk acceptance in writing. | Unrecorded risk carried by the agency. |
| The requested outcome belongs to `02-platform-audit` or `04-brand-voice-intake` | Route there and hand over the verified intake answers already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- Both outputs are generated from the same completed questionnaire; no information is contradicted between the two documents.
- The full brief covers all twelve sections; no section is skipped or left empty without a clear note explaining why.
- Posting frequency recommendations are grounded in Uganda/EA platform norms, not generic global benchmarks.
- Content restrictions are stated plainly and unambiguously so any team member can act on them without seeking clarification.
- Tone adjectives are carried forward accurately and will be usable by the `04-brand-voice-intake` skill.
- The at-a-glance card fits a single page, declares the UX scope level, and no section contains more detail than quick reference needs.
- British English spelling is used throughout; tone follows the `east-african-english` skill.
- The consultant notes field in the at-a-glance card identifies at least one follow-up item where information is missing or unclear.

## Anti-Patterns

- Drafting strategy or content from a half-completed questionnaire. Fix: issue the draft brief with [TO CONFIRM] markers and the follow-up list, and wait for answers.
- Copying global posting benchmarks into the brief. Fix: use the Uganda/EA starting frequencies and flag unrealistic expectations.
- Pricing a speculative brief as delivery work. Fix: apply the Field-of-Dreams flag and scope discovery first.
- Writing vague content restrictions ("be careful with competitors"). Fix: state the competitor mention policy (Never / Only positively / Can reference if factual) and each banned topic in one line.
- Skipping the UX scope declaration. Fix: declare Single Interaction, Journey or Relationship in the brief and the card.
- Absorbing the platform audit or the brand voice guide into this workflow. Fix: route to `02-platform-audit` or `04-brand-voice-intake` with the verified inputs.

## References

- [Client questionnaire and output templates](references/client-questionnaire-and-output-templates.md): read when sending the Part A questionnaire, laying out the twelve brief sections and the at-a-glance card, or applying the pre-brief filters.
- [intake-question-bank](references/intake-question-bank.md): read when starting a new engagement, sending a short intake form or running a first discovery call, or writing follow-up questions for [TO CONFIRM] gaps.
- [UX strategy and product lenses](references/ux-strategy-and-product-lenses.md): read at intake when the brief involves a digital product or website-led campaign, or when stakeholders disagree about "good design".
- [`02-platform-audit`](../02-platform-audit/SKILL.md): read once the brief is approved.
- [`04-brand-voice-intake`](../04-brand-voice-intake/SKILL.md): read when building the full brand voice guide.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

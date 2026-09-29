---
name: playbook-pr-publicity
description: 'Use when a client wants press, radio or TV coverage: story angles, news releases, a publicity kit, journalist pitching, newsjacking and tracking earned media; produces the PR plan, pitch pack and media contact log; not for responding to hostile coverage or a crisis (use `playbook-crisis-communications`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# PR and Publicity Playbook

Turns genuine news into earned coverage in newspapers, radio, TV and AI answers, with a release, kit and pitch a journalist would run, and tracks it honestly.

<!-- dual-compat-start -->
## Use When
- News such as a launch, award or milestone deserves newspaper, radio or TV coverage: story angle, news release and publicity kit.
- Pitch journalists at Daily Monitor, New Vision or NBS TV by email or WhatsApp, keep a media contact log and share the coverage on our social channels.
- Newsjack breaking news, such as a Bank of Uganda rate decision, with fast expert comment set up from Google Alerts that journalists and AI search can cite.
- Plan a year-round publicity calendar of story hooks.
- Track earned media and report it without treating advertising value equivalents as results.

## Do Not Use When
- `playbook-crisis-communications` for responding to hostile media or a story already damaging the brand.
- `strategy-csr-purpose-communications` for purpose, CSR and community-impact messaging.
- `ai-generative-search-optimisation` for wider visibility in AI answers beyond news commentary.
- Stop before sending a release, pitching a journalist or quoting a spokesperson without the client's sign-off on facts and quotes.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name and industry / sector | Client brief | Yes | Ask; the angle and target outlets depend on the sector. |
| Country or city | Client | Yes | Default to Uganda / East Africa. |
| Primary goal: launch coverage, sustained brand awareness or thought leadership | Client owner | Yes | Stop; the release, kit and calendar differ by goal. |
| The news itself, with verifiable facts, data and a named spokesperson | Client, signed off | Yes for any release or pitch | Draft the angle only and mark claims unverified; do not pitch. |
| Existing media relationships and past coverage | Client or media contacts log | Conditional | Start the media list and contact log from zero; mark past coverage `not assessed`. |

## Workflow

1. Ask the intake questions in [publicity kit and release method](references/publicity-kit-and-release-method.md) and confirm who signs off facts and quotes.
2. Apply the news filter; if the story is routine promotion with no public relevance or proof, stop and rework the angle rather than pitch it.
3. Write the news release in the standard format: inverted pyramid, active voice, body under 400 words, one quote from a named person.
4. Assemble the eight-part publicity kit as one PDF or one tidy shared folder.
5. Build the media list and write the one-page query letter with a time-sensitive hook; pitch and amplify with [PR media integration](references/pr-media-integration.md).
6. For breaking news in the client's expertise, triage, produce and distribute with [newsjacking and AI citation](references/newsjacking-and-ai-citation.md).
7. Build the 12-month publicity calendar and the earned-media tracking log; review monthly.
8. Run the quality checks and the anti-slop gate; correct any failed item and rerun before anything is sent. Nothing is sent without client sign-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| News release | Client approver, then journalists | Passes the "would a journalist run this?" test; standard format; every claim verifiable. |
| Publicity kit | Journalists | All eight components at the stated lengths, delivered as one PDF or folder. |
| Query letter and media target list | Client PR lead | One printed page with a genuine hook; named outlets or outlet types for the sector and geography. |
| 12-month publicity calendar | Client owner | Names real, specific news moments with lead times; two or three per quarter at least. |
| Earned media tracking log and monthly review | Client owner | Earned impressions and share of voice calculated with sources; AVE shown only as context. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Media contacts and coverage log | Table: date, outlet, story type, journalist, status, link/clip, estimated reach | Every reach figure states its source. |
| Claim verification and sign-off record | Table: claim, source, approver, date | Each fact and quote in a release is signed off before sending. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Sending releases, pitching journalists and quoting a spokesperson each need the client's sign-off on facts and quotes.

## Degraded Mode

Without verified facts and a signed-off spokesperson, return the narrowest qualified result and mark the affected checks `not assessed`. The news-value assessment, draft angles, kit checklist and publicity calendar can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A story is promotional but lacks public relevance or proof | Rework the angle or do not pitch. | Wasting journalist trust. |
| A breaking story touches the client's expertise | Triage, produce and distribute with the newsjacking reference; pause for editorial and risk approval if the event involves harm, uncertainty or political sensitivity. | Missing the news window, or exploiting a crisis. |
| The client wants coverage in named Ugandan or East African outlets | Score the hook, pitch and amplify with the PR media integration reference; verify socially useful claims before pitching. | Unsupported publicity and wasted coverage. |
| A story is major | Offer one outlet a 48–72-hour exclusive. | Losing the best placement to a scattered send. |
| A journalist is on deadline | Answer immediately; otherwise follow up once by phone about 48 hours after sending. | Lost coverage, or pestering. |
| The target is print | Allow three to four weeks' lead time. | Missing the edition. |
| Reporting results | Report earned impressions and share of voice; show advertising value equivalent only as context, never as an outcome. | Inflated, misleading results. |

## Quality Standards

- Every release passes the "would a journalist run this?" test.
- Releases follow the standard format: inverted pyramid, no advertising language.
- The publicity kit contains all eight components at the stated lengths.
- The query letter fits on one page and has a genuine time-sensitive hook.
- The 12-month calendar names real, specific news moments, not generic "brand awareness".
- Media targets are named outlets or outlet types relevant to the client's sector and geography.
- All content uses the professional register defined in `east-african-english`.

## Anti-Patterns

- "We're excited to announce" with no reason for the reader to care. Fix: lead with the most important fact and why it matters.
- Opening the lead with the company name. Fix: open with who, what, when, where and why.
- Writing "a spokesperson said". Fix: quote a named person, with a quote that adds information.
- Pitching the editor-in-chief. Fix: read the outlet and pitch the reporter who covers the beat, starting with trade press.
- Sending a string of separate attachments or an editable document. Fix: plain text in the email body or a PDF, and one kit file or folder.
- Building relationships only when coverage is needed. Fix: read and share journalists' work and attend media events beforehand.
- Lying or spinning. Fix: never; credibility with media takes years to build and one day to lose.

## References

- [Publicity kit and release method](references/publicity-kit-and-release-method.md): read when filtering news, writing the release, building the kit, writing the query letter, using the media-relations checklist, the calendar or the tracking formulas, or citing Hahn (2003), Edwards, Edwards and Douglas (1991) or Pinskey (1997).
- [Newsjacking and AI citation](references/newsjacking-and-ai-citation.md): read when responding to breaking news with expert commentary, alerts, GEO checks and a trigger calendar.
- [PR media integration](references/pr-media-integration.md): read when building a Ugandan media list, pitching by email or WhatsApp, amplifying coverage or keeping a media contacts log.
- [`playbook-crisis-communications`](../playbook-crisis-communications/SKILL.md): read when coverage turns hostile.
- [Legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read before sending a release that makes firsts, data or regulated claims.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting releases, pitches and opinion pieces.
- [East African English standard](../../language/east-african-english/SKILL.md): read for the professional register.
<!-- dual-compat-end -->

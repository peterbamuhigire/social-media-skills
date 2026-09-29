---
name: eac-call-for-applications-campaign
description: Use when a donor, programme or accelerator opens a call for applications, expression of interest or beneficiary intake across EAC states; produces the announcement, applicant guidelines and FAQ, channel and partner-kit copy, a dissemination evidence log and fairness checklist; not for a commercial launch (use `09-campaign-strategy`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# EAC Call for Applications Campaign

Runs donor-compliant calls for applications across the EAC, which are not normal marketing campaigns: the goal is transparent access, fair and consistent information, eight-state reach, bilingual readiness where needed, applicant support, evidence of dissemination and a clean handoff into the application register. Default assumptions: Uganda/East Africa, British English, WhatsApp-first outreach, English plus French where Burundi/DRC participation matters, and evidence over vanity metrics.

<!-- dual-compat-start -->
## Use When
- A donor-funded programme, grant or accelerator is opening applications and needs the announcement and applicant guidelines.
- We need WhatsApp, LinkedIn, Facebook, email and partner-kit copy, in English and French where Burundi or DRC applicants matter.
- Applicants will ask questions and we need an FAQ and a query-response protocol so everyone gets the same answer.
- The donor or programme manager wants evidence that outreach was fair, accessible and reached all eight EAC states.

## Do Not Use When
- `09-campaign-strategy` for a commercial launch, offer or awareness drive with no beneficiary selection.
- `playbook-sms-whatsapp-marketing` for ongoing broadcasts to an opted-in list.
- `13-campaign-brief` for a creative brief handed to a production team.
- Stop if eligibility and award criteria are not confirmed, and never invent partner directories, channel statistics or association names.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Programme summary, eligibility criteria, award/scoring criteria and selection process | Programme manager or donor | Yes | Stop; no call notice is drafted without confirmed eligibility and award criteria. |
| Application form link or fields, deadline (with timezone), languages and contacts | Programme manager | Yes | Hold the affected assets with visible placeholders; never guess a deadline. |
| Target countries, applicant profile, inclusion priorities and partner networks | Programme manager; verified partner sources | Yes | Mark each state with no verified partner channel as a gap and escalate before launch. |
| Approved brand/donor wording and any disclaimers | Donor or communications lead | Yes | Use neutral wording and flag every donor-wording slot for approval. |
| Application register requirements and query escalation rules | Programme operations lead | Yes | Draft the query protocol with escalation marked `not assessed`. |

## Workflow

1. Confirm the call is a beneficiary-selection intake (route a commercial launch to `09-campaign-strategy`); stop if the eligibility and award criteria are not confirmed.
2. Write the master call notice and applicant guidelines in plain language, covering eligibility, benefits, obligations, selection process, timeline, data-use notice and contact route, and every item in the [required call-notice content](references/call-assets-and-fairness-checklist.md#required-content-in-every-call-notice).
3. Create channel-specific variants for WhatsApp, LinkedIn, Facebook, email, partner newsletters and website/news posts while preserving identical substantive terms.
4. Prepare bilingual English/French assets where francophone markets are in scope; translate meaning, not just words, and keep criteria identical.
5. Build the partner dissemination kit: intro note, short post, long post, flyer text, FAQ link, deadline reminder and evidence-log instructions; verify every partner name, link and contact close to launch.
6. Set a four-week outreach calendar with launch, mid-window reminder, final-week push and final 48-hour reminder.
7. Define the applicant query protocol: material clarifications go to all applicants or into the FAQ, not only to the person who asked.
8. Run the fairness, anti-bias, accessibility and evidence checks before launch and again before closing; correct any mismatch in criteria, deadline or benefits across channels and languages, then rerun the checks.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Call announcement and applicant guidelines | Applicants; donor | Contains every required call-notice item, including the statement that applying does not guarantee selection. |
| WhatsApp, LinkedIn, Facebook, email and partner-kit copy (English, and French where in scope) | Channel owners and partners | Eligibility, deadline, benefits and obligations identical across all channels and languages. |
| Applicant FAQ and query-response protocol | Programme team | Material clarifications are published to all applicants. |
| Outreach calendar and dissemination evidence log | Programme manager; donor reporting | Four-week calendar; log covers all eight EAC states separately. |
| Fairness, anti-bias and accessibility checklist | Programme manager | Completed before launch and before closing. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Dissemination evidence log | Table with the [log fields](references/eac-dissemination-evidence-log.md#log-fields) | Each entry has country, partner/channel, verified source, language, asset, date/time with timezone, owner and evidence. |
| Eight-state control | Row per state: Kenya, Uganda, Tanzania, Rwanda, Burundi, South Sudan, DRC, Somalia | Every state shows a verified channel or an escalated gap. |
| Fairness check record | Completed checklist, pre-launch and pre-close | Every fairness check marked pass or fail with the correction made. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Applicant data is collected only under the programme's data-use and confidentiality notice.

## Degraded Mode

Without confirmed eligibility and award criteria, return the narrowest qualified result and mark the affected checks `not assessed`. The asset structure, the query protocol, the four-week calendar skeleton and the empty eight-state evidence log can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Burundi, DRC or other francophone applicants are in scope | Produce English and French assets with identical criteria. | English-only assets that exclude eligible applicants. |
| One applicant's question produces a material clarification | Add it to the FAQ or send it to all applicants. | Unequal information access. |
| A state has no verified partner channel | Mark it as a gap and escalate before launch. | A claim of eight-state reach the log cannot support. |
| A partner directory, association, hub, chamber, WhatsApp penetration or channel statistic is proposed from memory | Verify names, links, contacts and relevance close to launch and record the source and date, or leave it out. | Invented partner lists or undated statistics. |
| A channel variant changes the deadline, criteria or benefits | Correct it back to the master notice before release. | Different terms across channels. |
| The application form is long or not mobile-friendly | Shorten it and test on a phone before launch. | Accessibility barriers for mobile-first applicants. |

## Quality Standards

- Eligibility and award criteria are identical across all channels and languages.
- The FAQ and query protocol prevent unequal information access.
- Outreach evidence can show reach across all targeted EAC states.
- Accessibility barriers are reduced: plain language, mobile-friendly instructions, deadline clarity and support route.
- No association, hub, chamber, WhatsApp penetration or channel statistic is shipped without verification and date.
- Selection-process notes include the reviewer-bias reminder, and outreach includes women-led, non-capital-city and smaller-market networks where relevant.

## Anti-Patterns

- Optimising for clicks while ignoring fairness and evidence. Fix: judge the campaign by eight-state reach and the evidence log, not engagement.
- English-only assets for a genuinely EAC-wide call involving francophone states. Fix: produce French versions with identical criteria.
- Different deadline, criteria or benefits across channels. Fix: derive every variant from the master notice and check it against the fairness checklist.
- Inventing partner lists or country networks. Fix: verify each partner close to launch and record the source and date.
- No dissemination log for donor reporting. Fix: keep the evidence log from launch, one entry per outreach action.

## References

- [Call assets and fairness checklist](references/call-assets-and-fairness-checklist.md): read when assembling the asset pack, checking the required call-notice content or running the fairness checks.
- [EAC dissemination evidence log](references/eac-dissemination-evidence-log.md): read when setting up the evidence log fields and the eight-state control.
- [`09-campaign-strategy`](../../pipeline/09-campaign-strategy/SKILL.md): read when the brief is a commercial launch with no beneficiary selection.
- [`biz-dev-positioning`](../biz-dev-positioning/SKILL.md): read when the request is really about how the programme or agency positions itself, not the call itself.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when the call makes data-use, eligibility or country-specific claims.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the notice and channel copy.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

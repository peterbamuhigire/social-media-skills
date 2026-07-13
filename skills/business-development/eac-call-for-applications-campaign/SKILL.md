---
name: eac-call-for-applications-campaign
description: Use when EAC Call for Applications Campaign is needed to produce a campaign pack for social-media or digital-marketing work; use `biz-dev-positioning` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# EAC Call for Applications Campaign

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **campaign pack** and the supplied brief falls within eac call for applications campaign.

## Do Not Use When
- Use `biz-dev-positioning` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Commercial brief, target buyer, offer, proof and requested next step | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified campaign pack; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Buyer problem, proof strength and commercial objective align | Choose the offer and proof sequence that supports the requested buying decision. | A generic sales asset with unsupported claims or the wrong ask. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact campaign pack, consumer, market, channel and approval boundary; route to `biz-dev-positioning` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete campaign pack; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Campaign pack | Requester, client reviewer or delivery team | The campaign pack addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source/assumption register and completed release checklist | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested campaign pack, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [biz-dev-positioning](../biz-dev-positioning/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Overview
Use this skill for donor-compliant calls for applications across the EAC. This is not a normal marketing campaign. The goal is transparent access, fair and consistent information, eight-state reach, bilingual readiness where needed, applicant support, evidence of dissemination, and a clean handoff into the application register.

Default assumptions: Uganda/East Africa, British English, WhatsApp-first outreach, English plus French where Burundi/DRC participation matters, and evidence over vanity metrics.

## Use When
- Launching a call for applications, expression of interest, accelerator intake, or beneficiary selection campaign.
- Creating applicant guidelines, FAQs, channel copy, partner kits, dissemination logs, and query-response protocols.
- A donor or programme manager needs proof that outreach was fair, accessible, and geographically broad.

## Do Not Use When
- The task is a commercial sales campaign with no beneficiary-selection obligations.
- The eligibility and award criteria are not known.
- You are asked to invent partner directories, channel statistics, or association names without verification.

## Required Inputs
- Programme summary, eligibility criteria, award/scoring criteria, application form link or fields, deadline, languages, contacts, and selection process.
- Target countries, applicant profile, inclusion priorities, and partner networks.
- Approved brand/donor wording and any disclaimers.
- Application register requirements and query escalation rules.

## Workflow
1. Write the master call notice and applicant guidelines in plain language. Include eligibility, benefits, obligations, selection process, timeline, data-use notice, and contact route.
2. Create channel-specific variants for WhatsApp, LinkedIn, Facebook, email, partner newsletters, and website/news posts while preserving identical substantive terms.
3. Prepare bilingual English/French assets where francophone markets are in scope. Translate meaning, not just words; keep criteria identical.
4. Build the partner dissemination kit: intro note, short post, long post, flyer text, FAQ link, deadline reminder, and evidence-log instructions.
5. Set a four-week outreach calendar with launch, mid-window reminder, final-week push, and final 48-hour reminder.
6. Define the applicant query protocol. Material clarifications go to all applicants or into the FAQ, not only to the person who asked.
7. Run fairness, anti-bias, accessibility, and evidence checks before launch and before closing.

## Quality Bar
- Eligibility and award criteria are identical across all channels and languages.
- The FAQ and query protocol prevent unequal information access.
- Outreach evidence can show reach across all targeted EAC states.
- Accessibility barriers are reduced: plain language, mobile-friendly instructions, deadline clarity, and support route.
- No association, hub, chamber, WhatsApp penetration, or channel statistic is shipped without verification and date.

## Anti-Patterns
- Optimising for clicks while ignoring fairness and evidence.
- English-only assets for a genuinely EAC-wide call involving francophone states.
- Different deadline, criteria, or benefits across channels.
- Inventing partner lists or country networks.
- No dissemination log for donor reporting.

## Outputs
- Call announcement and applicant guidelines.
- WhatsApp, LinkedIn, Facebook, email, and partner-kit copy.
- Applicant FAQ and query-response protocol.
- Outreach calendar and dissemination evidence log.
- Fairness, anti-bias, and accessibility checklist.

## References
- [references/call-assets-and-fairness-checklist.md](references/call-assets-and-fairness-checklist.md): Asset pack and fairness checks.
- [references/eac-dissemination-evidence-log.md](references/eac-dissemination-evidence-log.md): Evidence log fields and eight-state outreach controls.

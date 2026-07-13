---
name: training-diy-content
description: Use when the main deliverable concerns a self-contained client handbook for planning, creating, reviewing, and publishing content; use training-client-team when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# DIY Content Creation Handbook

<!-- dual-compat-start -->
## Use When

- Use this skill for a self-contained client handbook for planning, creating, reviewing, and publishing content.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `training-client-team` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to a self-contained client handbook for planning, creating, reviewing, and publishing content | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `training-client-team`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| A self-contained client handbook for planning, creating, reviewing, and publishing content deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
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
| The client will work independently after handover | Document repeatable checks and examples that do not require a facilitator | A workshop outline is delivered as an unusable handbook |
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

## How to Use This Skill

Collect the Required Input below. Generate each section in full, substituting all bracketed placeholders with the client's specific details. Write in a warm, jargon-free tone — this document is used by business owners and staff who are not marketing specialists. The client will refer to this independently after handover.

---

## Required Input

Ask for the following before generating the handbook:

- **Client name** — trading name of the business
- **Industry** — sector (e.g. retail, food and beverage, professional services)
- **Country / city** — default Uganda/East Africa
- **Primary goal** — what the client wants to achieve through DIY content management
- **Platforms used** — which platforms the business is active on
- **Scheduling tool name** — e.g. Buffer, Hootsuite, or Meta Business Suite
- **Content calendar location** — folder link, Google Drive path, or shared drive name
- **Consultant contact details** — name, WhatsApp number, email address
- **Brand voice 3 words** — the three tone descriptors from the brand voice guide
- **Banned vocabulary list** — words or phrases not to use in captions
- **Standard hashtag set** — the agreed hashtag bank from the hashtag strategy

---

## DIY content handbook curriculum

Load [diy-content-handbook.md](references/diy-content-handbook.md) for this part of the training curriculum.

## Quality Criteria

- [ ] All bracketed placeholders are replaced with the client's specific details — no generic text remains
- [ ] Platform template sizes in Section 1 are accurate and include all platforms the client uses
- [ ] Brand voice words, banned vocabulary, and hashtag set are inserted into Sections 4 and the caption checklist
- [ ] Content calendar location in Section 3 is filled in with the actual link or folder path
- [ ] Consultant contact details in Section 7 are complete and correct
- [ ] Tone is warm and encouraging — appropriate for a non-specialist business owner
- [ ] British English spelling throughout
- [ ] Handbook is self-contained — the client can use it without additional explanation from the consultant

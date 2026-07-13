---
name: training-ai-prompt-writing
description: Use when the main deliverable concerns practical prompt construction, critique, iteration, and marketing exercises; use training-ai-foundations when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Prompt Writing for Marketing Teams — Training Guide

<!-- dual-compat-start -->
## Use When

- Use this skill for practical prompt construction, critique, iteration, and marketing exercises.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `training-ai-foundations` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to practical prompt construction, critique, iteration, and marketing exercises | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `training-ai-foundations`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Practical prompt construction, critique, iteration, and marketing exercises deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
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
| Learners understand basic AI limits and need repeatable prompting practice | Use worked exercises with human review and verified facts | Participants copy prompts without checking outputs |
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

Collect the Required Input below. Then generate the full training guide in four modules, substituting all bracketed placeholders with the client's specific details. Output is a complete, facilitator-ready training document — not a slide deck. For a slide deck version, use the `deck-` prefix convention and build slides separately.

---

## Required Input

Ask for the following before generating the training guide:

- **Client business name and industry** — trading name and sector (e.g. telecoms, microfinance, FMCG, hospitality)
- **Country / city** — default Uganda / East Africa
- **Primary goal** — what the client wants the team to achieve after training
- **Team size and prior AI experience level** — number of participants and experience (none / basic / intermediate)
- **Primary content types produced** — captions, emails, blogs, WhatsApp broadcasts, SMS, ad copy, etc.
- **Preferred AI tools** — ChatGPT, Gemini, Claude, or other (specify versions where known)
- **Training format** — in-person half-day / virtual session / self-guided handout

---

## Output: Complete Training Guide

Generate the following four modules in full. Use the client's name, industry, preferred AI tools, and primary content types throughout. Write in plain English — no jargon. Tone: practical, encouraging, professional.

---

## Training Overview

**Programme:** AI Prompt Writing for Marketing Teams
**Total Duration:** Approximately 2.5 hours (150 minutes)
**Audience:** Marketing, communications, and content staff with any level of AI experience
**Format:** [Insert training format]
**Prepared for:** [Client Business Name]
**Industry:** [Industry]
**Primary Sources:** Upadhyay, M.A. (2024) *Generative AI for Marketing* (Packt); Anderson, D. (2022) *AI in Digital Marketing Training Guide* (Self-published)

---

## Prompt foundations and structure curriculum

Load [prompt-foundations-and-structure.md](references/prompt-foundations-and-structure.md) for this part of the training curriculum.

## Copy frameworks and practice curriculum

Load [copy-frameworks-and-practice.md](references/copy-frameworks-and-practice.md) for this part of the training curriculum.

## Quality Criteria

The completed training guide meets the standard if:

- All 4 modules are included with accurate time allocations totalling approximately 2.5 hours
- The Alpha-Beta-Gamma-Delta-Epsilon framework is explained in full with at least one complete worked example per element
- All 7 copywriting frameworks are named, defined, and illustrated with a Uganda/East Africa brand example
- Hands-on activities are specified in Modules 2, 3, and 4 — not lecture content only
- All worked examples use Ugandan/EA brands, UGX pricing, and local cultural references where relevant
- Output is structured so a non-technical facilitator can deliver it without additional preparation
- The `prompt-engineering-library` and `ai-content-humaniser` skills are explicitly referenced as companion resources
- The guide is written in British English with imperative language throughout

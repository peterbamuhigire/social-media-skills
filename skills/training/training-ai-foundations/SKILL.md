---
name: training-ai-foundations
description: 'Use when a marketing team is new to ChatGPT, Claude or Gemini and needs training: what AI can and cannot do, safe use of client data, checking outputs, and a follow-on prompt-writing workshop; produces the AI training guide with supervised exercises; not for a reusable prompt template library (use `prompt-engineering-library`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Foundations for Marketing Teams — Training Guide

<!-- dual-compat-start -->
## Use When

- Staff are using AI tools without guidance and need a beginner session on how they work, their limits and hallucinations.
- We need rules for safe use: client confidentiality, Uganda DPPA 2019 personal data, disclosure and human review.
- A team that knows the basics needs a hands-on prompt-writing workshop using the Alpha-Beta-Gamma-Delta-Epsilon structure and PAS and AIDA copy frameworks.
- Managers want supervised practice and proof that trainees can critique and improve prompts.

## Do Not Use When

- `prompt-engineering-library` for a reusable library of text, image, audio and video prompt templates.
- `training-client-team` for a social-media handover workshop or DIY content handbook.
- `policy-ai-content-ethics` for the organisation's AI content policy.
- Stop before exercises put real client personal data into public AI tools; use synthetic examples instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to beginner AI literacy for marketing teams, safe use, limitations, and supervised practice | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; decide whether the team needs foundations, the prompt-writing follow-on module, or both in sequence.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Beginner ai literacy for marketing teams, safe use, limitations, and supervised practice deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
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
| Learners lack a shared AI mental model | Teach literacy and risk before prompt technique | Prompt recipes create confidence without judgement |
| Learners understand basic AI limits and need repeatable prompting practice | Deliver the prompt-writing module from [prompt-writing-module.md](references/prompt-writing-module.md) with worked exercises, human review and verified facts | Participants copy prompts without checking outputs |
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
- [prompt-writing-module.md](references/prompt-writing-module.md) — read when the team needs the follow-on prompt-writing session (Alpha-Beta-Gamma-Delta-Epsilon, copywriting frameworks, iterative refinement); it routes to [prompt-foundations-and-structure.md](references/prompt-foundations-and-structure.md) and [copy-frameworks-and-practice.md](references/copy-frameworks-and-practice.md).
<!-- dual-compat-end -->

## How to Use This Skill

Collect the Required Input below. Then generate the full training guide across four modules, substituting all bracketed placeholders with the client's specific details. Output is a complete, facilitator-ready training document, not a slide deck. This repository has no active standalone slide-deck route; if slides are commissioned, hand the approved content to `design-system-skills`.

---

## Required Input

Ask for the following before generating the training guide:

- **Client business name** — trading name of the business
- **Industry** — sector (e.g. FMCG, hospitality, professional services, healthcare)
- **Country / city** — default Uganda / East Africa
- **Primary goal** — what the client wants the team to achieve after training
- **Team size and prior AI experience** — number of participants; experience level: none / basic / intermediate
- **Primary platforms used** — which platforms the business is active on (e.g. Facebook, Instagram, WhatsApp)
- **Training format** — in-person / virtual / self-guided handout
- **Time available** — 2-hour express / half-day full / spread across 4 weekly sessions

---

## Output: Complete Training Guide

Generate the following four modules in full. Use the client's name, industry, platforms, and city throughout. Write in plain English — no jargon. Tone: practical, encouraging, honest.

---

## Training Overview

**Programme:** AI Foundations for Marketing Teams
**Total Duration:** Approximately 2.5 hours (150 minutes) — or adapt to time available
**Audience:** Marketing and communications staff with no prior AI experience
**Format:** [Insert training format]
**Prepared for:** [Client Business Name]
**Industry:** [Industry]
**Primary Sources:** Anderson, D. (2022) *AI in Digital Marketing Training Guide* (Self-published); Ltifi, M. (ed.) (2025) *Advances in Digital Marketing in the Era of AI* (CRC Press); Farri, O. and Rosani, M. (2025) *Co-Intelligence: Working and Learning with AI*; Nayebi, H. (2025) *AI-First Marketing*

---

## Foundations and limits curriculum

Load [foundations-and-limits.md](references/foundations-and-limits.md) for this part of the training curriculum.

## Tools and human-review curriculum

Load [tools-and-human-review.md](references/tools-and-human-review.md) for this part of the training curriculum.

## Related Skills

- [prompt-writing-module.md](references/prompt-writing-module.md) — next-level training on the Alpha-Beta-Gamma-Delta-Epsilon prompt structure and copywriting frameworks; deliver this session after AI Foundations
- `anti-ai-slop` (humanising rewrite passes) — full quality control process, editing checklist, and banned vocabulary reference for AI-generated content
- `brand-voice-ai-training` — how to train AI tools on a specific brand voice
- `prompt-engineering-library` — ready-made prompt templates for common marketing content types
- `training-client-team` — general social media team training workbook for content creation and community management

---

## Co-Pilot vs Co-Thinker (Farri and Rosani, 2025)

The most important distinction for any marketing team new to AI:

**Co-Pilot mode** — AI handles speed tasks:
- Summarising documents and reports
- Drafting first versions of captions, emails, and briefs
- Generating slide content from bullet points
- Taking notes in meetings
- Formatting data into tables

**Co-Thinker mode** — AI acts as a thought partner for reflection-heavy work:
- Pressure-testing campaign strategy logic
- Mapping stakeholder perspectives the team may have overlooked
- Identifying assumptions in a brief that should be validated
- Framing the client's core marketing challenge as a solvable problem
- Generating alternative strategic options for evaluation

**When to use which:** Use Co-Pilot when you know what you want and need it done faster. Use Co-Thinker when you are not yet sure what the right answer is. Most marketing teams default to Co-Pilot only — they are leaving the most valuable AI capability unused.

**Training exercise:** Ask participants to list their last five AI interactions. Classify each as Co-Pilot or Co-Thinker. Discuss: what proportion were Co-Thinker? What would they have done differently?

---

## The Three Waves of AI in Marketing (Nayebi, 2025)

Help participants understand where they and their clients currently sit:

**Wave 1 — Automation (Most EA businesses today)**
Rules-based tools that follow fixed instructions. Examples: scheduled social posts, auto-reply chatbots, email drip sequences. No learning or adaptation. Reliable but rigid.

**Wave 2 — Predictive ML (Growing in EA)**
Systems that learn from data and predict future behaviour. Examples: audience segmentation models, engagement rate prediction, A/B test optimisation, sentiment analysis. Requires sufficient data. Improves over time.

**Wave 3 — Agentic AI (Horizon for EA)**
Autonomous agents that perceive their environment, reason about it, decide on actions, and learn from outcomes — without waiting for a human prompt. Examples: a content agent that monitors trending topics and drafts posts for approval; a campaign agent that detects low engagement and automatically triggers a response.

**Training exercise:** Ask participants to identify one marketing activity in their business at each wave level. Where is the gap between Wave 1 and Wave 2? What data or tools would be needed to close that gap?

---

## Quality Criteria

- Augmented intelligence framing is used consistently throughout — AI assists humans, it does not replace them; the junior assistant analogy is included
- All three AI types (Mechanical / Thinking / Feeling) are explained with Uganda/East Africa marketing examples
- The "What AI cannot do" section is specific and EA-calibrated — not a generic global list; Luganda/Swahili limitations and cultural intelligence gaps are named explicitly
- All 5 hands-on tools (ChatGPT, Gemini, Canva, FeedHive, Otter.ai) are verified as accessible on Android, free tier, and 3G connection; bandwidth guidance is included
- The human quality standard section includes the banned vocabulary list, the 5 signs of AI text, and the 3-step edit process
- Platform AI applications are presented as a table with EA-specific notes per channel — not a single generic list
- Output is structured so a non-technical marketing manager can facilitate the session without additional preparation
- British English spelling throughout; imperative language used in all instructions

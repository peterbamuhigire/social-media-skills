---
name: 00-client-intake
description: "Use when starting a new client engagement with standard questions and targeted follow-up. Produces completed intake record and confirmed discovery gaps; use `01-client-brief` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Client Intake — Two-Phase Kickstart

This skill runs in two phases. Phase 1 takes the client's answers to 10 standard questions and produces a draft client brief. Phase 2 analyses those answers, identifies gaps, and generates 5–7 targeted follow-up questions. After the follow-up answers are received, the brief is finalised and the engagement is ready to proceed.

Apply the `east-african-english` skill for tone throughout all outputs.

---


<!-- dual-compat-start -->
## Use When

- Use this skill for starting a new client engagement with standard questions and targeted follow-up.
- Confirm that `01-client-brief` is not the closer route before proceeding.

## Do Not Use When

- Use `01-client-brief` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Client contact, engagement context and consent to collect information | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Completed intake record and confirmed discovery gaps | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified completed intake record and confirmed discovery gaps. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Client contact, engagement context and consent to collect information is current and attributable | Produce the full completed intake record and confirmed discovery gaps and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `01-client-brief` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `01-client-brief` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the completed intake record and confirmed discovery gaps, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the completed intake record and confirmed discovery gaps without client contact. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `01-client-brief` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified client contact, the skill produces a completed intake record and confirmed discovery gaps with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`01-client-brief`](../01-client-brief/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

No prior client data is required to start. This skill generates the intake questions first, then works from the answers captured in Phase 1 and Phase 2.

## Phase 1 — The 10 Standard Questions

Present these questions exactly as written. They are suitable for a website intake form, a discovery call, or a document sent to the client. Each question owns a specific domain; together they cover all information needed for a complete client brief.

Do not reorder, split, or merge the questions. The client answers in their own words — free-form, open-ended.

---

**Question 1 — Business Overview**
Tell us about your business: what you do, what you sell or offer, how long you have been operating, how big your team is, and where you are based.

**Question 2 — Unique Value Proposition**
What makes your business different from your competitors? Why should a customer choose you over anyone else in your market?

**Question 3 — Target Audience**
Describe your ideal customer as a real person. Include their age range, gender (if relevant), location, income level or economic segment, occupation, and the specific problem your business solves for them. If you serve more than one type of customer, describe each.

**Question 4 — Social Media Goals**
What do you want social media to achieve for your business? What has prompted you to focus on this now, and what does success look like for you over the next 6–12 months?

**Question 5 — Current Social Media Presence**
Which platforms are you currently active on? For each one, tell us your handle, roughly how many followers you have, how often you post, and who manages the account today. How would you honestly rate your current performance — and what has worked or not worked so far?

**Question 6 — Competitors**
Name your top three to five competitors. For each, tell us which platforms they are on and what their social media presence looks like. Which competitor do you most admire and why — and which do you most want to be clearly different from?

**Question 7 — Brand Voice and Personality**
If your brand were a person walking into a room, how would they speak, dress, and carry themselves? Choose three words that describe how your brand should sound on social media. Name two or three brands — anywhere in the world — whose tone you admire, and two or three you absolutely do not want to sound like.

**Question 8 — Visual Identity**
Describe your visual brand: your colours (with hex codes if you have them), your fonts, and your logo status. Do you have existing brand guidelines? What overall look and feel do you want your social media content to have — and are there any visual styles you want to avoid?

**Question 9 — Resources, Budget, and Approval**
What content resources do you have available — photography, video capability, someone willing to appear on camera, a team member who writes well? What is your monthly budget for social media management and/or paid advertising? Who must approve content before it is published, and how quickly can they turn approvals around?

**Question 10 — Posting Expectations, Restrictions, and Reporting**
Which platforms do you want to prioritise, and how often do you expect content to be posted? Are there any topics, words, or approaches your brand should never use? How often would you like performance reports, and in what format? Is there anything else — upcoming launches, past challenges, sensitivities, regulated industry requirements — we should know before we begin?

---

## Phase 1 Output — Draft Client Brief

Once the 10 answers are received, generate the draft client brief immediately. Do not ask for clarification before generating — gaps and ambiguities are addressed in Phase 2.

Structure the brief using the 12 sections below. Write in full sentences where appropriate; use tables for structured data. Where an answer is missing or vague, note it clearly with the marker **[TO CONFIRM]** so it is visible for follow-up.

---

### 1. Business Overview
Name, industry/sector, founding year (or approximate age), team size, location(s), and a one-paragraph summary of what the business does and who it serves.

### 2. Target Audience
Primary audience profile: age range, gender (if stated), location, income/economic segment, occupation, and the core problem the business solves. Note secondary audiences if mentioned. State whether the business is B2C, B2B, or both.

### 3. Social Media Presence
Reproduce the platform data as a table. Add a one-line consultant commentary on each active platform.

| Platform | Handle | Followers | Posting frequency | Manager | Consultant note |
|---|---|---|---|---|---|

Below the table: summarise what has worked and what has not, as stated by the client.

### 4. Competitors
Named competitors in a table with their platform handles and a brief note on the client's view of each. Highlight the one the client most admires and the one they want to differentiate from.

| Competitor | Platforms / handle | Client's view |
|---|---|---|

### 5. Content Goals
Primary goal in bold. All secondary goals listed. Note the trigger — why the client is acting now.

### 6. Tone of Voice
Three brand adjectives. Admired brands and what the client likes about each. Brands to avoid and why.

### 7. Brand Guidelines
Colours (hex codes or description), fonts, logo status, brand guidelines status, visual style direction, and any visual restrictions.

### 8. Posting Frequency and Expectations
Client's stated expectations per platform. Flag any that are unrealistic against Uganda/EA norms:
- Facebook: 4–5 posts per week
- Instagram: 3–4 posts per week
- LinkedIn: 2–3 posts per week
- TikTok: 3–5 short videos per week
- WhatsApp: 1–2 broadcast messages per week

### 9. Budget and Resources
Budget band stated by client. Content resources available (photography, video, on-camera talent, writers). Note what is missing.

### 10. Approval Workflow
Approver name and role. Turnaround time. Approval method (email, shared drive, tool). Multiple approval stages if mentioned.

### 11. Content Restrictions
Topics to avoid. Competitor mention policy. Regulated industry requirements and disclaimers. Past incidents or sensitivities.

### 12. Reporting Preferences
Frequency, format, recipients, and priority metrics as stated. Note anything vague with **[TO CONFIRM]**.

---

## Phase 2 — Follow-Up Questions

Immediately after the draft brief, generate 5–7 targeted follow-up questions. These are not standard questions — they are generated fresh based on this specific client's answers.

**How to generate them:**

Review the draft brief against the 12 sections. For each **[TO CONFIRM]** marker and for every section where the answer is thin, contradictory, or strategically important but unclear, draft one precise question. Prioritise:

1. Anything that would change the strategic direction if answered differently
2. Missing data that blocks the `02-platform-audit`, `03-audience-personas`, or `05-social-media-strategy` skills from running
3. Contradictions between answers (e.g. a "premium brand" with a very low paid budget)
4. Vague goals that need a specific, measurable target
5. Unclear approval or reporting expectations that will cause friction in the retainer

Cap at 7 questions. If fewer than 5 gaps exist, generate only as many as needed — do not pad.

**Format each follow-up question as:**

> **[Domain] — [Question number of 5–7]**
> [The question, written directly to the client in plain language.]
> *Why we are asking: [One sentence explaining what this unlocks for the strategy or workflow.]*

---

## After Phase 2 Answers Are Received

Update the draft client brief with the follow-up answers. Replace all **[TO CONFIRM]** markers. The finalised brief is ready for handoff to:
- `02-platform-audit` — if a platform audit is needed
- `03-audience-personas` — to build audience persona documents
- `04-brand-voice-intake` — to develop the full brand voice guide
- `05-social-media-strategy` — to begin strategy development

---

## Quality Criteria

- All 12 sections of the client brief are populated or clearly marked **[TO CONFIRM]** — no section is silently skipped
- The draft brief is generated from the 10 answers without requesting further information first; gaps are handled in Phase 2
- Follow-up questions are specific to this client — none could be copy-pasted to a different client without rewriting
- Each follow-up question states why it is being asked, so the client understands its purpose
- Posting frequency recommendations are grounded in Uganda/EA platform norms, not generic global benchmarks
- Contradictions between answers are surfaced and resolved in Phase 2, not ignored
- The finalised brief after Phase 2 is complete enough for any downstream skill to run without needing to return to the client for basic information
- British English spelling throughout; tone follows the `east-african-english` skill

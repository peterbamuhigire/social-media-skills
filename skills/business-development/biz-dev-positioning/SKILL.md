---
name: biz-dev-positioning
description: 'Use when an agency or consultant needs its own positioning: niche, differentiating promise (USP), spoken pitch, mission and the proof behind them; produces the positioning statement, proof architecture and practice-building plan; not for a client brand''s segmentation and value proposition (use `marketing-foundations-stp-positioning`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Business Development — Positioning

Decides who an agency or consultancy serves and what it promises, then backs the promise with proof: USP, spoken pitch, niche, mission, vision and a preeminence plan. Default market is Uganda and East Africa.

<!-- dual-compat-start -->
## Use When
- Our agency sounds like every other agency and we need to decide who we serve and what we promise.
- We need a differentiating promise, a 30-second spoken pitch, and a mission and vision we can back with proof.
- We are choosing a niche by sector or service and want the checks done before we commit.
- I am a freelance social media consultant positioning my own practice: niche, USP testing, testimonials, LinkedIn thought leadership and a referral system.

## Do Not Use When
- `marketing-foundations-stp-positioning` for a client brand's segmentation, targeting and value proposition.
- `strategy-personal-brand` for an individual's public profile, content and monetisation as a creator or executive.
- `biz-dev-credentials` for the credentials document and case studies that present the positioning.
- Stop before claiming awards, results or client names the practice cannot evidence; mark them as proof gaps.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry or sector, and country or city | Firm owner | Yes | Ask; country defaults to Uganda / East Africa. |
| Current positioning (how the firm describes itself now, if at all) | Firm owner, website, proposals | Yes | Record "none stated" and start from the service list. |
| Primary competitor(s), named or described | Firm owner; competitor scan | Yes | Run the competitor test as `not assessed` until at least one competitor is named. |
| Primary client type to attract and what the firm most wants to be known for | Firm owner | Yes | Ask; do not choose the niche for them. |
| Revenue, referral and delivery evidence for the niche grid (invoices, referral log, delivery reviews) | Firm finance and delivery records | Conditional | Score the grid from the owner's view and label it unverified. |
| Proof held: results, testimonials, awards, client names with consent | Firm owner; consent records | Conditional | List each missing item as a proof gap; claim nothing it cannot evidence. |

## Workflow

1. Confirm whose positioning this is: a firm, or a consultant's own practice (then apply [practitioner positioning](references/practitioner-positioning.md)); route a client brand's segmentation to `marketing-foundations-stp-positioning`.
2. Ask the intake questions in the [positioning method](references/positioning-method.md#required-input); stop if the client type or competitors are unknown and cannot be supplied.
3. Define the niche: score candidate client types on the selection grid, choose where answers overlap, narrow in layers (sector, sub-sector, buyer role, geography, outcome) and state what it excludes.
4. Write the USP from service outcomes using the formula, then run the competitor test.
5. Draft the spoken pitch, mission and vision from the formulas; say the pitch aloud and check it against the failure checks.
6. Test the whole position against the five strategic checks (Pull, Focus, Access, Standing, Marketing craft); correct each failing element as the table directs and rerun the checks until all pass or the gap is named.
7. Choose one or two preeminence routes and build the 12-month action plan with named publications, events and organisations.
8. Run the `anti-ai-slop` ship gate and deliver the positioning brief with its proof register; any award, result or client name without evidence stays a proof gap.

## Statement Formulas

- USP: "We [specific action] for [specific client type] so that [specific outcome] — without [the obstacle or pain competitors leave in place]."
- Mission: "We [verb] [service or output] for [client type] so that [outcome]."
- Vision: "To be [position] in [market] by [year]."
- Spoken pitch: what we do + for whom + the result they get + why us; two or three sentences, under 15 seconds.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| USP statement and short spoken pitch | Founder and business-development lead | USP passes the competitor test; pitch runs under 15 seconds and sounds like conversation. |
| Niche definition (sector, sub-sector, buyer role, geography, outcome) | Founder; `biz-dev-credentials` | Five layers stated, with explicit exclusions. |
| Mission and vision statements | Whole team | Mission has subject, verb, client type and outcome; vision names position, market and date. |
| One-page positioning brief | `biz-dev-proposal`, `biz-dev-credentials` | Combines the above, with every claim tied to proof or listed as a gap. |
| Preeminence action plan (12 months) | Founder | One or two routes, each with named publications, events or organisations. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Niche selection grid | Table: question, evidence source, score per candidate | Each score cites invoices, referral log, delivery reviews or competitor scan, or is labelled owner view. |
| Strategic positioning check record | Table: Pull, Focus, Access, Standing, Marketing craft | Each check marked pass, fail with fix, or `not assessed`. |
| Proof register | Table: claim, evidence, consent status | No award, result or client name without evidence; gaps listed. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. A client-research survey under the Research route needs consent and data-protection compliance before any data is collected.

## Degraded Mode

Without named competitors and a chosen target client type, return the narrowest qualified result and mark the affected checks `not assessed`. Candidate niche grids and draft USP options can still be delivered for the owner to choose from.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The subject is the consultant's own practice, not a client firm | Apply [practitioner positioning](references/practitioner-positioning.md): niche and viability tests, first-person USP, proof schedule, LinkedIn plan and referral system. | Firm-level positioning that never reaches the consultant's WhatsApp, calls or proposals. |
| A direct competitor could say the USP sentence truthfully | Sharpen it: pick the outcome most valuable to the client and least offered by competitors. | A promise that differentiates nothing. |
| The pitch opens with a job title, describes inputs, is too broad or runs past 20 seconds | Rewrite from the formula and say it aloud again. | A brochure line nobody remembers. |
| The niche is too large to reach and lead, or too small to carry the revenue needed | Re-score the grid and narrow or widen one layer. | A niche the firm cannot win or cannot live on. |
| Focus check fails | Return to niche definition. | A generalist position in a specialist market. |
| Access check fails | Build the gatekeeper list in `playbook-networking`. | A plan with no trusted route to the ideal client. |
| Pull check fails | Tighten the offer; fix delivery before marketing. | Marketing that amplifies a weak offer. |
| An award, result or client name cannot be evidenced | Mark it as a proof gap; do not claim it. | Unsupported claims in credentials and proposals. |

## Quality Standards

- The USP passes the competitor test: a direct competitor could not say the same sentence.
- The spoken pitch sounds natural aloud, not like marketing copy.
- The niche states what it excludes, not only what it includes.
- The mission has a subject, a verb, a client type and an outcome.
- The vision names a position, a market and a date.
- The preeminence plan names specific publications, events and organisations.
- Content reflects the East African market where relevant.

## Anti-Patterns

- Describing services instead of outcomes ("We provide social media management services"). Fix: use the USP formula with a specific client type and outcome.
- A pitch that describes inputs ("we post three times a week"). Fix: state the result the client gets and why us.
- A niche with no exclusions. Fix: name who the firm will not serve.
- A vision with no date or market. Fix: "To be [position] in [market] by [year]".
- Treating preeminence as a campaign. Fix: commit to one or two routes for 12–36 months.
- Claiming a sector award or ranking that has not been won. Fix: record it as a proof gap or choose the Recognise route to create one transparently.

## References

- [Positioning method](references/positioning-method.md): read when asking the intake questions, writing the USP, pitch, niche, mission and vision, running the five strategic checks, choosing preeminence routes or citing the sources.
- [Practitioner positioning](references/practitioner-positioning.md): read when a consultant is positioning their own practice: niche, USP testing, social proof schedule, LinkedIn plan and referrals.
- [`biz-dev-credentials`](../biz-dev-credentials/SKILL.md): read when the positioning must be presented in a credentials pack or case studies.
- [`biz-dev-proposal`](../biz-dev-proposal/SKILL.md): read when the positioning feeds a costed proposal.
- [`playbook-networking`](../../playbooks/playbook-networking/SKILL.md): read when the Access check fails and a gatekeeper list is needed.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the USP, pitch, mission and vision.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

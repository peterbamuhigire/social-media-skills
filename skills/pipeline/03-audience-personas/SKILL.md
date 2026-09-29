---
name: 03-audience-personas
description: Use when a client needs to know who its customers are and how they behave online, including synthetic personas when there is no research budget or an audience spanning several generations; produces persona cards and a comparison matrix; not for choosing target segments and positioning (use `marketing-foundations-stp-positioning`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Audience Persona Generator

Builds 2–4 audience personas, the strategic foundation for every channel, content and messaging decision, from the client brief, platform audit findings and East African consumer behaviour; where client data is thin, apply industry knowledge and flag every assumption. Apply the `east-african-english` skill for tone throughout.

<!-- dual-compat-start -->
## Use When

- The strategy needs two to four evidence-based portraits of real customer types before channels or content are chosen.
- Client data is thin, so each persona must separate what research shows from assumptions, with problem interviews to validate them.
- There is no budget or time for primary research, so the client wants AI synthetic personas or a synthetic focus group to test a campaign concept, with a disclosure note.
- The audience spans Gen Z, Millennials, Gen X and Baby Boomers and needs trust triggers, platform mix and content formats set per generation.

## Do Not Use When

- `marketing-foundations-stp-positioning` for choosing segments, targeting, positioning and the marketing mix.
- `04-brand-voice-intake` for how the brand should sound and look once the audience is known.
- `meta-social-listening` for ongoing monitoring of what audiences say online.
- Stop before presenting synthetic or assumed persona traits as research findings; label every assumption and its source.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Completed `01-client-brief` (audience demographics, tone preferences, competitor context) | `01-client-brief` output | Yes (essential) | Ask for business name, industry, primary audience description and the client's three brand tone adjectives before proceeding. |
| Specific client industry and target market (B2C, B2B or both, with sub-segments) | Client brief | Yes | Ask; do not build personas for an unnamed market. |
| Existing customer data (WhatsApp broadcast list size, past customer records, walk-in demographics, survey results) | Client | Strongly preferred; even rough data is valuable | Apply industry knowledge, flag every assumption, and build 2 personas pending a customer interview programme. |
| Platform audit findings | `02-platform-audit` output | If available | Use the EA platform baseline and mark platform usage as assumed. |
| Country / city | Client brief | Yes | Default to Kampala, Uganda; adjust EA consumer behaviour notes for Kenya or Tanzania if relevant. |

## Workflow

1. Collect the inputs; stop and ask for the minimum brief fields if the `01-client-brief` is unavailable.
2. Decide how many personas to build from the market type (see the count rules below) and choose ONE Essential Persona per audience cluster; document the choice and the reasoning.
3. Apply the Uganda / East Africa consumer behaviour baseline (platform behaviour, consumption habits, purchasing behaviour), adjusted for income level, urban vs. rural and age cohort.
4. Fill every field of each persona card (demographics, platform usage, content, pain points, goals, follow and unfollow triggers, product fit paragraph, messaging that resonates and to avoid, assumptions flag) using the template in [persona-build-method](references/persona-build-method.md).
5. Apply the Technology Adoption Lens (TAM) to each persona and, where cohorts differ, the generational trust calibration.
6. Build the persona summary matrix and the 3–5 sentence strategic note.
7. Check each card against the quality standards; correct any unflagged inference or generic pain point and rerun the matrix and strategic note from the corrected cards.
8. Run the anti-slop ship gate and hand the personas to `04-brand-voice-intake` and `05-social-media-strategy`.

## Persona count rules

- **B2C, single product/service:** 2 personas (primary buyer, secondary influencer or gifter)
- **B2C, multiple products or broad audience:** 3 personas
- **B2B:** 2 personas (decision-maker, influencer or budget holder)
- **B2B and B2C combined:** 4 personas (2 per side)
- **If client data is very thin:** generate 2 personas and flag that additional personas should be developed after a customer interview programme

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| 2–4 persona cards, each numbered with a name and industry-specific archetype | `04-brand-voice-intake`; `05-social-media-strategy`; content team | Every field completed; mechanics floor met; assumptions flagged. |
| Persona summary matrix with strategic note | Content and channel planners | A team member can make a quick content decision without reading the full cards; the note names the priority persona, tensions and one shared platform. |
| TAM adoption assessment per persona | Channel planning | States likely and unlikely adoption and the primary barrier (usefulness, ease-of-use or trust gap). |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Assumptions Flag per persona | Quoted note on each card | Every inferred field is listed with what the client should validate it against. |
| Data-source note | Table: field, source (client data, audit, EA baseline, synthetic hypothesis) | Synthetic or inferred sources are never presented as research findings. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Customer records used for personas are summarised, never copied into the deliverable.

## Degraded Mode

Without client customer data or primary research, return the narrowest qualified result and mark the affected checks `not assessed`. Two provisional personas built on the EA baseline, with every assumption flagged and a customer interview programme recommended, can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Primary research is unavailable but personas are still needed | Build disclosed synthetic hypotheses and validate them with [synthetic-persona-hypotheses](references/synthetic-persona-hypotheses.md); commission research instead above UGX 50 million at stake. | Hypotheses presented as research findings. |
| Personas span three or more generational cohorts | Calibrate trust, platform and format per cohort with [generational-segment-lens](references/generational-segment-lens.md). | One trust approach applied to every age group. |
| Personas span several generations (Rageh, 2026) | Specify what each cohort needs before trusting a brand digitally: Gen Z brand activism and algorithmic transparency; Millennials data control and privacy signals; Generation X institutional credentials and third-party endorsements; Baby Boomers personal service access and traditional authority signals. | A single trust-building approach applied uniformly. |
| A persona's demographic fit suggests adoption of a digital service | Test Perceived Usefulness and Perceived Ease of Use (Hanlon and Tuten, 2022), including digital literacy, device quality, connectivity cost and trust in digital transactions. | Strategies that assume adoption from income or age alone. |
| A stakeholder asks "what if a user wants X?" | Answer by name: "Persona <name> doesn't need X." | Personas edge-cased to death. |
| A stakeholder disputes the Essential Persona choice | Walk them through `docs/ux-foundations.md` Section 1 ("Choosing the Essential Persona"): a design for the right Essential Persona will at least work for the others. | A blurred average persona. |
| The requested outcome is how the brand should sound or look | Route to `04-brand-voice-intake` and hand over the verified personas. | Neighbour collision and duplicated work. |

## Quality Standards

- Each persona reads as a real, specific individual, not a demographic average or a marketing archetype.
- Pain points are grounded in the client's specific industry and the Uganda/EA market context; no generic pain points.
- Platform usage tables are completed with realistic EA usage patterns; peak times align with the morning/lunch/evening framework (7–9 am, 12–2 pm, 7–10 pm).
- The "how the client's product fits their life" paragraph is specific to this persona; it could not be copied to a different persona without rewriting.
- All inferred data is flagged explicitly in the Assumptions Flag field; no invented data is presented as fact.
- The persona summary matrix enables a team member to make a quick content decision without reading the full cards.
- British English spelling throughout; tone follows the `east-african-english` skill.
- The strategic note after the matrix identifies at least one concrete implication for content or channel prioritisation.

## Anti-Patterns

- Generic archetype labels ("The Millennial"). Fix: choose or create an archetype specific to the client's industry and market.
- Generic pain points ("I want to be healthy"). Fix: write the concrete frustration, such as wasting a full morning at the government hospital for a 20-minute condition.
- Averaging four audiences into one blurred persona. Fix: a 4-persona deliverable means 4 Essential Personas, each documented.
- Letting the persona live only on its card. Fix: the "clingy" tactic: full name, photo placeholder and one memorable quote on every page that references the persona.
- Recommending data-heavy formats to data-conscious audiences. Fix: assume small screens, vertical content and limited data; avoid long autoplay videos without captions.
- Presenting synthetic or inferred personas as research. Fix: disclose them and flag every assumption for client validation.

## References

- [Persona build method](references/persona-build-method.md): read when filling persona cards and the matrix, applying the EA behaviour baseline, or applying the TAM and generational lenses.
- [Persona discipline](references/persona-discipline.md): read when building, choosing or defending personas, or validating a provisional persona with problem interviews.
- [synthetic-persona-hypotheses](references/synthetic-persona-hypotheses.md): read when primary research is unavailable and AI-synthesised personas or a synthetic focus group are needed.
- [generational-segment-lens](references/generational-segment-lens.md): read when the audience spans several generations and trust, channel, format or tone must be calibrated per cohort.
- [`04-brand-voice-intake`](../04-brand-voice-intake/SKILL.md): read when the audience is known and the voice guide comes next.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

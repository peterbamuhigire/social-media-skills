---
name: biz-dev-credentials
description: Use when a prospect asks for your agency profile, company credentials or proof of past work before a pitch; produces a credentials document, an eight-slide deck outline and one-page client case studies with a three-slide version; not for a costed scope of work for one client (use `biz-dev-proposal`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Agency Credentials Generator

Builds the agency's credentials pack for a prospect or procurement team: a written credentials document, an eight-slide deck outline and, where one result deserves it, a one-page case study with a three-slide version. Proof comes only from approved, traceable client results.

<!-- dual-compat-start -->
## Use When
- A prospect or procurement team has asked for our agency profile or company credentials before they shortlist us.
- We need a written agency overview with our founding story, services, approach, team profiles and three client success stories, plus a slide deck to present it.
- One client's results should become a standalone case study: a one-page success story with before-and-after metrics and a testimonial, and a three-slide version.
- Our proof is scattered and we need testimonials, logos, awards and numbers gathered, checked for permission and ranked by strength.

## Do Not Use When
- `biz-dev-proposal` for a costed proposal and statement of work for one named client.
- `biz-dev-positioning` for deciding the agency's niche, promise and proof architecture before the credentials are written.
- `biz-dev-pricing-menu` for service tiers, packages and rate cards.
- Stop before naming any client, result, logo or testimonial the client has not approved for publication; list it as a permission gap instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Agency name, tagline, founder name and background (history, experience, why the agency was founded) | Agency owner | Yes | Ask before generating; do not invent a founding story or year. |
| Services offered (up to 6) in plain English | Agency owner | Yes | Ask; list only services the agency actually delivers. |
| Three client results, each with a measurable outcome (anonymised is acceptable) | Consultant, client reports or platform exports | Yes | Ask for numbers; a story without a metric is held as a gap, never written as "significant improvement". |
| Team members: name, role, 3-sentence bio, key expertise areas | Agency owner | Yes | Ask; profile only the people supplied. |
| Contact details (phone, email, website, address or city) and country/city | Agency owner | Yes | Ask for contacts; country/city defaults to Kampala, Uganda. |
| Client permissions for names, logos, testimonials and data | Client consent records | Yes, before release | Anonymise with one consistent descriptor and list the permission gap. |

## Workflow

1. Confirm the prospect, the buying decision the pack must support and the approval boundary; route to `biz-dev-positioning` if the niche and promise are not yet decided, or to `biz-dev-proposal` if a costed scope is wanted.
2. Ask the intake questions in the [build method](references/credentials-build-method.md#required-input); stop until every missing item is supplied or recorded as a gap.
3. Gather and rank the proof against the six social proof sources (Bly, 2018); check permission for each named client, logo, testimonial and screenshot; stop any claim whose consent or evidence is missing.
4. Where useful, score the agency on the 16-criterion Brand Asset Scorecard (Killian, in Hahn, 2003) to decide which strengths to emphasise and which gaps to acknowledge.
5. Write the six credentials sections in order, leading with the strongest client outcome, then the eight-slide deck outline in the exact slide format; for one standalone result, follow the [case study method](references/case-study-method.md).
6. Test every superlative and result against the Fluff/Guff/Geek/Weasel Test and the Quality Standards below; correct each failing line (add the number, name the client result, or cut it) and rerun the check.
7. Run the `anti-ai-slop` ship gate, then deliver the pack with its proof and permission register and the next approval step; a blocking factual or permission defect stops release.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Written credentials document (six sections: overview and founding story, services, approach, three success stories, team profiles, contact and next steps) | Prospect or procurement team | No section skipped; continuous prose with no superlatives; each story has a specific metric. |
| Eight-slide deck outline | Presenter | Every slide carries Headline, 3–5 Bullets, Speaker Notes and Visual Direction. |
| One-page case study and three-slide version (when requested) | Prospect, proposal or website owner | Follows the case study method and its release checklist. |
| Permission gap list | Agency owner | Every unapproved client name, logo, testimonial or figure is listed, not published. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Social proof register (six sources) | Table: source, evidence held, placement, consent status | Evidence exists for at least four of six sources, or the gap is flagged to the consultant. |
| Brand Asset Scorecard (when used) | 16-row table scored 1–10 with total | Total banded 130–160 strong, 90–129 functional, below 90 investment required. |
| Claim and consent log | Table: claim, source, date, approval | Every result, quote and logo traces to a source and a consent record, or is marked unverified. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Naming a client, quoting them or showing their account data needs that client's recorded permission.

## Degraded Mode

Without measurable, approved client results, return the narrowest qualified result and mark the affected checks `not assessed`. The overview, services, approach, team profiles and deck skeleton can still be delivered, with success-story slots held as visible placeholders.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| One client result needs its own standalone case study (one-page write-up and three-slide deck) | Apply the [case study method](references/case-study-method.md): real metrics, consented name or one anonymised descriptor, never a fabricated quote. | A vague success story or an invented testimonial. |
| Evidence exists for fewer than four of the six social proof sources | Flag the missing sources to the consultant and ship with the gap shown. | A credentials document padded with embellished or vague claims. |
| The prospect is in a known sector (for example financial services) | Organise proof by client type and industry and put same-sector proof first. | A general mix that fails to convince this buyer. |
| A superlative ("the best", "leading", "premier", "world-class") appears | Support it with a number or a named client result, or remove it (Sant: Fluff/Guff/Geek/Weasel Test). | Noise that reads as self-praise. |
| Deciding what opens the pack | Lead with the most impressive client result; place credentials after the client's need is established (Sant: NOSE, Primacy Principle). | Opening with history the buyer does not care about. |
| A client has not approved publication of its name, logo or testimonial | Anonymise with one descriptor and list it as a permission gap. | Unauthorised disclosure of a client. |
| The Brand Asset Scorecard shows low-scoring criteria | Emphasise the strengths and offer the gaps as consultancy opportunities. | A deck that ignores what the prospect needs. |

## Quality Standards

- Agency overview is factual, confident, and free of superlatives or vague claims.
- Each client success story contains at least one specific metric (number, percentage, or concrete outcome).
- Team bios are professional and informative; each is distinct in voice and content.
- Deck outline follows the exact format specified in CLAUDE.md with no missing fields.
- Services are described in plain English a non-specialist business owner would understand.
- Methodology references the RACE framework (Chaffey and Ellis-Chadwick, 2022) at the appropriate step.
- Contact and next steps section includes a clear, courteous call to action.
- British English spelling throughout; no American variants.

## Anti-Patterns

- Writing "significant improvement" in a success story. Fix: use the real number from the input, or hold the story as a gap.
- Padding team bios with "passionate about" or "dedicated to". Fix: keep the three-sentence format: background, what they bring, one relevant detail.
- Opening with the founding year and history. Fix: lead with the strongest outcome; the founding year is irrelevant to the client's decision.
- Presenting a general catalogue of past activity. Fix: frame each credential as proof for a specific outcome this prospect wants.
- Writing a testimonial the client never gave, or naming a client without consent. Fix: use the placeholder and the anonymised descriptor, and record the permission gap.
- Treating the document's look as secondary. Fix: its quality, design and accuracy are Physical Evidence (Hatton) of the service; check every figure and name before release.

## References

- [Credentials build method](references/credentials-build-method.md): read when asking the intake questions, writing the six sections and eight slides, applying the formatting rules, the social proof taxonomy, the Brand Asset Scorecard or the persuasion principles.
- [Case study method](references/case-study-method.md): read when one client result needs a standalone one-page case study and three-slide deck.
- [Proposal frameworks](references/proposal-frameworks.md): read when applying NOSE, the Primacy Principle, the Fluff/Guff/Geek/Weasel Test or Hatton's Physical Evidence.
- [`biz-dev-positioning`](../biz-dev-positioning/SKILL.md): read when the niche, promise or proof architecture is not settled.
- [`biz-dev-proposal`](../biz-dev-proposal/SKILL.md): read when the prospect wants a costed scope of work.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the overview, bios and slide copy.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

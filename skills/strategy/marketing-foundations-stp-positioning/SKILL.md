---
name: marketing-foundations-stp-positioning
description: Use when a client's digital marketing or advertising programme needs segmentation, targeting, positioning, marketing-mix and value-proposition decisions before channels or creative; use biz-dev-positioning for the agency's own positioning and business-plan-skills for full plan documents.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Marketing Foundations: STP, Positioning and Marketing Mix

Turn a client's business goal into the marketing decisions every channel, advertisement and post must obey: who we serve, what we stand for in their mind, what we offer, at what price, through which routes, and which two or three messages carry the load.

<!-- dual-compat-start -->
## Use When

- A campaign, advertising plan, content strategy or website brief needs an agreed segment, target, positioning statement and value proposition first.
- A client says "everyone is our audience", lists ten benefits, or wants to rebrand without a stated reason.
- Creative keeps failing because the brief carries no single message or no reason to believe.
- A retainer review must diagnose whether weak results come from positioning, offer, price or channel.

## Do Not Use When

- The deliverable is the agency's own positioning statement or credentials; use `biz-dev-positioning` or `biz-dev-practitioner-positioning`.
- The deliverable is a full business plan or bankable marketing-plan document; hand the decisions over to business-plan-skills.
- The question is which acquisition channels to test; use `traction-channel-bullseye` after positioning is agreed.
- Required customer evidence or decision authority is absent and cannot be obtained; stop and return the intake gap.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business objective, offer list, price points and margins | Client owner or finance lead | Yes | Stop; request it or return a qualified intake list |
| Customer evidence (sales records, CRM export, enquiries, reviews, interviews) | Client systems or supplied research | Yes for final positioning | Label every segment provisional and plan a customer-insight sprint |
| Competitor list and their visible claims | Client, search and ad-library review | Conditional | Mark the competitive frame `not assessed` and avoid superiority claims |
| Market, legal or category facts | Digital Research Engine or source register | Conditional | Phrase as a check; never state as fact |

## Workflow

1. Confirm the decision, market, period and approver; stop if nobody can approve positioning.
2. Build the customer picture: segment on needs and behaviour first, then demographics and location; record sample, method and date for each insight.
3. Qualify each segment (reachable, large enough, willing to pay, incremental sales exceed tailoring cost) and choose one primary and at most one secondary target; write the excluded groups and why.
4. Map the choice set the buyer really considers, including substitutes and "do nothing"; chart the attributes competitors already own.
5. Select two or three value themes where customer importance, available proof and distinctiveness are all high; move every other benefit to supporting copy or FAQ.
6. Write the positioning statement and run the seven tests and four failure-mode checks; withhold release if the reason to believe is not a verifiable fact.
7. Set the marketing-mix decisions (product/offer, price, place, promotion, and for services people, process, physical evidence) and a Five F's message line; correct any mix element that contradicts the position, then rerun the tests.
8. Hand over a one-page foundation sheet to the brief, channel, advertising and content skills, with open assumptions and the re-test date.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Segment and target decision table | Strategist, media planner, client approver | Each segment has evidence source/date, qualification result and a keep/drop decision |
| Positioning statement with proof | Creative, copy and advertising teams | Passes the seven tests; reason to believe is checkable; no failure mode present |
| Value-theme and message sheet (2–3 themes) | `creative-brief-and-big-idea`, `ad-copy-and-hook-lab`, content skills | Every theme has proof and is distinct from the top competitors |
| Marketing-mix decision record | Client owner and business-plan-skills if a plan follows | Every mix element supports the position or is flagged for change |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Customer-insight register | Table: insight, source, sample, date, confidence | Every segment and theme traces to evidence or a labelled assumption |
| Positioning test record | Completed checklist | Seven tests and four failure modes recorded with evidence |

## Capability and Permission Boundaries

Read and search supplied files and authorised evidence. Analysis and planning are read-only. Surveys, interviews, list matching or any personal-data processing need explicit client authority and a lawful basis; publishing, spend and live-account changes need separate explicit authority.

## Degraded Mode

Without customer evidence, deliver a provisional foundation sheet with hypotheses marked `not assessed`, a customer-insight sprint plan (interviews, short survey, CRM analysis) and a re-test date. Never present a hypothesis segment as validated.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Client names "everyone" as the audience | Segment with data; choose one primary target and write exclusions | Diluted message that reaches no one well |
| More than three benefits proposed as headline messages | Score importance × proof × distinctiveness; keep the top 2–3 | Communicating everything so nothing is remembered |
| Reason to believe is an adjective | Replace with a certification, process, partnership or datum, or withhold | Unprovable claims and regulatory risk |
| Position sits close to a stronger competitor | Reframe to an ownable attribute or niche | Double or confused positioning |
| Client wants a rebrand "because we are tired of it" | Ask for the business reason; pause until one exists | Expensive repositioning with no gain |
| Price contradicts the chosen position | Fix price, offer or position before creative | Mixed signals that break trust |

## Quality Standards

- Segments are defined by needs and behaviour, then described by demographics and location (district, town or estate for East Africa).
- One label per brand: the statement says one thing clearly.
- Every claim is provable; comparative claims pass `docs/quality-gates/legal-market-release-gate.md`.
- British English, plain words, no superlative without evidence; apply `anti-ai-slop`.

## Anti-Patterns

- Treating demographics as the target ("women 25–40"). Fix: add the motive, behaviour and current alternative.
- Writing positioning from the founder's view of the company. Fix: start from customer evidence and the choice set.
- Listing ten benefits. Fix: keep two or three value themes; move the rest to FAQ.
- Borrowing a competitor's owned attribute. Fix: map owned attributes first and choose white space the brand can prove.
- Setting price after the creative is done. Fix: decide the mix before briefing creative.
- Calling a hypothesis a finding. Fix: label it, date it and schedule the test.

## References

- [Positioning and marketing-mix toolkit](references/positioning-and-mix-toolkit.md) — read when writing the statement, running the tests, mapping perceptions or setting the mix.
- [Customer insight and value-theme method](references/customer-insight-and-value-themes.md) — read when building the evidence base or choosing message themes.
- [Agency positioning](../../business-development/biz-dev-positioning/SKILL.md) — neighbour route for the agency's own position.
- [Traction channel bullseye](../traction-channel-bullseye/SKILL.md) — next step for channel choice.
- [Creative brief and big idea](../../advertising/creative-brief-and-big-idea/SKILL.md) — consumer of the message sheet.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md)
<!-- dual-compat-end -->

## Foundation sheet (one page)

| Field | Content |
|---|---|
| Business objective | Metric, baseline (source, date), target, deadline, place |
| Primary target | Needs, behaviour, current alternative, location, reachable through |
| Secondary target (optional) | As above, with trigger to activate |
| Excluded this period | Group and reason (margin, capacity, distance, law) |
| Choice set | Named competitors, substitutes, "do nothing" |
| Positioning statement | For [target and mindset], [Brand] is the [frame of reference] that [single promise], because [checkable proof]. |
| Value themes (2–3) | Theme · proof · why distinct |
| Five F's line | For [target], [Brand] means [primary F] and [secondary F]. |
| Mix decisions | Offer, price position, place/route, promotion role, people, process, physical evidence |
| Value discipline | Operational excellence, product leadership or customer intimacy, with threshold standards on the other two |
| Open assumptions | Assumption · test · owner · date |

## Worked example (labelled scenario, not client evidence)

A Kampala pest-control firm has run "50% off" posters for years. Interviews with 12 households in Muyenga and Kololo (scenario data) suggest affluent owners read discounts as "cheap and risky" and value child- and pet-safe treatment, uniformed staff and a local owner. Primary target: home-owning families in named parishes who already pay for garden and security services. Position: "For Kampala families who want a pest-free home without risking their children or pets, [Firm] is the locally owned service that treats with pet-safe products and uniformed, vetted technicians, because every treatment follows [named certification — to verify]." Value themes: safety for family, visible professionalism, quarterly bundle convenience. Mix change: replace discounts with a quarterly bundle payable by mobile money in instalments. Everything else (price per room, years in business) moves to FAQ.

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

---
name: media-planning
description: 'Use when a campaign needs a media plan: channel mix, reach and frequency, GRPs/TRPs, target CPM, flighting or pulsing, and regional or seasonal weights across radio, TV, outdoor and digital; produces the media plan, flowchart and post-buy reconciliation; not for setting the total budget (use `advertising-strategy-and-budget`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Media Planning

Decides where, when and how often the target audience should meet the message, at what cost per thousand people who matter, and how delivery will be checked against the plan. Written from established media-planning practice and Stockwell and Shaw (1994) *Direct Marketing Checklists*, NTC Business Books. The skill plans and specifies; booking and spending need explicit client authority.

<!-- dual-compat-start -->
## Use When

- The campaign needs a media plan: which channels, what weight, which weeks and how much per medium.
- Radio or Facebook? How often should people see this? Is this station worth the money?
- Compare what was booked against what actually ran, and agree make-goods for the shortfall.
- Weight the budget by region or season, for example heavier in Kampala or around Christmas.

## Do Not Use When

- `advertising-strategy-and-budget` when the total budget or objectives are not yet set.
- `traction-channel-bullseye` for choosing which acquisition channels to test at all.
- `playbook-paid-social-advertising` or `paid-search-advertising` for platform campaign builds and ad sets.
- Stop before any booking, insertion order or spend without the client's written authority.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, target audience definition and campaign period | Approved brief | Yes | Stop; request the brief |
| Approved media budget and floor | advertising-strategy-and-budget output or client | Yes | Plan scenarios at two budget levels, labelled |
| Audience data per medium (circulation audits, listenership, platform audience estimates, ad reach) | Media owners' kits, audits, platform tools, source register | Conditional | Mark in-target share `not assessed`; plan a test or research step |
| Rate cards and quotes | Media owners, platforms, suppliers | Conditional | Use labelled ranges from the client's own buying history; never quote remembered prices |
| Sales or distribution by area | Client | Conditional | Weight by population and label the assumption |

## Workflow

1. Restate objective, audience and period; stop if the target audience is undefined or "everyone".
2. Choose the delivery goal: reach-led (launch, awareness), frequency-led (complex message, competitive clutter) or response-led (leads and sales).
3. Screen each candidate medium with the four-point test and classify primary, secondary or tertiary by in-target audience share (see [media maths and selection](references/media-maths-and-selection.md)).
4. Compare media on cost per thousand in-target (target CPM), then incremental reach per shilling.
5. Set reach and frequency targets and the effective-frequency assumption for this brand and message; record the reasoning.
6. Schedule: continuity, flighting or pulsing, aligned to buying cycles, school terms, holidays and payday (see [scheduling and weighting](references/scheduling-weighting-and-post-buy.md)).
7. Weight geography by category and brand development and by distribution; do not advertise where people cannot buy.
8. Build the plan table and the post-buy template, stating every assumption and its source; run quality and anti-slop gates, correct and rerun, and withhold any rate or audience figure without a source.
9. After the flight, reconcile planned vs actual delivery and recommend make-goods or re-weighting.

## Core concepts at a glance

| Term | Definition | Formula |
|---|---|---|
| Reach | % (or number) of the target exposed at least once in the period | Unduplicated exposed ÷ target universe |
| Frequency | Average exposures among those reached | Impressions to target ÷ people reached |
| GRPs | Gross rating points across a schedule (total audience) | Reach % × average frequency |
| TRPs | Rating points among the defined target | Target reach % × target frequency |
| Effective reach | % of target reached at or above the effective frequency | From the frequency distribution |
| CPM | Cost per thousand impressions | Cost ÷ impressions × 1,000 |
| Target CPM (CPIM) | Cost per thousand in-target impressions or readers | Cost ÷ in-target audience × 1,000 |
| CPP | Cost per rating point | Cost ÷ rating points |
| Share of voice | Brand weight ÷ category weight | Brand spend or GRPs ÷ category total |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Media plan | Client approver, media buyer | Medium, rationale, in-target share, target CPM, weight, dates, cost and delivery target per line |
| Reach and frequency statement | Client and strategist | Reach %, average frequency, effective-frequency assumption and GRP/TRP total are stated with method |
| Flowchart (schedule) | Buyer and client | Week-by-week weights by medium with bursts and gaps visible |
| Post-buy reconciliation | Client and agency | Planned vs actual delivery, variance, cause and make-good action per line |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Audience and rate source register | Table | Each audience and cost figure has source and date, or is labelled an assumption |
| Medium screening table | Table | Four-point test and in-target share recorded per medium |
| Post-buy record | Table | Proof of delivery (platform exports, station logs, photographs of outdoor sites) attached or `not assessed` |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Booking, signing insertion orders, paying media owners or contacting suppliers on the client's behalf needs the same authority, and outdoor permits and regulated categories route to the legal/market release gate.

## Degraded Mode

Without audited audience or rate data, return the narrowest qualified result and mark the affected checks `not assessed`. Medium roles, schedule logic, weights as percentages of budget and a list of data to obtain can still be delivered; never convert an unaudited claim into a delivery target.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A medium's in-target share is low but it is the only route to a segment | Keep it as tertiary with a capped weight | Losing a segment for the sake of efficiency |
| Two media overlap heavily | Cost the second only against incremental in-target reach; consider alternating | Paying twice for the same people |
| Budget cannot reach effective frequency across the whole audience | Narrow the audience or shorten the flight | Wide, forgettable exposure |
| Competitors avoid a medium entirely | Test before assuming it is an untapped opportunity | Buying a medium that does not pay |
| Delivery claims come only from the seller | Require audit, logs or platform exports | Paying for undelivered spots or impressions |
| Uganda Meta ad-reach figures used for sizing | Treat as a floor, not the audience size | Under-planning because the figure reflects a blocked-platform period (register MK-02) |
| The flight overlaps an election or national event, or relies on a platform whose access is unstable (Facebook in Uganda) | Verify access at the booking date, add a pause rule and a non-internet medium (radio, SMS, outdoor), and flag outage days in the post-buy | Paying for undelivered impressions during a shutdown (registers UG-INTERNET-SHUTDOWN-2026, UG-FACEBOOK-ACCESS-2026) |

## Quality Standards

- Every medium has a role, a rationale from audience evidence and a delivery target.
- Target CPM, not headline CPM, drives comparison; incremental reach is shown when adding media.
- Effective-frequency assumption is explicit and justified for this message, not a universal "3+".
- Schedule reflects the buying cycle and local calendar; geography reflects distribution.
- A post-buy template exists before launch, and the plan acceptance checklist ([planning sequence and handoffs](references/planning-sequence-and-handoffs.md)) is complete, including a response code per medium.
- British English; UGX (or named currency); no remembered prices or audience figures.

## Anti-Patterns

- Choosing media by title prestige or headline CPM. Fix: compare cost per thousand in-target and incremental reach.
- Treating "3+ exposures" as a law. Fix: set the effective-frequency assumption per brand, message and clutter, and test.
- Spreading a small budget across many stations and platforms. Fix: concentrate to reach effective frequency in fewer places.
- Advertising where the product is not stocked. Fix: check distribution before weighting geography.
- Paying on seller claims. Fix: require logs, audits, photographs and exports; reconcile after the flight.
- Quoting a WhatsApp user figure for Uganda or Kenya without a named survey. Fix: state that no credible figure was admitted (register MK-03) and use the client's own list data.

## References

- [Media maths and selection](references/media-maths-and-selection.md): read when computing reach, frequency, GRPs, CPM or comparing media.
- [Scheduling, weighting and post-buy](references/scheduling-weighting-and-post-buy.md): read when building the flowchart, geographic weights or reconciliation.
- [East African media mix notes](references/east-african-media-mix.md): read when the market is Uganda, Kenya or the wider EAC.
- [Planning sequence, worked example and handoffs](references/planning-sequence-and-handoffs.md): read when walking the planning sequence, handing plan lines downstream, drafting plan sentences or running the acceptance checklist.
- [Advertising strategy and budget](../advertising-strategy-and-budget/SKILL.md), [attribution and measurement](../advertising-attribution-and-measurement/SKILL.md) and [direct-response economics](../direct-response-economics/SKILL.md): read when the budget, response measurement or break-even is the real question.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when outdoor permits or a regulated category are involved.
<!-- dual-compat-end -->

---
name: media-planning
description: Use when building or reviewing a media plan with reach, frequency, GRPs/TRPs, target CPM, scheduling (flighting, pulsing, continuity), medium selection, geographic weighting and post-buy reconciliation; use advertising-strategy-and-budget to set the total budget first.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Media Planning

Decide where, when and how often the target audience should meet the message, at what cost per thousand people who matter, and how delivery will be checked against the plan. Written from established media-planning practice and Stockwell and Shaw (1994) *Direct Marketing Checklists*, NTC Business Books. The skill plans and specifies; booking and spending need explicit client authority.

<!-- dual-compat-start -->
## Use When

- A campaign needs a media plan: channel mix, weights, schedule, budget by medium and delivery targets.
- A client asks "radio or Facebook?", "how often should people see this?" or "is this station worth the money?".
- A post-buy review must compare planned and actual delivery.
- Geographic or seasonal weighting of an advertising budget is needed.

## Do Not Use When

- The total budget or objectives are not yet set; use [advertising-strategy-and-budget](../advertising-strategy-and-budget/SKILL.md).
- The task is choosing which acquisition channels to test at all; use [traction-channel-bullseye](../../strategy/traction-channel-bullseye/SKILL.md).
- The task is platform campaign build (objectives, ad sets, specs); use [playbook-paid-social-advertising](../../playbooks/playbook-paid-social-advertising/SKILL.md) or [paid-search-advertising](../paid-search-advertising/SKILL.md).
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
8. Build the plan table and the post-buy template; state every assumption and its source.
9. Run quality and anti-slop gates; correct and rerun. Withhold any rate or audience figure without a source.
10. After the flight, reconcile planned vs actual delivery and recommend make-goods or re-weighting.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
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

Read and search supplied files and authorised sources. Planning is read-only. Booking, signing insertion orders, paying media owners, changing live campaigns or contacting suppliers on the client's behalf requires explicit authority. Outdoor permits and regulated categories route to the legal/market release gate.

## Degraded Mode

If audience or rate data is unavailable, return a qualified plan: medium roles, schedule logic, weights as percentages of budget, and a list of data to obtain. Mark unavailable figures `not assessed`; never convert an unaudited claim into a delivery target.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A medium's in-target share is low but it is the only route to a segment | Keep it as tertiary with a capped weight | Losing a segment for the sake of efficiency |
| Two media overlap heavily | Cost the second only against incremental in-target reach; consider alternating | Paying twice for the same people |
| Budget cannot reach effective frequency across the whole audience | Narrow the audience or shorten the flight | Wide, forgettable exposure |
| Competitors avoid a medium entirely | Test before assuming it is an untapped opportunity | Buying a medium that does not pay |
| Delivery claims come only from the seller | Require audit, logs or platform exports | Paying for undelivered spots or impressions |
| Uganda Meta ad-reach figures used for sizing | Treat as a floor, not the audience size | Under-planning because the figure reflects a blocked-platform period (register MK-02) |

## Quality Standards

- Every medium has a role, a rationale from audience evidence and a delivery target.
- Target CPM, not headline CPM, drives comparison; incremental reach is shown when adding media.
- Effective-frequency assumption is explicit and justified for this message, not a universal "3+".
- Schedule reflects the buying cycle and local calendar; geography reflects distribution.
- A post-buy template exists before launch.
- British English; UGX (or named currency); no remembered prices or audience figures.

## Anti-Patterns

- Choosing media by title prestige or headline CPM. Fix: compare cost per thousand in-target and incremental reach.
- Treating "3+ exposures" as a law. Fix: set the effective-frequency assumption per brand, message and clutter, and test.
- Spreading a small budget across many stations and platforms. Fix: concentrate to reach effective frequency in fewer places.
- Advertising where the product is not stocked. Fix: check distribution before weighting geography.
- Paying on seller claims. Fix: require logs, audits, photographs and exports; reconcile after the flight.
- Quoting a WhatsApp user figure for Uganda or Kenya without a named survey. Fix: state that no credible figure was admitted (register MK-03) and use the client's own list data.

## References

- [Media maths and selection](references/media-maths-and-selection.md) — read when computing reach, frequency, GRPs, CPM or comparing media.
- [Scheduling, weighting and post-buy](references/scheduling-weighting-and-post-buy.md) — read when building the flowchart, geographic weights or reconciliation.
- [East African media mix notes](references/east-african-media-mix.md) — read when the market is Uganda, Kenya or the wider EAC.
- [Advertising strategy and budget](../advertising-strategy-and-budget/SKILL.md); [attribution and measurement](../advertising-attribution-and-measurement/SKILL.md); [direct-response economics](../direct-response-economics/SKILL.md).
<!-- dual-compat-end -->

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

## Planning sequence in one page

1. Target universe: count the people who matter (source, date).
2. Delivery goal: e.g. "reach 60% of target at least three times in four weeks" — the "three" is this plan's assumption, not a rule.
3. Candidate media → four-point test → in-target share → target CPM.
4. Build reach with the most efficient primary medium; add secondary media for incremental reach or a different job (demonstration, response, reminder).
5. Schedule weights; check the flighting pattern against the purchase cycle.
6. Cost it; compare with the budget floor and ceiling.
7. Prepare post-buy and measurement links (codes, UTMs, WhatsApp keywords per medium).

## Worked example (illustrative figures, not market data)

A Kampala solar-home-system retailer targets 40,000 rural-edge households in Wakiso and Mukono for a six-week season. Options: a Luganda FM breakfast package; Meta (Facebook, Instagram) with geo-targeting; a boda-stage poster run. Four-point test: FM reaches the target and competitors use it; Meta reaches younger household members more than the buyer; posters reach commuters but not farms. In-target share estimates (station audience survey, platform estimate — both dated) make FM primary, Meta secondary for demonstration video and click-to-WhatsApp, posters dropped. Schedule: pulse — two heavy weeks at the start of the harvest cash window, a lighter reminder week, then a second burst. Each medium gets its own WhatsApp keyword so the post-buy can compare cost per enquiry by medium.

## Handoffs

| Output | Goes to | What is handed over |
|---|---|---|
| Platform lines of the plan | [playbook-paid-social-advertising](../../playbooks/playbook-paid-social-advertising/SKILL.md), [paid-search-advertising](../paid-search-advertising/SKILL.md) | Audience, weight, dates, delivery target, response code |
| Creative requirements per medium | [creative-brief-and-big-idea](../creative-brief-and-big-idea/SKILL.md) | Formats, durations, campaign structure (identical templates for high-frequency media; varied family for long runs) |
| Response codes and post-buy | [advertising-attribution-and-measurement](../advertising-attribution-and-measurement/SKILL.md) | Codes per medium, planned delivery |

## Sentence bank

- "[Medium] reaches about [n] people, of whom about [p]% match our target ([source, date]), giving a cost of UGX [x] per thousand in-target — the lowest of the options compared."
- "We assume [n] exposures within [period] are needed because the message is [new/complex]; we will check brand linkage at [date]."
- "Weight is concentrated in [areas] where the product is stocked and category demand is highest; [area] waits until distribution reaches [level]."
- "The schedule pulses: heavy weeks at [trigger], a lighter reminder, then a second burst before [date]."

## Plan acceptance checklist

- [ ] Target universe counted with source.
- [ ] Each medium passes the four-point test and has a class (primary, secondary, tertiary).
- [ ] Target CPM and incremental reach shown.
- [ ] Effective-frequency assumption stated and justified.
- [ ] Geography matches distribution.
- [ ] Response code per medium.
- [ ] Post-buy template and proof requirements agreed with sellers.

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

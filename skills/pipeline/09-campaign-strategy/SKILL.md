---
name: 09-campaign-strategy
description: Use when a client wants one focused push such as a product launch, offer, awareness drive, event, contest or giveaway; produces the single-campaign strategy with channel plan, timeline, budget and a one-page strategic summary; not for the supplier handover of an approved campaign (use `13-campaign-brief`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Campaign Strategy Generator

Produces a client-specific strategy for one time-bound campaign with a specific objective, distinct from always-on social media activity (covered in `05-social-media-strategy`); defaults to Uganda/East Africa.

<!-- dual-compat-start -->
## Use When

- The client has one launch, offer, awareness drive or event and needs objective, audience, core message, channels and timeline.
- The campaign needs a paid amplification plan, budget split and success measures agreed before production.
- The client wants a contest, giveaway or prize draw: entry mechanic, prize in UGX, Meta and WhatsApp promotion rules, terms and conditions, a WhatsApp mini-contest and the winner announcement.
- A hashtag challenge or seasonal promotion needs a clear concept and a content production list.

## Do Not Use When

- `13-campaign-brief` for the execution brief handed to the team or suppliers once strategy is approved.
- `creative-brief-and-big-idea` for finding the insight and screening creative ideas.
- `05-social-media-strategy` for the always-on programme rather than one campaign.
- Stop before launching a prize promotion without checking the lottery and gaming rules and platform terms that apply; flag the legal review.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry and sub-sector, country/city, and the business goal the campaign supports | Client brief or `01-client-brief` | Yes | Default the location to Kampala, Uganda; ask for the one-sentence business goal before writing the objective. |
| Campaign type and start and end dates (day-month-year) | Client lead | Yes | Stop the timeline; plan phases in relative weeks marked provisional. |
| Target persona | `03-audience-personas` or client | Yes | Ask the client to confirm the target audience before proceeding. |
| Total budget in UGX, split into production and paid spend | Client | Yes | Plan organic channels only and mark the paid plan and budget table `not assessed`. |
| Available channels | Client or channel plan | Yes | Plan only the channels the client confirms it can activate. |
| Offer, main objection, available proof, primary CTA and post-click destination | Client or consultant | Yes | Stop: the campaign concept is not ready. |

## Workflow

1. Ask the intake questions in [campaign-strategy-document-sections](references/campaign-strategy-document-sections.md) § Intake questions; route to `05-social-media-strategy` for always-on work or `13-campaign-brief` once strategy is approved.
2. Confirm the offer, objection, proof, CTA and destination; stop if they are unclear, because the concept is not ready.
3. Write the SMART objective, the target persona and the concept with its core message pressure-tested against the four questions (and the `premium-commercial-writing` message spine for premium or trust-sensitive campaigns).
4. Build the channel plan by role and cross-channel sequence, then the four-phase timeline with specific dates, using [sequence-and-proof-architecture](references/sequence-and-proof-architecture.md) for staging.
5. List every asset with specs and owners, then write the paid amplification plan and the budget table that totals to the client's stated budget.
6. For any contest, giveaway, prize draw or hashtag challenge, design it with [contests-promotions-and-gaming-rules](references/contests-promotions-and-gaming-rules.md) and flag the legal review.
7. Agree success metrics before launch and produce the one-page campaign brief.
8. Check against the quality standards; correct failing sections and rerun the check, then run the anti-slop gate and hand over to `13-campaign-brief` and the client for sign-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Campaign strategy document (ten sections) | Client lead | All ten sections present with client-specific content; no generic filler. |
| Channel plan, dated four-phase timeline and content production list | `11-content-calendar`; production team | Every channel has a role; every asset has specs, quantity, owner and due date. |
| Paid amplification plan and budget table | Client lead; media buyer | Production and paid spend separated; grand total matches the stated budget or the shortfall is flagged. |
| One-page campaign brief | `13-campaign-brief`; creative partners; client sign-off | Standalone: a designer or client could act on it without the full document. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Budget reconciliation | Table: production, paid spend, contingency, total against stated budget | Totals match or the shortfall and trade-offs are stated. |
| KPI target register | Table: KPI, target, measurement method, agreed date | Targets are specific numbers agreed with the client before launch. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Boosting posts, building audiences or launching a prize promotion is out of scope until the client approves the plan.

## Degraded Mode

Without confirmed campaign dates, budget or offer, return the narrowest qualified result and mark the affected checks `not assessed`. An objective, persona fit, concept and channel roles can still be delivered as a draft for sign-off.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The offer, objection, proof or CTA is unclear | Stop concept work and collect them first. | A campaign with nothing believable to act on. |
| Two personas are targeted | Confirm the core message works for both and note channel or content adaptations for each. | A diluted message that fits neither. |
| The campaign is premium, executive, high-ticket or trust-sensitive | Build the `premium-commercial-writing` message spine and put proof, value, objection handling and price integrity before the strongest ask. | A hard sell that breaks trust. |
| Planned boost spend is below about UGX 20,000–50,000 per day on Facebook/Instagram in Uganda | Concentrate spend on fewer posts or days; below this threshold, results are negligible. | Paid spend too thin to reach 2,000–5,000 people. |
| The budget table does not reach the stated budget or overruns it | Flag which activities to prioritise and which to reduce. | An unfundable plan. |
| The campaign includes a contest, giveaway or prize draw | Design it with [contests-promotions-and-gaming-rules](references/contests-promotions-and-gaming-rules.md), including T&Cs and lottery or gaming checks. | An unfair, non-compliant or unlicensed promotion. |
| The request is the execution brief for the team or suppliers | Route to `13-campaign-brief` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- The campaign objective is a complete SMART statement with a specific number, date and link to a business goal; the target persona is explicitly named and linked to 03-audience-personas where available.
- Cross-channel sequencing shows how platforms work together, not just a list of channels.
- The campaign timeline has specific dates (not relative weeks) derived from the client's stated campaign dates.
- The content production list includes specs for every asset type, enough for a designer to work from.
- Paid amplification notes include EA-specific minimum spend thresholds and audience targeting logic; the budget table distinguishes production costs from paid spend and totals to the client's stated budget.
- Success metrics are agreed before the campaign starts; targets are specific numbers, not "increase" or "improve".
- The one-page campaign brief is standalone and complete: a designer or client could act on it without reading the full document.
- British English spelling throughout; EAT timezone applied to all scheduling references; premium campaigns use proof, value, objection handling and price integrity before the strongest conversion ask.

## Anti-Patterns

- Letting secondary objectives dilute focus. Fix: keep one primary objective as the anchor for every campaign choice.
- Giving every channel the same job. Fix: assign roles (attention, education, proof, conversion, reminder, follow-up or retention).
- Manufacturing urgency with artificial deadlines. Fix: use last-chance messaging only when the offer has a real close date, and state it.
- Keeping assets that do not serve the core message. Fix: cut any asset that does not reinforce it.
- Producing graphics or video inside this skill. Fix: supply briefs and specs and direct the client to a designer or videographer.
- Boosting posts or launching a prize promotion during planning. Fix: hand over the plan; spend and launch need separate authority and the legal review.

## References

- [Campaign strategy document method](references/campaign-strategy-document-sections.md): read when asking the intake questions or writing any of the ten sections, including the channel table, timeline phases, production list, paid plan, budget table, KPIs and one-page brief.
- [sequence-and-proof-architecture](references/sequence-and-proof-architecture.md): read when staging attention, education, proof, offer and close for a timed campaign, launch or event.
- [contests-promotions-and-gaming-rules](references/contests-promotions-and-gaming-rules.md): read when the campaign includes a contest, giveaway, prize draw or hashtag challenge.
- [`13-campaign-brief`](../13-campaign-brief/SKILL.md): read when strategy is approved and the execution brief is needed.
- [`05-social-media-strategy`](../05-social-media-strategy/SKILL.md): read when the work is the always-on programme.
- [`creative-brief-and-big-idea`](../../advertising/creative-brief-and-big-idea/SKILL.md): read when the insight or creative idea is not yet found.
- [`premium-commercial-writing`](../../content-writing/premium-commercial-writing/SKILL.md): read for premium, executive, high-ticket or trust-sensitive campaigns.
- [`meta-reporting`](../../meta-analytics-ops/meta-reporting/SKILL.md): read when structuring the post-campaign report.
- [Finished campaign exemplars](../../../docs/world-class-exemplars/campaign-exemplars.md): read when checking the finished standard.
- [Creative review gate](../../../docs/quality-gates/creative-review-gate.md): read before creative sign-off.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when the campaign runs a prize promotion or makes market claims.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

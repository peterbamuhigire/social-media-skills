---
name: meta-budget-planner
description: Use when a client asks how to split a confirmed marketing budget across channels, content production, tools and contingency, or how many leads a revenue target needs; produces the budget allocation plan and bottom-up revenue plan with a CAC ceiling; not for setting the paid-media budget (use `advertising-strategy-and-budget`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Meta Budget Planner

Splits a confirmed monthly marketing budget across channels, content production, tools and contingency, and ties it to revenue through a bottom-up plan and a CAC ceiling. Amounts are in UGX and calibrated for the Uganda/East Africa market as of 2026; confirm exchange rates, tool subscription costs and freelance rates before presenting any plan.

<!-- dual-compat-start -->
## Use When

- The marketing budget is confirmed, say UGX 1.5 to 5 million a month, and the owner asks how to divide it across channels, production, tools and a reserve.
- The client wants to know which budget tier fits them and what Starter, Growth or Scale spending buys.
- Work back from next year's sales or revenue target to the enquiries, deals and opportunities each channel must bring in, the most we can afford to pay to win a customer (CAC ceiling), a weighted pipeline forecast and deal velocity targets.
- A quarterly budget review should move money from weak channels to proven ones.

## Do Not Use When

- `advertising-strategy-and-budget` for paid-media objectives, the ad budget floor and ceiling and spend release phases.
- `meta-roi-framework` for proving the return on money already spent.
- `media-planning` for the media schedule, flighting and weights.
- Stop before committing, moving or spending money; deliver the plan for the client's approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Total monthly digital marketing budget (UGX or USD) | Client owner or finance lead | Yes | Stop the allocation; if a revenue target exists, build the bottom-up revenue plan first and let its CAC ceiling set the budget. |
| One SMART objective for the next 6 months | Client brief | Yes | Return the objective question; do not allocate against "general growth". |
| Current channels and monthly spend per channel, including zero-spend channels | Client or ad-account exports | Yes | Rank channels as low priority (no prior evidence of paid return) and keep the paid mix to one platform. |
| Cost per result from previous paid activity and organic reach per channel | Client-authorised platform exports | If available | Mark the ranking provisional and fund a small test (UGX 50,000–200,000) before scaling. |
| Revenue target, average deal value and historical conversion rates | Client finance or sales lead | For a revenue plan | Apply the Kahan (2022) benchmarks labelled as benchmarks, not client results. |
| Team size, constraints and non-negotiables | Client lead | Yes | Record "not stated" and flag any fixed line (for example a WhatsApp Business API subscription) as an assumption. |

## Workflow

1. Ask the intake questions ([budget tiers and allocation method](references/budget-tiers-and-allocation.md) § Intake questions); stop if there is no confirmed budget or objective, and route paid-media floors and phases to `advertising-strategy-and-budget`.
2. When the budget must come from a revenue target, build the [bottom-up revenue plan](references/bottom-up-revenue-plan.md) first and carry its CAC ceiling forward.
3. State the five budget principles and show how each changes this client's allocation.
4. Match the client to a tier (Starter, Growth or Scale); present the lower tier as the base when the budget falls between tiers and note what the higher tier adds.
5. Apply the four-step channel allocation framework to the client's actual channels, then price content production from the EA rate table.
6. Calculate ROI per channel with the client's own figures (or a labelled worked example) and check actual CAC against the ceiling.
7. Build the monthly, quarterly and annual review cadence with a named owner for each review.
8. Run the quality standards and the anti-slop gate; correct any line that does not map to the objective or breaches the CAC ceiling and rerun the check before hand-over. Deliver the plan for approval; never commit, move or spend money.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Budget allocation plan (tier table, channel ranking, content budget, contingency) | Client owner or finance approver | UGX amount and percentage on every line; every line maps to the objective or is flagged for removal. |
| Bottom-up revenue plan with CAC ceiling | Client owner; sales lead | Funnel maths, channel inquiry targets and CAC ≤ CLV × 0.25 shown; benchmarks labelled. |
| Review cadence | Named budget owner | Monthly, quarterly and annual reviews with owners and reallocation triggers. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| ROI and CAC workings | Table per channel: TLV, COCA, ROI, CAC ceiling | Client figures and benchmark figures labelled separately; formula cited (Bodnar and Cohen, 2012; Kahan, 2022). |
| Rate and exchange-rate log | Table: item, rate, source, date | Every UGX rate and the UGX 3,700 = USD 1 estimate confirmed with the client or suppliers, or marked unconfirmed. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. The plan goes to the client for approval; committing, moving or spending money is the client's decision.

## Degraded Mode

Without a confirmed budget ceiling or channel cost evidence, return the narrowest qualified result and mark the affected checks `not assessed`. The tier comparison, the channel ranking logic and a bottom-up revenue plan on labelled benchmarks can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client needs the budget derived from a revenue target, a funnel-based lead volume plan or a weighted pipeline forecast | Build the revenue plan with [bottom-up-revenue-plan](references/bottom-up-revenue-plan.md) first; cap the budget at its CAC ceiling (CAC ≤ CLV × 0.25). For customer value, use CLV (revenue × transactions × years, Kahan 2022) when purchase frequency is known and the simpler TLV (revenue × lifespan, Bodnar and Cohen 2012) otherwise; name the formula used. | An activity budget with no link to revenue, or a budget that buys customers at a loss. |
| The requested outcome belongs to `meta-roi-framework` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |
| A channel is untested | Run small paid experiments (UGX 50,000–200,000 per test) and commit no more than 30% of the paid budget to it in the first month. | Large spend on an unproven channel or creative. |
| Ranking channels for paid budget | Put a minimum of 70% of the paid budget into the highest-priority channel and keep no more than three channels in the paid mix. | Spreading across four or more channels, which makes measurement impossible. |
| Budget is at Starter tier | Focus all paid spend on one platform (Facebook is the default for Uganda/EA) and add no second paid channel until organic engagement is consistent. | Thin spend that proves nothing. |
| A channel has spent more than 15% above plan in the monthly review | Pause and investigate before continuing. | Silent overspend. |
| A channel's ROI is below zero | Pause and diagnose; optimise at 0–1.0, maintain and test scaling at 1.0–3.0, consider more budget above 3.0. | Scaling a channel that loses money. |
| The client asks how their budget compares with other companies | Use a dated, cited peer benchmark such as the Gartner 2025 CMO Spend Survey (register `GARTNER-CMO-SPEND-2025`; Secondary, Vendor research; figures `NOT_ASSESSED` until the release is read) as context only; state its sample, regions and firm sizes and never set the budget from it. | Copying a large-company budget ratio onto an East African SME. |
| A channel decision rests on less than 90 days of data | Wait for full data before adding or removing the channel. | Reallocating on noise. |

## Quality Standards

- All three tier templates are present with UGX amounts and percentages on every line; the client's tier is identified and highlighted.
- The channel allocation framework is applied step by step to the client's actual channels and stated objective, not presented as a generic template.
- The content production table uses EA market rates in UGX with freelance versus agency guidance matched to the client's tier.
- The ROI formula (Bodnar and Cohen, 2012) is cited, defined and applied with the client's own figures where available, or with worked examples where they are unknown.
- A monthly, quarterly and annual review cadence has named responsibilities and specific reallocation triggers.
- Owned before paid is applied: at least one owned-channel line (email, WhatsApp or blog) at Tier 2 and above.
- Every budget line maps to the stated objective; any line that cannot be justified is flagged for removal or deprioritisation.
- Actual CAC is confirmed below the CAC ceiling before the plan goes to the client or board.

## Anti-Patterns

- Allocating a budget with no link to revenue. Fix: work back from the revenue target to required leads and cap spend at the CAC ceiling.
- Paying to amplify weak content. Fix: fund content production first, then amplify the posts with the strongest organic engagement.
- Scaling paid media before building owned assets. Fix: include an email or WhatsApp list-building line at every tier.
- Carrying last year's allocation forward. Fix: reset from the objective at the annual review.
- Recommending Google Ads for a client without a functional website and conversion tracking. Fix: hold that line until tracking exists.
- Drafting influencer contract terms inside the budget plan. Fix: refer influencer contracts to a legal professional.
- Presenting benchmark conversion rates as the client's own. Fix: label Kahan (2022) figures as benchmarks until client data replaces them.

## References

- [Budget tiers and allocation method](references/budget-tiers-and-allocation.md): read when asking intake questions, stating the five principles, presenting tier tables, ranking channels, pricing content, setting the review cadence or calculating ROI (TLV and COCA definitions).
- [Bottom-up revenue plan](references/bottom-up-revenue-plan.md): read when the plan must start from a revenue target: funnel maths, channel inquiry targets, CAC cap (CLV definition), weighted pipeline, velocity and monthly funnel review.
- [`meta-roi-framework`](../meta-roi-framework/SKILL.md): read when the client needs a full per-channel ROI model and attribution methodology.
- [`meta-testing-framework`](../meta-testing-framework/SKILL.md): read before designing any new paid channel test.
- [`09-campaign-strategy`](../../pipeline/09-campaign-strategy/SKILL.md): read when the objective needs refining into campaign-level tactics.
- [`peso-integrated-strategy`](../../strategy/peso-integrated-strategy/SKILL.md): read when a fully integrated Paid/Earned/Shared/Owned channel strategy is needed before the budget is finalised.
- [`advertising-strategy-and-budget`](../../advertising/advertising-strategy-and-budget/SKILL.md): read when the question is the paid-media budget floor, ceiling or spend release phases.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the plan.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

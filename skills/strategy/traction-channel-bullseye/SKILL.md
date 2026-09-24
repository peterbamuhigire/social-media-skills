---
name: traction-channel-bullseye
description: Use when choosing which acquisition channels a business should test and fund, from all nineteen traction channels, with capped parallel tests and a critical path; use strategy-channel-architecture to assign roles inside channels already chosen.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Traction Channel Bullseye

Choose where customers will come from by considering every recognised acquisition channel, testing the three most promising in parallel with capped budgets, and funding the one the numbers favour (Weinberg & Mares, 2014).

<!-- dual-compat-start -->
## Use When

- A client arrives asking for one fashionable channel ("we need TikTok") before anyone has compared alternatives.
- A marketing or advertising plan needs a defensible channel section with cost and volume assumptions.
- Growth has flattened and the current channel is saturating or decaying.
- A new market, segment or product needs its first customers.

## Do Not Use When

- The channels are already chosen and the task is role, flow and effort within them; use `strategy-channel-architecture`.
- The task is scheduling and weighting paid media inside a chosen mix; use `advertising/media-planning`.
- Positioning and target are not agreed; run `marketing-foundations-stp-positioning` first.
- A regulated or contractual route is mandatory (for example a public tender); follow that route instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Traction goal, product phase and what reaching it changes | Client owner | Yes | Stop and agree the goal first |
| Unit economics: price, gross margin, allowable acquisition cost | Client finance; chwezi-accounting-doctrine for method | Yes for focus decisions | Run tests only; mark focus decision `not assessed` |
| Positioning and target segment | `marketing-foundations-stp-positioning` output | Yes | Label channel ideas provisional |
| Tracking readiness (codes, tagged links, "how did you hear" field) | Client or implementation team | Yes before tests | Build tracking first; do not start tests |
| Test budget and time | Client approver | Yes | Produce the ranked plan only |

## Workflow

1. Confirm the traction goal, the phase (first customers, product–market fit, scale) and the "needle-moving" threshold; stop if no goal exists.
2. Brainstorm at least one realistic idea for each of the 19 channels, using the East African vocabulary in the reference; score probability, expected acquisition cost, volume available at that cost and test time.
3. Rank ideas into inner (A), potential (B) and long-shot (C) rings; pick three inner-circle channels.
4. Write a test card per channel (hypothesis, cap, duration, metric, success line, tracking method, owner); withhold any test without working tracking.
5. Run the three tests in parallel and read weekly; stop a test early if it breaches its cap or a legal/consent check fails.
6. Decide focus, extend or drop with reasons; hand the winner to the channel, advertising and testing skills for optimisation.
7. Set re-run triggers (flat growth for two months, rising cost, saturation) and recover by re-running the Bullseye with the data gathered.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| 19-channel idea sheet with ring ranking | Client approver and strategist | Every channel has at least one idea and a score; bias sources noted |
| Three test cards | Delivery team and media buyer | Each card has cap, duration, metric, success line and tracking method |
| Focus decision memo | Client owner, finance | Decision cites cost per qualified outcome against allowable cost |
| Critical path with "not doing" list | Project owner | Only necessary milestones remain, in dependency order |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Test log | Table: channel, spend, outcomes, cost per outcome, quality notes | Figures trace to tracked sources; untracked results excluded |
| Decision record | Memo | States the rule applied and the evidence behind it |

## Capability and Permission Boundaries

Read and search supplied data and authorised sources. Planning is read-only. Running tests that spend money, contact people, list on platforms or process personal data needs explicit client authority, a lawful basis and a named owner.

## Degraded Mode

Without economics or tracking, deliver the ranked idea sheet and draft test cards marked `not assessed` for cost and focus, plus the tracking set-up list. Do not recommend a focus channel.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Client insists on one channel | Complete the 19-channel sheet anyway; test the requested channel alongside two others | Channel bias and missed cheaper routes |
| No tracking in place | Build unique links, codes, keywords and "how did you hear" first | Tests that cannot be read |
| Retention leaks (customers do not return) | Fix activation/retention before scaling acquisition | Pouring money into a leaky bucket |
| A channel cannot reach the needle-moving volume at allowable cost | Drop or park it this phase | Chasing blips |
| Winner's cost rises or volume flattens | Treat as decay; re-run the Bullseye | Assuming a channel lasts forever |
| Budget too small for three parallel tests | Test sequentially, strongest first | Spreading below a readable level |

## Quality Standards

- Channel ideas are specific and local (named station, association, WhatsApp channel, fair), not generic.
- Tests are cheap and small; optimisation starts only after a channel shows promise.
- Every figure carries source and date; book examples are never benchmarks.
- Language is professional: "decay" and "saturation", not startup slang.

## Anti-Patterns

- Choosing only familiar or fashionable channels. Fix: force one idea for each of the 19 channels.
- Testing everything at once or one thing for months. Fix: three inner-circle tests in parallel, capped.
- Optimising before validating. Fix: test first; optimise only a proven channel.
- Scaling acquisition while customers churn. Fix: pass the retention check first.
- Buying lists or using black-hat tactics to feed a channel. Fix: permission-based lists and legitimate methods only.
- Treating US prices from the book as local benchmarks. Fix: build local cost assumptions from rate cards and own tests.

## References

- [Bullseye procedure, 19 channels and East African forms](references/bullseye-channels-and-test-cards.md) — read when brainstorming, writing test cards or deciding focus.
- [Critical path, phases and traction maths](references/critical-path-and-traction-maths.md) — read when setting the goal, thresholds and milestone plan.
- [Channel architecture](../strategy-channel-architecture/SKILL.md) — next step once channels are chosen.
- [Ad testing and scaling](../../advertising/ad-testing-and-scaling/SKILL.md) — optimisation of a winning paid channel.
- [Marketing foundations](../marketing-foundations-stp-positioning/SKILL.md) — prerequisite positioning.
<!-- dual-compat-end -->

## Plan section slot template

"We assessed all 19 recognised acquisition channels for [business] in [location]. Three show the strongest case for [phase]: [A], [B] and [C], because [evidence]. Each will be tested for [n] weeks with a cap of UGX [x], judged on cost per [qualified outcome] against an allowable UGX [y]. The best performer receives [z]% of the year-one budget; the others are dropped or parked. We will re-run this assessment when monthly growth falls below [threshold] for two consecutive months."

## Before and after

- Generic: "We will use social media, radio, SEO and events to increase brand awareness."
- Professional: "We will test three channels: Facebook lead ads in Wakiso, a two-week Luganda FM morning-show package, and a stand at a regional agricultural expo, each capped at UGX 1.5m, then fund the one with the lowest cost per qualified farmer enquiry." (Scenario figures.)

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

---
name: meta-testing-framework
description: 'Use when a client wants to know whether one caption, format, audience or offer truly beats another: hypotheses, one variable at a time, sample size, significance and decision rules; produces the test plan, test register and result interpretation; not for scaling or killing live paid ads (use `ad-testing-and-scaling`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# meta-testing-framework

A structured approach to experiment design, A/B testing, and result interpretation for social media content and campaigns in Uganda and East Africa.

<!-- dual-compat-start -->
## Use When

- The team wants to prove what works rather than guess: which hook, format, language (Swahili or English) or offer wins.
- A test needs a hypothesis, one changed variable such as caption style or format, guardrail metrics, a sample size and run length, and a rule for calling the winner.
- Results from a Meta Ads Manager A/B test or an organic post comparison need reading correctly, including negative results.
- A monthly testing calendar is needed that avoids holiday and school-fees periods in Uganda and East Africa.
- Learning from finished tests must be logged and fed into the next campaign.

## Do Not Use When

- `ad-testing-and-scaling` for deciding which live ads to scale, kill or refresh and how to raise budgets.
- `meta-algorithm-guide` for the platform ranking reference and posting-time schedule.
- `advertising-attribution-and-measurement` for incrementality, holdout or geo tests on ad spend.
- Stop before declaring a winner on a sample too small to call; report it as inconclusive.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Primary goal and what the client wants to test (creative, copy/caption, audience segment, CTA or posting time) | Client | Yes | Stop; propose the priority order (hook first) and ask which decision the test must inform. |
| Platform focus and access to analytics (Meta Ads Manager, TikTok Ads Manager, native insights or none) | Client | Yes | Without analytics access, run only organic tests measured from screenshots at 48 hours. |
| Current monthly ad budget in UGX or USD, or "organic only" | Client | Yes | Use Template B organic post tests; never plan a paid test below UGX 30,000. |
| Baseline for the primary metric and sample constraints | Platform exports or tracking sheet | Yes | Mark the decision threshold provisional and treat the first round as directional. |
| Duration the client can commit (minimum 7 days) and blackout dates | Client | Yes | Check the Uganda/East Africa periods to avoid and schedule outside them. |
| Client name, industry, country and city | Client brief | Yes | Default to Uganda. |

The intake list is in [testing method](references/testing-method.md) § Required Inputs.

## Workflow

1. Confirm the intake and name the audience problem and the decision the test informs; stop and route to `ad-testing-and-scaling`, `meta-algorithm-guide` or `advertising-attribution-and-measurement` when the request is scaling live ads, posting-time reference or incrementality.
2. Apply the practical-significance filter: if a realistic positive result cannot move COCA by a meaningful margin, deprioritise the test (Bodnar and Cohen, 2012).
3. Pick the element by priority (hook, format, CTA, audience, posting time, caption length, hashtags) and change one variable only.
4. Fill Template A, B or C with hypothesis, control, variant, budget split, duration, primary metric, guardrails and a numeric decision rule before launch.
5. Check each variant on mobile (legible without expanding, thumb-reachable CTA, watchable with sound off) and for audience empathy, accessibility and cultural fit before any performance reading.
6. Run for 7 days to 4 weeks without stopping early or editing the creative; if the client asks for an edit, stop the test, record it inconclusive and restart.
7. Read the results against the sample thresholds and confidence rule, log every test (including inconclusive ones) in the tracking sheet with anomalies in Notes, and correct distorted rounds by rerunning outside blackout periods.
8. Apply the [Kaizen campaign learning loop](references/kaizen-campaign-learning-loop.md): preserve the audience problem, narrative job, failed/inconclusive result, standardisation decision, and next baseline.

Principles, templates, the tracking sheet, result reading, the calendar and EA adjustments are in [testing method](references/testing-method.md).

## Thresholds and blackout periods

- Paid tests: 50 conversions per variant or 1,000 impressions per variant, whichever comes first; act only at 90% confidence or above.
- Organic tests: 200 organic reach per post or 48 hours after publishing, whichever comes later; margin under 5 percentage points is inconclusive.
- Duration: minimum 7 days, maximum 4 weeks; 1–2 tests per month.
- Micro-budget paid tests: UGX 50,000–200,000 (approximately USD 13–53) per test.

| Period | Approximate dates |
|---|---|
| Ramadan | Varies (lunar calendar) |
| Christmas / New Year | 20 Dec – 5 Jan |
| Uganda Independence Day | 9 October |
| School holidays (Uganda) | Jan, Apr, Aug, Dec |
| Election periods | As declared |
| End of financial year | June (public sector) |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Test design (Template A, B or C) | Client lead and whoever runs the ads or posts | Every field is filled before launch, including a numeric decision rule and next action. |
| Testing calendar | Client lead | 1–2 tests per month, clear of the blackout periods relevant to the product and audience. |
| Result interpretation | Client; `meta-reporting` | States winner, inconclusive or distorted, with the threshold met and the change to next month's plan. |
| Campaign learning record | `09-campaign-strategy` and the content team | Follows the Kaizen minimum record with decision and next baseline. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Tracking sheet (Google Sheets) | Columns Test # to Action plus Notes | Every test is recorded, including inconclusive ones, with confidence % (paid) or "Directional" (organic). |
| Result screenshots or exports | Native insights at exactly 48 hours, or the Ads Manager A/B test panel | Dated and attached to the test number. |
| Guardrail check | Table: readability, accessibility, trust, accuracy, complaints per variant | A variant that worsens a guardrail is rejected or rolled back whatever its metric lift. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Launching a test, splitting a budget or editing a live ad is a live account change and needs that authority.

## Degraded Mode

Without a baseline and access to platform results, return the narrowest qualified result and mark the affected checks `not assessed`. A filled test template, the calendar and an organic Template B plan can still be delivered; the result reading waits for data.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Two or more elements differ between control and variant | Redesign so only one element changes; enforce it even when the client pushes back. | Unattributable results and wasted budget. |
| One variant appears to be winning before the end date, or Meta shows a winner early | Keep the test running to the scheduled end. | Inflated effect size from early stopping. |
| Organic test on a small account (under 5,000 followers or under UGX 500,000/month ad spend) | Use directional data; run three rounds of the same test type before concluding. | False certainty from an underpowered test. |
| A public holiday, major event or outage falls inside or between test windows | Flag the result as distorted in Notes and weight or discard it. | Seasonal effects credited to the content. |
| Budget is below UGX 30,000 | Do not run the paid test; use an organic test. | A sample too small to be directional. |
| LinkedIn paid testing is proposed for a typical Ugandan client | Advise against it; CPM is too high for the addressable audience. | Spend with no usable result. |
| A variant lifts the metric but worsens readability, accessibility, trust, accuracy or complaints | Reject or roll back the variant. | Standardising a harmful pattern. |
| The requested outcome belongs to `meta-algorithm-guide` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- Every hypothesis follows the exact format "Changing [element] from [A] to [B] will increase [metric] because [reason]"; no vague or untestable hypotheses are accepted.
- The one-variable rule is enforced without exception; each test isolates exactly one element.
- The tracking sheet is populated with column guidance specific to the client's platform and metric, not left as a generic blank.
- Every test design includes a precise decision rule with a numeric threshold (for example 10% improvement, 1,000 impressions minimum); no open-ended "we'll see how it goes".
- Budget recommendations are calibrated to EA realities: micro-budget paid tests (UGX 50,000–200,000) or organic-only templates when no paid budget exists.
- Minimum sample sizes are stated explicitly (50 conversions or 1,000 impressions for paid; 200 organic reach or 48 hours for organic) and applied to the platform in scope.
- The testing calendar flags at least the Uganda-specific blackout periods relevant to the client's product category and audience.
- Every proposed variant is checked for audience empathy, information hierarchy, mobile readability, accessibility, cultural fit, and one clear action before performance interpretation.

## Anti-Patterns

- Declaring a winner too early, the most frequent error. Fix: enforce the minimum duration and sample size rules with every client.
- Not controlling the audience in paid tests; even one interest difference invalidates the comparison. Fix: keep an identical audience definition for both variants.
- Comparing results across platforms. Fix: run platform-specific tests; a Facebook result does not transfer to TikTok.
- Assuming video always wins. Fix: test format; static images often produce higher click-through for product offers.
- Treating a metric lift as a win when readability, accessibility, trust, accuracy, or complaint guardrails worsen. Fix: reject or roll back the variant.
- Designing a test around a clever hook without naming the audience problem or decision. Fix: return to the narrative job and baseline.
- Deleting negative or inconclusive results. Fix: record every test; over 6–12 months the log shows the patterns.

## References

- [Testing method](references/testing-method.md): read when applying the principles, choosing what to test, filling a template, keeping the tracking sheet, reading results, building the calendar or adapting to EA budgets and small accounts.
- [Kaizen campaign learning loop](references/kaizen-campaign-learning-loop.md): read when closing a test and setting the next baseline.
- [Narrative, audience empathy, and content quality audit](../meta-content-audit/references/narrative-empathy-and-content-quality.md): read when checking variants before performance interpretation.
- [`meta-algorithm-guide`](../meta-algorithm-guide/SKILL.md): read for posting-time and frequency tests and the ranking reference.
- [`meta-reporting`](../meta-reporting/SKILL.md): read after test completion to place results in the monthly reporting cycle and format them for the client.
- [`meta-roi-framework`](../meta-roi-framework/SKILL.md): read when judging whether a test's potential upside justifies the time and budget before designing it.
- [`09-campaign-strategy`](../../pipeline/09-campaign-strategy/SKILL.md): read when results must become campaign decisions or a test sits inside a wider campaign.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when writing variant copy; [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

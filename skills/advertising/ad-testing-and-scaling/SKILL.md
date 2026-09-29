---
name: ad-testing-and-scaling
description: Use when ads need testing before the main budget goes out, results must be read to scale, kill or refresh, organic reach has dropped and proven posts need boosting, or a retargeting pool is needed; produces test cards, a results read-out and a scale plan; not for general experiment statistics (use `meta-testing-framework`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Ad Testing and Scaling

Tests small and many before the bulk of a budget is spent, decides with pre-agreed lines, and scales winners in controlled steps while watching fatigue, frequency and unit economics. Covers message-angle testing, retargeting pools, comparative ads and the retest-to-roll-out ladder.

<!-- dual-compat-start -->
## Use When

- We want to try a few ad angles cheaply before committing the main campaign budget.
- The test results are in: tell us which ads to pause or switch off, which to refresh, and which to scale, extend or iterate on.
- One ad or audience is winning and we want to raise daily spend or roll it out to more markets or channels without resetting learning.
- Cost per lead or per result keeps climbing and people have seen the ads too often; we need a refresh plan against creative fatigue.
- Design retargeting or re-engagement pools from site visitors, video viewers, WhatsApp contacts, SMS lists or lead forms.
- Hardly anyone sees our Facebook or Instagram posts since organic reach collapsed: pick the proven posts worth boosting, a monthly boost budget in UGX or Kenyan shillings, a WhatsApp owned audience and the words to explain paid boosting to the client.

## Do Not Use When

- `meta-testing-framework` for sample size, significance and guardrails in any marketing experiment.
- `creative-brief-and-big-idea` for screening campaign concepts before they become ads.
- `ad-copy-and-hook-lab` for writing the copy variants.
- Stop before changing live budgets, pausing campaigns or boosting posts without account authority; deliver the decision memo instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, primary metric and break-even or allowable cost | `advertising-strategy-and-budget`, `advertising-attribution-and-measurement` | Yes | Stop; a test without a line in the sand cannot be decided. |
| Working tracking for the primary metric | Tag owner, platform exports | Yes | Build tracking first ("tracking before testing"); mark results `not assessed`. |
| Variants with hypotheses | `ad-copy-and-hook-lab`, creative team | Yes | Request them; do not test unlabelled variants. |
| Test budget cap and duration | Client owner | Yes | Propose a capped test plan for approval; do not spend. |
| Platform exports (spend, reach, frequency, results by variant and segment) | Client ad accounts (read-only) | For reading results | Mark decisions provisional; request exports. |
| Privacy basis for retargeting and list use | Client data-protection owner (PL-01, PL-02) | Yes for pools | Exclude list-based pools until the lawful basis and privacy notice are confirmed. |

## Workflow

1. Confirm objective, metric, break-even line and tracking; stop if tracking fails or the line is undefined.
2. Write a test card per test ([test design and reading](references/test-design-and-reading.md)): hypothesis, variable, cells, cap, duration, success and kill thresholds, segment read-outs, owner; lock it as a pre-registered card with guardrails and the SRM note ([test rigour](references/test-rigour-srm-and-preregistration.md)).
3. Order tests by the test hierarchy (offer, then angle/hook, then format/visual, then copy length) — a working hypothesis to confirm with the client's own data, not a law.
4. Launch only after written approval; the authorised operator runs it. Do not optimise mid-window unless a guardrail breaks.
5. Read results against the pre-agreed line; check segment differences, brand linkage and downstream quality (leads that become customers), not just clicks.
6. Decide per the roll-out ladder ([scaling, fatigue and retargeting](references/scaling-fatigue-and-retargeting.md)): retest, extend, balance, roll out — or kill. Record why.
7. Scale in steps; after each step re-read cost per result and frequency before the next. If performance breaks, recover by returning to the last stable level and diagnosing.
8. Schedule creative refresh and re-run the test cycle; archive learnings in the test register.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Test plan with test cards | Client approver, operator | Each card has hypothesis, variable, cap, duration, lines and owner |
| Results read-out | Client, strategist | Decision per cell with evidence, segment view and downstream quality |
| Scale / roll-out plan | Operator, finance owner | Step sizes, checkpoints and stop rules stated |
| Retargeting pool design | Operator, data-protection owner | Pool definitions, windows, creative per stage, exclusions and privacy notice confirmed |
| Test register entry | Knowledge base, `kaizen-improvement-system` | Result, decision and learning recorded |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Test card and results table | Table per test | Lines set before launch; results attach exports and dates |
| Decision memo | Short note | Names the decision, the evidence and what would reverse it |
| Pool and consent record | Table | Lawful basis and notice recorded for each list-based pool |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Launching, pausing, changing budgets, uploading lists or editing live ads also need a named operator, and retargeting and list matching require a lawful basis and a privacy notice disclosing pixels and tracking.

## Degraded Mode

Without platform exports, working tracking or the break-even line, return the narrowest qualified result and mark the affected checks `not assessed`. A test plan and reading template can still be delivered; never declare a winner from impressions alone or from a window shorter than the plan.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| No tracking for the primary metric | Build tracking before testing | Deciding on noise |
| Test spend approaching the plan's cap with no signal | Stop; review hypothesis and offer | Big-budget "tests" that are really launches |
| Winner on clicks but not on qualified leads or sales | Do not scale; fix downstream or reject | Buying cheap, useless volume |
| Winner differs by segment | Scale per segment | Averaging away a strong segment |
| Frequency rising and cost per result worsening | Refresh creative or widen audience before more budget | Fatigue and wasted spend |
| Result beats the line for the agreed window | Extend in steps, re-reading at each | Destabilising delivery with large jumps |
| Comparative ad names a competitor | Legal review before launch; prefer a category rival | Disparagement or code breach |
| Deciding whether to boost an organic Page post | Apply the early-engagement thresholds, decision tree and budget bands in [organic-to-paid amplification](references/organic-to-paid-amplification.md) | Boosting weak posts, or paid reach with no CTA |

## Quality Standards

- Lines in the sand are written before the test and never lowered merely to pass; move a line only with segment-level evidence that value exists at the new level (Croll & Yoskovitz 2013).
- Test one variable per cell; keep a control.
- Report cost per qualified outcome and downstream conversion, not only CTR.
- Expect most tests to lose; record losers as learning.
- Platform budget-change behaviour, learning periods and minimum data rules are checked on the live help centre with the date.

## Anti-Patterns

- Spending a large sum and calling it a test. Fix: small, capped, many tests; keep most budget for scale.
- Changing audience and creative at once. Fix: one variable per cell.
- Reading results after two days. Fix: read at the planned horizon unless a guardrail breaks.
- Chasing people who have seen the ad many times and never engaged. Fix: concentrate on the engaged pool; cap frequency.
- Retargeting with the same ad. Fix: stage-specific creative (proof for abandoners, offer for warm).
- Fake urgency in retargeting ("last chance" every week). Fix: real deadlines only.
- Assuming a winning channel lasts. Fix: watch decay and keep small tests running.

## References

- [Test design and reading](references/test-design-and-reading.md): read when writing test cards or reading results.
- [Test rigour: SRM and pre-registration](references/test-rigour-srm-and-preregistration.md): read when locking a decision-grade creative test, checking assignment balance or reading a platform's early "winner".
- [Scaling, fatigue and retargeting](references/scaling-fatigue-and-retargeting.md): read when deciding roll-out, refresh or pool design.
- [Organic-to-paid amplification](references/organic-to-paid-amplification.md): read when explaining organic reach decline, deciding which organic posts to boost, or setting a monthly boost budget.
- [Method notes and sources](references/method-notes-and-sources.md): read when building a message-angle matrix, filling a test card, running the 100-visitor funnel check, applying the retest-to-roll-out ladder or handling East African phone-number pools.
- [Meta-testing framework](../../meta-analytics-ops/meta-testing-framework/SKILL.md): read when the test needs statistical design; [advertising attribution and measurement](../advertising-attribution-and-measurement/SKILL.md): read when incrementality is in question.
- [Ad copy and hook lab](../ad-copy-and-hook-lab/SKILL.md), [paid social playbook](../../playbooks/playbook-paid-social-advertising/SKILL.md) and [paid search](../paid-search-advertising/SKILL.md): read when variants or channel builds are needed.
- [Direct-marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md): read when writing retargeting or comparative ads.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when a comparative ad names a competitor.
<!-- dual-compat-end -->

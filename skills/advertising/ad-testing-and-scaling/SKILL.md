---
name: ad-testing-and-scaling
description: Use when designing ad tests, reading results, deciding what to scale, kill or refresh, building retargeting pools, or rolling a winning ad out across budgets and markets; use meta-testing-framework for general experiment statistics and creative-brief-and-big-idea for concept screening.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Ad Testing and Scaling

Test small and many before spending the bulk of a budget, decide with pre-agreed lines, and scale winners in controlled steps while watching fatigue, frequency and unit economics. Covers message-angle testing, retargeting pools, comparative ads and the retest-to-roll-out ladder.

<!-- dual-compat-start -->
## Use When

- A campaign needs a test plan before the main budget is committed.
- Test results need reading and a scale, extend, iterate or kill decision.
- A winning ad or audience needs a controlled roll-out across budget, markets or channels.
- Performance is decaying (fatigue, rising cost) and the team needs a refresh plan.
- A retargeting or re-engagement pool (web, video, WhatsApp, SMS, lead-form) needs designing.

## Do Not Use When

- The question is statistical design for any marketing experiment (sample size, significance, guardrails in general); use `meta-testing-framework`.
- The concepts themselves need screening; use `creative-brief-and-big-idea`.
- Copy variants need writing; use `ad-copy-and-hook-lab`.
- Changing live budgets or pausing campaigns is requested without authority; deliver the decision memo and stop.

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
2. Write a test card per test ([test design and reading](references/test-design-and-reading.md)): hypothesis, variable, cells, cap, duration, success and kill thresholds, segment read-outs, owner.
3. Order tests by the test hierarchy (offer, then angle/hook, then format/visual, then copy length) — a working hypothesis to confirm with the client's own data, not a law.
4. Launch only after written approval; the authorised operator runs it. Do not optimise mid-window unless a guardrail breaks.
5. Read results against the pre-agreed line; check segment differences, brand linkage and downstream quality (leads that become customers), not just clicks.
6. Decide per the roll-out ladder ([scaling, fatigue and retargeting](references/scaling-fatigue-and-retargeting.md)): retest, extend, balance, roll out — or kill. Record why.
7. Scale in steps; after each step re-read cost per result and frequency before the next. If performance breaks, recover by returning to the last stable level and diagnosing.
8. Schedule creative refresh and re-run the test cycle; archive learnings in the test register.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
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

Read and search exports and plans; analysis is read-only. Launching, pausing, changing budgets, uploading lists or editing live ads require explicit client authority and a named operator. Retargeting and list matching require a lawful basis and a privacy notice disclosing pixels and tracking.

## Degraded Mode

If exports, tracking or the break-even line are unavailable, return the narrowest useful qualified output: a test plan and reading template with decisions marked `not assessed`. Never declare a winner from impressions alone or from a window shorter than the plan.

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

- [Test design and reading](references/test-design-and-reading.md) — read when writing test cards or reading results.
- [Scaling, fatigue and retargeting](references/scaling-fatigue-and-retargeting.md) — read when deciding roll-out, refresh or pool design.
- [Meta-testing framework](../../meta-analytics-ops/meta-testing-framework/SKILL.md) for statistical design; [advertising attribution and measurement](../advertising-attribution-and-measurement/SKILL.md) for incrementality.
- [Ad copy and hook lab](../ad-copy-and-hook-lab/SKILL.md); [paid social playbook](../../playbooks/playbook-paid-social-advertising/SKILL.md); [paid search](../paid-search-advertising/SKILL.md).
- [Direct-marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md).
<!-- dual-compat-end -->

## Method summary

### Message-angle matrix (Stutts 2021)

Freeze the two or three value themes from research; write two or three angles per theme (social proof / review, comparative, third-party authority, humour, emotional/family, demonstration) in two formats; test on cheap inventory first — a response on a low-intent format signals a strong message; read by segment (different segments often favour different angles). The test phase also seeds retargeting pools.

### Test card (Weinberg & Mares 2014, adapted)

| Field | Content |
|---|---|
| Channel / idea | e.g. "Click-to-WhatsApp ads, parents of Senior 1 applicants, Wakiso" |
| Assumptions to validate | cost per qualified enquiry ≤ UGX [x]; ≥ [n] enquiries available per month; enquirers match the target |
| Variable and cells | e.g. offer A vs offer B, same creative |
| Cap and duration | UGX [amount], [n] days |
| Tracking | unique link, WhatsApp keyword, UTM, "how did you hear" field |
| Success / kill lines | e.g. success ≤ UGX [x] per qualified enquiry; kill > UGX [y] after [n] results |
| Result and decision | focus / retest / drop, with reason |

Test vs optimise: a test is a few variants to validate a channel or message; optimisation (many variables) comes only after a channel shows promise.

### 100-visitor funnel check (from Brunson's funnel practice)

Before scaling traffic, send a small, known amount of traffic through the whole path and read each step's conversion; fix the weakest step first. A strong ad cannot rescue a broken page or slow WhatsApp response.

### Retest → extend → balance → roll out (Stockwell & Shaw 1994)

Borrowed from list testing: after a winning cell, retest at the same size; if it holds, extend to a larger quantity; then balance (much larger); then roll out to the full audience or market. Kill at any stage when cost per order or cost per qualified lead breaches the P&L line (see `direct-response-economics`).

### East Africa notes

- Pools are often phone-number lists (WhatsApp, SMS, call-back) rather than cookie lists; they require opt-in and honoured opt-outs. Uganda: objections to direct marketing must be honoured within 14 days (PL-01). Kenya: consent plus a free, simple opt-out; objections are absolute (PL-02). Checked 2026-09-23.
- Small markets saturate quickly; watch frequency and refresh creative sooner.
- Derive baselines from the client's own first weeks; no imported CPM or CTR norms.

## Sources

- Stutts, P. (2021) *The Undefeated Marketing System*, Scribe/Lioncrest.
- Weinberg, G. and Mares, J. (2014) *Traction*, S-curves Publishing.
- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics*, O'Reilly.
- Stockwell, J. and Shaw, H.M. (1994) *Direct Marketing Checklists*, NTC Business Books.

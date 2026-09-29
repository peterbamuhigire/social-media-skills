---
name: kaizen-improvement-system
description: Use when a campaign, content system, strategy, report or training product keeps underperforming or needs a structured post-mortem, or when this social-media engine needs a quality review; produces a scored audit, blocker list, plan to 95/100 and a logged improvement experiment; not for humanising a single draft (use `anti-ai-slop`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Kaizen Improvement System
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

Runs a capped Kaizen audit on the social-media engine and on one product (campaign, content system, calendar, report, training asset, policy or website/social output), then improves it towards 95/100 one small reversible experiment at a time.

<!-- dual-compat-start -->
## Use When

- A campaign, report or content system has finished and the client wants an honest review of what to fix before the next round.
- Client feedback, audience reactions, platform changes or results must be turned into a tested improvement rather than a guess.
- A deliverable scores below standard and needs a plan from its current score to 95 out of 100.
- The social-media engine or one of its skills needs an audit and a standardised learning record.

## Do Not Use When

- `anti-ai-slop` for cleaning up one AI-assisted draft so it reads as human.
- `meta-testing-framework` for designing the experiment itself.
- `ai-slop-audit` for an evidence-backed audit of AI-generated content.
- Stop when current platform, market, legal or policy claims lack a dated source-register entry; verify them first.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Brief, audience/market, channel and objective (sets audit scope and improvement target) | Client brief | Yes | Stop; the audit has no scope without an objective. |
| The content, campaign or report under review, with its current score and constraints | Engine, client or reviewer | Yes | Score only what is supplied and mark the rest unassessed. |
| Evidence: platform data, measurement exports and the source register | Platform data, client exports, Digital Research Engine | Yes | Publish the capped baseline with evidence gaps visible; withhold release readiness. |
| Rights, permissions and a named reviewer | Client and release owner | Yes | Mark the rights and review checks `not assessed`; no standardisation. |

## Workflow

1. Begin with the Digital Research currentness gate (below), then read the local adoption plan, router, anti-slop gates and portfolio standard.
2. Inventory strategy, platform, content, AI, analytics, reporting, training, policy and campaign routes.
3. Score applicable dimensions and output types. Publish `min(raw score, 65)` and record legal, rights, safety and evidence blockers.
4. Audit audience value, cultural fit, evidence, message/story, accessibility, channel execution, ethical persuasion, AI provenance, measurement, handoff and learning, using the [product adapter](references/product-type-adapters.md) that matches the output.
5. Build a 95/100 plan with exact skill/reference/fixture, owner, experiment, metric, acceptance evidence and rollback.
6. Run a small content, channel, CTA or measurement experiment. If the evidence or safety gate fails, pause, recover the safe version and correct it.
7. Standardise only what the evidence supports, rerun the relevant gates and schedule the next review.

## Two-Level Product Contract

Run the loop once for the engine (routes, skills, references, validators, templates, handoffs and East Africa defaults) and once for the product (campaign, content, calendar, report, training asset, policy, or website/social output). At each level the first analysis is capped at `min(raw_score, 65)`; then select one root cause and one reversible improvement toward 95/100. Use the product adapters in `references/product-type-adapters.md`; do not transfer a campaign metric directly to a report, training asset or website without its own evidence.

## Mandatory 65-to-95 Gate

The first review is an initial analysis: calculate raw findings, publish only `min(raw_score, 65)`, and keep evidence, rights, safety and measurement gaps visible. Do not improve the score by adding copy alone. After the capped baseline, target 95/100 through one small reversible change at a time, with a root cause, owner, primary measure, trust/accessibility guardrail, stop/rollback rule, acceptance evidence, standardisation decision and re-audit date.

## Mandatory Digital Research Currentness Gate

Every Kaizen cycle must begin with the Digital Research Engine at `digital-research-engine`, using its source evaluation and source verification. Record scope, dates, freshness class, support status, uncertainty and review date for current platform, market, legal, policy, technology and lifecycle claims; quarantine unsupported claims as `NOT_ASSESSED`. Apply the portfolio Kaizen currentness gate at `digital-research-engine/docs/continuous-improvement/kaizen-currentness-gate.md`.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Capped audit with evidence/legal/quality blockers | Strategist, client and reviewer | Published score is `min(raw score, 65)`; every blocker named. |
| 95/100 plan and experiment result | Strategist and release owner | Evidence, owner, decision rule, guardrail and re-audit date are explicit. |
| Standardised learning record | Engine maintainer and release owner | Records the decision (standardise or reject) with its evidence. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Brief-to-output map, source register, creative/legal review, measurement result and before/after decision record | Tables and decision log | Another reviewer can reproduce the decision and verify the learning. |
| Currentness record | Source register entries | Scope, dates, freshness class, support status, uncertainty and review date recorded for every current claim. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Edits to engine files need the same explicit authority; route current facts to Digital Research and visual work to chwezi-design-engine.

## Degraded Mode

Without the brief, audience evidence, platform data, source register, rights or reviewer, return the narrowest qualified result and mark the affected checks `not assessed`. The capped baseline and blocker list can still be delivered, with release readiness withheld.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A performance claim lacks a source or baseline | Remove or qualify it. | Fabricated proof. |
| A trend improves reach but harms trust, safety or cultural fit | Reject, pause or narrow the test. | Harmful optimisation. |
| A test passes outcome and guardrail checks | Standardise the learning and re-audit. | Lessons lost. |
| A short-form video gets reach but no qualified action and triggers cultural concerns | Retain the result as a failed experiment, pause the variant, document the evidence and test a better-fit message with a guardrail. | Scaling a variant that harms trust. |
| A current platform, market, legal or policy claim has no dated source-register entry | Quarantine it as `NOT_ASSESSED` until verified. | Stale claims driving the plan. |
| A campaign metric is proposed as evidence for a report, training asset or website | Require that product's own evidence from its adapter. | False transfer of results between product types. |

## Quality Standards

- Do not invent platform benchmarks, audience statistics or performance results.
- The first published score never exceeds `min(raw_score, 65)`.
- Each improvement is one reversible change with root cause, owner, primary measure, guardrail, stop/rollback rule and re-audit date.
- The score is not raised by adding copy alone.
- Failed or inconclusive tests are retained as learning.
- British English and East African defaults unless the brief says otherwise.

## Anti-Patterns

- Optimising vanity metrics without a decision. Fix: define outcome, guardrail, and action.
- Copying a trend without audience fit. Fix: test the local hypothesis.
- Treating a content calendar as strategy. Fix: connect content to funnel and learning.
- Using AI output without provenance or cultural review. Fix: run AI, legal, and cultural gates.
- Closing a test without a learning record. Fix: standardise or reject explicitly.

## References

- [Product-type adapters](references/product-type-adapters.md): read when choosing what to inspect and what evidence to require for a campaign, content asset, calendar, report, training or policy product, or website content, and when asking the root-cause prompts.
- [Local adoption plan](../../../docs/continuous-improvement/kaizen-adoption-2026-08.md): read at the start of every cycle.
- [Portfolio Kaizen standard](https://github.com/peterbamuhigire/digital-research-skills/blob/main/docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md) (digital-research-engine; locally, resolve it through the engine-routing table): read when setting the cycle's portfolio-wide rules.
- [`meta-testing-framework`](../../meta-analytics-ops/meta-testing-framework/SKILL.md): read when designing the improvement experiment.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md): read when running the anti-slop gate on copy.
- [Book-driven campaign learning and retention](../references/book-driven-campaign-learning-and-retention.md): read when auditing audience, story-to-action, ethical experimentation, retention and currentness.
- [Book-driven Kaizen Wave 3](../references/book-driven-kaizen-wave-3-2026-09-02.md): read when checking outcome/guardrail experimentation, provenance, cultural review and platform currentness.
<!-- dual-compat-end -->

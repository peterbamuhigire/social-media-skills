# Control-plane adoption

This engine adopts the shared ten-engine contract from
`C:\wamp64\www\skills-web-dev\docs\engine-control-plane.md`. Social-media
doctrine remains authoritative for strategy, content, campaigns, communities,
platform operations, and measurement.

## Local roles and commands

| Role | Responsibility | Stop condition |
|---|---|---|
| Campaign strategist | Set audience, objective, funnel, offer, channel, and experiment. | Brief is incomplete or unsupported. |
| Content producer | Produce channel-fit assets from the approved content matrix. | Source, rights, or disclosure is unresolved. |
| Compliance reviewer | Check legal, market, rights, privacy, safeguarding, and platform constraints. | Any blocking gate is missing or failed. |
| Analytics reporter | Reconcile measurement definitions, baselines, and outcomes. | Metric lineage or access is absent. |

Route thin commands `campaign`, `content-qa`, `measure`, and `retro` to
existing workflows; no command may publish directly without the release gate.

## Hook and release contract

- `preflight` records audience, market, objective, platform, permissions,
  rights, disclosure, and approval owners.
- `context` loads the current brief, content matrix, source dates, brand and
  design constraints, prior performance, and known platform changes.
- `before_write` checks claims, rights, privacy, safeguarding, and whether the
  asset is draft-only or approved for scheduling.
- `after_write` runs creative, anti-slop, legal/market, and accessibility
  checks as applicable and records the verdict.
- `release` requires approval, content-matrix trace, audience evidence,
  measurement baseline, and required counsel or platform escalation.
- `stop` writes a handoff with unscheduled assets, failed checks, missing
  approvals, and the next review owner.

An absent platform, legal, rights, or measurement check is `NOT ASSESSED` and
blocks publishing; advisory telemetry may fail open.

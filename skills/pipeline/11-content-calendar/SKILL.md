---
name: 11-content-calendar
description: Use when approved themes and campaigns need turning into dated posts for the next three months, with local holidays, seasonal hooks and campaign windows; produces the 90-day content calendar with owners and production cues; not for setting up the weekly workflow that makes the posts (use `playbook-content-production`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# 90-Day Content Calendar Generator

Turns approved pillars, campaigns and seasons into a dated 90-day plan of what goes out on which platform, for the client lead and the production team. Apply `east-african-english` for tone throughout.

<!-- dual-compat-start -->
## Use When

- Pillars, themes and campaigns are agreed and the team needs a dated, post-by-post plan of what goes out on which platform, month by month.
- The schedule must include Ugandan and East African public holidays and observances such as Independence Day, international awareness days and industry seasonal hooks.
- Campaign windows need blocking out so promotions and always-on posts do not clash.
- The client wants a weekly rhythm template, a posting schedule showing each post's approval status, and a pre-publish check that samples posts before they go live.

## Do Not Use When

- `playbook-content-production` for the drafting, design, approval and batching workflow.
- `10-content-pillars` when the recurring themes are not yet agreed.
- `12-website-content-plan` for blog and website articles.
- Stop before scheduling or publishing to live accounts; hand over the calendar for client approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Approved pillars with percentages | `10-content-pillars` output or client sign-off | Yes | Stop; route to `10-content-pillars` rather than inventing themes. |
| Platforms in scope and posting frequency per platform | Channel plan or client lead | Yes | Default to Facebook, Instagram and WhatsApp and label the frequency provisional. |
| Campaign windows (name and dates) | `09-campaign-strategy` or client | If campaigns run | Mark no `[CAMPAIGN]` weeks and note that none were supplied. |
| Three high-revenue seasons and the calendar start Monday | Client or consultant | Yes | Ask the seasonal-hook question; never guess the client's peak periods. |
| Location and the year's variable observance dates (Ramadan, the Eids) | Client; a dated official calendar | Yes | Default to Kampala, Uganda; mark unconfirmed lunar dates `not assessed`. |
| Production capacity and approval owner | Client lead | Yes | Cap volume at stated capacity; return the calendar as an approval draft. |

## Workflow

1. Confirm the intake answers (pillars, platforms, frequency, campaigns, seasons, start date, location); stop if the pillars are not approved and route to `10-content-pillars`.
2. Fix the 13-week grid from the start Monday, then place `[CAMPAIGN]`, `[HIGH SEASON]` and `[OBSERVANCE]` weeks before any always-on content.
3. Select 6–10 awareness days relevant to the industry and state why each was chosen.
4. Set the weekly rhythm template, then fill the Month 1, 2 and 3 tables with one row per platform per week per pillar, each with a specific headline, a two-sentence brief, an owner and an approval status.
5. Write the cross-platform theme under each month and check the 10-4-1 ratio per month.
6. Run the stratified-sampling pre-publish check; batch-fix any failure type seen twice, then re-sample and rerun until a sample is clean (escalate at round 3).
7. Run the anti-slop ship gate and hand the calendar to the client lead as an approval draft; withhold release while a blocking date, permission or evidence defect remains.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Weekly rhythm template and three monthly tables (W1–W13) with owners and approval status | Client lead; `playbook-content-production` | Every row has a specific headline, pillar, platform, format, two-sentence brief and owner; no placeholder rows. |
| Month overviews with cross-platform themes and 10-4-1 ratio notes | Client lead | Each month states its focus, tone, events and measured ratio. |
| Selected awareness days with reasons | Client lead | 6–10 days chosen, each tied to the client's industry. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Observance and date register | Table in the deliverable | Every variable date is confirmed from a dated source or marked `not assessed`. |
| Sampling QC record | Table: round, sample size, failure types, batch-fixes | A clean round is recorded before hand-off; a bare "reviewed" claim does not pass. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Scheduling posts in a live tool is out of scope; the calendar goes to the client for approval.

## Degraded Mode

Without confirmed pillars or observance dates, return the narrowest qualified result and mark the affected checks `not assessed`. A dated 13-week grid with campaign and season blocks can still be delivered, with topic rows held for the approved pillars.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A campaign window overlaps always-on content | Let the campaign lead: cut pillar posts that week and add one supporting organic post per platform. | Mixed messages and paid/organic duplication. |
| A week falls in a high-revenue season | Raise posting frequency by 20–30 % and brief at least two seasonal posts per platform. | Missing the client's biggest demand window. |
| An observance is solemn (Uganda Martyrs Day) or religious (Ramadan) | Acknowledge rather than promote; during Ramadan reduce promotion and avoid daytime food imagery where relevant. | Cultural offence and brand damage. |
| A variable lunar date is unconfirmed | Confirm the year's date from a dated source or mark it `not assessed`; never carry last year's date. | An Eid greeting on the wrong day. |
| A month's ratio drifts towards promotion | Rebalance towards about 10 value, 4 brand and 1 promotional per 15 rows (Bodnar and Cohen, 2012). | A calendar the audience reads as advertising. |
| A sampled failure type appears more than once | Treat it as systematic; fix every matching row, not only the sampled ones. | The same error shipped across dozens of rows. |

## Quality Standards

- All three monthly tables are produced; no month is skipped or abbreviated.
- Every row has a specific topic or headline; none says "TBC" or "educational post".
- Observances in the window are included with tone guidance; 6–10 awareness days carry a stated reason.
- Campaign weeks are marked and defer to the campaign.
- Each week's cross-platform content shares a theme without identical copy.
- The 10-4-1 ratio is noted per month and the calendar is not mainly promotional.
- The sampling QC record states sample size, failure types, batch-fixes and the converging round.
- British English; dates in day-month-year form (for example 7 April 2026).

## Anti-Patterns

- Inserting a generic post on an observance and calling it culturally relevant. Fix: write a brief that suits the occasion's tone, or leave the day out.
- Reusing last year's Eid or Ramadan dates. Fix: confirm the current year's dates before generating.
- Pasting the same copy across platforms and calling it a cross-platform theme. Fix: vary format, day and angle per platform under one weekly theme.
- Sampling only Month 1 in the pre-publish check. Fix: spread the sample across all three months and every platform in scope.
- Treating the calendar as a locked schedule. Fix: review it every Friday for reactive posts, follow-ups and approval timing.
- Scheduling posts in a live tool during planning. Fix: hand the calendar over for approval; publishing needs separate authority.

## References

- [Calendar build method](references/calendar-build-method.md): read when asking the intake questions, laying out the table columns, picking observances and awareness days, setting the weekly rhythm or running the sampling check.
- [`10-content-pillars`](../10-content-pillars/SKILL.md): read when the pillars are missing or disputed.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting headlines and briefs.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

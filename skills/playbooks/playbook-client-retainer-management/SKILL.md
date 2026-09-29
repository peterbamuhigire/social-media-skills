---
name: playbook-client-retainer-management
description: 'Use when a monthly client relationship needs managing: scope, scope creep, change requests, monthly check-ins, performance-review triggers, renewal and price rises; produces the scope sheet, change-request log, check-in agenda and renewal plan; not for grading a portfolio of B2B customers (use `strategy-b2b-customer-community`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Playbook: Client Retainer Management

Scope creep, communication breakdown and poor renewal handling are the three leading causes of retainer loss; this playbook prevents all three with a scope sheet, change-request log, check-in agenda, review triggers and a value-first renewal plan.

<!-- dual-compat-start -->
## Use When
- A new retainer is starting: deliverables, platforms, revision rounds, response times, approvals and exclusions agreed in writing before work begins.
- The client keeps asking for extra work outside the agreement; a polite, written change-request process is needed.
- Plan the monthly client check-in and decide what should trigger a performance review when results or the relationship slip.
- The retainer ends in four weeks: prepare the renewal, the price at renewal and a value-first renewal conversation.
- A client has not renewed, or the agency missed a commitment, and the relationship needs resetting.

## Do Not Use When
- `strategy-b2b-customer-community` for grading many business customers, account penetration and key-account plans.
- `playbook-agency-operations` for agency-wide onboarding, invoicing, team roles and white-label partners.
- `biz-dev-proposal` for the proposal and statement of work that wins a new client.
- Stop before sending a price change, contract amendment or termination notice without the account owner's approval; deliver the draft and the conversation script.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name and industry | Account owner | Yes | Ask before drafting; scripts cannot be tailored without it. |
| Retainer start and end dates | Signed agreement | Yes | Treat the renewal date as unknown and start renewal preparation now. |
| Current deliverables, listed with quantities | Signed agreement or statement of work | Yes | Build the six-element scope sheet first; do not judge creep against a vague scope. |
| Primary pain point (scope creep, non-communication, pricing disputes, renewal negotiation) | Account owner | Yes | Deliver the standard sequence (scope, change requests, check-in, renewal). |
| Relationship health (good, strained, crisis) | Account owner | Yes | Assume strained and include the reset script. |
| Change-request log, monthly reports and baseline metrics | Account records | For renewal | Mark the value recap `not assessed` and gather results before pricing. |

## Workflow

1. Run the intake questions and set priority: a strained or crisis relationship goes to the review triggers and reset script first; an end date within six weeks goes to renewal first. Stop if the deliverables or end date cannot be confirmed.
2. Write or repair the scope sheet with all six elements (deliverables with quantities, platforms, revision rounds, response time, approval process, exclusions), using the [retainer operating procedures](references/retainer-operating-procedures.md).
3. Classify current extra requests against the scope-creep table and the EA patterns, and answer each with the change-request protocol and script.
4. Start or update the change-request log (date, request, status, agreed fee, notes) and confirm each approved change in writing.
5. Set the 30-minute monthly check-in agenda and the voice-note summary; name any performance-review trigger that has fired and schedule the unscheduled review.
6. Six weeks before the end date, prepare the renewal: results against baseline, scope additions, low-value deliverables, a revised proposal, three equal-value packages and a concession worksheet ([value-first renewal](references/value-first-renewal-and-relationship-health.md)).
7. Check every script for tone and every fee for a source; correct and rerun the quality checks, then hand drafts and scripts to the account owner for approval before anything is sent.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Six-element scope sheet | Account owner and client | Every deliverable has a quantity; unlisted platforms are out of scope; exclusions named. |
| Change-request log and scripts | Account manager | Each approved change has a date, status and agreed fee; scripts are positive and firm. |
| Monthly check-in agenda and review-trigger list | Account manager | Timed 30-minute agenda with four segments; triggers are observable signals with named actions. |
| Renewal plan (value recap, three packages, concession worksheet, scripts) | Account owner | Opens with value against baseline; no unsourced "standard increase" percentage. |
| Offboarding checklist for non-renewal | Account manager | Five-working-day asset handover and word-for-word handover message included. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Change-request log | Living table | Referenced at the monthly check-in and at renewal; no verbal-only approvals. |
| Value recap against baseline | Table with sources | Each result names its metric, period and source, or is marked `not assessed`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Price changes, contract amendments and termination notices go out only with the account owner's approval.

## Degraded Mode

Without the signed agreement's deliverables list, return the narrowest qualified result and mark the affected checks `not assessed`. The six-element scope template, change-request script, check-in agenda and reset script can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Repeated requests exceed the agreed service boundary | Document the pattern and agree a scope or fee change. | Silent scope creep. |
| A request falls outside the deliverables list | Acknowledge positively, quote the fee or offer to include it at renewal; never "I'll do it this once". | A precedent that extra work is free. |
| A performance-review trigger fires (primary metric down 2 consecutive months, client silent 2+ weeks, approvals stalled 14 days, invoices 45 days overdue) | Hold an unscheduled review before the next invoice; do not wait for the monthly check-in. | A retainer lost without warning. |
| Client asks for a lower price without reducing scope | Counter with a reduced price paired with fewer deliverables. | Margin erosion. |
| The agency misses a commitment | Run the trust-recovery protocol within 24 hours. | Lost trust compounding into non-renewal. |
| Retainer end date is six weeks away | Start renewal and communicate any price change now; set it from cost-to-serve, value delivered and market, not a remembered percentage. | A weak last-minute negotiation. |
| Client cancels the check-in twice in a row | Treat it as a non-communication trigger and request a review. | Relationship drift. |

## Quality Standards

- The scope sheet covers all six elements: deliverables, platforms, revision rounds, response time, approval process and exclusions.
- The scope-creep table lists at least six common EA request types, each with a scripted or recommended response.
- The change-request protocol includes a word-for-word script, positive in tone and firm on boundaries.
- The monthly check-in is a timed 30-minute agenda with four named segments and a purpose for each.
- Review triggers are specific, observable signals with named actions.
- Renewal is a six-week process opening with value against an agreed baseline, equal-value options and conditional concessions.
- Offboarding includes a word-for-word handover message and a five-working-day asset handover deadline; the full criteria list, including the client-council and trust-recovery items for high-grade retainers, is in the procedures reference.

## Anti-Patterns

- Writing "social media management" or "and other platforms as agreed" in scope. Fix: name every deliverable with a quantity and every platform.
- Letting WhatsApp "quick things" pile up unbilled. Fix: log each request and route anything outside scope through the change-request protocol.
- Accepting new approvers added to the chain without discussion. Fix: restate the approval process in writing and agree who signs off.
- Sending a renewal proposal without a meeting. Fix: schedule the 30-minute conversation first, then send the document.
- Apologising for a price increase. Fix: tie the new price to results achieved and forward value.
- Scaling back effort after a client decides not to renew. Fix: deliver through the final day and hand over all assets within five working days.

## References

- [Retainer operating procedures](references/retainer-operating-procedures.md): read when running intake, defining scope, handling scope creep or change requests, running check-ins, acting on triggers, preparing renewal or offboarding.
- [Value-first renewal and relationship health](references/value-first-renewal-and-relationship-health.md): read before renewals, relationship resets, after a missed commitment, or when designing the client council.
- [`biz-dev-proposal`](../../business-development/biz-dev-proposal/SKILL.md): read when defining scope at proposal stage or producing the revised renewal proposal.
- [`playbook-agency-operations`](../playbook-agency-operations/SKILL.md): read when the issue is agency-wide process rather than one client.
- [`playbook-daily-operations-routine`](../playbook-daily-operations-routine/SKILL.md): read when the fix is day-to-day execution discipline.
- [B2B customer community and key accounts](../../strategy/strategy-b2b-customer-community/SKILL.md): read when grading clients and planning key accounts.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting client scripts and messages.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone for East African clients.
<!-- dual-compat-end -->

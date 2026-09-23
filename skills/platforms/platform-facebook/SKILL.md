---
name: platform-facebook
description: Use when creating a Facebook channel plan covering account setup, content, community and measurement for Uganda or East Africa. Use a playbook for cross-channel operations and a strategy skill for channel selection.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Facebook Presence Plan

<!-- dual-compat-start -->
## Use When
- Create or revise a Facebook-specific presence, growth or publishing plan.
- Translate a confirmed audience, offer and objective into channel decisions.

## Do Not Use When
- The task is cross-channel operating procedure; use the closest `playbook-*` skill.
- The task is choosing channels or business direction; use `strategy-channel-architecture`.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client objective, audience and offer | Approved brief or client interview | Yes | Stop and request the missing decision; do not invent it |
| Current account and content evidence | Native account export, screenshots or supplied audit | Conditional | Mark the account baseline unassessed and qualify recommendations |
| Current platform rules and feature limits | Official Facebook help or policy source | Conditional | Omit volatile specifications or flag them for live verification |

## Capability and Permission Boundaries
Read supplied artefacts and search relevant evidence. Treat review, audit and planning as read-only. Editing the requested draft is allowed; publishing, messaging, production changes, personal-data processing, spending, destructive actions and certification claims require explicit authority. Use network access only for authorised verification.

## Degraded Mode
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Facebook channel plan plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A peer-to-peer community is the primary need | Use a Group with named moderation rules; retain the Page as the official identity | Mixing official notices with unmanaged member discussion |
| Account is absent or not accessible | Produce a setup plan with assumptions labelled | False optimisation against invented history |
| Evidence shows an established account | Prioritise measured gaps and retained strengths | Destructive reset of working assets |
| A rule, limit or feature is time-sensitive | Verify against the official platform source before stating it | Stale platform advice |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply [the channel creative and service lab](../../pipeline/06-digital-marketing-strategy/references/channel-creative-and-service-lab.md), the platform decisions below and the verified account evidence; draft a capacity-based plan with an accountable conversion path.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Facebook channel plan | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
| Assumption and gap register | Approver or next workflow | Every missing source, unassessed check and required approval has an owner or next action |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and verification record | Inline table or appendix | Each material choice traces to an input, source or labelled assumption |
| Release-gate result | Completed checklist | No blocking policy, factual, permission or anti-slop finding remains |

## Quality Standards
Use British English and the specified market context. Recommendations must be executable with the stated capacity, current claims must be verified or qualified, and acceptance conditions must be observable. A worked example must use a labelled scenario, not fabricated client evidence.

## Anti-Patterns
- Inventing a client fact, benchmark, budget or approval. Fix: cite the source or label the assumption and its effect.
- Copying one channel or client pattern unchanged. Fix: tie each choice to the named audience, objective and evidence.
- Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim.
- Treating an inaccessible account, file or metric as healthy. Fix: mark it `not assessed` and bound the conclusion.
- Publishing, spending, messaging or changing production state from planning authority. Fix: obtain explicit action authority.
- Delivering actions without owner, timing or acceptance. Fix: assign all three or return the item as an unresolved gap.

## References
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- [East African English standard](../../language/east-african-english/SKILL.md)
- Use the directly cited sources and companion skills in the domain guidance below; verify time-sensitive claims before use.
<!-- dual-compat-end -->

## Page, community and conversion plan

Confirm the business identity, audience, service area, objective, source assets,
existing account evidence, team capacity and buying path. Do not infer local
platform penetration or customer behaviour from a regional stereotype.

Review the Page's accurate description, current contact/service information,
proof assets and primary next step. Verify current controls, dimensions, CTA
availability and connected messaging options before specifying setup. Preserve
working assets; do not unpublish a live Page as a routine setup instruction.

## Creative and community choices

Choose image, video, link, Story, event or discussion formats according to the
reader's job and production evidence. Use original demonstrations, accurate
offer details, permissioned cases and useful answers. A caption should give
the context the content needs; it need not force humour or a comment prompt.
Reject fixed content ratios, guaranteed reach ceilings and universal link penalties.

Create a group only when members have a recurring purpose and a moderator can
support it. Define membership, privacy, topics, promotion rules and escalation.
Participate in existing groups within their rules; membership is not a prospect
list. Do not remove legitimate criticism simply because it mentions a competitor.

## Enquiry and service handoff

Choose website, telephone, Messenger or WhatsApp from audience preference and
actual operating capacity. Verify current product availability and authorised
connections. Test the whole enquiry route and record recipient, confirmation,
failure recovery, working hours and response commitment. Collect only necessary
information. A message arriving after a post is not proof that the post caused it.

Use a response decision tree: answer routine questions; acknowledge and investigate
complaints; protect private details; escalate safety, legal or reputational issues;
moderate abuse/spam consistently. Promise a next action you can honour, not an
automatic resolution. Adapt replies to the issue rather than using synthetic warmth.

## Pilot, paid readiness and reporting

Build a thirty-day plan only to the agreed capacity, with each unit's audience
question, source, format, creative direction, owner, destination and review.
Choose posting times from available account evidence and a bounded test. No
minimum weekly quota is an algorithm requirement. Scheduling-tool choices need
current authorised integration evidence, not assumed reach penalties.

Before paid activity, verify objective, audience, offer, policy, tracking,
destination, budget authority and sales/service readiness. Separate a test of
creative from a test of the offer. Report qualified enquiries, service outcomes,
accepted opportunities and contribution alongside reach and interactions.

## Worked example and acceptance

A retail post produces many messages but the team cannot quote stock or delivery
accurately. Repair catalogue/service information and response ownership before
increasing reach. The plan passes when an operator can fulfil the promised next
step, each claim is sourced, and the report distinguishes attention from sales.

## Operational reference

- [Channel creative and service lab](../../pipeline/06-digital-marketing-strategy/references/channel-creative-and-service-lab.md) — production, creators, community, paid readiness and commercial measurement.

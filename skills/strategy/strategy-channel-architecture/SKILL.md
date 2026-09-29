---
name: strategy-channel-architecture
description: 'Use when a brand is on several platforms without clear jobs for each: assign platform roles, choose the conversion hub, map how audiences move between channels and split team effort; produces the hub-and-spoke channel map with an effort allocation table; not for choosing which acquisition channels to test (use `traction-channel-bullseye`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Strategy: Channel Architecture

Designs a hub-and-spoke channel architecture: the conversion hub, one role per platform, the customer traffic flow and the split of content effort, based on Schaffer's platform role framework (*Maximize Your Social*, Wiley, 2013) adapted for Uganda and East Africa.

<!-- dual-compat-start -->
## Use When

- We post identical content everywhere and cannot say what Facebook, Instagram, TikTok, LinkedIn or WhatsApp is each for.
- We need a conversion hub (website, WhatsApp Business or landing page) and a traffic flow map from every spoke to it.
- A small team is stretched across too many platforms and must decide where effort and posting frequency go.
- Content should flow from one core piece to the other platforms instead of being made separately for each.

## Do Not Use When

- `traction-channel-bullseye` for deciding whether social media or another channel family should be tested at all.
- `peso-integrated-strategy` for coordinating paid, earned, shared and owned media and growing owned audiences.
- `05-social-media-strategy` for the full social-media strategy document.
- Stop when the business goal or the list of active accounts is unknown; request the channel audit before assigning roles.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry and business type, country and city | Client owner | Yes | Default the location to Uganda/Kampala and say so; stop without the business type. |
| Primary goal: one of awareness, leads, sales, community or retention | Client owner | Yes | Stop; roles cannot be assigned without one goal. |
| Current platforms with approximate followers and monthly reach | Client and platform insights | Yes | Record "Unknown — recommend pulling from platform insights" and proceed with the audit. |
| Primary target audience (age range, urban or rural location, income or professional status) | Client brief or audience data | Yes | Use a labelled working audience; do not give Instagram or TikTok a high-effort role until the audience fit is checked. |
| Available weekly content production time (hours) | Client or team lead | Yes | Cap the plan at one High and one Medium platform and mark the time budget `not assessed`. |
| Hub preference and its state (WhatsApp Business, website, Google Business Profile, landing page, email list, physical location) | Client; a check of the hub itself | Yes | Ask explicitly; never assume a website is the hub. |

## Workflow

1. Confirm the intake answers from the [channel architecture method](references/channel-architecture-method.md); stop when the business goal or the list of active accounts is unknown and request the channel audit.
2. Check the upstream gate: if channels have not been tested against the other acquisition channels, run `traction-channel-bullseye` first.
3. Define the conversion hub and its single primary call to action before any spoke is assigned.
4. Audit current channels; name the strongest, the weakest and the missing channels.
5. Assign exactly one primary role per active platform (table below) and flag any unassigned role, especially Conversion and Retention.
6. Draw the traffic flow map across all five stages and the content flow map from one pillar piece to its derivatives; for a timed launch, add sequence roles from [launch channel sequencing](references/launch-channel-sequencing.md).
7. Allocate effort (no more than three platforms at High or Medium), add a participation, affordance and privacy card for each High or Medium platform, and reconcile the weekly time budget with the stated hours.
8. Check the map against the Quality Standards and the anti-slop gate; correct any failed item and rerun the check before hand-off.

## Platform roles (Schaffer, 2013)

| Role | Definition | Best platforms in Uganda/EA |
|---|---|---|
| **Discovery** | First contact — the audience finds the brand for the first time | Facebook, TikTok, Instagram Reels, Google Search |
| **Engagement** | Builds relationship and trust over repeated interactions | Facebook Groups, WhatsApp Community, Instagram feed |
| **Conversion** | Drives the specific commercial action (enquiry, purchase, visit) | WhatsApp Business, Google Business Profile, landing page |
| **Retention** | Keeps existing customers connected and loyal post-purchase | WhatsApp Broadcast, Email, Facebook Page |
| **Advocacy** | Turns satisfied customers into active referrers | WhatsApp (referral asks), Instagram UGC, Facebook reviews, Google reviews |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Hub definition (hub, URL or contact, rationale, primary CTA) | Client owner and every channel lead | Stated before any spoke role; one primary call to action. |
| Channel audit and role assignment table | Client owner; `05-social-media-strategy` | Every active platform has exactly one primary role with a one-sentence rationale. |
| Traffic flow map (written flow and text diagram) | Content and community leads | Covers Discovery → Engagement → Conversion → Retention → Advocacy for this client, not a copied example. |
| Effort allocation table with weekly time budget and participation cards | Team lead | At most three High or Medium platforms; posts per week for every platform; hours reconcile. |
| Content flow map | Content producer; `10-content-pillars` | Shows how Tier 1 pillar content becomes Tier 2 derivatives and Tier 3 native posts, all pointing to the hub. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Channel audit record | Table with followers, reach, engagement rate and data date | Unknown figures are marked unknown with a request to pull platform insights. |
| Audience-fit and penetration notes | Short table per recommended platform, with source and date | Platform recommendations rest on dated Uganda/EA data or are labelled assumptions. |
| Consent and safeguarding notes | One line per High or Medium platform card | Public-to-private handoff owner and consent risk recorded. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Closing or deprioritising an account is a recommendation for the client to act on.

## Degraded Mode

Without the client's active-account list and weekly production hours, return the narrowest qualified result and mark the affected checks `not assessed`. A hub recommendation, the role definitions and a blank traffic-flow template for the client to complete can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client is spread thinly or lacks a role for each channel | Choose a primary hub and explicit support roles | Every channel receives equal effort without a conversion path |
| Channel choice has not been tested against the other acquisition channels | Gate: run `traction-channel-bullseye` (19 channels, three capped tests) before assigning social roles; record whether each social channel harvests demand or generates it | Building an elaborate social architecture on a channel that cannot reach customers at allowable cost |
| The named website hub has not been updated in six months or has no clear call to action | Recommend WhatsApp Business or a landing page as the hub and note the reason | Sending traffic to a dead end |
| The client is on more platforms than there are roles | Deprioritise some platforms to Minimal effort | Two roles on one platform, or none done well |
| More than three platforms are proposed at High or Medium effort | Cut to three and move the rest to Low or Minimal | Nothing remarkable on any platform |
| The primary audience is 16–30 in Uganda | Test TikTok as the lead discovery platform (growth ranking `NOT_ASSESSED`) | Missing a leading discovery channel for that audience |
| The client cannot commit to one YouTube video a week, or targets retail consumers on X/Twitter | Do not make YouTube or X a priority platform unless the commitment or audience data supports it | Effort on channels that cannot grow |
| Content is about to be cross-posted unchanged | Adapt format and copy per platform from one pillar piece | Identical posts that ignore each platform's norms |

## Quality Standards

- Every active platform has exactly one primary role; no platform has two roles and no role goes to two platforms.
- No more than three platforms are at High or Medium effort.
- The traffic flow map covers all five stages: Discovery → Engagement → Conversion → Retention → Advocacy.
- The hub is defined and confirmed (method Section 1) before any spoke roles are assigned.
- The content flow map shows how pillar content becomes derivative spoke content.
- Platform recommendations reflect current Uganda/EA penetration data and audience characteristics.
- The effort allocation table gives posts-per-week guidance for every platform.
- The weekly time budget is reconciled against the client's stated available hours.

## Anti-Patterns

- Assuming the website is the hub. Fix: ask explicitly; many Ugandan SMEs have no website or an outdated one.
- Leaving Conversion and Retention unassigned. Fix: flag them; they are the two roles EA clients most often neglect.
- Copying the retail, professional-services or restaurant flow examples verbatim. Fix: adapt the pattern to the client's industry and hub.
- A high-effort channel whose only job is "post more". Fix: complete the participation card (motive, affordance, job, boundary, hub action, risk, guardrail) first.
- Relying on the Facebook Page alone for community. Fix: invest in a Facebook Group where the client has or could build a community.
- Starting the WhatsApp Broadcast list late. Fix: build it from Day 1 and put a join CTA on every other platform.

## References

- [Channel architecture method](references/channel-architecture-method.md): read when running the intake, filling the six output sections, drawing flow diagrams or applying the EA platform notes.
- [Launch channel sequencing](references/launch-channel-sequencing.md): read when the architecture must support a timed campaign, launch, enrolment window or event.
- [Traction channel bullseye](../traction-channel-bullseye/SKILL.md): read when the channel families have not yet been tested (upstream gate).
- [`peso-integrated-strategy`](../peso-integrated-strategy/SKILL.md): read when paid, earned, shared and owned media need coordinating or the owned hub needs depth.
- [`05-social-media-strategy`](../../pipeline/05-social-media-strategy/SKILL.md): read when the full social-media strategy document is needed.
- [`10-content-pillars`](../../pipeline/10-content-pillars/SKILL.md): read when deciding what content to produce per platform.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the map and rationales.
<!-- dual-compat-end -->

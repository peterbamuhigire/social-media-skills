---
name: platform-instagram
description: 'Use when a brand needs to run Instagram well: formats and Reels cadence, feed grid and visual look, DMs, stalled follower growth or reach, and measurement; produces the Instagram channel plan with growth experiments and a visual standards brief; not for paid ad campaigns (use `playbook-paid-social-advertising`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Instagram Presence Plan

Plans how a brand uses Instagram formats, discovery, creators and DMs to move buyers to a sale or booking, for the client owner and delivery team.

<!-- dual-compat-start -->
## Use When
- The client wants a clear mix of Reels, Stories and carousels, how often to post each, and the Instagram numbers that matter.
- Follower growth or reach has stalled and the client wants a diagnosis and a phase-based test plan for Reels, hashtags, collabs and broadcast channels.
- The feed needs a planned grid, mood board, colour palette and editing preset, with a visual standards brief for the designer.
- Instagram DMs, shopping links and profile proof need to turn interest into sales or bookings.

## Do Not Use When
- `playbook-paid-social-advertising` for Instagram and Meta ad campaigns.
- `strategy-video-content` for a video approach shared across several platforms.
- `caption-writer` for the captions themselves.
- Stop before posting, starting collabs or changing the live account without client authority; deliver the plan for approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, offer and intended next step | Approved brief or client interview | Yes | Stop; do not choose formats before the buyer and next step are known. |
| Account insights, top posts and profile screenshots | Account admin or supplied audit | Conditional | Mark the baseline `not assessed`; return a set-up plan, not a growth diagnosis. |
| Brand assets, usage rights and production capacity | Client marketing lead | Yes | Limit the plan to formats the team can produce and label rights gaps as blockers. |
| Current format, account, hashtag, broadcast-channel and link features | Official Instagram help or the account itself | Conditional | Omit volatile specifications or flag them for live verification. |
| Creator quotes and agreed deliverables | Creator or agency, in writing | If collabs are planned | Hold the collaboration; obtain current quotes rather than using a generic price band. |

## Workflow

1. Confirm objective, buyer, decision owner and permission boundary; stop if the objective or owner is missing, or if the job is paid Meta campaigns.
2. Review identity, description, proof and destination for buyer comprehension, and verify current searchable fields, profile limits and link options.
3. Choose formats and series with the [format, discovery and sales method](references/instagram-format-discovery-and-sales-method.md); specify each video's opening, visual evidence, explanation, ending, audio, captions and destination.
4. If growth or reach has stalled, place the account on the phase ladder and diagnose the plateau with [growth diagnosis and experiments](references/growth-diagnosis-and-experiments.md) before adding volume.
5. If a grid or visual standards brief is needed, write it with [grid and visual system](references/grid-and-visual-system.md) and route visual execution to chwezi-design-engine.
6. Design the route to sale (enquiry, product or service page, booking or permissioned resource), test fulfilment and handoff, and agree creator terms in writing.
7. Plan one learning cycle with defined measures, then run the quality and anti-slop gates; correct any failed check and rerun it before handing over for approval.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Instagram channel plan: profile, format mix, series and cadence | Client owner and delivery team | Each format choice states the reader's job and the production evidence behind it; no format is claimed to always win. |
| Growth diagnosis and one-lever experiment plan | Client owner | Account placed on the phase ladder; each experiment changes one lever and has a stop rule. |
| Visual standards brief (grid, mood board, palette, preset) | Designer via chwezi-design-engine | Brief is implementable without further instruction; no rigid alternating grid or single filter imposed. |
| DM, shopping and route-to-sale map with creator terms | Sales or service lead | Destination and handoff tested; fee, deliverables, approvals, disclosures and usage rights agreed in writing. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Feature verification log | Table: feature, source, date, account eligibility | Every volatile claim has a dated source or is marked `not assessed`. |
| Rights and creator agreement record | Table per asset or creator | Commercial rights for sound, likeness and creator material recorded before use. |
| Pilot review record | Table: attention, saves/shares, qualified actions, accepted opportunities, contribution | Metric definitions and tracking limits stated; stages reported separately. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. DM automation needs an authorised integration, a current policy check, limited scope and human recovery.

## Degraded Mode

Without account insights or a confirmed offer and next step, return the narrowest qualified result and mark the affected checks `not assessed`. A profile review, format rationale and pilot template can still be delivered with assumptions labelled.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The objective needs discovery and proof | Pair Reels for reach with carousels or Stories for evaluation | Reach without a conversion path |
| No account exists or insights are not accessible | Produce an account set-up plan with assumptions labelled | False optimisation against invented history |
| Insights show an established account | Prioritise measured gaps and keep what already works | Destructive reset of working assets |
| A format, hashtag, broadcast-channel or link feature is time-sensitive | Verify it against official Instagram help before stating it | Stale platform advice |
| Follower growth or reach has stalled, or a growth plan is requested | Place the account on the phase ladder, diagnose the plateau and run one-lever experiments with [growth diagnosis](references/growth-diagnosis-and-experiments.md) | Adding volume into a suppressed or mis-targeted account |
| The client needs a feed grid or visual standards brief | Write the planning brief with [grid and visual system](references/grid-and-visual-system.md); route visual execution to chwezi-design-engine | Unbriefed creators or consultant-made visual assets |
| A piece repeats claims without substantiated product proof | Reject it; replace repetition with a genuine comparison or demonstration and check the destination | Attractive content that sells nothing truthfully |
| A resource is requested in DMs | Deliver the resource only; do not treat the request as broad marketing consent or send unsolicited follow-ups | Consent and spam breaches |

## Quality Standards

- Each unit makes a distinct point, with truthful visuals, cleared rights, readable rendering and an accountable next step.
- Still, carousel, Reel, Story and collaboration choices each state why that format carries the point.
- Video briefs specify opening, visual evidence, explanation, ending, audio, captions and destination; crops and UI obstruction are checked in the intended surface.
- Hashtag and discovery advice uses accurate descriptive, location and topic cues without arbitrary counts or size tiers.
- Guides, broadcast channels and other features appear only after current availability is verified.
- Creator evaluation cites audience fit, actual work and commercial evidence, never a follower threshold alone.
- Measures separate attention, useful sharing/saving, qualified actions, accepted opportunities and contribution; no universal save, completion, follower-growth or profile-to-click rate is used as a standard.

## Anti-Patterns

- Claiming only two profile fields are indexed or that a profile change guarantees discovery. Fix: verify current searchable fields and state the limit.
- Imposing a rigid alternating grid, one filter or a luxury colour formula. Fix: brief intentional art direction through chwezi-design-engine.
- Using trending sound as a reach guarantee. Fix: choose sound for meaning and commercial rights.
- Reviving Instagram Guides from a historical book. Fix: verify availability or use an owned website resource.
- Diagnosing a restriction from a missing interface tab. Fix: diagnose with account data and the growth reference.
- Defaulting to a named automation vendor. Fix: specify the authorised integration, scope and human recovery route.

## References

- [Instagram format, discovery and sales method](references/instagram-format-discovery-and-sales-method.md): read when reviewing the profile, choosing formats and series, planning discovery, creator partnerships, the route to sales or the pilot review.
- [Growth diagnosis and experiments](references/growth-diagnosis-and-experiments.md): read when follower growth or reach has stalled or a phase-based growth plan is needed.
- [Grid and visual system](references/grid-and-visual-system.md): read when briefing a feed grid, mood board, palette, editing preset or visual standards document.
- [Channel creative and service lab](../../pipeline/06-digital-marketing-strategy/references/channel-creative-and-service-lab.md): read when planning production, creators, community, paid readiness and commercial measurement.
- [`caption-writer`](../../content-writing/caption-writer/SKILL.md): read when the captions themselves are needed.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting captions, briefs and DM replies.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and spelling.
<!-- dual-compat-end -->

---
name: platform-x-twitter
description: 'Use when a brand, leader or organisation wants a voice on X (Twitter) with journalists, opinion leaders, policy and NGO audiences: whether X fits, profile, threads, polls and joining live conversations; produces the X channel plan with a 30-day plan and KPIs; not for press releases or media pitching (use `playbook-pr-publicity`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# X (Twitter) Presence Plan

Decides whether X fits the client and, if so, plans its profile, threads, polls, community and media relations. X in East Africa serves journalists, opinion leaders, academics, NGO and development workers, public servants, politicians and urban professionals: disproportionately valuable for B2B and professional services, lower priority than Facebook, WhatsApp and TikTok for FMCG, retail and mass-market goods.

<!-- dual-compat-start -->
## Use When
- The client wants to know whether X is worth the effort for its audience before committing time.
- A leader, NGO, B2B firm or professional practice wants to reach journalists, opinion leaders and public servants on X.
- The team needs thread outlines, tweets, single-post and poll ideas, and a posting rhythm for X (Twitter).
- The client wants to join live conversations and trending debates on X without damaging its reputation.

## Do Not Use When
- `playbook-pr-publicity` for press releases, media pitching and earned coverage.
- `playbook-crisis-communications` when a live issue or backlash needs a response.
- `strategy-channel-architecture` for deciding which platforms to use overall.
- Stop before posting on political or contested topics without the client's approved position and sign-off.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client and trading name, industry, products/services and country/city | Approved brief or client interview | Yes | Default the market to Uganda/East Africa and label it. |
| Target audience on X (journalists, professionals, public sector, general public) and primary goal | Client confirmation | Yes | Stop; if X is not right for the audience, say so and recommend the appropriate platform instead. |
| Content areas the client can comment on with authority, and its approved positions on contested topics | Client leadership | Yes | Limit the plan to uncontested expertise; do not post on political or contested topics without sign-off. |
| Posting and daily engagement capacity | Client team | Yes | Build the plan for the capacity stated, never for the growth-phase range by default. |
| Existing account stats (followers, monthly impressions, top posts) | Native Analytics tab | Conditional | Set Month 1 as the baseline and mark the audit `not assessed`. |

## Workflow

1. Run the platform fit check against the confirmed audience; stop and recommend another platform if X does not fit, or route to `playbook-pr-publicity` or `playbook-crisis-communications` when the job is press work or a live issue.
2. Set up the profile (handle, display name, bio, header, pinned post, profile link) from the [X channel playbook](references/x-channel-playbook.md) §1.
3. Choose content types and set frequency to the client's capacity (§2–§3), with EAT posting windows.
4. Write thread outlines post by post and single-post and poll ideas specific to the client's industry (§4, §7).
5. Plan community building (replies, strategic following, lists, mentions, X Communities) and the media, NGO, public-sector and regulated-industry uses (§5–§6).
6. Set KPIs with the action to take when each is below target (§8).
7. Check every live-topic or contested post against verified facts and the approved position; run the quality and anti-slop gates, correct any failure and rerun before handing the plan over.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Platform fit decision | Client owner | States clearly whether X fits the confirmed audience, with the alternative platform if not. |
| X channel plan: profile, content types, frequency and community tactics | Client owner and delivery team | Frequency matches stated capacity; EA media-ecosystem uses addressed where they apply. |
| 30-day plan: weekly rhythm, 4 full thread outlines, 20 single-post ideas, 8 poll ideas | Content owner | Every thread post drafted to near-final standard; every poll has four options. |
| KPI set with below-target actions | Client owner | Each KPI says what to do when it falls short. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Fit-check record | Short table: audience, goal, verdict, alternative | Completed before the full plan is written. |
| Position and verification log for live or contested topics | Table: topic, facts verified, source, approver | No live-topic post drafted for release without verified facts and sign-off. |
| Monthly KPI record | Table from native Analytics | Baseline Month 1 recorded; changes explained. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Posts on political or contested topics also need the client's approved position and sign-off.

## Degraded Mode

Without a confirmed audience on X, return the narrowest qualified result and mark the affected checks `not assessed`. A fit assessment with a recommended alternative platform can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A live topic is relevant but facts remain unverified | Monitor or draft; do not post until verification | Fast public misinformation |
| No account exists or analytics are not accessible | Produce a set-up plan with assumptions labelled | False optimisation against invented history |
| Analytics show an established account | Prioritise measured gaps and keep what already works | Destructive reset of working assets |
| A character limit, image size, feature or analytics location is time-sensitive | Verify it against official X help before stating it | Stale platform advice |
| The client sells FMCG, retail, food and beverage or beauty to the general consumer market | Keep X secondary; put reach into Facebook, WhatsApp and TikTok | Effort spent on the wrong audience |
| The client is B2B, a professional service, media, NGO or public-facing organisation | Treat X as strategically important alongside WhatsApp | Missing the region's public-discourse channel |
| A regulated-industry client faces a breaking issue on X | Respond within the hour: acknowledge, explain the facts, state what is being done; route to `playbook-crisis-communications` | Defensive posts that break reputation fastest |
| The client can post only a little each day | Build the plan for that capacity, not five posts a day | A plan the team abandons |

## Quality Standards

- An explicit platform suitability check comes before the full plan; if X is not right for the client's audience, the plan states this clearly and recommends the correct platform.
- The 4 thread outlines are complete post by post, written or drafted to near-final standard.
- The 20 single-post ideas are specific and ready to use with light editing, not generic prompts.
- The 8 poll ideas carry all four answer options and fit the client's industry and EA context.
- Community tactics reflect the EA media ecosystem: journalist engagement, public-sector monitoring and NGO relevance where applicable.
- The EA market context is applied throughout, not confined to one section: every content type and frequency recommendation reflects who actually uses X in Uganda, Kenya and Tanzania.
- KPI explanations are actionable: they tell the client what to do when a metric is below target, not just what the metric measures.
- Posting frequency is calibrated to the client's stated capacity: a client who can post twice per day receives a plan built for twice per day, not five times.

## Anti-Patterns

- "Great point!" replies. Fix: reply with a specific insight, example or respectful counter-perspective.
- Following in bulk and then unfollowing. Fix: engage with an account's content before following.
- Mentioning accounts arbitrarily for reach. Fix: mention only accounts that would find the content genuinely useful.
- Filler bio phrases ("passionate about", "change-maker", "disrupting the space"). Fix: state keywords, value proposition, location and one link or CTA.
- Numbers in the handle. Fix: add a location suffix such as @BrandKampala or @BrandUG.
- Quoting to agree vaguely. Fix: quote only to add something concrete.
- Promotional language in newsworthy posts aimed at journalists. Fix: post specific, verifiable facts and tag relevant journalists and media houses.

## References

- [X (Twitter) channel playbook](references/x-channel-playbook.md): read when checking fit, collecting the intake, setting up the profile, choosing content types and frequency, writing threads, planning community and media relations, drafting the 30-day plan or setting KPIs.
- [`playbook-crisis-communications`](../../playbooks/playbook-crisis-communications/SKILL.md): read when a live issue or backlash needs a response.
- [`playbook-pr-publicity`](../../playbooks/playbook-pr-publicity/SKILL.md): read when the job becomes press releases or media pitching.
- [`strategy-channel-architecture`](../../strategy/strategy-channel-architecture/SKILL.md): read when X fails the fit check and the overall platform mix needs deciding.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting posts, threads and bios.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and spelling.
<!-- dual-compat-end -->

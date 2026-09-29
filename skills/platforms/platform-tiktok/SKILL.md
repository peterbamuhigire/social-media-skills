---
name: platform-tiktok
description: 'Use when a brand is deciding whether and how to use TikTok: account choice, native short-video ideas, sounds and music rights, creator participation, and when to put money behind posts; produces the TikTok channel plan with a pilot and measures; not for a video approach across several platforms (use `strategy-video-content`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# TikTok Presence Plan

Decides whether TikTok fits the client's audience and offer and, if it does, plans native video, rights, creator participation and paid tests, for the client owner and delivery team.

<!-- dual-compat-start -->
## Use When
- The client is unsure whether TikTok fits its audience and offer and wants a clear decision.
- The brand needs native TikTok video ideas grounded in evidence, not reposted adverts.
- Sounds, music rights, duets, stitches and creator participation need rules before the account goes live.
- The client wants to know when a TikTok post is worth paid testing and how results will be judged.

## Do Not Use When
- `strategy-video-content` for video formats, series and scripts shared across platforms.
- `training-smartphone-video-production` for teaching staff to film and edit on a phone.
- `playbook-paid-social-advertising` for full TikTok ad campaigns.
- Stop before posting, using licensed music or paying for promotion without client authority and confirmed rights.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Audience evidence, buyer situation, commercial objective and follow-up route | Approved brief or client interview | Yes | Stop; do not assume an East African age profile, humour preference or video length. |
| Original assets and production capacity | Client marketing lead | Yes | Plan only concepts the team can produce truthfully; name the capacity gap. |
| Account analytics and existing videos | Account admin or supplied audit | Conditional | Mark the baseline `not assessed` and return an account decision and set-up plan. |
| Account types, link controls, commercial music, ads, Shop and creator programmes in the intended country | Official TikTok help or the account itself | Conditional | Record each as `NOT_ASSESSED`; never import historical menus, regional rollouts or eligibility thresholds from a book. |
| Commercial rights for music, footage, likenesses and creator material | Rights holder or creator, in writing | Before any production | Hold the asset; trending audio is not permission. |

## Workflow

1. Confirm objective, buyer, decision owner and permission boundary; stop if the objective or owner is missing, or if the job is a cross-platform video approach (`strategy-video-content`).
2. Decide whether TikTok fits, from researched language, devices and context for the actual audience; record the verified account features and what remains NOT_ASSESSED.
3. Develop a small number of distinct concepts and recurring series from real customer questions, quality distinctions, process demonstrations and useful comparisons, using the [native video, rights and testing method](references/tiktok-native-video-rights-and-testing-method.md).
4. Brief each video: opening shot, supporting evidence, sequence, voice/sound, captions, on-screen text, ending and destination.
5. Clear rights and Duet/Stitch settings before any response format is suggested.
6. Set a sustainable cadence and a thirty-day plan of concepts, evidence, production tasks, owners, destinations and review dates.
7. For a paid test, confirm availability, authorisation, offer economics, landing page, event quality, lead routing, budget cap and stopping rules.
8. Run the quality and anti-slop gates; correct any failed check and rerun it before handing the plan over for approval.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| TikTok fit decision and account set-up record | Client owner | Decision cites audience evidence; every feature is verified or marked NOT_ASSESSED. |
| Concept and series plan with video briefs | Delivery team; `training-smartphone-video-production` for filming | Each episode has its own source and point; no invented transformations, origin stories or controversy. |
| Thirty-day production plan and paid-test design | Client owner; `playbook-paid-social-advertising` for full campaigns | Owners, destinations and review dates named; paid test has a budget cap and stopping rules. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Feature and eligibility log | Table: feature, country/account, source, date, status | Each entry verified or NOT_ASSESSED. |
| Rights register | Table per music track, footage, likeness and creator asset | Commercial right recorded before production. |
| Pilot measurement record | Table: retention/attention, qualified destination actions, accepted leads, sales, returns, contribution | Windows, denominators, deduplication and tracking gaps stated. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Using licensed music and paying for promotion also need confirmed rights.

## Degraded Mode

Without audience evidence or verified account features, return the narrowest qualified result and mark the affected checks `not assessed`. A fit assessment with named evidence gaps and a concept shortlist can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A trend conflicts with the brand, audience or safeguarding duty | Skip it and use a native format built around the offer | Trend chasing that damages trust |
| No account exists or analytics are not accessible | Produce an account set-up plan with assumptions labelled | False optimisation against invented history |
| Analytics show an established account | Prioritise measured gaps and keep what already works | Destructive reset of working assets |
| An account type, music, ads, Shop or creator-programme feature is time-sensitive | Verify it in the intended country/account before stating it | Stale platform advice |
| Duet or Stitch is proposed to answer a claim | Verify availability, settings and reuse rights; avoid repeating the unverified claim while debunking it | Amplifying misinformation and rights breaches |
| A trend lifts views but attracts buyers outside the service area | Retain the learning, revise audience/offer clarity and judge qualified outcomes before scaling | Scaling attention that cannot buy |
| A native split or lift tool is offered | Use it only with current eligibility and a valid study design | Treating tool availability as proof of incrementality or sufficient sample size |

## Quality Standards

- The fit decision rests on researched audience language, devices and context, not regional stereotypes.
- Each video opens with a real reason to watch and fulfils that promise; product or method is shown clearly and stories are true.
- Distinct concepts are tested before cosmetic variations; length and pacing are tested for comprehension.
- Captions are accurate and key visuals readable; rights are recorded for every sound, likeness and creator asset.
- The thirty-day plan names concepts, evidence, production tasks, owners, destinations and review dates rather than a fixed quota.
- Paid tests separate creative response from profitable customer acquisition.
- A premium plan passes only when its creative can be produced truthfully, its rights are clear and its next step can be delivered.

## Anti-Patterns

- Requiring a universal three-second rule or forced cuts at fixed intervals. Fix: test length and pacing for comprehension.
- Treating a few missed days as a verified distribution reset. Fix: set cadence from quality, staffing and audience evidence.
- Lowering the quality bar to keep a posting streak. Fix: publish fewer, better-evidenced videos.
- Assuming a phone recording beats studio production, or the reverse. Fix: match polish to brand and context.
- Inventing customer transformations, origin stories, controversy or local cultural details. Fix: give each episode a real source and point.
- Imposing universal completion, share or monthly growth thresholds. Fix: judge against the account's own baseline and qualified outcomes.

## References

- [TikTok native video, rights and testing method](references/tiktok-native-video-rights-and-testing-method.md): read when deciding the account, developing concepts and series, checking rights, planning production and paid tests, or setting measures.
- [Channel creative and service lab](../../pipeline/06-digital-marketing-strategy/references/channel-creative-and-service-lab.md): read when planning production, creators, community, paid readiness and commercial measurement.
- [`strategy-video-content`](../../strategy/strategy-video-content/SKILL.md): read when the video approach spans several platforms.
- [`playbook-paid-social-advertising`](../../playbooks/playbook-paid-social-advertising/SKILL.md): read when a paid test becomes a full TikTok campaign.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting scripts, captions and on-screen text.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and spelling.
<!-- dual-compat-end -->

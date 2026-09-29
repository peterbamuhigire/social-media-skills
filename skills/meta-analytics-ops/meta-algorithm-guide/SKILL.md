---
name: meta-algorithm-guide
description: Use when a client asks why organic reach fell, what Facebook, Instagram, TikTok, YouTube, LinkedIn or X currently rank, or when and how often to post in EAT; produces the platform ranking guide, pre-publication checklist and posting-time schedule; not for designing controlled experiments (use `meta-testing-framework`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Platform Algorithm Guide — Organic Reach Reference

An operational reference, not a strategy document: ranking signals, penalised behaviours, favoured formats and posting benchmarks for the six primary platforms used in the East African market, with a pre-publication checklist to run before every post. For platform-specific strategy, use the relevant `platform-*` skill.

<!-- dual-compat-start -->
## Use When

- Organic reach or views have fallen, for example halved on the Facebook page, and the client wants to know what each platform's feed rewards and penalises right now and which posting habits to drop.
- The team wants a checklist to run before every post: format, opening seconds, watch time, links and engagement bait.
- The client asks when to post and how often on each platform, in East Africa Time, and wants a weekly posting schedule.
- A four-week posting-time test should replace guesses about the best hours and frequency.
- The ranking reference is out of date after a platform change and must be refreshed from dated sources.

## Do Not Use When

- `meta-testing-framework` for a controlled experiment with hypothesis, sample size and decision rule.
- `11-content-calendar` for filling the editorial calendar once the posting schedule is agreed.
- `platform-instagram` (or the matching platform skill) for a full channel operating plan.
- Stop before stating a ranking signal without a dated source; mark it unverified.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry, country/city and primary goal (reach growth, engagement rate, team training or reach recovery) | Client brief | Yes | Default to Uganda / Kampala; ask the goal question before ranking advice is prioritised. |
| Active platforms, current posting frequency per platform and primary content format | Client or account owner | Yes | Cover all six platforms and label the frequency comparison provisional. |
| Native analytics with timestamped post performance (90+ days where possible) | Client-authorised Meta Business Suite, Instagram, LinkedIn, TikTok, YouTube exports or screenshots | For a posting schedule | Use the EA baseline windows labelled provisional; replace with native data as soon as it exists. |
| Dated first-party platform guidance for each ranking claim | Platform help centres, creator or newsroom posts, source register | Yes | Mark the signal unverified; never state it as current. |
| Team size and production capacity | Client lead | Yes | Set frequency at the platform minimum until capacity is confirmed. |

## Workflow

1. Collect the intake answers ([platform ranking reference](references/platform-ranking-reference.md) § Intake questions) and confirm which decision is needed: reach diagnosis, pre-publication checklist, or posting schedule.
2. Check each ranking signal you will cite against a dated first-party source; stop and mark any signal without one as unverified rather than stating it.
3. For reach diagnosis, compare the client's recent posts with the platform's signals, engagement window, favoured formats and penalised behaviours (Sections 1–4 and 7 of the reference) and name the habits to drop.
4. Apply East African context: data costs, video length, captions, evening Wi-Fi viewing and WhatsApp distribution (Section 6 of the reference).
5. For a posting schedule, read native analytics first, set frequency per platform and run the 4-week test in [posting-time and frequency tests](references/posting-time-and-frequency-tests.md); use EA baseline windows only when no prior analytics exist.
6. Issue the pre-publication checklist (Section 8 of the reference) in a form a producer can print or pin.
7. Run the anti-slop gate and the quality standards below; correct any undated signal, generic cross-platform advice or strategy bleed and rerun the check before hand-over. Withhold release while a ranking claim has no date.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Platform algorithm guide (signals, engagement windows, formats, frequency, penalised behaviours) | Client lead and content team | Each platform names its unique primary signal; every signal carries a source date or `unverified`. |
| Pre-publication checklist | Content producer | Covers fundamentals, format and upload, algorithm signals, penalised behaviours and the first 30–60 minutes after posting. |
| Weekly posting schedule (day, EAT time, platform, format, pillar, direction) | Client lead; `11-content-calendar` | Every cell populated; analytics source, review trigger and WhatsApp cap noted below the table. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Ranking-signal source log | Table: platform, signal, source, date | No signal presented as current without a dated first-party source. |
| Posting-time test record | Table: week, variable, five metrics, decision | Week 4 decision follows the adopt / maintain / revert rule; baseline windows labelled provisional. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Reading native analytics needs client-authorised access, and the guide never posts or schedules on the client's behalf.

## Degraded Mode

Without dated platform guidance or the client's native analytics, return the narrowest qualified result and mark the affected checks `not assessed`. The pre-publication checklist and a schedule built on provisional EA baseline windows can still be delivered, with each undated signal labelled unverified.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A ranking signal has no dated first-party source | Mark it unverified and stop before stating it as current platform behaviour. | Advice built on outdated or invented ranking claims. |
| The client needs a client-specific posting time and frequency schedule | Run the native-analytics read, frequency check and 4-week test in [posting-time and frequency tests](references/posting-time-and-frequency-tests.md). | Schedules copied from global "best time" articles. |
| The account has fewer than 90 days of analytics | Use the EA baseline windows, labelled provisional, and replace them when native data exists. | Stalling, or presenting defaults as findings. |
| A post carries an outbound link on Facebook, LinkedIn or X | Move the link to the first comment (or a reply on X) and say so in the post. | Suppressed reach for posts that send users off-platform. |
| Content exists on another platform | Upload natively; never post a YouTube link on Facebook when the goal is reach. | Linked or duplicate content ranked below native uploads. |
| Video is aimed at mobile-data audiences | Keep TikTok and Reels under 45 seconds and educational YouTube under 10 minutes unless the audience is Wi-Fi-dominant; add captions. | Abandoned views that hurt the completion-rate signal. |
| The goal is guaranteed reach to existing customers | Use WhatsApp broadcast lists and Status to drive traffic to the platform post, not to replace it. | Treating WhatsApp replies as platform ranking signals. |
| Engagement falls after a burst of posting | Return to a consistent weekly cadence the team can sustain. | Posting in bursts, which lowers algorithmic trust. |

## Quality Standards

- Platform specificity: every platform section names its unique primary signal (completion rate for TikTok, saves for Instagram, watch time for YouTube), not generic advice for all platforms.
- EA market grounding: data-cost constraints, WhatsApp distribution logic and EAT peak times are built into the guidance, not appended as an afterthought.
- Checklist usability: a content producer can print the Section 8 checklist or pin it to their screen and use it without reading the full document.
- Penalised behaviours are specific: each names the platforms affected and explains the mechanism of penalisation, not just that it "hurts reach".
- Engagement windows are actionable: Sections 3 and 6.1 give specific EAT times, not "post when your audience is active".
- The formats table is decision-ready: a producer knows which format to prioritise from Section 4 without further research.
- No strategy bleed: the guide does not recommend content pillars, audience personas or brand voice, which belong in the relevant strategy skills; it stays operational.
- British English throughout (organisation, behaviour, favoured, recognise, analyse); no American spellings.

## Anti-Patterns

- Recommending posting times from global benchmark articles. Fix: read native analytics and run the 4-week test in [posting-time and frequency tests](references/posting-time-and-frequency-tests.md).
- Stating a ranking signal as current from memory or an undated blog. Fix: cite a dated first-party source or label it unverified.
- Engagement bait ("Like if you agree", "Tag 3 friends to win"). Fix: give the audience a genuine reason to comment, save or share.
- Hashtag stuffing (30 tags on every post). Fix: stay within 3–5 on LinkedIn and at most 5 on Instagram, the platform cap since 18 Dec 2025 (register `INSTAGRAM-HASHTAG-LIMIT-PRIMARY`), all relevant.
- Posting and going offline straight away. Fix: respond to every comment within 30 minutes of posting.
- Giving one "post X times a week" instruction across all channels. Fix: set frequency per platform at the level full quality can hold.
- Publishing or scheduling on a live account during review. Fix: hand the guide and schedule over; posting needs separate authority.

## References

- [Platform ranking reference](references/platform-ranking-reference.md): read when collecting intake, explaining per-platform ranking signals, engagement windows, favoured formats, frequency benchmarks (Section 5), EAT peak times (Section 6.1), data costs, WhatsApp, penalised behaviours or the pre-publication checklist (Section 8).
- [Posting-time and frequency tests](references/posting-time-and-frequency-tests.md): read when setting posting times, frequency per platform, the 4-week test or a weekly posting schedule.
- [`meta-testing-framework`](../meta-testing-framework/SKILL.md): read when a controlled experiment with hypothesis, sample size and decision rule is needed.
- [`11-content-calendar`](../../pipeline/11-content-calendar/SKILL.md): read when the agreed schedule is ready to fill the editorial calendar.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the guide and checklist.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

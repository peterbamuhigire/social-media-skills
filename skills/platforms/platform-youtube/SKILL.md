---
name: platform-youtube
description: 'Use when a brand wants a YouTube channel people find through search: set-up, video types, titles and descriptions for YouTube search, Shorts, Community posts and upload rhythm; produces the YouTube channel plan with a 30-day content plan and KPIs; not for video formats shared across all platforms (use `strategy-video-content`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# YouTube Channel Strategy

Plans a business YouTube channel for East African viewers who use YouTube mainly for research, tutorials and entertainment: set-up, searchable video, Shorts and Community posts at a cadence the client can sustain.

<!-- dual-compat-start -->
## Use When
- The client wants to start or revive a YouTube channel and needs set-up, branding and playlists sorted.
- Videos are not found in search and need titles, descriptions, tags and thumbnails planned for YouTube SEO.
- The client wants a video mix, Shorts and Community posts at an upload cadence it can sustain.
- A 30-day upload plan and YouTube-specific KPIs are needed, with blog angles drawn from each video.

## Do Not Use When
- `strategy-video-content` for video formats, podcasts or AI-avatar video across platforms.
- `training-smartphone-video-production` for filming and editing skills.
- `platform-tiktok` for short video planned for TikTok first.
- Stop before uploading, changing channel settings or switching on monetisation without the channel owner's authority.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client and trading name, industry, products/services, country/city and primary goal | Approved brief or client interview | Yes | Default the market to Uganda/East Africa; stop the plan if the goal is unknown. |
| Target audience: who they are, the problems they are solving and what they search for | Client and search research | Yes | Build the first month from Hygiene content on the client's most frequent customer questions and label the audience as provisional. |
| Topics the client has genuine expertise in | Client practitioners | Yes | Limit the plan to those topics; do not invent authority. |
| Realistic videos per month | Client production lead | Yes | Scale the 4 long-form + 8 Shorts month down to the stated capacity. |
| Channel stats (subscribers, average views, top 3 videos by watch time) and reusable footage | YouTube Studio or supplied audit | Conditional | Set Month 1 as the baseline and mark the channel audit `not assessed`. |
| Current dimensions, feature thresholds and YPP terms | Official YouTube help | Conditional | Flag each figure for live verification before it goes to the client. |

## Workflow

1. Confirm goal, audience, owner and permission boundary; stop if the goal or owner is missing, or route to `strategy-video-content` for a cross-platform video approach.
2. Apply the EA market context and Hero/Hub/Hygiene model from the [YouTube channel playbook](references/youtube-channel-playbook.md): prioritise searchable Hygiene content first.
3. Set up channel art, icon, About section, trailer, playlists, end screens and cards (§1).
4. Match video types to the client's expertise and goals (§2), then apply title, description, tags, captions, thumbnail and chapter guidance (§3).
5. Set cadence and the private-first upload workflow (§4), the Shorts plan (§5) and Community posts once the tab is available (§6).
6. Draft the 30-day plan with a title, three-sentence brief, thumbnail concept and CTA for every entry (§7).
7. Set KPIs with watch time and average view duration as the primary signals (§8), and apply the algorithm notes to upload workflow, CTA placement and playlists (§9).
8. Run the quality and anti-slop gates; correct any failed check and rerun it before handing the plan over.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Channel set-up specification | Channel owner | Dimensions, safe zone, About copy, trailer structure, playlists and end-screen template stated. |
| Video type mix and SEO guidance applied to each video | Content producer | Every long-form title follows the playbook §3 title structure (primary keyword, benefit, brand). |
| 30-day content plan (4 long-form + 8 Shorts, scaled to capacity) | Content producer; `training-smartphone-video-production` for filming | Every entry has a title, three-sentence brief, thumbnail concept and CTA. |
| KPI set and blog post angles | Client owner; `blog-writer` | Each KPI says why it matters; angles target specific audience pain points. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Platform figure verification log | Table: figure, source, date | Dimensions, the Community tab threshold, Shorts length and YPP terms verified or flagged. |
| Monthly KPI record | Table from YouTube Studio | Top 3 videos by watch time identified; Shorts and long-form tracked separately. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Uploading, changing channel settings and switching on monetisation need the channel owner's authority.

## Degraded Mode

Without confirmed expertise topics and production capacity, return the narrowest qualified result and mark the affected checks `not assessed`. A channel set-up specification and a Hygiene topic shortlist can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The query needs a durable explanation | Use a searchable long-form video and derive Shorts afterwards | Short-lived clips with no depth |
| No channel exists or YouTube Studio is not accessible | Produce a channel set-up plan with assumptions labelled | False optimisation against invented history |
| Studio data shows an established channel | Prioritise measured gaps and keep what already works | Destructive reset of working assets |
| A dimension, threshold, Shorts length or YPP rule is time-sensitive | Verify it against official YouTube help before stating it | Stale platform advice |
| The channel is new | Prioritise Hygiene (searchable tutorials, FAQs) in the first 30 days; layer in Hub series once an audience forms | A series with no search foundation |
| Viewers are data-cost-sensitive | Place the primary CTA before the 3-minute mark, reward first | Viewers leaving before the ask |
| A B2B or professional channel considers the YouTube Partner Programme | Weigh competitor advertisements on the videos against revenue; the channel need not be monetised to be commercially valuable | Competitor ads at the moment of highest intent |
| A video has low CTR on impressions | Test a new thumbnail on the existing video before re-uploading | Losing the video's accumulated history |

## Quality Standards

- All ten playbook sections are complete with no placeholders; the 30-day plan has a full title, three-sentence brief, thumbnail concept and CTA for every entry.
- Every long-form title follows the `[Primary keyword] — [Benefit] | [Brand]` format.
- Video types match the client's stated expertise and goals; a service business receives more testimonial and behind-the-scenes recommendations than product showcase videos.
- Video lengths and topics reflect the EA context: shorter video preference, mobile-first viewing, data-cost sensitivity and YouTube as a research tool.
- The Hero/Hub/Hygiene framework is correctly applied: the plan prioritises searchable Hygiene content in the first 30 days before layering in Hub series.
- Shorts are positioned as trailers and repurposed content, integrated with long-form, not a separate workstream.
- KPI explanations say why each metric matters, not just what it measures.
- All production guidance is achievable with a smartphone and basic lighting; the plan does not assume studio production capability.

## Anti-Patterns

- Misleading thumbnails and clickbait titles. Fix: match thumbnail and title to the content; "Not interested" clicks train the algorithm against the whole channel.
- Publishing with incomplete metadata. Fix: upload as Private, complete title, description, tags, chapters, end screens and cards, then publish or schedule.
- Irregular uploading after a weekly start. Fix: commit to a cadence the team can hold and pre-schedule two weeks ahead.
- Saving the CTA only for the end screen. Fix: deliver the most useful insight first, then ask before the 3-minute mark.
- Pivoting channel topics abruptly. Fix: keep topic coherence and add new topics through related playlists.
- Optimising titles in English only. Fix: test bilingual titles for Luganda, Swahili or Kinyarwanda keyword gaps.

## References

- [YouTube channel playbook](references/youtube-channel-playbook.md): read when collecting the intake, setting up the channel, choosing video types, applying SEO guidance, setting cadence, Shorts and Community posts, drafting the 30-day plan, setting KPIs, applying the algorithm notes or picking blog angles.
- [`strategy-video-content`](../../strategy/strategy-video-content/SKILL.md): read when the video approach spans several platforms.
- [`platform-tiktok`](../platform-tiktok/SKILL.md): read when short video is planned for TikTok first.
- [`blog-writer`](../../content-writing/blog-writer/SKILL.md): read when turning a blog angle into an article.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting titles, descriptions and scripts.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and spelling.
<!-- dual-compat-end -->

---
name: playbook-content-production
description: 'Use when a team must make the photos, videos and graphics for social: shoot and design briefs, shot lists, batch shoot days, quality standards, or an AI-assisted drafting workflow with prompts and disclosure; produces the production briefs, shoot checklist and AI content workflow; not for deciding what goes out when (use `11-content-calendar`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Content Production Playbook

Produces the photography, video and graphic design briefs, the batch shoot-day plan and checklist, the content quality standard and, where AI drafts copy, the AI-assisted production workflow, with East African light and bandwidth defaults.

<!-- dual-compat-start -->
## Use When
- Decide how posts get made each week: who drafts, who designs, who approves and when photo shoots are batched.
- A photography, video or graphic design brief with shot lists, dimensions, lighting and brand elements for the photographer, videographer or designer.
- Plan a batch shoot day so one session gives several weeks of posts, with a shoot checklist and the editing and scheduling that follow.
- Decide how the team uses ChatGPT, Claude or Canva to draft captions and ideas: a brand context block, prompts, checks on AI-drafted copy and an AI disclosure rule.
- Posts look inconsistent; every asset needs a quality standard to pass before it is scheduled.
- Reacting to trends quickly without losing the brand voice or skipping approval.

## Do Not Use When
- `11-content-calendar` for the dated 90-day schedule of posts.
- `training-smartphone-video-production` for teaching staff to shoot and edit on a phone.
- `caption-writer` for writing the captions themselves.
- Stop before publishing AI-generated or identifiable customer material without disclosure, consent and the client's approval; deliver the assets for review.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, business type and country/city | Client | Yes | Default to Uganda/East Africa; ask for the business type before writing the shot list. |
| Shoot date, location and team members available (names and roles) | Client | Yes | Write the briefs undated and mark the batch plan provisional. |
| Platforms the content is for | Channel plan or `11-content-calendar` | Yes | Brief every key scene in landscape and portrait and flag the dimension table `not assessed` for unlisted platforms. |
| Products or services to feature and any campaign or seasonal moment | Client | Yes | Stop the shot list; request the specific products rather than writing a generic list. |
| Brand colours (hex) and fonts | Brand guide or `04-brand-voice-intake` | Yes | Describe colours in words and mark the design brief for brand confirmation. |
| Brand context block, pillars and maturity stage (for AI drafting) | `04-brand-voice-intake`, `10-content-pillars` | If AI tools draft copy | Run brand voice calibration before any AI content is generated. |

## Workflow

1. Run the intake questions in [production briefs and batch shoot](references/production-briefs-and-batch-shoot.md); stop if the products or platforms are unknown.
2. Write the photography brief: scene descriptions, an 8–12 shot list tailored to the client, East African lighting windows (07:00–09:00 or 16:30–18:00 EAT) and the do's and don'ts.
3. Write each video brief: duration target by platform, dialogue option, B-roll list, mandatory captions, CTA spoken and on screen, and branding.
4. Write each graphic design brief: platform dimensions, headline of 6 words or fewer, text hierarchy, brand elements and the 10% safe area.
5. Plan the batch shoot day (prepare, morning photography, midday video, afternoon behind-the-scenes, post-shoot review, editing and scheduling 2–3 days after) and issue the printable shoot checklist, including written permission from non-team people in frame.
6. If AI drafts captions or ideas, apply the [AI-assisted production workflow](references/ai-assisted-production-workflow.md); for trend-led posts, use the [real-time content bridge](references/real-time-content-bridge-and-voice.md).
7. Apply the content quality standard (Share or Solve, six story characteristics, Think Like a Publisher) to every asset; correct and rerun any asset that fails before it goes to the client for review.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Photography brief with shot list | Photographer or team lead | 8–12 scene-specific shots tailored to the client's products; both orientations for key scenes. |
| Video briefs | Videographer and editor | Complete B-roll list; captions stated as mandatory; CTA spoken and shown. |
| Graphic design briefs | Graphic designer | Platform dimensions table and a clear text hierarchy; brand hex codes and fonts named. |
| Batch shoot plan and printable checklist | Shoot team | Time blocks add up to a full working day; checklist usable on the day. |
| AI content workflow (where AI drafts copy) | Content team | Brand context block, prompts, quality control and disclosure rule present. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Consent record | Table: person, shoot date, written permission held | Every non-team person in frame has written permission before use. |
| Asset quality check | Checklist per asset | Each asset passes Share or Solve and the six characteristics, or is returned for rework. |
| Dimension and spec check | Table with source and date | Each dimension is confirmed against the platform's current help centre or marked `not assessed`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Loading assets into Buffer or Hootsuite is followed by client review before publishing begins.

## Degraded Mode

Without the shoot date, platforms and product list, return the narrowest qualified result and mark the affected checks `not assessed`. Brief templates, the lighting windows and the shoot checklist can still be delivered for the client to complete.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A content item lacks source, owner or approval | Hold it out of production. | Untraceable or unauthorised publishing. |
| AI tools (ChatGPT, Canva, CapCut) draft captions, ideas or repurposed posts, or AI output contains an unsupported claim or generic filler | Apply the AI-assisted production workflow: brand context block, core prompts, six-check quality control and hallucination gate; return failing output to evidence and editorial review. | Fast production of generic or misleading AI content. |
| An outdoor shoot is planned in Uganda/East Africa | Schedule 07:00–09:00 or 16:30–18:00 EAT; avoid 10:00–14:00; shoot video indoors or in shade at midday. | Harsh equatorial shadows and blown-out highlights. |
| A person who is not a team member appears in frame | Obtain written permission before the shoot or exclude them. | Using identifiable people without consent. |
| An asset neither solves a problem nor is worth sharing | Do not publish it. | Content that only shows the brand exists. |
| A platform dimension or duration is taken from the table | Confirm it against the platform's current specification before briefing. | Assets cropped or rejected by the platform. |

## Quality Standards

- The photography shot list has 8–12 scene-specific shots tailored to the client's product or service, not a generic list.
- The video brief has a complete B-roll list and states captions as mandatory.
- The graphic design brief has the platform dimensions table and a clear text hierarchy.
- Batch workflow steps carry realistic time blocks that add up to a full working day.
- Platform dimensions are current and accurate at the time of briefing.
- Lighting guidance is specific to equatorial sun timing and golden-hour windows in EAT.
- The shoot checklist is formatted for printing and use on the day.
- All content uses British English; no American spellings.

## Anti-Patterns

- Shooting one orientation and assuming it covers every platform. Fix: shoot every key scene in landscape (16:9) and portrait (9:16 or 4:5).
- Checking images only on the camera display. Fix: review on a laptop or large screen before the team disperses.
- Publishing video without captions. Fix: add captions through CapCut, YouTube auto-caption (checked and corrected) or an SRT file.
- Stiff posed group photos and stock-style imagery. Fix: direct real team members and customers to do the thing naturally.
- More than two font families or off-palette colours in a graphic. Fix: use brand fonts and palette; seek approval for exceptions.
- Using AI to answer a reputational incident. Fix: route to `playbook-crisis-communications`; no AI drafting there.

## References

- [Production briefs and batch shoot](references/production-briefs-and-batch-shoot.md): read when running intake, writing photo, video or design briefs, checking durations and dimensions, planning a batch shoot, printing the checklist or applying the quality standard.
- [AI-assisted production workflow](references/ai-assisted-production-workflow.md): read when AI tools draft captions, content ideas, hashtags or repurposed posts, or when staging a client on the AI content maturity model.
- [Real-time content bridge and voice contract](references/real-time-content-bridge-and-voice.md): read when producing timely content through the listen/verify/adapt/approve/publish/measure bridge, or keeping several contributors in one intent-led, distinctive human voice.
- [`11-content-calendar`](../../pipeline/11-content-calendar/SKILL.md): read when confirming which content the next 4–6 weeks need.
- [`caption-writer`](../../content-writing/caption-writer/SKILL.md): read when writing the captions for the finished assets.
- [`training-smartphone-video-production`](../../training/training-smartphone-video-production/SKILL.md): read when staff need to learn phone shooting and editing.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when AI has drafted any copy.
- [East African English standard](../../language/east-african-english/SKILL.md): read when checking spelling and tone.
<!-- dual-compat-end -->

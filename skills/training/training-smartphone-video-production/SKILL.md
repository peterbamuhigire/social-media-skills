---
name: training-smartphone-video-production
description: 'Use when staff or a client team must film and edit on their own phones: light, sound, framing, camera settings, editing in CapCut or InShot, export for Reels, TikTok and YouTube, and uploading on low data; produces the phone filming training guide with practice drills; not for deciding what videos to make (use `strategy-video-content`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Smartphone Video Production Training Guide

Produces a skimmable, jargon-free phone filming guide for Uganda and East African field conditions (Android phones, equatorial sun, noisy markets, patchy data), putting light and audio before kit and effects.

<!-- dual-compat-start -->
## Use When

- Our videos are dark, shaky or have noisy sound and we have no budget for a crew.
- Staff need to know which cheap kit to add (lapel mic, tripod, ring light) to the phones they already have.
- Teach framing, camera settings and vertical versus horizontal shooting for each platform.
- Show how to edit simply on the phone, then export and upload on slow or costly data.

## Do Not Use When

- `strategy-video-content` for video series, hooks, scripts and what to publish.
- `training-client-team` for the wider social-media handover workshop.
- `training-social-media-fundamentals` for beginners' social-media basics.
- Stop before filming customers, patients or children without recorded consent or release forms.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name, industry and country/city | Client lead | Yes | Default to Uganda/Kampala and use generic retail, NGO or hospitality examples. |
| Primary goal: what the team will film (product demos, testimonials, behind-the-scenes, tutorials) | Client lead or `strategy-video-content` output | Yes | Cover talking-head and product shots and ask before adding specialist drills. |
| Platforms in use (TikTok, Reels, WhatsApp Status, YouTube, Facebook) | Client lead | Yes | Teach 9:16 vertical first and keep the full platform table. |
| Team skill level (complete beginners, some experience, confident) | Client lead or pre-session check | Yes | Assume complete beginners and explain every technical term on first use. |
| Smartphone models in use (Samsung, Tecno, Itel, Infinix, iPhone) | Participants | If known | Give generic Android menu paths and have trainees find the setting on their own phones. |
| Consent or release forms for any customer, patient or child on camera | Client owner | If people are filmed | Film staff, products and spaces only. |

## Workflow

1. Run the intake in [phone-video-training-guide.md](references/phone-video-training-guide.md) and route "what should we film" questions to `strategy-video-content`.
2. Set the East African field-conditions context, then write Section 1 on equipment already owned and cheap add-ons, with UGX prices.
3. Write Sections 2–3 (lighting, audio) as the priority topics, each with a free fix before any purchase.
4. Write Sections 4–6 (framing, camera settings, platform formats) matched to the platforms in use.
5. Write Sections 7–8 (phone editing in CapCut, InShot or VN; export; low-bandwidth upload) and Section 9 on common mistakes.
6. Add a capture-to-export practice drill on the trainees' own phones; stop any drill that would film customers, patients or children without recorded consent.
7. Check the guide against the Quality Standards and `anti-ai-slop`, block release on an F from `ai-slop-audit`; correct any failing section and rerun the check before hand-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Phone filming training guide, Sections 1–9 | Client staff and trainer | Every instruction can be applied at the next shoot with no purchase needed for the core guidance. |
| Capture-to-export practice drill | Trainees | Each trainee films, tests audio, edits and exports one 1080p, 30fps, H.264 clip on their own phone. |
| Platform format and file-size table | Staff uploading content | Matches only the platforms in use, with orientation, length and upload size targets. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Practice clip record | Clip per trainee with a short checklist (light, audio, framing, export) | Each clip is reviewed against the checklist, not only "shot". |
| Platform and price check | Table of specs, file limits and UGX prices with date checked | Each figure is dated or marked `not assessed`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Filming identifiable customers, patients or children needs recorded consent or a release form.

## Degraded Mode

Without the team's platforms and phone models, return the narrowest qualified result and mark the affected checks `not assessed`. The lighting, audio, framing and common-mistakes sections can still be delivered, as they need no specific device or platform.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Learners need production competence with available phones and field conditions | Practise a complete capture-to-export exercise using the actual device constraints | Advice assumes professional gear or reliable studio conditions |
| Budget allows one upgrade | Recommend a lapel microphone (UGX 15,000–40,000) before a ring light or gimbal | Money spent on kit while audio still ruins the video |
| Filming outdoors between 10am and 3pm | Move to open shade, wait for cloud or film at golden hour (7–9am or 4–6pm) | Harsh shadows that editing cannot fix |
| Storage or upload data is limited | Shoot 1080p, not 4K; compress to the platform file-size target and upload on Wi-Fi | Stalled uploads and failed posts |
| Speech includes Luganda or Swahili | Add captions manually with the Text tool, not auto-captions | Wrong captions on local-language speech |
| A platform spec, file limit or UGX price conflicts with a current source | Keep the guide figure, flag it for the trainer to confirm on the day, and mark it `not assessed` | Trainees exporting to a spec the platform no longer accepts |
| A drill would post practice clips to the client's live accounts | Keep clips on the phone or a shared folder; posting needs client authority | Unapproved practice footage published |

## Quality Standards

- **Locally grounded**: all equipment prices are in UGX, all examples reflect Uganda/EA shooting conditions, and app recommendations work on the Android devices most EA creators use.
- **Immediately actionable**: every instruction can be applied on the next filming session with no additional purchases required for the core guidance.
- **Platform-specific**: framing, orientation, length, and export settings are matched precisely to each platform the client uses.
- **Audio and lighting prioritised**: the guide makes clear that lighting and audio deliver the highest return on a beginner's attention; equipment and effects are secondary.
- **Jargon-free**: all technical terms (EIS, aspect ratio, bitrate, H.264) are explained in plain language on first use.
- **Honest about constraints**: upload limitations, storage limitations, and low-bandwidth conditions are addressed directly with practical workarounds, not glossed over.
- **Concise and skimmable**: section headings, tables, and short paragraphs allow a busy team member to find specific guidance quickly without reading the full document; British English throughout.
- **Error-prevention focused**: the Common Mistakes section addresses the specific failures most likely to occur in EA field conditions, not generic global advice.

## Anti-Patterns

- Filming with the window or light source behind the subject. Fix: always face the light.
- Neglecting audio. Fix: use a lapel microphone and record a 10-second test with earphones before every session.
- Rotating the phone mid-recording. Fix: set vertical or horizontal before pressing record.
- Using digital zoom. Fix: walk closer, or accept the wider sharp framing.
- Over-editing with spinning transitions and layered effects. Fix: simple cuts and clean text overlays.
- Recommending a DSLR, gimbal or studio lights to a team with phones. Fix: start with the rear camera, a tripod or stack of books, and window light.

## References

- [phone-video-training-guide.md](references/phone-video-training-guide.md): read when running intake or writing the field-conditions context and Sections 1–9, including the platform format table, export settings and file-size targets.
- [`strategy-video-content`](../../strategy/strategy-video-content/SKILL.md): read when the team must decide what videos to make, hooks and scripts.
- [`training-client-team`](../training-client-team/SKILL.md): read when phone filming is one module of a wider handover workshop.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the guide copy.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read when scoring the finished phone video guide before release.
- [AGENTS.md](../../../AGENTS.md): read when checking repository-wide doctrine.
<!-- dual-compat-end -->

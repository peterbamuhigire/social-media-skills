---
name: meta-content-repurposing
description: Use when one proven blog, video, podcast or webinar must become many platform-ready pieces, or old posts should be refreshed and rotated as evergreen; produces the repurposing map, an AI-assisted ten-asset pipeline or a 90-day evergreen rotation; not for judging past post performance (use `meta-content-audit`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Content Repurposing Plan

Turns one proven source piece into many platform-native outputs through a three-tier Content Factory, so a single investment of research, filming or writing fills 7–10 platform slots and cuts production cost by 60–70% compared with creating original content for every platform. Every output is an adaptation, never the same copy pasted across platforms.

<!-- dual-compat-start -->
## Use When

- A strong article, video, podcast or webinar should be cut into reels, carousels, quote cards, threads and WhatsApp messages.
- The client wants one long piece turned into ten platform-ready assets with AI prompts and a human quality check in under an hour.
- Old posts that still answer real questions should be scored, refreshed and put on a 90-day rotation.
- An interview or session is about to be recorded and should be captured so it can be reused widely.

## Do Not Use When

- `meta-content-audit` for judging which past posts worked and what to retire.
- `11-content-calendar` for the master publishing calendar.
- `blog-writer` for writing a new long-form article from scratch.
- Stop before reusing material the client has no rights to adapt; flag it for permission.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Approved source assets (blog, video, podcast, webinar, article) with performance data | Client library and native analytics | Yes | Stop; ask for the highest-performing piece of the last 30 days rather than repurposing an untested one. |
| Rights to adapt each source (music, guests, stock, third-party material) | Client or content owner | Yes | Flag the asset for permission and leave it out of the plan. |
| Platforms in scope | Client brief | Yes | Default to Facebook, Instagram, TikTok and WhatsApp and mark the rest `not assessed`. |
| Existing content types the client already produces | Client | Yes | Recommend starting with a video or audio recording, which gives the widest content tree. |
| Content production capacity (hours per week) | Client lead | Yes | Plan for one social media manager with a phone and a scheduling tool. |
| Client name, industry, country/city and primary goal | Client brief | Yes | Default to Uganda / Kampala; pick worked examples from the nearest industry. |

## Workflow

1. Collect the intake ([Content Factory and repurposing chains](references/content-factory-and-repurposing-chains.md) § Intake questions); stop before using any material the client has no rights to adapt, and route performance judgements to `meta-content-audit`.
2. Choose the branch: a source piece to cut into derivatives (this skill), one written source to ten AI-assisted assets ([AI-assisted recycling pipeline](references/ai-assisted-recycling-pipeline.md)), an archive to rotate ([evergreen register and rotation](references/evergreen-register-and-rotation.md)), a recording still to be made ([capture for repurposing](references/capture-for-repurposing.md)), or a launch or topic cluster ([repurposing for launch and clusters](references/repurposing-for-launch-and-clusters.md)).
3. Map the source into Tier 1, Tier 2 and Tier 3 outputs and check each combination against the platform repurposing matrix.
4. Write the repurposing chain for each source piece, naming the content title, extraction approach and platform-native adaptation; include at least one chain from the client's own industry.
5. Remove anything on the what-not-to-repurpose list (trend content, time-sensitive posts, platform-specific calls to action, below-average performers, personal one-offs).
6. Set the output rhythm with the 1-7-30-4-2-1 cadence and the Monday-to-Friday weekly workflow, feeding the slots into `11-content-calendar`.
7. Run the quality standards and anti-slop gate; correct any slot that duplicates another platform's copy and rerun the check. Withhold release while a rights or duplication defect remains.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Repurposing map (Content Factory tiers and matrix for the platforms in scope) | Client lead; social media manager | Three tiers distinguished with their logic; matrix complete for every platform in scope, non-viable combinations marked honestly. |
| Repurposing chains per source piece | Social media manager; designer | Each chain names title, extraction approach and platform-native adaptation; no two slots share verbatim copy. |
| Weekly repurposing workflow and production sequence | Social media manager; `11-content-calendar` | Monday-to-Friday sequence with realistic timing and no resources beyond a phone and a scheduling tool. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Source performance and rights log | Table: source, engagement vs client average, rights status | Every source is at or above the client's average engagement rate and has confirmed rights, or is excluded. |
| Duplication check | Table: slot, platform, adaptation made | No slot is the same copy pasted with a different header. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Scheduling the finished assets in a live tool is a separate, authorised step.

## Degraded Mode

Without approved source assets and their performance data, return the narrowest qualified result and mark the affected checks `not assessed`. The Content Factory model, the matrix for the platforms in scope and a capture plan for the next recording can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client wants to identify, refresh and schedule durable posts from an existing archive (evergreen register, 90-day rotation) | Follow [evergreen-register-and-rotation](references/evergreen-register-and-rotation.md): screen, score, refresh, rotate; feed refreshed posts back into the repurposing chain. | Republishing dated content or producing everything new. |
| One long-form written source (500–1,500 words) must become ten platform assets quickly with AI assistance | Follow [ai-assisted-recycling-pipeline](references/ai-assisted-recycling-pipeline.md): fix the human approval gate, run the ten prompts, apply platform rules and the quality gate. | Raw AI output published unreviewed or duplicated across platforms. |
| A draft slot repeats another platform's copy | Treat it as a QC failure and rewrite it for that platform's constraints, tone and audience; never post identical content cross-platform. | Duplication passed off as repurposing. |
| The source piece is someone else's content, or an output only restitches clips or adds a watermark | Repurpose only the client's own or rights-cleared material, and transform each output with new commentary, voiceover or editing; on Facebook, repeated unoriginal reposting loses reach and monetisation (registers `META-UNORIGINAL-CONTENT-2025`, `PREMIUM-META-ORIGINAL-2026`) | Distribution penalties and rights claims |
| The source piece performed below the client's average engagement rate | Leave it out of the repurposing cycle. | Recycling what did not work. |
| No Tier 1 piece is scheduled this week | Repurpose the highest-performing piece of the last 30 days. | An empty week or filler posts. |
| The client has limited production time | Start from a video or audio recording. | A narrow content tree from a text-only source. |
| A post carries a platform-specific call to action ("swipe up", "link in bio") or is time-sensitive | Rewrite the CTA for the destination platform; do not repurpose time-sensitive posts. | Misleading or broken calls to action. |

## Quality Standards

- The Content Factory model distinguishes the three tiers and explains the hierarchy's logic, not just a list of platforms.
- The platform repurposing matrix is complete for every platform in the client's scope, with non-viable combinations marked honestly.
- Worked examples are specific: they name the content title, the extraction approach and the platform-native adaptation.
- At least one worked example is relevant to the client's actual industry.
- The weekly workflow is actionable for a single social media manager: realistic timing, clear sequence, no resources beyond a phone and a scheduling tool.
- "What not to repurpose" gives clear criteria, not vague cautions; the 60–70% cost reduction principle is stated and tied to the model.
- No platform slot duplicates another platform's copy verbatim; each is a genuine adaptation.
- British English throughout; no American spellings.

## Anti-Patterns

- Cutting a blog post's paragraphs into carousel slides, or stripping hashtags from the Facebook caption for WhatsApp. Fix: adapt each output to the platform's format, tone and length.
- Recycling an evergreen post without the refresh protocol. Fix: run the refresh checklist in the evergreen reference before it re-enters the chain.
- Repurposing a viral-sound TikTok for LinkedIn or WhatsApp. Fix: keep trend content on its home platform.
- Publishing raw AI output. Fix: pass every AI-drafted asset through the human approval gate in the pipeline reference.
- Recording an expert session with no plan for reuse. Fix: follow the capture reference before recording.
- Reusing third-party music, guests or images without permission. Fix: confirm rights or drop the asset.

## References

- [Content Factory and repurposing chains](references/content-factory-and-repurposing-chains.md): read when collecting intake, applying the Repurposing Chain (Nemo, 2017), the 1-7-30-4-2-1 cadence (Handley, 2012), the three tiers, the platform matrix, the ten worked chains, the weekly workflow, what not to repurpose, or the Hero/Hub/Hygiene and Meerman Scott (2022) framing.
- [Capture for repurposing](references/capture-for-repurposing.md): read before recording an interview or session that will be repurposed, or when designing an expert-minimum content service.
- [AI-assisted recycling pipeline](references/ai-assisted-recycling-pipeline.md): read when one long-form source must become ten platform-ready assets with AI prompts, a platform rules table and a human quality gate in under 60 minutes.
- [Evergreen register and rotation](references/evergreen-register-and-rotation.md): read when identifying, scoring, refreshing and scheduling evergreen content from an existing library into a 90-day rotation.
- [Repurposing for launch and clusters](references/repurposing-for-launch-and-clusters.md): read when repurposing must support a campaign, funnel or topic cluster rather than just produce more posts.
- [`11-content-calendar`](../../pipeline/11-content-calendar/SKILL.md): read when placing evergreen and repurposing slots in the master calendar.
- [`meta-content-audit`](../meta-content-audit/SKILL.md): read when judging which past posts worked before choosing sources.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting derived copy.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

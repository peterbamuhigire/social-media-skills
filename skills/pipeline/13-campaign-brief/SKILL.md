---
name: 13-campaign-brief
description: Use when an approved campaign must be handed to the team, agency or suppliers with every asset, spec, deadline and sign-off spelled out; produces the operational campaign brief with deliverables, owners, deadlines and approvals; not for finding the insight and creative idea (use `creative-brief-and-big-idea`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Campaign Brief Generator

Produces the operational handover brief that tells the execution team exactly what to make, to what specifications, by when and to whose approval; `09-campaign-strategy` decides what campaign to run. Apply `east-african-english` for tone throughout.

<!-- dual-compat-start -->
## Use When

- Campaign strategy is approved and designers, videographers, printers or content creators need one handover document listing each asset to make, its sizes, the deadline and who signs it off.
- Each deliverable needs specifications, platform sizes, copy, and brand do's and don'ts.
- The team needs a timeline with deadlines, owners and an approval chain before work starts.
- Content claims, sources and image or music rights must be recorded before assets go out.

## Do Not Use When

- `creative-brief-and-big-idea` for the insight, the creative idea and the creative review.
- `09-campaign-strategy` when the campaign's objective, message and channels are not yet decided.
- `ad-copy-and-hook-lab` for writing the ad headlines and hooks themselves.
- Stop before issuing the brief to suppliers or committing spend without the named approver's sign-off.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Approved campaign strategy: campaign name, dates (with teaser and analysis windows), key message | `09-campaign-strategy` or client sign-off | Yes | Stop; route to `09-campaign-strategy` rather than deciding strategy here. |
| Target persona | `03-audience-personas` | Yes | Name the persona gap; mark channel fit `NOT_ASSESSED`. |
| Deliverables required, with quantities | Approved strategy or client lead | Yes | List only what the strategy names; do not assume every channel or format is in scope. |
| Team and partner names and roles, first reviewer and final approver | Client lead or account manager | Yes | Use role titles and note "Assign names at kickoff meeting." |
| Budget per deliverable type (UGX) | Client | Yes | Leave the budget lines blank with a kickoff note; do not invent rates. |
| Brand voice guide and approved brand assets | `04-brand-voice-intake`; client | Yes | Hold the do's and don'ts and any graphic specification until the guide is supplied. |

## Workflow

1. Confirm the intake answers in [brief-document-sections](references/brief-document-sections.md) § Intake questions (Country/city defaults to Kampala, Uganda); stop and route to `09-campaign-strategy` if objective, message or channels are undecided.
2. Write sections 1–4 (background and objective, target audience with channel evidence, one-sentence key message, campaign concept).
3. Build the deliverables table and per-deliverable specifications from current official sources through the platform skills; omit and mark `NOT_ASSESSED` any specification that cannot be verified.
4. Write campaign-specific brand do's and don'ts, the full-lifecycle timeline and the approval process, including what happens when feedback is late.
5. Set one primary and three supporting KPIs with baselines and targets.
6. Complete the [reader-first content brief](references/reader-first-content-brief.md) and [content evidence and rights record](references/content-evidence-and-rights-record.md) for each production unit. Quarantine unsupported claims, missing rights, mismatched destinations or unassessed review states.
7. Record the Five Outcomes for each deliverable; return any failed deliverable to its strategy, content or design owner, correct it and rerun the gate.
8. Run the anti-slop ship gate; stop before issuing the brief to suppliers or committing spend without the named approver's sign-off.

## Five Outcomes gate before sign-off

Canonical reference: `docs/ux-foundations.md` Section 3.

For each outcome below, record `pass`, `fail` or `NOT_ASSESSED` and cite the evidence. A failed outcome blocks the affected deliverable. Do not treat missing audience, source, approval or render evidence as a pass.

| # | Outcome | Campaign-specific verification |
|---|---|---|
| 1 | **Useful** | The campaign addresses the persona's stated goal (not a vanity metric like "more followers") |
| 2 | **Easy** | The intended audience can identify the message and next action from the reviewed asset; no universal seconds threshold |
| 3 | **Efficient** | The required information remains understandable in the tested delivery context; provide an equivalent text route where needed |
| 4 | **Pleasing** | Visual quality matches the approved brand direction, assessed against the actual rendered asset |
| 5 | **Accessible** | Useful image descriptions, accurate captions or text alternatives, readable contrast checked against the applicable standard, and clear language |

The sign-off wording template is in [brief-document-sections](references/brief-document-sections.md) § Five Outcomes.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Ten-section campaign brief | Designers, copywriters, videographers, printers; client approver | Any qualified team member could act on it without further explanation; no unexplained placeholders. |
| Deliverables table with specification sources | Production team | Every required asset listed with placement, format, official source and access date (or `NOT_ASSESSED`), quantity, due date and owner. |
| Timeline and approval process | Account manager; client approver | Kickoff to post-campaign report covered; late-feedback and emergency sign-off rules stated. |
| Five Outcomes record per deliverable | Final approver | Every applicable outcome is `pass` with cited evidence before the deliverable ships. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Specification source log | Table: platform, placement, source, source date or version, access date, recheck trigger | Each technical value traces to a current official source or is omitted and marked `NOT_ASSESSED`. |
| Content evidence and rights record | One record per content unit | Every claim, image and music item has a source or rights entry; gaps are quarantined. |
| Accessibility and render review | Caption, alt text, contrast and native-size preview notes | Recorded against a rendered asset before production approval; no render means `NOT_ASSESSED`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Issuing the brief to suppliers or scheduling content needs the named approver's sign-off.

## Degraded Mode

Without an approved campaign strategy or current platform specifications, return the narrowest qualified result and mark the affected checks `not assessed`. Background, audience, key message, concept, timeline skeleton and approval process can still be drafted for kickoff.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A technical specification cannot be verified from the official current source for the exact platform, account and placement | Omit the value, mark it `NOT_ASSESSED` and leave it out of the executable handoff. | Assets built to stale sizes, durations or limits copied from an old brief. |
| Audience evidence for a proposed channel is absent | Mark channel fit `NOT_ASSESSED`; do not infer preference or reach from Uganda/East Africa location alone. | Channel choices built on stereotype. |
| A unit has no approved offer, working destination or response owner | Leave the CTA out of that unit. | CTAs that lead nowhere or go unanswered. |
| Spoken or audio-dependent video | Require reviewed captions or an equivalent text alternative, tested in the intended placement. | Inaccessible video; captions mistaken for disclosure. |
| The client or approver misses the feedback window | Move the timeline by the same number of days, note it to the client and pause production. | Guessing what the client wants. |
| A time-sensitive reactive post inside the campaign | Allow account-manager approval on the client's voice note, with written confirmation within 24 hours. | Missed moments or unapproved posts. |
| A Five Outcomes check fails or lacks evidence | Block that deliverable; return it to its owner or keep `NOT_ASSESSED` and withhold release. | Shipping unreviewed or failing assets. |
| Objective, message or channels are not yet decided | Route to `09-campaign-strategy` and hand over the verified inputs already collected. | Strategy decided inside an execution brief. |

## Quality Standards

- All ten sections are present and complete; no section is left blank or contains a placeholder without a note explaining what must be filled in at kickoff.
- The deliverables table accounts for every asset mentioned in the Required Input; nothing is omitted.
- Each technical platform specification has current official-source and intended-placement evidence, or is omitted and marked `NOT_ASSESSED`.
- Spoken or audio-dependent video has reviewed captions or an equivalent text alternative; rendered accessibility and native-size preview evidence are recorded before production approval.
- The key message is one sentence only and is clearly distinct from the campaign slogan or tagline.
- Brand do's and don'ts are campaign-specific and reference the client's actual brand voice, not generic rules applicable to any campaign.
- The timeline table covers the full lifecycle from kickoff to post-campaign report, with realistic sequencing between review and production stages, and the approval process states what happens when feedback is late (ambiguity here is a common cause of campaign delays).
- Success metrics include baselines and targets; a KPI without a target is not a KPI.

## Anti-Patterns

- Copying fixed dimensions or character limits from an old brief. Fix: route specifications through the platform skills and verify the official source.
- Forcing a word count, hashtag quota or CTA onto every unit. Fix: give each unit one audience need and one communication job.
- Writing the slogan as the key message. Fix: state the strategic truth in one sentence, then two sentences on what it achieves and asks.
- Implying a visual has been reviewed when no render exists. Fix: record alt text, contrast and render review with the design owner.
- Partial, drip-fed client feedback. Fix: the first reviewer returns consolidated feedback within the agreed working days.
- Using unlicensed images or music. Fix: use only approved brand assets and licensed or owned media, logged in the rights record.
- Issuing the brief to suppliers before sign-off. Fix: wait for the named approver; spend needs separate authority.

## References

- [Campaign brief document method](references/brief-document-sections.md): read when asking the intake questions, writing the ten sections, filling the deliverables, timeline, approval and KPI tables, or recording the Five Outcomes wording.
- [Reader-first content brief](references/reader-first-content-brief.md): read for each content unit handed from strategy to production.
- [Content evidence and rights record](references/content-evidence-and-rights-record.md): read before approving any content unit with claims, images or music.
- [Synthetic Ugandan small-retailer discussion example](examples/synthetic-retail-discussion-unit.md): read to see channel adaptation and evidence boundaries; it is not an approved strategy, a complete campaign brief, or authority to publish.
- [`09-campaign-strategy`](../09-campaign-strategy/SKILL.md): read when objective, message or channels are not yet decided.
- [`creative-brief-and-big-idea`](../../advertising/creative-brief-and-big-idea/SKILL.md): read when the insight or creative idea is missing.
- [`ad-copy-and-hook-lab`](../../advertising/ad-copy-and-hook-lab/SKILL.md): read when the ad headlines and hooks must be written.
- [Facebook](../../platforms/platform-facebook/SKILL.md), [Instagram](../../platforms/platform-instagram/SKILL.md), [LinkedIn](../../platforms/platform-linkedin/SKILL.md) and [TikTok](../../platforms/platform-tiktok/SKILL.md) platform skills: read when sourcing current specifications.
- [Finished campaign exemplars](../../../docs/world-class-exemplars/campaign-exemplars.md): read when checking the finished standard.
- [Creative review gate](../../../docs/quality-gates/creative-review-gate.md): read before creative sign-off.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->
